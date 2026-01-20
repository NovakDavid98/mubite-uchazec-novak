interface Album {
  userId: number;
  id: number;
  title: string;
}

async function getAlbums(): Promise<Album[]> {
  const apiUrl = process.env.API_URL || 'http://localhost:4000';
  const res = await fetch(`${apiUrl}/api/albums`, { cache: 'no-store' });

  if (!res.ok) {
    throw new Error('Failed to fetch albums from API');
  }

  return res.json();
}

export default async function Home() {
  const albums = await getAlbums();

  return (
    <div className="min-h-screen bg-gradient-to-br from-zinc-900 via-zinc-800 to-zinc-900">
      <div className="container mx-auto px-4 py-12">
        {/* Header */}
        <header className="mb-12 text-center">
          <h1 className="text-4xl font-bold bg-gradient-to-r from-purple-400 via-pink-500 to-red-500 bg-clip-text text-transparent mb-4">
            Album Collection
          </h1>
          <p className="text-zinc-400 text-lg">
            Displaying {albums.length} albums from our API
          </p>
        </header>

        {/* Album Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
          {albums.map((album) => (
            <div
              key={album.id}
              className="group relative bg-zinc-800/50 backdrop-blur-sm border border-zinc-700/50 rounded-2xl p-6 transition-all duration-300 hover:bg-zinc-700/50 hover:border-purple-500/50 hover:shadow-lg hover:shadow-purple-500/10 hover:-translate-y-1"
            >
              {/* Album ID Badge */}
              <div className="absolute top-4 right-4 w-8 h-8 bg-gradient-to-br from-purple-500 to-pink-500 rounded-full flex items-center justify-center text-xs font-bold text-white">
                {album.id}
              </div>

              {/* Album Icon */}
              <div className="w-12 h-12 bg-gradient-to-br from-purple-500/20 to-pink-500/20 rounded-xl flex items-center justify-center mb-4 group-hover:scale-110 transition-transform duration-300">
                <svg className="w-6 h-6 text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
                </svg>
              </div>

              {/* Album Title */}
              <h2 className="text-zinc-100 font-medium leading-relaxed capitalize">
                {album.title}
              </h2>

              {/* User ID */}
              <p className="text-zinc-500 text-sm mt-2">
                User #{album.userId}
              </p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
