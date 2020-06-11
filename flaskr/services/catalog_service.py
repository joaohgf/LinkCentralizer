from typing import List, Dict, Tuple
from flask_restful import reqparse
import ast
INFOS: List = [
        {"user_id": 1,
            "background": {
                          "colors": ["#FDD900"],
                          "image": "www.imagens.com"
                                    },
            "logo": "s3-testando.aws.amazon.com",
            "links": {
                                      "tinder": "queronamorar.com",
                                      "ifood": "huehuecomida.com",
                          }
                      },
        {"user_id": 2,
            "background": {
                "colors": ["#green"],
                "image": "www.outrasimagens.com"
                          },
            "logo": "s2-testando.alo.amazon.com",
            "links": {
                                  "tinder": "querobeijar.com",
                                  "ifood": "frangaocomida.com", }
                      }
    ]
class CatalogService:
    def __init__(self):
        pass
    ## não usei type hint ainda
    def save(self, user_id) -> Tuple[List, int]:
        arg = reqparse.RequestParser()
        arg.add_argument('background')
        arg.add_argument('logo')
        arg.add_argument('links')
        data : Dict = arg.parse_args()
        background : Dict = ast.literal_eval(data['background'])
        NEW_INFOS : Dict = {
            "user_id": user_id,
             "background": {"colors" : background['colors'],
                            "images": background['image']
                            },
             "logo": data['logo'],
             "links": data['links']
            }
        INFOS.append(NEW_INFOS)
        return NEW_INFOS, 200


    ## Usando lista somente para retornar o valor de infos
    def get(self, user_id)-> Tuple[List, int]:
        if user_id == 0:
            return INFOS
        else:
            for info in INFOS:
                if info['user_id'] == user_id:
                    return info






