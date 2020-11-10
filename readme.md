
# Code Review App

### How to get data:
    getting the data by making a python program that analyze blocks of code, 
    and using that program we will analyze real word code, 
    some of those code is qualified and some of them are unqualified,
    and all the data will be stored on an SQL database, and also on an CSV file

### Which Machine Learning model will apply
    So, this app will be some sort of classification app, it will classify if the code
    is a quality code, an unqualified code, or an acceptable quality code that could be enhanced,
    so, with that being said we will apply the KNN model because I think it will a great solution 
    for this idea.

### How I will build the code analyzer program:
    So, the code analyzer will start start looking at the code line by line, 
    and we will save each line inside the 'codeSource' array.
    Then a function will loop through the 'codeSource' array and will start analyzing the line
    word by word, and based on the keywork the algorithme will apply a certain operation inside
    the 'codeSource' array and also inside the final record that the app should return
    The final record is basically some crucial information about the code that is gathered from
    the code itself such as number of variables, number of functions, number of unused variables,
    number of classes, number of if/for/while blocks ...

### steps:
    [ ] Developing the code analyzing program
        [x] Splitting the code into lines and assign them into the 'codeSource' array
        [x] Looping through each lines of code (item inside 'codeSource')
        [x] Assign each lines of code based on the keywork to its appropriate function
        [ ] Developing the analyzing functions
        [ ] Creating the output records
    [ ] Test the code analyzing program
    [ ] Gather the code that the code analyzer will analyze
    [ ] Assign the values into the dataset