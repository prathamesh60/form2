"""form2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from app2 import views

urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('religion',views.religion),
#     path('show_religion',views.show_religion),
#     path('edit/<int:id>',views.edit),
#     path('update/<int:id>',views.modify_religion),
    # path('religion/create',views.Create.as_view(),name='create_religion'),
    path('religion',views.religion),
    path('show_religion',views.show_religion),
    path('delete/<int:id>',views.delete_religion),
    path('<pk>/update', views.ReligionUpdateView.as_view()),
    re_path(r'^\d+/religion',views.religion),
    path('caste',views.caste),
    path('<pk>/update_caste', views.CasteUpdateView.as_view()),
    re_path(r'^\d+/caste',views.caste),
    path('delete_caste/<int:id>',views.delete_caste),
    path('suplhead',views.suplhead),
    path('<pk>/suplhead', views.SuplHeadUpdateView.as_view()),
    re_path(r'^\d+/suplhead',views.suplhead),
    path('delete_suplhead/<int:id>',views.delete_suplhead),

    path('category',views.category),
    path('show_category',views.show_category),
    path('delete_category/<int:id>',views.delete_category),
    path('<pk>/update_category', views.CategoryUpdateView.as_view()),
    re_path(r'^\d+/category',views.category),
]
