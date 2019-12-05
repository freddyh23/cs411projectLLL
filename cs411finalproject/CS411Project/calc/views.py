from django.shortcuts import render
from .models import Users
from django.db import connections, connection
from collections import namedtuple
import random
import pyaes

UNIQUE_ID = -1

# Create your views here.
def home(request):
    return render(request, 'home.html')

def updatePage(request):
    return render(request, 'base.html')

def allusers(request):
    return render(request, 'allusers.html')

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
    encrypt_password = "empty"


    for e in Users.objects.using('users_db').filter(user_name=username):
        encrypt_password = e.password
    print("encrypt_password: ", encrypt_password)

    byte_key = "cs411cs411cs411cs411cs411cs411cs"

    decrypt_password = AES_decrypt(byte_key, password)
    if str(decrypt_password) != str(encrypt_password) or encrypt_password == "empty":
        return render(request, 'login.html')


    global UNIQUE_ID
    for e in Users.objects.using('users_db').filter(user_name=username):
        UNIQUE_ID = int(e.uid)

    with connections['default'].cursor() as cursor:
        cursor.execute('SELECT * FROM calc_person p Where p.id = %s',
                       [UNIQUE_ID])
        rawdata = cursor.fetchall()

    return render(request, 'profile.html', {'all_post': rawdata})

