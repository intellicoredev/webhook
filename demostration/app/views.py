# Create your views here.


from django.shortcuts import render, HttpResponse
from requests.auth import HTTPBasicAuth
import requests
import json
from flatten_json import flatten
import time

from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

import hashlib
import hmac
import http.client
import json
import simplejson

from django.conf import settings
from app import views
from app.models import Radios

from time import strptime, strftime, mktime, gmtime

from sigfoxapi import Sigfox

import inspect
import logging


def function_logger(file_level, console_level=None):
    function_name = inspect.stack()[1][3]
    logger = logging.getLogger(function_name)
    logger.setLevel(logging.DEBUG)  # By default, logs all messages

    if console_level != None:
        ch = logging.StreamHandler()  # StreamHandler logs to console
        ch.setLevel(console_level)
        ch_format = logging.Formatter('%(asctime)s - %(message)s')
        ch.setFormatter(ch_format)
        logger.addHandler(ch)

    fh = logging.FileHandler("{0}.log".format(function_name))
    fh.setLevel(file_level)
    fh_format = logging.Formatter('%(asctime)s - %(lineno)d - %(levelname)-8s - %(message)s')
    fh.setFormatter(fh_format)
    logger.addHandler(fh)

    return logger


def fn_iot():
    f1_logger = function_logger(logging.DEBUG, logging.ERROR)
    f1_logger.debug('debug message')
    f1_logger.info('info message')
    f1_logger.warn('warn message')
    f1_logger.error('error message')
    f1_logger.critical('critical message')


def f1():
    f1_logger = function_logger(logging.DEBUG, logging.ERROR)
    f1_logger.debug('debug message')
    f1_logger.info('info message')
    f1_logger.warn('warn message')
    f1_logger.error('error message')
    f1_logger.critical('critical message')


def f2():
    f2_logger = function_logger(logging.WARNING)
    f2_logger.debug('debug message')
    f2_logger.info('info message')
    f2_logger.warn('warn message')
    f2_logger.error('error message')
    f2_logger.critical('critical message')


def datetime_converter(datetime_string):
    # (1) Convert to datetime format
    target_timestamp = strptime(datetime_string, '%Y-%m-%d %H:%M:%S')

    # (2) mktime creates epoch time from the local time
    mktime_epoch = mktime(target_timestamp)
    print(int(mktime_epoch))  # convert to integer to remove decimal

    # (3) gmtime to convert epoch time into UTC time object
    epoch_to_timestamp = strftime('%Y-%m-%d %H:%M:%S', gmtime(mktime_epoch))
    print(epoch_to_timestamp)


def date_converter(date_string):
    # (1) Convert to date format
    target_timestamp = strptime(date_string, '%Y-%m-%d')

    # (2) mktime creates epoch time from the local time
    mktime_epoch = mktime(target_timestamp)
    print(int(mktime_epoch))  # convert to integer to remove decimal

    # (3) gmtime to convert epoch time into UTC time object
    epoch_to_timestamp = strftime('%Y-%m-%d %H:%M:%S', gmtime(mktime_epoch))
    print(epoch_to_timestamp)


datetime_converter('2018-02-15 00:00:00')
date_converter('2018-02-15')

# Create your views here.

import logging

logging.basicConfig(filename="test.log", level=logging.DEBUG)


payload_in = {}
request_in = {}

def index(request):
    return HttpResponse('Hello World!')

def test(request):
    return HttpResponse('My second view!')

#def profile(request):
#    req = requests.get('https://api.github.com/users/intellicoredev')
#    content = req.text
#    return HttpResponse(content)




def profile(request):
    parsedData = []
    if request.method == 'POST':
        username = request.POST.get('user')
        req = requests.get('https://api.github.com/users/' + username)
        jsonList = []
        jsonList.append(json.loads(req.content))
        userData = {}

        flat = flatten_json(jsonList)
        json_normalize(flat)
        for data in jsonList:
            userData['login'] = data['login']
            userData['name'] = data['name']
            userData['blog'] = data['blog']
            userData['email'] = data['email']
            userData['public_gists'] = data['public_gists']
            userData['public_repos'] = data['public_repos']
            userData['avatar_url'] = data['avatar_url']
            userData['followers'] = data['followers']
            userData['following'] = data['following']
        parsedData.append(userData)
    return render(request, 'app/profile.html', {'data': parsedData})

