from app.models import CustomUser, Credit_card,Parking,Bicycle
from django.contrib.auth.forms import UserCreationForm
from app.forms import CustomUserCreationForm,CustomUserUpdateCreationForm,CreditCardUpdateForm
from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login as do_login,logout as do_logout
from django.views.decorators.csrf import csrf_protect
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def home(request):
    return render(request,'app/home.html')

def register(request):
    form=CustomUserCreationForm()
    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            data = {
                'username':username
            }
            #messages.success(request,'Cuenta creada correctamente')
            return render(request,'app/credit_card.html',data)
    context={'form':form}
    return render(request,'app/register.html',context)

def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=='POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username=username,password=password)

            if user is not None:
                do_login(request,user)
                return redirect('home')
            
            if user is None:
                messages.error(request,'Usuario o contraseña incorrectos')

        return render(request,'app/login.html')

def logout(request):
    do_logout(request)
    return redirect('login')

def list_user(request):
    if request.user.is_authenticated:

        if request.user.is_staff:

            usuarios=CustomUser.objects.filter(is_staff=0)

            data= {
                'usuarios':usuarios
            }

            return render(request,'app/list-user.html',data)
        return redirect('home')


    else:
        return redirect('home')

def list_user_id(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            id = request.GET['select']
            data = {
                'select':id
            }
            filtro = 0
            for val in data.keys():
                if data[val] == '1':
                    filtro = 1
                    print("FILTRAR POR ID")
                if data[val] == '2':
                    filtro = 2
                    print("FILTRAR POR RUT")
                if data[val] == '0':
                    filtro = 0

            x = request.GET['input-filter']
            if filtro == 1:
                if len(x)==0:
                    x=0
                usuarios=CustomUser.objects.filter(id=x)

                data= {
                    'usuarios':usuarios
                }
                return render(request,'app/list-user.html',data)
            else:
                if filtro == 2:
                    usuarios=CustomUser.objects.filter(username=x)

                    data= {
                        'usuarios':usuarios
                    }
                    return render(request,'app/list-user.html',data)
                else:

                    if filtro == 0:
                        usuarios=CustomUser.objects.filter(is_staff=0)

                        data= {
                            'usuarios':usuarios
                        }
                        return render(request,'app/list-user.html',data)

                    else:
                        return redirect('home')

        return redirect('home')                


def modify_user(request,id):
    usuario=get_object_or_404(CustomUser,id=id)

    data={
        'form': CustomUserUpdateCreationForm(instance=usuario)
    }

    if request.method=='POST':
        formulario=CustomUserUpdateCreationForm(data=request.POST, instance=usuario,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect("perfil")
        data["form"] = formulario

    return render(request,'app/modify.html',data)

def modify_card(request,id):
    upcard=Credit_card.objects.get(username_id=request.user.id)

    data = {
        'form':CreditCardUpdateForm(instance=upcard)
    }
    if request.method=='POST':
        formulario=CreditCardUpdateForm(data=request.POST, instance=upcard,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect("perfil")
        data["form"] = formulario
    return render(request,'app/modify_card.html',data)

@csrf_protect
def modify_card_save(request):
    #print("titular {0}".format(request.POST['headline']))
    headline=request.POST['headline']
    number=request.POST['number']
    #date_expired=request.POST['date_expired']
    cvv=request.POST['cvv']
    month=request.POST['month']
    year=request.POST['year']
    id=request.user.id
    card=Credit_card.objects.filter(username=id)
    card=card(
        headline=headline,
        number=number,
        cvv=cvv,
        month=month,
        year=year
    )
    card.save()
    return redirect("perfil")

def delete_user(request,id):
    usuario=get_object_or_404(CustomUser,id=id)
    usuario.delete()
    return redirect("list-user")

def geolocator(request):
    print(request.user)
    return render(request,'app/map.html')

def credit_card(request):
    return render(request,'app/credit_card.html')

@csrf_protect
def save_card(request):
    try:
        #print("titular {0}".format(request.POST['headline']))
        headline=request.POST['headline']
        number=request.POST['number']
        #date_expired=request.POST['date_expired']
        cvv=request.POST['cvv']
        month=request.POST['month']
        year=request.POST['year']
        username=CustomUser.objects.get(username=request.POST['username'])
        card = Credit_card(
            headline=headline,
            number=number,
            month=month,
            year=year,
            cvv=cvv,
            username=username
        )
        card.save()
        return render(request,'app/credit_card.html')
    except ObjectDoesNotExist as e:
        messages.error(request,'Hubo un error, intente nuevamente el registro')
    return redirect('register')

def perfil(request):
    if request.user.is_authenticated:
        id=request.user.id
        card=Credit_card.objects.filter(username=id)
        usuario=CustomUser.objects.filter(username=request.user.username)
        data = {
            'usuario':usuario,'card':card
        }
        print(type(id))
    return render(request,'app/perfil.html',data)

def bicycle(request,id):
    if not request.user.is_authenticated:
        messages.error(request,'Debe estar logeado para ver estacionamientos y bicicletas disponibles')
        return redirect('login')
    if request.method=='GET':
        #STATE = 0 (BICI DISPONIBLE)
        #STATE = 1 (BICI NO DISPONIBLE)
        #PARKING = A0 (ESTACIONAMIENTO 0)
        #PARKING = A1 (ESTACIONAMIENTO 1)
        if int(id) ==0:
            bike=Bicycle.objects.filter(parking="A0")
            park="A0"
            address="Av. Echeñique 8490-8480, La Reina, Región Metropolitana"
            data = {
                'id':id,
                'bike':bike,
                'park':park,
                'address':address
            }

            print(type(id))
            return render(request,'app/bicycle.html',data)
        if int(id) ==1:
            bike=Bicycle.objects.filter(parking="A1")
            park="A1"
            address="Simón Bolívar 8146-8046, La Reina, Región Metropolitana"
            data = {
                'id':id,
                'bike':bike,
                'park':park,
                'address':address
            }
            
            print(type(id))
            return render(request,'app/bicycle.html',data)
    return redirect('geolocator')

def rent(request,id,cod):
    #ID = CODIGO BICICLETA
    #COD = CODIGO ESTACIONAMIENTO
    if cod =='A0':
        parking=Parking.objects.filter(cod='A1').filter(state=0)
        data = {
            'id':id,
            'parking':parking
        }
    if cod=='A1':
        parking=Parking.objects.filter(cod='A0').filter(state=0)
        data = {
            'id':id,
            'parking':parking
        }
    return render(request,'app/rent.html',data)

def route(request):

    return render(request,'app/route.html')