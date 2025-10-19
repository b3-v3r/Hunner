# Author B3avers
import urllib.request as urllib2
import re
import sys
import os
import random

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, IntPrompt

console = Console()
THEME = "#7B61FF"
TABLE_MODE = False

def display_table(title: str, rows: list):
    tbl = Table(title=title, show_lines=True, border_style=THEME)
    tbl.add_column("Index", justify="center", no_wrap=True)
    tbl.add_column("Action", justify="left")
    tbl.add_column("Description", justify="left")
    for idx, action, desc_text in rows:
        tbl.add_row(str(idx), str(action), str(desc_text))
    console.print(tbl)
    
def info():
    VERSION = "[bold]" + "1.0" + "[/bold]"
    AUTHOR = "[bold]" + "B3-v3r" + "[/bold]"
    panel_text = f"\n\n          Version -> {VERSION}\n\n          Author  -> {AUTHOR}\n"
    console.print(Panel(panel_text, title="[bold]Hunner Info[/bold]", border_style=THEME))

def XXS():
    os.system("clear")
    console.print(Panel("[bold]XXS Scanner[/bold]", border_style=THEME))
    while True:
        try:
            site = console.input(f"[{THEME}]Hunner»XXS» [/]")
        except Exception:
            console.print("[red]\nError[/red]")
            return

        cmd = site.strip().lower()
        if cmd == "help":
            help_tbl = Table(title="XXS — Usage Help", show_lines=True, border_style=THEME)
            help_tbl.add_column("Field", justify="left", no_wrap=True)
            help_tbl.add_column("Description", justify="left")
            help_tbl.add_row("What it does", "Checks a site for a simple reflected XSS by appending a test payload and looking for it in the response.")
            help_tbl.add_row("Input format", "Enter a target URL. If scheme missing, http:// will be added automatically.")
            help_tbl.add_row("Requirement", "Target URL should contain an 'id=' parameter to test injectable parameter behavior.")
            help_tbl.add_row("Example", "example.com/page.php?id=1  → or → http://example.com/page.php?id=1")
            help_tbl.add_row("Commands", "'help' → show this help | 'back' or 'exit' → return to main menu")
            help_tbl.add_row("Payload shown", "If vulnerable, payload and response info will be printed")
            console.print(help_tbl)
            continue
        if cmd in ("back", "exit", "99"):
            return

        if "http://" not in site and "https://" not in site:
            site = "http://" + site

        if "id=" not in site:
            console.print(f"[red][!][/red] Site does not have an 'id' parameter")
        else:
            console.print(f"[yellow][*][/yellow] [green]Site {site} has an 'id' param[/green]")

        try:
            res = urllib2.urlopen(site)
        except Exception:
            console.print("[red][!] Site not reachable[/red]")
            return

        try:
            console.print("[yellow][+][/yellow] [green]Site reachable[/green]")
            scr = ';<script>alert(111111111111111111111);</script>'
            site_xxs = site + scr
            res = urllib2.urlopen(site_xxs)
            info_hdr = res.info()
            console.print(Panel(str(info_hdr), title="Response Headers", border_style=THEME))
            text = res.read()

            if "111111111111111111111" not in str(text):
                console.print("[red][!][/red] Site does not appear vulnerable to this simple XSS test")
                return
            else:
                console.print(f"[underline][yellow][++] [/yellow][bold blue]Site {site} is vulnerable to reflected XSS[/bold blue][/underline]")
                console.print(f"[yellow]Payload:[/yellow] [green]{site_xxs}[/green]")
                sys.exit(1)

        except Exception:
            console.print("[red][!][/red] Fatal Error")
            return


def desc():
    console.print(Panel(
        "This program was created for review and not for causing harm.\n\n"
        "Usage of hunner for attacking targets without prior mutual consent is illegal.\n\n"
        "Developers assume no liability and are not responsible for any misuse or damage caused by this program.",
        title="Disclaimer",
        border_style=THEME
    ))

