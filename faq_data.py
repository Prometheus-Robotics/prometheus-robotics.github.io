# -*- coding: utf-8 -*-
"""English FAQ content (visible accordion + FAQPage JSON-LD) for the two master
pages. Per-language translations live in translations/<code>.py as FAQ_HOME and
FAQ_RESEARCH lists (same order). No double-quotes or & in values.

FAQ_HOME    -> industrial homepage /
FAQ_RESEARCH -> /research/
"""

FAQ_HOME = [
    ("Is the robot safe and certifiable for factory use?",
     "It is designed for CE certification under ISO 10218-1 and ISO 10218-2, the standards for industrial robots. The deployment safety configuration — guarding, speed limits, and interlocks — is defined per site during pilot preparation."),
    ("Does it integrate with our existing line?",
     "Yes. The station works alongside your existing stations and workflows — parts come to the robot, so there is no line rebuild. A simple REST API connects it to your line control."),
    ("How does the robot learn a new task?",
     "Operators teleoperate the robot through the task to record demonstrations, and vision-language-action policies such as Pi0 and ACT are trained from those demos. Autonomous operation is trained per task during the pilot."),
    ("Where is the robot made?",
     "Prometheus is designed and manufactured in the European Union, which matters for European research labs and companies that care about supply-chain provenance, support, and data sovereignty."),
]

FAQ_RESEARCH = [
    ("Which AI models does the robot support?",
     "Out of the box it supports modern vision-language-action and imitation-learning policies, including Pi0, Pi0.5, ACT, and SmolVLA. Collect teleoperation data, fine-tune on a consumer GPU, and deploy through the SDK."),
    ("What is included with the robot?",
     "Every unit ships with the full SDK and a simple REST API, a URDF model, a bundled simulator, head-mounted stereo plus wrist cameras, grippers, and direct engineering support. The teleoperation pipeline works on day one."),
    ("Can I collect teleoperation data and train policies myself?",
     "Yes. Teleoperate via VR with a Meta Quest 3S or a leader-follower controller, record demonstrations in the standard dataset format, and train ACT or fine-tune a vision-language-action model on a single consumer GPU."),
    ("What compute does the robot run on?",
     "Onboard compute is a Raspberry Pi 5 or an NVIDIA Jetson. Lightweight policies run on-device, while heavier vision-language-action models can run on a tethered workstation GPU and stream commands over the REST API."),
    ("Is the robot modular?",
     "Yes. You can swap grippers and end-effectors (2-finger, 4-finger, five-finger hands) to match your task. The base is a fixed tripod or a motorized linear axis (rail); legged locomotion is on the roadmap."),
    ("Where is the robot made?",
     "Prometheus is designed and manufactured in the European Union, which matters for European research labs and companies that care about supply-chain provenance, support, and data sovereignty."),
]
