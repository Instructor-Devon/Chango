from django.db import models

# Create your models here.
class Monkey(models.Model):
    
    # first_name VARCHAR(255)
    first_name = models.CharField(max_length=255)
    # last_name
    last_name = models.CharField(max_length=255)
    # email
    email = models.EmailField(unique=True)
    # phonenumber
    phone_number = models.IntegerField()
    password = models.CharField(max_length=255)


    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    # created_posts => [Post, Post, Post]

    def __str__(self):
        return "Monkey: {}".format(self.first_name)

class Post(models.Model):
    content = models.CharField(max_length=255)

    # SPECIAL
    # monkey_id ??
    author = models.ForeignKey(Monkey, related_name="created_posts")
    # likers = models.ManyToManyField(Monkey, related_name="liked_posts")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

# Monkey => m
# m.first_name => "Ray"
# m.created_posts.all() => [Post, Post, Post]
# m.liked_posts => [Post, Post, Post]

# Post => p
# p.created_at => 1/3/98
# p.content => "sup yall METALICA!!!!"
# p.author.first_name => "Ray"
# p.likers => [Monkey, Monkey]

# "likes"
# monkey_id
# post_id
# created_at
# is_upvote (reddit)
# emoji (facebook)