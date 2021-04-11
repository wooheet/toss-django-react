from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views import defaults as default_views
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.settings import api_settings
from toss import views

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path(r"api-token-auth/", obtain_jwt_token, name="token"),
    path(r"users/", include("toss.users.urls")),
    path(r"contracts/", include("toss.contracts.urls")),
    path(r"rest-auth/", include('rest_auth.urls')),
    path(r"rest-auth/registration/", include('rest_auth.registration.urls')),
    path(r"accounts/", include("allauth.urls")),

    re_path("", view=views.ReactAppView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
