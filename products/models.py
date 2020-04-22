from django.db import models
from django.conf import settings
from django.utils import timezone
import stripe
from django.views.generic import ListView, DetailView



class MyModel(models.Model):
    pass



class Feature(models.Model):
    STATUS_CHOICES = ( 
        ('todo', 'To Do'),
        ('inprogress', 'In Progress'),
        ('done', 'Done')
    )
    the_month_of_exp = [(i, i) for i in range(1,13)]
    
    the_year_of_exp = [(i, i) for i in range(2020, 2030)]
    

    first_name = models.CharField('First Name', max_length=120)
    last_name = models.CharField('Last Name', max_length=120)
    email_address = models.EmailField('Email Address', blank=True)
    web_address = models.URLField('Web Address', blank=True)
    summary_of_feature = models.TextField(max_length=1000, help_text='Enter a brief description of the feature')
    detail_description_of_feature = models.TextField(max_length=3000, help_text='Enter a detail description of the feature')
    date_of_feature = models.DateField('When do you want it fixed by', null=True, blank=True)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default="todo")
    user_rec = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    address_one = models.CharField(max_length= 100, default='')
    city = models.CharField(max_length= 50, default='')
    state = models.CharField(max_length= 2, default='')
    stripe_id = models.CharField(max_length=30, blank=True)
    credit_crd_num = models.CharField('Please enter in credit card number',null=True, max_length=120)
    expiring_month_credit_crd = models.CharField('month', choices=the_month_of_exp,null=True, max_length=120)
    expiring_year_credit_crd = models.CharField('year', choices=the_year_of_exp,null=True, max_length=120)
    card_cvv = models.CharField('Your cvv at back of credit card',null=True, max_length=120)

    class Meta:
        verbose_name_plural = 'subscriber'

    def __unicode__(self):
        return u"%s's Subscription Info" % self.user_rec

    def charge(self, request, email, fee):
        # Set your secret key: remember to change this to your live secret key
        # in production. See your keys here https://manage.stripe.com/account
        stripe.api_key = settings.STRIPE_SECRET_KEY

        # Get the credit card details submitted by the form
        token = request.POST['stripeToken']

        # Create a Customer
        stripe_customer = stripe.Customer.create(
            card=token,
            description=email
        )

        # Save the Stripe ID to the customer's profile
        self.stripe_id = stripe_customer.id
        self.save()

        # Charge the Customer instead of the card
        stripe.Charge.create(
            amount=fee, # in cents
            currency="usd",
            customer=stripe_customer.id
        )

        return stripe_customer

    def __str__(self):
        return self.first_name

class FeatureComment(models.Model):
    on_delete= models.CASCADE
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    bug = models.ForeignKey(Feature, null=True,on_delete=models.CASCADE)
    comment_submitted = models.TextField(max_length=500)
    date_of_published = models.DateTimeField(blank=True, null=True, default=timezone.now)
    
    def __str__(self):
        return self.comment_submitted

class FeatureUserVotes(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)


class Bug(models.Model):
    STATUS_CHOICES = ( 
        ('todo', 'To Do'),
        ('inprogress', 'In Progress'),
        ('done', 'Done')
    )
    first_name = models.CharField('First Name', max_length=120)
    last_name = models.CharField('Last Name', max_length=120)
    email_address = models.EmailField('Email Address', blank=True)
    web_address = models.URLField('Web Address', blank=True)
    summary_of_bug = models.TextField(max_length=1000, help_text='Enter a brief description of the bug')
    detail_description_of_bug = models.TextField(max_length=3000, help_text='Enter a brief description of the bug')
    date_of_bug = models.DateField('Date of submission of bug', null=True, blank=True)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default="todo")

    def __str__(self):
        return self.first_name


class BugComment(models.Model):
    on_delete= models.CASCADE
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    bug = models.ForeignKey(Bug, null=True,on_delete=models.CASCADE)
    comment_submitted = models.TextField(max_length=500)
    date_of_published = models.DateTimeField(blank=True, null=True, default=timezone.now)
    
    def __str__(self):
        return self.comment_submitted

class BugUserVotes(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,on_delete=models.CASCADE)
    bug = models.ForeignKey(Bug, null=True, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.bug

class BugView(ListView):
    template_name = 'view_bug.html'
    context_object_name = 'bug_list'

    def get_queryset(self):
        return Bug.objects.all()
  
class FeatureView(ListView):
    template_name = 'view_feature.html'
    context_object_name = 'feature_list'

    def get_queryset(self):
        return Feature.objects.all()
  






    