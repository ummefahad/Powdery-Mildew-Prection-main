import streamlit as st
import pickle
import numpy as np
model=pickle.load(open('model.pkl','rb'))

def inputs():
    CloudFactor = st.selectbox("Select Cloud Factor",tuple(cloudfactor_label.keys()))
    Soilmoisture = st.selectbox("Select Soil moisture",tuple(soilmoisture_label.keys()))
    Temperature = st.selectbox("Select Temperature",tuple(temperature_label.keys()))
    Humidity = st.selectbox("Select Humidity",tuple(humidity_label.keys()))
    
    #encoding
    v_CloudFactor=get_value(CloudFactor,cloudfactor_label)
    v_Soilmoisture=get_value(Soilmoisture,soilmoisture_label)
    v_Temperature=get_value(Temperature,temperature_label)
    v_Humidity=get_value(Humidity,humidity_label)
    
    data=np.array([[v_CloudFactor,v_Soilmoisture,v_Temperature,v_Humidity]]).astype(np.int64)
    
    return data
    
cloudfactor_label={'Open (0 to 2 Oktas)':0,'Broken (3 to 7 Oktas)':1,'Closed (8 to 9 Oktas)':2}
soilmoisture_label={'Adequate (70% to 90%)':0,'Inadequate (Below 70%)':1}
temperature_label={'Moderate (25C to 30C)':0,'Minimum (15C to 25C)':1,'Maximum (30C to 35C)':2}
humidity_label={'Moderate(70%rh to 90%rh)':0,'Minimum (50%rh to 70%rh)':1,'Maximum (90%rh to 100%rh)':2}

#get the value
def get_value(val,my_dict):
    for key,value in my_dict.items():
        if val==key:
            return value

def main():
    html_temp = """
    <div style="background-color:#006400;padding:10px">
    <h2 style="color:white;text-align:center;">Powdery Mildew Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    input=inputs()
    
    if st.button("predict"):
        prediction=model.predict(input)
        pred='{0}'.format(prediction[0])
        if pred == '0':
            st.header("Chances of getting Powdery Mildew disease is Low(20% to 40%)")
        elif pred == '1':
            st.header("Chances of getting Powdery Mildew disease is Medium(40% to 70%)")
        else:
            st.header("Chances of getting Powdery Mildew disease is High(70% to 90%)")
        st.subheader("Precautions Or Treatment to avoid Powdery Mildew:")
        st.markdown("BAKING SODA SOLUTION: Mix 1 tablespoon baking soda and ½ teaspoon liquid soap such as Castile soap (not detergent) in 1 gallon of water. Spray liberally, getting top and bottom leaf surfaces and any affected areas. This method may work better as a preventative measure, although it does have some effect on existing powdery mildew as well.")
        st.markdown("POTASSIUM BICARBONATE: Mix 1 tablespoon potassium bicarbonate and ½ teaspoon liquid soap (not detergent) in 1 gallon of water. Spray liberally to all affected areas. This mixture may work better than baking soda.")
        st.markdown("NEEM OIL: By itself, neem oil has mixed reviews on its effectiveness to treat powdery mildew, but it can be added to the above mixtures for an extra boost.")
        st.markdown("POWDERY MILDEW FUNGICIDE: Use sulfur-containing organic fungicides as both preventive and treatment for existing infections.")
        st.markdown("TRIM OR PRUNE: Remove the affected leaves, stems, buds, fruit or vegetables from the plant and discard. Some perennials can be cut down to the ground and new growth will emerge. Do not compost any damaged or diseased foliage as the spores can spread and persist in the composted material. Disinfect pruners and all tools after using on infected plants.")
if __name__ == '__main__':
    main()