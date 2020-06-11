from services.catalog_service import CatalogService
from typing import Tuple, List

class CatalogFacade:
    """ class responsible for seeking catalog services """
    def __init__(self) -> None:
        self._catalog_service = CatalogService()

    def save_catalog(self, data) -> None:
        """
        facade method to save the catalog in the database
        :param data:
        :return:
        """
        pass

    ## Usando lista somente para conseguir me retornar a lista de dicts
    def get_catalog(self, user_id) -> Tuple[str, int]:
        catalog : Tuple = CatalogService.get(self, user_id)
        return catalog