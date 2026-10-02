import random

def gerar_mensagem_32bits():
    return ''.join([str(random.randint(0, 1)) for _ in range(32)])

def calcular_crc_passo_a_passo(mensagem):
    divisor = "1010111"
    r = 6
    
    dividendo = mensagem + ("0" * r)
    lista_dividendo = list(dividendo)
    
    print("\n CÁLCULO DO CRC (QUESTÃO 1) ---")
    print(f"Mensagem original (k bits): {mensagem}")
    print(f"Divisor (Polinômio Gerador): {divisor}")
    print(f"Dividendo (Mensagem + {r} zeros): {dividendo}\n")
    
    print("=== INÍCIO DA DIVISÃO (MÓDULO 2) ===")
    print(dividendo)
    
    for i in range(len(mensagem)):
        if lista_dividendo[i] == '1':
            print(" " * i + divisor)
            print(" " * i + "-" * len(divisor))
            
            for j in range(len(divisor)):
                lista_dividendo[i+j] = str(int(lista_dividendo[i+j]) ^ int(divisor[j]))
            
            resultado_parcial = "".join(lista_dividendo)
            print(" " * (i + 1) + resultado_parcial[i+1:])
            
    resto = "".join(lista_dividendo)[-r:]
    
    print("\n=== RESULTADO FINAL DA DIVISÃO ===")
    print(f"Resto da Divisão (FCS): {resto}")
    print(f"Mensagem a ser transmitida (T): {mensagem}{resto}")
    
    return resto

def exibir_esquema_lfsr():
    print("\n--- LFSR SIMPLIFICADO (QUESTÃO 2) ---")
    print("graph LR")
    print("    I(( I )) --> XOR_F((+))")
    print("    R5[R5] -->|Realimentação| XOR_F")
    print("    XOR_F --> R0[R0]")
    print("    R0 --> XOR_1((+))")
    print("    XOR_F -->|F| XOR_1")
    print("    XOR_1 --> R1[R1]")
    print("    R1 --> XOR_2((+))")
    print("    XOR_F -->|F| XOR_2")
    print("    XOR_2 --> R2[R2]")
    print("    R2 --> R3[R3]")
    print("    R3 --> XOR_4((+))")
    print("    XOR_F -->|F| XOR_4")
    print("    XOR_4 --> R4[R4]")
    print("    R4 --> R5")
    print("```")

def simular_lfsr_tabela(mensagem):
    r = [0, 0, 0, 0, 0, 0]
    
    entrada_completa = mensagem
    
    print("\n--- QUADRO DE EVOLUÇÃO DO LFSR (QUESTÃO 3) ---")
    print("| Ciclo | Entrada (I) | R5 | R4 | R3 | R2 | R1 | R0 |")
    print("|-------|-------------|----|----|----|----|----|----|")
    print(f"|   0   |      -      |  {r[5]} |  {r[4]} |  {r[3]} |  {r[2]} |  {r[1]} |  {r[0]} |")
    
    for i, bit_i in enumerate(entrada_completa):
        I = int(bit_i)
        
        F = r[5] ^ I
        
        r0_ant, r1_ant, r2_ant, r3_ant, r4_ant, r5_ant = r
        
        novo_r0 = F
        novo_r1 = r0_ant ^ F
        novo_r2 = r1_ant ^ F
        novo_r3 = r2_ant
        novo_r4 = r3_ant ^ F
        novo_r5 = r4_ant
        
        r = [novo_r0, novo_r1, novo_r2, novo_r3, novo_r4, novo_r5]
        
        print(f"|  {i+1:2d}   |      {I}      |  {r[5]} |  {r[4]} |  {r[3]} |  {r[2]} |  {r[1]} |  {r[0]} |")
        
    resto_lfsr = f"{r[5]}{r[4]}{r[3]}{r[2]}{r[1]}{r[0]}"
    print(f"\n=== RESULTADO FINAL (LFSR) ===")
    print(f"Resto obtido pelo simulador LFSR: {resto_lfsr}")
    
    return resto_lfsr

if __name__ == "__main__":
    mensagem_sorteada = "00001111010111100110110000101001"
    
    print("========================================")
    print("=== TRABALHO DE REDES: CÁLCULO CRC   ===")
    print("========================================")
    print(f"Mensagem Definida (32 bits): {mensagem_sorteada}")
    
    resto_divisao = calcular_crc_passo_a_passo(mensagem_sorteada)
    exibir_esquema_lfsr()
    resto_lfsr = simular_lfsr_tabela(mensagem_sorteada)
    
    print("\n========================================")
    print("=== VERIFICAÇÃO E CONCLUSÃO FINAL    ===")
    print("========================================")
    if resto_divisao == resto_lfsr:
        print(f"[SUCESSO] O resto matemático ({resto_divisao}) é IDÊNTICO ao hardware ({resto_lfsr})!")
    else:
        print("[ERRO] Os restos estão diferentes. Reveja a lógica.")