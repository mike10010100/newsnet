from django.db import models

# Create your models here.
class Post(models.Model):
    post_text = models.CharField(max_length=2000)
    pub_date = models.DateTimeField('date published')


class Comment(models.Model):
    post = models.ForeignKey(Post)
    choice_text = models.CharField(max_length=2000)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)