import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Pull the file
filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

# Pull appropriate data from file
all_eq_dicts = all_eq_data['features']
title = all_eq_data['metadata']['title']

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])

# Map the earthquakes
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [1.7**mag if mag > 0 else mag*0 for mag in mags],
        'color': mags,
        'colorscale': 'viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
        'line': {'color': 'rgba(255, 255, 255, 0.1)'}
    },
}]

my_layout = Layout(title=title)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
