from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('auth/', obtain_auth_token),

    path('candidate/<int:pk>', views.CandidateDetailAPIView.as_view(), name='candidate-detail'),
    path('candidate/create',views.CandidateCreateAPIView.as_view()),
    path('candidates/', view= views.CandidateListAPIView.as_view(), name='candidate-list'), #mind the 's' at the end of the request
    path('candidate/', view=views.CandidateListCreateAPIView.as_view()),
    path('candidate/update/<int:pk>', views.CandidateUpdateAPIView.as_view(), name='candidate-update'),
    path('candidate/delete/<int:pk>', views.CandidateDeleteAPIView.as_view()),

    path('candidates/upload/', views.CandidateImportView.as_view(), name ='candidate-upload'),
    path('test-momo-pay', views.test_momopay, name='test_momo_pay'),
]

urlpatterns += static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
)