import os
from arcgis.gis import GIS
from datetime import date

# INSERT USER ArcGIS ONLINE CREDENTIALS WITH ADMIN PRIVLEDGES
user = "USERNAME"
password = "PASSWORD"

# SPECIFY OUTPUT LOCATION
output_location = "C:\\OUTPUT\\LOCATION"


# Creating a new folder in output location
today = date.today().strftime("%Y%m%d")

new_dir = today + "_MebaneAGOL_Backup"
path = os.path.join(output_location, new_dir)
os.mkdir(path)

# Connecting to AGOL instance and downloading data
mebane = GIS("https://mebanenc.maps.arcgis.com/home/index.html", user, password)

feature_layers = mebane.content.search(query="owner:*",item_type="Feature Layer", max_items=10000)

for layer in feature_layers:
    try:
        service_title = layer.title
        date = "_" + today
        fgdb_title = service_title+date
        result = layer.export(fgdb_title, "File Geodatabase")
        result.download(path)
        result.delete()
    except:
        print("An error occurred downloading" + " " + service_title)