matriola1 = "s341046"
matricola2 = "s991088"

print(f"Mettere in ordine crescente le matricole {matriola1} e {matricola2}\n{matriola1 + ' --> ' + matricola2 if int(matriola1[1:]) >= int(matricola2[1:]) else matricola2 + ' --> ' + matriola1}")
