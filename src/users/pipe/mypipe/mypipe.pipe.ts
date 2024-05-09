import { ArgumentMetadata, HttpException, HttpStatus, Injectable, PipeTransform } from '@nestjs/common';
import { CreateUserDto } from 'src/users/dtos/CreateUser.dto';

@Injectable()
export class MypipePipe implements PipeTransform {
  transform(value: CreateUserDto, metadata: ArgumentMetadata) {
    const umurnya = value.usia;
    console.log(isNaN(umurnya));
    if (isNaN(value.usia)) {
      throw new HttpException("Usia Harus Angka",HttpStatus.BAD_REQUEST);
    } else return value;
 
  }
}
