import tkinter as tk
import numpy as np
import joblib


def load_model_and_predict(AgeMonths=0, WeightKg=0, Vaccinated=0, HealthCondition=0, 
                           TimeInShelterDays=0, AdoptionFee=0, PreviousOwner=0, PetType_Cat=0, 
                           PetType_Dog=0, PetType_Rabbit=0, Breed_Labrador=0, Breed_Parakeet=0, 
                           Breed_Persian=0, Breed_Poodle=0, Breed_Rabbit=0, Breed_Siamese=0, 
                           Color_Brown=0, Color_Gray=0, Color_Orange=0, Color_White=0, 
                           Size_Medium=0, Size_Small=0):
    
    feature_vector = np.array([AgeMonths, WeightKg, Vaccinated, HealthCondition, TimeInShelterDays,
                               AdoptionFee, PreviousOwner, PetType_Cat, PetType_Dog, PetType_Rabbit, 
                               Breed_Labrador, Breed_Parakeet, Breed_Persian, Breed_Poodle, 
                               Breed_Rabbit, Breed_Siamese, Color_Brown, Color_Gray, 
                               Color_Orange, Color_White, Size_Medium, Size_Small]).reshape(1, -1)
    
    model = joblib.load('decision_tree_model.pkl')
    prediction = model.predict(feature_vector)
    
    print(prediction)
    
    return prediction

def predict():
    AgeMonths = int(AgeMonths_value.get())
    WeightKg = float(WeightKg_value.get())
    Vaccinated = int(Vaccinated_value.get())
    HealthCondition = int(HealthCondition_value.get())
    TimeInShelterDays = int(TimeInShelterDays_value.get())
    AdoptionFee = float(AdoptionFee_value.get())
    PreviousOwner = int(PreviousOwner_value.get())
    PetType_Cat = int(PetType_Cat_value.get())
    PetType_Dog = int(PetType_Dog_value.get())
    PetType_Rabbit = int(PetType_Rabbit_value.get())
    Breed_Labrador = int(Breed_Labrador_value.get())
    Breed_Parakeet = int(Breed_Parakeet_value.get())
    Breed_Persian = int(Breed_Persian_value.get())
    Breed_Poodle = int(Breed_Poodle_value.get())
    Breed_Rabbit = int(Breed_Rabbit_value.get())
    Breed_Siamese = int(Breed_Siamese_value.get())
    Color_Brown = int(Color_Brown_value.get())
    Color_Gray = int(Color_Gray_value.get())
    Color_Orange = int(Color_Orange_value.get())
    Color_White = int(Color_White_value.get())
    Size_Medium = int(Size_Medium_value.get())
    Size_Small = int(Size_Small_value.get())
    
    prediction = load_model_and_predict(AgeMonths, WeightKg, Vaccinated, HealthCondition, 
                                        TimeInShelterDays, AdoptionFee, PreviousOwner, 
                                        PetType_Cat, PetType_Dog, PetType_Rabbit, Breed_Labrador, 
                                        Breed_Parakeet, Breed_Persian, Breed_Poodle, Breed_Rabbit, 
                                        Breed_Siamese, Color_Brown, Color_Gray, Color_Orange, 
                                        Color_White, Size_Medium, Size_Small)
    
    Result = "Likely to be adopted" if prediction == 1 else "Unlikely to be adopted"
    
    result_label.config(text=f"Prediction: {Result}")
    
    

ui = tk.Tk()
ui.title("Adoption_likeklihood_predictor")
ui.geometry("600x400")

AgeMonths_value = tk.StringVar()
WeightKg_value = tk.StringVar()
TimeInShelterDays_value = tk.StringVar()
AdoptionFee_value = tk.StringVar()
Vaccinated_value = tk.IntVar()
HealthCondition_value = tk.BooleanVar()
PreviousOwner_value = tk.BooleanVar()
PetType_Dog_value = tk.BooleanVar()
PetType_Cat_value = tk.BooleanVar()
PetType_Rabbit_value = tk.BooleanVar()
Breed_Labrador_value = tk.BooleanVar()
Breed_Parakeet_value = tk.BooleanVar()
Breed_Persian_value = tk.BooleanVar()
Breed_Poodle_value = tk.BooleanVar()
Breed_Rabbit_value = tk.BooleanVar()
Breed_Siamese_value = tk.BooleanVar()
Color_Brown_value = tk.BooleanVar()
Color_Gray_value = tk.BooleanVar()
Color_Orange_value = tk.BooleanVar()
Color_White_value = tk.BooleanVar()
Size_Medium_value = tk.BooleanVar()
Size_Small_value = tk.BooleanVar()

