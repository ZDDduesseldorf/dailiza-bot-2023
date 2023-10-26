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
    
    [r"Was ist (.*)",
    ["Ist {0} nicht hochkomplex und kann nicht in wenigen Worten beschrieben werden.",
    "Wenn du {0} lang genug betrachtest,\nwird sich eine neue Erkenntnis kristallisieren.",
    "Ich kann {0} nur empfehlen."]],
    
    [r"Was (kann|soll) .*",
     ["Die Entscheidung liegt letztenendes bei dir selber. Hör auf dein Herz und es wird dich leiten.",
      "Du {0}st deine Gedanken noch einmal erforschen um einen neuen Pfad zu finden.",
      "Niemand {0} dir besser helfen als du selbst.",
      "Man {0} immer einen neuen Weg einschlagen, wenn der jetzige nicht gut ist"]],
    
    [r"Hast du bock auf (.*)",
     ["Ich bin zwar nur ein Chatbot, aber ich lasse mich gerne zu {0} überreden.",
      "Fühlst du dich vielleicht einsam?",
      "So ein Zufall, {0} ist meine Lieblingsbeschäftigung!"]]

]
