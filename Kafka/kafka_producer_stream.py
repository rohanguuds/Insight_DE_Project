#!/usr/bin/env python

from kafka import KafkaProducer
import config
import random
import time
import datetime

def main():
    count = 0;
    producer = KafkaProducer(bootstrap_servers=config.KAFKA_BROKERS)
    flag = True
    while True:
        tm = datetime.datetime.now()
        count += 1
        time.sleep(.100)
        # There could be more than 1 record per user per second, so microsecond is added to make each record unique.
        time_field = tm.strftime("%Y-%m-%d %H:%M:%S %f")
        if (flag and count < 100):
            pressure_1 = random.randint(720,725)
            pressure_2 = random.randint(700, 705)
            pressure_3 = random.randint(685, 691)
            pressure_4 = random.randint(740, 745)
        elif ( count >= 100 and count < 200):
            pressure_1 = random.randint(720,725)
            pressure_2 = random.randint(750, 780)
            pressure_3 = random.randint(685, 691)
            pressure_4 = random.randint(600, 650)
        elif ( count >= 200 and count < 300):
            pressure_1 = random.randint(720,725)
            pressure_2 = random.randint(800, 850)
            pressure_3 = random.randint(685, 691)
            pressure_4 = random.randint(550, 600)
        else:
            pressure_1 = random.randint(720,725)
            pressure_2 = random.randint(900, 950)
            pressure_3 = random.randint(685, 691)
            pressure_4 = random.randint(350, 400)
        well_name = 'stream'
        message_info = '{"id": "%d", "time": "%s", "well_name": "%s", "pressure_1": "%d", "pressure_2": "%d", "pressure_3": "%d", "pressure_4": "%d"}' \
                       % (count, time_field, well_name, pressure_1, pressure_2, pressure_3, pressure_4)
        
        producer.send('rtpressure', message_info.encode('utf-8'))

    producer.flush()
    return


if __name__ == '__main__':
    main()
