# -*- coding: utf-8 -*-
"""Translation matrix for the Prometheus site.

Keys are the EXACT English strings as they appear in index.html (including
HTML entities like &amp; and straight quotes). Each value maps a language code
to its translation. Used by build_site.py via longest-first string replacement.

To add a language: add its code to LANGS in index.html's inline <script>, add a
column here for every key, then run `python3 build_site.py`.
"""

# Language metadata: code -> (html lang attribute, og:locale, native label)
LANG_META = {
    "de": ("de", "de_DE", "Deutsch"),
    "fr": ("fr", "fr_FR", "Français"),
}

# Per-language SEO for each tab (title, description).
SEO = {
    "de": {
        "research": (
            "Prometheus Robotics — Humanoide Plattform für Forschungslabore",
            "Ein modularer humanoider Roboter für die Robotikforschung: volles SDK, Stereo- und Handgelenkkameras, URDF, mitgelieferter Simulator und Unterstützung für VLA-Modelle wie Pi0 und ACT.",
        ),
        "manufacturing": (
            "Prometheus Robotics — Humanoide Roboter für die Fertigung",
            "Ein trainierbarer Humanoid für die Produktionshalle: Endkontrolle, Pick-and-Place und repetitive Linienaufgaben. In Minuten umrüstbar und günstiger als eine Sonderzelle.",
        ),
        "entertainment": (
            "Prometheus Robotics — Humanoide Roboter für Entertainment & Veranstaltungsorte",
            "Ein echter interaktiver Humanoid für Freizeitparks, Hotels und Events. Kostümieren, live per VR (Meta Quest 3S) steuern, Routinen aufnehmen und abspielen, Gäste begrüßen und Inhalte präsentieren.",
        ),
    },
    "fr": {
        "research": (
            "Prometheus Robotics — Plateforme humanoïde pour laboratoires de recherche",
            "Un robot humanoïde modulaire pour la recherche en robotique : SDK complet, caméras stéréo et de poignet, URDF, simulateur inclus et prise en charge des modèles VLA comme Pi0 et ACT.",
        ),
        "manufacturing": (
            "Prometheus Robotics — Robots humanoïdes pour l'industrie",
            "Un humanoïde entraînable pour l'atelier : tests en fin de ligne, pick-and-place et tâches répétitives. Reconfigurable en quelques minutes et moins cher qu'une cellule sur mesure.",
        ),
        "entertainment": (
            "Prometheus Robotics — Robots humanoïdes pour le divertissement et les lieux d'accueil",
            "Un véritable humanoïde interactif pour parcs à thème, hôtels et événements. Costumez-le, pilotez-le en VR (Meta Quest 3S), enregistrez et rejouez des routines, accueillez et présentez aux visiteurs.",
        ),
    },
}

