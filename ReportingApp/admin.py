from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from .models import QALabSupport
from .models import SmartTerminalDefect
from .models import LaunchpadDefects
from .models import Dashboard

class ReportAdmin(ImportExportModelAdmin):
    list_display = ('Name', 'Priority', 'State','Attachements')
    change_list_template = 'admin\\ReportingApp\\QALabSupport\\change_list.html'
admin.site.register(QALabSupport, ReportAdmin)

class ReportAdmin(ImportExportModelAdmin):
    list_display=('DName','DSeverity', 'DPriority', 'DState','DAttachements')
    change_list_template = 'C:\\Users\\akaja\\PycharmProjects\\Report\\templates\\admin\\ReportingApp\\SmartTerminalDefect\\change_list.html'
admin.site.register(SmartTerminalDefect,ReportAdmin)

class ReportAdmin(ImportExportModelAdmin):
    list_display=('LName','LSeverity', 'LPriority', 'LState','LAttachements')
admin.site.register(LaunchpadDefects,ReportAdmin)

class ReportAdmin(admin.ModelAdmin):
    list_display=('LName','LSeverity', 'LPriority')
admin.site.register(Dashboard,ReportAdmin)
