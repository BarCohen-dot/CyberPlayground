import plotly.graph_objects as go
import pandas as pd

# יצירת נתונים מעודכנים
data = {
    'Task': [
        'Define project scope and objectives', 'Assemble Agile team and assign roles',
        'Identify stakeholders and requirements', 'Establish constraints and risks',
        'Create high-level product backlog', 'Define sprints and duration',
        'Develop roadmap and resource allocation', 'Conduct initial sprint planning',
        'Develop core functionalities', 'Implement feedback and refine functionalities',
        'Add advanced features and enhance UX', 'Comprehensive testing and finalization',
        'Sprint reviews and retrospectives', 'Unit, integration, and UAT testing',
        'Validate success criteria', 'Deliver final product',
        'Gather and document feedback', 'Conduct project retrospective',
        'Provide training/documentation for users', 'Monitor live environment',
        'Identify lessons learned'
    ],
    'Duration': [
        1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1
    ],
    'Phase': [
        'Initiation Phase', 'Initiation Phase', 'Initiation Phase', 'Initiation Phase',
        'Planning Phase', 'Planning Phase', 'Planning Phase', 'Planning Phase',
        'Sprint 1', 'Sprint 2', 'Sprint 3', 'Sprint 4',
        'Quality Assurance', 'Quality Assurance', 'Quality Assurance',
        'Project Delivery', 'Project Delivery', 'Project Delivery',
        'Post-Implementation', 'Post-Implementation', 'Post-Implementation'
    ]
}

# יצירת DataFrame
df = pd.DataFrame(data)

# סינון נתונים להסרת ספרינטים 1-4
df = df[~df['Phase'].isin(['Sprint 1', 'Sprint 2', 'Sprint 3', 'Sprint 4'])]

# חישוב התחלה וסיום לכל משימה לפי גרף מפל
start_dates = []
current_start = pd.Timestamp('2025-01-01')

for duration in df['Duration']:
    start_dates.append(current_start)
    current_start += pd.Timedelta(days=duration)

df['Start'] = start_dates
df['Finish'] = df['Start'] + pd.to_timedelta(df['Duration'], unit='D')

# יצירת גרף גאנט
fig = go.Figure()

# הגדרת צבעים לאבני הדרך
phase_colors = {
    'Initiation Phase': 'rgb(0, 123, 255)',  # כחול חזק
    'Planning Phase': 'rgb(0, 200, 83)',  # ירוק עז
    'Quality Assurance': 'rgb(255, 69, 0)',  # אדום בהיר
    'Project Delivery': 'rgb(255, 165, 0)',  # כתום בוהק
    'Post-Implementation': 'rgb(186, 85, 211)'  # סגול עז
}

# הוספת משימות לגראף
for i, row in df.iterrows():
    fig.add_trace(go.Bar(
        y=[row['Task']],
        x=[(row['Finish'] - row['Start']).days],
        base=(row['Start'] - df['Start'].min()).days,
        orientation='h',
        name=row['Phase'],
        marker=dict(color=phase_colors[row['Phase']]),
        showlegend=(row['Task'] == df[df['Phase'] == row['Phase']]['Task'].iloc[0])  # פעם אחת לכל שלב
    ))

# עיצוב הגרף
fig.update_layout(
    title="Project Timeline - Waterfall Gantt Chart",
    xaxis=dict(
        title="Days",
        tickmode='array',
        tickvals=list(range(0, (df['Finish'].max() - df['Start'].min()).days + 1)),
        ticktext=pd.date_range(start=df['Start'].min(), end=df['Finish'].max(), freq='D').strftime('%d-%m')
    ),
    yaxis=dict(
        title="Tasks",
        categoryorder='array',
        categoryarray=df['Task'][::-1]  # סדר מהסוף להתחלה
    ),
    barmode='stack',
    xaxis_showgrid=True,
    yaxis_showgrid=True,
    template="plotly_dark",
    plot_bgcolor="rgba(0, 0, 0, 0)",
)

# הצגת הגרף
fig.show()
