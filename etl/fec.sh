#!/bin/bash

export PGHOST=localhost PGDATABASE=postgres PGUSER=postgres PGPASSWORD=
fec init
export PGHOST=localhost PGDATABASE=postgres PGUSER=postgres PGPASSWORD=

# OUTPUT=($(python /path/path/script.py attr attr attr | tr -d '[],'))

files=($(python3 ./etl/fec_files.py | tr -d '[],'))
# Not sure how but the part after the pipe turns the python list into a bash array

# files=(1356193 1355002 1354756 1356509 1356518 1355724 1355503 1356058 1355130 1355578 1355368 1355602 1356686 1356740)

for file in "${files[@]}"
do
    curl -s "https://docquery.fec.gov/dcdev/posted/$file.fec" | fec convert $file --format=psql | psql    
done

$(python3 ./etl/pgquery.py)