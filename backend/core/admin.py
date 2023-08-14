from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import *
from django.utils.html import format_html
from .models import Employment, Candidate, Company, EmployerHR, CandidateKYC, BankingInfo\
    

class CandidateKYCInline(admin.StackedInline):
    model = CandidateKYC
    max_num = 1
    can_delete = False


class BankingInfoInline(admin.StackedInline):
    model = BankingInfo


class PersonContactInline(admin.StackedInline):
    model = PersonalContacts


class EmpoyerHRInline(admin.StackedInline):
    model = EmployerHR


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    inlines = [
        CandidateKYCInline,
        BankingInfoInline,
        PersonContactInline,
    ]

    def candidate_location(self, obj):
        if obj.personalcontacts:
            return f"{obj.personalcontacts.region} - {obj.personalcontacts.country}"
        return ""
    candidate_location.short_description = "Location"

    def candidate_contact(self, obj):
        if obj.personalcontacts:
            if obj.personalcontacts.phone_number != obj.personalcontacts.whatsapp_number:
                    return f"WhatsApp:{obj.personalcontacts.phone_number} - Other:{obj.personalcontacts.country}"
            else:
                return f"WhatsApp:{obj.personalcontacts.phone_number}"
        return ""
    candidate_contact.short_description = "Contact Details"

    list_display = ['full_name','age','education_level','prefered_industry','salary_expectation','candidate_contact','candidate_location']
    


@admin.register(Employment)
class EmploymentAdmin(admin.ModelAdmin):
    pass

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    inlines = [
        EmpoyerHRInline,
    ]
    list_display = ['name', 'sector']
    
