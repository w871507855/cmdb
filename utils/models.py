from django.db import models

class CoreModel(models.Model):
    id = models.BigAutoField(primary_key=True, help_text="ID", verbose_name="ID")
    create_datetime = models.DateTimeField(auto_now=True, null=True, blank=True, help_text="创建时间", verbose_name="创建时间")
    update_datetime = models.DateTimeField(auto_now_add=True, null=True, blank=True, help_text="更新时间", verbose_name="更新时间")

    class Meta:
        abstract = True
        verbose_name = "核心模型"
        verbose_name_plural = verbose_name
