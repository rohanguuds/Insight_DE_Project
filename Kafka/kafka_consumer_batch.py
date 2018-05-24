import sys
import time
from kafka import KafkaConsumer
import os
from hdfs3 import HDFileSystem
import datetime
import config

class KafkaConsumerBatch(object):
    def __init__(self):
        self.consumer = KafkaConsumer(config.KAFKA_TOPIC, bootstrap_servers=config.KAFKA_BROKERS, auto_offset_reset='earliest')
        self.block_cnt = 0
        self.temp_file_dir =''
        self.temp_file=''
        self.messageBlock=0
        self.now = datetime.datetime.now()
        self.dt = self.now.strftime("%Y-%m-%d")
        self.total_file = 0

    def consume(self, output):
        messageBlock = 0
        self.temp_file_dir = os.path.dirname(os.path.abspath(__file__)) + '_' + str(self.total_file)
        self.temp_file = open(self.temp_file_dir, "w")

        for message in self.consumer:
            self.messageBlock += 1
            self.temp_file.write(message.value + "\n")

            if self.messageBlock % 98999 == 0:
                print("inside the msg blcok")
            	self.copy_hdfs(config.HDFS_PATH)

    def copy_hdfs(self, dir):
        timestamp = time.strftime('%Y%m%d%H%M%S')
        self.temp_file.close()
        h_cmd = "hadoop fs -put %s %s" % (self.temp_file_dir, dir)
        print(h_cmd)
        os.system(h_cmd)
        os.remove(self.temp_file_dir)
        self.total_file += 1
        self.temp_file_dir = os.path.dirname(os.path.abspath(__file__)) + '_' + str(self.total_file)
        self.temp_file = open(self.temp_file_dir, "w")


def main():
    myconsumer = KafkaConsumerBatch()
    myconsumer.consume(config.KAFKA_TOPIC)


if __name__ == "__main__":
    main()
