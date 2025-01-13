from django.contrib import admin

from todo.models import TodoList


class TodoListAdmin(admin.ModelAdmin):
  list_display = ("title", "description",)

# Register your models here.
admin.site.register(TodoList,TodoListAdmin)