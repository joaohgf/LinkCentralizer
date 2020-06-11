from typing import List, Dict, Tuple

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

    def save(self):
        pass
    ## Usando lista somente para retornar o valor de infos
    def get(self, user_id)-> Tuple[List, int]:
        for info in INFOS:
            if info['user_id'] == user_id:
                return info






