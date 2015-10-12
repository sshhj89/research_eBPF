#include <uapi/linux/ptrace.h>
#include <linux/sched.h>

struct infoTaskCPU
{
	u32 cpu;
	u32 pid;
};

BPF_TABLE("hash", struct infoTaskCPU, u64, stats, 1024);

int count_sched(struct pt_regs *ctx, struct task_struct *prev) {
  u64 zero = 0, *val;
  struct infoTaskCPU itC;


  itC.cpu =  bpf_get_smp_processor_id();
  itC.pid = prev->pid;
  
  val = stats.lookup_or_init(&itC, &zero);
  (*val)++;
  return 0;
}

