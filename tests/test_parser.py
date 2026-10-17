import pathlib

from parser import extract_summary


def test_extract_summary_counts_words_and_keywords():
    text = "Hello world. Hello again! This is a sample doc."
    result = extract_summary(text)

    assert result["word_count"] == 9
    assert result["sentence_count"] == 3
    assert result["top_keywords"][:2] == ["hello", "doc"]


def test_extract_summary_handles_empty_input():
    result = extract_summary("   \n\t  ")

    assert result["word_count"] == 0
    assert result["sentence_count"] == 0
    assert result["top_keywords"] == []
