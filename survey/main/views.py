from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import JsonResponse
from main.models import student1
from main.models import staff2
from main.models import parent1
from main.models import Industry
from django.core.files.storage import FileSystemStorage
from main.models import Industry
from main.models import Industry1
from main.models import Alumni
from main.models import Alumni1
from main.models import Academician
from main.models import Academician1
import pandas as pd
from django.http import HttpResponse
from django.core.mail import send_mail
import random
import string
import os
from django.utils import timezone
import pandas as pd
from django.http import HttpResponse
from .models import student1  # Import your student1 model

def student(request):
    # Retrieve data from your SQLite database (replace this with your actual data retrieval logic)
    data = student1.objects.values('name','email','batch','vision','mission','peo','pos','created_at')  # Replace YourModel with your actual model

    # Create a pandas DataFrame from the data
    df = pd.DataFrame(data.values())  # You might need to format this according to your model

    # Convert the 'created_at' datetime field to timezone unaware
    df['created_at'] = df['created_at'].apply(lambda x: x.astimezone(timezone.utc).replace(tzinfo=None) if x is not None else None)

    # Create a response object with appropriate headers for an Excel file
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="data.xlsx"'

    # Write the DataFrame to the response as an Excel file
    df.to_excel(response, index=False)

    return response
import pandas as pd
from django.http import HttpResponse
from django.utils import timezone

def staff(request):
    print("lzjck")
    # Retrieve data from your SQLite database (replace this with your actual data retrieval logic)
    data = staff2.objects.values('staff_name', 'staff_email', 'vision', 'mission', 'peo', 'pos', 'created_at')  # Replace YourModel with your actual model

    # Create a pandas DataFrame from the data
    df = pd.DataFrame(data)

    # Convert the 'created_at' datetime field to timezone unaware
    df['created_at'] = df['created_at'].apply(lambda x: x.astimezone(timezone.utc).replace(tzinfo=None) if x is not None else None)

    # Create a response object with appropriate headers for an Excel file
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="data.xlsx"'

    # Define the number of empty columns you want to insert between data columns
    num_empty_columns = 2  # You can adjust this value as needed

    # Insert empty columns into the DataFrame
    for _ in range(num_empty_columns):
        for col_name in df.columns[1:]:  # Start from the second column to avoid emptying the first column
            df.insert(df.columns.get_loc(col_name), f'Empty_{col_name}', ' ')  # Use a space as a placeholder

    print("hello")

    # Write the DataFrame with spacing to the response as an Excel file
    df.to_excel(response, index=False)
    return response

def parent(request):
    # Retrieve data from your SQLite database (replace this with your actual data retrieval logic)
    data = parent1.objects.values('sd','batch','occupation','vision','mission','peo','pos','created_at') # Replace YourModel with your actual model

    # Create a pandas DataFrame from the data
    df = pd.DataFrame(data.values())  # You might need to format this according to your model

    # Convert the 'created_at' datetime field to timezone unaware
    df['created_at'] = df['created_at'].apply(lambda x: x.astimezone(timezone.utc).replace(tzinfo=None) if x is not None else None)

    # Create a response object with appropriate headers for an Excel file
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="data.xlsx"'

    # Write the DataFrame to the response as an Excel file
    df.to_excel(response, index=False)

    return response
def industry(request):
    # Retrieve data from your SQLite database (replace this with your actual data retrieval logic)
    data = Industry1.objects.values('name','working_in','designation','email','vision','mission','poe','pos','created_at')  # Replace YourModel with your actual model

    # Create a pandas DataFrame from the data
    df = pd.DataFrame(data.values())  # You might need to format this according to your model

    # Convert the 'created_at' datetime field to timezone unaware
    df['created_at'] = df['created_at'].apply(lambda x: x.astimezone(timezone.utc).replace(tzinfo=None) if x is not None else None)

    # Create a response object with appropriate headers for an Excel file
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="data.xlsx"'

    # Write the DataFrame to the response as an Excel file
    df.to_excel(response, index=False)

    return response
