# Beispiele

## Solution Manifest

```json
{
  "solution_name": "member-onboarding",
  "solution_version": "1.4.0",
  "business_owner": "operations",
  "technical_owner": "platform-team",
  "data_classification": "internal",
  "connectors": ["Microsoft 365", "Dataverse"],
  "dlp_reviewed": true,
  "environment_strategy": ["development", "test", "production"],
  "source_control_path": "src/member-onboarding"
}
```

## Power Fx Eingabevalidierung

```text
If(
    IsBlank(Trim(txtEmail.Text)) || !IsMatch(txtEmail.Text, Match.Email),
    Notify("Bitte eine gültige E-Mail-Adresse eingeben.", NotificationType.Error),
    SubmitForm(frmMember)
)
```

Business-kritische Regeln zusätzlich außerhalb der UI dokumentieren und serverseitig beziehungsweise in der Datenquelle absichern, wenn Umgehung der App möglich ist.
