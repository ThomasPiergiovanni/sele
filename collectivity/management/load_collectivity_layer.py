from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from collectivity.models.collectivity import Collectivity

collectivity_mapping = {
    'name': 'nom',
    'insee_code': 'insee',
    'activity': 'activity',
    'feat_geom': 'Polygon',
}

collectivity_layer = Path(__file__).resolve().parent / \
    'd:/01_work' / 'communes_idf_3.geojson'


def run(verbose=True):
    lm = LayerMapping(Collectivity, collectivity_layer,
                      collectivity_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