def sigfox_iot(request ):


    content = request_in
    jsonList = []
    userData = {}

    userData = {}
    parsedData = []
    print(('sigfox_iot Log <<<b>>>>: Received the {} device'.format(content)))

    return HttpResponse('Hello World!' + ' sigfox_iot Log <<<b>>>>: Received the {} device'.format(content))


    #userData['device'] = content['device']
    #userData['time'] = content['time']
    #userData['station'] = content['station']
    #userData['data'] = content['data']
    #userData['lat'] = content['lat']
    #userData['lng'] = content['lng']
    #userData['reles'] = content['reles']
    #userData['energia'] = content['energia']
    #userData['blue'] = content['blue']
    #userData['duplicate'] = content['duplicate']
    #userData['snr'] = content['snr']
    #userData['avgSnr'] = content['avgSnr']
    #userData['rssi'] = content['rssi']
    #userData['seqNumber'] = content['seqNumber']
    # userData = record
    parsedData.append(userData)
    print(('sigfox_iot Log <<<b>>>>: Received the {} device'.format(parsedData)))

    return HttpResponse('Hello World!')


    #return render(request, 'app/sigfox_iot.html', {'data': parsedData})




def devices(request):
    parsedData = []
    parsed_rinfoData = []


    user = "5ae21bf09058c2642494fb60"
    password = "0a84892f1600d66de7c45bc2f6a9fae3"
    #deviceId = "42A5B8"

    #url = 'https://backend.sigfox.com/api/devices/' + deviceId + '/messages'


    if request.method == 'POST':
        device_id = request.POST.get('device_id')
        url = 'https://backend.sigfox.com/api/devices/' + device_id + '/messages'
        print("{} {}".format(device_id, url))
        req = requests.get(url,auth=HTTPBasicAuth(user, password))
        print("{} {}".format(req.status_code,req.text))
        
        jsonList = []
        jsonList.append(json.loads(req.text))
        userData = {}

        flat = flatten_json(jsonList)
        json_normalize(flat)

        for data in jsonList:
            userData = {}
            for record in data['data']:
                userData['device'] = record['device']
                userData['time'] = record['time']
                userData['data'] = record['data']
                userData['seqNumber'] = record['seqNumber']
                userData['nbFrames'] = record['nbFrames']
                userData['operator'] = record['operator']
                userData['country'] = record['country']
                userData['snr'] = record['snr']
                userData['linkQuality'] = record['linkQuality']
                userData['groupId'] = record['groupId']
                userData['rinfos'] = record['rinfos']
                #userData = record
                parsedData.append(userData)
                parsed_rinfoData = {}
    return render(request, 'app/devices.html', {'data': parsedData,'rinfos':parsed_rinfoData})


def sigfox(request):
    return HttpResponse('Hello sigfox!')



@csrf_exempt
def hello(request):
    return HttpResponse('pong sigfox')




def handle_webhook(event, payload):
    """Simple webhook handler that prints the event and payload to the console"""
    print(('handle_webhook Log: Received the {} event'.format(event)))
    print((json.dumps(payload, indent=4)))

