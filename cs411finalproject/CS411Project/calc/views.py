from django.shortcuts import render
from .models import Users
from django.db import connections, connection
import random


# Create your views here.
def home(request):
    return render(request, 'home.html')

def updatePage(request):
    return render(request, 'base.html')

def createProfilePage(request):
    return render(request, 'create_profile.html')

def viewProfile(request):
    print(UNIQUE_ID)
    with connections['default'].cursor() as cursor:
        cursor.execute('SELECT * FROM calc_person p Where p.id = %s',
                       [UNIQUE_ID])
        rawdata = cursor.fetchall()
    print(rawdata)
    return render(request, 'profile.html', {'all_post': rawdata})

def login(request):
    return render(request, 'login.html')

def logout(request):
    global UNIQUE_ID
    UNIQUE_ID = -1
    return render(request, 'login.html')

def login_action(request):

    username = request.GET.get('username')
    password = request.GET.get('password')

    results = list(Users.objects.using('users_db').filter(user_name=username, password=password))

    if len(results) == 0:
        return render(request, 'login.html')

    global UNIQUE_ID
    for e in Users.objects.using('users_db').filter(user_name=username, password=password):
        UNIQUE_ID = int(e.uid)

    # print("results: ", results.user_name)
    # user = Users()
    # user.user_name = username
    # user.password = password
    # user.save()


    return render(request, 'profile.html')

def suggestions(request):
    return render(request, 'results.html')

UNIQUE_ID = -1

# updates profile with new height

def updateProfile(request):
    firstName = request.GET.get('firstname')
    lastName = request.GET.get('lastname')
    password = request.GET.get('password')
    age = 0
    age = request.GET.get('age')

    height = request.GET.get('height')
    gender = request.GET.get('gender')
    ethnicity = request.GET.get('ethnicity')
    university = request.GET.get('university')
    jobIndustry = request.GET.get('jobIndustry')



    global UNIQUE_ID

    if firstName is not None:
        with connections['default'].cursor() as cursor:
            cursor.execute('UPDATE calc_person  SET firstname = %s WHERE id = %s ', [firstName, UNIQUE_ID])

    if lastName is not None:
        with connections['default'].cursor() as cursor:
            cursor.execute('UPDATE calc_person  SET lastname = %s WHERE id = %s ', [lastName, UNIQUE_ID])

    if age is not None:
        with connections['default'].cursor() as cursor:
            cursor.execute('UPDATE calc_person  SET age = %s WHERE id = %s ', [age, UNIQUE_ID])
    if height is not None:
        with connections['default'].cursor() as cursor:
            cursor.execute('UPDATE calc_person  SET height = %s WHERE id = %s ', [height, UNIQUE_ID])
    if gender != "None":
        with connection.cursor() as cursor:
            cursor.execute('UPDATE calc_person  SET gender = %s WHERE id = %s ', [gender, UNIQUE_ID])

    if ethnicity != "None":
        with connection.cursor() as cursor:
            cursor.execute('UPDATE calc_person  SET race = %s WHERE id = %s ', [ethnicity, UNIQUE_ID])

    if university != "None":
        with connection.cursor() as cursor:
            cursor.execute('UPDATE calc_person  SET schoolname = %s WHERE id = %s ', [university, UNIQUE_ID])

    if jobIndustry != "None":
        with connection.cursor() as cursor:
            cursor.execute('UPDATE calc_person  SET companyname = %s WHERE id = %s ', [jobIndustry, UNIQUE_ID])

    return render(request, 'base.html')


#deletes persom based on name

def deletePerson(request):
    global UNIQUE_ID
    with connection.cursor() as cursor:
        cursor.execute('DELETE FROM calc_person p WHERE p.id = %s ', [UNIQUE_ID])
    UNIQUE_ID = -1
    return render(request, 'login.html')

#creates new user based on inputs
def gettingInputFromCreate(request):
    firstName = request.GET['firstname']
    lastName = request.GET['lastname']
    username = request.GET.get('username')
    password = request.GET['password']
    age = request.GET['age']
    height = request.GET['height']
    gender = request.GET['gender']
    ethnicity = request.GET['ethnicity']
    school = request.GET['schools']
    industry = request.GET['industry']

    while 1:
        uniqueId = random.randint(1,100)
        with connections['default'].cursor() as cursor:
            cursor.execute('SELECT p.firstname, p.lastname FROM calc_person p WHERE p.id = %s ',
                           [uniqueId])
            rawData = cursor.fetchall()
        print(rawData)
        if len(rawData) == 0:
            break
        print("id %s", uniqueId)

    with connections['default'].cursor() as cursor:
        cursor.execute("INSERT INTO calc_person "
                       "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                       [str(uniqueId),  firstName, lastName, gender, height, ethnicity, industry, school,
                        industry, age])

    user = Users()
    user.user_name = username
    user.password = password
    user.uid = uniqueId
    user.save(using='users_db')

    global UNIQUE_ID
    UNIQUE_ID = uniqueId
    print("finished", UNIQUE_ID)

    with connections['default'].cursor() as cursor:
        cursor.execute('SELECT * FROM calc_person p Where p.id = %s',
                       [UNIQUE_ID])
        rawdata = cursor.fetchall()

    return render(request, 'profile.html', {'all_post': rawdata})

def personal_profile(request):
    with connections['default'].cursor() as cursor:
        cursor.execute('SELECT * FROM calc_person p Where p.id = %s',
                   [UNIQUE_ID])
        rawdata = cursor.fetchall()

    return render(request, 'profile.html', {'all_post': rawdata})
# searches based on gender

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
                           [gender, lowerBound, upperBound, school, ethnicity, industry])
            rawdata = cursor.fetchall()

    global UNIQUE_ID

    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM calc_perference p WHERE p.uid = %s',
                       [UNIQUE_ID])
    alreadyInclude = cursor.fetchall()

    if len(alreadyInclude) == 0:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO calc_perference "
                           "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                           [UNIQUE_ID,  gender, lowerBound, upperBound, 0, 0,  ethnicity, school, school, industry])

    return render(request, 'results.html')
