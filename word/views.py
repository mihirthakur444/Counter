from django.shortcuts import render, redirect
from .models import Text
from .forms import TextForm
# Create your views here.


def counter(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            total_count = form.cleaned_data['chars']
            total_words = total_count.split()
            total_count = len(total_count)
            # print(total_count)
            single_word = {}
            for word in total_words:
                if word in single_word:
                    single_word[word] += 1
                else:
                    single_word[word] = 1
    else:
        form = TextForm()
        total_count = 0
        total_words = 0
        single_word = {}

    context = {
                'total_count':total_count,
                'form':form,
                'total_words':len(total_words),
                'single_word':single_word.items(),
              }
    return render(request, 'word/counter.html', context)
