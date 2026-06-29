"use client";

import { useEffect, useState } from "react";

interface Urun {
  isim: string;
  fiyat: number;
}

export default function Page() {
  const [items, setItems] = useState<Urun[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(`${process.env.NEXT_PUBLIC_API_URL}/urunler`)
      .then((res) => res.json())
      .then((data) => {
        setItems(data);
        setLoading(false);
      })
      .catch((err) => {
        console.error("Veri çekilirken hata:", err);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <p>Yükleniyor...</p>;
  }

  return (
    <ul>
      {items.map((item, i) => (
        <li key={i}>
          {item.isim} - {item.fiyat} TL
        </li>
      ))}
    </ul>
  );
}
