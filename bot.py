import bottle
import requests
import os


@bottle.post('/')
def main():
    bot_token = os.environ.get("token")
    data = bottle.request.json
    response = {
        "chat_id": data['message']['chat']['id'],
        "text": data['message']['text']
    }
    requests.post("https://api.telegram.org/bot" + bot_token + "/sendMessage", json=response)
    print(data)
    print(response)
    return


if __name__ == '__main__':
    bottle.run(host='0.0.0.0', port=8080, debug=True)
