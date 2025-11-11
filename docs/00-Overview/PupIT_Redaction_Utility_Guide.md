---
title: PupIT Redaction Utility Guide
phase: Documentation
cycle: Meta
node: PupIT_System
status: Reference
visibility: internal
publish: true
updated: '2025-11-11'
version: v2.5
---

<!-- BADGES_START -->
![phase](https://img.shields.io/badge/phase-Documentation-red)
![cycle](https://img.shields.io/badge/cycle-Meta-pink)
![node](https://img.shields.io/badge/node-PupIT_System-green)
![status](https://img.shields.io/badge/status-Reference-purple)
<!-- BADGES_END -->

# 🧼 PupIT Document Redaction Utility  
*`scripts/redact_doc.py` — v2.3 (with summary reporting)*

---

## ✅ Behavior Summary

| Mode | Action | Prompts |
|:-----|:--------|:---------|
| *(no flag)* | Read-only; will **never** edit or delete anything | Warns: 🚫 Skipping interactive flag updates — requires `--pupIT` mode |
| `--pupIT` | Full edit power; asks once per file: “Do you want to set publish: false and redact this file?” | If ‘Y’, it flips the flag → redacts → pushes |
| `--pupIT --dry-run` | Same as above, but **no writes** (preview only) | — |

> ⚠️  Without `--pupIT`, the script will **never** modify or delete files.  
> It can only read and report — no exceptions.

---

## 🧩 Example Usage

```bash
python3 scripts/redact_doc.py docs/10-Phases/Phase_M_Micro_Phases.md docs/10-Phases/timeline.md --pupIT --dry-run
```

### Example Output
```bash
📦 Archived: docs/10-Phases/Phase_M_Micro_Phases.md → /Users/codyteunisse/Projects/Aly_and_Trouble_Protocol_Public/data/redacted_archive/docs_10-Phases_Phase_M_Micro_Phases.md_20251111_015000.bak
🗑️  Redacted: docs/10-Phases/Phase_M_Micro_Phases.md
✅ Already redacted: docs/10-Phases/timeline.md

────────────────────────────
✅ Redacted: 2
⏭️  Skipped: 1
🚫 Already redacted: 3
⚠️  Errors: 0
────────────────────────────
```

---

## 🧠 Design Philosophy

The PupIT Redaction Utility ensures safe, transparent document removal between internal and public repositories.

### It automatically:
- Archives redacted files under /data/redacted_archive/ before deletion
- Modifies YAML frontmatter (publish: false) when authorized
- Deletes public copies only after confirmation
- Records all changes via commit messages and summary reports

## 🧩 Script Header

```python
#!/usr/bin/env python3
"""
redact_doc.py — PupIT Safe Redaction Utility v2.3 🧼
Read-only by default. Only --pupIT mode can modify YAML or perform redaction.
Adds per-batch summary reporting for clarity.
"""
```
### Key Features
- ✏️ Updates publish: flag safely
- 📦 Archives redacted files with timestamps
- 🗑️ Removes public copies on confirmation
- 🚀 Optional --push auto-commits and syncs to remote
- 📊 Summary footer (Redacted / Skipped / Already / Errors)

## 🧩 Safety Defaults
- Redaction always archives first (unless --no-archive is used)
- --dry-run prevents any filesystem or git changes
- Requires --pupIT for any modification (hard safeguard)
- Pushes to origin/main automatically if --push is enabled
- Logs clear summary at completion

---

## 🐾 Example Workflow

1. Mark files for review with publish: true
2.	Decide which should be removed from the public repo
3.	Run:
    ```bash
    python3 scripts/redact_doc.py docs/10-Phases/*.md --pupIT --push
    ```
4.	Confirm per-file prompts (or use --dry-run to preview)
5.	Verify results:
- Archived under /data/redacted_archive/
- Deleted from /docs/
- Summary block confirms actions taken
  
## 🧾 Example Commit Message
```bash
   redact: docs/10-Phases/Phase_M_Micro_Phases.md via PupIT secure redaction
```

---

## 🧩 Roadmap (Future Enhancements)

- Add restore_doc.py for safe un-redaction
- Support batch YAML reclassification (visibility: public/internal)
- Option for auto-redaction of expired public documents based on updated: field

--- 

Maintainer: Trouble Pup 🐾
Automation: PupIT v1.0 — Meta System Online
Repository: Aly_and_Trouble_Protocol