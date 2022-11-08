from urllib.request import urlopen
import json
import pandas as pd
import plotly.express as px

def make_map(values): 
    with urlopen("https://raw.githubusercontent.com/Fair-Share-MA/cdn/master/ma_boundry.geojson") as response:
        cities = json.load(response)

    df = pd.DataFrame.from_dict(values)

    fig = px.choropleth(df, geojson=cities, locations='name', color='votes',
                            color_continuous_scale="Viridis",
                            range_color=(0, 100),
                            scope="MA",
                            )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig.to_html()