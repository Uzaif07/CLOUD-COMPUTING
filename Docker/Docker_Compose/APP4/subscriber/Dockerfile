FROM ubuntu:20.04

LABEL "DEVELOPER"="DIOT-2022"

RUN apt update -y && apt install mosquitto-clients -y


CMD [ "mosquitto_sub", "-t","cdac/diot/temp", "-h", "mqttbroker", "-p", "1883","-d"]

