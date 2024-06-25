from django.urls import path
from . import views
urlpatterns = [
    # path("",views.review,name="reviews"),
    path("",views.review.as_view(),name="reviews"),
    path("review_list",views.review_list.as_view(),name="review_list"),
    path("review_list/<int:id>",views.single_template_view.as_view(),name="single_template"),

    path("review/thank-you",views.ThankYouView.as_view(),name="thanks")
]

