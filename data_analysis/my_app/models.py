from django.db import models

# Create your models here.
# class user_info(models.Model):
#     username=models.OneToOneField(User)


class plot_information(models.Model):
    type_of_graph=models.CharField(max_length=256,blank=True,null=True)
    data_file=models.FileField(upload_to="datasets",null=True,blank=True)
    title=models.CharField(max_length=256)
    no_of_var=models.PositiveIntegerField()
    x_col=models.PositiveIntegerField()
    y_col=models.PositiveIntegerField(blank=True,null=True)
    #graph=models.CharField(max_length=256)

 