"""
Custom flat-vector mascots for each Money Spirit.

One inline SVG per behavioural driver. Each mascot carries a signature prop
that signals the customer's *spending behaviour* (a boarding pass + backpack
for the traveller, a burger for the foodie, a piggy bank for the saver, and
so on), drawn in a consistent premium flat-illustration style on a 200x200
viewBox so they scale cleanly from a 28px chip to the 190px reveal.

No external assets — every mascot is embedded directly in the rendered HTML,
so the experience stays a single, shareable, offline payload.
"""

MASCOTS = {
    # --- Travel Kangaroo · sunglasses + boarding pass + backpack ----------
    "travel": """<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <ellipse cx="100" cy="184" rx="46" ry="8" fill="rgba(0,0,0,0.16)"/>
  <!-- tail -->
  <path d="M64 178 Q26 168 30 126 Q40 118 54 122 Q44 150 80 160 Z" fill="#A9602F"/>
  <!-- hind foot -->
  <path d="M72 166 Q60 184 94 182 L102 170 Z" fill="#A9602F"/>
  <!-- body -->
  <path d="M100 82 C129 82 139 112 135 141 C132 163 117 175 100 175 C83 175 68 163 65 141 C61 112 71 82 100 82 Z" fill="#C77B4A"/>
  <ellipse cx="103" cy="138" rx="19" ry="29" fill="#E8B585"/>
  <!-- backpack peeking behind shoulder -->
  <path d="M68 100 Q52 108 54 134 Q56 152 70 158 Q60 130 72 102 Z" fill="#2E7D74"/>
  <path d="M60 116 q-8 2 -6 16" stroke="#256b63" stroke-width="5" fill="none" stroke-linecap="round"/>
  <!-- arms -->
  <path d="M120 116 q15 5 15 20" stroke="#B06A3D" stroke-width="10" fill="none" stroke-linecap="round"/>
  <path d="M85 124 q-7 6 -5 17" stroke="#B06A3D" stroke-width="9" fill="none" stroke-linecap="round"/>
  <!-- boarding pass -->
  <g transform="rotate(-10 104 150)">
    <rect x="84" y="139" width="42" height="23" rx="4" fill="#fff"/>
    <rect x="84" y="139" width="12" height="23" rx="4" fill="#FFCC00"/>
    <circle cx="90" cy="150.5" r="2.4" fill="#fff"/>
    <rect x="100" y="145" width="21" height="3" rx="1.5" fill="#2E7D74"/>
    <rect x="100" y="151" width="16" height="2.4" rx="1.2" fill="#C9CDD2"/>
    <rect x="100" y="156" width="12" height="2.4" rx="1.2" fill="#C9CDD2"/>
  </g>
  <!-- head -->
  <ellipse cx="102" cy="65" rx="23" ry="22" fill="#C77B4A"/>
  <!-- ears -->
  <ellipse cx="90" cy="36" rx="6" ry="17" fill="#C77B4A" transform="rotate(-16 90 36)"/>
  <ellipse cx="113" cy="35" rx="6" ry="17" fill="#C77B4A" transform="rotate(11 113 35)"/>
  <ellipse cx="90" cy="38" rx="2.6" ry="10" fill="#E89B6A" transform="rotate(-16 90 38)"/>
  <ellipse cx="113" cy="37" rx="2.6" ry="10" fill="#E89B6A" transform="rotate(11 113 37)"/>
  <!-- muzzle + nose -->
  <ellipse cx="108" cy="74" rx="13" ry="10" fill="#D98B57"/>
  <ellipse cx="115" cy="73" rx="3.8" ry="2.9" fill="#3A2418"/>
  <!-- sunglasses -->
  <rect x="83" y="59" width="16" height="11" rx="5" fill="#23282D"/>
  <rect x="103" y="59" width="16" height="11" rx="5" fill="#23282D"/>
  <rect x="98" y="62" width="6" height="3" rx="1.5" fill="#23282D"/>
  <rect x="86" y="61" width="6" height="2.6" rx="1.3" fill="#5b6470"/>
  <circle cx="90" cy="80" r="3.6" fill="#FF9D70" opacity="0.4"/>
</svg>""",

    # --- Lifestyle Quokka · phone (selfie) + coffee ----------------------
    "lifestyle": """<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <ellipse cx="100" cy="190" rx="48" ry="8" fill="rgba(0,0,0,0.16)"/>
  <ellipse cx="100" cy="132" rx="44" ry="48" fill="#A9733F"/>
  <ellipse cx="100" cy="142" rx="27" ry="32" fill="#D7A567"/>
  <!-- ears -->
  <circle cx="74" cy="84" r="13" fill="#A9733F"/>
  <circle cx="126" cy="84" r="13" fill="#A9733F"/>
  <circle cx="74" cy="84" r="6.5" fill="#C99A63"/>
  <circle cx="126" cy="84" r="6.5" fill="#C99A63"/>
  <!-- arms -->
  <path d="M70 120 q-12 4 -14 -8" stroke="#A9733F" stroke-width="11" fill="none" stroke-linecap="round"/>
  <path d="M130 120 q14 6 16 22" stroke="#A9733F" stroke-width="11" fill="none" stroke-linecap="round"/>
  <!-- phone (selfie) -->
  <g transform="rotate(18 52 108)">
    <rect x="44" y="96" width="20" height="30" rx="4" fill="#23282D"/>
    <rect x="47" y="100" width="14" height="20" rx="2" fill="#7FD7E8"/>
    <circle cx="54" cy="123" r="1.6" fill="#5b6470"/>
  </g>
  <!-- coffee cup -->
  <g transform="rotate(-8 150 120)">
    <path d="M142 116 h16 l-2 18 h-12 Z" fill="#E6D7BE"/>
    <rect x="141" y="112" width="18" height="5" rx="2" fill="#B98A5A"/>
    <path d="M150 104 q3 4 0 7" stroke="#fff" stroke-width="2" fill="none" stroke-linecap="round" opacity="0.7"/>
  </g>
  <!-- head/face -->
  <circle cx="100" cy="100" r="38" fill="#B5814A"/>
  <ellipse cx="100" cy="116" rx="21" ry="17" fill="#D7A567"/>
  <path d="M78 98 q6 -6 12 0" stroke="#2E1C10" stroke-width="3" fill="none" stroke-linecap="round"/>
  <path d="M110 98 q6 -6 12 0" stroke="#2E1C10" stroke-width="3" fill="none" stroke-linecap="round"/>
  <ellipse cx="100" cy="112" rx="5" ry="3.6" fill="#5A3A22"/>
  <path d="M88 120 Q100 130 112 120" stroke="#5A3A22" stroke-width="3" fill="none" stroke-linecap="round"/>
  <circle cx="76" cy="114" r="5" fill="#FF8FB5" opacity="0.5"/>
  <circle cx="124" cy="114" r="5" fill="#FF8FB5" opacity="0.5"/>
</svg>""",

    # --- Foodie Koala · burger ------------------------------------------
    "food": """<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <ellipse cx="100" cy="190" rx="46" ry="8" fill="rgba(0,0,0,0.16)"/>
  <ellipse cx="100" cy="134" rx="40" ry="44" fill="#9AA3AA"/>
  <ellipse cx="100" cy="144" rx="23" ry="28" fill="#C2C9CE"/>
  <!-- ears -->
  <circle cx="64" cy="80" r="21" fill="#9AA3AA"/>
  <circle cx="136" cy="80" r="21" fill="#9AA3AA"/>
  <circle cx="64" cy="80" r="11" fill="#C7A9B8"/>
  <circle cx="136" cy="80" r="11" fill="#C7A9B8"/>
  <!-- arms holding burger -->
  <path d="M72 128 q-6 14 14 20" stroke="#8A939A" stroke-width="11" fill="none" stroke-linecap="round"/>
  <path d="M128 128 q6 14 -14 20" stroke="#8A939A" stroke-width="11" fill="none" stroke-linecap="round"/>
  <!-- burger -->
  <path d="M78 150 q22 -16 44 0 Z" fill="#E0A24A"/>
  <circle cx="90" cy="142" r="1.4" fill="#fff"/>
  <circle cx="100" cy="139" r="1.4" fill="#fff"/>
  <circle cx="110" cy="142" r="1.4" fill="#fff"/>
  <path d="M76 150 q24 8 48 0 Z" fill="#5FBF6A"/>
  <rect x="76" y="152" width="48" height="7" rx="2" fill="#8A4B2E"/>
  <path d="M76 159 q24 12 48 0 Z" fill="#E0A24A"/>
  <!-- head/face -->
  <circle cx="100" cy="94" r="37" fill="#A6AFB6"/>
  <circle cx="84" cy="88" r="5.5" fill="#2C3136"/>
  <circle cx="116" cy="88" r="5.5" fill="#2C3136"/>
  <circle cx="85.6" cy="86" r="1.8" fill="#fff"/>
  <circle cx="117.6" cy="86" r="1.8" fill="#fff"/>
  <path d="M86 104 Q100 118 114 104 Q108 114 100 114 Q92 114 86 104 Z" fill="#34393E"/>
  <circle cx="74" cy="100" r="5" fill="#FF9DBb" opacity="0.4"/>
  <circle cx="126" cy="100" r="5" fill="#FF9DBb" opacity="0.4"/>
</svg>""",

    # --- Cinephile Possum · 3D glasses + popcorn ------------------------
    "entertainment": """<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <ellipse cx="100" cy="190" rx="44" ry="8" fill="rgba(0,0,0,0.16)"/>
  <path d="M138 150 Q172 150 168 118 Q150 132 130 134 Z" fill="#7C858E"/>
  <ellipse cx="100" cy="136" rx="38" ry="42" fill="#8E97A0"/>
  <ellipse cx="100" cy="146" rx="22" ry="26" fill="#B4BCC3"/>
  <!-- ears -->
  <path d="M60 72 L68 102 L90 92 Z" fill="#8E97A0"/>
  <path d="M140 72 L132 102 L110 92 Z" fill="#8E97A0"/>
  <path d="M66 78 L72 96 L84 90 Z" fill="#E7A9B0"/>
  <path d="M134 78 L128 96 L116 90 Z" fill="#E7A9B0"/>
  <!-- arms holding popcorn -->
  <path d="M74 130 q-4 16 16 18" stroke="#828b94" stroke-width="11" fill="none" stroke-linecap="round"/>
  <path d="M126 130 q4 16 -16 18" stroke="#828b94" stroke-width="11" fill="none" stroke-linecap="round"/>
  <!-- popcorn box -->
  <path d="M84 146 h32 l-4 22 h-24 Z" fill="#E04A4A"/>
  <path d="M84 146 h32 l-4 22 h-24 Z" fill="url(#pop)" opacity="0"/>
  <rect x="88" y="150" width="4" height="18" fill="#fff" opacity="0.8"/>
  <rect x="98" y="150" width="4" height="18" fill="#fff" opacity="0.8"/>
  <rect x="108" y="150" width="4" height="18" fill="#fff" opacity="0.8"/>
  <circle cx="90" cy="144" r="5" fill="#FCE3A8"/>
  <circle cx="100" cy="141" r="6" fill="#FCE3A8"/>
  <circle cx="110" cy="144" r="5" fill="#FCE3A8"/>
  <circle cx="96" cy="140" r="4.5" fill="#FFF1C9"/>
  <circle cx="105" cy="140" r="4.5" fill="#FFF1C9"/>
  <!-- head/face -->
  <circle cx="100" cy="96" r="35" fill="#9AA3AB"/>
  <path d="M100 94 L82 85 L82 108 Z" fill="#C2C9CF"/>
  <path d="M100 94 L118 85 L118 108 Z" fill="#C2C9CF"/>
  <circle cx="100" cy="116" r="13" fill="#C2C9CF"/>
  <!-- 3D glasses -->
  <rect x="76" y="86" width="22" height="15" rx="4" fill="#E04A4A" opacity="0.9"/>
  <rect x="102" y="86" width="22" height="15" rx="4" fill="#3DB6E0" opacity="0.9"/>
  <rect x="96" y="90" width="8" height="4" fill="#23282D"/>
  <circle cx="87" cy="93.5" r="3.4" fill="#23282D"/>
  <circle cx="113" cy="93.5" r="3.4" fill="#23282D"/>
  <ellipse cx="100" cy="110" rx="5" ry="4" fill="#E78FA0"/>
</svg>""",

    # --- Fitness Emu · sweatband + dumbbell -----------------------------
    "fitness": """<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <ellipse cx="100" cy="190" rx="34" ry="7" fill="rgba(0,0,0,0.16)"/>
  <!-- legs -->
  <path d="M93 150 L89 184" stroke="#D9963F" stroke-width="6" stroke-linecap="round"/>
  <path d="M107 150 L111 184" stroke="#D9963F" stroke-width="6" stroke-linecap="round"/>
  <path d="M89 184 l-10 4 M89 184 l0 11 M89 184 l9 6" stroke="#D9963F" stroke-width="4" stroke-linecap="round"/>
  <path d="M111 184 l10 4 M111 184 l0 11 M111 184 l-9 6" stroke="#D9963F" stroke-width="4" stroke-linecap="round"/>
  <!-- body -->
  <ellipse cx="100" cy="120" rx="40" ry="44" fill="#5B6168"/>
  <ellipse cx="100" cy="116" rx="30" ry="34" fill="#727983"/>
  <!-- wing -->
  <ellipse cx="73" cy="120" rx="11" ry="22" fill="#4E545B"/>
  <!-- dumbbell held across body -->
  <rect x="84" y="131" width="32" height="7" rx="3.5" fill="#34D39A"/>
  <rect x="80" y="125" width="7" height="19" rx="2.5" fill="#2BA378"/>
  <rect x="113" y="125" width="7" height="19" rx="2.5" fill="#2BA378"/>
  <!-- neck -->
  <path d="M96 92 Q88 56 106 44" stroke="#5B6168" stroke-width="14" fill="none" stroke-linecap="round"/>
  <!-- head -->
  <circle cx="110" cy="42" r="15" fill="#727983"/>
  <path d="M123 44 l16 2 l-15 6 Z" fill="#E8A24A"/>
  <circle cx="115" cy="39" r="3.2" fill="#15171A"/>
  <circle cx="116" cy="38" r="1.1" fill="#fff"/>
  <!-- sweatband -->
  <path d="M96 33 a15 15 0 0 0 28 4 l0 -5 a15 15 0 0 1 -28 -4 Z" fill="#FF5A5A"/>
  <rect x="106" y="30" width="5" height="6" rx="1" fill="#fff" opacity="0.85"/>
</svg>""",

    # --- Saver Echidna · piggy bank + coin ------------------------------
    "saving": """<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <ellipse cx="100" cy="188" rx="54" ry="8" fill="rgba(0,0,0,0.16)"/>
  <g>
    <path d="M78 132 L62 84 L92 128 Z" fill="#6E4A28"/>
    <path d="M94 128 L88 70 L112 126 Z" fill="#5A3E22"/>
    <path d="M114 126 L122 72 L132 130 Z" fill="#6E4A28"/>
    <path d="M132 132 L150 86 L142 138 Z" fill="#5A3E22"/>
    <path d="M64 136 L46 100 L74 132 Z" fill="#5A3E22"/>
  </g>
  <ellipse cx="100" cy="146" rx="48" ry="32" fill="#8A5E34"/>
  <!-- snout -->
  <path d="M54 152 Q26 146 20 128 Q42 134 60 138 Z" fill="#C99A63"/>
  <ellipse cx="28" cy="135" rx="6" ry="4" fill="#3A2614"/>
  <circle cx="62" cy="136" r="4.4" fill="#2E1C10"/>
  <circle cx="63.6" cy="134.4" r="1.5" fill="#fff"/>
  <!-- piggy bank -->
  <ellipse cx="120" cy="158" rx="24" ry="18" fill="#FF9DC0"/>
  <ellipse cx="120" cy="158" rx="24" ry="18" fill="#FF8FB5"/>
  <circle cx="104" cy="156" r="6" fill="#FFB3D1"/>
  <ellipse cx="100" cy="156" rx="3.5" ry="4.5" fill="#E86A9A"/>
  <circle cx="99" cy="155" r="1.2" fill="#7A2E4E"/>
  <circle cx="103" cy="155" r="1.2" fill="#7A2E4E"/>
  <rect x="116" y="142" width="10" height="3" rx="1.5" fill="#E86A9A"/>
  <path d="M108 174 l-3 6 M120 176 l0 6 M132 174 l3 6" stroke="#FF8FB5" stroke-width="4" stroke-linecap="round"/>
  <ellipse cx="135" cy="146" rx="5" ry="3.5" fill="#FFB3D1"/>
  <!-- coin going in -->
  <circle cx="121" cy="130" r="8" fill="#FFCC00" stroke="#E0AC00" stroke-width="2"/>
  <text x="121" y="134" font-size="9" font-weight="900" text-anchor="middle" fill="#B98A00">$</text>
</svg>""",

    # --- Techie Platypus · laptop ---------------------------------------
    "technology": """<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <ellipse cx="100" cy="190" rx="52" ry="8" fill="rgba(0,0,0,0.16)"/>
  <path d="M148 152 Q182 152 182 134 Q182 118 154 126 Z" fill="#5A3A24"/>
  <ellipse cx="98" cy="138" rx="54" ry="34" fill="#6E4A30"/>
  <ellipse cx="98" cy="146" rx="38" ry="20" fill="#8A6242"/>
  <!-- head -->
  <circle cx="66" cy="104" r="29" fill="#6E4A30"/>
  <!-- bill -->
  <path d="M38 108 q-16 0 -18 12 q12 8 28 4 q8 -8 0 -16 Z" fill="#E8A24A"/>
  <ellipse cx="24" cy="116" rx="3.4" ry="2.4" fill="#5A3A24"/>
  <ellipse cx="32" cy="116" rx="3.4" ry="2.4" fill="#5A3A24"/>
  <circle cx="60" cy="96" r="4.4" fill="#1F140C"/>
  <circle cx="61.6" cy="94.4" r="1.6" fill="#fff"/>
  <circle cx="76" cy="96" r="4.4" fill="#1F140C"/>
  <circle cx="77.6" cy="94.4" r="1.6" fill="#fff"/>
  <!-- arms to laptop -->
  <path d="M82 132 q14 6 18 16" stroke="#5e3e28" stroke-width="9" fill="none" stroke-linecap="round"/>
  <!-- laptop -->
  <g transform="translate(0 4)">
    <rect x="96" y="120" width="44" height="30" rx="3" fill="#2E343B"/>
    <rect x="100" y="124" width="36" height="22" rx="2" fill="#3DD6FF"/>
    <rect x="104" y="128" width="20" height="2.6" rx="1.3" fill="#fff" opacity="0.85"/>
    <rect x="104" y="133" width="26" height="2.6" rx="1.3" fill="#fff" opacity="0.55"/>
    <rect x="104" y="138" width="16" height="2.6" rx="1.3" fill="#fff" opacity="0.55"/>
    <path d="M90 150 h56 l4 8 h-64 Z" fill="#9AA3AB"/>
    <rect x="108" y="152" width="20" height="3" rx="1.5" fill="#6B7178"/>
  </g>
  <path d="M150 110 l7 -7 l-2 5 l5 -2 l-7 7 l2 -5 Z" fill="#3DD6FF"/>
  <path d="M164 128 l4 -4 l-1 3 l3 -1 l-4 4 l1 -3 Z" fill="#3DD6FF"/>
</svg>""",

    # --- Giver Kookaburra · gift box ------------------------------------
    "giving": """<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <ellipse cx="100" cy="190" rx="44" ry="8" fill="rgba(0,0,0,0.16)"/>
  <path d="M94 152 L90 178 M108 152 L112 178" stroke="#C98A3D" stroke-width="5" stroke-linecap="round"/>
  <ellipse cx="100" cy="126" rx="38" ry="44" fill="#B98A5A"/>
  <ellipse cx="100" cy="138" rx="22" ry="29" fill="#E6D7BE"/>
  <!-- blue wing -->
  <path d="M122 116 q30 4 34 40 q-26 -6 -36 -22 Z" fill="#3D6E8A"/>
  <path d="M128 124 q18 6 22 30" stroke="#2C5470" stroke-width="3" fill="none" opacity="0.5"/>
  <!-- arms holding gift -->
  <path d="M78 136 q-6 14 14 18" stroke="#A87C4F" stroke-width="10" fill="none" stroke-linecap="round"/>
  <path d="M122 136 q6 14 -14 18" stroke="#A87C4F" stroke-width="10" fill="none" stroke-linecap="round"/>
  <!-- gift box -->
  <rect x="82" y="146" width="36" height="26" rx="3" fill="#E0526A"/>
  <rect x="82" y="146" width="36" height="9" rx="3" fill="#EF6E84"/>
  <rect x="96" y="146" width="8" height="26" fill="#FFCC00"/>
  <path d="M100 146 q-10 -12 -2 -12 q6 0 2 12 Z" fill="#FFCC00"/>
  <path d="M100 146 q10 -12 2 -12 q-6 0 -2 12 Z" fill="#FFCC00"/>
  <circle cx="100" cy="142" r="3.4" fill="#FFD84D"/>
  <!-- head -->
  <circle cx="90" cy="78" r="33" fill="#E8E2D4"/>
  <path d="M68 64 q22 -10 44 0 q-12 8 -22 8 q-12 0 -22 -8 Z" fill="#B98A5A" opacity="0.5"/>
  <!-- beak -->
  <path d="M112 82 L152 88 L112 96 Z" fill="#4A4A4A"/>
  <path d="M112 88 L148 88" stroke="#2E2E2E" stroke-width="1.6"/>
  <circle cx="90" cy="76" r="6.2" fill="#23282D"/>
  <circle cx="92.2" cy="73.8" r="2.2" fill="#fff"/>
  <path d="M62 64 q-6 -10 4 -16 q6 8 2 16 Z" fill="#B98A5A"/>
</svg>""",
}
