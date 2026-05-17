notes = []

def ajouter_note():
    note = input("✏️ Votre note : ")
    notes.append(note)
    print("✅ Note ajoutée !")

def voir_notes():
    if not notes:
        print("📭 Aucune note")
    else:
        for i, note in enumerate(notes):
            print(f"{i+1}. {note}")

def supprimer_note():
    voir_notes()
    try:
        choix = int(input("Numéro à supprimer : "))
        del notes[choix - 1]
        print("🗑️ Note supprimée")
    except:
        print("❌ Numéro invalide")

def menu():
    while True:
        print("\n📒 CARNET DE NOTES")
        print("1. Ajouter une note")
        print("2. Voir les notes")
        print("3. Supprimer une note")
        print("4. Quitter")
        choix = input("Votre choix : ")
        
        if choix == "1":
            ajouter_note()
        elif choix == "2":
            voir_notes()
        elif choix == "3":
            supprimer_note()
        elif choix == "4":
            print("👋 Au revoir !")
            break

if __name__ == "__main__":
    menu()