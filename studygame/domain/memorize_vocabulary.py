#_*_ coding:utf-8 _*_
from studygame.models import Vocabulary,Item
from django.db.models import Q
from studygame.base import Subject

def getRandCantUseEnWord():
    record = Vocabulary.randoms.all().filter(can_use=0)[1]
    return record.word

def getRandCantSpellEnWord():
    record = Vocabulary.randoms.all().filter(can_write=0)[1]
    return record.paraphrase

def getRandUnknownEnglishwords(count, ignore=None):
    if(ignore is not None):
        records = Vocabulary.randoms.all().filter(~Q(word=ignore),subject=Subject.ENGLISH,can_know=0 )[0:count]
    else:
        records = Vocabulary.randoms.all().filter(can_know=False)[0:count]
    return records

def isFoundUnKnowedWord(word,choice,answer):
    isFound = 0
    ret = {"word": word, "paraphrase": answer}
    item = Item.objects.get( id='feather_english' )
    if(choice == answer):
        isFound = 1
        item.count += 1
        vocabulary =  Vocabulary.objects.get( word=word)
        vocabulary.can_know = 1
        vocabulary.save()
        item.save()
    else:
        unknown = Vocabulary.objects.get( paraphrase =choice)
        ret["word2"] = unknown.word
        ret["paraphrase2"] = unknown.paraphrase
        if(unknown.can_know!=0):
            unknown.can_know = 0
            unknown.save()

    ret["isFound"] = isFound
    ret["count"] = item.count

    return ret

def isDictateRight(word,paraphrase):
    vacabulary = Vocabulary.objects.get( paraphrase =paraphrase)
    isRight=False
    item = Item.objects.get( id='body_english' )
    if(vacabulary.word==word):
        isRight=True
        vacabulary.can_write=1
        vacabulary.save()
        item.count+=1
        item.save()
    ret={"isRight":isRight,"word":word,"paraphrase":paraphrase,"word2":vacabulary.word,"count":item.count}
    return ret

def hatch_en_word(request):
    if(Vocabulary.objects.filter(word=request.POST["word"]).count()==0):
        print("asdfasdf")
        vocabulary = Vocabulary.objects.create( word=request.POST["word"] )
        # vocabulary.word=request.POST["word"]
        vocabulary.pronunciation = request.POST["pronunciation"]
        vocabulary.paraphrase = request.POST["paraphrase"]
        vocabulary.book = request.POST["book"]
        vocabulary.save()
        item = Item.objects.get( id='shell_english' )
        item.count+=1
        item.save()
        flag = True
        reason = ""
        print(flag)
    else:
        flag = False
        reason = "已经孵化过【%s】小英兽了，请孵化不同的小英兽。"%request.POST["word"]
        print(reason)
    count = Item.objects.get( id='shell_english' ).count
    return {"flag":flag,"reason":reason,"count":count ,
            "word":request.POST["word"],"pronunciation":request.POST["pronunciation"],"paraphrase":request.POST["paraphrase"]}

