System.out.print("How many credits was your first class? ");
first = Integer.parseInt(input.nextLine());
System.out.print("What grade did you get? ");

letterGrade = input.nextLine();
if (letterGrade.charAt(0) == 'F') {
    letterGradeValue = 0;
}
else {
	letterGradeValue = Math.abs(((int)letterGrade.charAt(0)) - 69);
}
if (letterGrade.length() == 2) {
	letterSubgradeValue = (((double)letterGrade.charAt(1)) - 44) * -0.5;
}
else {
	letterSubgradeValue = 0;
}
firstGrade = letterGradeValue + letterSubgradeValue;

System.out.print("How many credits was your second class? ");
second = Integer.parseInt(input.nextLine());
System.out.print("What grade did you get? ");

letterGrade = input.nextLine();
if (letterGrade.charAt(0) == 'F') {
    letterGradeValue = 0;
}
else {
	letterGradeValue = Math.abs(((int)letterGrade.charAt(0)) - 69);
}
if (letterGrade.length() == 2) {
	letterSubgradeValue = (((double)letterGrade.charAt(1)) - 44) * -0.5;
}
else {
	letterSubgradeValue = 0;
}
secondGrade = letterGradeValue + letterSubgradeValue;

System.out.print("How many credits was your third class? ");
third = Integer.parseInt(input.nextLine());
System.out.print("What grade did you get? ");

letterGrade = input.nextLine();
if (letterGrade.charAt(0) == 'F') {
    letterGradeValue = 0;
}
else {
	letterGradeValue = Math.abs(((int)letterGrade.charAt(0)) - 69);
}
if (letterGrade.length() == 2) {
	letterSubgradeValue = (((double)letterGrade.charAt(1)) - 44) * -0.5;
}
else {
	letterSubgradeValue = 0;
}
thirdGrade = letterGradeValue + letterSubgradeValue;

System.out.print("How many credits was your fourth class? ");
fourth = Integer.parseInt(input.nextLine());
System.out.print("What grade did you get? ");

letterGrade = input.nextLine();
if (letterGrade.charAt(0) == 'F') {
    letterGradeValue = 0;
}
else {
	letterGradeValue = Math.abs(((int)letterGrade.charAt(0)) - 69);
}
if (letterGrade.length() == 2) {
	letterSubgradeValue = (((double)letterGrade.charAt(1)) - 44) * -0.5;
}
else {
	letterSubgradeValue = 0;
}
fourthGrade = letterGradeValue + letterSubgradeValue;

System.out.print("How many credits was your fifth class? ");
fifth = Integer.parseInt(input.nextLine());
System.out.print("What grade did you get? ");

letterGrade = input.nextLine();
if (letterGrade.charAt(0) == 'F') {
    letterGradeValue = 0;
}
else {
	letterGradeValue = Math.abs(((int)letterGrade.charAt(0)) - 69);
}
if (letterGrade.length() == 2) {
	letterSubgradeValue = (((double)letterGrade.charAt(1)) - 44) * -0.5;
}
else {
	letterSubgradeValue = 0;
}
fifthGrade = letterGradeValue + letterSubgradeValue;

