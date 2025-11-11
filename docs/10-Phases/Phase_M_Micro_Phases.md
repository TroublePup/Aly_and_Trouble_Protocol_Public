---
title: Micro-Phases Reference
phase: Meta
cycle: Sub_Phase_Map
node: Secure_Agent
status: Stable
visibility: internal
publish: true
updated: '2025-11-11'
version: v1.1
---
<!-- BADGES_START -->
![phase](https://img.shields.io/badge/phase-Meta-red)
![cycle](https://img.shields.io/badge/cycle-Sub_Phase_Map-pink)
![node](https://img.shields.io/badge/node-Secure_Agent-green)
![status](https://img.shields.io/badge/status-Stable-purple)
<!-- BADGES_END -->

---

# 🧬 Micro-Phases Reference

Micro-phases provide finer control within each major stage of the **Aly × Trouble Protocol**,  
allowing small hormonal, behavioral, and emotional adjustments between macro transitions.  
Each sub-phase has its own tone, duration, and symbolic rhythm — together, they make each cycle feel alive and adaptive.

---

## 🩸 Overview Table

| **Macro Phase** | **Micro-Phase** | **Approx. Duration** | **Intent / Focus** | **Serum Targets (E2/T)** | **Keywords / Tone** |
|------------------|-----------------|----------------------|--------------------|---------------------------|----------------------|
| **BreakOut** | *Reset* | 3–5 days | Detox, restore circadian rhythm | E2 < 30 pg/mL / T baseline | Clarity • discipline • purging |
|  | *Ignite* | 7–10 days | Activate mitochondria & peptides | E2 < 40 pg/mL / T baseline | Energy • renewal • focus |
| **Aly Rising** | *Soft Bloom* | 5–7 days | Introduce estradiol, emotional openness | E2 70–100 pg/mL / T < 400 ng/dL | Warmth • receptivity |
|  | *Entrainment* | 7–10 days | Stabilize rhythm & mood | E2 100–120 pg/mL / T 300–400 ng/dL | Balance • connection |
| **Aly Core** | *Liminal* | 7–10 days | Deep immersion, sensual embodiment | E2 120–160 pg/mL / T 250–350 ng/dL | Intimacy • stillness |
|  | *Eclipse* | 7–10 days | Quiet integration, emotional reflection | E2 100–140 pg/mL / T 250–400 ng/dL | Glow • reflection |
| **Trouble Rising** | *Reclaim* | 7–10 days | Controlled androgen ramp, focus | E2 40–80 pg/mL / T 500–700 ng/dL | Motion • assertion |
|  | *Anchor* | 7–10 days | Temper strength with awareness | E2 45–75 pg/mL / T 600–750 ng/dL | Center • discipline |
| **Trouble Core** | *Forge* | 10–14 days | Build & consolidate muscle | E2 35–60 pg/mL / T 700–900 ng/dL | Power • service |
|  | *Crown* | 10–14 days | Lead with integrated confidence | E2 35–60 pg/mL / T 700–850 ng/dL | Leadership • devotion |
| **Refine & Recycle** | *Unwind* | 7 days | Recovery & introspection | E2 40–70 pg/mL / T 400–500 ng/dL | Rest • gratitude |
|  | *Seed* | 7–10 days | Prepare biologically & emotionally for next Aly loop | E2 50–80 pg/mL / T 350–450 ng/dL | Renewal • anticipation |

---

## 🧭 Using the `sub_phase` Field

Each phase document includes a `sub_phase:` tag in its YAML front-matter.  
Example:

```yaml
---
title: Phase 2 – Aly Core
phase: Aly_Core
sub_phase: Aly_Liminal
cycle: Deep_Immersion
node: Secure_Agent
status: Active
visibility: internal
publish: true
updated: 2025-11-12
---
### Badge example:

| **Badge** | **Rendered Example** | **Meaning** |
|------------|----------------------|--------------|
| **phase** | ![phase](https://img.shields.io/badge/phase-Apollo_Rising-red) | Hormonal or metabolic focus — e.g., `Apollo`, `Aly`, `Trouble` |
| **sub_phase** | ![sub_phase](https://img.shields.io/badge/sub_phase-Aly_Liminal-rose) | Micro-phase refinement within a major phase |
| **cycle** | ![cycle](https://img.shields.io/badge/cycle-Aly_Rising-pink) | Current sub-cycle or feminization phase |
| **node** | ![node](https://img.shields.io/badge/node-Secure_Agent-green) | Identity of the protocol operator / subject |
| **status** | ![status](https://img.shields.io/badge/status-Experimental-purple) | Development or review maturity |

## 🧠 Practical Applications
	•	Dose Tuning: micro-phases define micro-dosing or tapering windows for smooth transitions.
	•	Psychological Framing: each name signals a mindset cue — “Liminal” ≈ receptive stillness; “Forge” ≈ deliberate output.
	•	Data Analytics: sub-phase labels can be parsed by /data/analytics/ scripts to graph serum changes with emotional tone.
	•	Automation: Home Assistant or Notion can sync phase start/end triggers based on sub-phase duration data.

⸻

## 🪞 Reflection Mantra

“Transformation is not one leap — it’s a hundred quiet adjustments,
each small enough to listen, yet powerful enough to change the story.”
