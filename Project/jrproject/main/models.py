from django.db import models

# Create your models here.

#User for the repo
class Artificat(models.Model):
    Art_ID = 
    Art_Name = 
    Date_Mod = 
    Type = 
    Comp_ID = 


class Component(models.Model):
    Comp_ID = 
    Comp_Name = 
    Layer = 


class State(models.Model):
    State_ID = 
    Art_ID = 
    S_Name = 



class Version(models.Model):
    Ver_ID = 
    Ver_Name = 
    Art_ID = 
    Date = 



class LOB(models.Model):
    LOB_ID = 
    Name = 


class EA3_LOB_lvl(models.Model):
    EA3_LOB_ID = 
    LOB_ID = 
    EA_lvl_ID = 


class EA3_Level(models.Model):
    Art_ID = 
    Art_Name = 
    Date_Mod = 
    Type = 
    Comp_ID = 