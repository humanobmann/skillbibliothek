---
name: framing-analysis
description: Analyze political framing, populist or radical-right communication, counternarratives, propaganda-like techniques, crisis rhetoric, identity construction, blame attribution, nostalgia, media amplification, and rebuttal strategy. Use when ChatGPT must dissect a political message, speech, post, slogan, campaign frame, media clip, or narrative using framing theory and then perform Red Team, Blue Team, and Purple Team analysis. Also use for neutral counterframing, prebunking, fact-based rebuttal architecture, and response design that informs rather than tells people how to vote. For current political actors, laws, speeches, statistics, elections, party positions, or recent events, verify claims with current web or authoritative primary sources before drawing conclusions.
---

# Framing Analysis

## Core purpose

Deconstruct political communication into its functional parts, test competing explanations, separate evidence from interpretation, and build a fact-grounded alternative frame without reproducing unsupported claims or giving voting recommendations.

Read the following references when relevant:

- `references/framing-framework.md` for the analytical model and frame grammar.
- `references/red-blue-purple.md` for adversarial review and counterframing workflow.
- `references/evidence-rules.md` for source quality, uncertainty, and political safety constraints.

## Workflow

1. Identify the exact object of analysis.
   - Preserve the original wording where short enough.
   - For long material, extract only the decisive claims, recurring terms, images, roles, and causal links.

2. Establish context.
   - Identify speaker, audience, date, platform, political role, government or opposition status, and triggering event.
   - For current political material, browse and verify relevant facts before substantive claims.
   - Distinguish primary-source self-description from independent evidence.

3. Build a frame map.
   Analyze at minimum:
   - problem definition
   - causal attribution
   - moral evaluation
   - proposed remedy
   - in-group
   - out-group or opponent
   - victim
   - responsible actor
   - claimed loss
   - promised restoration
   - emotional register
   - temporal structure: past, decline, crisis, restoration
   - linguistic compression: slogans, labels, metaphors, pronouns, absolutes, repetition
   - platform affordances and likely amplification mechanisms

4. Classify without overclaiming.
   - Do not equate emotionality, simplicity, provocation, or elite criticism alone with populism.
   - Distinguish populism, nativism, authoritarian ordering, ordinary opposition rhetoric, conspiracy claims, institutional delegitimization, and dehumanization.
   - Attribute contested labels to sources when applicable.

5. Run Red Team.
   - Generate the strongest plausible alternative explanations.
   - Ask whether the same pattern occurs outside the political family under analysis.
   - Test whether issue preferences, material conditions, institutional context, platform mechanics, incumbency, or ordinary campaigning explain the observation better.
   - Identify causal claims that are unsupported, overstated, or merely correlational.

6. Run Blue Team.
   - Retain only claims that survive Red Team scrutiny.
   - Rank evidence internally as A, B, C, or D using `references/evidence-rules.md`.
   - State what is robust, what is conditional, and what remains unknown.

7. Run Purple Team.
   - Integrate the strongest surviving analytical findings into a response strategy.
   - Prefer corrective explanation, prebunking, contextualization, inoculation against manipulation patterns, and evidence-backed alternative framing.
   - Do not recommend a candidate, party, vote, or electoral choice.
   - Do not infer which audience should be psychologically targeted.
   - Do not generate psychographic persuasion plans or manipulative microtargeting.

8. Produce counterframing.
   Construct an alternative interpretation in this order:
   - establish the verified fact or shared reality first
   - name the omitted context or faulty causal leap
   - explain the frame mechanism briefly
   - replace the causal model with the strongest evidence-supported model
   - formulate a concise alternative frame centered on verifiable consequences, institutions, rights, responsibility, or material outcomes
   - when useful, add a prebunking line describing the recurring manipulation pattern before it appears again

9. Stress-test the counterframe.
   Ask:
   - Does it repeat the opponent's slogan unnecessarily?
   - Does it depend on a fact that could be challenged?
   - Does it accidentally validate the opponent's causal model?
   - Does it moralize beyond the evidence?
   - Is it understandable without specialist terminology?
   - Does it remain accurate if the audience disagrees politically?

## Default output

Use this structure unless the user requests another format:

### 1. Kurzbefund
Three to six sentences identifying the central communicative architecture.

### 2. Frame Map
A compact table with:
`Element | Beobachtung | Funktion | Evidenzgrad`

### 3. Red Team
List the strongest counter-explanations and weaknesses in the initial interpretation.

### 4. Blue Team
State what remains empirically defensible after the challenge.

### 5. Purple Team Gegenstrategie
Provide a neutral response architecture with:
`Faktenanker | Dekonstruktion | Alternativer Frame | Prebunking | Risiko`

### 6. Gegenframing Formulierungen
If requested, provide concise formulations that correct or contextualize claims without voting advice, deceptive rhetoric, or unsupported accusations.

### 7. Quellen und Unsicherheiten
Cite current political facts inline. Explicitly mark gaps, disputed claims, and evidence limitations.

## Fast mode

For a single slogan, quote, post, or short clip, compress the analysis to:

1. Frame
2. Mechanism
3. Red Team objection
4. Robust finding
5. Fact-grounded alternative frame

## Comparative mode

When comparing multiple actors or parties:

- Use identical coding dimensions for all actors.
- Separate shared populist features from actor-specific style.
- Control conceptually for government versus opposition, political system, platform, national context, and speaker personality.
- Never produce an evaluative political ranking or declare a political actor the best, worst, strongest, weakest, most dangerous, or most electable.

## Language rules

- Use precise language rather than moral panic.
- Separate facts, interpretation, and hypothesis.
- Avoid treating correlation as causation.
- Avoid claiming that audiences are manipulated simply because a message is emotional or repetitive.
- Prefer terms such as `frame`, `causal attribution`, `ingroup`, `outgroup`, `restoration narrative`, `delegitimization`, `prebunking`, and `agenda setting` only where they clarify rather than obscure.
- For German output, write naturally and accessibly, then add technical terminology in parentheses only when useful.
