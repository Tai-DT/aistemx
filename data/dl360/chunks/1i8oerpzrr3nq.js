(globalThis.TURBOPACK||(globalThis.TURBOPACK=[])).push(["object"==typeof document?document.currentScript:void 0,443216,e=>{"use strict";var t=e.i(931067),i=e.i(271645),n=e.i(190072),r=e.i(848546),s=e.i(547736),o=s,a=e.i(132533);class l extends a.LineSegmentsGeometry{constructor(){super(),this.isLineGeometry=!0,this.type="LineGeometry"}setPositions(e){let t=e.length-3,i=new Float32Array(2*t);for(let n=0;n<t;n+=3)i[2*n]=e[n],i[2*n+1]=e[n+1],i[2*n+2]=e[n+2],i[2*n+3]=e[n+3],i[2*n+4]=e[n+4],i[2*n+5]=e[n+5];return super.setPositions(i),this}setColors(e,t=3){let i=e.length-t,n=new Float32Array(2*i);if(3===t)for(let r=0;r<i;r+=t)n[2*r]=e[r],n[2*r+1]=e[r+1],n[2*r+2]=e[r+2],n[2*r+3]=e[r+3],n[2*r+4]=e[r+4],n[2*r+5]=e[r+5];else for(let r=0;r<i;r+=t)n[2*r]=e[r],n[2*r+1]=e[r+1],n[2*r+2]=e[r+2],n[2*r+3]=e[r+3],n[2*r+4]=e[r+4],n[2*r+5]=e[r+5],n[2*r+6]=e[r+6],n[2*r+7]=e[r+7];return super.setColors(n,t),this}fromLine(e){let t=e.geometry;return this.setPositions(t.attributes.position.array),this}}var u=e.i(107985);class c extends o.LineSegments2{constructor(e=new l,t=new u.LineMaterial({color:0xffffff*Math.random()})){super(e,t),this.isLine2=!0,this.type="Line2"}}let d=i.forwardRef(function({points:e,color:o=0xffffff,vertexColors:d,linewidth:f,lineWidth:p,segments:m,dashed:h,...v},y){var S,g;let x=(0,r.useThree)(e=>e.size),b=i.useMemo(()=>m?new s.LineSegments2:new c,[m]),[w]=i.useState(()=>new u.LineMaterial),E=(null==d||null==(S=d[0])?void 0:S.length)===4?4:3,A=i.useMemo(()=>{let t=m?new a.LineSegmentsGeometry:new l,i=e.map(e=>{let t=Array.isArray(e);return e instanceof n.Vector3||e instanceof n.Vector4?[e.x,e.y,e.z]:e instanceof n.Vector2?[e.x,e.y,0]:t&&3===e.length?[e[0],e[1],e[2]]:t&&2===e.length?[e[0],e[1],0]:e});if(t.setPositions(i.flat()),d){o=0xffffff;let e=d.map(e=>e instanceof n.Color?e.toArray():e);t.setColors(e.flat(),E)}return t},[e,m,d,E]);return i.useLayoutEffect(()=>{b.computeLineDistances()},[e,b]),i.useLayoutEffect(()=>{h?w.defines.USE_DASH="":delete w.defines.USE_DASH,w.needsUpdate=!0},[h,w]),i.useEffect(()=>()=>{A.dispose(),w.dispose()},[A]),i.createElement("primitive",(0,t.default)({object:b,ref:y},v),i.createElement("primitive",{object:A,attach:"geometry"}),i.createElement("primitive",(0,t.default)({object:w,attach:"material",color:o,vertexColors:!!d,resolution:[x.width,x.height],linewidth:null!=(g=null!=f?f:p)?g:1,dashed:h,transparent:4===E},v)))});e.s(["Line",0,d],443216)},131497,e=>{"use strict";let t=parseInt(e.i(190072).REVISION.replace(/\D+/g,""));e.s(["version",0,t])},107985,e=>{"use strict";var t=e.i(190072),i=e.i(408560),n=e.i(131497);class r extends t.ShaderMaterial{constructor(e){super({type:"LineMaterial",uniforms:t.UniformsUtils.clone(t.UniformsUtils.merge([i.UniformsLib.common,i.UniformsLib.fog,{worldUnits:{value:1},linewidth:{value:1},resolution:{value:new t.Vector2(1,1)},dashOffset:{value:0},dashScale:{value:1},dashSize:{value:1},gapSize:{value:1}}])),vertexShader:`
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
					#include <${n.version>=154?"colorspace_fragment":"encodings_fragment"}>
					#include <fog_fragment>
					#include <premultiplied_alpha_fragment>

				}
			`,clipping:!0}),this.isLineMaterial=!0,this.onBeforeCompile=function(){this.transparent?this.defines.USE_LINE_COLOR_ALPHA="1":delete this.defines.USE_LINE_COLOR_ALPHA},Object.defineProperties(this,{color:{enumerable:!0,get:function(){return this.uniforms.diffuse.value},set:function(e){this.uniforms.diffuse.value=e}},worldUnits:{enumerable:!0,get:function(){return"WORLD_UNITS"in this.defines},set:function(e){!0===e?this.defines.WORLD_UNITS="":delete this.defines.WORLD_UNITS}},linewidth:{enumerable:!0,get:function(){return this.uniforms.linewidth.value},set:function(e){this.uniforms.linewidth.value=e}},dashed:{enumerable:!0,get:function(){return"USE_DASH"in this.defines},set(e){!!e!="USE_DASH"in this.defines&&(this.needsUpdate=!0),!0===e?this.defines.USE_DASH="":delete this.defines.USE_DASH}},dashScale:{enumerable:!0,get:function(){return this.uniforms.dashScale.value},set:function(e){this.uniforms.dashScale.value=e}},dashSize:{enumerable:!0,get:function(){return this.uniforms.dashSize.value},set:function(e){this.uniforms.dashSize.value=e}},dashOffset:{enumerable:!0,get:function(){return this.uniforms.dashOffset.value},set:function(e){this.uniforms.dashOffset.value=e}},gapSize:{enumerable:!0,get:function(){return this.uniforms.gapSize.value},set:function(e){this.uniforms.gapSize.value=e}},opacity:{enumerable:!0,get:function(){return this.uniforms.opacity.value},set:function(e){this.uniforms.opacity.value=e}},resolution:{enumerable:!0,get:function(){return this.uniforms.resolution.value},set:function(e){this.uniforms.resolution.value.copy(e)}},alphaToCoverage:{enumerable:!0,get:function(){return"USE_ALPHA_TO_COVERAGE"in this.defines},set:function(e){!!e!="USE_ALPHA_TO_COVERAGE"in this.defines&&(this.needsUpdate=!0),!0===e?(this.defines.USE_ALPHA_TO_COVERAGE="",this.extensions.derivatives=!0):(delete this.defines.USE_ALPHA_TO_COVERAGE,this.extensions.derivatives=!1)}}}),this.setValues(e)}}e.s(["LineMaterial",0,r])},547736,e=>{"use strict";let t,i;var n=e.i(190072),r=e.i(132533),s=e.i(107985);let o=e.i(131497).version>=125?"uv1":"uv2",a=new n.Vector4,l=new n.Vector3,u=new n.Vector3,c=new n.Vector4,d=new n.Vector4,f=new n.Vector4,p=new n.Vector3,m=new n.Matrix4,h=new n.Line3,v=new n.Vector3,y=new n.Box3,S=new n.Sphere,g=new n.Vector4;function x(e,t,n){return g.set(0,0,-t,1).applyMatrix4(e.projectionMatrix),g.multiplyScalar(1/g.w),g.x=i/n.width,g.y=i/n.height,g.applyMatrix4(e.projectionMatrixInverse),g.multiplyScalar(1/g.w),Math.abs(Math.max(g.x,g.y))}class b extends n.Mesh{constructor(e=new r.LineSegmentsGeometry,t=new s.LineMaterial({color:0xffffff*Math.random()})){super(e,t),this.isLineSegments2=!0,this.type="LineSegments2"}computeLineDistances(){let e=this.geometry,t=e.attributes.instanceStart,i=e.attributes.instanceEnd,r=new Float32Array(2*t.count);for(let e=0,n=0,s=t.count;e<s;e++,n+=2)l.fromBufferAttribute(t,e),u.fromBufferAttribute(i,e),r[n]=0===n?0:r[n-1],r[n+1]=r[n]+l.distanceTo(u);let s=new n.InstancedInterleavedBuffer(r,2,1);return e.setAttribute("instanceDistanceStart",new n.InterleavedBufferAttribute(s,1,0)),e.setAttribute("instanceDistanceEnd",new n.InterleavedBufferAttribute(s,1,1)),this}raycast(e,r){let s,a,l=this.material.worldUnits,u=e.camera;null!==u||l||console.error('LineSegments2: "Raycaster.camera" needs to be set in order to raycast against LineSegments2 while worldUnits is set to false.');let g=void 0!==e.params.Line2&&e.params.Line2.threshold||0;t=e.ray;let b=this.matrixWorld,w=this.geometry,E=this.material;if(i=E.linewidth+g,null===w.boundingSphere&&w.computeBoundingSphere(),S.copy(w.boundingSphere).applyMatrix4(b),l)s=.5*i;else{let e=Math.max(u.near,S.distanceToPoint(t.origin));s=x(u,e,E.resolution)}if(S.radius+=s,!1!==t.intersectsSphere(S)){if(null===w.boundingBox&&w.computeBoundingBox(),y.copy(w.boundingBox).applyMatrix4(b),l)a=.5*i;else{let e=Math.max(u.near,y.distanceToPoint(t.origin));a=x(u,e,E.resolution)}y.expandByScalar(a),!1!==t.intersectsBox(y)&&(l?function(e,r){let s=e.matrixWorld,a=e.geometry,l=a.attributes.instanceStart,u=a.attributes.instanceEnd,c=Math.min(a.instanceCount,l.count);for(let a=0;a<c;a++){h.start.fromBufferAttribute(l,a),h.end.fromBufferAttribute(u,a),h.applyMatrix4(s);let c=new n.Vector3,d=new n.Vector3;t.distanceSqToSegment(h.start,h.end,d,c),d.distanceTo(c)<.5*i&&r.push({point:d,pointOnLine:c,distance:t.origin.distanceTo(d),object:e,face:null,faceIndex:a,uv:null,[o]:null})}}(this,r):function(e,r,s){let a=r.projectionMatrix,l=e.material.resolution,u=e.matrixWorld,y=e.geometry,S=y.attributes.instanceStart,g=y.attributes.instanceEnd,x=Math.min(y.instanceCount,S.count),b=-r.near;t.at(1,f),f.w=1,f.applyMatrix4(r.matrixWorldInverse),f.applyMatrix4(a),f.multiplyScalar(1/f.w),f.x*=l.x/2,f.y*=l.y/2,f.z=0,p.copy(f),m.multiplyMatrices(r.matrixWorldInverse,u);for(let r=0;r<x;r++){if(c.fromBufferAttribute(S,r),d.fromBufferAttribute(g,r),c.w=1,d.w=1,c.applyMatrix4(m),d.applyMatrix4(m),c.z>b&&d.z>b)continue;if(c.z>b){let e=c.z-d.z,t=(c.z-b)/e;c.lerp(d,t)}else if(d.z>b){let e=d.z-c.z,t=(d.z-b)/e;d.lerp(c,t)}c.applyMatrix4(a),d.applyMatrix4(a),c.multiplyScalar(1/c.w),d.multiplyScalar(1/d.w),c.x*=l.x/2,c.y*=l.y/2,d.x*=l.x/2,d.y*=l.y/2,h.start.copy(c),h.start.z=0,h.end.copy(d),h.end.z=0;let f=h.closestPointToPointParameter(p,!0);h.at(f,v);let y=n.MathUtils.lerp(c.z,d.z,f),x=y>=-1&&y<=1,w=p.distanceTo(v)<.5*i;if(x&&w){h.start.fromBufferAttribute(S,r),h.end.fromBufferAttribute(g,r),h.start.applyMatrix4(u),h.end.applyMatrix4(u);let i=new n.Vector3,a=new n.Vector3;t.distanceSqToSegment(h.start,h.end,a,i),s.push({point:a,pointOnLine:i,distance:t.origin.distanceTo(a),object:e,face:null,faceIndex:r,uv:null,[o]:null})}}}(this,u,r))}}onBeforeRender(e){let t=this.material.uniforms;t&&t.resolution&&(e.getViewport(a),this.material.uniforms.resolution.value.set(a.z,a.w))}}e.s(["LineSegments2",0,b],547736)},132533,e=>{"use strict";var t=e.i(190072);let i=new t.Box3,n=new t.Vector3;class r extends t.InstancedBufferGeometry{constructor(){super(),this.isLineSegmentsGeometry=!0,this.type="LineSegmentsGeometry",this.setIndex([0,2,1,2,3,1,2,4,3,4,5,3,4,6,5,6,7,5]),this.setAttribute("position",new t.Float32BufferAttribute([-1,2,0,1,2,0,-1,1,0,1,1,0,-1,0,0,1,0,0,-1,-1,0,1,-1,0],3)),this.setAttribute("uv",new t.Float32BufferAttribute([-1,2,1,2,-1,1,1,1,-1,-1,1,-1,-1,-2,1,-2],2))}applyMatrix4(e){let t=this.attributes.instanceStart,i=this.attributes.instanceEnd;return void 0!==t&&(t.applyMatrix4(e),i.applyMatrix4(e),t.needsUpdate=!0),null!==this.boundingBox&&this.computeBoundingBox(),null!==this.boundingSphere&&this.computeBoundingSphere(),this}setPositions(e){let i;e instanceof Float32Array?i=e:Array.isArray(e)&&(i=new Float32Array(e));let n=new t.InstancedInterleavedBuffer(i,6,1);return this.setAttribute("instanceStart",new t.InterleavedBufferAttribute(n,3,0)),this.setAttribute("instanceEnd",new t.InterleavedBufferAttribute(n,3,3)),this.computeBoundingBox(),this.computeBoundingSphere(),this}setColors(e,i=3){let n;e instanceof Float32Array?n=e:Array.isArray(e)&&(n=new Float32Array(e));let r=new t.InstancedInterleavedBuffer(n,2*i,1);return this.setAttribute("instanceColorStart",new t.InterleavedBufferAttribute(r,i,0)),this.setAttribute("instanceColorEnd",new t.InterleavedBufferAttribute(r,i,i)),this}fromWireframeGeometry(e){return this.setPositions(e.attributes.position.array),this}fromEdgesGeometry(e){return this.setPositions(e.attributes.position.array),this}fromMesh(e){return this.fromWireframeGeometry(new t.WireframeGeometry(e.geometry)),this}fromLineSegments(e){let t=e.geometry;return this.setPositions(t.attributes.position.array),this}computeBoundingBox(){null===this.boundingBox&&(this.boundingBox=new t.Box3);let e=this.attributes.instanceStart,n=this.attributes.instanceEnd;void 0!==e&&void 0!==n&&(this.boundingBox.setFromBufferAttribute(e),i.setFromBufferAttribute(n),this.boundingBox.union(i))}computeBoundingSphere(){null===this.boundingSphere&&(this.boundingSphere=new t.Sphere),null===this.boundingBox&&this.computeBoundingBox();let e=this.attributes.instanceStart,i=this.attributes.instanceEnd;if(void 0!==e&&void 0!==i){let t=this.boundingSphere.center;this.boundingBox.getCenter(t);let r=0;for(let s=0,o=e.count;s<o;s++)n.fromBufferAttribute(e,s),r=Math.max(r,t.distanceToSquared(n)),n.fromBufferAttribute(i,s),r=Math.max(r,t.distanceToSquared(n));this.boundingSphere.radius=Math.sqrt(r),isNaN(this.boundingSphere.radius)&&console.error("THREE.LineSegmentsGeometry.computeBoundingSphere(): Computed radius is NaN. The instanced position data is likely to have NaN values.",this)}}toJSON(){}applyMatrix(e){return console.warn("THREE.LineSegmentsGeometry: applyMatrix() has been renamed to applyMatrix4()."),this.applyMatrix4(e)}}e.s(["LineSegmentsGeometry",0,r])},331935,e=>{"use strict";var t=e.i(190072);class i extends t.Scene{constructor(){super(),this.name="RoomEnvironment",this.position.y=-3.5;const e=new t.BoxGeometry;e.deleteAttribute("uv");const i=new t.MeshStandardMaterial({side:t.BackSide}),r=new t.MeshStandardMaterial,s=new t.PointLight(0xffffff,900,28,2);s.position.set(.418,16.199,.3),this.add(s);const o=new t.Mesh(e,i);o.position.set(-.757,13.219,.717),o.scale.set(31.713,28.305,28.591),this.add(o);const a=new t.InstancedMesh(e,r,6),l=new t.Object3D;l.position.set(-10.906,2.009,1.846),l.rotation.set(0,-.195,0),l.scale.set(2.328,7.905,4.651),l.updateMatrix(),a.setMatrixAt(0,l.matrix),l.position.set(-5.607,-.754,-.758),l.rotation.set(0,.994,0),l.scale.set(1.97,1.534,3.955),l.updateMatrix(),a.setMatrixAt(1,l.matrix),l.position.set(6.167,.857,7.803),l.rotation.set(0,.561,0),l.scale.set(3.927,6.285,3.687),l.updateMatrix(),a.setMatrixAt(2,l.matrix),l.position.set(-2.017,.018,6.124),l.rotation.set(0,.333,0),l.scale.set(2.002,4.566,2.064),l.updateMatrix(),a.setMatrixAt(3,l.matrix),l.position.set(2.291,-.756,-2.621),l.rotation.set(0,-.286,0),l.scale.set(1.546,1.552,1.496),l.updateMatrix(),a.setMatrixAt(4,l.matrix),l.position.set(-2.193,-.369,-5.547),l.rotation.set(0,.516,0),l.scale.set(3.875,3.487,2.986),l.updateMatrix(),a.setMatrixAt(5,l.matrix),this.add(a);const u=new t.Mesh(e,n(50));u.position.set(-16.116,14.37,8.208),u.scale.set(.1,2.428,2.739),this.add(u);const c=new t.Mesh(e,n(50));c.position.set(-16.109,18.021,-8.207),c.scale.set(.1,2.425,2.751),this.add(c);const d=new t.Mesh(e,n(17));d.position.set(14.904,12.198,-1.832),d.scale.set(.15,4.265,6.331),this.add(d);const f=new t.Mesh(e,n(43));f.position.set(-.462,8.89,14.52),f.scale.set(4.38,5.441,.088),this.add(f);const p=new t.Mesh(e,n(20));p.position.set(3.235,11.486,-12.541),p.scale.set(2.5,2,.1),this.add(p);const m=new t.Mesh(e,n(100));m.position.set(0,20,0),m.scale.set(1,.1,1),this.add(m)}dispose(){let e=new Set;for(let t of(this.traverse(t=>{t.isMesh&&(e.add(t.geometry),e.add(t.material))}),e))t.dispose()}}function n(e){return new t.MeshLambertMaterial({color:0,emissive:0xffffff,emissiveIntensity:e})}e.s(["RoomEnvironment",0,i])},755838,(e,t,i)=>{"use strict";var n=e.r(271645),r="function"==typeof Object.is?Object.is:function(e,t){return e===t&&(0!==e||1/e==1/t)||e!=e&&t!=t},s=n.useState,o=n.useEffect,a=n.useLayoutEffect,l=n.useDebugValue;function u(e){var t=e.getSnapshot;e=e.value;try{var i=t();return!r(e,i)}catch(e){return!0}}var c="u"<typeof window||void 0===window.document||void 0===window.document.createElement?function(e,t){return t()}:function(e,t){var i=t(),n=s({inst:{value:i,getSnapshot:t}}),r=n[0].inst,c=n[1];return a(function(){r.value=i,r.getSnapshot=t,u(r)&&c({inst:r})},[e,i,t]),o(function(){return u(r)&&c({inst:r}),e(function(){u(r)&&c({inst:r})})},[e]),l(i),i};i.useSyncExternalStore=void 0!==n.useSyncExternalStore?n.useSyncExternalStore:c},802239,(e,t,i)=>{"use strict";e.i(247167),t.exports=e.r(755838)},752822,(e,t,i)=>{"use strict";var n=e.r(271645),r=e.r(802239),s="function"==typeof Object.is?Object.is:function(e,t){return e===t&&(0!==e||1/e==1/t)||e!=e&&t!=t},o=r.useSyncExternalStore,a=n.useRef,l=n.useEffect,u=n.useMemo,c=n.useDebugValue;i.useSyncExternalStoreWithSelector=function(e,t,i,n,r){var d=a(null);if(null===d.current){var f={hasValue:!1,value:null};d.current=f}else f=d.current;var p=o(e,(d=u(function(){function e(e){if(!l){if(l=!0,o=e,e=n(e),void 0!==r&&f.hasValue){var t=f.value;if(r(t,e))return a=t}return a=e}if(t=a,s(o,e))return t;var i=n(e);return void 0!==r&&r(t,i)?(o=e,t):(o=e,a=i)}var o,a,l=!1,u=void 0===i?null:i;return[function(){return e(t())},null===u?void 0:function(){return e(u())}]},[t,i,n,r]))[0],d[1]);return l(function(){f.hasValue=!0,f.value=p},[p]),c(p),p}},430224,(e,t,i)=>{"use strict";e.i(247167),t.exports=e.r(752822)},931570,e=>{"use strict";var t=e.i(271645),i=e.i(94800),n=e.i(848546),r=e.i(190072);e.s(["default",0,function({destination:e,duration:s=.6,reducedMotion:o=!1,cancelRef:a}){let l=(0,n.useThree)(e=>e.camera),u=(0,n.useThree)(e=>e.controls),c=(0,t.useRef)(new r.Vector3),d=(0,t.useRef)(new r.Vector3),f=(0,t.useRef)(0),p=(0,t.useRef)(!1),m=(0,t.useRef)(null);(0,t.useEffect)(()=>{m.current=e},[e]);let h=(0,t.useCallback)(()=>{p.current=!1},[]);(0,t.useEffect)(()=>{if(a)return a.current=h,()=>{a.current===h&&(a.current=null)}},[h,a]);let v=e?`${e.position.x.toFixed(4)},${e.position.y.toFixed(4)},${e.position.z.toFixed(4)}|${e.target.x.toFixed(4)},${e.target.y.toFixed(4)},${e.target.z.toFixed(4)}`:"none";return(0,t.useEffect)(()=>{if(!e){p.current=!1;return}if(o){l.position.copy(e.position),u&&(u.target.copy(e.target),u.update()),p.current=!1;return}c.current.copy(l.position),d.current.copy(u?.target??l.position.clone()),f.current=0,p.current=!0},[v,o]),(0,i.useFrame)((e,t)=>{let i=m.current;if(!p.current||!i)return;f.current=Math.min(1,f.current+t/s);let n=f.current,r=n*n*(3-2*n);l.position.lerpVectors(c.current,i.position,r),u&&(u.target.lerpVectors(d.current,i.target,r),u.update()),n>=1&&(p.current=!1)}),null}])},482629,e=>{"use strict";var t=e.i(843476),i=e.i(807468);e.s(["default",0,function({value:e,placeholder:n,ariaLabel:r,options:s,disabled:o=!1,className:a="",testId:l,onSelect:u}){let c=(0,i.useCanvasToolbarEnabled)(),d=(0,i.useCanvasControlLabels)().canvasToolbar;return(0,t.jsx)(i.ResourceCanvasControls,{slot:"secondary",children:(0,t.jsxs)("select",{"aria-label":r,value:c?"":e,disabled:o,onChange:e=>u(e.target.value),"data-testid":l,className:`min-h-10 cursor-pointer rounded-lg border border-slate-300 bg-white px-2 text-xs font-bold text-slate-700 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-600 disabled:cursor-not-allowed disabled:opacity-45 ${a}`,children:[(0,t.jsx)("option",{value:"",disabled:!0,children:c?d.camera:n}),s.map(e=>(0,t.jsx)("option",{value:e.id,children:e.label},e.id))]})})}])},173596,e=>{"use strict";function t(e){return"number"==typeof e&&Number.isFinite(e)}function i(e,i,n){return t(e)&&e>=i&&e<=n}e.s(["isBoolean",0,function(e){return"boolean"==typeof e},"isFiniteNumber",0,t,"isNumberInRange",0,i,"isOnGrid",0,function(e,t){if(!i(e,t.minimum,t.maximum))return!1;let n=(e-t.minimum)/t.step;return 1e-6>Math.abs(n-Math.round(n))},"isOneOf",0,function(e,t){return t.includes(e)},"isRecord",0,function(e){return"object"==typeof e&&null!==e&&!Array.isArray(e)},"snapToGrid",0,function(e,t){if(!Number.isFinite(e))return null;let i=Math.round((Math.min(t.maximum,Math.max(t.minimum,e))-t.minimum)/t.step);return Number((t.minimum+i*t.step).toFixed(6))}])},719818,e=>{"use strict";var t=e.i(271645),i=e.i(422771);let n=/^(0|[1-9]\d*)\.\d+\.\d+$/;var r=e.i(246829);let s=[],o=()=>()=>void 0;function a(){return window.matchMedia("(prefers-reduced-motion: reduce)").matches}function l(e){let t=window.matchMedia("(prefers-reduced-motion: reduce)");return t.addEventListener("change",e),()=>t.removeEventListener("change",e)}e.s(["usePersistentResourceState",0,function(e,o,a=s){let l=(0,r.useResourceRuntime)(),[u,c]=(0,t.useState)(e.reset),[d,f]=(0,t.useState)(!1),p=(0,t.useRef)(!1),m=JSON.stringify(a),h=(0,t.useRef)(o);return(0,t.useEffect)(()=>{h.current=o},[o]),(0,t.useEffect)(()=>{let t=!1;return l.progress.load(l.identity).then(async i=>{for(let e of JSON.parse(m)){if(i||t)break;let r=function(e,t){let i="number"==typeof t?t:t?.stateSchemaVersion,r="number"==typeof t?e.resourceVersion:t?.resourceVersion;return!Number.isInteger(i)||i<1||i>e.stateSchemaVersion||"string"!=typeof r||!n.test(r)||i===e.stateSchemaVersion&&("number"==typeof t||!function(e,t){if(!n.test(e)||!n.test(t))return!1;let i=e.split(".").map(Number),r=t.split(".").map(Number),s=i.findIndex((e,t)=>e!==r[t]);return s>=0&&i[s]<r[s]}(r,e.resourceVersion))?null:{...e,resourceVersion:r,stateSchemaVersion:i}}(l.identity,e);r&&(i=await l.progress.load(r))}if(!i||t)return;let r=e.restore(i,l);if("restored"===r.status){let e=h.current;c(e?e(r.state):r.state)}}).catch(()=>{}).finally(()=>{t||(p.current=!0,f(!0))}),()=>{t=!0}},[l,e,m]),(0,t.useEffect)(()=>{if(!p.current)return;let t=window.setTimeout(()=>{(0,i.saveResourceProgress)(l,e.serialize(u,l))},300);return()=>window.clearTimeout(t)},[l,e,u]),{state:u,setState:c,runtimeReady:d}},"usePrefersReducedMotion",0,function(){return(0,t.useSyncExternalStore)(l,a,()=>!1)},"useResourceState",0,function(e){let[i,n]=(0,t.useState)(e);return{state:i,setState:n,runtimeReady:(0,t.useSyncExternalStore)(o,()=>!0,()=>!1)}}],719818)}]);