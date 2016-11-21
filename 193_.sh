#!/bin/bash
cat tel.txt | grep -Eo '^((\([0-9]{3}\)\s)|([0-9]{3}-))[0-9]{3}-[0-9]{4}$'>tel_new.txt
#cat tel.txt | grep -Eo '^(\(?[0-9]{3}\)?[-|\s])[0-9]{3}-[0-9]{4}$'>tel_new.txt
#cat tel.txt | grep -Eo '^(([0-9]{3}-)|(([0-9]{3})\s))[0-9]{3}-[0-9]{4}$'>tel_new.txt
