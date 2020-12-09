from builtins import classmethod
from elasticsearch import Elasticsearch
from flask import jsonify

es = Elasticsearch(['https://search-srinivaselastic-hyo5dtu2vjdskmlntiwx4vhqb4.ap-south-1.es.amazonaws.com'],
                   http_auth=('srinivaselastic', 'Sriamazon@1994'))


class ElasticSearchService:

    @classmethod
    def insert_data(cls, email_address, user_id):
        body = {
            'email_address': email_address
        }
        es.index(index='srinivas_elasticsearch', doc_type='title', id=user_id, body=body)

    @classmethod
    def search_data(cls, _query):
        body = {
            "query": {
                "query_string": {
                    "query": "*" + _query + "*"
                }
            }
        }
        res = es.search(index="srinivas_elasticsearch", doc_type="title", body=body)
        return jsonify(res)

    @classmethod
    def delete_record(cls, user_id):
        es.delete(index='srinivas_elasticsearch', id=user_id)
