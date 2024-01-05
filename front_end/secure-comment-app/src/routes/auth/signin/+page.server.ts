import {superValidate} from "sveltekit-superforms/server";
import {z} from "zod";
import {fail} from "@sveltejs/kit"

const newContactSchema = z.object({
    email: z.string().email(),
    password: z.string().min(8)
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
        const response = await fetch('http://localhost:8000/token', {
            method: 'POST',
            body: new URLSearchParams({
                grant_type: '',
                username: form.data.email,
                password: form.data.password,
                scope: '',
                client_id: '',
                client_secret: ''
            }),
            headers: {
                'accept': 'application/json',
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        });
        const responseJson = await response.json()
        console.log(responseJson)
        if (response.status === 200) {
            return "account added successfully"
        }
    }
}
