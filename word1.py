import time

import pandas as pd
import requests
import json

word_set = []
with open('./data/word.txt', 'r') as f1:
    list1 = f1.readlines()
    for i in list1:
        word_set.append(i.strip().lower())

count = 0
word_map = {}
for word in word_set:
    item = {}

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }
    url = f'https://tuna.thesaurus.com/pageData/{word}'

    res = requests.get(url=url, headers=headers, verify=False)
    a = res.status_code
    b = res.text
    item['word'] = word
    try:
        data = json.loads(b)
    except Exception as e:
        print('error...%s...' % word)
        data = ''
    # item['data'] = data
    # with open(f'{page}X.json', 'a') as f2:
    #     f2.write(json.dumps(item) + '\n')
    word_map[word] = data
    time.sleep(0.5)
    count += 1

result = []
for word in word_set:
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
df.to_excel('./result/word.xls', index=False)
