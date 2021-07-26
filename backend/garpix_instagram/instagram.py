import os
import glob
from instabot import Bot
from .models import InstagramHashtag, InstagramPost  # noqa
import shutil


class Instagram(object):

    def __init__(self, username=os.getenv('INST_USERNAME'), password=os.getenv('INST_PASSWORD')):
        self.username = username
        self.password = password
        cookie_del = glob.glob("config/*cookie.json")
        if cookie_del:
            os.remove(cookie_del[0])
        shutil.rmtree('config')
        bot = Bot()
        bot.login(username=self.username, password=self.password)
        self.bot = bot

    def update_base(self):

        self.get_posts_by_hashtags()

    def get_posts_by_hashtags(self):

        hashtags = InstagramHashtag.objects.all()
        hashtag_list = []
        for hashtag in hashtags:
            hashtag_list.append(hashtag.title)
        posts = self.bot.get_total_hashtag_medias(hashtag_list)
        for post in posts:
            media_info = self.bot.get_media_info(post)
            print(media_info)
            # InstagramPost.objects.create(user_name=post.owner_username, like_count=post.likes,
            #                              user_link=post.url, user_image=post.owner_profile.profile_pic_url,
            #                              post_image=post)
