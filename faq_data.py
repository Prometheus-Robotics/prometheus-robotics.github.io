# -*- coding: utf-8 -*-
"""FAQ content for the landing page (visible accordion + FAQPage JSON-LD).

FAQ holds the English (question, answer) pairs — these EXACT strings must also
appear in the visible .faq accordion in index.html so build_site can localize
both the visible text and the schema together.

FAQ_T maps a language code to its translated (question, answer) pairs, in the
SAME ORDER as FAQ. Missing languages fall back to English. Keep answers free of
double quotes and the '&' character (they go into both HTML and JSON-LD).

Add a language: add a FAQ_T entry with all pairs, then run build_site.py.
"""

FAQ = [
    ("Which AI models does the robot support?",
     "Out of the box it supports modern vision-language-action and imitation-learning policies, including Pi0, Pi0.5, ACT, and SmolVLA. Collect teleoperation data, fine-tune on a consumer GPU, and deploy through the SDK."),
    ("What is included with the robot?",
     "Every unit ships with the full SDK and a simple REST API, a URDF model, a bundled simulator, head-mounted stereo plus wrist cameras, grippers, and direct engineering support. The teleoperation pipeline works on day one."),
    ("Can I collect teleoperation data and train policies myself?",
     "Yes. Teleoperate via VR with a Meta Quest 3S or a leader-follower controller, record demonstrations in the standard dataset format, and train ACT or fine-tune a vision-language-action model on a single consumer GPU."),
    ("What compute does the robot run on?",
     "Onboard compute is a Raspberry Pi 5 or an NVIDIA Jetson. Lightweight policies run on-device, while heavier vision-language-action models can run on a tethered workstation GPU and stream commands over the REST API."),
    ("Is the robot modular?",
     "Yes. You can swap arms, grippers (2-finger, 4-finger, or advanced five-finger hands), and base modules such as legs or wheels, and adapt the platform to your task rather than the other way around."),
    ("Where is the robot made?",
     "Prometheus is designed and manufactured in the European Union, which matters for European research labs and companies that care about supply-chain provenance, support, and data sovereignty."),
]

FAQ_T = {
    "de": [
        ("Welche KI-Modelle unterstützt der Roboter?",
         "Ab Werk unterstützt er moderne Vision-Language-Action- und Imitation-Learning-Policies, darunter Pi0, Pi0.5, ACT und SmolVLA. Sammeln Sie Teleoperationsdaten, feintunen Sie auf einer Consumer-GPU und deployen Sie über das SDK."),
        ("Was ist im Lieferumfang des Roboters enthalten?",
         "Jede Einheit wird mit dem vollständigen SDK und einer einfachen REST-API, einem URDF-Modell, einem mitgelieferten Simulator, kopfmontierter Stereokamera plus Handgelenkkameras, Greifern und direktem Engineering-Support geliefert. Die Teleoperation funktioniert ab dem ersten Tag."),
        ("Kann ich selbst Teleoperationsdaten sammeln und Policies trainieren?",
         "Ja. Teleoperieren Sie per VR mit einer Meta Quest 3S oder einem Leader-Follower-Controller, zeichnen Sie Demonstrationen im Standard-Datensatzformat auf und trainieren Sie ACT oder feintunen Sie ein Vision-Language-Action-Modell auf einer einzigen Consumer-GPU."),
        ("Auf welcher Recheneinheit läuft der Roboter?",
         "Die Onboard-Recheneinheit ist ein Raspberry Pi 5 oder ein NVIDIA Jetson. Leichte Policies laufen auf dem Gerät, während größere Vision-Language-Action-Modelle auf einer angebundenen Workstation-GPU laufen und Befehle über die REST-API streamen können."),
        ("Ist der Roboter modular?",
         "Ja. Sie können Arme, Greifer (2-Finger, 4-Finger oder fortschrittliche Fünf-Finger-Hände) und Basismodule wie Beine oder Räder austauschen und die Plattform an Ihre Aufgabe anpassen statt umgekehrt."),
        ("Wo wird der Roboter hergestellt?",
         "Prometheus wird in der Europäischen Union entworfen und gefertigt, was für europäische Forschungslabore und Unternehmen wichtig ist, denen Lieferketten-Herkunft, Support und Datensouveränität am Herzen liegen."),
    ],
    "fr": [
        ("Quels modèles d'IA le robot prend-il en charge ?",
         "Dès le départ, il prend en charge les politiques modernes de type vision-language-action et d'apprentissage par imitation, dont Pi0, Pi0.5, ACT et SmolVLA. Collectez des données de téléopération, affinez sur un GPU grand public et déployez via le SDK."),
        ("Qu'est-ce qui est inclus avec le robot ?",
         "Chaque unité est livrée avec le SDK complet et une API REST simple, un modèle URDF, un simulateur inclus, une stéréo montée sur la tête et des caméras de poignet, des préhenseurs et un support ingénierie direct. La téléopération fonctionne dès le premier jour."),
        ("Puis-je collecter des données de téléopération et entraîner des politiques moi-même ?",
         "Oui. Téléopérez en VR avec un Meta Quest 3S ou un contrôleur leader-suiveur, enregistrez des démonstrations au format de jeu de données standard, et entraînez ACT ou affinez un modèle vision-language-action sur un seul GPU grand public."),
        ("Sur quelle unité de calcul le robot fonctionne-t-il ?",
         "Le calcul embarqué est un Raspberry Pi 5 ou un NVIDIA Jetson. Les politiques légères s'exécutent sur l'appareil, tandis que les modèles vision-language-action plus lourds peuvent s'exécuter sur un GPU de station de travail relié et diffuser des commandes via l'API REST."),
        ("Le robot est-il modulaire ?",
         "Oui. Vous pouvez changer les bras, les préhenseurs (à 2 doigts, 4 doigts, ou mains avancées à cinq doigts) et les modules de base comme les jambes ou les roues, et adapter la plateforme à votre tâche plutôt que l'inverse."),
        ("Où le robot est-il fabriqué ?",
         "Prometheus est conçu et fabriqué dans l'Union européenne, ce qui compte pour les laboratoires de recherche et les entreprises européennes attachés à la provenance de la chaîne d'approvisionnement, au support et à la souveraineté des données."),
    ],
}
