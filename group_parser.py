import vk_api, time
from vk_api.longpoll import VkLongPoll, VkEventType

def save(data, name):
	with open(name, "w") as file:
		for item in data:
			file.write(str(item) + "\n")

def main():
	global api
	vk_session = vk_api.VkApi(token='') #можно узнать на vkhost.github.io
	api = vk_session.get_api()
		
	try:
		g_id = 1 #цифровой айди группы
		st = 'id_asc' #сортировка. Можно указать: id_asc — в порядке возрастания id; id_desc — в порядке убывания id; time_asc — в хронологическом порядке по вступлению в сообщество; time_desc — в антихронологическом порядке по вступлению в сообщество, time_asc и time_desc работает только при вызове от модератора сообщества.
		i = 0
		get = api.groups.getMembers(group_id=g_id, sort=st)
		count = get['count']
		items = get['items']
		while i < count:
			for i in range(1, count+1):
				items = items + api.groups.getMembers(group_id=g_id, sort=st, offset=i*1000)["items"]
				save(items, f'group{g_id}.txt')
	except Exception as error:
		print(error)
			
			
main()