AgeMonths_label = tk.Label(ui, text = 'Age in months:', font=('calibre',10, 'bold'))
AgeMonths_entry = tk.Entry(ui, textvariable = AgeMonths_value, font=('calibre',10,'normal'))
WeightKg_label = tk.Label(ui, text = 'Weight in kg:', font=('calibre',10, 'bold'))
WeightKg_entry = tk.Entry(ui, textvariable = WeightKg_value, font=('calibre',10,'normal'))
TimeInShelterDays_label = tk.Label(ui, text = 'Time in shelter:', font=('calibre',10, 'bold'))
TimeInShelterDays_entry = tk.Entry(ui, textvariable = TimeInShelterDays_value, font=('calibre',10,'normal'))
AdoptionFee_label = tk.Label(ui, text = 'Adoption fee:', font=('calibre',10, 'bold'))
AdoptionFee_entry = tk.Entry(ui, textvariable = AdoptionFee_value, font=('calibre',10,'normal'))

Conditions_label = tk.Label(ui, text = 'Conditions:', font=('calibre',10, 'bold'))
Vaccinated_checkbutton = tk.Checkbutton(text="Vaccinated", variable=Vaccinated_value)
HealthCondition_checkbutton = tk.Checkbutton(text="Health condition", variable=HealthCondition_value)
PreviousOwner_checkbutton = tk.Checkbutton(text="Previous owner", variable=PreviousOwner_value)

PetType_label = tk.Label(ui, text = 'Pet type:', font=('calibre',10, 'bold'))
PetType_dog_label = tk.Checkbutton(text="Dog", variable=PetType_Dog_value)
PetType_cat_label = tk.Checkbutton(text="Cat", variable=PetType_Cat_value)
PetType_rabbit_label = tk.Checkbutton(text="Rabbit", variable=PetType_Rabbit_value)

Breed_label = tk.Label(ui, text='Breed:', font=('calibre', 10, 'bold'))
Breed_Labrador_checkbutton = tk.Checkbutton(ui, text="Labrador", variable=Breed_Labrador_value)
Breed_Parakeet_checkbutton = tk.Checkbutton(ui, text="Parakeet", variable=Breed_Parakeet_value)
Breed_Persian_checkbutton = tk.Checkbutton(ui, text="Persian", variable=Breed_Persian_value)
Breed_Poodle_checkbutton = tk.Checkbutton(ui, text="Poodle", variable=Breed_Poodle_value)
Breed_Rabbit_checkbutton = tk.Checkbutton(ui, text="Rabbit", variable=Breed_Rabbit_value)
Breed_Siamese_checkbutton = tk.Checkbutton(ui, text="Siamese", variable=Breed_Siamese_value)

Color_label = tk.Label(ui, text='Color:', font=('calibre', 10, 'bold'))
Color_Brown_checkbutton = tk.Checkbutton(ui, text="Brown", variable=Color_Brown_value)
Color_Gray_checkbutton = tk.Checkbutton(ui, text="Gray", variable=Color_Gray_value)
Color_Orange_checkbutton = tk.Checkbutton(ui, text="Orange", variable=Color_Orange_value)
Color_White_checkbutton = tk.Checkbutton(ui, text="White", variable=Color_White_value)

Size_label = tk.Label(ui, text='Size:', font=('calibre', 10, 'bold'))
Size_Medium_checkbutton = tk.Checkbutton(ui, text="Medium", variable=Size_Medium_value)
Size_Small_checkbutton = tk.Checkbutton(ui, text="Small", variable=Size_Small_value)

predict_button = tk.Button(ui, text='Predict', command=predict)
result_label = tk.Label(ui, text='Prediction:', font=('calibre', 12, 'bold'))

AgeMonths_label.place(x=0, y=10)
AgeMonths_entry.place(x=90, y=10)
WeightKg_label.place(x=0, y=30)
WeightKg_entry.place(x=90, y=30)
TimeInShelterDays_label.place(x=0, y=50)
TimeInShelterDays_entry.place(x=90, y=50)
AdoptionFee_label.place(x=0, y=70)
AdoptionFee_entry.place(x=90, y=70)

Conditions_label.place(x=300, y=10)
Vaccinated_checkbutton.place(x=370, y=8)
HealthCondition_checkbutton.place(x=370, y=28)
PreviousOwner_checkbutton.place(x=370, y=48)

PetType_label.place(x=0, y=110)
PetType_dog_label.place(x=90, y=108)
PetType_cat_label.place(x=90, y=128)
PetType_rabbit_label.place(x=90, y=148)

Breed_label.place(x=300, y=90)
Breed_Labrador_checkbutton.place(x=370, y=88)
Breed_Parakeet_checkbutton.place(x=370, y=108)
Breed_Persian_checkbutton.place(x=370, y=128)
Breed_Poodle_checkbutton.place(x=370, y=148)
Breed_Rabbit_checkbutton.place(x=370, y=168)
Breed_Siamese_checkbutton.place(x=370, y=188)

Color_label.place(x=0, y=190)
Color_Brown_checkbutton.place(x=90, y=188)
Color_Gray_checkbutton.place(x=90, y=208)
Color_Orange_checkbutton.place(x=90, y=228)
Color_White_checkbutton.place(x=90, y=248)

Size_label.place(x=300, y=230)
Size_Medium_checkbutton.place(x=370, y=228)
Size_Small_checkbutton.place(x=370, y=248)

predict_button.place(x=0, y=300)
result_label.place(x=150, y=302)


ui.mainloop()
    