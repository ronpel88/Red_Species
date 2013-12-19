# coding: utf-8
from django.db import models

# Create your models here.
class Specie(models.Model):

    # seintific_name - שם מדעי (VARCHAR)
    seintific_name = models.CharField(max_length=200)
    # en_name - שם אנגלי (VARCHAR)
    en_name = models.CharField(max_length=200)
    # he_name - שם עברי (VARCHAR)
    he_name = models.CharField(max_length=200)
    # author - מחבר (VARCHAR)


    # en_synonym - שמות נרדפים באנגלית (VARCHAR)
    # he_synonym - שמות נרדפים בעברית (VARCHAR)
    # protection_status - האם מוגן (BOOLEAN)
    # eco_system - מערכת אקולוגית (VARCHAR)
    # chorotype - כורוטיפ (VARCHAR)
    # conservation_site - אתר מרכזי לשימור (VARCHAR)
    # rarity - נדירות (INT)
    # red_number - מספר אדום (INT)
    # iucn_category - קטגוריה לפי איגוד עולמי (CHAR)
    # vulnerability - פגיעות (INT)
    # attractiveness - אטרקטיביות (INT)
    # endemism - אנדמיזם (INT)
    # peripherality -פריפריאליות (BOOLEAN)
    # disjunctiveness -  צמידות (INT)
    # number_of_districts - מספר גלילות (INT)
    # percentage_of_protected_sites - אחוז האתרים המוגנים (INT)
    # plant_description - תיאור הצמח (TEXT)
    # uses - שימושים (TEXT)
    # distribution_in_israel - תפוצה בארץ (TEXT)
    # habitat - בית גידול (TEXT)
    # global_distribution - תפוצה בעולם (TEXT)
    # systematics_and_biogeography - סיסטמטיקה וביוגיאוגרפיה (TEXT)
    # nature_conservation - שמירת טבעי (TEXT)
    # conservation_recomendations - המלצות לממשק ושימור (TEXT)
    # discussion_and_conclusions - סיכום ומסקנות (TEXT)
    # literature - ספרות (TEXT)

# family_id - מזהה משפחה (INT) - מפתח זר























