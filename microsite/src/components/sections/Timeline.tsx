import { useRef } from "react";
import { motion, useInView } from "framer-motion";
import { Badge } from "../ui/badge";
import type { SiteData } from "../../types/data";

interface TimelineProps {
  data: SiteData;
}

const gateColors: Record<string, string> = {
  "Q3 2026": "#C8A04A",
  "Q4 2026": "#1a5499",
  "Q1 2027": "#2e7d32",
  "Q2 2027": "#7b1fa2",
  "Q3 2027": "#003D7A",
};

export function Timeline({ data }: TimelineProps) {
  const ref = useRef<HTMLDivElement>(null);
  const isInView = useInView(ref, { once: true, margin: "-100px" });

  return (
    <section id="timeline" className="py-20 px-6 bg-white">
      <div className="max-w-6xl mx-auto">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={isInView ? { opacity: 1, y: 0 } : {}}
          transition={{ duration: 0.6 }}
          ref={ref}
          className="text-center mb-16"
        >
          <p
            className="text-sm font-semibold tracking-widest uppercase mb-2"
            style={{ color: "#C8A04A" }}
          >
            Regulatory Roadmap
          </p>
          <h2
            className="text-3xl md:text-4xl font-bold"
            style={{ color: "#003D7A" }}
          >
            Q3 2026 → Fall 2027 Launch Timeline
          </h2>
          <p className="text-gray-500 mt-3 max-w-2xl mx-auto">
            Five-quarter gated pathway from syllabus authoring through ADEK
            authorization to first student intake.
          </p>
        </motion.div>

        {/* Track legend */}
        <div className="flex flex-wrap gap-4 justify-center mb-10">
          <div className="flex items-center gap-2">
            <span
              className="w-4 h-4 rounded-full inline-block"
              style={{ backgroundColor: "#003D7A" }}
            />
            <span className="text-sm text-gray-600">
              Sports Medicine Minor (SPMD 301-304)
            </span>
          </div>
          <div className="flex items-center gap-2">
            <span
              className="w-4 h-4 rounded-full inline-block"
              style={{ backgroundColor: "#C8A04A" }}
            />
            <span className="text-sm text-gray-600">
              Sports &amp; Fitness Coaching Concentration (SPMD 305-308)
            </span>
          </div>
        </div>

        {/* Timeline cards */}
        <div className="relative">
          {/* Connecting line (desktop) */}
          <div
            className="hidden lg:block absolute top-12 left-0 right-0 h-0.5 z-0"
            style={{ backgroundColor: "#e5e7eb" }}
          />

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-6 relative z-10">
            {data.phases.map((phase, i) => {
              const color = gateColors[phase.q] || "#003D7A";
              return (
                <motion.div
                  key={phase.q}
                  initial={{ opacity: 0, y: 40 }}
                  animate={isInView ? { opacity: 1, y: 0 } : {}}
                  transition={{ duration: 0.5, delay: i * 0.12 }}
                  className="flex flex-col"
                >
                  {/* Quarter indicator */}
                  <div className="flex items-center gap-3 mb-4 lg:flex-col lg:items-center">
                    <div
                      className="w-8 h-8 rounded-full flex items-center justify-center text-white text-xs font-bold flex-shrink-0 shadow"
                      style={{ backgroundColor: color }}
                    >
                      {i + 1}
                    </div>
                    <div className="lg:text-center">
                      <span
                        className="text-xs font-bold uppercase tracking-wider"
                        style={{ color }}
                      >
                        {phase.q}
                      </span>
                      <div className="text-xs text-gray-400">
                        {phase.date_range}
                      </div>
                    </div>
                  </div>

                  {/* Card */}
                  <div
                    className="flex-1 rounded-xl border-2 p-4 bg-white shadow-sm"
                    style={{ borderColor: color }}
                  >
                    <h3
                      className="font-bold text-sm mb-3 leading-tight"
                      style={{ color }}
                    >
                      {phase.label}
                    </h3>

                    {/* Minor deliverable */}
                    <div className="mb-3">
                      <Badge variant="minor" className="mb-1 text-xs">
                        Minor
                      </Badge>
                      <p className="text-xs text-gray-600 mt-1 leading-relaxed">
                        {phase.deliverables.minor}
                      </p>
                    </div>

                    {/* Concentration deliverable */}
                    <div className="mb-3">
                      <Badge variant="concentration" className="mb-1 text-xs">
                        Concentration
                      </Badge>
                      <p className="text-xs text-gray-600 mt-1 leading-relaxed">
                        {phase.deliverables.concentration}
                      </p>
                    </div>

                    {/* Gate */}
                    <div
                      className="mt-3 pt-3 border-t"
                      style={{ borderColor: `${color}33` }}
                    >
                      <p className="text-xs font-semibold text-gray-500 uppercase tracking-wide mb-1">
                        Gate
                      </p>
                      <p className="text-xs text-gray-700">{phase.gate}</p>
                    </div>

                    {/* Owner */}
                    <div className="mt-2">
                      <p className="text-xs text-gray-400">
                        <span className="font-medium">Owner:</span>{" "}
                        {phase.owner.split("+")[0].trim()}
                      </p>
                    </div>
                  </div>
                </motion.div>
              );
            })}
          </div>
        </div>
      </div>
    </section>
  );
}
