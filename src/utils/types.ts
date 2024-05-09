export type CreateUserParams = {
    username: string;
    password: string;
    email: string;
    usia: number;
    createdAt: Date;
    updatedAt: Date;
}

export type UpdateUserParams = {
    username: string;
    password: string;
    email: string;
    usia: number;
    updatedAt: Date;
}