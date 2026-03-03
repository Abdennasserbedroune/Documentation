import re

# Read original HTML
with open('final doc.html', 'r', encoding='utf-8') as f:
    html = f.read()

# French translations
translations = {
    'lang="en"': 'lang="fr"',
    '<title>Beewant Documentation</title>': '<title>Documentation Beewant</title>',
    'placeholder="Search docs..."': 'placeholder="Rechercher dans la doc..."',
    'Account management': 'Gestion des comptes',
    'Getting started': 'Premiers pas',
    'Profile &amp; Personal Information': 'Profil et informations personnelles',
    'Security &amp; Passwords': 'Sécurité et mots de passe',
    'API Access': 'Accès API',
    'Preferences': 'Préférences',
    'Plans &amp; Billing': 'Plans et facturation',
    'Agents': 'Agents',
    'creation of agents': 'création d\'agents',
    'customize agents': 'personnaliser les agents',
    'share agents': 'partager les agents',
    'Library and collections': 'Bibliothèque et collections',
    'supported formats': 'formats pris en charge',
    'creat collection': 'créer une collection',
    'share collection': 'partager une collection',
    'Chat': 'Chat',
    'Start chat': 'Démarrer le chat',
    'chat with text': 'chat avec texte',
    'chat with image': 'chat avec image',
    'chat with collectins': 'chat avec collections',
    'chat with web': 'chat avec web',
    'Tools': 'Outils',
    'core capabilities': 'capacités principales',
    'Image generation': 'génération d\'images',
    'analayzing data': 'analyse de données',
    'FAQ': 'FAQ',
    'Examples and use cases': 'Exemples et cas d\'utilisation',
    'Technical Recommendations': 'Recommandations techniques',
}

# Apply translations
for eng, fr in translations.items():
    html = html.replace(eng, fr)

# Save French version
with open('frenchdoc.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✓ frenchdoc.html created!")
