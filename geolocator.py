import pandas as pd
import plotly.express as px
import streamlit as st

class GeoLocator:
    def get_geo(self):
        # Predefined approximate coordinates for each city
        data = [
            {"city": "Seattle",         "state": "Washington",    "latitude": 47.6062, "longitude": -122.3321},
            {"city": "Tampa",           "state": "Florida",       "latitude": 27.9506, "longitude": -82.4572},
            {"city": "Boston",          "state": "Massachusetts", "latitude": 42.3601, "longitude": -71.0589},
            {"city": "New York City",   "state": "New York",      "latitude": 40.7128, "longitude": -74.0060},
            {"city": "Louisville",      "state": "Kentucky",      "latitude": 38.2527, "longitude": -85.7585},
            {"city": "Pittsburgh",      "state": "Pennsylvania",  "latitude": 40.4406, "longitude": -79.9959},
            {"city": "Cleveland",       "state": "Ohio",          "latitude": 41.4993, "longitude": -81.6944},
            {"city": "Leeds",           "state": "Alabama",       "latitude": 33.5482, "longitude": -86.5444},
            {"city": "Fort Lauderdale", "state": "Florida",       "latitude": 26.1224, "longitude": -80.1373},
            {"city": "Los Angeles",     "state": "California",    "latitude": 34.0522, "longitude": -118.2437},
            {"city": "Asbury Park",     "state": "New Jersey",    "latitude": 40.2204, "longitude": -74.0121},
            {"city": "Chattanooga",     "state": "Tennessee",     "latitude": 35.0456, "longitude": -85.3097},
            # Duplicate Los Angeles entry (if desired)
            {"city": "Los Angeles",     "state": "California",    "latitude": 34.0522, "longitude": -118.2437},
            {"city": "Miami",           "state": "Florida",       "latitude": 25.7617, "longitude": -80.1918},
        ]

        df = pd.DataFrame(data)

        # Create a Plotly map with a clean, modern style
        fig = px.scatter_geo(
            df,
            lat="latitude",
            lon="longitude",
            hover_name="city",
            hover_data=["state"],
            scope="usa",
            projection="albers usa",
        )

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
        
        # Render the Plotly figure within Streamlit's page
        st.plotly_chart(fig, use_container_width=True)
