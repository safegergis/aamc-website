from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import tweepy
auth = tweepy.OAuthHandler('TWWewG75yzhwKeWrOWlILowmV', 'I8cruG8zoTe0QsrnPjgAfMhIQRWDYjkTb2EmD3vkG8AqfEsepC')
auth.set_access_token('706178168789422080-lEwkuL8hzBvZ5UEFyeVc7eDJjdXZfda','R1sg7JoTlhCKr6Vraf3NTimjGP1h3st84EsUOQsomQ9mz')
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
