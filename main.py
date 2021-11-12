from pollbot import PollBot

def main():

    user = 'email@nyu.edu'
    password = 'password'
    host = 'jeffepsteinnyu'

    # If you're using a non-UW PollEv account,
    # add the argument "login_type='pollev'"
    with PollBot(user, password, host, login_type='pollev', open_wait=30) as bot:
        bot.run()


if __name__ == '__main__':
    main()
