# Run log — after_max_chunks

- Produced by: `run_eval.py::main`
- Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`
- Corpus: `city_guides` (index variant `default`)
- top-k: 98 · relevance cutoff: 0.5
- Runs per question: 3, caching off
- When: 2026-09-28 15:28

This table is one row per QUESTION. The run log your README asks for is
one row per CRITERION, so aggregate these into it — criterion 1 is how many
of your questions had the answer in the retrieved chunks, and so on.

| Question | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| What town is the easiest to walk in for those who require accessibility? | fail | fail | fail |
| What is Elder Ness? | fail | fail | fail |
| Which towns have a hospital and what times are they open? | fail | fail | fail |
| If any, where are the grocery stores? | fail | fail | fail |
| Where does the name of the town Elder ness originate from? | fail | fail | fail |

---

## The relevance gate on out-of-corpus questions

Produced by `run_eval.py::check_out_of_scope`, cutoff 0.5. Refused 5 of 5.

Retrieval is deterministic and the gate is a comparison against a
fixed number, so these do not vary between runs — one pass over the
list is the whole measurement.

| Out-of-scope question | Best distance | Gate |
|---|---|---|
| What is the capital of Mongolia? | 0.754 | refused |
| How do I change the oil in a diesel engine? | 0.889 | refused |
| Who won the 1994 World Cup? | 0.899 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.838 | refused |
| How do I write a for loop in Rust? | 0.838 | refused |

---

## Real output

This is what the system actually produced. Paste the relevant parts
into your README underneath the table — the rubric asks for real
output as text, not a description of it.

### What town is the easiest to walk in for those who require accessibility? — run 1

- Best distance: 0.4984 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_corry_vale.md, guide_eating.md, guide_elder_ness.md, guide_givens_mill.md, guide_halden_bay.md, guide_kestrelford.md, guide_marchwood.md, guide_pellew_sands.md, guide_regional_transport.md, guide_seasons.md, guide_thornby_wells.md, guide_walking.md

```
Based on the provided documents, Thornby Wells is the easiest town in the region for walking and accessibility, as it is flat, compact, and everything is level and within three minutes of everything else. 

This information comes from `guide_accessibility.md` and `guide_thornby_wells.md`.
```

### What town is the easiest to walk in for those who require accessibility? — run 2

- Best distance: 0.4984 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_corry_vale.md, guide_eating.md, guide_elder_ness.md, guide_givens_mill.md, guide_halden_bay.md, guide_kestrelford.md, guide_marchwood.md, guide_pellew_sands.md, guide_regional_transport.md, guide_seasons.md, guide_thornby_wells.md, guide_walking.md

```
Thornby Wells is the region's most accessible town on foot, described as flat, compact, and having level streets and gardens. 

Source: guide_accessibility.md and guide_walking.md
```

### What town is the easiest to walk in for those who require accessibility? — run 3

- Best distance: 0.4984 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_corry_vale.md, guide_eating.md, guide_elder_ness.md, guide_givens_mill.md, guide_halden_bay.md, guide_kestrelford.md, guide_marchwood.md, guide_pellew_sands.md, guide_regional_transport.md, guide_seasons.md, guide_thornby_wells.md, guide_walking.md

```
According to `guide_accessibility.md`, Thornby Wells is the easiest town in the region for accessibility, featuring flat, level streets and gardens where everything is within three minutes.
```

### What is Elder Ness? — run 1

- Best distance: 0.1876 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_corry_vale.md, guide_eating.md, guide_elder_ness.md, guide_givens_mill.md, guide_halden_bay.md, guide_kestrelford.md, guide_marchwood.md, guide_pellew_sands.md, guide_regional_transport.md, guide_seasons.md, guide_thornby_wells.md, guide_walking.md

```
Elder Ness is a headland with a village of 300 people, a lighthouse, a bird observatory, and very little else. People visit for birds, walking, or a deliberate absence of things to do.

Source: `guide_elder_ness.md`
```

### What is Elder Ness? — run 2

- Best distance: 0.1876 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_corry_vale.md, guide_eating.md, guide_elder_ness.md, guide_givens_mill.md, guide_halden_bay.md, guide_kestrelford.md, guide_marchwood.md, guide_pellew_sands.md, guide_regional_transport.md, guide_seasons.md, guide_thornby_wells.md, guide_walking.md

```
Elder Ness is a headland with a village of 300 people, a lighthouse, a bird observatory, and very little else. People visit for birds, walking, or a deliberate absence of things to do.

Source: `guide_elder_ness.md`
```

### What is Elder Ness? — run 3

- Best distance: 0.1876 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_corry_vale.md, guide_eating.md, guide_elder_ness.md, guide_givens_mill.md, guide_halden_bay.md, guide_kestrelford.md, guide_marchwood.md, guide_pellew_sands.md, guide_regional_transport.md, guide_seasons.md, guide_thornby_wells.md, guide_walking.md

```
Elder Ness is a headland featuring a village of 300 residents, a lighthouse, a bird observatory, and very little else. 

