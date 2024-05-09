import { IsAlphanumeric, IsDate, IsEmail, IsNotEmpty, IsNumber, MaxLength, MinLength } from "class-validator";

export class CreateUserDto_new {
    @MinLength(8)
    @MaxLength(20)
    username: string;

    @IsNotEmpty()
    @IsAlphanumeric()
    @MinLength(8)
    password: string;

    @IsEmail()
    @IsNotEmpty()
    email: string;

    @IsNotEmpty()
    @IsNumber()
    usia: number;

    @IsDate()
    @IsNotEmpty()
    createdAt: Date;

    @IsDate()
    @IsNotEmpty()
    updatedAt: Date;
}

export class UpdateUserDto_new {
    username: string;

    password: string;

    email: string;

    createdAt: Date;
}