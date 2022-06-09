#!/bin/bash

docker build -t pytrack .

function run_exercice {
    docker run \
    --rm \
    --read-only \
    --network none \
    --memory 500M \
    --cpus 2.0 \
    --user 1000:1000 \
    --env HOME=/jail \
    --env TMPDIR=/jail \
    --workdir /jail \
    --tmpfs /jail:size=100M,noatime,exec,nodev,nosuid,uid=1000,gid=1000,nr_inodes=5k,mode=1700 \
    --volume `pwd`/solutions/$1:/jail/student:ro \
    --env EXERCISE=$1 \
    --env USERNAME=toto \
    pytrack
}

folder_list=`ls tests`

if [ $# -eq 1 ] && [ $1 = "--all" ]; then
    echo "Run all ewercises"
    for folder in $folder_list; do
        if [[ $folder == Q* ]]; then
            echo "Run exercice $folder"
            run_exercice $folder
        fi
    done

elif [ $# -eq 2 ] && [ $1 = "--all" ]; then
    echo "Run all exercises for quest $2"
    for folder in $folder_list; do
        if [[ $folder == $2* ]]; then
            echo "Run exercice $folder"
            run_exercice $folder
        fi
    done

else
    echo "Run exercice $1"
    run_exercice $1
fi
