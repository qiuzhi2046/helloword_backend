from django.db import models


# 抽出基表
class BaseModel(models.Model):
    creat_time=models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    update_time=models.DateTimeField(auto_now=True,verbose_name='最后更新时间')
    is_delete=models.BooleanField(default=False,verbose_name='是否删除')
    is_show=models.BooleanField(default=True,verbose_name='是否展示')
    display_order=models.IntegerField()
    class Meta:
        abstract=True  #在元类（Meta）中的使用表示该模型是一个抽象基类。它将不会被Django用来创建数据库表。
        # 相反，当你在其他模型中继承这个抽象基类时，它的字段会被添加到子类模型中，并且子类模型会有自己的数据库表。