class DashboardService:

    def carregar_dashboard(self):

        return {
            "proxima_aula": {
                "disciplina": "Estruturas de Dados",
                "horario": "08:00 - 10:00",
                "sala": "LAB 02"
            },

            "pendencias": [
                "Lista 3",
                "Projeto IA"
            ],

            "agenda_hoje": [
                "08:00 - Estruturas de Dados",
                "14:00 - Reunião PET"
                ]
            }
