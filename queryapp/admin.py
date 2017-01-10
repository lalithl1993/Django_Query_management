from django.contrib import admin
from queryapp.models import *

class studentAdmin(admin.ModelAdmin):
	list_display= ["__str__","id","name","usn","password"]
	class Meta:
		model = student 


class teacherAdmin(admin.ModelAdmin):
	list_display= ["__str__","id","name","password"]
	class Meta:
		model = teacher



class questionAdmin(admin.ModelAdmin):
	list_display= ["__str__","id","question","status"]
	class Meta:
		model = question 


class answerAdmin(admin.ModelAdmin):
	list_display= ["__str__","id","qid","answer"]
	class Meta:
		model = answer 


admin.site.register(loginInfo)
admin.site.register(student,studentAdmin)
admin.site.register(teacher,teacherAdmin)
admin.site.register(question,questionAdmin)
admin.site.register(answer,answerAdmin)


