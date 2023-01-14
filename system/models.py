from django.db import models
from utils.models import CoreModel

class User(CoreModel):
    username = models.CharField(max_length=150, unique=True, db_index=True, verbose_name="用户名", help_text="用户名")
    email = models.EmailField(max_length=255, null=True, blank=True, verbose_name="邮箱", help_text="邮箱")
    mobile = models.CharField(max_length=255, null=True, blank=True, verbose_name="联系方式", help_text="联系方式")
    status = models.BooleanField(default=True, verbose_name="状态", help_text="状态")
    GENDER_CHOICES = (
        (0, "女"),
        (1, "男"),
    )
    gender = models.IntegerField(choices=GENDER_CHOICES, default=1, verbose_name="性别", help_text="性别")
    role = models.ManyToManyField(to="Role", db_constraint=False, help_text="关联角色", verbose_name="关联角色")

    class Meta:
        db_table = "system_users"
        verbose_name = "用户表"
        verbose_name_plural = verbose_name
        ordering = ("-create_datetime",)


class Role(CoreModel):
    name = models.CharField(max_length=64, verbose_name="角色名称", help_text="角色名称")
    code = models.CharField(max_length=64, unique=True, verbose_name="角色编码", help_text="角色编码")
    status = models.BooleanField(default=True, verbose_name="角色状态", help_text="角色状态")

    class Meta:
        db_table = "system_role"
        verbose_name = "角色表"
        verbose_name_plural = verbose_name
        ordering = ("-create_datetime",)