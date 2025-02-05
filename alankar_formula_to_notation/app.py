from shiny import App, reactive, render, ui

# TODO Add Bhatkhande Notation

def komal(text):
    return "".join(f"<u>{char}</u>" if char.strip() else char for char in text)
def tivra(text):
    return f"{text}\'"

THAAT_SWAR_DEVANAGRI_DICT = {
    'Bilawal thaat': [".सा ",".रे ",".गा ",".म ",".प ",".ध ",".नि "," सा "," रे "," गा "," म "," प "," ध "," नि "," सा."," रे."," गा."," म."," प."," ध."," नि."," सा.."],
    'Kalyan thaat': [".सा ",".रे ",".गा ",".म' ",".प ",".ध ",".नि "," सा "," रे "," गा "," म' "," प "," ध "," नि "," सा."," रे."," गा."," म'."," प."," ध."," नि."," सा.."],
    'Khamaj thaat': [".सा ",".रे ",".गा ",".म ",".प ",".ध ",komal(".नि ")," सा "," रे "," गा "," म "," प "," ध ",komal(" नि ")," सा."," रे."," गा "," म."," प."," ध.",komal(" नि.")," सा.."], 
    'Kafi thaat': [".सा ",".रे ",komal(".गा "),".म ",".प ",".ध ",komal(".नि ")," सा "," रे ",komal(" गा ")," म "," प "," ध ",komal(" नि ")," सा."," रे.",komal(" गा.")," म."," प."," ध.",komal(" नि.")," सा.."],
    'Asavari thaat': [".सा ",".रे ",komal(".गा "),".म ",".प ",komal(".ध "),komal(".नि ")," सा "," रे ",komal(" गा ")," म "," प ",komal(" ध "),komal(" नि ")," सा."," रे.",komal(" गा.")," म."," प.",komal(" ध."),komal(" नि.")," सा.."],
    'Bhairavi thaat': [".सा ",komal(".रे "),komal(".गा "),".म ",".प ",komal(".ध "),komal(".नि ")," सा ",komal(" रे "),komal(" गा ")," म "," प ",komal(" ध "),komal(" नि ")," सा.",komal(" रे."),komal(" गा.")," म."," प.",komal(" ध."),komal(" नि.")," सा.."],
    'Bhairav thaat': [".सा ",komal(".रे "),".गा ",".म ",".प ",komal(".ध "),".नि "," सा ",komal(" रे ")," गा "," म "," प ",komal(" ध ")," नि "," सा.",komal(" रे.")," गा."," म."," प.",komal(" ध.")," नि."," सा.."],
    'Marwa thaat': [".सा ",komal(".रे "),".गा ",".म' ",".प ",".ध ",".नि "," सा ",komal(" रे ")," गा "," म' "," प "," ध "," नि "," सा.",komal(" रे.")," गा."," म'."," प."," ध."," नि."," सा.."],
    'Purvi thaat': [".सा ",komal(".रे "),".गा ",".म' ",".प ",komal(".ध "),".नि "," सा ",komal(" रे ")," गा "," म' "," प ",komal(" ध ")," नि "," सा.",komal(" रे.")," गा."," म'."," प.",komal(" ध.")," नि."," सा.."],
    'Todi thaat': [".सा ",komal(".रे "),komal(".गा "),".म' ",".प ",komal(".ध "),".नि "," सा ",komal(" रे "),komal(" गा ")," म' "," प ",komal(" ध ")," नि "," सा.",komal(" रे."),komal(" गा.")," म'."," प.",komal(" ध.")," नि."," सा.."], 
}

THAAT_SWAR_LATIN_DICT = {
    'Bilawal thaat': [".S ",".R ",".G ",".M ",".P ",".D ",".N "," S "," R "," G "," M "," P "," D "," N "," S."," R."," G."," M."," P."," D."," N."," S.."],
    'Kalyan thaat': [".S ",".R ",".G ",".M' ",".P ",".D ",".N "," S "," R "," G "," M' "," P "," D "," N "," S."," R."," G."," M'."," P."," D."," N."," S.."],
    'Khamaj thaat': [".S ",".R ",".G ",".M ",".P ",".D ",komal(".N ")," S "," R "," G "," M "," P "," D ",komal(" N ")," S."," R."," G "," M."," P."," D.",komal(" N.")," S.."],
    'Kafi thaat': [".S ",".R ",komal(".G "),".M ",".P ",".D ",komal(".N ")," S "," R ",komal(" G ")," M "," P "," D ",komal(" N ")," S."," R.",komal(" G.")," M."," P."," D.",komal(" N.")," S.."],
    'Asavari thaat': [".S ",".R ",komal(".G "),".M ",".P ",komal(".D "),komal(".N ")," S "," R ",komal(" G ")," M "," P ",komal(" D "),komal(" N ")," S."," R.",komal(" G.")," M."," P.",komal(" D."),komal(" N.")," S.."],
    'Bhairavi thaat': [".S ",komal(".R "),komal(".G "),".M ",".P ",komal(".D "),komal(".N ")," S ",komal(" R "),komal(" G ")," M "," P ",komal(" D "),komal(" N ")," S.",komal(" R."),komal(" G.")," M."," P.",komal(" D."),komal(" N.")," S.."],
    'Bhairav thaat': [".S ",komal(".R "),".G ",".M ",".P ",komal(".D "),".N "," S ",komal(" R ")," G "," M "," P ",komal(" D ")," N "," S.",komal(" R.")," G."," M."," P.",komal(" D.")," N."," S.."],
    'Marwa thaat': [".S ",komal(".R "),".G ",".M' ",".P ",".D ",".N "," S ",komal(" R ")," G "," M' "," P "," D "," N "," S.",komal(" R.")," G."," M'."," P."," D."," N."," S.."],
    'Purvi thaat': [".S ",komal(".R "),".G ",".M' ",".P ",komal(".D "),".N "," S ",komal(" R ")," G "," M' "," P ",komal(" D ")," N "," S.",komal(" R.")," G."," M'."," P.",komal(" D.")," N."," S.."],
    'Todi thaat': [".S ",komal(".R "),komal(".G "),".M' ",".P ",komal(".D "),".N "," S ",komal(" R "),komal(" G ")," M' "," P ",komal(" D ")," N "," S.",komal(" R."),komal(" G.")," M'."," P.",komal(" D.")," N."," S.."],
}
    
