type Song = {
  title: string;
  lyrics: string;
};

type Props = {
  song: Song;
};

export default function LyricSheet({ song }: Props) {
  return (
    <div>
      <h1>{song.title}</h1>
      <pre>{song.lyrics}</pre>
    </div>
  );
}
