from flask import Flask

from Services import ElasticSearchService as elasticSearch
elasticSearchService = elasticSearch.ElasticSearchService

app = Flask(__name__)


@app.route('/test')
def home_page():
    return 'working'

@app.route('/search/<string:_query>', methods=[constants.GET])
@cross_origin()
def search(_query):
    return elasticSearchService.search_data(_query)

if __name__ == '__main__':
    app.run()
