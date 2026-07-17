<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn5.telesco.pe/file/i5kruk9pXJTOKeHAEy3brOdrH8Ko6UcvZYbY0nh2Xe4PZM17ji6NGz-NGR16jvEwAF2qFqK9fxkuYy7gFHjlN23TPdwdXckqFB-kMsl4yIZqlzuo1tn32cApPLsUK4jyCMM96UxQycpHOtmV0CI0EWHIo6ksNrfL7jrqLWgaFvuSTx0O8vqOka9bw4hB58HIKsknftNO3ph-T-rtDPzvoouKgi4gAlEoouX61kmXm-K07uZy6YBXK2CG-gKRdgOjzrMbm9Gp3J3Az1wXvafUkoUouBpJk8yaAv4U-K8N-jVy_lwD7A20K5ppOsjkX1uM-62FzTR3sPDp7i0A9VAp2g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 567K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 09:43:41</div>
<hr>

<div class="tg-post" id="msg-100594">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4324684be2.mp4?token=I7B4XZxlyobh0KpMs8Qugo6A1srBHnPx8hBjp-igkNuGj-9u8qHHwbneIZIsNLfe9TMfysfJQcD64FZ2m9IUZh7lchXEMEo_Lp8Ma8l80aWTxaIpZCA40IVBQIoOAWK2PvmlY4EuVUAg6yjSgmJTUAMJhvnbnqeRGfKfVEucViYGPZeVVn863f5mH-LzM10glUbgayKffzKVj2qBdGI-3fl8YAttLQyxYZVvHSkAOAmkIT9ey6SfB40xQX9Rr5FnsKeNfVFiQ6WhNy35RMRFN4hIXPrLZ-YECOElLNuHeoXsX_YfHtHZFQYWRPnRookOIalH97jR9Hd-R1LOd-D1ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4324684be2.mp4?token=I7B4XZxlyobh0KpMs8Qugo6A1srBHnPx8hBjp-igkNuGj-9u8qHHwbneIZIsNLfe9TMfysfJQcD64FZ2m9IUZh7lchXEMEo_Lp8Ma8l80aWTxaIpZCA40IVBQIoOAWK2PvmlY4EuVUAg6yjSgmJTUAMJhvnbnqeRGfKfVEucViYGPZeVVn863f5mH-LzM10glUbgayKffzKVj2qBdGI-3fl8YAttLQyxYZVvHSkAOAmkIT9ey6SfB40xQX9Rr5FnsKeNfVFiQ6WhNy35RMRFN4hIXPrLZ-YECOElLNuHeoXsX_YfHtHZFQYWRPnRookOIalH97jR9Hd-R1LOd-D1ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🙂
تمسخر مجری شبکه ورزش توسط ابوطالب و سوژه شدن آن در رسانه‌ها.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/Futball180TV/100594" target="_blank">📅 09:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100589">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a6e4da4f4.mp4?token=Pg7zIaCO1IDI_r0gti8aw7_uHL8GhU43V9E4LgsVnNxnEzKuZ2k0qMMOAOYO7CRVqSfJEu8xLFHs1Z9rk_LTtnadwQGG6B4GN8cMvzqoNXY_STt6K6Lu-f6dnSdVLIxoth3ZnpaFTnflS_MeJYgTF8LlT9XM0laH6tqIKum8yQZSRzV9dUjK31k70R4-upeoEKSXEhOotjAj2C2inluzDCl-SGr46n7jcDAkspYWsI9FSi8CgtoVHo-wxiaBCMheEZglaRPLayJK0NnbHJCH4iI9KPKDgIDq-mT5YLFWVg9BKgsNDuXYjfbijemklybhmwmReeEz4-XOYmOuZZ1Y_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a6e4da4f4.mp4?token=Pg7zIaCO1IDI_r0gti8aw7_uHL8GhU43V9E4LgsVnNxnEzKuZ2k0qMMOAOYO7CRVqSfJEu8xLFHs1Z9rk_LTtnadwQGG6B4GN8cMvzqoNXY_STt6K6Lu-f6dnSdVLIxoth3ZnpaFTnflS_MeJYgTF8LlT9XM0laH6tqIKum8yQZSRzV9dUjK31k70R4-upeoEKSXEhOotjAj2C2inluzDCl-SGr46n7jcDAkspYWsI9FSi8CgtoVHo-wxiaBCMheEZglaRPLayJK0NnbHJCH4iI9KPKDgIDq-mT5YLFWVg9BKgsNDuXYjfbijemklybhmwmReeEz4-XOYmOuZZ1Y_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
خاطره بامزه خسرو حیدری از فتح‌الله‌زاده: روزی سه با گوشیشو میشوره
😂
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/Futball180TV/100589" target="_blank">📅 09:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100588">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84d54514e4.mp4?token=jVpQoonrLRj6NUz5L0Aktj1aumoT7-F7xOSVmskuZE1CyA8Pnn-3TnUOWwCQGFGJChRX_vI63V96DutjN7rM80boAEl2PxvXw1UkC_juTBGxpHpYymWmxdHR6y9-ZvOpmNVGchgL7w-N_QnsoDMGijLGiQp9cfXMWqCxZISzY5EQKl2yKJPthV3fNSTkx1Kao3wl7KOcLlZjf-BoeVUA8QgVHq7Ou6NQfYIX-Mxspp0i0rPZV_VEaw9XHwWEd6ELrUuMwX7r6jTO-xDAHSiWTGNBeH8PPXW-MwQj3WwYSyL17kIeZESwrmnk8Ef9pMq-icVSflGtLRvYaKuH5xn5ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84d54514e4.mp4?token=jVpQoonrLRj6NUz5L0Aktj1aumoT7-F7xOSVmskuZE1CyA8Pnn-3TnUOWwCQGFGJChRX_vI63V96DutjN7rM80boAEl2PxvXw1UkC_juTBGxpHpYymWmxdHR6y9-ZvOpmNVGchgL7w-N_QnsoDMGijLGiQp9cfXMWqCxZISzY5EQKl2yKJPthV3fNSTkx1Kao3wl7KOcLlZjf-BoeVUA8QgVHq7Ou6NQfYIX-Mxspp0i0rPZV_VEaw9XHwWEd6ELrUuMwX7r6jTO-xDAHSiWTGNBeH8PPXW-MwQj3WwYSyL17kIeZESwrmnk8Ef9pMq-icVSflGtLRvYaKuH5xn5ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🎙
علی دایی در دفاع از مهدوی‌کیا: با او چه کردیم که با دلش ملی بیاید؟ مگر او را دعوت کردید؟ انسان‌ها با ارزش‌هایشان بزرگ می‌شوند، نه با مجسمه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/Futball180TV/100588" target="_blank">📅 09:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100587">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlyUUapLM3BCxH2QzkbBlzsSUtdIesNflqfPS9O7a71dIjiZIbFZ9YC-tLgPegJ1B9eXCRqJZJNZ0oW3AKa4SSeilncRQj2dwon40TDTo-Zc_hcJk6YKpvQBmz19lRBQuKjjYQC6JbicAfgKs2zdKHfpyOTnKK-qZi4Jnm7_HF6AGjJx_FZK8tu9nOGgeyE0qV-RSFr2Uof9ASPPRSiHkuaB3Un0Gn6CX-8CTjhU9Uyfih8zK57OGfHOa-zu8ujIeQ2VRqmtF-sPvFsICW9CFNvOCwtSz8HYpP97W_71KAwhhHT0d36sYJty8IM3PU73JPQZDidK8M3ZHge9xaYZRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🚨
فیفا اعلام کرد که برای اولین بار در تاریخ جام جهانی، "نشان‌های قهرمانی" به همراه جام و مدال‌های طلا اهدا خواهند شد، مشابه آنچه در NBA انجام می‌شود.
🔻
2026 عدد نشان قهرمانی تولید خواهد شد. تیم قهرمان جام جهانی 30 عدد از این نشان‌ها را دریافت می‌کنند، در حالی که 1996 نشان باقی‌مانده برای فروش به هواداران در سراسر جهان عرضه خواهد شد.
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/Futball180TV/100587" target="_blank">📅 08:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100586">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfeWX4p-gozdJXxAUSEmIMN19aPflw0oXgsNuD734Egr-JCMec2_yY7mSnAiM4YNXX3qmXgPBDMTSDeACm0ZfWCyizI6_mrgokK0QUiavLoNl-UccUt39WVmkkWQ8kIPrKJoRucL7J7V1_dx5Cra5Vl9uuI3719-xJ5HLQT2mgoZkBGGOFcLZNzzy2innkctZCDwkGCF9Ex_5iWfC1Pp3s0TjRZCnB6fwynvZz1pbhzHBCaQpgTtf-a8nydaIfOc0eKxf3ouq9obo_xyPJRoL3x8LcRzrOyk_RK-jbFp_cfRZt9VVGgxX_lTHoA9iKGoKuCdh2SJUs05N89z8tIGFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#رسمی؛ با اعلام فیفا داورایی از کشورهای اسلوونی و ونزوئلایی برای قضاوت فینال جام جهانی بین آرژانتین و اسپانیا و دیدار رده بندی بین انگلیس و فرانسه انتخاب شدن و حضور فغانی تو این ۲ بازی عملا کنسل شد..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/100586" target="_blank">📅 05:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100584">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MNSIXIkBEnA_ZavuMhHkljJmz-9bsGkW54iZ7wGDh6CNQoZCnQu509gSo5Zqqpe8di0XX2bYqHn8q4S8DjntCOrvqlwnU5zB80f69TFFlYZUSNwNg575vdMXvdZMfMCAzSv0ZHBi2829VNYxfank8uPLHtxlq46dIm59HicXyhAfrGl-yxTn5JcsJJGea17HZ-0BES7m3izAfKJ2e7TKJgb5hrLlZMr0hFWKNOXwL7WZCoOzUeUXDm11tUbl2qETik1zLwEewZon5Bo7QpxoNQGeO1KXCeiaLZVyQdRfOAJZUiILBowmuMTuYZ_3RE0WWEK5UrTJdiZcTeela1jx-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O0fUgZUekPUBx0LpJP5GtETZ0nYnAc7dY9DPZUmmK1J2Xz8qF5Q9cdm-DM3pETTjX4JLKLcNOXkZ54Ce8WmwdcEBtwnElH-VHPzxgq50s7gWupgZ8br0hNy7cRwIro2HTUumuonlb-W0fO2hR0aa3M0eWO3SfPTG_Lw99nI2jgLoLqbI94zG6hBJPYmpiMhMdv5G3yMd7r0Zo3PYS4MgJjqRxfCGFaxcllw0wuFzei18VwVPUqa0Ge4N7FFlJuZ1xQWixuD-3t1J8-FT-w6WuQH9N9NVFbIEw_uuwHEsO3Cju0CDwh3gJBUhx7I0-j9GcK6GpCsp0sOfzuvLk8dkQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
لحظاتی پیش در پی حملات آمریکا، برج کنترل دریایی ۸۰ متری چابهار بطور کامل فرو ریخت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/100584" target="_blank">📅 05:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100582">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V9QwjrFScVlaS27inPbVt22iuRrbj1O6DvDAQPuZN4ixgIKmlWTYEMuiKJFdooDJ2C19529e1QRN770mIhE2mQ84JlNPJZaeZBPUP684d_6ErOla6qigsXkGPvfjKT6px-6KSXZ4jouazMt6TKUDABcfFcwqDojng5-YzfDn_I_MzhPBD5ilMZUM4QLWY8bmH5cRFm0r06yYRA6Kq4-B9nmm3aVLCFHkHtI_81Qf7R052Afcytg4965BjfUSWDi9femgdil3MlCpPq2QfFS116J-tpR5mOFAg2sK9Vwz0U0sw7L1-radw-YilMbbTOFogNb_727vWjFlSdW4V8e9Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hTjqE9gu0RvbZhGiN47T5kVBbNfonIBd8h4jUDS1z6tgFVYNZWAggIGvUGrZ1_V-0rCx9uWRhGJb904L7fwlYlq9VT-q0DkNR_Mn_LL8s5MUZS2fnbLvZXJf9BiswwelB_T3Na-vqbXCWULyPAg4eaHAiaI8lXGNnYI-oOJzrGFgrmtPLewA6qGS83dJtE3Mwu5wFLG2_GjqwAp5i0l6PklsGtSE61banLFJbDS4_iOvYfvQvwTkOIyYEjMeVg8cmgZ8Z0SeLj4HGd6-y02iNQ62tiD6wM4l4kbJSAgaELRKBV6n_gb71COMMDELUkosvnowm9JSamHaiRCMggKUPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
#رسمی
؛
با اعلام فیفا داورایی از کشورهای اسلوونی و ونزوئلایی برای قضاوت فینال جام جهانی بین آرژانتین و اسپانیا و دیدار رده بندی بین انگلیس و فرانسه انتخاب شدن و حضور فغانی تو این ۲ بازی عملا کنسل شد..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/100582" target="_blank">📅 05:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100581">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sReM6vs0vMVzuEXLa-BUNfDef2BfXJRXS3pl2mmlq78LoCTkXs47mLmQphLza-m3sLccJ4HdAG62DkQC0VbGSI1wQBMVCXx1tdMjfVMmo0iq1OIBxoAz4gXLI103Zlgj1Bd2K2tg2h0ahhRaUV-J5RMVtmXW6jAiyaZ5WSn-oxSfxh3cK4Axb09F6aiVXp7LcfhTel01gDMi8eSBuR4761BYf-InnW0sHhHLG38NJ_amfDjtaV0kbTRe2hUTNvu_OPoJgj2dRvizO0M0fnKkokc5pSx3GIUFc8vaFG2gkAH9pzoqge8Y_x1UETPqbziv07vr4a7Nsg-3cOlx-DLQaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاپورتا: اگر داوری در فینال عادلانه باشد، اسپانیا 100٪ پیروز خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/100581" target="_blank">📅 05:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100580">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qt9G_Mc2CNYc-f936Sh8NWx-OKXtRL25CFgtWwOqjvaMUpEO5HpAzk7HUNIJ6ZcLTJB2gX9rkp_gM2YPJ3K51FXRtjAa5n4s2VG_JE4zKJ7oYvA-Dng23uI3InkVxzbtru0bSW1PWkmhdRgBwn2OdAlFIyI3wwgxBLSz5ijoZrUer0S3ZxLH1aWFqMcn8RZGawYf-XlZFPJcb1I2KOKnARG3-hFNgPyHckC_JqtaZ1-_3NUGIDlsPmHUHgj15Kw5FJ024VuO9x1aBAxWjjHeu7Cow9voQDOSyphhwkW3We6qHCAjRrWud7LCz5jy8AFU4i0xNQvM80PWHgRnaca-mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
پپ گواردیولا:
یکی از بزرگترین پشیمونیام توی دوران مربیگریم اینه که نتونستم توی دوران اوج نیمار توی بارسلونا سرمربیش باشم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/100580" target="_blank">📅 02:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100579">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOc7-eov9vUNX3-xHzqZgPNZZrx2OtCMvAr8Tqu3xl-pTXCMmYf5DokqiH_XpTc2H5pBA65MGh6Iso-1mM374JzVDei_O1Osexr8CSVah1qhrZO_tptAa6EIkKUGluVT5I_rrTnuL7yu4tb2QGx_5-F3N6-Ah1N-1WJN7jpX23eF3CeOWyGtwLnHOpEMkBTFu6mQ8CPANsWUpb34ofB_nD_qGF7mS6Hsf2XuG-3O-56YQlgOpDzKTtAQb2E65u8VBJlZv5jd5FTR2q_iLfCtYeAoRCWhsTBNV81WipNlJOzlJtQFWFV5d5Q1jLARjseCtNrUzZzLkJ41eLORTXoItg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
🔻
مارکا:
مصر درخواست میزبانی سوپرجام اسپانیا در سال 2027 را ارائه کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/100579" target="_blank">📅 02:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100578">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🎙
🇪🇸
خوان لاپورتا:
- ما یک پیشنهاد ارائه دادیم و اکنون تصمیم با باشگاه اتلتیکو است.
- بازیکن(آلوارز) اعلام کرده که می‌خواهد جدا شود، اما پیشنهاد ما تا ابد باز نیست.
- در صورت تغییر موضع باشگاه اتلتیکو، ما یک مهلت نهایی تعیین خواهیم کرد.
- ما یک پیشنهاد بسیار خوب ارائه دادیم.
- این بازیکنی است که فلیک و دکو می‌خواهند.
- اما اگر این انتقال انجام نشود، باید روی گزینه‌های جایگزین دیگری کار کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/100578" target="_blank">📅 02:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100577">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7THh4Mt5nBHx6-NTYgmFVde_GCF2T2EzzwhWkv2TnLNFr42JtodaPNmnEI2iNB1lqF-_oUFHxelr4TEM6bLZbZkuFNd3GrHojB0mO-YHqtvdtunGlhsniS1JlrrmLkLSA7zWERxAwTsMJrONpgivMKpfwLPQPCi-meP971_KAwx4L9dPyZSGrDj_IcxsMDGR-48IoBhE86UDeSX2B09zKL6kzOG9hGhafGHxxl82t72rWXJzg85_-jJgnvkWP1nxxNCjnSLixo1y5UTdoMEogttq92ydijGOrDCXAi0fVIRD8InWNPBi0xwOJkdQotSJ-UkOPDw8z7bIc1KNhniEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولیسه کیه بابا.
همون همیشگیو بیارید بایرنیا یکم حالشون خوب بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/100577" target="_blank">📅 02:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100576">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/100576" target="_blank">📅 02:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100575">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OJPqS3oCa7z0HYT2hKJFw6cZBslen1RLfuh1D1V3cjl-NxndDnns8oPW5TUONzhrtxcBJz_BmlbbHovoaPeMTxDM3Qs2tBdOCLA5Kag2yvAR-1lPK7LHWh-j_HmqoGEZsEuIrlp37VgOxwzHd7ObhbFio3Smpd1VmNTx37VMxLcrK5Bt8rtDStjjhMQG_CqgXsC9DzFm1sqiTGxoaCILpUiiKEwZUsb1-70eUUWjVrjmZL0qm1l9Ncf1Sg1nxdJF6Qi-HB-zasvI-6QpizwXg9FObKc8xu-h4qzi1oUTFLL4NFWEOswIp-kGgyIJoWntb3siPQI_vDR-0KhJAXGdxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/100575" target="_blank">📅 02:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100574">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
‼️
لکیپ: مدیران بایرن‌مونیخ از طریق اوپامکانو درخواست تمدید قرارداد به اولیسه ارائه کردن اما این بازیکن رد کرده و گفته فقط میخوام به رئال‌مادرید برم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/100574" target="_blank">📅 01:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100573">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_6mjRkZJveE7tolEx4-iuhIMwrrIR0-WtkbrQwjCZN2RUKlbu5F1p0XB3bH8PpNdvxIpXmrYuwL4sbs1bfsMukzqfMFTBkdVtIWhgmwAwdk9NXfr7Pwjkm9KGyVbQ_KxVDTEpXLsmympi3Jnv4qI0oCU7o9kQExLkcV7pDVM6a5Aq155HL4MVadZLW13IJE1RfvQkfe7GwGH-JJLedu4bsj9yhuhZGBbQC57dCSM1PbgB3WoGMfJSqQe5Iq2hBro3W1l765Hi8cY1o37uQgQPmitmen_nbzIiBuKNT7C0bMIDgn5dzYgH0hpkxVenIbUDFJIsRgLuYBby8w5pKeIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇩🇪
🇪🇸
لکیپ‌فرانسه: برخلاف صحبت منابع خبری آلمان، اولیسه شدیدا دلش رئال‌مادرید رو میخواد و پرز بعد جام‌جهانی با پیشنهادی دیوانه وار برای جذب این بازیکن اقدام میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/100573" target="_blank">📅 01:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100572">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bw1-ZdbH_yAb6wges4SHC4QtBcCexTiecU-Ox5M5u1qITdGki-0pz5_Oi8YXchEkvGB8TCRjeH_QCdA6MDD_peeJ354rRPl1e0SKJH-2LVnC4FR0GBwfMY9WyTF5SktrEXRjybQgh6NrduFsetN4nUFhlBBQ3kCsi2ayM1XIIhRcM-Xwrjca0ko0leKH2qdg44wfgApSFpi9ujxBOl5JSEUBMpNPV9dTZ4F6T8z8md2pkL90yj4X5mW-7ZLRth_y35iKEGvQ4O924DeKZBOWWV1vQyxP1OLYMnro2z5aM7MSVD-JZXAxVVZiRTphi4tCLSSOGrRlmx9ZeUNh9LrnDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇩🇪
🇪🇸
لکیپ‌فرانسه: برخلاف صحبت منابع خبری آلمان، اولیسه شدیدا دلش رئال‌مادرید رو میخواد و پرز بعد جام‌جهانی با پیشنهادی دیوانه وار برای جذب این بازیکن اقدام میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/100572" target="_blank">📅 00:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100571">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrssHWxFPMPhe2vK0kjeKDs7PA7uca3UtdJ1Pc_TVV3-YKHjaBvER1YET_-48hKkb5dEkTXnmSCMQ4uDYAcj2cz__PtV4Gq_wy65GgPC-bDjzVs4wkHTHPnW7AOQLuc_rNx2Sdwhb1UlIZtnn_pt3ThrBqoE-LA_X-cIt2TJW-BZC7o2sdpxYJgYLJjBOGRPsuU__IFWtEKu1kzKmRGPAaerbsyG44Zn2YUYSXrfAtcCMrj_Ja7XCaETBqdo3-IxC8e-P1eI9ZpYKnKes2y5BGCdm-OuYBZ4djMgwPqVoqjcnvHOUkoSANtWDIFyg7QdtqaEPTno1Jq1v9eSJr9v1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
رسانه‌های آمریکایی: مطابق صحبت‌های رئیس جمهور ترامپ، حملات به زیرساخت‌ها شروع شده
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/100571" target="_blank">📅 00:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100570">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHBGfT_DzJcSsSdx5oPmw6P_zvEMsT7JJj3Hy1Xv6Pid-6x9Frb7MIkF5H8qytVu31dNa2u3hNt82YiUnFRx0x6eu5sMqaOnKkjkwyyGTcBhT5O-KqTH_MWzoVm_oOmZ9XyzzknXjuW6JkUyeTaUwrq0ughM78vBt6VbJDTvz7O9kOwAgtZ1RlAvNR3Tehmz9g_xAutLzj5aLINyy6UPhoDuvSnxjPxHKd8mKRwa7FE4KpgWl_MHWieHUZ_I1wYwC80_lXXH3gDmu404MSBPj9gmDXwyCZkPURFch5EUIGpKnVV61Kb-uXNO3aErqjgKbIZg6-D_0f8sTucPbLJSqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ویدیو دیگر از پل مسیر شهر لار به بندرعباس که کاملا تخریب شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/100570" target="_blank">📅 00:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100569">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/orSRCvQqnajs81FWFIeuOVhTeVCUBABA3Dnc9AUHlbz3jBmVu-GzKXbfMgkw0e_QuCB2ndQX8B6l1MbksS_wQO0lQ9jLwJdKS-AQPwT5G1U6eqknO6Bsc95hDbgWIt5B4LLcN_RHuacvrhzimxqMCBOeVl3_6B-yBeBJtFL_imk2j1zZJwj4k2dYdCv2VAGnPTokOhH1A1ZeixOGmS8lYQwWCQl4HNkz8jrp8SaZNNJpTPE-WX9IoRTkf30K6kLE5EcB_G5hbkLJm6BBhoANkMto6DjknrDJMWg0vwEi-DZV_ypLNLxfY5b33JO5G9W-k836PDMsDHQ18IYhjH6KRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تمامی پل هایی که بندر خمیر را به بندرعباس متصل می کرد توسط ارتش آمریکا مورد اصابت قرار گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/100569" target="_blank">📅 00:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100568">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
⭕️
ایستگاه راه‌آهن بندرعباس بمباران شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/100568" target="_blank">📅 00:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100567">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Afg6oO-ovq317_tQTOo0HxO0ggUX-lRgpM0yRmrc0WM13OZuX3D6hDfRDh5LG8vuEeWCzw0OR5UaWr5x5ly4XOyUxmPSMeAT5k-o9cYHiOxpX_OAB7x60yLW3jYxbDF14ogWhScxsY-Y4sk6R18pMXL656qR6e_1Be3ipOR4PLs4BDdC3sXHuNj6wgFe2B0Wr63WzB9SAGimMCbaL5V89OOW6gMk08U6I5OxsDpdVwOh9qJCe0s8ZyULqG2_H5roQfl4d7DRqXGAwOlHL4UA3XNu8VLhst_6mW4hWAdPUQ5wVzH7QQ62uqFfo5NPRUe4idQNVoxHhWHCxCgG0GiC7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، تو فینال جام جهانی 2026 حضور داره و شخصاً جام رو به کاپیتان تیم برنده اهدا میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/100567" target="_blank">📅 00:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100566">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMLrZ9MjbmGQ5Uw12JZF48FwGQHToWaBKn8pAZmwLN7BwJ4-rJnc07jLdIdGhqrrq5cM1YScmnNz5AyMwyrZasakkH83Wq9mS-2WjZPDHU5a8uRvdhRr-QvyvV42GUAm7vwt-pSojVDKkH4RUkgnigS_4kopyP3QQ8Q-fkqfiFBZfHAHdFslOxj9RsPmAn_kdKx_ShrL7Ijie1-5vPYa4vDjK2bcRzLU5PSEn1lyN7kKXlc0VmjwHparvuMff2I6j1IxRSSDV69hLh5bDt14UVotkGOb3CACUdrbeT0PvYWax-MqMrqnn8t4s3kSCUvepLf3hUF_0Y3RhV5Asl9Vwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
محمد صلاح قصد دارد در این تابستان با باشگاه بشیکتاش‌ ترکیه  قرارداد امضا کند. صلاح درخواست دستمزد ۱۵ میلیون یورویی داشته است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/100566" target="_blank">📅 00:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100565">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
گزارشات حمله شدید به سیریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/100565" target="_blank">📅 00:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100564">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a4bc985b6e.mp4?token=Be68sHZEO3kY9b4FOeraWGvrcnmW5RNGawVCp64gDXk5HX4QdJhNJbZ90X1sBlW5X6NW0qZGa54imOmoEY02Ivs8aGdid63JORSxGlglaP4aDwN_6q0iCghIwmLGoC1hjtkUGNk2GjW2mdpRpgQao-WP2t04rT41SU7Fb_8XDtBeAD66fTIXYpyhsfGH2trzpv5xwhbKvo8bqXxcQ8VrA02Lrqlw9-yCW5V9lYJPZ1hsmAJfWphvpsqoAWusfwwx_WSPS8fxwbwiQ3VSzPYANqxA0QiaWyiYzwcOqepsjScSEGlvPga7tvNpBqOL-9YwXDbbqThfEFMRX7aIvul7aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a4bc985b6e.mp4?token=Be68sHZEO3kY9b4FOeraWGvrcnmW5RNGawVCp64gDXk5HX4QdJhNJbZ90X1sBlW5X6NW0qZGa54imOmoEY02Ivs8aGdid63JORSxGlglaP4aDwN_6q0iCghIwmLGoC1hjtkUGNk2GjW2mdpRpgQao-WP2t04rT41SU7Fb_8XDtBeAD66fTIXYpyhsfGH2trzpv5xwhbKvo8bqXxcQ8VrA02Lrqlw9-yCW5V9lYJPZ1hsmAJfWphvpsqoAWusfwwx_WSPS8fxwbwiQ3VSzPYANqxA0QiaWyiYzwcOqepsjScSEGlvPga7tvNpBqOL-9YwXDbbqThfEFMRX7aIvul7aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
صدای پرواز جنگنده‌ها در ایرانشهر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/100564" target="_blank">📅 00:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100563">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ویدیو دیگر از پل مسیر شهر لار به بندرعباس که کاملا تخریب شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/100563" target="_blank">📅 00:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100561">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/110e253ea3.mp4?token=s7KfgZb4ppJ6aQlCbrKRylYS8bDAX7Iw2xD_UirlHs9mGM5lU6T-O2ue9Cm9laWQoEOkmq9mlBe-1rRhCLuG9cYmQwzL8JsTYAEpzThtMc9aJuX0OkzkVd5MaSRMXz3BbTXRZV7a4JPse_JABs1KnVUPDkjw3HyBtVI5xYSixIQwvxwVtlV1d5XkS0Vv8vhNdIYKCtN8xC_Wayo0AGuWoO4js0WvMTwvuHStkJ3sKLWHe4QisVImR_lwoGaJJzOdC8x0tuGz1RMT_7CuTkHCPPKN9QhM18C2kJza1WHB8EgUYPfZgIIl70xxCJFJdejrl28H_4AyNqtnqyk2X3ERfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/110e253ea3.mp4?token=s7KfgZb4ppJ6aQlCbrKRylYS8bDAX7Iw2xD_UirlHs9mGM5lU6T-O2ue9Cm9laWQoEOkmq9mlBe-1rRhCLuG9cYmQwzL8JsTYAEpzThtMc9aJuX0OkzkVd5MaSRMXz3BbTXRZV7a4JPse_JABs1KnVUPDkjw3HyBtVI5xYSixIQwvxwVtlV1d5XkS0Vv8vhNdIYKCtN8xC_Wayo0AGuWoO4js0WvMTwvuHStkJ3sKLWHe4QisVImR_lwoGaJJzOdC8x0tuGz1RMT_7CuTkHCPPKN9QhM18C2kJza1WHB8EgUYPfZgIIl70xxCJFJdejrl28H_4AyNqtnqyk2X3ERfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ویدیو دیگر از پل مسیر شهر لار به بندرعباس که کاملا تخریب شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/100561" target="_blank">📅 23:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100560">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e073aa854.mp4?token=kC6G5jHPdTWIAAHcomh-KClPDSdb5G0sxPZE3NawBwlFOY7PEUwIAqVYSzGa7x0NbjqxU_W5C9f6PggYomIITHz09kWZrqhJs6kMx0Fi7oAy_3eYMEd2qQT7FLJt9jpfPRIc0FQ2R6lUQSuK81fZJHwwV9dwdEUFKtLfIK7xOpNlImN8L2LfDNRXcf7eIYWuLSpg3Oh6Wv9Kfds_BHa_LSIAy_pt_uwMtKPJaZfKQWiUMGpUzgR7IePRiIimAgZ6_O72C8Jf8vyq3Q-9wuSba57KSxQysqwurGo2ZD9PJhCiSL862YfQJysoXQmxq3oNbaezzkzx9ffnugSJp0MPJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e073aa854.mp4?token=kC6G5jHPdTWIAAHcomh-KClPDSdb5G0sxPZE3NawBwlFOY7PEUwIAqVYSzGa7x0NbjqxU_W5C9f6PggYomIITHz09kWZrqhJs6kMx0Fi7oAy_3eYMEd2qQT7FLJt9jpfPRIc0FQ2R6lUQSuK81fZJHwwV9dwdEUFKtLfIK7xOpNlImN8L2LfDNRXcf7eIYWuLSpg3Oh6Wv9Kfds_BHa_LSIAy_pt_uwMtKPJaZfKQWiUMGpUzgR7IePRiIimAgZ6_O72C8Jf8vyq3Q-9wuSba57KSxQysqwurGo2ZD9PJhCiSL862YfQJysoXQmxq3oNbaezzkzx9ffnugSJp0MPJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
پل استراتژیک که شیراز را به بندرعباس متصل میکرد و مسیر اصلی حمل و نقل مرکز کشور به بندرعباس بود، مورد حمله آمریکا قرار گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/100560" target="_blank">📅 23:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100559">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
تسنیم: شدت حملات در بندر عباس به قدری زیاد است که برق برخی مناطق بندر عباس قطع شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/100559" target="_blank">📅 23:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100558">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
تسنیم: شدت حملات در بندر عباس به قدری زیاد است که برق برخی مناطق بندر عباس قطع شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/100558" target="_blank">📅 23:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100557">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kouHaaLcN5VPMoIfu7PlsOJtCnsxhgtel3rAq30x_pnjrcuKj0tMgRJqAQ3tnerVQWH4awD5fZdr3JzjfNZhv0OJA4S53PERkp7zMsKN-SZFO05fuvo0qYJVBsvWNfep1gy_h0s-M5TFNp_ZIuiYPkpVWR_jjAmycAPRhM7aGsP8j3cveXY7x0hYCAuvpkRhGBaoJ3kcQs4fsTRI5e_f2IRWE4mGkPSVMjzMOXuarMqHMc9sCeA9KNMHVZXrA8URa3jlkLNA9z5x6PXhPw6L0y34FSGa9MKQrFtOMMyITF67B5lB3-2nx2c4e6RZdbrQnMFBwV6YOcxszaZTi8xqWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
گزارش برگ ریزون RMC SPORT:
ویلیام سالیبا درحالی برای فرانسه 7 بازی انجام داد که دچار شکستگی در ناحیه کمر بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/100557" target="_blank">📅 23:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100556">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OyfnjCviw0ZZTc9mD6mUPT1T_NIJ-Fx5MB6zYCu4CbvjlyQzTJ-okvJXrttH81ncwN9SlOFneteAYLDw6HaKc996VhrZe43wk1UBs30VFJNego9lH5ic9pppVzDtULJUsx9TNOfLpEJiypfwKP2BLpi2D3rZ5ehgdQAwcKacSsv1NsHH2mSxLwWivJB3bKNjlv2L9q-WcM5GuWK-5eWTNarDQ2uOEWCSqG2Lkfjeyp7jQM_XQy2ymmht78L19hiX2nA0AoxL5XbF1ZRantF6KymUsoqieYBT2xWHjYqXQvf-UCQEvy9n0OevQ2rlvJYeltOAbk25ZiJ7XLqnOtemCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🎙
انریکه سرایزو، رئیس باشگاه اتلتیکو مادرید:
خوان لاپورتا از قبل میداند که خولیان آلوارز در فصل آینده در کدام تیم بازی خواهد کرد.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/100556" target="_blank">📅 22:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100555">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e16fb64d04.mp4?token=trFcvpXnQqVvx3E4MgGNUys6SCZArV0cyeYHjhsx298jTA1s6a87SBBrZ1Cec-1lZ6V-MVxF4tHl8SZi-1EDEJr_8HdRihSJaqIQUy1jCgs4Ibs2OptkTydPd9EXb4hj5zSsmZ0t5yNT018bDkCQ8llFBLLux5aYRSGy4nzBQXUitRr9Up_YEq8S7udztOcgSxs37RrbYhvwXlgP4UfSSWAcHQWotBa34dDvCgJudyM9Ig0b6dIyE2X5k3ZpjToe_bNwWM2RfkCjBqTWfBLN5l4MoFMXNji2ImKR5SZN7ZveCYfWwgqQEAUSf3qDEXp8me8n5i1_JM5E1PS-bpvzOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e16fb64d04.mp4?token=trFcvpXnQqVvx3E4MgGNUys6SCZArV0cyeYHjhsx298jTA1s6a87SBBrZ1Cec-1lZ6V-MVxF4tHl8SZi-1EDEJr_8HdRihSJaqIQUy1jCgs4Ibs2OptkTydPd9EXb4hj5zSsmZ0t5yNT018bDkCQ8llFBLLux5aYRSGy4nzBQXUitRr9Up_YEq8S7udztOcgSxs37RrbYhvwXlgP4UfSSWAcHQWotBa34dDvCgJudyM9Ig0b6dIyE2X5k3ZpjToe_bNwWM2RfkCjBqTWfBLN5l4MoFMXNji2ImKR5SZN7ZveCYfWwgqQEAUSf3qDEXp8me8n5i1_JM5E1PS-bpvzOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسی و یامال تو فینال
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/100555" target="_blank">📅 22:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100554">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBwJ1MEjZYhqhfcVp8PuNAHGJR1dEyEAyRZxSwFPISdROtDhYUUg4aOo_8xn_5Qjh8ub_Wsq9GqSm7S9ik2royYQsKELF2ZuXBClW2qDijDxK2kQUfqZqBkZ8MrKM2WIXRRR6zZnQXeF1YSTDO3OaL-nDCHM8XU2nyC0IC9URy4DNTFvU-fWfLGuDBQ0Skztk3tbSf4Cmg7d_SEu_FDpT8B86vGRUCSF3WIfeYvjUJQy_UNw7RyuSt7E_Rppj_P_vh7PPnwlzYrOiOAI6kQ8HTuc7I9X6Mm-PE9T9QHtw8wEThiMpAugD21FzvZ6JyCxdS00VImTmHKn4ubXA53PIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
برترین گلزنان تاریخ تیم ملی آرژانتین.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/100554" target="_blank">📅 22:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100552">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dVjippR3xz38UbuX-HiFI2rh4NKtpKZesiaUAqyi_Mo-HpmWiAU1Py6jnM-R5D_K6_PXT789eAVHRERnPOSZ5odtLVGhMQR7DSgBT550NIcsBNcpfuf0bjw--wR4lJD2OTD17r_kw0vTrr_lBxY7dm-ZPWltl9ti6cNxwXeS5_uAlgp_-JgJ3hGKvPJzmgLZqeLNUuCzD9DeDNH26oSGXTIQPsvMAP0nCfmdw8IYiygBNXWt5L_PTuEzYM6NeXh22OFhMBVBtecFJwbs20i5zszahXqNKudkwb-MkcjVmYV6sE13pVsEspYZCdEi37tmo2D11M8GciSrSQsbEOsEUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IISK3AL1vEq_m3ynI2TJez0RAJ8GbYevJZDp1O7D1vcEuA-4vC_nAgRKdJL9EyKK7y07Qk63IJPVKEBbJrx5QQX35oR0E9b26zt6xyKNdQZaUS5KKiPxQvywuDdYEQpliWXjzQbfppBLQe0pF1hRGPrpZC6v5tzrR-b-OAGAQpy-IxulnusEiWyr7vFnMHGW68ECxijoxWyqpeUubVw6VleA4Trm1lXDsmhHdjj3vw67EBkkFnHcn3sGZNdiEgx8wFi1WxM7bOTtteWK5es6tJFLv05vvxF3R8CjLqTHMbO0opo5OTMTh0XQY6r8ayXqi8YBNFP2gvjOHkQpXkhqKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
تنها 2 بازیکن در جام جهانی 2026 بیش از 20 دریبل موفق ثبت کردن:
🔺
25 : لیونل مسی
🔺
22 : لامین یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/100552" target="_blank">📅 22:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100551">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFNHHt71RmAla-b2kc7o5AS3dpsGvuy2VD63ls3u60P0FsWcnDnjEB-C9_q_F7WcsXVx351Z8xyFiL4ceDPL2JJw9EjaNA6py0s8WGBWeYCvZdPumPA-UvmcOgCGAWFr8VxRAbMdRiUy9220fXhej84nb2Uvz4iTcJnQhQxtQHbQjbJuS5RQxL34lv1ieYZxrVPpw-mt6KKeAnSMCW3XAScq_DlmF6IGI03LCQzzp6FKkKtwk_mGXOTjTlg0E-Ok3VzGUJ2EB96YMZIAyNTp5laEg7UErr3KtdC_CwY3wPJQHmmy0L5QQnNykSikGciVwd3EnZdFRtp3qZ8pFRI-Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگه آنلاین‌شاپ‌ داری این خبر مخصوص خودته!
اگر فروشگاهت تو تلگرام، اینستاگرام یا بقیه‌ی شبکه‌های اجتماعی فعاله، حالا می‌تونی بدون نیاز به سایت درگاه پرداخت اسنپ‌پی را فعال کنی.
✨
امکان خرید ۴ قسطه برای مشتریات
✅
فعال‌سازی در کمتر از یک هفته
✅
افزایش اعتماد مشتری به پرداخت
✅
بدون نگرانی از فیش‌های واریزی نامعتبر
🔥
همین حالا ثبت‌نام کن ‌و درگاه پرداخت اسنپ‌پی رو به فروشگاهت اضافه کن:
👇🏻
https://l.snpy.ir/i1ekm</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/100551" target="_blank">📅 22:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100550">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eo7HIzFsCCxFQeRr_y5TRnVVjK_b6_wY4mtNmPCcGZE1bXHr19djJckv3CyK-3nIrEjqdLMg4igNO_DBws0SgR9XvMsm3Tdg9qZrb8LO4S8HJtLUBNOXKpmBe9EER3vX1akHNi6pOqQFduSy8YbHFAWfozSjE77JUrcyWvFMOoZJ7Ek064VuF0bh7WusloM6xydpA18v1ZVGSok4zxpe6YPqbh28QpbK5VAoFWfJc0UXb0BbpsaEIZc4bQHtRafdJURLjtrT6YB8Vw2dEgR1TxdadR3TK5iq-d8S9eybUquLqT0wk2er-1kN_j9a5ACXBW8bAUPGeWSqTqq_JazvcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فابریزیو رومانو:
فابیان رویز با پاری‌سن‌ژرمن برای تمدید ۲ ساله قراردادش به توافق رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/100550" target="_blank">📅 22:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100549">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGj5895lr25rK21mjYXds9LkYOuWuF05-c9COGBllDyfLif_X4jjWj5djHXFCyWs6Py0Bk3Yw-NthZYz-_yY1BIGGXp7z08oEvw1bw3FHacKqRSuXDUvegliTiRpBzoziUOEMZF-nqxsej6t2zxe4go-Q4e2gBcIlyCucMXh31iPdvt-8zuggj9ecdvv0a988FGY93vzDT4DZbjOnxrXNsWA62eCbvtWhdS7KHeqqCQIYsF0FwqOoOvk86b_L53MpQHiT8FmwGYDrEmBdg3VehjaKOnZ0QGnMry6_-cqTcbiZg0NYkWVtrp2n-PyXelgdap9a5tRhzzUj2QOhUixzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سنتکام: حملات ما به جنوب ایران شروع شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/100549" target="_blank">📅 21:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100544">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dQTiNbsGaK1joQfnMcGhtNUMnhKyDkEnlM35PEtcRE1DmJjMaMTg3krf87S05S8bRJj0Pe82BiKMWkvUTHg3vbbyVuPqpAsI2AbyvBez3YEYFDRxN2smAjEOu02PPrMgtvhP7SkCuOBVt73BuOvQ2P4e5lTzyOJfSoZCIghJ7GZdg3nJreJkU10xPsUEEehSUC9lui9CliNhrjgSXCXousX8SxouVX0vXKX5h9yiOG8CsqImhC2W0X5J7wsgBy-ODxlK6oGRA8qtN0LLNBvjgr5omBAB77KmtDU7QXFRRNEODYq_PyMGIHqPsr3MZ1QVa_jU8YWy8PfVcmge0xJ7mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SYYyOpwxqmD9XmOTvfcO8PibB_iBhR4n65Hes1ewXmry7vxvEsitZrr_Au5-h4PO1_esnJR1Tr3NE68pjj7ZU92X3F8RVg5NuvL-6Hdw6W0qEHQunkOYYWX-dfA5GcarPjFu5RG4nfz_sS8kGT5nWHtDyShYJzq7pZag2r4cpgSMHkNvI7_fZGyzBEexJ9YepXzAT362UjnHT2EpNhMk5soDn4OAUDq3PNXysq9R5wgs0fKjjKfABtqRDLSjx6hAMz0B9Ui6IfPTe4nyJLyWu3PzfqKJYuqMdkSpNk4dEPUJxWYE4CNgoctuBGIAnUrvqi8uTgGvvUeolCZha_32pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AZG1GpIP5yNp1ViB_UOUca9RwUMlexvOHP3d7gv1BUmXAWAfcLnVBT5r3Y2Lzk8HnidaMmmXbt8GMaWALB9L2suZTnPw37-9j19OAAkbI4nJtkQ3uLpuc3k4zaagCR0UmabPeqFrFQ8BKVkkjzuaPW6gketIbefre_-3c11BS-sA6WwB7VNhzNQUM17mUz0TscRhyqYkLKSa6fAuSMhfbAgC9kIsyjt-CZdKPbzzSxRCZ51C0U9qGQFiRU57NbN3yNj6T7t0Su5KEmgngAfJZi4WFAjZY8RWqxaxcGnq4ByLJss7h9kvn4My8DqkQPYzpAsRgbRvVX5i5Zv0d2SNjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KOgaJ9-WJHw1AlOTuvQoGMcj7YLvw3vy0fC7ectqr7xiEaDsJukNYeIjeYHdhoN3vO7K-QL_woI3DsTpjF58FbbMs-goWTB1Rto9PaiWsmpj5aHxtdAoGJw9FMZcbWXzxbquD4mvy1uYgX7vcvaiPjGBt_NJZEKljzsEREdZ6amJvCkdkAVOUk9d4j9ysl5eK6dU_9jxYPqtk21h5IBKU0p_4sJNM6BMzFvTRDj25hqR4yN66wh9NAspxgj7CiryuxvtAzjIUVRphMlOHuVMmjPMgFVRqyYdV8D8p8fmmDBNXEMHwPU2wdtk82fnDDKnCroZIwHcRtM266oWZDXtig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s7z1zp3UeMxFLufHIowzoRHOKuzJsnCM91oHWC4DCUVVffPBSGx7wm-g6TP2e87roqt9ns0ZYgtLn2t_tztJXWjx08B6UP4l0k4w_T1UlgL1mCeoYXRknrVa0H45H1COEQYAK3YSAiqKjQ-cxH_2bS2QAkWjiexLlFKjN285tMElOHwhcjSqnfXopV5YBQpI7YXePJnLSWGNXb8pjeQQFDEULTPOE6B9NqJCL4NUpmvXHHBDSqJhpSiPC8xrJdTt0rcEFgcmPo6U0dQ1WzZidiwUxddehYP9vmXQ7Vhqr8vAYgDmTK4jPAnQ6qA2AF4U7pBd4H6TvjMvF3M299DCCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پدر و پسران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/100544" target="_blank">📅 21:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100543">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQBX7Vs0CFUNWYWGOpxwHXRCeht195jS3UuivhHKvV4y6gKEGh_mkhwuMoVS6lfCLuI6qSDPtSes6skAUwYviXWPOXvzRMQ9sBrIjAXsUcpyruoSV3hJiaV8FRvUo1EpZkG368nfVulAQL6q4Hm3I2AUpikq5xI9ccTD4J1Ot8_jv3-vbxsQptwZZzwMGs7LxRLADjOGd0BdhUCXyj9GUx9alMs9pvyYNs_Zqg8SF3rAyGtIRRBB1Dp31V0GsG9suP0vFF2KjLrsIbQ8doLIp1YNgpzL1-yqCaeCwNaOwFdtXTqBiMoA2rp-D3Su585jtXBBFXIOjuygbAwgAE-Lpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
اولین بازی‌های زین‌الدین زیدان به عنوان سرمربی تیم ملی فرانسه:
😀
ترکیه
🆚
🇫🇷
فرانسه — ۲۵ سپتامبر ۲۰۲۶
😀
بلژیک
🆚
🇫🇷
فرانسه — ۲۸ سپتامبر ۲۰۲۶
🇫🇷
فرانسه
🆚
🇮🇹
ایتالیا — ۲ اکتبر ۲۰۲۶
🇫🇷
فرانسه
🆚
🇧🇪
بلژیک — ۵ اکتبر ۲۰۲۶
🇮🇹
ایتالیا
🆚
🇫🇷
فرانسه — ۱۲ نوامبر ۲۰۲۶
🇫🇷
فرانسه
🆚
🇹🇷
ترکیه — ۱۵ نوامبر ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/100543" target="_blank">📅 21:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100542">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsbaQu-kYKY5BdIBFELfcp9lbZcv1LqejPXzUD-BvbmnKS78eApfLD6NfFpos3ZEn9khi-0dmrzvNvzhE1bGFC7n_3Kk9B0DkzAUIC4VX1hDOxnIXo3Sgm8jB1kcSkh0LPds2BYiWTF6hgoKv7y-_m-4lVTQ6x_Wsb520lCvxdFkAVN4MOpsifUVPhwaa8rQHvec5n1wqwueHV0crS3j97DydrfQk_l7hwpUngDmX7s4T6ETSwRV4MtqvHFgU_E4WiWwjn4cw-u4dWxqRANUPEZZCfIBWOPkkUsD1nnC46Quc92218Nbeg3D3xvL7DF-hP1OTcmPD21-2m3Raxx5nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
خبرنگار: چه تیمی قهرمان جام جهانی خواهد شد؟
🎙
گواردیولا: بنظرم آرژانتین قهرمان جام جهانی میشه چون حضور مسی در بالاترین سطح آمادگی، یک مزیت بزرگ برای اونا به حساب میاد؛ مسی همه چیز رو تغییر میده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/100542" target="_blank">📅 21:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100541">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b0ffa0ac5.mp4?token=DBjs-n6yIBclHkYiY1CUDbu_8Qs86q_6pl7g15lhj7Y3nobZ6qNfL6vHS4To05ykohr4Lca0npo7rmoyEbmn54YOUlGj9v0lQPXeWRL4ZhzY4m36kXXg4vWweNBveLnzY3s_uTqfYRIg8CWXfK7EVkvzr8JObLcOejoAnNcYKYHH6SDgarrnqQiKU0Yh2KW8pXuUupt4Yd9XYU6OwqyjTZlEuA0fuOItUovaIy-WtMlaSJA9hF7FYrwiWmg34Pg78asfbTdXoinRX1GqAU-gB4CCr7coxBq_TTKewfYO6mr-JX9admGsJGYAJTMroF4o7pSqGYcgUPTlT8gE_nlRpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b0ffa0ac5.mp4?token=DBjs-n6yIBclHkYiY1CUDbu_8Qs86q_6pl7g15lhj7Y3nobZ6qNfL6vHS4To05ykohr4Lca0npo7rmoyEbmn54YOUlGj9v0lQPXeWRL4ZhzY4m36kXXg4vWweNBveLnzY3s_uTqfYRIg8CWXfK7EVkvzr8JObLcOejoAnNcYKYHH6SDgarrnqQiKU0Yh2KW8pXuUupt4Yd9XYU6OwqyjTZlEuA0fuOItUovaIy-WtMlaSJA9hF7FYrwiWmg34Pg78asfbTdXoinRX1GqAU-gB4CCr7coxBq_TTKewfYO6mr-JX9admGsJGYAJTMroF4o7pSqGYcgUPTlT8gE_nlRpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرد شریف روزگار
👍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/100541" target="_blank">📅 21:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100540">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">فرم هایی که چنل های دیگه با اسم vip ماهیانه 2-3 میلیون به ممبراشون میفروشن رو شما بصورت کاملا رایگان میتونید تو فاک بت دریافت کنید
💸
🫶
فقط کافیه ۲۰۰ هزارتومن اکانتت رو شارژ کنی و با مدیریت درست فرم های یک روز فاک بت رو استفاده کنی تا نتیجش رو ببینی  @FutballFuckBet…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/100540" target="_blank">📅 21:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100539">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Stg69w2A2y8CH3l6U7O78Zgv0qLWFJkgU-yE0Pkh3WIizoyrIdgWb2mldFVXAlH-ACFIEQC81m9OKI1M25qDlgNPGL9ZiXjbX0DRB9el1vEvOjeaCzg2jE0_0LLEN7MjXZKLz9oPR9bKNFHb_1vX3C8WMATZPU-Trb9foNSoZgHkHAaRlB8fYfZ0AcIk4X9MNFKHflraU9Ox7e-zMIUGEcsFjMf9tBqQdPslxXo_cKGfqV4F3Li6GujNJXZkPdI6zzp5ykRtgH16whRgD7zBNTtWuLNxFV5NTcgBQ1cIqd1k-QgBLIm0bpCAKgU9YsKfOxTA5OAMo4rnBEStGXH1Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرم هایی که چنل های دیگه با اسم vip ماهیانه 2-3 میلیون به ممبراشون میفروشن رو شما بصورت کاملا
رایگان
میتونید تو فاک بت دریافت کنید
💸
🫶
فقط کافیه ۲۰۰ هزارتومن اکانتت رو شارژ کنی و با مدیریت درست فرم های یک روز فاک بت رو استفاده کنی تا نتیجش رو ببینی
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/100539" target="_blank">📅 21:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100538">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IkJCsgwdyG5f-Y-ZbHn9HU9-yX0l7nF3ccSxco2jxH633mu8fiEIyh6a5LgL0JBRIhrQkVm-tHhVQzTDjNM8IiX2RGKisLoNYQEQbyhMdCG7aB8-hbgE7H1CNYVtCFJqubuwJ4qPLQDbc5ZM3e06eFHXKhgMoNSSBpey0jW8EDqGgFjAl6-aYPBDXuMvp7aIRmgCQ3YTjUxviCDlztdSZzohLuY9KwcQHHGnzkrYiCCHZn6Ww-hohssdl83dG2e0M_6vcfY-mAHer0e-R71X8-ykiHCz-Fguyrrhhd-vENDbrdMonqP6iT1iZRaJEzvYg50B0k6KZjQBNv19A6jASg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🗞
🇩🇪
#فوری
از اسکای‌اسپورت: اولیسه به بایرن‌مونیخ اطلاع داده که در این باشگاه قراره بمونه به رئال‌مادرید نمیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/100538" target="_blank">📅 21:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100537">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CudcaN-6GvW1Botd5lOg7X888ZJxfL7WL2maOA9g7jrY0rUIHMS_poGOlV3Uqbamocupg_Kwez5Z2w3KbVSpOTJxoHe5rtG-Lt41hisUDh6_nNqs1O_XrWamfxx2IVtahuRqu_jHdwWXuSomXetIZ06JXaw24tjDZ38aGRsd7gx31Ko6V_GO2DBDhiAruVznnD9DawrNX1Km7KYX40ppAI_jH7eK7H6_RNDDUCPjyYx0_8cbWyk7K89G8FJS1UTAMBX0Ex1KELxAOMFmvrdYaTWe9Ko2a_pSAigax8pwjlv3teIXFGAZFvoLCD0uHPpht1T9hUUtGROhg2lxDHlvQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
یه‌کم جمع و جور تر بشینید مهمون داریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/100537" target="_blank">📅 21:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100536">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🏆
🇺🇸
سخنگوی کاخ‌سفید: دونالد ترامپ در فینال جام‌جهانی حضور دارد و به تیم قهرمان کاپ را اهدا می‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/100536" target="_blank">📅 21:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100535">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/378abba176.mp4?token=I_7oRLYOFTIyv_PcIjfOW9VhjDDzO_aNym9uTdHzhccKIjlAeTs-arOYpoooyYyLiLnWMJINCzUrBru8VlMEzXume4k-EmEskkRD2NXUkVC4a4YUwyVTknkZP0InCK3aTJ84Jg5b_FRyyPVHZp5DScbuAPp4u9yFRMJIKoJjOrbhgpn1Gz3_UZTgJEGodjkbE36dDy0Qb5u2xVhB__A7kgSuB5QqvACxTbmdWA8ZAb7tAFL2Kh0Zp7H0UpxJDCUQbwZOptk5HX8_tLDWcWRtRTu1053uwyY9TgBjEFzvk66iCE9ejErvX8aYY02d-YlyHXMJfZlAsOUGZEvMgDNnpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/378abba176.mp4?token=I_7oRLYOFTIyv_PcIjfOW9VhjDDzO_aNym9uTdHzhccKIjlAeTs-arOYpoooyYyLiLnWMJINCzUrBru8VlMEzXume4k-EmEskkRD2NXUkVC4a4YUwyVTknkZP0InCK3aTJ84Jg5b_FRyyPVHZp5DScbuAPp4u9yFRMJIKoJjOrbhgpn1Gz3_UZTgJEGodjkbE36dDy0Qb5u2xVhB__A7kgSuB5QqvACxTbmdWA8ZAb7tAFL2Kh0Zp7H0UpxJDCUQbwZOptk5HX8_tLDWcWRtRTu1053uwyY9TgBjEFzvk66iCE9ejErvX8aYY02d-YlyHXMJfZlAsOUGZEvMgDNnpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
فنونی زاده خطاب به جهانبخش: اگر تو ایران بودی یه تیم دسته چهارمی دنبالت میومد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/100535" target="_blank">📅 21:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100534">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47fe3526bc.mp4?token=oKRM__4feNIwo7uJ3RLNz3QSYPy-sPJYGbzagpBU0R9-fBzp6cKqCWe8KrRL7fY6I_PNAJbCrl5_e5hVcFJwxsEN0T6MPTxGBRBxrYzlCRXaDDS07oIvrGKZl2b7CKUEeaT7B2cnY2tBSvMuWb1fvgHLYsr2pyJnFkn5_zLVn8WwgQ3O79n8kK9L4SL_F89CM486bsnX-x53RTQQbHr1xZE0Pf6F0MStvgH-gW7L-Kpwm0waHs6sfxAeLnfQMUJOQwOSvrFMJjMCaztS74YwHQwYzEoR0UwknQ2x6WRzyUHwUEjrC519pJkWPMQEfAhGiwc6cfsPI3Vyt5vhAxWceg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47fe3526bc.mp4?token=oKRM__4feNIwo7uJ3RLNz3QSYPy-sPJYGbzagpBU0R9-fBzp6cKqCWe8KrRL7fY6I_PNAJbCrl5_e5hVcFJwxsEN0T6MPTxGBRBxrYzlCRXaDDS07oIvrGKZl2b7CKUEeaT7B2cnY2tBSvMuWb1fvgHLYsr2pyJnFkn5_zLVn8WwgQ3O79n8kK9L4SL_F89CM486bsnX-x53RTQQbHr1xZE0Pf6F0MStvgH-gW7L-Kpwm0waHs6sfxAeLnfQMUJOQwOSvrFMJjMCaztS74YwHQwYzEoR0UwknQ2x6WRzyUHwUEjrC519pJkWPMQEfAhGiwc6cfsPI3Vyt5vhAxWceg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🏆
حضور تیم‌هایی از قاره‌های آمریکا جنوبی و اروپا، احتمال قضاوت علیرضا فغانی را در فینال افزایش می‌دهد؟!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/100534" target="_blank">📅 21:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100533">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGnTqKCvr6lMJOTS3KEtIefu_NBM_5opmzVeHk7H64ibiOwxJQU7kl-E6GPp30Loa6n9easpfCcduS4UGQSt4CDcv2Q0WOeZlK60N4zFtiDatxRO41xw7DOXs0GpPNpkwnlizczUFT7bbYMsRxuEsjPB6IKiDTBlHBRD2Dg6jge_Eqnatn8z4mIpOn8oEWv9GvGdHYuP2y0vTIn0nhoELdR8npWQDlA3IAJDWhTjtm2YRxRGIlvoNjkWPlFdwS-c5zGA2nsHQvjxFsOkj0_dzj28KwVe1OR0cCR_qx7wwp5i3-5XFMW3a8Uk-hFG0QGBpqoxIznv3XJ8PNVKB4jqqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کپی ترید خودکار
— فارکس و کریپتو
⚡
اجرای آنی
— بدون تاخیر، بدون دردسر
💎
رفرال
— با دعوت دوستان درآمد جداگانه داری
💻
پشتیبانی ۲۴/۷
— همیشه در دسترس
🎞
آموزش شارژ حساب</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/100533" target="_blank">📅 21:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100532">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/735694936e.mp4?token=px0rgKq1lyIfm8E1_QcHlJ57_ykxWk6teAK4_GUnRjwyKYf5WXDTjqXIxpDSnBSVxQo4jRDtuYxN1JrxEoEWNHXPgQTVpZVD6Cv5nF-OioFKY6kmArZ3e3-jBk6rzQzl5DNzp06Vh8GqOhhRycwCYqfNr19gVMu1bJA8OfWiQ2d0Xx5FJXdWplCoJCb1vOv69bdHNzocdr7jq96w-Ub5KPG03xO18_qf6bC4-w0LqnQLkmFm7J4GXMWxvmh_qjg_Os9g-Xb77VoGPEJI5pMsHiUvMHqWzH9SSckCz1RC9bU9R3SyYEJXRX1xLu2azzoRjDj1iMvCiWoRtCe5v33aAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/735694936e.mp4?token=px0rgKq1lyIfm8E1_QcHlJ57_ykxWk6teAK4_GUnRjwyKYf5WXDTjqXIxpDSnBSVxQo4jRDtuYxN1JrxEoEWNHXPgQTVpZVD6Cv5nF-OioFKY6kmArZ3e3-jBk6rzQzl5DNzp06Vh8GqOhhRycwCYqfNr19gVMu1bJA8OfWiQ2d0Xx5FJXdWplCoJCb1vOv69bdHNzocdr7jq96w-Ub5KPG03xO18_qf6bC4-w0LqnQLkmFm7J4GXMWxvmh_qjg_Os9g-Xb77VoGPEJI5pMsHiUvMHqWzH9SSckCz1RC9bU9R3SyYEJXRX1xLu2azzoRjDj1iMvCiWoRtCe5v33aAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی وقته دنیا یه خوشحالی از ته دل مثل این صحنه به ما ایرانیا بدهکاره..
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/100532" target="_blank">📅 21:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100531">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BKsxqecPzWq0ff2ISlxm217bMDD-N1Stu7KHDK1Ibd10PQMExUbj6opnP5CR0RNrrKxPRg3ffRhy7XVPhW4tlqCk-wqkXc0DuoJXh5hAxa5prufg11ScX59DxLUIwoOQtKH5E8KZ7AECPqL8z0vgDU4YSWi0FlLFjZBhJ5H5jPbCGsHf2KNT5x8Mzr5V_Wz-NQrDolwVN_tHZpuHfPYzT2SD1c9WjZHEAWInmPf68ECLrTsGxg3NKq4kuD3fmHxay4AeBrnXqAQYO7B2iE6Xr2rubFtlgzyQcfnBT3pEemdA-RdEptkteDQXIiMQ13H8xdEPN-hrGcH3aLbliadz_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو
🚨
🚨
🚨
🔴
کریستوس تزولیس از کلوب بروژ با مبلغ ۴۰ میلیون یورو به آرسنال پیوست.
𝙃𝙀𝙍𝙀𝙀𝙀𝙀 𝙒𝙀 𝙂𝙊!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/100531" target="_blank">📅 20:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100530">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6JDy3hkKY_gwM3i0OYMLca4mHZabkJJLcTNsCEzyyxyZwHXwEbAea3fZeymR40TN_Ov7mfzZxAAaFkkUp-I9vFayLLMqngBRN2gHrwM8zpo5cjehjSpaJGCDtqUTqtJRSRCPM4yYC98dm3o6gBk1dt1CZLjJ1Yx4KimNmo-0wDX_NqIzqchgZ0CQo7pM1ZF4-a84vDdzGtHcDNQSJniETUJeWJqOhHmipe-GA-hEbZV8IYAHKm2kwayHCvaKXOiDRCifDZJl0-sFJE5e9TK3OgywkMXmh3zjAY4_cb9wGAaaplb8iCWuBJzpm4ursNHJPswDMxoF5Le1UuTaUvmUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🚨
لیتان، رئیس باشگاه لیل:
🔻
ایوب بوعدی باید برای یک فصل دیگر در تیم بماند چون باشگاه لیل در لیگ قهرمانان اروپا شرکت خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/100530" target="_blank">📅 20:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100529">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">لیگ ملت‌های والیبال
ایران
3⃣
➖
2⃣
آلمان
🇮🇷
25|26|18|25|15
🇩🇪
22|28|25|20|12
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/100529" target="_blank">📅 20:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100528">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ec19c4e50.mp4?token=QGPR4PaTLBMs_j6S6Vd4BnTqK6s9zBdqETfwJB9LoPE4_ljbzRg8HSfIhTIRSkvVM1ACu5RXhAGe_zVAcog9D0Lkvx59HUZcPEM2mgWhBk75BzXZFNeCgipwjlVZWrmSawNgJiO6bIkOSC4972MS-xcwaJ4LU1v_TzkWscDp23CxDQlBF3c11xqao-4wfH33ACxcZrFMPKLy7gVVzlQzic4Q7FrC1TSvznR2AgcjPVE51jkGvQC5maHruCnIZoONZ5FDA61ISvg_9ElMPvypexUbFdLToWhuEaHD8pub1Y1vGZsDnLhTiW5Nf5L1yHjwNBCJonT2-ixsOd70but6Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ec19c4e50.mp4?token=QGPR4PaTLBMs_j6S6Vd4BnTqK6s9zBdqETfwJB9LoPE4_ljbzRg8HSfIhTIRSkvVM1ACu5RXhAGe_zVAcog9D0Lkvx59HUZcPEM2mgWhBk75BzXZFNeCgipwjlVZWrmSawNgJiO6bIkOSC4972MS-xcwaJ4LU1v_TzkWscDp23CxDQlBF3c11xqao-4wfH33ACxcZrFMPKLy7gVVzlQzic4Q7FrC1TSvznR2AgcjPVE51jkGvQC5maHruCnIZoONZ5FDA61ISvg_9ElMPvypexUbFdLToWhuEaHD8pub1Y1vGZsDnLhTiW5Nf5L1yHjwNBCJonT2-ixsOd70but6Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
بلینگام، درباره بحث با مسی:
هیچ مشکلی نبود فقط داشتیم درباره صحنه خطا صحبت میکردیم، خیلی شلوغش کردن! بازی کردن جلوی مسی واقعا افتخاره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/100528" target="_blank">📅 20:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100527">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f42b6ddc.mp4?token=G5zIT3nfk9jtnu6KsXyVLUDLN50jQMNhOprP-CYbadA-4ov4qzWdVBTCSk10u-oRzBkJOk-gDHtObLfJjYOQTL51xicEkc_NAMkLkRtRgKmOyAO9WfHAq4fbxAKA4dPen24FMYxmZFP5w-1aFAluIHuXnN-_uRQXeIp-z26hfou6ClCtITLhx_SCCkGVUHy3yTEE4SpdrUTYMNDcGv2f9Vdocx5l7UFr0msf6jb13B4_abcRLkN7JSEKE-uepAFoV2qWoTOU8yB8LR8AnIXNgzkH0FA-ANsnD2WbjdyothVHBKU4InrUMvov-ffwbAm1IVugK2_Ct7VB0DEFY0RYW0TXqvaWIK7YD1EQJhR2QNUN7eZhbkSEV9Rdj1HNyhSIrM7CYlBRI-maesoXh73Eqk4FLn5DVvTGWHMZNtHI__RTopQiRUv7egFHRY5lCRgEHMIjcn6FYvcurAtJbF6g6w5q2DpYJQ2sh1D7EIRFK1FwoaqJ7SdvxLC4YaE8EgG9n3NDgcKQMkqKf5EGke-Hd8frGMeGIKhdH1lA5LdIR4v_drEyOAJZRNsTuS9m7ur71Vq72SSvbPrgm5qjPdJBTu8tIZPRRDYpJU8drVMj0RM5tN2UrIk7ECm-LY7F_ASc5gY4GvS1I-lLSDdbNrul9X7OOWEdV_z04sAA9KurYkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f42b6ddc.mp4?token=G5zIT3nfk9jtnu6KsXyVLUDLN50jQMNhOprP-CYbadA-4ov4qzWdVBTCSk10u-oRzBkJOk-gDHtObLfJjYOQTL51xicEkc_NAMkLkRtRgKmOyAO9WfHAq4fbxAKA4dPen24FMYxmZFP5w-1aFAluIHuXnN-_uRQXeIp-z26hfou6ClCtITLhx_SCCkGVUHy3yTEE4SpdrUTYMNDcGv2f9Vdocx5l7UFr0msf6jb13B4_abcRLkN7JSEKE-uepAFoV2qWoTOU8yB8LR8AnIXNgzkH0FA-ANsnD2WbjdyothVHBKU4InrUMvov-ffwbAm1IVugK2_Ct7VB0DEFY0RYW0TXqvaWIK7YD1EQJhR2QNUN7eZhbkSEV9Rdj1HNyhSIrM7CYlBRI-maesoXh73Eqk4FLn5DVvTGWHMZNtHI__RTopQiRUv7egFHRY5lCRgEHMIjcn6FYvcurAtJbF6g6w5q2DpYJQ2sh1D7EIRFK1FwoaqJ7SdvxLC4YaE8EgG9n3NDgcKQMkqKf5EGke-Hd8frGMeGIKhdH1lA5LdIR4v_drEyOAJZRNsTuS9m7ur71Vq72SSvbPrgm5qjPdJBTu8tIZPRRDYpJU8drVMj0RM5tN2UrIk7ECm-LY7F_ASc5gY4GvS1I-lLSDdbNrul9X7OOWEdV_z04sAA9KurYkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی دایی: «ما شکست خوردیم، به چیزی که می‌خواستیم نرسیدیم.»
کریم باقری: «همه طلبکارانه صحبت می‌کنند، در حالی که هیچ دستاوردی نداشتند.»
عادل فردوسی‌پور: «چرا باید برایشان مجسمه بسازند؟ چرا باید درباره استقبال از تیم ملی، واقعیت را وارونه نشان بدهیم؟ ما هیچ دستاوردی نداشتیم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/100527" target="_blank">📅 20:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100526">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFQjvSx_g1kJY5aSN5MLaeHM1SvxQL7Ztwg8LLqvdMJ--hSwL4VC11kaXWrkyQHpJyOYH27nOKVfEPieaRv1FDydqqPK42qHm8sKgvRFn0X2UI8Qjr1qzaoFeUIIlzU8PNswI-S_Ho69E_Pwuflr8k6Tz-uIXkfiI1T6ijb9YK5Rq0NZsK808X5i0R9XJ4CqXGpZ76CeLzVXEsniHihBFNK5IR9kCwC9z_thrTlB7c-JW2CXjDZkV_VyJjnFqW4KHtf4Rg0-UxNPs0XY0BZibzkYMqKEgdDadMxNGAkpI8lu7MbsKRMCHvHNLObx7smbduOzb2-3ExCpaDiBSkCvuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">�
جدیدترین پیش‌بینی Polymarket برای قهرمان جام جهانی ۲۰۲۶
بعد از برد ارژانتين در برابر انگلستان
🇪🇸
اسپانیا:
۵۸.۱٪
🇦🇷
آرژانتین:
۴۱.۹٪
حالا نوبت توئه؛ از داده‌های بازار ایده بگیر و پیش‌بینی خودت رو در
Betegram
ثبت کن.
🎁
۱۰۰٪ بونوس رایگان اولین واریز
⚡
واریز و برداشت سریع
🏆
بهترین ضرایب بازار
👇
همین حالا ثبت‌نام کن:
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/100526" target="_blank">📅 20:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100525">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zetqpj2MR3DFGKyQ_rhFtzPdwvWiIs2B8e_FGOBCcZdK8qOH7BeoAarjjQk8qWCOKj2ROEix5SUxwHcSZFnQY_tiKnGxz7SYrDfWpNgbc-_nkxuh29gt_q4CziAWiiBkePDPyOzJuuhXicAxgUC4JgOR7ni0f-taUL-rJNYMxKl5qHKycWv5Ng9hF4ztmaeEcIX8FBY7lcuouOJjixh58eI47_0xSaSZy1fIZxe6RU9REWD6Svj3inSGGneXiiPYfp3K8C5uZBFjjaKeg-Lkvw-bFefy96q9jwZOA4aEAiuCsK9dGCrzAJhpJkPs79XPokWFFc0Fs3lorox8-HUjtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
عشقتون تو تمرین امروز تیم ملی آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/100525" target="_blank">📅 20:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100524">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d68c789aa9.mp4?token=q5ovuUQ_KDcqEcwnrZZ7RFv-Avo-50Oc3tEB62EGPYF1m01wLCS22iKzlOqtwnZOZYmHRAVEEb-Qsk1x3nys5889zp63MQlreD1Avi_Fdyztmu6pjsQqY1tq7_Y4CWnH4I2K_I2yPhpbvh2ea43Yt_4y_VlyEPxSLo1BYrjINGLY31tNR31aQoQ6dvrN5OhxS0d9V0prVYAS4_KnKr20y4zTPOGf5amk7lvn9vWovAVUGXiDHaUSa70ZWx7_tF_V4q7e6QYBBhcBBw8X5--wEEIzqDbNRDorSJ-C2D4c-6yBucuS1rxi1Dw5Q-RhlNKdtbqBsZvNQ9AtB-iiWNuAXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d68c789aa9.mp4?token=q5ovuUQ_KDcqEcwnrZZ7RFv-Avo-50Oc3tEB62EGPYF1m01wLCS22iKzlOqtwnZOZYmHRAVEEb-Qsk1x3nys5889zp63MQlreD1Avi_Fdyztmu6pjsQqY1tq7_Y4CWnH4I2K_I2yPhpbvh2ea43Yt_4y_VlyEPxSLo1BYrjINGLY31tNR31aQoQ6dvrN5OhxS0d9V0prVYAS4_KnKr20y4zTPOGf5amk7lvn9vWovAVUGXiDHaUSa70ZWx7_tF_V4q7e6QYBBhcBBw8X5--wEEIzqDbNRDorSJ-C2D4c-6yBucuS1rxi1Dw5Q-RhlNKdtbqBsZvNQ9AtB-iiWNuAXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
❌
لامین یامال در تمرین گروهی اسپانیا حاضر نشده و روی ران پای چپش بانداژ دیده می‌شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/100524" target="_blank">📅 20:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100523">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PGA6hZxMJ4gCXPIX2Dw1YD1cxz2BauKCxbAM13joTc-ghNzNP-5nEYDVIXjH5XDq7Sq16rZwra4jtuvWuZQ2xrnjl4AKJ83uvBZm7xRkx1gWbO5FwVVECgETpQ9eeDAZ9EoOhbvdvswN0_5MWhowfJseyuLOGKh9vCzyrLDskD0HUrHh6w9KEvPOFSS-kdh_TADhTLReacJKwpOppDDZMeGC4tkybuGJax7H8qyHnLow4r3NUnmYWNU4hlMxGifR7RT9ZwfGJtHhYWEHc2XxcHdgmr4StvkY4yJjCzw97I-pwCOwWCma8ri3-XcwGLENOeQsnbd-OMDYMMaiHUVZTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
#فوووووری
– گل
:
رتبه‌بندی ۵ بازیکن برتر برای توپ طلا تا به امروز:
1 - هری کین.
2 - اسطوره مسی.
3 - لامین یامال.
4 - مایکل اولیسه.
5 - کیلیان امباپه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/100523" target="_blank">📅 20:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100522">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Keph4i2kKe7zunAKsZClpBCcEaZ1roYvYvwviVHHdDbTtvbj_Cj4OkMn64sSivZ7Lx0tAkcvb6tknVvImnDv936_pWej1bfPLxbnr7HNLm5K1FxQdzOACutYdDvLMIbWM2LM5crJ7nKM0foUDF6_uT7fb9_ACJpHw9oKGUTdqcfxIr8_d18183sLaLYnis89yHMgXkZo1ObmpHYEFjboaeUlchjakFeT5ZQV6nz3fkuOYI6qaRxGm0zK5RYbbHrP0-UL8kJYroGpC5RPVORxYT_utx5JA-LJZh6tv7J5OJLM3QSFmlMrLenaKyYiYkPqTFf3mZd7i5B-M2HPL2JiXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📊
🏆
| مقایسه آمار لیونل مسی در جام جهانی 2026 و 2022
غیرقابل توقف
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/100522" target="_blank">📅 19:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100521">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62c9ac7d18.mp4?token=doxBXeMA0J_JYJQBW--vrggDjle1Tw6iuDorJ6btCo1GMllyWI6_VLAu6ZjOoQoRWZU1s_X0HFLvLk2X2zoAAzSMktlWvnx66n6lFEQ9ciOk9GJFkklvklAjXyVw5CrH5jN228VrOzVLplB4cfN0s3b0GXutamao3bpXp_AL3lBD5jw_gpi24ddLWZiKw6iulZ3Hy3UFqs0O8Q_9hGdbdntH-GdXNIypMfVS3Mkjb8zgP8_3ud0vjTA988cpcj1So-90XfaZC0Sox9I96SMX-BKmb592YCW_pHpl1plswunfw6rxpW7cdrGW2ZB20X4J1xY7p9gR0QrN6d6um83vMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62c9ac7d18.mp4?token=doxBXeMA0J_JYJQBW--vrggDjle1Tw6iuDorJ6btCo1GMllyWI6_VLAu6ZjOoQoRWZU1s_X0HFLvLk2X2zoAAzSMktlWvnx66n6lFEQ9ciOk9GJFkklvklAjXyVw5CrH5jN228VrOzVLplB4cfN0s3b0GXutamao3bpXp_AL3lBD5jw_gpi24ddLWZiKw6iulZ3Hy3UFqs0O8Q_9hGdbdntH-GdXNIypMfVS3Mkjb8zgP8_3ud0vjTA988cpcj1So-90XfaZC0Sox9I96SMX-BKmb592YCW_pHpl1plswunfw6rxpW7cdrGW2ZB20X4J1xY7p9gR0QrN6d6um83vMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
کل‌کل بامزه دیشب عادل فردوسی‌پور و علی‌آقا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/100521" target="_blank">📅 19:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100520">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCk-sWsJ8QXGKr6xo3nqhQ5ehilWiev4fgjQoZMoDzKihypTxsL-d9DSsRgtqeCw4yToPOutDRZaNacmdtTCsWMw2JUpLL_acnr1aiMRslmJsST_-LpWWK_QxyQwqFfP29CEHe7xf6m-xH_-50jbNq-HnTT77189fkqMA06R23NzCHo8oFDd6edqQ9brGO_tmzEcItKACsD6M6YQPQwiS7wtsjz6K1o_DEC43q1Tkab6JRAFAWgy8YxnH09j7HjjyKwK4e_VC_m4mhtr24J5vHE7qzz4cQJe1WkEu0iDy5XhaH3FmO5pIX0Os_y5zqXYXE8wAzMJhSJP-ie_CUIboQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فابرگاس و خانواده قبل بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/100520" target="_blank">📅 19:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100519">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ea-6e355u7q2zIVd9FR1Immq7ima0SIDLct3VKLU9jRYPLm8aELRi3pY_HAjZFbYuy8KOpHfAmWXoyBIV_wUonigL3V1QsyzgSLCwmPtxy37BrpGfoaVXejABx-BDrhchH0CNPbSLxRD78gqCz_7MfI4nTOQYTn-7geO-iPyqdMndZMu7uIFoWAglg3W8s0e6diixmD-AfhVXlmgnmyc8njNRIpYh3-acgRbwniAE4jbZi4xv3EyvxWf1vdY09u-65lgiGWHwoaoKyPFJwdiUGVVZZFGqyQOt3iM-QoOWVWLdZF1I3ghE2n0orkPGyMEqxoNK7Mnb3wM71v2IPwQmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیت اول آتالانتا برای فصل بعد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/100519" target="_blank">📅 19:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100518">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OYok3l7dxmOeVXprkdNaGAWkMb5SKJHpX-r2_ubki8JXD0joaD8MrnGpe6Qe-k4tzxcHPfRGC8lxPrL0ukmpdKlD5mlwQ-ggEQGA2XOQfbyzGKJJRpo8xiFO_0kgs1_hEs8813YRN_kRSMk1GO98ypjhHRqGxOJLG_ACES-_1JGhfp4_oETj1htYp5Ho6w3APCzDPgdxcCZJ6EEDIzSaXcEL2TBk-i1ihqNtflj5KYZ0izUeOTA2Ebb0nopvS6GC5ncwKLtVTmjm3xJrTYGdcelc1QH6Q7mdUFkmvWsGdiB4vfUQG8rfhyUPh_ExpKJ7g4VPMCHPoLoiwoeMbQj3jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سازگار با تمام اپراتور‌ها
✅
لینک ساب اختصاصی
✅
مناسب برای گیم
💵
20 گیگ — 120 تومان
💵
30 گیگ — 150 تومان
💵
نامحدود — 200 تومان
📣
همراه با تست رایگان
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn
چنل رضایت مشتری‌ها
⬇️
@kavianivpn</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/100518" target="_blank">📅 19:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100517">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ugDGvSdNz_xEKvb4ytUZzNQaAuiXm6jKhSC29re3VuzlHZ0EpzjGuJg_Vbzq_psi0QfHXC4ugERrQU2b0AZcHVenlTYTTeRrzEPoNZBtRzJZb5Gme91qW9fUxCgGUPIn5vr4Gkl5n3vtfxqkdXQfw9qU94Vvf_f7-BYTF93FpE1kqz9j2P_zUtJPa7e-JbWQBQlUhDya7le1dIzeioEcojVbFi_VJ3tU8ecFKJMsbfW4VEFiwkIOYajszF2_1h3dFxlpNbgLxP9eLmRg16KZyP5diSqjHo37gj5wCP8hxxbHGTSaqpOx_s6kaCZdtUcy4A-us7KSiy2fk6S2L324ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
استوری رامین‌رضاییان که بنظر شاهد جدایی این بازیکن از استقلال خواهیم بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/100517" target="_blank">📅 19:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100516">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4mS7Lbm8LiT0NbK7Eq6Y2_nyAmYQy1c9i_bRBjLpybQmVvS2fe3EKhKvEUi-uBKmgUbJoNZwgoE8Vgub0TNP7lVylAE3Lt8RBx6dE6biXyPkgBu47DIDnz5cNdaqBdP-cjrJEJiks6QFA8L0TxIcxZKkWltkt5LuzBisjj-RvnuDRjA7lXX6mc9SJMPLVqflVQgE9MIiPVx4rgsNo6IFWUQZwXxXArahzynJJ0-DW_Ky7ZaC7xGYtSmMv_NYqaNpS95iLm8u86VkAUlq9ioBXZ_aKSibHGXec2oCoCQTDACWMx9AuSr4LB9qBufFwg6yhx5rbW1l44-8uunVYv1kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
زین الدین زیدان برای یک انقلاب بزرگ در تیم ملی فرانسه آماده میشود.
زیدان قصد دارد یک کادر فنی بزرگ تشکیل دهد که ممکن است شامل بیش از 25 نفر باشد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/100516" target="_blank">📅 19:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100515">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ff7cbd247.mp4?token=CuGsSWD7foda-qmrEQSl54q6dNzoDzbwQMp4XUn4zcvwcV_H0YKVIkW1dltcFFwsxax7kaYP2uB1DvL6u49rf4U0THoxHJouXBXT9w5tsp6RUD6PzmlCb-WsU_y0l3xgHkl4m_njjQK4-9c7ZU46LjtX1jfpRY-uH176oTsi4bHCSzn-F5YJW0bxpjFY0y16IR81VIHwU24vkFOFPjaZKIvYprv33TkkAbeNdrsU0O3nrlGE4fKd58Akv1qc4ml2mW-7RL-uvqa9wHb7TnTOYfJEkB1YXyrCBRwZNyBNTxNwwIHu5BruK8CV4JBGlaGn0pUmD-uzpBeuj5Ro1vjcdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ff7cbd247.mp4?token=CuGsSWD7foda-qmrEQSl54q6dNzoDzbwQMp4XUn4zcvwcV_H0YKVIkW1dltcFFwsxax7kaYP2uB1DvL6u49rf4U0THoxHJouXBXT9w5tsp6RUD6PzmlCb-WsU_y0l3xgHkl4m_njjQK4-9c7ZU46LjtX1jfpRY-uH176oTsi4bHCSzn-F5YJW0bxpjFY0y16IR81VIHwU24vkFOFPjaZKIvYprv33TkkAbeNdrsU0O3nrlGE4fKd58Akv1qc4ml2mW-7RL-uvqa9wHb7TnTOYfJEkB1YXyrCBRwZNyBNTxNwwIHu5BruK8CV4JBGlaGn0pUmD-uzpBeuj5Ro1vjcdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«قاب رو ببینید... علی دایی و کریم باقری... خیلی سنگینه!»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/100515" target="_blank">📅 19:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100514">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6P8D88h1e_ywTuh4UbXQl0IfKxaOV3ICgNj9HZMNa6vUrtLgEvcWrA-4XKjikI95cSbIOI3UxhEo130W9H7sCxIHj1sS0nkabkVPi-XLWDYx4gwxLt6I0H_phj0YYP1w9mdgYgdy00oUeMbBg4Th1Gf6LvyQGciFGdEm1YIuFf1UcdBulm1GcMHEzv1X08i6epvFD8i7oOfIQnr0Edjony9FrCacSx0F9vMeEyKqupitevpO3xQMk_2JIjfhoFucUpiSJiqCveP4xFM5YM4TBuG5hahgVx2OGBl2SVcNRM859sg3d-0iKhXGSFWIaAL0PRMBuU65LZKgIoihoyMtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمعی از هواداران فرانسوی، طوماری را برای درخواست برگزاری مجدد مسابقه بین فرانسه و اسپانیا منتشر کردند. این اقدام در اعتراض به پنالتی‌ای است که به نفع لامین یامال گرفته شد، به این دلیل که ادعا شده بود قبل از ضربه، دست او به توپ برخورد کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/100514" target="_blank">📅 18:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100513">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/121dde0263.mp4?token=SQ8_rWfQxEy_AK2o_Gzt9OUyZsVnQQN8-pZ2-Kj0xETT9KB_NV798nlUR5E34Zr5zx8JWlbmxX-To6I06BRkw2bpbhI0NAUfQc5QARuDbT3j1YA-ea6h_CwNmKYZuH1oZy8NOeWqyFKeEMO560HC6U_kgvHYOn1CrBPLNR3STOwndTFovDxbo6cnGdSopM3X6ZOmjs89nFpeXQpBVWsVht4asZITsUdd9HjV3nMpRUbUuHj8SuXyDbGf4HVg-omYTF2dzHTrbCOymP8dHudCzgBh6O2_gA36TxhL6UHElEO5ZMZpGg787bZT3syeYOIu1z3kEs7G-tKfqThNqxI7Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/121dde0263.mp4?token=SQ8_rWfQxEy_AK2o_Gzt9OUyZsVnQQN8-pZ2-Kj0xETT9KB_NV798nlUR5E34Zr5zx8JWlbmxX-To6I06BRkw2bpbhI0NAUfQc5QARuDbT3j1YA-ea6h_CwNmKYZuH1oZy8NOeWqyFKeEMO560HC6U_kgvHYOn1CrBPLNR3STOwndTFovDxbo6cnGdSopM3X6ZOmjs89nFpeXQpBVWsVht4asZITsUdd9HjV3nMpRUbUuHj8SuXyDbGf4HVg-omYTF2dzHTrbCOymP8dHudCzgBh6O2_gA36TxhL6UHElEO5ZMZpGg787bZT3syeYOIu1z3kEs7G-tKfqThNqxI7Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
تفریحات کارگردان استادیوم‌های جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/100513" target="_blank">📅 18:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100512">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c73b07447d.mp4?token=os3PSBVmhXOU1KUK3FCP-59YZDp5MFksUuE3HddxqGiervwpKupLnxNjL2y0qEcYihrhEFdtNvGQfYUF4jLfO3cAyrJsPQ5Zxwv0nyGXA_ZOxaLPaI1FGnaUIlEFcuTb7NzmjkwvnWqXr9X7buxMSfxZD1NcqUbkYQEk2ZozlbMa1mTXNfdZgbidDMNFg6dxiJMXriTIofb4COOejj5sbkS3PNBEW6EnxppEbiA6-ZSocU1tIA83n9tqoCIn10yo1eC6S6f3gINfvdG03Gr-H08nRa2kzBHfU6HBrpkznteGMACKx9Bv_SKXO76FJ2a_U58xgb-7M9E6u66GK1YW6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c73b07447d.mp4?token=os3PSBVmhXOU1KUK3FCP-59YZDp5MFksUuE3HddxqGiervwpKupLnxNjL2y0qEcYihrhEFdtNvGQfYUF4jLfO3cAyrJsPQ5Zxwv0nyGXA_ZOxaLPaI1FGnaUIlEFcuTb7NzmjkwvnWqXr9X7buxMSfxZD1NcqUbkYQEk2ZozlbMa1mTXNfdZgbidDMNFg6dxiJMXriTIofb4COOejj5sbkS3PNBEW6EnxppEbiA6-ZSocU1tIA83n9tqoCIn10yo1eC6S6f3gINfvdG03Gr-H08nRa2kzBHfU6HBrpkznteGMACKx9Bv_SKXO76FJ2a_U58xgb-7M9E6u66GK1YW6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتخارات ایرانی‌ها تموم شدنی نیست :))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/100512" target="_blank">📅 18:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100511">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f049197c85.mp4?token=dAqnQlXE0hPwDs1L-CGP2GdfmQ81lVY9bEzblqgYwIk2yT5hlqc69rbiLfmRqT4hARAwiCkHmm7cNg5pvh49BFEZIEPWHn2Cl4fz_ekc2PcpMJRwRBq2fnLjfGge457L2iM04LUWZ88oYhTkbRgpUcwPoPntYvlB_ffYoyJyAJUzpfC7Yuhk1sHlSQqYxo9ap0hjfSXyBN9zvWYNcehzzJK_Klu-fsvRBkIfeFVt7tLnG3bLRt6eOAKqsC750NTiZYmH4lcbazLQRB1fxY-jY8kf19vSkGXWxtZXPPOcrCrZVeEzBLw8TogOUjyCByGi7X_kllAfj7Ed-I_ZhYW6Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f049197c85.mp4?token=dAqnQlXE0hPwDs1L-CGP2GdfmQ81lVY9bEzblqgYwIk2yT5hlqc69rbiLfmRqT4hARAwiCkHmm7cNg5pvh49BFEZIEPWHn2Cl4fz_ekc2PcpMJRwRBq2fnLjfGge457L2iM04LUWZ88oYhTkbRgpUcwPoPntYvlB_ffYoyJyAJUzpfC7Yuhk1sHlSQqYxo9ap0hjfSXyBN9zvWYNcehzzJK_Klu-fsvRBkIfeFVt7tLnG3bLRt6eOAKqsC750NTiZYmH4lcbazLQRB1fxY-jY8kf19vSkGXWxtZXPPOcrCrZVeEzBLw8TogOUjyCByGi7X_kllAfj7Ed-I_ZhYW6Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرژانتینی‌های دوست داشتنی خوشحال از پیروزی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/100511" target="_blank">📅 18:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100510">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4981bd9a51.mp4?token=EOoXIckZML67jWJA5gXJgL9fcnb0wniAA7iZR_TTzLagspD04lsACjrBAbOh3lutxLL8RwCObGCpky7ulta7J7w0Ca_roT8QZugSInrYe0-y3lS7pLOpCgsT_HGH21iQTyYW2z0HuOZWwpOTk5O31gBEQUtKDs7ZPW8gu230zjOZ2cf5RhUkEwwarMLFI3ihYA66eexbFv8pLJTUFLHmX56VaFv7O0-55xVca9mez1a6ZF05WGb7vWVIC8jhb-1Mwh7f9oT4uyljvPcRsq4WzICMHevC5Trn6cJbE0cz0FMSugpORYM2Df_dkZZWHnyST7FI1UU2Ylf06SGbZnGW-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4981bd9a51.mp4?token=EOoXIckZML67jWJA5gXJgL9fcnb0wniAA7iZR_TTzLagspD04lsACjrBAbOh3lutxLL8RwCObGCpky7ulta7J7w0Ca_roT8QZugSInrYe0-y3lS7pLOpCgsT_HGH21iQTyYW2z0HuOZWwpOTk5O31gBEQUtKDs7ZPW8gu230zjOZ2cf5RhUkEwwarMLFI3ihYA66eexbFv8pLJTUFLHmX56VaFv7O0-55xVca9mez1a6ZF05WGb7vWVIC8jhb-1Mwh7f9oT4uyljvPcRsq4WzICMHevC5Trn6cJbE0cz0FMSugpORYM2Df_dkZZWHnyST7FI1UU2Ylf06SGbZnGW-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
از کجا به کجا رسیدیم واقعا...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/100510" target="_blank">📅 18:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100509">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62564cea43.mp4?token=LFmNLIIS_elPTDB2KFC7ypwNrVoFSfGvNxxplEX_AgZAjECpLT4EjDjBrAvEhjOJ7qXj0rvRk81MoRJi7uHGIdRJ_ndQle3ROFSvD6upIrEpf0IpwQFSTcaBq73BXHEdL4S2SEhE_JfQ8uFhnlw4kaLzVExQbTWxjSVAFgvUM7WPZujQt9VwFegaw5fnZdl2_2Epo9JZtAyx_c374sWq5TrSYppGLO51Pyk1IoZ2XbzghLB3D3iHXlPA_q-6b0tbeuNxeUbEEEYmIHqjL5l6ZDWFYSi3VNmfd9__KKYziL_NAVuYwBfHIrVaY3ER6RfDn28fuJiElaY5rkrmy1O4bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62564cea43.mp4?token=LFmNLIIS_elPTDB2KFC7ypwNrVoFSfGvNxxplEX_AgZAjECpLT4EjDjBrAvEhjOJ7qXj0rvRk81MoRJi7uHGIdRJ_ndQle3ROFSvD6upIrEpf0IpwQFSTcaBq73BXHEdL4S2SEhE_JfQ8uFhnlw4kaLzVExQbTWxjSVAFgvUM7WPZujQt9VwFegaw5fnZdl2_2Epo9JZtAyx_c374sWq5TrSYppGLO51Pyk1IoZ2XbzghLB3D3iHXlPA_q-6b0tbeuNxeUbEEEYmIHqjL5l6ZDWFYSi3VNmfd9__KKYziL_NAVuYwBfHIrVaY3ER6RfDn28fuJiElaY5rkrmy1O4bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مارسلو چندسال پیش گفت: ما تو الکلاسیکو مسی رو خیلی عصبانی نمی‌کردیم چون در این صورت عملکردش خیلی بهتر میشد و دیگه نمیتونستیم جلوشو بگیریم! درسی که جود بلینگام یاد نگرفت و باعث درخشش مسی شد!
👑
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/100509" target="_blank">📅 17:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100508">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2241a88830.mp4?token=pddk8enQhq6gRLXGtSf73o5UDncqGt5Dm3bARhNO7KtVnaa4FdfQfiyf5Kj8akeuM24kj1JjTpfPqzAQJnd66MDAaLfqRAXjDaWK-ZhxtukbJyTEIjO0G2M_gBCgpi5SZRmA7Xj863mQxWD-hKkrlanFnUmip7YGbVdwBbleBbzxP2Mk2fbSgzyodPVSCOiVwF-VYjpgpJvzrVZKd-iWA2Rv_FtUoLKYM8eFxK3YJ-p-B3dR1Zn3a63idEux86U96hnY5UQzBgdMWKs3Hd9rHdfKm1eorOrBboFcKf9EF1XvC3Jj6c_bcWRxsi_Q22MB4HxR-mnd45e0XV2VJrZBJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2241a88830.mp4?token=pddk8enQhq6gRLXGtSf73o5UDncqGt5Dm3bARhNO7KtVnaa4FdfQfiyf5Kj8akeuM24kj1JjTpfPqzAQJnd66MDAaLfqRAXjDaWK-ZhxtukbJyTEIjO0G2M_gBCgpi5SZRmA7Xj863mQxWD-hKkrlanFnUmip7YGbVdwBbleBbzxP2Mk2fbSgzyodPVSCOiVwF-VYjpgpJvzrVZKd-iWA2Rv_FtUoLKYM8eFxK3YJ-p-B3dR1Zn3a63idEux86U96hnY5UQzBgdMWKs3Hd9rHdfKm1eorOrBboFcKf9EF1XvC3Jj6c_bcWRxsi_Q22MB4HxR-mnd45e0XV2VJrZBJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چالش عادل فردوسی‌پور در تلفظ نام وریا
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/100508" target="_blank">📅 17:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100507">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fb09b2935.mp4?token=pxZIHZ-mNIUdC9RWnEBbhyrkeEOW3O5FWovH_uTSNB68RXPEfAcQD8YcVpWgn85ycllsGkHO2-arpa9oFo7ASvGtkRlaS5t4J7OQ1pL-V2JhY4Ma80mZ7lZuRvWwWfDk15jgmkxgensxYyCaQKd0sXvZiKbOi1Omq87vrrfpmaFaA9NVqYayUYrufZXX8kRCfB8HmiZb68dzzAwuZALyNr25XqccQKOXf901aTYQ6_8c55qydoctW5AT5sisV_TJDrpOjDtNgF6MoRBGADDnvdU0eTYI070tdhWG9DN7gfwvDRJOQbY6uXhWoNHBqCoO4YmCB_YRBX6CgMhlMuIb95PVNI_piIiW9VkD8SRxgds02jxH3weCaumr9s8aE5x3NDS0IyuY1JNeVjmYAUPHjPRGo2mUa59gdR7_Set7TDgYIYaJuTVtynf6Kv4Bcx5C3CyMe2Ceh4AVtmBpvMSi2oL90u49k8X6v9ZzceT-1tpq1PUcMMj83xlDyXYCK84syTz5_Lz3fZ_z8g765RMFmLwksDhrsqNBTRnkG4Me3AJCuH1fK4-5gj-P1rd-98yoxUZovLZyRshDbGFAK9NrpXnH-3Nr3k7HG9AWDl0iJ6FQ6Fy-TN_hZkb2hbuaRy7VF5ruzI0jN2TiKxwn3vK4JSDxN9C8Yu-zuJcps_mK9vs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fb09b2935.mp4?token=pxZIHZ-mNIUdC9RWnEBbhyrkeEOW3O5FWovH_uTSNB68RXPEfAcQD8YcVpWgn85ycllsGkHO2-arpa9oFo7ASvGtkRlaS5t4J7OQ1pL-V2JhY4Ma80mZ7lZuRvWwWfDk15jgmkxgensxYyCaQKd0sXvZiKbOi1Omq87vrrfpmaFaA9NVqYayUYrufZXX8kRCfB8HmiZb68dzzAwuZALyNr25XqccQKOXf901aTYQ6_8c55qydoctW5AT5sisV_TJDrpOjDtNgF6MoRBGADDnvdU0eTYI070tdhWG9DN7gfwvDRJOQbY6uXhWoNHBqCoO4YmCB_YRBX6CgMhlMuIb95PVNI_piIiW9VkD8SRxgds02jxH3weCaumr9s8aE5x3NDS0IyuY1JNeVjmYAUPHjPRGo2mUa59gdR7_Set7TDgYIYaJuTVtynf6Kv4Bcx5C3CyMe2Ceh4AVtmBpvMSi2oL90u49k8X6v9ZzceT-1tpq1PUcMMj83xlDyXYCK84syTz5_Lz3fZ_z8g765RMFmLwksDhrsqNBTRnkG4Me3AJCuH1fK4-5gj-P1rd-98yoxUZovLZyRshDbGFAK9NrpXnH-3Nr3k7HG9AWDl0iJ6FQ6Fy-TN_hZkb2hbuaRy7VF5ruzI0jN2TiKxwn3vK4JSDxN9C8Yu-zuJcps_mK9vs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
اسپید:
دستم به دامنت یامال، تو رو به هرچی قبول داری قسمت میدم آرژانتین رو ببر و نذار مسی دوباره قهرمان جام جهانی بشه! اگه اون دوباره قهرمان بشه ما هوادارای رونالدو دیگه اصن چی داریم که بگیم؟!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/100507" target="_blank">📅 17:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100506">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I66BdoEzW2YZ8RXjTCZ1O8LIhTJ9cPlqcvIN49gv8ldUBDhWA4ZMe71jvzEBj3GJuBnZ-6W1dsrjFofNFvOsTgBW4a6vzCAfkkU0N5TKjbpbDjWeUJCq5lEw7zRhgyBsIr9qrqEFDwfWMNrasPat4AhpRm_ZO077Sfw-NuBgnc0FVxeJ17QzwxjNcD-m-VPMQzS6XNUkZVWbvj0fEtMc59_JSJBXId1bE_sRLaBpkNsk6i8V0qB5iQ2__XXQ_AnbQWxF5A5OtaVO9Dl5TkauTgA84GtXZGC968V4yfXAKhkI6Mi5-0GVfihxxjQNr-sZkwppIr0BPgQcjPbC_hhjng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رامون آلواز:
رئال مادرید واسه فروش کاماوینگا مبلغ 80 میلیون یورو تعیین کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/100506" target="_blank">📅 17:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100505">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/901a48c5c7.mp4?token=TM8xcd59G0l0GRF3ZvklTaWQJrNlCAh89WFcTdAGslMys9OCnULhrNYW6317PwbhgHu2VBf6dU2p4a75lIl_ZBQkDZovCXFrgssPKHOQbVxNtM7y54j9eK4njHch9Z-_jV39gNiKzN4wG4R9AU_B7PkNjo-xxeTctOtDkqc8nQkSWjX91K8Aw5vVxIGblKNPO57bzQmT1BjdHZS44ZBIOyWEFSBKaG44mKD76P3z4HswBxCRz_7AZaPWf-svPAyyPpcHjl62eIoNOAP0f8aTTh4oaJkrMFy2EkrpMGUkGaRLqHAD8oPiOYHYrvGCJGP3Z6SRCXhxiGSl0jCWRguPRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/901a48c5c7.mp4?token=TM8xcd59G0l0GRF3ZvklTaWQJrNlCAh89WFcTdAGslMys9OCnULhrNYW6317PwbhgHu2VBf6dU2p4a75lIl_ZBQkDZovCXFrgssPKHOQbVxNtM7y54j9eK4njHch9Z-_jV39gNiKzN4wG4R9AU_B7PkNjo-xxeTctOtDkqc8nQkSWjX91K8Aw5vVxIGblKNPO57bzQmT1BjdHZS44ZBIOyWEFSBKaG44mKD76P3z4HswBxCRz_7AZaPWf-svPAyyPpcHjl62eIoNOAP0f8aTTh4oaJkrMFy2EkrpMGUkGaRLqHAD8oPiOYHYrvGCJGP3Z6SRCXhxiGSl0jCWRguPRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
🏆
تصور کنید توی اوج هیجان و استرس فینال جام جهانی بین آرژانتین و اسپانیا؛ نتیجه بازی 2-2 مساویه و بازیکن ها رفتن برای استراحت بین دو نیمه، همون لحظه بیژن مرتضوی وسط زمین:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/100505" target="_blank">📅 17:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100504">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e5386b5fd.mp4?token=MgtXxp38utDy6hhpF3-vqTH9mJP8PpMSiWVKHIL5KMi1RXHCunYhPCOwZGjrUq_qz7gSfQKZRcaoHoCDfqCALG1otc8gAg4cM3vfejClglymlnuHVjxNRaHEBCB28VJCDSx3wxLawEjBkLmUAKfX2fx-i00h2cb61qCETYj4JVhAEXmOf4eXtQPrw479y9MoQx_V1M0JdeniEQ6BRCcKb0IaT0VsdRVc52Kfv22kX3SaYzCIhKO5n1vU_mDI1n6hs-n9F9Je8P5sBfTULVK4pjNJh3pSnxlop-L9GBXbaBV4-swbgCJ_uNI_O-jnI7eAByqsYFi593fStd_ZYuQzxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e5386b5fd.mp4?token=MgtXxp38utDy6hhpF3-vqTH9mJP8PpMSiWVKHIL5KMi1RXHCunYhPCOwZGjrUq_qz7gSfQKZRcaoHoCDfqCALG1otc8gAg4cM3vfejClglymlnuHVjxNRaHEBCB28VJCDSx3wxLawEjBkLmUAKfX2fx-i00h2cb61qCETYj4JVhAEXmOf4eXtQPrw479y9MoQx_V1M0JdeniEQ6BRCcKb0IaT0VsdRVc52Kfv22kX3SaYzCIhKO5n1vU_mDI1n6hs-n9F9Je8P5sBfTULVK4pjNJh3pSnxlop-L9GBXbaBV4-swbgCJ_uNI_O-jnI7eAByqsYFi593fStd_ZYuQzxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه مخ‌زدن در استادیوم‌های جام‌جهانی
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/100504" target="_blank">📅 17:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100502">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b77728c3bf.mp4?token=GPZbvyZAmuHH-FVaZCgABhjgsZwwPbCJ0F7-HQMai7ZxlcW9u7Bwsv4fqOcvLljES5SdO47BRJ7D5erGfFWVPf_YSMOi82pIQlJCtt_xmMa-eZWZmt3z6TBawQxCctDm-Dav0zvo0QY5PZv4k10FT0o0ze-K5UDND0Xe7qK4hDEsqVwGYrxnSsVyrILGfvuvVGw_ymQM7Tm0ECUv5t4QE2oUyt0oWBjzKBZiSdpJ4zgv1dWP39yChaz3TFc_WQ2zn3Hs3iExxSulwfEby-raicH6KBrbpowKDmE91u7PHwlIdD1gSfupQIE4PmlQINvnYL8FE4qvzXCHhnsllJ1cWzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b77728c3bf.mp4?token=GPZbvyZAmuHH-FVaZCgABhjgsZwwPbCJ0F7-HQMai7ZxlcW9u7Bwsv4fqOcvLljES5SdO47BRJ7D5erGfFWVPf_YSMOi82pIQlJCtt_xmMa-eZWZmt3z6TBawQxCctDm-Dav0zvo0QY5PZv4k10FT0o0ze-K5UDND0Xe7qK4hDEsqVwGYrxnSsVyrILGfvuvVGw_ymQM7Tm0ECUv5t4QE2oUyt0oWBjzKBZiSdpJ4zgv1dWP39yChaz3TFc_WQ2zn3Hs3iExxSulwfEby-raicH6KBrbpowKDmE91u7PHwlIdD1gSfupQIE4PmlQINvnYL8FE4qvzXCHhnsllJ1cWzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
قیاسی: رگ گردن میذارم که هالند لره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/100502" target="_blank">📅 17:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100500">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mlPUFoZLOGzXhPfEgL911uGYR2kTNrz72fM2LrXh1HjUuwYawbya9Zy3cwu3TqU4yQyw1hrrD_Vb6fIYhy0NgQSo92nw5G3tOImIVKzgTL1q8d9YibYKZ7iyd1VVrkN-FEquz9KHcLBhhFCLFwWajM2vIRCRMEfFB3H8Z3rfYZ_yVHwlxbvf2ypDWD-E2jqr9FBTW6auJcQKGGqLPep1mpQoUq35Qv6bMJuHP4IDkiAb-zqJCnYRb3pIm3TStVE5NBng40ATBrMtTL4Qh8fWIngqcroZdAY0P3F9N7jg974sCkcoPU1IcdutWk4MQPuD50L_kk683B-3lr8DvpfIQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nygSx4LEqycSAbEUKLNnzpFGsb87iMqiZJwE2uuD-OfDOGlTLmCr79rRBqTlHxvhfHL9y-E7AzEYkSPjX4T0R2XIgbPzn8VMX_5IGsJgqiwrCaITDISlvtDnonnxcExMDFnEGdD13hd9RBDHkMInDMum3jaD8o6gNrmYltqt75JPpsmFLgvcFvkhsaqmu9FUDjIgr2h8IW4Zc_seRWI3ZVNm9HMqaMH7j048P8beBN8V6F-1W-514L4BRXvi-UwbrDF7tBUOTIUDGFIgNmj-vL7CFA6DTwm8OrjlUiVQVmfA2wpWpFiWEalDl4uDwc6jBvB6szDN2_o0fRJbOYFmlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مینی تقابلی که قراره روی سکوها بین داداش یامال و پسر انزو فرناندز داشته باشیم:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/100500" target="_blank">📅 16:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100499">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCSBck__x5LAioM5UXWS6pD7DTIQKnTbyR_x081YWjhgw1hatBwbEIntucXVFlemJHpyhtt601bDQCuHbv4dH0Jpb7yrMvi1Wj5EhO1gfhsD1sSXB7NIwNUXA7iv5A8jUdUnpZvSdNoRUAdogo0DsWME0DjPD9jIwvHqaRAj0cNoTfe07wbyf6SaUndgUW5KRwAgpSI6LekTMaLIemZa6BMMn0r65ITT-1X9n0NNkiCest8ULb3cXYyXbCVkIP5GWogGcO188dl4RLAkCP6YZTmeXB9ooZUXnI6TfV9zhoPTvg5hN10nD0W0FusVXA6BpcZ2ykGwlFhjmyCz0BiMwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
الکسیس مک آلیستر بازیکنی است که بیشترین بازی را در تاریخ جام جهانی بدون باخت انجام داده است
11 برد، 2 تساوی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/100499" target="_blank">📅 16:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100498">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HrvtrRcHL1C5qnoG-B8Cxy8eyXUWDuQGaewQqWJPxoOAe430viFHKlRfL77YlzYmOkYRvYreyySZX9FJDhAHawpDYTV9OWFl-m72YygrNp2KQ4ik1B9ByfAgRyzD98EP_GehkNsMMDm5N9qCem_FaaMxBZ7UybItftupPN_oGki61IJ1w-MLfGu7y7l1vsmKssljPOkdu_uU5wB_vIeGBbPZbrXNAw4GtZucCHOeFCa-DLISo61XWW1XCspkdQd9xcNSJ_Iyxws_RYRk2X0X323811cpK0rqwPZxbs_oa7NiBMzUpaNT_qQXqK6JlbOn1GEy9wQQfCBQEvb5UCycMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
رومانو: سوبوسلای مجارستانی با لیورپول برای تمدید قرارداد تا ۲۰۳۱ به توافق رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/100498" target="_blank">📅 16:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100497">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef12f755c5.mp4?token=MiUingkuGqkoaB_qhqxX7WVAI3jTpnhCCSZAHY4YHbYJqDaSORJjqhgxwhMabPzC_z08a_6UnzWZyqGTSJKd-rErOGu_xT8bYBZLUhNJymFoTrcIkJV3B3cTjs0wNExmNMKXMOenu1EHv6DYq96c9Oc7_rnmaXZv9EddzoEKV4oQEWBI228T8CgBZS_mRTfk6OJ31NZ3caLZRCoADL1uuX9YLJ7qi3EuXdM392LPHrNAjcocC39VcPpmqYOox5-afMuB7bkl0oOt31iogY8DGE1K0CvFlzUbZ6LPONBHJr9z0aPnL_E22KJG7Uh5pYBret82l4YqHFPZFP2UcoZXgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef12f755c5.mp4?token=MiUingkuGqkoaB_qhqxX7WVAI3jTpnhCCSZAHY4YHbYJqDaSORJjqhgxwhMabPzC_z08a_6UnzWZyqGTSJKd-rErOGu_xT8bYBZLUhNJymFoTrcIkJV3B3cTjs0wNExmNMKXMOenu1EHv6DYq96c9Oc7_rnmaXZv9EddzoEKV4oQEWBI228T8CgBZS_mRTfk6OJ31NZ3caLZRCoADL1uuX9YLJ7qi3EuXdM392LPHrNAjcocC39VcPpmqYOox5-afMuB7bkl0oOt31iogY8DGE1K0CvFlzUbZ6LPONBHJr9z0aPnL_E22KJG7Uh5pYBret82l4YqHFPZFP2UcoZXgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این جام که نشد ایشالا جام‌جهانی بعدی بانو
🎈
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/100497" target="_blank">📅 16:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100496">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efcbbbb391.mp4?token=YxewW_VPjh8ZM6SKGBINLRDMTSdwZRxvYmtCzaLBMZLq0o4Rk_lA4HuoXYRpsd2tsT_BA3Vdlbs64cszORyjyjzMvPH-P8JNFWrIiQiuDiPvGAnhSjTgGyj-gpSwmAqYcP0RCeIES93qWOSlCAoheOnKzYBHWbt4ZqCfyMF73gkZ6AhLaVAOSilm7JP_eqr2Bc8ZNq7LI35qYSX3IV5BTH2G5pjPv4UCg2ZceMEGn7BGkdTDBuzYSLnG19Ogrwr33ojDx-4fRWB5zR-0qm1zmQhM7NQ46SwcqlhGXlhVyMNpj90JiVLAvt4EqxQqFRUxev79O3M7nWIgTtHdzbLQcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efcbbbb391.mp4?token=YxewW_VPjh8ZM6SKGBINLRDMTSdwZRxvYmtCzaLBMZLq0o4Rk_lA4HuoXYRpsd2tsT_BA3Vdlbs64cszORyjyjzMvPH-P8JNFWrIiQiuDiPvGAnhSjTgGyj-gpSwmAqYcP0RCeIES93qWOSlCAoheOnKzYBHWbt4ZqCfyMF73gkZ6AhLaVAOSilm7JP_eqr2Bc8ZNq7LI35qYSX3IV5BTH2G5pjPv4UCg2ZceMEGn7BGkdTDBuzYSLnG19Ogrwr33ojDx-4fRWB5zR-0qm1zmQhM7NQ46SwcqlhGXlhVyMNpj90JiVLAvt4EqxQqFRUxev79O3M7nWIgTtHdzbLQcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
علی‌آقا دایی که میگه بخاطر مسی آرژانتینی هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/100496" target="_blank">📅 16:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100495">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDYn_8AjvM17dlnMPhYQJJIuiFH27f_S8Q_h03xF-G3FK9qdxYde_mKlKtnMCD9U3AxTnsP--tLsqiUUvqAmm4qiYs-eMtd9Kg2sL-ullrbHcf3AHdipqn_g4Qpyj324bzn6n-pO5KqPaPoh99ssjQP1pzE99-XIbO3Q-mZIVuu2y2oOQu_p1651fMOJ6DsLxAIPh_N_DjDlML_ZPwPUDvxyvotQWzaErYR99uEoOC1m3_puuJ3UcpEKiVqWPOusWyGECEy58uXBXqa6vAYl2wJpYiEtruK15hd8fstTDI7cfb7UDJoyEuklzC23yhYVeh9MtbXC9DwLyoataRHA_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری دی پائول کنار مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/100495" target="_blank">📅 16:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100494">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cb2da8dfa.mp4?token=Bt8gYX8MHRqxo7ZXONIr6ARiSUH3QhQZkEBZozitJoNcTYg4XDKz89TNOSfYseH7umtiu6U1uqpnha3Yto4T_4tD_DZC4EFVxJ40boMMdgV2_mKi_lJmjMSipYE-ysi7KvgtU3YUOGUXEn1VqiZW7wz-Oh1kcNaB9q1PXHrfM1Xdst_La3ENlmlqrf1qArBKrMAN18DTGPtdTnAILC9Lf3V-3RtAiqgeLWTH_1d-8USURs9r31VuviIqqP-gAm6r1hFtc-l69XiX0DdEMZLcrCzXxEjdSKF0PGAcvAUn7-PkEgVzndN2T9YTwNVWhhmk9UA4JfmkLjSVkbXi-8M8OgmrJMpnmncL2a1wAQ6JbL9pyBh0vUBWO2r4GMuLtepm32n0ATZ1T3EyeDp4646CfpyVrBdk79hIXh8pFb6m4CJvThNnwVS5WdRkKDB0q_1LWkwojV4pNsGwBNEvuAunuhvFC4IzsB_MyNpsqMMXJ92sO-ukeXysU9MyWq9D61ArVpCcBemE9ReQTgEAa5qK1y1Gm4ttLadlIl5ZripQUo-IqxTbb2GIAgHd3RARA3xg-gf6l-J_thlDDC4eQe4aSeAq3TnZXoDGwYjyUBsToiz6wBwWgkiSVuqZBaz_Kghq-oulmbWCLG9cPS3-USuoZhCpkDsFriFecuH9-DZj62g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cb2da8dfa.mp4?token=Bt8gYX8MHRqxo7ZXONIr6ARiSUH3QhQZkEBZozitJoNcTYg4XDKz89TNOSfYseH7umtiu6U1uqpnha3Yto4T_4tD_DZC4EFVxJ40boMMdgV2_mKi_lJmjMSipYE-ysi7KvgtU3YUOGUXEn1VqiZW7wz-Oh1kcNaB9q1PXHrfM1Xdst_La3ENlmlqrf1qArBKrMAN18DTGPtdTnAILC9Lf3V-3RtAiqgeLWTH_1d-8USURs9r31VuviIqqP-gAm6r1hFtc-l69XiX0DdEMZLcrCzXxEjdSKF0PGAcvAUn7-PkEgVzndN2T9YTwNVWhhmk9UA4JfmkLjSVkbXi-8M8OgmrJMpnmncL2a1wAQ6JbL9pyBh0vUBWO2r4GMuLtepm32n0ATZ1T3EyeDp4646CfpyVrBdk79hIXh8pFb6m4CJvThNnwVS5WdRkKDB0q_1LWkwojV4pNsGwBNEvuAunuhvFC4IzsB_MyNpsqMMXJ92sO-ukeXysU9MyWq9D61ArVpCcBemE9ReQTgEAa5qK1y1Gm4ttLadlIl5ZripQUo-IqxTbb2GIAgHd3RARA3xg-gf6l-J_thlDDC4eQe4aSeAq3TnZXoDGwYjyUBsToiz6wBwWgkiSVuqZBaz_Kghq-oulmbWCLG9cPS3-USuoZhCpkDsFriFecuH9-DZj62g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
تسلط کامل فیروز کریمی روی زبان انگلیسی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/100494" target="_blank">📅 16:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100493">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8ceabea2a.mp4?token=bRxNrwU9kIBpB030PaZSQtobPbNI_T06G0GDGwsLAKXfcQTP6Vr7WObNKPO_9vLx7-ETeXuhy6-kg-iMBuWVpzztIbIamQegWCQqziV2GzsUtWjfc0RvhuYkZdY_aVO8EvnP4j5ANVdUwUhnCcaVxqXeV6KscuJ3PyyVHdj3Y5MkBFXa5jYbPjrwRPIECQGUI32Nju10WHl-Zbjb-yZhtuvkmK8PkNVAh2aYiYJhLjvF3tXGfATqsLHhZKLACiYu50L4Ti7pOeyEcL3FkO7XjLQSEfhBNTSbqD8TsXtR6wA7UHi7bPhtaIte5M2uT8umg1kgoX5bqI0KVszl8eRIBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8ceabea2a.mp4?token=bRxNrwU9kIBpB030PaZSQtobPbNI_T06G0GDGwsLAKXfcQTP6Vr7WObNKPO_9vLx7-ETeXuhy6-kg-iMBuWVpzztIbIamQegWCQqziV2GzsUtWjfc0RvhuYkZdY_aVO8EvnP4j5ANVdUwUhnCcaVxqXeV6KscuJ3PyyVHdj3Y5MkBFXa5jYbPjrwRPIECQGUI32Nju10WHl-Zbjb-yZhtuvkmK8PkNVAh2aYiYJhLjvF3tXGfATqsLHhZKLACiYu50L4Ti7pOeyEcL3FkO7XjLQSEfhBNTSbqD8TsXtR6wA7UHi7bPhtaIte5M2uT8umg1kgoX5bqI0KVszl8eRIBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
آخر عاقبت گنده‌گوزی یه بچه‌سال برا اسطوره:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/100493" target="_blank">📅 16:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100492">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0505b98db1.mp4?token=G_80stBd5pzClj4ABSIUnjMQRcZ2oLzE6ahDzrjwy6v9AbQ3QnOQfkrX6vvUIj-z63reDmthAT1EKQ7Lh6dwRw7cKckvh432GrbcAMHiGBQIeakFqwc9xDaHtEiOg6338O_LNThWz761ZZRC80LZY7qmwGI5-obWhWBN8i9QxLo9fUSSEOhSjoibBqqhkydSwZEOZJ-AX3z-5k8psuyguPPyh0pQlQTRzUagAa4Y3h4Ip4BJcjtAps9DKqBy-GYhqqirqTrc7ErlhKXo33l3lbfp6woQLwPQhZIyXTTUP3Uoo_AOsMGw38TMoQ_ryPgtcHb76GjcDp2N0E9fYGYBQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0505b98db1.mp4?token=G_80stBd5pzClj4ABSIUnjMQRcZ2oLzE6ahDzrjwy6v9AbQ3QnOQfkrX6vvUIj-z63reDmthAT1EKQ7Lh6dwRw7cKckvh432GrbcAMHiGBQIeakFqwc9xDaHtEiOg6338O_LNThWz761ZZRC80LZY7qmwGI5-obWhWBN8i9QxLo9fUSSEOhSjoibBqqhkydSwZEOZJ-AX3z-5k8psuyguPPyh0pQlQTRzUagAa4Y3h4Ip4BJcjtAps9DKqBy-GYhqqirqTrc7ErlhKXo33l3lbfp6woQLwPQhZIyXTTUP3Uoo_AOsMGw38TMoQ_ryPgtcHb76GjcDp2N0E9fYGYBQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای عمو ها اووعو اووعوو رو بخونید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/100492" target="_blank">📅 15:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100491">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zuh7bEUQG4OLPo1pQWMINfwLnh_BPqKbgcbfJTdl8c-t5kn7hjtOHDyCzXaLorPi8V7D-hXG6pjNqWAIynFOSOs5PrMh9B0Ok5tqYMnkagmsGYfMeaKFqsigz9awEh-XYBCMKsxDwtkIAWcMPhdVUGOcYqTH4wzIQDXv-nhrIgZy9o85jUGRxQoJPm3gZ9bSLi1CWryxfvTif3uGYWA6_SlHxpf0o_lxosLrU3y3UFTQRJhWLitjMPLqjZeyMFJG6Nb-ahP9H0f8rgCEylrbsbzRMusm3VXJkXsBZp8hJXoUMlecaJedflq0V5r15ci2OT0rJVCbwkl_hh-5aCCjcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦁
🇦🇷
آرژانتین در مراحل حذفی جام‌جهانی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/100491" target="_blank">📅 15:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100490">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UncF6lIUrhYAm3oV3be0PxVtI3CYe64pTzoseHB8k-L2A7-Vq-UNDqTb3PfbE8SW84Egx30pDW4FZ4fXFd5UJLRVYCHmbW-cnBioUQcTytOymU2UyKZ21SQWL9kLp6fizhJSIESfPUkvgoaqZ2zIRTSbcrg0qrUVi2qJR6V0Gb3Fp7WRUc0eQYldFWAA8nAWQT2iob0DKVAWMlF08CV-IcI0ee1QXoQsNsM_o17p3iqcBXEEcBq9ED_tElex-58vM731PTfDcCqLJrU4XZC3FNp_5B08WXoJ63TxoTgXcvCXZ7TrIGqYJM6vOq_bL9ww6t4ZXbnKZ5HOikYmX_aWNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
🏆
با صعود به فینال جام‌جهانی، آرژانتین با عبور از اسپانیا صدرنشین رنکینگ فیفا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/100490" target="_blank">📅 15:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100489">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYN5nsVCu8LBNJCHW5FzG-8cXpIVWAJEHtX20C7uGm3XsAqTodJiCkdzDqS3clvo7OQKqfMPGSblskCZ5xNyKgbygPlClEztDlNG39dndHLNPzDmaOO3X5f_mtRBAAB8ImyrNlgnXpBagU2ayVXhqKLs0VDleTH7hPl0qZFcFLmzHv435MS-xNbWaAf5RziRk8VUhZZLfWXeca9V3Yhw_BCXHRUOVSQRnjwtPYmfvHM-p9ya8JLtLKSlnYRrw21L6MhOMw0Pflh3e9Pta-P1UV31T3lzK4F_6_liDlVtdMUOZnykYaSg9A-PnPLQ8xPSiwU5eZ0OkQpIl6D-QQBPBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🏆
مالکیت توپ دو تیم آرژانتین و انگلیس بعد گلی که گوردون زد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/100489" target="_blank">📅 15:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100488">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/100488" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/100488" target="_blank">📅 15:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100487">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/100487" target="_blank">📅 15:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100486">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd9b7cbb4f.mp4?token=Q9pRyH-eaALK85vUEFFly_uuJeMHAjZTpCWflv2W9Pkd7MeOoWbOj4fq7V4RRlDuzlsUEvGjdaZc2ToZk7W7yR83n19GntHWNRScun37oCAYmJ0y8l7HyzCTvyG5uRtI1MpqhH-0ZTT3yJ2VfC7h690C0kkbruHVnb5EoDC4ulaAltj3jSaaSp8SldCCt98Ah-1FYZj8efTchM4h4J4O4q5Rd1W3GPmjtwMXm8YGJczRq2BHeXQMSXP8sbU4F6e2zGNahdCLYgLPSnGIUgLcB2Lp61nLqxeg8VSK_KaZG8Qxn-5_LFUWkgX6iibfhdiYDCj0SJ5f63DphOzZBzU1ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd9b7cbb4f.mp4?token=Q9pRyH-eaALK85vUEFFly_uuJeMHAjZTpCWflv2W9Pkd7MeOoWbOj4fq7V4RRlDuzlsUEvGjdaZc2ToZk7W7yR83n19GntHWNRScun37oCAYmJ0y8l7HyzCTvyG5uRtI1MpqhH-0ZTT3yJ2VfC7h690C0kkbruHVnb5EoDC4ulaAltj3jSaaSp8SldCCt98Ah-1FYZj8efTchM4h4J4O4q5Rd1W3GPmjtwMXm8YGJczRq2BHeXQMSXP8sbU4F6e2zGNahdCLYgLPSnGIUgLcB2Lp61nLqxeg8VSK_KaZG8Qxn-5_LFUWkgX6iibfhdiYDCj0SJ5f63DphOzZBzU1ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
لیونل‌مسی به فینال جام‌جهانی بازگشته‌است...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/100486" target="_blank">📅 15:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100485">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6732c2de4.mp4?token=gjAmlo150HDhRAco_PJdf9PUBPh1zhPvdw8lH-7zvDaUrAxnC72WrZVt6YbV5r4x9MhRDgBL0TVhzhmlFK9De2U4JmPV5Y4wxyjDihbTq9sndGT1s8HJulwbyRHSB2sl96nV_GRgwHzEIRvpZRhLWIMK8Nj_IrEYJ76rSQSF3o_z6a2iEPR2bh-LwCRBfJz9LUDQO0Kh74HpCgbed7-rGy_mdbn4Pbjlp9RPabl97rreqMFssu0zUE4RaF8OjHMFRjQQ7nRjxSXbuUPZT2UXog7VkrRqa3YyO-nOcagj7CvJUCFXeerNCjy9YYYateM4pMSRNaYFVB8NzMXd22J9Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6732c2de4.mp4?token=gjAmlo150HDhRAco_PJdf9PUBPh1zhPvdw8lH-7zvDaUrAxnC72WrZVt6YbV5r4x9MhRDgBL0TVhzhmlFK9De2U4JmPV5Y4wxyjDihbTq9sndGT1s8HJulwbyRHSB2sl96nV_GRgwHzEIRvpZRhLWIMK8Nj_IrEYJ76rSQSF3o_z6a2iEPR2bh-LwCRBfJz9LUDQO0Kh74HpCgbed7-rGy_mdbn4Pbjlp9RPabl97rreqMFssu0zUE4RaF8OjHMFRjQQ7nRjxSXbuUPZT2UXog7VkrRqa3YyO-nOcagj7CvJUCFXeerNCjy9YYYateM4pMSRNaYFVB8NzMXd22J9Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مردم لندن درحال تماشای حذف انگلیس از جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/100485" target="_blank">📅 15:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100484">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0519f41eb2.mp4?token=bk2Z1T8NNF6FSArSojumeUdaxGLwwQiHixHRoQvn1eonlvG4OT_s89XB6AlxvgyJzaYLJjeg4xIqzwdnEHD4KEvLKnqTxUGaSLaWSuipWZ6_t-R3cNt5QjJib8xxWaln5cYtPKswZWO6W2y0qU1zm-P8joXSKOWsoIs6d1CIffjMY-FRVVFjpI_YO0TapyUkQPUbGoQBpEi9MpavdmtlgsLgPYvppYi0fpjYQjDELq6dpJurVlJcZWjp9UDRvZ0xD88gxiFL_YXez3Jam7obszZoLFTUYYYdJtMhg7LURWAGeQl6VmGMtU8n-cGp_FhRG0RpPYTfVkMazzyaN67h_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0519f41eb2.mp4?token=bk2Z1T8NNF6FSArSojumeUdaxGLwwQiHixHRoQvn1eonlvG4OT_s89XB6AlxvgyJzaYLJjeg4xIqzwdnEHD4KEvLKnqTxUGaSLaWSuipWZ6_t-R3cNt5QjJib8xxWaln5cYtPKswZWO6W2y0qU1zm-P8joXSKOWsoIs6d1CIffjMY-FRVVFjpI_YO0TapyUkQPUbGoQBpEi9MpavdmtlgsLgPYvppYi0fpjYQjDELq6dpJurVlJcZWjp9UDRvZ0xD88gxiFL_YXez3Jam7obszZoLFTUYYYdJtMhg7LURWAGeQl6VmGMtU8n-cGp_FhRG0RpPYTfVkMazzyaN67h_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
جمعیت پشم‌ریزون در بوئنوس آیرس آرژانتین هنگام صعود این کشور به فینال جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/100484" target="_blank">📅 14:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100483">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b87eecf2d.mp4?token=TFGrEPjqtMn7AQ1-UD6Uja5vZKjNLyLfsRZ0YSz-7Ch3AQPtFm6jVLKLCgHjf5G3JUYIFursGbdITjZ4pTikNgCZOQlWH0sd13AbeOHslrRPxinPk7uxVJan0a8EYfSuOZcOYPa2fXkGJfOXvfWIzeRGz2fgdMvWCaMr4ewDonSnvCKGigbnCpCxCm2mBt1Mavklwxz6BslYU7epYB5kG2GCqSGdjb1oe17HRljyaLjCfbdEXBKqbO5KmkVhHRmU3rlnaXy6XuCiMhZeA3bMITofLKwooy-FaZGH7aEn-PUQ0OqiXVLXZR3KUDuZprTget7MgJqyezRJMk0YABZxSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b87eecf2d.mp4?token=TFGrEPjqtMn7AQ1-UD6Uja5vZKjNLyLfsRZ0YSz-7Ch3AQPtFm6jVLKLCgHjf5G3JUYIFursGbdITjZ4pTikNgCZOQlWH0sd13AbeOHslrRPxinPk7uxVJan0a8EYfSuOZcOYPa2fXkGJfOXvfWIzeRGz2fgdMvWCaMr4ewDonSnvCKGigbnCpCxCm2mBt1Mavklwxz6BslYU7epYB5kG2GCqSGdjb1oe17HRljyaLjCfbdEXBKqbO5KmkVhHRmU3rlnaXy6XuCiMhZeA3bMITofLKwooy-FaZGH7aEn-PUQ0OqiXVLXZR3KUDuZprTget7MgJqyezRJMk0YABZxSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
فریادهای رومرو بر سر بلینگهام بعد بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/100483" target="_blank">📅 14:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100482">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f72bbd0a4.mp4?token=e9Mu8UxhU3QqYYGn875ospyNXir3uAVLtgMzl8kvhEcySJXJf-j2ugEVp0deQaWRzhBxAHqaeJ_zq87fkjHMma8Tpj51ylMyQhFtUd7QTpCZ_XFrCfr-VomGyApZNXSYUPS-cZPiOvBM8lmIXOMEmQ0WLr7y5qx5h0SKoQ0n6xpnWieXewBzC6I8yzJXipfdejV19LHgMY0aVlon2yt-VYwnCDlXOjQtv0yad0W8xcbL9om7AuLzW4cg6Jq6t3Y0TLlcpWiImcPJ3Zok_eRmq6sYemhGGO7pErU0Ko53qVq96UWpd_Aa5EErH0HfxBTQikGWWOw227Cud_LPstxaGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f72bbd0a4.mp4?token=e9Mu8UxhU3QqYYGn875ospyNXir3uAVLtgMzl8kvhEcySJXJf-j2ugEVp0deQaWRzhBxAHqaeJ_zq87fkjHMma8Tpj51ylMyQhFtUd7QTpCZ_XFrCfr-VomGyApZNXSYUPS-cZPiOvBM8lmIXOMEmQ0WLr7y5qx5h0SKoQ0n6xpnWieXewBzC6I8yzJXipfdejV19LHgMY0aVlon2yt-VYwnCDlXOjQtv0yad0W8xcbL9om7AuLzW4cg6Jq6t3Y0TLlcpWiImcPJ3Zok_eRmq6sYemhGGO7pErU0Ko53qVq96UWpd_Aa5EErH0HfxBTQikGWWOw227Cud_LPstxaGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇦🇷
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آنچه در بازی دیشب اتفاق افتاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/100482" target="_blank">📅 14:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100481">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPUJREBhKzcJkM44H36Nm-RQIQN18fqQuiz29EAxLZgRfO4lKluhoytpNHHn3AWHvCqNUt6szNXkMOKXoG2SPJcqKBB69cfFT3ml9-Z4wRmMmzgFvkY5wzWVfGrlogeISOw4HGNXlY56qPoiQ7lLEKy2DCk64D_yJJKCEuzlnoM9Yb_T4_UQdGb9cSA0M_uYBU-c1fmAxPyTQnW4QM2w38-mbBgTm0uRnkXRnxKCLcyLPt3N_45WzFlpSBAigh_r2OkjW0-ipl7A3XeCwqBivvOeF-1KxngIbR6yvzXHz5RRiWnF8mZpvpI4YHMacZJRm0yh_-gATw1_ix03kJ-ODw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
محمد مهدی زارع، مدافع میانی ۲۳ ساله احمدگروژنی روسیه، با قراردادی چهار ساله به پرسپولیس پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/100481" target="_blank">📅 14:01 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
