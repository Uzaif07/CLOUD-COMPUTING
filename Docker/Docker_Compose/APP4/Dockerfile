FROM ubuntu:20.04

LABEL "DEVELOPER"="DIOT-2022"

RUN apt update -y && apt install mosquitto -y
# RUN service mosquitto start
CMD ["/usr/sbin/mosquitto"]
# CMD [ "service", "mosquitto", "start" ]
EXPOSE 1883
