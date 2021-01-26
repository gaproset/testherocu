from django.contrib import admin
from .models import Ekdilwsi # add this
from .models import Invite
from .models import partnersType
from .models import partners
from .models import library
from .models import attendancelogger


class EkdilwsiAdmin(admin.ModelAdmin):  # add this
    list_display = ('id','name', 'description','info', 'place','happeningdate', 'organizer')

class InviteAdmin(admin.ModelAdmin):  # add this
    list_display = ('id','ekdilwsiinvited','fromUser', 'toUser', 'sentdate','isopened', 'isAccepted','isRejected','isDeciding')

class partnersTypeAdmin(admin.ModelAdmin):  # add this
    list_display = ('id','typename')

class partnersAdmin(admin.ModelAdmin):  # add this
    list_display = ('id', 'afm', 'cost','details')

class libraryAdmin(admin.ModelAdmin):  # add this
    list_display = ('id','name','location')

class attendanceloggerAdmin(admin.ModelAdmin):  # add this
    list_display = ('id','first_name','last_name', 'email', 'credentials','libraryvisited', 'section','reason','timelogged')


admin.site.register(Ekdilwsi, EkdilwsiAdmin)
admin.site.register(Invite, InviteAdmin)
        
admin.site.register(partnersType, partnersTypeAdmin)
admin.site.register(partners, partnersAdmin)
        
admin.site.register(library, libraryAdmin)
admin.site.register(attendancelogger, attendanceloggerAdmin)
        


