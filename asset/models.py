from django.db import models

class Asset(models.Model):
    id = models.BigAutoField(primary_key=True, help_text="编号", verbose_name="编号", )
    create_time = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name="创建时间", help_text="创建时间")
    update_time = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="更新时间", help_text="更新时间")
    name = models.CharField(max_length=125, verbose_name="资产名称", help_text="资产名称")
    kind = models.CharField(max_length=125, verbose_name="资产种类", help_text="资产种类")
    location = models.CharField(max_length=125, verbose_name="资产所在地", help_text="资产所在地")
    owner = models.CharField(max_length=125, verbose_name="资产所属人", help_text="资产所属人")
    scrap_time = models.DateTimeField(null=True, blank=True, verbose_name="报废时间", help_text="报废时间")

    class Mate:
        db_table = 'asset'
        verbose_name = '资产表'
        verbose_name_plural = verbose_name
        ordering = ('-create_time')
