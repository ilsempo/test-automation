import logging

def log_user_sorts_by(args, step_name):
    logging.info(f"\033[92m{step_name} \033[0m\033[36m-> {args[0]}\033[0m")

def log_fill_form(args, step_name):
    logging.info(f"\033[92m{step_name}\033[0m")
    data = args[0]
    max_key_length = max(len(key) for key in data)
    max_value_length = max(len(value) for value in data.values())
    for key, value in data.items():
        key_string = key.ljust(max_key_length)
        value_string = value.ljust(max_value_length)
        logging.info(f"\033[36m   | {key_string} -> {value_string} |\033[0m")

def log_user_clicks(args, step_name):
    logging.info(f"\033[92m{step_name}\033[0m\033[36m {args[0]}\033[0m\033[92m element\033[0m")

def log_login(args, step_name):
    user = args[0] if args else "valid"
    logging.info(f"\033[92m{step_name}\033[0m\033[36m {user}\033[0m\033[92m user\033[0m")

def log_message(args, step_name):
    logging.info(f"\033[36m{args[0]}\033[0m\033[92m {step_name}\033[0m")

def log_element_present(args, step_name):
    logging.info(f"\033[36m{args[0]}\033[0m\033[92m {step_name}\033[0m")

def log_user_access_page(args, step_name):
    logging.info(f"\033[92m{step_name}\033[0m\033[36m {args[0]}\033[0m\033[92m page by clicking\033[0m\033[36m {args[1]}\033[0m\033[92m element\033[0m")

def log_user_is_in_page(args, step_name):
    logging.info(f"\033[92m{step_name}\033[0m\033[36m {args[0]}\033[0m")

def log_switch_tab(args, step_name):
    logging.info(f"\033[92m{step_name}\033[0m\033[36m -> {args[0]}\033[0m")

def log_url_external(args, step_name):
    from utils.utils import get_url
    url_to_log = get_url(args[0])
    logging.info(f"\033[92m{step_name}\033[0m\033[36m -> {url_to_log}\033[0m")

def log_default(step_name):
    logging.info(f"\033[92m{step_name}\033[0m")

step_handlers = {
    "user_sorts_by": log_user_sorts_by,
    "fill_form_with_data": log_fill_form,
    "user_clicks": log_user_clicks,
    "login": log_login,
    "message_is_displayed": log_message,
    "element_present_in_page": log_element_present,
    "user_access_page": log_user_access_page,
    "user_is_in_page": log_user_is_in_page,
    "user_switches_to_tab": log_switch_tab,
    "validate_external_url": log_url_external
}