def SQL():
    os.system("clear")
    console.print(Panel("[bold]SQL Scanner[/bold]", border_style=THEME))
    site = console.input(f"[{THEME}]Hunner»SqlScaner»[/]{''}")
    if "http://" not in site and "https://" not in site:
        site = "http://" + site
    else:
        pass
    if "id=" not in site:
        console.print("[red][!][/red] Site don't have id parameters")
    else:
        console.print(f"[yellow][*][/yellow] [green]Site {site} have \"id\" param[/green]")
    try:
        res = urllib2.urlopen(site)
        console.print("[yellow][+][/yellow] [green]Site work[/green]")
    except Exception:
        console.print("[red][!][/red] Site dont work")
        return
    try:
        info_hdr = res.info()
        console.print(Panel(str(info_hdr), title="##################### Info #####################", border_style=THEME))
        bad_site = site + "\'\""
        res = urllib2.urlopen(bad_site)
        text = res.read()
        if "You have an error in your SQL syntax" not in str(text):
            console.print(f"[yellow][--][/yellow][red] Site {site} not have Sql Error[/red]")
        else:
            console.print(f"[yellow][++][/yellow][bold]{site} have SQL Error[/bold]")
            y = Prompt.ask("Start sqlmap ? (Y/n)", default="n")
            if y == "Y" or y == "y":
                os.system("sqlmap -u " + site + " --dbs")
            else:
                console.print("[yellow]<< Good by >>[/yellow]")
    except Exception:
        console.print("[red]Fatal error[/red]")

def Dos():
    """
    DoS module (safe, non-destructive interactive UI).
    - 'help' shows a detailed help table.
    - Accepts a target and level, but never executes destructive commands.
    - Requires exact confirmation "I HAVE PERMISSION" before showing a simulated command.
    - 'back', 'exit', or '99' return to the main menu.
    """
    os.system("clear")
    console.print(Panel("[bold]DoS Module — Safe Mode[/bold]", border_style=THEME))
    while True:
        try:
            cmd = console.input(f"[{THEME}]Hunner»Dos» [/]").strip()
        except Exception:
            console.print("[red]\nError[/red]")
            return

        lc = cmd.lower()
        if lc == "help":
            help_tbl = Table(title="DoS — Usage Help (Safe Mode)", show_lines=True, border_style=THEME)
            help_tbl.add_column("Field", justify="left", no_wrap=True)
            help_tbl.add_column("Description", justify="left")
            help_tbl.add_row("What it does", "Simulates DoS options and shows the commands that *would* be used — it will NOT run any attack.")
            help_tbl.add_row("Input format", "Enter a target host or IP (e.g. example.com or 192.0.2.1). Then choose level 1 / 2 / 3.")
            help_tbl.add_row("Levels", "1 = High (simulated hping3 flood)\n2 = Port (simulated hping3 against a port)\n3 = Low (simulated local module)")
            help_tbl.add_row("Examples", "example.com → then choose level 1/2/3\nexample.com (then level 2) → you'll be asked for port e.g. 80")
            help_tbl.add_row("Safety", "This tool will NOT execute attacks. DoS is illegal without explicit permission.")
            help_tbl.add_row("Authorized testing", "For legal load-testing use tools like locust or k6 in a lab or with written permission.")
            help_tbl.add_row("Commands", "'help' → show help | 'back' or 'exit' or '99' → return to main menu")
            console.print(help_tbl)
            continue

        if lc in ("back", "exit", "99"):
            return

        target = cmd
        if target == "":
            console.print("[red][!][/red] Enter a target host or type 'help' for usage")
            continue

        console.print(Panel(f"[bold]Selected target:[/bold] {target}", border_style=THEME))

        try:
            console.print(
                "Enter level:\n"
                "  1) High dos (simulated hping3 flood)\n"
                "  2) Dos port (simulated hping3 against a given port)\n"
                "  3) Low dos (simulated local module)\n"
            )
            level_input = console.input(f"[{THEME}]Hunner»Dos»Level» [/]").strip()
            if level_input.lower() in ("back", "exit", "99"):
                return
            level = int(level_input)
            if level not in (1, 2, 3):
                raise ValueError
        except Exception:
            console.print("[red][!][/red] Invalid level — please enter 1, 2 or 3")
            continue

        if level == 1:
            console.print("[yellow]High DoS (SIMULATION) selected.[/yellow]")
            simulated_cmd = f"hping3 -S -P --flood -V {target}"
        elif level == 2:
            port = console.input(f"[{THEME}]Hunner»Dos»Level»Port» [/]").strip()
            if port.lower() in ("back", "exit", "99") or port == "":
                console.print("[red]Port required for level 2[/red]")
                continue
            console.print(f"[yellow]Port-targeted DoS (SIMULATION) selected for port {port}.[/yellow]")
            simulated_cmd = f"hping3 -S -P --flood -V -p {port} {target}"
        else:  # level == 3
            console.print("[yellow]Low DoS (SIMULATION) selected.[/yellow]")
            simulated_cmd = f"python3 modules/dos.py {target}  # (simulated)"

        console.print("\n[bold]Safety check:[/bold] To proceed, you must confirm you have written permission to test the target.")
        console.print("[dim]Type exactly: I HAVE PERMISSION  —  (case sensitive)[/dim]")
        confirm = console.input(f"[{THEME}]Confirm→ [/]").strip()
        if confirm != "I HAVE PERMISSION":
            console.print("[red]Permission not confirmed. Aborting action.[/red]")
            console.print("[green]Tip:[/green] If you want to learn about legal load-testing tools, type 'help' for alternatives.")
            continue

        sim_tbl = Table(title="Simulated Command (NOT EXECUTED)", show_lines=True, border_style=THEME)
        sim_tbl.add_column("Field", justify="left", no_wrap=True)
        sim_tbl.add_column("Value", justify="left")
        sim_tbl.add_row("Target", target)
        sim_tbl.add_row("Level", str(level))
        sim_tbl.add_row("Command", simulated_cmd)
        sim_tbl.add_row("Note", "This command is shown for educational/reference purposes and is NOT executed by this program.")
        console.print(sim_tbl)

        alt_tbl = Table(title="Safe Alternatives for Authorized Testing", show_lines=True, border_style=THEME)
        alt_tbl.add_column("Tool", justify="left", no_wrap=True)
        alt_tbl.add_column("Use case", justify="left")
        alt_tbl.add_row("locust", "Distributed load testing in a controlled environment (Python-based).")
        alt_tbl.add_row("k6", "Modern load-testing tool with scripting (JavaScript) and cloud options.")
        alt_tbl.add_row("wrk / wrk2", "Lightweight benchmarking tools for HTTP performance.")
        alt_tbl.add_row("Change approach", "Set up a private lab or use a staging server you control for stress tests.")
        console.print(alt_tbl)

        console.print("[green]Simulation complete. No destructive action was performed.[/green]")
        return

