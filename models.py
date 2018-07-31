from django.db import models

class description(models.Model):
	book_name=models.CharField(max_length=50)
	book_price=models.IntegerField(default=0)
	book_author=models.CharField(max_length=60)

	def __str__(self):
		return self.book_name
