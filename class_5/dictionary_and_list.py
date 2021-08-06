import math

# Courses 1 and 2
# Course 1 course code = 1100, course 2 = 1300
# Each course has an undetermined amount of tests sampled for the course.

course_1 = [98, 66.8, 87, 55]
course_2 = [100, 20, 30, 80, 90]

scores_by_course = {1100: course_1, 1300: course_2}

# what is the average score of course#2 (PROVIDED only the dictionary).

#course = input("For what course # would you like the class average?")

average2 = sum(scores_by_course[1300])/len(scores_by_course[1300])
print("The average is {:.1f}".format(average2))


average = math.fsum(scores_by_course[1300])/len(scores_by_course[1300])
print("The average is {:.1f}".format(average))

