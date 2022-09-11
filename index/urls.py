from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="am"),
    path("about",views.about,name="ab"),
    path("blog-single",views.blog_single,name="bs"),
    path("blog",views.blog,name="bg"),
    path("checkout",views.checkout,name="ch"),
    path("contact",views.contact,name="co"),
    path("food-page",views.food_page,name="fp"),
    path("<int:ak>",views.food_pagecat,name="fps"),
    
    path("food-page2",views.food_page2,name="fb2"),
    path("gallery",views.gallery,name="ga"),
    path("homepage2",views.homepage2,name="ho2"),
    path("homepage3",views.homepage3,name="ho3"),
    path("homepage4",views.homepage4,name="ho4"),
    path("login",views.login,name="lo"),
    path("menu",views.menu,name="me"),
    path("shopping-cart",views.shopping_cart,name="sh"),
    path("signup",views.signup,name="si"),
    path("single-dish",views.single_dish,name="sin"),
    path("single-food",views.single_food,name="sif"),
    path("error",views.error,name="err"),
]
