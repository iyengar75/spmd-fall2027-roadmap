export interface Course {
  title: string;
  credits: number;
  lecture_hours: number;
  laboratory_hours: number;
  level: number;
  semester: string;
  prerequisites: string[];
  track: "minor" | "concentration";
  status: string;
  description: string;
  clos: string[];
  plos: string[];
  ku_gelo: string[];
  _inferred: boolean;
  icreps_alignment?: string;
  reps_gaps_closed?: string[];
  embedded_certifications?: string[];
}

export interface Track {
  id: string;
  name: string;
  credits_total: number;
  courses: string[];
  status: string;
  icreps_eligible: boolean;
  note: string;
}

export interface Phase {
  q: string;
  label: string;
  date_range: string;
  deliverables: {
    minor: string;
    concentration: string;
  };
  gate: string;
  owner: string;
  decision_maker: string;
  key_actions: string[];
}

export interface RegulatorAlignment {
  [courseId: string]: string;
}

export interface Regulator {
  full_name: string;
  name_ar: string;
  url: string;
  level: string;
  scope: string;
  tier: string;
  alignment: RegulatorAlignment;
}

export interface SiteData {
  program: {
    name: string;
    full_name: string;
    institution: string;
    college: string;
    launch: string;
    target_intake: string;
    total_credits_baseline: number;
    total_credits_with_concentration: number;
    qf_emirates_level: number;
    adek_submission_version: string;
    note: string;
  };
  tracks: Track[];
  courses: Record<string, Course>;
  phases: Phase[];
  regulators: Record<string, Regulator>;
  ku_brand: {
    navy: string;
    gold: string;
  };
  bscnd_plos: Array<{
    id: string;
    label: string;
    description: string;
    qfemirates_alignment: string;
  }>;
}
