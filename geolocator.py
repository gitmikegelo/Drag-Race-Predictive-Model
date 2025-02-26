import pandas as pd
import plotly.express as px
import streamlit as st

class GeoLocator:
    def get_geo(self):
        # Predefined data: Queen, City, State, and approximate lat/lon
        data = [
            {"queen": "Arrietty",         "city": "Seattle",         "state": "Washington",    "latitude": 47.6062, "longitude": -122.3321},
            {"queen": "Jewels Sparkles",  "city": "Tampa",           "state": "Florida",       "latitude": 27.9506, "longitude": -82.4572},
            {"queen": "Kori King",        "city": "Boston",          "state": "Massachusetts", "latitude": 42.3601, "longitude": -71.0589},
            {"queen": "Lana Ja'Rae",      "city": "New York City",   "state": "New York",      "latitude": 40.7128, "longitude": -74.0060},
            {"queen": "Lexi Love",        "city": "Louisville",      "state": "Kentucky",      "latitude": 38.2527, "longitude": -85.7585},
            {"queen": "Lydia B Kollins[b]","city": "Pittsburgh",      "state": "Pennsylvania",  "latitude": 40.4406, "longitude": -79.9959},
            {"queen": "Onya Nurve",       "city": "Cleveland",       "state": "Ohio",          "latitude": 41.4993, "longitude": -81.6944},
            {"queen": "Sam Star",         "city": "Leeds",           "state": "Alabama",       "latitude": 33.5482, "longitude": -86.5444},
            {"queen": "Suzie Toot",       "city": "Fort Lauderdale", "state": "Florida",       "latitude": 26.1224, "longitude": -80.1373},
            {"queen": "Acacia Forgot",    "city": "Los Angeles",     "state": "California",    "latitude": 34.0522, "longitude": -118.2437},
            {"queen": "Crystal Envy",     "city": "Asbury Park",     "state": "New Jersey",    "latitude": 40.2204, "longitude": -74.0121},
            {"queen": "Hormona Lisa",     "city": "Chattanooga",     "state": "Tennessee",     "latitude": 35.0456, "longitude": -85.3097},
            {"queen": "Joella",           "city": "Los Angeles",     "state": "California",    "latitude": 34.0522, "longitude": -118.2437},
            {"queen": "Lucky Starzzz",    "city": "Miami",           "state": "Florida",       "latitude": 25.7617, "longitude": -80.1918},
        ]

        df = pd.DataFrame(data)

        # Create the Plotly map
        fig = px.scatter_geo(
            df,
            lat="latitude",
            lon="longitude",
            hover_name="queen",           # Hover shows the queen's name
            hover_data=["city", "state"], # Also show city/state on hover
            scope="usa",
            projection="albers usa",
        )

        # Style the map layout
        fig.update_layout(
            geo=dict(
                bgcolor='rgba(0,0,0,0)',
                landcolor='white',
                showlakes=True,
                lakecolor='LightBlue',
                subunitcolor='lightgrey'
            ),
            template="plotly_white",
            margin={"r":0,"t":0,"l":0,"b":0},
        )

        # Display the figure inline in Streamlit
        st.plotly_chart(fig, use_container_width=True)
