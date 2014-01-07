# coding: utf-8
from django.db import models

# Create your models here.
class Species(models.Model):

    # layer_id - קוד לפי שכבת הנתונים ()
    layer_id = models.IntegerField(unique=True, blank=True, null=True)
    
    # scientific_name - שם מדעי (VARCHAR)
    scientific_name = models.CharField(max_length=200, unique=True)
	
    # scientific_name_synonym - שם מדעי נרדף (VARCHAR)
    scientific_name_synonym = models.CharField(max_length=200, blank=True, null=True)

    # he_name - שם עברי (VARCHAR)
    he_name = models.CharField(max_length=200)
	
    # he_name_synonym -   שם עברי נרדף (VARCHAR)
    he_name_synonym = models.CharField(max_length=200, blank=True, null=True)

    # he_name_punc - שם עברי מנוקד (VARCHAR)
    he_name_punc = models.CharField(max_length=200, blank=True, null=True)

    # en_name - שם אנגלי (VARCHAR)
    en_name = models.CharField(max_length=200, blank=True, null=True)
	
	# arab_name - שם ערבי (VARCHAR)
    arab_name = models.CharField(max_length=200, blank=True, null=True)

    # author - מחבר (VARCHAR)
    author = models.CharField(max_length=200)
	
    # text_participate - משתתף בכתיבה (VARCHAR)
    text_participate = models.CharField(max_length=200, blank=True, null=True))

    # protection_status - סוג הגנה (VARCHAR)
    protection_status = models.CharField(max_length=200)

    # eco_system - מערכת אקולוגית (VARCHAR)
    eco_system_text = models.CharField(max_length=200)

    # chorotype - כורוטיפ (VARCHAR)
    chorotype_text = models.CharField(max_length=200)

    # conservation_site - אתר מרכזי לשימור (VARCHAR)
    conservation_site = models.CharField(max_length=200, blank=True, null=True)

    # rarity - נדירות (INT)
    rarity = models.SmallIntegerField(blank=True, null=True)

    # red_number - מספר אדום (FLOAT)
    red_number = models.FloatField(blank=True, null=True)

    # iucn_category - קטגוריה לפי איגוד עולמי (CHAR)
    iucn_category = models.CharField(max_length=50, blank=True, null=True)

    # vulnerability - פגיעות (INT)
    vulnerability = models.SmallIntegerField(blank=True, null=True)

    # attractiveness - אטרקטיביות (INT)
    attractiveness = models.SmallIntegerField(blank=True, null=True)

    # endemism - אנדמיזם (INT)
    endemism = models.SmallIntegerField(blank=True, null=True)

    # peripherality -פריפריאליות (VARCHAR)
    peripherality = models.CharField(max_length=50,blank=True, null=True)

    # disjunctiveness -  צמידות (INT)
    disjunctiveness = models.SmallIntegerField(blank=True, null=True)

	# past_number_of_districts - מספר גלילות בעבר (INT)
    past_number_of_districts = models.SmallIntegerField(blank=True, null=True)

    # number_of_districts - מספר גלילות (INT)
    number_of_districts = models.SmallIntegerField(blank=True, null=True)

	
    # fragmentation - קיטוע (VARCHAR)
	fragmentation = models.CharField(max_length=50,blank=True, null=True)
	
    # percentage_of_protected_sites - אחוז האתרים המוגנים (FLOAT)
    percentage_of_protected_sites = models.FloatField(blank=True, null=True)
	
    # plant_description - תיאור הצמח (TEXT)
    plant_description = models.TextField()

    # uses - שימושים (TEXT)
    uses = models.TextField(blank=True, null=True)

    # distribution_in_israel - תפוצה בארץ (TEXT)
    distribution_in_israel = models.TextField()

    # habitat - בית גידול (TEXT)
    habitat = models.TextField()

    # global_distribution - תפוצה בעולם (TEXT)
    global_distribution = models.TextField(blank=True, null=True)

    # systematics_and_biogeography - סיסטמטיקה וביוגיאוגרפיה (TEXT)
    systematics_and_biogeography = models.TextField(blank=True, null=True)

    # nature_conservation - שמירת טבעי (TEXT)
    nature_conservation = models.TextField(blank=True, null=True)

    # conservation_recomendations - המלצות לממשק ושימור (TEXT)
    conservation_recomendations = models.TextField(blank=True, null=True)

    # discussion_and_conclusions - סיכום ומסקנות (TEXT)
    discussion_and_conclusions = models.TextField(blank=True, null=True)

    # literature - ספרות (TEXT)
    literature = models.TextField(blank=True, null=True)

	# family_id_num 
    family_id_num = models.SmallIntegerField(db_index=True)
	
    #family_id - מזהה משפחה (INT) - מפתח זר
    #family_id = models.ForeignKey()

    def __unicode__(self):
        return self.seintific_name

    def test_name(self):
        return self.seintific_name == 'Scientific_Name'

