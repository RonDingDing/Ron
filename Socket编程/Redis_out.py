#!/usr/bin/env python
# coding=utf-8

####################redis配置####################
# redis主机
REDISCONFIG = {
    'host': 'localhost',
    'port': 6379,
    'password': 'fw@redis'
}

####################UDP配置####################
UDPCONFIG = {
    'host': 'localhost',
    'port': 7665,
    'proto': 'UDP',
    'status': 'ON',

}

####################代码主体######################
import threading, json, redis, time, socket

class RedisSender(threading.Thread):
    """docstring for RedisSender"""

    def __init__(self):
        super(RedisSender, self).__init__()
        self.event = threading.Event()
        self.dic = {}
        self.begin()

    def create_redis(self, host=REDISCONFIG['host'],
                     port=REDISCONFIG['port'],
                     pw=REDISCONFIG['password']):
        try:
            redis_obj = redis.Redis(host=host, port=port)
            redis_obj.ping()
        except Exception as error:
            redis_obj = None
            print('Error occurred in create_redis(): {}.'.format(error))

        return redis_obj


    def create_socket(self, host=UDPCONFIG['host'],
                 port=UDPCONFIG['port'],
                 proto=UDPCONFIG['proto'],
                 status=UDPCONFIG['status']):
        if status.lower() == 'off':
            return
        if proto.lower() == 'tcp':
            # tcp client
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            # udp client
            client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        return client


    def begin(self):
        self.redis_obj = self.create_redis()
        self.pubsub = self.redis_obj.pubsub()
        self.pubsub.psubscribe('flow_stat*')
        self.radio = self.pubsub.listen()

        self.client = self.create_socket()

    def send_out(self, message):
        self.client.sendto(message, (UDPCONFIG['host'], UDPCONFIG['port']))
        #print ('Send {} to {}:{}.'.format(message, UDPCONFIG['host'], UDPCONFIG['port']))


    def function(self):
        i = next(self.radio)
        message_raw = i['data']
        if isinstance(message_raw, long):
            return
        else:
            self.send_out(message_raw)


    def run(self):
        while True:
            if self.event.isSet():
                break
            self.function()

    def stop(self):
        self.event.set()
        self.client.close()


if __name__ == '__main__':
    try:
        scc = RedisSender()
        scc.start()
        while True:
            time.sleep(1)




    except KeyboardInterrupt:
        scc.stop()


