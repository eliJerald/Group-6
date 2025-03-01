"""
Courses Models Serializers.
This module defines serializers for the models in the courses app.
Serializers are used to convert model instances into JSON format (and vice versa)
for use in RESTful APIs. They also handle validation and simplify the creation
and updating of model instances.
"""

from rest_framework import serializers
from courses import models
from users import serializers as user_serializer

# ------------------------------------------------------------
# ProfessorSerializer
# ------------------------------------------------------------
class ProfessorSerializer(serializers.ModelSerializer):
    """Professor Model Serializer.
    
    This serializer handles the serialization of the Professor model.
    It is set up to serialize all fields of the Professor model.
    
    Note:
      - The nested user serializer is commented out. If you need detailed user
        information in the API responses, you can uncomment the line below.
    """
    # Uncomment the following line to nest detailed user data.
    # user = user_serializer.UserSerializer(read_only=True)
    
    class Meta:
        # Specify the model that this serializer is for.
        model = models.Professor
        # Serialize all fields from the Professor model.
        fields = "__all__"

# ------------------------------------------------------------
# ClassSerializer
# ------------------------------------------------------------
class ClassSerializer(serializers.ModelSerializer):
    """Class Model Serializer.
    
    This serializer is used for the Class model and only includes the 'name'
    field. It is used to provide a concise representation of a class in API responses.
    """
    class Meta:
        # Define the model to be serialized.
        model = models.Class
        # Only include the 'name' field in the serialized output.
        fields = ['name']

# ------------------------------------------------------------
# SemesterSerializer
# ------------------------------------------------------------
class SemesterSerializer(serializers.ModelSerializer):
    """Semester Model Serializer.
    
    This serializer handles the Semester model and provides a simple representation
    by including only the 'name' field.
    """
    class Meta:
        # Set the model for serialization.
        model = models.Semester
        # Only include the 'name' field.
        fields = ['name']

# ------------------------------------------------------------
# ProfessorClassSectionSerializer
# ------------------------------------------------------------
class ProfessorClassSectionSerializer(serializers.ModelSerializer):
    """ProfessorClassSection Model Serializer.
    
    This serializer handles the ProfessorClassSection model and is designed to
    work with both read and write operations:
    
    - For read operations, it provides a nested representation of related fields:
        - 'semester' is represented using the SemesterSerializer.
        - 'class_instance' is represented using the ClassSerializer.
    
    - For write operations, it accepts only the primary key IDs for the nested
      relationships:
        - 'semester_id' is used to set the 'semester' field.
        - 'class_instance_id' is used to set the 'class_instance' field.
    
    This design simplifies the API for clients by allowing them to send only the
    necessary IDs when creating or updating instances, while still receiving
    detailed nested data when retrieving objects.
    """
    # For read operations: nested, detailed representation of the semester.
    semester = SemesterSerializer(read_only=True)
    # For read operations: nested, detailed representation of the class.
    class_instance = ClassSerializer(read_only=True)

    # For write operations: accept only the primary key (ID) for the semester.
    semester_id = serializers.PrimaryKeyRelatedField(
        # Provide a queryset to validate the input against existing Semester instances.
        queryset=models.Semester.objects.all(),
        # Map this field to the 'semester' attribute of the model.
        source='semester',
        # Set as write-only to ensure it is only used for creating/updating data.
        write_only=True
    )
    # For write operations: accept only the primary key (ID) for the class.
    class_instance_id = serializers.PrimaryKeyRelatedField(
        # Provide a queryset to validate the input against existing Class instances.
        queryset=models.Class.objects.all(),
        # Map this field to the 'class_instance' attribute of the model.
        source='class_instance',
        # Set as write-only to ensure it is only used for creating/updating data.
        write_only=True
    )

    class Meta:
        # Specify the model that this serializer targets.
        model = models.ProfessorClassSection
        # Define the fields to be included in the serialized output:
        # - 'section_number': The section number for the class section.
        # - 'semester': The detailed (nested) representation of the semester.
        # - 'semester_id': The ID used to set the semester during write operations.
        # - 'class_instance': The detailed (nested) representation of the class.
        # - 'class_instance_id': The ID used to set the class during write operations.
        fields = [
            'section_number',
            'semester',
            'semester_id',
            'class_instance',
            'class_instance_id'
        ]


