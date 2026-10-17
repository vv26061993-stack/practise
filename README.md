# Demo Document Parser

This is a small project for learning Git commands while working on a real, simple code example.

## What it does

The parser reads a text file and extracts:
- word count
- sentence count
- top keywords

## Run it

```bash
python main.py sample_doc.txt
```

Example output:

```python
{'word_count': 46, 'sentence_count': 6, 'top_keywords': ['and', 'document', 'parser', 'to', 'words']}
```

## Git practice workflow

After installing Git on your machine, run the following commands in this folder:

```bash
git init
git status
git add .
git commit -m "Initial parser version"
git branch
git checkout -b feature/keyword-filter
git status
git add parser.py
git commit -m "Improve keyword ranking"
git checkout main
git merge feature/keyword-filter
git log --oneline
```

## Project structure

- `parser.py` - parsing logic
- `main.py` - CLI entry point
- `sample_doc.txt` - sample document used for testing
- `tests/test_parser.py` - unit tests

## Good Git exercises

- create a feature branch
- make a change and commit it
- check `git diff`
- view the history with `git log`
- reset or restore a file when needed
