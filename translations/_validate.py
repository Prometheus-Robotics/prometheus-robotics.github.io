#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validate a translations/<code>.py file after the industrial-repositioning
update. Usage:  python3 translations/_validate.py <code>"""
import importlib.util
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

code = sys.argv[1]
path = os.path.join(ROOT, "translations", code + ".py")
spec = importlib.util.spec_from_file_location("tr_" + code, path)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

manifest = open(os.path.join(ROOT, "translations", "_new_strings_en.txt"), encoding="utf-8").read()
keys = manifest.split("### T_NEW START\n")[1].split("\n### T_NEW END")[0].strip().split("\n")

errors = []
for k in keys:
    if k not in m.T:
        errors.append("T missing key: %r" % k)
    elif not m.T[k] or not m.T[k].strip():
        errors.append("T empty value for: %r" % k)

if "home" not in m.SEO:
    errors.append("SEO missing 'home' entry")
else:
    t, d = m.SEO["home"]
    if "Prometheus Robotics" not in t:
        errors.append("SEO home title should keep the brand name")
if "research" not in m.SEO:
    errors.append("SEO missing 'research' entry")
for old in ("manufacturing", "entertainment"):
    if old in m.SEO:
        errors.append("SEO still has retired entry: %s" % old)

faq_home = getattr(m, "FAQ_HOME", None)
if not faq_home or len(faq_home) != 4:
    errors.append("FAQ_HOME must be a list of 4 (q, a) pairs")
else:
    for q, a in faq_home:
        if '"' in q or '"' in a:
            errors.append("FAQ_HOME contains a double quote: %r" % q)
    if faq_home[3] != m.FAQ_RESEARCH[5]:
        errors.append("FAQ_HOME pair 4 must equal FAQ_RESEARCH pair 6 (made-in-EU)")
if len(getattr(m, "FAQ_RESEARCH", [])) != 6:
    errors.append("FAQ_RESEARCH must still have 6 pairs")

# keys must be absent from values (common paste error: translating the key)
for k in ("Bimanual Robots for Tasks Too Flexible for Fixed Automation",):
    if k in m.T and m.T[k] == k:
        errors.append("T value equals English for: %r" % k)

if errors:
    print("FAIL %s" % code)
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("OK %s (%d new keys, SEO home, FAQ_HOME present)" % (code, len(keys)))
