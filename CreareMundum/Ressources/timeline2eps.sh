#!/bin/bash

FILE_bak=timeline.tex;
FILE=post_timeline.tex;

cp $FILE_bak $FILE
echo -e "\documentclass[a4paper, 11pt]{article}\n\usepackage[T1]{fontenc}\n\usepackage[utf8]{inputenc}\n\usepackage[francais]{babel}\n\usepackage[babel=true,kerning=true]{microtype}" > $FILE
echo "\begin{document}" >> $FILE
echo "$(cat $FILE_bak)" >> $FILE
echo "\end{document}" >> $FILE
latex $FILE
dvips ${FILE%tex}dvi -o ${FILE%tex}eps

cp ${FILE%tex}eps ${FILE_bak%tex}eps
rm ${FILE%tex}*
