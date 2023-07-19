from django.shortcuts import render, redirect
from app.models import Doktor, Xona, Bemor, Xamshira
from app.tgbot import send_messege


def get_doktor(requests):
    dok = Doktor.objects.all().order_by('status')
    ctx = {
        "root": dok
    }
    return render(requests, 'get_lists/doktor_list.html', context=ctx)


def get_xona(requests):
    xona = Xona.objects.all().order_by('odam_soni')
    ctx = {
        "root": xona
    }
    return render(requests, 'get_lists/doktor_list.html', context=ctx)


def get_bemor(requests, pk=None):
    ctx = {
        'all': Bemor.objects.all().order_by('status'),
        "xona": Xona.objects.all(),
        "doktor": Doktor.objects.all(),
        "xamshira": Xamshira.objects.all()
    }

    if requests.POST:
        data = requests.POST
        try:
            doktor = Doktor.objects.filter(id=int(data['doktor'])).first()
            xona = Xona.objects.filter(id=int(data['xona'])).first()
            hamshira = Xamshira.objects.filter(id=int(data['xamshira'])).first()

            if xona.odam_soni > 2 or doktor.status or hamshira.status:
                ctx['error'] = f'Bular bant'
                return render(requests, 'get_lists/bemor_list.html', ctx)

            a = Bemor.objects.create(
                ism=data['ism'],
                familiya=data['familiya'],
                phone=data['phone'],
                xona=xona,
                doktor=doktor,
                xamshira=hamshira,
            )
        except ValueError:
            ctx['error'] = f'Data toliq emas'
            return render(requests, 'get_lists/bemor_list.html', ctx)
        send_messege(doktor.telegramnikname, hamshira.telegramnikname, xona, a.ism)

        doktor.status = True
        doktor.save()

        xona.odam_soni += 1
        xona.save()

        hamshira.status = True
        hamshira.save()

        return render(requests, 'get_lists/bemor_list.html', ctx)
    if pk:
        bemor_pk = Bemor.objects.filter(id=pk).first()
        doktor_pk = Doktor.objects.filter(id=bemor_pk.doktor.id).first()
        xona_pk = Xona.objects.filter(id=bemor_pk.xona.id).first()
        hamshira_pk = Xamshira.objects.filter(id=bemor_pk.xamshira.id).first()

        doktor_pk.status = False
        doktor_pk.save()

        hamshira_pk.status = False
        hamshira_pk.save()

        xona_pk.odam_soni -= 1
        xona_pk.save()

        bemor_pk.status = False
        bemor_pk.save()

        return redirect('get_klient')
    return render(requests, 'get_lists/bemor_list.html', ctx)


def get_xamshira(requests):
    xamshira = Xamshira.objects.all().order_by('status')
    ctx = {
        "root": xamshira
    }
    return render(requests, 'get_lists/xamshira_list.html', context=ctx)


def index(request):
    ctx = {
        "doktor": len(Doktor.objects.all()),
        "xona": len(Xona.objects.all()),
        "bemor": len(Bemor.objects.all()),
        "xamshira": len(Xamshira.objects.all())
    }

    return render(request, 'index.html', ctx)
