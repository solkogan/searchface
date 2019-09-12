import vk_api
import time, codecs
import os, sys, shutil, requests
import os.path
# Заходим ВКонтакте под своим логином
vk_session = vk_api.VkApi('логин ВК', 'Пароль ВК')
vk_session.auth()
vk = vk_session.get_api()

# Пишем возраст от и до людей которых надо спарсить
vozrast=18
vozrastmax=30

# Номер города
citynumber=104

# 1 - девушки, 2 - парни
psex=1

# Открываем файл для записи результатов
ff=codecs.open('ids.txt', 'w', encoding='utf8')

# Перебор возрастов
while(vozrast<=vozrastmax):
    mesac=1
    # Перебор месяцев рождения
    while(mesac<=12):
        # Пауза для API
        time.sleep(4)
        # Пишем какую группу людей качаем
        print('Download ID: '+str(vozrast)+' age, born in '+str(mesac))
        # Получаем 1000 юзеров - их ФИО, айди, и фотку 
        z=vk.users.search(count=1000, fields='id, photo_max_orig, has_photo, first_name, last_name', city=citynumber, sex=psex, age_from=vozrast, age_to=vozrast, birth_month=mesac)
        mesac=mesac+1
        print('Peoples count: '+str(z['count']))
        for x in z['items']:
            if(x['has_photo']==1):
                # Записываем данные о юзере в файл разделяя черточкой |
                s=str(x['id'])+'|'+str(x['photo_max_orig'])+'|'+str(x['first_name'])+' '+str(x['last_name'])+'\n'
                ff.write(s)
    vozrast=vozrast+1

ff.close()
print('Done!')


