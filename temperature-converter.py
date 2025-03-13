from nicegui import ui

ui.colors(
      primary= '#38b6ff',
      secondary= '#fcf7d9',
      accent= '#c946e0',
      positive= '#79c443',
      negative= '#c90e43',
      info= '#ffa6d5',
      warning= '#f7ce48'
)

def convert():
    try: 
        temp = float(input_field.value)
        if conversion_type.value == "Celsius to Fahrenheit":
            result_label.set_text(f"{temp}°C = {temp * 9/5 + 32:.2f}°F")
        else:
            result_label.set_text(f"{temp}°F = {(temp - 32) * 5/9:.2f}°C")
        result_label.classes("text-lg font-semibold text-positive mt-4")
        # text-positive: positive text color
    except ValueError:
        result_label.set_text("Please enter a valid number.")
        result_label.classes("text-lg font-semibold text-negative mt-4")
        # text-negative: negative text color

def convert_slider():
    temp = slider.value
    if slider_conversion.value == "Celsius to Fahrenheit":
        slider_result.set_text(f"{temp}°C = {temp * 9/5 + 32:.2f}°F")
    else:
        slider_result.set_text(f"{temp}°F = {(temp - 32) * 5/9:.2f}°C")
    slider_result.classes("text-lg font-semibold text-positive mt-4")

#ui.label("Temperature Converter").classes("text-2xl font-bold text-accent mb-4")
# text-2xl: Text size
# font-bold: Bold text
# text-accent: text in accent color
# mb-4: Margins

with ui.row().classes("mx-auto"):  
    with ui.card().classes("w-100 p-6 shadow-xl mx-auto mt-10 rounded-xl bg-secondary border"):
        ui.label("Temperature Converter").classes("text-accent text-bold text-xl mx-auto mt-4 mb-4")
        # w-100: Set element width to be fixed at 100
        # p-6: Padding
        # shadow-xl: Casts a shadow under the element
        # mx-auto: Margins, center
        # mt-10: Margins
        # rounded-xl: Borders, rounded edges of the element
        input_field = ui.input("Enter Temperature").props('type="number"').classes("w-full mb-4 p-2 text-lg border rounded bg-white")
        # w-full: width, full span of the page
        # border: applies solid border to the element
        # rounded: creates a rounded element, can choose which corner to apply it to
        conversion_type = ui.radio(["Celsius to Fahrenheit", "Fahrenheit to Celsius"], value="Celsius to Fahrenheit").classes("mb-4")
        convert_button = ui.button("Convert", on_click=convert).classes("text-white font-bold py-2 px-4 rounded mx-auto")
        # text-white: white text
        # py-2: Padding (vertical)
        # px-4: Padding (horizonatal)
        result_label = ui.label("").classes("text-lg mt-4 mx-auto")
    with ui.card().classes("w-100 p-6 shadow-xl mx-auto mt-10 rounded-xl border"):
        ui.label("Slider Converter").classes("text-info font-bold mx-auto text-xl mt-4")
        slider = ui.slider(min=-100, max=200, value=50, on_change=convert_slider)
        ui.label().bind_text_from(slider, 'value')
        slider_conversion = ui.radio(["Celsius to Fahrenheit", "Fahrenheit to Celsius"], value="Celsius to Fahrenheit").classes("mb-4")
        convert_button = ui.button("Convert", on_click=convert).classes("text-white font-bold py-2 px-4 rounded mx-auto")
        slider_result = ui.label("").classes("text-lg mt-4 mx-auto")

ui.run()