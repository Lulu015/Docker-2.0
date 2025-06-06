import smtplib
from email.message import EmailMessage

def enviar_email(destinatario, assunto, corpo):
    try:
        email = EmailMessage()
        email['From'] = 'seuemail@gmail.com'
        email['To'] = destinatario
        email['Subject'] = assunto
        email.set_content(corpo)
        
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('seuemail@gmail.com', 'SENHA_DO_APP')  # Utilize uma senha de aplicativo
            smtp.send_message(email)
        
        print(f"Email enviado com sucesso para {destinatario}")
        return True
        
    except Exception as e:
        print(f"Erro ao enviar email para {destinatario}: {str(e)}")
        return False

def processar_agendamento():
    usuarios = [
        {"nome": "Alice", "email": "alice@email.com"},
        {"nome": "Bruno", "email": "bruno@email.com"}
    ]
    
    # Enviar emails de agendamento recebido
    print("Enviando notificações de agendamento recebido...")
    for usuario in usuarios:
        sucesso = enviar_email(
            usuario["email"], 
            "Agendamento Recebido",
            f"Olá {usuario['nome']}, seu agendamento foi solicitado."
        )
        if sucesso:
            print(f"Agendamento solicitado para {usuario['nome']}")
    
    # Enviar emails de agendamento atendido
    print("\nEnviando notificações de agendamento atendido...")
    for usuario in usuarios:
        sucesso = enviar_email(
            usuario["email"], 
            "Agendamento Atendido",
            f"Olá {usuario['nome']}, seu agendamento foi concluído."
        )
        if sucesso:
            print(f"Agendamento atendido para {usuario['nome']}")

# Exemplo de uso
if __name__ == "__main__":
    processar_agendamento()