Source: guide_elder_ness.md
```

### Which towns have a hospital and what times are they open? — run 1

- Best distance: 0.4897 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_corry_vale.md, guide_eating.md, guide_elder_ness.md, guide_givens_mill.md, guide_halden_bay.md, guide_kestrelford.md, guide_marchwood.md, guide_pellew_sands.md, guide_regional_transport.md, guide_seasons.md, guide_thornby_wells.md, guide_walking.md

```
The nearest full hospital is in Marchwood. Brightwater also has a hospital, while Kestrelford, Halden Bay, Corry Vale, Givens Mill, and Elder Ness have minor injuries units with limited hours or nothing at all. 

Source: guide_accessibility.md
```

### Which towns have a hospital and what times are they open? — run 2

- Best distance: 0.4897 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_corry_vale.md, guide_eating.md, guide_elder_ness.md, guide_givens_mill.md, guide_halden_bay.md, guide_kestrelford.md, guide_marchwood.md, guide_pellew_sands.md, guide_regional_transport.md, guide_seasons.md, guide_thornby_wells.md, guide_walking.md

```
Based on the documents provided:

- **Marchwood** is the location of the nearest full hospital. (Source: `guide_accessibility.md`)
- **Brightwater** also has a hospital, while Kestrelford, Halden Bay, Corry Vale, Givens Mill, and Elder Ness have minor injuries units with limited hours or nothing at all. (Source: `guide_accessibility.md`)

The documents do not state the operating hours of these hospitals.
```

### Which towns have a hospital and what times are they open? — run 3

- Best distance: 0.4897 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_corry_vale.md, guide_eating.md, guide_elder_ness.md, guide_givens_mill.md, guide_halden_bay.md, guide_kestrelford.md, guide_marchwood.md, guide_pellew_sands.md, guide_regional_transport.md, guide_seasons.md, guide_thornby_wells.md, guide_walking.md

```
The nearest full hospital is in Marchwood. Brightwater has a hospital, while Kestrelford, Halden Bay, Corry Vale, Givens Mill, and Elder Ness have minor injuries units with limited hours or nothing at all. 

Source: `guide_accessibility.md`
```

### If any, where are the grocery stores? — run 1

- Best distance: 0.5997 (refused by the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_corry_vale.md, guide_eating.md, guide_elder_ness.md, guide_givens_mill.md, guide_halden_bay.md, guide_kestrelford.md, guide_marchwood.md, guide_pellew_sands.md, guide_regional_transport.md, guide_seasons.md, guide_thornby_wells.md, guide_walking.md

```
I don't have enough information about that.
```

### If any, where are the grocery stores? — run 2

- Best distance: 0.5997 (refused by the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_corry_vale.md, guide_eating.md, guide_elder_ness.md, guide_givens_mill.md, guide_halden_bay.md, guide_kestrelford.md, guide_marchwood.md, guide_pellew_sands.md, guide_regional_transport.md, guide_seasons.md, guide_thornby_wells.md, guide_walking.md

```
I don't have enough information about that.
```

### If any, where are the grocery stores? — run 3

- Best distance: 0.5997 (refused by the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_corry_vale.md, guide_eating.md, guide_elder_ness.md, guide_givens_mill.md, guide_halden_bay.md, guide_kestrelford.md, guide_marchwood.md, guide_pellew_sands.md, guide_regional_transport.md, guide_seasons.md, guide_thornby_wells.md, guide_walking.md

```
I don't have enough information about that.
```

### Where does the name of the town Elder ness originate from? — run 1

- Best distance: 0.2798 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_corry_vale.md, guide_eating.md, guide_elder_ness.md, guide_givens_mill.md, guide_halden_bay.md, guide_kestrelford.md, guide_marchwood.md, guide_pellew_sands.md, guide_regional_transport.md, guide_seasons.md, guide_thornby_wells.md, guide_walking.md

```
I do not have enough information in the provided documents to explain where the name of the town Elder Ness originates.
```

### Where does the name of the town Elder ness originate from? — run 2

- Best distance: 0.2798 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_corry_vale.md, guide_eating.md, guide_elder_ness.md, guide_givens_mill.md, guide_halden_bay.md, guide_kestrelford.md, guide_marchwood.md, guide_pellew_sands.md, guide_regional_transport.md, guide_seasons.md, guide_thornby_wells.md, guide_walking.md

```
I do not have enough information to answer where the name Elder Ness originates from. 

Source: guide_elder_ness.md
```

### Where does the name of the town Elder ness originate from? — run 3

- Best distance: 0.2798 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_corry_vale.md, guide_eating.md, guide_elder_ness.md, guide_givens_mill.md, guide_halden_bay.md, guide_kestrelford.md, guide_marchwood.md, guide_pellew_sands.md, guide_regional_transport.md, guide_seasons.md, guide_thornby_wells.md, guide_walking.md

```
I don't have enough information in the provided documents to explain where the name of the town Elder Ness originates.
```
