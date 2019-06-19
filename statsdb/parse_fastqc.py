#!/usr/bin/env python

import argparse
import os
import sys
import MySQLdb
import db
import run_table
import qc_analysis
import fastqc


def main():
    parser=optparse.ArgumentParser()
    parser.add_argument("-i", "--input", type="string", dest="input")
    parser.add_argument("-d", "--db_config", type="string", dest="db_config")
    args = parser.parse_args()

    try:
        #read config file and get connection information
        dbhost=""; dbuser="";password=""; dbname=""
        fh=open(args.db_config)
        firstline=fh.readline().strip().split("\t")[1].split(";")
        dbhost=firstline[1].split("=")[1]
        dbname=firstline[0].split(":")[2]
        dbuser=fh.readline().strip().split("\t")[1]
        password=fh.readline().strip().split("\t")[1]
        # print(dbhost, dbuser, password, dbname)
        conn= MySQLdb.connect(dbhost, dbuser, password, dbname)
    except:
        print("Could not get connection. Please check the database name.")
        exit(1)

    run_table.add_header_scope("barcode", "analysis")
    list_of_objs = run_table.parse_file(input_metafile)

    #db.connect(config)
    db = db.Database(conn)

    for obj in list_of_objs:
        print(obj.data["property"])
        fast_qc_file = obj.get_property("path_to_analysis")
        print("fast_qc_file: ", fast_qc_file)
        if os.path.exists(fast_qc_file):
            fastqc.parse_file(fast_qc_file, obj)
            # print("Inserting the record now: ")
            db.insert_analysis(obj)
        else:
            print("WARN: Unable to read file:", fast_qc_file)

    conn.close()

if __name__ == "__main__":
    main()