def alumni(request):
    # Retrieve data from your SQLite database (replace this with your actual data retrieval logic)
    data = Alumni1.objects.values('name','batch_studied','designation','official_mail','vision','mission','pos','poe','created_at') # Replace YourModel with your actual model

    # Create a pandas DataFrame from the data
    df = pd.DataFrame(data.values())  # You might need to format this according to your model

    # Convert the 'created_at' datetime field to timezone unaware
    df['created_at'] = df['created_at'].apply(lambda x: x.astimezone(timezone.utc).replace(tzinfo=None) if x is not None else None)

    # Create a response object with appropriate headers for an Excel file
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="data.xlsx"'

    # Write the DataFrame to the response as an Excel file
    df.to_excel(response, index=False)

    return response


def academy(request):
    # Retrieve data from your SQLite database (replace this with your actual data retrieval logic)
    data = Academician1.objects.values('name', 'working_college', 'designation', 'official_mail', 'vision', 'mission', 'poe', 'pos', 'created_at')  # Replace YourModel with your actual model

    # Create a pandas DataFrame from the data
    df = pd.DataFrame(data)

    # Convert the 'created_at' datetime field to timezone unaware
    df['created_at'] = df['created_at'].apply(lambda x: x.astimezone(timezone.utc).replace(tzinfo=None) if x is not None else None)

    # Create a response object with appropriate headers for an Excel file
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="data.xlsx"'

    # Define a function to apply cell spacing to specific columns
    def format_columns(cell_value):
        return f"   {cell_value}"  # Add 3 spaces before the cell value

    # Apply the formatting function to the 'vision', 'mission', 'poe', and 'pos' columns
    df['vision'] = df['vision'].apply(format_columns)
    df['mission'] = df['mission'].apply(format_columns)
    df['poe'] = df['poe'].apply(format_columns)
    df['pos'] = df['pos'].apply(format_columns)

    # Write the DataFrame to the response as an Excel file
    df.to_excel(response, index=False)

    return response



def excels(request):
    return render(request, "excel.html")
def process(request):
    otp=request.POST.get("otp")
    recived=request.session.get("otp")
    print(otp==recived)
    try:
        if(otp==recived):
            print("hello")
            return JsonResponse({'message':"logged in"})
        else:
            return JsonResponse({'message':"incorrect otp!"})
    except Exception as e:
        return JsonResponse({'message':e})

def generate_otp(length=6):
    otp = ''.join(random.choices(string.digits, k=length))
    return otp
def process_login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        email = "sriram5066@gmail.com"
        print(name, password)

        if name == 'admin':
            # Generate a random OTP
            otp = generate_otp()
            request.session["otp"]=otp

            # Send an email to the provided email address with OTP in the subject
            subject = f'Admin Login OTP: {otp}'
            message = 'You have logged in as admin.'
            from_email = 'ssri47856@gmail.com'  # Replace with your email
            recipient_list = [email]

            try:
                send_mail(subject, message, from_email, recipient_list, fail_silently=False)
                return JsonResponse({'message': 'Email sent successfully.'})
            except Exception as e:
                return JsonResponse({'message': f'Failed to send email: {str(e)}'}, status=500)

        # Handle non-admin user login logic here

        return JsonResponse({'message': 'Logged in successfully.'})
    return JsonResponse({'message': 'Invalid request method'}, status=400)

def disps(request):
    return render(request,'disp.html')
def inde(request):
    if(request.method=="POST"):
        return render(request,'2nd.html')
    return render(request,'index.html')
def home(request):
    return render(request, 'index.html')
def student_group(request):
    return render(request, '2nd.html')
def index(request):
    return render(request,'index1.html')
