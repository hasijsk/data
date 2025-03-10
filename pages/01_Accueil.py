import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Accueil - Analyse Descriptive",
    page_icon="📊",
    layout="wide"
)

# Style personnalisé avec animations améliorées
st.markdown("""
<style>
    .stApp {
        background-color: #1e293b;
        background-image: 
            radial-gradient(at 47% 33%, rgba(69, 59, 100, 0.4) 0, transparent 59%), 
            radial-gradient(at 82% 65%, rgba(41, 84, 128, 0.4) 0, transparent 55%);
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }

    .glass-container {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        animation: fadeIn 0.8s ease-out;
    }

    .title-container {
        text-align: center;
        padding: 3rem 1rem;
        animation: fadeIn 0.6s ease-out;
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
        animation: float 6s ease-in-out infinite;
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
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }

    .feature-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(120deg, transparent, rgba(255,255,255,0.1), transparent);
        transform: translateX(-100%);
        transition: 0.5s;
    }

    .feature-card:hover::before {
        transform: translateX(100%);
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
        transition: all 0.3s ease;
    }

    .feature-card:hover .feature-icon {
        transform: scale(1.1) rotate(5deg);
        background: rgba(255, 255, 255, 0.2);
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
        cursor: pointer;
    }

    .list-item:hover {
        background: rgba(255, 255, 255, 0.05);
        transform: translateX(5px);
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
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
        cursor: pointer;
    }

    .badge:hover {
        transform: translateY(-2px) scale(1.05);
        background: white;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
    }

    .section-title {
        color: white !important;
        font-size: 2.2rem !important;
        font-weight: 700 !important;
        margin-bottom: 1rem !important;
        position: relative;
        display: inline-block;
    }

    .section-title::after {
        content: '';
        position: absolute;
        left: 0;
        bottom: -5px;
        width: 100%;
        height: 2px;
        background: linear-gradient(90deg, rgba(255,255,255,0.1), rgba(255,255,255,0.7), rgba(255,255,255,0.1));
    }

    .section-subtitle {
        color: rgba(255, 255, 255, 0.7) !important;
        font-size: 1.2rem !important;
        max-width: 600px;
        margin: 0 auto 2rem auto !important;
    }

    .stats-container {
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
        margin: 2rem 0;
    }

    .stat-item {
        text-align: center;
        padding: 1.5rem;
        margin: 1rem;
        background: rgba(255, 255, 255, 0.03);
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        min-width: 200px;
    }

    .stat-number {
        font-size: 2.5rem;
        font-weight: 700;
        color: white;
        margin-bottom: 0.5rem;
        background: linear-gradient(120deg, #ffffff, #a8b8d0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .stat-label {
        color: rgba(255, 255, 255, 0.7);
        font-size: 1.1rem;
    }
</style>
""", unsafe_allow_html=True)

# En-tête
st.markdown("""
<div class="title-container">
    <h1 class="main-title">📊 Analyse Descriptive Interactive</h1>
    <p class="subtitle">Explorez et analysez vos données en profondeur</p>
</div>
""", unsafe_allow_html=True)

# Création de deux colonnes pour les cartes principales
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📈</div>
        <h3 class="feature-title">Exploration des Données</h3>
        <p class="feature-text">Des outils puissants pour comprendre vos données</p>
        <div class="list-item">📊 Visualisation interactive et dynamique</div>
        <div class="list-item">🔍 Filtrage intelligent des données</div>
        <div class="list-item">💡 Interface intuitive et réactive</div>
        <div class="list-item">📱 Analyses statistiques avancées</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🎯</div>
        <h3 class="feature-title">Guide d'Utilisation</h3>
        <p class="feature-text">Suivez ces étapes pour une analyse efficace</p>
        <div class="list-item">1️⃣ Importez votre fichier CSV via le menu latéral</div>
        <div class="list-item">2️⃣ Explorez les différentes visualisations</div>
        <div class="list-item">3️⃣ Analysez les tendances et patterns</div>
        <div class="list-item">4️⃣ Exportez vos résultats</div>
    </div>
    """, unsafe_allow_html=True)


# Section Support et Ressources
st.markdown("""
<div class="glass-container" style="text-align: center; margin-top: 0.5cm;">
    <h2 class="section-title">❓ Support & Ressources</h2>
    <p class="section-subtitle">Tout ce dont vous avez besoin pour réussir</p>
    <div style="margin-top: 2rem;">
        <span class="badge">📚 Documentation Complète</span>
        <span class="badge">🎓 Tutoriels Vidéo</span>
        <span class="badge">💬 Chat Support 24/7</span>
        <span class="badge">📈 Exemples Pratiques</span>
    </div>
    <div style="margin-top: 1rem;">
        <span class="badge">👥 Communauté active</span>
    </div>
</div>
""", unsafe_allow_html=True)
