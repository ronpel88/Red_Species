# coding: utf-8
from django.core.management.base import BaseCommand
import csv
from pages.models import Species
import codecs


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Starting to import data from csv to model")
        with codecs.open("csv/RedSpeciesDataTable.csv", 'r', 'utf-8', 'ignore') as f:
            r = csv.DictReader(f)
            for d in r:
                species = Species(seintific_name=d['Scientific_Name'],
                            en_name=d['English_Name'],
                            he_name=d['Scientific_Name'],
                            author=d['Scientific_Name'],
                            protection_status=bool(d['Protection_by_Law_State']),
                            eco_system_text=d['Ecosystem'],
                            chorotype_text=d['Chorotype'],
                            conservation_site=d['Main_conservation_sites'],
                            rarity=int(d['Vulnerability']),
                            red_number=d['Red_index'],
                            iucn_category=d['IUCN_Category'],
                            vulnerability=int(d['Vulnerability']),
                            attractiveness=int(d['Attractiveness']),
                            endemism=int(d['Endemism']),
                            peripherality=bool(d['Peripherality']),
                            disjunctiveness=d['Disjunctiveness'],
                            number_of_districts=int(d['Number_of_Districts']),
                            percentage_of_protected_sites=int(d['Percentage_of_protected_sites']),
                            plant_description=d['Plant_Description'],
                            uses=d['Uses'],
                            distribution_in_israel=d['Distribution_in_Israel'],
                            habitat=d['Habitat'],
                            global_distribution=d['Global_Distribution'],
                            systematics_and_biogeography=d['Systematics_and_Biogeography'],
                            nature_conservation=d['Nature_Conservation'],
                            conservation_recomendations=d['Recommendations_for_Management_and_Conservation'],
                            discussion_and_conclusions=d['Discussion_and_conclusions'],
                            literature=d['Literature'])
                species.save()




        self.stdout.write("Done!")
        # l = Species.objects.all()
        # for x in l:
        #     print x