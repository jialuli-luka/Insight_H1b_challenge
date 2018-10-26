#preprocessing the data
#used for count the appearence for every job and every state.

import sys

class Counting:
    def __init__(self,file,chunksize=1000):
        self.file = file
        self.count_job = dict()
        self.count_state = dict()
        self.count_sum = -1
        self.status_index = -1
        self.job_index = -1
        self.state_index = []

    #find which column is for job name, state name and whether H1B is certified.
    def find_index(self):
        #split the field_name into list
        field_name = []
        fhandle = open(self.file,'r')
        for line in fhandle:
            field_name = line.split(';')
            break;

        #find the index of state, status and job
        for i in range(len(field_name)):
            name = field_name[i].lower()
            if "status" in name:
                self.status_index = i
            elif "state" in name and "work" in name:
                self.state_index.append(i)
            elif "soc" and "name" in name:
                self.job_index = i

        if self.status_index == -1:
            print("Field_name Error: status not found.")
            sys.exit(0)
        elif self.state_index == []:
            print("Field_name Error: state not found.")
            sys.exit(0)
        elif self.job_index == -1:
            print("Field_name Error: job title not found.")
            sys.exit(0)

    #return
    #self.count_job: dictionary. key is the job name and value is the counts
    #self.count_state: dictionary. key is the state name and value is the counts
    #self.count_sum: int. count for all H1B applications
    def count(self):
        self.find_index()
        with open(self.file) as file:
            data = []
            for line in file:
                data = line.split(';')
                if data[self.status_index].lower() == 'certified':
                    self.count_job[data[self.job_index]] = self.count_job.get(data[self.job_index],0) + 1
                    self.count_state[data[self.state_index[0]]] = self.count_state.get(data[self.state_index[0]],0) + 1
                self.count_sum = self.count_sum + 1
        return self.count_job, self.count_state, self.count_sum
