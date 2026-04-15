# Manual Annotation Codebook

A condensed reference for the workshop. The full codebook (with every category and edge case) is distributed alongside the PSoGA database on Harvard Dataverse.

## 1. Unit of analysis

The **natural sentence** — linguistically coherent and replicable across languages. Lists and bullet points are treated as standalone sentences.

## 2. Three coding decisions per sentence

For each sentence, record:

1. **Group detection** — Is a social group overtly mentioned? If yes, capture the **full span including all modifiers** (e.g. *"young women in rural areas"*, not just *"women"*).
2. **Stance** — `Positive` / `Negative` / `Neutral` toward the target group (not the overall sentiment of the sentence).
3. **Policy link** — `Yes` / `No`: is a concrete policy (pledge, record, or criticism) directed at the group present?

If multiple groups appear in one sentence, record each separately with its own stance and policy label. Intersectional groups are assigned to multiple meaningful group categories.

## 3. What counts as a social group

> **Definition.** A segment of society or collection of people sharing common socio-demographic traits — ascriptive and/or acquired (sex, age, ethnicity, religion, residence, education, occupation, etc.). *(Huber & Dolinsky 2023)*

**Included** — workers, elderly, women, students, migrants, religious communities, farmers, intersectional groupings ("young women", "low-income families"), groupings within organisations (police officers, union members).

**Excluded** — organised entities (trade unions, corporations, state authorities), political-ideology / opinion groups ("conservatives", "activists"), party affiliations ("Labour voters", "Republicans"), broad unspecific terms ("everyone", "all", "people" without a modifier).

> **Key test.** Does the group share socio-demographic traits — not just beliefs or organisational membership?

## 4. Common challenges

| Situation | Rule |
|---|---|
| **General terms** | Code only if a modifier specifies a defined grouping. ✓ "ordinary people", "people in rural areas" — ✗ "We will help people". |
| **Relational references** | "their families", "their patients" relative to a primary group → **do not** record as independent groups. |
| **Group inside a law title or party name** | e.g. *"Workers' Party"* → code as **Neutral** stance, **no policy**. |
| **Policy without overt group mention** | If the group is not explicitly named, **do not code** the appeal — even if the policy clearly targets them. |
| **Criticism of a rival party's policy** | Record stance toward the **group mentioned in the rival's policy**, not toward the rival party. |

## 5. Worked examples

1. *"…legislate to tackle hate crimes against people with a disability."* (Fianna Fáil, 2020)
   - Group: **people with a disability** · Stance: **Positive** · Policy: **Yes**
2. *"The rich are getting richer whilst everyone else struggles to make ends meet."* (UK Greens, 2019)
   - Group: **the rich** · Stance: **Negative** · Policy: **No**
3. *"The Conservative Party's policy of tax cuts has favoured the rich at the expense of the struggling working class."*
   - Group 1: **the rich** · Negative · Policy: Yes
   - Group 2: **the working class** · Positive · Policy: No

## 6. Building a corpus

1. **Source selection** — manifestos, speeches, social media, news; consider language(s).
2. **Sentence parsing** — split into natural sentences; treat list items as standalone.
3. **Guidelines** — operationalise concepts with examples for every decision; pilot-test with coders.
4. **Platform** — INCePTION, Doccano, or Label Studio.
5. **Inter-rater reliability** — target Krippendorff's α ≥ 0.8; review disagreements; update guidelines; re-annotate.

See [`group_categories.md`](group_categories.md) for the 43 meaningful group categories.
