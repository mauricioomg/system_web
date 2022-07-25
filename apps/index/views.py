from django.contrib.auth import login, authenticate, views
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from django.db.models import Q
from .models import Book
from . import forms


""" LANDING """
class IndexView(generic.TemplateView):
    template_name = 'landing/index.html'


class AboutUsView(generic.TemplateView):
    template_name = 'landing/about_us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_us'] = 'about_us'
        return context
""" END_LANDING """


""" USERS """
class UserRegisterView(generic.CreateView):
    model = User
    form_class = forms.UserForm

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return redirect('index:index')


class UserUpdateView(generic.UpdateView):
    model = User
    form_class = forms.UserForm
    success_url = reverse_lazy('index:index')


class UserLoginView(views.LoginView):
    template_name = 'landing/index.html'
    authentication_form = forms.LoginAuthForm

    def get_success_url(self):
        if self.request.user.is_staff:
            return reverse_lazy('dashboard:index')
        else:
            return reverse_lazy('index:list_books')

    # def form_invalid(self, form):
    #     context = {'form':form}
    #     context['error_message'] = "Ingrese un %(username)s y contraseña correctos. Tenga en cuenta que estos campos pueden distinguir entre mayúsculas y minúsculas."
    #     return render(self.request, self.template_name, context)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form'] = self.form_class
    #     return context


class UserLogoutView(views.LogoutView):
    template_name = '../templates/index/base.html'
""" END_USERS """


""" BOOKS """
class CreateBookView(generic.CreateView):
    template_name = 'books/create.html'
    model = Book
    form_class = forms.BookForm
    success_url = reverse_lazy('index:list_books')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear'
        context['create_book'] = True
        return context

    # Guarda en la variable Creator al usuario autenticado
    def form_valid(self, form):
        user = self.request.user
        form.instance.creator = user
        return super(CreateBookView, self).form_valid(form)


class UpdateBookView(generic.UpdateView):
    template_name = 'books/create.html'
    model = Book
    form_class = forms.BookForm
    success_url = reverse_lazy('index:list_books')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar'
        context['update_book'] = True
        return context
    
    def form_valid(self, form):
        user = self.request.user
        form.instance.creator = user
        return super(UpdateBookView, self).form_valid(form)


class ListBooksView(generic.ListView):
    template_name = 'books/list.html'
    context_object_name = 'list_books'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q', None)
        object_list = Book.objects.all()
        if query is not None:
            object_list = object_list.filter(Q(title__icontains=query))
        return object_list.order_by('title')


class ListMyBooksView(generic.ListView):
    template_name = 'books/my_books/list.html'
    context_object_name = 'my_books'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q', None)
        object_list = Book.objects.filter(creator=self.request.user)
        if query is not None:
            object_list = object_list.filter(Q(title__icontains=query))
        return object_list.order_by('title')


class DetailBookView(generic.DetailView):
    template_name = 'books/detail.html'
    model = Book


class DeleteBookView(generic.DeleteView):
    model = Book
    success_url = reverse_lazy('index:list_books')
""" END_BOOKS """