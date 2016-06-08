from elasticsearch import Elasticsearch


def main():
    es = Elasticsearch()
    es.indices.create(index='person-index', ignore=400)
    return es

if __name__ == '__main__':
    main()
