from ..services.catalog_service import CatalogService
from typing import Tuple

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
    def get_catalog(self, user_id) -> Tuple[list, int]:
        pass