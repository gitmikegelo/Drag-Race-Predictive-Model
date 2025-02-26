import streamlit as st
import pandas as pd
from graph import Graph
from geolocator import GeoLocator

st.set_page_config(layout="wide")  # Use full width

graph = Graph()
geolocator = GeoLocator()

# Inject custom CSS for a Drag Race aesthetic
st.markdown(
    """
    <style>
    /* Global background with a soft pink-to-white gradient */
    .stApp {
        background: linear-gradient(135deg, #ffe6f2, #ffffff);
    }
    /* Import a decorative font (Cinzel Decorative from Google Fonts) */
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@400;700&display=swap');

    /* Main title styling with text shadow for extra glam */
    h1 {
        color: #ff66a3;
        font-family: 'Cinzel Decorative', cursive;
        text-align: left;
        text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
        margin-bottom: 0.5em;
    }
    /* Subheader styling with similar decorative font */
    h2, h3 {
        color: #ff66a3;
        font-family: 'Cinzel Decorative', cursive;
        text-align: left;
        margin-bottom: 0.5em;
    }
    /* Customize the table appearance */
    .css-1d391kg {
        border: 2px solid #ff66a3;
        border-radius: 10px;
        overflow: hidden;
        margin: 1em 0;
    }
    /* Button styling with hover scaling effect */
    .stButton>button {
         background-color: #ff66a3;
         color: white;
         border: none;
         padding: 10px 20px;
         border-radius: 5px;
         transition: transform 0.2s, box-shadow 0.2s;
    }
    .stButton>button:hover {
         transform: scale(1.05);
         box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
    }
    /* Additional styling for input fields for consistency */
    .stTextInput>div>div>input {
         border: 1px solid #ff66a3;
         border-radius: 5px;
         padding: 5px;
    }
    /* Scrollable panel styling */
    .scrollable-box {
        border: 2px solid #ff66a3;
        border-radius: 10px;
        padding: 15px;
        width: 100%;
        height: 300px;
        overflow-y: scroll;
        background-color: #ffffff;
        color: #333;
        font-family: 'Arial', sans-serif;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Create two columns: left for main content, right for extra space
left_col, right_col = st.columns([1.5, 1])

with left_col:
    st.title("Data and Drag")
    st.subheader("RPDR Finals Probability Dashboard")
    st.write('''Honey, welcome to the glitziest, most fabulous Dashboard of our recent queens and their chances of sashaying into the finals! 
We’ve conjured up this dazzling calculation using an ensemble of high-heel-stomping machine learning models, trained on the fierce data of queens from Season 7 to Season 16. 

Get ready to see who’s serving looks and landing a spot in the finale—served up with a side of sparkle and sass!
         ''')

    data_queens = pd.read_csv('queen_probab.csv')
    data_queens = data_queens.sort_values(by="Probability", ascending=False)
    data_queens['Probability'] = data_queens['Probability'].apply(lambda x: f"{x * 100:.0f}%")

    st.subheader("Season 17")
    html_table = data_queens.to_html(index=False)
    st.markdown(html_table, unsafe_allow_html=True)
    st.write("As of Episode 8*")

    # Display the graph
    graph.get_graph()

    st.subheader("Queens from different places.")
    st.write("Who are the baddie queens of the West.")
    
    # Display geolocation
    geolocator.get_geo()

with right_col:

    st.markdown("""
### Development of the Predictive Model, Hunty: Serving Stats with Drag Realness

Alright, dolls, let’s spill the tea on how this predictive model came to sashay into existence—because we’re not just throwing glitter at a wall and calling it couture. We’re talking a full-on werkroom glow-up with data from 139 fierce queens across Seasons 7 to 16 of *RuPaul’s Drag Race*. These are the gurls who’ve brought the drama, the looks, and the lip-sync slayage, and we’re breaking it all down like a sickening runway critique.

#### The Dataset: 139 Queens, No Filler, All Killer

Our dataset is a fabulous lineup of 139 queens, spanning from the high-fashion eleganza of Season 7 to the gag-worthy moments of Season 16. We’ve got the stats that matter, honey:

- **Number of Episodes:** How long these dolls stayed in the game before they had to sashay away.
- **Wins and Bottoms Per Episode:** We took the total number of WINS (those “Condragulations, you’re a winner, baby!” moments) and BOTTOMS (the “Lip sync for your life, gurl” close calls), then divided that by the total episodes in their season. It’s the T on their track record, serving consistency or chaos.
- **Category Scores:** We rated these queens on a scale of “meh” to “mother-tucking iconic” across four gag-worthy domains:
  - *Fashion Runway:* Are they serving high couture or Party City clearance rack?
  - *Comedy:* Can they make Ru cackle or are they bombing harder than a shady reading challenge?
  - *Performance:* Do they own the stage like a main challenge queen or fade into the backdrop?
  - *Lip Sync:* Are they turning the party or just flailing like a fish out of sequins?
- **Sentiment Analysis by Grok 3:** Our fabulous AI sidekick, Grok 3, got in on the action, reading the vibes of these queens like a psychic at a drag brunch. Positive, negative, or shady neutral—we’ve got the emotional runway covered.

#### The Model: Werking the Numbers Like a Lip Sync Assassin

Now, let’s talk about the techy realness, because this ain’t no basic kiki. I threw every trick in the book at this predictive gig—think of it like a maxi challenge with extra glitter. We tested a whole lineup of models, gurls:

- *Random Forest:* For that deep, leafy decision-making realness.
- *SVM (Support Vector Machine):* Cutting through the noise like a sharp stiletto.
- *Logistic Regression:* Classic, reliable, and ready to calculate the odds.
- *Naive Bayes:* Simple but sassy, bringing some probabilistic T.

I didn’t just stop there, oh no—I turned it into a full-on grid search extravaganza, tweaking every knob and dial on these models like a queen perfecting her tuck. After countless iterations—think weeks of “Can I get an amen up in here?”—and some fierce feature engineering (adding more spice to the data pot), I landed on the ultimate slay: an **ensemble of Random Forest and Logistic Regression**. This dynamic duo clocked a **90% accuracy** on a 90-10 train-test split. That’s right, 90% of the time, this model knows who’s gonna shantay and who’s gonna sashay before the lip sync even starts. Werk it!

#### The Prediction Results: Reading the Current Season’s House Down

So, what’s the tea on the dashboard? It’s serving up predictions for the queens of the current season—Season 17, airing as of this glorious moment on February 26, 2025—using that trained ensemble model. We’re taking all that juicy data from Seasons 7 to 16, mixing it with the fresh beats of the new season, and letting the model spill the T: who’s got the charisma, uniqueness, nerve, and talent to snatch the crown? It’s like a crystal ball for drag superstardom, but with better makeup and no foggy vibes.

""")

    
    

    # Display scrollable panel
    