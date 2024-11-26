def same_network(ip1 : str, ip2 : str, mask : int) -> bool:
    ''' Verifica se dois IPs diferentes pertencem a mesma rede '''

    if not (0 <= mask <= 32):
        raise ValueError("mascara invalida!")
    
    # separa os octetos e converte para binario
    """ zfill usado para garantir que seja em 8 bits """
    """ bin converte para binario """
    """ '[2:]' para remover os 2 caracteres do binario """
    """ join junta os octetos binarios com o parametro ''(nada) """
    bin_IP1 = ''.join(bin(int(octet))[2:].zfill(8) for octet in ip1.split('.'))
    bin_IP2 = ''.join(bin(int(octet))[2:].zfill(8) for octet in ip2.split('.'))

    # aplica a mascara nos IPs
    """ fatia os binarios usando a mascara, preservando apenas os 24 bits a esquerda  """
    with_mask_IP1 = bin_IP1[:mask]
    with_mask_IP2 = bin_IP2[:mask]

    return with_mask_IP1 == with_mask_IP2

if same_network(ip1 = input('digite o primeiro ip: '), ip2 = input('digite o segundo ip: '), mask = int(input('digite a mascara: '))):
    print("são da mesma rede")
else:
    print("\nnão são da mesma rede")
