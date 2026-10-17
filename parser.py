import re
from collections import Counter


def normalize_words(text):
    return [word for word in re.findall(r"[A-Za-z']+", text.lower()) if len(word) > 1]


def extract_summary(text):
    source = (text or "").strip()
    if not source:
        return {
            "word_count": 0,
            "sentence_count": 0,
            "top_keywords": [],
        }

    words = normalize_words(source)
    sentences = [sentence.strip() for sentence in re.split(r"(?<=[.!?])\s+", source) if sentence.strip()]

    keyword_counts = Counter(words)
    top_keywords = [
        word for word, _ in sorted(keyword_counts.items(), key=lambda item: (-item[1], item[0]))[:5]
    ]

    return {
        "word_count": len(words),
        "sentence_count": len(sentences),
        "top_keywords": top_keywords,
    }
