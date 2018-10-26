# Insight_H1b_challenge
Coding challenge for insight data engineering

# Table of Contents
1. [Problem](README.md#problem)
2. [Approach](README.md#approach)
3. [Run Instructions](README.md#run-instructions)

# Problem

A newspaper editor was researching immigration data trends on H1B(H-1B, H-1B1, E-3) visa application processing over the past years, trying to identify the occupations and states with the most number of approved H1B visas. Statistics can be found from the US Department of Labor and its [Office of Foreign Labor Certification Performance Data](https://www.foreignlaborcert.doleta.gov/performancedata.cfm#dis).  

The editor would like to analyze past years data for certified visa applications based on two metrics: Top 10 Occupations and Top 10 States.

Some requirements for this task are listed as follows:
1. Code should be modular and reusable for future. Code should also work well on data for 2019 or 2020.
2. Code should have reasonable time complexity and space complexity. The original data may be very large and the code is for no reason to run for hours.
3. Code should be well-commented. Well-commented code will help with further update in the code.
4. Code should deal with special situation like data missing.
5. No external library is allowed.

The output data should following these rules:
1.The first line is the field name and separated by semicolumn.
2.The Top 10 Occupations or Top 10 States should be listed in a descending order based on how many times they appear in the data. If there are two occupations or states have the same count, sort them using alphabet.
3.The output consists of 3 column. First column is the name. Second column is the count. Third column is the how much percentage that occupation/states takes compared to the total number of certified visa.

# Approach

To deal with the problem of finding top 10 items from large amount of data, there's mainly two steps.
1. Use a hashtable to save the count for every element in the data. When it comes to python, a dictionary is used in this project.
The time for building the dictionary is O(n). n is the number of instances in the data.
2. Use MinHeap to keep track of the 10 most commonly appeared occupations and states.
Choosing MinHeap because when adding a new element into the heap, the time for updating the heap is O(logk). k is the size of the heap. Thus, we can go through all the data and get the 10 most commonly appeared occupations or states in O(nlog10)
3. Extract value and key from the heap and sort the result into the form needed: Sort by the count it appears. If two jobs or two states appear same amount of times, sort them using alphabet.



# Run Instructions

1.put the input data in input folder and name it h1b_input.csv
2.run the command:
./run.sh
3.the output will be ready in the output folder.

