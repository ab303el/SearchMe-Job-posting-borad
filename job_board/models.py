from django.db import models

# Create your models here.
# job posting table
#  title , description , company , salary

class jobPosting(models.Model):

    # id - starts at 1 and autoincrements 

    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=100)
    salary = models.IntegerField()
    is_active = models.BooleanField(default= False)
    category = models.TextField(default='General')
    jobcategories = models.ForeignKey('jobcategories', on_delete=models.CASCADE , null=True,blank=True )
    # pk = models.ForeignKey(
    #     jobcategories,  # Reference the Category model
    #     on_delete=models.CASCADE,  # Delete job postings if category is deleted
    #     related_name="job_postings"  # Enables reverse access from Category to JobPosting
    # )

    def __str__(self):
        return f"{self.jobcategories}|{self.category}|{self.title} |{self.company} | Active:{self.is_active}"
    
class jobcategories(models.Model):
    categoryName = models.CharField(max_length=100)
    image_link = models.CharField(max_length=250)
    images = models.ImageField(upload_to='images/' , default='empty')

    def __str__(self):
        return f"{self.pk}|{self.categoryName}"
    