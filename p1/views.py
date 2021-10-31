from django.shortcuts import render
from .forms import *
from django.contrib import messages
from datetime import date, datetime, timedelta 
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from .filters import *
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.  
# @login_required
def mainp(request):
	#Total Orders Value
	t_ord = Orders.objects.filter(Is_Confirmed=True)
	tOrders = 0
	for x in t_ord:
		tOrders = int(tOrders+x.Order_Value)

	#Recent Orders Value
	t_ordrec = Orders.objects.filter(Is_Confirmed=True, Order_Date__range=[(date.today()-timedelta(days=30)), (date.today())])
	tOrdersRec = 0
	for x in t_ordrec:
		tOrdersRec = int(tOrdersRec+x.Order_Value)

	#Total Received Payments
	t_recpay = PaymentDetails.objects.all()
	tPaid = 0
	for x in t_recpay:
		tPaid = int(tPaid+x.Paid_Value)

	#Recent Received Payments
	t_recrecpay = PaymentDetails.objects.filter(Payment_Date__range=[(date.today()-timedelta(days=30)), (date.today())])
	tPaidRec = 0
	for x in t_recrecpay:
		tPaidRec = int(tPaidRec+x.Paid_Value)

	#Pending Payments
	t_value = Orders.objects.filter(Is_Confirmed=True, Is_Completed=True)
	tValue = 0
	for x in t_value:
		tValue = int(tValue+x.Order_Value)
	pPay = tValue-tPaid

	#Pipeline Orders Value
	pipline = Orders.objects.filter(Is_Confirmed=False, Is_Completed=False)
	pOrders = 0
	for x in pipline:
		pOrders = int(pOrders+x.Order_Value)

	homelist = {'tOrders':tOrders, 'tOrdersRec':tOrdersRec,'tPaid':tPaid, 'tPaidRec':tPaidRec,  'pPay':pPay, 'pOrders':pOrders}

	return render(request, 'index.html', {'homelist': homelist})


def custform(request):
	if request.method ==  'POST':
		form = CustomerDetailsForm(request.POST)
		if form.is_valid():
			form.save()
			form = CustomerDetailsForm()
			messages.success(request, "Customer Details Has Been Added")
			return render(request, 'custform.html', {'form': form})
		else:
			messages.success(request, "Data is not valid")
	else:
		form = CustomerDetailsForm()
		return render(request, 'custform.html', {'form': form})


def ordersform(request):
	if request.method ==  'POST':
		form = OrdersForm(request.POST)
		if form.is_valid():
			form.save()
			form = OrdersForm()
			messages.success(request, "Order Details Has Been Added")
			return render(request, 'ordersform.html', {'form': form})
		else:
			messages.success(request, "Data is not valid")
	else:
		form = OrdersForm()
		return render(request, 'ordersform.html', {'form': form})

def expensesform(request):
	if request.method ==  'POST':
		form = ExpensesForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			form = ExpensesForm()
			messages.success(request, "Expenses Has Been Added")
			return render(request, 'expensesform.html', {'form': form})
		else:
			messages.success(request, "Data is not valid")
	else:
		form = ExpensesForm()
		return render(request, 'expensesform.html', {'form': form})

def expenses_update(request, expns_id):
	try:
		expnsdata=get_object_or_404(Expenses, id=expns_id)
		if request.method ==  'POST':
			form = ExpensesForm(request.POST, request.FILES, instance=expnsdata)
			if form.is_valid():
				form.save()
				form = ExpensesForm()
				messages.success(request, "Expenses Has Been Updated")
				return render(request, 'expensesform.html', {'form': form})
			else:
				messages.success(request, "Data is not valid")
		else:
			form = ExpensesForm(instance=expnsdata)
			update="True"
			return render(request, 'expensesform.html', {'form': form, 'update':update})
	except Exception as e:
	        return HttpResponse(e)


def orders(request):
	table = Orders.objects.all()
	filter_data = OrdersFilter(request.GET, queryset=table)
	table = filter_data.qs
	
	tOrders=0
	for x in table:
		if x.Is_Confirmed==True:
			tOrders = tOrders + x.Order_Value

	tOrdComp=0
	for x in table:
		if x.Is_Completed==True:
			tOrdComp = tOrdComp + x.Order_Value

	tOrdProg=0
	for x in table:
		if x.Is_Completed==False:
			tOrdProg = tOrdProg + x.Order_Value

	tOrdPipe=0
	for x in table:
		if x.Is_Confirmed==False:
			tOrdPipe = tOrdPipe + x.Order_Value

	ordset = {'tOrders':tOrders, 'tOrdComp':tOrdComp, 'tOrdProg':tOrdProg, 'tOrdPipe': tOrdPipe}

	return render(request, 'orders.html', {'table': table, 'filter_data':filter_data, 'ordset':ordset})


