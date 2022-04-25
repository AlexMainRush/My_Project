from django.db import models


class CreateUser(models.Model):
    name = models.CharField(max_length=60, null=True)
    email = models.EmailField(null=True)

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return f'{self.name} {self.email}'
