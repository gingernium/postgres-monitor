#!/bin/python

#Import librarys

import lib.sql


result = lib.sql.query_pgsql("postgres", "select * FROM pg_settings")
#result = query_pgsql("postgres", "select * FROM pg_stat_activity")
counter=0

for row in result:
    print " ", row['name'],"-",row['setting']
    counter += 1

print counter,"settings found"
