from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, FormView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .models import Note
from .forms import AddNote, CreateUserForm


# Create your views here.

class NoteHome(ListView):
    model = Note
    template_name = "note/index.html"

    def get_contex_data(self, **kwarg):
        context = super().get_contex_data(**kwarg)
        return context

class AddNoteView(FormView):
    template_name = 'note/add.html'
    form_class = AddNote
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super(AddNoteView, self).form_valid(form)

class NoteDetailView(DetailView):
    model = Note
    template_name = 'note/detail.html'

    def get_context(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def registration(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created' + username)
            return redirect('login_page')

    context = {'form': form}
    return render(request, 'note/registration.html', context)


def loginPage(request):

    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'login or password is incorrect')
            return render(request, 'note/login.html', context)

    return render(request, 'note/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login_page')