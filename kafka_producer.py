# -*- coding: utf-8 -*-
"""Kafka_Producer.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1b2uzSDc4lZVv2_lkGrw6IFZHGyGWwZGw
"""

!pip install kafka-python
import pandas as pd
from kafka import KafkaConsumer, KafkaProducer
from time import sleep
from json import dumps
import json
from time import sleep
from json import dumps
import json

producer = KafkaProducer(bootstrap_servers=['18.119.105.88:9092'], #change ip here
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

producer.send('demo_test', value={'Name':'Aayush'})

df = pd.read_csv("indexProcessed.csv")

df.head()

df.sample(1)

while True:
    dict_stock = df.sample(1).to_dict(orient="records")[0]
    producer.send('demo_test', value=dict_stock)
    sleep(1)

producer.flush()