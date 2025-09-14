# generate.py
from jinja2 import Environment, FileSystemLoader, select_autoescape
import yaml
import os
import shutil

HERE = os.path.dirname(__file__)
TEMPLATE_DIR = os.path.join(HERE, "templates")
STATIC_DIR = os.path.join(HERE, "static")
OUT_DIR = os.path.join(HERE, "docs")  # GitHub Pages: serve from docs/

def load_data():
    with open(os.path.join(HERE, "data.yaml"), "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def copy_static(out_dir):
    dest = os.path.join(out_dir, "static")
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(STATIC_DIR, dest)

def render():
    data = load_data()
    env = Environment(
        loader=FileSystemLoader(TEMPLATE_DIR),
        autoescape=select_autoescape(['html', 'xml'])
    )
    if not os.path.exists(OUT_DIR):
        os.makedirs(OUT_DIR)
    pages = ["index.html", "projects.html", "contact.html"]
    for page in pages:
        template = env.get_template(page)
        html = template.render(site=data['site'], projects=data.get('projects', []))
        out_path = os.path.join(OUT_DIR, page)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
    copy_static(OUT_DIR)
    print("Site generated to", OUT_DIR)

if __name__ == "__main__":
    render()
