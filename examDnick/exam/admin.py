from django.contrib import admin
from exam.models import Profesor, Exam, ExamProfesor
# Register your models here.
class ProfesorAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser
class ExamProfesorAdmin(admin.StackedInline):
    model = ExamProfesor
    extra = 0
class ExamAdmin(admin.ModelAdmin):
    exclude = ('profesor', 'user',)
    inlines = [ExamProfesorAdmin]
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(ExamAdmin, self).save_model(request, obj, form, change)
    def has_delete_permission(self, request, obj=None):
        return obj and obj.user == request.user


admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Exam, ExamAdmin)
admin.site.register(ExamProfesor)
