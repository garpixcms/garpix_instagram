import os
import glob
from instabot import Bot
from .models import InstagramHashtag, InstagramPost  # noqa
import shutil


class Instagram:
    def __init__(self, username=os.getenv('INSTAGRAM_USERNAME'), password=os.getenv('INSTAGRAM_PASSWORD')):
        self.username = username
        self.password = password
        cookie_del = glob.glob("config/*cookie.json")
        if cookie_del:
            os.remove(cookie_del[0])
        shutil.rmtree('config', ignore_errors=True)
        bot = Bot()
        bot.login(username=self.username, password=self.password)
        self.bot = bot

    def update_base(self):
        self.get_posts_by_hashtags()

    def get_posts_by_hashtags(self):
        hashtags = InstagramHashtag.objects.all().values('title')
        hashtag_list = []
        instagram_posts_bulk_create = []
        for hashtag in hashtags:
            hashtag_list.append(hashtag['title'])
        posts = self.bot.get_hashtag_medias(hashtag_list, filtration=False)
        for post in posts:
            media_info = self.bot.get_media_info(post)[0]
            username = media_info['user']['username']
            kwargs = {
                'user_name': username,
                'user_image': media_info['user']['profile_pic_url'],
                'user_link': f'https://www.instagram.com/{username}/',
                'post_link': f'https://www.instagram.com/p/{media_info["code"]}/',
                'like_count': media_info['like_count'],
                'post_image': media_info['image_versions2']['candidates'][0]['url'],
            }
            instagram_post = InstagramPost(**kwargs)
            instagram_posts_bulk_create.append(instagram_post)
        InstagramPost.objects.bulk_create(instagram_posts_bulk_create)
