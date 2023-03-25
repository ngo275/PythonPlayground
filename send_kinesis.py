### This file is to send sample/test***.json to Kinesis stream
import boto3
import json
import os
import sys
import time

def put_record(stream_name, data):
    kinesis = boto3.client('kinesis')
    response = kinesis.put_record(
        StreamName=stream_name,
        Data=data,
        PartitionKey='partitionkey')
    return response

def put_records(stream_name, data):
    kinesis = boto3.client('kinesis')
    response = kinesis.put_records(
        Records=data,
        StreamName=stream_name)
    return response

def main():
    stream_name = 'event-tracking-test'
    data = []
    for i in range(300):
        with open(f'sample/test{i}.json') as f:
            data.append({'Data': f.read(), 'PartitionKey': 'test'})
    print(put_records(stream_name, data))

if __name__ == '__main__':
    main()