import json
import pandas as pd
import requests

for page in range(2, 4):
    word_list = []
    with open(f'{page}X.txt', 'r') as f1:
        list1 = f1.readlines()
        for i in list1:
            word_list.append(i.strip().lower())

    word_map = {}
    with open(f'{page}X.json', 'r') as f1:
        list1 = f1.readlines()
        for i in list1:
            data = json.loads(i.strip())
            word = data['word']
            word_map[word] = data['data']

    result = []
    for word in word_list:
        item = {}
        if word_map[word]['data']:
            definition = word_map[word]['data']['definitionData']['definitions'][0]['definition']
            pos = word_map[word]['data']['definitionData']['definitions'][0]['pos']
        else:
            definition = ''
            pos = ''

        result.append({
            'word': word,
            'definition': definition,
            'pos': pos
        })
    df = pd.DataFrame(result, columns=['word', 'pos', 'definition'])
    df.to_excel(f'{page}X_1.xls', index=False)
    # print(word + '...' + definition + '...' + pos)
