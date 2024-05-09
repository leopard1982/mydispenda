import { Body, Controller, Get, HttpStatus, Post, ValidationPipe, Put, Param, Delete } from '@nestjs/common';
import { CreateUserDto_new, UpdateUserDto_new } from 'src/users/dtos/Users.dto';
import { MydbService } from './mydb.service';

@Controller('mydb')
export class MydbController {
    constructor(private userService: MydbService) {

    }

    @Get()
    async getUsers() {
        const mydata = await this.userService.findUser();
        return {
            'status':200,
            'rowCount':mydata.length,
            'data':mydata
        }
    }

    @Post()
    postUser(@Body() createUserDto:CreateUserDto_new) {
        const mydata = this.userService.createUser(createUserDto);
        return {
            'status': 200,
            'data': mydata
        }
    }

    @Put(':username')
    async updateUserByUsername(
        @Param('username') username:string,
        @Body() userupdateDto: UpdateUserDto_new) {
        const updatedb = await this.userService.updateUser(username,userupdateDto)
        if(updatedb.affected===1)
            return{'status':HttpStatus.ACCEPTED,'msg':updatedb}
        else
            return{'status':HttpStatus.NOT_MODIFIED,'msg':{}}
    }

    @Delete(':username')
    async deleteUserByUsername(@Param('username') username:string) {
        const deletedb = await this.userService.deleteUser(username);
        if (deletedb.affected===1)
            return{'status':HttpStatus.ACCEPTED,'msg':deletedb}
        else
            return{'status':HttpStatus.NOT_MODIFIED,'msg':[]}   
    }
}
