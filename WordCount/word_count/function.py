# from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'HtmlDemo.html')


def count(request):
    user_text = request.GET['text']
    total = len(request.GET['text'])
    word_dict = {}

    for each in user_text:
        if each not in word_dict:
            word_dict[each] = 1
        else:
            word_dict[each] += 1
    # 将字典中的值按照从大到小的顺序排列
    sorted_dict = sorted(word_dict.items(),key=lambda w:w[1],reverse=True)
    return render(request, 'count.html', {'count': total, 'text': user_text, 'dict': sorted_dict})