def handle_sigfox_webhook_old(event,request):
    """Simple webhook handler that prints the event and payload to the console"""
    print(('handle_sigfox_webhook Log (event): Received the {} device'.format(event)))
    print('handle_sigfox_webhook Log (request)', request)
    print((json.dumps(request, indent=4)))


    #request_in = request


    jsonList = []
    userData = {}

    userData = {}
    parsedData = []


    content = request

    userData['device'] = content['device']
    userData['time'] = content['time']
    userData['station'] = content['station']
    userData['data'] = content['data']
    userData['lat'] = content['lat']
    userData['lng'] = content['lng']
    userData['reles'] = content['reles']
    userData['energia'] = content['energia']
    userData['blue'] = content['blue']
    userData['duplicate'] = content['duplicate']
    userData['snr'] = content['snr']
    userData['avgSnr'] = content['avgSnr']
    userData['rssi'] = content['rssi']
    userData['seqNumber'] = content['seqNumber']
    # userData = record
    parsedData.append(userData)
    print(('handle_webhook Log (b): Received the {} device'.format(parsedData)))

@csrf_exempt
def webhook(request):
    # Check the X-Hub-Signature header to make sure this is a valid request.
    #github_signature = request.META['HTTP_X_HUB_SIGNATURE']
    #signature = hmac.new(settings.GITHUB_WEBHOOK_SECRET, request.body, hashlib.sha1)
    #expected_signature = 'sha1=' + signature.hexdigest()
    #if not hmac.compare_digest(github_signature, expected_signature):
    #    return HttpResponseForbidden('Invalid signature header')

    # Sometimes the payload comes in as the request body, sometimes it comes in
    # as a POST parameter. This will handle either case.
    if 'payload' in request.POST:
        payload = json.loads(request.POST['payload'])
    else:
        payload = json.loads(request.body)

    event = request.POST

    # This is where you'll do something with the webhook
    handle_webhook(event, payload)


    return HttpResponse(payload, status=http.client.ACCEPTED)


from datetime import datetime, tzinfo, timedelta


class Zone(tzinfo):

    def __init__(self, offset, isdst, name):
        self.offset = offset
        self.isdst = isdst
        self.name = name

    def utcoffset(self, dt):
        return timedelta(hours=self.offset) + self.dst(dt)

    def dst(self, dt):
            return timedelta(hours=1) if self.isdst else timedelta(0)

    def tzname(self, dt):
         return self.name





def pretty_request(request):
    headers = ''
    for header, value in request.META.items():
        if not header.startswith('HTTP'):
            continue
        header = '-'.join([h.capitalize() for h in header[5:].lower().split('_')])
        headers += '{}: {}\n'.format(header, value)

    return (
        '{method} HTTP/1.1\n'
        'Content-Length: {content_length}\n'
        'Content-Type: {content_type}\n'
        '{headers}\n\n'
        '{body}'
    ).format(
        method=request.method,
        content_length=request.META['CONTENT_LENGTH'],
        content_type=request.META['CONTENT_TYPE'],
        headers=headers,
        body=request.body,
    )


# Get The Current Date Or Time
def getdatetime(timedateformat='complete'):
    from datetime import datetime
    timedateformat = timedateformat.lower()
    if timedateformat == 'day':
        return ((str(datetime.now())).split(' ')[0]).split('-')[2]
    elif timedateformat == 'month':
        return ((str(datetime.now())).split(' ')[0]).split('-')[1]
    elif timedateformat == 'year':
        return ((str(datetime.now())).split(' ')[0]).split('-')[0]
    elif timedateformat == 'hour':
        return (((str(datetime.now())).split(' ')[1]).split('.')[0]).split(':')[0]
    elif timedateformat == 'minute':
        return (((str(datetime.now())).split(' ')[1]).split('.')[0]).split(':')[1]
    elif timedateformat == 'second':
        return (((str(datetime.now())).split(' ')[1]).split('.')[0]).split(':')[2]
    elif timedateformat == 'millisecond':
        return (str(datetime.now())).split('.')[1]
    elif timedateformat == 'yearmonthday':
        return (str(datetime.now())).split(' ')[0]
    elif timedateformat == 'daymonthyear':
        return ((str(datetime.now())).split(' ')[0]).split('-')[2] + '-' + ((str(datetime.now())).split(' ')[0]).split('-')[1] + '-' + ((str(datetime.now())).split(' ')[0]).split('-')[0]
    elif timedateformat == 'hourminutesecond':
        return ((str(datetime.now())).split(' ')[1]).split('.')[0]
    elif timedateformat == 'secondminutehour':
        return (((str(datetime.now())).split(' ')[1]).split('.')[0]).split(':')[2] + ':' + (((str(datetime.now())).split(' ')[1]).split('.')[0]).split(':')[1] + ':' + (((str(datetime.now())).split(' ')[1]).split('.')[0]).split(':')[0]
    elif timedateformat == 'complete':
        return str(datetime.now())
    elif timedateformat == 'datetime':
        return (str(datetime.now())).split('.')[0]
    elif timedateformat == 'timedate':
        return ((str(datetime.now())).split('.')[0]).split(' ')[1] + ' ' + ((str(datetime.now())).split('.')[0]).split(' ')[0]


