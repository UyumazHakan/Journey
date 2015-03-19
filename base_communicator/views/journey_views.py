__author__ = 'Hakan Uyumaz'


import http.client

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse