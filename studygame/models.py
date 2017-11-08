from django.db import models
from studygame.base import subject_choice,book_choice


class RandomManager(models.Manager):
    def get_queryset(self):
        return super(RandomManager, self).get_queryset().order_by('?')


class Vocabulary(models.Model):
    word = models.CharField("写法",max_length = 20 ,primary_key = True)
    paraphrase = models.TextField("意思",max_length = 100)
    pronunciation = models.CharField("发音",max_length = 20,null=True,blank=True)
    subject = models.CharField("科目",max_length = 4,choices = subject_choice,null=True)
    book = models.CharField("教材",max_length=20 , choices= book_choice,null=True,blank=True)

    can_know = models.BooleanField("能认识",default=False)
    can_use = models.BooleanField("会使用",default=False)
    can_write = models.BooleanField("会拼写",default=False)

    passed = models.BooleanField("已通关",default=False)

    objects = models.Manager() # The default manager.
    randoms = RandomManager()

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = '词汇小怪'
        verbose_name_plural = '词汇小怪'


class Item(models.Model):
    id = models.CharField( "编号", max_length=20, primary_key=True )
    name = models.CharField( "名称", max_length=20 )
    count = models.IntegerField( "数量", null=True )
    describe = models.CharField( "描述", max_length=100)

    class Meta:
        verbose_name = '道具'
        verbose_name_plural = '道具'

    def __str__(self):
        return self.name


class Task( models.Model ):
    id = models.CharField( "编号", max_length=50, primary_key=True )
    name = models.CharField( "名称", max_length=20 )
    subject = models.CharField( "科目", max_length=4 ,choices = subject_choice)
    describe = models.CharField( "描述",max_length=100)
    reward = models.IntegerField("赏金")
    status = models.CharField("状态" ,max_length=2,default='00')
    url = models.CharField("url",max_length=100 ,null=True,blank=True,default='')

    class Meta:
        verbose_name = '任务'
        verbose_name_plural = '任务'

    def __str__(self):
        return self.name


class TaskItem(models.Model):
    task = models.ForeignKey( Task , primary_key=True )
    item = models.ForeignKey( Item )
    need_count = models.IntegerField()


    class Meta:
        verbose_name = '任务道具'
        verbose_name_plural = '任务道具'

class AccomplishedTask( models.Model ):
    id = models.AutoField( "编号",  primary_key=True )
    task = models.ForeignKey( Task )
    completion_date = models.CharField("完成日期", max_length=8)
    actual_reward = models.IntegerField("赏金")
    desc = models.CharField("描述",max_length=100)


class Player( models.Model ):
    id = models.AutoField( "编号", primary_key=True )
    english_name = models.CharField( "英文名" ,max_length=50)
    chinese_name = models.CharField( "中文名" ,max_length=10)
    school_coin = models.IntegerField("斯古币")

    english_ability = models.IntegerField("英语力")
    chinese_ability = models.IntegerField("语文力")
    math_ability = models.IntegerField("数学力")
    drawing_ability = models.IntegerField("美术力")
    music_ability = models.IntegerField("音乐力")
    labour_ability = models.IntegerField("劳动力")
    physique_ability = models.IntegerField("身体力")
    memory = models.IntegerField("记忆力")


class TaskAbility( models.Model ):
    task = models.ForeignKey( Task )
    english = models.IntegerField("英语力",default=0)
    math = models.IntegerField("数学力",default=0)
    drawing = models.IntegerField("美术力",default=0)
    physique = models.IntegerField("身体力",default=0)
    chinese = models.IntegerField("语文力",default=0)
    labour = models.IntegerField("劳动力",default=0)
    music = models.IntegerField("音乐力",default=0)
    memory = models.IntegerField("记忆力",default=0)

    class Meta:
        verbose_name = '任务能力成长'
        verbose_name_plural = '任务能力成长'
    def __str__(self):
        return self.task

class PlayGrowUpDaily( models.Model ):
    task = models.ForeignKey( Task )
    english = models.IntegerField("英语力",default=0)
    math = models.IntegerField("数学力",default=0)
    drawing = models.IntegerField("美术力",default=0)
    physique = models.IntegerField("身体力",default=0)
    chinese = models.IntegerField("语文力",default=0)
    labour = models.IntegerField("劳动力",default=0)
    music = models.IntegerField("音乐力",default=0)
    memory = models.IntegerField("记忆力",default=0)
    school_coin = models.IntegerField( "斯古币" )
    cdate = models.DateTimeField("完成时间",auto_now_add=True)

class Sentence(models.Model):
    id = models.AutoField("编号",primary_key=True)
    word = models.ForeignKey( Vocabulary )
    sentence = models.CharField("句子",max_length=500)