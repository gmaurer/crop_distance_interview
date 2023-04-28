# crop_distance_interview
This is for reference:

Doctors Office
Exercise Description
We are running a simulation of a doctors office waiting room. The information about the waiting room is described by an unordered list of events that happened throughout the day. Using that data, write a script that generates a list of patients and their ages in the order they were called back to see the doctor. This office prioritizes calling back the oldest patient in the waiting room first.

Input Data
The input data for this exercise is a text file with each row representing a Patient Arrival(A) or Calling a Patient Back(C). This file is accessible from the following path: /home/coderpad/data/data.txt.

Sample Input
timestamp eventKey id firstName lastName dob
1660761287 A 9371733504 Josie B 12/2/1993
1660761469 C
1660761189 C
1660761415 A 4767174149 Karen Q 7/2/1991
1660761088 A 4600447495 Sammy H 11/2/1981
1660761418 C
Output Data
The output data for this exercise is a list of patients and their age in the order they were called back to see the doctor.

Output Format
The output data should be formatted: FirstName LastInitial AgeInYears

Sample Output
Sammy H 41
Karen Q 31
Josie B 29
