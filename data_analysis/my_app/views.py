from django.shortcuts import render,get_object_or_404,redirect
import os
import pandas as pd
from bokeh.io import output_file,show
from bokeh.plotting import figure
from my_app.forms import Plotform
from my_app.models import plot_information
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
class home(TemplateView):
    template_name='index.html'

def graph_info(request):
    if request.method=="POST":
        form=Plotform(request.POST,request.FILES)
        print("hey") 
        if form.is_valid():
          print("hey")
          plots=form.save(commit=False)
          print(plots.data_file)
          print(plots.title)
          if plots.data_file in request.FILES:
              print("xyz")
              plots.data_file=request.FILES['data_file']
          plots.save()

          return redirect('plot',pk=plots.pk)
        # return HttpResponse("Invalid info")
    else:
        form=Plotform()
  

    return render(request,'graph_info.html',{'Plotform':form})

def plot(request,pk):
   plot=get_object_or_404(plot_information,pk=pk)
   df=pd.read_csv(os.path.join('media/',str(plot.data_file)))
   df=df.dropna(how='any')
   X=plot.x_col
   Y=plot.y_col
   p=figure()
   p.circle(df.iloc[:,X],df.iloc[:,Y],size=10)
   #return redirect('home')
   output_file('a.html')
   show(p)
   


