class time_period:
	day = ""
	start_time = 0 #minutes since start of day
	end_time = 0  

	def __init__(self, st_time, end_time, d):
		self.start_time = self.convert_string(st_time)
		self.end_time = self.convert_string(end_time)
		self.day = d

	def convert_string (self, str_time):
		str_half = int((str_time[5: -1]) == "PM")
		str_hour = int(str_time[0 :2]) %  12
		str_minute = int(str_time[3: 5])
		return (str_hour * 60 + str_minute) + (str_half * (12 * 60))


class single_class:
	number = "" 
	name = ""
	units = 0
	times = [] #




class schedule:
	total_units = 0
	classes = []



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





#outputs : top 10 best schedules ranked
# iput priority dictionary of classes, RAW from Api
def best_schedules () 