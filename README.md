# Return format?
In the server.py, in the hello_world function, how should the files be returned so that they can be parsed by PowerBI reference map module?

I tried sending it as zip, raw json payload, json file etc but nothing worked. 
However just publishing the files to github and downloading them from the files "Raw" mode, it worked fine. It uses "plain/text" as headers and not "application/json".

Another possibility is that the features in this example are invalid somehow.
In a later experiment I created the files using python geopandas, and those reference layers were actually working
However I ran into problems with the rotation of the polygons, so I had to use some python library to 
rotate the polygons correctly. 