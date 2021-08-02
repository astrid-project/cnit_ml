import ast
import csv
import json
import re
import sys
import time
from os import listdir

import numpy as np
import pandas as pd
from joblib import dump, load
from kafka import KafkaConsumer, KafkaProducer

# new from Panagiotis
file = open('vdpi_output_eth0_attack_22Jun21.log', 'r')
#file = open('vdpi_output_eth0_normal_22Jun21.log', 'r')
# old
#file = open('vdpi_output_13Apr21.log', 'r')
#file = open('vdpi_output_22Jun21_3.log', 'r')

lines = file.read().splitlines()
file.close()


producer = KafkaProducer(bootstrap_servers='kafka-service:9092')
counter = 0
for line in lines:
    print(line)
    producer.send('network-data', json.dumps(json.loads(line)).encode('utf-8'))
    time.sleep(0.05)
