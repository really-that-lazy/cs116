

## QUESTION 1 ##########################

def freq_table(nlst):
    pass


## QUESTION 2 ######################3


##Part a)

def most_popular_courses(term):
    pass
    
##Part b)

def common_courses(t1, t2):
    pass

##Part c)

def offered_once(t1, t2):
    pass

##Part d)

def enroll_student(term, course, studid):
    pass
        
    
##Part e)

def drop_student(term, course, studid):
    pass



## QUESTION 3 ######################

class Line:
    '''Fields: slope(anyof Int Float "undefined"), intercept (anyof Int Float)
          '''  
    
    def __init__(self,slope,intercept):
        self.slope = slope
        self.intercept = intercept
        
        
    def __repr__(self):
        s1 = "Y = {0:.2f}X + {1:.2f}"
        s2 = "X = {0:.2f}"
        s3 = "Y = {0:.2f}"
        if self.slope=="undefined":
            return s2.format(self.intercept)
        elif self.slope==0:
            return s3.format(self.intercept)
        else:
            return s1.format(self.slope, self.intercept)
    
    def __eq__(self, other):
            return type(other) == type(self) and self.slope == other.slope and \
                   self.intercept == other.intercept    
        
    
    def points_to_line(x1,y1,x2,y2):
        pass
        
    def perpendicular_line(self,x,y):
        pass
        

    def parallel(self, other):
        pass
    
    def intersect(self, other):
        pass
   
# end of Line class


