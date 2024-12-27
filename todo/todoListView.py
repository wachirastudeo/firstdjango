from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Todo
from .todoSerializer import TodoSerializer

class TodoListView(APIView):
    def get(self, request):
        todos = Todo.objects.all()  # ตรวจสอบโมเดล Todo
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
    

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
