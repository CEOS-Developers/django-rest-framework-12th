from django.contrib import admin

# Register your models here.
from .models import Profile
from .models import Routine
from .models import Workout
from .models import Training
from .models import Set

admin.site.register(Profile)
admin.site.register(Routine)
admin.site.register(Workout)
admin.site.register(Training)
admin.site.register(Set)
