from django.db import models

# Create your models here.
class User(models.Model):    
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 15)
    password = models.CharField(max_length = 32)
    email = models.CharField(max_length = 30)
    
    def __str__(self):
        return self.id + ' ' +self.name + ' ' + self.password
    
    


    

class Game(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 30)
    country = models.CharField(max_length = 30)
    
class Comment(models.Model):
    user_id =  models.ForeignKey(User,on_delete=models.CASCADE)
    game_id =  models.ForeignKey(Game,on_delete=models.CASCADE)
    text = models.CharField(max_length = 400)

class Vote(models.Model):
    user_id =  models.ForeignKey(User,on_delete=models.CASCADE)
    game_id =  models.ForeignKey(Game,on_delete=models.CASCADE)
    vote = models.BooleanField(default = True)