def handle_sigfox_webhook(data, request):
    import datetime

    """Simple webhook handler that prints the event and payload to the console"""
    
    '''
    Data comes in json format as {
        "device": "42A58F",
        "time": "1532456232",
        "station": "2501",
        "data": "419b348ac2c653a400000002",
        "lat": 19.400654,
        "lng": -99.16336,
        "reles": 0,
        "energia": 0,
        "blue": 0,
        "duplicate": "false",
        "snr": "23.27",
        "avgSnr": "16.37",
        "rssi": "-120.00",
        "seqNumber": "1324"
    }
    '''
    

    logging.debug(('log: handle_sigfox_webhook  (data):receive'))
    logging.debug('log:handle_sigfox_webhook  (request.body)')
    '''
    payload = request.body
    event = request.POST
    my_json = payload.decode('utf8').replace("'", '"')
    logging.debug(my_json)
    logging.debug('-' * 50)
    '''
    #print('log:handle_sigfox_webhook request: \n %s', json.dumps(request.POST, indent=4, sort_keys=True))
    logging.info('-' * 50)
    data_json = json.dumps(data, indent=4)
    print("DEBUG:handle_sigfox_webhook:data_json\n {}".format(data_json))

    device_in = data['device']
    time_in  = data['time']
    station_in = data['station']
    data_in = data['data']
    lat_in = data['lat']
    lng_in = data['lng']
    reles_in = data['reles']
    energia_in = data['energia']
    blue_in = data['blue']
    duplicate_in = data['duplicate']
    snr_in = data['snr']
    avgSnr_in = data['avgSnr']
    rssi_in = data['rssi']
    seqNumber_in = data['seqNumber']

    date_in = time.localtime(int(time_in))
    print_date_in = time.strftime('%Y-%m-%d %H:%M:%S', date_in)

    logging.info('---------')
    logging.info(print_date_in)
    logging.info('---------')

    logging.debug('data: \n\n')

    
    
    
    try:
        Radio = Radios.objects.get(KeyRadio=device_in)
    except Radios.DoesNotExist:
        Radio = Radios.objects.get_or_create(KeyRadio=device_in, 
                                            DateCreation=print_date_in,
                                            Station=station_in,
                                            Data=data_in, 
                                            Lat=lat_in, 
                                            Lng=lng_in, 
                                            Reles=reles_in,
                                            Energia=energia_in, 
                                            Blue=blue_in,
                                            AvgSnr=avgSnr_in, 
                                            Rssi=rssi_in, 
                                            Snr=snr_in, 
                                            SeqNumber=seqNumber_in
                                           )
        Radio.save()
        logging.info(Radio)
        logging.info("KeyRadio:" + device_in)
        # entrará aqui cuando no exista ningun elemento
        # que coincida con la busqueda
   


    '''
        pass
    except Persona.MultipleObjectsReturned:
        radio = Radio(clave=device, station=station, fecha=pr,
                                            data=dta, lat=lat, lng=lng, reles=reles,
                                            energia=energia, blue=blue,
                                            avgSnr=avgSnr, rssi=rssi, snr=snr, seqNumber=seqNumber, direccion_id=1)
        radio.save()
        print(radio)
        print("clave:" + device)
        pass
    '''
    # pr = time.gmtime(int(tm))
    # print(pr)
    
    date_time_local = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
    print(date_time_local)
    print(print_date_in)

    now = datetime.datetime.now()
    time_now = (now.year, now.month, now.day, now.hour, now.minute, now.second)
    print(time_now)

    print(getdatetime("datetime"))

    logging.debug('{} {} {} {} {} {} {} {} {} {} {} {} {} {} \n'.format(device_in, time_in, station_in, data_in,
    lat_in, lng_in, reles_in, energia_in, blue_in, duplicate_in, snr_in,
    avgSnr_in, rssi_in, seqNumber_in ))
    # request_in = request

    
