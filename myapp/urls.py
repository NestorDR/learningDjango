from django.urls import path

from myapp import views

# urlpatterns: List to be included in main configuration URLconf (in urls.py of the project)
# Visit: https://docs.djangoproject.com/en/3.1/ref/urls/#include
urlpatterns = [
    path('', views.home, name='Home'),
    path('blog/', views.blog, name='Blog'),
    path('videos/', views.video, name='Videos'),
    path('contact/', views.contact, name='Contact'),

    # Early learning functions
    path('hello/', views.hello_world, name='hello_word'),
    path('age/<int:current_age_>/<int:future_year_>/', views.calculate_age, name='age'),
]