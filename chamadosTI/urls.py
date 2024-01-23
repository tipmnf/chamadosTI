"""
URL configuration for chamadosTI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import Http404

class CustomPasswordResetView(PasswordResetView):
    def form_valid(self, request, *args, **kwargs):
        email = self.request.POST.get('email') or self.request.GET.get('email')
        if not User.objects.filter(email=email).exists():
            messages.error(self.request, 'Este e-mail não foi encontrado no sistema.')
        return super().get(request, *args, **kwargs)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chamadosApp.urls')),
    path('reset-password', CustomPasswordResetView.as_view(), name='password_reset'),
    path('reset-password/done', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset-password/confirm/<uidb64>[0-9A-Za-z]+)-<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'), 
    path('reset-password/complete/',PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)