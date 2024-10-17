#-------------------Question 1-------------------------

def read_grades(filename):
    # Open the specified file in read mode
    with open(filename, 'r') as file:
        # Read all lines from the file
        lines = file.readlines()
    
    students = []
    grades = []
    
    # Process each line from the file
    for line in lines:
          
        name, grade = line.split()
        students.append(name)
        grades.append(int(grade))
        
    # Return the lists of students and grades
    return students, grades

def calculate_average(grades):
    # Calculate the average of the grades; return 0 if the list is empty
    return sum(grades) / len(grades) if grades else 0

def count_above_average(grades, average):
    # Count how many grades are above the calculated average
    return sum(1 for grade in grades if grade > average)

def write_results(filename, average, count):
    # Open the specified output file in write mode
    with open(filename, 'w') as file:
        # Write the average grade formatted to two decimal places
        file.write(f"Average Grade: {average:.2f}\n")
        # Write the count of students with grades above average
        file.write(f"Number of Students Above Average: {count}\n")

def main():
    # Define the input and output filenames
    input_file = 'grades.txt'
    output_file = 'results.txt'
    
    # Read the grades from the input file
    students, grades = read_grades(input_file)
    
    # Check if any grades were read; if not, print a message and exit
    if not grades:
        print("No grades found.")
        return
    
    # Calculate the average grade
    average = calculate_average(grades)
    # Count how many students have grades above the average
    count_above_avg = count_above_average(grades, average)
    
    # Write the results to the output file
    write_results(output_file, average, count_above_avg)
    # Print a message indicating where the results have been written
    print("Results written to results.txt")

# This ensures that the main function runs when the script is executed directly
if __name__ == "__main__":
    main()


#-------------Question2---------------------------

def transform_data(int_list):
    # Create a new list containing each integer squared
    squared_list = [x ** 2 for x in int_list]
    
    #Calculate the sum of the squared values
    squared_sum = sum(squared_list)
    
    #Return both the new list and the sum
    return squared_list, squared_sum

#Call the function to test
if __name__ == "__main__":
    test_values = [1, 2, 3, 4, 5]
    squared_values, total_sum = transform_data(test_values)
    print("Squared Values:", squared_values)
    print("Sum of Squared Values:", total_sum)
