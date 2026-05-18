import { useRef } from "react";
import { motion, useInView } from "framer-motion";
import { FileText, Table, Globe, Image, Music, BookOpen } from "lucide-react";
import { Button } from "../ui/button";

const artifacts = [
  {
    name: "SPMD_Fall2027_Roadmap.docx",
    label: "Roadmap Document (.docx)",
    icon: FileText,
    type: "Word Document",
    color: "#003D7A",
  },
  {
    name: "SPMD_Fall2027_Roadmap.xlsx",
    label: "Roadmap Spreadsheet (.xlsx)",
    icon: Table,
    type: "Excel Workbook",
    color: "#1a5499",
  },
  {
    name: "SPMD_Fall2027_Roadmap.html",
    label: "Roadmap Web View (.html)",
    icon: Globe,
    type: "HTML Document",
    color: "#C8A04A",
  },
  {
    name: "qtg_matrix.png",
    label: "QTG Matrix (PNG)",
    icon: Image,
    type: "Image",
    color: "#2e7d32",
  },
  {
    name: "regulator_alignment.png",
    label: "Regulator Alignment Chart (PNG)",
    icon: Image,
    type: "Image",
    color: "#2e7d32",
  },
  {
    name: "briefing.pdf",
    label: "Executive Briefing (.pdf)",
    icon: FileText,
    type: "PDF",
    color: "#c62828",
  },
  {
    name: "study_guide.pdf",
    label: "Study Guide (.pdf)",
    icon: BookOpen,
    type: "PDF",
    color: "#c62828",
  },
  {
    name: "audio_overview.mp3",
    label: "Audio Overview (.mp3)",
    icon: Music,
    type: "Audio",
    color: "#6a1b9a",
  },
  {
    name: "qa_pack.pdf",
    label: "QA Pack (.pdf)",
    icon: FileText,
    type: "PDF",
    color: "#c62828",
  },
];

export function Downloads() {
  const ref = useRef<HTMLDivElement>(null);
  const isInView = useInView(ref, { once: true, margin: "-80px" });

  return (
    <section
      id="downloads"
      className="py-20 px-6"
      style={{ backgroundColor: "#f8f9fc" }}
    >
      <div className="max-w-4xl mx-auto">
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
            Review Pack
          </p>
          <h2
            className="text-3xl md:text-4xl font-bold"
            style={{ color: "#003D7A" }}
          >
            Download Artifacts
          </h2>
          <p className="text-gray-500 mt-3 max-w-xl mx-auto">
            All artefacts for ADEK review. Files will be available following
            Wave 3 pipeline deployment.
          </p>
        </motion.div>

        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
          {artifacts.map((artifact, i) => {
            const Icon = artifact.icon;
            return (
              <motion.div
                key={artifact.name}
                initial={{ opacity: 0, x: -20 }}
                animate={isInView ? { opacity: 1, x: 0 } : {}}
                transition={{ duration: 0.4, delay: i * 0.06 }}
              >
                <a
                  href={`/${artifact.name}`}
                  download
                  className="flex items-center gap-4 p-4 rounded-xl border border-gray-200 bg-white hover:shadow-md hover:border-[#003D7A] transition-all group"
                >
                  <div
                    className="w-10 h-10 rounded-lg flex items-center justify-center flex-shrink-0"
                    style={{ backgroundColor: `${artifact.color}15` }}
                  >
                    <Icon
                      className="w-5 h-5"
                      style={{ color: artifact.color }}
                    />
                  </div>
                  <div className="flex-1 min-w-0">
                    <p className="text-sm font-medium text-gray-800 truncate group-hover:text-[#003D7A] transition-colors">
                      {artifact.label}
                    </p>
                    <p className="text-xs text-gray-400 mt-0.5">{artifact.type}</p>
                  </div>
                  <Button
                    variant="outline"
                    size="sm"
                    className="flex-shrink-0 text-xs"
                    onClick={(e) => e.stopPropagation()}
                  >
                    Download
                  </Button>
                </a>
              </motion.div>
            );
          })}
        </div>

        <motion.p
          initial={{ opacity: 0 }}
          animate={isInView ? { opacity: 1 } : {}}
          transition={{ delay: 0.8 }}
          className="text-xs text-gray-400 text-center mt-6"
        >
          Files served from <code className="bg-gray-100 px-1 rounded">/public/</code> — populated by Wave 3 (A7) before
          deployment. Links are active once files exist.
        </motion.p>
      </div>
    </section>
  );
}
