from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

# Redirect root URL to signin page
def redirect_to_signin(request):
    return redirect('signin')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_to_signin),               # Root URL redirects to signin
    path('portal/', include('portal.urls')),    # Include portal app URLs
]
