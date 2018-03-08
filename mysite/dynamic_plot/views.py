from django.shortcuts import render
import utils.plot_function as p
import utils.data_function as d

def homepage(request):
    data_list = d.create_data()
    bokeh_script, bokeh_div = p.bokeh_plot(data_list)

    return render(request, 'dynamic_plot/homepage.html', {'data_list': data_list,
                                                          'bokeh_script': bokeh_script,
                                                          'bokeh_div': bokeh_div})