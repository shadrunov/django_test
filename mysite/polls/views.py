from django.http import HttpResponse
from django.shortcuts import render
from openpyxl import Workbook, load_workbook
from .xls2db import process_sheet


# Create your views here.

def process(request):
    wb = load_workbook("template.xlsx")
    process_sheet(wb)
    return HttpResponse("Done")

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
