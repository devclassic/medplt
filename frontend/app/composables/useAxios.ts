import axios from 'axios'

const config = useRuntimeConfig()
const baseUrl = config.public.BASE_URL as string

const http = axios.create({
  baseURL: baseUrl,
})

export const useAxios = () => {
  return http
}
