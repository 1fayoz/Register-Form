from django.db import models

# class  Authors(models.Model):
#     name = models.CharField(max_length=50)
#     bio = models.TextField()

# class Genres(models.Model):
#     name = models.CharField(max_length=100)
#     discription = models.TextField()

# class Book(models.Model):
#     title = models.CharField(max_length=70)
#     discription = models.TextField()
#     genres_id = models.ForeignKey(Genres, on_delete=models.PROTECT) 


# class Books_authors(models.Model):
#     book_id = models.ForeignKey(Book, on_delete=models.PROTECT)
#     author_id = models.ForeignKey(Authors, on_delete= models.PROTECT)
#     is_main_author = models.BooleanField(default=True)

 
class registration(models.Model):
    ism_falmilya = models.CharField(max_length= 70)
    yosh = models.IntegerField()
    telfon_nomer = models.IntegerField()
    radio = models.CharField(max_length= 70)
    email = models.EmailField()

    def __str__(self) :
        return self.ism_falmilya














