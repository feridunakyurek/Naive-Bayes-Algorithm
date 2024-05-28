from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Eğitim verileri
emails = [
    "Ödül kazandınız ücretsiz tıklayın",
    "Yeni teklifler sizi bekliyor",
    "Faturanız hazır lütfen kontrol edin",
    "Toplantı yarın saat 10'da",
    "Ücretsiz kredi kartı başvurusu",
    "Ödeme alındı teşekkürler"
]
labels = ['Spam', 'Spam', 'Normal', 'Normal', 'Spam', 'Normal']

# E-posta metinlerini kelime frekanslarına dönüştürme
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(emails)

# Multinomial Naive Bayes modelini oluşturma ve eğitme
model = MultinomialNB()
model.fit(X, labels)

# Yeni bir e-posta metninin tahmini
new_email = ["Ücretsiz hediye kazandınız, tıklayın"]
new_email_counts = vectorizer.transform(new_email)
prediction = model.predict(new_email_counts)
print(f'Tahmin edilen sınıf: {prediction[0]}')
