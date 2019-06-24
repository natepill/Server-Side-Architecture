from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    """
        Choice objects are edited on the Question admin page. By default,
        provides enough fields for 3 choices.
    """
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None,{'fields': ['question_text']}),('Date information', {'fields': ['pub_date']})]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # adds a “Filter” sidebar to filter the change list by the pub_date field
    list_filter = ['pub_date']

    # adds a search box at the top of the change list page and searches term in
    # question_text field
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
