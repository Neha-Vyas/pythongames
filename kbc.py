Questions =[[ "1. Who developed Python Programming  Language?","Wick van Rossum", "Rasmus Lerdorf", "Guido van Rossum", "Niene Stom", 3],
["2. How is a code block indicated in Python?", "Brackets", "Indentation","Key", "None", 2],
["3. Which of the following concepts is not a part of Python?", "Pointers", "Loops", "Dynamic Typing", "All of the above", 1],
["4.Which of the following types of loops are not supported in Python?", "for", "While", "do-while", "none", 1],
[ "5.Which type of Programming does Python support?", "object-oriented programming", "structured programming", "functional programming", "all of the mentioned", 4],
[ "6. Which of the following is the correct extension of the Python file?", 
".python", ".pl", ".py",".p", 3],
[ "7. Which keyword is used for function in Python language?", "Function", 
"def", "Fun", "Define", 2],
["8. Which of the following is not a core data type in Python programming?", "Tuples", "Lists", "Class", "Dictionary", 3],
[" 9. What is the maximum possible length of an identifier in Python?", "79 characters", "31 characters", "63 characters", "none of the mentioned", 4],
["10. What does pip stand for python?", "Pip Installs Python", "Pip Installs Packages", "Preferred Installer Program", "All of the mentioned", 3],
["11. Which of the following is the use of id() function in python?", "Every object doesn’t have a unique id.", "Id returns the identity of the object", "All of the mentioned", "None of the mentioned", 2],
["12. To add a new element to a list we use which Python command?", "list1.addEnd(5)", "list1.addLast(5)", "list1.append(5)", "list1.add(5)", 3],           
["13. Which of the following functions is a built-in function in python?", "factorial()", "print()", "seed()", "sqrt()", 2],
["14. What is output of print(math.pow(3, 2))?", "9.0", "None", "9", "None of the mentioned", 1]
]


levels = [1000, 2000, 3000, 5000 ,10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]

money = 0
for i in range(0,len(Questions)):
  ques= Questions[i]
  print(f"\n\nQuestion for Rs. {levels[i]}")
  print(f"1. {ques[1]}      2. {ques[2]}"  )
  print(f"3. {ques[3]}      4. {ques[4]}"  )
  reply = int(input("Enter your answer between (1-4) or 0 to quit: \n "))
  if(reply==0):
    money= levels[i-1]
    break
  if(reply == ques[-1]):
    print(f"Correct Answer, You have won Rs. {levels[i]}")
    if(i==4):
      money== 10000
    elif(i==9):
      money = 320000
    elif(i==14):
      money = 10000000
     
  else:
    print("Wrong Answer!!!!")

print(f"YOur take home money is: {money}")