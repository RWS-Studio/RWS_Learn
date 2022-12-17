from grades_manager import GradesManager

GradesManager = GradesManager()

GradesManager.add_subject("Anglais")
print("create")
GradesManager.add_grade("Anglais", 7, 0.5, "Commentaire", 10)
print("add commentaire")
GradesManager.add_grade("Anglais", 18, 0.5, "Dissertation")
print("add dissertation")
GradesManager.add_grade("Anglais", 10, 1, "A del")
print("add a del")
GradesManager.del_grade("Anglais", 3)
print("del")
GradesManager.update_grade("Anglais", 14, 1, "Commentaire", 1)
print("update")
print("\nFinished")
