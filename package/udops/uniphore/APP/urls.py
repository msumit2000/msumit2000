from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('count/', views.get_udops_count),
    path('summary/',views.summary),
    path('list/',views.get_corpus_list),
    path('search_by_name/',views.search_corpus_by_name),
    path('search_by_string/',views.list_by_string_name),
    path('upsert/', views.upsert),
    path('donut/', views.donut),
    path('summary_custom/',views.summary_custom),
    path('update_custom_field/',views.update_custom_field),
        ### dataset API #### 
    path('udops/dataset/summary/',views.dataset_summary),
    path('udops/dataset/list/',views.dataset_list),
    path('udops/dataset/search/',views.dataset_search),
    path('udops/dataset/update/',views.update_dataset),
    path('udops/dataset/corpus_list/',views.dataset_corpus_list),
    ### user management API ###
    path('udops/user/list/',views.list_user),
    path('udops/user/upsert_user/',views.upsert_user),
    path('udops/team/list/',views.team_list),
    path('udops/team/upsert/',views.team_upsert),
    path('udops/team/add_users/',views.add_users_team),
    path('udops/team/remove_users/',views.remove_users_team),
    path('udops/user/access_permission/',views.grant_corpus),
    path('udops/user/remove_permission/',views.remove_user_corpus),
    path('udops/user/corpus_access_list_write/',views.grant_corpus_list_write),
    path('udops/user/corpus_access_list_read/',views.grant_corpus_list_read),    

]
