# ================================
# Quantum Noise Models – Final Project Code
# ================================

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from IPython.display import display, Markdown
from ipywidgets import interact, SelectMultiple

# --- Parameters ---
key_length = 512
original_key = ''.join(np.random.choice(['0','1'], key_length))

# All supported noise models
noise_models = [
    'Bit Flip', 'Phase Flip', 'Bit-Phase Flip', 'Depolarizing',
    'Amplitude Damping', 'Generalized Amplitude Damping', 'Phase Damping',
    'Non-Markovian', 'Collective Correlated', 'Gaussian Bosonic',
    'Polarization Mode Dispersion', 'Photon Number Splitting'
]

# --- Noise Simulation ---
def apply_noise(key, p, model):
    noisy = ""
    for i, bit in enumerate(key):
        rand = np.random.rand()
        if model == 'Bit Flip':
            noisy += '1' if bit=='0' and rand<p else '0' if bit=='1' and rand<p else bit
        elif model == 'Phase Flip':
            noisy += bit
        elif model == 'Bit-Phase Flip':
            noisy += '1' if bit=='0' and rand<p else '0' if bit=='1' and rand<p else bit
        elif model == 'Depolarizing':
            noisy += np.random.choice(['0','1']) if rand<p else bit
        elif model == 'Amplitude Damping':
            noisy += '0' if bit=='1' and rand<p else bit
        elif model == 'Generalized Amplitude Damping':
            if bit=='1' and rand<p*0.6: noisy += '0'
            elif bit=='0' and rand<p*0.4: noisy += '1'
            else: noisy += bit
        elif model == 'Phase Damping':
            noisy += bit
        elif model == 'Non-Markovian':
            noisy += np.random.choice(['0','1']) if rand<p and i%2==0 else bit
        elif model == 'Collective Correlated':
            noisy += '1' if bit=='0' and rand<p else '0' if bit=='1' and rand<p else bit
        elif model == 'Gaussian Bosonic':
            noisy += np.random.choice(['0','1']) if np.random.normal(0,0.1)+p>0.15 else bit
        elif model == 'Polarization Mode Dispersion':
            noisy += '1' if bit=='0' and rand<p/2 else '0' if bit=='1' and rand<p/2 else bit
        elif model == 'Photon Number Splitting':
            noisy += '1' if bit=='1' and rand<p else bit
        else:
            noisy += bit
    return noisy

# --- Metrics ---
def qber(orig, noisy):
    return sum(o!=n for o,n in zip(orig,noisy)) / len(orig)

def shannon_entropy(q):
    if q in (0,1): return 0
    return -q*np.log2(q) - (1-q)*np.log2(1-q)

def adaptive_amplification(ent):
    if ent>=0.9:  return 1.0
    if ent>=0.75: return 0.75
    if ent>=0.6:  return 0.6
    return 0.5

# --- Unified Static vs Adaptive across ALL models ---
def unified_comparison_all_models():
    noise_range = np.linspace(0.01, 0.3, 12)
    static_baseline = key_length // 2
    adaptive_matrix = []
    model_gains = {}

    for model in noise_models:
        adaps = []
        for p in noise_range:
            nk  = apply_noise(original_key, p, model)
            q   = qber(original_key, nk)
            ent = 1 - shannon_entropy(q)
            ada = int(key_length * adaptive_amplification(ent))
            adaps.append(ada)
        adaptive_matrix.append(adaps)
        model_gains[model] = np.mean(np.array(adaps) - static_baseline)

    adaptive_matrix = np.array(adaptive_matrix)
    mean_adaptive   = adaptive_matrix.mean(axis=0)
    min_adaptive    = adaptive_matrix.min(axis=0)
    max_adaptive    = adaptive_matrix.max(axis=0)

    # Identify best and worst models
    best_model = max(model_gains, key=model_gains.get)
    worst_model = min(model_gains, key=model_gains.get)
    best_gain = model_gains[best_model]
    worst_gain = model_gains[worst_model]

    # Plot unified graph
    plt.figure(figsize=(11, 7))
    for row in adaptive_matrix:
        plt.plot(noise_range, row, alpha=0.25, linewidth=1, color="gray")

    plt.fill_between(noise_range, min_adaptive, max_adaptive,
                     alpha=0.12, label="Adaptive range (min–max)")
    plt.plot(noise_range, mean_adaptive, linewidth=2.5, color="blue",
             label="Adaptive (mean across models)")
    plt.plot(noise_range, [static_baseline]*len(noise_range), '--', linewidth=2, color="red",
             label=f"Static baseline ({static_baseline} bits)")

    # Highlight best and worst models
    idx_best = noise_models.index(best_model)
    idx_worst = noise_models.index(worst_model)
    plt.plot(noise_range, adaptive_matrix[idx_best], linewidth=3, color="green",
             label=f"Best: {best_model} (+{best_gain:.1f} bits)")
    plt.plot(noise_range, adaptive_matrix[idx_worst], linewidth=3, color="orange",
             label=f"Worst: {worst_model} ({worst_gain:.1f} bits)")

    # Annotate best/worst
    plt.text(noise_range[-1], adaptive_matrix[idx_best][-1],
             f"⬆ {best_model}", color="green", fontsize=12,
             ha="right", va="bottom")
    plt.text(noise_range[-1], adaptive_matrix[idx_worst][-1],
             f"⬇ {worst_model}", color="orange", fontsize=12,
             ha="right", va="top")

    plt.title("Unified Retention vs Noise\nStatic vs Adaptive across ALL Models")
    plt.xlabel("Noise Probability (p)")
    plt.ylabel("Secure Bits Retained")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Textual summary
    avg_gain   = float(np.mean(mean_adaptive - static_baseline))
    gain_at_max= float(mean_adaptive[-1] - static_baseline)
    display(Markdown(
        f"""
**Unified Comparison Summary**

- Best model favouring adaptive amplification: **{best_model}**
  (average gain = {best_gain:.2f} bits over static)

- Worst model for adaptive amplification: **{worst_model}**
  (average gain = {worst_gain:.2f} bits over static)

- Mean adaptive vs static gain (all models): {avg_gain:.2f} bits
- Gain at highest noise (p = {noise_range[-1]:.2f}): {gain_at_max:.2f} bits
"""
    ))

# --- Run visualization once ---
unified_comparison_all_models()
