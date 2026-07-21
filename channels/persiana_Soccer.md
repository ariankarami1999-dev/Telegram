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
<img src="https://cdn4.telesco.pe/file/toKjM-XBPhDFdEauepOrDFZtFiRmSSKY1Ia73S-DVUMkT8h6XVwtNbqIREdD9ppRQZ3SPvv30rj0u5TK7xx13gX5Ew3ksiYYYoxUIS8FiPZK56nOLcSzDIxBQq1eYmZYPpGk0PrERePBGh2US24sunf28O4B_QfVoNmDLgEOnjFm9WDCwl8YACgjInKkX3GIOJGBs6vdHzl8gTtgZCjKuS-Y0lKPOrqT2BbGvNbT_0IZbe8fzmOsoSw08enfUGpE6GdNhr6Ju1DJibp286LdYws3igD4LfQq8B1pdm0flYe4C4lkp20SsT3fdRlFZLKFvU7jjUBjCS7NbV1mG37SZQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 528K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 18:01:04</div>
<hr>

<div class="tg-post" id="msg-26230">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/keaqzuBCRk3rm51hC_ZkvZpYbrZvbQtSrCiI5K7phSvpKOKzgiBOPNdr2vnkP1BVeVo2ZhlLEg5jq877HRMVM6DVQO5IPzZMx9N9AoclI6pj5OlQlkMNTN8a3-x5cxkRF9iAn8yGUEWv0kIJFBDj7vTFjsZc6w4do_2u9Xj8S1Xk1_ArQd-vxe2FA0pay6FUIzB5OWkFagAPc8d8MmuABgfcHvmK-XKZjWwx_3E2gFf_qixenuRhqN7UgsAP3xyGDh8p5O16mt-9cVtQyKsjSt5-0gASqKWGvy1WLIGKT11Q5fW1UEhsFJ4niCOvJS0RNQcQ6aOYDnR-3StaoBPo0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بهترین گلر شش دوره‌اخیر جام جهانی؛ بوفون، کاسیاس، نویر، تیبو کورتوا، مارتینز و اونای سیمون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/persiana_Soccer/26230" target="_blank">📅 17:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26229">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fV8tnVDWoHBR9qW8VAENrC08hNM1RVcRripU6rpb7mVZ9GBNjADX1fR8un11hKi9-nC-4z3To3CYhEQjLbl_1a6TbC8cot8ah-B1O1F5YjJvlosJ-MTU0CtwKNPDSBuZUlcDn6HWvEtLj6HJCLcXJntcVkUzwZrr03qzJf0PeaI-7LfKEbR53Gc0PahKwPNWF74rA73mQKVErUfucUlkZubp36gHgAeOzMM7tbpUKal1I5B4nfnTv5f-CeP1tUzxYbp_6_kFSZFD1P3NXlBxtb1QrSiYjM17L8JVDECO6rFsDH3T0XqC4X6pt0EIb6ulX-qPz0WW_XxAlqBWTMeslQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت رده‌بندی فیفا پس از جام جهانی؛ سقوط ایران و صعود اسپانیایی‌ها در رنکینگ بندی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/persiana_Soccer/26229" target="_blank">📅 17:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26228">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3639cfb2fe.mp4?token=gqe0bIzUePT0JkCEtDj2Dgub3FpmqP9WeS4pC-dqyPp16n3ki_pUwC0drl-5dokzY7u5HmC96wHT3XdgZvcdhfLPs-qOLSMwE1AsORDyh8EDZJIdIbTNwebJpJTDFekLsULvzEJT6NHjEfG4b3cwIOlWLHg8_p5ocAKrVvlB3dxzMVehWE60p7a4hjhvOOU6jYDDQMzu87VCxZ-xY7yD5EBLVrpVqSnXy7YK6lVxCfPv7ommgp9ltXK5_B8Bq0JEjyVN9aUcNKKlRE6KTL_zKhcdKdd2BVmlXeINoVS9SUzbRi0R6fynLDjBKKHet91YPGwVMoU7vTK66cCx5X-LPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3639cfb2fe.mp4?token=gqe0bIzUePT0JkCEtDj2Dgub3FpmqP9WeS4pC-dqyPp16n3ki_pUwC0drl-5dokzY7u5HmC96wHT3XdgZvcdhfLPs-qOLSMwE1AsORDyh8EDZJIdIbTNwebJpJTDFekLsULvzEJT6NHjEfG4b3cwIOlWLHg8_p5ocAKrVvlB3dxzMVehWE60p7a4hjhvOOU6jYDDQMzu87VCxZ-xY7yD5EBLVrpVqSnXy7YK6lVxCfPv7ommgp9ltXK5_B8Bq0JEjyVN9aUcNKKlRE6KTL_zKhcdKdd2BVmlXeINoVS9SUzbRi0R6fynLDjBKKHet91YPGwVMoU7vTK66cCx5X-LPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بعضی‌صحنه‌هاگل‌نیستن امابه‌اندازه یه قهرمانی ارزش دارن. دفع‌توپ‌کوبارسی تو دقیقه ۱۲۰ از همون لحظه‌ها بود؛ جایی که با یه اشتباه می‌تونست گل به خودی بزنه یا پنالتی بده، اما با خونسردی کامل توپ رو بیرون کشید. این فقط دفاع نیست، یه اثر هنریه.
و یادمون نره؛ فقط ۱۹ سالشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/persiana_Soccer/26228" target="_blank">📅 17:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26227">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ec8c45572.mp4?token=d8z8IdSsPjZ_bV9X83-7L0UvIi0U9Tmrt0_axbqZvqoEnIdrLPqbpTKbH8Z8jHdypK4oiuENh7hpNEpPgPby4M8hvGdZGuuRUNPn0bccjELYWC7OjBAVHvRXq3SJra690ZJLFsPCvf_J_R9iojTWg_-9AygnNY8iX8BhaTB9jCf1WctQnAsNkmT8M9bbrCCa7oSW85E_O3EtXnsq_ZZFrq0ifAhQyt9E9aSiq4fhrlXTtpP9yQwz64wb06If7u8w0_5fxqQ2rXhYJJ-SgZvC4KUqjZD6MN8OM3E7BMAQPkpNgkISQA2WUT72RB5JnwhRsg8ebajiDLN44io0WwzfcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ec8c45572.mp4?token=d8z8IdSsPjZ_bV9X83-7L0UvIi0U9Tmrt0_axbqZvqoEnIdrLPqbpTKbH8Z8jHdypK4oiuENh7hpNEpPgPby4M8hvGdZGuuRUNPn0bccjELYWC7OjBAVHvRXq3SJra690ZJLFsPCvf_J_R9iojTWg_-9AygnNY8iX8BhaTB9jCf1WctQnAsNkmT8M9bbrCCa7oSW85E_O3EtXnsq_ZZFrq0ifAhQyt9E9aSiq4fhrlXTtpP9yQwz64wb06If7u8w0_5fxqQ2rXhYJJ-SgZvC4KUqjZD6MN8OM3E7BMAQPkpNgkISQA2WUT72RB5JnwhRsg8ebajiDLN44io0WwzfcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حرکات عجیب لامین یامال ستاره 19 ساله تیم اسپانیا درجشن‌قهرمانی‌شب‌گذشته؛ چرا یهو کشیدی پایین؟ یه‌درصدتوپ‌طلابگیری میخوای چیکار کنی؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/persiana_Soccer/26227" target="_blank">📅 17:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26226">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqA5-_1a2UUXEAqsbUKLdSDLOkvyiseDzqk_dXW6XA4eTfauHKVIY5Hqp5wEVqnvi9fT_9n3eu_Ail_d_rNKkLDGXCoPUPFawODGLWKaJZ1b9mIwul34Si3jDmGqPTJjLtHm7i6JZRhT86wQFCOeIY_WIS694v0nGf7CGpoBQXJnR4uZkNAoyJEYtGnT1RtCTS3VEE6HEQz2IMTC8PBF-fHcYOlA7BnzSXjt5Nr4nkrZDvgeBvL8w19dBz_zFQCcgl7lYUbX5nZ5hhEsgeSw3zmJHwx7616Fi_oKhjKYu7KgnJyGF-UslDCJXMH8yHh2Ar7rk7hhHLnpq7V6svh3ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐉
میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال
Evil Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی
👍
آدرس عضویت کانال vip:
https://t.me/+TmGWkUYH_8c0OWZk
https://t.me/+TmGWkUYH_8c0OWZk</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/persiana_Soccer/26226" target="_blank">📅 17:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26225">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8b008c54e.mp4?token=ZI0Wxj3hkBYpPmb5OcN-w10mt5k5jit0JrNNiggcN3MC_4ukxV34PRQuFmjIkdqBWmsj2sUYSA7N7V1bXT67OEz1byYp-TYUp7UYPQbK5z2EL9wsifb_VCJvYh2jzW2UkNkil5E2c1wBsaJL-Ef6dwOhX-6Nv383zK39cuHh59mfX2gNN8sFZrjifIPvZxZ49DR2_Qk49o98E73ecID2qPIu-IH5KOAYI7RsMMcUk6lFSoPwHY2xbv_V5T1PanmxkQtAfd5GEc8e6sd1ZA4J8HvU06MHVjZSWMwkHy-KINDBB37LVPrwtddUpPbdlBboAICgBmyXL1O_hRmCq8TO8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8b008c54e.mp4?token=ZI0Wxj3hkBYpPmb5OcN-w10mt5k5jit0JrNNiggcN3MC_4ukxV34PRQuFmjIkdqBWmsj2sUYSA7N7V1bXT67OEz1byYp-TYUp7UYPQbK5z2EL9wsifb_VCJvYh2jzW2UkNkil5E2c1wBsaJL-Ef6dwOhX-6Nv383zK39cuHh59mfX2gNN8sFZrjifIPvZxZ49DR2_Qk49o98E73ecID2qPIu-IH5KOAYI7RsMMcUk6lFSoPwHY2xbv_V5T1PanmxkQtAfd5GEc8e6sd1ZA4J8HvU06MHVjZSWMwkHy-KINDBB37LVPrwtddUpPbdlBboAICgBmyXL1O_hRmCq8TO8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
#تکمیلی؛قرارداد محمد خلیفه دروازه‌بان 21 ساله جدید استقلال پنج‌ساله امضا شده است. باشگاه بزودی پوستر رونمایی از خلیفه رو منتشر میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/persiana_Soccer/26225" target="_blank">📅 17:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26224">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgGRecqPvkEfSA2uARHdVgQCy3Zu6tTVom70i6jrON1DoOtChpxS4tJCC0V5v9KsoiexePBFsXAaK7_yhy0QuLjPpOUdGr2llPUWu3ic-OsvEW9e3mNUMJliYqC9Ac0pM4_mqdsPOC7xXpGqms3oWbENquwz9syStdoom1k7sl9cGJgre105TRG5UcQ1-pprMZrasfnOhN5FW8o9oJ9B-4Er4UvNji2y6_FCEtjFF8FwO2se3M0Iyf5Y0pmQRSWuGI8FYAVaNqbevAfQj8p0r1fe8KkjYxy940wiVrkq9z27NWH-zzHEpfrVfFz2D7iclqpblkUtsHwRSKXo-Csceg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
◽️
👤
#تکمیلی؛طبق‌شنیده‌های‌رسانه پرشیانا؛ مجتبی حسینی سرمربی سابق‌تیم آلومینیوم اراک که در روزهای گذشته مذاکرات مثبتی رو با مدیران فجر سپاسی داشت. امشب بعد از جدایی رضا عنایتی از نساجی مدیریت این تیم با او تماس گرفته و صحبت‌ های مفصلی رو با او داشته. حسینی…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/26224" target="_blank">📅 16:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26222">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t6Eerm4-BOZlhrUvDhEMXBp5De-FHtxjzsASfgxFb9t2Q42vZyES46yB71M2mnk6a6KEsdbiNs_yONekXTBFensFY3K-mPsRtUIqtkN236Pwh-uS5XEaNguGwhfD6IW-_lMaT_owUjbvhLFeWndZ5S97yAOM7j_1Fy7l34ltpPoZXl62ajfOI1EY9X2UZYmqM_3EJu8j4AEUsZLL2KIWo4yPWBajF1N_PRsxiNERM7T_oZNGTXxY8bQWQR27zPX-AVaKad8XLmuQTUQ5Bh8gWbofDbjw8jOGd7WGL9qZEB44Dg_44UJ8FuqzJl-_CTsR51JnnXPHIX1Up7fUakLEcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/afv1KEPeobz2-6_LwYbXHnUuB6kdjz4rGKzqOOUICG6VaTy6B0xXHA8stYDzqOfbFUyp9g5s5rZ3FKURJVTpKWZL6sWyDgveZvP9wL8nyoYbUG4FjCHrCunkC_Yvep-1jJj8Owpqo7SbfkWSZqonnHBf80SEq39aZlQWveNJWCSmAGE121y80irkWcMYkaFh3_qLEVnh1D4zjyNPLPPoNOuFXRMdmE9oWZAiqDf7euRSBH9MzLwUX01WgwcIbLDcf6mSK_OCdvbN-Zrhv-esKpu0ZR7mOSD4DoQjAAzF0wBZL51znoRfcebITH50g0Hj0jM0aknJYgkj_DliO5AboQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
خواننده‌های جشن قهرمانی تیم ملی اسپانیا بعد از موفقیت در تورنمنت بزرگ و ارزشمند جام جهانی.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/persiana_Soccer/26222" target="_blank">📅 16:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26221">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEH1oAVtARzS5gez9pVVM5qkk7NB670GOryxtG_Nii5bFfkpk4S4_HEcXEg9VsKN0T6DNXZuJgrcc6ErZR2Pw8BiGcqU40M5tyBMmV_mYEvJ_6PeZ0OwKDNBBonytDCUgRHKy8y2U-d9ByocAKlOlC_cdapH79mg5OhS1ybMVGLY-UspGTgyppzkTiq82iuuE7F8fvcgLuNhva85atypNJ7COVDZ4zchf2YmJM_IQCHg_-tBZX-rzv4_LO7zE8Te-ujG2ifrSl55mcyQWXaKaRSujZkCRC-N4NDL4LIdXCJKZym43wZ2I1NYbyoudfKtfE9cTNWvzXOBv7-f8DE1xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/persiana_Soccer/26221" target="_blank">📅 16:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26220">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HndLgVCLy5P_TjJAHm4xxjZaGF1D_Cn1RpjQWQ0gAOzs-lAJu0LYIukvWbRJwnJy4lx3LQM6Rn5Igx0KL3wzkh0D9qBuiAVDcgFnVRjuWBjdleT4rQWl06F5LAL0ZLfNvXr5svfPkBdMmv9jPEC4sQV6jX1WM_u0od2rFNetATE6BzzuX05xqI3z9zSUFzfRIf9t7kxandAiduL_vwHz6OrTasmRgQ4KQXkJu3IAMOdqAZJHJfhtoyGETG2F_36XxoDhac_uE4hDyGzO-u_glPcwqiW71WC4aJgbjU0mq2kIeMOpYZKCEA3ZqsJQEOWtUC7sU97IqU1geL3iEJvKqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
درحالی که با قهرمانی اسپانیا هیچ گزینه قاطعی برای کسب توپ طلا دیده نمیشود ، فرانس فوتبال در آخرین‌آپدیت‌خود درماه آپریل "عملکرد فردی در تمام مسابقات بزرگ و مهم" را جزو ملاک‌های مهم انتخاب برنده توپ طلا در سال جاری اعلام کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/26220" target="_blank">📅 16:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26219">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0BmT6gWhBnRVDVnAMLO0DAYSJR7jLThJW67978r-PCDl_FQASxYYwpe6-rSKrtE6MDUxsGBwUdAIF3HFa2MpzjowEe1YSW4Te3QqIyvyL0D88pi3rtJRNXp6W-VIQwzoRTMvU4bezZixBAQzOTZOcHMKPo23b0SfWpwxe3qvviZvI1_HSVxhU1kIkOpdKZcNJaTxmfhdbpFJiRkL-U1Tj_Y1gnrxgqjQtkHNsdfzJjc0H8xafcDXfn58H636TeoPajVsXNZgnLVyFWrIRm5wdzQNftMRTzHnaHkTnzOro6JqNJEhqKn74Ul0ddhlgnZi8xhJZiqRZpbHaQnyNwkWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رقابت‌های‌جام‌جهانی 2026 با 655 میلیون دلار جایزه نقدی، گران‌ترین دوره درتاریخ‌فوتبال شد. 50 میلیون دلار از این جایزه روفقط اسپانیایی‌ها بردن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/26219" target="_blank">📅 16:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26218">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFmpKLhRCH-49FlAgbyfcMTAE15LgubTPEX7qQZUOIBuLTO6yInG687WWeZlteiKiSXy3JruLHnx42HyJQUmuXNRIbzorH3_3Tx_TI1k8gd6ZWY6RnvA-MS5AIVyUFiN4e2l9-Z8VFppN6aPvi37U5LWRzwGdLnp7QC-k2OuAGWjvrBpS4GJyCiFiXeO_KkOuxKs8bTcWpHiucDHWAEIOSeqgJRTZd0OUcYTM0kd1VVcFLj1mW3e1iQxj6_VH4Gke7B3o7glihr43UEWv-t1SlD_A0UZ6ev2SY6WE0TYxLEaSjxd6aEnJAHlNrTdkrFfMOVLYv3A1TjH27uMaU6wGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
محرم نوید کیا سرمربی سپاهان؛ علی کریمی هافبک 32 ساله طلایی‌پوشان زاینده‌رود رو در لیست مازاد این تیم قرار داد و کریمی به زودی با حضور در ساختمان باشگاه قراردادش رو فسخ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/26218" target="_blank">📅 15:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26214">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/klYgDuWf4OusW5KzWZ0QBFSwiIU9Rx6BL9x3gYiBReF9Xzb3s0Xy8ybQVOqPrCWXpO7ccvlKPwOlpSd5X4JTNis9vWYjQ_h9cPQdAL4Gg5ltkOI3yZEZXTcvwIS9kbPgT9aDKXpX_JQEatxSTLDs6jcF0jaLg-BkDxO_pvQVKMEGVxi3QvH-yY5FPRUlrWxQ5M1xjOsjmHTKsl_SUDCq8h36SLtQ2RwWQ9q7R-ou-qGJhXFPwqm8aXtXZy2_EmF3og-o6P5TIdQ4oK3UxJ_QLNcevLuUhNMe3DuL6o3IYf-JgU6MR7rdAAYLVWNdbOGOpZQqd6Z24r-muNxp1v0uZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوری؛ رودری فوق ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی که بعنوان بهترین بازیکن جام جهانی 2026 انتخاب شد آمادگی خود را برای عقدقرارداد چهار ساله با رئال مادرید اعلام کرده و به نزدیکانش گفته پرز بخواد میاد رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/26214" target="_blank">📅 15:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26213">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scgutJYuS7zOAPOeEnaQDKJWxac0iD_fEcsiLyODiIdMMzLAPy0mPzTiFk3cQb9MhsiXNEZOygk8Og8dys8U1masWNNnCuNulJZOwhsdlr17nnXJh2NJIHK6Aaz-KDlAcA7K1o7IghXsIPvZZiUvYQV_onQ72pd1FJcklBMvWpHYP8MQSx2xzxeKtiFMdI8_iecCcoA3ajQ4GIkSVC4gmS7KDajy51gkXsh8NQySwQy5EFV6VyNyCGfjko-KvV3O5aXnxsiL3_qr2cZzRV36GmNtxZ9Ny88sk6M8iuPCOrGppu_8YvKWVTn1N-uDgsMPa03IqTvFlCVXGnXxQkqD_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عادل فردوسی پور دربرنامه امشب رسما اعلام کردکه: سایت و اپلیکیشن پلتفرم 360 رو به خاطر صحبت های روز گذشته امیر قلعه نویی بسته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/26213" target="_blank">📅 15:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26212">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbrkH1VgTZrO_Xa-cWJKXzkuMklCGp1LadUg0L90R7MeWZLx4B8OpkKTmU6jO7aJEVCTpdgp5o2BXwE5_XkHdiIwEkCa5_e2aNhV79KagmVwXXi-Mgqm0r2XzAFowjOLgqT0cvtYi68Mhr113jGU8S3THwmlSS7Tf2VzLKUdHZinuaAS2369Fx0MBWuEXDcqBOCX3KPLAb2F_KNdltt7umozBJURC76xxZVX7Q1xVJuR7V0EiYyn5RgC4-Sfswfrm8pingL2mVFMt80nrX44IlBVrPYWG33PLTBdjd4ZBlljEJ0hZiX3Wa72F0yo1UWAuTi-4AbtiVgnhw83mgoGhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال ساعتی قبل باباشگاه آلومینیوم بر سر انتقال محمد خلیفه دروازه‌بان ملی‌پوش ایرالکو به جمع آبی ها به توافق‌نهایی‌رسیدند‌. باشگاه استقلال بزودی 60 میلیارد تومان به حساب باشگاه اراکی واریز خواهد کرد و رضایت نامه خلیفه دو…</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/26212" target="_blank">📅 14:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26211">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxvKLDD9aAe2lB9Z7NwHpEO8jgHzd_OvJ03hPN1oSSlYF0buYCnxTwq7DffZjmb5iCEtibYKppnbGDEkqaWqDqhT_m5yKwh_UexqcjzmC5Wql7mxEOoeCKC0pS0tIXnOtQ74MfaEB02IWFUaQtaQ25DCH4W6MPj3Q148O6EHm5sCBU3c9Q_ApsUeAQlWOluRHGgk5kx-posu1R7fJr9QW-XA4vi4WX1bHUaSrewlIK_m_LdG1k1vCtnfrNAY64Va5KaEMAn6YUgzcY22M1_CYaC58ShEbkrQ3vYk7V7LBOGd9SwuHvnWZDWtANmP3Z-G9_6PFxD6Bi8Zt-j4YlD6Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا؛ علیرضا کوشکی فصل آینده در استقلال خواهد بود. تمام‌توافقات برای تمدید قراردادش‌ انجام‌ شده و بزودی‌راهی ساختمان باشگاه خواهد شد تا قراردادش رو سه ساله تمدید کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/26211" target="_blank">📅 14:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26210">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKTHBmXZ1hPrFEOtzBQ-Qml9zRX_BMX_lic1uyvTfeLer8I7HsMlosXERJV1TMxlROypWVtKeEyN52y9UR0hEEtbVp7u2LeSoYxWjVkgZsqZQeI282Mr7L6UGOmQapMbtod6dnfsSE6sXQjek-hF-m_wzmqIBZS85c5U1Y-qeUF74sPPvodIKvvYHUtkX0EMkWgnWjxyEy7rKyq7HCR0Hvdz3uBwLJQJZIjH11wleqdF6qSg5S7ILs81dsqRsKDsjX2w-8ro-D5tOU4RvJwcAX4ijUFEZ6pt8EbYrJkzfipUJ208xbdau0VuexFxW4EWoNnLJnwfULolDEhPe-zrWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
جسی بیسیوو وینگر 18 ساله کلوب‌بروژ با عقد قراردادی 5 ساله‌رسما بارسلونا پیوست. آبی اناری‌ها برای این انتقال 8.5 میلیون یورو هزینه کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/26210" target="_blank">📅 13:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26209">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jmr8SUKSZzD4C7jz96gTJH_SoQYp_umuCphZqfuaclyDfte6DAv9lnFE1pYJECsf7fU-Fh74jIS4EHegBEUgNaLO5m3bYHFY17jkxUjXwVCpMpFpr24Pzu8lQ6O7jK5Y9sBLxuBoz4y2AOx-PJUGvLTO2lv1RF1Eb8ygjIzEhHMFvInKHo4bmzaHJuBEvF-un9f9oe4HYCl4-og6Wp27tUVgofpZ1T11HUQINcP0H9u7CtZBPvuMSU1rg_QnOrtsubbJQgwjuxXBe4rRW4iD-nxODMlDgb43la_QQKM3iQJXBHmt-8wKx68uLwU5j8caN4QSQePDE5-LiQfS2Qt2Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوری
؛
رودری فوق ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی که بعنوان بهترین بازیکن جام جهانی 2026 انتخاب شد آمادگی خود را برای عقدقرارداد چهار ساله با رئال مادرید اعلام کرده و به نزدیکانش گفته پرز بخواد میاد رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/26209" target="_blank">📅 13:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26208">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJCdgnAvmv71M89troUfZK8qfO9qcbrc-IutRU_lKDDF2iQ3T7yBfH_lk5KUzjRTonFnIU9zLDrGF-exX3s6nEcfQV_fsisZy_SFBym-6f2FNgLrT8D6IHzfIDASQdF987tTZHb7j9a0X9P55U1dGvTf-6e161OPSyYNQXxJWfc6hbi-oxD0rXIk4V7W-E_aK_sNAqNgXLK4-5QBgAAFQkefGD9WlKBbsTgZiWeYOWWYV3Z--jfGGpQJmQRJU8W5B19FZQH_bF0RLqeBm0UVu7gfKjaaxb1x_fGc5B-_fH2GqHZCPwD77S2EzXDkI56vTnlA--8dRW7pwd44OhEQsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی 10 روز پیش پرشیانا
🔵
بهرام گودرزی مدافع‌چپ‌فصل‌قبل آلومینیوم اراک باعقد قراردادی پنج ساله رسما به استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/26208" target="_blank">📅 13:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26207">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVfb-83ruLyvuJ-SVkGNsq5VIwkfaP9OwXkSmPeiDUm2xZNAbMQN819kP051juS8yUNwtIW7Ayy95tOf-YX4pQOg6ComrtPhtAaoIQrIYfih2W1lZPw79KFQnRPnY7RItY5k38n8qM-aZfR3GSzXWCUhE7SWHKcvdDg6nJr0UyQhvb3HEV_Jrp00PU8X74R938UVeaxvfOWVwwzAvw9eP8KeSy6iEJT_1mLG8gi4tp2N-fMdbUn1EXWKAuXAHTebO4Ouwjn_UXvZ3ffdYmSdqhpwyOOC-8BEyo2t8HZW67olxbCrVuUJrc9kUlrwuPt45ZORaCmlj9BKhWxifBLL6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق شنیده‌های رسانه پرشیانا؛ مدیران هلدینگ خلیج فارس از عملکرد مدیریت‌فعلی باشگاه استقلال به هیچ‌عنوان رضایت ندارد و در هفته پیش تغییرات گسترده‌ای که مدیریت آبی پوشان رخ خواهد داد.
❌
علت نارضایتی هلدینگ بابت هزیته هنگفت برای جذب ستاره های خارجی استقلال در…</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/26207" target="_blank">📅 13:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26206">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZzlTbMTZA2M10pK8f3BthNO1QnP07TaCK3qsgp0sVbKTbRqxL1odWvgPbWoL6t7qCj99grzgRvUWj4c45ipqsnpa29GVpTKq_rBHWmP0fmZjdwzBmFiHk1xZOT_JXGO_zBZV2Fypk1eMeHJcK3Aq_SIzvbZXdPCNGbOfaNiRcEgQxYGjSRWEtxul-MzYk2-gcObPmvRN1UWpTL7PxTjnrvk2SPT8Vx5fXq08B9Hrf8HsybAsOa7dITYzA8zHU3_zK3AlyQCB9AeaInWwtYlpxPYz2ghkSqjCutNiKcmv8LaHTqYjb8np-_ehMhFao7ZqdE-tRo1B43qkCO4ZO-itA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
#تکمیلی؛ حمید مطهری به مدیریت باشگاه فولاد خوزستان اعلام با هییچ رقمی ابوالفضل رزاق پور رو به پرسپولیس نخواهد داد. مدیریت فولاد به پرسپولیسی‌هااعلام‌کرده بود اگه‌مطهری اوکی بدهد این‌بازیکن رو با دریافت 80 میلیارد بهتون میدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/26206" target="_blank">📅 12:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26205">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NSl5fW67J3sgzFsIcZz7SqqNbBP2M7OvfQ-0iaODasNstv_wgc3Ia-DvxO98Sdm4ZbMizoZi2nzjV9fc41jFeNo1991OLa6LgOpSyK7miJLf0wQUJkYPmfAoIf-OM2y57kev4lleEc2lcjAXxCTwo8Bkm5CjwE67PCZlmsMjFQbOBquMyPCL3bhvf1qHpPi_26qJODvMuZC7LkUmM51I-NYRrpkQEcTwkd7iPGTZTC1WGAI14oi5tLn_kJzyAX9ux-9-E6F8PyRrIG9SjaqkSWV0eiesoEMwBSe1qkx4jcwkz3h-3CPF5-YqNRGY7QI1MKpBIzQ1OHfIGbqo8lWDMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
سیدبندی فصل جدید لیگ‌نخبگان آسیا اعلام شد که در آن استقلال در سید نخست و تراکتور در سید سوم قراردارند. هر تیم با ۲ تیم هرسبد بازی میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/26205" target="_blank">📅 12:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26204">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">▶️
هایلایتی‌ازعملکرد بهرام‌گودرزی مدافع‌چپ جدید تیم استقلال در فصل گذشته رقابت‌ های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/26204" target="_blank">📅 11:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26203">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kq5NwEP_f4tg5TxCJFqBj_ddue0iQiEBKXigLaAzY5Sev9JKhfluUCYiYCbC905UCNBQn3IieSBFMx9emDePPqrg9IR1tWJv72b1tpHzm7C1kBERHiu6FYQZ2r5sBuaw98f0L-pB5dLxV6SxyqbMUCQjU7mOGHUQ1a_odZ46Dpa6u1dOAAsS5Sqy81CVI5LoCpuOHw7flFhjrXQfQvqf2yoA23QcCxdAaWfEDv9zgTPtyRT_AVfABhxcfo0251LAP8UGlhQS455_hMQWCJAjPt75CaBNVnZYhwwTfkdaj4QpL1TGZHzsw20QvRftr2fgGjSYVNolYKVPZLjU5G2T5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ باشگاه استقلال بعد از محمد خلیفه؛با بهرام گودرزی مدافع‌ چپ 20 ساله باشگاه آلومینیوم‌اراک برای عقد قراردادی چهار ساله به توافق کامل رسیده و بعد از باز شدن پنجره نقل و انتقالات آبی‌ها بلافاصله از او رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/26203" target="_blank">📅 11:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26202">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6cc5dfc32.mp4?token=hbdv1g6IiMdAVxu4_jO15AADFeIG2aXFD7HTse8k_u8qDn8ch7KqryNmf3--BsY1x1jgVPsyAwJkK7d6ACgOyrJUx8SvOtffg6NXMlE1hRZEoigeSt2RDu9Y8zJB81N6BfFetHXw76gBnLGcbvjCxoDDIgvkZGdUfQNHVo4Kw8nMWQv3UozW9yKZ0zVrEqVkml3iB3Qln_uKlYnHt9ZeeIhhX71mhhZGxkLhC8zW9N11fKnNkA1yS_m252Sz865Vkimu4W312TGlbpnt4MnTKxrVCuMWieFd909QiogFy62BVBOEAujhPir2esFpY5Oo9vUJTPUxxE6SRi4KTcGanA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6cc5dfc32.mp4?token=hbdv1g6IiMdAVxu4_jO15AADFeIG2aXFD7HTse8k_u8qDn8ch7KqryNmf3--BsY1x1jgVPsyAwJkK7d6ACgOyrJUx8SvOtffg6NXMlE1hRZEoigeSt2RDu9Y8zJB81N6BfFetHXw76gBnLGcbvjCxoDDIgvkZGdUfQNHVo4Kw8nMWQv3UozW9yKZ0zVrEqVkml3iB3Qln_uKlYnHt9ZeeIhhX71mhhZGxkLhC8zW9N11fKnNkA1yS_m252Sz865Vkimu4W312TGlbpnt4MnTKxrVCuMWieFd909QiogFy62BVBOEAujhPir2esFpY5Oo9vUJTPUxxE6SRi4KTcGanA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادل فردوسی پور دربرنامه امشب رسما اعلام کردکه: سایت و اپلیکیشن پلتفرم 360 رو به خاطر صحبت های روز گذشته امیر قلعه نویی بسته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/26202" target="_blank">📅 11:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26201">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mar34L5ZORXaufR1tn8lIIPL0Mk5IfRHQdVPAXSggyGeFd-mVTuG68K2hkkS8iOfZeFlnkAJaHFtAQRDj9nnMCzENNifgwIu3saveGGjVZD1ZyLfD_dQ5L2sneOh52rbzzJhC--NDRtDH5HTVyUDshWTm-rrhXTUQtpis_kShVRDWuPwTE_a_-ODC_kwv0MzAxB2FCEFf_1UMsNsQpq1K-VNnD5j1YyfH-eLREKLGb7IooAHIAVSwnqe-M4_y2kL_-aDzOuNLPqbT1aPR3lEQmcilMBhQcxaviJrn575m2zKxbCKPOTEKKpaL5izPEBtloquw9JxwY0qVCLwx0Wf5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد محمدی مدافع‌چپ‌فصل‌گذشته پرسپولیس باعدم تمدیدقراردادش با سرخ‌ها با عقد قراردادی یک و نیم ساله به مکس لاین ویتبسک بلاروس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/26201" target="_blank">📅 11:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26200">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-Ov1K8U2sr_vkMmvgYCmWDt8QNS86cO17HmZwtozmbbS_zztZDBF7B0ZBpe9XOcEM_fJt2QlpAkRpBPc2lQ_gaaHlVeLhpVnZrP6-MValRrtM7RGNhcUtJfCDHAT6YXoUwta5YwA6eUHFihuqNe-Ga1oGJudo9acEa3lJ0cOziA1ENmKYf20BnSf1Vgm1sq1x9y4Zi5n-Gk8WoOr7wMW41lxUPw0n7zV9y-w0BrtjpWVI8N6pYljy33xQ5sDmfhteiBMOUFOInF2jiLS-wRLDJhiVOUJK-ibfR8GsNZUSZNpEsFX4gm15yL5Hrp6XKpm_hAsYWj3OuDuGlZhT3gQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
علی تاجرنیا باز هم تاکید کرد: انشالله تا آخر همین هفته پنجره باشگاه استقلال باز خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/26200" target="_blank">📅 10:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26199">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jht8nLq_RcXzCut9ZBoTnEPrK7l3K4HIcbHeNEbGgHqx59IVyiqK1YwqvM_3x0G6KeavW2rjPpCv-Ayk7S2UOL_bmuBoWUhFjTo5_1Ay0zTz0AO2C0u-j4KPaCUHX1q7Meb9kotsPtNALr9RIXlabIJjzppNazcOSTSWy4ThfQdlpN4Jc1xhgyXfhe1Gs_F_rKEGr2tCAFCHRYzjTJjJ_ueYuk2in7__aI62gYQNbsJRQKLmTs9NPzu9AKW-VQ71Bf7NqG5ft747eZysHfolBJf4pwtF4u_v0ViLvZkp5Fs5IxkWA-L30xNA6gU3OrhalLoFNaaZytzU1MWAzSnX8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇭🇷
نشریه گاتزتا در خبری فوری؛
لوکا مودریچ فوق ستاره 40 ساله‌کروات‌سابق رئال مادرید و آث میلان تصمیم به خداحافظی از دنیای فوتبال گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/26199" target="_blank">📅 10:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26198">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8a3189b48.mp4?token=DEDJCwAPXMhAl_I9awy4orxoP0XwXMs-oABOVhi1cYap8nMjwWUZKAz-jLcSw5vUZWqMiVsBgbUq-NmT3Bd6OSeuMVQhwWoYlHUVAYxnq8CVOyjP_feDdS4GgxAWUQ5m8wPXNo0fGESvy3gZPt0bBClBHI0Y3lDy094vWp3HofPjq1WI1PI7zY3-s6xFUKheRqdvORnmO8ZF8xApYNHYHLzc3vEHha28H-8H6X7jx_zrFBsg0KRsmHmA_kfx2lA3Tu4KT9Ykm4j8dRp85qgcRuPSEuI9xHZyoz-KF03SdXtMjyTitj83w6NoqFvBi3tYoUqHgsJOKY8mLTam0QkYyUStuwE5CKfT0rUsAFn0azqTFmQ1aASVwambQFxQTuvdsQM37g9ClWQnATFEBkjegmqX3uwmHtZmDvf3Wgz_LJGG0sVUbh56bkQdoYwBpwkiJihGZkptjdp4X0O3X_gi_46swYytleR22D4ofkDypFdwcaCKLjmDGRRi98_UYPluX3FPlU93UXthfELt7dE9YBI_Fsf8pc4Xgjuh89-FqkmD2rVXz_8qdDgXyqPz2QEQLtywY802ewJTzR09olf2N2W2BkxtmrcTBbNn_1DJvc-ATDVjKIZPyuwiVcKz2LF4U4Xa3ILKBn3w4I0JTQM8RAbiyU2_XGNURPTG_H6n9s8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8a3189b48.mp4?token=DEDJCwAPXMhAl_I9awy4orxoP0XwXMs-oABOVhi1cYap8nMjwWUZKAz-jLcSw5vUZWqMiVsBgbUq-NmT3Bd6OSeuMVQhwWoYlHUVAYxnq8CVOyjP_feDdS4GgxAWUQ5m8wPXNo0fGESvy3gZPt0bBClBHI0Y3lDy094vWp3HofPjq1WI1PI7zY3-s6xFUKheRqdvORnmO8ZF8xApYNHYHLzc3vEHha28H-8H6X7jx_zrFBsg0KRsmHmA_kfx2lA3Tu4KT9Ykm4j8dRp85qgcRuPSEuI9xHZyoz-KF03SdXtMjyTitj83w6NoqFvBi3tYoUqHgsJOKY8mLTam0QkYyUStuwE5CKfT0rUsAFn0azqTFmQ1aASVwambQFxQTuvdsQM37g9ClWQnATFEBkjegmqX3uwmHtZmDvf3Wgz_LJGG0sVUbh56bkQdoYwBpwkiJihGZkptjdp4X0O3X_gi_46swYytleR22D4ofkDypFdwcaCKLjmDGRRi98_UYPluX3FPlU93UXthfELt7dE9YBI_Fsf8pc4Xgjuh89-FqkmD2rVXz_8qdDgXyqPz2QEQLtywY802ewJTzR09olf2N2W2BkxtmrcTBbNn_1DJvc-ATDVjKIZPyuwiVcKz2LF4U4Xa3ILKBn3w4I0JTQM8RAbiyU2_XGNURPTG_H6n9s8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
این‌بخش‌از گفتگو عادل و علی آقا دایی و کریم خان باقری در هفته گذشته بیشترین بازخورد رو در فضای‌مجازی‌داشته‌وحدود 50 میلیون ویو خورده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/26198" target="_blank">📅 10:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26197">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKU2tLFziWPQPDbyzWYfC1x_TVYCZ-SEq9LvGwjpyYficBpt8Zton6ns0UskOQc6uxHZIkEBj4w9oFRJfozJ5pOrkRnTaHRvwC1Irn0xIDCGPDJ1BmwatUixy8D94sV_9KnCGoIG7mHXYyHms2Kq4tQHAuW-_exoVfGHGJtVPBv88aiAlYyioIu1l7Xc5IMfZf_JJNWp23eGQsj-yVJwXgQ4XloX2IRdkddMlosrkEnYCtmqS89MSiNTovIZM77YTrPzIjfHQoR-MKnf5Q23fHT-lHv7O95AYz32qApPM59kDpzOKUcFwNB6WGU5evcG-9PqNzqRLDiMWSF4TYqcjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎲
سوپر بونوس
0️⃣
0️⃣
2️⃣
درصدی وینرو
🎲
💰
1️⃣
میلیون تومان واریز كن
3️⃣
میلیون تومان تو وینرو شارژ شو
🔝
✅
مخصوص اولین واریز
✔️
🎲
برای اولین بار در ایران
🎰
متنوع ترین بونوس های را در وینرو تجربه کنید
🔊
با وینرو همیشه راهی برای برد پیدا میکنی
🎁
🚨
اطلاعات تکیملی بونوس
⚡️
✅
✍
️
ثبت نام آسان و سریع کلیک کنید
✅
🤩
🤩
🤩
کش‌بک هفتگی
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
🔊
اپلیکیشن حرفه ای
📱
🔊
همین الان وارد شو و فرصت را از دست نده
!
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
r30
📩
@winro_io</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/26197" target="_blank">📅 10:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26196">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESLGO6g75P09C3Wl1XsX4fNGyMNqM0RfNEY3UPjWvVAs27bUpKB3AYZrHL-J1YeDZjLMQ8hdZ-oKT76u-ViHA7qKO3XH8ilyJn63pytOvsTi7PmHiaoyo7mg9HCzoQfc0AZgBPBgzOW9q9o4HNAZv1d0pru9hefMt3988BGn4r6ZAAFI_tm3pz6WMWSAR084i3-6k7hhLxHYLBbxYlgjtP5a2TvSjiPGthdAxNeDYm6JOJZCU5CNGYlIWAfK1Y5qvHOioogIVAHgchbWAMIdoUd6aZ0Fw7xDFIwqi7kwxyevthopeETQhmlB28hMOiUg2gJ7t6st2-xnIdj9Sy1Juw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برسه دست مجری صداوسیما؛ تیکه‌ سنگین رضا جاودانی به میثاقی در گفتگو شب گذشته با عادل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/26196" target="_blank">📅 10:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26195">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xnl9ymVkSXNfGTYR5mOVOLFT3oK4Iw7Pm8Pz_pa23Sh05bq7wNkne3VEcltpp4JakYGm-dsJDGeW5x-8CBHrLANEPpnvH7yL0FfEkoJsW8_tGe0MRBlpK7GOoL3nmXeRUrewWEhuY30bHk1hhVCN9vssc0oqJsxxTfi1koP601ccQYHeZWFLx6YSTneRW1YA_GumKT8kyZAXFPddePoo05BJeUtBgcASdyLVUUIHvhyDwZAOD0CQCMjrRnxSNRKGGMNaPwGjnCklAh0HVKoJazoK5fzvXcz54pG4EL6KFaUCBS6vEr_6smB64353qQN8kapjSvWyG9WLw7mQGGkuEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛پرسپولیسی‌ها برای‌جذب ابوالفضل رزاق پور مدافع چپ فولاد خوزستان با مدیریت این باشگاه تماس‌گرفته‌اند که گرشاسبی به حدادی اعلام کرده درصورت موافقت‌کادرفنی‌رضایت‌نامه رزاق‌پور روبا دریافت 80 میلیارد تومان براتون صادر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/26195" target="_blank">📅 09:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26193">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/944a94e4e2.mp4?token=rsyWix2ieIMsaL2WqXZZLJEpjOJV3mS6562rn287yttUm2OpqVlNLV6sq1_btoID0KcMAP_GSGl66CriKHtx7Y690fjzUYGOLuBSYlru-1-Y8zhRQe3Gl5di9ccSmmS3BYTVgWLpTvTpYReCOXkTIq4hf8HbEmrAZVbZDQnRt99ETv6ekgZ0m_ivEmMLIxrcb_IHhqw731GLDCMGyB6g73IEpws0ysy-nCJPArH-_OL82_SQLEG5zu_-5Z1S43Ek5slm6ON8OnKhF7oHpDRVlLTXLx2aNlM2hAeG1EIEWN6V9SUa8n7NAtfOKp5o1pBwGA1HEQc_qk9RJrp-ZrZltw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/944a94e4e2.mp4?token=rsyWix2ieIMsaL2WqXZZLJEpjOJV3mS6562rn287yttUm2OpqVlNLV6sq1_btoID0KcMAP_GSGl66CriKHtx7Y690fjzUYGOLuBSYlru-1-Y8zhRQe3Gl5di9ccSmmS3BYTVgWLpTvTpYReCOXkTIq4hf8HbEmrAZVbZDQnRt99ETv6ekgZ0m_ivEmMLIxrcb_IHhqw731GLDCMGyB6g73IEpws0ysy-nCJPArH-_OL82_SQLEG5zu_-5Z1S43Ek5slm6ON8OnKhF7oHpDRVlLTXLx2aNlM2hAeG1EIEWN6V9SUa8n7NAtfOKp5o1pBwGA1HEQc_qk9RJrp-ZrZltw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🎙
عادل: من هیییچوقت بلع قربان گو نبودم و نیستم و هیچوقت هم اینطوری نمیشم، اگه میبینید با من مشکلی دارید بیاید دستگیرم کنید و هر بلایی میخواین سرم بیارید ولی من بله قربان گو نیستم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/26193" target="_blank">📅 09:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26192">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a85e23671e.mp4?token=XZu2XudPaWg4jrxGnfPaqqzNzdiQFuzRXZPdlbzPO6RsSkUCEfmu_AG7ZIq89bXhE_xCqO2FdkOGwREUNc5RMTJAPdbMhDCiqL4SACUFjjy47c0iMiiT1fRl8AYRd5QXOzLnnMaDGm9jsiyMCXjrMXKag2PeSvAyz_3eaSpQILVwAaBij3Z9-MNVyxqIE2iJeIAaYszH8JxQtP-zUNrghh64PeTvACvlRYFUsboIharl8muNoXsHVV5dSOShWzlsJe30LzVhRGXQ5WEa0KxDXNDPvGGMHyezjK2Fz-020TgBc_qWoxCJqBaC12xVRWrqS_CdtPBZWqN43-mkkQ7ogA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a85e23671e.mp4?token=XZu2XudPaWg4jrxGnfPaqqzNzdiQFuzRXZPdlbzPO6RsSkUCEfmu_AG7ZIq89bXhE_xCqO2FdkOGwREUNc5RMTJAPdbMhDCiqL4SACUFjjy47c0iMiiT1fRl8AYRd5QXOzLnnMaDGm9jsiyMCXjrMXKag2PeSvAyz_3eaSpQILVwAaBij3Z9-MNVyxqIE2iJeIAaYszH8JxQtP-zUNrghh64PeTvACvlRYFUsboIharl8muNoXsHVV5dSOShWzlsJe30LzVhRGXQ5WEa0KxDXNDPvGGMHyezjK2Fz-020TgBc_qWoxCJqBaC12xVRWrqS_CdtPBZWqN43-mkkQ7ogA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/26192" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26191">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a72d81bfda.mp4?token=VnmWCUl214MAttY9HYp9jIXoSrVl97NkSQ5sTFpm1oZbPzWWM7hbZyhSTHJMcKkXfN4xn8VSweDCVH8_0Z7see4g29IIHAvEst5wsytrpwmgPUOHLTgbuWTDWYXCmpfHaaFUQ2m4p7kCt91KoNQtDv-W8fOQDJiQxvdAPb7MGF_IpGl35U3wjmE-PBymKWE5gqlIBwQGEFRzbRlS9mswbOeYH4iM616NYSxbD1uPkjb2bDzVnxNY5yEIZb_uGwGFrvOR3i81Qmh4QG67_H77Gk83TCQvA4tMo4yonsTiI12XmINNrnXqGr3PneMujcd9PeFXFoG1f1ziNsi9K6NB9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a72d81bfda.mp4?token=VnmWCUl214MAttY9HYp9jIXoSrVl97NkSQ5sTFpm1oZbPzWWM7hbZyhSTHJMcKkXfN4xn8VSweDCVH8_0Z7see4g29IIHAvEst5wsytrpwmgPUOHLTgbuWTDWYXCmpfHaaFUQ2m4p7kCt91KoNQtDv-W8fOQDJiQxvdAPb7MGF_IpGl35U3wjmE-PBymKWE5gqlIBwQGEFRzbRlS9mswbOeYH4iM616NYSxbD1uPkjb2bDzVnxNY5yEIZb_uGwGFrvOR3i81Qmh4QG67_H77Gk83TCQvA4tMo4yonsTiI12XmINNrnXqGr3PneMujcd9PeFXFoG1f1ziNsi9K6NB9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🎙
عادل: من هیییچوقت بلع قربان گو نبودم و نیستم و هیچوقت هم اینطوری نمیشم، اگه میبینید با من مشکلی دارید بیاید دستگیرم کنید و هر بلایی میخواین سرم بیارید ولی من بله قربان گو نیستم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/26191" target="_blank">📅 08:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26190">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgUAxC5pHx5gaUPiGOnspCn_7lHzxe3EGdrFRmH9xL-t-f61vB-sQxamUB0ApPqWxNTvW6V_AsATfukMErypehs6umQec5Q8HIobOAsbsLkigGqH4cUDKJAF-pKLh0lb6yw-YiufePvuU7XLSSBJ_4wcmUbrxYEl5n3uUlfYEgcjYOWBtpZ8m_38wTue-Ntof88G9x_jN_QWA3YSyIlN1tn-CliM2YR0WsCZ_JxiFNugHDkksmPeH2YRBU7aOX8077xkMdajc8a_f-fyxw7lQ9G70Rt0aq2TuG5MCpa-0lharQYIxnaC2nCvRwrctGx9ZJg9Cop8mAYUq9nn2QJE3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها…</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26190" target="_blank">📅 08:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26189">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCxKNMFZfNaUyCk8Z5FItKLLb3Esn6SNHOzBhrzG2RdRf5Ed-6nHHdwsKsCjrrw-Fj_fOSGLSeC7bV18sEUsGMV9AeGkYDZ1j-e1yQ93kagXkMoeRuxHAf_bQoeUqJv9183JSefyMbPK3WH1cMspRt-ZPhGMlFG6t1K9G_g26Egz_vYJUX66RhA6h0UONCx6yIXyCYZY1C9VfBmB3NC6A3RrIj8T_qJHQxtg7p6S7VqEd-euVujVkR4Me6xCpfaJ6wq1S40h50X44Lxt6VwDHAXNXLqUPtMTGXzBMQLX2KBpJ9vLr7lSJ9oAI6b5o4hgBhsVOOBrkGyDQLd-pI1Z0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی #اختصاصی_پرشیانا #فوری؛ محمدرضا اخباری گلرسابق‌سپاهان‌بعد از تماس مهدی تارتار دقایقی‌قبل موافقت خود را برای عقد قراردادی دو ساله با باشگاه پرسپولیس اعلام کرده و اگر اتفاق خاصی رخ ندهد اخباری بزودی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26189" target="_blank">📅 08:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26188">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc5216b419.mp4?token=HIc13qcEskQsenRFHQg6g03WeOqBTMFmL9pSAt_0H1J7a_GmIn_vc2KVHLI8eKQVcspMTxWgtAwfvA_BjsiOl2W6tnQEQ1-UuB47pKx3OXaYBrSaVvb9k5fvcWQmEFO9tygCYTPSEL0Pv-42wkQpCBRurT-WSPzIa4Jo9ubeD_GTHowM8BoCsZnTbsaPW-i8gDtPuCdFikBk7ctPx-JaRFUCeERqwQDijymw2MDeNT4LCH6MQCpuzPvQoHmrFGAY9cp7wMxX2X0DGO0PXmjJLkFmsU3mVUppN_M0AzlTWZWzRTwgHf8LkjcbJLd-SAyTPDG0k0NohoAP3WCIvBdR0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc5216b419.mp4?token=HIc13qcEskQsenRFHQg6g03WeOqBTMFmL9pSAt_0H1J7a_GmIn_vc2KVHLI8eKQVcspMTxWgtAwfvA_BjsiOl2W6tnQEQ1-UuB47pKx3OXaYBrSaVvb9k5fvcWQmEFO9tygCYTPSEL0Pv-42wkQpCBRurT-WSPzIa4Jo9ubeD_GTHowM8BoCsZnTbsaPW-i8gDtPuCdFikBk7ctPx-JaRFUCeERqwQDijymw2MDeNT4LCH6MQCpuzPvQoHmrFGAY9cp7wMxX2X0DGO0PXmjJLkFmsU3mVUppN_M0AzlTWZWzRTwgHf8LkjcbJLd-SAyTPDG0k0NohoAP3WCIvBdR0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
بغض‌عادل‌ازصحبت‌های حاج‌ رضایی بعداز توهین های بیشرمانه امیرقلعه‌نویی و فیلتر شدن پلتفرم ۳۶۰
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/26188" target="_blank">📅 01:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26187">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e8c2669f2.mp4?token=aqqJa1KLgskPru3KDneBvf3NEZdjGCcFhKpCmWc65YGDcQ1Po_xPeRysFARU-lhWjmuSnj5FYVB6KWr9vdEpCw4ns3mu93Du-JVsNJKbUd1ElN68HmrIndZgXdsvSWDD9Bdsz8q8keQfBfvA06a6a7v7mk9rrP_MAeA4s07NOjvQY1X7fqFXx_73a14Bx6nAwOXjL6dV_F89Ni4emt0mOY3aYgxLULN6TdKyc_1la5fts1u_k87g_rXQQfLIrNP6meE-Yzs80YIDCbmUvLPHDce67RfeikIo8tx1_FTWRsjdHg6gUV2C5bjt4BbyI_1O4YKpyLBImlEHgozLG8YSxbv8mzXsM66rvpfe1OTJVzGWTuR1aOzSSnrgtbL8wkDjoqZubdRGoayX1zgFo5q-RvZ5cT9ApCoRwV-LBjSfIDq8xzIdOq6j9ZV1qwW-Yi4oRjHnleIVOOfRGWSGzPFf6SoHsMaA8bjDMNLONndDgHKjZ_7asX0oBtqb2ugYQ5yNvlqrJ4iMnCcWTB6w4DxOWDOMQblRXw7e3R66oWjxZiNgFm2G_-vzlvw952D6vync4NdVbtwo_hg5lbper2NOT-v9KqKCPigF1yY6yNDwDW4PsDba9PhbIiqkqUiDOu7IFmdmqiqK1I17VkfBdmejGCebFVyto_5EFp05gi8V6Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e8c2669f2.mp4?token=aqqJa1KLgskPru3KDneBvf3NEZdjGCcFhKpCmWc65YGDcQ1Po_xPeRysFARU-lhWjmuSnj5FYVB6KWr9vdEpCw4ns3mu93Du-JVsNJKbUd1ElN68HmrIndZgXdsvSWDD9Bdsz8q8keQfBfvA06a6a7v7mk9rrP_MAeA4s07NOjvQY1X7fqFXx_73a14Bx6nAwOXjL6dV_F89Ni4emt0mOY3aYgxLULN6TdKyc_1la5fts1u_k87g_rXQQfLIrNP6meE-Yzs80YIDCbmUvLPHDce67RfeikIo8tx1_FTWRsjdHg6gUV2C5bjt4BbyI_1O4YKpyLBImlEHgozLG8YSxbv8mzXsM66rvpfe1OTJVzGWTuR1aOzSSnrgtbL8wkDjoqZubdRGoayX1zgFo5q-RvZ5cT9ApCoRwV-LBjSfIDq8xzIdOq6j9ZV1qwW-Yi4oRjHnleIVOOfRGWSGzPFf6SoHsMaA8bjDMNLONndDgHKjZ_7asX0oBtqb2ugYQ5yNvlqrJ4iMnCcWTB6w4DxOWDOMQblRXw7e3R66oWjxZiNgFm2G_-vzlvw952D6vync4NdVbtwo_hg5lbper2NOT-v9KqKCPigF1yY6yNDwDW4PsDba9PhbIiqkqUiDOu7IFmdmqiqK1I17VkfBdmejGCebFVyto_5EFp05gi8V6Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
اشک‌های تلخ عادل خان درویژه برنامه امشب؛ مردی که پیشنهادهای وسوسه‌انگیز رسانه‌های ایرانی اون آب رو بدون فکر کردن رد میکنه حقش این نوع برخورد از سوی مسئولان دولت نیست واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/26187" target="_blank">📅 01:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26186">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1oemB69HfekDgSsRzslAiqmBMgqLAl56ZSUOWzKgD0FuPb2ePzIfKcUNk5gdPyLs-hjKCa8UOJiugmn5yMPS3KNXHeVRZGN_o0XSmhe1XHKuZj_XNwgSnIU07NLUyeys7B4c2rzmtVSSj3Qk_Zc0K30tSYImZMb8D6c6jS7cJP8rOXQXpIQZuw26szDeKRISuFWQ3QDgk3ennGVdLI7Bm0WkBYG8DdQgioPxIy7Lad5u2UcbZ3XEsUWjg9y09gz-HvUtrLXdHAu-GBh5mA3NHFHHXfRRAdp4qnw_F8F-ITcEQx9ispXcLgWByhRcaUC06JUp29feH3W8I-X6vo7XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مزدک میرزایی:عوامل‌شبکه ایران اینترننشنال در سه مقطع پیشنهادمالی‌بسیار بالایی به عادل فردوسی پور داد که‌به‌این‌شبکه ملحق بشه اما او هر سه بار این پیشنهادات رو رد کرد و اعلام‌کرد هرگز خاک ایران رو به خاطر رفاه و منافع خودش ترک نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26186" target="_blank">📅 01:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26185">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6808ecf091.mp4?token=Ov-qAEhXupbCOqnAMIallwGa1-_IKuV-oaTqpzzMhol5T969T9Wm5QwuZt9r4_mpfdJylAlwuQ5ASaW4yl7AToIoFuFRYHpwCl9N4H6YQ-FbsDmKJrx44fH9SrJaFqewPMZfo8WZuYaytw9TI2JPub2zYcJei8r3fp3MlnhhOS4VfuuG-zez4EnRXkATFv6zl7LtpJcjq-FVrxQ_1ohAWXBPGlm4kwclkXusOGZhy0svz21PySnBMudy5pbbiW2_jJlIwQOSqmI1BWECks5A72y3VgKsHyxTPlywyNQkA1P2TA64JxFhfXT2Oy4sPxM8lX_NuJSknYyKdZ-R6FsVcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6808ecf091.mp4?token=Ov-qAEhXupbCOqnAMIallwGa1-_IKuV-oaTqpzzMhol5T969T9Wm5QwuZt9r4_mpfdJylAlwuQ5ASaW4yl7AToIoFuFRYHpwCl9N4H6YQ-FbsDmKJrx44fH9SrJaFqewPMZfo8WZuYaytw9TI2JPub2zYcJei8r3fp3MlnhhOS4VfuuG-zez4EnRXkATFv6zl7LtpJcjq-FVrxQ_1ohAWXBPGlm4kwclkXusOGZhy0svz21PySnBMudy5pbbiW2_jJlIwQOSqmI1BWECks5A72y3VgKsHyxTPlywyNQkA1P2TA64JxFhfXT2Oy4sPxM8lX_NuJSknYyKdZ-R6FsVcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
رقابت‌های‌جام‌جهانی2026
؛ جامی که اشک سه تااز بهترین و محبوب‌ترین‌بازیکنان تاریخ رو درآورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26185" target="_blank">📅 01:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26184">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19f1d43ddb.mp4?token=jB4ZUISyzJMgEf9eihIW2pFvEQuuyoPIlIjnxKFMtGSBPVAl7xBHjEGD2cs_ELx2hMDOeTZ2p4LPsjzN-vF3tTQaels6jyhz5IZo2aNgcRA563X7YUPPcmEpvOqDWmR8Z4U29M4pIky8QtR-co8SA6x0teQdsLIKqKRw8gypbrMyt9kWJNG1F4TjtiY4-Orhhjcj7flLzPyiXwU0RlrosMLTYX7kR2tVnsRUdgeX8BGm-bICvIUfIMubbIZc7fsWHn44xF5xx9T7QzjuANxziOEn0n9oihmJ4RlsJ9ctIeAunwX6CIFeYuM2xTkhA4oeIjPj8xCrSxMD3NN7NSj9QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19f1d43ddb.mp4?token=jB4ZUISyzJMgEf9eihIW2pFvEQuuyoPIlIjnxKFMtGSBPVAl7xBHjEGD2cs_ELx2hMDOeTZ2p4LPsjzN-vF3tTQaels6jyhz5IZo2aNgcRA563X7YUPPcmEpvOqDWmR8Z4U29M4pIky8QtR-co8SA6x0teQdsLIKqKRw8gypbrMyt9kWJNG1F4TjtiY4-Orhhjcj7flLzPyiXwU0RlrosMLTYX7kR2tVnsRUdgeX8BGm-bICvIUfIMubbIZc7fsWHn44xF5xx9T7QzjuANxziOEn0n9oihmJ4RlsJ9ctIeAunwX6CIFeYuM2xTkhA4oeIjPj8xCrSxMD3NN7NSj9QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
صحبت‌های تامل‌انگیزومعنادار ایمان صفا بازیگر سینما درباره‌شرافت‌دربرنامه‌شب گذشته‌ جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26184" target="_blank">📅 01:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26182">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gFYwwdRw-gI8filF77iNhRIofK74bL7fHjR69VXGlsKx8wK7qDby3ibj2xdiAXdq9QFrfWa385n3Yqd5wU24H6TsK2Gwqj_H_Svf6QhbwNUzLo83yLAb_p4fuJ8hg3ptKKpezpb0SOa1MZluQ8esCDPmwwwELRumBS1nmvneh4mGZwW-K6UCaR0XqQT8zY2tpF2ciC4paCn-WRskq6H-oMN6OmmP-HSXRgQ_X7JJG24cGc8Czxs98kWfftynRenu2lU1g5x-VVhyZ4YpG90btyzmnvCTbJ50fhdvBQ_Eh0EBqOeShHPn5bGjFZunAeV2hb--rTnw0DlyXqkV3lV96w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
رفقای گل دیروزهم گفتیم باشگاه پرسپولیس هیچ مذاکره‌ای با علیرضا کوشکی ستاره تیم استقلال انجام نداده و هیچ‌برنامه‌ای هم برای.جذب این بازیکن 26 ساله نداره. بعنوان اولین‌رسانه گفتیم مهدی ترابی 32 ساله بمب اصلی مدیران باشگاه پرسپولیس است و امشب هم جلسه بسیار…</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/26182" target="_blank">📅 00:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26181">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_5ZA86UdCtPCGSWtAym-3WCHoXaBkpeAjGWwsA3GuuoZNkR8YiMLc5imjUK45IrwtYp1TV8awVhSbeyU_psOjRac8syZH22Aj5AnEVoCly4c5vU7D-vBUg66bwXardGWhbFmdq7KTAZSzuRb0RLlTg6JDReR3PP0dEVfiLCjboVFDDx3GuVeAkTWbjAi49pGAOGDmbu1SebC_ybJGClIJeDEa3GgcBwK7m0vYCHRLivR-xggge3h3vj7O-_Ts3cY9xJF2H0NKNaFOiV7cAMFL7FtnPStjGZsNHHtpewKlvDx1w6DmlbO5TVuDhMWBa6qLvjCFL7GCOikC4yRs9CXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوه اوه اینو داشت یادم میرفتم بگم؛ با پایان جام جهانی 202؛ تنها دوتیم‌دراین تورنمنت شکست نخوردند. یکیش‌اسپانیا بود که قهرمان شد یکی هم تیم امیر قلعه‌نویی که از گروهش بالا نیومده. قراره صداوسیما مخاطباش رو با این افتخار باردار کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/26181" target="_blank">📅 00:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26180">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b7f2a6c71.mp4?token=pbuTbvKo1batzkgqOkeWIZj1aBe-4lrRk1c8F8J0YzkIOaJIC4cK5NnHoavWrn21Sou4G4oqcKLLyOnOwdWGX2zTSXFUWm69-wcasDBYj0d9hgvYHT6k5eVajW-QDJsu5DdtW-vFvr9-IqR8zqr8Yldk230OGqOns-452QDi5kv-Ipytw2tyqlBqJAu1EqnaDdzC9gjxH9P3Kdiys37bh9VlSgHP0mfhzZLw1gMe6FOefuwVj6PjaONLQ6-JmEWWq-WJSpGh9M4kKt96_nhZTcr5ul2S5beGtNZjzRbaMjBGV26k1_Xz-JR_amUPRnfJwo2Z7_5pJQFme6xGCh0fiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b7f2a6c71.mp4?token=pbuTbvKo1batzkgqOkeWIZj1aBe-4lrRk1c8F8J0YzkIOaJIC4cK5NnHoavWrn21Sou4G4oqcKLLyOnOwdWGX2zTSXFUWm69-wcasDBYj0d9hgvYHT6k5eVajW-QDJsu5DdtW-vFvr9-IqR8zqr8Yldk230OGqOns-452QDi5kv-Ipytw2tyqlBqJAu1EqnaDdzC9gjxH9P3Kdiys37bh9VlSgHP0mfhzZLw1gMe6FOefuwVj6PjaONLQ6-JmEWWq-WJSpGh9M4kKt96_nhZTcr5ul2S5beGtNZjzRbaMjBGV26k1_Xz-JR_amUPRnfJwo2Z7_5pJQFme6xGCh0fiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برگام‌داره واقعی میشه که؛ رسانه‌های نزدیک به امیرقلعه‌نویی میگن سرمربی تیم ملی ایران میخواد بابت صحبت های شب گذشته از عادل شکایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/26180" target="_blank">📅 00:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26179">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37ac31eab.mp4?token=EcDrD0C7NkjnXgyo95oVDGtlejM4uf08iDxQiFD27Ivyy2hXh25obXSEAnOx8SpKOfj8VNVxN742zMq4XMI4KXwlgSXWIu7biiFDas5IxFemI44Do10BEPd0Ju-1IKVxWE0I1MRiIv1UNBBhNFeCQ4GPMWQXj3yEeOoAwQj366CoRmB4ZtqeK_U1BBTrc_si1TJIjOAmZHPvkuggMYvBzIg3wtn_yhaAjAKnq-Gvypv1mEVXGnoZZvb3yNBJ2b3cvjCzCCByD1LcYMc5FdhwLSwXP9l3EZKTu2ZLCBC8uBp0dcARZ8f1B8BgXU1VEmUIXcSVDT7VCgxJMY37xt6syQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37ac31eab.mp4?token=EcDrD0C7NkjnXgyo95oVDGtlejM4uf08iDxQiFD27Ivyy2hXh25obXSEAnOx8SpKOfj8VNVxN742zMq4XMI4KXwlgSXWIu7biiFDas5IxFemI44Do10BEPd0Ju-1IKVxWE0I1MRiIv1UNBBhNFeCQ4GPMWQXj3yEeOoAwQj366CoRmB4ZtqeK_U1BBTrc_si1TJIjOAmZHPvkuggMYvBzIg3wtn_yhaAjAKnq-Gvypv1mEVXGnoZZvb3yNBJ2b3cvjCzCCByD1LcYMc5FdhwLSwXP9l3EZKTu2ZLCBC8uBp0dcARZ8f1B8BgXU1VEmUIXcSVDT7VCgxJMY37xt6syQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادل فردوسی پور دربرنامه امشب رسما اعلام کردکه: سایت و اپلیکیشن پلتفرم 360 رو به خاطر صحبت های روز گذشته امیر قلعه نویی بسته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/persiana_Soccer/26179" target="_blank">📅 00:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26178">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNIKhmnR9Kg9FDXvRfm9MvrWTaZisbtCvU19DsF4pKAmtY2T4e4JOZF_vDslx_OMJwJJPdyQW1a0jzVs4AQEO494bYZ_eGy_PcWYqKFvEQWfhp95zf6Rw1Bshz3mOZgxg82TF1wIHbej0Qho0g2T_zCQ8pavmD-d36fWgTs5L5Jju_wRr44-zWa26VDJMBOpFa1dkxDENbfGH392GHUNAh6Mai7QPV_PrjnNfX_niD55B0KaegMR0kRRKbSwGVykW8IE2upQpkVOJ1hoPqpstBOQqhZNNZ-HQXpo7c90DuWf1cLN-0T09vKlMPcy1sxxVbRcbA2ZEEn-8GDCmG74Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
شرط‌اصلی‌باشگاه پرسپولیس برای قرارداد با ستاره‌سابق‌بارسا؛مدیریت‌ پرسپولیس با آلن هلیلوویچ گفته که‌مامشکلی‌برای‌عقد قرارداد باهات نداریم منتها قبل‌قرارداد دراردوی ترکیه بیا چندجلسه با تیم تمرین کن و اگه کادر فنی تیم اوکی داد قرارداد میبندیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/persiana_Soccer/26178" target="_blank">📅 23:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26177">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R56J7PlCwWsQYQBHHKWjBf-Q4zpmJSlLhREJp8lkmqQYBPVOEAYwiL20n2FkKqPtTf74bgbZA8FUpQdXfsUQyLbaYrNNE6o_V4gZNjbp55HizuaWvosp8wtd7pjTHpLfYefO5bJVxmOdmH9NcQ315eRlDNlm7CD5q_dGO6RcCPZSZkb4dufmZ0olVwusT9XUwZskIM--ry-QPcJl4eFpYEk1yvBr40OZbWAJQgOvmKpMJtyMAiPJeJ7qvPiC971GT4bGZPprpgL5kbrAjEsqmF_B_xHkf0m9StMz3L1Vl5sgcU3hKYemh1XRy7Jg34mNwdzLnFJL9C2tAtqMPRXeNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها…</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/persiana_Soccer/26177" target="_blank">📅 23:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26176">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uslE27DWdo7o72IEhCFB3ki4u29dBSvhuaJNNpGjEHqKxRKIBmvCSm1n0N0yBp_fnOTEP4uazbcY_PMAiQe6260yWiPNvnHciUB8bCu_SDUn3estOSEps7yUCx8jWXJZktQUmSgMpEJwS8ntXRtiVC1zMihH55EbuLmPqlvFCFci7hfLCu0qcuRa-Ae5w4JfpcW5cV2ANdryecydf-qRAPXF0YuUU8hqxlIwM_9hbfONZtJJm-CAI8TZPyR8GrKmBjmGksHl2TNIMIlOlUIFbLhjlFQyjUnTabTbL9NBSCNwlD1Fn-ccdwytm6mgRPgywHncsL1wvOua5aPM5qkGWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#تکمیلی؛ راجب دانیال ایری به اندازه کافی تموم اخبارش رو ازروزهای‌گذشته تاظهرهمین امروز به‌عنوان اولین رسانه پوشش دادیم؛ حتی خبرگزاری آنا خبراز متتفی‌‌شدن این انتقال داد اما گفتیم منتفی‌ نشده و باشگاه نساجی72ساعت وقت داه. حالا طبق اخباریکه گرفتیم فرداصبح…</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/persiana_Soccer/26176" target="_blank">📅 23:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26175">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqkE7VaQ5mSX2T08yZ7lt-YC_jK5KKlX0hUQHbFstzb2CMKxzyKIm7UOG0_TyKHLRXfTkKhp6Y9O1o1G_52FrEd32IRsOfkcYCpkWu4IKDD9vZ9G7PqnxdUJzfJmTV-shfjuIpjkKtg7WU2139UNGD_iyQ183xTM07roWWPxNvDh-J1tZNMmEAw_ESkG84KhhkEiQwdAGlR21_Bil92C4TtpN5c7TUhJqLlsc5PvXWz64uutBM9m2HEkaBmtHgM0cBDT4tMaX6CYfCJ0ZBFlIYXhMPWX-UyxpLm6SdXumy-jqdtvz-GvAp9VifMUFHvDCQdUtCsyH8JejcEHS9wYDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه فجر سپاسی با مجتبی حسینی سرمربی سابق آلومینیوم مذاکرات مثبتی داشته و اگه اتفاق خاصی رخ ندهد بعنوان سرمربی جدید این تیم انتخاب خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/persiana_Soccer/26175" target="_blank">📅 23:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26173">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52ed7e49e2.mp4?token=qig-t6fw0hv4PYtKNxi4naCWZY3mk1w1ArqqUssPlBP8g7lgoxue8uH3RCDrqvZnpZGaHY0U3Q8kBN4LYrHYGfbpuNKtzMnDPfpjLrWfxzM5gSX71-uWttLXoZ8oLzpp_WbzfNHEF8L4cAgRsMO1RGONusF5VyV3Y0RCW9FWxX6SO4i-SqYmhNCuYdM02qVmmPme7ggJ0lpPgk8lstSu0V8O90yjiLLsq3NM6wwx9mqJ6oQhURizDZbv18Da4jjI6QuUsX7fWgYEvD9-oA-0Yf4VwjCy9hk633Z-iRiameRcgBjXlMP4DvbAS1pTVq8lmqZa5zqzzpr-KMi8sct28g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52ed7e49e2.mp4?token=qig-t6fw0hv4PYtKNxi4naCWZY3mk1w1ArqqUssPlBP8g7lgoxue8uH3RCDrqvZnpZGaHY0U3Q8kBN4LYrHYGfbpuNKtzMnDPfpjLrWfxzM5gSX71-uWttLXoZ8oLzpp_WbzfNHEF8L4cAgRsMO1RGONusF5VyV3Y0RCW9FWxX6SO4i-SqYmhNCuYdM02qVmmPme7ggJ0lpPgk8lstSu0V8O90yjiLLsq3NM6wwx9mqJ6oQhURizDZbv18Da4jjI6QuUsX7fWgYEvD9-oA-0Yf4VwjCy9hk633Z-iRiameRcgBjXlMP4DvbAS1pTVq8lmqZa5zqzzpr-KMi8sct28g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇦🇷
دیشب‌بعدبازی فینال؛
یه خلبان در حالی که کلی مسافر آرژانتینی داشته روآسمون گفته آرژانتین قهرمان شده درحالی که فینالو به اسپانیا باخته بودن و اینا از خدا بی خبر اینطوری خوشحالی کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/persiana_Soccer/26173" target="_blank">📅 23:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26172">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d51f33dc.mp4?token=XpI5axYf1qiaKLQzfX2tGnV-gMwfMKOtPvtEjt21dUqiSThFukQNXOokHwe-4zIg0HcXA7HC_asHANb0P9a-IzJ2c88INFszT2QQp5JUzBalxeAStD4KB5JcnFl0cie9SMGfmg3XBzAmnxqC4Nk6Xfisvunkbo_9dlYurgig8E24pJZx5DeQ9VV0EuFsSFXGjke0eCTHCrPKC6CewLBh2EUF8B-lziF7RBS4dXvxGls2DtJaiiIjH-YbSHtrqt5LB2f-mRofdyXUTpkPY-ZPdq_Tr4BVlHdCkchGkwzuO7IsP0bch1pejPeLWd18z1ruqtda4BlAqm0z0BtxEMZ1Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d51f33dc.mp4?token=XpI5axYf1qiaKLQzfX2tGnV-gMwfMKOtPvtEjt21dUqiSThFukQNXOokHwe-4zIg0HcXA7HC_asHANb0P9a-IzJ2c88INFszT2QQp5JUzBalxeAStD4KB5JcnFl0cie9SMGfmg3XBzAmnxqC4Nk6Xfisvunkbo_9dlYurgig8E24pJZx5DeQ9VV0EuFsSFXGjke0eCTHCrPKC6CewLBh2EUF8B-lziF7RBS4dXvxGls2DtJaiiIjH-YbSHtrqt5LB2f-mRofdyXUTpkPY-ZPdq_Tr4BVlHdCkchGkwzuO7IsP0bch1pejPeLWd18z1ruqtda4BlAqm0z0BtxEMZ1Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
دیس‌فوق‌سنگین ابوطالب در برنامه ویژه امشب جام‌جهانی به‌قلعه‌نویی: ما تو غار کنار عادل هستیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/26172" target="_blank">📅 22:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26171">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddacab4fa0.mp4?token=gTb7jks-H69tPNrLjyTc75sXIRtSJE9YQE7IMFFaQZn11x9uJqn3hGnn3rE5kXbjjott9WREdyAjw6jib3c-t4AoP06XOfkNbV4CARj7vM9Y-2IZUQCJp6srGwpFp0Ko5qGapClAOxV_C_N6G5P2b9v72URpUJjvG2gYTNyigA5YwuZwtPvLPs7BtewrORC3kE_rdGR8CFoxj_tjKLlKnR-2BZ2HSUcbcNAHCjFXYIrUehsl4C0hYpRUJ1OUKj_ewCjiwxF2jU5VEeF7GpMnijIU6JdbncqowwLaOa4gN3NvVt7gTnAkqjzPKVA2Pz-5PhdDfRA8E5GsNj8V4lVdSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddacab4fa0.mp4?token=gTb7jks-H69tPNrLjyTc75sXIRtSJE9YQE7IMFFaQZn11x9uJqn3hGnn3rE5kXbjjott9WREdyAjw6jib3c-t4AoP06XOfkNbV4CARj7vM9Y-2IZUQCJp6srGwpFp0Ko5qGapClAOxV_C_N6G5P2b9v72URpUJjvG2gYTNyigA5YwuZwtPvLPs7BtewrORC3kE_rdGR8CFoxj_tjKLlKnR-2BZ2HSUcbcNAHCjFXYIrUehsl4C0hYpRUJ1OUKj_ewCjiwxF2jU5VEeF7GpMnijIU6JdbncqowwLaOa4gN3NvVt7gTnAkqjzPKVA2Pz-5PhdDfRA8E5GsNj8V4lVdSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اینوقلعه‌نویی‌بشنوه‌دیگه فکر کنم شکایت کنه؛ تیکه فوق سنگین عادل فردوسی پور به قلعه نویی در بازی امشب: آرژانتین بارها تا آستانه حذف رفت. فاصله‌اش با حذف5سانت و 10سانت و 30 سانت بود اما خدا کمکش کرد و موند در این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26171" target="_blank">📅 22:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26170">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22beea35ed.mp4?token=EpjVv3RgZHVQasUnuo4A_YRl8ksWWknJAPgF1USi6zZ5SXb8bqqnJgDPwIzj2U99cI-PXzyOBHrBg5fQtt5fjJ8XYFnyvhVnktly1eCtHlmLzdKtL6acDNQefBGUEz-j3tbaujX3uJv-MGr1Nyauw5GcrpQIB1Eedei0jKHSu87KBmsCIlIySMgNVtry-bmkQMaBmCLtwb7g-1vj0q-yqaChXYMRv5MvdPcHtwB6mdgSqW9jzQ9gNqhJSv5h8YA0EyJqT3TIW8yQyo7ZasmMCAPrCpyW74TGT0OR3PjFsLPhWMD2n3cLmi2deYGOae7Kicw48mOAaIuSalQ5sl1QzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22beea35ed.mp4?token=EpjVv3RgZHVQasUnuo4A_YRl8ksWWknJAPgF1USi6zZ5SXb8bqqnJgDPwIzj2U99cI-PXzyOBHrBg5fQtt5fjJ8XYFnyvhVnktly1eCtHlmLzdKtL6acDNQefBGUEz-j3tbaujX3uJv-MGr1Nyauw5GcrpQIB1Eedei0jKHSu87KBmsCIlIySMgNVtry-bmkQMaBmCLtwb7g-1vj0q-yqaChXYMRv5MvdPcHtwB6mdgSqW9jzQ9gNqhJSv5h8YA0EyJqT3TIW8yQyo7ZasmMCAPrCpyW74TGT0OR3PjFsLPhWMD2n3cLmi2deYGOae7Kicw48mOAaIuSalQ5sl1QzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه سنگین و کاملا مستقیم علیرضا نیکبخت واحدی به میثاقی درگفتگوامشب خود با ابوطالب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26170" target="_blank">📅 22:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26169">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JM7BwcC-2HipZqmqEdwddwFX9sNawO5BqRg5VfhF3CJogDqmoMemlS_nglA2BbFljBjG1QlG2wE1ptUcy453b06Y6u7z6X5mr5-qF5zQ8JswB8tSJXEnN3XNoG7YgsGElrh_hKTZISYYVe7epgs0G7VmbqdsgutzIsSn23YtAIwLyGYPfOs_aYAdeyQjcWgWtxgKm8o8kUv_E-k8K-6XSTAEOm6YHL62RwCfUM4XMdq6h4XucfDx-DKV2bByuXpTmacuK7yW8eImNjI4xwULUZek0sdutkvmdXX9mLBdIwGG5qFfXZmexDaFJKGeNr_lUELGpsS4PicBQ5I2r_J8Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
20 ابزارهوش‌مصنوعی درسال 2026؛
بهترین ابزار های هوش مصنوعی در دسته های مختلف.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26169" target="_blank">📅 21:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26168">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ed6167b3d.mp4?token=ciVmi5mFnVTVwt2Ana10kzibFc0vUbWcwxz88IXwr-IwSmFHHySe53B1Kf3yFDm_9Ni4YIcQvN13mrHSU1mZ6OvvNKpePwsPqB7Na-yRjtEcfTHNanDLpY4qvFDj5UZy9NDWcs48xF2oqfMidZMg-l2XHyA1pSiwG-9QmLq_k83vpexPJN_jDcU21CjSw2SCYfBQFMcZv3RgwENqgAgS3GWBlKru25z5-lgl_Jx4gUUj32S0hRBx-axqbCfHP6gT3PsaaqiSxb1naPBPRfnGpSF5B0x8xyoEpNw0rTgusMI_ixiH60bFa9jewKzW6x6IAimrciBVKyXNHZ2B0B2Z8YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ed6167b3d.mp4?token=ciVmi5mFnVTVwt2Ana10kzibFc0vUbWcwxz88IXwr-IwSmFHHySe53B1Kf3yFDm_9Ni4YIcQvN13mrHSU1mZ6OvvNKpePwsPqB7Na-yRjtEcfTHNanDLpY4qvFDj5UZy9NDWcs48xF2oqfMidZMg-l2XHyA1pSiwG-9QmLq_k83vpexPJN_jDcU21CjSw2SCYfBQFMcZv3RgwENqgAgS3GWBlKru25z5-lgl_Jx4gUUj32S0hRBx-axqbCfHP6gT3PsaaqiSxb1naPBPRfnGpSF5B0x8xyoEpNw0rTgusMI_ixiH60bFa9jewKzW6x6IAimrciBVKyXNHZ2B0B2Z8YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسانه‌ های اسپانیایی: دوست‌ دختر یامال رابطه 5 ساله خودش رو با دوست‌ پسر سابقش به خاطر یه درخواست مسافرت از طرف یامال تموم کرد. گویا قرار بوده ازدواج هم کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/26168" target="_blank">📅 21:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26167">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Boe_92mTqcBiecJMXdexLilKVtRXqOv5Z2AgdMPfSHvZf9KNRUTft-ldM7EuhjfImQSYQcdUl0oTPYOtNxAYWzg4069vj9kmFuoRnnpHt6H3nefGcDfF7E99ogIj0-ZfXeQXI4yEwvU01NP_Hhae74BT8SCiKyIqrAWw04_gEuDpqC5qKdVXvKBNHX7pVPEJl6J4NTH81XM1rCXIkbtMfeTzc6fmPsdDE4ABMjPi7njJ3MWB8MSoDxd-tpQZ-zBDwL2lpdsQJEAmS94BhBNB6-AIwBGh6yypwlBPGF-TeXdNnnYR-c8GQUXQYHdffPC6clIinKpdwk3crBmcE8xFJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...با اعلام مدیربرنامه‌های داکنز نازون؛ این بازیکن قراردادش رو با باشگاه استقلال فسخ کرد و‌به‌شکل رسمی از جمع آبی پوشان پایتخت جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/persiana_Soccer/26167" target="_blank">📅 20:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26166">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogBUUP9aXj20HTqqEFR-SNXTPAjqWfyYMAOpIyVYprzAnPj2n-kJrkKcNlOrxHKiowasGS8li6ZFa8cA3klTpTzut6Dz9wN9JY9nolF5ZJ5pS4H8-rOChu4lA8WGwzUtF-YoX65tEy_EnV-1c8eZ6fdo7CYsSw89C3oBxS467gF35i_UJ2M-gwBbEbU1DP-A8DOVPzIPfTHwCbgSufRaaOHFuKWVRyRW9Mm1ZZtq_ZWuscJCLxaEjTLc9w6P2CrGKwF2P2fWyTd_p_I2WHMaSHZHcSl5UvGdA2gwtku7f1LG4RwO8X67zbJd9AkqJbnADSEUJqFImPNZUlvqeUjDcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ جدایی داکنز نازون مهاجم خارجی استقلال از جمع آبی‌ها قطعی شد. نازون به مدیریت آبی‌ها اعلام کرده دیگر به ایران باز نخواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26166" target="_blank">📅 20:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26165">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gpxkla5ugiAZ38JWHdqNrPR4fIORMYLrvawav2oqdJnNj3TXLH90MwLA7rOooGopiB4ZdPvKd_6r9r9Dpp5RMbzaiI8F66jiZV8PYYcbMiYT7UdThsZEssN3_ok9bEIvs4Cw7GvDhOa8PGfJyPKrsDP5kObQvr1tuOHAUZlCrantBgFSgYFj1lar1gq6gWAKklVn7juaGNWPWLxngwOxjaOrQoaWA3YJqBUJBQ--avUZ_pzSPdlj9FDsB-iAA3vzsYExCvknh2JgFDgI2dJZO1NnPZbQYqwS4Oik75okVpxXOxKNLy0HDq6YqqVn9xBv1f0Uv_wK2apzri5zYv9CUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛طبق‌اخبار دریافتی رسانه پرشیانا؛ حسین ابرقویی دیگر بازیکنی‌ست‌که به احتمال خیلی زیاد از جمع سرخپوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26165" target="_blank">📅 19:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26164">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSwKaqIsQCnsoNcljkDpUkuhMdP1HWZ2PnZV9gy0f68kXpDQVDpfupKBIvlj0bgP4oXSu0ESPWpA9GS3RbA51kv6Tuqmska4bVD2awUvb8fD-AzRk78nIxNKqPpLnOSjdXH6eEUfGM4tL5hhaYGygOJa65ccfJQO5b715KJ-XBuHH8uWkR4j8NzHBCsr5eFoEt6kf3xylPfvG0X6mY_0ISUMU4sN826jEvgNr-5gs35OmmGc7TmmiGf5qlcyYv9oGbN_jqL0_Y7gfosraANUlCglWe3xfj6szjE4S4y7xR3hexTICdPS2JAflJbVT7ckpr56ulAeSpHzVXa3tUFaTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مدیرعامل‌ تیم نساجی امروز صبح به مدیریت پرسپولیس اعلام کرده تا فردا فرصت دارند که 150 میلیاردتومان بابت رضایت نامه دانیال ایری پرداخت کنند تا بندفسخ‌او رو فعال کنند. در غیر این صورت اجازه جدایی به ایری رو نخواهند داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26164" target="_blank">📅 19:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26163">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424844d43d.mp4?token=dBCQPLaiya90VVwfo37RtB8d20tIJ0z3wCYEfcVPLBctQGoAtz_YJjWi7fuJy01QtuyAsZ1bunwj_wElUbhlJaDTR8E1H6cNt2iOW-hGE2uGieUgZ1RpYs2hf5wZr-2_8JCAiesqU8n7XYO5UAFzJpCn35HNlNJoGO56B7olFdyWAlUt25w-wbrv4-vXvxhPgdpXHkEK649I1S5xM3baJf5mHtJxeOdcFwvYXcjyR5y9eErCSFl0IBKxWjM0HGboA1L60SYWtbnQcQfoHrnXH_LHxRoaqLF878ZCcABfEKBl4nrP9byuB-syaIUU42rxpA73fVmBg8TpGeAHYfHRaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424844d43d.mp4?token=dBCQPLaiya90VVwfo37RtB8d20tIJ0z3wCYEfcVPLBctQGoAtz_YJjWi7fuJy01QtuyAsZ1bunwj_wElUbhlJaDTR8E1H6cNt2iOW-hGE2uGieUgZ1RpYs2hf5wZr-2_8JCAiesqU8n7XYO5UAFzJpCn35HNlNJoGO56B7olFdyWAlUt25w-wbrv4-vXvxhPgdpXHkEK649I1S5xM3baJf5mHtJxeOdcFwvYXcjyR5y9eErCSFl0IBKxWjM0HGboA1L60SYWtbnQcQfoHrnXH_LHxRoaqLF878ZCcABfEKBl4nrP9byuB-syaIUU42rxpA73fVmBg8TpGeAHYfHRaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
خوان کاپدویا فولبک اسپانیا در تیم قهرمان ۲۰۱۰ توییت‌کرده‌که‌توفینال ۲۰۱۰ جلو هلند من یه سکه با خودم بردم گذاشتم یه جایی زیر چمنا برای خوش‌ شانسی و به کوکوریا هم‌گفتم‌همین کاروبکنه امسال.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26163" target="_blank">📅 19:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26162">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6zk_uAxkaI9K6EQqnApVgo5W_drhW-qd4RvG591yviT7qoCLTt7gcUuEGSrYtI6tP-8FUMyy4f9dJ2F5wSriyb672OLsPOhtmeyrPl8JCD7sFRG6kjpGxOAsjbfiXxI4gV7MVTpdC_gWm8Ej9GbzcbNnwcSI4rP_Gn0yqDlX_ymviMQZmFF7KbNEp3J_RzrQGQrPgVRz__sVaBBNTC9Y_R9QEpf-BcUHMjHwsUytvsoGWCjRJKUEEpaYwTHYgR4TqgQ5wpTD6ragke_w7I3PWXKue6l4Bg5tQZBZ-osjfcGTFXBapiUV38L3JxPSid1rWq-dwOGQEJb3ItKUQBA3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
معنای جامع و کامل کلمه آندرریتد؛ فابیان روییز ستاره‌پاریسن‌ژرمن50 بازی ملی داره و تا حالا شکست‌نخورده توبازیایی‌که‌برای اسپانیا انجام داده.
🔵
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/persiana_Soccer/26162" target="_blank">📅 19:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26161">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/021b11787b.mp4?token=gni6Xq9HbHGNKcrDWKCFOht6KapnsBo82Gk9DBUPslGae81cimUBQl7bxKHCsY7eOIj2xbMnKuYTZ1rUr5hcmzFX3ipYFeqqZ-j9wVcp3-R0euiRrxFORcdCZ_Vs_rcNVx8uXxzcVQC94nYNbM72Vu2EBtH_vDCNV_DrV4zXFkcH_6uEZ6-m_5e6BrQTGPw_DRytQqcbdC-klWLoKg1nSRgfeD61dM05AUSDcJPuLl9b9sPRM5m7uxrpEH53RgTmFaW3MHLO9iWnT9ITDXWLFeNPq22yb1GgN4wqWpdPL7leJYKQXTpQs6zmZa08KxNgAEWte2zWDExHs21H-f32Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/021b11787b.mp4?token=gni6Xq9HbHGNKcrDWKCFOht6KapnsBo82Gk9DBUPslGae81cimUBQl7bxKHCsY7eOIj2xbMnKuYTZ1rUr5hcmzFX3ipYFeqqZ-j9wVcp3-R0euiRrxFORcdCZ_Vs_rcNVx8uXxzcVQC94nYNbM72Vu2EBtH_vDCNV_DrV4zXFkcH_6uEZ6-m_5e6BrQTGPw_DRytQqcbdC-klWLoKg1nSRgfeD61dM05AUSDcJPuLl9b9sPRM5m7uxrpEH53RgTmFaW3MHLO9iWnT9ITDXWLFeNPq22yb1GgN4wqWpdPL7leJYKQXTpQs6zmZa08KxNgAEWte2zWDExHs21H-f32Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
جملات‌زیبای عادل‌فردوسی‌پور برای لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌دنیا در پایان جام‌جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/26161" target="_blank">📅 18:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26159">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/522741a6f4.mp4?token=FSzXXQfXFxXeoxJXWVuah_1gg4GUkBBhawvd5N12rqD9N5Slf1zhqp4ss47m0bEmX7YUlcrQFYP6Ull1rTCmmxyN1yclf1n-vZTFX1qPt5NEEhqDujw3MIhmd106p2hqoFlERzDN64dagA-DR-SxOHVZBt7uDQM6jWiV1bXtxbGEhDGAhDgDDO5pdwXRsve0RLHVFa1-hOIH2YmztrkxpKMDJCdhICFLL4TPz7_Rl26Qik7OMTz2e6FdjUg3rKaS3-IZQeebGwkiPFnazbtd3DRPLNwRKP-wkCJFsEiYCiWe6WjcL3gFVaqMTpYhhF_k4Rovn7gtfXIX03SS6hL9SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/522741a6f4.mp4?token=FSzXXQfXFxXeoxJXWVuah_1gg4GUkBBhawvd5N12rqD9N5Slf1zhqp4ss47m0bEmX7YUlcrQFYP6Ull1rTCmmxyN1yclf1n-vZTFX1qPt5NEEhqDujw3MIhmd106p2hqoFlERzDN64dagA-DR-SxOHVZBt7uDQM6jWiV1bXtxbGEhDGAhDgDDO5pdwXRsve0RLHVFa1-hOIH2YmztrkxpKMDJCdhICFLL4TPz7_Rl26Qik7OMTz2e6FdjUg3rKaS3-IZQeebGwkiPFnazbtd3DRPLNwRKP-wkCJFsEiYCiWe6WjcL3gFVaqMTpYhhF_k4Rovn7gtfXIX03SS6hL9SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوتی خفن سوسن پرور دربرنامه اخیر قیاسی؛
قیاسی از سوسن خانم پرور میپرسه که کدوم ورزش رو دوست داری؟ میگه ژیمناستیک قیاسی میگه خب چرا؟ سوسن میگه: چون میخوابی پاتو میدی بالا!!!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26159" target="_blank">📅 18:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26157">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/219a5ecb02.mp4?token=eXII67Ggh3dud5GQPS-edHGI8tWTe7gi3j3XRtaEw4liI0a9Mg0HuXpq0d0REtvsdfND1ZlhPByvn0TU034k-tbifrN1ac_m0j06qPuWz0HWgHFC8tCbokPCxYpvoZG4y29CrYfaJC4FqO0vbHTzOB9vSuaU2fQRuOMXmSm1EIondMSoF54E6DZioo7wSEA24BTZBosFkV-r8Poqi-QDORr6CP1uOWvbTqmvt-1o499yauJ-penynOEUee-o3Dif_Tt8kKGCR90IZx0UEvGsDyUv1XzHw9SKcLJGl57yBhPFulrPRij6JPqWy6NfOK_ZbofjCBfjRYT9xL5W8pWAPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/219a5ecb02.mp4?token=eXII67Ggh3dud5GQPS-edHGI8tWTe7gi3j3XRtaEw4liI0a9Mg0HuXpq0d0REtvsdfND1ZlhPByvn0TU034k-tbifrN1ac_m0j06qPuWz0HWgHFC8tCbokPCxYpvoZG4y29CrYfaJC4FqO0vbHTzOB9vSuaU2fQRuOMXmSm1EIondMSoF54E6DZioo7wSEA24BTZBosFkV-r8Poqi-QDORr6CP1uOWvbTqmvt-1o499yauJ-penynOEUee-o3Dif_Tt8kKGCR90IZx0UEvGsDyUv1XzHw9SKcLJGl57yBhPFulrPRij6JPqWy6NfOK_ZbofjCBfjRYT9xL5W8pWAPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دخترهاوقتی‌امتحان 19.75 میگیرند
🆚
پسرایی که امتحان 0.75 میگیرند و درباره‌اش حرف میزنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26157" target="_blank">📅 18:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26156">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDVI4Ih734csp6MqKQ6TnCJHcnPRbg4aA_RPt8Dfww9PkSH-Lw5VycF6A34EMohVrfgeQLJiToi9Qz5kKEqlokj2uy6vl6fFL8DSQKXF6MsEz6OeqKVbdqlidKq5Zi-V-pduVR0QONfbZEg6kisXKXE48LhMBmL7P9PtRg0eriHUOMF3YSxkx3W-khnDBLE0COksrnH7hyAuz2V--jJWVEm_Lc39J3ZAduKxQXXXAmZL2fjJn9MOvncujcBRbVKo7dMM7RP0AcCfyNUO2Aa62zs0WhVU_Dc3ZTG1c4c64H7_5sD77iI9ziK2U0H0odgW1Qvr_xqOoJX9hZVCDoICuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بهترین گلر شش دوره‌اخیر جام جهانی؛ بوفون، کاسیاس، نویر، تیبو کورتوا، مارتینز و اونای سیمون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26156" target="_blank">📅 18:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26155">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gwji0t1195iwZ0cQ7H8EYU0Q7e96ulPbI2C6UhyRjLTmoMhOMoIM5JLtXufZS_3onGh7Mkxg169Oq9qlVlbGqPPaskr4RB1DRYm35l8PpLYpMTm9BusuKdXAJjltxgn9LxGLBEL-h5gjk8TYpHwA9vTr93EpuSBsiKTgOprk7y9Ivmo0q1yEd9R2Rc80GCsirhlmIhNQNjD_tLPXgx_KgaORNG1DMpZa_mBTxKvES7LuXAGwpQNiGyyCYbOppvoRW1A-w47CzcBVEisEXHo1kjFw1Tdb_WAJL9p3w3yz9G7UtxnPFKKKwIn_cJoDary2i_ktJbmlJ90O4Q2_du4oiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی پنج روز پیش پرشیانا
🔴
محمد عمری26ساله باحضور درساختمان باشگاه پرسپولیس قراردادش روبه‌مدت‌سه فصل تمدید کرد. حتی مدت‌دقیق‌قراردادش هم گفته بودیم. عمری آفر خوبی داشت ولی تارتار مخالفت کرد اینم موند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26155" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26154">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b054f61942.mp4?token=ftoNlglP3fXsAR_5i6bmlxpyg_oXmsU9dNNcvzhu_aAEQuyaUOeGJDbbjMPJhpa10IYnElgxWG7Lj5dLD6QNqJ3m7W2P7_EUcZqCD78LMudK-SYpGoRnHWtnETlpAAZLoxxIpIR7ooJD7gCJxp3qWI_NQwL2L1icdcf2R4K-M6fUVjHvEuXUBWESidf7WR-T6XjaQzgLMXznBHn_R7KKJMbbJz3SQ-wn8NUSa7HdChMBVo2AOFnVrKBQ9oXl9EWwSw0iy9FXZ8j-lPUsAHRBW_KfeEQrzGDedmI50meFmrOgWxlhPM0TMIg97Pju_dJ66vXlSR_8p9eySGFKS0qYQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b054f61942.mp4?token=ftoNlglP3fXsAR_5i6bmlxpyg_oXmsU9dNNcvzhu_aAEQuyaUOeGJDbbjMPJhpa10IYnElgxWG7Lj5dLD6QNqJ3m7W2P7_EUcZqCD78LMudK-SYpGoRnHWtnETlpAAZLoxxIpIR7ooJD7gCJxp3qWI_NQwL2L1icdcf2R4K-M6fUVjHvEuXUBWESidf7WR-T6XjaQzgLMXznBHn_R7KKJMbbJz3SQ-wn8NUSa7HdChMBVo2AOFnVrKBQ9oXl9EWwSw0iy9FXZ8j-lPUsAHRBW_KfeEQrzGDedmI50meFmrOgWxlhPM0TMIg97Pju_dJ66vXlSR_8p9eySGFKS0qYQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
قالبی بسیار زیباوسنگین از فوق ستاره هایی که باعث‌شدند ماهاعاشق‌فوتبال بشیم. چه زود گذشت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26154" target="_blank">📅 17:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26153">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1819c235ea.mp4?token=Ck7P7AEu0KwMsSrXKHBF__0CJSKilthTldDGjQVku3enkwDDNAVtxuERuOXymQMhHlM_gSo1PCTrUyrbrVQRfPeWGTPd62V0O0p0mmwqZnjEvCR8qModY7md6V6kFyhJTdlkOZngOUeXxDdjXztiY5NEE_qmWLJFx5-AYi5Fo8MKRYjWZ64oAB8xYJ1Ez-8rQYBxPmEoMkh0cAvgHyqXWzZOj1MwZL8-TWk4WvdVd7FEQVhQWTtaRksHt-lIo-XgfdijOiAzgzzuN4N_PAdMEdlZe_I7n1MhhA_OP2FqmjbAv9SdTvmPJjtdncubhfMnioORO0p_mKKJbVj32zHa-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1819c235ea.mp4?token=Ck7P7AEu0KwMsSrXKHBF__0CJSKilthTldDGjQVku3enkwDDNAVtxuERuOXymQMhHlM_gSo1PCTrUyrbrVQRfPeWGTPd62V0O0p0mmwqZnjEvCR8qModY7md6V6kFyhJTdlkOZngOUeXxDdjXztiY5NEE_qmWLJFx5-AYi5Fo8MKRYjWZ64oAB8xYJ1Ez-8rQYBxPmEoMkh0cAvgHyqXWzZOj1MwZL8-TWk4WvdVd7FEQVhQWTtaRksHt-lIo-XgfdijOiAzgzzuN4N_PAdMEdlZe_I7n1MhhA_OP2FqmjbAv9SdTvmPJjtdncubhfMnioORO0p_mKKJbVj32zHa-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
نیکو ویلیامز ستاره‌تیم‌اسپانیابلافاصله بعد از اینکه مدل‌روگرفت به این‌شکل به مادرش تقدیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26153" target="_blank">📅 17:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26151">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDrapC3UBPwyIsU8isPUh_co1DNjOGC3usEVjbDbsQO0Qb3xLJ0sc3c7JGRFXAJRuFLNFk43bsMCWMADgEXin2umlrYwMkG85ezujsnxF-wX-T0POYkxNT-_3VtpangtvLKj3K_i8_7Y90feSa1dP_HPAREm1YS6zYT6yGZk7xVmOplgAgnC6wLBgnpJCfymbWcXS7QeX1ellt2QVHwHcN49te_gxhUohoKq_Z7huslCtyUSm6W-G0DlVTIGg09vBo4cmi8DKaLRx4yaOy__6Oj0NLx_SDa8QAOZUJr2afEnFXPOsPureG-TJVzLGOsNt0U_vBzoLIWGwDIXCbIyGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بهترین بازیکن 6 دوره اخیر جام جهانی؛ زیدان، فورلان، لئو مسی، لوکا مودریچ، لئو مسی و رودری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/26151" target="_blank">📅 17:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26150">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DU17TQVc26_6G8nxzPgl5CkTaecdFFVt0ZAdgmGaOUHrmpzgy9jZyKXhZw5igD_-k9ETk_uMn8HYrEe7hw9PWO8eT5RBxeWLod02gPienLioyybq2NQy_M5Jlnbxl2U7VF-MlppBkpIV72_q6hJeeodKMvKEvfiUy4NsNKgAf6aE2n-Qw_t2DyU_tN8SAtsb-NI9Atn1f_Kw6y16exQLW4z2cbmI_JkrWKa3nz5VomVYrbirkWpw6R1JUJHNPzHnjyKzNCikGnjXKk_mYSGDSZOzVgACT3HRZkr8hx7BMgyczFc3gHNeP5lfH5KItObztInKV4mRRQEdR04aRa5jCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
درحالی که با قهرمانی اسپانیا هیچ گزینه قاطعی برای کسب توپ طلا دیده نمیشود ، فرانس فوتبال در آخرین‌آپدیت‌خود درماه آپریل "عملکرد فردی در تمام مسابقات بزرگ و مهم" را جزو ملاک‌های مهم انتخاب برنده توپ طلا در سال جاری اعلام کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26150" target="_blank">📅 17:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26149">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afc40ade6c.mp4?token=BNhmoJqU0cFdis5LCtTZ-e_jHqzxSrGaOZ8yfQX2JE2dHaJGk_gQ6454FrNVpNDZ0zOCQK0lAX-ieD_C9dk3LVkoKS4gLqRzVvnMVaNItKWTPmoogWkvH2KR8LGmamKzfPYyDkFA5PWH2FyGDcAhgSWNV3rMAbMRDm6YbNtMtSo7RUmvqPiy5__gae4Yo7aIG0hDp2NQtelbNas96OOc0lscXQt5RAcSD-DnYoW1k2RX0zEHi6hP6ats7ZmXaef2S7QkvSCRJtnpP4vKwuypnhWUw_jKsPgL2F0UD0a2UFDQT_gGVyMCaufZugHyUvk8Tz6-wiQTNPlavj8BylHc_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afc40ade6c.mp4?token=BNhmoJqU0cFdis5LCtTZ-e_jHqzxSrGaOZ8yfQX2JE2dHaJGk_gQ6454FrNVpNDZ0zOCQK0lAX-ieD_C9dk3LVkoKS4gLqRzVvnMVaNItKWTPmoogWkvH2KR8LGmamKzfPYyDkFA5PWH2FyGDcAhgSWNV3rMAbMRDm6YbNtMtSo7RUmvqPiy5__gae4Yo7aIG0hDp2NQtelbNas96OOc0lscXQt5RAcSD-DnYoW1k2RX0zEHi6hP6ats7ZmXaef2S7QkvSCRJtnpP4vKwuypnhWUw_jKsPgL2F0UD0a2UFDQT_gGVyMCaufZugHyUvk8Tz6-wiQTNPlavj8BylHc_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تمام امتحانات نهایی پایه‌های یازدهم و دوازدهم چهار استان هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، تاآروم‌شدن شرایط لغو و به تعویق افتاد. وضعیت دانش آموزای  بقیه استان های ایران:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26149" target="_blank">📅 17:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26148">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQKQSmtSdvDVz3lhJvrWENplYYvkJHQUSpnJu_kUfBrCm4t5Ru747Gwbft_oBawQnLhou3t9AJhO2GAqGt5arHKLpNCq5NLQzZzTVVfQQi37fjpihyGsovLcJL_shBirCXaBrTSqzC6-SNeagMt6gjy302u_hDFIOc8riIirhcpJG0kYefXg-r_EW0MHg0ZEqLruVcdR_i2dRbMIhu_JPFRW59eGUnk_N4vkO-GbklqX3D3_33FoO7hfs2crBDwrB_onGQnfQOXmYO-vNnw1QB5U937I8NKEJerG_DpK-XEL29SR_cKhIV7fOoRcT0fQ6mIMAfX9CZlKThhkBaUVjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
تو نوزادی مسی با اون همه افتخار نشست کونش رو شست. تو دوره نوجوونی‌هم‌یه‌کلی جام با بارسلونا برد. تو 16 سالگی‌قهرمان‌یورو شد. تو 19 سالگی جام جهانی رو برد. این وسط هم بالای 10 تا دوست دختر داشت لاس خشکه میزد. این بشر دیگه از خدا چی میخواد؟ چی روش میشه اصلا…</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26148" target="_blank">📅 16:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26147">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/II_JLnEnHNf01ow-_JoEOfXPkGZJPTMPPsZgZAjQBnVSc5eYtxLK3F6XpYazNVFsQb3rZqQAcW_cjypjSRLqH4U8wzaGPKE4_XRuY3vTEj6BpIn1HzD2YnVgRYtAZsIR-x5JI74En0CmGNloTRM8ctfUkIgk6DDiVq_5TzHV-zpfw58j4pzQnV4fTM-6StfzVXPSVlk69uMyWN5dKCTnNyoRIGiKKytnKQl4NIgojT82GJAgqZlMUNMlx64rz-TOEn92xiKe-m0q9bquu5iGei8kNZKDZAyhK-mLJEiiTFoUYi6kL6f1S5z_ZBBRPqoELLSCttClambp75oF3ElMVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آتزوری‌درحال‌شخصیت‌گرفتن؛بعدِانتخاب روبرتو مانچینی‌بعنوان‌سرمربی؛حالا پائولو مالدینی اسطوره میلانی‌ها بعنوان‌مدیرفنی تیم‌ملی‌ایتالیا انتخاب سد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26147" target="_blank">📅 16:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26146">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBMpCvjSE7sDw5h2T8P9luNWKd89i19OONPW8AvC43MvBq9g8nAOp8fz9xcuUJlgzR-6qY_-f824-yByLyx3ljEWNEwGtlEIz0i7RhGDnITRI_Eg1w2XcRhLk6tZxwyowC81ClqcPNB7vhlCnJbmDIUdV2su3RFiWBahZzYs90O_1rU7iV4XHzMVzANEoOp_FK_wO0JZyPi1XKxmTqqQ76xGidv2wWrvEPhV3Jw9KjDfL0jQRtE97LXIWpG8-7rhP3jMG-8wyD-CZR29I6meu2BtQHR8riosBi003nR95VIw5CRy21g3I5R-L_WMhhKDifJYL4_ZvULp5-sTW79ojw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛بامخالفت‌تارتارسرمربی پرسپولیس جدایی محمد عمری وینگر سرخ ها از این‌ تیم منتفی شد. ضمن‌اینکه محمد عمری برای تمدید قراردادش با باشگاه به مدت سه فصل دیگر به توافق کامل رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26146" target="_blank">📅 16:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26144">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o80eQMn3AAuREoEtJMjYj5B47RFV3mbG_Etd8G_99ZYBtzd6Cb_IOUf7i0s-Mh7OBZEx-yS6OKkd5jICW0J6uu63cl-wsQZtN1l3ITRZV6anzOXLliIOvZbm-5dxVkc7ctH7wLLeNERb6ZhZWC6s9yezxkCuDN2glQ3xqnKDorpjc7Qk7XMjuv_mGYicSFZsUJSr2-UoeAtPBbBg_sxke7_JnodNiJ_mFuAXSjmEcy5Hj-GghRS8dW1nMLMvfkGilKocCM69L3PMnWk-qNttWfLN2wcnUJKhkmepJED--JfwEb2qWbPLY1_l4iVu762txJKLlW3RvB54uVjd8QpncQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kj5xuy8zXFeP6RSyml8wyO1sJ1UKWU61MBgtGx39o0Ivf6fQVevSDv1a3RPw76v6y-6yz7-x42uIPOIueCweebAwGNKu4gSdDe2QhrSNKkzl683lWnV6nbKX9exTYqhcYIvP9jvc0OXbJ0M-XHj3UW433IShgy4CBiEoMSkhGvMUz0zt1jdd2bvPYrSoXfGg9nHqrD2TpDeVpMqzEx9DoNIDRKGGXgOBHBwoniknILXM0REU3f-GYvzAZ_JD-nm0u_DezbiXHV3sAk0r67rXtfXQbJt2nurfOD2cWCqkFJfNsCiOaq3wzt21fffJRko6zpZIAsc0M3YX-tmpWh7xRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
اسپید، یوتیوبر معروف که بشدت فن کریس رونالدو هست‌ شب‌گذشته حین اجرا در اختتامیه جام جهانی مقابل‌چشم‌ میلیاردها بیننده رو کُتش "فروهر" نماد ایران باستان و آیین زرتشتی داشت و به شدت مورد استقبال ایرانی‌ ها قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26144" target="_blank">📅 16:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26143">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMnw_6o_fcVcTI_P8PjxObB-EryAP1pZwHpR727-d6J_llY7jJ4E-y59u-Wc4JRh7aKbNyVE_8ZxfclSxejurA9QDQM4mhV3SeTFgOBf7MS5S2IBTH84YpAoQXeNFThaS9sVW3yspfl1UG_N3K8moq4HuLQBg3X7GBD6KFL8Seee_rvLGf7Kksic7_yY0ICwIPGGIUm_laCrsgud05Y2WPRInFysdtYLkD1WD_UHsYyofaVoWT4YMcpmdo21FCn5XhowSn62KxenVyqtMX5YdaxnTKSiK669cNcqb-qDPxuI_CMkfcfyWh5b_Hwm4xyjqK7NxuMQyp8uXacv3bux5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لئونور ملکه‌آینده‌اسپانیا: بی‌محلی به گاوی؟ من اصلا همچین ادمی رو تومراسم‌دیشب ندیدم. بچه‌ها فوق‌العاده‌بودند و یک‌شب‌استثتایی برای تموم مردم اسپانیا ساختند. نمیخوام راجب گذشته حرف بزنم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/26143" target="_blank">📅 16:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26142">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jX_fvPCNN91ciWLmSFODcfVTBfEaE6QZnzGVWwKUBYayRp7hw7snlrRCwsgTBLe25zK_I0svoNECU2M_emap5Cx7Tf4pmhfieCxt11UMkeD_NMs74opN8MstZMeuDNZbqNGRs79VH2t6sBK8Nfaq-9T4J0Kp8J74iV3FYJuqH4Ru8vW-vokDbgIj2de7IeXOtq0JZd1S5EjYtizgqNrf_sgLF-TN-b7CNj48iK2OiRl59Q9e_l1XWct3h56D-gjAmgXZWUexkTq18NUZLMUV0TC4PgLnws_ERPur4ABtTmtBEYJA3J8fLkE_qv7aBpRBQH4mvwNskSKhLU2mdveDFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لامین یامال ستاره جوان اسپانیا و دوست دخترش همراه با کاپ قهرمانی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26142" target="_blank">📅 15:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26141">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrL1Sn_dHfs1U5N7-V8M8opO5g3I8wuKnCXwKQCzdo_ePXabtN0Pgtcfyp0FJ7YQfhVlumXFIQp4PwBccNkieJpsZYX98Ja1ayBBDBl3NMEGPzvZ0HxMTP166cvruWreT_GGAQqiewt8SzCuX3Gs7jIZmxEXYCYW2ESEhCzHshqI6RgehZm5UfCjdflIEHcOE3ygXG7Qn2mGSah471DO6GT6Dqu0C1rMCMFGHnxRODhhtTCfvRmfk8UYocVwyppRTjyJI474WCMKFibI9tcgP4iYhRWrI0nUJGAD9D8HoeEOFtzyKmXWbO29Ap9FN9EUhy1xYxCiXM25vsPQWbTsHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
وحید امیری کاپیتان‌سابق‌تیم پرسپولیس به‌مدیریت.این‌باشگاه اعلام کرده‌که درصورت تاییدیه کادر فنی سرخ پوشان علاقمند است که یک فصل در پرسپولیس بازی کند و در پایان فصل از دنیای فوتبال خداحافظی کند و به کادر فنی سرخ ها اضافه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26141" target="_blank">📅 15:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26140">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6473e7bf72.mp4?token=j-_j_BB46FLV7xqSk533_ZHat7wuVzP3iuXQ3-BjpcgZuc4WV6ru6D4XxCqj62MhrpRymqS_mz809_Z5T1I6qRSs1FW2VetJAErY9J2oeFHbaH9hXfYNxvJ_qldrnK67_9SdTDtx1E3htlnqAjgSrp-ppfTNuPzwsI2kM_pB3CEA-U3CExg1E93mTF0QMa_icXgjd_cDcBtrwDTb2if0urp3c-NXvABwoDWUxyxVBGkgKT62wOb76k3Ef8BYZJkfm7d77u1IOwOtCs6aL0CXucVSwsUu2xPX_dwQOtpbf5P3E2iEuH6PWfWkTU2Qem468DhrgsKsMLByWx3VTFDaiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6473e7bf72.mp4?token=j-_j_BB46FLV7xqSk533_ZHat7wuVzP3iuXQ3-BjpcgZuc4WV6ru6D4XxCqj62MhrpRymqS_mz809_Z5T1I6qRSs1FW2VetJAErY9J2oeFHbaH9hXfYNxvJ_qldrnK67_9SdTDtx1E3htlnqAjgSrp-ppfTNuPzwsI2kM_pB3CEA-U3CExg1E93mTF0QMa_icXgjd_cDcBtrwDTb2if0urp3c-NXvABwoDWUxyxVBGkgKT62wOb76k3Ef8BYZJkfm7d77u1IOwOtCs6aL0CXucVSwsUu2xPX_dwQOtpbf5P3E2iEuH6PWfWkTU2Qem468DhrgsKsMLByWx3VTFDaiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیس فوق سنگین روزبه حصاری بازیگر مطرح سینما به علیرضا بیرانوند
: اینجا ایرانه چاله میدون نیست. با کشتی گرفتن با بزرگ‌تر از خودمون بزرگ نمیشیم با احترام کردن به بزرگ تر، بزرگ میشیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26140" target="_blank">📅 15:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26139">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6MM_CjV1nNQ2GYwnksG6ZpeyyubcC-g93TDHgY7vK_rOuiEvTI22uqt-nsk9VGCFTZzOu9j0M_gz9xV3eC1AmjFrDMNRKwJ-1nYn0WhXbWWDN3UFOaTyA1BNVmbeT-mhAnSLCKY2GFlJxInjvj7ezJ_J_dEAugsjiGbnUSGMk5gpz_lyufHsMto9nArJ0BmX0tTAmsVIC64m2U40PZ3LCLqeMr0KQr9MJrfOyp-EGG-_plr9j89_XLOGXkd8z47DX9knv5HD_zYrheWwnwHbPj7u4q84Zls-OXybsDtt2ws8FqDyedmabzF_Grv9doqrnWShCt-SA-FkLw-w4faBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استوری شدید الحن علیرضا بیرانوند علیه علی دایی اسطوره فوتبال ایران: من را با رانتی بازی به جایی نرسیدم که الان بخوام الکی جانب داری کنم. ترفند هات دیگه نرخ نما شده آقای علی دایی!!!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26139" target="_blank">📅 15:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26138">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_lA8VynBcYPCWS9dF9do3mB3RzjsJlvzRUMV-VNVu80GLzPs2qFyRQZLJ_rSCdml5HGUrUXkKgVdR7o1D1YQbA6YD6BTcYdpVw81iw4rUzMN-BHzJdiV2sKQwtJvxqEkQZCA4QT8VQrWT11cbefzVagIf_xdOGTFMauRC5bhJhYDg2qyuA_mlYpiLnL_9FnvuzzQkoPjlLyPRTptZWdjjIjkEc0hH-5Lly-ECu3IndKl6UwjteY-nz_8lD5AMfGaIOq35mdrKwtGNLCYtsfy7TaxJVyJIUr2ihnFMu9q2IlIbR6OzeYo8eBBi72f9_WowdWp0CwsWUDluCXO_L3Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
آرمین سهرابیان مدافع میانی سابق تیم استقلال باعقدقراردادی دو ساله رسما به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26138" target="_blank">📅 14:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26137">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dNB0t2JVPVbbH5NdKqwN4-xpEwJ5E03BdEPREJLGjtluKDgTpCPDtqP4JN0he1kcaENu350qpwnKIzHyrbkBYucx-lemadEMS4j1xuzmD0_k02pCF-axMgiA4cba9EiYJY8luU_cGHcEhZodFhVOL154RB4PfT1PFmydflxh9MF21hHlAKrrIy4Rdjlwt4OAy2J4RYv52yDj8CnvD_nS_6TymhDZYeXQ6v5drCP2vWJFyh8UN0MOPysJg5t-Yy1Ub1DaZGgfhYip8Wqt00LOrdKq3N1L00A-1vOjHmAq5pf-zEEjPnS_yqDVhspmmLOh_795qlVaFYZ9JxoJ8ZqVag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...بااعلام مدیربرنامه‌های عارف غلامی و آرمین سهرابیان در ترانسفر مارکت؛ این دو مدافع میانی از جمع آبی پوشان پایتخت رسما جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26137" target="_blank">📅 14:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26136">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه فینال جام جهانی 2026 شب گذشته عادل فردوسی پور؛ برنامه جذابی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26136" target="_blank">📅 14:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26135">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBSQ6_8aGhsAVzFFLvf1lWgrwG8f50uF3oEvzJvRfcsThS3i6aohZQtplifVh8GJ8ceCXHKcQG2mQDADQdL_CHQn9IEqY9nileYK_w1Raea7F8IiBzm-qHIWIF6yYKFdDTD2-kxztIFpmlPf_z6wYxIJrSBTHq4OBWb82z8WqjHMV75zMdxVDbbcVJP44bKgDV317_xGI_z2b-oG_Q_0XZ1Py9GZCBDXuEgEcRCGTqMdoIeAeOYsJsZ01N-XNrBX3icUu76YMefSrC0izzrWhRwx2dIeoX6yQP9lzuiwotwNW3vt2TqAr1NfFUwmj0rxNnJw-bQerpBTamdF_UvtRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق شنیده‌های رسانه پرشیانا؛ مدیران هلدینگ خلیج فارس از عملکرد مدیریت‌فعلی باشگاه استقلال به هیچ‌عنوان رضایت ندارد و در هفته پیش تغییرات گسترده‌ای که مدیریت آبی پوشان رخ خواهد داد.
❌
علت نارضایتی هلدینگ بابت هزیته هنگفت برای جذب ستاره های خارجی استقلال در…</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26135" target="_blank">📅 13:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26134">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HaTcZj3xIJNvdu9UZxSiHmh24rXm1rMj2cAr6d74EBGZKdxUjwSM49oDpIHkDw-v5_L7UmAeivTbmxMy6KfPvzvY2zFuFHclxCTFQsgdHk43wfeTg7YnIWXmKJDepWEMabSOKSwfmUFqUslGDMLFPmtQRGskt9Oj5Ft2fbAiVLYHcXkaE1vUNIDBXwPzG9kR-uYBs6ugJ91KlBR8bUyTN33nRTilDQ4RfJfEs2VodfPyX9DbEPdNPKJklamcvvpWuvDBlTwLyvjSyEV-PIXzGDXZmUQw2kMJrORNzqlO5b6TDGmwKaYBY8qI5PtbxdhWSziCT4EzHqTuP3DQU5KuCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
🇪🇸
#فکت؛ مارک کوکوریا مدافع جدید تیم رئال مادرید درمرحله‌حذفی‌جام‌جهانی تا فینال حتی یک‌بار هم دریبل‌ نخورد. یکی از بهترین‌های این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26134" target="_blank">📅 13:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26132">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tu9qxASy2zipFkPoClvcpyOjawqpPnW2mZ6FreY9D1_jSvX60_MdYojoFqCC7cx6hsT5nGj_FKK4j5kp-vtE2ffXE7lT1ToU39rM1Yg9ihA0dNMftq0v1U4FUXhsV03S_at1tt2bcULFuFeENcXqMjHkoM8P285WW5ZXbhvF5XnVS_Moo-rHP0LjpHsi8_sZ_DeI7Wra0v_Ag2C00p3_kl6Q2OkHOB_pjcnxB85bP9bbMPTfr52G6nMeSXPw4wbzqotvWzL1T0vyKsZPsj8aPee8UIyUaO0ozS3zSsTm0bRPD1lwjULH1mdAlPUL2_aIxYT7T67h6wAo08tAdznY9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
◽️
🔴
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه نساجی بعد از جلسه امروز با باشگاه پرسپولیس رقم رضایت‌نامه دانیال ایری مدافع تیم خود را از 190 به 150 میلیاردتومان‌کاهش داده و72ساعت به‌ مدیران پرسپولیس فرصت‌داده تااین‌رقم روپرداخت کنند در غیر این صورت توافقات طرفین بهم…</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26132" target="_blank">📅 12:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26131">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arNMpz_iMZ4m2KxKWQ5uTA-1K_3b41ljmInAIIQZgvsFm0Erhne3u6a4a0-0bsozeqU0KuHjyNlgofaZfdEpw9sliZJfABvDU4H7zkOvCj24VozYTiIkVQ23HXX-R8HjBwLKZMtzP8IZjAVMEhAr2kbsjIvG0KwHih7Lr7agwfya6BoMC1YfLf9hazPVJ3hk3HSqFb5x8cs4Uf27_Jm-KWSysdvmL510t-bzn_14e5dnL8gdckg0tWsOH2WqxSn0rf0q7VQgInnwt7t1YB00xXxXv0ZKpGPnE8a3ZzTOC7LXXLikTcdfAYL0HtPTPF2GWzHiaKpHAMyjHvTS8MhnFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون بریزه؛ میثاقی روی آنتن زنده شبکه سه خیلی‌جدی‌گفته آه مردم غزه  ایران تیم ملی آرژانتین روگرفت و باعث شد که این تیم قهرمان جام جهانی نشه. بعد همین شخص اون شب در گفتگو با گلر تیم قلعه‌نویی‌میگفت این چه‌حرفیه‌که میگن کارما مردم باعث شد که تیم‌ملی‌ایران…</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26131" target="_blank">📅 11:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26130">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwvQ50SkgBwvBaY517Op_8X9gGiLK8FCkkRQS1p-jy98LB6QALWtPOcNlbtLohhqAEoII28IHGfzMyQG_ZwDi110OogsT-xIgPuMNy2YJFaUncdSQpKxURc6mNeKuXE94QXlQkCXIeXBAAUtqnu__9TwsBU1b96PBjQPAs78KM_NoHzTuuEJctgDz4uknnieTEZ2xsyluug4mfuVLgJ7V9zkO8YjV38fObb7L4xCttATmRrRepo20jM3NWl_19Iq52LjMWj6weH7q9qjYVOYt5Jyf7j4ZLJu4WSyqgsI36wMiVoZjtfbWCc9bkqYl9oqR14KaQOWrJAKww3GsZsGlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون بریزه؛ میثاقی روی آنتن زنده شبکه سه خیلی‌جدی‌گفته آه مردم غزه  ایران تیم ملی آرژانتین روگرفت و باعث شد که این تیم قهرمان جام جهانی نشه. بعد همین شخص اون شب در گفتگو با گلر تیم قلعه‌نویی‌میگفت این چه‌حرفیه‌که میگن کارما مردم باعث شد که تیم‌ملی‌ایران…</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26130" target="_blank">📅 11:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26129">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADmoEYp2l-Sl_6pDtQpIPDmP6wPL-yCvPl45boid0HnrPwQwI64nbve0ySgRccF2FqQe2GY8-XFChTgSO7UZquJ30o-C2QjZCAjE6-4oLXz87eO1P4JH-SeuwqbaijeINkkWZImQb8YpVhkrZ8o5R_UWEhKCSuGsdqjnEqBXpoM2WAJK-QgjCDZ84b6VK54kF4xoicDHoAJgcxdWR-2eZ9KDlCS1qgbtvdgBwitdKbFtdEQBaCUDX1GPpi_piygLxn8FM9T0KjuMf8YpQYucaFwHIn-9_c2QthCLjbVOGVjLyw5dzfEg0_5jvL5t_usKyjQjHMu8WT5eVQP50EvTNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
#فوری؛ باشگاه پاری‌ سن ژرمن بزودی قرار دادی چهار ساله به فران تورس اسپانیایی تا تابستان 2030امضاخواهد‌کرد. تورس به مدیران‌بارسا اعلام کرده که‌دیگر‌علاقه‌ای به موندن دراین باشگاه ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26129" target="_blank">📅 11:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26128">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/202f77d369.mp4?token=mNivYloZQ7LMgtjUxGCSEM6GEL57o51OlpYUQfRLlagDUZ7NtK9YQkmfulLVamMSb-KOBo1-AVxbUIvaV4rlFIu4bPg31cREUstyv8OSea1WTZ1_oJ2DqLFNdmPA5gx5wjTKuvetRpragiWw-Jw4di_j6yYux5xMuVddRhMReWCzF9aoN7oJMiWpeEfonStoAhOzL5dQ0EQFphNd7-15yxlFtUqHQbWN8kBmjSqtt9IfglT_OsREW3fAf5q_cFdq8GIkShwAVG0noByKerzBZow-eLuIwZQUnpSfafkW_oYP-PG2LQeichhllyvWBZPURugKCeEDBzRNTI2GV1Ul2oM7BTRGseSVC3aI_yMzoW5DNLxEQ4i5vKM-xvMyNl3kCuOI2BIWbuX2ivNfoGuIdKeofeUMHdBB2Ms1-1win6ZuQ09kmIi7gJJy5vsiJZx8Xiigfnr0aQkvOlqa_nSvHPHGL8yKXNV6tS74oSZEoZOIJB153pkAJUbyBI-79OnLKjlirY5RoAm6HS_tQS5pFhONMAz0nujmR__EHXcPYdWNVyA3BQcDOX7zmBhh5XmoLTvx152LDroD_M-m7gLY5mx_WWQJiFsLUGGRe4hLWpRqh71CFlMKKq6jsg6vCQ3MVs20Yl5drnVTJRhiyfp4BnyTODJ_fPmNKXUVcDoHvJM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/202f77d369.mp4?token=mNivYloZQ7LMgtjUxGCSEM6GEL57o51OlpYUQfRLlagDUZ7NtK9YQkmfulLVamMSb-KOBo1-AVxbUIvaV4rlFIu4bPg31cREUstyv8OSea1WTZ1_oJ2DqLFNdmPA5gx5wjTKuvetRpragiWw-Jw4di_j6yYux5xMuVddRhMReWCzF9aoN7oJMiWpeEfonStoAhOzL5dQ0EQFphNd7-15yxlFtUqHQbWN8kBmjSqtt9IfglT_OsREW3fAf5q_cFdq8GIkShwAVG0noByKerzBZow-eLuIwZQUnpSfafkW_oYP-PG2LQeichhllyvWBZPURugKCeEDBzRNTI2GV1Ul2oM7BTRGseSVC3aI_yMzoW5DNLxEQ4i5vKM-xvMyNl3kCuOI2BIWbuX2ivNfoGuIdKeofeUMHdBB2Ms1-1win6ZuQ09kmIi7gJJy5vsiJZx8Xiigfnr0aQkvOlqa_nSvHPHGL8yKXNV6tS74oSZEoZOIJB153pkAJUbyBI-79OnLKjlirY5RoAm6HS_tQS5pFhONMAz0nujmR__EHXcPYdWNVyA3BQcDOX7zmBhh5XmoLTvx152LDroD_M-m7gLY5mx_WWQJiFsLUGGRe4hLWpRqh71CFlMKKq6jsg6vCQ3MVs20Yl5drnVTJRhiyfp4BnyTODJ_fPmNKXUVcDoHvJM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
گاوی در جشن قهرمانی خواست لئونور دختر پادشاه اسپانیا روبغل‌کنه‌که لئونور پسش زد و نذاشت بهش نزدیک بشه تا به‌نوعی انتقام گرفته باشه. لئونور در عوضش با پدری برخورد خیلی گرمی داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26128" target="_blank">📅 11:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26127">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1NAt6bDxlhKSMiH01oifUdjhz45zs4j7FkP2oEcEYsxq2CX5P5nf780BGuRD9OypnjWTrI60Va7zZ9mpvfEXt4LJEdy3Vm8WyBYRiokvmwYa4wkyVADQrSZQ40aNWxIaC1xF1d72gCCJtmojg67L1EwnDlElBmrzl085nR7a-EhOqIlWMt7m48P4KdbAiY3ylXM5YdzVnqnh-MNNkgVrwfj7g6SVBeD3AambnLpgP3cN9xkILcaUGrXRRuS4N8nsfZDK9NPEf3QJ0EwQGGuihzQuvO9LiiEmR_-MJkam7NlrPbsCMO3JxZhtkwezb4Hit1rs5FMo_tqbmyLQG5ySg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
طبق اخبار دریافتی پرشیانا
؛ رضا شکاری وینگر فصل گذشته پرسپولیس دو پیشنهاد از لیگ ستارگان قطر و سوپرلیگ‌بلژیک‌دریافت کرده و به احتمال زیاد درصورت‌توافق‌راهی یکی از این دو لیگ خواهد شد.
‼️
پیش‌تر در روزهای‌اخیررسانه‌ها مدعی شده بودند که شکاری قصد داره به باشگاه استقلال بپیونده اما پیگیری‌ها نشان داد هیچ مذاکره‌ای انجام نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26127" target="_blank">📅 10:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26126">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27dd0a5169.mp4?token=p-IQsDr-xTHXPhp7W0lBL0Bg2WFGZGJn1gIOpA5Z2o-KXkUNSJ5rk8MDHFzO-6N7GJr8R16uiJuzRTAIT1Gt3E51AGMZXSmbirfPpMhzjxO1iKYuKEizQhOfajr4DDwphlAJ_tP3j6zNRpnkFkjvxn5vkXU22ciRp6kREevi4mFI3KXPQVRb4IhTheB1yPr3pB7tFeSg8X8KH7u0PkOhNQSOV1R6XiQbohraFCN0qFTCJ1PCqwMbV0-vaTTtlZX0UVcA5x_ohgkt_ey23ClwMSK4e6yz3dnqvb6KCVK0ggP7jFlZI1L9YDmd4Uvu-zxOxlZtD6LL8dkJaD2cYGNymA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27dd0a5169.mp4?token=p-IQsDr-xTHXPhp7W0lBL0Bg2WFGZGJn1gIOpA5Z2o-KXkUNSJ5rk8MDHFzO-6N7GJr8R16uiJuzRTAIT1Gt3E51AGMZXSmbirfPpMhzjxO1iKYuKEizQhOfajr4DDwphlAJ_tP3j6zNRpnkFkjvxn5vkXU22ciRp6kREevi4mFI3KXPQVRb4IhTheB1yPr3pB7tFeSg8X8KH7u0PkOhNQSOV1R6XiQbohraFCN0qFTCJ1PCqwMbV0-vaTTtlZX0UVcA5x_ohgkt_ey23ClwMSK4e6yz3dnqvb6KCVK0ggP7jFlZI1L9YDmd4Uvu-zxOxlZtD6LL8dkJaD2cYGNymA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🩵
آپدیت جدید تلگرام دیشب اومد؛
چند تا قابلیت جدید بااستفاده‌از هوش‌مصنوعی اومده. چندتا عکس رو میتونید مثل اینستگرام پست کنید تو یک پست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26126" target="_blank">📅 10:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26125">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6a101f8f4.mp4?token=GjTJcA6zxeu8lTO2XQvPJ4Y-bmtlwx2YSmOwEAZDCSO8mLMxVyLTWG_bkA3EtOrNvieueGukompPjGY_NjyjactL3J-YMj-Vg8loNc-MZDe7FerwtfdFonR9faTy_yqwkslZvTtbai7T8iSk52TPOTSiuXG8X9PaO4goJzNTPs93_OdMSfh317foVHjMTDxidZPjtC368xeJiy83cZrfPkw60ZRpsQF1I4NIX5qQ88-TrNcUitt83LeWsYX21ljrzDZUJwCpREKv1lzT-U4USr-jPkGcda_n8dM9lnTzjH8-5T5JF20w-xA4K_gGJa7gmIO_xdInRHihsgGmVSVW0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6a101f8f4.mp4?token=GjTJcA6zxeu8lTO2XQvPJ4Y-bmtlwx2YSmOwEAZDCSO8mLMxVyLTWG_bkA3EtOrNvieueGukompPjGY_NjyjactL3J-YMj-Vg8loNc-MZDe7FerwtfdFonR9faTy_yqwkslZvTtbai7T8iSk52TPOTSiuXG8X9PaO4goJzNTPs93_OdMSfh317foVHjMTDxidZPjtC368xeJiy83cZrfPkw60ZRpsQF1I4NIX5qQ88-TrNcUitt83LeWsYX21ljrzDZUJwCpREKv1lzT-U4USr-jPkGcda_n8dM9lnTzjH8-5T5JF20w-xA4K_gGJa7gmIO_xdInRHihsgGmVSVW0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
گاوی در جشن قهرمانی خواست لئونور دختر پادشاه اسپانیا روبغل‌کنه‌که لئونور پسش زد و نذاشت بهش نزدیک بشه تا به‌نوعی انتقام گرفته باشه. لئونور در عوضش با پدری برخورد خیلی گرمی داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26125" target="_blank">📅 10:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26124">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1235d344e.mp4?token=kGgMh73j1LPpaumEbjaCL3TLW1lQ1b3gd4J0pB08E_9snV-IX3072QSi_LfOX_ngxZ7X-08qrhCuLzTyPGc5qJf8o7TjK3Wm0K8qHjwpH4gmGORcDGvIiOcJNHoyfXsqcUgy8oEEaZXgpu1Djk-EA_TNq0N2D4yhyeKiPbp4bZL0IU0GLs8k8_qPO6m5P6suHSWOqhxwncWfeeQx8eySSFIhSNEKApnUS2mahGTXyQtAtO8qJISCU4vZmoTNNXs45GodUXtUuRWAFsg0C44kGIexzyyLGRKcCZDGUmIKvzByLz2ximXXVcz4jZ647GghOqmLUnUDrwZxmLtTXidZNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1235d344e.mp4?token=kGgMh73j1LPpaumEbjaCL3TLW1lQ1b3gd4J0pB08E_9snV-IX3072QSi_LfOX_ngxZ7X-08qrhCuLzTyPGc5qJf8o7TjK3Wm0K8qHjwpH4gmGORcDGvIiOcJNHoyfXsqcUgy8oEEaZXgpu1Djk-EA_TNq0N2D4yhyeKiPbp4bZL0IU0GLs8k8_qPO6m5P6suHSWOqhxwncWfeeQx8eySSFIhSNEKApnUS2mahGTXyQtAtO8qJISCU4vZmoTNNXs45GodUXtUuRWAFsg0C44kGIexzyyLGRKcCZDGUmIKvzByLz2ximXXVcz4jZ647GghOqmLUnUDrwZxmLtTXidZNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دونالد ترامپ‌موقعی‌که‌کاپ‌رومیخواستن ببرن بالا ازپیش بازیکن‌هانمیرفت‌ بره‌ کنار؛ رئیسفیفا اینفانتینو دست ترامپ رو گرفت جدا شه از بازیکن‌ها، جدا نشد وایستاد تاکاپ ببرن بالا؛ فِش فِشه ها اتیش بازی بالای استادیوم چرا آبی بود. قرمزنبود! ازقبل بازی چرا آبی تدارک دیدن!؟ فکر میکردن تیم ملی آرژانتین میبره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26124" target="_blank">📅 10:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26122">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kU423t6vDwkz6e5lM2jOmftAayBnjhuFjyrMvOoFf36OcZ6FvZ9g57r11uldvRc3eZwhjvxiN2rJ5kZMKxpWEsexf5p4eTlNAZbb5t0rr9LYVNLGrBLJGZimTpcAK6eLB8uT9v4gskatdBNYEw0Q91HnoSCCJ0ZFqaM2L0EYZIhuE8Sz4u92ZR9rXatn4YfWBwFWkxn1NtH5pxQTIfgmzTfI5F8lCMpEhrH1HeDztz1gIKMFfv7PgTXW2qOrGuIHNc9feqRdZnRRL7G2tt0aZ3Tn-h5RxWHHJSWlkbrWIVZ7Tc6MOSo5fDI9PLaG21zMYHrqtEEnXlammb3XUHVvdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EVv-_PWCPQP_MMWK8hPUAQt36PJGbXA5xlN_EVjTCgluciSQLlUWLLutkkrbkVJuH7r2oaFGu5ds-Bm9U22qKiQwCsSvmk1Mqdhx91jC4AYjgcWZPo148ivYg3LAWvE2rSkaa-YVX6iUT-LYRzOgQkoF8PQNHbaNuV8U4P37MQKAWdjfiv9pCOVo3bkanw_c9eNdZ9kg7CPjTJjHUCBGdC7nM0ryRQQ3c2S9WnWz1rhojsZgGXefu51HrIJFdUvtQcfre6rwEMJFg47SenI4sjI7rq4w95tWjal4NVZK0pxxkyzHyeq-O6hT22ibSLwq-Y217u98BF9qGwSSxQPcJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
گاوی در جشن قهرمانی خواست لئونور دختر پادشاه اسپانیا روبغل‌کنه‌که لئونور پسش زد و نذاشت بهش نزدیک بشه تا به‌نوعی انتقام گرفته باشه. لئونور در عوضش با پدری برخورد خیلی گرمی داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26122" target="_blank">📅 10:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26121">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c071bd0be.mp4?token=A6FR0Dk2E51J4Pmpsljm_FwqG5rDvwAwUsSBmHnQK_5w1yQH6tDBVne0aUjYYt1_Ee6yeUO0Gmh2OJphllgdaMzYCEwQpyW7sD3bjbQuxg9snAXaqU1MPtzyjCu44v99M0F73Go-KtB37uSzghc5Ea_FIuZ_aVvqFpLniDBx1Xz2b7xsPjrX9Zrqh6CeYSdw-QH9ZXDf307ew6vmmvXzqNLiwFUqIOIJMueFTKwmgkv35EMBKdoxNmiZs-P1Jrm2ioiM5pVAGkqS0kYTzU-Dqa8MBeZSuiIm_3b0wsfQRNEEuXWu6_uNtu5biOsCPiA6yyS7h4i__mhByfz612XYdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c071bd0be.mp4?token=A6FR0Dk2E51J4Pmpsljm_FwqG5rDvwAwUsSBmHnQK_5w1yQH6tDBVne0aUjYYt1_Ee6yeUO0Gmh2OJphllgdaMzYCEwQpyW7sD3bjbQuxg9snAXaqU1MPtzyjCu44v99M0F73Go-KtB37uSzghc5Ea_FIuZ_aVvqFpLniDBx1Xz2b7xsPjrX9Zrqh6CeYSdw-QH9ZXDf307ew6vmmvXzqNLiwFUqIOIJMueFTKwmgkv35EMBKdoxNmiZs-P1Jrm2ioiM5pVAGkqS0kYTzU-Dqa8MBeZSuiIm_3b0wsfQRNEEuXWu6_uNtu5biOsCPiA6yyS7h4i__mhByfz612XYdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حماسه‌جدید خیابانی دربرنامه زنده؛ خداحافظی اوس جواد با مسی و میراث مارادونا با شعر مدونا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26121" target="_blank">📅 10:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26120">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec0657aa93.mp4?token=rjc3XxPK6xxwr7yniQDovYgtFeYi7QSE6t2Y5p3lDw5nJ_oKAQwiv1aSid5XHmdyjf08NvWU1ylycwZZyrl1vGay9xnK9C9lPeZf3k5yXxtH4q0JcNe5PugyqOAjTSsBj9_HGDhx-dZu7bg0Bqgd4ygs8G0t9GIT2AA-SpPxA7hIMLknaoDMf0DSBnUnyyFMlavWZnEPdV2U54dioCMb6UeAgSSV4LXImIMiGr9LA3gXFVCgXlTxCW_3FHnEt3Z8iIe75hsMnPU7wbR4K8082bSlK2QNQt_oGFAbhUUM-h9GvmqAYqAltapgdVtsnTOWeIqiDUhW7aMCxDyOt7U5XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec0657aa93.mp4?token=rjc3XxPK6xxwr7yniQDovYgtFeYi7QSE6t2Y5p3lDw5nJ_oKAQwiv1aSid5XHmdyjf08NvWU1ylycwZZyrl1vGay9xnK9C9lPeZf3k5yXxtH4q0JcNe5PugyqOAjTSsBj9_HGDhx-dZu7bg0Bqgd4ygs8G0t9GIT2AA-SpPxA7hIMLknaoDMf0DSBnUnyyFMlavWZnEPdV2U54dioCMb6UeAgSSV4LXImIMiGr9LA3gXFVCgXlTxCW_3FHnEt3Z8iIe75hsMnPU7wbR4K8082bSlK2QNQt_oGFAbhUUM-h9GvmqAYqAltapgdVtsnTOWeIqiDUhW7aMCxDyOt7U5XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
#تکمیلی؛ اینجا دیگه عادل آن‌فایر میشه و خطاب به قلعه نویی میگه من تو جنگ‌های این یک سال اخیر ازتهران‌تکون‌نخوردم ولی‌تویی‌که خودت هرسری فرار میکردی تو ویلات‌نیا ازاین‌حرفای‌عجیب‌وغریب بزن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/26120" target="_blank">📅 03:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26119">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aa1c44954.mp4?token=XSwqBTtltTyH3dJQJghWF8D0Y7CMTH964mfQypdgzoAmjstkvYqslXZ7ZdGemP6IEhfXQbVpHZ_y-3ZJAuIclbg33EusLgetJd0CkuSSvFShIxql4BMHVgzotDPiECsddWeT2CZr6MDUkuY3TPFyj83qE2Ex5OqNuTLJoGckfx8M92SVd5G2evVaEvRNRFBIG7fJIinqKakc_eTv66QqTMPvHPHJQu6u7O2d8hRrP10Q65hvtwlEfgVUmuAX-DZotul2NswXQrPkQdyYRa9YX0uMWRmU8xAqI4IFyl6ZYoPtFyMd2e28Ex-rle8YAzZOYeAOtgQc7sfBBsRTGKepxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aa1c44954.mp4?token=XSwqBTtltTyH3dJQJghWF8D0Y7CMTH964mfQypdgzoAmjstkvYqslXZ7ZdGemP6IEhfXQbVpHZ_y-3ZJAuIclbg33EusLgetJd0CkuSSvFShIxql4BMHVgzotDPiECsddWeT2CZr6MDUkuY3TPFyj83qE2Ex5OqNuTLJoGckfx8M92SVd5G2evVaEvRNRFBIG7fJIinqKakc_eTv66QqTMPvHPHJQu6u7O2d8hRrP10Q65hvtwlEfgVUmuAX-DZotul2NswXQrPkQdyYRa9YX0uMWRmU8xAqI4IFyl6ZYoPtFyMd2e28Ex-rle8YAzZOYeAOtgQc7sfBBsRTGKepxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
جملات‌زیبای عادل‌فردوسی‌پور برای لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌دنیا در پایان جام‌جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26119" target="_blank">📅 03:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26118">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55d171bce1.mp4?token=ntSyQ5aKH8Ddd_1562D0F5c5jc6xWbkKonI5UpL8z939BiFaL2o6mAF6UKoBoFbrGp7yxG5g04t5mWiNUkK9NBfPCtlz4L4hy_8CRTOwMiBzWhG9w4-ZaGggcYCfJdZ8-uJGqZQ0t7fmcsV14ifzzx8730D0A0axb4tKG54OUOf8EN2Vi8AB9orsarx86JE73E_VYC3_6Vorb9FmAZ22HNN1atcqXGL0YPqQBx12w9DZgZSYI4Jp3QdHxe3mVg7dj55EP7etuLbii8KAbzVqwwfXFobrP8m6Euwd41hb4lQyYYx9de4SKS5mH4z6ywtL2B2DM-_11bXLlB7TBdqq8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55d171bce1.mp4?token=ntSyQ5aKH8Ddd_1562D0F5c5jc6xWbkKonI5UpL8z939BiFaL2o6mAF6UKoBoFbrGp7yxG5g04t5mWiNUkK9NBfPCtlz4L4hy_8CRTOwMiBzWhG9w4-ZaGggcYCfJdZ8-uJGqZQ0t7fmcsV14ifzzx8730D0A0axb4tKG54OUOf8EN2Vi8AB9orsarx86JE73E_VYC3_6Vorb9FmAZ22HNN1atcqXGL0YPqQBx12w9DZgZSYI4Jp3QdHxe3mVg7dj55EP7etuLbii8KAbzVqwwfXFobrP8m6Euwd41hb4lQyYYx9de4SKS5mH4z6ywtL2B2DM-_11bXLlB7TBdqq8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
این هم برای هواداران لیونل‌مسی؛ مسیِ ۳۹ساله اگر نبود آرژانتین‌حتی‌از گروهشم صعود نمیکرد اما او یک‌تنه تیمش رو تافینال‌جهان برد و تهش به هم‌تیمیای خودش باخت. توخودت‌رو قبلا بارها ثابت کرده بودی لئو ممنونیم ازت که حتی در آخرین نمایشت هم درخشان بودی و مثل همیشه…</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26118" target="_blank">📅 02:52 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
