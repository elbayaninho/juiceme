from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from tablib import Dataset
import os
from mtnmomo.disbursement import Disbursement

from .models import *
from .serializers import *
from .utililies import *
from .mixins import CandidateEditorPermissionMixin
from .resources import CandidateResource



# Test API MOMO PAY
client = Disbursement({
    "DISBURSEMENT_USER_ID": os.environ.get("DISBURSEMENT_USER_ID"),
    "DISBURSEMENT_API_SECRET": os.environ.get("DISBURSEMENT_API_SECRET"),
    "DISBURSEMENT_PRIMARY_KEY": os.environ.get("DISBURSEMENT_PRIMARY_KEY"),
})


class CandidateDetailAPIView(generics.RetrieveAPIView, CandidateEditorPermissionMixin):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    

class CandidateCreateAPIView(generics.CreateAPIView,CandidateEditorPermissionMixin):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

    #Incase there is any additional data that is need to be passed
    def perform_create(self, serializer):
        print(serializer)
        return super().perform_create(serializer)
    

class CandidateListAPIView(generics.ListAPIView):
    queryset = Candidate.objects.all()
    serializer_class= CandidateSerializer


class CandidateListCreateAPIView(generics.ListCreateAPIView,CandidateEditorPermissionMixin):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

    #Incase there is any additional data that is need to be passed
    def perform_create(self, serializer):
        print(serializer)
        return super().perform_create(serializer)



class CandidateUpdateAPIView(generics.UpdateAPIView, CandidateEditorPermissionMixin):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        return super().perform_update(serializer)
    

class CandidateDeleteAPIView(generics.DestroyAPIView, CandidateEditorPermissionMixin):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    lookup_field = 'pk'
 
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
    


class CandidateImportView(APIView):
    parser_classes = (MultiPartParser, FormParser)
   

    def post(self, request, *args, **kwargs):
        candidate = CandidateResource()
        dataset = Dataset()
        new_books = request.FILES['file']
        imported_data = dataset.load(new_books.read().decode('utf-8'), format='csv')
        for data in imported_data:
            value = candidate(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4]
            )
            value.save()
        return Response({"message": "Candidate Details imported successfully"}, status=status.HTTP_201_CREATED)

        
@api_view(['POST'])
def pay_employee(request, employee_id):
    employee = get_object_or_404(Employment, id=employee_id)

    amount = request.POST.get('amount')

    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError
    except(TypeError, ValueError):
        return Response({'error': "Invalid AMount"}, status=status.HTTP_400_BAD_REQUEST)
    
    if employee.net_salary < amount:
        return Response({'error': "Insufficient Balance"}, status= status.HTTP_400_BAD_REQUEST)
    
    # Try to get the existing EmployeeWages object for this employee
    wages = EmployeeWage.objects.filter(employee=employee).first()

    if wages:
        # If the object already exists, update the total_paid_wage field
        wages.total_paid_wage += amount
        wages.save()
    else:
        # If the object does not exist, create a new object with the total_paid_wage field set to the requested amount
        wages = EmployeeWage.objects.create(employee=employee, total_paid_wage=amount)
        wages.save()


def payment_request_approval_view(request, request_id):
    try:
        payment_request = PaymentRequest.objects.get(id=request_id)
    except PaymentRequest.DoesNotExist:
        return Response({'error': 'Payment request does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if payment_request.hr_status:
        return Response({'error': 'Payment request already approved'}, status=status.HTTP_400_BAD_REQUEST)
    
    payment_request.hr_status = request.get('approval_status')
    payment_request.save()
    
    # # Send an email to the HR with the payment request details, we might just need to initiate whatsapp messager
    # subject = 'Payment Request Approval'
    # message = render_to_string('payment_request_approval_email.html', {
    #     'request': payment_request
    # })
    # from_email = 'juice@juice.com'
    # to_email = 'hr@juice.com'
    # send_mail(subject, message, from_email, [to_email])
    
    # return Response({'success': 'Payment request approved'}, status=status.HTTP_200_OK)



def generate_pdf_view(request):
    # Retrieve the user data from the model
    employee = Employment.objects.get(user=request.user)
    
    # Generate the PDF using the separate function
    pdf = generate_pdf(employee)

    # Create an HTTP response with the PDF content
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="pay_slip.pdf"'
    
    return response


class EmployerHRCreateView(APIView):
    def post(self, request, format=None):
        serializer = EmployerHRSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class EmployerHRDetail(generics.RetrieveUpdateAPIView):
    serializer_class = EmployerHRSerializer
    queryset = EmployerHR.objects.all()


# NEED TO REAL TEST
def test_momopay(request):
    print(client)
    #client.transfer(amount="600", mobile="256772123456", external_id="123456789", payee_note="dd", payer_message="dd", currency="EUR")
    return HttpResponse("Test momopay")

