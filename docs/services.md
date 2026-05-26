# Service Selection

This project checks only public Serbian e-government availability. It does not log in, submit forms, bypass CAPTCHA, scrape private data, or collect personal data.

Reviewed source for additional candidates: https://www.srb.guide/

## Selected Services

| Service | URL | Group | Reason |
| --- | --- | --- | --- |
| eUprava | https://euprava.gov.rs/ | Core e-government | Required initial service; public landing page for Serbian e-government services. |
| eID.gov.rs | https://eid.gov.rs/ | Identity | Required initial service; public identity portal landing page. |
| Welcome to Serbia | https://welcometoserbia.gov.rs/ | Immigration | Required initial service; public immigration portal landing page. |
| ePorezi | https://eporezi.purs.gov.rs/ | Taxes | Required initial service; public tax portal entry point. Authenticated tax account pages are excluded. |
| APR | https://www.apr.gov.rs/ | Business | Required initial service; public business registry landing page. |
| LPA | https://lpa.gov.rs/jisportal/homepage | Taxes | Required initial service; public local tax administration homepage. |
| eKatastar | https://katastar.rgz.gov.rs/eKatastarPublic/ | Property | Required initial service; public real-estate cadastre entry point. |
| data.gov.rs | https://data.gov.rs/ | Open data | Required initial service; public open-data portal landing page. |

No additional SRB.GUIDE candidates were added for the initial MVP. The required services already cover the target groups, and adding marginal or duplicate services would make the first release noisier without improving the core status page.

## Rejected Candidates

| Candidate | Source | Reason |
| --- | --- | --- |
| registracija.eid.gov.rs foreigner registration form | SRB.GUIDE eID registration guide | Rejected because it is a registration flow with document upload, form submission, and CAPTCHA-sensitive behavior. |
| ePorezi authenticated pages such as tax messages and device pairing | SRB.GUIDE e-government guide | Rejected because they require login, certificates, session state, or private tax data. |
| APR online application flows | SRB.GUIDE business guides | Rejected because application submission is an authenticated workflow, not a public availability check. |
| efaktura.mfin.gov.rs | SRB.GUIDE e-government guide | Rejected for the MVP because it is an authenticated business invoicing system and would duplicate the initial business/tax scope. |
| SRB.GUIDE calculators, stats pages, and izjava.rs tools | SRB.GUIDE service links | Rejected because they are community or private helper tools, not Serbian government service availability targets. |
| PIO and health-card related pages | SRB.GUIDE personal guides | Rejected for the initial MVP to keep the service list focused on the required groups; they can be reconsidered in a later expansion. |
| Bank, exchange-office, transport, housing, and private commercial links | SRB.GUIDE navigation | Rejected because they are not Serbian government or public e-government services. |
