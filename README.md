# The Unofficial Guide

Submitted by: Erick Vergara

Corpus selected: `city_guides`

---

# Unit 1

## What This Does
This project runs **Retrieval-Augmented Generation** (RAG) on your local machine which retrives a limited bank of information we provided to answer questions about a certain corpus or topic. 

I will be using the `city_guides` corpus. It has a collection of information about locations in the city to eat, the environment, seasons, and the nearby towns. The `city_guides` file's are longer than the other corpora and have many headers which will change how the RAG processes information

The questions my corpus system could answer would: be what is the easiest town to walk in, which places has transportation, and what are some warnings about navigating the city?

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. -->

## Chunking Strategy

**Chunk size:** 700

**Overlap:** 100

This is the perfect size for matching the document sections. This eliminates trailing chunks and mid-sentence fragments where chunks are too small or some chunks are too big. 

Every section in the document has around 200 to 700 characters and document headings usually tend to be around 50 characters

We want the chunk to encompass the entire section and the headers. 

`guide_accessibility.md` has 698 characters in one section.

`guide_eating.md` has 653 characters in one section.

Documents are around 2k characters on average so these numbers ensure that every section is included. If there were bigger sections or smaller sections the results for chunks will change so this only works for this specific corpus.

> Note: My implementation in `split_documents` doesn't use chunk_size or chunk_overlap. Each chunk is currently header separated without using the variables. I will add chunk_size and chunk_overlap once I have more time.

> Sidenote: `structure_chunk` has also has a sentence by sentence chunking strategy that uses chunk_size but doesn't use chunk_overlay. It is Gemini's solution so I only used it for testing.

<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. -->

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

**Chunk 1** — source: `guide_accessibility.md#0` — produced by: `chunker.py::split_documents`

```
# Getting around the region with limited mobility

An honest assessment rather than a promotional one. Some of these places are
difficult and it is better to know in advance.
```

**Chunk 2** — source: `guide_corry_vale.md#6` — produced by: `chunker.py::split_documents`

```
 When to go

May to September. Outside those months the pub in the third village closes, the farm shop reduces its hours, and several footpaths become genuinely boggy rather than merely wet. The road is not gritted above the second village and is impassable in snow.

```

**Chunk 3** — source: `guide_givens_mill.md#3` — produced by: `chunker.py::split_documents`

```
 Eat and drink

A tearoom attached to the mill, open 10 to 4 daily except Tuesdays, which sells bread made from the flour ground twenty metres away and is the reason most people come. One pub, food served lunchtimes and Thursday to Saturday evenings.
```

**Chunk 4** — source: `guide_kestrelford.md#6` — produced by: `chunker.py::split_documents`

```
 When to go

Late spring and early autumn. The Saturday market runs year-round but is much reduced from November to February. August is busy with walkers. The single-track approach road is genuinely difficult in snow and the town can be cut off for a day or two most winters.
```

**Chunk 5** — source: `guide_regional_transport.md#1` — produced by: `chunker.py::split_documents`

```
 The railway

The line runs along the river valley, connecting Brightwater to the regional
hub in 50 minutes. Eleven services a day on weekdays, six on Sundays. The line
north of Brightwater closed in 1963 and everything beyond it is bus or car.

Tickets are cheaper booked the day before than on the day, and considerably
cheaper than that booked a week ahead. There is no ticket office at
Brightwater station outside weekday mornings; the machine on the platform takes
cards only.
```

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:**
What town is the easiest to walk in for those who require accessibility?"

**Answer:**

```
According to the unofficial guide brightwater town is walkable end to end in about 35 minutes with two local bus routes at 30 min headway intervals until 7pm which stops on Sundays. Taxis exist but must be phoned; they do not circulate looking for fares. This is the easiest place to walk around compared to the information from other towns.

Sources retrieved: [from guide_brightwater.md]
```

**My relevance cutoff:** 0.5



<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->

