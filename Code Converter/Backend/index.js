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


app.post("/convert",async (req,res)=>{
    let {language,body}=req.body;

    let response=await runCompletion(`Convert the given code to ${language} code - ${body}`);

    console.log(response)
    res.send(response)
})

app.post("/debug",async (req,res)=>{
    let {body}=req.body;

    let response=await runCompletion(`Debug the following code with explanation - ${body}`);

    console.log(response)
    res.send(response)
})

app.post("/check",async (req,res)=>{
    let {body}=req.body;

    let response=await runCompletion(`Check the quality of the given code and give marks on syntax,logic and readability out of 10 - ${body}`);

    console.log(response)
    res.send(response)
})

app.listen(8080,()=>{
    console.log("Server running at 8080")
})
















async function runCompletion(myprompt) {
    try {
        const completion = await openai.createCompletion({
            model: "text-davinci-003",
            prompt: myprompt,
            max_tokens:100
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