# If Else Conditional

is_old = True

if is_old:
    print("Es mayor.")
else:
    print("Es menor.")

# Elif Conditional

is_old = True
is_licenced = True

if is_old and is_licenced:
    print("Puede manejar.")
elif not is_old and not is_licenced:
    print("No puede manejar, porqué es menor de edad y no tiene licencia.")
elif is_old and not is_licenced:
    print("No puede manejar, porqué no tiene licencia.")
else:
    print("No puede manejar, porqué no tiene la mayoría de edad.")

# Ternary Conditional

message = "Es mayor de edad" if is_old else "No es mayor de edad"

print(message)