# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Diseases(models.Model):
    iddisease = models.IntegerField(db_column='idDisease', primary_key=True)  # Field name made lowercase.
    diseasename = models.CharField(db_column='diseaseName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    prevalence = models.CharField(db_column='Prevalence', max_length=30, blank=True, null=True)  # Field name made lowercase.
    affectedsystem = models.CharField(db_column='AffectedSystem', max_length=30, blank=True, null=True)  # Field name made lowercase.
    treatment = models.CharField(db_column='Treatment', max_length=100, blank=True, null=True)  # Field name made lowercase.
    diagnosis = models.TextField(db_column='Diagnosis', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    #created=models.DateTimeField(auto_now_add=True)
    #updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'diseases'

    def __str__(self):
        return 'Name: %s, Prevalence: %s, AffectedSystem: %s, treatment: %s' %(self.diseasename, self.prevalence, self.affectedsystem, self.treatment)


class Resourcestype(models.Model):
    idtype = models.IntegerField(db_column='idType', primary_key=True)  # Field name made lowercase.
    Type = models.CharField(db_column='Type', max_length=40, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    #created=models.DateTimeField(auto_now_add=True)
    #updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Type: %s, idtype: %s' %(self.Type, self.idtype)

    class Meta:
        managed = False
        db_table = 'resourcestype'


class Url(models.Model):
    idurl = models.IntegerField(db_column='idURL', primary_key=True)  # Field name made lowercase.
    #language = EnumField(db_column='Language', values=('English','Spanish','Spanish/English','Others'))
    language = models.CharField(db_column='Language', max_length=15, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=300, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=60, blank=True, null=True)  # Field name made lowercase.
    #created=models.DateTimeField(auto_now_add=True)
    #updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'ID: %s, Language: %s, Address: %s, Location: %s' %(self.idurl, self.language, self.address, self.location)

    class Meta:
        managed = False
        db_table = 'url'


class Resources(models.Model):
    idresources = models.IntegerField(db_column='IdResources', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    #finality = EnumField(db_column='Finality', values=('Academic','Informative','Academic/Informative'))
    #price = EnumField(db_column='Price', values=('Free','Paid'))
    #access = EnumField(db_column='Access', values=('Public','Private'))
    finality = models.CharField(db_column='Finality', max_length=20, blank=True, null=True)  # Field name made lowercase.
    price = models.CharField(db_column='Price', max_length=4, blank=True, null=True)  # Field name made lowercase.
    access = models.CharField(db_column='Access', max_length=7, blank=True, null=True)  # Field name made lowercase.
    resources_diseases = models.ManyToManyField(Diseases, through='ResourcesDiseases')
    resources_resourcestype = models.ManyToManyField(Resourcestype, through='ResourcesResourcestype')
    resources_url = models.ManyToManyField(Url, through='ResourcesUrl')
    #created=models.DateTimeField(auto_now_add=True)
    #updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Name: %s, Finality: %s, Price: %s, Access: %s' %(self.name, self.finality, self.price, self.access)


    class Meta:
        managed = False
        db_table = 'resources'


class ResourcesDiseases(models.Model):
    idresource = models.ForeignKey(Resources, db_column='idResource',on_delete=models.CASCADE)
    iddisease = models.ForeignKey(Diseases, db_column='idDisease',on_delete=models.CASCADE)
    #idresource = models.IntegerField(db_column='idResource', primary_key=True)  # Field name made lowercase.
    #iddisease = models.IntegerField(db_column='idDisease')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'resources_diseases'
        unique_together = (('idresource', 'iddisease'),)


class ResourcesResourcestype(models.Model):
    idresource = models.ForeignKey(Resources, db_column='idResource',on_delete=models.CASCADE)
    idresourcetype = models.ForeignKey(Resourcestype, db_column='idResourceType',on_delete=models.CASCADE)
    #idresource = models.IntegerField(db_column='idResource', primary_key=True)  # Field name made lowercase.
    #idresourcetype = models.IntegerField(db_column='idResourceType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'resources_resourcestype'
        unique_together = (('idresource', 'idresourcetype'),)


class ResourcesUrl(models.Model):
    idresource = models.ForeignKey(Resources, db_column='idResource',on_delete=models.CASCADE)
    idurl = models.ForeignKey(Url, db_column='idURL',on_delete=models.CASCADE)
    #idresource = models.IntegerField(db_column='idResource', primary_key=True)  # Field name made lowercase.
    #idurl = models.IntegerField(db_column='idURL')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'resources_url'
        unique_together = (('idresource', 'idurl'),)