def SSH_Brut():
    """
    SSH brute UI (safe, non-destructive):
    - 'help' shows a detailed help table.
    - Accepts host, username and password file, but NEVER runs brute-force.
    - Requires exact confirmation "I HAVE PERMISSION" before showing a simulated command.
    - 'back', 'exit', or '99' return to the main menu.
    """
    os.system("clear")
    console.print(Panel("[bold]SSH Bruteforce — Safe Mode[/bold]", border_style=THEME))
    while True:
        try:
            cmd = console.input(f"[{THEME}]Hunner»SSH» [/]").strip()
        except Exception:
            console.print("[red]\nError[/red]")
            return

        lc = cmd.lower()
        if lc == "help":
            help_tbl = Table(title="SSH Bruteforce — Usage Help (Safe Mode)", show_lines=True, border_style=THEME)
            help_tbl.add_column("Field", justify="left", no_wrap=True)
            help_tbl.add_column("Description", justify="left")
            help_tbl.add_row("What it does", "Provides a safe UI for SSH brute-force parameters — it will NOT execute attacks.")
            help_tbl.add_row("Input format", "Enter target host (hostname or IP). Then you'll be asked for username and password list file.")
            help_tbl.add_row("Defaults", "If username left blank, 'admin' will be used as a default suggestion.")
            help_tbl.add_row("Password file", "Provide a path to your password list file (e.g. wordlists/pass.txt).")
            help_tbl.add_row("Commands", "'help' → show this help | 'back' or 'exit' or '99' → return to main menu")
            help_tbl.add_row("Safety", "Brute-force attacks are illegal without explicit permission. This UI only simulates the action.")
            help_tbl.add_row("Authorized testing", "Use authorized pentest frameworks and obtain written permission before testing.")
            console.print(help_tbl)
            continue

        if lc in ("back", "exit", "99"):
            return

        host = cmd
        if host == "":
            console.print("[red][!][/red] Enter target host or type 'help' for usage")
            continue

        console.print("[green]Enter username (leave blank for default 'admin')[/green]")
        user = console.input(f"[{THEME}]Hunner»SSH»User» [/]").strip()
        if user == "":
            user = "admin"

        console.print("[green]Enter password file path (e.g. password/password_list.txt)[/green]")
        password_file = console.input(f"[{THEME}]Hunner»SSH»PasswordFile» [/]").strip()
        if password_file == "":
            console.print("[red][!][/red] Password file required for a brute-force attempt (simulation).")
            continue

        console.print(Panel(f"[bold]Target:[/bold] {host}\n[bold]User:[/bold] {user}\n[bold]Password file:[/bold] {password_file}", border_style=THEME))
        
        console.print("\n[bold]Safety check:[/bold] To proceed, you must confirm you have written permission to test the target.")
        console.print("[dim]Type exactly: I HAVE PERMISSION  —  (case sensitive)[/dim]")
        confirm = console.input(f"[{THEME}]Confirm→ [/]").strip()
        if confirm != "I HAVE PERMISSION":
            console.print("[red]Permission not confirmed. Aborting action.[/red]")
            console.print("[green]Tip:[/green] If you want to learn about legal assessment, type 'help' for alternatives.")
            continue

        simulated_cmd = f"python3 modules/ssh.py {host} {user} {password_file}  # (simulated)"
        sim_tbl = Table(title="Simulated SSH Brute Command (NOT EXECUTED)", show_lines=True, border_style=THEME)
        sim_tbl.add_column("Field", justify="left", no_wrap=True)
        sim_tbl.add_column("Value", justify="left")
        sim_tbl.add_row("Target", host)
        sim_tbl.add_row("Username", user)
        sim_tbl.add_row("Password file", password_file)
        sim_tbl.add_row("Simulated Command", simulated_cmd)
        sim_tbl.add_row("Note", "This command is shown for educational/reference purposes and is NOT executed by this program.")
        console.print(sim_tbl)

        alt_tbl = Table(title="Safe Alternatives & Resources", show_lines=True, border_style=THEME)
        alt_tbl.add_column("Tool/Resource", justify="left", no_wrap=True)
        alt_tbl.add_column("Use case", justify="left")
        alt_tbl.add_row("ssh (manual)", "Use for legitimate admin access when you have credentials.")
        alt_tbl.add_row("authorized pentesting", "Obtain written permission and use frameworks like Metasploit with care.")
        alt_tbl.add_row("credential auditing", "Use password auditing tools on systems you own (e.g., Hydra in a lab with permission).")
        alt_tbl.add_row("Change approach", "Set up a lab VM or staging environment to practice safely.")
        console.print(alt_tbl)

        console.print("[green]Simulation complete. No destructive or unauthorized action was performed.[/green]")
        return


