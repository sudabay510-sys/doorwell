# Doorwell

A month-by-month maintenance and turnover plan for small landlords.

Quiz → personalized plan preview → email capture → Gumroad checkout (Monthly or Quarterly). Payments processed by Gumroad. Renews automatically. Cancel anytime from your Gumroad library.

## Run locally
```bash
pip install -r requirements.txt
python app.py   # http://127.0.0.1:5107
```

## Deploy (Render)
- Build: `pip install -r requirements.txt`
- Start: `gunicorn -b 0.0.0.0:$PORT app:app`
- Env: `SECRET_KEY`, `ADMIN_PASSWORD` (owner-only `/admin`), `DATABASE_URL` (pooled Neon Postgres URL), `DATABASE_SCHEMA=doorwell`. Without `DATABASE_URL` it falls back to SQLite (`DATABASE_PATH`).

## Tests
```bash
pytest -q
```

Plans are deterministic rules in `doorwell_brand.py` (`plan()`); swap in an LLM later if wanted.
With `DATABASE_URL` set, leads persist in Postgres. SQLite fallback on free hosting is ephemeral.
