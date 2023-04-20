import { Inter } from 'next/font/google'
import styles from '@/styles/Home.module.css'
import { useEffect, useState } from 'react'
import { Viewport } from 'next/dist/lib/metadata/types/extra-types'

const inter = Inter({ subsets: ['latin'] })

const URL_API = 'http://127.0.0.1:8000/produtos/'

export default function Home() {

  const [loading, setLoading] = useState(false)
  const [data, setData] = useState(null)

  const allData = async () => {
    try {
      setLoading(true)

      const response = await fetch(URL_API)
      const data = await response.json()
      if (!data) throw 'Error'
      setData(data)
      console.log(data)
      
    } catch (error) {
      console.log(error)
    } finally{
      setLoading(false)
    }
  }

  useEffect(() => {
    allData()
  }, [])

  return (
    <div className={styles.container}>
      {loading && !data &&
        <p>Carregando infomações...</p>
      }

      {data &&
        data.map((item) => (
          {/* <View>
            <Text>{item.name}</Text>
            <Text>{item.unitary_value}</Text>
          </View> */}
        ))
      }
    </div>
  )
}