def FTP_Brut():
    """
    FTP brute UI (safe, non-destructive):
    - 'help' shows a detailed help table.
    - Accepts host, username and password file, but NEVER runs brute-force commands.
    - Requires exact confirmation "I HAVE PERMISSION" before showing a simulated action summary.
    - 'back', 'exit', or '99' return to the main menu.
    """
    os.system("clear")
    console.print(Panel("[bold]FTP Bruteforce — Safe Mode[/bold]", border_style=THEME))
    while True:
        try:
            cmd = console.input(f"[{THEME}]Hunner»Ftp» [/]").strip()
        except Exception:
            console.print("[red]\nError[/red]")
            return

        lc = cmd.lower()
        if lc == "help":
            help_tbl = Table(title="FTP Bruteforce — Usage Help (Safe Mode)", show_lines=True, border_style=THEME)
            help_tbl.add_column("Field", justify="left", no_wrap=True)
            help_tbl.add_column("Description", justify="left")
            help_tbl.add_row("What it does", "Provides a safe UI for FTP brute-force parameters — it will NOT execute attacks.")
            help_tbl.add_row("Input format", "Enter target host (hostname or IP). Then you'll be asked for username and a password list file path.")
            help_tbl.add_row("Defaults", "If username left blank, 'admin' will be suggested as a default.")
            help_tbl.add_row("Password file", "Provide a path to a password list file (e.g. wordlists/ftp_passwords.txt).")
            help_tbl.add_row("Commands", "'help' → show this help | 'back' or 'exit' or '99' → return to main menu")
            help_tbl.add_row("Safety", "Brute-force attacks are illegal without explicit permission. This UI only simulates the action.")
            help_tbl.add_row("Authorized testing", "Use credential-auditing in a controlled lab or with written permission.")
            console.print(help_tbl)
            continue

        if lc in ("back", "exit", "99"):
            return

        host = cmd
        if host == "":
            console.print("[red][!][/red] Enter target host or type 'help' for usage")
            continue

        console.print("[green]Enter username (leave blank for default 'admin')[/green]")
        user = console.input(f"[{THEME}]Hunner»Ftp»User» [/]").strip()
        if user == "":
            user = "admin"

        console.print("[green]Enter password file path (e.g. wordlists/ftp_passwords.txt)[/green]")
        password_file = console.input(f"[{THEME}]Hunner»Ftp»Password» [/]").strip()
        if password_file == "":
            console.print("[red][!][/red] Password file required for a brute-force attempt (simulation).")
            continue

        console.print(Panel(f"[bold]Target:[/bold] {host}\n[bold]User:[/bold] {user}\n[bold]Password file:[/bold] {password_file}", border_style=THEME))

        console.print("\n[bold]Safety check:[/bold] To proceed, you must confirm you have written permission to test the target.")
        console.print("[dim]Type exactly: I HAVE PERMISSION  —  (case sensitive)[/dim]")
        confirm = console.input(f"[{THEME}]Confirm→ [/]").strip()
        if confirm != "I HAVE PERMISSION":
            console.print("[red]Permission not confirmed. Aborting action.[/red]")
            console.print("[green]Tip:[/green] If you want to learn about legal credential-auditing, type 'help' for alternatives.")
            continue

        sim_tbl = Table(title="Simulated FTP Brute Action (NOT EXECUTED)", show_lines=True, border_style=THEME)
        sim_tbl.add_column("Field", justify="left", no_wrap=True)
        sim_tbl.add_column("Value", justify="left")
        sim_tbl.add_row("Target", host)
        sim_tbl.add_row("Username", user)
        sim_tbl.add_row("Password file", password_file)
        sim_tbl.add_row("Action (simulated)", "Would run FTP brute-force module with the above parameters (simulation only).")
        sim_tbl.add_row("Note", "This action is shown for educational/reference purposes and is NOT executed by this program.")
        console.print(sim_tbl)

        alt_tbl = Table(title="Safe Alternatives & Resources", show_lines=True, border_style=THEME)
        alt_tbl.add_column("Tool/Approach", justify="left", no_wrap=True)
        alt_tbl.add_column("Use case", justify="left")
        alt_tbl.add_row("Local lab VM", "Set up a VM with an FTP server to practice safely.")
        alt_tbl.add_row("Credential auditing tools", "Use authorized auditing frameworks in a controlled environment.")
        alt_tbl.add_row("Monitoring & alerts", "Implement login-rate limiting and monitoring on production services.")
        alt_tbl.add_row("Change approach", "Perform testing only on systems you own or with written permission.")
        console.print(alt_tbl)

        console.print("[green]Simulation complete. No destructive or unauthorized action was performed.[/green]")
        return


