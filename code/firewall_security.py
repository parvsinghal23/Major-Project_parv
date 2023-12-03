import re

# Define a function to check for security issues in submitted data
def security_scan(data):
    # Look for HTML script tags/cross-site scripting attacks
    if re.search("(\<(script)\>)", data):
        return False

    # Check for common SQL injection attacks
    if re.search("((\%27)|(\')|(\-\-)|(\%23))[^\n]*((\%27)|(\')|(\-\-)|(\%23))", data):
        return False
    
    # Look for sensitive data being transmitted or stored in an unencrypted format
    elif re.search(r'\b(password|123456|qwerty|abc123|letmein|monkey|football|iloveyou|admin|welcome|login|princess|sunshine|flower|hottie|loveme|zaq1zaq1|baseball|dragon|superman)\b', data, re.IGNORECASE):
        return False
        
    # Look for various potential attacks using special characters
   
    elif re.search("';'", data):
        return False
    elif re.search('";"', data):
        return False
    elif re.search(r"((\%3D)|(=))[^\n]*((\%27)|(\')|(\-\-)|(\%3B)|(;))", data):
        return False
    elif re.search("--", data):
        return False
    elif re.search("\*", data):
        return False
    elif re.search("\|", data):
        return False

    # checks that the email address string has a valid format
    # elif not re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', data):
    #     return False


    # Check for path traversal attacks
    # elif re.search("\.\./", data):
    #     return False

   
    # If no potential security issues are found, return True
    else:
        return True
       

def security_scan_2(data):
    # Look for proxy address
    if re.search(r'(?i)(?<![\d.])(?:\d{1,3}\.){3}\d{1,3}(?::\d+)?(?![\d.])', data):
        return False
    # checks that the email address string has a valid format
    elif not re.search(r'^[a-zA-Z0-9_+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$', data):
        return False
    # limits the input data length to 10,000 characters
    # prevent buffer overflow attacks
    elif len(data) > 10000:
        return False
    

    # Check for insecure communications
    elif re.search(r'\b(http|ftp)\://', data, re.IGNORECASE):
        return False

    # Check for command injection attacks
    elif re.search(r'(?i)(\b(echo|exec|passthru|shell_exec|system|popen|proc_open|pcntl_exec)\b)|([\'\"]\s*(\||&|\$|`|<|>)\s*[\'\"])', data):
        return False
    # Check for LDAP injection attacks
    elif re.search(r"(?i)(\b(ALLOWED_ATTRS|AUTH_ATTRS|BIND_AUTH_DN|BIND_DN|BIND_PASSWORD|DEFAULT_MAIL_DOMAIN|DEFAULT_SEARCH_BASE|DELETE_ATTRS|FILTER)|([\'\"]\s*\*\s*[\'\"]))", data):
        return False
    # Check for XML injection attacks
    elif re.search(r"(?i)(\b(XPATH|XQUERY|XML)\b)|([\'\"]\s*<\s*/?\s*\w+\s*>?\s*[\'\"])", data):
        return False

    # Check for unused features
    elif re.search("(debug|test)", data, re.IGNORECASE):
        return False
    
    # Look for URLs pointing to internal or private IP addresses
    elif re.search(r'(http|https):\/\/((10|127)\.\d{1,3}\.\d{1,3}\.\d{1,3})|((172\.(1[6-9]|2\d|3[0-1])|192\.168)\.\d{1,3}\.\d{1,3})(:\d+)?(\/[^\s]*)?', data):
        return False
    
    # Check for XML External Entities (XXE) attacks
    elif re.search(r'<!ENTITY', data):
        return False
    elif re.search(r'<\!DOCTYPE', data):
        return False
    elif re.search("((\%3C)|<)[^(\%3E)|>]+((\%3E)|>)", data):
        return False
    elif re.search("((\%3C)|<)[^\n]+((\%3E)|>)", data):
        return False

    # If no potential security issues are found, return True
    else:
        return True