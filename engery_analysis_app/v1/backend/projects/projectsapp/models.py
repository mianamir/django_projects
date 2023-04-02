from django.db import models

class Projects(models.Model):

    project_name = models.CharField(max_length=100, null=True, blank=True)
    project_number = models.CharField(max_length=100, null=True, blank=True)
    acquisition_date = models.EmailField(max_length=100, null=True, blank=True)
    number_3l_code = models.EmailField(max_length=100, null=True, blank=True)
    project_deal_type_id = models.EmailField(max_length=100, null=True, blank=True)
    project_group_id = models.EmailField(max_length=100, null=True, blank=True)
    company_id = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'projects'

    def __str__(self):
        return self.project_name

    def __repr__(self):
        return self.project_name
