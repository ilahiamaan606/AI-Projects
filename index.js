const express=require("express");
const cors=require("cors")


const app=express();


app.use(express.json())
app.use(cors())


const { Configuration, OpenAIApi } = require("openai");
require('dotenv').config()

const configuration = new Configuration({
    apiKey: process.env.OPENAI_API_KEY,
});
const openai = new OpenAIApi(configuration)


app.post("/",async (req,res)=>{
    let {keyword}=req.body;

    let response=await runCompletion(keyword);

    console.log(response)
    res.send(response)
})


app.listen(8080,()=>{
    console.log("Server running at 8080")
})
















async function runCompletion(keyword) {
    try {
        const completion = await openai.createCompletion({
            model: "text-davinci-003",
            prompt: `Create a knock-knock joke using the word - ${keyword}`,
            max_tokens:75
        });
        return (completion.data.choices[0].text);

    } catch (error) {
        if (error.response) {
            console.log(error.response.status);
            console.log(error.response.data);
        } else {
            console.log(error.message);
        }
    }

}