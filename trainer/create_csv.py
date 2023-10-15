import os
import pandas as pd

checkum = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")
gcs = os.environ.get("GCS_BASE")

def get_images(dir):
    file_list = []
    for x in os.listdir(dir):
        if x.endswith('.jpg'):
            file_list.append(x)
    return file_list

package_images = []
for x in get_images(os.path.join(checkum, 'package')):
    package_images.append(os.path.join(gcs, 'data', 'package', x))

nopackage_images = []
for x in get_images(os.path.join(checkum, 'no_package')):
    nopackage_images.append(os.path.join(gcs, 'data', 'no_package', x))

package_list = []
for x in package_images:
    package_list.append([x, 'package'])

nopackage_list = []
for x in nopackage_images:
    nopackage_list.append([x, 'no_package'])

df = pd.DataFrame(package_list + nopackage_list)
df.to_csv('training_data.csv', index=False, header=None)