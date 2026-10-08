(globalThis.TURBOPACK||(globalThis.TURBOPACK=[])).push(["object"==typeof document?document.currentScript:void 0,131497,e=>{"use strict";let t=parseInt(e.i(190072).REVISION.replace(/\D+/g,""));e.s(["version",0,t])},107985,e=>{"use strict";var t=e.i(190072),n=e.i(408560),i=e.i(131497);class r extends t.ShaderMaterial{constructor(e){super({type:"LineMaterial",uniforms:t.UniformsUtils.clone(t.UniformsUtils.merge([n.UniformsLib.common,n.UniformsLib.fog,{worldUnits:{value:1},linewidth:{value:1},resolution:{value:new t.Vector2(1,1)},dashOffset:{value:0},dashScale:{value:1},dashSize:{value:1},gapSize:{value:1}}])),vertexShader:`
				#include <common>
				#include <fog_pars_vertex>
				#include <logdepthbuf_pars_vertex>
				#include <clipping_planes_pars_vertex>

				uniform float linewidth;
				uniform vec2 resolution;

				attribute vec3 instanceStart;
				attribute vec3 instanceEnd;

				#ifdef USE_COLOR
					#ifdef USE_LINE_COLOR_ALPHA
						varying vec4 vLineColor;
						attribute vec4 instanceColorStart;
						attribute vec4 instanceColorEnd;
					#else
						varying vec3 vLineColor;
						attribute vec3 instanceColorStart;
						attribute vec3 instanceColorEnd;
					#endif
				#endif

				#ifdef WORLD_UNITS

					varying vec4 worldPos;
					varying vec3 worldStart;
					varying vec3 worldEnd;

					#ifdef USE_DASH

						varying vec2 vUv;

					#endif

				#else

					varying vec2 vUv;

				#endif

				#ifdef USE_DASH

					uniform float dashScale;
					attribute float instanceDistanceStart;
					attribute float instanceDistanceEnd;
					varying float vLineDistance;

				#endif

				void trimSegment( const in vec4 start, inout vec4 end ) {

					// trim end segment so it terminates between the camera plane and the near plane

					// conservative estimate of the near plane
					float a = projectionMatrix[ 2 ][ 2 ]; // 3nd entry in 3th column
					float b = projectionMatrix[ 3 ][ 2 ]; // 3nd entry in 4th column
					float nearEstimate = - 0.5 * b / a;

					float alpha = ( nearEstimate - start.z ) / ( end.z - start.z );

					end.xyz = mix( start.xyz, end.xyz, alpha );

				}

				void main() {

					#ifdef USE_COLOR

						vLineColor = ( position.y < 0.5 ) ? instanceColorStart : instanceColorEnd;

					#endif

					#ifdef USE_DASH

						vLineDistance = ( position.y < 0.5 ) ? dashScale * instanceDistanceStart : dashScale * instanceDistanceEnd;
						vUv = uv;

					#endif

					float aspect = resolution.x / resolution.y;

					// camera space
					vec4 start = modelViewMatrix * vec4( instanceStart, 1.0 );
					vec4 end = modelViewMatrix * vec4( instanceEnd, 1.0 );

					#ifdef WORLD_UNITS

						worldStart = start.xyz;
						worldEnd = end.xyz;

					#else

						vUv = uv;

					#endif

					// special case for perspective projection, and segments that terminate either in, or behind, the camera plane
					// clearly the gpu firmware has a way of addressing this issue when projecting into ndc space
					// but we need to perform ndc-space calculations in the shader, so we must address this issue directly
					// perhaps there is a more elegant solution -- WestLangley

					bool perspective = ( projectionMatrix[ 2 ][ 3 ] == - 1.0 ); // 4th entry in the 3rd column

					if ( perspective ) {

						if ( start.z < 0.0 && end.z >= 0.0 ) {

							trimSegment( start, end );

						} else if ( end.z < 0.0 && start.z >= 0.0 ) {

							trimSegment( end, start );

						}

					}

					// clip space
					vec4 clipStart = projectionMatrix * start;
					vec4 clipEnd = projectionMatrix * end;

					// ndc space
					vec3 ndcStart = clipStart.xyz / clipStart.w;
					vec3 ndcEnd = clipEnd.xyz / clipEnd.w;

					// direction
					vec2 dir = ndcEnd.xy - ndcStart.xy;

					// account for clip-space aspect ratio
					dir.x *= aspect;
					dir = normalize( dir );

					#ifdef WORLD_UNITS

						// get the offset direction as perpendicular to the view vector
						vec3 worldDir = normalize( end.xyz - start.xyz );
						vec3 offset;
						if ( position.y < 0.5 ) {

							offset = normalize( cross( start.xyz, worldDir ) );

						} else {

							offset = normalize( cross( end.xyz, worldDir ) );

						}

						// sign flip
						if ( position.x < 0.0 ) offset *= - 1.0;

						float forwardOffset = dot( worldDir, vec3( 0.0, 0.0, 1.0 ) );

						// don't extend the line if we're rendering dashes because we
						// won't be rendering the endcaps
						#ifndef USE_DASH

							// extend the line bounds to encompass  endcaps
							start.xyz += - worldDir * linewidth * 0.5;
							end.xyz += worldDir * linewidth * 0.5;

							// shift the position of the quad so it hugs the forward edge of the line
							offset.xy -= dir * forwardOffset;
							offset.z += 0.5;

						#endif

						// endcaps
						if ( position.y > 1.0 || position.y < 0.0 ) {

							offset.xy += dir * 2.0 * forwardOffset;

						}

						// adjust for linewidth
						offset *= linewidth * 0.5;

						// set the world position
						worldPos = ( position.y < 0.5 ) ? start : end;
						worldPos.xyz += offset;

						// project the worldpos
						vec4 clip = projectionMatrix * worldPos;

						// shift the depth of the projected points so the line
						// segments overlap neatly
						vec3 clipPose = ( position.y < 0.5 ) ? ndcStart : ndcEnd;
						clip.z = clipPose.z * clip.w;

					#else

						vec2 offset = vec2( dir.y, - dir.x );
						// undo aspect ratio adjustment
						dir.x /= aspect;
						offset.x /= aspect;

						// sign flip
						if ( position.x < 0.0 ) offset *= - 1.0;

						// endcaps
						if ( position.y < 0.0 ) {

							offset += - dir;

						} else if ( position.y > 1.0 ) {

							offset += dir;

						}

						// adjust for linewidth
						offset *= linewidth;

						// adjust for clip-space to screen-space conversion // maybe resolution should be based on viewport ...
						offset /= resolution.y;

						// select end
						vec4 clip = ( position.y < 0.5 ) ? clipStart : clipEnd;

						// back to clip space
						offset *= clip.w;

						clip.xy += offset;

					#endif

					gl_Position = clip;

					vec4 mvPosition = ( position.y < 0.5 ) ? start : end; // this is an approximation

					#include <logdepthbuf_vertex>
					#include <clipping_planes_vertex>
					#include <fog_vertex>

				}
			`,fragmentShader:`
				uniform vec3 diffuse;
				uniform float opacity;
				uniform float linewidth;

				#ifdef USE_DASH

					uniform float dashOffset;
					uniform float dashSize;
					uniform float gapSize;

				#endif

				varying float vLineDistance;

				#ifdef WORLD_UNITS

					varying vec4 worldPos;
					varying vec3 worldStart;
					varying vec3 worldEnd;

					#ifdef USE_DASH

						varying vec2 vUv;

					#endif

				#else

					varying vec2 vUv;

				#endif

				#include <common>
				#include <fog_pars_fragment>
				#include <logdepthbuf_pars_fragment>
				#include <clipping_planes_pars_fragment>

				#ifdef USE_COLOR
					#ifdef USE_LINE_COLOR_ALPHA
						varying vec4 vLineColor;
					#else
						varying vec3 vLineColor;
					#endif
				#endif

				vec2 closestLineToLine(vec3 p1, vec3 p2, vec3 p3, vec3 p4) {

					float mua;
					float mub;

					vec3 p13 = p1 - p3;
					vec3 p43 = p4 - p3;

					vec3 p21 = p2 - p1;

					float d1343 = dot( p13, p43 );
					float d4321 = dot( p43, p21 );
					float d1321 = dot( p13, p21 );
					float d4343 = dot( p43, p43 );
					float d2121 = dot( p21, p21 );

					float denom = d2121 * d4343 - d4321 * d4321;

					float numer = d1343 * d4321 - d1321 * d4343;

					mua = numer / denom;
					mua = clamp( mua, 0.0, 1.0 );
					mub = ( d1343 + d4321 * ( mua ) ) / d4343;
					mub = clamp( mub, 0.0, 1.0 );

					return vec2( mua, mub );

				}

				void main() {

					#include <clipping_planes_fragment>

					#ifdef USE_DASH

						if ( vUv.y < - 1.0 || vUv.y > 1.0 ) discard; // discard endcaps

						if ( mod( vLineDistance + dashOffset, dashSize + gapSize ) > dashSize ) discard; // todo - FIX

					#endif

					float alpha = opacity;

					#ifdef WORLD_UNITS

						// Find the closest points on the view ray and the line segment
						vec3 rayEnd = normalize( worldPos.xyz ) * 1e5;
						vec3 lineDir = worldEnd - worldStart;
						vec2 params = closestLineToLine( worldStart, worldEnd, vec3( 0.0, 0.0, 0.0 ), rayEnd );

						vec3 p1 = worldStart + lineDir * params.x;
						vec3 p2 = rayEnd * params.y;
						vec3 delta = p1 - p2;
						float len = length( delta );
						float norm = len / linewidth;

						#ifndef USE_DASH

							#ifdef USE_ALPHA_TO_COVERAGE

								float dnorm = fwidth( norm );
								alpha = 1.0 - smoothstep( 0.5 - dnorm, 0.5 + dnorm, norm );

							#else

								if ( norm > 0.5 ) {

									discard;

								}

							#endif

						#endif

					#else

						#ifdef USE_ALPHA_TO_COVERAGE

							// artifacts appear on some hardware if a derivative is taken within a conditional
							float a = vUv.x;
							float b = ( vUv.y > 0.0 ) ? vUv.y - 1.0 : vUv.y + 1.0;
							float len2 = a * a + b * b;
							float dlen = fwidth( len2 );

							if ( abs( vUv.y ) > 1.0 ) {

								alpha = 1.0 - smoothstep( 1.0 - dlen, 1.0 + dlen, len2 );

							}

						#else

							if ( abs( vUv.y ) > 1.0 ) {

								float a = vUv.x;
								float b = ( vUv.y > 0.0 ) ? vUv.y - 1.0 : vUv.y + 1.0;
								float len2 = a * a + b * b;

								if ( len2 > 1.0 ) discard;

							}

						#endif

					#endif

					vec4 diffuseColor = vec4( diffuse, alpha );
					#ifdef USE_COLOR
						#ifdef USE_LINE_COLOR_ALPHA
							diffuseColor *= vLineColor;
						#else
							diffuseColor.rgb *= vLineColor;
						#endif
					#endif

					#include <logdepthbuf_fragment>

					gl_FragColor = diffuseColor;

					#include <tonemapping_fragment>
					#include <${i.version>=154?"colorspace_fragment":"encodings_fragment"}>
					#include <fog_fragment>
					#include <premultiplied_alpha_fragment>

				}
			`,clipping:!0}),this.isLineMaterial=!0,this.onBeforeCompile=function(){this.transparent?this.defines.USE_LINE_COLOR_ALPHA="1":delete this.defines.USE_LINE_COLOR_ALPHA},Object.defineProperties(this,{color:{enumerable:!0,get:function(){return this.uniforms.diffuse.value},set:function(e){this.uniforms.diffuse.value=e}},worldUnits:{enumerable:!0,get:function(){return"WORLD_UNITS"in this.defines},set:function(e){!0===e?this.defines.WORLD_UNITS="":delete this.defines.WORLD_UNITS}},linewidth:{enumerable:!0,get:function(){return this.uniforms.linewidth.value},set:function(e){this.uniforms.linewidth.value=e}},dashed:{enumerable:!0,get:function(){return"USE_DASH"in this.defines},set(e){!!e!="USE_DASH"in this.defines&&(this.needsUpdate=!0),!0===e?this.defines.USE_DASH="":delete this.defines.USE_DASH}},dashScale:{enumerable:!0,get:function(){return this.uniforms.dashScale.value},set:function(e){this.uniforms.dashScale.value=e}},dashSize:{enumerable:!0,get:function(){return this.uniforms.dashSize.value},set:function(e){this.uniforms.dashSize.value=e}},dashOffset:{enumerable:!0,get:function(){return this.uniforms.dashOffset.value},set:function(e){this.uniforms.dashOffset.value=e}},gapSize:{enumerable:!0,get:function(){return this.uniforms.gapSize.value},set:function(e){this.uniforms.gapSize.value=e}},opacity:{enumerable:!0,get:function(){return this.uniforms.opacity.value},set:function(e){this.uniforms.opacity.value=e}},resolution:{enumerable:!0,get:function(){return this.uniforms.resolution.value},set:function(e){this.uniforms.resolution.value.copy(e)}},alphaToCoverage:{enumerable:!0,get:function(){return"USE_ALPHA_TO_COVERAGE"in this.defines},set:function(e){!!e!="USE_ALPHA_TO_COVERAGE"in this.defines&&(this.needsUpdate=!0),!0===e?(this.defines.USE_ALPHA_TO_COVERAGE="",this.extensions.derivatives=!0):(delete this.defines.USE_ALPHA_TO_COVERAGE,this.extensions.derivatives=!1)}}}),this.setValues(e)}}e.s(["LineMaterial",0,r])},547736,e=>{"use strict";let t,n;var i=e.i(190072),r=e.i(132533),o=e.i(107985);let s=e.i(131497).version>=125?"uv1":"uv2",a=new i.Vector4,u=new i.Vector3,l=new i.Vector3,c=new i.Vector4,d=new i.Vector4,f=new i.Vector4,p=new i.Vector3,m=new i.Matrix4,h=new i.Line3,v=new i.Vector3,y=new i.Box3,S=new i.Sphere,g=new i.Vector4;function b(e,t,i){return g.set(0,0,-t,1).applyMatrix4(e.projectionMatrix),g.multiplyScalar(1/g.w),g.x=n/i.width,g.y=n/i.height,g.applyMatrix4(e.projectionMatrixInverse),g.multiplyScalar(1/g.w),Math.abs(Math.max(g.x,g.y))}class x extends i.Mesh{constructor(e=new r.LineSegmentsGeometry,t=new o.LineMaterial({color:0xffffff*Math.random()})){super(e,t),this.isLineSegments2=!0,this.type="LineSegments2"}computeLineDistances(){let e=this.geometry,t=e.attributes.instanceStart,n=e.attributes.instanceEnd,r=new Float32Array(2*t.count);for(let e=0,i=0,o=t.count;e<o;e++,i+=2)u.fromBufferAttribute(t,e),l.fromBufferAttribute(n,e),r[i]=0===i?0:r[i-1],r[i+1]=r[i]+u.distanceTo(l);let o=new i.InstancedInterleavedBuffer(r,2,1);return e.setAttribute("instanceDistanceStart",new i.InterleavedBufferAttribute(o,1,0)),e.setAttribute("instanceDistanceEnd",new i.InterleavedBufferAttribute(o,1,1)),this}raycast(e,r){let o,a,u=this.material.worldUnits,l=e.camera;null!==l||u||console.error('LineSegments2: "Raycaster.camera" needs to be set in order to raycast against LineSegments2 while worldUnits is set to false.');let g=void 0!==e.params.Line2&&e.params.Line2.threshold||0;t=e.ray;let x=this.matrixWorld,w=this.geometry,E=this.material;if(n=E.linewidth+g,null===w.boundingSphere&&w.computeBoundingSphere(),S.copy(w.boundingSphere).applyMatrix4(x),u)o=.5*n;else{let e=Math.max(l.near,S.distanceToPoint(t.origin));o=b(l,e,E.resolution)}if(S.radius+=o,!1!==t.intersectsSphere(S)){if(null===w.boundingBox&&w.computeBoundingBox(),y.copy(w.boundingBox).applyMatrix4(x),u)a=.5*n;else{let e=Math.max(l.near,y.distanceToPoint(t.origin));a=b(l,e,E.resolution)}y.expandByScalar(a),!1!==t.intersectsBox(y)&&(u?function(e,r){let o=e.matrixWorld,a=e.geometry,u=a.attributes.instanceStart,l=a.attributes.instanceEnd,c=Math.min(a.instanceCount,u.count);for(let a=0;a<c;a++){h.start.fromBufferAttribute(u,a),h.end.fromBufferAttribute(l,a),h.applyMatrix4(o);let c=new i.Vector3,d=new i.Vector3;t.distanceSqToSegment(h.start,h.end,d,c),d.distanceTo(c)<.5*n&&r.push({point:d,pointOnLine:c,distance:t.origin.distanceTo(d),object:e,face:null,faceIndex:a,uv:null,[s]:null})}}(this,r):function(e,r,o){let a=r.projectionMatrix,u=e.material.resolution,l=e.matrixWorld,y=e.geometry,S=y.attributes.instanceStart,g=y.attributes.instanceEnd,b=Math.min(y.instanceCount,S.count),x=-r.near;t.at(1,f),f.w=1,f.applyMatrix4(r.matrixWorldInverse),f.applyMatrix4(a),f.multiplyScalar(1/f.w),f.x*=u.x/2,f.y*=u.y/2,f.z=0,p.copy(f),m.multiplyMatrices(r.matrixWorldInverse,l);for(let r=0;r<b;r++){if(c.fromBufferAttribute(S,r),d.fromBufferAttribute(g,r),c.w=1,d.w=1,c.applyMatrix4(m),d.applyMatrix4(m),c.z>x&&d.z>x)continue;if(c.z>x){let e=c.z-d.z,t=(c.z-x)/e;c.lerp(d,t)}else if(d.z>x){let e=d.z-c.z,t=(d.z-x)/e;d.lerp(c,t)}c.applyMatrix4(a),d.applyMatrix4(a),c.multiplyScalar(1/c.w),d.multiplyScalar(1/d.w),c.x*=u.x/2,c.y*=u.y/2,d.x*=u.x/2,d.y*=u.y/2,h.start.copy(c),h.start.z=0,h.end.copy(d),h.end.z=0;let f=h.closestPointToPointParameter(p,!0);h.at(f,v);let y=i.MathUtils.lerp(c.z,d.z,f),b=y>=-1&&y<=1,w=p.distanceTo(v)<.5*n;if(b&&w){h.start.fromBufferAttribute(S,r),h.end.fromBufferAttribute(g,r),h.start.applyMatrix4(l),h.end.applyMatrix4(l);let n=new i.Vector3,a=new i.Vector3;t.distanceSqToSegment(h.start,h.end,a,n),o.push({point:a,pointOnLine:n,distance:t.origin.distanceTo(a),object:e,face:null,faceIndex:r,uv:null,[s]:null})}}}(this,l,r))}}onBeforeRender(e){let t=this.material.uniforms;t&&t.resolution&&(e.getViewport(a),this.material.uniforms.resolution.value.set(a.z,a.w))}}e.s(["LineSegments2",0,x],547736)},132533,e=>{"use strict";var t=e.i(190072);let n=new t.Box3,i=new t.Vector3;class r extends t.InstancedBufferGeometry{constructor(){super(),this.isLineSegmentsGeometry=!0,this.type="LineSegmentsGeometry",this.setIndex([0,2,1,2,3,1,2,4,3,4,5,3,4,6,5,6,7,5]),this.setAttribute("position",new t.Float32BufferAttribute([-1,2,0,1,2,0,-1,1,0,1,1,0,-1,0,0,1,0,0,-1,-1,0,1,-1,0],3)),this.setAttribute("uv",new t.Float32BufferAttribute([-1,2,1,2,-1,1,1,1,-1,-1,1,-1,-1,-2,1,-2],2))}applyMatrix4(e){let t=this.attributes.instanceStart,n=this.attributes.instanceEnd;return void 0!==t&&(t.applyMatrix4(e),n.applyMatrix4(e),t.needsUpdate=!0),null!==this.boundingBox&&this.computeBoundingBox(),null!==this.boundingSphere&&this.computeBoundingSphere(),this}setPositions(e){let n;e instanceof Float32Array?n=e:Array.isArray(e)&&(n=new Float32Array(e));let i=new t.InstancedInterleavedBuffer(n,6,1);return this.setAttribute("instanceStart",new t.InterleavedBufferAttribute(i,3,0)),this.setAttribute("instanceEnd",new t.InterleavedBufferAttribute(i,3,3)),this.computeBoundingBox(),this.computeBoundingSphere(),this}setColors(e,n=3){let i;e instanceof Float32Array?i=e:Array.isArray(e)&&(i=new Float32Array(e));let r=new t.InstancedInterleavedBuffer(i,2*n,1);return this.setAttribute("instanceColorStart",new t.InterleavedBufferAttribute(r,n,0)),this.setAttribute("instanceColorEnd",new t.InterleavedBufferAttribute(r,n,n)),this}fromWireframeGeometry(e){return this.setPositions(e.attributes.position.array),this}fromEdgesGeometry(e){return this.setPositions(e.attributes.position.array),this}fromMesh(e){return this.fromWireframeGeometry(new t.WireframeGeometry(e.geometry)),this}fromLineSegments(e){let t=e.geometry;return this.setPositions(t.attributes.position.array),this}computeBoundingBox(){null===this.boundingBox&&(this.boundingBox=new t.Box3);let e=this.attributes.instanceStart,i=this.attributes.instanceEnd;void 0!==e&&void 0!==i&&(this.boundingBox.setFromBufferAttribute(e),n.setFromBufferAttribute(i),this.boundingBox.union(n))}computeBoundingSphere(){null===this.boundingSphere&&(this.boundingSphere=new t.Sphere),null===this.boundingBox&&this.computeBoundingBox();let e=this.attributes.instanceStart,n=this.attributes.instanceEnd;if(void 0!==e&&void 0!==n){let t=this.boundingSphere.center;this.boundingBox.getCenter(t);let r=0;for(let o=0,s=e.count;o<s;o++)i.fromBufferAttribute(e,o),r=Math.max(r,t.distanceToSquared(i)),i.fromBufferAttribute(n,o),r=Math.max(r,t.distanceToSquared(i));this.boundingSphere.radius=Math.sqrt(r),isNaN(this.boundingSphere.radius)&&console.error("THREE.LineSegmentsGeometry.computeBoundingSphere(): Computed radius is NaN. The instanced position data is likely to have NaN values.",this)}}toJSON(){}applyMatrix(e){return console.warn("THREE.LineSegmentsGeometry: applyMatrix() has been renamed to applyMatrix4()."),this.applyMatrix4(e)}}e.s(["LineSegmentsGeometry",0,r])},755838,(e,t,n)=>{"use strict";var i=e.r(271645),r="function"==typeof Object.is?Object.is:function(e,t){return e===t&&(0!==e||1/e==1/t)||e!=e&&t!=t},o=i.useState,s=i.useEffect,a=i.useLayoutEffect,u=i.useDebugValue;function l(e){var t=e.getSnapshot;e=e.value;try{var n=t();return!r(e,n)}catch(e){return!0}}var c="u"<typeof window||void 0===window.document||void 0===window.document.createElement?function(e,t){return t()}:function(e,t){var n=t(),i=o({inst:{value:n,getSnapshot:t}}),r=i[0].inst,c=i[1];return a(function(){r.value=n,r.getSnapshot=t,l(r)&&c({inst:r})},[e,n,t]),s(function(){return l(r)&&c({inst:r}),e(function(){l(r)&&c({inst:r})})},[e]),u(n),n};n.useSyncExternalStore=void 0!==i.useSyncExternalStore?i.useSyncExternalStore:c},802239,(e,t,n)=>{"use strict";e.i(247167),t.exports=e.r(755838)},752822,(e,t,n)=>{"use strict";var i=e.r(271645),r=e.r(802239),o="function"==typeof Object.is?Object.is:function(e,t){return e===t&&(0!==e||1/e==1/t)||e!=e&&t!=t},s=r.useSyncExternalStore,a=i.useRef,u=i.useEffect,l=i.useMemo,c=i.useDebugValue;n.useSyncExternalStoreWithSelector=function(e,t,n,i,r){var d=a(null);if(null===d.current){var f={hasValue:!1,value:null};d.current=f}else f=d.current;var p=s(e,(d=l(function(){function e(e){if(!u){if(u=!0,s=e,e=i(e),void 0!==r&&f.hasValue){var t=f.value;if(r(t,e))return a=t}return a=e}if(t=a,o(s,e))return t;var n=i(e);return void 0!==r&&r(t,n)?(s=e,t):(s=e,a=n)}var s,a,u=!1,l=void 0===n?null:n;return[function(){return e(t())},null===l?void 0:function(){return e(l())}]},[t,n,i,r]))[0],d[1]);return u(function(){f.hasValue=!0,f.value=p},[p]),c(p),p}},430224,(e,t,n)=>{"use strict";e.i(247167),t.exports=e.r(752822)},931570,e=>{"use strict";var t=e.i(271645),n=e.i(94800),i=e.i(848546),r=e.i(190072);e.s(["default",0,function({destination:e,duration:o=.6,reducedMotion:s=!1,cancelRef:a}){let u=(0,i.useThree)(e=>e.camera),l=(0,i.useThree)(e=>e.controls),c=(0,t.useRef)(new r.Vector3),d=(0,t.useRef)(new r.Vector3),f=(0,t.useRef)(0),p=(0,t.useRef)(!1),m=(0,t.useRef)(null);(0,t.useEffect)(()=>{m.current=e},[e]);let h=(0,t.useCallback)(()=>{p.current=!1},[]);(0,t.useEffect)(()=>{if(a)return a.current=h,()=>{a.current===h&&(a.current=null)}},[h,a]);let v=e?`${e.position.x.toFixed(4)},${e.position.y.toFixed(4)},${e.position.z.toFixed(4)}|${e.target.x.toFixed(4)},${e.target.y.toFixed(4)},${e.target.z.toFixed(4)}`:"none";return(0,t.useEffect)(()=>{if(!e){p.current=!1;return}if(s){u.position.copy(e.position),l&&(l.target.copy(e.target),l.update()),p.current=!1;return}c.current.copy(u.position),d.current.copy(l?.target??u.position.clone()),f.current=0,p.current=!0},[v,s]),(0,n.useFrame)((e,t)=>{let n=m.current;if(!p.current||!n)return;f.current=Math.min(1,f.current+t/o);let i=f.current,r=i*i*(3-2*i);u.position.lerpVectors(c.current,n.position,r),l&&(l.target.lerpVectors(d.current,n.target,r),l.update()),i>=1&&(p.current=!1)}),null}])},482629,e=>{"use strict";var t=e.i(843476),n=e.i(807468);e.s(["default",0,function({value:e,placeholder:i,ariaLabel:r,options:o,disabled:s=!1,className:a="",testId:u,onSelect:l}){let c=(0,n.useCanvasToolbarEnabled)(),d=(0,n.useCanvasControlLabels)().canvasToolbar;return(0,t.jsx)(n.ResourceCanvasControls,{slot:"secondary",children:(0,t.jsxs)("select",{"aria-label":r,value:c?"":e,disabled:s,onChange:e=>l(e.target.value),"data-testid":u,className:`min-h-10 cursor-pointer rounded-lg border border-slate-300 bg-white px-2 text-xs font-bold text-slate-700 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-600 disabled:cursor-not-allowed disabled:opacity-45 ${a}`,children:[(0,t.jsx)("option",{value:"",disabled:!0,children:c?d.camera:i}),o.map(e=>(0,t.jsx)("option",{value:e.id,children:e.label},e.id))]})})}])},173596,e=>{"use strict";function t(e){return"number"==typeof e&&Number.isFinite(e)}function n(e,n,i){return t(e)&&e>=n&&e<=i}e.s(["isBoolean",0,function(e){return"boolean"==typeof e},"isFiniteNumber",0,t,"isNumberInRange",0,n,"isOnGrid",0,function(e,t){if(!n(e,t.minimum,t.maximum))return!1;let i=(e-t.minimum)/t.step;return 1e-6>Math.abs(i-Math.round(i))},"isOneOf",0,function(e,t){return t.includes(e)},"isRecord",0,function(e){return"object"==typeof e&&null!==e&&!Array.isArray(e)},"snapToGrid",0,function(e,t){if(!Number.isFinite(e))return null;let n=Math.round((Math.min(t.maximum,Math.max(t.minimum,e))-t.minimum)/t.step);return Number((t.minimum+n*t.step).toFixed(6))}])},719818,e=>{"use strict";var t=e.i(271645),n=e.i(422771);let i=/^(0|[1-9]\d*)\.\d+\.\d+$/;var r=e.i(246829);let o=[],s=()=>()=>void 0;function a(){return window.matchMedia("(prefers-reduced-motion: reduce)").matches}function u(e){let t=window.matchMedia("(prefers-reduced-motion: reduce)");return t.addEventListener("change",e),()=>t.removeEventListener("change",e)}e.s(["usePersistentResourceState",0,function(e,s,a=o){let u=(0,r.useResourceRuntime)(),[l,c]=(0,t.useState)(e.reset),[d,f]=(0,t.useState)(!1),p=(0,t.useRef)(!1),m=JSON.stringify(a),h=(0,t.useRef)(s);return(0,t.useEffect)(()=>{h.current=s},[s]),(0,t.useEffect)(()=>{let t=!1;return u.progress.load(u.identity).then(async n=>{for(let e of JSON.parse(m)){if(n||t)break;let r=function(e,t){let n="number"==typeof t?t:t?.stateSchemaVersion,r="number"==typeof t?e.resourceVersion:t?.resourceVersion;return!Number.isInteger(n)||n<1||n>e.stateSchemaVersion||"string"!=typeof r||!i.test(r)||n===e.stateSchemaVersion&&("number"==typeof t||!function(e,t){if(!i.test(e)||!i.test(t))return!1;let n=e.split(".").map(Number),r=t.split(".").map(Number),o=n.findIndex((e,t)=>e!==r[t]);return o>=0&&n[o]<r[o]}(r,e.resourceVersion))?null:{...e,resourceVersion:r,stateSchemaVersion:n}}(u.identity,e);r&&(n=await u.progress.load(r))}if(!n||t)return;let r=e.restore(n,u);if("restored"===r.status){let e=h.current;c(e?e(r.state):r.state)}}).catch(()=>{}).finally(()=>{t||(p.current=!0,f(!0))}),()=>{t=!0}},[u,e,m]),(0,t.useEffect)(()=>{if(!p.current)return;let t=window.setTimeout(()=>{(0,n.saveResourceProgress)(u,e.serialize(l,u))},300);return()=>window.clearTimeout(t)},[u,e,l]),{state:l,setState:c,runtimeReady:d}},"usePrefersReducedMotion",0,function(){return(0,t.useSyncExternalStore)(u,a,()=>!1)},"useResourceState",0,function(e){let[n,i]=(0,t.useState)(e);return{state:n,setState:i,runtimeReady:(0,t.useSyncExternalStore)(s,()=>!0,()=>!1)}}],719818)}]);