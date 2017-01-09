# -*- coding:utf-8 -*-

# やわすぴurl構成メモ
# http://yawaspi.com/[コミック固有ID]/comic/[話数000]_[ページ000].html

import sys
import os
import time
import requests

from GetFiles import GetFiles

def main():

    content_id = ""
    max_ep = 0
    if len(sys.argv) < 3:
        print("input content_id>")
        content_id = str(input())
        print("input max epsode number>")
        max_ep = int(input())
    else:
        content_id = str(sys.argv[1])
        max_ep = int(sys.argv[2])

    # IDのディレクトリを生成する
    try:
        os.mkdir(content_id)
    except:
        pass
    
    for epnum in range(1, max_ep + 1):
        print("epnum", epnum)
        # そのコミックのn話目のURL
        epsode_url = "http://yawaspi.com/%s/comic/%03d_001.html" % (content_id, epnum)
        # 指定した話数のエピソードが存在する
        if requests.head(epsode_url).status_code == 200:
            # 話数のディレクトリを生成する
            try:
                os.mkdir("%s/%03d" % (content_id, epnum))
            except:
                pass
            # その話のページのURLをnot foundが返ってくるまで取得する
            i = 1
            urls = []
            while True:
                url = "http://yawaspi.com/comic/%s/pc/%03d/%03d_001_%02d.jpg" % (content_id, epnum, epnum, i)
                print(url)
                if requests.head(url).status_code == 200:
                    urls.append(url)
                else:
                    break
                i += 1
                time.sleep(0.1)

            if len(urls) > 0:
                # ファイルを取得
                GetFiles(urls, "%s/%03d" % (content_id, epnum)).start()

if __name__ == '__main__':
    main()