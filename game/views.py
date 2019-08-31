from django.shortcuts import render,redirect
from person.models import Case, UserProfile
from django.http import HttpResponse
from django.contrib.auth.models import User

def play(request):
	print("yes")
	user=UserProfile.objects.filter(user_name=request.user).first()
	if user.num < 8:	
		case = Case.objects.filter(id=user.num).first()
		if user.num == 1 and user.form_submit == False:
			user.result = []
			user.save()

		if case is None:
			return redirect('/result')
		#case.num += 1
		context = {'Copy':case.Copy_1,'Cheat':case.Cheat_2,'Coop':case.Coop_3,'Detect':case.Detective_4,'Grudge':case.Grudger_7,'CopyKit':case.CopyKit_5,'Simple':case.Simp_6,'Random':case.Random_7}
	else:
		context = {}
	if user.num >= 1 and user.num < 8:
		return render(request,'game/index.html',context)
	elif user.num == 8 or user.num == 9:
		return render(request,'game/question.html',{'num':user.num})
	else:
		return render(request,'game/thank.html',context)

def result(request):

	solutions = {
		1:"COPYCAT:1, DETECTIVE: 10,  COOPERATE :4, ALL CHEAT:10   NO OF ROUNDS PER MATCH: 4   In the first round of the first match detective,cooperate and copy cat will have same score (18) as all of have same moves and all cheat will exploit every other character gaining a total of 15X3=45.   Second round: Now cooperates will get exploited by all cheats as well as detectives(2nd move is cheat) reducing its score by 20 points. A Cooperate gets 4X2 =8 points by cooperating by other three cooperates and a copy cat. Total=6    Now all cheat can exploit only cooperates incrementing its score by 4X3=12 making it 57. Detective gets 5X3 =15 points by cheating with copy cat and cooperates. Copy cat gets 4X2=8 points from cooperates and (-1)X10 from detectives making it a total of 16.  Inspecting further rounds we notice that cooperates are the least scorers and thus will get eliminated first.  The scenario will be the same when no of rounds is less. Therefore, making the result as:    All cheat>copycat>detective>cooperate.",
		2:"Always Cheat = 10, Always Cooperate = 4, Detective = 10, Copycat = 4. If number of rounds > 6 (=30) The winner in this case is = Copycat > Detective > Always Cheat > Cooperate. Explanation:  For rounds > 4, Cooperate and Detective behave similarly. So, we need to consider rounds < 4. If we have 4 Cooperates, then the copycats will be able to exploit them less than Detectives. That’s because for the remaining of the 26 moves will make them gain +3 against the copycats earning +2 from the always cooperates. After the round 1, 3 Always cooperates will get removed. So, with the remaining 1 Always Cooperate, the extent of exploitation begins to fall for Detectives. Also, now the first 4 moves of the Detective begin to take importance, that is Co Ch Co Co, which make them vulnerable to Always Cheats. And, thus their points start falling. In the next move, 2 always cheats are removed, and 1 Always Cooperate is also removed. Next onwards Copycat begins to Dominate. Thus making it the winner for larger cases.",
		3:"Grudger 9, Cheater: 9 , Cooperator: 7 No of rounds per match: 10  Payoffs: default.  After the first match, cooperator is exploited the most and hence three of them are eliminated leading to increase in the no of grudgers. Decrease in no of cooperators reduce the points gain of cheaters whereas mutual cooperation between cooperators and grudgers increases the points of cooperators at a significant rate making the result of the given case as:  Grudger> Cooperator>Cheater",
		4:"Let’s have some maths  Given number of rounds =10, and the guys being Always Cheat, Grudger, and Copycats. Eliminate 1 guy per match. We need to find the minimum sum of Copycats and grudgers such that the system gradually stabilises.  Students need to figure out that grugers and copycats eventually behave same after 1st move. So let’s conider x guys and 25-x guys will be always cheat. Now, mathematically, if always cheat must lose then, 3x < -(25-x) + (x-1)*2 + 9(x-1)*2  X > 45/18;  And the least possible x will be 3. Thus 2 answers : 1 CP 2 Grudger  2 Grudger 1 CP…",
		5:"Copy cat:1 Simpleton: 3, detective 15, copykitten: 6  1st step of all the characters is same, thus everyone has a score of 48.   2nd step benefits detective allowing it to take lead. In the next round copycat and simpleton cheats exploiting detective . In further rounds copykitten is the least scorer. Detective becomes cheater for simpleton and copycat after his 1st four steps. Simpleton gets alternate -1 points on its move making it the second least scorer.Copy cat keep getting points from simpleton hence leading. Copy cat>Detective>Simpleton>Copy Kitten ",
		6:"Not applicable",
		7:"Not applicable",
		8:"Students need to figure out that Grugers and Copycats eventually behave same after 1st move. So let’s conider x guys and 25-x guys will be always cheat.  Now, mathematically, if always cheat must lose then 3x < -(25-x) + (x-1)*2 + 9(x-1)*2  X > 45/18; And the least possible x will be 3. Thus 2 answers : <strong>1.CP 2.Grudger</strong>",
		9:"Hit and Trial",
	};

	user_ = UserProfile.objects.get(user_name=request.user)
	if user_.num < 8:
		case = Case.objects.filter(id = user_.num).first()
		print(user_.result)
		
		a = {'Copycat':1,'All_cheat':2,'All_cooperate':3,'Detective':4,'Grudger':5,'CopyKitten':6,'Simple':7,'Random':8}
		C1 = list(a.keys())[list(a.values()).index(int(case.Pref_1_ans))]
		C2 = list(a.keys())[list(a.values()).index(int(case.Pref_2_ans))]
		C3 = list(a.keys())[list(a.values()).index(int(case.Pref_3_ans))]
		C4 = list(a.keys())[list(a.values()).index(int(case.Pref_4_ans))]

		ans = {1:'Copycat',2:'All_cheat',3:'All_cooperate',4:'Detective',5:'Grudger',6:'CopyKitten',7:'Simple',8:'Random'}

		C = {1:C1,2:C2,3:C3,4:C4}

		sorted_x = sorted((user_.prefs).items(), key=lambda kv: kv[1])
		list_pref_sent = []
		for x in sorted_x:
			list_pref_sent.append(x[0])

		list_ans = []
		list_ans.append(ans[case.Pref_1_ans])
		list_ans.append(ans[case.Pref_2_ans])
		list_ans.append(ans[case.Pref_3_ans])
		list_ans.append(ans[case.Pref_4_ans])
		print(user_.form_submit)
		return render(request,'game/result.html',{'id': user_.num,'Score': user_.Score, 'case':list_ans, 'prefs': list_pref_sent,'solutions' : solutions[user_.num]})
	else:
 		print(user_.num)
 		return render(request,'game/result.html',{'id': user_.num,'Score': user_.Score,'solutions' : solutions[user_.num]})
 		
