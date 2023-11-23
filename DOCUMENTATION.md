# Email Service API Documentation

## Introduction

This documentation provides information on the usage of the Email Service API, which allows you to send emails through a Flask application.

## Table of Contents

1. [Setup](#setup)
2. [Endpoint](#endpoint)
3. [Request Parameters](#request-parameters)
4. [Responses](#responses)
5. [Example](#example)

## Setup<a name="setup"></a>

Ensure you have the required Python packages installed. You can install them using the following:

```bash
pip install Flask Flask-Mail Flask-Restful Flask-Swagger
```

Make sure to set the environment variable `MAIL_PASSWORD` with the email account password.

## Endpoint<a name="endpoint"></a>

- **Endpoint URL:** `/send_email`
- **HTTP Method:** POST

## Request Parameters<a name="request-parameters"></a>

The `/send_email` endpoint expects the following parameters in the form data:

1. **subject** (type: string, required): The subject of the email.
2. **recipient** (type: string, required): The email address of the recipient.
3. **body** (type: string, required): The body content of the email.

## Responses<a name="responses"></a>

- **200 OK:** Email sent successfully.
- **400 Bad Request:** Missing required fields.
- **500 Internal Server Error:** An error occurred during the email sending process.

## Example<a name="example"></a>

### Request

```bash
curl -X POST http://localhost:5000/send_email -F "subject=Hello" -F "recipient=example@email.com" -F "body=This is a test email."
```

### Response (Success)

```json
{
  "message": "Email sent successfully"
}
```

### Response (Bad Request)

```json
{
  "error": "Missing required fields"
}
```

### Response (Internal Server Error)

```json
{
  "error": "Internal Server Error Message"
}
```

## Conclusion

This API provides a simple interface for sending emails via a Flask application. Ensure that you provide the required parameters for successful email delivery.
