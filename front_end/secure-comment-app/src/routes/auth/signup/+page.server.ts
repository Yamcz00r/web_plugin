import {superValidate} from "sveltekit-superforms/server";
import {z} from "zod";
import {fail} from "@sveltejs/kit"

const newContactSchema = z.object({
    userName: z.string().min(1),
    repeatUserName: z.string().min(1),
    email: z.string().email(),
    password: z.string().min(8),
    repeatPassword: z.string().min(8)
})

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
                password : form.data.password
            }),
            headers: {
                'Content-Type': 'application/json'
            }
        });
        if (response.status === 200) {
            return "account added successfully"
        }
    }
}
