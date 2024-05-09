import {IsNotEmpty, IsEmail, isNotEmpty, isNumber, IsNumber} from 'class-validator';

export class CreateUserDto {
	@IsNotEmpty()
	username: string;
	
	@IsNotEmpty()
	password: string;
	
	@IsNotEmpty()
	@IsEmail()
  	email: string;

	@IsNotEmpty()
	// @IsNumber()
	usia: number;
}

export class GetUserDto {
	@IsNotEmpty()
	username: string;
	@IsNotEmpty()
	password: string;
	@IsEmail()
	@IsNotEmpty()
	email: string;
}