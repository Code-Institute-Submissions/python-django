from django.contrib import admin

# Register your models here.
from products.models import Feature, Bug, BugComment, FeatureComment


admin.site.register(Bug)

admin.site.register(Feature)

admin.site.register(BugComment)

admin.site.register(FeatureComment)



