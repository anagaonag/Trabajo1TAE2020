from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from predictor.serializers import PredictorSerializer
from predictor.models import Predictor
from rest_framework.decorators import action
import joblib
from datetime import datetime,timedelta
import numpy as np
import pandas as pd


#Carga de modelos predictivos (/modelos)
#scalers
min_max_scaler_dia=joblib.load('predictor/modelos/scaler_dia.pkl')
min_max_scaler_mes=joblib.load('predictor/modelos/scaler_mes.pkl')

#SVM
svm_dia=joblib.load('predictor/modelos/svm_dia.pkl')
svm_mes=joblib.load('predictor/modelos/svm_mes.pkl')
min_max_scaler_dia=joblib.load('predictor/modelos/scaler_dia.pkl')

#BOSQUES
bosque_dia = joblib.load('predictor/modelos/bosque_tuning_dia.pkl')
bosque_mes = joblib.load('predictor/modelos/bosque_tuning_mes.pkl') 

def PrepararData(data):
    if(data['resoluciontemporal']=='d'):   
        inicial = datetime.strptime(data['fecha_inicial'].replace('-','/'), '%Y/%m/%d')
        final = datetime.strptime(data['fecha_final'].replace('-','/'), '%Y/%m/%d')
        rango = final-inicial
        #formatox = ['Barrio_encoder','DIA','MES','Año','Especial']
        #[[],[],[]]
        Matrix= []
        for barrio_enc in range(0,303):
            bar = 0
            for i in range(0,rango.days+1):        
                fecha = inicial+timedelta(days=i)
                especial = 0
                dia = fecha.day
                mes = fecha.month
                anio = fecha.year
                Matrix.append([float(barrio_enc),float(dia),float(mes),float(anio),float(especial)])
                #normalizacion de datos
        marray = pd.DataFrame(Matrix)
        X_val_dia = min_max_scaler_dia.transform(marray)
        
        
        y_pred_dia = svm_dia.predict(X_val_dia)        
        y_pred_dia = pd.DataFrame(y_pred_dia) ##esto es lo que se envia
        print(y_pred_dia)
    




def TipoPredictor(data):
    #if(data['resoluciontemporal']=='d'):    
        
    #elif(data['resoluciontemporal']=='m'):
    
    #elif(data['resoluciontemporal']=='s'):
    
    return True



class PredictorViewSet(viewsets.ModelViewSet):    
    queryset = Predictor.objects.all()
    serializer_class = PredictorSerializer    
    
    @action(detail=False,methods=['post'])
    def predecir(self, request):      
        serializer = PredictorSerializer(data=request.data)      
        
        #Validaciones
        if(serializer.is_valid()): 
            modeloLearning = serializer.data['Modelo']
            if(modeloLearning=='SVM'):
                PrepararData(serializer.data)
                return Response({'Mensage':'svm'})
            elif(modeloLearning=='RF'):
                return Response({'Mensage':'rf'})
        else:
            return Response({'Errors':serializer.errors})