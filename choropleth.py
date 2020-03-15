import json
import pandas as pd
import folium
import requests

json_url = "https://raw.githubusercontent.com/qchenevier/municipales_2020/master/new_geo.json"

circonscriptions = requests.get(json_url).json()

#%%
circonscriptions["features"][0]["properties"]

#%%
property_name_for_id = "nom"

#%%
ids = [c["properties"][property_name_for_id] for c in circonscriptions["features"]]

#%%
df = (
    pd.DataFrame({"id": ids, "value": range(len(ids))})
)

#%%
m = folium.Map(location=[43.6047, 1.4442], zoom_start=5)

folium.Choropleth(
    geo_data=circonscriptions,
    data=df,
    columns=["id", "value"],
    key_on=f"properties.{property_name_for_id}",
    legend_name="the legend",
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
).add_to(m)

folium.LayerControl().add_to(m)

m.save("plot.html")
