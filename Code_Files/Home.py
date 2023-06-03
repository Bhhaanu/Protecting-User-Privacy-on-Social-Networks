import PySimpleGUI as sg
#import tweepy
#from tweepy import OAuthHandler
import rake

#access_token = "1281942076796485637-GhFJsNUM7wbEJYdPJCPe2Ug2fcr3U9"
#access_token_secret = "Pwybdg2fC1oddODv9i6WjmWFdzOOEPZTf69PgumIKvyOS"
#consumer_key = "OeuM5VDa9fJuLWTT3ktuTnM1n"
#consumer_secret = "WsBUWXEE3tPCTxOTLuUDZGMeEV6UxT5BtkiG4pzYpoFvH7bI"

def base64_to_style_image(base64_image):
    return "url('data:image/png;base64," + base64_image + "')"

#auth = OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)
#api = tweepy.API(auth)


layout = [[sg.Text('Tweet', size=(15, 1)), sg.Multiline('', key='msg')],
          [sg.Submit(), sg.Cancel()]]

window = sg.Window('Twitter Home page', layout)
while True:
    event, values = window.Read()
    if event in (None, 'Cancel'):
        break
    if event == 'Submit':
        msg = values['msg']
        print('You entered', msg)
        is_privacy = rake.Rake(msg)
        if is_privacy:
            sg.popup('This has some personal information')
        else:
            sg.popup('Tweet was posted!')
            window['msg'].update('')
window.close()
