from django.conf.urls.static import static
from django.urls import path

from StudentCRUD import settings
from apps.views import student_list_viwe, student_add_view, student_detail_view, student_delete_viwe, student_edit_viwe

urlpatterns = [
    path('student/list' , student_list_viwe , name='student-list'),
    path('student/add',student_add_view, name='student-add'),
    path('student/detial/<int:id>' , student_detail_view , name='student-detial'),
    path('student/delete/<int:id>' , student_delete_viwe, name='student-delete'),
    path('student/edit/<int:id>' , student_edit_viwe , name='student-edit'),
] # + config for image
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)