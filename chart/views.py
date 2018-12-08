from django.shortcuts import render
from django.http import HttpResponse

from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.dates import DateFormatter
import matplotlib.pyplot as plt

import random
import datetime

# Create your views here.
def showHistogram(request):
    return render(request, 'showlinediagram.html')

def showlinediagram(request):
    return render(request, 'chart/showlinediagram.html')

