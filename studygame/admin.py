from django.contrib import admin
from studygame.models import *
# Register your models here.


class VocabularyAdmin(admin.ModelAdmin):
    fieldsets = [
        ('', {'fields': ['word','paraphrase','subject','pronunciation']})
    ]
    list_display = ('word','paraphrase','subject','pronunciation')
    search_fields = ['word','paraphrase','subject','pronunciation']
    list_filter = ['subject']

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name','describe', 'subject', 'reward')
    search_fields = ['name', 'subject']
    list_filter = ['subject']

admin.site.register(Vocabulary,VocabularyAdmin)
admin.site.register(Item)
admin.site.register(Task,TaskAdmin)
admin.site.register(TaskItem)
admin.site.register(TaskAbility)
