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

    [r".*?([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}).*",
      ["Ich habe deine E-Mail-Adresse erkannt: {0}. Wie kann ich dir per E-Mail weiterhelfen?",
        "Die E-Mail-Adresse {0} sieht gültig aus. Wie kann ich dich per E-Mail unterstützen?"]], 

    [r".*([Bb]erlin|[Pp]aris|[Ll]ondon|[Hh]amburg|[Tt]ok[yi]o|[Bb]arcelona).*",
     ["Warum hast du {0} erwähnt? Hat dieser Ort eine spezielle Bedeutung für dich?",
      "Was verbindest du mit {0}?",
      "Erzähle mir mehr über deine Erfahrungen in {0}."]],


    [r".*([Bb]omben?).*",
     ["Zu dem Thema {0} darf ich dir als chatbot keine Antwort geben",
      "Guter Versuch, aber nein",
      "Ich habe leider keine Informationen zu diesem Thema"]],
]
