# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 11:40:17 2019

@author: MRZEZNIC
"""

import requests

link = "http://indy/abcde1245"
file_name = "download.data"
with open(file_name, "wb") as f:
        print "Downloading %s" % file_name
        response = requests.get(link, stream=True)
        total_length = response.headers.get('content-length')

        if total_length is None: # no content length header
            f.write(response.content)
        else:
            dl = 0
            total_length = int(total_length)
            for data in response.iter_content(chunk_size=4096):
                dl += len(data)
                f.write(data)
                done = int(50 * dl / total_length)
                sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )
                sys.stdout.flush()

from clint.textui import progress

r = requests.get(url, stream=True)
path = '/some/path/for/file.txt'
with open(path, 'wb') as f:
    total_length = int(r.headers.get('content-length'))
    for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1):
        if chunk:
            f.write(chunk)
            f.flush()

from tqdm import tqdm
for i in tqdm (range(int(9e6))):
    pass
