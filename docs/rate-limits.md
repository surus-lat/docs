# Límites de frecuencia

Los límites de frecuencia son restricciones que controlan la cantidad de solicitudes que un usuario puede hacer a la API en un período de tiempo determinado. Estos límites ayudan a prevenir abusos del servicio y mantener un rendimiento óptimo para todos los usuarios.

Medimos los límites de frecuencia en "solicitudes por minuto" (RPM). De exceder este límite, las solicitudes adicionales serán rechazadas hasta que se restablezca el contador.

Actualmente, los límites de frecuencia son los siguientes:

| Tipo de solicitud       | Límite (RPM) |
|-------------------------|--------------|
| Texto                   | 7000         |
| Visión                  | TBD          |
| Audio - Transcripción   | TBD          |
| Audio - Texto a Voz     | TBD          |
| Embeddings              | TBD          |

## Solicitudes adicionales

En caso de que tu caso de uso requiera un mayor límite de frecuencia, no dudes en contactarnos a través de nuestro [Discord](https://discord.gg/sFeXDcAJ9K) o [email](mailto:contacto@surus.dev).
---