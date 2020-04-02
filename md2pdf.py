#! /usr/bin/env python

# import libs
import os
import argparse
import yaml
from shutil import copyfile

# get template name
template_filename = "template.tex"

# make script receive filename as argument
parser = argparse.ArgumentParser()
parser.add_argument("input_filename", help = "Markdown file to be compiled into a formatted PDF")

# define filenames
input_filename = parser.parse_args().input_filename
input_name = input_filename[:len(input_filename) - 3] 
temp_filename = input_name + "-temp.tex"
tex_filename = input_name + ".tex"

# read markdown for metadata
input_md = open(input_filename).read()

# data wrangling
meta_marker = "---"
meta_begin = input_md.find(meta_marker)
meta_end = input_md[meta_begin + len(meta_marker):].find(meta_marker)
metadata_str = input_md[meta_begin + len(meta_marker):meta_end + len(meta_marker)]
metadata = yaml.safe_load(metadata_str)

# compile md to tex
os.system("pandoc " + input_filename + " -o " + temp_filename)
temp_latex = open(temp_filename).read()
output_latex = open(template_filename).read()

# add tex to template
marker = "\\begin{document}"
insertion_pos = output_latex.find(marker)
output_latex = output_latex[:insertion_pos + len(marker)] + "\n" +  temp_latex + output_latex[insertion_pos + len(marker):]

# replace vars from metadata
mapping = [("TITLEVAR", metadata["title"]), ("AUTHORVAR", metadata["author"]), ("INSTITUTEVAR",  metadata["institute"]), ("TRANSLATORVAR", metadata["translator"]), ("DATEVAR", metadata["date"])]
for k, v in mapping:
    output_latex = output_latex.replace(k, v)

# write full tex to file
tex_file = open(tex_filename, 'w')
tex_file.write(output_latex)

# compile full tex to pdf
tex_file.close()
os.system("pdflatex " + tex_filename)

# cleanup
os.remove(temp_filename)
temp_extensions = [".aux", ".log"] 
for ext in temp_extensions:
    temp_filename = input_name + ext
    os.remove(temp_filename)
