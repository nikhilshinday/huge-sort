# Huge Sort 
### Motivation
A few years ago when I was a sophomore in college, I met a Google employee in an airport. Excited, I asked him if he could refer me for an internship. He said, "sure, I can refer you, but you need to tell me your solution to sorting a list that is greater than the memory that you have available on a single machine." Fresh out of data structures and not knowing a thing about operating systems and distributed computing, I didn't have a solution for him. Now I think I do!

### Details
The narrow task that I am initially trying to accomplish is to sort an array of values which do not fit in memory using multiple machines. In the space of distributed datasets, there exist very complex problems in the task of sorting, some of which include:
  - sorting values that do not fit on one machine 
  - determining whether a value or range of values exist in the datastructure
  - optimization and network timing constraitns
For the time being, I'm not worrying about solutions to those issues and I'm just focusing on a simpler task. My test array is about 20 GB of 8 Byte floating point numbers. My approach is to apply a modified distributed sorting algorithm loosely resembling merge sort, or at least inspired by its divide-and-conquer aesthetic. 