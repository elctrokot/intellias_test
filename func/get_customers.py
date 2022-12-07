import requests
import json

host = 'https://reqres.in'
api_path = '/api/users'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' \
             ' (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
parameter = 'page'


def get_customers(*args):
    resulting_customer_list = []
    first_name_list = []
    last_name_list = []

    if len(args) != 2:
        print("Function takes only 2 parameters")
        return []

    if not all(isinstance(n, int) for n in args):
        print("Function takes only integers")
        return []

    if min(args) < 1 or max(args) > 12:
        print("Parameters should be from 1 to 12")
        return []

    start_finish_params = sorted(args)
    if max(start_finish_params) > 6 and min(start_finish_params) > 6:
        pages = ['2']
    elif max(start_finish_params) <= 6 and min(start_finish_params) <= 6:
        pages = ['1']
    else:
        pages = ['1', '2']

    headers = {'User-Agent': user_agent}

    for page in pages:
        response = requests.get(host + api_path + '?' + parameter + '=' + page, headers=headers)

        if response.status_code != 200:
            return []

        for customers in json.loads(response.text)['data']:
            if min(start_finish_params) <= customers['id'] <= max(start_finish_params):
                first_name_list.append(customers['first_name'])
                last_name_list.append(customers['last_name'])

    resulting_customer_list = [fn + ' ' + ln for fn, ln in sorted(zip(first_name_list, last_name_list))]

    return resulting_customer_list
