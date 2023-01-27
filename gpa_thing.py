file = open("thing.java", "w")

things = ["first", "second", "third", "fourth", "fifth"]
for i in things:
    program = f'System.out.print("How many credits was your {i} class? ");\n{i} = Integer.parseInt(input.nextLine());\nSystem.out.print("What grade did you get? ");\n\nletterGrade = input.nextLine();\nif (letterGrade.charAt(0) == \'F\') {{\n    letterGradeValue = 0;\n}}\nelse {{\n	letterGradeValue = Math.abs(((int)letterGrade.charAt(0)) - 69);\n}}\nif (letterGrade.length() == 2) {{\n	letterSubgradeValue = (((double)letterGrade.charAt(1)) - 44) * -0.5;\n}}\nelse {{\n	letterSubgradeValue = 0;\n}}\n{i}Grade = letterGradeValue + letterSubgradeValue;\n\n'
    file.write(program)
