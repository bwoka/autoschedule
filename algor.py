UNIT_LIMIT=62

class time_period:
	day = "" #day of week
	start_time = 0 #minutes since start of day
	end_time = 0  

	def __init__(self, st_time, end_time, d): #time in format XX:XXAM
		self.start_time = self.convert_string(st_time)
		self.end_time = self.convert_string(end_time)
		self.day = d #full weekday name in caps

	#convert XX:XXAM into minutes since start of the day
	def convert_string (self, str_time):
		str_half = int((str_time[5: -1]) == "PM")
		str_hour = int(str_time[0 :2]) %  12
		str_minute = int(str_time[3: 5])
		return (str_hour * 60 + str_minute) + (str_half * (12 * 60))

	def conflicts(self,time):
		if d!=d:
			return False
		elif self.start_time==time.start_time or self.end_time==self.end_time:
			return True

		elif self.start_time > time.start_time and self.start_time < time.end_time:
			return True
		elif time.start_time > self.start_time and time.start_time < self.end_time:
			return True
		else:
			return False



class single_class:
	number = ""
	class_name = ""
	lecture_section = ""
	recitation_section = ""
	units = 0
	lecture_times = [] #list of time period for class lecture
	recitation_times = [] #list of time period for recitations




class schedule:
	total_units = 0
	classes = [] ## list of single_classes
	times = [] ## list of all time_periods in schedule


#takes an list of single_class objects and returns a
#dictionary with single_class keys mapping to the corresponding time_period list
#inputted invalid classes return empty lists
def get_schedule(classes):
	result={}
	for class in classes:
		classInfo=1#get info here
		parsed=1#parse here
		result[class.name]=parsed
	return result


def anyConflicts(time,schedule):
	for clas in schedule:
		for l in clas.lecture_times:
			if time.conflicts(l): return True
		for r in clas.recitation_times:
			if time.conflicts(r): return True
	return False

def conflicts(clas, schedule):
	toAddLectures=clas.lecture_times
	toAddRecitations=clas.recitation_times
	for l in toAddLectures:
		if anyConflicts(l,schedule): return True
	for r in toAddRecitations:
		if anyConflicts(r,schedule): return True
	return False
		



#recurssive helper function for best_schedules
#inputs: list of desired classes, a schedule built so far.
def find_schedulees(allClasses, i, schedule, limit, units):
	if i>=len(allClasses) or units>UNIT_LIMIT or limit<=0:
		return schedule(total_units=units, classes=schedule)
	newRow=allClasses[i]
	new=[]
	for c in newRow:
		if not conflicts(c,schedule):
			new+=c
	if EARLY:
		new=new[0:limit]
	elif LATE:
		new=new[len(new)-limit:len(new)]
	else:
		new=new[(len(new))/2-(limit+1)/2:(len(new)/2)+(limit+1)/2]
	result=[]
	for n in new:
		newSchedules=find_schedules(allClasses,i+1,schedule+[n],limit-1, units+n.units)+[find_schedules(allClasses,i+1,schedule,limit, units)]
		for n in newSchedules:
			if not schedule.total_units<36:
				result+=n
	return result




#outputs : list of top 10 best schedules ranked
# iput priority dictionary of classes, RAW from Api
def best_schedules(classes):
	allClasses = parse_RAW(classesRAW) #Parse into list of lists of single_classes corresponding to a specific course
	return find_schedulees(allClasses,0,0,[],[])









