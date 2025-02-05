from shiny import App, reactive, render, ui

# TODO Background color spacegray
# TODO Add Bhatkhande Notation

SWAR_DEVANAGRI = [
    ".सा ",
    ".रे ",
    ".गा ",
    ".म ",
    ".प ",
    ".ध ",
    ".नि ",
    " सा ",
    " रे ",
    " गा ",
    " म ",
    " प ",
    " ध ",
    " नि ",
    " सा.",
    " रे.",
    " गा.",
    " म.",
    " प.",
    " ध.",
    " नि.",
    " सा..",
]

SWAR_LATIN = [
    ".S ",
    ".R ",
    ".G ",
    ".M ",
    ".P ",
    ".D ",
    ".N ",
    ' S ',
    ' R ',
    ' G ',
    ' M ',
    ' P ',
    ' D ',
    ' N ',
    " S.",
    " R.",
    " G.",
    " M.",
    " P.",
    " D.",
    " N.",
    " S..",
]

app_ui = ui.page_fluid(
    ui.page_sidebar(
    ui.sidebar(
        ui.input_select("swar_script", "Swar Notation using:", choices=["Devanagri script", "Latin script"]),
        
        ui.input_select("first_note", "First Note:", choices=[]),
        ui.input_select("last_note", "Last Note:", choices=[]),
        
        ui.input_numeric("formula_aroha", "Formula?", value=1234, min=1, max=10e10),
        ui.input_switch("aroha_avaroha_flag", "Aroha and Avaroha same formula?", value=True),
        ui.output_ui("conditional_input"),
        ui.input_slider("font_size", "Font Size", min=10, max=30, value=20),
        ui.div(
            ui.span("Light or Dark mode "),
            ui.input_dark_mode(),
        ),
    ),
    ui.output_ui("display_notation"),
    title="Paltan Practise Generator (Alankar Long Notation)",
))


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
        if input.swar_script() == "Devanagri script":
            swar_choices = SWAR_DEVANAGRI
            default_first_note = ".प "
        else:
            swar_choices = SWAR_LATIN
            default_first_note = ".P "
        ui.update_select("first_note", choices=swar_choices, selected=default_first_note)
    
    @reactive.Effect
    def update_swar_choices_last_note():
        if input.swar_script() == "Devanagri script":
            swar_choices = SWAR_DEVANAGRI
            default_last_note = " प."
        else:
            swar_choices = SWAR_LATIN
            default_last_note = " P."
        
        first_note = input.first_note()
        if first_note in swar_choices:
            swar_choices_last_note = swar_choices[swar_choices.index(first_note)+1:]
        else:
            swar_choices_last_note = swar_choices
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
        font_size = input.font_size()
        if input.swar_script() == "Devanagri script":
            title = {'aroha_heading': "* आरोह *",
                     'avaroha_heading': "* अवरोह *"}
            swar = SWAR_DEVANAGRI[SWAR_DEVANAGRI.index(str(input.first_note())):SWAR_DEVANAGRI.index(str(input.last_note()))+1]
        else:
            title = {'aroha_heading': "* Aroha *",
                     'avaroha_heading': "* Avaroha *"}
            swar = SWAR_LATIN[SWAR_LATIN.index(str(input.first_note())):SWAR_LATIN.index(str(input.last_note()))+1]
            
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
#app.run()
