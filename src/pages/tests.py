from django.test import TestCase
from pages.models import Species

species = Species(seintific_name='Scientific_Name',
        en_name='English_Name',
        # he_name=d['Scientific_Name'],
        # author=d['Scientific_Name'],
        protection_status='Protection_by_Law_State',
        eco_system_text='Ecosystem',
        chorotype_text='Chorotype',
        conservation_site='Main_conservation_sites',
        rarity=1,
        red_number=1,
        iucn_category='IUCN_Category',
        vulnerability=1,
        attractiveness=1,
        endemism=1,
        peripherality=True,
        disjunctiveness=1,
        number_of_districts=1,
        percentage_of_protected_sites=1,
        plant_description='Plant_Description',
        uses='Uses',
        distribution_in_israel='Distribution_in_Israel',
        habitat='Habitat',
        global_distribution='Global_Distribution',
        systematics_and_biogeography='Systematics_and_Biogeography',
        nature_conservation='Nature_Conservation',
        conservation_recomendations='Recommendations_for_Management_and_Conservation',
        discussion_and_conclusions='Discussion_and_conclusions',
        literature='Literature')

species.save()

def test(self):
    if self.test_name() == True:
        print "True"
        return True
    else:
        print "False"
        return False
test(species)

