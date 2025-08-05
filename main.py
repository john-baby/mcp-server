from server import mcp

import tools.check_leave_balance
import tools.apply_leave

if __name__ == "__main__":
    mcp.run(transport='streamable-http')