import { HttpStatus, Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { CreateUserType } from 'src/app/app.type';
import { UpdateUserParams } from 'src/utils/types';
import { Users } from 'src/typeorm/entities/Users';
import { Repository } from 'typeorm';
import { UpdateUserDto_new } from 'src/users/dtos/Users.dto';

@Injectable()
export class MydbService {
    constructor(@InjectRepository(Users) private userRepo:Repository<Users>) {}

    findUser() {
        return this.userRepo.find()
    }

    createUser(createUser:CreateUserType) {
        if(!(this.userRepo.exists({
            where: {
                username:createUser.username
            }
        }))) {
            const CreateUser = this.userRepo.create({
                ...createUser,
                createdAt:new Date(),
                updatedAt:new Date(),
            });
            this.userRepo.save(CreateUser);
            return CreateUser;
        } else {
            return [];
        }

    }

    updateUser (username:string, updateuserdto:UpdateUserDto_new) {
        return this.userRepo.update({username},{...updateuserdto,updatedAt:new Date()});
    }

    deleteUser(username:string) {
        return this.userRepo.delete({username});
    }
}
