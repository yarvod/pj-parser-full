import json
import logging
import os
import argparse
from dotenv import load_dotenv
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest

from serializers import MessageRawSeralizer


logger = logging.getLogger(__name__)
load_dotenv()


def main() -> None:

    parser = argparse.ArgumentParser(
        prog='Parsing Posts from telegram channel',
        description='Parsing Posts from telegram channel'
    )
    parser.add_argument('-c', '--channel', help='username of telegram channel', type=str, required=True)
    parser.add_argument('-l', '--limit', help='limmit number of posts, default 100', type=int, default=100)
    args = parser.parse_args()

    api_id = os.getenv('API_ID', '')
    api_hash = os.getenv('API_HASH', '')
    phone = os.getenv('PHONE', '')

    client = TelegramClient('session', api_id, api_hash)

    client.connect()
    if not client.is_user_authorized():
        client.send_code_request(phone)
        me = client.sign_in(phone, input('Enter code: '))

    channel_username=args.channel
    limit = args.limit

    serialized = MessageRawSeralizer(client.get_messages(channel_username, limit=limit), many=True).data

    with open('data.json', 'w', encoding='utf8') as f:
        json.dump(serialized, f, indent=4, ensure_ascii=False)



if __name__ == '__main__':
    main()
