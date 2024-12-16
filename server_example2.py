from flask import Flask, send_from_directory, request, Response


app = Flask(__name__, static_folder='public',
                      static_url_path='/frontend_public')

@app.route('/foobar')
def hello_world():

    # Use feature keys to select attributes to put in the reference layer
    feature_keys = request.args.get("feature_keys")
    print(feature_keys)


    return send_from_directory('customer-a', "reference_map.geojson")

# http://127.0.0.1:5000/foobar/reference_map.geojson