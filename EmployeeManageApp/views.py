from django.shortcuts import render, redirect, get_object_or_404
from .models import Personal, Office, Salary
from .forms import PersonalForm, OfficeForm, SalaryForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def npersonal(request):
    if request.method == 'POST':
        form = PersonalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('personal_list')
    else:
        form = PersonalForm()
    return render(request, 'npersonal.html', {'form': form})

def personal_list(request):
    personal_data = Personal.objects.all()
    return render(request, 'personal_list.html', {'personal_data': personal_data})

def noffice(request):
    if request.method == 'POST':
        form = OfficeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('office_list')
    else:
        form = OfficeForm()
    return render(request, 'noffice.html', {'form': form})

def office_list(request):
    office_data = Office.objects.all()
    return render(request, 'office_list.html', {'office_data': office_data})

def nsalary(request):
    if request.method == 'POST':
        form = SalaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('salary_list')
    else:
        form = SalaryForm()
    return render(request, 'nsalary.html', {'form': form})

def salary_list(request):
    salary_data = Salary.objects.all()
    return render(request, 'salary_list.html', {'salary_data': salary_data})

def modify_personal(request, pk):
    personal = Personal.objects.get(pk=pk)
    print(personal)
    if request.method == 'POST':
        form = PersonalForm(request.POST, instance=personal)
        if form.is_valid():
            form.save()
            return redirect('personal_list')
    else:
        form = PersonalForm(instance=personal)
    return render(request, 'modify_personal.html', {'form': form})

def modifyoffice(request, pk):
    office = Office.objects.get(pk=pk)
    if request.method == 'POST':
        form = OfficeForm(request.POST, instance=office)
        if form.is_valid():
            form.save()
            return redirect('office_list')
    else:
        form = OfficeForm(instance=office)
    return render(request, 'modifyoffice.html', {'form': form})


# from django.shortcuts import get_object_or_404

# Delete views
def delete_personal(request, pk):
    personal = get_object_or_404(Personal, pk=pk)
    if request.method == 'POST':
        personal.delete()
        return redirect('personal_list')
    return render(request, 'delete_personal.html', {'personal': personal})

def delete_office(request, pk):
    office = get_object_or_404(Office, pk=pk)
    if request.method == 'POST':
        office.delete()
        return redirect('office_list')
    return render(request, 'delete_office.html', {'office': office})

def delete_salary(request, pk):
    salary = get_object_or_404(Salary, pk=pk)
    if request.method == 'POST':
        salary.delete()
        return redirect('salary_list')
    return render(request, 'delete_salary.html', {'salary': salary})

# Search views
def search_personal(request):
    query = request.GET.get('query')
    if query:
        personal_data = Personal.objects.filter(name__icontains=query)
    else:
        personal_data = Personal.objects.all()
    return render(request, 'search_personal.html', {'personal_data': personal_data})

def search_office(request):
    query = request.GET.get('query')
    if query:
        office_data = Office.objects.filter(name__icontains=query)
    else:
        office_data = Office.objects.all()
    return render(request, 'search_office.html', {'office_data': office_data})

def search_salary(request):
    query = request.GET.get('query')
    if query:
        salary_data = Salary.objects.filter(name__icontains=query)
    else:
        salary_data = Salary.objects.all()
    return render(request, 'search_salary.html', {'salary_data': salary_data})

# ... (other view functions for delete and search operations)












# from django.shortcuts import render

# # Create your views here.
# import mysql.connector as a

# legend = a.connect(host="localhost",
#                    user="root",
#                    passwd="247231",
#                    database="employee")


# def npersonal():
#     n = input("ENTER EMPLOYEE NAME :")
#     y = input("ENTER GENDER :")
#     c = input("ENTER EMPLOYEE'S CITY NAME :")
#     d = input("ENTER EMPLOYEE'S D.O.B :")
#     p = input("ENTER EMPLOYEE'S PHONE :")
#     data = (n, y, c, d, p)
#     sql = 'insert into personal value(%s,%s,%s,%s,%s)'
#     c = legend.cursor()
#     c.execute(sql, data)
#     legend.commit()
#     print("----------------*----------DATA ENTERED SUCCESFULL------------*--------------")
#     main()


# def personal():
#     sql = "select*from personal"
#     c = legend.cursor()
#     c.execute(sql)
#     d = c.fetchall()
#     if len(d) == 0:
#         print("--------------*----------NO DATA IS FOUND---------------*------------")
#     else:
#         for i in d:
#             print(i)
#     main()


