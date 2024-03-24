import streamlit as st

# st.title('Hello Prajesh.Work Hard and Believe in your self.')
# title
st.title("Title :- Happy Coding!")
# Header
st.header("Header :- Machine Learning and Data Science")
# Subheader
st.subheader("subheader :- GFG")

# markdown
st.markdown("# Hello World!")
st.markdown("## Hello World!!")
st.markdown("### Hello World!!!")
st.markdown("#### Hello World!!!!")
st.markdown("##### Hello World!!!!!")

#commands 
# success
st.success("We are the best Software Developer and DataScientist of all time")

# Information
st.info("Information of Data")

#Warning
st.warning("Warning! NO DISTRACTION")

#Error
st.error("Test Error is being Displayed")

#If we want to define a specific error
st.exception(ZeroDivisionError("Division is not possible with 0"))
st.exception(FileNotFoundError("File not found"))
st.exception(ModuleNotFoundError("Module is not present"))


#Help 
st.help(ZeroDivisionError)

#Text
st.text("This is just a simple text")

#Write
st.write("range(1,10)")
st.write(range(1,10))
st.write('1+2+3')
st.write(1+2+3)
st.write(1*2*3)

#If We want to write a specific code
st.code('x=10 \n'
        'for i in range(x): \n'
        '   print(i)')


#Checkbox
st.checkbox("Male")
st.checkbox("Female")
if (st.checkbox("Fuzzy")):
    st.write("It will search with a tilda symbol '~'")

radioButton = st.radio("Select :-",('Male','Female','Other'))
if (radioButton=="Male"):
    st.write('You are a Male')
elif (radioButton=="Female"):
    st.write('You are a Female')
elif (radioButton=="Other"):
    st.write("You're other Gender")



#SelectBox
st.subheader("Select Your area of Data Science")
select_Box = st.selectbox("Data Science : ",['Data Analysis','Web Scrapping','Machine Learning',
                                "Deep Learning","Computer Vision","Natural Language Processing"]) 

st.write(select_Box)


st.subheader("Multi-Select Box")
multiselect_box = st.multiselect("Data Science : ",['Data Analysis','Web Scrapping','Machine Learning',
                                "Deep Learning","Computer Vision","Natural Language Processing"])
st.write(len(multiselect_box),multiselect_box)
# for i in range(len(multiselect_box)):
#     print(multiselect_box[i])

st.subheader("button")
if (st.button('Click me')):
    st.write("Thanks for clicking")

st.subheader("Slider")
vol=st.slider('Select the Volume :- ',1,10,step=1)
st.write("Your volume is :-",vol)

st.subheader("text-input")
username=st.text_input('Enter your name : ')
password=st.text_input("password : ",type='password')

st.subheader("Text-Area")
word=st.text_area("Write something interesting about yourself in 10 words",height = 10)
st.write(word)


st.subheader("Input Number")
number=st.number_input("Enter the desired number of your choice:-",18,60)
st.write("The number you entered is :-",number)


st.subheader("Input Date")
date=st.date_input("select the date of your choice :- ")
st.write(date)

st.subheader('Input Time')
time=st.time_input("select the time")
st.write(time)














