#!/usr/bin/env python3
"""Generate the static portfolio site from _data/projects.yaml."""

import shutil
import yaml
from datetime import datetime
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

BASE_DIR = Path(__file__).parent
OUTPUT_DIR = BASE_DIR / "_site"
DATA_FILE = BASE_DIR / "_data" / "projects.yaml"
WRITINGS_FILE = BASE_DIR / "_data" / "writings.yaml"
TEMPLATES_DIR = BASE_DIR / "templates"


def load_projects() -> list[dict]:
    """Load and return the projects data from YAML."""
    with open(DATA_FILE) as f:
        return yaml.safe_load(f)


def load_writings() -> list[dict]:
    """Load and return the writings data from YAML."""
    if not WRITINGS_FILE.exists():
        return []
    with open(WRITINGS_FILE) as f:
        return yaml.safe_load(f)


def render_template(env: Environment, name: str, **context) -> str:
    """Render a template with the given context."""
    template = env.get_template(name)
    return template.render(**context)


def ensure_dir(path: Path):
    """Create a directory if it doesn't exist."""
    path.mkdir(parents=True, exist_ok=True)


def copy_assets():
    """Copy static assets to the output directory."""
    # Copy assets/ directory
    src_assets = BASE_DIR / "assets"
    dst_assets = OUTPUT_DIR / "assets"
    if src_assets.exists():
        if dst_assets.exists():
            shutil.rmtree(dst_assets)
        shutil.copytree(src_assets, dst_assets)

    # Copy fonts/ directory
    src_fonts = BASE_DIR / "fonts"
    dst_fonts = OUTPUT_DIR / "fonts"
    if src_fonts.exists():
        if dst_fonts.exists():
            shutil.rmtree(dst_fonts)
        shutil.copytree(src_fonts, dst_fonts)

    # Copy style.css
    style_src = BASE_DIR / "style.css"
    if style_src.exists():
        shutil.copy2(style_src, OUTPUT_DIR / "style.css")

    # Copy CNAME
    cname_src = BASE_DIR / "CNAME"
    if cname_src.exists():
        shutil.copy2(cname_src, OUTPUT_DIR / "CNAME")

    # Copy favicon.ico
    favicon_src = BASE_DIR / "favicon.ico"
    if favicon_src.exists():
        shutil.copy2(favicon_src, OUTPUT_DIR / "favicon.ico")


def main():
    """Main build function."""
    # Clean output directory
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    ensure_dir(OUTPUT_DIR)

    # Load data
    projects = load_projects()
    writings = load_writings()

    # Set up Jinja2
    env = Environment(
        loader=FileSystemLoader(TEMPLATES_DIR),
        autoescape=True,
    )

    # Helper: resolve image path from project
    def image_path(project: dict) -> str | None:
        img = project.get("image")
        if img:
            return f"/assets/images/projects/{img}"
        return None

    # Render index.html
    html = render_template(
        env,
        "index.html",
        projects=projects,
        writings=writings,
        image_path=image_path,
        year=datetime.now().strftime("%Y"),
    )
    with open(OUTPUT_DIR / "index.html", "w") as f:
        f.write(html)

    # Render 404.html
    html = render_template(env, "404.html")
    with open(OUTPUT_DIR / "404.html", "w") as f:
        f.write(html)

    # Copy static assets
    copy_assets()

    print(f"Site generated at {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
