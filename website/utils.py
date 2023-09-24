from bson import ObjectId

def convert_to_object_id(value):
    try:
        # Attempt to convert the value to ObjectId
        object_id = ObjectId(value)
        return object_id
    except Exception as e:
        # Handle the exception or log it as needed
        print(f"Error converting '{value}' to ObjectId: {str(e)}")
        return None  # You can return None or raise an exception here
