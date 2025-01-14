import pytest
from fastapi.testclient import TestClient
from backend.main import app
import io
import pandas as pd

client = TestClient(app)

@pytest.mark.backend
def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

@pytest.mark.backend
def test_upload_csv():
    # Create a mock CSV file
    csv_content = "name,age\nJohn,30\nJane,25"
    files = {
        'file': ('test.csv', io.BytesIO(csv_content.encode()), 'text/csv')
    }
    
    response = client.post("/upload", files=files)
    assert response.status_code == 200
    
    data = response.json()
    assert "columns" in data
    assert "shape" in data
    assert "dtypes" in data
    assert "summary" in data
    assert data["columns"] == ["name", "age"]
    assert data["shape"] == [2, 2]

@pytest.mark.backend
def test_upload_excel():
    # Create a mock Excel file
    df = pd.DataFrame({
        'name': ['John', 'Jane'],
        'age': [30, 25]
    })
    excel_buffer = io.BytesIO()
    df.to_excel(excel_buffer, index=False)
    excel_buffer.seek(0)
    
    files = {
        'file': ('test.xlsx', excel_buffer, 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    }
    
    response = client.post("/upload", files=files)
    assert response.status_code == 200
    
    data = response.json()
    assert "columns" in data
    assert "shape" in data
    assert "dtypes" in data
    assert "summary" in data

@pytest.mark.backend
def test_upload_invalid_format():
    # Test with unsupported file format
    files = {
        'file': ('test.txt', io.BytesIO(b'some text'), 'text/plain')
    }
    
    response = client.post("/upload", files=files)
    assert response.status_code == 200  # API returns 200 with error message
    assert response.json() == {"error": "Unsupported file format"}

@pytest.mark.backend
def test_upload_invalid_csv():
    # Test with malformed CSV
    csv_content = "invalid,csv,format\nno,proper,structure"
    files = {
        'file': ('test.csv', io.BytesIO(csv_content.encode()), 'text/csv')
    }
    
    response = client.post("/upload", files=files)
    assert response.status_code == 200
    data = response.json()
    assert "columns" in data  # Even malformed CSV should return stats
