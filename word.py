import time

import requests
import json

for page in range(2, 4):
    word_set = set()
    with open(f'{page}X.txt', 'r') as f1:
        list1 = f1.readlines()
        for i in list1:
            word_set.add(i.strip().lower())

    count = 0
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
        item['data'] = data
        with open(f'{page}X.json', 'a') as f2:
            f2.write(json.dumps(item) + '\n')
        time.sleep(0.5)
        count += 1

        print('count:%s..%s' % (count, word))