def pretty_request(request):
    headers = ''
    for header, value in request.META.items():
        if not header.startswith('HTTP'):
            continue
        header = '-'.join([h.capitalize() for h in header[5:].lower().split('_')])
        headers += '{}: {}\n'.format(header, value)

    return (
        '{method} HTTP/1.1\n'
        'Content-Length: {content_length}\n'
        'Content-Type: {content_type}\n'
        '{headers}\n\n'
        '{body}'
    ).format(
        method=request.method,
        content_length=request.META['CONTENT_LENGTH'],
        content_type=request.META['CONTENT_TYPE'],
        headers=headers,
        body=request.body,
    )


def stop_using_unicode(x):

    def unicode_to_str(x):
        return x.normalize("NFKD").encode("ascii", "ignore")

    return {unicode_to_str(k): unicode_to_str(v) for k, v in x.items()}


@csrf_exempt
def sigfox_webhook(request):
    # Check the X-Hub-Signature header to make sure this is a valid request.
    # github_signature = request.META['HTTP_X_HUB_SIGNATURE']
    # signature = hmac.new(settings.GITHUB_WEBHOOK_SECRET, request.body, hashlib.sha1)
    # expected_signature = 'sha1=' + signature.hexdigest()
    # if not hmac.compare_digest(github_signature, expected_signature):
    #    return HttpResponseForbidden('Invalid signature header')

    # Sometimes the payload comes in as the request body, sometimes it comes in
    # as a POST parameter. This will handle either case.

    #f1_logger = function_logger(logging.DEBUG, logging.ERROR)
    

    

    

    
    pr_print = pretty_request(request)
    print("DEBUG:sigfox_webhook:pr_print: {}".format(pr_print))

    if 'data' in request.POST:
        data = json.loads(request.POST['data'])
        print(('sigfox_webhook Log: 1. POST <data> received the {} device'.format(data)))
    else:
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        print("DEBUG:sigfox_webhook:body_data: {}".format(body_data))

        data = body_data
        #data = json.loads(request.body)
        print("DEBUG:Body: {}".format(request.body))
        #print("{}".format(request.headers))
        #print(('sigfox_webhook Log: 2. <body> received the {} device'.format(data)))
        print('DEBUG:sigfox_webhook Log: 2. NO POST <body> received')
        print((json.dumps(data, indent=4)))

        data_unicode = request.body.decode('utf-8')
        data = json.loads(data_unicode)
        print("DEBUG:stop_using_unicode(data): {}".format(data))

    handle_sigfox_webhook(data, request)


    # request.META['HTTP_X_GITHUB_EVENT']

    # This is where you'll do something with the webhook
    #request_in = request.POST.copy()
    #print(('sigfox_webhook> request_in {}'.format(request_in)))

    #handle_sigfox_webhook(event, request)
    #print(('sigfox_webhook> data {}'.format(data)))
    #print(('sigfox_webhook> data:data {} '.format(data['data'])))

    #data_payload = data['data']   # Use this data for decode info
    # sigfox_iot(request)
    data_payload = data

    return HttpResponse(data_payload, status=http.client.ACCEPTED)


#class CallbackView(View):

#   def post(self, request, *args, **kwargs):
#        data = json.loads(request.body)
#        logging.info("The Callback sends me this: %s" % data)