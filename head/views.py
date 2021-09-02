from django.shortcuts import render, get_object_or_404, redirect

from django.http import Http404
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from django.contrib.auth.models import User
from . import twitterdata , clean
import pickle 
from xgboost import XGBClassifier

# model = XGBClassifier()
# model.load_model("xgb_model.json")
tfidf = pickle.load(open("tfidf1.pkl","rb"))

# Create your views here.
def homeView(request):
	context = {"data":""}
	if request.method == "POST":
		userid = request.POST.get("userid")
		print(userid)
		try: 
			info = twitterdata.get_data(userid)
			clean_text = clean.clean(" ".join(info[1]))
			print("\n",clean_text)
			context = {"data" : clean_text,
						"count" : info[0]}
			corpus = tfidf.transform([clean_text])
			print(corpus)
			return render(request,'home.html',context)
		except:
			context = {"data":"Invalid user id"}
	return render(request,'home.html',context)

def startquizView(request):
	return render(request,'startquiz.html',{})