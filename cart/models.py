from django.db import models

# Create your models here.

class cart_details(models.Model):
	book_id = models.CharField(max_length=1500)
	user_name = models.CharField(max_length=120)
	auther_names = models.CharField(max_length=120)
	book_prices= models.CharField(max_length=1500)
	book_img= models.CharField(max_length=1500)
	quantity = models.CharField(max_length=10)
	


