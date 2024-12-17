import streamlit as st

# ROT13 function
def rot13(text, mode):
    result = ""
    for char in text:
        if char.isalpha():
            shift = 13
            if char.islower():
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            elif char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += char
    return result if mode == "enkripsi" else result

# Vigenère Cipher function
def vigenere_cipher(text, key, mode):
    result = []
    key = key.lower()  # Convert key to lowercase for simplicity
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('a')
            if mode == "dekripsi":
                shift = -shift
            if char.islower():
                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result.append(new_char)
            key_index = (key_index + 1) % len(key)
        else:
            result.append(char)
    return ''.join(result)

# Streamlit interface
st.title("Aplikasi Kriptografi - Vigenere + ROT13")
st.header("Kelompok 6 - Muhamad Rumi Rifai, Candra Wibawa, Muhammad Adzikra Dhiya Alfauzan")

st.sidebar.title("Pilih Algoritma")
algoritma = st.sidebar.selectbox("Algoritma", ["ROT13", "Vigenere Cipher"])

# Pilih metode input
st.subheader("Input Teks")
input_method = st.radio("Pilih Metode Input", ["Ketik Manual", "Unggah File (.txt)"])

# User input dari file atau manual
if input_method == "Ketik Manual":
    text = st.text_area("Masukkan teks yang akan dienkripsi/didekripsi")
elif input_method == "Unggah File (.txt)":
    uploaded_file = st.file_uploader("Unggah file teks", type=["txt"])
    if uploaded_file is not None:
        text = uploaded_file.read().decode("utf-8")
        st.text_area("Isi File", value=text, height=200, disabled=True)

# Pilihan mode enkripsi atau dekripsi
mode = st.radio("Pilih Mode", ["enkripsi", "dekripsi"])

# Proses algoritma
if algoritma == "ROT13":
    st.subheader("Algoritma ROT13")
    if st.button("Proses"):
        if 'text' in locals() and text:
            result = rot13(text, mode)
            st.success(f"Hasil {mode.capitalize()}: {result}")
        else:
            st.error("Teks tidak boleh kosong!")
elif algoritma == "Vigenere Cipher":
    st.subheader("Algoritma Vigenere Cipher")
    key = st.text_input("Masukkan kunci untuk Vigenere Cipher")
    if st.button("Proses"):
        if not key:
            st.error("Kunci tidak boleh kosong!")
        elif 'text' not in locals() or not text:
            st.error("Teks tidak boleh kosong!")
        else:
            result = vigenere_cipher(text, key, mode)
            st.success(f"Hasil {mode.capitalize()}: {result}")

# Download hasil ke file
if 'result' in locals():
    st.subheader("Hasil Enkripsi / Dekripsi")
    st.download_button(
        label="Simpan Hasil ke File (.txt)",
        data=result,
        file_name="hasil_kriptografi.txt",
        mime="text/plain"
    )
