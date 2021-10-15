import json
import pandas as pd
import requests

for page in range(2,8):
    task = []
    with open(f'{page}.json', 'r') as f1:
        list1 = f1.readlines()
        for i in list1:
            task.append(json.loads(i.strip()))

    result = []
    for i in task:
        item = {}
        word = i['word']
        if i['data']['data']:
            definition = i['data']['data']['definitionData']['definitions'][0]['definition']
            pos = i['data']['data']['definitionData']['definitions'][0]['pos']
        else:
            definition = ''
            pos = ''

        result.append({
            'word':word,
            'definition': definition,
            'pos':pos
        })
    df = pd.DataFrame(result,columns=['word','pos','definition'])
    df.to_excel(f'{page}.xls',index=False)
    # print(word + '...' + definition + '...' + pos)
