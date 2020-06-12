from flask_restful import Resource, partial
from typing import Tuple, Dict, List
from facade.catalog_facade import CatalogFacade



class CatalogResource(Resource):
    ## Usando lista somente para conseguir me retornar a lista de dicts
    def get(self, user_id) -> Tuple[Dict,int]:
        catalog : List = CatalogFacade.get_catalog(self, user_id)
        return catalog

    def post(self, user_id)-> Tuple[Dict, int]:
        create_catalog : Dict = CatalogFacade.save_catalog(self, user_id)
        return create_catalog

    def put(self, user_id)-> Tuple[Dict, int]:
        update_catalog : Dict = CatalogFacade.update_catalog(self,user_id)
        return update_catalog