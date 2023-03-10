from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Leaguerank

import pandas as pd
import sqlite3
from pathlib import Path

class leaguerankBaseView(View):
    model = Leaguerank
    fields = '__all__'
    success_url = reverse_lazy('leaguerank:all')

class leaguerankListView(leaguerankBaseView, ListView):
    """View to list all leagueranks.
    Use the 'leaguerank_list' variable in the template
    to access all leaguerank objects"""

class leaguerankDetailView(leaguerankBaseView, DetailView):
    """View to list the details from one leaguerank.
    Use the 'leaguerank' variable in the template to access
    the specific leaguerank here and in the Views below"""

class leaguerankCreateView(leaguerankBaseView, CreateView):
    """View to create a new leaguerank"""

class leaguerankUpdateView(leaguerankBaseView, UpdateView):
    """View to update a leaguerank"""

class leaguerankDeleteView(leaguerankBaseView, DeleteView):
    """View to delete a leaguerank"""

def upload_csv(request):
    #conn =
    BASE_DIR = Path(__file__).resolve().parent.parent
    db = BASE_DIR /'db.sqlite3'
    dbName = BASE_DIR /'db.sqlite3'

    conn = sqlite3.connect(db)

    if "GET" == request.method:
        return render(request, "myapp/upload_csv.html", data)
    elif "POST"== request.method:
        print('csv posted')
        #print(request.FILES)
        csv_file = request.FILES['myfile']
        #print(csv_file)
        df = pd.read_csv(csv_file, header=None)
        #print(df)
        matchResult = []
        db_id = 0

        #print(df.shape)
        for rows in df:
            #print(rows)
            print(df.loc[rows])
            print('team1 score ->', df.loc[rows][3])
            if(df.iloc[rows][3] > df.iloc[rows][1]):
                matchResult.append({"id": db_id, "name": df.iloc[rows][2], "points":  df.iloc[rows][3] , "ranking":rows })
            else:
                matchResult.append({"id": db_id,"name": df.iloc[rows][0], "points":  df.iloc[rows][1], "ranking":rows })
            db_id = db_id + 1
        #print(matchResult)

        df2 = pd.DataFrame(matchResult)
        df2 = df2.sort_values(by='points',ascending=False )
        #df2['ranking'] = range( len(df2) -1 , -1,-1)
        df2['ranking'] = range( 1 ,  len(df2) +1  ,1)
        #print(df2)

        df2.to_sql('leaguerank_leaguerank', conn, if_exists='replace', index = False)




        return HttpResponseRedirect(reverse("leaguerank:all"))