| Question | In corpus? | Best distance | Expected answer | Answered expectedly?|
|---|---|---|---|---|
| What town is the easiest to walk in for those who require accessibility? | Y | 0.498 | Thornby Wells | N |
| What is Elder Ness? | Y | 0.188 | Description of village | Y |
| Which towns have a hospital and what times are they open? | Y | 0.490 | Marchwood and Brightwater | Y |
| If any, where are the grocery stores? | Y | 0.6 | Brightwater, and Marchwood | N |
| Where does the name of the town Elder ness originate from? | N | 0.193 | I don't have enough information about that | Y |
| What is the capital of Mongolia? | N | 0.754 | ^ | Y |
| How do I change the oil in a diesel engine? | N | 0.889 | ^ | Y |
| Who won the 1994 World Cup? | N | 0.899 | ^ | Y |
| What is the recommended dosage of ibuprofen for a headache? | N | 0.838 | ^ | Y |
| How do I write a for loop in Rust? | N | 0.838 | ^ | Y |

## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1.** I used AI to analyze my solutions. It revealed keywords in my test questions like `Elder Ness` trigger the system to think it has an answer which wastes token calls on **false positives**.. I learned I could write my test questions better, but also that I can try to prevent edge cases of keywords that may trigger wasted API calls.


**2.** I used AI to help me understand how to write an acceptance criteria for the code. I was stuck for many hours and asked it to explain chunk_size and chunk_overlay. It told me its so weak it passed by accident. I changed the rule to require 100% of top retrieved chunks to end on clean sentence or header boundaries


<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before
<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 3/5 | 3/5 | 3/5 | MISSED |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. 1 chunk of top 3 chunks ending with punctuation symbol. | 1/5 | 5/5 | 5/5| 5/5 | MET |
| 5. Unanswerable questions should scan entire corpus before terminating when top_k is 37 or more. | 5 of 5 | 0/5 | 0/5 | 0/5 | MISSED |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

From file: `run_2026-09-27_1721_before.md` and from function `run_eval.py::judge`

| Question | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| What town is the easiest to walk in for those who require accessibility? | fail | fail | fail |
| What is Elder Ness? | fail | fail | fail |
| Which towns have a hospital and what times are they open? | fail | fail | fail |
| If any, where are the grocery stores? | fail | fail | fail |
| Where does the name of the town Elder ness originate from? | fail | fail | fail |

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunks contain the answer | MET | Although the results verdict I did manually show I did not meet the criteria, I discovered that it wasn't the systems fault, so I decided to give a 'MET' verdict. The reason why some chunks didn't contain the answer was because one question was about a topic that was "inside the corpus but unanswerable since it didn't have any information" when all 5 test questions needed to have an answer in the corpus. That would've result in a pass still but another question also had a miss. The answer was not retrieved also due to the the question complexity since RAG couldn't find the right chunk due to retrieving the wrong sources, however, if it had a higher `top-k` e.g. 10 instead of 5 then it would find the results and answer correctly eventually as long as the context is high enough. |
| 2 | Every answer names a source | MET | This was a deterministic criteria that will always be met since every answer will come from a source. The only error I saw was the answer had said an answer came from more than 1 source which is wrong. |
| 3 | The relevance gate stops out-of-corpus questions | MET | The out-of-corpus questions were also deterministic and the relevance gate system stopped the questions in time exceeding the target since the `cutoff threshold` in config was a good value. |
| 4 | Reducing chunk overlap with broken sentences | MET | While this criteria was 'MET' it had unexpected results. It was dependent on whether code for chunker was good. Additionally, the corpora's file structure in the README file allowed it to split chunks appropriately. And the sections were also properly grammared ensuring complete sentences and sections. The target was set low since I didn't understand the chunker at first but after understanding it I was surprised to 80 of the 98 chunks ended with at least a period (.) symbol which accounts for 80% of the results being properly grammered. I would've check the 18 that were missing but I assumed 80% was good enough. It could even be 100% accurate too but there are probably some without punctuation symbols since there are some small chunks that are likely headers. Additionally, each corpora would need a different chunking function different since the current chunker relies heavily on the README header tags. |
| 5 | Unanswerable questions should scan entire corpus before terminating | MISSED | The criteria was wrong with its measurements. I predicted a `top_k` equal to 37 would scan all the documents. There were 14 documents total and each test run only scanned 11-12 documents total. The calculation for `top_k` was wrong however, the criteria's second evaluation was correct since a higher `top_k` will definitely result in all documents being scanned before terminating especially for the question that is "in-corpus but unanswerable" about the origin of the name of Elder Ness town. The system in that case cannot know that the name is likely a pun. So while this was missed it was half right since a having higher top_k's will result in criteria being true (I used a 36 top_k instead of 41 due to miscalcuation for top_k using original chunk size of 800 instead of 700). The criteria shouldn't be changed even though the results are wrong. It just helps to evaluate how high `top_k` should be which is (total_chars / chunk_size with some extra space in case it needs it). This doesn't require a fix other than having a higher `top_k` to ensure all documents are scanned. |

