import html

from shiny import App, render, ui

# TODO Justify each line
# TODO Background color spacegray
# DONE Light mode/dark mode
# TODO Add Bhatkhande Notation
# DONE Add buy me a coffee link
# TODO Add about page

app_ui = ui.page_fluid(
    ui.page_sidebar(
    ui.sidebar(
        ui.input_select("swar_script", "Swar Notation using:", choices=["Devanaagri script", "Latin script"]),
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

swar_devanagri = [
    ".प ",
    ".ध ",
    ".नि ",
    ' सा ',
    ' रे ',
    ' गा ',
    ' म ',
    ' प ',
    ' ध ',
    ' नि ',
    " सा.",
    " रे.",
    " गा.",
    " म.",
    " प.",
]

swar_latin = [
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
]


def get_all_substrings(input_string, formula):
    max_digit = max([int(i) for i in formula])# find the max digit for last phrase

    text = ""
    for start_index in range(0, len(input_string) - max_digit + 1):
        for i in formula:
            text += input_string[start_index + int(i) - 1] + " "
        text += "<br>"
    return text

def server(input, output, session):
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
        if input.swar_script() == "Devanaagri script":
            title = {'aroha_heading': "* आरोह *",
                     'avaroha_heading': "* अवरोह *"}
            swar = swar_devanagri
        else:
            title = {'aroha_heading': "* Aroha *",
                     'avaroha_heading': "* Avaroha *"}
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
#app.run()
