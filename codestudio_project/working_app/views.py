from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import *
from .forms import FeedbackForm
from django.core.mail import send_mail
from django.contrib import messages


def index(request):
    '''
    Обозначим наш первый и единственный элемент главной страницы в БД, продукты, форму фидбека
    и добавим их в словарь context
    '''
    homepage = HomePage.objects.first()
    products = Product.objects.all()
    form = FeedbackForm()
    context = {
        'homepage': homepage,
        'products': products,
        'form': form,
    }
    '''Форма отправки email сообщения'''
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            mail = send_mail(
                subject=form.cleaned_data['name'], message=form.cleaned_data['email'],
                from_email='mailfortests1337@gmail.com',
                recipient_list=['test@codestudio.org'], fail_silently=False
            )
            if mail:
                messages.success(request, 'Сообщение успешно отправлено!')
                return redirect('index_url')
            else:
                messages.error(request, 'Ошибка отправки!')
        else:
            form = FeedbackForm()

    return render(request, 'index.html', context=context)

def get_product(request, slug):
    '''Получим нашу страницу с продуктом по ее уникальному идентификатору'''
    product = get_object_or_404(Product, slug__iexact=slug)

    return render(request, 'product.html', {'product': product,})
    