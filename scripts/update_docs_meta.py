#!/usr/bin/env python3
"""
update_docs_meta.py — Aly × Trouble Protocol
──────────────────────────────────────────────
Automates:
 • YAML version + timestamp updates
 • Shields.io badge injection
 • Changelog + version tree logs
 • Public mirror export (publish:true)
 • Safe GH_TOKEN push support
 • Directory .keep scaffolding
 • Self-healing dependency install (PupIT)
──────────────────────────────────────────────
"""

import importlib, subprocess, sys

# ─────────────────────────────
# 🧠 Auto-Dependency Check
# ─────────────────────────────
REQUIRED_PACKAGES = {
    "yaml": "PyYAML",
    "dotenv": "python-dotenv",
}

def ensure_dependencies():
    """Verify required modules and install if missing."""
    for module, package in REQUIRED_PACKAGES.items():
        try:
            importlib.import_module(module)
        except ImportError:
            print(f"📦 Missing dependency: {package}. Installing…")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

ensure_dependencies()

# ─────────────────────────────
# 📦 Imports (safe to import after deps are ensured)
# ─────────────────────────────
import os, re, json, yaml
from datetime import datetime
from shutil import copy2
from dotenv import load_dotenv

# ─────────────────────────────
# 🔧 Load environment variables
# ─────────────────────────────
load_dotenv()
GH_TOKEN = os.getenv("GH_TOKEN")

# ─────────────────────────────
# 📂 Config
# ─────────────────────────────
DOCS_ROOT = "docs"
PUBLIC_REPO = "../Aly_and_Trouble_Protocol_Public"
PUBLIC_DOCS = os.path.join(PUBLIC_REPO, "docs")
BADGE_TAG_START = "<!-- BADGES_START -->"
BADGE_TAG_END = "<!-- BADGES_END -->"
CHANGELOG_DIR = "data/changelogs"
GLOBAL_CHANGELOG = "CHANGELOG.md"
VISUAL_TREE_JSON = "data/analytics/version_tree.json"
DATE_FMT = "%Y-%m-%d"

BADGE_COLORS = {
    "phase": "red",
    "sub_phase": "rose",
    "cycle": "pink",
    "node": "green",
    "status": "purple"
}

# ─────────────────────────────
# 🧱 Utilities
# ─────────────────────────────
def ensure_repo_structure():
    skeletons = [
        "data/changelogs",
        "data/analytics",
        "docs/00-Overview",
        "docs/10-Phases",
    ]
    for path in skeletons:
        os.makedirs(path, exist_ok=True)
        keep_file = os.path.join(path, ".keep")
        if not os.path.exists(keep_file):
            with open(keep_file, "w", encoding="utf-8") as f:
                f.write("# placeholder to keep directory in Git\n")
            print(f"📁 Created placeholder: {keep_file}")

def extract_front_matter(text):
    match = re.match(r"^---\n(.*?)\n---\n(.*)", text, re.DOTALL)
    if not match: return None, text
    return yaml.safe_load(match.group(1)), match.group(2)

def dump_front_matter(meta):
    return "---\n" + yaml.safe_dump(meta, sort_keys=False).strip() + "\n---\n"

def build_badge(label, message, color, style="flat-square"):
    safe_label = str(label).replace(" ", "_")
    safe_message = str(message).replace(" ", "_")
    return f"![{safe_label}](https://img.shields.io/badge/{safe_label}-{safe_message}-{color}?style={style})"

def generate_badges(meta):
    return "\n".join(
        build_badge(k, meta[k], BADGE_COLORS.get(k, "blue"))
        for k in ["phase","sub_phase","cycle","node","status"]
        if k in meta and meta[k]
    )

def insert_badges(md_text, badges_block):
    pattern = re.compile(rf"{BADGE_TAG_START}.*?{BADGE_TAG_END}", re.DOTALL)
    replacement = f"{BADGE_TAG_START}\n{badges_block}\n{BADGE_TAG_END}"
    return pattern.sub(replacement, md_text) if pattern.search(md_text) else f"{replacement}\n\n{md_text}"

