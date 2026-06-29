"use client";

import { useEffect, useState } from "react";

export default function Page() {
  const [items, setItems] = useState<any[]>([]);

  useEffect(() => {
    fetch(`${process.env.NEXT_PUBLIC_API_URL}/urunler`)
      .then((res) => res.json())
      .then((data) => setItems(data));
  }, []);

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
