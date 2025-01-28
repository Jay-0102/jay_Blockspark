'use client'
export default function Lecture({params}){
    return(
        <div>
            <h1>Day Of College {params.lectures[0]}</h1>
            <h2>Lecture No. {params.lectures[1]}</h2>
        </div>
    )
}