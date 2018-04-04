from django.db import models

from functools import partial


# Field used for A, B Values
ABValueField = partial(models.DecimalField, max_digits=5, decimal_places=2)
