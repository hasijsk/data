import streamlit as st

def load_css():
    st.markdown("""
    <style>
        /* Import des polices */
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');

        /* Variables et thème */
        :root {
            --primary: #ffffff;
            --secondary: rgba(255, 255, 255, 0.7);
            --background: #1e293b;
            --text: #ffffff;
            --card-bg: rgba(255, 255, 255, 0.05);
            --border: rgba(255, 255, 255, 0.1);
        }

        /* Style général */
        * {
            font-family: 'Plus Jakarta Sans', sans-serif;
            color: var(--text);
        }

        .stApp, div[data-testid="stAppViewContainer"], .main, .element-container, div.st-emotion-cache-kj6hex {
            background: var(--background) !important;
            color: var(--text) !important;
        }

        /* En-tête */
        h1, h2, h3, h4, h5, h6, p, span, div {
            color: var(--text) !important;
        }

        .subtitle {
            color: var(--secondary) !important;
            font-size: 1.2em;
            margin-bottom: 2.5rem;
            font-weight: 500;
        }

        /* Cartes modernes */
        div[data-testid="stVerticalBlock"] > div {
            background: var(--card-bg);
            border-radius: 16px;
            padding: 2rem;
            margin-bottom: 1.5rem;
            border: 1px solid var(--border);
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        div[data-testid="stVerticalBlock"] > div:hover {
            transform: translateY(-4px);
            box-shadow: 0 12px 24px rgba(0, 0, 0, 0.2);
            border-color: rgba(255, 255, 255, 0.2);
        }

        /* Boutons élégants */
        .stButton > button {
            background: var(--text) !important;
            color: white !important;
            border: none !important;
            padding: 0.75rem 1.5rem !important;
            border-radius: 12px !important;
            font-weight: 600 !important;
            letter-spacing: 0.5px !important;
            transition: all 0.3s ease !important;
            text-transform: uppercase !important;
            font-size: 0.9em !important;
        }

        .stButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1) !important;
        }

        /* Tableaux modernes */
        .stDataFrame {
            background: var(--card-bg) !important;
            border: 1px solid var(--border);
            border-radius: 16px;
            overflow: hidden;
        }

        .stDataFrame thead tr th {
            background: rgba(255, 255, 255, 0.1) !important;
            color: var(--text) !important;
            font-weight: 600;
            padding: 1rem !important;
            font-size: 0.95em;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .stDataFrame tbody tr {
            color: var(--text) !important;
        }

        .stDataFrame tbody tr:hover {
            background: rgba(255, 255, 255, 0.05) !important;
        }

        /* Stats container moderne */
        .stat-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 1.5rem;
            margin: 1.5rem 0;
        }

        .stat-card {
            background: var(--card-bg);
            padding: 1.5rem;
            border-radius: 16px;
            border: 1px solid var(--border);
            transition: all 0.3s ease;
        }

        .stat-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 12px 24px rgba(0, 0, 0, 0.2);
            border-color: rgba(255, 255, 255, 0.2);
        }

        .stat-value {
            font-size: 2em;
            font-weight: 700;
            color: var(--text);
            margin: 0.5rem 0;
            letter-spacing: -0.02em;
        }

        /* Empty state moderne */
        .empty-state {
            text-align: center;
            padding: 4rem 2rem;
            background: var(--card-bg);
            border-radius: 24px;
            margin: 3rem 0;
            border: 1px solid var(--border);
        }

        .empty-state-icon {
            font-size: 4em;
            margin-bottom: 1.5rem;
            opacity: 0.9;
            color: var(--text);
        }

        .empty-state h2 {
            font-weight: 700;
            margin-bottom: 1rem;
            color: var(--text);
        }

        .empty-state p {
            color: var(--secondary);
            font-size: 1.1em;
            margin-bottom: 2rem;
        }

        .badge-container {
            display: flex;
            gap: 0.75rem;
            justify-content: center;
            margin-top: 1.5rem;
            flex-wrap: wrap;
            color: #000000 !important;
        }

        .badge {
            background: #ffffff;
            color: #000000 !important;
            padding: 0.5rem 1rem;
            border-radius: 100px;
            font-size: 0.9em;
            font-weight: 500;
            letter-spacing: 0.5px;
            transition: all 0.3s ease;
        }

        .badge:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            background: #f8f9fa;
        }

        /* Sidebar moderne */
        section[data-testid="stSidebar"] {
            background: #1e293b !important;
            border-right: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: 2px 0 12px rgba(0, 0, 0, 0.1);
        }

        section[data-testid="stSidebar"] .block-container {
            padding-top: 2rem;
            background: #1e293b !important;
        }

        section[data-testid="stSidebar"] h2 {
            color: #ffffff;
            font-weight: 700;
            font-size: 1.2em;
            margin-bottom: 1.5rem;
        }

        section[data-testid="stSidebar"] p {
            color: rgba(255, 255, 255, 0.8);
        }

        section[data-testid="stSidebar"] .stButton > button {
            width: 100%;
            margin-bottom: 0.5rem;
            background: rgba(255, 255, 255, 0.1) !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
        }

        section[data-testid="stSidebar"] .stButton > button:hover {
            background: rgba(255, 255, 255, 0.15) !important;
        }

        /* Ajustements pour les éléments de la sidebar */
        section[data-testid="stSidebar"] [data-testid="stMarkdown"] {
            color: #ffffff;
        }

        section[data-testid="stSidebar"] .stSelectbox > div > div {
            background: rgba(255, 255, 255, 0.05) !important;
            border-color: rgba(255, 255, 255, 0.1) !important;
            color: #ffffff !important;
        }

        section[data-testid="stSidebar"] .stSelectbox > div > div:hover {
            border-color: rgba(255, 255, 255, 0.2) !important;
        }

        section[data-testid="stSidebar"] .stFileUploader {
            color: #ffffff;
        }

        section[data-testid="stSidebar"] .stFileUploader > div {
            background: rgba(255, 255, 255, 0.05) !important;
            border-color: rgba(255, 255, 255, 0.1) !important;
            color: #ffffff !important;
        }

        /* Inputs modernes */
        .stTextInput > div > div {
            background: var(--card-bg) !important;
            border-color: var(--border) !important;
            color: var(--text) !important;
        }

        .stTextInput > div > div:focus-within {
            border-color: rgba(255, 255, 255, 0.3) !important;
            box-shadow: 0 0 0 1px rgba(255, 255, 255, 0.3) !important;
        }

        /* Select boxes modernes */
        .stSelectbox > div > div {
            background: var(--card-bg) !important;
            border-color: var(--border) !important;
            color: var(--text) !important;
        }

        .stSelectbox > div > div:focus-within {
            border-color: rgba(255, 255, 255, 0.3) !important;
            box-shadow: 0 0 0 1px rgba(255, 255, 255, 0.3) !important;
        }

        /* Ajustements supplémentaires pour le thème sombre */
        .stMarkdown, .stMarkdown p {
            color: var(--text) !important;
        }

        .element-container {
            color: var(--text) !important;
        }

        div[data-testid="stMetricValue"] {
            color: var(--text) !important;
        }

        div[data-testid="stMetricLabel"] {
            color: var(--secondary) !important;
        }

        .stPlotlyChart {
            background: var(--card-bg) !important;
            border-radius: 16px;
            padding: 1rem;
            border: 1px solid var(--border);
        }

        /* Ajout du style pour st-emotion-cache-xwtqgq */
        .st-emotion-cache-xwtqgq {
            background-color: #1e293b !important;
        }

        div.st-emotion-cache-xwtqgq {
            background-color: #1e293b !important;
        }

        [class*="st-emotion-cache-xwtqgq"] {
            background-color: #1e293b !important;
        }

        /* Feature Cards Container */
        .features-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            padding: 2rem 0;
        }

        /* Feature Card */
        .feature-card {
            background: #1e293b;
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 2.5rem;
            margin-bottom: 1rem;
        }

        /* Feature Icon */
        .feature-icon {
            font-size: 3em;
            margin-bottom: 1.5rem;
        }

        /* Feature Text */
        .feature-card h3 {
            color: #ffffff;
            font-size: 1.8em;
            font-weight: 700;
            margin-bottom: 1rem;
        }

        .feature-card p {
            color: rgba(255, 255, 255, 0.7);
            font-size: 1.1em;
            line-height: 1.6;
            margin-bottom: 2rem;
        }

        /* Feature List */
        .feature-list {
            list-style: none;
            padding: 0;
            margin: 0;
        }

        .feature-list li {
            color: rgba(255, 255, 255, 0.9);
            font-size: 1.1em;
            padding: 1rem 1.5rem;
            margin-bottom: 0.8rem;
            background: rgba(255, 255, 255, 0.03);
            border-radius: 12px;
        }

        /* CTA Section */
        .cta-section {
            text-align: center;
            padding: 4rem 3rem;
            background: #1e293b;
            border-radius: 30px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            margin: 4rem 0;
        }

        .cta-section h2 {
            color: #ffffff;
            font-size: 3em;
            font-weight: 800;
            margin-bottom: 1rem;
        }

        .cta-section p {
            color: rgba(255, 255, 255, 0.7);
            font-size: 1.3em;
            margin-bottom: 2.5rem;
        }

        /* Badge Container */
        .badge-container {
            display: flex;
            gap: 1rem;
            justify-content: center;
            flex-wrap: wrap;
            margin-top: 2rem;
        }

        .badge {
            background: #ffffff;
            color: #1e293b;
            padding: 0.8rem 1.5rem;
            border-radius: 100px;
            font-size: 1em;
            font-weight: 600;
        }

        /* Styles généraux */
        [data-testid="stAppViewContainer"] {
            background-color: #1e293b;
        }

        [data-testid="stHeader"] {
            background-color: #1e293b;
        }

        .main {
            background-color: #1e293b;
        }

        /* Feature Cards */
        div[data-testid="stMarkdown"] .features-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            padding: 20px;
        }

        div[data-testid="stMarkdown"] .feature-card {
            background-color: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 25px;
            color: white;
        }

        div[data-testid="stMarkdown"] .feature-icon {
            font-size: 40px;
            margin-bottom: 20px;
            display: block;
        }

        div[data-testid="stMarkdown"] h3 {
            color: white !important;
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 15px;
        }

        div[data-testid="stMarkdown"] p {
            color: rgba(255, 255, 255, 0.8) !important;
            font-size: 16px;
            line-height: 1.6;
            margin-bottom: 20px;
        }

        div[data-testid="stMarkdown"] .feature-list {
            list-style: none;
            padding: 0;
            margin: 0;
        }

        div[data-testid="stMarkdown"] .feature-list li {
            color: rgba(255, 255, 255, 0.9) !important;
            background-color: rgba(255, 255, 255, 0.05);
            padding: 12px 20px;
            margin-bottom: 10px;
            border-radius: 8px;
            font-size: 16px;
        }

        /* CTA Section */
        div[data-testid="stMarkdown"] .cta-section {
            background-color: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 40px 20px;
            text-align: center;
            margin: 40px 0;
        }

        div[data-testid="stMarkdown"] .cta-section h2 {
            color: white !important;
            font-size: 32px;
            font-weight: bold;
            margin-bottom: 15px;
        }

        div[data-testid="stMarkdown"] .cta-section p {
            color: rgba(255, 255, 255, 0.8) !important;
            font-size: 18px;
            margin-bottom: 30px;
        }

        /* Badges */
        div[data-testid="stMarkdown"] .badge-container {
            display: flex;
            gap: 10px;
            justify-content: center;
            flex-wrap: wrap;
        }

        div[data-testid="stMarkdown"] .badge {
            background-color: white;
            color: #1e293b !important;
            padding: 8px 16px;
            border-radius: 20px;
            font-weight: 500;
            font-size: 14px;
            display: inline-block;
        }

        /* Sidebar */
        [data-testid="stSidebar"] {
            background-color: #1e293b;
        }

        [data-testid="stSidebar"] [data-testid="stMarkdown"] {
            color: white;
        }
    </style>
    """, unsafe_allow_html=True) 