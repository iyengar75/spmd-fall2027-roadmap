import { useRef } from "react";
import { motion, useInView } from "framer-motion";
import { ExternalLink, CheckCircle, Minus } from "lucide-react";
import { Badge } from "../ui/badge";
import type { SiteData } from "../../types/data";

interface RegulatorMatrixProps {
  data: SiteData;
}

const concentrationCourses = ["SPMD305", "SPMD306", "SPMD307", "SPMD308"];

const tierColors: Record<string, string> = {
  "Tier 1": "#003D7A",
  "Tier 2": "#1a5499",
  "Tier 3": "#6b7280",
};

export function RegulatorMatrix({ data }: RegulatorMatrixProps) {
  const ref = useRef<HTMLDivElement>(null);
  const isInView = useInView(ref, { once: true, margin: "-80px" });

  const regulatorEntries = Object.entries(data.regulators);

  return (
    <section id="regulators" className="py-20 px-6 bg-white">
      <div className="max-w-6xl mx-auto">
        <motion.div
          ref={ref}
          initial={{ opacity: 0, y: 20 }}
          animate={isInView ? { opacity: 1, y: 0 } : {}}
          transition={{ duration: 0.6 }}
          className="text-center mb-12"
        >
          <p
            className="text-sm font-semibold tracking-widest uppercase mb-2"
            style={{ color: "#C8A04A" }}
          >
            Accreditation &amp; Compliance
          </p>
          <h2
            className="text-3xl md:text-4xl font-bold"
            style={{ color: "#003D7A" }}
          >
            Regulator Alignment Matrix
          </h2>
          <p className="text-gray-500 mt-3 max-w-2xl mx-auto">
            How the Sports &amp; Fitness Coaching Concentration (SPMD 305-308)
            satisfies UAE and federal regulatory requirements.
          </p>
        </motion.div>

        {/* Regulator cards */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 mb-12">
          {regulatorEntries.map(([key, reg], i) => {
            const tierKey = reg.tier.startsWith("Tier 1")
              ? "Tier 1"
              : reg.tier.startsWith("Tier 2")
              ? "Tier 2"
              : "Tier 3";
            const tierColor = tierColors[tierKey];
            return (
              <motion.div
                key={key}
                initial={{ opacity: 0, y: 20 }}
                animate={isInView ? { opacity: 1, y: 0 } : {}}
                transition={{ duration: 0.5, delay: i * 0.08 }}
                className="rounded-xl border border-gray-200 p-4 bg-gray-50"
              >
                <div className="flex items-start justify-between gap-2 mb-2">
                  <div>
                    <div className="flex items-center gap-2">
                      <h3
                        className="font-bold text-sm"
                        style={{ color: tierColor }}
                      >
                        {key}
                      </h3>
                      <a
                        href={reg.url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="text-gray-400 hover:text-gray-600"
                      >
                        <ExternalLink className="w-3 h-3" />
                      </a>
                    </div>
                    <p className="text-xs text-gray-500 mt-0.5">{reg.full_name}</p>
                    <p
                      className="text-xs font-medium mt-0.5"
                      style={{ color: "#003D7A" }}
                    >
                      {reg.level}
                    </p>
                  </div>
                  <span
                    className="text-xs px-2 py-0.5 rounded-full text-white font-medium flex-shrink-0"
                    style={{ backgroundColor: tierColor }}
                  >
                    {tierKey}
                  </span>
                </div>
                <p className="text-xs text-gray-600 leading-relaxed line-clamp-3">
                  {reg.scope}
                </p>
              </motion.div>
            );
          })}
        </div>

        {/* Alignment matrix table */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={isInView ? { opacity: 1, y: 0 } : {}}
          transition={{ duration: 0.6, delay: 0.4 }}
        >
          <h3
            className="font-bold text-xl mb-6 text-center"
            style={{ color: "#003D7A" }}
          >
            Course × Regulator Alignment
          </h3>
          <div className="overflow-x-auto rounded-xl border border-gray-200 shadow-sm">
            <table className="w-full min-w-[700px] text-sm">
              <thead>
                <tr style={{ backgroundColor: "#003D7A" }}>
                  <th className="text-left text-white font-semibold px-4 py-3 w-32">
                    Regulator
                  </th>
                  {concentrationCourses.map((cid) => (
                    <th
                      key={cid}
                      className="text-center text-white font-semibold px-3 py-3"
                    >
                      <div className="font-bold">{cid}</div>
                      <div className="text-xs font-normal text-blue-200 mt-0.5 max-w-[140px] mx-auto">
                        {data.courses[cid]?.title.split(" ").slice(0, 3).join(" ")}…
                      </div>
                    </th>
                  ))}
                </tr>
              </thead>
              <tbody>
                {regulatorEntries.map(([key, reg], i) => (
                  <tr
                    key={key}
                    className={i % 2 === 0 ? "bg-white" : "bg-gray-50"}
                  >
                    <td className="px-4 py-3 font-semibold text-[#003D7A] text-xs align-top">
                      <div className="font-bold">{key}</div>
                      <div className="text-gray-400 font-normal text-xs mt-0.5">
                        {reg.full_name.split(" ").slice(0, 3).join(" ")}
                      </div>
                    </td>
                    {concentrationCourses.map((cid) => {
                      const alignment = reg.alignment[cid];
                      return (
                        <td
                          key={cid}
                          className="px-3 py-3 text-xs text-gray-600 align-top"
                        >
                          {alignment ? (
                            <div className="flex gap-1.5">
                              <CheckCircle
                                className="w-3.5 h-3.5 flex-shrink-0 mt-0.5"
                                style={{ color: "#003D7A" }}
                              />
                              <span className="leading-relaxed">{alignment}</span>
                            </div>
                          ) : (
                            <div className="flex justify-center">
                              <Minus className="w-4 h-4 text-gray-300" />
                            </div>
                          )}
                        </td>
                      );
                    })}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          <p className="text-xs text-gray-400 mt-3 text-center">
            SPMD 301-304 (Minor) rows omitted — minor courses do not directly
            target fitness-coach regulatory registration. Refer to track
            descriptions above.
          </p>
        </motion.div>

        {/* ICREPs eligibility callout */}
        <motion.div
          initial={{ opacity: 0 }}
          animate={isInView ? { opacity: 1 } : {}}
          transition={{ duration: 0.6, delay: 0.6 }}
          className="mt-8 rounded-xl p-6 border-2 border-[#C8A04A] bg-amber-50"
        >
          <div className="flex flex-wrap gap-4 items-start">
            <div className="flex-1 min-w-[200px]">
              <h4 className="font-bold text-[#003D7A] mb-2">
                ICREPs Eligibility — Concentration Only
              </h4>
              <p className="text-sm text-gray-700 leading-relaxed">
                The Sports &amp; Fitness Coaching Concentration (SPMD 305-308)
                is designed to satisfy all ICREPs Level 3 Personal Trainer
                competency units, enabling graduates to apply for REPs UAE
                Personal Trainer registration. The Sports Medicine Minor (SPMD
                301-304) alone does NOT confer fitness-coach registration
                eligibility.
              </p>
            </div>
            <div className="flex flex-col gap-2">
              <Badge variant="concentration" className="justify-center">
                ICREPs Level 3 PT ✓
              </Badge>
              <Badge variant="gold" className="justify-center">
                REPs UAE Eligible ✓
              </Badge>
            </div>
          </div>
        </motion.div>
      </div>
    </section>
  );
}
