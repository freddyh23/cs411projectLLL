from django.shortcuts import render
from .models import Person
from django.db import connections, connection
import random
import djongo.cursor


# Create your views here.
def home(request):
    return render(request, 'home.html')

def updatePage(request):
    return render(request, 'base.html')

def createProfilePage(request):
    return render(request, 'create_profile.html')

def viewProfile(request):
    return render(request, 'profile.html')




# updates profile with new height

def updateProfile(request):
    firstName = request.GET.get('firstname')
    lastName = request.GET.get('lastname')
    password = request.GET.get('password')
    age = request.GET.get('age')
    height = request.GET.get('height')
    gender = request.GET.get('gender')
    ethnicity = request.GET.get('ethnicity')
    university = request.GET.get('university')
    jobIndustry = request.GET.get('jobIndustry')
    # with connections['default'].cursor() as cursor:
    #     cursor.execute('UPDATE calc_person  SET height = %s WHERE firstname = %s ', [height, firstName])

    # with connections['users_db'].cursor() as cursor:
    #     djongo.cursor.Cursor(cursor, "users_db", ).execute('db.users.insert({"name": "Freddy Hernandez"})')
        # cursor.execute('db.users.insert({"name": "Freddy Hernandez"})')
    # with
    print("here")

    # with connection.cursor() as cursor:
    #     cursor.execute('UPDATE calc_person  SET age = %s WHERE firstname = %s ', [age, firstName])

    # with connection.cursor() as cursor:
    #     cursor.execute('UPDATE calc_person  SET schoolname = %s WHERE firstname = %s ', [school, firstName])

    # with connections['default'].cursor() as cursor:
    #     cursor.execute('UPDATE calc_person  SET  = %s WHERE firstname = %s ', [height, firstName])
    return render(request, 'base.html')


#deletes persom based on name

def deletePerson(request):
    firstName = request.GET['firstname']
    with connection.cursor() as cursor:
        cursor.execute('DELETE FROM calc_person p WHERE p.firstname = %s ', [firstName])
    return render(request, 'profile.html')

#creates new user based on inputs
def gettingInputFromCreate(request):
    firstName = request.GET['firstname']
    lastName = request.GET['lastname']
    password = request.GET['password']
    age = request.GET['age']
    height = request.GET['height']
    gender = request.GET['gender']
    ethnicity = request.GET['ethnicity']
    school = request.GET['schools']
    industry = request.GET['industry']

    while 1:
        uniqueId = random.randint(1,100)
        with connection.cursor() as cursor:
            cursor.execute('SELECT p.firstname, p.lastname FROM calc_person p WHERE p.id = %s ',
                           [uniqueId])
            rawData = cursor.fetchall()
        print(rawData)
        if len(rawData) == 0:
            break
        print("id %s", uniqueId)

    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO calc_person "
                       "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);",
                       [str(uniqueId),  firstName, lastName, ethnicity, gender, industry,  height, school, school])

    print("finished")

    return render(request, 'create_profile.html')

def personal_profile(request):
    # if(loggedIn)
        with connections['default'].cursor() as cursor:
            cursor.execute('SELECT * FROM calc_person',
                       [gender, lowerBound, upperBound])
            rawdata = cursor.fetchall()

    return render(request, 'profile.html', {'all_post': rawdata})
#searches based on gender

def preferencePerson(request):
    upperBound = request.GET['maxBound']
    lowerBound = request.GET['minBound']
    gender = request.GET.get('gender')
    ethnicity = request.GET.get('ethnicity')
    school = request.GET.get('schools')
    industry = request.GET.get('industry')

    if school == "None" and industry == "None" and ethnicity == "None":
        with connections['default'].cursor() as cursor:
            cursor.execute('SELECT p.firstname, p.lastname FROM calc_person p WHERE p.gender = %s and '
                           'p.height BETWEEN %s AND %s ',
                           [gender, lowerBound, upperBound])
            rawdata = cursor.fetchall()
    elif school == "None" and industry == "None" and ethnicity != "None":
        with connections['default'].cursor() as cursor:
            cursor.execute('SELECT p.firstname, p.lastname FROM calc_person p WHERE p.gender = %s and '
                           'p.height BETWEEN %s AND %s AND  p.race = %s',
                           [gender, lowerBound, upperBound, ethnicity])
            rawdata = cursor.fetchall()

    elif school == "None" and industry != "None" and ethnicity == "None":
        with connections['default'].cursor() as cursor:
            cursor.execute('SELECT p.firstname, p.lastname FROM calc_person p WHERE p.gender = %s and '
                           'p.height BETWEEN %s AND %s AND  p.companyname = %s',
                           [gender, lowerBound, upperBound, industry])
            rawdata = cursor.fetchall()
    elif school == "None" and industry != "None" and ethnicity != "None":
        with connections['default'].cursor() as cursor:
            cursor.execute('SELECT p.firstname, p.lastname FROM calc_person p WHERE p.gender = %s and '
                           'p.height BETWEEN %s AND %s AND  p.race = %s AND  p.companyname = %s',
                           [gender, lowerBound, upperBound, ethnicity, industry])
            rawdata = cursor.fetchall()

    elif school != "None" and industry == "None" and ethnicity == "None":
        with connection.cursor() as cursor:
            cursor.execute('SELECT p.firstname, p.lastname FROM calc_person p WHERE p.gender = %s and '
                           'p.height BETWEEN %s AND %s AND  p.schoolname = %s',
                           [gender, lowerBound, upperBound, school])
            rawdata = cursor.fetchall()

    elif school != "None" and industry == "None" and ethnicity != "None":
        with connections['default'].cursor() as cursor:
            cursor.execute('SELECT p.firstname, p.lastname FROM calc_person p WHERE p.gender = %s and '
                           'p.height BETWEEN %s AND %s AND p.schoolname = %s AND  p.race = %s',
                           [gender, lowerBound, upperBound, school, ethnicity])
            rawdata = cursor.fetchall()

    elif school != "None" and industry != "None" and ethnicity == "None":
        with connections['default'].cursor() as cursor:
            cursor.execute('SELECT p.firstname, p.lastname FROM calc_person p WHERE p.gender = %s and '
                           'p.height BETWEEN %s AND %s AND p.schoolname = %s AND  p.companyname = %s',
                           [gender, lowerBound, upperBound, school, industry])
            rawdata = cursor.fetchall()
    else:
        with connections['default'].cursor() as cursor:
            cursor.execute('SELECT p.firstname, p.lastname FROM calc_person p WHERE p.gender = %s and '
                           'p.height BETWEEN %s AND %s AND p.schoolname = %s AND p.race = %s AND p.companyname = %s',
                           [gender, lowerBound, upperBound, school, ethnicity])
            rawdata = cursor.fetchall()

    print(type(rawdata))
    return render(request, 'results.html', {'all_post': rawdata})
