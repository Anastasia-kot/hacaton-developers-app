from django.urls import include, path
from rest_framework import routers
from api import views
from rest_framework.authtoken import views as rest_views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'real_estate_owner', views.RealEstateOwnerViewSet)

router.register(r'real_estate', views.RealEstatesViewSet)
router.register(r'freelance_agent', views.FreelanceAgentViewSet)
router.register(r'agent_investor', views.AgentInvestorViewSet)
router.register(r'agency', views.AgencyViewSet)
router.register(r'agency_worker', views.AgencyWorkerViewSet)
router.register(r'tag', views.TagViewSet)
router.register(r'price_story', views.PriceStoryViewSet)
router.register(r'gold', views.GoldViewSet)
router.register(r'dollar', views.DollarViewSet)
router.register(r'euro', views.EuroViewSet)
router.register(r'btc', views.BtcViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += [
    path('api-token-auth/', rest_views.obtain_auth_token)
]
