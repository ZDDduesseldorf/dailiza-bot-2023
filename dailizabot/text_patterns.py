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

    [r"Du bist (.*)", 
     ["Wieso denkst du, dass {0}?",
      "Kann ich etwas gegen {0} tun?", 
      "Dankeschön, dass ich {0} bin!"]],

    [r"Kannst du (.*)?", 
     ["Ich kann {0} gerne versuchen!",
     "Das kann ich leider nicht machen!",
     "Kannst du nicht selbst {0}?"]],

    [r"Ich bin (.*)",
     ["Schade, dass du denkst du wärst {0}"], 
     ["Absolut recht, du bist {0}"], 
     ["Wieso bist du denn {0}?"]]


]