TRANS = {
    # --- Nav / common ---
    "Contacts": {"de": "Kontakt", "fr": "Contact"},

    # --- Hero ---
    "For Research Labs &amp; Technical Universities": {
        "de": "Für Forschungslabore &amp; technische Universitäten",
        "fr": "Pour les laboratoires de recherche &amp; universités techniques",
    },
    "Humanoid Platform for Robotics Research": {
        "de": "Humanoide Plattform für die Robotikforschung",
        "fr": "Plateforme humanoïde pour la recherche en robotique",
    },
    "A modular humanoid robot purpose-built for research. Train VLA policies, collect teleoperation data, validate in simulation, deploy on hardware — everything ready out of the box.": {
        "de": "Ein modularer humanoider Roboter, eigens für die Forschung entwickelt. Trainieren Sie VLA-Policies, sammeln Sie Teleoperationsdaten, validieren Sie in der Simulation und deployen Sie auf der Hardware — alles sofort einsatzbereit.",
        "fr": "Un robot humanoïde modulaire conçu pour la recherche. Entraînez des politiques VLA, collectez des données de téléopération, validez en simulation et déployez sur le matériel — tout est prêt à l'emploi.",
    },
    "Research Labs": {"de": "Forschungslabore", "fr": "Laboratoires de recherche"},
    "Technical Universities": {"de": "Technische Universitäten", "fr": "Universités techniques"},
    "Manufacturing": {"de": "Fertigung", "fr": "Industrie"},
    "Entertainment": {"de": "Entertainment", "fr": "Divertissement"},
    "Automation Suppliers": {"de": "Automatisierungsanbieter", "fr": "Fournisseurs d'automatisation"},
    "Startups": {"de": "Start-ups", "fr": "Start-ups"},
    "DIY Developers": {"de": "DIY-Entwickler", "fr": "Développeurs DIY"},
    "Buy Humanoid Robot": {"de": "Humanoiden Roboter kaufen", "fr": "Acheter le robot humanoïde"},
    "Book Call": {"de": "Termin buchen", "fr": "Réserver un appel"},

    # --- Research panel ---
    "Built for Modern Robotics Research": {
        "de": "Gebaut für moderne Robotikforschung",
        "fr": "Conçu pour la recherche robotique moderne",
    },
    "Everything your lab needs to start collecting data, training policies, and running experiments — shipped with the robot.": {
        "de": "Alles, was Ihr Labor braucht, um Daten zu sammeln, Policies zu trainieren und Experimente durchzuführen — wird mit dem Roboter geliefert.",
        "fr": "Tout ce dont votre laboratoire a besoin pour collecter des données, entraîner des politiques et mener des expériences — livré avec le robot.",
    },
    "VLA-Optimized Vision": {"de": "VLA-optimierte Vision", "fr": "Vision optimisée pour la VLA"},
    "Wrist cameras with customizable mounting angle — ideal for Pi0.5 and other VLA models. Plus head-mounted stereo for full-scene perception.": {
        "de": "Handgelenkkameras mit anpassbarem Montagewinkel — ideal für Pi0.5 und andere VLA-Modelle. Dazu kopfmontierte Stereokameras für die Wahrnehmung der gesamten Szene.",
        "fr": "Caméras de poignet à angle de montage réglable — idéales pour Pi0.5 et d'autres modèles VLA. Plus une stéréo montée sur la tête pour percevoir toute la scène.",
    },
    "Ready to be Trained": {"de": "Bereit zum Trainieren", "fr": "Prêt à être entraîné"},
    "Pre-configured for modern ML pipelines. Start collecting demonstrations and training policies on day one — no integration work required.": {
        "de": "Vorkonfiguriert für moderne ML-Pipelines. Sammeln Sie ab dem ersten Tag Demonstrationen und trainieren Sie Policies — ganz ohne Integrationsaufwand.",
        "fr": "Préconfiguré pour les pipelines de ML modernes. Collectez des démonstrations et entraînez des politiques dès le premier jour — sans aucun travail d'intégration.",
    },
    "Teleoperation Pipeline": {"de": "Teleoperations-Pipeline", "fr": "Pipeline de téléopération"},
    "Tele-op support out of the box for demonstration recording and remote control. Plug into your imitation learning workflow immediately.": {
        "de": "Teleoperation ab Werk für die Aufzeichnung von Demonstrationen und die Fernsteuerung. Sofort in Ihren Imitation-Learning-Workflow integrierbar.",
        "fr": "Téléopération prête à l'emploi pour l'enregistrement de démonstrations et le contrôle à distance. Intégrez-la immédiatement à votre workflow d'apprentissage par imitation.",
    },
    "URDF for Simulators": {"de": "URDF für Simulatoren", "fr": "URDF pour simulateurs"},
    "Full URDF robot model included. Drop-in compatibility with MuJoCo, Isaac Sim, PyBullet, Gazebo, and the rest of the standard sim stack.": {
        "de": "Vollständiges URDF-Robotermodell inklusive. Sofort kompatibel mit MuJoCo, Isaac Sim, PyBullet, Gazebo und dem übrigen Standard-Simulationsstack.",
        "fr": "Modèle de robot URDF complet inclus. Compatibilité immédiate avec MuJoCo, Isaac Sim, PyBullet, Gazebo et le reste de la pile de simulation standard.",
    },
    "Simulator Bundled": {"de": "Simulator inklusive", "fr": "Simulateur inclus"},
    "Simulator ships with every robot. Develop and validate in sim before touching hardware.": {
        "de": "Jeder Roboter wird mit Simulator geliefert. Entwickeln und validieren Sie in der Simulation, bevor Sie die Hardware anfassen.",
        "fr": "Le simulateur est livré avec chaque robot. Développez et validez en simulation avant de toucher au matériel.",
    },
    "Complete SDK for control, perception, and integration. Python-first and well-documented.": {
        "de": "Vollständiges SDK für Steuerung, Wahrnehmung und Integration. Python-first und gut dokumentiert.",
        "fr": "SDK complet pour le contrôle, la perception et l'intégration. Orienté Python et bien documenté.",
    },
    "Grippers Included": {"de": "Greifer inklusive", "fr": "Préhenseurs inclus"},
    "Manipulators ship with the platform. No need to source end-effectors separately.": {
        "de": "Manipulatoren werden mit der Plattform geliefert. Endeffektoren müssen nicht separat beschafft werden.",
        "fr": "Les manipulateurs sont fournis avec la plateforme. Inutile de vous procurer les effecteurs séparément.",
    },
    "Modular Hardware": {"de": "Modulare Hardware", "fr": "Matériel modulaire"},
    "Swap arms, grippers, and base modules. Adapt the platform to your research, not the other way around.": {
        "de": "Tauschen Sie Arme, Greifer und Basismodule aus. Passen Sie die Plattform an Ihre Forschung an — nicht umgekehrt.",
        "fr": "Changez les bras, les préhenseurs et les modules de base. Adaptez la plateforme à votre recherche, et non l'inverse.",
    },
    "Sample Scenarios": {"de": "Beispielszenarien", "fr": "Scénarios d'exemple"},
    "Pre-recorded movements and example execution scenarios. Validate the stack on your bench in minutes.": {
        "de": "Vorab aufgezeichnete Bewegungen und beispielhafte Ausführungsszenarien. Validieren Sie den Stack in Minuten auf Ihrem Prüfstand.",
        "fr": "Mouvements préenregistrés et scénarios d'exécution d'exemple. Validez la pile sur votre banc en quelques minutes.",
    },
    "Detailed Documentation": {"de": "Ausführliche Dokumentation", "fr": "Documentation détaillée"},
    "Comprehensive docs for hardware, software, calibration, and integration workflows.": {
        "de": "Umfassende Dokumentation für Hardware, Software, Kalibrierung und Integrations-Workflows.",
        "fr": "Documentation complète pour le matériel, le logiciel, l'étalonnage et les workflows d'intégration.",
    },
    "Direct Engineering Support": {"de": "Direkter Engineering-Support", "fr": "Support ingénierie direct"},
    "Direct line to our team — from unboxing through deployment, experiments, and publication.": {
        "de": "Direkter Draht zu unserem Team — vom Auspacken über das Deployment und die Experimente bis zur Veröffentlichung.",
        "fr": "Ligne directe avec notre équipe — du déballage au déploiement, aux expériences et à la publication.",
    },
    "Why labs choose Prometheus": {
        "de": "Warum Labore sich für Prometheus entscheiden",
        "fr": "Pourquoi les laboratoires choisissent Prometheus",
    },
    "There's no off-the-shelf humanoid built for research. Teams burn months gluing together hardware, cameras, sim, and ML tooling before they can run a single experiment. Prometheus ships that whole stack ready to go.": {
        "de": "Es gibt keinen humanoiden Roboter von der Stange, der für die Forschung gebaut ist. Teams verbringen Monate damit, Hardware, Kameras, Simulation und ML-Tools zusammenzufügen, bevor sie ein einziges Experiment durchführen können. Prometheus liefert diesen gesamten Stack einsatzbereit.",
        "fr": "Il n'existe pas d'humanoïde clé en main conçu pour la recherche. Les équipes passent des mois à assembler matériel, caméras, simulation et outils de ML avant de pouvoir lancer une seule expérience. Prometheus livre toute cette pile prête à l'emploi.",
    },
    "Research-first, not a demo unit": {
        "de": "Forschung zuerst, kein Demo-Gerät",
        "fr": "La recherche d'abord, pas une unité de démo",
    },
    "Open architecture, full SDK, URDF, and bundled simulator — designed around how robotics research actually works.": {
        "de": "Offene Architektur, vollständiges SDK, URDF und mitgelieferter Simulator — ausgelegt darauf, wie Robotikforschung wirklich funktioniert.",
        "fr": "Architecture ouverte, SDK complet, URDF et simulateur inclus — pensés pour la façon dont la recherche en robotique fonctionne réellement.",
    },
    "Skip months of integration": {"de": "Sparen Sie Monate an Integration", "fr": "Évitez des mois d'intégration"},
    "Cameras, teleop, and ML pipelines are pre-configured. Start collecting demonstrations and training policies on day one.": {
        "de": "Kameras, Teleoperation und ML-Pipelines sind vorkonfiguriert. Sammeln Sie ab dem ersten Tag Demonstrationen und trainieren Sie Policies.",
        "fr": "Les caméras, la téléopération et les pipelines de ML sont préconfigurés. Collectez des démonstrations et entraînez des politiques dès le premier jour.",
    },
    "Hackable &amp; modular": {"de": "Hackbar &amp; modular", "fr": "Modifiable &amp; modulaire"},
    "Swap arms, grippers, and base modules, write your own controllers, extend the SDK. Adapt the platform to your work.": {
        "de": "Tauschen Sie Arme, Greifer und Basismodule aus, schreiben Sie eigene Controller und erweitern Sie das SDK. Passen Sie die Plattform an Ihre Arbeit an.",
        "fr": "Changez les bras, préhenseurs et modules de base, écrivez vos propres contrôleurs, étendez le SDK. Adaptez la plateforme à votre travail.",
    },
    "Custom builds": {"de": "Individuelle Konfigurationen", "fr": "Configurations sur mesure"},
    "Bespoke sensor packages, alternative grippers, custom kinematics, and software integrations for specialized lab work.": {
        "de": "Maßgeschneiderte Sensorpakete, alternative Greifer, individuelle Kinematik und Software-Integrationen für spezialisierte Laborarbeit.",
        "fr": "Ensembles de capteurs sur mesure, préhenseurs alternatifs, cinématiques personnalisées et intégrations logicielles pour des travaux de laboratoire spécialisés.",
    },

    # --- Manufacturing panel ---
    "Put a Humanoid on Your Line": {
        "de": "Stellen Sie einen Humanoiden an Ihre Linie",
        "fr": "Mettez un humanoïde sur votre ligne",
    },
    "End-of-line testing, pick-and-place, and the repetitive line tasks you'd rather not staff — handled by a flexible humanoid that redeploys in minutes.": {
        "de": "Endkontrolle, Pick-and-Place und die repetitiven Linienaufgaben, die Sie ungern besetzen — übernommen von einem flexiblen Humanoiden, der sich in Minuten umrüsten lässt.",
        "fr": "Tests en fin de ligne, pick-and-place et les tâches répétitives que vous préféreriez ne pas pourvoir — pris en charge par un humanoïde flexible qui se redéploie en quelques minutes.",
    },
    "End-of-Line Testing": {"de": "Endkontrolle", "fr": "Tests en fin de ligne"},
    "Run functional and quality checks at the end of your production line — consistent, repeatable, and tireless across every shift.": {
        "de": "Führen Sie Funktions- und Qualitätsprüfungen am Ende Ihrer Produktionslinie durch — konstant, wiederholbar und unermüdlich in jeder Schicht.",
        "fr": "Effectuez des contrôles fonctionnels et qualité en fin de ligne de production — constants, reproductibles et infatigables à chaque équipe.",
    },
    "Pick &amp; Place": {"de": "Pick &amp; Place", "fr": "Pick &amp; Place"},
    "Reliable pick-and-place for parts, packaging, and kitting. Handle varied objects with the included grippers.": {
        "de": "Zuverlässiges Pick-and-Place für Teile, Verpackung und Kommissionierung. Handhaben Sie unterschiedliche Objekte mit den mitgelieferten Greifern.",
        "fr": "Pick-and-place fiable pour les pièces, l'emballage et le kitting. Manipulez des objets variés avec les préhenseurs inclus.",
    },
    "Repetitive Line Tasks": {"de": "Repetitive Linienaufgaben", "fr": "Tâches répétitives de ligne"},
    "Take over the dull, repetitive jobs — machine tending, sorting, assembly support — and free your people for higher-value work.": {
        "de": "Übernehmen Sie die eintönigen, repetitiven Aufgaben — Maschinenbedienung, Sortieren, Montageunterstützung — und machen Sie Ihre Mitarbeiter für höherwertige Arbeit frei.",
        "fr": "Confiez-lui les tâches monotones et répétitives — alimentation de machines, tri, aide à l'assemblage — et libérez vos équipes pour des tâches à plus forte valeur.",
    },
    "Learns the Task": {"de": "Lernt die Aufgabe", "fr": "Apprend la tâche"},
    "Powered by Pi0 — an easily trainable VLA model. Show it the task and it generalizes, adapting to variation instead of breaking on it. No rigid scripting.": {
        "de": "Angetrieben von Pi0 — einem leicht trainierbaren VLA-Modell. Zeigen Sie ihm die Aufgabe, und es generalisiert: Es passt sich Abweichungen an, statt an ihnen zu scheitern. Keine starre Programmierung.",
        "fr": "Propulsé par Pi0 — un modèle VLA facile à entraîner. Montrez-lui la tâche et il généralise, s'adaptant aux variations au lieu de s'y casser. Aucun script rigide.",
    },
    "Fast Changeover": {"de": "Schnelle Umrüstung", "fr": "Changement rapide"},
    "Reconfigure for a new task or product changeover in minutes, not weeks. One robot, many jobs.": {
        "de": "Rüsten Sie für eine neue Aufgabe oder einen Produktwechsel in Minuten um, nicht in Wochen. Ein Roboter, viele Aufgaben.",
        "fr": "Reconfigurez pour une nouvelle tâche ou un changement de produit en quelques minutes, pas en semaines. Un robot, de multiples tâches.",
    },
    "Vision-Guided": {"de": "Bildgeführt", "fr": "Guidé par la vision"},
    "Stereo and wrist cameras for part detection, alignment, and visual inspection right where the work happens.": {
        "de": "Stereo- und Handgelenkkameras für Teileerkennung, Ausrichtung und Sichtprüfung direkt am Ort des Geschehens.",
        "fr": "Caméras stéréo et de poignet pour la détection des pièces, l'alignement et l'inspection visuelle là où le travail se fait.",
    },
    "Modular Grippers": {"de": "Modulare Greifer", "fr": "Préhenseurs modulaires"},
    "Swap end-effectors to match the part. Manipulators ship with the platform, ready for your line.": {
        "de": "Tauschen Sie Endeffektoren passend zum Teil. Manipulatoren werden mit der Plattform geliefert, bereit für Ihre Linie.",
        "fr": "Changez d'effecteur selon la pièce. Les manipulateurs sont livrés avec la plateforme, prêts pour votre ligne.",
    },
    "Easy Integration": {"de": "Einfache Integration", "fr": "Intégration facile"},
    "A simple REST API plugs into your existing line control and workflows — no proprietary lock-in.": {
        "de": "Eine einfache REST-API lässt sich in Ihre bestehende Liniensteuerung und Workflows einbinden — ohne proprietäre Bindung.",
        "fr": "Une simple API REST s'intègre à votre contrôle de ligne et vos workflows existants — sans verrouillage propriétaire.",
    },
    "Why manufacturers choose Prometheus": {
        "de": "Warum Hersteller sich für Prometheus entscheiden",
        "fr": "Pourquoi les industriels choisissent Prometheus",
    },
    "The dull, repetitive line jobs are the hardest to staff and keep staffed — but task-specific robots force you to rebuild the line around them. Prometheus integrates seamlessly into your existing process instead, works three shifts a day, and never calls in sick.": {
        "de": "Die eintönigen, repetitiven Linienjobs sind am schwersten zu besetzen und besetzt zu halten — doch aufgabenspezifische Roboter zwingen Sie, die Linie um sie herum umzubauen. Prometheus fügt sich stattdessen nahtlos in Ihren bestehenden Prozess ein, arbeitet drei Schichten am Tag und meldet sich nie krank.",
        "fr": "Les postes monotones et répétitifs de la ligne sont les plus difficiles à pourvoir et à maintenir — mais les robots dédiés à une tâche vous obligent à reconstruire la ligne autour d'eux. Prometheus s'intègre au contraire en douceur dans votre processus existant, travaille trois équipes par jour et ne tombe jamais malade.",
    },
    "Fills hard-to-staff jobs": {"de": "Besetzt schwer zu besetzende Stellen", "fr": "Comble les postes difficiles à pourvoir"},
    "Cover the repetitive, high-turnover tasks people don't want — without scaling headcount or fighting churn.": {
        "de": "Decken Sie die repetitiven Aufgaben mit hoher Fluktuation ab, die niemand will — ohne Personal aufzustocken oder gegen Fluktuation zu kämpfen.",
        "fr": "Couvrez les tâches répétitives à fort turnover dont personne ne veut — sans augmenter les effectifs ni lutter contre le roulement.",
    },
    "Cheaper than a custom cell": {"de": "Günstiger als eine Sonderzelle", "fr": "Moins cher qu'une cellule sur mesure"},
    "One flexible humanoid replaces bespoke fixed automation that's costly to design, build, and maintain.": {
        "de": "Ein flexibler Humanoid ersetzt maßgeschneiderte feste Automatisierung, die teuer in Entwurf, Bau und Wartung ist.",
        "fr": "Un humanoïde flexible remplace une automatisation fixe sur mesure, coûteuse à concevoir, construire et entretenir.",
    },
    "Reconfigures in minutes": {"de": "Umkonfiguration in Minuten", "fr": "Se reconfigure en quelques minutes"},
    "A new product or task no longer means weeks of re-tooling. Retrain and repurpose the same robot across the line.": {
        "de": "Ein neues Produkt oder eine neue Aufgabe bedeutet nicht mehr wochenlange Umrüstung. Trainieren Sie denselben Roboter neu und setzen Sie ihn an der Linie anders ein.",
        "fr": "Un nouveau produit ou une nouvelle tâche ne signifie plus des semaines de réoutillage. Réentraînez et réaffectez le même robot sur la ligne.",
    },
    "Scales with demand": {"de": "Skaliert mit der Nachfrage", "fr": "Évolue avec la demande"},
    "Add units as volume grows and move them to the bottleneck. No fixed infrastructure to rip out and rebuild.": {
        "de": "Fügen Sie bei wachsendem Volumen Einheiten hinzu und versetzen Sie sie zum Engpass. Keine feste Infrastruktur, die herausgerissen und neu gebaut werden muss.",
        "fr": "Ajoutez des unités à mesure que le volume augmente et déplacez-les vers le goulet d'étranglement. Aucune infrastructure fixe à arracher et reconstruire.",
    },

    # --- Entertainment panel ---
    "A Humanoid That Steals the Show": {
        "de": "Ein Humanoid, der die Show stiehlt",
        "fr": "Un humanoïde qui vole la vedette",
    },
    "For theme parks, hotels, museums, and events — dress it up, drive it from VR, replay routines, and let it greet, present, and explain.": {
        "de": "Für Freizeitparks, Hotels, Museen und Events — kostümieren Sie ihn, steuern Sie ihn per VR, spielen Sie Routinen ab und lassen Sie ihn begrüßen, präsentieren und erklären.",
        "fr": "Pour les parcs à thème, hôtels, musées et événements — costumez-le, pilotez-le en VR, rejouez des routines et laissez-le accueillir, présenter et expliquer.",
    },
    "Dress It Up": {"de": "Kostümieren Sie ihn", "fr": "Costumez-le"},
    "Outfit the robot in custom costumes and branded clothing to match your venue, mascot, or event theme.": {
        "de": "Statten Sie den Roboter mit individuellen Kostümen und Markenkleidung aus, passend zu Ihrem Veranstaltungsort, Maskottchen oder Event-Thema.",
        "fr": "Habillez le robot de costumes personnalisés et de tenues à votre image pour s'accorder à votre lieu, votre mascotte ou le thème de l'événement.",
    },
    "VR Teleoperation": {"de": "VR-Teleoperation", "fr": "Téléopération en VR"},
    "Operate the robot live from VR with a Meta Quest 3S — wave, gesture, and interact with guests in real time.": {
        "de": "Steuern Sie den Roboter live per VR mit einer Meta Quest 3S — winken, gestikulieren und interagieren Sie in Echtzeit mit den Gästen.",
        "fr": "Pilotez le robot en direct en VR avec un Meta Quest 3S — saluez, gesticulez et interagissez avec les visiteurs en temps réel.",
    },
    "Record &amp; Replay": {"de": "Aufnehmen &amp; Abspielen", "fr": "Enregistrer &amp; rejouer"},
    "Capture a performance once and replay it on demand — greetings, dances, and scripted routines, show after show.": {
        "de": "Nehmen Sie eine Darbietung einmal auf und spielen Sie sie auf Abruf ab — Begrüßungen, Tänze und einstudierte Routinen, Show für Show.",
        "fr": "Capturez une performance une fois et rejouez-la à la demande — salutations, danses et routines scénarisées, spectacle après spectacle.",
    },
    "Present &amp; Explain": {"de": "Präsentieren &amp; Erklären", "fr": "Présenter &amp; expliquer"},
    "Have it host and explain — guided tours, product demos, and exhibits that talk visitors through the experience.": {
        "de": "Lassen Sie ihn moderieren und erklären — Führungen, Produktdemos und Ausstellungen, die Besucher durch das Erlebnis führen.",
        "fr": "Faites-en un animateur qui explique — visites guidées, démos produits et expositions qui guident les visiteurs tout au long de l'expérience.",
    },
    "Greet Guests": {"de": "Gäste begrüßen", "fr": "Accueillir les visiteurs"},
    "A friendly humanoid welcome for park entrances, hotel lobbies, and show floors.": {
        "de": "Ein freundlicher humanoider Empfang für Parkeingänge, Hotellobbys und Messeflächen.",
        "fr": "Un accueil humanoïde chaleureux pour les entrées de parc, les halls d'hôtel et les espaces d'exposition.",
    },
    "Remote Operation": {"de": "Fernsteuerung", "fr": "Pilotage à distance"},
    "Drive it remotely from anywhere — run interactions and performances without staff on the floor.": {
        "de": "Steuern Sie ihn von überall aus fern — Interaktionen und Darbietungen ganz ohne Personal vor Ort.",
        "fr": "Pilotez-le à distance depuis n'importe où — assurez interactions et performances sans personnel sur place.",
    },
    "Built for Venues": {"de": "Für Veranstaltungsorte gemacht", "fr": "Conçu pour les lieux d'accueil"},
    "Theme parks, hotels, museums, and events — a head-turning attraction that keeps crowds engaged.": {
        "de": "Freizeitparks, Hotels, Museen und Events — eine Attraktion, die alle Blicke auf sich zieht und das Publikum fesselt.",
        "fr": "Parcs à thème, hôtels, musées et événements — une attraction qui ne passe pas inaperçue et captive le public.",
    },
    "Always On Brand": {"de": "Immer markenkonform", "fr": "Toujours fidèle à votre marque"},
    "Consistent, repeatable performances every time — your signature character, delivered reliably.": {
        "de": "Konsistente, wiederholbare Darbietungen jedes Mal — Ihr unverwechselbarer Charakter, zuverlässig geliefert.",
        "fr": "Des performances constantes et reproductibles à chaque fois — votre personnage emblématique, livré de façon fiable.",
    },
    "Why venues choose Prometheus": {
        "de": "Warum Veranstaltungsorte sich für Prometheus entscheiden",
        "fr": "Pourquoi les lieux d'accueil choisissent Prometheus",
    },
    "Attractions live or die on the wow factor. Guests have seen screens and animatronics — a real, interactive humanoid is what they photograph, post, and come back for. It's a statement that your venue is the most advanced one out there.": {
        "de": "Attraktionen stehen und fallen mit dem Wow-Faktor. Bildschirme und Animatronics haben Gäste schon gesehen — ein echter, interaktiver Humanoid ist das, was sie fotografieren, posten und weshalb sie wiederkommen. Es ist ein Statement, dass Ihr Veranstaltungsort der fortschrittlichste ist.",
        "fr": "Une attraction vit ou meurt par son effet « waouh ». Les visiteurs ont déjà vu des écrans et des animatroniques — un véritable humanoïde interactif est ce qu'ils photographient, partagent et pour quoi ils reviennent. C'est une affirmation : votre lieu est le plus avancé du marché.",
    },
    "A crowd magnet": {"de": "Ein Publikumsmagnet", "fr": "Un aimant à foule"},
    "A real humanoid pulls crowds, photos, and social buzz that a screen or animatronic simply can't match.": {
        "de": "Ein echter Humanoid zieht Menschenmengen, Fotos und Social-Media-Aufmerksamkeit an, mit denen ein Bildschirm oder Animatronic einfach nicht mithalten kann.",
        "fr": "Un véritable humanoïde attire les foules, les photos et le buzz sur les réseaux qu'un écran ou un animatronique ne peut tout simplement pas égaler.",
    },
    "Instant prestige": {"de": "Sofortiges Prestige", "fr": "Un prestige immédiat"},
    "Show everyone you run the most advanced, future-facing venue in the market — and make sure they all see it.": {
        "de": "Zeigen Sie allen, dass Sie den fortschrittlichsten, zukunftsorientiertesten Veranstaltungsort am Markt betreiben — und sorgen Sie dafür, dass es alle sehen.",
        "fr": "Montrez à tous que vous gérez le lieu le plus avancé et tourné vers l'avenir du marché — et faites en sorte que tout le monde le voie.",
    },
    "One performer, every show": {"de": "Ein Darsteller, jede Show", "fr": "Un seul artiste, à chaque spectacle"},
    "Record routines once and replay them flawlessly all day — no breaks, no scheduling, no staffing the role.": {
        "de": "Nehmen Sie Routinen einmal auf und spielen Sie sie den ganzen Tag fehlerfrei ab — keine Pausen, keine Dienstplanung, keine Besetzung der Rolle.",
        "fr": "Enregistrez les routines une fois et rejouez-les sans faute toute la journée — pas de pauses, pas de planning, pas de poste à pourvoir.",
    },
    "Operate from anywhere": {"de": "Von überall steuern", "fr": "Pilotez depuis n'importe où"},
    "Drive it live in VR with a Meta Quest 3S to greet and interact with guests in real time — even remotely.": {
        "de": "Steuern Sie ihn live in VR mit einer Meta Quest 3S, um Gäste in Echtzeit zu begrüßen und mit ihnen zu interagieren — auch aus der Ferne.",
        "fr": "Pilotez-le en direct en VR avec un Meta Quest 3S pour accueillir les visiteurs et interagir avec eux en temps réel — même à distance.",
    },

    # --- Specifications ---
    "Technical Specifications": {"de": "Technische Daten", "fr": "Spécifications techniques"},
    "Upper Body on tripod — suitable for bench-top research": {
        "de": "Oberkörper auf Stativ — geeignet für Tischforschung",
        "fr": "Buste sur trépied — adapté à la recherche en laboratoire",
    },
    "Maximum Joint Torque": {"de": "Maximales Gelenkdrehmoment", "fr": "Couple articulaire maximal"},
    "Height": {"de": "Höhe", "fr": "Hauteur"},
    "Width": {"de": "Breite", "fr": "Largeur"},
    "Battery Life": {"de": "Akkulaufzeit", "fr": "Autonomie de la batterie"},
    "Degrees of Freedom": {"de": "Freiheitsgrade", "fr": "Degrés de liberté"},
    "Cameras": {"de": "Kameras", "fr": "Caméras"},
    "Microphones": {"de": "Mikrofone", "fr": "Microphones"},
    "Speaker on the mouth level": {"de": "Lautsprecher auf Mundhöhe", "fr": "Haut-parleur au niveau de la bouche"},
    "Speaker": {"de": "Lautsprecher", "fr": "Haut-parleur"},
    "Power Supply": {"de": "Stromversorgung", "fr": "Alimentation"},
    "Charger": {"de": "Ladegerät", "fr": "Chargeur"},
    "Compute": {"de": "Recheneinheit", "fr": "Unité de calcul"},
    "Robot Model": {"de": "Robotermodell", "fr": "Modèle de robot"},
    "Software": {"de": "Software", "fr": "Logiciel"},
    "Manual Controller": {"de": "Manueller Controller", "fr": "Manette manuelle"},
    "About 4h": {"de": "Etwa 4 Std.", "fr": "Environ 4 h"},
    "Optional": {"de": "Optional", "fr": "En option"},
    "Available Modules": {"de": "Verfügbare Module", "fr": "Modules disponibles"},
    "Legs Module": {"de": "Beinmodul", "fr": "Module jambes"},
    "Bipedal locomotion system for enhanced mobility and human-like movement capabilities.": {
        "de": "Zweibeiniges Fortbewegungssystem für mehr Mobilität und menschenähnliche Bewegungsfähigkeiten.",
        "fr": "Système de locomotion bipède pour une mobilité accrue et des mouvements proches de l'humain.",
    },
    "Wheels Module": {"de": "Radmodul", "fr": "Module roues"},
    "Wheeled base for efficient navigation and stable platform for various applications.": {
        "de": "Fahrbare Basis für effiziente Navigation und eine stabile Plattform für verschiedenste Anwendungen.",
        "fr": "Base à roues pour une navigation efficace et une plateforme stable pour diverses applications.",
    },
    "Contact Sales": {"de": "Vertrieb kontaktieren", "fr": "Contacter les ventes"},

    # --- Manipulators ---
    "Manipulator Options": {"de": "Greifer-Optionen", "fr": "Options de manipulateur"},
    "Choose the right end-effector for your research": {
        "de": "Wählen Sie den passenden Endeffektor für Ihre Forschung",
        "fr": "Choisissez l'effecteur adapté à votre recherche",
    },
    "2-finger gripper": {"de": "2-Finger-Greifer", "fr": "Préhenseur à 2 doigts"},
    "Simple pinch / precise closing. Ideal for delicate operations and precise manipulation tasks.": {
        "de": "Einfaches Greifen / präzises Schließen. Ideal für empfindliche Vorgänge und präzise Manipulationsaufgaben.",
        "fr": "Pince simple / fermeture précise. Idéal pour les opérations délicates et les tâches de manipulation de précision.",
    },
    '4-finger "claw" (paired fingers)': {
        "de": "4-Finger-„Klaue“ (gepaarte Finger)",
        "fr": "« griffe » à 4 doigts (doigts appariés)",
    },
    "For robust gripping of crates and tote boxes. Designed for warehouse and logistics applications.": {
        "de": "Für robustes Greifen von Kisten und Transportboxen. Konzipiert für Lager- und Logistikanwendungen.",
        "fr": "Pour une préhension robuste de caisses et de bacs. Conçu pour les applications d'entrepôt et de logistique.",
    },
    "Advanced manipulators": {"de": "Fortschrittliche Manipulatoren", "fr": "Manipulateurs avancés"},
    "Options include wrist cameras with customizable mounting angle (optimized for Pi0.5 and other VLA models), 5-finger hands, and other custom variants.": {
        "de": "Zu den Optionen zählen Handgelenkkameras mit anpassbarem Montagewinkel (optimiert für Pi0.5 und andere VLA-Modelle), Fünf-Finger-Hände und weitere individuelle Varianten.",
        "fr": "Les options incluent des caméras de poignet à angle de montage réglable (optimisées pour Pi0.5 et d'autres modèles VLA), des mains à 5 doigts et d'autres variantes personnalisées.",
    },

    # --- Bottom CTA ---
    "Ready to Put Prometheus to Work?": {
        "de": "Bereit, Prometheus an die Arbeit zu schicken?",
        "fr": "Prêt à mettre Prometheus au travail ?",
    },
    "Whether it's a research lab, a production line, or a venue floor — order a unit or book a call to discuss your configuration.": {
        "de": "Ob Forschungslabor, Produktionslinie oder Veranstaltungsfläche — bestellen Sie eine Einheit oder buchen Sie ein Gespräch, um Ihre Konfiguration zu besprechen.",
        "fr": "Que ce soit un laboratoire de recherche, une ligne de production ou un espace d'accueil — commandez une unité ou réservez un appel pour discuter de votre configuration.",
    },
    "Buy Modular Platform": {"de": "Modulare Plattform kaufen", "fr": "Acheter la plateforme modulaire"},

    # --- Footer ---
    "A modular humanoid platform for research, industry, and entertainment. Built for the labs, factory floors, and venues shaping the next generation of intelligent robots.": {
        "de": "Eine modulare humanoide Plattform für Forschung, Industrie und Entertainment. Gebaut für die Labore, Fertigungshallen und Veranstaltungsorte, die die nächste Generation intelligenter Roboter prägen.",
        "fr": "Une plateforme humanoïde modulaire pour la recherche, l'industrie et le divertissement. Conçue pour les laboratoires, les ateliers de production et les lieux d'accueil qui façonnent la prochaine génération de robots intelligents.",
    },
    "Navigation": {"de": "Navigation", "fr": "Navigation"},
    "Get Started": {"de": "Loslegen", "fr": "Commencer"},
    "Home": {"de": "Startseite", "fr": "Accueil"},
    "Buy Robot": {"de": "Roboter kaufen", "fr": "Acheter un robot"},
    "All rights reserved.": {"de": "Alle Rechte vorbehalten.", "fr": "Tous droits réservés."},

    # --- Contacts page ---
    "Company Information": {"de": "Unternehmensinformationen", "fr": "Informations sur l'entreprise"},
    "Click to reveal": {"de": "Zum Anzeigen klicken", "fr": "Cliquez pour afficher"},
    "Email:": {"de": "E-Mail:", "fr": "E-mail :"},
    "Phone:": {"de": "Telefon:", "fr": "Téléphone :"},

    # --- Misc ---
    "Our LinkedIn": {"de": "Unser LinkedIn", "fr": "Notre LinkedIn"},
    "Verify you're human": {"de": "Bestätigen Sie, dass Sie ein Mensch sind", "fr": "Vérifiez que vous êtes humain"},
}
