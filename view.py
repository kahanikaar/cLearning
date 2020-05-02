#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.http import HttpResponsedef init_automated_call(request):
    """ initial end point called by twilio on making a phone call to your twilio number"""response = VoiceResponse()
    voice_message = \
        'Welcome to tiptapcode Press one to hear a monkey, two to receive an SMS'with response.gather(action='/respond/', num_digits=1) as g:
        g.say(voice_message)
        g.pause(length=1)# if user does not response with an option
    # call your http://{domain}/gather end point again to repeat optionsresponse.redirect('/gather/')# HttResponse will return xml response object for twilio api to processreturn HttpResponse(str(response), content_type='application/xml')
