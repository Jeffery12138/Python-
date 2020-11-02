from django.db import models

# Create your models here.


class Topic(models.Model):
    """用户学习的主题"""
    # 属性text是一个CharField——由字符或文本组成的数据
    text = models.CharField(max_length=200)
    # date_added是一个DateTimeField——记录日期和时间的数据
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text


# Entry也继承了Django基类Model
class Entry(models.Model):
    """学到的有关某个主题的具体知识"""
    # 第一个属性topic是一个ForeignKey实例
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    # text是一个TextField实例
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    # 在Entry类中嵌套了Meta类，存储用于管理模型的额外信息
    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """返回模型的字符串表示"""

        return self.text[:50] + "..."
