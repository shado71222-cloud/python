from training.general.defs_c3 import Utils_jb61

user_1 = {
    "first_name": "John",
    "last_name": "Doe",
    "email": "abc@abc.com",
    "age": 42
}

user_2 = {
    "first_name": "John",
    "last_name": "Wick",
    "email": "john@abccom",
    "age": 16
}
utility=Utils_jb61()
utility.email_validator(user_1["email"])
utility.email_validator(user_2["email"])