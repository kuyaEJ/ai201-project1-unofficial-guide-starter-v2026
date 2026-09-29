# Run log — secondafter

- Produced by: `run_eval.py::main`
- Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`
- Corpus: `city_guides` (index variant `default`)
- top-k: 37 · relevance cutoff: 0.5
- Runs per question: 3, caching off
- When: 2026-09-27 22:54

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
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_corry_vale.md, guide_elder_ness.md, guide_givens_mill.md, guide_halden_bay.md, guide_kestrelford.md, guide_marchwood.md, guide_pellew_sands.md, guide_regional_transport.md, guide_thornby_wells.md, guide_walking.md

```
According to `guide_accessibility.md`, Thornby Wells is the easiest town in the region for those with limited mobility, as it is flat, compact, and level throughout.
```

### What town is the easiest to walk in for those who require accessibility? — run 2

- Best distance: 0.4984 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_corry_vale.md, guide_elder_ness.md, guide_givens_mill.md, guide_halden_bay.md, guide_kestrelford.md, guide_marchwood.md, guide_pellew_sands.md, guide_regional_transport.md, guide_thornby_wells.md, guide_walking.md

```
According to **guide_accessibility.md**, Thornby Wells is the easiest town in the region for accessibility, as it is flat, compact, and everything is within three minutes of everything else.
```

### What town is the easiest to walk in for those who require accessibility? — run 3

- Best distance: 0.4984 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_corry_vale.md, guide_elder_ness.md, guide_givens_mill.md, guide_halden_bay.md, guide_kestrelford.md, guide_marchwood.md, guide_pellew_sands.md, guide_regional_transport.md, guide_thornby_wells.md, guide_walking.md

```
Based on the documents, Thornby Wells is the easiest town in the region for accessibility. 

Source: `guide_accessibility.md`
```

### What is Elder Ness? — run 1

- Best distance: 0.1876 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_corry_vale.md, guide_eating.md, guide_elder_ness.md, guide_givens_mill.md, guide_halden_bay.md, guide_kestrelford.md, guide_marchwood.md, guide_pellew_sands.md, guide_thornby_wells.md, guide_walking.md

```
Based on guide_elder_ness.md, Elder Ness is a headland featuring a village of 300 residents, a lighthouse, a bird observatory, and very little else. People visit for walking, birds, or a deliberate absence of things to do.
```

### What is Elder Ness? — run 2

- Best distance: 0.1876 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_corry_vale.md, guide_eating.md, guide_elder_ness.md, guide_givens_mill.md, guide_halden_bay.md, guide_kestrelford.md, guide_marchwood.md, guide_pellew_sands.md, guide_thornby_wells.md, guide_walking.md

```
According to `guide_elder_ness.md`, Elder Ness is a headland with a village of 300 people, a lighthouse, a bird observatory, and very little else.
```

### What is Elder Ness? — run 3

- Best distance: 0.1876 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_corry_vale.md, guide_eating.md, guide_elder_ness.md, guide_givens_mill.md, guide_halden_bay.md, guide_kestrelford.md, guide_marchwood.md, guide_pellew_sands.md, guide_thornby_wells.md, guide_walking.md

```
According to `guide_elder_ness.md`, Elder Ness is a headland featuring a village of 300 residents, a lighthouse, a bird observatory, and very little else.
```

### Which towns have a hospital and what times are they open? — run 1

- Best distance: 0.4897 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_corry_vale.md, guide_elder_ness.md, guide_givens_mill.md, guide_halden_bay.md, guide_kestrelford.md, guide_marchwood.md, guide_pellew_sands.md, guide_regional_transport.md, guide_thornby_wells.md

```
Based on the provided documents, Marchwood has the nearest full hospital, and Brightwater also has a hospital. However, the documents do not state what times either hospital is open.

Source: `guide_accessibility.md`
```

### Which towns have a hospital and what times are they open? — run 2

- Best distance: 0.4897 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_corry_vale.md, guide_elder_ness.md, guide_givens_mill.md, guide_halden_bay.md, guide_kestrelford.md, guide_marchwood.md, guide_pellew_sands.md, guide_regional_transport.md, guide_thornby_wells.md

```
Based on the provided documents, Marchwood has the nearest full hospital, while Brightwater also has a hospital. The documents do not state what times these hospitals are open. 

Source: `guide_accessibility.md`
```

### Which towns have a hospital and what times are they open? — run 3

- Best distance: 0.4897 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_corry_vale.md, guide_elder_ness.md, guide_givens_mill.md, guide_halden_bay.md, guide_kestrelford.md, guide_marchwood.md, guide_pellew_sands.md, guide_regional_transport.md, guide_thornby_wells.md

```
Based on the provided documents, the nearest full hospital is in Marchwood, and Brightwater also has a hospital. The documents do not state what times these hospitals are open. 

Source: `guide_accessibility.md`
```

### If any, where are the grocery stores? — run 1

- Best distance: 0.5997 (refused by the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_corry_vale.md, guide_eating.md, guide_elder_ness.md, guide_givens_mill.md, guide_halden_bay.md, guide_kestrelford.md, guide_marchwood.md, guide_pellew_sands.md, guide_thornby_wells.md

```
I don't have enough information about that.
```

### If any, where are the grocery stores? — run 2

- Best distance: 0.5997 (refused by the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_corry_vale.md, guide_eating.md, guide_elder_ness.md, guide_givens_mill.md, guide_halden_bay.md, guide_kestrelford.md, guide_marchwood.md, guide_pellew_sands.md, guide_thornby_wells.md

```
I don't have enough information about that.
```

### If any, where are the grocery stores? — run 3

- Best distance: 0.5997 (refused by the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_corry_vale.md, guide_eating.md, guide_elder_ness.md, guide_givens_mill.md, guide_halden_bay.md, guide_kestrelford.md, guide_marchwood.md, guide_pellew_sands.md, guide_thornby_wells.md

```
I don't have enough information about that.
```

### Where does the name of the town Elder ness originate from? — run 1

- Best distance: 0.2798 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_corry_vale.md, guide_eating.md, guide_elder_ness.md, guide_givens_mill.md, guide_halden_bay.md, guide_kestrelford.md, guide_regional_transport.md, guide_thornby_wells.md, guide_walking.md

```
I do not have enough information in the documents to answer where the name of the town Elder Ness originates. 

Source: guide_elder_ness.md
```

### Where does the name of the town Elder ness originate from? — run 2

- Best distance: 0.2798 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_corry_vale.md, guide_eating.md, guide_elder_ness.md, guide_givens_mill.md, guide_halden_bay.md, guide_kestrelford.md, guide_regional_transport.md, guide_thornby_wells.md, guide_walking.md

```
I do not have enough information to answer where the name Elder Ness originates from. (Source: guide_elder_ness.md)
```

### Where does the name of the town Elder ness originate from? — run 3

- Best distance: 0.2798 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_brightwater.md, guide_corry_vale.md, guide_eating.md, guide_elder_ness.md, guide_givens_mill.md, guide_halden_bay.md, guide_kestrelford.md, guide_regional_transport.md, guide_thornby_wells.md, guide_walking.md

```
I do not have enough information to answer where the name of the town Elder Ness originates from. 

Source: guide_elder_ness.md
```
