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


    [r"W{0,3} bist du",
    ["Ich bin dein Chatbot Dailiza.",
    "Ich bin Dailza, und du?",
    "Du fragst zu viel. >:|"]]


    [r"Mir geht {0,5}s (.*)",
     ["Warum geht es {0}",
     "Was ist passiert?",
     "Erzähl mir mehr, ich bin für dich da."]]

     [r"W{0,3} (schliesse|beende|schließe) ich (*)",
      ["Gebe als nächsten input 'exit' ein.",
      "Indem du 'exit' eingibst"]]
]
