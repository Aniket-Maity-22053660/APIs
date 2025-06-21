from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('books', views.MyBooksView, basename="books")
urlpatterns = [
    path('', include(router.urls))
]

'''
view1 = views.MyBooksView.as_view({
    'get' : 'list',
    'post' : 'create'
})

view2 = views.MyBooksView.as_view({
    'get' : 'retrieve',
    'put' : 'update',
    'patch' : 'partial_update',
    'delete' : 'destroy'
})

urlpatterns = [
    path('books', view1, name="books"),
    path('books/<int:pk>', view2, name="books-id")
]
'''
'''
urlpatterns = [
    path('books/', views.MyBooksViewAll.as_view(), name="books"),
    path('books/<int:pk>', views.MyBooksViewDetail.as_view(), name="books-pk")
]
'''
