# Import packages
from dotenv import load_dotenv
import os
from influxdb_client import InfluxDBClient, Point, WriteOptions
from influxdb_client.client.write_api import SYNCHRONOUS

load_dotenv()
token = os.getenv('INFLUX_TOKEN')
org = os.getenv('ORG')
bucket = os.getenv('BUCKET')

client = InfluxDBClient(url="https://us-east-1-1.aws.cloud2.influxdata.com", token=token, org=org)