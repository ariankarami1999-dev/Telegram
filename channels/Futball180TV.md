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
<img src="https://cdn5.telesco.pe/file/a6TQU73zpo7YSwFtau3smlKrkw8KjNq9ZO6rEtloE4-ELkmHJU859mNADUSa2RQLl0LYQD8H86HSqKqFlfxpEjNoHWYO4CtETlv3CIvcuGfXwDga7aykBMx-IPEExu--xBdkyz-FHXqBuwdoixSv-g2u7eYgPFX7PVNz31_jaSeYbRU1Qspi_MxrjsdMXz_JoncDCSdE5dUtoyuA_AB5SunzL6nJLD7dbzHoRO-z04t-ublL6CUdLjvntt7Th94_rG7qTv52GuWuaAzxpX9VcXgTUKJMyDmAK6RLnu5_hnecrgGIVcnLN2pfJj-ML3JrgmcaYeupBpzQUmWIAe1IGQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 593K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 21:55:24</div>
<hr>

<div class="tg-post" id="msg-99595">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgOW3jeDYDWjv37TkeMdkqpIAfvU5bP4REZ5hWv1z2ciChPlO7lVoAAdi9nYskaxBLGFy6yiK0Y4t_yD8_fJl22nnUGvDIT7tYneARKBmWeNruU7tfvRd24_vY9ydQp5u5CxU8bcQoCuv-9p_pOYrviJfZ3o0nNplrFE9q6NBMUBFMBUr9jk_9Ugllpr2mKNWNRMXV-Dy9Qvz8fl_2Hr9UqqPLKzM-6C2Q9fZIIdgD7jgNU7pAEbQgUnkwlrmXVrA1LaSG2kZwyVo_G38z756RwrD_RoNCGfuCK1fCwzwdXfA9v761pv6RX_DMwxRq25olEGfeL2MrQf-kaloqwt3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جورجینا در کنار رونالدو با کپشن “Daddy
💘
” که میگه کریس حسابی حالش خوبه، نگرانش نباشید و برید به بگاییای خودتون برسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/Futball180TV/99595" target="_blank">📅 21:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99594">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/241daffc9d.mp4?token=qHFAa-k6AmwyiF6cxCTC13F8S1gG8Lzh3CvFSZ1Ke34LuElhK6D1hio_k6PAjpoCTtjt9IU4hW-J3t-fSOsJVpnu8eCIaR0qRJu0o9y71iVjAajwgjGXHkloSzUVzDEZBK3J4zNk9KftYOwrEv0-T8m_ocRyC7Qrkm_3UCcLQZ6I5fVPW8_f2BirAUCVXLxP6Cr1lgXDVeUkPG0o5iddxyhbhD97lFuS5aTkY7AQpSe6hFxRGHq9emUHai-whc_3kMvMBhe81TUjtn0JLjqScm45spgEfVvP4QlACA0pZlh2vCXOqA2-f-L0CnnPhqSIgCEGSiqDD0O4AdToNrjkxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/241daffc9d.mp4?token=qHFAa-k6AmwyiF6cxCTC13F8S1gG8Lzh3CvFSZ1Ke34LuElhK6D1hio_k6PAjpoCTtjt9IU4hW-J3t-fSOsJVpnu8eCIaR0qRJu0o9y71iVjAajwgjGXHkloSzUVzDEZBK3J4zNk9KftYOwrEv0-T8m_ocRyC7Qrkm_3UCcLQZ6I5fVPW8_f2BirAUCVXLxP6Cr1lgXDVeUkPG0o5iddxyhbhD97lFuS5aTkY7AQpSe6hFxRGHq9emUHai-whc_3kMvMBhe81TUjtn0JLjqScm45spgEfVvP4QlACA0pZlh2vCXOqA2-f-L0CnnPhqSIgCEGSiqDD0O4AdToNrjkxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😢
پیمان حدادی: نه‌تنها حقوقم را پس نمی‌دهم بلکه پاداش هم می‌خواهم!
وعده پس دادن حقوق در صورت عدم قهرمانی؟ حقوق سه سال من حدود ۳/۵ میلیارد می‌شود/ حقوق ماهیانه من فقط ۲۰۰ میلیون تومان است/ لیگ ادامه پیدا نکرد و هشت بازی دیگر باقی مانده بود/ برای اینکه دوماه تلاش کردم که تیم ششم جدول شانس سهمیه آسیایی داشته باشد، باید پاداش هم بگیرم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/Futball180TV/99594" target="_blank">📅 21:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99593">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/702b2e97d9.mp4?token=vagJU7kHKTbxGdygra3tjYonKT8GlKa2ExNbxUzk89By0nZ88-3RCcxmexDwNf-fbk6ZvnrMci1RRpaaqMZ5hhk6zKhAglqtcXC-Z7umak6gahxhZ5pUREDcT3JwAABdUUIsbUOPXe5zQR-WtEiNW0Fr14N9tkPGH82YAYd4niS_QD8bMbz1b8OvxnPV8TTdC7vvqEMtFeTOjX1nX3RCBADWdSonIzkIBh55zsKSyi5ujD5pFXExS44ROVPprUdffg1afcxclOmRu10kX-7Hb7sTFKC-qWcO12VdbyfGKXzDoAiyHzVXromynaAg5fjVt2xMHkugsE9IM0wBne7law" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/702b2e97d9.mp4?token=vagJU7kHKTbxGdygra3tjYonKT8GlKa2ExNbxUzk89By0nZ88-3RCcxmexDwNf-fbk6ZvnrMci1RRpaaqMZ5hhk6zKhAglqtcXC-Z7umak6gahxhZ5pUREDcT3JwAABdUUIsbUOPXe5zQR-WtEiNW0Fr14N9tkPGH82YAYd4niS_QD8bMbz1b8OvxnPV8TTdC7vvqEMtFeTOjX1nX3RCBADWdSonIzkIBh55zsKSyi5ujD5pFXExS44ROVPprUdffg1afcxclOmRu10kX-7Hb7sTFKC-qWcO12VdbyfGKXzDoAiyHzVXromynaAg5fjVt2xMHkugsE9IM0wBne7law" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇬
استقبال رئیس‌جمهور مصر از اعضای تیم فوتبال این کشور در بدو ورود به مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/Futball180TV/99593" target="_blank">📅 21:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99592">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9FLSEzwLIZvPYiXHRCp_WOZRujrb43fIJFQBUsbqfZx5mZ57NQXBFcV9owpIISeOEe1lPeyBo2ctXLIcLlQe6hqX_KR_Hhn6QrWScQjceyPWP2ZxG6qrGzwtOIJP-pZP1rTKRVbyj_gC41Fv8Wsbw5U25u-kPbSxHvF0mixuXzO9LpJJUOCNilHEbIRXBtvnf4l4IB2lJYhotCo5zL7w1beKJ5VVCUUYzSqy4nvc4GefcNHcn5--eatZSJVKedaJxWJKmT-e9JPBkGx_hiKiwbW_l_y3qjGJdwujFfaecPMPLkuPWszNbLT2LR33zYnWZO3DOdT7qRnkC5k9k0bIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📰
اسکای اسپورت:
🏴󠁧󠁢󠁥󠁮󠁧󠁿
باشگاه منچستر یونایتد گزارش‌هایی را که حاکی از لغو قرارداد با ادرسون است را تکذیب کرد و اعلام نمود که همه چیز طبق برنامه پیش می‌رود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/Futball180TV/99592" target="_blank">📅 21:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99591">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/773137bee7.mp4?token=qlWOGWabnYwJ-LB0E09h5G5E1GJoYCOFk3P-RLUnJAk769hvbZX75D4-I4iqCD7_GXqHU2SSsJpBY2wri83gkbZLUTO969hsgf0BJ8EBt5bzpUYdkdR2KwfZU6RkHHaFYU5UocwnMZVMa4ZCU-a-mzwrEJ2xeljFMbC95EmlYzZ620S1bkwIus0a5k_HolevRVh4mdyibT88KcO_4X-LHdhhfe9lElOTwWhwz5E9fcf5cPQlqFub63Ta2n2gYt-mtvPfnZ5T_5ZRom4OSk_B-QidKs-Eif_fRGBQR9KoMQOfAsb7NzKcfMffTCsorrMxwR6FzJCKZKQaGL5TMKKNNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/773137bee7.mp4?token=qlWOGWabnYwJ-LB0E09h5G5E1GJoYCOFk3P-RLUnJAk769hvbZX75D4-I4iqCD7_GXqHU2SSsJpBY2wri83gkbZLUTO969hsgf0BJ8EBt5bzpUYdkdR2KwfZU6RkHHaFYU5UocwnMZVMa4ZCU-a-mzwrEJ2xeljFMbC95EmlYzZ620S1bkwIus0a5k_HolevRVh4mdyibT88KcO_4X-LHdhhfe9lElOTwWhwz5E9fcf5cPQlqFub63Ta2n2gYt-mtvPfnZ5T_5ZRom4OSk_B-QidKs-Eif_fRGBQR9KoMQOfAsb7NzKcfMffTCsorrMxwR6FzJCKZKQaGL5TMKKNNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
💥
وقتی عادل فردوسی‌پور هم از ناز و عشوه شکیرا ذوق‌زده میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/Futball180TV/99591" target="_blank">📅 21:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99590">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBi4xUzdf-yO9y57d5ASqxZOEsLlZ5Mj5PlU0gdVwYwH2yOKMfnzjm8d-raWpbFqnNwx6dhA7MZ9ZrGw4wWGYD61tR0PNumwE6CwZrKuWl4wndSAjVBh2XC3Fquvrxcd5DRd9de_ssJhY1TB57wu_zYgy4w8H0Wd3RMQRnZf1w1ASu-oI6XOI2wF2mLhgear74SbpAu6TDmJrBAPtINop8sJkM2NwU9XIidNHSErWP8NLmFjq2dWv_7whT7Sc4NNXu1kStoAUzr8NIuu-7dx98RpNgunuWtb7J1aCO1dqtVmji108aDAZTUld2fdTQ3vLgoKFA3JtqrCchNz82LKig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
ژابی آلونسو افکت؛ او فقط مربیگری نمیکنه، رفاقت میکنه.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/99590" target="_blank">📅 20:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99589">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyK7wm743sMHZE1TTKe63nlfh7j0K1ziUL58CRpxY_pP7wUJ37jdAi-q6Bg74qJ0y3PQ1PnTmVf4jFjxJSg9SRdtUQdsljku54V-z7YkFsGVtavhjbGB6uyNT3PEEOFGHQcpK-VEug8KrV88x3Q5ce1H4pj-7bSBvY6Dk964e63j4ip_HWCsgdApCIUxt83RHlNYixncYNTd1l-9qD2wmhun0H1ZkGzTVBFwtOxrf_fePnsC-OlekAf49r-D81nrt07bkdWLdTuXG_sy3_eYHheiEvBl1x77HiC4zIpxiGuOKZzZakJDD3BiMgpE3uUJeBHdnGBBm1d58eNgEbqjCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
#فوووووری
؛ کارتل‌های مواد مخدر و اشرار کلمبیا در پیام‌های خصوصی به کامباز بازیکن این کشور بدلیل از دست دادن موقعیت تک به تک در دیدار با سوئیس این بازیکن رو تهدید به قتل کردن و گفتن که در این کشور حاضر نشه وگرنه به قتل میرسه
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/99589" target="_blank">📅 20:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99588">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9Kek5HXsHW2DJe0gck9kzy7Cw6aaggVitzxiUjWos3Hr9nihaicdMncj98y9dl3UUMCCluurRweuHVXg1mzLP2w87iPKwVIij3r15MLWagXvseYyoY9Xrh-HNM0GXlPCHQeQ43Oda0FP7B5b1VxhoZruv34th6QOOhd6F3e7EHas8R7fbNO262HAVsVauHNpJMEMPBZTiRc1JebutDN4z3lngKuqHwGCvFIGfUFsHxn9Q342YU1Lp-FOkSytlsc6sqtiQkaLURa9e3be-j8ftxczRAGlJkE8-OywefGgJraQD3v7YO5YyhFRZUBX05wxSqZb8QZ6J5sH482niguiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
مسی همچنان ادامه میده یا به این قاب میپیونده:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/99588" target="_blank">📅 20:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99587">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80421a357f.mp4?token=YbXx9OrIEhZ9hlUH4h0EW1v2ucjK0zeowp1iHSfFdAvluAD4ZH4VEZ-Y_hI-w8WFUCDMPU5crwz7LmE0_TCPV84PuatV21EtxHah_B8lXUj21SRH3r_AVK0NWC5R7QVfwDEMvJrKF1VOQUg0pYvuVDAlo8BOKL90BlRKiErB4Z39sZAYwX2ZVzu3QqlTDCoSGz9-KoI9CfC6rkpxcvuSo062OD4jcTalhHyLgPNxNcTRFsvydRO1Ju1PQFKelvV-VWy3eyZZbAJebBmd_wMKDuslwAmJ6nzpdRl0YOtT69okPLyxRadrJksDxvlMrJu7GFV6NMo51HzR--W__xT9bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80421a357f.mp4?token=YbXx9OrIEhZ9hlUH4h0EW1v2ucjK0zeowp1iHSfFdAvluAD4ZH4VEZ-Y_hI-w8WFUCDMPU5crwz7LmE0_TCPV84PuatV21EtxHah_B8lXUj21SRH3r_AVK0NWC5R7QVfwDEMvJrKF1VOQUg0pYvuVDAlo8BOKL90BlRKiErB4Z39sZAYwX2ZVzu3QqlTDCoSGz9-KoI9CfC6rkpxcvuSo062OD4jcTalhHyLgPNxNcTRFsvydRO1Ju1PQFKelvV-VWy3eyZZbAJebBmd_wMKDuslwAmJ6nzpdRl0YOtT69okPLyxRadrJksDxvlMrJu7GFV6NMo51HzR--W__xT9bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله مردم به مجریان صداوسیما در مشهد
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/99587" target="_blank">📅 20:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99586">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLW9vKaPDfKYhilnbu5P8HI4H8okQ4_m-Ikk_uohmt8tfnXtUEIkt1XiJxLg9RjmEvLa-XU3ZDdZRuSLtDQtvjHPD-HVRGErtkUbClIQOmuQ70_iqtSZK5xZtk_dfH0Uj5yY3AgeFt2NJjKzKdFAH70dqM6dSASTaAtnblcEGRNmpTNfXwSrsGCKjwHGGRbmDJNXmLQL_ooqBG29SyJwY7ePwc8r_0w23h4Wz-vC-HBLvv2PvCO1I8bOCdm6Tl37anvEeXw5w4mODIN9iNybpwhaDXIf_doCRjwfzpUPUKU0_2u2Gu7pp90QBAYgXug1L8fqT8-ofBD3B_61z3x9Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
🗞
رومانو: الکس خیمنز مهاجم بورنموث با عقد قراردادی به فیورنتینا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/99586" target="_blank">📅 20:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99585">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">با رومابت
✅
بازی های
#جام_جهانی
رو با کمترین ریسک پیشبینی کن
😍
⚽️
انگلیس
-
نروژ
آدرس ثبت نام
👇
✅
https://halvirox9371.bar
ادرس کانال تلگرام
👇
💠
@RomaBet_official</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/99585" target="_blank">📅 20:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99584">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wb8mL9bcp6k0_pe7Z3I7ywGyIcgzyfUKaaj1a1aOyFFh97aHAlIJ6hksB4Agm_4mD3XO_Ypkd1hjjWGcvir6sVlR0KsTgRLd41hkwAAl9AoluP1igg_gCkdEgCQNgGFL2tdRPa9gRu6hFzrBi5AhIhlHGurE_my9HocCUALtKUF2UlfGCSpyUCr60YrRQTvAOuU4T1AUlTDrcz84cXH92NqKA70cRYKczFLXBx8VnGpHOznfnb-NGBe8YedyDDHsjfxYp3t4Z02ec3e3fDOCz_PySitbdODWBudBH1XMcDZSVhHEKw0KOqUd_wZhRyenPBOThJMRUMSMBvs8KPJxow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مسابقات جام جهانی 2026
⚽️
🏛️
رومابت دنیای آفر ها و بونوس های ورزشی و کازینویی میباشد
✅
🎁
با شرطبندی روی مسابقات جام جهانی وارد تورنومنت 2.500.000.000 تومانی رومابت شوید
✅
#میلیاردی
🚨
همین حالا وارد حساب کاربری شوید و شرط مورد نظر خود را ثبت کنید
👇
🌐
https://halvirox9371.bar
✅
کانال تلگرامی
#رومابت
👇
G20
🔵
@RomaBet_official</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/99584" target="_blank">📅 20:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99583">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b93b2a590d.mp4?token=qQ5VZST70zXsDfrnRecFHMiCW2_ZxrzsubTNNk5u7Z0uEBn0ZoLS2uMIVTm7FZSXe46giMQKpPQX2hQE_Uzcvf3AOkgK9bn4AKCiJePNE977uLy22FR7dWkKyEBB1_8Nu-Cicim7sDkIz8uOf5wkP3g4WIuvzrKIdWtfAqFEqebNc0-xLtXzYhgAgmYXKC3oQ6G-nqlI0lXXQV7DfBwXs4bJiUg5R_lzqtl-jm-Mk3C-nQRstZ1CBLw17S05tplRGSRp8p_xXA6Digm_3-MMjzWYQm4ft346snerOChudEbI-6h27LAfZWOuDrV0YOLRqP4xJWMJx1A3BjFCmemRsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b93b2a590d.mp4?token=qQ5VZST70zXsDfrnRecFHMiCW2_ZxrzsubTNNk5u7Z0uEBn0ZoLS2uMIVTm7FZSXe46giMQKpPQX2hQE_Uzcvf3AOkgK9bn4AKCiJePNE977uLy22FR7dWkKyEBB1_8Nu-Cicim7sDkIz8uOf5wkP3g4WIuvzrKIdWtfAqFEqebNc0-xLtXzYhgAgmYXKC3oQ6G-nqlI0lXXQV7DfBwXs4bJiUg5R_lzqtl-jm-Mk3C-nQRstZ1CBLw17S05tplRGSRp8p_xXA6Digm_3-MMjzWYQm4ft346snerOChudEbI-6h27LAfZWOuDrV0YOLRqP4xJWMJx1A3BjFCmemRsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏆
نصرت سر آشپز معروف تو حاشیه جام‌جهانی برا یامال نمایش راه انداخته
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/99583" target="_blank">📅 20:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99582">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SO9n0pLA-5er3QsEwMA7CIAOW8JTKCB-_VihKob4GE6LE8BwV6Uiq4c2wwS0cp0sNl447By2p6n69lquAsVQTImoVh4_cn77whw5Xh9wHnU3WPzwzkZ2fFdt2X-ic6K0glzG2YGZAh5EDwHB2gRPoEwY4MZsuLRv9Vu2DGVr_U18LFHpsZLAdwyGIK9XtVbe4xRZNDKq-r6AiKqWoRc_nOBBsFRqIACIVTUIISEsJaIIEGumcscqPnP-0DTgDnAeTcGUqPeTAH2Ne7tk2AHoM3iIVP4H6kjKzmnQnMlbFEQiha-HLQfxZmlo6TtF1HZgw09x3xQbhuCiS0QTK34vdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
هادی حبیبی‌نژاد ستاره چادرملو اردکان با رد پیشنهاد سپاهان به تراکتور تبریز پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/99582" target="_blank">📅 20:18 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99581">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rrq-v8HS8Bw9-kIH7Xyb96BEm6Le0WtCGHGUBQnAaL7axkCUqwOaDcBg9N6_eb_xWFyPn2p_xkl6hQbMpgGgH5dpxJDWnw7qOar4-eJaJLZZ3zPFUXhseWpTxK0BDfsyv02DO88zn9pPLNCRTW-82V2wLy8kkg2MA4zexJVZlg9VUKAmXA0NNWSyhj8VWvSiAlDpdr572JZOMGqsR6AYxTHB-Tk2zCcLCh3y4FgJbnTa26F5kigF7Ytc4pYuLPBI4b3n5rDO7jLQAtNyZclnRxs3VFzrvZjcqr5p42fOlFouzkmfWs46WRoxcuf6V7UzMyCGN73uH5-e-2T8dtxmVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
#فوووووری
؛ باشگاه الاهلی عربستان با ترینکائو بازیکن سابق بارسلونا به توافق نهایی رسید و رقم ۵۰ میلیون یورو به اسپورتینگ لیسبون پرداخت خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/99581" target="_blank">📅 20:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99580">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5GM2g_ymB-GfMPqH9UotXJ0DuKf4dLOynCXuJBX_GZ9xaOHjt7sLQpbRLeMQKKLBkup7kwiMMbWEmAlqQXMIyL8ObdJrqirGSSJpYawCAdMKEziSRInbN06p1uRVkx6_OokalmbbbgWNi6bnZK8Tkeet5ecRfz0H5ML047ZExIUaTIeir7b7UMdlRNU5sJeh1uWlLe6lQVMv5mzkHWl51wE5OD9f5sz9jRE3GHpk7kLdketGl9XLE6WbMn-4GoELMXMmUzIKcaqrEjKrAn6giMAEo7Zi0_D3duPV_4qZg1q1HFkUK3kN_EHYw6n6QbIRje6usWbgmtNPnUl08afvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏆
🇳🇴
دیلی‌میل انگلیس: دلیل گرمای شدید در آمریکا، احتمال داره بازی امشب انگلیس و نروژ با تاخیر شروع بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/99580" target="_blank">📅 20:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99579">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tC-0BeRDxQsqVjlyvHSuKqdiemkCK8B87RHvcq5Y1oieEQ4ARDuECrannarVx1DUSbleIkdLRcCl3VcG725Naef1VUWSVNSOyBABksP15J8DPc8wJ4hEIp6LT_BThAheWvuLOPIloKz1E7VHHUU4NEb-77p6qKrZCJQEy93-S0UfzoOOAUU9CPaqjtRdMlMuBGTOrQMhSgQ7rvBjZRULgoGwUHlhKZvftYXorjIRhpUNLqOrDde459qKbcDLifxwWUoFjjFVkXhVi4E6rYB_H_3fYkyO_eYZxo9LNcC65ni-DyoWbnB1B7ZRLPQmDNUSYHi7_ENZ-srnjWRAZwdYSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
با اعلام باشگاه پرسپولیس، قرارداد امید عالیشاه با سرخپوشان به صورت توافقی فسخ شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/99579" target="_blank">📅 19:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99578">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXk4t7JhzNYXbt6ptxZDynOyOUrV2U1IVSkTN5YiONed1dVbRFMWPAfDMsPfP8QvuotIrktCZXIVLz7yZPphmw9nCgDl6G3ZkkZfFv-thJetUKWPMHkTU4RkKT52qR8gQWC67O68Z-qjPiXobeS9AFaUqTEcv9S_0V12XXf0MziVmSbwz6JeCR4cewzg9s7NSsl0hlLsCZ5yMagA-I_dADKKbhdFyv71s4oANhpe30OQ6XZIsWLK1R1K3wYGqOQLrvJbxSunNYma1wugmgA609EdFGfdSPDwTR8D4Fgvpvix7iWxalSo46DMtqzvTdUXdE7_31Nphg3ADSIbVVpXIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
با اعلام باشگاه پرسپولیس، قرارداد میلاد سرلک با سرخپوشان به صورت توافقی فسخ شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/99578" target="_blank">📅 19:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99577">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rl95RdFuZXLFZ4IT2sFY7whFroz3mxoSTRL_zdfvRn5iQk7nBqjUqQLbKjKy3XRJmCYlm9BZh0qk0ilJ1XAvwN2MRAMBaM4QIG7yr418gjmpimJjp-HCFsE_hyfqDeFb4kRmkPB5_sAqYM3CoDvE8GzdNDhzWZlvA6eNHwC1fXPRvTKjcxFIEAj_EjooUipktJANmXW1Ai5E1gy7Wi98-z6V2ZUZYPcZQUfjwAi7ktOwz-n7mXcq13nYFAzzAOxl0kCIWLnIFZ0ZnRWY0wHcSuwKf0R5nluY0RWqaR2n7W019HdSHKU2kBqLh6jIoZX0IAmcbpe8Og7UCh3SQV-_Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🔴
مدیریت بانک‌شهر بدنبال ایجاد تغییراتی در بدنه مدیریتی باشگاه پرسپولیس است و اگر اتفاق خاصی رخ ندهد احتمالا پیمان حدادی بزودی از مدیرعاملی سرخپوشان جدا خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/99577" target="_blank">📅 19:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99576">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tf_4qNKKyI9wcdAz30JBTGb6GhD0UaM0EiSAxxbxNjCdlEF0kIZEe1fmdU5-71GO7tEOWa1N6H_AR-e8eZnmUWVQFNje6JptEriqloflhppTYJORmAY_42TwneLu9wuoSnZfWcepbgTzC_xZER_e67KutkVSytqd6a92Dc8jUasn9egqT8VVi18675My49mCgrS-lE4WACPxNDUphWwjmhZ4IhMNgsHVkZ7Rc-cTxCr13LTg_igS4Vdq6Zx_HWgOS1igPTBeL6Q34IU14jP5np9uktXxD3GPK-RUmMPp4WnzKRWw8fi_4mpmwAR4ZhZF9W7Ul0OJ8dPfWvp2zDyjUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
تیم‌های ایرانی بدلیل احتمال از سرگیری جنگ از میزبانی در آسیا محروم شدند. عراق، تاجیکستان و قرقیزستان گزینه‌های میزبانی تراکتور و استقلال در آسیا هستند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/99576" target="_blank">📅 19:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99575">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏆
🇳🇴
دیلی‌میل انگلیس: دلیل گرمای شدید در آمریکا، احتمال داره بازی امشب انگلیس و نروژ با تاخیر شروع بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/99575" target="_blank">📅 19:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99574">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vV9VQfrpxhTswVcMReKsWmeXgbfy_u3xJyXjsrltL9z_sogNAfHt5WUZVcwxWRO1AdEzBOamc6IsbRf2yUH1lk7mi5NDBpjkqRNWO8S8Jge9J_XWI9fBaoKB2uc2zJ4wgmWQXZ4R6OSjLldAghoIwKUpfI73KtriTza-i5_MePtJ94V7Box1kEnrCJG40FFq26hUbgHjvrZtp21TzUuHADgx4dLwD5MrNJ6wZMlYQeWFHpBcx2gy3NeTPADu_vCXQAuKrCZKAbwliBd8uFeiAkhoeCHGCMezOz_aKprY5Cea2qSDsbzX7vUSR05aLSmLrhZGI5EK4UxNkyUZgzZklw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور در برنامه ماهواره‌ای دردسرساز شد/ براساس شنیده‌ها برخورد با فیروز کریمی در دستور کار قرار گرفت
🔹
بر اساس اطلاعات رسیده به خبرنگار مهر یکی از نهادهای امنیتی برای حضور فیروز کریمی در  یکی از شبکه‌های ماهواره‌ای گردش کار قضایی برای برخورد با وی را تهیه کرده و در دست اقدام قرار داده است.
🔹
قبل از شروع جام جهانی نهادهای مربوط به برخی چهره‌ها تذکرات لازم مبنی بر ممنوعیت قطعی حضور در شبکه‌های ماهواره‌ای را داده بودند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/99574" target="_blank">📅 19:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99573">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYwEa5OBSvh-nQGnzh9GyeVeDmkCpAbRD5H085VOz2XKSDG6fxLeOpWJ-FttRSYBA8aqF2OgdRruqPT5oWd5fCgc_WMHbjIR3iJ2s-HTrdev_JHNOPbxp7dFeyzH_SxSW9z-ntkotnAC-60TMei2ecq-0Uceuf1N-AtQeL4EAl7gZ2T6l7p6SZ8IpEGVjqKPxSE--7hOs-K0Yo3k5eTvlYg82fh3_hxG8lBD1q29wlX_PDrvsjHiZ-dgWx23OLlGxpwSUlkBkt79XAxMO46gYC2tkyJrUgqjaCB63U68wqdyFAyH29ecIgCyZ-4Eu27XwFitoQg4pKpZyBo_ft5QbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوئیس هرگز آرژانتین را شکست نداده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/99573" target="_blank">📅 19:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99572">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E57KrMvk_j29yrWrTQXXrN8HamLMnmL2_ZSIBps3Vd2A_e9MoZCQqx9oIZqh-lYUv8-adyMm_pbQivVM4brwL15mH-_MjzGMJcVAlm63uZS4_x26PDPH4gpotoO4kHCbCxJlgzkv6tAC19_d5d9pKCCkrtN5aO8WkM9zjHG6-7KV3ZOemeyBJuvcJR3yeR9EnX1z4mGiHNaSfNsQ9jdYPTkDysPiuPyaYrc7OcWxPd319yATroz0oRi57JqcBVjy_tWmoFXmKsqppnsdjv0eHIbneyq_QZCUC-hpHO5TujudrFpj8CwlE0E3lQqTmhVgtlrOMx00vdUfe8BKLRg4xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
کیف 45 هزار دلاری هالند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/99572" target="_blank">📅 18:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99571">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bk8Ol5nn_ie-iTC1Qp5RteOYLsDa_aWNc2gkF5xa2TjgcF179zAWnxFzo1IP5CQdrWmTnBW_y-MvQCctntfGjGsOoJoy0ti_o4DE-AjfN_igA3E1-QYKSFXByLIUaqt0a4jdOY3lmo2ePBhvFJs-_PR4DmBVkLrCvyW2UyYBtAHU-i1G4S_ixosa8HT0tEp1AtpKjMsWRDR8UNl_GAS5zrR_bojSUvjjtTFmFIFs4MZjNQXFbXMoKFgnFv4cz-a5dYr4o8uVAnMoyzOnoZ4YZGwVHGahvxg6DD3VhCKcjWfIC1yF7crmaD_IXvQX90keM-VuhiIEway_Mi26NDhn8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
میزان شرط ها روی تیم ملی فرانسه بشدت افزایش پیدا کرده و با اختلاف شانس اول قهرمانی محسوب میشن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/99571" target="_blank">📅 18:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99570">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVJKcWqEtekPYtpnp0HYgGMK5KzRVXqLvgNUC51N2XSX9K5OLq3d_yawF8Vlc4Z9jVcokYYbIQWDxEtJmiLPLu28Dlz4zuj6eCiKyjU82xtJIyo1a0B4pRjmkEBFwfmPYg155cKuc-k8qTp6GGCZaWlIjslvBtuDieqDYdvGsbZYzuzxDG4H2za7jDwPTlhwsCnGGxuqe94a7IqCCAnZ0g9n847MDU3ORYac5lAuJELaE3d8XK7t13lIp6JcJ7vl9G1b7eVlFsW5WMDDNsRXqBEil26jTETA-R4A2HhmrPVA2d5mDeW9Btp8clvZbKmKaz8ThAzu1Kv1VsanPsvXCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این آمار نشان‌دهنده میزان مشارکت هری کین کاپیتان تیم ملی انگلیس در ایجاد موقعیت‌های گلزنی و حرکاتش در زمین در طول مسابقات این تیم در این رقابت‌ها است.
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/99570" target="_blank">📅 18:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99569">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y6j7Z3412I99Vd2p1YVILP1hdjJCxmjiYEdtIrSSRuIQrOQEWsMLgLKOh39I_UxtDSAMF8RDWIeYfhB-BEzVXsGSmYyVxpCV6DeE5VSwUDltuiQwIxop8YtZpHhzHSeCB2Ox0oTyEQkVVCmJOo-WWkycByBgvkxOjinJcPkFrFTmvQuAYx1dIlji3pFj5zUu19IXrBJNf1uG7RB4ZXj42wZB6KcttVFR5xpKUC5I9tN9jt5GUddJVsJdwtMe5QD5Zaoc2gpl-UBV5NEsgQqgaMhBrqv99-mnRejnkLfS3fe3TOKuaSVP37vvfI3w6VSfg7P9YXLhVqdLQaBx6Svuvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🗣
دومینیک سوبوسلای:
- من مطمئنم که ما توانایی رقابت را داریم و امیدوارم که با مربی جدید، آندونی ایراولا، در مسیر درستی قرار بگیریم.
🔥
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/99569" target="_blank">📅 18:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99568">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmV2GToeLw4unrSqfUz07d7T-EjSfX9GPcBuFx95wOdMWrfuUJRbVY2Iu9BzHiW4GsY2-gNgn0w3_-IRCz084Ar9UGGN9SpIm9D5YAAVPs9CMYiN8NIWkNRWlbgnrOaCw9kjNC0W3m8sbPSHHxKYF-SPRTgrJzitBCD6veaxChjy4DesblJuOb9kyvV-kJseBhJxhH90HhUqyFWNjxlxNEhY3Jpso5PoKnZrmZFsVpPA72zNSXI_MAKPu0EAhZioszEDcEgO-jtdfWMaLFHCVPJlzntrLy8nwudHfP2gteMAtGGIpbWp6TTv5-WkvJQzw9Ednci7uuLFTH4kIdJGSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
آمار لیونل مسی در مقابل تیم‌های اروپایی در مسابقات جام جهانی، در طول تمامی حضورهایش:
• [18] بازی.
• [9] گل.
• [6] پاس گل.
• [15] مشارکت (گل یا پاس گل).
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/99568" target="_blank">📅 17:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99567">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3ebd7973c.mp4?token=OGiTf2cm_WDMuOGix8r6aOS77hjvldoBNzXgNtVTzineR8V3tv-PczPNQb9PgeeHIPCEA_FbSaeB519NxuZ9HnZ3ZKBD8q6BT5KSReyFT1gbjn4QMVSNK7SvA2at-6n5nAKSATNuIGv4GmlNFmqZYKIAQeFUOJod0UkNg4Dnm8Qw4WxohKHs41iptZgM6DS55PUJJekTXq0cD6j7mAjxslxsT_o-6qULwvcBCDAp2mFAmbfvLPmS_wDamUS8KLcz1MARz7qYObTXZvJgtC8Khxf2-FgGwdgAoEdUUcshVMiP2NBPvLHkgmcwspKrypUDxUzFxgWpp1FVHTvdDNDMdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3ebd7973c.mp4?token=OGiTf2cm_WDMuOGix8r6aOS77hjvldoBNzXgNtVTzineR8V3tv-PczPNQb9PgeeHIPCEA_FbSaeB519NxuZ9HnZ3ZKBD8q6BT5KSReyFT1gbjn4QMVSNK7SvA2at-6n5nAKSATNuIGv4GmlNFmqZYKIAQeFUOJod0UkNg4Dnm8Qw4WxohKHs41iptZgM6DS55PUJJekTXq0cD6j7mAjxslxsT_o-6qULwvcBCDAp2mFAmbfvLPmS_wDamUS8KLcz1MARz7qYObTXZvJgtC8Khxf2-FgGwdgAoEdUUcshVMiP2NBPvLHkgmcwspKrypUDxUzFxgWpp1FVHTvdDNDMdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
محتوای خوابایی که میبینیم:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/99567" target="_blank">📅 17:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99566">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uO8foidMWrGdYoEK2dGDFGOCqD5n5EB0Qnp2XDC6HjVhuh3bvg_urIIILiCLNEsTWRhVcCYuI0TIsHv4GVS3zGV0Pjup_kqbxwVaEPqDnly6IWeyDNBZei3DqECcBsy8WYiTAAvDtYFYpui3p5cU4snoVzTmNuLaB-c9Lp_l9PWUiVpVXDKzZyK32rJbmQQLwG3TFGVJDOBz4wgosBEDalhgiuriIMz2qaKE8pmn_npjP6DxribxlksrV_2pcsknqc5ujKrg6WN-hITOyRt9zpq-VWePl8DxzU2eRzizO80Y7-Jfh4tJFrIq5w7b5EIYKlPlZvxb7xSJBV7_-KcnAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
⌛
| مقایسه باورنکردنی کریر رونالدو نازاریو و امباپه:
🔺
امباپه:
🔵
590 بازی
🔵
440 گل
🔵
183 پاس گل
🔻
رونالدو نازاریو:
🔴
598 بازی
🔴
392 گل
🔴
115 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/99566" target="_blank">📅 17:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99565">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAWn61dZTkOT1QxIaiOdbj82GR5Ld-EXxaTxU437Mco6-kPWi4m5mDE7JQOAaUJZCJKsooxbPtepcIypklv8DPMuWOeu5UOFemTQXNIFruMmPkV2dxnSJV-KuzXEWb7z0rtFW7WZ8K5ubOXRg-J9LbJXDL7uAeIVOvVp27fgZFhoRnGeU0hf7GM3R6Sa4Z_hdqjOBzMhqdOo6tjIMBIDfaattjPWyqUMKyBIALV92QEkBMnOchgLcBCZzIdV7fYSA8Ueh_kAXKT7pj2ZLSzUXWLrr-kuBurZzQGKkJ4D9O9DQ2DrmAY8mFHhV1iD4ak9JVoM1WZ5W8U2nAHfxwK6rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرینو وقتی میبینه تو تیم حریف یه اسطوره محبوب حضور داره که در صورت باخت باید از فوتبال خداحافظی کنه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/99565" target="_blank">📅 17:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99564">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRLneVlh8hNiwoX6vCWyaJVi0u91RHvd08orl5zAcYKWl6VkZFzoZaf0Y4XZ8K1_w-JBFWzRxXvz6AdInngSOwFrkexmo4Z9qUfDgyJOrjDgD2v9DkRo3Dc2DKzZaNb6SIPc13v2yutnw3UE6kONKbEkJueLVJUSfofbi7pCSuQPQ68wnpPl_FATVLTi_eu592tWth82iWxoocRYWRyaex40btauJ_7TTEnlFU79ua8H03d-6Ovn9qZDEVoPEo1-knhiX7FM5ggNkDmnCen4gCt6lgtSWt7RIZwRvqrOD-cYb-Vh0DxHgEP9O9mtdpS3go2PolTudubg_W2X1su-Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
🚨
🇿🇦
جیدن آدامز در ۲۵ سالگی درگذشت
جیدن آدامز، هافبک ۲۵ ساله تیم ملی آفریقای جنوبی و باشگاه ماملودی سان‌داونز، تنها چند هفته پس از حضور در جام جهانی ۲۰۲۶، درگذشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/99564" target="_blank">📅 16:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99563">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bbdc557e5.mp4?token=Nl630VfpQunY9__QnuBVxb7eBHTFHHFE5DWfMJhSiJDHZUbH13kQhZQc9HVYkg8qqk7zaIMULs3DRcCFygJzCJZmMTbrA-mQICYaffmXPT4U1veJjolPdVs8Ktz983kGdUnza7qj7RnbvBqUJEDn5rSoEzEgZAgW0pHculLB2zHn7luYSgQkCgdogfMD3w2krRvsVLndfDBkU6t_l8EWhCzPivbwiN_VDFMsYdHH2cUF6nKZBDtorr4CnpAfgiQpK_Mzg13IGgbNsaa71uZaVDB7h-Kt4DM9dpdzkcYHZ7qhArdPHUslFyO1Pry106WuGIqJRaiHYh0LXZo4lFMcKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bbdc557e5.mp4?token=Nl630VfpQunY9__QnuBVxb7eBHTFHHFE5DWfMJhSiJDHZUbH13kQhZQc9HVYkg8qqk7zaIMULs3DRcCFygJzCJZmMTbrA-mQICYaffmXPT4U1veJjolPdVs8Ktz983kGdUnza7qj7RnbvBqUJEDn5rSoEzEgZAgW0pHculLB2zHn7luYSgQkCgdogfMD3w2krRvsVLndfDBkU6t_l8EWhCzPivbwiN_VDFMsYdHH2cUF6nKZBDtorr4CnpAfgiQpK_Mzg13IGgbNsaa71uZaVDB7h-Kt4DM9dpdzkcYHZ7qhArdPHUslFyO1Pry106WuGIqJRaiHYh0LXZo4lFMcKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کمپینی که مصریا برای سوزوندن پیراهن مسی راه انداختن؛ اینا بهتره یه شاخه گل بگیرن با خودشون آشتی کنن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/99563" target="_blank">📅 16:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99562">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/308efbcab6.mp4?token=uk1qRHYXg8xDVtfeMfCGtEM9dX8alo_Oj4dZK8aha--tK-R__iGQlX61QjiBjohwVF2U8YP33yP2Cw1ffzGe4acZ-CQ1dgGbFS86DqexAX40ykXP4sjJAbltHY4puKwI58xlwa-x-4JUhg128Y4zNOwI_aIWry7Awe50jApbwobApQn3r2t_SNuvxa-jOZdb5vAPSR4fNMkGxK_yJbiiMUJ0apNUyAn0fd_JKL1bA7Ai0EmSuDRVSliaeGlFkA4vdG-R_IvQutSKQ_Ik0RAIz22jnCys0BEGR888dJzFW2pE56ioARCdNmtwmQCSJJKZA1RP1yd8N3wyzqZbtrv_aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/308efbcab6.mp4?token=uk1qRHYXg8xDVtfeMfCGtEM9dX8alo_Oj4dZK8aha--tK-R__iGQlX61QjiBjohwVF2U8YP33yP2Cw1ffzGe4acZ-CQ1dgGbFS86DqexAX40ykXP4sjJAbltHY4puKwI58xlwa-x-4JUhg128Y4zNOwI_aIWry7Awe50jApbwobApQn3r2t_SNuvxa-jOZdb5vAPSR4fNMkGxK_yJbiiMUJ0apNUyAn0fd_JKL1bA7Ai0EmSuDRVSliaeGlFkA4vdG-R_IvQutSKQ_Ik0RAIz22jnCys0BEGR888dJzFW2pE56ioARCdNmtwmQCSJJKZA1RP1yd8N3wyzqZbtrv_aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🎙
انتقاد تند رضا جاودانی از صحبت‌های محمد حسین میثاقی: حرفه‌هایش به فاجعه بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/99562" target="_blank">📅 16:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99561">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/411cd56909.mp4?token=pul7SFEcjH2yfSQHUFU4Tb1sXqUA2hcZ1Jk9mJsfoFzbDSi_pAx3bHE9kVnMFijPvMiLOZIOCmaiPzJlsLw0wlLm4LHeH4TJbPIJ7UcGydBGXBEMts_KldKhqWe7b3noUNfDZ2cu51xx18FSN9WWg1RZ25iZAIdxt_JaXPsTi7k2K9gA-dhI3N-jXErMUrXnL9rj7Kkez73PGlLKMgrDhKseCDJOp-hgHAGiZrF_rlXzesnKCqnLIGrnSkQCPvu430F8z7F713gdxJ4qAoq4SXoExD6kpUOGAA-CjBZt_o09HfaEKjxY_3u-bxoZlE4fmCdUgRaFTdzbTIXxSDeKn4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/411cd56909.mp4?token=pul7SFEcjH2yfSQHUFU4Tb1sXqUA2hcZ1Jk9mJsfoFzbDSi_pAx3bHE9kVnMFijPvMiLOZIOCmaiPzJlsLw0wlLm4LHeH4TJbPIJ7UcGydBGXBEMts_KldKhqWe7b3noUNfDZ2cu51xx18FSN9WWg1RZ25iZAIdxt_JaXPsTi7k2K9gA-dhI3N-jXErMUrXnL9rj7Kkez73PGlLKMgrDhKseCDJOp-hgHAGiZrF_rlXzesnKCqnLIGrnSkQCPvu430F8z7F713gdxJ4qAoq4SXoExD6kpUOGAA-CjBZt_o09HfaEKjxY_3u-bxoZlE4fmCdUgRaFTdzbTIXxSDeKn4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🛂
سیستم VAR در مسابقات محلات شمال کشور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/99561" target="_blank">📅 16:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99560">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTZsxPXlrFNaUkbRo-MOmFhaNQ7bW9KzlZNTfDYR6t8O0r3Kh1jahLKWa7WOJBcFCUPYd3qOormvr985loRTrD6KtClwkazWhxQlbBM9-EOkEYXlbL0CGnGxxSaK41LVFBful1pnhV8sePLg9gyFx1htNtqxTTT2u2x62UdtrzFXmtU3535X24O-j-1CFiqhEIM5pcSKgq29GfzQajV9d_hPzi7I2QCqCrK6qTcQyOCl0s8tEOKrRla7kDF-UMsWs4yLVe_UQVys8Yv0qDm5zqLsb4xp-MHxOpuplXqrHzqqzUF46P7M4OOZTd2T2i-Mwkg2RETzkyF6sXXvk7zfbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">+ ترجیح مردم کشور های مختلف در بازی امشب :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/99560" target="_blank">📅 16:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99559">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2fbd5dd7b.mp4?token=EQqgGHKbqh7C6pxazj4aCjm648n7aPH2vk6gxUyKUvn4-mBWeVZvIaGiSTbzgZfGe0SUk2JxBFsxIJhDusuQOd8DgDlZkUp80VRJAMz4q8gisPDW6PFPFZ1qNhoRkA5Qw3xPsPIdBSnODYwO1Xh1Daf6gGfCkEtJD1GWnDiNTItcSsIG35hyudvVw3yECVrKtLv2xvOoCdaEqrqTMWl2uOKVNpnB5Wdho6eadvBu01yF8ezVjydLo8BYduuMCin5JQJW6xtiKR958fA-GmJQYgSH9yUkGS6TR2mvv-MvGJByb46syeC1eyTt_0mt5jh-nQtqtnGPUi2kEqrKtdFvwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2fbd5dd7b.mp4?token=EQqgGHKbqh7C6pxazj4aCjm648n7aPH2vk6gxUyKUvn4-mBWeVZvIaGiSTbzgZfGe0SUk2JxBFsxIJhDusuQOd8DgDlZkUp80VRJAMz4q8gisPDW6PFPFZ1qNhoRkA5Qw3xPsPIdBSnODYwO1Xh1Daf6gGfCkEtJD1GWnDiNTItcSsIG35hyudvVw3yECVrKtLv2xvOoCdaEqrqTMWl2uOKVNpnB5Wdho6eadvBu01yF8ezVjydLo8BYduuMCin5JQJW6xtiKR958fA-GmJQYgSH9yUkGS6TR2mvv-MvGJByb46syeC1eyTt_0mt5jh-nQtqtnGPUi2kEqrKtdFvwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
مرینو کلا آخرین رقص و آخرین شانس و این چیزا حالیش نیستا.
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/99559" target="_blank">📅 16:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99558">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1Aaw9qOI5VgaPqZOlPyLfS5FW3HCu2wS27EKdm9SdcPy8ePwogAtWbJKunrZRxvKtMJEjCu6yo3AqbQfT2FsuHMpEZQ16q0KPFwFtu_Uph0k5NoAgE-j8Vw7t1KureJAbchdScLOJNKYNxyPpjzOcp9TwyjxbCse2aV1cFZlIdBDy5EhA20Cp4sDFQ23wgBrKAA2MhWpAUcI5seEARBDBCMC8pJBS_OjY8-YZ4nSxIXPqADwWrH7i8yeQGhd574qJ1QvuwzgRgC1xLspJN3-iP_ki-8QJ704QUBelzCs6edyHaRDRGrbFbIEpBT80XlFzHaSYPhKu_hFOQWr40x3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇫🇷
سن خط‌حمله فرانسه در دو جام‌جهانی آینده جوری هست که به راحتی میتونن کنار هم بازی کنند!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/99558" target="_blank">📅 15:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99557">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c84faa7ffb.mp4?token=njd1oCoVmQpzHjBXSup6vuNXbS_qWsLBEYVA0qzM9rfv6-2faDyvsUvKVa-nb_OSciVbhGqOhZ8QRL0ueusmDdzf8FoSIBx_4jecDJurkNqIZjQMjHinquAy2nvMGtb-EB7S63q9VO7uChBUdS0YwQKLu0CU3UWKfpQJCDVzJMHFlkO3jWnWt4dHZF0IeKK7fOGnz2Ko0ZWgr6w7jwXkiEf0BuUYiRZ9TIeTlDdOqgzxIfZctjusnrXKVTXe66LP_cfQFR5Pq1YvmrhnbWpQOshk4t_OpWjkMP4OeAuKcLysYmTrSrsvP7tMR3eF6zHjUF8zAqnKBQFCNutiKejs1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c84faa7ffb.mp4?token=njd1oCoVmQpzHjBXSup6vuNXbS_qWsLBEYVA0qzM9rfv6-2faDyvsUvKVa-nb_OSciVbhGqOhZ8QRL0ueusmDdzf8FoSIBx_4jecDJurkNqIZjQMjHinquAy2nvMGtb-EB7S63q9VO7uChBUdS0YwQKLu0CU3UWKfpQJCDVzJMHFlkO3jWnWt4dHZF0IeKK7fOGnz2Ko0ZWgr6w7jwXkiEf0BuUYiRZ9TIeTlDdOqgzxIfZctjusnrXKVTXe66LP_cfQFR5Pq1YvmrhnbWpQOshk4t_OpWjkMP4OeAuKcLysYmTrSrsvP7tMR3eF6zHjUF8zAqnKBQFCNutiKejs1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خبرگزاری مهر خبر داده که برای فیروز کریمی به دلیل حضور در شبکه ماهواره ای جم توسط نهادهای امنیتی پرونده قضایی تشکیل شده
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/99557" target="_blank">📅 15:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99556">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c2e8d837a.mp4?token=lFFwICpqVJBn3KyMdRpvxjH1Au6Xo7HbEaaDywtrdmusnX-4v4KMp-WaeJs-iIVAfOUwtaR1Q8G8XX_31Q6eOAyQw8c-Llm935AcP748U58lCMosmIdwHjUqf45S5PB58oRR-vaCE2YSATlkhuX__dQMxX9GMWLNnfYYu1SeGX44stg_GWEDhjN73PvEJijrrPbZu1JbvO-0diYX5FBJgWgf84YgH2X0mAq1G-V-wDDThQMJI90YlEUxQJ5xq2ckWW_pqlUeXF8g0ENL7SMXA3ul13zMWVP7Va30nExBRHKn0QOz2KrWcRH8yC7620q5QH-6x3RpKbMjXfTbOOvlLJyA0ojgEyZhiSaGC2ZpNhx_1psSvVw7R1KeS3DZjGapRmz2djAm2P2N6opK-vyT0M9hVjfBsFViGSRyM2rbA4bQZAY0-NGNQrvzJGaCYNaM0MmrpamYQG6feRJbcUxz5DgO-dS-kv0-Cvdamte3AUWbJhIkLM-xFL71GQYYDbSwIgedMCeBPJLTPBudoMONtNcizcrg4ExK56WKZ5UwYwLks-5lGf-b_cbWZBcA4eTQlkEj9iOYRIG7GBWT3zY60t-RyQZdLexXJ7vL-96rEIHBl64zD_yEYsYgSL9PQh_eiDkZHYQnaG2lnnqD2QoaDvPlmXvI3H2bzI6IHnH31CY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c2e8d837a.mp4?token=lFFwICpqVJBn3KyMdRpvxjH1Au6Xo7HbEaaDywtrdmusnX-4v4KMp-WaeJs-iIVAfOUwtaR1Q8G8XX_31Q6eOAyQw8c-Llm935AcP748U58lCMosmIdwHjUqf45S5PB58oRR-vaCE2YSATlkhuX__dQMxX9GMWLNnfYYu1SeGX44stg_GWEDhjN73PvEJijrrPbZu1JbvO-0diYX5FBJgWgf84YgH2X0mAq1G-V-wDDThQMJI90YlEUxQJ5xq2ckWW_pqlUeXF8g0ENL7SMXA3ul13zMWVP7Va30nExBRHKn0QOz2KrWcRH8yC7620q5QH-6x3RpKbMjXfTbOOvlLJyA0ojgEyZhiSaGC2ZpNhx_1psSvVw7R1KeS3DZjGapRmz2djAm2P2N6opK-vyT0M9hVjfBsFViGSRyM2rbA4bQZAY0-NGNQrvzJGaCYNaM0MmrpamYQG6feRJbcUxz5DgO-dS-kv0-Cvdamte3AUWbJhIkLM-xFL71GQYYDbSwIgedMCeBPJLTPBudoMONtNcizcrg4ExK56WKZ5UwYwLks-5lGf-b_cbWZBcA4eTQlkEj9iOYRIG7GBWT3zY60t-RyQZdLexXJ7vL-96rEIHBl64zD_yEYsYgSL9PQh_eiDkZHYQnaG2lnnqD2QoaDvPlmXvI3H2bzI6IHnH31CY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🤣
لحظاتی با داداش بامزه لامین‌یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/99556" target="_blank">📅 15:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99555">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a53021254.mp4?token=jyTcd45nscKlgLCjegAGDp3_T5yhQmuM8N-BM3NE2jmFkWBYt1-LvnnFdyVm8-0dxR6uu7rNtP8TQE6wpP3GOZVeT86F46qQpm_m6XOg8eRUQeQvZpOWjxYaWp_o-pIDxzw59jOUn-j7mxMdwPPwLquVpsPkw4-Y4FrBY1XpS4gwNMFjmJiuqG8N2hr3HZn7cJvBafyRqSFGhT5w-q6nS4-QpOOcBmvGaWYWNIqpTbOoY6IDaLsFM_zEFYbkfMuD2gxHeL5iKbWGf_q4AxOUrah_5Tpv-ky_RIgcszoC1V1lEB2dTEwu6FLy3-pluhaTOBPvjwBhUfSG2voqRPvdPqD_MLPZXhUjj4d3BNWASrofRIVzPbc3a0TPqTzLYQQZsOtotpAmzmtYeXBVyqL1PdvIHDRGWg2ChQ2lYCSxx6quvfrB7wkrtFkKj_Dy43VnfrRBUxcAf-f3iUT_ItPkqHJJoNRcbhQ6I-4BqVC0aHO46H4f9rDKu0Acg3iszknBNba6neOh5c1zWeyH0U3JOFbHRbBDW4Wmcni1lw8Ho_8ooO3pTI4zKolCCdtemk9LlnjIL1Vdy-X0rJJo9Hl3f345FAsTZhY7DrxsuVvx7F79R1G7ihCIGZzv7XIpv69cir8RakwMYtNX0wnDRkj6JV6MICrUoFWU_jVsX7az2S0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a53021254.mp4?token=jyTcd45nscKlgLCjegAGDp3_T5yhQmuM8N-BM3NE2jmFkWBYt1-LvnnFdyVm8-0dxR6uu7rNtP8TQE6wpP3GOZVeT86F46qQpm_m6XOg8eRUQeQvZpOWjxYaWp_o-pIDxzw59jOUn-j7mxMdwPPwLquVpsPkw4-Y4FrBY1XpS4gwNMFjmJiuqG8N2hr3HZn7cJvBafyRqSFGhT5w-q6nS4-QpOOcBmvGaWYWNIqpTbOoY6IDaLsFM_zEFYbkfMuD2gxHeL5iKbWGf_q4AxOUrah_5Tpv-ky_RIgcszoC1V1lEB2dTEwu6FLy3-pluhaTOBPvjwBhUfSG2voqRPvdPqD_MLPZXhUjj4d3BNWASrofRIVzPbc3a0TPqTzLYQQZsOtotpAmzmtYeXBVyqL1PdvIHDRGWg2ChQ2lYCSxx6quvfrB7wkrtFkKj_Dy43VnfrRBUxcAf-f3iUT_ItPkqHJJoNRcbhQ6I-4BqVC0aHO46H4f9rDKu0Acg3iszknBNba6neOh5c1zWeyH0U3JOFbHRbBDW4Wmcni1lw8Ho_8ooO3pTI4zKolCCdtemk9LlnjIL1Vdy-X0rJJo9Hl3f345FAsTZhY7DrxsuVvx7F79R1G7ihCIGZzv7XIpv69cir8RakwMYtNX0wnDRkj6JV6MICrUoFWU_jVsX7az2S0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
امیرمهدی ژوله: هوادار فوتبال و شور و حال آن را کاملاً درک می‌کنم / حرف من درباره فردوسی پور این بود که ماه نحوه شادی کردن را بلد نیستیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/99555" target="_blank">📅 15:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99554">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-v8lCcngHB5OkqNW2e9iTatJ4AJZnL2QWJFrErP_0fILzWNJNEnwrR7sq09nhMSTpmZMv2xd0aCc5KQViHnvcnKWyHN8i-ydnViytsuZoEfYJaYAV0s9Emitq5dqQC6fInYFVjmGLGv4kJRxvvvdBn_PETVWbxWVl39CD9vF97vcIj7hP21qg1pYipfG3lBV86BNuEglxUAZAYfcfTJJOu5WxaTV4GQWFtIEcaL7VKtt6l17y4wxldg-GcC1Pp_fJ_HnGYvgVXAUwgDp6jVt3luZ6im5ba1C4VuPFvQ2eASQuXP0dUD5v4brwcfWBaAhPIEO8Ty3yQVzExhHv1qhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تیبو کورتوا:
برنده بازی اسپانیا-فرانسه بدون هیچ شکی قهرمان جام جهانی میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/99554" target="_blank">📅 14:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99553">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/735c75025b.mp4?token=RJ5hCY-J4MUR3nlqY8Ub4-tFdP5g6Ol_mc557I1Kdo52n5zxm-y7HWfm3Fk-3R75PVO4u8_XsgoreMQc79rO2kwh3oG4KnHZa9PES5iIe71yTA1zwerrcKEup_PNtGHVPzwoj4zCuSfi0sWhF3dMhoKxS4AtS1Uu43ZQITS5QOsIYD_y0w1ZXS_q2GorX4EzMMPYtuY2cD3E0rBogW1swhxqO55hJhM5zNafQVoqlnFVeCw7ziwBO_2bBsTr3j8HpyP8QvPjlmkqPwREjOuzphMKAwzWZs5fkDNkYMYdA40EClbF5vM6F5WV1YkGqO4ATY9tdsHxN97GYMNZEvVhIEuUz1E3niXIfBBRypIjy8wfjJF88ngn0J74WgmBAoFe0W4ylMMXELp9eR37WGPm-wlHxKxG0aBtN-VLUKR2uiBxpSV9sGk6WchmU39JtCIVIoXRKbQgmRggxeI-_zyM55dPhuEVnqoropduZXM67lBHE163332uqZxPC7j_ziV_lxA0aVKFh4dKEa9s1uMZw51Ox8eEq_al2OAMQN3-2GpOCtTgmHfGw_3f3mUPNkiE1eVz31n-BA7G8gcyHeNm05qDP9kT4u0-2W3LwAvEPzOhT_i8gY3TLZdXlRXzS7ufSd5RFak_P7bs5ufFChcx5b7jvRAevANMubBZ5DKqdEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/735c75025b.mp4?token=RJ5hCY-J4MUR3nlqY8Ub4-tFdP5g6Ol_mc557I1Kdo52n5zxm-y7HWfm3Fk-3R75PVO4u8_XsgoreMQc79rO2kwh3oG4KnHZa9PES5iIe71yTA1zwerrcKEup_PNtGHVPzwoj4zCuSfi0sWhF3dMhoKxS4AtS1Uu43ZQITS5QOsIYD_y0w1ZXS_q2GorX4EzMMPYtuY2cD3E0rBogW1swhxqO55hJhM5zNafQVoqlnFVeCw7ziwBO_2bBsTr3j8HpyP8QvPjlmkqPwREjOuzphMKAwzWZs5fkDNkYMYdA40EClbF5vM6F5WV1YkGqO4ATY9tdsHxN97GYMNZEvVhIEuUz1E3niXIfBBRypIjy8wfjJF88ngn0J74WgmBAoFe0W4ylMMXELp9eR37WGPm-wlHxKxG0aBtN-VLUKR2uiBxpSV9sGk6WchmU39JtCIVIoXRKbQgmRggxeI-_zyM55dPhuEVnqoropduZXM67lBHE163332uqZxPC7j_ziV_lxA0aVKFh4dKEa9s1uMZw51Ox8eEq_al2OAMQN3-2GpOCtTgmHfGw_3f3mUPNkiE1eVz31n-BA7G8gcyHeNm05qDP9kT4u0-2W3LwAvEPzOhT_i8gY3TLZdXlRXzS7ufSd5RFak_P7bs5ufFChcx5b7jvRAevANMubBZ5DKqdEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
▶️
افشاگری رضا جاودانی مجری سابق مردان آهنین از پشت‌پرده این مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/99553" target="_blank">📅 14:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99552">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFY6q4H0c_uqBpeIOz03Rw1nY1pkU1hrOgu3v0fxPqiHP8vVDPmHmKACUYwBLggQSNwA4SAXE9mh1zSDeBg2gOlTxi7UgDRTVUGozWu415DBFbkSlzPfL7HqAPcMEcsD9ZQddSA5zZzRZeQlkfdW0XBtDQeZEXGcO8fRKW64zFMuQx1VyyGBO0y3XsgsAoyq41oxlGqmHWglhk9D-BG09WBAW1cetjuMHMmVn3wyJqvbGIpI3jfAKGLBpQYuhrdwsKoGHi6v89c-ZGSQu0SwhL_GhoNX2Unw-XDGGs5IQSwJAf1eX5NsfaVh27U9pMuJQOR-2KugXmR4pAtUC4lrmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇮🇳
اسپید:
هند به کمک نیاز داره! اگه این هندی‌ها واقعا دوست دارن تو جام جهانی 2030 حاضر باشن فقط یک راه حل داره اونم اینکه من رو جذب کنن تا واسشون بازی کنم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/99552" target="_blank">📅 14:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99551">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HTD8yAzzxVGZHa1lQYGVnUbEc2lSNC80l89WRXop5NMe1NpnFvMEHF53nBRNTnCXZH0-V5DbPTEkQkQAtoPDPuztpt5Km-CN1flhQjbAZMu9A-9Z4WFho0xvvYqBkkskFK8T6n7z-XosllqmuWn3n-2Mw9Hs0HdqiN4a5i9Gjfra8dZCfBmjzxxPO6TstVN8O8Z1QsnFz6J7sMj0-K3f4ATXsqhQbs71pucJkvoXNV6e5otjQQjFyPmHD9gQkntBc2G0GqlskTBTm4X2s5SjlehO2aJUNk4UY3DzfAzEma1VH3q_zeIQHYcR-BWZPV9_2HsaGGqr1vhzYmb9DsrnBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه فلیکس دیاز: رئال‌مادرید و وینیسیوس تقریبا به این نقطه اشتراک رسیده‌اند که تمدید قرارداد بزودی حاصل می‌شود و ستاره برزیلی ستون اصلی پروژه بازسازی رئال‌مادرید خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/99551" target="_blank">📅 14:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99549">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/734fedf32f.mp4?token=mr6DIR1VyNsCxlbqUjAu5hvQPxFO5q-lck6Bi74loRFjBo5WmBR9eNrGCELgP71m1Cp0iGiRYm-6JXkqyTjrNFfBByaXPfGD32G7aCtP54dF_d9ijvluqJbyUIldojnrFm8y5NYp8dYbGoCwpIfp46hoY-g1cvDnSdFfcSe1v5JrJlwEs7Qb2rEp1ia1i7MIIZOMcPpPgbvb7ly6cTGRzxs1-gHIDBL8jYULYm0e6jUAWkFdEeceK0ZTkKIP6pguQ6KzLvuB4pQ8t9k8vfDFd2A1_kbpJkKYjHoyrl2fw-8uhDCh4cZu0dtTtH572VRK5mi8xkx-AmsIQhRGaXdFfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/734fedf32f.mp4?token=mr6DIR1VyNsCxlbqUjAu5hvQPxFO5q-lck6Bi74loRFjBo5WmBR9eNrGCELgP71m1Cp0iGiRYm-6JXkqyTjrNFfBByaXPfGD32G7aCtP54dF_d9ijvluqJbyUIldojnrFm8y5NYp8dYbGoCwpIfp46hoY-g1cvDnSdFfcSe1v5JrJlwEs7Qb2rEp1ia1i7MIIZOMcPpPgbvb7ly6cTGRzxs1-gHIDBL8jYULYm0e6jUAWkFdEeceK0ZTkKIP6pguQ6KzLvuB4pQ8t9k8vfDFd2A1_kbpJkKYjHoyrl2fw-8uhDCh4cZu0dtTtH572VRK5mi8xkx-AmsIQhRGaXdFfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😁
چه اطلاعات مفیدی مهدی‌رحمتی بهمون داد
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/99549" target="_blank">📅 14:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99548">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8suwO8oHF9JMEO3JF7m-I3daiK7ccUmlVncxiIhRKxlWlWrSvBfk3sd-VhcVx3fBW4LSzGazhxDgoy8IairVAhE29c2Ho-8_pPRN7MW89R0A7XQY_Ka4TSxKlMAA8JZNbphebFWDuX4L5l7YEhMzRTcU6GqSUmgFgMRXFqmpeNmQ4DOefxnGOLY8gxQUAY6GuOJbc-MiRnol65JpxsDMbRmxPd3msacDAY8Ci9haMe-O29KOszLtqN5g_DIZCH46-sVyxd914n45D_Jdz8QHQb39AbHj0JGT1m8qZ1nCYumBvi27LZ33bvUIxjamdLBaF8NZoQWl_tSKWbgxzI9fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه فلیکس دیاز: رئال‌مادرید و وینیسیوس تقریبا به این نقطه اشتراک رسیده‌اند که تمدید قرارداد بزودی حاصل می‌شود و ستاره برزیلی ستون اصلی پروژه بازسازی رئال‌مادرید خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/99548" target="_blank">📅 14:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99547">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LWdm3xH584JU8aMuu2jWfmYkBXbGg1uObugtuIAWIboXDeUcak2U_S0L4uaYSf9lxp3LuJb8Ybkkjo7g6oGALBw6jX4G6hhvNGQ_7s7o8vn6p00MWxQjY4RY51FK1ig6eJbb1Qx8QQuq0pQhejAFwrUNBkBVq6tzNgcqQvwHyGF0Qt6BlIul-bCFnqshx75HeDGhHb_drJZS8HlE6Qg8vr-Hh1qIEvcrxRuzBum0rhXM3O08crDqR2r_pB8g_p7Kd6yIUMoIE6rdXtmH5vGmcsHdgXy9iA2523WA-wwxDNrbh_suHNSCqpWPtgHB4rpe2BDm_e5AYQGvlpYLODBztw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‏فابریزیو رومانو:
🔵
بارسلونا آماده ارائه یک پیشنهاد جدید به کلوب‌بروژ برای جذب جسی بیسیو، وینگر 18 ساله با استعداد بلژیکی است.
✅
بیسیو با انتقال به بارسلونا موافقت کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/99547" target="_blank">📅 14:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99546">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQn5H_wkBoFC_XXclhZRKgLbXcyBfyZgazceGyHCCXPhevAKMoeIAoEPdVIp3VXWz66ryGAjZjhpi_U4xatgYl-AIcy7-7ghegsQG1zjbYc_V_x8t-YPdW6PcXB6d-zwnccaGQX3n5URssbPtheC-zntDSl-PTVLn4b8KhOE5HoGD8WDQg3SjvscbigdsqJkzmh4mBiVeWjRIac89ElQYIOaBo6E3jbKkWgt2cekYbebbcp2BFAUOFeQrns5lsbCwu-YSwExrR2fPNGg8y7xed00SoS3DNRT72t533rPmFrLLhwMruKzhzbj9NWZTRNTnbpskKn8rpuJky7oX5eV3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکل مرینو اولین بازیکن تاریخ جام جهانی است که در دو بازی حذفی مختلف به عنوان بازیکن تعویضی گل پیروزی را به ثمر میرساند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/99546" target="_blank">📅 13:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99545">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_X2Hsf4HcjKCjBbrt4JKU639H26BFpzxwjZBH3tbzb7S8RhFvDcSpTkSo5uGfoQo8L7nmkyZmV0UaMUEfxQYQPxzmAYrL2uGReJMi31O7rDp4pWrXSgx7yDNOewixMysRuqZI6IbKyrkUnJi7R76oa3RjiIsnkoj8JiaBQjS1sOmnsEgITKdn0HYzvPftEZacwoxgOqS1TuSYr66PdiH644RVVWPeZHEnY7pP2OpGE3YzKf3j7dkkVPqOIPzkgVDQFBEfaD_F0Lh6luw6z_ieuw56SuuRvSfDldff28IKD3NGK54ljvgJ3Rq2-KLI9ZIryXoqyWjR5b-7kzdzY5Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
شانس صعود انگلیس و نروژ از نگاه اوپتا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/99545" target="_blank">📅 13:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99544">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tyVteCPAaxv0AT35NkMKLQphED9ku0ySwjt2VRxZztgSvUk3Gvf9Ih6mdGoc0Kp_QXHoHRDP4qvWCXzVmpQ2vAoGAKrZMKnO9uZanFjfZhuf2ZrVDksc25Ak19Ah4ESONoHVnLV_h1LjY5v2ECi_tw-EAGl2CefOC977QbCVfWyOoGljeghgT6qrrHyCfADpMv3n1vubWbl3kMbdeqQtrTzIzMGMC2nAvZBLcFT0XyGXUkbklZz--whq-0D8PlrPGW2kHgtEjrI8c1ofnZCclZsyPDOGPCjBsJvLH-l1FUqN1EsL_D-6G1WTyjtrd1vywyJS_92G0t0bhRVVT_3TFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها کشور آفریقایی که از جام‌جهانی حذف نشده:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/99544" target="_blank">📅 13:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99543">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lm11zx5UD_qcAe-E_gsZjB3LyIuo_nMK0J4qRDHRjT2K98dEglOxrLY_46AKfBrsgx6hNmmfq5AkzndqX0y2geTYantVkQvtm_Y5j6cK7rbCAzHt4p3QhVULyw6AvsKahToOBPT7JRIjXykVbCvZERuQboTTWl0fHrXvnmbpkthSIcn76avpRs2NglA7Az5OKCu1E0sZeMRDAVjXjPNDxdMrPLMs3hahFjyGJ80X3HrtIk6KTjkkSXnQhEFhCAgq6MAdf0mrZhQaabV3NkptSf_G55U2ATtpkmZwiHZF2ragE-agJ5pyFIJJxwCdr-f3CEVH1xKkwTr4xm408-Gpsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
| رودری، بیشترین تعداد پاس موفق رو در یک‌سوم دفاعی حریفان در طول جام جهانی 2026 داشته است.
⌛
از 180 پاس، 170 پاس او موفق بوده است. همچنین، او بهترین درصد دقت پاس را در بین تمام هافبک‌هایی که 100 پاس یا بیشتر انجام داده‌اند، با نرخ 93.41٪ داراست.
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/99543" target="_blank">📅 13:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99542">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fji_TqT2XiSlsiQQmtCCbEzolHPfMP53FbFnkqOQGdC-MCtkSwSvmX4vafmy7JOqS-mK4Ck8NbYMR3OfV5Zow69qPBmDGHs8XkmeIhZoJVHEgIQvbs7pWkkSKQX-5e1wQa_zHkCM751SoQ0PkuanjE5lV89pUoWS1SltlUVTQzIIc0iObVpy_MsTkgyrMP6kQl7Ec0aEJ9PmPZK-DKRiHFlDN5ogxyMrhC5XI0biS5Ih7RrSY1a53cwlXG0VvjJxKWa0C1fxSQBCagOb7QkqMpc0qTZqZCwvo-BWDifYbHUD4tEbCgAdiEtifOXfO96lNjUcHDwnTkbFPFdgLOtT7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینا دیگه چیه برا هالند میسازن
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/99542" target="_blank">📅 13:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99541">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآپارات اسپرت | AparatSport</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYZsr2rO11kavClTFXY7BlZZ6fOSFx1hcHazV9RSEWgSdT_ZUjpgFmoDCE3C8SMdaQXlvRZuqxlvJELz8d3sBjomI9i2BDGkiLkHjnAYtlhpp5V_zQKm7Ej4XLqSAYoS_MgY495ZvusFnfP2yX24rrnNtk4zfgUS8cOAojHYpmDXhRKOpytezDhC1aPlTxKrUz3at1j1VIW2j3j3Q7p-2HlA0V7f_MzUgE37HaLr5VbTsSafCC-0JBAy55s3_SytKJjN5ifAlm1rw4SoRzVn2DIi_0bwE0NcQgjIdmr62N-Kky-FPdSwpoU8Ei-hgBWVVz0KzjJIiiJ3k1eg4toMQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پخش زنده و اختصاصی بازی نروژ و انگلیس با گزارش محمدرضا احمدی در آپارات اسپرت
📅
یکشنبه
👈
ساعت ۰۰:۳۰
🔗
لینک تماشای مسابقه
(بدون فیلترشکن وارد شو)
@aparatsport</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/99541" target="_blank">📅 13:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99540">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pn8EMPychJBExuIeMHkVgRljfTexT_qkkLuEIkHQ1YgVgrfFpH882yXjfaRl_VGz_0IV300ssA8iVddIsWQghTUtG-p4vypOXHsD7p5bPKn_-rFtwk5aMO_0LU2xKGzT6-OAu7E8LoEDo--1ALjDvNy81KrPxDM-HzzUcbSnSGF94WlUglnJ6irqnM2IXq1oyS4OSPd1kmjRrcbXt5_P1oElv4sB044t9GvTsxVJyhEt_QE_fp802O_uHBvJpFttP_ArAydOpcwZyYDkvGRwomoP4v3XKOfaIyrlz4nyeNuAj6dEiwwNYcfz5Wt7ePo4CFQIxKAN4EwO1HFm69_FBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
همسر جذاب و دوست‌داشتنی آقای نیمار هستن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/99540" target="_blank">📅 13:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99539">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50fb9f73e4.mp4?token=tgVFvcsjhdJSiKkvYCYBonsQbuvZOZ76ZcKmugvNZxvjoVlg-Xm_zjs9-tP-k4Bsz62EWkL4_Nf8CW--yxPCyl-p1jzgvTZWe49LoeuXycypK63_-G0nBmT-kO61lzoNAcUnRNBTSSePuSt2GioDhhQDk1U57Kjo5i0wpfSP86DByRFfy_3YkoxnsDza6zwQPhRfKlu1_rSrbhmGZh0c-pTEHsVbu44EsGa1hHHmdeXVEPQzBaLdioMlYZzMeogDrHhzBqTjbP_KViraOe1XDzOBu08VuS61UXdOKeVYFsdIdOwOZOTWXtcTImNbKYH4IpiOgUGtmzBtTycEg4JfYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50fb9f73e4.mp4?token=tgVFvcsjhdJSiKkvYCYBonsQbuvZOZ76ZcKmugvNZxvjoVlg-Xm_zjs9-tP-k4Bsz62EWkL4_Nf8CW--yxPCyl-p1jzgvTZWe49LoeuXycypK63_-G0nBmT-kO61lzoNAcUnRNBTSSePuSt2GioDhhQDk1U57Kjo5i0wpfSP86DByRFfy_3YkoxnsDza6zwQPhRfKlu1_rSrbhmGZh0c-pTEHsVbu44EsGa1hHHmdeXVEPQzBaLdioMlYZzMeogDrHhzBqTjbP_KViraOe1XDzOBu08VuS61UXdOKeVYFsdIdOwOZOTWXtcTImNbKYH4IpiOgUGtmzBtTycEg4JfYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینا دیگه چیه برا هالند میسازن
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/99539" target="_blank">📅 13:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99538">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
‼️
🔵
🔴
جزئیات لحظه زندان رفتن ستاره‌های پرسپولیس و استقلال از زبان ناصر ابراهیمی: من که لُخت نشدم. به هاشمی‌نسب گفتم پاشو خودت رو به غش کردن نزن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/99538" target="_blank">📅 13:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99537">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d194f8eb6.mp4?token=OOVlweOTi-jHDCmU9j2Y1VedWGbexuRU3_IWUXrWT-ileRP3VW01PdWCEVu1vL7UV_Fxdm_N2tMn3pXsUzrIIaNe_Jrq7ygDRERJkXzpW5hMx1TlCGb6iHld8BIzzfS-jlR7Yhoq7AK4pLdhwT3QCi5aB5dxG8i9Dv3xOOEtiKEZ1EESlg2yK2BtgjiFuvrGblwLwsWsCXVQoV2jm7_B7VCS2AEc-J8_GoIrqvIeQHQ5N_CbMjVR3HxumOE3hKxR9qHL6zLyYKTCY7WfAkEZux9ASqrq8VKwYyNF6TD7Dqs5GuUOhf4FNA4RFnOvTdDNdjJbYskwOwDDCJUWc53F4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d194f8eb6.mp4?token=OOVlweOTi-jHDCmU9j2Y1VedWGbexuRU3_IWUXrWT-ileRP3VW01PdWCEVu1vL7UV_Fxdm_N2tMn3pXsUzrIIaNe_Jrq7ygDRERJkXzpW5hMx1TlCGb6iHld8BIzzfS-jlR7Yhoq7AK4pLdhwT3QCi5aB5dxG8i9Dv3xOOEtiKEZ1EESlg2yK2BtgjiFuvrGblwLwsWsCXVQoV2jm7_B7VCS2AEc-J8_GoIrqvIeQHQ5N_CbMjVR3HxumOE3hKxR9qHL6zLyYKTCY7WfAkEZux9ASqrq8VKwYyNF6TD7Dqs5GuUOhf4FNA4RFnOvTdDNdjJbYskwOwDDCJUWc53F4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇪🇸
لحظاتی‌کوتاه با آدیمی‌ستاره جدید بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/99537" target="_blank">📅 13:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99536">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbw5pj5sv21pS-8ElSveR7fylVrXMJ4TfS72HfW95c_D4bt9GENPIEYWFTHLycY6YYkSZOPYN7_8QFhBb99TLoKPWznNFhslSslg3HXCp5b4D39ymjL6nt7GeGNUwMOEzUJIVkM7TQ4khabtCIPVWcA12PoT2STTOGQ4vT4T65Ap7xMqsVFPXIFdOXEp3tVJ17ffNS78e0eC3p1a6WDC3p6ssnyIE7nKTytYtq_vbhmQFbpa9FEsmC1jAxqnZKih1jsYKfgU6HidtLGEoixHWD6jt37KEieNphI8gLfIZ0ZI7RmIRNFCdwetw-YhuaSpE7uCZUeEu4fl_klfJM6etg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">12 سال پیش تو چنین روزی لوییز سوارز به بارسلونا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/99536" target="_blank">📅 12:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99535">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/99535" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔴
1میلیون شارژ کن 1.200 میلیون تحویل بگیر با پشتیبانی آنلاین ۲۴ ساعته
⚽️
تنها سایت مورد
#
تایید
ما
✅
اپ اختصاصی بدون فیلتر</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/99535" target="_blank">📅 12:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99534">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgYGNphDqpjj4Me8CwwPKHuWIYronqQ5EM_eh2cJKomWXqqnWvxd6QCBFDSHiMtpijWqvn1QOR7qIKw6cXHNsBq0km0FUdNsTwoKntkZ-L4xe8fOUBrp86uU04Y7ZBiCVPkWR7k07M7PXW2ltefjoNg-yjNx0G1hWuNPCwsCqviITQdsYjKy0TZK1rWyuxfxqi8ZHttvIS4ZxaGr-zomfuXXGh_pE2076TBnXxf_1o_FNNne6LBOs9kcxlDftwmB2Ht-jiyQyotosNJ57Kor6rvAmnDfVQiyhvbQtrClBBzDzzj9if94zlfDewkkUz99eLqF6YetY27Ixdoz7IFKzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✊
برای یک بار هم که شده بدون استرس شرط ببند!
❌
با هر 1 میلیون شارژ ،
🅰️
🅰️
🅰️
هزارتومان شارژ اضافی بگیر
🅰️
0️⃣
2️⃣
🔣
بابت هر شارژ موجوی اضافی بگیر
0️⃣
2️⃣
🔣
کش بک بابت هر باخت
✅
این بونوس ها بدون
#قیدو
شرط و نامحدود هست
.
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
r20
@betinjabet</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/99534" target="_blank">📅 12:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99533">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bdae855b9.mp4?token=vQNrxQ47UT-ljnvsVzJ87JMfJ2BwhpNFun439SMVI80fPPRavu734We8da_H6djMbSoW4V3977IS213dm4_9mEEBMNT7uykYUZysFC_BHFHPiWaRiFi_LoidKugWKsF20qXcrvJl9mtJyRr9BMjDjq_5NjE62sT5ji_bEBd0ZuJwHgcwg_4TocMXN4byFCgkuvNXizx5RN-IDkQrN05iKnRLWHSIBebqjKR1Vikk6FTjy8px3pgZKnMcUn4uq-7-8K7VkiblRu8AOV2SQUt8NdloPD7A6K1doDzCukwIIP-7AzU4LCfObYQ973DUpPkXQCksYiUn6aQrNugTREdM3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bdae855b9.mp4?token=vQNrxQ47UT-ljnvsVzJ87JMfJ2BwhpNFun439SMVI80fPPRavu734We8da_H6djMbSoW4V3977IS213dm4_9mEEBMNT7uykYUZysFC_BHFHPiWaRiFi_LoidKugWKsF20qXcrvJl9mtJyRr9BMjDjq_5NjE62sT5ji_bEBd0ZuJwHgcwg_4TocMXN4byFCgkuvNXizx5RN-IDkQrN05iKnRLWHSIBebqjKR1Vikk6FTjy8px3pgZKnMcUn4uq-7-8K7VkiblRu8AOV2SQUt8NdloPD7A6K1doDzCukwIIP-7AzU4LCfObYQ973DUpPkXQCksYiUn6aQrNugTREdM3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇵🇹
ژرژ ژسوس در مراسم معارفه به عنوان سرمربی تیم ملی پرتغال: برای من اسامی مهم نیستند و هر کاری که برای تیم ملی بهتر باشد، انجام خواهم داد.⁣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/99533" target="_blank">📅 12:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99532">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad73d33a3.mp4?token=V_rtCLCi3HZPk39dyOUbyI5P_lrKO7kqBSd7cZxusELG8AT2pMb6NfVI7kcbrElQJKw1uqNGNEUVoMQRrR9nMFuINYZi8To4iN4qkxBAD0kpxqv_kHL78YDR1hAaGJdqDoZhRtaAMf5V6-KCippL5xoQJ5tAF42BSDGoqZsgwEReeOHmbIQ_v6wH0xMBGQZ_WpLzmKlZDNMDK6XXiFDxRXXNfESYZWS0xvlWYlZ8o45oSXrDbN7RzP8De7IhZvHUXDxqf-WPYicw532lOIFlm68cFC8HM7LRTToKXJwrf8uycNpgGjotRejyWsKOtPfzq3D3rn81eJ7jupcpTR8zKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad73d33a3.mp4?token=V_rtCLCi3HZPk39dyOUbyI5P_lrKO7kqBSd7cZxusELG8AT2pMb6NfVI7kcbrElQJKw1uqNGNEUVoMQRrR9nMFuINYZi8To4iN4qkxBAD0kpxqv_kHL78YDR1hAaGJdqDoZhRtaAMf5V6-KCippL5xoQJ5tAF42BSDGoqZsgwEReeOHmbIQ_v6wH0xMBGQZ_WpLzmKlZDNMDK6XXiFDxRXXNfESYZWS0xvlWYlZ8o45oSXrDbN7RzP8De7IhZvHUXDxqf-WPYicw532lOIFlm68cFC8HM7LRTToKXJwrf8uycNpgGjotRejyWsKOtPfzq3D3rn81eJ7jupcpTR8zKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
بعضی وقتا اتفاقات تلخ و سخت باعث تغییر مسیر و زندگی ستاره‌ها میشه...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/99532" target="_blank">📅 12:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99531">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/882a067f73.mp4?token=JP6eYT8E-lrXKXFeeJ1Ukz7wfKacheiZz7PuL-cew932fpwpjyPDlc58Il6e61kbUmsp90CkHnyssg_Omsn3StuFEsag_WDbPAOsYGVsMZfo8eYTyWMH5mI9Z6RAAdQ_E6rdA9p2iOle0mSSLfb48Q_7ruqg6KBFy-zbATQOB7SJNT5wpPGcEbqYgVwP6ahRWGkEEB0SdfdKZQewSUfc5gVHSdBi4rqGuev1e80gmQbrRjjB5tBVkKn6di0b-JHsxUyRCuLXVSrXUExpH272nBINDqjsNSZPxQ3wmYIrflPIBpiXvD4wpQCXspQuiXmIB107sR-rzCEmU9zQSWzV1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/882a067f73.mp4?token=JP6eYT8E-lrXKXFeeJ1Ukz7wfKacheiZz7PuL-cew932fpwpjyPDlc58Il6e61kbUmsp90CkHnyssg_Omsn3StuFEsag_WDbPAOsYGVsMZfo8eYTyWMH5mI9Z6RAAdQ_E6rdA9p2iOle0mSSLfb48Q_7ruqg6KBFy-zbATQOB7SJNT5wpPGcEbqYgVwP6ahRWGkEEB0SdfdKZQewSUfc5gVHSdBi4rqGuev1e80gmQbrRjjB5tBVkKn6di0b-JHsxUyRCuLXVSrXUExpH272nBINDqjsNSZPxQ3wmYIrflPIBpiXvD4wpQCXspQuiXmIB107sR-rzCEmU9zQSWzV1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🎙
ماجرای شماره گرفتن امیر کاظمی از وریا غفوری: رفیقم گفت آخه بی‌شعـ ـور تو وریا غفوری رو نمی‌شناسی؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/99531" target="_blank">📅 12:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99530">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrPcvoSRcRIL1AImVh1a_9NnLCudK574NQWXKxBLRHwy7keVMOnsWzLNjG-8ODWtDw1K5BBvsHkxhCTwgtpA_V3SYawtkomnpHC2L0Ghj_vg0AUh62uqS5E-X2XzSz98LePq6Z5GJWQK3p7I1mxtp3Uir4YqVX__TKoN5QhDkXkZrCrKAwt_Q2zmanAdfcz-CE2kZ5r7Oor6-b_H8nyrZtv-16YuqcZAvcwv9n96O1QZSOeDdwUF50eHKcGuDvBELoIP-O1jVAOYZZRpQvmdZtqhbZkn0BgUsEY-oKtXvo35HDCbXNIrbbgH3oyUqJNXIrZghFud8sP2TOwILkvHJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
دی‌مارزیو: کورتیس‌جونز هافبک لیورپول مدنظر اینتر قرار گرفته و در صورت انجام این معامله باید رقمی بین ۳۵ تا ۴۰ میلیون یورو به لیورپول پرداخت شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/99530" target="_blank">📅 11:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99529">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🔵
🔴
#اختصاصی_فوتبال‌180
#فوری
🔴
🔵
برخلاف اخبار منتشر شده در دقایق اخیر، باشگاه پرسپولیس تا این لحظه هیچ مذاکره‌‌ای با کوشکی و اسلامی دو بازیکن استقلال انجام نداده و این اخبار برای بازارگرمی و مختل شدن روند تمدید قرارداد این نفرات است. گفتنی‌ست که آبی‌پوشان به‌توافق خوبی با این دو برای تمدید قرارداد رسیده‌اند و با توجه به تعدد وینگرهای ترکیب پرسپولیس، شایعات در این زمینه صحت ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/99529" target="_blank">📅 11:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99528">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d06676f902.mp4?token=MNGDntjKq7EgWhZZKFXf1OFvUBDLtNKMBGCZuWqLmNGMqoML5euyoiyjwl4GUVTkqq4zg7ygiUaYleJ9SCv2YqkSUV2qNzkZ8rC3TjjXEDo6oxKR5Fty6LWjtLQxUk8UDSmeGn4jX7oq2MbwOfTVPuWMT6SAxDj2iahk9tPCBkYwIYJrDdxLxnb4kH_ar1z4RjFdFP2q1VFsWYesuofmWHw1rOw_pS_pLn_LM_CY7tXa6gBSu0JQueDlUVCQHsSypWMqV6HX2zwxeIQLBu1soxQn5CExFF9T-UMx7J5znTJAWii8f36Q2xMz_G8e3U6ylIH50_tEPQzOMsE_ofBQPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d06676f902.mp4?token=MNGDntjKq7EgWhZZKFXf1OFvUBDLtNKMBGCZuWqLmNGMqoML5euyoiyjwl4GUVTkqq4zg7ygiUaYleJ9SCv2YqkSUV2qNzkZ8rC3TjjXEDo6oxKR5Fty6LWjtLQxUk8UDSmeGn4jX7oq2MbwOfTVPuWMT6SAxDj2iahk9tPCBkYwIYJrDdxLxnb4kH_ar1z4RjFdFP2q1VFsWYesuofmWHw1rOw_pS_pLn_LM_CY7tXa6gBSu0JQueDlUVCQHsSypWMqV6HX2zwxeIQLBu1soxQn5CExFF9T-UMx7J5znTJAWii8f36Q2xMz_G8e3U6ylIH50_tEPQzOMsE_ofBQPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
پست جدید صفحه رئال‌مادرید که نوشته شمارش معکوس آغاز شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/99528" target="_blank">📅 11:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99527">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b08f3a463c.mp4?token=vdXGsZLD_fo57WO9kkkAORR__fUvUW2ztYSEjgaW9AngBD16UGOz5o6d8BCWUt5NoQEnjzHnx825ncrBzrS7RVNBbtJiYOU3axPHghhwrP8jvHSbtBAJ7tryb8fgnYidZ7w-Kimyb3xrGlxcdjD770Wwc8-7bFjxkr31H2kD_7yOMds4WMTn_XN4mlM0vEix3MNM2FA2ka8Iy09LSpK6HGtZuA6c3J1A4MELDPTci_bckrvFjEwUuE3E1U0l0QedZN_TvIjg9LsIBbFCdIb-0aCOSTWM5M7_5ZZXxlYRWWfSw4qcLFTjmdEsyUiLGhTSNiulfXkTjLIXADKzgqAzuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b08f3a463c.mp4?token=vdXGsZLD_fo57WO9kkkAORR__fUvUW2ztYSEjgaW9AngBD16UGOz5o6d8BCWUt5NoQEnjzHnx825ncrBzrS7RVNBbtJiYOU3axPHghhwrP8jvHSbtBAJ7tryb8fgnYidZ7w-Kimyb3xrGlxcdjD770Wwc8-7bFjxkr31H2kD_7yOMds4WMTn_XN4mlM0vEix3MNM2FA2ka8Iy09LSpK6HGtZuA6c3J1A4MELDPTci_bckrvFjEwUuE3E1U0l0QedZN_TvIjg9LsIBbFCdIb-0aCOSTWM5M7_5ZZXxlYRWWfSw4qcLFTjmdEsyUiLGhTSNiulfXkTjLIXADKzgqAzuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇬🇭
پشت‌پرده زندگی جادوگر معروف غنایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/99527" target="_blank">📅 11:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99526">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4raELVTegc2uvgVC9_SYvJmfN26TgscgvoBBSDAKsRBJPQBSfbthl19G_LPEHL9FKhdLBnHttH26HHGkh97lVQRYO7kWwjNlVktM8qSUi02i30OIE5jNSn8eHlk0GfMze-9fBN7hxrmNadJUwPDvuJ8hhJ9K22-t1j7d7N_YqmW3zjCQUxh3Z2THmTcbYp6QO2L0SDYLRcg-9Sgb_jvoEqYlMrMdgHCcls4S0XaNaZYfqbOmH1AHS-L1VBQXeZiZXVawzotQTuyEvZVjuqx67ruEGTOIHG9kvB-Gc2lMLfP5BHHoPMuJOAA0b8JAKwxi96siK_OsIadaOMQoDypqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🔵
رامین‌رضاییان که برای گذراندن تعطیلات خود به اسپانیا سفر کرده، هیچگونه پیشنهادی از تیم‌های لالیگایی ندارد و صرفا برای ماندن در استقلال خواستار افزایش رقم دستمزدش شده که باید دید هلدینگ‌خلیج‌فارس با درخواست وی موافقت میکند یا نه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/99526" target="_blank">📅 11:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99525">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c662948346.mp4?token=gJR9vohaCsQz5fdS_D4ny0HKc3ifXRb9J28MosE0-3JCnpnAwp764o6CbOdNbTPW4Jk8Ivjvyxk5-MbCqBo61JDUmO0byrwnv-tGuTbNxUMLaAcq2x7VS4Cz1RTIbs_QXTS9Tn98tgs8VWvu7keWcj8Er00Ug0A8RjO-3b6u2RvW27e5mDJNFqdsawLMqZbMwtVJZzWG-kPnNK9umAvWyatGiVrDUx_TMkw7coSBmf-a7vLxp_6faYe7VqRhRkNJ4eZfJGppbz42vzY8_XRyMZoHrUJqIKfpLukx565VK4rtXSpSU6XLKftnnU8ehDZ0zG0BezufZgfqPPBgnGuPXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c662948346.mp4?token=gJR9vohaCsQz5fdS_D4ny0HKc3ifXRb9J28MosE0-3JCnpnAwp764o6CbOdNbTPW4Jk8Ivjvyxk5-MbCqBo61JDUmO0byrwnv-tGuTbNxUMLaAcq2x7VS4Cz1RTIbs_QXTS9Tn98tgs8VWvu7keWcj8Er00Ug0A8RjO-3b6u2RvW27e5mDJNFqdsawLMqZbMwtVJZzWG-kPnNK9umAvWyatGiVrDUx_TMkw7coSBmf-a7vLxp_6faYe7VqRhRkNJ4eZfJGppbz42vzY8_XRyMZoHrUJqIKfpLukx565VK4rtXSpSU6XLKftnnU8ehDZ0zG0BezufZgfqPPBgnGuPXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادل فردوسی‌پور هم به ۱۰ سانت و ۲۰ سانت معروف قلعه‌نویی کنایه زد
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/99525" target="_blank">📅 11:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99524">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjNUGhdkPWns0KQnKtKZcJypB3PmsSGEL8un7EQosS5KWmzY6rV_upWWH3y1QFcLKk1Bxu9eruw_4waFMJeq7YoqiE4__XiPAp2lCR5j86lxIA9_GRsAJaDsTu8FoC-vaXVP2HrCsudMllNHAVAWrMYk6w9-r2O07yaIP-mFwzwyEk-nG2jURjESutCkrznA2PV4Yt5LNxV0tdMV_YkWCsijskXrmKjBccKY8uxLI4ufA9r3_9vjVtypKRFWguIdCzqYtCrUXk_g0Y73-If2yCrDXk06llyRyXxdcJl83ySLU0hnrQVVu4wKbrqFq9p717-9EGko4GX4jd8Mf3upZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
کوین دیبروینه و عیالش در بازی دیشب
🤍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/99524" target="_blank">📅 11:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99523">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53dd4678ff.mp4?token=D-p6elYuoZAgW0tCPTYNFwoZRXZriruP2hiBZj_deJnI-vDHoMsbhLqFb-cAqApkOTBeqVTxZLQjq29w_8EMvXOns6wl5eLfUbBOzmiVTYGsVA-M14dB9AHcfmzTyMeTgYrwfT9nKbLnJmhdodOFjIm1Zusux8frHlv15bS7lWxKSkC8hho8H6SpcxSlHnZQTVYv8T7_lzbTgeyPUu9DfuekMeReGCyNlu-lcIHEiWHf5jD-VXsNd3Cc7YIfGNEHFCmTReZorSeZHTkljAWXGlpOIgc0Dem7Uydx-QWU2-meHauvNVyMhcN9zVxWkgkCRA4aJwEE5E4GxXJ2TKEpEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53dd4678ff.mp4?token=D-p6elYuoZAgW0tCPTYNFwoZRXZriruP2hiBZj_deJnI-vDHoMsbhLqFb-cAqApkOTBeqVTxZLQjq29w_8EMvXOns6wl5eLfUbBOzmiVTYGsVA-M14dB9AHcfmzTyMeTgYrwfT9nKbLnJmhdodOFjIm1Zusux8frHlv15bS7lWxKSkC8hho8H6SpcxSlHnZQTVYv8T7_lzbTgeyPUu9DfuekMeReGCyNlu-lcIHEiWHf5jD-VXsNd3Cc7YIfGNEHFCmTReZorSeZHTkljAWXGlpOIgc0Dem7Uydx-QWU2-meHauvNVyMhcN9zVxWkgkCRA4aJwEE5E4GxXJ2TKEpEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⁉️
رضا جاودانی استقلالیه یا پرسپولیسی؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/99523" target="_blank">📅 10:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99522">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb0798a162.mp4?token=knXj8Wj5242ZsTOI5wKt3Q-I9omgaZI1Eq0fE6NBFpxiVredNirUrwy5X6tEhUAnkqvHzQ1v0ZQVbP4BIWtdhB3vsR55UcMOykfFMK288hkABI88F0NCEK2VqW8mlSOka5SEVbWS5Q-9wLtqH99NIff2fGtikXC9hRV8I9vA5ZYPWUT_LG-XqkKaxYWv7yps-Hj5F31DeXP35lm-zX1webTqMVuUKknof07IWURnSWOie3_wMQEt2RiuHRyx65XYc6e8pRLOTI2rupBmgB8XIcNnAXxuKzT2tDXI8iGCS0W16lZABr0XibJTe7RcJDkhNpcchgEIitIxULiuowa5aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb0798a162.mp4?token=knXj8Wj5242ZsTOI5wKt3Q-I9omgaZI1Eq0fE6NBFpxiVredNirUrwy5X6tEhUAnkqvHzQ1v0ZQVbP4BIWtdhB3vsR55UcMOykfFMK288hkABI88F0NCEK2VqW8mlSOka5SEVbWS5Q-9wLtqH99NIff2fGtikXC9hRV8I9vA5ZYPWUT_LG-XqkKaxYWv7yps-Hj5F31DeXP35lm-zX1webTqMVuUKknof07IWURnSWOie3_wMQEt2RiuHRyx65XYc6e8pRLOTI2rupBmgB8XIcNnAXxuKzT2tDXI8iGCS0W16lZABr0XibJTe7RcJDkhNpcchgEIitIxULiuowa5aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🏆
رقابت بر سر توپ طلا هم امسال خیلی جالب شده.
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/99522" target="_blank">📅 10:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99521">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‼️
⚠️
شکیل اونیل ستاره سابق بسکتبال NBA مهمان برنامه ناتالی فریدمن بازیگر و مجری آمریکایی شده که برای او پدیکور فوری میده. هرچقدر از سم بودن ۳ دقیقه بگم کمه
😂
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/99521" target="_blank">📅 10:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99520">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🎙
🔵
🔴
جزئیات قاپ زدن علی‌کریمی الماس فوتبال ایران از دست استقلالی‌ها: فتح‌الله زاده به من گفت دزد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/99520" target="_blank">📅 09:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99519">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae6aa61c60.mp4?token=ErEJr7nKaKNjZdX05GwKis3o7JMqkzEsK6HgurWgcY13Bk_NRYj8IMCTdobWPtZuYj9Dp7t-rUcdcmLI6jhUaYqB5WQmp8eK9Y_qBQGFJcI6Hu9fZsOvcrLufnnWTlBNxXaPCbYUTg-cBS3XS2UOD-JA4QwWA6f8T_C1MdxZScm-ddkmlpRpE1JAq_rgQXmi9z29XCDVOMD265sMvoFXfLZDk5stQECZkEshLVd9Spj2cCCPKjwgb5gP_-so-ln5lUnh4S6uk5Hgvo4CeuMk3cu-xWIT9ylWihiDugFCgtuaTE3_RwIJLDADSBRok_360YY_6SmZR-TC8rehhTUoLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae6aa61c60.mp4?token=ErEJr7nKaKNjZdX05GwKis3o7JMqkzEsK6HgurWgcY13Bk_NRYj8IMCTdobWPtZuYj9Dp7t-rUcdcmLI6jhUaYqB5WQmp8eK9Y_qBQGFJcI6Hu9fZsOvcrLufnnWTlBNxXaPCbYUTg-cBS3XS2UOD-JA4QwWA6f8T_C1MdxZScm-ddkmlpRpE1JAq_rgQXmi9z29XCDVOMD265sMvoFXfLZDk5stQECZkEshLVd9Spj2cCCPKjwgb5gP_-so-ln5lUnh4S6uk5Hgvo4CeuMk3cu-xWIT9ylWihiDugFCgtuaTE3_RwIJLDADSBRok_360YY_6SmZR-TC8rehhTUoLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
میثاقی دیشب ناینگولان رو آورده بود آنتن زنده که یه لحظه از دستش دررفت تبلیغ شراب کرد
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/99519" target="_blank">📅 09:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99518">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29484b00cb.mp4?token=UolBJ3RWeChsZE--erUaU8DxPFVJfI1LxKXViYb8KXp9Lpu3PDsp7N9FiuJa_GtAd0uvErRQ-lZiYBP5D46hsrZIXNEw1NK6boaVn5C2tvtdMnjQBotELeLDsAK-PqjDmF2W86X1mjDlOH12obH7X1qyPfUafj4xdcm41R9dNI2C2bPudylwKlEh0BLm-rBdY1oZwOvVGWLk6L384tNv5OSLH1bOB18GkjeWoxP1eWPzG35nZqrjS0KqLQTRWDTPqlDEr4u8NWMJ_EC8MbBsj57huTJNsjlCEiNDLA0AXEIRdd73RpJ2Q8i9rmk1FkfqBgmJLLDL6TS2vWB1nQ-a4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29484b00cb.mp4?token=UolBJ3RWeChsZE--erUaU8DxPFVJfI1LxKXViYb8KXp9Lpu3PDsp7N9FiuJa_GtAd0uvErRQ-lZiYBP5D46hsrZIXNEw1NK6boaVn5C2tvtdMnjQBotELeLDsAK-PqjDmF2W86X1mjDlOH12obH7X1qyPfUafj4xdcm41R9dNI2C2bPudylwKlEh0BLm-rBdY1oZwOvVGWLk6L384tNv5OSLH1bOB18GkjeWoxP1eWPzG35nZqrjS0KqLQTRWDTPqlDEr4u8NWMJ_EC8MbBsj57huTJNsjlCEiNDLA0AXEIRdd73RpJ2Q8i9rmk1FkfqBgmJLLDL6TS2vWB1nQ-a4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🔥
🏆
تکلیف اولین دیدار نیمه نهایی جام جهانی مشخص شد: اسپانیا-فرانسه!
🇪🇸
🇫🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/99518" target="_blank">📅 09:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99517">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUC4WDf3-PcGLK_23QXtiTdVOV35UAKFZ6hudoA5hF2muJ90Y-l0dyizErwKT01iRqBcaRESUX1WGi0asxGhiNqusck-mtyrVoZZTlCA2PX6vLSLRVDMOAJsKrQGE_7OAwQxt2Ri2-vNl-xdpetqQffIyVQLVUeNBzT5NNRGBcVs7qsmnvyXRwsRO_5g4h35v4Qn09Xk7PBaer5TnZ0pZX_PrPOvO-O2C5_oKkxqvV7x4KrtAu0i8WSkMdqgyZ8RILW13E24z4Lev-6FLFFJCXFzPv6hp7Q1qc925Ry55gAfVkqI0tfGFUEos7GFP84a6SMyE6PUdgACWch0pjhhbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
نیمار دیشب در تمجید از لامین‌یامال یه کیت با امضای خودش رو به دست ستاره اسپانیا رسوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/99517" target="_blank">📅 08:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99516">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3f60623d0f.mp4?token=tiir0bV6ogWC3kk_0I19Ra1QT40rCrahw2EoKcMSO3fyy9o9ECS2_B8ykZqH0P3-Gy81ixkO-vuYMyLKIRilVWRDCn_myhyKhaNeTJH0HpLB1310LnMhX0JYVFW_fRamafWeGfE-RdhIu-RcRR9x7bbgYbOm_6RbfpmKjLTp2-Dce-ZEPW9UOwUOrO-bH96CS2_k-I9dukItFW1H73-ON4Gu7oE7alW5Zx6g3IM7jm4Un57JKV7AEUaqJoSAhGoN148UdzajC1nQQIHv1jWcUbinZ9z4uAqJn54Sebmd8vwa64MYr4i9Aa6dS7ODBVhVDiE6IZS_UTwzEA5o0P20qg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3f60623d0f.mp4?token=tiir0bV6ogWC3kk_0I19Ra1QT40rCrahw2EoKcMSO3fyy9o9ECS2_B8ykZqH0P3-Gy81ixkO-vuYMyLKIRilVWRDCn_myhyKhaNeTJH0HpLB1310LnMhX0JYVFW_fRamafWeGfE-RdhIu-RcRR9x7bbgYbOm_6RbfpmKjLTp2-Dce-ZEPW9UOwUOrO-bH96CS2_k-I9dukItFW1H73-ON4Gu7oE7alW5Zx6g3IM7jm4Un57JKV7AEUaqJoSAhGoN148UdzajC1nQQIHv1jWcUbinZ9z4uAqJn54Sebmd8vwa64MYr4i9Aa6dS7ODBVhVDiE6IZS_UTwzEA5o0P20qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
آغوش گرم لامین‌یامال و تیبو کورتوا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/99516" target="_blank">📅 08:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99515">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
📰
فوری از فابریزیو رومانو:
👑
- باشگاه الهلال خواهان جذب رافینیا است و به شدت به او علاقه دارند، اما در حال حاضر، رافینیا تمایل به ماندن در بارسلونا دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/Futball180TV/99515" target="_blank">📅 03:12 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99514">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v72NApHhe8RnOr1iLOI_Ii7tjDcvLqsBiRSiG9i4TEoggQVPT-ZWTWmZYqFee8_jiTEd86AQr4CMBtMDef0kCBNwYCPLsJ7GoYQFVrcEfMC71tIKBBARR-SHh3t47KxnQ55G3KEC4FAg6FVQW33U1XsZDFR2v3ETGN5djpI6g5909kFirmkXXSwLoGSLgiACcQraCULQlxy455EdJKwAT7BsHDyv8328honIkGoBwSs86GyVBQhgpuvh9npaarzcmThyvClueUcNiRjpAF2Er_m4zqpvcSbD33m8Ipg58tC-bzQMq6QIJYnH1QMJfjAv8D0DNZHYASb6mkPEBTVKTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📰
فوری از فابریزیو رومانو:
👑
- باشگاه الهلال خواهان جذب رافینیا است و به شدت به او علاقه دارند، اما در حال حاضر، رافینیا تمایل به ماندن در بارسلونا دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/Futball180TV/99514" target="_blank">📅 03:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99512">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGWeiIZ0wlmDWOylZb2VBVckPdpl5FgaAzThYtn56vcB1r-cgpQmo17K6FPQ7UTutbPpDvoVtshyVTFlgAOCX7K_5aTs5veWmdVaJV64Hd0bZ0cl4m4A7UmfZ6RH5pL4B6tg1SWunjyaVAoEWVtLBBX8jH1YThGwbHHUJsmlRw5zZ5DfEHnCmbgp7Gp-HKC2Y8xn6S3FVah9PQDEpNDuJMtAvgnlvZRfArM1uGxFw2A-orgW_BuOTDlS0mQlTe3G6EerjcQ1QuVNOhy7ccEXu2sgqUJCPjPxv9SuD_CuhQH1S1_uhgRc7PSkz9lex7G_8s2pvafCFCi9kef5BybfPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔵
رومانو:
پاریس سن ژرمن به شدت به جذب فران تورس علاقه‌منده و اونو برای جایگزینی گونزالو راموس زیر نظر داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/Futball180TV/99512" target="_blank">📅 03:07 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99511">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bf_ItwC7H41cveuPDePYSgOmrcBDGZpJw-hZW93nK6GqC0ZK9HldVZULiHQKG0GA0u7FbwpzZ0uaRtGLCoIodY6GCzD6aPABDpdGxZKrEB0Lr4Rdn1NRSRmlF_s8PdX9LiPOU3iwTYcaDIL4HgwJeEsG0RuNC6zf3x5dRcoiIxkEIbFDMe-YHwCM7E-wFr06-XziM6XAWiikJUN2lxsGHgazWOzyPZQiIuvIG4wJ5C4ZYpzXKkLg4dkUw5-3CYz3G9DUL4RqulPrHImP0r_aUTo9BnCOvAMcK0ZLZYPa8zodyovUgrHxUCC_asLJF6qtq4fIQ8PSvn4Gm-qzmhUkEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هالند پیش زیدی بوده که یکی یواشکی میخواسته ازشون عکس و فیلم بگیره بعد هالند زودتر طرفو دیده و از یارو و زنش عکس گرفته گذاشته استوری و نوشته هی یو
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/99511" target="_blank">📅 03:03 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99510">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d0867b13a.mp4?token=ORvTuZr6rX-fLIZaEwiYSbfEVB3rvHnLQcxck1PC4LL8CU49t38ng1s5KrCVUP-Bf5tu4aXoNqtT-OWbGn0Ggt0RJymoWOlSxcd5eBM3Tw34eegD4_fn931MLy2nElIAuEUBobJ_uFiPnAiInK8UEgsb1fYJREFtBG6rlT9xP69TRZIQbVM_ZV2qpRlFHfNlv3GPFq4fZ_4J9bFryt_zfgstOfs9ksLbGYq9GfZKYL5qzf4qrpJvSyqwJY_k1ZjsMH1Qfoh9UBYeYcTaIKkYQ_iaEywobL5E3KlpdKerrZooDDbV7MGe4YoBwxjq7Ugdni2pfvdmEPA9VGM30xcqPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d0867b13a.mp4?token=ORvTuZr6rX-fLIZaEwiYSbfEVB3rvHnLQcxck1PC4LL8CU49t38ng1s5KrCVUP-Bf5tu4aXoNqtT-OWbGn0Ggt0RJymoWOlSxcd5eBM3Tw34eegD4_fn931MLy2nElIAuEUBobJ_uFiPnAiInK8UEgsb1fYJREFtBG6rlT9xP69TRZIQbVM_ZV2qpRlFHfNlv3GPFq4fZ_4J9bFryt_zfgstOfs9ksLbGYq9GfZKYL5qzf4qrpJvSyqwJY_k1ZjsMH1Qfoh9UBYeYcTaIKkYQ_iaEywobL5E3KlpdKerrZooDDbV7MGe4YoBwxjq7Ugdni2pfvdmEPA9VGM30xcqPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😭
گاهی پایان، با یک سوت آغاز می‌شود...
🔻
امشب فقط بلژیک حذف نشد؛ آخرین جام جهانی نسلی به پایان رسید که سال‌ها از آن به عنوان «نسل طلایی» یاد می‌شد. نسلی با ستاره‌هایی مثل کوین دی‌بروینه، روملو لوکاکو، تیبو کورتوا و اکسل ویتسل؛ تیمی که روی کاغذ، توانایی فتح دنیا را داشت اما بدون حتی یک جام بزرگ، صحنه را ترک می‌کند.
🔻
سال‌ها امید ساختند، لحظه‌های فراموش‌نشدنی خلق کردند و بلژیک را به جمع قدرت‌های فوتبال رساندند، اما جامی که شایسته‌اش بودند، هیچ‌وقت به دستانشان نرسید. اما بعضی نسل‌ها با جام‌ها به یاد آورده نمی‌شوند؛ با خاطرات، با احترام و با تأثیری که برای همیشه در تاریخ فوتبال بر جای می‌گذارند.
🥂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/Futball180TV/99510" target="_blank">📅 02:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99509">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_K1MWod9XJZ_1JhFBnWrgfVizwiXiJxRx09jJEm1XprnjtHqbxr1nSQR_a0DXgnZ31xRMYXAzdXg9jzYuvpNmeDjOgcLVp_qIjm1U3bDpbVe5VQGvrEg77Bx95iPJCuYf14FXIv88ewxFrWzC-ajsJW39-G_ZRS76pIovxbGp4Vi7aPOSYuhSQmqRLn05jLen9OwmsYT2nQZVoLTU8m3IqeZFi2JiEux8K4IE2MovH8tZy8YPilV_9CFS2DIWd9vzcbDTYMDrf-soo8LItLW13N0UpoSU8pzmmgE3zvxlyftPWPz21GuWR-DsISxY5l_5la0LVTbAHBCr8qeIsdPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
طبق اعلام رسانه های نزدیک به بارسلونا، فران تورس از پاریسن ژرمن پیشنهاد دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/99509" target="_blank">📅 01:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99508">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
طبق اعلام رسانه های نزدیک به بارسلونا، فران تورس از پاریسن ژرمن پیشنهاد دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/99508" target="_blank">📅 01:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99507">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2Xa5eV5YLNPHRkG_co2kfAYo0kJxUU_fJbtxnBRJIOOuLFumH0vXb-RMkAXIm1g_K_d-d31BQ0Ea05EM6x-LfwdJX6xzg5OPGMzVKOGeyw7euEQkOBGwLPgJz9CLTvlTr6OAKtTv5NMBiZ9akmYYBtLEjutRLExhut4PIzt5yl8NtTIwL3InyieNK-dcSxH0R5S3BhQuwzMf4nAydxQJCDLbI4TLDhFWMRfEXy1V14cusk4UHlG25gKKoiI9WZdpmFtynzal5nTW3UlYFB6X_XXHxTS3Crzw_y93kcMPsusEHC-iBH91GTFAa2Njw1BF3Hp2StpN4dyClkSVNWd4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
16 سال پیش تو چنین روزی اسپانیا با شکست دادن هلند قهرمان جام‌جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/Futball180TV/99507" target="_blank">📅 01:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99506">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBAN7dDqKZDFmvDE_QKT0QkRGxJ9kcuoU4THoO62cJvOmGx8M7PU3bMyjOUMTD_lP3LxJ3UKCQmCMngFrEQWdnmQJ8utg6wG-wG1Z5J4jV4vEWOm693O4D2t0FFA3iJpVFm8LTin_tXtxrVxMHnAk83pArJbpUWbzNfc8AHNkICY_8YyhhAABK5oojui0U4KKd9SD_WRLJokDS0OVWHckbKODCsZfod_zU45zZ5oVx0_UCqblGkKnzQlil7bTRwiZd81zRyZt9-qHss-H9eXNFSTfYF7JjvSwQ5Nw8wIyfp3dbcHGfdTp8QqOoOuAxYLPWD8XWE01kiup2vU7FY_xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
🇧🇪
تیبو کورتوآ: «می‌خواهم یک سال کامل استراحت کنم و در هیچ مسابقه‌ای با تیم ملی بلژیک شرکت نکنم، و سپس در مسابقات مقدماتی جام ملت‌های اروپا و خود جام ملت‌های اروپا در سال ۲۰۲۸ شرکت کنم. نمی‌دانم که آیا بلژیک با این موضوع موافقت خواهد کرد یا خیر.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/Futball180TV/99506" target="_blank">📅 01:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99505">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPgQMe5-oX669ui2GaWEhkuVAC8Do0F3fbpjQn8eOTe8UvHez_DpOqFwygjtOb30lqbTZ_4Vm-OgHtdu4YRJyKu5i1AXh0gMRje0Vq1Rk2vcbl0RnldkfGBYxdag2vv0qvkYr77b-OPRVNDKhAN0iLCSCxJqbnthuQ9keYQyXqb1G48AG101dK4eOla_IfoLCDxP1iXjfKdYvjE1Q8Np96nsJ_HPaYiF4b8QOHPQMqnUfZJ9i2ULpGqLqpeAWX7EnC82tzvmlfc7ATJYNtDTBfDX3mldJhEUizTVeOl5ngraTudxAW4wVBmxKhRlJ5Tztq75BRtNIBArvylHsdapdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🚨
🔥
🚨
🔥
🇫🇷
🇪🇸
لامین یامال:
‏فرانسه یا برای بار سوم متوالی به مرحله فینال جام جهانی می‌رسد، یا ما آن‌ها را برای بار سوم متوالی شکست خواهیم داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/Futball180TV/99505" target="_blank">📅 01:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99503">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
💔
💔
اشک های تیبو کورتوآ پس از تعویض در دیدار بلژیک مقابل اسپانیا به دلیل مصدومیت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/99503" target="_blank">📅 01:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99502">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWYTTRSLUTgLEB42QmrPWvy2WiX3S-hPQP6IIsOGGEIZ2NOAELDYnRLvcKYaCql6DBlJpTbj4TCOeapR1KHKzjkii9QNbARmLns5lJIwbcJBDNd_2RWB7HGQALxPfQ9fqS6lAdr8nStDY7v4cYknFdkIV8Zgf8mSF0VtTdrTfgbJaxmTo4RSSvLLzdeulo_F-sgOU_aYzCLJQ2k2gM4TJPTLIoxLZy1kr_cjHVgEoXNtaEYeC9XQStlSpU3aY5y_tAcXa2CltkXCUyt068L0kGPUKaum6FymYFgsqF3OoGR6lobXMrVTU1ktkwPUt9AiK-y9SkhRj9QmL244kFqEdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🎙
استارت رجزخوانی لامین یامال: « فکر می‌کنم اگر فرانسه قرار باشه از تیمی بترسه، آن تیم ما هستیم ، چون این ما بودیم که آن‌ها را حذف کردیم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/Futball180TV/99502" target="_blank">📅 01:06 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99501">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b961be455f.mp4?token=Sjxjhg2PzdDUO8wfy_VXUeRtxp2427dWqgxQ0te_6Dq39IFAatBJ6q9nk80UpXbg37fQEz47iun9DfmeqFi2Uin9MfHKPTIIIRMmvCXoDR98Ic1BWFrchDXmXjhEPdw_2-zh2MzUeWXH2x86o35CJyKF2lMKJ5fWRRnl4htu9D0b_xacLGe5K3F-Hl02-P5_IQ2jNeHNmmTJs53zR7wiT4ZRKRUpUeomQgMlvIMZQdkeGJmwmJ466vV1TUCuo3yPT-KFKVrcKAG-fpavcSn7GF6ubixwy2MaeCOts1F8e28A9HZ-CSiQbYn9kNn1rUHKdXNtA9hq45ViP-Iu1VedHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b961be455f.mp4?token=Sjxjhg2PzdDUO8wfy_VXUeRtxp2427dWqgxQ0te_6Dq39IFAatBJ6q9nk80UpXbg37fQEz47iun9DfmeqFi2Uin9MfHKPTIIIRMmvCXoDR98Ic1BWFrchDXmXjhEPdw_2-zh2MzUeWXH2x86o35CJyKF2lMKJ5fWRRnl4htu9D0b_xacLGe5K3F-Hl02-P5_IQ2jNeHNmmTJs53zR7wiT4ZRKRUpUeomQgMlvIMZQdkeGJmwmJ466vV1TUCuo3yPT-KFKVrcKAG-fpavcSn7GF6ubixwy2MaeCOts1F8e28A9HZ-CSiQbYn9kNn1rUHKdXNtA9hq45ViP-Iu1VedHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداش یامال چرا اینجوری میکنه
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/Futball180TV/99501" target="_blank">📅 01:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99500">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87d00634e4.mp4?token=d9mVxxK9JitbJZv1CueFEG7_hhVGS8KoLxywUsyGNkUmtm4U279DrVa50zgZZLZYtf_mHkk7njX8jenACH3-pbzHPFJBCLCYCSDa6W0US6P61gtPxXTUEYD0mzQclyBWWFw9gVcWJJl41cFjPiB_13EAoGhxI6SA88PDAnpufe2pNRKpsM_O4dZDPUmqIEG7TzMlJtKenArq9vhUVXopZ6KtQDFuaPeH6CeI8wGVKuZzq3fKXQlGhhe68MHGnv-QY1j2E7AftGEzXwScZCXDjjb-LFEOuvccgignJTjnFCEJhUHKeTHolYxBUJVSGtm2RM9mAMP2sb07uV5RJyB0yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87d00634e4.mp4?token=d9mVxxK9JitbJZv1CueFEG7_hhVGS8KoLxywUsyGNkUmtm4U279DrVa50zgZZLZYtf_mHkk7njX8jenACH3-pbzHPFJBCLCYCSDa6W0US6P61gtPxXTUEYD0mzQclyBWWFw9gVcWJJl41cFjPiB_13EAoGhxI6SA88PDAnpufe2pNRKpsM_O4dZDPUmqIEG7TzMlJtKenArq9vhUVXopZ6KtQDFuaPeH6CeI8wGVKuZzq3fKXQlGhhe68MHGnv-QY1j2E7AftGEzXwScZCXDjjb-LFEOuvccgignJTjnFCEJhUHKeTHolYxBUJVSGtm2RM9mAMP2sb07uV5RJyB0yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
MOTM
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/99500" target="_blank">📅 00:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99499">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPr9XbRFvYqsTGwSSwh2xeX4ip1kH_uLwVdvecrW0uZGPu1UkSD3BQfq_ROW0cy_ipKsv5lwhGPOPjQQAfsXWLTOK_N2tNag5Bkn15kDfHihL3nNj8DnTZ3oOrgmvbc7QumxOCO-u4yqGFusYoFQOGO6lQh5RNjYQhK2IUHwMZxrP1Ky6xip5ZZP5TS3vyrByAlJ-I-wE3mCylwQsLchblQYbHTsaKn7PmzvhkcHZ6VPGm_CHoIPl_ykwXp_YJvaRoXOKjM6sqlSY_yTBG5eudLzvqxkuU19GQUwgIYDzt6j78NbINdUSgeb2REWc75OO-RWcSp3J-XL7w5N-OOnLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🤯
🇪🇸
فابیان رویز تا به امروز هیچ مسابقه‌ای را با پیراهن تیم ملی اسپانیا نباخته است:
‏
📊
48 مسابقه؛ 33 پیروزی؛  15 تساوی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/99499" target="_blank">📅 00:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99498">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">📊
🇪🇸
مرينو در دو بازی آخر در جام جهانی:
🇵🇹
در دقایق پایانی بازی مقابل پرتغال، او یک گل زد و باعث شد اسپانیا به دور یک‌چهارم نهایی راه پیدا کند.
🇧🇪
همچنین، در 5 دقیقه پایانی بازی مقابل بلژیک، او یک گل زد و اسپانیا به نیمه‌نهایی رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/99498" target="_blank">📅 00:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99497">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNok2vkMAZw7eAoHhImyh7df6rvsVUU59gisHvHQxlEIy2JQ1-KKsrdt0BvqT7xXmjgpQy0XSpAqt-h4DW_j_n-whEAL-YdxVtKtWTkbLpF0c7FcVB5iQPBoJkyXUJbYsn8IJeGzTjaUOdX68PinPfQiBDequ6nt0SSmP7ZfsAG5smYDnxhvILl9AEXtFpZ4XvlabvLodt0Go0hCplKWlSdzAOP_R0MsQWkpj1XCq3jB1YIb9l_UdASexxdRJQXfOkES6WaxtySNtzmtFLrz-qa3YzXyAor_rbjcenBaM_jG3suj2phmCBztPx9idP2XeY6eXL5pj4-H7OjxGowIyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🔥
اسپانیا با پیروزی در این مسابقه، برای 36 بازی متوالی، بدون شکست باقی ماند و یک رکورد جدید در تاریخ این تیم را به ثبت رساند.
✔️
‏آمار این روند: ‏27 برد؛ ‏9 تساوی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/99497" target="_blank">📅 00:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99496">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app.apk</div>
  <div class="tg-doc-extra">51.3 MB</div>
