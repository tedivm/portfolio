# AGENTS.md

## Site Generation

This is a static portfolio site generated from YAML data using Python.

- **Generator:** `generate.py` (uses Jinja2 templates + PyYAML)
- **Dependencies:** `jinja2>=3.0`, `pyyaml>=6.0` (managed via `pyproject.toml`)
- **Output:** `_site/` directory

### Regenerate the site

```bash
uv run python generate.py
```

Do not use `pip install` — the project uses `uv` for dependency management via `pyproject.toml`.

## Theme Updates

The site uses Rob's Style Guide as its upstream theme. CSS lives in `style.css`.

### Updating colors from upstream

1. Load the `robs-theme-implementation` skill to get the latest color tokens
2. Fetch the upstream theme from `https://tedivm.github.io/robs-style-guide/vanilla/theme.css`
3. Update `style.css` `:root` (dark mode) and `.light` (light mode) variables to match
4. Update any hardcoded `rgba()` values in badges, buttons, `hr`, and gradient hovers to match the new hex tokens
5. Regenerate the site with `uv run python generate.py`

### Key variables to watch for changes

- `--primary`, `--secondary`, `--accent` (may swap roles or shift hues)
- `--bg`, `--surface`, `--border` (mode-dependent layers)
- `--error`, `--success`, `--warning` (status colors)
- `--muted`, `--dim` (text hierarchy)
- All hardcoded `rgba(...)` values in component styles

## Project Structure

- `style.css` — all CSS (variables, components, layout, portfolio-specific styles)
- `_data/projects.yaml` — project data source
- `_data/writings.yaml` — writings data source
- `templates/` — Jinja2 HTML templates
- `generate.py` — build script
- `_site/` — generated output (gitignored)
- `fonts/` — self-hosted font files