def gets(request):
    if request.method == "POST":
        s=student1.objects.all()
        for i in s:
            print(i.created_at)
        stakeholder = request.POST.get('stakeholder')
        request.session['stakeholder'] = stakeholder

        if stakeholder == 'student':
            name = request.POST.get('name_student')
            batch = request.POST.get('batch_stu')
            email = request.POST.get('email_stu')
            request.session['email']=email
            request.session['name']=name
            saves=student1(name=name,email=email,batch=batch)
            saves.save()
            response_data = {"message": "Student data received and processed successfully"}
            return JsonResponse(response_data)
        elif stakeholder == 'staff':
            staff_name=request.POST.get('staff_name')
            staff_email=request.POST.get('staff_email')
            request.session['staff_name']=staff_name
            request.session['staff_email']=staff_email
            saves=staff2(staff_name=staff_name,staff_email=staff_email)
            saves.save()
            response_data = {"message": " data received and processed successfully"}
            return JsonResponse(response_data)
        elif stakeholder == 'parent':
            parent_name=request.POST.get('parent_name')
            sd=request.POST.get('sd')
            batch=request.POST.get('batch')
            ocu=request.POST.get('occupation')
            request.session['parent_name']=parent_name
            request.session['sd']=sd
            saves=parent1(parent_name=parent_name,sd=sd,batch=batch,occupation=ocu)
            saves.save()
            response_data = {"message": " data received and processed successfully"}
            return JsonResponse(response_data)
        elif stakeholder == 'industry':
            indus_name = request.POST.get('indus_name')
            working_in = request.POST.get('working_in')
            designation = request.POST.get('designation')
            email_ind = request.POST.get('email_ind')
            request.session['indus_name']=indus_name
            request.session['email']=email_ind
            uploaded_file = request.FILES.get('uploads')  # Access uploaded file
            
            if uploaded_file:
                # Rename the uploaded file using the name of the industry person
                file_content = uploaded_file.read()
                
                # Create a new Industry instance and set the attributes
                instance = Industry1.objects.create(
                    name=indus_name,
                    working_in=working_in,
                    designation=designation,
                    email=email_ind,
                    uploaded_file=file_content  # Assign the path to the new file in the model field
                )
                
                # Return a success message
                response_data = {'message': 'Industry information and file uploaded successfully'}
                return JsonResponse(response_data)
            else:
                response_data = {'error': 'No file was uploaded'}
                return JsonResponse(response_data, status=400)



            response_data = {"message": " data received and processed successfully"}
        elif stakeholder == 'academician':
                name_c = request.POST.get('name_c')
                coll_name = request.POST.get('name_coll')
                desig = request.POST.get('desig')
                id_mail = request.POST.get('id')
                request.session['name_c']=name_c
                request.session['id_mail']=id_mail
                uploaded_file = request.FILES.get('uploads')
                if uploaded_file:
                # Read the binary content of the uploaded file
                    file_content = uploaded_file.read()

                    # Create a new Academician instance and set the attributes
                    instance = Academician1.objects.create(
                        name=name_c,
                        working_college=coll_name,
                        designation=desig,
                        official_mail=id_mail,
                        uploaded_file=file_content  # Save the binary content in the model field
                    )

                    # Return a success message
                    response_data = {'message': 'Academician information and file uploaded successfully'}
                    return JsonResponse(response_data)
                else:
                    response_data = {'error': 'No file was uploaded'}
                    return JsonResponse(response_data, status=400)   
        elif stakeholder == 'alumni':
            name_alumni = request.POST.get('name_alumni')
            batch_studied = request.POST.get('batchs')
            currently_working = request.POST.get('curret')
            designation = request.POST.get('desigs')
            official_mail = request.POST.get('em_id')
            uploaded_file = request.FILES.get('uploads')

            request.session['name_alumni']=name_alumni
            request.session['official_mail']=official_mail
            if uploaded_file:
                # Read the binary content of the uploaded file
                file_content = uploaded_file.read()

                # Create a new Alumni instance and set the attributes
                instance = Alumni1.objects.create(
                    name=name_alumni,
                    batch_studied=batch_studied,
                    currently_working=currently_working,
                    designation=designation,
                    official_mail=official_mail,
                    uploaded_file=file_content  # Save the binary content in the model field
                )

                # Return a success message
                response_data = {'message': 'Alumni information and file uploaded successfully'}
                return JsonResponse(response_data)
            else:
                response_data = {'error': 'No file was uploaded'}
                return JsonResponse(response_data, status=400)
    return render(request, '2nd.html')
