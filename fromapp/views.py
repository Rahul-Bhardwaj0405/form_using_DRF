from functools import partial
from rest_framework .views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import FormData
from .serializers import FormDataSerializer
from django.shortcuts import render, redirect
from .forms import FormDataForm


# Create your views here.

def submit_form(request):
    if request.method == 'POST':
        form = FormDataForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the data to the database
            return redirect('fromapp/success')  # Redirect to a success page
    else:
        form = FormDataForm()

    return render(request, 'fromapp/submit_form.html', {'form': form})



def success(request):
    return render(request, 'fromapp/success.html')


class FormDataListCreateView(APIView):
    def get(self, request):
        formdata = FormData.objects.all()
        serializer = FormDataSerializer(formdata, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = FormDataSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FormDataDetailsUpadteView(APIView):
    def get(self, request, pk):
        form_data = get_object_or_404(FormData, pk=pk)
        serializer = FormDataSerializer(form_data)
        return Response(serializer.data)
    
    def put(self, request, pk):
        form_data = get_object_or_404(FormData, pk=pk)
        serializer = FormDataSerializer(form_data, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        form_data = get_object_or_404(FormData, pk=pk)
        serializer = FormDataSerializer(form_data, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    



