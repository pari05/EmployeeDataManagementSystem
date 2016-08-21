from django.db import models
#from django.utils.encoding import smart_unicode

# Create your models here.

class Employee(models.Model):
	Name = models.CharField(max_length=200)
	Age = models.IntegerField()
	EmployeeID = models.IntegerField(primary_key=True)
	Email = models.EmailField()
	Sex = models.CharField(max_length = 100)
	Phonenumber = models.IntegerField()

	def __unicode__(self):
		#return self.Name + "/" + str(self.Age) + "/" + str(self.EmployeeID) + "/"+ smart_unicode(self.Email)+" "
		return self.Name + "/" + str(self.Age) + "/" + str(self.EmployeeID) +"/" + smart_unicode(self.Email)+"/" + self.Sex + "/" + str(self.phonenumber)+" "