# def noffice():
#     ec = input("ENTER EMPLOYEE CODE :")
#     n = input("ENTER EMPLOYEE NAME :")
#     ps = input("ENTER EMPLOYEE'S POST :")
#     j = input("ENTER EMPLOYEE'S JOINING DATE :")
#     bp = int(input("ENTER EMPLOYEE'S ASSIGNED SALARY :"))
#     data = (ec, n, ps, j, bp)
#     sql = 'insert into office values (%s,%s,%s,%s,%s)'
#     c = legend.cursor()
#     c.execute(sql, data)
#     legend.commit()
#     print("----------------*----------DATA ENTERED SUCCESSFULLY----------------*----------")
#     main()



# def office():
#     sql = "select*from office"
#     c = legend.cursor()
#     c.execute(sql)
#     d = c.fetchall()
#     if len(d) == 0:
#         print("--------------*----------NO DATA IS FOUND---------------*------------")
#     else:
#         for i in d:
#             print(i)
#     main()


# def nsalary():
#     ec = input("ENTER EMPLOYEE CODE :")
#     v = (ec,)
#     sql = "select basicpay,name from office where Ecode=%s"
#     c = legend.cursor()
#     c.execute(sql, v)
#     bs = c.fetchone()
#     na = bs[1]
#     y = int(input("ENTER MONTHS:"))
#     wd = int(input("ENTER WORKING DAYS:"))
#     print("NAME", na)
#     print("BASIC SALARY:", bs[0])
#     td = y * 30 + wd
#     mn = td / 30
#     fp = bs[0] * mn
#     data = (ec, na, y, wd, fp)
#     sql = 'insert into salary values (%s,%s,%s,%s,%s)'
#     c = legend.cursor()
#     c.execute(sql, data)
#     legend.commit()
#     print("----------------*----------DATA ENTERED SUCCESSFULLY----------------*----------")
#     main()


# def salary():
#     sql = "select*from salary"
#     c = legend.cursor()
#     c.execute(sql)
#     d = c.fetchall()
#     if len(d) == 0:
#         print("--------------*----------NO DATA IS FOUND---------------*------------")
#     else:
#         for i in d:
#             print(i)
#     main()


# def modify_personal():
#     print("""
#           CHOOSE CRITERIA FOR UPDATE
#           (::PLESE CHOOSE THAT CRITERIA WHICH IS CORRECT(NEED NO CHANGE)::)
#           1.BY NAME
#           2.BY DATE OF BIRTH
#           3.BY PHONE NO
#           4.BY CITY
#           """)
#     choice = input("ENTER YOUR CHOICE:")
#     if choice == '1':
#         n = input("ENTER EMPLOYEE NAME:")
#         city = input("ENTER EMPLPOYEE'S UPDATED CITY NAME:")
#         dob = input("ENTER EMPLOYEE UPDATED D.O.B:")
#         phone = input("ENTER EMPLOYEE UPDATED PHONE NO:")
#         data = (city, dob, phone, n)
#         sql = "update personal set city=%s,birthdate=%s,phone=%s where name=%s"
#         c = legend.cursor()
#         c.execute(sql, data)
#         legend.commit
#     elif choice == '2':
#         n = input("ENTER EMPLOYEE DATE OF BIRTH:")
#         city = input("ENTER EMPLPOYEE'S UPDATED CITY NAME:")
#         dob = input("ENTER EMPLOYEE UPDATED NAME:")
#         phone = input("ENTER EMPLOYEE UPDATED PHONE NO:")
#         data = (city, dob, phone, n)
#         sql = "update personal set city=%s,name=%s,phone=%s where birthdate=%s"
#         c = legend.cursor()
#         c.execute(sql, data)
#         legend.commit
#     elif choice == '3':
#         n = input("ENTER EMPLOYEE PHONE NO:")
#         city = input("ENTER EMPLPOYEE'S UPDATED CITY NAME:")
#         dob = input("ENTER EMPLOYEE UPDATED D.O.B:")
#         phone = input("ENTER EMPLOYEE UPDATED NAME:")
#         data = (city, dob, phone, n)
#         sql = "update personal set city=%s,birthdate=%s,name=%s where phone=%s"
#         c = legend.cursor()
#         c.execute(sql, data)
#         legend.commit
#     elif choice == '4':
#         n = input("ENTER EMPLOYEE CITY NAME:")
#         city = input("ENTER EMPLPOYEE'S UPDATED NAME:")
#         dob = input("ENTER EMPLOYEE UPDATED D.O.B:")
#         phone = input("ENTER EMPLOYEE UPDATED PHONE NO:")
#         data = (city, dob, phone, n)
#         sql = "update personal set name=%s,birthdate=%s,phone=%s where city=%s"
#         c = legend.cursor()
#         c.execute(sql, data)
#         legend.commit
#     print("-----------UPDATE IS SUCCESSFUL-----------")
#     main()



