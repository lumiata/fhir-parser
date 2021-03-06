//
//  FHIRContainedResource.swift
//  SMART-on-FHIR
//
//  Created by Pascal Pfiffner on 7/18/14.
//  2014, SMART Platforms.
//

import Foundation


/**
 *  Contained resources are stored to instances of this class until they are resolved.
 *  The id of contained resources will be referenced from their parents as URL fragment, meaning "med1" will be
 *  referenced as "#med1". FHIRReference handles id normalization.
 *
 *  http://hl7.org/implement/standards/fhir/references.html#contained
 */
public class FHIRContainedResource
{
	/** The id of the resource. */
	public var id: String?
	
	/** The type of the resource. */
	public var type: String?
	
	/** The complete JSON dictionary. */
	var json: NSDictionary?
	
	public init(id: String?, type: String?, json: NSDictionary?) {
		self.id = id
		self.type = type
		self.json = json
	}
	
	public convenience init(json: NSDictionary) {
		let id = json["id"] as? String
		let type = json["resourceType"] as? String
		self.init(id: id, type: type, json: json)
	}
}

