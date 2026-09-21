"""
Stage 2 of the pipeline: splitting documents into chunks.

⚠️ THIS IS THE FILE YOU CHANGE IN MILESTONE 3.

`split_documents` below is deliberately plain. It cuts every document into
fixed-size pieces with a fixed overlap and pays no attention to where sentences
or paragraphs end. It works, and it is not good.

On a corpus of short posts it may not cut anything at all: `campus_life` comes
out as 88 documents and 88 chunks, because almost nothing in it reaches 800
characters. That is the baseline, not a bug — Milestone 3 is where you decide
whether one post should stay one chunk.

Your job in Milestone 3 is to replace the *body* of `split_documents` with a
strategy that fits the documents you actually read in Milestone 1. Keep the
name and the shape of what it returns — the rest of the pipeline calls it, and
your README has to name the function that produced your chunks.

If you get stuck for 30 minutes, `fallback_split` is the original. Switch back
to it, write down what you saw, and move on. That's a real observation about
your pipeline, not giving up.
"""

from dataclasses import dataclass

import config
from ingest import Document


@dataclass
class Chunk:
    """One piece of one document."""

    text: str
    source: str        # which file it came from
    index: int         # which chunk within that file, starting at 0
    produced_by: str   # the function that made it — cite this in your README

    @property
    def label(self) -> str:
        return f"{self.source}#{self.index}"


def fallback_split(
    documents: list[Document],
    chunk_size: int | None = None,
    overlap: int | None = None,
) -> list[Chunk]:
    """
    The starter's original chunker. Fixed-size character windows with overlap.

    Keep this function. Milestone 3's stop rule points back at it, and having
    something to compare your own strategy against is useful in unit 2.
    """
    chunk_size = chunk_size or config.CHUNK_SIZE
    overlap = overlap or config.CHUNK_OVERLAP

    if overlap >= chunk_size:
        raise ValueError("overlap has to be smaller than chunk_size")

    chunks: list[Chunk] = []
    for doc in documents:
        start = 0
        index = 0
        while start < len(doc.text):
            piece = doc.text[start : start + chunk_size].strip()
            if piece:
                chunks.append(
                    Chunk(
                        text=piece,
                        source=doc.source,
                        index=index,
                        produced_by="chunker.py::fallback_split",
                    )
                )
                index += 1
            start += chunk_size - overlap

    return chunks


def split_documents(documents: list[Document]) -> list[Chunk]:
    """
    Split documents into chunks. ⚠️ REPLACE THE BODY OF THIS IN MILESTONE 3.

    Right now it just calls the fallback. That is the plain, generic behaviour
    the brief is talking about.

    When you write your own strategy, set `produced_by` to
    "chunker.py::split_documents" so your README's Sample Chunks section names
    the right function. `app.py chunks` prints that string for you.

    Things worth thinking about before you write any code:
      - Are your documents short posts or long guides?
      - Is the useful information in one sentence, or spread over a paragraph?
      - Would splitting on paragraph breaks keep more thoughts intact than
        splitting on a character count?
    """

    chunk_size = config.CHUNK_SIZE
    overlap = config.CHUNK_OVERLAP

    if overlap >= chunk_size:
        raise ValueError("overlap has to be smaller than chunk_size")
    """
    This is what I could come up in the 2 hours I was working on it. I will revise it as I learn and test
    more. I was stuck on understanding milestone 2 for longer than 5 hours so I didn't have much time for coding.
    It doesn't use chunk_size or chunk_overlap though since it is a basic implementation meant to seperate chunks
    by headers. 

    Weaknesses: Shortest chunk is only 25 characters (probably a header that ends early for some reason).
                Probably not good at scale.

    Results:
        Corpus: city_guides
        loaded   14 documents, 28,958 characters, ~2,068 characters per document
        chunked  98 chunks, 293 characters on average (shortest 25, longest 711), produced by chunker.py::split_documents
        embedding 98 chunks (first run downloads the model)...
        stored   98 chunks in 13.8s

    """ 
    chunks: list[Chunk] = []
    for doc in documents:
        index = 0
        for chunk in doc.text.split('##'):
            chunks.append(
                Chunk(
                    text=chunk,
                    source=doc.source,
                    index=index,
                    produced_by="chunker.py::split_documents",
                )
            )
            index += 1
    return chunks
    # return fallback_split(documents) # I changed config.py so I have to hardcode the old config into the func
    # return fallback_split(documents, 800, 120)

def chunk_documents(documents, chunk_size=600, min_chunk_size=120):
    """
    Discussed chunks that Gemini said was the best but it does not use chunk_overlay
    The results here are good but it is not my work so I just used it to see how it compares as a testing function.

    Output:
        Corpus: city_guides
        loaded   14 documents, 28,958 characters, ~2,068 characters per document
        chunked  94 chunks, 304 characters on average (shortest 174, longest 637), produced by chunker.py::structure_split
        embedding 94 chunks (first run downloads the model)...
        stored   94 chunks in 11.8s

    """
    chunks: list[Chunk] = []

    for doc in documents:
        # Split on Markdown level-2 headers, preserving section structure
        raw_sections = doc.text.split('##')
        index = 0

        for raw_section in raw_sections:
            section_text = raw_section.strip()

            # 1. Skip empty or whitespace-only splits
            if not section_text:
                continue

            # Re-add '## ' so header context isn't lost
            full_section_text = f"## {section_text}" if not section_text.startswith('#') else section_text

            # 2. Handle Oversized Sections (> chunk_size)
            if len(full_section_text) > chunk_size:
                # Fallback: split long section on sentence boundaries
                sentences = full_section_text.split('. ')
                current_chunk = ""

                for sentence in sentences:
                    if len(current_chunk) + len(sentence) < chunk_size:
                        current_chunk += sentence + ". "
                    else:
                        if len(current_chunk.strip()) >= min_chunk_size:
                            chunks.append(Chunk(text=current_chunk.strip(), source=doc.source, index=index, produced_by="chunker.py::structure_split"))
                            index += 1
                        current_chunk = sentence + ". "

                if len(current_chunk.strip()) >= min_chunk_size:
                    chunks.append(Chunk(text=current_chunk.strip(), source=doc.source, index=index, produced_by="chunker.py::structure_split"))
                    index += 1

            # 3. Handle Normal/Ideal Sections
            elif len(full_section_text) >= min_chunk_size:
                chunks.append(Chunk(text=full_section_text, source=doc.source, index=index, produced_by="chunker.py::structure_split"))
                index += 1

    return chunks

def describe(chunks: list[Chunk]) -> str:
    """A one-line summary, printed after indexing."""
    if not chunks:
        return "0 chunks"
    lengths = [len(c.text) for c in chunks]
    return (
        f"{len(chunks)} chunks, "
        f"{sum(lengths) // len(lengths)} characters on average "
        f"(shortest {min(lengths)}, longest {max(lengths)}), "
        f"produced by {chunks[0].produced_by}"
    )


if __name__ == "__main__":
    from ingest import load_documents

    chunks = split_documents(load_documents())
    print(describe(chunks))