app_ui = ui.page_fluid(
    ui.page_sidebar(
        ui.sidebar(
            ui.input_select("swar_script", "Swar Notation using:", choices=["Devanagri script", "Latin script"]),
            ui.input_numeric("formula_aroha", "Formula?", value=1234, min=1, max=10e10),
            ui.input_slider("font_size", "Font Size", min=10, max=30, value=20),
            ui.div(
                # ui.span("Light or Dark mode "),
                ui.input_dark_mode(),
            ),
            ui.accordion(
                ui.accordion_panel(
                    "More Options",
                    ui.input_select("thaat", "Thaat:", choices=list(THAAT_SWAR_DEVANAGRI_DICT.keys()), selected="Bilawal thaat"),
                    ui.input_select("first_note", "First Note:", choices=[]),
                    ui.input_select("last_note", "Last Note:", choices=[]),
                    ui.input_switch("aroha_avaroha_flag", "Aroha and Avaroha same formula?", value=True),
                    ui.output_ui("conditional_input"),
                    
                ),
                open=False  # Initially collapsed
            ),
        ),
        ui.output_ui("display_notation"),
        title="Paltan Practise Generator (Alankar Long Notation)",
    )
)


def get_all_substrings(input_string, formula):
    max_digit = max([int(i) for i in formula])# find the max digit for last phrase
    text = ""
    for start_index in range(0, len(input_string) - max_digit + 1):
        for i in formula:
            text += input_string[start_index + int(i) - 1] + " "
        text += "<br>"
    return text

def server(input, output, session):
    @reactive.Effect
    def update_swar_choices_first_note():
        thaat = input.thaat()
        if input.swar_script() == "Devanagri script":
            thaat_swar = THAAT_SWAR_DEVANAGRI_DICT[thaat]
            default_first_note = ".प "
        else:
            thaat_swar = THAAT_SWAR_LATIN_DICT[thaat]
            default_first_note = ".P "
        ui.update_select("first_note", choices=[ui.HTML(note) for note in thaat_swar], selected=default_first_note)
    
    @reactive.Effect
    def update_swar_choices_last_note():
        thaat = input.thaat()
        if input.swar_script() == "Devanagri script":
            thaat_swar = THAAT_SWAR_DEVANAGRI_DICT[thaat]
            default_last_note = " प."
        else:
            thaat_swar = THAAT_SWAR_LATIN_DICT[thaat]
            default_last_note = " P."
        first_note = input.first_note()
        if first_note in thaat_swar:
            swar_choices_last_note = thaat_swar[thaat_swar.index(first_note)+1:]
        else:
            swar_choices_last_note = thaat_swar
        ui.update_select("last_note", choices=swar_choices_last_note, selected=default_last_note)
        
    @output
    @render.ui
    def conditional_input():
        if not input.aroha_avaroha_flag():
            return ui.input_numeric("formula_avaroha", "Avaroha Formula?", value=1234, min=1, max=10e10)
        return None
    
    @output
    @render.ui
    def display_notation():
        thaat = input.thaat()
        font_size = input.font_size()
        first_note = input.first_note()
        last_note = input.last_note()
        if input.swar_script() == "Devanagri script":
            title = {'aroha_heading': "* आरोह *",
                     'avaroha_heading': "* अवरोह *"}
            swar_devanagri = THAAT_SWAR_DEVANAGRI_DICT[thaat]
            if first_note in swar_devanagri:
                swar = swar_devanagri[swar_devanagri.index(first_note):swar_devanagri.index(last_note)+1]
            else:
                swar = swar_devanagri
        else:
            title = {'aroha_heading': "* Aroha *",
                     'avaroha_heading': "* Avaroha *"}
            swar_latin = THAAT_SWAR_LATIN_DICT[thaat]
            if first_note in swar_latin:
                swar = swar_latin[swar_latin.index(first_note):swar_latin.index(last_note)+1]
            else:
                swar = swar_latin
            
        if input.aroha_avaroha_flag():
            aroha_text = get_all_substrings(swar, str(input.formula_aroha()))
            avaroha_text = get_all_substrings(swar[::-1], str(input.formula_aroha()))
        else:
            aroha_text = get_all_substrings(swar, str(input.formula_aroha()))
            avaroha_text = get_all_substrings(swar[::-1], str(input.formula_avaroha()))
        
        combined_output = f"""
                        <div style="display: flex; justify-content: center; font-size: {font_size}px;">
                            <div style="flex: 1; padding: 10px; text-align: center; border: 1px solid black; margin-right: 10px;">
                                {f"<b style='font-size: {font_size+2}px;'>{title['aroha_heading']}</b><br><br>"}
                                {aroha_text}
                            </div>
                            <div style="flex: 1; padding: 10px; text-align: center; border: 1px solid black; margin-left: 10px;">
                                {f"<b style='font-size: {font_size+2}px;'>{title['avaroha_heading']}</b><br><br>"}
                                {avaroha_text}
                            </div>
                        </div>
                        """
        return ui.HTML(combined_output)

app = App(app_ui, server)