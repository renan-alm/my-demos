---
name: modern-java-app-debugger
description: Guide for debugging failing Java applications during modernization. Use this when asked to debug build failures, dependency conflicts, runtime errors, or test failures in modernized Java projects migrating to Spring Boot, newer Java versions, or modern frameworks.
---
# Modern Java Application Debugger

To debug Java applications undergoing modernization (e.g., migrating from legacy systems to Spring Boot and Angular), follow this structured process:

## Debugging Process

1. **Check dependency conflicts first**
   - Use `run_in_terminal` to execute `mvn dependency:tree` (Maven) or `gradle dependencies --scan` (Gradle)
   - Look for version conflicts between legacy and updated libraries
   - Check for duplicate dependencies with different versions
   - Pay special attention to Spring Boot BOM (Bill of Materials) overrides

2. **Verify Java version compatibility**
   - Check `pom.xml` or `build.gradle` for `java.version`, `maven.compiler.source`, or `sourceCompatibility`
   - Ensure the runtime Java version matches or exceeds the compile target
   - Use `run_in_terminal` to verify with `java -version` and `mvn -version` or `gradle -version`
   - Watch for features that require specific Java versions (e.g., records require Java 16+)

3. **Enable verbose build logging**
   - For Maven: Add `-X` flag (e.g., `mvn clean install -X`)
   - For Gradle: Add `--debug` or `--stacktrace` flag
   - Use verbose output to identify the exact point of failure

4. **Check for deprecated API usage**
   - Look for calls to removed or deprecated Java APIs (common in Java 8 → 11+ migrations)
   - Search for removed packages: `javax.*` → `jakarta.*` (Java EE → Jakarta EE)
   - Check for removed JDK internals (e.g., `sun.*` packages)

5. **Review build tool migration issues**
   - Verify plugin versions are compatible with the new Java version
   - Check Maven/Gradle wrapper versions (`mvnw` or `gradlew`)
   - Ensure parent POM or dependency management sections are correctly configured

6. **Inspect module system conflicts**
   - Check for reflection-based code that may break with Java 9+ module system
   - Look for `IllegalAccessError` or `InaccessibleObjectException`
   - Add necessary `--add-opens` or `--add-exports` JVM flags if required

7. **Verify environment configuration**
   - Check that `JAVA_HOME` points to the correct JDK version
   - Verify system properties and environment variables are set correctly
   - Review application.properties or application.yml for configuration issues

8. **Analyze runtime errors**
   - Read stack traces carefully for `ClassNotFoundException`, `NoSuchMethodError`, or `NoClassDefFoundError`
   - These often indicate dependency version mismatches or missing transitive dependencies
   - Use dependency analysis tools to find the source

## Common Migration Issues

- **Spring Boot 2 → 3**: Requires Java 17+, Jakarta EE namespace changes, removed properties
- **Java 8 → 11+**: Removed modules (JAXB, JAX-WS), different garbage collectors
- **Hibernate 5 → 6**: Breaking API changes, different query behaviors
- **JUnit 4 → 5**: Different annotations (`@Test`, `@Before`, `@After`)
