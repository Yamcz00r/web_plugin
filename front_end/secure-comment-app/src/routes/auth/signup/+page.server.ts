import {superValidate} from "sveltekit-superforms/server";
import {z} from "zod";
import {fail, redirect} from "@sveltejs/kit"
import {token} from "../../store.js";

const newContactSchema = z.object({
    userName: z.string().min(1),
    email: z.string().email(),
    password: z.string().min(8),
    repeatPassword: z.string().min(8)
}).superRefine(({repeatPassword, password}, ctx) => {
    if (repeatPassword !== password) {
        ctx.addIssue({
            code: "custom",
            message: "The passwords did not match"
        });
    }
});

export const load = async (event) => {
    const form = await superValidate(event, newContactSchema)
    return {
        form
    }
}

export const actions = {
    default: async (event) => {
        const form = await superValidate(event, newContactSchema)
        if (!form.valid) {
            return fail(400, {form})
        }
        const response = await fetch('http://localhost:8000/users/create_user/', {
            method: 'POST',
            body: JSON.stringify({
                email: form.data.email,
                user_name: form.data.userName,
                password: form.data.password
            }),
            headers: {
                'Content-Type': 'application/json'
            }
        });
        const responseJson = await response.json()
        console.log(responseJson && responseJson.access_token)
        if (response.status === 200) {
            token.update(() =>responseJson.access_token)
            throw redirect(302, '/')
        }
    }
}
