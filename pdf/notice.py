from datetime import datetime 
import csv 
import io 

from django.template.loader import get_template
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from xhtml2pdf import pisa

from .models import *
from web_super_admin.models import *