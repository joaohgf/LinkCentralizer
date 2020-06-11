from services.catalog_service import CatalogService
from typing import Tuple, List, Dict

class CatalogFacade:
    """ class responsible for seeking catalog services """
    def __init__(self) -> None:
        self._catalog_service = CatalogService()

    def save_catalog(self, user_id) -> Tuple[List, int]:
        catalog : List = CatalogService.save(self, user_id)
        return catalog

    ## Usando lista somente para conseguir me retornar a lista de dicts
    def get_catalog(self, user_id) -> Tuple[List, int]:
        catalog : List = CatalogService.get(self, user_id)
        return catalog, 200