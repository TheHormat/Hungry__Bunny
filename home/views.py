from django.shortcuts import get_object_or_404, redirect, render
from article.forms import ArticleForm
from article.models import Article, Like
from home.models import BurgerMenu, DrinkMenu, SetMenu
from django.contrib.auth.decorators import login_required


@login_required(login_url='user:login/')
def dashboard_view(request):
    articles = Article.objects.filter(author=request.user)

    context = {
        'articles': articles,
    }
    return render(request, 'dashboard.html', context)


@login_required(login_url='user:login/')
def single_view(request):
    if keyword := request.GET.get("keyword"):
        articles = Article.objects.filter(title__contains=keyword)
        return render(request, "single.html", {"articles": articles})
    articles = Article.objects.all()

    return render(request, "single.html", {"articles": articles})


@login_required(login_url='user:login')
def addarticle_view(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        return redirect('article:dashboard')

    return render(request, 'addarticle.html', {'form': form})


@login_required(login_url='user:login')
def home_view(request):
    burger_menu = BurgerMenu.objects.all()
    drink_menu = DrinkMenu.objects.all()
    set_menu = SetMenu.objects.all()

    context = {
        'burger_menu': burger_menu,
        'drink_menu': drink_menu,
        'set_menu': set_menu,
    }
    return render(request, 'index.html', context)


@login_required(login_url='user:login')
def paypal_view(request):
    return render(request, 'paypal.html', {})


@login_required(login_url='user:login')
def about_view(request):
    return render(request, 'about.html', {})


@login_required(login_url='user:login')
def menu_view(request):
    burger_menu = BurgerMenu.objects.all()
    drink_menu = DrinkMenu.objects.all()
    set_menu = SetMenu.objects.all()

    context = {
        'burger_menu': burger_menu,
        'drink_menu': drink_menu,
        'set_menu': set_menu,
    }
    return render(request, 'menu.html', context)


@login_required(login_url='user:login')
def include_menu(request):
    burger_menu = BurgerMenu.objects.all()
    drink_menu = DrinkMenu.objects.all()
    set_menu = SetMenu.objects.all()

    context = {
        'burger_menu': burger_menu,
        'drink_menu': drink_menu,
        'set_menu': set_menu,
    }
    # context = {}
    # if BurgerMenu.objects.all().exists() and DrinkMenu.objects.all().exists() and SetMenu.objects.all().exists():
    #     context = {"burgermenu": BurgerMenu.objects.all().last(),
    #                "drinkmenu": DrinkMenu.objects.all().last(),
    #                "setmenu": SetMenu.objects.all().last()
    #                }
    return render(request, 'include_menut.html', context)


@login_required(login_url='user:login')
def booking_view(request):
    burger_menu = BurgerMenu.objects.all()
    drink_menu = DrinkMenu.objects.all()
    set_menu = SetMenu.objects.all()

    context = {
        'burger_menu': burger_menu,
        'drink_menu': drink_menu,
        'set_menu': set_menu,
    }
    return render(request, 'booking.html', context)


@login_required(login_url='user:login')
def contact_view(request):
    return render(request, 'contact.html', {})


def delete_view(request, id):
    article = get_object_or_404(Article, id=id)
    article.delete()
    return redirect('article:dashboard')


@login_required(login_url='user:login')
def faq_view(request):
    return render(request, 'FAQ.html', {})


@login_required(login_url='user:login')
def terms_view(request):
    return render(request, 'terms.html', {})


@login_required(login_url='user:login')
def update_view(request, id):
    article = get_object_or_404(Article, id=id)
    form = ArticleForm(request.POST or None,
                       request.FILES or None, instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        return redirect("article:dashboard")
    return render(request, "update.html", {"form": form})


@login_required(login_url='user:login')
def post_view(request):
    qs = Article.objects.all()
    user = request.user
    context = {
        'qs': qs,
        'user': user,
    }

    return render(request, 'single.html', context)


@login_required(login_url='user:login')
def like_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Article.objects.get(id=post_id)

        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)

        like, created = Like.objects.get_or_create(user=user, post_id=post_id)

        if not created:
            like.value = 'UnLike' if like.value == 'Like' else 'Like'
        like.save()

    return redirect('article:single')
