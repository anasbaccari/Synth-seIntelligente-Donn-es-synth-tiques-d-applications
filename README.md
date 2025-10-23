# SynthèseIntelligente — Génération de données synthétiques avec l’IA

**SynthèseIntelligente** est un projet qui utilise un **réseau antagoniste génératif (GAN)** pour créer des **données synthétiques réalistes** à partir de jeux de données réels.  
L’objectif est de simuler des comportements d’utilisation d’applications mobiles, tout en préservant la confidentialité des données originales.  

Le projet comprend trois étapes principales :  
1. **Prétraitement des données** — Nettoyage et normalisation du dataset réel.  
2. **Entraînement du modèle GAN** — Génération de données synthétiques à l’aide de réseaux de neurones.  
3. **Visualisation et validation** — Analyse et comparaison entre données réelles et générées.

---

### Prétraitement des données
Le jeu de données est préparé à l’aide de `pandas` et `scikit-learn` afin d’être compatible avec le modèle GAN.  
![Data preprocessing](screenshots/preprocessing.png)

### Entraînement du GAN
Le modèle est entraîné sur plusieurs itérations pour apprendre la distribution des données réelles.  
![GAN training logs](screenshots/training.png)

### Données synthétiques générées
Une fois l’entraînement terminé, le générateur produit de nouvelles données simulant un comportement d’utilisation réaliste.  
![Synthetic data](screenshots/synthetic_data.png)
