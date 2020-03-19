import requests
API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def get_response_from_server():
    text = input()
    from_lang = input()
    to_lang = input()
    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}-{}'.format(from_lang, to_lang),  # задать язык
    }
    response = requests.get(URL, params=params)
    return response.status_code

def get_translate_result():
    text = input()
    from_lang = input()
    to_lang = input()
    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}-{}'.format(from_lang, to_lang),  # задать язык
    }
    response = requests.get(URL, params=params)
    res_json = response.json()
    return res_json['text'][0]






