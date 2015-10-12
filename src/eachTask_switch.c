#include <uapi/linux/ptrace.h>
#include <linux/sched.h>

// map_type, key_type, leaf_type, table_name, num_entry
BPF_TABLE("hash", u32, u64, stats, 1024);
int count_sched(struct pt_regs *ctx, struct task_struct *curr) {
  u32 pid = 0;
  u64 zero = 0, *val;
  u32 n = 0;
 
  pid = bpf_get_current_pid_tgid();

  bpf_probe_read(&n, sizeof(int),(void*)curr->nvcsw); 
  bpf_trace_printk("nvcsw : %d\n", n ); 
  zero = curr->nvcsw + curr->nivcsw;
  val = stats.lookup_or_init(&pid, &zero);
//  (*val)++;
  return 0;
}	
