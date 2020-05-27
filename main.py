from config import token, chat
# you need token and chat_id in your config file

import vk_api
from random import randrange
import datetime
import time
import sys


def captcha_handler(captcha):
    key = input("Enter captcha code {0}: ".format(captcha.get_url())).strip()
    return captcha.try_again(key)


def main():
    while True:
        try:
            if datetime.datetime.now().hour != 15 and not sys.argv[1] == "test":
                print(datetime.datetime.now().hour)
                time.sleep(60 * 60)
                continue
            vk_session = vk_api.VkApi(token=token, captcha_handler=captcha_handler)
            vk = vk_session.get_api()
            poll = vk.polls.create(
                question="Фамия, %s" % str(datetime.datetime.now()), is_multiple=1,
                add_answers="[\"21:00\", \"21:30\", \"22:00\", \"22:30\", \"Позже\", \"хз\", \"Нет\"]")
            poll_att = "poll{}_{}".format(poll['owner_id'], poll['id'])
            id = randrange(10 ** 9)
            message_id = vk.messages.send(peer_id=2000000000 + chat, message="", random_id=id, attachment=poll_att)
            print(id)
            try:
                vk.messages.pin(peer_id=2000000000 + chat, message_id=message_id)
            except Exception as e:
                print(e)
                pass
            time.sleep(60 * 60)
        except KeyboardInterrupt as e:
            print('Get interrupt signal, stopping')
            break

        except Exception as e:
            print(e)
            pass


if __name__ == '__main__':
    main()
