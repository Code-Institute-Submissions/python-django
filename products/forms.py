from django import forms
from products.models import Feature, FeatureComment, Bug, BugComment
from django.db import models
from django.views.generic import ListView, DetailView

class FeatureForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = ('first_name', 'last_name', 'email_address', 'web_address', 'summary_of_feature', 'detail_description_of_feature', 'date_of_feature', 'status', 'address_one', 'city', 'state','credit_crd_num','expiring_month_credit_crd', 'expiring_year_credit_crd', 'card_cvv', 'stripe_id')


class FeatureCommentForm(forms.ModelForm):
    class Meta:
        model = FeatureComment
        fields = ('comment_submitted', 'date_of_published')



class BugForm(forms.ModelForm):
    
    class Meta:
        model = Bug
        
        fields = ('first_name', 'last_name', 'email_address', 'web_address', 'summary_of_bug', 'detail_description_of_bug', 'date_of_bug', 'status')



class BugCommentForm(forms.ModelForm):
    class Meta:
        model = BugComment
        fields = ('comment_submitted', 'date_of_published')

  