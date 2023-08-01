from django.db import models

class FormData(models.Model):
    first_name = models.CharField(max_length=100)
    country_of_residence = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    email_id = models.EmailField(unique=True, default='example@example.com')
    phone_number = models.CharField(max_length=20)
    current_company = models.CharField(max_length=100)
    current_role = models.CharField(max_length=100)
    company_worked_at = models.CharField(max_length=100)
    title_at_company = models.CharField(max_length=100)
    relationship_description = models.TextField()
    duration_of_knowing = models.CharField(max_length=100)
    linked_in_url = models.CharField(max_length=100, default='A summery of what you have done as a professional')
    Q1_1 = models.CharField(max_length=100, default='A summery of what you have done as a professional')
    Q1_2 = models.CharField(max_length=50000, default='A list of your roles and the impact you have made while in the '
                                                      'position')
    Q1_3 = models.CharField(max_length=100, default='A summery of what you have done as a professional')
    Q2_1 = models.CharField(max_length=100,  default='A summery of what you have done as a professional')
    Q2_2 = models.CharField(max_length=100, default='A summery of what you have done as a professional')
    Q2_3 = models.CharField(max_length=100,  default='A summery of what you have done as a professional')
    Q2_4 = models.CharField(max_length=100,  default='A summery of what you have done as a professional')
    Q2_5 = models.CharField(max_length=100, default='A summery of what you have done as a professional')
    Q2_6 = models.CharField(max_length=100, default='A summery of what you have done as a professional')
    Q2_7 = models.CharField(max_length=100,  default='A summery of what you have done as a professional')
    Q3_1 = models.CharField(max_length=100, default='A summery of what you have done as a professional')
    Q3_2 = models.CharField(max_length=100, default='A summery of what you have done as a professional')
    Q3_3 = models.CharField(max_length=100, default='A summery of what you have done as a professional')
    Q4 = models.CharField(max_length=100, default='A summery of what you have done as a professional')
    Q4_1 = models.CharField(max_length=100, default='A summery of what you have done as a professional')
    Q5_1 = models.CharField(max_length=100, default='A summery of what you have done as a professional')
    Q5_2 = models.CharField(max_length=100, default='A summery of what you have done as a professional')
    Q6_1 = models.CharField(max_length=100, default='A summery of what you have done as a professional')
    Q6_2 = models.CharField(max_length=100, default='A summery of what you have done as a professional')
    Q7_1 = models.CharField(max_length=100, default='A summery of what you have done as a professional')
    Q7_2 = models.CharField(max_length=100, default='A summery of what you have done as a professional')





class NewTest1(models.Model):
    Que1 = models.TextField()
    Que2 = models.TextField()
    Que3 = models.TextField()
    Que4 = models.TextField()
    
