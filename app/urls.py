from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home_view, about_view, contact_view, courses_view, team_view, testimonial_view

urlpatterns = [
    path('',home_view,name='home-page'),
    path('about/',about_view,name='about-page'),
    path('contact/',contact_view,name='contact-page'),
    path('courses/',courses_view,name='courses-page'),
    path('team/',team_view,name='team-page'),
    path('testimonial/',testimonial_view,name='testimonial-page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)