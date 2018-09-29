import json
import requests

from django.http import HttpResponse
from django.http import JsonResponse

from app.traceip.models import TraceIp

from urllib.parse import urljoin

def traceipfromget(request):
	try:
		get_ip = request.GET.get('ip')
		request_by_ip	= request.META['REMOTE_ADDR']
		# import pdb; pdb.set_trace()
		if get_ip:
			DOMAIN = "ip-api.com/json/"
			BASE_URL = "http://"

			url = BASE_URL + DOMAIN + get_ip
			headers = {
				'Accept': 'application/json'
			}
			response = requests.get(
				url,
				headers=headers
			)
			entry_in_db = TraceIp.objects.create(request_by_ip=request_by_ip,searched_for_ip=get_ip)
			print(entry_in_db)
			return JsonResponse({"ip_details" : response.json()})
		else:
			message = "ip is not provided"
			return JsonResponse({"status" : False, "message" : message})

	except Exception as err:
		print("Oops we met some error : ", str(err))
		return JsonResponse({"status" : 'False',"error" : str(err)})