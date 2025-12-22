import React from "react";
import LyricSheet from "../components/LyricSheet";

export default function Home() {
  const song = {
    title: "Imagine",
    lyrics: `
Imagine there's no heaven
It's easy if you try
No hell below us
Above us only sky
Imagine all the people
Living for today...
    `,
  };

  return (
    <div>
      <LyricSheet song={song} />
    </div>
  );
}
