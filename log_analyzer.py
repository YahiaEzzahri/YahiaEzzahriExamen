from colorama import Fore, Style, init
init()

def analyser_log(fichier_log, fichier_rapport):
    nb_info = nb_warning = nb_error = 0

    with open(fichier_log, 'r') as f:
        for ligne in f:
            if 'INFO' in ligne:
                nb_info += 1
            elif 'WARNING' in ligne:
                nb_warning += 1
            elif 'ERROR' in ligne:
                nb_error += 1

    with open(fichier_rapport, 'w') as f:
        f.write(f"Statistiques des logs :\n")
        f.write(f"INFO : {nb_info}\n")
        f.write(f"WARNING : {nb_warning}\n")
        f.write(f"ERROR : {nb_error}\n")

    print(Fore.GREEN + "Rapport généré avec succès." + Style.RESET_ALL)
