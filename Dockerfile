# Gunakan image dasar Python
FROM python:3.10-slim

# Set working directory di container
WORKDIR /app

# Copy semua file ke dalam container
COPY . /app

# Install dependensi
RUN pip install --no-cache-dir -r requirements.txt

# Expose port Flask (ganti jika perlu)
EXPOSE 5000

# Jalankan aplikasi Flask
CMD ["python", "app.py"]
