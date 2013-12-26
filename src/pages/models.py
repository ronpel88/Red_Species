# coding: utf-8
from django.db import models

# Create your models here.
class Species(models.Model):

    # seintific_name - שם מדעי (VARCHAR)
    seintific_name = models.CharField(max_length=200, unique=True)

    # # en_name - שם אנגלי (VARCHAR)
    en_name = models.CharField(max_length=200)

    # # he_name - שם עברי (VARCHAR)
    he_name = models.CharField(max_length=200)

    # # author - מחבר (VARCHAR)
    author = models.CharField(max_length=200)

    # # protection_status - האם מוגן (BOOLEAN)
    protection_status = models.BooleanField()

    # # eco_system - מערכת אקולוגית (VARCHAR)
    eco_system_text = models.CharField(max_length=200)

    # # chorotype - כורוטיפ (VARCHAR)
    chorotype_text = models.CharField(max_length=200)

    # # conservation_site - אתר מרכזי לשימור (VARCHAR)
    conservation_site = models.CharField(max_length=200)

    # # rarity - נדירות (INT)
    rarity = models.SmallIntegerField()

    # # red_number - מספר אדום (INT)
    red_number = models.CharField(max_length=200)

    # # iucn_category - קטגוריה לפי איגוד עולמי (CHAR)
    iucn_category = models.CharField(max_length=200)

    # # vulnerability - פגיעות (INT)
    vulnerability = models.SmallIntegerField()

    # attractiveness - אטרקטיביות (INT)
    attractiveness = models.SmallIntegerField()

    # endemism - אנדמיזם (INT)
    endemism = models.SmallIntegerField()

    # peripherality -פריפריאליות (BOOLEAN)
    peripherality = models.SmallIntegerField()

    # disjunctiveness -  צמידות (INT)
    disjunctiveness = models.CharField(max_length=200)

    # number_of_districts - מספר גלילות (INT)
    number_of_districts = models.IntegerField()

    # percentage_of_protected_sites - אחוז האתרים המוגנים (INT)
    percentage_of_protected_sites = models.IntegerField()

    # plant_description - תיאור הצמח (TEXT)
    plant_description = models.TextField()

    # uses - שימושים (TEXT)
    uses = models.TextField()

    # distribution_in_israel - תפוצה בארץ (TEXT)
    distribution_in_israel = models.TextField()

    # habitat - בית גידול (TEXT)
    habitat = models.TextField()

    # global_distribution - תפוצה בעולם (TEXT)
    global_distribution = models.TextField()

    # systematics_and_biogeography - סיסטמטיקה וביוגיאוגרפיה (TEXT)
    systematics_and_biogeography = models.TextField()

    # nature_conservation - שמירת טבעי (TEXT)
    nature_conservation = models.TextField()

    # conservation_recomendations - המלצות לממשק ושימור (TEXT)
    conservation_recomendations = models.TextField()

    # discussion_and_conclusions - סיכום ומסקנות (TEXT)
    discussion_and_conclusions = models.TextField()

    # literature - ספרות (TEXT)
    literature = models.TextField()

    # family_id - מזהה משפחה (INT) - מפתח זר
    # family_id = models.ForeignKey()

    def __unicode__(self):
        return self.seintific_name




















