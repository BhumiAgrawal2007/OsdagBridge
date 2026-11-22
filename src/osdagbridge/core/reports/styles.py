"""
Single source of truth for report styling.
Every value here was taken from the original report_generator.py.
"""

# ---- Page layout ----
PAGE = {
    "paper": "a4paper",
    "margin": "1in",
}

# ---- Colors (name -> HTML hex) ----
COLORS = {
    "osdagGreen": "91B014",
}

# ---- Table layout ----
TABLE = {
    "tabcolsep": "6pt",
    "arraystretch": "1.12",
    "arrayrulewidth": "0.5pt",
    "extrarowheight": "0.6pt",
    "lt_pre": "0pt",
    "lt_post": "6pt",
    "row_pad": "6pt",          # the \\[6pt] used after every row
    "needspace": "5",          # baselineskips kept free before a table
}

# ---- Captions ----
CAPTION = {
    "labelfont": "bf",
    "justification": "raggedright",
}

# ---- Header/footer ----
HEADER_FOOTER = {
    "rule_width": "1pt",
    "footer_left": r"Osdag $|$ FOSSEE $|$ Indian Institute of Technology Bombay",
}

# ---- Charts (for Tasks 4 and 5) ----
CHART = {
    "dpi": 200,
    "figsize": (6.5, 4.0),
    "pass_color": "#" + COLORS["osdagGreen"],
    "fail_color": "#C0392B",
    "threshold_color": "red",
    "threshold_style": "--",
}