from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name='user'
urlpatterns=[
    path('',views.UserHome.as_view(), name='userhome'),
    path('editprofile/',views.EditProfile.as_view(), name='edit-profile'),
    path('restaurant/', include('restaurant.urls', namespace='restaurant')),
    path('deliveryperson/', include('deliveryperson.urls', namespace='deliveryperson')),
    path('restaurantmenu/', views.RestaurantMenu.as_view(),name='restaurantmenu'),
    path('cart/', views.Cart.as_view(),name='cart'),
    path('address/', views.AddAddress.as_view(),name='address'),
    path('orderdetails/', views.OrderDetailsView.as_view(),name='orderdetails'),
    path('myoffers/', views.MyOffersView.as_view(),name='myoffers'),
    path('rating/<int:restaurant_id>/', views.RatingView.as_view(), name='rating'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
