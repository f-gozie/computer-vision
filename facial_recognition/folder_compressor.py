#!/usr/bin/env python
import os
import zipfile

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

if __name__ == '__main__':
    zipf = zipfile.ZipFile('dataset.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir('dataset', zipf)
    zipf.close()