# def modifyoffice():
#     print("""
#         CHOOSE CRITERIA FOR UPDATE
#         1.BY EMPLOYEE CODE
#         2.BY EMPLOYEE NAME
#         3.BY EMPLOYEE POST
#         4.BY EMPLOYEE JOINING DATE
#         """)
#     choice = input("ENTER YOUR CHOICE:")
#     if choice == '1':
#         ec = input("ENTER EMPLOYEE CODE :")
#         dd = input("ENTER EMPLOYEE NAME:")
#         ps = input("UPDATE EMPLOYEE'S POST :")
#         j = input("UPDATE EMPLOYEE'S JOINING DATE :")
#         # bp=int(input("UPDATE EMPLOYEE'S ASSIGNED SALARY :"))
#         sql = "update office set post='{}',joining='{}',name='{}' where ecode='{}'".format(ps, j, dd, ec)
#         c = legend.cursor()
#         c.execute(sql)
#         legend.commit
#     elif choice == '2':
#         ec = input("ENTER EMPLOYEE NAME :")
#         cc = input("ENTER EMPLOYEE ECODE:")
#         ps = input("UPDATE EMPLOYEE'S POST :")
#         j = input("UPDATE EMPLOYEE'S JOINING DATE :")
#         bp = int(input("UPDATE EMPLOYEE'S ASSIGNED SALARY :"))
#         sql = "update office set ecode='{}',post='{}',joining='{}',basicpay='{}' where name='{}'".format(cc, ps, j, bp,
#                                                                                                          ec)
#         c = legend.cursor()
#         c.execute(sql)
#         legend.commit
#     elif choice == '3':
#         ec = input("ENTER EMPLOYEE POST :")
#         cc = input("ENTER EMPLOYEE ECODE:")
#         ps = input("UPDATE EMPLOYEE NAME :")
#         j = input("UPDATE EMPLOYEE'S JOINING DATE :")
#         bp = int(input("UPDATE EMPLOYEE'S ASSIGNED SALARY :"))
#         data = (ps, j, bp, cc, ec)
#         sql = "update office set name=%s,joining=%s,basicpay=%s,ecode=%s where post=%s"
#         c = legend.cursor()
#         c.execute(sql, data)
#         legend.commit
#     elif choice == '4':
#         ec = input("ENTER EMPLOYEE JOINING DATE :")
#         cc = input("ENTER EMPLOYEE ECODE:")
#         ps = input("UPDATE EMPLOYEE'S POST :")
#         j = input("UPDATE EMPLOYEE NAME :")
#         bp = int(input("UPDATE EMPLOYEE'S ASSIGNED SALARY :"))
#         data = (ps, j, bp, cc, ec)
#         sql = "update office set post=%s,name=%s,basicpay=%s,ecode=%s where joining=%s"
#         c = legend.cursor()
#         c.execute(sql, data)
#         legend.commit
#     print("---------------UPDATE SUCCESSFUL-------------")
#     main()


# def deletepersonal():
#     print("""
#           CHOOSE CRITERIA FOR UPDATE
#           1.BY NAME
#           2.BY DATE OF BIRTH
#           3.BY PHONE NO
#           4.BY CITY
#           """)
#     choice = input("ENTER YOUR CHOICE:")
#     if choice == '1':
#         n = input("ENTER EMPLOYEE NAME:")
#         sql = "Delete from personal where name='{}'".format(n)
#         c = legend.cursor()
#         c.execute(sql)
#         legend.commit
#     elif choice == '2':
#         n = input("ENTER EMPLOYEE DATE OF BIRTH:")
#         sql = "Delete from personal where birthdate='{}'".format(n)
#         c = legend.cursor()
#         c.execute(sql)
#         legend.commit
#     elif choice == '3':
#         n = input("ENTER EMPLOYEE PHONE NO:")
#         sql = "Delete from personal where phone='{}'".format(n)
#         c = legend.cursor()
#         c.execute(sql)
#         legend.commit
#     elif choice == '4':
#         n = input("ENTER EMPLOYEE CITY:")
#         sql = "Delete from personal where city='{}'".format(n)
#         c = legend.cursor()
#         c.execute(sql)
#         legend.commit
#     print("--------------DELETED SUCCESSFULLY-----------")
#     main()


