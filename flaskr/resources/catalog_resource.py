from flask_restful import Resource, partial, reqparse
from typing import Tuple, Dict, List
from facade.catalog_facade import CatalogFacade



class CatalogResource(Resource):
    ## Usando lista somente para conseguir me retornar a lista de dicts
    def get(self, user_id) -> Tuple[str,int]:
        catalog : str = CatalogFacade.get_catalog(self, user_id)
        return catalog, 200

    @staticmethod
    def post() -> Tuple[Dict[str, str], int]:
        pass
