# app.py
import streamlit as st
import pandas as pd
import json
from PIL import Image
import os

st.set_page_config(page_title="Sarovar TT Stats", layout="wide", initial_sidebar_state="expanded")
# st.markdown("""
#     <style>
#     body {background-color: #0e1117; color: white;}
#     .stApp {background-color: #0e1117;}
#     </style>
# """, unsafe_allow_html=True)
st.markdown("""
    <style>
    .stDataFrame tbody td {
        text-align: center !important;
        white-space: nowrap !important;
    }
    .stDataFrame thead th {
        text-align: center !important;
        white-space: nowrap !important;
    }
    </style>
""", unsafe_allow_html=True)



# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Overall Stats", "Elo Ratings"])

# Load data paths
ASSETS_PATH = "assets"

# Load helper data
# with open(os.path.join(ASSETS_PATH, "last_updated.txt"), 'r') as f:
#     last_updated = f.read().strip()

# st.sidebar.markdown(f"**Last Updated:** {last_updated}")

# Page 1: Overall Stats
if page == "Overall Stats":
    st.title("\U0001F3D3 Overall Stats Dashboard")

    # Player Stats Table
    st.header("Player Stats")
    df_player = pd.read_json(os.path.join(ASSETS_PATH, "player_stats.json"))
    df_player.columns = ["Player", "Games", "Wins", "Losses", "Points Scored", "Points Against", "Win%", "Point Win%", "Point Diff", "Diff/Game"]
    st.dataframe(df_player.style.format({"Win%": "{:.1%}", "Point Win%": "{:.1%}", "Diff/Game": "{:.2f}"}), hide_index=True, width=800)

    # Team Stats Table
    st.header("Team Combination Stats")
    df_team = pd.read_json(os.path.join(ASSETS_PATH, "team_stats.json"))
    df_team.columns = ["Team", "Games", "Wins", "Losses", "Win%", "Point Diff", "Diff/Game"]
    st.dataframe(df_team.style.format({"Win%": "{:.1%}", "Diff/Game": "{:.2f}"}), hide_index=True, width=600)

    # Point Diff in Wins/Losses
    st.header("Average Point Differential in Wins/Losses")
    df_point_diff = pd.read_json(os.path.join(ASSETS_PATH, "point_diff_stats.json"))
    df_point_diff.columns = ["Player", "Avg Diff (Wins)", "Avg Diff (Losses)", "Variance"]
    st.dataframe(df_point_diff.style.format({"Avg Diff (Wins)": "{:.2f}", "Avg Diff (Losses)": "{:.2f}"}), hide_index=True, width=400)

    # Heatmaps
    st.header("Win % by Partner")
    partner_heatmap = Image.open(os.path.join(ASSETS_PATH, "partner_heatmap.png"))
    st.image(partner_heatmap, width=800)

    st.header("Win % by Opponent")
    opponent_heatmap = Image.open(os.path.join(ASSETS_PATH, "opponent_heatmap.png"))
    st.image(opponent_heatmap, width=800)

# Page 2: Elo Ratings
elif page == "Elo Ratings":
    st.title("\U0001F4CA Elo Ratings Dashboard")

    # Leaderboard
    st.header("Leaderboard")
    df_leaderboard = pd.read_json(os.path.join(ASSETS_PATH, "leaderboard.json"))
    df_leaderboard.columns = ["Player", "Rating"]
    st.dataframe(df_leaderboard.style.format({"Rating": "{:.1f}"}), hide_index=True, width = 200)

    # Elo Graph
    st.header("Elo Ratings Chart")
    elo_graph = Image.open(os.path.join(ASSETS_PATH, "elo_graph.png"))
    st.image(elo_graph, use_container_width=True)
