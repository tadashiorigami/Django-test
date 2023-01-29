from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import SequenceForm
from .lr_model import get_lr_model, round_number, regression_xy
import re
from plotly.offline import plot
from plotly.graph_objs import Scatter


# Create your views here.
def post_list(request):
    coefs = ""
    x_message = None
    y_message = None
    x_sequence = ''
    y_sequence = ''
    form = ""
    excel_formula = ""
    python_formula = ""
    plot_div = ""
    rmse = 0
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SequenceForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            x_sequence = form.cleaned_data['x_sequence']
            x_sequence = [float(s) for s in re.findall(r'-?\d+\.?\d*', x_sequence)]
            y_sequence = form.cleaned_data['y_sequence']
            y_sequence = [float(s) for s in re.findall(r'-?\d+\.?\d*', y_sequence)]
            degree = int(form.data['degree'])
            for number in x_sequence:
                if x_message == None:
                    x_message = f"{number}"
                else:
                    x_message = f"{x_message}, {number}"
            for number in y_sequence:
                if y_message == None:
                    y_message = f"{number}"
                else:
                    y_message = f"{y_message}, {number}"

            if len(x_sequence) == len(y_sequence):
                coefs, rmse = get_lr_model(x_sequence, y_sequence, degree)
                rmse = round_number(rmse, 4)
                min(x_sequence)
                x, y = regression_xy(coefs, min(x_sequence), max(x_sequence))

                
                plot_div = plot([Scatter(x=x, y=y,
                                    opacity=0.8, marker_color='red', name = 'Regression line'),
                                Scatter(x=x_sequence, y=y_sequence,
                                        opacity=0.8, marker_color='green', name = 'Input',
                                        mode='markers')],
                                output_type='div')


                for i in range(len(coefs)):
                    coef = round_number(coefs[i], 4)
                    coef = f"+ {coef}" if coef >= 0 else f"{coef}"
                    p = len(coefs)-1-i
                    if p > 1:
                        excel_formula = f"{excel_formula} {coef} * x^{p}"
                        python_formula = f"{python_formula} {coef} * x**{p}"
                    elif p == 1:
                        excel_formula = f"{excel_formula} {coef} * x"
                        python_formula = f"{python_formula} {coef} * x"
                    else:
                        excel_formula = f"{excel_formula} {coef}"
                        python_formula = f"{python_formula} {coef}"

                
                
                # slope = f"+ {slope}" if slope >= 0 else f"{slope}"
                # intercept = f"+ {intercept}" if intercept >= 0 else f"{intercept}"
                
            else:
                form.add_error('y_sequence', 'X and Y has different lengths')

            # sequence = sequence.replace(" ", ",")
            # sequence = sequence.replace("\n", ",")
            # sequence = re.sub(pattern, ', ', sequence)
            # sequence = sequence.split(",")
            # sequence = [float(x.strip()) for x in sequence]

    return render(request, 'blog/post_list.html', {'coefs': coefs,
                                                   'form' : form,
                                                   'rmse' : rmse,
                                                   'excel_formula' : excel_formula,
                                                   'python_formula' : python_formula,
                                                   'x_message' : x_message,
                                                   'y_message': y_message,
                                                   'x_sequence' : x_sequence,
                                                   'y_sequence': y_sequence,
                                                   'plot_div': plot_div})