from django.db import models

class Person(models.Model):
    iin = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.iin}"

    def save(
        self,
        *args,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        nums = list(map(int, self.iin))[:11]
        sum_ = sum((idx+1) * val for idx, val in enumerate(nums))
        if sum_ % 11 != int(self.iin[11]):
            raise ValueError("Incorrect IIN")

        super().save()
