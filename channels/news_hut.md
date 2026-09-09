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
<img src="https://cdn4.telesco.pe/file/v86Oc6utbMeeY0UQf6ZixNb1XZ5qEeJoSvUnyi_2q889zebKEI5GeWFesJ5Tn0PNL1Zu8wMPsqOsCbj4Q5zHcPRE9JN7igugiS6-GgPzE9-dqnIKbXU-7wUHoGol2WjLWabd0uys01_5AyyhV_4MVNjv4xoBYWLujSJooPlb3z2uvHrJlLeSIoR_IeidmoBTYgNFTeaedtQLnptNy5Qya12DCn6U06EJ8fivA5g9WZC3YArLl0IX7O6bbsIyu9x59X5OyciGB4CmgiVgcvvAbjZ0pVlqxMzBEP4HbU8FfJ3VppybWlrNjAUIQbQ4jYXxCLiqyefi1Ffcsh1Xe5KbRg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 111K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-18 22:26:57</div>
<hr>

<div class="tg-post" id="msg-71378">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c27e89aeff.mp4?token=BYj5ZDcfcslyuQXV_tY2NHd7ME7UMGefEPksdh_MjCJWgf5UYJb75I7zQp9nKHUXS74xIADWhSz0229SQBeNCpSxXgg_GRHsTfildTm9o7MQ7_AfnwU3d-VydE_Cz6zI5z5Df0vcioIG3oIuKyqcZjXbritf215UNwIqprszhggvdbXaBoy2Zg-TwIiFfY5n926DrWVNClhOVq8QPwkUC0NFT6Dm3ifX8u4BvOrWdkoYnBbiBH2TFZu1WparJD881Q9OkCs93W9hJGcjJ_HUjS0Y09KLcnkhU4c157SbQokapbykpEeAn6eX5IxxN_US9NuxEUlqZ9qWyzFiXQYL_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c27e89aeff.mp4?token=BYj5ZDcfcslyuQXV_tY2NHd7ME7UMGefEPksdh_MjCJWgf5UYJb75I7zQp9nKHUXS74xIADWhSz0229SQBeNCpSxXgg_GRHsTfildTm9o7MQ7_AfnwU3d-VydE_Cz6zI5z5Df0vcioIG3oIuKyqcZjXbritf215UNwIqprszhggvdbXaBoy2Zg-TwIiFfY5n926DrWVNClhOVq8QPwkUC0NFT6Dm3ifX8u4BvOrWdkoYnBbiBH2TFZu1WparJD881Q9OkCs93W9hJGcjJ_HUjS0Y09KLcnkhU4c157SbQokapbykpEeAn6eX5IxxN_US9NuxEUlqZ9qWyzFiXQYL_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
کمی بعد، اما درست بعد از انتخابات، چون آنها دوست دارند اوضاع به این شکل باشد، اما درست بعد از انتخابات، قیمت نفت رو به کاهش خواهد گذاشت. قیمت‌ها پایین خواهد آمد و فکر می‌کنم قیمت بنزین را پایین خواهیم آورد، به زیر ۲ دلار در هر گالن.
@News_Hut</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/news_hut/71378" target="_blank">📅 22:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71377">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/34c7f74659.mp4?token=NBNmLCCdQkqJVbn20bRJXswAXBF9xErgpIkcGNXDLHNYD8_uLvbVwYSn4FXg2J37rE-1kQ2odXYxPz-tlc8IN6Eg9tp4Yl_YVkDwDLGpNkRhWb5YXcN1e1bx0TJy1XAHdILB7KrWrDug2isC4dw91atl1ap53ptH_fPio9T35QFQmCKtCWGJxGr6YuKXNgAkugqD28w8O6518MSfhMVRsy7ycBTWPW9gbsV-1x2OCgpqOSzb5GQV6YdIUxr2ZJBnIKBBVmk2htBTFMEr_RjE4aVC7tNEhFKwFXcbXGIPXqMEaTnqA9oravMcWTl0KGFx713SwzKCfydKj1Xv9BPj9w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/34c7f74659.mp4?token=NBNmLCCdQkqJVbn20bRJXswAXBF9xErgpIkcGNXDLHNYD8_uLvbVwYSn4FXg2J37rE-1kQ2odXYxPz-tlc8IN6Eg9tp4Yl_YVkDwDLGpNkRhWb5YXcN1e1bx0TJy1XAHdILB7KrWrDug2isC4dw91atl1ap53ptH_fPio9T35QFQmCKtCWGJxGr6YuKXNgAkugqD28w8O6518MSfhMVRsy7ycBTWPW9gbsV-1x2OCgpqOSzb5GQV6YdIUxr2ZJBnIKBBVmk2htBTFMEr_RjE4aVC7tNEhFKwFXcbXGIPXqMEaTnqA9oravMcWTl0KGFx713SwzKCfydKj1Xv9BPj9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه هموطن بعد از گرونی بنزین زد به سیم آخر و از بالا تا پایین مسئولین رو یکی کرد.
حاوی الفاظ رکیک، هندزفری لازم
@News_Hut</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/news_hut/71377" target="_blank">📅 22:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71376">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SGBjchYjTo1VsigFjIPPFjAZAndno88yVrHfL9EinoHefCoWAUEfAfGrzpZzZuefo-f7GiQcdsAkxqlFsPkiQRv6pL9qWflMkuIhuNOx7ENoVqxeB-rDfQAcAl28iCKtk7vMGbygr8ccbFFMNXfAIJVtvI5_dHhsNjHWQuwGJ3_5UnWhhoBHsw0WH1NjrsW5dgcQ6r0zxUUUVR78Ty0m-S6hC33MvQRej0_eXbdH8Ef7nDGJsuj4ATA35Wl8HqsoUbiLTROR_7Y3sho-Z1gw0D-Fo2UwtHyooqRTRvJuOmYP8TnqH_WFDTYuKXF5Ki38u-7m7VwikZfG_vianrHj9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
🇺🇸
🇺🇸
به گزارش «نیوزنیشن»، دونالد ترامپ همچنان در «بال غربی» (West Wing) حضور دارد و طبق برنامه، هنوز عازم دالاسِ تگزاس نشده است.
ترامپ در حال دریافت گزارش اطلاعاتی به همراه جی‌دی ونس (معاون رئیس‌جمهور)، پیت هگسث (وزیر دفاع) و ژنرال دن کین بوده است.
احتمال می‌رود این جلسه پیرامون موضوع ایران باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/news_hut/71376" target="_blank">📅 21:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71375">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d22f299161.mp4?token=c--xFjwwPjfI7-nKX6w09apkVJ3R-tf5EJpbNfJdk2IlpieoZxnIlez5hG5ulUkr9VpnuI9Cdt2VmEzFkGdASSdMskkrb7xkxOnB1_L125P9EabAx6Oe0aY4vlFUZd95i_lC3Gb1bP5CTduco4VAz0JqjU5lOKrinQZdprWZCk4_nfx4jXAhpJ9Q507Xx3EwCTGud4hLUeJDUERrurSpPucwdltL-ssigFVs8UnTPODsEKFsdwqVrHgU1g6wMU-t4BAcpCnJaI0g4NVnk0zO7UVd8--aQR8-Mtc1T-XpQZH7PgE06eb46TtBTWnOoynJGvqiYRihkxYkwghHZur9Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d22f299161.mp4?token=c--xFjwwPjfI7-nKX6w09apkVJ3R-tf5EJpbNfJdk2IlpieoZxnIlez5hG5ulUkr9VpnuI9Cdt2VmEzFkGdASSdMskkrb7xkxOnB1_L125P9EabAx6Oe0aY4vlFUZd95i_lC3Gb1bP5CTduco4VAz0JqjU5lOKrinQZdprWZCk4_nfx4jXAhpJ9Q507Xx3EwCTGud4hLUeJDUERrurSpPucwdltL-ssigFVs8UnTPODsEKFsdwqVrHgU1g6wMU-t4BAcpCnJaI0g4NVnk0zO7UVd8--aQR8-Mtc1T-XpQZH7PgE06eb46TtBTWnOoynJGvqiYRihkxYkwghHZur9Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🤡
اوستاد خوش‌چشم تحلیل‌گر ارشد صداوسیما:ما به سوی یک درگیری تمام‌عیار و کوتاه‌مدت در پاییز می‌رویم.
@News_Hut</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/news_hut/71375" target="_blank">📅 21:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71374">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rNOiIN7V-TVXvn0P-7r_pAQ_g4R1viyxVnoX3Z7c-zA0_RLjhJ5DgLzyPpAflCN4BpQGcotdMoh5Bw7H40w6YCf3JsXu5e5C_IkGW47A7A1Z0w4iJGXnYzH_AOkwWQE8cNk78D01dLSPoyxz0BqVlZUrlzfXSvQcTwKUJibH6lBQE4P_NQHozAiwhPdRGzQrBvBFXz-yEfmrSXA_HmRWgkFV3bk2Z2KtOzXqOhKupwuvlICCp0C1F_JdfNFo0DLDo_lY1DBRrFKVJU60KoGc1OKYjtMyieRh9HHAisSw0NEssvmOlCK93HsXqwR5Y1imZ-wqiW49TMouvVy7_sp6RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
تصویری زیبا از رعدوبرق دیشب تهران.
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/71374" target="_blank">📅 20:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71373">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69c9063c46.mp4?token=GvL6ypJg7W46w0Xe0gX_Y3CfRqJ2yb2gXRiZcxqboloUIdHRxwBL_W8OCZKkyPzhcPqu06aggrc0ol07_I9N178FpFSW06E6tDdN6GQKU6kDuzs75BmBpTjaF4bxtgGvfY8LaLYcfUux4gyjA8bnrKIQIOuccXV46paMn_ZyHugDEsddC2DVkpwjjL1eT6HxtXRj1QT_yaQhioQicvNle_Kxa96F_NPPi6asaC_pZ9KaK-eNEc-u-pEyAjHgiGWqDTfsepz2f2NQacbPj6H5epbbnA1le-nFfIgtMAl8Fh-7tOhtyeKfziFB1J8LBmJHeMDyKxOosbWoh3Mk07HofQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69c9063c46.mp4?token=GvL6ypJg7W46w0Xe0gX_Y3CfRqJ2yb2gXRiZcxqboloUIdHRxwBL_W8OCZKkyPzhcPqu06aggrc0ol07_I9N178FpFSW06E6tDdN6GQKU6kDuzs75BmBpTjaF4bxtgGvfY8LaLYcfUux4gyjA8bnrKIQIOuccXV46paMn_ZyHugDEsddC2DVkpwjjL1eT6HxtXRj1QT_yaQhioQicvNle_Kxa96F_NPPi6asaC_pZ9KaK-eNEc-u-pEyAjHgiGWqDTfsepz2f2NQacbPj6H5epbbnA1le-nFfIgtMAl8Fh-7tOhtyeKfziFB1J8LBmJHeMDyKxOosbWoh3Mk07HofQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
⭕️
#فوری
؛شورای حکام آژانس بین‌المللی انرژی اتمی امروز، ۹ سپتامبر ۲۰۲۶، قطعنامه‌ای را تصویب کرد که بر اساس آن، موضوع هسته‌ای ایران به شورای امنیت سازمان ملل گزارش می‌شود. این نخستین ارجاع از این نوع در حدود ۲۰ سال گذشته است.
۲۳ کشور موافق قطعنامه بودند.
روسیه، چین و نیجر مخالف بودند.
۸ کشور ممتنع دادند و یک کشور رأی نداد.
🔴
قطعنامه با ابتکار آمریکا، بریتانیا، فرانسه و آلمان ارائه شد.
دلیل اصلی اقدام آژانس، عدم توانایی بازرسان در راستی‌آزمایی کامل مواد و فعالیت‌های هسته‌ای ایران و پاسخ نگرفتن درباره آثار اورانیوم کشف‌شده در برخی سایت‌های اعلام‌نشده عنوان شده است.
آژانس همچنین می‌گوید به دلیل محدودیت دسترسی، نمی‌تواند با اطمینان درباره میزان و محل ذخایر اورانیوم غنی‌شده ایران اظهار نظر کند.
⚠️
اقدام بعدی در شورای امنیت خواهد بود و هرگونه اقدام الزام‌آور جدید در آنجا با توجه به حق وتوی احتمالی روسیه و چین با موانع جدی روبه‌روست.
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/71373" target="_blank">📅 20:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71372">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fc965eb9f.mp4?token=A8aVUNQCSIB7c9l5MXtXcf2JTvPF2HYGbgBJrYQK6xYSWi-1tlHrxBzuUQmsfpXVXHgnIwhikAUguxFwkWvuNhxLXw9yAQnab6iZjJmEfeK85mDZQG-k-FSvLRISOxvTr8TMNJoBcSi49L6k4gvfzM_sjcMHeQrJPEZ9DyvCz_iGKOhU3B2cHcGDyKiWufMtbgQxYq_h1PPDpzxuAntanECiyiThtNx4zeOhED1snx6JezhhwyMRKEP6Hone4rrmEKcTi8t2DzKxpcFnZNNoIQJmZZ3WAa4LW6fGjhhPLa0Soe1gAmrRrhwfFwCPgN-f4dk3xqWHdaQhC-FTfikuBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fc965eb9f.mp4?token=A8aVUNQCSIB7c9l5MXtXcf2JTvPF2HYGbgBJrYQK6xYSWi-1tlHrxBzuUQmsfpXVXHgnIwhikAUguxFwkWvuNhxLXw9yAQnab6iZjJmEfeK85mDZQG-k-FSvLRISOxvTr8TMNJoBcSi49L6k4gvfzM_sjcMHeQrJPEZ9DyvCz_iGKOhU3B2cHcGDyKiWufMtbgQxYq_h1PPDpzxuAntanECiyiThtNx4zeOhED1snx6JezhhwyMRKEP6Hone4rrmEKcTi8t2DzKxpcFnZNNoIQJmZZ3WAa4LW6fGjhhPLa0Soe1gAmrRrhwfFwCPgN-f4dk3xqWHdaQhC-FTfikuBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇸🇦
🇾🇪
ساعاتی پیش، چندین حمله هوایی عربستان سعودی در حمایت از عملیات «شورای رهبری ریاست‌جمهوری» (PLC)، مواضع حوثی‌ها (انصارالله) را در جبهه مأرب یمن هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/71372" target="_blank">📅 19:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71371">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/71371" target="_blank">📅 19:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71370">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb4ebfee62.mp4?token=sQ-kB8zsbUe9O5OL4U0NNApGJ-fy3U5rO-z8IDIF-cHCxvOpW-F84FkBaxK3aXt7P86ZPOgdg7DhEy8WdtYb1VJeyKfn3zLDoFCXZ2eiZMqlkQPbOc-34QMv3wkcfMYdSoRGBsI0GSYiNg5V1jqPAVnYyEcesSm_q-STvKyRlBja8vvGG3pUUuXo5y1BjghrEARiG1_behb6IGTIwyqh_Bfrl8txnNIp7ZDMDLFP1NLisjwW-JP_ZpjkVeZ9KcCZ0nYFn9cdSRS8Y1c0sFbmzItfDPpLE-NKjT0LFuYHVJKPLrd-hUS3VeLrzXqE1n5H_NB7Jgv70ilJK3nHDtxPgqAIDyxRaO5-3WQOrttPODZnbH64PPzm_bdeLxb0yzWVE7_Sa5XTVkyVuZrhaTxtuWdyYTvwijQzryxNsIZcLI9hVLtAt2CrYtnC8TZ_WTuoYEKhZAWpMb5tBZm7h5mtXntmt0iFaS7w_iRrEjkc75sir_ZY-wMrtp9V46OEsrzxzfhYRJYPzl3MvFKX2aPx4H8x4vQdFjS364_mZ5iv8jiZ25XA67PkWhne1mqtpNBkd7rtpdAaim8LWqUJNeTAGfxxCyB-MrKneMwMRzZuiwo8eMHgICPkKqCKeLzNgBUOW863Yam0VH7x78DRyy7XcPhuz9cBzcUTDU1Jqm78nIs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb4ebfee62.mp4?token=sQ-kB8zsbUe9O5OL4U0NNApGJ-fy3U5rO-z8IDIF-cHCxvOpW-F84FkBaxK3aXt7P86ZPOgdg7DhEy8WdtYb1VJeyKfn3zLDoFCXZ2eiZMqlkQPbOc-34QMv3wkcfMYdSoRGBsI0GSYiNg5V1jqPAVnYyEcesSm_q-STvKyRlBja8vvGG3pUUuXo5y1BjghrEARiG1_behb6IGTIwyqh_Bfrl8txnNIp7ZDMDLFP1NLisjwW-JP_ZpjkVeZ9KcCZ0nYFn9cdSRS8Y1c0sFbmzItfDPpLE-NKjT0LFuYHVJKPLrd-hUS3VeLrzXqE1n5H_NB7Jgv70ilJK3nHDtxPgqAIDyxRaO5-3WQOrttPODZnbH64PPzm_bdeLxb0yzWVE7_Sa5XTVkyVuZrhaTxtuWdyYTvwijQzryxNsIZcLI9hVLtAt2CrYtnC8TZ_WTuoYEKhZAWpMb5tBZm7h5mtXntmt0iFaS7w_iRrEjkc75sir_ZY-wMrtp9V46OEsrzxzfhYRJYPzl3MvFKX2aPx4H8x4vQdFjS364_mZ5iv8jiZ25XA67PkWhne1mqtpNBkd7rtpdAaim8LWqUJNeTAGfxxCyB-MrKneMwMRzZuiwo8eMHgICPkKqCKeLzNgBUOW863Yam0VH7x78DRyy7XcPhuz9cBzcUTDU1Jqm78nIs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پسر‌بچه ارومیه‌ای که چند وقته به شدت ویدیو هاش وایرال میشه موزیک جدید داده بیرون
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/71370" target="_blank">📅 19:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71369">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/696aa56e23.mp4?token=F4kW1sC9NbybkpJf3P7f4LSKXBzReg2t5TopkSswMZq7c_RzDljKPgj4dXfWczl_YX4t92m7vqcSLATtEBMFb4idt1NXZsSAlfyXwE5g6Dj8aQ5oR3X-6BEyxrwh2tCCuo6sg3IneZV7V8jkLhVy7xoNbayqSE-OcNoA-FoWxvockqZjFp0IrtaHihNmr-lQg5dtUYzZEtXy8iV0pTRDDA_Zckft1wWcdTykEnG2ahBohWGcyKJV4LuMYuR_8Ptzxj4oFH2KP_9N-05ZAjWD8hVk8r_qZUikU4gv9dSU0IFlav096DBCJhLfL1oL0IKQu7vs-RJPCHQsjAOUBkYdKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/696aa56e23.mp4?token=F4kW1sC9NbybkpJf3P7f4LSKXBzReg2t5TopkSswMZq7c_RzDljKPgj4dXfWczl_YX4t92m7vqcSLATtEBMFb4idt1NXZsSAlfyXwE5g6Dj8aQ5oR3X-6BEyxrwh2tCCuo6sg3IneZV7V8jkLhVy7xoNbayqSE-OcNoA-FoWxvockqZjFp0IrtaHihNmr-lQg5dtUYzZEtXy8iV0pTRDDA_Zckft1wWcdTykEnG2ahBohWGcyKJV4LuMYuR_8Ptzxj4oFH2KP_9N-05ZAjWD8hVk8r_qZUikU4gv9dSU0IFlav096DBCJhLfL1oL0IKQu7vs-RJPCHQsjAOUBkYdKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز تو بجنورد، فردی که سال‌ها با معلولیت شدید تو یکی از خیابون‌های شهر دیده می‌شد و مردم هر روز بهش کمک می‌کردن؛
به محض دیدن پلیس کامل درمان شد و درلحظه به‌طور کامل کاملاً شفا گرفت.
طبق گزارشات این فرد روزانه چیزی بیش از 20 میلیون‌تومان درآمد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/71369" target="_blank">📅 18:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71368">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a8d769b56.mp4?token=Djc2buSiJ0pCKkotMSHkZt3L0-kUTvmZ-c7GBLMj3R66acEyp0_GuCni1L1AUdsMG9rnQHlB2tIdYdVM--IN3FOhR8vpMo34rANzVOCE9pzfJtJpYlagqor2zutCOqBHMChSPPdrQQ4S6gcVlEay2a6PVg1CNvHay3O7Mv4XfX3PVH7S8YcX5dLQT7vabGTT3It52Rr_fCrzT9MtKAXP1X2Rg_0QmeUTulXnu8frH8Ynn-uk9DgU_76AdTYvzr-zcNKS_KT11xjjW-HwjlV488U0dAzzxvfn8T9bvQPFOTVuYllFbe4xXvOtr7_-uR8fLfYjWsphkacrPd1AnNxCJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a8d769b56.mp4?token=Djc2buSiJ0pCKkotMSHkZt3L0-kUTvmZ-c7GBLMj3R66acEyp0_GuCni1L1AUdsMG9rnQHlB2tIdYdVM--IN3FOhR8vpMo34rANzVOCE9pzfJtJpYlagqor2zutCOqBHMChSPPdrQQ4S6gcVlEay2a6PVg1CNvHay3O7Mv4XfX3PVH7S8YcX5dLQT7vabGTT3It52Rr_fCrzT9MtKAXP1X2Rg_0QmeUTulXnu8frH8Ynn-uk9DgU_76AdTYvzr-zcNKS_KT11xjjW-HwjlV488U0dAzzxvfn8T9bvQPFOTVuYllFbe4xXvOtr7_-uR8fLfYjWsphkacrPd1AnNxCJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بازی مناسب برای جوانان خاورمیانه ای:
یه سایته یه بازی ساخته، میری توش بمب اتم مورد علاقت رو انتخاب میکنی و میزنیش تو شهر مد نظرت و بعد بهت میگه چند نفر رو کشتی
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/71368" target="_blank">📅 17:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71367">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCrMBgiod3AAtxGHnbsryD4SYpptlUHSFRa-V4eusO2gWJ5zmVQkXtKk598FWyhcjiKI8xeuJYQXCN74ixaiUqzTG4vapo1m24_HDaLh3wY802KwzJppVwBZvhy3RYZSjRjDqJ4mIFLz2wtb828r5AsantxirbwjN_ZEua6FxsLRr0nXjSdfH_HUNAbvusccorzWJMM7kb4daWcd55XPvOa-GKIIxMEQVE8bXRx1Dg1y_Bf7s_rXWXEGHoI_m_dkxg51qyNqkxsDxT81JjOMX_2yW01Rxpksj4yxxY6jnLaNRsLVif4_VqZKHK1b2MpAUEyD_hGONBO5vBViXNFnYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇺🇸
📰
سی‌ان‌ان:ایران به سرعت در حال ساخت یک تأسیسات هسته‌ای مشکوک است که در اعماق کوه گرانیتی نزدیک نطنز - ملقب به "کوه کلنگ" - دفن شده است و تصاویر ماهواره‌ای افزایش ساخت و ساز در سال 2026 را نشان می‌دهد.
این سایت احتمالاً برای محافظت از سانتریفیوژها یا کارهای غنی‌سازی فراتر از دسترس بمب‌های سنگرشکن فعلی ایالات متحده طراحی شده است.
ترامپ تهدید کرده است که به آن حمله خواهد کرد ("ما ممکن است خیلی زود کلنگ را بزنیم")، اما بزرگترین بمب غیرهسته‌ای پنتاگون ممکن است به اندازه کافی عمیق نفوذ نکند.
نشانه‌ها نشان می‌دهد که ایالات متحده در حال حاضر روی این مشکل کار می‌کند: یک روز قبل از شروع جنگ، یک آژانس سلاح‌های کشتار جمعی پنتاگون قراردادی اضطراری برای تعمیر یک تأسیسات آزمایشی زیرزمینی که در گرانیت در وایت سندز حک شده بود - مرتبط با شبیه‌سازی حملات به عمیق‌ترین پناهگاه‌های ایران - امضا کرد.
یک بمب "نسل بعدی نفوذگر" در حال توسعه نمونه اولیه است.
تحلیلگران CSIS می‌گویند کلنگ هنوز عملیاتی نشده است، اما ساخت و ساز از حفاری به ساخت و ساز داخلی و سخت شدن تغییر می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/71367" target="_blank">📅 17:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71366">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a6e3b3343.mp4?token=A0YdovehugeydJExYFcX_1NGfFkb9_kFDCrNGdWS5Ft-yYcQlh_y_w4QbtJbsLSH2D6wgQG-7FWrsgJ600R9JrWGU4ri9NuE7JQUoji8OCDdlsJhOjid-IrFGR2TtNyeBQZSicQd5mh4MlIpz6Klw4_yMfgWNlwu2OIPx-viH0Iz4LA1HiAOolbhPiFEhMgDCkvDl5q3x3Fx1xoYE9qAwBDmJbBP5XMYGStibT0jvZH3Uat9sIv7-PBlKzZm5rEvbAH6YWc3_ubkGhaEcXB0ZV_GWL3NmTY1wewejRivFwE54IbMWTucH68doXXH4huFMzR-CyP0p7UHY8ap5RQDBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a6e3b3343.mp4?token=A0YdovehugeydJExYFcX_1NGfFkb9_kFDCrNGdWS5Ft-yYcQlh_y_w4QbtJbsLSH2D6wgQG-7FWrsgJ600R9JrWGU4ri9NuE7JQUoji8OCDdlsJhOjid-IrFGR2TtNyeBQZSicQd5mh4MlIpz6Klw4_yMfgWNlwu2OIPx-viH0Iz4LA1HiAOolbhPiFEhMgDCkvDl5q3x3Fx1xoYE9qAwBDmJbBP5XMYGStibT0jvZH3Uat9sIv7-PBlKzZm5rEvbAH6YWc3_ubkGhaEcXB0ZV_GWL3NmTY1wewejRivFwE54IbMWTucH68doXXH4huFMzR-CyP0p7UHY8ap5RQDBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر مسی رو پیدا کرده بهش میگه بگو علی تولدت مبارک
😔
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/71366" target="_blank">📅 17:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71365">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71365" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/71365" target="_blank">📅 17:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71364">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/as6w2wIf2m3RlcQvoIHR7VI0mNPz1-liWmG17TY5haVDDzppgN6MbuOU9Hv5XgIRMJ0O1Lcjv7W5xMcK69mYKPqXjPFLosBFHr-CshWtBhbpI6phNuNfTc9y8ImmnSiP38LSi35z3-87uTdclg5Fae-_4ocuZ6fgWjooMSpmS65vCy7q1VXHcXMNczsuDb3Y0CgBusRiRJ-32t8_RVVGQKVoSRc0-AAkaU8vQ1YurkK0Or9rjsvqZkxZarCQwlq6cqw3Lj3P2savsbQPClY1BfE4iZip5b8l7NYp02Tl7FE2OmIzOxTcjtxcM5s85pE_ATTh-CETE7M1GjSiD-hohA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
آرسنال
🆚
ناپولی
⚽️
🎯
این نبرد حساس
چمپیونزلیگ
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📊
نگاهی به آمار ۲ تیم در ۵ تقابل اخیر:
⚽️
آرسنال: ۵ بازی ۳ برد، ۱ تساوی، ۱ شکست و ۷ گل زده
⚽️
ناپولی: ۵ بازی ۱ برد، ۱ تساوی، ۳ شکست و ۴ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/71364" target="_blank">📅 17:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71363">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146bbc1159.mp4?token=hHuoz8uQgK3qBOENQsSa8Cvi20snGdWRlpxRtS0JTeyW2EsYk00IJMXxKtCsrT5sN6Vvyh-po5Rzib-SBDF6FWrytK5sqNb1kwtDaoKh6cBa11zthOypYvelqaOY5ysy6Opswm96E3SAB1OHttTIY1zBeOrj_CEQ9904Vg11747TY3balMTHb_UAcmj9UHWUr5tujKjRY5UlpaRVsXeoE06bOuPMBLkcOtT-xMmcyhVtBfvD3bta1RjrZhYxI8trcmCb5v7ai3Htfd1GwCmOBv4UWsrMbLFh03H8Z1ONoQVkDChMvuwQHyttxfQDJ3ebgaWqvBiwmV6pRqPY4CId3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146bbc1159.mp4?token=hHuoz8uQgK3qBOENQsSa8Cvi20snGdWRlpxRtS0JTeyW2EsYk00IJMXxKtCsrT5sN6Vvyh-po5Rzib-SBDF6FWrytK5sqNb1kwtDaoKh6cBa11zthOypYvelqaOY5ysy6Opswm96E3SAB1OHttTIY1zBeOrj_CEQ9904Vg11747TY3balMTHb_UAcmj9UHWUr5tujKjRY5UlpaRVsXeoE06bOuPMBLkcOtT-xMmcyhVtBfvD3bta1RjrZhYxI8trcmCb5v7ai3Htfd1GwCmOBv4UWsrMbLFh03H8Z1ONoQVkDChMvuwQHyttxfQDJ3ebgaWqvBiwmV6pRqPY4CId3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
دیروز تو سمنان عرزشیا برای مجتبی خامنه‌ای جشن تولد گرفتن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/71363" target="_blank">📅 16:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71362">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48ece16841.mp4?token=GokGvW-bZ7cqZyBcEKSGkGXYvy3BavgL29oqacy6VulXGoFwh5KiymuL12NDHLN2atatr2d8qdyYnjMoswkA-AZ33A2VwgaZaxgaZxH-c3u9LxaM01PGOx6gysKkiOwqiY0gY5ekLHcjQhaVrNmxrAg2EqJNRYVKlE3hbpxEg1hE3OowXC1KtttSuw96KtX4QzSG4RAgk6o7jXHfFLkL_Z9p8k7fS6dqWxayTqVhTCrGzOYlLHtU-m6a4ECZnnx1AHg6AWEyfRAp4zI7BZfZNGaA3lid1y8KnD8VqgRYYQZw6maUUG_vnL4m9iiYntORUbJNmoklvX-wAnvbgmOCRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48ece16841.mp4?token=GokGvW-bZ7cqZyBcEKSGkGXYvy3BavgL29oqacy6VulXGoFwh5KiymuL12NDHLN2atatr2d8qdyYnjMoswkA-AZ33A2VwgaZaxgaZxH-c3u9LxaM01PGOx6gysKkiOwqiY0gY5ekLHcjQhaVrNmxrAg2EqJNRYVKlE3hbpxEg1hE3OowXC1KtttSuw96KtX4QzSG4RAgk6o7jXHfFLkL_Z9p8k7fS6dqWxayTqVhTCrGzOYlLHtU-m6a4ECZnnx1AHg6AWEyfRAp4zI7BZfZNGaA3lid1y8KnD8VqgRYYQZw6maUUG_vnL4m9iiYntORUbJNmoklvX-wAnvbgmOCRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مراد ویسی:
جمهوری‌اسلامی سربه‌سر اسرائیل نمی‌ذاره، چون می‌دونه اونا نمیان "نفت‌کش" بزنن.
اونا میان "نعش‌کش" راه می‌ندازن
.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/71362" target="_blank">📅 15:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71360">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBtC34mpGmiSxrADZdiCRA7mlUCVprzJhM0v5MdCyhQJR077Y67jlCo2TiC1zj9UaFIHKSYm_XAKc6C5mXHytuw3sxtEQDgaAxPyJXsepDi52XveqQQilP6EI0sfC6KW-UC8hbBqftH0COTD5gNdPQNs9rvcABZ-CKW_eC8pouCrUh6EeKctjjPVkCXARaHr3AUSVm-GdcFD7RldCwQimjLvjO9kvclVmLKViZYglQ_aehhEIX7rXP8146mmZkVS5ihnBi97J5dOZWYgo-QRRJD_PngKwCaBpWIf7tHA7kmu_wLnbl9BpD9N5vWfbymnuFoW6MqeaUfVg69_Dfcn-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7f399e219.mp4?token=n0y5XY5huycwFlZz9behA351PAyWqbWGRiMSGVXFnYccN0Et3fTSdveCO3DdhzlwQTnZ3BUYNczRQKsFMxkuNpJfYAamKirJG8fBSS-HdOGMwsikMt4XZfCzqBC_MghBHPNASNmm7_GjyBXCblJGrjqt1YkPPXgZiQpAyD4P85EuuYWpU0ihoRaibXsHmIsXDZ8xAC6rzh7UPAJUqRyW3mhd6j4T-E0LrLSnwcuYdFXuohWNmdBg1fXGiq_oPSleBfSgsJ5txFe4g9D8nSMLl_mvmER4CfCu2OI77_E6zy4CAe0-xXsMrVJf31KbcYjVfrBv-PLXSAUb7th2gSOX2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7f399e219.mp4?token=n0y5XY5huycwFlZz9behA351PAyWqbWGRiMSGVXFnYccN0Et3fTSdveCO3DdhzlwQTnZ3BUYNczRQKsFMxkuNpJfYAamKirJG8fBSS-HdOGMwsikMt4XZfCzqBC_MghBHPNASNmm7_GjyBXCblJGrjqt1YkPPXgZiQpAyD4P85EuuYWpU0ihoRaibXsHmIsXDZ8xAC6rzh7UPAJUqRyW3mhd6j4T-E0LrLSnwcuYdFXuohWNmdBg1fXGiq_oPSleBfSgsJ5txFe4g9D8nSMLl_mvmER4CfCu2OI77_E6zy4CAe0-xXsMrVJf31KbcYjVfrBv-PLXSAUb7th2gSOX2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⛈
⚡️
ویدیویی که یک هموطن ساکن مازندران از وضعیت چند شب پیش آسمون مازندران منتشر کرده و نوشته؛
تو تاریخ مازندران چنین رعدوبرقی که بی‌وقفه ۳ساعت بزنه نداشتیم
😳
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71360" target="_blank">📅 15:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71359">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkMRUfCZ0NjpH3ZHmpJcesmPf4lzqkGaGmB_kUMuzYBXT8NvmmPccQJl91Rj2JzAca89OoCvWhTcRtfLL6TyIVDrhjGZUZtvBDOiS1HdXc3lKPWBDuBJFIX-fEg7uFGhe4x2s8-OJ9Tn94aXyxgI3txEpwtVJ6I0hTCAO0YMmTPWlkKE34CUEuDGyPr7aM2gK4e9lHx-5S9sOaYqkTrTWR434YwSULc2mMBHGfGnH9kX5qoMLHOKGVGbLJnlcLzrPPMt_P3RCAoktrId7amkiTFKBXBxb5L_xCqQG0Kjjk9tEMS5nAckcdYySoZzsAFunOZVf8UlEaOo5uHUmKjbPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
🇺🇸
#فوری
؛سخنگوی سپاه پاسداران شروط جدیدی را برای پایان دادن به جنگ مطرح کرد؛
🔴
اگر دشمن خواهان پایان این وضعیت است؛
۱_ضمن توقف کامل جنگ، از تهدید مجدد دست بکشد
۲_ارتش رژیم صهیونیستی از لبنان عقب‌نشینی کند
۳_محاصرهٔ یمن پایان یابد
۴_۲۴ میلیارد دلار دارایی مسدودشدهٔ ایران آزاد شود
۵_از هرگونه مداخله در توان هسته‌ای و موشکی کشور دست بردارد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71359" target="_blank">📅 15:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71358">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf337ab4f7.mp4?token=sj7q-8T-H8ImwmqpYqZAlD32Q2ALTSFdrKFHOM8WUJZjzHKEQdXFS8Ok53ySHWn8X4OaC7FSGqtjlhshvgB0lpd5oCRQrUFbqUbOuBVnzD4VD2X4uWahxw-Jj_UazU6mlTsdq-G4F-6sqaJrT-q_3V4M6fWsjH8l61Pj5yXvJo-YyvdLZNvR8EktzMG5sW-M5eFQHzQS2Tj7fR_jTbz7OguNm-omXByAbthpAUGGOwdrVfkNRSU5IMAVtEaV97h61a2vIYtFHC-ItMFKIMVcyPFUkZUA0xWt1TxrKoFQxrIuHIn3L4gfx5JL4-fQwuWdTW8KfdANlmeKh44PZJ2YNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf337ab4f7.mp4?token=sj7q-8T-H8ImwmqpYqZAlD32Q2ALTSFdrKFHOM8WUJZjzHKEQdXFS8Ok53ySHWn8X4OaC7FSGqtjlhshvgB0lpd5oCRQrUFbqUbOuBVnzD4VD2X4uWahxw-Jj_UazU6mlTsdq-G4F-6sqaJrT-q_3V4M6fWsjH8l61Pj5yXvJo-YyvdLZNvR8EktzMG5sW-M5eFQHzQS2Tj7fR_jTbz7OguNm-omXByAbthpAUGGOwdrVfkNRSU5IMAVtEaV97h61a2vIYtFHC-ItMFKIMVcyPFUkZUA0xWt1TxrKoFQxrIuHIn3L4gfx5JL4-fQwuWdTW8KfdANlmeKh44PZJ2YNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
📰
یک فایل صوتی که اختصاصی به ایران اینترنشنال رسیده است، نشان می‌دهد یک هواپیمای نظامی آمریکا در مکالمات رادیویی به نفتکش جمهوری اسلامی هشدار داده به‌دلیل «رعایت نکردن محاصره نظامی» در بنادر و سواحل ایران، موتورخانه آن را هدف می‌گیرد و خدمه باید در ۱۰ دقیقه موتورخانه را ترک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71358" target="_blank">📅 14:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71357">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcr65FOwbCxhzQVRrAcmP_0IOd8HTk5KfWwe7ohcHFZDiBib5ehqzNlhSqZCgc25jgex4iFVuIvgZlLonv_nNSqrSElD38AwCESofdqZE0n_pwTmPZJrWS3so3Y0Gv9e01BpQrdHwrSpv_lhCSEsZCvwjHet9KDHWbMwtt828YyJcMlA7hb3G6KUkUEfVcYng9UmY-YPuP4T6G8IY_B2yQk4tS0IimHESO6iRknIFzmIWtZrBu2xO6bhxIvOsDCuUGmP8xv9oBhTLv2lqHgM5u26MLPhjUPBPHy-DP2EZSD4QcSfJg78wdZ0LIMqL4TVtHEvd9j9nExWsUUlAKyUaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
گزارشی مبنی بر وقوع حادثه‌ای در ۲۸ مایل دریایی جنوب شرقی «الفاو» در عراق دریافت کرد.
فرمانده یک نفتکش گزارش داد که این شناور مورد اصابت پرتابه‌ای با منشأ نامعلوم قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/71357" target="_blank">📅 14:30 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71356">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSdfg8Qu9dSXOwWqX3AVZfo3crxjIvhn8afjoW_l7uHJuBn4daj1c82xef_d7D8YVjew5v5qnAAfMliK4Rqez9LD--slCQKajxMtruSbffem_sIPIdQv8VsDdJNw-uywpR2vStjuoXPZHugmNLEYv60MtwKsUmzNQooi1PenjrPXiNoVZ6pcvonQ71b2cJDiKFDvJaB3EoPaTqxosshXUtbBp1CnQ1LOKeAs1ddB_HjZbDd8BpH4WgBSgxglmMatDkqZuTChs70BU9Bb_X8LLRFPKuBZTCLrYyTDwJwQ0FbhjXqLJMzhxlOSeOMTr2G8pZ7YSQCqtFCz2WDqjv3oeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
💸
🫵
دقایقی پیش دلار و تتر به شکل عجیبی تا 241,000 تومن بالا رفت و دوباره برگشت و الان 234,000 تومن هستش...
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71356" target="_blank">📅 13:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71355">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7Lh59d7Su-5iqq_Feit-_dCQvSkzY7IT02pGP10ww20yzjefM6qb68RP3yHh9B4cISbb7rGNpBJnWU7j2s2c4jkPD_bIMyOeIdbWCtit9xjVOgU8yoTNnMCcbNMYUrQI1fSHXIClPm8WD5MxFW-lT-0ilRfSuy6xW4l_M_DWVkltxeeOwGYiwe5vmmGZelJdGfi-VhDWzp6i9HjFwK1LxWwZCGqYyA1aVEYL_Gywl8Vj3BOi-S2RUcTHRg0uSaF34_xk4b4p2Ae1ylr62izOMtGE-z0AU28_3PYOV9V3gHQoJVMakclsub-S0Bn0nD7UYH4s4nwVE-eqB2xU4s6lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
〰️
فرماندهی مرکزی ایالات متحده:
❌
ادعا: نیروهای سپاه پاسداران انقلاب اسلامی ایران (IRGC) مدعی شده‌اند که به دو ناوشکن نیروی دریایی ایالات متحده در خاورمیانه حمله کرده‌اند. این ادعا کاملاً نادرست است.
✔️
واقعیت: هیچ‌یک از شناورهای جنگی نیروی دریایی ایالات متحده مورد اصابت قرار نگرفته‌اند؛ تمام تلاش‌های سپاه برای انجام حمله با شکست مواجه شده است.
در همین حال، نیروهای آمریکایی تنها در هفته گذشته موفق به انهدام ۱۰ نفتکش ایرانی شده‌اند. این شناورها بخشی از یک شبکه پنهانِ چند میلیارد دلاری بودند که بودجه سپاه را تأمین می‌کند و ایران قادر به محافظت از آن‌ها نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71355" target="_blank">📅 13:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71354">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf3721b8d8.mp4?token=X2SAkz7F-lUPBnmgNFqMc_vXLW-lfoBN-N2JUtmrG-We3zXX77ru80SSZkRK5zyDQt5DsByjxlos0vspRDilgjnvXRn8El_vrzlviQF_zNXm2o83KXElNbvDHsSv54-tMPpmwUsLolpLFBIYmT2ZiGvJ17cidY7b6SDgZURua6wztIbUxqRIdh5R8ZoMEo26FVRAektYcarnyyNaND2Hh4m4EhMkLxVFw1O1hlQw__H36rEBlkVv9VzoFe5N1BdLvRH8XdsLKHcg0mRZvR70CyigeA5zDps1gqijjxhcQO-AL-HnfL894Xl1NBjFxFXw_9D-ioZzLWUGmT4HWND4vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf3721b8d8.mp4?token=X2SAkz7F-lUPBnmgNFqMc_vXLW-lfoBN-N2JUtmrG-We3zXX77ru80SSZkRK5zyDQt5DsByjxlos0vspRDilgjnvXRn8El_vrzlviQF_zNXm2o83KXElNbvDHsSv54-tMPpmwUsLolpLFBIYmT2ZiGvJ17cidY7b6SDgZURua6wztIbUxqRIdh5R8ZoMEo26FVRAektYcarnyyNaND2Hh4m4EhMkLxVFw1O1hlQw__H36rEBlkVv9VzoFe5N1BdLvRH8XdsLKHcg0mRZvR70CyigeA5zDps1gqijjxhcQO-AL-HnfL894Xl1NBjFxFXw_9D-ioZzLWUGmT4HWND4vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
پرسنل نظامی جمهوری اسلامی:
رفتم یه شونه تخم‌مرغ رو گرفتم با یک کیلو میوه شده یه میلیون تومن. حالا نمی‌دونم بیست‌وشش و خورده‌ای هم دریافتیمه.
مثلاً بیست هفت هشت تومن سر ماه به ماه میدن به ما. مردم چکار کنن؟ خب دیگه یارو میاد بیرون حق داره اعتراض کنه دیگه. به جز این که اصلاً راهی نیست. بعد هزاری انگ هم می‌چسبونن که آقا یارو تروریسته، فلانه، بسانه.
مرد حسابی مردم گرسنه‌اند. خودتو زدی به اون راه. من با این لباس دیگه قشنگ با این لباس نیروی انتظامی ناراضیم. وای به حال مردم. یعنی قشنگ میری بیرون خشم و نفرتو تو چهره مردم می‌بینی.
می‌خوان جرت بدن منتها نمیتونن. یعنی همین الان میری بیرون اصن یه جوری‌ان نگاه نفرت‌انگیزشون نسبت به این لباس قشنگ معلومه.
حالا یه عده خودشونو به خواب خیال زدن. بابا دیگه خجالت بکشین. بی‌شرفی یه حدی داره. مثلاً انقدر. شما دیگه رسیدین به اون سقف. یه کم خجالت بکشین. یعنی اصلاً من نیروی ناراضی‌ام. وای به حال مردم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/71354" target="_blank">📅 13:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71353">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jciHwHbu0mjZ1DU61jWT25o0fPAdkqbbXtUJyMcaAzNEGvss-fpWpCGOztBfWhDAoqQQ1e4KpDvEhl2Xrg6tkt8LWvYa8UW-lxjteDs25OZxyphMeD2NldqKHFcwqjtejSHchZ8NcBnOtoMpnQgdoHylvHXicEQa_VTZWY3wVDhlGPEQ8-vRtKeDEEmxk8TWLzLvM8FD8VlaUmZCTncq3FypIiUsXgSfqBAo-LicBxI17DHwMu_EttpKx4nv-X75xFvYVwbIW7mrlmwSNANfNcsk72kztiiNiDDoudnhC-_tWu99HlYfU6mM-pYWdGhP1u06o3PcPvqUxwoy9oIXJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
گزارشی از یک طرف ثالث درباره وقوع حادثه‌ای در فاصله ۲۴ مایل دریایی شمال غربی بندر راشد در امارات متحده عربی دریافت کرده است.
فرمانده یک نفتکش گزارش داده است که شناوری را در وضعیت مایل (کج‌شدگی) در حالت لنگر‌اندازی مشاهده کرده است؛ وضعیتی که احتمالاً نشان‌دهنده ورود آب به داخل شناور در پی اصابت پرتابه‌ای ناشناس است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/71353" target="_blank">📅 13:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71352">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71352" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/71352" target="_blank">📅 13:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71351">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UdRiaQFtXkCJyTqbtUCwZRDWosCk5qlKBXC2puc6prqoIzj8BCW7EKLTfNecLvm9hz9s-e2i8GVZSV46_aLbxyzHp9dYztlMovzOw75_qztQkehUU0TJofWjNA4JK9K1uygDW9CAnCkK_aoG-KYG-OMYc8gBDGsWdf5AWNzpDPYbGZXxCQPD33JITJJqjeuh_QtWHohbq7YvOUoXRyaRNYgNxHDCxCVHP4g48I0TPVddgODAMnfswvv2jtRl0ORty8YtbTkdacBUqotMP3MOZ9ro5eY-J8ypArVtDXIEdz67zy_JBwCahC-vWKD3t188ZT522IVnxvohsxJd2P89MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شبِ بزرگ فوتبال اروپا فرا رسید!
⚽️
اتلتیکو مادرید
🆚
لیورپول
⚽️
🎯
این نبرد حساس
چمپیونزلیگ
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📊
نگاهی به آمار ۲ تیم در تقابل‌های اخیر:
⚽️
اتلتیکو مادرید: ۵ بازی، ۲ برد و ۳ شکست، ۸ گل زده
⚽️
لیورپول:  ۵ بازی، ۳ برد و ۲ شکست، ۱۰ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/71351" target="_blank">📅 13:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71350">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5Ady4c7H3JQbgOZ_Kk_WptbtRepiRj2bOnixZSoyPtdcOJZXDpbzEVNAYA-Y9StHrTGfrGpL2z3ScWrB1Rdh0YRMZ1f7clKtfueSgJeSDgifvPNoAe4s39Muc8YyYkiIt6JDPqJGAdrpHJNOpuKkiAXAHkdRdP5tWb6zPmxEhkp6E5YcSrA5LI5zvhoR3mzcMA4uJxEFVIg96w3q8iPahlgbNqv3lt6r4gyHSP1IO2dC0w9kEi-z2HUUxOrvmA-_mhjgrtPo1izASTo_otX-647PVnDGiC74c52Sraz7YIiPeqpep6uFKhN1AJSzgROK8WavIWHl6BU6mL2F09HwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📈
قیمت نفت خام برنت برای نخستین بار از ماه ژوئیه، به بالای ۱۰۰ دلار در هر بشکه جهش کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/71350" target="_blank">📅 12:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71348">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDVI5wtTCvhd6ooG8hv_rVSLJdwJcqIuAXcetNyaGNl0AoRgwyxnwhYukMiv_iTbgysUauELEGbNc2_W2vYW-qoGMcoRS3AOnk_arKd4kA-dPgTGYxebxzr0xS_5eXk94fds3nTIGSWq8aotXIFq1_MOl6LNw8r49lP83uZKu6K5ADV5fC-AtbKdyXxsCkvIwiCBEX_YKk1XfuIkShVCbVMrkJvEBy1w5dChIqd05AC_gNsc2Br1hcH3rKRANZ4Bzp0epYXKfZy29qUuIF3Y1YWN6E-Ue3vZv31BiziSRbxVrGdFxYhzPv4UFTZ3pqOAVOnKIg0P3AcylIouFCSOFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c11c683d6.mp4?token=BqakshGfk6PwR24r41352a5UeMj_2Fe3udGo_Tc1UlNluer4G8BHWQqY9HgiYOh50WwDZHHPyDy1bK6sGNct5zdOgK5b6KDhh9aJM8Ln942jZaIYAS8JPv_rkpeA6m9XtULfRX59USMzO_ywXol8BxVEDzZx5dWkm_0ol99AS9gvsDZLf_VAIqKLVJn9rOu63rHXe5NtJv3fUyrrrG8YAxPQdcab1BEgMVVGHhiRpW06GdDXwdjLbiyu5loZ8h0vLtYPiszmA9J_vKBjWDsXLLOfYfITSQmE4YnPFSQ08NfWsanEEGGs2PZiChx_wyEwRP5djdb2iFzvhKYvBa2CrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c11c683d6.mp4?token=BqakshGfk6PwR24r41352a5UeMj_2Fe3udGo_Tc1UlNluer4G8BHWQqY9HgiYOh50WwDZHHPyDy1bK6sGNct5zdOgK5b6KDhh9aJM8Ln942jZaIYAS8JPv_rkpeA6m9XtULfRX59USMzO_ywXol8BxVEDzZx5dWkm_0ol99AS9gvsDZLf_VAIqKLVJn9rOu63rHXe5NtJv3fUyrrrG8YAxPQdcab1BEgMVVGHhiRpW06GdDXwdjLbiyu5loZ8h0vLtYPiszmA9J_vKBjWDsXLLOfYfITSQmE4YnPFSQ08NfWsanEEGGs2PZiChx_wyEwRP5djdb2iFzvhKYvBa2CrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این دختر یکی از پشم ریزون ترین خودکشی هارو داشته:
دو روز پیش "پایال دِوی" داشت اولین فتوشاتشو برای یک مجله تو حرفه‌ی مدلینگش انجام میداد که یهو وسط عکس برداری تصمیم میگیره بی دلیل خودش رو تو رودخونه پرت کنه.
ویدیوش خیلی عجیبه و بعضیا میگن امکان نداره این خودکشی بوده باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71348" target="_blank">📅 12:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71347">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/032667483d.mp4?token=IPTzEU06gmJUfT1zBCbwFIpdSIGmE_-lx7lZ7TPXev0VrzKox-EfeLYkyrJx5IqMKRQYjtneEFFk9-8O6yoet9elIBTwdkG9vPx_DWFYNiTyhFJWWEeGRD8n_Y1lcnoleTgKLPPZcGjguP2aErgecleoKqiaNSvG7jvXGJVZSF2mluKUu7-uwzlgXqo5A3KZvbwbdQLHkAeJZoYPk1-4mGjv_R5ZUKByPwMGtGpXpREX10KWV5mnPzdB0yV9f_CgD4O9uCM6tP6YIdwdNLOW_pCEb1UmgSghoKMFcUZPII5s7_k5BtPIDpLtby4vIOej4w2g_N4pGLuwfpK8w5b8xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/032667483d.mp4?token=IPTzEU06gmJUfT1zBCbwFIpdSIGmE_-lx7lZ7TPXev0VrzKox-EfeLYkyrJx5IqMKRQYjtneEFFk9-8O6yoet9elIBTwdkG9vPx_DWFYNiTyhFJWWEeGRD8n_Y1lcnoleTgKLPPZcGjguP2aErgecleoKqiaNSvG7jvXGJVZSF2mluKUu7-uwzlgXqo5A3KZvbwbdQLHkAeJZoYPk1-4mGjv_R5ZUKByPwMGtGpXpREX10KWV5mnPzdB0yV9f_CgD4O9uCM6tP6YIdwdNLOW_pCEb1UmgSghoKMFcUZPII5s7_k5BtPIDpLtby4vIOej4w2g_N4pGLuwfpK8w5b8xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گویا طبق فتوای جدید حضور نداشتن تو اجتماعات شبانه، غضب الهی رو در پی خواهد داشت و تو زندگیتون ذلت و خواری میاره
😂
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71347" target="_blank">📅 11:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71346">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhMxEOb8mzaKNll-38wZIi0jlOYJLgKPo1eB8V1tN_I5XIxhagzoV6rD5sOafqewupset-ieVH2di9B2Cl-bq-OgpVXgRMMLOcG7Q7KF5uVnweMLdZb1toMPmkLYo3Au2K46skuZBjuC99I3vNn9QiH4e3u4fyJU0gOByppRbS3CppQlY2cbJa3f_KlEx9m2M4CUHyOoKfcNiNMXyJpgS3rL_4hYKlyM2gJLOZuFloMSauLKodSnTjrW4eDq3IDXOJBNxtdL0ipSmdNOI_ZOXNzeM3Q6sNVSZ_0jj7WProxN_qOOT25EfstPiWfNXYmsu-zFsOdztpS63kPbmnYHvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
♨️
دوازده کشور با صدور بیانیه‌ای مشترک، ممنوعیت‌های ملی تجارت کالا از شهرک‌های غیرقانونی اسرائیل را اعلام کردند؛
🇫🇷
فرانسه
🇬🇧
بریتانیا
🇨🇦
کانادا
🇩🇰
دانمارک
🇪🇸
اسپانیا
🇫🇮
فنلاند
🇮🇪
ایرلند
🇮🇸
ایسلند
🇳🇴
نروژ
🇵🇱
لهستان
🇵🇹
پرتغال
🇸🇪
سوئد
مکرون، نخست وزیر بریتانیا برنهام، و نخست وزیر کانادا، کارنی، توافق کردند که وضعیت با خشونت «بی‌سابقه» شهرک‌نشینان و گسترش شهرک‌سازی رو به وخامت است و به طور خاص پروژه E1 را «غیرقابل قبول» خواندند.
آنها از اقداماتی که قبلاً توسط ایرلند، اسپانیا، هلند، نروژ و بلژیک انجام شده است، تقدیر می‌کنند.
این بیانیه از اسرائیل می‌خواهد که فوراً گسترش شهرک‌سازی را متوقف کند، شهرک‌نشینان خشونت‌طلب را پاسخگو قرار دهد و اتهامات علیه نیروهای اسرائیلی را بررسی کند.
آنها «قاطعانه با هرگونه اقدامی که منجر به الحاق سرزمین‌های فلسطینی یا آوارگی اجباری شود، مخالفند.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71346" target="_blank">📅 11:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71345">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcf294068.mp4?token=Q5ioMJBhHuLuxjcO9zYqRjhkE4Hc05Anajp7AvLdVvZgKrxu3ulHhFX5GB0A_MuaZrHGaVeIYYcOfEYtyAPsBBKt9rqDA66w2fjUXexOmLoB37NBb1qgSg-A4672Bmxfd36S8Laua83H1MvPTSfMt9pSdzje-wJIqbgiIzGLN1zzOU82OYyCIzJgtUErF3eOcCp54j93fHXkdMJvi1RLjmKrhQaaslo1O8xRw_vkmvThnAXDDAmKg2A9bJ-Jjdm73cIDQUfPry5pEsshgKTzXewwMWyJVCJyZrmaxjhedR8HkNROHddiab45wEiZqjJC7ks_cTS5_r2AlDHv7_Ti9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcf294068.mp4?token=Q5ioMJBhHuLuxjcO9zYqRjhkE4Hc05Anajp7AvLdVvZgKrxu3ulHhFX5GB0A_MuaZrHGaVeIYYcOfEYtyAPsBBKt9rqDA66w2fjUXexOmLoB37NBb1qgSg-A4672Bmxfd36S8Laua83H1MvPTSfMt9pSdzje-wJIqbgiIzGLN1zzOU82OYyCIzJgtUErF3eOcCp54j93fHXkdMJvi1RLjmKrhQaaslo1O8xRw_vkmvThnAXDDAmKg2A9bJ-Jjdm73cIDQUfPry5pEsshgKTzXewwMWyJVCJyZrmaxjhedR8HkNROHddiab45wEiZqjJC7ks_cTS5_r2AlDHv7_Ti9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
〰️
سنتکام:
کشتی «ریسکو» (M/T Riesco) در تاریخ ۸ سپتامبر در خلیج عمان غرق شد؛ این کشتی پس از تلاش سپاه پاسداران برای حمله به یک ناو جنگی نیروی دریایی ایالات متحده، توسط نیروهای سنتکام (CENTCOM) منهدم شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71345" target="_blank">📅 10:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71344">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/128e77e5cf.mp4?token=uL3pH__qTtoZ9d4qQtpNn_rS123iul2jo0qIp40GezjVvJJtcQxtwnPG5AJAhJCGLfW4xWDbbPruhedlLyd-en_b6GGGbXGvWyzbNM6BHxS07pkGS191fb-lOLSyJMf8f01QOIAL6GYLn0tz-03BJEOADm0PswMAoQj-HN2Ts4ED1Ha5R_FE2h8Y02Yk-QBrj9iGV0Yi5aRXVtkCNmUCctkF0WXg-c2pxwBuuucgFSkW5WkbZrUyEmiRYguWMMtduccuEu6fT6goTJTSEiPuMma3H0BJSYwSKkMCEBCaCtRx3xiMb38M7AAZLBNsGAFS2idBST1_d46eh-lM_qtXmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/128e77e5cf.mp4?token=uL3pH__qTtoZ9d4qQtpNn_rS123iul2jo0qIp40GezjVvJJtcQxtwnPG5AJAhJCGLfW4xWDbbPruhedlLyd-en_b6GGGbXGvWyzbNM6BHxS07pkGS191fb-lOLSyJMf8f01QOIAL6GYLn0tz-03BJEOADm0PswMAoQj-HN2Ts4ED1Ha5R_FE2h8Y02Yk-QBrj9iGV0Yi5aRXVtkCNmUCctkF0WXg-c2pxwBuuucgFSkW5WkbZrUyEmiRYguWMMtduccuEu6fT6goTJTSEiPuMma3H0BJSYwSKkMCEBCaCtRx3xiMb38M7AAZLBNsGAFS2idBST1_d46eh-lM_qtXmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🇮🇷
مهران رجبی:
اونی که نمیاد تجمعات باید بهش بگی فازت چیه که نمیای ؟
این وظیفه ملی و دینی ماست و باید بیایم کف خیابون
ضرر نداره بیایم و شما کاری میکنید که کفار ناراحت میشه پس بیاید
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71344" target="_blank">📅 10:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71343">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a8a7be1a9.mp4?token=roo7IUFXboKFZ-szS7a3y-Vz0e4NyO7Z4C2ilyfbXrxt_caypGKxFfdtCkI7j-oiBT-75h6MEYyhjdLayPLYN4riuqrC1cVmdnaELEga25TUpxAKThZpCb9Wg6ji-mC-gQ0ojAqdtp7JOI9uAB-YiNbQavOaiUrZ_4DNMbwAsf53dZbF-4Bw0V2vZy6_-pXSqU-k9UT3vynlOycK7s8yVX9iAIwm1Cnr23f5733xSz6tXtLZJUskP2NaR2PoK9cQTe6XzQeSB07FJ0H6X83w8U61bgyHWOMupz8O0nE2TGDV4rFmLLb6fijObJzOc2TS-hi5Bqzpbu8p-I56TAjdJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a8a7be1a9.mp4?token=roo7IUFXboKFZ-szS7a3y-Vz0e4NyO7Z4C2ilyfbXrxt_caypGKxFfdtCkI7j-oiBT-75h6MEYyhjdLayPLYN4riuqrC1cVmdnaELEga25TUpxAKThZpCb9Wg6ji-mC-gQ0ojAqdtp7JOI9uAB-YiNbQavOaiUrZ_4DNMbwAsf53dZbF-4Bw0V2vZy6_-pXSqU-k9UT3vynlOycK7s8yVX9iAIwm1Cnr23f5733xSz6tXtLZJUskP2NaR2PoK9cQTe6XzQeSB07FJ0H6X83w8U61bgyHWOMupz8O0nE2TGDV4rFmLLb6fijObJzOc2TS-hi5Bqzpbu8p-I56TAjdJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از طویله مجلس
😳
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71343" target="_blank">📅 09:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71338">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gv1YBgJMLhclOyuDsz55CcaK8wf1-eYffpnFeT2zMmaKyNd3hKzTO45qQGe6TgAxJi9H8gNsN2_7NHtSQNxSIZRmMYwAZ0wRqwx8DQql0_9GwSUyUVgwUENAYNyhP0O9KgoX8RASqecnWpIwf_sL1IoIb8rbZftpmmez2TVc_RFaEcXjhsjKy2bsSVe3ZfJLNcAZjsvut--KWBhbyL2tcsn2OBn4pwJ3Np0oLxxF6yBmgdGbfTCzGcLZ4veAdi3dMf1c9eKLRmDbtn1FvCRWM9bZFMoGEK9_ZwgIJn_VsGAe4QGZ2hF4jd9gn-ukLPb-XG4jhtLpv2AGbGZAl_WSsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TKTf5QWMu-PbG2i6Ja2Yf8wQfTq9SxKR7dt8kstYASx6c-SNTJkChqM7kvCIUppAlKUDBaktTwS9glybdLSuDtfjC-TC43-7-sAjBKfgi4cM2_eWcqy6RYTmy96f3LgCW9hv2Txn3X-bEQfYlEON3cFjb6mJfJrQy_RwJD4letQgKizEhma_yY8DMHkKaRoTRE971u79sfTHbhR-myY6M0J3-a9H6kz-Jhj7__4DLTznLvXEiZXAzxh8GmRV-NLNymKGw_JnurtbWhxNJrfboH__p9Bx7aNEd8E9Ek2TuEIhVyEOOeEDe97hpKa6vHldhXQhj77mmCHo2RKhS6F6zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BoJvK-dMyxGQOVVL8pkzFHPaRqMkoqw2-5pOYDTifQBqv-lhHUTxM5DT8-qgoLGN0qYj4CrPTM4Wp1eIbLAHk_veSbfrh3wKD20TjitH0g_FGcvDMwZwj_I-1eYFUQGqOXDD8ydGjwyTV-pZm0iGG5K08AaClXSHxCf-Uo5V1oa226lnaW2KRQv9LK1VBkyMHYBfTe6n1lqSqvBLg3MgLT4WmwEhtK4elyrvCtfRAzyhEEslrd1SIVjQ6yBWO3WCrGqidsOeHfBUlwuX2Ceh2rAVse1fq2rGMv_VfzO9PNV0I0OjCzBaQjjRZmNyxVej2FvdfrOsgW6bIWeDazpoDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TDZWP9RgZXtrTdaM42Ow3gq88boM330LbCFZO-THvTXe4japXQDeHZCQ1IragfziNFkbjS1Tdt4eV2MhJcKXVfctDqu1dWRGCin2eqXxgs0ltEIdHE8tN-okLlolfu_D0qJAVV2URrokV2uUGPBHoNr6WDVZUPVsN7Nn4h5D1W0pGks2cfmc7vWcDxO41f-hj1txzYdlYIF-DgcWLrSKYxnodBOskzbYxquiLf8hSxnvufPPzly_ElcWm0Vy6vZqA_bwrUN8WTGCFBs3VXMP8L2GKJx4jQGhemFrH_c0FI5SM2Uugh3WxxnTCCmOs7e8HHQwDVAGs3YjxGGZjw5y-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CzvCsm2kq9jBWh3Mh0TGPrnPmrrISRYpszN2I3pl1-yUdgI6Hegjr23zX2Cqvfm6guGQaBuYqdoTlS9G3GUYNNKOxzcLjIdtL6AVj8O1ndDVr8DU5fSgH2kHuqsvRIXzOTexLcTnc8UqjbLrBeTOc7XMQhQDMzy9Mv_zYYWhGFg1B6MW7V0eeYF1vHuvUjVzKmlEP6bofVahXteUX4aZxGr0O2ARvVSqB8gq8gFh4gEAiSYjf-YpBqhpouLMFNx9XE6vOaEzK8ROxOdDY_VngmrxdywwNkHNW1GRtSiVnYmoKY9K23s6FOaVjImx6_KGyyTTkMr3q6I4jPcAYgEelg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
🇮🇷
🇺🇸
سپاه پاسداران تصاویری از زیردریایی‌ بدون سرنشین آمریکایی که به عنوان غنیمت گرفته منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71338" target="_blank">📅 09:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71337">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در TrexBet، بین ۲ تا ۴ عکس چالشی منتشر می‌کنیم که داخل هرکدوم یک Promo Code یک‌دلاری مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار ۱ دلاری.  18:30 → اولین شکار  20:00 → شکار دوم
🦖
• شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71337" target="_blank">📅 01:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71336">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdyWZSZQh_x4yr30siG58ryRi2vv-GqnbB-JcFf9eeWKh2tRVDB4VsaMH7-y6riFmJf75WfWkrUbEQEQiR2xk9_GVlGHmTD8LxNtUarIw1mqIZoJPRj42h4RpGr1n3T1sFpngC7vHShEWw-cuOwpQlv6pSsWfezFUMNNYui1IzVN47WhwF_TA2Vt1vc9usBUWhdl57rOWoeeOAGvkG-LJEMtGJKaxLg9fr_mEBsOhyWdrW8rYWPTrWsFSuQqIDo2fEZwtyCw1KAsK7pWU0dQM6Otv8S_c6FAA8Rq3X2RItWmvy04g2pAUp43Oflf2DJCEp7sA4W8bLNcWyomYxoTPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در
TrexBet
، بین
۲ تا ۴ عکس چالشی
منتشر می‌کنیم که داخل هرکدوم یک
Promo Code یک‌دلاری
مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار ۱ دلاری.
18:30 → اولین شکار
20:00 → شکار دوم
🦖
•
شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت نره...
ممکنه کدی که دنبالش هستی، فقط چند ثانیه با تو فاصله داشته باشه.
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71336" target="_blank">📅 01:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71335">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
〰️
#فوری
؛سنتکام:
نیروهای سنتکام در تاریخ ۸ سپتامبر پنج شناور حمل نفت خام ایران را منهدم کردند؛ این اقدام پس از آن صورت گرفت که سپاه پاسداران انقلاب اسلامی طی دو روز گذشته، دو بار یک کشتی جنگی نیروی دریایی ایالات متحده را با موشک‌های بالستیک هدف قرار داد.
کشتی جنگی آمریکا با موفقیت از حملات تلاش‌شدۀ ایران گریخت و به گشت‌زنی در آب‌های منطقه ادامه داد.
هیچ‌یک از پرسنل آمریکایی آسیب ندیدند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71335" target="_blank">📅 01:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71332">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
📰
خبرنگار العربیه:
چندین موشک ایرانی در جنوب سوریه رهگیری و منهدم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71332" target="_blank">📅 01:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71331">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/665d19bf87.mp4?token=dIuajY6Nlb96G4EODBlWmKtragLQ6qusfALC2K15V4ScqgLQ_lTPub_bMdLIDJ3plGQx_a4trm1w2xGUwvt1pH6CpOubA-du30_6vt5C6-VFOoY9mqt5cV3f3VDw8OK9h90TVNcuDPHoHvkpgGK-q0Sxm2S1sRzEccUoGlpiN70ZVaYUPn87hUiYv2ltXWP7_1S-craPYjOJ3osBt_MuCMJX0dhlQVcNaHiFAseMnqFhu7snI4j9lM4clrGkdUhQNQEVejboRPTuWGuEQzMKSts49Nw8FbT9XV3bux-d_EJbnEXF9BdoH44znGlXtcNBpf2xvCBQa7A-M81f7xtMGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/665d19bf87.mp4?token=dIuajY6Nlb96G4EODBlWmKtragLQ6qusfALC2K15V4ScqgLQ_lTPub_bMdLIDJ3plGQx_a4trm1w2xGUwvt1pH6CpOubA-du30_6vt5C6-VFOoY9mqt5cV3f3VDw8OK9h90TVNcuDPHoHvkpgGK-q0Sxm2S1sRzEccUoGlpiN70ZVaYUPn87hUiYv2ltXWP7_1S-craPYjOJ3osBt_MuCMJX0dhlQVcNaHiFAseMnqFhu7snI4j9lM4clrGkdUhQNQEVejboRPTuWGuEQzMKSts49Nw8FbT9XV3bux-d_EJbnEXF9BdoH44znGlXtcNBpf2xvCBQa7A-M81f7xtMGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آسمون اردن
😳
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71331" target="_blank">📅 01:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71330">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf482be15e.mp4?token=rt2KFLTHWEGNb_aBOgCm6swzoieX_6nEOUsSq_tIx_PiKidMeQmhPUS47C8l6xdkLhhVLaKL9wxKuxBR12z7QZRAr3QAl2qKqZagLRsc7BFCT4ozz_s58FSw6x9Ls1aZTJUDQjMhBAijOE-e3GyngyiEGbOCRZDTOxhJgq-Z9qnxM8t5kTG2htugIsH2gdFMJYyKOUKJJkAd0HApaMKfoyIPj6YLr8_tKWTbOGKsnCrAHLPj0roOC_qNtmuOC1U2672cZNj4S1q_0uQh8d8Ny3_79m78RIS8aQ7WG9ti-dhisCjBrpMPmTPGMgJS-LZuH-brQybc2v-w06Ps9qgcIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf482be15e.mp4?token=rt2KFLTHWEGNb_aBOgCm6swzoieX_6nEOUsSq_tIx_PiKidMeQmhPUS47C8l6xdkLhhVLaKL9wxKuxBR12z7QZRAr3QAl2qKqZagLRsc7BFCT4ozz_s58FSw6x9Ls1aZTJUDQjMhBAijOE-e3GyngyiEGbOCRZDTOxhJgq-Z9qnxM8t5kTG2htugIsH2gdFMJYyKOUKJJkAd0HApaMKfoyIPj6YLr8_tKWTbOGKsnCrAHLPj0roOC_qNtmuOC1U2672cZNj4S1q_0uQh8d8Ny3_79m78RIS8aQ7WG9ti-dhisCjBrpMPmTPGMgJS-LZuH-brQybc2v-w06Ps9qgcIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
مهمات خوشه ای سپاه در آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71330" target="_blank">📅 01:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71329">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🇮🇷
نایا به نقل ازمنبع ایرانی:
سپاه پاسداران انقلاب اسلامی، دقایقی پیش، موشک‌های خیبرشکن را مورد استفاده قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71329" target="_blank">📅 01:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71328">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee276f397f.mp4?token=XCYNvrLecJXdLuKmWYY0gjbW8mdIpcF0itpPTSbAl3BIQ1bSsYmhOO5rSQS96PDPNvyYkqAKNDE_R915o_Vv4YfqIV4GTZqwjyzD0TdConQPBdfO54_wdz16eValls1nWJkin-dN8kZjbLQWiAQ-WMtXShUJNqXXxM-0ljD8iHjOhn63q1zsc2LkEawRRjkUhcGvoY2t5GzvMt9t2vYhEzXrKDMDZhfRS4SsjELSlywfnM2iIzV-BKnfKHh3nJnJfWVNoXjYsI0fYVtkPrBsjK7mokww752FUYnS_kZZ_jsq1F6gHW8Idhyf1teJev1fu5249YotY8ev5WHviUOsfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee276f397f.mp4?token=XCYNvrLecJXdLuKmWYY0gjbW8mdIpcF0itpPTSbAl3BIQ1bSsYmhOO5rSQS96PDPNvyYkqAKNDE_R915o_Vv4YfqIV4GTZqwjyzD0TdConQPBdfO54_wdz16eValls1nWJkin-dN8kZjbLQWiAQ-WMtXShUJNqXXxM-0ljD8iHjOhn63q1zsc2LkEawRRjkUhcGvoY2t5GzvMt9t2vYhEzXrKDMDZhfRS4SsjELSlywfnM2iIzV-BKnfKHh3nJnJfWVNoXjYsI0fYVtkPrBsjK7mokww752FUYnS_kZZ_jsq1F6gHW8Idhyf1teJev1fu5249YotY8ev5WHviUOsfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
گویا سپاه توی حملات امشبش از موشک خوشه ای استفاده کرده
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71328" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71327">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f211389571.mp4?token=t9GlZnL2YXPNumWhjrjQbr_Iqrx2hkcO1xY6qQA_9UrhNRquQCjH6_msUtzB5oeGUj_bxSdHW8NkSCpXKTFmBTgTfXYiWvdf2xob0Px6XPPkCthvTVBUQmyjLOdWhdpiXs4XV58da_mYJPWPxZeDT4SDO9Aebhol0vRtXh_puvJLFPyv-sO7fJqmrlhOXv9INYHTNCHakkhhM6CP5QZKXxE4Co_3j_xg5SGg93JjILCu5Zfi_qv666heoCFNhEs_rbxOYxIwRqLsc057loLQRISUTDofCtOTRbxAX07-3r11z4tuJcqFrdxMkM1IHrGJMK8e1eLacVp2W_na601g6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f211389571.mp4?token=t9GlZnL2YXPNumWhjrjQbr_Iqrx2hkcO1xY6qQA_9UrhNRquQCjH6_msUtzB5oeGUj_bxSdHW8NkSCpXKTFmBTgTfXYiWvdf2xob0Px6XPPkCthvTVBUQmyjLOdWhdpiXs4XV58da_mYJPWPxZeDT4SDO9Aebhol0vRtXh_puvJLFPyv-sO7fJqmrlhOXv9INYHTNCHakkhhM6CP5QZKXxE4Co_3j_xg5SGg93JjILCu5Zfi_qv666heoCFNhEs_rbxOYxIwRqLsc057loLQRISUTDofCtOTRbxAX07-3r11z4tuJcqFrdxMkM1IHrGJMK8e1eLacVp2W_na601g6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعالیت شدید پدافند در آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71327" target="_blank">📅 01:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71326">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
از اکثر نقاط کشور به سمت پایگاه های آمریکا موشک شلیک کردن
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71326" target="_blank">📅 01:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71325">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d314b4d1bf.mp4?token=Zw0DScmJQBe-DBIMECrxtKFYT-FbfMldtCoEUWITDQ_ngJcBodoT60VQs5iKPmim9v7qFkXKkOdEnarZYPzp-yQKY5L9UxBRA6tqveMhJ3Dpr0jMcVG5BGomCjDcRvCPeVlFUyAwZkZTEXKp7Skv7Y79KVZqY3cynly3_vIIpr5GfROKE6UXpKlkUTVTNP3mt92YyFnStL0VpfEXtKVgVKRvXPgpfZpMaXfbDW33IQvQWaYWbDDeuQ7QQed2OhDFzKKJ9vBpE42pSD4RiDUK26ord2k1EcgXSy-n3-RSgdOsRbOPek8ivTAErndifywIQKBu1C0Aov93AFzMTpeTuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d314b4d1bf.mp4?token=Zw0DScmJQBe-DBIMECrxtKFYT-FbfMldtCoEUWITDQ_ngJcBodoT60VQs5iKPmim9v7qFkXKkOdEnarZYPzp-yQKY5L9UxBRA6tqveMhJ3Dpr0jMcVG5BGomCjDcRvCPeVlFUyAwZkZTEXKp7Skv7Y79KVZqY3cynly3_vIIpr5GfROKE6UXpKlkUTVTNP3mt92YyFnStL0VpfEXtKVgVKRvXPgpfZpMaXfbDW33IQvQWaYWbDDeuQ7QQed2OhDFzKKJ9vBpE42pSD4RiDUK26ord2k1EcgXSy-n3-RSgdOsRbOPek8ivTAErndifywIQKBu1C0Aov93AFzMTpeTuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
موشک ها در آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71325" target="_blank">📅 01:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71324">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
ارسالی از اصفهان:
از نجف آباد دوتا موشک از اصفهان ۴ تا
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71324" target="_blank">📅 01:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71323">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6edcd17216.mp4?token=u_Adm060uHnyJFGJ3h4Ve09VmP70V1jH6nK-N05nlvj40F251n3-X2AJwG66J0017hSYx_B6_5LRvIgOr3DHJ4ytNjmbKw5n8McpUG5VNqsEKwbhsYrRI7j6UkfFylTdPshbT-4VwMqdIR2EGPyQjBaSAUJMMupCRwCKk8UKqk7takF0hwyLICg0nZT2-e_cs9yoj164F_iEWQpG3_2Fl6A6u5z-hMD8JcrphEaLEaa7Dmzg8QOKaMdhRdwYEkVpt9B72Zw1XnMv-nzMvTSDeBop-L-dsS9BF51Tflje-qIpbcltC9PnsaKzR3NHx61S9ZDpmD2kMmoooC43B-8CcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6edcd17216.mp4?token=u_Adm060uHnyJFGJ3h4Ve09VmP70V1jH6nK-N05nlvj40F251n3-X2AJwG66J0017hSYx_B6_5LRvIgOr3DHJ4ytNjmbKw5n8McpUG5VNqsEKwbhsYrRI7j6UkfFylTdPshbT-4VwMqdIR2EGPyQjBaSAUJMMupCRwCKk8UKqk7takF0hwyLICg0nZT2-e_cs9yoj164F_iEWQpG3_2Fl6A6u5z-hMD8JcrphEaLEaa7Dmzg8QOKaMdhRdwYEkVpt9B72Zw1XnMv-nzMvTSDeBop-L-dsS9BF51Tflje-qIpbcltC9PnsaKzR3NHx61S9ZDpmD2kMmoooC43B-8CcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن پدافند اردن
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71323" target="_blank">📅 01:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71322">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
گزارش ارسالی:
از زنجانم موشک زدن همین ۱۰ دقیقه پیش
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71322" target="_blank">📅 01:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71321">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OY5kxih4S3qT0p0e5LlbugYDe0hg-AL_2rmVWKz1O0J-I6GCe6R_dTW1uGPBbFwFoKZGb3A2v4a46j6Dbts3rZOue56BSAreKGoPjMkBbggrykWqC7BRVYAMflPy68YgoVJGgojjSvY0GVrYxhcVg3F0MNpqwry72gPqjLSUeecP-LZlo6DFqB5NK5hMXGoWl4fmdLI0ZeK-nnrVT5-g9BZgPKXvxO1BPkJW_1iPfjIJctz4xmIsdqsx4FUe8ZNgpUh3HNj0nMHdgvGE9ctF-bBsoRbX9r9CGdQpXHAzdQflHlfE42XchI0S00QfGatz67bIYxCl4TdIpBV42ak1MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ارسالی از نجف‌آباد
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71321" target="_blank">📅 01:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71320">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc98612785.mp4?token=StdcjbiaNCj8DGEmwvEPlemDcDfOVOrGbQ-R9sftCPFbqJ9poDMMFuXHLU_8RkhyWr5gmBOADSOqt5cwCGAiNq9o-5YLdYWNxaMtOnaD_WLhKHf35V8jE3rkOlCULxWcF-RjrbORgbTpP3N_z9HOJrtb4YDENx7BFyhpwMOqNP7EaaXbhRVFK_77COhonTScR7Dot3TDDF76O8f6ySBT1eUuznAnmo3A5pWX_Km6zxVYSkgFctVyjln41kOy_24aXSQxtonKjEyXh7Zc48VH-SmhWovQkXcNCgcD3I698GAm2hGDO910DUf6lvHxoB0Vcn7KZcbkrzgH8XFE6ym5bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc98612785.mp4?token=StdcjbiaNCj8DGEmwvEPlemDcDfOVOrGbQ-R9sftCPFbqJ9poDMMFuXHLU_8RkhyWr5gmBOADSOqt5cwCGAiNq9o-5YLdYWNxaMtOnaD_WLhKHf35V8jE3rkOlCULxWcF-RjrbORgbTpP3N_z9HOJrtb4YDENx7BFyhpwMOqNP7EaaXbhRVFK_77COhonTScR7Dot3TDDF76O8f6ySBT1eUuznAnmo3A5pWX_Km6zxVYSkgFctVyjln41kOy_24aXSQxtonKjEyXh7Zc48VH-SmhWovQkXcNCgcD3I698GAm2hGDO910DUf6lvHxoB0Vcn7KZcbkrzgH8XFE6ym5bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ارسالی از اصفهان:
حداقل چهار/پنج موشک دیده میشه توی آسمون
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71320" target="_blank">📅 01:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71319">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c50434db49.mp4?token=lMeB4-GxvD3DqV0BpkcelYbxX7pBY1-rT3om9pkyto17AgqYTSg0HEQg2-OSAhjVSvp24xnuKbS1WaMuHQq8jZ2nnpNBPB7yofXe2EDgEktWnqrmwACgP_Yak4K6oo0u0wXz4WPWB7fRHX4wo7Foi2vJHoLucJISQGMJB4qEDVId16A1AlJ4qowXjZjKcuqzLfyNG6n6ePdkjKj4zKgzGnfn2gln99ZIi0TI3jddSfvtJbRg9_CW5I8uzUiGQ-RzA9cVFYNl_kamrSf7Xx0wJ-j-f9kFdqV59uYrBQ_Xe47kdUhA08A-lyiWi6cNxy74LrTvA7rJR-UQ-QqPxgeF_g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c50434db49.mp4?token=lMeB4-GxvD3DqV0BpkcelYbxX7pBY1-rT3om9pkyto17AgqYTSg0HEQg2-OSAhjVSvp24xnuKbS1WaMuHQq8jZ2nnpNBPB7yofXe2EDgEktWnqrmwACgP_Yak4K6oo0u0wXz4WPWB7fRHX4wo7Foi2vJHoLucJISQGMJB4qEDVId16A1AlJ4qowXjZjKcuqzLfyNG6n6ePdkjKj4zKgzGnfn2gln99ZIi0TI3jddSfvtJbRg9_CW5I8uzUiGQ-RzA9cVFYNl_kamrSf7Xx0wJ-j-f9kFdqV59uYrBQ_Xe47kdUhA08A-lyiWi6cNxy74LrTvA7rJR-UQ-QqPxgeF_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو ارسالی:
همین الان از دماوند موشک زدن
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71319" target="_blank">📅 00:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71318">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
ارسالی از تبریز:
همین الان از تبریز موشک زدن
سایت موشکی امند
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71318" target="_blank">📅 00:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71317">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
چندین گزارش از خرم‌آباد اومد که صدای انفجار شنیدن./احتمالا پرتاب موشک
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71317" target="_blank">📅 00:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71316">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
ارسالی از بروجرد:
سلام بروجرد هم فرستاد
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71316" target="_blank">📅 00:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71315">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
گزارش ارسالی از اصفهان:
هفت تیر مبارکه اصفهان موشک بلند شد
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71315" target="_blank">📅 00:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71314">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKULpBhwmf-XgQtlyixZMwNLtrROEqprAAuVRuQx0eZD5i7PP4ge1u1odk79HOpNI77b1bH1zNRKtkfITM46snz4MLwTCr3DI1qOXN25kX_f_20NMjxtCCY89j-D5Qwjg6v0-gyqsuk3u5RUs6SqnUNTsUuL2Hns7_MblxYDetyg03ScFuxF8IccbdbMFP94p5byVvgUMK3pQMVgv3tK7xAnUGLiHnM_vMdeXFVE6-YdavNofPLpMTgUJUH-RTivHCVpktLu_EPx6jKeXiIjXCI9p4upilaIcGNsUHM2kWGbPzMi8Qf86Ih_Cw6n1QFkhe-y-D0PoKV4YwOux7NDUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تصویر منتسب به اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71314" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71313">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
گزارش ارسالی از یزد:
از یزدم موشک زدن همین الان
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71313" target="_blank">📅 00:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71312">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
گزارش از اصفهان:
اصفهان الان زدن موشک نمیدونم شهر رضا بود یا نجف اباد
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71312" target="_blank">📅 00:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71311">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
گزارش ممبرا:
۱۵ خرداد اصفهان شلیک ۲ تا موشک همین الان
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71311" target="_blank">📅 00:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71310">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛صداوسیما:
دقایقی قبل نیروهای آمریکایی به یک فروند شناور تجاری در آب‌های ساحلی شهرستان جاسک حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71310" target="_blank">📅 00:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71309">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBR8JOh8vTasNaSo3kYTEOILlokGdfgvqtuxx4n5gqGtX1GJBhGaaJifSRhN9S457c9UMc0_Y5J6mvX6sPWyI6iUUAuP3Gei2QgbvgYdTUHK3Bl_xoWPZgzir0H29o12X5TOFlcW5OPfkvuPWRl7orzkInCjLt0LU7H85_qNEY5vMO7qn1ZgwQ-m2QxHGX5bV8GVXuvXsJqesv7O3pyHx8yLw4BSkEVNudhTeZt_M-nMBRdf4xiCnuM6PFH0WVnQEClwo3tk6h315kH-XgaQzCArcTwStGf42OV_dZzCpkCs9TQgLw-7D_s4i9uddnCA8t-zl0LGhMpG88kthaprCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
📰
وال استریت ژورنال:ایران ظرف سه روز، دومین موج حملات موشکی را علیه کشتی‌های نیروی دریایی آمریکا انجام داد، اما هیچ‌یک از شناورهای آمریکایی هدف قرار نگرفتند.
این حملات موجب نگرانی واشنگتن شده است، زیرا به نظر می‌رسد ایران از موشک‌های پیشرفته‌تری استفاده می‌کند که قادر به هدف قرار دادن کشتی‌های در حال حرکت هستند.
مقامات آمریکایی همچنین در حال بررسی این موضوع هستند که آیا چین یا روسیه ممکن است در شناسایی موقعیت ناوهای جنگی آمریکا به ایران کمک کنند یا خیر.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71309" target="_blank">📅 00:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71308">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WF53vdprmR62CBI6trHkYbBLtoJYS2C8gsjR2PYZcK29lxvx3g09Sc-ERMW16afyXHCCgSmrvQLU-eOQcViM6typ4d1_pxOXUB8YHVpm7IVZj4XJoligujlHXNk8EQzo6jbRaqbfL4pCC7-r9QBZW3kub33uhWtZlZ3B31GIikE_NMCFSmnfgzLa8BZcDFQLcyd7xlvyl6y0E7ccZu5GJ2bcctC_iIlx88_81ZBJUjGkbmFNX2bM0qOfmxLCIqBG4Isus5eLbVsokRKxz_tZR5diXrOMoXK1Uld3f8h3mWkkm2ZCczPhFPmILbkIpDHj8wj3tFC7vdQYNZdEWySPKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
نیروی دریایی سپاه:
به تمامی خدمه نفت‌کش‌ها در بنادر و لنگرگاه‌های کویت و بحرین هشدار می‌دهیم که فوراً شناورهای خود را ترک کنند، زیرا این شناورها هدف قرار خواهند گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71308" target="_blank">📅 00:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71307">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwF-az3rIW2VXdNZSiGDIabi2vDy6HjX4DUw5NTuBAQ_RjBboDWfaQf7vPaUrrA3MR6t02TZHsozpUwWVhykkoIQJe-GUj1a7nBqGH0Ei8_BfpxjcheFWCLEhbHKBjDLKKkNrm4WBTPcGqMoWxPFQqen1tZ2DpocK6AYrfTWl6J9zlN9RG7MAN0eeSpDy8OxxmRiJpgV6msyCrhNaJYjzh8f09mfUckYw6SrtYE4P7mFYXjX4JbLgE8s88rvox5rfX3lshHiIuZ7PvZgyiASFFOpFBBDXN2kgYOmOoP-CY96utW1FkXBRFW8JWL3Qe_laUl5iX_7ij6zm-aaTumcMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇺🇸
مصطفی نجف زاده:
آمریکا با هدف قرار دادن نفتکش‌ها در سواحل ایران و مشخصا خارک، علاوه بر اینکه می‌خواهد بازدارندگی معتبر در برابر رویکرد تهاجمی اخیر ایران در حمله به ناوگان دریایی آمریکا ایجاد کند، ممکن است گام تازه‌ای در راهبرد محاصره نیز باشد که براساس آن، قصد دارد حلقه فشار را از مسیرهای انتقال نفت به مبدأ حرکت نفتکش‌ها منتقل کند و صادرات انرژی ایران را از نقطه آغاز با اختلال جدی مواجه کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71307" target="_blank">📅 23:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71306">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
📰
فاکس نیوز:
امشب
برای سربازان امریکا دعا کنید
نیروهای آمریکایی به طور فعال در حال حمله به نفتکش‌های ایرانی در اطراف جزیره خارک هستند، به نقل از فاکس نیوز
ایران گفته است که در مقابل به پایگاه‌های آمریکایی حمله خواهد کرد، اما بدیهی است که ایران *خیلی حرف‌ها* می‌زند
امشب برای نیروهای آمریکایی در منطقه دعا کنید
و برای خانواده‌هایشان که بدون شک نگران پسران، دختران، شوهران و همسرانشان خواهند بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71306" target="_blank">📅 23:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71305">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/114d9f6af1.mp4?token=Tj0c8xGiSRAyBqB8GKkZHjMXz8LYCdzpAreF6MaDc5LoguGH94JqYN5w7RPhssHPgmu3eBaAGRMdfrAwq2WG9un-4vlaEawBgDZEHhF1Ltx3vkocvfItCdk1P1MsKR6-ex26BwJ04ijrAtbIh7xfzZcZSsUMuXU7EzXAehQJ5YW_67XYoNbcGO1kD4YBnEIofjryuMXwK_i6saTTvdgO1oabqkrSLi_Xb7bhKAmdCf-bznwL0M__W6P7XMVqON4YBJPMCMBMnk6PRAO0uxlODD5L4xbrzDSHC9YtKLR5Yu1DOGvL1oou_PzqBuBJYGUXrzbUj88NykbAG-WsRBsLTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/114d9f6af1.mp4?token=Tj0c8xGiSRAyBqB8GKkZHjMXz8LYCdzpAreF6MaDc5LoguGH94JqYN5w7RPhssHPgmu3eBaAGRMdfrAwq2WG9un-4vlaEawBgDZEHhF1Ltx3vkocvfItCdk1P1MsKR6-ex26BwJ04ijrAtbIh7xfzZcZSsUMuXU7EzXAehQJ5YW_67XYoNbcGO1kD4YBnEIofjryuMXwK_i6saTTvdgO1oabqkrSLi_Xb7bhKAmdCf-bznwL0M__W6P7XMVqON4YBJPMCMBMnk6PRAO0uxlODD5L4xbrzDSHC9YtKLR5Yu1DOGvL1oou_PzqBuBJYGUXrzbUj88NykbAG-WsRBsLTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این فیلم‌ لحظه‌ای را نشان می‌دهند که هواپیمای باربری آمازون در روز یکشنبه در فرودگاه بین‌المللی میامی از باند فرود خارج شد و متاسفانه ۵ نفر کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71305" target="_blank">📅 23:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71304">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96f0bbe630.mp4?token=TaJvLXEZ_InGr66EI4fcEH4Gi9gZyNtNmdL77DkVRNF_XrKlwMO2-ood_eCt1ocSr6gU1sg3g2WC9nwTSiuT4fIXwOfn9Og-GAQY7T4ZYJkB_aSB5okvB2JUJEZc8PZQZSKoM1mgs3HZ_MR5Cpi2GVhyJybsPNEW-1f4lra1W0ndJtgycsPD66TBByiN9WyivCScjBbCQ6KKMbkBAhP29tSED4QLIknbA0X2ItSVYU9VgKC6zCGMpfxXDfu8qnUHkCDbzK_obKBP6J9Jd6pi7KeAA1KhldFDujhWScB_LfoDROuSGi3CEG9543ve7ES5637R38O_y47kyQGeoJv_qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96f0bbe630.mp4?token=TaJvLXEZ_InGr66EI4fcEH4Gi9gZyNtNmdL77DkVRNF_XrKlwMO2-ood_eCt1ocSr6gU1sg3g2WC9nwTSiuT4fIXwOfn9Og-GAQY7T4ZYJkB_aSB5okvB2JUJEZc8PZQZSKoM1mgs3HZ_MR5Cpi2GVhyJybsPNEW-1f4lra1W0ndJtgycsPD66TBByiN9WyivCScjBbCQ6KKMbkBAhP29tSED4QLIknbA0X2ItSVYU9VgKC6zCGMpfxXDfu8qnUHkCDbzK_obKBP6J9Jd6pi7KeAA1KhldFDujhWScB_LfoDROuSGi3CEG9543ve7ES5637R38O_y47kyQGeoJv_qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
آیت‌الله بی‌بی‌سی از لندن فرمودن بنزین(۱۰ هزار تومنی) در ایران تقریبا مجانیه. این دقیقا عین جمله‌ایه که آیت الله بی‌بی‌سی برای مردم ایران پخش کرد!
تا حالا شده بی‌بی‌سی فارسی حقوق کارگران در ایران رو هم به دلار حساب کنه و نتیجه بگیره مجانی کار می کنن؟!
یا تورم رو حساب کنه و مقایسش  کنه با حقوق کارگر؟
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71304" target="_blank">📅 23:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71303">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3dcabadfe.mp4?token=jLm0yuWjT8bO-Z8MWI74gIjmh28sb1haFYVvV_Pk0qxcFhsX0K9oWaQ_l2xWTmzGURsc4UgbAwERvuyCXrjVRbLHlF0qKxfxuaYjkWQA7nUKeDG0orur7yI9IiC9gSbIi2YixBRjyTqYJsxyOevSQFt-8tOjrRopxKL9kR7E8dLSvXo8muH9ZB-MhwmVFhblBRP2lyCe08gI5I327yYGxvXuevBpxa3fdx8YT1DgOVMy4uB1tcgu-niqEp3iGmfLx1cEmuNPSTCQPO-S6idELEkENhqzaVMF8A4hGkwVL-6bZU9GaFsmICyMQhrVHV99mO7tRJ_CoK0sRQdjzQEkAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3dcabadfe.mp4?token=jLm0yuWjT8bO-Z8MWI74gIjmh28sb1haFYVvV_Pk0qxcFhsX0K9oWaQ_l2xWTmzGURsc4UgbAwERvuyCXrjVRbLHlF0qKxfxuaYjkWQA7nUKeDG0orur7yI9IiC9gSbIi2YixBRjyTqYJsxyOevSQFt-8tOjrRopxKL9kR7E8dLSvXo8muH9ZB-MhwmVFhblBRP2lyCe08gI5I327yYGxvXuevBpxa3fdx8YT1DgOVMy4uB1tcgu-niqEp3iGmfLx1cEmuNPSTCQPO-S6idELEkENhqzaVMF8A4hGkwVL-6bZU9GaFsmICyMQhrVHV99mO7tRJ_CoK0sRQdjzQEkAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
این روزا تور مدیتیشن و استراحت مد شده و طرفدارای زیادی داره
:
اونایی که مشکل روحی روانی دارن میرن درخت بغل میکنن و گریه میکنن
یا با حشرات توی جنگل و حیواناش اینا حرف میزنن حرف میزنن حالشون خوب میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71303" target="_blank">📅 22:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71302">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a391f5b86.mp4?token=YJzpaD3hYdbGtX1qeHLLAKJ1E01TTrkp0MYZOe14FvdzB3YYzGDhzxFNoYDzVPz__B4INmEEEEOK-kuQ0XEhQsUxQ_J2WM-JXXAGivOwUXVYqNF0_4V1t8dZFz1VCFqfI2ewWn7lSd2k6qTiY3fR7_3VViFv8eYveZswSHghjdNiGMTFhJ0-W_G5Pp51Lrz5DvCp-mpXzeOQ1I7epBmkObqd9EyCdS9FGg82FY7oo1ZA9qwDPcf28y7f3CynZ30kPRDjKCnpHWS3HhMboj69MtGAlMz8z65hnPufW68EBY_SlHOcc8LTfWsaAiANsc20JZEW2DLBWYq15dnH7fU4DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a391f5b86.mp4?token=YJzpaD3hYdbGtX1qeHLLAKJ1E01TTrkp0MYZOe14FvdzB3YYzGDhzxFNoYDzVPz__B4INmEEEEOK-kuQ0XEhQsUxQ_J2WM-JXXAGivOwUXVYqNF0_4V1t8dZFz1VCFqfI2ewWn7lSd2k6qTiY3fR7_3VViFv8eYveZswSHghjdNiGMTFhJ0-W_G5Pp51Lrz5DvCp-mpXzeOQ1I7epBmkObqd9EyCdS9FGg82FY7oo1ZA9qwDPcf28y7f3CynZ30kPRDjKCnpHWS3HhMboj69MtGAlMz8z65hnPufW68EBY_SlHOcc8LTfWsaAiANsc20JZEW2DLBWYq15dnH7fU4DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
اسکات بسنت وزیر خزانه‌داری آمریکا:
زمانی که بچه بودم و در کارولینای جنوبی زندگی می‌کردیم، خانه‌مان نزدیک یک مرداب بود.
گاهی مارهای سمی زیادی در حیاط پیدا می‌شد.
وقتی سر مار را قطع می‌کردید، مار می‌مرد، اما خودش نمی‌دانست که مرده است؛ بنابراین باید مراقب می‌بودید، چون سرِ جداشده هنوز می‌توانست شما را نیش بزند و دُم مار هم ممکن بود تا زمان غروب خورشید تکان بخورد.
اما وقتی خورشید غروب می‌کرد و هوا خنک می‌شد، تکان خوردن دُم هم متوقف می‌شد.
🔴
حالا مار ایرانی — یعنی همان رهبری — هم هنوز نمی‌داند که مرده است، اما در واقع مرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71302" target="_blank">📅 21:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71301">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc7c3d5f1.mp4?token=HXpfDkan4wk5VXgorymVujmc8i6_wyJtrvESAPv5NTT_yQv36LievU6578l4xTNjrdWmxlaym0eymlu1poauqmqNNYTwsWs9o6RgfIfYQRXBAINKFrCynun17IVfw3MOCdFQetyOlaj7Tkv0R5vsGbsEUOHBhCWLJOj4H7LmJNf7RFtU5e5fSho1-YR3E7LAwrGeXzHrJXwbpKWCuGgGttWSAHROEYy0tmlhKH4QhlUo0knbvCZI1vEoXcqCBKYQupwn9Fy5VAaI1VG0NH4GyCcFbQa7cs6qlEM9olGIB5l5yZKQTcgfPAJz5P5vAL4U1S9fvSlGKPybX70luQTL4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc7c3d5f1.mp4?token=HXpfDkan4wk5VXgorymVujmc8i6_wyJtrvESAPv5NTT_yQv36LievU6578l4xTNjrdWmxlaym0eymlu1poauqmqNNYTwsWs9o6RgfIfYQRXBAINKFrCynun17IVfw3MOCdFQetyOlaj7Tkv0R5vsGbsEUOHBhCWLJOj4H7LmJNf7RFtU5e5fSho1-YR3E7LAwrGeXzHrJXwbpKWCuGgGttWSAHROEYy0tmlhKH4QhlUo0knbvCZI1vEoXcqCBKYQupwn9Fy5VAaI1VG0NH4GyCcFbQa7cs6qlEM9olGIB5l5yZKQTcgfPAJz5P5vAL4U1S9fvSlGKPybX70luQTL4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اقتدار به روایت تصویر؛
🇮🇷
مقام جمهوری اسلامی:پمپ های قدیمی جا برای بنزین ده هزار تومانی نداشتند؛
یک صفر دستی اضافه کردیم
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71301" target="_blank">📅 21:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71300">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">از دیشب تا همین الاناست که مسلمونا افتادن به جون هم، شیعه های یمن، سنی های عربستان رو دارن با موشک و پهپاد می‌زنن، یعنی کشوری که خانه خدا اونجاست
عقل
🤯
#hjAly‌</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71300" target="_blank">📅 20:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71299">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCHTted6PcTPbryxMTosU-YFoP0U2FSnMenU7CFJHBJgKAfKSRN9y56GYuNukx9vAYqhzgIudvQXvn0P69aHc49vQn8f5tcF5_AOoRflNKudGd9UAOsD9Y3d19Cn3bTy5eY-_IwG6quJVeT9F_poeqLmxrBVZc9cIAi8ssl0XcnAmuq-g1XOuYOAdKsRLCwY7cQORAm-ziWiUvzeqScIXo6ugiN9HYOuOExDyOmE2JCdATTqK6F0dNbdOiNVSdmxvVm8ZOihLBNmWiT8kIhVPBRXpS4_xZfVijecdf7uHWsgywFwP_AcuHNTUgqNsqd1SF9CeWWpRh3Nnlbw3FtUww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
⭕️
⭕️
وزارت خزانه‌داری ایالات متحده تحریم‌های گسترده‌ای را علیه بخش هوانوردی تجاری باقی‌مانده ایران تحت عنوان «عملیات اقتصادی مطرود» اعمال کرده است که ۳۶ نهاد را به دلیل حمایت از خطوط هوایی ایران، دور زدن تحریم‌ها و شبکه‌های تهیه هواپیما هدف قرار می‌دهد.
دفتر کنترل دارایی‌های خارجی (OFAC) ۲۷ شرکت هواپیمایی فعال ایرانی، از جمله ایران ایر تور، هواپیمایی آسمان ایران، هواپیمایی کیش، هواپیمایی قشم ایر و هواپیمایی زاگرس را تحریم کرد.
وزارت خزانه‌داری همچنین چندین مجوز هوانوردی، از جمله مقرراتی که پروازهای خاصی را مجاز می‌دانست و به شرکت‌های هواپیمایی غیرآمریکایی اجازه پرواز هواپیماهای آمریکایی یا تحت کنترل آمریکا را به ایران می‌داد، به حالت تعلیق درآورد.
این تحریم‌ها همچنین شرکت‌ها و افرادی را در امارات متحده عربی، ترکیه، بریتانیا، مالزی و قزاقستان که متهم به حمایت از ماهان ایر هستند، هدف قرار می‌دهد. وزارت خزانه‌داری اعلام کرد که برخی از آنها انتقال حداقل سه هواپیمای بوئینگ ۷۷۷ به ماهان ایر را از طریق امارات متحده عربی و عمان در تابستان ۲۰۲۶ تسهیل کردند، در حالی که برخی دیگر محموله‌هایی از جمله قطعات پهپاد، تجهیزات صنعتی و قطعات هواپیماهای ساخت آمریکا را جابجا می‌کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71299" target="_blank">📅 20:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71295">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nF3L6FgGRsndmgrwUccm34xt_5DK9COZWYYoRWGquZ8YEbhkYmSTrlQeUm9EqXDRAhWlBAhn27YiPLGV3cFLImbyQPRcockvuxMOljsdc4FQW0uVqmScDibWaF9Zx7AqEkPoJws4o48vWnI7Cc9kk8v1k4xYR4qMP9khQo2GKbNp9lfkQwBi5aIAW3MFjBvUMEDEAaziRKaiN6d2vQ30y2Gh9ZGMHWj0RIeveT2qNbqPvSP1PszwZ5Rqg01IRrkfjYtdGgNgY9_JtQVbjHi3PuEVWbGkorxNTBfWQACv3kgzCTHuRaBAmEAWzQ8b0bv50_uqF5w-xgJKo6fr4GW09A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d307bda604.mp4?token=lC7e54oqvi9RhKUEb4CQRetpDwBbPFJm28J2NEhTii4o4va3QgEx1EBW_B-paXA-E1tgKryG6cNbRLEBsKi5B82pBkIIgHTMrPCF38Kl0syOzLasObyC8eKAeB-80QHhZiaQvt_GXf8oyB9rVyzr2i8dl2BJB4M0s5NYibDlOVUe81YyOrKi_vKre35gkrR-w6RLMd184XKcBihOHC9u0j8MH789ZATs0V0v__pUIX2NwErx0QK9y-7ScBha8ZDx3-4kRJCVhJ8UPpOWeHdqSeBfak-LlUInFi1R36-e5QcZtZ95f7WG-RVh-mgSqTkGyi8nX_MaOfAt7iuGBJ0gLw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d307bda604.mp4?token=lC7e54oqvi9RhKUEb4CQRetpDwBbPFJm28J2NEhTii4o4va3QgEx1EBW_B-paXA-E1tgKryG6cNbRLEBsKi5B82pBkIIgHTMrPCF38Kl0syOzLasObyC8eKAeB-80QHhZiaQvt_GXf8oyB9rVyzr2i8dl2BJB4M0s5NYibDlOVUe81YyOrKi_vKre35gkrR-w6RLMd184XKcBihOHC9u0j8MH789ZATs0V0v__pUIX2NwErx0QK9y-7ScBha8ZDx3-4kRJCVhJ8UPpOWeHdqSeBfak-LlUInFi1R36-e5QcZtZ95f7WG-RVh-mgSqTkGyi8nX_MaOfAt7iuGBJ0gLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌂
امروز صبح رسما شمال کشور رو سیل برد!
به حدی بارون شدید بود، که حتی آب توی خونه‌ها نفوذ کرده و تبدیل به استخر شدن.
ماشینا وسط خیابون تبدیل به قایق شدن و برق اکثر مناطق قطع شده.
باد و طوفان شدید باعث شد کلی درخت و... شکسته بشن و بیفتن روی ماشین، خونه و مغازه مردم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71295" target="_blank">📅 19:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71294">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SONwRVbzBqyjrm3mhmBGH1oC8afWJGvXF9gngq8cFPHBhcLhLkF0js-qxbxGuaJYHtnh5o7xDEJOBdB2G8R7u-9lKu3cppdBy3uiwS45cJgazkBvKkdF4LSm9L12Uw-JQyslu1MR38zrVxrRpnlhzNcl0g2qZlLu8c7dBOlm_S7F9arKPC37fSXlLOBllbkNClr9yv9vgtqjQEkLxoQWUyhA-59to5VgYzvmrvg_5MK4AW0TJC4vm7o6ynJKlP-hgDH8_XjM7K9uQlErL6jmRnDWfaLXXd9zWy3qMBprQEal_pKkfSYcO12xDjuSQxs64L3jUrZCHtGcBmlIzUap0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران انقلاب اسلامی:
مردم مبعوث شده ایران عزیز؛ با عنایت خاصه خداوند متعال رزمندگان نیروی دریایی سپاه یکی از مدرن ترین زیر دریایی‌های هوشمند و بدون سرنشین ارتش تروریست امریکا را در ورودی تنگه هرمز طی یک اقدام پیچیده اشراف اطلاعاتی و عملیاتی در سحرگاه امروز به دام انداختند.
این زیر سطحی هوشمند از جدیدترین تکنولوژی در حوزه زیر سطحی در دنیا برخور دار بوده، که سال ۲۰۲۵ میلادی به ناوگان ارتش تروریست آمریکا تحویل شده است.
گفتنی است این زیر سطحی اکنون به غنیمت گرفته شده و طی ساعات دیگر تصاویری از آن منتشر خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71294" target="_blank">📅 18:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71293">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">⏺
🤩
تسنیم:
تا دقایقی دیگر خبری مهم از شکار رزمندگان نیروی دریایی سپاه در تنگه هرمز منتشر می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71293" target="_blank">📅 18:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71292">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7da31dc3dd.mp4?token=c-pBUia4FyAu1ab8ZUruBo0XbXEQyr-s1C20SdhYvrvMiQlWRX4OZ-zDI5aLzFZheJ8iVCjuTBN28iBcPh4Chh8lbLd9Piy9M4xJnPgYn0Dj1LxCoGyTiGd0q51SmTnRaL5t4f8lUnbb_uVwC6JjQftSuumOnY0s9jJSJTVuofoJOCvgjFTOt8sCprZdTqjf7zA6-wlu75ld6eo11rvkrNLlTUiEPHmFNSLeuseXoyQx0LXZw6ewz0uNThrdIBDkgXDjJiM42A9Hhe0tB2gLum00kZonpr02HEqKNdt_AFq4fjvF7tBspA9N_ydwS3dSAw6b_l77bnfsChDrVbilUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7da31dc3dd.mp4?token=c-pBUia4FyAu1ab8ZUruBo0XbXEQyr-s1C20SdhYvrvMiQlWRX4OZ-zDI5aLzFZheJ8iVCjuTBN28iBcPh4Chh8lbLd9Piy9M4xJnPgYn0Dj1LxCoGyTiGd0q51SmTnRaL5t4f8lUnbb_uVwC6JjQftSuumOnY0s9jJSJTVuofoJOCvgjFTOt8sCprZdTqjf7zA6-wlu75ld6eo11rvkrNLlTUiEPHmFNSLeuseXoyQx0LXZw6ewz0uNThrdIBDkgXDjJiM42A9Hhe0tB2gLum00kZonpr02HEqKNdt_AFq4fjvF7tBspA9N_ydwS3dSAw6b_l77bnfsChDrVbilUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
⚠️
🇺🇸
افسر نیروی هوایی ایالات متحده که در ماه آوریل پس از سرنگونی هواپیمایش بر فراز ایران، دو روز زنده ماند، برای نخستین بار در برنامه «۶۰ دقیقه» (60 Minutes) — که قرار است روز یکشنبه پخش شود — به بیان ماجرا می‌پردازد.
این افسرِ مسئولِ سامانه‌های تسلیحاتی که نام عملیاتی‌اش «دود ۴۴ براوو» (Dude 44 Bravo) بود، یکی از دو سرنشین جنگنده «اف-۱۵ ای» (F-15E) به شمار می‌رفت.
در حالی که خلبان ظرف چند ساعت نجات یافت، «براوو» به مدت دو روز در مناطق کوهستانی ایران، در حالی که مجروح و تنها بود، از دست نیروهای ایرانی پنهان ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71292" target="_blank">📅 18:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71291">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71291" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71291" target="_blank">📅 18:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71290">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdxG9gdOc8xoMv26WkaOZB5k48JSeYSjkVHzypE5NwbqRRVdwNad3a-p0SeIQcT_p47krAK2dUFev7w4D5t75d41RWFU_87WPI3Rgyz_ePi3izZZh1rSzWadlWH_KQi520R4JK527V1cSKZ7HH2gLdNtAAT1TWy9BO9pahucQvvJE4VvmYa4Mv-C_YhNHMrZOHXN2QND1SZKH8u2iGQuyQOAjICD4Q9Cyh96ovmRbwUHxIwPGDSczAt3rzeHankrtTbgS0Y5byZkRE5aSXpVWQJB8xayz58P3XmD5XFuoCm9gkZ_etQ4EPpfpw5WxNyCxFR2965W5YxDBGbwNUTA2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شبِ بزرگ فوتبال اروپا فرا رسید!
⚽️
منچسترسیتی
🆚
پورتو
⚽️
🎯
این نبرد حساس
چمپیونزلیگ
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📊
نگاهی به آمار ۲ تیم در تقابل‌های اخیر:
⚽️
منچسترسیتی: ۴ بازی، ۳ برد و ۱ تساوی، ۹ گل زده
⚽️
پورتو: ۴ بازی، ۳ شکست و ۱ تساوی، ۳ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71290" target="_blank">📅 18:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71289">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
دقایقی قبل صدای سه انفجار از سمت تنگه هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71289" target="_blank">📅 17:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71288">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b881718fc3.mp4?token=CF4m4a6fw8t0Eh_Ah8_xDqO9dGpmbtuGn4wt8LnG0AaGGT_WKF35QNnBG7jNo_5EUK9qEXuKUk5KpheOKY-JlRYSOji0CWotSBv-yZKxYlD8Mo4HIjKKDiGRVYt3JXLhasQVDcUFE9d9TFnNSdTt4DgXr23YQrz1i_nEXQYwTYn_XXG5k-3HqxLC6h6KVmdYEOChkuVAgNNnlBh6-LZTLcGf5qKEpTh8YtxchbkUhooAEaK1dlTEQn1T7n3bfM_qDjwyrGqgSRdfa8efqhQ76u_6Xut3ipyHvjBtcEfWGjSO5PkH2A6dFUqwV1TZLDN8_UTPMeC_qcNIh2clzrOZiZkHk0V4QaMAZqE1E89s4ngDztAOtYvIum1P-a3gV3EpDLvyCD9m-YxBvrF7D_-IxLXzCPTMh833l9ZLKTmo2DtOzJLfvX0hvrM7opJK3ic9CW6LQVPaQtM1SvBbThA8zIG92sPSlrerbSJKS4FCfUzdDkp5mEJHb-AREvbodVPCK93l8AmJ3iwq9rhy8RKtUYpsLXMLPzKBWhhD5MSqAboK_GQTxDxfXSWdNknIH8ORaJh5dzroafimAGoGxK-r_oY7-LNvKbL-thsoRxzugTLl60HvQN2X45Oe9YeMIcoyaadGAcwifIiBwNu7ExLJo6GA-iY_wB51uIbQ9feA6Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b881718fc3.mp4?token=CF4m4a6fw8t0Eh_Ah8_xDqO9dGpmbtuGn4wt8LnG0AaGGT_WKF35QNnBG7jNo_5EUK9qEXuKUk5KpheOKY-JlRYSOji0CWotSBv-yZKxYlD8Mo4HIjKKDiGRVYt3JXLhasQVDcUFE9d9TFnNSdTt4DgXr23YQrz1i_nEXQYwTYn_XXG5k-3HqxLC6h6KVmdYEOChkuVAgNNnlBh6-LZTLcGf5qKEpTh8YtxchbkUhooAEaK1dlTEQn1T7n3bfM_qDjwyrGqgSRdfa8efqhQ76u_6Xut3ipyHvjBtcEfWGjSO5PkH2A6dFUqwV1TZLDN8_UTPMeC_qcNIh2clzrOZiZkHk0V4QaMAZqE1E89s4ngDztAOtYvIum1P-a3gV3EpDLvyCD9m-YxBvrF7D_-IxLXzCPTMh833l9ZLKTmo2DtOzJLfvX0hvrM7opJK3ic9CW6LQVPaQtM1SvBbThA8zIG92sPSlrerbSJKS4FCfUzdDkp5mEJHb-AREvbodVPCK93l8AmJ3iwq9rhy8RKtUYpsLXMLPzKBWhhD5MSqAboK_GQTxDxfXSWdNknIH8ORaJh5dzroafimAGoGxK-r_oY7-LNvKbL-thsoRxzugTLl60HvQN2X45Oe9YeMIcoyaadGAcwifIiBwNu7ExLJo6GA-iY_wB51uIbQ9feA6Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇬🇧
⭕️
#فوری
؛اد میلیبند، وزیر امور خارجه بریتانیا:
ایران هرگز نباید به سلاح هسته‌ای دست یابد؛
از این رو، ما نیز در این هفته همگام با متحدانمان اقدام به ارجاع پرونده ایران به شورای امنیت سازمان ملل متحد به دلیل نقض تعهدات هسته‌ای‌اش می‌کنیم.
همچنین امروز می‌توانم اعلام کنم که ما در هماهنگی با اتحادیه اروپا و ایالات متحده، تحریم‌های اقتصادی عمده‌ای را علیه ایران مجدداً اعمال خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71288" target="_blank">📅 17:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71283">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/645274372a.mp4?token=e2K69y2C6goE1e_osdQJAAAno-SDx2DmbZOYrlKrBftBZGmE4eUmXxRridZ0BWDlG2gVnuQeBHZ23ymUraE17m6rLh7V7OpYJyowDblJFn2YRQygGoy5q4qHCPfyvfooTBbR3iHNMzjwln6Z73uK0KSM3hOVuJkXXPYTiQHwFYDlKU_nuskr38GMS_HR6fBnzkBmsL25Qb3iE9tL7-97SiaCqB3QB4dAudPHQ7cEJYeDVybXbzLRro6HmJuBCVxq8P56BuIhSOuArjiR_FMsUKYiKrVUQDyjhmua8MZlz1roPCbRp8BUm0yLY9y34s_lDQZd7S4nC85s1kNXSTp4Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/645274372a.mp4?token=e2K69y2C6goE1e_osdQJAAAno-SDx2DmbZOYrlKrBftBZGmE4eUmXxRridZ0BWDlG2gVnuQeBHZ23ymUraE17m6rLh7V7OpYJyowDblJFn2YRQygGoy5q4qHCPfyvfooTBbR3iHNMzjwln6Z73uK0KSM3hOVuJkXXPYTiQHwFYDlKU_nuskr38GMS_HR6fBnzkBmsL25Qb3iE9tL7-97SiaCqB3QB4dAudPHQ7cEJYeDVybXbzLRro6HmJuBCVxq8P56BuIhSOuArjiR_FMsUKYiKrVUQDyjhmua8MZlz1roPCbRp8BUm0yLY9y34s_lDQZd7S4nC85s1kNXSTp4Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇸🇦
🇾🇪
نیروهای «شورای رهبری ریاست‌جمهوری» (PLC) تحت حمایت عربستان سعودی به همراه جنگجویان قبایلی، شهر «الیتمه» در استان الجوف را از کنترل حوثی‌ها (انصارالله) بازپس گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71283" target="_blank">📅 16:47 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71282">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">⏺
فارس:
یک پهپاد MQ-1 بر فراز منطقه راهبردی تنگه هرمز با هوشیاری نیروهای پدافند هوایی جنوب شرق ارتش جمهوری اسلامی ایران شناسایی شد و هدف قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71282" target="_blank">📅 16:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71281">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77de453ade.mp4?token=ioXUcwW48Rr4F_Xq7i5vAAXtD8xogHd1P94iqW7WJe-eNDkCezjIwNckfARZ53m4XFuxtSvhDf75cSWs04gsbqBzjSvZGWiTLTpPu1LKibGsU4rLIoxo6ZtWqdkmMKmjj1Q0CukhJqe8gfNrWZ5lktwWL386W1loatouCt3AQkX4DJy35RONLgMjwGeFqHhrayQTjZYWM92opNpHrYph4ZD7IYCYKjHinhQL0PXigTKOkgnR-uRLQMJ0UsgCQZfvyEfjQ1hmABloWpsqNnZWg2BDC00R1Vx4oWkLIL_-RxRLRFF7FUp7_Q87Yd3We6B3jeBT0SmZDdEQDBr4mbAr-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77de453ade.mp4?token=ioXUcwW48Rr4F_Xq7i5vAAXtD8xogHd1P94iqW7WJe-eNDkCezjIwNckfARZ53m4XFuxtSvhDf75cSWs04gsbqBzjSvZGWiTLTpPu1LKibGsU4rLIoxo6ZtWqdkmMKmjj1Q0CukhJqe8gfNrWZ5lktwWL386W1loatouCt3AQkX4DJy35RONLgMjwGeFqHhrayQTjZYWM92opNpHrYph4ZD7IYCYKjHinhQL0PXigTKOkgnR-uRLQMJ0UsgCQZfvyEfjQ1hmABloWpsqNnZWg2BDC00R1Vx4oWkLIL_-RxRLRFF7FUp7_Q87Yd3We6B3jeBT0SmZDdEQDBr4mbAr-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
جنازه و تابوت ترامپ و نتانیاهو زیر پای طرفداران حکومت برای بار هزارم له شد
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71281" target="_blank">📅 16:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71280">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a724fc44e.mp4?token=O02oA0HIoWvJucSMINVvO7cIrH39Di4e-uaGrWb0ZWLfobXo2OhE38E5LrmNgS8atjSNA3aHGdZnexvTXDmhR4nXaJcMq4UpUd2X8fGtNJYk_H2FHoUU5TPR_epQsMJcIVHdv6s5CvzO8hbizlM7I7uR2GENhdr1sZJ7ye9Ix1HtZvsrBlyGme54E8hlPtL6xpzmWb1Xz5jGenFdMhdaHSjcFiyER89GgLuTkuy2_ypR5nL3s1kXa7nCvq4TaALM-9Z7VDvVExwcl2xVAy6O0-ZswqRa68oAKQ2MNapwXZAJVjhW2DT88twqT2fKO6R09q1ebK6Jo3eFYS1KOeXV1E37-WUjDxAmkB8FylsTeFu_faRWKoT4lxs5dSyDBmV15lrYmjBOnEOgsGNTKjWFnkWqpkSi6HuV-9iU71NdEa_1fpzRM2FPZbvfm9Awy99e8l6_RrxKmEZebGNMAuCHn6ZBcpwgQE6eXchJBh6WMU4H8mqSukVBDxlC6tlyusUSgLJgEpIpcUI6qwjGEXgXrrDTbJM4l3SIWSvWNX6ZSs0fd_kIXz_lbZOjEw78O9HHJQbsGEdqPyNdt0M01GiEZrBvPN4x9IGIu0SpKTD0IL_QQ2e0dYdCipgJkJ4x92nYaegsy0GMsyh1tEwMaMKPouMgrmoGzSFjAC9msmwk8IY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a724fc44e.mp4?token=O02oA0HIoWvJucSMINVvO7cIrH39Di4e-uaGrWb0ZWLfobXo2OhE38E5LrmNgS8atjSNA3aHGdZnexvTXDmhR4nXaJcMq4UpUd2X8fGtNJYk_H2FHoUU5TPR_epQsMJcIVHdv6s5CvzO8hbizlM7I7uR2GENhdr1sZJ7ye9Ix1HtZvsrBlyGme54E8hlPtL6xpzmWb1Xz5jGenFdMhdaHSjcFiyER89GgLuTkuy2_ypR5nL3s1kXa7nCvq4TaALM-9Z7VDvVExwcl2xVAy6O0-ZswqRa68oAKQ2MNapwXZAJVjhW2DT88twqT2fKO6R09q1ebK6Jo3eFYS1KOeXV1E37-WUjDxAmkB8FylsTeFu_faRWKoT4lxs5dSyDBmV15lrYmjBOnEOgsGNTKjWFnkWqpkSi6HuV-9iU71NdEa_1fpzRM2FPZbvfm9Awy99e8l6_RrxKmEZebGNMAuCHn6ZBcpwgQE6eXchJBh6WMU4H8mqSukVBDxlC6tlyusUSgLJgEpIpcUI6qwjGEXgXrrDTbJM4l3SIWSvWNX6ZSs0fd_kIXz_lbZOjEw78O9HHJQbsGEdqPyNdt0M01GiEZrBvPN4x9IGIu0SpKTD0IL_QQ2e0dYdCipgJkJ4x92nYaegsy0GMsyh1tEwMaMKPouMgrmoGzSFjAC9msmwk8IY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چنتا دختر با کیسه زباله خودشونو شبیه لاکپشت های نینجا میکنن میرن تو خیابون...
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71280" target="_blank">📅 16:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71279">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b2ae4bae8.mp4?token=WiANysuslVyoo4sjEW221zCl1_k-QjGhAVb5NZQQ2EVr-fhvQnXwjWCmJeFRwDs6YRhRXELXILj2RyPmDupSWHVbSos6hICk-3ILDKXUyj-_bEXrHGpt1HDUsOULL4D1cXulCq-K3dh_dpWbLNjh0HTTjaiUmUtM6dqW1vnrlwtchEiK-lSuoJva9vn1yu93gHqkosv0MdKw-SKQuaMMBGJUBp6T7VFluKvyLLQZkaSE81UdYJYhkijHjeJtrEFBzJ-9zoZx4Zixb5CJkTauAY7RukUtJAJGyt4Fc33A2hWZOdD7UDKxvLmeDbimq5Q3gh_LAjZykAIH8YC4ltXXbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b2ae4bae8.mp4?token=WiANysuslVyoo4sjEW221zCl1_k-QjGhAVb5NZQQ2EVr-fhvQnXwjWCmJeFRwDs6YRhRXELXILj2RyPmDupSWHVbSos6hICk-3ILDKXUyj-_bEXrHGpt1HDUsOULL4D1cXulCq-K3dh_dpWbLNjh0HTTjaiUmUtM6dqW1vnrlwtchEiK-lSuoJva9vn1yu93gHqkosv0MdKw-SKQuaMMBGJUBp6T7VFluKvyLLQZkaSE81UdYJYhkijHjeJtrEFBzJ-9zoZx4Zixb5CJkTauAY7RukUtJAJGyt4Fc33A2hWZOdD7UDKxvLmeDbimq5Q3gh_LAjZykAIH8YC4ltXXbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
آتش‌سوزی در تاسیسات آرامکو عربستان سعودی در پی حملات حوثی های یمن
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71279" target="_blank">📅 15:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71278">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef148c5074.mp4?token=RP62HUkOVsRwKl9U2QpC0y35X_Q6q4b04Fcqu5VmAOcRHdLlKPM1AKuUH4XzTra2k_5oiFIBAIho5HnAb8V4JAASOeiW2yRORWkLwOaWjYosE_9S9eSXiGF4I_CJ_veuHBwkWtF3If_ox0sPs-XQEvqcRtV1JZ5wmRe8X4fQhR571SJnmDKEXOBhykQAnQ19KsYXfeySvmj-DicyuQrRM4J_w2gITz99AOFnFaO8RPeBRJAtgYNwLrZpqWeDNLb562gAFGYYQ4J43bSvwexSxMRNDysTPQQsdih8a0RQWEtVnVrFLqVJfTMRowimb_PBjG0pLgW9YLT8rLT6xEsgNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef148c5074.mp4?token=RP62HUkOVsRwKl9U2QpC0y35X_Q6q4b04Fcqu5VmAOcRHdLlKPM1AKuUH4XzTra2k_5oiFIBAIho5HnAb8V4JAASOeiW2yRORWkLwOaWjYosE_9S9eSXiGF4I_CJ_veuHBwkWtF3If_ox0sPs-XQEvqcRtV1JZ5wmRe8X4fQhR571SJnmDKEXOBhykQAnQ19KsYXfeySvmj-DicyuQrRM4J_w2gITz99AOFnFaO8RPeBRJAtgYNwLrZpqWeDNLb562gAFGYYQ4J43bSvwexSxMRNDysTPQQsdih8a0RQWEtVnVrFLqVJfTMRowimb_PBjG0pLgW9YLT8rLT6xEsgNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
در سمنان برای دومین شب پیاپی میان مردم و دانشجویان عراقی وابسته به حشدالشعبی درگیری شد.
این درگیری روبه‌روی خوابگاه عراقی‌ها در باغ‌فردوس اتفاق افتاد.
ماجرا مربوط به متلک‌پرانی و مزاحمت آنها برای زنان و دختران است که بارها اتفاق افتاده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71278" target="_blank">📅 15:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71277">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C1Ixbd3V7xZ6cRx1LxGzYVX5t9hd5ntQnkvGOTBjtzywqiECIOX6mrYBEsLHjj_-xycA7vOdTIOrWuS3BqzZdes6XJFbYi5AGxRIHK6Z1StXuCf_mvLiISuLX8ZHo5LnzupPTLhmFOJKJlpfNtCpbIvD66s4FiRdHWnYtzn6UB_VWOGTfEmUum7eDmhg05_lt1-NKM-u80n7XuivkZZsSGmtZf1-Icn5z3lgBwbPGbhS34u3lJY53aD8ZKEkZ4Je997p04kkD8hmYJDCjrWMkzyOtVcxT_L2nYXNIZrNLtELmZ6tL_wNEpkzsIZcsfSc-ukMP_hiE8s2g13HprW6sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
امروز ۱۷ شهریور، تولد مجتبی خامنه‌ایه و ۵۷ ساله شد.
اگه زنده ای شمع هارو فوت کن
.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71277" target="_blank">📅 14:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71276">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed3b8e81d9.mp4?token=TXau-AZaJnyE12GwZUBUotGwJjqr1dfE_4E-qjHhMCy2fma4GbxUmuKI0arimzUNT_dSb_yOOuZw42Uw_axk8jRWAkhKipqOYvwqZojQ_WufQ3c5On9v_Iwv_DZhwjaKysF12hjVDS4krHzyYRtYMjZ2DLcOSCiQnvhpj7pddQ2hP20lLGR0j7Gu-tvwzoSiQ68MdAUpCpgShj1oadZMB18z5SaBgAqI2VKIF_YroPE2YM7ypoFT4wpqRfQQJiio-htTgX_SoKWt5hQSyBTYUHKv1GuVu5P47a-5VI9JsaQ7cWJrJGfEfqVzSak8kNaoFc0QNwx08k6r5IMsSJE2lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed3b8e81d9.mp4?token=TXau-AZaJnyE12GwZUBUotGwJjqr1dfE_4E-qjHhMCy2fma4GbxUmuKI0arimzUNT_dSb_yOOuZw42Uw_axk8jRWAkhKipqOYvwqZojQ_WufQ3c5On9v_Iwv_DZhwjaKysF12hjVDS4krHzyYRtYMjZ2DLcOSCiQnvhpj7pddQ2hP20lLGR0j7Gu-tvwzoSiQ68MdAUpCpgShj1oadZMB18z5SaBgAqI2VKIF_YroPE2YM7ypoFT4wpqRfQQJiio-htTgX_SoKWt5hQSyBTYUHKv1GuVu5P47a-5VI9JsaQ7cWJrJGfEfqVzSak8kNaoFc0QNwx08k6r5IMsSJE2lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
شب گذشته در سمنان، به افزایش قیمت بنزین اعتراض شد.
این اعتراض در پی تصمیم جمهوری اسلامی برای دو برابر کردن قیمت بنزین خارج از سهمیه یارانه‌ای از روز سه‌شنبه صورت گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71276" target="_blank">📅 13:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71275">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXXD4J8cxTk_11ueuvfS92Ghw9rDYI5Nc89kwhR3V_PU9NIb_vgFiNkj5Gqg99gaK9Uld9apEjIwgIAShdhju2E17gW9IHsGs0Uy-HnKuzrDmRG15kejqOGURBckpR_5rA_i9b0DH_bXbODC9v1nl7zvQf_nHiJVS4FIHNbTU29Ao_oM-nYI2UkjiGD89A6UuCHD7JWD6DOdTCzYg4w6YyBDa9b4MlVWK347y3zZbB4QD5qxmeibwUP7l0l_O29rRxWjbb_6ThvQVbw0M8hs_ThwRJfc83MvuCjFy7uqpoHrvbERset7Tu6LFUXoj5XzKLpvAsXxADREg0exkL9njw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
مسعود پزشکیان:
جمهوری اسلامی ایران همواره با جنگ مخالف بوده و حفظ منافع مردم و امنیت منطقه را در پرهیز از آتش افروزی دانسته است.
اما چنانکه تا امروز در برابر تجاوز، دلیرانه به دفاع برخاسته است این مقاومت را تا پشیمانی کامل متجاوزان با قوت ادامه خواهد داد و پاسدار حقوق ملت بزرگ ایران خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71275" target="_blank">📅 13:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71272">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KMBEhfJMmXMSydQNhvUJ8iTOxcZXuZwR3cScZKjBLPXoqhga6ZhVtmB6hfTsWhXE7b2S4UVA5NcVJpjmO9UxVHPLX6EOyD7ZA0hWmnBM0fvO3R1RVqHNadln5L3T6SEQdB_Ra6rcPXg2EtACGB9p5u-qOeGPZzgLH7_hi0nhGoNnoEzniZgTt0zM1iWsKU3W_8vWZWqLBRM-eC1DJwJ2C1T0xVn4kYfACsBjijwNjsob8fhm06ZaxvsPW8-n_AHL0CE86i0043oefw6P54ntHM4AQi5lTb_vJitka4IX3ViKVJ_ZDzI9pKvdBJLiLm20eA7NVZ4NSOWkpOybiys0sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8833895957.mp4?token=segfQ33gu_lRK28sey7pv5NasmmgvmEEI8GdWsE8-YJ4NIH3oIOP4B9N4pz7OIafpQYuSo_ZE1slCcv2AJV25r0aVSDWT39vELqgMnrbF3o4wcDW2sQvQMUehKwRTVefXjY3d1LNXAKzR-BMRRwdBFgW-eELH3K6dI-1UbvRifOWytO22ub4A7C8mQMUKDBOni9KtzxNDbFkHC8TTvWjRPStmJN0-mIesMWtdKamTSyc4xMrNhBeyjebAZjn8Nb8NrvKCJj5Xg3Y_WkPrzmnRF0_AeQmERJrRmEUcKGyf5m3N5G3fVY1C8KiWRnlkoJDNwLcp7y5ff-L9qyr4yECng" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8833895957.mp4?token=segfQ33gu_lRK28sey7pv5NasmmgvmEEI8GdWsE8-YJ4NIH3oIOP4B9N4pz7OIafpQYuSo_ZE1slCcv2AJV25r0aVSDWT39vELqgMnrbF3o4wcDW2sQvQMUehKwRTVefXjY3d1LNXAKzR-BMRRwdBFgW-eELH3K6dI-1UbvRifOWytO22ub4A7C8mQMUKDBOni9KtzxNDbFkHC8TTvWjRPStmJN0-mIesMWtdKamTSyc4xMrNhBeyjebAZjn8Nb8NrvKCJj5Xg3Y_WkPrzmnRF0_AeQmERJrRmEUcKGyf5m3N5G3fVY1C8KiWRnlkoJDNwLcp7y5ff-L9qyr4yECng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌧
بارش شدید باران دیشب در رشت که منجر به وقوع سیل شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71272" target="_blank">📅 12:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71270">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stCLgozEAJvpt3_lYlxfvi5O_lGEI_bghqd6dqWO9_b9SKC8xA7l57TsvXORE4-13FDVroqi5V679djSmRQjI1DE_kBwOpRFD76lGHyzBiXy0it90oDDpjbBSLWqDzKZCvFz7iI8PSaPntSuLcthwtOjf_jiyvYKuRqad0K0_TrZLdolaOAX7vR3iVVW1arzD9bN6cGoWi0J8VcXcsGv4ILN5mVZKow0hFjdYyUVq8N2CuvilEGaqmwfYyTB7FxVlS9x_YHOb0QfSpE4ggCWNFLpI8Sr6TFxs33mykSPib1dEBvF_66RCK-LQ_ydyeLho5QlIWfyfxa4gtbfkDmrGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9bd51248f.mp4?token=CqC5L3xp3aCj7VxrMAlXlhgnHdzdVpFJE5WgZtXUcEaeiYF7ZcQKsWRVN0hQyaN6yqHT1Dc0jvIzqhammpswISHDZ0W8vS29q4jegK-YkiEMatSKVfFaNoLBZiqVjCoOC0R3G6qe9FrUYir5VbXqxLnUjRhrdy98ERCJrMuFUQf-aQRLqJ_hBDFJYdhis0slBUYnJgfxu-dmYpMHcwKtZL6eMT362YRzp0LXHUzI9ysTzS5nJXINlwJPdDkUwNoFdL5uvEqNK6fE5H-UFUXifGGaR7jt5AYcPnYPhGinIBYt6BUc2iisItuRBFF-LwVu-8w4KJRIsVIZCyuSdduhvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9bd51248f.mp4?token=CqC5L3xp3aCj7VxrMAlXlhgnHdzdVpFJE5WgZtXUcEaeiYF7ZcQKsWRVN0hQyaN6yqHT1Dc0jvIzqhammpswISHDZ0W8vS29q4jegK-YkiEMatSKVfFaNoLBZiqVjCoOC0R3G6qe9FrUYir5VbXqxLnUjRhrdy98ERCJrMuFUQf-aQRLqJ_hBDFJYdhis0slBUYnJgfxu-dmYpMHcwKtZL6eMT362YRzp0LXHUzI9ysTzS5nJXINlwJPdDkUwNoFdL5uvEqNK6fE5H-UFUXifGGaR7jt5AYcPnYPhGinIBYt6BUc2iisItuRBFF-LwVu-8w4KJRIsVIZCyuSdduhvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپاد اوکراینی به یک ساختمان مسکونی در پرم، روسیه، تقریباً در ۱۶۰۰ کیلومتری قلمرو تحت کنترل اوکراین برخورد کرد و یک نفر را کشت و چهار نفر را زخمی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71270" target="_blank">📅 12:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71269">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71269" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71269" target="_blank">📅 12:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71268">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYxqJ4d0_3S2ArluG0R391CHx3B55S9ivZkoNUKmyri2fBz3fwOxny_4EQ6BfDbW8fFWpxFm7ztekEJ1wA_NRFfkv3nL2zCJLaGi66fRvQowiFXlGPzunmEUcBOQKhbVdYBYYJnCI80LCKO2D7E7cwWTyhGq2il-vZc6ckCAlRvvCsntK7m_0UHBRpPyujyGHJRa25TjucP8GujdVcZHdpRzr0tFQ7TUG-SRxRuqtt3YBbXd3bEWousE7TK_08EtuWqwm2jehB2L_gd8tqo7aqZqvPepvKMzzdp5iBN6s0DN5AAU2AmGbCrOGHZs3WahjRwVvqpApXXAbrZYbJLVtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شبِ بزرگ فوتبال اروپا فرا رسید!
⚽️
رئال مادرید
🆚
اینتر
⚽️
🎯
این نبرد حساس
چمپیونزلیگ
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📊
نگاهی به آمار ۲ تیم در ۵ تقابل اخیر:
⚽️
رئال مادرید: ۵ بازی ۵ برد و ۱۱ گل زده
⚽️
اینتر: ۵ بازی ۵ شکست و ۲ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71268" target="_blank">📅 12:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71267">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/193f66d1ff.mp4?token=LAmmXSGY_vd8Eqz2hEjJVTucKuOdVfIwmFH1AqiHYRHlWkX3FlBC3kC-bffNxJNqXvyEHUlgXjJ43JntQ5H0CVQ5FUZ_-qCgVCkegdtSVesLRLHGg22eCpPkTj-XYUl7IBr02S1d0WaVyp9jqjsnk5knG6hg2noJOP_HMw1YrNEDbbZxK3vIO2Ux1yc3kpr2miUFu98ugI8SyokCfnjMu9SYJ1nqbCqrRWOpDwxKF1LS5hbCI9WC1uiuMsjv7qnBGVxGLNJrZ9cYb8yIhfnGsqlnOVKX0qTnyD74z2JYmdh8f9RA6pIdPqo-TLTCuf-Wt9-5ISV0QHjHeEvL1lzHtoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/193f66d1ff.mp4?token=LAmmXSGY_vd8Eqz2hEjJVTucKuOdVfIwmFH1AqiHYRHlWkX3FlBC3kC-bffNxJNqXvyEHUlgXjJ43JntQ5H0CVQ5FUZ_-qCgVCkegdtSVesLRLHGg22eCpPkTj-XYUl7IBr02S1d0WaVyp9jqjsnk5knG6hg2noJOP_HMw1YrNEDbbZxK3vIO2Ux1yc3kpr2miUFu98ugI8SyokCfnjMu9SYJ1nqbCqrRWOpDwxKF1LS5hbCI9WC1uiuMsjv7qnBGVxGLNJrZ9cYb8yIhfnGsqlnOVKX0qTnyD74z2JYmdh8f9RA6pIdPqo-TLTCuf-Wt9-5ISV0QHjHeEvL1lzHtoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">〰️
حساب کاخ سفید در پلتفرم ایکس:
در روشن‌ترین روز و تاریک‌ترین شب، هیچ شرارتی از نگاه من در امان نخواهد ماند.
آن‌هایی که قدرت شر را می‌پرستند
از توان من برحذر باشند..نور فانوس سبز!
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71267" target="_blank">📅 12:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71265">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/658f8cd399.mp4?token=umaM_kLC7iz4hKAFSSqElG4v9fvYndn0VwF0D8uhPqPvCuSs4iGxRFdS_EcIry9j5biekU9lBqcf2uzWKqyZctDBpT0cIpJ-yaHzDBRmyVDDNXeP0EguFC1iLmNW8UJP-04gETW1z4uEyWgz9SQy2l1LQ9TN4tSLd0oerZS8pfcvt2TznbZO-ZB-so24yUHj38kH-ZUTdh12Yv0WBilsFMas74BRQW3dmK1cM7xGWVepV6slJrjcF589FgPYn5KzqoDqbTfymR63gF-uwaFqWnJ0vsd21uTpnomyrNoR5B1gnXzlsTNhGwSWDQZF_3W_MRfhmetb8vlEiEjnNZTLIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/658f8cd399.mp4?token=umaM_kLC7iz4hKAFSSqElG4v9fvYndn0VwF0D8uhPqPvCuSs4iGxRFdS_EcIry9j5biekU9lBqcf2uzWKqyZctDBpT0cIpJ-yaHzDBRmyVDDNXeP0EguFC1iLmNW8UJP-04gETW1z4uEyWgz9SQy2l1LQ9TN4tSLd0oerZS8pfcvt2TznbZO-ZB-so24yUHj38kH-ZUTdh12Yv0WBilsFMas74BRQW3dmK1cM7xGWVepV6slJrjcF589FgPYn5KzqoDqbTfymR63gF-uwaFqWnJ0vsd21uTpnomyrNoR5B1gnXzlsTNhGwSWDQZF_3W_MRfhmetb8vlEiEjnNZTLIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از یکی‌ از مراسم های تولد در بالاشهر تهران
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71265" target="_blank">📅 11:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71264">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c0de73320.mp4?token=buRtwz9Xb8yYuR6uEm1rxpLnmkRguTTcfm_wUZ2tkuoiC33a3ExDyw0igUwAp9hqcwIm2ezvxe734t-nZVodOHz-bA5abHO3-Dq2ueJJaQ_pdn7pz0QvcfHrvxuh1dX5uFRKNzpaBNKvup5o_1XBYbPWV3YgvEdMG1LCwgs-C7CRGS7-rM_CJMfWbtsHCB2jN7HnlXIKuwT-oJyU0e1BYBxcBpcbrI7Do9_kJ0GMFmX5gmP163FVTJCZftkuPxrmb1zfZ3ysoLDNU16AQN0g3j21fdhQbiJuTGJDxXwzulbBEM49Oh4WEg4NEltG315xBZIIq9r_XWnxc0dcGvZKvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c0de73320.mp4?token=buRtwz9Xb8yYuR6uEm1rxpLnmkRguTTcfm_wUZ2tkuoiC33a3ExDyw0igUwAp9hqcwIm2ezvxe734t-nZVodOHz-bA5abHO3-Dq2ueJJaQ_pdn7pz0QvcfHrvxuh1dX5uFRKNzpaBNKvup5o_1XBYbPWV3YgvEdMG1LCwgs-C7CRGS7-rM_CJMfWbtsHCB2jN7HnlXIKuwT-oJyU0e1BYBxcBpcbrI7Do9_kJ0GMFmX5gmP163FVTJCZftkuPxrmb1zfZ3ysoLDNU16AQN0g3j21fdhQbiJuTGJDxXwzulbBEM49Oh4WEg4NEltG315xBZIIq9r_XWnxc0dcGvZKvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
یک پهپاد اوکراینی در طول شب، بمب‌افکن تاکتیکی سو-۲۴ روسیه را در پایگاه هوایی ساکی در کریمه با موفقیت هدف قرار داد
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71264" target="_blank">📅 11:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71263">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/233fc1eb07.mp4?token=U0y_SVp7R-7BrGA00Y2euKRuzO3LUgRykRX07RhQei-ohSY8CqlUOcB-xMBZt8_j5d6NIiXw4-mnMES0zvqfM0JgaBeSJn6qP5fRpU51T8jm8NBQGT0NbT1xjXRdRxptV6wAxzo-Qy04i5oejk-nAwvxZ7uQjtYdGH_DATPk6L2qnVkFfpVJ01snFixmuooXTVbJbm05H1FNw52EgIJT-XCPghlbHDjWTse3bDOiU4Y2m0OVS4AS2R7Of7b_jIGTldOueJCzsz81R4kQesmC3bk3YOZMXZO02BP_ysWrCSMIrXy1XWWSYkIu23Nyvpi9ttzxBprkx1zRo8u93KSNQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/233fc1eb07.mp4?token=U0y_SVp7R-7BrGA00Y2euKRuzO3LUgRykRX07RhQei-ohSY8CqlUOcB-xMBZt8_j5d6NIiXw4-mnMES0zvqfM0JgaBeSJn6qP5fRpU51T8jm8NBQGT0NbT1xjXRdRxptV6wAxzo-Qy04i5oejk-nAwvxZ7uQjtYdGH_DATPk6L2qnVkFfpVJ01snFixmuooXTVbJbm05H1FNw52EgIJT-XCPghlbHDjWTse3bDOiU4Y2m0OVS4AS2R7Of7b_jIGTldOueJCzsz81R4kQesmC3bk3YOZMXZO02BP_ysWrCSMIrXy1XWWSYkIu23Nyvpi9ttzxBprkx1zRo8u93KSNQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تهران، بیت رهبری، ۹اسفند ساعت ۹:۴۰دقیقه صبح
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/71263" target="_blank">📅 10:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71262">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4221662e8f.mp4?token=uByImQROopPH4Vuhau8SVK3RyU--UnLNfgryHGJokYCqp0B91aUboBmR5i3S0NmLTpiNAJRyM3WOp3AHIJCjgZENsz3qwjTD5vz_znuJ57Ne9fh7ZMU33wiUvufSt-rbKokheisywfwlIc7p-UOWSQ9qrr2UAT597Qq5oOqZby0TogQUd9h-lTRQ48E9sUZx7qMaMWLc31DJZ6dPx_vFjb1rNAHdcgsZUvSKudvS7dveYRsHRTyjeXu7iBQdb3cETiEEPlOwn1NYiCP1SeplMaMzJYO7mbT4SfKK5g4ZBDq-Cyfycivz3iJ7SOjtPii9RoiXw34pkouiub62q5m-D6O_Wd7pbrIfAecf_cs79cwl0Z3KDxQZR4tl03-Lu_euOPIhrf9x_tAvo3kmACPZQ1QHcRjfxMQ1ghBqIoo39Ifn7XP4Onbxf9dy-_s4GwcRN1lC1FyS2xocrXZ0vIl6u3GXkh2214OpD3q2VoeZs52ZHvi07wjaskGUeQ6fLr_zmF_vI5Q0yNTI6hc62cHKLntoCRMtvmQptPqqMg0VnL-rFoZsXig2s2PyAxhtCU6B5W1zocfP3Il9QC0u2snLHzVYa3uquGcwkDvZoSKhmyZ5Tlbf-6fy-n0FowArJCFQZDzsm-pK5gWnwIEKH9haxGbid4QYPwCSQzhKeqOmVXM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4221662e8f.mp4?token=uByImQROopPH4Vuhau8SVK3RyU--UnLNfgryHGJokYCqp0B91aUboBmR5i3S0NmLTpiNAJRyM3WOp3AHIJCjgZENsz3qwjTD5vz_znuJ57Ne9fh7ZMU33wiUvufSt-rbKokheisywfwlIc7p-UOWSQ9qrr2UAT597Qq5oOqZby0TogQUd9h-lTRQ48E9sUZx7qMaMWLc31DJZ6dPx_vFjb1rNAHdcgsZUvSKudvS7dveYRsHRTyjeXu7iBQdb3cETiEEPlOwn1NYiCP1SeplMaMzJYO7mbT4SfKK5g4ZBDq-Cyfycivz3iJ7SOjtPii9RoiXw34pkouiub62q5m-D6O_Wd7pbrIfAecf_cs79cwl0Z3KDxQZR4tl03-Lu_euOPIhrf9x_tAvo3kmACPZQ1QHcRjfxMQ1ghBqIoo39Ifn7XP4Onbxf9dy-_s4GwcRN1lC1FyS2xocrXZ0vIl6u3GXkh2214OpD3q2VoeZs52ZHvi07wjaskGUeQ6fLr_zmF_vI5Q0yNTI6hc62cHKLntoCRMtvmQptPqqMg0VnL-rFoZsXig2s2PyAxhtCU6B5W1zocfP3Il9QC0u2snLHzVYa3uquGcwkDvZoSKhmyZ5Tlbf-6fy-n0FowArJCFQZDzsm-pK5gWnwIEKH9haxGbid4QYPwCSQzhKeqOmVXM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇭
🔞
وایرال شده از رقص و شادی سربازان ناو آبراهام لینکلن توی کلوب شبانه توی پاتایا تایلند
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71262" target="_blank">📅 10:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71261">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b860e39243.mp4?token=tcKmxo_NxF9z6EIsrNtFLJMUuBsY-dYXbMYlEINmVnFRQz9r0SjE1GZ7urnxmO7R5z831WeQiFqXIYbAyuK5TE2tRYn7SLhWXD-QfU3ApoAJB6E8JyCuyn5CRrrKh5EjpM-ILKw7MeYFKspqymHfJAV6i6KOUgHAEbHziof5JARdeYbU2YG_0MMoUkq3JIu9Q9c2F0YmrZa-0JlmxvH23W792kQPFTSljsEwiE4Dxk7ifgkbtAUUrpaUISN5l-VE8oYGXA0CRch6nXucX3ze7YjlWOmGdBwmTpStinf06jfW-FmNfYRTmmd5sLRs9s033x8_B_7VmH-FL5Cb8bLCDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b860e39243.mp4?token=tcKmxo_NxF9z6EIsrNtFLJMUuBsY-dYXbMYlEINmVnFRQz9r0SjE1GZ7urnxmO7R5z831WeQiFqXIYbAyuK5TE2tRYn7SLhWXD-QfU3ApoAJB6E8JyCuyn5CRrrKh5EjpM-ILKw7MeYFKspqymHfJAV6i6KOUgHAEbHziof5JARdeYbU2YG_0MMoUkq3JIu9Q9c2F0YmrZa-0JlmxvH23W792kQPFTSljsEwiE4Dxk7ifgkbtAUUrpaUISN5l-VE8oYGXA0CRch6nXucX3ze7YjlWOmGdBwmTpStinf06jfW-FmNfYRTmmd5sLRs9s033x8_B_7VmH-FL5Cb8bLCDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فیلم ترسناک منتشر شده از یه بیمارستان روان‌پزشکی و رفتار یه بیمار ساعت ۳ صبح بخاطر مصرف مواد مخدر شیشه، گل و...
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71261" target="_blank">📅 09:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71260">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84f97591b9.mp4?token=SUKgYjpjBMQBt89vs8sAK1BMaxwifi5F7Zy_E2MhhykAHeRSMLoKMpaC19ApuL0WrnYdNnIKetbADfTayMJWS-e-6i7YjDsha7pJbFC-52YOLxHLWTvOqfd4X8-ffo6nB-9Uj7kBFScf3UcpD7Pr0jp4jRIg4phhnbdMMD7yjL00FiEy-NFeZuQzLqLSTBKdbbXx2x_2D8JF4yHopk5nPhjXm8jMf3hFCEPVpghvO5CdgRPyxTq0rwGENmPOar9M3dvPENcExt2KQVG5FC8pNMehFbBgYGWqmqgSwC8dBC4Cz9sBHOwiu8GYaXXHdJNM-rTYAqDtsex4bkbYbbengQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84f97591b9.mp4?token=SUKgYjpjBMQBt89vs8sAK1BMaxwifi5F7Zy_E2MhhykAHeRSMLoKMpaC19ApuL0WrnYdNnIKetbADfTayMJWS-e-6i7YjDsha7pJbFC-52YOLxHLWTvOqfd4X8-ffo6nB-9Uj7kBFScf3UcpD7Pr0jp4jRIg4phhnbdMMD7yjL00FiEy-NFeZuQzLqLSTBKdbbXx2x_2D8JF4yHopk5nPhjXm8jMf3hFCEPVpghvO5CdgRPyxTq0rwGENmPOar9M3dvPENcExt2KQVG5FC8pNMehFbBgYGWqmqgSwC8dBC4Cz9sBHOwiu8GYaXXHdJNM-rTYAqDtsex4bkbYbbengQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⁉️
⭕️
گزارش‌هایی از تماس‌های ناشناس با ساکنان جنوب ایران؛
درخواست برای خودداری از حمایت از سپاه در درگیری‌های احتمالی آینده
بر اساس گزارش‌های منتشرشده، اخیرا تماس‌هایی از مبدأ نامشخص با شماری از ساکنان بومی جنوب ایران برقرار شده و از آنان خواسته شده در صورت وقوع درگیری‌های آینده از سپاه پاسداران حمایت نکنند.
گفته می‌شود این تماس‌ها با کد کشوری سوریه برقرار شده‌اند، اما هویت و وابستگی تماس‌گیرندگان تاکنون مشخص نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/71260" target="_blank">📅 09:01 · 17 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
