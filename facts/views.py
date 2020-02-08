from django.db.models import F
from django.shortcuts import render, get_object_or_404
from facts.models import Artist, Song, Facts


def get_artist(request, artist_number):
    relevant_artist = get_object_or_404(Artist, pk=artist_number)
    artist_songs = relevant_artist.songs.all
    return render(request, 'facts/artist.html', {'artist_songs': artist_songs, 'relevant_artist': relevant_artist})


def get_song(request, song_number):
    relevant_song = get_object_or_404(Song, pk=song_number)
    relevant_songs = Song.objects.filter(song__startswith=relevant_song.song[0])
    return render(request, 'facts/song.html', {'relevant_songs': relevant_songs, 'relevant_song': relevant_song})


def get_facts(request, facts_number):
    print(facts_number)
    relevant_fact = Facts.objects.filter(song_id=facts_number)
    print(type(relevant_fact))
    return render(request, 'facts/fact.html', {'relevant_fact': relevant_fact})



    # str = "my name is jonatan"
    # return render(request, "facts/song.html", str)

    # import calendar
    #
    # from django.contrib import messages
    # from django.shortcuts import render, get_object_or_404, redirect
    #
    # from expenses import forms
    # from expenses.models import Expense
    #
    # def expense_list(request):
    #     o = calendar.HTMLCalendar()
    #     qs = Expense.objects.order_by('-date')[:12]
    #     # FIXME: use sql group by sum???
    #     total = sum([x.amount for x in qs])
    #     return render(request, "expenses/expense_list.html", {
    #         'object_list': qs,
    #         'total': total,
    #         'month': o.formatmonth(1969, 7),
    #     })
    #
    # def expense_detail(request, id):
    #     o = get_object_or_404(Expense, id=id)
    #
    #     return render(request, "expenses/expense_detail.html", {
    #         'object': o,
    #     })
    #
    # def expense_create(request):
    #     if request.method == "POST":
    #         form = forms.ExpenseForm(request.POST)
    #         if form.is_valid():
    #             # data = form.cleaned_data
    #             o = form.save()
    #             messages.success(request, f"Expense #{o.id} added. Thank you so very much!!!!!")
    #             # return redirect(o)  # TODO: implement get_absolute_url
    #             return redirect("expenses:list")
    #
    #     else:
    #         form = forms.ExpenseForm()
    #     return render(request, "expenses/expense_form.html", {
    #         'form': form,
    #     })
