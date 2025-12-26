import streamlit as st
from ingredients_data import INGREDIENTS_DB
from detector import auto_detect_ingredients

st.set_page_config(
    page_title="Food Ingredient Detector",
    page_icon="🍜"
)

st.title("🍜 Food Ingredient Auto Detector")
st.write(
    "Copy **ingredients dari kemasan makanan instan**, "
    "sistem akan **mendeteksi otomatis** dan menampilkan "
    "**manfaat, keamanan, dan risiko**."
)

input_text = st.text_area(
    "Masukkan Ingredients",
    placeholder="Contoh: Gula, Garam, Penguat Rasa (MSG/E621), Pewarna Tartrazin",
    height=150
)

if st.button("🔍 Analisis"):
    if not input_text.strip():
        st.warning("Silakan masukkan ingredients.")
    else:
        detected = auto_detect_ingredients(
            input_text,
            INGREDIENTS_DB
        )

        if not detected:
            st.error("Tidak ada bahan yang terdeteksi.")
        else:
            st.subheader("📊 Hasil Deteksi")

            for ingredient in detected:
                data = INGREDIENTS_DB[ingredient]

                st.markdown(f"### 🧪 {ingredient.upper()}")
                st.success(f"**Fungsi:** {data['fungsi']}")
                st.info(f"**Keamanan:** {data['keamanan']}")
                st.warning(f"**Risiko:** {data['risiko']}")
