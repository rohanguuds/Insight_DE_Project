#!/usr/bin/env python

import os
from kafka import KafkaProducer
import json
import config


def main():
    producer = KafkaProducer(bootstrap_servers=config.KAFKA_BROKERS)
    mypath = os.path.dirname(os.path.abspath(__file__))
    files = os.listdir(mypath + '/../data/')
    for f in files:
        with open(mypath + '/../data/' + f) as json_data:
                ad_data = json.load(json_data)
        for each in ad_data:
                msg = json.dumps(each, encoding = 'utf-8')
                producer.send(config.KAFKA_TOPIC, msg)
    producer.flush()


if __name__ == '__main__':
    main()
