========================
What MANTIS is and isn't
========================

MANTIS 

* *isn't* a finished tool or even project: we like to think that it provides
  a solid basis on which cyber-threat intelligence management can be built up upon,
  but if you expect something that out of the box covers all aspects
  of cyber-threat intelligence management, MANTIS isn't for you.

* (currently) *isn't* a tool fit for importing *huge* datasets. It can
  import fairly large XML documents such as the `MITRE STIX conversion
  of the APT-1 report`_, but this takes a while (expect 20-30 minutes
  or so.) So do not expect to be able to throw, e.g., dozens and
  dozens of MAEC files with sizes of several 100MBs into the system:
  the generic importer is not fit for such sizes.

  This situation may change at some point of time with more stream-lined
  importers, but MANTIS is really not intended to deal with very big data
  the way log management solutions such as Splunk et al. are.

What MANTIS is:

* MANTIS provides an example implementation of a framework for
  managing cyber threat intelligence expressed in standards such as
  STIX, CybOX, IODEF, etc. The aims of providing such an example
  implementation are:
  
  * To aide discussions about emerging standards such as STIX, CybOX et al.
    with respect to questions regarding tooling: how would a certain
    aspect be implemented, how do changes affect an implementation? Such
    discussions become much easier and have a better basis if they can
    be lead in the context of example tooling that is known to
    the community.

  * To lower the entrance barrier for organizations and teams (esp.
    CERT teams) in using emerging standards for cyber-threat
    intelligence management and exchange.

  * To provide a platform on the basis of which research and
    community-driven development in the area of cyber-threat
    intelligence management can occur.
    
* Even though MANTIS is in no way a complete system, it already does
  cover a first use case: MANTIS provides an information repository
  into which cyber threat intelligence received in STIX/CybOX, OpenIOC
  and IODEF can be imported in a meaningful way that allows browsing,
  filtering and searching for information. Thus, MANTIS can be used as
  information base for keeping all the information you receive and
  information you generate yourself that is expressed in one of the
  currently supported standards.  Because the importer is highly
  configurable, importers for other structured data should not be too
  difficult to write (and will hopefully be shared with the
  community ...).


.. _MITRE STIX conversion of the APT-1 report: http://stix.mitre.org/downloads/APT1-STIX.zip
