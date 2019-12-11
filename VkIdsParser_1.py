import vk_api
import time
import codecs


if __name__ == '__main__':
    # Заходим ВКонтакте под своим логином
    vk_session = vk_api.VkApi('логин ВК', 'Пароль ВК')
    vk_session.auth()
    vk = vk_session.get_api()

    # Пишем возраст от и до людей которых надо спарсить
    age = 18
    age_max = 30

    # Номер города
    city_number = 104

    # 1 - девушки, 2 - парни
    gender = 1

    # Открываем файл для записи результатов
    ff = codecs.open('ids.txt', 'w', encoding='utf8')

    # Перебор возрастов
    while age <= age_max:
        month = 1
        # Перебор месяцев рождения
        while month <= 12:
            # Пауза для API
            time.sleep(4)
            # Пишем какую группу людей качаем
            print('Download ID: ' + str(age) + ' age, born in ' + str(month))
            # Получаем 1000 юзеров - их ФИО, айди, и фотку
            z = vk.users.search(count=1000,
                                fields='id, photo_max_orig, has_photo, '
                                       'first_name, last_name',
                                city=city_number,
                                sex=gender,
                                age_from=age,
                                age_to=age,
                                birth_month=month)
            month = month + 1
            print('Peoples count: ' + str(z['count']))
            for x in z['items']:
                if x['has_photo'] == 1:
                    # Записываем данные о юзере в файл разделяя черточкой |
                    s = str(x['id']) + '|' + str(x['photo_max_orig']) + '|' + str(
                        x['first_name']) + ' ' + str(x['last_name']) + '\n'
                    ff.write(s)
        age = age + 1

    ff.close()
    print('Done!')
