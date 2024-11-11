import argparse
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
VIEW_FILE = os.path.join(current_dir, "app.py")
CRUD_FILE = os.path.join(current_dir, "util", "form", "crud.py")


def add_endpoint_to_view(endpoint_type: str, function_name: str, route: str):
    new_code = f"""
@app.{endpoint_type}("{route}")
async def {function_name}():
    result = await formService().{function_name}()
    return jsonify(result), 200
"""

    with open(VIEW_FILE, "r") as file:
        view_content = file.readlines()

    insert_position = None
    for i, line in enumerate(view_content):
        if 'if __name__ == "__main__":' in line:
            insert_position = i
            break

    if insert_position is not None:
        view_content.insert(insert_position, new_code.strip() + "\n\n")
    else:
        view_content.append(new_code.strip() + "\n")

    if route not in view_content:
        with open(VIEW_FILE, "w") as file:
            file.writelines(view_content)
        print(f"Endpoint {route} added to {VIEW_FILE}")
    else:
        print(f"Endpoint {route} already exists in {VIEW_FILE}")


def add_function_to_crud(function_name: str, function_body: str, crud_file: str = CRUD_FILE):
    # Properly indent the function body
    formatted_body = "\n".join(f"        {line}" for line in function_body.split("\\n"))

    # Construct the new function string
    new_function = f"""
    async def {function_name}(self):
{formatted_body}
    """

    # Read the existing CRUD file
    with open(crud_file, "r") as file:
        crud_content = file.readlines()

    # Check if the function already exists
    if any(f"async def {function_name}(" in line for line in crud_content):
        print(f"Function {function_name} already exists in {crud_file}")
        return

    # Find the position to insert the new function
    insert_position = None
    for i, line in enumerate(crud_content):
        if "self.session = session" in line:
            insert_position = i + 1
            break

    # Insert the new function at the identified position
    if insert_position is not None:
        crud_content.insert(insert_position, "\n")
        crud_content.insert(insert_position + 1, "    " + new_function.strip() + "\n")
    else:
        crud_content.append(new_function.strip() + "\n")

    # Write the modified content back to the CRUD file
    with open(crud_file, "w") as file:
        file.writelines(crud_content)

    print(f"Function {function_name} added to {crud_file}")


if __name__ == "__main__":
    # Setup argument parser
    parser = argparse.ArgumentParser(description="Add an endpoint and a CRUD function via command line.")
    
    parser.add_argument("--endpoint_type", required=True, help="Type of the endpoint (e.g., 'get', 'post').")
    parser.add_argument("--function_name", required=True, help="Name of the function to add.")
    parser.add_argument("--route", required=True, help="API route for the endpoint.")
    parser.add_argument("--function_file", required=True, help="The body of the function as a string.")
    
    args = parser.parse_args()

    add_endpoint_to_view(
        endpoint_type=args.endpoint_type,
        function_name=args.function_name,
        route=args.route,
    )

    add_function_to_crud(
        function_name=args.function_name,
        function_body=args.function_file,
    )