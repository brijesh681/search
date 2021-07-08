from django.shortcuts import render , redirect
from django import forms
import markdown2
import re
import random
from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

#rendering page content for a title
def wiki(request , title):
	titles=util.list_entries()

	if title in titles:
		content = util.get_entry(title)
		return render(request , "encyclopedia/wiki.html",{
			"title":title,
			"content":markdown2.markdown(content) #Convert Markdown contetn in HTML
			})
	else:
		return render(request, "encyclopedia/error.html",{
			"error_message":" requested page was not found."
			})

# for search Bar
def search(request):
	if request.method == 'POST':
		search_text = request.POST
		search_text = search_text['q']
		search_list = []
		titles = util.list_entries()

		for title in titles:
			if re.search(search_text.lower(),title.lower()):
				search_list.append(title)
		if len(search_list)==0:
			 # searchlist is empty
			 return render(request, "encyclopedia/error.html", {
			 	"error_message":f" No result found for {search_text}"
			 	})

	return render(request, "encyclopedia/search.html", {
		"entries":search_list
		})

# for creating new page
def new_page(request):
	titles=util.list_entries()
	if request.method=='POST':
		title=request.POST.get('title')
		content=request.POST.get('content')

		if title in titles:
			return render(request, "encyclopedia/createPage.html",{
			"available":True
			}) 
		else:
			util.save_entry(title,content)
			return redirect(wiki , title=title)
	return render(request , "encyclopedia/createPage.html",{
		"available":False
		})

# for edit page
def edit_page(request , title):
	content = util.get_entry(title)
	if request.method=='GET':
		return render(request, "encyclopedia/editPage.html",{
			"title":title,
			"content":content
			})
	if request.method=='POST':
		content = request.POST.get('editcontent')
		util.save_entry(title,content)
		return redirect(wiki, title=title)

# for random page search
def random_page(request):
	titles = util.list_entries()
	title = random.choice(titles)

	return redirect(wiki , title=title) #redirect to random page.





