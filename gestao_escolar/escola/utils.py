from django.contrib import messages
from django.core.exceptions import ValidationError

class GerenciadorMensagem:

    @staticmethod
    def processar_mensagem_erro(request, validation_error):
        mensagens_unicas = set()

        if isinstance(validation_error, ValidationError):
            if hasattr(validation_error, "message_dict") and validation_error.message_dict:
                for campo, erros in validation_error.message_dict.items():
                    if isinstance(erros, list):
                        for erro in erros:
                            mensagens_unicas.add(f"{campo.title()}: {erro}")
                    else:
                        mensagens_unicas.add(f"{campo.title()}: {erros}")

            elif hasattr(validation_error, "messages") and validation_error.messages:
                for erro in validation_error.messages:
                    mensagens_unicas.add(str(erro))
            else:
                mensagens_unicas.add(str(validation_error))
        else:
            mensagens_unicas.add(str(validation_error))

        for mensagem in mensagens_unicas:
            messages.error(request, mensagem)

    @staticmethod
    def processar_mensagem_sucesso(request, mensagem):
        if isinstance(mensagem, str):
            messages.success(request, mensagem)
        elif isinstance(mensagem, list):
            mensagens_unicas = list(set(mensagem))
            for msg in mensagens_unicas:
                messages.success(request, msg)
        else:
            raise ValueError("A mensagem deve ser uma string ou uma lista de strings.")
