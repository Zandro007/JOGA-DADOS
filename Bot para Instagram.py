from instabot import Bot
bot = Bot()
bot.login(username="", password="")

bot.upload_photo('image.jpg',
                 caption='type oyur picture here')

bot.follow('elonrmuskk')

bot.send_message('Hello from codehub',['user1', 'user2'])

my_followers = bot.get_user_followers('codehub.py')
for follower in my_followers:
    print(follower)

bot.unfollow_everyone()
