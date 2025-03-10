import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from utils.statistical_analysis import (
    calculate_descriptive_stats, plot_distribution_analysis
)
from utils.style import load_css

# Configuration de la page
st.set_page_config(
    page_title="Analyse Descriptive Avancée",
    page_icon="📊",
    layout="wide"
)

# Style personnalisé
st.markdown("""
<style>
    .stApp {
        background-color: #1e293b;
        background-image: radial-gradient(at 47% 33%, rgba(69, 59, 100, 0.4) 0, transparent 59%), radial-gradient(at 82% 65%, rgba(41, 84, 128, 0.4) 0, transparent 55%);
    }

    .main-header {
        text-align: center;
        padding: 2rem 0;
        margin-bottom: 2rem;
        animation: fadeIn 0.8s ease-out;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .gradient-text {
        background: linear-gradient(120deg, #ffffff, #a8b8d0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem !important;
        font-weight: 800 !important;
    }

    .subtitle {
        color: rgba(255, 255, 255, 0.8);
        font-size: 1.2rem;
        margin-top: 1rem;
    }

    .glass-container {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        transition: transform 0.3s ease;
    }

    .glass-container:hover {
        transform: translateY(-5px);
    }

    .stat-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
        padding: 1rem;
    }

    .stat-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        padding: 1.5rem;
        text-align: center;
        transition: all 0.3s ease;
    }

    .stat-card:hover {
        transform: translateY(-5px);
        background: rgba(255, 255, 255, 0.08);
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
    }

    .stat-value {
        font-size: 1.8rem;
        font-weight: 700;
        color: #fff;
        margin: 0.5rem 0;
        background: linear-gradient(120deg, #ffffff, #a8b8d0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .stat-label {
        color: rgba(255, 255, 255, 0.7);
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .sidebar-header {
        background: rgba(255, 255, 255, 0.05);
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
    }

    .sidebar-header h2 {
        color: white;
        font-size: 1.5rem;
        margin: 0;
    }

    .file-uploader {
        background: rgba(255, 255, 255, 0.03);
        border: 2px dashed rgba(255, 255, 255, 0.2);
        border-radius: 10px;
        padding: 2rem;
        text-align: center;
        transition: all 0.3s ease;
    }

    .file-uploader:hover {
        border-color: rgba(255, 255, 255, 0.4);
        background: rgba(255, 255, 255, 0.05);
    }

    .section-title {
        color: white;
        font-size: 1.8rem;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid rgba(255, 255, 255, 0.1);
    }

    .info-box {
        background: rgba(255, 255, 255, 0.03);
        border-left: 4px solid #4CAF50;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 0 10px 10px 0;
    }

    .warning-box {
        background: rgba(255, 255, 255, 0.03);
        border-left: 4px solid #FFC107;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 0 10px 10px 0;
    }

    /* Style pour les graphiques */
    .plot-container {
        background: rgba(255, 255, 255, 0.03);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }

    /* Style pour le DataFrame */
    .dataframe-container {
        background: rgba(255, 255, 255, 0.03);
        border-radius: 15px;
        padding: 1rem;
        margin: 1rem 0;
        overflow: auto;
    }

    .stDataFrame {
        background-color: transparent !important;
    }

    .stDataFrame td, .stDataFrame th {
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# En-tête de la page
st.markdown("""
<div class="main-header">
    <h1 class="gradient-text">📊 Analyse Descriptive Avancée</h1>
    <p class="subtitle">Explorez et visualisez vos données avec des outils statistiques puissants</p>
</div>
""", unsafe_allow_html=True)

# Sidebar pour le chargement des données
with st.sidebar:
    st.markdown("""
    <div class="sidebar-header">
        <h2>🔄 Configuration de l'Analyse</h2>
    </div>
    """, unsafe_allow_html=True)
    
    with st.container():
        st.markdown("""
        <div class="file-uploader">
            <p style="color: rgba(255, 255, 255, 0.8);">Déposez votre fichier CSV ici</p>
        </div>
        """, unsafe_allow_html=True)
        uploaded_file = st.file_uploader("", type=['csv'])
    
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.markdown("""
            <div class="info-box">
                ✅ Données chargées avec succès!
                <br>Nombre de lignes: {}<br>
                Nombre de colonnes: {}
            </div>
            """.format(len(df), len(df.columns)), unsafe_allow_html=True)
        except Exception as e:
            st.markdown(f"""
            <div class="warning-box">
                ❌ Erreur lors du chargement : {str(e)}
            </div>
            """, unsafe_allow_html=True)
            df = None
    else:
        df = None

# Contenu principal
if df is not None:
    # Vue d'ensemble des données
    st.markdown("""
    <div class="glass-container">
        <h2 class="section-title">📋 Vue d'ensemble des données</h2>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-value">{len(df)}</div>
            <div class="stat-label">Nombre de lignes</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-value">{len(df.columns)}</div>
            <div class="stat-label">Nombre de colonnes</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        missing_values = df.isnull().sum().sum()
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-value">{missing_values}</div>
            <div class="stat-label">Valeurs manquantes</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # Données brutes avec options de filtrage
    st.markdown("""
    <div class="glass-container">
        <h2 class="section-title">🔍 Exploration des Données</h2>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 1])
    with col2:
        search = st.text_input("🔍 Rechercher une colonne")
        
    filtered_cols = [col for col in df.columns if not search or search.lower() in col.lower()]
    if len(filtered_cols) > 0:
        with col1:
            selected_cols = st.multiselect("Sélectionner les colonnes à afficher", filtered_cols, default=filtered_cols[:5])
        
        if selected_cols:
            st.markdown('<div class="dataframe-container">', unsafe_allow_html=True)
            st.dataframe(df[selected_cols], height=300)
            st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.warning("Aucune colonne ne correspond à votre recherche.")
    
    st.markdown("</div>", unsafe_allow_html=True)

    # Analyse statistique
    st.markdown("""
    <div class="glass-container">
        <h2 class="section-title">📈 Analyse Statistique</h2>
    """, unsafe_allow_html=True)
    
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    
    if len(numeric_columns) > 0:
        selected_column = st.selectbox("Sélectionnez une colonne pour l'analyse", numeric_columns)
        
        if selected_column:
            stats = calculate_descriptive_stats(df[selected_column])
            
            st.markdown('<div class="stat-grid">', unsafe_allow_html=True)
            
            metrics = [
                ("Moyenne", stats['moyenne'], "La valeur moyenne des données"),
                ("Médiane", stats['médiane'], "La valeur centrale des données"),
                ("Écart-type", stats['écart_type'], "Mesure de la dispersion des données"),
                ("Mode", stats['mode'], "La valeur la plus fréquente"),
                ("Skewness", stats['skewness'], "Mesure de l'asymétrie"),
                ("Kurtosis", stats['kurtosis'], "Mesure de l'aplatissement")
            ]
            
            for label, value, description in metrics:
                st.markdown(f"""
                <div class="stat-card" title="{description}">
                    <div class="stat-label">{label}</div>
                    <div class="stat-value">{value:.2f}</div>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Visualisation
            st.markdown("""
            <div class="plot-container">
                <h3 style="color: white; margin-bottom: 1rem;">Distribution des données</h3>
            """, unsafe_allow_html=True)
            
            fig = plot_distribution_analysis(df[selected_column], f"Distribution de {selected_column}")
            st.pyplot(fig)
            
            st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="warning-box">
            ⚠️ Aucune colonne numérique trouvée dans les données
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

else:
    # Message d'accueil amélioré
    st.markdown("""
    <div class="glass-container" style="text-align: center; max-width: 800px; margin: 4rem auto;">
        <div style="font-size: 4rem; margin-bottom: 2rem;">📤</div>
        <h2 style="color: white; margin-bottom: 1rem;">Commencez votre analyse</h2>
        <p style="color: rgba(255, 255, 255, 0.8); margin-bottom: 2rem;">
            Importez un fichier CSV via le menu latéral pour explorer vos données en détail
        </p>
        <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
            <div class="stat-card" style="min-width: 200px;">
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">📊</div>
                <div class="stat-label">Visualisations Interactives</div>
            </div>
            <div class="stat-card" style="min-width: 200px;">
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">📈</div>
                <div class="stat-label">Analyses Statistiques</div>
            </div>
            <div class="stat-card" style="min-width: 200px;">
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">🔍</div>
                <div class="stat-label">Exploration des Données</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True) 