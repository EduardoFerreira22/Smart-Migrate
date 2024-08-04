import gui.app_instance as app_instance # Importe o módulo que você criou

def configurar_interface_banco_de_dados(servidor='', user='', password='', db_name='', port='', 
                                        conectar_visible=True, buscar_sqlite_visible=False, 
                                        user_visible=True, password_visible=True, db_name_visible=True, 
                                        port_visible=True):
    ui = app_instance.get_ui_instance()
    ui.txt_servidor_data_base.setText(servidor)
    ui.txt_user_data_base.setText(user)
    ui.txt_password_data_base.setText(password)
    ui.txt_data_base_name.setText(db_name)
    ui.txt_port_data_base.setText(port)

    ui.bt_conectar_data_base.setVisible(conectar_visible)
    ui.bt_buscar_sqlite.setVisible(buscar_sqlite_visible)
    ui.txt_user_data_base.setVisible(user_visible)
    ui.txt_password_data_base.setVisible(password_visible)
    ui.txt_data_base_name.setVisible(db_name_visible)
    ui.txt_port_data_base.setVisible(port_visible)

def configurar_interface(combo1_visible, combo2_visible, combo3_visible, combo4_visible, 
                         bt_setas1_visible, bt_setas2_visible,bt_setas3_visible, txt_opcao1_visible, txt_opcao2_visible, 
                         txt_opcao3_visible, txt_opcao4_visible, bt_add_opcoes2_visible, bt_add_opcoes3_visible, 
                         bt_retirar_opcoes2_visible, bt_retirar_opcoes3_visible, bt_processamento_de_para_visible, 
                         txt_opcao1_placeholder, txt_opcao2_placeholder, 
                         txt_opcao3_placeholder, txt_opcao4_placeholder):
    ui = app_instance.get_ui_instance()
    ui.combo1_colunas_processamento.setVisible(combo1_visible)
    ui.combo2_colunas_processamento.setVisible(combo2_visible)
    ui.combo3_colunas_processamento.setVisible(combo3_visible)
    ui.combo4_colunas_processamento.setVisible(combo4_visible)
    ui.bt_setas1.setVisible(bt_setas1_visible)
    ui.bt_setas2.setVisible(bt_setas2_visible)
    ui.bt_setas3.setVisible(bt_setas3_visible)
    ui.txt_opcao1_processamento.setVisible(txt_opcao1_visible)
    ui.txt_opcao2_processamento.setVisible(txt_opcao2_visible)
    ui.txt_opcao3_processamento.setVisible(txt_opcao3_visible)
    ui.txt_opcao4_processamento.setVisible(txt_opcao4_visible)
    ui.bt_add_opcoes2.setVisible(bt_add_opcoes2_visible)
    ui.bt_add_opcoes3.setVisible(bt_add_opcoes3_visible)
    ui.bt_retirar_opcoes2.setVisible(bt_retirar_opcoes2_visible)
    ui.bt_retirar_opcoes3.setVisible(bt_retirar_opcoes3_visible)
    ui.bt_processamento_de_para.setVisible(bt_processamento_de_para_visible)
    ui.txt_opcao1_processamento.setPlaceholderText(txt_opcao1_placeholder)
    ui.txt_opcao2_processamento.setPlaceholderText(txt_opcao2_placeholder)
    ui.txt_opcao3_processamento.setPlaceholderText(txt_opcao3_placeholder)
    ui.txt_opcao4_processamento.setPlaceholderText(txt_opcao4_placeholder)


def configurar_busca_interface(frame_visible, bt_busca_visible, bt_extrair_duplicados_visible, txt_busca_visible, inteligente_visible, combo1, placeholder=''):
    ui = app_instance.get_ui_instance()
    ui.frame_analise_inteligente.setVisible(frame_visible)
    ui.bt_buscar_op_busca.setVisible(bt_busca_visible)
    ui.bt_extrair_duplicados.setVisible(bt_extrair_duplicados_visible)
    ui.txt_opcoes_busca.setVisible(txt_busca_visible)
    ui.frame_analise_inteligente.setVisible(inteligente_visible)
    ui.txt_opcoes_busca.clear()
    ui.combo1_colunas_opcoes_busca.setVisible(combo1)

    # Verifica se o placeholder é uma string
    if isinstance(placeholder, str):
        ui.txt_opcoes_busca.setPlaceholderText(placeholder)
    else:
        ui.txt_opcoes_busca.setPlaceholderText("")


