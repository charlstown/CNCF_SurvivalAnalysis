from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
import json
import time
import math

# elastic_loader:
# This library helps to manage load and upload info and documents to Elasticsearch.
# To call this library append the path where is located and do an "import elastic_loader"

def load_json(path):
    print('Loading json file...', '\n')
    start = time.time()
    path_open = open(path, 'r').readlines()
    count = 0
    file = []
    try:
        for i, line in enumerate(path_open):
            file.append(json.loads(line))
            percent = math.trunc(((i+1)/len(path_open))*100)
            if (percent >= 25 and count == 0) or (percent > 50 and count == 1) or (percent > 75 and count == 2) or percent == 100:
                count += 1
                end = round(time.time() - start, 2)
                print("{} percent completed: {} documents in {}s".format(percent, i+1, end))
        print('\n')
        print('json file was loaded succesfully!')
    except Exception as e:
        print(e)
    return file


def upload_to_index(client, index_name, data):
    start = time.time()
    print('Starting upload...', '\n')
    count = 0
    for i, doc in enumerate(data):
        client.index(index=index_name, id=doc['_id'], body=doc['_source'])
        percent = math.trunc(((i+1)/len(data))*100)
        if (percent >= 25 and count == 0) or (percent > 50 and count == 1) or (
                percent > 75 and count == 2) or percent == 100:
            count += 1
            end = round(time.time() - start, 2)
            print("{} percent completed: {} documents in {}s".format(percent, i + 1, end))
    print('\n')
    print('Data was uploaded succesfully!')
