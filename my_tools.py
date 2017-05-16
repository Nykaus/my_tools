import sublime
import sublime_plugin
import os
import re
import webbrowser

#ctrl+alt+g selection un url
class FrToEnCommand(sublime_plugin.TextCommand):
	def run(self,edit):
		tabRegion=self.view.sel()
		for laRegion in tabRegion:
			laRecherche=self.view.substr(laRegion).replace(" ","+")
			checkUrl="https://translate.google.fr/?hl=fr#fr/en/"+laRecherche
			webbrowser.open(checkUrl)#ctrl+alt+g selection un url


			
#ctrl+alt+g selection un url
class EnToFrCommand(sublime_plugin.TextCommand):
	def run(self,edit):
		tabRegion=self.view.sel()
		for laRegion in tabRegion:
			laRecherche=self.view.substr(laRegion).replace(" ","+")
			checkUrl="https://translate.google.fr/?hl=en#en/fr/"+laRecherche
			webbrowser.open(checkUrl)#ctrl+alt+g selection un url


#ctrl+alt+c	
class NumerotationCommand(sublime_plugin.TextCommand): 
	def run(self, edit): 
		tabRegion=self.view.sel()	 
		compteur=1		 
		for laRegion in tabRegion: 
			self.view.replace(edit,laRegion,str(compteur))
			compteur=compteur+1

#ctrl+alt+v	
class ClearConsoleCommand(sublime_plugin.ApplicationCommand):
	def run(self):
		print('\n' * 50)

#ctrl+alt+space selection 2 region
class SwitchCommand(sublime_plugin.TextCommand):
	def run(self , edit):
		tabRegion=self.view.sel()	
		tabContent=[self.view.substr(tabRegion[0]),self.view.substr(tabRegion[1])]
		self.view.replace(edit, tabRegion[0], tabContent[1])
		self.view.replace(edit, tabRegion[1], tabContent[0])

#ctrl+alt+keypad_plus
class PlusOneCommand(sublime_plugin.TextCommand):
	def run(self,edit):
		tabRegion=self.view.sel()
		for laRegion in tabRegion:
			numRegion=int(self.view.substr(laRegion))+1
			self.view.replace(edit, laRegion,str(numRegion))

#ctrl+alt+keypad_minus
class MinusOneCommand(sublime_plugin.TextCommand):
	def run(self,edit):
		tabRegion=self.view.sel()
		for laRegion in tabRegion:
			numRegion=int(self.view.substr(laRegion))-1
			self.view.replace(edit, laRegion,str(numRegion))

#ctrl+alt+f
class GetPathCommand(sublime_plugin.TextCommand):
	def run(self , edit):		
		tabRegion=self.view.sel()	
		self.view.replace(edit, tabRegion[0], str(self.view.file_name()))

#ctrl+alt+x
class StampHeureCommand(sublime_plugin.TextCommand):
	def run(self,edit):
		tabRegion=self.view.sel()
		laRegion = tabRegion[-1]
		self.view.sel().clear()
		self.view.sel().add(laRegion)
		self.view.show(laRegion)
		from datetime import datetime
		FMT = '%H:%M'
		self.view.replace(edit, laRegion,str(datetime.now().strftime(FMT)))
		print(laRegion)

#ctrl+alt+keypad_divide
class DiffHeureCommand(sublime_plugin.TextCommand):
	def run(self,edit):
		#recuperation des selections faites sur l'editeur
		from datetime import datetime
		FMT = '%H:%M'
		
		tabRegion=self.view.sel()
		for laRegion in tabRegion:	
			Selection=self.view.substr(laRegion);
			Resultat=Selection.replace(" ","").split("-",2)
			tdelta = datetime.strptime(Resultat[1], FMT) - datetime.strptime(Resultat[0], FMT)
			Res=str(tdelta).replace("-1 day, ","").split(":",2)	
			self.view.replace(edit, laRegion,Res[0]+":"+Res[1]+"\t"+str(Selection))

