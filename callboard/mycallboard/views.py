from django.contrib import messages
from django.db.models import Count, F
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import *
from .forms import CreateAdForm, UserRegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin


def register(request):
    categories = Category.objects.annotate(cnt=Count('ad', filter=F('ad__is_moderation'))).filter(cnt__gt=0)
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'callboard/register.html', context={'form': form, 'categories': categories})


def login(request):
    return render(request, 'callboard/login.html')


class AdsList(ListView):
    model = Ad
    context_object_name = 'ads'
    template_name = 'callboard/Ads_List.html'
    categories = Category.objects.annotate(cnt=Count('ad', filter=F('ad__is_moderation'))).filter(cnt__gt=0)
    extra_context = {'categories': categories}
    paginate_by = 6

    def get_queryset(self):
        return Ad.objects.filter(is_moderation=True).select_related('category', 'ad_type', 'currency', 'city',
                                                                    'district')


class AdsCategoryList(ListView):
    model = Ad
    context_object_name = 'ads'
    template_name = 'callboard/Ads_List.html'
    categories = Category.objects.annotate(cnt=Count('ad', filter=F('ad__is_moderation'))).filter(cnt__gt=0)
    extra_context = {'categories': categories}
    paginate_by = 5

    def get_queryset(self):
        return Ad.objects.filter(category_id=self.kwargs['pk'], is_moderation=True).select_related('category',
                                                                                                   'ad_type',
                                                                                                   'currency',
                                                                                                   'city', 'district')


class CreateAd(LoginRequiredMixin, CreateView):
    # login_url = '/login/'
    raise_exception = True
    form_class = CreateAdForm
    template_name = 'callboard/create_ad.html'
    success_url = reverse_lazy('create_success')


def create_success(request):
    return render(request, template_name='callboard/create_success.html')
