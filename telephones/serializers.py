from rest_framework import serializers
from .models import Assign

class FullnameField(serializers.RelatedField):
    def to_representation(self, value):
        return f"{value.first_name} {value.last_name}"

class DepNameField(serializers.RelatedField):
    def to_representation(self, value):
        return f"{value.dep_title} {value.dep_name}"

class PosTitleField(serializers.RelatedField):
    def to_representation(self, value):
        return value.title

class DutiesField(serializers.RelatedField):
    def to_representation(self, value):
        return value.duties

class DutiesField(serializers.RelatedField):
    def to_representation(self, value):
        return value.duties

class ExtensionField(serializers.RelatedField):
    def to_representation(self, value):
        return value.extension

class CompleteNumberField(serializers.RelatedField):
    def to_representation(self, value):
        return value.complete_number

class DescField(serializers.RelatedField):
    def to_representation(self, value):
        return value.description


class AssignNameSerializer(serializers.ModelSerializer):
    # PrimaryKeyRelatedField
    full_name = FullnameField(source='position.owner', read_only=True)
    position = PosTitleField(source='position.position_type', read_only=True)
    dep = DepNameField(source='position.dep', read_only=True)
    duties = DutiesField(source='position', read_only=True)
    extension = ExtensionField(source='tel', read_only=True)
    complete_number = CompleteNumberField(source='tel', read_only=True)
    description = DescField(source='tel', read_only=True)
  
    class Meta:
        model = Assign
        fields = (
            'full_name',
            'position',
            'dep',
            'duties',
            'extension',
            'complete_number',
            'description')