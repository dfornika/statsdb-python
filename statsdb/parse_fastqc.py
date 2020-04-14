#!/usr/bin/env python

import argparse
import json
import os
import sys
import pymysql.cursors
import db
import run_table
import qc_analysis
import fastqc

from pprint import pprint

def main(args):
    
    try:
        #read config file and get connection information
        dbhost = ""
        dbuser = ""
        password = ""
        dbname = ""
        port = None
        fh=open(args.db_config)
        firstline=fh.readline().strip().split("\t")[1].split(";")
        dbhost=firstline[1].split("=")[1]
        if ':' in dbhost:
            dbhost, port = dbhost.split(":")
            port = int(port)
        dbname=firstline[0].split(":")[2]
        dbuser=fh.readline().strip().split("\t")[1]
        password=fh.readline().strip().split("\t")[1]
        print(
            json.dumps(
                {
                    "dbhost": dbhost,
                    "port": port,
                    "dbuser": dbuser,
                    "password": password,
                    "dbname": dbname,
                }
            )
        )
        conn= pymysql.connect(
            host=dbhost,
            port=port,
            user=dbuser,
            passwd=password,
            db=dbname,
        )
    except:
        print("Could not get connection. Please check the database name.")
        exit(1)

    # run_table.add_header_scope("barcode", "analysis")
    list_of_objs = run_table.parse_file(args.input)
    print(list_of_objs)
    #db.connect(config)
    database = db.Database(conn)

    for obj in list_of_objs:
        print(obj.data["property"])
        fast_qc_file = obj.get_property("path_to_analysis")
        print("fast_qc_file: ", fast_qc_file)
        if os.path.exists(fast_qc_file):
            fastqc.parse_file(fast_qc_file, obj)
            # print("Inserting the record now: ")
            pprint(obj)
            database.insert_analysis(obj)
        else:
            print("WARN: Unable to read file:", fast_qc_file)

    conn.close()

if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("-i", "--input", dest="input")
    parser.add_argument("-d", "--db_config", dest="db_config")
    args = parser.parse_args()
    main(args)
