from django.urls import path
from .views import nodeListCreate,nodeDetailView,nodeUpgradeView,nodeLowerView

urlpatterns = [
    path('notes/',nodeListCreate.as_view()),
    path('notes/<int:pk>/',nodeDetailView.as_view()),
    path('notes/<int:pk>/upgrade/',nodeUpgradeView.as_view()),
    path('notes/<int:pk>/lower/',nodeLowerView.as_view())
]