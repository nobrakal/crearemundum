#!/bin/bash

FILE_bak=timeline.tex;
FILE=post_timeline.tex;
FILE_withouttex=post_timeline;

echo -e "\documentclass[a4paper, 11pt]{article}\n\usepackage[T1]{fontenc}\n\usepackage[utf8]{inputenc}\n\usepackage[francais]{babel}\n\usepackage[babel=true,kerning=true]{microtype}" > $FILE
echo "\begin{document}" >> $FILE
echo "$(cat $FILE_bak)" >> $FILE
echo "\end{document}" >> $FILE
latex $FILE
dvips -R -E ${FILE%tex}dvi -o ${FILE%tex}eps
convert -quality 100 -density 150 ps:${FILE%tex}eps ${FILE%tex}png

cp $FILE_withouttex."png" "timeline.png"
rm $FILE_withouttex.*
