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
    author = models.CharField(max_length=200)

    # protection_status - האם מוגן (BOOLEAN)
    protection_status = models.BooleanField()

    # eco_system - מערכת אקולוגית (VARCHAR)
    eco_system_text = models.CharField(max_length=200)

    # chorotype - כורוטיפ (VARCHAR)
    chorotype_text = models.CharField(max_length=200)

    # conservation_site - אתר מרכזי לשימור (VARCHAR)
    conservation_site = models.CharField(max_length=200)

    # rarity - נדירות (INT)
    rarity = models.SmallIntegerField()

    # red_number - מספר אדום (INT)
    red_number = models.SmallIntegerField()

    # iucn_category - קטגוריה לפי איגוד עולמי (CHAR)
    iucn_category = models.CharField(max_length=200)

    # vulnerability - פגיעות (INT)
    vulnerability = models.SmallIntegerField()

    # attractiveness - אטרקטיביות (INT)
    attractiveness = models.SmallIntegerField()

    # endemism - אנדמיזם (INT)
    endemism = models.SmallIntegerField()

    # peripherality -פריפריאליות (BOOLEAN)
    peripherality = models.SmallIntegerField()

    # disjunctiveness -  צמידות (INT)
    disjunctiveness = models.SmallIntegerField()

    # number_of_districts - מספר גלילות (INT)
    number_of_districts = models.SmallIntegerField()

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























