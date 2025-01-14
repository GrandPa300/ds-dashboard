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
