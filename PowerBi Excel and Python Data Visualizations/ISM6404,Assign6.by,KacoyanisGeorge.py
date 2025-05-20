import pandas as pd

d = pd.read_csv('CollegeData.csv')

print(d.head())
idvar=d['id']
print(idvar)
name=d['name']
print(name)
city=d['city']
print(city)
state=d['state']
print(state)
region=d['region']
print(region)
highest_degree=d['highest_degree']
print(highest_degree)
control=d['control']
print(control)
gender=d['gender']
print(gender)
admission_rate=d['admission_rate']
print(admission_rate)
sat_avg=d['sat_avg']
print(sat_avg)
undergrads=d['undergrads']
print(undergrads)
tuition=d['tuition']
print(tuition)
faculty_salary_avg=d['faculty_salary_avg']
print(faculty_salary_avg)
loan_default_rate=d['loan_default_rate']
print(loan_default_rate)
median_debt=d['median_debt']
print(median_debt)
lon=d['lon']
print(lon)
lat=d['lat']
print(lat)

import matplotlib.pyplot as plt

# Histogram of Tuition
plt.hist(tuition, bins=20, color='yellow', edgecolor='black')
plt.title('Histogram of Tuition')
plt.xlabel('Tuition')
plt.ylabel('Frequency')
plt.savefig('HistogramofTuition.jpg')
plt.close()

plt.boxplot(tuition)
plt.title('Boxplot and Whisker of Tuition')
plt.xlabel('Tuition')
plt.ylabel('Tuition Distribution')
plt.savefig('BoxplotWhiskerofTuition.jpg')
plt.close()

plt.hist(admission_rate, bins=20, color='yellow', edgecolor='black')
plt.title('Histogram of Admission Rate')
plt.xlabel('Admission Rate')
plt.ylabel('Frequency')
plt.savefig('HistogramofAdmissionRate.jpg')
plt.close()

plt.hist(undergrads, bins=20, color='yellow', edgecolor='black')
plt.title('Histogram of Undergraduates')
plt.xlabel('Undergraduates')
plt.ylabel('Frequency')
plt.savefig('HistogramofUndergrads.jpg')
plt.close()

plt.hist(sat_avg, bins=20, color='yellow', edgecolor='black')
plt.title('Histogram of Average SAT Scores')
plt.xlabel('Avg SAT Scores')
plt.ylabel('Frequency')
plt.savefig('HistogramofSATAVG.jpg')
plt.close()

plt.scatter(admission_rate, sat_avg)
plt.title('Average SAT Scores vs Admission Rates')
plt.xlabel('Admission Rate')
plt.ylabel('Avg SAT Scores')
plt.savefig('ScatterPlotofSATAVGvsAdmissionRate.jpg')
plt.close()

plt.scatter(admission_rate, tuition)
plt.title('Tuition vs Admission Rates')
plt.xlabel('Admission Rate')
plt.ylabel('Tuition')
plt.savefig('ScatterPlotofTuitionvsAdmissionRate.jpg')
plt.close()

plt.scatter(sat_avg, tuition)
plt.title('Tuition vs Average SAT Scores')
plt.xlabel('Average SAT Scores')
plt.ylabel('Tuition')
plt.savefig('ScatterPlotofTuitionvsSATAVG.jpg')
plt.close()

plt.scatter(faculty_salary_avg, tuition)
plt.title('Tuition vs Average Faculty Salary')
plt.xlabel('Average Faculty Salary')
plt.ylabel('Tuition')
plt.savefig('ScatterPlotofTuitionvsAVGFacultySalary.jpg')
plt.close()