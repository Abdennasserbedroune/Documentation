#!/usr/bin/env python3
"""Generate nested/API_FR.html from nested/API EN.html.

Extended version: translates more UI labels and top-level section titles safely.
(We keep replacements targeted to avoid breaking code blocks.)

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
    repl: dict[str, str] = {
        'lang="en"': 'lang="fr"',
        '<title>Beewant Documentation</title>': '<title>Documentation API Beewant</title>',

        # Header / switchers
        '<span>API documentation</span>': '<span>Documentation API</span>',
        '>Platform documentation<': '>Documentation de la plateforme<',
        '>API\n              documentation<': '>Documentation\n              API<',

        # Search
        'placeholder="Search docs (⌘K)"': 'placeholder="Rechercher dans la documentation (⌘K)"',

        # Sidebar headings
        '>Overview<': '>Vue d\'ensemble<',
        '>indexes<': '>Index<',

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

        # Common UI
        '>Previous<': '>Précédent<',
        '>Next<': '>Suivant<',
        '>Copy<': '>Copier<',

        # Common API labels
        '>API Method<': '>Méthode API<',
        '>Query Parameters<': '>Paramètres de requête<',
        '>Query Response Schema<': '>Schéma de réponse<',
        '>Request Body<': '>Corps de requête<',
        '>Parameter<': '>Paramètre<',
        '>Description<': '>Description<',

        # Overview headings
        '<h2 id="overview">Overview</h2>': '<h2 id="overview">Vue d\'ensemble</h2>',
        '<h2 id="breaking-it-down">Breaking It Down</h2>': '<h2 id="breaking-it-down">Décomposer</h2>',
        '<h2 id="responses-and-error-handling">Responses and Error Handling</h2>': '<h2 id="responses-and-error-handling">Réponses et gestion des erreurs</h2>',
        '<h2 id="workflow-examples">Workflow Examples</h2>': '<h2 id="workflow-examples">Exemples de workflow</h2>',
        '<h2 id="prerequisites">Prerequisites</h2>': '<h2 id="prerequisites">Prérequis</h2>',
        '<h2 id="supported-content-types">Supported Content Types</h2>': '<h2 id="supported-content-types">Types de contenu pris en charge</h2>',
        '<h2 id="getting-started">Getting Started</h2>': '<h2 id="getting-started">Bien démarrer</h2>',

        # Non-literal intro paragraph
        (
            'Ready to dive into the Beewant API? With our versatile platform, you can easily extract information\n'
            '              from videos, audio files, and documents, turning your data into actionable insights. Built on REST\n'
            '              principles, our API returns responses in JSON format, making it accessible across various programming\n'
            '              languages and tools like Postman or any REST client.\n'
            '            '
        ):
        (
            "Prêt à utiliser l'API Beewant ? Notre plateforme vous permet d'extraire des informations à partir de vidéos, "
            "de fichiers audio et de documents afin de transformer vos contenus en informations exploitables. Basée sur les "
            "principes REST, l'API renvoie des réponses au format JSON et s'intègre facilement à Postman (ou à tout client REST) "
            "ainsi qu'à la plupart des langages.\n"
            "            "
        ),

        # Token reminder
        'ENSURE TO REPLACE <code>&lt;YOUR_TOKEN&gt;</code> WITH YOUR API KEY.':
            'ASSUREZ-VOUS DE REMPLACER <code>&lt;YOUR_TOKEN&gt;</code> PAR VOTRE CLÉ API.',
    }

    for a, b in repl.items():
        html = html.replace(a, b)

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
