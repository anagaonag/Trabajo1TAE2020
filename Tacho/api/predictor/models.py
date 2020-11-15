from django.db import models

# Create your models here.
class Predictor(models.Model):
    choiceResolucion =[
        ('d','Dia'),
        ('m','Mes'),
        ('s','Semana')    
    ]
    choiceModels = [
        ('SVM','SoporteVectorial'),
        ('RF','BosquesAleatorios')
    ]
    fecha_inicial = models.DateField()
    fecha_final = models.DateField()
    resoluciontemporal = models.CharField(max_length=100,choices=choiceResolucion)
    Modelo = models.CharField(max_length=100,choices=choiceModels,default=choiceModels[0])