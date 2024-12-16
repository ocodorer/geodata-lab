from flask import Flask, send_from_directory, request, Response
import json
import os 
import shutil

import zipfile 

app = Flask(__name__, static_folder='public',
                      static_url_path='/frontend_public')


def send_as_zip(base):
    if os.path.isdir("tmp"):
        shutil.rmtree("tmp")
    os.mkdir("tmp")
    with open(os.path.join("tmp", "reference_map.geojson"), "w") as fo:
        json.dump(base, fo)
    shutil.make_archive('reference_map', 'zip', 'tmp')

    return send_from_directory('.', "reference_map.zip", as_attachment=True, mimetype="application/zip")

def send_as_jsonfile(base):
    with open(os.path.join("reference_map.geojson"), "w") as fo:
        json.dump(base, fo)
    # return send_from_directory('.', "reference_map.geojson")
    response = send_from_directory('.', "reference_map.geojson", mimetype="text/plain", headers={"Content-Type": "text/plain"})
    # response.headers["Content-Disposition"] = 'inline;filename="reference_map.geojson"'
    #response.headers.remove("Content-Disposition")
    #response.headers.add("Content-Disposition", )
    # response.mimetype = 'text/plain'
    #response.content_type = "text/html; charset=utf-8"
    #response = Response(response=base, mimetype="plain/text")
    
    return response

@app.route('/foobar')
def hello_world():

    feature_keys = request.args.get("feature_keys")
    # Use feature keys to select attributes to put in the reference layer
    print(feature_keys)
    
    # geojson template file
    with open("reference_map.geojson.template") as fo:
        base = json.load(fo)

    # Load some features
    with open("feature.json") as fo:
        f1 = json.load(fo)
    with open("feature2.json") as fo:
        f2 = json.load(fo)

    # Write them
    with open("public/taipei.json") as fo:
        base2 = json.load(fo)
    base["features"].append(f1)
    
    
    return send_as_jsonfile(base2)
    # return send_from_directory('.', "reference_map.geojson", mimetype="application/geo+json")
    #return send_from_directory('.', "reference_map.geojson", as_attachment=True, mimetype="application/geo+json")

# http://127.0.0.1:5000/reference_map.geojson