'''Exercise 2: This program counts the distribution of the hour of the day for each of the messages. 
You can pull the hour from the "From " line by finding the time string and then splitting that string 
into parts using the colon character. Once you have accumulated the counts for each hour, print out the counts, 
one per line, sorted by hour as shown below.
“python timeofday.py
Enter a file name: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1”
'''

# open file directly to easier testing
fhand = open('mbox-short.txt')
email_times = {}

for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    else:
        find_double_dots = words[5].find(':')
        double_dots = words[5][:find_double_dots]
        if double_dots not in email_times:
            email_times[double_dots] = 1

        else:
            email_times[double_dots] +=1

for key, value in email_times.items():
    print(f'{key}: {value}')