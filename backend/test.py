import json


def convert_to_json_parsable(input_str):
    try:
        # Convert the string to a JSON object
        json_data = json.loads(input_str)
    except json.JSONDecodeError:
        # If it fails, we'll escape the string and return it as JSON
        input_str = input_str.replace("\n", "\\n")
        json_data = {"value": input_str}

    return json.dumps(json_data)


input_str = """
        try:
            users = self.session.query(UserSignUP).all()
            if not users:
                return {"message": "No users found"}, 404
            
            return [user.to_dict() for user in users]
        except Exception as exception:
            return {"message": f"Error retrieving users: {str(exception)}"}"""

json_parsable = convert_to_json_parsable(input_str)
print(json_parsable)