def mail():
    """
    Mail brute UI (safe, non-destructive):
    - 'help' shows a detailed help table.
    - Accepts mail/login and a password list file, but NEVER runs brute-force commands.
    - Requires exact confirmation "I HAVE PERMISSION" before showing a simulated action summary.
    - 'back', 'exit', or '99' return to the main menu.
    """
    os.system("clear")
    console.print(Panel("[bold]Mail Bruteforce — Safe Mode[/bold]", border_style=THEME))
    while True:
        try:
            cmd = console.input(f"[{THEME}]Hunner»Mail» [/]").strip()
        except Exception:
            console.print("[red]\nError[/red]")
            return

        lc = cmd.lower()
        if lc == "help":
            help_tbl = Table(title="Mail Bruteforce — Usage Help (Safe Mode)", show_lines=True, border_style=THEME)
            help_tbl.add_column("Field", justify="left", no_wrap=True)
            help_tbl.add_column("Description", justify="left")
            help_tbl.add_row("What it does", "Provides a safe UI for mail credential brute-force parameters — it will NOT execute attacks.")
            help_tbl.add_row("Input format", "Enter the email/login (e.g. user@example.com). Then you'll be asked for a password list file path.")
            help_tbl.add_row("Password file", "Provide a path to a password list file (e.g. wordlists/mail_passwords.txt).")
            help_tbl.add_row("Commands", "'help' → show this help | 'back' or 'exit' or '99' → return to main menu")
            help_tbl.add_row("Safety", "Brute-force or credential stuffing is illegal without explicit permission. This UI only simulates the action.")
            help_tbl.add_row("Authorized testing", "Use credential auditing on systems you own or with written permission; consider using rate-limited, controlled tests.")
            console.print(help_tbl)
            continue

        if lc in ("back", "exit", "99"):
            return

        mail_login = cmd
        if mail_login == "":
            console.print("[red][!][/red] Enter the target email/login or type 'help' for usage")
            continue

        console.print("[green]Enter password file path (e.g. password/password_list.txt). Leave blank to use default suggestion.[/green]")
        password_file = console.input(f"[{THEME}]Hunner»Mail»Password» [/]").strip()
        if password_file == "":
            console.print("[dim]No file entered. Default will be used: password/password_list.txt[/dim]")
            password_file = "password/password_list.txt"

        console.print(Panel(f"[bold]Target Email:[/bold] {mail_login}\n[bold]Password file:[/bold] {password_file}", border_style=THEME))

        console.print("\n[bold]Safety check:[/bold] To proceed, you must confirm you have written permission to test the target.")
        console.print("[dim]Type exactly: I HAVE PERMISSION  —  (case sensitive)[/dim]")
        confirm = console.input(f"[{THEME}]Confirm→ [/]").strip()
        if confirm != "I HAVE PERMISSION":
            console.print("[red]Permission not confirmed. Aborting action.[/red]")
            console.print("[green]Tip:[/green] If you want to learn about legal assessment, type 'help' for alternatives.")
            continue

        sim_tbl = Table(title="Simulated Mail Brute Action (NOT EXECUTED)", show_lines=True, border_style=THEME)
        sim_tbl.add_column("Field", justify="left", no_wrap=True)
        sim_tbl.add_column("Value", justify="left")
        sim_tbl.add_row("Target Email", mail_login)
        sim_tbl.add_row("Password file", password_file)
        sim_tbl.add_row("Action (simulated)", "Would run mail brute-force module with the above parameters (simulation only).")
        sim_tbl.add_row("Note", "This action is shown for educational/reference purposes and is NOT executed by this program.")
        console.print(sim_tbl)

        alt_tbl = Table(title="Safe Alternatives & Resources", show_lines=True, border_style=THEME)
        alt_tbl.add_column("Tool/Approach", justify="left", no_wrap=True)
        alt_tbl.add_column("Use case", justify="left")
        alt_tbl.add_row("Credential auditing (in lab)", "Use on systems you control to validate password strength and policies.")
        alt_tbl.add_row("Rate-limited testing", "Perform tests with rate limiting to avoid service disruption and to stay ethical.")
        alt_tbl.add_row("Password hygiene", "Encourage MFA, password policies, and breach-detection for real environments.")
        alt_tbl.add_row("Change approach", "Use a staging server or VM for practicing brute-force techniques safely.")
        console.print(alt_tbl)

        console.print("[green]Simulation complete. No destructive or unauthorized action was performed.[/green]")
        return


