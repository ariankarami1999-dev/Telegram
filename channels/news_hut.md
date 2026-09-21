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
<img src="https://cdn4.telesco.pe/file/MguCARJz5nA0tulXDb1v8LL8mZQQlAVmP8BsMj7bzRxEA6jb0WX7tZi6UKhbi0knTP8Gxs2y9ECL3TRLkRY51_XUK74o3hklWLQklETYRVp6q-_haSotprBnZkFPfN6T2w3sI7lR4QPf467QjSm_0zVIdGLaMEyc45p0yTIti8iQbFtXlcU_OnjeQwAy7Odos2Ez-wVWanZFAP-GJTNR9q-T72uSbVjYgQ2-rTbvochL4b7hM3S3IAgBwKyuGd-TkJQM9P7woc49i9aHU_cREJEFIE6ZW4qErglOZe6ynsxAE8_1AyT1z7EHFRynqzlG6F3mdMG9AsMB7555DGFOWg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 106K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-30 15:01:28</div>
<hr>

<div class="tg-post" id="msg-71986">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8tz0nuoaLq1ujUMYa3CB1eDfoBA54tQZr7QmDd_gs7YDgiyRnpH8S3VyJcJEIgPTAd_UIstlpXKPuSZ0_iFMrmfjvboEyG2ZnkrA8U5NchzWrcXcO7DIYuFbm-pQaydAZtOiBTgNfmkNC39BmKUkBnhtquz_6beJFExrkOAX5Pe-ndV1edJc_T4rqGtCL26pqT1U6Zehcgpzh4SLG3VhmBUKvP3W0dMSzUkm776-kuxX1R8yeY29omIuM93wARb8e92TR0Kq5XJ9BXF3vmS5qYkpoQIUu1xJhP4_hURemKdlrp7aERVTFzeyL6u6KALKSfT7i1itfGgKsb3Yju12A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش پولیتیکو، سی‌ان‌ان، ام‌اس ناو و پولیتیکو پس از لغو دسترسی مطبوعاتی‌شان توسط کاخ سفید، از دولت ترامپ شکایت کرده‌اند و استدلال می‌کنند که این اقدام نقض متمم اول قانون اساسی است.
این رسانه‌ها می‌گویند که به دلیل گزارش‌هایشان هدف قرار گرفته‌اند، در حالی که رئیس جمهور ترامپ از این ممنوعیت دفاع کرد و گفت که ملزم به پذیرش رسانه‌هایی که «داستان‌های منفی» منتشر می‌کنند، در کاخ سفید نیست.
انتظار می‌رود درخواست اضطراری از یک قاضی فدرال در واشنگتن دی سی ارائه شود که احتمالاً منجر به جلسات استماع و استدلال‌هایی از سوی دولت در این هفته خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/news_hut/71986" target="_blank">📅 14:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71985">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba57cb4ffa.mp4?token=VxR0EIHUbfwep-DBDnu89oz_Y9dvSHRwY_JTY55hSxIKvFtOXnNlUnZeIJcU3p1Kdl1l1AHBnWTEA8Tm-Al53onrBrnZSZIUMjq5sBI88pdxxKMDaAE9bkDSktzuvFNYKkfoaTX7H-DwM1p7TeBUbRNTHeOTnFvvpAKcS3f-dv0XlUBT0ZlNnwaUzgo5k4anI0Lv9ORIfJz1xR_Hecl0Nxd7cNKb9e1fKnWRAq4gmjR8xD6obzQrTnJWwTE-dfK2XODic2dR7TZjGLAZEYEZYTvIyhjrCWjTmWPyELUMoaUwZaXuXc2Bu7cO7zkr-RmFfkyZ51ib1JIt_Z3upHk3aJ4JyMIXBeTb-0-f3VkIrfCDoP99PAMihcES8JHtF8GD8yEdo69ZL6N_m-v3lwLK3h4Qlm-ocbG5sIQ2hNH8OxoEowMOaQis-cbNm9a_GUX-mThZ4LkSdfCLRv-IM2x1SYh7NydPX9WKw1ihPEt8hrHISDmH8Y-B1QMJ2_DMFy5ZL7tUAB8onO5yfjU6hK9Is8fQX7FLrVsKnpU-bvjrBN4zhLKc1HmVs8vtwv0oJTxkfeJnSDN8TV1MueLmI_jLFNsgxbaiPJsO3NFJHZlPJrvnGgqwr9Hiv4Of9Z5EfL769kRMUarxT_x0JZEd_k_SsGhvOav8WjqFGG7eNnTHRoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba57cb4ffa.mp4?token=VxR0EIHUbfwep-DBDnu89oz_Y9dvSHRwY_JTY55hSxIKvFtOXnNlUnZeIJcU3p1Kdl1l1AHBnWTEA8Tm-Al53onrBrnZSZIUMjq5sBI88pdxxKMDaAE9bkDSktzuvFNYKkfoaTX7H-DwM1p7TeBUbRNTHeOTnFvvpAKcS3f-dv0XlUBT0ZlNnwaUzgo5k4anI0Lv9ORIfJz1xR_Hecl0Nxd7cNKb9e1fKnWRAq4gmjR8xD6obzQrTnJWwTE-dfK2XODic2dR7TZjGLAZEYEZYTvIyhjrCWjTmWPyELUMoaUwZaXuXc2Bu7cO7zkr-RmFfkyZ51ib1JIt_Z3upHk3aJ4JyMIXBeTb-0-f3VkIrfCDoP99PAMihcES8JHtF8GD8yEdo69ZL6N_m-v3lwLK3h4Qlm-ocbG5sIQ2hNH8OxoEowMOaQis-cbNm9a_GUX-mThZ4LkSdfCLRv-IM2x1SYh7NydPX9WKw1ihPEt8hrHISDmH8Y-B1QMJ2_DMFy5ZL7tUAB8onO5yfjU6hK9Is8fQX7FLrVsKnpU-bvjrBN4zhLKc1HmVs8vtwv0oJTxkfeJnSDN8TV1MueLmI_jLFNsgxbaiPJsO3NFJHZlPJrvnGgqwr9Hiv4Of9Z5EfL769kRMUarxT_x0JZEd_k_SsGhvOav8WjqFGG7eNnTHRoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر قطر:
از زمان جام جهانی، دیگر روی آرامش را ندیده‌ام.
پس از آن، ماجرای هفتم اکتبر پیش آمد و از آن زمان تاکنون، هیچ‌کس حاضر نیست به ما فرصتی برای نفس کشیدن بدهد.
از همه خواهش می‌کنم؛ ما برای سال ۲۰۲۷ به سالی سرشار از صلح و آرامش نیاز داریم.
لطفاً، ما به کمی استراحت نیاز داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/news_hut/71985" target="_blank">📅 13:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71984">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLpfnTfuOCeoJSJIHF9SLAmmAV0muFeQXyVTTeSRFl43xrUIoWwJCej-JD_2X8veNREQVdMY3tLrdy9tfNMrS3TJngjKKnihWQXAMqXWliLbB632sfuklyQuxLPLNrX7z6abOzsoSJUUirBQAlBSwI-zr9nq5tzHprlWp-L0G7POjASGLTZpnw3Fw0ywmpUjGNq-ouuywno8jyEs3_UC1DLP--XrCUoYzw6XOgS2oFqDxiNnTgBwT_TPZI1jZYwyQfPkoLw_N6y9BxuYxjuNzdp2FNDvtNvBs7kap3Rc1MzXhUQH2o4Bug8LV73kjVdB1eJqPU5Oq8hJMSVcT-zS8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
در هشدار شماره ۲۶-۱۴۰ که ساعت ۰۷:۳۰ به وقت هماهنگ جهانی (UTC) صادر شد، گزارش داد که یک نفتکش در حال عبور به سمت داخل تنگه هرمز، مورد اصابت یک پرتابه ناشناس قرار گرفته است. دو تن از خدمه دچار جراحات سطحی شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/news_hut/71984" target="_blank">📅 13:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71983">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ada732dd6.mp4?token=kT3o8In0uccgE9NtOTr_XzTFy9s1vuXRX3etPGUtPpBB4ZcpmlBN9T3VWj00b-qx-FVbR-BIzzqv-POafQKcO84pjHKBjG_3mOTSjVWeJ64_QDYECokAvmce9KbxBKJLsyhEWPAyNx_X9hvG1FUrXDHqIR5I1qXQd_wPwQErzQVvdvw7indjOywXu2C6DseNaFcYI5KBCf74pY_fYO0UhXcKw0CqzGweLvitP0rEKIOLrxozIfZ8Cn8KkUqUiWIrn8Ta5GdHVClChxmlW8E2CPJ-QOSzyelm50AjItv8WwTDuhq5POUJrTs34feibLEKaF0xmimoRi-IzDMB9g_Umg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ada732dd6.mp4?token=kT3o8In0uccgE9NtOTr_XzTFy9s1vuXRX3etPGUtPpBB4ZcpmlBN9T3VWj00b-qx-FVbR-BIzzqv-POafQKcO84pjHKBjG_3mOTSjVWeJ64_QDYECokAvmce9KbxBKJLsyhEWPAyNx_X9hvG1FUrXDHqIR5I1qXQd_wPwQErzQVvdvw7indjOywXu2C6DseNaFcYI5KBCf74pY_fYO0UhXcKw0CqzGweLvitP0rEKIOLrxozIfZ8Cn8KkUqUiWIrn8Ta5GdHVClChxmlW8E2CPJ-QOSzyelm50AjItv8WwTDuhq5POUJrTs34feibLEKaF0xmimoRi-IzDMB9g_Umg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سؤال: آیا ایران دردسرساز است؟
نخست‌وزیر قطر: کاملاً آشکار است که آن‌ها صلح‌جو نیستند.
@News_Hut</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/news_hut/71983" target="_blank">📅 12:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71982">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0a06bd3e5e.mp4?token=d7t79yUWGvGzblk2anI4UupXZgcU3oFtzMoihzocLzcUPK7OwhSN_cVo4HX8HByXXKxGqedT3YB779gsS5DyuuoOo1gzohophXVmYoOpPrDLEEZCicFg2n9EvaaplvG2zw4EwfCoLnOGdO8o6BYYu3K8bVmeff1HG5sXDe-5AIP_r8wRBAQjFd0bBdc4Zjz2gw8nkVAvxkfpIJwCvn4LB6syW0JDZDc-iVfdYrSxYpN04yKtIZMWG9L67P3EqJBVsIuKTg6YnpDDRYkt9M62pBPktiKGJlvcqzy5vudccyMOAatL_N2SUnME_kBy5k_SzQAk-i2O5mhJeN-BfkecVA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0a06bd3e5e.mp4?token=d7t79yUWGvGzblk2anI4UupXZgcU3oFtzMoihzocLzcUPK7OwhSN_cVo4HX8HByXXKxGqedT3YB779gsS5DyuuoOo1gzohophXVmYoOpPrDLEEZCicFg2n9EvaaplvG2zw4EwfCoLnOGdO8o6BYYu3K8bVmeff1HG5sXDe-5AIP_r8wRBAQjFd0bBdc4Zjz2gw8nkVAvxkfpIJwCvn4LB6syW0JDZDc-iVfdYrSxYpN04yKtIZMWG9L67P3EqJBVsIuKTg6YnpDDRYkt9M62pBPktiKGJlvcqzy5vudccyMOAatL_N2SUnME_kBy5k_SzQAk-i2O5mhJeN-BfkecVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان هم به این شکل زنگ آغاز سال تحصیلی جدید رو به صدا درآورد.
@News_Hut</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/news_hut/71982" target="_blank">📅 12:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71981">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71981" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/news_hut/71981" target="_blank">📅 12:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71980">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Avd1F5t8XYfcHu2ffZ-CpBV7bD53gNkxB1tA69-HZJfhEA21dLZhC7fKbgTEKNywyLeR6gHYutmBS0R6_rDTX62Lq2I1n2X2fHULoG4IVPC-yZzxg30FX2AqoqBUAL153ls43X1gjR4VTfcXdfCewaCRbYrrpgf8FKhkbH4_llqV6Mtq06pni7BxKX6Wa80TG1IsQvqTlEKm2ierjd0GNlP2BKHMZcwHciCCU9aOEr1cMQRp8rsA2iBH0dzcYS88vNTJEgE-RdbgVZBbqv8eITEiiWGA3rGGALV1E48qcRNfL-3-jEFWhHuWg3wGH1FVMiflanywP0S3igGnfZKQaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مسابقات
UFC Fight Night
شروع شد!
🦖
یک شب پر از مبارزات هیجان‌انگیز، رقابت‌های نزدیک و لحظه‌هایی که نتیجه می‌تونه در چند ثانیه تغییر کنه.
مبارزات رو زنده دنبال کن، عملکرد فایترها رو بررسی کن و پیش‌بینی خودت رو در
TrexBet
ثبت کن.
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/news_hut/71980" target="_blank">📅 12:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71979">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/19ac1824ad.mp4?token=GotKPvZDbue0eLRq8SJ34k05rOqJ6zspBfjxd0Orz1hyxeToq-45Tm46xBde81gyXiYiDr1Xht9dUmMlJ_HqrugZdmJgaQedCMFEL5nIGnHI906IYKAoV-10tNjOYRHjw-XQfu8o_85BuGj82mi0I2Qkyzrq6ntnA45_H01NbOHxq1R8o1xwiWHLw7TVCaNv-3YkMIGy2pf3v46heV3ys3ZfVj6kTxSKAGVSd8hFl4kuKr32Nx6jkxBaqII-Djz8kpMVM4rARU2vmGW7DaKe58mKNd-r_R3uh-syhvlPM6PANKNgxLA3CZEPAe18oDRjXpTLacdp8cth29Oj4r6zkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/19ac1824ad.mp4?token=GotKPvZDbue0eLRq8SJ34k05rOqJ6zspBfjxd0Orz1hyxeToq-45Tm46xBde81gyXiYiDr1Xht9dUmMlJ_HqrugZdmJgaQedCMFEL5nIGnHI906IYKAoV-10tNjOYRHjw-XQfu8o_85BuGj82mi0I2Qkyzrq6ntnA45_H01NbOHxq1R8o1xwiWHLw7TVCaNv-3YkMIGy2pf3v46heV3ys3ZfVj6kTxSKAGVSd8hFl4kuKr32Nx6jkxBaqII-Djz8kpMVM4rARU2vmGW7DaKe58mKNd-r_R3uh-syhvlPM6PANKNgxLA3CZEPAe18oDRjXpTLacdp8cth29Oj4r6zkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاید باورتون نشه ولی، یه دختر نصف شب، این شکلی دختر خالشو سورپرایز کرد:
یه دسته گل بزرگ+ آیفون ۱۸ پرومکس+ کلی شکلات!
@News_Hut</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/71979" target="_blank">📅 12:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71978">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfc3620090.mp4?token=JCxPB_4u7NLS4ebNH5OkUC2U-piSLb6Bl4VqyFzecJTPaFchTlgOK6CPpqIJ7OfWLeaqw8wvXP-Z6FP1pUDeZitO-2q7oUJzuhB0NUwpuFzU_zLDJkGXZffyViUkDyZB8hzf5GwZPhipwjwE4MEbP1fVmOTbGF0m1QrzQBhG0WGGlU_XfEOxNt0LvNLORf2Y-iDXWsG85rXDZFuVRjIo56TSl-DH4zN020aQIgX6lBgYncF_ograCrskPC0SU6AxbGL2YK_yCSqm9uLQca654GIdLjpQADb143_IoM_qQ4kKBbfomcMZlH6--2CvEZMmL5RFt6ZVz_VguRI9Xwtd0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfc3620090.mp4?token=JCxPB_4u7NLS4ebNH5OkUC2U-piSLb6Bl4VqyFzecJTPaFchTlgOK6CPpqIJ7OfWLeaqw8wvXP-Z6FP1pUDeZitO-2q7oUJzuhB0NUwpuFzU_zLDJkGXZffyViUkDyZB8hzf5GwZPhipwjwE4MEbP1fVmOTbGF0m1QrzQBhG0WGGlU_XfEOxNt0LvNLORf2Y-iDXWsG85rXDZFuVRjIo56TSl-DH4zN020aQIgX6lBgYncF_ograCrskPC0SU6AxbGL2YK_yCSqm9uLQca654GIdLjpQADb143_IoM_qQ4kKBbfomcMZlH6--2CvEZMmL5RFt6ZVz_VguRI9Xwtd0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از دو دختر جانفدا به اسم پرنسس های جنگجو؛
میگه همه با دوست پسراشون میان رزمایش من با دوست دخترم
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/71978" target="_blank">📅 11:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71977">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">محبی، سخنگوی سپاه پاسداران:
در صورت وقوع حمله‌ای دیگر از سوی آمریکا، ایران واکنش نظامی خود را — از جمله «جغرافیای جنگ» و تسلیحات مورد استفاده — به‌طور قابل‌توجهی تغییر خواهد داد.
«ما تسلیحات جدیدی با قابلیت‌های تازه به میدان نبرد خواهیم آورد و جهانیان شگفت‌زده خواهند شد.»
محبی افزود که ایران همچنین «اهداف جدیدی» در اختیار دارد که تاکنون مورد حمله قرار نگرفته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/71977" target="_blank">📅 10:56 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71975">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9961c391f4.mp4?token=JYdpY_HTc4XunZEMtN_iAE4A51E4Sih1uCWEKCIod3JdMSOaNluh8r1xAInjpAV2hfqU_U3ENcl-fhODmH-Lw9pJRfXogp3kexuzraCjJOOzXHnikWa1Zm-Oje9yLfuS42wSMD8sUx157sPe8bERwm28KnOun-rDAYlZVgyu6nU5XYplTlVQGb3jicZs6rUF2LcKAFu6DhCJuwu41v7bJ5AkEFcy3Kk84ViSIQyDxN06E_kNEXjsSRw33dglb0u4RXuP5mEwrRW6-F-IG-VyqfdXF-wmns4ykWXoKgp2516WzVfzyHp1WeMVpK9ZavWwjUJsnfKhj7qqLmht5X2QFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9961c391f4.mp4?token=JYdpY_HTc4XunZEMtN_iAE4A51E4Sih1uCWEKCIod3JdMSOaNluh8r1xAInjpAV2hfqU_U3ENcl-fhODmH-Lw9pJRfXogp3kexuzraCjJOOzXHnikWa1Zm-Oje9yLfuS42wSMD8sUx157sPe8bERwm28KnOun-rDAYlZVgyu6nU5XYplTlVQGb3jicZs6rUF2LcKAFu6DhCJuwu41v7bJ5AkEFcy3Kk84ViSIQyDxN06E_kNEXjsSRw33dglb0u4RXuP5mEwrRW6-F-IG-VyqfdXF-wmns4ykWXoKgp2516WzVfzyHp1WeMVpK9ZavWwjUJsnfKhj7qqLmht5X2QFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات پهپادی روسیه به زاپوریژیا به یک مرکز خرید و قدیمی‌ترین ساختمان دانشگاه ملی زاپوریژیا آسیب رساند.
در حملاتی جداگانه در منطقه اودسا، انبارهای مواد غذایی که گفته می‌شود متعلق به فروشگاه‌های زنجیره‌ای «سیلپو» (Silpo) هستند، هدف قرار گرفتند.
در استان کی‌یف، این حملات به ۳۴ نقطه در پنج منطقه، از جمله خانه‌ها، انبارها و زیرساخت‌ها، خسارت وارد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/71975" target="_blank">📅 10:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71974">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08216dc24f.mp4?token=Ie1RtGpXuPlbWbYbfDWuM_-nhNsGUpYMhwXYQUhkJ2_2dkOI4pIKEL5YnTWUq3M_JLpCdQu7atqsqd5ojSnzvaDyP9w5sYFPLc5qxvpyqxMqG9srHllHMRxlN8-9VbUtDIJmxRECOrcgx2W095TdKAG2XXBHQRcLw2GJeo1yHH_Elj37QLGdnEU46h88J0HBsAj70lB7Zrtm980GtRuq_i6fdJRb91kn7cRNftE2_N-nYsKImEB8ZcpAn5F9q6dH4GfgRzjcJz3AwLAorllKLnmjqZfREfIAVydaJVdefy_9EniC3zSH8_5aJyNT02ncmlvHhDS_SNfT8CWjDydkFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08216dc24f.mp4?token=Ie1RtGpXuPlbWbYbfDWuM_-nhNsGUpYMhwXYQUhkJ2_2dkOI4pIKEL5YnTWUq3M_JLpCdQu7atqsqd5ojSnzvaDyP9w5sYFPLc5qxvpyqxMqG9srHllHMRxlN8-9VbUtDIJmxRECOrcgx2W095TdKAG2XXBHQRcLw2GJeo1yHH_Elj37QLGdnEU46h88J0HBsAj70lB7Zrtm980GtRuq_i6fdJRb91kn7cRNftE2_N-nYsKImEB8ZcpAn5F9q6dH4GfgRzjcJz3AwLAorllKLnmjqZfREfIAVydaJVdefy_9EniC3zSH8_5aJyNT02ncmlvHhDS_SNfT8CWjDydkFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مونا محبی، تراپیست :
«یه بیمار داشتم که سه تا پسر داشت؛ فقط پسر اول بچه شوهرش بود. پسر دوم بچه عموی شوهرش و پسر سوم هم بچه شوهرعمه شوهرش بود!
حالا بچه دوم یه مشکل خونی پیدا کرده و برای تشخیص باید
آزمایش ژنتیک
بده؛ آزمایشی که ممکنه مشخص کنه بچه، بچه شوهرش نیست و این راز بعد از سال‌ها لو بره.
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/71974" target="_blank">📅 10:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71973">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b710ab2e63.mp4?token=g2FC9Rr8jXwUJHN_WoPJ-7EKIeQeJeXMKKhAbVSG1NnBY9_7XqyMU4VHY_4241y6lFmZopsl9Saim6vlGxJ1SzrTaDXuuL75iXlTWkKtKuuhk494p-MpQr74bUPeJowWOUxAgPwH3PAEY0hRhSlO6Vmt9Ou0LsOyq41Ipqm-r7dDV615T9TjS9zd5X7gzR2o751l5b5BYv6yIdhGfgHR90qTyY5gUO0O0WI181L2dkzCKRvWl2I-i5Vj3hOQSUt3wmHQMo1b8zkva0KXXvV5w0IUh5YAh4hgPq9f53OS9n8LRcTTqKWJzijrLhGxD89i_0GtED9sR2BIGhdjwCJV5ZQyzrCiHz2mwBU_Jdy9TkH1LOa4qe0TKOGLKj8JFBDPb9BRPtwf-zmSAr7bgtjD7jLo5Svh7yZpf4OJ5G7kc1bCzJgMMG-zRz8UWnO3GUDuzlRYirjfpjnuGDgypy7FT66jLWavUT0AnxlTcMo_8m9_Hvv-a5RMACakQAsbJANZO7p5UvnKqsqjDalVCLj2IwZPWqo5-4xcIqIm_Lya01FuHXw74_kPfGTC5D5711oAV78dLWcQX5ZryRSBTVHeM45Lt5MSCJeyinGe-42nNZZ6rSHzfqk--haqxY-DX2RHW7edshl6VGrye2tyOBIMLzyvB9Y7sNRXR3FCRC8FvBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b710ab2e63.mp4?token=g2FC9Rr8jXwUJHN_WoPJ-7EKIeQeJeXMKKhAbVSG1NnBY9_7XqyMU4VHY_4241y6lFmZopsl9Saim6vlGxJ1SzrTaDXuuL75iXlTWkKtKuuhk494p-MpQr74bUPeJowWOUxAgPwH3PAEY0hRhSlO6Vmt9Ou0LsOyq41Ipqm-r7dDV615T9TjS9zd5X7gzR2o751l5b5BYv6yIdhGfgHR90qTyY5gUO0O0WI181L2dkzCKRvWl2I-i5Vj3hOQSUt3wmHQMo1b8zkva0KXXvV5w0IUh5YAh4hgPq9f53OS9n8LRcTTqKWJzijrLhGxD89i_0GtED9sR2BIGhdjwCJV5ZQyzrCiHz2mwBU_Jdy9TkH1LOa4qe0TKOGLKj8JFBDPb9BRPtwf-zmSAr7bgtjD7jLo5Svh7yZpf4OJ5G7kc1bCzJgMMG-zRz8UWnO3GUDuzlRYirjfpjnuGDgypy7FT66jLWavUT0AnxlTcMo_8m9_Hvv-a5RMACakQAsbJANZO7p5UvnKqsqjDalVCLj2IwZPWqo5-4xcIqIm_Lya01FuHXw74_kPfGTC5D5711oAV78dLWcQX5ZryRSBTVHeM45Lt5MSCJeyinGe-42nNZZ6rSHzfqk--haqxY-DX2RHW7edshl6VGrye2tyOBIMLzyvB9Y7sNRXR3FCRC8FvBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک پاراگلایدر سوار لحظاتی را که در حین فرود به سرعتی بیش از ۱۲۵ کیلومتر در ساعت می‌رسید، ثبت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/71973" target="_blank">📅 09:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71972">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c67a57267.mp4?token=vJhk6V3GcfJsrQrXi0wOCt3LymrhojAWPKsE9iq53u3bwVHXeDZ8H4hKWOlVj4XAeB74oKncVKGUtfZTB9fmhaIutgpLUzdppC9MoSy2xNqJ8axc9T4TSG4dyVA3iTpDEyU8W91pApfdrnf43m16qu2q1LKX1O-BxoGUtZp6YKcUo6Jo5oTVw3sTZjugxCeTcgovrrlCUt5wiKMnVWsfeywvXf5dR8cimvnGL2iXK855t2sYtNE99ki55FKf7zTCAAqy04T455rc5TASxKaVR071gH97CGCzQeJb8FloNJ4JGR2u-3vbrgu4WA6L5TSVE1ihHknERqfEQMAApr1FLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c67a57267.mp4?token=vJhk6V3GcfJsrQrXi0wOCt3LymrhojAWPKsE9iq53u3bwVHXeDZ8H4hKWOlVj4XAeB74oKncVKGUtfZTB9fmhaIutgpLUzdppC9MoSy2xNqJ8axc9T4TSG4dyVA3iTpDEyU8W91pApfdrnf43m16qu2q1LKX1O-BxoGUtZp6YKcUo6Jo5oTVw3sTZjugxCeTcgovrrlCUt5wiKMnVWsfeywvXf5dR8cimvnGL2iXK855t2sYtNE99ki55FKf7zTCAAqy04T455rc5TASxKaVR071gH97CGCzQeJb8FloNJ4JGR2u-3vbrgu4WA6L5TSVE1ihHknERqfEQMAApr1FLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد شجاعی، از روحانیون حامی جمهوری اسلامی:
امام‌زمان برای ظهور به لشکر نیاز دارد
۵۰ روستا در لبنان را که سال گذشته بازسازی کرده بودیم، از بین رفتند
دیشب طرح آبرسانی به مردم غزه را آغاز کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/71972" target="_blank">📅 09:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71969">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lw4tQE1Ny2frQSHgYBYjBUeEpBkWqesleCcmuI2Na82-vWJlelWvOd-IDGpTX4ipZHDXBHYf6D78gVNe2HMDa_qbeaiE58sIUxN1q9TwFoUpq28bGTPxotK2lvjCPRSB6pubj7npPpyUSqKbYZ5D34jXsp6St_qBRjAu-GeE4fEdQIq8AIKPWUzZbrRM28PySfGCQ1fuzb7WXKxO63JfZJTfHRn81MaDec8Y2f2F5yHZy6-gBBn1Emx-VZTBw7Sr688Cw36GbOiJNnkTd_HQgSyQu4Ei63wWYvNQpwraT-4EIr7IjFlHn2Kk2B6Bb9LgpZdd_iatHJ2V2SSA8sbrAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5e7e08059.mp4?token=GVNWP73c8on3uqminJ-Rv-i0TR268nK5nEbSrBDuzzd6ryVICogaatV9OVElzTklHbmp193FTKZrCLtLi5PiDMHjJ5a4Pqt86g6D4rDSeDyGPmPTA7wEvPaR5K1B3HWwF8GmiQQtPlx5AfFI0bbUcWdmSceD1ri-e7obRdKNWqhWRoLsTeCaUbP8e3Rz4Gvq1trB6gohegsAwDc3arIKATmT_bhEZgmvVR7VsKI53EFiTa4YwtOFVrMB-qCcSdgNMLFxOQfKcgN-0wTN-yH6xI9CqCRMfnI6qPE2sNBFiZv7YhQwpKZo1b4sGlgKBELgdeoVhnp038lYeSWcoKJo0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5e7e08059.mp4?token=GVNWP73c8on3uqminJ-Rv-i0TR268nK5nEbSrBDuzzd6ryVICogaatV9OVElzTklHbmp193FTKZrCLtLi5PiDMHjJ5a4Pqt86g6D4rDSeDyGPmPTA7wEvPaR5K1B3HWwF8GmiQQtPlx5AfFI0bbUcWdmSceD1ri-e7obRdKNWqhWRoLsTeCaUbP8e3Rz4Gvq1trB6gohegsAwDc3arIKATmT_bhEZgmvVR7VsKI53EFiTa4YwtOFVrMB-qCcSdgNMLFxOQfKcgN-0wTN-yH6xI9CqCRMfnI6qPE2sNBFiZv7YhQwpKZo1b4sGlgKBELgdeoVhnp038lYeSWcoKJo0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند ساعت قبل شخصی این ویدیو رو با این توضیحات منتشر کرده؛صحت ویدیو تایید یا تکذیب نمیشه:
تهران ، اتوبان آزادگان
29 شهریور
از اجرام ناشناخته آسمانی فیلم گرفتم
واقعا نمیدونم چی هست ولی نزدیک ابرها بود نور های خاصی داشت و بدون هیچ صدایی در فضا معلق بود !!!
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71969" target="_blank">📅 06:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71968">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71968" target="_blank">📅 01:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71967">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/news_hut/71967" target="_blank">📅 01:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71966">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d2ba66ac5.mp4?token=uVtTo0fmoH3tBX5Jb8r6DvmVDMbXCufMcxM7YP_SVdEsX97UGmm-ZWv99dqE_iAquRBbZ2O2GrKa11aew6RU58mFOtwq76oGWc7RvPbVFsehGOQChPh26PhIjIDUF_xADIToZTAqxxisozHV9ekalPNoovf_xSPbTlICeBeCUJWiwOPxqraKDwuaZQpGCEQZMSEhhqg4n5-Kow5oOw3bQQKZctmMpxm1LbdovB4KbOyM4LH9IiUo5V3Ag5rhIjAhxXyk-M-DxrqWlx1KmmS9DF3PLaE0MZPDnDAH9QV78R3QsR0vTB89-H__YvrF669ghr2cNr0YcwJyMg1z3R3wdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d2ba66ac5.mp4?token=uVtTo0fmoH3tBX5Jb8r6DvmVDMbXCufMcxM7YP_SVdEsX97UGmm-ZWv99dqE_iAquRBbZ2O2GrKa11aew6RU58mFOtwq76oGWc7RvPbVFsehGOQChPh26PhIjIDUF_xADIToZTAqxxisozHV9ekalPNoovf_xSPbTlICeBeCUJWiwOPxqraKDwuaZQpGCEQZMSEhhqg4n5-Kow5oOw3bQQKZctmMpxm1LbdovB4KbOyM4LH9IiUo5V3Ag5rhIjAhxXyk-M-DxrqWlx1KmmS9DF3PLaE0MZPDnDAH9QV78R3QsR0vTB89-H__YvrF669ghr2cNr0YcwJyMg1z3R3wdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حوثی ها:
آری، امروز ما حرمین شریفین را هدف قرار خواهیم داد؛ آن‌ها را هدف می‌گیریم تا از وجود آل سعود پاک‌شان کنیم.
ما این حرمین شریفین را هدف قرار می‌دهیم تا به چراغ راهی برای مسلمانان آزاده بدل شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71966" target="_blank">📅 00:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71965">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89dd2a1fad.mp4?token=fcCfyksF52fcX6gn0WhaeGtiJyPwCFSGXCYoOTb14vJa_xXg6R07-RtLoirpBgDELbZUqcxRHHBj6aZs7dDb_RQYZqLLvLTjx-Og2FVN9pdiaRIeV9CXql9hPVKKlCjZwsy0FAo7G2SbqBPaPTh6GyIor5ij3gaTzzVKIlFWU4quWgeZhccDa2dv93ZKmp0PaTwjGCjng7ZMkAH2sYNoGQ3h6hzRYqHgaW_lHlgULWIQHzpacpQ_CoUoFDlEsrx1d6_d7RDXYE2nYi0K1J1KoYzF15ffiWd8NbOcT79iXkW3Iah2oFG3-FbNtrgiyNqpiFnG1m6iYMuYljGrt6pkQj3shnBPLQxWUzbB1C0yK5imi3nvW2zy9zFfgemlw_Kg1sBs5xEZaw-Qt5ONfutdWNpyXTFj4R9cNbQJnlp4Mv4smetkqxRTBtes5zN2UMFDGMr84CE10Akc6V3Y8UEWUNrONPy4hdfF8mNFR4YjCvbrzB52wojXc3kcGWYzloMnUCNjoNnDs6ViE8GdZfD-q2701aRpCigZ2xXzC6XnSLo0i34sEpieVpP_NYyXhMX7E_DIG8A9TvRsD2BTjVc5c8PgHnCBdHWiPuKf9L_dbF04H5ZIgR_D_0N_VVqYLJUFm0crFaV4cd3Sg_ooTgxG9cdw5vtYKB-LbvudzJl6aF4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89dd2a1fad.mp4?token=fcCfyksF52fcX6gn0WhaeGtiJyPwCFSGXCYoOTb14vJa_xXg6R07-RtLoirpBgDELbZUqcxRHHBj6aZs7dDb_RQYZqLLvLTjx-Og2FVN9pdiaRIeV9CXql9hPVKKlCjZwsy0FAo7G2SbqBPaPTh6GyIor5ij3gaTzzVKIlFWU4quWgeZhccDa2dv93ZKmp0PaTwjGCjng7ZMkAH2sYNoGQ3h6hzRYqHgaW_lHlgULWIQHzpacpQ_CoUoFDlEsrx1d6_d7RDXYE2nYi0K1J1KoYzF15ffiWd8NbOcT79iXkW3Iah2oFG3-FbNtrgiyNqpiFnG1m6iYMuYljGrt6pkQj3shnBPLQxWUzbB1C0yK5imi3nvW2zy9zFfgemlw_Kg1sBs5xEZaw-Qt5ONfutdWNpyXTFj4R9cNbQJnlp4Mv4smetkqxRTBtes5zN2UMFDGMr84CE10Akc6V3Y8UEWUNrONPy4hdfF8mNFR4YjCvbrzB52wojXc3kcGWYzloMnUCNjoNnDs6ViE8GdZfD-q2701aRpCigZ2xXzC6XnSLo0i34sEpieVpP_NYyXhMX7E_DIG8A9TvRsD2BTjVc5c8PgHnCBdHWiPuKf9L_dbF04H5ZIgR_D_0N_VVqYLJUFm0crFaV4cd3Sg_ooTgxG9cdw5vtYKB-LbvudzJl6aF4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی:
من به تمام کشورهای عربی و همسایه می‌گویم: اگر آمریکایی‌ها تلاش کنند در روابط تجاری و مالی ما اخلال ایجاد کنند، ما دو اقدام انجام خواهیم داد.
نخست اینکه قطعاً به شرکت‌های آمریکایی — از جمله شرکت‌های حفاری آمریکایی که فعالیت گسترده‌ای در پیرامون ما دارند، و همچنین شرکت‌های تجاری و بنگاه‌های اقتصادی آمریکا — حمله خواهیم کرد.
ما آن‌ها را هدف قرار خواهیم داد و اعلام می‌کنیم: این حمله‌ای به اقتصاد آمریکا در پاسخ به حمله آمریکا به اقتصاد ایران است؛ یعنی مقابله‌به‌مثل در برابر حمله.
از سوی دیگر، به کشورهای همسایه نیز می‌گوییم: با آمریکا همکاری نکنید، زیرا ما نیز اقدام متقابل انجام خواهیم داد. اگر کشوری همسایه در اعمال محاصره اقتصادی علیه ایران — برای مثال در امور مالی و فعالیت‌های مرتبط با ما — با آمریکایی‌ها همکاری کند، ما کشتی‌های آن کشور را در تنگه هرمز تنبیه خواهیم کرد.
ما بر تردد و عبور و مرور آن‌ها و برخی فعالیت‌هایشان محدودیت‌هایی اعمال خواهیم کرد، یا در زمینه همکاری‌های اقتصادی، اقدام متقابل انجام خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71965" target="_blank">📅 23:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71964">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d864b0e8a.mp4?token=vod6_ZsE-GFhOMo5jjKkcpSJG-yDT7sEj_h1X9sMkY2oJ1ri8opxF5pO4ah2-Eiu_465spmUt6CUC1MBNk2i4F94HL07SbOmykBAMS1hXKE37B7uZvjlEu7dJkE0xkXLgROry-giUqsbKTARRP_hBAq3IcS828aiPiWzUGLvsQtNn7VZuW3cPXxPsT7KrEmMe07NiQuMGOjjH-7qgBfLJhZcle3WvM4vwh4FZMMFiQmD7a45Jco4fZY93rurKvetjTvpPx9wLgpYNWBUbqIvj4eOhrI6JuLIG9C0cgrzfInwwEJszcXBYZK2vt3hZUgAM0JwWv8qEFTL7pg2BCa8GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d864b0e8a.mp4?token=vod6_ZsE-GFhOMo5jjKkcpSJG-yDT7sEj_h1X9sMkY2oJ1ri8opxF5pO4ah2-Eiu_465spmUt6CUC1MBNk2i4F94HL07SbOmykBAMS1hXKE37B7uZvjlEu7dJkE0xkXLgROry-giUqsbKTARRP_hBAq3IcS828aiPiWzUGLvsQtNn7VZuW3cPXxPsT7KrEmMe07NiQuMGOjjH-7qgBfLJhZcle3WvM4vwh4FZMMFiQmD7a45Jco4fZY93rurKvetjTvpPx9wLgpYNWBUbqIvj4eOhrI6JuLIG9C0cgrzfInwwEJszcXBYZK2vt3hZUgAM0JwWv8qEFTL7pg2BCa8GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو تهران دختره بعد از اینکه پروفایل اکسشو‌ چک میکنه و میبینه اکسش رفته با یکی دیگه درجا سکته میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/71964" target="_blank">📅 23:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71963">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3758b5713d.mp4?token=Wk9yp6ZxJGxZvgAm-7JM85bXWx5BCv2oGp77hCxcz4YJJ-WENgPu-5xKdJgUI-UvZdY0oJzHRvreeZOVef0kxjuMzf9HPcj-wu4MnzhH21L4HDDlMBUoy6iP1IZUim90u0mVWI-K9vhBQfJAv1iOarAG7zRsemBoTq0qjJkZ6SWNmHB13NBOPSeQJnK6d13FqnWSG1QUYt7eeqTMuQEyqWCBb21NcdMOc025YrAOkXi0yMeMfwSvxC6Rt7QLdR2s_xzLV5z-q4mLPY-yMvX0l0suopdttYWYlQzcAdT37DLUwCBppgNeotHQH0XcIYRIZmcPf3EAWNCX3T9n889UkA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3758b5713d.mp4?token=Wk9yp6ZxJGxZvgAm-7JM85bXWx5BCv2oGp77hCxcz4YJJ-WENgPu-5xKdJgUI-UvZdY0oJzHRvreeZOVef0kxjuMzf9HPcj-wu4MnzhH21L4HDDlMBUoy6iP1IZUim90u0mVWI-K9vhBQfJAv1iOarAG7zRsemBoTq0qjJkZ6SWNmHB13NBOPSeQJnK6d13FqnWSG1QUYt7eeqTMuQEyqWCBb21NcdMOc025YrAOkXi0yMeMfwSvxC6Rt7QLdR2s_xzLV5z-q4mLPY-yMvX0l0suopdttYWYlQzcAdT37DLUwCBppgNeotHQH0XcIYRIZmcPf3EAWNCX3T9n889UkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیر ایرانی چند ماه پیش:
کیرم تو جمهوری اسلامی! کیرم تو قبر خامنه‌ای، ایشالا تو جهنم میسوزه!
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/71963" target="_blank">📅 22:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71962">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baf9813dda.mp4?token=VOxQXwzMQ8kXetNMRC44xTranBPtfNKE429W0hOL90_xTWK_SIOYIqjKZ-d_TXCsa2AjDADldDdHaqfVTMWRj--AN-IwlOs8OApMFs8r1xUxgFtqcY-Jh4GPxR39D2AgsM3zjchfgTYEN2CZWeZ9GMOs2qbc13NJeKO47EHl3rEu8PDrRa_0jw8ZLMEE1xvrkgb8hN56k-Hcs8JN8hqpI5ybygEKm0AUgUP79Sz6jvMi5IJE-J7eBoPdr7WdqxE1taeY0hF9gQZlhl8c-Su24ZHvugJewHE3zUNkxUyVkn9zBR56IXORvvCYqVbvU8dHJgb_UWV_rMU2GI5PC0OIrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf9813dda.mp4?token=VOxQXwzMQ8kXetNMRC44xTranBPtfNKE429W0hOL90_xTWK_SIOYIqjKZ-d_TXCsa2AjDADldDdHaqfVTMWRj--AN-IwlOs8OApMFs8r1xUxgFtqcY-Jh4GPxR39D2AgsM3zjchfgTYEN2CZWeZ9GMOs2qbc13NJeKO47EHl3rEu8PDrRa_0jw8ZLMEE1xvrkgb8hN56k-Hcs8JN8hqpI5ybygEKm0AUgUP79Sz6jvMi5IJE-J7eBoPdr7WdqxE1taeY0hF9gQZlhl8c-Su24ZHvugJewHE3zUNkxUyVkn9zBR56IXORvvCYqVbvU8dHJgb_UWV_rMU2GI5PC0OIrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه دختر خانومی تو تهران میره به پسرا پیشنهاد میده که با حساب خودش برن کافه، اما هیچ پسری قبول نمیکنه و دست رد به سینه این بانو میزنه.
آخر سر هم کلش خراب میشه میگه پسرا پرنسس شدن و تنها میره کافه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/71962" target="_blank">📅 21:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71961">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPc4jmr6BG-LWZF1gdcpG_fXAzAojroFMCBDo0J9O-Tu0JdqUqGmzTvAxNbaP4ersBsokfKf48oNmRkJb97iF122dAsElWvuXSqrZrLVbZD5hOMNqDFniLa3HcULSasiKaIOrbnml1T8HQH_Jn93VGC8Q42i3tKu9PE7dOYwZUZ-CHUMlfG63R_LIUVdCpCuF8TBuvIPX7CAMB39akSMmtd7CdhbiIDxezTr_3xti5oZUQnnf13tegXPanQZJ8fu4wbKeyWiEG6GFMnGNin-V52-iIGqqGH9OTMRjUwmWsAOm2BEZfMwzTKvQEXc-Kyvenojx-och6fzJsFnXsAVJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ در تروث سوشال
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/71961" target="_blank">📅 20:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71959">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10eceadf6.mp4?token=e5WPSkHxLlq6At_iAHddtvY71HYFbxmIqiI5Tgx1Ei1vzogR2mHlRoTwYqN3XaUZaVKHECD4yzk_baY9NN7M4bLU-7606oTairYwdG8bCN8WFbdhh8rfMBtxxDoeTm1yzjlydEOGiy6njVwXJaTmgvbQ_ec5fQiwEqzCz3qGZCvVB4tg9_vD7YoNlb7pM07VL5Z456ChhDL4tb1yvoi7_UJReuRdHE6oy6-OnuuDPxY2O2ZtHMi5Ffw_zykNFCojXQ_XjAVDyabjbPCpjDqro-no3DvqN4uLwok3gW_ESXC58ytlVLeAb-TKGstLy0DqWEOPzp5m5_-pzZJlrt-g0yP-AvOWiG3aUvXxZjX4AfoGb-_351UHymyPkyG-fVO6KtIjronfLv9v-fupH7oPXmFCqL3xGdhBp4_sCtrHry28pDv0Q0Qzk4YlAg-uSbAo370sS7Zm8ve6GOAmJ2A6gi4OsW1PvQ6pgYDZRxUj8mWxHj-rx_L0iLC7V3AIupomzG5OSY0baRqQp6v4ngVY6xt3qI1hVqRrPZ3HYdCsC67wTs1W1WaBflFNd2oQhN3jHWXniQLCNJCg4fr8YshYPhwwLtecsGGrYA9PxFHOnJuDC2ATQ2xHRmf-unuovUceJ5Q-pgDqDin4dFuhFpvmsvPHlQv3pft7gkXM-tn8mVM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10eceadf6.mp4?token=e5WPSkHxLlq6At_iAHddtvY71HYFbxmIqiI5Tgx1Ei1vzogR2mHlRoTwYqN3XaUZaVKHECD4yzk_baY9NN7M4bLU-7606oTairYwdG8bCN8WFbdhh8rfMBtxxDoeTm1yzjlydEOGiy6njVwXJaTmgvbQ_ec5fQiwEqzCz3qGZCvVB4tg9_vD7YoNlb7pM07VL5Z456ChhDL4tb1yvoi7_UJReuRdHE6oy6-OnuuDPxY2O2ZtHMi5Ffw_zykNFCojXQ_XjAVDyabjbPCpjDqro-no3DvqN4uLwok3gW_ESXC58ytlVLeAb-TKGstLy0DqWEOPzp5m5_-pzZJlrt-g0yP-AvOWiG3aUvXxZjX4AfoGb-_351UHymyPkyG-fVO6KtIjronfLv9v-fupH7oPXmFCqL3xGdhBp4_sCtrHry28pDv0Q0Qzk4YlAg-uSbAo370sS7Zm8ve6GOAmJ2A6gi4OsW1PvQ6pgYDZRxUj8mWxHj-rx_L0iLC7V3AIupomzG5OSY0baRqQp6v4ngVY6xt3qI1hVqRrPZ3HYdCsC67wTs1W1WaBflFNd2oQhN3jHWXniQLCNJCg4fr8YshYPhwwLtecsGGrYA9PxFHOnJuDC2ATQ2xHRmf-unuovUceJ5Q-pgDqDin4dFuhFpvmsvPHlQv3pft7gkXM-tn8mVM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کشتی «لوچینگ یوان‌یو ۱۰۸» با پرچم چین و یک کشتی باری با پرچم پاناما در نزدیکی سواحل سنگاپور با یکدیگر برخورد کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/71959" target="_blank">📅 20:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71958">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4d61320a9.mp4?token=YHHZ_WUWtzqpfo1t4EhQG2iex8A2sIvAk-NIa0aEiW3ifCioJl7-v8bgKyFAgJqvXRFm79xHkjatETUmbS8Xjic4XfGpI25nX027cB67Z4y-iqUaVs7T6zT8o4nFkTFiTze9vMUEY2HgcMCDDMM6tOJf6gUFf_4yfYS6D0knUvTIri8PpJqPyk6EQ7pcXzxgk7s8jsEBwmLdgdGvguH11P0ItFYY0kXTRFlLIDxO1Rq12FGaXKrLPTrIxl-PJgNW752nGY6p1ZwN59fbgM4cZSVYtHKRZi4kSx52KDVY1buaGzhZfJ83MFQyI8ImSLgioVgEob5EGatvPddxHl7TUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4d61320a9.mp4?token=YHHZ_WUWtzqpfo1t4EhQG2iex8A2sIvAk-NIa0aEiW3ifCioJl7-v8bgKyFAgJqvXRFm79xHkjatETUmbS8Xjic4XfGpI25nX027cB67Z4y-iqUaVs7T6zT8o4nFkTFiTze9vMUEY2HgcMCDDMM6tOJf6gUFf_4yfYS6D0knUvTIri8PpJqPyk6EQ7pcXzxgk7s8jsEBwmLdgdGvguH11P0ItFYY0kXTRFlLIDxO1Rq12FGaXKrLPTrIxl-PJgNW752nGY6p1ZwN59fbgM4cZSVYtHKRZi4kSx52KDVY1buaGzhZfJ83MFQyI8ImSLgioVgEob5EGatvPddxHl7TUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک هموطن به مایک جانسون رئیس مجلس نمایندگان آمریکا:
لطفا کار مربوط به ایران را تمام کنید
۸۰ میلیون ایرانی منتظر شما هستند
مایک جانسون:
میدونم ، قطعا و علامت پیروزی
✌🏻
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/71958" target="_blank">📅 19:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71957">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b0937658f.mp4?token=OzGoPDj98vrRzy5L9-S9ohXmlZz4VPUbMOMPIbpsV1uK1k96jWdJzmXRj0WY_r4v_RV-zz5nD5MqdXzNwdDc7aghr23HYrs-4T8DL9kqB7Ay9Hm8sqzHLBgM0QwR2s564NG7RLCU0XRSnC29T4GAPQHgHoliPw6KdyVXak6tTNUo6CHaeR4ZBat_VShxFyAQDn-yXBfJovGRIlPHOP1IYkItECsbJSyHPhyFgzYgrubBQyN3fp9-Fkxxz2qcVBpCJ-7y4MhexP0u_RMMtG6VQrE5geonHvaJOwoVPmMOmnBlZDDdLdDE9uPWbJS6nyHZnxH2KO8t5irZo--6_1s4Mm-VRpXzZM5LZvXTSumZsVchx32ynCpBxFJvySTxtSa9GCru94ukN3dG_lQSR-VqLCgYHW8ifCD4RgWbZxUEq_7D12CMGsOCvepu2zNC08DKm6OaQx0UmUEQsOp7AJwHe5k7AHC_Heula37hVjKn4Xxx5Dgy6mxStIlSepOdvimVQXJtC_sLpPvrBZFI6WgSWpB2rLANBVPo5HEgVRxUPpeq2_x0SCC_bNj9BzL-OWtCdjxKa6h_fmWlOE_fdi8YhxfiWYlqCZrsjkaaQbrK6f3J8SYuqEutkYCDfu9P9FMXmHnhbnPmOoz7mNNwPElpg3ID1cYUO88lO8QWLuIlzT8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b0937658f.mp4?token=OzGoPDj98vrRzy5L9-S9ohXmlZz4VPUbMOMPIbpsV1uK1k96jWdJzmXRj0WY_r4v_RV-zz5nD5MqdXzNwdDc7aghr23HYrs-4T8DL9kqB7Ay9Hm8sqzHLBgM0QwR2s564NG7RLCU0XRSnC29T4GAPQHgHoliPw6KdyVXak6tTNUo6CHaeR4ZBat_VShxFyAQDn-yXBfJovGRIlPHOP1IYkItECsbJSyHPhyFgzYgrubBQyN3fp9-Fkxxz2qcVBpCJ-7y4MhexP0u_RMMtG6VQrE5geonHvaJOwoVPmMOmnBlZDDdLdDE9uPWbJS6nyHZnxH2KO8t5irZo--6_1s4Mm-VRpXzZM5LZvXTSumZsVchx32ynCpBxFJvySTxtSa9GCru94ukN3dG_lQSR-VqLCgYHW8ifCD4RgWbZxUEq_7D12CMGsOCvepu2zNC08DKm6OaQx0UmUEQsOp7AJwHe5k7AHC_Heula37hVjKn4Xxx5Dgy6mxStIlSepOdvimVQXJtC_sLpPvrBZFI6WgSWpB2rLANBVPo5HEgVRxUPpeq2_x0SCC_bNj9BzL-OWtCdjxKa6h_fmWlOE_fdi8YhxfiWYlqCZrsjkaaQbrK6f3J8SYuqEutkYCDfu9P9FMXmHnhbnPmOoz7mNNwPElpg3ID1cYUO88lO8QWLuIlzT8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعاتی پیش، یک موشک رهگیر پدافند هوایی اوکراین در حومه کی‌یف موفق به اصابت به پهپاد جت‌سوز روسی «گران-۵» (Geran-5) نشد و این پهپاد لحظاتی بعد به هدف برخورد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71957" target="_blank">📅 18:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71954">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12842b3342.mp4?token=IPMLtNKFKJVCYJrAtzDwWOKrW_Bnu_gvzac64G1bUQ1cZKhLZeDuTNdFLWrPjXdGbpwzGDwlpLRwpkXIbc7mFj1t8vMv2hdpdPq3jv91Xh4dKGYzMDmOE5TJjPNv0dHvj7vsgMEGlATXhkaZgxdMVxhFGMvQZfxzMh_IlP27hbjxYK5CjnjH2oYM1BYRX2HLprkmya5v0u3EZ8cGIpqkXbTAvfO8-hJPhbmZNkAO4p9IB7xiqQNFxgIFUVWzpu86X_Okg6LGZhCORi-KZpyyypNC-fYeVmawD2kuSZmaq_W4oP0S61-i8IIQ-3VJqbFdGFbhuNfdTkuvXOK1pbsWZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12842b3342.mp4?token=IPMLtNKFKJVCYJrAtzDwWOKrW_Bnu_gvzac64G1bUQ1cZKhLZeDuTNdFLWrPjXdGbpwzGDwlpLRwpkXIbc7mFj1t8vMv2hdpdPq3jv91Xh4dKGYzMDmOE5TJjPNv0dHvj7vsgMEGlATXhkaZgxdMVxhFGMvQZfxzMh_IlP27hbjxYK5CjnjH2oYM1BYRX2HLprkmya5v0u3EZ8cGIpqkXbTAvfO8-hJPhbmZNkAO4p9IB7xiqQNFxgIFUVWzpu86X_Okg6LGZhCORi-KZpyyypNC-fYeVmawD2kuSZmaq_W4oP0S61-i8IIQ-3VJqbFdGFbhuNfdTkuvXOK1pbsWZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به گزارش رویترز، سامانه‌های پدافند هوایی در اربیل (واقع در اقلیم کردستان عراق) یک پهپاد را در نزدیکی فرودگاه اربیل سرنگون کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71954" target="_blank">📅 18:17 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71953">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">رئیس کمیسیون امنیت ملی:
دخل و خرج زندگی مردم آمریکا با هم نمی‌خواند و آمریکایی‌ها در مسائل داخلی به جان هم افتاده‌اند
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71953" target="_blank">📅 18:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71952">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71952" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71952" target="_blank">📅 18:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71951">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bXNg0f7PiuyHQk6vuSmcUNfc_nGY-x9TZlK-qeknxZ4-Hn2jvdwjbckGKjPs8pbaWvDPum2nf7Yv8AB-2r3iPy5psk_hbsJ_HptvuoCae4hMufGgvH3_NH8zWAu5fOKZD-76IZ_iAXf76J72Hjep1VNe7Hm7bDMHNZPzq_plcFdOzMU0McRr4JVDMTjR3zVhqFTARjB89y-BzLoyfFiIyOY7zWSiS-4nWhLDyI24r4EufdHkK_gA7KxutxX79M_g7M7ZuJuPwdX52v55-77sHM5wq0Yp7Lqkn45iKFTR9zn4pnsaMRQto3BafWrxQ3bbUvfyR0DohZSYotYT3pw2Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71951" target="_blank">📅 18:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71950">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ea24117fc.mp4?token=dPvLvkQk8g-pFS6fcp_ZriyzIq9TyeFpVuXJhi2Wt-nqwqvyOe392Ed6KVUsnVuDWmhuq57_xAuSDpVdt1jvpywyVHnf6i8XTEnOQY5VaAS19e6Sd7mxFC-f6fAjaRNUllpxC9AHCJ1bW52vORhX2eEeDw_h9hui-Xjfym_12kpmUwQyGTz2aU1-1BcjUZ_8-XTV7CZhnhZxdtuwSmIc9Z2-fiXBzSRBE5aUrDdTlJ1ADr6DSf07Hois0Krxdl3d_NxSWxaNnQW-4AvF8AS476edNWQiMCaUGR9xcnZpL5H-yUakmxOqm1kru28hc6g0FTjraeHmRdX_kZkkefnKhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ea24117fc.mp4?token=dPvLvkQk8g-pFS6fcp_ZriyzIq9TyeFpVuXJhi2Wt-nqwqvyOe392Ed6KVUsnVuDWmhuq57_xAuSDpVdt1jvpywyVHnf6i8XTEnOQY5VaAS19e6Sd7mxFC-f6fAjaRNUllpxC9AHCJ1bW52vORhX2eEeDw_h9hui-Xjfym_12kpmUwQyGTz2aU1-1BcjUZ_8-XTV7CZhnhZxdtuwSmIc9Z2-fiXBzSRBE5aUrDdTlJ1ADr6DSf07Hois0Krxdl3d_NxSWxaNnQW-4AvF8AS476edNWQiMCaUGR9xcnZpL5H-yUakmxOqm1kru28hc6g0FTjraeHmRdX_kZkkefnKhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
برخی از مقامات ایرانی همچون موش‌ها پنهان شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71950" target="_blank">📅 17:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71949">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ درباره ایران:  در «مرحله تصمیم‌گیری» هستم و در آینده‌ای نه چندان دور، اتفاقات بسیار بزرگی رخ خواهد داد.  گزینه‌ها عبارتند از: نابودی کامل ایران، رها کردن آن‌ها تا از نظر اقتصادی بپوسند، یا دستیابی به توافق.  بهتر است درست رفتار کنند!  @News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71949" target="_blank">📅 17:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71948">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0471fa6ac.mp4?token=SKolgHdKNnYmfvNhjk6ZRPP5OPPjZNTxhZopeuooi2EB81-cq2b_ezMUtl1i9oXiuZEKBOf_nGP7_eHWtPeo1uCQObm_CAs-j6VS0hn11NyYcArovr-wpnhEMmdMyzJDLF77aEjmoCXYfGaQAnpl6PFP-WvL1HosMFgn4Alk8S65PguTy8-HCPT6ER_UEvACLlM5FLHTr9TNqX9QHGiXfLV7I-FtQbBqAWWB7We1dCQJYl6WQF9FAPR2qPjd-HfnUEtNWNpOUBC339stOxpW887by4lsxmy721rraWimbotfcCEgfEuaioCxSooRb8BlJrtM7sWUrqDA9foxd7gD8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0471fa6ac.mp4?token=SKolgHdKNnYmfvNhjk6ZRPP5OPPjZNTxhZopeuooi2EB81-cq2b_ezMUtl1i9oXiuZEKBOf_nGP7_eHWtPeo1uCQObm_CAs-j6VS0hn11NyYcArovr-wpnhEMmdMyzJDLF77aEjmoCXYfGaQAnpl6PFP-WvL1HosMFgn4Alk8S65PguTy8-HCPT6ER_UEvACLlM5FLHTr9TNqX9QHGiXfLV7I-FtQbBqAWWB7We1dCQJYl6WQF9FAPR2qPjd-HfnUEtNWNpOUBC339stOxpW887by4lsxmy721rraWimbotfcCEgfEuaioCxSooRb8BlJrtM7sWUrqDA9foxd7gD8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس نیوز به نقل از ترامپ:
ترامپ می‌گوید «احتمالاً» برای دیدار با مسعود پزشکیان، رئیس‌جمهور ایران، در حاشیه مجمع عمومی سازمان ملل آمادگی دارد
😂
پزشکیان هفته آینده در نیویورک خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71948" target="_blank">📅 17:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71947">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6e65f0569.mp4?token=pITFxTs2aGCbyhCbLh9x3XovmVvNg7dKuiDQsKgsnKc1bpQllL2UR71IDcGt9Qdt7W9EotI8rtKbdKNHAnmCF_ap7SBeB0cvIfieJeDwdRntydKsz83sa-QowA4SwP_soGo-ILCingEJex6TVJUk-1Yvq6_Um96vomdKKg7J561UUkUcuWevrjvz813bss4YQznaOVT8g6dEO5zE_RhPytyjZVa7nE9AIoUxZi8ImgtN_5IL8690Ya13ceCVEMY7NpeV1ZNt7KEePDNI0intHN-ef-ALDhyazXrN6eWgkShKMrvRQTHTOLMru4991YF_vKGBhrhlRh6oPCYqJGFA-YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6e65f0569.mp4?token=pITFxTs2aGCbyhCbLh9x3XovmVvNg7dKuiDQsKgsnKc1bpQllL2UR71IDcGt9Qdt7W9EotI8rtKbdKNHAnmCF_ap7SBeB0cvIfieJeDwdRntydKsz83sa-QowA4SwP_soGo-ILCingEJex6TVJUk-1Yvq6_Um96vomdKKg7J561UUkUcuWevrjvz813bss4YQznaOVT8g6dEO5zE_RhPytyjZVa7nE9AIoUxZi8ImgtN_5IL8690Ya13ceCVEMY7NpeV1ZNt7KEePDNI0intHN-ef-ALDhyazXrN6eWgkShKMrvRQTHTOLMru4991YF_vKGBhrhlRh6oPCYqJGFA-YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
در «مرحله تصمیم‌گیری» هستم و در آینده‌ای نه چندان دور، اتفاقات بسیار بزرگی رخ خواهد داد.
گزینه‌ها عبارتند از: نابودی کامل ایران، رها کردن آن‌ها تا از نظر اقتصادی بپوسند، یا دستیابی به توافق.
بهتر است درست رفتار کنند!
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71947" target="_blank">📅 17:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71946">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3687d7bcf.mp4?token=qLwIUsvPymQIVqMeP77A6QHMzKO58kVdmdwVwAvEahWmLK8lnRmXrs2Iag0dRqMu4WL1ZCDTSDxo4djuK38M53Ng6tH57ZuviurvpHDX5NMHgSHeGh4me7y4h_USnboY1IEfPTfANKoY9xbSMxT-R91N_EUHC-AfeeG6SzG1Yl04RARp2pUzyTS00O1L4yCmODxYdrO45Ij6OHO9ViG2MkXymIUwi-GlY7imYhY4Bg44MXHzPKAR22mKJWs1jrklGN8TLcjMYSoxDZx5V01HFTn2jjFrtNXt3RAHt2mwClojxNug7oHH2wYvwfFQ86AerB5nGUpX1A5GOfmgGi5OJTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3687d7bcf.mp4?token=qLwIUsvPymQIVqMeP77A6QHMzKO58kVdmdwVwAvEahWmLK8lnRmXrs2Iag0dRqMu4WL1ZCDTSDxo4djuK38M53Ng6tH57ZuviurvpHDX5NMHgSHeGh4me7y4h_USnboY1IEfPTfANKoY9xbSMxT-R91N_EUHC-AfeeG6SzG1Yl04RARp2pUzyTS00O1L4yCmODxYdrO45Ij6OHO9ViG2MkXymIUwi-GlY7imYhY4Bg44MXHzPKAR22mKJWs1jrklGN8TLcjMYSoxDZx5V01HFTn2jjFrtNXt3RAHt2mwClojxNug7oHH2wYvwfFQ86AerB5nGUpX1A5GOfmgGi5OJTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهراب قاسم‌خانی نویسنده سریال پاورچین :
تو سریال یه اصطلاحی بین مهران مدیری و سحر زکریا ( نقش زن و شوهر ) بود که درباره " کوه رفتن " به هم میگفتن؛
مثلا زکریا به مدیری میگفت بیا بریم کوه، یا میگفت تو اوایل ازدواجمون بیشتر میومدی کوه،
ولی اصلا موضوع کوه نبود و داشتن درباره رابطه‌شون صحبت میکردن.
بعد از 5,6 قسمت مسئولان صداوسیما متوجه شدن و دیگه اجازه ندادن این دیالوگ تو سریال رد و بدل بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71946" target="_blank">📅 17:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71945">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/152e7c05de.mp4?token=JRGgbgH7_o3tlpP0odwIppecypO9Ad4m839ci8U9fQgB6f_0m6LFpcqFczWYh_XhaFPAanFWrNUlWJgfVHo8HgZH9o4_yjnpdp_MbHzZq-RpqD81IaxIdQ1kdSKSUrUlBlOuvhRqtU7ilyd6Sm8crHdJoO_ScPF15ie0kS2p7OfB02ygGfdNg3MHgxgCcfRs4ICoWSZBmzH8d54F9BV6ZRuRR3LOY3cPeXayUqc3kvO6MP-KE42ib1QnFsqaY7cfChNA6FildbExBRu6YdizQ0db6AO4XT4TD3HtzD2g16IxzO2QFhRPBQYLs3FIpL0mtd_0r0C3PhLher5kCRFKSIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/152e7c05de.mp4?token=JRGgbgH7_o3tlpP0odwIppecypO9Ad4m839ci8U9fQgB6f_0m6LFpcqFczWYh_XhaFPAanFWrNUlWJgfVHo8HgZH9o4_yjnpdp_MbHzZq-RpqD81IaxIdQ1kdSKSUrUlBlOuvhRqtU7ilyd6Sm8crHdJoO_ScPF15ie0kS2p7OfB02ygGfdNg3MHgxgCcfRs4ICoWSZBmzH8d54F9BV6ZRuRR3LOY3cPeXayUqc3kvO6MP-KE42ib1QnFsqaY7cfChNA6FildbExBRu6YdizQ0db6AO4XT4TD3HtzD2g16IxzO2QFhRPBQYLs3FIpL0mtd_0r0C3PhLher5kCRFKSIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاشار سلطانی :
100 میلیون بشکه نفت تو مملکت گم شده !
کسی که مسئول نظارت رو این موارد بود بهم گفته که 100 میلیون بشکه نفت رو نمیدونیم چی شده. نه تو دریا ریخته شده، نه امریکا تحریمش کرده و نه دزدای دریایی دزدیدنش.
به نیروی مسلح، قرارگاه فلان‌جا، نیروی انتظامی و ستاد کل چه ربطی داره که همشون دارن نفت میفروشن؟
اطلاعاتی نباید نفت بفروشه؛
اطلاعاتی سواد و فهمش رو نداره، درک نمیکنه. اطلاعاتی‌ای که 50 میلیون حقوق میگیره، میلیارد دلار، ترانزکشن، بیمه، حمل و نقل و این چیزها رو نمیفهمه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71945" target="_blank">📅 16:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71944">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1367899db.mp4?token=L42CTQEYTotWKiXBtlet7TxGC-Jk7Q27b1Ji2Wtoy-2fcObXyKnPUF9aXAa2Lj6oYaVoud-K4EOAh5q48-yDYgaN7vsq780BKvIWPu5WwL2WJ6SAnUEXqhzzoaHKzccfm18mXSRxY5vN78dnaprJAbrBgLAJ54q4NrnIHc3g9J1Z9lPbPQp8rdTOyDRzfLBaa8oFHngHJ_rbOvB8SH2GlsZeRnOYbBndmEeJGbq5WekkueWkencvifojuxVey8tridOZ41gv7yTqfcidz707c6SytihvqX0KGWNXPMHp_zESwzvPOSHSwfTq3rD-ihV1SI8zYMfLIGZTivkp4J-E5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1367899db.mp4?token=L42CTQEYTotWKiXBtlet7TxGC-Jk7Q27b1Ji2Wtoy-2fcObXyKnPUF9aXAa2Lj6oYaVoud-K4EOAh5q48-yDYgaN7vsq780BKvIWPu5WwL2WJ6SAnUEXqhzzoaHKzccfm18mXSRxY5vN78dnaprJAbrBgLAJ54q4NrnIHc3g9J1Z9lPbPQp8rdTOyDRzfLBaa8oFHngHJ_rbOvB8SH2GlsZeRnOYbBndmEeJGbq5WekkueWkencvifojuxVey8tridOZ41gv7yTqfcidz707c6SytihvqX0KGWNXPMHp_zESwzvPOSHSwfTq3rD-ihV1SI8zYMfLIGZTivkp4J-E5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساجده سلیمانی، مجری شبکه یک:
آقای جبلی میگن ۷۰ درصد مردم صداوسیما رو دنبال میکنن
والا من ۵ سال تو شبکه یک مجری بودم وقتی میرفتم بیرون جز یه مشت پیرمرد و پیرزن که صبح برای نماز بلند میشدن و تلویزیون میدیدن دیگه کسی منو نمیشناخت.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71944" target="_blank">📅 16:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71941">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebc55859ee.mp4?token=LDCLqHK6YbTvv78GLfhl7khkWrX2mzMxIcu-Yf5DT5T22mr0Vc5OVBbbBqw-zf71vKxw5sHYFP39hdAu71sIXQytI3UK-mNMMdqWeo7Ywk2xgYjvf7IT-g1UnyyBb07wavDNnqdqhHCcp_AFxPQXSNfkOLAcqdUu-MXmCz4BeItMgn2rPveLMzmpuE9o4AumpY1zleu6Fnl5U-JwQ7BOd2kdexHHr8BPRvTNTdqn7jRNYNzX8k7411j970CCWgWx3nrfq8qx0_W8i9lI0awnyp26ldUq6qmiWDnkkas14wVvZ_6AGA0hQOigdF2oHn6wdLTvfMZ3BVhiQi1CbhQUUQMWlUfDvbdQOIAwbOdL8pe7sNXp72VF9W0TfVZrBTwu1U5sHHxLHkBnxM6qnxmc74scDsS_2M0iYFxsH_4_q9jIBQBRHCO-B_y8mlyUkJvDxEOrpGJBDn3IXrql1Kq_MTdZfAq750Cbm8NHlYV_thsb3pr49O59FlR9estBM2d1rev9z9kLwWYZQgzJfpgEKGRvqxFGSTmHSFV5xx1Gh6AmSCJ8Nc0TDa5ebbviRQI-9LJ85L6Ruggu07m_EUZVBvUeLeft3SILHlh7Q6o_A2RoLARh5ti24vWHEyqT0-rSHUdng0iNAbfRqvFoa5Ab9dxikQQin_mL_VD9cxkaaXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebc55859ee.mp4?token=LDCLqHK6YbTvv78GLfhl7khkWrX2mzMxIcu-Yf5DT5T22mr0Vc5OVBbbBqw-zf71vKxw5sHYFP39hdAu71sIXQytI3UK-mNMMdqWeo7Ywk2xgYjvf7IT-g1UnyyBb07wavDNnqdqhHCcp_AFxPQXSNfkOLAcqdUu-MXmCz4BeItMgn2rPveLMzmpuE9o4AumpY1zleu6Fnl5U-JwQ7BOd2kdexHHr8BPRvTNTdqn7jRNYNzX8k7411j970CCWgWx3nrfq8qx0_W8i9lI0awnyp26ldUq6qmiWDnkkas14wVvZ_6AGA0hQOigdF2oHn6wdLTvfMZ3BVhiQi1CbhQUUQMWlUfDvbdQOIAwbOdL8pe7sNXp72VF9W0TfVZrBTwu1U5sHHxLHkBnxM6qnxmc74scDsS_2M0iYFxsH_4_q9jIBQBRHCO-B_y8mlyUkJvDxEOrpGJBDn3IXrql1Kq_MTdZfAq750Cbm8NHlYV_thsb3pr49O59FlR9estBM2d1rev9z9kLwWYZQgzJfpgEKGRvqxFGSTmHSFV5xx1Gh6AmSCJ8Nc0TDa5ebbviRQI-9LJ85L6Ruggu07m_EUZVBvUeLeft3SILHlh7Q6o_A2RoLARh5ti24vWHEyqT0-rSHUdng0iNAbfRqvFoa5Ab9dxikQQin_mL_VD9cxkaaXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از حمله گسترده پهپادی اوکراین به پالایشگاه کاپوتنیا در مسکو، روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71941" target="_blank">📅 15:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71940">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b8ac28a42.mp4?token=dGXZoenZ38szPPEKPAspk9P3jtyJ-aIL2PjggmrvjNMK02p2bynmq5ayZ8l0AQVD12IfumwkCpyE37x7tEBHq5XpwG4D18c0REF7LdDUxcHPzBZOcHY6f4fpy92_WSfns1argUC5m_D8PuQPpAKIVvrJEkhJzpXY_MFlcMMXY3uzSYzJfPUqThE5Azd4LsC7H02HHDlw7x5sJxjDJBMUSjM83pVGHxYWy3cslPhPDPKVKm4T3PGqSo14T-5FQv-wu1dJpTYGQ71l5zCbo3YEIhKi-Vig8UdBWAl9GL9-6fUMtTRv-tC5qzA2_CVeP6-KrBCJl01ORu9WGf1paQzgIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b8ac28a42.mp4?token=dGXZoenZ38szPPEKPAspk9P3jtyJ-aIL2PjggmrvjNMK02p2bynmq5ayZ8l0AQVD12IfumwkCpyE37x7tEBHq5XpwG4D18c0REF7LdDUxcHPzBZOcHY6f4fpy92_WSfns1argUC5m_D8PuQPpAKIVvrJEkhJzpXY_MFlcMMXY3uzSYzJfPUqThE5Azd4LsC7H02HHDlw7x5sJxjDJBMUSjM83pVGHxYWy3cslPhPDPKVKm4T3PGqSo14T-5FQv-wu1dJpTYGQ71l5zCbo3YEIhKi-Vig8UdBWAl9GL9-6fUMtTRv-tC5qzA2_CVeP6-KrBCJl01ORu9WGf1paQzgIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میانگین آی‌کیو یمنی‌ها:
یه حوثی پین نارنجک رو کشید واسه اینکه نشون بده خدا باهاشه و نتیجه شد این.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71940" target="_blank">📅 15:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71939">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">قرارگاه خاتم الانبیا:
هرگونه حمله به ایران، منجر به حملات «مداوم، مؤثر و دردناک» به تمامی پایگاه‌ها و منافع آمریکا در منطقه، «بدون هیچ‌گونه محدودیتی» خواهد شد.
کشورهای منطقه‌ای که با تجاوز آمریکا همراهی کنند، شریک این حمله محسوب شده و نباید انتظار خویشتن‌داری ایران را داشته باشند.
بر اساس اطلاعات دریافتی آمریکا با چراغ سبز متحدان منطقه‌ای خود و بر اساس هماهنگی‌های صورت‌گرفته در یک نشست اروپایی، در حال برنامه‌ریزی اقداماتی جدید علیه ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71939" target="_blank">📅 14:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71938">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abf3ef96ed.mp4?token=ZinFbRDa9inN927KQMWa-1lksf0xeEE1Ndcwvxsy9M3EbKTqTRCVGbGYvZyQzG6WTMYnacZhjJXChQbrndNaGy-8JLO3OAcUIaSGIlIYPsrVjtRx3Et56WnxlUADbd9166HsIkt7UwsVeKVlr3AD8wXKtW_1yciU1PkreMKeZy6Qr0Ka8X3eFtHcmM6JQ1yOiiCYbNYHvorAMVzYL1lfVlT488d5rSjj4M_7SWPlCYYvlyasWpEwiXhibKRczloAfwb054AWWy5-vlBzs4zrJ3Rv9op95rPiyIoUwjz3kI8Qu0VCUlJey87mPmdltuWPh5tvaS8VXi8mKY5Etao8lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abf3ef96ed.mp4?token=ZinFbRDa9inN927KQMWa-1lksf0xeEE1Ndcwvxsy9M3EbKTqTRCVGbGYvZyQzG6WTMYnacZhjJXChQbrndNaGy-8JLO3OAcUIaSGIlIYPsrVjtRx3Et56WnxlUADbd9166HsIkt7UwsVeKVlr3AD8wXKtW_1yciU1PkreMKeZy6Qr0Ka8X3eFtHcmM6JQ1yOiiCYbNYHvorAMVzYL1lfVlT488d5rSjj4M_7SWPlCYYvlyasWpEwiXhibKRczloAfwb054AWWy5-vlBzs4zrJ3Rv9op95rPiyIoUwjz3kI8Qu0VCUlJey87mPmdltuWPh5tvaS8VXi8mKY5Etao8lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نجمه امینی، دانشجوی ۲۳ ساله و بازداشت شده در جریان انقلاب ملی در مشهد که او را محکوم به اعدام کرده‌اند، در تماسی تلفنی از زندان وکیل‌آباد مشهد از همه مردم خواست تا صدای او باشند.
درود به مردم عزیز ایران، حکم اعدام من صادر شده، لطفا صدای من باشین، من یه جوونم با کلی آرزو.
تروخدا فقط صدای منو نشنوین، اونو نشر بدین و صدای من باشین، من بی گناهم.
شاید این آخرین صدایی باشه که از من میشنوین چون شاید دیگه نتونم حرف بزنم، ولی تنها امیدم ایران آباد و آزاده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71938" target="_blank">📅 13:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71937">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4daecc7856.mp4?token=OxfIVtK6Oz7NeA0iBmDNvIS7fnQfoCR06slI6sRqRM275qjsfOtsm1x0PSC5SUmv9ZaEDoleCdBbp6SxneZzorlDUxgVzgf2BMuETcu6gM5OdRnofTdsv8yPuqGpbRbKDJtnK2HVC2JuukVanqOASuipwaxKIo5AKic0QfJ8xTjB1lR3WOH2Q8TVgUYToguNftqd15-fsruAoZD9FbsTNEjrCNErmD7yQdTcyyMOsRCINnBrceJ7ovlAr6KPq68LAD6c488Q7GkVsLI_ByIU6R3y3IH9NBuWQ1zkNUDuYsOTlHX76-zwL-M0r1YXorRtxFz3XlL_Roqjvx9kzphpeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4daecc7856.mp4?token=OxfIVtK6Oz7NeA0iBmDNvIS7fnQfoCR06slI6sRqRM275qjsfOtsm1x0PSC5SUmv9ZaEDoleCdBbp6SxneZzorlDUxgVzgf2BMuETcu6gM5OdRnofTdsv8yPuqGpbRbKDJtnK2HVC2JuukVanqOASuipwaxKIo5AKic0QfJ8xTjB1lR3WOH2Q8TVgUYToguNftqd15-fsruAoZD9FbsTNEjrCNErmD7yQdTcyyMOsRCINnBrceJ7ovlAr6KPq68LAD6c488Q7GkVsLI_ByIU6R3y3IH9NBuWQ1zkNUDuYsOTlHX76-zwL-M0r1YXorRtxFz3XlL_Roqjvx9kzphpeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی:
اسرائیلی‌ها تونل‌های خالی در لبنان را برای اهداف تبلیغاتی و نمایش انتخاباتی منفجر کردند. آن‌ها عکس و فیلم گرفتند و گفتند: «ببینید نتانیاهو چقدر قدرتمند است.»
همه این‌ها تبلیغات است و همگی به انتخابات مربوط می‌شود.
اما کار ما مبتنی بر اصول است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71937" target="_blank">📅 12:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71936">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ea49a57b9.mp4?token=U_NszTG3ff_9APg6bPKKIO0oQb-7-mp6h1qlsYUBDT0ojnCpBXFY586plMoH79pl93vOWrjHJ73yqmbb213MWb7lXZwdzbsLsuGmiYXyQ-eBBkcvR2tqJE2jkz7FdBBA8a-Ti0ZmsPY8KmBVc-giWJNqmYccJ0q2PjoofGHS0JhB11arEwWwJs77_bxD4QJ9WWjdh8M2S4L_Woy9WTrn7y3D37mWfgDuIU1DF52B2mX-EKiINa3nAIYiadIA2u5zoA4imRKAlCRkshiPdZAOaurAIdeo6yJFgkF1Sp4_hcos9qgFFmacAr59Jsaze7nQBJj5eYHkZcI8lskhwlca6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ea49a57b9.mp4?token=U_NszTG3ff_9APg6bPKKIO0oQb-7-mp6h1qlsYUBDT0ojnCpBXFY586plMoH79pl93vOWrjHJ73yqmbb213MWb7lXZwdzbsLsuGmiYXyQ-eBBkcvR2tqJE2jkz7FdBBA8a-Ti0ZmsPY8KmBVc-giWJNqmYccJ0q2PjoofGHS0JhB11arEwWwJs77_bxD4QJ9WWjdh8M2S4L_Woy9WTrn7y3D37mWfgDuIU1DF52B2mX-EKiINa3nAIYiadIA2u5zoA4imRKAlCRkshiPdZAOaurAIdeo6yJFgkF1Sp4_hcos9qgFFmacAr59Jsaze7nQBJj5eYHkZcI8lskhwlca6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رضایی:
پرسش من از مقامات عرب این است: اگر ایران مقاومت نمی‌کرد و ناچار به تسلیم می‌شد، آیا اسرائیل امروز به عربستان سعودی حمله نمی‌کرد؟ آیا اسرائیل تا دمشق پیشروی نمی‌کرد؟ آیا اسرائیل به عراق حمله نمی‌کرد؟
ما در اینجا شهید دادیم و از کشورهای عربی دفاع کردیم. اگر بینی آمریکا و اسرائیل را در اینجا، در ایران، به خاک نمی‌مالیدیم و اگر آن‌ها در ایران احساس پیروزی می‌کردند، دیگر کسی در منطقه باقی نمی‌ماند که بتواند در برابرشان بایستد.
اسرائیل به تمام کشورهای عربی حمله می‌کرد و آمریکا نیز از آن حمایت می‌نمود. ما مقاومت کردیم — بله، ما از کشور خودمان دفاع کردیم — اما دفاع ما به نفع کشورهای عربی نیز تمام شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71936" target="_blank">📅 12:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71935">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c2df1caeb.mp4?token=HNPOd4LACrwpnkrB2pDHiDiA7Q-fjW9tcUrfp5cYw3nRMVcO1QPnriuYqEj8su_7UdzmIs4TbjXPEYOTqn7XYrycBqQtO4aHLiOHBdVo9_eq2EFMMXcJGeGJUee-ZQO3VGVfHjCyy-oS_0pxLDqXywgQkWha0CuyaTJj_asSSZYI5XUO-5ilpIwhCiZlQxU5dmooIVFwhUTDsWgVTefuKfUSjTUGsOmIFTmNd-BMj-y-4CXx_ZR-Ij1C3rUafZn3qVjlZOpxPOXr7V3-JXchjZnbP0_gmvMs2pjRnG8ddLHA_f7tYHTUK8QS7oTdJ4B3yeZkDMAMGubA7uEK3FUzKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c2df1caeb.mp4?token=HNPOd4LACrwpnkrB2pDHiDiA7Q-fjW9tcUrfp5cYw3nRMVcO1QPnriuYqEj8su_7UdzmIs4TbjXPEYOTqn7XYrycBqQtO4aHLiOHBdVo9_eq2EFMMXcJGeGJUee-ZQO3VGVfHjCyy-oS_0pxLDqXywgQkWha0CuyaTJj_asSSZYI5XUO-5ilpIwhCiZlQxU5dmooIVFwhUTDsWgVTefuKfUSjTUGsOmIFTmNd-BMj-y-4CXx_ZR-Ij1C3rUafZn3qVjlZOpxPOXr7V3-JXchjZnbP0_gmvMs2pjRnG8ddLHA_f7tYHTUK8QS7oTdJ4B3yeZkDMAMGubA7uEK3FUzKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی:
آمریکا و ترامپ خواهند رفت. همه می‌دانند که اقتصاد آمریکا در واقعیت، در مسیر فروپاشی قرار دارد. آمریکا طی ۱۰ سال آینده، دیگر آن کشوری نخواهد بود که امروز هست.
اما ما و کشورهای عربی باقی خواهیم ماند. ما خودمان باید وضعیت منطقه را سامان دهیم. ما باید امنیت خلیج فارس را برقرار کنیم، پیمانی برای همکاری اقتصادی شکل دهیم و در منطقه با یکدیگر دوست باشیم.
ما یک خانواده هستیم؛ خانواده خلیج فارس. ما هشت کشوریم و باید بر بازسازی و توسعه اقتصادی تمرکز کنیم، با یکدیگر همکاری داشته باشیم، در سرمایه‌گذاری‌های هم مشارکت کنیم و حتی به سمت ایجاد واحد پولی مشترک و بازار مشترک واحد حرکت کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71935" target="_blank">📅 12:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71934">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed047a6e6.mp4?token=Bt0sTAuViGrihMm0mZJrSAA8Hhq7Yf3M4Ouq4QEFnyG8Ocgxa-eKN0EfnZ9phH5cWHXYyacU0npdzQTvQ4dvFxpisN3GUhHtw54aZRlZ3HWK9ffdQjmhTP3oVr8Z9if7pjU5EZOBQkJR0xFTgwQunmtiGs-IIzkwrzefp7mFDlXRlarM0A0IO-sGg57fsEuFbwZUCXCMcYuKDeVaO1zqjah-EoIlg1bLaQ-MU_2RTugfs0-or4OqFKZzsi0BrE9L0IzNFLS1DYnHR_NUzV9GiIYSz6_970LsVckXOANBbSSBjRvtft5qekZ_NdQAjjrfq8X040OnPGub-K8iwls1XBuA1k6QggttlyGz4EvlfP5PKosq9PHRDAK-bOCNnlOT4K4lkVl0Jcj71l3QzVmIuDTUk5g0fw6wA-8p6bspUnYy-iorGOJYWx2mFtOUC5JSAVVTPvcEtOfowwoB5cqdfDbMtvdjq6sMMIC1MZ5XnMLJKUaYvGD41US1p53GqCXxlUM64YLHSXXPTIgZVInxkw7DKOL00nY5cw_RJxD67knl6XR8uw0UEgJ54r6MW6-GzL5xo6GXBZGjhUkNmSDnrHIzmw8fWbuKP5CDBnmmwgENu4ZCnkemDBwTHPWmyQbafn7tosg7Mlc7Sbn-pNsYYzawxX4dckGy_AZ8ZszUbSs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed047a6e6.mp4?token=Bt0sTAuViGrihMm0mZJrSAA8Hhq7Yf3M4Ouq4QEFnyG8Ocgxa-eKN0EfnZ9phH5cWHXYyacU0npdzQTvQ4dvFxpisN3GUhHtw54aZRlZ3HWK9ffdQjmhTP3oVr8Z9if7pjU5EZOBQkJR0xFTgwQunmtiGs-IIzkwrzefp7mFDlXRlarM0A0IO-sGg57fsEuFbwZUCXCMcYuKDeVaO1zqjah-EoIlg1bLaQ-MU_2RTugfs0-or4OqFKZzsi0BrE9L0IzNFLS1DYnHR_NUzV9GiIYSz6_970LsVckXOANBbSSBjRvtft5qekZ_NdQAjjrfq8X040OnPGub-K8iwls1XBuA1k6QggttlyGz4EvlfP5PKosq9PHRDAK-bOCNnlOT4K4lkVl0Jcj71l3QzVmIuDTUk5g0fw6wA-8p6bspUnYy-iorGOJYWx2mFtOUC5JSAVVTPvcEtOfowwoB5cqdfDbMtvdjq6sMMIC1MZ5XnMLJKUaYvGD41US1p53GqCXxlUM64YLHSXXPTIgZVInxkw7DKOL00nY5cw_RJxD67knl6XR8uw0UEgJ54r6MW6-GzL5xo6GXBZGjhUkNmSDnrHIzmw8fWbuKP5CDBnmmwgENu4ZCnkemDBwTHPWmyQbafn7tosg7Mlc7Sbn-pNsYYzawxX4dckGy_AZ8ZszUbSs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی:
اگر آمریکایی‌ها جدی هستند، بگذارند سربازانشان بیایند و وارد ایران شوند. چرا وارد نمی‌شوند؟
در جنگ‌ها، این نیروهای زمینی هستند که همیشه حرف آخر را می‌زنند.
چرا لشکر‌های هوابرد نمی‌آیند؟ چرا نیروهای زمینی آمریکا وارد ایران نمی‌شوند؟ چرا فقط از آسمان بمباران می‌کنند و سپس می‌روند؟
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/71934" target="_blank">📅 12:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71933">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f4920ecc6.mp4?token=ubGQF_XY3SJFBY1GJTZaH4MSAZvYPSDaaEiVW_btBZoVLK8S_7OPCyK9T2dor-lum5oHbrY-QlT_2GhSwgUaGCBWjLOJgnFiE5Mn3ebTXNnNTTSUATCIA-REmWyzaWj-aP6ZT2Pn2G1_ueeEsj7u6T1zh1Yi6DrEifm7n4tWbtB7o4vG_4WXQy_fqVvhAMCtkw7-wvSxtvxRX_DkibCV_Rk5Uz2alLuGbHh_psUbzXwDGhHLRjlsd0A6m2ne9PyKO3cPWSPUW9F-xmoVU3lXInkkz7Ny0i1fDvyo1F4SNhl1kdGALEYmIzYqSoMrfIGBI51Dp0runeFnQXExLiYocA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f4920ecc6.mp4?token=ubGQF_XY3SJFBY1GJTZaH4MSAZvYPSDaaEiVW_btBZoVLK8S_7OPCyK9T2dor-lum5oHbrY-QlT_2GhSwgUaGCBWjLOJgnFiE5Mn3ebTXNnNTTSUATCIA-REmWyzaWj-aP6ZT2Pn2G1_ueeEsj7u6T1zh1Yi6DrEifm7n4tWbtB7o4vG_4WXQy_fqVvhAMCtkw7-wvSxtvxRX_DkibCV_Rk5Uz2alLuGbHh_psUbzXwDGhHLRjlsd0A6m2ne9PyKO3cPWSPUW9F-xmoVU3lXInkkz7Ny0i1fDvyo1F4SNhl1kdGALEYmIzYqSoMrfIGBI51Dp0runeFnQXExLiYocA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی:
اگر جنگی دوباره آغاز شود، کشتی‌های آمریکا — مگر اینکه اقیانوس هند را ترک کنند — در هر کجای این اقیانوس که باشند، هدف حمله قرار خواهند گرفت. ما به این توانمندی‌ها دست یافته‌ایم.
ما سرعت موشک‌های هایپرسونیک (مافوق صوت) خود را از ۶ ماخ به ۱۰ ماخ افزایش داده‌ایم.
همچنین سامانه‌های جنگ الکترونیک خود را توسعه داده و پدافند هوایی‌مان را ارتقا بخشیده‌ایم؛ علاوه بر این، تدابیر دیگری نیز داریم که در زمان مناسب از آن‌ها استفاده خواهیم کرد.
بنابراین، ما کاملاً آماده‌ایم. اگر آمریکا جنگی را آغاز کند، با نیرویی بیشتر و ضرباتی پرتعدادتر و دردناک‌تر با آن مقابله خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/71933" target="_blank">📅 12:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71932">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71932" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/71932" target="_blank">📅 12:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71931">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4RUVMFR45u3ENIoqNMfDFx6Ojp9nlsmcsf3sbfNaklBFnwhSn1Fg1ppq1gKUyt2p7iDjvEVcMHjwaw5WGvoigFn_ry1NN6OxzZXPkIc4VYulCTVTObYMf6ZM41App9Yaq6aYtquzIltoz5ia14MV2GPE9vpC0UxCe-iWin7XUwExZE2TMGzywucVuQAZzU1iUqDEUB9MbpHvKZqaOQyPHtCE12INCrt2NHyLbfkjl-KvCdiNeOww2h_3lEVpTr0yEHzBJMBe9xf7BQRjcCHlgblGfbdLam6ucKMkyGBrEWTIqK3BDGhe52ceJrSEC0wPtrz3ESUeLbarabzxFk1Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
رویارویی غول‌های مادرید!
🦖
نبرد هیجان انگیز رئال مادرید
🆚
اتلتیکو مادرید را در
TrexBet
پیش‌بینی کنید!
📉
نگاهی به آمار ۵ رویارویی اخیر دو تیم:
رئال مادرید: ۳ برد، ۲ شکست و ۹ گل زده
اتلتیکو مادرید: ۲ برد، ۳ شکست و ۱۰ کل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71931" target="_blank">📅 12:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71930">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf2e9358bf.mp4?token=Kl71FwO-iIUGdCP_jYrIL0Y5VHyX6xA31Ab0hPX-ZVLzp1kljBBhXKjefQgMcnxnqqMC6PuCLFx2PvydRUON2MCzvVLxrYPuTIftuZgnmFTlT_r_i_u1Xk1IGp8IcEHUax03B1VwWPom5ZcI0L1yLbJkCpbpnRJ6-kcbcM3qkFuZYJ18AokoaGBZBDRWyLLhSVOWYGLNiVg-fgyPGci2dC4t9X5F4sZJDuoVBNVJywxIRe4vsdlJzYeilZLs2W8gsL5sBVZTEMIUy5AjeQjU5ikG_zdrKs04pdcN9gKPOwRJrpFlWdfFPMj8krZgeepEOrwfWGA2TuIljSGNX0BfSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf2e9358bf.mp4?token=Kl71FwO-iIUGdCP_jYrIL0Y5VHyX6xA31Ab0hPX-ZVLzp1kljBBhXKjefQgMcnxnqqMC6PuCLFx2PvydRUON2MCzvVLxrYPuTIftuZgnmFTlT_r_i_u1Xk1IGp8IcEHUax03B1VwWPom5ZcI0L1yLbJkCpbpnRJ6-kcbcM3qkFuZYJ18AokoaGBZBDRWyLLhSVOWYGLNiVg-fgyPGci2dC4t9X5F4sZJDuoVBNVJywxIRe4vsdlJzYeilZLs2W8gsL5sBVZTEMIUy5AjeQjU5ikG_zdrKs04pdcN9gKPOwRJrpFlWdfFPMj8krZgeepEOrwfWGA2TuIljSGNX0BfSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لیلی فلیپس پورن استار آمریکایی، موقع انجام کار‌ نیک راهی بیمارستان شد.
امروز در حین تلاش برای شکستن رکورد بیشترین تعداد سکس تو ۲۴ ساعت، دقایقی بعد از آغاز عملیات یکی از مردایی که باهاش رابطه داشت پاشید تو صورتش و بیناییش بشدت به مشکل خورد و راهی بیمارستان شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71930" target="_blank">📅 11:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71929">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146935a692.mp4?token=CrZlqeRdjv6Bpu2ZYZnIs5iBhyNvYMIfQPm2IfaO282PehcimNtt8QT87Kzt1rXkPQ2P5be69BMoG-yj7VqLgTr_C0OWQ05HjvfDwkQjKjiPGPfu-1-xYqKXZWykPZIqsmmRkyXcFpFdwmVIph1DRlI9wFLnLrwAXhj-8gAtXm9s1SnkBo5jHaBuLN2tsGFSBYDyqGz44rQGIQr0kkqmqjutl8huNE0aEtyMXgFUD5QPdT_FuN0ffyLVkIyjLpsjs1-CApDQhXiIfmjzgQ0NxlH0knn9_1pxyBnbEZoKUrle0y_QegCq9SkxrOZoTnSe_Jk_XLMJL8VhYjAYQPfhYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146935a692.mp4?token=CrZlqeRdjv6Bpu2ZYZnIs5iBhyNvYMIfQPm2IfaO282PehcimNtt8QT87Kzt1rXkPQ2P5be69BMoG-yj7VqLgTr_C0OWQ05HjvfDwkQjKjiPGPfu-1-xYqKXZWykPZIqsmmRkyXcFpFdwmVIph1DRlI9wFLnLrwAXhj-8gAtXm9s1SnkBo5jHaBuLN2tsGFSBYDyqGz44rQGIQr0kkqmqjutl8huNE0aEtyMXgFUD5QPdT_FuN0ffyLVkIyjLpsjs1-CApDQhXiIfmjzgQ0NxlH0knn9_1pxyBnbEZoKUrle0y_QegCq9SkxrOZoTnSe_Jk_XLMJL8VhYjAYQPfhYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوکراین شب گذشته یکی از بزرگترین حملات پهپادی خود را علیه مسکو انجام داد.
روسیه مدعی است که بیش از ۱۶۰۰ پهپاد، از جمله ۴۵۰ پهپادِ عازمِ مسکو، سرنگون شده‌اند.
این حملات به پالایشگاه نفت «کاپوتنیا» (بزرگترین پالایشگاه مسکو) و ساختمان‌های مسکونی اصابت کرد که منجر به کشته شدن دو نفر در منطقه مسکو و تخلیه ۴۰۰ نفر از ساکنان شد.
محدودیت‌های پروازی در فرودگاه‌های مسکو اعمال شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71929" target="_blank">📅 11:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71926">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f7f510c35.mp4?token=HwJRBvxM9AFOL_e0peelttdUbiD03KYyBubC-YETOljh236G1VC4h_ALLyZcyKm1hpj3ytKmHsk4StHNkISUbEiXkln5wgl8fNXU7otdoTo5MTh0V5E58LMG62dUJf5u77gmKK8434vIVLLx1ukiPGjoYuNKIAT39QLohaTzjMp5SKR_bZRWAc9dpYJ_4gkFb0JaDhQcpiEM1hxbJdZEs66fR-fMwtZsFrJL4XD0n1xDWRqLTqj030JCxpggQArfmkM7w1ywCJFR499ReACmdMKuleZtfaUg0YtqqgACpbMEuVkhwaoIHx7cHYCoFHkhvShoVUddrSO_XQqCSvO4dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f7f510c35.mp4?token=HwJRBvxM9AFOL_e0peelttdUbiD03KYyBubC-YETOljh236G1VC4h_ALLyZcyKm1hpj3ytKmHsk4StHNkISUbEiXkln5wgl8fNXU7otdoTo5MTh0V5E58LMG62dUJf5u77gmKK8434vIVLLx1ukiPGjoYuNKIAT39QLohaTzjMp5SKR_bZRWAc9dpYJ_4gkFb0JaDhQcpiEM1hxbJdZEs66fR-fMwtZsFrJL4XD0n1xDWRqLTqj030JCxpggQArfmkM7w1ywCJFR499ReACmdMKuleZtfaUg0YtqqgACpbMEuVkhwaoIHx7cHYCoFHkhvShoVUddrSO_XQqCSvO4dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزارت امور خارجه آمریکا با توجه به تحولات منطقه، هشداری امنیتی برای آمریکایی‌های ساکن خاورمیانه در خصوص احتمال بسته شدن حریم هوایی صادر کرده است.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71926" target="_blank">📅 10:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71925">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">شاهزاده رضا پهلوی:
با توجه به شرایط جدید، تاکتیک‌ها و روش‌های اجرایی مخالفان جمهوری اسلامی تغییر کرده، اما هدف همچنان سرنگونی جمهوری اسلامی و دستیابی به ایرانی آزاد و آباد است.
«ما امروز با تجربه‌تر و مصمم‌تر از هر زمان دیگری هستیم. هدف ما مشخص است، سرنگونی جمهوری اسلامی و رسیدن به یک ایران آزاد و آباد.»
ایشان گفتند: «چهار اصل کلیدی ما مشخص است:
حفظ تمامیت ارضی ایران
جدایی دین از حکومت
آزادی‌های فردی و برابری همه شهروندان در قانون
حق ملت در مشخص کردن شکل آینده حاکمیت ایران از طریق صندوق رای آزاد و منصفانه
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71925" target="_blank">📅 09:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71924">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3eacbff262.mp4?token=usiT1kHJmz0Rknipg5cu7djaauazoB9J8NqzQN8vUktZftIszfrtP5d7Vqvx3-GVR-IFGO1jQeFSUUKelPw1lW0EdmrfZ4h5fZHV1BGpb03xNFQBxQF0ptQXuass0dyScU9HMugwvSrdHBoai6DG727YPMRBqQzHFZ357Ot8yiKsCy1JVWx-0EFefv6Y4yKyfT_HNOU31y-hwVALovBQHrcETLNSdfzr8Gag9tzhb51UoKglx2X-NRYf_fD6lF-1Wtl7DvYaSzbogqF6z2q5eDkaYGRGvVcc6Sm0rK7Erf0FSsWLc9mh7rBWWP9WGRKsnkei7Wdc5KxDCnt2bhgYVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3eacbff262.mp4?token=usiT1kHJmz0Rknipg5cu7djaauazoB9J8NqzQN8vUktZftIszfrtP5d7Vqvx3-GVR-IFGO1jQeFSUUKelPw1lW0EdmrfZ4h5fZHV1BGpb03xNFQBxQF0ptQXuass0dyScU9HMugwvSrdHBoai6DG727YPMRBqQzHFZ357Ot8yiKsCy1JVWx-0EFefv6Y4yKyfT_HNOU31y-hwVALovBQHrcETLNSdfzr8Gag9tzhb51UoKglx2X-NRYf_fD6lF-1Wtl7DvYaSzbogqF6z2q5eDkaYGRGvVcc6Sm0rK7Erf0FSsWLc9mh7rBWWP9WGRKsnkei7Wdc5KxDCnt2bhgYVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی:مجتبی مفقود است و اگر هم زنده باشد در تاریکی زیرزمین جرأت آن را ندارد که حتی صدایی از خود منتشر کند :))
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71924" target="_blank">📅 09:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71923">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d403914707.mp4?token=HsWzVl35BKBY9Kg2YSoms-b9KI6bjBMjBPhr6NZPv2emzEuJyFcWeXAl9DGaldeavo-GFKCeBJMwGAIu9l8qdZdcshex3t-ThaTyOmDOwFaSShbKhf7HndNaGHKfb-1TP-sVVbqml1KJUQamZKglzYctqu0zGOPD3046Akig89637bw7sQD_NOvrKN7YINEpLxJOLkHIrH0-r76N5jgDTRsQqUgBCywdgkp8UQjWz9BkZRD1dGu7ZP4jScg7yHTFuEifPssqcrqF6nxSVoUns9g7xsFr2A4PoYa_y5HEBHhMA0tVbv9BeHGOx69Z95gqwl29YSwhY0qrTObexuKA6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d403914707.mp4?token=HsWzVl35BKBY9Kg2YSoms-b9KI6bjBMjBPhr6NZPv2emzEuJyFcWeXAl9DGaldeavo-GFKCeBJMwGAIu9l8qdZdcshex3t-ThaTyOmDOwFaSShbKhf7HndNaGHKfb-1TP-sVVbqml1KJUQamZKglzYctqu0zGOPD3046Akig89637bw7sQD_NOvrKN7YINEpLxJOLkHIrH0-r76N5jgDTRsQqUgBCywdgkp8UQjWz9BkZRD1dGu7ZP4jScg7yHTFuEifPssqcrqF6nxSVoUns9g7xsFr2A4PoYa_y5HEBHhMA0tVbv9BeHGOx69Z95gqwl29YSwhY0qrTObexuKA6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده‌ رضا پهلوی:
«امروز این (جاویدشاه) یک شعار است .
یک شعار پشتیبانی و من از صمیم قلب سپاس گزارم.
کاری بکنیم که اون روزی که صندوق رای در تهران برقرار شد تبدیل  به رای بشه , نه یک شعار .»
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71923" target="_blank">📅 09:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71922">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71922" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71922" target="_blank">📅 01:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71921">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E6UeezFl-GCAEB5nPaFmpPNVQ7y8iRQLOI2FyKTdDm81UDSa0TvZSmZqSG6RmshNzCenHc9NlIXtSTvKkmXZDEXbSUGdPIxpsCQmmlZYNyR2AjXLQC7Xup_7mqAxxakqKyfAHfCcVhopMAuYT5ZvL8-ELEpgmjMaYUxx-CJZ3BMJD-bVU37pYXR2gvhPLCMcwo5w6ZOuaiihYhBDGMXTvnC6G2avnJRR7Dl23qvfFVGdCDweLzs4hNm_cObEBos39E2jSAGhDf97riMYFIXmigC9pzoDiSJzjKqk_CVtMrBnyyObdrMgonazkN4Fcy2eGS-bP_Rf_w6MAH8l9ClbgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه‌ای و تجربه‌ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71921" target="_blank">📅 01:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71920">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJXmfpycSpHsRC4TKQ22qA6olvihVMeBCf02LPQR9Qut3ILGhMQ3lS4abRGjI3BMvEnYSAVYrL_2ib8T6cquvqRJyS_ZjdNIkcbzwNIbI7SOkWvdgBXvpGPkR8EzgSbW_iZWMs4kbBai5rIH9BBxCQ8xbUfwUKDl2IDdmjg8mVloL4IKU8Uc5kWz0SOGDqo6y2-JbXLRT-K5-o-aUZDALh9STvGVtwLoYYHhP0rG_eswdrHXVLVrt31v_YzmotjeGTGr_v1aa0dMqqOrWUyscBMEFIBkHA5wIxaxjHooNrrPWUuIZ76MbRC_9m9_YpzRBrBFnCMWeokkTdiu9BwX2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه آمریکا با توجه به تحولات منطقه، هشداری امنیتی برای آمریکایی‌های ساکن خاورمیانه در خصوص احتمال بسته شدن حریم هوایی صادر کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71920" target="_blank">📅 01:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71919">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">هشدار جدید آمریکا برای شهروندانش در خاورمیانه:
بر اساس آخرین اطلاعات منتشرشده، عربستان سعودی، بحرین، کویت و قطر در سطح «۳؛ تجدیدنظر در سفر» قرار دارند.
آمریکا در مورد عربستان نسبت به خطر حملات پهپادی و موشکی، درگیری مسلحانه و تهدیدهای تروریستی هشدار داده است.
در بحرین نیز آمریکا به تهدید حملات پهپادی و موشکی و اختلال در پروازهای تجاری اشاره کرده و سفر به این کشور را در سطح «تجدیدنظر در سفر» قرار داده است.
هشدار آمریکا درباره کویت نیز همچنان در سطح ۳ قرار دارد و از تهدید درگیری مسلحانه و حملات پهپادی و موشکی به‌عنوان عوامل اصلی این هشدار نام برده شده است.
در قطر نیز وزارت خارجه آمریکا نسبت به تهدید ناشی از درگیری مسلحانه، اختلال در پروازها و خطرات مرتبط با وضعیت امنیتی منطقه هشدار داده و از شهروندان خود خواسته برای احتمال تشدید شرایط آماده باشند.
در همین حال، لبنان در سطح بالاتری از هشدار قرار دارد و وزارت خارجه آمریکا از شهروندانش خواسته به لبنان سفر نکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71919" target="_blank">📅 01:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71915">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L1seb3YXKp6bhKwDT0hRUW9N0NuuTmFSboDN6qSe3SUmIXFPJQqIq5yyvd4_XFM_dUg790hs14w0te-Jd9I2JwnmvXr_sgpooLTcRXcAc8kdSJRsEnaPwY_Q13ZZw0mlZ9WisMb9fajR91WbuSlXtQ9_2_6RWXQuvQyL08LYIcD0YXnJGXIUT1SQ_7vIV2k1n2fmtRjKNy-HktKvW7-0zxrTC6_MPi97rYQq0SfaiQMPOgGuFNKkbXIg7nhB95PF6WktUy8O_q_iNBkmXljEiLIknWMTfeF_4q1N4KuoEA9IM4bLHd7v6qAl2_qZ1la-TAX3tfcdH87QO-YDRC9D0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7ac25f2861.mp4?token=Kx0u9MUDhBfxQgrBVtDzjy-sLxUaJ2k0_CQ4PbpzLDqLs37-IEMJ3WU627Rq0dk-QTxfIHVH9C29mzjjoJgIKRGMAHbtRn6VQm05w59PsVGGFbhAodw5wpgOlWL_s4aejxnYC7Oej01Wj4eaNf9URIw6n3v_8UTAJG4P91yzy-R2705aEwJYRdgIXw4p03aD3DP9dVers1yvyrmXX5WTaWiRDI9qOxGoHTQAzRyFlTstidxTj7wj37iGFui8xf22OvvOsSEQQjUiLL0JPJKm8y_xF4T2ACtsu2xTXTmmjs7H4GFsr1MDCtF69GbOmLThy1Lf_rl-zO2xK3eAqkzpbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7ac25f2861.mp4?token=Kx0u9MUDhBfxQgrBVtDzjy-sLxUaJ2k0_CQ4PbpzLDqLs37-IEMJ3WU627Rq0dk-QTxfIHVH9C29mzjjoJgIKRGMAHbtRn6VQm05w59PsVGGFbhAodw5wpgOlWL_s4aejxnYC7Oej01Wj4eaNf9URIw6n3v_8UTAJG4P91yzy-R2705aEwJYRdgIXw4p03aD3DP9dVers1yvyrmXX5WTaWiRDI9qOxGoHTQAzRyFlTstidxTj7wj37iGFui8xf22OvvOsSEQQjUiLL0JPJKm8y_xF4T2ACtsu2xTXTmmjs7H4GFsr1MDCtF69GbOmLThy1Lf_rl-zO2xK3eAqkzpbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور شاهزاده رضا پهلوی در مراسم بزرگداشت کوروش بزرگ در تورنتو کانادا و استقبال فوق‌العاده مردم از ایشان.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71915" target="_blank">📅 01:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71914">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vv0h1rwT0qHWqv8r7bbxF_l7yqXB3qiCQlsHpZ2sMJK3gueSoqUuiHzewwkpK-hlL9ehsFqz1TyL3_ysyfgCzj8WP6i6Mq5nTi3uG12eBaxD0wZV5dQWeenkBJ7xbdBhtBUyj8m4pIs33-RVxM_6c0druDaSzWdl2attOmZjh-FfACo0BwnKIqtwrmXiIm2q_FYq0WtIx1MhJT5BVKOqAJPF8DDb2xvmtscRGuXX3dslh8dFFfgxdCg7K2IRU6wY-PtIxJkErXB6W7xwT8DDgNp35XmYTjyWZGYZX23uUiqldBWRJ-pw8cHB3zZ7Vo1nafzWA1dETMsf3r6JLmWAOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی:
ایران هفت شرط را برای آغاز هرگونه مذاکره به دولت آمریکا اعلام کرده است.
پیام تهران روشن و صریح است؛ اگر واشنگتن می‌خواهد از باتلاقی که خود برای خویش ایجاد کرده رهایی یابد و از گرفتارتر شدن در آن پرهیز کند، چاره‌ای جز پذیرش حقوق و شروط ایران ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71914" target="_blank">📅 00:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71913">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/654a3cad3e.mp4?token=NYu7rpXmyB6Ebn2kPjeT59-rTt3SZ1i1k120VL_dT2Fp7dgCqgw-4Q0N5a1x6pTddnZbq7Good7AtCkDd7v6T_hquwI7MpDWuJfwkEYAlXBDyxvuAnh9b7_yeoUKx1TzBbqE9jVlg8nxpjn1Sk-iLEZbh9ZzcAhxMfcnMmM-SrE52FkjQM8WcdddjlspF6n3R8CUEjP4QN_QHA106mvio4QpXu4RiV5wP460pZ_CL05zAenbKdy106qxgQ1RH4Tgeo1Zh6ZedbgIDHvbavel7lZ6czmj8YEcWb7uigaZBZ2AlbAjjlqHaisxwt11pwbmcugynatbQf2AKSp2PufZcGf-koDFIEiQEIcHbbu2bp8WCZHECzMGNpk1TqlJEZDAuna9OPVjH4icOzbhGx1IPZJMwr7UMu4kDsJq0vjXYDglg5P5lRoTqNoastfdIEuS-UEcRqgaJ5I0O_6xA3jlvK3BIJI7JcMsnUa4PFjG-m91Ino5p5qVS-B4x6qIbCWjXuf9I53oEBldjz9ezJnKEaUXZaI44D5bo2fwWHapF0iDFGneTy-mApZOEK7-U7Ixk3bqgCMzeBbc68IETK7DzBVuO-4NcBfYlqLZI5Qgwjn7vuUAvF_e093zqKC2fInYeVgDSFI08nLvOoINugzI3AOIPARuHBjI-A-WGz2Agmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/654a3cad3e.mp4?token=NYu7rpXmyB6Ebn2kPjeT59-rTt3SZ1i1k120VL_dT2Fp7dgCqgw-4Q0N5a1x6pTddnZbq7Good7AtCkDd7v6T_hquwI7MpDWuJfwkEYAlXBDyxvuAnh9b7_yeoUKx1TzBbqE9jVlg8nxpjn1Sk-iLEZbh9ZzcAhxMfcnMmM-SrE52FkjQM8WcdddjlspF6n3R8CUEjP4QN_QHA106mvio4QpXu4RiV5wP460pZ_CL05zAenbKdy106qxgQ1RH4Tgeo1Zh6ZedbgIDHvbavel7lZ6czmj8YEcWb7uigaZBZ2AlbAjjlqHaisxwt11pwbmcugynatbQf2AKSp2PufZcGf-koDFIEiQEIcHbbu2bp8WCZHECzMGNpk1TqlJEZDAuna9OPVjH4icOzbhGx1IPZJMwr7UMu4kDsJq0vjXYDglg5P5lRoTqNoastfdIEuS-UEcRqgaJ5I0O_6xA3jlvK3BIJI7JcMsnUa4PFjG-m91Ino5p5qVS-B4x6qIbCWjXuf9I53oEBldjz9ezJnKEaUXZaI44D5bo2fwWHapF0iDFGneTy-mApZOEK7-U7Ixk3bqgCMzeBbc68IETK7DzBVuO-4NcBfYlqLZI5Qgwjn7vuUAvF_e093zqKC2fInYeVgDSFI08nLvOoINugzI3AOIPARuHBjI-A-WGz2Agmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پورن‌استار ایرانی ملقب به «شیر ایرانی» با شروع بسم الله و کشیدن علامت صلیب توبه کرد :
خدایا منو ببخش و از این آتیش جهنم دورم کن بعد این همه گناهی که کردم
بدترین انسان نیستم ولی بهترین انسان هم نیستم به همه میگم خوبی بکنن کارای مثبت بکنن
دنیا خرابه جنگ زیاده سختی زیاده اصلا سختی دنیا زیاد شده و سختی عمر اعصاب آدما رو خراب کرده
خدایا نه فقط من بلکه همه آدمای دنیا رو از آتیش جهنم دور کن
الله اکبر خدایا منو ببخش خدایا دنیا رو جای خوبی بکن خدایا جنگ ها رو تموم بکن
خدایا منو نجات بده نزدیک خودت بکن میخام آدم خوبی بشم خواهرام و برادرام هم میخام بهت نزدیک بشن الحمدلله
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/71913" target="_blank">📅 23:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71912">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSoZzWOSd2R5cj-ywS9MH1IkZ5SHhrvm3Duf27bEVGnIcX3Ox75zLdMl253Eg6irDEBIatqYJxjG2o11rQNgI6C90hjR4J7zwVjDEd_wA6fQ55-4h_3D-4taTBxZfKrXhmXZJn0ab9IIH9CPFEtdpG1R60mfAHg1jlXvtS6hr7aSRHE_pKqPRFIJFJCyZFM3lOuZw5_QrnDK00Cv-7-13R2zeQzWJBTa8-IV1Dt-yRuRtyjl9E9tWOto2Tnnq3chPl3Zfr9D75qxFUZJUoR4LEgUqcj23v3bMrkWPhzHtHaDEqiNob16I07lOsZDsEbjPYs2xE-FQbGT1NQjJZuyrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ بعد دیدن این عکس دستور حسینیه شدن کاخ سفید رو صادر کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71912" target="_blank">📅 23:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71911">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BA1ujvh6S4AaAm7hYD27rkN2J7ZDvnU4fTzvCtI3bFNZGVoFRwEtjo2FheF3yqN-aM-LBlk-iRnjzDKQ9Tzp8pXTidbUgr6ncpzo5RYcGOnNg6SoSdWsYVB0i0i7CF4t7qsQrLgVDbTrthv_QIzPrHBdHPrYW-dpo0gKK1pzj41lYB4XhDdffeWmwOeXw_DnLXr6ZAP2UPp2j38c0GltbEyFiBo4wSaCENzWz9OqEzpJAlNKboXV9t-7XLBknZ_1_kbr7upJveRgUrSjfibCWekiVC7URwxNNO1U3M1Jhp_6qr4ViU2WiqXmU0O9lfbf4xrOM5EF6jlssmz2nTA1Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه سی‌ان‌ان اعلام کرد که روز شنبه به دلیل ممنوعیت اعمال‌شده از سوی ترامپ، از ورود خبرنگارانش به محوطه کاخ سفید جلوگیری شده است؛ این شبکه اقدام مذکور را «تعرضی غیرقانونی» به حقوق خود ذیل متمم اول قانون اساسی توصیف کرد.
سی‌ان‌ان با تأکید بر اینکه «قاطعانه از تیم خود در کاخ سفید حمایت می‌کند»، اظهار داشت: «ما از انجام وظیفه خود در پاسخگو نگه داشتن دولت و سایر نهادهای عمومی، باز نخواهیم ایستاد.»
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71911" target="_blank">📅 22:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71910">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/411c3a472b.mp4?token=aRPNt3v9ehZwbCN16_7wJL9pR1UACWBXzUhE_U6ZdQRr_Be8nDlxCXenNEWaDugXv-gj4BJ2n-ImheebhPYadAsocvcKkdccNQs421lIqlvjDeBb3p7fIZAeZGHui0yoE_WIgEljDYugnfbTdJOaT35SlP5wBXgCafpNHaxVLS4YbtIuSMX5XkeB76Cz5ZbujD7dr3oxEkUFuC6Ofi7HIkup60_Uge87zG3xh3m4L43WoUsMwAi8CPHJV5BXustmQxXfwcMrrQDZZ0MXIdCbr_A-MyvavatY01PD_oJwQx0zxggJmyaGFTQoKKRwicn0aGSoPRttxTpXsa2FBQQBjlHGdyKjVgsrGU0Zxu3_ydiyLNX4jJkMz-rm7iAFjLOjEJhikxI8UnqKK8jsEGKHVJhp08KRhjdqwk6PQ6YEjqlWD6rpFjPYiEnvuWziFI_oNY-EgAHt_EQGNvX1r0HghNZzOJwnllVXx3gQB_fMNe50o2SucpziuP-1gFL8RqebxKctrMPvwNXWkhbOH0D6-eJRmZBh89RhcxumBiz9hRoZZg2OR4pcImacDoE25Sv6XkRhyS2FzCzfE8PVSkzQhRG-Tr-dM4rGRu6-Jhc0WWNb6FPdNh9HvXSHElmto9fri0Q9YQMTArxOfHKn8Lp_neZPMMeSvF02zQJmwzIuJ6k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/411c3a472b.mp4?token=aRPNt3v9ehZwbCN16_7wJL9pR1UACWBXzUhE_U6ZdQRr_Be8nDlxCXenNEWaDugXv-gj4BJ2n-ImheebhPYadAsocvcKkdccNQs421lIqlvjDeBb3p7fIZAeZGHui0yoE_WIgEljDYugnfbTdJOaT35SlP5wBXgCafpNHaxVLS4YbtIuSMX5XkeB76Cz5ZbujD7dr3oxEkUFuC6Ofi7HIkup60_Uge87zG3xh3m4L43WoUsMwAi8CPHJV5BXustmQxXfwcMrrQDZZ0MXIdCbr_A-MyvavatY01PD_oJwQx0zxggJmyaGFTQoKKRwicn0aGSoPRttxTpXsa2FBQQBjlHGdyKjVgsrGU0Zxu3_ydiyLNX4jJkMz-rm7iAFjLOjEJhikxI8UnqKK8jsEGKHVJhp08KRhjdqwk6PQ6YEjqlWD6rpFjPYiEnvuWziFI_oNY-EgAHt_EQGNvX1r0HghNZzOJwnllVXx3gQB_fMNe50o2SucpziuP-1gFL8RqebxKctrMPvwNXWkhbOH0D6-eJRmZBh89RhcxumBiz9hRoZZg2OR4pcImacDoE25Sv6XkRhyS2FzCzfE8PVSkzQhRG-Tr-dM4rGRu6-Jhc0WWNb6FPdNh9HvXSHElmto9fri0Q9YQMTArxOfHKn8Lp_neZPMMeSvF02zQJmwzIuJ6k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب حامیان حکومت تو تجمعات شبانه شهر بابلِ استان مازندران داشتن دورهم «کلاغ پر» بازی میکردن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/71910" target="_blank">📅 21:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71909">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZY3MrnfDEn8MR_80Xmy5ABOUwOaK64JQIdlGitYnt6dIGXxwlatYoum9N_DwaN8vff4A0vCiWgu4pIlMKKDEwrZWALCfY0Bh555HehJQHA0K-gILhfzl99TBxJmCm1BVg4vbbPYxZFe1k0BsaYiFga-QxIkou5w1_1KVJieTzDjYo-SZWRTJsIjtUcLhinGgAJxKgrSmFvvx-OYrv0kVgSPPglAnPKjBcCludAc9SMMqWUOvoKlOKC4Vjo8SvJyoc2sLaa2XlfGhuVF16jo5-aOfuYP5GUFWXrqyVkvFuScwe-t5Xm6ntwY9g3MWsT75jQmwfnJdAAsMltqA-4A-fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:نام فعلی هوش مصنوعی چرته و از رأی‌دهندگان می‌پرسه که آیا نام «هوش مصنوعی» باید به «هوش برتر»، «هوش فوق‌العاده» یا «هوش متعالی» تغییر کنه یا نه.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71909" target="_blank">📅 21:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71908">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c50e52af4f.mp4?token=ds-oME6OfcXbLp1XPHPrVtdmkeVk_tf1lYYgYX-xdMlYRu_m78P-rUIvsiEe1Ok9FG3PATf6AxE2j_6i_zAhDAVLh8gtdsczk-DTkDTci7fKzVnmdkXFsgbcr-Z2evyS3fSRmS9o9V-Hq_g0oIV0U-Ilk7z6nvLASQzylJFTgo51VG71uq77qtEPe53fLowXAvRcfbEpgwhocoMPeAlkvGk641YexSRZD54rLxkfzEBOmgQKaraf6mRhz5BInDvaZJLj7oSGdT_Th_B0gZ6s123NTmpBh9QWl4aPaEAXF2SvyAUlNQJrfWh0kCM-srYMCKuukBtARe_l35edyhodiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c50e52af4f.mp4?token=ds-oME6OfcXbLp1XPHPrVtdmkeVk_tf1lYYgYX-xdMlYRu_m78P-rUIvsiEe1Ok9FG3PATf6AxE2j_6i_zAhDAVLh8gtdsczk-DTkDTci7fKzVnmdkXFsgbcr-Z2evyS3fSRmS9o9V-Hq_g0oIV0U-Ilk7z6nvLASQzylJFTgo51VG71uq77qtEPe53fLowXAvRcfbEpgwhocoMPeAlkvGk641YexSRZD54rLxkfzEBOmgQKaraf6mRhz5BInDvaZJLj7oSGdT_Th_B0gZ6s123NTmpBh9QWl4aPaEAXF2SvyAUlNQJrfWh0kCM-srYMCKuukBtARe_l35edyhodiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تست اکتان بنزین در عربستان …
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/71908" target="_blank">📅 20:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71907">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IuXwCxBixX5fVIVgoNkTe9uQ-ZTxVgkHO5Q5cDGXmV8Y0wuxqhlwDd3GMEsQ7y9TSxFZNLRWfqaEpLgPpt_C-5M3SFxSd3o6WZxrmnhTjHqY1UUVWrjdTiOwmu_mYy1svJxMGIMfeFVzcC5P63aYeRI_Gbovv0GanHJM0Ak4FgTtRAHshg4XAn_NLq8w2dScnl4VfgOtMj4LtCDz8LiLUo57ofMfJTaqRdBm1UeCCIslxehNy79O67GKETtOTUjUSuBtCdCLXYDETC1jG91pwI8Csw4RgDgf0W_l8AVmYwc3Z6wkL53kP59-RLkKJF7VrzdNc7syaGMyCFw5U0MO0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان هواشناسی: طبق پیش‌بینی‌های فصلی، بارش پاییز امسال در مجموع فراتر از نرمال خواهد بود؛ تمرکز بیشتر بارش‌ها نیز در غرب، جنوب‌غرب، دامنه‌های زاگرس و بخش‌هایی از البرز پیش‌بینی شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71907" target="_blank">📅 19:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71906">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی ایران، در گفتگو با شبکه الجزیره اظهار داشت که دونالد ترامپ، رئیس‌جمهور آمریکا، در ارزیابی خود نسبت به ایران «دچار اشتباه محاسباتی» شده است؛ وی همچنین بنیامین نتانیاهو، نخست‌وزیر اسرائیل، را به تحریک برای آغاز جنگ متهم کرد.
رضایی با بیان اینکه تهران «برای یک جنگ قاطع» آمادگی دارد، هشدار داد که هرگونه حمله بیشتر، با پاسخ‌های شدیدتر علیه پایگاه‌ها و منافع آمریکا در سراسر منطقه مواجه خواهد شد.
وی خاطرنشان کرد که ایران نقاط ضعف ارتش آمریکا را می‌شناسد و برای مقابله با حملات هوایی این کشور آمادگی بهتری دارد؛ ضمن آنکه اخیراً یک موشک ضدکشتی را در نزدیکی یک ناو هواپیمابر آمریکایی آزمایش کرده است.
او همچنین افزود که ایران به این نتیجه رسیده است که پس از خروج آمریکا از یک تفاهم‌نامه، باید راهبرد خود را در قبال واشنگتن تغییر دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71906" target="_blank">📅 19:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71905">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">رضایی، دبیر شورای امنیت ملی:
رایزنی‌ها با میانجی‌های قطری و پاکستانی ادامه دارد و ما شرایط خود را برای مذاکره به آن‌ها اعلام کرده‌ایم.
ما با میانجی قطری در تماس هستیم؛ او شرایط ما را برای توقف جنگ به واشنگتن منتقل کرده است و ما منتظر پاسخ ترامپ به این شرایط هستیم.
شرایط ما عبارتند از: پایان دادن به جنگ در تمام جبهه‌ها، آزادسازی منابع مالی بلوکه‌شده و پایان دادن به محاصره دریایی.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71905" target="_blank">📅 19:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71904">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5wx0qhPk_jk1l59WCwpS2SyAsoN8fx-7jA4INjU3phk2HU11kSS4qS4MdZRXVRR7VeAhDKRxsr4UURNGedZVlPhqeAj9s2RNlyUZFOPlI8mjf_GFWFke3UVU2fD_roGH9Vww7MXYpJFtjuccVAi4JnCyVZZWTVmfYrSHzHpWtAUkM0E51Fb7n_WFkN5VpymAtJtt2Uo6YCGP4l7ZOgwdP80ID-Pv5n3A-cx8ChMWmb4Tg-f_vYlZRiX1MGt3O6HnHFPxzIsngi2oOB_wB5hKLocg55yndqdQ6YM2eV5b0iSvUw9s9K2iVckjOPqFrtFejVTtg6buPp7VLs5yKfLgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی در گفتگو با الجزیره: اقدامات آمریکا و اسرائیل ممکن است ایران را به سمت خروج از «پیمان منع گسترش سلاح‌های هسته‌ای» (NPT) سوق دهد.
رضایی گفت که ایران هنوز تصمیمی برای خروج از این پیمان نگرفته و افزود که این تصمیم به اقدامات آتی واشنگتن بستگی خواهد داشت.
وی تأکید کرد که ایران همچنان به فتوای رهبر فقید انقلاب اسلامی مبنی بر ممنوعیت سلاح‌های هسته‌ای پایبند است و دکترین هسته‌ای خود را تغییر نداده، اما «نمی‌دانیم در آینده چه پیش خواهد آمد.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71904" target="_blank">📅 19:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71903">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7703ac3568.mp4?token=mj6xc1G8xcBBMAOy_JPdjiHbfmAQ3YZ0Spy4KWkmyva59cEoFwI7eFDyU_bpaFox4cNVLKF0H_XyocvbjlUunPDbtOcUKT4DDLFUCRfvyWl83vR-TGCaEJWwc_My_jusyjohsJrq3eHtRGuXbQVZIUO5xdZDzQ56VWpil0KYexlIkk6b2UiGNviMY0J4SOEt_-46-hct_QVIw_mUaTBiISD0Bmdw9XjeUM0PdXGuG9R53ypcl8IKHo7AfVrpHiKXYL0VAfQEkO-Ga8OidT49Mh-bKkE1lFENJDsGDKFIjMEQAzrFT7gU44jQSgfvq1i0ZTkF3Z7KVq2tomRuDs_AcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7703ac3568.mp4?token=mj6xc1G8xcBBMAOy_JPdjiHbfmAQ3YZ0Spy4KWkmyva59cEoFwI7eFDyU_bpaFox4cNVLKF0H_XyocvbjlUunPDbtOcUKT4DDLFUCRfvyWl83vR-TGCaEJWwc_My_jusyjohsJrq3eHtRGuXbQVZIUO5xdZDzQ56VWpil0KYexlIkk6b2UiGNviMY0J4SOEt_-46-hct_QVIw_mUaTBiISD0Bmdw9XjeUM0PdXGuG9R53ypcl8IKHo7AfVrpHiKXYL0VAfQEkO-Ga8OidT49Mh-bKkE1lFENJDsGDKFIjMEQAzrFT7gU44jQSgfvq1i0ZTkF3Z7KVq2tomRuDs_AcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: کنگره در چه مقطعی وارد عمل شده و به مسئله جنگ با ایران می‌پردازد؟
رئیس مجلس، جانسون: ببینید، دولت این وضعیت را یک جنگِ در جریان نمی‌داند؛ و واقعاً هم چنین نیست. آن‌ها در تلاش برای به سرانجام رساندن یک عملیات هستند — عملیات «خشم حماسی» (Epic Fury) که موفقیتی عظیم بود.
به گمانم در حال حاضر نیازی نیست دموکرات‌های لیبرالِ مارکسیست در کنگره بخواهند به فرمانده کل قوا دیکته کنند که با ارتش چه کار کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71903" target="_blank">📅 18:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71901">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75801e50d0.mp4?token=esftxdLOc6HkRGVhofGKqB0eTeepe-pkMhaPP78c2ypqTeCCoN7Z84hRnHd2y0WodpYNySEP2CcTGD67FQtpNNTyTPMFnG7UG5UX2jWzhhCAcSMPgUxNGLeWZUca4Ns5aewqo1WqV8blnyxrwNERRhfIUh-sreed9Goi9JIMOxjYXPuFfmMkGAQYuXtWyJWhcCnJ1JCb79qnYIwm_RTeb87tjpbVG8F7Fll1x93mtGhcAfCdPiBmS6j4tHsejjRP5WM_b3Xv6zGABVde0EeTtSW74xmA4Nucchj3ufPE4hKqRInuS-pCq1QBp6lIzFm6TjtqRaYR-3ciOlQA60xKeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75801e50d0.mp4?token=esftxdLOc6HkRGVhofGKqB0eTeepe-pkMhaPP78c2ypqTeCCoN7Z84hRnHd2y0WodpYNySEP2CcTGD67FQtpNNTyTPMFnG7UG5UX2jWzhhCAcSMPgUxNGLeWZUca4Ns5aewqo1WqV8blnyxrwNERRhfIUh-sreed9Goi9JIMOxjYXPuFfmMkGAQYuXtWyJWhcCnJ1JCb79qnYIwm_RTeb87tjpbVG8F7Fll1x93mtGhcAfCdPiBmS6j4tHsejjRP5WM_b3Xv6zGABVde0EeTtSW74xmA4Nucchj3ufPE4hKqRInuS-pCq1QBp6lIzFm6TjtqRaYR-3ciOlQA60xKeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروهای اسرائیلی به تخریب خانه‌ها در «میس‌الجبل» و «المنصوری» در جنوب لبنان ادامه می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71901" target="_blank">📅 18:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71900">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8be83e9c35.mp4?token=INV4Bl2_92rrEu8tkVgsI8L2C-iIlQ9bPCQwZ02VADlVcvK4Ke39reVfRmseI66Rh5ldZyQo8fuJTFwukz3zxBaaO8jhdcWHkTC205yb72vLcJqSOMa5J5crtA_mHpyze-yNew8n5M2f8DsEET0D4z48WqMYBAA4mONpEJviZUQbYjk7OQNJFLex5Fl6mje8Yg3lvIUNJBGH3htOlfV8PEPvlE77XQK1yDS5zVSe4fLThR5xsdupLFgKrwYbuta7kje7ZU0b3-xBp4tpRGkkj1dxtt7UJnrGeZ1VpEH3gjh1-YCtpSRHrxBDuPF8PnD0nXpkGAcOV-AF5a9pHss8Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8be83e9c35.mp4?token=INV4Bl2_92rrEu8tkVgsI8L2C-iIlQ9bPCQwZ02VADlVcvK4Ke39reVfRmseI66Rh5ldZyQo8fuJTFwukz3zxBaaO8jhdcWHkTC205yb72vLcJqSOMa5J5crtA_mHpyze-yNew8n5M2f8DsEET0D4z48WqMYBAA4mONpEJviZUQbYjk7OQNJFLex5Fl6mje8Yg3lvIUNJBGH3htOlfV8PEPvlE77XQK1yDS5zVSe4fLThR5xsdupLFgKrwYbuta7kje7ZU0b3-xBp4tpRGkkj1dxtt7UJnrGeZ1VpEH3gjh1-YCtpSRHrxBDuPF8PnD0nXpkGAcOV-AF5a9pHss8Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ، در حال انجام تمرینات بدنی صبحگاهی با «سپاه دانشجویان افسری» دانشگاه تگزاس ای‌اندام (Texas A&M) است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71900" target="_blank">📅 17:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71899">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">دریاسالار برد کوپر، فرمانده سنتکام:
بیش از یک میلیارد بشکه نفت خام از سوی شرکای ما در خلیج فارس از طریق تنگه هرمز ارسال شده، در حالی که ایران به لطف محاصره آهنین ما، حتی یک بشکه هم صادر نکرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71899" target="_blank">📅 17:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71898">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71898" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/71898" target="_blank">📅 17:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71897">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxYrW3mQPqpu0Y8lKyvpvcpFRfAzCRrL8vkACif4HU9ChRgvYKXKt4EDsiUhb6RZwc5hB7P3EAmyJg95aMxp68qnPoH9GlV9B6-gOm07dQXM3PV8nTHAtU4MtBruyOymubJ4qpeJQ8P4l3A0-YLv6YcBQbPAU4Ch_cLonTQh6Jl_v6D3Sg8tF-R1AQ4UdNIyFIpPpgiJEWr0M6o8Y4eMmVxb-5xYcML0ApLI24kqR_zBzsfkYgfb81D6dFxEXv90rZnu6KczN3Lax4ebDIvdX0Ee7gTWC31hx7IHfE41o9kQwIE1CTBRGAc9mXMG3GoHdTaHblNzZhl4ofxJmKlHgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان‌انگیز  بارسلونا
🆚
سویا
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
بارسلونا: ۵ برد و ۲۵ گل زده
سویا: ۳ برد، ۱ تساوی، ۱ شکست و ۷ کل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71897" target="_blank">📅 17:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71896">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7687234b2e.mp4?token=ePr_E2xiAbXlrame6mu8FZvdcPgtLYOTK4HugPuLwzG35RXy6fdT-3rr5fo1eAK7j6T84UYgbcZr_0gm2FO3KdsdXHarswUWej1vusQI3qNV9BZIpDv4F4yTfm8T06AVUQIsvG423D6YVUunfIEFLE9cvDTtBS3hedYep7clXH10j8h-uDP7JAhjS-DkuzY-2rusCVjNVKl4U2rJeDbqXj-wWeHOwmSN-nHJIO37fT2mem8tnLAzJspA4Jg3sz07QmO9z4I5V3emsQstdi2cIg_BM_dzUITK3qBW4x0SrqmlZ6pMbvy0mIC6O-EdMXiRYKGH33oZJWGhOHpadPFsBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7687234b2e.mp4?token=ePr_E2xiAbXlrame6mu8FZvdcPgtLYOTK4HugPuLwzG35RXy6fdT-3rr5fo1eAK7j6T84UYgbcZr_0gm2FO3KdsdXHarswUWej1vusQI3qNV9BZIpDv4F4yTfm8T06AVUQIsvG423D6YVUunfIEFLE9cvDTtBS3hedYep7clXH10j8h-uDP7JAhjS-DkuzY-2rusCVjNVKl4U2rJeDbqXj-wWeHOwmSN-nHJIO37fT2mem8tnLAzJspA4Jg3sz07QmO9z4I5V3emsQstdi2cIg_BM_dzUITK3qBW4x0SrqmlZ6pMbvy0mIC6O-EdMXiRYKGH33oZJWGhOHpadPFsBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رژه ده‌ها هزار نفری جانفداهای عراقی در حمایت از صدام حسین دو ماه قبل از سقوط رژیم عراق (۱۵ بهمن ۱۳۸۱)
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71896" target="_blank">📅 17:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71895">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f42ac1c41.mp4?token=gEXic_ILfD36JAN2EgnWfKa5YlIiHt1PnVb37GxjSePzhvAqthoUjLUKoyJeVKCF3Ml79bbpcU2hYeJJV49Q_Jwl5RtKeDl_4jqaiocPDPn5-y-7iGaFvjUz1IYbW_hWdlE4d4r1ic1wktFbc1AJFs4jUdYWfK4h3Nueyl2Z2n2Cq68gzV_Rgj5dglMTUw0oCmK3lzUTjsWMIOMvIDmxZXdihU2l-PsXtcUj_mELP1lHTzQbfAEhUG4aCJLkoU897_SSXpgDzZmZuODqMKBO53dXQFVU3CP8jTL2Lk_DeRrENH0AymhUxY6LTdQGeDKGxPuUZGD9HqIpkk6wzzAoXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f42ac1c41.mp4?token=gEXic_ILfD36JAN2EgnWfKa5YlIiHt1PnVb37GxjSePzhvAqthoUjLUKoyJeVKCF3Ml79bbpcU2hYeJJV49Q_Jwl5RtKeDl_4jqaiocPDPn5-y-7iGaFvjUz1IYbW_hWdlE4d4r1ic1wktFbc1AJFs4jUdYWfK4h3Nueyl2Z2n2Cq68gzV_Rgj5dglMTUw0oCmK3lzUTjsWMIOMvIDmxZXdihU2l-PsXtcUj_mELP1lHTzQbfAEhUG4aCJLkoU897_SSXpgDzZmZuODqMKBO53dXQFVU3CP8jTL2Lk_DeRrENH0AymhUxY6LTdQGeDKGxPuUZGD9HqIpkk6wzzAoXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه آخوند تو صداوسیما :
اگر یک
قو
با
لک لک
ازدواج کنه بچشون
«قلک»
می‌شه
اگر یه
دارکوب
با
بلدرچین
ازدواج کنه بچشون
«دارچین»
می‌شه
اگر یه
مارمولک
با
لاک پشت
ازدواج کنه، بچه‌دار نمی‌شن براشون دعا کنین
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71895" target="_blank">📅 17:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71894">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWESfnygcQOE0OfMDX0EpLMNwAhpWSKT76YRRtxg1BCT1pnGlALhYW72XASUyeHqiTrbU4_nIdxkK_JR_HpYlPPXZCUOB7Zh73vx0zpU8yedigzx9S94rrQ6Mxdk5IOqcken_PC7fYXRzKm3YLGFJdQGA5Oa7d-fMIlw9BkLfudKmYSoFOYsxtqOS5Pxct0nYl6_Nda0eiIUUzinRIw_8l-4AxwsZ3trKQSCtKo0hg6aTDwRJBvS16p91UNysbuGHLtaSffwNm3jMc1g7ugeIXJ9doJ04vbjCaBWdieLCeoXuqfHOq-7lS3i0jI-BQlwFqqZnOH7xxDWmqL9eBBrXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنتاگون روز جمعه ششمین مجموعه از اسناد مربوط به UAP/UFO (پدیده‌های هوایی ناشناس/اشیای پرنده ناشناس) را منتشر کرد که شامل ۷۱ پرونده مربوط به بازه زمانی ۱۹۵۲ تا ۲۰۲۵ است.
این مجموعه شامل ۵۵ فایل PDF، ۱۵ ویدیو و یک فایل صوتی است که ۶۴ مورد از این ۷۱ پرونده، حاوی بخش‌های سانسورشده (حذف‌شده) هستند.
در میان این اسناد، سوابقی از یک برنامه نظامی وجود دارد که پژوهش‌هایی را درباره موضوعات غیرمتعارف — از جمله پیشرانه‌های «وارپ» (warp drives)، کرم‌چاله‌ها و گزارش‌های مربوط به آسیب‌های وارده به پژوهشگران در پی برخوردهای احتمالی با وسایل پرنده ناشناس — سفارش داده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/71894" target="_blank">📅 16:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71893">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e4104492c.mp4?token=vAmNYQ6iORxT3o77wo1i0y4UNQslEy9e_ZAMrECvgWYte64LtsNwqOwcXkiXUj1e3u7-EVfyHni0cucC6tz4MGy9K6_wHsFo4KB2wtuZv06S32nsYRc-LFhMNU6SvM2cpkAmiiFCqRQuqozyHCW0rF1HaHJ8Ond9tQnQg1EjM3wesBHHeJRFMiSAT8tGID8dudTHkoJ_R5mV7CVw6llRiI7IjLTH2ivGRVoNW2wKHYxsJEYZMrwB_cwISw_K_8V5b4vxA6CoB3lmJDGj3lPYqZJyLOKUqwa47MXbJssy8HUZISx2eWaB1tv1oNPKTX20Ghm6eGbcBtonFKTAviqOUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e4104492c.mp4?token=vAmNYQ6iORxT3o77wo1i0y4UNQslEy9e_ZAMrECvgWYte64LtsNwqOwcXkiXUj1e3u7-EVfyHni0cucC6tz4MGy9K6_wHsFo4KB2wtuZv06S32nsYRc-LFhMNU6SvM2cpkAmiiFCqRQuqozyHCW0rF1HaHJ8Ond9tQnQg1EjM3wesBHHeJRFMiSAT8tGID8dudTHkoJ_R5mV7CVw6llRiI7IjLTH2ivGRVoNW2wKHYxsJEYZMrwB_cwISw_K_8V5b4vxA6CoB3lmJDGj3lPYqZJyLOKUqwa47MXbJssy8HUZISx2eWaB1tv1oNPKTX20Ghm6eGbcBtonFKTAviqOUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاشار سلطانی روزنامه‌نگار و فعال رسانه‌ای:
هنوز مشخص نشده که موشک رو کی شلیک کرد (به کشتی‌های عربستان و قطر) و توافق رو بهم زد!
وقتی رئیس جمهور تو عراق بود، وقتی رئیس مجلس تو مشهد بود، وقتی پیکر رو هوا بود؛ یه عده خودسرانه موشک زدن.
کشور داشت آزادانه نفت می‌فروخت و پولش رو می‌گرفت ولی یه عده بی‌دلیل به دوتا کشتی تجاری موشک زدن.
چرا؟ چون میخواستن شبکه فروش نفت‌ خودشون رو حفظ کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71893" target="_blank">📅 16:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71888">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GlMwk5r51_DRJN61ckLt8W6yndUAFq10OlYoVOm5363qCUb4DxY-UM30zM0GMBPOQKVj8dZMk6104tuUmzURHzU9YY5HGECrNh3537V9Fw798o45_T8aE8OreQvV7keYM0JVicjhYVLPcub6BPwmxmO2u9OMUb4ScYUbjYeT5yc5BQmwQh-1dH2TN6wstfZnFz3Mbol8ytYbbReawRr3swNtYsuHQEDCXNR9lNLyaUlmbi8tgd5l68nF1xvilJawQTDpkJauKJvk_rzhuEu5RHag00QpYtCEDp7oX4MeGViXxTTCQxKQSEow9uxfgzmbNhAZ8ckhwpjmonNho3-i6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OdwbdDy9YqLQhvahretsTWe9kzzQhSfyt_kxPbFwkZf3bVFdo0D1WXLdJWcXvH4m-6Bcf3LFeYDNm2MM5fFwyOanv5-YvZwQDm2Xqn3HS7QhsDajvzWC0rVSE8eCVatby-AVcLdAu5Pgqao_EELGyychT8K3MLNEksasfJmCVkzwozNbn-u7dMrR0jGFS7L4JsVAGDpjPA5r0HMhUK6QlzDafO3iHcCy8DoW55OP8v8fq1xW-WyBYHJ4YMJdRA8R-xIV9ddIN7C_Jhs95kEsixn7kEkxO9GN9Xnu0zTAhS993uEQqvcKqG5nDn72Rz-asOxMpZd7YPC5OrQfawtvYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oP5knb-APdGIpkOCtnqN4fRTyD78oC7jPqwyMPNKHsNmpyZc0V4uM5q0gqNmtb3OJ2N2TNO6z2GdAN8N5RDWvwmw_XxlNrrkTNrjeOEBYT4jyuy_asRFGA-WS0vXcrn0fFkuh0WIMBIICMagTj4x03Rly09v6QaLLb9Qrv4pBKSI3EOMWRYQNaxX6g6JOD6_DaAMc34zo0woZvkxleG1tvugP51eVRnze4IP7R581ZqhN9ZOJIWBf3bkJPXbMm-EM0JfxO4DoOr-4NA4cfQgyGNq1QE9-guPWsM4nKx2KRER4ShIR9RBuIH3-mcckkXNP9oBi4qjd8rczBHiZTX9Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VPBHJeSpP_uJLmep6Gaa58qEou-J93pqi2vVuQ4UhMXSGwV9NyulfQv0vSz3QTjcGntDXGxxfsgIDYtZmnW2nNcC1cb0I6ch6qQ_t1CV10usZhQf0h2rGL_oVLwOC9tMiVsA-cIoO4eoRZqAVhRLIJHcb-YfO3h89hJsaAdWXE5lFeRJSr4BbvrMXvgIuvX7oaUpElwqPSE6oiZ5AqFxixzZ1SbFZty71qXY626wV86lJS8h3WvFzQlLNY5jOEejN4GvA8nqxQBlqbmV9SDGfhlZ-G3LANwk312kXjCkpbv1DRTbUElytZCCZ848HajlNPYoJab5M96UI5oVI-dHEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IYRrOoc0cqgJ6kA650anzBgay7-3I4H3--tEiyq6HN2kZpaCcshmH3HKUMsikF7hm0sj1Z5kxve6eJI1uUCT0GAMjaNDlilo31gqunY-j7xEwuLdqL1BWXLEtDiKG-OAChwr4ANb_3HV9gnRw8k2ueQUaiWJ-lQsjkF3VuPZttwmR3rFV9CAp8WB1BYiqKSA-XYmIgNN3ydIkKN4yA4b-xtR5gHXuDe453DBI4UYiXk7Atcg1bOGfY3lDXJo3ETiaP-zZGfl9RaMzO0IDB65DyeskbxpopR6HPe_CPathxTCthkrej4oIXA3U7oQO-8Hl0JOp5ZS1rz-RvPp4CbYBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسانه «میداس نیوز» (Meidas News) پنج عکس منتشر کرده است که پیامدهای حمله ایران به یک پایگاه آمریکایی در کویت را نشان می‌دهند.
در این گزارش نام دقیق پایگاه ذکر نشده، اما من آن را به عنوان «کمپ عارف‌جان» (Camp Arifjan) متعلق به ارتش ایالات متحده شناسایی کرده‌ام.
تصاویر حاکی از وارد آمدن خسارات سنگین به یک انبار، محوطه بالگردها، یک پناهگاه مستحکم (که برای اسکان نیروهای آمریکایی در شرایط حمله در نظر گرفته شده بود)، یک ساختمان چندطبقه و یک ساختمان پشتیبانی دیگر است که همگی در کمپ عریفجان واقع شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71888" target="_blank">📅 15:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71885">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PqUfy3QTFTTF7-mEb7dlN1_p5LUyLFA1M50KUFfzPrVEL6OyGbfGmfDNz-o4U1tpLLc5NS7UfsCVzSdf1IA9XEI_kMHf_nDgJux--1se-Iv8jTeXH44pframtJrweSNKiib1RU76NoLjlSllF3r-tbJwqUu-egVIUHEjJPi0MtFwQ28xjfhq5sVCcrQ2nbTF_cb-RFfPUDdzG8oRuZpTjN9cHuAJz86x16oLyBK8Era-2-xvq8L9AJyEQTItaMKPwjYQh35EjxLL8jNYb9kRptQ5ZJP6F3mh5u7tcvkIpRnKEyRyOLnlzU4t2B4cIIETn6QN-rkyGK2hjFjEtiXlDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WQq-bg_Lfw290dMRXibXSOaaDC9DX6V19yH9zZ2nabJQfyJI-132ECO6TP5c5R8gfI1s_T0BQt51V_RsJuCYWXb88vPsyvTkybFaX0Y1m3OHfwyLMPAsKiQqgVDT_HdG830qyZMVXE2aGXVEjNMQ-owOV0oQhEZ-wU41lDS60du3X-U2ff5JscLSm81RVfzZtevPIA9eBtvXnjJxGqEDeMrYVR8UpCNP5BUVWqmj39vga9KzS-Tbs4pytU-RBejP-7m_hvxQ69HIO3oTZGei_b1cOTyB4dcB8RQ8UYmth9-NzGJ8eHyiwLQmosG0ehIhKAUXucNnEm_xGacAg9nN1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E_7UZXFa9_MbUlOU0X7AKmM8h8tWuoZihlsiD1dsHdZcgVKm5Ic2bEK1jHYpakk2fgToT4Exry-kIW9w9COrAplHCQmXE8qmh2hGWAOJTVigpUhy9_l_6oTUzQ0b_mk0MmnSizIw4KPhp8UpLmejpDC_ojqNorhuPjz1ulIyO0IRsgrkRV3aFY1TyVvptsjK18avJ7aOdgaWx6ysIhsL5RtuLEXdfy4wNmVoOiT5tRj0Zf1CgHMwBHfZcQl6ietSc7Sn3K8GvucWZkIuLp5LRXyrBmthwqUyUdP-464Qjy9YSCGDZxcTuLL-X1_lNSoM-ph3uLVnpSbAGHWc0G7htw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انفجارهای پیاپی در نزدیکی فرودگاه بین‌المللی ملک خالد در ریاض
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/71885" target="_blank">📅 14:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71884">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/974e7b2cdf.mp4?token=kPabBOTCtphuzkfJe53j8t9ZBkl9Z2M6bCtKo4hy-WEw2CCjVxgfb0thw0vKO-66lafvR832Rq9AXmv41c_jbS0pePHpdDNDjbMWaWwodxxm1kVzSevVLejmMoH4Tj69iMRaAcUPAZr1CcwoRvXBLQaRPjyZIwTOsVqZvJdnsYBVm_BAQvSQ4MLmt0qz8mnZ87neeqNzUfhDvJTd9bJNtoaUknRpf1kBEddCwpFCVU5Hey4m607p6NCjIEQr60pw-Mc604T_Ny7HjZI2yNrs4Ecll-KawoOY0mEmy103pVaF7G3yBMkad_KYmp2CsMbCBu1bQekjq9GybR971bMp0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/974e7b2cdf.mp4?token=kPabBOTCtphuzkfJe53j8t9ZBkl9Z2M6bCtKo4hy-WEw2CCjVxgfb0thw0vKO-66lafvR832Rq9AXmv41c_jbS0pePHpdDNDjbMWaWwodxxm1kVzSevVLejmMoH4Tj69iMRaAcUPAZr1CcwoRvXBLQaRPjyZIwTOsVqZvJdnsYBVm_BAQvSQ4MLmt0qz8mnZ87neeqNzUfhDvJTd9bJNtoaUknRpf1kBEddCwpFCVU5Hey4m607p6NCjIEQr60pw-Mc604T_Ny7HjZI2yNrs4Ecll-KawoOY0mEmy103pVaF7G3yBMkad_KYmp2CsMbCBu1bQekjq9GybR971bMp0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف سوال پرسیده: سخت‌ترین قسمت پسر بودن چیه؟
جوابا جالب و دردناک بود:
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71884" target="_blank">📅 14:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71880">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95e492d945.mp4?token=WHR_15lTVUVKJa_C950tYeCxfnTkeQfJdGP1fF_FDuz2zorglO95sOMfZ81JLkBiJ674X8U4FPjAbz__PvXW2gmtILJo11bFtLmqJocvPYHg_lPsqOciSUVAfZkVNAldQfJPdxnBIMqorLKbBfZBrLfib0zpW6KT56IOqakzLWE_oiNBcaQjVWV0nTQRn6O3GzaZ46pseRcEDhQCVB_gEwrk7zrI4gqUU-ComFpQtgxA2c53zJUkq5ZiEHsIceifdzTVnGma9GyrZtWCsehnRWpCEznTKInD8RXR6DjUxTRw2BNDhG_nzxqcMZxTY4RkqdOLWWlhWP5mZGE-QWnSgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95e492d945.mp4?token=WHR_15lTVUVKJa_C950tYeCxfnTkeQfJdGP1fF_FDuz2zorglO95sOMfZ81JLkBiJ674X8U4FPjAbz__PvXW2gmtILJo11bFtLmqJocvPYHg_lPsqOciSUVAfZkVNAldQfJPdxnBIMqorLKbBfZBrLfib0zpW6KT56IOqakzLWE_oiNBcaQjVWV0nTQRn6O3GzaZ46pseRcEDhQCVB_gEwrk7zrI4gqUU-ComFpQtgxA2c53zJUkq5ZiEHsIceifdzTVnGma9GyrZtWCsehnRWpCEznTKInD8RXR6DjUxTRw2BNDhG_nzxqcMZxTY4RkqdOLWWlhWP5mZGE-QWnSgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروهای امنیتی پاکستان عملیاتی را علیه یک هسته تروریستی — که گفته می‌شود متشکل از شبه‌نظامیان «تی‌تی‌پی» (TTP) است — در منطقه «کوهات» واقع در استان خیبر پختونخوا آغاز کردند.
در پی حملات بمب‌گذاری روز گذشته علیه مسجد شهر، شبه‌نظامیان مسلح یک مقر پلیس را به تصرف خود درآوردند که منجر به درگیری‌ای ۲۰ ساعته شد.
نیروهای پاکستانی اکنون این مقر را به‌طور کامل پاکسازی کرده و تمامی شبه‌نظامیان را از پای درآورده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71880" target="_blank">📅 14:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71879">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6895254ca3.mp4?token=lRH8ndoauarOhTPy0Ha53yhoTpVkFNzRQ47XpiG-uqJWms7brYRu-T9fo5Yb14Src5cK9EYRQnTiaLYbgXhy-eCxNoN1avs-KHqWDHe0nyb5NaC1Oo8c-KR5VSlQ1kopWiyC-dzy3K1GYg-61QwYhIuWPBbKdq0v3b2A2uqJc_ARVYkUbBwq7ykKf75bfr7xxZYMvnyZEAvdaHf2fi4WjtCYj94cdRI-NCQuv3mfRa_732WWrfwXJzl0llv2XShUFghp2KWVTgu2_gyP1uCLIVczvlNbdnedWj5rWT1k0Jaiq4Y6nggS9f4yGy5Jx0qKau14brTjzlT0SsspHnnY5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6895254ca3.mp4?token=lRH8ndoauarOhTPy0Ha53yhoTpVkFNzRQ47XpiG-uqJWms7brYRu-T9fo5Yb14Src5cK9EYRQnTiaLYbgXhy-eCxNoN1avs-KHqWDHe0nyb5NaC1Oo8c-KR5VSlQ1kopWiyC-dzy3K1GYg-61QwYhIuWPBbKdq0v3b2A2uqJc_ARVYkUbBwq7ykKf75bfr7xxZYMvnyZEAvdaHf2fi4WjtCYj94cdRI-NCQuv3mfRa_732WWrfwXJzl0llv2XShUFghp2KWVTgu2_gyP1uCLIVczvlNbdnedWj5rWT1k0Jaiq4Y6nggS9f4yGy5Jx0qKau14brTjzlT0SsspHnnY5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قبیله‌ای در جنگل‌های آمازون که با دنیای بیرون تماسی نداشته، از هوا فیلم‌برداری شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71879" target="_blank">📅 13:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71878">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fe570c529.mp4?token=Nfrf11tlHlTOJ7kICw46P-t2SWsluM_I-kvU3dApxtr4_SWGcO1D-50Fq37BEpoeZ9O3XqRly4xun4wdrspg1apiJBdAqaHRJvmkait7GPKT7RWvvGTUSHtwNSPjSHWEphTnWwoqYGcU9528fdz_9j02WTrXcI6mLWqxGXI_8JOI-hKMmGMKBPriMnfmogJorD73w3J5pXYoYDC8c0OiQeLQTmo7cwbUvo6-fsQG_E6khI-ryPHn9FylkfoAImh2WVRxGlirUxia3Ve5YQHSh610UkiHdrgrwB8gvWcbsYn75cGjETs-1Nh30YDferFRxFIcGK3v7P-SWYM0egJnag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fe570c529.mp4?token=Nfrf11tlHlTOJ7kICw46P-t2SWsluM_I-kvU3dApxtr4_SWGcO1D-50Fq37BEpoeZ9O3XqRly4xun4wdrspg1apiJBdAqaHRJvmkait7GPKT7RWvvGTUSHtwNSPjSHWEphTnWwoqYGcU9528fdz_9j02WTrXcI6mLWqxGXI_8JOI-hKMmGMKBPriMnfmogJorD73w3J5pXYoYDC8c0OiQeLQTmo7cwbUvo6-fsQG_E6khI-ryPHn9FylkfoAImh2WVRxGlirUxia3Ve5YQHSh610UkiHdrgrwB8gvWcbsYn75cGjETs-1Nh30YDferFRxFIcGK3v7P-SWYM0egJnag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیبی می‌نوازد:
«نصرالله کجاست؟ بعد از من تکرار کنید: حذف شد!»
جمعیت: «حذف شد!»
بیبی: «سنوار کجاست؟»
جمعیت: «حذف شد!»
بیبی: «هنیه کجاست؟»
جمعیت: «حذف شد!»
بیبی: «با خامنه‌ای چه کار کردیم؟»
جمعیت: «حذف شد!»
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71878" target="_blank">📅 13:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71877">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71877" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/71877" target="_blank">📅 13:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71876">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQ5vQSDTNZpG0NIpL--IRNgijmY2Lvm05vGeUbkSFL-kOGVTgW-PFdHnnK4u3BdVgoqXjLUMtPpMFNCAuxRhODmm-I2um_OZJHJTX2rbKUiOv0ocyirjAcPv4Mhc0jZ9sbf0rLoMHJvv9DVjfJpui9kLzCEhl_DjrBEIDS-RXfWet5FxfCmrUXHWPziFuz9w1SP-ET1tI80b03fMDo9WyRyMic-gu9K1EyQjUZde8KQGgqGS-3aHHoMt_idVyK_cxOPPADfCvP9VLn4I4c-SDYd-jwnoH3E2BKxB1rpAuhPU_UeOF7DgUvIAPLjQ9RteAwqmEUGb0fQxGd-eSC8iLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
استون ویلا
🆚
تاتنهام
آرسنال
🆚
برایتون
بارسلونا
🆚
سویا
دورتموند
🆚
اشتوتگارت
اینتر
🆚
رم
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71876" target="_blank">📅 13:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71875">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e25ecc6de4.mp4?token=SelijWQ3aEdaNwRNsPL7She5Cq9QK5bH5WZXmeolh65xjMi49wv5bod30OdmuijGmiIr166HZJVlg9l_CfBb9B0rDBTkSOYIMt8YONHuh4R1gNjEkxyuNNXgQjg0D3LVRR6RRE6U3MwJiZeHTyI2-i_vC0uRNGjItWg4gNlbEWZkPVvh01fqbKET5mb9zJZ6yfS4hGK92SnPMEbEVgSNB5MPAir-iXUsQHr2HTuM0jvUIkDg6XqjWnE2yy0Dn9zAEKK40XWvE1SHaoy0SxODsDQLuEudCRB5-z-5nD4C5mVfQI3dMrbXTL8jNEAlWtTFy8Ep_YhYKu7oqgZHLKEsIbFUCJ-KgY989OL3pM7dZMM210wWw17fhX4HDHGsVzTWbf-mBvFrZlLZ06JeHxNjkiYEEs7dr1SIi_mWparVvQajwDdHajh9G8aNWVGM48yGbx8GOvQKsIL-bFMxXrpRgzsW-ZkJKCBUXImQgMHe3R-8Ki5pfs4cQw7KQ1p0It9f4LDOguFvZmfY-8isW6hLTlBluecQ3WhoFmhk4ecaxsSFLv-Gc3ooinIPpvFFsV_lB__bGvA1K8SHkG4ouiaOxoZ_knedAC7yuKpU6HsrjYTtst_OFcsf8ajWzzNOoUcUexu2ks_BnMN1nWVwqGY-NXsyULmQiz1lYTeilEsJwvI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e25ecc6de4.mp4?token=SelijWQ3aEdaNwRNsPL7She5Cq9QK5bH5WZXmeolh65xjMi49wv5bod30OdmuijGmiIr166HZJVlg9l_CfBb9B0rDBTkSOYIMt8YONHuh4R1gNjEkxyuNNXgQjg0D3LVRR6RRE6U3MwJiZeHTyI2-i_vC0uRNGjItWg4gNlbEWZkPVvh01fqbKET5mb9zJZ6yfS4hGK92SnPMEbEVgSNB5MPAir-iXUsQHr2HTuM0jvUIkDg6XqjWnE2yy0Dn9zAEKK40XWvE1SHaoy0SxODsDQLuEudCRB5-z-5nD4C5mVfQI3dMrbXTL8jNEAlWtTFy8Ep_YhYKu7oqgZHLKEsIbFUCJ-KgY989OL3pM7dZMM210wWw17fhX4HDHGsVzTWbf-mBvFrZlLZ06JeHxNjkiYEEs7dr1SIi_mWparVvQajwDdHajh9G8aNWVGM48yGbx8GOvQKsIL-bFMxXrpRgzsW-ZkJKCBUXImQgMHe3R-8Ki5pfs4cQw7KQ1p0It9f4LDOguFvZmfY-8isW6hLTlBluecQ3WhoFmhk4ecaxsSFLv-Gc3ooinIPpvFFsV_lB__bGvA1K8SHkG4ouiaOxoZ_knedAC7yuKpU6HsrjYTtst_OFcsf8ajWzzNOoUcUexu2ks_BnMN1nWVwqGY-NXsyULmQiz1lYTeilEsJwvI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنری کیسینجر و توضیح سه مسیر تاریخی ایران:
دولت–ملت
امپراتوری
ایدئولوژی خمینی.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71875" target="_blank">📅 12:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71874">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beaae9822a.mp4?token=hWxcEbk7OK526nHLo26O9RqM7Ng1FRnomayQY21FkFMR0PRAYP8FwHqOVt2I8TyLoQfHlePTW6GAAvrGea4-czwu-CEOv1Pt0X6JRL8hjc4yf6BpwK__7rk_hJ_Pxo7D31HMRZ2olDllAwDkJxsXUlUWUf5UOofMv1399HnUbI54GAMgyH89kkUSy__K9O86Fluh1FBfftO_zKF4DDlbnxbjQmT7kVdb0CwZPifE1o4Vi6n1H3bQ3Iru3NuZOF1lxEo8kHCgNypHBrnVdFQPuS1aooQwvox7Km6FLWnIidoLIKEDlrVak4HJWReAeCfhO5csiBh2iUcq-pVO5gbVcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beaae9822a.mp4?token=hWxcEbk7OK526nHLo26O9RqM7Ng1FRnomayQY21FkFMR0PRAYP8FwHqOVt2I8TyLoQfHlePTW6GAAvrGea4-czwu-CEOv1Pt0X6JRL8hjc4yf6BpwK__7rk_hJ_Pxo7D31HMRZ2olDllAwDkJxsXUlUWUf5UOofMv1399HnUbI54GAMgyH89kkUSy__K9O86Fluh1FBfftO_zKF4DDlbnxbjQmT7kVdb0CwZPifE1o4Vi6n1H3bQ3Iru3NuZOF1lxEo8kHCgNypHBrnVdFQPuS1aooQwvox7Km6FLWnIidoLIKEDlrVak4HJWReAeCfhO5csiBh2iUcq-pVO5gbVcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تئاترهای مملکت این روزا تو وضعیت عجیبی قرار گرفتن؛ گویا شوخی های جنسی برای تئاتر ها آنلاک شده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71874" target="_blank">📅 12:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71873">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77deac1aa1.mp4?token=aKnQ5ZqyU7zRR4UtdwTW3kGj1O1Jtzcj-ioaZMCqQvuzB6WDpD_pAilX_soJgABmEqsgspUcF0POYp15pyxgrZ0vW-9aodYF2VZd6TIRhO2kJ8bDqCuF2JMqEYpFmxl5W7KU7TZMbcbWueXYcGUuNrfw66nT2Yf4hG8CdZa7lR1XhVhNwxNQlrzQxkoooy_gdBHvCvM66HpnPB-FRVoW4mvMJq5vVuV47xKQa2BkWUpVwD0XMSMe2tUcAXfrfFBMngtmcR9RLowBeefPUOP58sx1DyUxFfKdOXI3NyhJIBYOfKq-DbDyj-XCWKE1B6kGQ0lRlW7553iEkwgln2qk-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77deac1aa1.mp4?token=aKnQ5ZqyU7zRR4UtdwTW3kGj1O1Jtzcj-ioaZMCqQvuzB6WDpD_pAilX_soJgABmEqsgspUcF0POYp15pyxgrZ0vW-9aodYF2VZd6TIRhO2kJ8bDqCuF2JMqEYpFmxl5W7KU7TZMbcbWueXYcGUuNrfw66nT2Yf4hG8CdZa7lR1XhVhNwxNQlrzQxkoooy_gdBHvCvM66HpnPB-FRVoW4mvMJq5vVuV47xKQa2BkWUpVwD0XMSMe2tUcAXfrfFBMngtmcR9RLowBeefPUOP58sx1DyUxFfKdOXI3NyhJIBYOfKq-DbDyj-XCWKE1B6kGQ0lRlW7553iEkwgln2qk-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه شغلی در کانادا هست به اسم آتش‌بان. طرف باید فصل تابستان رو در کابینی بالای کوه بگذرونه و هر وقت آتش‌سوزی جنگلی دید گزارش کنه. عمیقا حس میکنم من میتونم خیلی تو این شغل موفق باشم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71873" target="_blank">📅 11:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71872">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d090aca4d2.mp4?token=RRs1HGGzGP3zqXLj74LSFLMTBjsYry9k5UHeL4-6jO_PQfoLWPO2niEMYmNQRIGVtLET2Ij03Pt8yyYp-f1RerA-GrN5xlR-VWb5d4hbCZSROQchqJ_T4GbYzXVU0dKRw0fqc5TxRMdLlrqw1XCjYADYB13HH_hbafAKBzFI6ug-NHNdqJo7Kabrc-xIn53gMSCS9hB7ON1L9Q82TNMFfSsh_HKgz4uOrPYj073MVNvH8tGAxSSmVbOAIIlHm89SRjOf3u7ZRzatiHJ_PVXkgf35xZ1oNADdnBM6NBopFlXGlo1JJ7sUG31Owdw7VnNsfGHzdVOmZaQouCc08ByuPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d090aca4d2.mp4?token=RRs1HGGzGP3zqXLj74LSFLMTBjsYry9k5UHeL4-6jO_PQfoLWPO2niEMYmNQRIGVtLET2Ij03Pt8yyYp-f1RerA-GrN5xlR-VWb5d4hbCZSROQchqJ_T4GbYzXVU0dKRw0fqc5TxRMdLlrqw1XCjYADYB13HH_hbafAKBzFI6ug-NHNdqJo7Kabrc-xIn53gMSCS9hB7ON1L9Q82TNMFfSsh_HKgz4uOrPYj073MVNvH8tGAxSSmVbOAIIlHm89SRjOf3u7ZRzatiHJ_PVXkgf35xZ1oNADdnBM6NBopFlXGlo1JJ7sUG31Owdw7VnNsfGHzdVOmZaQouCc08ByuPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رائفی‌پور:
رهبر شهید به رئیسی گفتند چرا به امیر تتلو نزدیک‌تر نشدی
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71872" target="_blank">📅 11:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71871">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/400c93a6ac.mp4?token=PkJUEouU1cMSzs2vxsUOiiB59mxeJzGctrnarNPMdyRW89TGk9OKwMVTqIPWYxdKfuuKOLTY3sXSrfrvfLORDaoz7Dy2RjYAYjKBWmComLVxPdQx5s0JeiHi4tPm0RLSB2HIQ4o9-y_WnmLPQoTpaYISLfEzxGRo7RYuQ6xCsqWsYx1mLTFbJ8tUbcDLsjODjhHl_QyeGg285GGFJLznVybG36IvqEGzFIbls-Wr6AqZj_gTaRDNxgK7rMrPzjdl0Lgimc9acr8zfVliXRlxVp-Wqsx2ltyK1BrXiLxy7B6lJ_ur-RVnBa4QFKnlYval6_DEO_zSPHVx7LNACLuEqA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/400c93a6ac.mp4?token=PkJUEouU1cMSzs2vxsUOiiB59mxeJzGctrnarNPMdyRW89TGk9OKwMVTqIPWYxdKfuuKOLTY3sXSrfrvfLORDaoz7Dy2RjYAYjKBWmComLVxPdQx5s0JeiHi4tPm0RLSB2HIQ4o9-y_WnmLPQoTpaYISLfEzxGRo7RYuQ6xCsqWsYx1mLTFbJ8tUbcDLsjODjhHl_QyeGg285GGFJLznVybG36IvqEGzFIbls-Wr6AqZj_gTaRDNxgK7rMrPzjdl0Lgimc9acr8zfVliXRlxVp-Wqsx2ltyK1BrXiLxy7B6lJ_ur-RVnBa4QFKnlYval6_DEO_zSPHVx7LNACLuEqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پورن استار معروف ایرانی ملقب به «شیر ایرانی» با انتشار این ویدیو اعلام کرده که مسلمون شده و از خدا طلب بخشش کرده :
کاری به هیچی ندارم ، چرا وقتی میگه بسم‌الله ، با دستاش صلیب میکشه
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71871" target="_blank">📅 10:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71870">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40d28238ee.mp4?token=ILvH1RYswfz9CUi8Ddyx9pcIiTz0RPxaMfHC-TFGFM8KWM5vtkJMSKU7bPUVNh-cr1ZOX50_YOtW3VXuxQOBpe-rbAncjHW_mlXRVieJre6FTf7pu5X4IkvZ6UE7garFs3wyfxQ9AA2XSnOIuhpZXFnmqrF04NQoIRh5d0FnjCm6od3IS5T6vCnGEnPswlwXfSPMYi0mBp8SWg9AuFyRvp3pAJXT_TivsV79lQJFPeQ14t1v50wvizwqj2_M1jmGNQy_xW54ZlBeUApct8r1CCqUXE7hEXd5vcOoZfRkF8TgvYmbB-5iTXgH-Pij56IhAUo55eR6Cwy8HeCNK7SBNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40d28238ee.mp4?token=ILvH1RYswfz9CUi8Ddyx9pcIiTz0RPxaMfHC-TFGFM8KWM5vtkJMSKU7bPUVNh-cr1ZOX50_YOtW3VXuxQOBpe-rbAncjHW_mlXRVieJre6FTf7pu5X4IkvZ6UE7garFs3wyfxQ9AA2XSnOIuhpZXFnmqrF04NQoIRh5d0FnjCm6od3IS5T6vCnGEnPswlwXfSPMYi0mBp8SWg9AuFyRvp3pAJXT_TivsV79lQJFPeQ14t1v50wvizwqj2_M1jmGNQy_xW54ZlBeUApct8r1CCqUXE7hEXd5vcOoZfRkF8TgvYmbB-5iTXgH-Pij56IhAUo55eR6Cwy8HeCNK7SBNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو اسلامشهر ی موتوری خیلی ریلکس و بدون پوشوندن صورتش میاد گوشی ی دختر جوونو به زور ازش میگیره و فرار میکنه :
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71870" target="_blank">📅 10:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71866">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6655905e8b.mp4?token=l0HSVLnTUfB9n-0VUFYOwFknbFMLNKQmItJ22iWEOwVIfVxiuqkAr0OSxEGyCXIbzaJIe7dKEgOvvSGLeDDsMvpVCPrgUWHN1B0JJzCNgkglwz8Gg5lUFbqaSpVy74To0vyy-iebHPvxIfOtfDu4aIiBeeftkK2BeM2oZwWqLVi74IJ9urB-yaqFpuGE7mGdwUqrbP4NPNZIV5qyKvT_Ci_aQThmU2kDJtLSfyfcv6FxM0GWw4b_I1j2raXXzQBfwf7iFG_aUKbWlTKQjzk26kvz8Yc8wvFWWeddAuRMm5HIGBH8TxHOR9nN0glBEUv46xhetG6EayEZgVHaBXwaFw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6655905e8b.mp4?token=l0HSVLnTUfB9n-0VUFYOwFknbFMLNKQmItJ22iWEOwVIfVxiuqkAr0OSxEGyCXIbzaJIe7dKEgOvvSGLeDDsMvpVCPrgUWHN1B0JJzCNgkglwz8Gg5lUFbqaSpVy74To0vyy-iebHPvxIfOtfDu4aIiBeeftkK2BeM2oZwWqLVi74IJ9urB-yaqFpuGE7mGdwUqrbP4NPNZIV5qyKvT_Ci_aQThmU2kDJtLSfyfcv6FxM0GWw4b_I1j2raXXzQBfwf7iFG_aUKbWlTKQjzk26kvz8Yc8wvFWWeddAuRMm5HIGBH8TxHOR9nN0glBEUv46xhetG6EayEZgVHaBXwaFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاید باورتون نشه ولی ایشون دختر نیست و یه فمبوی(پسر) ایرانیه که خیلیا روش کراش زدن و توی تله‌اش افتادن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71866" target="_blank">📅 09:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71865">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbf20c1179.mp4?token=WwJjSQwl1Ni3YP0_877xrSl1TSLbjP6W4trHdyEgcJHos3_Q51qjvgcijKnWYM3PTHZkG0Pd2BDHH7hlPOYd2XV-_GSLLSVtPYsAwmFicLAKdaPkhjzVbXIawl4mxGOT2Pn5-23hY99RZzbmr2_NvkwEtKLVmYAe_PDtFYldHUL8BN1viKVIDodldJ9rYAOV-0UzIIygP0T4ggRKcWPUS5MN4E3x64-12xXF9P54iet5IH8Q-D9H1dzGWpL3iJowYpnaeVN7IOEiePhtmkdxMDfjnKd8L3_p3fGX5aEWqgcEUFPdweu7zD_zIe3RbGeSofla-ElzCmnejXzeNVqbHo3fOungZVtbW6wyophTLD4SHAdMbNXFxtp032A33V3o0A96uY6Gpw9EJ3pqXhGPhSIPSArAueSRBlfg97QjeZGHXYNYGPP689J7wKC168VpfH7hsduKMP4LWvqsSeBhDL3rsg0MZFWXLzNC9j_ZUFUPtMa4P7lrsPkwq8qnZokUpYVDpWs-Z4-pTdpp5KbWf_nUsZXE6Z4SmEZ-DM3lTakJ1pFZps31c1wQKvC-fbyhanN6e6AiMnYI8d6imtRIFhKM4xdixra2BKTtDE00mz9DveQmgczhL8P4XgMALWOiRzTnXzD1N17Kli-tPwXcbrz08AufwQ66RfSGj9ODMtM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbf20c1179.mp4?token=WwJjSQwl1Ni3YP0_877xrSl1TSLbjP6W4trHdyEgcJHos3_Q51qjvgcijKnWYM3PTHZkG0Pd2BDHH7hlPOYd2XV-_GSLLSVtPYsAwmFicLAKdaPkhjzVbXIawl4mxGOT2Pn5-23hY99RZzbmr2_NvkwEtKLVmYAe_PDtFYldHUL8BN1viKVIDodldJ9rYAOV-0UzIIygP0T4ggRKcWPUS5MN4E3x64-12xXF9P54iet5IH8Q-D9H1dzGWpL3iJowYpnaeVN7IOEiePhtmkdxMDfjnKd8L3_p3fGX5aEWqgcEUFPdweu7zD_zIe3RbGeSofla-ElzCmnejXzeNVqbHo3fOungZVtbW6wyophTLD4SHAdMbNXFxtp032A33V3o0A96uY6Gpw9EJ3pqXhGPhSIPSArAueSRBlfg97QjeZGHXYNYGPP689J7wKC168VpfH7hsduKMP4LWvqsSeBhDL3rsg0MZFWXLzNC9j_ZUFUPtMa4P7lrsPkwq8qnZokUpYVDpWs-Z4-pTdpp5KbWf_nUsZXE6Z4SmEZ-DM3lTakJ1pFZps31c1wQKvC-fbyhanN6e6AiMnYI8d6imtRIFhKM4xdixra2BKTtDE00mz9DveQmgczhL8P4XgMALWOiRzTnXzD1N17Kli-tPwXcbrz08AufwQ66RfSGj9ODMtM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
«آیا خواهان جناح چپ هستید؟ (جمعیت: نه!)
آیا خواهان جناح راست هستید؟ (جمعیت: بله!)»
«آیا خواهان تشکیل کشور فلسطین هستید؟ (جمعیت: نه!)
آیا خواهان کشوری یهودی هستید؟ (جمعیت: بله!)»
«آیا می‌خواهید تسلیم شوید؟ (جمعیت: نه!)
آیا می‌خواهید بجنگید؟ (جمعیت: بله!)»
«این جوهره‌ی این انتخابات است: یا چپ، یا راست.»
ما در جناح راست هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71865" target="_blank">📅 08:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71864">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🦖
اینجا فقط ضری ب‌ها نیستن که می‌درخشن...
🦖
چندتا Star آماده‌ست برای کسایی که توی قرعه‌کشی شرکت کردن. شاید قرعه به اسم تو بخوره؛ امتحان کردنش که هزینه‌ای نداره!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71864" target="_blank">📅 01:36 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71863">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/news_hut/71863" target="_blank">📅 01:36 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71862">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">#فوری؛دونالد ترامپ، رئیس‌جمهور، «قانون لیندزی او. گراهام برای اعمال تحریم علیه روسیه و ایران (مصوب ۲۰۲۶)» را امضا و به قانون تبدیل کرد.  این قانون، تحریم‌های قانونی، تعرفه‌ها و ممنوعیت‌های اعمال‌شده علیه روسیه را گسترش می‌دهد و تحریم‌های موجود علیه ایران را…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71862" target="_blank">📅 01:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71861">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CcaX-gScXZXOyhfnSzYkBgB4xRMPYdL37e_HQS9NDrf2Et08wUb7UGjY3a3YfcvU7CfFdXswdHEyja01EnEid7W4pglbSeVxZTqB65ySJ3-UIQ_89GkYb2wiNWN3JIeRy0MrDRGy-FS4V_jr3K4kowD5fGI4ght2nxyPCRCvNfZrOvVnJbsim1dZPPyCEFkI9EGnw4D579na3v2iAhijOmG3MRh1oFXEt4iDqWxlDAN3HGQlpoGpfRIiv5TAqejthyQtLftEZjGRxXgeFanMU7xfgTtN8PS5mJBV2gSql4WT7jG7aSrOYQx_gtNd3v2iL4fG_8G6TgzEABWjk_VNHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛دونالد ترامپ، رئیس‌جمهور، «قانون لیندزی او. گراهام برای اعمال تحریم علیه روسیه و ایران (مصوب ۲۰۲۶)» را امضا و به قانون تبدیل کرد.
این قانون، تحریم‌های قانونی، تعرفه‌ها و ممنوعیت‌های اعمال‌شده علیه روسیه را گسترش می‌دهد و تحریم‌های موجود علیه ایران را تمدید می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71861" target="_blank">📅 01:24 · 28 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
