#!/bin/bash

#a=6
#b=6

#if [ $a -lt $b ] || [ $a -eq $b ]
#then
#   echo "b is greater than or equal to a"
#else
#   echo "a is greater than or equql to b"
#fi

#complist="1 2 3 4"
#count=0
#for comp in $complist; 
#do
#    echo $comp
#    let newco=$count + $comp
#    $newco
#done

getdoc=$(service docker status)
echo $getdoc
