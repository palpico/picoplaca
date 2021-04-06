from unittest import TestCase
import pytest
from django.test import RequestFactory
from django.utils.datetime_safe import datetime
from django.core.exceptions import ValidationError
from picoplaca.platecheck.models import PlateCheck, plate
from picoplaca.platecheck.views import PlateCheckCV, picoplaca, check_date, time_range


# date creator
def dt_cr(arg_str):
    return datetime.strptime(arg_str, "%m/%d/%Y").date()


# time creator
def tm_cr(arg_str):
    return datetime.strptime(arg_str, "%H:%M:%S").time()


@pytest.mark.parametrize("times", [["7:00:00", "9:30:00", tm_cr("10:30:00")],
                                   ["16:00:00", "19:30:00", tm_cr("20:30:00")]
                                   ])
def test_out_time_range(times):
    assert not time_range(*times)


@pytest.mark.parametrize("times", [["7:00:00", "9:30:00", tm_cr("8:30:00")],
                                   ["16:00:00", "19:30:00", tm_cr("18:30:00")]
                                   ])
def test_in_time_range(times):
    assert time_range(*times)


# argument 1 plate ending in 1 should be limited mondays
# argument 2 plate ending in 2 should be limited mondays
@pytest.mark.parametrize("plate_date", [["AAA1231", dt_cr("4/12/2021")],
                                        ["AAA1232", dt_cr("4/12/2021")]
                                        ])
def test_plate_not_check_date(plate_date):
    assert check_date(*plate_date)


# argument 1 plate ending in 5 does not have restrintion on tuesday 8:30 am
# argument 2 plate ending in 5 does not have restrintion on tuesday 17:30 am
# argument 3 plate ending in 3 has restriction on tuesday but time is not in restriction range 12:30 pm
# argument 4 no restriction on saturday
# argument 5 no restriction on sunday
@pytest.mark.parametrize("arguments", [["AAA1235", dt_cr("4/20/2021"), tm_cr("8:30:00")],
                                       ["AAA1235", dt_cr("4/20/2021"), tm_cr("17:30:00")],
                                       ["AAA1233", dt_cr("4/20/2021"), tm_cr("12:30:00")],
                                       ["AAA1233", dt_cr("4/17/2021"), tm_cr("12:30:00")],
                                       ["AAA1233", dt_cr("4/18/2021"), tm_cr("12:30:00")]
                                       ])
def test_picoplaca_can_drive(arguments):
    assert picoplaca(*arguments)


# argument 1 plate ending in 1 has restrintion on monday 8:30 am
# argument 2 plate ending in 1 has restrintion on monday 17:30 am
@pytest.mark.parametrize("arguments", [["AAA1231", dt_cr("4/19/2021"), tm_cr("8:30:00")],
                                       ["AAA121", dt_cr("4/19/2021"), tm_cr("17:30:00")],
                                       ["AAA1232", dt_cr("4/19/2021"), tm_cr("8:30:00")],
                                       ["AAA122", dt_cr("4/19/2021"), tm_cr("17:30:00")],
                                       ["AAA1233", dt_cr("4/20/2021"), tm_cr("8:30:00")],
                                       ["AAA123", dt_cr("4/20/2021"), tm_cr("17:30:00")]
                                       ])
def test_picoplaca_cant_drive(arguments):
    assert not picoplaca(*arguments)