#ctrl+alt+keypad_multiply
class SumHeureCommand(sublime_plugin.TextCommand):
	def run(self,edit):
		#recuperation des selections faites sur l'editeur
		tabRegion=self.view.sel()
		sumMinute=0
		sumHours=0
		cpt=0
		for laRegion in tabRegion:				
			Selection=self.view.substr(laRegion);
			select=Selection.split(":",2)
			sumMinute+=int(select[1])
			sumHours+=int(select[0])
			if sumMinute>=60:
				sumMinute=sumMinute-60
				sumHours+=1
			if cpt==0:
				self.view.replace(edit, laRegion,"\t\t"+str(Selection))
			else:
				self.view.replace(edit, laRegion,"= "+str(sumHours)+":"+str(sumMinute)+"\t"+str(Selection))
			cpt+=1

#ctrl+alt+s  
class MergeMultiSelectionCommand(sublime_plugin.TextCommand): 
	def run(self, edit):
		tabRegion=self.view.sel()
		laRegion = tabRegion[-1]
		self.view.sel().clear()
		self.view.sel().add(laRegion)
		self.view.show(laRegion)

#ctrl+alt+s
class GetCalendarCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		from math import floor
		from math import ceil
		from datetime import datetime
		import calendar

		arrMonthFr=["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Août","Septembre","Octobre","Novembre","Décembre"]
		
		tabRegion=self.view.sel()

		for laRegion in tabRegion:
			espaceTitreTotal = 36
			calendarFormat="------------------------------------\n|%_space1_%%_mois_annee_%%_space2_%|\n------------------------------------\n| Lu | Ma | Me | Je | Ve | Sa | Di |\n------------------------------------\n"
			Selection=self.view.substr(laRegion);

			cal = calendar.Calendar()

			Resultat=[]
			# verifier si il y a une selection du type M-AAAA
			if re.match(r"[0-9]{1,2}-[0-9]{4}", Selection): 
				Resultat=Selection.replace(" ","").split("-",2)			
				arrCalendar = cal.monthdayscalendar(int(Resultat[1]), int(Resultat[0]))	
				Resultat[0]=arrMonthFr[int(Resultat[0])-1]
			else:
				objDate = datetime.now()
				arrCalendar = cal.monthdayscalendar(objDate.year, objDate.month)		
				Resultat=[arrMonthFr[objDate.month-1]]
				Resultat+=[objDate.year]

			# Mettre les jours sur chaque ligne
			tabCalendar = ""
			for rowCalendar in arrCalendar:
				for dateCalendar in rowCalendar:
					# si le jour n'apartien pas au mois mettre vide
					if dateCalendar==0:
						tabCalendar+="     "
						continue
					if dateCalendar<=9:
						tabCalendar+="| 0"+str(dateCalendar)+" "
					else:
						tabCalendar+="| "+str(dateCalendar)+" "
				tabCalendar+="|\n------------------------------------\n"

			# Preparation du titre le mois puis l'annee
			titreMoisAnnée = str(Resultat[0])+" "+str(Resultat[1])
			espaceVideTotal= espaceTitreTotal- len(titreMoisAnnée)

			# calcul des espaces pour le titre
			espaceVide1=""
			espaceVide2=""
			for i in range(1,floor(espaceVideTotal/2)):
				espaceVide1+=" "
			for i in range(1,ceil(espaceVideTotal/2)):
				espaceVide2+=" "
			
			#creation du titre du table
			calendarFormat = calendarFormat.replace("%_mois_annee_%",titreMoisAnnée)
			calendarFormat = calendarFormat.replace("%_space1_%",espaceVide1)
			calendarFormat = calendarFormat.replace("%_space2_%",espaceVide2)

			#Afficher le tableau a la place de la selection
			self.view.replace(edit, laRegion,calendarFormat+tabCalendar)		

		# arreter la selection du tableau et le pointer le curseur a la fin
		rowRegion = self.view.rowcol(tabRegion[-1].b)[0]		
		pointEnd = self.view.text_point(rowRegion, 0)			
		self.view.sel().clear()		
		self.view.sel().add(pointEnd)
		self.view.show(pointEnd)

#ctrl+alt+q
#TODO a  ameliorer test pour recuperer tous les fichiers dans plusieurs dossier
class GetFileCommand(sublime_plugin.TextCommand):
	def run(self , edit):
		tabRegion=self.view.sel()
		folder_path = self.view.substr(tabRegion[0])
		filesname="Liste des fichiers:\n"+folder_path+"\n\n"
		for path, dirs, files in os.walk(folder_path):
		    for filename in files:
		    	filesname=filesname+"\n"+filename
			
		self.view.replace(edit, tabRegion[0], filesname)

