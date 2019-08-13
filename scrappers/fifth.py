import random

import requests
from lxml.html import fromstring
from lxml import etree
from multiprocessing.pool import ThreadPool
import json


userAgent = [
            (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'),
    # chrome
    ('Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'),
    # chrome
    (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'),
    # chrome
    (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'),
    # chrome
    (
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'),
    # chrome
    ('Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'),
    # chrome
    (
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'),
    # chrome
    ('Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36'),  # chrome
    (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'),
    # chrome
    (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'),
    # chrome
    (
        'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'),
    # chrome
    ('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.83 Safari/537.1'),
    # chrome
    (
        'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'),
    # chrome
    (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'),
    # chrome
    (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'),
    # chrome
    (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'),
    # chrome
    (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'),
    # chrome
    (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'),
    # chrome
    (
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'),
    # chrome
    (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'),
    # chrome
    (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'),
    # chrome
    (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'),
    # chrome
    (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'),
    # chrome
    (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'),
    # chrome
    (
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'),
    # chrome
    (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'),
    # chrome
    ('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36'),
    # chrome
    (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'),
    # chrome
    (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'),
    # chrome
    (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'),
    # chrome
    ('Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'),
    # chrome
    ('Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'),
    # chrome
    (
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'),
    # chrome
    (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'),
    # chrome
    (
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'),
    # chrome
    (
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'),
    # chrome
    (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'),
    # chrome
    ('Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'),  # chrome
    ('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'),
    # chrome
    (
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'),
    # chrome
    (
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'),
    # chrome
    (
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'),
    # chrome
    (
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'),
    # chrome
    (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'),
    # chrome
    ('Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'),
    # chrome
    (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'),
        ]
proxies_arr = ['bbercaw10:gPBizQfI@207.188.174.13:60099',
         'bbercaw10:gPBizQfI@207.188.174.16:60099',
         'bbercaw10:gPBizQfI@207.188.174.24:60099',
         'bbercaw10:gPBizQfI@207.188.174.34:60099',
         'bbercaw10:gPBizQfI@207.188.174.73:60099',
         'bbercaw10:gPBizQfI@207.188.174.76:60099',
         'bbercaw10:gPBizQfI@207.188.174.81:60099',
         'bbercaw10:gPBizQfI@207.188.174.82:60099',
         'bbercaw10:gPBizQfI@207.188.174.97:60099',
         'bbercaw10:gPBizQfI@207.188.174.102:60099',
         'bbercaw10:gPBizQfI@207.188.174.103:60099',
         'bbercaw10:gPBizQfI@207.188.174.134:60099',
         'bbercaw10:gPBizQfI@207.188.174.142:60099',
         'bbercaw10:gPBizQfI@207.188.174.143:60099',
         'bbercaw10:gPBizQfI@207.188.174.149:60099',
         'bbercaw10:gPBizQfI@207.188.174.177:60099',
         'bbercaw10:gPBizQfI@207.188.174.185:60099',
         'bbercaw10:gPBizQfI@207.188.174.193:60099',
         'bbercaw10:gPBizQfI@207.188.174.202:60099',
         'bbercaw10:gPBizQfI@207.188.174.209:60099',
         'bbercaw10:gPBizQfI@207.188.174.220:60099',
         'bbercaw10:gPBizQfI@207.188.174.223:60099',
         'bbercaw10:gPBizQfI@207.188.174.247:60099',
         'bbercaw10:gPBizQfI@207.188.174.250:60099']


def process_details(content):
    content = etree.tostring(content, with_tail=False, method='html')
    content = content.decode('utf-8')
    content = content.replace('  ', '').replace('\n', '').replace('\r', '').replace('\t', '')
    return content

import requests


def get_case(case_info):
    if 'events' in case_info:
        return case_info
    header = {
        'User-Agent': userAgent[random.randint(0, 44)]
    }
    proxy_item = proxies_arr[random.randint(0, 23)]

    proxies = {
        'http': 'http://{}'.format(proxy_item),
        'https': 'http://{}'.format(proxy_item),
    }

    print('[-]================================GetCase')
    url = "http://www.search.txcourts.gov/Case.aspx?cn=" + case_info['Case Number'] + "&coa=coa04"
    res = requests.get(url, headers=header, proxies=proxies)
    print(res.status_code)
    if res.status_code != 200:
        return case_info


    try:
        t = fromstring(res.text)
        main_content = t.xpath('//div[@id="main-content"]/div[@class="row-fluid"]')

        case_info['events'] = process_details(main_content[2])
        case_info['trial'] = process_details(main_content[len(main_content) - 1])
        case_info['parties'] = process_details(main_content[4])
        case_info['calendars'] = process_details(main_content[3])
        case_info['briefs'] = process_details(main_content[1])
    except:
        return case_info
    return case_info


def update_case(case_info):
    header = {
        'User-Agent': userAgent[random.randint(0, 44)]
    }
    proxy_item = proxies_arr[random.randint(0, 23)]
    proxies = {
        'http': 'http://{}'.format(proxy_item),
        'https': 'http://{}'.format(proxy_item),
    }

    print('[-]================================UpdateCase')
    url = "http://www.search.txcourts.gov/Case.aspx?cn=" + case_info.case_number + "&coa=coa04"
    res = requests.get(url, headers=header, proxies=proxies)
    if res.status_code != 200:
        return res.status_code


    try:
        t = fromstring(res.text)
        main_content = t.xpath('//div[@id="main-content"]/div[@class="row-fluid"]')
        case_events = process_details(main_content[2])
        if case_info.case_events == case_events:
            return 'same'
        case_info.case_events = process_details(main_content[2])
        case_info.trial_court_information = process_details(main_content[len(main_content) - 1])
        case_info.parties = process_details(main_content[4])
        case_info.calendars = process_details(main_content[3])
        case_info.appellate_briefs = process_details(main_content[1])
        case_info.save()
        return 'updated'
    except:
        return 'error while updating'


def get_court(court_info):
    get_court.progress += 1

    if 'events' in court_info:
        return

    print(get_court.progress)
    header = {
        'User-Agent': userAgent[random.randint(0, 44)]
    }
    proxy_item = proxies_arr[random.randint(0, 23)]
    proxies = {
        'http': 'http://{}'.format(proxy_item),
        'https': 'http://{}'.format(proxy_item),
    }
    print('[-]================================GetCourt')

    url = "http://www.search.txcourts.gov/Case.aspx?cn=" + court_info['Case Number'] + "&coa=coa04"
    res = requests.get(url, headers=header, proxies=proxies)
    if res.status_code != 200:
        print('error occurred at', get_court.progress, 'with', res.status_code)
        return


    try:
        t = fromstring(res.text)
        main_content = t.xpath('//div[@id="main-content"]/div[@class="row-fluid"]')

        court_info['events'] = process_details(main_content[2])
        court_info['trial'] = process_details(main_content[len(main_content) - 1])
        court_info['parties'] = process_details(main_content[4])
        court_info['calendars'] = process_details(main_content[3])
        court_info['briefs'] = process_details(main_content[1])
        print(len(main_content), url, court_info['trial'])
    except Exception as e:
        print('error occurred at', get_court.progress, 'with', e)


if __name__ == '__main__':
    court_file = open('data/div1.json')
    court_infos = []
    for court in court_file.readlines():
        court_infos.append(json.loads(court))
    court_file.close()

    get_court.progress = 0

    pool = ThreadPool(32)
    for id, _ in enumerate(pool.imap_unordered(get_court, court_infos)):
        if get_court.progress % 200 == 0:
            print(len(court_infos))
            court_file = open('data/div1.json', 'w')
            for case in court_infos:
                court_file.write(json.dumps(case) + '\n')
            court_file.close()

    court_file = open('data/div1.json', 'w')
    for case in court_infos:
        court_file.write(json.dumps(case) + '\n')
    court_file.close()
