# Provided code
# This function checks to ensure that a list is of length
# 8 and that each element is type float
# Parameters:
# row - a list to check
# Returns True if the length of row is 8 and all elements are floats
def check_row_types(row):
    if len(row) != 8:
        print("Length incorrect! (should be 8): " + str(row))
        return False
    ind = 0
    while ind < len(row):
        if type(row[ind]) != float:
            print("Type of element incorrect: " + str(row[ind]) + " which is " + str(type(row[ind])))
            return False
        ind += 1
    return True
	
# define your functions here
def convert_row_type(list_of_elements) :
    corrected_list = []
    for element in list_of_elements :
        element = float(element)
        corrected_list.append(element)
    return corrected_list

def calculate_score(list) :
    SAT = list[0]
    GPA = list[1]
    Interest = list[2]
    Q = list[3]
    GPA_Score = ((GPA * 2) * 0.4)
    SAT_Score= ((SAT / 160) * .3)
    interest_score = (Interest *.1)
    HSQ_score = (Q * .2)
    return "{:.2f}".format(SAT_Score + GPA_Score + interest_score + HSQ_score, 2)

def is_outlier(list) :
    SAT = list[0]/160
    GPA = list[1] * 2
    Interest = list[2]
    Q = list[3]
    if Interest == 0 or GPA > SAT + 2 :
        return True
    else :
        return False

def calculate_score_improved(list) :
    outlier = is_outlier(list)
    score = float(calculate_score(list))

    if outlier == True or score >= 6 :
        return True
    else :
        return False
    
def grade_outlier(list) :
    new_list = sorted(list)
    min_value = new_list[0]
    min_value2 = new_list[1]
    if (min_value2 - min_value) > 20 :
        # print("you have an outlier")
        return True
    else :
        return False
    
def grade_improvement(list) :
    # list.sort()
    if list[0] < list[1] and list[1] < list[2] and list[2] < list[3] :
        return True
    else :
        return False

        

def main():
    # Change this line of code as needed but 
    # make sure to change it back to "superheroes_tiny.csv"
    # before turning in your work!
    # filename = "admission_algorithms_dataset.csv"
    filename = "superheroes_tiny.csv"
    student_scores_name = "student_scores.csv"
    chosen_file = "chosen_students.txt"
    outlier_students_file_name = "outliers.txt"
    improved_file = "chosen_improved.txt"
    improved_chosen = "improved_chosen.csv"
    extra_improved_student_filename = "extra_improved_chosen.txt"

    input_file = open(filename, "r")
    student_scores_file = open(student_scores_name, "w")
    output_file = open(chosen_file, "w")  
    outlier_file = open(outlier_students_file_name, "w")
    S_Impr_File = open(improved_file, "w")
    improved_chosen_students = open(improved_chosen, "w")
    extra_improved_file = open(extra_improved_student_filename, "w")
  
    
    
    print("Processing " + filename + "...")
    # grab the line with the headers
    headers = input_file.readline()
    
    # TODO: loop through the rest of the file
    lines = input_file.readlines()
    for line in lines :
        data = []
        data = line.strip().split(",")
        student_name = data[0]
        data = data[1:]
        score = 6
        # print (input_file.readline()) 
        # print(data)
        # print(convert_row_type(data))
        # print(check_row_types(convert_row_type(data)))
        correctedlist = convert_row_type(data)

        # SAT, GPA, Interest, HighSchool Qualitiy
        first_4_numbers = correctedlist[0:4]
        semester_grades = correctedlist[4:]
        # print(first_4_numbers)
        # print(semester_grades)
        # print(calculate_score(first_4_numbers))
        # print(student_name + "," + str(calculate_score(first_4_numbers)))
        # print(student_name + "," + calculate_score(first_4_numbers))
        outlier = is_outlier(first_4_numbers)
        student_score = float(calculate_score(first_4_numbers))
        improved_chosen_true_false = calculate_score_improved(first_4_numbers)

        student_scores_file.write(student_name + "," + calculate_score(first_4_numbers) + "\n")

        if outlier == True :
            outlier_file.write(student_name + "\n")
        
        if float(calculate_score(first_4_numbers)) >= score :
            output_file.write(student_name + "\n") 
        
        if student_score >= score or (student_score >= 5 and outlier == True) :
            S_Impr_File.write(student_name + "\n")

        if improved_chosen_true_false == True :
            improved_chosen_students.write(student_name + "," + str(first_4_numbers[0]) + "," + str(first_4_numbers[1]) + "," + str(first_4_numbers[2]) + "," + str(first_4_numbers[3]) + "\n")
        
        if student_score>= score or (student_score >= 5 and (is_outlier(first_4_numbers) == True or grade_outlier(semester_grades) == True or grade_improvement(semester_grades) == True)) :
            extra_improved_file.write(student_name + "\n")
        
        # print(student_name + ", " + str(grade_outlier(semester_grades)))
        # print(grade_improvement(semester_grades))



    # TODO: make sure to close all files you've opened!
    input_file.close()
    output_file.close()
    outlier_file.close()
    S_Impr_File.close()
    improved_chosen_students.close()
    extra_improved_file.close()

    print("done!")

# this bit allows us to both run the file as a program or load it as a
# module to just access the functions
if __name__ == "__main__":
    main()