def Main_Menu():
    """Full-screen, terminal-filling main menu using rich Layout."""
    from rich.layout import Layout
    from rich.align import Align
    from rich.box import ROUNDED, DOUBLE
    from rich import box

    global TABLE_MODE
    desc()
    console.clear()

    layout = Layout(name="root")
    layout.split(
        Layout(name="header", size=3),
        Layout(name="body", ratio=1),
        Layout(name="footer", size=3),
    )

    body_inner = Layout(name="body_inner")
    body_inner.split_row(Layout(name="menu"), Layout(name="info", ratio=2))
    layout["body"].update(body_inner)

    header_text = Align.center(f"[bold]{' HUNNER ':=^{console.width - 2}}", vertical="middle")
    layout["header"].update(Panel(header_text, style=f"bold {THEME}", box=ROUNDED, padding=(0,1)))

    menu_tbl = Table.grid(padding=(0,2))
    menu_tbl.add_column(justify="center", ratio=1, no_wrap=True)
    menu_tbl.add_column(ratio=4)

    menu_tbl.add_row(f"[bold cyan]◈[/bold cyan] [bold underline]Hunner Menu[/bold underline]", "")

    tools = [
        ("1", "XXS", "Quick XSS check using an alert payload and response verification"),
        ("2", "Sql", "Simple SQL error injection test and optional sqlmap trigger"),
        ("3", "Dos site", "Choose DoS intensity or run local DoS module"),
        ("4", "Brute Ftp", "FTP credential brute-force using provided wordlist"),
        ("5", "Brute SSH", "SSH brute-force with username and password list"),
        ("6", "Brute mails", "Mail account brute-force using a password list"),
        ("7", "Toggle Table Mode", f"Switch menu display between classic and modern table (current: {'ON' if TABLE_MODE else 'OFF'})"),
        ("99", "Return to Menu / Exit", "Exit the program or return to previous menu"),
    ]
    
    for idx, action, desc_text in tools:
        menu_tbl.add_row(f"[bold cyan]{idx}[/bold cyan]", f"[bold]{action}[/bold]\n[dim]{desc_text}[/dim]")

    menu_panel = Panel(menu_tbl, title="[bold]Options[/bold]", border_style=THEME, box=DOUBLE, padding=(1,2), expand=True)
    body_inner["menu"].update(menu_panel)

    info_tbl = Table.grid(expand=True)
    info_tbl.add_row(f"[bold]Tip:[/bold] Type the option number and press Enter")
    info_tbl.add_row("")
    info_tbl.add_row("[bold]Help:[/bold] type 'help' to show tool info")
    info_tbl.add_row("")
    info_tbl.add_row(Align.left("[italic]Disclaimer: Use responsibly. See program disclaimer above.[/italic]"))
    info_panel = Panel(info_tbl, title="[bold]Info & Hints[/bold]", border_style=THEME, box=ROUNDED, padding=(1,2), expand=True)
    body_inner["info"].update(info_panel)

    footer_text = Align.center("[bold]Enter choice →[/bold]", vertical="middle")
    layout["footer"].update(Panel(footer_text, border_style=THEME, box=ROUNDED, padding=(0,1)))

    console.print(layout)

    try:
        v = console.input("\n[bold]Hunner-» [/bold]")
    except Exception:
        console.print(" Good by ")
        sys.exit()

    if v == "help":
        info()
    else:
        try:
            vi = int(v)
        except Exception:
            console.print("[red][!][/red] You entered an incorrect value")
            sys.exit()

        if vi == 1:
            XXS()
        elif vi == 2:
            SQL()
        elif vi == 3:
            Dos()
        elif vi == 4:
            FTP_Brut()
        elif vi == 5:
            SSH_Brut()
        elif vi == 6:
            mail()
        elif vi == 7:
            TABLE_MODE = not TABLE_MODE
            console.print(f"[bold]Table Mode turned {'ON' if TABLE_MODE else 'OFF'}[/bold]")
            Main_Menu()
        elif vi == 99:
            console.print("[bold]Exiting...[/bold]")
            sys.exit()
        else:
            console.print("[red][!][/red] You entered an incorrect value")
            sys.exit()

            
if __name__ == "__main__":
    Main_Menu()
