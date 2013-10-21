echo. > log.txt
echo ==================================== >> log.txt
echo %date% %time% >> log.txt
echo ==================================== >> log.txt
echo. >> log.txt
python -m cProfile -s calls solitaire.py >> log.txt 2>&1