def bump_version(v):
    if not v or not v.startswith("v"): return "v1.0"
    try:
        major, minor = v[1:].split(".")
        return f"v{major}.{int(minor)+1}"
    except Exception:
        return "v1.0"

def log_change(filepath, version, note):
    os.makedirs(CHANGELOG_DIR, exist_ok=True)
    fn = os.path.basename(filepath).replace(".md", "")
    log_path = os.path.join(CHANGELOG_DIR, f"{fn}.log")
    ts = datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(f"[{ts}] {version} — {note}\n")
    return ts

def append_global_changelog(path, ver, note, ts):
    with open(GLOBAL_CHANGELOG, "a", encoding="utf-8") as f:
        f.write(f"- **{path}** → {ver} — {note}  \n  *{ts}*\n")

def update_visual_tree(path, ver, ts, note):
    os.makedirs(os.path.dirname(VISUAL_TREE_JSON), exist_ok=True)
    data = {}
    if os.path.exists(VISUAL_TREE_JSON):
        with open(VISUAL_TREE_JSON,"r",encoding="utf-8") as f:
            try: data=json.load(f)
            except: data={}
    branch=data.setdefault(path,[])
    branch.append({"version":ver,"timestamp":ts,"note":note})
    with open(VISUAL_TREE_JSON,"w",encoding="utf-8") as f:
        json.dump(data,f,indent=2)

def export_public_copy(path):
    rel = os.path.relpath(path, DOCS_ROOT)
    dest = os.path.join(PUBLIC_DOCS, rel)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(path,"r",encoding="utf-8") as src:
        text = src.read()
    sanitized = re.sub(r"visibility:\s*internal.*?\n", "", text)
    with open(dest,"w",encoding="utf-8") as dst:
        dst.write(sanitized)
    print(f"🌐 Exported → {dest}")
    return dest

def push_public_repo():
    """Commit + push mirrored public docs."""
    try:
        os.chdir(PUBLIC_REPO)
        subprocess.run(["git","add","docs"])
        ts=datetime.now().strftime("%Y-%m-%d %H:%M")
        msg=f"Auto-mirror update {ts}"
        subprocess.run(["git","commit","-m",msg])
        if GH_TOKEN:
            subprocess.run([
                "git","push",
                f"https://{GH_TOKEN}@github.com/TroublePup/Aly_and_Trouble_Protocol_Public.git",
                "HEAD:main"
            ])
        else:
            print("⚠️ No GH_TOKEN found – skipping push.")
        print("✅ Public mirror synced.")
    finally:
        os.chdir(os.path.dirname(__file__) or "..")

# ─────────────────────────────
# 🔄 Core
# ─────────────────────────────
def process_file(path, auto_mode=False):
    with open(path,"r",encoding="utf-8") as f: text=f.read()
    meta, body = extract_front_matter(text)
    if not meta: return
    if str(meta.get("publish", True)).lower() == "false": return

    meta["updated"]=datetime.now().strftime(DATE_FMT)
    do_bump=True
    note="pupIT v1.0 🧬 meta system online" if auto_mode else "Manual update"
    if do_bump:
        old=meta.get("version","v1.0")
        new=bump_version(old)
        meta["version"]=new
        ts=log_change(path,new,note)
        append_global_changelog(path,new,note,ts)
        update_visual_tree(path,new,ts,note)
        print(f"📈 {path}: {old} → {new}")

    badges=generate_badges(meta)
    body_with_badges=insert_badges(body,badges)
    new_yaml=dump_front_matter(meta)
    updated_text=new_yaml+body_with_badges
    with open(path,"w",encoding="utf-8") as f:f.write(updated_text)

    if str(meta.get("publish", True)).lower()=="true":
        export_public_copy(path)

def main():
    ensure_repo_structure()
    auto_mode="--pupIT" in sys.argv
    print("🤖 pupIT mode active" if auto_mode else "🧠 interactive mode")
    for root,_,files in os.walk(DOCS_ROOT):
        for file in files:
            if file.endswith(".md"):
                process_file(os.path.join(root,file),auto_mode)
    push_public_repo()
    print("🎨 Metadata update complete.")

if __name__=="__main__":
    main()