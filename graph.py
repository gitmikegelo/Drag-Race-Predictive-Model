import streamlit as st
import plotly.graph_objects as go
import pandas as pd


class Graph():
    def get_graph(self):
        # Sample data (replace with your actual data if needed)
        data = {
            'Person': ['Person 1', 'Person 2', 'Person 3', 'Person 4', 'Person 5', 'Person 6', 'Person 7', 'Person 8', 'Person 9', 'Person 10', 'Person 11'],
            'Fashion': ['High', 'High', 'High', 'Medium', 'Medium', 'Medium', 'High', 'High', 'Medium', 'Medium', 'High'],
            'Performance': ['Medium', 'Medium', 'High', 'High', 'Medium', 'High', 'Medium', 'Medium', 'High', 'High', 'Medium'],
            'Comedy': ['Low', 'Low', 'Medium', 'Medium', 'Medium', 'High', 'High', 'High', 'High', 'Medium', 'Low'],
            'Lip Sync': ['Medium', 'Medium', 'High', 'High', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium', 'High', 'High'],
            'Charisma': ['Medium', 'High', 'High', 'High', 'High', 'High', 'High', 'High', 'High', 'High', 'Medium']
        }

        # Convert categorical ratings to numerical values
        def convert_rating(rating):
            if rating == 'High':
                return 4
            elif rating == 'Medium':
                return 2
            else:  # Low
                return 1

        # Create a DataFrame
        df = pd.DataFrame(data)

        # Categories for the radar chart
        categories = ['Fashion', 'Performance', 'Comedy', 'Lip Sync', 'Charisma']

        # Convert ratings to numerical values and sum across all persons
        summed_stats = []
        for category in categories:
            total = df[category].apply(convert_rating).sum()
            summed_stats.append(total)

        print(summed_stats)

        # Streamlit app
        st.subheader("Aggregate Talent Attributes")
        st.write("Visualizing the total sum of ratings across all individuals for each talent category.")

        # Create a single radar chart
        fig = go.Figure()

        fig.add_trace(go.Scatterpolar(
            r=summed_stats,
            theta=categories,
            fill='toself',
            name='Total Ratings',
            line_color='rgba(0, 100, 200, 0.7)',  # Sleek blue color
            fillcolor='rgba(0, 100, 200, 0.2)'    # Light fill for elegance
        ))

        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, max(summed_stats) + 5],  # Dynamic range based on max sum, with padding
                    showticklabels=True,
                    tickvals=[0, 5, 10, 15, 20, 25, 30],  # Adjust based on your data's max sum
                    ticktext=['0', '5', '10', '15', '20', '25', '30']  # Custom labels
                ),
                angularaxis=dict(showticklabels=True)
            ),
            showlegend=True,
            title="Total Talent Profile Across All Individuals",
            font=dict(size=12, family="Arial, sans-serif"),  # Clean font
            plot_bgcolor='rgba(0,0,0,0)',  # Transparent background for sleekness
            paper_bgcolor='rgba(0,0,0,0)'   # Transparent paper for elegance
        )

        # Display the chart in Streamlit
        st.plotly_chart(fig, use_container_width=True)

        # Optional: Add a footer or explanation
        st.write("This radar chart shows the sum of all individual ratings across five talent categories.")