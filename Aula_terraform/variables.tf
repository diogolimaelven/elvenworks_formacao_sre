variable "region" {
  default = "us-east-1"
}

variable "profile" {
  default = "noprod"
}

variable "name_security_group" {
  default = "allow_ssh"
}

variable "vpn_id_security_group" {
  default = "vpc-0360e69c46f3fc009"
}

variable "ami_aws_instance" {
  default = "ami-04505e74c0741db8d"
}

variable "type_aws_instance" {
  default = "t2.micro"
}

variable "subnet_id_aws_instance" {
  default = "subnet-0aa444b78f2864645"
}

variable "key_aws_instance" {
  default = "Curso_terraform"
}