# def deleteoffice():
#     print("""
#         CHOOSE CRITERIA FOR DELETION
#         1.BY EMPLOYEE CODE
#         2.BY EMPLOYEE NAME
#         3.BY EMPLOYEE POST
#         4.BY EMPLOYEE JOINING DATE
#         """)
#     choice = input("ENTER YOUR CHOICE:")
#     if choice == '1':
#         ec = input("ENTER EMPLOYEE CODE:")
#         sql = "delete from office where ecode='{}'".format(ec)
#         c = legend.cursor()
#         c.execute(sql)
#         legend.commit
#     elif choice == '2':
#         ec = input("ENTER EMPLOYEE NAME:")
#         sql = "delete from office where name='{}'".format(ec)
#         c = legend.cursor()
#         c.execute(sql)
#         legend.commit
#     elif choice == '3':
#         ec = input("ENTER EMPLOYEE POST:")
#         sql = "delete from office where post='{}'".format(ec)
#         c = legend.cursor()
#         c.execute(sql)
#         legend.commit
#     elif choice == '4':
#         ec = input("ENTER EMPLOYEE JOINING DATE:")
#         sql = "delete from office where joining='{}'".format(ec)
#         c = legend.cursor()
#         c.execute(sql)
#         legend.commit
#     else:
#         print("----------INVALID OPTION------------")
#     print("-------------DELETED SUCCESSFULLY---------")
#     main()


# def deletesalary():
#     b = input("ENTER EMPLOYEE ECODE:")
#     sql = "delete from salary where ecode='{}'".format(b)
#     c = legend.cursor()
#     c.execute(sql)
#     legend.commit
#     print("-----------DELETION SUCCESSFUL-----------")
#     main()


# def searchpersonal():
#     print("""
#           CHOOSE CRITERIA FOR SEARCH:
#           1.BY NAME
#           2.BY CITY
#           3.BY DATE OF BIRTH
#           4.BY GENDER
#           5.BY PHONE NUMBER
#           """)
#     choice = input("ENTER YOUR CHOICE:")
#     if choice == '1':
#         n = input("ENTER NAME:")
#         sql = "select* from personal where name='{}'".format(n)
#         c = legend.cursor()
#         c.execute(sql)
#         data = c.fetchall()
#         for i in data:
#             print(i)
#         legend.commit

#     elif choice == '2':
#         n = input("ENTER CITY:")
#         sql = "select* from personal where city='{}'".format(n)
#         c = legend.cursor()
#         c.execute(sql)
#         data = c.fetchall()
#         for i in data:
#             print(i)
#         legend.commit
#     elif choice == '3':
#         n = input("ENTER DATE OF BIRTH:")
#         sql = "select* from personal where birthdate='{}'".format(n)
#         c = legend.cursor()
#         c.execute(sql)
#         data = c.fetchall()
#         for i in data:
#             print(i)
#         legend.commit
#     elif choice == '4':
#         n = input("ENTER GENDER:")
#         sql = "select* from personal where gender='{}'".format(n)
#         c = legend.cursor()
#         c.execute(sql)
#         data = c.fetchall()
#         for i in data:
#             print(i)
#         legend.commit
#     elif choice == '5':
#         n = input("ENTER PHONE NUMBER:")
#         sql = "select* from personal where phone='{}'".format(n)
#         c = legend.cursor()
#         c.execute(sql)
#         data = c.fetchall()
#         for i in data:
#             print(i)
#         legend.commit
#     else:
#         print("----------INVALID OPTION------------")
#     main()


