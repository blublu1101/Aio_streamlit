import requests, re

# area = ['gulou', 'jianye', 'qinhuai', 'xuanwu', 'yuhuatai', 'qixia', 'jiangning', 'pukou', 'liuhe', 'lishui', 'gaochun']
area = ['gulou']

for _area in area:
    url = f"https://nj.ke.com/chengjiao/{_area}/pg/"

    payload = {}
    headers = {
        'Cookie': 'lianjia_uuid=e793dd8b-a07b-42f2-8003-8d358c5b9db9; expires=Thu, 22-Jun-34 08:40:01 GMT; Max-Age=315360000; domain=.lianjia.com; path=/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    ys = ''.join(re.findall('{"totalPage":(.*?),', response.text))
    print(response.text)

    # for pn in range(1, int(ys) + 1):
    #     print(list_aa, pn)
    #     url = f"https://tj.ke.com/xiaoqu/{list_aa}/pg{pn}/"
    #
    #     payload = {}
    #     headers = {
    #         'Cookie': 'SECKEY_ABVK=2UuSpBiJF0EyUOXqMP6jYAWjr2uAkgtcEGYgLNwlblk%3D; BMAP_SECKEY=2UuSpBiJF0EyUOXqMP6jYIs_cq2vBg3Ln2KK1l1LJ0hXiE7FXLHjebyeP7vqiyCJxAPkYdXEHrKE0irT6iAa9BA4CngYl7xRpaZmHBsHU1H0YYrsFlK1me40TYvJ7f3JWpCwFTzLohaeFjHEaaSXIvLAcLMteKWmC6-w8sl-G9V8K_WJJm7pw17jDRvW9dU-; lianjia_uuid=8e89dd5d-57a3-4d73-b3e7-d04b7d488879; crosSdkDT2019DeviceId=ewr3ua--ics2qa-7a3g4wjlzyqwm1i-56cwoexqk; ftkrc_=8d03c157-9b42-4154-927c-c61c3303991a; lfrc_=4491d6b1-f560-4bbb-ab39-1f315ee03724; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218851e6b1c17a2-02abc8a1cd818a-26031a51-1327104-18851e6b1c2f76%22%2C%22%24device_id%22%3A%2218851e6b1c17a2-02abc8a1cd818a-26031a51-1327104-18851e6b1c2f76%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E4%BB%98%E8%B4%B9%E5%B9%BF%E5%91%8A%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Fother.php%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E8%B4%9D%E5%A3%B3%22%2C%22%24latest_utm_source%22%3A%22baidu%22%2C%22%24latest_utm_medium%22%3A%22pinzhuan%22%2C%22%24latest_utm_campaign%22%3A%22wytianjin%22%2C%22%24latest_utm_content%22%3A%22biaotimiaoshu%22%2C%22%24latest_utm_term%22%3A%22biaoti%22%7D%7D; select_city=120000; lianjia_ssid=e681e664-1263-4242-a944-4446cdc55109; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1699234449,1699255368,1699511014,1700620561; login_ucid=2000000015717757; lianjia_token=2.0014b8d04c6dd268dd0515f97d65006744; lianjia_token_secure=2.0014b8d04c6dd268dd0515f97d65006744; security_ticket=l5hrILircjmVbnYhyhtpiWAcy7xy4o0K7vaClvPV3dl3G2KOwwk97kL75ASd7AfqqBExPdKIqZravB4l/YSnco8h0QfTmsKaMxNDKsLlwq8Ib7ZGCMfCjFrBGUq5EETVrj1WHcZxlVg8S5Z4pP9MVRaQaPisLmc/5jw3yr2Julk=; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1700620742; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiYzk0MGNlNzk5N2NjNjIzYjlkZjdiNDUxOWM0MGNlYmZhNDdmNWIzZjI4OGNiZWM5NjQ2ODNkYjljMTliMjI5MDNiYjQyZjllNTU0NDI2NjgyNTUxMzM4NWFhNThjYzIyYzk4NWVlNDVjMDk0MTYwYmVhYjlkMDAwMjE2YmU2NTcwMjAzNWRjZGM5YzY1M2IzMzU1ZTM2YjQ0OWU0Mzk3ZjNjM2M0NTg5NDM4YjNmMzBmZmYyYWExNWVkNzlhNDVmMGNjODI0YTg0MTg4YjM1Mjg5MzA2NGZhZjJjMDY2NGY1MzcxZmIyMDI2YzU5OGFmMThmMDhhODY0NmFiMzUwZFwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCIwODk1OGI0OVwifSIsInIiOiJodHRwczovL3RqLmtlLmNvbS94aWFvcXUvMTIyMDA0MTEzMjUzMjU0Mi8/ZmJfZXhwb19pZD03Nzk2NTcxMDE2NjgxNjc2ODAiLCJvcyI6IndlYiIsInYiOiIwLjEifQ==',
    #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    #     }
    #
    #     response = requests.request("GET", url, headers=headers, data=payload)
    #     ys = ''.join(re.findall('{"totalPage":(.*?),', response.text))
    #     r = html.etree.HTML(response.text)
    #     bk_list1 = r.xpath('//div[@class="info"]')
    #     # bk_list1 = r.xpath('//a[@class="maidian-detail"]/text()')
    #     # bk_list2 = r.xpath('//a[@class="district"]/text()')
    #     for bk in bk_list1:
    #         xq = ' '.join(bk.xpath('.//a[@class="district"]/text()') + bk.xpath('.//a[@class="maidian-detail"]/text()'))
    #         with open('data.txt', 'a') as f:
    #             f.write(xq + '\n')
