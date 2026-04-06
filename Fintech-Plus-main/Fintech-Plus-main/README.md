# Fintech Plus - Ecosistema de Inspección Continua

## 📌 Descripción
Proyecto base que implementa:
- Pruebas unitarias con pytest
- Cobertura de código ≥ 80%
- Pipeline CI con GitHub Actions
- Análisis estático con SonarCloud

## 🚀 Instalación

```bash
pip install -r requirements.txt
```

## 🧪 Ejecutar pruebas

```bash
pytest --cov=app --cov-report=xml
```

## ☁️ Configuración SonarCloud

1. Crear cuenta en SonarCloud
2. Vincular repositorio
3. Crear token
4. Agregar en GitHub:
   Settings > Secrets > Actions
   Nombre: SONAR_TOKEN

## ✅ Resultado esperado
- Cobertura ≥ 80%
- Pipeline en verde
- Quality Gate aprobado

## 🔗 Repositorio
(Aquí pegas tu URL de GitHub)