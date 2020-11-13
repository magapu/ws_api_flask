from builtins import classmethod
from elasticsearch import Elasticsearch
from flask import request, jsonify

es = Elasticsearch('http://localhost:9200/')


class ElasticSearchService:

    @classmethod
    def insert_data(cls, email_address, user_id):
        body = {
            'email_address:': email_address
        }
        es.index(index='srinivas_elasticsearch', doc_type='title', id=user_id, body=body)

    @classmethod
    def search_data(cls):
        email_address = request.json['email_address']
        body = {
            "query": {
                "multi_match": {
                    "query": email_address
                }
            }
        }
        res = es.search(index="srinivas_elasticsearch", doc_type="title", body=body)
        return jsonify(res)
