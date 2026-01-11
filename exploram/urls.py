from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.accounts import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('login/', account_views.user_login, name='login'),
    path('logout/', account_views.user_logout, name='logout'),
    path('accounts/', include('apps.accounts.urls')),

    # ✅ ORIGINAL HOME (RESTORED)
    path('', include('application.urls')),

    # ✅ PUBLIC TRIPS
    path('trips/', include('apps.trips.urls')),

    # ✅ ADMIN PANEL (still works)
    # admin-panel/ is inside trips app
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
