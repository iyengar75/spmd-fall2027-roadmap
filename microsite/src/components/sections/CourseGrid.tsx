import { useState, useRef } from "react";
import { motion, useInView } from "framer-motion";
import { BookOpen, FlaskConical, Clock } from "lucide-react";
import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
} from "../ui/card";
import { Badge } from "../ui/badge";
import {
  Sheet,
  SheetContent,
  SheetHeader,
  SheetTitle,
  SheetDescription,
} from "../ui/sheet";
import type { SiteData, Course } from "../../types/data";

interface CourseGridProps {
  data: SiteData;
}

function CourseDrawer({
  courseId,
  course,
  open,
  onClose,
}: {
  courseId: string;
  course: Course;
  open: boolean;
  onClose: () => void;
}) {
  return (
    <Sheet open={open} onOpenChange={(v) => !v && onClose()}>
      <SheetContent className="overflow-y-auto">
        <SheetHeader className="mb-6">
          <div className="flex flex-wrap gap-2 mb-3">
            <Badge variant={course.track === "minor" ? "minor" : "concentration"}>
              {course.track === "minor" ? "Sports Medicine Minor" : "Concentration"}
            </Badge>
            {course._inferred && (
              <Badge variant="proposed">
                Proposed — pending faculty validation
              </Badge>
            )}
            <Badge variant="outline">{course.credits} Credits</Badge>
          </div>
          <SheetTitle className="text-xl" style={{ color: "#003D7A" }}>
            {courseId}: {course.title}
          </SheetTitle>
          <SheetDescription>{course.semester} · Level {course.level}</SheetDescription>
        </SheetHeader>

        <div className="space-y-6">
          <div>
            <h4 className="font-semibold text-sm uppercase tracking-wide text-gray-500 mb-2">
              Description
            </h4>
            <p className="text-sm text-gray-700 leading-relaxed">
              {course.description}
            </p>
          </div>

          <div>
            <h4 className="font-semibold text-sm uppercase tracking-wide text-gray-500 mb-2">
              Prerequisites
            </h4>
            {course.prerequisites.length > 0 ? (
              <ul className="list-disc list-inside space-y-1">
                {course.prerequisites.map((p) => (
                  <li key={p} className="text-sm text-gray-700">
                    {p}
                  </li>
                ))}
              </ul>
            ) : (
              <p className="text-sm text-gray-500">None</p>
            )}
          </div>

          <div>
            <h4 className="font-semibold text-sm uppercase tracking-wide text-gray-500 mb-2">
              Course Learning Outcomes (CLOs)
            </h4>
            <ul className="space-y-2">
              {course.clos.map((clo, i) => (
                <li key={i} className="flex gap-3">
                  <span
                    className="w-6 h-6 rounded-full flex-shrink-0 flex items-center justify-center text-xs text-white font-bold mt-0.5"
                    style={{ backgroundColor: "#003D7A" }}
                  >
                    {i + 1}
                  </span>
                  <p className="text-sm text-gray-700 leading-relaxed">
                    {clo.replace(/^CLO\d+:\s*/, "")}
                  </p>
                </li>
              ))}
            </ul>
          </div>

          <div>
            <h4 className="font-semibold text-sm uppercase tracking-wide text-gray-500 mb-2">
              Programme Learning Outcomes (PLOs)
            </h4>
            <div className="flex flex-wrap gap-2">
              {course.plos.map((plo) => (
                <Badge key={plo} variant="outline">
                  {plo}
                </Badge>
              ))}
            </div>
          </div>

          {course.icreps_alignment && (
            <div>
              <h4 className="font-semibold text-sm uppercase tracking-wide text-gray-500 mb-2">
                ICREPs / REPs UAE Alignment
              </h4>
              <p className="text-sm text-gray-700 leading-relaxed">
                {course.icreps_alignment}
              </p>
            </div>
          )}

          {course.reps_gaps_closed && course.reps_gaps_closed.length > 0 && (
            <div>
              <h4 className="font-semibold text-sm uppercase tracking-wide text-gray-500 mb-2">
                Regulatory Gaps Closed
              </h4>
              <ul className="list-disc list-inside space-y-1">
                {course.reps_gaps_closed.map((g) => (
                  <li key={g} className="text-sm text-gray-700">
                    {g}
                  </li>
                ))}
              </ul>
            </div>
          )}

          {course.embedded_certifications && (
            <div>
              <h4 className="font-semibold text-sm uppercase tracking-wide text-gray-500 mb-2">
                Embedded Certifications
              </h4>
              <div className="flex flex-wrap gap-2">
                {course.embedded_certifications.map((cert) => (
                  <Badge key={cert} variant="gold">
                    {cert}
                  </Badge>
                ))}
              </div>
            </div>
          )}

          {course._inferred && (
            <div className="bg-amber-50 border border-amber-200 rounded-lg p-4">
              <p className="text-xs text-amber-800 font-medium">
                Note: This course is proposed. CLOs and PLO mappings are
                inferred pending faculty review and formal syllabus authoring
                before UGCC submission.
              </p>
            </div>
          )}
        </div>
      </SheetContent>
    </Sheet>
  );
}

