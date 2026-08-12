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
<img src="https://cdn5.telesco.pe/file/nEo9_qyHk4y-qkv4wdwRuZNyycILKwknw8fXXCAlnEROtOZNuwVSajMkaAF-9tRvZFfjB1MPVySuDtHW4vnw8Px9D0XpZHFfTEMdpJW1CUv0hDYjAXGqFk-19JvLL2nyRWsbqTSDfV7q_JZw_DhDXcaRMqs7Q57Q7FzYo-ZWT9CRP-3lz_fXT_tYcidu7WgygFzI_0xG9ISafolMsHW5a2eG-Jte8xLTQmTDi1VAUG-KdbmRhieQpmVWhwjOd6WnHFMEBdseRbwbMEEtSKMGr6vQgi272qIORfysR000zof2UCgW1lTS5PyT9OiEE2GV98K5bHaBJSlNzmtAr4sunA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 474K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 14:22:24</div>
<hr>

<div class="tg-post" id="msg-103444">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81d1d4d2c8.mp4?token=lvBRETZpE40h-7pzmq1Qva_8IYxcQ-kgGjyjND8u6zoRZrA9fQSzed7UJhX6hza2BQ23-9lnwTtwP9yJCL0He05E8YOXUIDyHMprywPFLhSiLTSu_fF6paxuq8rPcnRMLKaho7LtV7v2EIYDiJFnNh6YOslhoxnw236_Tx58EnKGJCzD0HXSiI1D0Yj4T8_kJHbtqVxbFDoWWZUtRCWexArMbOZ5hGLLN1_4Y57Xj9RBxnedonZdA2oWP6FYlD6w4PgIfv5Fa8Wrq-JWwoEB3wKIfIo_glUZSaXiAVHyQtY-jc36MazB1Enp_PrUs7I9xw5ljbkbdzYCZkbZhkZghA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81d1d4d2c8.mp4?token=lvBRETZpE40h-7pzmq1Qva_8IYxcQ-kgGjyjND8u6zoRZrA9fQSzed7UJhX6hza2BQ23-9lnwTtwP9yJCL0He05E8YOXUIDyHMprywPFLhSiLTSu_fF6paxuq8rPcnRMLKaho7LtV7v2EIYDiJFnNh6YOslhoxnw236_Tx58EnKGJCzD0HXSiI1D0Yj4T8_kJHbtqVxbFDoWWZUtRCWexArMbOZ5hGLLN1_4Y57Xj9RBxnedonZdA2oWP6FYlD6w4PgIfv5Fa8Wrq-JWwoEB3wKIfIo_glUZSaXiAVHyQtY-jc36MazB1Enp_PrUs7I9xw5ljbkbdzYCZkbZhkZghA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
دل‌هارو ببریم به سمت دوستان فوتبال‌باز قدیمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/Futball180TV/103444" target="_blank">📅 14:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103443">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fba285851.mp4?token=UHpGNDZoQ_3H6F2N5lX3pEvQiNA84jE6v8n1WR_PpdlNl0rsu4KHiDXJyU0kro7F_DSNZBc9Bm5WWZ3-ycu2jcE0E4JALZdVvZXQMwtl6R3_0vpZKfSSY12DCwLxs20juVKWLNmygSezswusDeBS7xWCVwtUEIfHXRRpg-ZVuc2ajATaOXts2QC1g2eeATVLBvZRJEHRJ-2gLykgDOB6Z7XxaJoxMAHrDchokpeDrFjFV4IR30fS7nDPAmn1WgFqWM17NmdgOTaGp3GuY1OuyoYPqiUywQVdwF3dZGdrRVGmG-btoR3-ZL-hoegT3eIIGavzg1_ac6f_EVFhfD5KfzssS-yiXO5hsEYguMXhiYylyxyPUB335RqKa4D0v59j6qtrUjAetb5Wrub2cY4_ofM147XDpKs_v5vIPDVncNPFqzg9ofOXzLla-N4sUbS_7t-CvQZwT42IDkqAhNfa4ytRxL0PENV47SAPUMhcZHpupFeydIx-rxCSmeCmfqAyDhY71ukoZjGNv0cWlQ0StuvwP3bAG7-lQdC5TsCcYAnROvE_bErp9xUhqM16Mlo0rQLOHQWcSGKPVFaPmGsxuPHSq5cCKSFJH20qMgbnORpwiK2MQcY3aMPVbqeoys4zSM-36T51X6_PsqGimwRQTCbmTiFtViZgkL7a2jXIvv4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fba285851.mp4?token=UHpGNDZoQ_3H6F2N5lX3pEvQiNA84jE6v8n1WR_PpdlNl0rsu4KHiDXJyU0kro7F_DSNZBc9Bm5WWZ3-ycu2jcE0E4JALZdVvZXQMwtl6R3_0vpZKfSSY12DCwLxs20juVKWLNmygSezswusDeBS7xWCVwtUEIfHXRRpg-ZVuc2ajATaOXts2QC1g2eeATVLBvZRJEHRJ-2gLykgDOB6Z7XxaJoxMAHrDchokpeDrFjFV4IR30fS7nDPAmn1WgFqWM17NmdgOTaGp3GuY1OuyoYPqiUywQVdwF3dZGdrRVGmG-btoR3-ZL-hoegT3eIIGavzg1_ac6f_EVFhfD5KfzssS-yiXO5hsEYguMXhiYylyxyPUB335RqKa4D0v59j6qtrUjAetb5Wrub2cY4_ofM147XDpKs_v5vIPDVncNPFqzg9ofOXzLla-N4sUbS_7t-CvQZwT42IDkqAhNfa4ytRxL0PENV47SAPUMhcZHpupFeydIx-rxCSmeCmfqAyDhY71ukoZjGNv0cWlQ0StuvwP3bAG7-lQdC5TsCcYAnROvE_bErp9xUhqM16Mlo0rQLOHQWcSGKPVFaPmGsxuPHSq5cCKSFJH20qMgbnORpwiK2MQcY3aMPVbqeoys4zSM-36T51X6_PsqGimwRQTCbmTiFtViZgkL7a2jXIvv4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
⚽️
چالش‌جذاب و دیدنی تمرینات لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/Futball180TV/103443" target="_blank">📅 13:35 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103442">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOVbDxsxFAwhgDQU6dh9v1ZTbbpnLdZ9dQwU3Sf6320iF_SqB4QHjBcPkZKuOI40c5-j3P57AVZP067-w6S9a8iJFVsu0_5XGjeKWq8SUrRq_i5wMn4kVYjDgNamDNWA_pSCMjg60XybYiZFOkNOWK7c3GfBSJQjSviB2s8WkxOnobc3djP-pQ-_IOuWL_amaeQRN3SciRYaRGHDdh_ecUOwce0Xf_LlhBYpHJm7Ga-fC8VFTgcafdgLksDX2j2tSGCyw6wTgO2jDrGJM7zuoJ-8sVqYowmvawHBrWsFGjiyxWMtA4afwSeWuwb7U_Uxrnt4ZHvhb1AH1eh4PRiyiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
مودریچ و کارواخال، پرافتخارترین بازیکنان در رقابت‌های سوپرجام اروپا با کسب ۵ عنوان قهرمانی.
🚨
📊
🏆
کواچیچ، با کسب سه عنوان قهرمانی از سه باشگاه مختلف، رکورددار است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/Futball180TV/103442" target="_blank">📅 13:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103441">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc3b0e5a8.mp4?token=hj-CnmPBeRfbkQSiaz5crrKDWKSMo-kpSryMGcx7rzp80CEYljiiCrhpNGfjNw-7hh6-IQWfSZZwJYALeemJrkeZaM28EZHc5VvUzFRjO68IqErnffasOBRHGFuN7wybYFlYfNQXQEQJI-yStN_iQZ1J1kKLA9cbYbdU8SXh4aWjEci_puWkknUYywXyan0-eeOitZCuhVclwTi6Hw-5r_8H3cWCbSMJM_TcsiW8GPqlJPBr5Ho_8Dk5trISrLJklz9pWSVWJWOGJvcpI48_huPG0yRJ7BcvBBriaF64XGkos7cXP9IVa005owgDFju30fuCLAphUuTxsLjWhiLExQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc3b0e5a8.mp4?token=hj-CnmPBeRfbkQSiaz5crrKDWKSMo-kpSryMGcx7rzp80CEYljiiCrhpNGfjNw-7hh6-IQWfSZZwJYALeemJrkeZaM28EZHc5VvUzFRjO68IqErnffasOBRHGFuN7wybYFlYfNQXQEQJI-yStN_iQZ1J1kKLA9cbYbdU8SXh4aWjEci_puWkknUYywXyan0-eeOitZCuhVclwTi6Hw-5r_8H3cWCbSMJM_TcsiW8GPqlJPBr5Ho_8Dk5trISrLJklz9pWSVWJWOGJvcpI48_huPG0yRJ7BcvBBriaF64XGkos7cXP9IVa005owgDFju30fuCLAphUuTxsLjWhiLExQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🤯
💸
وقتی استاد فیروز کریمی بیشترین دستمزدی که در فوتبال گرفته رو لو میده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/Futball180TV/103441" target="_blank">📅 13:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103440">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79bf3a3f4d.mp4?token=ZllDaVjz8YlkkaPb1rufhhsQcBhbpub1RR6xcrlF8OrKAvBskWSmW6LdT4XVZX23Cdvrh5ZeWyx5znjyFoy4KErjKC63Dk-NTNJn5FS0G8aKrBRa_LVcI1--XoMqlHCHn1vLZ8035ZFjryB-uNr4puXphH-qV9gKDJhmhRsgCW5ou9y-rbEqq0GJoPqaf3EkvfqKEKUgnJAlyrFko8Yy5_JnjFCdXdsfHfrvB9Q7Dpg6OObtiYNB-ypfjV3So7OFMNuo9jZAvlb8vIlwseG6eYm9bpYgyNcH_BiIfclLEEnbHFX4Vk_Bk8qLZLwaqlyjGeCsR8zky7OMTMtHnEJZMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79bf3a3f4d.mp4?token=ZllDaVjz8YlkkaPb1rufhhsQcBhbpub1RR6xcrlF8OrKAvBskWSmW6LdT4XVZX23Cdvrh5ZeWyx5znjyFoy4KErjKC63Dk-NTNJn5FS0G8aKrBRa_LVcI1--XoMqlHCHn1vLZ8035ZFjryB-uNr4puXphH-qV9gKDJhmhRsgCW5ou9y-rbEqq0GJoPqaf3EkvfqKEKUgnJAlyrFko8Yy5_JnjFCdXdsfHfrvB9Q7Dpg6OObtiYNB-ypfjV3So7OFMNuo9jZAvlb8vIlwseG6eYm9bpYgyNcH_BiIfclLEEnbHFX4Vk_Bk8qLZLwaqlyjGeCsR8zky7OMTMtHnEJZMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
✅
بواتنگ از خاطراتش در بارسلونا و استعداد بی نظیر مسی میگه...
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/Futball180TV/103440" target="_blank">📅 12:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103439">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o46hayq4efUwFr0hQcRZzjyRF75q0gR70m25VS7DqXqT-5WNc6HjjzeNiFM2bC2M2j2lgmKZB9YnjdmNt6D9mjFyJ-NFx23TY3yPfaOUsE6yvIhryuoIcOsTn_a_ZrYss32mO1xufkTTi6kT6Db2ub7bkS3D2_8YkYQMgZcXmUdReeXAMfbQn6Ql5hlrRFmiFkMCO_tm-az-99kb-yNRTQBYBlkZjOATIumNLjz2Y2oH-oHtTihUjSpLEKxxI-behQTWsb3yyzk_Uo-e4ZI7rgbsvSAX8RbqhyUUeh1blxGZGkowK394DJ66NECkLpn7iv9N5mSr-T-vsv6uDjirJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
🇮🇹
🗞
رومانو: دو باشگاه اینتر و لاتزیو درحال مذاکره نهایی برای جابه‌جایی داوید فراتسی هستند. رقم پیشنهادی لاتزیو ۱۵ میلیون یورو است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/Futball180TV/103439" target="_blank">📅 12:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103438">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/531604864b.mp4?token=REFX26g8WM8HScE_169m9YQpNjj4VGUQ2l6kGIR1cdEvPwxqLr13CEjI6vYTbPKuWFjf9-4pMP2WmBG6UVeXZChd6iURgKmJx4SQjr-OICHX6G_UIopZvEhj8Y9OacWxvIxroZagcmaD-E44RE8OLclywBS4OP2g3SwTPrdFk3_NhApwC4ihF5SZM0vMNX_w1XMLGWfVLqw76x9EPsm5Nhs6t-mdf6GTbfEWncFZ8Fc5CyFeBevw-6P_2LnDlAn-_o-wtSa7xgVF_mhYaw31cySFzy30fZJA32tuSPsjVtB0Ko-C0W9SgqzEoDUv4sNxw2H1FX9WQfHkldMM43pkhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/531604864b.mp4?token=REFX26g8WM8HScE_169m9YQpNjj4VGUQ2l6kGIR1cdEvPwxqLr13CEjI6vYTbPKuWFjf9-4pMP2WmBG6UVeXZChd6iURgKmJx4SQjr-OICHX6G_UIopZvEhj8Y9OacWxvIxroZagcmaD-E44RE8OLclywBS4OP2g3SwTPrdFk3_NhApwC4ihF5SZM0vMNX_w1XMLGWfVLqw76x9EPsm5Nhs6t-mdf6GTbfEWncFZ8Fc5CyFeBevw-6P_2LnDlAn-_o-wtSa7xgVF_mhYaw31cySFzy30fZJA32tuSPsjVtB0Ko-C0W9SgqzEoDUv4sNxw2H1FX9WQfHkldMM43pkhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رامین رضاییان بزرگ
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/Futball180TV/103438" target="_blank">📅 12:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103437">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHVnJ1GgZLSKz7gB96UEA61lcWRS8n7SsrM_gbn59sdVw7uCuJInITBGn0UC3HydcAnf8conSUaUeo2ToaBwxGB97IOZP5MZMVggnZ37FSC92NgeqNvaXpr5EzB8pV7QrIMfun7JbfUS8IP9IvTmIh9VApBSeVqazuFRlWnt56j0Gq75EQVO1gYQRcyCKAMQvV6-2cOwvrZ2gCTytvI1cMB89t8JwXygQXfNM_yig2dwh60lIzq12C3Y1lQ1lTbAHW-U4MAj_9esb9SN2glTZX2IL4xJxznXwZimElIEob3oGi6b-YrwP2RDM0J9S8gnGwjfvbPg6eHlvBmFNNgyOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
✅
#فوووووری
و
#رسمیییییی
؛
🇹🇷
روملو لوکاکو با عقد قراردادی به فنرباغچه پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/Futball180TV/103437" target="_blank">📅 12:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103435">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q8e9ke_QH3moW6NheZwiOpvhK91OaLCusVEGk6HUwyzYo4C69zC1kBIjxRIBAt1pM5D7egkay0xMiL0SpgqaxUhne1zlC3YZQZP_AEpTKCPlWr7uldtcOrOCIcIPTT07-vBBC642csxQmswv5SyQ8NBClzZs72-bpnx8p5BqlyGJ2oIRkd4UahsUCFWVatMrlRtM8U3KyFnSR61GvFWve3OK1790HpB3ZIZkxFoYaXTVkjyVWLdRMj6bkHwIP3mg7aTGn_kpp1keNNhXu0J1slE5RAZxQfZF5p32WPf4XN4krf_YWSxIXMp9KWqXKfY-0_CQmRpxrSbd5ZbQfAYT_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YEOTBJAAAib5GwjdVZydyUrRf44vwCTahYd6gUz2yW9x6EZm9-S_7zqYJYdUUkutb18XUtJz5gaX0XdL6ZkaGJl7UOQyIOEtQMkUKu1e_9eddo7Teh7Mxx7zDMN9mz9RjHM_5k0GI4pptNUjf1HUQKGOwcMPO-F2gymVsJpO6WJMQ6TQbDbSO4DqdAw9HWbSxH9bIOnLoBAF2SdfioOuMzEXsvQR-pDUbkY-VizMGYmd-3AyQR9QMgSBQApeyldde9WYuhT9YwFaVp_UC5ztgPCWtH9Kp1XcbIanyDs6ih49upNyT8CDuUMUJ0yzDIF-WzRs5J-NfWP5XWmIAE1gNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇷
تمرینات امروز اتلتیکومادرید با حضور آلوارز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/103435" target="_blank">📅 12:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103434">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba2ab6526.mp4?token=FwVHgexyrsMgghrVs3X43PHCd_pPuZOW66vd2Cv2dzUCLWQi_XVtpZ78ZRYAfvGjQi6NfkeK7JBH87lQ6qdCJon3j02KVGhlBhj3Q-A6YxNe7DvVXb42LoIVgcpMc3m0ANixdy594vM0U35m_03WNQs3PIPMuveVj53L_l2jlLNzVCeCV5_S-jiD2dei899_HiLQEudZasC7ciWLGiXlo4iFwLlVoDpoaMus56rSQbeSx8FLAsY8LI91lK06aOJA4ZQTaKwh6yQwX22yxLeT5cUpQkADui1UBI36MLZBAnbzbKifNysS-k4gCTnmMQUE2WX5NmiwFwPZUnhn5X09rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba2ab6526.mp4?token=FwVHgexyrsMgghrVs3X43PHCd_pPuZOW66vd2Cv2dzUCLWQi_XVtpZ78ZRYAfvGjQi6NfkeK7JBH87lQ6qdCJon3j02KVGhlBhj3Q-A6YxNe7DvVXb42LoIVgcpMc3m0ANixdy594vM0U35m_03WNQs3PIPMuveVj53L_l2jlLNzVCeCV5_S-jiD2dei899_HiLQEudZasC7ciWLGiXlo4iFwLlVoDpoaMus56rSQbeSx8FLAsY8LI91lK06aOJA4ZQTaKwh6yQwX22yxLeT5cUpQkADui1UBI36MLZBAnbzbKifNysS-k4gCTnmMQUE2WX5NmiwFwPZUnhn5X09rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراسم ازدواج رونالدو و جورجینا.
🎉
😍
💍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/103434" target="_blank">📅 12:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103433">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aav3XhgwTNSeu7vwujwjo-w93KgtUcg5r75-0pFlTUh2kmBhrEHU_J9MlHCWkbQReNH2gkFtiPVyKETZMMz-EYbPvWxltMBfF2XSHcfyzDkRzxdSkwH0JefIfGKB3rCf-lWOAzuj9Uhz7saFMXmK6zSaA5w_EZyo_OCLYOE4-mP9S6LOeSXr1qOOPKkH5NEwEDqSpRNoFuXsVost39Q03tmMnIC2OD9pweoYboqGvndA1uF5AKf6Ro5Vrj0kRjDD3UxTSt93kw0iRix2iYUZtbPsDwSs0GPtqgv76kDy9Fq9lQK8_enibTf8d67QUVn74c49DJr4kYq2Wu4cQpazGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📱
❌
استوری تند روزبه‌سینکی دروازه‌بان شریف فوتبال ایران علیه رامین‌رضاییان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/103433" target="_blank">📅 11:48 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103432">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uilfk-YrW9mWl2ECOBon1nmDiAig7okE4P0uHt9xq78axI7sBbpSN_0a2-kr3sbTeyRaZuY7FO0F0kRgmJKvDLTJagrT0tW3NPb1VohJYTTAWIYb0LLeJEO8aYrem05ICk00ns01r_bCebcVC-pPa2yKSkqClWvpdP8ZjPWa8y10tdeoDZ45b5PiHo1QJkyrVpl9HVizzULgNUd7YZvsDUc1v3jBHQCGIq1T8pJjYIdzTBbb3SiMWP1YRPSVa5hdUJy2AR-vwKJK75Nm7vw1k8RVARExF0I4eX_ATmNi_XkvSvcCLEu39Rj58GUOpWqY8i6tZPedXNeOhskaDjlI_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
قیمت‌بلیت بازی تیم‌های فوتبال استقلال و مس‌شهربابک ناقابل ۳۰۰ هزار تومان وجه‌رایج مملکته
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/103432" target="_blank">📅 11:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103431">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AnD5J9DrIfQHc_IQBBVEemy9Q20_1G3kLBrfwHJTvPIN5rXlueuC6NwRe-gkyllgEngATTFlyYPlCodUPThlACcKecooadrH4pQfg6viErkO7m6AfgvOrd2UZUL9yFZ7OZMicBHu1BGOxX9E0F7qZMqAiNA8p_aCjzv0HFnSG2s6x7Mzcgew_xXorjHon81gUSCqXXDATKCtqS9YEQOptAQ_2IraBcR80RhHtxBfaNFrlB8Bq04tfQaQS-X-fp0UY9zP6FATN7xXi5tBqMo6R6LwTSDaawvcZBVIuJgPydT8U0E8AB2roCQpzVP8iR-2xvxJ7LtKiEUDDWGmViybrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
رونمایی‌رسمی از کیت‌اول قهرمان‌فوتبال آسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/103431" target="_blank">📅 11:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103430">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emL1tD9i5SDeaUv_6saGmTLoGWl3ZawLGtaIK1cE3br7HRxmmI0g86lFbF4UJK0525yVLm7jQi71yIC2UdrZW7-PyfrGAHN71W_v_f0KXEcrLCnQN4N1Oha5dFM8D5ohuSO1nFl1XUJ5hMy1D1yt-8pSCSR0QKlhYVJc2R5tRvPHlLEtFqB5J-fQ5feUjT5peTPmS_Xy5mNk4Gz8P9operWQCNIai6UPdLTtmRpCMQP9EXAPPT1GH0LK0WUaAY1gbEhkHICa7Vhqg6Z-PEsiAPK1JaAifU4meSa6AQ0Z758tyc48QoRCKKh-sSCnc-NsxiXRonCew4DDs0nGjjeK9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
✅
⚽️
#رسمیییییی
؛ باشگاه چلسی رسماً اعلام کرد که با پپ چاواریا از باشگاه رایو وایکانو به مبلغ 21 میلیون یورو (همراه با موارد اضافی) قرارداد امضا کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/103430" target="_blank">📅 11:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103429">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWjH9KVwxvPHl95F2DxT1iM8u6Q9EqvZpUgEyj879aoWJKzfiwb47gu_Fv0XmRZ08druEM0xTcTw_SPugeBmr2lezyJ7WfVERzdH53uRw4isVKolBcuDxWHm5lfttTJ1aRVCwiyeBFzfpDcaPr9HkXSvrybbYusptpAidVCEFCP67YiflZ4kfKWNcJPWL709XW2E_JxfAlP1IxbxuKuMkg1wU48O4EH74ohFRIwQI8QX0ahgGS198b6dcsk9o3D9LbZ6teR37XNThnBiObbGrhJZUgWQI-ok9XcPXDlXxDzbKrfEOa07326mV_MBQ4plmBQRjEckQrytRmuWOf-2hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📰
فابریزیو رومانو:
🇪🇸
پیشنها دوم بارسلونا برای رودری به مبلغ ۶۰ میلیون ارسال شد
🚫
🏴󠁧󠁢󠁥󠁮󠁧󠁿
سیتی ۸۰ میلیون یورو می‌خواد
💸
✅
انتظار میره روی مبلغی بین ۶۰ و ۸۰ میلیون توافق بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/103429" target="_blank">📅 11:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103428">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4QJ7iQZtXf2M7fdvAxt5Fa6bSobr_IL5vCNkA6eidhjPjHUNnXECrzHeYMTJyI7mjlT5nAABNOoc9gwDDa4D_p14w3NVJtjqJNEHYmIu7zLKFUTU7maeMBHnilz4-ViYti9LiNNqDsVzzuut0SyQWQaD1H6ZnMc8ItZTa0D7YA1Vus8ZCCmzDvfP8ZXU2SRo0oeF1j21GZXH0CSBOrfvvxeqCWDlru83dwJ5tEZhDLPujOaa6oJSsB8ZjKWvmUoWQ6AxTM5i7spYz26-TmVEi2CtlGEZSKAKxdQW5otsXpyom0Cj_7HBtmXm4VvIzw9Txu2D2LxCMXMLK0vTifqZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رونمایی‌رسمی از کیت‌سوم و صورتی رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/103428" target="_blank">📅 11:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103427">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/103427" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✈️
اپلیکیشن MelBet
🥇
🎁
کد هدیه 100 دلاری:
Sport100
🔒
برای تعیین رمز ورود حداقل از 8 کاراکتر و حروف بزرگ و کوچک انگلیسی و اعداد انگلیسی استفاده کنید، مانند Hamid120
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/Futball180TV/103427" target="_blank">📅 11:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103426">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zgisa4H-pIXJIjqElk7pIcqdLwO8bWJiS-RWEEVRF98n8I-8i29dTHDc8W0GwKNzZXHO6qCKXE4zxvK4PcBbxDJsMF1Ev3TVJ7y8Z14NZ_tqaHGJNTthROU-XlEPfmNpT89540abKJQ5LKuxIeCgT9ZBD3tGI_Vz4eY2H5JwanhWJUkUDdY9WicRPgKLqBJqtgRCI0n0nAIpBU256mIi_Wq7w1PRrJO9ZrkWJ_28JILP1Dim7mRVDFeQcXnkSk4tCK_Nnz5SMqjFgvT2j2QCAqvfsF_TDZ2GS4okjmwunvD6qgxX7YBCeC5DCm5oFPWCyJHZmMxvDhuAQQIf87lJ2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌     ‌ ‌ ‌ ‌ ‌    ‌‌ ‌‌‌  ‌
💯
‌
فینال سوپر کاپ اروپا
💯
🆕
دیدار فوق حسااااااس
پاری‌سن ژرمن
و
استون ویلا
رو با آپشن های تخصصی در
MelBet
پیشبینی کنید!
💯
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
📱
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه ای، مطمئن و در کلاس جهانی پیشبینی کنید!
برای ورود به سایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/Futball180TV/103426" target="_blank">📅 11:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103425">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/870f9db185.mp4?token=pASKbcx1dQE0VjT1_kzbSiTkxVoMsgmf7ZlrCmrHl8z8JP_HtHsJSkU28Kh0_YL-n2U7VyP94djIjw5B53VYE11Nh71A1T_jEdnE7yeyilpeldgpVhr51UCiUAlJUY2lXuVzG2sWI-wb-kTwJXh_WbeqZhRtFHeNMUDwAAqhV4GsWDyQyl-XPxMbg64VxIkrDY_e812gitJsrj6VJZDCp7I3xfzo_KiO_sMiYKLhk1zY8SXCQOTqLrMBD4iHKGEdG9uf0VDStr8I7ER-uwDKwYqi5WCnzxTfONxA1KAd3O_SRpirQ6HMxetl2bC8NHrcj00vn0S4SVI6N7A43wwFU4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/870f9db185.mp4?token=pASKbcx1dQE0VjT1_kzbSiTkxVoMsgmf7ZlrCmrHl8z8JP_HtHsJSkU28Kh0_YL-n2U7VyP94djIjw5B53VYE11Nh71A1T_jEdnE7yeyilpeldgpVhr51UCiUAlJUY2lXuVzG2sWI-wb-kTwJXh_WbeqZhRtFHeNMUDwAAqhV4GsWDyQyl-XPxMbg64VxIkrDY_e812gitJsrj6VJZDCp7I3xfzo_KiO_sMiYKLhk1zY8SXCQOTqLrMBD4iHKGEdG9uf0VDStr8I7ER-uwDKwYqi5WCnzxTfONxA1KAd3O_SRpirQ6HMxetl2bC8NHrcj00vn0S4SVI6N7A43wwFU4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
😃
لو رفته از مراسم ازدواج رونالدو و جورجینا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/103425" target="_blank">📅 11:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103424">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6KuGbX2dg58CD8Ipk9p-54vV86QNv7cTg9mNNU4Fol9ctu9WQ9QiQF7lJi_my-aY9Pz_qIxXv4btlbYy7VFziGr-wiRarD-oXgAeK5kqH1BbGrH8-mLQoFV9SI1Vf5w6_wfTdQ_JIhnL-g7SbYOahIt0CbvYTh5RuqvQ6jIj1y2kL0F8SrfHIaGVIiTFFmAapdrS_1U_OKh6dicrEPKZy6_G7bRNquUi6bVkdem4YzbtrZFjR7ZWZcKc7bA3dxyJpes_MTO2L_E9Dsq3z-hsS_96HRWpXKcVLKtWHX-auP0KJn3kpLNPwWeudWqBu5WNVOxr82l7SRbENr6q01DmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
مقایسه افتخارات یامال و امباپه در ۱۹ سالگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/103424" target="_blank">📅 10:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103423">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c644437b15.mp4?token=rvCOMk0ApYNDxSrSDgeep4sWmHzILYlFKz0wDPvmML5TqFhEyVWqGVU2tacNwOupPoXc31fhp94y4EbFeYNIYHPZ0R9El-JEXA2gXVLKt8IhwStaSJ1760PbCgSUBf6xLrqCwjtPCdebl3W1Tjm_LsPu4kqutGS3cXyZ3Fk_drYGHrnQFqEtnTz7wrg03dJzIgApBtf0fRWmTkJtIC-vGbK7hN0jiNs9YnlwVJgDvk985jSgTVBZ-n1-TGSZiAHZVRyZTbMaJ4hTGkcRR4J4htEp-Hy8sBImt2c-YjfTrS1uE2GaLpg4T0GMd6XzOGRuKB7zXrvHuG7XEzuERZ2HmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c644437b15.mp4?token=rvCOMk0ApYNDxSrSDgeep4sWmHzILYlFKz0wDPvmML5TqFhEyVWqGVU2tacNwOupPoXc31fhp94y4EbFeYNIYHPZ0R9El-JEXA2gXVLKt8IhwStaSJ1760PbCgSUBf6xLrqCwjtPCdebl3W1Tjm_LsPu4kqutGS3cXyZ3Fk_drYGHrnQFqEtnTz7wrg03dJzIgApBtf0fRWmTkJtIC-vGbK7hN0jiNs9YnlwVJgDvk985jSgTVBZ-n1-TGSZiAHZVRyZTbMaJ4hTGkcRR4J4htEp-Hy8sBImt2c-YjfTrS1uE2GaLpg4T0GMd6XzOGRuKB7zXrvHuG7XEzuERZ2HmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
🇪🇸
اولین‌حضور پدری در تمرینات بارسلونا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/103423" target="_blank">📅 10:21 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103422">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gom1mcBYpapmKn8AeYYiRyEhrCgNZBETsiU26PY_yIrRzTAv-APx007-Gbq9v5GjG_FQOdbvBQUKzsX7I_HjRnx9ShWQEvuX_tfeoMM48UODFDLiZJU2janVUjGTPf5d0PauyPp3DOUJpNAuLs6uVoBdSbXKQpVs_bGngsUyurVrCahEb7Cy8RPWz7d5hUvXPUVJttR2CZb8nBnIsMgPJSERyZHCUW8C9E6C8cZHBd0rCXb1N4it6zZHCMuK7CqYs2WN9emTYH88e1Zq-YTlNPYdZOeaVVyXPNPW0_gm0iesDAmL4Ir14nlqMo_RcHzd7sZee-MkzAGaBs9tVvk2MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
❌
جرارد رومرو: هانسی فلیک علاقه ای به اوسیمن ، ولاهوییچ یا لائوتارو نداره و فقط خولیان الوارز رو میخواد
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/103422" target="_blank">📅 10:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103421">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDmTF2Ylssby6oGHC1tvu0fu2tvnnZAKlUSOT34jM7z14ifUcMleCC2hw9E0_4iC0KPDIoTX-LBGkKWr3Vkgo0aDY8JliyfQAC62A8rWBlzdNOfAnXb3paCr0xszHtPlnvbuUZgChJ0mUwT18kQPH5WFtHvdwQdM5rWTU2ujTNqJQ8m--5Ij6E5g-YW1TcNqB36jCxWelvF31dSx0mRe5MMj4lvwIjNz8F3ppR7D52B7mnFg27OvJQ2VTrXvZ--U2IP1CSqIQGkVI7cgxWhOZIhvqsCAxeo-C1TaTzR5DzUeV2FyEYjXkHvV1Y3bXPz0gngGL2r_14EkxmWA_3RL2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
✅
تمامی قهرمانان سوپرجام اروپا به بهانه بازی امشب تیم‌های پاری‌سن‌ژرمن و استون‌ویلا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/103421" target="_blank">📅 09:49 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103420">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cY0GsCXFv4j--HUJJ962-TNtLO7ETJR2cbqfa3VNyUz5lVV0S2YJEadEpVtJP5SgyoEDq5_NZYHFjykIznHqWlGCKwCqs6kTHFkaGE0FpMn_mwaXEIxinufAsXHPLWZcG9KyrOmiLbEGxzi_nrLlFJj-q3AHKvb6Mus20GRf0eUBFjHxQpGaT9TEyNaLF-S42Rqjhbb0dL2KBwKZUjaLpL77t10OQGan6Axu9ozIKYNAHUKeN8aaCEFHlUcHUJXg95ephvcCQjUHx0EqqpLRa4yBZRhB2cv9z8zQNJytlRo4lbsZCIt8AMWtH9Hx4BPZbRskaAt-GWLkbpAnJTTNNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
اولین باری که رونالدو و جورجینا این دو مرغ عشق باهم دیده شدن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/103420" target="_blank">📅 09:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103419">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea09ff2dc9.mp4?token=H1WSLL0zFPpeZOmFPIS48SQZjo_8C6ADPQvsq7W8RENy5mgyr1H3kz_pcvSZGdkgHi1C-jzUqqeNLIZ5UBMDg04-E9n453DytZBhHE7mFu8Au-FAaA3kpC5IHfkRZlYz-516VbpA2wjxXwLST157x1L7H2vP2lr97LKZ57Cm1X7e9h3zMpE11veH8Pkm3xir_7lYG7W3nPLvz0Et6I1etEOFpWEXgKQ0Xq0tYMsVKEtDuFQRcqQOnzz2Xz4aqWZmDHxByvZRgr77nK6nZmAxMwH98Hh3xctL7eMbU4GtENLHIB-qKOftA1knheU8dVmnyOFdug8udvyxo5XHf2PGEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea09ff2dc9.mp4?token=H1WSLL0zFPpeZOmFPIS48SQZjo_8C6ADPQvsq7W8RENy5mgyr1H3kz_pcvSZGdkgHi1C-jzUqqeNLIZ5UBMDg04-E9n453DytZBhHE7mFu8Au-FAaA3kpC5IHfkRZlYz-516VbpA2wjxXwLST157x1L7H2vP2lr97LKZ57Cm1X7e9h3zMpE11veH8Pkm3xir_7lYG7W3nPLvz0Et6I1etEOFpWEXgKQ0Xq0tYMsVKEtDuFQRcqQOnzz2Xz4aqWZmDHxByvZRgr77nK6nZmAxMwH98Hh3xctL7eMbU4GtENLHIB-qKOftA1knheU8dVmnyOFdug8udvyxo5XHf2PGEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاوووو عاوووو رامین‌رضاییان چه کوفتیه دیگه قرمساق
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/103419" target="_blank">📅 09:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103418">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5-2hAILJg7Ba1oELsnsVap6cPzQU_pcSEWUI2-F8puBLuToNcFitbDL4VyFGbNqyEUaS7dw1Wj-T1Y8wptLVAz9GJAuXN-NfWTdPUUN6d-T3Z6UzU_PB9GPZR8JAeycExvLww-NBZ0TXDmOxBUrNmxFM9DIG057XZLnc7xsz-lL4Xcu9QZmyKEsXlJGo5MgYTuLx_W_sEjY-OiSRznQw2E8BJ4Ax63CGjkXH6pxrimFALyTaB-QpsnjyZ3WOF2JBNE4wTP7koa-dyfdQo_loC_Y6s4pdiH7SPU-E0K0ICwqrj9aLcvgCcOrcOY4ZBBizOY8h2HfTOsmMNysoCOuAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇹🇷
رومانو: دوشان ولاهوویچ به بشیکتاش
HERE WE GO
✅
✅
✅
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/103418" target="_blank">📅 09:07 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103417">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fcd964c7b.mp4?token=akoQ48m3AjDixnrhyxPAkHFzfjG-H_p8k14wCtqCf36Es1CiOKnFDE4zyjHT8nfJk5b6xvByLwY6tXKvPE_-7rQHdd1Rocnq9K412lrDNpIElwBSvqwRypG4xPAgsTIx-vsS7d10QozTV_fM05heCzUdETXnGlC0_2-9fS-FWPWYdP460t4UPHxwHTPgB2wYOR_vGb58bzVyzhoItJxgMzChTaUrcANNvqnJ0iKYb8_WWpr89i3JNl1KDGsP5FKqmlDVEEYlvYUQ9B57ABg5G3xWA5mphzts6wPsG67-lrADUc92KsFx3dBKluyk9gxXBhyyug5foCT6VH5ZUleDOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fcd964c7b.mp4?token=akoQ48m3AjDixnrhyxPAkHFzfjG-H_p8k14wCtqCf36Es1CiOKnFDE4zyjHT8nfJk5b6xvByLwY6tXKvPE_-7rQHdd1Rocnq9K412lrDNpIElwBSvqwRypG4xPAgsTIx-vsS7d10QozTV_fM05heCzUdETXnGlC0_2-9fS-FWPWYdP460t4UPHxwHTPgB2wYOR_vGb58bzVyzhoItJxgMzChTaUrcANNvqnJ0iKYb8_WWpr89i3JNl1KDGsP5FKqmlDVEEYlvYUQ9B57ABg5G3xWA5mphzts6wPsG67-lrADUc92KsFx3dBKluyk9gxXBhyyug5foCT6VH5ZUleDOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عشق و احترام لیونل‌مسی و پدر فقیدش
🖤
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/103417" target="_blank">📅 08:35 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103416">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22164b16b5.mp4?token=ANVK5zThBsj_LcJDUA35emlTB4Kpu60mb7r_k9pz-NwadKCaeRuWbrk7uF3lu_QbiGn-PxWqmbD4ZqeSkwRz2QuKUBPc-G598c017GATgqbyy0dmzyqe1Hxu2t3gxkSsGxDMBXIjgiVHStJsufMUiG304rhJwvynLwAhKQ8hHdYXdVISbXFt493q9JqR2Why8P3fvN-WFnBj01NRPGsZLNI1aK4I1ksPnUnD4mPYaVgnuZ8N1YX6P5x5MVFBY_6Bf0pepgf1_SxogIbfvN4s9xbuFl9ptGVd5f37wAzhcHH_VIfmEAcXgIYVVteUcIKAwL04Z95Ey_RC3rmQtSjxDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22164b16b5.mp4?token=ANVK5zThBsj_LcJDUA35emlTB4Kpu60mb7r_k9pz-NwadKCaeRuWbrk7uF3lu_QbiGn-PxWqmbD4ZqeSkwRz2QuKUBPc-G598c017GATgqbyy0dmzyqe1Hxu2t3gxkSsGxDMBXIjgiVHStJsufMUiG304rhJwvynLwAhKQ8hHdYXdVISbXFt493q9JqR2Why8P3fvN-WFnBj01NRPGsZLNI1aK4I1ksPnUnD4mPYaVgnuZ8N1YX6P5x5MVFBY_6Bf0pepgf1_SxogIbfvN4s9xbuFl9ptGVd5f37wAzhcHH_VIfmEAcXgIYVVteUcIKAwL04Z95Ey_RC3rmQtSjxDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
▶️
یه‌ویدیو کاملا کاربردی برای دوستانی که باشگاه میرن و میخوان بدونن هر حرکت برای تقویت کدوم ناحیه از بدنشون هست. حتما ببینید و برای دوستانتون بفرستید
❤️
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/103416" target="_blank">📅 01:34 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103415">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v12FmJUaR2HXGO2LGnvKPG4PV0ZfcUlnfEh4ywWL7mcneJ7g5aFRsjBuKDc-PfD5HEU7duSt-0CkvgrLQfK2buhYPoGzlIf3PN3v6Gz-gD75Br_to8F9ptcW4YBVzQJ6gWnccPdfJ3uethKWIJEe375xxePMT7DBhnBuC4pI_w95ysMKaCEb1lJuUmeWd85HBuerAOr6vHpW0iVXGVv2xo4xpVMDuG2a6gdXo3g0knHzk4Mxo_ep7JGfRm6pDG114U44T2_hH6lL8Gs9eQ90BgXzqR_LILwTxOZ0idf8VQjPCEPkaaetaas3wCbEQzC7zCucxBSFLNx89dK2IGBBqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
رومانو: HERE WE GO فران تورس بزودی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/103415" target="_blank">📅 01:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103414">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/038cd39016.mp4?token=rIvON15YNBCZ2at9CAmM63uiffkAS0dl7kGTSZzzSjbKMiCneLbsu_z_E_zXgeYcNuwshpcKaCuWYCZfdIZptCjQ7n3RExxoLbLf8D64IYzkB8yRvRlO4_XaFDuFfZ96lnj96q1vvtuJtrWGP4UWdbQ-_U8EXns_7CQVA6SHPG_UEwTJCNSv3MSsOzFXfoy7H6q3oWqpP9jHIk-1zCjE7Bzuk86D0ili7ttyjgEMt_gb3f0yz3mbe4p3S1t9JwnvOlR0-LoJFiEBcjOnuPUknY1gPmCwfL-rTYQas-GbWxkkvmuoimSJvsPDEOdEY2RjNRnZGBQILXeQi1EdzN1zyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/038cd39016.mp4?token=rIvON15YNBCZ2at9CAmM63uiffkAS0dl7kGTSZzzSjbKMiCneLbsu_z_E_zXgeYcNuwshpcKaCuWYCZfdIZptCjQ7n3RExxoLbLf8D64IYzkB8yRvRlO4_XaFDuFfZ96lnj96q1vvtuJtrWGP4UWdbQ-_U8EXns_7CQVA6SHPG_UEwTJCNSv3MSsOzFXfoy7H6q3oWqpP9jHIk-1zCjE7Bzuk86D0ili7ttyjgEMt_gb3f0yz3mbe4p3S1t9JwnvOlR0-LoJFiEBcjOnuPUknY1gPmCwfL-rTYQas-GbWxkkvmuoimSJvsPDEOdEY2RjNRnZGBQILXeQi1EdzN1zyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😞
😢
مسی وقتی می‌بینه رونالدو و جورجینا حداقل تا چهلم پدرش صبر نکردن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/103414" target="_blank">📅 01:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103413">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VpXz6zPfOCBzvr4WyHUSG1hzUKs1T5dv3CkyjWJddcO4NCfuNGKWdvQafjyhAjSGW_UvLxcM-wpdVW6jf8ar3KsSg59tbWfZfwq2nLJxc31CvFl9-3b1VUQomBciwchVk-kQprTyIycelQx5GLcywPwyZ-5fiAHYM-lUVvNKbalHaRUkAwypRe5fryqQbcAm8BRIx8Lua3jG06qjGIKhlqp2JGHVKPwqdKNP7txZCMTcCWXFeyMNMfhfMGL9ZoyUSL13p6lYdTf-a5gEW2181pGnMkSKKta2Wp8m5EyBQnpUDqysz-b8anG2VbJ_7sri2PZ14-tcYt-Nwix0jVu--A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
#فوووووری از رومانو: مذاکرات دو تیم استون‌ویلا و اتلتیکومادرید درباره متئو روجری در وضعیت پیشرفته قرار داره و بزودی توافق حاصل میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/103413" target="_blank">📅 00:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103412">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKrI26iejkKh2ZJ8QK-qpRuJep8n6mTYrIM9Ba1lp5_IRcLHK3Ea5DzCLqJviC6NfK0Q5ymo8luzMsngd2fLlTi50oZLMI4v8Tq_iAoobYeUIyM-HkqJVUdKKmESV-NAhlb-vlnBfVh5AwzG3kpJCYky1jDmNutzMXo_pBFZRWdwTPF3XNpqOt6QKtT3pH7l15Ex93G9e0LhCP0nieyJa8_jOxH38CqdzrygVaDaB8voOQnuemwJuAYWCzj7xrHbBjTgR6qPhJveoCSjadR1oduw0W9PrrtkD1L1N-gsS1GwGqtiK8YOKtlcitCFHD9_bX2Z4AAiaRjMUefe63kq7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوووووری
از جرارد رومرو:
🤯
🤯
🔥
🔥
🔥
دکو مدیر ورزشی بارسا با وکیل لائوتارو مارتینز ملاقات کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/103412" target="_blank">📅 00:44 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103411">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLuEJx8Qp37o39CquVsNqDLpdvA10u4KyBcnt0tvUVQCn6y1CJa8F7hDCcVtZLRmtD5z8s4yLNzGJzI7MejfuwqVMPFTjWygSMtRIL5KeimgMCHJxTn0oZHR656uCy9dZpfJuT4B3tr2uPlYKEqJmwOW1CD-kX5gDrzyrOQHarcFSKL1DwV_D3wLZyyueLEd4kfS6ubZxD5vqS03U6saCFgOCEAKKHjjU6M7XsYRSQ7Vi1K6aI99-KudsSs0CcUJ_W-Ex1qkjKKUOlJJYQppb5i6dP7TG5-KbAWzVtVyp4YI9RgFH28y028f5-ozLKpna7VT93PiedDWKgjuvBG4Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇫🇷
#فوووووری
از اسپورت :
🔻
بارسا و‌پاریس برای فران‌تورس به توافق نهایی رسیدن. ۵۰ میلیون ثابت + ۵ میلیون یورو متغیرات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/103411" target="_blank">📅 00:42 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103410">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObaWZ-ibng1FXVcZjOC5pmcMIW8Glh2pKummKVTiqhRDJnw0js40IDLe8qyYnIn19SLdyObl779PWgoQ3HfyL6-Qp9k4EkmVydP_3TjaFDi3cSH2OLt8x-tb-JP5N3fB2hXWw4XXsbOhSPyInON_ydkTuX4W2cd8a_aGItIL8-Dqkbs5fuYesKi72K3BmS2QgPyabBUdUE5UEXOFDqIJEUMaGXI9pkNB0mlLlRJB-PSE_mjiXCLZ90GrYviBm7Kinlqv0jOx8IUY3_cwseyHSInKEwmf7YHkmPW6z3An-GATUKUBx5hFif9ZZKod-nPcd6liQ8YWe96NPdewmwUSLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
🇺🇸
#فوووووری
از نشریه The Athletic:
🔻
دونالد ترامپ بزودی شخصا با روسای جمهور کشورهای مختلف تماس خواهد گرفت تا صندلی ریاست فیفا را برای جیانی اینفانتینو تضمین کند. ترامپ بدلیل روابط صمیمی با رئیس فیفا به وی قول داده که تا زمان حضورش به عنوان ریاست جمهوری آمریکا هرگز اینفانتینو از فیفا برکنار نمی‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/103410" target="_blank">📅 00:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103409">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c334f75417.mp4?token=LnEFhI03PrtbaHUsiwqMoZRpxNrfvnkkuf6b_4NW2SGHm2jbIe80B-qG7mQ4HpllY5C_1KLQHVWuDXYGnR2ocRb8jkTQEqZbbjzNfV5duTRNRpWOwrNV9cLNPYzhpuqooE3YDRU7B1c0zYnGNb4lYd77eZT3wYi6SUKVYgpbCNNJUBOT6b2OLFrd6B2Wb-uW6V3Fsptj_BUxEnRChIm6GTp71_RsCVZpRYj7WS51tZRBzYlAn-fD3NFQthln-5NCT5OT-MrjkXZMv5_sU0zQG9BpF74AOCO8ADpKh8Fb6YSPMNt2abbLEySPJuAlWV02x3iRLxqkS0ZBOBlZd5obAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c334f75417.mp4?token=LnEFhI03PrtbaHUsiwqMoZRpxNrfvnkkuf6b_4NW2SGHm2jbIe80B-qG7mQ4HpllY5C_1KLQHVWuDXYGnR2ocRb8jkTQEqZbbjzNfV5duTRNRpWOwrNV9cLNPYzhpuqooE3YDRU7B1c0zYnGNb4lYd77eZT3wYi6SUKVYgpbCNNJUBOT6b2OLFrd6B2Wb-uW6V3Fsptj_BUxEnRChIm6GTp71_RsCVZpRYj7WS51tZRBzYlAn-fD3NFQthln-5NCT5OT-MrjkXZMv5_sU0zQG9BpF74AOCO8ADpKh8Fb6YSPMNt2abbLEySPJuAlWV02x3iRLxqkS0ZBOBlZd5obAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
✔️
ده روز تا آغاز لیگ برتر انگلستان باقی مانده است. پائولو دی‌کانیو، شماره ۱۰ وست‌هم و ستاره‌ای مشهور به خشونت، در سال ۲۰۰۱ جایزه بازی جوانمردانه فیفا را دریافت کرد؛ زیرا در بازی مقابل اورتون، به جای گلزنی از موقعیت حریف، دروازه‌بان آسیب‌دیده را کمک کرد. او ثابت کرد انسان‌ها سیاه و سفید نیستند.
همان‌طور که تالستوی در رستاخیز نوشت:
انسان‌ها مانند رودخانه‌ای هستند که آب درون همهٔ آن‌ها یکی است. هر رودخانه در جایی باریک و تنگ، در جایی تند و خروشان، در جایی گل‌آلود و در جایی زلال است. به همین سان، هر انسانی همهٔ قابلیت‌های انسانی را در خود دارد.
👍
دی‌کانیو با این کار نوع‌دوستی ثبت کرد، هرچند رفتارهای بعدی‌اش بسیاری را ناامید ساخت. اما هیچ وجودی بدون تضاد ممکن نیست. نفرت یک انتخاب است، اما باید فراموش نکنیم که جهان سراسر خاکستری است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/103409" target="_blank">📅 00:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103408">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/103408" target="_blank">📅 00:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103407">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=Hw09oktxPqdYK-WnLIR_VaG6pUxDPH7pe6b7A3Vm07NRzwP3_-ROUAp_3I_YeSM2SAC9QS2eLJLnUvATX0JcrtnZ-P4wiEzPT0lFizCkD7Vq-uS3MumiddvD6i7aQwD92PcVgtOYYNRnmow3YsajE3zc3vbh1DQ1hs9A7-BBH8RXhf5sGmOM3-5wysjyjeDMfe-SQKWl107r2q7eepj2MRyCJ7PxnyjReDF6kcoj4R_0NoaYfe31NhW3UJs-IEgsoYOPeT_IdWLWP9JMBi_RVwfhJO3vmmvCUD9E4wt1xOJfsig6ooyeQOCRLqyKypEQTAWLUoQkgJ7EXur3AK8_AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=Hw09oktxPqdYK-WnLIR_VaG6pUxDPH7pe6b7A3Vm07NRzwP3_-ROUAp_3I_YeSM2SAC9QS2eLJLnUvATX0JcrtnZ-P4wiEzPT0lFizCkD7Vq-uS3MumiddvD6i7aQwD92PcVgtOYYNRnmow3YsajE3zc3vbh1DQ1hs9A7-BBH8RXhf5sGmOM3-5wysjyjeDMfe-SQKWl107r2q7eepj2MRyCJ7PxnyjReDF6kcoj4R_0NoaYfe31NhW3UJs-IEgsoYOPeT_IdWLWP9JMBi_RVwfhJO3vmmvCUD9E4wt1xOJfsig6ooyeQOCRLqyKypEQTAWLUoQkgJ7EXur3AK8_AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
➕
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
a20
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/103407" target="_blank">📅 00:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103406">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swUFrPWEox8Bai0gsxNeNMjqZbYT-PDsz46tZnFjx1GWMPJo1voBk01rH4i-BOPPZIZEtlT4Y9pEiQJxNeow87MgNpASaNaz1YgQvneQlWvbzXKlt7hzl0TGDul4ridmnlbakjyuFjLRnCKkjGRk_jsSHyte4ScYlNjD-BYhFEfTZoB2npoBGlWCnfXFL5yvQGYfh4P6muGOFdgY2V0n6NrRfMkQac04oXd3odCncwIjCFWCheICg1jLmEWKewxmCzopcBuhiVOXGDLzWFY8UnHk82nmuJrn0EOo9PiGpcFC6YxycV618WNE1E3n9sA3kIbELMc5CTbgse20R3wUWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇷
کسری‌طاهری بازیکن نساجی با عقد قراردادی به تیم‌فوتبال سپاهان اصفهان پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/103406" target="_blank">📅 00:01 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103405">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkfCBra3R6l4GPKGYHh9X4MB5jzk8YscQnOnc2pvv8hPR0P32ygdqKbRZqggO_AN4LYt4Xt0jIiom8fA2y7XQwsh0hPWVOWyQEqmxXGZBGP5hIGb989zgrs5KJ3FIU-8gY1kuqtRrNI54XQPxLiioeU8LPM6fW1BhTO7R5JlzwxPrZL_mPvKG4GWyTTcT4IiC06_1VuulL-Sr_oL4lFFtoMN1bd6mF7YxhUtmMpDmFz_okcH4-dn4naASZW3E6S5iDGaNxn-eVzeyxfaQUjFGK9iRWKGEDxwlouaQmtJUV5XdccBSAKJRLaJLq05zGbHJQbUWsw7k280g2Zgq5fUJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
ستارگانی که ‌تو لیگ آمریکا و عربستان بازی میکنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/103405" target="_blank">📅 23:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103404">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AnQqt0q6Odg7peH-GC9AV6Wju3O_iwFinQkxw1IT5f_uvCUqKNkQafMne_Lo7cWpfFHp4HCk9MiiTynyQwAeOq_vwIVAH3eMRawQSU_gC2L0MuS0Ab5GAcB6yN_O6CvD4TrmA2vC78HQM0eNuOZ-EbHR0Bp_SloCTACWPy-hXZJ9ozsBVBpDY3_4pDKnQSmWOHCpLdW4gd3fcwYuWmdFkElJ5NIqQC7P7dYw7cwz3K2O4ACoabor6fpsNTWzMGnRKCsWJCUwcAkUWPIpXXKcQ_e9g0RrwCSWt9Lag0mGyiE7z3ISic_m55DL6-Sg9Jdp2ZZXZpthKa1y0euLny6Tkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
باشگاه کورنتیانس برزیل اعلام کرد که بخاطر مشکلات مالی توان تمدید قرارداد با دیپای‌ ستاره هلندی خودش رو نداره و این بازیکن پس از دو فصل از این تیم بالاجبار جدا میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/103404" target="_blank">📅 23:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103403">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmTQXJhuWc9HYT5t5222jzqcEHm9i3cwa4Xt5LQV_4QbumKhN8D_W6RJ5dld2WuVN8t1Qr-cV1XMXPlNz3AotblWMyHOqk-6jNxmEwwA-Lpo4Wh_71JA6asKQVz97uT-YwWxek-a_4TD2-__v1Q0hYEDiUUJAY4cgx6O1dAgrkhyufAJk-bcKl98gyksHFK1LxXHD_IpSaWoi14Yg-cRo350xOEmN9dnthrz4mTXrdjBDpJGlXRQMrDSqJnotgZI_NrYB3DZh0WdYyvR_ngaXA7sz57Sti_95MP1UD9-HBdVa6cyJ15ftkMzL2dlrs5-WZU3aMBEZfv8eX5rWoPFyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🐐
🎙
مورینیو (در مستند جدیدش) درباره اسطوره لیونل مسی:
او یک کابوس همیشگی برایم بود.
☠️
☠️
☠️
ما چه کاری می‌توانستیم انجام دهیم تا جلوی او را بگیریم؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/103403" target="_blank">📅 23:52 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103402">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUo-T6O_HQfhtJUiUGeJh3ZDSIDt6_r51Pya6TZIYqI6fN-CL3ekyHBhyuxx-qXYIY3NboTcvi9rmhKVFyR0Inc8g8mN0GL6lI_YAnXRoXj8QewNZDB3Hwq6QZmVSB8WaYn2NktFcHYUOE6MznwdEeP24TSo-NotjdQjRZ_RUbP-BtcNZJpbUZnjbEn_2MqKzO6nenPsf7dXXEUaOU5SlVanYaPBp-B-up-PXUjmjN1Q-7R_hCLCjKfyNqFK7BXSuCtRlWk9MecwoThGZNe-Yijrq3oHeWOTrtlRZin3aBVO2rtv-RSLf6azqkV4NKr3jj-BDyB16UwKDmXZgxzU-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رونالدو و جورجینا رسما زن و شوهر شدن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/103402" target="_blank">📅 23:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103401">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPEzZIBVmUeWyriRlq3py7ftEG-MVUqh-6T-kmHQTPkzoM4reN1XIcclChIHiq679VmOVpp37N0hK3nMafRWl4Wtm4NLjJxJi8iFDNJVk5IELIrxzx9NeWU7_mnaOeLXG9tGKyt6fqD0WJT7TYavimQmfqc6PHKLye10gjRZ6t1FKd7-Wfpy_ZjBeLdCGP1xmWlKhDrhg8he9Sfv6o08TznC1avhmSsSA-H5ArDc0tp28qsvWBEoYRD0seGKU8DSx_uaSKcrFcJ0vh3tnle0OBMlIb1i6QoowomUeXiPTAOG1l93RFVF0CNDyeIRf-NbxDU5RiwUeMNzkNBVxp_CdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از رومانو: چلسی برای فروش انزو فرناندز به سیتیزن‌ها رقم ۱۲۰ میلیون پوند میخواد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/103401" target="_blank">📅 21:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103400">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M93KxMN6wktTspCLvoJqivnl_F2kE1Xo2JnxLhs46fdLPtzJcEsJUm4Dp3KRm_nSJ7gJMmTmQEQhQ1dqdbULur67c-F0b65aIKuSWmThNdqOIHVoaIcxNuwvlUmW7g7qaH-dImLY3IYlQxAsUV2WsYCfzmkvIiOMUdjXQFaLE0ti0YMSqjT8ooeRA-KFeR-Q0D8PspWewHnEoH4LdDAsuFN9iHKBuEa7L_cZvVNqDlnBcZQPbY4-jpc-izbsqo8D0-1HNLJ0-VlUzFSgjOJyenG5yOuZ6Uz_oaHLjBJdjDTMi1hYsnqcKgajorrtWsvgi4RK_MAx7BkbCFOsVl8MKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
لیست ۱۶ تیم نهایی لیگ‌نخبگان آسیا؛ استقلال در سید اول و تراکتور در سید سوم قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/103400" target="_blank">📅 21:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103399">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/km_KLNVY6uWoCZW77W8-YLgjPdJq92HCD0fBhcthc95mR_p25ICoB2IzQ_5MNxJQCM_vavaIxqzaiGanBqUhaJvEu6G-IVagQCUOcawzhsHduxdF_NIh9h_YiXUCzpcB-nsaPdpoaXxLHegY7sJde5sAoe0LkLzNiZbmhqjSxsgPiusFMvXgJstEePoDrd5r28E1masnJMjC0Et4MBr8QnJLOSs948Y_rMsY6yb3PeH7NROyjwKFqB5HlhSGM-zw9Nmx-g0t1NcRMJDX1SRIJ0m_pqVH4mD9ZBlmwVXGd9Er0lMH7uzRXzGwAXQsDsEV4tpq8BOHsfZIGOl_h_jZKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇫🇷
#فوووووری
از روزنامه اکیپ
:
🔻
باشگاه موناکو بدلیل مصدومیت پل پوگبا قصد دارد قرارداد خود با این بازیکن را فسخ کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/103399" target="_blank">📅 21:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103398">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SefApAw1HNtXjZS8ztme6soyIxLN588AI2NqhV3qyVUb-3drM5PvFdO8UxXTdUKIHXFfGrTLblyROje_jJ2Z7po7P3yS95vp6eTXFJ8C4Nk40mDyH_dGy_uENaORPNGo9dSeluynYOn_W02mk4J0nY8NeAX0MR4oXqObou4Dc_C6VUF1VDwCZZKsjYfSmAY7j0_Z3GcwU5KIcmL7yuM9P1aYsIr_DA7gd6YW0f20vUP4UpQVDCDFHdwWFh30T8HkV7I9GHs4A-a5VObyXO0xnx-oemzLmW5DQfNA7O5Qq_qxCsmRgKcoehHo9DPp7MHo5AyNgsV7Oe9gefiZ-X-msw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ویتینیا:
توپ طلا باید به یکی از بازیکنان پاریس برسه و انتخاب من کوارتسخلیاست،‌اما نباید بازیکنانی مثل امباپه و هری کین رو ندید بگیریم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/103398" target="_blank">📅 20:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103397">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2lsTyDIzdtDUjwwXj_ez9agZxfxDGWcxqjwGZF6tICvjggAGCVvrQwWm9IIqVg1uXfYyx_E1gfVsMIuY4mpMomLCB8IHMZHdGjcjD8qtVn_HpTNwc306WYOhQqgoIc3O6mRHTii4mCo4sdMbEIxVmt-8tUH6uBC1cYvXOhrW2FZzKg1oI8qg5WGVp98UUV38oJSgvFnohZdXPJABPH6ZSBC-pNF4V9BE-TrA2kgLivOHBo794TTeO9Fy444__Z9J3X_RPmLsBC0JDqr0YdcDSvb7XlWXYWEYNGwwSV95i_RF6jCDBqF6-89c62-dJS_WQ6eLH0i916AoWgAmLzTeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔵
#فوووووری؛
🔺
هلدینگ‌خلیج‌فارس اعلام کرد که سهام باشگاه استقلال بزودی به چند شرکت یا شخص متمول هوادار آبی‌ها به فروش خواهد رسید. مذاکرات در این زمینه آغاز شده و بزودی نتیجه نهایی به مردم اطلاع‌رسانی می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/103397" target="_blank">📅 20:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103396">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ig2Uh1K_Vo1f1dcGgdh3FnnWQ26CVZx-JRYByfTlE4SrNEWOdIL431hqDZv1dFyQ0kFroRUD6Ua7hGr2-PmuBSycaXg0qmMYJeHZyDBqGzuDFAuuwwQt3jwzJaiklyvU3r9rYhHHft_wgkUJNYKy2sARnHfrCpB8sInCDB9QgCcSQa1Wv7i0MSE_pfe7mbYjN37r_N9Zp1PU27-1UtOvvvzHsLScOxE-eGTmOHJKTNeENyAL5BAIWZcrERYlLkZP1yvbyzkpISaZh9jSl-hlSR1-VEDPVpKGI6MW_m5Q1cL5FFkbznrUaKE_wxoUk3hJDKyuusgTlnZ-c5TE3HTuJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
⚽️
باشگاه پاختاکور ازبکستان با برتری مقابل الحسین اردن راهی مرحله گروهی لیگ‌نخبگان آسیا شد. مرتضی پورعلی‌گنجی در این مسابقه برای پاختاکور حضور نداشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/103396" target="_blank">📅 20:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103395">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZs4szVYRaCWAcBMblBTjS0CrAElk1wM7lpr-Sfs5VH0I8mGqtpzzrY-hwGWDItpS1irIFRKZSzabTjKUrMIIUyRZF_Vn-Go19gcTL-HCYx_d-NCfMmwhwTqS_lb9HFYtjFhX0sXW8eRw13J41TSYi93bx2WvpD2I_5qu6h_1Q4RjbyE0FmDB5BmcRJsPYj6R2HFj6gDeF4U8ABxaCF-fVD8uGvcvRywTgmu3TWPvxtGlnkmt566TlfpSvagBx04Ttz6J6LsH_zPPW9zKvDB4XyxwGgKHBAJO_ZDRNuej82uHPoscBTPzFmoT2I9zAiWL9UBcWOw75kCXLAE8OuSjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صحبتای جالب مورینیو دربارهٔ کاسیاس در مستند جدیدش که از نتفلیکس پخش شده:
"اولین سه باری که با ایکر، کاپیتان تیم، صحبت کردم، اولین چیزی که بهم گفت این بود: «اومدم درخواست کنم به بازیکن‌های تیم ملی تعطیلات بیشتری بدید.»"
"دومین بار که باهام صحبت کرد ازم خواست تمرینات رو یک ساعت عقب بندازم، چون ساعتی که من می‌خواستم تمرین کنیم، توی مادرید ترافیک زیادی بود."
"سومین باری که با هم صحبت کردیم، بهم گفت: «ما نمی‌خوایم به هتل بریم. ترجیح می‌دیم روز بازی همدیگه رو ببینیم و مستقیم بریم ورزشگاه و بازی کنیم.»"
"خیلی زود متوجه شدم که حسابی لوس و نازپرورده شده بودن."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/103395" target="_blank">📅 20:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103394">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJHL3h8gi31MSKU1n5iiy2RAJxxqHEe6pKa2NSKojzou-4Y0BkWRLsd-pPTxAG9_b7JYfh6E_SsomoflK79lCPP5i09iLJIvbOuoQkYgX08ABv7z2YDCcpA6sJoDsNIjPWoCFYSvEuUa7gj9IaNNE-Ew9RoJWhZf2qCqMlzdGOZ8Q9uXKgN8djIYncRDgVUOP70JVbp6OQF-_H7l0nXo336Hf5BiD-iCsliSnKI9p_D4h9k0raalAcXiYTu090N59ipjT7_V3WNxcWjECWFQTTVepUmVqqOPGnJhBMBibUK53RzqzPpsxJI5i9sPMPA_KJezDTkD5cDVwo5GLwHV4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار خط حمله اصلی رئال مادرید در فصل گذشته:
🔺
وینیسیوس جونیور: ۵۳ بازی، ۲۲ گل و ۱۴ پاس گل.
🔺
کیلیان امباپه: ۴۴ بازی، ۴۲ گل و ۷ پاس گل.
🔺
یان دیومانده: ۳۶ بازی، ۱۳ گل و ۱۰ پاس گل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/103394" target="_blank">📅 20:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103392">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uVOEYuqIbvaWw_q_ELaplngESP7Bafd0_v2727dxnS8xkPv_C2Ahl51gV1IPsehyFzThwKDp4NEp6VADl79uRPC4BdC8LLAdeI-K2woY4Ni8p0mQp6qQQ2uFPPiQeFLozHoYKxOmNWDK_xdTbxtIIh4CkpSE_SsHBODs-yOYU-kExgkZupchG85dv2dJGSdrgjMnoxhSVHOAucQEyvSAVqmOHvKJChLlEgXrMZncr0LcY8YzF1gcQMZMu6qrAck80wXecp4l7cjG4rT50dHE8LdYzItcHVS1mhlbViVMYuwGchJe96XpNut4jchWyYIjStUmcWsBRGSpGKFA37m2aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MsVxKX899x_rZwX3jbVTf6YfSO9KciOvjE8wM9qxaodkocPZSHHG-bYfpxhsMzhusV6GJNjoUcDG0MqkdC5O5kUua8QojEsu_JvvC1wQWokF6N12eUU19c6GFxI6V5JnudRuAGwT4Nlvp5ejquA5NvfV4SLY5vbkar_4qKzfZBdGyvnQCEsD9j-rbFAAmMfyGfacNP1ao6rM87gQGoUzvMJ3KbOL4t7Y278aPIjuE9oiP8Qb_281jqUFrg7pLFVTzMKjifbmaIy059D7vbOkW5YSKj3iNxlkZ7_Z5LKwCPyGUKedmgoczrEIGNF_3BDEK2bWcFwBhpQ3An7QiBnm4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👟
تبلیغ موزی پدری برای آدیداس
🍌
♥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/103392" target="_blank">📅 19:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103391">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ofaai-wBqHr2pDwVqkCXQ0DLxfDvIYaub-zLbaW_vFW5VYmkc43LCyDFa8j0aK1WaAVp-ssYqeq1AjIBZ83QRk8Hqijjlkn8CVCExaf9symD6-lT4PWKpnilnJwEnEfeDDDMjacxDjW5Sx9yFmsbcU2Pq78haL4g6WjNbggn6Fha2qAkOhBypuDykiwoTNBhbKvRGpr4rOjOmbfvEX1Vw14sBZHBC-UXXH5lGQJHhFTf6ngD1c5teO6KWQeheHpPRITh4XsFpC-ievyv34Oc55PRKBetLKiUwR9V8vwy2QJZwxZfpFgyDRTQylqQTQFIaEDwE2AcoWX9RZ6VX-dJCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دوست دختر جدید گارناچو؛ خارج از زمین فوتبال اوضاع واسه گارناچو خوب پیش میره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/103391" target="_blank">📅 19:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103390">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf2ed3bb71.mp4?token=ahuuCxaKDoeih0oM8Ak_b1AphS1wvuELnQ9IDd61Vx6CO46xwGuoQhp3jRGrHDFt4DaRaXPEpLNYemg2lpeRyGsMz-ybg-mnHyOU1ZAxbg9GTl5a0mlWLgb2kwwzPWYsblL1sqzVMjSOrl6DtErHporn7Xg99-3AWkZlYWNJhqWOSxvVf9myJ9nZ8pYiOuag2IT3o1DBJtgMpREch-QHxLUA14WDlP6-x1jhOBiy74G5HgMzy7g9trMYfKUwT1h5-1ZCXv_BaOWxveiZyuko6QEO-rpeOmCkKa41SdTKCa2oFCiWZ9p5XMrIB9QdeKYsFHhLEnHlnjarBgAN_ihvbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf2ed3bb71.mp4?token=ahuuCxaKDoeih0oM8Ak_b1AphS1wvuELnQ9IDd61Vx6CO46xwGuoQhp3jRGrHDFt4DaRaXPEpLNYemg2lpeRyGsMz-ybg-mnHyOU1ZAxbg9GTl5a0mlWLgb2kwwzPWYsblL1sqzVMjSOrl6DtErHporn7Xg99-3AWkZlYWNJhqWOSxvVf9myJ9nZ8pYiOuag2IT3o1DBJtgMpREch-QHxLUA14WDlP6-x1jhOBiy74G5HgMzy7g9trMYfKUwT1h5-1ZCXv_BaOWxveiZyuko6QEO-rpeOmCkKa41SdTKCa2oFCiWZ9p5XMrIB9QdeKYsFHhLEnHlnjarBgAN_ihvbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
کالوین فیلیپس هافبک دفاعی سیتیزن‌ها با قرارداد قرضی یک ساله به شفیلدیونایتد پیوست
منچسترسیتی در سال 2022 برای جذب فیلیپس 50 میلیون یورو هزینه کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/103390" target="_blank">📅 19:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103389">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzA1ulFZAJPIkLyHoisVMVe1V0OYjF9uQQeB3rGlwr1naFmlm0ST3k1EmHZYT8-x9QJQ0Q3kyJMwtf1r0TAIZQ5-4imJI9lTObnY_Ya6mQwwdskvupyck9mp0NYXEeSxAJSf2xKwrbYtwa4g867fhXWKAKOxdsdSKypZqSwxHrdGiXBLQ6muc6EVQWialPbspJU43UQtkdk8y5Ha79w6zmt4SRsvLQ5hExZtyiktKlQksDEXdi3THogqKzddpDB4hwzxzhTgEkLbRQD1B2D_imgJxRWMi0ilFH-Xm-kN9UHUHOMARILQe-sIvBAI51spJorHeOcXG7U0TmvsmJNjLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇦🇷
خولیان آلوارز بعد از تمرین صبح، مجددا به مقر تمرینی اتلتیکو برگشت اما این بار به همراه ایجنتش!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/103389" target="_blank">📅 19:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103388">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🇦🇷
خولیان آلوارز بعد از تمرین صبح، مجددا به مقر تمرینی اتلتیکو برگشت اما این بار به همراه ایجنتش
!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/103388" target="_blank">📅 19:30 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103386">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sta8bEYN3gNFQtHCF6Xh6ZjAIpBpI-7TIE-iV0u92iLCf1b_jIHzVxYDkEaTSJDSymUMGRjVNNvq5B-5XD7zTktHuvd8GgmVXFFi2WW6kZMW5nIyTxvbYrj6P0vklLEQFWsWosgjSa4ritlDB1mCsLNjbhzYpZ6vUAg6MR_ad1qzX0GyFo6SjuGylNRmWgqV1HnQ9OSISWj1tB7QOHtw6XoVlvV3Bi1Mm6OTkPnBb5DPx_2CWGmbwf2RUBW-e2iSw0dgklrxf-zCaodzcsWhu_4lzmYtUZ9uNsjsB3Jz2MTxku3sb3X6jhwBMXrjHQPbrN3H9Ckm4PIy2UhjG8aZdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W4Usm-5fldzpdv2XncJwKJhadjtJq5l96LB7ROEViazS8JqmsvfufALT42dEjb_jhRIy8x8ArL1weG8eFTZBAeCYwh7zu81bLl7bnLyK5clY2xaEENSLf_zEnxNaUPzROLlktgHTsNP_lDgxxCvy9mD829ZeHBfF1RgQUFjFCQl40-M5rWogtu6ny4tv0_cFjNAuPFGuNm5SV1CJ7FwVNdyI6V0CJ-nGIjKQSsy0bwoqOG7X1WYHiNFj41gH5usjA5kH5GiIlLTfb9Feeig9pq27_HdrU4pnTj72Gloc4XMpC5oa5fatGSCY6dAPHKH5VAckPflBgPZE_YB4oS8a6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
امباپه و استر اکسپوزیتو در ایبیزا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/103386" target="_blank">📅 19:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103385">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RXkUI-xt9pmyCzZrTmbC_gIXZkL3yp8xwWp8YdqGB7Zh734e-XA_Sex-VFx_iOuAvhP768VnE8r850w3bOtAZalltvTp8b2y83aBQu8V6y7_nRyjTkurp3yPUWkYXJSc8LcIcxumgO-P7yqd8WZgIpoayWOAsDJuVJaG83DgiXiayiqENSikrRD7UjpvtTfHbqkRpr86eBBfQVWpshOZAL8yeCGOAFaQA8BeC1SEr6IW4ADPXD2tO7aZCimBW35WywtYaN0l4ay0J1rgdY_cN53d6rYV2fs-aE9rvl0rTO1VdpuLgrudp5IxZ2mdjc-u_7ngC7c8uFHQYXOtvKbZFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
واکنش روزبه سینکی به صحبتای دیشب رضاییان:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/103385" target="_blank">📅 19:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103384">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzlLRkzKld7SC58OrwerNZbcrCIVtQRgN1Nw00hHlyjghWfyhogt6YHwyl4AnyTx8DNk-sMjXCTO8aHpUzVJV97Y922dCRydjFb2ZsusO_QQO5E6v89DKbAZ2EiU3QBUXd1oJ1ahwDXxFHEsvX_Gvt4gtUF5EGBq4hrWBo4Qu1Dgj9fr4fAn8Nl4cYk2IEcm7xvcihEjI0laG8JQno3WaPsjsi6OgogOsV4IXET_Op_8CRiCxNY4LEMAuw0s8xD6O0LuXLRVatry1pD38wS-u18TMSbMbbNDxoQmJLiJynWTTxk7gkDdOfKG3X614yM2XqsklkIGhTgPPCORFjzamA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🎙
ویتینیا درباره جایزه توپ طلا:
🔺
‏
"به نظر من، طبیعی است که یک بازیکن از پاریس، مانند کوارتسخلیا بعد از فصل درخشانی که در لیگ قهرمانان اروپا داشت، یا دمبله بعد از فصل فوق‌العاده‌اش، یا فابیان که همه جام‌ها را برده است، این جایزه را ببرد. به نظر من، رقابت بین این سه بازیکن خواهد بود و من به یک بازیکن از پاریس در توپ طلا رای خواهم داد."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/103384" target="_blank">📅 19:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103383">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63fe3eb369.mp4?token=p8nUyCtrWuDDXvxSNkGuq_S_1QGV5yZYGPCnVvT3wc0qkb0SaIP9T_qkEX4Hh_OJnUZW2covrkzfN7SALo3FXca6-NRiw49ex18dwggQPjA_ZPHkpkJx8L58OV_JYasovgZ_XflalZFNygik21jPj8rfDeNKgoWJuKwyL5PQx9TDF7bw79ALK9z5Pn5PqbaleMOqW4_oVwVRI9z2rlUyz3tGsgKZGv6NRZc5WepPZAWl_LlXXn0P4kdW19chgWrBoFL9AXsaJiIRUWPYUXP6GmL-kktt2LRkPv3f2L2JNfzFEOJvYZezebqex8cgmGd_ekVmOSBsEk_r9XvZ_JvBcJ-ZNlPD2I2YHGin0NUu4cBHMVQpyp35B-CfjLxWK9yRpvTOf9GwFD6xcLlvrIUkr14uvmCYHaY1m70wSLrXFBkgml5BkB7F4iL6EdKkAN0Wiwp-4SuZPEaW0C4NRPKzMdgeL-t0kediLm9U6kluEk8H6D6GrGA8eXGXaLoNg1swdhHM7DR3zBh-3cT0PIE0eqgNdnFBASFQXAx595w4ODXgbXp4S-FmTJCOFizscGijyEPBCtpbkzs-shpi26RykXkgDn8gT2SbsrZJyHBbP3r-puaKHzrX3JN3cA50EGjyk6CPL3mdcLIVEKK2jbifAUoYUa5Z77_PZJ20TnI3IdE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63fe3eb369.mp4?token=p8nUyCtrWuDDXvxSNkGuq_S_1QGV5yZYGPCnVvT3wc0qkb0SaIP9T_qkEX4Hh_OJnUZW2covrkzfN7SALo3FXca6-NRiw49ex18dwggQPjA_ZPHkpkJx8L58OV_JYasovgZ_XflalZFNygik21jPj8rfDeNKgoWJuKwyL5PQx9TDF7bw79ALK9z5Pn5PqbaleMOqW4_oVwVRI9z2rlUyz3tGsgKZGv6NRZc5WepPZAWl_LlXXn0P4kdW19chgWrBoFL9AXsaJiIRUWPYUXP6GmL-kktt2LRkPv3f2L2JNfzFEOJvYZezebqex8cgmGd_ekVmOSBsEk_r9XvZ_JvBcJ-ZNlPD2I2YHGin0NUu4cBHMVQpyp35B-CfjLxWK9yRpvTOf9GwFD6xcLlvrIUkr14uvmCYHaY1m70wSLrXFBkgml5BkB7F4iL6EdKkAN0Wiwp-4SuZPEaW0C4NRPKzMdgeL-t0kediLm9U6kluEk8H6D6GrGA8eXGXaLoNg1swdhHM7DR3zBh-3cT0PIE0eqgNdnFBASFQXAx595w4ODXgbXp4S-FmTJCOFizscGijyEPBCtpbkzs-shpi26RykXkgDn8gT2SbsrZJyHBbP3r-puaKHzrX3JN3cA50EGjyk6CPL3mdcLIVEKK2jbifAUoYUa5Z77_PZJ20TnI3IdE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
رختکن جدید و سکسی استادیوم نیوکمپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/103383" target="_blank">📅 19:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103382">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bbef9d0be.mp4?token=nLrgWxmX2SJYg4RJUH60c0kdn12RqMcFpdKnu7ySIoeiTfTi5ToKUQLVqsro07793l7Gg8YcmtwaAFAsw-qEDl_B_FTn_Jzq8M-KyaaEOSGhkilvqxuZjyGrMD2ElXlJh2AHKvb7xyHAGMGc2BuyxPQiScSDitcusPys3XfxcNG5YisXPhau3S9iszw4SQ4Z_AZCCLiQkG3vCyWabZKKT3z3LnhDacfl79Rxi6EgyJS8Z3Ub7rO76P1yLK2tZSLU5HTI7f1DSczt-lwYpoU_RVJ8Ftp0RgTL0J9UtfLuXQEcfIhZnWCctWbCQKMwIIQ2ny40LSMC-jb6zVO6yCV-Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bbef9d0be.mp4?token=nLrgWxmX2SJYg4RJUH60c0kdn12RqMcFpdKnu7ySIoeiTfTi5ToKUQLVqsro07793l7Gg8YcmtwaAFAsw-qEDl_B_FTn_Jzq8M-KyaaEOSGhkilvqxuZjyGrMD2ElXlJh2AHKvb7xyHAGMGc2BuyxPQiScSDitcusPys3XfxcNG5YisXPhau3S9iszw4SQ4Z_AZCCLiQkG3vCyWabZKKT3z3LnhDacfl79Rxi6EgyJS8Z3Ub7rO76P1yLK2tZSLU5HTI7f1DSczt-lwYpoU_RVJ8Ftp0RgTL0J9UtfLuXQEcfIhZnWCctWbCQKMwIIQ2ny40LSMC-jb6zVO6yCV-Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرواز زمینی چه کوفتیه
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/103382" target="_blank">📅 19:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103381">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی We pari همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/103381" target="_blank">📅 19:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103380">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sa1j6wzD4PWCZfoJZdBpcONOpK02NHjm3I3pfEBD9czlIwrgYCcMLuj8U-F-S5zIkX1lkvTpwNadvIpbiET56NLLuez1NqF6BiiUEbgVqASZ4-MAApw_1fmeI5YG1xNNmZgktOUSnWzrlzibrI5Omz0CPsmXvlbLoi8KUth4jAPfGxYGU8hZK4WNA6HK8dcUAuZ5o26HVjpXdMM2U71jt_oH4En1piNos-EVnn3kr29VnNTi3eiHnPAR-2KnQQYyp7h4SnkIla2y-jiBkvnwzTa-eK1oRK3qVrgqC20uw3EvMv-O4FS6zC47JaxIwj8zbcpZgIaL3nht3FUEGBQjUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی
We pari
همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر
💖
واریز اول و هر شنبه 2 برابر شارژ میشین
💖
تسویه حساب سریع و بدون احراز
💖
دارای مجوز رسمی Anjuan و curacao
💖
فعالیت بدون تخلف در کشورهای مختلف دنیا
💖
بازگشت بخشی از باخت به صورت هفتگی
💖
اسپانسر سوپر  لیگ ترکیه
😃
😃
😃
😃
👑
کد هدیه ثبت نام:GG007
👑
ادرس سایت:
http://til.ac/z5jcpGT
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا،کشورهای اسیایی
👑
دانلود اپلیکیشن اندروید
➡️
🔥
کانال اطلاع رسانی ایران:
👇
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/103380" target="_blank">📅 19:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103378">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Evm0A1Ha9EpED14uoL-QcmikHC2D74yKI6eNHeX-HptxQgVV5JUbaPLpAZYxVKBCJT3LKnJ1bQ--NKA3lIdPI54-ncbJXek5RSZvnlZQq6oxd_0b6bDSPuVlmoHJklKi6Ua9tdZ7aAv0I-adweiJudC_K_yp08bCvt7aeru6gr7TKxtuFT9Njljp_NbaSGb6wWbsWy-1BNYtIvJI0qK4VuJlcdSy13BuYDeVOaibL_97zp71rAekuRlG-jNeWS8vy70OMYPm_CbTRAgx1ETE9L5yNRiUUIWj8LZ-JlU7cA4N8N2nhHYAwOSia23cDhjRDVfppkApTQlwnXkpaYV4IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میبینی رودیگر از امباپه و وینیسیوس دریبل نمیخوره ولی میزاره گولر بهش لایی بزنه.
⚽️
@Futball180TV
| بایرام حقگو</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/103378" target="_blank">📅 18:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103377">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad153bb5d9.mp4?token=CNXnIOLdfbkjHppL1SfiPO5I_mGG82S3SXlDX_-kqm_09p7TfuBSYfnXk0pwZpp4os8pnIgq84WHpgEWI-hMhA8THVR1UD_kbJNwSjBCBetEDlHlPR36iMZr56iaE9QpSnsqGlkgSQCtwjd7xsIUXMBn8GfYaw1_PBh3Txd16vT-AAsW0g84-nprRNqQs2DDKFaOxJ5o8-Ks3jVIdWrLa02D8dF7CWPHcKomJ9oZVuHQLxQC6CkQKno-vpiz6YIqeHE1GJ-wVg1N_dfDPZxomaJF8wuyY55aSRtNVkPzAtjHwBYw0PkB7PwDbdWdjqmk1qhfekZ4lvragEWo1lwKuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad153bb5d9.mp4?token=CNXnIOLdfbkjHppL1SfiPO5I_mGG82S3SXlDX_-kqm_09p7TfuBSYfnXk0pwZpp4os8pnIgq84WHpgEWI-hMhA8THVR1UD_kbJNwSjBCBetEDlHlPR36iMZr56iaE9QpSnsqGlkgSQCtwjd7xsIUXMBn8GfYaw1_PBh3Txd16vT-AAsW0g84-nprRNqQs2DDKFaOxJ5o8-Ks3jVIdWrLa02D8dF7CWPHcKomJ9oZVuHQLxQC6CkQKno-vpiz6YIqeHE1GJ-wVg1N_dfDPZxomaJF8wuyY55aSRtNVkPzAtjHwBYw0PkB7PwDbdWdjqmk1qhfekZ4lvragEWo1lwKuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
محتواهای فاخر صداوسیما درباره فوتبال:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/103377" target="_blank">📅 18:11 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103376">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f850200c.mp4?token=iRPvE3oYAMt6CufrrLJtCUEIZETc2fKHVdYUKu3jnZ8ISZYJO_-QVHnLAs4Fgmrshs51wuvaLQnNZKc7VliLU2N6MyLlccDpQOWayAyDuofNpxkAKT76WprpVw0YTkz5sj42UOq613ISJLZhwoIkeJdowN8maWs5vikeY6sIahy0Z15YMuxPtZO6JsSJxoVbQBBkIokzsMAFp8jZs2LvRCoznfftPXyN9Qcw8JZQhJL3CmXeT-T4fssNXCnU5EdTjauP_e3moMRevBDXHItPMzgnzYRLOU1_bGhgVWxoJR1FbxtOSwRIGA1_qasq4L8jLt0MqxgMqeuud9-TR0j_zi0Vzl4k_PABo5SBeM6rPyBF5n2QPijh1VHuYSyMTagcTY2y5SrLty5_OQ-OK3Ux1NmRF0YIwwWIDL39AKll4L8REa4ryZQhR1wAXPQD-i3rEMP_aH_2o5tm7aGZO_m049rGH15pPXfq0UfM5T6cJ2QO0qHtbPt_YPTF2RupguOTn-V6fUFYufvW2YuasRVNO1SYoE7GaqLqi5qkBceWVV8MUHlDKNxKHdB7HYSOy3yoHCEjy-Hv9qCb3umPXV1fQVwdgkgxVDufs7svLDgO4xOUvES9vy8mFsLPDMxQllnNJtdvS8UBTc3e4tDj9NpoXwhy6WbkwxuyVP0ZxoCpwqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f850200c.mp4?token=iRPvE3oYAMt6CufrrLJtCUEIZETc2fKHVdYUKu3jnZ8ISZYJO_-QVHnLAs4Fgmrshs51wuvaLQnNZKc7VliLU2N6MyLlccDpQOWayAyDuofNpxkAKT76WprpVw0YTkz5sj42UOq613ISJLZhwoIkeJdowN8maWs5vikeY6sIahy0Z15YMuxPtZO6JsSJxoVbQBBkIokzsMAFp8jZs2LvRCoznfftPXyN9Qcw8JZQhJL3CmXeT-T4fssNXCnU5EdTjauP_e3moMRevBDXHItPMzgnzYRLOU1_bGhgVWxoJR1FbxtOSwRIGA1_qasq4L8jLt0MqxgMqeuud9-TR0j_zi0Vzl4k_PABo5SBeM6rPyBF5n2QPijh1VHuYSyMTagcTY2y5SrLty5_OQ-OK3Ux1NmRF0YIwwWIDL39AKll4L8REa4ryZQhR1wAXPQD-i3rEMP_aH_2o5tm7aGZO_m049rGH15pPXfq0UfM5T6cJ2QO0qHtbPt_YPTF2RupguOTn-V6fUFYufvW2YuasRVNO1SYoE7GaqLqi5qkBceWVV8MUHlDKNxKHdB7HYSOy3yoHCEjy-Hv9qCb3umPXV1fQVwdgkgxVDufs7svLDgO4xOUvES9vy8mFsLPDMxQllnNJtdvS8UBTc3e4tDj9NpoXwhy6WbkwxuyVP0ZxoCpwqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
مرتضی فنونی‌زاده رازی رو افشا کرد که امیر قلعه‌نویی در جلسه‌ای که با علی پروین برگزار و در تمرین پرسپولیس شرکت کرده بود، فقط یک امضا تا سرخپوش شدن فاصله داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/103376" target="_blank">📅 17:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103373">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f83944eb6b.mp4?token=sEf4NE4_uyudwZ6KGgDYz5tu_ZNHPDvJ6d5hg2o5Z1qDsiELCDsLVWzWSuu33B2djQceaHwsqNrXbsbM9eJhi_8uetc-OIz368TVibWcsm6iWZVWvsDSjUdANZgvPamaCC683cxORDBO5cz82AK-JlOd6bB4UXui8cffixWVVswx10kPG_24jdoAFPx9W6Qrm2am12FoB3VtrAyIxeCnBCATJ6-Wp30elL4syPBo5pShDX7QmViYWkAIjckYZRAM51TdZxbG4b1IWGWj2Jzfv-C-gGr6rtWjnshU2gvLCSmX2n_WEfglV-xEuB5NjvU1R_Tg8BskHNLKH41ame6cjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f83944eb6b.mp4?token=sEf4NE4_uyudwZ6KGgDYz5tu_ZNHPDvJ6d5hg2o5Z1qDsiELCDsLVWzWSuu33B2djQceaHwsqNrXbsbM9eJhi_8uetc-OIz368TVibWcsm6iWZVWvsDSjUdANZgvPamaCC683cxORDBO5cz82AK-JlOd6bB4UXui8cffixWVVswx10kPG_24jdoAFPx9W6Qrm2am12FoB3VtrAyIxeCnBCATJ6-Wp30elL4syPBo5pShDX7QmViYWkAIjckYZRAM51TdZxbG4b1IWGWj2Jzfv-C-gGr6rtWjnshU2gvLCSmX2n_WEfglV-xEuB5NjvU1R_Tg8BskHNLKH41ame6cjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبر بسیار بباید پدر پیر فلک را
تا دگر‌ مادر گیتی چو تو فرزند بزاید...
نام و یاد استاد محمود فرشچیان گرامی‌باد
🖤
برشی از صحبت‌های استاد فرشچیان در دانشگاه هاروارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/103373" target="_blank">📅 17:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103372">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVsSBldX71-lS_auNN7_w7D7xTgQviYQpPnDO-F_6fDyz0_8f_FemA0l7szuQDgCI7zzOdis6BpARkkges00l9ONdRjjGNAkflzLPQIAxO0KjCK9m3bAS5AghJFi45lHVFa8OR5LNicLgSHrUmDqjfu_Mof9m4g_fVu-BFk4mWvuXrSS_OGRbk25whxCyibBJVIAKZZcwWyfHciujpt8rudnG_g1Lt0PfbxBgdf2HgVY40eB5Q0uiE11oGlj0OxrlJNkJAIqOjp4oDTG7BQTpl7Ew8_510mxX57HCLzzY6mGrRJGmy5XbWpTK8MDjN7AhmRnqT_5yfkkbULc4U6iVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
❌
بیانیه رسمی باشگاه بارسلونا: رونی بارداگجی رباط پاره کرد و به زودی جراحی میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/103372" target="_blank">📅 17:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103371">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUTos2ndKde_ZgG8sfOagoAXSBNZGn0rvIKLMBbieBMjGbfwQwPxQ4pgeVf5ytTKFbHDPS5wx09S1PlAR9MbDxrmO029kW51IgisL4w85Rz4XfYgT7LQ-LUW9429HnrmcVp4QPyoeOqfpeZExoaZqsHParyQ_p0PFzOAaBwdf00mdrZ8-Jk2wJWCvYAb_Nu0bzGmxKxwRwQCs1UYx_j8w2cwKU5Sk2XCnKAeRddQzrH3iXHVfFgSxGUlo1GodciowOVXovFCCmfWF5LstBmcWvYoYxr2SAi6yAnpBSIB3aKD_HmFdxQeuBeRQE3g_kNapIAoI5RkUEEY3fsuHasglg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
فنرباغچه همه استعدادای بگا رفته اروپا رو تو یه تیم جمع کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/103371" target="_blank">📅 17:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103370">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N56nUWWQMdCYsJ-oLmyRQBNMWi8f2U1VLA4GC2FXjXVyNsXuRlrNIXx_OnrxosC6YlJCZeQ27H60ZeVKtqvf9HE2tMq0K_uNgMB46ftIuQ3-qLf9zQjSWxPVaHNc0fCVl9YzAJxa3cbsxitfwcOjRk0xjJstrPEYAGplNAJJrnol8y2i8-AnMKbKssXt0yeSikGqlF3ePBC3cZ9mS_QCF8SZD3_RFfJOyHrst8KySf-GiyWMBfi7eHCsPulSXf8TE2KC6i0d5zemHq5gjZwNn7xgXujp1QvLZEKvQHR6avP13vXaep5D3zLkUkmDrnTsK2RF82_HtZvuRCDMB_PwXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
لونین دروازه‌بان رئال مادرید بهمراه همسرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/103370" target="_blank">📅 17:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103369">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9fc92de2f.mp4?token=GjLfrzOjbdk49cmYqllVZrHLUV8BJ0C_6nzZISKMIz1F3YSXD-Broh0vqZjpsvIe-xDrG9U-E4PfY695wrR5aQ0enX7Pafm1H-I24AZEUI8h0toRXP2LLOhIV-QaMlIa0bg1sJS7HwbENF3jKTYGkvM33MBYwOQo0WspS_vbKdkdDTZWTJRI-0HHQYYk9t8svinVIOBPk2TjPwS9rrbcwPJ2s6Lcfx-ALO_4bFR5pl9CrqNwVfpvNQ2uXjeDXPgS6F1-ntaNZfYd5850HLyQxkWhVDEmtdxiM82d0djYT6phlQ-TJI98AF0LhbaEDkGq7WZUahNKGyyc7LuFDhZc7b5v7VcA7sRJO-d0o9kHPNyPuqWBpf59y4hUBUlI-TdJ0uRP73iqay0_aFClgleNUfw2rWmbBtrYh5Ay16GBskP_UWJ8Ff9qG9Yts7jT3_BMjE6UQDOeVnL2idgtERGC026j7HrRIdF9XZFTh6Og0Tj-w8KkV5SkMr1QDpLyK-LFeXd8NdxkIjBROuSMnrDOXRTF2SwkmkIfB5MAFbZKLvCLt8_sGxxa5t9b9clbyWRhMJ2y7PaOgc-hukkv-ZT1bHrY1UBd5s_NYyshmdxcPWBlKVsZRqbMQvuYYVm31jKGZ3iDN0sBjqczDqbINCcByZo8aSEXO9GEVhi7_spZvi0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9fc92de2f.mp4?token=GjLfrzOjbdk49cmYqllVZrHLUV8BJ0C_6nzZISKMIz1F3YSXD-Broh0vqZjpsvIe-xDrG9U-E4PfY695wrR5aQ0enX7Pafm1H-I24AZEUI8h0toRXP2LLOhIV-QaMlIa0bg1sJS7HwbENF3jKTYGkvM33MBYwOQo0WspS_vbKdkdDTZWTJRI-0HHQYYk9t8svinVIOBPk2TjPwS9rrbcwPJ2s6Lcfx-ALO_4bFR5pl9CrqNwVfpvNQ2uXjeDXPgS6F1-ntaNZfYd5850HLyQxkWhVDEmtdxiM82d0djYT6phlQ-TJI98AF0LhbaEDkGq7WZUahNKGyyc7LuFDhZc7b5v7VcA7sRJO-d0o9kHPNyPuqWBpf59y4hUBUlI-TdJ0uRP73iqay0_aFClgleNUfw2rWmbBtrYh5Ay16GBskP_UWJ8Ff9qG9Yts7jT3_BMjE6UQDOeVnL2idgtERGC026j7HrRIdF9XZFTh6Og0Tj-w8KkV5SkMr1QDpLyK-LFeXd8NdxkIjBROuSMnrDOXRTF2SwkmkIfB5MAFbZKLvCLt8_sGxxa5t9b9clbyWRhMJ2y7PaOgc-hukkv-ZT1bHrY1UBd5s_NYyshmdxcPWBlKVsZRqbMQvuYYVm31jKGZ3iDN0sBjqczDqbINCcByZo8aSEXO9GEVhi7_spZvi0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
▶️
لوئیس سوارز ورژن ترسناک و جوان آژاکس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/103369" target="_blank">📅 16:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103368">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtJQtIeJZCiZEJ1IjTZgvGsF83AfgNp7ovoe37tCA_uPWCphhFcvpBungmHxStQ60t6YC-vxW9KKz4X_FPLhJCjOHYo_KAt0xgZKdgXq1vmnpg-WCyzKzE00KtX9JnVfji24D9QGmBGQcgEncHcuYQ4kuW6U_l4PvpPkBIzBqez3UzcBBpYyGfunX9tbKgpB5cWTH546Fz3BgwOb3o_Dm7PXwYjdh5yXVLCy8h3xj3a-RjXHqqna67wNHB5v6WjGootpGPoYM7NV7qDh5YADYPE3TYDlKQovtdQtCxTnowo0Lzhm1pXnh7SREL7G6TOxrE--qnsDi7RpHhXJLsfTdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❤️
رومانو؛ باشگاه بشیکتاش، پیشنهاد نهایی خود را به دوشان ولاهوویچ ارسال کرده است تا در ساعات آینده به توافق برسند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/103368" target="_blank">📅 16:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103367">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b011d4118.mp4?token=kzjxxadhJKkq9K1A3f6_pSAquKTxzBR8uA2RXSW0I29JKLBdQenGRJJt0sUV50lB1wIc4reFZpJoA7koWoZGcLybfY543jhR567XohSbMO8Z5gv3iuowGYohgXfCQMUBhTinIND3GPtXb7AzUuO8EVGw_GuD4As7S9-J930XQh2kfB9qPKvjGo_peBAModEOMZUDJWdyGCPJARzZlQk7MqGckcdlnHujkV-8VyrTgws4xge0FNbfQX3taqX374nnG3-_eBT3K7RiHoFAmOMH1908Jt6vTnXEBJD6IlWxm3hjpSmFmnhJirWwGZ6b_vi4tNJWiqwLxLRl2EqM7WFyCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b011d4118.mp4?token=kzjxxadhJKkq9K1A3f6_pSAquKTxzBR8uA2RXSW0I29JKLBdQenGRJJt0sUV50lB1wIc4reFZpJoA7koWoZGcLybfY543jhR567XohSbMO8Z5gv3iuowGYohgXfCQMUBhTinIND3GPtXb7AzUuO8EVGw_GuD4As7S9-J930XQh2kfB9qPKvjGo_peBAModEOMZUDJWdyGCPJARzZlQk7MqGckcdlnHujkV-8VyrTgws4xge0FNbfQX3taqX374nnG3-_eBT3K7RiHoFAmOMH1908Jt6vTnXEBJD6IlWxm3hjpSmFmnhJirWwGZ6b_vi4tNJWiqwLxLRl2EqM7WFyCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
پشمام؛ روایت یه وکیل از جنجالی ترین پرونده خیانتی که داشته: زنی که از انگلیس پا میشه میاد ایران برای خیانت به شوهرش....
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/103367" target="_blank">📅 16:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103366">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FoM34XMEv2ikP1MS7rSlEfiGazZ4EmACDbGDKDmc1ejrOC27bEdNxaJCpNP1Gnqeab8iuGm5yEJ43IFiEiusSA_sB-lE9sWw0aqYiRWiaZwNSr4qmXsujH2IbTVTgbDNfZ59AiGo0tjXRDwV7648Ue1n37ImTjMBH8n3tkUqH0BYxvN8N4AOou9ZQrNmJJuJVLqj_yQZ1BmXDyC8mxxijtfxNiAvwkJzCI-EoJx-aCbD7k3DjruBw26IpvXC67e0PODyS1_BfxtUmOk13zo8S-tCbva4dacUuEfb5MAjHVcyi7FZwVbeb7QFAVvyESLd_mzTYA0dvueh7vkA7ZGZjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔴
آلوارز در تمرینات اتلتیکو مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/103366" target="_blank">📅 16:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103365">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gf6LS8_xndC8mLxhSvNxyTeUF2BkrxZltNBVzq2p3NpHhdlZPOk8V49QMddwhpZ90UPJgX2tsMRid3QEcLd85v6W6oJXjzb0Pz-UxYd1vjAAcA-h9VGCK8dNe8Fd93Zerxm8mj2Gfq3DVlX1q6doWr9hNUxOVVtdQktx_XhU3zhCdCGXgg1lVuA8Cayvl8GCz7bCOp5i_0kSEZTxrl7tebIGu0V2E6qNnpd6uPoJXdgXZMK8d0Ei2Y9dzB6TisPRDnO5ZnPbD7ILryhA-1JNnAp1VUFnLyWG1usNNzKrCNVv2IFXlc2-AF3Cf-ymZZlzKyF5lP9NczfrlKcQPa0kuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇪🇸
لیست نفرات رئال‌مادرید برای دیدار فردا مقابل دپورتیوو لاکرونیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/103365" target="_blank">📅 16:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103364">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2091ae4f3.mp4?token=vYP1GnRiE-tO72v3Hnvqj14TFfF3RHYRMmphiGWi46F68woHYiBeDa0kDff8TvVb0OopEJNQCN7OsEnw2EjRlVD941w82DI3pnQNEpAYobQjI2xdrdR7grgRXUcuYtMslMSi8mBJ2rotzNY2C-BaSBXIG8ABwwkQzcUbLd6BNHXUeLfBKUrs9DYgNqAvil3Y1Std2lclpBdfwZU_bbexALkB8lnQGbCpXiyQ-8uDlaQc1HyxFzqNnM-QVwoBluKq5OggSvPRxkiF8whyngiGAzzJHub4Uzq81lB79RnuXYt3JkZMwvNxmxjxOXsC5rH9wurBWwNSajo7eflv4Is0rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2091ae4f3.mp4?token=vYP1GnRiE-tO72v3Hnvqj14TFfF3RHYRMmphiGWi46F68woHYiBeDa0kDff8TvVb0OopEJNQCN7OsEnw2EjRlVD941w82DI3pnQNEpAYobQjI2xdrdR7grgRXUcuYtMslMSi8mBJ2rotzNY2C-BaSBXIG8ABwwkQzcUbLd6BNHXUeLfBKUrs9DYgNqAvil3Y1Std2lclpBdfwZU_bbexALkB8lnQGbCpXiyQ-8uDlaQc1HyxFzqNnM-QVwoBluKq5OggSvPRxkiF8whyngiGAzzJHub4Uzq81lB79RnuXYt3JkZMwvNxmxjxOXsC5rH9wurBWwNSajo7eflv4Is0rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
رفاقت ورزشکاران
💞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/103364" target="_blank">📅 16:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103363">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3q3Z1Pn8BaZ0dU-hgNKHWfN7Ma4gV4jjx9PJoe7Pv1N_lO3QNjVgbqEHU-W4jZCfkStPgs6GZ3PmRhzW7L9tHhH8LLrtTsN0eyUTVYbnLld0CpGlI2Amqv2G-Aq4QPBrF3MygSAjfCte93atmXgpJllwytffsDRmn1hyH3HcD-TXcvx0ciPZw2wDy9zq4FoUk_SArJatpVp0dh9fhT6c9uGRW9vcNKaKptFPS2Q3X9FLyzMWcKaKbsfnRddpnT1exHavtAOM4ejTMQTKoKfBon7t7FA-QFyPrMTSVLq0oHYM1IHDH093CFvHMTMzmkyeSq8_ENX8m25MiwAQGE2-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دخترا: پسرا وفادار نیستن.
پسرا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/103363" target="_blank">📅 15:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103362">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFpOVJGeqUzrMiauv70EY0zceCmlnCnvRZBM7Ea-aw_PupmWFdgPKRJVGJkf57c3mMwT2FfQ5ReuO_kj7xzth3LgDYMpXyuFBqjnf5LW561V8ZIPIAM0kKKi8T_80EHqRUfZgteTeY3lX1D_AvNM-DQDXG5BrXD2Ol05aCpIZAdafid0V3Bo2GW_6QbR2XWGvtI48XFoJUtSkfZ5xAxftuBQHZJPwdSonj81xipQft7uvatqTpgoq2g4R97c7GrCuwe9m-d9axqf7JiW28trCn9k0Qzrkp1gYiXZqIbfzBiuDUuq0Uey4sCoWZFFET8ePh7nCuWVe4VbqylDN1KloA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
✅
فابريزيو رومانو:
اینتری‌ها میخوان هر جور شده اسپنس رو به میلان ییارن. اون میخوان این انتقال رو با کمتر از 40 میلیون یورو نهایی کنن و مذاکرات بین دو باشگاه به زودی از سر گرفته خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/103362" target="_blank">📅 15:18 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103361">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bea6d735e.mp4?token=sV471rvxEPr2xZ76IN6ldkB0Bm22vr_0tNkA8MMyV3uZ4QvBJcu4csHslY2QkIvDqHCKLoxP0B1mkvOSEcSG50zBV9isxHpPlmjHj7wCAEWyiJhk-D6pvs2VtNbMff6l1l7K9rNnvePo5gPlqey7fQNI2V3ixgRtmrlG03dGw1EcXDzKgikfxRg2fN_mbLqfle_hk3irSIfX42MA-zyom1WQ8FPw6u3SI3p0t2ZBPMWRvXhjoiC6KbzhrF70kWDSQlQ-fi1dt_gFz6dv9KtLnDaB-gVe4cUA6WDiX-420zPsyml1sREgqL1Uu7nnh--yPHlyhzTb69lTKkFKWH7SYoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bea6d735e.mp4?token=sV471rvxEPr2xZ76IN6ldkB0Bm22vr_0tNkA8MMyV3uZ4QvBJcu4csHslY2QkIvDqHCKLoxP0B1mkvOSEcSG50zBV9isxHpPlmjHj7wCAEWyiJhk-D6pvs2VtNbMff6l1l7K9rNnvePo5gPlqey7fQNI2V3ixgRtmrlG03dGw1EcXDzKgikfxRg2fN_mbLqfle_hk3irSIfX42MA-zyom1WQ8FPw6u3SI3p0t2ZBPMWRvXhjoiC6KbzhrF70kWDSQlQ-fi1dt_gFz6dv9KtLnDaB-gVe4cUA6WDiX-420zPsyml1sREgqL1Uu7nnh--yPHlyhzTb69lTKkFKWH7SYoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادل و دستای پشت پرده فوتبال
😂
خنده بازار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/103361" target="_blank">📅 15:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103360">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhQlGuyL0J1Gjx3e9--D-GejCUB-HoSiL5l64p0w71mxMvqOdgf1a58BNEokeWfbbf8vkzv5t2KOrATbyRH7vHNFO92jalzzD5cU1G0YpkAGb5ynMAPuDhHikCpbVRddPYU2UMhPHb4xKlDcoNL9t5gATjAoWwjR3zfU43Uuk16AB3EMh6cqI-Mbsks3ME3hwXtT4e2ZIau2x5bbxSdCVWlGCW_Irg7hoAewCUkJA6aRgf6vmB2bdztBq_ajyhQLruyYGAZnNnxeLMLFPONizQeO1sa7yWgPM3Jnn_WIPrH3j0U-F5ggZ74RmMzWPXSJuS1g6LyMqOPLYqwGzgeRcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
🔵
فابریزیو رومانو: فلیپس با قراردادی قرضی از منچستر سیتی به شفیلد یونایتد پیوست.
𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/103360" target="_blank">📅 15:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103359">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfyO5x5wHH2wH9jcN5eQpp6V9I6ZXbVkoJxs_w-rzzjWS971WPCcBGT91zjg0OeGzksjXnluzcyiXc1bGAi3TLpiU_LU8orVOCNyrzaag6c5wIsJjyOPpZv7TDblFV4nL23uYxkFyWw_rdAdH9tHAObV9JJ-jDdqYEbU4f6jvwVTtiXhjMybecXItXu3o-RclRHiIRWdkjfnqBaiWCCruxekCB2UDctTRDnqf947H6lNcqo5bPsu8IcqlbHjRfronPXGrM4rKEou8Pvrzd6nIsaMeWRg4-8ojn9Tb9abgM30JjVZOYbnOktTl6rMSQmQLpYgZr1_s_tydApWqNBtSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
🔹
خط دفاعی یوونتوس در فصل 2016/17 لیگ قهرمانان اروپا فقط 2 گل خورده بود تا اینکه در فینال به رئال مادرید رسید..
⚪️
اونا تو فینال 4 گل خوردن و جام رو تقدیم رونالدو کردن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/103359" target="_blank">📅 15:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103358">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1146b9d2c3.mp4?token=Nt-HkEGqGte27Sx7nqKW0ov3TJLD5NAV2w0OR2vllV-7QGjZAV7dxzGbEsrGXVu-wFtLFWkusY4sqfXzi1frMetAlt_rQWod9yTNgbpnSZS_2J3xjOw2kj_kyvsZ4VEVJ7qMpuo2c9C4lfKQZ0rPPTdsMOPuoF5sX-K03jAaoGzcfju0tpqjgu25JF-OUmnO7Y05cQvNzUbR8o9GC1SZov57-00sJKVGv6h6k29klD1qMFuqLH146xXzrRs2Ri1s-1txSFV7gRU-EZoNGe47KlzmjnGgj7Mq__m49dfe3j4s2pvFfDcxfxB9rYNOIJW91R39l3d-D6jw97YRForHBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1146b9d2c3.mp4?token=Nt-HkEGqGte27Sx7nqKW0ov3TJLD5NAV2w0OR2vllV-7QGjZAV7dxzGbEsrGXVu-wFtLFWkusY4sqfXzi1frMetAlt_rQWod9yTNgbpnSZS_2J3xjOw2kj_kyvsZ4VEVJ7qMpuo2c9C4lfKQZ0rPPTdsMOPuoF5sX-K03jAaoGzcfju0tpqjgu25JF-OUmnO7Y05cQvNzUbR8o9GC1SZov57-00sJKVGv6h6k29klD1qMFuqLH146xXzrRs2Ri1s-1txSFV7gRU-EZoNGe47KlzmjnGgj7Mq__m49dfe3j4s2pvFfDcxfxB9rYNOIJW91R39l3d-D6jw97YRForHBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
تعریف و تمجید ستاره‌های سابق از لئو مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/103358" target="_blank">📅 14:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103357">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNRsDaPUpCgY_N2tcM-iA0kJ6VYkXICe6guKBYBJNCzJl10kVkDbJkp_6hUjQlsD9P3tag0INhXgN_aJTLOg6uGQRe1x6nA0J6-WT4HH2-3vmVQPIvG5OI1owQEWJ9XCiHu268cE7GRmw6OLuoTqjZfSnlAUaFLxE4Xzgq1mXZEHtoGdF285TWAUzz_XtWaBHjV27aKDj9-cocV5_kVI74XD1w7UvLvhDKoSi-4DK8Lt5DF_PBtRgyQ0notDDKkzNQisK_-U9Q-XLcJilY4AfopqN7_3Mni_1-tQpUpcuMv3sIfH1zsJw6TWpBn-eYpOp0qICAD2_MRHMRJE_M3NXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
#فوووووری از رومانو: دیگه مثل سابق قصد حضور فعال در اخبار نقل‌وانتقالات رو ندارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/103357" target="_blank">📅 14:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103356">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/befb00f0c7.mp4?token=gBZJJ-1l30sqou2IkV3Si2purOSZBmHDYR5dZN3VfFdbzESuZ2g4XDFSlM7bhV7Nd4OJAKXgl6hJsJWs5nxZWg99wAhpRLTbeqDFAl7bZSTsnfVHLjik-6kd7dKRXxACkiaV7zbmolLr8xmRtptqSfG39HQ3kT7r8VnId-J6awrShcFuB32kt4uxWoHlGGPkTzWRx8cceviRlbjA_t2syBAxZs-n8xCCfxgzRxitcZBVHu0Qh_jNj78nCTrfJGJ1dhic1POWqNQzzayD9MDAIWUcInA7P7CNOVC5W8EGkv_1ZNeSHe_oF1O2a98GiMK5H3dQaUCoGK-zCc-AfQg5DLyvIIgaYgoTIRjIcJNpWG6qYSok5Ymce1O9smTFzy79X6eXN-kYYPodgInT4lZo_6mNTMfRN__iGEk4MgFkrR0BW9qOTN19VNYcnLrHuyPYpRfZSkwV9Icjg58E11Rc_lUGKWCGCVajsO5jdLG_Nqrf71hFj3HzNfixM7P7Zp-E59LAi3CCOuSPR4GoyI31h6gt4BMV7W_vmDuz3CB_0pvVto8OeoSbbZ_Fv0zgEUwIfXiCLEB400Ha40y5tdiD98zK0nSttyaebObwaUoNE3mPO1w69Xhus-4FwW9_jkp00RaNsOLHKv4bxhsM3U45gn0KEkFUUZQ4i5F21i6QS9c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/befb00f0c7.mp4?token=gBZJJ-1l30sqou2IkV3Si2purOSZBmHDYR5dZN3VfFdbzESuZ2g4XDFSlM7bhV7Nd4OJAKXgl6hJsJWs5nxZWg99wAhpRLTbeqDFAl7bZSTsnfVHLjik-6kd7dKRXxACkiaV7zbmolLr8xmRtptqSfG39HQ3kT7r8VnId-J6awrShcFuB32kt4uxWoHlGGPkTzWRx8cceviRlbjA_t2syBAxZs-n8xCCfxgzRxitcZBVHu0Qh_jNj78nCTrfJGJ1dhic1POWqNQzzayD9MDAIWUcInA7P7CNOVC5W8EGkv_1ZNeSHe_oF1O2a98GiMK5H3dQaUCoGK-zCc-AfQg5DLyvIIgaYgoTIRjIcJNpWG6qYSok5Ymce1O9smTFzy79X6eXN-kYYPodgInT4lZo_6mNTMfRN__iGEk4MgFkrR0BW9qOTN19VNYcnLrHuyPYpRfZSkwV9Icjg58E11Rc_lUGKWCGCVajsO5jdLG_Nqrf71hFj3HzNfixM7P7Zp-E59LAi3CCOuSPR4GoyI31h6gt4BMV7W_vmDuz3CB_0pvVto8OeoSbbZ_Fv0zgEUwIfXiCLEB400Ha40y5tdiD98zK0nSttyaebObwaUoNE3mPO1w69Xhus-4FwW9_jkp00RaNsOLHKv4bxhsM3U45gn0KEkFUUZQ4i5F21i6QS9c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇪🇸
لحظه‌شماری بارسایی‌ها برای جذب رودری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/103356" target="_blank">📅 14:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103355">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FULRv9Vru3ZMfS_JxPi6oCm2gTcZxq2F8q7FDG2Q-aHwhBK5MaXQihxEsYBxY-E4GnzUmHa5k1aacwOrT741MaFMH8rcLC3SR88ul9MqWO9zMnwnYa21X_iXhT89lQYCb3KboGQdQILLE8yruW-jJje4yxEe8srHnmDwQjFzW9JDDWbMLfvkFB5d3sDNIeYh3AD-7EEqWr_rQDE_2V7JJXP-wUn2eVfMtcNne_UIo3LUnxEsynpJDtx8wybWrgmdMhJNROzM_7hOXX9c68mOC59A-jVEAXiPdMHSp4eyCnAXllgEhmjQvrt7H7tZiAFjhC7PFb0nX2FHsvC67tgkYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔺
🔻
دو تیم ایتالیایی که برای آخرین بار قهرمان لیگ قهرمانان اروپا شده‌اند:
🔴
2007: میلان
🔵
2010: اینتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/103355" target="_blank">📅 14:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103353">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
#فوووووری
از رومانو: دیگه مثل سابق قصد حضور فعال در اخبار نقل‌وانتقالات رو ندارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/103353" target="_blank">📅 13:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103352">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/spjjL8EUgnZTwx1iVQOuGVuLoXOQV_iJufQk-BnOzV08-hlIZkGMHiiDPXNRbxzCdW1rr9ldFK68gVbwKZRDn_3SUWzBOnzz6eLGzCRWEUv3OtlXEXiSMRXARmSCl1Z6uGMvqO60uzQEjBcFeI6LmfkioFH-vyVXej0zJj5cwhSkkoVJyIZo-YEY9R0Kq2tfUNfXV4jqLhhHnS-mNEUHh5JefxLUuDNJKhlIrtKR1Ud6lAEFmcy82OV1Y2P1K7veZcEN25JvqeXAnplWZVOerI_cln7LZwMPwEcQBwEOhQPsQTdu-nPSGR5oYP_7BmGrxqIZVilE4nCzgDRhtJg2-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
😆
سال 2021 قبل از بازی منچستر یونایتد و لیورپول، لیورپولیا میدونستن که هوادارای یونایتد میخوان جلوی اتوبوس تیم رو که داشت به سمت اولدترافورد میرفت بگیرن و نذارن تیم به ورزشگاه برسه.
🔻
برای همین لیورپول یک اتوبوس خالی رو در مسیر هوادارای یونایتد فرستاد، در حالیکه بازیکنان و کادر فنی لیورپول به طور مخفیانه از یک مسیر دیگر به ورزشگاه رفتند.
🔻
نقشه‌شون دقیقاً همون‌طور که میخواستن پیش رفت و هوادارای یونایتد اتوبوس خالی رو متوقف کردن و حتی لاستیک‌هاش رو هم پنچر کردن، بدون اینکه اصلاً خبر داشته باشن اتوبوس واقعی لیورپول خیلی آروم و بی‌دردسر از یه مسیر دیگه به سمت اولدترافورد رفت. لیورپول تونست برای اولین بار بعد از هفت سال توی اولدترافورد یونایتد رو شکست بده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/103352" target="_blank">📅 13:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103351">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9708df2d85.mp4?token=i2XTIzOTjKaRq9ZYerF5LynES8J5_TwoR7qAemaA3RACo30DK_t6LrjGtud9scpFNmmkYmhdo9Pa8qvwIm6tr6aoF9YSiqsA0GFIVbTXtVZ8dX9nezahkzuiQJAAm9wp6ligTiuzh7t6T6zP6CkblDsUd3jEIvxq7rNArQMJJb-3ObubcViC5beGmrch7280jbSn7BBdG5tk1otXkiE2KgM4sQI0sDLwcdVOSzKGIfQjrc81-Teg1qCrSNs5rnDTilz0zihqCavUBlqgoTyI5fbgU9ohZbwp-EMhe0uUUQ7C4Vy26bNHvmYCfDQNo5R_y6Ue8X9sBP6ZGyKSAcy8GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9708df2d85.mp4?token=i2XTIzOTjKaRq9ZYerF5LynES8J5_TwoR7qAemaA3RACo30DK_t6LrjGtud9scpFNmmkYmhdo9Pa8qvwIm6tr6aoF9YSiqsA0GFIVbTXtVZ8dX9nezahkzuiQJAAm9wp6ligTiuzh7t6T6zP6CkblDsUd3jEIvxq7rNArQMJJb-3ObubcViC5beGmrch7280jbSn7BBdG5tk1otXkiE2KgM4sQI0sDLwcdVOSzKGIfQjrc81-Teg1qCrSNs5rnDTilz0zihqCavUBlqgoTyI5fbgU9ohZbwp-EMhe0uUUQ7C4Vy26bNHvmYCfDQNo5R_y6Ue8X9sBP6ZGyKSAcy8GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
مقایسه مراسم معارفه در تبریز و ترکیه؛ فاصله جغرافیایی زیاد نیست اما فاصله سخت‌افزاری کیلومتر‌ها دیده میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/103351" target="_blank">📅 13:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103350">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWp9g5ZJAc9pM11d2hIqiadyXQGAcJWyIDsrpuHr3_ZUHGJZNS6pesjKT3blzaItt8TCzTYGSNXtCz0aBQWIDa-t-qnPa_D8ko3SjFLmnuYZNTXRUK82jMKIwPfn9RCToTVW4oWzrGOW17uUbR-nEBzFn99sy9IwuxS1UtiADdPCxyHA_Uc1rGS0o-SmonhRYyhH7rtPmldY55_FEKN2aq5DA3_nfA14M5GYiJs-S3wKZwxaAl5hq_8YNNYKbdMpBr0T2_ev-rwV99gwu1jDlCI6KF8zAeZFcigOzQrMqtNrCwK4l2C7YYM_nN045_qfxhcWPQmOrKSECzLjQNzDOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری
؛ ورود خولیان آلوارز با وکیلش به محل تمرینات اتلتیکومادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/103350" target="_blank">📅 13:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103349">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/705d7fe27d.mp4?token=SjQZNKoLp4Spt9Uq31NsFwYgE8kFj8u8VEKI0ed4MLzm3zq2p4vpYfxdMYYBoTvnsGou3IRFh81GDjPd0BAOnGPenE_3tuK2sj_eis80May6bEtPa2PGJW3xyLy5uMaqcIffbDDnpl5SqXPnwyejPj1SZWAgBb0eo0oEV0BHvSdrchWwk884_0kx02Jp5P36MqOyb17yjEG_4InMMwmfx-4LamWcEv9wGfCOop69eWI2iP_JOP6mJfzBA9cj0NTXmFd3lRYDlw4-wWb_TsQ2rSTYnCX_VzGIUEWQG0pD2x1MuEP3-GAhi4QhTacaxWcjhXMHWUqytyoeBRkl12iyvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/705d7fe27d.mp4?token=SjQZNKoLp4Spt9Uq31NsFwYgE8kFj8u8VEKI0ed4MLzm3zq2p4vpYfxdMYYBoTvnsGou3IRFh81GDjPd0BAOnGPenE_3tuK2sj_eis80May6bEtPa2PGJW3xyLy5uMaqcIffbDDnpl5SqXPnwyejPj1SZWAgBb0eo0oEV0BHvSdrchWwk884_0kx02Jp5P36MqOyb17yjEG_4InMMwmfx-4LamWcEv9wGfCOop69eWI2iP_JOP6mJfzBA9cj0NTXmFd3lRYDlw4-wWb_TsQ2rSTYnCX_VzGIUEWQG0pD2x1MuEP3-GAhi4QhTacaxWcjhXMHWUqytyoeBRkl12iyvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🚨
‼️
تاج: قلعه‌نویی اول با ما ۱۸ میلیارد تومان قرارداد بست بعد قراردادش به ۳۰ میلیارد تومان رسید. ۷۰ میلیارد هم برای جام جهانی به قلعه‌نویی پاداش پرداخت کردیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/103349" target="_blank">📅 13:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103348">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
🗞
رومانو؛ سوزوکی به پاری‌سن‌ژرمن   HERE WE GO
🔥
🔥
🔥
🔥
✅
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/103348" target="_blank">📅 12:57 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103347">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NdQ3a0IrUUX4ArDwAaqA2xXGalERqYuOl8bKHJK4Ex-eYc_DOIsg_f6N-52DucZUO_xwY90R8nSFYnhoxAv7T-oxge-nX3zOoav2sya4qptumez0QzDSidp43nxdVPOQWb2Tf5V39IxzSlS4hmg-SX_-tn-WqK9CjIwLMU9XQN0UxirvQVcU1_xOlfaeYMBpD0hPXapntXl4WBXcjvaHjoZvyZLxk-2qcPpaHllENZAElYFPw5v2gBOEggNe64b8bxKkXncYy1ZFmbuAJuKkD-pHEVSmBD6XubXN2yfZ7XF4I5YNO991BAqeTirUelEyUXIgYTbrN_TWT6qDznKmEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
✅
هاوکینز: باشگاه پاری‌سن‌ژرمن با مبلغ ۳۵ میلیون یورو موفق به جذب سوزوکی گلر تیم‌ملی ژاپن از باشگاه پارما شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/103347" target="_blank">📅 12:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103346">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksEuBKO1oxXRao1udZiMv5WD0-dsDn4ECH6JY020cPrrTJ2frrT7whqDBSR5aCQZtVj1WaThZKp2_UPvmMqHQ02GFKxm4BOewI_M_Kmo1OttFBigfGFoHQdCMtx7u0BCb5y4WquI9qS78LQy20FCc2zaVl615M53T0k39V8wnteloJbrt3ENyVnfhKhkxxLR1UGtHS-3gXXf7jEDlwRHKzZpTh-QRunyEfaPYCGNvMFh3ljHYahYHQgDsllgU-AbcsoMo8pK9kzutcWKhc8l1nZm0UAwoZi09IgTeQR5odxQYSEgd2-7RchzvOXHrpHPMm46xHD_Na_yglHvPa6U5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
✅
هاوکینز: باشگاه پاری‌سن‌ژرمن با مبلغ ۳۵ میلیون یورو موفق به جذب سوزوکی گلر تیم‌ملی ژاپن از باشگاه پارما شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/103346" target="_blank">📅 12:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103345">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از بن‌جیکوبز:
🔺
منچسترسیتی اگر بخواهد با انزو فرناندز قرارداد ببندد، باید رقمی بیش از ۱۳۰ میلیون یورو به چلسی پرداخت کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/103345" target="_blank">📅 12:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103344">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oq-onyIDvW4aY1N5sUvIJV9heM9fWQ-Po6aWjaRMKY5tnGGKXrGJTojUbOkUaOz0cgB8Wk0wHKIBMLassLWbz9kXl2AoZgkRTWvdgze6fHSywBHN3sh9OZ-83bthafF13U6cfv_UtQMUtJm8Tf7ZDureQYiKyh95j5TCcFRG2pkn3s6pDJ9N3kICqw0gBsV95I1hUwq0aF3LIZscVcsftUqThIYNQmYJ_geBtV4tVPCDOrCjpqdhzxdTkAd_Vh6kjCszNqD7kUNrakh75tLoF0CfksQM_4VPs6VI36xUYi_NAFp2YmReJZFiYwGLhAsgRUvXLQd9fMYTtyAk6Lt-hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📱
استوری کنایه‌آمیز سیدحسین حسینی
که احتمالا مخاطبش رامین‌رضاییان هست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/103344" target="_blank">📅 12:48 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103342">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J_R6VnHFFua46d4cFlR96PtYRRKtJ3xAeDdkXKrvNU2GzULdH3luUeUsIby7dw0DkoDGF7RVxcC85QltRdnOj1nGP2pgsBn4pRxcE95ZWzvV107WZUpBwW7r_eHLywaqbsribqpoviyfUdDXp_c7QTqcCL4xiQSTEtBX2_xwhP2ldQpcGxcI9YC3pd1FknGbSooBhY0bIE7RGTCzGPiyrJmT-gvyo2F0CVWbuQPyeGfnbNtYHd_byJUGtzHrTSmpyDoTEPCsAMAomOM1OFla9sRCBniK7pRZi3bmXUD0fHriVFpGK7yPEyJSGVqCJIHRVzaGb_uTvOPtQXFSXOg6NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OHT42UK9t9yVu80phu67NVus1YvV8u1VPJe7_X6xqWm3517yjr-Rv_niVqCXYy_lwhA-E2vpOuDDzxklc7zfwnagnHgL0KhWSIj7FjPGW1NBYTOCGzXHx2ZCilShjt_-FF3GseaFjxw2femG4pR0KAh7bccdWfzKKsYRh9qUV9Ks0OT8N18q3QvPSTSKHhU5bKjqavL0XorutdHAFyJpcugF8ZYWDdx9AmXjxJ0djyEboIC7bN-l9-cRyNu8vpJ96UB88k9RLBbksnO0kJ5iwFiK3dOAQYmTcugNl4dO2sRe0Cv6jNZ0pH2h6JIc1-1u6_gZNMO8z6fp5thWGXylaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇫🇷
لیست پاری‌سن‌ژرمن برای دیدار سوپرکاپ اروپا فرداشب مقابل استون‌ویلا انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/103342" target="_blank">📅 12:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103341">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5bsajp_KKqfxRr63voGsA-z0VMR_Q1fqvCPma6XwPvYUPDqb6gK4oZYY1L-CcolRX4uYNNFxfaQuYHH1Ny9M70VS8ZY_5t37PwLBKbi4Wr19AU0bRH55v4ROD9vc0Y1TKNvJT5GeToDFhE5kOJVMQqeD2BoDfdafeB67IIcmI11hX4kBXFq-fqEtbeKNvVSFm-iQh3FuZN1xVRGLw4851nDHwuvZxYxERq5cRK6cStO6-srPt8MOZDVAXdshulLDgnmUfzviEYEM3YW1hCs7LkBieMZKB762rUo3PJL8HESNagJe7FfMcLcFCifn7nbDIcjCYLPXWMYDIOjiExRGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شما اصن تیمو ببین..
بهترین بازیکنا رو تو هر پست داشتن ولی طرف اینقدر عقل نداشت که مسی رو هافبک بازی میداد. همه جوره این تیم تکمیل بود ولی فک کن قهرمانی لیگم حتی با درخشش فردی بازیکنا میگرفتن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/103341" target="_blank">📅 12:27 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103340">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZcqj7enuicGJfeJBa7XUsp2s5M_7j34dJWn2PPF61227TswW7qva2-Q3OMSyXRGCSAsWOLAWYWh-lzYOOkisQeyu3DVFNkmJUmkk-C0LYOtlmOymqbGnpuJy6_XgKUaxAryItUrIEPjD-Z8fTEqxrFYhZqFxQEesc4uviZ6X9EFGmrWArUVLmQjbqY-qp2zTblRheDF_WDNaT8dA5nH6kvRi-vWeK22KRDBwEX1CiDLkop5ozbtkgovhAxjW9jwgrDGw3y-HRZMFcZkP--vxfTmYSy1Z7vYd2e30cua_N2arZV0n-is5Yecys9Lloq38fy7ek8kgLNs7j9hlwXhaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رومانو:
روملو لوکاکو به فنرباغچه:
HERE WE Go
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/103340" target="_blank">📅 12:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103339">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5tM4CT4pnaePDCfZcPFchpM8HsptmnNynd0a6z-cBCHnOM2WfrCLGNa8EzeqebU4sNkKfClug8enZwmuurrOnFxTBY2ZVU6UW0a-yW0FVAE6d8DbeGvV_aKeiNMtqXBr1T6gI3RWCjMu-2M1Jh6cj8lXa1YZSDnokX0vQNtDAU6F2h6HlVfRwW4nQhL6iWA-t_9LBu52ej4DeJjfxQikAcOOUWMdCCealndjgqEVq-irZmq4ZC9hJ8xkGRK97KL8HUsy_vrJEbAq0bBxCwG9MwFYgyv5MRFt5DM9_hX1vc0tmWspDByJ6Vmps814ecHznTXjfIJKX538M3DXtlkTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
مقایسه بازیکنان خط‌حمله وحشی بایرن‌مونیخ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/103339" target="_blank">📅 12:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103338">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUfozxL9ofojz1KKSSy-_nJNf_pgg-Eo8BFUd-RbjLRH_i6yekqWc-zA_tOCQnvHNdCET3pSGA3GmwiuhWyf4heoKLhl7D1fvoB-qEAF75c-_WGgvim3Vgym8jZb98ehWXfGeRLO_6yR3X7yGhw8Ki6d2LkgbCS3gqCjGXumt3NlhMHHf7h4R-kryuO2Yrg0whesIITvklK-Xb0l4RY0pEDGCrSfuP4Q70xoLZIyxMhy-9JG36X_dyeiNyNFoDrkpxd7x7Va9A4D9FMO3p3jCrGwNv7QoGX0rTvo7enHa4L6UosDkNWvCfLuX-g76UZww_Jmw0FccbmhEifhDPZybg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
پیراهن دوم و سکسی دورتمند برای فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/103338" target="_blank">📅 12:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103337">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQtoMPog2QV7gEzMp1hMaUqH4VKJS74Ckhq_1xVpB2-RL7Ukh4sMHPPd7nKCKVIRWJZcg51pMGV7ASFI0KoG7DleeV3CuKe-S1iUdAOxEINUDUome5WlRCbV3_Iu0YkeCJq0WL0cBSmWZdxX5-TeSK4tHBMClGOIEerzm0IL6OCOFH29HNImy3jXK2kI5FlRv-1VKQV0ZaqBcmmdZzq1Y02O-oZ7yrF0FlYX0YoTCK9x1HCzGCDv4vQICfuBAhpEzPPjFSQcM5VQn1b2JxOuYCOzOHA4JGi7KzNgpnlMZwwxtxObvwqBA44JCwz2FjDmMBufh0oEm_2-JnRJgmHKPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری بامزه جواد کاظمیان
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/103337" target="_blank">📅 11:48 · 20 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
