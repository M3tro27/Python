from pytube import YouTube
<<<<<<< HEAD
=======
import ffmpeg
import os
>>>>>>> 580955f5df2223cb1f7e8204e5b77bfd6b71739a

def downloader(odkaz, rozliseni, titulky):

	yt = YouTube(odkaz) 	 #najde video

	print("Název: ",yt.title)			#vypíše paramtery videa
	print("Délka videa: ",yt.length)
	print("Počet shlédnutí: ",yt.views)

<<<<<<< HEAD
	if rozliseni == 'nezadano':					#pokud uživatel nezadá rozlišení, stáhne se video v nejlepší kvalitě
		ys = yt.streams.get_highest_resolution()
	else:
		ys = yt.streams.filter(res=rozliseni)

=======
>>>>>>> 580955f5df2223cb1f7e8204e5b77bfd6b71739a

	try:
		if titulky == 'ano':
			caption = yt.captions.get_by_language_code('en')
			caption.xml_captions
			tit = caption.generate_srt_captions()
			tit.download()
	except:
		print("Žádné titulky  k dispozici")

<<<<<<< HEAD
	try: 
		ys.download()     #zahájí stahování videa
		print("Stahování")
	except:
		print("Špatně zadaná data")
=======
	if rozliseni == 'nezadano':													#pokud uživatel nezadá rozlišení, stáhne se video v nejlepší kvalitě
		video_file = yt.streams.filter(mime_type="video/webm").order_by('resolution').desc().first()		
	else:
		video_file = yt.streams.filter(mime_type="video/webm").filter(res=rozliseni).order_by('resolution').desc().first()

	audio_file = yt.streams.filter(only_audio=True).order_by('abr').desc().first()		


	if not os.path.exists(os.getcwd()+"/tmp"):
			os.makedirs(os.getcwd()+"/tmp")

	if not os.path.exists(os.getcwd()+"/downloaded_videos"):
			os.makedirs(os.getcwd()+"/downloaded_videos")

	try: 
		print("Stahování")
		video_file.download(output_path=os.getcwd()+"/tmp",filename="video")    						 	#zahájí stahování videa a zvukobé stopy
		audio_file.download(output_path=os.getcwd()+"/tmp",filename="audio") 		

		print(os.getcwd()+"/tmp/audio.webm")
		source_audio = ffmpeg.input(os.getcwd()+"\\tmp\\audio.webm")			#zpracování videa a stopy
		source_video = ffmpeg.input(os.getcwd()+"\\tmp\\video.webm")

		ffmpeg.concat(source_video, source_audio, v=1, a=1).output("downloaded_videos/"+yt.title+".mp4").run(cmd=os.getcwd()+"\\Source\\binaries\\ffmpeg")

		print("Staženo")

	except:
		print("Špatně zadaná data")


	if os.path.exists(os.getcwd()+"/tmp/video.webm"):
			os.remove(os.getcwd()+"/tmp/video.webm")

	if os.path.exists(os.getcwd()+"/tmp/audio.webm"):
		os.remove(os.getcwd()+"/tmp/audio.webm")

	if os.path.exists(os.getcwd()+"/tmp"):
		os.rmdir(os.getcwd()+"/tmp")
>>>>>>> 580955f5df2223cb1f7e8204e5b77bfd6b71739a