class ObsservationTypes(object):
    WI = 4 # escaped to the wild
    LI = 3 # literature site
    EP = 2 # episode site
    A65 = 1 # after 1965
    B65 = 0 # before 1965

    choices = (
               (B65, 'sites from which data was collected prior to 1965, and the species is now extinct.'),
               (A65, 'sites from which data was collected after 1965.'),
               (EP, 'episodic; sites where the plant was observed but no permanent population remains.'),
               (LI, 'uncertain site, based only on reports from the literature but has not been currently verified in the field.'),
               (WI, 'sites where the plant is cultivated (originating from a cultivated population) or introduced. See, for example, Iris pseudacorus.'),
              )


class IUCNLevel(object):
    EX = 6
    EW = 5
    CR = 4
    EN = 3
    VU = 2
    NT = 1
    LC = 0

    choices = (
               (LC, 'Least concern'),
               (EX, 'Extinct'),
               (EW, 'Extinct in the wild'),
               (CR, 'Critically endangered'),
               (EN, 'Endangered'),
               (VU, 'Vulnerable'),
               (NT, 'Near threatened'),
              )



class Families(models.Model):
    # he_name - שם עברי (VARCHAR)
    family_he_name = models.CharField(max_length=100, db_index=True)
    # he_name_synonym - שם משפחה נרדף (VARCHAR)
    family_he_synonym = models.CharField(max_length=100, db_index=True, null=True, blank=True))

    # scientific_name - שם מדעי (VARCHAR)
    family_scientific_name = models.CharField(max_length=100, db_index=True)
    # scientific_name_synonym - שם מדעי נרדף (VARCHAR)
    family_scientific_synonym = models.CharField(max_length=100, db_index=True, null=True, blank=True)
	
    # מזהה משפחה מספרי מהטבלה
	family_id_num = models.SmallIntegerField(db_index=True,unique=True)




    def __unicode__(self):
        return self.family_en_name

class Images(models.Model):

    # species_id - מפתח זר
    species_id = models.ForeignKey(Species)

    # url - כתובת התמונה (URL)
    url = models.URLField()

    # photographer - שם הצלם - (VARCHAR)
    photographer = models.CharField(max_length=50, db_index=True)

    # ordinal - סדר התמונות
    ordinal = models.IntegerField()

    def __unicode(self):
        return self.url


class Obs(models.Model):

    # species_id - מפתח זר
    species_id = models.ForeignKey(Species)

    # obs_x - קו אורך (FLOAT)
    obs_lng = models.FloatField()

    # obs_y - קו רוחב (FLOAT)
    obs_lat = models.FloatField()

    # obs_date - תאריך תצפית (DATE) null
    obs_date = models.DateField(null=True, blank=True)

    # aggregation_num - מספר תצפיות (INT)
    aggregation_num = models.IntegerField()

    # obs_type_id - סוג תצפית (INT) - מפתח זר
    obs_type = models.IntegerField() #int replaced by ENUM - check Udi's example


