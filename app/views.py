from app.models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from app.forms import CustomUserCreationForm
from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login as do_login,logout as do_logout

# Create your views here.
def home(request):
    return render(request,'app/home.html')

def register(request):
    form=CustomUserCreationForm()

    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)
        context = {'form' : form}
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Cuenta creada correctamente')
            return redirect('home')
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
        'form': CustomUserCreationForm(instance=usuario)
    }

    if request.method=='POST':
        formulario=CustomUserCreationForm(data=request.POST, instance=usuario,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect("list-user")
        data["form"] = formulario

    return render(request,'app/modify.html',data)

def delete_user(request,id):
    usuario=get_object_or_404(CustomUser,id=id)
    usuario.delete()
    return redirect("list-user")

def geolocator(request):
    return render(request,'app/map.html')

def bicycle(request,id):
    if request.method=='GET':
        print(id)
    return render(request,'app/bicycle.html')