import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Accueil",
    page_icon="🏠",
    layout="wide"
)

# Style personnalisé
st.markdown("""
<style>
    .stApp {
        background-color: #1e293b;
        background-image: 
            radial-gradient(at 47% 33%, rgba(69, 59, 100, 0.4) 0, transparent 59%), 
            radial-gradient(at 82% 65%, rgba(41, 84, 128, 0.4) 0, transparent 55%);
    }

    .glass-container {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
    }

    .title-container {
        text-align: center;
        padding: 3rem 1rem;
    }

    .main-title {
        color: white !important;
        font-size: 3.5rem !important;
        font-weight: 800 !important;
        margin-bottom: 1rem !important;
        line-height: 1.2 !important;
        background: linear-gradient(120deg, #ffffff, #a8b8d0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .subtitle {
        color: rgba(255, 255, 255, 0.8) !important;
        font-size: 1.5rem !important;
        margin-bottom: 2rem !important;
        font-weight: 400 !important;
    }

    .feature-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 2rem;
        height: 100%;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
        border-color: rgba(255, 255, 255, 0.2);
    }

    .feature-icon {
        font-size: 2.5rem;
        margin-bottom: 1.5rem;
        background: rgba(255, 255, 255, 0.1);
        width: 70px;
        height: 70px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }

    .feature-title {
        color: white !important;
        font-size: 1.8rem !important;
        font-weight: 600 !important;
        margin: 1rem 0 !important;
    }

    .feature-text {
        color: rgba(255, 255, 255, 0.7) !important;
        font-size: 1.1rem !important;
        line-height: 1.6 !important;
    }

    .list-item {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 1rem 1.5rem;
        border-radius: 12px;
        margin: 0.7rem 0;
        color: rgba(255, 255, 255, 0.9) !important;
        font-size: 1.1rem;
        transition: all 0.3s ease;
    }

    .list-item:hover {
        background: rgba(255, 255, 255, 0.05);
        transform: translateX(5px);
    }

    .badge {
        background: rgba(255, 255, 255, 0.9);
        color: #1e293b;
        padding: 0.7rem 1.2rem;
        border-radius: 100px;
        margin: 0.5rem;
        font-weight: 500;
        font-size: 0.95rem;
        transition: all 0.3s ease;
        border: 2px solid transparent;
        display: inline-block;
    }

    .badge:hover {
        transform: translateY(-2px);
        background: white;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
    }

    .cta-section {
        text-align: center;
        padding: 4rem 2rem;
        background: rgba(255, 255, 255, 0.02);
        border-radius: 30px;
        margin: 3rem 0;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }

    .section-title {
        color: white !important;
        font-size: 2.2rem !important;
        font-weight: 700 !important;
        margin-bottom: 1rem !important;
    }

    .section-subtitle {
        color: rgba(255, 255, 255, 0.7) !important;
        font-size: 1.2rem !important;
        max-width: 600px;
        margin: 0 auto 2rem auto !important;
    }
</style>
""", unsafe_allow_html=True)

# En-tête
st.markdown("""
<div class="title-container">
    <h1 class="main-title">🌟 Bienvenue dans l'Analyseur de Données</h1>
    <p class="subtitle">Une solution moderne et puissante pour explorer vos données</p>
</div>
""", unsafe_allow_html=True)

# Création de deux colonnes pour les cartes
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">💡</div>
        <h3 class="feature-title">Fonctionnalités Principales</h3>
        <p class="feature-text">Découvrez nos outils puissants et intuitifs</p>
        <div class="list-item">📊 Visualisations interactives avancées</div>
        <div class="list-item">📈 Analyses statistiques détaillées</div>
        <div class="list-item">🔍 Exploration approfondie des données</div>
        <div class="list-item">📱 Interface moderne et responsive</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🚀</div>
        <h3 class="feature-title">Pour Commencer</h3>
        <p class="feature-text">Un processus simple en quatre étapes</p>
        <div class="list-item">1️⃣ Importez vos données CSV</div>
        <div class="list-item">2️⃣ Choisissez vos analyses</div>
        <div class="list-item">3️⃣ Explorez les résultats</div>
        <div class="list-item">4️⃣ Exportez vos insights</div>
    </div>
    """, unsafe_allow_html=True)

# Section Avantages
st.markdown("""
<div class="cta-section">
    <h2 class="section-title">✨ Pourquoi Nous Choisir ?</h2>
    <p class="section-subtitle">Une solution complète qui s'adapte à vos besoins</p>
    <div style="margin-top: 2rem;">
        <span class="badge">⚡ Performance</span>
        <span class="badge">🛡️ Sécurité</span>
        <span class="badge">📱 Responsive</span>
        <span class="badge">🔄 Temps Réel</span>
        <span class="badge">📊 Visualisations</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Call to Action
st.markdown("""
<div class="glass-container" style="text-align: center;">
    <h2 class="section-title">🎯 Prêt à Découvrir ?</h2>
    <p class="section-subtitle">Commencez votre voyage d'analyse de données dès maintenant</p>
    <div style="margin-top: 2rem;">
        <span class="badge">✨ Gratuit</span>
        <span class="badge">🔓 Open Source</span>
        <span class="badge">👥 Support Communautaire</span>
    </div>
</div>
""", unsafe_allow_html=True) 