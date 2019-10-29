from django.urls import path
from . import views

urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail")
]
# here <int:pk>/ shows that we are putting 1,2,3 the ID of each project in the url so that for each project there is different url

