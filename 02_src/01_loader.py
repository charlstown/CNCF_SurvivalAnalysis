from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
import json
import time

start = time.time()

elastic = Elasticsearch(["http://127.0.0.1:9200"])
index = "clients"

path = "../data/cncf_git_data.json"

data = []
for line in open(path, 'r'):
    data.append(json.loads(line))

print(len(data))

for idx, doc in enumerate(data):
    print('Starting indexing...', '\n')
    client.index(index=doc['_index'], doc_type=doc['_type'], id=doc['_id'], body=doc['_source'])
    if idx%5000 == 0:
        print(idx)


end = time.time()-start
print(round(end, 2))