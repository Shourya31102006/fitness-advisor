import pyttsx3


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
speak("thakaan ke liye Ek dabaaye")
speak("enter your username")
x = input("enter your username : ")
speak("enter your password")
y = input("enter your password : ")
if x == "marvel" and y == "xyz" :
    print("access granted")
    speak("access granted")
    print("how much is your weight")    
    speak("how much is your weight")
    weight = float(input("kilograms : "))
    print("how much is your height")
    speak("how much is your height")
    height = float(input("metres : "))    
    s = weight/(height*height)
    print(s)
    if s<18.5 :
        print("you're in the underweight range.")
        speak("you're in the underweight range.")
        print ("If you are underweight, it's important to eat a variety of foods that give you the nutrition you need. You should make sure you eat enough energy to gain weight, protein to repair your body and build your muscles, and vitamins and minerals to make you healthy.")
        speak ("If you are underweight, it's important to eat a variety of foods that give you the nutrition you need. You should make sure you eat enough energy to gain weight, protein to repair your body and build your muscles, and vitamins and minerals to make you healthy.") 
    elif s>18.5 and s<24.9:
        print("you're in the healthy weight range.") 
        speak("you're in the healthy weight range.") 
        print("Limit portion size to control calorie intake. Add healthy snacks during the day if you want to gain weight. Be as physically active as you can be. Talk to your doctor about your weight if you think that you weigh too much or too little.")
        speak("Limit portion size to control calorie intake. Add healthy snacks during the day if you want to gain weight. Be as physically active as you can be. Talk to your doctor about your weight if you think that you weigh too much or too little.")
    elif s>24.9 and s<29.9:
        print("you're in the overweight range.")    
        speak("you're in the overweight range.")        
        print("Diet. A steady weight loss of about one pound a week is the safest way to lose weight. Your doctor can refer you to a registered dietitian if you need help in planning your diet Regular exercise such as brisk walking, running, swimming, biking, dancing. The amount of exercise needed to lose weight is different for everyone")    
        speak("Diet. A steady weight loss of about one pound a week is the safest way to lose weight. Your doctor can refer you to a registered dietitian if you need help in planning your diet Regular exercise such as brisk walking, running, swimming, biking, dancing. The amount of exercise needed to lose weight is different for everyone")  
    elif s>30.0:
        print("you're in the obese range.")    
        speak("you're in the obese range.")
        print("People with obesity need to get at least 150 minutes a week of moderate-intensity physical activity to prevent further weight gain or to maintain the loss of a modest amount of weight. While the A.H.A mentions activities like climbing stairs and jogging, one of the easiest and most effective ways to ease into a healthier lifestyle is to begin walking.")       

    
    else :                                                                               
        print("access denied")
        speak("access denied")