def third(request):
    return render(request,'third.html')
def thirs(request):
    stake = request.session.get('stakeholder')
    if stake == 'student':
        if request.method == "POST":
            email = request.session.get('email')
            name = request.session.get('name')
            vision_option = request.POST.get('vision_option')
            if vision_option == 'current_vision':
                vision="The Department should continue with the current vision statement as written."
            elif vision_option == 'revised_vision': 
                vision=(request.POST.get('vision_goal'))
            entry=student1.objects.get(name=name,email=email)
            entry.vision=vision
            entry.save()
    if stake=="staff":
        if request.method == "POST":
            staff_name=request.session.get('staff_name')
            staff_email=request.session.get('staff_email')
            vision_option = request.POST.get('vision_option')
            if vision_option == 'current_vision':
                vision="The Department should continue with the current vision statement as written."
            elif vision_option == 'revised_vision': 
                vision=(request.POST.get('vision_goal'))
            entry=staff2.objects.get(staff_name=staff_name,staff_email=staff_email)
            entry.vision=vision
            entry.save()
    if stake=="parent":
        if request.method == "POST":
            parent_name=request.session.get('parent_name')
            sd=request.session.get('sd')
            vision_option = request.POST.get('vision_option')
            if vision_option == 'current_vision':
                vision="The Department should continue with the current vision statement as written."
            elif vision_option == 'revised_vision': 
                vision=(request.POST.get('vision_goal'))
            entry=parent1.objects.get(parent_name=parent_name,sd=sd)
            entry.vision=vision
            entry.save()
    if stake=="industry":
        if request.method == "POST":
            name=request.session.get('indus_name')
            email=request.session.get('email')
            vision_option = request.POST.get('vision_option')
            if vision_option == 'current_vision':
                vision="The Department should continue with the current vision statement as written."
            elif vision_option == 'revised_vision': 
                vision=(request.POST.get('vision_goal'))
            entry=Industry1.objects.get(name=name,email=email)
            entry.vision=vision
            entry.save()
    if stake=="academician":
        if request.method == "POST":
            name=request.session.get('name_c')
            email=request.session.get('id_mail')
            vision_option = request.POST.get('vision_option')
            if vision_option == 'current_vision':
                vision="The Department should continue with the current vision statement as written."
            elif vision_option == 'revised_vision': 
                vision=(request.POST.get('vision_goal'))
            entry=Academician1.objects.get(name=name,official_mail=email)
            entry.vision=vision
            entry.save()
    if stake=="alumni":
        if request.method == "POST":
            name=request.session.get('name_alumni')
            email=request.session.get('official_mail')
            vision_option = request.POST.get('vision_option')
            if vision_option == 'current_vision':
                vision="The Department should continue with the current vision statement as written."
            elif vision_option == 'revised_vision': 
                vision=(request.POST.get('vision_goal'))
            entry=Alumni1.objects.get(name=name,official_mail=email)
            entry.vision=vision
            entry.save()
    return render(request, 'fouth.html')
