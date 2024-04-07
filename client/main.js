import * as THREE from 'three'
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader';
import { OrbitControls} from 'three/examples/jsm/controls/OrbitControls';

const scene = new THREE.Scene();

const camera = new THREE.PerspectiveCamera(75, window/innerWidth / window.innerHeight, .1, 1000);

loader.load(
  'CLT-Hackathon-Spring-2024\models\coffeeshop.gltf',
  function(gltf) {
      scene.add(gltf.scene);
  },
  function(xhr) {
      console.log((xhr.loaded / xhr.total * 100) + '% loaded');
  },
  function(error) {
      console.error('An error happened', error);
  }
);

const renderer = new THREE.WebGLRenderer({alpha: true});
renderer.setSize(window.innerWidth, window.innerHeight);c

document.getElementById("container3D").appendChild(renderer.domElement);

const topLight = new THREE.DirectionalLight(0xffffff, 1);
topLight.position.set(500, 500, 500);
topLight.castShadow = true;
scene.add(topLight);

const ambientLight = new THREE.AmbientLight(0x333333, 3);
scene.add(ambientLight);

function animate(){
  requestAnimationFrame(animate);
  controls.update();

  renderer.render(scene, camera);

}

const controls = new OrbitControls(camera, renderer.domElement);