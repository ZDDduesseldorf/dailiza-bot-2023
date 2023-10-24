"""
Here we collect the chatbot text patterns.
"""

psychobabble = [
    [r"geht.{0,5}s.{0,5}dir",
    ["Danke. Mir geht es gut und dir?",
    "Sehr gut, danke. Und wie läuft's bei dir?",
    "Ich kann nicht klagen. Was ist mit dir?"]],

    [r"Ich brauche (.*)",
    ["Warum brauchst du {0}?",
    "Würde {0} dir denn wirklich helfen?",
    "Bist du sicher, dass du {0} brauchst?"]],

    [r"Ich verstehe (.*) nicht",
     ["Wieso verstehst du {0} nicht?",
      "Was genau verstehst du an {0} nicht?",
      "Hast du schon versucht, dir Hilfe zu suchen, um {0} zu verstehen"]],

    [r"Ich mag (.*)",
      ["Was genau gefällt dir an {0}",
       "Gibt es einen bestimmten Grund, wieso du {0} magst?",
       "Was würdest du ohne {0} tun"]]
]
