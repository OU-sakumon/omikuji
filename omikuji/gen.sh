#!/bin/bash

cd quiz
for file in *.tex
do
  platex "$file"
done

for file in *.dvi
do
  dvipdfmx "$file"
done

rm *.dvi *.aux *.log *.out
mv *.pdf ../backend/pdf
