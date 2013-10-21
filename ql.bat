echo. > log.txt
echo ==================================== >> log.txt
echo %date% %time% >> log.txt
echo ==================================== >> log.txt
echo. >> log.txt
python solitaire.py >> log.txt 2>&1
