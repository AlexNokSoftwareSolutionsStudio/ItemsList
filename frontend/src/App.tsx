import { useEffect, useState } from 'react';

interface Item {
  id: number;
  itemname: string;
}

function App() {
  const [items, setItems] = useState<Item[]>([]);

  useEffect(() => {
    fetch('http://localhost:8000/items') // URL backend
      .then(res => res.json())
      .then(data => setItems(data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold mb-4">Список Item</h1>
      <ul className="list-disc pl-5">
        {items.map(item => (
          <li key={item.id} className="mb-2">
            {item.itemname}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
