from __future__ import print_function
from pyspark.sql import SparkSession
import config
import os
import sh
 

def main():
    #hdfs_path = config.HDFS_PATH
    hdfs_list_cmd = 'hadoop fs -ls ' + config.HDFS_PATH
    #files = os.system(hdfs_list_cmd)
    files =  [ line.rsplit(None,1)[-1] for line in sh.hdfs('dfs','-ls',config.HDFS_PATH).split('\n') if len(line.rsplit(None,1))][1:]
    spark = SparkSession.builder.appName("batch_processing").config("spark.cassandra.connection.host","127.0.0.1").getOrCreate()
    df = spark.read.json(config.HDFS_PATH)
    df.printSchema()
    df.groupby(['date', 'well_name']).sum('allocated_gas', 'allocate_oil', 'allocated_water')
    df.groupby(['date', 'well_name']).avg('pressure')
    df = df.createOrReplaceTempView("oildata")
    sqlDF = spark.sql("SELECT TO_DATE(CAST(UNIX_TIMESTAMP(date, 'MM/dd/yyyy') AS TIMESTAMP)) as dt, well_name, sum(allocated_gas) as gas_mscf, sum(allocate_oil) as oil_bbl, avg(pressure) as pressure, sum(allocated_water) as water_bbl from oildata group by date, well_name order by date")
    sqlDF.write.format("org.apache.spark.sql.cassandra").mode('append').options(table="oil_production", keyspace="oilwell").save()
    spark.stop()

if __name__ == '__main__':
    main()
