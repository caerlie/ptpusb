#!/usr/bin/env python
# -*- coding: utf-8 -

class PtpApi(object):

    def __init__(self):
        self.ssesion_id = None
        self.transaction_id = 0
        self.usb = None

    def send(self, operation, response, data):
        self.response = None

        if operation.code == 0x1002:
            self.ssesion_id = 0
            self.transaction_id = 0

        result = sendreq(operation)

        if data is not None:
            result = senddata(operation, data)

        response = getresp()

        self.transaction_id+=1


        


    
