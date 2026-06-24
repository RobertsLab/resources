# Corrections / suggestions — Google Form setup

The explorer has a **"✎ Suggest a correction"** button in every sample and orphan detail view.
It opens a Google Form with the identifying fields prefilled, so viewers only type the actual
correction. Responses collect in a Google Sheet you triage, then fold accepted changes back into
the databank. This takes ~10 minutes to wire up once.

## 1. Create the Form

At [forms.google.com](https://forms.google.com) make a form ("Histology Databank — Corrections")
with these questions, in this order:

| # | Question | Type | Notes |
|---|----------|------|-------|
| 1 | Sample / image ID | Short answer | prefilled |
| 2 | Species | Short answer | prefilled |
| 3 | Where (sample or orphan) | Short answer | prefilled |
| 4 | Image / folder reference | Short answer | prefilled |
| 5 | Type of correction | Multiple choice | e.g. Wrong sample/label · Wrong tissue · This orphan = sample X · Image quality · Other |
| 6 | Your correction / note | Paragraph | the actual suggestion |
| 7 | Your name or email | Short answer | optional, for follow-up |

Questions 1–4 are the ones the button fills in automatically.

## 2. Get the prefill link + field IDs

In the Form editor: **⋮ (top right) → Get pre-filled link**. Type any placeholder text into
questions 1–4 (e.g. `AAA`, `BBB`, `CCC`, `DDD`), then **Get link** and **Copy link**.

The copied URL looks like:

```
https://docs.google.com/forms/d/e/1FAIpQLSxxxx/viewform?usp=pp_url
  &entry.1111111111=AAA
  &entry.2222222222=BBB
  &entry.3333333333=CCC
  &entry.4444444444=DDD
```

- The part **before** `&entry...` (ending in `viewform?usp=pp_url`) is your **formBase**.
- Each `entry.NNNNNNNNNN` is the field ID for that question, matched by the placeholder you typed.

## 3. Paste into the explorer

Open `index.html`, find the `FEEDBACK` block near the top of the `<script>`, and fill it in:

```js
const FEEDBACK = {
  formBase: "https://docs.google.com/forms/d/e/1FAIpQLSxxxx/viewform?usp=pp_url",
  fields: {
    sampleId: "entry.1111111111",   // the placeholder you used for "Sample / image ID" (AAA)
    species:  "entry.2222222222",   // Species (BBB)
    source:   "entry.3333333333",   // Where (CCC)
    context:  "entry.4444444444",   // Image / folder reference (DDD)
  },
};
```

Match each `entry.` ID to the right question by the placeholder text. Save, reload the page,
open any sample, and click **✎ Suggest a correction** — the form should open with fields filled.

Until `formBase` is set, the button still appears but shows a "not set up yet" note.

## 4. The triage loop

1. Form responses land in a linked Google Sheet (**Responses → View in Sheets**).
2. Review them; for accepted changes, edit `build/histology_databank.csv` (or your live databank
   Sheet, then re-export to that CSV).
3. Re-run `python3 build_index.py` and redeploy. Orphan → sample reclassifications are the
   highest-value fixes; each one moves an image out of the "Unmatched" backlog.

Tip: add a "Status" column (new / accepted / applied / rejected) to the responses sheet so you can
track what's been folded in.
