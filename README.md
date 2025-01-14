# Data Science Dashboard

A web-based dashboard for quick data analysis and visualization. This application allows users to upload CSV or Excel files and perform instant data analysis with interactive visualizations.

## Features

- File upload support for CSV and Excel files
- Automatic data type detection
- Interactive data preview
- Distribution plots for numerical and categorical data
- Summary statistics
- Correlation analysis for numerical columns
- Responsive layout with side-by-side visualizations

## Screenshots

### Data Overview and Analysis
![Data Overview](public/Screenshot%202025-01-14%20152313.png)

### Correlation Analysis
![Correlation Analysis](public/Screenshot%202025-01-14%20152342.png)

## Architecture

The project consists of two main components:

### Backend (FastAPI)
- Handles file uploads
- Processes data files
- Provides basic statistics and data analysis
- RESTful API endpoints for data operations

### Frontend (Streamlit)
- User-friendly interface
- Interactive data visualization
- Real-time data analysis
- Responsive layout design

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ds-dashboard.git
cd ds-dashboard
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the backend server:
```bash
cd backend
uvicorn main:app --reload
```

2. Start the frontend application:
```bash
cd frontend
streamlit run app.py
```

3. Open your browser and navigate to `http://localhost:8501`

## Dependencies

- FastAPI: Web framework for building APIs
- Streamlit: Frontend framework for data applications
- Pandas: Data manipulation and analysis
- Plotly: Interactive visualizations
- Other dependencies:
  - uvicorn
  - numpy
  - matplotlib
  - seaborn
  - python-multipart
  - openpyxl
  - requests

## Features in Detail

1. **Data Upload**
   - Support for CSV and Excel files
   - Automatic file format detection
   - Error handling for unsupported formats

2. **Data Overview**
   - Display of data shape and columns
   - Interactive data preview
   - Basic data information

3. **Analysis Tools**
   - Distribution plots for numerical and categorical data
   - Summary statistics
   - Correlation analysis for numerical columns
   - Interactive visualization options

4. **Visualization**
   - Histograms for numerical data
   - Bar charts for categorical data
   - Correlation heatmaps
   - Interactive Plotly charts

## API Endpoints

- `POST /upload`: Upload and process data files
- `GET /health`: Health check endpoint

## Error Handling

The application includes comprehensive error handling for:
- File upload issues
- Data processing errors
- Invalid file formats
- Runtime exceptions

## Testing

The project uses pytest for both backend and frontend testing. Tests are organized in a structured manner:

```
tests/
├── __init__.py
├── backend/
│   ├── __init__.py
│   └── test_main.py      # API endpoint tests
└── frontend/
    ├── __init__.py
    └── test_app.py       # Frontend component tests
```

### Running Tests

1. Ensure you're in the correct conda environment:
```bash
conda activate ds-dashboard
```

2. Run all tests:
```bash
pytest
```

3. Run specific test suites:
```bash
# Backend tests only
pytest -v -m backend

# Frontend tests only
pytest -v -m frontend

# Tests in specific directory
pytest tests/backend/
pytest tests/frontend/
```

### Test Coverage

Backend tests cover:
- File upload functionality
- CSV and Excel file processing
- Error handling for invalid formats
- Health check endpoint
- Data processing and statistics generation

Frontend tests cover:
- Component rendering
- User interface interactions
- File upload component functionality

### Adding New Tests

1. Backend Tests:
   - Add new test functions in `tests/backend/test_main.py`
   - Use `@pytest.mark.backend` decorator
   - Follow existing patterns for API testing

2. Frontend Tests:
   - Add new test functions in `tests/frontend/test_app.py`
   - Use `@pytest.mark.frontend` decorator
   - Follow component testing best practices

### Test Configuration

The `pytest.ini` file configures test discovery and execution:
- Automatic test discovery in the `tests` directory
- Test file naming pattern: `test_*.py`
- Custom markers for backend and frontend tests
- Verbose test output by default
