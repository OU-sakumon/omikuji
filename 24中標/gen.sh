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

cd ../pdf # now in backend/pdf
rm *.pdf

cd ../png # now in backend/pdf/png
rm *.png

cd ../omikuji_gen # now in backend/omikuji_gen
mv ../omikuji_gen/*.pdf ../.. # now the file is in omikuji
cd ../.. # now in omikuji

for pdf in *.pdf
do
  mv "$pdf" completed/
done
