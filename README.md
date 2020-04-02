# md2pdf
A short script to convert Markdown documents to formatted PDFs for endcoronavirus.org.

## User's Guide

### Prerequisites
Unfortunately, this script only works on UNIX systems. You need to have Python, a full LaTeX install, and Pandoc for this to work. Make sure you have `pyyaml` installed by running `pip install pyyaml`.

### Using this script
Firstly, write your translation as a Markdown file, which we'll call `file.md`. This script supports five title fields, which should be written like so in the beggining of your Markdown file:

```
---
title: "The Odyssey"
author: "Homer"
institution: "University of Greek Oral Tradition"
translator: "Alexander Pope"
date: "A very long time ago"
---

\maketitle

(the rest of your document goes here)
```
Just place the script `md2pdf.py` and the LaTeX template `template.tex` in the same folder as `file.md` and run the script by typing `python md2pdf.py file.md` or `./md2pdf.py file.md` in your terminal!
