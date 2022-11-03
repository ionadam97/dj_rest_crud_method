from django.db import models


class Category(models.Model):
    """Categorie"""
    name = models.CharField("Categorie", max_length=150)
    description = models.TextField("Descriere")


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categorie"
        verbose_name_plural = "Categorii"


class Product(models.Model):
    """Produs"""
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(
        Category, verbose_name="Categorie", on_delete=models.SET_NULL, null=True
    )
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "produs"
        verbose_name_plural = "produse"
        ordering = ["-created"]