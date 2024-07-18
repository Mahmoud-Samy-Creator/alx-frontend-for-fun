# Sass & Scss
📂 Specializations - Web Stack programming ― React  
👤 By Mahmoud Samy Elshora  
©️ Alx Software Engineering 12-month program  
🔖 Front-end | CSS | SASS  

## Resources
### Read or watch:  
- [Sass Basics](https://sass-lang.com/guide/)  
- [Sass flow control directives: @if, @for, @each and @while](https://sass-lang.com/documentation/at-rules/control/)  
- [Sass references](https://sass-lang.com/documentation/)

## Learning Objectives
At the end of this project, you are expected to be able to `explain to anyone`, without the help of Google:  
### General
* What Sass means
* How to write Sass & Scss file
* What is the difference between Sass and Scss
* What is the Sass preprocessing
* How to declare a variable
* How to use nested definition
* How to import a Sass file
* How to use mixins
* How to declare extend/inheritance styles
* How to manipulate operators

## Requirements
### General

* Allowed editors: `vi`, `vim`, `emacs`.
* All your files will be executed on Ubuntu 18.04 LTS using `Sass 3.7.4` (or higher).
* All your files should end with a new line.
* All your Scss files should have a comment at the beginning (i.e. syntax above).
* All your files should start by a comment describing the task
`A README.md` file, at the root of the folder of the project, is mandatory.
* The length of your files will be tested using `wc`.


## More Info
### Comments for your Scss file:
#### All your Scss file must start with a comment block

```
$ cat my_styles.scss
/* My style */
body {
    .container {
        color: #3D3D3D;
    }
}
$
```

### Install Sass/Scss on Ubuntu 18.04 LTS
```
$ sudo apt-get install -y ruby2.5 ruby2.5-dev
$ sudo apt-get install ubuntu-dev-tools
$ gem install sass -v 3.7.4
$ sass --version
Ruby Sass 3.7.4
```

## Tasks:
### 0. Always debugging!
Write a Sass file that prints `Hello world` in the debug output.
```
guillaume@ubuntu:~/$ sass 0-debug_log.scss | head -n 0
0-debug_log.scss:2 DEBUG: Hello world
guillaume@ubuntu:~/$ 
```
Repo:

* GitHub repository: `alx-frontend-for-fun`
* Directory: `sass_scss`
* File: `0-debug_log.scss`
***
### 1. Color variable
Write a Sass file that assigns the text color `#3D3D3D` to the HTML tags `body` and `p`.
* You must use a Sass variable
```
guillaume@ubuntu:~/$ sass 1-color_variable.scss | tail -n +2
body {
  color: #3D3D3D; }

p {
  color: #3D3D3D; }
guillaume@ubuntu:~/$ 
```

Repo:

* GitHub repository: `alx-frontend-for-fun`
* Directory: `sass_scss`
* File: `1-color_variable.scss`
***

### 2. Colors
Write a Sass file that assigns:

* The text color #3D3D3D to the HTML tags body and p
* The background color #6D6D6D to the HTML tags body and h2
* You must use 2 Sass variables

```
guillaume@ubuntu:~/$ sass 2-color_variables.scss | tail -n +2
body {
  color: #3D3D3D;
  background-color: #6D6D6D; }

p {
  color: #3D3D3D; }

h2 {
  background-color: #6D6D6D; }
guillaume@ubuntu:~/$ 
```
Repo:

* GitHub repository: `alx-frontend-for-fun`
* Directory: `sass_scss`
* File: `2-color_variables.scss`
***

### 4. Nested class
Write a Sass file that assigns:

* Text color `#3D3D3D` to elements inside `body` tags
* Text color `#FF0000` to any elements of class `.red` inside `body` tags
* You must use nested declarations
```
guillaume@ubuntu:~/$ sass 4-nested_class.scss | tail -n +2
body {
  color: #3D3D3D; }
  body .red {
    color: #FF0000; }
guillaume@ubuntu:~/$ 
```
Repo:

* GitHub repository: `alx-frontend-for-fun`
* Directory: `sass_scss`
* File: `4-nested_class.scss`
***

### 5. Nested child
Write a Sass file that assigns:

* Text color #3D3D3D to elements inside body tags
* Text color #FF0000 to any elements of class .red that are th
e first children of the body
* You must use nested declarations

```
guillaume@ubuntu:~/$ sass 5-nested_child.scss | tail -n +2
body {
  color: #3D3D3D; }
  body > .red {
    color: #FF0000; }
guillaume@ubuntu:~/$ 
```

Repo:

* GitHub repository: `alx-frontend-for-fun`
* Directory: `sass_scss`
* File: `5-nested_child.scss`
***

### 6. Nested hover
Write a Sass file that assigns:

* Text color `#FF0000` to `button` tags
* When the user hovers over `button` tags, text color should change to `#00FF00`
* You must use nested declarations
```
guillaume@ubuntu:~/$ sass 6-nested_hover.scss | tail -n +2
button {
  color: #FF0000; }
  button:hover {
    color: #00FF00; }
guillaume@ubuntu:~/$ 
```
Repo:

* GitHub repository: `alx-frontend-for-fun`
* Directory: `sass_scss`
* File: `6-nested_hover.scss`
