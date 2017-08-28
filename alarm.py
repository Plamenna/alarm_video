import os
import click
import time
import math
import webbrowser
import random 
#check if the file with all music 
@click.command()
@click.option('--time1',default=1.0)
def ringalarm(time1): 
	if os.path.isfile("Videos.txt")==False:
		print "The file does't exist"
        	print "Creating the file "
		flags=os.O_CREAT | os.O_EXCL | os.O_WRONLY 
 		filename=os.open("Videos.txt",flags)
		with os.fdopen(filename, 'w') as file:
		#file.write("https://youtu.be/BZg8BhBWyo8")
			file.write("https://www.youtube.com/watch?v=3AtDnEC4zak")
 	#click.echo('The time is ' % time)
	Time = time.strftime("%H.%M")
	print "the time is =", Time
	with open("Videos.txt") as f:
		content=f.readlines()

	if  Time !=time1:
		print "The time is ",Time 
		time_diff=abs(float(time.strftime("%H.%M") )-time1)
		frac,whole=math.modf(time_diff)
		time_step= frac*60*100+whole*3600
		print time_step
		time.sleep(time_step)
		videorandom=random.choice(content)
		webbrowser.open(videorandom)
		print ":AA::A:A:"
                
	
if __name__=="__main__":
	ringalarm()

