from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Category(MPTTModel):
	parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
	title = models.CharField(max_length = 100)
	icon = models.CharField(max_length = 3000)
	description = RichTextField()
	created = models.DateField(auto_now_add = True)
	updated = models.DateField(auto_now = True)

	def __str__(self) -> str:
		return self.title
		
	class MPTTMeta:
		order_insertion_by = ['title']

class Post(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE )
	author = models.ForeignKey(User, related_name="author", on_delete=models.CASCADE, blank = True, null=True)
	title = models.CharField(max_length = 200)
	image = models.ImageField(blank = True, upload_to = 'images', null = True)
	details = RichTextField()
	liked = models.ManyToManyField(User, blank=True, related_name='liked')
	created = models.DateField(auto_now_add = True)
	updated = models.DateField(auto_now = True)
	
	def __str__(self):
		return self.title

	@property
	def like_total(self):
		return self.likes.all().count()
		
	def get_absolute_url(self):
		return reverse('home')
	
	def image_tag(self):
		if self.image.url is not None:
			return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
		else:
			return ""

LIKE_CHOICES = (
	('like','like'),
	('unlike', 'unlike'),
)
class Like(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
	post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True)
	value = models.CharField(choices=LIKE_CHOICES, default='like', max_length=10)

	def __str__(self) -> str:
		return self.post
	

class Images(models.Model):
    product=models.ForeignKey(Post,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

class Headline(models.Model):
	title = models.CharField(max_length=200)
	image = models.URLField(null=True, blank=True)
	url = models.TextField()
	created = models.DateField(auto_now_add = True)
	updated = models.DateField(auto_now = True)
	
	def __str__(self):
		return self.title