# def searchoffice():
#     print("""
#           CHOOSE CRITERIA FOR SEARCH:
#           1.BY ECODE
#           2.BY NAME
#           3.BY POST
#           4.BY JOINING DATE
#           """)
#     choice = input("ENTER YOUR CHOICE:")
#     if choice == '1':
#         ec = input("ENTER ECODE:")
#         sql = "select* from office where ecode='{}'".format(ec)
#         c = legend.cursor()
#         c.execute(sql)
#         data = c.fetchall()
#         for i in data:
#             print(i)
#         legend.commit
#     elif choice == '2':
#         ec = input("ENTER NAME:")
#         sql = "select* from office where name='{}'".format(ec)
#         c = legend.cursor()
#         c.execute(sql)
#         data = c.fetchall()
#         for i in data:
#             print(i)
#         legend.commit
#     elif choice == '3':
#         ec = input("ENTER POST:")
#         sql = "select* from office where post='{}'".format(ec)
#         c = legend.cursor()
#         c.execute(sql)
#         data = c.fetchall()
#         for i in data:
#             print(i)
#         legend.commit
#     elif choice == '4':
#         ec = input("ENTER JOINING DATE:")
#         sql = "select* from office where joining='{}'".format(ec)
#         c = legend.cursor()
#         c.execute(sql)
#         data = c.fetchall()
#         for i in data:
#             print(i)
#         legend.commit
#     main()


# def searchsalary():
#     m = input("ENTER EMPLOYE ECODE:")
#     sql = "select*from salary where ecode='{}'".format(m)
#     c = legend.cursor()
#     c.execute(sql)
#     data = c.fetchall()
#     for i in data:
#         print(i)
#     legend.commit
#     main()


# def main():
#     while True:
#         print("""
#         1.ADD NEW EMPLOYEE PERSONAL DETAILS
#         2.DISPLAY EMPLOYEE DETAILS
#         3.UPDATE EMPLOYEE DETAILS
#         4.DELETE EMPLOYEE DETAILS
#         5.SEARCH EMPLOYEE DETAIL
#         6.EXIT """)

#         choice = input("ENTER TASK NUMBER :")

#         if (choice == '1'):
#             print("""
#                   1.ADD NEW EMPLOYEE DETAIL
#                   2.ADD NEW EMPLOYEE OFFICE DETAIL
#                   3.ADD NEW EMPLOYEE SALARY DETAIL
#                   """)
#             choice1 = input("ENTER YOUR CHOICE:")
#             if (choice1 == '1'):
#                 npersonal()
#             elif (choice1 == '2'):
#                 noffice()
#             elif (choice1 == '3'):
#                 nsalary()
#             else:
#                 print("------INVALID OPTION------")
#         elif (choice == '2'):
#             print("""
#                   1.DISPLAY EMPLOYEE PERSONAL DETAIL
#                   2.DISPLAY EMPLOYEE OFFICE DETAIL
#                   3.DISPLAY EMPLOYEE SALARY DETAIL
#                   """)
#             choice = input("ENTER YOUR CHOICE:")
#             if (choice == '1'):
#                 personal()
#             elif (choice == '2'):
#                 office()
#             elif (choice == '3'):
#                 salary()
#             else:
#                 print("------INVALID OPTION------")
#         elif (choice == '3'):
#             print("""
#                   1.UPDATE PERSONAL DETAIL
#                   2.UPDATE OFFICE DETAIL
#                   """)
#             choice = input("ENTER YOUR CHOICE:")
#             if (choice == '1'):
#                 modify_personal()
#             elif (choice == '2'):
#                 modifyoffice()
#             else:
#                 print("------INVALID OPTION------")
#         elif (choice == '4'):
#             print("""
#                   1.DELETE PERSONAL DETAIL
#                   2.DELETE OFFICE DETAIL
#                   3.DELETE SALARY DETAIL
#                   """)
#             choice = input("ENTER YOUR CHOICE:")

#             if choice == '1':
#                 deletepersonal()
#             elif choice == '2':
#                 deleteoffice()
#             elif choice == '3':
#                 deletesalary()
#             else:
#                 print("------INVALID OPTION------")
#         elif (choice == '5'):
#             print("""
#                         1.SEARCH PERSONAL DETAIL
#                         2.SEARCH OFFICE DETAIL
#                         3.SEARCH SALARY DETAIL
#                         """)
#             choice = input("ENTER YOUR CHOICE:")
#             if choice == '1':
#                 searchpersonal()
#             elif choice == '2':
#                 searchoffice()
#             elif choice == '3':
#                 searchsalary()
#             else:
#                 print("------INVALID OPTION------")
#         elif choice == '6':
#             print("EXITING...................")

#             break

#         else:
#             print("WRONG CHOICE..TRY AGAIN")


# main()
