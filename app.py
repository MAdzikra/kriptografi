import streamlit as st

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

def vigenere_cipher(text, key, mode):
    result = []
    key = key.lower()
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

st.title("Aplikasi Kriptografi - Vigenere + ROT13")
st.header("Kelompok 6 - Muhamad Rumi Rifai, Candra Wibawa, Muhammad Adzikra Dhiya Alfauzan")

st.sidebar.title("Pilih Algoritma")
algoritma = st.sidebar.selectbox("Algoritma", ["ROT13", "Vigenere Cipher"])

if algoritma == "ROT13":
    st.subheader("Algoritma ROT13")
    mode = st.radio("Pilih Mode", ["enkripsi", "dekripsi"])
    input_text = st.text_area("Masukkan Teks")
    if st.button("Proses"):
        result_text = rot13(input_text, mode)
        st.success(f"Hasil {mode.capitalize()}: {result_text}")

elif algoritma == "Vigenere Cipher":
    st.subheader("Algoritma Vigenere Cipher")
    mode = st.radio("Pilih Mode", ["enkripsi", "dekripsi"])
    input_text = st.text_area("Masukkan Teks")
    key = st.text_input("Masukkan Kunci")
    if st.button("Proses"):
        if not key:
            st.error("Kunci tidak boleh kosong!")
        else:
            result_text = vigenere_cipher(input_text, key, mode)
            st.success(f"Hasil {mode.capitalize()}: {result_text}")
