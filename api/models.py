from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        RECRUITER = 'RECRUITER', 'Recruiter'
        SEEKER = 'SEEKER', 'Job Seeker'

    base_role = Role.SEEKER
    role = models.CharField(max_length=50, choices=Role.choices, default=base_role)
    email = models.EmailField(unique=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
        super().save(*args, **kwargs)

class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    website = models.URLField(blank=True, null=True)
    location = models.CharField(max_length=255)
    recruiter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='companies')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class JobPosting(models.Model):
    JOB_TYPES = [
        ('FULL_TIME', 'Full-time'),
        ('PART_TIME', 'Part-time'),
        ('REMOTE', 'Remote'),
        ('INTERN', 'Internship'),
    ]

    title = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='job_postings')
    description = models.TextField()
    requirements = models.TextField()
    location = models.CharField(max_length=255)
    salary_range = models.CharField(max_length=100, blank=True, null=True)
    job_type = models.CharField(max_length=20, choices=JOB_TYPES, default='FULL_TIME')
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} at {self.company.name}"

class Application(models.Model):
    STATUS_CHOICES = [
        ('APPLIED', 'Applied'),
        ('REVIEWING', 'Reviewing'),
        ('INTERVIEW', 'Interview Scheduled'),
        ('OFFERED', 'Offered'),
        ('REJECTED', 'Rejected'),
    ]

    job = models.ForeignKey(JobPosting, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='APPLIED')
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('job', 'applicant')

    def __str__(self):
        return f"{self.applicant.username} -> {self.job.title}"