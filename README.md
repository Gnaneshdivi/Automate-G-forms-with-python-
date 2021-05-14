# Automating Google forms with Python
 Getting started with the code 
 
### Setting Up Environment 
 Run Commands in Gitbash or terminal 
 
 *  ```shell pip3 install selenium```
 
  *  ```shell pip3 install chromedriver```
   
 
 
### Collecting Component address 

* -Open developer options in chrome for the google
* -select the component using the hover in inspect pannel\n 
* -Copy the id and use it to address the component from the script 


### Usage
Veriable tag used below can be altered with any veriable

* ``` web = webdriver.Chrome(ChromeDriverManager().install()) ``` - To get the Brouser connection


* ``` web.get(formurl) ``` - Open Perticular Url (formurl to be changed)


* ``` veriable = web.find_element_by_xpath(elementid) ``` - Connect the element with a veriable ( elementid to be changed accordingly )


* ``` veriable.send_keys(value)``` - Set a pertucualar value of any type to the field ( Value to be changed )


* ``` veriable.click() ``` - Click action on any element 

