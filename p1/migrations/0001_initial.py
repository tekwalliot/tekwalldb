# Generated by Django 3.1.1 on 2021-09-03 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BillingDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BillNo', models.CharField(blank=True, help_text='Bill/Invoice No if any', max_length=30, null=True)),
                ('BillDate', models.DateField(blank=True, help_text='Purchase Order Date', null=True)),
                ('BillValue', models.FloatField(blank=True, help_text='Billing Value', max_length=10, null=True)),
                ('BillType', models.CharField(blank=True, choices=[('GST Bill', 'GST Bill'), ('TDS Bill', 'TDS Mail'), ('Cash', 'Cash')], max_length=20, null=True)),
                ('Tax', models.FloatField(blank=True, help_text='18/12/5/10/1/0.75/0/any other tax', max_length=10, null=True)),
                ('IsWithTax', models.BooleanField(default=False, help_text='Tax Included/Excluded')),
                ('Bill_Copy', models.ImageField(blank=True, help_text='Attach Bill/Invoice', null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='ContactDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PersonName', models.CharField(help_text='Contact Person Name', max_length=30, null=True)),
                ('Email', models.EmailField(blank=True, max_length=50, null=True)),
                ('PhoneNumber', models.CharField(max_length=20, null=True)),
                ('Designation', models.CharField(blank=True, help_text='Person Designation', max_length=30, null=True)),
                ('OtherInfo', models.CharField(blank=True, help_text='Other Information if any', max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(help_text='Company Name', max_length=50, null=True)),
                ('NickName', models.CharField(help_text='Company Nick Name', max_length=20, null=True)),
                ('Address', models.CharField(blank=True, help_text='Company Address', max_length=200, null=True)),
                ('GST_No', models.CharField(blank=True, help_text='Company GST Number if Available', max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrderDetails', models.TextField(blank=True, max_length=500, null=True)),
                ('OrderValue', models.FloatField(blank=True, help_text='Order Value or Estimated Value', max_length=10, null=True)),
                ('Is_Confirmed', models.BooleanField(default=False, help_text='Order is Confirmed or in Pipe Line')),
                ('Order_No', models.CharField(blank=True, help_text='Received PO No', max_length=30, null=True)),
                ('Order_Date', models.DateField(blank=True, help_text='Purchase Order Date', null=True)),
                ('Order_Through', models.CharField(blank=True, choices=[('By PO', 'By PO'), ('By Mail', 'By Mail'), ('By Phone', 'By Phone')], max_length=20, null=True)),
                ('CompanyName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p1.customerdetails')),
                ('Order_RefName', models.ForeignKey(help_text='PO Reference Person Name', on_delete=django.db.models.deletion.CASCADE, to='p1.contactdetails')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PO_Details', models.TextField(blank=True, max_length=500, null=True)),
                ('PO_Value', models.FloatField(blank=True, help_text='PO Value', max_length=10, null=True)),
                ('PO_No', models.CharField(blank=True, help_text='Received PO No', max_length=30, null=True)),
                ('PO_Date', models.DateField(blank=True, help_text='Purchase Order Date', null=True)),
                ('PO_Type', models.CharField(blank=True, choices=[('GST Purchase', 'GST Purchase'), ('Cash Purchase', 'Cash Purchase')], max_length=20, null=True)),
                ('PO_Copy', models.ImageField(blank=True, help_text='Attach Purchase Order', null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='WorkProgress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UpdateDate', models.DateField(help_text='Payment', null=True)),
                ('WorkProgress', models.IntegerField(blank=True, help_text='Work Progress %', null=True)),
                ('Is_Completed', models.BooleanField(default=False, help_text='Is Work Order Completed')),
                ('OtherInfo', models.TextField(blank=True, max_length=500, null=True)),
                ('CompanyName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p1.customerdetails')),
                ('PO_Details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p1.orders')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PaymentDate', models.DateField(help_text='Date of Payment', null=True)),
                ('PaidValue', models.FloatField(blank=True, help_text='Billing Value', max_length=10, null=True)),
                ('NextDate', models.DateField(help_text='Next Commitment Date', null=True)),
                ('IsCleared', models.BooleanField(default=False, help_text='Fully Paid or Not')),
                ('BillNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p1.billingdetails')),
                ('CompanyName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p1.customerdetails')),
            ],
        ),
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(blank=True, choices=[('Commission', 'Commission'), ('Transport', 'Transport'), ('Food', 'Food'), ('Furniture', 'Furniture'), ('Other', 'Other')], max_length=20, null=True)),
                ('Amount', models.FloatField(blank=True, help_text='Expenses Value', max_length=10, null=True)),
                ('Date', models.DateField(help_text='Payment', null=True)),
                ('Description', models.TextField(blank=True, max_length=500, null=True)),
                ('CompanyName', models.ForeignKey(blank=True, help_text='If expenses towrds that particular company', on_delete=django.db.models.deletion.CASCADE, to='p1.customerdetails')),
            ],
        ),
        migrations.AddField(
            model_name='contactdetails',
            name='CompanyName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p1.customerdetails'),
        ),
        migrations.AddField(
            model_name='billingdetails',
            name='CompanyName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p1.customerdetails'),
        ),
    ]
