
from .models import Alumno
from rest_framework import serializers

class AlumnoSerializer(serializers.ModelSerializer):

    #Fields = {
        # School Controll : school_controll, 
        # FullName : name, 
        # Age : age, 
        # Email : email,
    #}  

    class Meta:
        model = Alumno
        fields = '__all__'
