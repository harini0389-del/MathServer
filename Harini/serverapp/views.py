from django.shortcuts import render
def calculate_total(request):
	P=int(request.POST.get('Price',0))
	GST=int(request.POST.get('GST',0))
	total= P + (P *GST/100) if request.method=="POST" else 0
	print("Price=",P)
	print("GST=",GST)
	print("Total=",total)
	return render(request,'serverapp/side.html',{'P':P,'GST':GST,'total':total})