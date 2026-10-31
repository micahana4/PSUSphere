from rest_framework import serializers
from studentorg.models import College, Student, Program # <-- update

class CollegeSerializer(serializers.ModelSerializer):
  class Meta:
      model = College
      fields = '__all__'
    #   fields = ['college_name', 'created_at', 'updated_at']

# Serializer for Student (nested in Program)
class StudentSerializer(serializers.ModelSerializer):
    program_name = serializers.CharField(source='program.prog_name', read_only=True)
    college_name = serializers.CharField(source='program.college.college_name', read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'student_id', 'lastname', 'firstname', 'middlename', 'program', 'program_name', 'college_name']
        read_only_fields = ['program_name', 'college_name']

# Serializer for Program with nested students
class ProgramSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, read_only=True, source='student_set')
    college_name = serializers.CharField(source='college.college_name', read_only=True)

    class Meta:
        model = Program
        fields = ['id', 'prog_name', 'college', 'college_name', 'students']
        
      