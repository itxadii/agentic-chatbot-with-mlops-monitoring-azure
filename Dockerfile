# 1. Use a slim Python 3.11 image for optimization
FROM python:3.11-slim

# 2. Set the working directory
WORKDIR /app

# 3. Prevent Python from writing .pyc files and buffer stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 4. Install system dependencies if needed (none for this specific stack)
# RUN apt-get update && apt-get install -y --no-install-recommends ...

# 5. Install dependencies separately for better layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy the entire modular structure
# This includes the agent/ and monitoring/ folders
COPY . .

# 7. Set the PYTHONPATH so modules can find each other
ENV PYTHONPATH=/app

# 8. Run the main script
CMD ["python", "main.py"]