import csv
import plotly.express as exp
from pathlib import Path

filename = 'MODIS_C6_1_Global_24h.csv'

with open(filename) as f:

    reader = csv.reader(f)
    header_row = next(reader)

    lats, lons, brights = [], [], []
    for row in reader:
        lat = float(row[0])
        lon = float(row[1])
        bright = float(row[2])
        lats.append(lat)
        lons.append(lon)
        brights.append(bright)

title = 'World Wide Wildfires'
fig = exp.scatter_geo(
    lat=lats, 
    lon=lons, 
    size=brights, 
    title=title,
    color=brights,
    color_continuous_scale='sunset',
    labels={'color':'Brightness'},
    projection='natural earth'
    )

fig.show()