#/bin/bash

KEY="^ /etc/passwd \\echo  "

c="grep -i $KEY dictionary-short.txt"

eval $c