num_opcoes_adicionadas = 0
def atualizar_interface():

        global num_opcoes_adicionadas
        global visible_combos

        visibilidade = {
            'combo1': True,
            'combo2': True,
            'combo3': False,
            'combo4': False,
            'bt_setas1': True,
            'bt_setas2': False,
            'bt_setas3': False,
            'txt_opcao1': True,
            'txt_opcao2': True,
            'txt_opcao3': False,
            'txt_opcao4': False,
            'bt_add_opcoes2': True,
            'bt_add_opcoes3': False,
            'bt_retirar_opcoes2': False,
            'bt_retirar_opcoes3': False,
            'bt_processamento_de_para': True,
            
        }
        
        placeholder = {
            'txt_opcao1': "De",
            'txt_opcao2': "Para",
            'txt_opcao3': "",
            'txt_opcao4': ""
        }

        if num_opcoes_adicionadas == 1:
            visibilidade.update({
                'combo1': True,
                'combo2': True,
                'combo3': True,
                'bt_setas1': True,
                'bt_setas2': True,
                'bt_setas3': False,
                'txt_opcao1': True,
                'txt_opcao2': True,
                'txt_opcao3': True,
                'txt_opcao4': False,
                'bt_add_opcoes2': False,
                'bt_add_opcoes3': True,
                'bt_retirar_opcoes2': True,
                'bt_retirar_opcoes3': False,
                'bt_processamento_de_para': True,
       
            })
            placeholder.update({
                'txt_opcao1': "De",
                'txt_opcao2': "Para",
                'txt_opcao3': "Para"
            })
            
        elif num_opcoes_adicionadas == 2:
            visibilidade.update({
                'combo1': True,
                'combo2': True,
                'combo3': True,
                'combo4': True,
                'bt_setas1': True,
                'bt_setas2': True,
                'bt_setas3': True,
                'txt_opcao1': True,
                'txt_opcao2': True,
                'txt_opcao3': True,
                'txt_opcao4': True,
                'bt_add_opcoes2': False,
                'bt_add_opcoes3': False,
                'bt_retirar_opcoes2': True,
                'bt_retirar_opcoes3': True,
                'bt_processamento_de_para': True,
            })
            placeholder.update({
                'txt_opcao1': "De",
                'txt_opcao2': "Para",
                'txt_opcao3': "Para",
                'txt_opcao4': "Para"
            })
            
        elif num_opcoes_adicionadas == 3:
            visibilidade.update({
                'combo1': True,
                'combo2': True,
                'combo3': True,
                'combo4': False,
                'bt_setas1': True,
                'bt_setas2': True,
                'bt_setas3': True,
                'txt_opcao1': True,
                'txt_opcao2': True,
                'txt_opcao3': True,
                'txt_opcao4': False,
                'bt_add_opcoes2': False,
                'bt_add_opcoes3': True,
                'bt_retirar_opcoes2': True,
                'bt_retirar_opcoes3': True,
                'bt_processamento_de_para': True,

            })
            placeholder.update({
                'txt_opcao1': "De",
                'txt_opcao2': "Para",
                'txt_opcao3': "Para"
            })
            
        elif num_opcoes_adicionadas == 4:
            visibilidade.update({
                'combo1': True,
                'combo2': True,
                'combo3': True,
                'combo4': True,
                'bt_setas1': True,
                'bt_setas2': True,
                'bt_setas3': True,
                'txt_opcao1': True,
                'txt_opcao2': True,
                'txt_opcao3': True,
                'txt_opcao4': True,
                'bt_add_opcoes2': True,
                'bt_add_opcoes3': False,
                'bt_retirar_opcoes2': True,
                'bt_retirar_opcoes3': True,
                'bt_processamento_de_para': True,

            })
            placeholder.update({
                'txt_opcao1': "De",
                'txt_opcao2': "Para",
                'txt_opcao3': "Para",
                'txt_opcao4': "Para"
            })
        
        # Aplicar a visibilidade e placeholders
        configurar_interface(
            visibilidade['combo1'],
            visibilidade['combo2'],
            visibilidade['combo3'],
            visibilidade['combo4'],
            visibilidade['bt_setas1'],
            visibilidade['bt_setas2'],
            visibilidade['bt_setas3'],
            visibilidade['txt_opcao1'],
            visibilidade['txt_opcao2'],
            visibilidade['txt_opcao3'],
            visibilidade['txt_opcao4'],
            visibilidade['bt_add_opcoes2'],
            visibilidade['bt_add_opcoes3'],
            visibilidade['bt_retirar_opcoes2'],
            visibilidade['bt_retirar_opcoes3'],
            visibilidade['bt_processamento_de_para'],
            placeholder['txt_opcao1'],
            placeholder['txt_opcao2'],
            placeholder['txt_opcao3'],
            placeholder['txt_opcao4']
        )

def adicionar_opcoes():
    global num_opcoes_adicionadas
    num_opcoes_adicionadas += 1
    atualizar_interface()

def remover_opcoes():
    global num_opcoes_adicionadas
    if num_opcoes_adicionadas > 0:
        num_opcoes_adicionadas -= 1
        atualizar_interface()