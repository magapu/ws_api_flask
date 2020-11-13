from builtins import classmethod
from elasticsearch import Elasticsearch

es = Elasticsearch('http://localhost:9200/')


class ElasticSearchService:

    @classmethod
    def insert_data(cls, email_address, user_id):
        body = {
            'email_address:': email_address
        }
        es.index(index='srinivas_elasticsearch', doc_type='title', id=user_id, body=body)
