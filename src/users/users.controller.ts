import { 
	Controller, Get, Post, Body, Header, Param, Put, Patch, Delete, Query,
	ValidationPipe, UsePipes, ParseIntPipe, ParseBoolPipe,
	HttpException,
	HttpStatus,
	UseGuards
} from '@nestjs/common';

import { CreateUserDto, GetUserDto } from './dtos/CreateUser.dto';
import { UsersService } from './users.service';
import { MypipePipe } from './pipe/mypipe/mypipe.pipe';
import { MyguardGuard } from './guard/myguard/myguard.guard';

@Controller('users')
@UseGuards(MyguardGuard)
export class UsersController {
	constructor(private userService: UsersService) {
		
	}

	@Get()
	@UsePipes(new ValidationPipe())
	getUsers(
		@Body() mybody:GetUserDto,
		@Query('ascId',ParseBoolPipe) ascId:boolean,
	) {
		const data = this.userService.fetchUser(ascId);
		return {
			statusCode:200,
			message: {
				totalRows: data.length,
				msg: data
			}
		}
	}

	@Post()
	@UsePipes(new ValidationPipe())
	postUsers(@Body(MypipePipe) userRequest:CreateUserDto) 
	{
		const mydata = {
			'username': userRequest.username,
			'password': userRequest.password,
			'email': userRequest.email,
			'usia':userRequest.usia
		}	
		console.log(userRequest.usia.toPrecision(3));
		return this.userService.insertUser(mydata);

	}

	@Get(':username')
	@UsePipes(new ValidationPipe())
	getUserById(
		@Param('username') username:string,
		@Body() getUser:GetUserDto,
		) 
		{
			let mydata = this.userService.fetchUserByID(username);
			console.log(mydata);
			if(mydata.length==0) {
				// throw new HttpException("Data Not Found massehhh",HttpStatus.BAD_REQUEST);
				return {
					'statusCode':400,
					'method':'GET',
					'totalRows': 0, 
					'data': {
						mydata				
					}
				};
			}
			return {
				'statusCode':200,
				'method':'GET',
				'totalRows': mydata.length, 
				'data': {
					mydata				
				}
			};
	}

	@Post(':id/:nama')
	@UsePipes(new ValidationPipe())
	PostUserID(@Param('id',ParseIntPipe) id:number, 
		@Param('nama') nama:string, 
		@Body() getUser:GetUserDto,
		) {
		return {
			'statusCode':200,
			'method':'POST',
			'data': {
				getUser,
				'parameter': {
					id,
					nama
				}
			}
		}
	}

	@Put(':id/:nama')
	putUserID(@Param('id') id:number, 
		@Param('nama') nama:string, 
		@Body() getUser:GetUserDto,
		) {
		return {
			'statusCode':200,
			'method':'PUT',
			'data': {
				getUser,
				'parameter': {
					id,
					nama
				}
			}
		}
	}
	
	@Patch(':id/:nama')
	patchUserID(@Param('id',ParseIntPipe) id:number, 
		@Param('nama') nama:string, 
		@Body() getUser:GetUserDto,
		) {
		return {
			'statusCode':200,
			'method':'PATCH',
			'data': {
				getUser,
				'parameter': {
					id,
					nama
				}
			}
		}
	}

	@Delete(':id/:nama')
	deleteUserID(@Param('id',ParseIntPipe) id:number, 
		@Param('nama') nama:string, 
		@Body() getUser:GetUserDto,
		) {
		return {
			'statusCode':200,
			'method':'DELETE',
			'data': {
				getUser,
				'parameter': {
					id,
					nama

				}
			}
		}
	}
}
