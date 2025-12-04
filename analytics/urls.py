from django.urls import path

from analytics.views import InstituteAnalyticsDataEndpoint

urlpatterns = [
    path(
        "analytics/",
        InstituteAnalyticsDataEndpoint.as_view(),
        name="institute-analytics-data",
    ),
]