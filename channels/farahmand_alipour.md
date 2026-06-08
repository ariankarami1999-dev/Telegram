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
<img src="https://cdn4.telesco.pe/file/LwVhhoeNiDAe7HKkaMgAjFJxme7TH6Ljr8xjrIAEfAxDv6mk0nIYUY02JxlpJwPjarQWsg_Wp07Pq1jRQM6R-fNe6npJlFcYlyBJfKa51QkWvplNOaRi6KZhy0coCntnIg0XQ7I4YNV_iP5s5EsmEMqKUxYOfleJisRqtYcOaGM0rkB5ZjoapxO-q71TFmQ1Ot-jpRuWft4zPkAVBHDE9HXu7eFc_9e-pUMsddskOWm0wmxXj6eZmwuXjv68VBHSb49DM2uGYt-JYF33k8s0DpwdOPmAQqq3AX_hOvRHw--i_snRzM-ognOtdAkzXBgEWY-Q7mhh2rEqz6J0kWwC1Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.1K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 18:24:47</div>
<hr>

<div class="tg-post" id="msg-5419">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSI6XhpcKhhyX-p4jUn3coWb6WKpydoMhMi7mOO16YKillKOdrHM-6XRWYluAVn4hMh5CRSV49uugBKzhEm9A8pAONk2iHxv8bGf0_W44BB6C7tTDjg5wQqUj1FoKJOor7iqXGIgXyV4gCd0v1KmTdTI29zhB_5QDooB_eCELZgD6YCE7ubjiKnefDgHTlDeeoLlYkFKvKDWRxkxcmgyyG_l-aJ9sQp-YTVtaAY2zJ2f8z_aN9kR6pTc3Qu0Y7K5I-FmthVkrF8p7qKAb_pj-ROWk00UAQsSCaiiXBFT2IE-kAk0WoWO1K1n66X1AyO9lf6xs5ZX7a2K7l3iM0r5BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farahmand_alipour/5419" target="_blank">📅 17:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5418">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=BnbsKhzi1uiA3fFYbM5vHbN9SoHA2KZa85c430MOdIBFwKFZgibmk-5rJUdnhxgfUA1YGHrpxkt4y13S786SmoDPbd_gj0T4Fqv2j1o5Jf4uf95LTrIyRX1ArVoacB7eWbQs67HN4LwB9_8YlTdvRxcQ7FK0_aupNDYXgfxwj6fEPFzrnRpQB1I8-wGZzT0b0T-xMoC8bzOiHK8JLj02Uz9YTiwPb-csYvIvLOX0bxYSs_WuyPTGpzNZPUOAAU-y8hHtSeVe4g5djfoWnFwTqBArRnh4Gt8GOT-1Vc6ksZ3dpZ0B_Wvdn3-Wxx2Bvyl9VsnDji7q-syjshAiPZEQUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=BnbsKhzi1uiA3fFYbM5vHbN9SoHA2KZa85c430MOdIBFwKFZgibmk-5rJUdnhxgfUA1YGHrpxkt4y13S786SmoDPbd_gj0T4Fqv2j1o5Jf4uf95LTrIyRX1ArVoacB7eWbQs67HN4LwB9_8YlTdvRxcQ7FK0_aupNDYXgfxwj6fEPFzrnRpQB1I8-wGZzT0b0T-xMoC8bzOiHK8JLj02Uz9YTiwPb-csYvIvLOX0bxYSs_WuyPTGpzNZPUOAAU-y8hHtSeVe4g5djfoWnFwTqBArRnh4Gt8GOT-1Vc6ksZ3dpZ0B_Wvdn3-Wxx2Bvyl9VsnDji7q-syjshAiPZEQUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ : همین الان زنگ میزنم به نتانیاهو تا بهش بگم که به حملات جمهوری اسلامی پاسخی نده!</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/5418" target="_blank">📅 16:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5417">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=nChgvLDRQG6hVrZjQid8Sho2Smxds428ZMx0CnzlEM3cQzG6WKWQEqadQWyIXUb0Upu7a_H2EtRA8rX4rjHEkV0Kpo2GrguudkfJss0LXWfkDgOodvDz9mOs7XDHSin7t-IthzAahVXJZVjML797RIvssLmc5hb9XMt6bO5NsCrrqrCi4aiZpcIR8TKzFPVMHKSqS0sqVqX-WfyQFI3BtrP8mIf-LSO70l-dpscbenMabzWvO7utE0r201AvFEQVEtH7P1mr89WXESwQu47xuvf7zhg5aOqaVm4fKrCJWtTXgaydetzrXDigPZ0zjFhOdZjk8yrYY5C3M5WeB03WdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=nChgvLDRQG6hVrZjQid8Sho2Smxds428ZMx0CnzlEM3cQzG6WKWQEqadQWyIXUb0Upu7a_H2EtRA8rX4rjHEkV0Kpo2GrguudkfJss0LXWfkDgOodvDz9mOs7XDHSin7t-IthzAahVXJZVjML797RIvssLmc5hb9XMt6bO5NsCrrqrCi4aiZpcIR8TKzFPVMHKSqS0sqVqX-WfyQFI3BtrP8mIf-LSO70l-dpscbenMabzWvO7utE0r201AvFEQVEtH7P1mr89WXESwQu47xuvf7zhg5aOqaVm4fKrCJWtTXgaydetzrXDigPZ0zjFhOdZjk8yrYY5C3M5WeB03WdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فکر کنید
این ویدئو رو خودشون پخش کردن !
اخطار سرفرماندهی نیروی دریایی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/5417" target="_blank">📅 16:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5416">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اورژانس : ۱۴ نفر در حملات اسرائیل به ماهشهر زخمی شدند.
لغو تمام پروازها در سراسر کشور تا اطلاع ثانوی</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/5416" target="_blank">📅 16:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5415">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=Nsbk_2QDXA0ACkEs9ZyYceKGmg6vTehgVvWACIAp3EHSChHQo2ghXVu88O8_o76HGqqG8PFZ_MQHU7jpjTgaNBFTCXE-91p6DUmul1kC-_HWd8yp3_2b7RlKM3H_bK0fiT7R3imNBl1aUUv9CPO2PARrnV-7BHU8i9rCimUJem-nQs9xHDgtZ-my78txVRZp_FEXiCKpq2bDWh3EL6rjWjFEgd3B_29RlWUUqfrClmZ64tMgDyqOP7QIj3wm7f78vljj1q2jRIZX643yuSgQWW85OwXWX8H_mnCpgLEtTMYXsv4JDKcg9EXT8Cu96xd82hXICu8fU_Z0B5kNGnvnjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=Nsbk_2QDXA0ACkEs9ZyYceKGmg6vTehgVvWACIAp3EHSChHQo2ghXVu88O8_o76HGqqG8PFZ_MQHU7jpjTgaNBFTCXE-91p6DUmul1kC-_HWd8yp3_2b7RlKM3H_bK0fiT7R3imNBl1aUUv9CPO2PARrnV-7BHU8i9rCimUJem-nQs9xHDgtZ-my78txVRZp_FEXiCKpq2bDWh3EL6rjWjFEgd3B_29RlWUUqfrClmZ64tMgDyqOP7QIj3wm7f78vljj1q2jRIZX643yuSgQWW85OwXWX8H_mnCpgLEtTMYXsv4JDKcg9EXT8Cu96xd82hXICu8fU_Z0B5kNGnvnjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل در حال بمباران جنوب لبنان
- برج الشمالی - حومه صور</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/5415" target="_blank">📅 16:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5413">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cf3PHh3LtMSh_zqSPUpUCbFpArE58y2EZBDd3XBrKfGl7acfotyUSb9BJIkQ7Xz8SZ-nHyWzRRDsP48UkH4KYpcgokq73jrbnJnuN-sHC-hADvwAOEZxPUNR1CAqeVvc0bzgL0JYyybxeFCQAk0wvOvNumPJhttHPbgQ9Kgh539E7MZW1B1yaRmJzZyAhEpXInQM2n3z2slnuB1tb-ETkY0AePZv18xGW70nWcSt32BPIVtgndQjaSJG5LSrS_gQPs_ZUbT-sHZxuyv-kNegwEs7yh_7kmKf-7m50pBK8vhki0dcem-QpIvUDtXoj6Z1NNRHNENnK208F8Bf9aGATQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b-IdRHS2E1ilfJj-RAzHx3GTRIoC7AmweePIbohu2q-lhiuHCo0TPEjmomAv7rSvf7xP5U2ZP2SSdHGZxZfw_s_MP6NOvNQ0oJBLlhqMFHvflqZlensXogQPNJGD0VY-ax07bYrxUDGpvM5u0TZJrqTQXuPKj3aPC0KybNxIjWVfmVulZHuWZokT8fnnVsPfwHpE2HW8uYQhLFNzXgCqEyiRixp6oSuFM8zYwLgcZ394fxpKundMxunN8zzTyLDjuy8nACOjIWLX99idLCsbhA6YNGws7fUIa-2Rm_Xuy2oj24c5P6HoR6Ku6CJL7ULRuvf5OXgwL4ETUywZDXjPvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگه اسرائیل، دیگه به «جنوب لبنان» و به «ضاحیه» حمله نکنه،  یعنی موفق شده معادله‌ای تازه رو ایجاد کنه.  جمهوری اسلامی هم گفته اگه اسرائیل به جنوب لبنان و یا ضاحیه حمله کنه، سخت‌تر حمله میکنه.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/5413" target="_blank">📅 16:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5412">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
‏قرارگاه خاتم‌:  «پاسخی دردناک به اسرائیل داده شد و توقف عملیات اعلام می‌گردد! اما تاکید می‌شود که در صورت تداوم تجاوزات، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.»</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5412" target="_blank">📅 15:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5411">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/336071990a.mp4?token=LTUb9b5mqE0hl8kEKt3kILNwYvXrlo95PxWNDOp84XNG_IvZViwK6bCvucKxh_6CwcrtnurzOrbh9URrqx1PmZDcim4uIu5wsbjJz0VBugS5h9lYpKfKUX6m8PBX5i52x0B9rv0epik24RucTRON3wIM5iBqSostxJeJdA6bXft6ay2LMKuAGOyrpRQ86DDHPbq5m2ZUzvfvNnuAwukqDIxP5yKtPO4eXxwpLAOUHyjebwUPrwB0wihs4hO6S9IKPALqV7jKpwjuhZXyufF-NzcXGH_LZM5OzhVn1XN6niSRFfs9K1dLnzSSMuyYRzF9FkG1MGWEctNiKhGE56MB8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/336071990a.mp4?token=LTUb9b5mqE0hl8kEKt3kILNwYvXrlo95PxWNDOp84XNG_IvZViwK6bCvucKxh_6CwcrtnurzOrbh9URrqx1PmZDcim4uIu5wsbjJz0VBugS5h9lYpKfKUX6m8PBX5i52x0B9rv0epik24RucTRON3wIM5iBqSostxJeJdA6bXft6ay2LMKuAGOyrpRQ86DDHPbq5m2ZUzvfvNnuAwukqDIxP5yKtPO4eXxwpLAOUHyjebwUPrwB0wihs4hO6S9IKPALqV7jKpwjuhZXyufF-NzcXGH_LZM5OzhVn1XN6niSRFfs9K1dLnzSSMuyYRzF9FkG1MGWEctNiKhGE56MB8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از حمله به یکی از پدافندهای همایی غرب کشور توسط اسرائیل.
این انفجارهای پشت سر هم مربوط به موشک‌های این سامانه است که یکی پس از دیگری منفجر می‌شوند.
این سامانه پدافندی قرار بود از آسمان کشور دفاع کن (با شلیک موشک)
ولی اسرائیل بهش حمله کرد.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5411" target="_blank">📅 15:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5410">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سپاه یکطرفه این آتش‌بس و توقف جنگ رو اعلام کرد. نه به درخواست کشور ثالثی، نه با رسیدن به هدفی و…
این می‌تونه ضعیف جمهوری اسلامی تلقی بشه.
احتمالا برخی‌ها در حکومت ترمز سپاه رو کشیدن</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5410" target="_blank">📅 15:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5409">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
‏قرارگاه خاتم‌:
«پاسخی دردناک به اسرائیل داده شد و توقف عملیات اعلام می‌گردد! اما تاکید می‌شود که در صورت تداوم تجاوزات، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.»</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5409" target="_blank">📅 14:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5408">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7deb2f31d.mp4?token=LQWranoo6ndXSFHEh0-PwqCiChDeIbwSQdfbVH54-dWz0YjRPEIasiHGvtAO1pt8t6NllfMlupO29APp4k1Y9LflJnZBQpHQsVMgRTDOyOM-HusZ-Ix5hi6OC9a5S-dD32_UjZ13RUa88EW3tWHUDN7Cp4YYVh0o19Iy-M8Uk6iyVj90V3FDjz592rlhfJXqnZYuh-LMWOVoditb1-6c441rfCQyulbKLoeSfiXRzaarBq00XgVcX_EbNBfnJsAaKphQb4LMlt8CMxZcwcTpk7AiQADVxljspSgIgIGjk1srX_irIeasKFanHd2H7njuNebYCS7jOc0WucLOoz_E4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7deb2f31d.mp4?token=LQWranoo6ndXSFHEh0-PwqCiChDeIbwSQdfbVH54-dWz0YjRPEIasiHGvtAO1pt8t6NllfMlupO29APp4k1Y9LflJnZBQpHQsVMgRTDOyOM-HusZ-Ix5hi6OC9a5S-dD32_UjZ13RUa88EW3tWHUDN7Cp4YYVh0o19Iy-M8Uk6iyVj90V3FDjz592rlhfJXqnZYuh-LMWOVoditb1-6c441rfCQyulbKLoeSfiXRzaarBq00XgVcX_EbNBfnJsAaKphQb4LMlt8CMxZcwcTpk7AiQADVxljspSgIgIGjk1srX_irIeasKFanHd2H7njuNebYCS7jOc0WucLOoz_E4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله به یک نفتکش هندی در سواحل عمان!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5408" target="_blank">📅 14:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5407">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">چرا ترامپ چنین مواضعی میگیره؟
در پایان جنگ ۴۰ روزه، آمریکا دست به تحریم دریایی جمهوری اسلامی زد و مانع فروش نفت شد.  موضوعی که فشار سهمگین روی جمهوری اسلامی وارد کرده.
همزمان اسرائیل حملات خود در لبنان را افزایش داد و بخش بزرگی از مناطق شیعه‌نشین را گرفت و جمهوری اسلامی را تحت فشار سنگینی برای پاسخ دادن قرار داد.
این بار، حمله اسرائیل به جمهوری ضلع سوم فشار است!
ترامپ میخواد به جمهوری اسلامی بگه : اختیار اسرائیل چندان دست من نیست، اما اگه بیایی و با من توافق کنی، اون وقت جلوی اسرائیل رو هم میگیرم!  تحریم دریایی رو هم برمیدارم! فروش نفت هم آزاد میشه.
اما اگه قضایا بخواد بدتر پیش بره، خودم هم میام سراغت!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5407" target="_blank">📅 13:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5406">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_-ck1ufxBY7ZlsBptoEAQUX49M66JszI8t3DtT1bzIEVbwRQ5Ql76ij2tF8Dn09EhtT5s3N6jBEKT-NBzQvAwp8vfbb_o6Z4cSG40EuEZRQuOPItAV2YCx3r3bEYaVQLiNPPJBotwrHZel5t7-G9KeNgYe3LHym4xRfxnwmitdcix3fqoaTHY7eoJNu4E-JGQn6s4OUhx175H9vayJuhPde-cm-pHBw6--jqjGJqu3Vb3nV6sD6_-oFiLSHgC9DLBxE7Zxk5AYDoiB8XVWiFwcguenxEUdeN-_xtKebZNQc2C_HmBzO1tx58_Tr00Bu4evoQEd7qheHWxrqaovEDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5406" target="_blank">📅 13:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5405">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e7503cf1.mp4?token=ANCxAohvnPaLSBu--SUDgSJFGCcEY6nAo-LaLnNQakA9dGoEITbdM7FOmERBBZYH4kZMe-Z0Vg1YsCykQFf9MBnuiEZHX3XzeG4vCpJ4PbU5gUWIFcNAKshBnobAlwsEdxdGXB4ZHKUW2LJFKu63qJXl8KHK9LXL08JmXEoeKDPDJmSY7lPTej9vM0e05RXvE6LKhaDpFFY5nuWAU5h4x0a6yAW_ocMaFna1FY7wZGC6dqMNws9OvtJYiIhLDoIaZQzOXogPdZFPhIgXc1EHGOeVZ8QecY9dCSuHS3rwyB0-NR3A9YkY0Llguc0NflbH83qN1NRG2t7Ti-7PJVqN-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e7503cf1.mp4?token=ANCxAohvnPaLSBu--SUDgSJFGCcEY6nAo-LaLnNQakA9dGoEITbdM7FOmERBBZYH4kZMe-Z0Vg1YsCykQFf9MBnuiEZHX3XzeG4vCpJ4PbU5gUWIFcNAKshBnobAlwsEdxdGXB4ZHKUW2LJFKu63qJXl8KHK9LXL08JmXEoeKDPDJmSY7lPTej9vM0e05RXvE6LKhaDpFFY5nuWAU5h4x0a6yAW_ocMaFna1FY7wZGC6dqMNws9OvtJYiIhLDoIaZQzOXogPdZFPhIgXc1EHGOeVZ8QecY9dCSuHS3rwyB0-NR3A9YkY0Llguc0NflbH83qN1NRG2t7Ti-7PJVqN-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سقوط یکی از موشک‌های جمهوری اسلامی حوالی شهر فلسطینی «اریحا»
دفعه قبل موشک به یک روستای فلسطینی  زدند و
۵ زن فلسطینی کشته شدند.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5405" target="_blank">📅 13:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5404">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
در جریان حملات اسرائیل، حداقل به دو سایت پتروشیمی حمله شد که هر دو استراتژیک محسوب می‌شوند:
پتروشیمی کارون در ماهشهر و
پتروشیمی سلمان فارسی ماهشهر</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5404" target="_blank">📅 13:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5403">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aClTm4qfiUfdz8oh6HdUlAPdggj7VQqZbahR2AYUzf8-JfLcy9zXqhQFIRrGkiNjMPK9Kppw0dplx7K1c_h69ydz9X8Zw6yhL4znt8lzTxNUlX4hgWs_D8gCCgWGW-V8jg5faGZvfh4CaXZD4vnxNc3FnZuCwtoIUQ_1ihg42W57Rj722hZj80iHOTGVfqSJt-PJgguWXqWAFL_Fcy8QLDz5Lc5YAFopH0DsCdcv2DIGRli8HpgU_uTBDMIv8BXZnWOH-3I7jIHXSjorF_d34z5WE45SLe1bykavhmi5MjhjnXWKqnnHAp2B9s6Fmm4zH8w2xhxEKbrbO9sWdiDbtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ : اسرائیل و ایران باید سریعا حملات خود را متوقف کنند.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5403" target="_blank">📅 13:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5402">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">در جایی از داستان شاهنامه «ضحاک» ، که نماد پلیدی است و هر روز جوانان ایران را به قتل میرساند، برای فریب افکار عمومی دست به یک پروپاگاندای بزرگ میزنه.     دستور میده همه بزرگان ایران زمین متنی رو امضا کنن که بر اساس اون اعتراف کنند که ضحاک بهترین و عادل‌ترین…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5402" target="_blank">📅 12:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5401">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/heePX2bwR0h_r8zrwE6nulmAnmsGGXfh3MZ4KaA9wkGRHdK60wfrXdkjnIGIvEuCnURIbSNj-9CFAnzLkyZ7hu7lXi6qkMtZAvkHnXuWZGcYDS6vTEQhzzPFX7p799Rnl36a7xiaj5n7RgxAz-PGPNOhzXjkmTUzF2d88zLzknhZOQTT34zwcvO8Rh1D5vKxi1fzsrwz_hXPFpiNVyQb3Q6uWm5Cc9eq_rRe9B7PLy83C9sCNMkzYs_2k3D59j3VhJQPNWwqbjKqWa8YkPov7eTHQurTVBaD_gBN_11Z9D-OrPKvmkRQP3-i95lOBZfq7c4GQCoAu_D9vYEviMj-8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جایی از داستان شاهنامه «ضحاک» ، که نماد پلیدی است و هر روز جوانان ایران را به قتل میرساند، برای فریب افکار عمومی دست به یک پروپاگاندای بزرگ میزنه.
دستور میده همه بزرگان ایران زمین متنی رو امضا کنن که بر اساس اون اعتراف کنند که ضحاک بهترین و عادل‌ترین شاه ایران است،
امضا کنند
که :« جز تخم نیکی سپهد نکشت!»
متنی که در اون نوشته شده بود :
«نگوید سخن جز به داد و خطیر
نباشد به پیمان او بر، زحیر»
(هیچ فردی به خاطر فرمان‌ها و تصمیم‌های  او دچار آسیبی نمی‌شود!)
در واقع ضحاک به این بسنده نمیکنه که
خب زور دارم، پس سرکوب میکنم و حکومت،  بلکه احساس نیاز پیدا میکنه به فریب  افکار عمومی  و فریب ایرانیان!
برای همین دست به تهیه این «شهادت نامه» میزنه.
و از روی ترس، همه بزرگان ایرانی هم صف می‌کشند و گواهی میدن که او بهترینه! عادل‌ترینه!
که با این شهادت‌نامه، دشمنان ضحاک به عنوان دشمنان یک شاه ایران‌دوست و خیرخواه و عادل معرفی می‌شدند!
کاوه اما این بازی را بهم زد! یک تنه! تنها! طومار را پاره می‌کند و به ایرانیان نشان می‌دهد که رنج ایران از ضحاک است و آن دو ماری که بر دوش دارد!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5401" target="_blank">📅 12:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5400">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
انفجار در غرب و جنوب تهران
🚨
انفجار در فرودگاه شیراز
🚨
انفجار در کرج</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5400" target="_blank">📅 12:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5399">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWKnFAYYZ0Eby-8ZrWiYt0CVKmRdaxq-j2uCRWSBAU-04H5uPmGFxFzYoQIxTHuc7DdSuzPetTqmFplCMlCoL7-KnFkgmy8ibXz7bkvf7kPp6D_qgZqEB8G2FgqNU3OMtdKyCcF3-hD54b5BFcpsqfiqS5hFNa76rD3UIyl5UDsLrx33jzRhnBuxXwH8RTQICZagsSnT_0YTUqotcfr_CpczRPOQ-lKx1XeJmjqOkJG9S90j03j-Jd_-_63aQw5LJG88Fql2whHTRi3-V1DZfwsRMyEgfHxZSzyeVFYWsIVr1oaEnNYWqrmQEfcENZNUr0Cb17NLY09GIRi2LSF5FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
صداهای انفجار در تهران و اصفهان
🚨
حمله به دانشگاه هوا - فضای سپاه پاسداران در تهران.
🚨
گزارش‌هایی از حمله به یک ایستگاه متعلق به بسیج در کبود آهنگ همدان
🚨
جمهوری اسلامی در پاسخ به حمله اسرائیل به پتروشیمی ماهشهر : صنایع انرژی کشورهای منطقه (کشورهای مسلمان عربی!) رو هدف قرار میدیم!
تصویر : حمله امروز اسرائیل به تهران</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5399" target="_blank">📅 11:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5398">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bI-a_K4D8o4obCUoTcDhVHZbKrkJtTat7vsfsVSXiEfRmFq5_0gnw5gkKw0MHTpN_PLVN-Yu7OeyFpDWTA_YRBHjr52PZ8fOUiZG6UaLAkb0tMTTZ0pbV8i0wJvfdfS8EZKJrnQ3iR7sdoMblRZTkJi5m8VWadfQ7xeyJ4-Qvp733gUAzqDrKOg7ciwHBM-F8sn3zLycp1EhjazlU8jYyEDotNz3hEJbhmTnCm29wTUrPSjYIg9pm6VY9T8-q9v2aVbvPeBSdyamxc0k2M_jYmaXujUA0aYBQ0KbkxRwnrf4e97V9gzA1fnwLs7jOc0h3vettDub3xVh0I_CZ7yiaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی برای عمیق کردن دشمنی بین مردم ایران و اسرائیل این بحث «پوریم» رو به شدت تقویت کرد.
۱- پوریم اساسا افسانه است و داستان!
هیچ واقعیتی نداره!
۲- حتی اگه واقعیت داشته باشه :
یک وزیر ایرانی به نام هامون تصمیم گرفت یهودیان ساکن ایران رو قتل عام کنه،
ملکه ایران متوجه داستان شد، قضیه رو به شاه ایران گفت، شاه ایران هم با عاملان این طرح و با هامون برخورد کرد و سرکوبشون کرد!
حامیان جمهوری اسلامی حالا اومدن میگن : ما میخواستیم یهودیان
رو قتل عام کنیم، چرا ملکه رفته لو داده و چرا شاه ایران دستور برخورد  با عوامل طرح و هامون داده! عقلشون هیمنقدره!!
خب شکر خوردید خواستید قتل عام کنید که شکست خوردید!
کی دستور برخورد با هامون داد؟ شاه ایران!
۳- این داستان اساسا افسانه است !</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5398" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5397">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">۴ موشک جمهوری اسلامی به سمت حیفا و ۲ موشک به سمت تل‌آویو شلیک شده‌اند.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5397" target="_blank">📅 10:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5396">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
آغاز دور تازه‌ای از حملات نیروی هوایی اسرائیل به ایران.
🔺
حوثی‌ها : با موشک به اسرائیل حمله کردیم. دریای سرخ بر کشتی‌های اسرائیلی بسته است.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5396" target="_blank">📅 10:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5395">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
آغاز دور تازه‌ای از حملات نیروی هوایی اسرائیل به ایران.
🔺
حوثی‌ها : با موشک به اسرائیل حمله کردیم. دریای سرخ بر کشتی‌های اسرائیلی بسته است.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5395" target="_blank">📅 09:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5394">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">جمهوری اسلامی از دیشب تبدیل به نیروی نیابتی حزب‌الله شد.
وقتی جمهوری اسلامی در خوزستان ، تهران و کرمانشاه جنگید تا ضاحیهِ بیروت بیروت آسیب نبیند.
مقامات ارشد جمهوری اسلامی بارها و به صراحت گفتند که نیروهای «نیابتی» را ساختند تا آنها سد دفاع از جمهوری اسلامی باشند،
مثلا خامنه‌ای سال ۹۴ گفت :« اگر اینها مبارزه نمی‌کردند، این دشمن می‌آمد داخل کشور... اگر جلویش گرفته نمی‌شد، ما باید اینجا در کرمانشاه و همدان و بقیه استان‌ها با اینها می‌جنگیدیم و جلوی اینها را می‌گرفتیم.»
یا قاسم سلیمانی گفت : جمهوری اسلامی امروز در سراسر منطقه دارای عمق راهبردی است. این عمق راهبردی نه برای کشورگشایی، بلکه برای ایجاد یک سد استوار در برابر استکبار است تا دست آن‌ها به مرزهای ما نرسد.»
یحیی رحیم صفوی : «خط دفاعی ما به جنوب لبنان و مرزهای رژیم صهیونیستی منتقل شده است. این توانمندی مانع از آن می‌شود که دشمنان به فکر تعرض به خاک ایران بیفتند.»
دیشب اما جمهوری اسلامی تبدیل به نیروی نیابتی حزب‌الله شد!
داستان بر عکس شد!
جمهوری اسلامی دیشب در خوزستان و تهران و کرمانشاه و تبریز درگیر شد، تا دست اسرائیل را از ضاحیه بیروت و حزب‌الله دور کند!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5394" target="_blank">📅 09:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5393">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/258de5db5b.mp4?token=g-uSSlFd7JlOP7A2eDWBNoTQLDVqMOKhNvD68HtGueAlP2aDrCU9szvRcKb7Mzdy_yh9iKdZob88prvIZhjElhuAMSsSy9kIX8KOjYT1fGmh_SnoNv0I0j0Uld91JZqGQlopaxI9ej2sXvetLAcPHjEZksh3jW_sWxpsIF4X1CcwjSw2lzpzRPSE4f1P59xH8vkbFZPfZRQS5wCTnlQ3CudNw-BUZFWrlBe_a753nSG1jqbUvDhc2ySMuAp9q-RafLhwVWBAtMrLJ-4Av90UB_Dzvx9wp2Dk7R6d3ER7CpzqO8cqm0v0l-4Pw3F4wXFdkYIq1zl4JSzZX9CkO0mCLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/258de5db5b.mp4?token=g-uSSlFd7JlOP7A2eDWBNoTQLDVqMOKhNvD68HtGueAlP2aDrCU9szvRcKb7Mzdy_yh9iKdZob88prvIZhjElhuAMSsSy9kIX8KOjYT1fGmh_SnoNv0I0j0Uld91JZqGQlopaxI9ej2sXvetLAcPHjEZksh3jW_sWxpsIF4X1CcwjSw2lzpzRPSE4f1P59xH8vkbFZPfZRQS5wCTnlQ3CudNw-BUZFWrlBe_a753nSG1jqbUvDhc2ySMuAp9q-RafLhwVWBAtMrLJ-4Av90UB_Dzvx9wp2Dk7R6d3ER7CpzqO8cqm0v0l-4Pw3F4wXFdkYIq1zl4JSzZX9CkO0mCLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - لحظه اعلام خبر حمله موشکی  جمهوری اسلامی به اسرائیل و  واکنش مخالفان جنگ! حامیان خارج نشین‌ اینها میان توی تلویزیون‌ها میگن دیاسپورای ایرانی عامل جنگه!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5393" target="_blank">📅 09:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5392">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔺
وزیر کشور پاکستان صبح امروز تهران را ترک کرد.
با پیامی که مهم توصیف شده بود، از سوی رئیس ستاد ارتش پاکستان و نخست وزیر پاکستان، دو روز پیش وارد تهران شده بود.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5392" target="_blank">📅 09:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5391">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24ce7a16e2.mp4?token=mE8KyMxFTior7J5gNJyDnx3Zo3dIu4LXlWU6zpbdMjwvJ1HXGhsF9l7jCxsIZTcwJw2mOnFDH4adUtT72n34ntxouw5vBx77g9fPEEKtWY_beVkUSU3xIM4r_sp6-ruLyWhjf33UK4siW8ZP-uXHu9NvwNkit9kO6aNZfxF38EVIwA5ANErhccxeXPSp81bJ-Vm3sLJSy43e_SVnQy9voZFfu_R6rp8zH4K_l_hvUvHlsS2hl-BXfsJ263q7vIaIe3NXn5Nly_VLpp0NfvN_qJCKclNemLgXBwQ0uMCUNUzK_BRc-CsbFDYBt3DDbfKXCbq_ja8Yi6FmkmrzzICw6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24ce7a16e2.mp4?token=mE8KyMxFTior7J5gNJyDnx3Zo3dIu4LXlWU6zpbdMjwvJ1HXGhsF9l7jCxsIZTcwJw2mOnFDH4adUtT72n34ntxouw5vBx77g9fPEEKtWY_beVkUSU3xIM4r_sp6-ruLyWhjf33UK4siW8ZP-uXHu9NvwNkit9kO6aNZfxF38EVIwA5ANErhccxeXPSp81bJ-Vm3sLJSy43e_SVnQy9voZFfu_R6rp8zH4K_l_hvUvHlsS2hl-BXfsJ263q7vIaIe3NXn5Nly_VLpp0NfvN_qJCKclNemLgXBwQ0uMCUNUzK_BRc-CsbFDYBt3DDbfKXCbq_ja8Yi6FmkmrzzICw6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - لحظه اعلام خبر حمله موشکی
جمهوری اسلامی به اسرائیل و
واکنش مخالفان جنگ! حامیان خارج نشین‌ اینها
میان توی تلویزیون‌ها میگن دیاسپورای ایرانی عامل جنگه!</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5391" target="_blank">📅 09:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5390">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BzFVZt_7KFHHIa1J04-wdFTo3v1zQmTpYbAC6-CTf_Ag6HeL-jgQv-g65pnD_k3tBO55NpapiSxME07eG9QrMj8wpNU22UIKss2RjlaZLQu5FqQ_nj2d8lX55c2pW4tJ2NZ4UMOIBc_T3AaZOlwgI9yqQI_dNDfmuD9GC3j4MN2_ijYqaL8XlMS0VPZc3H2bmkwikU_Qljspy8SutLge46WuDJJFdM4yWPXwtbRohBFKq0P_nCLVYmRluFFazkxHVAXpmQ4hrqVfCnQT5rlvzpdTxYzL23jkMjn75FRw5RdQgvGDjVhaifxl0xmhd9pr0IBXvZlsjQ5qrMPJa_7XWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاریجانی هم صبح زود از اون دنیا توییت زد که غم ویرانی ایران رو نداریم!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5390" target="_blank">📅 08:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5389">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
سپاه : اسرائیل شب گذشته به چند سایت راداری در سه نقطه کشور حمله کرده است.
🚨
سپاه : دقایقی پیش حمله به مراکز مهم‌اسرائیلی چون پایگاه هوایی نواتیم را آغاز کردیم.
چند توضیح :
🔺
سایت‌های راداری که اسرائیل به آنها حمله کرده کار شناسایی و مقابله با جنگنده‌های اسرائیلی را انجام می‌دهند که اسرائیل به آنها حمله کرده
🔺
سطح ضربه‌های دیشب اسرائیل به نظر میرسد کنترل شده بود. با توجه به مخالفت ترامپ با پاسخ دهی اسرائیل.
اما به نظر میرسد سطح درگیری و ضربات امروز افزایش یابد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5389" target="_blank">📅 08:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5388">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKJXoqHLBtzTVFIATevzYZ60tIqUvIDm6fh8iC4jq0udQiKXdYjFjVDh_qVmWkxcC87tysvCLH3GSXJLeLZMJH3UtUzU_i2OrUHzN4Bp75sSF8oFHOKcGRjZBIojj_x6klhe0zKD5-TCc7rkR1qB_oppFEl2xDgmn9eTBBo_CnUskx7r9iKKWWdoP80FyBJoOMeoJna6nmSXet929dpEY-1NN6PcPbiQXiDf5JeclYS_ovT8isqT8fLDG5o40lz9nmE8AAVImp_NEPyNzJeAfMAfnB1_KF_0ZV-71VDSMzMgyEggEmjhWHwLaYpncHcHKT15SsdqWbZOCoH8bjdCMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خبرگزاری‌های داخلی : اسرائیل شب گذشته به «پتروشیمی کارون» در ماهشهر حمله کرد و این تاسیسات خسارت دیدند.
🚨
اسرائیل دیشب به فرودگاه مهرآباد نیز حمله کرد.
🚨
جمهوری اسلامی دقایقی پیش موجی تازه از موشک‌ها را به سمت اسرائیل شلیک کرد و اسرائیل در حال آمادگی برای…</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5388" target="_blank">📅 08:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5387">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
خبرگزاری‌های داخلی : اسرائیل شب گذشته به «پتروشیمی کارون» در ماهشهر حمله کرد و این تاسیسات خسارت دیدند.
🚨
اسرائیل دیشب به فرودگاه مهرآباد نیز حمله کرد.
🚨
جمهوری اسلامی دقایقی پیش موجی تازه از موشک‌ها را به سمت اسرائیل شلیک کرد و اسرائیل در حال آمادگی برای موج جدید حملات است.
🔺
کابینه امنیتی اسراییل تا ساعاتی دیگر برگزار خواهد شد.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5387" target="_blank">📅 08:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5386">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">تاکنون : حمله به تهران، تبریز، ارومیه و کرمانشاه گزارش شده است.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5386" target="_blank">📅 05:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5385">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی ارتش اسرائیل رسما حملات اسرائیل به مناطقی در غرب و مرکز ایران را تایید کرد.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5385" target="_blank">📅 04:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5384">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای انفجارهای مهیب در تهران ، کرج و اصفهان.
کانال ۱۴ اسرائیل؛ آغاز حملات اسرائیل در ایران</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5384" target="_blank">📅 04:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5383">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اسرائیل ارسال هرگونه کمکی به غزه را قطع کرد.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5383" target="_blank">📅 01:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5382">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">یدیعوت آحارونوت:
🚨
🚨
در گفت‌وگویی که لحظاتی پیش پایان یافت، نتانیاهو به ترامپ از قصد خود برای حمله‌ای قدرتمند به ایران اطلاع داد.
رئیس‌جمهور آمریکا تصریح کرد که اگر چنین حمله‌ای انجام شود، آمریکایی‌ها در آن شرکت نخواهند کرد.</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/5382" target="_blank">📅 01:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5381">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">هم‌اکنون : تماس تلفنی نتانیاهو و ترامپ</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5381" target="_blank">📅 00:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5380">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">یدیعوت آحارونت:
ایالات متحده به اسرائیل پیام داد که بهتر است چند روز صبر کنید تا ببینیم آیا می‌توان به توافقی دست یافت، و اگر نه، ما طبق برنامه به اقدام مشترک ادامه خواهیم داد، و ارزش ندارد که این را با درگیری‌های محدود تلافی‌جویانه هدر دهید.</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/5380" target="_blank">📅 00:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5379">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrDmFQkGM_nTwvVGG0Zpqiy3d8_r1VASD6vLdTjfeMk1ZXBNodXDJC2aIq5qESJlzffIWLzfqzWAp0RWudDRA47s1kGrbaEDUI3C1duO3dU-VzIDmnqAxufRkqs3zixL_N2cMxEFnvRekQfbHLLrSUhYITWEJq-LUDd5o7J6SNJLkkDALc9newNMMfEbfXUPkJwUoSoGOhBRDk41E2EelETW8pRntdm_heGxTk_zGV4AEVR6MbBF2ZP61eLjp_gmpqwQkhFKRx-RX6_5Z1L4NHiC6Zts1BGMPCRxzcb-d5l9ridonyc3eRiY3GK3UZ41x2riepDTCT8L7b-N4mIm5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شخصا بعید می‌دونم اسرائیل فشار ترامپ رو بپذیره و پاسخی به شلیک موشک‌های ج‌ا نده.   گرچه وقتی در ۱۹۹۱ صدام با ۴۲ موشک اسکاد به اسرائیل حمله کرد و آمریکا درخواست داد ، اسرائیل پذیرفت و پاسخ صدام رو نداد.   ولی این بار رو بعید می‌بینم. عدم پاسخ اسرائیل، یک معادله…</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5379" target="_blank">📅 00:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5378">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">رهبران اپوزسیون اسرائیل، نفتالی بنت و آویدگور لیبرمن، خواستار حملات قاطع به جمهوری اسلامی شدند.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5378" target="_blank">📅 00:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5377">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXq65nXICBnK-MWUJI4rrRlFFOxnbsdt60qECqfzdfbMv-MmrklPbZyNuNOk0uFZ2cX9Uf04GGUHz47A5Dg693WyEf6Glyjn3YGd5RwWB5PORUvBGgwA6SSvo0DUjEA7xTs8I3PjaiOqAARbWynV0pOe1BE9J5fMWbmoRy37VjzgcZT5EZEZyT8EcDMmkPm9xFeVYP6d8P6u6K0zmuXQBGlzoZSeGVYZBAGByMVkMcgZOkJbBMUoUrymaNlDdVkAMOf7qFn5B8xMkBn-1s3DofytCbYbI1feM9mGlRgVFX4tz-zoV5eTWHNOpt3RmsgDfWjDwfDetcFyOfZwFbcCcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاسخ وزیر خارجه اسرائیل به توییت عراقچی.
عراقچی پرچم جمهوری اسلامی و لبنان
رو کنار هم قرار داده بود.
وزیر خارجه اسرائیل ولی پرچم حزب‌الله و جمهوری اسلامی را کنار هم قرار داد و عراقچی را «شیاد» توصیف کرد.
اشاره به اینکه جمهوری اسلامی حامی لبنان نیست بلکه حامی حزب‌الله است.
🔺
یادآوری : دولت لبنان سفیر جمهوری اسلامی را اخراج و جمهوری اسلامی را عامل  جنگ در کشورش معرفی کرد.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5377" target="_blank">📅 00:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5376">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">هم‌اکنون : تماس تلفنی نتانیاهو و ترامپ</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5376" target="_blank">📅 00:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5375">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">حوثی‌ها حملات موشکی جمهوری اسلامی را تبریک گفتند.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5375" target="_blank">📅 00:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5374">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">شخصا بعید می‌دونم اسرائیل فشار ترامپ رو بپذیره و پاسخی به شلیک موشک‌های ج‌ا نده.
گرچه وقتی در ۱۹۹۱ صدام با ۴۲ موشک اسکاد به اسرائیل حمله کرد و آمریکا درخواست داد ، اسرائیل پذیرفت و پاسخ صدام رو نداد.
ولی این بار رو بعید می‌بینم.
عدم پاسخ اسرائیل، یک معادله تازه ایجاد خواهد کرد و ‌دست اسرائیل رو در لبنان خواهد بست.
چون در برابر هر حمله به حز‌ب‌الله، اسرائیل هدف قرار خواهد گرفت.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5374" target="_blank">📅 00:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5373">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
ترامپ : همین الان زنگ میزنم به نتانیاهو تا بهش بگم که به حملات جمهوری اسلامی پاسخی نده!</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/5373" target="_blank">📅 23:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5372">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
ترامپ : از حمله امروز اسرائیل به بیروت ناخرسندم. اسرائیل با آمریکا هماهنگ نکرده بود!</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/5372" target="_blank">📅 23:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5371">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
سی‌ان‌ان به نقل از مقامات اسرائیلی: پاسخی قدرتمند به حملات امشب موشکی جمهوری اسلامی خواهیم داد.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5371" target="_blank">📅 23:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5370">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‏ترامپ در اولین اظهارات خود: به ایران می‌گویم؛ شما به اندازه کافی شلیک کردید، بس است. حالا برگردید پای میز مذاکره!</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/5370" target="_blank">📅 23:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5369">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">فرهمند عليپور Farahmand Alipour
pinned «
🚨
اسرائیل : ۱۰ موشک به اسرائیل شلیک شد، که هر ۱۰ موشک رهگیری و ساقط شدند.
»</div>
<div class="tg-footer"><a href="https://t.me/farahmand_alipour/5369" target="_blank">📅 23:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5368">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
اسرائیل : ۱۰ موشک به اسرائیل شلیک شد، که هر ۱۰ موشک رهگیری و ساقط شدند.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5368" target="_blank">📅 23:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5367">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
اسرائیل : تاکنون تمامی موشک‌های شلیک شده را رهگیری و ساقط کردیم.
🚨
گزارش‌هایی از موج ‌پنجم و‌ ششم شلیک موشک‌های ج‌ا به سمت اسرائیل.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5367" target="_blank">📅 23:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5366">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
والا نیوز : اسرائیل در پی کسب چراغ سبز آمریکاست تا به زیرساخت‌های انرژی ایران حمله کند.</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/5366" target="_blank">📅 23:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5365">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
موج اول موشک‌ها از کرمانشاه
موج‌دوم از  تبریز و موج سوم از ارومیه شلیک شدند.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5365" target="_blank">📅 22:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5364">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
اسرائیل : پاسخ حملات امشب جمهوری اسلامی را خواهیم داد!</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5364" target="_blank">📅 22:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5363">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXwcfkPI6I2__zEChaPuGRJ189-znAoTmXQv1hZFigp1gluIoMp2ebANwfaFTdoxbQFkPIF-fw4iO8irY7CHrRy6IfRiJVrbN_yxtnmuaZ3vE8ztR1S2vWGV3FV3szc-2O-Vhu2aLTDsoZZJxQOqLfxTsa0YvWvVNSFDncdUdtwG04cJm_iRZylrKZUL5Jx4Uiy4LuYt77Xe89cDS3o49O-JYtW8MZJntg-o5OLCcM7zNUbNluN12DXj2V9AL5XCGqFDMmqTPIR3wDhxIDwkLNZqt1Spr7uOFQfDn3qt0WYgN7FIFh-0myX5dvEJcZt8BByT4WK_8C-cfDPttNZa3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
موج دوم و موج سوم حملات موشکی ج‌ا به سمت اسرائیل
توییت عراقچی</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5363" target="_blank">📅 22:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5362">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
منابع اسرائیلی : ۴ موشک بالستیک به سمت اسرائیل شلیک شد!
دیشب نامه مشترک رئیس ستاد ارتش پاکستان و نخست وزیر پاکستان رو تحویل گرفتند، که آخرین فرصت توافق و گفتگو است.
امشب جنگی تازه را شروع کردند، این بار برای حزب‌الله لبنان!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5362" target="_blank">📅 22:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5361">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از حمله موشکی ج‌ا به اسرائیل.
🚨
هشدار حمله موشکی در شمال اسرائیل
🚨
قطر آسمان خود را بست.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5361" target="_blank">📅 22:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5360">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ارتش اسرائیل در حال آمادگی برای مقابله با موشک‌های جمهوری اسلامی
فردا : تعطیلی کلاس‌های درس در اسرائیل.
اسرائیل : نشانه‌هایی از احتمال حمله موشکی ج‌ا به اسرائیل وجود دارد.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5360" target="_blank">📅 22:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5359">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
آسمان‌های ایران و اسرائیل بسته شدند.
🔺
امروز ‌و در پی حمله موشکی حزب‌الله به شمال اسرائیل، ارتش اسرائیل  به مرکز فرماندهی حزب‌الله در بیروت حمله کرد.
جمهوری اسلامی چند روز پیش به اسرائیل هشدار داده بود که به بیرون حمله نکند و در غیر این صورت به اسرائیل حمله خواهد کرد.
مقامات جمهوری اسلامی امروز اسرائیل را تهدید به انجام حمله کرده‌اند.  اسرائیل نیز هشدار داده که هرگونه حمله ج‌ا به این کشور را شروع یک جنگ تمام عیار تلقی خواهد کرد.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5359" target="_blank">📅 22:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5358">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o28JApxU5Olv_qA2lsxyDszwgYFqtn8dRW7XzvfNpC3askz0KS6Povz_cpfrXN3X-TnT9KHhI1RF8_KLsFR646hMO1N8VAZEeMWcX5SnsGBKhuSGlHuZt2Q2q0UJ7uXq2wZRdm4TG4LdXXEJyWZUqC4IWt3E2I4NWf_vIHNZvm1VjKc-0Vz7YAcnMyuIKT8FSpJLtmBJKUDbp_tRNMS2mlvg0izYthmI575L0dVogNXNl3hh-EH3AHTRTE_HQjcBT8Vn_7BOMMNJ0GJwTa3IS67J8eozC5rx4uUHdX8BWy8VMk-lS98RKJuLk4wTIQfpX_HsCcrJN7FV9lNPInva-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرواز تهران - استانبول تغییر جهت داد و به تهران بازگشت.
گزارش‌ها : حداقل سه پرواز ایران مسیر خود را تغییر دادند.
گزارش‌هایی از بسته شدن آسمان ایران.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5358" target="_blank">📅 22:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5357">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ارزیابی برخی رسانه‌ها : جمهوری اسلامی به جای اسرائیل به کشورهای عربی حمله خواهد کرد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5357" target="_blank">📅 21:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5356">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
هشدار اسرائیل به جمهوری اسلامی:
هر‌ حمله‌ای به اسرائیل به معنای آغاز یک جنگ تمام عیار خواهد بود.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5356" target="_blank">📅 21:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5355">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اگر فرضا جمهوری اسلامی برای کمک به حزب‌الله، وارد جنگ شد و در پاسخ اسرائیل زیرساخت‌های ایران رو زد، اینبار چطوری میخوان توجیه‌اش کنن؟</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5355" target="_blank">📅 20:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5354">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">جنگ خارجی نباید به اذن و دستور فرمانده کل قوا باشه؟
نباید قاعدتا مجتبی فرمان بده؟</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5354" target="_blank">📅 20:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5353">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
قرارگاه خاتم سپاه : به حمله اسرائیل به ضاحیه بیروت پاسخ میدهیم.
🚨
اژه‌ای : حزب‌الله جان ایران است !
🚨
قالیباف : فقط زبان زور می‌فهمند.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5353" target="_blank">📅 20:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5352">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KP912zahAWh_Es5qWvQ2WTMs_DiPZg0Lko2cirKen-47vtpTlrWUke2WavYfFLSDbgihHnDEyI2176IwcFFVqOc3fLz7VKW9wxdqsVD6ak3Pypo_1CESJk2Of30BJ74gFwnxCEx32Eh4j9FUPaaCdHvh_l4u-MI-NQ0191cNvzPjkoE7EF-hTcUFIwGtowoOz6t5bjaUCzWmWTjyhFgz7i4yQSwn1Fk5VJu2EoUWGq-p-6KlImP-inWKAN6re3enKQxE4FGcS_PrzwMJWusqPQyyIUset_yXVYbXcANpMZUbaMRTVeSLh2McAUVN3eCuSj49HxecT1IOG0iRvg3VYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به این گروه اطمینان خاطر داده بود که اسرائیل از ترس واکنش جمهوری اسلامی به بیروت حمله نخواهد کرد. اینها هم با خیال راحت در بیروت بودن!  در عوض، اینگونه شد!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5352" target="_blank">📅 19:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5351">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVsEVmGet1mT4bhQ8WBaS6zz8xXwBJuf8nvROJUGG7SuZLaC6L97kYO8Q79vwPUonCPFVfrXsXaIarJqsvz5H-eoaes42kHAWf9KqnZfzBaoGWLLaHnAEoyLnv5o0nvGAMmoAIbiMaNohpOSNzDOmp0chsJEsijrpbTj5dylNaZzjK5M2Lj1ARI6hEFzrP5BLk76mIkbYCtmMdE6jrTB4MSBfx3MXtgpwf8Wber42Cq9OqrYvCt1K5M-jZpLIazCGToHjnBvNRVhCmZ_cBcqQQT-O4Iy9wDtEWz2nzsINwPNmhULw-OdsRmsad43e1X8R7MFZd50zjtZie1GnPCVew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به این گروه اطمینان خاطر داده بود که اسرائیل از ترس واکنش جمهوری اسلامی به بیروت حمله نخواهد کرد. اینها هم با خیال راحت در بیروت بودن!
در عوض، اینگونه شد!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5351" target="_blank">📅 18:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5350">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bhhukZpqJSDOgM7CcI_0m7obIjfLsxctr1cZZyhfBgad0rixjG-K2WW2y-_ZgBRPt5SKMhxv7wTYCCqaTJIli7noJP0y0_cKgmFsssov1KOXZhi1ytlijlZGswAuADiRXtzLNHoQPQK_TuWHqE9wwiC1d0xdgEQVJ1jo5DfeHqhHNMtIzggTICKz5ujnUhinW6d_AkZqcDpeDUrFjMlQplLgl7gMh-cS-ca1gw8gxcYegn0IcOSXeeyvghoPY38lStuRD4tH5ApNL-Hk2G2XyqBg5iSW6vcIHqMD1JxYYyGtJ3W3TPd9eYbwwxHsF9IQ2mnW8jB8rYhfvPm_Dh08bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی حز‌ب‌الله،
اسرائیل به جنوب بیروت
(منطقه شیعه نشین ضاحیه) حمله کرد، چرا مهمه؟
چون جمهوری اسلامی هفته گذشته تهدید کرده بود  که اگر حمله‌ای به بیروت شود،
به اسرائیل حمله خواهد کرد.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5350" target="_blank">📅 18:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5349">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd67e1a1b.mp4?token=s24ZtQmnwFuDEakBxkK74Ye9cT5ZSMhBU-87V3sjqWGz9wv_PG1s9nRJ3kiaE5x6E38_oxfIUtsHDg-LrKApEIvoxWSxiLBJKireRpPx9BcBqLMf7h_ZwpEE0BxQq1ZrRneA1IqKNN-8yE3J5oBSzUgKIBQrQdv0FPLCxgOpqxuzCFx7Wqf9-yFK8KG96gtgCz3QeRG72ojNd7Sz8qAdSvVagvro8VLkITKuzMyxtEjQGDJ1HqAOEzzVVbg2X8Mi8fDIv6ys1kqfFJ2PBPuSodl_kdfsVxCaG2ONWmXVcgFFdwBRIDM6MhbnZcI2s2i7Xm7xuqMEFBhMO5e5YIczqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd67e1a1b.mp4?token=s24ZtQmnwFuDEakBxkK74Ye9cT5ZSMhBU-87V3sjqWGz9wv_PG1s9nRJ3kiaE5x6E38_oxfIUtsHDg-LrKApEIvoxWSxiLBJKireRpPx9BcBqLMf7h_ZwpEE0BxQq1ZrRneA1IqKNN-8yE3J5oBSzUgKIBQrQdv0FPLCxgOpqxuzCFx7Wqf9-yFK8KG96gtgCz3QeRG72ojNd7Sz8qAdSvVagvro8VLkITKuzMyxtEjQGDJ1HqAOEzzVVbg2X8Mi8fDIv6ys1kqfFJ2PBPuSodl_kdfsVxCaG2ONWmXVcgFFdwBRIDM6MhbnZcI2s2i7Xm7xuqMEFBhMO5e5YIczqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعتی پیش اسرائیل به ضاحیه بیروت حمله کرد،  عراقچی ۴ روز پیش به شبکه المیادین  (شبکه لبنانی با پول ایران) :  اگر اسرائیل به بیروت حمله کند  اصلا تحمل نخواهیم کرد  و این یعنی شکست آتش بس (بین ایران و آمریکا)  و نیروهای مسلح ما پاسخ خواهند داد.  به کشورهای دیگه…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5349" target="_blank">📅 18:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5348">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b087eb5a38.mp4?token=nsDVUewjRBVsexrCJGHkFF6xxOb4Y6rnoKsbAVbXy2T-6y1nKUUq86xct-ovSse6ko78Hz_S4JcCbzhoN52nvjYvo830pzAfgcwnBdSnLp3bw4oegd1ZzKOZ78kmAnZc-z6t70_xJi_Co4x1driCO0WHJ9r65KYkjWaVJXhgST0yIcuxv0FdbIEQZ0LBaoGbL3DP92TfNEs8w86IdIjDfgShESIIlLH1q2KLFLAFsiENnJh3aZbEl2q1u7-3nzvZAiy8qpFl9h3cli_asnyim_5pkQYOXQ-qYoXSs209bc4-CiA4JujHbrUXLCfdyQWwGE7P9fmPhJQbC4i-b7DIow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b087eb5a38.mp4?token=nsDVUewjRBVsexrCJGHkFF6xxOb4Y6rnoKsbAVbXy2T-6y1nKUUq86xct-ovSse6ko78Hz_S4JcCbzhoN52nvjYvo830pzAfgcwnBdSnLp3bw4oegd1ZzKOZ78kmAnZc-z6t70_xJi_Co4x1driCO0WHJ9r65KYkjWaVJXhgST0yIcuxv0FdbIEQZ0LBaoGbL3DP92TfNEs8w86IdIjDfgShESIIlLH1q2KLFLAFsiENnJh3aZbEl2q1u7-3nzvZAiy8qpFl9h3cli_asnyim_5pkQYOXQ-qYoXSs209bc4-CiA4JujHbrUXLCfdyQWwGE7P9fmPhJQbC4i-b7DIow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعتی پیش اسرائیل به ضاحیه بیروت حمله کرد،
عراقچی ۴ روز پیش به شبکه المیادین
(شبکه لبنانی با پول ایران) :
اگر اسرائیل به بیروت حمله کند
اصلا تحمل نخواهیم کرد
و این یعنی شکست آتش بس
(بین ایران و آمریکا)
و نیروهای مسلح ما پاسخ خواهند داد.
به کشورهای دیگه هم‌ گفتیم که در اثر اقدام اسرائیل جنگ‌ دوباره آغاز خواهد شد.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5348" target="_blank">📅 18:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5347">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41dfa742b0.mp4?token=aLb6sXM7WZ0nze5xKNFM1PsBN8rObUcp45KuEZGtPva79zLvCdFfAwWdjx8EZD4eiYsGWPaKschD6Of4nGWMxjAclQrPU_Yi3AaMyx0scDyXr-s8sNkQCeeAr8tEgx1NcUX0gjB-4QcUcuMUZXI0UDGSxcGM7fwu1ki3Ad1DtMiT0HYqGujWnYC0i2qwSRUCn410spRxNLOZ2FWGeY95jFzNxk-Ris5MDqYVs7l2m7kxxBOzQiycV12w9D-64EKq8ofdJ3KgDpY6tTmqNatCHvQ6tjJpdkLA1Q4s4BegIOwgj2GoaQjAAlvY7Hckch96eRDNf3ePA-pC3xgprEs_jjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41dfa742b0.mp4?token=aLb6sXM7WZ0nze5xKNFM1PsBN8rObUcp45KuEZGtPva79zLvCdFfAwWdjx8EZD4eiYsGWPaKschD6Of4nGWMxjAclQrPU_Yi3AaMyx0scDyXr-s8sNkQCeeAr8tEgx1NcUX0gjB-4QcUcuMUZXI0UDGSxcGM7fwu1ki3Ad1DtMiT0HYqGujWnYC0i2qwSRUCn410spRxNLOZ2FWGeY95jFzNxk-Ris5MDqYVs7l2m7kxxBOzQiycV12w9D-64EKq8ofdJ3KgDpY6tTmqNatCHvQ6tjJpdkLA1Q4s4BegIOwgj2GoaQjAAlvY7Hckch96eRDNf3ePA-pC3xgprEs_jjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو‌ رستم تهمتنی،
«چرا دیگه نمیزنی»؟؟
بله جنگ طلبها دیاسپورای ایرانی بودن!
نه اینها که ۴۷ ساله سیاست‌های
خصمانه و جنگ طلبانه دارن!
در دیماه وقتی مردم ایران رو قتل عام میکردن «حیدر حیدر» میگفتن، یک ماه بعدش شد «رستم رستم» !</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5347" target="_blank">📅 11:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5346">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qa_tKy-FgnxzgbWFhaR4Zd3MxYeK3WPfww7kcRLKmxIXaGLpsxFEIeu7Pf1U4dl5P6JrQqJqsqCNNt_pVdNu5VPdU0ZNiNxQpeiO0UO_fbBjYXWBCgiMkNlUYDRelc_8MtFt1J5oheYebQ0dRGLMIqzDpNCJ_ydH2aVd6Mo0AFFSB-hecpL9aI3VqkY1VgsD30jPM8Z9AO9GNxjVqqvWetK2LVGACL0gYT8UpzBfY13OVBRmlh-1XjdUwi2cuvwt8l5h33Ubba-G13KDolRSjSVXWEx3y2cYdif7VMLxp6ghwQg-XvTV3nbwtSKypTLnMgcLQIhcxnpYG_PHCs1Scg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید دولت فلسطین نه کشته شدن علی‌خامنه‌ای رو تسلیت گفت و نه برای رهبر شدن مجتبی خامنه‌ای پیام تبریک داد. در قبال حمله اسرائیل به جمهوری اسلامی هم کاملا سکوت کرد!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5346" target="_blank">📅 11:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5345">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SyzZizbqHksUmWskKIZBcCKJCJpE-5f4k4cQ6LNfMB7BmhDDrplyB3RKirecskFzReDxNEhUbnN9LeTrJfquG77KjHFulKEyn0UbFywGUcxe1UIDYYO0HTv9-tCmdyFkXEnZj3rHB6jcmLxNbN6m5izBXprA7Gqs44NbC6RsjrRJvX6QxDM6A2coGBCWLavpRQ-IWg5ljawpmfuhiSlXh6Uzd9_H3oS3J2-YvV55NUtQe5CamYMMKBIRnjpEmVqjZCsaLlsuJWbbQBn1tmlC8WcDJG2G16oN0MS35gn2jO7oE_01qaoOiha31YIQM07fiN6JKmkxBUZnO9MPD4uAcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید دولت فلسطین نه کشته شدن علی‌خامنه‌ای رو تسلیت گفت
و نه برای رهبر شدن مجتبی خامنه‌ای پیام تبریک داد.
در قبال حمله اسرائیل به جمهوری اسلامی هم کاملا سکوت کرد!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5345" target="_blank">📅 11:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5344">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">کارشناس حکومتی : در اعتراضات دیماه ۱۴۰۴ حدود ۱۰۰ شهر سقوط کردند یا تا آستانه سقوط رفتند.
نهادهای امنیتی گزارش داده بودند که کار رژیم تمام است.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5344" target="_blank">📅 10:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5343">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
رویترز - آمریکا قصد دارد از پولهای بلوکه شده ایران، خسارت کشورهای عربی مورد حمله جمهوری اسلامی را پرداخت کند.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5343" target="_blank">📅 01:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5342">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سفیر ج‌ا در مکزیک : ویزای اعضای تیم فوتبال برای آمریکا چند ساعته است، همان روز مسابقه وارد خاک آمریکا می‌شوند و در پایان بازی باید سریعا خاک آمریکا را ترک کنند.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5342" target="_blank">📅 00:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5341">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IyCaRMuXodv17pD6uIyV1MHvDWM792p6Nhqv7bNvFrYSvMa60X_F_01JEqH1QGWUVehcFRKXYeUnaaPbgdW_Yt_Su6fiqlwdpmvGGJ9FgvRw3ltof2q3MuSbgN1qY2xwQH7-uNOgjHkHg9gfgJHkQ3wu6s8Y4VduDr2eYdIIJiR0L2EN0oTSaWC89NXNDuGF1_ahjM-0dJDW9ODSr3aKYX6iA6siHJU3RMbLCT77XPa5TJrYQwFn7xp29IK_uLYPrRvlr-FPkQm6sTRm-3fR8YdZlpE1ojofsOGT4_8oOs_IZGDStXYjqb96i2eM0jj-ZYMg8ikMDuM4RqwavzfOKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه ویژه و مشترک رئیس ستاد ارتش پاکستان (عاصم منیر که روابط ویژه‌ای با ترامپ داره) و نخست وزیر پاکستان
برای مجتبی خامنه‌ای</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5341" target="_blank">📅 23:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5340">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLkZNU72acxcuwDFHkQ385ay7qcVtIJFuKnunTzjOP9NSCN_evBVRyZyIII1qru9-oy-xZl-nguRgF54L8c6BhjalqKqXEzJ7zBEQpZ-eIAsurs9lB5CKIm5Np_S-QEa4Suz03lN2PBzPqmCXb9i5tZH5ZqfgDF81pPkfmemDnWxQhXA8UDfpCrC6M_tiC5_I-_qStAY6CjsMZEBQ9Mj1VfNyf4IPYuY1ELYqhFY2EqLGEVrgekeq4GaKoPNnjyCMmu5t_WaKi5imj7MwaWqMVol_PxdGETctlE1rR_IMjKNt0eE_ArDAym9QU7XVd0nA71Wih-4bktX7jJWtOlGXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اونهایی که فرانسه و عربستان رو دارن
توی خونه‌هاشون نشستن،
ولی اونهایی که جمهوری اسلامی پشت و پناهشونه، رفتن توی گاراژ و انباری
و توالت اونها قایم شدن :)
با این توصیف، خوش به حال اونهایی که
جمهوری اسلامی پشت و پناهشون نیست!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5340" target="_blank">📅 19:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5339">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5BoOyO_PPfS9O0PVQqNcGbkjiNM5yF_5VPbhS0ivWXcMJa7PabL-I8RxRB7jmQpPiz56Mg5L-AhjRum21iRU-fLcneXxD_D5OLiVVk05LuJfSyIboqGV_uYg-yWnox39tJcHBhHOHuRToopNMokejH4__gjLMIlqvIuDkSub_oD8CdXugG3gGhP3OcqrqyX7jYsq4-GT92Xe13eZrNTQQc1WjRI73OvO0if4GfYL380rnfN9Ew5I1pXpTlVd7s2zrGEOMWbpaF5rn6JFrQbH93O7qpZxhu6TgwkhAZfiwoO6uUyj-IqzswhNCEupPBXYaoJS0AIf7zxi9eEhLzuCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی به رییس جمهور لبنان توپیده که مگه ما کشور شما رو اشغال کردیم و لبنان رو بمباران می‌کنیم.   ولی واقعیت اینه :
🔺
گروه تروریستی حزب‌الله لبنان برای خون خواهی خامنه‌ای وارد جنگ با اسرائیل شد! با سلاح و پولی که جمهوری اسلام بهش میده!
🔺
پول و سلاح حزب…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5339" target="_blank">📅 18:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5338">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCDEFDk4QW2eRlX-xvMCDimjUL6SEC1mGnDtJVjrCVEk-8kLImvdwij04XOs26fZhUtw3AUl2a4Fvxalx0X3E59Vxw7QjhjGYEbP5mE2Ohg8gNF1Ipn3QkmVV09Xn9Du-acdLWYqjHAJ_GPmUh0GwovLZSjZsotyY-q0vDb9_qvWWzCxwNz5PYgRn-thbJ0ub14_1PmAuDPAQFPQCZyUS8QcXwp9EaVwjDdushuFYK0Jwprs0M5snBTEKHCFz29qpuFeJ-ZKfYU4Dn41-t5ZzlDkDwJdshpHJDdQQFV6XqYzkBAXWtHyp-k663KwG_Y7HbjsFf_Ua0a8TL5SJSbEVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی به رییس جمهور لبنان توپیده که مگه ما کشور شما رو اشغال کردیم و لبنان رو بمباران می‌کنیم.
ولی واقعیت اینه :
🔺
گروه تروریستی حزب‌الله لبنان برای خون خواهی خامنه‌ای وارد جنگ با اسرائیل شد! با سلاح و پولی که جمهوری اسلام بهش میده!
🔺
پول و سلاح حزب الله از طرف دولت لبنان نیست! حزب‌الله برای شروع جنگ از دولت لبنان اجازه نمیگیره!
🔺
این جنگ رو حزب الله به لبنان کشاند و باعث شد یک چهارم جمعیت لبنان آواره بشن و یک پنجم خاکش اشغال بشه! به خاطر جمهوری اسلامی!
🔺
جنگ به خاطر لبنان و منافع ملی لبنان نبود! با اجازه دولت و مجلس و ارتش لبنان نبود! با سلاح لبنانی و پول لبنان نبود! به خاطر خامنه‌ای بود و با پول و سلاح جمهوری اسلامی!
🔺
تا الان هم برای خونخواهی خامنه‌ای بیش از ۳۵۰۰ لبنانی از جمله آنها ۶۰۰ کودک لبنانی!! به خاطر خونخواهی خامنه‌ای!  کشته شدند!
🔺
لبنان و اسرائیل ۲ روز پیش به توافق آتش‌بس رسیدند ، سپاه پاسداران اولین گروهی بود که بیانیه داد و آن را محکوم و رد کرد!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5338" target="_blank">📅 16:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5337">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0e4yyQ9OoqYzlpPMksgjYpMMyX7-fQ2-gsRJhfnI-Ej7l8GC_8nPOJlBuAGqDQ5_xGxfH2LELWZxfNW1i7rX5S9MgwyKvuzMMTiUn2jw5TIFDp1xKehcL0YrZA1VMc_WbPsj7jg2aHHsp4dLOMqR37pSORnmR-JPv8ZiN3zsj6DYJNSYH3qNVKZXcL-qggWDZb1kIW7M3-nnueoN3X9IZXPJGmGe8oG61VHmdjO2GmXr5U3X_BTsBIxUPCPHvZTjyfP_1e9T2MNtyrTMNSqUSfTWRAL8XnnAh627q5aOCpDrt6lUol21WRlpK_V-coEr5QKst-MOeKN3vBNwL-o8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان منو در توییتر غریب رها نکنید :)
https://x.com/farahmandalipur/status/2063193568332615691?s=46</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5337" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5335">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mwNIuiPA-QEyTXqUEh6KugG3YxA4LxBQyGfor7pkE2_6_AN6bit4cR-OCOKXuH5EclBdUCgRZiTdxIkKRbfAluiIBSFTmqnlSUI3ASQ_1zwujdZOhofcmYEarFWxVUmWWvxD4ApGXbEWtu41Urai1wg6ruTjuPzOdtPAl5VVWYwC4jLh0imsWu-KmyxArxJ-C1xQtK7ohl332C5H8cMWhNg51XS642xlgunxcbj7Y2M8T_xq9s0nvI_LdesZ0lS4PEgboxuO342rqYqmCXUW5OS5E9OoQ2QidvF391YyZDU93gBK6ofA5tLgw3V6jl41kp0V7oSg2pB9JQfbAQ8Vyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jAFcmrV7uT_SJZx6EquHKssDOPnoq4K26N2oX8GuEeX_AW_PsXEoK6LZ9qO87vVgTrNhRk9my9-PZH1s-kkqiQHuJnCltyQghbCOii_mPUxx0DbbINO_ebOt2NolqIEZzYlpbAHcpoj7JRp1mo2IvbfX1VzAaVxSbYAG-47CuvQ9AqK0syZK95oOgzgDHUEYIOR8l26h_CKbmQ0N8iO9XvPBjgqFsh66KJSEK7F1e2lWofQkWtit2TMA7SB_sBe4goEDm_3g3iVff40RlBYulT_3xkOxCRVKgzVN4pmjPlcixia-e2zlAll4ENWpn2M_tu2PsKhN1HMJIqvmla2-tg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انتهای ۴۴ ساعت تلاش در عمق صدها کیلومتری خاک ایران و تجمع برنو به دستان و  ….، کشته شدن چهار شهروند دهدشتی در جریان جستجو برای خلبان بود (که تشویق شده بودن برید جستجو کنید و…) و البته کسب غرورآفرین شورت خلبان آمریکایی!
ارزش این فوز عظیم رو عطالله مهاجرانی از همه بیشتر درک میکنه!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5335" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5332">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56b5549bfb.mp4?token=E5SWG6PtDkp4H2zARvU3pHwUbUOVR2KyhBvil9daE-6mkz2h69ymWzdp3mBrSzzWNO3UqXlZDddSM3DFZqobqYkVS_jWE2dZeU-ebQbQcmlxGHfUXfT5HYZsYcaOWSVebqUvOAwD0EjbU0NfmbS86iRGGqi67OpV9TbPZJOingvDfU1R5rYFegA8u4FCCLKxvQkuAMbg36ucGu701_QQ8guNsLggKOKXWu41Cl424eiNol3royg6oUx4GhZTQW4KcXNYj2u7wrtdJ0AONOf84t7BXSB-98Krn0SAIRcQAQ_-40OthJrc9Vm38Qaf5fsUKOVKqj13obRoq9nQiRofug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56b5549bfb.mp4?token=E5SWG6PtDkp4H2zARvU3pHwUbUOVR2KyhBvil9daE-6mkz2h69ymWzdp3mBrSzzWNO3UqXlZDddSM3DFZqobqYkVS_jWE2dZeU-ebQbQcmlxGHfUXfT5HYZsYcaOWSVebqUvOAwD0EjbU0NfmbS86iRGGqi67OpV9TbPZJOingvDfU1R5rYFegA8u4FCCLKxvQkuAMbg36ucGu701_QQ8guNsLggKOKXWu41Cl424eiNol3royg6oUx4GhZTQW4KcXNYj2u7wrtdJ0AONOf84t7BXSB-98Krn0SAIRcQAQ_-40OthJrc9Vm38Qaf5fsUKOVKqj13obRoq9nQiRofug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبکه خبر ، پخش مستقیم تجمع پیرمردها عشایری برنو به دست رو نشون میداد!  تشویق برای پیدا کردن خلبان!!</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5332" target="_blank">📅 13:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5331">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">شبکه دنا تبلیغ می‌کرد،   هر کس خلبان رو پیدا کنه،  پراید میدیم! مدال میدیم! ۵ میلیارد میدیم و…..!</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5331" target="_blank">📅 13:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5327">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bgO4UfQMOC9EIvACK0fY_F6ykrZT6Ltdi_UnuAX0W80fXhXvcYNGMV4RnLn3dA0TOCxXRFXKdqZ9Yub28Knn-wKAzDilPO8yr7Ql27To4PQQGqkywNkMEQwvkLLI2xiiLewewuxDyQcdp3IweCcEr0KvLOa-83qGnnrdlkzLgC6BhyxGPHTre7LV3XGIB9pk6d8xjl_6BGnS9S6vsxjwx6g0FlmvYQSZCi_2BDmRToe-KUACBcI1D5f6Y1kUFVmvsqs7Gv-a9nbCw_t5spxeZpb0WOTxqlMDoTCVY7ui3j4-DH--4eGo7CeLLCk2nylfeHLXCODxMDnLOzJaAKhI8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K8lJkHSDA98lZk2kl5h8x_SbGegJPtAqSiSNWqUbQdjF-nnaITI0NnNLmj9kvkoZmbXeKWcZkpDmMvWlvP0zCYunCH65AfXmnZhffg6UiuP6HJr1N3V--0qwdakSpYT9ak-k6SxxVx7Mi-MguGCIbS3i3fN_IFhBG6AKlzdzfj3B4K4GqixzzQKcpwWPJrRtDQINljJ62sQpZxq_QvH3QODmxdwsO9be2q23YaogvmDQccyDJbijUTDOGp-TH1WBY6zZ7w0eVJwrGZ9K25clQS8ucskqtMTvebepBNgWzWWu1Mriw53CSSg0HtJEJhk7QPDJnZDxOnAh74wfeJIIcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XXcLfFY9DlzcwoFmuNzqbLHFv2KwzS_LDyrXz21J4gSpsSShaoSTHqdrc7Dqn_ohUEHG-LOzPxthoB4feq_V-9rhKmJkldAvCeXImMQApiJS6FjDF0rjjPc-PLwZWUhGlyhNV6sTXF8x2PCgJlR4pq8kFwq3mtsizISTRNbthXGNAaPBw81vfTCcMj25IMsMKW89PEAPsQ9WHukeTbOWSTKNUwogkRcKlKCHTteqbnNoC71lNxid1sOsipTo_77GhoslxnrQTN6Z4NVOWffC8lTaOyGxj304tRV52WOhXygxTiHogtZvesL0q1rsEvZddJR4q5gf8Jk6K-a-CwiKlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IPg0ijHzWz7B15vY7v0gGEF3QucTX94VZSbVVOM3JRZ8P7iDiei-FKPe_cwAhds0vdpVXiDTWEq9nw5vjFVbU5SWxnosKhPiFyJoLXJ0rfIGXeG2W-3PRpfHbIoGSQwRWIcCvvj97grm4vhXIMXhYjr7k44_TMMX6yM3vonmUOSI9KNcCKn7vwrN4oWnbhMCmKy0rx5M2eU4bUeJi7dSqF9yu8Fk4H2_ZawgzyINya-6FUs63qAD8-2UjON_xWBeUjZmAk8mFaKaIoU9Y208A3E3bnv1twzNeLJsU047xPiIJ8JRQS52g-IBI9np_SsB4ji0oisJNVlxLwmKMrANcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صدا و سیما مارش نظامی می‌زد!  مردم رو بسیج می‌کرد برید خلبان رو پیدا کنید و بهتون جایزه میدیم :)</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5327" target="_blank">📅 13:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5326">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5ac7f4504.mp4?token=t__OEcjQZ4PaBN82rCURonXZaEUgw3HL9lBUZvHcDq0scnmGy6I_n4M9riPg4bgBV0MvBqa7M3bgwDCSED2Vekp2bBQe_h8oRNa_NwlbXfrDIKmBL9hMaiTOHLc18AJAZ34O2AWYp6mekScVu4bK9Qg8LOkD-3sFsj6D8DSPcRJBGg8qVsH7EJkt_5Ml4xf-cAi1THEhAlmIjt2InoK3UUA5bY0pDRgHTW_LLPMgHp_dAUwkiPIBUHaim678lcymCkU4TLyZovup95nCyGOZZhVawTzbXpzxE1kq9akjQsO4IRlOBtmssCnZ7Td_dXsSgsBVFzw8XexMBny9GxkJ2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5ac7f4504.mp4?token=t__OEcjQZ4PaBN82rCURonXZaEUgw3HL9lBUZvHcDq0scnmGy6I_n4M9riPg4bgBV0MvBqa7M3bgwDCSED2Vekp2bBQe_h8oRNa_NwlbXfrDIKmBL9hMaiTOHLc18AJAZ34O2AWYp6mekScVu4bK9Qg8LOkD-3sFsj6D8DSPcRJBGg8qVsH7EJkt_5Ml4xf-cAi1THEhAlmIjt2InoK3UUA5bY0pDRgHTW_LLPMgHp_dAUwkiPIBUHaim678lcymCkU4TLyZovup95nCyGOZZhVawTzbXpzxE1kq9akjQsO4IRlOBtmssCnZ7Td_dXsSgsBVFzw8XexMBny9GxkJ2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی هم این مدلی دنبال خلبان بود! در انتها هم نه ارتش، نه سپاه  نه عشایر نتونستن پیداش کنن و  سهمشون همون شورت شد که عطا مهاجرانی از لندن نوشت باید این دستاورد حفظ بشه!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5326" target="_blank">📅 13:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5325">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEHI31gOoyQMng9sZ0GFU9687dlxxRXYWZApsRKwbIDEGHJG4B0AxLLuLxmwYS941mIx6dcZhwDuXiHP0qqQO0FYCTFF6Z-7sOsTbBmrR3VpQS1_lymd06BHGlStoT9XrdrV226_53S1IZEZY69sERKcWAxxxsW8u9MIwNNGMC9nwC9EnNcYZS4sKcKXognSvOGLLbKyMcBpp2BdULwf54ELvE6HUjxbYleSY755h-b5cc1O9bTL9ejK6mOtSrKvRcZCqxPM4ZIpQI0a_UtnVQESotq7k-g2vjjeNU-aOUkOHQDKQxjr4E5910x03KPpL_OUCK72ILQV2JfKiDsb6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هلی‌کوپترهای آمریکایی در جستجوی خلبانشون در عمق ۵۰۰ کیلومتری خاک ایران، با این ارتفاع پائین حرکت میکردن! در عمق صدها کیلومتری خاک ایران!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5325" target="_blank">📅 13:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5324">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a614fd1e8.mp4?token=oC1zryE1-8Ea8Gn6rZ8DkDZgCo7qa4r6Xi7w0dc-dKYYJKjiOaMmWHTxKjVEQ2Fhp_GhskwIfxDAW3G_5SUw_SFY0Mf1V-dVor7WEr3L58bGrC1g9Cnzwt5TaYuPXKtcEADr4w_AP4CH8PzPMiw0-GfvaneqgQabzpouSBYu6GutNB_2kK0aW2erWeBWhqqqUBBWwFzDlJLcm5nciSVhIafkNFUq1XRYvUPVpr5OjwpcfwC57A6UUVVgAGHxLVmi7LVvdCRt5PH_dHjl1OZrYSlZ0no5P2YKmbCnIliScJwWRFxjwQJXRKsPVTah0FQg17yRi4i8eytO5QyW-aGS_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a614fd1e8.mp4?token=oC1zryE1-8Ea8Gn6rZ8DkDZgCo7qa4r6Xi7w0dc-dKYYJKjiOaMmWHTxKjVEQ2Fhp_GhskwIfxDAW3G_5SUw_SFY0Mf1V-dVor7WEr3L58bGrC1g9Cnzwt5TaYuPXKtcEADr4w_AP4CH8PzPMiw0-GfvaneqgQabzpouSBYu6GutNB_2kK0aW2erWeBWhqqqUBBWwFzDlJLcm5nciSVhIafkNFUq1XRYvUPVpr5OjwpcfwC57A6UUVVgAGHxLVmi7LVvdCRt5PH_dHjl1OZrYSlZ0no5P2YKmbCnIliScJwWRFxjwQJXRKsPVTah0FQg17yRi4i8eytO5QyW-aGS_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دستاورد عظیم کسب شورت خلبان آمریکایی چنان برای جمهوری اسلامی غرور انگیز شد که عطاالله مهاجرانی، که برای سالها به عنوان روشنفکر و باسواد به مردم ایران قالب شده بود،  گفته برای این فتح الفتوح عظیم  موزه جنگ راه بندازیم!</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5324" target="_blank">📅 13:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5323">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_xMUShbNBGSoUhnhepgqEZkAl0tV1kTwWsAYoobHc6LwxKOgErvMjwqr4IWquWw2q1aQT_G1k3WUV4dMCUbZAUU_kzXtO6wa80CW_txRaB0JSLeZp8mwejBiI9271YW2qALESssp6EAj41YA5YSGSWrcoH71ndV3HJdQLTloRDvXKV93SuNSV3vbPONMqszW2xhgTWVXG8Lc8hJUw2oz_PdwPXfICLvAgMgmpeT_bwbYuPC0HuaLetieP08FIS0FGDM7vdPeJ0XtGh1MiczL6bBz1CtMtLmJDl9hp-OQixTVm6BQZHjbdELO2b96oTx6rAWAO4yeEd9JvPfD3ts1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نبودید یک خلبان آمریکایی  در عمق ۵۰۰ کیلومتری خاک ایران افتاد،  جمهوری اسلامی ۴۴ ساعت همه نیروهاش رو بسیج کرد اما نتونست پیداش کنه!  در نهایت سهم جمهوری اسلامی  «شورت» یک سرباز آمریکایی شد!  که باهاش عکس یادگاری گرفتن!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5323" target="_blank">📅 13:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5322">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/row-l4ALR__9dgpN4PoLNMu5q2WsnodDF-4sXfq-l9p-4TGw_tKqFtqwi-eTKB1LkJw0N5xfnLV0cQFwvvEun6X-WBcZu8CQxnes_-TOFUs7o-m9AMSRXCTidqBwWH3pHxn3jDYh4ncZwN5bVXfjDL8eGlWMK_n0_WcMTng3bpSE2sLdAtAhzJnTOWbsftJhROxBjJcX0F260ziebQ1ruDmzsSUNMINu8jrjtt13kCf0oJnBckAxRhSuBGQMUKpLayB1r20WZvzhnL1q5lIeHtfZiXTKO8mbs4rlKCJnTkIrY4XphKALDKrGBlspoxkoQ45tcDQVYpbv85fv-vC1Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نبودید یک خلبان آمریکایی
در عمق ۵۰۰ کیلومتری خاک ایران افتاد،
جمهوری اسلامی ۴۴ ساعت همه نیروهاش رو بسیج کرد اما نتونست پیداش کنه!
در نهایت سهم جمهوری اسلامی
«شورت» یک سرباز آمریکایی شد!
که باهاش عکس یادگاری گرفتن!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5322" target="_blank">📅 13:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5321">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66cef5c3c1.mp4?token=lCiIpGAJx_YtDcXW-8pGBm5niCZz11EYI_nqRSQ19yXY2XzTfg6cxScFwnH3N2HVufJNJSadrosW00ipQReKuFPNdZx5zZdYHt7K7vpGm9xLtp9KIMgVdkBnDHw1kvfh1r2ZnY1nIshF09SO9awy4Q9iJxmzyjVhviroz-yO3ZqAGHYoQ4EjqeHScnSM0TqFlS4tPb6BjAWE1A3LHkepnyVRR3rAVdLw0kab2vmERwmiddSWiMzajjgfn88dd4Ms5RWRUfnh9CYUkV9cRFNQVA_rOsu7ZYmPFzrKguCIqz7AHWfWti57ghNgwfXhc2cBLH2ks8h7vevQQbHEjSiQXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66cef5c3c1.mp4?token=lCiIpGAJx_YtDcXW-8pGBm5niCZz11EYI_nqRSQ19yXY2XzTfg6cxScFwnH3N2HVufJNJSadrosW00ipQReKuFPNdZx5zZdYHt7K7vpGm9xLtp9KIMgVdkBnDHw1kvfh1r2ZnY1nIshF09SO9awy4Q9iJxmzyjVhviroz-yO3ZqAGHYoQ4EjqeHScnSM0TqFlS4tPb6BjAWE1A3LHkepnyVRR3rAVdLw0kab2vmERwmiddSWiMzajjgfn88dd4Ms5RWRUfnh9CYUkV9cRFNQVA_rOsu7ZYmPFzrKguCIqz7AHWfWti57ghNgwfXhc2cBLH2ks8h7vevQQbHEjSiQXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قاسمیان : سربسته بهتون بگم
امورات دست مجتبی خامنه‌ای نیست.
قاسمیان نمیخواد بهشون بگه
«چیزی به اسم مجتبی خامنه‌ای اساسا وجود نداره!»  میگه : امور دستش نیست!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5321" target="_blank">📅 13:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5320">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vr7SEwkw1PNrnCSHFrzMVPiKufTxM0Vwb9fc2RFdLr2hGLP1HWmEdVZx84PnDwWm6pfH3gXP54pbfn2FSWsEiojh3UrURRqN1HWIgGRdBGa0rvbAxLX2Ao-ILydEHAY0Ig6HliEHfGQ2dbYa1d_VAbBFHFZ12Kx5X_LAsCDpS5boy30IEzX_k6bw2ynRfOM4viZ561-aZd8JxHUCt5y6FjqnGMFpLazqRsb5cJ5XtukDHaVKR8B2YDt5WiLEO-fizeQk8ZZVNxetg2uWkNYVxLIN-COYO0dvkhhn0aaanL1JbRU53FfTm6J3WWJ1fZypP4G-x2OA-pjFn3Pxe57W2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5320" target="_blank">📅 12:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5319">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93fe3a5cfc.mp4?token=GnEGHVE7TbAdRc8yguKV32jnT_Q7GODPllGo9VQ1YVttc7KdlZVuQ-Q4MuYi5hSWQFGqwKN7XSuD7BdrLgHhV-qoH1YUNO27Hy6ZwRDUKCjMqTBK4Wj15ZbFqRjz-x6ooxr9W4d1TOfTpDsogrXYY5xOLcKU1sKv95OkYcaxm0mPhl9h4h82vr6FOo1Fr-v2EM5-YZ0MrQjbkuCIG59mgBIg2Z-28DZiMdQW-_nAa0ZbCTncLvYW7ZpUCT3OCF-nwhbf4cjsA_H_UKEDCGj1syBtk34ekf9O6G_6uWgsQhCvlNXyiHqPJDYHIEDEAeDVEb-16sl_IOyvfmKMYSeB9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93fe3a5cfc.mp4?token=GnEGHVE7TbAdRc8yguKV32jnT_Q7GODPllGo9VQ1YVttc7KdlZVuQ-Q4MuYi5hSWQFGqwKN7XSuD7BdrLgHhV-qoH1YUNO27Hy6ZwRDUKCjMqTBK4Wj15ZbFqRjz-x6ooxr9W4d1TOfTpDsogrXYY5xOLcKU1sKv95OkYcaxm0mPhl9h4h82vr6FOo1Fr-v2EM5-YZ0MrQjbkuCIG59mgBIg2Z-28DZiMdQW-_nAa0ZbCTncLvYW7ZpUCT3OCF-nwhbf4cjsA_H_UKEDCGj1syBtk34ekf9O6G_6uWgsQhCvlNXyiHqPJDYHIEDEAeDVEb-16sl_IOyvfmKMYSeB9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تاریخ مصرفشون تموم شد</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5319" target="_blank">📅 10:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5318">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMTUeDyprY01cGAFOUVALqGzwjoofiH175NZ3bx9XxVJk88Kz_fyREV3m-f3RlDLAG-Dx0HXr1_808-tJNjkITn6sUC4Yb74kF5omVseUAqZkDQlcdQPZF0JEj-kXP67PwCEoPjUfSCkjRVh0c9fJSgSmcdp5i5sdj9nv8kLM-ladJBLfWSvyxmjY6PQ5J1gFywaCtkpfaC87LcU2_uVzuqi0SdkhPnjYvLago8JINd95-gFb688KKCUUXJCQMoCY1T76kIKHnemB4VZSpl9Vj3Qdpz6zTHnw_R_36YzbjA8xP79J1sNQ7ivhPvP-3Zaokd8lIhoIjohLS5g-8ZAlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5318" target="_blank">📅 09:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5317">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">سی‌ان‌ان به نقل از مقامات رسمی آمریکایی :
جمهوری اسلامی به سمت تنگه هرمز چند پهپاد شلیک کرد.
ارتش آمریکا حداقل ۴ فروند از پهپادها را ساقط کرد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5317" target="_blank">📅 02:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5316">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله به جزیره خارک</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5316" target="_blank">📅 01:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5315">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dor9y_BG2_q0A5VwjnXp9CIS1wfjLQu-Oo2Br-FGXsoEo9FQeRtg7VvDqQ3IOPpljc43Lulnn2NI_J7hpLKwMDbd2TZmW2KMrRIYDOo06v0jdZEswP3Mqb8Dgrk1BPhu40z6Qsjf_aHBMG7c9XGwE_n7-iIrT8LB5-zFhZlGYLjleHp-1FgGUJsuApDklDt7Dm9Lc5bZoFQLgeD2P9NVEVF4YntHcFrFzcdqYd6aNCBpSCYqoo9cLOiFxyzt4_8Mjk4H1sFbq6pxoBspFRZ-OMfoLxt_9UAsjtr_lOKpJAaGpSFNKrTmH2WQRrOoJqubH7z3OUCMbNI5mwIjNN6JGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5315" target="_blank">📅 01:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5314">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
گزارش‌هایی از حمله به جزیره خارک</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5314" target="_blank">📅 00:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5313">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LsOxcAWkEHoCX8ujoRRZZQl-Mk455wdw_3WN-i0bRAy3kVI9n1XBXUtPtEe3qtLuNg-dOjkf2qEtnkWqlhVTuqJsYQZcdi4Bhj3HVLG0RaykUVqdbhvx10Ph8vi4LhGrtHC6xa3e6n0j-ZeKo9u1_fAC1b00m15Uky6eYneie3nVJH9umXk0RmbYbWh-3SQ5EYK20tLq09qugz5DgxDfautXjCwKKWtV40jN-knsmxnWy9HorWgSZ63BCaRILQKxCjrX45VzC20tXhruZ-cvXEnT2Q5qM9fL36jo1iAw0UEaIVzKfvSVbm0lN0cwfAjRELIyGmmZFDAcuX5D1Gi71w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتقاد شدید نخست وزیر لبنان از سپاه
و جمهوری اسلامی
نواف سلام با اشاره به توافق به دست آمده میان اسرائیل و لبنان، برای آتش‌بس گفت: «ما موفق شدیم در لبنان
به توافق آتش‌بس برسیم.
با این حال،
مردم لبنان دیروز با کمال تعجب دیدند که سپاه اولین طرفی بود که قبل از هر کس دیگری آن را رد کرد!
این کار تأیید دیگری است که این جنگ، جنگ ما نیست،
بلکه در سرزمین ما
و به هزینه مردم ما انجام می‌شود.»</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5313" target="_blank">📅 23:16 · 15 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
