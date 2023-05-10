from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from modules import  models
from .models import  giver_reg, taker_reg, login_table, make_trips, requested_trip
import django.contrib.auth
from django.contrib.auth.models import auth, User
from django.contrib import messages
from datetime import date
# Create your views here.
def index(request):
    return render(request, 'Homepage/homepage.html')

def logout(request):
    auth.logout(request)
    return redirect(index)


def giver_register(request):
    if request.method == 'POST':

        giver = models.giver_reg()
        login = models.login_table()
        uploaded_file = request.FILES.get('profile_pic')
        print(' uploaded_file')
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        img_name = uploaded_file.name
        giver.profile_pic = img_name

        giver.giver_name = request.POST['giver_name']
        giver.address = request.POST['address']
        giver.aaddhar = request.POST['aaddhar']
        giver.mob_no = request.POST['mob_no']
        giver.native = request.POST['native']
        giver.nationality = request.POST['nationality']
        giver.veh_type = request.POST['veh_type']
        giver.password = request.POST['password']

        login.username = request.POST['giver_name']
        login.type = 'Giver'
        login.status = '1'
        login.password = request.POST['password']
        giver.save()
        login.save()
    return render(request, 'Giver_templates/Giver_register/register_form.html')

def taker_register(request):
    if request.method == 'POST':
        giver = models.taker_reg()
        login = models.login_table()
        uploaded_file = request.FILES.get('profile_pic')
        print(' uploaded_file')
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        img_name = uploaded_file.name
        giver.profile_pic = img_name

        giver.taker_name = request.POST['taker_name']
        giver.address = request.POST['address']
        giver.aaddhar = request.POST['aaddhar']
        giver.mob_no = request.POST['mob_no']
        giver.native = request.POST['native']
        giver.nationality = request.POST['nationality']
        giver.password = request.POST['password']

        login.username = request.POST['taker_name']
        login.type = 'Taker'
        login.status = '1'
        login.password = request.POST['password']
        giver.save()
        login.save()

    return render(request, 'Taker_templates/Taker_register/register_form.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST['password']
        user = login_table.objects.filter(username=username, password =password, status=1).exists()
        print(user)

        if user is not False:
            user_deatil = login_table.objects.get(username=username, password = password, status=1)
            username_user = user_deatil.username
            type1 = user_deatil.type
            print(username_user)
            print(type1)
            if type1 == 'Giver':
                request.session['username'] = username
                return redirect(giver_home)
            elif type1 == 'Taker':
                request.session['username'] = username
                return redirect(taker_home)

    return render(request, 'login/login.html')

def giver_home(request):
    msg = ''
    username_user = request.session['username']
    det = giver_reg.objects.get(giver_name = username_user)
    print(det)
    des = requested_trip.objects.filter(giver_name=username_user, trip_status='Requested').count()
    print('Count Value')

    make = make_trips.objects.filter(giver_name=username_user)
    print(make)
    if make:
        msg = 'Trips Found'
    else:
        msg = 'Trips Not Found'
    context = {'username_user': username_user, 'det':det,'des':des, 'make':make,'msg': msg}
    return render(request , 'giver_templates/Giver_home/giver_home.html', context)

def taker_home(request):
    username_user = request.session['username']
    des = requested_trip.objects.filter(taker_name=username_user, trip_status='Accepted',payment_status = '').count()
    print('Count Value')
    context = {'username_user': username_user,'des':des}
    return render(request , 'taker_templates/Taker_home/taker_home.html', context)

def make_trip(request):
    num = ''
    no = make_trips.objects.all().count()
    nu = str(no)
    if nu == ' ':
        num = '0'
    else:
        num = nu
    print('Number of Data is:', num)

    trip_id = 'EF2023' + num
    print('Trip Id is:', trip_id)

    if request.method == 'POST':
        make = models.make_trips()
        make.giver_name = request.POST['giver_name']
        make.start = request.POST['start']
        make.destination = request.POST['destination']
        make.time = request.POST['time']
        make.date = request.POST['date']
        make.price = request.POST['price']
        make.veh_model = request.POST['veh_model']
        make.price = request.POST['price']
        make.seat = request.POST['seat']
        make.bal_seat = request.POST['seat']
        make.status = 'Ongoing'
        make.trip_id = trip_id
        make.save()
    return redirect(giver_home)

def trip_details(request):

    username_user = request.session['username']
    det = make_trips.objects.filter(giver_name = username_user)
    detail = giver_reg.objects.get(giver_name = username_user)
    print(detail)
    print(det)
    context = {'det': det, 'detail':detail}

    return render(request, 'Giver_templates/Trip_details/trip_details.html', context)


def available_trip(request):
    username_user = request.session['username']
    req =''
    reqs = ''
    msg = ''
    msgs = ''
    dess=''
    abc = []
    abcd = []
    reqests = ''
    abcs = []
    abcds = []
    datesss = ''
    new = []
    news = []
    if request.method == 'POST':
        start = request.POST['start']
        dest = request.POST['destination']
        tri = request.POST['trip_date']
        print(start)
        print(dest)
        print(tri)
        dess = make_trips.objects.filter(start=start, destination = dest, date = tri)
        if dess:
            msg = 'Record Found'
            print(msg)
        else:
            msg = 'No Record Found'
            print(msg)

        for tab in dess:
            name = tab.giver_name
            det = giver_reg.objects.get(giver_name=name)
            abc.append(det)

            abcd =[*set(abc)]
            print('Latest')
            print(abcd)

    reqs = requested_trip.objects.all()
    if reqs:
        rt= reqs
    else:
        rt = 'no records'

    for det in reqs:
        print(det.giver_name)
        print(username_user)
        datesss = det.date
        reqests = requested_trip.objects.filter(taker_name = username_user, giver_name = det.giver_name,date = det.date)
        print(reqests)
        if reqests is None:
            rts = 'No records'
            break
        else:
            rts = reqests
    requested = requested_trip.objects.filter(taker_name= username_user, payment_status = 'Successfull',date = datesss)
    print('Requested Rows')
    print(requested)


    context = {'dess':dess, 'msg': msg, 'abcd':abcd, 'username_user':username_user, 'req':req, 'msgs': msgs, 'reqests':reqests,'abcs':abcs, 'requested':requested , 'news':news}
    return render(request, 'Taker_templates/Available_trips/ava_trip.html', context)


def request_trip(request, taker_name, giver_name, date, veh_model,start, dest, trip_id):
    msg = ''
    req = models.requested_trip()
    req.taker_name = taker_name
    req.giver_name = giver_name
    req.date = date
    req.veh_model = veh_model
    req.trip_status = 'Requested'
    req.start = start
    req.destination = dest
    req.trip_id = trip_id
    req.save()
    return redirect(available_trip)


def acceptance(request):
    dess = ''
    abc = []
    abcd = []
    dates = ''
    des = ''
    act = ''
    msg=''
    des = ''
    username_user = request.session['username']
    if request.method == 'POST':
        dates = request.POST['date']
        #print(dates)
        act = request.POST['action']
        print(act)
        print('Action', act)
        print('Date is',dates)
        dess  = requested_trip.objects.filter(giver_name = username_user, date = dates, trip_status = act)
        print(dess)
        if dess:
            msg = 'Record Found'
            print(msg)
        else:
            msg = 'No Record Found'
            print(msg)

        for tab in dess:
            name = tab.taker_name
            det = taker_reg.objects.get(taker_name=name)
            abc.append(det)

            abcd =[*set(abc)]
            print('Latest')
            print(abcd)

        des = make_trips.objects.filter(giver_name = username_user)
    context = {'dess': dess, 'abcd':abcd, 'des':des, 'username_user':username_user, 'act':act, 'msg':msg}
    return render(request, 'Giver_templates/Acceptance/accept.html',context)


def request_trips(request):
    msg = ''
    abc = []
    dates = ''
    act = ''
    details = ''
    detailss = ''
    username_user = request.session['username']
    if request.method == 'POST':
        dates = request.POST['date']
        act = request.POST['action']
        print('Action', act)
        details = requested_trip.objects.filter(taker_name = username_user, date = dates , trip_status = act)
        print(details)
        if details:
            msg = 'Record found'
            print(msg)
        else:
            msg = 'Record Not Found'
            print(msg)
        for tab in details:
            name = tab.giver_name
            det = giver_reg.objects.get(giver_name = name)
            abc.append(det)
            print(abc)
        detailss = requested_trip.objects.filter(taker_name=username_user, date=dates, trip_status=act, payment_status = 'Successfull')
    context = {'details':details,'detailss':detailss, 'msg':msg, 'abc':abc, 'act':act}
    return render(request, 'Taker_templates/Request_trip/request_trip.html', context)

def accept_trip(request, trip_id, id):
    seat = ''
    msg = ''
    print(trip_id)
    make = make_trips.objects.get(trip_id = trip_id)
    print(make)
    seat = make.bal_seat
    seats = int(seat)
    print('Total Seat', seats)
    print(seats)
    if seats <=0:
        msg = 'Seat not Available'
        print('Seat not Available')
        messages.success(request, 'Seat not Available')
    else:
        ava_seat = seats - 1
        print('Available Seat:', ava_seat)
        available_seat = str(ava_seat)
        make.bal_seat = available_seat
        req = requested_trip.objects.get(id = id)
        req.trip_status = 'Accepted'
        make.save()
        req.save()
        messages.success(request, 'Accepted Successfully ')

    context = {'msg': msg}
    return redirect(acceptance)

def redirects(request, trip_id):
    context = {'trip_id':trip_id}
    return render(request,'Taker_templates/Redirecting/redirecting.html', context )

def payment_card(request, id):
    msg = ''
    msgs = ''
    det = requested_trip.objects.get(id = id)
    print(det)
    trip_id = det.date
    tak = det.giver_name
    make = make_trips.objects.get( date = trip_id, giver_name = tak)
    print(trip_id)

    price = int(make.price)
    gst_amnt = 6/100*price
    print('GST Amount', gst_amnt)

    total_amount = price + gst_amnt
    print('Total Amount:', total_amount)



    giver = det.giver_name
    print(giver)
    giver_det = giver_reg.objects.get(giver_name = giver)
    print(giver_det)

    taker = det.taker_name
    print(taker)

    taker_det = taker_reg.objects.get(taker_name=taker)
    print(taker_det)


    if giver_det and taker_det :
        msg = 'Record Found!'
    else:
        msg = 'Record Not found'

    context = {'id':id,'giver_det':giver_det, 'taker_det': taker_det, 'det':det, 'make': make, 'total_amount':total_amount}
    return render(request,'Taker_templates/Payment_card/payment_card.html', context)



def payment_processing(request,id):
    print(id)
    trans = '102346576' + id
    print(trans)
    context = {'trans':trans, 'id':id}
    return render(request ,'Taker_templates/Payment_processing/payment_processing.html', context)

def payment_completion(request, id, trans_id):
    print(trans_id)
    print(id)
    req = requested_trip.objects.get(id = id)
    req.payment_id = trans_id
    today = date.today()
    req.payment_status = 'Successfull'
    req.pay_date = today
    req.save()

    context = {'trans_id':trans_id, 'id':id}
    return render(request, 'Taker_templates/Payment_completion/payment_completion.html',context)


def receipt(request, id, trans_id):
    username_user = request.session['username']
    req_det = requested_trip.objects.get(id = id, payment_id = trans_id, taker_name = username_user, payment_status = 'Successfull')
    print(req_det)
    tak = req_det.giver_name
    dates = req_det.date
    print('Giver Name:',tak)
    make = make_trips.objects.get(giver_name=tak, date = dates)
    print(make)
    today = date.today()
    taker_details = taker_reg.objects.get(taker_name = username_user)
    giver_details = giver_reg.objects.get(giver_name = tak)

    price = int(make.price)
    gst_amnt = 6 / 100 * price
    print('GST Amount', gst_amnt)

    total_amount = price + gst_amnt
    print('Total Amount:', total_amount)

    context = {'req_det':req_det, 'make':make, 'today':today, 'taker_details':taker_details,'giver_details':giver_details, 'total_amount':total_amount }
    return render(request, 'Taker_templates/Receipt/receipt.html', context)

def receipt_view(request):
    msg = ''
    username_user = request.session['username']
    req_det = requested_trip.objects.filter(taker_name = username_user, payment_status = 'Successfull')
    if req_det:
        msg = 'Receipt Found!'
    else:
        msg = 'No Receipt Found'
    context = {'req_det':req_det, 'msg':msg}
    return render(request, 'Taker_templates/Receipt_View/receipt_view.html', context)

def receipt_info(request, pay_id, trip_id):
    username_user = request.session['username']
    print(username_user)
    print(pay_id)
    req_det = requested_trip.objects.get(taker_name=username_user, payment_status='Successfull', payment_id = pay_id)
    giver = req_det.giver_name
    giver_details = giver_reg.objects.get(giver_name = giver)
    print(giver_details)
    taker_details = taker_reg.objects.get(taker_name = username_user)

    trip_id = req_det.trip_id
    print(trip_id)
    dates = req_det.date

    make = make_trips.objects.get(giver_name=giver, date = dates, trip_id = trip_id  )
    print(make)

    price = int(make.price)
    gst_amnt = 6 / 100 * price
    print('GST Amount', gst_amnt)

    total_amount = price + gst_amnt
    print('Total Amount:', total_amount)

    context = {'username_user':username_user, 'req_det':req_det, 'giver_details':giver_details, 'taker_details':taker_details, 'make':make, 'total_amount':total_amount}
    return render(request, 'Taker_templates/Receipt_View/receipt_info.html', context)

def giver_receipt_view(request, trip_id):
    username_user = request.session['username']

    taker_details= []
    msg = ''

    receipt_inf = requested_trip.objects.filter(giver_name = username_user, payment_status = 'Successfull', trip_id = trip_id)
    print(receipt_inf)
    if receipt_inf :
        msg = 'Receipt Found'
    else:
        msg = 'Receipt Not Found!'

    makes = make_trips.objects.get(trip_id = trip_id)

    giver_details = giver_reg.objects.get(giver_name = username_user)
    for i in receipt_inf:
        print(i.taker_name)
        taker_det = taker_reg.objects.get(taker_name = i.taker_name)
        print(taker_det)
        taker_details.append(taker_det)
        print(taker_details)

    price = int(makes.price)
    gst_amnt = 6 / 100 * price
    print('GST Amount', gst_amnt)

    total_amount = price + gst_amnt
    print('Total Amount:', total_amount)

    context = {'receipt_inf':receipt_inf, 'makes':makes, 'giver_details':giver_details,'taker_details':taker_details, 'total_amount':total_amount, 'msg':msg}
    return render(request, 'Giver_Templates/Reciept/reciept.html', context)


def test(request):
    abc = []
    dess = make_trips.objects.filter(start='Kollam', destination='Pathanamthitta', date='2023-04-28')
    for tab in dess:
        name = tab.giver_name
        det = giver_reg.objects.get(giver_name = name)
        abc.append(det)
        print(abc)
    context = {'dess': dess, 'abc':abc}
    return render(request, 'test/test.html', context)