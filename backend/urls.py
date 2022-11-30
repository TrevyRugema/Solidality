
from django.urls import path,re_path
from backend import logic
from .views import dashboard
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    
    path('', dashboard,name='dashboard'),
    # Member Urls
    path('list-member',logic.PersonList.as_view(),name='list-member'),
    path('view-member/<int:pk>/',logic.PersonView.as_view(),name='view-member'),
    path('create-member',logic.PersonCreate.as_view(),name='create-member'),
    path('edit-member/<int:pk>/',logic.PersonUpdate.as_view(),name='update-member'),
    path('delete-member/<int:pk>/',logic.PersonDelete.as_view(),name='delete-member'),
    # Social Fund Urls
    path('list-fund',logic.SocialFundList.as_view(),name='list-fund'),
    path('view-fund/<int:pk>/',logic.SocialFundView.as_view(),name='view-fund'),
    path('create-fund',logic.SocialFundCreate.as_view(),name='create-fund'),
    path('edit-fund/<int:pk>/',logic.SocialFundUpdate.as_view(),name='update-fund'),
    path('delete-fund/<int:pk>/',logic.SocialFundDelete.as_view(),name='delete-fund'),

    # Saving Urls
    path('savings-list',logic.SavingList.as_view(),name='savings-list'),
    path('view-saving/<int:pk>/',logic.SavingView.as_view(),name='view-saving'),
    path('create-saving',logic.SavingCreate.as_view(),name='create-saving'),
    path('edit-saving/<int:pk>/',logic.SavingUpdate.as_view(),name='update-saving'),
    path('delete-saving/<int:pk>/',logic.SavingDelete.as_view(),name='delete-saving'),

    # Loan Urls
    path('loans-list',logic.LoanList.as_view(),name='loans-list'),
    path('view-loan/<int:pk>/',logic.LoanView.as_view(),name='view-loan'),
    path('create-loan',logic.LoanCreate.as_view(),name='create-loan'),
    path('edit-loan/<int:pk>/',logic.LoanUpdate.as_view(),name='update-loan'),
    path('delete-loan/<int:pk>/',logic.LoanDelete.as_view(),name='delete-loan'),
]
urlpatterns += static(settings.MEDIA_URL, doument_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)