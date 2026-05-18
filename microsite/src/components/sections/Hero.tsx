import { motion } from "framer-motion";
import { Badge } from "../ui/badge";
import type { SiteData } from "../../types/data";

interface HeroProps {
  data: SiteData;
}

export function Hero({ data }: HeroProps) {
  const { program } = data;

  return (
    <section
      id="hero"
      className="relative min-h-[60vh] flex flex-col items-center justify-center text-center px-6 py-20 overflow-hidden"
      style={{ backgroundColor: "#003D7A" }}
    >
      {/* Background pattern */}
      <div
        className="absolute inset-0 opacity-5"
        style={{
          backgroundImage:
            "repeating-linear-gradient(45deg, #C8A04A 0, #C8A04A 1px, transparent 0, transparent 50%)",
          backgroundSize: "20px 20px",
        }}
      />

      <motion.div
        initial={{ opacity: 0, y: 30 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.7 }}
        className="relative z-10 max-w-4xl mx-auto"
      >
        {/* Institution line */}
        <motion.p
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.2 }}
          className="text-sm font-semibold tracking-widest uppercase mb-4"
          style={{ color: "#C8A04A" }}
        >
          {program.institution} · {program.college}
        </motion.p>

        {/* Fall 2027 badge */}
        <motion.div
          initial={{ opacity: 0, scale: 0.8 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ delay: 0.3 }}
          className="inline-flex mb-6"
        >
          <Badge
            variant="gold"
            className="text-sm px-4 py-1.5 rounded-full font-bold tracking-wide shadow-lg"
          >
            Fall 2027 Launch · {program.target_intake}
          </Badge>
        </motion.div>

        {/* Program title */}
        <motion.h1
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.4 }}
          className="text-4xl md:text-5xl lg:text-6xl font-bold text-white leading-tight mb-4"
        >
          {program.name}
        </motion.h1>

        {/* Subtitle */}
        <motion.p
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.5 }}
          className="text-xl md:text-2xl mb-8"
          style={{ color: "rgba(200, 160, 74, 0.9)" }}
        >
          Two-Track Sports Medicine Offering at KU BSCND
        </motion.p>

        {/* Description */}
        <motion.p
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.6 }}
          className="text-base md:text-lg text-blue-100 max-w-3xl mx-auto leading-relaxed mb-10"
        >
          {program.note}
        </motion.p>

        {/* Stats row */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.7 }}
          className="flex flex-wrap justify-center gap-8"
        >
          {[
            { label: "Baseline Credits", value: program.total_credits_baseline },
            { label: "With Concentration", value: program.total_credits_with_concentration },
            { label: "QF Emirates Level", value: program.qf_emirates_level },
            { label: "Courses Proposed", value: "8 (SPMD 301-308)" },
          ].map((stat) => (
            <div key={stat.label} className="text-center">
              <div
                className="text-3xl font-bold"
                style={{ color: "#C8A04A" }}
              >
                {stat.value}
              </div>
              <div className="text-xs uppercase tracking-wider text-blue-200 mt-1">
                {stat.label}
              </div>
            </div>
          ))}
        </motion.div>

        {/* Nav links */}
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.9 }}
          className="flex flex-wrap justify-center gap-4 mt-10"
        >
          {["timeline", "courses", "regulators", "downloads"].map((section) => (
            <a
              key={section}
              href={`#${section}`}
              className="px-5 py-2 rounded-full border border-white/30 text-white/80 text-sm hover:bg-white/10 hover:border-white/60 transition-all capitalize"
            >
              {section}
            </a>
          ))}
        </motion.div>
      </motion.div>
    </section>
  );
}
