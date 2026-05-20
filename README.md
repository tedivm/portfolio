# Robert Hafner's Portfolio

This is my portfolio page. You can view it in action [here](https://projects.tedivm.com).

## Local Development

Build the site:

```bash
uv run python generate.py
```

Serve locally:

```bash
uv run python generate.py && python -m http.server 8000 -d _site
```

Then visit `http://localhost:8000`.

## How It Works

This site is built with a lightweight Python static site generator:

- **`generate.py`** — reads `_data/projects.yaml`, renders Jinja2 templates, copies static assets to `_site/`
- **`templates/index.html`** — main page template with Rob's Theme styling
- **`templates/404.html`** — error page template
- **`style.css`** — full Rob's Theme stylesheet with self-hosted fonts
- **`pyproject.toml`** — project metadata and dependencies (managed by `uv`)

Content lives in `_data/projects.yaml`. Edit it, rebuild, and refresh.

## Deployment

The site deploys automatically via GitHub Actions to `gh-pages` on every push to `master`.

## Dependencies

- Python 3.12+
- `uv` for environment management
- `jinja2` and `pyyaml` (installed automatically by `uv`)
