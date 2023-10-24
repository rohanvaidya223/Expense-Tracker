from django.shortcuts import render,redirect
from .forms import ExpenseForm
from .models import Expense
from django.db.models import Sum
import datetime
from .forms import LoginForm ,UserRegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.

def user_login(request):

    if request.method == "POST":
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            data = login_form.cleaned_data
            user = authenticate(request,username=data['username'],password=data['password'])

            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                pass


    else:
        login_form = LoginForm()
    
    return render(request,'myapp/login.html',{'login_form':login_form})

def register(request):
    
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            return redirect('login')
    else:
        user_form = UserRegistrationForm()

        return render(request,'myapp/register.html',{'user_form':user_form})


@login_required
def index(request):

    if request.method == "POST":
        expense_form = ExpenseForm(request.POST)
        if expense_form.is_valid():
            expense_form.save()

    expenses = Expense.objects.all()
    total_expenses = expenses.aggregate(Sum('amount'))
    

    # logic to calculate 365 days expenses
    last_year = datetime.date.today() - datetime.timedelta(days=365)
    data = Expense.objects.filter(date__gt=last_year)
    yearly_sum = data.aggregate(Sum('amount'))

    # logic to calculate 30 days expenses
    last_month = datetime.date.today() - datetime.timedelta(days=30)
    data = Expense.objects.filter(date__gt=last_month)
    monthly_sum = data.aggregate(Sum('amount'))
    
    # logic to calculate 7 days expenses
    last_week = datetime.date.today() - datetime.timedelta(days=7)
    data = Expense.objects.filter(date__gt=last_week)
    weekly_sum = data.aggregate(Sum('amount'))

    daily_sums = Expense.objects.filter().values('date').order_by('date').annotate(sum=Sum('amount'))

    categorical_sums = Expense.objects.filter().values('category').order_by('category').annotate(sum=Sum('amount'))

    expense_form = ExpenseForm()
    return render(request,'myapp/index.html',{'expense_form':expense_form,'expenses':expenses,'total_expenses':total_expenses,'yearly_sum':yearly_sum,'monthly_sum':monthly_sum,'weekly_sum':weekly_sum,'daily_sums':daily_sums,'categorical_sums':categorical_sums})









def edit(request,id):
    expense = Expense.objects.get(id=id)
    expense_form = ExpenseForm(instance = expense)
    if request.method == 'POST':
        expense = Expense.objects.get(id=id)
        form = ExpenseForm(request.POST,instance= expense)
        if form.is_valid():
            form.save()
            return redirect('index')
    

        
    return render(request,'myapp/edit.html',{'expense_form':expense_form})















def delete(request,id):
    
    if request.method == 'POST' and 'delete' in request.POST:
        expense = Expense.objects.get(id=id)
        expense.delete()
    
    return redirect('index')