#_*_ coding:utf-8 _*_
from studygame.models import Task,AccomplishedTask,TaskAbility,Player,TaskItem,Item,PlayGrowUpDaily
from datetime import datetime
from django.db import transaction

@transaction.atomic
def complete_task(task_id, report=None):
    task = Task.objects.get(id=task_id)
    task_item = TaskItem.objects.filter(task=task)
    if(task_item.count()>0):
        task_item = TaskItem.objects.get( task=task )
        item = Item.objects.get(id=task_item.item_id)
        if(item.count>=task_item.need_count):
            item.count-=task_item.need_count
            item.save()
        else:
            flag=False
            reason = '少帅，你的%s还不够呢，请攒够之后再来领取奖励吧'%item.name
            return {"flag":flag,"reason":reason}
    today = datetime.now().strftime( "%Y%m%d" )
    at = AccomplishedTask.objects.create(task_id=task_id,actual_reward = task.reward,completion_date=today,desc = report)
    at.save()
    growup = TaskAbility.objects.get(task_id=task_id)

    player = Player.objects.get(english_name="Ever Summer")
    player.school_coin += task.reward
    player.english_ability+=growup.english
    player.chinese_ability +=growup.chinese
    player.math_ability +=growup.math
    player.drawing_ability +=growup.drawing
    player.music_ability +=growup.music
    player.labour_ability +=growup.labour
    player.physique_ability +=growup.physique
    player.memory +=growup.memory
    player.save()

    daily = PlayGrowUpDaily.objects.create(task=task,school_coin=task.reward)
    #daily.school_coin=task.reward
    daily.english = growup.english
    daily.chinese = growup.chinese
    daily.math = growup.math
    daily.drawing = growup.drawing
    daily.musica = growup.music
    daily.labour= growup.labour
    daily.physique= growup.physique
    daily.memory = growup.memorya
    daily.save()

    return {"flag":True,"name":task.name,"reward":at.actual_reward,"subject":task.get_subject_display()}