# reference：https://blog.csdn.net/m0_37589837/article/details/84332864
# python_version = 3.5
import re
import requests
import time
import sys
import os

pdfs_URL = []
base_URL = "https://www.aclweb.org/anthology/P19-"
for i in range(1000, 1661):
    URL = base_URL + str(i) + '.pdf'
    pdfs_URL.append(URL)
print(pdfs_URL)

for i in pdfs_URL:
    time.sleep(2)
    r = requests.get(i)
    path = re.sub("https://www.aclweb.org/anthology/", "C:/Users/viruser.v-desktop/Desktop/download_file/", i)
    path = re.sub('\n', '', path)
    with open(path, "wb") as f:
        f.write(r.content)
