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
<img src="https://cdn4.telesco.pe/file/ErUBJj5DlLH96z_Io5gwWDsCCGkTI53ukcG3jGjPTKIc3PtQs8I78vxK06ry5ouzOf4Hn__jtiKFh44FkSTmrmYiLKEpME1X98sIjCVJjKgvVsDC340fdfvapDWp7iPAylyyf-LIt9UdbVnvPAC7AJDFe-l4AYLEJ_pX9o17LsuJa66i4WmLf8zBVjD3ue_x-5Z9Qe9K_Btj8w9XGrKs7elecr9n4rpdCIzUCZDcnAOWllDz3oEk0cqFvBB5MHkn1Tdke76luZDERr2wHGS4DvS-fWD3vCSl0IdppVQ0n58ZxJhskHQwE7pGj6GHqEpq55duDPCwv4_ofeV-lDTCSQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.48M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-19 21:42:35</div>
<hr>

<div class="tg-post" id="msg-697578">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O8aoxTygta2TMKib_czugoEEADE5BWAEL-jHHUH1bUhUMce86RdlGG0g4NOdYcoWQqoziPR_A3ub2qxZgr_VD9pY5lrouSnpQn6Rj9Gw5rdYjR6UwUBS_wruOJRYozyVOEeSlquMPpBGxCwd7_UZoVjVVGWImDmQAUmWavi4rPWVZPLHU4OzTurCkrKmYzHdKLyliU1QD1UfYhDf_fyIowcs_C1n0in8meD0l9dJpd8I8EVaqNEN2hdJHXuYFvJEn3k-ePCNPQur-7pTjX0WtApxl-f4HBAjaWxHPvfJyEvkMpGUfF2Wz2yd0RwVJzxb8XqY5Lk9IYt2apFdMXBjXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NVNYbaci962S_Mk_4HCJvonp8Br0wbgpKhVnQeRWzrDb3TYhRuJK_CR5fUoca9ylRA5BgQSxa1ATKeSr5AWqPdJcNW3aALh5GdKW1G4EMcnxLrwKngeEo0gHwWEAgSyeKDlieo6jnGbl0tUOAWBT_WpcV-Ar0fQ6xNzhXXJEdL_SPvr0KMk8Ft5fGqocmCZkOXh3v5KW2ervMXndSUI1vIAh2rxlSM5My1Td4_NWgT1XS7m-fOfIpQLOqc1_eB2ZMwm60QMLhRQv0cBYmYm2TTpM5jSdNolBzNdeeswqcVWuSvbw23k4HxkulTCw0XTcma3UHIxX-ucYjO9-2GbOHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HqAIP8lEx-aIQlzZMynwDCyQ_BQY9iixHFz_PmRFIdsQSodcDdZI3-2Keye9xCMhYh-upDUH1VFwajhvym32PxMKNUpvOnzxw_IrrBdB2bq685Um3GL9_m3qrFMIq4edaP5UxGVmVEgShvHQiIie0HKrkopGZFJnI7gAxwpajIsSqZnkl_zWrmyrF7P5h9ZWKfasOyI8NT0m-AgCgqrX-rbRf1Q36WNnfq2Cu3GN7XVEu_6F_k7E8CP8KcnL7YUn9-T7Mz7vyZf4V6sYNu4weve5_PBil8LJCBbyyrxh4iQCR-GI2Y5YhkROjMdxi7WFuyP3r5FzxFYpv4E9ghskGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EhQ63qjWSOcts8Ddt6v9Od3tVMVbxCuZu2lqw5CTv9w9jL1ZXkvDNpUxpWPEpWLeIu0Ihihj8BdgXoIFNmnWF562UQ-f2IH6ydXdYnleLIIXB4Zv8Lbkd2W6ZUuUZ-Vo6bcIlyRvTRpKcFYwyYDp9UFfu9m7GwkoR8S5eoTGxDNSPvHtsFzZsomTodE9X3WetctBkXH9xtD8FD8j15lnScgHHr6YBxyHRKv5luTQDEu3i3dohCwEGi4Ebd0FF0_2QuBmU0iGC5mXhj6ASqvXqE-WlLbAab1zXvmHpaehSoTJ7K_NOzTBr826KnjYBLOINw8fcqD0mfFYanm0FmARSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hDUE941fI43_qrwWek6zcMu4edBR5FZcfvhDsT8y_08BUWtdai5u1-mMy2g5Hy8-VOfQHOjz87TUSvXiEtmX56vFGEwHCE-dVw8czl9jPLRjql7Oi0VXYyVKuFB-Dy3Jp_VPavdXWCfn5k-qC33kNSzKKimeGUb--s2lP2AW8j655SjAOnJF4ZTjtBRHB54Zk42pxoLhbFUsbKvbKz9YO7xEZ60vQi1Uj54eCo8OA8ZLI3heO-8VoY88JJDEXA8YzwiXEtKuaEfZqrdOl0EN-h_d54g-bmYhUm6U5tcdqG6rDybAlX63uhpzteYc3IlA22VNpZ6kQZfd1LAgrqvtQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cBN2ko2JJW064JgN1kMkp1Dy7QL46oh9QpzLa58VPlBNWmYi7I-1khmr4ZIYOA84DF7if1C6qPM8JGt9Sl8ilMTwL4pNh_qty1EcUwWX73YdbhGk6oX9npAlg3IYfSU_u3SYhGTkhR8To1kz0naNk8gibDn4e1NdK9Y4Ik1gs49owux15m6jJR3FZDgKA7SP3jLwJdRqNHjowSU1ZCt0IHLGY7ZBaPf_J6jhGThRDXzU9Bo4ugwBAJnk56DWELbuQ0cqE6dCFexd_WTdkLiNm0BHfsBpUqM2OGzDD1Cv1dkXi8jAbbCICYRyN6MS6FbUOpzgl-s9L5RpNtrVaupwZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/splocHU6fGrgU5p8i8LvskWLLcjFbKUvm98wtIzXyyM_OToRNSBZGPr-1vtgSQUuXBDqZBqo6H88qZW0U6-FsZkxlqupkCnvw6MMNu6R4-CFfZ7emQEsZQYu63J4CDQN08_ZN1Nicul9PP4pVUiqARQuQnVwjwh1TIzaRZFA5hXDCHTWEJxC9KtuxkEZERlF0_7zCN-AiDkVdkoBRZFHofCl-zeBq3VI4rQK-T0F8snOCGap1fSwOF74KEd-nanNJf5hhaBU8UGwL_ywEiX7X5rMfizHW0G7aj0Z3oo3cv99RGm1AFtwNvjlN8ClWApuCm4-ti5ezcti-rkKpa7Ohw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I9zQpokKO6w_pcrqs-xSzuqlBmpaIsnPp03EWGw3Yn9fH6fFpAsRKvSHSugh5AH0B11wING3kAJPvaqFDgbMq4oFma6QFRTIf5cAMGTYQQtDFkNIR3MYz47fg7QzPnEqpl38feO4wmX3jcL4r6ZONG5rzDuTgXSFRMJfbtCqJjkA6LJA1u--MGjq7f7AjUtf9f89CN-qLhOAIdxlEWE948AX93gAwrCYV1gph93s2vIbUjaWxr74k8jaA-wgnZz3sTbb8yzeYpUJXV1yzPbIT28CVBMFk7MpMKbNwgudG6iK135LsPabd5rs-kcTIlVx4zsK_tXjJZf3FQKIhfHaVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
با چندتا کد ساده می‌تونی ادیت‌هایی روی عکست انجام بدی که معمولاً کلی زمان می‌برن؛ از تغییر نور و رنگ گرفته تا ساخت استایل‌های متفاوت با AI
🔥
#هوش_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/697578" target="_blank">📅 21:42 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697577">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/967a5a7390.mp4?token=VKG4GnsPH1q19ZNkVLubUz3KCMhHGdy425yzRAQ6H_a8rYNQzlBxuMoKcBvAeo6tgo0TrOjR7jyOff7vgSKnq3j3HluPM9LSRNMp1k0NfRcZAIMpC20_d3UpHcPkXT6fXSaxK0CwT_NdhZfDwIH9AOjWO59kQYLdd44o_9yCyapD2Wr8fctb4GTy6uC0chH5x_xSSaTrw4NyhZsxRBWeMikxfsuoyPcjLpe0QMhCWmQSlbpIuTJzEVe2m5kHFhQ2rg8vjmj26Wyy7xIpGlBI7IDs4BW4J1Ex15vqeO5spX2YU-nBTgnMj6LX4ckkbedYsGR9qV7hr_gSZSg8b8j_dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/967a5a7390.mp4?token=VKG4GnsPH1q19ZNkVLubUz3KCMhHGdy425yzRAQ6H_a8rYNQzlBxuMoKcBvAeo6tgo0TrOjR7jyOff7vgSKnq3j3HluPM9LSRNMp1k0NfRcZAIMpC20_d3UpHcPkXT6fXSaxK0CwT_NdhZfDwIH9AOjWO59kQYLdd44o_9yCyapD2Wr8fctb4GTy6uC0chH5x_xSSaTrw4NyhZsxRBWeMikxfsuoyPcjLpe0QMhCWmQSlbpIuTJzEVe2m5kHFhQ2rg8vjmj26Wyy7xIpGlBI7IDs4BW4J1Ex15vqeO5spX2YU-nBTgnMj6LX4ckkbedYsGR9qV7hr_gSZSg8b8j_dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعضی همکاری‌ها با یک جلسه شروع نمی‌شوند؛ با یک گفت‌وگوی متفاوت شروع می‌شوند.
در گراد، ما به فرصت‌هایی فکر می‌کنیم که هنوز شکل نگرفته‌اند؛ به ایده‌هایی که می‌توانند به همکاری تبدیل شوند و به ارتباط‌هایی که شاید مسیر تازه‌ای برای کسب‌وکار بسازند.
این بار در شیراز، نه فقط برای معرفی یک برند، بلکه برای شنیدن ایده‌ها، شناختن ظرفیت‌های تازه و پیدا کردن نقطه‌های مشترک کنار هم هستیم.
اگر شما هم به امکان‌های تازه فکر می‌کنید، شاید این دیدار آغاز یک مسیر مشترک باشد.
گراد در Shiraz Expo 2026
|
📍
سالن حافظ | غرفه‌های ۴۳ و ۴۴ |
| ------------ | ---------------- |
GERAD | G NEXT
www.Gerad.ir</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/akhbarefori/697577" target="_blank">📅 21:37 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697576">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
ادعای وزیر خزانه‌داری آمریکا: به احتمال زیاد، اقتصاد ایران در دو هفته آینده فرو خواهد پاشید
🔹
انزوای اقتصادی ایران به صورت مرحله‌ای اجرا می‌شود و ارزهای دیجیتال، هوانوردی و حمل‌ونقل دریایی را در بر می‌گیرد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/akhbarefori/697576" target="_blank">📅 21:35 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697575">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
ادعای ترامپ : از همین لحظه، در جنگ میان روسیه و اوکراین آتش‌بس در حوزه انرژی برقرار می‌شود؛ هر ۲ طرف توافق کرده‌اند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/akhbarefori/697575" target="_blank">📅 21:32 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697574">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
محققان: هوش مصنوعی و جنگ هسته‌ای می‌توانند تا سال ۲۱۰۰ بشر را منقرض کنند
🔹
کمیته‌ای از دانشمندان نشریه علمی «لنست» ۱۷ تهدید عمده برای سلامت انسان را شناسایی کرده است؛ از جمله جنگ هسته‌ای، استفاده مخرب از هوش مصنوعی، تغییرات اقلیمی، آلودگی هوا، سوءتغذیه کودکان و کاهش کمک‌های بین‌المللی.
🔹
کارشناسان تأکید کردند این تهدیدها به یکدیگر مرتبط‌اند و مقابله با آن‌ها به اقدامات هماهنگ نیاز دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/akhbarefori/697574" target="_blank">📅 21:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697572">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
ادعای ترامپ : از همین لحظه، در جنگ میان روسیه و اوکراین آتش‌بس در حوزه انرژی برقرار می‌شود؛ هر ۲ طرف توافق کرده‌اند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/akhbarefori/697572" target="_blank">📅 21:20 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697571">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nuFbTtKopCj0_XqNonGmlBPb6xZxOC0f2QShPj8o6TAziXDmcwDxMkSsR13l3-zc7xDLbcDV5CCl6BSypM6NgCseQJZq9mGeZ2E9Kh1fZd6YbpVWz6B3H4dMmXAb2KqINEC58W1jo3PJohVMxw2mopDKqLkXgq6xM3crTP1ZQCO2RE5_k_QpfWsSFKsyMG4t-6OQEtfVaEYnzzQBwD1751RU3wALNLBVtITO5JBm_3ryy5X9xoQnS_v95eosBzOCfbDX3cuqI4WRxHyIEiJ6XbivX1DX4HMHZMTIjwr3e6PjmvMiglSvA8cD9BK0CmEDD0-GoeNjXPeYtC4uRuFalQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از دنده اتومات چطوری استفاده کنیم؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/akhbarefori/697571" target="_blank">📅 21:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697565">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jOKP_BwCRncO6z4_TAqKZoY5a2qWRN68UXyHehJYmem8lX48mrfML4Eo5x7nV63uLFHtvGFgA1RT6aTrt3_4set4IYoqE9Jpg7jEaD3e_CIPRMBA8NOTVk_oR1RnuUdUV2zIEyrjLUmsXIWzXL6w7yedQnDF3KpWw4gtbF8Ge6IdtJpN1HckprfA0GWiHRAl8KCq_vyEmkFkCBq8PoRJEwhK78673VN2VDH2kvohdENq86T-sEu3dUyN3_4dwXvp0OZXgrhixt5Lq_14jpotLdQWHmzIfTtkpFcANV5vLCzsRWSayrerJuoOTKbP3KSX0m6si9PVs2VZdsMdtgpfWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TsICzV7j5ewKDrX64FgZT5pul1vwMmuIHdG3Rn3U6fUPQ7UFeW9idcyZ5TPxkrmSljKvRvsLtrDjLOCU3AHyrKHc4Kk9dqq8ZGaMchNCz3iBFiNoZs1Umevb04FxSAywBVRB28Po9AbVLU-jMw-TrqChOWEjqKcKcnZK9x3WSHTg25Hra3PW7QikFusyd5ZUt9icbpD7aCw76LV5CPV3vohyAegd_k67hGAEWzKOgTmDHeAx20wwCoU5dJFAQZpua30z5b1N6t1bN2XEFXIIIGooJVpHb-45JoCRUBJGxqny8NCtrgH4teipl0d8TtUVid3ylFkPsnLe4FXzWz9ZYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UV44nkwG6entJLXsyvikRzbgiDyqxH-XOPt0lTIOqZzbyKT77SM50UC7XFsn24LWFZ4F3TgRUq2oTIw8cXJ0RyLyeR3_MvYghhvcpNLR-_SSEvoMTOIJOw8wKWpNG81vELWgYFuSIi-g9KPoO2M7q8Oo0giiqXopckxJ3hq4IlP_oCeyPdQREY5xFD99lWqGCquhMR5zARoGRIKjKhFxxk2TimOgxaez8ueOUx8T25cv8n-r05Fuj9c-4RoA5qC-Kz02Idi9COeN7e-W-l2mYQtUw6BsrRiJzBO_XLDjBCB9NX7aa7ztksYinkEhtAfLJDTYmnShCZ-PUVK1oyGSJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G2e4wWjTgGXwDNgQGrSeuy0LFiyv_R_OSudFGu7bJqudN4etkimLJ-9n5r2Rd8pw_VUTQXPWqeV4YLYYt-pHQ7qSkLxfkoYEElE34YpgkBkzXs40MPccjKhGSSZ1YiB81WhdBYhGoyhg8o38npG-dxrXlBdtnSrxW89E9dU_nggbQZHFFvSRMBm5tPvmwq0Qy632d0PJdTVyHMTBWKEyHGFG-L58zTPg8nTTWOqXpQcSHRVZZfGWx2PJfodGBQn4kBbgclwrUP867yfckR6XI1CSZLtpLoO_aS4nYb-X-McyHZVvqaZHuXHqHvsiz6htUdGK_8p6tjRn_BKOtOwW6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QB1PC9tFRiJWOYuM1XK-j7-libUmeyQlENf1VcN7ueBUMEyteEv_oghTpd2A6pBaHTSLJI8N5O2sapCRLH2vBDmPzgJW1DT7IfkN5ES1ItEmk0StvrZ0eM2zAdoVAp-sqCqhcChiQUMwgbrSbIcHZlpEKdEObpM13uVR2Li4hstNSxz7hTvXjp-mvw3ZPf9ht32SURQyIl1sbpGggqz2Df3Vs4uZsLeC4xoCWxRrUFj8vzXjkDTLTxGdfUFvQDs3zlEVlf9v-dkqFVZtMEvF8ipGFo-bIPUE62oXJH3dNI5okaUWaAQCv-AxuXo4yqs82q--jCIntHiVL6PuUodrfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
"پیام محسن رضایی و قالیباف خطاب به وزیر خارجه آمریکا" روی بیلبورد‌های شهری
در مقابل ایران زانو خواهید زد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/697565" target="_blank">📅 21:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697564">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
مرشایمر: به نفع امارات و عربستان است روابط خصمانه ای با ایران نداشته باشند، امریکا دیگر نمیتواند از انها دفاع کند
نظریه‌پرداز علوم سیاسی:
🔹
از این به بعد هیچ کشوری در خلیج فارس جرات اقدام علیه ایران را ندارد؛ ایران خیلی قدرتمندتر از همه انها خودش را نشان داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/697564" target="_blank">📅 21:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697563">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92dec01ca3.mp4?token=j2rLeCH4WI2As9qzTQCSfGxE6s-gF1vRytM2IiNFzvjjTP-Uws3DhzJN6SEJoFDrpGRI5xhFNQuC17HxTE8VjF6H5y-4y14mhSSI6qLPk6fFb32XolwvLNB2W8CsNcJabpNc1mgzkBzTAqhaw93IYSbtZCtgKRdDGyPpb7Rx1ITAbOWOwhEpSr9TA77dET-DX00kFPO11pZQpAJgFqIPY5eeKOOsDINvOBXqx5waYNAo4zItojgH4BgjZtZX8me8fDN08On5RmIx1czbVf52tIT5-ykVCRv3VHRrak8u2ycmduIVGRfpeAUeBGK6ixx-v5WJObns95JeEir8l_Jqzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92dec01ca3.mp4?token=j2rLeCH4WI2As9qzTQCSfGxE6s-gF1vRytM2IiNFzvjjTP-Uws3DhzJN6SEJoFDrpGRI5xhFNQuC17HxTE8VjF6H5y-4y14mhSSI6qLPk6fFb32XolwvLNB2W8CsNcJabpNc1mgzkBzTAqhaw93IYSbtZCtgKRdDGyPpb7Rx1ITAbOWOwhEpSr9TA77dET-DX00kFPO11pZQpAJgFqIPY5eeKOOsDINvOBXqx5waYNAo4zItojgH4BgjZtZX8me8fDN08On5RmIx1czbVf52tIT5-ykVCRv3VHRrak8u2ycmduIVGRfpeAUeBGK6ixx-v5WJObns95JeEir8l_Jqzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازهم فاجعه در فوتبال؛ کتک زدن داور این بار در اصفهان
🔹
این اتفاق در لیگ‌ زیر ۱۳ ساله‌های اصفهان افتاده است.
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/697563" target="_blank">📅 21:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697562">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5fee01983.mp4?token=BFIjz2nBF9kjZT4YZ1f8FfPqrP35TNeApnVc_ofgCWJ1O0q85V8qbsAVoSaDhAsXSTvo_0G5fB5oUtNXftKxIalA7a52gvL-GJgD8yTt2VhaYfWY9_8RjFEGfK4g0_CN2ldiECbZaRBCruPw23VpFSZZ3vs27B0DmBpheVpjHpQK69FLAWiL9sjw9nYQqr9wJDUeYJIN3UWzj3Tg1ZYH0lnNeSI4PBk-1rI7eg7ueLyuE87afVyjI5Yo1GlQfutISLOn9APOf27hs4OnfD8yqMHWAlAVf1DU5M13MKe8CipLs_FvEui7z0NgtIzJCN05gbu0AiZ6nlmOOdi5cc1d3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5fee01983.mp4?token=BFIjz2nBF9kjZT4YZ1f8FfPqrP35TNeApnVc_ofgCWJ1O0q85V8qbsAVoSaDhAsXSTvo_0G5fB5oUtNXftKxIalA7a52gvL-GJgD8yTt2VhaYfWY9_8RjFEGfK4g0_CN2ldiECbZaRBCruPw23VpFSZZ3vs27B0DmBpheVpjHpQK69FLAWiL9sjw9nYQqr9wJDUeYJIN3UWzj3Tg1ZYH0lnNeSI4PBk-1rI7eg7ueLyuE87afVyjI5Yo1GlQfutISLOn9APOf27hs4OnfD8yqMHWAlAVf1DU5M13MKe8CipLs_FvEui7z0NgtIzJCN05gbu0AiZ6nlmOOdi5cc1d3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هدف قرارگرفتن یک کشتی متخلف در سواحل امارات
🔹
به‌دنبال صدور بیانیه نیروی دریایی سپاه درباره انفجار نفتکش متخلف در خلیج‌فارس،‌ امارات هم از آتش‌ گرفتن نفتکش خود در این منطقه خبر داد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/697562" target="_blank">📅 20:58 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697561">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f04822bdcc.mp4?token=acQDceWyOlDHUBaoCu2YtDBAv2a5fUG4hzbb-V2XRYLm4qrxDMEdCbQ-ydueFJLo5jMIJF44tAtTXRCEGndwKygkQyIEWrcKSsp2qipQESusedFc65nzBhf9RomoFDjWadZiqst3VAqfgeSAfj4UC8i9NxuvpXqDuZrkh26owMq97JmoDrXCcWtCp3t0VHxOnNiRzCz7Deb0ScfcUmHHltbUQQQ_SGI0trgb-jT8L8Jg2IaaRVs1GM7HXaeDSqtY3c7CvzSdlw1kvukgo_CLRPgkPBq5KxK9LUjIBTp9OdulcJ9u8M5yIW8cmHMY-Q0DP4aLdvGvUt0tFx_RRtGDyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f04822bdcc.mp4?token=acQDceWyOlDHUBaoCu2YtDBAv2a5fUG4hzbb-V2XRYLm4qrxDMEdCbQ-ydueFJLo5jMIJF44tAtTXRCEGndwKygkQyIEWrcKSsp2qipQESusedFc65nzBhf9RomoFDjWadZiqst3VAqfgeSAfj4UC8i9NxuvpXqDuZrkh26owMq97JmoDrXCcWtCp3t0VHxOnNiRzCz7Deb0ScfcUmHHltbUQQQ_SGI0trgb-jT8L8Jg2IaaRVs1GM7HXaeDSqtY3c7CvzSdlw1kvukgo_CLRPgkPBq5KxK9LUjIBTp9OdulcJ9u8M5yIW8cmHMY-Q0DP4aLdvGvUt0tFx_RRtGDyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قهوه رو اینجوری بخور
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/697561" target="_blank">📅 20:55 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697560">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aec4ba8b0a.mp4?token=MtKrrhBuhBFeAuPSGMi2GDVjNQHY2g1eJggetX7XqjueoUngODKGJutPt1oOlz0AYIjwZHBanWOJ_IZ2d2Ph4RnSWNtz9E8QfAMozCzsdWYve40z-Jpn043Ijg-_o1FeDl39P0ZQx_QItgCYlvXZo2ICGnUHSUu9DPL5FG3bDX1Wrb6udooQiRxgOD9twp2FO_WXO-gzIsvAJPnmU5dozPID3rxXRajse4XRmzbGKgWdv0-M8T6sGD7LARG5EJoes0cqpMnM9DdVv01FhtZhYNRpwpMEyJ7ImEbHmQ0tMGay4oAMII8XsB71WKhbF0dSh1GPBgOC1x5rDJoeoMBwJh_K2K2dxoe16NzfBVZI-KEc11_R2hVkhlASvzAm8h_Q6TPQyD9SHeHutqfixgXCl9jvoQbwo_sVfHbYP4uqR1Vqe-DkImVTpelUMBHu0FYzAOR3bQAJn4M91w2aAsq-q7H25diTGP-jHVUqxHgLsHqnXmRT0eTT06UETRTS-DPWW8rB0M5a6kEbM12iveUnP9BuM6jx2naRJDLXZWCmOAtzDGISitlbFCmLU1tPyDX9wtxEb6B7Xv6QrnEUYyggHFNdVvT8stzkQoGi_23ZEjT5mqqfyGUt9ioUWLnF_2EtqalWvt1xVIPOkHjgC8-zm1Xf4_vX-mpStpy1pktfbZM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aec4ba8b0a.mp4?token=MtKrrhBuhBFeAuPSGMi2GDVjNQHY2g1eJggetX7XqjueoUngODKGJutPt1oOlz0AYIjwZHBanWOJ_IZ2d2Ph4RnSWNtz9E8QfAMozCzsdWYve40z-Jpn043Ijg-_o1FeDl39P0ZQx_QItgCYlvXZo2ICGnUHSUu9DPL5FG3bDX1Wrb6udooQiRxgOD9twp2FO_WXO-gzIsvAJPnmU5dozPID3rxXRajse4XRmzbGKgWdv0-M8T6sGD7LARG5EJoes0cqpMnM9DdVv01FhtZhYNRpwpMEyJ7ImEbHmQ0tMGay4oAMII8XsB71WKhbF0dSh1GPBgOC1x5rDJoeoMBwJh_K2K2dxoe16NzfBVZI-KEc11_R2hVkhlASvzAm8h_Q6TPQyD9SHeHutqfixgXCl9jvoQbwo_sVfHbYP4uqR1Vqe-DkImVTpelUMBHu0FYzAOR3bQAJn4M91w2aAsq-q7H25diTGP-jHVUqxHgLsHqnXmRT0eTT06UETRTS-DPWW8rB0M5a6kEbM12iveUnP9BuM6jx2naRJDLXZWCmOAtzDGISitlbFCmLU1tPyDX9wtxEb6B7Xv6QrnEUYyggHFNdVvT8stzkQoGi_23ZEjT5mqqfyGUt9ioUWLnF_2EtqalWvt1xVIPOkHjgC8-zm1Xf4_vX-mpStpy1pktfbZM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سلاح کشتار جمعی زیر کت مکرون
🔹
رئیس‌جمهوری که برای ترسناک به نظر رسیدن، به‌راحتی آزمایش اتمی انجام میده و دنیا رو تهدید می‌کنه! اما واقعا چه کسانی دارن امنیت جهان رو به خطر می‌اندازن؟
🔹
جزئیات رو توی این ویدئو ببینید.
@TV_Fori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/697560" target="_blank">📅 20:47 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697559">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YccbDzWAFyzEd-19rY_xMa7c9-YyJjNNrdF5zxcf9QdbinUNnkkkljvQ4Is8hiNkbiS3BzdyJ_p-rbiUfAAySV1X383kSutW2VclTsL5lZXClwxavotmmFhtmM2ll1rjUZAUd_D3tZpj1hQyBThr3ws2P7g6Vs4MdS5AGHwgchD9mkUiv-5kvXUwb0eXnZUJ7PYzLlb8bE8W7UCHrjRIicLuW82wFULWbwVVeH0jdsIkoFqLuFOy0zXMLA2_L1x0BntgSGYbANsEx4VFPIhBxnQZIvIZd5oqCcangkh00rncS0JElIHvm6UBHjas5wYssDTiswuknrEA27jP7YnZAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پایان صف تسویه در میلی/ ۱۳ همت پول به کاربران واریز شد
🔹
میلی از پایان صف درخواست‌های برداشت کاربران خبر داد. بر اساس اعلام این پلتفرم، از ۲۰ شهریور تا ۱۸ مهرماه، بیش از ۱۳ هزار و ۲۱۳ میلیارد تومان از مطالبات کاربران تسویه شده و ۶۹۶ هزار درخواست برداشت با موفقیت انجام شده است.
🔹
همچنین ۲۶۳ هزار درخواست برداشت از سوی کاربران لغو شده و تمامی درخواست‌های معوق از طریق تسویه ریالی تعیین تکلیف شده‌اند. با پایان صف، تسویه درخواست‌های جدید طبق روال عادی ادامه دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/697559" target="_blank">📅 20:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697558">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c020369ef.mp4?token=oxO_C6uQ9ce_E7Satgz5PQrQk_lXJq6CzrRq6gqnBl6DG0ytoWgaEKoSXNUF6TQAlvTi9sg8oKlfUu3BqxJKjYhrH-DrjehM24r07bqUK-zYyK9JU4F3lLDKtYYXM9vDl8FeF8k9_TFKQz_P1VqQgYb0QY6_HYMx3JTVWKksKsK-V65Pos73h28iHD0VpZQY9alhsfkkihIKxsEZvAvJZ5qQfj_aAY0fqupuLBLNFqminZTMCRVLNt3aqsqnDbKUCCHUo1mHxX2gUmiTNUz3GU7TXIYrUzF0BMUynFZzAYy98Ez-CLvyjuIUqwSAWI8gRc3Ro7UshJMCs7Ssc9DjJamhS3nqwt7CT8RKRNSqbSIkHQecTndpwsUdSNVWlV0R95RILbi3Pe3cle_FIqin418wSe72JZd_6jSR8VFORCMLumPTSXmhP4q9fzsWx99aQeA82TXhILbexLbNTt3H53wHxn26OyXuk6kUwjUTXxqzAGjyczqdC4C86RGferpUezy7OQJ5yOzfRTc-SSXjGcc0j8huS3Rh-x5y16NdyijZasXKVRiXmR9oBgM9_z3hmTSopB0lG4r5XBQ4FGa3vdxFagzTUKZaL0yO9gBusclVPgbAchMIlBVFhFGLG8vqwsjjzAuTfITLLXdz2Vi_PbfOdLjMosqyGFdv7kMSnyI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c020369ef.mp4?token=oxO_C6uQ9ce_E7Satgz5PQrQk_lXJq6CzrRq6gqnBl6DG0ytoWgaEKoSXNUF6TQAlvTi9sg8oKlfUu3BqxJKjYhrH-DrjehM24r07bqUK-zYyK9JU4F3lLDKtYYXM9vDl8FeF8k9_TFKQz_P1VqQgYb0QY6_HYMx3JTVWKksKsK-V65Pos73h28iHD0VpZQY9alhsfkkihIKxsEZvAvJZ5qQfj_aAY0fqupuLBLNFqminZTMCRVLNt3aqsqnDbKUCCHUo1mHxX2gUmiTNUz3GU7TXIYrUzF0BMUynFZzAYy98Ez-CLvyjuIUqwSAWI8gRc3Ro7UshJMCs7Ssc9DjJamhS3nqwt7CT8RKRNSqbSIkHQecTndpwsUdSNVWlV0R95RILbi3Pe3cle_FIqin418wSe72JZd_6jSR8VFORCMLumPTSXmhP4q9fzsWx99aQeA82TXhILbexLbNTt3H53wHxn26OyXuk6kUwjUTXxqzAGjyczqdC4C86RGferpUezy7OQJ5yOzfRTc-SSXjGcc0j8huS3Rh-x5y16NdyijZasXKVRiXmR9oBgM9_z3hmTSopB0lG4r5XBQ4FGa3vdxFagzTUKZaL0yO9gBusclVPgbAchMIlBVFhFGLG8vqwsjjzAuTfITLLXdz2Vi_PbfOdLjMosqyGFdv7kMSnyI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عربستان سعودی اصابت موشک و وقوع آتش‌سوزی در فرودگاه ملک خالد ریاض را تایید کرد
🔹
دقایقی پیش ترمینال مسافربری شماره ۴ فرودگاه ریاض مورد حمله قرارگرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/697558" target="_blank">📅 20:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697557">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
تغییر جدیدی در روند مذاکرات غیرمستقیم ایران و آمریکا رخ نداده است
🔹
بررسی پاسخ آمریکا به طرح ۷ ماده‌ای ایران در داخل کشور ادامه دارد و پیش‌بینی می‌شود این پاسخ طی چند روز آینده از طریق میانجی قطری به آمریکا منتقل شود./ جماران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/697557" target="_blank">📅 20:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697556">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
بدون نظریه اینشتین، مسیریاب گوشی شما روزانه چندین کیلومتر خطا داشت!
🔹
ماهواره‌های GPS با اندازه‌گیری زمان حرکت سیگنال‌ها، موقعیت شما را تعیین می‌کنند؛ اما ساعت آن‌ها به‌دلیل تفاوت گرانش و سرعت حرکت، روزانه حدود ۳۸ میکروثانیه سریع‌تر از ساعت‌های زمینی کار می‌کند.
🔹
نور در این مدت بیش از ۱۱ کیلومتر حرکت می‌کند! بدون اصلاح این اختلاف زمانی با استفاده از نظریه‌های نسبیت خاص و عام اینشتین، خطای GPS به‌سرعت افزایش می‌یافت و مکان‌یابی دقیق مختل می‌شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/697556" target="_blank">📅 20:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697555">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
مهلت انتخاب رشته کنکور ۱۴۰۵ تا پایان روز دوشنبه ۲۰ مهر تمدید شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/697555" target="_blank">📅 20:18 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697554">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e933c02e46.mp4?token=Y3QYQ_piPHfiu7spwZuEQc9g1oIA-UqU1VKZYLWWncqB0jcWnRvLXgrabhk-vZqPMhMd7Nj76N5g-gIsJSFACV3gOKz4mISQPquepNbGVV0L8X628Ca2kWaISdCzF4saK9Rw_c5d8HSj2f6YZAKtSSrsyTPboz2vpPAoKarcD3pzAjYho3skJrM2aI7Kprlb-4BQ-hKQkiTu8Q47Nu1C82ub4Fw_iiRvixp2BCXI3eb3MIQxm2gx7WsMXD6kl73KjkQICMW3xA95SPK92lAPSozE-Hm6zrshgcv0bDelCLJUnw8iFue6YUJfE3ifNqgRPGy-EYq69Ir23v_uveqknQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e933c02e46.mp4?token=Y3QYQ_piPHfiu7spwZuEQc9g1oIA-UqU1VKZYLWWncqB0jcWnRvLXgrabhk-vZqPMhMd7Nj76N5g-gIsJSFACV3gOKz4mISQPquepNbGVV0L8X628Ca2kWaISdCzF4saK9Rw_c5d8HSj2f6YZAKtSSrsyTPboz2vpPAoKarcD3pzAjYho3skJrM2aI7Kprlb-4BQ-hKQkiTu8Q47Nu1C82ub4Fw_iiRvixp2BCXI3eb3MIQxm2gx7WsMXD6kl73KjkQICMW3xA95SPK92lAPSozE-Hm6zrshgcv0bDelCLJUnw8iFue6YUJfE3ifNqgRPGy-EYq69Ir23v_uveqknQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در نهایت متوجه میشی که مسیر سخت، تنها مسیریه که ارزش طی کردن داره …</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/697554" target="_blank">📅 20:16 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697553">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e753101023.mp4?token=b8hyg6gaiR-06qr9yn5rstgP18bcuD-ykJ6viwlKHKFZFTBLoLdq-fnTE1evGv6pp5VFOFiQy6tgOmjRqzjt1gnWbOsFq8wMngi9cfcQKKeMBTXPD1txfo5ve5ycr6ino0omNWMTN5AT0O2uPfhFHd34brdALQQ4XI-LOydfIrMqCqitTN0OXGf0josKCxOqPS9aKba_pNQo8snKRcsCw7aVnupUnxd4fJhNF5g6wOtEYrEmPpuZa1pwt2XDIbN1PHs20lNBuXP1rQ9obKlOWRaQ_XHPJTAErNv5aOYv4BUv78odRB1ksoc0mHrM28tok85btTZtPv9hqwUGk1PSzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e753101023.mp4?token=b8hyg6gaiR-06qr9yn5rstgP18bcuD-ykJ6viwlKHKFZFTBLoLdq-fnTE1evGv6pp5VFOFiQy6tgOmjRqzjt1gnWbOsFq8wMngi9cfcQKKeMBTXPD1txfo5ve5ycr6ino0omNWMTN5AT0O2uPfhFHd34brdALQQ4XI-LOydfIrMqCqitTN0OXGf0josKCxOqPS9aKba_pNQo8snKRcsCw7aVnupUnxd4fJhNF5g6wOtEYrEmPpuZa1pwt2XDIbN1PHs20lNBuXP1rQ9obKlOWRaQ_XHPJTAErNv5aOYv4BUv78odRB1ksoc0mHrM28tok85btTZtPv9hqwUGk1PSzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش مدیرعامل پرسپولیس به پیشنهاد استقلال برای از سرگیری جام حذفی: قاعدتا نمی‌توانند مسابقات را از سر بگیرند وگرنه لیگ هم باید ادامه پیدا می‌کرد
پیمان حدادی، مدیرعامل باشگاه پرسپولیس در
#گفتگو
با خبرفوری:
🔹
بحث ادامه جام حذفی را دوستان فدراسیون باید بررسی کنند اما فکر نمی‌کنم عملی شود، زیرا آن فصل تمام شد و فدراسیون و سازمان لیگ به AFC اعلام کردند که مسابقات لیگ و جام حذفی، نیمه  کاره تمام شدند و قاعدتا نمی‌توانند آن مسابقات را از سر بگیرند و اگر به این شکل بود، لیگ گذشته هم باید ادامه پیدا می‌کرد.
🔹
فکر نمی‌کنم که اختلاف امتیاز زیادی در لیگ گذشته وجود داشته باشد، اگر مسابقات ادامه پیدا می‌کرد، حتما در صدر جدول شاهد تغییر در رتبه‌بندی تیم‌ها بودیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/697553" target="_blank">📅 20:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697552">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
عربستان سعودی اصابت موشک و وقوع آتش‌سوزی در فرودگاه ملک خالد ریاض را تایید کرد
🔹
دقایقی پیش ترمینال مسافربری شماره ۴ فرودگاه ریاض مورد حمله قرارگرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/697552" target="_blank">📅 20:07 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697551">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‌
♦️
دبیر شورای‌عالی امنیت ملی: آمریکا دارایی‌های بسیار گران‌قیمتی در امارات و پیرامون تنگهٔ هرمز دارد که ما هنوز آن‌ها را در میان اهداف خود نگنجانده‌ایم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/697551" target="_blank">📅 20:06 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697550">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71d86d3bae.mp4?token=iK_mL8CAYf6UV56tRmDuQa3TXRS_8Vr6vNRocX7Dly7u-vnUlr-lEzujC65cxiDKp1addmpajN31En0uPEIVOYndODncN8jvLgEPihiKmPmWEtAC_hvaVHfG-brBxyPswz99j8mYbhJbOcfQc20-hWUAr6My7CEbb88ODVlgEbunwyqmrMa7mp7L9Dss2gyCRZq0Mbmc4sBhg83u7aWwt5-BuSMpCoE5164cwP3SvAwtggQGGznswScGvzKMXJNRCXdKurqXtwwhNhNq8fmKs31Mo30-ZlB0CoBNa9dIuFuUmDQv0lozpzQ874qFrOdBcBIyHPzobNhT3INNcF_VUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71d86d3bae.mp4?token=iK_mL8CAYf6UV56tRmDuQa3TXRS_8Vr6vNRocX7Dly7u-vnUlr-lEzujC65cxiDKp1addmpajN31En0uPEIVOYndODncN8jvLgEPihiKmPmWEtAC_hvaVHfG-brBxyPswz99j8mYbhJbOcfQc20-hWUAr6My7CEbb88ODVlgEbunwyqmrMa7mp7L9Dss2gyCRZq0Mbmc4sBhg83u7aWwt5-BuSMpCoE5164cwP3SvAwtggQGGznswScGvzKMXJNRCXdKurqXtwwhNhNq8fmKs31Mo30-ZlB0CoBNa9dIuFuUmDQv0lozpzQ874qFrOdBcBIyHPzobNhT3INNcF_VUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این ترفند، قدیمی‌ترین لکه‌های چربی هود و کابینتت رو ازبین ببر! #ترفند_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/697550" target="_blank">📅 20:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697549">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-o1czF6Z7l8zOSlA5SDPnN65uZqbCV-53_mz6_LWD1ob6uFrw2dUQd8eq2zPmNSH6Bu9xlh859jebfoY8KIdokFb7ZWm28c9t7SVcPtKenXJfUQUEmVBOTWB-bwh0WNhHrq_BjKOKvai2_LVJKAAUR7Sw94tKtGM99GL2yJ7pGQY_mWloZa2eTF0dw5O1FUDpkJE6x-IDx45yZXQK9WKT_VLsO68K7G2w55ais_v_tHU4WxE4DOgk_tQ__GTJnoySgFW5lTem-4Ksc_LqudL0k7wRau59VGfD1Lutj_IKrak9aChWFtD_nMcGGXb1k0cpT3jelDIiP0HdkQHU-y3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سه آبگیر با سه رنگ متفاوت گیلان زیبا
🇮🇷
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/697549" target="_blank">📅 19:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697548">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UYmQnQ2PN_s0OZr4crEil-fMiJ6Fim3leyhrmk_Ia7XvOuaXTP9GunIZ_tbIUJQ_-VhSXXEwJDAbUXT-LHoiRs2Mkwkewv9tRmmmT4sbcFSMIR_MCL2O-1-qvAEStMkWcaalM-i2QbROLqKcfR-KmCvC-ntaYr_LLcdA5h-IWhzljZtbdpEuzQhG8fYevO6-K4fIRmczyl4rDnK1d-JnLcJ7ay0dp1BOetHqSE9vuKQRKinA-F4wpuFsWkU2d8EcLZR0y1fLTHo2UML8fSpKTfSRcTZB0KiwTIC-lpe29447hWgnb2U9GOUjbLZOPTrhhb4TC8foS1k8sgdcIJf2TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تهران نه، ریاض
🔹
پس از ۸ ماه جنگ آمریکا علیه ایران، دامنه‌درگیری‌ها به دیگر نقاط منطقه کشیده شده است. آمریکا که به دنبال مختل کردن پروازهای ایران و اعمال محاصره هوایی بود، حالا در پی تشدید درگیری‌های انصارالله و عربستان، با توقف فعالیت فرودگاه ریاض و لغو گسترده پروازها روبه‌رو شده است. این تحولات بار دیگر یک واقعیت را یادآوری می‌کند، در خاورمیانه صلح و آرامش یک‌جانبه معنایی ندارد، یا صلح برای همه است یا برای هیچ‌کس. جنگ‌افروزی آمریکا اکنون بیش از هر زمان دیگری پیامدهای خود را نشان می‌دهد، پیامدهایی که از مرزهای ایران فراتر رفته و دامن متحدان منطقه‌ای آمریکا را فرا گرفته است.
🔹
هشتصدوهشتادوسومین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/697548" target="_blank">📅 19:42 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697547">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
لایو ای‌آی‌اس به نقل از ملوانان نفتکش‌ها در تنگه هرمز: اسکورت‌های آمریکا دیشب پس از حمله به یک کشتی، در میانه راه متوقف شدند
🔹
دو کشتی خروجی پس از حادثه امنیتی، مسیر خود را تغییر دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/697547" target="_blank">📅 19:38 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697546">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcff288f73.mp4?token=tbpMFe0P-XPw-khlCkcDCmeSyma5ihQLzGvEix7XsdNzvG1Cg5dER8dpcdWMeIYYsZSPrT-YbrvPcfjJmSIAwAB99lT0YGZqNiFWqu_0wJr5PcK3RcLrwviIne6rIKN6rEw_k3D7PDhv5dYMv4AF2OQTzZiPThO52XANxm8Gnzc4wF-c2_vAv5TVu-Y1loJGKxsyOZvKgGxTR_Huiy8fA6oVFypIiBefxT98t7I3fcbX7JbcDRJxzPz66vH-lMUZsELCdYeDAzMRgIpY7Kv9Us0s1trqSuZDBm3Q8d8ZiCs2TPt8li_VD1BrFRZEw2hNXNjvLSru_liKyy_l04Yvsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcff288f73.mp4?token=tbpMFe0P-XPw-khlCkcDCmeSyma5ihQLzGvEix7XsdNzvG1Cg5dER8dpcdWMeIYYsZSPrT-YbrvPcfjJmSIAwAB99lT0YGZqNiFWqu_0wJr5PcK3RcLrwviIne6rIKN6rEw_k3D7PDhv5dYMv4AF2OQTzZiPThO52XANxm8Gnzc4wF-c2_vAv5TVu-Y1loJGKxsyOZvKgGxTR_Huiy8fA6oVFypIiBefxT98t7I3fcbX7JbcDRJxzPz66vH-lMUZsELCdYeDAzMRgIpY7Kv9Us0s1trqSuZDBm3Q8d8ZiCs2TPt8li_VD1BrFRZEw2hNXNjvLSru_liKyy_l04Yvsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ساخت گل‌های زیبا و دست‌ساز با وسائل دم‌ِدست
🌼
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/697546" target="_blank">📅 19:37 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697545">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dcb792439.mp4?token=g8nEuwJoqEwR6Y8jsVOAo8dPyfn5WrjZny9rmMkpATcZOwdQw0-OZJU2mq3WvkNpRxIWSMp95nLMWICYjgqmJU6DUMlgUyvhlUjSekq9aWH3GaX0iOWsaBWtwa2dXKm3XE5q4xh7KWJR8ZOSBse6ARBgjlmnR5IXsrph6oWIaEJDdws6YVdmmSfZdtSQu12uweLy0NEujjlZ3IIr0IItA1VvKCqJj4g-CMYZ6KAshSKLGylyqGEcEcSFfyIUZCuebEhfPx4Cr3R__5uYaEnhJfatS56GIjXKw20hcuLOgvbnjW84I12sOilVxwWkokSg7gMbMFf-xinim_z_1uvuBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dcb792439.mp4?token=g8nEuwJoqEwR6Y8jsVOAo8dPyfn5WrjZny9rmMkpATcZOwdQw0-OZJU2mq3WvkNpRxIWSMp95nLMWICYjgqmJU6DUMlgUyvhlUjSekq9aWH3GaX0iOWsaBWtwa2dXKm3XE5q4xh7KWJR8ZOSBse6ARBgjlmnR5IXsrph6oWIaEJDdws6YVdmmSfZdtSQu12uweLy0NEujjlZ3IIr0IItA1VvKCqJj4g-CMYZ6KAshSKLGylyqGEcEcSFfyIUZCuebEhfPx4Cr3R__5uYaEnhJfatS56GIjXKw20hcuLOgvbnjW84I12sOilVxwWkokSg7gMbMFf-xinim_z_1uvuBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مدیرعامل پرسپولیس: در ازای هر گلی که بزنیم، یک نفر را آزاد می‌کنیم/ در این فصل ۴۳ زندانی آزاد شدند
پیمان حدادی، مدیرعامل باشگاه پرسپولیس در
#گفتگو
با خبرفوری:
🔹
از آذر ماه سال گذشته، باشگاه پرسپولیس به عنوان بزرگترین تشکل مردمی غیر دولتی کشور، کمپین مهر سرخ را شروع کرد و در این پویش یکی از کارهای اساسی و بزرگی که به کمک هواداران انجام دادیم، آزادسازی زندانیان مالی جرائم غیر عمد است.
🔹
سال گذشته در استان تهران، ۶۰ نفر از هم‌وطنان که در زندان‌های تهران بودند، آزاد شدند و در ماه گذشته، در بازی پرسپولیس - استقلال ۶ نفر دیگر از هموطنان آزاد شدند.
🔹
امروز در آستانه بازی هشتم پرسپولیس در لیگ، در شهر آقا امام رضا (ع) نیت داشتیم که ۸ نفر دیگر را آزاد کنیم، اما به کمک خیرین، این ۸ نفر به ۳۷ نفر افزایش پیدا کرد و مجموعا طی این پویش ۱۱۰ نفر را آزاد کردیم.
🔹
از ابتدا این فصل قرار شد به ازای هر یک گلی که یکی از ۶ تیم فوتبال پرسپولیس می‌زند، تحت عنوان گل آزادی، یک نفر را آزاد کنیم و در این فصل ۴۳ زندانی آزاد شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/697545" target="_blank">📅 19:27 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697544">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/517f29697b.mp4?token=QMBd5s6RGMabmmbido5KL_U8rfy-vuz09tvk07f0ci28MR_JjvuWIEuPJtRD851oG_F_qi7tdJ72U6ZCZFSLmeoEy72-dr8_zBtDWV_S6MjeVVcYDCkOyTLcxqxy0NFcSoMPpyYetTglRqrAE_M_VnVzOXAmb2M6EsOtQdH3C1xOH6yYDfX3QrQKLVUX7198GH-0yOaB6iOZZGS0rjnF7gPKGW8c4AEaltMXtZ71F8zmSh5FNwpDLTUzUWQP4NL-HDImar7QDGVeQyNHgcl1z2pKTXvz5TNJNEkx1uBjKBcLjID60_97syH1rektxBgtxROESRf7wIgPCW-92X7GHjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/517f29697b.mp4?token=QMBd5s6RGMabmmbido5KL_U8rfy-vuz09tvk07f0ci28MR_JjvuWIEuPJtRD851oG_F_qi7tdJ72U6ZCZFSLmeoEy72-dr8_zBtDWV_S6MjeVVcYDCkOyTLcxqxy0NFcSoMPpyYetTglRqrAE_M_VnVzOXAmb2M6EsOtQdH3C1xOH6yYDfX3QrQKLVUX7198GH-0yOaB6iOZZGS0rjnF7gPKGW8c4AEaltMXtZ71F8zmSh5FNwpDLTUzUWQP4NL-HDImar7QDGVeQyNHgcl1z2pKTXvz5TNJNEkx1uBjKBcLjID60_97syH1rektxBgtxROESRf7wIgPCW-92X7GHjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خیلی از خوراکی‌هایی که روزانه میخوریم احتمال ابتلا به کبد چرب رو افزایش میده!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/697544" target="_blank">📅 19:17 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697543">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/714574dcee.mp4?token=YGF4hr1ox2ii3l8NW9cwi0rOJgEG40vH7v5huskwoGjlTBvLpQzuDTrq-jPsLt93x0X5ZI9ZosHZphcbyvWJNoPFwKXaQlhB79R_J0lA2KmXISAKTZc5PkwdFCPgR7Y3StNK5s-tvZ42P0_YUjJb82Ln_00oD4YCknIviO8qWovTXf4YBtMhFdSVMiI92agM6ERi1IgI3xb_uu5JAvb_miazl1yx_vuiInG8DAK48oBwOzexBsn_9zeVKGCgQH3To4iJTzuU1qgGMmDOe2ZNyCRWXk2TptQuUfdFK6msPHNPYOHZtyh-ar2Xs1D0cLLeiH_dGSeZhemKrfcWPrQyrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/714574dcee.mp4?token=YGF4hr1ox2ii3l8NW9cwi0rOJgEG40vH7v5huskwoGjlTBvLpQzuDTrq-jPsLt93x0X5ZI9ZosHZphcbyvWJNoPFwKXaQlhB79R_J0lA2KmXISAKTZc5PkwdFCPgR7Y3StNK5s-tvZ42P0_YUjJb82Ln_00oD4YCknIviO8qWovTXf4YBtMhFdSVMiI92agM6ERi1IgI3xb_uu5JAvb_miazl1yx_vuiInG8DAK48oBwOzexBsn_9zeVKGCgQH3To4iJTzuU1qgGMmDOe2ZNyCRWXk2TptQuUfdFK6msPHNPYOHZtyh-ar2Xs1D0cLLeiH_dGSeZhemKrfcWPrQyrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس دانشگاه فردوسی مشهد:
روایت تحول و تغییر رویکرد خاص در معاونت علمی، باید مورد توجه نخبگان کشور قرار بگیرد.
🔹
عبدالرضا جوان‌جعفری، رئیس دانشگاه فردوسی مشهد، با اشاره به اهمیت سخنرانی دکتر حسین افشین، معاون علمی، فناوری و اقتصاد دانش‌بنیان رئیس‌جمهور، درباره «تغییر پارادایم معاونت علمی»، از نخبگان، استادان و دانشجویان دعوت کرد این سخنرانی را با دقت بشنوند.
🔹
این دعوت، بر اهمیت تبیین رویکردها و سیاست‌های جدید در زیست‌بوم علم، فناوری و نوآوری کشور و ضرورت آگاهی جامعه دانشگاهی از مسیر تحول در معاونت علمی تأکید دارد.
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/697543" target="_blank">📅 19:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697542">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
محسن رضایی خطاب به روبیو: قدرت‌های بسیاری در طول تاریخ رؤیای اشغال ایران را داشتند، اما نامشان از تاریخ پاک شد و ملت ایران همچنان باقی ماند
🔹
هرچه بیشتر علیه ایران تلاش کنید، بیشتر در باتلاق فرو می‌روید و بار دیگر در برابر ملت ایران زانو خواهید زد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/697542" target="_blank">📅 19:07 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697541">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 اگر بخواهید یک مشکل اجتماعی را در محله خود حل کنید، کدام را در اولویت قرار می‌دهید؟</h4>
<ul>
<li>✓ آلودگی و نظافت</li>
<li>✓ امنیت</li>
<li>✓ کمبود فضای سبز</li>
<li>✓ کمبود امکانات ورزشی و فرهنگی</li>
<li>✓ آسیب‌های اجتماعی</li>
<li>✓ فرسودگی معابر</li>
</ul>
</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/697541" target="_blank">📅 19:06 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697540">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
اظهارات بی‌شرمانه روبیو، وزیر خارجه آمریکا علیه مردم ایران
🔹
هخامنشیان ۴۸۰ سال پیش از میلاد به یونان حمله کردند و آنجا را غارت کردند ریشه ایرانی‌ها به این غارتگران برمی‌گردد!
🔹
او در لفاظی‌اش علیه تاریخ کهن ایران به این واقعیت هیچ اشاره‌ای نکرد که ۴۰۰ سال…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/697540" target="_blank">📅 19:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697539">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
محسن رضایی: می‌توانستیم تنگه هرمز را کاملاً ببندیم، اما به دلایل انسان‌دوستانه این کار را نکردیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/697539" target="_blank">📅 18:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697538">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/499fae8935.mp4?token=QKUuflA8n1cF32XbkaaX-_1-iHP4aeE5c6aZWQLlbkEtejNak4ElKku1lMGHq0fO3t9bI9t-1sokWDL_BYPoBzLte7cniAXyHrvJniqqHQ6LcGTM3dmfz9_6AnKMFbTi6YDsqo60ntB4mIrt4XzhbHdB32w-fxfdhabKOMJh3afJoSOI_DfPUaO5lq7uEhzNJQhQG4Lfkd_OIIdWlVQvsgOeVckEM2duVQe2Ko90ewvp3fuJGdmknsjr42RJ_vjr455RDFNLIS2OxY094nvSaPUxrB8DNpRb53xjXNMZ17aWwAyc5ysXSEJ-gPMWW9XSldj8VFDOBVGibyh8nwVT3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/499fae8935.mp4?token=QKUuflA8n1cF32XbkaaX-_1-iHP4aeE5c6aZWQLlbkEtejNak4ElKku1lMGHq0fO3t9bI9t-1sokWDL_BYPoBzLte7cniAXyHrvJniqqHQ6LcGTM3dmfz9_6AnKMFbTi6YDsqo60ntB4mIrt4XzhbHdB32w-fxfdhabKOMJh3afJoSOI_DfPUaO5lq7uEhzNJQhQG4Lfkd_OIIdWlVQvsgOeVckEM2duVQe2Ko90ewvp3fuJGdmknsjr42RJ_vjr455RDFNLIS2OxY094nvSaPUxrB8DNpRb53xjXNMZ17aWwAyc5ysXSEJ-gPMWW9XSldj8VFDOBVGibyh8nwVT3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دبیر شورای‌عالی امنیت ملی: تهران به رویه‌های دیپلماتیک گذشتۀ خود باز نخواهد گشت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/697538" target="_blank">📅 18:49 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697537">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d461159826.mp4?token=Jk8OL-jM-1JDaMJjTI_xOKlxl4D3Ory17G0VDxJstWNrAYLjCOv2eGooFj4u6OLGhY3utuw8K3BxPqd8njmxBBwtxwPYXjkdmOpyasduzW8nDPHW92Ob95C9NO-RNPz-SIMyjqluxW6MzbmowwaeI8VPAAL1wkYvblvPRqNXTBXIGzkEMH6IGfLbTYxh-wCogxuCUr53MFTkQ0KByXpwKrVymL4oAeH0ofjQvywJ9pTL6Lr6o5XkWSdnKHeD116xpa5Y5aRjSIXhSklsPaq01UyrJvDTFGFBehRRQq5P4I4xAQ1plBF5YJasS8FpzQedMhEpZRW2FteNEJYpJBxrPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d461159826.mp4?token=Jk8OL-jM-1JDaMJjTI_xOKlxl4D3Ory17G0VDxJstWNrAYLjCOv2eGooFj4u6OLGhY3utuw8K3BxPqd8njmxBBwtxwPYXjkdmOpyasduzW8nDPHW92Ob95C9NO-RNPz-SIMyjqluxW6MzbmowwaeI8VPAAL1wkYvblvPRqNXTBXIGzkEMH6IGfLbTYxh-wCogxuCUr53MFTkQ0KByXpwKrVymL4oAeH0ofjQvywJ9pTL6Lr6o5XkWSdnKHeD116xpa5Y5aRjSIXhSklsPaq01UyrJvDTFGFBehRRQq5P4I4xAQ1plBF5YJasS8FpzQedMhEpZRW2FteNEJYpJBxrPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای وزیر خزانه‌داری آمریکا: اگر این ایرانی‌ها کشورشان را دوست دارند، تبریک می‌گویم، شما باید آنجا بمانید
🔹
آنها نمی‌توانند اقوامشان را در لندن ببینند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/697537" target="_blank">📅 18:41 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697536">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
محسن رضایی: بخشی از محموله‌هایی هم که اکنون جابه‌جا می‌شوند، متعلق به خود ما هستند. ما این محموله‌ها را مدیریت می‌کنیم تا غلات، اقلام ضروری و سایر کالاهای اساسی را وارد کشور کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/697536" target="_blank">📅 18:39 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697535">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
دبیر شورای عالی امنیت ملی: حمله آمریکا به ایران جزو احمقانه ترین جنگ های تاریخ بشر است
🔹
دولت ترامپ چشم بسته افسار خود را دست نتانیاهو داد و بدون برآورد دقیق وارد جنگ با ایران شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/697535" target="_blank">📅 18:38 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697534">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KvXw2QwxgRGFar9w_RmOBcnwdegBmdwj5xh-iHWtgL0NDfGLke_sb6nbCPjez9ijDL_DA5OCCYtgZT1rMDFCsPLIlKsDQ450LuU1Z6KSZhuQD7sjHGz62Egb4qzs4zpzozp9lQmx-cll2fhMM0Hcm06tAACEm_-8OrHNzjAiwdipABniu6g5UjrQuxZP90tcxGzeffoRqIAr3eI-cdZc3zCMLamIXnJPBSkeb0Dp5XSBhzHvRIkthzeKLvf6Zb31g4Wiql2k5H15-Cp12H5otrIy1N2R0Rzsl7AAxAZMX8hg-B1zXfj-NhtbHX_MSAJ79XP9yfb6Jj0G_j6VLJm97Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۵ سناریو برای انتخابات اسرائیل | نتانیاهو می‌ماند یا سقوط می‌کند؟ | ایران چگونه می‌تواند معادلات انتخابات اسرائیل را تغییر دهد؟
🔹
انتخابات پارلمانی اسرائیل پنج آبان در شرایطی برگزار می‌شود که این رژیم پس از سال‌ها بی‌ثباتی سیاسی، جنگ چندجبهه‌ای و تشدید شکاف‌های اجتماعی، با پنج سناریوی متفاوت روبه‌روست؛ از اختلال در رأی‌گیری و بن‌بست سیاسی گرفته تا پیروزی نتانیاهو، تشکیل دولت مخالفان یا ایجاد ائتلافی فراگیر برای عبور از بحران.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3251597</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/697534" target="_blank">📅 18:37 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697533">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
محسن رضایی: آمریکا برخی از شروط ۷ گانه ایران را پذیرفته/ ما پاسخشان را ناکافی می‌دانیم
🔹
تنگه هرمز برای تضمین صلح و امنیت منطقه تحت مدیریت ما باقی خواهد ماند و ما در این موضوع عقب‌نشینی نخواهیم کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/697533" target="_blank">📅 18:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697532">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
‌دبیر شورای‌ عالی امنیت ملی: اگر دوباره جنگی در بگیرد، بسیاری از کابل‌ها، دیتاسنترها، تأسیسات هوش مصنوعی و سایت‌های دیگر موجود در منطقه نابود خواهند شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/697532" target="_blank">📅 18:32 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697531">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‌
♦️
دبیر شورای‌عالی امنیت ملی: آمریکا دارایی‌های بسیار گران‌قیمتی در امارات و پیرامون تنگهٔ هرمز دارد که ما هنوز آن‌ها را در میان اهداف خود نگنجانده‌ایم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/697531" target="_blank">📅 18:27 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697530">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
دبیر شورای‌عالی امنیت ملی: ترامپ با استخدام تعدادی از اشرار که در آب‌های ساحلی عمان فعالیت می‌کنند، به قاچاق روی آورده است
🔹
طی چند ماه گذشته، ما هر شب در تنگهٔ هرمز ۵ فروند از کشتی‌هایی را که قاچاقچیان استفاده می‌کردند هدف قرار داده‌ایم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/697530" target="_blank">📅 18:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697528">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
ادعای ترامپ : از همین لحظه، در جنگ میان روسیه و اوکراین آتش‌بس در حوزه انرژی برقرار می‌شود؛ هر ۲ طرف توافق کرده‌اند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/697528" target="_blank">📅 18:22 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697527">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
عربستان سعودی اصابت موشک و وقوع آتش‌سوزی در فرودگاه ملک خالد ریاض را تایید کرد
🔹
دقایقی پیش ترمینال مسافربری شماره ۴ فرودگاه ریاض مورد حمله قرارگرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/697527" target="_blank">📅 18:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697519">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/igGGntxwE4xALoM75dt8XrHIqQo-GrRTaZUGW-ZQ7XfBV2jz0ZvcnYAtw-zm_YBHRgZmYuzgY9al5XzW-lf4pSbH4qzoJC3-mRJ_v22nRDUuYXTY29uJC3gM2II_oKziaFLsbTVYnrgNOLXM3rUow5p2W2Yehnj6Zg5Qi5lkaYC0t-ZMlS3UKKia0EeQ0R-fyZQPtDWk30lcdew-hnAqEQST7t9hZBLg16Ybm5-_-kQxORgiHmliJbCdEkrOnCMdTJktYLE4FikWjsy3c9sDQV5xitZy0WKZxwAoYJa6XVlMJw3h2bTu_aZBxsyKFC2V9D6oFGHKDNT_0KO7urGvFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lIOAv0QgN9qC7uV5cQqurvGJ2ljFzS864jV4wJGTKoaf824sUkgmFiYW6zhyoRneJeV-7sJcM1ZtCuUsLXhILoQsg9uLzHwY1Q_xhc2-bPjqel0fn8JskoJ0jUbAsanzbvXsmFDufwervLbDvmXXwO1Am8Q3DGINoKo65gEUwlK6mUQMBPpeidsxcCY0mIY-4ykyJaUh7KlSbmPfcsQcfgJjpksYjhYt5kRCYWfLkPnPQQHEuGC9BhQ2C9V4OCgyKn5yTjwYitVX3tG4OD5XUxzgn00l15cBZ5GWsLrcpd55Y0CBgTBhP4OUa-Msq5x_nEF4_lkSnmBpd7o2vIdBpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LB6Z8t9BnZ5KNYdlJY_3TfKQOvoN0qZlSvtbrUw5FvJyAOwIVsafpdNDaUvAwU3cwdhTOd8MvjQ7qkiSeaYz9Y0WNS_7K7bNz0n5-IkSuvUIZ3E7BQ9-T1bmYUKYY5ua08lBZpsjO50YmdE_sQGsFl29HN9ubbNBBJ45aE8ZZYy_Gj_cwbmhtUIB-ARxXNlDX_wwqpN7KqIckeyIeg3VskP9YkNulPoL_wj1uKYC1rMmqVrnYUL6G79diRakj69xanGVbwVGSbUcyK9jlNvLEFoXJhd7MmMCjaZJWIU2KzjbQmzSo78gDAe04LJIvlOW4-_mcQlYCFB5tlHDdBQtBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rd5zgy8GcRqeX1Fvx28ALzBc6hF6aGMNOmfBVJ__SJczBy7-5Z9bfj_KTrf7D86F17vyH_p9Hi2S7Q8vHC1TkBfEwPSbnRvhe8MsQWs-dncaaR3ftQ1K0ikhE8aP9GsuWIPwCD0JNE5cSi-E22RS5ERA1gHZUF8KDUA63xmk6iuSRpezslomJvHoDgHuMBDR3nXM5NP46iCV5mT0inIYJOSZKNZ-K7Gl_--3uWJi23yVPqkREJPKytRPU9JNzP3sZNwbNTWj_An1FMHctFLFMA7acfmy1L9KWW_wZTMwWaQKozbspNCDChQrwMtKVC8TOj3i8h8Nz9_yKGmCokRMyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/daVwBQUAOeR4B4hS6caa1I6uc42qpaivi4UXhjJumNszwMRja6N_LFLPSEQTO6AOInRfHyhzQNbtVyTl00XSmKcT0dHVUwNoVtce-zvgih6Pruk6k4BaM1bhf2Y5QWU7jXoeBiyXWMTnY0gUk_sMSRH3oYlbso7n2cPpuHGhoBt8fsRD_8o7lMr7wrQqdOH5CK8mNJKIs1vTi8KQSj3xJ-RiV-cypH4yV8XFHi6WlOIUsNtMdIv3ZonmKneU8sW8v2DD5B89zQCx0QbfO7DXHMz1jUPhNxOL-mfYtjp6_CANCtcSl8LkAcDrpgRd3e_NeRok-rZ_erERXuVXWOBQyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p_v5Qe6EMzpenJz3bjYUHmiTrrrQ-v62cTUk3U04zm1cwump7I8uswaZ3KGRz017td8iZQ1eHnjG-9w5f9rb_HAx1gMynYYWt28aWwUmwADGCfzvrNq-LcPYQXx2mtg1eC2ERr1ddoHtnOWtVxMb6ZSdQ4qaES1ExKCjpN__p3230WSjKfxiA0dMSzFFyeA_5m37K6XV_UoU0j2PA0QDcBv1m467Eu9Z8vhiuhsfl9jDOYbDhGZ3XD8BXLuoALDN7gEJWR-uNIra3firUmgMtEzRBcf7qZj0e8uTPheMQvWa85yLqI4tRjsCEClq9uxc9IpPgZlXDhAOpP1jAzduUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MaW0TQeEsEuYpg4nBd1xz9Zjy6rmpFOvBGXCbAn31oebKApbs4m2QKcbBFmzjjpg0nvQ8X5yQc0Hid-amQstZxRi3Q4QBCNgi3rRbbROPC-kMnqfStMmzTlaCMi7VMvfCR-ZUaqtRxVuhsha-yg7_yLeFnX91cGPOZWeA8eDWUkOQB6isU6Vo6UeCmgSMuhvuBRaE4O5Yv6dxZ3MJp2PFktUIJqpiD18gK4ip8PUVDHULPqV-pU_rDj59zB2nXfekJwRAEXQmhqCUGGor6mUjvUExm2ZTWNbRQlTd0vKO47PBHO1NnHNxRT0q04120OhgAvyKZUAhL-CKM9QbMKRNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XfRe8qJEa4lP5HrUljYGq2aiIzGXOoGkueQfjeX14HzB9Jx2mQ6r-8N9eHs-3jk4MFTCHB9BThlA_oYt2Wm6F4hIjPE614iS5sv6JOED1uRoA6RsqM4HjOb8oXMJQVV1dCfRcGL3tQgkNp5qd152AVhxBDz0qBC0yVl4DSU8X_P1MhVG6fESEHRQTHu6gBUMYpsSyW-__RIHFZtj3mtUm_WSdZD-6OjWbc_Ud9O7qBVSk0Hbsm10u6wyn5U9RZSwVnd2sgNtj_HHlj8GS3ocWS-Zv0CFNkTUvXWu78IBKY5yqtLCYU4HGUfX7J8CKDr2TaFNKMPj0rDGcxNGTDnRDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بازدید مدیرعامل پرسپولیس از هلدینگ رسانه‌ای خبرفوری
🔹
پیمان حدادی مدیرعامل باشگاه پرسپولیس، عصر امروز با حضور در هلدینگ رسانه‌ای خبرفوری از بخش‌های مختلف این مجموعه بازدید کرد و با ابعاد گوناگون فعالیت‌ها، ساختار و سازوکار سیستم رسانه‌ای خبرفوری آشنا شد.
🔹
در این بازدید بر لزوم ایجاد همکارهای مشترک بین دو مجموعه خصوصا در بخش مسئولیت‌های اجتماعی تاکید شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/697519" target="_blank">📅 18:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697518">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
جبران خسارت‌های آثار تاریخی آسیب‌دیده در جنگ ۷.۵ همت هزینه می‌برد
علیرضا ایزدی، رئیس مرکز ثبت، حفظ و احیای میراث‌فرهنگی و طبیعی در
#گفتگو
با خبرفوری:
🔹
از مجموع ۱۴۹ اثر تاریخی آسیب‌دیده در جنگ رمضان، ۴۲ اثر تحت مالکیت وزارت میراث فرهنگی است که مرمت ۱۱ اثر به پایان رسیده و ۳۱ اثر دیگر در دست اقدام است.
🔹
برآورد جبران خسارت‌ها ۷.۵ همت است، اما تاکنون ۵۰ میلیارد ریال بابت پروژه‌های متعلق به وزارتخانه پرداخت شده است.
@TV_Fori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/697518" target="_blank">📅 18:10 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697516">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/822d3d5c4f.mp4?token=BUhK8p4YrbDchYOQs-zAcu71khxKD3mmbg2bWMyGIjyc6h8z8KDOPma_DHip58dAEzrFtX7dJfe3FGVLaiNQSj-614Mltlpsn_IfvatekSDOW2PFmNp5c3u4LnNuxa_Nu_VaAZDCPWlXCTleFg5LhV_ss5LQQWW8CSs0lifNJYvp3k9yDVSVg7odSYoHtdB8sYQ8qTm3jROli9CySRmRjP1GM__U1zY0mEfdY0wlhg5jJkuHJ-jK4Grp2xRieK5yJKaEXlbuhO2K_kpTmUctDHzSbSK7DWEokmOMtGSNQjzDOrSOvH57O9mEbVBXSDMLzpgk1JFw20llvpLErKFW9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/822d3d5c4f.mp4?token=BUhK8p4YrbDchYOQs-zAcu71khxKD3mmbg2bWMyGIjyc6h8z8KDOPma_DHip58dAEzrFtX7dJfe3FGVLaiNQSj-614Mltlpsn_IfvatekSDOW2PFmNp5c3u4LnNuxa_Nu_VaAZDCPWlXCTleFg5LhV_ss5LQQWW8CSs0lifNJYvp3k9yDVSVg7odSYoHtdB8sYQ8qTm3jROli9CySRmRjP1GM__U1zY0mEfdY0wlhg5jJkuHJ-jK4Grp2xRieK5yJKaEXlbuhO2K_kpTmUctDHzSbSK7DWEokmOMtGSNQjzDOrSOvH57O9mEbVBXSDMLzpgk1JFw20llvpLErKFW9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از خم شدن تا دست زدن، همه افعال حرکات بدن رو به انگلیسی یاد بگیر
#زبان_فوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/697516" target="_blank">📅 18:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697515">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vg-tvDcDuraliS7JamtbXj3ryT3w9dMnv9fd0rwDQWLMBYE9n26u4j8gRvlQ3JBYuDGTi1cXf8LbjVaJgzWv8LDMGtL6r3hudtYIGhxJ28bmIBdKgnwzvyqhx4b4xH2KSAKubdWaRTtGjvPegllD0ZnAuhwLqsbHltKLviidSiAFhziI8C3MR-DRbFCByBAf1-d66fdY7gQ1YBLm3tTRQAVlzvpjJtyuog5otuvaIbsMTULbP7fECQaCrtpyCY6235fsI2Y_2g1noGlrHtOkDybP0hflaP_4rPf7COgf6cS_1XurvCltaepkdx-ehI9Wyzi1ZPPVELg_fEQHXbevzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎀
یه دختر قشنگ، یه پک خوشگل، یه عالمه ذوق و عشق!
💕
🌸
پک‌های دخترونه‌ی ارکیده شاپ
با رنگ‌های ناز و ملیح، آماده‌ان تا روز دختر رو برات خاص‌تر کنن!
🎁
😍
💗
با خرید پک های روز دختر هم تخفیف داری ،هم اشانتیون میگیری ، هم ارسال رایگان میشه برات
😍
🥳
✨
برای خودت یا دخترای دوست‌داشتنی زندگیت کدوم پک رو انتخاب می‌کنی؟
😍
🎁
https://t.me/Orkide2025
https://t.me/Orkide2025</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/697515" target="_blank">📅 18:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697514">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rt6h0Jipv-sx8FPGU8Ii5QTsse_I3BFLZhMDSaNTVcr50Yg8vYEolfjVRwm43WaXvJ0Ze1_eKzhRK7Pm4Lr3iSOU6FT2sqabkqvTIxhYnBZSuVSnIqCJzRaJxWz8ZDxzf_23rabTWgt4-Ir8j99jN9CmIqrPTGb-B5pqe_Hq8iQX5P7laxYIzaetTJA_4rhknv75wBomMDpNh6tEJc6ZVt_PyX3J8gTd-ch6mBt6g2_UgHBOrglIgFs_fi8zRGjzcDqLbGh6tjZ1HbI5o6ooPLwLg5yuZ7Rl6UAiW-QhRxyqMNSo45YMuvF1mldiylvvgn9ae4Wb4vmKMnra6eXCLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ترامپ : از همین لحظه، در جنگ میان روسیه و اوکراین آتش‌بس در حوزه انرژی برقرار می‌شود؛ هر ۲ طرف توافق کرده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/697514" target="_blank">📅 17:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697513">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zy8o5bHNUKJIYucRsfc0t9F0U303fjIB8YpzeRgtAequrE8F0zwFMz4umVxMqCt0BOg-QL7y0aei0GdNxHDsOMsnnAcGQImnycMkSTj7tnymi-RrfvEuaV1YLvdvoWfUo5yhC6ok9r9zdbcDw8Fqpg6ielaN9FMD1R0zBDcR10iE-a0kBUCGxzWn_Eud2ZeD_uJH_8cxz14kNtKJXw8OyFwmoeOALovpqyFlBruh1IpLCqVq1Ue4dcMkh5oAxUdYUTVInLwp7Z0mPzOITRsWH6jttp80S2ujXV2A-XyFwkhUwdOmlYOuy-jAiTd6257eg6Y83y9D6yk3YE2LtaKwDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بنیامین نتانیاهو:من به شدت حمله تروریستی وحشتناک به فرودگاه بین‌المللی خالد پادشاه در ریاض، عربستان سعودی را که جان ۱۲ نفر بی‌گناه را گرفت و باعث زخمی شدن صدها نفر دیگر شد محکوم می‌کنم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/697513" target="_blank">📅 17:44 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697510">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
دبیر شورای‌عالی امنیت ملی: عاقبت قدرت‌هایی بزرگ‌تر از آمریکا که تلاش کرده‌اند ایران را فتح کنند، زباله‌دان تاریخ بوده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/697510" target="_blank">📅 17:35 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697508">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f14ba63f5.mp4?token=R3xJm5KWKF-6KECJqfk7HJb8NNd-Jivz9QvXq5aSpYGBcwMycE3izWf27wluvn3_96ZyZRLHy9g1GKe7yvKdhl0siy3wF0Z4271tRmfbZCWJlZiqjMzzLBQbD2thEVXZdjrwZRdF9gv-oNnGsSoKyyr-J40tmSv9k9Mt3dkAzq-dW-bsGx4053q39pG3mbCDBSqUNz_zeN6flMAiQi0Fsic7AtB9zsRBupQloDD29IjdqAxw0zODnM39okyyggRkLUO063l2XsIbUdNBPCJTQmKRwR2mg8L6GWiVtH-M6kC9dz82GZVl41lGlnjzJgT1pyYEGCvegkayM5gJPSvkdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f14ba63f5.mp4?token=R3xJm5KWKF-6KECJqfk7HJb8NNd-Jivz9QvXq5aSpYGBcwMycE3izWf27wluvn3_96ZyZRLHy9g1GKe7yvKdhl0siy3wF0Z4271tRmfbZCWJlZiqjMzzLBQbD2thEVXZdjrwZRdF9gv-oNnGsSoKyyr-J40tmSv9k9Mt3dkAzq-dW-bsGx4053q39pG3mbCDBSqUNz_zeN6flMAiQi0Fsic7AtB9zsRBupQloDD29IjdqAxw0zODnM39okyyggRkLUO063l2XsIbUdNBPCJTQmKRwR2mg8L6GWiVtH-M6kC9dz82GZVl41lGlnjzJgT1pyYEGCvegkayM5gJPSvkdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای
وزیر خزانه‌داری آمریکا: اگر این ایرانی‌ها کشورشان را دوست دارند، تبریک می‌گویم، شما باید آنجا بمانید
🔹
آنها نمی‌توانند اقوامشان را در لندن ببینند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/697508" target="_blank">📅 17:31 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697507">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZT87MXVxA_Fc52SDxjNOs1Fo69GuuJaUvNnaQeRgdNqhwOFa2PGdZYcmlmqEOAk6QuaQIii8xK9VaRxS6ySVDG4vVDT-iOx5IDF7rfq6Bq770tZ_o2t5PFZK61Yt-dHxTk7LNZeYdKKOpTnwEUePp8fBTiqMUFRVygo3b8F1gm1o8JJlbusefeUcb0KVyUdG2k32upz1qHMZ7yxblcPlJAldDk1F9eBAXFYWZDuMXelNFg0mStcOY7Jts_mTUIEC7wIrmc7d91CmWsr-tUMbuX2zXUHYuNIp6vt-nb2cqotD-TXDa3vbKeWlgYwus1BNcsFQgw9x1j6nOap_Boxnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعداد موزه‌های ایران به هزار می‌رسد
🔸
بر اساس اعلام معاون وزیر میراث فرهنگی، در حال حاضر ۸۳۳ موزه در سراسر کشور وجود دارد.
🔸
برای تحقق هدف برنامه هفتم توسعه، نیاز است تا پایان این برنامه ۱۶۷ موزه جدید به ظرفیت کشور اضافه شود و تعداد موزه‌ها به ۱۰۰۰ مورد برسد.
@amarfact</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/697507" target="_blank">📅 17:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697506">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
دبیر شورای‌عالی امنیت ملی: عاقبت قدرت‌هایی بزرگ‌تر از آمریکا که تلاش کرده‌اند ایران را فتح کنند، زباله‌دان تاریخ بوده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/697506" target="_blank">📅 17:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697505">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaac3fd9dd.mp4?token=Uwt2Qj3Rq_zYjU6SpqZYUKIGC9I1yMUCjnzoH_PnoLa0nGuLm66uAVLdw1taiwquEvRskVo73wWdBhu5c9FP8_WVX_VAEMNiJsR4IQ-Z1HC3rz4fGP144DhHy86tFEq7--ZN7Rc6-yq2P1jWgC1LbFY4Y_IY06HqVf1DNdETE3v-6vg2XkGTp7lzusepnKg5MS04RaDsloCODGpBTvrBsKJASUhfb5SyWPy0BI3tzP6kswFav4ov5qElnIfz0nGgrPW9xGibhqDr7GMoZDwEylMsVWTYKNXlcBhHkvUq-HHnyYKtfLxuj4zNH2whkedyo9qCB9n3v0U3v7r9allIow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaac3fd9dd.mp4?token=Uwt2Qj3Rq_zYjU6SpqZYUKIGC9I1yMUCjnzoH_PnoLa0nGuLm66uAVLdw1taiwquEvRskVo73wWdBhu5c9FP8_WVX_VAEMNiJsR4IQ-Z1HC3rz4fGP144DhHy86tFEq7--ZN7Rc6-yq2P1jWgC1LbFY4Y_IY06HqVf1DNdETE3v-6vg2XkGTp7lzusepnKg5MS04RaDsloCODGpBTvrBsKJASUhfb5SyWPy0BI3tzP6kswFav4ov5qElnIfz0nGgrPW9xGibhqDr7GMoZDwEylMsVWTYKNXlcBhHkvUq-HHnyYKtfLxuj4zNH2whkedyo9qCB9n3v0U3v7r9allIow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای بسنت: ایران در حال حاضر هیچ درصدی از نفت خود را در حال حمل‌و‌نقل دریایی ندارد. آنها با کسری بودجه مواجه هستند
🔹
ترامپ انتظار ندارد تا حداقل بعد از انتخابات میان‌دوره‌ای، شاهد درگیری‌های نظامی جدی باشیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/697505" target="_blank">📅 17:22 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697504">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
اذعان وزیر خزانه‌داری آمریکا به موفقیت ایران در تنبیه کشتی‌های متخلف در تنگه هرمز
وزیر خزانه‌داری آمریکا:
🔹
ایران هر شب پهپاد پرتاب می‌کند اما توانایی‌های رصد خود را از دست داده و پهپادهایش به برخی کشتی‌ها اصابت می‌کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/697504" target="_blank">📅 17:20 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697503">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
وزیر آموزش‌وپرورش: الزام دانش‌آموزان به حضور در کلاس درس با پلاک، دروغ‌پردازی رسانه‌ای است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/697503" target="_blank">📅 17:19 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697501">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39237cc31f.mp4?token=tLm5leFEWm9BoU0ixr36ShQNhOuskeWBipqaJnBdzsFSQd6zQU8L_3DL1OnjVLLwqQYxBxh1CbkVdDs3GNbS2TEu8BCH3ybtFx_iiXco4n3Zah7caw5rO0O5iQ0OZm6ttZlpR9UeIa6f_wxGqtD2wuJvIB7PRBrDgw-5d6dAOH0k4hV9ZX3LW_dTeZlAUH-f7S6eOxxJPR-MJeUIjIvjAzitmSp-ZSY1WQ4uiPyljaaR5QBpmi0em4FecXlyZjjylvV9PDgr7LFpO2VRqZHXR6-ufAyY0lSa60Xzjx2UL3AMDWWOHzdNn_waytjM1ckKXwxidXC08la2Reo6zBn1Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39237cc31f.mp4?token=tLm5leFEWm9BoU0ixr36ShQNhOuskeWBipqaJnBdzsFSQd6zQU8L_3DL1OnjVLLwqQYxBxh1CbkVdDs3GNbS2TEu8BCH3ybtFx_iiXco4n3Zah7caw5rO0O5iQ0OZm6ttZlpR9UeIa6f_wxGqtD2wuJvIB7PRBrDgw-5d6dAOH0k4hV9ZX3LW_dTeZlAUH-f7S6eOxxJPR-MJeUIjIvjAzitmSp-ZSY1WQ4uiPyljaaR5QBpmi0em4FecXlyZjjylvV9PDgr7LFpO2VRqZHXR6-ufAyY0lSa60Xzjx2UL3AMDWWOHzdNn_waytjM1ckKXwxidXC08la2Reo6zBn1Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سازمان عملیات تجارت دریایی بریتانیا: یک نفتکش هنگام خروج از تنگه هرمز، از سمت چپ کشتی هدف اصابت یک پرتابه قرار گرفته و آسیب دیده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/697501" target="_blank">📅 17:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697500">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
دلالی با کارت آزاد بنزین | چرا رانندگان برای سوخت‌گیری باید پول اضافه بدهند؟
🔹
در برخی جایگاه‌های سوخت، دریافت بنزین آزاد برای رانندگانی که کارت سوخت شخصی همراه ندارند یا سهمیه‌شان تمام شده، به تجربه‌ای پرتنش تبدیل شده است؛ تجربه‌ای که گاهی با بهانه‌جویی، انتظار طولانی و مطالبه مبالغی خارج از نرخ رسمی همراه می‌شود.
بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3251584</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/697500" target="_blank">📅 17:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697499">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57ec39cb19.mp4?token=a6hodUX-8m922GRZO3fyxH5AHFtmmPrZF5Hd4dOBYQrBv-u3pPjvb2onsr527FJMtusNa7ExvIAbW52xveeDRdDa3RUEhOZhs3CCMbbDG9dYZeHbNTzjUhvU_ljgE8U80JwpZMK_-TeyZnkdwL7NScttCXs20enP6qPFDWRdRgtIouOuLGyi1UrYL_iX_t_56BHEjHmXdmWDCyv7eCgjDjPKNowNvcy-kEjamzixjqQDKj2h25Sxa9n52dB9IRYL_m92kO4SRSs1ijtjXJzCgKXPxkqh9wAvxhgL5EzOx0xwxzIsNGwU-vyzgqtjcjTNE8jmIrkvqAkoFSHenefbBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57ec39cb19.mp4?token=a6hodUX-8m922GRZO3fyxH5AHFtmmPrZF5Hd4dOBYQrBv-u3pPjvb2onsr527FJMtusNa7ExvIAbW52xveeDRdDa3RUEhOZhs3CCMbbDG9dYZeHbNTzjUhvU_ljgE8U80JwpZMK_-TeyZnkdwL7NScttCXs20enP6qPFDWRdRgtIouOuLGyi1UrYL_iX_t_56BHEjHmXdmWDCyv7eCgjDjPKNowNvcy-kEjamzixjqQDKj2h25Sxa9n52dB9IRYL_m92kO4SRSs1ijtjXJzCgKXPxkqh9wAvxhgL5EzOx0xwxzIsNGwU-vyzgqtjcjTNE8jmIrkvqAkoFSHenefbBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تا حالا کاهو رو این‌طوری خرد کرده بودی؟
🥬
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/697499" target="_blank">📅 17:02 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697498">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7f3ca69e6.mp4?token=NvWXekl4ncqkN6D9eu8bmrNLyAwaiDsFVV9lEnkgCyYKoUCH2T5P392uM8niUfcHYXYMsAI6a37J5GB82vbV6vrKUYZ_kZFvDadw7h3iub1PqO5ZcOLYQSgkdrbJjEE4vJK1V7qvaoeeFKU43j__JK3TS07T_yWD1mB34lvBHZHcezxnEFrxwt2Glb0WmPLo_jsC3v2i_fML4XRy_aTsJBaqVM3AYK9P4UwONcQHpfpWErDNozXpME_Xx5Jy7KQYDlECrbTWMpgJRzyCpapOIaPW7IMDEy5qL-dzOEbfc9p7KPynAe3_pPiTqn1tz5SxicJD5droYEkhqvoEUBdNcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7f3ca69e6.mp4?token=NvWXekl4ncqkN6D9eu8bmrNLyAwaiDsFVV9lEnkgCyYKoUCH2T5P392uM8niUfcHYXYMsAI6a37J5GB82vbV6vrKUYZ_kZFvDadw7h3iub1PqO5ZcOLYQSgkdrbJjEE4vJK1V7qvaoeeFKU43j__JK3TS07T_yWD1mB34lvBHZHcezxnEFrxwt2Glb0WmPLo_jsC3v2i_fML4XRy_aTsJBaqVM3AYK9P4UwONcQHpfpWErDNozXpME_Xx5Jy7KQYDlECrbTWMpgJRzyCpapOIaPW7IMDEy5qL-dzOEbfc9p7KPynAe3_pPiTqn1tz5SxicJD5droYEkhqvoEUBdNcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراضات در فرانسه با حضور گسترده پرچم‌ها در حمایت از فلسطین
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/697498" target="_blank">📅 16:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697497">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
«روایت امروز از هنر ساختن فردا»؛ نگاه اسنوا به آینده زندگی ایرانی
🔹
دکتر میلاد کوچکیان، مدیر برند اسنوا، در گفت‌وگو با خبرفوری در نمایشگاه لوازم خانگی، از رویکرد جدید این برند در طراحی و عرضه محصولات متناسب با سبک زندگی خانواده‌های ایرانی گفت.
🔹
اسنوا با معرفی سه سری محصول «اوان»، «بوم» و «هوم»، تلاش کرده است نیازهای گروه‌های مختلف مصرف‌کنندگان را پوشش دهد؛ از زوج‌های جوانی که زندگی مشترک خود را آغاز کرده‌اند تا خانواده‌هایی که به‌دنبال محصولات با امکانات و فناوری‌های پیشرفته‌تر هستند.
🔹
هدف این رویکرد، ساده‌تر کردن انتخاب برای مصرف‌کننده ایرانی و حرکت از فروش صرف محصول به سمت ارائه راهکارهای زندگی است. مدیریت و بهره‌وری انرژی نیز از دیگر محورهای مورد توجه این برند در توسعه محصولات به شمار می‌رود.
🔗
مشروح خبر
khabarfoori.com/fa/tiny/news-3251632
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/697497" target="_blank">📅 16:56 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697496">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
حمله موشکی یمن به تأسیسات نفتی و نظامی جده، حریم هوایی را مختل کرد و پروازها در فرودگاه‌های جده و الدمام متوقف شد
/ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/697496" target="_blank">📅 16:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697495">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4746484ff5.mp4?token=qATEcP2neHqEBzXgEuZ1xktTO6ZjqdDkeulf8i9j0DiKwV7CjEGPcznUd9g_vanlVRuzBPCD9MlJqc3wYbojleF0gSyD5j7zhawYKLxAJ7gpaQoZUvnrIXtI8lD4AiOEbw5avzLAyfCwVDEXxz2UrvcEDv8Lmh7heqYhviHEil40X1MrIf6eERf968CP5lJSUP78C2Z3O3NjiokpGM0EBSpqQ4OT_F01THvlwPfve0L2ceNvUHjymUDCZ3hZLGKoYcEfoBYZiyvGLiTzvapUTuWvr9KstrWiuOJoarDhu4Zkpa41sM9gDbCWbn9sJP1781N9mtIp3j_YDt18CMBeyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4746484ff5.mp4?token=qATEcP2neHqEBzXgEuZ1xktTO6ZjqdDkeulf8i9j0DiKwV7CjEGPcznUd9g_vanlVRuzBPCD9MlJqc3wYbojleF0gSyD5j7zhawYKLxAJ7gpaQoZUvnrIXtI8lD4AiOEbw5avzLAyfCwVDEXxz2UrvcEDv8Lmh7heqYhviHEil40X1MrIf6eERf968CP5lJSUP78C2Z3O3NjiokpGM0EBSpqQ4OT_F01THvlwPfve0L2ceNvUHjymUDCZ3hZLGKoYcEfoBYZiyvGLiTzvapUTuWvr9KstrWiuOJoarDhu4Zkpa41sM9gDbCWbn9sJP1781N9mtIp3j_YDt18CMBeyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلمی که به تازگی از حمله به یک شهرک در افسریه تهران طی جنگ ۴۰ روزه منتشر شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/697495" target="_blank">📅 16:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697494">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4auLfVKrZcWBi0p4JAO_K7vXd-qYfJ4yNQenGgYRDkfZTsagHyd4jL06u53vpKFdTQ4xhkhzyV0E8m1nByy1Jbdax1Avrm62mhcRAnlBchJ9tPkfEe4F114tEjoN0JZzvZX6Uttn2Udbwu5vty5FhBJnVPoDD6ohEq3uzZr7B5iWT7RvlLjFth8nfOUVViulMc4KedojlrzrEskXMbXux_CAm4QJYm_HS-xfzM-FhNd1KnducjvYK4jyf0VMdnTD3_zxcr2uuOc1VJzp4WF0s4yr7t-r-lIEVUi6GZC9eIERYZJajX9cM5cESEGWJ2LjltyeUk_3MHEYTuEuWERAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سازمان عملیات تجارت دریایی بریتانیا: یک نفتکش هنگام خروج از تنگه هرمز، از سمت چپ کشتی هدف اصابت یک پرتابه قرار گرفته و آسیب دیده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/697494" target="_blank">📅 16:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697493">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42feee0627.mp4?token=mfudG6wiahNSoLDuG5MZezfZyUMHR_4772Tx4FatdnNVABzo3YKLz6ydtEMJQYO2DsB_SHiYPYxNUp7f7TOEzdV9RCpgGNNyoILQKB9zfOXNFAHKGfw41pGfNZMTW2Q9I3YQn6bLJWL5-fL7tCsvH6LxC8ejGaf7RxgblBTq3Y1YTSuRNcrkZ0t9RcVN3gYIzS3Ax_rq9DBpwuBtGjzAqSfNlvVc1eymx31Hg1JsVaMvuxdShgVSck_zjeyDE9vsgLsH1r3cgePa3VJvJ8wGJM6mys5P2Ho7bwq3MXuXTRJpLrKNFaK20flt8Ep_-XzxQKrYJcH0bYKdKglbfrd-5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42feee0627.mp4?token=mfudG6wiahNSoLDuG5MZezfZyUMHR_4772Tx4FatdnNVABzo3YKLz6ydtEMJQYO2DsB_SHiYPYxNUp7f7TOEzdV9RCpgGNNyoILQKB9zfOXNFAHKGfw41pGfNZMTW2Q9I3YQn6bLJWL5-fL7tCsvH6LxC8ejGaf7RxgblBTq3Y1YTSuRNcrkZ0t9RcVN3gYIzS3Ax_rq9DBpwuBtGjzAqSfNlvVc1eymx31Hg1JsVaMvuxdShgVSck_zjeyDE9vsgLsH1r3cgePa3VJvJ8wGJM6mys5P2Ho7bwq3MXuXTRJpLrKNFaK20flt8Ep_-XzxQKrYJcH0bYKdKglbfrd-5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسام‌الدین آشنا: راننده تاکسی بازنشسته سپاه بهم گفت شما اینقدر نامردید و لج منو در اوردید، که از لج شما می‌گویم رضا پهلوی تا بسوزید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/697493" target="_blank">📅 16:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697492">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
فارس: با پایان دو هفته، وعده بسنت درباره فروپاشی اقتصاد ایران محقق نشد و دلار از ۲۷۲ هزارتومان به ۲۶۵ هزارتومان رسیده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/697492" target="_blank">📅 16:42 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697491">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
خبرنگار جنجالی آکسیوس، افسر واحد ۸۲۰۰ ارتش اسرائیل از آب درآمد
تسنیم:
🔹
باراک راوید بیش از آنکه خبرنگار باشد، افسر واحد ۸۲۰۰ ارتش اسرائیل است و شاید این قلب فهم ماجراست! نیوز وان (news۱) از رسانه‌های اسرائیلی چند سال پیش درباره او نوشته است که راوید پیشتر درجه‌دار واحد ۸۲۰۰ ارتش اسرائیل بوده و با درجه سروان از آن {در ظاهر} خارج شده است!
🔹
مجله Vanity Fair آمریکایی نیز درباره راوید به صراحت به سابقه او در اطلاعات نظامی اسرائیل اشاره و حضور او در واحد ۸۲۰۰ ارتش را تایید می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/697491" target="_blank">📅 16:39 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697490">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦
می‌دونستین این خطوط زمینی در ایستگاه‌های مترو چه جوری طراحی شده؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/697490" target="_blank">📅 16:37 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697489">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1_WSJ_oa0vxsYiH_pVNOCnvV4Iz63JtVZFJyGJVNlML1p_BqK-EM6RcoAi4ezVzTKoc9MG24IzTeCKPssykBkBQcprDKvTar5XDY6f1MgyOAa8rbIKJf-DsNJnR5Z1TgRKOht3_1HuXYKaKQR6HlFzw4iBMkuxGtdb9DFd4Aog8TtXdTiDNl16ZrcDJVJJyetdf03rxctfr0cQWA7e4Hae3poy73Pc9JZdYopVSzGf4lEWpv3P1qtBlg5NNi7DSZRQnGa_cBZ6hwTsCo7PIptimF89JOsuWqIGz-oEfcyT8kfRu1HjzkitCFRShsluysgyCKzpu082pNcpMmyRRew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۰ نقطه راهبردی در کنترل انصارالله یمن
🔹
در سپتامبر ۲۰۲۶ مجموعاً ۱۰ نقطه راهبردی شامل ۵ پایگاه، ۳ فرودگاه، یک بندر و ۲ جزیره در غرب یمن در کنترل انصارالله قرار گرفته‌اند.
🔹
در میان این نقاط، فرودگاه المخا، فرودگاه بنی‌الحکم، بندر المخا و جزیره میون به‌دلیل نزدیکی به باب‌المندب و مسیر کشتیرانی دریای سرخ از اهمیت جغرافیایی بالاتری برخوردارند.
🔹
همچنین جزیره میون با باند هوایی حدود ۱.۸۵ کیلومتر و جزیره زُقَر با باندی نزدیک به ۲ کیلومتر، از مهم‌ترین نقاط جزیره‌ای این فهرست هستند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/697489" target="_blank">📅 16:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697488">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">جامعۀ مهدوی/ج۲</div>
  <div class="tg-doc-extra">استاد علیرضا پناهیان</div>
