from django.db import models


class Menu(models.Model):
    item = models.TextField(
        max_length=64,
        verbose_name="menu_item",
        help_text='item'
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='link to item',
        help_text='slug'
    )

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"

    def __str__(self):
        return self.item
