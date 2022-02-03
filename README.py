from requests import get
from re import findall
from rubika import Bot
import time

bot = Bot("gohtpqqdpzivgcjlcqfdbzmeqvmxxcdo")
target = "g0B2OdK02cde2ac53eaf293172698adb"
answered = [bot.getGroupAdmins]
retries = {}
sleeped = False
# delmess = ["دولی","کصکش","کون","کص","کیر" ,"خر","کستی","دول","گو","کس","کسکش","کوبص"]
plus= True

while True:
	try:
		admins = [i["member_guid"] for i in bot.getGroupAdmins(target)["data"]["in_chat_members"]]
		min_id = bot.getGroupInfo(target)["data"]["chat"]["last_message_id"]
		while True:
			try:
				messages = bot.getMessages(target,min_id)
				break
			except:
				continue
		
		open("id.db","w").write(str(messages[-1].get("message_id")))

		for msg in messages:
			if msg["type"]=="Text" and not msg.get("message_id") in answered:
				if not sleeped:
					if msg.get("text") == "بات" and msg.get("author_object_guid") in admins :
						bot.sendMessage(target, "ربات ندیده ای اینقد میگی بات😐", message_id=msg.get("message_id"))

		for msg in messages:
			if msg["type"]=="Text" and not msg.get("message_id") in answered:
				if not sleeped:
					if msg.get("text") == "آنلاینی" and msg.get("author_object_guid") in admins :
						bot.sendMessage(target, "آره عشقم فعالم😉❤", message_id=msg.get("message_id"))

					elif "forwarded_from" in msg.keys() and bot.getMessagesInfo(target, [msg.get("message_id")])[0]["forwarded_from"]["type_from"] == "Channel" and not msg.get("author_object_guid") in admins :
						bot.deleteMessages(target, [str(msg.get("message_id"))])

					elif msg.get("text") == "اهل کجایی":
						bot.sendMessage(target, "هر جا که جانان میکشد", message_id=msg.get("message_id"))

					elif msg.get("text").startswith("add") :
						bot.invite(target, [bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["object_guid"]])
						bot.sendMessage(target, "کاربر به گپ اضافه شد ✅", message_id=msg.get("message_id"))

					elif msg.get("text") == "پیشی":
						bot.sendMessage(target, "ها چی میگی ", message_id=msg.get("message_id"))

					elif msg.get("text") == "😐😂":
						bot.sendMessage(target, "چیه پوکر و خنده میدی؟", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "خوبی":
						bot.sendMessage(target, "تو چطوری؟🤪", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "چه خبر":
						bot.sendMessage(target, "ســلامـتیت😍♥", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "چخبر":
						bot.sendMessage(target, "ســلامـتیت😍♥", message_id=msg.get("message_id"))
							
					elif msg.get("text") == "ربات":
						bot.sendMessage(target, "جــونـم😁💋", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "استغفرالله":
						bot.sendMessage(target, "توبه توبه", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "سبحان الله":
						bot.sendMessage(target, "😱😂", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "😂":
						bot.sendMessage(target, "😂😂", message_id=msg.get("message_id"))
							
					elif msg.get("text") == "😂😐":
						bot.sendMessage(target, "ها چیه ؟¿", message_id=msg.get("message_id"))

					elif msg.get("text") == "اسکل":
						bot.sendMessage(target, "بچه بیا پایین سرمون درد گرفت اه", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "زشت":
						bot.sendMessage(target, "جای تو رو تنگ کردم 😒", message_id=msg.get("message_id"))
												
					elif msg.get("text") == "سگ":
						bot.sendMessage(target, "فش نده ریم میشی", message_id=msg.get("message_id"))

					elif msg.get("text") == "گوه":
						bot.sendMessage(target, "بخور", message_id=msg.get("message_id"))

					elif msg.get("text") == "تست ":
						bot.sendMessage(target, "هنوز زنده ام", message_id=msg.get("message_id"))

					elif msg.get("text") == "سوری":
						bot.sendMessage(target, "چیکارم داری؟ 😑", message_id=msg.get("message_id"))

					elif msg.get("text") == "رلم میشی":
						bot.sendMessage(target, "نه 🤨", message_id=msg.get("message_id"))

					elif msg.get("text") == "بن":
						bot.sendMessage(target, "سید بن نمیکنم", message_id=msg.get("message_id"))

					elif msg.get("text") == "اه":
						bot.sendMessage(target, "برو توودستشویی بگو", message_id=msg.get("message_id"))

					elif msg.get("text") == "خبی":
						bot.sendMessage(target, "معلومه که خوبم فدات بشم من 😇", message_id=msg.get("message_id"))

					elif msg.get("text") == "سلام":
						bot.sendMessage(target, "های جیگر", message_id=msg.get("message_id"))

					elif msg.get("text") == "شکر":
						bot.sendMessage(target, "الحمدالله", message_id=msg.get("message_id"))

					elif msg.get("text") == "عشق منی":
						bot.sendMessage(target, "تو بیشتر عزیزم😍", message_id=msg.get("message_id"))

					elif msg.get("text") == "سوری چند سالته":
						bot.sendMessage(target, "25", message_id=msg.get("message_id"))

					elif msg.get("text") == "کجا ":
						bot.sendMessage(target, "نا کجا", message_id=msg.get("message_id"))

					elif msg.get("text") == "نخیر":
						bot.sendMessage(target, "نامرد", message_id=msg.get("message_id"))

					elif msg.get("text") == "چیشد":
						bot.sendMessage(target, "هعب😐💔،گوز هوا شد ", message_id=msg.get("message_id"))

					elif msg.get("text") == "اسمت چیه":
						bot.sendMessage(target, "عباس 😐", message_id=msg.get("message_id"))

					elif msg.get("text") == "اره/n":
						bot.sendMessage(target, "دقیقاحق باشماهست قربان", message_id=msg.get("message_id"))

					elif msg.get("text") == "ن":
						bot.sendMessage(target, "نکمه😕", message_id=msg.get("message_id"))

					elif msg.get("text") == "ربات/n":
						bot.sendMessage(target, "بگیر بخواب", message_id=msg.get("message_id"))

					elif msg.get("text") == "بات":
						bot.sendMessage(target, "بفرمایین 😊", message_id=msg.get("message_id"))

					elif msg.get("text") == "قوانین":
						bot.sendMessage(target, "خاک بر سرت قوانین ایران رو نپیدونی چیه", message_id=msg.get("message_id"))

					elif msg.get("text") == "طینز":
						bot.sendMessage(target, "عا", message_id=msg.get("message_id"))

					elif msg.get("text") == ".":
						bot.sendMessage(target, "روبیکا ریده؟", message_id=msg.get("message_id"))

					elif msg.get("text") == "اوکی":
						bot.sendMessage(target, "👌😉", message_id=msg.get("message_id"))

					elif msg.get("text") == "چند سالته":
						bot.sendMessage(target, "25", message_id=msg.get("message_id"))

					elif msg.get("text") == "سوری خر":
						bot.sendMessage(target, "عمته", message_id=msg.get("message_id"))

					elif msg.get("text") == "سلام":
						bot.sendMessage(target, "سلام خوبی", message_id=msg.get("message_id"))

					elif msg.get("text") == "😐":
						bot.sendMessage(target, "شاخ نشو", message_id=msg.get("message_id"))

					elif msg.get("text") == "💔":
						bot.sendMessage(target, "عع عع چی شد🤨", message_id=msg.get("message_id"))

					elif msg.get("text") == "تنهام":
						bot.sendMessage(target, "نمیدونم والا ☹️", message_id=msg.get("message_id"))

					elif msg.get("text") == "چی":
						bot.sendMessage(target, "بادام چی😗", message_id=msg.get("message_id"))

					elif msg.get("text") == "چی؟":
						bot.sendMessage(target, "بادام چی😗", message_id=msg.get("message_id"))

					elif msg.get("text") == "س":
						bot.sendMessage(target, "سلام خوبی", message_id=msg.get("message_id"))

					elif msg.get("text") == "ها":
						bot.sendMessage(target, "مرگِ ها 😐", message_id=msg.get("message_id"))

					elif msg.get("text") == "بای":
						bot.sendMessage(target, "فردا بخور های بای", message_id=msg.get("message_id"))

					elif msg.get("text") == "اها":
						bot.sendMessage(target, "خوبه فهمیدی داشتم نا امید میشدم😏", message_id=msg.get("message_id"))

					elif msg.get("text") == "خر":
						bot.sendMessage(target, "ادبت کو گوساله🗿", message_id=msg.get("message_id"))

					elif msg.get("text") == "چطوری":
						bot.sendMessage(target, "متوری", message_id=msg.get("message_id"))

					elif msg.get("text") == "سجاد":
						bot.sendMessage(target, "با سازنده پسر عموم چیکار داری", message_id=msg.get("message_id"))

					elif msg.get("text") == "معلون":
						bot.sendMessage(target, "تو معلولی🗿", message_id=msg.get("message_id"))

					elif msg.get("text") == "پی چک":
						bot.sendMessage(target, "با منی؟", message_id=msg.get("message_id"))

					elif msg.get("text") == "هعب😐💔":
						bot.sendMessage(target, "چیشد عشقم 💔", message_id=msg.get("message_id"))

					elif msg.get("text") == "خش😂":
						bot.sendMessage(target, "خوبی نفش 😂", message_id=msg.get("message_id"))

					elif msg.get("text") == "آها":
						bot.sendMessage(target, "خوبه فهمیدی داشتم نا امید میشدم😏", message_id=msg.get("message_id"))

					elif msg.get("text") == "چشم":
						bot.sendMessage(target, "بوس رو چشت", message_id=msg.get("message_id"))

					elif msg.get("text") == "خیلی خری":
						bot.sendMessage(target, "خریت از خودتونه 😁", message_id=msg.get("message_id"))

					elif msg.get("text") == "عا":
						bot.sendMessage(target, "باز چه مرگته؟", message_id=msg.get("message_id"))

					elif msg.get("text") == "نت ریده":
						bot.sendMessage(target, "به درک🗿", message_id=msg.get("message_id"))

					elif msg.get("text") == "جوون":
						bot.sendMessage(target, "فنجون", message_id=msg.get("message_id"))

					elif msg.get("text") == "جون":
						bot.sendMessage(target, "بادمجون این سه تا رو نرنجون", message_id=msg.get("message_id"))

					elif msg.get("text") == "چرا تحول نمیگیری":
						bot.sendMessage(target, "عزیزم مگه من سفارشت دادم که حالا بخام تحولیت بگرم ", message_id=msg.get("message_id"))

					elif msg.get("text") == "خوبم تو خوبی":
						bot.sendMessage(target, "اره ممنون خوبم", message_id=msg.get("message_id"))

					elif msg.get("text") == "برو بابا":
						bot.sendMessage(target, "نگو بابا،احساس مسئولیت میکنم", message_id=msg.get("message_id"))

					elif msg.get("text") == "گلابی":
						bot.sendMessage(target, "مامور مسترابی", message_id=msg.get("message_id"))

					elif msg.get("text") == "الو":
						bot.sendMessage(target, "اَی خِداااااا چته چکارم داری نمیزاری بخوابم", message_id=msg.get("message_id"))

					elif msg.get("text") == "سینا":
						bot.sendMessage(target, "بابا بیا این کارت داره", message_id=msg.get("message_id"))

					elif msg.get("text") == "اصل ":
						bot.sendMessage(target, "🗿", message_id=msg.get("message_id"))

					elif msg.get("text") == "والا":
						bot.sendMessage(target, "بمولا", message_id=msg.get("message_id"))

					elif msg.get("text") == "خدا وکیلی":
						bot.sendMessage(target, "خدا الان وکیل نیست قاضی", message_id=msg.get("message_id"))

					elif msg.get("text") == "زر نزن":
						bot.sendMessage(target, "تو بزن پولشو بگیر", message_id=msg.get("message_id"))

					elif msg.get("text") == "زر نزن":
						bot.sendMessage(target, "تو بزن", message_id=msg.get("message_id"))

					elif msg.get("text") == "نوب":
						bot.sendMessage(target, "میدونی چیه ؟", message_id=msg.get("message_id"))

					elif msg.get("text") == "شایان":
						bot.sendMessage(target, "چیکارش داری💔", message_id=msg.get("message_id"))

					elif msg.get("text") == "سید هوشمند":
						bot.sendMessage(target, "اسم شوهرمو به زبونت نیار 🗿", message_id=msg.get("message_id"))

					elif msg.get("text") == "خش":
						bot.sendMessage(target, "الحمدالله", message_id=msg.get("message_id"))

					elif msg.get("text") == "جــــر نخـوری😂🌹":
						bot.sendMessage(target, "تیکه بنداز بهش 🗿", message_id=msg.get("message_id"))

					elif msg.get("text") == "سلم/n":
						bot.sendMessage(target, "منم یاد بگیرم اینجوری سلام کنم😐", message_id=msg.get("message_id"))

					elif msg.get("text") == "جوووون":
						bot.sendMessage(target, "بادمجون سه تاشو بگیر نرنجون", message_id=msg.get("message_id"))

					elif msg.get("text") == "باشه":
						bot.sendMessage(target, "خب چه کنم🗿", message_id=msg.get("message_id"))

					elif msg.get("text") == "خیخی":
						bot.sendMessage(target, "ممد بیا بببن این چی میگه", message_id=msg.get("message_id"))

					elif msg.get("text") == "چجوری":
						bot.sendMessage(target, "اینجوری همینجوری ", message_id=msg.get("message_id"))

					elif msg.get("text") == "پیشی بات":
						bot.sendMessage(target, "چیه کره خر", message_id=msg.get("message_id"))

					elif msg.get("text") == "باش":
						bot.sendMessage(target, "افرین", message_id=msg.get("message_id"))

					elif msg.get("text") == "افرین":
						bot.sendMessage(target, "خواهش میکنم", message_id=msg.get("message_id"))

					elif msg.get("text") == "لیست":
						bot.sendMessage(target, "دستـــورات ربـات 🤖:\n\n●🤖انلاینی  : فعال یا غیر فعال بودن بات\n\n●❎خاموش : غیر فعال سازی بات\n\n●✅شروع : فعال سازی بات\n\n●🕘ساعت : ساعت\n\n●📅 !تاریخ : تاریخ\n\n●📋پاک : حذف پیام با ریپ بر روی ان\n\n●🔒قفل گپ : بستن چت در گروه\n\n●🔓باز گپ : باز کردن چت در گروه\n\n●❌ریم : حذف کاربر با ریپ زدن\n\n●✉ send : ارسال پیام با استفاده از ایدی\n\n●📌اد : افزودن کاربر به گپ با ایدی\n\n●📜لیست : لیست دستورات ربات\n\n●🆑ماشین حساب :ماشین حساب\n\n●🔴 !user : اطلاعات کاربر با ایدی\n\n●😂جوک : ارسال جک\n\n●🔵 !فونت : ارسال فونت\n\n●🔴پینگ : گرفتن پینگ سایت\n\n●🔵ترجمه : مترجم انگلیس\n\n دیالوگ: دیالوگ \n\n ●🔵داستان:گفتن داستان \n\n ●🔵 پ ن پ : گفتن پ ن پ \n\n ●🔵 دانستی:گفتن دانستنی \n\n ●🔵 حدیث : گفتن حدیث \n\n ●🔵 ذکر : گفتن ذکر \n\n ●🔵 weather : گرفتن آب و هوای با گزاشتن اسم شهر خود جلوی کلمه")		
					elif msg.get("text").startswith("ماشین حساب"):
						msd = msg.get("text")
						if plus == True:
							try:
								call = [msd.split(" ")[1], msd.split(" ")[2], msd.split(" ")[3]]
								if call[1] == "+":
									am = float(call[0]) + float(call[2])
									bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
									plus = False
							
								elif call[1] == "-":
									am = float(call[0]) - float(call[2])
									bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
							
								elif call[1] == "*":
									am = float(call[0]) * float(call[2])
									bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
							
								elif call[1] == "/":
									am = float(call[0]) / float(call[2])
									bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
							except IndexError:
								bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ❌" ,message_id=msg.get("message_id"))
						plus= True
					elif msg.get("text").startswith("پیام") :
						bot.sendMessage(bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["object_guid"], "شما یک پیام ناشناس دارید:\n"+" ".join(msg.get("text").split(" ")[2:]))
						bot.sendMessage(target, "پیام ارسال شد ✅", message_id=msg.get("message_id"))

					elif msg.get("text") == "افرین ربات بز":
						bot.sendMessage(target, "اولن ممنون دومن خودتی ", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("نگاییدم"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						
					elif msg.get("text").startswith("kir"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						
					elif msg.get("text").startswith("کیر"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						
					elif msg.get("text").startswith("کص"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						
					elif msg.get("text").startswith("کون"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						
					elif msg.get("text").startswith("مادرت"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						
					elif msg.get("text").startswith("مادرتو"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						
					elif msg.get("text").startswith("کیرم"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						
					elif msg.get("text").startswith("کوص"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						
					elif msg.get("text").startswith("کوس"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						
					elif msg.get("text").startswith("کبص"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						
					elif msg.get("text").startswith("کوبص"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						
					elif msg.get("text").startswith("کسکش"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						
					elif msg.get("text").startswith("بی ناموس"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						
					elif msg.get("text").startswith("بیناموس"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						
					elif msg.get("text").startswith("بی ناموص"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						
					elif msg.get("text").startswith("بیناموص"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])

					elif msg.get("text") == "سنجاق" and msg.get("author_object_guid") in admins :
						    bot.pin(target, msg["reply_to_message_id"])
						    bot.sendMessage(target, "پیام مورد نظر با موفقیت سنجاق شد!", message_id=msg.get("message_id"))

					elif msg.get("text") == "برداشتن سنجاق" and msg.get("author_object_guid") in admins :
						    bot.unpin(target, msg["reply_to_message_id"])
						    bot.sendMessage(target, "پیام مورد نظر از سنجاق برداشته شد!", message_id=msg.get("message_id"))
					elif msg.get("text") == "برداشتن سنجاق" and msg.get("author_object_guid") in admins :
						    bot.unpin(target, msg["reply_to_message_id"])
						    bot.sendMessage(target, "پیام مورد نظر از سنجاق برداشته شد!", message_id=msg.get("message_id"))

					elif msg.get("text") == "بابات کیه":
						bot.sendMessage(target, "سینا جون", message_id=msg.get("message_id"))

					elif msg.get("text").startswith("trans"):
						
						try:
							responser = get(f"https://api.codebazan.ir/translate/?type=json&from=en&to=fa&text={msg.get('text').split()[1:]}").json()
							al = [responser["result"]]
							bot.sendMessage(msg.get("author_object_guid"), "پاسخ به ترجمه:\n"+"".join(al)).text
							bot.sendMessage(target, "نتیجه رو برات ارسال کردم😘", message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "دستور رو درست وارد کن دیگه😁", message_id=msg["message_id"])


					elif msg.get("text").startswith("فونت"):
						#print("\n".join(list(response["result"].values())))
						try:
							response = get(f"https://api.codebazan.ir/font/?text={msg.get('text').split()[1]}").json()
							bot.sendMessage(msg.get("author_object_guid"), "\n".join(list(response["result"].values())[:110])).text
							bot.sendMessage(target, "نتیجه رو برات ارسال کردم😘", message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "دستور رو درست وارد کن دیگه😁", message_id=msg["message_id"])
                    								
					elif msg.get("text") == "ربات":
						bot.sendMessage(target, "بـلـه‍😁", message_id=msg.get("message_id"))						
																		
					elif msg.get("text") == "اره":
						bot.sendMessage(target, "😂اجر پاره خشتک بابات پاره" , message_id=msg.get("message_id"))

					if  msg.get("text").startswith('ایدی @'):
						try:
							user_info = bot.getInfoByUsername( msg.get("text")[7:])
							if user_info['data']['exist'] == True:
								if user_info['data']['type'] == 'User':
									bot.sendMessage(target, 'Name User:\n ' + user_info['data']['user']['first_name'] + ' ' + user_info['data']['user']['last_name'] + '\n\nBio User:\n ' + user_info['data']['user']['bio'] + '\n\nGuid:\n ' + user_info['data']['user']['user_guid'] ,  msg.get('message_id'))
									print('sended response')
								else:
									bot.sendMessage(target, 'کانال است ❌' ,  msg.get('message_id'))
									print('sended response')
							else:
								bot.sendMessage(target, "کاربری وجود ندارد ❌" ,  msg.get('message_id'))
								print('sended response')
						except:
							print('server bug6')
							bot.sendMessage(target, "خطا در اجرای دستور مجددا سعی کنید ❌" ,message_id=msg.get("message_id"))
							
					elif msg.get("text") == "چخبر":
						bot.sendMessage(target, "سلامتی رهبر ", message_id=msg.get("message_id"))
					
					elif msg.get("text") == "خاموش" and msg.get("author_object_guid") in admins :
						sleeped = True
						bot.sendMessage(target, "ربات خاموش شد ✅", message_id=msg.get("message_id"))

					elif msg.get("text").startswith("ذکر"):
						
						try:
							response = get("http://api.codebazan.ir/zekr/").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "دستورت رو اشتباه وارد کردی", message_id=msg["message_id"])

					elif msg.get("text").startswith("حدیث"):
						
						try:
							response = get("http://api.codebazan.ir/hadis/").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "دستورت رو اشتباه وارد کردی", message_id=msg["message_id"])

					elif msg.get("text").startswith("بیوگرافی"):
						
						try:
							response = get("https://api.codebazan.ir/bio/").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "دستورت رو اشتباه وارد کردی", message_id=msg["message_id"])

					elif msg["text"].startswith("weather"):
						response = get(f"https://api.codebazan.ir/weather/?city={msg['text'].split()[1]}").json()
						#print("\n".join(list(response["result"].values())))
						try:
							bot.sendMessage(msg["author_object_guid"], "\n".join(list(response["result"].values())[:20])).text
							bot.sendMessage(target, "نتیجه بزودی برای شما ارسال خواهد شد...", message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "متاسفانه نتیجه‌ای موجود نبود!", message_id=msg["message_id"])

					elif msg.get("text").startswith("دیالوگ"):
						
						try:
							response = get("http://api.codebazan.ir/dialog/").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "دستورت رو اشتباه وارد کردی", message_id=msg["message_id"])

					elif msg.get("text").startswith("دانستنی"):
						
						try:
							response = get("http://api.codebazan.ir/danestani/").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "دستورت رو اشتباه وارد کردی", message_id=msg["message_id"])

					elif msg.get("text").startswith("داستان"):
						
						try:
							response = get("http://api.codebazan.ir/dastan/").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "دستورت رو اشتباه وارد کردی", message_id=msg["message_id"])

					elif msg.get("text").startswith("الکی مثلا"):
						
						try:
							response = get("http://api.codebazan.ir/jok/alaki-masalan/").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "دستورت رو اشتباه وارد کردی", message_id=msg["message_id"])

					elif msg.get("text").startswith("پ ن پ"):
						
						try:
							response = get("http://api.codebazan.ir/jok/pa-na-pa/").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "دستورت رو اشتباه وارد کردی", message_id=msg["message_id"])

					elif msg.get("text").startswith("پینگ"):																															
						try:
							responser = get(f"https://api.codebazan.ir/ping/?url={msg.get('text').split()[1]}").text
							bot.sendMessage(target, responser,message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ❌", message_id=msg["message_id"])

					elif msg.get("text").startswith("ترجمه"):
						
						try:
							responser = get(f"https://api.codebazan.ir/translate/?type=json&from=en&to=fa&text={msg.get('text').split()[1:]}").json()
							al = [responser["result"]]
							bot.sendMessage(msg.get("author_object_guid"), "پاسخ به ترجمه:\n"+"".join(al)).text
							bot.sendMessage(target, "نتیجه به پیوی شما ارسال شد ✅", message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ❌", message_id=msg["message_id"])

					elif msg.get("text").startswith("فونت"):
						#print("\n".join(list(response["result"].values())))
						try:
							response = get(f"https://api.codebazan.ir/font/?text={msg.get('text').split()[1]}").json()
							bot.sendMessage(msg.get("author_object_guid"), "\n".join(list(response["result"].values())[:110])).text
							bot.sendMessage(target, "نتیجه به پیوی شما ارسال شد ✅", message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ❌", message_id=msg["message_id"])



					elif msg.get("text").startswith("جوک"):
						
						try:
							response = get("https://api.codebazan.ir/jok/").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ❌", message_id=msg["message_id"])

					elif msg.get("text") == "ساعت":
						bot.sendMessage(target, f"Time : {time.localtime().tm_hour} : {time.localtime().tm_min} : {time.localtime().tm_sec}", message_id=msg.get("message_id"))

					elif msg.get("text") == "تاریخ":
						bot.sendMessage(target, f"Date: {time.localtime().tm_year} / {time.localtime().tm_mon} / {time.localtime().tm_mday}", message_id=msg.get("message_id"))

					elif msg.get("text") == "پاک" and msg.get("author_object_guid") in admins :
						bot.deleteMessages(target, [msg.get("reply_to_message_id")])
						bot.sendMessage(target, "پیام پاک شد ✅", message_id=msg.get("message_id"))

					# elif msg.get("text").split(" ")[0] in  delmess:
					# 	bot.deleteMessages(target, [msg.get("message_id")])
					# 	bot.sendMessage(target, "یک پیام مستهجن پاک شد ✅", message_id=msg.get("message_id"))


					elif msg.get("text") == "قفل گپ" and msg.get("author_object_guid") in admins :
						print(bot.setMembersAccess(target, ["ViewMembers","ViewAdmins","AddMember"]).text)
						bot.sendMessage(target, "گپ بسته شد ✅", message_id=msg.get("message_id"))

					elif msg.get("text") == "باز گپ" and msg.get("author_object_guid") in admins :
						bot.setMembersAccess(target, ["ViewMembers","ViewAdmins","SendMessages","AddMember"])
						bot.sendMessage(target, "گپ باز شد ✅", message_id=msg.get("message_id"))

					elif msg.get("text") == "عا":
						bot.sendMessage(target, "چه مرگته ؟", message_id=msg.get("message_id"))

					elif msg.get("text") == "ربات جون ":
						bot.sendMessage(target, "چیه بز", message_id=msg.get("message_id"))

					elif msg.get("text").startswith("ریم") and msg.get("author_object_guid") in admins :
						try:
							guid = bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["abs_object"]["object_guid"]
							user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
							if not guid in admins :
								bot.banGroupMember(target, guid)
								bot.sendMessage(target, f"✅ کاربر حذف شد", message_id=msg.get("message_id"))
							else :
								bot.sendMessage(target, f"❎ کاربر حذف نشد", message_id=msg.get("message_id"))
								
						except IndexError:
							a = bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"]
							if a in admins:
								bot.sendMessage(target, f"کاربر حذف نشد ❌", message_id=msg.get("message_id"))
							else:
								bot.banGroupMember(target, bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"])
								bot.sendMessage(target, f"کاربر حذف شد ✅", message_id=msg.get("message_id"))
								
					elif msg.get("text") == "کص کش":
						bot.sendMessage(target, "ننته😞", message_id=msg.get("message_id"))
				
				else:
					if msg.get("text") == "شروع" and msg.get("author_object_guid") in admins :
						sleeped = False
						bot.sendMessage(target, "ربات فعال شد ✅", message_id=msg.get("message_id"))

			elif msg["type"]=="Event" and not msg.get("message_id") in answered and not sleeped:
				name = bot.getGroupInfo(target)["data"]["group"]["group_title"]
				data = msg['event_data']
				if data["type"]=="RemoveGroupMembers":
					user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"خدانگهدار {user} 🗑️سزای رعایت نکردن قوانین گپ همینه ", message_id=msg["message_id"])          
                    																
				elif data["type"]=="AddedGroupMembers":
					user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"سلام کاربر {user} به گروه {name} خوش اومدید 😃\nلطفا قوانین رو رعایت کن ✅", message_id=msg["message_id"])
				elif data["type"]=="LeaveGroup":
					user = bot.getUserInfo(data['performer_object']['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"خدانگهدار {user} 🗑️", message_id=msg["message_id"])
					
				elif data["type"]=="JoinedGroupByLink":
					user = bot.getUserInfo(data['performer_object']['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"سلام کاربر {user}  به گروه {name} خوش اومدید 😃\nلطفا قوانین رو رعایت کن ✅", message_id=msg["message_id"])

			answered.append(msg.get("message_id"))

	except KeyboardInterrupt:
		exit()

	except Exception as e:
		if type(e) in list(retries.keys()):
			if retries[type(e)] < 3:
				retries[type(e)] += 1
				continue
			else:
				retries.pop(type(e))
		else:
			retries[type(e)] = 1
			continue
