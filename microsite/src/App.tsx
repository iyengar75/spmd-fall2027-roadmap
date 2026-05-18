import { useState, useEffect } from "react";
import { Hero } from "./components/sections/Hero";
import { Timeline } from "./components/sections/Timeline";
import { CourseGrid } from "./components/sections/CourseGrid";
import { RegulatorMatrix } from "./components/sections/RegulatorMatrix";
import { Downloads } from "./components/sections/Downloads";
import { Footer } from "./components/sections/Footer";
import type { SiteData } from "./types/data";
import "./index.css";

function NavBar() {
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => setScrolled(window.scrollY > 60);
    window.addEventListener("scroll", handleScroll, { passive: true });
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  return (
    <nav
      className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 ${
        scrolled ? "shadow-lg" : ""
      }`}
      style={{
        backgroundColor: scrolled ? "#003D7A" : "transparent",
      }}
    >
      <div className="max-w-6xl mx-auto px-6 py-3 flex items-center justify-between">
        <a
          href="#hero"
          className="text-sm font-bold tracking-wide text-white opacity-90 hover:opacity-100"
        >
          KU · BSCND · SPMD
        </a>
        <div className="hidden sm:flex items-center gap-6">
          {[
            { href: "#timeline", label: "Timeline" },
            { href: "#courses", label: "Courses" },
            { href: "#regulators", label: "Regulators" },
            { href: "#downloads", label: "Downloads" },
          ].map((item) => (
            <a
              key={item.href}
              href={item.href}
              className="text-xs uppercase tracking-wider text-white/70 hover:text-white transition-colors"
            >
              {item.label}
            </a>
          ))}
        </div>
      </div>
    </nav>
  );
}

function LoadingScreen() {
  return (
    <div
      className="min-h-screen flex items-center justify-center"
      style={{ backgroundColor: "#003D7A" }}
    >
      <div className="text-center">
        <div className="w-12 h-12 rounded-full border-4 border-white/20 border-t-white animate-spin mx-auto mb-4" />
        <p className="text-white/70 text-sm">Loading programme data…</p>
      </div>
    </div>
  );
}

function ErrorScreen({ error }: { error: string }) {
  return (
    <div className="min-h-screen flex items-center justify-center p-8">
      <div className="text-center max-w-lg">
        <h2 className="text-2xl font-bold text-red-600 mb-4">
          Failed to load data
        </h2>
        <p className="text-gray-600 text-sm">{error}</p>
      </div>
    </div>
  );
}

export default function App() {
  const [data, setData] = useState<SiteData | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetch("/_data.json")
      .then((r) => {
        if (!r.ok) throw new Error(`HTTP ${r.status}`);
        return r.json() as Promise<SiteData>;
      })
      .then((json) => setData(json))
      .catch((err: Error) =>
        setError(err.message || "Unknown error fetching _data.json")
      );
  }, []);

  if (error) return <ErrorScreen error={error} />;
  if (!data) return <LoadingScreen />;

  return (
    <div className="min-h-screen">
      <NavBar />
      <Hero data={data} />
      <Timeline data={data} />
      <CourseGrid data={data} />
      <RegulatorMatrix data={data} />
      <Downloads />
      <Footer />
    </div>
  );
}
