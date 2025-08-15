# Django Books API PowerShell Examples

## 1. Create a Book (No Auth, CSRF Exempt Example)
```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/books/api/books/create/" `
    -Method Post `
    -ContentType "application/json" `
    -Body '{"title": "New Book", "author": "Jane Doe", "published_date": "2024-08-12"}'
```

## 2. List All Books (GET Request)
```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/books/"
```

## 3. Create a Book with Token Authentication
```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/books/" `
    -Method Post `
    -ContentType "application/json" `
    -Headers @{Authorization="Token your_token_here"} `
    -Body '{"title": "Token Book", "author": "John Token", "published_date": "2024-08-12"}'
```

## 4. Obtain JWT Tokens
```powershell
$response = Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/token/" `
    -Method Post `
    -ContentType "application/json" `
    -Body '{"username":"user", "password":"123"}'
```

## 5. View JWT Tokens in Readable JSON
```powershell
$response | ConvertTo-Json -Depth 10
```
Example output:
```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc1NTM0NjY4NiwiaWF0IjoxNzU1MjYwMjg2LCJqdGkiOiJiMjhlZDJmMDU5YzI0NTIyOWJjMDM3OGU5MWVhOGVjZCIsInVzZXJfaWQiOiIyIn0.YZaBHk50IsojV84Gib6wPSQkLeslzLw77fTefLaGdHY",
    "access": "..."
}
```

## 6. Use JWT Access Token to GET Books
```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/books/" `
    -Headers @{Authorization="Bearer your_access_token_here"} |
    ConvertTo-Json -Depth 10
```

## 7. Use JWT Access Token to POST a New Book
```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/books/" `
    -Method Post `
    -ContentType "application/json" `
    -Headers @{Authorization="Bearer your_access_token_here"} `
    -Body '{"title": "JWT Book", "author": "JWT Author", "published_date": "2024-08-12"}'
```

## 8. Refresh JWT Token
Use your existing refresh token to get a new access token.
```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/token/refresh/" `
    -Method Post `
    -ContentType "application/json" `
    -Body '{"refresh":"<your_refresh_token_here>"}' |
    ConvertTo-Json -Depth 10
```

Use the new access token:
```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/books/" `
    -Headers @{Authorization="Bearer <your_new_access_token_here>"} |
    ConvertTo-Json -
```

## 9. Search by Title
```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/books/?search=Harry" `
    -Headers @{Authorization="Bearer <your_access_token>"} `
    | ConvertTo-Json -Depth 10
```
## 10. Order by Title (Ascending)
```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/books/?ordering=title" `
    -Headers @{Authorization="Bearer <your_access_token>"} `
    | ConvertTo-Json -Depth 10
```

## 11. Order by Title (Descending)
```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/books/?ordering=-title" `
    -Headers @{Authorization="Bearer <your_access_token>"} `
    | ConvertTo-Json -Depth 10
```

