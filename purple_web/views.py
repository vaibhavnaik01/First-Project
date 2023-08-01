from django.shortcuts import render, redirect
import pyodbc
from django import forms
from .forms import RegistrationForm,SignUpForm
from .db import insert_user,connect_to_db, save_form_data



from django.shortcuts import render, HttpResponseRedirect
# from .forms import SignUpForm
# from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout #update_session_auth_hash
from .db import insert_user_signup,insert_user,connect_to_db
from .forms import RegistrationForm


def sign_up(request):
    if request.method == 'POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['username']
            first_name=fm.cleaned_data['first_name']
            email = fm.cleaned_data['email']
            pwd = fm.cleaned_data['password1']
            
            
            conn = connect_to_db()
            if conn:
                insert_user_signup(conn, name,first_name, email, pwd)
                messages.info(request, 'Your Account Successfully Created..!!!')
            else:
                messages.error(request, 'Error connecting to the database.')

            fm.save()
    else:
        fm = SignUpForm()
    return render(request, 'signup.html', {'form': fm})


def login_form(request):
    if not request.user.is_authenticated:


        if request.method=='POST':
            fm = AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user:
                    login(request, user)
                    messages.success(request, 'Logged  in successfully')
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request, 'loginform.html', {'form':fm})
    else:
        return HttpResponseRedirect('/profile/') 

# def profile(request):
#     if request.user.is_authenticated:
#         return render(request, 'profile.html',{'name':request.user})
#     else:
#         return HttpResponseRedirect('/login/')
        
    
# def profile(request):
    
      
#     if request.method == 'POST':
#         form_data = {
#             'first_name': request.POST.get('first_name'),
#             'country_of_residence': request.POST.get('country_of_residence'),
#             'type': request.POST.get('type'),
#             'email_id': request.POST.get('email_id'),
#             'phone_number': request.POST.get('phone_number'),
#             'current_company': request.POST.get('current_company'),
#             'current_role': request.POST.get('current_role'),
#             'company_worked_at': request.POST.get('company_worked_at'),
#             'title_at_company': request.POST.get('title_at_company'),
#             'relationship_description': request.POST.get('relationship_description'),
#             'duration_of_knowing': request.POST.get('duration_of_knowing'),
#             'linked_in_url': request.POST.get('linked_in_url'),
#             'Q1_1': request.POST.get('Q1_1'),
#             'Q1_2': request.POST.get('Q1_2'),
#             'Q1_3': request.POST.get('Q1_3'),
#             'Q2_1': request.POST.get('Q2_1'),
#             'Q2_2': request.POST.get('Q2_2'),
#             'Q2_3': request.POST.get('Q2_3'),
#             'Q2_4': request.POST.get('Q2_4'),
#             'Q2_5': request.POST.get('Q2_5'),
#             'Q2_6': request.POST.get('Q2_6'),
#             'Q2_7': request.POST.get('Q2_7'),
#             'Q3_1': request.POST.get('Q3_1'),
#             'Q3_2': request.POST.get('Q3_2'),
#             'Q3_3': request.POST.get('Q3_3'),
#             # 'Q4': request.POST.get('Q4'),
#             'Q4_1': request.POST.get('Q4_1'),
#             'Q5_1': request.POST.get('Q5_1'),
#             'Q5_2': request.POST.get('Q5_2'),
#             'Q6_1': request.POST.get('Q6_1'),
#             # 'Q6_2': request.POST.get('Q6_2'),
#             'Q7_1': request.POST.get('Q7_1'),
#             # 'Q7_2': request.POST.get('Q7_2'),
#         }
#         save_form_data(form_data)

#         return render(request, 'summary.html', {'data': form_data})

    

#     if request.user.is_authenticated:
#         return render(request, 'test.html', {'name': request.user})
#     else:
#         return HttpResponseRedirect('/login/')


############### for new ########
from .models import NewTest1
def profile(request):
    
      
    if request.method == 'POST':
        form_data = {
            
            'Que1': request.POST.get('Que1'),
            'Que2': request.POST.get('Que2'),

            'Que3': request.POST.get('Que3'),
            'Que4': request.POST.get('Que4'),
            
            
            
        }
        save_form_data(form_data)

        return render(request, 'summary.html', {'data': form_data})

    

    if request.user.is_authenticated:
        return render(request, 'test.html', {'name': request.user})
    else:
        return HttpResponseRedirect('/login/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')








 

class RegistrationForm(forms.Form):

    full_name = forms.CharField(label='Full Name', max_length=100)
    email = forms.EmailField(label='Email')
 

def placeholder_view(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            selected_name = form.cleaned_data['full_name']
            selected_email = form.cleaned_data['email']
            try:
                connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-7JF3UC3K\SQLEXPRESS;DATABASE=test;Trusted_Connection=yes;')
                cursor = connection.cursor()
                cursor.execute("SELECT full_name, email FROM test7 WHERE full_name = ? AND email = ?", (selected_name, selected_email))
                rows = cursor.fetchall()
                if not rows:
                    return render(request, 'record_not_found.html')
                formatted_strings = []
                for row in rows:
                    name = row[0]
                    email = row[1]
                    formatted_string = f"I'm {name} and {email} this is my contact mail id"
                    formatted_strings.append(formatted_string)

                cursor.close()
                connection.close()
                return render(request, 'err_template.html', {'formatted_strings': formatted_strings})
            except pyodbc.Error as e:
                error_message = str(e)
                return render(request, 'err_template.html', {'error_message': error_message})
    else:
        form = RegistrationForm()
    return render(request, 'export_data.html', {'form': form})























#######################################
# def registration_view(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form_data = form.cleaned_data
#             conn = connect_to_db()
#             if conn:
#                 insert_user(conn, form_data)
#                 return render(request, 'my_app.html')  # Redirect to a success page
#     else:
#         form = RegistrationForm()

#     return render(request, 'my_app.html', {'form': form})