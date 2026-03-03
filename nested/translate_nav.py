import re

with open('final doc.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace lang attribute
html = html.replace('lang="en"', 'lang="fr"')

# Replace title
html = html.replace('<title>Beewant Documentation</title>', '<title>Documentation Beewant</title>')

# Replace search placeholder
html = html.replace('placeholder="Search docs..."', 'placeholder="Rechercher dans la doc..."')

# Sidebar navigation items
html = html.replace('>Account management<', '>Gestion des comptes<')
html = html.replace('>Getting started<', '>Premiers pas<')
html = html.replace('>Profile &amp; Personal Information<', '>Profil et informations personnelles<')
html = html.replace('>Security &amp; Passwords<', '>Sécurité et mots de passe<')
html = html.replace('>API Access<', '>Accès API<')
html = html.replace('>Preferences<', '>Préférences<')
html = html.replace('>Plans &amp; Billing<', '>Plans et facturation<')
html = html.replace('>Agents<', '>Agents<')
html = html.replace('>creation of agents<', '>création d\'agents<')
html = html.replace('>customize agents<', '>personnaliser les agents<')
html = html.replace('>share agents<', '>partager les agents<')
html = html.replace('>Library and collections<', '>Bibliothèque et collections<')
html = html.replace('>supported formats<', '>formats pris en charge<')
html = html.replace('>creat collection<', '>créer une collection<')
html = html.replace('>share collection<', '>partager une collection<')
html = html.replace('>Chat<', '>Chat<')
html = html.replace('>Start chat<', '>Démarrer le chat<')
html = html.replace('>chat with text<', '>chat avec texte<')
html = html.replace('>chat with image<', '>chat avec image<')
html = html.replace('>chat with collectins<', '>chat avec collections<')
html = html.replace('>chat with web<', '>chat avec web<')
html = html.replace('>Tools<', '>Outils<')
html = html.replace('>core capabilities<', '>capacités principales<')
html = html.replace('>Image generation<', '>génération d\'images<')
html = html.replace('>analayzing data<', '>analyse de données<')
html = html.replace('>FAQ<', '>FAQ<')
html = html.replace('>Examples and use cases<', '>Exemples et cas d\'utilisation<')
html = html.replace('>Technical Recommendations<', '>Recommandations techniques<')

# Main headings
html = html.replace('>Beewant Account Management<', '>Gestion des comptes Beewant<')
html = html.replace('>Agents: Expertise at Scale<', '>Agents : Expertise à grande échelle<')
html = html.replace('>Library &amp; Collections: Knowledge at Your Fingertips<', '>Bibliothèque et Collections : Le savoir à portée de main<')
html = html.replace('>Chat: Intelligent Conversation Engine<', '>Chat : Moteur de conversation intelligent<')
html = html.replace('>Tools: The Engine Behind Every Output<', '>Outils : Le moteur derrière chaque résultat<')

# Video tab buttons
html = html.replace('>Creating an Account<', '>Créer un compte<')
html = html.replace('>Profile Settings<', '>Paramètres du profil<')
html = html.replace('>Security Setup<', '>Configuration de sécurité<')
html = html.replace('>Creating Your First Agent<', '>Créer votre premier agent<')
html = html.replace('>Configuring Agent Settings<', '>Configurer les paramètres<')
html = html.replace('>Agent Best Practices<', '>Meilleures pratiques<')

# Callout labels
html = html.replace('<strong>TIP:</strong>', '<strong>CONSEIL :</strong>')
html = html.replace('<strong>NOTE:</strong>', '<strong>REMARQUE :</strong>')
html = html.replace('<strong>WARNING:</strong>', '<strong>AVERTISSEMENT :</strong>')
html = html.replace('<strong>BEST PRACTICE:</strong>', '<strong>MEILLEURE PRATIQUE :</strong>')
html = html.replace('<strong>SECURITY RECOMMENDATION:</strong>', '<strong>RECOMMANDATION DE SÉCURITÉ :</strong>')

# Navigation buttons
html = html.replace('>Previous<', '>Précédent<')
html = html.replace('>Next<', '>Suivant<')

# Copy button
html = html.replace('>Copy<', '>Copier<')

with open('frenchdoc.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✓ frenchdoc.html updated with French navigation and UI")