def expenses(request):
	table = Expenses.objects.all().order_by('Date')
	print(table)
	filter_data = ExpensesFilter(request.GET, queryset=table)
	table = filter_data.qs
	
	tExpenses=0
	for x in table:
		tExpenses = tExpenses + x.Amount
	tExpenses = int(tExpenses)

	tTransp=0
	transp = Expenses.objects.filter(Category='Transportation')
	for x in transp:
		tTransp = tTransp + x.Amount
	tTransp = int(tTransp)

	tOthers=0
	others = Expenses.objects.filter(Category='Others')
	for x in others:
		tOthers = tOthers + x.Amount
	tOthers = int(tOthers)

	tGenExpns=tExpenses-tTransp-tOthers


	expset = {'tExpenses':tExpenses, 'tTransp':tTransp, 'tGenExpns':tGenExpns, 'tOthers':tOthers}

	return render(request, 'expenses.html', {'table': table, 'filter_data':filter_data, 'expset':expset})



def payform(request):
	if request.method ==  'POST':
		form = PaymentDetailsForm(request.POST)
		if form.is_valid():
			form.save()
			form = PaymentDetailsForm()
			messages.success(request, "Payment Details Has Been Added")
			return render(request, 'payform.html', {'form': form})
		else:
			messages.success(request, "Data is not valid")
	else:
		form = PaymentDetailsForm()
		return render(request, 'payform.html', {'form': form})


def poform(request):
	if request.method ==  'POST':
		form = PurchaseForm(request.POST)
		if form.is_valid():
			form.save()
			form = PurchaseForm()
			messages.success(request, "Payment Details Has Been Added")
			return render(request, 'poform.html', {'form': form})
		else:
			messages.success(request, "Data is not valid")
	else:
		form = PurchaseForm()
		return render(request, 'poform.html', {'form': form})


def allpro(request):
	return render(request, 'index2.html')

class ChartData(View):
	def get(self, request):
		try:
			xaxis=[]
			y1=[]
			y2=[]
			y3=[]
			y4=[]

			x1 = []
			y5 = []

			ch_cust = Orders.objects.filter(Is_Confirmed=True)
			for x in ch_cust:
				cust_name = x.Company_Name.Nick_Name
				xaxis.append(cust_name) #Customers List
				xaxis = list(dict.fromkeys(xaxis)) #Delete Duplicate Names
				# comp_list.append(x.Company_Name.Name)
				# comp_list = list(dict.fromkeys(comp_list)) 

			for x in range(len(xaxis)):
				#Total Orders Value
				ch_tord = Orders.objects.filter(Company_Name__Nick_Name=xaxis[x], Is_Confirmed=True)
				tOrdVal = 0
				for a in ch_tord:
					tOrdVal = int(tOrdVal + a.Order_Value)
				y1.append(tOrdVal)
					 
				#Completed Work Received Payments (advance paymnet???)
				ch_recpay = PaymentDetails.objects.filter(Company_Name__Nick_Name=xaxis[x]) 
				RecPaid = 0
				for b in ch_recpay:
					if b.Paid_Value=='Null':
						b.Paid_Value = 0
					RecPaid = int(RecPaid + b.Paid_Value)
				y2.append(RecPaid)

				#Pending Work Payments
				ch_pwork = Orders.objects.filter(Company_Name__Nick_Name=xaxis[x], Is_Confirmed=True, Is_Completed=False) 
				pWorkPay = 0
				for c in ch_pwork:
					if c.Order_Value=='Null':
						c.Order_Value = 0
					pWorkPay = int(pWorkPay + c.Order_Value)
				y4.append(pWorkPay) 

			#Completed Work Pending Payments
			for x in range(len(y1)):
				ppay = y1[x]-y2[x]
				y3.append(ppay)
			return JsonResponse({'xaxis':xaxis, 'y1':y1, 'y2':y2,'y3':y3, 'y4':y4})
		except Exception as e:
			return JsonResponse({"error":str(e)})
