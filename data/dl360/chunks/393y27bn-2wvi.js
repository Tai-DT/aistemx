(globalThis.TURBOPACK||(globalThis.TURBOPACK=[])).push(["object"==typeof document?document.currentScript:void 0,867809,347739,e=>{"use strict";var t=e.i(843476),r=e.i(271645),i=e.i(270950),i=i,a=e.i(190072),s=e.i(94800);function o(e){let t=(0,r.useRef)(null);return(0,s.useFrame)(()=>{if(t.current)for(let[r,i]of Object.entries(e))t.current.uniforms[r].value=i.value}),t}let l=`
  varying vec2 vUv; varying vec3 vNormal; varying vec3 vWorld;
  void main(){
    vUv=uv; vec4 world=modelMatrix*vec4(position,1.);
    vNormal=normalize(mat3(modelMatrix)*normal); vWorld=world.xyz;
    gl_Position=projectionMatrix*viewMatrix*world;
  }`,n=`
  uniform sampler2D surfaceMap, normalMap, specularMap, nightMap, cloudMap;
  uniform bool earthDetail, ringShadow; uniform sampler2D ringMap;
  uniform vec3 lightDirection, ringAxis; uniform float opacity;
  varying vec2 vUv; varying vec3 vNormal; varying vec3 vWorld;
  // Derivative tangent frame keeps normal mapping aligned with the rotating UVs.
  vec3 mappedNormal(vec3 n){
    vec3 q1=dFdx(vWorld), q2=dFdy(vWorld);
    vec2 st1=dFdx(vUv), st2=dFdy(vUv);
    vec3 t=normalize(q1*st2.y-q2*st1.y);
    vec3 b=normalize(-q1*st2.x+q2*st1.x);
    vec3 mapN=texture2D(normalMap,vUv).xyz*2.-1.;
    mapN.xy*=.34;
    return normalize(mat3(t,b,n)*mapN);
  }
  void main(){
    vec3 geometric=normalize(vNormal), light=normalize(lightDirection);
    float mu=dot(geometric,light);
    vec3 n=earthDetail?mappedNormal(geometric):geometric;
    vec3 albedo=texture2D(surfaceMap,vUv).rgb;
    float diffuse=max(mu,0.)*(1.+clamp(dot(n,light)-mu,-.12,.12));
    // Continuous cosine falloff: no constant brightness step at the terminator.
    // Small illustrative fill preserves legibility, without moving the boundary.
    float transmission=1.;
    if(ringShadow){
      // Sphere normal is its center-relative position in units of radius.
      // Trace toward the Sun and sample the same radial opacity as the ring.
      float angle=dot(light,ringAxis);
      if(abs(angle)>.0001){
        float t=-dot(geometric,ringAxis)/angle;
        float radial=length(geometric+light*t);
        if(t>0. && radial>1.28 && radial<2.3){
          float alpha=texture2D(ringMap,vec2((radial-1.28)/1.02,.5)).a;
          transmission=1.-alpha*.88;
        }
      }
    }
    vec3 color=albedo*(.012+diffuse*1.75*transmission);
    if(earthDetail){
      float ocean=texture2D(specularMap,vUv).r;
      float cloud=texture2D(cloudMap,vUv).r;
      vec3 halfVector=normalize(light+normalize(cameraPosition-vWorld));
      float spec=pow(max(dot(n,halfVector),0.),72.)*ocean*max(mu,0.)*(1.-cloud);
      color+=vec3(1.,.94,.8)*spec*.7;
      vec3 cities=texture2D(nightMap,vUv).rgb;
      color+=cities*.95*(1.-smoothstep(-.12,.02,mu))*(1.-cloud*.92);
    }
    gl_FragColor=vec4(color,opacity);
    #include <tonemapping_fragment>
    #include <colorspace_fragment>
  }`;function u(e,t=[]){let s=(0,i.G)(a.TextureLoader,e),o=t.join(","),l=(0,r.useMemo)(()=>s.map((e,t)=>{let r=e.clone();return r.colorSpace=o.split(",").includes(String(t))?a.NoColorSpace:a.SRGBColorSpace,r.anisotropy=8,r.needsUpdate=!0,r}),[s,o]);return(0,r.useEffect)(()=>()=>l.forEach(e=>e.dispose()),[l]),l}let h=`
  uniform sampler2D cloudMap; uniform vec3 lightDirection;
  varying vec2 vUv; varying vec3 vNormal; varying vec3 vWorld;
  void main(){
    float cloud=texture2D(cloudMap,vUv).r;
    float mu=max(dot(normalize(vNormal),normalize(lightDirection)),0.);
    gl_FragColor=vec4(vec3(.015+mu*1.8),cloud*.86);
    #include <tonemapping_fragment>
    #include <colorspace_fragment>
  }`,d=`
  uniform vec3 glowColor, lightDirection; varying vec3 vNormal; varying vec3 vWorld;
  void main(){
    vec3 normal=normalize(vNormal);
    float rim=pow(1.-abs(dot(normal,normalize(cameraPosition-vWorld))),3.5);
    float daylight=smoothstep(-.15,.45,dot(normal,normalize(lightDirection)));
    gl_FragColor=vec4(glowColor,rim*daylight*.45);
    #include <colorspace_fragment>
  }`,c=`
  varying vec2 vUv; varying vec3 vNormal; varying vec3 vLocal;
  void main(){
    vUv=uv; vLocal=position;
    vNormal=normalize(mat3(modelMatrix)*normal);
    gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.);
  }`,f=`
  uniform sampler2D ringMap; uniform vec3 localLight, lightDirection; uniform float radius, opacity;
  varying vec2 vUv; varying vec3 vNormal; varying vec3 vLocal;
  void main(){
    vec4 ring=texture2D(ringMap,vUv);
    vec3 point=vLocal/radius, ray=normalize(localLight);
    float toward=-dot(point,ray);
    float closest=length(point+ray*max(toward,0.));
    // Ray / sphere shadow, in ring-local coordinates. The ring follows the pole.
    float shadow=toward>0.?smoothstep(.97,1.03,closest):1.;
    float lit=.055+( .32+.8*abs(dot(normalize(vNormal),normalize(lightDirection))) )*shadow;
    gl_FragColor=vec4(ring.rgb*lit,ring.a*opacity);
    #include <tonemapping_fragment>
    #include <colorspace_fragment>
  }`;e.s(["Atmosphere",0,function({radius:e,color:i,light:s}){let o=(0,r.useMemo)(()=>({glowColor:{value:new a.Color(i)},lightDirection:{value:s}}),[i,s]);return(0,t.jsxs)("mesh",{raycast:()=>{},children:[(0,t.jsx)("sphereGeometry",{args:[1.025*e,64,48]}),(0,t.jsx)("shaderMaterial",{vertexShader:l,fragmentShader:d,uniforms:o,transparent:!0,blending:a.AdditiveBlending,depthWrite:!1})]})},"EarthClouds",0,function({url:e,radius:i,light:a}){let s=u([e],[0]),o=(0,r.useMemo)(()=>({cloudMap:{value:s[0]},lightDirection:{value:a}}),[s,a]);return(0,t.jsxs)("mesh",{raycast:()=>{},children:[(0,t.jsx)("sphereGeometry",{args:[1.008*i,64,48]}),(0,t.jsx)("shaderMaterial",{vertexShader:l,fragmentShader:h,uniforms:o,transparent:!0,depthWrite:!1})]})},"PlanetSurface",0,function({url:e,light:i,earthAssets:a,ringAssets:s,ringAxis:h,opacity:d}){let c=o({opacity:d}),f=u(a?[e,a["earth-normal"],a["earth-specular"],a["earth-night"],a["earth-clouds"]]:s?[e,s["saturn-ring"]]:[e],a?[1,2,4]:[]),m=(0,r.useMemo)(()=>({surfaceMap:{value:f[0]},normalMap:{value:f[1]??f[0]},specularMap:{value:f[2]??f[0]},nightMap:{value:f[3]??f[0]},cloudMap:{value:f[4]??f[0]},earthDetail:{value:!!a},ringShadow:{value:!!s},ringMap:{value:f[1]??f[0]},ringAxis:{value:h},lightDirection:{value:i},opacity:d}),[f,a,s,h,i,d]);return(0,t.jsx)("shaderMaterial",{ref:c,vertexShader:l,fragmentShader:n,uniforms:m,transparent:!0})},"SaturnRing",0,function({radius:e,light:i,localLight:s,url:l,opacity:n}){let h=o({opacity:n}),d=u([l]),m=(0,r.useMemo)(()=>{let t=new a.RingGeometry(1.28*e,2.3*e,256),r=t.attributes.position,i=t.attributes.uv;for(let t=0;t<r.count;t++)i.setXY(t,(Math.hypot(r.getX(t),r.getY(t))/e-1.28)/1.02,.5);return t},[e]);(0,r.useEffect)(()=>()=>m.dispose(),[m]);let p=(0,r.useMemo)(()=>({ringMap:{value:d[0]},lightDirection:{value:i},localLight:{value:s},radius:{value:e},opacity:n}),[d,i,s,e,n]);return(0,t.jsx)("mesh",{rotation:[-Math.PI/2,0,0],geometry:m,raycast:()=>{},children:(0,t.jsx)("shaderMaterial",{ref:h,vertexShader:c,fragmentShader:f,uniforms:p,transparent:!0,side:a.DoubleSide,depthWrite:!1})})},"planetVertex",0,l,"useSolarTextures",0,u],867809);var m=e.i(20840),p=e.i(560099),v=e.i(848546);let g={name:"CopyShader",uniforms:{tDiffuse:{value:null},opacity:{value:1}},vertexShader:`

		varying vec2 vUv;

		void main() {

			vUv = uv;
			gl_Position = projectionMatrix * modelViewMatrix * vec4( position, 1.0 );

		}`,fragmentShader:`

		uniform float opacity;

		uniform sampler2D tDiffuse;

		varying vec2 vUv;

		void main() {

			vec4 texel = texture2D( tDiffuse, vUv );
			gl_FragColor = opacity * texel;


		}`};var x=a;class M{constructor(){this.isPass=!0,this.enabled=!0,this.needsSwap=!0,this.clear=!1,this.renderToScreen=!1}setSize(){}render(){console.error("THREE.Pass: .render() must be implemented in derived pass.")}dispose(){}}let b=new x.OrthographicCamera(-1,1,1,-1,0,1);class _ extends x.BufferGeometry{constructor(){super(),this.setAttribute("position",new x.Float32BufferAttribute([-1,3,0,-1,-1,0,3,-1,0],3)),this.setAttribute("uv",new x.Float32BufferAttribute([0,2,0,0,2,0],2))}}let T=new _;class C{constructor(e){this._mesh=new x.Mesh(T,e)}dispose(){this._mesh.geometry.dispose()}render(e){e.render(this._mesh,b)}get material(){return this._mesh.material}set material(e){this._mesh.material=e}}class S extends M{constructor(e,t="tDiffuse"){super(),this.textureID=t,this.uniforms=null,this.material=null,e instanceof a.ShaderMaterial?(this.uniforms=e.uniforms,this.material=e):e&&(this.uniforms=a.UniformsUtils.clone(e.uniforms),this.material=new a.ShaderMaterial({name:void 0!==e.name?e.name:"unspecified",defines:Object.assign({},e.defines),uniforms:this.uniforms,vertexShader:e.vertexShader,fragmentShader:e.fragmentShader})),this._fsQuad=new C(this.material)}render(e,t,r){this.uniforms[this.textureID]&&(this.uniforms[this.textureID].value=r.texture),this._fsQuad.material=this.material,this.renderToScreen?e.setRenderTarget(null):(e.setRenderTarget(t),this.clear&&e.clear(e.autoClearColor,e.autoClearDepth,e.autoClearStencil)),this._fsQuad.render(e)}dispose(){this.material.dispose(),this._fsQuad.dispose()}}class w extends M{constructor(e,t){super(),this.scene=e,this.camera=t,this.clear=!0,this.needsSwap=!1,this.inverse=!1}render(e,t,r){let i,a,s=e.getContext(),o=e.state;o.buffers.color.setMask(!1),o.buffers.depth.setMask(!1),o.buffers.color.setLocked(!0),o.buffers.depth.setLocked(!0),this.inverse?(i=0,a=1):(i=1,a=0),o.buffers.stencil.setTest(!0),o.buffers.stencil.setOp(s.REPLACE,s.REPLACE,s.REPLACE),o.buffers.stencil.setFunc(s.ALWAYS,i,0xffffffff),o.buffers.stencil.setClear(a),o.buffers.stencil.setLocked(!0),e.setRenderTarget(r),this.clear&&e.clear(),e.render(this.scene,this.camera),e.setRenderTarget(t),this.clear&&e.clear(),e.render(this.scene,this.camera),o.buffers.color.setLocked(!1),o.buffers.depth.setLocked(!1),o.buffers.color.setMask(!0),o.buffers.depth.setMask(!0),o.buffers.stencil.setLocked(!1),o.buffers.stencil.setFunc(s.EQUAL,1,0xffffffff),o.buffers.stencil.setOp(s.KEEP,s.KEEP,s.KEEP),o.buffers.stencil.setLocked(!0)}}class y extends M{constructor(){super(),this.needsSwap=!1}render(e){e.state.buffers.stencil.setLocked(!1),e.state.buffers.stencil.setTest(!1)}}class U{constructor(e,t){if(this.renderer=e,this._pixelRatio=e.getPixelRatio(),void 0===t){const r=e.getSize(new a.Vector2);this._width=r.width,this._height=r.height,(t=new a.WebGLRenderTarget(this._width*this._pixelRatio,this._height*this._pixelRatio,{type:a.HalfFloatType})).texture.name="EffectComposer.rt1"}else this._width=t.width,this._height=t.height;this.renderTarget1=t,this.renderTarget2=t.clone(),this.renderTarget2.texture.name="EffectComposer.rt2",this.writeBuffer=this.renderTarget1,this.readBuffer=this.renderTarget2,this.renderToScreen=!0,this.passes=[],this.copyPass=new S(g),this.copyPass.material.blending=a.NoBlending,this.timer=new a.Timer}swapBuffers(){let e=this.readBuffer;this.readBuffer=this.writeBuffer,this.writeBuffer=e}addPass(e){this.passes.push(e),e.setSize(this._width*this._pixelRatio,this._height*this._pixelRatio)}insertPass(e,t){this.passes.splice(t,0,e),e.setSize(this._width*this._pixelRatio,this._height*this._pixelRatio)}removePass(e){let t=this.passes.indexOf(e);-1!==t&&this.passes.splice(t,1)}isLastEnabledPass(e){for(let t=e+1;t<this.passes.length;t++)if(this.passes[t].enabled)return!1;return!0}render(e){this.timer.update(),void 0===e&&(e=this.timer.getDelta());let t=this.renderer.getRenderTarget(),r=!1;for(let t=0,i=this.passes.length;t<i;t++){let i=this.passes[t];if(!1!==i.enabled){if(i.renderToScreen=this.renderToScreen&&this.isLastEnabledPass(t),i.render(this.renderer,this.writeBuffer,this.readBuffer,e,r),i.needsSwap){if(r){let t=this.renderer.getContext(),r=this.renderer.state.buffers.stencil;r.setFunc(t.NOTEQUAL,1,0xffffffff),this.copyPass.render(this.renderer,this.writeBuffer,this.readBuffer,e),r.setFunc(t.EQUAL,1,0xffffffff)}this.swapBuffers()}void 0!==w&&(i instanceof w?r=!0:i instanceof y&&(r=!1))}}this.renderer.setRenderTarget(t)}reset(e){if(void 0===e){let t=this.renderer.getSize(new a.Vector2);this._pixelRatio=this.renderer.getPixelRatio(),this._width=t.width,this._height=t.height,(e=this.renderTarget1.clone()).setSize(this._width*this._pixelRatio,this._height*this._pixelRatio)}this.renderTarget1.dispose(),this.renderTarget2.dispose(),this.renderTarget1=e,this.renderTarget2=e.clone(),this.writeBuffer=this.renderTarget1,this.readBuffer=this.renderTarget2}setSize(e,t){this._width=e,this._height=t;let r=this._width*this._pixelRatio,i=this._height*this._pixelRatio;this.renderTarget1.setSize(r,i),this.renderTarget2.setSize(r,i);for(let e=0;e<this.passes.length;e++)this.passes[e].setSize(r,i)}setPixelRatio(e){this._pixelRatio=e,this.setSize(this._width,this._height)}dispose(){this.renderTarget1.dispose(),this.renderTarget2.dispose(),this.copyPass.dispose()}}class P extends M{constructor(e,t,r=null,i=null,s=null){super(),this.scene=e,this.camera=t,this.overrideMaterial=r,this.clearColor=i,this.clearAlpha=s,this.clear=!0,this.clearDepth=!1,this.needsSwap=!1,this.isRenderPass=!0,this._oldClearColor=new a.Color}render(e,t,r){let i,a,s=e.autoClear;e.autoClear=!1,null!==this.overrideMaterial&&(a=this.scene.overrideMaterial,this.scene.overrideMaterial=this.overrideMaterial),null!==this.clearColor&&(e.getClearColor(this._oldClearColor),e.setClearColor(this.clearColor,e.getClearAlpha())),null!==this.clearAlpha&&(i=e.getClearAlpha(),e.setClearAlpha(this.clearAlpha)),!0==this.clearDepth&&e.clearDepth(),e.setRenderTarget(this.renderToScreen?null:r),!0===this.clear&&e.clear(e.autoClearColor,e.autoClearDepth,e.autoClearStencil),e.render(this.scene,this.camera),null!==this.clearColor&&e.setClearColor(this._oldClearColor),null!==this.clearAlpha&&e.setClearAlpha(i),null!==this.overrideMaterial&&(this.scene.overrideMaterial=a),e.autoClear=s}}let R={name:"LuminosityHighPassShader",uniforms:{tDiffuse:{value:null},luminosityThreshold:{value:1},smoothWidth:{value:1},defaultColor:{value:new a.Color(0)},defaultOpacity:{value:0}},vertexShader:`

		varying vec2 vUv;

		void main() {

			vUv = uv;

			gl_Position = projectionMatrix * modelViewMatrix * vec4( position, 1.0 );

		}`,fragmentShader:`

		uniform sampler2D tDiffuse;
		uniform vec3 defaultColor;
		uniform float defaultOpacity;
		uniform float luminosityThreshold;
		uniform float smoothWidth;

		varying vec2 vUv;

		void main() {

			vec4 texel = texture2D( tDiffuse, vUv );

			float v = luminance( texel.xyz );

			vec4 outputColor = vec4( defaultColor.rgb, defaultOpacity );

			float alpha = smoothstep( luminosityThreshold, luminosityThreshold + smoothWidth, v );

			gl_FragColor = mix( outputColor, texel, alpha );

		}`};class D extends M{constructor(e,t=1,r,i){super(),this.strength=t,this.radius=r,this.threshold=i,this.resolution=void 0!==e?new a.Vector2(e.x,e.y):new a.Vector2(256,256),this.clearColor=new a.Color(0,0,0),this.needsSwap=!1,this.renderTargetsHorizontal=[],this.renderTargetsVertical=[],this.nMips=5;let s=Math.round(this.resolution.x/2),o=Math.round(this.resolution.y/2);this.renderTargetBright=new a.WebGLRenderTarget(s,o,{type:a.HalfFloatType}),this.renderTargetBright.texture.name="UnrealBloomPass.bright",this.renderTargetBright.texture.generateMipmaps=!1;for(let e=0;e<this.nMips;e++){const t=new a.WebGLRenderTarget(s,o,{type:a.HalfFloatType});t.texture.name="UnrealBloomPass.h"+e,t.texture.generateMipmaps=!1,this.renderTargetsHorizontal.push(t);const r=new a.WebGLRenderTarget(s,o,{type:a.HalfFloatType});r.texture.name="UnrealBloomPass.v"+e,r.texture.generateMipmaps=!1,this.renderTargetsVertical.push(r),s=Math.round(s/2),o=Math.round(o/2)}this.highPassUniforms=a.UniformsUtils.clone(R.uniforms),this.highPassUniforms.luminosityThreshold.value=i,this.highPassUniforms.smoothWidth.value=.01,this.materialHighPassFilter=new a.ShaderMaterial({uniforms:this.highPassUniforms,vertexShader:R.vertexShader,fragmentShader:R.fragmentShader}),this.separableBlurMaterials=[];const l=[6,10,14,18,22];s=Math.round(this.resolution.x/2),o=Math.round(this.resolution.y/2);for(let e=0;e<this.nMips;e++)this.separableBlurMaterials.push(this._getSeparableBlurMaterial(l[e])),this.separableBlurMaterials[e].uniforms.invSize.value=new a.Vector2(1/s,1/o),s=Math.round(s/2),o=Math.round(o/2);this.compositeMaterial=this._getCompositeMaterial(this.nMips),this.compositeMaterial.uniforms.blurTexture1.value=this.renderTargetsVertical[0].texture,this.compositeMaterial.uniforms.blurTexture2.value=this.renderTargetsVertical[1].texture,this.compositeMaterial.uniforms.blurTexture3.value=this.renderTargetsVertical[2].texture,this.compositeMaterial.uniforms.blurTexture4.value=this.renderTargetsVertical[3].texture,this.compositeMaterial.uniforms.blurTexture5.value=this.renderTargetsVertical[4].texture,this.compositeMaterial.uniforms.bloomStrength.value=t,this.compositeMaterial.uniforms.bloomRadius.value=.1,this.compositeMaterial.uniforms.bloomFactors.value=[1,.8,.6,.4,.2],this.bloomTintColors=[new a.Vector3(1,1,1),new a.Vector3(1,1,1),new a.Vector3(1,1,1),new a.Vector3(1,1,1),new a.Vector3(1,1,1)],this.compositeMaterial.uniforms.bloomTintColors.value=this.bloomTintColors,this.copyUniforms=a.UniformsUtils.clone(g.uniforms),this.blendMaterial=new a.ShaderMaterial({uniforms:this.copyUniforms,vertexShader:g.vertexShader,fragmentShader:g.fragmentShader,premultipliedAlpha:!0,blending:a.AdditiveBlending,depthTest:!1,depthWrite:!1,transparent:!0}),this._oldClearColor=new a.Color,this._oldClearAlpha=1,this._basic=new a.MeshBasicMaterial,this._fsQuad=new C(null)}dispose(){for(let e=0;e<this.renderTargetsHorizontal.length;e++)this.renderTargetsHorizontal[e].dispose();for(let e=0;e<this.renderTargetsVertical.length;e++)this.renderTargetsVertical[e].dispose();this.renderTargetBright.dispose();for(let e=0;e<this.separableBlurMaterials.length;e++)this.separableBlurMaterials[e].dispose();this.compositeMaterial.dispose(),this.blendMaterial.dispose(),this._basic.dispose(),this._fsQuad.dispose()}setSize(e,t){let r=Math.round(e/2),i=Math.round(t/2);this.renderTargetBright.setSize(r,i);for(let e=0;e<this.nMips;e++)this.renderTargetsHorizontal[e].setSize(r,i),this.renderTargetsVertical[e].setSize(r,i),this.separableBlurMaterials[e].uniforms.invSize.value=new a.Vector2(1/r,1/i),r=Math.round(r/2),i=Math.round(i/2)}render(e,t,r,i,a){e.getClearColor(this._oldClearColor),this._oldClearAlpha=e.getClearAlpha();let s=e.autoClear;e.autoClear=!1,e.setClearColor(this.clearColor,0),a&&e.state.buffers.stencil.setTest(!1),this.renderToScreen&&(this._fsQuad.material=this._basic,this._basic.map=r.texture,e.setRenderTarget(null),e.clear(),this._fsQuad.render(e)),this.highPassUniforms.tDiffuse.value=r.texture,this.highPassUniforms.luminosityThreshold.value=this.threshold,this._fsQuad.material=this.materialHighPassFilter,e.setRenderTarget(this.renderTargetBright),e.clear(),this._fsQuad.render(e);let o=this.renderTargetBright;for(let t=0;t<this.nMips;t++)this._fsQuad.material=this.separableBlurMaterials[t],this.separableBlurMaterials[t].uniforms.colorTexture.value=o.texture,this.separableBlurMaterials[t].uniforms.direction.value=D.BlurDirectionX,e.setRenderTarget(this.renderTargetsHorizontal[t]),e.clear(),this._fsQuad.render(e),this.separableBlurMaterials[t].uniforms.colorTexture.value=this.renderTargetsHorizontal[t].texture,this.separableBlurMaterials[t].uniforms.direction.value=D.BlurDirectionY,e.setRenderTarget(this.renderTargetsVertical[t]),e.clear(),this._fsQuad.render(e),o=this.renderTargetsVertical[t];this._fsQuad.material=this.compositeMaterial,this.compositeMaterial.uniforms.bloomStrength.value=this.strength,this.compositeMaterial.uniforms.bloomRadius.value=this.radius,this.compositeMaterial.uniforms.bloomTintColors.value=this.bloomTintColors,e.setRenderTarget(this.renderTargetsHorizontal[0]),e.clear(),this._fsQuad.render(e),this._fsQuad.material=this.blendMaterial,this.copyUniforms.tDiffuse.value=this.renderTargetsHorizontal[0].texture,a&&e.state.buffers.stencil.setTest(!0),this.renderToScreen?e.setRenderTarget(null):e.setRenderTarget(r),this._fsQuad.render(e),e.setClearColor(this._oldClearColor,this._oldClearAlpha),e.autoClear=s}_getSeparableBlurMaterial(e){let t=[],r=e/3;for(let i=0;i<e;i++)t.push(.39894*Math.exp(-.5*i*i/(r*r))/r);return new a.ShaderMaterial({defines:{KERNEL_RADIUS:e},uniforms:{colorTexture:{value:null},invSize:{value:new a.Vector2(.5,.5)},direction:{value:new a.Vector2(.5,.5)},gaussianCoefficients:{value:t}},vertexShader:`

				varying vec2 vUv;

				void main() {

					vUv = uv;
					gl_Position = projectionMatrix * modelViewMatrix * vec4( position, 1.0 );

				}`,fragmentShader:`

				#include <common>

				varying vec2 vUv;

				uniform sampler2D colorTexture;
				uniform vec2 invSize;
				uniform vec2 direction;
				uniform float gaussianCoefficients[KERNEL_RADIUS];

				void main() {

					float weightSum = gaussianCoefficients[0];
					vec3 diffuseSum = texture2D( colorTexture, vUv ).rgb * weightSum;

					for ( int i = 1; i < KERNEL_RADIUS; i ++ ) {

						float x = float( i );
						float w = gaussianCoefficients[i];
						vec2 uvOffset = direction * invSize * x;
						vec3 sample1 = texture2D( colorTexture, vUv + uvOffset ).rgb;
						vec3 sample2 = texture2D( colorTexture, vUv - uvOffset ).rgb;
						diffuseSum += ( sample1 + sample2 ) * w;

					}

					gl_FragColor = vec4( diffuseSum, 1.0 );

				}`})}_getCompositeMaterial(e){return new a.ShaderMaterial({defines:{NUM_MIPS:e},uniforms:{blurTexture1:{value:null},blurTexture2:{value:null},blurTexture3:{value:null},blurTexture4:{value:null},blurTexture5:{value:null},bloomStrength:{value:1},bloomFactors:{value:null},bloomTintColors:{value:null},bloomRadius:{value:0}},vertexShader:`

				varying vec2 vUv;

				void main() {

					vUv = uv;
					gl_Position = projectionMatrix * modelViewMatrix * vec4( position, 1.0 );

				}`,fragmentShader:`

				varying vec2 vUv;

				uniform sampler2D blurTexture1;
				uniform sampler2D blurTexture2;
				uniform sampler2D blurTexture3;
				uniform sampler2D blurTexture4;
				uniform sampler2D blurTexture5;
				uniform float bloomStrength;
				uniform float bloomRadius;
				uniform float bloomFactors[NUM_MIPS];
				uniform vec3 bloomTintColors[NUM_MIPS];

				float lerpBloomFactor( const in float factor ) {

					float mirrorFactor = 1.2 - factor;
					return mix( factor, mirrorFactor, bloomRadius );

				}

				void main() {

					// 3.0 for backwards compatibility with previous alpha-based intensity
					vec3 bloom = 3.0 * bloomStrength * (
						lerpBloomFactor( bloomFactors[ 0 ] ) * bloomTintColors[ 0 ] * texture2D( blurTexture1, vUv ).rgb +
						lerpBloomFactor( bloomFactors[ 1 ] ) * bloomTintColors[ 1 ] * texture2D( blurTexture2, vUv ).rgb +
						lerpBloomFactor( bloomFactors[ 2 ] ) * bloomTintColors[ 2 ] * texture2D( blurTexture3, vUv ).rgb +
						lerpBloomFactor( bloomFactors[ 3 ] ) * bloomTintColors[ 3 ] * texture2D( blurTexture4, vUv ).rgb +
						lerpBloomFactor( bloomFactors[ 4 ] ) * bloomTintColors[ 4 ] * texture2D( blurTexture5, vUv ).rgb
					);

					float bloomAlpha = max( bloom.r, max( bloom.g, bloom.b ) );
					gl_FragColor = vec4( bloom, bloomAlpha );

				}`})}}D.BlurDirectionX=new a.Vector2(1,0),D.BlurDirectionY=new a.Vector2(0,1);let A={name:"OutputShader",uniforms:{tDiffuse:{value:null},toneMappingExposure:{value:1}},vertexShader:`
		precision highp float;

		uniform mat4 modelViewMatrix;
		uniform mat4 projectionMatrix;

		attribute vec3 position;
		attribute vec2 uv;

		varying vec2 vUv;

		void main() {

			vUv = uv;
			gl_Position = projectionMatrix * modelViewMatrix * vec4( position, 1.0 );

		}`,fragmentShader:`

		precision highp float;

		uniform sampler2D tDiffuse;

		#include <tonemapping_pars_fragment>
		#include <colorspace_pars_fragment>

		varying vec2 vUv;

		void main() {

			gl_FragColor = texture2D( tDiffuse, vUv );

			// tone mapping

			#ifdef LINEAR_TONE_MAPPING

				gl_FragColor.rgb = LinearToneMapping( gl_FragColor.rgb );

			#elif defined( REINHARD_TONE_MAPPING )

				gl_FragColor.rgb = ReinhardToneMapping( gl_FragColor.rgb );

			#elif defined( CINEON_TONE_MAPPING )

				gl_FragColor.rgb = CineonToneMapping( gl_FragColor.rgb );

			#elif defined( ACES_FILMIC_TONE_MAPPING )

				gl_FragColor.rgb = ACESFilmicToneMapping( gl_FragColor.rgb );

			#elif defined( AGX_TONE_MAPPING )

				gl_FragColor.rgb = AgXToneMapping( gl_FragColor.rgb );

			#elif defined( NEUTRAL_TONE_MAPPING )

				gl_FragColor.rgb = NeutralToneMapping( gl_FragColor.rgb );

			#elif defined( CUSTOM_TONE_MAPPING )

				gl_FragColor.rgb = CustomToneMapping( gl_FragColor.rgb );

			#endif

			// color space

			#ifdef SRGB_TRANSFER

				gl_FragColor = sRGBTransferOETF( gl_FragColor );

			#endif

		}`};class F extends M{constructor(){super(),this.isOutputPass=!0,this.uniforms=a.UniformsUtils.clone(A.uniforms),this.material=new a.RawShaderMaterial({name:A.name,uniforms:this.uniforms,vertexShader:A.vertexShader,fragmentShader:A.fragmentShader}),this._fsQuad=new C(this.material),this._outputColorSpace=null,this._toneMapping=null}render(e,t,r){this.uniforms.tDiffuse.value=r.texture,this.uniforms.toneMappingExposure.value=e.toneMappingExposure,(this._outputColorSpace!==e.outputColorSpace||this._toneMapping!==e.toneMapping)&&(this._outputColorSpace=e.outputColorSpace,this._toneMapping=e.toneMapping,this.material.defines={},a.ColorManagement.getTransfer(this._outputColorSpace)===a.SRGBTransfer&&(this.material.defines.SRGB_TRANSFER=""),this._toneMapping===a.LinearToneMapping?this.material.defines.LINEAR_TONE_MAPPING="":this._toneMapping===a.ReinhardToneMapping?this.material.defines.REINHARD_TONE_MAPPING="":this._toneMapping===a.CineonToneMapping?this.material.defines.CINEON_TONE_MAPPING="":this._toneMapping===a.ACESFilmicToneMapping?this.material.defines.ACES_FILMIC_TONE_MAPPING="":this._toneMapping===a.AgXToneMapping?this.material.defines.AGX_TONE_MAPPING="":this._toneMapping===a.NeutralToneMapping?this.material.defines.NEUTRAL_TONE_MAPPING="":this._toneMapping===a.CustomToneMapping&&(this.material.defines.CUSTOM_TONE_MAPPING=""),this.material.needsUpdate=!0),!0===this.renderToScreen?e.setRenderTarget(null):(e.setRenderTarget(t),this.clear&&e.clear(e.autoClearColor,e.autoClearDepth,e.autoClearStencil)),this._fsQuad.render(e)}dispose(){this.material.dispose(),this._fsQuad.dispose()}}function B({url:e,time:i}){let a=o({time:i}),s=u([e]),l=(0,r.useMemo)(()=>({surfaceMap:{value:s[0]},time:i}),[s,i]);return(0,t.jsx)("shaderMaterial",{ref:a,toneMapped:!1,uniforms:l,vertexShader:"varying vec2 vUv; void main(){vUv=uv;gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.);}",fragmentShader:`uniform sampler2D surfaceMap; uniform float time; varying vec2 vUv;
      void main(){
        vec2 flow=vec2(sin(vUv.y*44.+time*.22),cos(vUv.x*57.-time*.18))*.0015;
        vec3 surface=texture2D(surfaceMap,vUv+flow).rgb;
        float filaments=.95+.05*sin(vUv.x*90.+sin(vUv.y*70.)+time*.38);
        gl_FragColor=vec4(surface*vec3(3.4,2.55,1.7)*filaments,1.);
        #include <colorspace_fragment>
      }`})}e.s(["SolarBloom",0,function({enabled:e}){let{gl:t,scene:i,camera:o,size:l,viewport:n}=(0,v.useThree)(),u=(0,r.useMemo)(()=>{if(!e)return null;let r=new a.WebGLRenderTarget(1,1,{type:a.HalfFloatType,samples:Math.min(4,t.capabilities.maxSamples)}),s=new U(t,r),l=new P(i,o),n=new D(new a.Vector2(1,1),.48,.55,1.8),u=new F;return s.addPass(l),s.addPass(n),s.addPass(u),{composer:s,render:l,bloom:n,output:u}},[e,t,i,o]);return(0,r.useEffect)(()=>{u&&(u.composer.setPixelRatio(n.dpr),u.composer.setSize(l.width,l.height))},[u,n.dpr,l.width,l.height]),(0,r.useEffect)(()=>()=>{u?.composer.dispose(),u?.bloom.dispose(),u?.output.dispose()},[u]),(0,s.useFrame)((e,r)=>{u?u.composer.render(r):t.render(i,o)},1),null},"Stars",0,function(){let e=(0,v.useThree)(e=>e.viewport.dpr),i=(0,r.useMemo)(()=>({pixelRatio:{value:e}}),[e]),s=(0,r.useMemo)(()=>(function(){let e=new Float32Array(6e3),t=new Float32Array(6e3),r=new Float32Array(2e3),i=7321,s=()=>(i=1664525*i+0x3c6ef35f>>>0)/0x100000000;for(let i=0;i<2e3;i++){let a=2*s()-1,o=s()*Math.PI*2;e.set([Math.sqrt(1-a*a)*Math.cos(o)*92,92*a,Math.sqrt(1-a*a)*Math.sin(o)*92],3*i);let l=.28+.7*Math.pow(s(),5),n=s()>.85;t.set([l*(n?1:.76),.85*l,l*(n?.7:1)],3*i),r[i]=1.1+2.2*Math.pow(s(),8)}let o=new a.BufferGeometry;return o.setAttribute("position",new a.BufferAttribute(e,3)),o.setAttribute("color",new a.BufferAttribute(t,3)),o.setAttribute("size",new a.BufferAttribute(r,1)),o})(),[]);return(0,r.useEffect)(()=>()=>s.dispose(),[s]),(0,t.jsx)("points",{geometry:s,raycast:()=>{},children:(0,t.jsx)("shaderMaterial",{uniforms:i,transparent:!0,depthWrite:!1,vertexColors:!0,vertexShader:`attribute float size; uniform float pixelRatio; varying vec3 vColor;
      void main(){vColor=color; vec3 direction=position+cameraPosition; gl_Position=projectionMatrix*viewMatrix*vec4(direction,1.); gl_PointSize=size*pixelRatio;}`,fragmentShader:"varying vec3 vColor; void main(){float a=1.-smoothstep(.05,.5,length(gl_PointCoord-.5)); gl_FragColor=vec4(vColor,a);}"})})},"Sun",0,function({url:e,radius:i,clock:l,reducedMotion:n,positionMarker:u,rotationDays:h}){let d=(0,r.useRef)(null),c=(0,r.useMemo)(()=>({time:{value:0}}),[]),f=o(c);return(0,s.useFrame)(({gl:e},t)=>{d.current&&h&&(d.current.rotation.y=2*Math.PI*(l.current.days%h)/h),l.current.playing&&!n&&"hidden"!==document.visibilityState&&(c.time.value+=Math.min(t,.1)),e.domElement.dataset.solarEffectTime=c.time.value.toFixed(4)},-.5),(0,t.jsxs)("group",{scale:i/1.25,children:[u&&(0,t.jsx)(p.Html,{center:!0,zIndexRange:[9,0],style:{pointerEvents:"none"},children:(0,t.jsx)("span",{"aria-hidden":"true",className:"block size-1.5 rounded-full bg-amber-100 shadow-[0_0_10px_3px_#ffb34280]"})}),(0,t.jsx)("group",{rotation:h?[0,0,-7.25*Math.PI/180]:void 0,children:(0,t.jsxs)("mesh",{ref:d,children:[(0,t.jsx)("sphereGeometry",{args:[1.25,64,48]}),(0,t.jsx)(r.Suspense,{fallback:(0,t.jsx)("meshBasicMaterial",{color:"#fff1b8"}),children:(0,t.jsx)(B,{url:e,time:c.time})})]})}),(0,t.jsx)(m.Billboard,{children:(0,t.jsxs)("mesh",{raycast:()=>{},children:[(0,t.jsx)("planeGeometry",{args:[9,9]}),(0,t.jsx)("shaderMaterial",{ref:f,transparent:!0,depthWrite:!1,blending:a.AdditiveBlending,uniforms:c,vertexShader:"varying vec2 vUv; void main(){vUv=uv;gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.);}",fragmentShader:`varying vec2 vUv; uniform float time;
        void main(){
          vec2 p=vUv-.5; float r=length(p)*2.; float angle=atan(p.y,p.x);
          float glow=exp(-r*7.)*.85;
          float corona=exp(-max(r-.265,0.)*18.)*smoothstep(.24,.3,r);
          float stream=sin(angle*13.+sin(angle*5.-time*.13)-r*20.+time*.65);
          float fine=sin(angle*29.+r*9.-time*.22);
          float rays=.78+.17*stream+.08*fine;
          float outward=pow(max(0.,stream),4.)*exp(-max(r-.27,0.)*10.)*smoothstep(.27,.34,r);
          gl_FragColor=vec4(1.,.53,.17,(glow+corona*.34*rays+outward*.10)*(1.-smoothstep(.7,1.,r)));
        }`})]})})]})}],347739)}]);