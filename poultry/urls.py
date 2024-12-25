from django.urls import path
from .views import *
# from .views import fetch_individual_egg_dashboard_api
urlpatterns = [ 
    # BACK_END API FOR BREED CRUD
    path('breed/add/', add_breed_api, name='add_breed_api'),
    path('breed/list/', fetch_breed_api, name='fetch_breed_api'),
    path('breed/delete/<int:pk>/', delete_breed_api, name='delete_breed_api'),
    path('breed/breed/<int:pk>/', fetch_one_breed_api, name='fetch one breed'),
    path('breed/update/<int:pk>/', update_breed_api, name='update breed'),
    
    # BACK_END API FOR HOUSE CRUD
    path('house/add/', add_house_api, name='add_house_api'),
    path('house/list/', fetch_house_api, name='fetch_house_api'),
    path('house/delete/<int:pk>/', delete_house_api, name='delete_house_api'),
    path('house/house/<int:pk>/', fetch_one_house_api, name='fetch one house'),
    path('house/update/<int:pk>/', update_house_api, name='update house'),
    
    # BACK_END API FOR INDIVIDUAL CHICKEN CHICKEN CRUD
    path('chicken/add/', add_chicken_api, name='add_chicken_api'),
    path('chicken/list/', fetch_chicken_api, name='fetch_chicken_api'),
    path('chicken/delete/<int:pk>/', delete_chicken_api, name='delete_chicken_api'),
    path('chicken/chicken/<int:pk>/', fetch_one_chicken_api, name='fetch one chicken'),
    path('chicken/update/<int:pk>/', update_chicken_api, name='update chicken'),

    # BACK_END API FOR REQUESTER  REQUESTER CRUD
    path('requester/add/', add_requester_api, name='add_requester_api'),
    path('requester/list/', fetch_requester_api, name='fetch_requester_api'),
    path('requester/delete/<int:pk>/', delete_requester_api, name='delete_requester_api'),
    path('requester/requester/<int:pk>/', fetch_one_requester_api, name='fetch_one_requester_api'),
    path('requester/update/<int:pk>/', update_requester_api, name='update_requester_api'),
    
    # BACK_END API FOR CHICKENDISTRIBUTION CRUD
    path('chickendistribution/add/', add_chickendistribution_api, name='add_chickendistribution_api'),
    path('chickendistribution/list/', fetch_chickendistribution_api, name='fetch_chickendistribution_api'),
    path('chickendistribution/delete/<int:pk>/', delete_chickendistribution_api, name='delete_chickendistribution_api'),
    path('chickendistribution/chickendistribution/<int:pk>/', fetch_one_chickendistribution_api, name='fetch_one_chickendistribution_api'),
    path('chickendistribution/update/<int:pk>/', update_chickendistribution_api, name='update_chickendistribution_api'),

    # BACKE_END API FOR INDIVIDUAL BODYWEIGHT CRUD
    path('bodyweight/add/', add_bodyweight_api, name='add_bodywieght_api'),
    path('bodyweight/list/', fetch_bodyweight_api, name='fetch_bodywieght_api'),
    path('bodyweight/delete/<int:pk>/', delete_bodyweight_api, name='delete_bodywieght_api'),
    path('bodyweight/bodyweight/<int:pk>/', fetch_one_bodyweight_api, name='fetch one bodywieght'),
    path('bodyweight/update/<int:pk>/', update_bodyweight_api, name='update bodywieght'),

    # BACK_END API FOR INDIVIDUAL INTAKE
    path('intake/add/', add_intake_api, name='add intake api'),
    path('intake/list/', fetch_intake_api, name='fetch intake api'),
    path('intake/delete/<int:pk>/', delete_intake_api, name='delete intake api'),
    path('intake/intake/<int:pk>/', fetch_one_intake_api, name='fetch one intake'),
    path('intake/update/<int:pk>/', update_intake_api, name='update intake'),

    # BACK_END API FOR INDIVIDUAL EGG PRODUCTION
    path('egg/add/', add_egg_api, name='add egg api'),
    path('egg/list/', fetch_egg_api, name='fetch eggg api'),
    path('egg/delete/<int:pk>/', delete_egg_api, name='delete egg api'),
    path('individual_egg_dashboard/list/', fetch_individual_egg_dashboard_api, name='fetch_individual_egg_dashboard_api'),
    path('egg/egg/<int:pk>/', fetch_one_egg_api, name='fetch one egg'),
    path('egg/update/<int:pk>/', update_egg_api, name='update egg'),
    
    # BACK_END API FOR GROUP CHICKEN 
    path('group_chicken/add/', add_group_chicken_api, name='add group chicken api'),
    path('group_chicken/list/', fetch_group_chicken_api, name='fetch group chicken api'),
    path('group_chicken/delete/<int:pk>/', delete_group_chicken_api, name='delete group chicken api'),
    path('group_chicken/group_chicken/<int:pk>/', fetch_one_group_chicken_api, name='fetch one group chicken'),
    path('group_chicken/update/<int:pk>/', update_group_chicken_api, name='update group chicken'),

    # BACKE_END API FOR GROUP BODYWEIGHT CRUD
    path('group_bodyweight/add/', add_group_bodyweight_api, name='add_group_bodywieght_api'),
    path('group_bodyweight/list/', fetch_group_bodyweight_api, name='fetch_group_bodywieght_api'),
    path('group_bodyweight/delete/<int:pk>/', delete_group_bodyweight_api, name='delete_group_bodywieght_api'),
    path('group_bodyweight/group_bodyweight/<int:pk>/', fetch_one_group_bodyweight_api, name='fetch one bodywieght'),
    path('group_bodyweight/update/<int:pk>/', update_group_bodyweight_api, name='update group group bodywieght'),

    # BACK_END API FOR GROUP INTAKE
    path('group_intake/add/', add_group_intake_api, name='add group_intake api'),
    path('group_intake/list/', fetch_group_intake_api, name='fetch group_intake api'),
    path('group_intake/delete/<int:pk>/', delete_group_intake_api, name='delete group_intake api'),
    path('group_intake/group_intake/<int:pk>/', fetch_one_group_intake_api, name='fetch group_one intake'),
    path('group_intake/update/<int:pk>/', update_group_intake_api, name='update group_intake'),

    # BACK_END API FOR GROUP EGG PRODUCTION
    path('group_egg/add/', add_group_egg_api, name='add group_egg api'),
    path('group_egg/list/', fetch_group_egg_api, name='fetch group_eggg api'),
    # For Dashboard Purpose
    path('group_egg_dashboard/list/', fetch_new_group_egg_api, name='fetch_new_group_egg_api'),
    path('group_egg/delete/<int:pk>/', delete_group_egg_api, name='delete group_egg api'),
    path('group_egg/group_egg/<int:pk>/', fetch_one_group_egg_api, name='fetch one group_egg'),
    path('group_egg/update/<int:pk>/', update_group_egg_api, name='update group_egg'),

    # BACK_END API FOR GROUP DEATH
    path('group_death/add/', add_group_death_api, name='add group_death api'),
    path('group_death/list/', fetch_group_death_api, name='fetch group_death api'),
    path('group_death/delete/<int:pk>/', delete_group_death_api, name='delete group_death api'),
    path('group_death/group_death/<int:pk>/', fetch_one_group_death_api, name='fetch one group_death'),
    path('group_death/update/<int:pk>/', update_group_death_api, name='update group_death'),

    # BACK_END API FOR GROUP CULLING
    path('group_culling/add/', add_group_culling_api, name='add group_culling api'),
    path('group_culling/list/', fetch_group_culling_api, name='fetch group_culling api'),
    path('group_culling/delete/<int:pk>/', delete_group_culling_api, name='delete group_culling api'),
    path('group_culling/group_culling/<int:pk>/', fetch_one_group_culling_api, name='fetch one group_culling'),
    path('group_culling/update/<int:pk>/', update_group_culling_api, name='update group_culling'),

    # BACK_END API FOR GROUP REPLACEMENT
    path('group_replacement/add/', add_group_replacement_api, name='add group_replacement api'),
    path('group_replacement/list/', fetch_group_replacement_api, name='fetch group_replacement api'),
    path('group_replacement/delete/<int:pk>/', delete_group_replacement_api, name='delete group_replacement api'),
    path('group_replacement/group_replacement/<int:pk>/', fetch_one_group_replacement_api, name='fetch one group_replacement'),
    path('group_replacement/update/<int:pk>/', update_group_replacement_api, name='update group_replacement'),

    # BACK_END API FOR INDIVIDUAL DEATH
    path('individual_death/add/', add_individual_death_api, name='add individual_death api'),
    path('individual_death/list/', fetch_individual_death_api, name='fetch individual_death api'),
    path('individual_death/delete/<int:pk>/', delete_individual_death_api, name='delete individual_death api'),
    path('individual_death/individual_death/<int:pk>/', fetch_one_individual_death_api, name='fetch one individual_death'),
    path('individual_death/update/<int:pk>/', update_individual_death_api, name='update individual_death'),

    # BACK_END API FOR GROUP VACCINATION
    path('group_vaccine/add/', add_group_vaccine_api, name='add group_vaccine api'),
    path('group_vaccine/list/', fetch_group_vaccine_api, name='fetch group_vaccine api'),
    path('group_vaccine/delete/<int:pk>/', delete_group_vaccine_api, name='delete group_vaccine api'),
    path('group_vaccine/group_vaccine/<int:pk>/', fetch_one_group_vaccine_api, name='fetch one group_vaccine'),
    path('group_vaccine/update/<int:pk>/', update_group_vaccine_api, name='update group_vaccine'),

    
    # BACK_END API FOR INDIVIDUAL VACCINATION
    path('individual_vaccine/add/', add_individual_vaccine_api, name='add individual_vaccine api'),
    path('individual_vaccine/list/', fetch_individual_vaccine_api, name='fetch individual_vaccine api'),
    path('individual_vaccine/delete/<int:pk>/', delete_individual_vaccine_api, name='delete individual_vaccine api'),
    path('individual_vaccine/individual_vaccine/<int:pk>/', fetch_one_individual_vaccine_api, name='fetch one individual_vaccine'),
    path('individual_vaccine/update/<int:pk>/', update_individual_vaccine_api, name='update individual_vaccine'),

    
    # BACK_END API FOR HATCHERY RECORD
    path('hatchery_record/add/', add_hatchery_record_api, name='add hatchery_record api'),
    path('hatchery_record/list/', fetch_hatchery_record_api, name='fetch individualhatchery_record_vaccine api'),
    path('hatchery_record/delete/<int:pk>/', delete_hatchery_record_api, name='delete hatchery_record api'),
    path('hatchery_record/hatchery_record/<int:pk>/', fetch_one_hatchery_record_api, name='fetch one hatchery_record'),
    path('hatchery_record/update/<int:pk>/', update_hatchery_record_api, name='update hatchery_record'),

    
    # BACK_END API FOR INCUBATION RECORD
    path('incubation_record/add/', add_incubation_record_api, name='add incubation_record api'),
    path('incubation_record/list/', fetch_incubation_record_api, name='fetch incubation_record api'),
    path('incubation_record/delete/<int:pk>/', delete_incubation_record_api, name='delete incubation_record api'),
    path('incubation_record/incubation_record/<int:pk>/', fetch_one_incubation_record_api, name='fetch one incubation_record'),
    path('incubation_record/update/<int:pk>/', update_incubation_record_api, name='update incubation_record'),

    
    # BACK_END API FOR HATCHER SUMMARY
    path('hatchery_summary/add/', add_hatchery_summary_api, name='add hatchery_summary api'),
    path('hatchery_summary/list/', fetch_hatchery_summary_api, name='fetch hatchery_summary api'),
    path('hatchery_summary/delete/<int:pk>/', delete_hatchery_summary_api, name='delete hatchery_summary api'),
    path('hatchery_summary/hatchery_summary/<int:pk>/', fetch_one_hatchery_summary_api, name='fetch one hatchery_summary'),
    path('hatchery_summary/update/<int:pk>/', update_hatchery_summary_api, name='update hatchery_summary'),

    # KPI
    path('kpi/fetch_egg_production_per_group_api/', fetch_egg_production_per_group_api, name='fetch_total_egg_production_api'),
    path('kpi/fetch_feed_intake_refusal_per_group_api/', fetch_feed_intake_refusal_per_group_api, name='fetch_feed_intake_refusal_per_group_api'),
    path('kpi/fetch_death_per_group_api/', fetch_death_per_group_api, name='fetch_death_per_group_api'),
    path('kpi/fetch_culling_per_group_api/', fetch_culling_per_group_api, name='fetch_culling_per_group_api'),
    path('kpi/fetch_replacement_per_group_api/', fetch_replacement_per_group_api, name='fetch_replacement_per_group_api'),
    path('kpi/fetch_body_weight_per_group_api/', fetch_body_weight_per_group_api, name='fetch_body_weight_per_group_api'),
    path('kpi/fetch_vaccination_count_per_group_api/', fetch_vaccination_count_per_group_api, name='fetch_vaccination_count_per_group_api'),
    path('kpi/count_chicken_groups_api/', count_chicken_groups_api, name='count_chicken_groups_api'),

    path('kpi/fetch_egg_production_per_individual_chicken_api/', fetch_egg_production_per_individual_chicken_api, name='fetch_egg_production_per_individual_chicken_api'),
    path('kpi/fetch_feed_intake_refusal_per_individual_chicken_api/', fetch_feed_intake_refusal_per_individual_chicken_api, name='fetch_feed_intake_refusal_per_individual_chicken_api'),
    path('kpi/fetch_body_weight_per_individual_chicken_api/', fetch_body_weight_per_individual_chicken_api, name='fetch_body_weight_per_individual_chicken_api'),
    path('kpi/fetch_vaccination_count_per_individual_chicken_api/', fetch_vaccination_count_per_individual_chicken_api, name='fetch_vaccination_count_per_individual_chicken_api'),
    path('kpi/fetch_individual_death_count/', fetch_individual_death_count, name='fetch_individual_death_count'),
    path('kpi/count_individual_chickens_api/', count_individual_chickens_api, name='count_individual_chickens_api'),

]
