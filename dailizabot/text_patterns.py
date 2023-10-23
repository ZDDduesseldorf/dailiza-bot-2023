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

    [r"[Ee]rzaehle mir (?:einen|einen weiteren) Witz",
    ["Natürlich! Hier ist ein Witz für dich: Warum hat der Kühlschrank den Laptop nicht bezahlt? Weil er schon eine eigene Rechnung hatte!",
     "Klar, hier ist einer: Was macht ein Clown im Büro? Faxen!",
     "Warum hat der Mathematiker eine Brille? Weil er mit Zahlen jongliert!",
     "Was ist grün und läuft durch den Wald? Eine Rudel Gurken!"]],

]
