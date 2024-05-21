from django.contrib import admin
from .models import Profile

# ProfileAdmin ke thua tu lop admin.ModelAdmin 
class ProfileAdmin(admin.ModelAdmin):
    #cac truong hien thi trend ds profile
    list_display = ["id", "pkid", "user", "gender", "phone_number", "country", "city"]
    #cac truong se duoc su dung de loc ket qua tren danh sach
    list_filter = ["gender", "country", "city"]
    #cac truog hien thi duoi dang lien ket
    list_display_links = ["id", "pkid", "user"]

#dang ki Profile va ProfileAdmin vao trang quan li
admin.site.register(Profile, ProfileAdmin)