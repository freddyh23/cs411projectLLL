from django.shortcuts import render
from .models import Person
from django.db import connection

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
    height = request.GET.get('height')
    with connection.cursor() as cursor:
        cursor.execute('UPDATE calc_person  SET height = %s WHERE firstname = %s ', [height, firstName])
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
    num = int(Person.objects.count()) + 1
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO calc_person "
                       "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);",
                       [str(num),  firstName, lastName, ethnicity, gender, industry,  height, school, school])

    print("finished")

    return render(request, 'create_profile.html')


#searches based on gender

def preferencePerson(request):
    upperBound = request.GET['maxBound']
    lowerBound = request.GET['minBound']
    gender = request.GET.get('gender')
    ethnicity = request.GET.get('ethnicity')
    school = request.GET.get('schools')
    industry = request.GET.get('industry')
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM calc_person p WHERE p.gender = %s', [gender])
        rawdata = cursor.fetchall()
        x = []
        for raw in rawdata:
            x.append(raw)
        print(x)
    return render(request, 'results.html', {'all_post': x})