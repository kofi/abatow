from django.contrib import admin

# Register your models here.
from .models import Country, Congress, Region, Election, Result, Party, Candidate


    
class CountryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"nameslug": ("name",)}  
    list_display = ("name","total_registered")

class PartyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"nameslug": ("name",)} 

class RegionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"nameslug": ("name",)} 

class ResultAdmin(admin.ModelAdmin):
    list_display = ("candidate", "votes", "result_region", "result_party", 
                 "result_congress","result_electiontype", "created_at", "updated_at",
                 "is_published", "date_published")
    list_filter = ['date_published']
    search_fields = ["votes",]

class ResultInline(admin.TabularInline):
    model = Result
    extra = 6

class ElectionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"name": ("congress","region","electiontype_text",)}
    list_display = ('congress', 'electiontype_text', 'region')
    #fieldsets = fieldset + []
    inlines = [ResultInline]
    
class CandidateAdmin(admin.ModelAdmin):
    prepopulated_fields={"nameslug" : ("firstname","middlename","lastname",)}
    list_display = ('firstname', 'middlename', 'lastname', 'party')

class CongressAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "election_date", "country")

admin.site.register(Country,CountryAdmin)
admin.site.register(Congress,CongressAdmin)
admin.site.register(Region,RegionAdmin)
admin.site.register(Election,ElectionAdmin)
admin.site.register(Result,ResultAdmin)
admin.site.register(Party,PartyAdmin)
admin.site.register(Candidate,CandidateAdmin)