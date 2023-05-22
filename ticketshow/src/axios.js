import axios from 'axios'

const instance = axios.create({
  baseURL: 'http://localhost:8000',
   
})
instance.interceptors.request.use((config)=>{
const token = JSON.parse(localStorage.getItem("user"))

if(user?.accessToken){
    config.headers.Authorization= `Bearer ${token}`
}
return config
},
(err)=>{
    Promise.reject(err)
})

export default instance