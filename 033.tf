# Terraform Configuration - main.tf
 
# Define a simple AWS EC2 instance
resource "aws_instance" "example_instance" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}
 
# Define a security group allowing inbound traffic on port 80
resource "aws_security_group" "example_sg" {
  name        = "example_sg"
  description = "Allow inbound traffic on port 80"
 
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
