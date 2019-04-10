from django.db import models

# Create your models here.
class book_category(models.Model):
	book_category_name = models.CharField(max_length=120)
	def __str__(self):
		return self.book_category_name


class book_details(models.Model):
	book_cat = models.ForeignKey(book_category, on_delete=models.CASCADE)
	book_name = models.CharField(max_length=120)
	auther_name = models.CharField(max_length=120)
	book_price= models.CharField(max_length=1500)
	book_img= models.FileField()
	book_pdf = models.FileField()