def fourth(request):
    stake = request.session.get('stakeholder')
    if stake == 'student':
        if request.method == "POST":
            email = request.session.get('email')
            name = request.session.get('name')
            vision_option = request.POST.get('mission_option')
            if vision_option == 'current_mission':
                vision="The Department should continue with the current mission statement as written."
            elif vision_option == 'revised_mission': 
                vision=(request.POST.get('mission_goal'))
            entry=student1.objects.get(name=name,email=email)
            entry.mission=vision
            entry.save()
    if stake=="staff":
        if request.method == "POST":
            staff_name=request.session.get('staff_name')
            staff_email=request.session.get('staff_email')
            vision_option = request.POST.get('mission_option')
            if vision_option == 'current_mission':
                vision="The Department should continue with the current mission statement as written."
            elif vision_option == 'revised_mission': 
                vision=(request.POST.get('mission_goal'))
            entry=staff2.objects.get(staff_name=staff_name,staff_email=staff_email)
            entry.mission=vision
            entry.save()
    if stake=="parent":
        if request.method == "POST":
            parent_name=request.session.get('parent_name')
            sd=request.session.get('sd')
            vision_option = request.POST.get('mission_option')
            if vision_option == 'current_mission':
                vision="The Department should continue with the current mission statement as written."
            elif vision_option == 'revised_vision': 
                vision=(request.POST.get('mission_goal'))
            entry=parent1.objects.get(parent_name=parent_name,sd=sd)
            entry.mission=vision
            entry.save()
    if stake=="industry":
        if request.method == "POST":
            name=request.session.get('indus_name')
            email=request.session.get('email')
            vision_option = request.POST.get('mission_option')
            if vision_option == 'current_mission':
                vision="The Department should continue with the current mission statement as written."
            elif vision_option == 'revised_mission': 
                vision=(request.POST.get('mission_goal'))
            entry=Industry1.objects.get(name=name,email=email)
            entry.mission=vision
            entry.save()
    if stake=="academician":
        if request.method == "POST":
            name=request.session.get('name_c')
            email=request.session.get('id_mail')
            vision_option = request.POST.get('mission_option')
            if vision_option == 'current_mission':
                vision="The Department should continue with the current mission statement as written."
            elif vision_option == 'revised_mission': 
                vision=(request.POST.get('mission_goal'))
            entry=Academician1.objects.get(name=name,official_mail=email)
            entry.mission=vision
            entry.save()
    if stake=="alumni":
        if request.method == "POST":
            name=request.session.get('name_alumni')
            email=request.session.get('official_mail')
            vision_option = request.POST.get('mission_option')
            if vision_option == 'current_mission':
                vision="The Department should continue with the current mission statement as written."
            elif vision_option == 'revised_mission': 
                vision=(request.POST.get('mission_goal'))
            entry=Alumni1.objects.get(name=name,official_mail=email)
            entry.mission=vision
            entry.save()
    return render(request, 'fifth.html')
def fifth(request):
    stake = request.session.get('stakeholder')
    if stake == 'student':
        if request.method == "POST":
            email = request.session.get('email')
            name = request.session.get('name')
            vision_option = request.POST.get('mission_option')
            if vision_option == 'current_mission':
                vision="The Department should continue with the current PEOs statement as written."
            elif vision_option == 'revised_mission': 
                vision=(request.POST.get('mission_goal'))
            entry=student1.objects.get(name=name,email=email)
            entry.peo=vision
            entry.save()
    if stake=="staff":
        if request.method == "POST":
            staff_name=request.session.get('staff_name')
            staff_email=request.session.get('staff_email')
            vision_option = request.POST.get('mission_option')
            if vision_option == 'current_mission':
                vision="The Department should continue with the current PEOs statement as written."
            elif vision_option == 'revised_mission': 
                vision=(request.POST.get('mission_goal'))
            entry=staff2.objects.get(staff_name=staff_name,staff_email=staff_email)
            entry.peo=vision
            entry.save()
    if stake=="parent":
        if request.method == "POST":
            parent_name=request.session.get('parent_name')
            sd=request.session.get('sd')
            vision_option = request.POST.get('mission_option')
            if vision_option == 'current_mission':
                vision="The Department should continue with the current PEOs statement as written."
            elif vision_option == 'revised_vision': 
                vision=(request.POST.get('mission_goal'))
            entry=parent1.objects.get(parent_name=parent_name,sd=sd)
            entry.peo=vision
            entry.save()
    if stake=="industry":
        if request.method == "POST":
            name=request.session.get('indus_name')
            email=request.session.get('email')
            vision_option = request.POST.get('mission_option')
            if vision_option == 'current_mission':
                vision="The Department should continue with the current PEOs statement as written."
            elif vision_option == 'revised_mission': 
                vision=(request.POST.get('mission_goal'))
            entry=Industry1.objects.get(name=name,email=email)
            entry.peo=vision
            entry.save()
            
    if stake=="academician":
        if request.method == "POST":
            name=request.session.get('name_c')
            email=request.session.get('id_mail')
            vision_option = request.POST.get('mission_option')
            if vision_option == 'current_mission':
                vision="The Department should continue with the current PEOs statement as written."
            elif vision_option == 'revised_mission': 
                vision=(request.POST.get('mission_goal'))
            entry=Academician1.objects.get(name=name,official_mail=email)
            entry.peo=vision
            entry.save()
    if stake=="alumni":
        if request.method == "POST":
            name=request.session.get('name_alumni')
            email=request.session.get('official_mail')
            vision_option = request.POST.get('mission_option')
            if vision_option == 'current_mission':
                vision="The Department should continue with the current PEOS statement as written."
            elif vision_option == 'revised_mission': 
                vision=(request.POST.get('mission_goal'))
            entry=Alumni1.objects.get(name=name,official_mail=email)
            entry.peo=vision
            entry.save()
    return render(request, 'sixth.html')
