from flask import Flask, request, render_template_string
import random

app = Flask(_name_)

ilac_veritabani = {
    "Etol Fort 400 mg": {"kutu": "Beyaz-mavi", "marka": "Nobel", "ambalaj": "20 tablet"},
    "Parol 500 mg": {"kutu": "Beyaz-kırmızı", "marka": "Atabay", "ambalaj": "20 tablet"},
    "Majezik 100 mg": {"kutu": "Beyaz-turuncu", "marka": "Sanovel", "ambalaj": "15 tablet"}
}

@app.route("/", methods=["GET", "POST"])
def eczane_ustasi():
    ilac = random.choice(list(ilac_veritabani.keys()))
    dogru_cevap = f"{ilac_veritabani[ilac]['kutu']}, {ilac_veritabani[ilac]['marka']}, {ilac_veritabani[ilac]['ambalaj']}"
    secenekler = ["Beyaz-mavi, Nobel, 20 tablet", "Beyaz-kırmızı, Atabay, 20 tablet", "Beyaz-turuncu, Sanovel, 15 tablet"]
    random.shuffle(secenekler)

    sonuc = ""
    if request.method == "POST":
        secim = request.form.get("secim")
        if secim == dogru_cevap:
            sonuc = "Doğru cevap! Harikasın!"
        else:
            sonuc = f"Yanlış! Doğru cevap: {dogru_cevap}"

    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Eczane Ustası</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body { font-family: Arial, sans-serif; text-align: center; padding: 20px; }
            h2 { color: #333; }
            form { margin: 20px 0; }
            input[type="radio"] { margin: 10px; }
            input[type="submit"] { padding: 10px 20px; background-color: #4CAF50; color: white; border: none; }
            p { font-size: 18px; color: #d32f2f if '{{sonuc}}'.startswith('Yanlış') else '#2e7d32'; }
        </style>
    </head>
    <body>
        <h2>Hangi kutu '{{ilac}}' ilacına aittir?</h2>
        <form method="POST">
            {% for secenek in secenekler %}
                <input type="radio" name="secim" value="{{secenek}}" required> {{secenek}}<br>
            {% endfor %}
            <br>
            <input type="submit" value="Kontrol Et">
        </form>
        <p>{{sonuc}}</p>
        <a href="/">Yeni Soru</a>
    </body>
    </html>
    """
    return render_template_string(html, ilac=ilac, secenekler=secenekler, sonuc=sonuc)

if _name_ == "_main_":
    app.run(debug=True)
