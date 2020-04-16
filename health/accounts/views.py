from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Doctor, Pharmacist, People, Prescription, Vitals

# Create your views here.
def home(request):
    if request.method == 'GET':
        return render(request, 'accounts/home.html')

    else:
        val = request.POST['login'] 
        username = request.POST['username']
        password = request.POST['password']
        if val == 'Doctor':
            if Doctor.objects.filter(username=username).exists() and Doctor.objects.filter(password=password).exists():
                return render(request, 'accounts/doctor.html')
            else:
                messages.info(request, 'Username and Password does not match')
                return redirect('/')
        
        elif val == 'Admin':
            if request.POST['username'] == 'admin' and request.POST['password'] == 'admin123':
                return render(request, 'accounts/admin.html')
            else:
                messages.info(request, 'Username and Password does not match')
                return redirect('/')            
        
        elif val == 'Pharmacist':
            if Pharmacist.objects.filter(username=username).exists() and Pharmacist.objects.filter(password=password).exists():
                return render(request, 'accounts/pharmacist.html')
            else:
                messages.info(request,'Username and Password does not match')
                return redirect('/')

        elif val == 'Patient':
            if People.objects.filter(username=username).exists() and Pharmacist.objects.filter(password=password).exists():
                return render(request, 'accounts/patient.html')
            else:
                messages.info(request,'Username and Password does not match')
                return redirect('/')
        
        else:
            messages.info(request, 'Please select login-as')
            return redirect('/')


def changedetails(request):
    
    if request.method == 'GET':
        return render(request, 'accounts/changedetails.html')
    else:
        adhar = request.POST.get('padhar', False)
        bp = request.POST['bp']
        temp = request.POST['temp']
        pulse = request.POST['pulse']
        height = request.POST['height']
        weight = request.POST['weight']
   
        dtype = request.POST['type']
        drug = request.POST['drug']
        dose = request.POST['dose']
        quant = request.POST['quant']
        slot = request.POST['slot']
        time = request.POST['time']
        pref = request.POST['pref']
        note = request.POST['note']

        vit = Vitals(adhar_num=adhar, BP=bp, temperature=temp, height=height, weight=weight, pulse_rate=pulse)
        vit.save()
        pre = Prescription(adhar_num=adhar, type=dtype, drug_name=drug, dose=dose, quantity=quant, slots=slot, time=time, preferred=pref, note=note)
        pre.save()

        return render(request,'accounts/doctor.html')


def PDetails(request):
    if request.method == 'GET':
        return render(request, 'accounts/doctor.html')

    else:
        adhar = request.POST['padhar']
        if People.objects.filter(adhar_no=adhar).exists():
            details = People.objects.filter(adhar_no=adhar)
            vitals = Vitals.objects.filter(adhar_num=adhar)
            pres = Prescription.objects.filter(adhar_num=adhar)

            context = {
                'record': details,
                'vit': vitals,
                'medcine': pres,
            }        
                       
            return render(request, 'accounts/pdetails.html', context)

def docregister(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['number']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        address = request.POST['address']
        email = request.POST['email']
        adhar_num = request.POST['adhar_num']
        qualification = request.POST['qualification']

        if password1 == password2:
            if Doctor.objects.filter(adhar_num=adhar_num).exists():
                messages.info(request, 'already registered')
                return redirect('docregister')

            elif Doctor.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('docregister')
            else:    
                doc = Doctor(username=adhar_num, Firstname=first_name, Lastname=last_name, address=address, password=password1, email=email, phone=phone, qualification=qualification, adhar_num=adhar_num)
                doc.save()
                print('Doctor Registered')
                return redirect('/')              
        else:
            messages.info(request, 'password not matching')
            return redirect('docregister')

    else:
        return render(request, 'accounts/docregister.html')


def pharmregister(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['number']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        address = request.POST['address']
        email = request.POST['email']
        adhar_num = request.POST['adhar_num']
        qualification = request.POST['qualification']

        if password1 == password2:
            if Pharmacist.objects.filter(adhar_num=adhar_num).exists():
                messages.info(request, 'already registered')
                return redirect('pharmregister')

            elif Pharmacist.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('pharmregister')
            else:    
                doc = Pharmacist(username=adhar_num, Firstname=first_name, Lastname=last_name, address=address, password=password1,email=email,phone=phone,qualification=qualification,adhar_num=adhar_num)
                doc.save()
                print('Pharmcist Registered')
                return redirect('/')               
        else:
            messages.info(request, 'password not matching')
            return redirect('docregister')

    else:
        return render(request, 'accounts/docregister.html')

def userregister(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['number']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        address = request.POST['address']
        email = request.POST['email']
        adhar_num = request.POST['adhar_num']
        
        if password1 == password2:
            if People.objects.filter(adhar_no=adhar_num).exists():
                messages.info(request, 'User alreay registered')
                return redirect('userregister')
            elif People.objects.filter(email=email):
                messages.info(request, 'Email already taken')
                return redirect('userregister')
            else:    
                user = People(username=first_name, first_name=first_name, last_name=last_name, address=address, adhar_no=adhar_num, phone=phone, password=password1, email=email)
                user.save()
                print('user created')
                return redirect('/')
        else:
            messages.info(request, 'password not matching')
            return redirect('userregister')

    else:
        return render(request, 'accounts/userregister.html')
    
