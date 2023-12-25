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
        console.log(event, form);
        if (!form.valid) {
            return fail(400, {form})
        }
        return {
            form
        }
    }
}