</div>
<a href="https://t.me/Futball180TV/99496" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📱
اپلیکیشن اندروید بدون فیلتر لنز بت
🚀
🛡
ثبت نام آسان و سریع
✔️
📱
اپ
ل
یکیشن را روی موبایل اندروید خود
نصب کنید و بدون نیاز به
🔤
🔤
🔤
وارد سایت شوید
💬</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/99496" target="_blank">📅 00:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99495">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/iQZNgTZMorRxY1wjN7YzG-qX6ZaR--A7crMAfrTMiFQ_qYsE7Ar8y9ZeuluB4Voo8lmRmTWZP3vZXAjU7Qvvy4I_mt8hqAQN2B20Sez7L7vtftkHQKE2ImAy0OZxvqxDk6WpOKypn9FNhSkwX589-j7CUdUPWV720WB8ztDBB5rtX2wq_tdZH86WAyRdbNE2wiOKmuYokDKITHpyIlxelPuBkcxoZJsEhs9ECEyYKUX1A28yHlUPEcu-UZYpW1NO-BfMTBwpYevbfAaSpTBjjXwkDviKTXB1l1gSiQkfWlnqgtJzPMaLdBd23gndFaoyp9Zi08b-0SeIOfa3vtU_qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
قهرمان جام جهانی ۲۰۲۶ از نگاه شما کدام تیم است؟
✨
با پیشبینی قهرمان جام جهانی شانس چندین برابر شدن بردتو امتحان کن
🚀
💥
متنوع ترین آپشنهای پیشبینی در
لنزبت
😮
بونوس
🛍
0️⃣
0️⃣
2️⃣
خوش آمد گویی
💯
بونوس
🔤
0️⃣
0️⃣
1️⃣
برای هر واریز
💯
بونوس
🔤
0️⃣
0️⃣
1️⃣
کازینو
🏦
کد هدیه
0️⃣
2️⃣
🔤
🔤
بعد از واریز
🔣
0️⃣
3️⃣
کش بک هفتگی
📇
امتیاز وفاداری با انواع هدایای نقدی   روزانه مخصوص کاربران فعال لنزبت
💵
پشتیبانی از تمامی ارزهای دیجیتال و کارت به کارت آنلاین برای شارژ و برداشت
🔤
🔤
🔤
🔤
🔤
🔤
🔤
📱
@lenzbet_official
A19
📱
https://www.lenzbet1.living</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/99495" target="_blank">📅 00:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99494">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3mkvNFx0tp6lM1luMY2xDP-inj7qi8y5MBlVdPatlTXmnNBwVV5SrpRZ94oOWwTs-kpCqidwJrdlSYuFIAgqD5ZRwmJ9soJBrKSFwKpxQoJNSkk7ITeI4x5KMixDia5GvG-6yRrHIjhIitA23L9Cv6D1bwZ-o6Gd-FLVRjVD8oy6m-CmF2FT15xhzcZ8DEzrmR3iqtIF053MEBpSKG3g5TtS2I7RiMmGsLynQ_9agiBFFASHh7mQTbLH6tmOIi4utZ4UFvTgfVpUfJMFiqqP8H6zTLPgZW5b_jSIzrVleOCmCiWQEnbiIoN240_Z_F4G7P4bAellN2poAdBoev1VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
در 11 بازی اخیر که لامین یامال از ابتدا در ترکیب اصلی تیم ملی اسپانیا حضور داشته، اسپانیا در مسابقات بزرگ (یورو + جام جهانی) پیروز شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/99494" target="_blank">📅 00:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99493">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
؛ دکلان‌رایس، مارک‌گهی و ریس جیمز در آستانه بازی با نروژ به تمرینات انگلیس بازگشتند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/99493" target="_blank">📅 00:43 · 20 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
