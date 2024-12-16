import os
import json


with open("geodata-lab/customer-c/reference_map.geojson", "r") as fo:
    data = json.load(fo)

import random

geoids = []
for feature in data["features"]:
    gid = feature["properties"]["GEO_ID"]
    geoids.append({
        "GEO_ID": gid, "attribute1": random.randint(0, 30000), "attribute2": random.randint(0, 2000)
    })

# with open("geodata-lab/customer-a/reference_map.geojson", "r") as fo:
#     data = json.load(fo)
# for feature in data["features"]:
#     gid = feature["properties"]["GEO_ID"] + "GeoKeyNotRealLocation"
#     geoids.append({
#         "GEO_ID": gid, "attribute1": random.randint(0, 30000), "attribute2": random.randint(0, 2000)
#     })

with open("datafile.json", "w") as fo:
    json.dump(geoids, fo)