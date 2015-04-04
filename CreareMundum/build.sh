#!/bin/sh

for ((i=0 ; 2 - $i ; i++)) do
pdflatex -interaction=nonstopmode Ere_raciale.tex
pdflatex -interaction=nonstopmode Ere_medievale.tex
pdflatex -interaction=nonstopmode Ere_technologique.tex
pdflatex -interaction=nonstopmode Apocalypse.tex
pdflatex -interaction=nonstopmode Ere_post-apocalyptique.tex
done

rm -rf *.out *.toc *.aux *.log 
