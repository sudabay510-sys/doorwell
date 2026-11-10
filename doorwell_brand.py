from helpers import L, LM, opt, env_names

Q = [
    {"id": "units", "type": "choice", "prompt": "How many rental units (doors) do you manage?",
     "options": [opt("1", "1 unit"), opt("2_4", "2–4 units"), opt("5_10", "5–10 units"), opt("11", "11+ units")]},
    {"id": "ptype", "type": "choice", "prompt": "What type of property is most of your portfolio?",
     "options": [opt("sfh", "Single-family homes"), opt("duplex", "Duplex / small multifamily"), opt("condo", "Condos"), opt("adu", "ADU / rooms in my home")]},
    {"id": "climate", "type": "choice", "prompt": "What’s the climate like?",
     "options": [opt("cold", "Cold winters / freezing"), opt("hot", "Hot summers"), opt("mild", "Mild / coastal"), opt("wet", "Rainy / humid"), opt("mixed", "Four distinct seasons")]},
    {"id": "hvac", "type": "choice", "prompt": "Main heating / cooling setup?",
     "options": [opt("furnace", "Furnace + central AC"), opt("heatpump", "Heat pump"), opt("boiler", "Boiler / radiators"), opt("wall", "Wall / window units"), opt("unsure", "Not sure")]},
    {"id": "who", "type": "choice", "prompt": "Who does repairs?",
     "options": [opt("me", "Mostly me (DIY)"), opt("handy", "A regular handyman"), opt("vendors", "Different vendors each time"), opt("none", "I scramble each time")]},
    {"id": "missed", "type": "choice", "prompt": "What slipped through the cracks last year?",
     "options": [opt("filters", "Filters & routine upkeep"), opt("alarms", "Smoke / CO alarm checks"), opt("renewals", "Lease renewal timing"), opt("turns", "Slow unit turnovers"), opt("emergency", "An avoidable emergency repair")]},
    {"id": "turn", "type": "choice", "prompt": "Any move-out / turnover expected in the next 3 months?",
     "options": [opt("yes", "Yes"), opt("maybe", "Maybe"), opt("no", "No")]},
    {"id": "hours", "type": "choice", "prompt": "Hours per month you want to spend on upkeep planning?",
     "options": [opt("1", "About 1"), opt("3", "2–4"), opt("6", "5+")]},
    {"id": "state", "type": "text", "prompt": "Which state or city are your rentals in?", "placeholder": "e.g. Sacramento, CA", "help": "Used only to remind you to check local landlord-tenant rules. Not legal advice."},
]

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def plan(a):
    climate = a.get("climate", "mixed")
    seasonal = {
        "cold": ["Oct: furnace service + pipe insulation check", "Nov: gutter clean, exterior hose bibs off", "Jan: check for ice dams / drafts"],
        "hot": ["Apr: AC service + condensate line flush", "Jun: check attic ventilation", "Aug: irrigation & exterior paint check"],
        "mild": ["Mar: roof & gutter visual check", "Jun: exterior wood & caulk check", "Oct: drainage before rains"],
        "wet": ["Sep: gutters, downspouts, grading", "Nov: check for leaks & mildew", "Mar: exhaust fans & dehumidifier"],
        "mixed": ["Apr: AC service", "Oct: furnace service", "Nov: gutters before winter"],
    }.get(climate)
    state = a.get("state") or "your area"
    return {
        "title": f"Doorwell maintenance calendar — {L(Q[0]['options'], a.get('units'))}, {L(Q[1]['options'], a.get('ptype')).lower()}",
        "summary": f"Built for a {L(Q[2]['options'], climate).lower()} climate with {L(Q[3]['options'], a.get('hvac')).lower()}. Last year’s miss: {L(Q[5]['options'], a.get('missed')).lower()}. This is a maintenance planning tool — not legal advice, and not a substitute for licensed inspections.",
        "preview_sections": [
            {"title": "Every month (unlocked)", "bullets": ["Log any tenant-reported issue the day it’s reported.", "Walk the exterior (or ask a neighbor/handyman) for leaks, trip hazards, and drainage.", "Check your vendor list is current."]},
            {"title": "Seasonal anchors", "bullets": seasonal + ["Every 6 months: test smoke & CO alarms (and give required notice before entering — rules vary)."]},
            {"title": "Local rules reminder", "body": f"Entry notice, deposit, habitability, and renewal rules vary by state and city. Check official sources for {state} or ask a local attorney. Doorwell doesn’t provide legal advice."},
        ],
        "locked_sections": [
            {"title": "12-month calendar by unit", "teaser": "Month-by-month tasks matched to your HVAC and climate."},
            {"title": "Turnover punch list", "teaser": "Move-out walk, repairs, cleaning, and photo log." + (" Starts now — you flagged a coming turnover." if a.get("turn") == "yes" else "")},
            {"title": "Vendor call log", "teaser": "Who to call, what they charged, and how it went."},
            {"title": "Tenant notice outlines", "teaser": "Plain-language outlines to adapt with your local rules — not legal forms."},
        ],
    }


