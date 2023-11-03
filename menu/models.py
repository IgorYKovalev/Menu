from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class MenuItem(MPTTModel):
    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='название'
    )

    slag = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name='url'
    )

    position = models.PositiveIntegerField(
        'Позиция',
        default=1
    )

    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )

    class MPTTMeta:
        order_insertion_by = ['position']

    def __str__(self):
        return str(self.name)

