from django.contrib import admin
from todo.models import TodoList


# Register your models here.

@admin.register(TodoList)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['task', 'create_date', 'dueon_date', 'owner', 'mark']
    search_fields = ['owner', 'task']
    list_filter = ['create_date']
