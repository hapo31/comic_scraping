# -*- coding: utf-8 -*-

import requests
import os

class GetFiles:
    """
    GetFiles module
    与えられたURL先のファイルを連番で保存する
    """
    def __init__(self, url_list, save_dir):
        self.url_list = url_list
        self.save_dir = save_dir

    def start(self):
        for i, url in enumerate(self.url_list):
            print(url)
            res = requests.get(url)
            if res.status_code == 200:
                ext = url.split(".")[-1]
                filename = "%02d.%s" % (i, ext)
                try:
                    os.mkdir("%s" % self.save_dir)
                except:
                    pass
                with open("./%s" % ("/".join([self.save_dir, filename])), "wb") as file:
                    file.write(res.content)
            else:
                print("file not found:%s" % url)

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