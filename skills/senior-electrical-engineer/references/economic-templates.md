# Economic Analysis Templates for Electrical Projects

## Template 1: Total Cost of Ownership (TCO) Framework

### Capital Expenditure (CapEx)
| Item | Cost (USD) | Notes |
|---|---|---|
| Equipment (materials) | $ | Transformers, switchgear, cable, etc. |
| Engineering & Design | $ | 5–10% of equipment cost |
| Installation (labor) | $ | US: $80–150/hr; Colombia: $15–30/hr |
| Commissioning & Testing | $ | 2–5% of total CapEx |
| Permitting & Inspection | $ | Varies by jurisdiction |
| Project Management | $ | 5–8% of total CapEx |
| Contingency | $ | 10–15% of CapEx |
| **Total CapEx** | **$** | |

### Operating Expenditure (OpEx — Annual)
| Item | Cost/Year (USD) | Notes |
|---|---|---|
| Preventive Maintenance | $ | |
| Corrective Maintenance | $ | Estimated from MTTR/MTBF |
| Insurance | $ | |
| Monitoring & Software | $ | |
| Utility Charges | $ | Demand charges, connection fees |
| Personnel (if applicable) | $ | |
| **Total Annual OpEx** | **$** | |

### TCO Calculation
```
TCO (N years) = CapEx + Σ(Annual OpEx × escalation factor) - Σ(Salvage Value)
Net Present Cost = TCO discounted at WACC or cost of capital
```

---

## Template 2: ROI for Energy Efficiency or Generation Projects

### Annual Savings / Revenue
| Source | Annual Value (USD) |
|---|---|
| Energy savings (kWh reduction × tariff) | $ |
| Demand charge reduction | $ |
| PV generation revenue / bill offset | $ |
| Avoided maintenance costs | $ |
| Reduced downtime costs | $ |
| Incentives / tax benefits (annualized) | $ |
| **Total Annual Benefit** | **$** |

### Key Financial Metrics
```
Simple Payback Period = Total CapEx / Annual Net Benefit (years)

ROI (%) = (Total Benefits - Total Costs) / Total Costs × 100

NPV = Σ [Cash Flow_t / (1 + r)^t] - Initial Investment
  where r = discount rate, t = year

IRR = Discount rate at which NPV = 0

Levelized Cost of Energy (LCOE) for generation projects:
LCOE = (Total Lifecycle Cost) / (Total Lifetime Energy Production in kWh)
```

---

## Template 3: Cost-Benefit Comparison Matrix

Use when presenting alternatives to decision-makers:

| Criteria | Option A (Base) | Option B (Premium) | Option C (Digital) |
|---|---|---|---|
| CapEx | $ | $ | $ |
| Annual OpEx | $ | $ | $ |
| 10-Year TCO | $ | $ | $ |
| Simple Payback | yrs | yrs | yrs |
| NPV (10-yr) | $ | $ | $ |
| Risk Level | High/Med/Low | | |
| Compliance Risk | H/M/L | | |
| Scalability | H/M/L | | |
| **Recommendation** | | ✓ | |

---

## Template 4: Business Case One-Pager Structure

**Project Title:**
**Prepared By:** [Senior Electrical Engineer]
**Date:** [Date]
**Prepared For:** [C-Suite / Board]

### Problem Statement (2–3 sentences)
What is the current situation? What risk or cost is it creating?

### Proposed Solution (2–3 sentences)
What is recommended? What technology/approach?

### Financial Summary
| Metric | Value |
|---|---|
| Total Investment | $ |
| Annual Savings | $ |
| Simple Payback | X years |
| 10-Year NPV | $ |
| IRR | X% |

### Risk Summary
| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Regulatory non-compliance | Med | High | Engage certified inspector |
| Equipment lead time | Low | Med | Order 16+ weeks ahead |
| Cost overrun | Low | Med | 15% contingency included |

### Recommendation
One clear, action-oriented sentence. What should leadership approve, by when, and why.

---

## Quick Reference: Typical Project Cost Ranges

### US Market (2024–2025)
| Project Type | Typical Range |
|---|---|
| Commercial PV (100–500kW) | $1.20–$1.80/Wp installed |
| Industrial PV + Storage | $1.50–$2.50/Wp |
| Generator installation (200–1000kW) | $300–$600/kW |
| Substation upgrade (15kV) | $500K–$2M |
| SCADA/Automation upgrade | $150K–$800K |
| Arc flash study + remediation | $30K–$150K |

### Colombia Market (2024–2025)
| Project Type | Typical Range |
|---|---|
| Commercial PV (100–500kW) | USD $700–$1,100/kWp installed |
| Industrial PV + Storage | USD $1,000–$1,800/kWp |
| Generator installation (200kVA) | USD $80K–$200K |
| Substation upgrade (11.4kV) | USD $150K–$600K |
| SCADA/Automation upgrade | USD $50K–$300K |

*Note: Colombia costs are significantly lower due to labor rates but can increase due to import duties on equipment (unless Ley 1715 exemptions apply)*