export function CourseGrid({ data }: CourseGridProps) {
  const [selectedCourse, setSelectedCourse] = useState<string | null>(null);
  const ref = useRef<HTMLDivElement>(null);
  const isInView = useInView(ref, { once: true, margin: "-80px" });

  const courseEntries = Object.entries(data.courses);

  return (
    <section id="courses" className="py-20 px-6" style={{ backgroundColor: "#f8f9fc" }}>
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
            Academic Programme
          </p>
          <h2
            className="text-3xl md:text-4xl font-bold"
            style={{ color: "#003D7A" }}
          >
            Course Catalogue
          </h2>
          <p className="text-gray-500 mt-3 max-w-2xl mx-auto">
            Eight SPMD courses across two tracks. Click any card to view full
            CLO/PLO details.
          </p>
          <div className="flex flex-wrap justify-center gap-4 mt-6">
            <div className="flex items-center gap-2 text-sm text-gray-600">
              <span className="w-3 h-3 rounded-full bg-[#003D7A] inline-block" />
              Sports Medicine Minor (SPMD 301-304) — Pending UGCC review
            </div>
            <div className="flex items-center gap-2 text-sm text-gray-600">
              <span className="w-3 h-3 rounded-full bg-[#C8A04A] inline-block" />
              Concentration (SPMD 305-308) — Proposed
            </div>
          </div>
        </motion.div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
          {courseEntries.map(([id, course], i) => (
            <motion.div
              key={id}
              initial={{ opacity: 0, y: 30 }}
              animate={isInView ? { opacity: 1, y: 0 } : {}}
              transition={{ duration: 0.5, delay: i * 0.07 }}
            >
              <Card
                className="h-full cursor-pointer hover:shadow-md transition-shadow border-2 hover:border-[#003D7A]"
                style={{
                  borderColor:
                    course.track === "minor"
                      ? "rgba(0,61,122,0.2)"
                      : "rgba(200,160,74,0.3)",
                }}
                onClick={() => setSelectedCourse(id)}
              >
                <CardHeader className="pb-3">
                  <div className="flex flex-wrap gap-1 mb-2">
                    <Badge
                      variant={course.track === "minor" ? "minor" : "concentration"}
                      className="text-xs"
                    >
                      {course.track === "minor" ? "Minor" : "Concentration"}
                    </Badge>
                    {course._inferred && (
                      <Badge variant="proposed" className="text-xs">
                        Proposed
                      </Badge>
                    )}
                  </div>
                  <p
                    className="text-xs font-bold uppercase tracking-wider"
                    style={{
                      color: course.track === "minor" ? "#003D7A" : "#C8A04A",
                    }}
                  >
                    {id}
                  </p>
                  <CardTitle className="text-sm leading-tight">
                    {course.title}
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <CardDescription className="text-xs leading-relaxed line-clamp-3 mb-4">
                    {course.description}
                  </CardDescription>
                  <div className="space-y-1.5">
                    <div className="flex items-center gap-2 text-xs text-gray-500">
                      <Clock className="w-3 h-3" />
                      {course.semester}
                    </div>
                    <div className="flex items-center gap-2 text-xs text-gray-500">
                      <BookOpen className="w-3 h-3" />
                      {course.credits} credits · {course.lecture_hours}h lecture
                    </div>
                    {course.laboratory_hours > 0 && (
                      <div className="flex items-center gap-2 text-xs text-gray-500">
                        <FlaskConical className="w-3 h-3" />
                        {course.laboratory_hours}h lab/week
                      </div>
                    )}
                  </div>
                  <div className="flex flex-wrap gap-1 mt-3">
                    {course.plos.map((plo) => (
                      <span
                        key={plo}
                        className="text-xs px-1.5 py-0.5 rounded border border-gray-200 text-gray-500"
                      >
                        {plo}
                      </span>
                    ))}
                  </div>
                  <p className="text-xs text-[#003D7A] mt-3 font-medium">
                    View CLOs &amp; PLOs →
                  </p>
                </CardContent>
              </Card>
            </motion.div>
          ))}
        </div>
      </div>

      {selectedCourse && data.courses[selectedCourse] && (
        <CourseDrawer
          courseId={selectedCourse}
          course={data.courses[selectedCourse]}
          open={!!selectedCourse}
          onClose={() => setSelectedCourse(null)}
        />
      )}
    </section>
  );
}
