#!/bin/bash

#unzipping 250 times starting at 1 name of file since 1 unzips 2, 2 unzips 3, so on and so on. 
for i in {1..250}; do
    unzip -oq "${i}.zip"
    #trying to keep original file and not delete it
    if ((i != 1)); then
        #Testing
        echo "${i}.zip"
        #removing unecessary files
        rm "${i}.zip"
    fi
done
#creating variable forr text and using cat to display in reverse with rev
flag=$(cat present.txt | rev)

echo $flag