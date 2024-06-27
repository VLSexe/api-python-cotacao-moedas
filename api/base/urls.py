from django.urls import path, include

from rest_framework import routers
from base.views import *



router = routers.DefaultRouter()
router.register(r'cotacao', CotacaoViewSet, basename="cotacao")


urlpatterns = [
    path('cotacao/get-first/', GetFirstSolicitacao.as_view()),
    path('cotacao/<str:code>/', FilaViewSet.as_view({
        'patch': 'partial_update',
    })),
    path('', include(router.urls))
]