INSTALLED_APPS= [
  'rest-framework',
]

urlpatterns = [
  path('api-/auth/', include('rest_framework.urls'))
]

REST_FRAMEWORK = {
  # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

