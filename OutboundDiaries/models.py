from django.db import models

class branch(models.Model):
    branch = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.branch}"

class university(models.Model):
    university = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.university}"

class out_stu(models.Model):
    year = models.PositiveIntegerField()
    image = models.ImageField(blank=True, null=True, upload_to = '%Y/%m/%d/')
    name = models.CharField(max_length=50)
    branch = models.ForeignKey(branch, on_delete=models.CASCADE, related_name="branch_students")
    university = models.ForeignKey(university, on_delete=models.CASCADE, related_name="uni_students")
    area = models.CharField(max_length=50)
    duration = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.year}: {self.name} of {self.branch} in {self.area}"

class interview(models.Model):
    student = models.ForeignKey(out_stu, on_delete=models.CASCADE, related_name="faq")
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return f"{self.question}:{self.answer}"