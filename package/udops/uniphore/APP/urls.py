from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('count/', views.get_udops_count),
    path('summary/',views.summary),
    path('list/',views.list_by_string_name),
    path('search_by_name/',views.search_corpus_by_name),
    #path('search_by_string/',views.list_by_string_name),
    path('upsert/', views.upsert),
    path('donut/', views.donut),
    path('summary_custom/',views.summary_custom),
    path('update_custom_field/',views.update_custom_field),
    ### dataset API ### **************************************
    path('udops/dataset/summary/',views.dataset_summary),
    path('udops/dataset/list/',views.dataset_list),
    path('udops/dataset/search/',views.dataset_search),
    path('udops/dataset/update/',views.update_dataset),
    path('udops/dataset/corpus_list/',views.dataset_corpus_list),

    path('udops/user/list/',views.get_user_list),
    path('udops/user/list/',views.update_user),
    path('udops/user/list/',views.get_team_list),
    path('udops/user/list/',views.get_user_list),
    path('udops/user/list/',views.get_user_list),

]
