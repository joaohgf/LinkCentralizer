from flask_restful import Resource, partial, reqparse
from typing import Tuple, Dict, List

infos: List = [
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


class CatalogResource(Resource):
    def get(self, user_id) -> Tuple[list, int]:
            for info in infos:
                if info['user_id'] == user_id:
                    return info, 200
            return List['error'], 404

    @staticmethod
    def post() -> Tuple[Dict[str, str], int]:
        """
        here is the POST method documentation
        :return:
        """
        pass
