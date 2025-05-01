#!/bin/bash

if [[ $# != 1 ]]
then
    echo "writetables.sh <target_dir>"
    exit
fi

if [[ ! -d $1 ]]
then 
    echo "Invalid directory path provided"
    exit
fi

targetDir=$1
origAbsPath=$(pwd)

cd "$targetDir" || exit

declare -a toWrite

for file in *.csv ;
do
    [[ -e "$file" ]] || break
    toWrite+=("$file")
done

for filename in "${toWrite[@]}";
do
    if [ "$filename" = "student"]
    then
        mysql
    fi
done

