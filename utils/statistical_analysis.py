import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def calculate_descriptive_stats(series):
    """Calcule les statistiques descriptives pour une série de données."""
    return {
        'effectif': len(series),
        'moyenne': np.mean(series),
        'médiane': np.median(series),
        'mode': series.mode().iloc[0] if not series.mode().empty else np.nan,
        'écart_type': np.std(series),
        'coefficient_variation': (np.std(series) / np.mean(series) * 100) if np.mean(series) != 0 else np.nan,
        'skewness': series.skew(),
        'kurtosis': series.kurtosis()
    }

def plot_distribution_analysis(series, title):
    """Crée un graphique de distribution pour une série de données."""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Histogramme avec courbe de densité
    sns.histplot(data=series, kde=True, ax=ax)
    
    # Personnalisation du graphique
    ax.set_title(title)
    ax.set_xlabel('Valeurs')
    ax.set_ylabel('Fréquence')
    
    # Ajout des lignes verticales pour la moyenne et la médiane
    mean_val = np.mean(series)
    median_val = np.median(series)
    
    ax.axvline(mean_val, color='red', linestyle='--', label=f'Moyenne: {mean_val:.2f}')
    ax.axvline(median_val, color='green', linestyle='--', label=f'Médiane: {median_val:.2f}')
    
    ax.legend()
    plt.tight_layout()
    
    return fig 