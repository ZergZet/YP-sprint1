# Build stage
FROM golang:1.22-alpine AS builder
   
# Set working directory
WORKDIR /app

# Copy go.mod and go.sum files
COPY go.mod go.sum ./

# Download dependencies
#RUN go mod download

# Copy the source code
COPY . .

# Build the application
#RUN CGO_ENABLED=0 GOOS=linux go build -o smarthome
RUN CGO_ENABLED=0 GOOS=linux go build -mod=vendor -o smarthome 

# Runtime stage
FROM alpine:latest

# Install necessary runtime dependencies
#RUN apk --no-cache add ca-certificates tzdata
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/

# Set working directory
WORKDIR /app

# Copy the binary from the builder stage
COPY --from=builder /app/smarthome .

# Копируем файлы временных зон из /usr/share/zoneinfo
COPY --from=builder /usr/share/zoneinfo /usr/share/zoneinfo
# Указываем нужную временную зону через переменную окружения
ENV TZ=Europe/Moscow

# Expose the port the app runs on
EXPOSE 8080

# Command to run the application
CMD ["./smarthome"]
