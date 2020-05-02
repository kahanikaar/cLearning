#!/usr/bin/python
# -*- coding: utf-8 -*-def handle_user_response(request):
    """ response handler function"""# twilio passes key pressed digits via form-data form key value Digitsdigits = request.POST.get('Digits', '')
    response = VoiceResponse()# evaluate user input from phones keypad and take an appropriate actionif digits == '1':
        response.play('http://demo.twilio.com/hellomonkey/monkey.mp3')
    if digits == '2':
        number = request.POST.get('From', '')
        response.say('Thank you for calling, for more content see site blog'
                     )
        response.sms('Thanks for trying out this tutorial, share with your friends!'
                     , to=number)# HttResponse will return xml response object for twilio api to processreturn HttpResponse(str(response), content_type='application/xml')
