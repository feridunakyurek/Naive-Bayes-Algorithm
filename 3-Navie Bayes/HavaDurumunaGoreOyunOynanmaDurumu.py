# Verilen değerler
total_days = 14
yes_days = 9
no_days = 5

# Olasılıklar
P_yes = yes_days / total_days
P_no = no_days / total_days

# Koşullu olasılıklar
P_H_Gunesli_yes = 2 / yes_days
P_H_Gunesli_no = 3 / no_days

P_S_Soguk_yes = 3 / yes_days
P_S_Soguk_no = 1 / no_days

P_R_Kuvvetli_yes = 3 / yes_days
P_R_Kuvvetli_no = 3 / no_days

P_N_Yuksek_yes = 3 / yes_days
P_N_Yuksek_no = 4 / no_days

# P(X | Evet) hesaplaması
P_X_given_yes = P_yes * P_H_Gunesli_yes * P_S_Soguk_yes * P_R_Kuvvetli_yes * P_N_Yuksek_yes

# P(X | Hayır) hesaplaması
P_X_given_no = P_no * P_H_Gunesli_no * P_S_Soguk_no * P_R_Kuvvetli_no * P_N_Yuksek_no

# Sonuçları yazdırma
print("P(X | Evet) =", P_X_given_yes)
print("P(X | Hayır) =", P_X_given_no)

if P_X_given_yes > P_X_given_no:
    print("Sonuç: Evet (Oyun oynanır)")
else:
    print("Sonuç: Hayır (Oyun oynanmaz)")
