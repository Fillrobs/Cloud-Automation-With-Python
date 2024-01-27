# Declarative Terraform Configuration
resource "aws_instance" "example_instance" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}
 
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
 
