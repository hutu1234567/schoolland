#_*_ coding:utf-8 _*_
from django.db import models

class Subject:
    CHINESE = '001'
    ENGLISH = '002'
    MATH = '003'
    DRAWING = '301'
    MUSIC = '302'
    PHYSIQUE = '301'
    MEMORY = '601'
    LABOUR = '602'


subject_choice=(
    (Subject.CHINESE , u"语文"),
    (Subject.ENGLISH ,u"英语"),
    (Subject.MATH ,u"数学"),
    (Subject.DRAWING ,u"美术"),
    (Subject.MUSIC ,u"音乐"),
    (Subject.PHYSIQUE ,u"体育"),
    (Subject.MEMORY ,u"记忆"),
    (Subject.LABOUR ,u"劳动"),
)

book_choice=(
    ('unknown',u'未知'),
    ('pep3-1', u'人教版三年级上'),
    ('pep3-2', u'人教版三年级下'),
    ('pep4-1', u'人教版四年级上'),
    ('pep4-2', u'人教版四年级下'),
    ('pep5-1', u'人教版五年级上'),
    ('pep5-2', u'人教版五年级下'),
    ('pep6-1', u'人教版六年级上'),
    ('pep6-2', u'人教版六年级下'),
    ('pep7-1', u'人教版七年级上'),
    ('pep7-2', u'人教版七年级下'),
    ('pep8-1', u'人教版八年级上'),
    ('pep8-2', u'人教版八年级下'),
    ('pep9-1', u'人教版九年级上'),
    ('pep9-2', u'人教版九年级下'),



)