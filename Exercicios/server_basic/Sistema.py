import psutil
import webbrowser
import os

class System:

    @staticmethod
    def comando(cmd) -> str:
        match cmd.split()[0]:
            case "/help":
                return "Ajuda Requisitada: \n\t /mem para ver a memoria\n\t /off para desligar\n\t /hd espaço em disco\n\t /google abrir o navegador"
            
            case "/hd":
                resposta = psutil.virtual_memory()
                return str(resposta)
            
            case "/mem":
                    if os.name == "nt":
                        caminho = "c:\\"
                    else: 
                        caminho = "/"
                    
                    resposta = psutil.disk_usage(caminho)
                    return str(resposta)
            
            case "/google":
                chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
                url = "https://laica.ifrn.edu.br/"
                webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
                webbrowser.get('chrome').open_new_tab(url)
                return "Abrindo Navegador"
            case "/ip":
                discart, ip1, ip2, mask = map(str,cmd.split())
                mask = int(mask)

                bin_IP1 = ''.join(bin(int(octet))[2:].zfill(8) for octet in ip1.split('.'))
                bin_IP2 = ''.join(bin(int(octet))[2:].zfill(8) for octet in ip2.split('.'))

                with_mask_IP1 = bin_IP1[:mask]
                with_mask_IP2 = bin_IP2[:mask]

                return str(with_mask_IP1 == with_mask_IP2)
            
            case _:
                return "Opção Inválida"