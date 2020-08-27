from django.urls import path

from . import views

urlpatterns = [
    path('', views.diary, name="diary19", kwargs={'year': 2019}),
    path('<int:year>', views.diary, name="diary"),
    path('outbound_diaries/<int:student_id>', views.student, name="student"),
    path('filter/<int:year>/<int:branch_id>', views.filter, name="filter"),
    path('submit/<int:year>', views.submit, name="submit")
]