
from datetime import date
from django.contrib.auth.models import User
from django.contrib import admin
from django.db.models.signals import post_save, pre_save
from django.db.models.functions import Concat
from django.dispatch import receiver
from django.db import models
from django.core.exceptions import ValidationError
from datetime import timezone

from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField

from django.db import models
from .choices_fields import *


class Candidate(models.Model):
    first_name = models.CharField(max_length=120, blank= False, null= False)
    middle_name = models.CharField(max_length=120, blank=True, null=True,)
    last_name = models.CharField(max_length=120)
    dob = models.DateField(max_length=8)
    gender = models.CharField(max_length=15, choices=gender_id)
    maritual_status = models.CharField(max_length=15, choices=maritual_status)
    prefered_industry = models.CharField(max_length=120)
    salary_expectation = models.DecimalField(max_digits=12, decimal_places=2,default=0.00, null=True, blank=True)
    education_level = models.CharField(max_length=50, choices=education_levels, null=True, blank=True)
    skills = models.TextField( null=True, blank=True)
    Experience = models.TextField( null=True, blank=True)
    language = models.CharField(max_length=15, choices = languages)

    @admin.display(ordering=Concat('last_name', models.Value(' '), 'first_name'),description='Full name',)
    def full_name(self):
        return self.first_name + ' ' + self.last_name
    
    @property
    def age(self):
        "Return the Candidate's age"
        today = date.today()
        yrs = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
        return yrs

    def __str__(self):
        return self.full_name() 

#TODO: Ensure that each candidate is associaate with only one KYC 
class CandidateKYC(models.Model):
    candidate = models.OneToOneField(to=Candidate, on_delete=models.CASCADE)
    identity_type = models.CharField(max_length=20)
    identity_issuer = models.CharField(max_length=120)
    identity_number = models.CharField(max_length=120)


#TODO: Ensure that each candidate is asso
class PersonalContacts(models.Model):
    user = models.OneToOneField(to=Candidate,on_delete=models.DO_NOTHING)
    phone_number = PhoneNumberField(blank = False)
    whatsapp_number = PhoneNumberField(blank = True)
    email = models.EmailField()
    home_address = models.CharField(max_length=120)
    region = models.CharField(max_length=120)
    country = CountryField()

#https://codereview.stackexchange.com/questions/116095/bank-account-model-implementation-in-django
#https://github.com/Jaye-python/Python-Django-Bank-Application
class BankingInfo(models.Model):
    user = models.OneToOneField(to=Candidate, on_delete=models.CASCADE)
    banking_system = models.CharField(max_length = 120, choices=banking_system)
    bank_name = models.CharField(max_length=120)
    account_number= models.CharField(max_length=15)
    account_name = models.CharField(max_length=120)
    mobile_network = models.CharField(max_length=120)
    banking_phone_number = PhoneNumberField()


class Company(models.Model):
    name = models.CharField(max_length=120)
    id_type = models.CharField(max_length=30)
    id_number = models.CharField(max_length=64)
    sector = models.CharField(max_length=120)
    registration_date = models.DateField()

    ownership = models.CharField(max_length=64, choices=(('Private','Private'),('Public','Public'),('Partnership','Partnership'),('NGO','NGO')))
    owners_name = models.CharField(max_length=120)
    owners_phone_number = PhoneNumberField()
    owner_email = models.EmailField(verbose_name='Owners Email Address')

    contact_person_name = models.CharField(max_length=120)
    contact_person_phone= PhoneNumberField()
    contact_person_email = models.EmailField()

    address = models.CharField(max_length=120)
    email = models.EmailField()
    phone_number = PhoneNumberField()
    region = models.CharField(max_length=120)
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name_plural = 'Companies'

    
class EmployerHR(models.Model):
    user  = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company,on_delete=models.DO_NOTHING, blank=True, null= True)
    phone_number = PhoneNumberField()
    address = models.CharField(max_length=20,unique=True)
    dob = models.DateField()
    designation = models.CharField(max_length=50,choices=designations_opt)


@receiver(post_save, sender=User)
def create_user_employerhr(sender,instance, created, **kwargs):
    if created and not instance.is_superuser:
        EmployerHR.objects.create(user=instance)


@receiver(post_save,sender=User)
def save_user_employerhr(sender,instance, **kwargs):
    if not instance.is_superuser:
        instance.employerhr.save()
    
    
class Employment(models.Model):
    company = models.ForeignKey(Company, on_delete= models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete= models.CASCADE,)
    employement_type = models.CharField(max_length = 15,choices=job_types)
    designation = models.CharField(max_length=50,choices=designations_opt)
    net_salary = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    hired_date = models.DateField()
    terminated_date = models.DateField(null=True, blank=True)
    is_terminated = models.BooleanField(default=False)

    def __str__(self):
        return "Employment for {}".format(self.company)

    def clean(self):
        if not self.is_terminated:
            # Check if the person is already associated with another company
            existing_employment = Employment.objects.filter(candiate=self.candidate, is_terminated=False).exclude(id=self.id).first()
            if existing_employment:
                raise ValidationError(f"Candidate {self.candidate.first_name} is already associated with company {existing_employment.company.name}.")


@receiver(pre_save, sender=Employment)
def set_terminated_date(sender, instance, **kwargs):
    if instance.is_terminated and not instance.terminated_date:
        instance.terminated_date = timezone.now().date()


class EmployeeWage(models.Model):
    employeeId = models.ForeignKey(Employment, on_delete=models.DO_NOTHING)
    net_salary = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    total_paid_ewa = models.DecimalField(max_digits=12, decimal_places=2,default=0.00)

    def balance_str(self):
        return 'Your Remaining Balance is: {.2f}'.format (self.net_salary - self.paid_ewa)


class PaymentRequest(models.Model):
    employee_Id = models.ForeignKey(Employment,on_delete=models.CASCADE,related_name="requesterId")
    amount = models.DecimalField(decimal_places=2, max_digits=12, default=0.00)
    request_reason = models.TextField()
    request_time = models.DateTimeField(auto_now_add=True)
    destination_wallet = models.CharField(max_length=50)
    

class RequestStatus(models.Model):
    request_Id = models.ForeignKey(PaymentRequest,on_delete=models.DO_NOTHING)
    request_time = models.DateTimeField()
    hr_status = models.CharField(max_length=13, choices=(('Approved','Approved'),('Rejected','Rejected'),('Pending','Pending') ), 
                                 default='Pending')
    hr_status_update_time = models.DateTimeField(auto_now_add=True)
    juice_dispursed_status = models.CharField(max_length=12,choices=(('A','Settled'),('B','Juice Pending To Be Complete'),('C','HR approval Waiting'), ('E','Was Rejected'),('F','Incomplete Request'))) 
    juice_status_time = models.DateTimeField()


class Attendance(models.Model):
    employeeId = models.ForeignKey(Candidate,on_delete=models.CASCADE)
    month = models.CharField(max_length=50,choices=months)
    days = models.CharField(max_length=5,choices=days)

    def __str__(self):
        return "%s %s" % (self.employeeId, self.month)

class Notice(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    publish_date = models.DateTimeField()

    def __str__(self):
        return self.title 


class WorkAssignment(models.Model):
    assigner_id = models.ForeignKey(Employment,on_delete=models.CASCADE,related_name="assignerId")
    work = models.TextField()
    assign_date = models.DateTimeField()
    due_date = models.DateTimeField()
    tasker_id = models.ForeignKey(Employment,on_delete=models.CASCADE,related_name="taskerId") 
