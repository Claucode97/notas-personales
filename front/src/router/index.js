import { createRouter, createWebHistory } from 'vue-router'


const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/pages/home/HomePage.vue'),
  },
  {
    path: '/notes',
    name: 'Notes',
    component: () => import('@/pages/notes/Notes.vue'),
  },

  {
    path: '/notes/:id',
    name: 'NoteDetail',
    component: () => import('@/pages/noteDetail/NoteDetail.vue'),
  },
  {
    path: '/notes/add',
    name: 'AddNote',
    component: () => import('@/pages/add/AddNote.vue'),
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
