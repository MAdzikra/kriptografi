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

# User input
text = st.text_area("Masukkan teks yang akan dienkripsi/didekripsi")
mode = st.radio("Pilih Mode", ["enkripsi", "dekripsi"])

if algoritma == "ROT13":
    st.subheader("Algoritma ROT13")
    if st.button("Proses"):
        result = rot13(text, mode)
        st.success(f"Hasil {mode.capitalize()}: {result}")
elif algoritma == "Vigenere Cipher":
    st.subheader("Algoritma Vigenere Cipher")
    key = st.text_input("Masukkan kunci untuk Vigenere Cipher")
    if st.button("Proses"):
        if not key:
            st.error("Kunci tidak boleh kosong!")
        else:
            result = vigenere_cipher(text, key, mode)
            st.success(f"Hasil {mode.capitalize()}: {result}")

# Display result
if 'result' in locals():
    st.subheader("Hasil Enkripsi / Dekripsi")

    # Save to file button
    st.download_button(
        label="Simpan Hasil ke File (.txt)",
        data=result,
        file_name="hasil_kriptografi.txt",
        mime="text/plain"
    )
