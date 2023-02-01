  
"""
Sensor range is 0 - 50
"""


def send_alert(username,deviceid,sennsor_name,sennsor_value):
    print("Hello {username} on your{deviceid};{sennsor_name} is not working as it is sending {sennsor_value} which out of range (0-50)")