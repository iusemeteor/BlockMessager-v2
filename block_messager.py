import requests
import keyboard

with open('token.txt', 'r') as file:
    token = file.read()

channel = input("What's the channel id? ")
user = input("What's the user id? ")
msg = input("What's the message you would like to send? ")


def send_message():
    global res_msg
    url = "https://discord.com/api/v9/channels/ " + channel + "/messages"

    payload = {
        "content": msg
    }

    headers = {
        "Authorization": token
    }
    res_msg = requests.post(url, payload, headers=headers)
    if res_msg.status_code == 400:
        print("I could not block message, maybe invalid channel id? ")
        exit()
    if res_msg.status_code == 401:
        print("I could not block message, maybe invalid token? ")
        exit()
    elif res_msg.status_code == 200 or 204:
        pass
    else:
        print(res_msg.status_code)


def block():
    global res_block
    headers = {
        'authorization': token,
        'content-type': 'application/json',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9151 Chrome/120.0.6099.291 Electron/28.2.10 Safari/537.36',
    }

    json_data = {
        'type': 2,
    }

    res_block = requests.put(
        'https://discord.com/api/v9/users/@me/relationships/' + user,
        headers=headers,
        json=json_data,
    )
    if res_block.status_code == 401:
        print("I could not block, maybe invalid token? ")
        exit()
    elif res_block.status_code == 404:
        print("I could not block, maybe invalid user id?")
    elif res_block.status_code == 200 or 204:
        pass
    else:
        print(res_block.status_code)


def unblock():
    global res_unblock
    headers = {
        'authorization': token,
        'content-type': 'application/json',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9151 Chrome/120.0.6099.291 Electron/28.2.10 Safari/537.36',
    }

    json_data = {
        'type': 2,
    }

    res_unblock = requests.delete(
        'https://discord.com/api/v9/users/@me/relationships/' + user,
        headers=headers,
        json=json_data,
    )
    if res_unblock.status_code == 401:
        print("Pretty sure this is an invalid token.")
        exit()
    elif res_unblock.status_code == 404:
        print("I could not unblock, maybe invalid user id?")
    elif res_unblock.status_code == 200 or 204:
        pass
    else:
        print(res_unblock.status_code)


def check_if_we_chillin():
    good = (200, 204)
    if res_msg.status_code in good and res_block.status_code in good and res_unblock.status_code in good:
        print("Successfully block message'd " + user + ".")
    else:
        print("Could not block message " + user + ".")

def do_it_again():
    print("Press F6 to block message that user again.")
    while True:
        try:
            if keyboard.is_pressed('F6'):
                unblock()
                send_message()
                block()
                check_if_we_chillin()
        except:
            exit()


if __name__ == '__main__':
    unblock()
    send_message()
    block()
    check_if_we_chillin()
    do_it_again()
