def main():
    print("Anmeldung:")
    
    get_password()

def get_password():
    tries = 3
    
    while True:
        try:
            question = (
                "- Bitte geben Sie das Passwort ein ({} {} verbleiben): "
                .format(tries, "Versuche" if tries > 1 else "Versuch")
            )
            
            password = str(input(question))           
        except ValueError:
            print("- Bitte geben Sie eine gültige Antwort: ")
            continue
        
        print("")
        
        if (password == "Nixdorf"):
            print("Anmeldung erfolgreich!")
            break     
        else:
            tries -= 1
            
            if (tries > 0):      
                print("Das angegebene Passwort ist falsch.\n")
                continue            
            else:
                print("Zu viele Versuche, bitte kommen Sie später wieder.")
                break
                
main()
