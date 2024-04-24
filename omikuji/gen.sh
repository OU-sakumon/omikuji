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

rm *.dvi *.aux *.log
mv *.pdf ../backend/pdf

cd ../backend/omikuji_gen
/usr/bin/python3 omikuji.py

cd ../pdf
rm *.pdf

cd ../png
rm *.png

