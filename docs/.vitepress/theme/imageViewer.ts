export function setupImageViewer() {
  let overlay: HTMLDivElement | null = null

  const close = () => {
    overlay?.remove()
    overlay = null
    document.documentElement.classList.remove('img-viewer-open')
  }

  const open = (src: string, alt: string) => {
    close()
    overlay = document.createElement('div')
    overlay.className = 'img-viewer'

    const img = document.createElement('img')
    img.src = src
    img.alt = alt

    overlay.appendChild(img)
    overlay.addEventListener('click', close) // click ra ngoài hoặc vào ảnh đều đóng
    document.body.appendChild(overlay)
    document.documentElement.classList.add('img-viewer-open')
  }

  document.addEventListener('click', (e) => {
    const target = e.target
    if (
      target instanceof HTMLImageElement &&
      target.closest('.vp-doc') &&   // chỉ ảnh trong nội dung markdown
      !target.closest('a')           // bỏ qua ảnh nằm trong link (badge, logo...)
    ) {
      open(target.currentSrc || target.src, target.alt)
    }
  })

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') close()
  })
}