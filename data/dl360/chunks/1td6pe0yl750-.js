(globalThis.TURBOPACK||(globalThis.TURBOPACK=[])).push(["object"==typeof document?document.currentScript:void 0,443216,e=>{"use strict";var t=e.i(931067),r=e.i(271645),n=e.i(190072),i=e.i(848546),o=e.i(547736),s=o,a=e.i(132533);class l extends a.LineSegmentsGeometry{constructor(){super(),this.isLineGeometry=!0,this.type="LineGeometry"}setPositions(e){let t=e.length-3,r=new Float32Array(2*t);for(let n=0;n<t;n+=3)r[2*n]=e[n],r[2*n+1]=e[n+1],r[2*n+2]=e[n+2],r[2*n+3]=e[n+3],r[2*n+4]=e[n+4],r[2*n+5]=e[n+5];return super.setPositions(r),this}setColors(e,t=3){let r=e.length-t,n=new Float32Array(2*r);if(3===t)for(let i=0;i<r;i+=t)n[2*i]=e[i],n[2*i+1]=e[i+1],n[2*i+2]=e[i+2],n[2*i+3]=e[i+3],n[2*i+4]=e[i+4],n[2*i+5]=e[i+5];else for(let i=0;i<r;i+=t)n[2*i]=e[i],n[2*i+1]=e[i+1],n[2*i+2]=e[i+2],n[2*i+3]=e[i+3],n[2*i+4]=e[i+4],n[2*i+5]=e[i+5],n[2*i+6]=e[i+6],n[2*i+7]=e[i+7];return super.setColors(n,t),this}fromLine(e){let t=e.geometry;return this.setPositions(t.attributes.position.array),this}}var c=e.i(107985);class u extends s.LineSegments2{constructor(e=new l,t=new c.LineMaterial({color:0xffffff*Math.random()})){super(e,t),this.isLine2=!0,this.type="Line2"}}let d=r.forwardRef(function({points:e,color:s=0xffffff,vertexColors:d,linewidth:f,lineWidth:p,segments:m,dashed:h,...v},y){var g,x;let S=(0,i.useThree)(e=>e.size),w=r.useMemo(()=>m?new o.LineSegments2:new u,[m]),[b]=r.useState(()=>new c.LineMaterial),E=(null==d||null==(g=d[0])?void 0:g.length)===4?4:3,M=r.useMemo(()=>{let t=m?new a.LineSegmentsGeometry:new l,r=e.map(e=>{let t=Array.isArray(e);return e instanceof n.Vector3||e instanceof n.Vector4?[e.x,e.y,e.z]:e instanceof n.Vector2?[e.x,e.y,0]:t&&3===e.length?[e[0],e[1],e[2]]:t&&2===e.length?[e[0],e[1],0]:e});if(t.setPositions(r.flat()),d){s=0xffffff;let e=d.map(e=>e instanceof n.Color?e.toArray():e);t.setColors(e.flat(),E)}return t},[e,m,d,E]);return r.useLayoutEffect(()=>{w.computeLineDistances()},[e,w]),r.useLayoutEffect(()=>{h?b.defines.USE_DASH="":delete b.defines.USE_DASH,b.needsUpdate=!0},[h,b]),r.useEffect(()=>()=>{M.dispose(),b.dispose()},[M]),r.createElement("primitive",(0,t.default)({object:w,ref:y},v),r.createElement("primitive",{object:M,attach:"geometry"}),r.createElement("primitive",(0,t.default)({object:b,attach:"material",color:s,vertexColors:!!d,resolution:[S.width,S.height],linewidth:null!=(x=null!=f?f:p)?x:1,dashed:h,transparent:4===E},v)))});e.s(["Line",0,d],443216)},560099,e=>{"use strict";let t,r;var n=e.i(931067),i=e.i(271645),o=e.i(88014),s=e.i(190072),a=e.i(848546),l=e.i(94800);let c=new s.Vector3,u=new s.Vector3,d=new s.Vector3,f=new s.Vector2;function p(e,t,r){let n=c.setFromMatrixPosition(e.matrixWorld);n.project(t);let i=r.width/2,o=r.height/2;return[n.x*i+i,-(n.y*o)+o]}let m=e=>1e-10>Math.abs(e)?0:e;function h(e,t,r=""){let n="matrix3d(";for(let r=0;16!==r;r++)n+=m(t[r]*e.elements[r])+(15!==r?",":")");return r+n}let v=(t=[1,-1,1,1,1,-1,1,1,1,-1,1,1,1,-1,1,1],e=>h(e,t)),y=(r=e=>[1/e,1/e,1/e,1,-1/e,-1/e,-1/e,-1,1/e,1/e,1/e,1,1,1,1,1],(e,t)=>h(e,r(t),"translate(-50%,-50%)")),g=i.forwardRef(({children:e,eps:t=.001,style:r,className:h,prepend:g,center:x,fullscreen:S,portal:w,distanceFactor:b,sprite:E=!1,transform:M=!1,occlude:A,onOcclude:L,castShadow:_,receiveShadow:z,material:U,geometry:P,zIndexRange:O=[0x1000037,0],calculatePosition:C=p,as:R="div",wrapperClass:B,pointerEvents:T="auto",...V},D)=>{let{gl:I,camera:W,scene:j,size:H,raycaster:F,events:N,viewport:$}=(0,a.useThree)(),[G]=i.useState(()=>document.createElement(R)),k=i.useRef(null),q=i.useRef(null),J=i.useRef(0),K=i.useRef([0,0]),X=i.useRef(null),Z=i.useRef(null),Q=(null==w?void 0:w.current)||N.connected||I.domElement.parentNode,Y=i.useRef(null),ee=i.useRef(!1),et=i.useMemo(()=>{var e;return A&&"blending"!==A||Array.isArray(A)&&A.length&&(e=A[0])&&"object"==typeof e&&"current"in e},[A]);i.useLayoutEffect(()=>{let e=I.domElement;A&&"blending"===A?(e.style.zIndex=`${Math.floor(O[0]/2)}`,e.style.position="absolute",e.style.pointerEvents="none"):(e.style.zIndex=null,e.style.position=null,e.style.pointerEvents=null)},[A]),i.useLayoutEffect(()=>{if(q.current){let e=k.current=o.createRoot(G);if(j.updateMatrixWorld(),M)G.style.cssText="position:absolute;top:0;left:0;pointer-events:none;overflow:hidden;";else{let e=C(q.current,W,H);G.style.cssText=`position:absolute;top:0;left:0;transform:translate3d(${e[0]}px,${e[1]}px,0);transform-origin:0 0;`}return Q&&(g?Q.prepend(G):Q.appendChild(G)),()=>{Q&&Q.removeChild(G),e.unmount()}}},[Q,M]),i.useLayoutEffect(()=>{B&&(G.className=B)},[B]);let er=i.useMemo(()=>M?{position:"absolute",top:0,left:0,width:H.width,height:H.height,transformStyle:"preserve-3d",pointerEvents:"none"}:{position:"absolute",transform:x?"translate3d(-50%,-50%,0)":"none",...S&&{top:-H.height/2,left:-H.width/2,width:H.width,height:H.height},...r},[r,x,S,H,M]),en=i.useMemo(()=>({position:"absolute",pointerEvents:T}),[T]);i.useLayoutEffect(()=>{var t,n;ee.current=!1,M?null==(t=k.current)||t.render(i.createElement("div",{ref:X,style:er},i.createElement("div",{ref:Z,style:en},i.createElement("div",{ref:D,className:h,style:r,children:e})))):null==(n=k.current)||n.render(i.createElement("div",{ref:D,style:er,className:h,children:e}))});let ei=i.useRef(!0);(0,l.useFrame)(e=>{if(q.current){W.updateMatrixWorld(),q.current.updateWorldMatrix(!0,!1);let e=M?K.current:C(q.current,W,H);if(M||Math.abs(J.current-W.zoom)>t||Math.abs(K.current[0]-e[0])>t||Math.abs(K.current[1]-e[1])>t){var r;let t,n,i,o,a=(r=q.current,t=c.setFromMatrixPosition(r.matrixWorld),n=u.setFromMatrixPosition(W.matrixWorld),i=t.sub(n),o=W.getWorldDirection(d),i.angleTo(o)>Math.PI/2),l=!1;et&&(Array.isArray(A)?l=A.map(e=>e.current):"blending"!==A&&(l=[j]));let p=ei.current;l?ei.current=function(e,t,r,n){let i=c.setFromMatrixPosition(e.matrixWorld),o=i.clone();o.project(t),f.set(o.x,o.y),r.setFromCamera(f,t);let s=r.intersectObjects(n,!0);if(s.length){let e=s[0].distance;return i.distanceTo(r.ray.origin)<e}return!0}(q.current,W,F,l)&&!a:ei.current=!a,p!==ei.current&&(L?L(!ei.current):G.style.display=ei.current?"block":"none");let h=Math.floor(O[0]/2),g=A?et?[O[0],h]:[h-1,0]:O;if(G.style.zIndex=`${function(e,t,r){if(t instanceof s.PerspectiveCamera||t instanceof s.OrthographicCamera){let n=c.setFromMatrixPosition(e.matrixWorld),i=u.setFromMatrixPosition(t.matrixWorld),o=n.distanceTo(i),s=(r[1]-r[0])/(t.far-t.near),a=r[1]-s*t.far;return Math.round(s*o+a)}}(q.current,W,g)}`,M){let[e,t]=[H.width/2,H.height/2],r=W.projectionMatrix.elements[5]*t,{isOrthographicCamera:n,top:i,left:o,bottom:s,right:a}=W,l=v(W.matrixWorldInverse),c=n?`scale(${r})translate(${m(-(a+o)/2)}px,${m((i+s)/2)}px)`:`translateZ(${r}px)`,u=q.current.matrixWorld;E&&((u=W.matrixWorldInverse.clone().transpose().copyPosition(u).scale(q.current.scale)).elements[3]=u.elements[7]=u.elements[11]=0,u.elements[15]=1),G.style.width=H.width+"px",G.style.height=H.height+"px",G.style.perspective=n?"":`${r}px`,X.current&&Z.current&&(X.current.style.transform=`${c}${l}translate(${e}px,${t}px)`,Z.current.style.transform=y(u,1/((b||10)/400)))}else{let t=void 0===b?1:function(e,t){if(t instanceof s.OrthographicCamera)return t.zoom;if(!(t instanceof s.PerspectiveCamera))return 1;{let r=c.setFromMatrixPosition(e.matrixWorld),n=u.setFromMatrixPosition(t.matrixWorld);return 1/(2*Math.tan(t.fov*Math.PI/180/2)*r.distanceTo(n))}}(q.current,W)*b;G.style.transform=`translate3d(${e[0]}px,${e[1]}px,0) scale(${t})`}K.current=e,J.current=W.zoom}}if(!et&&Y.current&&!ee.current)if(M){if(X.current){let e=X.current.children[0];if(null!=e&&e.clientWidth&&null!=e&&e.clientHeight){let{isOrthographicCamera:t}=W;if(t||P)V.scale&&(Array.isArray(V.scale)?V.scale instanceof s.Vector3?Y.current.scale.copy(V.scale.clone().divideScalar(1)):Y.current.scale.set(1/V.scale[0],1/V.scale[1],1/V.scale[2]):Y.current.scale.setScalar(1/V.scale));else{let t=(b||10)/400,r=e.clientWidth*t,n=e.clientHeight*t;Y.current.scale.set(r,n,1)}ee.current=!0}}}else{let t=G.children[0];if(null!=t&&t.clientWidth&&null!=t&&t.clientHeight){let e=1/$.factor,r=t.clientWidth*e,n=t.clientHeight*e;Y.current.scale.set(r,n,1),ee.current=!0}Y.current.lookAt(e.camera.position)}});let eo=i.useMemo(()=>({vertexShader:M?void 0:`
          /*
            This shader is from the THREE's SpriteMaterial.
            We need to turn the backing plane into a Sprite
            (make it always face the camera) if "transfrom"
            is false.
          */
          #include <common>

          void main() {
            vec2 center = vec2(0., 1.);
            float rotation = 0.0;

            // This is somewhat arbitrary, but it seems to work well
            // Need to figure out how to derive this dynamically if it even matters
            float size = 0.03;

            vec4 mvPosition = modelViewMatrix * vec4( 0.0, 0.0, 0.0, 1.0 );
            vec2 scale;
            scale.x = length( vec3( modelMatrix[ 0 ].x, modelMatrix[ 0 ].y, modelMatrix[ 0 ].z ) );
            scale.y = length( vec3( modelMatrix[ 1 ].x, modelMatrix[ 1 ].y, modelMatrix[ 1 ].z ) );

            bool isPerspective = isPerspectiveMatrix( projectionMatrix );
            if ( isPerspective ) scale *= - mvPosition.z;

            vec2 alignedPosition = ( position.xy - ( center - vec2( 0.5 ) ) ) * scale * size;
            vec2 rotatedPosition;
            rotatedPosition.x = cos( rotation ) * alignedPosition.x - sin( rotation ) * alignedPosition.y;
            rotatedPosition.y = sin( rotation ) * alignedPosition.x + cos( rotation ) * alignedPosition.y;
            mvPosition.xy += rotatedPosition;

            gl_Position = projectionMatrix * mvPosition;
          }
      `,fragmentShader:`
        void main() {
          gl_FragColor = vec4(0.0, 0.0, 0.0, 0.0);
        }
      `}),[M]);return i.createElement("group",(0,n.default)({},V,{ref:q}),A&&!et&&i.createElement("mesh",{castShadow:_,receiveShadow:z,ref:Y},P||i.createElement("planeGeometry",null),U||i.createElement("shaderMaterial",{side:s.DoubleSide,vertexShader:eo.vertexShader,fragmentShader:eo.fragmentShader})))});e.s(["Html",0,g])},131497,e=>{"use strict";let t=parseInt(e.i(190072).REVISION.replace(/\D+/g,""));e.s(["version",0,t])},107985,e=>{"use strict";var t=e.i(190072),r=e.i(408560),n=e.i(131497);class i extends t.ShaderMaterial{constructor(e){super({type:"LineMaterial",uniforms:t.UniformsUtils.clone(t.UniformsUtils.merge([r.UniformsLib.common,r.UniformsLib.fog,{worldUnits:{value:1},linewidth:{value:1},resolution:{value:new t.Vector2(1,1)},dashOffset:{value:0},dashScale:{value:1},dashSize:{value:1},gapSize:{value:1}}])),vertexShader:`
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
			`,clipping:!0}),this.isLineMaterial=!0,this.onBeforeCompile=function(){this.transparent?this.defines.USE_LINE_COLOR_ALPHA="1":delete this.defines.USE_LINE_COLOR_ALPHA},Object.defineProperties(this,{color:{enumerable:!0,get:function(){return this.uniforms.diffuse.value},set:function(e){this.uniforms.diffuse.value=e}},worldUnits:{enumerable:!0,get:function(){return"WORLD_UNITS"in this.defines},set:function(e){!0===e?this.defines.WORLD_UNITS="":delete this.defines.WORLD_UNITS}},linewidth:{enumerable:!0,get:function(){return this.uniforms.linewidth.value},set:function(e){this.uniforms.linewidth.value=e}},dashed:{enumerable:!0,get:function(){return"USE_DASH"in this.defines},set(e){!!e!="USE_DASH"in this.defines&&(this.needsUpdate=!0),!0===e?this.defines.USE_DASH="":delete this.defines.USE_DASH}},dashScale:{enumerable:!0,get:function(){return this.uniforms.dashScale.value},set:function(e){this.uniforms.dashScale.value=e}},dashSize:{enumerable:!0,get:function(){return this.uniforms.dashSize.value},set:function(e){this.uniforms.dashSize.value=e}},dashOffset:{enumerable:!0,get:function(){return this.uniforms.dashOffset.value},set:function(e){this.uniforms.dashOffset.value=e}},gapSize:{enumerable:!0,get:function(){return this.uniforms.gapSize.value},set:function(e){this.uniforms.gapSize.value=e}},opacity:{enumerable:!0,get:function(){return this.uniforms.opacity.value},set:function(e){this.uniforms.opacity.value=e}},resolution:{enumerable:!0,get:function(){return this.uniforms.resolution.value},set:function(e){this.uniforms.resolution.value.copy(e)}},alphaToCoverage:{enumerable:!0,get:function(){return"USE_ALPHA_TO_COVERAGE"in this.defines},set:function(e){!!e!="USE_ALPHA_TO_COVERAGE"in this.defines&&(this.needsUpdate=!0),!0===e?(this.defines.USE_ALPHA_TO_COVERAGE="",this.extensions.derivatives=!0):(delete this.defines.USE_ALPHA_TO_COVERAGE,this.extensions.derivatives=!1)}}}),this.setValues(e)}}e.s(["LineMaterial",0,i])},547736,e=>{"use strict";let t,r;var n=e.i(190072),i=e.i(132533),o=e.i(107985);let s=e.i(131497).version>=125?"uv1":"uv2",a=new n.Vector4,l=new n.Vector3,c=new n.Vector3,u=new n.Vector4,d=new n.Vector4,f=new n.Vector4,p=new n.Vector3,m=new n.Matrix4,h=new n.Line3,v=new n.Vector3,y=new n.Box3,g=new n.Sphere,x=new n.Vector4;function S(e,t,n){return x.set(0,0,-t,1).applyMatrix4(e.projectionMatrix),x.multiplyScalar(1/x.w),x.x=r/n.width,x.y=r/n.height,x.applyMatrix4(e.projectionMatrixInverse),x.multiplyScalar(1/x.w),Math.abs(Math.max(x.x,x.y))}class w extends n.Mesh{constructor(e=new i.LineSegmentsGeometry,t=new o.LineMaterial({color:0xffffff*Math.random()})){super(e,t),this.isLineSegments2=!0,this.type="LineSegments2"}computeLineDistances(){let e=this.geometry,t=e.attributes.instanceStart,r=e.attributes.instanceEnd,i=new Float32Array(2*t.count);for(let e=0,n=0,o=t.count;e<o;e++,n+=2)l.fromBufferAttribute(t,e),c.fromBufferAttribute(r,e),i[n]=0===n?0:i[n-1],i[n+1]=i[n]+l.distanceTo(c);let o=new n.InstancedInterleavedBuffer(i,2,1);return e.setAttribute("instanceDistanceStart",new n.InterleavedBufferAttribute(o,1,0)),e.setAttribute("instanceDistanceEnd",new n.InterleavedBufferAttribute(o,1,1)),this}raycast(e,i){let o,a,l=this.material.worldUnits,c=e.camera;null!==c||l||console.error('LineSegments2: "Raycaster.camera" needs to be set in order to raycast against LineSegments2 while worldUnits is set to false.');let x=void 0!==e.params.Line2&&e.params.Line2.threshold||0;t=e.ray;let w=this.matrixWorld,b=this.geometry,E=this.material;if(r=E.linewidth+x,null===b.boundingSphere&&b.computeBoundingSphere(),g.copy(b.boundingSphere).applyMatrix4(w),l)o=.5*r;else{let e=Math.max(c.near,g.distanceToPoint(t.origin));o=S(c,e,E.resolution)}if(g.radius+=o,!1!==t.intersectsSphere(g)){if(null===b.boundingBox&&b.computeBoundingBox(),y.copy(b.boundingBox).applyMatrix4(w),l)a=.5*r;else{let e=Math.max(c.near,y.distanceToPoint(t.origin));a=S(c,e,E.resolution)}y.expandByScalar(a),!1!==t.intersectsBox(y)&&(l?function(e,i){let o=e.matrixWorld,a=e.geometry,l=a.attributes.instanceStart,c=a.attributes.instanceEnd,u=Math.min(a.instanceCount,l.count);for(let a=0;a<u;a++){h.start.fromBufferAttribute(l,a),h.end.fromBufferAttribute(c,a),h.applyMatrix4(o);let u=new n.Vector3,d=new n.Vector3;t.distanceSqToSegment(h.start,h.end,d,u),d.distanceTo(u)<.5*r&&i.push({point:d,pointOnLine:u,distance:t.origin.distanceTo(d),object:e,face:null,faceIndex:a,uv:null,[s]:null})}}(this,i):function(e,i,o){let a=i.projectionMatrix,l=e.material.resolution,c=e.matrixWorld,y=e.geometry,g=y.attributes.instanceStart,x=y.attributes.instanceEnd,S=Math.min(y.instanceCount,g.count),w=-i.near;t.at(1,f),f.w=1,f.applyMatrix4(i.matrixWorldInverse),f.applyMatrix4(a),f.multiplyScalar(1/f.w),f.x*=l.x/2,f.y*=l.y/2,f.z=0,p.copy(f),m.multiplyMatrices(i.matrixWorldInverse,c);for(let i=0;i<S;i++){if(u.fromBufferAttribute(g,i),d.fromBufferAttribute(x,i),u.w=1,d.w=1,u.applyMatrix4(m),d.applyMatrix4(m),u.z>w&&d.z>w)continue;if(u.z>w){let e=u.z-d.z,t=(u.z-w)/e;u.lerp(d,t)}else if(d.z>w){let e=d.z-u.z,t=(d.z-w)/e;d.lerp(u,t)}u.applyMatrix4(a),d.applyMatrix4(a),u.multiplyScalar(1/u.w),d.multiplyScalar(1/d.w),u.x*=l.x/2,u.y*=l.y/2,d.x*=l.x/2,d.y*=l.y/2,h.start.copy(u),h.start.z=0,h.end.copy(d),h.end.z=0;let f=h.closestPointToPointParameter(p,!0);h.at(f,v);let y=n.MathUtils.lerp(u.z,d.z,f),S=y>=-1&&y<=1,b=p.distanceTo(v)<.5*r;if(S&&b){h.start.fromBufferAttribute(g,i),h.end.fromBufferAttribute(x,i),h.start.applyMatrix4(c),h.end.applyMatrix4(c);let r=new n.Vector3,a=new n.Vector3;t.distanceSqToSegment(h.start,h.end,a,r),o.push({point:a,pointOnLine:r,distance:t.origin.distanceTo(a),object:e,face:null,faceIndex:i,uv:null,[s]:null})}}}(this,c,i))}}onBeforeRender(e){let t=this.material.uniforms;t&&t.resolution&&(e.getViewport(a),this.material.uniforms.resolution.value.set(a.z,a.w))}}e.s(["LineSegments2",0,w],547736)},132533,e=>{"use strict";var t=e.i(190072);let r=new t.Box3,n=new t.Vector3;class i extends t.InstancedBufferGeometry{constructor(){super(),this.isLineSegmentsGeometry=!0,this.type="LineSegmentsGeometry",this.setIndex([0,2,1,2,3,1,2,4,3,4,5,3,4,6,5,6,7,5]),this.setAttribute("position",new t.Float32BufferAttribute([-1,2,0,1,2,0,-1,1,0,1,1,0,-1,0,0,1,0,0,-1,-1,0,1,-1,0],3)),this.setAttribute("uv",new t.Float32BufferAttribute([-1,2,1,2,-1,1,1,1,-1,-1,1,-1,-1,-2,1,-2],2))}applyMatrix4(e){let t=this.attributes.instanceStart,r=this.attributes.instanceEnd;return void 0!==t&&(t.applyMatrix4(e),r.applyMatrix4(e),t.needsUpdate=!0),null!==this.boundingBox&&this.computeBoundingBox(),null!==this.boundingSphere&&this.computeBoundingSphere(),this}setPositions(e){let r;e instanceof Float32Array?r=e:Array.isArray(e)&&(r=new Float32Array(e));let n=new t.InstancedInterleavedBuffer(r,6,1);return this.setAttribute("instanceStart",new t.InterleavedBufferAttribute(n,3,0)),this.setAttribute("instanceEnd",new t.InterleavedBufferAttribute(n,3,3)),this.computeBoundingBox(),this.computeBoundingSphere(),this}setColors(e,r=3){let n;e instanceof Float32Array?n=e:Array.isArray(e)&&(n=new Float32Array(e));let i=new t.InstancedInterleavedBuffer(n,2*r,1);return this.setAttribute("instanceColorStart",new t.InterleavedBufferAttribute(i,r,0)),this.setAttribute("instanceColorEnd",new t.InterleavedBufferAttribute(i,r,r)),this}fromWireframeGeometry(e){return this.setPositions(e.attributes.position.array),this}fromEdgesGeometry(e){return this.setPositions(e.attributes.position.array),this}fromMesh(e){return this.fromWireframeGeometry(new t.WireframeGeometry(e.geometry)),this}fromLineSegments(e){let t=e.geometry;return this.setPositions(t.attributes.position.array),this}computeBoundingBox(){null===this.boundingBox&&(this.boundingBox=new t.Box3);let e=this.attributes.instanceStart,n=this.attributes.instanceEnd;void 0!==e&&void 0!==n&&(this.boundingBox.setFromBufferAttribute(e),r.setFromBufferAttribute(n),this.boundingBox.union(r))}computeBoundingSphere(){null===this.boundingSphere&&(this.boundingSphere=new t.Sphere),null===this.boundingBox&&this.computeBoundingBox();let e=this.attributes.instanceStart,r=this.attributes.instanceEnd;if(void 0!==e&&void 0!==r){let t=this.boundingSphere.center;this.boundingBox.getCenter(t);let i=0;for(let o=0,s=e.count;o<s;o++)n.fromBufferAttribute(e,o),i=Math.max(i,t.distanceToSquared(n)),n.fromBufferAttribute(r,o),i=Math.max(i,t.distanceToSquared(n));this.boundingSphere.radius=Math.sqrt(i),isNaN(this.boundingSphere.radius)&&console.error("THREE.LineSegmentsGeometry.computeBoundingSphere(): Computed radius is NaN. The instanced position data is likely to have NaN values.",this)}}toJSON(){}applyMatrix(e){return console.warn("THREE.LineSegmentsGeometry: applyMatrix() has been renamed to applyMatrix4()."),this.applyMatrix4(e)}}e.s(["LineSegmentsGeometry",0,i])},755838,(e,t,r)=>{"use strict";var n=e.r(271645),i="function"==typeof Object.is?Object.is:function(e,t){return e===t&&(0!==e||1/e==1/t)||e!=e&&t!=t},o=n.useState,s=n.useEffect,a=n.useLayoutEffect,l=n.useDebugValue;function c(e){var t=e.getSnapshot;e=e.value;try{var r=t();return!i(e,r)}catch(e){return!0}}var u="u"<typeof window||void 0===window.document||void 0===window.document.createElement?function(e,t){return t()}:function(e,t){var r=t(),n=o({inst:{value:r,getSnapshot:t}}),i=n[0].inst,u=n[1];return a(function(){i.value=r,i.getSnapshot=t,c(i)&&u({inst:i})},[e,r,t]),s(function(){return c(i)&&u({inst:i}),e(function(){c(i)&&u({inst:i})})},[e]),l(r),r};r.useSyncExternalStore=void 0!==n.useSyncExternalStore?n.useSyncExternalStore:u},802239,(e,t,r)=>{"use strict";e.i(247167),t.exports=e.r(755838)},752822,(e,t,r)=>{"use strict";var n=e.r(271645),i=e.r(802239),o="function"==typeof Object.is?Object.is:function(e,t){return e===t&&(0!==e||1/e==1/t)||e!=e&&t!=t},s=i.useSyncExternalStore,a=n.useRef,l=n.useEffect,c=n.useMemo,u=n.useDebugValue;r.useSyncExternalStoreWithSelector=function(e,t,r,n,i){var d=a(null);if(null===d.current){var f={hasValue:!1,value:null};d.current=f}else f=d.current;var p=s(e,(d=c(function(){function e(e){if(!l){if(l=!0,s=e,e=n(e),void 0!==i&&f.hasValue){var t=f.value;if(i(t,e))return a=t}return a=e}if(t=a,o(s,e))return t;var r=n(e);return void 0!==i&&i(t,r)?(s=e,t):(s=e,a=r)}var s,a,l=!1,c=void 0===r?null:r;return[function(){return e(t())},null===c?void 0:function(){return e(c())}]},[t,r,n,i]))[0],d[1]);return l(function(){f.hasValue=!0,f.value=p},[p]),u(p),p}},430224,(e,t,r)=>{"use strict";e.i(247167),t.exports=e.r(752822)},931570,e=>{"use strict";var t=e.i(271645),r=e.i(94800),n=e.i(848546),i=e.i(190072);e.s(["default",0,function({destination:e,duration:o=.6,reducedMotion:s=!1,cancelRef:a}){let l=(0,n.useThree)(e=>e.camera),c=(0,n.useThree)(e=>e.controls),u=(0,t.useRef)(new i.Vector3),d=(0,t.useRef)(new i.Vector3),f=(0,t.useRef)(0),p=(0,t.useRef)(!1),m=(0,t.useRef)(null);(0,t.useEffect)(()=>{m.current=e},[e]);let h=(0,t.useCallback)(()=>{p.current=!1},[]);(0,t.useEffect)(()=>{if(a)return a.current=h,()=>{a.current===h&&(a.current=null)}},[h,a]);let v=e?`${e.position.x.toFixed(4)},${e.position.y.toFixed(4)},${e.position.z.toFixed(4)}|${e.target.x.toFixed(4)},${e.target.y.toFixed(4)},${e.target.z.toFixed(4)}`:"none";return(0,t.useEffect)(()=>{if(!e){p.current=!1;return}if(s){l.position.copy(e.position),c&&(c.target.copy(e.target),c.update()),p.current=!1;return}u.current.copy(l.position),d.current.copy(c?.target??l.position.clone()),f.current=0,p.current=!0},[v,s]),(0,r.useFrame)((e,t)=>{let r=m.current;if(!p.current||!r)return;f.current=Math.min(1,f.current+t/o);let n=f.current,i=n*n*(3-2*n);l.position.lerpVectors(u.current,r.position,i),c&&(c.target.lerpVectors(d.current,r.target,i),c.update()),n>=1&&(p.current=!1)}),null}])},719818,e=>{"use strict";var t=e.i(271645),r=e.i(422771);let n=/^(0|[1-9]\d*)\.\d+\.\d+$/;var i=e.i(246829);let o=[],s=()=>()=>void 0;function a(){return window.matchMedia("(prefers-reduced-motion: reduce)").matches}function l(e){let t=window.matchMedia("(prefers-reduced-motion: reduce)");return t.addEventListener("change",e),()=>t.removeEventListener("change",e)}e.s(["usePersistentResourceState",0,function(e,s,a=o){let l=(0,i.useResourceRuntime)(),[c,u]=(0,t.useState)(e.reset),[d,f]=(0,t.useState)(!1),p=(0,t.useRef)(!1),m=JSON.stringify(a),h=(0,t.useRef)(s);return(0,t.useEffect)(()=>{h.current=s},[s]),(0,t.useEffect)(()=>{let t=!1;return l.progress.load(l.identity).then(async r=>{for(let e of JSON.parse(m)){if(r||t)break;let i=function(e,t){let r="number"==typeof t?t:t?.stateSchemaVersion,i="number"==typeof t?e.resourceVersion:t?.resourceVersion;return!Number.isInteger(r)||r<1||r>e.stateSchemaVersion||"string"!=typeof i||!n.test(i)||r===e.stateSchemaVersion&&("number"==typeof t||!function(e,t){if(!n.test(e)||!n.test(t))return!1;let r=e.split(".").map(Number),i=t.split(".").map(Number),o=r.findIndex((e,t)=>e!==i[t]);return o>=0&&r[o]<i[o]}(i,e.resourceVersion))?null:{...e,resourceVersion:i,stateSchemaVersion:r}}(l.identity,e);i&&(r=await l.progress.load(i))}if(!r||t)return;let i=e.restore(r,l);if("restored"===i.status){let e=h.current;u(e?e(i.state):i.state)}}).catch(()=>{}).finally(()=>{t||(p.current=!0,f(!0))}),()=>{t=!0}},[l,e,m]),(0,t.useEffect)(()=>{if(!p.current)return;let t=window.setTimeout(()=>{(0,r.saveResourceProgress)(l,e.serialize(c,l))},300);return()=>window.clearTimeout(t)},[l,e,c]),{state:c,setState:u,runtimeReady:d}},"usePrefersReducedMotion",0,function(){return(0,t.useSyncExternalStore)(l,a,()=>!1)},"useResourceState",0,function(e){let[r,n]=(0,t.useState)(e);return{state:r,setState:n,runtimeReady:(0,t.useSyncExternalStore)(s,()=>!0,()=>!1)}}],719818)}]);