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

cd "$targetDir" || exit

file=./SQL.sql
if [ ! -e  "$file" ] ;
then
    touch "$file"
fi

declare -a toWrite

for file in *.csv
do
    [[ -e "$file" ]] || break
    toWrite+=("$file")
done

for file in "${toWrite[@]}"
do
    tablename="${file::-9}s"
    columnNames="$(cut "$file" -d $'\n' -f1 | tr -d $'\n')" 
    echo "INSERT INTO $tablename ($columnNames) VALUES" > SQL.sql
    cut "$file" -d $'\n' -f 2- |
    while read line
    do
        echo "($line)," >> SQL.sql
    done
    sed '$ s/.$//' SQL.sql > newSQL.sql
    echo ';' >> newSQL.sql
    rm -rf "SQL.sql"
    mysql schoolschedules < newSQL.sql
    rm -rf "newSQL.sql"
done