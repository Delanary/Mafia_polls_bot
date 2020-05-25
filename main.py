from config import token, chat
# you need token and chat_id in your config file

import vk_api
from random import randrange
import datetime
import time


def main():
    while True:
        try:
            if datetime.datetime.now().hour != 15:
                time.sleep(60 * 60)
                print(datetime.datetime.now().hour)
                continue
            vk_session = vk_api.VkApi(token=token)
            vk = vk_session.get_api()
            poll = vk.polls.create(
                question="Фамия, %s" % str(datetime.datetime.now().day) + str(datetime.datetime.now().month) + str(
                    datetime.datetime.now().year), is_multiple=1,
                add_answers="[\"21:00\", \"21:30\", \"22:00\", \"22:30\", \"Позже\", \"хз\", \"Нет\"]")
            poll_att = "poll{}_{}".format(poll['owner_id'], poll['id'])
            vk.messages.send(peer_id=2000000000 + chat, message="", random_id=randrange(10 ** 9), attachment=poll_att)
        except:
            pass


if __name__ == '__main__':
    main()
