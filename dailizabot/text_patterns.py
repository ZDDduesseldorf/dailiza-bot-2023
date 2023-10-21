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
    
    [r"[Ww]arum bin ich (\b\w+\b)", 
    ["{0} zu sein ist normal. Mach Dir nicht so einen Kopf. ;)",
     "Finde heraus, warum Du {0} sein könntest.", 
     "Es könnte hilfreich sein, mit anderen Leuten über {0} zu sprechen."]],
    
    [r"[Ww]arum fühle ich mich (.*)", 
    ["Es gibt viele Gründe, warum Du Dich {0} fühlen könntest. Hast Du kürzlich etwas Bestimmtes erlebt?", 
     "Es ist normal, sich manchmal {0} zu fühlen. Was denkst Du, könnten Gründe sein?", 
     "Das Gefühl, sich {0} zu fühlen, kann verschiedene Ursachen haben."]],
    
    [r"[Mm]ein (.*) (.*)",
    ["Warum denkst Du, dass dein {0} {1}?",
     "Wie beeinflusst dein {0} dein Leben?",
     "Hast du mit jemandem über dein {0} gesprochen?"]]
]
