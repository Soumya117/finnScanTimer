import requests
import threading
import datetime

def sendRequests(url):
    print("Sending request to: ", url)
    response = requests.get(url)
    if not response.status_code == 200:
        print("Request failed..!")

def on_success(r):
    if r.status_code == 200:
        print('Post succeed: {}'.format(r))
    else:
        print('Post failed: {}'.format(r))

def on_error(ex):
    print('Post requests failed: {}'.format(ex))

def send(url):
    print("Sending requests to {} at {}: ".format(url, datetime.datetime.now()))
    threading.Timer(10800.0, send, args=[url]).start()
    requests.get(url)
    print("Finished at: {}!".format(datetime.datetime.now()))

if __name__== "__main__":
    print("Running main!!")
    send('http://127.0.0.1:56733/links')
    send('http://127.0.0.1:56733/price')
    send('http://127.0.0.1:56733/sold')
    send('http://127.0.0.1:56733/visning')
    send('http://127.0.0.1:56733/clean')
