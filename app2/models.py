from django.db import models
class Religion(models.Model):
    RELIGION_NO = models.IntegerField(default=None,null=True, blank=True)
    RELIGION_NAME = models.CharField(max_length=20,null=True, blank=True)
    class Meta:
        db_table = "RELIGION"
class Caste(models.Model):
    CASTE_NO = models.IntegerField(default=None,null=True, blank=True)
    CASTE_NAME = models.CharField(max_length=20,null=True, blank=True)
    class Meta:
        db_table = "CASTE"
class SuplHead(models.Model):
    SUPLNO = models.IntegerField(default=None,null=True, blank=True)
    SUPLHEAD_NAME = models.CharField(max_length=30,null=True, blank=True)
    class Meta:
        db_table = "SUPLHEAD"
class Title(models.Model):
    TITLE_NO = models.IntegerField(default=None,null=True, blank=True)
    TITLE_NAME = models.CharField(max_length=20,null=True, blank=True)
    class Meta:
        db_table = "TITLE"
class Designature(models.Model):
    DESIGNATURE_NO = models.IntegerField(default=None,null=True, blank=True)
    DESIGNATURE_NAME = models.CharField(max_length=20,null=True, blank=True)
    class Meta:
        db_table = "DESIGNATURE"
class Category(models.Model):
    CATEGORY_NO = models.IntegerField(default=None,null=True, blank=True)
    CATEGORY_NAME = models.CharField(max_length=20,null=True, blank=True)
    class Meta:
        db_table = "CATEGORY"
class TypeTran(models.Model):
    TYPETRAN_NO = models.IntegerField(default=None,null=True, blank=True)
    TYPETRAN_NAME = models.CharField(max_length=20,null=True, blank=True)
    class Meta:
        db_table = "TYPETRAN"
