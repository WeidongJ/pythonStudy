#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import socket
from selectors import DefaultSelector,EVENT_WRITE,EVENT_READ


selector = DefaultSelector()
'''
sock = socket.socket()
sock.setblocking(False)
try: 
    sock.connect(('xkcd.com',80))
except BlockingIOError:
    pass

def connected():
    selector.unregister(sock.fileno())
    print('connected')

selector.register(sock.fileno(),EVENT_WRITE,connected)

def loop():
    while True:
        events = selector.select()
        for event_key, event_mask in events:
            callback = event_key.data
            callback(event_key,event_mask)


'''


class Future:
    def __init__(self):
        self.result = None
        self._callbacks = []

    def add_done_callback(self,fn):
        self._callbacks.append(fn)

    def set_result(self, result):
        self.result = result
        for fn in self._callbacks:
            fn(self)

class Fetcher:
    def __inin__(self, url):
        self.response = b''
        self.url = url
        self.sock = None

    def fetch(self):
        self.sock = socket.socket()
        self.sock.setblocking(False)
        try:
            self.sock.connect(('xkcd.com',80))
        except BlockingIOError:
            pass

        while True:
            f = Future()
            def on_connected():
                f.set_result(None)

            # Register next callback.
            selector.register(self.sock.fileno(),EVENT_WRITE,on_connected)
            chunk = yield f
            selector.unregister(self.sock.fileno())
            print('connected')
            if chunk:
                self.response += chunk
            else:
                # Done reeding
                break


    def connected(self, key, mask):
        print('connected')
        selector.unregister(key.fd)
        request = b'GET {} HTTP/1.0\r\nHost:xkcd.com\r\n\r\n'
        self.sock.send(request)

        # Register the next callback.
        selector.register(key.fd,EVENT_WRITE,self.read_respose)

    def read_respose(self,key,mask):
        global stopped

        urls_todo =set(['/'])
        seen_urls =set(['/'])

        chunk = self.sock.recv(4096)
        if chunk:
            self.response += chunk
        else:
            selector.unregister(key.fd)
            links = self.parse_links()

            # python set-logic:
            for link in links.difference(seen_urls):
                urls_todo.add(link)
                Fetcher(link).fetch()
            
            seen_urls.update(links)
            urls_todo.remove(self.url)
            if not urls_todo:
                stopped = True

def read(sock):
    f = Future()

    def on_readable():
        f.set_result(sock.recv(4096))
    
    selector.register(sock.fileno(),EVENT_READ,on_readable)
    chunk = yield f
    selector.unregister(sock.fileno())
    return chunk

def read_all(sock):
    response = []

    chunk = yield from read(sock)
    while chunk:
        response.append(chunk)
        chunk = yield from read(sock)

    return b''.join(response)

class Task:
    def __init__(self,coro):
        self.coro = coro
        f = Future()
        f.set_result(None)
        self.step(f)

    def step(self,future):
        try:
            next_future = self.coro.send(future.result)
        except StopIteration:
            return

        next_future.add_done_callback(self.step)

fetcher = Fetcher('/353/')
fetcher.fetch()
loop()
while True:
    events = selector.select()
    for event_key, event_mask in events:
        callback = event_key.data
        callback(event_key,event_mask)

stopped = False

def loop():
    while True:
        events = selector.select()
        for event_key, event_mask in events:
            callback = event_key.data
            callback()
