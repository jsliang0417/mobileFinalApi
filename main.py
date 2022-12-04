"""
desgining an api taking in payload as an array with 4 elements
returning body with classification name
"""

from fastapi import FastAPI
import pickle
import os
import numpy as np
from dog import SearchBreed
from clean import reverseCode
from image_processing import Dog_Image_Preprocessing

model_name = "model.pkl"
app = FastAPI()
opened_model = open(model_name, 'rb')
model = pickle.load(opened_model)


@app.get('/dog/{baseCode}')
def dog_classfication(baseCode):
    reversed_code = reverseCode(baseCode)
    dog_names = {
            0:"Chihuahua",
            1:"Japanese_spaniel",
            2:"Maltese_dog",
            3:"Pekinese",
            4:"Shih-Tzu",
            5:"Blenheim_spaniel",
            6:"papillon",
            7:"toy_terrier",
            8:"Rhodesian_ridgeback",
            9:"Afghan_hound",
            10:"basset",
            11:"beagle",
            12:"bloodhound",
            13:"bluetick",
            14:"black-and-tan_coonhound",
            15:"Walker_hound",
            16:"English_foxhound",
            17:"redbone",
            18:"borzoi",
            19:"Irish_wolfhound",
            20:"Italian_greyhound",
            21:"whippet",
            22:"Ibizan_hound",
            23:"Norwegian_elkhound",
            24:"otterhound",
            25:"Saluki",
            26:"Scottish_deerhound",
            27:"Weimaraner",
            28:"Staffordshire_bullterrier",
            29:"American_Staffordshire_terrier",
            30:"Bedlington_terrier",
            31:"Border_terrier",
            32:"Kerry_blue_terrier",
            33:"Irish_terrier",
            34:"Norfolk_terrier",
            35:"Norwich_terrier",
            36:"Yorkshire_terrier",
            37:"wire-haired_fox_terrier",
            38:"Lakeland_terrier",
            39:"Sealyham_terrier",
            40:"Airedale",
            41:"cairn",
            42:"Australian_terrier",
            43:"Dandie_Dinmont",
            44:"Boston_bull",
            45:"miniature_schnauzer",
            46:"giant_schnauzer",
            47:"standard_schnauzer",
            48:"Scotch_terrier",
            49:"Tibetan_terrier",
            50:"silky_terrier",
            51:"soft-coated_wheaten_terrier",
            52:"West_Highland_white_terrier",
            53:"Lhasa",
            54:"flat-coated_retriever",
            55:"curly-coated_retriever",
            56:"golden_retriever",
            57:"Labrador_retriever",
            58:"Chesapeake_Bay_retriever",
            59:"German_short-haired_pointer",
            60:"vizsla",
            61:"English_setter",
            62:"Irish_setter",
            63:"Gordon_setter",
            64:"Brittany_spaniel",
            65:"clumber",
            66:"English_springer",
            67:"Welsh_springer_spaniel",
            68:"cocker_spaniel",
            69:"Sussex_spaniel",
            70:"Irish_water_spaniel",
            71:"kuvasz",
            72:"schipperke",
            73:"groenendael",
            74:"malinois",
            75:"briard",
            76:"kelpie",
            77:"komondor",
            78:"Old_English_sheepdog",
            79:"Shetland_sheepdog",
            80:"collie",
            81:"Border_collie",
            82:"Bouvier_des_Flandres",
            83:"Rottweiler",
            84:"German_shepherd",
            85:"Doberman",
            86:"miniature_pinscher",
            87:"Greater_Swiss_Mountain_dog",
            88:"Bernese_mountain_dog",
            89:"Appenzeller",
            90:"EntleBucher",
            91:"boxer",
            92:"bull_mastiff",
            93:"Tibetan_mastiff",
            94:"French_bulldog",
            95:"Great_Dane",
            96:"Saint_Bernard",
            97:"Eskimo_dog",
            98:"malamute",
            99:"Siberian_husky",
            100:"affenpinscher",
            101:"basenji",
            102:"pug",
            103:"Leonberg",
            104:"Newfoundland",
            105:"Great_Pyrenees",
            106:"Samoyed",
            107:"Pomeranian",
            108:"chow",
            109:"keeshond",
            110:"Brabancon_griffon",
            111:"Pembroke",
            112:"Cardigan",
            113:"toy_poodle",
            114:"poodle",
            115:"standard_poodle",
            116:"Mexican_hairless",
            117:"dingo",
            118:"dhole",
            119:"African_hunting_dog"
        }
    data = Dog_Image_Preprocessing(reversed_code)
    prediction = model.predict(data) 
    index = np.argmax(prediction)
    class_name = index
    confidence_score = prediction[0][index]
    return {
        "dog_type": dog_names[class_name],
        "confidence_score": f"{float(confidence_score)*100:.4f}%",
        "breed_facts": SearchBreed(dog_names[class_name])
    }
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ['PORT']))
    