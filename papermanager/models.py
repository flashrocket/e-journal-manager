from django.db import models
from django.contrib.auth.models import User
from slugger.fields import AutoSlugField

# Create your models here.
class Paper(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    author=models.ForeignKey(User)
    public=models.BooleanField(default=False)
    slug = AutoSlugField(populate_from='name',unique=True)

    def __str__(self):
        return self.name

class PaperVersion(models.Model):
    SUBMISSION_CHOICES=(
        ("latex","Lamport TeX (LaTeX)"),
        ("pdf","Portable Document Format (PDF)"),
    )
    paper=models.ForeignKey(Paper)
    name=models.CharField(max_length=20)
    submissionType=models.CharField(max_length=7,choices=SUBMISSION_CHOICES)
    submissionDate=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name

class PaperFiles(models.Model):
    filename=models.CharField(max_length=255)
    filedata=models.BinaryField()