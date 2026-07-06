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
<img src="https://cdn4.telesco.pe/file/hFKH2Nz-yflLidgTchok_cRdkvEConDCDdA348uGclv2P_bDvnS8eFCYGuTsSk2_IstKp3pUbmROw0I2-pBMCc0Rn3bca8zZvorWuBJdoSfKhDlswVy-RHEUiBfMAGPaZqjieuo_AjvEM9leLphhZQTkcwtvsaxF_Q1qlQECoakTm2je77zzhG4eukLFIsA9xMnfBMZ9lirbbzYgdBRVnL2Mt73AzR-gL5ox_JcjD6I5y13h0xL-uvysOWaK2t4PqrQu-YUYN-OOhlRcJq2MEVq3kRzf4Op-Gx_eElwTkmQscNkHVh8qNPfOsFVBxwl75z-SBqfdJpp0WgtvMKFSjQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 407K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 11:41:22</div>
<hr>

<div class="tg-post" id="msg-25066">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I08cQio5M-iBdJoF4JL9dtg0XkzVbRFO2et6tlROxoOpHqmT5VYDS6Da1byy56JgWZ9GHY-9uQDGcuy2GZGyVyAcIHCCjnzp_7I_TkFEYPCrCQsgZWsNamVeWjXWhpdor29y8h2fmh_r3mpLurVFMygzzYXZl5zn2GSavDLI4EjnFn3I-llARjlvvMHX3GBIQtCAhXpveEq3IyqtMN8ulo4RbInDMw9IjcXXFuIr0ooSyS7pPDmoxLxkkXR727JxnwE8lj-1KB8pzifPhflmrpyRuLwiboz46RqsI5l4QqmSMZRBBVb9Nz1lWbIah_XhRey-gcsqvJTELf_MjIskjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛باشگاه‌استقلال برای جذب دانیال ایری پیشنهاد فروش عارف غلامی، محمدرضاآزادی + 30 میلیارد تومان به نساجی داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/persiana_Soccer/25066" target="_blank">📅 11:27 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25065">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBN0arrz6E9sFNwP1cMcNEgEEjIVbz8OAzV7zwiUzY9aw7rTTynruQugMMe_oUQNxl158YKIJKbhuzwPDmiv9TQXVgwbzly6F2cAfjRUymNw9XPiVURE4Agd8Nc-R0fdI0NHebIch_7MrC1QJTvnlg5nGvcyGA5oYEp4hyArNrVwqJCUmxF8S6tKq_nL7kR0wNSkOq6uiBHieVXZ5rNxpSb19cLl2SX3kPuMCWfdqnn7qZCAK0_mnOcGEPcMjqfQqGBohdkyXBoZFUjnYmR8kWh8O17yI1ckWzjq3HMuZbfHG1Y-_RD68ZkdexxKEdizzDqAUdZXMUZY5G7Pfw8bVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/25065" target="_blank">📅 11:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25064">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9398d6a28e.mp4?token=Uzg0lpx3IomAYZUwI5QpTkPH4yzMhZM4h4cWDFKor6k75lq3blQMevffpMn74k6-L7aVRXn5FEa9EmmEtjg9zbz_3YzrPUqMnJ7GrKBOmOW1410r5TPAr3kVPWpBMQqlmNvB9ADHSQV43Z2-zZ46jgsgO2IRoOrPHXkCva3ik_h2oG2JvQCjEIHGO0FNmCB-IPC1uVrsUGmT16x-FZsIU7rSHgxiT7OQHOo29zhS59pc_Mhk04ULLUHrKgY83gY4qHViDmlXt2DLwlC-Cme39xtwTeoEWngDVEs71UD2qcW8LNSfd0XvvO8YSgtxPY3MCttdSteP66oMyXkxf3QEiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9398d6a28e.mp4?token=Uzg0lpx3IomAYZUwI5QpTkPH4yzMhZM4h4cWDFKor6k75lq3blQMevffpMn74k6-L7aVRXn5FEa9EmmEtjg9zbz_3YzrPUqMnJ7GrKBOmOW1410r5TPAr3kVPWpBMQqlmNvB9ADHSQV43Z2-zZ46jgsgO2IRoOrPHXkCva3ik_h2oG2JvQCjEIHGO0FNmCB-IPC1uVrsUGmT16x-FZsIU7rSHgxiT7OQHOo29zhS59pc_Mhk04ULLUHrKgY83gY4qHViDmlXt2DLwlC-Cme39xtwTeoEWngDVEs71UD2qcW8LNSfd0XvvO8YSgtxPY3MCttdSteP66oMyXkxf3QEiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
هایلایتی از عملکرد علیرضا فعانی عزیز در بازی بامداد امروز انگلیس-مکزیک؛ چه کیفی داره خدایی یه‌مرد ایرانی‌ الاصل تو بالاترین سطح فوتبال جهان به‌این شکل میدرخشه. تنت سلامت علی آقای عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/persiana_Soccer/25064" target="_blank">📅 10:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25063">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2866a16ef2.mp4?token=g0PlDDOsACHm58ms_tJzY7o7dCuTvvsuXUiR6idHiYw7r2IZAYztH7H8Z1068l8uhGbW8syX64l8Ak1qInh2Mw4u2lEal59SkLSL06nbk5nEsCU71YU7CE9zr9IPxwNiq2hlRrF47vuzY0_jIP8kzf7AcCSWm3BikvIrC4aHOMUCepWB8javMb7IVThvLfp4nj194UTrI36WruFdN5SDbkmplIbLTbfWFLuW5JdwAvbSHVO8fdZdEoENPwcexXcLD8qZEeU-NNs_TvOkHWm8ie-6sk1esfdrrwRlQ8AziEzKEZ_pOjdLEgu-v9JihgqhBRbRuieguJYAjzubyM_b5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2866a16ef2.mp4?token=g0PlDDOsACHm58ms_tJzY7o7dCuTvvsuXUiR6idHiYw7r2IZAYztH7H8Z1068l8uhGbW8syX64l8Ak1qInh2Mw4u2lEal59SkLSL06nbk5nEsCU71YU7CE9zr9IPxwNiq2hlRrF47vuzY0_jIP8kzf7AcCSWm3BikvIrC4aHOMUCepWB8javMb7IVThvLfp4nj194UTrI36WruFdN5SDbkmplIbLTbfWFLuW5JdwAvbSHVO8fdZdEoENPwcexXcLD8qZEeU-NNs_TvOkHWm8ie-6sk1esfdrrwRlQ8AziEzKEZ_pOjdLEgu-v9JihgqhBRbRuieguJYAjzubyM_b5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌ های جالب دکتر انوشه از دلایل علاقه شدید بسیاری از مردان به فوتبال و مستطیل سبز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/25063" target="_blank">📅 10:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25062">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c09d93bfad.mp4?token=Edw1QaUCY8lbAYxR3B63Ybuj7JhUaBlFAl1wtJ5hQTt-zIIXwqCSl3r8evdeYKe1OmugK63IK1Fndt7KbElTT2UUq9wXJ8igJyox8EZhdr1y2FsypuBVSwASmVmNKHzBaHyOjPcJb53VO_KUpiSTm3ndSHnCl6ped0RGRzZw9uZsn2MMP-h40rMnE5H_3QIiagNKWaMMrsEalVjN5mx6Nt_ojTM3VLe--v9l3vTO0zfERtSRV_L5W4PNWWcNLGaIcEDPUgLGNJJcXJbkkBDBLyQcd7Fin-NdJXKztJphgG9vv_KFEyQUAKZHOWAKNqY0FCmDedhm_GfduIqW3xLF1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c09d93bfad.mp4?token=Edw1QaUCY8lbAYxR3B63Ybuj7JhUaBlFAl1wtJ5hQTt-zIIXwqCSl3r8evdeYKe1OmugK63IK1Fndt7KbElTT2UUq9wXJ8igJyox8EZhdr1y2FsypuBVSwASmVmNKHzBaHyOjPcJb53VO_KUpiSTm3ndSHnCl6ped0RGRzZw9uZsn2MMP-h40rMnE5H_3QIiagNKWaMMrsEalVjN5mx6Nt_ojTM3VLe--v9l3vTO0zfERtSRV_L5W4PNWWcNLGaIcEDPUgLGNJJcXJbkkBDBLyQcd7Fin-NdJXKztJphgG9vv_KFEyQUAKZHOWAKNqY0FCmDedhm_GfduIqW3xLF1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
حسادت عادل‌به‌حال‌خوب‌نروژی‌ها بعداز پیروزی ارزشمند و تاریخی‌مقابل برزیل و صعود به ¼ نهایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/25062" target="_blank">📅 10:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25061">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daac7485e4.mp4?token=Eecf9l21DtjdXd_xvsFMJENKhY9agVb0bqGaKINcPKoyflCk_LgoWOK8-x9Y4pvWRUfN_VVHi5jgpHMfP9WqCBzeVxE_MRjUeCHvp0fiBiQs17tgbArLyVr9bc-GdfdYD87qpd71CCpc3ks561VzmYHgPW19H720XxU5N4SKGTkpYMNS3d-FeLubJMhrp3LeMOqbB4GA946rySWqIQdsVEyi0OnEIWIbmoxSURyR8FzvyLu3Abbewr2XKOzHpIZ9H5gPr8wuFhqeqnBRURRXUvg7BXnsIJuCsqbrNg8zEOGgCW_a3Vv21bkyhO-13A1XHYnHm13wKB723OU5-iNkBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daac7485e4.mp4?token=Eecf9l21DtjdXd_xvsFMJENKhY9agVb0bqGaKINcPKoyflCk_LgoWOK8-x9Y4pvWRUfN_VVHi5jgpHMfP9WqCBzeVxE_MRjUeCHvp0fiBiQs17tgbArLyVr9bc-GdfdYD87qpd71CCpc3ks561VzmYHgPW19H720XxU5N4SKGTkpYMNS3d-FeLubJMhrp3LeMOqbB4GA946rySWqIQdsVEyi0OnEIWIbmoxSURyR8FzvyLu3Abbewr2XKOzHpIZ9H5gPr8wuFhqeqnBRURRXUvg7BXnsIJuCsqbrNg8zEOGgCW_a3Vv21bkyhO-13A1XHYnHm13wKB723OU5-iNkBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی از صحبت‌های جواد خیابانی دیگ رد داده میگه باید در پایان جام جهانی بستری شم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/persiana_Soccer/25061" target="_blank">📅 09:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25060">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🏆
ویدیویی جالب از نظر دختران خارجی درباره بازیکنان ایرانی و نمره دادن به قیافه ملی پوشان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/persiana_Soccer/25060" target="_blank">📅 09:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25059">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/529bb11b1c.mp4?token=krMQB2K0DgEjIL2SPhWv1vDO0iIqB1gZOP8mxSirX-NrX7lWKZE9F_xGHc0_7Hff22uVIscZfQfTF9EisQBIQlhyNAtL14ehYlAJEclUjx8QtWHUJ7Ln0zzMQ-jFnbDaNJamyVW8665orARY62KSNUwdvQgemkdR5VMsXuNQQC176ZoKL2__ajAgzRsUUArRQ-sQDSLGAWxMzdPxftLsp7QMkQDznrttLXTT-b0WChK8zD_KoFnEadi9BDZ1Y56VeEbhYMjJ83HJxH_cacSDx0nJEN9JT-_pOqqx6PosZbsx9NIYhmHx1ZoNtLuD8i4AN0dYNYshaG_lgKBOQWOxZzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/529bb11b1c.mp4?token=krMQB2K0DgEjIL2SPhWv1vDO0iIqB1gZOP8mxSirX-NrX7lWKZE9F_xGHc0_7Hff22uVIscZfQfTF9EisQBIQlhyNAtL14ehYlAJEclUjx8QtWHUJ7Ln0zzMQ-jFnbDaNJamyVW8665orARY62KSNUwdvQgemkdR5VMsXuNQQC176ZoKL2__ajAgzRsUUArRQ-sQDSLGAWxMzdPxftLsp7QMkQDznrttLXTT-b0WChK8zD_KoFnEadi9BDZ1Y56VeEbhYMjJ83HJxH_cacSDx0nJEN9JT-_pOqqx6PosZbsx9NIYhmHx1ZoNtLuD8i4AN0dYNYshaG_lgKBOQWOxZzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هری‌کین بنده‌خدا درپایان بازی با مکزیک صداش بالا نمیاد خبرنگاره‌جلوش رو گرفته میگه حرف بزن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/25059" target="_blank">📅 08:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25058">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjAB9PXHSx_6Thupg09MAoOI-ofld20LzkdKVkTjKcIGEOwpcNzH7KDahDDJLLgCPjbTPutB3c_0_uq6xZjGc1zkf6dymRhG99ASkyfpAdI3PI21Eouh9s5dNUq4zSFMCGTqnq_Sd6Zp_KAE_lyE9YqkDoJXvIEaJX_ftN5Axe2Hnu_qpNe9tpalJZAygxp3icHXIZGwml--B7sm7-yaCe0ciB9732Q08x_KI8wyub90hNC0rpOawiEWWdrJhTFEaS9zzXZQIpdJX4EgaAE_7_0jJM-2YeSK-Srf8Outo01_rJsZXUWxvEfT7Zc3tzcwlSbAv6YRo_LbS0alrEeEsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مرحله یک‌ هشتم نهایی جام جهانی 2026؛ پیروزی‌ارزشمند و البته نفسگیر سه شیرها مقابل مکزیک میزبان و صعود به ¼ نهایی رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/25058" target="_blank">📅 07:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25056">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GbkXn8gO4N1-6HfPLN6R7c3L2oX5lU_hr4eOY_Gr6MYFPKzaUSajulguxXYuAeUrxQR0SjWRrq-HiCXdsraCHiwxyrmhPwgCeBz2sjxS2ZKEvBaW0xQtG1DWh4HVe0AHhcEOLXeCp0OSkOgjEmjw14Z9L4TvBrStSl7fx9Ogw8qM_owD3SgZfVIZ8BS7BFi5zJfJoqGUJtDIs0gDMuxz7MwDb54mQfuOCMjyev7ME_psYT5h_n1LfxvhKrDso_pUy8vB6nHCJ2K7fiLU_mADtX_I9NVLMiRIUjJhJuInC6kGApaT8ouW0clIs5JrpV8RgFE-wXdrp031yBSGnp_Byw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qQNVTBRZjx2aLBg6J3ES6PRE7oJMQ4lgSwUHuE-L-wbft3cAEi_5w91pq96TpqqjITW7XJUl0nqWEDTfo1_JbpE-qBs-em3Bw8SOqVa3tGAK2t5dP4T5pRaZLg7P2soaoqQHqgrZrb-5Luz7bHs-71cSTvr_DwMAeah_04j3ELAJ9WSx1L2igxrdcJV5uuV7R4liP8oryu9i3tpbbK0ok0iMlaPR4SCzf7wGLwbyDLI5w9xBPLk_YeU6gOggvpeo43xuJ0MyYcAmd94tjgbygLHsy9Rq4GShSViZY8nXZSy7XsoYc2-iPBU0oJw4qXlR_I5XOHifI2XOxDkngEu3Nw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌هشتم‌ نهایی‌ جام‌جهانی؛ شماتیک ترکیب دو تیم ملی انگلیس
🆚
مکزیک؛ ساعت 03:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/25056" target="_blank">📅 07:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25055">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ezbF-wfGTizc4k_nRacRBGv9vO28_em2XoIf65I3HwGAjD2uu2fB5V_xd3PhH8LkXbjP0HnnT5c0v_sJuxKBxDUfvIyhcCpIc85U4cJxplo95VDgHs-EAoBNJf8MLZ-Aupfm0MB0mDNrMmOB3m9EEUceMejj4N7uYFmlDlYC-3-wXd4GsoRaQ48Qy5KzgBdBca9OWrHwJBsYmLZsa_jGUZi5J7A8sqw-AFJ_wM35EkVuH06r-e4KZwb9aLIyAtYGTP0Jyp4_0QNmlUa8gAS7wRKyjKyoGtjHPnyI-UmY5y1Q7RoIJIPbW0SQK3swFJ7EQ1KgxzrUwI3-WVo9o1yLiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌ نهایی‌ جام‌جهانی؛ شماتیک ترکیب دو تیم ملی انگلیس
🆚
مکزیک؛ ساعت 03:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/25055" target="_blank">📅 02:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25053">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XjCwyTkNznSDKuARCjAVaMLHtytHwA8wpS7fdwamWGiKGhMZsEcI36RPk1TCGNBX9YHKzZwHa0V73wYQN4wtJ9hJw6O0ZHcJ5TmKvN2uNWFNC6fk9LmUoHxWao4wOIHBqBMSEZBE6XPBMtAdvB4kN_4oaZBzoqgW8cE1yuXCcpxraNzcw-3afm3He8iykXf7hzABF_nY0XkJV4c7C9xu2qsIskQG8gedEtL1qk-RrG447oqfFVBUeVlgwyi5KOCJoPRZrdQYVw6Iyccto2r-SJsVTC3287-fBzgV7fLIbEU5uLlTQOQYxBXb9sYSEVdsUjdqMK1CD0vzZIev1cykNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OyifKWL6E2h6VxfCUKDOz7cu0hdxzQWy4TrM4_tToZM3rOe-zaIU53BVfvhDfgSK8yiLyLVSZKCdhFhRtUQ_lCOxi7ZhugvgdDMTHjvtjbgrhgypOI75f0JC9VreRdtAucmBG5oGAmsHerfKQStYHIwQKPjqT0HZKKqZKm0GFuKnhB0Cai4XFo3dMrgLrDp3b-QrUFtdSdjp_jJdeV3I_wJhQoWvkcXGKXZYuL7AY3pxHVvtPQxSdniWAowskuUOFR2hZgfAGGr10LwhoqIqPU0OuRn_f7MrpmeP7ZtFEHNc2TNdJ7V0Ekmrzqs0dCT0y3ulbij8HbnamgC8Kt1dzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛ از نبرد خانگی مکزیکی‌ها مقابل انگلیس باقضاوت علیرضا فغانی تا جدال فوق‌ العاده حساس و تماشایی یاران رونالدو برابر اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/25053" target="_blank">📅 02:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25050">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOwRadaQs68PdMnpznZ15xL3h-pLRQ77UUX84UcUNBC1CaI2Xpk7wwKgvatjIg3Kb72M_aZsVIEaRu6xgrysPxVDUol5wC0dItSsL7oRArEXfepThNIlTm7J7CuqmLdV15PnKrLULhkceuBWNuoIlWCN6Oelc5qtL-291dzKASCybkuSq5-me2fB0x4MyhuBju856-lGvF23hHx2ipVqrHBPU9v5KRKZ9W_frW0jUslkw_PtyW4QxulsCshtjO1t3zW8GqHUVZg0R668zNsK6FWix-gLNcpPKlBNypqWmwiLkQMDjy5O8DLB2EDG-YmpnKQJtwQbBvPvSG70zx-mRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باز هم ناکامی تیم ملی برزیل در مرحله حذفی جام جهانی؛ حذف سلسائو در مرحله حذفی شش دوره اخیر جام جهانی این بار با کارلو آنجلوتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/25050" target="_blank">📅 02:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25049">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6DJnk2gxAVJTJQNMR2PuRzvMRt78mE6270QkWDnMz7meJobUlH4d5biC0UpUv8yk6LsuYhFkOuyForfWTazGkDH_gn-52yiNq-07p82Qaw4d_c6AN23OdYOHhwW3laNxukTMRDFf4d8QsJVz195le2s0nQYqrWZTHQ_hPrkbNQ40KvbxcFI6gTjwviU5npkOT7fsFmkMN191IIMQ9SY7E7Afp7aUEfG0pZxbQ4DxgWqKE5fl1z8Avpa464Z_NTc52vzcSg6CrS1DqbV45crM1rzwVt0YkX5hgCEuV_TLf8Mj4Q76XmQQ-DAu8OojzKbx14Z7lOl7-AoJJt47q3pUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای تقویت خط هافبک خود؛ احمد نوراللهی و محمد قربانی 23 ساله و ملی پوش رو رها کرد و قراردادی 2 ساله با پوریا پورعلی هافبک دفاعی30ساله‌ سابق گل گهر و تراکتور بست. پورعلی درتراکتورِ اسکوچیچ کامل‌نیمکت‌نشین بود.. پوریا پورعلی جانشین میلاد سرلک…</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/25049" target="_blank">📅 01:55 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25047">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBasClq6XbwDz4j6oOT13lPl59dnCup1AyBtryA4YZ42TqUefvfJfzacvBEAxQx-NIYldaMuByh8aImxiXPjGmhdSS1Za9idWkNqdnZOlkML9_IElA_ebVdJesCBQfhkBxIUX07JK7C1wJdQi97s9SDUWU2Y-xxW8tlOvn0ujW5DAcZ3HX6dlco4lMEW6y2-G-iAltDRe_WQz5XSicYffgw5_lg0NZ8zT4u0BPZKQYyTg1HiDVqm0vMPQyBHKcVTxBYVzS-0BXygOdRaPijDQAZF0jb4zY3glSZQ2z_TCJGqWCSvU9ltgCNNBOzJ3twa9e9aRltnOYYvt06xRc5X2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛
از نبرد خانگی مکزیکی‌ها مقابل انگلیس باقضاوت علیرضا فغانی تا جدال فوق‌ العاده حساس و تماشایی یاران رونالدو برابر اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/25047" target="_blank">📅 01:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25046">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EOuiX5F357n09IGptZGznhOlwtcTyU9XETNJOnOLF0Cc5P4OAThgoRntoQ50TmtgvcdX2qBLAkmcVeIL4AkWUFGR14V4TfmRZaNIHYWLh2FnOdffzw9KwZguZt4podeKWx3r60TzXdwWWewSo2Z6cvfc6AA1LKQBya9cpW2QYqauFdzWFeq_gBnXF2_kigZ_P4WDBRXXH6aq0DG6E8XLFrjeUEnwWyd0p8-QVjkdWEor9eF4Ave3jD8lgrpqLJRv_i6TWYjDYrdRwz48yMXk4oWdeDYgQHuNWCsVDoV0TGlFcY_IxUTBkpHILTHLqHFbICvLUVr2StJ73RgEogcj7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
صعود فرانسه و نروژ با درخشش‌ادامه‌دارامباپه و هالند و طلسم‌ادامه‌دار تیم برزیل مقابل‌تیم‌های‌اروپایی در دورحذفی جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/25046" target="_blank">📅 01:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25045">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLR3ZTR5S8AwUu7iOb0WNf2n_t1s8c_Q_xs0qLBGuDvWg1JmrFRdadYmMWqY53WVGDqSkdXsDncgw3GIZXcOHYMOmLGIdznt4yt7ePIaJk0ox7PtDhhgZus5D5TTjj_gyPnrUfMYMEDQy2R6NXvHozTvJEvl35EQN9QaFbdDEcqG1ShqpQRmbru4JqzoY9TE2aH8wh1eMDCR2XiUBOJWJhXnfHVGWDt3LfIt3TXF2RDnnlDw2XipfnXYcvhFl0HEEUeaPUND2WAO5toCuvmubie9zkuNnR4He0epHV-YP164ctwtcy17RZDD5WHrq5XSMiBOML4QgOm030WA6vasxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی2026؛حذف شاگردان کارلتو از جام جهانی با امضای هالند؛ دو موقعیت دو گل؛ هالند یه تنه نروژی‌ها رو به مرحله بعدی برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/25045" target="_blank">📅 01:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25044">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇳🇴
خوشحالی هواداران تیم ملی نروژ از صعود این تیم به یک‌چهارم نهایی جام؛ نروژ به مصاف برنده مسابقه دو تیم انگلیس - مکزیک میره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/25044" target="_blank">📅 01:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25043">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6zB4CHwvHSeNbj1GHugnGlPjeSVJVtNiejdrSfxGx_rsduzPSKcbNn5beSX62kYxBUv7g3TbVwO6N9BdaF_SBgOmtaawEKM3XQ3cehlI0OoWf9S6sYoz0LWui8o3BRcLKy3HY89V154hcm6Tq0vpsa3n0S1wsrLO2_lbph_XC4vlKO05fWSEIOnAAGafi_mqobpgUzrhvyjV4AyleSY8dbgEOQM8SdISmfnxEivSDz-oflmS7XcpJ-sGabkVmiK2lNxpHka7mh33uWeqMNiqdjEgrMWNFCOGycQy-r2ELS-Wo8v8XnAyy7TT8wJkADFvq2g2rYRouywzFWPhKhyaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی2026؛حذف شاگردان کارلتو از جام جهانی با امضای هالند؛ دو موقعیت دو گل؛ هالند یه تنه نروژی‌ها رو به مرحله بعدی برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/25043" target="_blank">📅 01:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25042">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2de979c355.mp4?token=dQI154Ao-2t2uP0abTAHUj7tXGIUsWr_ZBqCbIc7I2DI8Wlmb1mpqKaAOUIb661ydz8eD8kVEoQIJFWoiHVE4OvMyCDYGJnJHc1rdvYvbrKjhga7RRNJPaObs3b_P8GyCURxf2utyD3XpwuYI_hYjHnJWv5E5uurKgqrnBT-NtNA_1DQRlfdBkq91SPGjxgegd_lXch1Lap_VAkPb7EaaDA9jCWAngUMk6aMiTjM1IMh0PBYKXtYIHgCmhIez_GgogY8EmTeBLtdBPV-IP44osW8uZjKqcBWIzQZJUMaYTnGQAPtCXABS42klkSMeWwhiCTNNZopMeYGX-EAbeJeeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2de979c355.mp4?token=dQI154Ao-2t2uP0abTAHUj7tXGIUsWr_ZBqCbIc7I2DI8Wlmb1mpqKaAOUIb661ydz8eD8kVEoQIJFWoiHVE4OvMyCDYGJnJHc1rdvYvbrKjhga7RRNJPaObs3b_P8GyCURxf2utyD3XpwuYI_hYjHnJWv5E5uurKgqrnBT-NtNA_1DQRlfdBkq91SPGjxgegd_lXch1Lap_VAkPb7EaaDA9jCWAngUMk6aMiTjM1IMh0PBYKXtYIHgCmhIez_GgogY8EmTeBLtdBPV-IP44osW8uZjKqcBWIzQZJUMaYTnGQAPtCXABS42klkSMeWwhiCTNNZopMeYGX-EAbeJeeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی جام جهانی 2026؛ شماتیک ترکیب دوتیم‌ملی‌‌برزیل
🆚
نروژ؛ ساعت 23:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/25042" target="_blank">📅 01:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25041">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae7cbb0612.mp4?token=ReWfvu945k0EcrKuNAb_RxpLxjSOhZ8-dMNGfQFaQsKohZmZjbPIvUOsK5-8cY1HqVrkHa9jlBnYPZWGskUSWGO9X7FF1lio49IM0hlp7q62gybbpQhwstlWIC-bSB1-GJxeoi0ZMc5Q7CkEDbrFM3QiYdFiJyzok_RTKzQlSUgwcESSqwcPmrBn5VDhLaEGwBYpcLz9-vJfC5Zy4WeJ44YigryGPzKNYj6gAy_FfJm6_I222mE9BuzqPSbbgivrltJWrR2GMWUdEBOwb7wf1nDpyEIM7ADnRMZbqAYf0I7__PRKnQjhwN4g-r8vtle47FeKmCk3jub0s5tACbaezg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae7cbb0612.mp4?token=ReWfvu945k0EcrKuNAb_RxpLxjSOhZ8-dMNGfQFaQsKohZmZjbPIvUOsK5-8cY1HqVrkHa9jlBnYPZWGskUSWGO9X7FF1lio49IM0hlp7q62gybbpQhwstlWIC-bSB1-GJxeoi0ZMc5Q7CkEDbrFM3QiYdFiJyzok_RTKzQlSUgwcESSqwcPmrBn5VDhLaEGwBYpcLz9-vJfC5Zy4WeJ44YigryGPzKNYj6gAy_FfJm6_I222mE9BuzqPSbbgivrltJWrR2GMWUdEBOwb7wf1nDpyEIM7ADnRMZbqAYf0I7__PRKnQjhwN4g-r8vtle47FeKmCk3jub0s5tACbaezg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
تشکر دونالد ترامپ رئیس جمهور آمریکا از فیفا برای بخشش‌کارت‌قرمز بالوگان‌مهاجم‌تیم ملی آمریکا. بالوگان حالا می‌تواند مقابل بلژیک به میدان برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/25041" target="_blank">📅 01:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25040">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8897e8ba1a.mp4?token=tAVKVAEDXOtOZ891S1ZkQSLfR6OHy_fFVjy3d_Fq57U-6aUXeO2DZ4lWLWubEk6TMJ8MWWKqgICUtQs3spWjoFoWSfAWImNfS2-mPtlRPU0QfEScRKGb0KzRRVfPpIxehi9QW-ktW9WwxwknmDbSi5Q4GGv658lVYuNDYvdKBTDkw128b_ic5fL_H8Z5GIjb8PvRElobfwP30ExrRRJjfUnTz9Zo_76l7-Fiv72oR5s9BIRC2rzC74mUI2gnSNC40ex9aIN3M3U8n9m1imiYQ19B2kSB5rvMJtzE1meTiBEnLbdP-enhmfNvt2-Q45_1tYYBkSn0DuQox-Kzogx59g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8897e8ba1a.mp4?token=tAVKVAEDXOtOZ891S1ZkQSLfR6OHy_fFVjy3d_Fq57U-6aUXeO2DZ4lWLWubEk6TMJ8MWWKqgICUtQs3spWjoFoWSfAWImNfS2-mPtlRPU0QfEScRKGb0KzRRVfPpIxehi9QW-ktW9WwxwknmDbSi5Q4GGv658lVYuNDYvdKBTDkw128b_ic5fL_H8Z5GIjb8PvRElobfwP30ExrRRJjfUnTz9Zo_76l7-Fiv72oR5s9BIRC2rzC74mUI2gnSNC40ex9aIN3M3U8n9m1imiYQ19B2kSB5rvMJtzE1meTiBEnLbdP-enhmfNvt2-Q45_1tYYBkSn0DuQox-Kzogx59g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
کریستیانو رونالدو:
خدا کنه آخرین جام جهانیم نباشه، تا شماها بتونید بیشتر منو اذیت کنید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/25040" target="_blank">📅 00:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25039">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bN2QZDCldUxwwAKczOVMGN3hHuzqSlVb-47SmgHKws3yktCcWRmEXUrIOhZkarsiPk0C90IFdaulaMMwsieB9HmBc-iwuGI-g4bz0TF6JBJxGR5RcPljpC7nPsv8dl7vApXmN1OP7l1-fvmkHn9sKS8rycsUULFqYN8htKJhb3pWp3krxr8JBE2klbHzcDPgLNSUyjk5Emk2lZWyCtj3tX6OqyX7qD1ZAlaAYgUjT9q6vXNixm4GanXax9Rb491Dj2YxZiH8h_AXJEkAQtwJLeW20UjoRZ0VqFKa82jdmRSkpXd1B-lCOR7SEfh3flld6zMHMoJIEHgEg80U0hDYEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇳🇴
پدر ارلینگ‌هالند ستاره‌نروژی منچسترسیتی:
شاید روزی در آینده نچندان دور هالند رو در تیم رئال ببینیم. ممکن است اتفاقات هیجان انگیزی رخ بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/25039" target="_blank">📅 00:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25038">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_HbwJa9FJJd43b-bucxF6WymmUDlDSfNco6k-TlCYknOk5YuCtLkWYCqjkXYtTr1E2SDURlFaa1tdf6rFEIh5jPb4kL087VJJsTEWFPDOga0KsuvBEWlfqr4bMUricS0lhK09L3WO5D1AmZZpHQG_eoMC01jehnoJcuFyINhysNCReJ36z9SFYlkvJIS9D9lJS-b9BnjWLhsLsEtPtxzIhSDcXbRotpp9Nsp-RTMtOcScxDuZAQlsDKS1EbLsDk2HANdky0LqjKjyYxPqSAi5-2016NcsDIFzjv7EM56nUlpfbi4OX--iZKHjQgWG0l92aGUKzAHiQT0ruCYmovfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ کارلوس کی‌ روش در بخش دیگه‌ ای که از مصاحبه‌ اش به تعریف و تمجید از مردم ایران پرداخته و گفته من حدود 12 سال اونجا بودم. اگه روزی ازباشگاه‌های‌ایران‌پیشنهاد رسمی‌ دریافت‌ کنم ممکن است به‌آن‌پاسخ‌مثبت بدهم. من برنامه‌ای برای بازنشستگی ندارم و علاقه…</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/25038" target="_blank">📅 23:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25037">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhGuJltbDnlKiRqVBguHR60V4g5lbYYnEyTH3KvoiqLW3rrPQ0zkv90C-1TVpeg1Em5EokdHWo-IiMe97gzlidrA8It4u0ftfoxpX70c5tmIOQi7C6AH9rHOmxHiPDpRQpdbA3FsKNNHl33rFu7TX49OeinW6yIzUchfFyATzaNXNT-Euxev9eANYovRFsZALLWNLbt5oIaytKElrOPo-wXNAj-qlzHLLnxk1Rh7sFU4UEoKu53umOw4P2B7nYuQqchMHGcdeDYUj_wxVSseZXu8_NnkO89_QCNAlogP4lRS1paHAK7qVsJjyYMs2F6oKlrImPTk3Ns6KoGibhGb1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باحذف تیم‌ملی‌غنا از جام‌جهانی؛ به احتمال زیاد کارلوس کی‌روش به زودی قراردادش رو با فدراسیون فوتبال این کشور فسخ خواهد کرد و جدا میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/25037" target="_blank">📅 23:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25036">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81c1096e89.mp4?token=csQvaxO3mwPUWmNP6yaDUhGgiAX4oZMZ_-flNZPfCKBFkJUVC_gB0QpZEp2JcXEqXPKUBOMh6VuQDJeQFafOuCWEwzTaXyjolPwEpaV3FXeaJ7JfzwKNzncqLhaT9gGGoT3n-e15bahmyo4g1_TqLSf-RItGDIdGx1cF0zdtFG1mDgnjAEQDUnjPs7CDyal00yRVpHar_UujW4dEpX_ugi9D3nPuoub4qeFiTND_UiMh_Omjcs4Y4AMufRml1IGVmkVToBrJF1LT-uKWuV4qVHXhcciFbJ3YqsKoIbii4STbZW3-D2rD_q6OvcoWkHab4ZlmRySIyz17FmPc2wjuk21u1gskEiJw5POCoMDjcmPGgS6OR5QVNP0zyHQ6V51MJ0KzJzOINUTSiMAQoIRDJ3r9GE2u91juvge0E4zawHQjFC9FKPg4qWvlPYs2vcTu9-p-5m15mjh_9V7J4gd5g2-nGPZwuGva8jS4UKtwufIhcQQ88xX5xIl1CJZ2PHPDDYIueOm4m_DCmIleG2ROAn5QfvkYyQbu7SHwFCjOcHgZLaqt6sHnL1zeXB7YiebLMmFz0yU9-C0Fdo079krTp5mkWHBsuOlHhmFp1-YAfXrg9sciSUl-loj1pFhnnagpdRqD6-A9AI2bzHMj-UTGkFMDDAmc0gE8h0rBXmicJY0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81c1096e89.mp4?token=csQvaxO3mwPUWmNP6yaDUhGgiAX4oZMZ_-flNZPfCKBFkJUVC_gB0QpZEp2JcXEqXPKUBOMh6VuQDJeQFafOuCWEwzTaXyjolPwEpaV3FXeaJ7JfzwKNzncqLhaT9gGGoT3n-e15bahmyo4g1_TqLSf-RItGDIdGx1cF0zdtFG1mDgnjAEQDUnjPs7CDyal00yRVpHar_UujW4dEpX_ugi9D3nPuoub4qeFiTND_UiMh_Omjcs4Y4AMufRml1IGVmkVToBrJF1LT-uKWuV4qVHXhcciFbJ3YqsKoIbii4STbZW3-D2rD_q6OvcoWkHab4ZlmRySIyz17FmPc2wjuk21u1gskEiJw5POCoMDjcmPGgS6OR5QVNP0zyHQ6V51MJ0KzJzOINUTSiMAQoIRDJ3r9GE2u91juvge0E4zawHQjFC9FKPg4qWvlPYs2vcTu9-p-5m15mjh_9V7J4gd5g2-nGPZwuGva8jS4UKtwufIhcQQ88xX5xIl1CJZ2PHPDDYIueOm4m_DCmIleG2ROAn5QfvkYyQbu7SHwFCjOcHgZLaqt6sHnL1zeXB7YiebLMmFz0yU9-C0Fdo079krTp5mkWHBsuOlHhmFp1-YAfXrg9sciSUl-loj1pFhnnagpdRqD6-A9AI2bzHMj-UTGkFMDDAmc0gE8h0rBXmicJY0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
درگیری‌رونالدو بامارسلوبچلرخبرنگار برزیلی در کنفرانس مطبوعاتی پیشاز بازی پرتغال-اسپانیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/25036" target="_blank">📅 23:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25034">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HA8L81sqfbmybkjVanP5hcAKaJjkuR5FLzpuMsIHAxlHZ_tOG8IAkCl36EEFCuVMjeNR8gWovxpsTpesiIO5MC05nxztYYpWv0oiuzXJ04QbSqks-5wdrgLysPUZOwcVFLXnh8JZ7ZLucMp8dZSo_MQGrlh6Gw8n3NBF_2LSg69ucGnDrr2gGgaipEUJWOwEqRtc09E5HSvm5W2rITd0OqKfHBppnUEvtm7NMINzVmy6Rq8t0LEeX9B7ERCkQKa7RyzkArqQtSNUENFEH5Y6xj31bUL_QBj1ZECoH2EhG2f9DX0GgBviSBorT1ZKkROb54vZYF5nVq7efTmM1eNu7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ علی نعمتی مدافع‌ ملی‌پوش سابق باشگاه فولاد برای عقد قراردادی دوساله‌باپرسپولیس خواستار دریافت مبلغ سالانه 75 میلیاردتومان‌‌شده‌است. درصورتی‌که بانک شهر با این رقم موافقت کند به زودی پوستر رونمایی از مدافع جدید سرخ‌ها…</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/25034" target="_blank">📅 22:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25033">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHHcjTpDYzkXUslbWD4YCSalGrGAxziDGRga0lxLvGUzCbdbX4wdo5SCYI_d6eFcWk9qmZv5a0x3Kptr-lNNU8IHjJ0iEZySaVkE7s4ocOgrxkmHuzJt4xFPpShAumrlRVlAVyUmVEFE2ziGh6VZVXKvmPO135qkCcghvP95FkDgA8QM0MpmU7xBasPKJCxcuJ3MQDmPkUM0dDi8JAVm4Lytls-vV8Lft0BYt-Cx75n7cyJ31XqdsY-xHrFRACf6XWYpIRaSQCSUcjD0iO4BF6sp4wT0ZBOxAfGUncKa2WfgV1gb6n6tYg8UC1hDrVvS9HdLF-GzWotkpUztEL48hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی جام جهانی 2026؛ شماتیک ترکیب دوتیم‌ملی‌‌برزیل
🆚
نروژ؛ ساعت 23:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/25033" target="_blank">📅 22:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25032">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UB4OS9oYQ_TBSardgNxr6uQwd4Kbis2-n9LU8LsClg70zaFsy2CAZUClBsjOrG8Fhg3MDXkMjDCGUgqXBrVJkAMzqJbxksJg9ZhEm0oek7l0clo2yVyTFY1fFwPM6B9mw3Iq3JDMGCXV8Ju7PKC95ZysSld049uMYo24TyO05IE8eWMMfbQCroERiAmZhaP7RHsuMahXQJOAblpfhCqwSNgoDRCoSRYxRVBvMCYJW2iaKAV9l5I2xgLgKMErkGlNcJ8-Z0TLYIxot1AE2GJUdBwiJmjNGa8DEg5klXBPTUG3P_wnV0WCbVpkkwml3BuELKAuHixwCd69xpQB00pOcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
🔥
بلاخره انتظار ها به سر رسید
🚨
👤
نود جورجینا همسر کریس لو رفت
🔥
👇
🚨
👈
گزاشتم تو لینک زیر بگا نریم
👇
https://t.me/+wYDPG2ky70AwODU0</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/25032" target="_blank">📅 22:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25031">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nEpDbp5tjNEdTMe2rBPV-pqpo6n9xJv3YyQT2tg0sKBUIq3pbaWcEP5mvtsaIcpEaoCihA0zGfKIllTEMD11NgOIEtsyTFOlsn6V0LfjEpG896gBB2EnSrSAV3fsDXz9DJSfndF9MRQaubtr_r595Y_b9bwFuHQdo5ZC6azj7_FtThCD_CnxsCmUodFmKdjUnhLE52_xaUp8P8b4h2gzdy_3fOM-hAXXgngNQyREMjz3VkS6_4iayS444sk2d-PzXWs33pDtJkq623RhSHXesaLTORNoEdB5Ujy8HhyNjiB8YL7VXS_QMUU4t_nv7x8eb1MM6PWkOTcA3dQQgIQVRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای تقویت خط هافبک خود؛ احمد نوراللهی و محمد قربانی 23 ساله و ملی پوش رو رها کرد و قراردادی 2 ساله با پوریا پورعلی هافبک دفاعی30ساله‌ سابق گل گهر و تراکتور بست. پورعلی درتراکتورِ اسکوچیچ کامل‌نیمکت‌نشین بود.. پوریا پورعلی جانشین میلاد سرلک…</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/25031" target="_blank">📅 22:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25030">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDr2qSqbZ3yhciZGS9DicjioVS_5gSwy2nNqQNhL6J5QubOvJtdBnivAv4qA81fVjd1BIINgovDtOBlw8n7Asg6GkJFLEcngUh96odGSg7C0ZCHhDMvpviA-KeopLdrWDiDPQAARwrI2UabDmLooEHZ2LvD70qfDi2i-LlGudGf4r1Nb7CmDKb5gN4A27WCNrmCZNZ7lfxS0W2Vwuuh6FQoEUH6Baq5-z5SB9_X8O8n0r_gisqiOFyaptkmflYLlx6TCYbi6YU-EIZNsd51H2HojbNIrUtEf2GsuPUPZcjEbCUbd14Xh2LyviNO14zmV9qHfqaKnkxgWcL58qCNnFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#اختصاصی_پرشیانا #فوری؛دراگان اسکوچیچ سرمربی‌سابق‌تیم‌تراکتور و نماینده رسمی‌اش از شب گذشته بایک‌باشگاه‌لیگ‌برتری در حال انجام مذاکرات نهایی است و به‌احتمال بسیار زیاد فصل جدید او رو درلیگ‌برترایران خواهیم‌دید. مقصد جدید اسکوچیچ فوتبال ایران رو سورپرایز…</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/25030" target="_blank">📅 22:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25028">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uQiXVQp-dAdY-cseqgXdrJirXhOsw2rL0o2XKN3qaUvcb0QxWz1kpvJ7kNWWZyzvoJ1JRKD03ai-Um-ow_A9bvMEjvsgSfFu3meBppUdWlNnj_u60zkLW2nhnB-bAikPk-1PHrftX7rfqJh69Co8SB3aULcsxjfbXWtLKNgrEw51ZqwUQ09TvEIfY7wqZEMh0n2iZ9MnuvZfqhxE3bckTK4KR96AFfDN1UGEuYRJcJx8s9SrSlEnPmEQD5oedRstk_b3RiSau4idN_AdknsaYSkelhcyFdm43zvP4JcpWhYmim7Cq_NdnOeuLPg8POKHssDUVJpic_yfzfkeI4suCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ALTWGg1Sg-37orXPTRTw-MK5HlDvxWxFqhoq5DVnkLOH-D1RA59hxheE7q1xb0TGhxhz-_xYTPjer1_HKtdvdt1Jnhj-XH5GV0dGiI39OSrRpiOdhKA483_F2lxvreZpvZjHQ51PUs2hYnA5tSgRGqzRkRNTKEXdxRb9TU5JNkHHjEKgdhy_NPPHThnghJMPSGqUbId0QYxXNROWg_pSf_vDp5l2Ztd3Z11XNqxW4CNhRERWomt9k_ee2GM7i5ZCweF-97mVoS-uZ2D1hQojxPaY5n-0bLi9mPFYTvrWSid1np6pRYpYkKhEw4u8Oxl94qnpVk6GrWdjICRBNogdEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی جام جهانی
2026
؛ شماتیک ترکیب دوتیم‌ملی‌‌برزیل
🆚
نروژ؛ ساعت 23:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/25028" target="_blank">📅 22:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25027">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WWbGRXdQNz_gWibiAp3oK4cAzfo_MU3vTyqxbD8S4Zkekg9YDWUdcTOigkN3-oYCXVamOgk8pou0O93EanwZmU0RiOcQ5nupcHWp3sOMGA3G3h6mc2cBwluTkf1omxi__UDt6sjNG6MWOj1D6seNIwiRe-oHilO57VH0qfWKr68O-y_LNLlkbfH4_0lWOHd2XiU_WECPUyW4AogpbLOGCvWSPpWsuwUpbeUwQ2AsmQXTFJl7bPVwiQOgiTHcHTc_spLyxcUJ-HG0OEOIqa9nzYcXrqckHMqP33yLyHBRtOZQuqoZ8nU-XxtWXj_EhVAiZTBNXBvYpcJbZaLNzzkgpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
تشکر دونالد ترامپ رئیس جمهور آمریکا از فیفا برای بخشش‌کارت‌قرمز بالوگان‌مهاجم‌تیم ملی آمریکا. بالوگان حالا می‌تواند مقابل بلژیک به میدان برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/25027" target="_blank">📅 21:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25026">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ni4EqpumGxf_4WO6DHWETIWTXl-ixxMIHWbfh9K5yIzopLRq8m7Iel2B4R2XJ_YQkzDtzZVW7jmBrY8gcvqvkNe4rkIfv-wdY0keuX541CIzU0jaYoKPCeC5GIjchbWEmnaAqbQ2UfAh9X7JK3iF2yriOw-Ir3JMAvt0XY8YnljrKv3O4xfDNmtgtKjdvSIR3UafQCOtOOuIaMAa4wMwRQzl18tJQwjle2CjQVjDpaNnwQXb8vjW6gXGpidiTsYoycxApuivp9Y92jH_fZEOp14qQ4oMgoesWOZOBaJ5nIW4sLywCKqlpb67QPbPcGxp2we0HZ-AX4BvW1b8ldYV4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اقدام انسان دوستانه همسر رونالدو؛
جورجینا برای کمک‌به‌زلزله‌زده‌های‌ ونزوئلا پنج تخت اورژانس به یک بیمارستان اهدا کرد و ۵۰ هزار یورو  پرداخت کرد تا برای خونواده‌های آسیب‌دیده غذا تامین بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/25026" target="_blank">📅 21:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25025">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJ1etEeQ29d-9wde25KDmfClGIq_bjX1v-0M21yih48n5SGNMggQJDnk4_d51YAoap1f_mxKvov9VjCbdRE4WpEPyyxxFvGPIkibhSktl5SLwLktnkAAajqf_0nTnvWSxSC0dHgGbP5-l358GXAgu9lOu1tefXW7rvt5PoBuNGlhubSMnQTDS9N9parm0yFMuYWxhYAraSlHur1r53_ebCgyCXvTQ2CJWm8h4FmwFrmyttsybjxxRelkjBAVHCh8jFVBx_484AEv1T3fXvYYMfmOfjjUpl6uqXW7aQE8bjJTBnVHUtuele0J06q71nQX62Yj5gHPuAwZRiLi3mnzdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوراللهی نامزد جایزه‌بهترین‌بازیکن ماه لیگ امارات شد؛ احمدنوراللهی‌بازیکن‌ایرانی تیم اتحادکلبا امارات بهمراه مهندعلی، تادیچ، کوجو و کریم البرکاوی نامزد دریافت جایزه بهترین بازیکن ماه ادنوک لیگ شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/25025" target="_blank">📅 21:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25024">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmQUKUsTdcHWVMGAzcF8CpTedVouUGoGm66iHgGBdu90mJxSjF1_bw0AcQQewh2YwbQiocWuHheZjifP-W_9BQa-5j8pjMBgQKhZH1eeib0GfcawbjrOsTlavLXpySn451703w1w33JQIgZGO_ZF-XK1USXPbU63AlC1ey6wBlfxQnLl-DDL86b1b7iVBEnQiHPtRZehKawev7BjJbJhwXGgf_tDJa87LdtE1ht8AjDSRRE_uzSmSm0EgXFoMrjQbhBRr0fNiCm7w1bLA2xBmQ1G3OJYIZb6StRTCLIftlxwcLmcF0Abdnfxgr-xno6e2OxaZ1bAzHl9BHhzRahrOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مهدی رحمتی سرمربی موفق فصل قبل خیبر خرم آباد با عقد قراردادی 3 ساله به گل گهر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/25024" target="_blank">📅 20:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25023">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmIu3k4SYxDDM7EvsET3s-xOKqLQizZvI3WjtB0pD8GDvMJej7sBrg0UmCNtXknZHTm1LI9eZN6U3_x2zDL_0FcG2gRuBK6WicEAFbSoR-y01dsjaXApzCJXe24R1G4IFYv_CLJl1_iXvbGdaevJdfVVZUFapHL6bVl3L7PFRk_bXjW-uKx2J63Xmabr5RAAuo-NsDwHeBum11Hplw4VSk3m6acwpnFYc3EzACWCh_zryFMeM0so9Js7HiTOTgByOz8QHsxBu-PphxwQSWst_vW4AWr9kzyCjPY8mnYnvJrnnIdCoRANJ3JCf-tP5t5ppQ4cPQHRVQzouAr3EwgE9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مهدی رحمتی سرمربی موفق فصل قبل خیبر خرم آباد با عقد قراردادی 3 ساله به گل گهر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/25023" target="_blank">📅 20:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25022">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9652d5ab0d.mp4?token=irfEk36vfg0kebpPfkuVUnibF25VbsGLjkBuFItMasl5QBmlhA8FH_GBN0HJ_0g9-TNa8ho7LAdwNkT_g5XNUdPktu4Cpn9TFTD7iwJGr8_uvO0xRjrFYkgkqLDpLrQFEeb3NhXK5LPWFa-YPY4bEvdc6lVtEbdHvUcN5uVypr-YvfMPD8s5IrXsdN9WkqYgYvY5iQDS3Gi9tF8xw28_JBWjieGa1C639O0DDEqARRfqrKNivtD7mEU7zXBb7wZFcc1bR55E8zgrXEgXgzAyk1l8hEAOFAE7YwqVouwqpoKxnBd1NtvreJP-H_y_rWT5tr5vjQMcMLkW-Gasamb5JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9652d5ab0d.mp4?token=irfEk36vfg0kebpPfkuVUnibF25VbsGLjkBuFItMasl5QBmlhA8FH_GBN0HJ_0g9-TNa8ho7LAdwNkT_g5XNUdPktu4Cpn9TFTD7iwJGr8_uvO0xRjrFYkgkqLDpLrQFEeb3NhXK5LPWFa-YPY4bEvdc6lVtEbdHvUcN5uVypr-YvfMPD8s5IrXsdN9WkqYgYvY5iQDS3Gi9tF8xw28_JBWjieGa1C639O0DDEqARRfqrKNivtD7mEU7zXBb7wZFcc1bR55E8zgrXEgXgzAyk1l8hEAOFAE7YwqVouwqpoKxnBd1NtvreJP-H_y_rWT5tr5vjQMcMLkW-Gasamb5JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تایید خبر اختصاصی روز گذشته پرشیانا
🔴
مهدی تارتار سرمربی سابق تیم گلگهر با عقد قرار دادی 2 دو ساله رسما سرمربی تیم پرسپولیس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/25022" target="_blank">📅 19:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25021">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89b613cca1.mp4?token=SG1-74vtPzhSzzAMEGAnTCKhmzipG9QiOISMfdAMXtfV529gXpJroGxTrVHM8YwWyDkSeu5Gpd60tiPt4i4rGiAqpDzmImCY7PfgMIc0rkv_0tvO74uRo6Ph1kls5fKgo1bP3xcfGXhTkOBrxCJFFnAO8ghV5Exe0x_oEpNd1t6HBqUasCEiMYrkrurBKoCyvYRCbBJsC4QWFqx7Y6whceipV626T58aYGVuACTT8RzrW3d4RoFiqbOviDCoAWtbuGVniXCrSq4a4JahjzvokcmNWUuzlYV337LwWhgwDVVEaPoKKxm8PMKF8fULF9sTx97aI5w87bc2FZVw5VMYBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89b613cca1.mp4?token=SG1-74vtPzhSzzAMEGAnTCKhmzipG9QiOISMfdAMXtfV529gXpJroGxTrVHM8YwWyDkSeu5Gpd60tiPt4i4rGiAqpDzmImCY7PfgMIc0rkv_0tvO74uRo6Ph1kls5fKgo1bP3xcfGXhTkOBrxCJFFnAO8ghV5Exe0x_oEpNd1t6HBqUasCEiMYrkrurBKoCyvYRCbBJsC4QWFqx7Y6whceipV626T58aYGVuACTT8RzrW3d4RoFiqbOviDCoAWtbuGVniXCrSq4a4JahjzvokcmNWUuzlYV337LwWhgwDVVEaPoKKxm8PMKF8fULF9sTx97aI5w87bc2FZVw5VMYBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
همراهی‌رایان‌شرکی باکیلیان‌امباپه در پایان بازی با پاراگوئه: لازم باشه توی کثافت، شیرجه میزنیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/25021" target="_blank">📅 19:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25020">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/REs6QYqKLwO-oJGs_ZjK-A8UISX8ef9-mpEUBgoEbg3gl3Qyd-8hliSZnbj7nRHYihG5Cen1sIeT0XMzXwmNYb_KCJUz-4S8XSFoy_VaM3ctfGoRiOv7hZHjoavDF5Oow6MfE1LChxEcPWdlc5rsS1T2qUJ6vEVF4pAzSdahkAovfr3NPzDB2GQIud0qrBpogCTxRqxCr10DkVffnLP6EwAv5cgqckvlcp3Er2QZVl-TX_tusZDt-0TcHfVx_pIATZv5NpXPus3g0gP04ek0Smj4rOn7gCbAZzwDixhciYOJ267EChgrpQjiLY_b7qlLsR1VtfyKhyza5iPnkt4Wnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تیری هانری اسطوره آرسنال:
کیلیان امباپه در سن30سالگی‌به‌رکورد 1000 گل زده خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/25020" target="_blank">📅 19:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25019">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrnDz3jzZWmDyW0BpQPmycb2dTHVfuE-dJXuZPSXLN5zz5QMmwEsQat5Bw9u_uudJsPOm5Xz_g7zRSM-lO_7tL5KmMFwlKD_EAf3y8b4yfZx0LAxOMAN1svTTkFz_ANC9BWDvv0gG8mklD8sTWHSu3mLzMZpawYqQlRc286c70yNVQzsTKjjN68sAIDQ4P5VejSoIrgMPgUZYf-Go0oGAWzV95wXxWzSVjXdGKBvGm3relZ6TF3kdTeSC_gJhvMt5noxVshSHHK5An1dUrz8QyCay7MZXolD0R8jYbAqigOVL6A0YEReturbXzPxSBG8QVuHiIpV0IzC_TBEKGLrXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دیدار فوق‌العاده‌حساس‌وجذاب فرداشب دو تیم پرتغال
🆚
اسپانیا رو عادل در آپارات گزارش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/25019" target="_blank">📅 19:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25017">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TjS7_zICtrOhpERA70uF2L3pOiGRdLmuNh9bWp-sq_AqTUBArBm_JwwXFT7tScfARmd0A9ScH8AxXRD27qnbNm5TBE2voUybTrzjbMGCPqQ-AtStU4HbQb6_mvgZ79LhfBIN_zEuYAwFLf4b1Hw30GfvgcTxvBSfNmP6NeCmCKYt6O4S5o8C-r1mUiiOn9C-f10xTY4FXn7cYik_h2YP8pCNDErCM5ycL-zkmwHsHPLSIMPg1TSOrPzmuRoC98UuXPrY5UDWOTgSzeRDEBLu2onLlawxV4Xb9kWF5THI3jg3dcXzMEIhVL_GHgBMG_H3t26zDMAyDUYu0KvDiiHzWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rlyxZo_-VaaVEdT3v3PwPxW5e0Gh2kK5TXMgwNxgtxNkxBJMdDR4ye7ZiQzc6dAtFUSuOwsRCMa6Oi7fgsfPVjjV6Jx5q8tZEAFtj4zQWhFXv2S47wWlOC-2Urr6Q2DwAUZ1gY11Aq6SCGV4jhCw67tTpcU73GbKkAZNWwmEOz0_tPtZJm2dGX9ZYsvhtCexshApc7bTM9tr-zd_zdE1Gh2oT2TPPZv3Ktg8o8X8SRNGdY4MVStNR6GFuVfdV1Du22Fz7NL8_z7L-oPDh2XtKaH732AufAxw5PD9IPlrP1jrl08-wK6Eo8qcu5poupqIpkPizicknrGZpN3c4PDNYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
🆚
🇳🇴
🗓️
۱۴ تیر
⏰
۲۳:۳۰
برزیل
🆚
نروژ
📌
صعود برزیل یا شگفتی نروژ؟
⚽
🔥
پرافتخارترین تیم تاریخ جام جهانی برای ادامه مسیر قهرمانی به میدان می‌آید، اما نروژِ آماده رویای حذف یکی از بزرگ‌ترین مدعیان را در سر دارد.
👀
⚡️
برزیل صعود می‌کند یا نروژ تاریخ‌سازی خواهد کرد؟
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/25017" target="_blank">📅 19:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25015">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZNWpdfvSJyowojWhE084golEawVP55VL7XVs4V1BIx0bukBy7b9IhzD7uKqgxFcrXMnpMBYUKBijTeOf9v_pPd3kc50vjS2k5JzFHA6RApgKVzk-vbLtwraduanNw7GbPzb_7LEnZ7OwDyXcZA2mATKBHCWZRuKrJWzzfk8b511ofzAMc1acHcbEb-7D0Q1jCacVM1qP9JvnFyUPRyq26IRJIxmkGP4LZv0msRSKaEQuXxYllGtNQJRteY5Lvj_S65pY2uFqvRXEFOOy2hCY5BB0hON5F1L9sIBI27MyHzOEfYzoohubNBIBA9BUhoiuEv0v66XlNEgtV2Ro3-b1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دراگان اسکوچیچ: مدیریت‌ تیم پرسپولیس به شان‌وشخصیت بنده توهین‌کرد. تو عمرم ندیده بودم مدیران یک باشگاهی این‌چنینی با گزینه سرمربیگری خود برخورد‌کنند. اگر شرایط مهیا شود روزی دوباره بعنوان سرمربی یک باشگاه بزرگ به ایران برمیگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/25015" target="_blank">📅 19:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25014">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5KzvOy3_sRPnMRl205g5WihGO-OFQMjf3eiKURPNE01fOaMdxzajIKme9wPdC-p3mFME3T0PLgRemohRk9WJ4SOzaqEXprsclueyBQBfCSdXDnRiSU0Neq3r-Nu-aux08I7WeHXZk2wERfnwFmbLZHNV2y6sdODbOkpJf6PyTVY7RJDxg2KgVSsvpOB6zpSt6I5Jk45NnxpvIJxKbvLYKvF0Cc6tWl3Uwo1w70xdqAAsjOX4GXxjwDFLb3vEwpBjgZGevgfoxU1gc30UPQSU2Cpzk7TvGdatWBFghRUr8qvVNCvMA1ywOJRkUBelPUGqm70E1xAj50Utv5BsMbhtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Aparat Sport [3.6.2].apk</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/25014" target="_blank">📅 19:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25013">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rS94XaJBqc9l0XrIc94co3b7kcotCKSrRe9W00FIEKForK3RLfu2wHkK2ojiOTCLpK16t7Hu_YpePPmvYPyudOy0xrfhgjxkt-buvJX0d2i13RbgT2uNrBm__WJ5AyXiepqj2ANpzOngVE-Tv1zI6IkjpA3bMerDcGz2WuYu0icoZJdt-7hN2x-rexE5NkJQ0Kex18FBl7VgZEpDPc63Mal1gV4MFM5mCEAVTfEfoPURa_mfYY6eJ-pDAg_NawIGjUViXkiapx3REJEa7hJLibN6n2R3s_OivNJ_u4C0FD5kvFDULtO0bFUuaMSF2IF5AkQsjyJEVibvvXTgXmT5rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد.. مهدی تیکدری، مدافع راست 29 ساله فصل گذشته گل‌گهر سیرجان، با امضای قراردادی دو ساله رسما به باشگاه پرسپولیس تهران پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/25013" target="_blank">📅 18:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25012">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVLuDwIr5Ms21EvOSAQ5yBAtnZ0ZZVKkSuEabkWQxm7FIBZL67doW_O7IpD2gWIGQ6a1lDMFF9P94jhXLi4mBhNRZZ-jZ2QddiSZP8otwiDszv7JYD7uJ7LQexwIfPoNLy2GoAWMYSIEBLMZgfr9_wNmMSBSKQTMvd5b83ug6okHtTjZKTS42xEnFjYzmi4E5JQKFTumPafVEn0bf6dr9rEO_0eGjHVK0awvdUhsCi0RZbbMhJrpEM81_2vi_PXDVefN1NXJGmS8Mwr3-oid-_QLueGjxbrcO6lxf4x_1n-gyxbdBBueI-Xp6DM4ZiwEvQ9MJgslgsQGIPXSiHGM0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/25012" target="_blank">📅 18:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25011">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tm0DFFGnlsL0noPJej0US79jod4Zb7FThoWYvvf2XBH8p8u5NxypIRsmv21H4zuW-7kYh4zb5lqaT9o-cRMLMwvIeP1e5UqwdTWe_PnChnUWw6VUHXTFY0fr-_8HiQjGWSDfmLbNkhqbPlUXni9Zuokl9TizVfC84LQ9Ww-U8oGQJ4YzKqw5GDRXMooVdSgU5ZIA5a2LGN7U4fnL8HSSyWY28VbGZiyC4-LuPvJNa3Fy623G_1LDlGwQrcpBXKSiaLobq6IUSU2n90HVU--7YjxL2JiVPU42zu3dHqPNZ9FDrOUMwIxOHufQGhDXK4NoJwplYcB2ya1YQVbsT6hB5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌آلومینیوم رقم آخرفروش محمد خلیفه رو به باشگاه استقلال اعلام کرد: 60 میلیارد تومان. ایرالکو تخفیفی 10 میلیاردی به آبی‌ها داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/25011" target="_blank">📅 18:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25010">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXMp0ApqPCeOs6-S3PJegNYtBnhx6MBxcgLkJOK47ucttoLGnpL4srnFZFXI1BLgy5Fy_1C57YjPWQ0K9KqZbaOTnKHDo1kY-aVy_T7C0pY_RewgKKUAedhsHGLlT9VFMpm7PmaUfrJE-PPSwhp5pagDyGwwJAKpXhNR1sbajUlwcVqAaLcs9hZ6U3ZM2ugvSqDSwixV5dEejMLyakGKzds0oznOseblTOZIsH-XrbVv2evpC4UMsXOxn-ULPi6CdRX9U7p-PQdErjECDJIEKzUSSiA4jdByHbI9NrYs5TJiSpJPWhPutkKKwv85VjUXb-C9a0WZ04KaCyhksTUiEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
14 روز و 14بازی دیگه‌از جام‌جهانی باقی مونده بعداز اون‌باید 1440 روز برای دوره بعدی صبر کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/25010" target="_blank">📅 17:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25009">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b051966bf.mp4?token=EAsnjZcETccyI6PRVrYaq1bydY2Ys5zd2SrJskVLfYZel9YDa_apKWSTSwVn7cWfWfa-srd7IJyHW_YtM9Pzif6hU75Ax-CWFHnNm65VtgvTJwFwZoEoEdDRlM8CIarRxsIa_iv7YyxbtW4yC6q-TXUFHo2OFpWt9BYGOwBkD2xbNy52GxEUCPr78dw14nmB6uqMHR5dozuKDYJ2Uae6A5iN1xvMzuhSwAmf7KzotcixODgk53M3n_UfJ8F8GLQOhz-QAKjSx6Z0aIw_VEsSNJ_h4Cya1uqBpHcL0sFJfqP8QgF9ikYB9ULQdHfp25OSB2FeMqsKekBmqTtahBokow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b051966bf.mp4?token=EAsnjZcETccyI6PRVrYaq1bydY2Ys5zd2SrJskVLfYZel9YDa_apKWSTSwVn7cWfWfa-srd7IJyHW_YtM9Pzif6hU75Ax-CWFHnNm65VtgvTJwFwZoEoEdDRlM8CIarRxsIa_iv7YyxbtW4yC6q-TXUFHo2OFpWt9BYGOwBkD2xbNy52GxEUCPr78dw14nmB6uqMHR5dozuKDYJ2Uae6A5iN1xvMzuhSwAmf7KzotcixODgk53M3n_UfJ8F8GLQOhz-QAKjSx6Z0aIw_VEsSNJ_h4Cya1uqBpHcL0sFJfqP8QgF9ikYB9ULQdHfp25OSB2FeMqsKekBmqTtahBokow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ریمیکس امیرقلعه‌نویی هم بالاخره منتشر شد؛
دهنتون سرویس این چه سماییه درست میکنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/25009" target="_blank">📅 17:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25008">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvptXgL9jkWA9qc3CtJ3LcsXFWX_vd6j7M7O42YWy4b8ELg4zFxIx_N4aXDLNBSCaaHstykV63eibFUyYVbEqWtwItbB-DXt6tnz9jLyhzAu-sXMvuQP-X1yrfsGyoClDs7WnQ3O2Wh5ZELfwWf9zMFjurWZZoantoD4-a5dtPDDDcuZ16IQdiqwR7NAxeCDEsT1emjy8XkKysdI0cN5W_77A1p9e6lPYvStpCg0WePWD9V4iiePU5j4uibzxXZ_q54jo5q2gd49sbj2ckqEn1kwCyqvV1es3mLRxv4ROxmZ4PKiE31m2XoZnRjeK_SPH9uGBZ0pXWbMXY3W2vlAbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
سرمربی تیم‌های مدعی ایران در فصل جدید:
‼️
استقلال: سهراب بختیاری‌زاده، پرسپولیس: مهدی تارتار، تراکتور: محمد ربیعی، سپاهان: محرم نویدکیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/25008" target="_blank">📅 17:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25007">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeaaa6b3cd.mp4?token=jB-cz4j0LRHACKlUj9rEkZm4oNntPrKm9onKwH5L0Q2p7ZMOWelnJO9FnV40CqJVFGnpyUJywvlw1LgsXog3eoEjkKOM3-Qo7p-UB0EKzGceK3IcMJ6MG_ZvCwjF30C7xl-vsBX59XK5fzWh37xvzwYvWmSQ77wzGorZgvjTYT0cTGiQtlu0MtxKdUUtJDVQ5R7PosN4zKw_W9W8PpuWZUmqGz406o9M1DrpCl3fhNllqH7XIbSNlXzJOQVGd3k3S_T2VgcRcrLBqeuMjQCj-BJZ35Xlbu9APM1hcY3dNq7QGf83Jb79l3elVCBzlcZxUWK9drqlijaj4X8G7lufag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeaaa6b3cd.mp4?token=jB-cz4j0LRHACKlUj9rEkZm4oNntPrKm9onKwH5L0Q2p7ZMOWelnJO9FnV40CqJVFGnpyUJywvlw1LgsXog3eoEjkKOM3-Qo7p-UB0EKzGceK3IcMJ6MG_ZvCwjF30C7xl-vsBX59XK5fzWh37xvzwYvWmSQ77wzGorZgvjTYT0cTGiQtlu0MtxKdUUtJDVQ5R7PosN4zKw_W9W8PpuWZUmqGz406o9M1DrpCl3fhNllqH7XIbSNlXzJOQVGd3k3S_T2VgcRcrLBqeuMjQCj-BJZ35Xlbu9APM1hcY3dNq7QGf83Jb79l3elVCBzlcZxUWK9drqlijaj4X8G7lufag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی زیبا از تحلیل جذاب گل دیدنی لیونل مسی به کیپ ورد دریک‌شانردهم‌نهایی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/25007" target="_blank">📅 16:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25006">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bs8DdkRAtOv7XhcmCvDi2IaHt-uVD0bmFWTFxpmeNdW7fpN-TZPt_g5uylmRLdmY4313KkazoJYOpdp_62DEXsJPj1y5IZCKB5rvs8jHFb2ZR1nQR6PkSdRgQSzLldmhd4aV4GhC28OHDKDs-64IB8QQjAt-WFzzjiAcbxHkOvKCvKr_jQafsGNiL0RrsPblmuZsTrQiHnJXfMjfkjFL8cjQMniY92tHCLosP5a-NTiE2JrZTHiYD_t7yyoTSeWlCHu9RFJhaxpd62SZ02prYC1MTv_lzHYyX0Jc64RZltJuLMdadTst4QY9bBIVqiUsth932_mgklZn0sXrNESTRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
باشگاه استقلال و تراکتورتبریز امروز صبح با ارسال نامه‌ای به فدراسیون فوتبال خواستار افزایش سهمیه خارجی تیم‌ها از عدد چهار به شش شده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/25006" target="_blank">📅 16:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25005">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqaPu7W-sF5qDzdHyszUza1HERnJNNiBtk0cXSJG0oiDEYO-Vm7vStMULN3pAsmFCMFxi7x_9HcFxB4z6uaURaxOrVpsUSzwOO5DOnx7ajueLwIdjE3tbiaN3rb6Cd5iz2MNDKa6JLosOcfhjGuDACVzAuBIBJx6JpylyuhagwyTiIj-i15FYnlukSbcW0ACnC9gSuMv2iCd36OYY2Ayc_EcKBoPi3GzJf-O4GmPhwaDc2pswWRovtJJa0u_EL-G5RLy5RcVo2M3Fmnx0IeFAyt_Wd2jnCvIzfRPtZDI5rM6WdKfv2-bq3aerax4use7p_j99cErjsJcpQRQh13JGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
#نقل‌وانتقالات|پیغام پرز برای وینیسیوس جونیور: یا تاقبل‌از اتمام نیم‌فصل قراردادت رو طبق شرایط باشگاه تمدید کن یا قطعا تو رو میفروشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/25005" target="_blank">📅 16:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25004">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aa6c0365f.mp4?token=Rjh_rz1rln3dsiT5Ck6fPKP3eFOGJsS5Pt72muPTg-eE5M125oCWSNPZ-xh6EGKyJdO98s5njqsBYH0zEuiqBUpY7o-ri_q2xbUOip-B_OsBu--AWIasJyLn4U60ybEzLGiFE-RO8fItK8RaBAUKX5UNtI4AlqPhzREKKmANps0w7J9pFKvZN3Fqy3yihYf0ZnN4YCKdwRpV532MsnrMz4N-BsM51MswiFmrkYaDFezzC8mCCqeJwgZ6YXyBECUilWW9ro_LvIfT3h7fbLLpGuGzIXlAWM2ZNkI5_wgkYga5FHlTcPm0xh5v97fiNdZ6R80Xk1ViO6y4xTCjq6oqPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aa6c0365f.mp4?token=Rjh_rz1rln3dsiT5Ck6fPKP3eFOGJsS5Pt72muPTg-eE5M125oCWSNPZ-xh6EGKyJdO98s5njqsBYH0zEuiqBUpY7o-ri_q2xbUOip-B_OsBu--AWIasJyLn4U60ybEzLGiFE-RO8fItK8RaBAUKX5UNtI4AlqPhzREKKmANps0w7J9pFKvZN3Fqy3yihYf0ZnN4YCKdwRpV532MsnrMz4N-BsM51MswiFmrkYaDFezzC8mCCqeJwgZ6YXyBECUilWW9ro_LvIfT3h7fbLLpGuGzIXlAWM2ZNkI5_wgkYga5FHlTcPm0xh5v97fiNdZ6R80Xk1ViO6y4xTCjq6oqPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌ازهواداران تیم‌ملی‌مکزیک رسیدن جلو هتل بازیکنای‌انگلیس‌که‌نتونن خوب استراحت بکنن: بامداد فردا ساعت 3:30 بازی مکزیک و انگلیسیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/25004" target="_blank">📅 16:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25003">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‼️
یه‌ویدیو سه‌دقیقه‌ای‌جالب و تامل برانگیز درباره زندگی شخصی و فوتبالی مدافع تیم ملی کیپ ورد
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/25003" target="_blank">📅 16:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25002">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rx2omjNjX9vevzXuggb997A4qPuTNqAXoQDxUIokDxAIPysedlEevZzIc-2ZXL1RTVR4KvuF-B0RdGQy8GjVTkF4tJd0xCaVOyycVlkHNetri-_kKBknPMuUxydg5kJ82-79Lwqih8dPG8nVyHGT-d6fb0mmpP1Ht5vqVB5zzJC28YJu925csa1ysGWyW9n_gYaMR3KP_FAR_n9a8sbAA8CNV6sXfZVXJX5HZvmmAbkIVgUNf8yLLUlbSJt3RY1jbd1RM2u9otvSuRV2ryvk-anPB7ZTuZb90ogvBqb2MVwvn3B7ll_wy_nTuRTDGMnlbQZF80C7IMHnbs1V5Sg2Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی روز گذشته پرشیانا
🔴
مهدی تارتار سرمربی سابق تیم گلگهر با عقد قرار دادی 2 دو ساله رسما سرمربی تیم پرسپولیس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/25002" target="_blank">📅 15:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25001">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NxS3D-pYt4MvG2-d9LhpNAnMiATjoE9-KNcYX2GLwdSXcefAZYqdnyqVJ5L9PWcwFvNPOUjM7nFmh3BZOdTVS0nawlsbe4KZwn_18wPHuycRjcqS7LbTDjURmLXm7BWicmXSpzK5tUcwlSJJhjXNvXq_TsDwdm9kHGXkE-MXiW55A1t0JgHZGNePySdbbuSWzrbh-IImC470UN_P_m4wq0jKf6G0G0kM_JP4Ze5AKwTl-gypjBdZdJYItZ4U-oiEbPEcIoXWWsgVK_ZHIyciWNsOxGa_VetsxZHVQlDf6h0uLAY0TBWvJSzSfl9xo_dQ-ML65d7usfiKaSVIzKTnow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/25001" target="_blank">📅 15:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25000">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGqona0e_nVjGeHhy8N2h4QY8ot_ojvInVc0KIVxvZ8JLnbhzdOyvmR68uz2TilhiH4cRcP5ftkRU7Vs1J7bg1cyOJgTdYVfQfbNtoAtXflcEGjBj6ZeOpzNcwarAybWa8mmf4j60m-bFb-DZrABwg1Gku5Ybwy6lKuChHs_HVxjHT1iG4JHai_lJ8i1jFAZBWCh0ELIHsxA_hbBC7sKvgEIFp-gCmVNV0oYMD7_QLNFnDyyiulYwN1EN_eeFpU1zrb2LBJ-GIbVPBCIUxDKoFILfir-MW5p8H9Bbv0RTDoB9R2Pw-uzTHMNyPkmDO-5JiONyJy-7U0mPK77K53tTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه گلگهر سیرجان که اخیرا قرارداد مهدی تارتار رو تمدید کرد بندی در قراردادش گنجانده شده درصورتیکه باشگاه پرسپولیس این سرمربی رو بخواهد با پرداخت 20 میلیارد تومان رضایت نامه تارتار صادر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/25000" target="_blank">📅 15:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24998">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CZXnwSgc7Wg1hVYtE8HLrmA6SXi4d9AEQ45zjUuYab05M15mllMn5TZ4RqFSd9RTQZiRaCeZRIYpYOugTG4fCa4ZTLgsOuOwHawAyzMoP6jUgLim0fejcubIUpIf-N6GI0zl8LI7RNWxuF6t9DYdOJLWqp3x-R4SjfvIliENMySoMWz3K_H2Djx5j2uMswbWSIQIO0lZHwo3XxTl8ObFhjNjDEOYRkvqUt4S-UvOPkWuFve4s1HxD_LFQC89sT3EV7cP2rTWz0hnAYFJc7ku0LTAgKnPB9zMLQAa0ouBcvxL6Ra7yhapjIJXK6XNy9mwQe-L3fc_oijODXa_vowaAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AHxpZDOHwFXKjL16_7WM0RKyM_-FDj67L6zsBwvRsROgdPoA3u36wC5q8FT8UmPCW_QKhS2TYjSzz2enlPsY7E4Z72kCM2QQwbP-D76AL4zdCMiu0plkXnEke-h4DKSbcg5QRW3_SQUlhIeBUUcYAnxbVlYaSLJFWeje5fGrmFKhXO6jBeTftPoajx-e-dz5Ltfrwpem3dotBte5wLkCRZ46eUkLE-g8JAt9CnA0kCbNucHyP_srMMSm6pBP_tLnqoc2ynj_tXi9Ypru0D9OoimamDdYFJVDYY_ehuL8NjMHw5CqDuxl_W-tylivc9-5PAggL57v7pMLTmRXMKBPAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🗓
#تقویم
؛ سال2006 در چنین‌ روزی؛
جواد نکونام پس از جام‌جهانی 2006 به‌تیم اوساسونا پیوست و به نخستین بازیکن ایرانی لالیگا تبدیل شد. او طی هفت فصل حضور درتیم اوساسونا 197 بازی انجام داد و ۳۱ گل هم به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24998" target="_blank">📅 15:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24997">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePqmA25vkk76VCxF_-LFBC4wnjI96ajnq6gTv0gSUm7Hz_MCEaQA0lCA6w9JajWkhVOm9QRLQPjxMRFI5qgXlRaxDNWTNEgb2GAXAWOuGGEzvq5p2d-9QrBxvfdK2BJrlPLzMYdr1HnPMpv2kcRSmPSpWMqMIJ1dr4f0l-R6w-autaGAVmStodl1tSSs18WWjJPgUJYGtww3LY9pVicjcjiwJOgYvJ-PDVJInDTlSPXL0Liq363mv8J0ZHWJ_kSCUA1A08QTuoYBYMHJGKgiapVKHw2LlBnTcvHCC4wqjx7EFkIyV744Y4hD-EJ9EsC0skRgG9bh-Wm124NiqGtRrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🔴
تایید خبر شب گذشته پرشیانا؛ با اعلام باشگاه‌گلگهر مهدی تارتار از این‌تیم جدا شد و بعنوان سرمربی‌جدید باشگاه پرسپولیس تهران انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/24997" target="_blank">📅 15:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24996">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SmQi4dgBleXKU4BJ8VTxvBljejUorw2fesZY00nCR9NxF8QISKDSBZB9RAO9Zt1RjYqjj8IZjjIK5fql6mv3srsmOx30vqDmLGcMQr-F2XToOhs0ExRGhAlaha_t3b3ZjrWeDnLRdFRdrzpeutl4foixVPaDnE7c85cAQZyTzUNKfEFAOZJevYyeZn-deGjhIoQCGeaVyaA5i5I_VWlBCusWoNDJrteQIZidrLDXSuNQoumOvKWKIF8wdYC2RY46Z1eXHAmgzdCbZYigL02cgQvMLsNe4ZDcBr_bKW1yZuEATnJHv29_BbAEWX5j_HGgMeZ2oZmsWq9OXpzE-56NPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ مهدی تارتار به‌حدی برای نشستن روی نیمکت باشگاه پرسپولیس ذوق داره که به پیمان حدادی گفته خودش مبلغ 20 میلیارد تومان به گل گهر سیرجان پرداخت میکنه و قرارداد دو ساله خود را با پرسپولیس امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/24996" target="_blank">📅 14:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24995">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdbtZ6o0nz5rgRtyG119b56L99xj_51ac2lz_J748zL6QMLFAVhIQoBAS2KnTVd50-nA-RVJpKD1oFEg_qLhb8WwNVxnmxz2mnd71CAUfYSnPGmP9jIw878Hx7PGEkD1aiBX7qCYHsEncsSdBJnU3nGkIl0_9H5_ANbvuk_jkMRmB_uiPhVsayY__gYF1eVLPZPMbUROxSUGn4VFULUYfaSo9-DpolLQZEFtW_-mCG5KdRO89AP3134YjKMGwE5Zg2g5lP2T5OIGGAne8pHOKXIEI0MgEcPNfW3txZIi9FN5eZvxc6LbbU1lB7wOBK928nXDMWrI-3faZNs6ox_Dtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دیدارها‌ی‌‌ امروز؛ از مصاف فرانسوی‌ها با پاراگوئه تا نبرد تماشایی سلسائو برابر یاران هالند
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/24995" target="_blank">📅 14:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24994">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oIL004Z0VLnjXgIFCB4MBSIerOX03_2OJ6_F-m2l3VcnkgsRDFg4V-8uKpWUO4-tzvQBjAYDR3vd-MLE1IbSCJaD_QFBEUQ3k3hqPMipx-zIkNkj-G5o7z5-epGuzngvjVXUgF5p4tI5SV3QZnLxZlNB8Rv3C01G5JCB_3Zeo2470AadpjmMNnbZrN6u_80nIMIrI1KdJWtUB8tcMIFZOuYsw5lEJXt7q8ccwpq8RpDJbnsrJiXmzMwCkonSudLNzQ2JGNn168kDC595jGf5_UPiXYU02kUJwK8rigDcebE_20B-xchHWSmbmi1fMRlp0l2xjUDi6Os7BenD6Zm5uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وزینیا ۴۰ ساله در جام‌جهانی ۲۰۲۶: ‏۴ بازی، ‏۲۳ شوت مهارشده،۱۸سیو، ‏۷۸.۳٪ درصد سیو؛ مردی که ۲۵ سالگی وارد فوتبال شد و از رانندگی اتوبوس و برقکاری رسید بدرخشش مقابل‌آرژانتین و اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/24994" target="_blank">📅 14:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24993">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnhTcGrFWnuuaNgMIotMnKjLOn2BBs8WdOLhEdKI_z2os5JFOpXaUv9q7tVtDthkDzSm9xsv3f377fwF_zlZ7cbOzMDeNgnJfYr5yxPxWbfZSX1qtud3SBIYIAdESkaDLl0C4aI2k70g2S_8YjQqy53GBFyumBoYpWMDvkGuF4clA08Po0tPjvPr0og72d8s14A2MA2TC1wp1gBHbtUYj3x050FoY-lPJx1JYMoVgsAw1UyGnDsZhgdQZg0jrocnih7lInutSP5ULdGXcf4sAKihVpamxKrWxXpOuOnb97PB5EQcnQ_ydqRfmVWRds8MExN5aDUoiGxS09N0rVjA9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تارتار عصر امروز مبلغ 20 میلیارد تومان به حساب باشگاه گل گهر سیرجان واریز خواهد کرد و با عقدقراردادی1+1 ساله‌راهی پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/24993" target="_blank">📅 13:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24991">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYlMnq0EB3UQi_DIpLMm_EI1xIo2YRXKUoLfUBV0HgiTWD6RZkOWQv8RG0748DeafADmSbnWliDZx1PqzKCsTh-nPBk1j06m9lqLKSM5kpWA8Q-55Un800WiWyJ-5XCHyOq7oituP1dwkSizYAZPcY48Uyx9Tm_6me1dIk05U3As6RF9cSs7cVP19mGDrJodkPPqUwiLQ7Ni8mBUESXZg_nLYWoGE4sCokPQuXWzEA3zSodRP04hhIZd7ik0ZbsxTmgVxQ4rawDCaANllk_WGig6Y8ZK3_dgRtuaywwlhk51Sdnq1U_lCCOjJAqSkODyjoy9M5teV97j_o2qJDkvew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رومانو: ابراهیم کوناته و دنزل دامفریس با عقد قرار دادی 4 ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/24991" target="_blank">📅 13:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24990">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWSpcmBAqWB3-Az-AbOO9biFuExuYJe9kNsKO07emTbWoRrcpROOVYPRLDfRqORD1xBH7sTxHqzLZsrDAG24Jy0XOBqHt9cUbzdOKgq2uo-HQh9wAzZVvzXaE5tFokvE7NGJ1BuOXZDMs6xLuhgSLj6f7xLbdLGl8uwFr-O_bdBijHEgD5-f8OI1i1gDQk4o9MOFl3YyrYt-Dvn4R9VfQ2VrABWcKQdfNfGBZUi5dFVmy9snhYdn9haY8Vr6Aphbom1jCy5TY_MaSUcfJGSk1cWxqN-lLSlI63LTqbZSKZkVMmvuxeMYPWhmI2C6gwRgUwcrFvRUXokYXHg6XDzRPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ گزینه دوم باشگاه پرسپولیس برای سکان هدایت سرخ پوشان مهدی مهدوی کیا اسطوره سرخ پوشانه که مدیریت باشگاه پیشنهادی سه ساله با دو دستیار خارجی به ایشان داده است. مهدی مهدوی‌کیا از مدیریت بانک شهر حدود یک هفته زمان خواسته تا پاسخ بدهد.…</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/24990" target="_blank">📅 13:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24989">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8RchaCsfZRSnYz3SlUgTwEX-0joN2X5UTN0gzp14dOM0TZllYY23biME_ikGL-36yFRMxmygJTGlWxTW_vFvHzpvzJlz7WbzjHMTiDZz4LhO5ONuJ8muBu4Q9HsneW7qRoc21eAIpn3Z6FOfSONQ3awWOEebccvbMwulRV7b3uHVR4z-aIoBqGHK_OBNHEoUJUw9_dmQ_9saXr7Ie2DFzbbCPf2s_jt0_pYcaSZzwh74hzvKw1w_-RptKqQ6kjyFgj-2NaabuonTegJkbvmHk7V39rUgQo6WxGgFpSLu9ymT8XFCT0ly3d-eLoQfAuJvWvMvGI7USx_gVZYhbmscQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌رومانو؛فدراسیون‌فوتبال‌آلمان با ناگلزمن سرمربی خود قطع همکاری کرد. یورگن کلوپ اصلی ترین گزینه سکان هدایت ژرمن‌ها در یورو بعدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/24989" target="_blank">📅 13:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24988">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_MZFFRQ2HvXMGHp_EwoDBt__BXz8i1B71wc_kQAm_Xs0zOmVgf1xpY0VMvYCK2d5kgaudzqkgAWAWlZBUCl2hCoBq7JhC4UPms6_8oKlu2bSvTFSWggMXzjGouWbg1Ik2fEhuFECGbVsoA568B1NqGO_yDi5QqJoVH1y-Avl8hwQY1CbuWkTxXxWnV0tmAy9EEnzR8fNom7PdrYmj2DhH_n93NB53fDBDAEPzM3Aeo5387Xlo4_Z2WAFUi5IxVg2ntRLH15Ln8UdLduD_plI5HFeKnHLx10SdZCOtYnbmBbgCkGf6ckVuFrkqGce_yyIwwjX5TZZH9Eq6vQxdPXuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تارتار امروزاگه‌بتونه‌رضایت نامه‌اش رو از گل گهر بگیره سرمربی پرسپولیس میشه. در غیر این صورت مدیریت‌سرخهاسراغ مجبی حسینی میروند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/24988" target="_blank">📅 13:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24987">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b31ZX3KthpMKewEsnZbV-pwkQz3aSGQTOuOI4WCcS9F1fSMuyyGGb-j4YRg8Gi4kqcJsDFB0mr0mtKTU9qdL2u1o0vef4k3N0-kx-QPTPrtgXKJ0sbU0YQ8UJ--EW5nM8tWQFY1-JjAdClcNxhv4EEiM9LjhtaGv9CUQ8HV8M6HEwtShE4rqHBJJdl2qo_sFP5eNIrPBdWJkhN0EO--xbrEdcjOufMc_sfLCKv_XllvMjY3GX6wkt7_RKRrwbRJTtCjT0gn7_GpR1QhLHy6xk16E7H_8j6KTNrVruzTtzj14WMQ5xQ06Cob-UlSf8X4q-apzGdxvCCiSAbEPGAE5Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/24987" target="_blank">📅 12:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24986">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwfBqduTcr01H89_S9zRG-BI9_5QW89_7BHGTKCRHUKrS8dGnN5ri0K7fl-U49hHWSRi1YreruEJUL_amv_phfGu-PGNdzMRB7W1kYh-A-Pigl2Jh6QGoNh1AqPsfYJrUB1zPzfKPO79qmX1cdC3VFzHRnZpi4NX53miXkJAEPsRAlzR9dY1p2wic-FzrlyUWgYBCmI2KAX75tTYMoLaWMUi-ESC0JqW7HDdkiNFGMNsUZV7KBfYLnct2HfpjkBeiEs0kowTOZxbEz4CQW2c7Y1XeWSOFE-cNGbS6y7F6QMNa3fjfeVidhocDIeXMZ09RUTX5FiG89HPNsCQpgicOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#نوستالژی؛ یادی کنیم‌از مصاحبه قدیمی کارول سلیکو، همسر سابق کاکا و علت جدایی‌اش از او:
‼️
کاکا هرگز بهم خیانت نکرد او همیشه با من خوب رفتار میکرد و خانواده‌فوق‌العاده‌ای به من داد اما من خوشحال نبودم چون یک چیزی کم بود. مشکل این بود که او برای من خیلی کامل…</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/24986" target="_blank">📅 12:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24985">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTdB7zRxkKjEpVwYBhLX6dPtDKX5T-3iio7jPgNtp3ss3me5sM53kfGj0UEtft9nsuDgrP-k7wCvdJoDaeA9_w7kvh-lPPlqLtnK37vGwZZ4M6grCc1z4VAcoMR4OMA76A_VHURBaT7_uJzo8hABpcpZ1hBnPQzu89MZSHRPuCMXexWIrLbweSBokwdcmhdmBFzWDy0-kLNG27oIPUlurkFoO_VVqh7XZwAc2VZMYm6mnqiVhh36pnz6L_LfJIs-MeXlH-As8eNKiNVAT0BdEVtjDzoLF3Swhp1c_uMIZIsZMDXEu9Eqb0p3_FqIKjPOXQ2sO77EMLPAodEKkoV0EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ طبق‌آخرین اخبار دریافتی پرشیانا؛ عصر امروز جلسه نهایی بین مهدی تارتار و مدیران‌گلگهربرای‌فسخ قرارداد برگزار میشود. همانطور که شب گذشته نیز خبر داد مهدی تارتار به مدیریت تیم پرسپولیس اعلام کرده خودش رضایت نامه‌اش رو از باشگاه سیرجانی…</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/24985" target="_blank">📅 12:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24984">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9VyaOTd68nHMZIcoFYTD160BB95cvp3Og-IU9PkUMiPMgyHOCH43eMcougEV50dfRfNy2_-Pv-cj_fCoSSpysCtWdGrSklrcFkWOwd73WuvDXkgQLgmL2eCgmua_3uaC3MvheE767b5XGd-8TPj6qA4y_joPaUwleVmPjcpfujEx_mAdTggtweZPxPwycpBh-Co1ruPDXH080v-Rbb2llYJBzUz8kGfuGqko8hYHt0oOv4EhLBtJCsGBCA0kNKRaPgvnh7OHoOWFnU3Y4xIXg4LTdN3D2940pthBycb-7OT1hCho_9NBCck9angBKLMmPEClfokV8FuhjiWMri2Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ مهدی تارتار به‌حدی برای نشستن روی نیمکت باشگاه پرسپولیس ذوق داره که به پیمان حدادی گفته خودش مبلغ 20 میلیارد تومان به گل گهر سیرجان پرداخت میکنه و قرارداد دو ساله خود را با پرسپولیس امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/persiana_Soccer/24984" target="_blank">📅 11:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24983">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ks9OrUKKiboTvGfZhfddZPNPRZSO_ianaDRJ2lkodbJpAvmPzVl-LXPkbwoT0Oc1-G-2ZjnbrKFAHbGHwS3MORSh8033_czD6iBzeOD9UtiYzwt-_DqqGxG0NTsyaJPixgcsExb4H_BtP-fGEYCvnyWBfYn5B0ax-CJufhiCyjFImSeBPskOiEbvK72fmCXAg2EFsyw-V6gtF8Nwu3ieoD2zyh46fLVa76Tb-UPwsH6Xx2t5ZthJbQS3dgLTHEpJiM_Tj4dzYtZyT1VXIBajCFyV9hjPKrky3iCFSbzYsil2grlfEPTRa0j9HqDKNlutGsOOAWQGcdriOCT0zO2WUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌مرحله‌حذفی جام‌جهانی2026؛ فرانسه و مراکش در یک چهارم مقابل هم قرار میگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/24983" target="_blank">📅 10:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24982">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3vLwDiPNTg946E-Swt2DTtxsAMuDZOS1KoxhKGjhRNI40U3jGSGED8M26LTVvu6d5CYBiWShQgckhexxej590yeaSQaeVDHwZ_ptHYC8sRaXDPONFJcQ7my5D_wSBmzjxiQTKCC_HpnhbBkOGab5rPJ2M3uaoKlZaS99lFTb6eRL_yuiD91pbMPouNRa1070X6ICFgS6OY0LbRoS4_cm5YMoPsys9FJeTvkYE2eUQUZJxnKPzo8pEcxtX5z9fAXnOwhfMyD3gW1lWt5ukOcB_k5rVZUne0Gw2Hy3QPy-c7e09VJvHcvtsNWx0pZpamDvS4byi3HuL4rephZSH0ttg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏این‌داستان: امباپه‌‌کم‌عقل؛ رابطه‌ی کیلیان امپابه ستاره فرانسوی رئال مادرید با دوست دخترش، استر اکسپوزیتو باروشدن‌خیانت امباپه‌ کم عقل تموم شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/24982" target="_blank">📅 09:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24981">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gaeXxNJ-fWf3biKnBFQz6hVSZZeLcGcmUAnRN3gMKijViAifwG0vnAK3y4DhQbZZzSZ5tjN1kRS59if6Fm8s6Q2O9zlY-CTvJ2xrpzCUM10E4AflOaJYbUVkg5HmW1XE2lDJWEtk_-25y8qG7sscUerrUwOfbUajBlrhg6I5SJfbrtAix_gwV1HvGNUHaNXodRC6NnmpNw3oLZs-loE9wmdjWXE0xbXxplFJBwkUU9k8YMZ2ruUpEd9XYsySbD6TWUheiMZOG37V2RubJVFEp0QvetSVr_Z6hAyQEZIHE_7A4B3E2-HxTVmtzzkh5g3vX4FIKxRTHPddQpvGwGJCXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌دهوک‌عراق به درخواست یحیی گل محمدی؛ با سینا اسدبیگی، حامد لک و محمدرضا سلیمانی سه بازیکن فصل گذشته فولاد وارد مذاکره شده‌اند تا درصورت توافقات نهایی این سه بازیکن با تجربه فصل آینده در لیگ برتر عراق به میدان بروند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/24981" target="_blank">📅 09:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24980">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7875374a88.mp4?token=mhw9MgfcdeoEf1jiL4P-gMx8eu_hKgL7mVPWoszzUvAwwQQa2bpTQiXGZnB0PNijsBoyvsvlf8nNCh-dJ_lepTnqylBGUBqkBOdeCuQbGd_PlmQnQX5irbvSni0hftBXVR9w5OixrP-d5ghoi-psULJPyn7YmaPgNJmO71m_XVFEGYp2vFhEGGXbFtR8HT7zhnlCPENwF_E9A-uI_26jsml2TQcbKL9ECrY0cJHFeg99qwyLIVVp90YcTHjuTGsrUgMzhq9IZdiyEWy8z79jzHhtrqVJ1fLTbZEf2FRoMKNLayhOMyYTXk2_1cDp1OPunXI3QDuNNkD8DwZEFXMI4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7875374a88.mp4?token=mhw9MgfcdeoEf1jiL4P-gMx8eu_hKgL7mVPWoszzUvAwwQQa2bpTQiXGZnB0PNijsBoyvsvlf8nNCh-dJ_lepTnqylBGUBqkBOdeCuQbGd_PlmQnQX5irbvSni0hftBXVR9w5OixrP-d5ghoi-psULJPyn7YmaPgNJmO71m_XVFEGYp2vFhEGGXbFtR8HT7zhnlCPENwF_E9A-uI_26jsml2TQcbKL9ECrY0cJHFeg99qwyLIVVp90YcTHjuTGsrUgMzhq9IZdiyEWy8z79jzHhtrqVJ1fLTbZEf2FRoMKNLayhOMyYTXk2_1cDp1OPunXI3QDuNNkD8DwZEFXMI4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ مهدی تارتار به‌حدی برای نشستن روی نیمکت باشگاه پرسپولیس ذوق داره که به پیمان حدادی گفته خودش مبلغ 20 میلیارد تومان به گل گهر سیرجان پرداخت میکنه و قرارداد دو ساله خود را با پرسپولیس امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/24980" target="_blank">📅 09:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24979">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhiIWurWgPO1LO1o8wOduiiBWEnOmJYv0sCGsSCtKoMLejpVJRv58kGrcV_x_ob4gBzAXDwh_2VzkC-C-E7_yX-plNCQ-chQUVs3U87oW0bvMBdbLnQLAXwg4Ts-lPtirXw8r7UojYZ_RnWxarPiDC7O0o2qJLsCuQeMBewOszdWUHzf8wFeG92HR3t-qhcroOtknisr2B8ypFzfMcNB9Kw3RDJDiCyoXnonk9cZaktBFl_y9ah6NgnlVPr_g47i6rUgNH7rmu3Z8lQpoQpMhsqMiapMe-I7ZcoKKFf8UqjzW37tHpYAXYiCK7nFAk6ctmCgCQuaGcIvz77ncKcnVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گائل کاکوتا هافبک‌تهاجمی‌سابق‌چلسی و استقلال در سن 35 سالگی از دنیای فوتبال خداحافطی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/24979" target="_blank">📅 08:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24978">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cd8c901fa.mp4?token=mIEqWm3AFnVcNmHA3_BwZMhv7AD8ojVFqd41saZclt8h5V5ksQJk02SSutaIF5VmDo86bYG3pvKWltjrU7RiRtLvVvg9Q5YeTepxwB78ZPIF2YzOPjaDVReI0nyUp8ar28O0gdBLt0Jo334CdUD-mWCWAd1VqqYI7ZP7nCIJly0i-PpocN9zvDtSODkEc1SR-HgdAPUvVEZUqxM-pCwvJRnWgFrP8gtFNyXDgzNglOKlTAvXvhE1bjwxQo6DG7Lx3dNbtARsJAFRqbRiPINKsgPZ1jLoypcv7XrMEa7ECF3R2WdPW9aqiPCJKh4jd95d_-U0RzeZX75gtXniX038MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cd8c901fa.mp4?token=mIEqWm3AFnVcNmHA3_BwZMhv7AD8ojVFqd41saZclt8h5V5ksQJk02SSutaIF5VmDo86bYG3pvKWltjrU7RiRtLvVvg9Q5YeTepxwB78ZPIF2YzOPjaDVReI0nyUp8ar28O0gdBLt0Jo334CdUD-mWCWAd1VqqYI7ZP7nCIJly0i-PpocN9zvDtSODkEc1SR-HgdAPUvVEZUqxM-pCwvJRnWgFrP8gtFNyXDgzNglOKlTAvXvhE1bjwxQo6DG7Lx3dNbtARsJAFRqbRiPINKsgPZ1jLoypcv7XrMEa7ECF3R2WdPW9aqiPCJKh4jd95d_-U0RzeZX75gtXniX038MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه خطاب به تیم پاراگوئه:
اگه لازم باشه دستمون روکثیف‌کنیم و وارد جنگ‌های تن‌به‌تن بشیم، این کار رو هم میکنیم، ببخشید که این‌طوری میگم. ما اصلاً مشکلی با این قضیه نداریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/24978" target="_blank">📅 07:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24977">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O4bQ0lETtyBu8gakke8ejrTv1yrgaWCoxDvCCU9cQkvnJCRs_iY0Mm2IVEtZTMoiRNiqdkp3ZLc2nm_b09UT98NyhnRpTFOHn5i-z97r3yfmrorNKzmMsZIoHeUFAJiSGUnmNh0YtfL6IuigGGhEloFEYFTQO2_sTw3b6XlVSwkcxjNqKJpRvsVhG5AYXJeBgim_gZgixrrlhEfXNpRZe7qN3KLbhAnwlaUL630XE4WJRgYE4IfqhIsYygofSQfzhpbyKnVjHqtTNuiQOKw6UsxDa0M9US2PxqhHnW5A07Q6RxWJsN1dMaE5RJc-PoaamXIna_Wd6cCOMdfdBb8pqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌مرحله‌حذفی جام‌جهانی2026؛
فرانسه و مراکش در یک چهارم مقابل هم قرار میگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/24977" target="_blank">📅 07:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24976">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5736be2a0.mp4?token=upy9qwrEJpHDBnruirlBX8IZ5YcyZdY0CGT7EXbbhPdZ1NgCNoxJob6TDqsQRyfJjGhcswFofXisqLsilVYAaayna9LNcJt3RMKh6JKyzDjwYY3EQVj6VNosNNqMCNVibn45EIuARSC96ViKEeqp05GYn1rN76eSTTTdm-lTmSLFWROCCOg38HedqowPF9LCtBw1Xwyc8PkMiaL0BCK4nGVt4wJLewI-V9rynKwpAIG0sqZkCxQW6VSLjWusBhwzt1cG93cR7jtyGU6HKh1flbrEYKfyLANwXrLfdJKTWOJmOFq1cGIXnzXQbogI316XoPyvXwMcSYCEfJfA0_4-dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5736be2a0.mp4?token=upy9qwrEJpHDBnruirlBX8IZ5YcyZdY0CGT7EXbbhPdZ1NgCNoxJob6TDqsQRyfJjGhcswFofXisqLsilVYAaayna9LNcJt3RMKh6JKyzDjwYY3EQVj6VNosNNqMCNVibn45EIuARSC96ViKEeqp05GYn1rN76eSTTTdm-lTmSLFWROCCOg38HedqowPF9LCtBw1Xwyc8PkMiaL0BCK4nGVt4wJLewI-V9rynKwpAIG0sqZkCxQW6VSLjWusBhwzt1cG93cR7jtyGU6HKh1flbrEYKfyLANwXrLfdJKTWOJmOFq1cGIXnzXQbogI316XoPyvXwMcSYCEfJfA0_4-dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👤
👤
این‌روزها ترکیب جواد خیابانی و خداداد عزیزی خیلی‌سمه‌خیلی؛ از دست‌ندید. این بار خداداد به جواد گیر داد ولی دهن سرویس کم نیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/24976" target="_blank">📅 00:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24974">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rx6QN4M_5qp-RgMp7LVWImizFpPlDJgnGQgjdOfC_n4fzOLqm9FHXmsrRaZNJky25lEh11XugOW3Xq3DHZK2zd97OfaM1KFnCY9gB-xu0WC_Z8gFC9lsrXTqFGrKBwAMJaGifkbkAelfpHGy1fsQobNYvXncTyZExYyNMNVNH-iy4irdhRZjGvzY7FMuF9_70mog5Qiiwglf5KLYr4A0rDuuHN5L9rvUb5IiE0C4FhYVEBCYJH2irYX_Lni1UTt_cR9pALIvdlUon5fwwGE3YWEnAcglC0IlbOGxEhVj0y2tY46O_jGf7tRhH7ClNR8fj_Hv8uq5lc9pcUsgRrKX4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ گزینه دوم باشگاه پرسپولیس برای سکان هدایت سرخ پوشان مهدی مهدوی کیا اسطوره سرخ پوشانه که مدیریت باشگاه پیشنهادی سه ساله با دو دستیار خارجی به ایشان داده است. مهدی مهدوی‌کیا از مدیریت بانک شهر حدود یک هفته زمان خواسته تا پاسخ بدهد.…</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/24974" target="_blank">📅 00:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24973">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQF29x9BZLL9whFSCICuEmRvveUiXs27USGSJ-okyTeBD2MD396kwxdsGhPMc33AEeOXjdu4qL17TJEUpiK4avQDMG0bijZHMEnnx1LKiMuPpEL-wGUAp3Frf0iiBbekh1cJSCbisTrcex0bnFqO7ZIRggPU2FozRH4CQ88G_Mk1b_JmuVHu6HrxHvBs3leRNe7p2qGNZHZcYon1LU7qWjI-aZ_YmrpEHLnAW30nKirRdArT4xHj00zqYTm26cI-_igPpLSAdjabmiyAPZm4aGUYaPipuze-JaCx2htFRZyMWSXJChwsnuQ-zSGohoco9nrN_cHx23J7WkMCoGGYug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دیدارها‌ی‌‌ امروز؛
از مصاف فرانسوی‌ها با پاراگوئه تا نبرد تماشایی سلسائو برابر یاران هالند
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/24973" target="_blank">📅 00:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24972">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfmMAhSUF7zR3pkY3VqRwe58T4QYB1Vo--1WYw2wyq_IomyNempSrJLufl1Vw1BYInu5m3BZfe7KoD7MCrjej-bAISZxQNDoijbF1vTVVQEyFlaQonz2m9Y-HEdwXSpwxkIxb49OvxPCCA_Ls3uPmHIf3Wyn-Azh_rqBK720yP0dA5LEYqkAEVNDyrPQ6lD6BA292RuhRN4Mbbo68qXKtuDFOXxw-5mMhRuHRbgi6U7RZYsBrUrZFYfcycXkGIpFSmOqWJLo5ad5fQILgA8rq_hhZKFqhK_Nvwz6GcLZRMQ04TydYf8iE_V3_z49a3yE01OG2zVbjN9bGho0JzyF7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
صعود دشوار و نفس گیر یاران لیونل مسی در دیداری تماشایی مقابل کیپ‌ ورد و برد قاطعانه مراکشی‌ها برابر کانادا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/24972" target="_blank">📅 00:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24969">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NnslMDKrIH_7uL6yecTN4WsiB8eFN-Wh08mHutpWHeZxm8kjcsPw1fmZq3qUK8LonORGUspBeCWBsmG379c4JY_zcjlqN4soqmUaVxtz__Q51X_biCOeorRkraosoXkowz3jl9j-qV2W7fQP5W3BFBXP6Eu3h5RuMO9kSENB56725bJlkAORwdJqkTeV2Q6GWpinE3iYQvW9nTD_2KjjaoCYWB0znowQHAUH42ECKAhWl6Y-6MUFQxPEB-gJByj1vAflrZgejiFyz4f5t9NpOTFZmu96aW4PIYhbZhziNwxAtau2E2SlGpDtuZDR4pfN1GLvIhc3P1hX0ZvkXz0h9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الاهلی عربستان؛
ریاض محرز ستاره 35 ساله تیم‌ملی الجزایر از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/24969" target="_blank">📅 00:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24968">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/imbbAIuoGZU85Y1rLqoHJu599L39o4jLYkxdP5TNSDD6kk9MoH4Z_0YfJunTfwaJoOp8Bc72m7KfOqqqHJTGckhB25zliG9XGh37w1Ckjzv6Gn9LOiohTWtINi6JqeC6mq4k4DqeMY3_FHHUmC4iHCU66TtBMJWuTJGzaeLRzROOsVgPgMSi05cW1gjOQ94jiaNLBU8u_Q2O3sG_oeacYGbdVHKipfrgC4uw9gMo-zxkrZLBPRO9P3Zj4BrK69_XGnWY-sTHbH2b767dlf-i3_6Ylm2KBBplza_d4h8kvaDHOC2y0-oqFh9PUUQs2n7Rnh4Dgx5lmKTz3fCwKR0Jsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌دوگزینه‌داخلی برای سکان هدایت سرخ‌ ها در فصل جدید مدنظر داره که سعی میکنیم اطلاعات دقیق و کامل درباره این دو گزینه بدست بیاریم و امشب یا فردا شب بهش بپردازیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/24968" target="_blank">📅 00:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24966">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJHppuWboTMQ5MjVxel-4Hpzu3Is80g9Q8NFBpuzkFMlXCWb1KCyK8rzcTeFyYzxJbabCvaNeg5RBQZdEC3mdAN258L6Jnb-t6AAbTE0oxu4PTBHIA7e05nXRJs8rFovb8aYwqIdzbR77Ae5Dje2jA9Mv9ILrhXqzBdtuGOGUMaWwNRXrFTFyHNCzObLSUmidSk5dc5f5kDWfmqH-LIyxf5zJJOngKR3B9VrI6bkq80IzqLh2ee6r-E1sCQfia9ri3KMufFBDERAEEDeABQ00yzeR6mOG98cUo7vlf1VNc_Qr6poxZ6sv7xGiHXIIRMsSB9GvOuFKGnmpMXhTK6lBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه گلگهر سیرجان که اخیرا قرارداد مهدی تارتار رو تمدید کرد بندی در قراردادش گنجانده شده درصورتیکه باشگاه پرسپولیس این سرمربی رو بخواهد با پرداخت 20 میلیارد تومان رضایت نامه تارتار صادر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/24966" target="_blank">📅 00:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24965">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/de5oaQws0R276ApFdsUohd85_KfKK5TEKmgHpH2xE6UF5RnYwGgbH_FYRcp9uZIjiUk6lK6fA6GquLu3emrFKEebVsasTxH3cVz1KhRoxgj7sc3DayAoAXMN8NQ76xJkrfh1854ZQKFIwTB-OEaUl6SQ7DIO0Bcinc8_5dN5_ka4_ZjNQI6-rgJiSxlZtrgbuZiqK4FjmJWmXryQ7dPXEsxUsRD_yHnBTRCOxif97fw-TFQZCl26tOQaC5zeVOpFE3Mxkb3kEwliWNoxWUJzXqVeB9DC-W7zYC7pICpjQ2XTUd5-WjiSqxn_nTx2Szq7b_70eGFg8pVSojf7mxft3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛باشگاه‌استقلال برای جذب دانیال ایری پیشنهاد فروش عارف غلامی، محمدرضاآزادی + 30 میلیارد تومان به نساجی داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/24965" target="_blank">📅 23:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24964">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rh41dAKCju0zmxc2rZqUK2o2iBzDYWB_6v8yJX8sN7jm2KMPcbVamjXwvLBftuufTy8wH9vfEQUZfhmkdkFDs8HqXQgayaCyrbsGJ87OZdLTiz0FuXmKdeOJvoy_6Fox5K4IE4-g9DAvwlX8aTORL9DR96n7p6M3C3-2wPIEY6W6wCZUGGWFMJjJdWFvzPsQ1soFhYxDvm3iLTtZtEj1KruVEUMICBSBGYSgz-sIYyVbhwErHo5HjWkntlmH1HuXIkDOjC3263-p2xK9b_bBnjRA3HeJ2r7u-Hrv_ApmHoITAvzmAtEPeAJeFleOQ9KfQvbucPNDR4z523uzIXrpug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
💰
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس با ارسال نامه‌ای به باشگاه نساجی رسما خواستار جذب دانیال‌ایری مدافع‌ملی پوش 21 ساله این‌باشگاه‌شده‌است. سرخپوشان به مدیریت نساجی اعلام کرده که 90 میلیارد زیاده و تا 55 میلیارد ما حاضریم برای رضایت نامه ایری هزینه…</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/24964" target="_blank">📅 23:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24963">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcFOFC_WhlkjFacVaBwexT-hgbKrv8bXwJvlN25SSwEKO9ZBOXZkck6m2HSjeWmuchNTW2n7LHWpTRqwxFRomzpnTiRU_ZXhJqxsiu6GYvppPp-14WUv-STwFrDMm988gk2FcON5y7pwwu1sRyD02H0NbvMzGI8Yl65gJiYPFX9qRbuxxdvhSeXxgMzxYdqLZu5FTPK4kLFVNQAfHRvjkcNY0jaCxGC-7ake8zbL8SCjMzjU-3jViZ2ufOO-_FcM91gZi_WXgyWvwqe2zrgekGFIpZq5iMExJQvgcw8E_Y68mfQD3SeVf8B7Kxat-cyMeRU3sBwIOZYkASKQb-4X9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
در بازی شب گذشته؛ این هوادار آرژانتین کیتش رو میندازه برا لیساندرو مارتینز که براش امضا کنه، مارتینز هم کیت رو برمیداره و با خودش میبره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/24963" target="_blank">📅 22:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24962">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXAayia2xIOz6nj4hDndZEl9eExpAkgPduRT8_IqOBSfzMOZR8S-OVAFLfT_Y_DBrytaSkNEueOfDsqX-puYm7nBVxKfjO46ZBt16R16H4Nw4_5Z63y5EU4Arw1xI0QCvIs6NahgW_miaVt0mSzX5LkDyUHJ7CE4LVt_B6OTff_fq_xpdHqqFcr0G4J5JjgxsEcaUdQ1Nr-PpweSYioluxa1hpUMuOKxhy6TSlquWV7DS5v56Irt_ZnsjPc4XO20Q0JW8F4lkCuXDKCJeA9t-fYZyvF4TwiapXzpqGdM6A4WJO-iN_pLpRAa5pgNvuAEA6JzNybw_9Wmgy5ITIBJ7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک هشتم نهایی جام‌جهانی؛
پیروزی ارزشمند و شیرین یاران اشرف حکیمی مقابل کانادای میزبان و صعود تاریخی به یک چهارم نهایی رقابت‌ها.
🇲🇦
مراکش
3️⃣
-
0️⃣
کانادا
🇨🇦
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/24962" target="_blank">📅 22:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24961">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQQK1-tert70cgn72dv2N53SdyIP-cMP5aFIzuJ7WCkXjoIXzT0qBwzJvkZ11-bjL80qI_iZ5YEhrfuRWe140wC3HWX2-Agc0UiIQaih9n0QHDN-y6XwEJ4eC8ixHR4N5n7krDIVs9jc2ekO-xa6A2BSFwrUdQjuPvCdV6aKtDIx0dH_37qSxOC4loFN_ACSQ0dFYyKjNirAJNEqPOwVU_dCFBG6LWnEx-rCwRkV1Zxo7XDyN1ZDvbLLPP6e9tE_ienlBv7Bk9AUvKNrtRH9egXDObmBpPcUqCn02ISynSuBVrzHDJpCfzE1aPYSDtKq482nyqXgyh4JmVNWDLPOzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/24961" target="_blank">📅 22:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24960">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nd2abgD5V_cdMVOmxZOuZrNCtWj_wPnnicV9L7G--j793PG_D6PNm-WmgCWX9aka-0La0sSpjRdcboTdHeRV96FEUtQsftMKlXwjszSiqovtQvwHsNcQhcxc613epuneI1-qTD9SJ-vZZ1-2A_1uu5LJI3wEYjpFqJ0NyRn-GbrPwZyaDR0IaAV7K4OuJddnWfXvhCjNzMFWH9HFECu6GjQV6G5NpxbUjgR8_D7B5bV3QJ6uhagBFY5znUbDfQaaHR1zGGdMcEaQmXZ2oViaThanLsG6O8gVavM3oHKuSlqajmz6Gz3Gfhpv7WhmhBpDP-GdtqxLoiICS0kR10dJnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هروه رنار سرمربی مراکشی تونس بعد از دوباره از عقد قراردادش از این تیم جداشد و در حال حاضر سرمربی آزاد بشمار می‌آید. کاش بشه ایران آوردش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/24960" target="_blank">📅 21:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24959">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQuY06DaXgo9xMqRdOoBDi4z7HuAQcN5XVC9Gb-O3eXIPos7qjIxEn2N9Ox_lnnSQr_Ht49vCwuQaPMFcW2gFrzydFYMqXyR4BJqDYqyL3DRGaDIQ6a3gvKZxt2_yv-d-EV_i_paaeKjpoSZSfPyglbnqfHQ_xU6iQ94gU_GZayIb1gw_McXCPP9ZpDX0Pxlfl4F5KTN3m9vVdaQVbAgCVihNMRtYUB29UG2vRqVSXp3r4xug9y5Go4pkcMnEJgAT-tZh8ZinDM8wNFM9umuHQ9qW-KTeamLaGu9GDi5GDN2lAGe_YBoDYsFiux1PopeC7qARDpbcq3nVJSrPh9QLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇮🇹
🇧🇷
بااعلام رسانه‌های برزیلی؛
کارلو آنجلوتی تصمیم گرفته بجای پاکتا مصدوم نیمار جونیور رو در بازی‌فرداشب‌مقابل نروژ فیکس کنه. نیمار در تمرینات روزهای اخیر با انگیزه بسیار بالایی حضور داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/24959" target="_blank">📅 21:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24958">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUyU3yjKi8DTEy8YPcPgnhKMeMawPcvxRvoibBx2vWF0RbReJlDkAQlY7iOjHtosDm2WujUkzaj0YdVc78gdy5Apzd-S8fj7AB9U1Wih7TRf3o6LvFFqja2W4IjYsO09b9dQWVknr5WsJGCUbQFUK2mPKLMmiyQgigw4GFl3uiCnaO0is4hmye75nchjblMiM61fFD-CSO5E6624wtrBBRdimXahC9pWDGB3jJMk9RJrGeAJZpJfLw1j7U2EHQyJj_c6tGD18HGsvqIai5F78D861vCQUu27F3OFFWlGmDFx_KYKH3n6IngwNnezUjLkkpr_43PseQkelDoXdpv6hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
منیر الحدادی ستاره مراکشی استقلال امشب در تماس علی‌ تاجرنیا رئیس‌هیات مدیره استقلال اعلام کرده تا روز شنبه با خانواده‌اش به تهران باز خواهد گشت و به تمرینات آبی ها اضافه خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/24958" target="_blank">📅 20:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24957">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmIVsVQezodMhynyY2tEXWGk8EN9Nt7Dbvn-tHWe48bJRFpbXFZT6ahtNL02ZsMsoTt4AsX7uz8jhXr21obluYJClh3BRMIOwFXf9nqieK_8E1S4R7zj5bAkGztlFGHuChqKatDE2YLQXylPxfCRfOBIDFLMTAYiKs0TXzdW_iYikGe185Dj8GMn-tL_KDbwmfwCwl1iICETF4w2p5L1vvFrAMwLEdVa2SUyL0MfHB5kjKwbgeYWPadbt9-9luQBE_HBlJVhBVTmusrMhGp-OarHyO44KSVGlxFtvIuVgkKNyI05B1o_m5GmZUhLUU-k0iGkHzDMGYMANUc-d5RoUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی حین بازی آرژانتین
🆚
کیپ ورد لایو گذاشته‌ومیگه‌کار یاران لیونل مسی امشب تمومه و حذف میشن. بازی تا پایان 90 دقیقه یک بر یک در جریان است و بازی رفت وقت‌های اضافی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/24957" target="_blank">📅 19:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24956">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWYKvaDc9dbY12PlC4hDSs6onoeygmOdAUbxULQuphPszoe84Xt3hmiV6aSrBv9wKcxJjoOEcX7LLpVa6Eklgtg0zgX8FG3Ys2lFVm8pcGcfH04pnnlF-8Ix375qVsS7aMvGMcrjJgmcdL6amBGr0gIh7ByIvhJbdoqBY-Wmc75YaUcwtBYBMjNXqYz2e_uCU56Sv_pDTQuDLEOrW5G8YAVO-CVX7qJlTjqvH1YHL_nXSqFeO0ZrbeH39jXU7F_QiNId211HBobah2vASgjxbi0IRH7PVkEfqQdkatMoxL8MUs8PHMzs9_WT5w789gWJ3AIMvUAT8L7XB8N4hlDEQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول‌گلزنان برتر جام‌جهانی در پایان مرحله یک شانزدهم این‌مسابقات؛ لئو مسی با اختلاف در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/24956" target="_blank">📅 19:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24955">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‼️
خودزنی‌خداداد‌عزیزی روی برنامه زنده جام جهانی از دست جواد خیابانی ؛ میگه اگه زنوزی اینجا نمیبود همین‌الان برنامه رو ترک میکردم و به ارواح خاک پدرم دیگر به‌برنامه برنمیگشتم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/24955" target="_blank">📅 19:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24954">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ulspD1owsBONscFrqEvdM2hfIPuQxtEEL8zdI0m4WVIUNYTWUp_99tjHWiw0eHSosfuwf5is6v_VdmIDqjticXQUb-ie0_nyIZo96dWAG-Arep4imbqW8TkgDEYsXM3Ss4epmZrIrtWXE3sZfxsb0-KCV4IlQKEsa_0eH32pZ94VLTyQ-EZpzbIkhy0cPzeJ9D67Nk51h7sObByiYrA3qCHSO5EcEQ7mCjU0fcoEPXE5v00tFCn9j6aq3HNWNL4ympBZM6qDVgRceROhTwchQq9V2lUDsbG-CYHDbt9ckBKxb_vsqI_KItEjrkjMneZT-8AN2G_qJ6JvCedwFV2GLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
مراکش
🆚
کانادا
🇨🇦
فکر می‌کنید کدام تیم برنده این دیدار خواهد شد؟ رأی خود را ثبت کنید و اگر پیش‌بینی شما با نتیجه نهایی مسابقه مطابقت داشته باشد، در تقسیم جایزه
۱۰۰۰ دلاری
بین برندگان واجد شرایط شرکت خواهید کرد.
💰
جایزه به صورت مساوی و مطابق قوانین و شرایط سایت، بین تمامی شرکت‌کنندگانی که پیش‌بینی صحیح ثبت کرده باشند، توزیع خواهد شد.
⏰
مهلت ثبت پیش‌بینی: تا قبل از شروع مسابقه
👇
انتخاب شما چیست؟
🇲🇦
مراکش
🇨🇦
کانادا
شركت در قرعه كشي:
Https://t.me/betegramd
📺
پخش زنده بدون سانسور در کانال تلگرام
🚀
برای تماشای مسابقه و ثبت پیش‌بینی، به کانال تلگرام ما بپیوندید
عضويت در كانال
Https://t.me/betegram_official</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/24954" target="_blank">📅 19:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24953">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S9_abFBGN5zXyBDCh9-SbGbfkVdDIekLG19hbk4RIFxV53_Wp2hTPsuDQVox_fk54K9dTwhqEbm3-3XAwSlBHqqOE7bMQJGGVzxakIx4cY_KHX4HvjNDLOtQFhkFr0cdK7DDBCKTWrZGs1EpVoAGtM8-TL7RiMz24calrXLrEhi2oeqwRs0nQpA1jqBzt7s3Ng0r6YcqIbqi5caCKPASKOed9m1nlH4J7VGtlA2980Fxlzw7azfarsSnx6K2L-MkzIvuE0nWwiJp1u6wx6Z6mWTeW886lZA4kRPnc9QCC02qzsEEdA8dHX5I28ZB39MoRPjpXuVRHYqYCewGSQjSzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/24953" target="_blank">📅 18:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24952">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyllyOWzyWLPuqBcjsyobrnCu0FGCEM4EHezMAtMFot_UAZRS72Bt74wUy_WbkIh9FHYgy3VhUoeLsLJgh4RQKqr35KKbr2qBrdVIw9eFWMlljfCrUIymUdu5JlHg4Q2f3zI0_766cD-VaIpnJq1kEcIxi_XHSn1Wo10D8QPUCaebe0p9sO_bEC4CNOIHL-K7ukAtSKBrWlHz2oUarAF74csZE9a-2S5qeMbKmwoshqDgT58jsXQtvVx6YPky3u_e5PTpmKGftYXSupJCYOgELPlVLpHQlYwrPyrgtEqYD6Q8MrBbT7kAKr6kWsWjuojr46YsOHLjSEUmzRC8W3Pdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وزینیا ۴۰ ساله در جام‌جهانی ۲۰۲۶: ‏۴ بازی، ‏۲۳ شوت مهارشده،۱۸سیو، ‏۷۸.۳٪ درصد سیو؛ مردی که ۲۵ سالگی وارد فوتبال شد و از رانندگی اتوبوس و برقکاری رسید بدرخشش مقابل‌آرژانتین و اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/24952" target="_blank">📅 18:30 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
