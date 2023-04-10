from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from customerapp.forms import SignupForm, AddRecordForm
from customerapp.models import Record

from django.contrib.auth.models import User, auth

# Create your views heres

def home(request):
    records=Record.objects.all()
    #check if user is logged in
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password1']

        #authenticate the user
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
         
            messages.success(request,  f'{username} You logged in successfully!...')
            return redirect('home')
        else:
            messages.info(request, 'Please try with correct ceredentials...')
            return redirect('home')
    else:

     return render(request, 'home.html',{'records':records})






def logout_user(request):
    
    auth.logout(request)
    messages.info(request,' you have been logged out...')
    return redirect('home')



        
             
# 
def register_user(request):
    if request.method == 'POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request, user)
            messages.success(request, f'{username} you have successfully registered!...')
            return redirect('/')
    else:
        form=SignupForm()
        return render(request, 'register.html',{'form':form})
           

    return render(request,'register.html', {'form':form})             

               
    		   
# @login_required(login_url='home')	
def customer_record(request,pk):
    if request.user.is_authenticated:

        customer_record=Record.objects.get(id=pk)
        print(customer_record)
        return render(request,'record.html', {'customer_record': customer_record})  

    else:
        messages.info(request,'you must login to view record')
        return redirect('home')
    






def delete_record(request,pk):
    delete_id=Record.objects.get(id=pk)
    delete_id.delete()
    messages.success(request, 'Record Deleted Successfully')
    return redirect('home')







def add_record(request):
    form=AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method =='POST':
            if form.is_valid():
                add_record=form.save()
                messages.success(request, 'Record added successfully....')
                return redirect('home')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.info(request, 'You must logged in to add new record ....')
        return redirect('home')
    






def update_record(request, pk):
        
        if  request. user.is_authenticated:
            current_record=Record.objects.get(id=pk)
            form=AddRecordForm(request.POST or None, instance=current_record)
            if form.is_valid():
                form.save()
                messages.info(request,"Record has been updated")
                return redirect('home')
            return render(request, 'update.html',{'form':form})
        else:
            messages.info(request,"You Must Be Logged In..")
            return redirect('home')
        
        
   
                
	


              
                        
    	 		    

                

  