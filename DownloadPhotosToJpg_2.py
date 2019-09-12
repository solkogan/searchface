import vk_api
import time, shutil
import random, codecs, os, requests

def loadfile(name,url):
    if not(os.path.exists('jpg/'+str(name)+'.jpg')):
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open('jpg/'+str(name)+'.jpg', 'wb') as f:
               r.raw.decode_content = True
               shutil.copyfileobj(r.raw, f)

vk_session = vk_api.VkApi('логин ВК', 'Пароль ВК')
vk_session.auth()

vk = vk_session.get_api()

ff=codecs.open(u'ids.txt', 'r', encoding='utf8')

def getphotosbyid(userid):
    try:
        z=vk.photos.getAll(owner_id=userid, count=50, no_service_albums=0)
        prev=''
        flag=0
        fotki=[]
        for x in z['items']:
            for t in x['sizes']:
               s=str(t['url'])
               mas=s.split('/')
               ident=mas[4]
               if(prev!=ident):
                   prev=ident
                   flag=0
               else:
                   flag=flag+1
                   if(flag==3):
                       fotki.append(s)
        maxflag=0
        for t in fotki:
            maxflag=maxflag+1
            if(maxflag<10):
                loadfile(str(userid)+'_'+str(maxflag),t)
    except:
        pass
e=0
for x in ff:
    e=e+1
    print(e)
    mas=x.split('|')
    userid=int(mas[0])
    getphotosbyid(userid)
    


