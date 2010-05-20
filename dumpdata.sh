#!/bin/sh
./manage.py dumpdata dluhy | sed 's/\}\},/}},\n/g' > dluhy/fixtures/initial_data.json
