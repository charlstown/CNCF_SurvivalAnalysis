from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
import pandas as pd
import json
import time
import math
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# elastic_query:
# This library helps to manage diferent kind of queries and pandas workflow from Elasticsearch.
# To call this library append the path where is located and do an "import elastic_query"

def search_to_pandas(search):
    results = search['hits']['hits']
    df_documents = pd.DataFrame([doc['_source'] for doc in results])
    return df_documents

def documents_to_pandas(documents):
    df_documents = pd.DataFrame(documents)
    return df_documents
