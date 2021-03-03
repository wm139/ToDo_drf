from task.models import Task
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
    create_time = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'complete_flag', 'create_time']

    def get_create_time(self, obj):
        return {'date': obj.create_time.date(),
                'time': obj.create_time.time()}
''
