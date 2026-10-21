# Literatur zu Referatsthemen

> [!IMPORTANT]
> **Die hier aufgeführte Literatur ist nur ein Einstieg – keine vollständige Quellenliste.**
>
> Es wird ausdrücklich **erwartet und erwünscht**, dass ihr eigenständig weiter recherchiert und die Literatur **erweitert**:
>
> - **Eigene Recherche:** Sucht nach weiteren, möglichst **aktuellen** Quellen (z. B. über Google Scholar, arXiv, Semantic Scholar oder direkt in den Proceedings großer Konferenzen wie **ACL / EMNLP** (ACL Anthology), **NeurIPS**, **ICML** oder **ICLR**).
> - **Wissenschaftliche Quellen bevorzugen:** Peer-reviewte Paper, Studien und offizielle Berichte haben Vorrang vor Blogposts oder Herstellerseiten.
> - **Kritisch prüfen:** Wer ist der Autor? Gibt es Interessenkonflikte (z. B. Hersteller über das eigene Produkt)? Wie aktuell ist die Quelle?
> - **Sauber belegen:** Alle verwendeten Quellen im Referat nachvollziehbar angeben.

## Übersicht

| Nr. | Thema                                                                                                                |
| --- | -------------------------------------------------------------------------------------------------------------------- |
| R1  | [Technologische Innovationsstrategien](#thema-r1-technologische-innovationsstrategien)                               |
| R2  | [Der Energiehunger von LLMs](#thema-r2-der-energiehunger-von-llms)                                                   |
| R3  | [LLM-Benchmarks im Überblick](#thema-r3-llm-benchmarks-im-überblick)                                                 |
| R4  | [Bias in LLMs](#thema-r4-bias-in-llms)                                                                               |
| R5  | [AI-Liebe im Digitalen Raum: AI-Companions](#thema-r5-ai-liebe-im-digitalen-raum-ai-companions)                      |
| R6  | [Vibe Coding](#thema-r6-vibe-coding)                                                                                 |
| R7  | [World Models](#thema-r7-world-models)                                                                               |
| R8  | [Sind LLMs Vorläufer einer AGI – oder eine Sackgasse?](#thema-r8-sind-llms-vorläufer-einer-agi--oder-eine-sackgasse) |

---

## Thema R1: Technologische Innovationsstrategien

**Wie unterscheiden sich EU, Asien und die USA bei der Entwicklung eigener LLMs und Infrastruktur?**

### Inhalte

- Vergleich der KI-Strategien von EU, USA und China/Asien (z. B. Regulierung, Förderung, nationale KI-Strategien)
- Investitionen in Rechenzentren, Chips und Energieinfrastruktur (z. B. Stargate-Projekt, Gigafactories)
- Rolle regionaler Foundation Models (z. B. Mistral, Qwen, Llama vs. proprietäre US-Modelle)
- Einfluss regulatorischer Rahmenbedingungen auf Innovationsgeschwindigkeit
- Geopolitische Abhängigkeiten (Chip-Exportkontrollen, Talentgewinnung, Cloud-Infrastruktur)

### Literatur

1. https://www.sciencedirect.com/science/article/pii/S2666954425000316
2. https://hai-production.s3.amazonaws.com/files/hai_ai_index_report_2025.pdf
3. https://www.researchgate.net/publication/391222042_A_Review_of_Large_Language_Models_LLMs_Development_A_Cross-Country_Comparison_of_the_US_China_Europe_UK_India_Japan_South_Korea_and_Canada
4. https://arxiv.org/html/2503.04745v1
5. https://eur-lex.europa.eu/eli/reg/2024/1689/oj \
   _EU AI Act, Primärquelle_
6. https://www.whitehouse.gov/wp-content/uploads/2025/07/Americas-AI-Action-Plan.pdf \
   _US AI Action Plan 2025_
7. https://digichina.stanford.edu/work/full-translation-chinas-new-generation-artificial-intelligence-development-plan-2017/ \
   _Chinas KI-Strategie, Übersetzung_

---

## Thema R2: Der Energiehunger von LLMs

**Die ökologische Bilanz von LLMs**

### Inhalte

- Energieverbrauch von Training vs. Inferenz (Sehr wichtig: Sehr aktuelle Studien/Statistiken einbeziehen)
- Technische Innovationen zur Reduktion des Energieverbrauchs (z. B. Quantisierung, effizientere Hardware, Drafter)
- CO2-Bilanz von Rechenzentren und Wasserverbrauch für Kühlung
- Vergleich verschiedener Modelle/Anbieter hinsichtlich Effizienz
- Ausblick: Wachstum des Energiebedarfs durch zunehmende KI-Nutzung

### Literatur

1. https://news.mit.edu/2025/explained-generative-ai-environmental-impact-0117
2. https://www.piie.com/blogs/realtime-economics/2024/ais-carbon-footprint-appears-likely-be-alarming
3. https://cloud.google.com/blog/products/infrastructure/measuring-the-environmental-impact-of-ai-inference?hl=en
4. https://www.nature.com/articles/s41598-024-76682-6
5. https://www.iea.org/reports/energy-and-ai \
   _IEA-Bericht "Energy and AI", 2025_
6. https://arxiv.org/abs/2505.09598 \
   _Jegham et al.: "How Hungry is AI?" – Energie, Wasser und CO2 der LLM-Inferenz, 2025_

---

## Thema R3: LLM-Benchmarks im Überblick

**Konzepte, Grenzen und Herausforderungen**

### Inhalte

- Überblick gängiger Benchmarks (MMLU, HumanEval, GSM8K, Chatbot Arena/lmarena)
- Unterschied zwischen statischen Benchmarks und Live-Arena-Rankings
- Probleme / Kritik an Benchmarking: Data Contamination, Overfitting auf Benchmarks, Sättigung
- Grenzen bei der Bewertung von Alltagstauglichkeit und Reasoning
- Alternative Bewertungsansätze (LLM-as-a-Judge, menschliche Evaluation)

### Literatur

1. https://arxiv.org/html/2508.15361v1
2. https://www.evidentlyai.com/llm-guide/llm-benchmarks
3. https://lmarena.ai/leaderboard
4. https://arxiv.org/abs/2403.04132 \
   _Chatbot-Arena-Paper_
5. https://neurips.cc/virtual/2025/loc/san-diego/poster/121845 \
   _"The Leaderboard Illusion" – Kritik an LM Arena, NeurIPS 2025_

---

## Thema R4: Bias in LLMs

**Technisches Problem oder einfach nur Spiegel gesellschaftlicher Ungleichheiten?**

### Inhalte

- Ursachen von Bias (Trainingsdaten, Annotation, RLHF)
- Arten von Bias (Gender, ethnisch, politisch/partisan)
- Beispiele und Studien zu politischem Bias verschiedener Modelle
- Methoden zur Messung und Reduktion von Bias
- Gesellschaftliche Implikationen und Verantwortung der Entwickler

### Literatur

1. https://www.nature.com/articles/s41598-025-14875-3
2. https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1558696/full
3. https://news.stanford.edu/stories/2025/05/ai-models-llms-chatgpt-claude-gemini-partisan-bias-research-study
4. https://arxiv.org/pdf/2405.13041
5. https://aclanthology.org/2024.cl-3.8/ \
   _Gallegos et al.: "Bias and Fairness in Large Language Models: A Survey", Computational Linguistics 2024_

---

## Thema R5: AI-Liebe im Digitalen Raum: AI-Companions

### Inhalte

- Funktionsweise von AI-Companion-Apps (z. B. Replika, Character.AI)
- Beliebtheit, Akzeptanz und Nutzungsmuster (Demografie, Nutzungsdauer, Interaktionshäufigkeit)
- Finanzierung, Umsatzstatistiken und Monetarisierungsstrategien
- Psychologische und soziale Auswirkungen (Einsamkeit, Bindung, Abhängigkeit)
- Ethische Fragestellungen (Manipulation, vulnerable Nutzergruppen, Minderjährige)

### Literatur

1. https://www.adalovelaceinstitute.org/blog/ai-companions/
2. https://arxiv.org/abs/2509.11391
3. https://arxiv.org/html/2502.20231v1
4. https://huggingface.co/datasets/lmsys/toxic-chat
5. https://link.springer.com/article/10.1007/s12599-025-00955-1
6. https://scale.stanford.edu/ai/repository/how-ai-and-human-behaviors-shape-psychosocial-effects-chatbot-use-longitudinal \
   _MIT Media Lab & OpenAI: Längsschnitt-RCT zu psychosozialen Effekten von Chatbot-Nutzung_
7. https://arxiv.org/abs/2407.19096 \
   _De Freitas et al.: "AI Companions Reduce Loneliness"_
8. https://www.ftc.gov/news-events/news/press-releases/2025/09/ftc-launches-inquiry-ai-chatbots-acting-companions \
   _FTC-Untersuchung zu AI-Companions, 2025_

---

## Thema R6: Vibe Coding

**Technischer Hintergrund, Möglichkeiten und Herausforderungen**

### Inhalte

- Wie funktioniert ein Coding-Agent grundlegend? (LLM + Tool-Integration, z. B. IDE, Compiler, Debugger)
- Definition und Konzept: Programmieren durch natürlichsprachliche Prompts
- Verbreitete Tools (GitHub Copilot, Cursor, Claude Code u. a.)
- Chancen
- Risiken: Sicherheitslücken, mangelndes Codeverständnis, Qualitätsprobleme
- Auswirkungen auf Berufsbild und Ausbildung von Softwareentwicklern

### Literatur

1. https://www.ibm.com/think/topics/vibe-coding
2. https://github.com/features/copilot
3. https://arxiv.org/pdf/2507.21928
4. https://www.heise.de/hintergrund/Vibe-Coding-Wie-KI-komplette-Software-erstellt-10482241.html
5. https://www.handelsblatt.com/technik/ki/kuenstliche-intelligenz-dieses-risiko-birgtvibe-coding-fuer-die-it-sicherheit/100116588.html
6. https://cacm.acm.org/news/catching-the-vibe-of-vibe-coding/
7. https://arxiv.org/abs/2507.09089 \
   _METR: Produktivitätsstudie mit erfahrenen Open-Source-Entwicklern, 2025_
8. https://arxiv.org/abs/2310.06770 \
   _SWE-bench – Evaluation von Coding-Agents_
9. https://arxiv.org/abs/2509.16941 \
   _SWE-Bench Pro – Long-Horizon-Aufgaben für Coding-Agents, 2025_

---

## Thema R7: World Models

**Konzepte, physikalisches Weltverständnis und Wege zu autonomen KI-Systemen**

### Inhalte

- Konzept "World Model" im Vergleich zum klassischen LLM (physikalisches/räumliches Verständnis)
- Aktuelle Ansätze (z. B. Genie, JEPA, Sora als Weltmodell)
- Unterschied zwischen Simulation der Welt und reiner Textvorhersage
- Anwendungsfelder: Robotik, autonome Systeme, Simulation

### Literatur

1. https://arxiv.org/abs/1803.10122
2. https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/
3. https://arxiv.org/abs/2603.19312
4. https://www.derstandard.de/story/3000000315485/sind-grosse-sprachmodelle-eine-sackgasse-und-world-models-die-loesung
5. https://time.com/article/2026/07/15/world-models-are-ai-s-next-frontier/
6. https://openreview.net/pdf?id=BZ5a1r-kVsf \
   _LeCun: "A Path Towards Autonomous Machine Intelligence" – Grundlage JEPA_

---

## Thema R8: Sind LLMs Vorläufer einer AGI – oder eine Sackgasse?

### Inhalte

- Definition(en) von AGI und Abgrenzung zu heutigen LLMs
- Argumente für LLMs als Weg zu AGI (Skalierungshypothese)
- Argumente dagegen (fehlendes echtes Verständnis, Reasoning-Grenzen, Halluzinationen)
- Positionen großer Akteure (z. B. OpenAI, DeepMind)
- Gesellschaftliche und ethische Implikationen einer möglichen AGI
- Einordnung / Kritik an existierenden Benchmarks (z.B. ARC-AGI)

### Literatur

1. https://www.ibm.com/think/topics/artificial-general-intelligence
2. https://openai.com/index/planning-for-agi-and-beyond/
3. https://www.heise.de/en/news/General-artificial-intelligence-OpenAI-s-definition-has-a-price-tag-10220909.html
4. https://link.springer.com/content/pdf/10.1007/s43681-023-00268-7.pdf
5. https://www.heise.de/news/OpenAI-stellt-GPT-6-Astra-vor-Mehr-Intelligenz-und-AGI-Raunen-11440778.html
6. https://arxiv.org/abs/2311.02462 \
   _Google DeepMind: "Levels of AGI"_
7. https://arxiv.org/abs/2001.08361 \
   _Kaplan et al.: Scaling Laws – Basis der Skalierungshypothese_
8. https://machinelearning.apple.com/research/illusion-of-thinking \
   _Apple: "The Illusion of Thinking" – Grenzen von Reasoning-Modellen_