BRAND = {
    "name": "Doorwell", "slug": "doorwell", "port": 5107,
    "tagline": "A month-by-month maintenance and turnover plan for small landlords.",
    "eyebrow": "For owners of 1–10 doors",
    "hero_title": "Stay ahead of filters, alarms, and turnovers — without property software.",
    "hero_lede": "Tell Doorwell about your units, climate, and who handles repairs. Get a maintenance calendar and turnover checklist sized for small portfolios.",
    "cta_primary": "Build my maintenance calendar", "cta_short": "Start quiz",
    "cta_band_title": "Small portfolio. Big-league habits.",
    "cta_band_text": "A calendar you can actually keep, built around your climate and your units.",
    "honesty_line": "Maintenance planning only. Not legal advice. Check your local landlord-tenant rules.",
    "audience_line": "Self-managing owners of 1–10 rental units who find full property-management software too heavy.",
    "personas": [
        {"title": "Accidental landlord", "text": "You rent out a former home and want to do it right."},
        {"title": "House-hacker", "text": "A duplex or ADU, with you as the handyman."},
        {"title": "Small portfolio owner", "text": "5–10 doors and too many sticky notes."},
    ],
    "journey": [
        {"stage": "Every month", "pain": "Small issues get noticed too late.", "fix": "A 15-minute monthly check routine."},
        {"stage": "Each season", "pain": "HVAC and gutters get skipped.", "fix": "Climate-matched seasonal anchors."},
        {"stage": "Renewal time", "pain": "Lease dates sneak up.", "fix": "Reminders to review terms with your local rules."},
        {"stage": "Turnover", "pain": "Vacant days pile up.", "fix": "A move-out punch list and vendor call log."},
    ],
    "how_steps": [
        {"title": "Quiz your units", "text": "Units, climate, HVAC, repairs, and last year’s misses."},
        {"title": "Preview your calendar", "text": "Monthly habits and seasonal anchors unlocked."},
        {"title": "Start your plan", "text": "Enter your email, then complete checkout on Gumroad."},
    ],
    "features": [
        {"title": "12-month calendar", "text": "Tasks matched to climate and HVAC type."},
        {"title": "Turnover punch list", "text": "Move-out to move-in, step by step."},
        {"title": "Vendor log", "text": "Track who you called and what it cost."},
        {"title": "Climate packs", "text": "Subscription: seasonal updates and annual renewal checklist."},
    ],
    "sample_peek": ["Monthly 15-minute walk", "Smoke/CO checks every 6 months", "Furnace or AC service window", "Turnover punch list"],
    "trust_points": [
        {"title": "No legal advice", "text": "We remind you to check local rules — we don’t interpret them."},
        {"title": "Safety first", "text": "Gas, electrical, and structural work belong to licensed pros."},
        {"title": "Light by design", "text": "A plan, not another system to learn."},
    ],
    "faq": [
        {"q": "Is this property-management software?", "a": "No. Doorwell is a planning and checklist tool. It doesn’t collect rent or handle tenant screening."},
        {"q": "Do the notice templates satisfy my state’s laws?", "a": "No guarantee. They’re plain-language outlines. Check your state and city rules or ask a local attorney."},
        {"q": "Can I use it for one unit?", "a": "Yes — plans scale from one door to about ten."},
        {"q": "How does billing work?", "a": "Choose Monthly or Quarterly, save your email, then complete payment on Gumroad. Renews automatically. Cancel anytime from your Gumroad library."},
    ],
    "pricing": [
        {"id": "monthly", "name": "Monthly", "price": "$15", "period": "/ month",
             "intro": "$15", "renewal": "$15 / month", "renewal_note": "Renews automatically. Cancel anytime from your Gumroad library.",
             "includes": ['12-month calendar', 'Monthly routine', 'Vendor log']},
        {"id": "quarterly", "name": "Quarterly", "price": "$39", "period": "every 3 months",
             "intro": "$39", "renewal": "$39 every 3 months", "renewal_note": "Renews automatically. Cancel anytime from your Gumroad library.", "featured": True,
             "includes": ['Everything in Monthly', 'Turnover punch list', 'Climate pack updates']},
    ],
    "checkout_url": "https://solvfix.gumroad.com/l/iouqzv",
    "disclaimer_short": "Maintenance planning only. Not legal, tax, or inspection advice. Landlord-tenant rules vary — check yours.",
    "disclaimer_long": "Doorwell provides general rental maintenance planning checklists. It is not legal advice and does not interpret landlord-tenant, habitability, notice, deposit, or fair-housing laws, which vary by state and city — consult official sources or a licensed attorney. Use licensed professionals for gas, electrical, structural, and safety work. Payments are processed by Gumroad, not on this site.",
    "font_url": "https://fonts.googleapis.com/css2?family=Archivo:wght@500;700;800&family=Public+Sans:wght@400;500;600&display=swap",
    "fonts": ("Archivo", "Public Sans"),
    "questions": Q, "generate_plan": plan,
    "voice": "Steady and practical, like a trusted building super. Plain words, no jargon, no legal opinions.",
    "palette": {"Background": "#F6F4EF", "Alt": "#ECE8DF", "Card": "#FFFFFF", "Ink": "#1F2A24", "Muted": "#5E665F", "Accent (brick)": "#B4462E", "Accent hover": "#923823", "Secondary (forest)": "#2F5D50"},
    "logo_svg": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none"><rect width="64" height="64" rx="8" fill="#B4462E"/><path d="M22 50V16h20v34" stroke="#FFF7F2" stroke-width="4" stroke-linejoin="round"/><circle cx="37" cy="34" r="2.6" fill="#FFF7F2"/><path d="M14 50h36" stroke="#FFF7F2" stroke-width="4" stroke-linecap="round"/></svg>',
    "css_vars": """
  --bg:#F6F4EF;--bg-alt:#ECE8DF;--card:#FFFFFF;--ink:#1F2A24;--muted:#5E665F;--line:#DDD6C8;
  --accent:#B4462E;--accent-2:#923823;--on-accent:#FFF7F2;--radius:6px;
  --font-display:'Archivo', system-ui, sans-serif;--font-body:'Public Sans', system-ui, sans-serif;
  --shadow-card:0 10px 0 rgba(31,42,36,.06);--shadow-btn:0 4px 0 #7A2E1E;
  --cta-band-bg:#2F5D50;--cta-band-ink:#F6F4EF;--cta-band-btn:#F6F4EF;--cta-band-btn-ink:#2F5D50;--tracking:-0.02em;
""",
    "personality": "background:repeating-linear-gradient(90deg, transparent 0 79px, rgba(180,70,46,.05) 79px 80px), var(--bg);",
    "extra_css": "h1,h2{text-transform:none;font-weight:800}.hero-card,.feature,.price-card,.journey-card{border-width:2px}",
    "dos": ["Point to licensed pros for gas, electrical, and structural work.", "Say ‘check your local rules’ wherever notice or deposits come up."],
    "donts": ["Give legal advice or claim templates are legally compliant.", "Discuss tenant screening in ways that could raise fair-housing issues."],
}
BRAND.update(env_names("doorwell"))
