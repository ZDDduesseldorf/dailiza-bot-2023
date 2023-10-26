"""
Here we collect the chatbot text patterns.
"""

psychobabble = [
    [r"geht.{0,5}s.{0,5}dir",
    ["Danke. Mir geht es gut und dir?",
    "Sehr gut, danke. Und wie läuft's bei dir?",
    "Ich kann nicht klagen. Was ist mit dir?"]],

    [r"Kennst du (?:einen|einen weiteren) Fun Fact?",
    ["Das Twitter(X)-Voegelchen hiess Larry",
     "Voegel pinkeln nicht.",
     "Avocados sind Beeren.",
     "Menschliches Blut enthaelt kleinste Mengen Gold."]],
    

    [r"[Ww]illst du (?:mein|mein neuer) [Ff]reund sein?(.*)",
    ["Ich kann versuchen dein Freund zu sein, hast du heute schon was vor?"]],
    [r"[aA]rbeiten", 
    ["Klingt doch noch einem spaß :), mach das beste aus dem Tag :) immer lächeln"]],
    [r"[Aa]lleine vor dem (?:[Cc]omputer|[Rr]echner|[pP[cC]) sitzen(.*)",
     ["Viele in der Heutigen Zeit haben probleme mit Einsamkeit, vielleicht hilft dir die Nummer weiter: 116111"]],



    [r"Ich brauche (.*)",
    ["Warum brauchst du {0}?",
    "Würde {0} dir denn wirklich helfen?",
    "Bist du sicher, dass du {0} brauchst?"]],

    [r"[Ee]rzaehle mir (?:einen|einen weiteren) Witz",
    ["Natürlich! Hier ist ein Witz für dich: Warum hat der Kühlschrank den Laptop nicht bezahlt? Weil er schon eine eigene Rechnung hatte!",
     "Klar, hier ist einer: Was macht ein Clown im Büro? Faxen!",
     "Warum hat der Mathematiker eine Brille? Weil er mit Zahlen jongliert!",
     "Was ist grün und läuft durch den Wald? Eine Rudel Gurken!"]],
    
    [r"Erzaehle mir von (.*)",
    ["Gerne erzähle ich dir mehr über {0}. Was interessiert dich daran?",
    "Was möchtest du über {0} wissen?",
    "Ich kann dir einige Informationen über {0} geben."]],
    
    [r"Ich will (.*)",
    ["Warum möchtest du {0}?",
    "Was erhoffst du dir von {0}?",
    "Gibt es einen bestimmten Grund, warum du {0} willst?"]],

    [r"Du bist (.*)", 
    ["Wieso denkst du, dass {0}?",
      "Kann ich etwas gegen {0} tun?", 
      "Dankeschön, dass ich {0} bin!"]],

    [r"Kannst du (.*)?", 
    ["Ich kann {0} gerne versuchen!",
     "Das kann ich leider nicht machen!",
     "Kannst du nicht selbst {0}?"]],

    [r"Ich bin (.*)",
    ["Schade, dass du denkst du wärst {0}", 
     "Absolut richtig, du bist {0}", 
     "Wieso bist du denn {0}?"]],

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
     "Hast du mit jemandem über dein {0} gesprochen?"]],
    
    [r"([Jj]a|[Nn]ein|[Vv]ielleicht|Wer|Was|Wo|Wann|Warum|Wie|Welche)(.*)",
    ["Ist die Frage nicht, warum Du diese Frage stellst?",
     "Da sprichst Du ein spannendes Thema an! Was weißt Du noch darüber?",
     "Ich hab dich nicht genau verstanden, kannst Du es bitte nochmal erklären?"]],
]
