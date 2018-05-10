import os

# add dependency to use spark with kafka
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.2.0 pyspark-shell'

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.sql import Row, SparkSession
import json
from cassandra.cluster import Cluster
from cassandra.query import BatchStatement
from cassandra import ConsistencyLevel

import config

count =0
def getSparkSessionInstance(sparkConf):
    if ("sparkSessionSingletonInstance" not in globals()):
        globals()["sparkSessionSingletonInstance"] = SparkSession \
            .builder \
            .config(conf=sparkConf) \
            .getOrCreate()
    return globals()["sparkSessionSingletonInstance"]


def sendPartition(iter):
    cassandra_cluster = Cluster(['54.71.115.97','35.166.209.97','35.166.89.248','34.218.167.77'])
    cassandra_session = cassandra_cluster.connect('oilwell')

   # sql_statement = cassandra_session.prepare("INSERT INTO data (tag, count) VALUES (?, ?)")
    for record in iter.collect():
        # sql_statement = "INSERT INTO ad_campaign" + \
        #                 " (tag, count) VALUES (\'" + str(record["tag"]) + "\' ," \
        #                 +  record["count"] + "\')"
        dt = str(record[1])
        sql_statement ="INSERT INTO well_pressure (id, dt, well_name, pressure_1, pressure_2, pressure_3, pressure_4 ) VALUES (%d, \' %s \', \'%s\', %d, %d, %d, %d);" %  (int(record[0]), dt, str(record[2]), int(record[3]), int(record[4]), int(record[5]), int(record[6]))
        # batch.add(sql_statement,
        #           (record[0], int(record[1])))
        cassandra_session.execute(sql_statement)
        """
        print ('Write into Canssandra success!')
        """
    #cassandra_session.execute(batch)
    cassandra_cluster.shutdown()

def main():
    sc = SparkContext(appName="campaign_stream_processing")
    sc.setLogLevel("WARN")

    ssc = StreamingContext(sc, 1)
    ssc.checkpoint("hdfs://ec2-54-71-115-97.us-west-2.compute.amazonaws.com:9000/checkpoint/")

    # create a direct stream from kafka without using receiver
    kafkaStream = KafkaUtils.createDirectStream(ssc, ['rtpressure'], {"metadata.broker.list": config.KAFKA_BROKERS})

    # parse each record string as json
    data_ds = kafkaStream.map(lambda v: json.loads(v[1]))

    data_ds.count().map(lambda x: 'Records in this batch: %s' % x) \
        .union(data_ds).pprint()

    # use the window function to group the data by window
    #dataWindow_ds = data_ds.map(lambda x: (x['campaignid'], (x['acc'], x['time']))).window(10, 10)
    # rdd = kafkaStream.map(lambda x: (x["tag"] + '_' + (x["eventType"]), 1)).reduceByKey(lambda a, b: a + b)
    # rdd.pprint(10)
    dataWindow_ds = data_ds.map(lambda x: (x['id'], x['time'], x['well_name'], x['pressure_1'], x['pressure_2'], x['pressure_3'],x['pressure_4']))

    dataWindow_ds.foreachRDD(sendPartition)
    '''
    calculate the window-avg and window-std
    1st map: get the tuple (key, (val, val*val, 1)) for each record
    reduceByKey: for each key (user ID), sum up (val, val*val, 1) by column
    2nd map: for each key (user ID), calculate window-avg and window-std, return (key, (avg, std))
    '''
    # dataWindowAvgStd_ds = dataWindow_ds \
    #     .map(getSquared) \
    #     .reduceByKey(lambda a, b: (a[0] + b[0], a[1] + b[1], a[2] + b[2])) \
    #     .map(getAvgStd)
    #
    # # join the original Dstream with individual record and the aggregated Dstream with window-avg and window-std
    # joined_ds = dataWindow_ds.join(dataWindowAvgStd_ds)
    #
    # # label each record 'safe' or 'danger' by comparing the data with the window-avg and window-std
    # result_ds = joined_ds.map(labelAnomaly)
    # resultSimple_ds = result_ds.map(lambda x: (x[0], x[1], x[5]))
    #
    # # Send the status table to rethinkDB and all data to cassandra
    # result_ds.foreachRDD(lambda rdd: rdd.foreachPartition(sendCassandra))
    # #resultSimple_ds.foreachRDD(sendRethink)

    ssc.start()
    ssc.awaitTermination()
    return


if __name__ == '__main__':
    main()
