from cProfile import label
from django.db import models
from django.contrib.auth.models import User

class Card(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name='message_owner')
    card_id=models.IntegerField(default=-1)
    content=models.TextField(max_length=1000)
    point=models.IntegerField(default=-1)
    pub_date=models.DateTimeField(auto_now_add=True)
    card1=models.IntegerField(default=-1)
    card2=models.IntegerField(default=-1)
    card3=models.IntegerField(default=-1)
    card4=models.IntegerField(default=-1)
    card5=models.IntegerField(default=-1)
    card6=models.IntegerField(default=-1)
    card7=models.IntegerField(default=-1)
    card8=models.IntegerField(default=-1)
    card9=models.IntegerField(default=-1)
    card10=models.IntegerField(default=-1)
    card11=models.IntegerField(default=-1)
    card12=models.IntegerField(default=-1)
    card13=models.IntegerField(default=-1)

    def __str__(self):
        return str(self.content)+'('+str(self.owner)+')'

    class Meta:
        ordering=('-pub_date',)






