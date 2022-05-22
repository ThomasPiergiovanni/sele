# pylint: disable=E1101, R0201, W0106, W1514
"""ResetCollectivity module.
"""
import json
from pathlib import Path

from django.contrib.gis.utils import LayerMapping
from django.core.management.base import BaseCommand

from collectivity.models import Collectivity, PostalCode
from config.settings import BASE_DIR


class Command(BaseCommand):
    """Reset Collectivity data from DB.
    """

    help = "Reset Collectivity data from DB. Use it with"

    def __init__(self):
        super().__init__()
        self.testing = False
        self.postal_code_path = (
            Path(BASE_DIR).resolve().parent/'config/settings/data/'
            'laposte_hexasmall.json'
        )
        self.collectivity_path = (
            Path(BASE_DIR).resolve().parent/'config/settings/data/'
            'commune_fr.geojson'
        )

    def handle(self, *args, **options):
        """Method that reset Collectivity data from DB.
        """
        self.__drop_collectivity(),
        self.__drop_postal_code(),
        if self.testing:
            self.postal_code_path = (
                Path(BASE_DIR).resolve().parent/'config/settings/data/'
                'postal_code_4_tests.json'
            )
            self.collectivity_path = (
                Path(BASE_DIR).resolve().parent/'config/settings/data/'
                'communes_idf.geojson'
            )
        self.__insert_postal_code(),
        self.__insert_collectivity(),
        self.__set_collectivity_postal_code()

    def __drop_collectivity(self):
        """Method thats drop Collectivity from DB.
        """
        self.__drop_objects(Collectivity)

    def __drop_objects(self, object_class):
        """Manager method thats drop objects from DB
        """
        objects = object_class.objects.all()
        objects.delete()

    def __insert_collectivity(self):
        """Method that insert Collectivity geojson into DB.
        """
        collectivity_mapping = {
            'name': 'nom',
            'insee_code': 'insee',
            'activity': 'activity',
            'feat_geom': 'MultiPolygon',
        }
        feature_class = self.collectivity_path
        collectivity = LayerMapping(
            Collectivity,
            feature_class,
            collectivity_mapping,
            transform=False
        )
        collectivity.save(strict=True, verbose=False)

    def __drop_postal_code(self):
        """Method that drop postal code objects from DB
        """
        self.__drop_objects(PostalCode)

    def __insert_postal_code(self):
        """Method that insert PostalCode into DB.
        """
        source_data = self.postal_code_path
        with open(source_data) as file:
            places = json.load(file)

        for place in places:
            postal_code = PostalCode(
                postal_code=place['fields']['code_postal'],
                insee_code=place['fields']['code_commune_insee']
            )
            postal_code.save()

    def __set_collectivity_postal_code(self):
        """Method that sets Collectivity postal_code.
        """
        postal_codes = PostalCode.objects.all()
        last_postal_code = PostalCode.objects.all().last()
        collectivities = Collectivity.objects.all()
        for postal_code in postal_codes:
            for collectivity in collectivities:
                if postal_code.insee_code == collectivity.insee_code:
                    collectivity.postal_code_id = postal_code.id
                    collectivity.save()
        for collectivity in collectivities:
            if collectivity.postal_code_id is None:
                collectivity.postal_code_id = last_postal_code.id
                collectivity.save()
