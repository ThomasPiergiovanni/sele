# pylint: disable=E1101,R0201
""" DB management command
"""
from django.contrib.gis.db import models
from django.contrib.gis.utils import LayerMapping
from django.core.management.base import BaseCommand
from pathlib import Path

from collectivity.models.collectivity import Collectivity
from config.settings import BASE_DIR


class Command(BaseCommand):
    """ Reset proposition data from DB. Use it with
    option --all to reset all users as well. This including superuser
    """
    help = "Reset proposition info from DB. Use it with"\
        " option --all to reset all users as well. This including superuser"

    def __init__(self):
        super().__init__()

    def add_arguments(self, parser):
        parser.add_argument(
            '--all',
            action='store_true',
            help='Reset all DB tables values including users and superusers'
        )

    def handle(self, *args, **options):
        self.__drop_collectivity(),
        self.__insert_collectivity(),


    def __drop_collectivity(self):
        """Method thats drop kind objects from DB
        """
        self.__drop_objects(Collectivity)

    def __drop_objects(self, object_class):
        """Manager method thats drop objects entities from DB
        """
        objects = object_class.objects.all()
        objects.delete()

    def __insert_collectivity(self):
        """Method that insert Collecivity geojson objects into DB.
        """
        collectivity_mapping = {
            'name': 'nom',
            'insee_code': 'insee',
            'activity': 'activity',
            'feat_geom': 'Polygon',
        }
        feature_class = (
            Path(BASE_DIR).resolve().parent/'config/settings/data/'
            'communes_idf.geojson'
        )
        collectivity = LayerMapping(
            Collectivity,
            feature_class,
            collectivity_mapping,
            transform=False
        )
        collectivity.save(strict=True, verbose=True)
