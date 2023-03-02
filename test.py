import statistics_operator as so 

class GetData():
    def __init__ (self):
        self.data = None
        self.population_value = None




    def get_continuous (self):
        data = so.DataContinuous()
        population_value = data.population

        if population_value == True:
            self.stdev = so.CFormulas.stdevP (data.data_set)
            self.variance = so.CFormulas.varianceP(data.data_set)
            self.label = '(P)'

        elif population_value == False:
            self.stdev = so.CFormulas.stdevS (data.data_set)
            self.variance = so.CFormulas.varianceS (data.data_set)
            self.label = '(S)'

        self.mean = so.CFormulas.mean(data.data_set)
        self.calc_range = so.CFormulas.range(data.data_set)
        self.median = so.CFormulas.median(data.data_set)
        self.mode = so.CFormulas.mode(data.data_set)
        self.data = so.CFormulas.mode(data.data_set)




    def get_qdiscrete(self):
        data = so.DataDiscreteQ()
        self.population_value = data.population
        self.df = data.df
        self.population_value = data.population
        self.frequency = data.frequency 
        self.midpoints = data.get_midpoints()
        self.bins = data.bins
        self.sum_fx = so.DFormulas.sumfx(self.frequency, self.midpoints)
        self.mean = so.DFormulas.mean(self.sum_fx, self.frequency)
        self.calc_range = so.DFormulas.calc_range(data.bins)
        self.mode = data.bins[self.frequency.index(max(self.frequency))]
        self.median = so.DFormulas.median(self.frequency, self.bins)
    
    #calculating stdev using the correct formula based on whether a population or sample is being used
        if self.population_value == True: 
            self.variance = so.DFormulas.varianceP(self.frequency, self.midpoints, self.mean)
            self.stdev = so.DFormulas.stdev(self.variance)
            self.label = '(P)'
        if self.population_value == False:
            self.variance = so.DFormulas.varianceS(self.frequency, self.midpoints, self.mean)
            self.stdev = so.DFormulas.stdev(self.variance)
            self.label = '(S)'






    def get_stats (self, discrete = None):
        stats = [f'Mean: {self.mean}', f'Range: {self.calc_range}', f'Median: {self.median}', 
                f'Mode: {self.mode}', f'Std deviation{self.label}: {self.stdev}',
                f'Variance{self.label}: {self.variance}']
        for answers in stats: 
            print (answers)

        if discrete is not None:
            pass


bins = ['50 - 79', '80 - 109', '110 - 139', '140 - 169', '170 - 199', '200 - 229']

answer = GetData()
answer.get_qdiscrete()
stats = answer.get_stats()
print (stats)