from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe


class QALabSupport(models.Model):
    Name = models.CharField(max_length=2083,default='null')
    #Severity = models.CharField(max_length=2083,default='null')
    Priority = models.CharField(max_length=2083,default='null')
    State = models.CharField(max_length=2083,default='null')
    Attachements = models.FileField(upload_to='media',default='null')

class SmartTerminalDefect(models.Model):
    DName = models.CharField(max_length=2083, default='null')
    DSeverity = models.CharField(max_length=2083,default='null')
    DPriority = models.CharField(max_length=2083, default='null')
    DState = models.CharField(max_length=2083, default='null')
    DAttachements = models.FileField(upload_to='media', default='null')

class LaunchpadDefects(models.Model):
    LName = models.CharField(max_length=2083, default='null')
    LSeverity = models.CharField(max_length=2083,default='null')
    LPriority = models.CharField(max_length=2083, default='null')
    LState = models.CharField(max_length=2083, default='null')
    LAttachements = models.FileField(upload_to='media', default='null')

class Dashboard(models.Model):
    LName = models.CharField(max_length=2083, default='null')
    LSeverity = models.CharField(max_length=2083, default='null')
    LPriority = models.CharField(max_length=2083, default='null')
