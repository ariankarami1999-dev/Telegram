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
<img src="https://cdn4.telesco.pe/file/uhDvF0Gd3UEBtEBFl4Yp7Sh3i_muUp38zvdlXLEKhGwsCO4Ia8JfvG34n7f23tFfktpfRgkygpIhV9EDe_JocDXI037w3kc47LmuKryf5dRDQh6pRb7vApZMvyt9YWo7sTaQ3B4Le138NoBtqwFFM04DJ0-y_wx8KK71UMidxZ38dfLtUAVygO2-GAfzrMxg-IJEWKMp4Bv-o03ShPmVM3v-U9REKx8EBRwDZJcHkXLRwoDflmxT852VRvjgKHrAONAnk_15mMLOvMtILUjhDlz8jxqEL_2-er1RINOdbdc8KpLlMrtAjQEgKg0kCvB4lUzADkKyMbtWlCgTZyXukQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.3M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 08:10:41</div>
<hr>

<div class="tg-post" id="msg-672419">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJ8lcpMsasV0OZj7FKOfTUovlYzBXvod9pvTY8O7UgGZv9UcP2EGzkP0XEH9wh9aczjUJaolfp9dNwM9YdBMjlbRDpnCyQwfXLW1yZZIid5zNol8805YoEc6NHIX3S1je1KJTJjPzF5TD1DZDPxQ3ZCyPP72M-uMKAjT5E93fYE4TEETgJ2YfhSDzVYpEHvMBDjWLJe2mxjGJrbv8xLZlghj2c29bJaDrkttUQW6XAAJxyt-v62vFRIvyNG4bAyvO3xorqD2oHBkYjBW1-ytfZvO4zzj-WTRWICCs4othK5BiLHHarNFHcTve9Dmc5hKpqaojQnp-HWCv7T5ZpKpvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پوستر فیفا برای فینال جام جهانی ۲۰۲۶
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/672419" target="_blank">📅 08:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672415">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fANLbCzYD8oJKkd_c0fMH5RNw-6wDkrbSHGxqlbsXwCR5sQe4D0nNV4FVynLn8-T5Z4VuvDce3pcFH2_s7PUtGBsYB9YwD7pc9Jhq8Ny_EovsOmBnuGPWJcHHMHhq4I1gAokVUHm8HnDtaEl58eH3ojYg8dvh-_bvMv3VejYKiYUyOnRhaljhfBhULfLm9Tb38E5X8m2fLC2GeFDY5gzpU54SGtVbRuyHAnolmbSi9FMbL91Xh66k_0wbPl4kA3W2h2-GNx0c2Vwb74g3Ps0KfqLksmcdBtUPbi1hBh3lYaIb_4x8WEBI44gdevT6ljd9t4o5szv_u2lrCggHz4HgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EzgWd8fR87P6dxGGex1G2AfIwh28zRw7KfvjEB6N55uV5hBy_QmtKk9pNbZWfeaDvJHFqjIKYCOpw79qKYO4rUARfIZMpB2t0gfFiYNdQzAKOKx6bHIH48JcaBt4LyXTPXsB9GNa5kxYx5HdujQ-8cBvsTkCRqDX210HNTK95C2Nc4XWon3n0zjtJ9XOLEnAxXWwiBFok8S_6A5Y8CPIfGY4W4oBgsuC-akZqotvy5oQiaq2vxML3lr2qeXSgDQfs9bs11fsNRZspGT0vJ9mRFS2ZgdjjY7TbwH0B3vuod2jx1cWv9F6uj5tv1z2HIBzJqLwot4HLWrNFAsumzZWwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jnk_d4U-VBw8yBgabeNrp8tm_tVLbAfi-YLRnp7UX2UJHs-Jm5xYb60y3E-0E1SOEfxUaBbac_yT5SGekFOKc1TKPU8tpecks36k0-03JVNv_SUd6v5-nG3gwylUEwEoaRr_wznomurZdBY1V_m7SZoret64hs9hhJzgf7tGR6j37IrZ6xPTB0687fd06KuGx35vnPjkFBSMrz-ec5y5lm8lmROj4al6rMx42Lr4AX5BSLnTVV434ULZk3hHaWss06GjmU5ORMRu7FgTL7QAZ6rB7P8CfmvWlyKikI0R__1y39gQsSAndZ9BS9sWYFnZRXGgjgQZU5W7dl7wzjYg_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a69e676ae.mp4?token=URt1GuT0izhNq1iKrXlPAeCh1hLsWeGmeHFuSPhvT8YhXwIxwKfqmaWqcIvOMqIPBmfkYmMlyPu6v-xqwqVtS_-Zx8t7SKZh9sDUUEvsEibdjxhH1MdrcSAVnyNLvgakxIyhZg6Zo6Pg55RLIJfNnZGVppCS7FAsYCSWYYdi3_smXHo4Tf8s8EGat3oQVHQZORknNsVh_np299TnnNQRlTmnPChrR4GeKE5Qz4KOcTWfaqT613660SS7v8TV5EZ5xdpLzL4DGn8ORlFjDJMKgVbsNfLb67JSVwqZOSggxCWxm0Iy_qwVvi6aqf4lj_QB7Fa4ISceanu0poqNCdM-Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a69e676ae.mp4?token=URt1GuT0izhNq1iKrXlPAeCh1hLsWeGmeHFuSPhvT8YhXwIxwKfqmaWqcIvOMqIPBmfkYmMlyPu6v-xqwqVtS_-Zx8t7SKZh9sDUUEvsEibdjxhH1MdrcSAVnyNLvgakxIyhZg6Zo6Pg55RLIJfNnZGVppCS7FAsYCSWYYdi3_smXHo4Tf8s8EGat3oQVHQZORknNsVh_np299TnnNQRlTmnPChrR4GeKE5Qz4KOcTWfaqT613660SS7v8TV5EZ5xdpLzL4DGn8ORlFjDJMKgVbsNfLb67JSVwqZOSggxCWxm0Iy_qwVvi6aqf4lj_QB7Fa4ISceanu0poqNCdM-Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر دیگری از آتش در مقرهای احزاب کرد مخالف ایران در اربیل و سلیمانیه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/672415" target="_blank">📅 08:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672414">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d5c6c882c.mp4?token=KRrYMUv0vgTKooA5mno08SzScqcqn1ihSBdWXfYzIEEMRsvTmJouqtBj1zCt39Df9x253xipVP8LdGFwtaWHdUYqOLGX97YOhg94fQTQSChAiOtqbYxkCiebIoK8ojngt5EkbHj-n1oxq1DmSAAvg6NTNHmfwJJvFDKOFq7nPBKnykegyD9DkcR5kYPPqwlT1vk6esP8TPxZO0tRVCLCgVstAybGcZWZQIwPgvHxtnSDJ6--NqI87tSz4kbS9HKu3eCIvdxUkBSeg98JrY7tFwVTxkO4Hr4qCAGM0jQ9_n7WpI-IQ_eAfZWlfaHQUNVk2G078LyHty2dOXsuTKI6-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d5c6c882c.mp4?token=KRrYMUv0vgTKooA5mno08SzScqcqn1ihSBdWXfYzIEEMRsvTmJouqtBj1zCt39Df9x253xipVP8LdGFwtaWHdUYqOLGX97YOhg94fQTQSChAiOtqbYxkCiebIoK8ojngt5EkbHj-n1oxq1DmSAAvg6NTNHmfwJJvFDKOFq7nPBKnykegyD9DkcR5kYPPqwlT1vk6esP8TPxZO0tRVCLCgVstAybGcZWZQIwPgvHxtnSDJ6--NqI87tSz4kbS9HKu3eCIvdxUkBSeg98JrY7tFwVTxkO4Hr4qCAGM0jQ9_n7WpI-IQ_eAfZWlfaHQUNVk2G078LyHty2dOXsuTKI6-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برنامه یک روزه فول بادی بدون نیاز به باشگاه و تجهیزات
💪🏻
#ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/akhbarefori/672414" target="_blank">📅 08:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672413">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
منابع رسانه‌ای از وقوع انفجارهایی در شهر الخرج عربستان سعودی گزارش می‌دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/akhbarefori/672413" target="_blank">📅 07:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672412">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
اطلاعیه شماره ۲۷/روابط عمومی سپاه پاسداران انقلاب اسلامی: کشورهای میزبان نظامیان متجاوز آمریکا آماده دریافت پاسخ متناظر باشند
🔹
محل استقرار تجمع نیروهای متجاوز در مرکز پشتیبانی نیروهای زمینی در عریفجان و رادار پایگاه علی السالم آمریکا در کویت منهدم شدند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/672412" target="_blank">📅 07:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672411">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
زمین‌لرزه‌ای به بزرگی ۳.۵ ریشتر، صبح شنبه حوالی شهرستان بندر خمیر را لرزاند.
🔹
احتمال شنیده‌شدن صدای انفجار در محدودۀ جنوب اصفهان/ مردم نگران نباشند.
🔹
خبرگزاری کویت: آژیرهای خطر برای چهارمین بار در این کشور به صدا درآمدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/672411" target="_blank">📅 07:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672410">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b822dcfe2.mp4?token=ppPxUvAJlJe4HYdY5HGbBJIM31q0FbtBDxzdG9A7f0pkFN_vXrbLwqrJwxJsVSr7aCy7wZ5fPqiXFVXwhPVyjqy8iyDTEbBsbzfSuIJGpIQP7bNx86ecejZgKdlaEvL-Gc8zXq7FoDwAGk8MJg4NfJrq20ltsF7nPy7z6w06r4PtSZnPo3gKNFa9rOOr812VQ2x29R8mCyhY5J6F8rvAKJVVBovUha0zmHqsTWjdHvLweTlR0HrNUE55XH0dQcSnTVdKZEuzVqnL4c9Tx-o3xpUweDjAVhbwV6m7CihXdsYYjW4GrFS-xaQfXvRtEztYkFv77oQC3nUa7f7we6YivQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b822dcfe2.mp4?token=ppPxUvAJlJe4HYdY5HGbBJIM31q0FbtBDxzdG9A7f0pkFN_vXrbLwqrJwxJsVSr7aCy7wZ5fPqiXFVXwhPVyjqy8iyDTEbBsbzfSuIJGpIQP7bNx86ecejZgKdlaEvL-Gc8zXq7FoDwAGk8MJg4NfJrq20ltsF7nPy7z6w06r4PtSZnPo3gKNFa9rOOr812VQ2x29R8mCyhY5J6F8rvAKJVVBovUha0zmHqsTWjdHvLweTlR0HrNUE55XH0dQcSnTVdKZEuzVqnL4c9Tx-o3xpUweDjAVhbwV6m7CihXdsYYjW4GrFS-xaQfXvRtEztYkFv77oQC3nUa7f7we6YivQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پس از ادعای خوک زرد درمورد گرسنگی مردم ایران، یک ایرانی در خیابان‌های لس‌آنجلس با پخش رایگان پیتزا، پاسخ خود را نه با سخن، بلکه با عمل داد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/672410" target="_blank">📅 07:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672409">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
سران کشورهای عربی که به دشمن پایگاه داده‌اند، قاتل رهبر ما هستند و باید قصاص شوند
🔹
جنگنده‌های آمریکا و رژیم صهیونیستی برای ترور و به شهادت رساندن رهبر و دانشمندان و فرماندهان نظامی کشورمان از پایگاه‌های این دو در کشورهای عربی پرواز کرده بودند.
🔹
بنابراین سران این کشورهای عربی که پایگاه داده‌اند نیز در شهادت بزرگان ما شریک هستند و به عنوان قاتل باید قصاص شوند. پس چرا به قصرها و کاخ‌هایشان حمله نمی‌کنیم و آنها را به جهنم نمی‌فرستیم؟/ روزنامه کیهان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/672409" target="_blank">📅 07:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672408">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTXGlnSxOtfom2XidjoaMWa1Tj96_sxNP1FZOxjt-Ls1izPKGSmN1nlOXyBtExObG0H-w2PZGwhhy4-CpxMdOV172cBhWe9CcTAU5T0xqExytNC_URIdjOkd4Ktf3Ed9mBbk8mh1dM3IbngfTH2mgDEXgAimFnXaBMoENGgi5gVqsobnBL8CVlZH8RIxIUCUjvBVkchkn7_eYExREX60xNERQP5-pCg8Rx9HHEkrXp970tCnXD6rw1sbbql8bxnqEOTUH3H9Auv-Gtz_SoCJUNVcMlLSwAllVmT0YPYE7htcSeJR229I6vHPjBNXtjDeYnYLKYeoiRemJrKxBoLclA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز شنبه
۲۷ تیر ماه
۳ صفر ‌۱۴۴۸
۱۸ جولای ۲۰۲۶
شنبه‌ها
#دعای_عهد
بخوانیم
⬅️
متن و صوت دعای عهد
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/672408" target="_blank">📅 07:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672407">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ex5yEYOdO6PE32UU3kFxaOTf7fX3CGgOEo5cuZhuzq6RpDnHapE98VE3CoOzd3OK8GGXHyoxzXLmhXBCz7p2uCylpzRL-NFxB0EPMppR4RFLCdZ7xttHM4YwhEQ5QE-luUK3lfNCGo2ggND_8g5Qz_v3MP3kZ9k5GRq9bdYNUckw2JtVLwBA7emnhVZZiEuJMEtKqHI9ZliOrUhm0YT3-A4rA735w1Q1Sm1l_WSA50qMk46T8Zlv3aFD0ejrHmT9jyydmBShjYyy4v35ZLVx4I0ilxa0cdmhQ3vsQ3ye0-IvTmoMJPnrWHLhJzVwsGhjT3k-HUVqK4PPhkAniPTr8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
منابع عربی: انفجارهایی دوباره، پایگاه‌های نظامی آمریکا در بحرین و کویت را به لرزه درآورد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/672407" target="_blank">📅 07:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672406">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
منابع محلی از حملۀ مستقیم موشک‌های ایرانی به تأسیسات آمریکایی در بحرین، و انفجارهای مداوم در آن محل‌ها خبر دادند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/672406" target="_blank">📅 07:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672405">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d479df485.mp4?token=j_0W1YJKET2cZCZtxiYUF8Kx7HFPp5-5CsfJfexdIsynqbtmEsPSQEGYslFsgFWx_il9Lc8kStR4jcn2Q1NOGlEVACg9omY6DMuWVbaWHAAPKMZ1C2Miiw5lmyleYlTkbWZ4Q8XvWzeyEdIHsICq9wuRGI5k8czAG52voGNAjuPVs9rp1ZptyxptqHjQLknDKK7KErJ0WcPdBtLuPuWvKkiGdf5w_x_0BUlCEiuicCncqN6u7yVR85hKZ5mncYY109Vzzgt-xTGB58AglLt6GvORkUBCDqD402QpbecXetbZ1UFhbbGnmyVjlEGKu-x2RY_meyVO4ptVg7Jl6Cv6Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d479df485.mp4?token=j_0W1YJKET2cZCZtxiYUF8Kx7HFPp5-5CsfJfexdIsynqbtmEsPSQEGYslFsgFWx_il9Lc8kStR4jcn2Q1NOGlEVACg9omY6DMuWVbaWHAAPKMZ1C2Miiw5lmyleYlTkbWZ4Q8XvWzeyEdIHsICq9wuRGI5k8czAG52voGNAjuPVs9rp1ZptyxptqHjQLknDKK7KErJ0WcPdBtLuPuWvKkiGdf5w_x_0BUlCEiuicCncqN6u7yVR85hKZ5mncYY109Vzzgt-xTGB58AglLt6GvORkUBCDqD402QpbecXetbZ1UFhbbGnmyVjlEGKu-x2RY_meyVO4ptVg7Jl6Cv6Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع عربی: ناوگان پنجم نیروی دریایی ایالات متحده در بحرین، مورد حمله هوایی شدید قرار گرفته است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/672405" target="_blank">📅 06:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672404">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
منابع عربی: ناوگان پنجم نیروی دریایی ایالات متحده در بحرین، مورد حمله هوایی شدید قرار گرفته است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/672404" target="_blank">📅 06:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672403">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
۶ صدای انفجار در بحرین شنیده شد.
🔹
وزیر امور خارجه عراق: مخالف جنگ، گسترش و ادامه آن هستیم
🔹
رسانه رژیم صهیونیستی: اسرائیل تولید بمب‌های هدایت‌شونده را آغاز می‌کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/672403" target="_blank">📅 06:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672402">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
صدای چند انفجار در اردن
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/672402" target="_blank">📅 06:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672401">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
معاون سیاسی، امنیتی و اجتماعی استاندار هرمزگان: جنایت جنگی دیگر آمریکا این بار در جاسک
تأسیسات برق و پمپ‌های آب‌شیرین‌کن اسکله روستای بونجی هدف حملات موشکی قرار گرفت
🔹
بر اثر حمله به این تاسیسات آب شرب چندین روستا در غرب شهرستان جاسک قطع شده است
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/672401" target="_blank">📅 06:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672400">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
منابع عربی: انفجارهایی دوباره، پایگاه‌های نظامی آمریکا در بحرین و کویت را به لرزه درآورد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/672400" target="_blank">📅 05:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672399">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bce0a3dfc.mp4?token=MBZBWHwL06DoeG82MggT6flZPiaaAREXA6dDSzsBEyoUlzvIqb9d8hpygPIsRIX5e624DR8r6aZN5hw_k3ow-kytYwXp9ELEs3Ue1sSaX_Kmie-bU-OmG5VJaUfe9eZ5cKaPHtUOGAN8F89xL2FiBXpN4Du_PTpAm7kJakpnP7NP-sA7gpQxDaVsrD9pI0Q7lc1iAbSmtGaq6RoFEeCpiXJ2ewrjWgnvwPb3mPziNJbJkUpgxAoYiP5lrRNwgcGlVj-NH5hPm263hu3LN1OwzMkOnLfkBClvGlrnkbGEScgC8mrH5Y0roJkW_8QZa_PaEpftATh16orJNbxSQqqSTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bce0a3dfc.mp4?token=MBZBWHwL06DoeG82MggT6flZPiaaAREXA6dDSzsBEyoUlzvIqb9d8hpygPIsRIX5e624DR8r6aZN5hw_k3ow-kytYwXp9ELEs3Ue1sSaX_Kmie-bU-OmG5VJaUfe9eZ5cKaPHtUOGAN8F89xL2FiBXpN4Du_PTpAm7kJakpnP7NP-sA7gpQxDaVsrD9pI0Q7lc1iAbSmtGaq6RoFEeCpiXJ2ewrjWgnvwPb3mPziNJbJkUpgxAoYiP5lrRNwgcGlVj-NH5hPm263hu3LN1OwzMkOnLfkBClvGlrnkbGEScgC8mrH5Y0roJkW_8QZa_PaEpftATh16orJNbxSQqqSTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
♦️
پهپاد ایرانی در آسمان بی دفاع بحرین در جدیدترین موج حملات پیاپی ایران به پایگاه‌های آمریکایی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/672399" target="_blank">📅 05:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672398">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
کویت، بحرین و اردن به دلیل ناتوانی سامانه‌های آمریکایی در برابر ایران، در حال مذاکره برای جایگزینی پیمان‌های دفاعی با پاکستان به جای واشنگتن هستند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/672398" target="_blank">📅 05:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672397">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
حملۀ هوایی دشمن آمریکایی به جزیرۀ هرمز
استانداری هرمزگان:
🔹
در ساعت ۵ بامداد، نقطه‌ای در جزیرۀ هرمز هدف حملۀ دشمن آمریکایی قرار گرفت.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/672397" target="_blank">📅 05:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672396">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
حمله موشکی ایران به پایگاه موفق سلطی در اردن
🔹
این پایگاه میزبان نیروها و هواپیماهای آمریکایی است. پایگاه در حال حاضر در آتش است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/672396" target="_blank">📅 05:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672395">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
انفجارهای شدیدی همچنان در کویت ادامه دارد
🔹
موشک‌های ایرانی به کویت رسیدند و انفجارهایی پایگاه هوایی علی‌السالم را لرزاند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/672395" target="_blank">📅 05:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672394">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMqm17c1RKKjTGcmCnUdgUPuLNM5lznyiG5x5HVoa33UMn4lCXv1sAHiEdVFHiTRTp1_mJuPiL02MpL4aebTvk61PSAtcquC697vDXfIEOdAHvACRtm1dzhiXrnZIRaONUMCHChVWEsQC7bL3Z2Z8MkncGS8UNBcFDCxnXZPi-5SV0jarVOhdaKZyFk0HjZWMQ3jVn-K152E1s3Ct-K_dCn04fB_eIy2qUAvwsKoxdnHBCBRBe47AQd-M1LY8hlAi7WMGL7MOVb9Pw7svClY1z6nxq_6ddGZYSddGpqhn5jCaZ1Igps_qvnxNudUZvvIJGiUab9ufywrNzxuhv29WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله موشکی ایران به پایگاه موفق سلطی در اردن
🔹
این پایگاه میزبان نیروها و هواپیماهای آمریکایی است. پایگاه در حال حاضر در آتش است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/672394" target="_blank">📅 05:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672393">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mD2k5PRF8_LAjFFaTXWb97FCJvTulyLUxJlkZTmKzFaVXX9G1PFqw1k2HZoyvP2nd8QYnaKgRZCb-vC_sDNE5WqbflkWWck6dAC3n480jZvwrye4IZJgcIyg6ym_zJRB52WU79I7OOCA5Txs1QL3a_Bd9F4U4ilQntGq6NJ-DL-9Q3vp2MaPo9vN8-bc9grAojLnBKNc9qXMA_LA-3vlhZ7QtlZiRIXjs16YrMdVK8FWQSK1x3654pAac2WcndoYWLWeio11SyKu-U3LFf_NFdiE5UrnAqQEJCjd67uS8WauTlYsrlQsesmbhUKQUfj1cOFCWhvb-UIjHRc4txaOqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیروهای آمریکایی به دلیل ترس از قرار گرفتن در معرض حملات ایران به تخلیه دارایی های خود از خاورمیانه ادامه می دهند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/672393" target="_blank">📅 05:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672392">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
حوالی ساعت ۵ صدای دو یا سه انفجار در خرم آباد شنیده شد
./ ایرنا
#اخبار_لرستان
در فضای مجازی
👇
@Akhbarlorestan</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/672392" target="_blank">📅 05:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672391">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
سازمان تروریستی سنتکام: هفتمین شب متوالی از حملات علیه ایران را به پایان رساندیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/672391" target="_blank">📅 05:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672390">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aee131af51.mp4?token=kEfpDXgalg6tx978mlvMs3MnzlggPcHrQqWSqNDUB41nykbZYdOvbxBOjoBc3Kx_i0YFIes8icz5SRjIIHoA8G9PuK-tKWNwj143FC3C0bq4cOghHSso0OK2cAi3DEpmOlZBjWvPZy1mCJGkMpKoUTttxLWoTCpgGbcA3zsCQ2XU4H0blkNs2qBMryu28ECVorppCdFy1Fa5f20OVfFU-BtxVmD4kkMFcG-A6K1_dUEJikSfTkKUNTg8blD-R6lUiaZbdqq0_jtEEwgdXYWftftx0jW9RX70UP-uHDDKaiRPWMTFGvx1HMSxLphzxBS99iyGxP4t9hDb8S4rasH6Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aee131af51.mp4?token=kEfpDXgalg6tx978mlvMs3MnzlggPcHrQqWSqNDUB41nykbZYdOvbxBOjoBc3Kx_i0YFIes8icz5SRjIIHoA8G9PuK-tKWNwj143FC3C0bq4cOghHSso0OK2cAi3DEpmOlZBjWvPZy1mCJGkMpKoUTttxLWoTCpgGbcA3zsCQ2XU4H0blkNs2qBMryu28ECVorppCdFy1Fa5f20OVfFU-BtxVmD4kkMFcG-A6K1_dUEJikSfTkKUNTg8blD-R6lUiaZbdqq0_jtEEwgdXYWftftx0jW9RX70UP-uHDDKaiRPWMTFGvx1HMSxLphzxBS99iyGxP4t9hDb8S4rasH6Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شلیک موشک از خاک کویت به سمت ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/672390" target="_blank">📅 05:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672389">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
ارتش کویت از مقابله با حملات پهپادی خبر داد
🔹
همزمان با شنیده شدن صدای انفجارهای شدید در کویت، ارتش این کشور در اطلاعیه‌ای اعلام کرد که در حال مقابله با حملات پهپادی است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/672389" target="_blank">📅 04:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672388">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
منابع عربی از انفجارهای شدیدی و صدای آژیرها در بحرین خبر دادند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/672388" target="_blank">📅 04:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672387">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
سازمان تروریستی پنتاگون اعلام کرد که تعداد تلفات آمریکایی‌ها در جنگ علیه ایران به ۴۲۷ نفر رسیده است/ ایسنا
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/672387" target="_blank">📅 04:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672386">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
حمله نظامی دشمن آمریکایی به حوالی جاسک
🔹
در ساعت ۰۴:۴۴، نقطه‌ای در حوالی جاسک هدف حمله نظامی دشمن آمریکایی قرار گرفت.
🔹
جزئیات این حادثه پس از انجام ارزیابی‌های اولیه و جمع‌بندی اطلاعات، متعاقباً اعلام خواهد شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/672386" target="_blank">📅 04:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672385">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7a40b49b4.mp4?token=Lgihpy2jeKNNI0ndPTjSR8sbs3GMZmnlD4a8wAzLsQarRHL3pzlAE-zaAgyGJxoGhQ_re2rx6glJgB1jOwBVdAjuz1jUOWpLsQ6IV4Wlr3Mem2nxLOy1BE4F_ZeJBACGiMpOAoE1JENbihcXZPPmxNt9WJGpjCOSdiEN7SIDgFTEXicsOduQkDlZhgPdMkO12cXzkqZ1AqAqGu4Yu367Dt76NlY9ZEe2jA-oDpJVJT6pnHpTLtvDgQjkqEBOActdDw87WXLQP6u4drcU76DJwnvqospSmUEYDkftV0gfIir0wyriIXjjppg2Jssi7ydZlFVIaFZraMVVbo-V5ddujg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7a40b49b4.mp4?token=Lgihpy2jeKNNI0ndPTjSR8sbs3GMZmnlD4a8wAzLsQarRHL3pzlAE-zaAgyGJxoGhQ_re2rx6glJgB1jOwBVdAjuz1jUOWpLsQ6IV4Wlr3Mem2nxLOy1BE4F_ZeJBACGiMpOAoE1JENbihcXZPPmxNt9WJGpjCOSdiEN7SIDgFTEXicsOduQkDlZhgPdMkO12cXzkqZ1AqAqGu4Yu367Dt76NlY9ZEe2jA-oDpJVJT6pnHpTLtvDgQjkqEBOActdDw87WXLQP6u4drcU76DJwnvqospSmUEYDkftV0gfIir0wyriIXjjppg2Jssi7ydZlFVIaFZraMVVbo-V5ddujg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله به زیرساخت‌های ایران
روایتی از محل حمله آمریکا به جاده بندرعباس رودان
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/672385" target="_blank">📅 04:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672384">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
اطلاعیه شماره ۲۶/دو فروند کشتی نفتکش با عبور از مسیر مین گذاری شده جنوب تنگه هرمز منفجر و دچار حریق گسترده شدند  سپاه پاسداران:
🔹
ملت قهرمان و بصیر ایران اسلامی؛ حضور شما در صحنه و حماسه آفرینی خیابانی شما، همانگونه که قائد شهید امت فرمودند سوخت موشک‌های…</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/672384" target="_blank">📅 04:34 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672382">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uD37--ZB1To11aYVlq4TxFvwcmKGXz8-TFJhdLffj-lYp34E6QcFTAuP0xtjBr8sR_kjSjwu3k1Qhz3vfZw8UGAAuoKY2i_jVvtSEVPymarmsZjHowR_xazz5fXpaMmbFmYUNv7kEprLE5WJJ0drQ5mkW5T-Pa1DBoAOqBHjs11oP_c7HlnXYHBm1Fyy_w0rXJWRHzwuW5v9xQNlkF9DFtwGLeFiX2JQvaOdDOlu00tSswcY-VShTGxWcpYpcIPejRNSTppNbbsIug_-5_NxXrwlxIrxyKYTadqOtKa4K-QvUaLUZ7wd6vdjRzkihRkbt_D3_kqA0tCehK_S0hq0Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xpc9MFbcIMI8CSk3y5GBQHzscML1MsElwQJva7czT_5kvov44lZ2veh-szQcuXBBg_oFQWWTcoGkEWgaA_3Ni0ewGumqLVQEMCb_F198s0t47lhNJ_ncqISznHJs7STJMX8oKDd40myYvecYYK54v2IECefWGQWnvrnDe7BL070ADByl5H_cl2hBfQkY4GXUuFa-V_CX-kOArExF9vesBJmFnLiojWMQ_nh9_1sjFS1jDY4caUA66TiN9WfRaOL6wDoVDknLvviym5zs6dojsbclyP60jmUJ93POrsyLjqbe3xdPTHqMCB0_qb947aCmGG5gnHmprcT6rKA6WtPnzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
منابع عراقی: شدت آتش‌سوزی مقر گروهک‌های تجزیه‌طلب در سلیمانیه به‌حدی است که آتش‌نشانان کنترل آتش را از دست داده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/672382" target="_blank">📅 04:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672381">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
سازمان تروریستی پنتاگون اعلام کرد که تعداد تلفات آمریکایی‌ها در جنگ علیه ایران به ۴۲۷ نفر رسیده است/ ایسنا
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/672381" target="_blank">📅 04:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672380">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
انسداد محورهای مواصلاتی هرمزگان در پی حملات دشمن
🔹
در پی حملات به زیرساخت‌های جاده‌ای هرمزگان، تونل «شهید میرزایی» (محور بندرعباس-حاجی‌آباد) به طور کامل مسدود شد.
🔹
همچنین پل «شور» و پل محور سه‌راهی میناب به رودان نیز مورد حمله قرار گرفتند. از شهروندان خواسته…</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/672380" target="_blank">📅 04:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672379">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
حمله نظامی دشمن آمریکایی به حوالی بندرعباس
🔹
در ساعت ۰۳:۵۰ نقطه ای در حوالی بندرعباس مورد حمله نظامی دشمن آمریکایی قرار گرفت که گزارش تکمیلی پس از ارزیابی‌های اولیه متعاقبا اعلام خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/672379" target="_blank">📅 04:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672378">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WW0oF2bxZYg10T6cBcLstQulRZkHmzn1UIFHV__HmVrpXdSBPHH1AQnA3pZrawdt-EddpdxP3D_ICai_a_8KhX41oUVFI9YehYJ148fk_vxlVTRX_0dshnqnyi--4KJzjYcqAur8cjL-VfXfIk_2smfVyvF8DzENxcSXPyR0tZGkvoZEZ0I_UNKIF4J7LoPTTHnMfttn-lFtFXrHrE-mho18KlZCod2ihu7V4FgOfcfUIfC8fKqODPSwz8vgpO3dYiiYX9EhgTma_PODLg5E3k3EYUTRkDfrW3hSvQvkdgHOST0mokWbtGkJoU53yjdYGGHMdK9KVp8VIvLtuPa50A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شیرجه سهمگین موشک ایرانی بر روی پایگاه موفق السلطی در اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/672378" target="_blank">📅 04:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672377">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
ارتش کویت: پدافند هوایی کویت در حال حاضر در حال مقابله با حملات پهپادی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/672377" target="_blank">📅 03:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672376">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/192eb09786.mp4?token=TavLgv1CgVJ8gVb9RIQ5ZsU6w-dED6aI8K8qj61iyvy79606tnpXBh6ILR8DUJHgjAOiZwHl1SMpPF_zO5-uDhEuHQplBZ39-2eNVHStmpXjm8TJeKWRqiTJmjQ5aBs4pm3dYgqkQnNhPZ4kj3WjqFFLPqXbr_kBcaTeunObJsCXZ6ZHpzD7HT1c5XIXiuQOcv3B_loT6xQnyfCDenzDV59RUl5TUIlF8asweLcL3GTF0DPbSeQgBOARZtJmt56pP0RIZL5CEQy-_9LkFU_D23C15uJ0r_cqLYPN8PdCjZOyEK5fkLWOdmb3zd8GPl6CgOAVZ3Oe4KjgbI4hMFxjJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/192eb09786.mp4?token=TavLgv1CgVJ8gVb9RIQ5ZsU6w-dED6aI8K8qj61iyvy79606tnpXBh6ILR8DUJHgjAOiZwHl1SMpPF_zO5-uDhEuHQplBZ39-2eNVHStmpXjm8TJeKWRqiTJmjQ5aBs4pm3dYgqkQnNhPZ4kj3WjqFFLPqXbr_kBcaTeunObJsCXZ6ZHpzD7HT1c5XIXiuQOcv3B_loT6xQnyfCDenzDV59RUl5TUIlF8asweLcL3GTF0DPbSeQgBOARZtJmt56pP0RIZL5CEQy-_9LkFU_D23C15uJ0r_cqLYPN8PdCjZOyEK5fkLWOdmb3zd8GPl6CgOAVZ3Oe4KjgbI4hMFxjJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخی منابع خبری: سامانه‌های دفاعی آمریکا و اردن نتوانسته‌اند هیچ یک از موشک‌های شلیک شده به پایگاه موفق السلطی را رهگیری و منهدم کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/672376" target="_blank">📅 03:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672375">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
وقوع چند انفجار در بحرین
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/672375" target="_blank">📅 03:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672374">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
اصابت موشک‌های ایرانی به پایگاه موفق السلطی اردن، محل استقرار ارتش تروریستی آمریکا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/672374" target="_blank">📅 03:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672373">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80c3e5dae0.mp4?token=SI5kb92Zg8NXVauk8Q66uSO5RXY4W6eC3cUDSrnydhpj6TczK1qx_sHuUMz4410hoV8IiqoAEIIvxG00KZdOiFlRDaBmlYqun-4yMkoWC4wrQUkzup7bNRdp9Ju35I9dcNRAKNnlqSh-ig5SEtoxLhTY8Xun4W0ZeLpojUvDKnpNr56BMYUzmuclj6pxFOMkDfXPDEwwHN5qv_Ng9YsbGmH6QMWQhp8I5H2RvC6Ux6XbPSdYTE14E8Br0_EjfTlNX-f4iSOgQRUVkhaC5PappB_iKxOSC0MkRxSwSk5XViXgY0ZCU4wLlL4ZlWM8-y1SRj6iGCDowj3u6pdhA4piPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80c3e5dae0.mp4?token=SI5kb92Zg8NXVauk8Q66uSO5RXY4W6eC3cUDSrnydhpj6TczK1qx_sHuUMz4410hoV8IiqoAEIIvxG00KZdOiFlRDaBmlYqun-4yMkoWC4wrQUkzup7bNRdp9Ju35I9dcNRAKNnlqSh-ig5SEtoxLhTY8Xun4W0ZeLpojUvDKnpNr56BMYUzmuclj6pxFOMkDfXPDEwwHN5qv_Ng9YsbGmH6QMWQhp8I5H2RvC6Ux6XbPSdYTE14E8Br0_EjfTlNX-f4iSOgQRUVkhaC5PappB_iKxOSC0MkRxSwSk5XViXgY0ZCU4wLlL4ZlWM8-y1SRj6iGCDowj3u6pdhA4piPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله پهپادی ارتش به پایگاه‌های آمریکا در کویت و اردن
روابط عمومی ارتش جمهوری اسلامی ایران:
🔹
در مرحله چهاردهم «عملیات صاعقه»، پهپادهای ایرانی انبار مهمات و مراکز پشتیبانی در «اردوگاه العدیری» و پایگاه «علی‌السالم» کویت، و همچنین مخازن سوخت پایگاه «الازرق» اردن را هدف قرار دادند.
🔹
ارتش جمهوری اسلامی ایران با تاکید بر اینکه وارث غیرت و ایثار ملت بزرگ ایران است، هشدار می‌دهد: هر قدرتی که سودای آزمودن اراده ملت ایران را در سر بپروراند، با عزم راسخ و آمادگی نیروهای مسلح  و مردم قهرمان و نستوه این سرزمین کهن روبه‌رو خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/672373" target="_blank">📅 03:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672372">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
جزیره
لارک مورد هدف قرار گرفت
🔹
گزارش‌های محلی از اصابت موشک به دکل مرکز کنترل ترافیک دریایی در جزیره حکایت دارد./ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/672372" target="_blank">📅 03:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672371">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
وقوع چند انفجار در بحرین
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/672371" target="_blank">📅 03:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672370">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8c5a8ae3b.mp4?token=rO_ZU6xJ0U1gtpq41Tk4Sx_zUKd8YqIq4qEBzyIBttHCoBxiwZdDUkgNbnrpGL9-DTUANri3zhrt-ASGqoWq_xESagUj0vVizNZ0rwB2X2X0ke-7yPNoS-C4XZuZSj7yiJUFdQtEP5j046SKwp16Wqc17vpY4cnuzPruhod1tcegXIYR7_WM4RsaDt8oLFYu1MgaWgGFmSqW-ZnDJDwYoiVd5oyA5NlW6SzE0mCXh_dxsJ8FLc91pobhU2RYTaTdju-W8g2XyaoSwlYIbI0dUnT5N_XY-5LSZ6y9QPKiwyQYXaT_amxe_SnsAo6TkCVvl4MOLzOAvvK368WLPaxywn-8mkdftc1K7-DxdbM29MaYE_fRvt8REzE4U8DdipgFMlgxY1hl9WEJ0fusPdNujkLEX7zEg2NpAV2lqlNRYaXIoNYbGx3nHKjd4xhNPIXDNiYRH3cYOteDmWD8CrOUIXWrCHOrUGVsIfYu9V1HCTCAQxqV6FG96OShJyEfBtvVPJBHj7jGEudxuD66-SE2U0xDkMpJ5J_4Ak0S91WiWm5bGq1umdTmLHNHA9pU2S7FpTaOtljsFm2KD3CysGLstHM229SL1q04LAuwZdT75fZ6X31fcJvxmZyATbSjJOaLc98K9IpD_WMIWGzoPoBaifDIfHOVqRTmXymKDSf7ieY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8c5a8ae3b.mp4?token=rO_ZU6xJ0U1gtpq41Tk4Sx_zUKd8YqIq4qEBzyIBttHCoBxiwZdDUkgNbnrpGL9-DTUANri3zhrt-ASGqoWq_xESagUj0vVizNZ0rwB2X2X0ke-7yPNoS-C4XZuZSj7yiJUFdQtEP5j046SKwp16Wqc17vpY4cnuzPruhod1tcegXIYR7_WM4RsaDt8oLFYu1MgaWgGFmSqW-ZnDJDwYoiVd5oyA5NlW6SzE0mCXh_dxsJ8FLc91pobhU2RYTaTdju-W8g2XyaoSwlYIbI0dUnT5N_XY-5LSZ6y9QPKiwyQYXaT_amxe_SnsAo6TkCVvl4MOLzOAvvK368WLPaxywn-8mkdftc1K7-DxdbM29MaYE_fRvt8REzE4U8DdipgFMlgxY1hl9WEJ0fusPdNujkLEX7zEg2NpAV2lqlNRYaXIoNYbGx3nHKjd4xhNPIXDNiYRH3cYOteDmWD8CrOUIXWrCHOrUGVsIfYu9V1HCTCAQxqV6FG96OShJyEfBtvVPJBHj7jGEudxuD66-SE2U0xDkMpJ5J_4Ak0S91WiWm5bGq1umdTmLHNHA9pU2S7FpTaOtljsFm2KD3CysGLstHM229SL1q04LAuwZdT75fZ6X31fcJvxmZyATbSjJOaLc98K9IpD_WMIWGzoPoBaifDIfHOVqRTmXymKDSf7ieY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موشک‌های ایرانی بر فراز پایگاه موفق السلطی اردن محل استقرار ارتش تروریست آمریکا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/672370" target="_blank">📅 03:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672369">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/049b5524e5.mp4?token=jj41LPdDCAr8ZdjxxHux1F18DiDZKjz4bXvbnc9B4nohiPGnlpv61jzJZQTaiyE5B4rhBqhrZifmtkAJREk4bEcCecijy7Ni6GlJKIMDqDlz8dM-0UbpjDTcsZjK_LVtuN5lK9QHQrhVHBzotYxf6P1WMGb73YQlET0X-0qmKUF_dcBiyJmLOM4XEHeFGxwIh3qECCbJ0XmWOmZ8UIAn_drIu6h0aEFIkBOiF69xjqYe5_wBeTv08kFi1drXes2seD1F4j_uaMCpRyVl3cLlnIlIrSghAEgpFulmtPt7h9hRZy449Q2PRrrHT2NW-h9z91W-7GWAcBh29qF0qsQgdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/049b5524e5.mp4?token=jj41LPdDCAr8ZdjxxHux1F18DiDZKjz4bXvbnc9B4nohiPGnlpv61jzJZQTaiyE5B4rhBqhrZifmtkAJREk4bEcCecijy7Ni6GlJKIMDqDlz8dM-0UbpjDTcsZjK_LVtuN5lK9QHQrhVHBzotYxf6P1WMGb73YQlET0X-0qmKUF_dcBiyJmLOM4XEHeFGxwIh3qECCbJ0XmWOmZ8UIAn_drIu6h0aEFIkBOiF69xjqYe5_wBeTv08kFi1drXes2seD1F4j_uaMCpRyVl3cLlnIlIrSghAEgpFulmtPt7h9hRZy449Q2PRrrHT2NW-h9z91W-7GWAcBh29qF0qsQgdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آسمان الزرقاء، اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/672369" target="_blank">📅 03:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672368">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
انفجار در کویت
🔹
منابع عربی از چند انفجار شدید در پی اصابت پرتابه‌هایی از سمت ایران خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/672368" target="_blank">📅 02:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672367">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a67fed2838.mp4?token=Akrs0FTVt7MmRELHbvxLoY1f0N4JAqeuDq5xW8w4jO2cAYuPLCbkLJUCA3rHbJZ8etWAssZRCfVb3Cd1rCfuL1_80Wg5ata0dBNem_8A3KM_E8dw8bTs3kOXfTRdx_qdVhygA2vflF3Ryi4JfWIvjoYbx_ulz6jStj17BD6dPLMzDWwO6YyStMFfiKPjiMYDe2KeHgADO_d9_uyNOCfOlm42llfpkeWcvRKCuEAfJsFhuFjfA2IDi6jcnx1hCuSlY_LwJuBB3k7W6SRNMJLqhJgBQwjCFUPDraPHE72To1uYJt2I4cJVljY2OdBYp2hfRQ-g6HQwK5Q01ouxdjUyQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a67fed2838.mp4?token=Akrs0FTVt7MmRELHbvxLoY1f0N4JAqeuDq5xW8w4jO2cAYuPLCbkLJUCA3rHbJZ8etWAssZRCfVb3Cd1rCfuL1_80Wg5ata0dBNem_8A3KM_E8dw8bTs3kOXfTRdx_qdVhygA2vflF3Ryi4JfWIvjoYbx_ulz6jStj17BD6dPLMzDWwO6YyStMFfiKPjiMYDe2KeHgADO_d9_uyNOCfOlm42llfpkeWcvRKCuEAfJsFhuFjfA2IDi6jcnx1hCuSlY_LwJuBB3k7W6SRNMJLqhJgBQwjCFUPDraPHE72To1uYJt2I4cJVljY2OdBYp2hfRQ-g6HQwK5Q01ouxdjUyQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه‌های عربی: صدای انفجارها در پایگاه‌های آمریکایی اردن به حدی بود که در مناطق اشغالی شنیده شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/672367" target="_blank">📅 02:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672366">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AxFE3iMV16qo3smsgSpliPICwnf3DHgzFaxhpL6aA4lHtvU87XzgkTaV8mbsQbSRQSmCTKO4ZBNVydOSDW87SAf691Zzc96Uz1G45XQ0QWt1_HGd5ikeAKcKjipC6SfZROC7ZaH8hJZE72n5halfOWKlXBVfKev8v5wbkq4P4Xw-zfkYDJeA36NPhG4l4DRy2je2fSHqKCRTP-FAlrDNdNM9_2fH-gMXKEMrWHuzHZNcO5T5iQh8tRevv8CqxmQT1nR9nVWxfOvY4Kgd9kQ5fsrw1sdkoz1_T9fxJisivsmGpMxRqxQ4PqJpyaFy8iU26VxCLCT6K-85h-ZhScxD2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای اکسیوس به نقل از مقام آمریکایی: ایران یک موشک بالستیک به سوی یک پایگاه آمریکایی در عربستان سعودی شلیک کرد
🔹
این نخستین حمله ایران به عربستان است پس از ۴ ماه.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/672366" target="_blank">📅 02:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672365">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
بر اساس گزارش‌ها، آژیرهای هشدار در شهرهای الخرج و ینبع پس از رصد شلیک موشک از ایران به صدا درآمده‌اند/ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/672365" target="_blank">📅 02:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672364">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
رسانه‌های عراقی: صدای انفجار در اردن به گوش می‌رسد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/672364" target="_blank">📅 02:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672363">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
فرماندار بوشهر: لحظاتی قبل یک نقطه اطراف شهر چغادک از توابع این شهرستان مورد اصابت تهاجم دشمن آمریکایی قرار گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/672363" target="_blank">📅 02:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672362">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
انفجار در کویت
🔹
منابع عربی از چند انفجار شدید در پی اصابت پرتابه‌هایی از سمت ایران خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/672362" target="_blank">📅 02:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672361">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
معاون استاندار هرمزگان: در پی حملات دشمن به برخی نقاط استان هرمزگان سه نفر شهید و ۸ نفر مصدوم شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/672361" target="_blank">📅 02:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672360">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
صداهای شنیده شده در لرستان مربوط به شلیک موشک های رزمندگان اسلام است
🔹
مردم عزیزمان نگران نباشند./ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/672360" target="_blank">📅 02:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672359">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‌‌
♦️
منابع عربی: پایگاه‌های نظامی آمریکا در عربستان سعودی، هدف حملۀ موشکی قرار گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/672359" target="_blank">📅 02:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672358">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
فارس: دقایقی پیش اهالی امیدیه خوزستان از شنیده‌شدن صدای انفجار خبر دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/672358" target="_blank">📅 02:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672357">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
رسانه‌های عربی از وقوع چندین انفجار در عربستان سعودی خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/672357" target="_blank">📅 02:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672356">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
رسانه‌های عربی از وقوع چندین انفجار در عربستان سعودی خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/672356" target="_blank">📅 02:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672355">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
ایروانی: آمریکا مسئول کامل تلفات و خسارات حملات علیه ایران است
🔹
سفیر و نماینده دائم ایران در سازمان ملل متحد در نامه‌ای به دبیرکل سازمان ملل و شورای امنیت، آمریکا را مسئول کامل تلفات جانی و خسارات ناشی از حملات اخیر علیه ایران دانست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/672355" target="_blank">📅 02:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672354">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
رسانه‌های عراقی: صدای انفجار در اردن به گوش می‌رسد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/672354" target="_blank">📅 02:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672353">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPuovJgSDNyP5FFRZA9jx1lNplBv69UR8ODmDBRLlr9KzS9n3eFG0J2WEa1fQNq4sziGgMttsbi1RCz8RFYBuzcpzi6-cbEB4tOIDQ4QUM1y_uzQWICXtZLsicn5rLWfWHmfRdi_rWlb0AoocJfm00CFPhpJ1bUsWlf1CwmCxuLeoITqtM-dtEkT0C3XmyHwq1ZtmzSsAetN6uRozwtX7HvBn8OmbZd4YBR0nkHA0U_Ord3d4sk014RDiNplQIyIKeFZWAxLP1e-cxL2iaOJuD_XRyQ4pk_aWmOg7Geyqne-b2eKO2Hy-pGslVUcubkpn86SOQdZNBiBtfXUWB3diQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیروی دریایی سپاه: در ساعات گذشته ۴ کشتی متخلف متوقف شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/672353" target="_blank">📅 02:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672352">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
حمله پهپادی مجدد به اربیل و انفجارها در پایگاه‌های اشغالگران و تروریست‌های تجزیه طلب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/672352" target="_blank">📅 02:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672351">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
تایید مسئولیت آمریکا در کشتار مدرسه میناب
🔹
تحقیقات مشترک «اسکای‌نیوز» و آژانس «معماری قانونی» با استناد به تحلیل‌های فنی، بررسی‌های منبع‌باز و شهادت بازماندگان، مسئولیت مستقیم ارتش آمریکا در حمله به یک مدرسه در شهر میناب را تایید کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/672351" target="_blank">📅 02:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672350">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
سی‌بی‌اس نیوز به نقل از مقامات آمریکایی: در جریان حملات هفته جاری به دو پایگاه در اردن، شماری از نظامیان آمریکایی مجروح شده‌اند/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/672350" target="_blank">📅 02:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672349">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
انسداد محورهای مواصلاتی هرمزگان در پی حملات دشمن
🔹
در پی حملات به زیرساخت‌های جاده‌ای هرمزگان، تونل «شهید میرزایی» (محور بندرعباس-حاجی‌آباد) به طور کامل مسدود شد.
🔹
همچنین پل «شور» و پل محور سه‌راهی میناب به رودان نیز مورد حمله قرار گرفتند. از شهروندان خواسته شده است تا اطلاع ثانوی از ترددهای غیرضروری در این مسیرها خودداری کنند./ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/672349" target="_blank">📅 01:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672348">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
افزایش سطح آماده‌باش سنتکام در پایگاه‌های منطقه
🔹
فرماندهی مرکزی آمریکا (سنتکام) با استناد به ارزیابی‌های اطلاعاتی درباره احتمال حملات تلافی‌جویانه، سطح آماده‌باش نظامی در تمامی پایگاه‌های ایالات متحده در منطقه را افزایش داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/672348" target="_blank">📅 01:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672347">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
حملات دشمن آمریکایی به اهواز، لار، یزد و چند شهر ایران
🔹
ارتش تروریستی آمریکا در ادامه حملات نامشروع امشب به خاک وطن، برای چند بار متعدد مناطقی در شهرهای اهواز، بندرعباس، قشم، لار، داراب و یزد را هدف موشک‌های خود قرار داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/672347" target="_blank">📅 01:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672346">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در قشم؛ مشاهده نور انفجار در بندرعباس
🇮🇷
✊
@AkhbareFori.</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/672346" target="_blank">📅 01:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672345">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
۵ انفجار در حومه یزد؛ آسمان امن گزارش شد
معاون سیاسی و امنیتی استانداری یزد ضمن تأیید شلیک ۵ پرتابه دشمن در خارج از محدوده این شهر:
🔹
این حادثه خسارت جانی در پی نداشته و در حال حاضر با برقراری آرامش، امنیت کامل بر آسمان یزد حاکم است./ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/672345" target="_blank">📅 01:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672344">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
پدافند هوایی آمریکا ۸ مجروح برجای گذاشت  رسانه‌های عراقی:
🔹
در ‌پی اصابت گلوله‌های پدافند هوایی آمریکا به یک زمین بازی در استان سلیمانیه، ۸ نفر مجروح شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/672344" target="_blank">📅 01:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672343">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در قشم؛ مشاهده نور انفجار در بندرعباس
🇮🇷
✊
@AkhbareFori
.</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/672343" target="_blank">📅 01:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672342">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
اطلاعیه شماره ۲۶/دو فروند کشتی نفتکش با عبور از مسیر مین گذاری شده جنوب تنگه هرمز منفجر و دچار حریق گسترده شدند
سپاه پاسداران:
🔹
ملت قهرمان و بصیر ایران اسلامی؛
حضور شما در صحنه و حماسه آفرینی خیابانی شما، همانگونه که قائد شهید امت فرمودند سوخت موشک‌های رزمندگان اسلام و دعای شما تضمین پیروزی‌های درخشان آنهاست.
🔹
ساعتی پیش دو فروند کشتی نفتکش که با فریب سازمان‌های جاسوسی آمریکا قصد عبور از مسیر مین گذاری شده جنوب تنگه هرمز را داشتند، منفجر شده دچار حریق گسترده شدند.
🔹
نیروی دریایی سپاه با قاطعیت اعلام می‌دارد تنگه هرمز به خاطر شرارت‌های ارتش کودککش آمریکا به شدت ناامن و به طور کامل بسته است و تا زمانی که تجاوزات آمریکای جنایتکار پایان نیابد، امکان صدور کود شیمیایی و حتی یک قطره نفت و گاز از این منطقه وجود ندارد.
🔹
شناورها برای حفظ سرمایه و مهمتر از آن جان خود فریب نخورند و وارد مسیر مین‌گذاری شده نشوند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/672342" target="_blank">📅 01:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672341">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
صدای انفجار و پرواز هواگرد در بندرعباس
🔹
صدای چندین انفجار و پرواز هواگرد در بندرعباس و اطراف آن گزارش شده است.
🔹
خبرنگار مهر شنیده شدن ۲ انفجار را تایید می کند./ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/672341" target="_blank">📅 01:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672340">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4cca69fa3.mp4?token=OOqHvmNe2o8myaQJO1DWBRkFvacbnv6M2krZEAlhduI7f__h0tz0WINBqNSkqXyBXVxOsLX4LIlxEZEM4dBiWJbVobbG-evBoi-Dt-FHBIkA2s8R35ShMqliu_nFVgp4n3y7VxUXctVQyVt78GlqZe-UoJGc-QyZwaxVlYV-lV2WEB-TBg1CumyOtAQiDjT1PbPajSxXqUhcmsnxnzTdelvmOutJQWjyFHknN0d56rhVABpGsqbXE3IaXfwgHlsq3pC-CYT2ehhUTwKETWKSnr212MI7JsEos_S3yOW1vwCvR_Zn3ezx4ACvTSnsbzlXh--tpAB_sCZIxIUwCY2NYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4cca69fa3.mp4?token=OOqHvmNe2o8myaQJO1DWBRkFvacbnv6M2krZEAlhduI7f__h0tz0WINBqNSkqXyBXVxOsLX4LIlxEZEM4dBiWJbVobbG-evBoi-Dt-FHBIkA2s8R35ShMqliu_nFVgp4n3y7VxUXctVQyVt78GlqZe-UoJGc-QyZwaxVlYV-lV2WEB-TBg1CumyOtAQiDjT1PbPajSxXqUhcmsnxnzTdelvmOutJQWjyFHknN0d56rhVABpGsqbXE3IaXfwgHlsq3pC-CYT2ehhUTwKETWKSnr212MI7JsEos_S3yOW1vwCvR_Zn3ezx4ACvTSnsbzlXh--tpAB_sCZIxIUwCY2NYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اینفانتینو: فدراسیون بین‌المللی فوتبال (فیفا) منبع اصلی شادی برای بشریت است/ ترامپ: مگر اینکه تیم شما شکست بخورد!
رئیس فدراسیون جهانی فوتبال:
🔹
شما نیازی به افرادی ندارید که شما را تحسین کنند، اما این جام جهانی بدون شما، به این میزان موفقیت چشمگیر را به دست نمی‌آورد.
🔹
جام جهانی ۲۰۲۶ بزرگترین رویداد اجتماعی و فرهنگی انسانی است که بشر تا به حال شاهد آن بوده است. از شما سپاسگزارم، آقای ترامپ.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/672340" target="_blank">📅 01:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672339">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‌
♦️
منابع عراقی: دو انفجار مجدد پایگاه آمریکایی در اربیل، شمال عراق را لرزاند
🔹
پدافند هوایی آمریکا در تلاش است تا با پهپادها در آسمان اربیل مقابله کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/672339" target="_blank">📅 01:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672338">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
صدای انفجار در حاشیه جنوبی لار
🔹
منابع محلی اعلام کردند که لحظاتی پیش صدای یک برخورد در حاشیه جنوبی این شهر شنیده شده است./مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/672338" target="_blank">📅 01:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672337">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
انهدام یک فروند پهپاد MQ9 در آسمان بوشهر
🔹
لحظاتی قبل یک فروند پهپاد MQ9 با آتش سامانۀ نوین پدافند پیشرفتۀ نیروی دریایی سپاه در آسمان بوشهر رهگیری و منهدم شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/672337" target="_blank">📅 01:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672336">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‌
♦️
منابع عراقی: دو انفجار مجدد پایگاه آمریکایی در اربیل، شمال عراق را لرزاند
🔹
پدافند هوایی آمریکا در تلاش است تا با پهپادها در آسمان اربیل مقابله کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/672336" target="_blank">📅 01:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672335">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
معاون استاندار اصفهان: هرگونه فعالیت پدافندی در شهرستان نجف‌آباد تکذیب می شود
/ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/akhbarefori/672335" target="_blank">📅 00:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672334">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
وقوع هرگونه برخورد یا انفجار در لار استان فارس تکذیب شد/ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/akhbarefori/672334" target="_blank">📅 00:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672333">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
حملۀ موشکی به نقاطی از اطراف شهر اهواز توسط دشمن آمریکایی
معاون استانداری خوزستان:
🔹
دقایقی پیش نقاطی در اطراف شهر اهواز توسط دشمن تروریستی آمریکا مورد حملۀ موشکی قرار گرفت.
🔹
اخبار تکمیلی متعاقبا اعلام می‌گردد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/akhbarefori/672333" target="_blank">📅 00:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672332">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e35cd90c5.mp4?token=cb18mW1vY-EX_ZeBZLZ3JyTRRwIzJ2gIGBFct2O5k7ac8jkEHkT3vaDusObSe7GwhRWN9JdvLMb13oAy0yXWaGi8uFjhzbgsx2-6w2uzjFjnwA0AFbuiXILo9fxcv6YhuMlSAGXd0BTxUEPHK-3FN5oa9ZIdBzT4HYkb3Ukgc5W90mArKdgDgtw-rNxAnITHsfNHsmnbIoiu6YBV-palnInB8TCNppe-gy-5Xnx_e8MWmBXBqm3cobwkeZ1rHWnc3bVx-8DfLS0aFspXy2c_y7rmTpXtWDfnc8UG4li1NLLBXF-1yx15pjkQtbHUu0SUuV3bInYMaCdpWE-sfp_M7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e35cd90c5.mp4?token=cb18mW1vY-EX_ZeBZLZ3JyTRRwIzJ2gIGBFct2O5k7ac8jkEHkT3vaDusObSe7GwhRWN9JdvLMb13oAy0yXWaGi8uFjhzbgsx2-6w2uzjFjnwA0AFbuiXILo9fxcv6YhuMlSAGXd0BTxUEPHK-3FN5oa9ZIdBzT4HYkb3Ukgc5W90mArKdgDgtw-rNxAnITHsfNHsmnbIoiu6YBV-palnInB8TCNppe-gy-5Xnx_e8MWmBXBqm3cobwkeZ1rHWnc3bVx-8DfLS0aFspXy2c_y7rmTpXtWDfnc8UG4li1NLLBXF-1yx15pjkQtbHUu0SUuV3bInYMaCdpWE-sfp_M7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع محلی در سلیمانیه عراق می‌گویند شدت انفجارهای امشب به حدی است که برخی گمان کرده‌اند زلزله رخ داده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/akhbarefori/672332" target="_blank">📅 00:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672331">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
هم‌اکنون شنیده شدن صدای ۵ انفجار در یزد/ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/akhbarefori/672331" target="_blank">📅 00:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672330">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
وقوع هرگونه برخورد یا انفجار در لار استان فارس
تکذیب شد
/ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/akhbarefori/672330" target="_blank">📅 00:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672329">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
استانداری هرمزگان: تا این لحظه اصابتی به بندرعباس گزارش نشده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/akhbarefori/672329" target="_blank">📅 00:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672328">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nqzv-Msvh4eoiuDd2zPR5cI--CPtUlPQlomtWOqb_QLQDGUUnH3o7VPFAxC2H1cA92EH-M-JgFOX7157xolUafTZsXPixzRRhO4wNQgvRhTupYfOknjuUFYlbtqNm-56eodgtc0phaXI5xONmFvvOD_sRRoDP4AJqR2v5h68M_fjhdtlQo52XV4GOhRE97BYGdG1WnU5-adN4lzbyQZdvUMH1pOdVEXJ_7vA4HoWPBtvoBAPR96sieoMgtfSCxF9xKiO9fbHM2kesJ3djPuv4zu29TKf3T2iaNukGFqUP_c1OgyYOCgRO_kS4S-J7NGWfOhqAzg3qcZVh_YyirP7cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: ملت ایران امروز بیش از هر زمانی متحد و مصمم است که قاطعانه دشمنان وحشی را از تجاوز نظامی جنایتکارانه علیه میهن عزیزمان، پشیمان کند
🔹
آمریکا می‌خواهد با حمله به زیرساخت‌های غیرنظامی و کشتار بی‌گناهان، به اصطلاح «قدرت» خود را به رخ بکشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/akhbarefori/672328" target="_blank">📅 00:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672327">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
فرماندار بوشهر: تاکنون هیچ گزارشی از اصابت در بوشهر دریافت نشده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/672327" target="_blank">📅 00:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672326">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
داستان جنایت آمریکا؛ از ۶۶ کودک شهید پرواز مسافربری تا ۱۶۸ کودک شهید میناب
گزارش متفاوت اژدهایی، خبرنگار صداوسیما در بیمارستان بندرعباس:
🔹
من روزی با موی سیاه بر لب ساحل ایستادم و پیکر ۶۶ کودک شهید پرواز ۶۵۵ مسافربری را دیدم، حالا با موهای سفید دوباره روایتگر جنایت آمریکا هستم.
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/672326" target="_blank">📅 00:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672325">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bff2416c74.mp4?token=vUR7t7fJDCUV7GY5USQrT-vlyFmgQdx9hhD8fPGi3GYiQjuYfAJbHH5WzdjUeOt09-6VB1UxVytgoPm_z-_5tNA0Ne1x6DJCx72B4SR6f07g48AqX0SXd5pi25ahh4qOaZF2ATLhSzCPqwB5mZ42--DaE7QXsdSUbzlpLHq6TwTvodlYCGbWi9pFVkQ3aRDwevWV0stvfLi9IVPvuVofWNWVfr0ckcUsyMOWcseb5YlKkvbxBXmqswqV-aaeDhp1c6g5E6rZNe0bEJH04CimY9Xl3UFrQQHu45RleIaf817AUMjhJlrruIEY7GFFW9kVEHqGMjshQb6ux8_HTPglJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bff2416c74.mp4?token=vUR7t7fJDCUV7GY5USQrT-vlyFmgQdx9hhD8fPGi3GYiQjuYfAJbHH5WzdjUeOt09-6VB1UxVytgoPm_z-_5tNA0Ne1x6DJCx72B4SR6f07g48AqX0SXd5pi25ahh4qOaZF2ATLhSzCPqwB5mZ42--DaE7QXsdSUbzlpLHq6TwTvodlYCGbWi9pFVkQ3aRDwevWV0stvfLi9IVPvuVofWNWVfr0ckcUsyMOWcseb5YlKkvbxBXmqswqV-aaeDhp1c6g5E6rZNe0bEJH04CimY9Xl3UFrQQHu45RleIaf817AUMjhJlrruIEY7GFFW9kVEHqGMjshQb6ux8_HTPglJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع محلی در سلیمانیه عراق می‌گویند شدت انفجارهای امشب به حدی است که برخی گمان کرده‌اند زلزله رخ داده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/akhbarefori/672325" target="_blank">📅 00:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672324">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
گزارش شنیده شدن صدای ۴ انفجار در سیریک
🔹
خبر اولیه از شهرستان سیریک در استان هرمزگان حاکی از شنیده شدن صدای چهار انفجار متوالی است.
🔹
جزئیات بیشتر در خصوص علت و منبع این صداها هنوز در دست بررسی است و اخبار تکمیلی متعاقبا اعلام خواهد شد/ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/akhbarefori/672324" target="_blank">📅 00:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672323">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJVWI9C3TMaqJU4MaFk9qCldUc3imu_ee-dPEgzrhncaKKVAdvRH20QKKt6yMjgIAFDlY_nxjVETFLnkpXj41edFaaPDvv9ktjLegbS1_5jyhiuR676cF8rldBxyU5J02zis9nH86ZCgyCb98JRWBB6b4jE6GipbrbtW1R6vocQDvotwu3TWuk-kr18lM_NaKkr0kvrWGq2yNv5HSK9n7QvYFpnfToqzipzmmtJOh4A5r4mU1GtObDsWspV0Ois9jMotJJwEBuGXyd5Cz_y8-QhNT3oG3EPN2ErH2V1XA4MB_aP_tcwlBMQlpgdi4P6OXg_Rdi4eMVj_YxWyB9Z7nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
📈
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/akhbarefori/672323" target="_blank">📅 00:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672322">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
لغو تمامی پروازها در فرودگاه اربیل
🔹
در پی حملات پهپادی به مقر ارتش تروریستی آمریکا در پایگاه حریر واقع در مجاورت فرودگاه اربیل،  تمامی پروازهای این فرودگاه لغو شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/672322" target="_blank">📅 00:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672321">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
اطلاعیه شماره ۲۵/
دپوی شهپادهای آمریکایی (شناورهای بدون سرنشین) در بحرین در هم کوبیده شد
🔹
مرکز اصلی هوش مصنوعی بحرین که در هدف‌یابی دشمن مورد استفاده شیطان بزرگ قرار می‌گرفت با چندین موشک بالستیک و بیش از ده‌ها فروند پهپاد به طور کامل تخریب شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/akhbarefori/672321" target="_blank">📅 00:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672319">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
سخنگوی دولت: دولت چهاردهم تا پای جان کنار مردم ایستاده است
فاطمه مهاجرانی:
🔹
در نشست روز چهارشنبه هیات دولت مقرر شد با توجه به حملات دشمن، به‌ویژه در استان خوزستان، برنامه‌ریزی لازم برای حضور در این استان انجام شود.
🔹
مردم جنوب، جان ایران هستند. همه مردم ایران قدردان رنج‌ها، ایستادگی، صبوری و فداکاری‌های شما هستند و به لطف خدا، با همدلی و همراهی، از این شرایط و گردنه دشوار نیز عبور خواهیم کرد.
🔹
این دولت تا پای جان پای کار مردم ایستاده است و اجازه نخواهد داد خللی در ارائه خدمات به مردم ایجاد شود./ ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/akhbarefori/672319" target="_blank">📅 00:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672318">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
وزارت دفاع کویت: چند مرکز و پادگان متعلق به ارتش کویت هدف حملات پهپادی قرار گرفته‌ است
🔹
در این حملات تعدادی از نظامیان مجروح شده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/akhbarefori/672318" target="_blank">📅 00:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672317">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvG6H2KmICNpbskwf7CPvRh4fmK5ijii5AJOBJmiH_LSB4P5PGZFzef9Z3rJLbIVKfBtWXgJPeUEQtn3Ky7kepTQMEvjje_AUEpfmJWkexxZsQRg_ZfXym6uV-E5VqXLH7WCbiaj68fxisHlMkY4FFsiROzS88MBxAGnpswnoZ1SAyenRjQZBYofOpmKEUgh9QzJBgJS01vO2iZppUutNRzuWk-7Yjj-d9jVT0DOW7twJIs73Me1wXnaBgIv9BYmJFXBC2kftwq2SbQRdGBJS7kxjAeU_szB539FxG-yo5EFpJ-X8FpktI-HFGngRIcQB7XAKb9NXE6sSKyL1DHbkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/672317" target="_blank">📅 00:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672316">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
استانداری هرمزگان: فردا شنبه ادارات و بانک‌های استان با حضور ۵۰ درصدی کارکنان فعالیت خواهند کرد
🇮🇷
✊
@AkhbareFor</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/672316" target="_blank">📅 23:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672315">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
صدای ۳ انفجار در بخش بمانی سیریک شنیده شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/akhbarefori/672315" target="_blank">📅 23:50 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
