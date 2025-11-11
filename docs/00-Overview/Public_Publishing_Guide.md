---
title: Public Publishing Guide
phase: Documentation
cycle: Meta
node: PupIT_System
status: Reference
visibility: public
publish: true
updated: 2025-11-10
version: v1.0
---

<!-- BADGES_START -->
![phase](https://img.shields.io/badge/phase-Documentation-red?style=flat-square)
![cycle](https://img.shields.io/badge/cycle-Meta-pink?style=flat-square)
![node](https://img.shields.io/badge/node-PupIT_System-green?style=flat-square)
![status](https://img.shields.io/badge/status-Reference-purple?style=flat-square)
![visibility](https://img.shields.io/badge/visibility-Public-blue?style=flat-square)
<!-- BADGES_END -->

# 🌐 Public Publishing Guide  
*For the Aly × Trouble Protocol Repositories*

---

## 🧭 Purpose

This guide defines how internal documentation is mirrored to the public repository  
**`Aly_and_Trouble_Protocol_Public`** through the **PupIT** automation system.

Each file contains YAML *frontmatter* that controls its visibility and publishing behavior.

---

## 🧩 Publishing Fields

| Field | Example | Meaning | Action |
|:------|:--------|:--------|:-------|
| **visibility** | `public` | Human-readable flag describing the intended audience (`public` or `internal`) | For clarity and documentation hygiene |
| **publish** | `true` | Controls whether the file is exported to the public mirror | PupIT uses this field to determine export eligibility |

---

## 🧬 Examples

### ✅ Public-Facing File

``` yaml
---
title: Phase 1 — Aly Rising Overview
phase: Apollo_Rising
cycle: Aly_Rising
node: Secure_Agent
status: Released
visibility: public
publish: true
updated: 2025-11-10
---
```

#### Result:

- Exported to /Aly_and_Trouble_Protocol_Public/docs/10-Phases/Phase_1_Aly_Rising.md
- Included in public changelogs and version trees.

### 🚫 Internal-Only File

``` yaml
---
title: Phase 1 — Aly Rising Overview
phase: Apollo_Rising
cycle: Aly_Rising
node: Secure_Agent
status: Released
visibility: public
publish: true
updated: 2025-11-10
---
```

#### Result:
- Remains private and versioned internally.
- Not exported or mirrored publicly.
- Still logged in internal changelogs and version history.

## 🧠 Recommended Defaults by Folder

| Folder | Default publish | Visibility | Purpose |
|:-------|:----------------|:-----------|:--------|
**🌐 docs/00-Overview/**|✅ true|public|Overview, mission, and project documentation|**🧬 docs/10-Phases/**|🟡 Mixed|public or internal|Phase summaries public; dosing & methods private|**⚗️ docs/20-Compounds/**|🚫 false|internal|Compound formulations, actives, and notes|**📊 docs/30-Tracking/**|🚫 false|internal|Quantitative tracking, metrics, visualizations|**💭 docs/40-Reflection/**|🚫 false|internal|Personal reflections and creative logs|**🗄️ data/**|🚫 false|internal|Analytics, changelogs, and serialized datasets|

***💡 Tip:
Default to private first, then promote to public once peer-reviewed and finalized.

## 🐾 PupIT Behavior Summary

| Step | Action | Result |
|:-----|:-------|:-------|
|1️⃣|Scans all .md files under /docs|Detects all Markdown files for evaluation|2️⃣|Reads YAML frontmatter|Extracts metadata and publishing flags|3️⃣|Filters for publish: true|Determines which docs qualify for export|4️⃣|Exports matching files to public repo|Mirrors sanitized copies into /|Aly_and_Trouble_Protocol_Public/docs/|5️⃣|Commits & timestamps changes|Auto-generates commit messages with version and time|6️⃣|Pushes to GitHub via secure token|Syncs to the public repository using GH_TOKEN|7️⃣|Updates local changelogs & version tree|Maintains versioning continuity internally|8️⃣|Prints final summary in console|Confirms exported files and completion status|

✨ Best Practices
	•	Use visibility: public and publish: true for educational, conceptual, or aesthetic material.
	•	Use publish: false for content with compounds, lab data, or sensitive logs.
	•	Always include updated: and version: fields for clear version history.
	•	Label intended audience in YAML frontmatter.
	•	Name internal drafts as Draft_*.md and public releases as Public_*.md.
	•	Review all public files before running --pupIT mode.
	•	Remember: once mirrored, files are public instantly.

---

🧩 Example Publishing Workflow
	1.	Draft a new doc in /docs/10-Phases/
	2.	Keep publish: false until internal review
	3.	Set visibility: public and publish: true once finalized
	4.	Run:
    ```python
    python3 scripts/update_docs_meta.py --pupIT
    ```
	5.	Verify mirror update in: https://github.com/TroublePup/Aly_and_Trouble_Protocol_Public￼

Maintainer: Trouble Pup 🐾
Automation: PupIT v1.0 — meta system online
Repository: Aly_and_Trouble_Protocol

---

✅ **Visual Fixes in this Version:**
- Code blocks are wrapped in **```yaml** fences (not plain text).
- The extra “Code block:” lines are removed (they break rendering).
- The triple `---` frontmatter inside the YAML examples stays **inside** the fences.
- List items render correctly with `-` instead of tabs.