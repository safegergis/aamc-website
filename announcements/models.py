from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import tweepy
auth = tweepy.OAuthHandler('J3SwYatgiR5M1xt6O6x7cjvuj', 'XisaR4offolPVvQznlrHPlxQt5lSmC3l7bTHoyYiE1Zy4HyULs')
auth.set_access_token('255237367-5NICERfrsEswrN2xTkFFDkSJKlt1JOIFDNExTcdB','OMcyYRX2rU4RwQRW79Lv6WdBuAu0puGPNOki79qAT7MU6')
api = tweepy.API(auth)

class Post(models.Model):
	title = models.CharField(max_length=88)
	body = models.TextField(max_length=1000)
	date = models.DateTimeField()

	def __str__(self):
		return self.title
		return self.body
@receiver(post_save,sender=Post)
def new_post_event(sender,instance,created,**kwargs):
	if created:
		api.update_status('"{}" Read more at archangelmichaeloc.org/announcements/{}'.format(instance.title,instance.pk))
