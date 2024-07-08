def create_endpoint_block(method, url, description, parameters, returns):
    # Create parameters block
    parameters_block = ""
    for param in parameters:
        parameters_block += f"""
            <div class="parameter">
                <code>{param['name']}</code> (тип: {param['type']}, обязательный: {param['required']}) - {param['description']}.
            </div>
        """

    # Create returns block
    returns_block = ""
    for ret in returns:
        returns_block += f"""
            <div class="return">
                <p><code>{ret['code']}</code> - {ret['message']}:</p>
                <pre><code>{ret['example']}</code></pre>
            </div>
        """

    # Combine all blocks
    endpoint_block = f"""
        <div class="endpoint">
            <h2><span class="method">{method}</span> <span class="url">{url}</span></h2>
            <div class="description">
                <p>{description}</p>
            </div>
            <div class="parameters">
                <h3>Параметры:</h3>
                {parameters_block}
            </div>
            <div class="returns">
                <h3>Возвращаемые данные:</h3>
                {returns_block}
            </div>
        </div>
    """
    return endpoint_block

def get_input_data():
    method = input("Введите метод (например, POST): ")
    url = input("Введите URL (например, /auth/change_user_access): ")
    description = input("Введите описание: ")

    parameters = []
    while True:
        param_name = input("Введите имя параметра (или нажмите Enter для завершения): ")
        if not param_name:
            break
        param_type = input(f"Введите тип параметра для {param_name}: ")
        param_required = input(f"Параметр {param_name} обязателен? (да/нет): ")
        param_description = input(f"Введите описание параметра {param_name}: ")
        parameters.append({
            'name': param_name,
            'type': param_type,
            'required': 'да' if param_required.lower() == 'да' else 'нет',
            'description': param_description
        })

    returns = []
    while True:
        return_code = input("Введите код ответа (или нажмите Enter для завершения): ")
        if not return_code:
            break
        return_message = input(f"Введите сообщение для кода ответа {return_code}: ")
        return_example = input(f"Введите пример JSON для кода ответа {return_code}: ")
        returns.append({
            'code': return_code,
            'message': return_message,
            'example': return_example
        })

    return method, url, description, parameters, returns

def main():
    html_start = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>URL endpoint auth</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        .container {
            width: 80%;
            margin: 0 auto;
            padding: 20px;
            background-color: #fff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1, h2, h3 {
            color: #333;
        }
        code {
            background-color: #eee;
            padding: 2px 4px;
            border-radius: 4px;
            font-family: Consolas, monospace;
        }
        .endpoint {
            margin: 20px 0;
        }
        .method {
            font-weight: bold;
            color: #2c3e50;
        }
        .url {
            font-size: 1.1em;
            color: #2980b9;
        }
        .description {
            margin: 10px 0;
            color: #555;
        }
        .parameters, .returns {
            margin: 20px 0;
            padding: 10px;
            background-color: #f9f9f9;
            border: 1px solid #ddd;
        }
        .parameters h3, .returns h3 {
            margin-top: 0;
        }
        .parameter, .return {
            margin: 10px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>URL endpoint auth</h1>
    """

    html_end = """
    </div>
</body>
</html>
    """

    # Gather input data
    method, url, description, parameters, returns = get_input_data()

    # Create HTML block for the endpoint
    endpoint_block = create_endpoint_block(method, url, description, parameters, returns)

    # Combine all parts of the HTML
    html_content = html_start + endpoint_block + html_end

    # Write to an HTML file
    with open("api_documentation.html", "w", encoding="utf-8") as file:
        file.write(html_content)

    print("Документация успешно создана и сохранена в файл 'api_documentation.html'")

if __name__ == "__main__":
    main()
