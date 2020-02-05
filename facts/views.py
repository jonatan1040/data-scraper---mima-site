from django.http import HttpResponse
from django.shortcuts import render


def facts(request):
    return HttpResponse("Hello, world. You're at the polls index.")
    # str = "my name is jonatan"
    # return render(request, "facts/facts.html", str)

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
