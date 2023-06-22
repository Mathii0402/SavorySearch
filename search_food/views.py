from django.shortcuts import render
import pandas as pd
from .models import hotel

def search(request):
    if 'q' in request.GET:
        query = request.GET.get('q')
        hotels = find_hotels(query)
    else:
        hotels = []

    return render(request, 'home.html', {'hotels': hotels})

def find_hotels(query):  


    # Searching directly using the given excel file
    hotels = []
        # df = pd.read_csv('https://python-exercise.s3.ap-south-1.amazonaws.com/restaurants_small.csv')
        # filtered_df = df[df['items'].str.contains(query, case=False)]      # Filter the dataset based on the dish name
        # hotels = filtered_df['name'].tolist()
        # return hotels
    

    #Searching the excell data which is uploaded to the database and apllying filters
    queryset = hotel.objects.values_list('name','items')    #getting only 2 necessary columns
    for q in queryset:
        if query.lower() in q[1].lower():                   #checking query matches or not
            hotels.append(q[0])
    return hotels[:5]                                       #returning top 5

