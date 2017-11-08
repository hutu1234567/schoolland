from django.shortcuts import render
from studygame.models import *
import random
import studygame.domain.memorize_vocabulary as memorize_vocabulary
import studygame.domain.task as task
from datetime import datetime
from studygame.base import book_choice


def recognize_en_word(request):
    question = memorize_vocabulary.getRandUnknownEnglishwords( 1 ).values()[0]
    confused_item = memorize_vocabulary.getRandUnknownEnglishwords( 10, question["word"] )
    list = confused_item.values_list( "word", "paraphrase" )
    word_list = []
    paraphrase_list = []
    for each in list:
        word_list.append( each[0] )
        paraphrase_list.append( each[1] )

    answer_index = random.randint( 0, 9 )
    paraphrase_list[answer_index] = question["paraphrase"]
    data = {"question": question["word"], "answer": question["paraphrase"], "paraphrase_list": paraphrase_list,
            "word_list": word_list}
    return render( request, "studygame/recognizeEnWord.html", context=data )


def recognize_en_word_result(request):
    ret = memorize_vocabulary.isFoundUnKnowedWord( request.POST["word"], request.POST["choice"],
                                                   request.POST["answer"] )
    return render( request, "studygame/recognizeEnWordResult.html", context=ret )


def task_center(request):
    try:
        subject = request.GET["subject"]
    except KeyError as err:
        subject = "all"
    condition = "1=1"
    if(subject!="all"):
        condition = "subject ='%s'"%subject
    today = datetime.now().strftime( "%Y%m%d" )
    sql = "select task.*,count(at.task_id) as qty from studygame_task task " \
          "left JOIN studygame_accomplishedtask at on task.id=at.task_id and at.completion_date='%s' where %s " \
          "group by task.id"%(today,condition)

    list = Task.objects.raw( sql )
    ret = {'tasks': list}
    return render( request, "studygame/taskCenter.html", context=ret )

def do_task(request):
    content={"task_id":request.GET["taskid"]}
    return render(request,"studygame/doTask.html",context=content)


def complete_task(request):
    ret = task.complete_task(task_id=request.POST["task_id"],report=request.POST["report"])
    return render(request,"studygame/completeTask.html",context={"ret":ret})


def player(request):
    player = Player.objects.get( english_name="Ever Summer" )
    return render( request, "studygame/player.html", context={'player': player} )

def hatch_en_word(request):
    return render(request, "studygame/hatchEnWord.html",{"books":book_choice} )

def save_en_word(request):
    ret = memorize_vocabulary.hatch_en_word(request)
    return render(request, "studygame/hatchEnWordResult.html",{"ret":ret})

def shop(request):
    return render(request, "studygame/shop.html")

def dictate_en_word(request):
    paraphrase = memorize_vocabulary.getRandCantSpellEnWord()
    return render(request, "studygame/dictateEnWord.html",{"paraphrase":paraphrase})

def dictate_en_word_result(request):
    date = memorize_vocabulary.isDictateRight(request.POST["word"],request.POST["paraphrase"])
    return render( request, "studygame/dictateEnWordResult.html",context=date )

def make_en_sentence(request):
    word = memorize_vocabulary.getRandCantUseEnWord()
    return render( request, "studygame/makeEnSentence.html",{'word':word})

def make_en_sentence_result(request):
    vocabulary = Vocabulary.objects.get(word=request.POST["word"])
    sentence = Sentence.objects.create(sentence=request.POST["sentence"],word=vocabulary)
    sentence.save()
    ret = task.complete_task(task_id="make_en_sentence",report= "用【%s】造了一个句子"%request.POST["word"])
    print(ret)
    return render(request,"studygame/completeTask.html",context={"ret":ret})

def challenge_thirty_en_word():