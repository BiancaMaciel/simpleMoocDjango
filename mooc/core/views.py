#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request, 'home.html')


def contact(request):
	return render(request, 'contact.html')