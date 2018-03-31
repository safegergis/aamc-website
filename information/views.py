from django.shortcuts import render
from django.shortcuts import redirect
def ourchurch(request):
	return render(request,'information/ourchurch.html')
def fm(request):
	return render(request,'information/fm.html')
def yi(request):
	return render(request,'information/yi.html')
def mh(request):
	return render(request,'information/mh.html')
def fathers(request):
	return render(request,'information/fathers.html')
def d(request):
	return redirect('https://goo.gl/maps/bueQNCpHoMP2')
def schedule(request):
	return render(request, 'information/schedule.html')
