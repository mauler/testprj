from django.db import models

from functools import partial


ValueField = partial(models.DecimalField, max_digits=5, decimal_places=2)
