from django.http import HttpResponse

def traceipfromget(request):
	tracedip = request.META['REMOTE_ADDR']
	return HttpResponse('<h1> Your Ip is : ' + tracedip + '</h1>')