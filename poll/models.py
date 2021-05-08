from django.db import models



# Create your models here.
class Poll(models.Model):

  STATUS = (
  (0,"Draft"),
  (1, "Publishe"),
)

  title = models.CharField(max_length=100)
  question = models.CharField(max_length=200, )
  active_until = models.DateTimeField(auto_now=True)
  status = models.IntegerField(choices=STATUS, default=0)

  def __str__(self):
    return f"{self.title} - Active until: {self.active_until}" 

class Option(models.Model):
 
  poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
  title = models.CharField(max_length=100)

  def __str__(self):
    return self.title

class Response(models.Model):
  
  option = models.ForeignKey(Option, on_delete=models.CASCADE)
  name = models.CharField(max_length=50)
  response_time = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.name} - Response time: {self.response_time}"