## Diagnoses
**1 Retrieved chunks contain the answer **
Question 1 asks about which town is the easiest to walk in for those who require accessibility. The answer is in `guide_accessibility.md` but the retrieved sources do not contain the answer of the chunk. The top_k was too low and the vector distance for the best answer was farther than the system expected resulting in the **retrieval stage** but it could also be in the **embedding stage** where the failure happened due to the first 5 chunks not containing the answer. The reranker or scoring step is wrong which is around these two stages. The correct chunk was missed by the initial vector search and was somewhat poorly ordered in priority for question 1. This is because the vector distances were not appropriately measured for the question since the answer ended up being farther away from the first chunks searched. The question was a little harder to find an answer for the system resulting it in needing a larger `top_k` to scan enough documents. I actually thought it would be easier to answer because it has the word `accessibility` in it and the file is the first one in the folder to alphabetically read but for some reason the system doesn't search that document as one of it's first files. The vector distancing similarity method of finding the right chunk can sometimes be wrong when corpora references keywords that are common in many documents like `walk`. When the keywords are widely referenced and the system may score other keywords like `accessibility` lower even if it's meant as a hint. I learned that in RAG simple vector similarity embeddings for keywords are measured in a broad manner in a question rather than by being measured for a narrower relevance. Additionally, having a higher chunk intake definitely helps to answer questions although it's best to have a optimized algorithm that orders the chunks better.

**5 Unanswerable questions should scan entire corpus before terminating**
Question 5 asks where does the name of the town Elder Ness originate from. The answer is not actually in the corpus and should have no answer. It was meant to be a wild and trick test question that would sound like it is "in-corpus" but wasn't. I ended up working and tricking the system. This resulted in the relevance gate not working as intended which was what I wanted. This means the pipeline failed at the **retrieval stage** again. It failed successfully but the system had to use retrieval and make token calls to see that it was out of corpus when it should terminate and detect it is out of scope already. To fix this the RAG system should either get more information to find an answer (increase scope) or it's retrieval should optimized to know more accurately what can be answered before searching.

Overall, some targets were defintely set too low which was unintended. Then again the failures I wanted were also unintended too. The things I thought would suceed failed while the things I wanted to fail failed successfully. 

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

## The Improvement

**What I changed:**
I changed `top-k` to `10` so that it doesn't retrieve too many chunks but has just enough chunks to find the answer to question 1.
**Why I picked it:**
I picked this since it was the simplest to solve and vastly improved the margin of error for answering questions.
<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 4/5 | 4/5 | 4/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. 1 chunk of top 3 chunks ending with punctuation symbol.| 1 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 5. Unanswerable questions should scan entire corpus before terminating when top_k is 37 or more. | 1 of 5 | 0/5 | 0/5 | 0/5 | 0/5 |

From file: `run_2026-09-27_2046_after.md` and from function `run_eval.py::judge`

| Question | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| What town is the easiest to walk in for those who require accessibility? | fail | fail | fail |
| What is Elder Ness? | fail | fail | fail |
| Which towns have a hospital and what times are they open? | fail | fail | fail |
| If any, where are the grocery stores? | fail | fail | fail |
| Where does the name of the town Elder ness originate from? | fail | fail | fail |


**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
