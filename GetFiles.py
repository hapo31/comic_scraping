# -*- coding: utf-8 -*-

import os
import time
import requests

class GetFiles:
    """
    GetFiles module
    与えられたURL先のファイルを連番で保存する
    """
    def __init__(self, url_list, save_dir):
        self._url_list = url_list
        self._save_dir = save_dir

    def start(self):
        for i, url in enumerate(self._url_list):
            print(url)
            res = requests.get(url)
            if res.status_code == 200:
                ext = url.split(".")[-1] # 拡張子決め打ち取得
                filename = "%02d.%s" % (i, ext) # 連番ファイル名生成
                try:
                    os.mkdir("%s" % self._save_dir)
                except:
                    pass
                with open("./%s" % ("/".join([self._save_dir, filename])), "wb") as file:
                    file.write(res.content)
            else:
                print("file not found:%s" % url)
            time.sleep(0.1) # サーバーに負荷を掛けないように手加減する
    
    @property
    def url_list(self):
        return self._url_list

    @url_list.getter
    def url_list(self):
        return self._url_list

def main():
    import sys
    urls = []
    for arg in sys.argv[2:]:
        urls.append(arg)

    if len(urls) != 0:
        get_image = GetFiles(sys.argv[1], urls)
        get_image.start()

if __name__ == '__main__':
    main()