</div>
<a href="https://t.me/akhbarefori/697488" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
جامعۀ مهدوی/ جلسۀ دوم
🔹
سخنران: پناهیان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/697488" target="_blank">📅 16:32 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697487">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac7a0589fd.mp4?token=sn5lRCzeX-5t_hAWb7ABnS2CG8O00L8H55Ob6p-BGXZfP5KizsXo0L2Zk2dtWXQkq2XlLBSrDjaB92Q6ukwst0EyATrsvdEA-pouu_qMJCkPLmnCZpBqSYad4PsPmpS6VRZDwYWRWf41JhRupBYXrw-eJ7-LdEtMkeb5BYO516ZMjAPEpKCLmVgUadaaxxlz7TZDkwbFKg_SOWEuHmQ6FVzmqScZ0lM-xO33vXyuFytU9m2X06FizfLdJh0ibbIGoCKqoS2m9Yy3OFWbu0YHrXGQE0IP11zyTjFdFwKVg4fQWawwLMwYADXpT-xJjSMiLkeh8l4qw1wnDCUzyJ66TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac7a0589fd.mp4?token=sn5lRCzeX-5t_hAWb7ABnS2CG8O00L8H55Ob6p-BGXZfP5KizsXo0L2Zk2dtWXQkq2XlLBSrDjaB92Q6ukwst0EyATrsvdEA-pouu_qMJCkPLmnCZpBqSYad4PsPmpS6VRZDwYWRWf41JhRupBYXrw-eJ7-LdEtMkeb5BYO516ZMjAPEpKCLmVgUadaaxxlz7TZDkwbFKg_SOWEuHmQ6FVzmqScZ0lM-xO33vXyuFytU9m2X06FizfLdJh0ibbIGoCKqoS2m9Yy3OFWbu0YHrXGQE0IP11zyTjFdFwKVg4fQWawwLMwYADXpT-xJjSMiLkeh8l4qw1wnDCUzyJ66TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موزه‌ای شگفت‌انگیز در اعماق آب‌های قبرس!
🌊
🗿
🔹
این موزه زیرآبی در سال ۲۰۲۱ با نصب حدود ۹۳ مجسمه انسان و درخت در عمق ۸ تا ۱۰ متری دریا ساخته شد تا به‌مرور به زیستگاهی برای آبزیان و صخره‌ای زنده تبدیل شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/697487" target="_blank">📅 16:23 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697485">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab408a0297.mp4?token=Od4vxha7U-QVtdJbGAhv35Pzg-uzc58qF9kq3ZQmK0mfTVubik3ZahAkVOGv1L_q5Tr3z23q1R3Sj7uIQYXwE-KqIh0MlIOTtDundgYclwNZb43SHYiXPbfBJWyjGbE__jCuH_2SShT9R4b7gbvQ0rGdttCk70GLDH8NAAQUIhVGTd1-BsjQt_t2in6962hY9ffD6UdiUAhasHscTfy8j55v698S2aHS-2CfXJhHIbpjCeJbYY0jRxJrZ-BvmUAxy1o2dAEdbqv0YZrtpKgHv3EyQOn_dLhnbxldQ8-54QgSjNrBsHeCZeMM7FwHUoLNxJ6DLJQeeH6sXFFTLJKEroWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab408a0297.mp4?token=Od4vxha7U-QVtdJbGAhv35Pzg-uzc58qF9kq3ZQmK0mfTVubik3ZahAkVOGv1L_q5Tr3z23q1R3Sj7uIQYXwE-KqIh0MlIOTtDundgYclwNZb43SHYiXPbfBJWyjGbE__jCuH_2SShT9R4b7gbvQ0rGdttCk70GLDH8NAAQUIhVGTd1-BsjQt_t2in6962hY9ffD6UdiUAhasHscTfy8j55v698S2aHS-2CfXJhHIbpjCeJbYY0jRxJrZ-BvmUAxy1o2dAEdbqv0YZrtpKgHv3EyQOn_dLhnbxldQ8-54QgSjNrBsHeCZeMM7FwHUoLNxJ6DLJQeeH6sXFFTLJKEroWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نگاهی به آخرین وضعیت دموکرات‌ها و جمهوری‌خواهان در انتخابات آمریکا
اکبر مختاری، کارشناس مسائل آمریکا:
🔹
نظرسنجی‌ها نشان می‌دهد که دموکرات‌ها در انتخابات میان‌دوره‌ای آمریکا، شانس بسیار بالایی برای کسب اکثریت در مجلس نمایندگان دارند. اما در سنا، رقابت بسیار نزدیک‌تر و پیچیده‌تر از این حرف‌هاست./ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/697485" target="_blank">📅 16:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697483">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
گزافه‌گویی نخست‌وزیر پیشین قطر: ایران دشمن اصلی ماست اما این به معنای کنار گذاشتن روابط شفاف با آن نیست
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/697483" target="_blank">📅 16:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697482">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سکوت سنگین در صحنه جرم؛ روایت میدانی از قتل پاساژ سعدی
🔹
روایت خبرفوری از صحنه‌ی جرم و آخرین شنیده‌ها از زبان شاهدان عینی  درباره قتل پاساژ سعدی را در این ویدیو ببینید
@TV_Fori</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/697482" target="_blank">📅 16:09 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697480">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iEa-dmneug3sdAosCW0u1PWkhLmUkxiRgDuNtkyvF92dKN0h6Fw_eJe-Dn2mqNMh62JkSab_OfvdrIBpSZTmJyOiqIZGxvuNl00s9Yyoh7btcpyB1rNOXdrusvzSWXzhomsVKLjJqj38EYjTQbBRUIPAPVaRaYesWB2Q8NO7htZmmCAORM2toAH7TOPIZz66Z-58hIzR6GjPyLtKmoeFivY4qcyxcutrZDrN4H75kR9JDpm1VXsgBBATUAYBrfDXWPDHMT06cJVgSrh-nG9t7QnHUmTQ8z23YRGp3toYeKMlIiJydyiePWTgFsSh-3WFVwcNwzLBhZTmodnw0x615Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مفسر سیاسی آمریکایی:
آمریکا در جنگ با ایران است.
روسیه از ایران حمایت می‌کند.
آمریکا نفت از روسیه می‌خرد.
آمریکا در حال تأمین مالی جنگی علیه خودش است. قضیه هر بار فقط احمقانه‌تر و احمقانه‌تر می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/697480" target="_blank">📅 16:02 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697479">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
ادعای ترامپ: من معتقدم ایران مسئول حادثه هواپیمای فلای‌دبی است
🔹
ترامپ: عقب‌نشینی بمب‌افکن‌های آمریکایی از بریتانیا، در پی یک تهدید صورت گرفت و ما می‌دانیم چه کسی پشت این تهدید قرار دارد #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/697479" target="_blank">📅 15:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697478">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f84dd6e8d.mp4?token=BnD-c2ab_b8R4iyid7colW8sFLLsBox5ZmlWH63QAnYlZlAcqLyb2o2I0LWATAVbAwHyynz7L7X5gFvMVfkh1vB2Wi-dwlE8Jl3GYcQCiLmUoEAnqWbh8mWiphGR-s4HsBdRENFVvK6RekwHwfdW4yCEDr7aVn9sW4P-dfSnuUPLiNT1hu5zzRjcEQ_ZJGekwElHfMcWNUyGBSjB2LRnmnIJtUBtj2yFSa5Pn3CITW-c-AI6K4RkuQd5hg37x6VCxRYIoz7MPtPxwp5vOzb0BwFPmVr8MVhYrryxuzDs00uZrO7QQvbKDCqAF41G2QWdb1ze1vonnzWc4Ahz3JvQmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f84dd6e8d.mp4?token=BnD-c2ab_b8R4iyid7colW8sFLLsBox5ZmlWH63QAnYlZlAcqLyb2o2I0LWATAVbAwHyynz7L7X5gFvMVfkh1vB2Wi-dwlE8Jl3GYcQCiLmUoEAnqWbh8mWiphGR-s4HsBdRENFVvK6RekwHwfdW4yCEDr7aVn9sW4P-dfSnuUPLiNT1hu5zzRjcEQ_ZJGekwElHfMcWNUyGBSjB2LRnmnIJtUBtj2yFSa5Pn3CITW-c-AI6K4RkuQd5hg37x6VCxRYIoz7MPtPxwp5vOzb0BwFPmVr8MVhYrryxuzDs00uZrO7QQvbKDCqAF41G2QWdb1ze1vonnzWc4Ahz3JvQmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تلاش یک روس، برای سرنگون کردن پهپاد انتحاری اوکراینی با استفاده از یک نصف آجر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/697478" target="_blank">📅 15:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697475">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ieG3G1nY95_gN9OOnH_t7OnLc0LriwAaW14Ht77kb6xeUEQQEM3fER8bV_bl2dkMXhMgrcf-yE43tk2e0OlOwY5TxxUP2kxgPcuQLzbKz3FM6z1DgT2DbSlA7DPJcfIH-3vWWmyziNrnFl10-tPVcpG9k6KDogVZZWkbn8Zz7R_9ldNJvs5C042X3JUAN5MSctPBkWqiQdFpqo6j3jsCTOJ4VFOo4G4iEOcQ7hvULdE_5xPXTFrkVkx4skFw6FLuTIXfJTK6Qge9v5-FTYb-CqqNPTLOeeglSBHOH6LLpPdklRDTSiKDjwjYwOMvn9rslWZMmz7s-IWss-dlkM-Gbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BuysPgxMRSEKoMvLe_LRXhSX6QCyzUvYxFwX51LuAHymhK28sRtAUE93Fw6svGX6ykbmmrhXrY2NmahVYerG_Gp_MHy0wwAZFNkmdXHUwLxpkTsNULGZHfvZ-_yCBQJisIgKbkoBYaIYG_-6UL0714p9KtULZO_krrZy8GYnZkAAaYMMJSnw3IHkAngmJ0wDMreChkdBVkLzf1OH76whj84TaBJFt8tV3GCmvWKavjkYnpGfI2zbFr32C6tKFYfMTyGlwEkEXitb-XW8pSX_mk32D3ZYpHp3zG-mM9LT2_dYYawB4qZEucIaRtAsn0WlAnaer8kIhnLYoSHekHZklQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o0BIi6svlZ4nlsrDKi53jZ9v72NMK38p9TWzApmaPAR2o7RUu-TcuTXPQ_IWY_X39DcV98amLbAZTjvheRUvNrqkWyfPsoPMb6sGSl-CU8S06yH-LmBZTk34_zElM-looE3VN5oAW_lSlQGVApkZ_cmojkt3KmUGa7b8iwUo3e_iLrI7TLtKMloPseLhcHMQ0QEGyawu__LWf-Z-cVcL2o9FqxaahcIqD3QTj4LQ9_V-12bXPIp8Djz0SeAhXeL7ZkhDKKm8c-DeEquaQ9qosEYYDgxetM_YzW7Tkn4A5M6vfRkcTaeyuMUQDU8G7igJPg3PeLUmqOokakwsx2CXlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
این جلوه‌های رنگی فیلتر دیجیتال نیست؛ حاصل برخورد نور با بال‌های مرغ مگس‌خوار سیاه ژاکوبین است!
🦜
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/697475" target="_blank">📅 15:42 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697474">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQnFbceawf3FTSeRBm_qPqadEB0pvtyuDu1RYw-8QXFCLtfmFsVwAvEDbr7fXBEydZ_EGmMeJQ7FBgVYEG8Fb9ca-cSRepwmxJ_JPj3Y56EOtMHLqnQzd64znFVz36pjK1JAxNVO_SUiFFrqTM2COJds1gvt6-5CULFP5CD7RLDHNedzLfc9wc6F_DHopeeHk9OqEJjHYl6JSqz3y4trY_Hqp3_ZwRBVPAduhOkLHoJB81padHOU5lvy6Vst5fAiOnCEf59IX_GbQaqV0w5MAkRktJ-BZw2141W9afMOcNXHnaTpFT1uGWz2118WoJxBlpUdMtPW7g4PrwLwYkDfWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هیجانات بازار ارز چگونه فروکش کرد؟
🔹
از زمانی که
طرح عرضه دلار به «کد ملی»
در حاشیه قیمت بازار کلید خورد،
ترمز رشد پرشتاب قیمت ارز نیز کشیده شد.
این رویکرد بازی را در بازار تغییر و هیجان را کاهش داد.
🔹
در شرایط جنگ و محاصره،
آمریکا به‌دنبال القای خالی‌بودن دست سیاست‌گذار ارزی بود؛
تا جایی که معاون خزانه‌داری این کشور در مصاحبه با بی‌بی‌سی مدعی شد
فروش نفت و منابع مالی در دسترس ایران رو به پایان است و این فشارها ایران را به زانو در خواهد آورد.
🔹
در چنین فضایی، اقدام بانک مرکزی پاسخی صریح و مقتدرانه بود:
نشان دادن دست پر بانک مرکزی و مدیریت روانی بازار با عرضه گسترده.
در این میان، منتقدانی این اقدام را «اتلاف منابع» خواندند؛ اما در
اوج جنگ ادراکی و ناامنی روانی بازار،
انفعال به بهانه حفظ ذخایر، زمین بازی را دودستی تقدیم سفته‌بازان می‌کرد.
بانک مرکزی باید با اقتدار وارد میدان می‌شد تا انتظارات منفی را کنترل نماید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/697474" target="_blank">📅 15:40 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697472">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
پاسخ وزرات بهداشت به روانشناسی زرد/ اقدام به روان درمانی بدون تخصص کاملاً تخلف است
محمدرضا شالبافان، مدیر کل دفتر سلامت روانی، اجتماعی و اعتیاد وزارت بهداشت:
🔹
اینکه افراد مختلف اطلاع‌رسانی علمی کنند حتی اگر روانشناس یا روانپزشک نباشند، ارزشمند است و ایرادی ندارد، اما اگر افرادی تخصص مربوطه را ندارند و اقدام درمانی انجام بدهند؛ کاملا تخلف است.
🔹
افرادی که مداخلات روان درمانی انجام می‌دهند نیازمند یکسری اقدامات قانونی هستند که سازمان روانشناسی در این خصوص پیگیر است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/697472" target="_blank">📅 15:35 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697467">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BKiC-V7LCshxrjOCTdez1ixKEEOHlKF28kodCgr-iekRDRdD22dOczgqz0_Xag5oan1ooAYV0mYPZQRwcV0PsLGvx5TWy22LU0wEl41wZIIOcHd6yoMBvT91dHpXmLYENWrfj5YPi_8CNWGkLqV6VX5Bvm7Gf9Dwi2jHw6ixt8j5fS-FBIcgNYF6lBHL8bSzmEbiVNCcOLAdp6qo5GfLKwiwgH0G-Z2RrqKOCAsRJkEqoUulbqRxxfKAFbLN4c3kQ1gl2x_F4nCv2A3vaDq-01ePHfYTHXSd3ZPUE5TOyIic8C5kUCvG73IlAcohvDSZ5zN4oCHzIIz7W_InKeWZvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/snssFHzN_kpYn5XWBhHaQmPJTzfkhrnOxbCdmhyplPh0bP2J8gm00Gpg28Og7UmJxkji9QP5a2uGOXuq7Z_YyB0TjE3xvaBpnnj0xPZ7zmOVbuoeEurJXq5I4oro8uz-IHw3a1an029CAJsh8dra6KsHzVJNjPJdTxNZS8GYm2RgbFcpyGu6Hhcj6S8TmDGo-Gbs2DdsQUPUcVffsxq9d6S_IgwkS3GPRK_C7XvNfgRwlGCax1Ac-hUMiF92Mp4b_jui-dJqjteKmNvuzpO3IA44GXbiWuujsspAjO6vltZdwvxps0YRSr4b5x_3joT9IN0yLu4e7UI10N5GBILa1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HMb1ZFiVOn5qrloOSXPl2C3mmZFWE0cL4iyM-OaN8CigVvWmXCw7U2SgZRfRk9mLerUC9DiAMVynP0j5lnfBwgaIrM6YykpE_tiMHEVedof7OcJnTW31cA4-w3YQ306IxaGSr0fcanNnmQ4gwW3hSMOre-qdypQ06QPyg-M1MYVdT1clqQdWuYknsrQYAiaDo3BHBTSTeHQzVfbMOhf2MwgbGiyi9H6-11jitqWv7mY246jmWlqFxlk5p3Bsr1U2Aklgb6RkPrcSj3WbelzjfyZY1an9-2ULlk66GuBdIKH3LNsdhc5tvcPGgQXj1ZIzIUqRibNjtM9eUl9Oi2YU8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mK79585Y8hbFfqVdJcdAWfH4TJI-lcl_5VcnHy4WAZRKFsrNg69ZIDqDQl3gyMO9iECXuhWAh6jqOch8eyZPwXG-RMAwbgJZdpIrG76hYU2fDoxcFp-13zhvbGSjdTMXwxAf69eLlyuvX3twSRJYBGmmuror5LqlUI7aV0Rdo_FTIyFFcww0_nSajyUTj1xKyHZGya2AOQp5G51jUSVPn_093wd4SarY8taUVD_0pEbJfqCAPdTvQmVJNVH415S-ntO17tUTEMfj-kQzdx4GJUT2uQQnrvRZxmqSpGXkuS4clpXJPOq9NTrfjAhRlaTcGhIguAYKR-sXp1SJvn4vXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UIqHt14V_qmGOJaK_f2Y0C-7qr5i2J7Fn1xPH58RX_M48PNJro0Akd6xC681MHkuu_j5PVtj8IoJxGWHY9YiySVbufSve32AjaLkOUUFyVlvvAfGkL_UtL2vmwj5nMmXIsw6FMS4rto-fdp2n1CVkwrUjjp0UUn9BTw9Frdnd8njH2Cosrwy5oKVQIdEqeqm5ZfRlJzpcH0vX2hLTB_68ec5Jd5oMS4LmEA6O-cqDZVdcNiNaxmlbuRpiTCrWvOBymPSWoBk7GN2Huht3590p7bb1Ue3uHXwv8V9e8HTQ3FtugLoiwkSIoSifIie-W7EVcEfuXj7haaTwZbthnQICg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هر
قرص‌جوشان دقیقاً برای چی خوبه
؟
💊
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/697467" target="_blank">📅 15:27 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697466">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d0a45d897.mp4?token=fZ-XhvUT4I0h0PKmG_Gj5oZFErmoNv1Tf9zkfbteL6nBFSqTpdhhMmFfq5LqIorBCZwncD-07c6tFAjbF6q59-QZUNBdbrELf46OwCi8tnmbYzDESzBs2wWvVfprwnpMQk-UrNK0GFTU7sF5WzhaAMs1df-r7JawUeh0y6uWFQreBkO9fh8Wm9DMToWrxqOd1V0eoqT4Y7mK9bVkfMcS_vYFHr1Z6h39928IGcZcV18SllD09y9E6M8XhK81prpQN7YUyOvqw--N-YL1RiD8fRPE8j_PkFxbUHFcXo7VQud0WOgTaIL_R4WcbWLIlRDIU_D6oIrk6ke4P2BSc0WKAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d0a45d897.mp4?token=fZ-XhvUT4I0h0PKmG_Gj5oZFErmoNv1Tf9zkfbteL6nBFSqTpdhhMmFfq5LqIorBCZwncD-07c6tFAjbF6q59-QZUNBdbrELf46OwCi8tnmbYzDESzBs2wWvVfprwnpMQk-UrNK0GFTU7sF5WzhaAMs1df-r7JawUeh0y6uWFQreBkO9fh8Wm9DMToWrxqOd1V0eoqT4Y7mK9bVkfMcS_vYFHr1Z6h39928IGcZcV18SllD09y9E6M8XhK81prpQN7YUyOvqw--N-YL1RiD8fRPE8j_PkFxbUHFcXo7VQud0WOgTaIL_R4WcbWLIlRDIU_D6oIrk6ke4P2BSc0WKAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معارض سعودی: تعطیلی فرودگاه ریاض برای بن‌سلمان خطرناک‌تر از قطع نفت است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/697466" target="_blank">📅 15:19 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697465">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
هاآرتص: هزینه حمل‌ونقل یک نفتکش در حال حاضر از هزینه پرتاب یک موشک اسپیس‌ایکس هم بیشتر شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/697465" target="_blank">📅 15:17 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697464">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1LgnLZ4wOMi3kROuUOTM3t5i0EC1-Skfe-hgVpVGiO-BJtDx6IdcxAc9L-NL01jPrDyuJjFW18GtvyN7-XMdeKQ8j9nefcYIQAioHQN2iGCgstLb-6-JXN8JtcmFzM58qa5IY1lEMJ7lsydvQUNJJWmHIcHLJ6DFOwRzsi8Tgc4zrlgyk7r1J8LwyDNH8mSxByqjV2xHlj5SUnLSePzR74Ap3yVqpmA2PQguDSc7qOy6kewBGpAcb2j9C0MG5i9m1K6jW-uz0TQczt7x8ZMP79RW47CdOZW7VRcHBzLlW4p8yEA4Qkb1CO9371nBqKPpHS1ywm5od3jtxcmcgI_hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استیو هانکه: شرکت‌های هواپیمایی باید صورت‌حساب خسارت‌هایشان را برای ترامپ و نتانیاهو بفرستند و از آن‌ها غرامت بخواهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/697464" target="_blank">📅 15:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697463">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
عضو کمیسیون امنیت: ایران جنگید و شهید داد، نمی‌شود اختیار تنگه هرمز دست عمان باشد!
اسماعیل کوثری، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
آمریکا با فشار بر عمان به‌دنبال آن است که تمام مسیر عبور کشتی‌ها از تنگه هرمز در آب‌های سرزمینی این کشور قرار بگیرد، موضوعی که ایران با آن مخالف است.
🔹
آن‌ها ابتدا با عبور کشتی‌ها با هماهنگی نیروی دریایی سپاه موافقت کرده بودند، اما بعداً از موضع خود عقب‌نشینی کردند.
🔹
ایران واگذاری اختیار تردد به عمان را نمی‌پذیرد، چراکه جنگ را ما کردیم و شهدا را ما دادیم و نمی‌شود اختیار تنگه هرمز دست عمان باشد.
@TV_Fori</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/697463" target="_blank">📅 15:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697462">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxGCI6VWWftYpO60r3k99grY8S2FfWCGbdYdNUy9pzsxn1i9JJdVJwl0XK3E5oScbKFfWmfhXSBUrxOFTCaPRY9qCo4UwHnbp0UsXH4sGOv_DrHZoqCXdwmoBpxL_2snIXNAcNV8nJm1AmxzBN0UcQgDWHKaiwvJJemMoBgHhBz84T0yCqF80kFNFWegQC9h_fd-tcG-NjYJWuUhZ4G_qiG1z0rDRFh44CGrnXQaaBqhlRcrRJJm9iJ7bxwlmDlO__8QCTQdFLlYzqkmlJZX4U3fa8GN4j3qS6r6tnTkJBjbZDo4mR1J0wCPcDam9H45YNaWQyahozm5boZIvduBTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روزنامه نگار کانادایی: احساس می‌کنم که ترامپ بعد از شکست جمهوری‌خواهان در انتخابات میان‌دوره‌ای، جنگ جهانی سوم را آغاز خواهد کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/697462" target="_blank">📅 15:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697461">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
تصاویری منتشر شده از لحظه حمله یمن به فرودگاه بین‌المللی ملک خالد در ریاض
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/697461" target="_blank">📅 15:02 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697460">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/428cf0b54a.mp4?token=qaX0cj0DFJ2IVfWOmmeaHsAXbbxpzCPov9NcAaPDKxHiNNNYYwqjsGZTytuetoWNEyZCP_cXifVPYAQZjuW2Y9j5f8Y43TNEu3OeERgT4EOyiaiLwHpNndfyww76udMURX8XfGTI7NmbkS_1rKUp0OSQmnzI9DLA8DzGTvXVnyuTa-82eulP1ysXkZYuYfthjAXM9vK3gM9EUGRYxzbw1yWlnHRENj-s_l40qeZklj5r-EVc5BtGgKpQt0FZlkoQ1AufPP9e1HxnfTjdb-cGerRXpDjO4lPvUbS5_0GyuiMnilyoLFHv5dJwrEp2fvGgS5oVsidU-0JlJ_VewC6J_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/428cf0b54a.mp4?token=qaX0cj0DFJ2IVfWOmmeaHsAXbbxpzCPov9NcAaPDKxHiNNNYYwqjsGZTytuetoWNEyZCP_cXifVPYAQZjuW2Y9j5f8Y43TNEu3OeERgT4EOyiaiLwHpNndfyww76udMURX8XfGTI7NmbkS_1rKUp0OSQmnzI9DLA8DzGTvXVnyuTa-82eulP1ysXkZYuYfthjAXM9vK3gM9EUGRYxzbw1yWlnHRENj-s_l40qeZklj5r-EVc5BtGgKpQt0FZlkoQ1AufPP9e1HxnfTjdb-cGerRXpDjO4lPvUbS5_0GyuiMnilyoLFHv5dJwrEp2fvGgS5oVsidU-0JlJ_VewC6J_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیو وایرال شده از خداحافظی عجیب خانم کمبرلی سفیر آمریکا در یونان با روبیو وزیر امورخارجه آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/697460" target="_blank">📅 14:58 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697459">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
به اصرار دکتر محمدحسین امید، اسم وی از روی خوابگاهی که به نام او زده شده بود پایین آورده شد
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/697459" target="_blank">📅 14:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697458">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/156e1734ac.mp4?token=JkoJri1L3oYOAzcRQ6hWpDTJhwAlhfKbRuxheAYkKOjcn43u7EtJdjvCB8ujJF6dGHyJ88a0kzbHi0KSBDJiRxWS_yJl04znFUwnyfog7rOuuiSADHqS_CVpRre1r929ia09Rnf3bOnnYyz6i2NdjRWN1NPAHh-p0lZhdwvdb0Y6eArisnz4XI5FXXWOBzNf14P6KjFeBHHN-N08QNpEiv1cew6Lk0vaxgOX-I7iWQ4zNnlndrAtuJDdrGSoVb_cKmDA06uE0-4-OIbABZXx8-qinz_ce9oa3dcKSivRVAebCzOjpOgyxesIuKzkhoQFWhCM2cpnQTAMxtY7aiOXlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/156e1734ac.mp4?token=JkoJri1L3oYOAzcRQ6hWpDTJhwAlhfKbRuxheAYkKOjcn43u7EtJdjvCB8ujJF6dGHyJ88a0kzbHi0KSBDJiRxWS_yJl04znFUwnyfog7rOuuiSADHqS_CVpRre1r929ia09Rnf3bOnnYyz6i2NdjRWN1NPAHh-p0lZhdwvdb0Y6eArisnz4XI5FXXWOBzNf14P6KjFeBHHN-N08QNpEiv1cew6Lk0vaxgOX-I7iWQ4zNnlndrAtuJDdrGSoVb_cKmDA06uE0-4-OIbABZXx8-qinz_ce9oa3dcKSivRVAebCzOjpOgyxesIuKzkhoQFWhCM2cpnQTAMxtY7aiOXlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عربستان کشته شدن ۱۲ نفر و زخمی شدن ۳۰۹ نفر در حمله به فرودگاه ملک خالد را تایید کرد   ملیت کشته شدگان حمله یمن به فرودگاه ریاض طبق اعلام رسمی:
🔹
۴ شهروند عربستانی
🔹
۲ شهروند بنگلادشی
🔹
یک آمریکایی، یک مصری، یک اردنی، یک سوری، یک فلسطینی و یک سودانی بودند.…</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/697458" target="_blank">📅 14:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697457">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78e9d0d1c4.mp4?token=W92INX3EinBYx2EnjusIraJfOpJIhUiizIIWUwLWUiHOqPgMxanRGBtjueNQWA8O48rAFZPMRqqmpKqYAKYqsXRJYmR1h24gkUuOWmEA9UnfKmpZVbZtXdtVDh8RT-vGtMrS5DVDKjG6_mGpOIOQLmqh09ajlVsZmTr9Qp8SUsi0zmyfVEp_J0kI6dKTqQzYFnhePp5wtE3AxeWoutYd8OTo-2EsuYGrpr5CuutAWHp_JB1dHIY30GfiHPk0jCBpUGrCtxrzVWqQsIlBNUrL6iosmgmz-NonypETNycmKMc43XTotR7dygkvTHWmDCsROyJNkG1ncBmv9EoGizZkuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78e9d0d1c4.mp4?token=W92INX3EinBYx2EnjusIraJfOpJIhUiizIIWUwLWUiHOqPgMxanRGBtjueNQWA8O48rAFZPMRqqmpKqYAKYqsXRJYmR1h24gkUuOWmEA9UnfKmpZVbZtXdtVDh8RT-vGtMrS5DVDKjG6_mGpOIOQLmqh09ajlVsZmTr9Qp8SUsi0zmyfVEp_J0kI6dKTqQzYFnhePp5wtE3AxeWoutYd8OTo-2EsuYGrpr5CuutAWHp_JB1dHIY30GfiHPk0jCBpUGrCtxrzVWqQsIlBNUrL6iosmgmz-NonypETNycmKMc43XTotR7dygkvTHWmDCsROyJNkG1ncBmv9EoGizZkuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهندسان ژاپنی دُم رباتیکی پوشیدنی طراحی کردن که با الهام از دم حیوانات، به حفظ تعادل و کاهش خطر زمین‌خوردن سالمندان کمک میکنه!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/697457" target="_blank">📅 14:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697456">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
رئیس مرکز آمار ایران: برآورد فعلی جمعیت کشور، مطابق برآوردهای پیش‌تر اعلام‌شده، حدود ۸۷ میلیون نفر است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/697456" target="_blank">📅 14:49 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697455">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
پزشکیان: اگر لازم باشد برق اتاق‌های دولت را خاموش می‌کنیم اما نمی‌گذاریم چرخ کارخانه و تولید متوقف شود/ مردم همکاری کنند فشار دشمنان شکست خواهد خورد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/697455" target="_blank">📅 14:43 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697453">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54bd09cd46.mp4?token=KNn6llPnIojq8b8xrKDMqe_iajKN4SAOhYpY3iZULE1k5YRb8y3BGoOO9xLrb0psLlSgtOlnLJQM0fVIAZCAK1Jzz8gB9dzT4s5zrSE2icOXrQCFVHkmBcO9pJfcmZsjdY7rMcZRUKl-9ruxUJDnMtdX7CeS_5Yv3zOdRRBPxEImvGQVBYqbEOC74eJOn9iXXwePWilYaqnocmyD8aKFjS9VKJhrY1TaGq5_7QB9vJPElQzZQkp1ameJohEZvtCx0Xh3Hhpgk3f4kz4g4e6lWHVhLjnGWjY0cLuyAcSQ_89zPnmWPmcgHacycOEwjneLZmWhHn7LR5Tk82QlXuoJPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54bd09cd46.mp4?token=KNn6llPnIojq8b8xrKDMqe_iajKN4SAOhYpY3iZULE1k5YRb8y3BGoOO9xLrb0psLlSgtOlnLJQM0fVIAZCAK1Jzz8gB9dzT4s5zrSE2icOXrQCFVHkmBcO9pJfcmZsjdY7rMcZRUKl-9ruxUJDnMtdX7CeS_5Yv3zOdRRBPxEImvGQVBYqbEOC74eJOn9iXXwePWilYaqnocmyD8aKFjS9VKJhrY1TaGq5_7QB9vJPElQzZQkp1ameJohEZvtCx0Xh3Hhpgk3f4kz4g4e6lWHVhLjnGWjY0cLuyAcSQ_89zPnmWPmcgHacycOEwjneLZmWhHn7LR5Tk82QlXuoJPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نایا مدعی رزمایش موشکی نیروهای نظامی ایران در غرب کشور شد/ مسئولین تاکنون درباره صحت این تصاویر توضیحی ارائه نکرده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/697453" target="_blank">📅 14:36 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697452">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/008da17ca9.mp4?token=BKhpI7P7pKF6FZpUL94I_hKXdOoX9jYOUSwTJXoYyRqYSy58pcY-n0sAmEG7g2S75UyK54TP8xAaFcCcPTyOOIpSJOgatFVUasFDrdXe3J4l1DKnkO6GHo57LIU4T_NcTTs2JRGkImtBs-3PonSL_RN2WiEYnMqQjK0-x3eYLybP_yLkmVG482pPhs1dYb3qWhPwKKJiHZJ8WBNyElzwkdp5z7kthOtMZCn_3Iu9GhiMgW5bYgvTzBF4KYwSAluI6Nf19VxDxweDnoNa3370UXoZauq_JYM2hvnZm7xeeFym9auW2fvSjnZwllVfK4VT3esxxNyPVcGAVwIr-cDsUE_6W7y_qLuELF4JvN2EyRFqH5YnCivEIeBYSXADjTcxe4fgGO6E6Dc_j-W2K1womtgDsW-Wk4IvwIIK2FyOEUiBQ__eM_2RnWcOS5OEYhr8LJWMBPTxJjSA3Rjh9iltqdVbkrymAvQJr-0d4iDwMyMbPF38DwnCvzpfdxYKqROC569GVjqUd4yj_dFqrU-W-9uS6EGotfIWqn8wE-fnQX2QEmCCvWG6d4i1l9OFC-W0Vm2j_FpOCLIfwJP21T_DxEU6CQogxT94Jzn5KzhzIN5zWoBEahHkJx461niM4i6TlkLMMDkq5XYfo6fHbOmJugWRoxxP4hAr1J9TidnV4WE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/008da17ca9.mp4?token=BKhpI7P7pKF6FZpUL94I_hKXdOoX9jYOUSwTJXoYyRqYSy58pcY-n0sAmEG7g2S75UyK54TP8xAaFcCcPTyOOIpSJOgatFVUasFDrdXe3J4l1DKnkO6GHo57LIU4T_NcTTs2JRGkImtBs-3PonSL_RN2WiEYnMqQjK0-x3eYLybP_yLkmVG482pPhs1dYb3qWhPwKKJiHZJ8WBNyElzwkdp5z7kthOtMZCn_3Iu9GhiMgW5bYgvTzBF4KYwSAluI6Nf19VxDxweDnoNa3370UXoZauq_JYM2hvnZm7xeeFym9auW2fvSjnZwllVfK4VT3esxxNyPVcGAVwIr-cDsUE_6W7y_qLuELF4JvN2EyRFqH5YnCivEIeBYSXADjTcxe4fgGO6E6Dc_j-W2K1womtgDsW-Wk4IvwIIK2FyOEUiBQ__eM_2RnWcOS5OEYhr8LJWMBPTxJjSA3Rjh9iltqdVbkrymAvQJr-0d4iDwMyMbPF38DwnCvzpfdxYKqROC569GVjqUd4yj_dFqrU-W-9uS6EGotfIWqn8wE-fnQX2QEmCCvWG6d4i1l9OFC-W0Vm2j_FpOCLIfwJP21T_DxEU6CQogxT94Jzn5KzhzIN5zWoBEahHkJx461niM4i6TlkLMMDkq5XYfo6fHbOmJugWRoxxP4hAr1J9TidnV4WE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هفت میلیون برای یک جلسه؛ کنکور یا رقابت جیب‌ها؟
🔹
وقتی قبولی در کنکور فقط به درس خوندن ختم نمی‌شه و پای جیب خانواده‌ها هم وسط میاد؛ آیا رقابت بر سر دانشه یا توان مالی؟
🔹
جزئیات را در این گزارش ببینید.
@TV_Fori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/697452" target="_blank">📅 14:29 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697451">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b16ed0a34.mp4?token=ShmUN1FpeRLn46hmYgIU_hLGZsF9wZ4sDgjkLRjuYzkYVAolu6pJbQ6QQF3g-qynjvdU-F8--9og1eZY_9DRSq9aEipy0v1iOsnZPNtssh69at9OfIOkWFyoLNGeODRmcsKSdKlOBR_pskkr4QQFeb06WEVdtADSR_mE9CuTRCE567O4abMeh3PEwC6vVmbSWZXP8MwwwM8nv_U4QWeKAHet7jx5qdjJnYmQ848cQJsgHsrg3wKZxrde_E_-nTrcs1nRCNTc7SYPvqwzneTcsJOo-8z1UovzEOZoa1n0n-SH0HC2V25jQ7ZVrC82GIwAVX_T07xgkW2rQx0OjcpZBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b16ed0a34.mp4?token=ShmUN1FpeRLn46hmYgIU_hLGZsF9wZ4sDgjkLRjuYzkYVAolu6pJbQ6QQF3g-qynjvdU-F8--9og1eZY_9DRSq9aEipy0v1iOsnZPNtssh69at9OfIOkWFyoLNGeODRmcsKSdKlOBR_pskkr4QQFeb06WEVdtADSR_mE9CuTRCE567O4abMeh3PEwC6vVmbSWZXP8MwwwM8nv_U4QWeKAHet7jx5qdjJnYmQ848cQJsgHsrg3wKZxrde_E_-nTrcs1nRCNTc7SYPvqwzneTcsJOo-8z1UovzEOZoa1n0n-SH0HC2V25jQ7ZVrC82GIwAVX_T07xgkW2rQx0OjcpZBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیوی منتشرشده از آب‌گرفتگی معابر و خیابان‌های شیرگاه پس از نخستین بارش پاییزی
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/697451" target="_blank">📅 14:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697450">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96db896ba5.mp4?token=V3FYc5YLV512hGlPVTEGqY6bon3GOZXCNicGuw_cze_rCJHM_7z7RYuaBHUJGkFzl9dJ9UwHcRNilYqvyYQ2XQUIVUg-j-QYuMB5dpVqJYPniHPbFOCRa_E0mIJ7x7Cjxo86OdAZwW1Q84mXvhvW4fpm2j1XBQC_SYpcteZoEVZTA7ZXRpyfX7BQt-bghkt8HZlhVjkGzTecmxItWnOoztwVZv_IhULLq-t2INmjsHLSzv6gRB5KCav4EmyM0UxqybnWncAEyUg0KUjKVb0v9ZB0nSrz6U81MTf2CMRjcUIh7lScK_BwYllYEnT1luI0LI9_vOAa2_p4mTEX27Icpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96db896ba5.mp4?token=V3FYc5YLV512hGlPVTEGqY6bon3GOZXCNicGuw_cze_rCJHM_7z7RYuaBHUJGkFzl9dJ9UwHcRNilYqvyYQ2XQUIVUg-j-QYuMB5dpVqJYPniHPbFOCRa_E0mIJ7x7Cjxo86OdAZwW1Q84mXvhvW4fpm2j1XBQC_SYpcteZoEVZTA7ZXRpyfX7BQt-bghkt8HZlhVjkGzTecmxItWnOoztwVZv_IhULLq-t2INmjsHLSzv6gRB5KCav4EmyM0UxqybnWncAEyUg0KUjKVb0v9ZB0nSrz6U81MTf2CMRjcUIh7lScK_BwYllYEnT1luI0LI9_vOAa2_p4mTEX27Icpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صعود نفس‌گیر با موتورسیکلت کراس!
🏍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/697450" target="_blank">📅 14:16 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697449">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abd5057416.mp4?token=DUuoEC_eFnkCvE_PNakufcYdEnscrRzfM37jXBn9kh_KFWgiFNLYSI11-O-XMDQvRD8cMnwznooDqvkWkYptO4-Vl49W_qArTlFRLJLYbD4ukV6HfJUvfcJNd3dskY1Ceuq-nN7IhlThnUUDUeJKKGA6rkF3_nsAgpbH7wb9LIqn4_QY2NOJypQ5S0UzF60_XjOW9qBtRLrLqVYdfotWvX-b4af06EcgqexhgQ0cCdQI1HtGh_velFmi2QblySPQFnRr0n1V-zDNpMHNRkvISpEAmkJyHjtj0ciYSK0qKftK5u53bnoPxljSSeIg0Bl4EQW_9sILav13CpVksS_bUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abd5057416.mp4?token=DUuoEC_eFnkCvE_PNakufcYdEnscrRzfM37jXBn9kh_KFWgiFNLYSI11-O-XMDQvRD8cMnwznooDqvkWkYptO4-Vl49W_qArTlFRLJLYbD4ukV6HfJUvfcJNd3dskY1Ceuq-nN7IhlThnUUDUeJKKGA6rkF3_nsAgpbH7wb9LIqn4_QY2NOJypQ5S0UzF60_XjOW9qBtRLrLqVYdfotWvX-b4af06EcgqexhgQ0cCdQI1HtGh_velFmi2QblySPQFnRr0n1V-zDNpMHNRkvISpEAmkJyHjtj0ciYSK0qKftK5u53bnoPxljSSeIg0Bl4EQW_9sILav13CpVksS_bUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت بغض آلود رهبر شهید از حاج قاسم سلیمانی
او کسی بود که آقای شهید ایران این چنین از غمش می‌گریست
برای شهید بودن باید مثل شهدا زندگی کرد
رفیق با معرفت مثل حاج قاسم سلیمانی</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/697449" target="_blank">📅 14:11 · 19 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
