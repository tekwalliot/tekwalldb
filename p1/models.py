from django.db import models

# Create your models here. 

class CustomerDetails(models.Model):
	Name 		= models.CharField(max_length=50, unique=True, null=True, help_text='Company Name')
	Nick_Name 	= models.CharField(max_length=20, unique=True, null=True, help_text='Company Nick Name')
	Address		= models.CharField(max_length=200, blank=True, null=True, help_text='Company Address')
	GST_No		= models.CharField(max_length=20, blank=True, null=True, help_text='Company GST Number if Available')

	def __str__(self):
		return self.Name 



class ContactDetails(models.Model):
	Company_Name 	= models.ForeignKey(CustomerDetails, on_delete=models.CASCADE)
	Person_Name 	= models.CharField(max_length=30, null=True, help_text='Contact Person Name')
	Email 			= models.EmailField(max_length=50, null=True, blank=True)
	Phone_Number	= models.CharField(max_length=20, null=True)
	Designation 	= models.CharField(max_length=30, null=True, blank=True, help_text='Person Designation')
	Other_Info 		= models.CharField(max_length=200, null=True, blank=True, help_text='Other Information if any')

	def __str__(self):
		return self.Person_Name


class Orders(models.Model): 
	Company_Name 	= models.ForeignKey(CustomerDetails, on_delete=models.CASCADE)
	Order_Details   = models.TextField(max_length=500, null=True, blank=True)
	Order_Value		= models.FloatField(max_length=10, null=True, blank=True, help_text='Order Value or Estimated Value')
	Is_Confirmed	= models.BooleanField(default=False, help_text='Order is Confirmed or in Pipe Line')
	Order_No		= models.CharField(max_length=30, null=True, blank=True, help_text='Received PO No')
	Order_Date 		= models.DateField(blank=True, null=True, help_text='Purchase Order Date')
	Order_RefName	= models.ForeignKey(ContactDetails, on_delete=models.CASCADE, help_text='PO reference person name')
	po_by = (('By PO', 'By PO'), ('By Mail', 'By Mail'), ('By Phone', 'By Phone'))
	Order_Through 	= models.CharField(max_length=20, choices=po_by, blank=True, null=True)
	Is_Completed	= models.BooleanField(default=False, help_text='tick if completed')

	def __str__(self):
		return str(self.Order_Date)+'-'+self.Company_Name.Name+'-'+str(self.Order_Value)


class Purchase(models.Model):
	PO_Details    	= models.TextField(max_length=500, null=True, blank=True)
	PO_Value		= models.FloatField(max_length=10, null=True, blank=True, help_text='PO Value')
	PO_No		 	= models.CharField(max_length=30, null=True, blank=True, help_text='Received PO No')
	PO_Date 		= models.DateField(blank=True, null=True, help_text='Purchase Order Date')
	po_type 		= (('GST Purchase', 'GST Purchase'), ('Cash Purchase', 'Cash Purchase'))
	PO_Type 		= models.CharField(max_length=20, choices=po_type, blank=True, null=True)
	Tax				= models.FloatField(max_length=10, null=True, blank=True, help_text='18/12/5/10/1/0.75/0/any other tax')
	Is_With_Tax		= models.BooleanField(default=False, help_text='tick if tax included')
	PO_Copy 		= models.ImageField(upload_to='images', null=True, blank=True, help_text='Attach Purchase Order')

	def __str__(self):
		return str(self.PO_Date)+'-'+str(self.PO_Value)


class BillingDetails(models.Model):
	Company_Name 	= models.ForeignKey(CustomerDetails, on_delete=models.CASCADE)
	Bill_No		 	= models.CharField(max_length=30, null=True, blank=True, help_text='Bill/Invoice No if any')
	Bill_Date 		= models.DateField(blank=True, null=True, help_text='Purchase Date')
	Bill_Value		= models.FloatField(max_length=10, null=True, blank=True, help_text='Billing Value')
	bill_type 		= (('GST Bill', 'GST Bill'), ('TDS Bill', 'TDS Bill'), ('Cash', 'Cash'))
	Bill_Type 		= models.CharField(max_length=20, choices=bill_type, blank=True, null=True)
	Tax				= models.FloatField(max_length=10, null=True, blank=True, help_text='18/12/5/10/1/0.75/0/any other tax')
	Is_With_Tax		= models.BooleanField(default=False, help_text='Tick if tax included')
	Bill_Copy 		= models.ImageField(null=True, blank=True, help_text='Attach Bill/Invoice')

	def __str__(self):
		return self.Bill_No


class PaymentDetails(models.Model):
	Company_Name 	= models.ForeignKey(CustomerDetails, on_delete=models.CASCADE)
	Bill_No		 	= models.ForeignKey(BillingDetails, null=True, blank=True, on_delete=models.CASCADE)
	Payment_Date 	= models.DateField(null=True, help_text='Date of Payment')
	Paid_Value		= models.FloatField(max_length=10, null=True, blank=True, help_text='Billing Value')
	Next_Date 		= models.DateField(null=True, blank=True, help_text='next commitment date if available')
	Is_Cleared		= models.BooleanField(default=False, help_text='Fully Paid or Not')

	def __str__(self):
		return self.Company_Name.Name+'-'+str(self.Payment_Date)+'-'+str(self.Paid_Value)


class WorkProgress(models.Model):
	Company_Name 	= models.ForeignKey(CustomerDetails, on_delete=models.CASCADE)
	PO_Details		= models.ForeignKey(Orders, on_delete=models.CASCADE)
	Update_Date 	= models.DateField(null=True, help_text='Payment')
	Work_Progress	= models.IntegerField(null=True, blank=True, help_text='Work Progress %')
	Is_Completed	= models.BooleanField(default=False, help_text='Is Work Order Completed')
	Other_Info	    = models.TextField(max_length=500, null=True, blank=True)

	def __str__(self):
		return self.Company_Name.Name+'-'+str(self.Work_Progress)


class Expenses(models.Model):
	cat 			= (('Commission', 'Commission'), ('Transport', 'Transport'), ('Food', 'Food'), ('Furniture', 'Furniture'), ('Other', 'Other'))

	CompanyName 	= models.ForeignKey(CustomerDetails, on_delete=models.CASCADE, null=True, blank=True, help_text='If expenses towrds that particular company')
	Category 		= models.CharField(max_length=20, choices=cat, blank=True, null=True)
	Amount			= models.FloatField(max_length=10, null=True, blank=True, help_text='Expenses Value')
	Date 			= models.DateField(null=True, help_text='yyyy-mm-dd')
	Description	    = models.TextField(max_length=500, null=True, blank=True)
	Attach			= models.FileField(upload_to='expenses/', blank=True)

	def __str__(self):
		return str(self.Date)+'-'+self.Category+'-'+str(self.Amount)



