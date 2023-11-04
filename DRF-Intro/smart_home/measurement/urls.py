from django.urls import path

from .views import SensorView, SensorRetrieveUpdateView, MeasurementCreateView

urlpatterns = [
    path('sensors/', SensorView.as_view(), name='sensors'),
    path('sensors/<int:pk>/', SensorRetrieveUpdateView.as_view(), name='sensor'),
    path('measurements/', MeasurementCreateView.as_view(), name='measurements'),
]
