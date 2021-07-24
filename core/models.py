from django.db import models
class Client(models.Model):  
	name=models.CharField(max_length=70)
	age=models.IntegerField()
	salary=models.DecimalField(max_digits=7,decimal_places=2)
	anand = models.DateField(null=True,blank=True)
	ad = models.DateField(null=True,blank=True)

	def gatfullname(self):
		return self.name +  str(self.age)

	def __str__(self):
		return self.gatfullname()

class images(models.Model):
	image=models.ImageField()

class user(models.Model):
	name=models.CharField(max_length=70)
	age=models.IntegerField()
	salary=models.DecimalField(max_digits=7,decimal_places=2)
	mail=models.EmailField(max_length=70)

	def email(self):
		return self.mail

	def __str__(self):
		return self.email()