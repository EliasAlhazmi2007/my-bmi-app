import streamlit as st

# إعدادات الصفحة (اختياري)
st.set_page_config(page_title="حاسبة BMI", page_icon="⚖️")

st.title("⚖️ حاسبة مؤشر كتلة الجسم (BMI)")
st.write("أدخل بياناتك بالأسفل لمعرفة حالتك الصحية:")

# مدخلات المستخدم
weight = st.number_input("الوزن بالكيلوجرام (kg):", min_value=1.0, value=70.0, step=0.1)
height = st.number_input("الطول بالأمتار (m):", min_value=0.5, value=1.70, step=0.01)

if st.button("احسب النتيجة"):
    bmi = weight / (height ** 2)
    st.subheader(f"مؤشر كتلة الجسم لديك هو: {bmi:.2f}")
    
    if bmi < 18.5:
        st.warning("الحالة: نقص في الوزن (Underweight)")
    elif 18.5 <= bmi < 25:
        st.success("الحالة: وزن صحي مثالي (Healthy weight)")
    elif 25 <= bmi < 30:
        st.warning("الحالة: وزن زائد (Overweight)")
    else:
        st.error("الحالة: سمنة (Obesity)")