def sixth(request):
    stake = request.session.get('stakeholder')
    if stake == 'student':
        if request.method == "POST":
            email = request.session.get('email')
            name = request.session.get('name')
            vision_option = request.POST.get('mission_option')
            if vision_option == 'current_mission':
                vision="The Department should continue with the current PSOs statement as written."
            elif vision_option == 'revised_mission': 
                vision=(request.POST.get('mission_goal'))
            entry=student1.objects.get(name=name,email=email)
            entry.pos=vision
            entry.save()
    if stake=="staff":
        if request.method == "POST":
            staff_name=request.session.get('staff_name')
            staff_email=request.session.get('staff_email')
            vision_option = request.POST.get('mission_option')
            if vision_option == 'current_mission':
                vision="The Department should continue with the current PSOs statement as written."
            elif vision_option == 'revised_mission': 
                vision=(request.POST.get('mission_goal'))
            entry=staff2.objects.get(staff_name=staff_name,staff_email=staff_email)
            entry.pos=vision
            entry.save()
    if stake=="parent":
        if request.method == "POST":
            parent_name=request.session.get('parent_name')
            sd=request.session.get('sd')
            vision_option = request.POST.get('mission_option')
            if vision_option == 'current_mission':
                vision="The Department should continue with the current PSOs statement as written."
            elif vision_option == 'revised_vision': 
                vision=(request.POST.get('mission_goal'))
            entry=parent1.objects.get(parent_name=parent_name,sd=sd)
            entry.pos=vision
            entry.save()
    if stake=="industry":
        if request.method == "POST":
            name=request.session.get('indus_name')
            email=request.session.get('email')
            vision_option = request.POST.get('mission_option')
            if vision_option == 'current_mission':
                vision="The Department should continue with the current PSOs statement as written."
            elif vision_option == 'revised_mission': 
                vision=(request.POST.get('mission_goal'))
            entry=Industry1.objects.get(name=name,email=email)
            entry.pos=vision
            entry.save()
    if stake=="academician":
        if request.method == "POST":
            name=request.session.get('name_c')
            email=request.session.get('id_mail')
            vision_option = request.POST.get('mission_option')
            if vision_option == 'current_mission':
                vision="The Department should continue with the current PSOs statement as written."
            elif vision_option == 'revised_mission': 
                vision=(request.POST.get('mission_goal'))
            entry=Academician1.objects.get(name=name,official_mail=email)
            entry.pos=vision
            entry.save()
    if stake=="alumni":
        if request.method == "POST":
            name=request.session.get('name_alumni')
            email=request.session.get('official_mail')
            vision_option = request.POST.get('mission_option')
            if vision_option == 'current_mission':
                vision="The Department should continue with the current PSOs statement as written."
            elif vision_option == 'revised_mission': 
                vision=(request.POST.get('mission_goal'))
            entry=Alumni1.objects.get(name=name,official_mail=email)
            entry.pos=vision
            entry.save()
    return render(request, 'seventh.html')
