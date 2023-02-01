
import paho.mqtt.client as paho
import json
import time
broker="localhost"
port=1883
def on_publish(client,userdata,result):             #create function for callback
    try:
        print(result)
        if result > 0:
            print(f"Message is published {result}\n")
        else:
            print("Failed to send message \n")
    except Exception as e:
        print("Exception is on published message",e)
        
def main_handler(sample_unit):
    client1= paho.Client()                           #create client object
    client1.on_publish = on_publish                          #assign function to callback
    client1.connect(broker,port)                                 #establish connection
    
    
#call the publish

    topic_name = "cdac/diot/temp"
    temp_reading = 11
    humi_reading = 55
    for reading_publish in range(40):
        sensor_data = {
            "temperature" : temp_reading,
            "humidity" : humi_reading
        }
        
        client1.publish(topic_name,json.dumps(sensor_data))
        time.sleep(5)
    

sample_unit = 40
main_handler(sample_unit)
    
                 