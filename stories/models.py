from django.db import models
from ckeditor.fields import RichTextField



# Create your models here.
class Poem(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length = 100)
    bio = models.TextField(blank=False)
    content = RichTextField()
    publication_date = models.DateField(auto_now_add=True)
    cover_photo = models.ImageField(upload_to='images/poem_covers', blank=True)

    def __str__(self):
        return self.title
    
def story_cover_upload_path(instance, filename):
    # Generate the upload path for each Story instance
    return f'story_covers/{filename}'
    
class Story(models.Model):
    title = models.CharField(max_length = 100)
    first_letter = models.TextField(max_length=1,blank=True)
    content = RichTextField()
    bio = models.TextField(blank=False)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    publication_date = models.DateField(auto_now_add=True)
    cover_photo = models.ImageField(upload_to=story_cover_upload_path, blank=True)

    def __str__(self):
        return self.title
    
class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField(unique=True)
    profile_image = models.ImageField(upload_to='images/author_profiles/', blank=True)

    def __str__(self):
        return self.name
