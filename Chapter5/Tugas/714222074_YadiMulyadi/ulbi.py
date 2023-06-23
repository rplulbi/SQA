import urllib.request

def load_url(url):
    try:
        response = urllib.request.urlopen(url)
        data = response.read()
        
        print(data)
    except urllib.error.URLError as e:
        print("Maaf Error! Coba Lagi ya:", e)


url = "https://www.ulbi.ac.id/"
load_url(url)

def process_text(input_text):
    
    processed_text = input_text.upper()
    return processed_text

input_text = input("Official Website ULBI")
processed_text = process_text(input_text)
print("Kampus BUMN di Bandung", processed_text)
