import time
import paho.mqtt.client as paho

from flask import Flask,jsonify
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)


broker="localhost" #브로커서버가 있는 라즈베리파이라서 localhost를 사용합니다.
recvData = ""
#define callback
def on_message(client, userdata, message):
    time.sleep(1)
    recvData = str(message.payload.decode("utf-8"))
    global humi;
    global temp;
    print(recvData)
    print(recvData[0],recvData[1],recvData[2],recvData[3],recvData[4])
    humi=(recvData[0]+recvData[1]+recvData[2]+recvData[3]+recvData[4])
    temp=(recvData[6]+recvData[7]+recvData[8]+recvData[9]+recvData[10])
    print(float(temp))
    print(float(humi))
    
    
    

client = paho.Client()
client.on_message=on_message


app = Flask(__name__)
api = Api(app)


print("connecting to broker ",broker)
client.connect(broker)#connect
client.loop_start() #start loop to process received messages
print("subscribing ")
client.subscribe("Sensor")#Sensor 토픽을 구독해 줍니다.

time.sleep(3)
#client.loop_forever()

client.disconnect() #disconnect



class RegistUser(Resource):
    def get(self):
        #return {"slip": { "id": 192, "advice": "Don't take it personally."}}
        my_res = jsonify({'hi':'hello'})
        x=str("Temperature : "+temp+"C")
        y=str("Humidity : "+humi+"%")
        temhumi=jsonify({'humi': x,'temp':y})
        temhumi.headers["Access-Control-Allow-Origin"] = "*"
        return temhumi
        
        
api.add_resource(RegistUser, '/temp')

if __name__ == '__main__':
    app.run(debug=True)
time.sleep(3)


