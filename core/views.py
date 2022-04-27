from django.shortcuts import render, redirect
from .models import Anime
from .forms import SuggestionForm
from django.contrib import messages
from .telegram import send_message, get_client_ip


def index_view(request):
    animes = Anime.objects.all().order_by("-date_created")
    blocked_animes = Anime.objects.filter(banned=True)
    context = {'animes':animes,'blocked_animes':blocked_animes}
    return render(request, "core/index.html", context)


def suggest(request):
    template_name = "core/suggest.html"
    if request.method == 'POST':
        form = SuggestionForm(request.POST)
        ip = get_client_ip(request)
        if form.is_valid():
            messages.success(request,"Спасибо за информацию!")
            send_message("**{}**\n Link: {} \n Info: {} \n IP: {}".format(
                form.cleaned_data["title"],
                form.cleaned_data["link"],
                form.cleaned_data["text"],
                ip))
            return redirect(request.path)
    else:
        form = SuggestionForm()
    return render(request, template_name, {'form':form})


def siteRedirect(request, sitelink):
    if sitelink.startswith("http://"):
        return redirect(sitelink)
    elif sitelink.startswith("https://"):
        return redirect(sitelink)
    else:
        URL = "https://"+sitelink
        return redirect(URL)