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
<img src="https://cdn5.telesco.pe/file/YDgGIKeUES_mT1P4WbRXqIWyVu2jye9MQxJXLTgqJkjohUcaDUc4z1Bghr96k_6trDA9IWW6tq4nYtIy2_0s7579sc4j0aI1vds7jbHKg0AM1eEtEGZKHdTsgZk6aUSSafK6pJKtiA76qG0wSP3NOF8nFiWSo1gCUDFU5ImKjpiZPVcAC8UQGjnPEy2OEReTvd6wZWXvXJerl7sTpqP-1jwHXjgENYE_8fao6po0pzRneDXkdxwofxVHfCskWG9fDgbd165C7fxLXXoe_RVVzlfsOQCaHrBG8kiXGVYp-EMY1mKcC0w46on4BrcjjCMkXmTtGPNkTHgoobanHdzhLQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 542K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 21:16:59</div>
<hr>

<div class="tg-post" id="msg-101593">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
#فوووووری
؛ دیلی‌میل: نیکو ویلیامز ستاره تیم‌ملی اسپانیا پس از تعطیلات احتمال بسیار زیاد از بیلبائو جدا شد. آرسنال از مشتریان جدی این بازیکن است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/Futball180TV/101593" target="_blank">📅 21:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101592">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76aa3864d3.mp4?token=TZuxHIgSJ334bfiW_VzB_vKZdgHnGpZwunRK-cpaTRrUmuqC1KIEmpNJ35CwkytHEIjZQRPGsvtfq1aMOUr8lR-U0n68BGz1C09Z5OsCXAkY_ImZSiBhsvQN531ShfZ1B0Jj9yNYdVUDcD6-s8hULEkz0KbW7ZplKSEbHu72RW4xwFbGHMlTZvde-67ANcUD3kWEk2pVRIqWBdZvUISH6QtDRJqwXr9y5lDRjMj40GWZjq1MG25WB9t-0fBps5wLyGQnVQu9VuHHcRuh6gh6o39EBHqbXVWLoDJV2AAf3dIFT0tn6ljbeyJI8TYCknff63qywgBhgHr37rGXGYJvVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76aa3864d3.mp4?token=TZuxHIgSJ334bfiW_VzB_vKZdgHnGpZwunRK-cpaTRrUmuqC1KIEmpNJ35CwkytHEIjZQRPGsvtfq1aMOUr8lR-U0n68BGz1C09Z5OsCXAkY_ImZSiBhsvQN531ShfZ1B0Jj9yNYdVUDcD6-s8hULEkz0KbW7ZplKSEbHu72RW4xwFbGHMlTZvde-67ANcUD3kWEk2pVRIqWBdZvUISH6QtDRJqwXr9y5lDRjMj40GWZjq1MG25WB9t-0fBps5wLyGQnVQu9VuHHcRuh6gh6o39EBHqbXVWLoDJV2AAf3dIFT0tn6ljbeyJI8TYCknff63qywgBhgHr37rGXGYJvVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
در اتفاقی عجیب، امروز تو پلی آف صعود به پرمیرلیگ مملکت مس رفسنجان تو زمین حاضر نشد و صنعت نفت آبادان با پیروزی 3_0 صعود کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/Futball180TV/101592" target="_blank">📅 21:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101591">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jc4NnRrTdlKE-dFRh3pertCs5RBht0tQdoC_-kuvHbcjT3IeRTLqKVbqFTGvjqSLzgWyiFIHUZz3chi933zW7axkClz-gHK5ZqKBFsVXa1JfMPZOvP4VQG5I1nxibA10OPdV6lZaurOytqeyKOd1fCMqK7-0XZR9WEKmemu-8HFgO3A1PHnObAtVu-oc4GUVKMf3FPHHm19p1ilMDOI8cDVo2XU5glD0akrflStpt7P_TC14IOAgmhuGFOLMthJx0iLPgpAv3DP-TnhMHALrZGPlhB6DXURlgp3vbmwm4pyqDhk4HTKPMgINduQtjQeMDGdaSmgO4R72GykHr6WoOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ یه پستی رو گذاشت که توش نوشته : پس از کشته شدن سربازان امریکایی، ترامپ به سنتکام دستور «دروازه جهنم رو باز کنید» و حمله به ایران رو آغاز کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/Futball180TV/101591" target="_blank">📅 20:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101590">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsM1MUvrqwNdYulM0FlDXzRZqX9bKxoedcKJMDuQnZSeqX_uE-kefedSwbn2VX-sqGirI32mEjW7oKHqNHdvJF9DHYDbSnYFLmeyC8brUY2blarmqtldUhAMBTJLsAX2drgNTAcIGjvaRaeiIg2Do76K9EKWrfKUm0o2cOxICk_EKWrBeh5cE3XkD-aWjrKxGA8NuuHS-ZutHO0S0aA4fnlVfgWElwNalxM6JPCSn0kqfimn9kpaRsFtcBE5EIbd7IdHCWpPWGqEtCElgqKMYUuI9RfFIZNGCTx9EaD_LalQa7mzfiiqJVo9pAR26rAKlAfX5MBdAwOyYldQfmHSWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
کنفدراسیون فوتبال آفریقا اعلام کرد که این مسابقات از سال ۲۰۲۷ با حضور ۲۸ تیم برگزار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/Futball180TV/101590" target="_blank">📅 20:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101588">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M7kI006o_Gym61vywfFUzrDVLW0U04dapd3aRlwTtJZrlSzwi8QftqCf1KHMx04x_MG_nCGkR6dHWqO6hCf1dY4CfoDjSdmnwshA0rmYeBE5DDEvgWM9pwHvTVxxaKN4qh0EUUiUysLUWtvO3OcGD25VOoMttJorpLhyWPiyZJeMEWFKkAjS34MVIf_8Sg6WYQpy8XPkd1awdrITt-LxDGgnrgyX9coZqedemRkp0hpsC5gEdCPsKRYGiQm_bnG_aEPBVVdXfTpm1e5k3V0a7vORtWeLcxxkt5Tumd1DcrP6uDQbejrRn7gOjihT60eIGAqOEvNDHcoFoYqbGjpmFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f8v480p-zRu2csLq_Mna6mtHqIX5VL5dH7wzH4wjv3XABvy6ezXNrQANwMI73Rl5crjjYpduEqOiMZolsqxGzkGPrq6bS5rz6klCYk1q1ETspdlHNn25yp4TyMNVo6SH3d0RTpa_4EtyRz_R4aRz3R8wXQaFcxo8WZkW5pjgwtmX78KPv2di3MqZhPzRkiEzFa7kKtHzKTPoVfH2ffG22AX4JbqTXQBn9b1fewr2mh1YKsQLTWTh2teCzLBDpqNOWc2JCA4mNx9TsaN5JrHpN1IoRMC3glqjqtl7msqXLy70ETyplZFFe5OI_iFlAqR48sVaWKtVZdrV2xkiZjiZTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
کاور رسمی نسخه استاندارد FC27
🔺
تریلر بازی فردا 23 جولای منتشر میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/Futball180TV/101588" target="_blank">📅 20:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101586">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxM-VV3CH0A6Cbf1ynzbHx2IG9CPuiTNRJlqHgWFWeNBOVa-VbrbL9zsLcCgux-yyO4gcMwyN2mBt6AU67f9tNpsWa9l72upHL-7vNB1ZTuqH5fmpxXrEGwe2iwn63W8_ZSwxg6FV-NdU9JJhYZ5dEUo8hbjv1EsihbYgXwCNoOHDVeit0Rw87Qpmm9Mdz-YLvGGUxmmKj7u8oM_zzFBPdhUseJHUXZYQUj4m-QXckgaZzk_CX1r_D-yAzibrslE_fEHLz3tHJqVedzgun-exeoSmAvBO_OtDqY2slP4x6jaIx1gek4rAZZ9ooMLAjmZIqBrVIbaa3n7VaAfYJcvng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6db999500.mp4?token=VzbfJshAGBzgjmb5n_WiNS8do9knFCdOBicPmrhc_Utn-Vm-bCmT-rfKcO1Nlpc2gV21d53h6_gMBfZIwj_cqjNsvtV9p_kX6QmBfuORxNwWiQt67gsDCkngFgqd3fidqzGohLHBZkAjx-VS5wwslX6qF1j0jFSI4i51j38Le6M07YwJFr6bj2-QR4aSbGYsOmu3F2MJpKguQSxb3adhKjCr1CjaRtH6qdqQs6LViEfm8KW7pan5S_FR9PTyhfWYdtxac0A30x8YnLl0EqU0ysLYJw7lq_PYnyj0zL_NNh7fnC1iyv8S0_yJ82bFHrGkDIIZkDVcfezydb_rS7vffw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6db999500.mp4?token=VzbfJshAGBzgjmb5n_WiNS8do9knFCdOBicPmrhc_Utn-Vm-bCmT-rfKcO1Nlpc2gV21d53h6_gMBfZIwj_cqjNsvtV9p_kX6QmBfuORxNwWiQt67gsDCkngFgqd3fidqzGohLHBZkAjx-VS5wwslX6qF1j0jFSI4i51j38Le6M07YwJFr6bj2-QR4aSbGYsOmu3F2MJpKguQSxb3adhKjCr1CjaRtH6qdqQs6LViEfm8KW7pan5S_FR9PTyhfWYdtxac0A30x8YnLl0EqU0ysLYJw7lq_PYnyj0zL_NNh7fnC1iyv8S0_yJ82bFHrGkDIIZkDVcfezydb_rS7vffw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📅
🔴
24 سال پیش در چنین‌روزی ریو فردیناند یکی از بهترین مدافعان تاریخ پریمیر لیگ به منچستریونایتد پیوست و با 30 میلیون پوند، گران‌ترین بازیکن تاریخ منچستر یونایتد شد.
🏟️
455 بازی
⛔️
203 بازی بدون گل خورده
✅
🔻
پرمیرلیگ [x6]
🔥
🔻
جام اتحادیه انگلیس [x2]
🚀
🔻
سوپرجام انگلیس [x4]
🔵
🔻
لیگ قهرمانان اروپا [x1]
✔️
🔻
جام باشگاه‌های جهان [x1]
🥇
🔻
عضو تیم منتخب فصل پرمیرلیگ [x6]
🥇
🔻
عضو تیم منتخب فصل فیفا [x1]
🥇
🔻
بازیکن فصل 1997/98 وستهم
🥇
🔻
عضو تالار مشاهیر فوتبال انگلیس
🥇
🔻
عضو تالار مشاهیر پرمیرلیگ
🎙
🔻
مایکل کریک:
به‌طور خلاصه، بهترین مدافع میانی‌ای که تا به حال دیده‌ام.
🎙
🔻
کریستیانو رونالدو:
واسه من افتخار بزرگیه که با یکی از بهترین مدافعان تاریخ همبازی بودم. فوتبال و شخصیت او داخل و خارج از زمین بی نظیر بوده. واقعاً خوش شانس بودم که کنار او بازی کردم نه مقابلش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/Futball180TV/101586" target="_blank">📅 20:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101585">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IettCqTYuu4HaEux2BIcO9iEfYYqHtHkh464g5hrjhD2U1qUUTQ8EvRHB8urB06UQp876V1gc-xmpf1GrD3IFKCUhyBCcr92M0lPXila9soRC118M4QRUwK-3v-LQcaV2A1_OpsJczhkjUGVhIPgqossZo98Br_IZAnKtcuEHnGPd89pXENI1fUA794cusEw-tnL2pnJhrDS9lWQc0ec60jIOZw2TE0b0lvzONxAQ6XO71glIgasaske5in6iU4xrhUuNovci3k2LbHytjPfP7pTCN5GZir1o4Lq0nCuuyRULCztC4NLqPR8tKzzP0jVt-CfxLcWHTbnw4qRBrh-1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کاسمیرو در انتقالی آزاد با قراردادی تا سال 2029 به اینترمیامی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/Futball180TV/101585" target="_blank">📅 19:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101584">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ansNckYq26VBoZCWkYD_9JqqmyOyXpBnAZaW4JmaIoZOYFmOGgcWgDTwQdq-als-LjosutiBQMlN_2TFFp_lurTfInnjuKdvJa3H9yESGlGII_Wx6f3xYbnwptjPeLx9y-Tc-KkWH2u1LNcpLMI4biKAEk83uyxpPRYcEvwyP2jlzg3sPCssjbU0X9KajtJsSzduqtcAWD6zKBkAgRXT6i2K2fzEKsDiE9h9pnMmB2KvY4JM1X5TGfVU9bcBqW01S6GNjDw4WYGbpdupLiUfTHJRyVzyEGCSIkovnuCEPjFdXYdKLOURgPclBIRunck6xpJMgUAy0g-_BhIvoTt4QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از رومانو: گارناچو با عقد قراردادی قرضی راهی استون‌ویلا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/101584" target="_blank">📅 19:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101583">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b963f629b0.mp4?token=fJNwhHhp-UZ-ZF4htG7ieqD0QKYLT-yVh6NdFCmhffjwVJGV1Kp8HPLb3QgU3q0rOce9cAyt9JS28dbXoArYyFmBfZSGkCIwvmSIiGiizpYa_HHBBRo2NNU1jMXShhewS5a1yJM_-lubEK5hhUfK-LYEafNm7V-w1U02iRrqP_zT2fbXX407CTyij58Z_wcUp5KHbLlpB8vbp9_Hhr8Oc2gBNtcUK9BcbaexMWu5gUZwAASd64QLL92OhppwkuVErr1TwhuLgNmvRp5TVzwaqjY1hgqbK8iw01wh3HvRP0VZ-xqnM1iG8F96LE4doe6s3LkBcJkHFhPIX-J-wstyRI1gAjJLyUDEV72P0YFhPFRVeAzldia79kRQaZzTeGknrzpBSyD1A-9exmXCtkPoslypz3bUYNLCblGG34NO3vXMs-R_Yh7CiDSmfkhtZI8UOacllux4ZMvNu13sLmaDaxhUInilmbI-GrwHGeFq8NHmWBnRN-9XwH-VqiC7NmOsfIgPU4_6yxipZzPqa2XknsRbBE7DsAZrUAjf74jNHXXue9XWBTdIVK-M9pyL6z-mjk5V-x-qaq91ONyABaWCVDLPjpXmRqfK39_e8P7zSl-Ps_kPfDvqc-6x94otxHGgrd2Kun55DNVvVX0Ua07H9RrZoiI0pwoqcS9S4iVZz5E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b963f629b0.mp4?token=fJNwhHhp-UZ-ZF4htG7ieqD0QKYLT-yVh6NdFCmhffjwVJGV1Kp8HPLb3QgU3q0rOce9cAyt9JS28dbXoArYyFmBfZSGkCIwvmSIiGiizpYa_HHBBRo2NNU1jMXShhewS5a1yJM_-lubEK5hhUfK-LYEafNm7V-w1U02iRrqP_zT2fbXX407CTyij58Z_wcUp5KHbLlpB8vbp9_Hhr8Oc2gBNtcUK9BcbaexMWu5gUZwAASd64QLL92OhppwkuVErr1TwhuLgNmvRp5TVzwaqjY1hgqbK8iw01wh3HvRP0VZ-xqnM1iG8F96LE4doe6s3LkBcJkHFhPIX-J-wstyRI1gAjJLyUDEV72P0YFhPFRVeAzldia79kRQaZzTeGknrzpBSyD1A-9exmXCtkPoslypz3bUYNLCblGG34NO3vXMs-R_Yh7CiDSmfkhtZI8UOacllux4ZMvNu13sLmaDaxhUInilmbI-GrwHGeFq8NHmWBnRN-9XwH-VqiC7NmOsfIgPU4_6yxipZzPqa2XknsRbBE7DsAZrUAjf74jNHXXue9XWBTdIVK-M9pyL6z-mjk5V-x-qaq91ONyABaWCVDLPjpXmRqfK39_e8P7zSl-Ps_kPfDvqc-6x94otxHGgrd2Kun55DNVvVX0Ua07H9RrZoiI0pwoqcS9S4iVZz5E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
میلاد کرمی: بخاطر چند میلیون پول بیشتر تصمیم گرفتم یه حرکت وحشتناک بزنم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/101583" target="_blank">📅 19:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101582">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5lREVv1eyZKLsiO4n7a03lqoeHCeLDWuMojF-ILCcXGfpVIYyTEsRgDCKTk1vssw8qvlWSJpQX9OnzEGGvDZXCXc9W0ATGMJnSJjpc0zrNQbNJ9gXbmFC-mr0qph9p1NQT7FOBDINyY5Ufh8sVp9c5T2PylQEb7o6aXnmvDfwaMkEz74FkpAZjtNAEZsm7exzsvu6IwjCR07WDVHEY35ilXnYnMMIBWWF5yBG7ZVGMqzgRLSn_jsTrB2zcIHqU_VMRSHT4T9gNh3g-0cz83HrMr9B4n8TL6vGBMFeWB9jR1237MZzBvpgm2wOT5yWFCJdpPkr0cSd9VkJDq2ak1YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏امباپه در این فصل آقای گل لالیگا، چمپیونزلیگ و جام جهانی شد و در نهایت هیچ جامی برنده نشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/101582" target="_blank">📅 19:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101581">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/723401c013.mp4?token=cvNEqpQy-FpBc3bH26FRVGkEYx2z0eywtr_w6R6C99s3Ds0pyd82_mc5k6XhwT-tE0BP-KHjCXUxz3YuWCjJLhJjq3xWwVjAHjvZAMFlyDwWeqXeaJHxa0EqmrEl5XDGElWbvGzkRrRlAmHqN9cx5ARdKV7_D4dlgzFAoqR5yvMMg7bCg76Cgt164FLchXY7Y66v1i1y6mdaCKtBe7S9Z89IX-9rJiwRRqv1aBtzgDf7ayV1OxJuui-lhNkvYm6kVvKZZ80w7G-AuNlF82cr1wKpDAbs5KAYs6MsEaF4R-pW6prRFsiouGbrEMiihusiE3nKfAg4yE2xClhzlMgn3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/723401c013.mp4?token=cvNEqpQy-FpBc3bH26FRVGkEYx2z0eywtr_w6R6C99s3Ds0pyd82_mc5k6XhwT-tE0BP-KHjCXUxz3YuWCjJLhJjq3xWwVjAHjvZAMFlyDwWeqXeaJHxa0EqmrEl5XDGElWbvGzkRrRlAmHqN9cx5ARdKV7_D4dlgzFAoqR5yvMMg7bCg76Cgt164FLchXY7Y66v1i1y6mdaCKtBe7S9Z89IX-9rJiwRRqv1aBtzgDf7ayV1OxJuui-lhNkvYm6kVvKZZ80w7G-AuNlF82cr1wKpDAbs5KAYs6MsEaF4R-pW6prRFsiouGbrEMiihusiE3nKfAg4yE2xClhzlMgn3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
علی‌قلی‌زاده: در عمل جراحی رباطی که داشتم، از یک‌عضو جسد برای پیوند استفاده شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/101581" target="_blank">📅 19:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101580">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KaimaR7Fms5FrYnfwuz7zG-_u4pDdR3j2a8Kk3y0yWAfVgKJVYaYUpmqfSN9XcmiZ40tiecCLwiBljQ3MVijyGwEePILM7oOH4ndI7hcrfifl2CZAat2i_LCuaGDKMNKV1-NNNhV0lqQn_gXA3usSXNmUiqDAP5iZxCNQP7tBwGFL-66nmcCaSclYMHPGyGMYjzUpZaHmI64xP6NmJEDYvqljQfltDBnEfGx5xqUiTrRAJVnLodqhVvvk7UfS0pvPKDKwmbcXJQVU_4vqvTTxpX_nPMQhgvSX2DaxeCUHpblvwb8b3w-Q0OEmQJ52ZbH5nkCXh0yL_4yYuq1FxyJnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
پزشکیان:
دستور ویژه دادم که سایت عادل فردوسی‌پور از فیلتر خارج بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/101580" target="_blank">📅 19:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101579">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfkX-Aq3lPTjJEE0QJpHhE0K5C5YllIfx20sEne0XxBAZegfgZH05cAoh55fGBmAwR50bQfixpjQBan09TIErZaWBB71geRBew6h1lbmrsx6toFEtBUu9mmbVGkXnLnNmEprLjCawFZoLZgJLDUhBpVz7t80aFPn6PzEQNMQMLikzq7dvhlGAyDQ6hxMLy9q9s67IUyZ4aLuRzQOtAp5iOVxydXGyoQRTnnAwVrIv_Tla7kH9P3CN7wO2WzbhkPYdmfeTV0wL3IuJnNjX77KYwh1omSmlBUTzdoMVJTiVWexcRtNFKez-EkoB7hAXtIpC_cmCIN_ognMVbn3rp0FDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاد بولی از زمان اومدنش به چلسی 291 میلیون پوند برای بازیکنای آکادمی منچسترسیتی هزینه کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/101579" target="_blank">📅 19:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101578">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2ZIrEtOyoOmhs6rhwWQUdTMulmZnb5RjjpAmJveWqXQm6sr5Phl2Z7hWxLmLrFybKXNR_vQjSUNr1ZmwlqoZuwH9pWwPWTsw_dWpax6IxiWraOAtbC2GnH-8811FM7nZq2FY3Q2caoj4UqXskF7wUtNQt-kN-Z0j38dIZ4IkLeffcvxXlxIRQB_meM7ZfoLMIG9jdiLdtCBQD-DQ7WTkFFjN8ht-EDCD1h3LttodNUV5d3ieFNLVQnicg0fEHehSriOWi9dPzuwnyWIka_uQePWLvGVNiqcIBr6h4nNF1MXG10QnVSy4HngwPnaV2AbTq_WxZJUGwTkHaUr8UxYnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/101578" target="_blank">📅 19:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101577">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cab44dc23d.mp4?token=J-DPDvgdT5Izj9KBZKT3TREe_dAkR8ZI1O6l_5pQfhHdW1F37zgh3z2eg5JF7RjSeLHbSvDdzhqVdkgiqgEbKa8vxlgAQu2fDTpITF9SDcPoU6i0SugsM9LgxNVVjv39wyYxuetDbI58YUAPmEBeI1ThdvGGVuNa3QaRS5f89W9QzZTv2EyYi4uUSqccZqKIx1Y7ROsztJA_l2a-pMxrGAZAAzwMANKHRZgjRNgAD3Kzt2lKIDeisb0VZU0k9H4ARAHJATD890XjtKGVVLpd9oijVQRnvWjCHSFpKKXJ5NP1qnwGHKJtL1u0yiEXntYNR9-iU3udf3SK1z6uI88Y3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cab44dc23d.mp4?token=J-DPDvgdT5Izj9KBZKT3TREe_dAkR8ZI1O6l_5pQfhHdW1F37zgh3z2eg5JF7RjSeLHbSvDdzhqVdkgiqgEbKa8vxlgAQu2fDTpITF9SDcPoU6i0SugsM9LgxNVVjv39wyYxuetDbI58YUAPmEBeI1ThdvGGVuNa3QaRS5f89W9QzZTv2EyYi4uUSqccZqKIx1Y7ROsztJA_l2a-pMxrGAZAAzwMANKHRZgjRNgAD3Kzt2lKIDeisb0VZU0k9H4ARAHJATD890XjtKGVVLpd9oijVQRnvWjCHSFpKKXJ5NP1qnwGHKJtL1u0yiEXntYNR9-iU3udf3SK1z6uI88Y3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
دیس سیدجلال‌حسینی به محمدحسین میثاقی و عادل فردوسی‌پور: یادشون رفته از کیروش حمایت می‌کردند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/101577" target="_blank">📅 19:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101576">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0c61d3ee9.mp4?token=OEvXiN5cl5euQCq1mRVMCTHal4ydAywkheg6Hg3-yaLABoPMTM3JtAaTSJtBQJ7spEAlhsDSTtD-c5osUPipxFll4knQ1RmRTvuqocLvNtqgDzpscQESIeOsEzOAV-YD4u57LfCDs5Qrba3j-gqGlTccR3LV-ZPplW6dHOPc9XMvg0mJbvP06oUEpxLXrEKL7eHwiQzuIP4Muck9R07vQRXDyDjnVCZKIs085eWBeJxL8Naf-K39YqMGRkQNmfjffZfXTyPfmj4zAHCuURoFBK5_21b9J2CyfeMZj9ERF7yll1pWEoMk2JLgsINzhoKD5meVlZo_6psyD_Co3LH0AA-ZB5AYnLzaH7rt1KrHn-miuUxIJaMSZ0We486JqdK21ZOEtFa2IC9SfrBqCILbIYIAX0RRlNnNFDUmESnu4AtRCpunLQ1NIBejfrkxPvt4jj-epEAacyCOQP3oF1Wj4ZXZaSaacfjtkhOaSr9mp7CLfOsc5OZde_oy5W4jdnrD5GDahUuAJuGkimmyYlkcTtouKtaHbyZ6Fr8t2yxZRU1PgF95zPsKia3ZrxbTlqn8pEUxoo82wITMpuM33t0oO4jHxqeRJ9w2pBRHRUVKY_pYFp5p-7pNo4cpRGY_QVtsQFmPIJnJ-kel7xPm9EJ9lizzdrDrsYw4Y9OImb4ZZzM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0c61d3ee9.mp4?token=OEvXiN5cl5euQCq1mRVMCTHal4ydAywkheg6Hg3-yaLABoPMTM3JtAaTSJtBQJ7spEAlhsDSTtD-c5osUPipxFll4knQ1RmRTvuqocLvNtqgDzpscQESIeOsEzOAV-YD4u57LfCDs5Qrba3j-gqGlTccR3LV-ZPplW6dHOPc9XMvg0mJbvP06oUEpxLXrEKL7eHwiQzuIP4Muck9R07vQRXDyDjnVCZKIs085eWBeJxL8Naf-K39YqMGRkQNmfjffZfXTyPfmj4zAHCuURoFBK5_21b9J2CyfeMZj9ERF7yll1pWEoMk2JLgsINzhoKD5meVlZo_6psyD_Co3LH0AA-ZB5AYnLzaH7rt1KrHn-miuUxIJaMSZ0We486JqdK21ZOEtFa2IC9SfrBqCILbIYIAX0RRlNnNFDUmESnu4AtRCpunLQ1NIBejfrkxPvt4jj-epEAacyCOQP3oF1Wj4ZXZaSaacfjtkhOaSr9mp7CLfOsc5OZde_oy5W4jdnrD5GDahUuAJuGkimmyYlkcTtouKtaHbyZ6Fr8t2yxZRU1PgF95zPsKia3ZrxbTlqn8pEUxoo82wITMpuM33t0oO4jHxqeRJ9w2pBRHRUVKY_pYFp5p-7pNo4cpRGY_QVtsQFmPIJnJ-kel7xPm9EJ9lizzdrDrsYw4Y9OImb4ZZzM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
قدرت شوت‌زنی اسطوره‌رونالدو که اگر‌توپ گل نمیشد قطعا بازیکن مصدوم میشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/101576" target="_blank">📅 18:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101575">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/641d875577.mp4?token=Y1B8W4gDKf28M8qOVZzvEdzoiLBSpMuADiZ4yDb3Y3bn2921gkvcAdKMsa2OV0yKvDMMinBubj7hIKPUM7c761yZJlEBIPewbgUbUFqMat-DzmpAfBfEezievu6nqT_KxI3jHhGgKFhX-R2pqP4ea7_cSOkJeP7bHeYkTk7PE_0FwHI5ht_uASYH4C24awpl1oHLPLDQPtcWIQNKasTFxcKIcFl24IPSV-cpWvdkoOZk6myJiq1haYkB7aPR7ggAbfJ3HW5RfUmh9fxZNuHewnl1zE6ebIdGmEeeUyZQqrNgsPiKpowbEwd6qoFOfoLDS-SjwcuzWh-gNUW7mBlTTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/641d875577.mp4?token=Y1B8W4gDKf28M8qOVZzvEdzoiLBSpMuADiZ4yDb3Y3bn2921gkvcAdKMsa2OV0yKvDMMinBubj7hIKPUM7c761yZJlEBIPewbgUbUFqMat-DzmpAfBfEezievu6nqT_KxI3jHhGgKFhX-R2pqP4ea7_cSOkJeP7bHeYkTk7PE_0FwHI5ht_uASYH4C24awpl1oHLPLDQPtcWIQNKasTFxcKIcFl24IPSV-cpWvdkoOZk6myJiq1haYkB7aPR7ggAbfJ3HW5RfUmh9fxZNuHewnl1zE6ebIdGmEeeUyZQqrNgsPiKpowbEwd6qoFOfoLDS-SjwcuzWh-gNUW7mBlTTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🎙
علی‌ قلی‌زاده‌: کل خانواده‌ام استقلالیه ولی من عاشق پرسپولیسم؛ خیلی دوست دارم در پرسپولیس بازی کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/101575" target="_blank">📅 18:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101574">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdff7389ce.mp4?token=fQMUS9iQYTINA2slQ334sJ87KSuGv-ITmHMd2gyxtYRYMGsBIC83Ma7sltg-5m-RNyKk4QpY4HOvTfxtYL5Fr8bluxgQV2_MQTeoKjzzQxwQjwfR8unP7hTJLBnnDnToTuuZpNMoRDGPMDEZom9Wuc81hkFOxEUTUeoHIwIatoHXwIH5NkZmrL3XHnu97SEfQe7xZBCY7aGZ8MUsxbsobk7wJpibpjRhGh2s0uU4FQ9KMEE5sU3B1WseOtSCztUTVVmWhDEmsf-Sz-Iw7BjaUYIlTLhpFM5giHidAdwWEtNGfnjOmcqIFOzt0FC7WJ9quZSuQNcGE8W6Yz5IP5z9Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdff7389ce.mp4?token=fQMUS9iQYTINA2slQ334sJ87KSuGv-ITmHMd2gyxtYRYMGsBIC83Ma7sltg-5m-RNyKk4QpY4HOvTfxtYL5Fr8bluxgQV2_MQTeoKjzzQxwQjwfR8unP7hTJLBnnDnToTuuZpNMoRDGPMDEZom9Wuc81hkFOxEUTUeoHIwIatoHXwIH5NkZmrL3XHnu97SEfQe7xZBCY7aGZ8MUsxbsobk7wJpibpjRhGh2s0uU4FQ9KMEE5sU3B1WseOtSCztUTVVmWhDEmsf-Sz-Iw7BjaUYIlTLhpFM5giHidAdwWEtNGfnjOmcqIFOzt0FC7WJ9quZSuQNcGE8W6Yz5IP5z9Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🎙
جواب عادل فردوسی‌پور به حرف‌های اخیر قلعه‌نویی: بودجه یک‌فصل تولید برنامه من از پاداش سرمربی تیم‌ملی قطعا کمتره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/101574" target="_blank">📅 18:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101573">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDSXiHCNHselNAe_1cGEMrGF8dkPfQF43M-Y4I-K09iJwGvnxNCP-i8qjwIyBypUBaHZdYvRZ0U7pSq42jxRj6UElaSV_p4KBReY202hOOyqiD-fZO1S5A4-2cW-9veyvXX0Dlls_yxd1eJYJ100g1aHzwa00UdYF_uMhOX_7EE9AHFK42oAiTs2hdKA_tFTcC5Fpm9oH8d9UBCPxez9E6bk5Hn_DuefYk6a_ZJRmeh_KlptfmywUJ8TlL0bQqICJPzZTj2nSo3tCDDJlKa0Svbk-1qLoEjxjV0Sxoj6_-5oNgL8f4FfrVSGb9B4AAzA3FPVfNMDW1i497kQmOyADg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
👀
فدراسیون بین‌المللی تاریخ و آمار فوتبال (IFFHS) به صورت رسمی لئو مسی را به عنوان بهترین بازیکن جام جهانی ۲۰۲۶ معرفی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/101573" target="_blank">📅 18:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101572">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f420d24855.mp4?token=X-hGiuHc3Vqswcp6eZlN_8PHl82nGryOzNGTcrwvapwzewXU87PubKY8F9oeFS3UGpgAzm5niLZQXk7-8xPsMvzN8Pq0pJnOOArY5yRDxXZCM21rFz0kCosSgr7ll79tMbTaGrtey6_XoewKB8nbANQXDyMZpiuaCb59mKM8nbd4JOKUGJOB0U2Kn2rLi-RotzmgI2PGYIlQWY9ZCWImHTeGa8G7LRo91iVk-GgJOcMmwaxh4t19zs9YtlI1zZ4bZU127sJmLNIQV3YqjTdoY7gLq1W1HXZL_ZdQgquedh6F5EnBLkbn0XBLUDqn9FBG7wxod1vPJHTupJ1fL_dWYykoPluOTkMZ8w4_Ui75Ln3aRYUMkZHabebwuK5vIcYv_s3KWX_4v2m1hvLYExtot8PafBm37exqNcHPpqukK28jdwYe4_2RhJu70wPpUCGNhki1KxvzkqQnpHeySFVX-XMn_5fuVpkX5iC3MtlMZnM01imBx5TPc-xq43sNFaCnIeGYBIazHR5lgkP-W1XnDJ-faWEH0fT9hiKPEacecHNMfhRWFD-_5ChfEIi3tg303nio7JARx373F_pofMzAgU_aHtVd-kYSVQZ6VcQX12j0536bsjrBOedD_BtFIpfkoI-fLFB7eBA5J7pTYsa8EEA2QN0oX0R18pb81Zc6oYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f420d24855.mp4?token=X-hGiuHc3Vqswcp6eZlN_8PHl82nGryOzNGTcrwvapwzewXU87PubKY8F9oeFS3UGpgAzm5niLZQXk7-8xPsMvzN8Pq0pJnOOArY5yRDxXZCM21rFz0kCosSgr7ll79tMbTaGrtey6_XoewKB8nbANQXDyMZpiuaCb59mKM8nbd4JOKUGJOB0U2Kn2rLi-RotzmgI2PGYIlQWY9ZCWImHTeGa8G7LRo91iVk-GgJOcMmwaxh4t19zs9YtlI1zZ4bZU127sJmLNIQV3YqjTdoY7gLq1W1HXZL_ZdQgquedh6F5EnBLkbn0XBLUDqn9FBG7wxod1vPJHTupJ1fL_dWYykoPluOTkMZ8w4_Ui75Ln3aRYUMkZHabebwuK5vIcYv_s3KWX_4v2m1hvLYExtot8PafBm37exqNcHPpqukK28jdwYe4_2RhJu70wPpUCGNhki1KxvzkqQnpHeySFVX-XMn_5fuVpkX5iC3MtlMZnM01imBx5TPc-xq43sNFaCnIeGYBIazHR5lgkP-W1XnDJ-faWEH0fT9hiKPEacecHNMfhRWFD-_5ChfEIi3tg303nio7JARx373F_pofMzAgU_aHtVd-kYSVQZ6VcQX12j0536bsjrBOedD_BtFIpfkoI-fLFB7eBA5J7pTYsa8EEA2QN0oX0R18pb81Zc6oYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
وقتی صحبت از کارما میشه منظور چیه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/101572" target="_blank">📅 18:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101571">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CY_sKteO_GIJdb0JsDS759bK9ve-acZH1oy-GGW2YHjDqRE-NlXo0jBGyHJjupSvrX1HD2Z3StgL3o87M2WEB6EA5wB2yhnWLQP26eSWDON1jGJr5PvFlHyoDBpclAwVd8VbrjaSxRYBkB1v0iQT9HJhvwRKcaiSJk6TPQvwOn9YXsgdIb6hZ1ltToODOrlg6cbVIqGo6qdxyloGOqqVdQmlqgnsD5hXIYRUlUjYiSlqYY1ICBsvJW6E-fifXxEz0PS9D25jRNSWa8m71mHmsGwtwrjix5B3GYKQR9rFw2FMBJ9ofgPt9MINqfnDSWUJrP0HrbvK1vwKYeOEer1ynQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیورپول و آرسنال درحال رقابت شدید برای جذب بردلی‌بارکولا هستند. حداقل رقم پیشنهادی به پاری‌سن‌ژرمن حدود ۱۰۰ میلیون یورو تخمین زده شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/101571" target="_blank">📅 17:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101570">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb17487185.mp4?token=R7lIVu1DCdJX5iKG7lxCqQOmLkSGscLyFvlfmJl_qhCGDIYblIgcGZ5HylB6Efmilw4gtxe0Nz-8wJP-Km5N6XTdTdokbygHekcjV_g015ikI4EVRt2IMKbE_8Or_0hEDgERJehe_SpqQYmL_CNTHANdX8OC1oo8vGo5RXO_fAcPSwyIflPFPgwAlGr7j-xJn6mDK-WBxfPx7eOmBGdk2wH8zfQ_p0UfmjHyhEc57DhAqm5sq8zcCsZeXbUXVhU8RfAwAtyhHZfimy4RxhYIFhKYheXGJiYcr6jA3MbkTfUlCPn3Q3Xs8EgmhNubUBVUKFMOJiuQfjLrl6VwoiJG0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb17487185.mp4?token=R7lIVu1DCdJX5iKG7lxCqQOmLkSGscLyFvlfmJl_qhCGDIYblIgcGZ5HylB6Efmilw4gtxe0Nz-8wJP-Km5N6XTdTdokbygHekcjV_g015ikI4EVRt2IMKbE_8Or_0hEDgERJehe_SpqQYmL_CNTHANdX8OC1oo8vGo5RXO_fAcPSwyIflPFPgwAlGr7j-xJn6mDK-WBxfPx7eOmBGdk2wH8zfQ_p0UfmjHyhEc57DhAqm5sq8zcCsZeXbUXVhU8RfAwAtyhHZfimy4RxhYIFhKYheXGJiYcr6jA3MbkTfUlCPn3Q3Xs8EgmhNubUBVUKFMOJiuQfjLrl6VwoiJG0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرصت‌سوزهای اسطوره فران‌تورس ستاره فعلی اسپانیا در فصل گذشته برای بارسلونا
😂
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/101570" target="_blank">📅 17:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101569">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ea79a8c03.mp4?token=Xf1riJsJfvHyrseNjwAa4crzaUTelNts0oTOXQE5qgIBxp4pw7fLe2uzr39-6w3wFRNaJuixUDVywdWIQk9Ixr913UaqXkbnvQVWn_fNyN7qNJtHFjEnq3ebuoQ0C0S6oiNiP4jU9vrBzkT0YsIkTVSxUqyAJoEnGbPdqx3R8RMNJgcW3WAHihThnc0RSaHQrgKsRhRXHy_nK7BP0_LcLC87DHlexp4bKfi4X4JfPmbkXufaBZ0HK87bBvMQSO070nAYttNwnBKipASSF49OoyYf85s2eYagKdEzFRSH5BQCQGfjMhBzHZdXJ1mnC_HO2DqZldaDNhbk8neIArtluQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ea79a8c03.mp4?token=Xf1riJsJfvHyrseNjwAa4crzaUTelNts0oTOXQE5qgIBxp4pw7fLe2uzr39-6w3wFRNaJuixUDVywdWIQk9Ixr913UaqXkbnvQVWn_fNyN7qNJtHFjEnq3ebuoQ0C0S6oiNiP4jU9vrBzkT0YsIkTVSxUqyAJoEnGbPdqx3R8RMNJgcW3WAHihThnc0RSaHQrgKsRhRXHy_nK7BP0_LcLC87DHlexp4bKfi4X4JfPmbkXufaBZ0HK87bBvMQSO070nAYttNwnBKipASSF49OoyYf85s2eYagKdEzFRSH5BQCQGfjMhBzHZdXJ1mnC_HO2DqZldaDNhbk8neIArtluQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
دسته‌گل استاد فران‌تورس در حین حمل مینی کاپ اهدایی جام‌جهانی از سوی فیفا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/101569" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101568">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8X3oPuD-JOi123iFE_6WNOZXhZ96ccVtDHUTk44_7j4S6g6OOBLevbhR4pWcydCqTIuhP3G1vjxKWLoMDdFZJe_xAlZPaTkf0nC7p3s6eatDoC9tthBY-8C0fzNgys0B7NSpNNBrSeviwQUqoBw2Tl5rYCyQgoZVWfH9w5XrG83ItZ7-le7EpkBQmnK2diFopB-iB5pikw1KYt_Di6dfl7pOhg-Op9EoCecagOAYCVL8ACWhbKSAPgaa6gN6xKGqEwLeQpD0D-ZANil3y2v2Mh9w4le_BUqax7gRi_AWC5IU7FN-sb1YGX_ePxrpPAdS0FjHN5PKAsRBORmKKrDoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
ترکیب منتخب جام‌جهانی از نگاه فیفا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/101568" target="_blank">📅 17:08 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101567">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e38a17a2eb.mp4?token=ERAvo72M2FE8nbTErnDw28NMc6cu1I0UNF1EeJqSVxTXxoLLufYzWmYmAeoAdfqH1wmBgzlpiIUeL5QoOnLZn2ttbHx-l52QJfjhaGpwe2wm_8J30Zi7O3xTFGLeVw_oCLpZZAOwLpunnYY0tNC374Y7azugcEEdMWhNj5VwYyaxsMTFcOJp5XX-Amn6md1bbeRED036dNHreerzo7om05y21x0EqrLsVw-G9v8yJbyHhIDMwaFDbHdZ7FdBbEwgmz-KuA4S7XhBCBqsP7aIhKo3BBav6TpYRTHHh1OBsidkBF2RwpYYIvUyCbM7jW_HYBTK9h2NmJ5lHmtBy3bqUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e38a17a2eb.mp4?token=ERAvo72M2FE8nbTErnDw28NMc6cu1I0UNF1EeJqSVxTXxoLLufYzWmYmAeoAdfqH1wmBgzlpiIUeL5QoOnLZn2ttbHx-l52QJfjhaGpwe2wm_8J30Zi7O3xTFGLeVw_oCLpZZAOwLpunnYY0tNC374Y7azugcEEdMWhNj5VwYyaxsMTFcOJp5XX-Amn6md1bbeRED036dNHreerzo7om05y21x0EqrLsVw-G9v8yJbyHhIDMwaFDbHdZ7FdBbEwgmz-KuA4S7XhBCBqsP7aIhKo3BBav6TpYRTHHh1OBsidkBF2RwpYYIvUyCbM7jW_HYBTK9h2NmJ5lHmtBy3bqUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
✔️
پیش‌بینی پپ در مورد شرایط رودری در مهر ماه ۱۴۰۴ که در ۲۸ تیر ۱۴۰۵ به حقیقت پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/101567" target="_blank">📅 17:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101566">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be9c5de5c5.mp4?token=c_7EnTaFyMi3n8iqdYvBQcHSfxK7s84JTeGODL9szAqyv5DFZrIqK9h6npdOoOXoiDepXXPc-LfNzuoFsDT67N1HNAIOg9THN9apOH9YLbPIaTAKkPlabI0N5_FSLOVjk0wQdFDwJtAgJAGaet3O5O3zZ7wlTcV8Vempi_UohEhubZuur1GwVEkA1_TMpsqSsIt_aWDnSpi2gzTibumZ3ZbCyVQxMVzhEY5x11zAfY3UHTfcAp2cDFc05O4RNoN9e8MrfHKyiVWKDrPK_z5t_xWM0ao_86silveRyUOaFC1iE-dy5WtkGTV8P02NAMC3X1mK-sNbLNMI68PGp_B8C7s_Xxa4in1b4whwUmD0I-TGIdj3LN4lssZ70edPCHGY_PGhhL-0JBXiz8dGPWXkHbLuCSz7Aeq3zI0SBXPKFjGgOevsi8Yi-74w38sW958YvUhdovCZUcqhaZDbsq8uZhbAUklHT9IWoLdyTGncd9E03huL-3EoOuyQGandJ3lXtlWjrhD0sholrWn1F5r__R8bx1gkjjnV0S85zPmeSbYm3yTX2zWQhaBY9qC2jsEq-UK5W2W8CRSr5ZTMBUEElpMDBMOhjQzDYE4GGauAaveotcc96wELPsA2AlcWz4I2MDO5VCu7I8jdXC6p7LK62meCyENuw0dPhhYPGNRJJtM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be9c5de5c5.mp4?token=c_7EnTaFyMi3n8iqdYvBQcHSfxK7s84JTeGODL9szAqyv5DFZrIqK9h6npdOoOXoiDepXXPc-LfNzuoFsDT67N1HNAIOg9THN9apOH9YLbPIaTAKkPlabI0N5_FSLOVjk0wQdFDwJtAgJAGaet3O5O3zZ7wlTcV8Vempi_UohEhubZuur1GwVEkA1_TMpsqSsIt_aWDnSpi2gzTibumZ3ZbCyVQxMVzhEY5x11zAfY3UHTfcAp2cDFc05O4RNoN9e8MrfHKyiVWKDrPK_z5t_xWM0ao_86silveRyUOaFC1iE-dy5WtkGTV8P02NAMC3X1mK-sNbLNMI68PGp_B8C7s_Xxa4in1b4whwUmD0I-TGIdj3LN4lssZ70edPCHGY_PGhhL-0JBXiz8dGPWXkHbLuCSz7Aeq3zI0SBXPKFjGgOevsi8Yi-74w38sW958YvUhdovCZUcqhaZDbsq8uZhbAUklHT9IWoLdyTGncd9E03huL-3EoOuyQGandJ3lXtlWjrhD0sholrWn1F5r__R8bx1gkjjnV0S85zPmeSbYm3yTX2zWQhaBY9qC2jsEq-UK5W2W8CRSr5ZTMBUEElpMDBMOhjQzDYE4GGauAaveotcc96wELPsA2AlcWz4I2MDO5VCu7I8jdXC6p7LK62meCyENuw0dPhhYPGNRJJtM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمود شهریاری چه اجرایی کرد
😂
😂
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/101566" target="_blank">📅 16:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101565">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESoAeKjKSMzxA8p1LJLTrc6megQaia5rKxjojBTYBeFA-nju1Slsn6zagVf1fiqEFpqIf7weZue04nmTiA-ElHem7hYdCshjZAFsRnwqMSWqk2HVUedtHuXbtETb3Ehl1J3H9X63TW9dLED30Jxa7XwUYdG-w4pzU8aGYLLQrNLgghvjd3d3Avdi7wzW2RnBb2X-XCqLeVPo1vgXbDdJQ1TXvGTrlRSW2wjldAQ6IbPASUPpqoBhdWyyvMGxq0D7E3n_fhGCz1_42ZekuaLgJVDk5Tjq9RFZ3ZGMq_YuICt1q-dIsdVqvqGJmYLQ_tFiN90yaUY7MO6cXVejutRIBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ: از این به بعد، هر زمان که جمهوری اسلامی ایران در تنگه هرمز به یک کشتی شلیک کند، چه با موشک، چه با پهپاد یا هر وسیله یا سلاح دیگری، ایالات متحده یک پل یا نیروگاه را بمباران و نابود خواهد کرد، از جمله آن‌هایی که در کنار یا در شهر پایتخت تهران قرار دارند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/101565" target="_blank">📅 16:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101564">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🎙
🚨
حمایت جالب رضا‌رشیدپور از فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/101564" target="_blank">📅 16:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101563">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/318ac55e88.mp4?token=CN699ZVLOYaw6Vgp1wvuvMUgSVkct-uH37kw2_gpkBtVj840Qr_EJn3VNbts59iVGHcU1ohlpAsSFI--S6ijhFX_qzGasEgFxRBS-1Iv9Y1vleAmDh2NCI1PyUwQmf7ZIcohbdPk36INqETRaio-gR7DMM4MLrCcd4_YCi758NBpkVUmPA7YIAo7ongKRz7tD7yLiI0iKh6WwvTsfQfSFaXkupj6fqpXmUEqANpFZzEZEp-I4wxIM99hxlbjbndz6HjxWsnee5SSK3zShmljaul4ckyRhI4ryC8ueW1CaMEPT1Bux2QXT0l3wzATmpHu7Zc28x623sFAP7Gz_S6uGKzymD4Sbo63dcFp4cc0O7xMXVljth6tjBos1Z1cHm1XEwcinTkU5EUTSdLtict-NVfKZ-teI9UUVw8gAXs6rnRddP2xoknh16_UcEHJankNzPwKemLTn-vP1zsZ0uR00dGyCrr7WfUWOk8dLvx6PfFa7L9NqpOsqnCGwBTPxQqokMGEf3iVWVgsmOiJKXdtr3yCbRFmYMOPHgMmYvs9qLLmpJEphvUhFZ--n-Y9UMCqY-N6NRFqkTzuLD_FKS-7BpQqAmF8laL-7uDT7SytSRz9aXfgeigkP08k5fRhvE-6yDTGMbHW7N82_HTlBsyw9FMy6Gpf2vAV4VfC3oDbgNE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/318ac55e88.mp4?token=CN699ZVLOYaw6Vgp1wvuvMUgSVkct-uH37kw2_gpkBtVj840Qr_EJn3VNbts59iVGHcU1ohlpAsSFI--S6ijhFX_qzGasEgFxRBS-1Iv9Y1vleAmDh2NCI1PyUwQmf7ZIcohbdPk36INqETRaio-gR7DMM4MLrCcd4_YCi758NBpkVUmPA7YIAo7ongKRz7tD7yLiI0iKh6WwvTsfQfSFaXkupj6fqpXmUEqANpFZzEZEp-I4wxIM99hxlbjbndz6HjxWsnee5SSK3zShmljaul4ckyRhI4ryC8ueW1CaMEPT1Bux2QXT0l3wzATmpHu7Zc28x623sFAP7Gz_S6uGKzymD4Sbo63dcFp4cc0O7xMXVljth6tjBos1Z1cHm1XEwcinTkU5EUTSdLtict-NVfKZ-teI9UUVw8gAXs6rnRddP2xoknh16_UcEHJankNzPwKemLTn-vP1zsZ0uR00dGyCrr7WfUWOk8dLvx6PfFa7L9NqpOsqnCGwBTPxQqokMGEf3iVWVgsmOiJKXdtr3yCbRFmYMOPHgMmYvs9qLLmpJEphvUhFZ--n-Y9UMCqY-N6NRFqkTzuLD_FKS-7BpQqAmF8laL-7uDT7SytSRz9aXfgeigkP08k5fRhvE-6yDTGMbHW7N82_HTlBsyw9FMy6Gpf2vAV4VfC3oDbgNE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
آنالیز بازی پائو کوبارسی ستاره تیم‌ملی اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/101563" target="_blank">📅 16:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101562">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‼️
🎙
کنایه علی علیپور به علیرضا بیرانوند به خودم اجازه نمی دهم درباره علی دایی و کریم باقری حرف بزنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/101562" target="_blank">📅 16:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101561">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🏆
🇪🇸
رسانه‌های اسپانیایی با وجود قهرمانی صحنه‌ها مشکوک داوری فینال رو منتشر کردند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/101561" target="_blank">📅 15:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101560">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4bPC8xxw_EulqoYaNzBvIVyExtZ8nkkurUhCK3SvGbJh4btwrl2oVdWEkyaPmpxXOAPcERKvIGc77iI57Rkc1lHatDPQOtXJl6UijhN9EzJ5tgcKZkjkmr1X3UUAewC1NoGyl03wJ7VPca__HGSUkYRQKKWsmCEcgSm7Rhx-XX3FeBkDql2o_O27De9zVg4SJlPXOOk3dIXChQtlvar1NoLwMVb-_EHgG1-Uv2zFANlvNbKhtuWAIfns8fNwz3xcuXRYwa1vcFOFewmHbki7KlNlVoOowKHiIgVgHDd1uGXcsuu7Z_WDVfFGJXpGnTiLTgYZk3a8kwXeYx5XWQOeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
منچسترسیتی قرارداد فیل فودن را تا سال 2030 تمدید کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/101560" target="_blank">📅 15:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101559">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e21d92126a.mp4?token=fPQw-Jszb7tiDR9yBi1W9iJml1jVfeggwuJzfjyLPYv76IdfwOG82rVKpiA9M8iTWR5gx1HmXZNTrs6s0UWa49VfsP_5JVmz4Ku5BEgFmJ4o0rdYL67OUw_eTE7TySFFyLE75zeST-V5E5LeH-x-X4g1wmuAMBTikKiSc3Oa36b3L_-R-g3MgcIOHXJbOPQhc-yHYoVCjRrSP6S1bAvhl1x8USkKS7OZ9_DBJ2XIIu0XK_MMYV3j3WH3LQjrlIo90erpWuTLtc1F9xAzwB3zGJMGIH_2fAnVR7iijIY3nNRbLff1td_kxqfyOeMP1hj9l-n_YT0WqF579z2QiLuMm7M0mqyN-Z0A8gat8V7iWXVVYDZa76d9gkht9XsKabZwump1Cg1m_HbOYylwkNiAjNCwRHlDE0E8x7KOtOpAf_kTCIPKTL0QJd9lnIpnA0baOdwudt52BsPfrRuj98WYq9QtSW2cIXh3XmkrBegm075etE_zb94ZXUSriu49sTjzQK7jAxCcE9MR38QhSrHea5Fvh7ZjC0NfvfMZrIXcf6aVTV603mGldWOsPY2sjT_zwH6ldjb_YSVKsPQsPNlZhNGyuGgwkI3QDNYSzIgK1mFoNwSSjLMAutnzpnptKHAjLOW2qJz7XZSdLA_Es9WCXmDqVGlDLqo74WFVCqcBXjE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e21d92126a.mp4?token=fPQw-Jszb7tiDR9yBi1W9iJml1jVfeggwuJzfjyLPYv76IdfwOG82rVKpiA9M8iTWR5gx1HmXZNTrs6s0UWa49VfsP_5JVmz4Ku5BEgFmJ4o0rdYL67OUw_eTE7TySFFyLE75zeST-V5E5LeH-x-X4g1wmuAMBTikKiSc3Oa36b3L_-R-g3MgcIOHXJbOPQhc-yHYoVCjRrSP6S1bAvhl1x8USkKS7OZ9_DBJ2XIIu0XK_MMYV3j3WH3LQjrlIo90erpWuTLtc1F9xAzwB3zGJMGIH_2fAnVR7iijIY3nNRbLff1td_kxqfyOeMP1hj9l-n_YT0WqF579z2QiLuMm7M0mqyN-Z0A8gat8V7iWXVVYDZa76d9gkht9XsKabZwump1Cg1m_HbOYylwkNiAjNCwRHlDE0E8x7KOtOpAf_kTCIPKTL0QJd9lnIpnA0baOdwudt52BsPfrRuj98WYq9QtSW2cIXh3XmkrBegm075etE_zb94ZXUSriu49sTjzQK7jAxCcE9MR38QhSrHea5Fvh7ZjC0NfvfMZrIXcf6aVTV603mGldWOsPY2sjT_zwH6ldjb_YSVKsPQsPNlZhNGyuGgwkI3QDNYSzIgK1mFoNwSSjLMAutnzpnptKHAjLOW2qJz7XZSdLA_Es9WCXmDqVGlDLqo74WFVCqcBXjE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇦🇷
رفتار عجیب بازیکنان آرژانتین در صحنه اخراج انزو فرناندز که وایرال شده !
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101559" target="_blank">📅 15:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101558">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f9401eccd.mp4?token=IbJJh_sVoHTpIdBZ5stoh1AKn5akqmQL4oXVVJks0X347c3_684ZPBjtTPcgA8UAcASIW1iBGCm2whAWaocsuz6X261cnwOdbmjHOSB0tJIkmQX5RwNnV6vVLFBiW3iJ_Q88Xe39Zukhv4ifMsiJhy2-ODOtt1owGV25G0Q1f2FohgWH-9yITRPIcm5xyZigC6Q6C3DQEm1ThAanyEuRvirZBequ2wU6QpHnQNvCWV2aGCFvDghMpmu2e2COQyhsrT4fKQGx5ma55bnGK0M1rxQYWefQiRsdtcTjKai5xCJJAtL7oqd-yWAYaKjFTyFYqykS71dRuhHe75V3X36yvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f9401eccd.mp4?token=IbJJh_sVoHTpIdBZ5stoh1AKn5akqmQL4oXVVJks0X347c3_684ZPBjtTPcgA8UAcASIW1iBGCm2whAWaocsuz6X261cnwOdbmjHOSB0tJIkmQX5RwNnV6vVLFBiW3iJ_Q88Xe39Zukhv4ifMsiJhy2-ODOtt1owGV25G0Q1f2FohgWH-9yITRPIcm5xyZigC6Q6C3DQEm1ThAanyEuRvirZBequ2wU6QpHnQNvCWV2aGCFvDghMpmu2e2COQyhsrT4fKQGx5ma55bnGK0M1rxQYWefQiRsdtcTjKai5xCJJAtL7oqd-yWAYaKjFTyFYqykS71dRuhHe75V3X36yvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
علیرضا نیکبخت جواب بیرانوند رو به زیباترین شکل ممکن داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/101558" target="_blank">📅 15:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101557">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHs_UZZdbzFIOF6hL4mY96v-H21k7eLU-iXfCtfhefeyXDES9U2lwdOjhfmuRajK3syx8LKG6kTwp8xPpI6PRG5HiSxIpE_JkTzN_eyskb-XoL1tRhUYGFljW_Zk0_Bs1x58O4cemHqYgF1mhlzLtOpdj4cg6SQVpx4fSFPUNiI1LDX9WY1jn1CwTL1PHgHaRzGhMQPcmq-UBcZ9-KnM6b0KnSGtXTZkdkT7Glnhe9qSWZr5valcenBEgzBq78NzBGG7alkZxIjo_BOTqZk5gFn-l5KFXO008v88V5U26nkE0nyNXrXyYu_oIMopEm3izBdA_0g5OZTKFE3Cc3Untg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
بازیکنانی که در این فصل، در بین پنج لیگ برتر اروپا، در تمام مسابقات بیشترین گل و پاس گل رو دادن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/101557" target="_blank">📅 14:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101556">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a761e81f7f.mp4?token=M7HTVAp4Rj9R-8LVwm5gQs28YcetI4JxhxhfZ19zqnxutc_Zjy8oZflROtmQFTnFDVX9nlWIvSlekYryy820GOKoPpaKJ5OHEUcRPyWy6Dn49F3mgJeHiY00MzqWgBBeHp6wCnUgEk2hqKB8T88v0I-tLmSC33g2Baj4tmhmE3LTAuQWDdt_8a-ZAOSGPPEIUdEJ85Kn00IP3EU44gkbOl5qmff84DV6u5kGKSvAyYpwyRZusF_ZaNDiOTmPE8RgAyCDUVZu2ZYR2fUBj2-xcwMX7DH0L5RwvJmmxlmhH5i_MCMxP0xj9jgK2zC_iBqqGPtZMVR0M88ISRjEM5ihjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a761e81f7f.mp4?token=M7HTVAp4Rj9R-8LVwm5gQs28YcetI4JxhxhfZ19zqnxutc_Zjy8oZflROtmQFTnFDVX9nlWIvSlekYryy820GOKoPpaKJ5OHEUcRPyWy6Dn49F3mgJeHiY00MzqWgBBeHp6wCnUgEk2hqKB8T88v0I-tLmSC33g2Baj4tmhmE3LTAuQWDdt_8a-ZAOSGPPEIUdEJ85Kn00IP3EU44gkbOl5qmff84DV6u5kGKSvAyYpwyRZusF_ZaNDiOTmPE8RgAyCDUVZu2ZYR2fUBj2-xcwMX7DH0L5RwvJmmxlmhH5i_MCMxP0xj9jgK2zC_iBqqGPtZMVR0M88ISRjEM5ihjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سگی که شباهت عجیبی به مارک کوکوریا داره و حسابی وایرال شده
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/101556" target="_blank">📅 14:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101554">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eUrjYJJIfFzLKTgJuTOgyKf3fLwozNg2qtUIkk3nEPhb4QkGaabAGkU68QpZd8yPiEytGHHMeevDy8oXmBYicXpPPx5Na1rbFwKSrzC4gO-Y-WvNG63OALRDyswiSrvJMPlAjr7nynpEHu-pvHhXjNPil8S8DMQBQpWPhqxAzzUiKB7Wa1iRY_qKZ56f6tNmY9yrRK5dKcWIVVXgsYVO-kWEioOcnrH2XNxmp9Tprt03f8qvJ2LPhfVP2HTJ7iWyIqS5gxDLZWiNh_k4iCUF55sNn6-6Ik7tdXnnp1zxniqj0t8nCAsdxICtHCPNc62OIEXwUv4AeorNI64QqKsKkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rrvebBrGW5flHk0bAmfSjmQM7oURMVZ3x0PU8fB1sdV9bi5Tzgr6IzO9VFWoEFOQykiaSWfqeBmubuFWZ53CLUzefdGNxFUvYYSAJtL8tJmflckGPfVnEC1nvBZ1GFM-hDRTaoMRoXiNvN0Mc0FzHzcZkkIWN_sLM0Urigiw3kEz2Nr1YZrNt39l2s-0sqUNaLXuZ80Ru_OVGVEKmRIXV1xkfEyW_IQU7grJkn6eXeiZSUQnRgQearuE8jETfgU1OyRr_mZSpFgwATljsOzbeKgoCpd8aOC32eES5vOuVir2xrQjPnAZhWRqLcAhsdWKVQlGxFWN084fTf1Ee4ogVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
خوان مونفورت، عکاس عکس معروف مسی و یامال:
من به خدا اعتقادی ندارم، اما این عکس نگاه من به زندگی رو عوض کرد. انگار همه‌چیز از قبل نوشته شده بود. هیچکس حتی در یک فیلم سینمایی هم چنین داستانی رو باور نمیکنه! هیچ توضیح منطقی یا علمی واسش وجود نداره. یکی به بهترین بازیکن تاریخ فوتبال تبدیل شد و دیگری حالا داره جای پای اونو در بارسلونا دنبال میکنه و در ۱۹ سالگی هم قهرمان جهان شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/101554" target="_blank">📅 14:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101553">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SI06vnfyh-9BdNnF5ebUAU_wq7TMVkduXHejz7_6ep5D5CWux4XhpWkwWadJJdx9Jm64oJ_-pTgooquvLXa1oo7X1qiougQtQ2OhYAuoWoNNaQa_KJNga28yrItBc23MpeoL3BD3trZHIjs0RXIkFgVf2XkEv6cm-Xu2WEqBI9RhvIVHwqJS4nCdoUTUfrVV4t_donwYgWcyZdFseNpEWijw4HuF-g5SB0v7ioAAh6cmubqzmxf1L4n9LAjKHs-kyvdLm4jf6FKhRSaQ6PXn7bIjX2wnr9PkriS-f9j3zb5m_hcldlq8zv0pV4crSbkCUrs-HjhEUYH76QGQIhkf4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیمار دوباره در برزیل جنجال به پا کرد!
باشگاه سانتوس اعلام کرد نیمار به‌جای سفر با تیم برای دیدار کوپاسودامریکانا، در برزیل ماند تا روی آمادگی بدنی‌اش کار کند. اما ساعاتی بعد، او در یک تورنمنت پوکر با مبلغ بالا در سائوپائولو دیده شد! این اتفاق باعث شد خیلی از هواداران شدیدا از او عصبانی شوند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/101553" target="_blank">📅 14:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101552">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iB0_MlbDcJWBK-aUJe0qOlywgjgZCsMGFFNdo0e39mIw-FxMnh1bpRKq9m8oewBdTwbQTZz8QY82Vk9jSWsxcwBG3MxGyhAG48D8hP0ho2Gk0hvPGvWSfdn2xyxTBC6_lb6-1ajQAVkPKGrfXMJNygu58fgjjou8cdpacFN1JCWmogdEISkq3unV6mNJ-Dm-UKnaEBgkJaurI8Fi-ogD-x1bMpNHW3VWpQeFTaTp3O9VulfhfD2K5XPsE9jBV5Gcr0q0OaVFR1kkAXzDz5ZQyS8TtgKfqCBQgimwfu8tydZbX7wzh-Yu-PI1HwWUJn0_TAeyLiSPOmJIMnA7w-0R1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🔥
الکس فرگوسن: "بعد از اینکه ایتالیا جام جهانی ۲۰۰۶ را برد و یوونتوس به سری B سقوط کرد، من مطمئن بودم که او یوونتوس را ترک خواهد کرد. بازیکنی مانند او در سری B بازی نمی‌کند. در آن زمان، رئال مادرید نیز به او علاقه‌مند بود، و با توجه به مشکلاتی که یوونتوس در آن زمان داشت، تصور می‌کردم که یک رقابت جدی بین منچستریونایتد و رئال مادرید برای جذب او وجود داشته باشد.
🔹
بعد از اینکه پیشنهاد خود را ارائه کردم، پاسخ او بسیار تکان‌دهنده بود. او به من گفت: "آقای فرگوسن، شما قبلاً با من صحبت کرده‌اید و من به شما احترام زیادی می‌گذارم، اما یوونتوس در حال حاضر شرایط سختی را تجربه می‌کند و وظیفه من این است که در اینجا بمانم. یوونتوس در بحران است و من کاپیتان این تیم هستم. آیا انتظار دارید که من آن‌ها را ترک کنم؟"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/101552" target="_blank">📅 14:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101551">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d88e870288.mp4?token=rGDXTnmwBQM4syUQl683l2j5Pty2UXJDim5AJ5G7K_xQwTxkDkq3vqL-uOYjVnIDCwJiHmZ8OGHJg6XigbYZSjWPLQtA4y1NJEpjr5HbArDOnKtbLKSibVX5TxQ5RCpV-Z7QoMOemR5bcrDGFCS9W7oe3OcYFlCjLN4R82gAe4BUT2BcsujdWr19hHUn4gtbyunVqIQZROTcnP_nrG2Lvo_bF7sisOLEBFitW1vWpONhiZLT562e33vMhHkycuCNSotpLsZAkc7w82CovqRPetrumc6nxKN_HQR4dFc_kFUWU0gRxQirFJf7yiOhVOHs0dhEg3RFANEnojpDWADgRXGoA1S5USF1yNDQPBuOa8xcQtz5gKFuo2eWvnAMz4FIC6N-OJFpau5oDzrX861QdqkwUNUWmZ7Li6UuDL47necZSe4iJYSbopPoKXwZL3YhJY7-X7-rW591AOJaRIUTLHPiIykeqHphhxqrcdVkgzBq7MwiRoS10qgs-zaOnicaXVyBf6ew25fbViKjDwQK18WDzEECXK6YobE7DYT5CGTQYoy2JTwMoGlVmNPXPX1E3mMzllqZYaXiw2k7SuYPrFiJDoHMduUPLHMUeOMWorJVVL7fWBOAI1R3LyqJG1mRpdb3i-zo6zo7UznMkBsgp-ECc60f32WktoQ7qQWia1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d88e870288.mp4?token=rGDXTnmwBQM4syUQl683l2j5Pty2UXJDim5AJ5G7K_xQwTxkDkq3vqL-uOYjVnIDCwJiHmZ8OGHJg6XigbYZSjWPLQtA4y1NJEpjr5HbArDOnKtbLKSibVX5TxQ5RCpV-Z7QoMOemR5bcrDGFCS9W7oe3OcYFlCjLN4R82gAe4BUT2BcsujdWr19hHUn4gtbyunVqIQZROTcnP_nrG2Lvo_bF7sisOLEBFitW1vWpONhiZLT562e33vMhHkycuCNSotpLsZAkc7w82CovqRPetrumc6nxKN_HQR4dFc_kFUWU0gRxQirFJf7yiOhVOHs0dhEg3RFANEnojpDWADgRXGoA1S5USF1yNDQPBuOa8xcQtz5gKFuo2eWvnAMz4FIC6N-OJFpau5oDzrX861QdqkwUNUWmZ7Li6UuDL47necZSe4iJYSbopPoKXwZL3YhJY7-X7-rW591AOJaRIUTLHPiIykeqHphhxqrcdVkgzBq7MwiRoS10qgs-zaOnicaXVyBf6ew25fbViKjDwQK18WDzEECXK6YobE7DYT5CGTQYoy2JTwMoGlVmNPXPX1E3mMzllqZYaXiw2k7SuYPrFiJDoHMduUPLHMUeOMWorJVVL7fWBOAI1R3LyqJG1mRpdb3i-zo6zo7UznMkBsgp-ECc60f32WktoQ7qQWia1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
📊
نمره‌دهی به لیونل‌مسی در بازی فینال جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/101551" target="_blank">📅 14:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101550">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c3187f185.mp4?token=N1deeG0fUwev68ahAWeMQdmE5VDayCDG_pxmhIBL6DYdsG0Q6NX_9g5ZDLmdvsayS5fHxDAshONaUrH0d-RlyvtyAWFGYZOdtuv3oFPUg0_uLuL43lAvcLmifnExxwGYKUIUfRb-sDvJZyenEEdUir9RyPOJVnSHkdJd6X0SkYjxSncQ805FnEg07EEJvtyoI7b7ooslDgn8screXalcOvR3C0F7Ugdb18cFQOFixSBOmp6HBdkCSDQiuqMa0gpODxGig0uQiySO2n3LHBUVYR91749GNOsth8cP9jDYWtqg2lCq3dht4TxpYgxh5a30-ngZXKf2QKzh7nAR5HfzTjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c3187f185.mp4?token=N1deeG0fUwev68ahAWeMQdmE5VDayCDG_pxmhIBL6DYdsG0Q6NX_9g5ZDLmdvsayS5fHxDAshONaUrH0d-RlyvtyAWFGYZOdtuv3oFPUg0_uLuL43lAvcLmifnExxwGYKUIUfRb-sDvJZyenEEdUir9RyPOJVnSHkdJd6X0SkYjxSncQ805FnEg07EEJvtyoI7b7ooslDgn8screXalcOvR3C0F7Ugdb18cFQOFixSBOmp6HBdkCSDQiuqMa0gpODxGig0uQiySO2n3LHBUVYR91749GNOsth8cP9jDYWtqg2lCq3dht4TxpYgxh5a30-ngZXKf2QKzh7nAR5HfzTjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
صحبت‌های مجتبی‌پوربخش علیه میثاقی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101550" target="_blank">📅 13:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101549">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c0345d2fb.mp4?token=tzRApRhnnucL9G2lNgbui79nLMnWG9b0BT6pswkMFcWsPZJhdhSQ1KVnlymIv0kY_8x_C2Q1ZOHN61U-lgzIld_JjzUSiUGq8H0GV_fgEUbAX6M3oDaPH6oIBU-JDQsuCIKq2IuJSC8cyVLA_HrVrZ78lmIXtu6umoxPgUqAnemCRgr5ZASgWIBt0QGRWbw2MFWGRk1IqEq8HReC8HMbX82RhuDgq7Gi9LWemebqK7_1ouZ-Pn9akUglPSMXkSmikU5sj9A6zI90atsVsvQK84uPiwmWT1Bmyv0h9ExddpNp-2HCdPcMZGOsWZdBlK8WbNsIj7SbpwS0GytdNP_7bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c0345d2fb.mp4?token=tzRApRhnnucL9G2lNgbui79nLMnWG9b0BT6pswkMFcWsPZJhdhSQ1KVnlymIv0kY_8x_C2Q1ZOHN61U-lgzIld_JjzUSiUGq8H0GV_fgEUbAX6M3oDaPH6oIBU-JDQsuCIKq2IuJSC8cyVLA_HrVrZ78lmIXtu6umoxPgUqAnemCRgr5ZASgWIBt0QGRWbw2MFWGRk1IqEq8HReC8HMbX82RhuDgq7Gi9LWemebqK7_1ouZ-Pn9akUglPSMXkSmikU5sj9A6zI90atsVsvQK84uPiwmWT1Bmyv0h9ExddpNp-2HCdPcMZGOsWZdBlK8WbNsIj7SbpwS0GytdNP_7bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🎙
خاطره بامزه علی دایی از معلم زبان خود و کریم باقری در دوران حضور در بیلفلد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/101549" target="_blank">📅 13:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101548">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbd74933b1.mp4?token=KmKqFpGUZcYaLkG4QJ9YnlSulj9JLUJpuSjV5yv_--OTOOMkjUMd711mERiF8Qn6_O1a63y6slThKJxgOBjAoIyiS9jc5P9jGuJrLjzcmwuIGHJxwTiRLa2Ft4tnkDUyYHrZMNOQ3HFVh7EkmEohZNCS9OBiF_d4ExUdwvy2hMXuntW2A-VBPdy3BJRcRuXEchqBqdQu3Ss6fxO7iJkwYVCqI9_85pGt-BDbyG_DbGe27Z6p-lkipOZoCLAVj4HPH13f3GuZcGh38Se8rzpgS7nIq5GvnjjaK03eoxzTHJlQgzMfzptJj_WEect33CwO8lI6AgBqsp4ovHR44sWvsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbd74933b1.mp4?token=KmKqFpGUZcYaLkG4QJ9YnlSulj9JLUJpuSjV5yv_--OTOOMkjUMd711mERiF8Qn6_O1a63y6slThKJxgOBjAoIyiS9jc5P9jGuJrLjzcmwuIGHJxwTiRLa2Ft4tnkDUyYHrZMNOQ3HFVh7EkmEohZNCS9OBiF_d4ExUdwvy2hMXuntW2A-VBPdy3BJRcRuXEchqBqdQu3Ss6fxO7iJkwYVCqI9_85pGt-BDbyG_DbGe27Z6p-lkipOZoCLAVj4HPH13f3GuZcGh38Se8rzpgS7nIq5GvnjjaK03eoxzTHJlQgzMfzptJj_WEect33CwO8lI6AgBqsp4ovHR44sWvsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
وضعیت رئال مادرید در این روزها.
🧐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/101548" target="_blank">📅 13:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101547">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlPguFKVFnNEQphagBLqSVEu1GPSrs2KKllNfo54giB5oNvEeiB6M4q9eEzxL810AMEh1i6s7OOelSNyuoY2NSTf7msAzPW-dMb79znVFWMJWyekHNgazf2MhICRlv-MgPH1XkhYVUVQQkikPm3zbiFQfZhSS3EFJH-7LNRwsgYWfTt4vp-V_CecTEe3tYIIU2SGzia3CK62E5hi0Rg2dqNX3zsCbK-EHvBUV4qwz7dykgR6kW5iHqHGEyVewjloSaEQohAFQB9kuHIkTTuWf5yeMqorrvAB9K1d63eiVIcgr2i-X0vaVP8ivP5jItMvyicmz-qOWof0L2_4Zn2-Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
وینیسیوس و زیدش بعد عمل زیبایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101547" target="_blank">📅 12:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101546">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e1e8799b7.mp4?token=EUr45thmLZgb-Rppmqoy0Hfbko_tfPX6AZCSe1LvjGJV2xvWnsyzX-VyYKMJb67LNoZVV7KumD46ZgU5116v7U3igmJuvCr-Rq_DIfxz7vR8-LXEFVY85xwsIc6tjsW9Z_1ncvLRDRtejHiwBDRe2nt-Szk6AWhEOu3xsKaC5mCsukNX-tSEOlGVHoXUmEu25EXfQjmacnk07-RNtVOUI5SwhUgE1HxuoPAzkSAKqJmXeHiAW9EgsxvYOxrajxKYZfK5XY0rqGRpXcHWZEcEYLFsigOHoxmu2mzdMppOJCGG9cB5ylunUJ6jFlL1ybKgZC0bGeH6CRtzQCz9bAZ2f58_KxW3jO7oK1Zti4PWM33i8C_azbm6_q77lCzqacKqRURruxPTrM0fXheIuYwyZIHYplfmYBRa_p-cEAdwQ9XDfZveqgTnLvR4kavwNwjn5v4b6uthZ-B1d1RQcZDF2HdyHzmPrNQSY8cBpJp3ygif6idVBOYL2euvrCPIfcC6QEOBj3LIDVP-Shy-fX0AFHiBwaOIITA64Og_AytehFa6-4lE3X10RRYdZ_XBdFy6mKNf8Yv41DJMvCGtr2356sDTdGQy4m6XwX75zKy3oIpvRQnqZxhOY_IX0oT8nkDvPYHYALEj9t-1ZTYjRHRjlLwX10QhMQjpUk5yH-Cxum4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e1e8799b7.mp4?token=EUr45thmLZgb-Rppmqoy0Hfbko_tfPX6AZCSe1LvjGJV2xvWnsyzX-VyYKMJb67LNoZVV7KumD46ZgU5116v7U3igmJuvCr-Rq_DIfxz7vR8-LXEFVY85xwsIc6tjsW9Z_1ncvLRDRtejHiwBDRe2nt-Szk6AWhEOu3xsKaC5mCsukNX-tSEOlGVHoXUmEu25EXfQjmacnk07-RNtVOUI5SwhUgE1HxuoPAzkSAKqJmXeHiAW9EgsxvYOxrajxKYZfK5XY0rqGRpXcHWZEcEYLFsigOHoxmu2mzdMppOJCGG9cB5ylunUJ6jFlL1ybKgZC0bGeH6CRtzQCz9bAZ2f58_KxW3jO7oK1Zti4PWM33i8C_azbm6_q77lCzqacKqRURruxPTrM0fXheIuYwyZIHYplfmYBRa_p-cEAdwQ9XDfZveqgTnLvR4kavwNwjn5v4b6uthZ-B1d1RQcZDF2HdyHzmPrNQSY8cBpJp3ygif6idVBOYL2euvrCPIfcC6QEOBj3LIDVP-Shy-fX0AFHiBwaOIITA64Og_AytehFa6-4lE3X10RRYdZ_XBdFy6mKNf8Yv41DJMvCGtr2356sDTdGQy4m6XwX75zKy3oIpvRQnqZxhOY_IX0oT8nkDvPYHYALEj9t-1ZTYjRHRjlLwX10QhMQjpUk5yH-Cxum4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇯🇴
استقبال از ادهم‌مخادمه داور اردنی(داور چهارم) فینال جام‌جهانی در بدو ورود به کشورش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101546" target="_blank">📅 12:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101545">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UntL7sUKiqjF1WdAMXd-83SJV2repKIwJeT7B0c_K-sD_jjjz6hZo9ydDWxTQ6VyQEiwWApC6t5BLr4AP-8-oNRD5-Es3-ZnFyf59J9ltKNQFZ-4uXvZbpevei2uIt7NkicRblQGLFmHYlgXHDNNTi4qUIKYYuNF_sDN1rkcA7wasvfXlOGiQOeHrAON6S2z5CtXKmyuiXURzapZKdNS5_mtLjKctxBcEgKsGEvjhRH_YKIrS_Rh1vh7ZF1wzQ7YoTe6vixp-JJrCBbSS5WJAs62zmLgcpo2kfx1Fk2Sby_czfLAa1TslCRBVmjdLzjBgd-SxluNyGW8JiffwfCXUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
۶ تیم قطعی صعود کرده به جام‌جهانی ۲۰۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101545" target="_blank">📅 12:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101544">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
💵
پرداخت آسان و سریع با تمامی روش‌های پرداختی
📣
30% فریبت ورزشی برای واریزهای کریپتوباکس (ارز دیجیتال اتوماتیک)
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/101544" target="_blank">📅 12:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101543">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYDlz1TAvxceBMDoOZS5zFCmQtT4mFzkDBApSaVoTkjR3YEbEO63gG0YOdORovBKHUjA-AiDqdmqVX-NEA0YaWb2zkOfYQzpZgI8_JY9GG6elBT27seXJdej8pwXZZAZLS2eEz8Md1KSO2SUNHaTqjoC8SEkNiH3aNJagvY5LMICefwXy5oFYViONaIqAAgAcmsKmOfPZIiN4GKvWnbNiJXuF4OxqhfKQocOuZZH8b0SYo6xD2FroQacBdb5bfItzhFRhtADQ6DgivYC4JU9eTO6E2gj9CKhLtWA7S4szdne7k9N5Zlzb6eyKTwqa4eMx5DRKbwkFhpp1UZWypk7zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBET
💎
🇪🇺
لیگ قهرمانان اروپا
⏰
شروع بازی ساعت 20:30
🎁
100% هدیه ورزشی ویژه اولین واریز
💰
محاسبه نرخ دلار با قیمت 2.200.000 ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/101543" target="_blank">📅 12:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101541">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbcad2324d.mp4?token=hIQxRA-NyvVxLMUNPpDiwiKixU2SvN_wTd0qvLMRzgkx5cc5gNI-rtmmZDTIl4GlcdGyabpZSbhnyRO9d8-fGMD6LnfVQC5LaIDUvBGa8nBqnERF9O5vkOigkUvpcuLLHo9fRAp8S9TTD5h8DbZB2xs9svJQz5NQohvIIB11zqJpD_5YZcb2kW-AnPgaHGsYdfNHwsHZjlWOmes3mivFkAa-EYpEqH6uKOiDcA_mneZHmm_OyaINZgsp1DB6_KsYZx1HOIMmUkXfbocQkgDnPSlJPqz_gyj7RWs4Qw7fBTZ6O2SMbYP5ndUHpuGOsprzqYHZbtbJ8vPWxR_DlZ1KRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbcad2324d.mp4?token=hIQxRA-NyvVxLMUNPpDiwiKixU2SvN_wTd0qvLMRzgkx5cc5gNI-rtmmZDTIl4GlcdGyabpZSbhnyRO9d8-fGMD6LnfVQC5LaIDUvBGa8nBqnERF9O5vkOigkUvpcuLLHo9fRAp8S9TTD5h8DbZB2xs9svJQz5NQohvIIB11zqJpD_5YZcb2kW-AnPgaHGsYdfNHwsHZjlWOmes3mivFkAa-EYpEqH6uKOiDcA_mneZHmm_OyaINZgsp1DB6_KsYZx1HOIMmUkXfbocQkgDnPSlJPqz_gyj7RWs4Qw7fBTZ6O2SMbYP5ndUHpuGOsprzqYHZbtbJ8vPWxR_DlZ1KRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
بازی‌های افتتاحیه جام‌جهانی ۲۰۳۰ به میزبانی سه کشور آرژانتین، اروگوئه و پاراگوئه برگزار میشه و سایر بازی‌ها در مراکش، اسپانیا و پرتغال خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101541" target="_blank">📅 12:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101540">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cde737c1a.mp4?token=RmfqyjUIPrk_jNYEjgYMaxYJRnQ-DhoWP2M99XTWpzNxeERkMzmGCfPh2_w6cJaQGkOQEekxoTAtr-FxoFYgrEx3tuyVItIZanp1CQBDTYhvRdXG57RY4kSQxKUGmaRKoLBwXU8B0ehIBZz5YJYMB14-wV-UCGtocITKIgNZ6aj7b0SqcH30Oi89vC-MePXTAcT4jcuPPz-1cOVQFhFfIukuVjL8n-Ba48hvC-OPzEym49ii9IMm_xJYWrt4tuLLjVbU_l17QRULWh7sTetRuTCIUrccWzfCigCJVbB1eOyn8xopuC-utKnJM2dFc5C6X53gjebNjKaxkPe3_1UB7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cde737c1a.mp4?token=RmfqyjUIPrk_jNYEjgYMaxYJRnQ-DhoWP2M99XTWpzNxeERkMzmGCfPh2_w6cJaQGkOQEekxoTAtr-FxoFYgrEx3tuyVItIZanp1CQBDTYhvRdXG57RY4kSQxKUGmaRKoLBwXU8B0ehIBZz5YJYMB14-wV-UCGtocITKIgNZ6aj7b0SqcH30Oi89vC-MePXTAcT4jcuPPz-1cOVQFhFfIukuVjL8n-Ba48hvC-OPzEym49ii9IMm_xJYWrt4tuLLjVbU_l17QRULWh7sTetRuTCIUrccWzfCigCJVbB1eOyn8xopuC-utKnJM2dFc5C6X53gjebNjKaxkPe3_1UB7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
علیرضا جهانبخش: به فردوسی‌پور قول دادم که لباس محمدصلاح رو براش بگیرم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101540" target="_blank">📅 11:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101539">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glRESzEk3xcRE07uYECnsnZzCJj1BDPeLaWqO6z3oMZOJ1U6BATAAT-dJiOlakHDkjiJr_5zuXtFCxEz2D_N7vgDi5vnHDc3VYhvRKgUrXYDYU5NF6KKuf-y8KsPa0SjNNSTznx93_RJZbqAXsl4z4IKcYvRBpNDlZh5UXQSpGQLCL4VUGwpfO7BpRFUFPGCrtkGuyUGm-bry57MNTQgEve4y-WiaiEpY0H5_nfktWx4SmuU_gvq8a7_mlWxcLc7RroGssSovUqU16ZJ9svA6wJ1S399bjTcGhLugjCrTYVA2B6ztX3yJxsEgiauYHaE5AyTNcEYCVJ5i10JiNATwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌دوم منچستریونایتد در فصل‌آینده مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101539" target="_blank">📅 11:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101538">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ovxvhk8mIgsyqcCjDLmAjwJj_1-nWdK-5RT5PcW9vGEejH1GC_-cjxDM-JT3zaJxgtbTMr6CD0W5Dsp4Kg7vEy4fjCB6grPnFGZuLfSv0E83AU2RFs2v5YCbrCN9V92ph7GXyjgUvXc1ESwruZ9HUWDCaYWZ8IQbEblA8sC5gDJbdirhxUNVYfgQTWx7JbufdLzAVzJIEF3l3z4iVlS9R-mrP0k1lpsAu7Jyt5ZW9SrfoSy-pagUnbq0QclepUDPh07844gfj5M8tcwx2bDsYDG7Yo7-JMqhYIq7i92Z3B0YF4zot4i-N9h8cR_Q08cKqAIrLn5o4XQI-oOsAeJx-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
حمایت یحیی گل‌محمدی از عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/101538" target="_blank">📅 11:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101536">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/330d45af26.mp4?token=mjzm0YVkWQMM_lz9FWMn0eTxdyIwNg2XcsBbYzJXC0G_Nq3wm7q3vHPeaaq2OECsJwqfbuUZX7PMuFqJeJzjTNjLIL5KVV484ZPOuslctsAvkid3wF5ODjQy9fbbNu2IB0WqkdF3j6FfZ4UMziO9MvevlxryvtIU3RBZKPZWvkmzz0DB5oh8FODDWpB-o6ag3gMG74Gl1OMI3iAQwYqTzcYejR4NrgnEatp4sr9lyFDvonN7tPh_uzDSKOk3ZEhKXzdy2HVGxvirjyOc89F6qII0ceGfdoqaKh4_2MME9lshJXtrsuZ1DHYuR8cUBTvBRedYXgh4PEYOHXCTBYUDMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/330d45af26.mp4?token=mjzm0YVkWQMM_lz9FWMn0eTxdyIwNg2XcsBbYzJXC0G_Nq3wm7q3vHPeaaq2OECsJwqfbuUZX7PMuFqJeJzjTNjLIL5KVV484ZPOuslctsAvkid3wF5ODjQy9fbbNu2IB0WqkdF3j6FfZ4UMziO9MvevlxryvtIU3RBZKPZWvkmzz0DB5oh8FODDWpB-o6ag3gMG74Gl1OMI3iAQwYqTzcYejR4NrgnEatp4sr9lyFDvonN7tPh_uzDSKOk3ZEhKXzdy2HVGxvirjyOc89F6qII0ceGfdoqaKh4_2MME9lshJXtrsuZ1DHYuR8cUBTvBRedYXgh4PEYOHXCTBYUDMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تمامی قهرمانان جام‌جهانی در یک ویدیو جالب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101536" target="_blank">📅 11:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101535">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41b3828f7c.mp4?token=NMHbetrcKCoi9EAla8litVSh3F-vaLZi1mPW4SbBL01KE7kS7SxjXJdxddXrQlXcbJWyLXgyEkEr59yv2mG03-6Nspd0azaKFsrsIwL1aV_gsOdWL43oQ-jftcHKP8k0IBO1OiyFNXT_nkpH7m9ntdnsfH7t4kwwhzk7qtk-EDd2Fs3HNx4smdgWUoMxkzbkA9LgBMnyahFDDNo5hXdGqURGipQf7I3SwoKKtKJLya_ILrd1798vvnRHEuReIg1-qomLHvLI_lhWOp2runLybmjbGOCkwtrcSGpCEZqnxm3Tbv46hhuQzNN7cCsdodI2o9TAr1DqUEEhJffMWizAQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41b3828f7c.mp4?token=NMHbetrcKCoi9EAla8litVSh3F-vaLZi1mPW4SbBL01KE7kS7SxjXJdxddXrQlXcbJWyLXgyEkEr59yv2mG03-6Nspd0azaKFsrsIwL1aV_gsOdWL43oQ-jftcHKP8k0IBO1OiyFNXT_nkpH7m9ntdnsfH7t4kwwhzk7qtk-EDd2Fs3HNx4smdgWUoMxkzbkA9LgBMnyahFDDNo5hXdGqURGipQf7I3SwoKKtKJLya_ILrd1798vvnRHEuReIg1-qomLHvLI_lhWOp2runLybmjbGOCkwtrcSGpCEZqnxm3Tbv46hhuQzNN7cCsdodI2o9TAr1DqUEEhJffMWizAQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی پول نظرتو عوض می‌کنه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101535" target="_blank">📅 10:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101533">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/191f51b3e1.mp4?token=XfC-U8aJ0d2lc_VFjAY4wSS7-T8lQcUmaLUBq3mpm2QnQ0rHpYV3kwFYSwG9Yqh6RAs-d9x5-6F7bwASp5C8R_Mx86MCK2FUb5ybPNOgU2LiY2_O2hQmIcdt0ZVqMbJD3L5FB50unpUhdt0UQmdv3eJy9J1V-fkuL0IUFF1iTy6uWkWBCsH9EfJpc3LrcWXO82KXal0JEgRSkb-1PCC5tS8b41NLWhLxmm7cqpRwI3w4Xb9B1ML7WmBiGkejOl7Dj0His3pGNznzD0q0yiz9pCgfEYLao2U8L5KmV2n6qb4YD2pqgfwkrFTOlpuplrOUzJX9cljjH969pjx0sFusZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/191f51b3e1.mp4?token=XfC-U8aJ0d2lc_VFjAY4wSS7-T8lQcUmaLUBq3mpm2QnQ0rHpYV3kwFYSwG9Yqh6RAs-d9x5-6F7bwASp5C8R_Mx86MCK2FUb5ybPNOgU2LiY2_O2hQmIcdt0ZVqMbJD3L5FB50unpUhdt0UQmdv3eJy9J1V-fkuL0IUFF1iTy6uWkWBCsH9EfJpc3LrcWXO82KXal0JEgRSkb-1PCC5tS8b41NLWhLxmm7cqpRwI3w4Xb9B1ML7WmBiGkejOl7Dj0His3pGNznzD0q0yiz9pCgfEYLao2U8L5KmV2n6qb4YD2pqgfwkrFTOlpuplrOUzJX9cljjH969pjx0sFusZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
یه سری ویدیو قدیمی از قبل آشنایی یامال با اینس گارسیا دوست دختر فعلیش داره پخش میشه که توش اینس وقتی یامال با نیکی نیکول بود تو لایو گفته:
‼️
🔻
اگه یامال یه میلیونر یا یک فوتبالیست نبود، نیکی نیکول حتی دو بار به اون نگاه نمیکرد!
﻿
‼️
🔻
همچنین ازش پرسیدن: «لمینه یامال یا امباپه؟»... گفت: «بلینگهام»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101533" target="_blank">📅 10:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101532">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">😂
😂
😂
تفریحات جدید اسپید بعد جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101532" target="_blank">📅 10:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101531">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d084b6a5a.mp4?token=e4v4-hdaBfoBDmgAiCht7mImT2WuFJFEwgtZC_TKl68I_TvPSoYclVyOHWFYqN06RzxHDnga-A6qe01Yeh2ktW9iR92mQZ0G3iPopfmiZCkQLP7HIDaxb_Stiv4PT4Jpuy5oYqBBy3we1HgMFmzzyyvJV1RqCrjnsNrYYrICmSa78DLx6s-RsKZkWtWiS4EvdWen-Oj4wLVmb44H3TNwBOUO_VnAQAKkqP27-x8Zn8Btd0kjrnqb-gdslNUopAp3ywpDahh78RSGNjujX9PjtmRDBI3MES_BhE84cvjm_MLHGXaNVRb0AsVLvC2iBiLFTa7WVX8h1XW5I9VkvzDXXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d084b6a5a.mp4?token=e4v4-hdaBfoBDmgAiCht7mImT2WuFJFEwgtZC_TKl68I_TvPSoYclVyOHWFYqN06RzxHDnga-A6qe01Yeh2ktW9iR92mQZ0G3iPopfmiZCkQLP7HIDaxb_Stiv4PT4Jpuy5oYqBBy3we1HgMFmzzyyvJV1RqCrjnsNrYYrICmSa78DLx6s-RsKZkWtWiS4EvdWen-Oj4wLVmb44H3TNwBOUO_VnAQAKkqP27-x8Zn8Btd0kjrnqb-gdslNUopAp3ywpDahh78RSGNjujX9PjtmRDBI3MES_BhE84cvjm_MLHGXaNVRb0AsVLvC2iBiLFTa7WVX8h1XW5I9VkvzDXXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یادی‌کنیم از سوال خبرنگار صداوسیما از لیونل‌مسی که بنده‌خدا اصلا ایران رو‌ نمیشناخت :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/101531" target="_blank">📅 10:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101530">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sukY0xtcSdDJMI0rMPE9mGB9MN3DcVd_dkQi4tjZlJEbW210JXg5bBozPTiwzSYV97lFiezuVLrtcO3UQq_FlR-AgFI9-2_WN8q3sD6uHJTubz4tYrA1ln-IlKovfv9DmQqDNXIiCCvgtzapKOOcKCAo4uU1bQUh0eUAt4VdVZB67tBPABapDSdRB0ON1jcgZqKsGhH9XHTVNBzwaUS8ViC5v1Dc1KQDQmJssisGCzOwwM1Dx896X_PVUWBbwUUObP_-sb8p0r-4aHjsArQ2dQHvr_sQHPJakSkLKnj3RsOuLX4cYP4fP-ltaCtBV8gX60z-t6hICsNBb59ciEPn3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📅
🏆
شش سال پیش، در همچین روزی لیورپول برای اولین بار پس از 30 سال قهرمان لیگ برتر انگلیس شد.
🎙
یورگن کلوپ: "این دستاورد بسیار فراتر از آن چیزی است که من تصور می‌کردم باشد."
🎙
جوردن هندرسون: "من بسیار خوشحالم که این عنوان را برای استیون (جرارد) به دست آوردم."
🎙
اندی رابرتسون: "ما 13 هفته منتظر ماندیم، اما هواداران ما 30 سال صبر کردند. این مدت کوتاهی در مقایسه با زمانی است که آن‌ها تحمل کردند."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101530" target="_blank">📅 09:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101529">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLDUadm019G0v8bPTwmKxi9HD-5z_XSDKxCAIlXq-MDRA2aeSwBHM47TEqmWd3IvHBtdiMC5vEfdJFSg19XBfb4FSDLwVc1mHQel_V0hhLYswI0Og28VpFiu8uSgqrP1naXYRPX00oXh3Z3hotVzYKTCLph_uKB9_duL1Q_DfZeqAmdjLnaqTMZCjjxoUWOm__VhJPnQz6bL-PzFXNMvOJRVNpjYVMHmGpe5PiFa0mNJuuKYh70UcorIFmRhhh0YAqs4n5Sgfbe1vKMw_-iqe2vjOuzDwcpSsSUYbTof-UJWbW5uCvCViIqqpBRGqrM_FRjfGfjReVDza3-YSZ5rnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو
🚨
🚨
🚨
🇧🇪
🔻
مارک فان بومل به عنوان سرمربی تیم ملی بلژیک انتخاب شد.
𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101529" target="_blank">📅 09:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101528">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8781c60fd.mp4?token=gBTpHTlMJdqEGs8sgtSSUACShtakjkmQac-ClUfj16zBy0Odi7YGinVkraasYBSaBCV7cizfjBtK42hc8Vn9G-0CgZh7bPNJEF0o-kVJa1uqR9s9VyPK8dDGo9fxIEW8Bzy6G5fsp-rDa_oqpea-rhZJu4daj6ig3ktCUfFcqPskQNGXHOt-g7RDe789v1wX_kXXZxbSU3m9qSocslpGsSD3YEYvBg5D__RrWJskQCCv-s3ZpYXlecdFn2pvb7-34FsDzrE0hNQCDxZ7cjTdGvLgOZt2gVYOVXCSlVPzxAzeSEDS0KaJn1U3acmXG6s_n7sss2_9llxTNyHVudfTrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8781c60fd.mp4?token=gBTpHTlMJdqEGs8sgtSSUACShtakjkmQac-ClUfj16zBy0Odi7YGinVkraasYBSaBCV7cizfjBtK42hc8Vn9G-0CgZh7bPNJEF0o-kVJa1uqR9s9VyPK8dDGo9fxIEW8Bzy6G5fsp-rDa_oqpea-rhZJu4daj6ig3ktCUfFcqPskQNGXHOt-g7RDe789v1wX_kXXZxbSU3m9qSocslpGsSD3YEYvBg5D__RrWJskQCCv-s3ZpYXlecdFn2pvb7-34FsDzrE0hNQCDxZ7cjTdGvLgOZt2gVYOVXCSlVPzxAzeSEDS0KaJn1U3acmXG6s_n7sss2_9llxTNyHVudfTrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
فینال‌باز واقعی آرژانتین در کنار لیونل‌مسی فقط یکی بود اونم دیماریا که واقعا نبودش امسال حس شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101528" target="_blank">📅 09:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101527">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d9304f085.mp4?token=siybEc3rtSTdlw39L0hC2iL_dvJlnQLwOp-C6uRC6C0M8dlpv67bYPoaOm14f-zin8HfBKBs7g0gM5YKSpTbOuFCmvAtLI-xgyeZmLS2j-dU0VJoEIn33zuMJTDtk8jezvy1LCVYZEr2Hc_g2nA6TQmcy30vsHn7QjjID18SXWHHKH86wMKHv4Ayb5U72tXtc53sy62kmmCxwWUG5cfrmeHKtPxQFoCsVFyUyi6bIga3_6OTm6XqcPWgrpsC_Skdo5SBuk4ZKdcVOGs3__6HuAll-sT3D25kRQmQZED4pSBJWfytDR7wc0qZPxxsL1EAEEvnyr5cLnEtInRP4NAsQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d9304f085.mp4?token=siybEc3rtSTdlw39L0hC2iL_dvJlnQLwOp-C6uRC6C0M8dlpv67bYPoaOm14f-zin8HfBKBs7g0gM5YKSpTbOuFCmvAtLI-xgyeZmLS2j-dU0VJoEIn33zuMJTDtk8jezvy1LCVYZEr2Hc_g2nA6TQmcy30vsHn7QjjID18SXWHHKH86wMKHv4Ayb5U72tXtc53sy62kmmCxwWUG5cfrmeHKtPxQFoCsVFyUyi6bIga3_6OTm6XqcPWgrpsC_Skdo5SBuk4ZKdcVOGs3__6HuAll-sT3D25kRQmQZED4pSBJWfytDR7wc0qZPxxsL1EAEEvnyr5cLnEtInRP4NAsQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😔
پیام استاد وحید قلیچ به دونالد ترامپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101527" target="_blank">📅 09:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101526">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMiEgM-d7vxL0Vz5mnzRELU7AQ5lLDLtGTz27JeMjzJoUdj0og6vxg_uwtqUxLN3cbHu80RNCGuJzAdn2mdT6dZutJyoCLGETy92W5DcLTaAYOEO8xNI0URoTQ3nb7JnB97wfNZWtu9nbDG0IJ6V9gjwKcRd9wfR5MvZsz5NoqTXF6-nkDknX4bMfORWC5iMvV2pJV_PSZBOLq1sT2GWd20CNjz-WeP-Y-TFXDNeS5P773kAchg7qdPKE67beLA4_-gRlkmRbosk0o_rf-E91-qvgxOVAoC5NEvmXbMAphow4_taMMi9O7o7rmlnmD9X2yoGoMiNpC1tFCMXuPqZYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
مارک کلینمن:
🔻
جف بزوس، بنیانگذار آمازون و چهارمین فرد ثروتمند جهان، برای پیوستن به ائتلافی به رهبری آمیت بهاتیا دعوت شده است؛ این ائتلاف در حال مذاکره برای خرید بخشی از باشگاه لیورپول است.
💣
💣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101526" target="_blank">📅 09:11 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101525">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab5d3c4f61.mp4?token=EZoQg13Mk29sHWEmIlF8SISgWXs14LfAdZIOYRLfzJwFXZ4VNs3-yG-aJaQqCMZNB5oQaUO90JYX7mKmjsegxJ-S8kzKiW1OYaRFhuJjwJdYwxyJiWuSje6ZfaIuzC1kqByWR_8bA4nu-NLgasHnlcuJ_DmGHWhNoZnBCYe04RmXp9gMazGuAE2RA9MChwHWPSDN2vLgLIGNjhy99Qo4IIWb3I_IelWMEt96o21atPVlymRB-ckQSmJppMRMxtSaXhzcsyHvJ6Ey_OaMBz-A3WS3N8bZHEM6De0gL10hJ-RwSIIfY4Qi8sVHM_ITYG-IZaB6lI11yfGS7QM-Kkl5qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab5d3c4f61.mp4?token=EZoQg13Mk29sHWEmIlF8SISgWXs14LfAdZIOYRLfzJwFXZ4VNs3-yG-aJaQqCMZNB5oQaUO90JYX7mKmjsegxJ-S8kzKiW1OYaRFhuJjwJdYwxyJiWuSje6ZfaIuzC1kqByWR_8bA4nu-NLgasHnlcuJ_DmGHWhNoZnBCYe04RmXp9gMazGuAE2RA9MChwHWPSDN2vLgLIGNjhy99Qo4IIWb3I_IelWMEt96o21atPVlymRB-ckQSmJppMRMxtSaXhzcsyHvJ6Ey_OaMBz-A3WS3N8bZHEM6De0gL10hJ-RwSIIfY4Qi8sVHM_ITYG-IZaB6lI11yfGS7QM-Kkl5qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
روایت امیر قلعه‌نویی از دیدار با یک آیت‌الله!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101525" target="_blank">📅 09:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101524">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/foInyhMbobJ9AzTG1iXA_ducSZOOw7BnJZimdpOTuyEdL68rNeO-syoMwr9WvFbsXvQsm_A3pbIB6meEbSJuy_vn0x2o2pRDPnbuwGgp5wf83Z-ohVPoekRqmObn-npx3B777AK4dDzJIspebBUw5F-MrdIZE_0MrE_lAQFTMffPZbU2jnM7pXbxU6Z_UIZryqaVQwoTpqcNY5ov5WRXl5Hr9fKESyMuknNn1ed_XHxmtDTOMHXL6B0xPkxpfZf8kKGJlHn578ZJ1UbvTj4xQ92iWRSrBpop51c8iLqC4H8mkwXIGgRNLcYS7JD9pf3NCx0b53S663549srGWKeqHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر شاهکاری یه کپی بی ارزش هم داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101524" target="_blank">📅 08:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101523">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-TbWtuhdECjf8xoGY373FgrLbBw8c0Wp2yIEkowRK_BSDT1-693VtH9aMwvLIwiQcJmCAZfjKDjKTkjZlE1Mtt8b3yXl5nhWWChNlKObjMml-TVY9lxdNu85SE_ObIeHBaopWz1igy3oDGXNeTcEWIruvpwYiVcEsyOxORk5Gif5HgtAF7iG2sQ0jrjaUC6jYjSQAtBI1LgJs6kwcyAIMgaVnRoLh6VxJj0BrZSzvQFqSFt4oestdVBc2xALt-eJzOv9BXR7Bj2KVuVJbX20CKp1Y-gBJX0U9Ro3bGIoEsLl4aTND9srOG4sxDoC84UoP4SR6bJh4d_zTnZijjWvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇽
👏
دیگه قرار نیست بعد دیدنش بفهمیم که 4 سال از زندگی گذشته و اوچوای دوست داشتنی بالاخره از فوتبال خداحافظی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/101523" target="_blank">📅 08:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101522">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQ3UfTXGhZv8m5mGqvufjmtMnUHU9fugarePAHynodRWk5VFkQlKzci-97PzWRJGlLtP4bDm0M6aPraD0FOaKoErfJMBzv_fZUDaIP_y6xORRajcuTz2Ntza7i9zqui5LUEpTofnqux-pL9bwwelerFgsAr9qD2bUf7BSgyzVrPoeClSwYHBCkw5l6iFwKL0R0NCFvB1OzOEkBv_1OdtfAWrqZCv5x8X84N2z_NoKdGbsQCPS3kGSatbA0xosVgGoEoUni0QTDwYQHCKVs3PrLu44v4kUDndeVe1T7RUYIFgcrooGOGicVDtHg56dmNtl19HyaE3Jq-M_CnVA1WHXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">-EURO 2024
-2025 Champions League
-2026 Champions League
-2026 World Cup
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/101522" target="_blank">📅 08:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101521">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
⚽️
ماريو كورتگانا:
🤩
🤩
- رئال مادرید در صورت ارائه پیشنهادی مناسب آماده فروش کاماوینگا و رائول آسنسیو است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/101521" target="_blank">📅 02:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101520">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqALh-VOKHHghdXkKFQUvlAm-Yy8mYPJnXu0LHXdK0ZAwEzywDMxkLHmQP9OevSwN41ufNxEojtJ4nNpntsLmNb-N9kQaqTsufk8UEy-cbwBqxibBMEMh7tSnqGlaGQAw0huX0Erg59YtzxjGeGni8BE7HA-BQlAgkh9EBZIw0gs7wq_WgHx_VqTKohgfH8OKcfNRIjnA3QJa7jM9zi0RXl990V3XH5MNBjOfLnt48nxP2XNlXBObqd7PD_TUei11rLkr0RduHR97ue4nKiyZYLDwuMdD97_VeZBMCsmXNVnxY0eBrmuyCRrwy2aRIZ7Hf47GJO4kWdvnBqNC0wVVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇳
دونالد ترامپ در یک جمع خصوصی به اینفانتینو پیشنهاد داده که در صورت عدم انتخاب مجدد به عنوان رئیس فیفا، نامزد پست دبیرکلی سازمان‌ملل شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/101520" target="_blank">📅 01:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101519">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XblSyhvvtYRxMSgQX0DgWYjCq6WkEeqgRuxVZGw62Y898ZQB2cEeikEhnyRurtKMv0dZKMwnwfzGKdRON2PIDE4vnvPrbdqjDL-pEETQOFqNAe_sN2h9znTa5MO7plXfNs881JwPX4BC2O2IpIzm6_DUM-5TjyEGUo3dvxegVFo109RqN_ufOFZJPIbP-yU7yKjJ9zcod0UHlXzP-192dkS6ge51c_brp9Xxc1wN_n8YWQMlG3Xe48U5WkAgzG6pW920STBkqzlNmhiihsrtFk-TGY-3vJAdIx5fsexXGFu5X864XnMfzIpdfNWLoCZTPzoa70eSMdFmT3IBAJqehA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیشترین جذب فالور از جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/101519" target="_blank">📅 01:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101518">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/StSdBixJ_HHjOlyAuJ9I_BHVi7snRu5EcoTAVsd0T1GBId2dd4IDJHPn5UO4-5rQmai9sw3T9-bMWknnHU1LOlN4aI657ZnhS4LQT1SORqtByxwu1J5mkzcz_WnUY87XolF7GpM-1TulihahNBAYLJ3s6rRkgZPIpo-zsRg9yQ7yngpq6kQFYelaj02OlxPKJTHg5xCBnapnGUnA_Gj_GeAVmTV3hFb53NcMOmNhAl361PhCGYu5FTxi7OEGUwpmJGIshv0iCY6U99bGmnXFujC07VxIbKWo2QhmnUw4SsJs_c2ZKJk0d37d6DFYfrRlRN3XFvxO3i6xnpJ1dBLV9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فورییییییی از متئو مورتو:
– فلورنتینو پِرز اکنون بیشتر از قبل، تمایل به تکمیل انتقال رودری دارد. توافق بر سر شرایط شخصی، به زودی حاصل خواهد شد.
💣
💣
💣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/101518" target="_blank">📅 01:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101517">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
💥
ارائه مهیج‌ ترین اسلات‌ های جهان
💲
شروعی هیجان‌انگیز با 100% هدیه خوش‌ آمدگویی ورزشی و کازینو تا سقف 100 میلیون ریال
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💰
محاسبه نرخ دلار با قیمت 2.200.000 ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/101517" target="_blank">📅 01:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101516">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4S9YGROY3sEZc8h6bczeXUn69CY3OTX3LEY85e682gsXokJhTPoSGCtnvW346JSiSL4HR7pvUwVAMHo6Qrw9lY8nSbwqXHfAOyVAmPTKa_nzzcyblMZJXx8tyuD5CRpGNr48Fj3oXdpMm5sIQGxHueZ8bsoHXZABQ9AT_THi7mBkbLZbIESXbjmAaoCwlpywHE0dSmV59URDXoN7poTXFS1K5ZJJe1DTOkfuTCCfdG_LflHElZPnyovRgY5keFWk6lW7nF0kpEfkf0R1ck7Ujdq6VlyWz5EEeDpYlpSkZ_y5zHLxZ5px2J51YCHG52JQvCAnrDEKzfaM78-weyZ3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🍾
شب‌های بی‌پایان در یک بت!
🎁
35%
بانس جبران باخت ورزشی و کازینو، شبی پر از هیجان و فرصت‌های جدید
⏰
مختص واریزی‌های ساعت 00 تا 8
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/101516" target="_blank">📅 01:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101515">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIXaKBJ8Ul9ZoIFM6O51eURut_a1tc-8lbz35tbgmU0havqPxwZMCvbeZ7fOB6CQGsSDizMU3nWVw0HzTQPkVI8AScXzk8UGCgg_4gidlGN-okQ6xBAE2PKZwNtvRb0LDmEqUtaWZHYQE3xAPPKrsJP2y0MuZBizl4_PI7sLj7r-yqgXy7pGcdfPxgaeHepQzhqXaHBcsWQYASQgUkFbRo6Q_prpN5EyqRk-v6Wc0cSUAU6vimkmeFyioeUEYOSU507HixojdAS6l1kvu27w2VgpwnGa7Wbn_GbT6cK_-h7ikxuFVK9jrbmfO8EtF8SIcvz3bOC2dQ05VOLbTci3lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
جدیدترین مصاحبه رودری و باز هم خایمالیش برای رئال مادرید:
🔹
رئال مادرید بزرگ‌ترین باشگاه دنیاست و واقعاً دلم می‌خواد برای این تیم بازی کنم. من و خانواده‌ام دوست داریم به اسپانیا برگردیم. اگر لازم باشه بدون لحظه‌ای تردید قراردادم رو با رئال امضا می‌کنم.
🔹
مدیر برنامه‌هام با رئال مادرید در ارتباطه اما بهش گفتم تا وقتی مسابقات تموم نشده، حواسم رو پرت نکنه. حالا می‌رم تعطیلات رو کنار خانواده‌ام بگذرونم و امیدوارم مدیر برنامه‌هام به‌زودی با یه خبر خوب باهام تماس بگیره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/101515" target="_blank">📅 01:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101514">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e61b7dff82.mp4?token=F1cczXnwqjf5wR0X7KkKNMOpAzC480PrXsRb55MZDH4nQ2XPkshBDG6cdJeCkfd7ipprtGnUOSP5Bo5_klHdGAlC1j9x2pdQMJpSESVCxSPZqf9vBpKKfneg_oM2JBy9aG6NpBjGG0fs48pO0iAi_1Z-r8whhnXAw4OKHrJMn-E2OJU-BAQF4eM-ncp-PM87R7LVavf5UgR5XnzWPZMIhFClh0VLy1jeZBBEG2PdvyP3hA4gwhMczrYL6xvaNbWGkcmjWbaNrKw9ueuF4yUm15TpXBsYonqWeAG1-tQJ6pu_I1n_FgEatjgKlgT9p41Tg55QwY0TEI7TPEFJnwNUZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e61b7dff82.mp4?token=F1cczXnwqjf5wR0X7KkKNMOpAzC480PrXsRb55MZDH4nQ2XPkshBDG6cdJeCkfd7ipprtGnUOSP5Bo5_klHdGAlC1j9x2pdQMJpSESVCxSPZqf9vBpKKfneg_oM2JBy9aG6NpBjGG0fs48pO0iAi_1Z-r8whhnXAw4OKHrJMn-E2OJU-BAQF4eM-ncp-PM87R7LVavf5UgR5XnzWPZMIhFClh0VLy1jeZBBEG2PdvyP3hA4gwhMczrYL6xvaNbWGkcmjWbaNrKw9ueuF4yUm15TpXBsYonqWeAG1-tQJ6pu_I1n_FgEatjgKlgT9p41Tg55QwY0TEI7TPEFJnwNUZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گاوی و فابیان رویز که اهل شهر لوس پالاسیوس استان سویا هستن بعد از قهرمانی با تیم ملی اسپانیا در جام جهانی، وقتی به شهر محل تولدشون رفتن، بردنشون روی ترازو و اندازه وزن بدنشون بهشون گوجه دادن
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/101514" target="_blank">📅 01:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101513">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RSUcrhY-s7bcPAx3IO_nCghUdQcAUQ-yHiZHzYd5KlCgIZSqnYe0YrP5Xpyg_mgtvJNztlW56PVuYen9o2CsRe74o7hJJZRCAv3lavWyciLyj0ausHyWA2naJpi4Cavk2CWWSImpHOQGyMMOSuG3BNi0R15SPVEYxZ336ZcPOymsjdk8_c0Kr9Z3k-TlypCSC8_M0hIt-YfVHclsp4D9fzFN1lExY6ZYtjMbrt7wWI_a8RIOBJVHy1VrUbVG9M91uYKitUrpZlogtzMxtbjqNZP-7QrRw5ntH2LXR15J8HLPjw9DbLSSSupH0VVNVztR7EHYizvdigT56N6yTcf4Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
۵۰ بازیکن برتر جام‌جهانی از نگاه the Athletic
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/101513" target="_blank">📅 01:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101512">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YmTlysingzedcufVRgcK8G-m7anzj5kHNupbOj3-vErD32BsrSNQM5lc0dL3aU02TEJHHYSibiQCLjOnXgcosR6McpDzBW48kraoPFJ33mmHlAVtzPYPY2la0gTq5R7-2YSofUpGuFw0fGdY8fQy72ViCrvaWCMkM17jNgXYmnV1hX9AWJ7L7LWdDNbeburwbx6wfnr_7p6LjEcgdYIZZ0w19_4uTTHBSqbT_UetUBRNeBFf8wSI0PwLxWlvy1VNoSn5KYkeLclkqHgUQJgmJEHlM_2VbvtIgVmtuNfl2JkIg40BJY5AQz3dl5rtzMjVCZvfHkhLUv5dIur9TNOc9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری
از رامون‌آلوارز: دیدگاه رئال‌مادرید نسبت به جذب رودری عوض شده و احتمال عقد قرارداد با ستاره تیم‌ملی اسپانیا افزایش یافته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/101512" target="_blank">📅 00:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101511">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
قرارگاه مرکزی خاتم‌الانبیا: تهدید حملات آمریکا به مراکز هسته‌ای ایران جدی است و اگر چنین اتفاقی رخ بدهد تمامی کشورهای منطقه آماج موشک‌های سهمگین قرار خواهند گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/101511" target="_blank">📅 00:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101509">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IvncDSnshsYlR2YbG7EcrTmbOAzNptgXaGTFxpeaZbC3yQuGRMpJl7FQ8quY82hvE8CQnWeh0K0DGAWshRxmyp3McYqVKrn1f3uHpoH9fq3rkTEKd2ufLqBQ1f6UtgVvEOS6VDegCamROUgYSRjWorwc2mO7Jn7bQVBR3M4vSurmqQLhZmFyC46EKdPqhquYRMOflrdf6y6zUPPVP4Lhpt1_4c6MSXnP_oDlKgC4B0N81joB8MKCoqSppVuIxUPhEtlc6LHaG4flyYmZAq3TsAup5ZqdOLvmeWB_mbfM1i0k0k5VzxUhWCqm7sfOnpuHvGLk1WoQHlyFFg-a0UdASw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ly7V9jpkYubyMbym0gbmqg4FW56H1D6-yF4U1pKnUpR7XExuTXHmPAAgb9RTsV2vKe0P0Z9IngXUeE91UcxYSUIwcDQ_9UZEc1XGjrqihmB58fQEDVMMKQGp7ZEoIWIEnWwDfJq9PYZRmvSinRLnJI3HttC445GrP07NV_Z80QHLVrBdIMLQkTaXPz_Xqh40DZRAoYwd5l2mc2UbGaOrt62X5UHV8MKywuIx8liiQZzd9_TDp54x6ow2T1G9pp2AX_AdaNmPcpYlMB8iCz212sXxqI3lvr6dCYKoYytohyn7clFuIwi7kH2EXF08bCr2HSE3ONl3MaQS2jQsowXH1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
رسمی؛ مورگان راجرز با مبلغ 137 میلیون یورو (117 میلیون پوند) به چلسی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/101509" target="_blank">📅 00:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101508">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnbGjLDLnH3EOUAItmcXy9-O-MQ_9TlsNlcRXpDvtEsRa0QHGvc2FNKQH_5A2048pNNOr8hdOx-FT5WV-ax64zjZjXKqHC9z4XhgsZ4DDHPEb2COXQpdcmGl2WaJzvwqe2Ey5wndTfy--O8QkZbKLy45hojBo4kH7MdatofTMWzO8fEAmFq3BmgRJWYZZ0_LKEYDi0CGI_k9JKPZmDQ0TOYcz2eda8SENvRoRqRtAU_FOsfIJEIUa9tA5ebB7KFQnmy9V-5VvlNFE1sOYYybeyKIIre2XfGa6lxI-9BRoaKgQbb6dJECiCMhp9ZOGgVzgQ-ibGG2cldGltQsyOLNKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رسمی؛ مورگان راجرز با مبلغ 137 میلیون یورو (117 میلیون پوند) به چلسی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/101508" target="_blank">📅 00:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101507">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vO3-YYzF6CmPgSWSJMz3qXuG51DuRgMCSxJ7E0nYlmVSwiw4jG_E7iOHaKBKM6Wa4ToD7AxLD-olgwVQLTLSb2fQp5UqwK36H9H0GaVAWqI-x9GFG03XJo3nznv_cTooMnBaAQvjZbKY2krubhXvSc1gc6by1zea8QAm-usxmpaQNIIEhUM2QbjH2mYkz-cYU-avQF2__nSpPZ7kasllfTFbuN5nGxZ4_HEWgsqKVeHJ66UEGvMi3-GY4AQb64Nxv-mbcYLrto3C5dZG3ryQ_rFFbjaekVG6IAdz3wBINQQjGr5dt5YD01ppvnfB0Tu7zSPCXLZvkYANP_1D6CNj2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سگی که شباهت عجیبی به مارک کوکوریا داره و حسابی وایرال شده
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/101507" target="_blank">📅 00:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101506">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBtO_5NRfvMu6W87gNBCGMp7IgfqNcSYQ8lOJQfgU5MobfhQ9l5b9TMRypIJgVTzT_P331uxMTKVA_w8YRSDgkJNPouYk8U_BHjRqbMbWMk027oTvVSh3wFbh7H1FJusszC6Rq5eSyZRG8inM0oxOfQJfMf-xwEI6tyih66zvNtgO_IZUIe6K08yl2f1TEfVQsBhD_wHiJBg9_SYpliKiemUXTzRyXsa3bwTGjaCFio1OowDw_aUPVWUPPGxG97U1yUaKLmk_N_pw1YweyGWR-EBicFHmcXXP_RXUvzbiQf3R7FAOPTpVlW3aRtpLcJ2LrPpzuQOjf9awbJCn1Vbvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رسمی؛ مورگان راجرز با مبلغ 137 میلیون یورو (117 میلیون پوند) به چلسی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/101506" target="_blank">📅 00:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101505">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">راجب پنجره
🔵
🚨
⚽️
امشب باز هم از علی تاجرنیا پرسیدم و ایشون خیلی با اطمینان جواب دادند که پنجره باز میشه و بر این حساب هم دارن بازیکنان خارجی رو مازاد می‌کنند و مذاکرات و میبرن جلو، بنابراین امشب دوباره تاجرنیا اعلام کرد که بهتون بگیم پنجره استقلال قطعا باز…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/101505" target="_blank">📅 00:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101504">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igV4pqe1ZhgNhptAxQZ_H6v-2ldlaoinda8XPC3GIoc2k39KLrzulJGjzbnmRgObCDMnjT70OD3oyJSo1NY97CvZiPk5HLLgstknFATzs7HOUIxzaRwZ6AUT8ZCO4z66LVpp-VzxZ8TWowoW-lmUwmYUOACi8AZhBnyhN27quFonkzzpvnkDll5NLLCVS3P7UW2rmjrl-TJyQVnghlkiNOxE8PrfZ4JkeO2eF2bUSKUDl-IpeCnW8zDEVy4IQB8rk9lvUPngH13sCFtNTsp7SWyhOr0GsktvV75ha3o2x6fcaCEncQWi5nKQa84hAXYNWC2nXj9PNW-Gl0-mDJqaKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
زلاتان:
پارادس خیلی خوش شانسه که من تو زمین نبودم! وگرنه یه جوری با سر میزدم تو سرش که کارت قرمز بگیرم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/101504" target="_blank">📅 23:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101503">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GB4jM9lm88dFCs_w4hTtS_ezSc6m0r7_QS8sEGE-K6TfgCWLKtSpEvYU_X2MsU7lDRtO42KDrBVBePtTbaEqJ-VoQr-TZmxfZHtUARQr_oRN-fnh1k1i8rI6odrzLTPczdWm4vvLb-30y1ceOnm-G1KhUI-YXSHdWp2C7MK-hr2c1x4oU_pLoRnWysb2YEAzHqvTpHchqXb5xD8TRsFglw25EYF5U5sphyON0Sht9bF6xZib9uxEVfGrAMXq2I4GLa4A6O2yJQp0rl7DBS0tkCVs0bjYe_6ttyut9-488SRGbvQ9hi98091LOC4P29IBV6G96DgGFdhJa2Ow1ZBMpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیا بازیکنان آرژانتینی که پس از پایان مسابقه رفتارهای خشونت‌آمیزی داشتند، باید مجازات شوند؟
🎙
گاوی:
به نظر من نباید آن‌ها را محروم کنند. میدانم که این رفتار تصویری مناسب برای کودکان ارائه نمی‌دهد، اما این بخشی از ذات فوتبال است، و گاهی اوقات خشونت نیز در آن وجود دارد. در نهایت، همه این‌ها بخشی از فوتبال است و باید همیشه به همین منوال باقی بماند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/101503" target="_blank">📅 23:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101502">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cd187695c.mp4?token=nLKxtRF3ZDNCwBMi6CBCQckTDuAycIeyIejqRSDpH83X0DMHJuM68jfoBy5HBnPBkHF0uh7Umqpf0MoVXnMERIZFc0cJdfYbOTxNXyd0w7T_BjQxj5kO2rm2WIzL7qIOWip9r2SXXb2-9KOWcYAA2Kd-wM6I5Dyyg_Jmx-r55KGX0W_RWslokezkfPShWNqZCpUe1rfVLdyD7LRPSjHkoKW0FJZoL1M2cfaDhj5U38VvfEvRr2mMQGqRCMeCeZgZa886dVar7AsWuQX8mp53YoHLJKJuE0aV39wb3J6N81n4ppK4crnb9-DhD_lnpOZgrSXZxbyIDHEgYMq9Ihrlww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cd187695c.mp4?token=nLKxtRF3ZDNCwBMi6CBCQckTDuAycIeyIejqRSDpH83X0DMHJuM68jfoBy5HBnPBkHF0uh7Umqpf0MoVXnMERIZFc0cJdfYbOTxNXyd0w7T_BjQxj5kO2rm2WIzL7qIOWip9r2SXXb2-9KOWcYAA2Kd-wM6I5Dyyg_Jmx-r55KGX0W_RWslokezkfPShWNqZCpUe1rfVLdyD7LRPSjHkoKW0FJZoL1M2cfaDhj5U38VvfEvRr2mMQGqRCMeCeZgZa886dVar7AsWuQX8mp53YoHLJKJuE0aV39wb3J6N81n4ppK4crnb9-DhD_lnpOZgrSXZxbyIDHEgYMq9Ihrlww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کلیپی که از مقایسه اونای سیمون و مارتینز بعد گرفتن دستکش طلایی وایرال شده.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/101502" target="_blank">📅 23:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101501">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOM7z7DTxT3e1ViZKamFoLJbyZPuQuIyf0K_C06I2jA21i5fVni7aAOOzIGX4_UKZM32CHs6dLnqVpa4g3etSojouSkqUoOBHT0IYGltStewIUWI0VJivU6z-LCqYzjQLmk9Fq-TWqxQA4GBPDmUy6fFUNP0Gka79taiv8vzFEpFasGUoAvvb114C_51eT3RGr51Xai7DrjMd-5Tc09kjJDTkxcNvQvQlYyeUHOsaW2RpF6jWov5sQWfkzuZRGsTS7DDPGsaZ6HRnuc41HG3ksvwLeSGFvWzOQYgA_C3YaTjHAw3A_UpAtIHaAaXbyUg-CfzCE2gtVutzs9NbVs7_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
توییت جدید امباپه: من برگشتم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/101501" target="_blank">📅 22:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101500">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9116787106.mp4?token=NWx42Y-v1---_CptZRDP9_P91aA0D0beJjainbj_Kq6M7h5tDmKqXDz1qntpoL87udqmtCUxbj_j4omKe3tWhBn6knpdXRrP-vXgtswvbrzFIoD-BIoZ2aZ60v6uBx0OIGFHkfIHw7gPMHaFKjm2jw3E0JL3_y2FjORiDSNmBJjgmuwfdlYVQFXqlbESv1wmIjDKu1iEiDCr9p4JMLca5gyltcAdLk5mZEIq6Q0FcDd_lhK-5SodWOA5-NI3E2dG8V7c80UDaFGB_wrKQ7KOvY97ftuFOXsOvjmxGvs_fbvZWBdwPvIbCMoltDEpDC2pUrLqHJwnoYlDhDIqA4CSZjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9116787106.mp4?token=NWx42Y-v1---_CptZRDP9_P91aA0D0beJjainbj_Kq6M7h5tDmKqXDz1qntpoL87udqmtCUxbj_j4omKe3tWhBn6knpdXRrP-vXgtswvbrzFIoD-BIoZ2aZ60v6uBx0OIGFHkfIHw7gPMHaFKjm2jw3E0JL3_y2FjORiDSNmBJjgmuwfdlYVQFXqlbESv1wmIjDKu1iEiDCr9p4JMLca5gyltcAdLk5mZEIq6Q0FcDd_lhK-5SodWOA5-NI3E2dG8V7c80UDaFGB_wrKQ7KOvY97ftuFOXsOvjmxGvs_fbvZWBdwPvIbCMoltDEpDC2pUrLqHJwnoYlDhDIqA4CSZjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
👀
خداداد عزیزی اومد یه خاطره از اولین سینما رفتنش بگه دیگه جواد خیابانی ولش نکرد و دونه به دونه اسم فیلمارو میگه و اشک عزیزی رو در میاره؛ خداداد عزیزی میگه من ۴۰ شبه از دستت چی میکشم آقا جواد
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/101500" target="_blank">📅 22:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101499">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4bCHLMtkBNKgFSdc-EGPn6J_44sILtowh7XIrkvdEX-xFhN6nFYvrcDps0MeaiCM176PvfD9OyAm9ZYiPgPUxeppgdj51Oafn2MFbjvK-SAt4H64AFD8n2_sDrnXHbxAZpakhRyi7sbq-20KiWH1UEPJ3XDYeL1pz4IMmIS_iXuYIuzWQIdVJlnaKWlN3M6L-j-Q_AhOj-5vUi9W8cchCsQ9XXUtP3D22ZU1h0gXNOrSrdlA2CFPTpk82bVMAK8pJcp06F37mSlAMQpc1k6OHssBw_0WiI-eT8VHLcywwPv_hxM-HlE1nbU28VpL7LFskw8wcElUdyBhkFwsF8u7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🥂
استوری جدید راموس در کنار لیونل مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/101499" target="_blank">📅 22:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101498">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76a3469819.mp4?token=RVg6HcMhnSM_qbaJTME_5yjvpklwjBllRQam2OCtBB9HsVw4Wxf-HAsvXnU3z4E1LlPdlelfYRJRK7NwIav1QY59ZCWbmtCdHc13ldUY8fze_v6-mEZiq3beh6hvLTiwZZ1qnWSBwO_FE2ROPnX6RuVfx_MFietcBdfNC4-OdgD4BZFOvwDKloygCHwbPIr2gR2WSr4NJ4X98hkJELDijE5JG_mkcWNK2h05JZbqkBYRJ3WH4rs85HONJdxvlka6q3NyLHTNi9eNvUUZbV9kXReiD3E3Yu0NK6_YBogno9z6KI47bWilyA3q2b7I7TkpueV3NaWixSLMVQmktLP4Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76a3469819.mp4?token=RVg6HcMhnSM_qbaJTME_5yjvpklwjBllRQam2OCtBB9HsVw4Wxf-HAsvXnU3z4E1LlPdlelfYRJRK7NwIav1QY59ZCWbmtCdHc13ldUY8fze_v6-mEZiq3beh6hvLTiwZZ1qnWSBwO_FE2ROPnX6RuVfx_MFietcBdfNC4-OdgD4BZFOvwDKloygCHwbPIr2gR2WSr4NJ4X98hkJELDijE5JG_mkcWNK2h05JZbqkBYRJ3WH4rs85HONJdxvlka6q3NyLHTNi9eNvUUZbV9kXReiD3E3Yu0NK6_YBogno9z6KI47bWilyA3q2b7I7TkpueV3NaWixSLMVQmktLP4Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینا حتی سطلای زبالشونم شادترین سطلای دنیا هستن
😞
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/101498" target="_blank">📅 22:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101497">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mP00UxQPW9izXPlUpkmwb18WKPBPwgVFwGNl8Dr7qHwjZZ8blZPA_W0VUnnfZZ2InS84EPg8P_XBNB1ILFsyGXqDnKYDXOKifPQA8sekdFlHLbWgXiGCf4fNervYOuG1VoNfxohdyNwp6n7wS4DOSqAapkWTRNN5pSKc5UKdonGbBYebZ7iq7Z67sCJOSFZNw7leF1F5UmH1ne2ZBu0V00YgZhwAa3VhLVL84sZvLNecnjNQuIvCgWCDqoO72GGkOwudFVzDPyvRl5FSQejzO4PVEFC71DeDA2zp5G2UfNc-AEwfDcEXGvD0l8b8v6F81OdEjI5CPxCkykN1-eb7aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاویه فکو که داری داداشششششش؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/101497" target="_blank">📅 22:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101492">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BBlfn9HhgOdlysDigbCKLF6xbNBCq-LSo0A0cHy7Hs-vOemXL_xIBs5a9Ibf-MHAUKQGxMM8nldkpkohVEEhZjwktcCQ7nWzoGfKxBmp_fS0PRXzhcA-fyPaeatJXa7i38hgsAEy1HiCJaTdcJZ-vTR1RxjOYMtuh9vIdFqO6KbVFKEUCWdyQ2LMoO1xiYiweSqV21Rqt8SkJxI1xpd27HKsjkAayJWNAFmA-Hfx6XqrMV3nQ-a9KiK9E-vDSKw0qJbDozpQr9suxcPqeHpiIK8oLJHaPaqT3_Ikc4eCG0C-Wlyoz6T2avJaYfhherz8gnHFiIcN8HwA0jDDTRhrEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jUe2wTpPVaMs5PYiPBoJbJ1r_YCVmIvbvx1SdFwv9QIEwYBj5jtMZmRM3byA_p2sLy9lURqo7dB1o9JhBgNfUm4LdJPsnnShC6SLs6VkZoEu39p4hAmhX5bLcrFoC98nisHiz85K3_Geobw3PqwUCVlgWcxg-HiQRjKhK7iCkQITVmZb8Sl3nuGHpqIkPnHlL-1irLkBNSqZI6jntgXm65MyCpdft3Y1a0zxoAx64uvFMsi_4jGRR6TSSfhm2cAbgEtbhhxhfnMSmkmxgZwXAodyryQV0EWw5_ISkMdVnB5uVjEX1XSoSZPVbJzJ7u20A1JA58vq6GlD2lIuw9Q0KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sfaRAyaUQtrbptCv_UVyh-olqeiDpMy4XAxRowsaSA4NdYWudbjPWmHIR_7xbvvaINwNGEoHgJkA-eKEu3gHslzG3W8VH1b8Dj_bMnEVAtT82ipNAYkLIH3YfylBU2Fa1Fj4jhZtwKEdG6eFRgEJ651u0hEp5JGLL9jKfnj8XUFb_DXEB0bWs7v23xvXD7OQXQPXusLLN6t95q7EwMHy7jgosKe7Uv5MIA44OGRAbzAgcELMaVUs2q6Z6lDqxvtrtMaqERHuq_lFMWdY3S7A2pZUJ0B9VETKVPMnNDD2bwLGcHHDjLgd2ni7lrej2MQTjGS9R3Avu0UA9cw8yT2CBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tp6JjLMEgN1RkdC0V1CwwDi69i_E_YiISIGwYdqBRktMfhMfrh9YsY-EXHep5GBnd_gPE9cMcqWbS2DQ1zZFHMpoatB_QpryB_83b5N0qfLDAHd6mH0bH2wnM4a7BkiuzPb4KFUbF5_nL-3OlitST3y43t58yPT88e04-0D9zNznwveuoQrt02Br-SHND2CcpVuOlgyjYt4iCHAvJbOefaM42KrzN-C3TTHB1dg_p8QUpFQMIv439XSiE0Mrtm6IWpqMF14acdm8yGmJdsR2pnie2LTBiBcCHsBtRMoDti1x2FqnNXWYII8Scrk4eA3GeK1NWmMqFuknEtAtfRvmFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bHyrjrwzpzxs3ibra_IUiEW_5iCZZqC8TOADX8LYUKFM5Ow0zkJX1H2dQfDrAsq-vP8ehSg2zHPCzCK3Iunp11-e25iimzM7c039B2vdxUsSNeQRkPJ2r9ShXPL4JLEasyxK-zujQHbgCjc9BFzLAYbuasqEiyxCmnNklE0T47aobJ099V5svXRLXzPKyNdhYklyAotV0A4k0BG6MNqc8_4i1JSIiQhco1LVGY6cn-gU2eeINdfdiHGpY_uNcJHCCFvmRAzSL558VPBRcq9lCNoI-747EtA2VI92P8WbAQFXO9Cci-61lixQNvRfNRhCOjgqqFXfElM2plOh98OQcw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
💥
تعطیلات تابستونی وینیسیوس و زیدش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/101492" target="_blank">📅 22:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101491">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf2aa4c289.mp4?token=H8mnx8XHGcXSGEAVDe-VtbTY9C3DZjfYUztr_Ph3nMP-QoIFQeZoS0M9M4PlCCfpYPmkkBTLdab1jQPn6JfLoz4gzerVBa7loToYHQflnIDRFdKEtaLw3EJxEyL19VtBbZEU7X6GtYA7ocYiaN0ncnKCxxevynl4_AtpY9OXnk3VCdLX8Xy_clZIikhNtW0xxIjetlhrNdSVantUDFRNBPrdpOOvK9vS0QxqzB5SF553OOGloMiu9JBKm9yBrAARDVLyjDNe1dyCzILoWCs90LI-1f-sBNUvWXupaJI4DBGUKo8uHcjWFVEqpq04ZFUhYMi5K3pdJgBh49O0crKE0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf2aa4c289.mp4?token=H8mnx8XHGcXSGEAVDe-VtbTY9C3DZjfYUztr_Ph3nMP-QoIFQeZoS0M9M4PlCCfpYPmkkBTLdab1jQPn6JfLoz4gzerVBa7loToYHQflnIDRFdKEtaLw3EJxEyL19VtBbZEU7X6GtYA7ocYiaN0ncnKCxxevynl4_AtpY9OXnk3VCdLX8Xy_clZIikhNtW0xxIjetlhrNdSVantUDFRNBPrdpOOvK9vS0QxqzB5SF553OOGloMiu9JBKm9yBrAARDVLyjDNe1dyCzILoWCs90LI-1f-sBNUvWXupaJI4DBGUKo8uHcjWFVEqpq04ZFUhYMi5K3pdJgBh49O0crKE0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"اصالت یعنی به ثروت برسی، اما حاضر باشی هزینه کنی برای کسانی که سال‌ها از آرزوهاشون گذشتن تا تو به آرزوهات برسی.
بعضی‌ها با ثروتشون دنبال دیده شدن هستن ولی بعضی‌ها دنبال جبران سال‌هایی هستن که پدر و مادرشون بی‌صدا از خودشون گذشتن.
شاید ارزش واقعی ثروت، به چیزهایی نباشه که برای خودت می‌خری؛ به لبخندی باشه که به روی لب ها میشونی و حمایت ودلگرمی ای که به دیگران میبخشی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/101491" target="_blank">📅 21:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101490">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZ3tzrkhdKingcEaL3K08W5I0jhWBw5u-FWO87XMNsIVGfLBqEeqW50ZHqrYuq1bUWSDiZq7nA_ykw0Rz_JRx0OX_7B8yFGuJmqG3nJFWrMypi9xq7GoW3TdSFICtKRoMkDFmX6AedXSStD0hav1py9NnKxfaNv33YTqud2_t_kA22Ow2q1Xe04xK4khZ8506CHiAiGgMetbQmewDBdL3Pnnqx4gpRkom2E8e8jqFAsVonX7JMkKs9ax8J8kmVSdeSiA5lGpPmCFO-Rc82gPEJrhAORtxcuxtXpX0CodZVY2zWH5acdyqIa6jwBT9Wnlc1a8I7nf8D1pHIMV33wOXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
تیم منتخب بدترین بازیکنان جام جهانی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/101490" target="_blank">📅 21:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101489">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0yf7YVUJwv7mdftk-_XQrKWZOD5Daln3EdxU-cC5TlR-PzwSvoyJlSH9nj2jT_noiWJJx2Urh76miQaV2b0oNIhtFAjM15pGEOertRkBLhMGN-SvLV_Z5S9vte5wGlVLYfbZZp5hXLKu3Px6kjKlin2sSExY70ovef-tE7dQFBbcNWDzlqYN_y3rjQ7plOGBQG5UJ_S4vWLlTv0oVXIKJCsLLWDVzrq-e5KaSultnyck3V2JXfwFh-7byWaM-T3_OepiPMU4nfmmmukHWGr2kBVfiIiNeXFvevqz4BO4ihmX9R4xo23LZZFqI4RqWtnPDQ2X26nAnFJqWI6Ij2A4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید وینی با چونه جدیدش.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/101489" target="_blank">📅 21:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101487">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CorIBqA6Mr77rijGkoH7FxHnx2om93RtX904FyxExpuSIkvxkc_01wLU4nGpkKKtkVWNa91dsXGyHMRpsNWEDBIjoSNIox1FukDZ0TFodjisHoDK-2b-ohVoLvYjpO4Zdk915BApqs7RQbrWY9tlWOTkyF_IbfRy80JG2lRwVNpw6uuEBBLtK_KHVDGT-RvACKDT-T5g9TgFA4EUnIsWzcA3k4OYCcLwF7XNXhqPyANmVvDIFWRWMPpIn4-hVbzvxEETRp0UJrYsTGOeGvqURyvFBVXJXDrLRURIU1SVy6MlCZ2z5qI_VfRa3E8PVkKVw8jhiiO-FwLLTuMg7NP6VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین گلزنان فصل 2025/26 در میان باشگاه‌ها و تیم‌های ملی در پنج لیگ برتر.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/101487" target="_blank">📅 21:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101486">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPvI0wtZ_fQrmfdFJWjJRdLnD6MRtaDgP5HaHEoY4UvfiDy1Jjof99yK0He4LyC1ZYhvBCCaH6zxfG8IdSbG139MtixPSSZ_DekHiS0qUmH1QigBmGbdFrOf3QKwdkmWASOdewpImAO2g9wmT0-s-gJLXRBXcGKbM-iEcrjXBI0vlT4L-B3l_x2vEVmFodda51ns_nu96RkV3_cHHNnB8ldTtYxc530KhJnGWM4SZQ6CfHUQRZqaEa_vkx8XmUpfZZWboEldaX8xk4r8opBXtUPTkIjnutp9HQUiuU3aQ6qb8idslh-_BR_WXHqnC3qhG4A9GgOLyFBFw1hMLSSv6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
رادیو کاتالونیا:
🔵
🔺
🔻
لاپورت جدیدترین بازیکنی است که خود را به بارسلونا پیشنهاد داده است. عوامل مربوط به بازیکن با لاپورتا در دالاس ملاقات کردند و ایده حضور در بارسلونا را مطرح کردند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101486" target="_blank">📅 21:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101484">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ShvMYb-2J3jxNhxOmwDHNRYvPcb67kkN38deUphTy2Vm8x8OBDJHXcLaxUVCujlI_VvYBZUNF5jxP_QENEbmYMvI-8g1hTBGVT7n9nPar40qAxbvkmUP2gRmGYVZ-Gx1ZjWiWRQbVyHXwfMfP4VQFSFoPGa2U5t-snFiaNi96irY8k1_azniRG0yuVsWKpshTSBm7GD6k0Y-cjmDVdeLbktSrYSkhvc75kFXlrjJiytSGv1u5xr30J85PX6GY1r9iLTG4GtvAnMXI0PJWC_ZZUv4ZhFwedpcu2HQCGNHUQVyPOjiHyF30e1Wz5TQd4mmoeBLh_oA779yg4pF0sAXAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RROoXNbqULBtxz_r9W9imW3Rne8dgM2kmbXDqkOtM_y4GGSConnneVA7EHUhJ3ro7855RSehaHUkgnTPGJvUBwmu418Lv6sfHVVfNnXgFNRcG6udl1DsWd40e0RI6CQ8UljP9x--0dX5lbzW6NR4VOkdxwbVrWPPTwM5NqQvfe5_tq5ENSjLn8kap8gopB6H3Srp-3oulDYBVlWL9b_zkuPYC6abPo206lSZqnhdzXae1hJImuLxQ4GvNHYt0CGQxBeX9HsjIEhMv7l1nGzl5iDbBpd-sN1-YKwRVLEHACZbeD5KSY6uvQN0LNA84-ci61OzqIQKG-yWGLu3kI2mig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😁
زیر بغل شکیرا از آینده‌مون تو ایران روشن‌تره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101484" target="_blank">📅 20:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101483">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEeHrxWF_qOGbkzPrdLrHNisc2IRrEnG2Q4tynGRuvAD4EFqbeoDT3oLocQ_l2_lDDokxA0Jml7I38yBsvuhKMbN5-NZ--a9JKfDV-spvsU_CS0Lr2Xg0KC_prY9JJlz7eTcR1Y08Bf5cSziLl21qsakY3Y3gsJ6DnKf1o-UQ0MxHE4rlckFJyrY2wLn4_XoVDMtIzwn7TFnmYvKqS-IASf_UnIzv4qk195fZNZap329cW4VatDMFtOXS4581P9dDFTj0W77-qrIz6JeEPKfTw9oUnCCFJILNOUY30lFLedyWs-Fh5KmF-m-kH9QWsvvA55ObLQ0rYAyNaAN0ATYNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔴
فوری از فابریزیو رومانو:
🔻
لوکا مودریچ قراردادشو یک فصل دیگه با میلان تمدید کرد.
𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101483" target="_blank">📅 20:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101482">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hupFBXvvoOtH62XHbsiu4UMo5LqV24rcVE8pWqBtEdXQXOzIhhH_i0vOxucdgMTF264gYRKXNyK14JDHw5wa_axBZ-orKfoLVgH173DRWlDpDi4UIAeRxH2YJXLscQbiq39YFW8xxWwsvUWlSJP55rXi7Al2pgnPt5-lv3ek1VMgkCBMLXJxergSIiBAlrQ5VILl1N3sP_o7q6wA_1rRWVFdDbg7KGKbAJPBhl0PXxwNLF4KYuujEssgp40Qg8zPXJuP8gxy3_ew63Xo_y_0uA79TqvVuabzA32wWCrGV0jSYlr1g8n0JnG7BbuGct0-s6VED0wCcc-HWniY3b7Eug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
||
بازیکنان جوان با بیشترین تعداد دریبل‌ موفق در تاریخ جام جهانی:
◉ 27 - لامینه یامال (2026)
👑
◎ 22 -
کیلیان امباپه (2018)
◎ 19 - جمال موسیالا (2022)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101482" target="_blank">📅 20:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101481">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krimAkQ83-bRuXR1CHzqvubXrDcqK3EEdliO8By6_S_2ihx1qw2M0hoLtqSUewEOCq9mAEq5IRPRVD2YE5M6G8NWCBXBtnhrwK16OI8uM5dXigu94iBOBz9pJ4BXk3lyaBWwCMU4zf_B-Y0mS0QAyT1ewNSxUun-fSS4dYBDFemgiQsAf0f1V1NGRi5jkFnvNS4eBHpabN13fUOl25IRjXw5G5ONEGJJMJue9GCNA5AsoF9jCwS2vnx-ceVwaKBUkdufbBuPI9JVqvg0lEGAqyG5Iisx2oNUPfi37INwb_Ns6nihM7oWeYGdQ5APN2Odtb3HSmYGkp3CLT_498jmUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیلیان امباپه کاور EA FC27
نوجوان و جوان ایرانی باید ۱۱۰ تا دلار ۱۹۰هزارتومنی برای خرید این بازی خرج کنه. تازه اگه فقط بخواد آفلاین بازیش کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101481" target="_blank">📅 20:39 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