def postresult(request):
	user_ = UserProfile.objects.get(user_name=request.user)

	if request.method == "POST":
		marks = 0 
		case = Case.objects.filter(id=user_.num).first()

		a = {'Copycat':1,'All_cheat':2,'All_cooperate':3,'Detective':4,'Grudger':5,'CopyKitten':6,'Simple':7,'Random':8}
		C1 = list(a.keys())[list(a.values()).index(int(case.Pref_1_ans))]
		C2 = list(a.keys())[list(a.values()).index(int(case.Pref_2_ans))]
		C3 = list(a.keys())[list(a.values()).index(int(case.Pref_3_ans))]
		C4 = list(a.keys())[list(a.values()).index(int(case.Pref_4_ans))]

		ans = {1:'Copycat',2:'All_cheat',3:'All_cooperate',4:'Detective',5:'Grudger',6:'CopyKitten',7:'Simple',8:'Random'}

		C = {1:C1,2:C2,3:C3,4:C4}

		Copycat = request.POST['Pref_1']
		All_cheat = request.POST['Pref_2']
		All_cooperate = request.POST['Pref_3']
		Detective = request.POST['Pref_4']
		Grudger = request.POST['Pref_5']
		CopyKitten = request.POST['Pref_6']
		Simple = request.POST['Pref_7']
		Random = request.POST['Pref_8']

		p = {'Copycat':Copycat,'All_cheat':All_cheat,'All_cooperate':All_cooperate,'Detective':Detective,'Grudger':Grudger,'CopyKitten':CopyKitten,'Simple':Simple,'Random':Random}
	

		for key in list(p.keys()):
			if p[key] == '0':
				p.pop(key)

		if str(a[list(p.keys())[list(p.values()).index('1')]]) == str(case.Pref_1_ans):
			marks += 4
		if str(a[list(p.keys())[list(p.values()).index('2')]]) == str(case.Pref_2_ans):
			marks += 4
		if str(a[list(p.keys())[list(p.values()).index('3')]]) == str(case.Pref_3_ans):
			marks += 4
		if str(a[list(p.keys())[list(p.values()).index('4')]]) == str(case.Pref_4_ans):
			marks += 4

		
		user_.result.append([marks])
		
		print(user_.result)
		user_.Score += marks
		# user_.num += 1
		user_.prefs = p
		user_.form_submit = True
		print(user_.result)
		user_.save()
		score = user_.Score
	return redirect('/play')

def proceed(request):
	user_ = UserProfile.objects.get(user_name=request.user)
	user_.num += 1
	user_.form_submit = False
	user_.save()

	return render(request,'game/proceed.html')

def postanswer(request):
	user_ = UserProfile.objects.get(user_name=request.user)

	if request.method == 'POST':
		correct_an=[3,4]
		ans=int(request.POST['Ans'])
		if ans==correct_an[user_.num - 8]:
			marks=10
		user_.result.append(marks)
		user_.Score += marks
		user_.save()
	return redirect('/play') 

def quesproceed(request):
	user_ = UserProfile.objects.get(user_name = request.user)
	user_.num+=1
	user_.save()

	return render(request,'game/quesproceed.html')

def play_words(request):
	return render(request,'game/words.html')


def modal(request):
	return render(request,'game/modal.html')

# def dbupdate(request):

# 	user_ = User.objects.all()
# 	for one in user_:
# 		one.is_staff = True
# 		one.save()
# 	return HttpResponse()

