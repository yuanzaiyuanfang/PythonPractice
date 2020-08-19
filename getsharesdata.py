import requests
from requests import adapters
import math
import json
import time
from datetime import datetime
import csv
import os

first_kcb = True
first_a = True
date = ""
totalShares = 4469
dir = "d://pyData/xueqiu/"

headers = {"Cookie": "xq_a_token=69a6c81b73f854a856169c9aab6cd45348ae1299",
           "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0"}


def get_shares_list(page):
    params = {"category": 'CN', "exchange": 'sh_sz', "order_by": 'symbol', "order": 'asc', "page": page,
              "size": 50, "only_count": 0, "_": int(time.time() * 1000)}
    return requests.get(url="https://xueqiu.com/service/screener/screen", params=params, headers=headers).text


def get_shares_detail(symbol):
    params = {"symbol": symbol, "extend": 'detail'}
    # 设置重连次数
    requests.adapters.DEFAULT_RETRIES = 10
    s = requests.session()
    # 设置连接活跃状态为False
    s.keep_alive = False
    return requests.get("https://stock.xueqiu.com/v5/stock/quote.json", params=params, headers=headers).text


def save_shares(bean: dict):
    if bean["symbol"].startswith("SH688"):
        # 科创板格式不一样单独保存一个
        with open('%s%skcb.csv' % (dir, date), 'a', newline='') as file:
            global first_kcb
            b = save(bean, file, first_kcb)
            first_kcb = b
    else:
        with open('%s%sa.csv' % (dir, date), 'a', newline='') as file:
            global first_a
            b2 = save(bean, file, first_a)
            first_a = b2


def save(bean, file, first):
    writer = csv.writer(file)
    if first:
        writer.writerow(bean)

    values = bean.values()
    for value in values:
        if isinstance(value, int) | isinstance(value, float):
            value = str(value) + " \t"
    writer.writerow(values)
    return False


if __name__ == '__main__':

    if not os.path.exists(dir):
        os.makedirs(name=dir, exist_ok=True)

    print("开始")
    start = int(time.time())
    date = datetime.now().strftime('%Y%m%d')

    for page in range(1, math.ceil(totalShares / 50) + 1):
        # if page == 20:
        #     break
        # 获取列表
        shares_list = json.loads(get_shares_list(page))["data"]["list"]
        # 遍历
        for shares in shares_list:
            # 去掉没用的
            symbol: str = shares["symbol"]
            if symbol.startswith("SH171"):
                continue

            # 获取详情
            sharesDetail: dict = json.loads(get_shares_detail(symbol))

            # 写入
            data = sharesDetail.get("data")
            if data is not None:
                quote_ = data["quote"]
                print("%s-%s" % (quote_["symbol"], quote_["name"]))
                save_shares(quote_)

            time.sleep(0.4)

    print("耗时%d秒" % (int(time.time()) - start))
