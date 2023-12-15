#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <query_xml_filename> <output_csv_filename>"
    exit 1
fi

query_xml_filename=$1
output_csv_filename=$2

python server.py &
server_pid=$!
sleep 1
python client.py "$query_xml_filename" "$output_csv_filename"
kill -9 $server_pid
sleep 1
cat output.csv

