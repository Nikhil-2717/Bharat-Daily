from django.db import models
from django.contrib.auth.models import User
class Category(models.Model):
    category_name=models.CharField(max_length=50,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):       #It is the strign representation of the category model 
        return self.category_name

 # Here we are mkaing this beacuse we want the status of teh blog to be either draft or published so we will use it as dropdown   
STATUS_BLOG =( 
    ("draft","Draft"),
    ("published","Published")
)
    
class Blog(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150,unique=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author=models.ForeignKey(User , on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='uplaod/%Y/%m/%d') #we are creating a folder and mentionig the date time year for the image 
    
    short_description = models.TextField(max_length=500)
    blog_body =models.TextField(max_length=2000)
    status = models.CharField(max_length=20,choices=STATUS_BLOG)
    featured = models.BooleanField(default=False)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    marked_posts = models.ManyToManyField(
        User,
        blank=True,
        related_name='saved_posts'
    )

    def __str__(self):
        return self.title
    
class SocialLink(models.Model):
    platform=models.CharField(max_length=50)
    link = models.URLField(max_length=100)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.platform
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
    


