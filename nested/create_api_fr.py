#!/usr/bin/env python3
"""Generate nested/API_FR.html from nested/API EN.html.

Goal: keep the exact same design/HTML structure/CSS/JS, and replace visible UI + documentation
text with professional French (context-aware replacements; avoid word-by-word literalism).

Usage:
  python3 nested/create_api_fr.py

Output:
  nested/API_FR.html
"""

from __future__ import annotations

from pathlib import Path

SRC = Path("nested") / "API EN.html"
DST = Path("nested") / "API_FR.html"


def apply_replacements(html: str) -> str:
    # IMPORTANT: Keep this as targeted replacements to avoid breaking code snippets.
    repl: dict[str, str] = {
        'lang="en"': 'lang="fr"',
        '<title>Beewant Documentation</title>': '<title>Documentation API Beewant</title>',

        # Header / switchers
        '<span>API documentation</span>': '<span>Documentation API</span>',
        '>Platform documentation<': '>Documentation de la plateforme<',
        '>API\n              documentation<': '>Documentation\n              API<',

        # Search placeholder
        'placeholder="Search docs (⌘K)"': 'placeholder="Rechercher dans la documentation (⌘K)"',

        # Sidebar headings
        '>Overview<': '>Vue d\'ensemble<',
        '>indexes<': '>Index<',
        '>Collections<': '>Collections<',
        '>Chat<': '>Chat<',
        '>Sources<': '>Sources<',
        '>Agents<': '>Agents<',

        # Sidebar items (overview)
        '>Breaking it down<': '>Décomposer<',
        '>Error handling<': '>Gestion des erreurs<',
        '>workflow examples<': '>Exemples de workflow<',
        '>Prerequisites<': '>Prérequis<',
        '>Supported content types<': '>Types de contenu pris en charge<',
        '>Getting started<': '>Bien démarrer<',

        # Sidebar items (indexes)
        '>create an indexes<': '>Créer un index<',
        '>list indexes<': '>Lister les index<',
        '>retrieve an index<': '>Récupérer un index<',
        '>update an index<': '>Mettre à jour un index<',
        '>Delete an index<': '>Supprimer un index<',

        # Sidebar items (collections)
        '>create a collection<': '>Créer une collection<',
        '>list collections<': '>Lister les collections<',
        '>Update collection<': '>Mettre à jour une collection<',
        '>Detelete collection<': '>Supprimer une collection<',

        # Sidebar items (chat)
        '>Transcription<': '>Transcription<',
        '>chat with text<': '>Chat avec du texte<',
        '>chat with web<': '>Chat avec le Web<',
        '>chat with tools<': '>Chat avec des outils<',
        '>chat with images<': '>Chat avec des images<',
        '>chat with index<': '>Chat avec un index<',
        '>chat with collection<': '>Chat avec une collection<',
        '>List chats<': '>Lister les conversations<',
        '>continue chat<': '>Continuer une conversation<',

        # Sidebar items (sources)
        '>New chat<': '>Nouvelle conversation<',
        '>Existing chat<': '>Conversation existante<',

        # Sidebar items (agents)
        '>create agent<': '>Créer un agent<',
        '>List agents<': '>Lister les agents<',
        '>Retrieve agent<': '>Récupérer un agent<',
        '>update agent<': '>Mettre à jour un agent<',
        '>delete agent<': '>Supprimer un agent<',

        # Common UI strings
        '>Previous<': '>Précédent<',
        '>Next<': '>Suivant<',
        '>Copy<': '>Copier<',

        # Callout labels (if present)
        '<strong>TIP:': '<strong>CONSEIL :',
        '<strong>NOTE:': '<strong>REMARQUE :',
        '<strong>WARNING:': '<strong>AVERTISSEMENT :',

        # Headings (main content)
        '<h2 id="overview">Overview</h2>': '<h2 id="overview">Vue d\'ensemble</h2>',
        '<h2 id="breaking-it-down">Breaking It Down</h2>': '<h2 id="breaking-it-down">Décomposer</h2>',
        '<h2 id="responses-and-error-handling">Responses and Error Handling</h2>': '<h2 id="responses-and-error-handling">Réponses et gestion des erreurs</h2>',
        '<h2 id="workflow-examples">Workflow Examples</h2>': '<h2 id="workflow-examples">Exemples de workflow</h2>',
        '<h2 id="prerequisites">Prerequisites</h2>': '<h2 id="prerequisites">Prérequis</h2>',
        '<h2 id="supported-content-types">Supported Content Types</h2>': '<h2 id="supported-content-types">Types de contenu pris en charge</h2>',
        '<h2 id="getting-started">Getting Started</h2>': '<h2 id="getting-started">Bien démarrer</h2>',

        # Overview paragraph (rewrite, not literal)
        (
            'Ready to dive into the Beewant API? With our versatile platform, you can easily extract information\n'
            '              from videos, audio files, and documents, turning your data into actionable insights. Built on REST\n'
            '              principles, our API returns responses in JSON format, making it accessible across various programming\n'
            '              languages and tools like Postman or any REST client.\n'
            '            '
        ):
        (
            'Prêt à utiliser l\'API Beewant ? Notre plateforme vous permet d\'extraire des informations à partir de vidéos, '
            'de fichiers audio et de documents, afin de transformer vos contenus en informations exploitables. Basée sur les '
            'principes REST, l\'API renvoie des réponses au format JSON et s\'intègre facilement à vos outils (Postman ou tout '
            'client REST) et à la plupart des langages.\n'
            '            '
        ),

        # Breaking it down bullets
        '<li><strong>Method Support:</strong> We offer several methods to interact with the API:':
            '<li><strong>Méthodes disponibles :</strong> Plusieurs méthodes sont disponibles pour interagir avec l\'API :',
        '<li><span class="method-badge method-get">GET</span>: Retrieve data.</li>':
            '<li><span class="method-badge method-get">GET</span> : Récupérer des données.</li>',
        '<li><span class="method-badge method-post">POST</span>: Create something new or trigger an action.\n                  </li>':
            '<li><span class="method-badge method-post">POST</span> : Créer une ressource ou déclencher une action.</li>',
        '<li><span class="method-badge method-patch">PATCH</span>: Update existing information.</li>':
            '<li><span class="method-badge method-patch">PATCH</span> : Mettre à jour une information existante.</li>',
        '<li><span class="method-badge method-delete">DELETE</span>: Remove something.</li>':
            '<li><span class="method-badge method-delete">DELETE</span> : Supprimer une ressource.</li>',

        '<li><strong>Base URL:</strong> Our API can be accessed at <code>https://beewant.com.com/api</code>.</li>':
            '<li><strong>URL de base :</strong> L\'API est accessible via <code>https://beewant.com.com/api</code>.</li>',

        '<li><strong>Parameters:</strong> Specify what you want to interact with (videos, audio, or documents)\n                using:':
            '<li><strong>Paramètres :</strong> Précisez la ressource ciblée (vidéos, audio ou documents) à l\'aide de :',
        '<li>Path Parameters: Point to a specific object.</li>':
            '<li>Paramètres de chemin : pointer vers un objet précis.</li>',
        '<li>Query Parameters: Additional options for filtering or sorting your responses.</li>':
            '<li>Paramètres de requête : options supplémentaires (filtrage, tri, etc.).</li>',

        '<li><strong>Authentication:</strong> Don\'t forget to include your API key in the headers to authenticate\n                your requests. </li>':
            '<li><strong>Authentification :</strong> Ajoutez votre clé API dans les en-têtes afin d\'authentifier vos requêtes.</li>',

        # Responses and error handling paragraph
        "Our API follows the RFC 9110 standard, so you'll always know if your request was successful or not.\n              Here's a breakdown of common HTTP status codes:":
        "L'API s'appuie sur les conventions HTTP (RFC 9110) : vous savez immédiatement si une requête a réussi ou non.\n              Voici les codes de statut les plus fréquents :",

        "If you encounter a 4xx error, the response will include a code and a friendly message explaining the\n              issue, which can be displayed in your app.":
        "En cas d'erreur 4xx, la réponse inclut un code et un message explicatif que vous pouvez afficher dans votre application.",

        # Workflow examples
        "This section provides an overview of common workflows for using the Beewant Multimodal AI Platform.":
        "Cette section présente des workflows courants pour utiliser la plateforme IA multimodale Beewant.",

        "When uploading content (videos, audio, or documents) to the platform, asynchronous processing is\n              required. Please wait for content processing to complete before proceeding to the next steps.":
        "Lors du téléversement (vidéos, audio ou documents), le traitement est asynchrone : attendez la fin du traitement avant de passer aux étapes suivantes.",

        # Prerequisites bullets
        "If you already have an account, go to the API Key page in your Beewant Accounts & Settings and click\n                the Copy icon next to your key.":
        "Si vous avez déjà un compte, ouvrez la page Clé API dans Beewant (Compte & Paramètres) puis cliquez sur l'icône Copier à côté de votre clé.",

        "If you don't have an account, sign up for a Beewant account, then follow the steps above to retrieve\n                your API key.":
        "Si vous n'avez pas de compte, créez-en un, puis suivez les étapes ci-dessus pour récupérer votre clé API.",

        # Supported content types
        '<li><strong>Videos:</strong> MP4 format.</li>': '<li><strong>Vidéos :</strong> format MP4.</li>',
        '<li><strong>Audio:</strong> MP3 format.</li>': '<li><strong>Audio :</strong> format MP3.</li>',
        '<li><strong>Documents:</strong> Text-based files such as PDF, TXT, JSON, and DOC.</li>':
            '<li><strong>Documents :</strong> fichiers texte (PDF, TXT, JSON, DOC, etc.).</li>',

        # Getting started list
        '<li>Select the content type(s) you wish to analyze.</li>':
            '<li>Sélectionnez le(s) type(s) de contenu à analyser.</li>',
        '<li>Upload your content using the appropriate API endpoints.</li>':
            '<li>Téléversez votre contenu via les endpoints correspondants.</li>',
        "<li>Wait for the processing to complete. A Chat button will appear when it's done.</li>":
            "<li>Attendez la fin du traitement. Un bouton Chat apparaît une fois l'opération terminée.</li>",
        '<li>Use the Chat Playground to extract insights from your processed content.</li>':
            '<li>Utilisez le Chat Playground pour extraire des informations à partir du contenu traité.</li>',

        # Footer-ish sentence
        'For further details on each step and specific workflows, refer to our comprehensive documentation.':
            'Pour plus de détails sur chaque étape et sur les workflows, consultez la documentation complète.',

        # “ENSURE TO REPLACE …” blockquote
        'ENSURE TO REPLACE <code>&lt;YOUR_TOKEN&gt;</code> WITH YOUR API KEY.':
            'ASSUREZ-VOUS DE REMPLACER <code>&lt;YOUR_TOKEN&gt;</code> PAR VOTRE CLÉ API.',

        # “Remember to replace …”
        'Remember to **replace** every <code>&lt;YOUR_TOKEN&gt;</code> with your real API key in all Python and\n              shell snippets.':
            'Pensez à **remplacer** chaque <code>&lt;YOUR_TOKEN&gt;</code> par votre clé API réelle dans tous les exemples Python et shell.',
    }

    for a, b in repl.items():
        html = html.replace(a, b)

    # Fix language switch only inside the API page header switcher.
    # Keep AR as-is; set FR as active.
    html = html.replace(
        '<a class="lang-btn is-active" href="final doc.html">EN</a>',
        '<a class="lang-btn" href="API EN.html">EN</a>',
    )
    html = html.replace(
        '<a class="lang-btn" href="frenchdoc.html">FR</a>',
        '<a class="lang-btn is-active" href="API_FR.html">FR</a>',
    )

    return html


def main() -> None:
    if not SRC.exists():
        raise SystemExit(f"Source file not found: {SRC}")

    html = SRC.read_text(encoding="utf-8")
    out = apply_replacements(html)

    DST.write_text(out, encoding="utf-8")
    print(f"✓ Created: {DST}")


if __name__ == "__main__":
    main()