def suggestions(request):

    with connections['default'].cursor() as cursor:
        cursor.execute('SELECT * FROM calc_suggestions p WHERE p.uid = %s ',
                       [str(UNIQUE_ID)])
        ids = namedtuplefetchall(cursor)
    print(ids)
    all_post = []
    for i in range(0, len(ids)):
        with connections['default'].cursor() as cursor:
            cursor.execute('SELECT p.firstname, p.lastname, p.age FROM calc_person p WHERE p.id = %s ', [str(ids[i].suggested)])
            rawdata = namedtuplefetchall(cursor)
            person = [rawdata[0].firstname, rawdata[0].lastname]
        all_post.append(person)
    return render(request, 'results.html', {'all_post': all_post})



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

    print("lastname: ",lastName)

    global UNIQUE_ID

    if firstName != "":
        with connections['default'].cursor() as cursor:
            cursor.execute('UPDATE calc_person  SET firstname = %s WHERE id = %s ', [firstName, UNIQUE_ID])

    if lastName != "":
        print("in LastName")
        with connections['default'].cursor() as cursor:
            cursor.execute('UPDATE calc_person  SET lastname = %s WHERE id = %s ', [lastName, UNIQUE_ID])

    if age != "":
        print("Here")
        with connections['default'].cursor() as cursor:
            cursor.execute('UPDATE calc_person  SET age = %s WHERE id = %s ', [age, UNIQUE_ID])
    if height != "":
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
    user = Users.objects.using('users_db').get(uid=UNIQUE_ID)
    user.delete()
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

    encrypted_password = AES_encrpyt("cs411cs411cs411cs411cs411cs411cs", password)
    print("encrypted_password", encrypted_password)
    user = Users()
    user.user_name = username
    user.password =  encrypted_password
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
    state = request.GET.get('state')
    maxBoundAge = request.GET['maxBoundAge']
    minBoundAge = request.GET['minBoundAge']

    print("in perference")

    if upperBound == "" or lowerBound == "" or gender == "None" or maxBoundAge == "" or minBoundAge == "":
        return render(request, 'home.html')

    global UNIQUE_ID

    if school == "None" and industry == "None" and ethnicity == "None":
        with connections['default'].cursor() as cursor:
            cursor.execute('SELECT p.firstname, p.lastname FROM calc_person p WHERE p.gender = %s and '
                           'p.height BETWEEN %s AND %s AND p.age BETWEEN %s AND %s',
                           [gender, lowerBound, upperBound, minBoundAge, maxBoundAge])
            rawdata = cursor.fetchall()

        with connections['default'].cursor() as cursor:
            cursor.execute('SELECT p.id FROM calc_person p WHERE p.gender = %s and '
                           'p.height BETWEEN %s AND %s AND p.age BETWEEN %s AND %s',
                           [gender, lowerBound, upperBound, minBoundAge, maxBoundAge])
            ids = namedtuplefetchall(cursor)

        deleteSuggestion()

        for i in range(0, len(ids)):
            print("i: ", type(i))
            randonID = choosingUID()
            with connections['default'].cursor() as cursor:
                cursor.execute('INSERT INTO calc_suggestions '
                               'VALUES(%s,%s, %s);',
                       [randonID,UNIQUE_ID, ids[int(i)].id])

    elif school == "None" and industry == "None" and ethnicity != "None":
        with connections['default'].cursor() as cursor:
            cursor.execute('SELECT p.firstname, p.lastname FROM calc_person p WHERE p.gender = %s and '
                           'p.height BETWEEN %s AND %s AND  p.race = %s AND p.age BETWEEN %s AND %s',
                           [gender, lowerBound, upperBound, ethnicity, minBoundAge, maxBoundAge])
            rawdata = cursor.fetchall()

        with connections['default'].cursor() as cursor:
            cursor.execute('SELECT p.id FROM calc_person p WHERE p.gender = %s and '
                           'p.height BETWEEN %s AND %s AND  p.race = %s AND p.age BETWEEN %s AND %s',
                           [gender, lowerBound, upperBound, minBoundAge, maxBoundAge])
            ids = namedtuplefetchall(cursor)
        # print("ids: ", ids[0].id)
        deleteSuggestion()
        for i in range(0, len(ids)):
            print("i: ", type(i))
            randonID = choosingUID()
            with connections['default'].cursor() as cursor:
                cursor.execute('INSERT INTO calc_suggestions '
                               'VALUES(%s,%s, %s);',
                               [randonID,UNIQUE_ID, ids[int(i)].id])

    elif school == "None" and industry != "None" and ethnicity == "None":
        with connections['default'].cursor() as cursor:
            cursor.execute('SELECT p.firstname, p.lastname FROM calc_person p WHERE p.gender = %s and '
                           'p.height BETWEEN %s AND %s AND  p.companyname = %s AND p.age BETWEEN %s AND %s',
                           [gender, lowerBound, upperBound, industry, minBoundAge, maxBoundAge])
            rawdata = cursor.fetchall()

        with connections['default'].cursor() as cursor:
            cursor.execute('SELECT p.id FROM calc_person p WHERE p.gender = %s and '
                           'p.height BETWEEN %s AND %s AND  p.companyname = %s AND p.age BETWEEN %s AND %s',
                           [gender, lowerBound, upperBound, minBoundAge, maxBoundAge])
            ids = namedtuplefetchall(cursor)
        # print("ids: ", ids[0].id)
        deleteSuggestion()
        for i in range(0, len(ids)):
            print("i: ", type(i))
            randonID = choosingUID()
            with connections['default'].cursor() as cursor:
                cursor.execute('INSERT INTO calc_suggestions '
                               'VALUES(%s,%s, %s);',
                               [randonID,UNIQUE_ID, ids[int(i)].id])


    elif school == "None" and industry != "None" and ethnicity != "None":
        with connections['default'].cursor() as cursor:
            cursor.execute('SELECT p.firstname, p.lastname FROM calc_person p WHERE p.gender = %s AND '
                           'p.height BETWEEN %s AND %s AND  p.race = %s AND  p.companyname = %s AND p.age BETWEEN %s AND %s',
                           [gender, lowerBound, upperBound, ethnicity, industry, minBoundAge, maxBoundAge])
            rawdata = cursor.fetchall()


        with connections['default'].cursor() as cursor:
            cursor.execute('SELECT p.id FROM calc_person p WHERE p.gender = %s and '
                           'p.height BETWEEN %s AND %s AND  p.race = %s AND  p.companyname = %s AND p.age BETWEEN %s AND %s',
                           [gender, lowerBound, upperBound, minBoundAge, maxBoundAge])
            ids = namedtuplefetchall(cursor)
        # print("ids: ", ids[0].id)
        deleteSuggestion()
        for i in range(0, len(ids)):
            print("i: ", type(i))
            randonID = choosingUID()
            with connections['default'].cursor() as cursor:
                cursor.execute('INSERT INTO calc_suggestions '
                               'VALUES(%s,%s, %s);',
                               [randonID,UNIQUE_ID, ids[int(i)].id])

    elif school != "None" and industry == "None" and ethnicity == "None":
        with connection.cursor() as cursor:
            cursor.execute('SELECT p.firstname, p.lastname FROM calc_person p WHERE p.gender = %s and '
                           'p.height BETWEEN %s AND %s AND  p.schoolname = %s AND p.age BETWEEN %s AND %s',
                           [gender, lowerBound, upperBound, school, minBoundAge, maxBoundAge])
            rawdata = cursor.fetchall()

        with connections['default'].cursor() as cursor:
            cursor.execute('SELECT p.id FROM calc_person p WHERE p.gender = %s and '
                           'p.height BETWEEN %s AND %s AND p.schoolname = %s AND p.age BETWEEN %s AND %s',
                           [gender, lowerBound, upperBound, minBoundAge, maxBoundAge])
            ids = namedtuplefetchall(cursor)
        # print("ids: ", ids[0].id)
        deleteSuggestion()
        for i in range(0, len(ids)):
            print("i: ", type(i))
            randonID = choosingUID()
            with connections['default'].cursor() as cursor:
                cursor.execute('INSERT INTO calc_suggestions '
                               'VALUES(%s,%s, %s);',
                               [randonID,UNIQUE_ID, ids[int(i)].id])

    elif school != "None" and industry == "None" and ethnicity != "None":
        with connections['default'].cursor() as cursor:
            cursor.execute('SELECT p.firstname, p.lastname FROM calc_person p WHERE p.gender = %s and '
                           'p.height BETWEEN %s AND %s AND p.schoolname = %s AND  p.race = %s AND p.age BETWEEN %s AND %s',
                           [gender, lowerBound, upperBound, school, ethnicity, minBoundAge, maxBoundAge])
            rawdata = cursor.fetchall()

        with connections['default'].cursor() as cursor:
            cursor.execute('SELECT p.id FROM calc_person p WHERE p.gender = %s and '
                           'p.height BETWEEN %s AND %s AND p.schoolname = %s AND  p.race = %s AND p.age BETWEEN %s AND %s',
                           [gender, lowerBound, upperBound, minBoundAge, maxBoundAge])
            ids = namedtuplefetchall(cursor)
        # print("ids: ", ids[0].id)
        deleteSuggestion()
        for i in range(0, len(ids)):
            print("i: ", type(i))
            randonID = choosingUID()
            with connections['default'].cursor() as cursor:
                cursor.execute('INSERT INTO calc_suggestions '
                               'VALUES(%s,%s, %s);',
                               [randonID,UNIQUE_ID, ids[int(i)].id])

    elif school != "None" and industry != "None" and ethnicity == "None":
        with connections['default'].cursor() as cursor:
            cursor.execute('SELECT p.firstname, p.lastname FROM calc_person p WHERE p.gender = %s and '
                           'p.height BETWEEN %s AND %s AND p.schoolname = %s AND  p.companyname = %s AND p.age BETWEEN %s AND %s',
                           [gender, lowerBound, upperBound, school, industry, minBoundAge, maxBoundAge])
            rawdata = cursor.fetchall()

        with connections['default'].cursor() as cursor:
            cursor.execute('SELECT p.id FROM calc_person p WHERE p.gender = %s and '
                           'p.height BETWEEN %s AND %s AND p.schoolname = %s AND  p.companyname = %s AND p.age BETWEEN %s AND %s',
                           [gender, lowerBound, upperBound, minBoundAge, maxBoundAge])
            ids = namedtuplefetchall(cursor)
        # print("ids: ", ids[0].id)
        deleteSuggestion()
        for i in range(0, len(ids)):
            print("i: ", type(i))
            randonID = choosingUID()
            with connections['default'].cursor() as cursor:
                cursor.execute('INSERT INTO calc_suggestions '
                               'VALUES(%s,%s, %s);',
                               [randonID,UNIQUE_ID, ids[int(i)].id])

    else:
        print("in else")
        with connections['default'].cursor() as cursor:
            cursor.execute('SELECT p.firstname, p.lastname FROM calc_person p WHERE p.gender = %s and '
                           'p.height BETWEEN %s AND %s AND p.schoolname = %s AND p.race = %s AND p.companyname = %s '
                           'AND p.age BETWEEN %s AND %s',
                           [gender, lowerBound, upperBound, school, ethnicity, industry, minBoundAge, maxBoundAge])
            rawdata = cursor.fetchall()
        print("after first slected")
        with connections['default'].cursor() as cursor:
            cursor.execute('SELECT p.id FROM calc_person p WHERE p.gender = %s and '
                           'p.height BETWEEN %s AND %s AND p.schoolname = %s AND p.race = %s AND p.companyname = %s '
                           'AND p.age BETWEEN %s AND %s',
                           [gender, lowerBound, upperBound, minBoundAge, maxBoundAge])
            ids = namedtuplefetchall(cursor)
        print("after second slected")
        # print("ids: ", ids[0].id)
        deleteSuggestion()
        for i in range(0, len(ids)):
            print("i: ", type(i))
            randonID = choosingUID()
            with connections['default'].cursor() as cursor:
                cursor.execute('INSERT INTO calc_suggestions '
                               'VALUES(%s,%s, %s);',
                               [randonID,UNIQUE_ID, ids[int(i)].id])
        print("after insert slected")


    with connection.cursor() as cursor:
        cursor.execute('DELETE FROM calc_scores p WHERE p.uid = %s',
                       [str(UNIQUE_ID)])

    with connection.cursor() as cursor:
        cursor.execute('DELETE FROM calc_perference p WHERE p.uid = %s',
                       [str(UNIQUE_ID)])

    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO calc_perference "
                       "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                       [UNIQUE_ID,  gender, lowerBound, upperBound, minBoundAge, maxBoundAge,  ethnicity, school, school, industry])

    return render(request, 'results.html', {'all_post': rawdata})



def AES_encrpyt(key, plaintext):
    # A 256 bit (32 byte) key
    if(len(key) == 32):
        key1 = key.encode('utf-8')
        aes = pyaes.AESModeOfOperationCTR(key1)
        ciphertext = aes.encrypt(plaintext)
    else:
        ciphertext = "invalid"
    return ciphertext

def AES_decrypt(key, password):
    if(len(key) == 32):
        key1 = key.encode('utf-8')
        aes = pyaes.AESModeOfOperationCTR(key1)
        enc_password = aes.encrypt(password)
    else:
        enc_password = "invalid"
    return enc_password


def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def choosingUID():
    while 1:
        uniqueId = random.randint(1,10000)
        with connections['default'].cursor() as cursor:
            cursor.execute('SELECT * FROM calc_suggestions p WHERE p.id = %s ',
                           [str(uniqueId)])
            rawData = cursor.fetchall()
        print(rawData)
        if len(rawData) == 0:
            return uniqueId

def deleteSuggestion():
    with connections['default'].cursor() as cursor:
        cursor.execute('DELETE FROM calc_suggestions p WHERE p.uid = %s ',
                       [str(UNIQUE_ID)])
