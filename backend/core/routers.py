from rest_framework.routers import DefaultRouter
from core.viewset import CandidateViewSet


router = DefaultRouter()
router.register('candidate-abc', CandidateViewSet, basename='candidate')
