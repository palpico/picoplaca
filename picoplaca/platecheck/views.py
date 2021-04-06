from django.shortcuts import render
from django.utils.datetime_safe import datetime

from picoplaca.platecheck.models import PlateCheck
from django.views.generic import CreateView
from django.shortcuts import render, redirect


class PlateCheckCV(CreateView):
    model = PlateCheck
    fields = "__all__"

    def form_valid(self, form):
        obj = form.save(commit=False)
        self.request.session['g_plate'] = "{}-{}".format(obj.platecheck_plate[:3], obj.platecheck_plate[3:])
        self.request.session['g_date'] = obj.platecheck_date.strftime("%m/%d/%Y")
        self.request.session['g_time'] = obj.platecheck_time.strftime("%H:%M %p")
        self.request.session['g_result'] = picoplaca(obj.platecheck_plate, obj.platecheck_date, obj.platecheck_time)
        return redirect('platecheck:result')


def picoplaca(arg_plate, arg_date, arg_time):
    if arg_date.strftime("%w") in ["0", "6"]:
        return True
    elif time_range("7:00:00", "9:30:00", arg_time) is False and time_range("16:00:00", "19:30:00", arg_time) is False:
        return True
    elif check_date(arg_plate, arg_date):
        return False
    else:
        return True


def check_date(arg_plate, arg_date):
    # dict for weekdays and last digit plate
    day_plates = {"1": ["1", "2"], "2": ["3", "4"], "3": ["5", "6"], "4": ["7", "8"], "5": ["9", "0"]}
    if arg_plate[-1] in day_plates[arg_date.strftime("%w")]:
        return True
    else:
        return False


def time_range(begin_time, end_time, check_time):
    if datetime.strptime(begin_time, '%H:%M:%S').time() <= check_time <= datetime.strptime(end_time, '%H:%M:%S').time():
        return True
    else:
        return False
