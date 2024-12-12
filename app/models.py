from django.db import models


# Create your models here.
class ProjetoDeLei(models.Model):
    ANO_CHOICES = (
        (2021, "2021"),
        (2022, "2022"),
        (2023, "2023"),
        (2024, "2024"),
    )

    STATUS_CHOICES = (
        ("Aprovado", "aproved"),
        ("Em Análise", "pending"),
        ("Negado", "denied"),
    )

    numero = models.CharField(max_length=7, verbose_name="Número")
    descricao = models.CharField(max_length=255, verbose_name="Descrição")
    documento = models.URLField(verbose_name="Link do Documento")
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, verbose_name="Status"
    )
    ano = models.IntegerField(choices=ANO_CHOICES, verbose_name="Ano")

    class Meta:
        verbose_name = "Projeto de lei"
        verbose_name_plural = "Projetos de Lei"

    def __str__(self):
        return f"PL {self.numero} - {self.descricao}"


class ExPresidente(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Nome")
    periodo = models.CharField(max_length=255, verbose_name="Período")
    foto = models.URLField(verbose_name="Foto")

    class Meta:
        verbose_name = "Ex-Presidente"
        verbose_name_plural = "Ex-Presidentes"

    def __str__(self):
        return self.nome