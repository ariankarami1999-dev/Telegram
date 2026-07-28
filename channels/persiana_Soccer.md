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
<img src="https://cdn4.telesco.pe/file/jCc3YSp78ZdyqfgEwgwUqx3oysH0qgR4aqjTXuxjv9rC_VvuMzlbkvWOG964vD6lBWkWZ_fEoADPwcj9ke883BDTfjYYHVT9VQWGWUyF6wYfRJ9M9BIHkwVyEkkUCH3O-_4UWsfmgB8_N8132nxEw0llXMc-8fBmvt_NMYcSLUL8rA_1x1UnZC2NLZETScQJ_gC4G9bdLdwW7nB4BR4za8uWd9TSYGCvDGBeTcrW7iCGvdaA4pkdJYQRnPjaY4n66_acKQO69OWRaT5M-MlMJRGL7nbOgoSYU4feJ9lK_3mrMDpIS2EAWCGKOy0Pj1QooCk-aYb5WKHtRnH_FdMMDQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 610K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 16:18:26</div>
<hr>

<div class="tg-post" id="msg-26689">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ccc06fbcc.mp4?token=r8IbanOygJJkEVJ0KHmIjeGV3hI1eJC8BPnpbpSsYO6PYbmteBz96sMkN_HgGoTHHL8m6DMhyCWNQxv2iClkHf1jz4vtoARIBoY6xfZ_i91yT0O_Mo_RNV0EtAVBLIIVtIQJCXQ5tRrUsuCE3KIeEAeHv31iAoAjqHNgvtU7xp8EjUBlrrWs4MzcSfxwqkHH2zR4p9IXMtDG7-CGo_3Mb2oSllbyprCqYtxZ9xHFphBCgKVaciEbJHQEFUhAPrBMDf2LyIroK1-59M6ekuMlXoJdpf-OdhOGJErHBS2w6T7LW6BSu3SZxB7djo7lGedMH06a56V5sUgQGfZyQJuDBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ccc06fbcc.mp4?token=r8IbanOygJJkEVJ0KHmIjeGV3hI1eJC8BPnpbpSsYO6PYbmteBz96sMkN_HgGoTHHL8m6DMhyCWNQxv2iClkHf1jz4vtoARIBoY6xfZ_i91yT0O_Mo_RNV0EtAVBLIIVtIQJCXQ5tRrUsuCE3KIeEAeHv31iAoAjqHNgvtU7xp8EjUBlrrWs4MzcSfxwqkHH2zR4p9IXMtDG7-CGo_3Mb2oSllbyprCqYtxZ9xHFphBCgKVaciEbJHQEFUhAPrBMDf2LyIroK1-59M6ekuMlXoJdpf-OdhOGJErHBS2w6T7LW6BSu3SZxB7djo7lGedMH06a56V5sUgQGfZyQJuDBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
هر اثری هنری دیدنی یک کپی بی ارزش داره؛ در نقاط سخت زندگی فردی به دادت خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/persiana_Soccer/26689" target="_blank">📅 16:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26688">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YW-QpSOMkBtsuYc0qeOlLH72-tfv9qfb1ezWpFmS8JjvmSsm-EU8dUwknxWUA3RXimabdwYO2XDlxBuR-sz2YesnCL6A887k1h6G2FQeFE1SN_nxYXuKSRa07eMoirksBbp8DLBS2rbccnjdickJA0Mbx0IYvJzGnHwKRMhi-6hv9Pwu7vbW0ibd-nM8a3bdaBsBCm_i4LFKUB5h9nKQiHS6c03IVQDFp7I03WCmOpsrWdXM8rk9u0JTC78ADP_UUUNAZ9KoC2-j3qxu0VvE83SgKreBTcVsXcz3qmrWMoWDzrlnti7LJXoQ7HEVRznPSodjUw9yF8pyyYwUCjnGDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
مارک‌کوکوریا مدافع‌تیم‌اسپانیا: اگه قهرمان جام‌ جهانی شویم و همسرم‌هم مشکلی نداشته باشه میخوام که عکس دلافوئنته رو روی قلبم تتو کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/26688" target="_blank">📅 16:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26687">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3fWqGRMGuV06tdwIHXzYzoH_-KMhDpgStENOjEkFgfMVwCquCVxL1NyO4fSKo-FXEJRprZCTdetHLpF00O_xzQF9EPM49lJ3b0NUc2Nmyhj19WzkdjQJAu48pDyiiY7X9wKNkRki_I27uFkiNXPzgisg8q_d52kzyqgOCyDr0h6Yxyb_Gb2PZrrigiFon3ShmU4vWfZdJqccFxW3nOi7YLvJdVV7RV2XjHcwrmCKrpS1GBo4YHCf4WSeB_f1emw8x6Gj0Zg7D9NvHR-k4qxVRgaS_XSpo3yvDFrzjDIvfp3G9ooISVvVLHD8v1Mf-OhV6tJRKWhaBBjvNo814p0Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ یوشکو گواردیول مدافع 24 ساله منچسترسیتی قراردادش‌روتاسال 2032 تمدید کرد. سیتیزن ها اعلام‌کرده‌‌اند که هر باشگاهی یوشکو رو میخواهد باید 80 میلیون یورو به ما پرداخت کنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/persiana_Soccer/26687" target="_blank">📅 15:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26686">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJMZpcLWgyFHxk4FB_kjFHi8_C3HGZ2MCtrux8jfen_S7hmjb05OHc3Vm14bBpG2AKG4val2pKqTGbTQgk3q96SiBKP9-zEfiGE40iQ9StF9HTdIpJsbydWrZ_t_FJlybO1WuBEBCMxaK-_OGLq-0a0bVewSnFVrRkGJkDRsGxJG3EV_X7wrmWob4HrZKS_o4RMYEXRr2F4m5nsk96Df-uqiQJImdblxwfQVZLlQQz-xlAF6REdH74yGmrVCWTaAsUDcMMmGdQnkirD5iRBOe-aogxQmIgyoEKC5E5tf5mrnpmcbZj0u7anq1biH_3QQd5n5pflaS-cEcd74nueL2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
#تکمیلی؛فیفا درروزهای‌اخیر رسما اعلام کرد که ازنظرحقوقی‌هیچ‌مشکلی‌برای پیوستن کسری طاهری از نساجی به تیم جدیدش نداره. هر باشگاهی پول رضایت نامه طاهری رو به نساجی پرداخت کنه باخیال راحت میتونه باهاش قرارداد امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/26686" target="_blank">📅 15:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26685">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYqaXIXvwEOXFYptnQHQQWKwEk7ip5sYroQGmG5A-qVTwns_uokgT_DtbIAtvtLsIUYuB1AC8mnuU7xBSZHl7f5oRliyOrb6_H_-ORj39XPpUk7DZWHhifOrIIyGjxhPurCN7IIPSFDgO3hjfY8Xbjbasbk08RFMfT7UwJ-C78SxOcaHfOCa47pkU7J_t_-YRaHDveZUg_47lc6VrtgB6mjyCY_sRQExzHyhfUA8gRqgjDgI-t17fl695-c8itgiFJCMgXokFsZ5jGIm4tXGFcEIUtkfUy8MBSSoGFZlHQOvKgzge1MDreQMMTOnq6JCZASEiOi1IX6ZEve95t7_uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرام‌جوینده همسر سپهر حیدری کاپیتان سابق پرسپولیس:
برای پیشرفت نیاز داشتم پارتنر بهتری پیدا کنم برای همین‌ازسپهر طلاق گرفت. دوس پسر جدیدم یکی‌ازخواننده‌های خوش صدا و خفن ایرانه که‌مردم خاطرات بسیار زیادی با آهنگ‌های او دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/26685" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26684">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXw5MtLHgvgsQPetDJObSyDcRvV1OLByA6JBfgHWx_PRTNVKJttmibtVToK0OjNXDVfxSZ6FM040LemutNd2blNQnkGhseVLxDCY0d2dLJSUza19cv53f0xsiy9IqhURGCfvbMepM0ZHznQS9HpNU12fWc-q-ALS3Oa-WOhpDzbjcIQ86OhfvOhwSq9vcVTL0QlJhtSbT_DfDaqVgugMBXCgRkuSv5FypW-7VeLvG3sfHvM2RqvjT4LU_L6GagORu6_jl_3T2k7387ElYzgw87pN0smV5t8yc82_-cJyQICw6m2SnaCMi8rKLmPUZ9vcqRg5EJCfWfygkmq5a7ornA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
خبرنگاروگزارشگر معروف ایتالیایی: فدراسیون فوتبال ایتالیا به زودی روبرتو مانچینی رو بعنوان سر مربی جدید آتزوری در یورو 2028 انتخاب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/26684" target="_blank">📅 14:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26683">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FnLD1k3LQDhoiQDI8E2jjRj2viqnyjLEZ6_Oc4vU0l01UTIOSHutNTJJd6nJgl1j8o7cWDHR1KSs-h9wFUTQS8-KNtlP23EtcmG5QWEt_QS5LFcUQegcTzTDJ_ZXwM4V2pHhqeSjDsBzRx2Kh1pbGagI_avKYKdoYAg5_r7Uy2ztZOlxvJ5KRd_hrG2P__h3ih40uAobEmvkG8qLx8j2YJQV5wO8MpjuYZxi6Z9Jxz0ZukxRIo1igvZMGMonLtXTA0qRkQ4FlcnioXKK4Bylb9rjZBD0BmMVSwIrzPcY-qfvEhW95M4qDve1CD1xvJmRWiBxS9ONYD2hByRVENP2Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ دقایقی قبل استعلام فیفا به دست مدیران باشگاه‌پرسپولیس رسید؛ فیفا رسما اعلام کرد که هیچ‌مشکلی‌برای‌عقدقرارداد کسری طاهری مهاجم جدید نساجی با باشگاه پرسپولیس وجود ندارد. حالا باشگاه با پرداخت زضایت نامه طاهری بزودی از او و دانیال ایری دیگر خرید خود…</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/26683" target="_blank">📅 14:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26682">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4AaVFtqXtydlyobnuiQKV-NN3p-Wg2EdZ-DI1Qk0lmiH7M6V2ARfh2zlBgUuszcYRjOYTIA_NnWv4MDN3aSTxlwqYSxhr_KXSbuwqL4X5ANnSeVSomODAOj7X1qBUihr3IqPIA95LngYWY4q-H3I4juOOqPV1EKJSYCfl5yCEAtSgmuLR4pQtnHumX6xBjmEROGBp2iBolFW8dzsZZxISRKChtv6sY1ZXikiTf7xNEyWEjr-foNQyYmy6c4K3FudNDhkcNZy2sI2GD6r8qCahepDOsOKXw-cYqw4aUTEw-hlo0DfjdS89NatLQml5vJ-qPYPY_jkfwGYhbHUPBEgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ ایجنت رضا غندی پور به مدیریت پرسپولیس گفته درصورتیکه درجذب این مهاجم 20 ساله شباب الاهلی مصمم باشند با 1.2 میلیون دلار حاضر است رضایت نامه رو از اماراتی‌ها بگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/26682" target="_blank">📅 14:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26681">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m2tYILvFmFo70hzR9P0MNyrj2E2LpYpbLNG2AjkWsWjYaj0IIVO5kVCPKi3jQCfCuXTvbDYgFJ8-k4YXbkEbN8Z8BOmOawsLYiq5X8kqyG6Lr-EYDdgxRePQCOY2knr8jUWRm_TdEJQ-7qYzY0JTYPo_bgIT_nH8WMP8l-mFNWrsmzcj7PrXEOCTz_ebeq61SqtsUe2Ij0Rcu75wv1Pop1P_KCENcGNREck4CTU5__PYl-AWQgMKk42mwN8k4t8e-W-yfPGJlmjR4vrPlG-nsEpedAPTOgJZ_lnYyliuKPcyNSvD3TwP8WFHvhhKpSJjSHk0FyQT4GBwbEixVj2ZFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
مدیریت باشگاه پرسپولیس تا امروز ساعت 14:00 فرصت‌دارندبرای‌پرداخت رضایت‌نامه دانیال ایری و کسری‌طاهری بامدیریت‌باشگاه نساجی تماس بگیرند و گرنه تموم توافقات روی هوا میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/26681" target="_blank">📅 14:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26680">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-jruXWwQac-cDhj01TRfsoiIlgfFRyL-MQRXAiPhYaSZ-Mj7RR0XNEMM6QLMxHFQaMneRjXcPrGuefXZZHLBiGhijx5J2gA-viYYACDcAO1GSpBqQ9Yn522wvi_-PTdbmrAWRJ2XP218ZcWPskA8UqnP2hP7nQZ4faxhVGT-PhPdTe0iMUIkKLD_-S1iFTO9XuRSfG6P1bPXzuRDshnJjZxbuS_v3GqT1GoCTumjU1U14t7Cev6L9yCUkzk-s-QBGyRuPh8E2K9MlIJT7Q0w46qNADnKz1fKBQdYthRj3hMkWpeOIsUpjLsXuvfI4XGnGBWy5qRgND-3pp1mqKvfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پوریا شهر آبادی، ابوالفضل جلالی و مهدی زارع سه‌خرید جدید پرسپولیس که سابق بازی در تیم‌های امید و بزرگسالان استقلال رو در کارنامه‌ داشته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/26680" target="_blank">📅 13:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26679">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gioTHkulBy2ba-rQ0koi4FZGYVRXh6WSOzneU40V36RAq_RJhWkYVUwG6ygUKByTpMFQfhSobaDTX2yD1DiM0rSrWqtDIqpdrkDpW2hBrCemm7erv1zyrxRD19eAPVWY_j_qEWdzGNQbuP2XAtqE5tY85ZIsiMgTotj2RpTVYpqZlKSYJgjFtdvcWSQiOh5dzBEC06zmMM5xZIq4htBfv8EaAJKRPfGb6qvg5to7ZKosFhegjYI9PjZRXBh702t6MMJsAxJ4mx1vmLWciOxM3yvqyd-mIremH6XwsEGP0MH3hR0-TQ5wORz0OlISSzBZKEyHbhH17NvJ48Dlv1ikTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/26679" target="_blank">📅 13:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26678">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_I0HK3_siwNlgg_UEAeL1uqOXcr0TecIV96vcx395cL-cjAcPbIPdghqg-I-2kjx3XSnxCmBpKt54sAVcnbil2prkHXD3klDBQVRS6XKcldLVxxWWKcxLtXXxoOleCp4Nvc_rMIVrmpMfbbxS7EUok2BT_QupAy70VuvMLyIQNUbHYOfMkL0tf4t7KFgKQydI2pHhHwiMF0M4GO6srAA9xoEm-aSn7wtPrdghYTgYc-N-hgvapo6bZol4gHpSjViPVoASwBaiKLZJHRcmEjm9P29OkgrWETwzcRMlJ68unhXifwv5oIvVR0Z-l_EtydPUA0IuSWcD_pqtwueHlbwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ محمدمهدی محبی تا ساعات آینده قرارداد رسمی‌خود را به‌مدت سه فصل با پرسپولیس امضا خواهد کرد. تمام‌توافقات بین محبی، اتحاد کلبا و پرسپولیس برای این انتقال نهایی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/26678" target="_blank">📅 13:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26677">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EfAtp2NwqpNorMP-c4SS7esh1sMyHrwpok8DH4sJZDPMS8VLgzULZjqkXY5qjiHNzW6fy3MKz9SmgsOF52HyFDpmgIVxH5cydUHqnXoxi0NTatiAkGBF0pLfGYL8PbGPsJuT2dfLS_40jRXSbPMsBy-sgiTR9wCTUOa5HDMSWR50QcZSg8Y2WqQY2d6eRZ_8ZrTtLH5B3ttnmVP70ijPoxOq0EDk_qTYWR7qKZcPKCLc9ypEM84vfW6FgtML7E2CBfkZso0M5gaZvC7xoTXXm5IrodFHxQJolPCnU0A9Uwt6soTAk4zZyLHxFxYcuJhOBAS-2clICzGkPTFJy4G6cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
اینستا یه آپدیت جدید داده؛ میتونین تو قسمت «یادبود» اینستا یک نفرو مشخص کنین که بتونه بعد مرگتون در پیجتون فعالیت کنه و توی بیوی پیجتون هم میزنه صفحه یادبود و یا کلا اکانتتون حذف بشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/26677" target="_blank">📅 13:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26676">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKnH2uvswPXzS_PNqzKe-u9Vmq4PSC_dGSxuC4JnincKNnIwoeYb3FXx90udiq60dfjwMkKEF98fbNQv4LUbsVL-bb--CRoTM0Fb8A9TPzoHbXEJOOw34FEB-NnT3MDXeFWGW7cDMwz4BbP8jpuWLqwI27vDuTCqBVIpwTvEbC5xhsqRnfqroqPyu1xD5NwzNUdSWWaJbqcgCu6dSlICQbGBlyYnRWPWb-d9B89TTVG6CpIu0TelhsVosQImLjtXfEbco9Zy3nRWpyHx2GhFJ-vyfW7zhHwFFmOdWsDUuQgaub_fPMKTYnWIJ8r-66iE_E5ZzadSrGiLEMTP8t-wyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
باشگاه‌بورسیادورتموند درطول‌سالای‌اخیر عثمان دمبله، جود بلینگهام، جیدون سانچو و ارلینگ هالند با ارقام پایین خریده و با رقم‌‌های نجومی به بارسا، رئال مادرید، منچستریونایتد و منچستر سیتی فروخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/26676" target="_blank">📅 13:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26675">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6BHKnm79gjEBfJ8ElbmL9c3CVsNuGgXIPTVkdX8zRg-ta5vFprBmN8mMTNw-XH0RELajr3Q-PuB2i3NS-aOOygbdZMRtey2a9c3sAaq-F6Lzuc5cNmxHRXJaT4n7gLSod2bzPsvqGq4ORUK07GVsl3r-ILMtKBcb49kN6X8VgrN5Bfi9Z6dQd00DI7QlGe2C3doSo2b4GpC_jSpgdwE8fvdeDQAUhkA_N9gig4AU8LiJiw7zEul6SUzU58EoJ75Tohb39ZiuuQNW7rIjAfe5PBKglFS0pz3QzfqrL8iZxwFvedcSzILQUTI6qcU-qjbiiFDv_gwPRgI4DNDe8VFGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو، توافق زیدان بافرانسه‌نهایی شد و این سرمربی جانشین دشان روی نیمکت فرانسه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/26675" target="_blank">📅 12:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26674">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIwTSOWrBNNjqbgmjE0Puzcp-fTcd1s93gwBqkGCeFsZG9FMWHmc4lI8QhI1z-5TjqI2LQOD_cGK9aKYk72NhwRZ_jrqIa6chUfbEjY5_HnFbOAASeIYvn0ZDlDhaSs5j1eRPmBvYyaslIQm9ZxfetXBINmboU6ssgx1CLhVd380q0S8fJfImk6bXmnzPkAXXcuDOW4MPAkxUpdOo-DUeg_VAEewKtPxsvAE-jZI9KzKCEYM6T4ImD671tD5jZYfG24urvJ0XjykAbYKNhkJyRWP_TbbsKll56RpSbUq80Te5TyGNeb72wHXCqga4F3VZaD7-Cl6Ju9bflO5QkFDPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
عجیـب‌ترین‌تولد ۵/۵/۵؛ یک‌اتفاق باورنکردنی!
‼️
صبح دیروز یک نوزاد دختر در تاریخی خاص، ۵/۵/۵، چشم‌به‌جهان‌گشود؛شگفتی‌ماجرا فقط تاریخ‌ تولدش‌نبود! مادرنوزادمتولد ۱۳۸۸ و مادر بزرگش که برای مراقبت‌از دختر و نوه‌اش در بیمارستان حضور داشت، متولد ۱۳۷۰ و فقط و فقط…</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/26674" target="_blank">📅 12:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26673">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cq35Sgnu8-uBWFRQg21Oo8QtnYwsVKZOXztQuRNBY5zloy8qGkZWkByWtp0y_02GZHr23usw0ltP6vyOkJbvL5PoT98pxGM70v2EKLkGBqD3_kLzZN5p3v0aPSFSZ1kbqteokVzYbWlFAa_FP4RTenPrDHA6o-bwjgwFMZERiAyr6JWTKF_6a9PT3H-QdhV_V0it8FUy3ZmKA50zEPMmXALhgX24KKAs9-3sln6xzt81t-5Nu2VW7EhmC6y8ydTV55XbqdUQde-Mj22dskd7lJue0P4aBZ0mH0fPGfFthB4YcC3SAo2teW4Tf9-hYUp4Jkop7yECjnJ0DQkbem-ZDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
«گونزالوتورس»پارتنرسابق«اینس گارسیا» یه استوری گذاشته و خطاب به لامین یامال گفته: او عاشقت نیست؛ فقط میخواهد از تو باردار شود و با گرفتن نفقه یا حمایت مالیِ فرزند، تو را گیر بیندازد. امیدوارم قبل از اینکه دیر شود، خودت متوجه این موضوع بشوی. گارسیا فقط بخاطر…</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/26673" target="_blank">📅 11:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26672">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OH2la9Fewv550c2XredFBbeEOExIdL8o-tNu_nqO3FuuUg0ZmbGfIxBO_m1k4MSbhnotbB-Dbvdoj4W0FEznPLwsTIKOoDer7iRMSoUpTQaqyu0wXKAkCM6jjxczG3hVaKgCapIfPdw9Eb3737ZNH9aVPpvCC7uf1cdBUG9-x7DIFtHhRDMjeF2j07F9YqgmsBINZmgoJmrqByPf6ZHfRnMSlo0H1u7frn-d7pswspCfUY3qFw0ch6WD1qsW5-x5BaZ34cxEzbV35OFGypqVzjA9Cd3OlRgzYzH2CNwSl3uuIyFZtzZSc0TYprfsfO_qDy1hYPrSHJroMkCWuvj9eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ اکثر رسانه‌ های یونانی از جدایی قریب‌الوقع مهدی طارمی از المپیاکوس خبر میدهند. این‌تیم‌چهار مهاجم داره که گویا سرمربی این باشگاه تصمیم گرفته طارمی رو در لیست مازاد قرار بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/26672" target="_blank">📅 11:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26671">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7fa18a77b.mp4?token=QmJBVvw91SrfGJrx3dW9rDtF0HppUm5LeLy7lvmdFRpmAWx-trHEyIkdpABRN8YNTKFweX3JncPdgkEA8lkCfbG90SqvSPyqCFkidymwK1OOM-Jg19BqY21PJ0pgdHv6u_uzwcm0QUWuyFksWBObtG26Nd-6ZEIy8xhgmgFi3gwTa0IwEROPjec-Bxkq7uFN325KSqnX-QMOV2G6dk62bKCMBjqW2vrqfrpo10fpaOuj4YmVgMgRetpjn5bzWDFn-glSZZnP5LlFGgdWTkHQtirqepoQBgdyssJA4MumHAKzZIrcfu4b9lAHR4oiXU9HhnQN4pxSwt6NpBk4tiHvZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7fa18a77b.mp4?token=QmJBVvw91SrfGJrx3dW9rDtF0HppUm5LeLy7lvmdFRpmAWx-trHEyIkdpABRN8YNTKFweX3JncPdgkEA8lkCfbG90SqvSPyqCFkidymwK1OOM-Jg19BqY21PJ0pgdHv6u_uzwcm0QUWuyFksWBObtG26Nd-6ZEIy8xhgmgFi3gwTa0IwEROPjec-Bxkq7uFN325KSqnX-QMOV2G6dk62bKCMBjqW2vrqfrpo10fpaOuj4YmVgMgRetpjn5bzWDFn-glSZZnP5LlFGgdWTkHQtirqepoQBgdyssJA4MumHAKzZIrcfu4b9lAHR4oiXU9HhnQN4pxSwt6NpBk4tiHvZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
🇦🇷
پائولو دیبالا ستاره آرژانتینی آاس رم قرارداد خود را به مدت دو فصل با این باشگاه تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/26671" target="_blank">📅 11:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26670">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">چرا
3️⃣
2️⃣
1️⃣
انتخاب درستی برای بت هست؟
🔢
امنیت و اعتبار بالا
→ چون ایرانی نیست، مثل خیلی از سایت‌های داخلی آینده مبهمی نداره.
🔢
سقف برداشت
→ در ریتزوبت سقف برداشت معنی نداره و شما میتونید بدون محدودیت شرطبندی کنید .
🔢
بونوس‌های فوق‌العاده
→ اولین شارژت 100% بونوس داره، و یکشنبه‌ها هم هر مقدار شارژ کنی همونقدر جایزه می‌گیری!
🔢
فعالیت بین‌المللی
→ در کشورهای بزرگی مثل برزیل
🇧🇷
، هند
🇮🇳
ترکیه
🇹🇷
و بنگلادش
🇧🇩
فعال هست.
🔢
اپلیکیشن اختصاصی
→ با اپ اندروید سریع ‌تر شرط‌بندی کن بدون نیاز به فیلترشکن .
➖
➖
➖
➖
➖
➖
➖
➖
🚀
لینک و اپ رو همینجا براتون می‌ذارم . برای
جام جهانی
هوشمندانه انتخاب کنید
✅
⚡️
اپلیکیشن اندروید ریتزوبت
👇
🌐
RitzoBet App
⚡️
لینک سایت معتبر ریتزوبت
👇
🌐
RitzoBetLink</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/26670" target="_blank">📅 11:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26669">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vp3IsqscX0dTtbyHSEXZDVEE4nZ42AKFso1H57mssfRbdOmZPZEE0ITYqicVCTZ3SixM6MST9Dxs1l0VxcuDOehOErdWVYwvSxv_pNZ2FrIzxGLFXONyBRHFITV7OsVtsrtJGiMozTYWrsngfjgWaBnmSrjm5XFSkZriRRrWIV3-l55mAa-v3ZViJ0LTU7-6NyggFfQb_7QiXPy3ISSTVtwBoXMhWiHzcV9PjdXq0v_apkCYDalyQqQ96ZdCnO9TYA61swZh6UeB8M4e_rVKt9O1fwtSMUitjRMh1yaA2idJGLFdGlNrc7axwJXOGTZP3-0b3AnHQKY0yrlEpPhzeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وندا اکس مائورو ایکاردی: علت‌جدایی ما این بود که ایکاردی با شغل من مشکل داشت و شکاک بود که باعث میشد هرشب که برمیگشتم باهم دعوا کنیم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/26669" target="_blank">📅 11:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26668">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4SczvTLZnQPB--UaMZFUaAuferm5AYK2OkQRDBumtSdPGkOfCrV6duR8U0fKE4f9_qKOFbhrt2umNGtw1ZUZ87jpmyLzjkkpSEkciHdT4AeG6SYP9D2MpHq84LpPWZOJJUjqZToyQY8g-MzpXaGc2XYURm2RV1_AwMWbBK-ckF1sAOImVj-JBT_3YC10bH0BqUxcEUs3_sdSXgqOL62Wm0KohkMunxFFhX5GLyVWlv8IniBQkLHZ2ZI-J0A6lbYmkuK8AdcqXQOMMY5O2_YnXa21atjrkxIWYXBehgjCfQT0lt8dqXUwvLP72HINb6aD342txNSFjNUDcF1iA6T6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
کریس رونالدو قراره وارد دنیای سریال‌ها بشه!
طبق‌گزارش‌ها رونالدو توی‌سریال‌فوتبالی Day 1s که با همکاری متیو وان، کارگردان فیلم‌های Kingsman ساخته میشه حضور داره. جالب‌تر اینکه رونالدو فقط بازیگر این‌پروژه نیست؛ خودش یکی از تهیه‌کننده‌های سریال هم هست و در کنار دیمین لوئیس، تیری آنری و رپر معروف Dave ایفای نقش می‌کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/26668" target="_blank">📅 11:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26667">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1z5Sz391KUDJ--Opal7FfC_6HUB5enBYnzmVi-_o6GAbnuO7-_3x0ZErdDco00SaWf1861lDG0vr-QzbT9h3GKXFyMSzHPRCiD-xenip88L0lH5rBvwihUoIRvpY3PGOFr3sqJPsxx5jNgUWvVMRxHvDAIt-ckdsqtkHvVprorcEg5ZbEQdUux65HTUroZBlDlDdm-RsZLnEPJeRHfHRTHMwNRU4xny_MD9plI7QGUKYpZf16Ryti2ARPFG0jVA2sw0Lneafn8TAzc16WSH4zi3Q0WErewItJNK52OKBf2hxCquJU6t5zVu5QuojiYQ9cz7wvcK5DWt63uelXAXqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
مدیریت باشگاه پرسپولیس تا امروز ساعت 14:00 فرصت‌دارندبرای‌پرداخت رضایت‌نامه دانیال ایری و کسری‌طاهری بامدیریت‌باشگاه نساجی تماس بگیرند و گرنه تموم توافقات روی هوا میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/26667" target="_blank">📅 11:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26666">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKmKYSihFxcb5BcRdtx6UwtoLWV2FczP5P9iuHA-erVAbtK5_MDlSUlcjCjLvSLMrY6wTGQlQqxy2ZPzfi5_eH8ULmwA8Higwa1GTekGBhix80AVCrYU4VZG8IoIIIF1FHtjPGf2UIIgZ1QFj6ilYXylHhWoH7inLeRpPJPiZ1pUR9Gm8brCmcWIO5aDDTJhjL6Pn1R8meFpDDE7trWWGBACM6Nik--Hr7UkHGNHXEScBEDeTyIhAxion5W4Q2Km1lpFPhC33HaHu3r6KnMXqf_w3BEjlGBjHxFtIWpFtSEDqafup5nDDE_E3I2rlFms7fb56ycMz5kY9bQupNQl2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرصت 24 ساعته نساجی به پرسپولیس! اگرپول ندهید دو بازیکن راهی استقلال میشوند!
‼️
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال امروز ساعت 11:00 باشهاب زندی مدیرعامل باشگاه نساجی تماس میگیره و به او اعلام میکنه که حاضره رقم رضایت نامه کسری طاهری و دانیال ایری…</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/26666" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26665">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWouwpLlvUekbUK4KDUPuZ6-YdX0WylQV288me3TktQW_8GHy5K_S_Bzo1HSyTghcYtYqRba-0bSfv1UVEHPrU2OirjqlQTroueqpmoKDomJnEep3Y-U7YKxhEEvt0QugR1-ycIdwdCeESwc-PwwZjRNxDk_KKpTHKuqxY9TdJ_wyYsU0wvoOFS7wXpYeuzX3vPLF8BJEXcX-kzEISCnIoyUqYQ4WPIrUKnDhFxswGKIjzkqDouxBhysdjV664_dsvgvj3ycXQyOyQxkIMS7R20_s-IqsvOtSga7uQIDHRVq-gc9tFO99sMyEkmY3vas4dcKKH7Z_oEyPmS1FfQd7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
#تکمیلی؛ محمد محبی هنوزآفر ارسالی باشگاه پرسپولیس روامضا نکرده و مدیریت باشگاه پرسپولیس نیز همچنان منتطر امضا قرارداد توسط ستاره سابق باشگاه سپاهانه. هرلحظه که امضا بشه سریعا توکانال پوشش میدیم. توافقات نهایی انجام شده و فقط امضای خودِ محبی باقی مونده…</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/26665" target="_blank">📅 10:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26664">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHbJGP557MJn6kXmshVxbkwpuA--j2UkdKrvtyE30uQxZG_VW71mElKGgQdjlUbZXPVzMUJ2Yj_J8daiAv6VssJCIoPSAJFRWQzsXl2-BJlBVHx4K2l2EgCTjFsgwpOXkK8D9qmqw37WZVIsDhEuCg1YEk4VizdmC_bgMTtDmFt-Nek0wXygf3tMbxDqYc8xmb7ho402WrfPgj2MXcL0Bw7Szyb-Jv6tjILYMXfCgMVENfj3qWdLqrpFJK1hQgtSumQOplKK2D7_aPzxt68cktxXLkNncogeCmYV9FyC7_aWIWy2IhTrfa_Tpol32boexYevOvanYtio1GJpLXFJNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام رومانو؛ پائولو مالدینی اسطوره دوست داستنی باشگاه آث‌میلان از مدیرفنی تیم ملی ایتالیا استعفا داد! گویا قراره از بین مانچینی و کونته یکی بیاد بشه سرمربی و مالدینی باهاشون مشکل داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/26664" target="_blank">📅 10:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26663">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b74f72d96e.mp4?token=m2B3rK7vPnaR7Z3Gq_TCZK0jeVSBYcRmxALBxJt8VbMjO1_eFkG99whsJkxoWEMkUobUogLgKFopA0PHoxzTffXfdop6eL86UXa_2TV9kbGNikVM8BC_A7zxnRXdnMpdxVE_uhJfU5-EIZnBLeLHdlGVADGfWMCTSS-xgcG0xXulXOyIPAp-xokIcGgx6ish8Zo5IAAuFifTOYwt2koflkBh_8X0upf8B59m1xWq3qdhlV-i0tkmFjDR-0ZIV3NfU553nN3tR-JoQrAtBjz3W444eJ407pxikyiTtapLgj7oHz2JGCA4We8bgPjTJX9Y8KI1md9abyLl1KdCyi6pT6p-uAq44q272NCW-imKHUy9WW9EN_Hxb17h6fLrFTofDCJ82ZJkHL8TXwL6w8v2zZvGBkiNvtdDHm5yH5_HLRP_DG1xWuWKnUor3hqn9oSlW1oIL_MVNbUO4SkfnA3_-msIESB8WHb9gY4UYebzsvIht3355znR5TkxW7lX34x2g4MxgWnnfJwxF84FLU2QdF12uThnTX6xTvO8amycsYo87l7-hisSaan5pic7Y6si0Ws0Fnd6HZVJeOMvcCu4s0qMMda69z8MiJlcsqPE4i853p_5jXYA57T9XsjiIqx_NQ-rhqn76xwPIyKQBre79wgQqAjVFaFECk5bOCjJFuU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b74f72d96e.mp4?token=m2B3rK7vPnaR7Z3Gq_TCZK0jeVSBYcRmxALBxJt8VbMjO1_eFkG99whsJkxoWEMkUobUogLgKFopA0PHoxzTffXfdop6eL86UXa_2TV9kbGNikVM8BC_A7zxnRXdnMpdxVE_uhJfU5-EIZnBLeLHdlGVADGfWMCTSS-xgcG0xXulXOyIPAp-xokIcGgx6ish8Zo5IAAuFifTOYwt2koflkBh_8X0upf8B59m1xWq3qdhlV-i0tkmFjDR-0ZIV3NfU553nN3tR-JoQrAtBjz3W444eJ407pxikyiTtapLgj7oHz2JGCA4We8bgPjTJX9Y8KI1md9abyLl1KdCyi6pT6p-uAq44q272NCW-imKHUy9WW9EN_Hxb17h6fLrFTofDCJ82ZJkHL8TXwL6w8v2zZvGBkiNvtdDHm5yH5_HLRP_DG1xWuWKnUor3hqn9oSlW1oIL_MVNbUO4SkfnA3_-msIESB8WHb9gY4UYebzsvIht3355znR5TkxW7lX34x2g4MxgWnnfJwxF84FLU2QdF12uThnTX6xTvO8amycsYo87l7-hisSaan5pic7Y6si0Ws0Fnd6HZVJeOMvcCu4s0qMMda69z8MiJlcsqPE4i853p_5jXYA57T9XsjiIqx_NQ-rhqn76xwPIyKQBre79wgQqAjVFaFECk5bOCjJFuU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی‌خاطره‌ای‌انگیز ازسوپرگل‌های لئو مسی از روی ضربات ایستگاهی در دوران حضور در بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/26663" target="_blank">📅 10:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26662">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6oOFR8yV_T_PQMM0kzLnGjOuwFK8opU9d_C0DBhEzeLnmDF8tQIkg01nOPTwYLT3AkIZ1YUQpvj1Qr6ErkW9dHa16REiDpHnYHp6bI24XTPvmTBwn3REYmHqUoBncuRO93Ojt2lBDe6YfRdHvdXafJwzNFGpDUFk3sizQZd1BhMIpEr2ErHkopmxpiMjKFeP59w45GQ8ckCuxL2WH8OaZAFsqJa9zZfIhTP6ysyXkeQ9MxozLR5c-JaLq0WnE_qVQsUS364BLEoz3l8QqechHYzjJpDTmSYLTztijhcMUvWIDxGVTCQYkRCeGQWVlwCr19Zn5Cg3lVYu_Do0H1cAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
یان دیومانده؛ از دزدی سیب‌زمینی تا تحقق وعده خواهر مرحوم و پیوستن به رئال مادرید.
❌
یان‌دیومانده‌وینگر ۱۹ ساله‌‌ساحل‌عاج پس از ثبت ۱۳گل و ۹پاس‌گل در ۳۶ بازی برای تیم لایپزیگ، راهی رئال مادرید شد. او در دوران کودکی شرایط سختی را پشت سر گذاشت و برای رفع…</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/26662" target="_blank">📅 09:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26661">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFlkVVJnyGJ9vn9F1yjZJGb8Hwh6Fwohh8jVFSojSA5dUuXaXGBPLwWhK1QMyHfRSkqvLM00-xD4LitFu6uR2qSTI03okONmpvD_riJ3U5EK7N1phkgN1z_N18a8aMrdq58pzHo0DWZLgSq1RCh5rrnNABfbakSrYoitVaKtBy7xV7LV0O4jFpFt-8iUQwviXGFAT1SWSUeTK6-Mo1bocNj_ahp3BnAPcx_ffs50QqRrDlN5E4cISj2UZam0ghd44JVzepgbFThwl5uLrSaRpDAvNOdoOmT3lFpCjGX9sR3LulY5wV3XkiSgl7m99WFKCdrlhrcTyVnOOgUm1pv2yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
صحبت‌های جالب مهدی ساداتی گزارشگر شبکه پرشیانا درباره زندگی قبلی دوس دختر لامین یامال. بزرگ‌ ترین خیانتی که یه پسر میتونه بخودش بکنه اینه با یه دختر متاهل و متعهد بره تو رابطه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/26661" target="_blank">📅 09:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26659">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jU7JaQYSl0SROiT9TA4yZMWG2Ijan1ASQF56DLY8OmQyo4FWOhEzwx6Qe0yx-Y3FMFbWGNeKxpMgSRuB45v9hjDIK57Jmk10hTmH7B-YyzgXzgNwne_ALvl0UjXMhE6SwzNL4zILiOrKU0P3vwl_SzM7JK8olvZB9t3ChUACyEYX9kcCrk4JaPkZU-RGyzOuV55-A1aeYYjm7EUK8ued16ABWYuQmncK_OaO878U6BPvmWYDur2UPXxFTbjCxeJ35ghZAm1q5P1SvEcCJ8xwomXhUjEZAtFBq2rioNE9h7OnlZlbPbOOXKidj2W54Xsi7HQAsDJ6FHyWvQxMj8n0wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/26659" target="_blank">📅 09:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26658">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8feaae9b61.mp4?token=rMKVxo1Y1bxJ_tQuqSURIDIyBtnhzjXpevcPbPhKskVJivMnRcEfETthwCMfxLcJArjyEXxui9OJp_f9gcjQb17D9qsTLuOc5MOXfvx_w3UJyNEYIoVZz8OxFfG3GJt-fPdzG6HliQmyJAnZXOkUiRbxwz_R2nHLNqx6Hr4DFRCetd38Tsofu0QaJUMfpnSfiIFtxOnZ-5IbMABbJLMJ-VjodhOpi2yYA80YNP9BX8mIBE-kfVwuDCZ_Ss7kNFvu0Ep92hO2bKJkWLZviXiHRhbnXnYgy5XmkHF0QQiLPBbMbHpCDbvl-TiPGEoKs1XdeIkqzvYXpHX-VqkNbSz8iBIfpDAXnISXRP_hu2T26X9fgqWUmNbt1QfnqX0vEYpGXwdEFXH-kL9AzGX6ca9TqpqLxJPpHc_Zqu8aKn2-ozMaVjQp4MA52t20x8xKOh3OgB23kfrljhku9UJZfODlo68b32ZpKKV7nRY7RY7w-z-WzczmhXKYqfmmPXFyr6ygEKeWEYVR8mLhR1woe9cUvRiUnad3mp_aFT5SqXS4uCVZjBOlhZw_dk43oFvVYnj5vEQIwAfc5HA-sNu3K6oyFUysTjGsdjwx7k1WC3tP1oJBC9xTnXqN23XG7g2IE-4OVb64DGfB4LZ9FO8HD4CstJIgCmwfAKqiqnAqpu8JaIo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8feaae9b61.mp4?token=rMKVxo1Y1bxJ_tQuqSURIDIyBtnhzjXpevcPbPhKskVJivMnRcEfETthwCMfxLcJArjyEXxui9OJp_f9gcjQb17D9qsTLuOc5MOXfvx_w3UJyNEYIoVZz8OxFfG3GJt-fPdzG6HliQmyJAnZXOkUiRbxwz_R2nHLNqx6Hr4DFRCetd38Tsofu0QaJUMfpnSfiIFtxOnZ-5IbMABbJLMJ-VjodhOpi2yYA80YNP9BX8mIBE-kfVwuDCZ_Ss7kNFvu0Ep92hO2bKJkWLZviXiHRhbnXnYgy5XmkHF0QQiLPBbMbHpCDbvl-TiPGEoKs1XdeIkqzvYXpHX-VqkNbSz8iBIfpDAXnISXRP_hu2T26X9fgqWUmNbt1QfnqX0vEYpGXwdEFXH-kL9AzGX6ca9TqpqLxJPpHc_Zqu8aKn2-ozMaVjQp4MA52t20x8xKOh3OgB23kfrljhku9UJZfODlo68b32ZpKKV7nRY7RY7w-z-WzczmhXKYqfmmPXFyr6ygEKeWEYVR8mLhR1woe9cUvRiUnad3mp_aFT5SqXS4uCVZjBOlhZw_dk43oFvVYnj5vEQIwAfc5HA-sNu3K6oyFUysTjGsdjwx7k1WC3tP1oJBC9xTnXqN23XG7g2IE-4OVb64DGfB4LZ9FO8HD4CstJIgCmwfAKqiqnAqpu8JaIo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
🇪🇸
دقیقا
20 سال پیش درچنین روزی؛
رود فن نیستلروی ستاره‌تیم‌ملی‌هلند با عقد قراردادی به رئال مادرید پیوست. این سوپرگل دیدنی او رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/26658" target="_blank">📅 09:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26657">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_-eZZC6Fjay1K7W0BZazKJaxTxA_qXJHAhrgcEGkGi_ComTXcJulw18dCh3MIjF_0_crAGSGjM6oyAY8vRzQfTclFdYKf79ZTHLRPNNyM-469otPn9FXPMfHvzk2TXCAPxqZTPp3oA11bGAIVw9Pzh4qNuq12pUpVkP1ojwMB7IgBfZ4X6LdLUBj7dBpxW4ZPs-ac-sm1GDLdacW7ShAXZ_Gb4Od2s3jklTfzD3hdhl1-syQ3jLLbuv9ByQv-T7lD8rqJg7xHMKPJUkEOXotjKJ6q6tlXnYGbCjXoQQvXAzQ2Sf-rTzQo1ZaTegD3GMyXrK8guGy5zFJvVeDPhGhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ مهم‌ ترین دیدار ها‌ی‌‌ امروز؛
بازی دوستانه شاگردان ژوزه مورینیو مقابل لگانس در مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/26657" target="_blank">📅 02:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26656">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnviYQdaSvh3p_dEhp0Lsf0SqlNKZQKOAYKqDjTbIiYn7RN82MgK1sJ9xhV4KpDqJW2xCw5qItiIrXwEkTd9aXBoPGVfXEkbY0i12KcG6puuwPowP-OO4iu7-bCbVHlxnQ-esE_5l_DcuHvQ8VTStFgSn4Kh2tk3rqr37l14LHybn-Z45ljQFgSgZZJ1ZGAbZvNb39Qq3mwR0SHY1Gy8Tej6XdFdtnV4g79ToA36VLEnn2ATSTUlEFdxtAka0mTm0p9DVDwg-BYVknSM0EuX60HRqVqmbGBBOW-Vx1lLwdH7kPmW3hGuvSVF_B1cokD9DafDLIHoCjJiRT72QgeCUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ میکل آرتتا سرمربی آرسنال تماس های خود رابا وینیسیوس جونیور آغازکرده و در تلاشه که اوپیشنهاد تمدید قرار داد رئال مادرید رو رد کنه و به جمع توپچی‌ها بپیونده. نیمار هم به وینیسیوس گفته جدایی از رئال مادرید یعنی نابود کل دوران کریرت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/26656" target="_blank">📅 01:44 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26655">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47adf0f058.mp4?token=vtLYzh0ZpADdg5EAfxzb0G6662ABs66BqLoEHAzUr5xdZx6bWvBz7PuOWo-_O5iIKHKRXwg7PRbHwTo7SOQp19giL8TkVYVEr-UiNbDuIOqI6aKaQAsmiYU8M_5FjLDuVRgH2w3OB7kihy3TsmqhpLoD08EmCD1Hi9eFBawPbvBtzQPx-HdWheUyjLE1pOA416xG1yckD5YXZqMZpvjOj0XQA_YVesz0nul-ykC0uJipGkpptfv1nLzyvcbjZZ4uvx-EFSysjAUuf5BviYIwkd0WIldPETAfNXWLLEnN_CSu2QSCtBS4_q7UbLYPDtQEGRCjG-GRTYdu8YtnHrsI4wyjKLF7Nh55Z_TSc3bsXRKTJd7M9l_0N2Bi2JmBCU04-aq15zlplz-ZM7vplBtSU-ofQjS6tT7XSgO85vV3CN5kb5igPqOyhSeqZ6PbsXRZhFAhdzlum-2m51UvnIAHbjaAcMlojUygM5gDojUUO_pEG3wmANhCPrQC1CDDV95F_M64EHQbbZ-V7yDNZWhk6-V076WzpVH5UchrJeVVk_Vw3-KAEgVUgxrfk7s1OAaQuh0-uOeWooEXQvwiYBRFcV5cZpEQZ042nKqZUO6NKCS3d3O9nc0nJw7vu_rdmOoL9TmAfXnisA-JL_bX45DLqfnmWL8PF_PRfaiAyVr6OZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47adf0f058.mp4?token=vtLYzh0ZpADdg5EAfxzb0G6662ABs66BqLoEHAzUr5xdZx6bWvBz7PuOWo-_O5iIKHKRXwg7PRbHwTo7SOQp19giL8TkVYVEr-UiNbDuIOqI6aKaQAsmiYU8M_5FjLDuVRgH2w3OB7kihy3TsmqhpLoD08EmCD1Hi9eFBawPbvBtzQPx-HdWheUyjLE1pOA416xG1yckD5YXZqMZpvjOj0XQA_YVesz0nul-ykC0uJipGkpptfv1nLzyvcbjZZ4uvx-EFSysjAUuf5BviYIwkd0WIldPETAfNXWLLEnN_CSu2QSCtBS4_q7UbLYPDtQEGRCjG-GRTYdu8YtnHrsI4wyjKLF7Nh55Z_TSc3bsXRKTJd7M9l_0N2Bi2JmBCU04-aq15zlplz-ZM7vplBtSU-ofQjS6tT7XSgO85vV3CN5kb5igPqOyhSeqZ6PbsXRZhFAhdzlum-2m51UvnIAHbjaAcMlojUygM5gDojUUO_pEG3wmANhCPrQC1CDDV95F_M64EHQbbZ-V7yDNZWhk6-V076WzpVH5UchrJeVVk_Vw3-KAEgVUgxrfk7s1OAaQuh0-uOeWooEXQvwiYBRFcV5cZpEQZ042nKqZUO6NKCS3d3O9nc0nJw7vu_rdmOoL9TmAfXnisA-JL_bX45DLqfnmWL8PF_PRfaiAyVr6OZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اوایل‌لیگ‌برتر
؛ یه‌باشگاه‌‌ایرانی‌یه‌بازیکن خارجی اورده بود "روزی صد تومن بهش میدادن میگفتن برو سر کوچه فلافل بخور… نوشابه هم نخور!"‌با نوشابه میشد ۱۵۰ صبح‌هم بهش یه بربری میدادن با چای! تو یه بازی گل زد یا تعویض شد، یهو فاک نشون داد بعد اوردنش نود که ماجرا چیه، اینارو تعریف کرد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26655" target="_blank">📅 01:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26654">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oPUfJCOvarP8yY_r2-F_fNNTt2kLofXDsEnC_17csyHk-f_BmyrQywSdOZsahLZgp5uItjwhRr0XwB1FYHtJzN1zV5kIlLmBzxKANlRRJtBtREQoy0kakd7Fc0ep3D3XB0FPiIyHCrdhz6xoANZRYY9eEjrea2j5XZbutFEGLuNj51XeAXR7se6cwOkkLENvyjrtMT63b1puKtsUbgu1EH_4YeUc9-FQpmBg8eUjHoDrBtSLZ3fFe_x2PW-QaKNmKuZY7kZ8xouOF3A3WwYTeVFLOcMVyGcbrYvbDfpJFvzKYns1AZI5hjr6gEmP1I_Jja7FJL7Lklc0s2_ZG_dJyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فلورین‌پلتنبرگ: رئال‌مادرید رسما آفرخود را برای تمدیدقرارداد به وینیسیوس جونیور داده. آرسنال هم بلافاصله اولین‌پیشنهادخود رابرای وینیسیوس و رئال مادرید فرستاده. حالا تصمیم نهایی به وینیسیوسه که کدوم باشگاه رو برای ادامه فوتبالش انتخاب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/26654" target="_blank">📅 01:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26653">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3lYiZ4K6d051HNLMMS6bc_dRWBa_W_devfrwO7cQrydZn6F1oh4jA9PMTniugIV7qZG-WbkpXlrEnKUROhIWKmzZolUhd46MzwX-FYR0UffMl2ww9Itpu_EwtUQPl8l79IV9c23JLIJ0u9X51CKhp4j_ONHGpAavj37BFEJ9oYFkbQtHCQZNCKHjQQPeEdNtAG4uKz4mcTCP-81OyLXllcrQBFY7zAPQptIVUwcuqhwF2KODR2W028gfn9xrfJFdo116PiYPkiGi38qQAQYfln7Od97EB9SaEPqoIWwE0v0nrzIEiTQ8rr2KXTz3tOMZ6cYIBPPx3vLK1WIpNgdJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
حضور کوین یامگا درتمرینات تیم مغرب الفارسی مراکش بدون استفاده از عینک؛ معجزه خدا تکمیل شد. بینایی او صدرصد برگشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/26653" target="_blank">📅 01:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26651">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCIVAxoeTRRCl6ybBc5SDr_Pwoz5qK58keffpq6KvmW6xyc7oD71sru-gpDLIIS-qodNFpdNZ5M444F6e11bA7oOTfIa8Sl8xnQSYEPksr51lCA22nlA97O8htYvpc3PkRUKjkb12e1lgjZXcTZuTwSKdA0tK_W1QI6DGKsnChrFR7LE8yLCs8orTwoq5quwbHA1t9zzk7DtbUU5fzwxgGo821KRa1yyy6TY1njuQ4VZwSoODuNx01T658pmtCHcQxvckjjIjIkTdEQoMVqITgyQXwrwWMBOm4Z8iDYnlK5YPC_CD2lbVUrvFwBO_vxhaei5evVaZpjJVyFnC0bVQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇪🇸
🇧🇷
خوزه فلیکس دیاز: باشگاه رئال مادرید برای فروش وینیسیوس جونیور ستاره برزیلی خود رقمی بین 160 الی 200 میلیون یورو میخواهد.
‼️
آرسنال آمادس تاحقوق‌هفتگی بیش از 450 هزار پوند به وینی بده که در تاریخ این تیم بی‌سابقه‌ست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/26651" target="_blank">📅 00:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26650">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/185f669e03.mp4?token=k2SVEyA0gw5bFrVikEcMHPrud5om6OwJUF2GsbIvH5wazCb-nng77y4dFElteclBirWeaXV0_I2XZxPfoyS3q_4Uj0ng0-TCuB6I7Vy751e0RxgytEQaSMo_jkSPv5JV9KrXa6FstuIbsTc7gQSXpUkJ0O4tnrOT2opQ6uYwoB92DfHhWHY6PtcRW1_qs4revOSoEM-6dKYK_Lx41pnuG8Ekkt6O4DhzdRzSESfjUDoyS-4E76VTy-x4Fj__W99sgEUIxC6LQ2m2C5NTsA-n6rp249iGB0D9nFSdcyK4D1i2N0ATUJejw0qRJ6XEEPE6l-qQoaKIUOyqooukyLmiDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/185f669e03.mp4?token=k2SVEyA0gw5bFrVikEcMHPrud5om6OwJUF2GsbIvH5wazCb-nng77y4dFElteclBirWeaXV0_I2XZxPfoyS3q_4Uj0ng0-TCuB6I7Vy751e0RxgytEQaSMo_jkSPv5JV9KrXa6FstuIbsTc7gQSXpUkJ0O4tnrOT2opQ6uYwoB92DfHhWHY6PtcRW1_qs4revOSoEM-6dKYK_Lx41pnuG8Ekkt6O4DhzdRzSESfjUDoyS-4E76VTy-x4Fj__W99sgEUIxC6LQ2m2C5NTsA-n6rp249iGB0D9nFSdcyK4D1i2N0ATUJejw0qRJ6XEEPE6l-qQoaKIUOyqooukyLmiDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های‌جالب بلینگهام از زمان‌ بعداز پیوستن به رئال مادرید: کارلو آنجلوتی گفت فکر کنم بلینگامِ اشتباهی رو خریدیم. باید برادرش رو می‌آوردیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/26650" target="_blank">📅 00:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26649">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLwjSavTUdpbAQYMtC1TN5nrhqESzs27_4vou4HCPLM_1-O4oj1Lksmm6_fAI3j0QqxcXuRqrv7jsGAlxJjfyb1vyIozPbGq7bj_U3utTmJ0RML1lJu-DJVqrIMu6VoC1BbC-Ro6sBA-B8kA6anggF2Rxo448oS0xbkv26JrPx0McfWMsaepI0BtWx-4d-JslaJ4LipUjIU6kNhPA6gycJ_a1iY5RUGfLqU6PhonmQ-lVNvb06-bwkBGzivnlJuwAlxH6YMdC57BtiDJ5Rb8ycbFav_aQDpD8qDO5a61E83UHXM_ouEhlj1CBQO-q94Tcq7jtJv_WXiRulWEog1QqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
#تکمیلی؛ تمام خبرنگاران معتبر خبر از عقد قرارداد رودری با رئال در آینده بسیار نزدیک میدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26649" target="_blank">📅 00:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26648">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2r1pORBUsKNfVPjmIOr07yJJUiDRXXBXmv1DdsdR9H0tQnUV5-NJDLs308zReIzh0YXH5LLtDpauBxm2GFHYvymVsh8anHYi2oA0IrZdW1nj1B4G5tPfYNFWH89GOM3y90r_fJW9dWDoQlFy9bqgB_8QIV4RgvRqWZMG8OCbriMsZ8i_WnFtBwAjPpORuOhOwK-etsRuJ1tqa03pndIhN3Jx0np2IK6NYhrheZsDDEiVgswbKmHUb3QUB_1aVzMauxcNKioHgr0ZEUB31qGN_QFP_o2lFulkhlbuN3j3tfTYmbetzVniLd4sAlJpdqWq3CHwq97XsFFhUCuNeCipg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان استونز مدافع میانی تیم منچستر سیتی برای عقدقراردادسه‌ساله با اینترمیلان به توافق نهایی رسید. استونز به‌احتمال‌زیادجانشین باستونی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26648" target="_blank">📅 00:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26647">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NuIArDVq8cr8QNJyE3aDaYfRd74BZZyizCpPoVcw8AK9GUZmoc3vW6-f3MTx0fvmHmUi69AhGb7peIZw5oz4XAYKDmmXkusnMZRl-EMkbRsMShmKsGTHNv28tt3iVK9ebJ3N5y5KO0UNt4Aez0MSrOXtNzLWoYrvD2PV3X5Kmk9KtzmrQmriBZ2u3UZ3t_2582gjpUu0pvQVwmq14UkTDx-vB6sdp3zK-mSBWoAzVUHjVEqm0pEYul4wnGliM-3Hs8ScO6MLrJA6x538mNpUdyxI1ompHK4dZSnXLQnHEc6Lu1botKkasP43n161LH7gyrmqJZlF3J8A3YJ9j9yLRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
امشب‌محمودرضابابایی ملقب به "بچه" به رفقای نزدیک جواد نکونام گفته "بی ناموس عالم هستم اگه اجازه‌بدم‌باشگاهی با جواد نکونام قرار داد امضا کند.
‼️
سرمربی‌سابق استقلال ظهرامروز با مدیران ایران خودرو برای قبول هدایت‌تیم‌پیکان به توافق رسیده و قرار شده فردا به…</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26647" target="_blank">📅 23:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26645">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e09976f50c.mp4?token=iVek3tyi_Me8t3LHdCn39awowy-J06y-NUbZnq6fz3jM9SADZP4W092L1j51-hX1FJm_az3r9eu8Iozp9bs7gVjieceisrb3lx1KnwufXqHYDOVb20p0i9TVIt_5humqgQu6cqFBzXXd_TAFEmZ3AJOlfG8Ba0y4VP5ADVr7SuHskXjLIB22TaaTAkj8UpH2Qmg82nNfwEZFBtyBsi82FSGJjWl4g9eJmj81MhssVv1xXIGVZOMMmx8LWuitok9EcWen3H1v51PPF13ehb6daqO0ZQxfazEVfJl6XI7ZhlFgisHdAATiBElMisYXOIGh_b5cNVckqGNjr2IJvElrgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e09976f50c.mp4?token=iVek3tyi_Me8t3LHdCn39awowy-J06y-NUbZnq6fz3jM9SADZP4W092L1j51-hX1FJm_az3r9eu8Iozp9bs7gVjieceisrb3lx1KnwufXqHYDOVb20p0i9TVIt_5humqgQu6cqFBzXXd_TAFEmZ3AJOlfG8Ba0y4VP5ADVr7SuHskXjLIB22TaaTAkj8UpH2Qmg82nNfwEZFBtyBsi82FSGJjWl4g9eJmj81MhssVv1xXIGVZOMMmx8LWuitok9EcWen3H1v51PPF13ehb6daqO0ZQxfazEVfJl6XI7ZhlFgisHdAATiBElMisYXOIGh_b5cNVckqGNjr2IJvElrgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
👤
طبق اخبار دریافتی رسانه پرشیانا؛ پس از کش‌وقوس های فراوان و مذاکرات با باشگاه های لیگ برتر؛ دقایقی قبل جواد نکونام با مدیران ایران خودرو برای عقد قرارداد یکساله با پیکان به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26645" target="_blank">📅 23:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26644">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7c-OdHAssw_OLfL5ioe1VGD4aGM6brN9GPYHfsw0vzKQ1_MB6ejqBMQGB0AygRkXce3Cwf1L-3MULStrT64sz-GAg7vU47vRI8IPdioVWJCu3pLlq4GN1A9j2nawroPSUHWKXl_thQTXv29R9rE7v90n9VGSptLtCyfFQfD8iLzIpR17xdTjpzjgufv8g_qCqgVLCFczWzw-PCbvMtT1gBxZPEhYbUU5PEEHVv4V62T8ygNaAMlZXw9g0WT-00n3YTjWeG1VB3FCjytxBWQWbDq8Dg7zaiut_XRFHNOo_Ij4ZKR7GOFoTeltl19X7Ebb5rQGbrBA8HfqqIYyt0LYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
فرداشش‌مردادحوالی ساعت 16:00 قرعه کشی فصل جدید رقابت‌های لیگ برتر خلیج فارس انجام خواهد شد. مراسم از شبکه ورزش پخش میشه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26644" target="_blank">📅 23:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26643">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVZrr9GPBCcvOkiWG3yoyvz7bTsuJwOWw-BxHy1Jix-9g61p6nHLVZiSzwXdUNr7tgfIHPQyoBiKfqQeIgPA4KHlgLmSvMo61Xm_cV5AUCR2o7n2QZBt9c-e386TqXMmw9yew_vE6-28M3cOXieYxTH4bRygfghWAw8FRQQE-BQI_dT8sn8MGSghfp8UR9nTbnoZXewJPtxrq8dfD5gmBd1MftuMmPmOS4hjrhJEydLO_3nYvoVrzHNiKD-7811nRgE1Tm7-De6VzqhiHPqST8tI7PM7kG3jPsOuaRaJum7Uh0PZjG13iXS5lN-fQqtALEUItn_UD5xC61gj2d0e6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
یکی از مدیران باشگاه استقلال درباره آسانی:
🔵
با توجه به اینکه فسخ قرارداد آسانی در سازمان لیگ و فدراسیون‌فوتبال به‌ثبت نرسیده و باشگاه هم اسم آسانی را ازلیست‌تیم‌خارج نکرده‌ونیازی به ثبت دوباره (new registration) ندارد بالغو فسخش و توافق نهایی، طرفین به قرارداد…</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26643" target="_blank">📅 23:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26642">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrMZzF2Pc23RjyI1F_fm6PNVVROD-YdYKOFeHx8Cl6IxnNZtU-eu8pQzlG37FGmbGTH33t8xKICIT3QmjfMi9DascmGOhGjUuJKgGgbubJyMVwPqRalUkFkOzJehA-z15B51Tghrw02bczflqDaX5b_VrO6HdB3n0nR-iZbxxYhiAwvTeHqg4gPZS0Vq5zWUFlRBTtK7G62boDIKqWgtJxQLgAepjhNaGcOf5b1T7XTUM3GFqJ3X5qybHOC72S3xxPSXiLsy4cTBbQMFkx4LZlVOY2fweG-Qv9i63jFfiCeF2x0IfmRJeFdjqBZadMiehLbfNNf4XmDx-SIxwKOIUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرنسس لئونور شاهزاده اسپانیا امروز درحال شنا کردند که ناگهان با شش تا پسر شکار شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26642" target="_blank">📅 23:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26641">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afWmQib5rUHSaeqx41eIdmFmnUQDYPjvvGn5gPYW9E1j4q8nSG3IIuxoP7r4XCSlPZAPfsPrslWvxCdMvfKkH9bzahzq8-M3yEMOwzuVuSZEecrJgGoWBq8YaxvqSRPIvKUs05LChIv1beaxnMi78UUN9vIFvO4KMh-7lXv763tr-VOIqV5QYFc8BbHokUKAJtXoBq5bwoy6nUjOEI1fOntOyIcoDXqFJpUBJWxG4goYA5oC8XKM9_dnHjPMzy85u3SL__spoDMIxzvTDmW1J962wX9nXvGs7-XvKWkASe3NmI56bmN5MrSNvLSj_vxOeuILA_YaxiBjHPS_rBv3kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
خبرنگارشبکه‌باشگاه رئال‌مادرید: به احتمال فراوان فلورنتینو پرز بعد از جذب رودری برای جذب الساندرو باستونی مدافع اینترمیلان اقدام میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26641" target="_blank">📅 22:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26640">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAVxqz-k023Czfjv6fSotMwleBPviaAqr6jU6Dnz7QwpV-OoAJP5ijS_GiepwN5N1vxy8eSuK3iMqWO5xr-KWDOALx4kMg6KxAkoQTDPJxdl8SJfAGyobI61gLe6qNI2ghqE4GLA-0GcqR_5cDmgTT62f-ODif8kB1IZbCHhYbOJNk60mwax99bQOIHvufIoo-HzBA2rVucM7yjFyFmVVB-OzzPG5Eht65HIl9hX-KoySrbV_A9exSqHYSxVmNu_kMRQA5T-miSvyejucVB-JiRS5G2ZJ3MxFXz-04d-lJqcQ6Qf_kFnNLgBiYfD6ygtcFkxfBI8NUHtcq6JKPiLwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#نقل‌وانتقالات|جیمز ترافورد دروازه‌بان 22 ساله انگلیسی برنلی باقراردادی‌بلندمدت به منچستر سیتی پیوست. احتمال جدایی ادرسون بالا گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26640" target="_blank">📅 22:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26639">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ebn3Oav3ENHGihPPfuLzm31y21ZX5dDXRGq5u61AzpYfbmKI1yCsxJxv2kz9FgLy-wVRYrOBAeTzjlGN3YWHvvAOeHS5B5NAL7cqdGAHIMPXLd_zw8S1nZtXGh8BQLNqcRXlr3APkVaKsjV1zAvOEMMRbMTEdrO4DbRzwdPCOodkJYpHHB1fw3JqmtxD4GxLGmvjy1bb4bSBCSdhqzw2Z80EjpiW3Z6538bu5-zW3xdrH4PEI45e6PnUx76icToJ5048qY4I3Ko3keXJD6o57jf9EUHSbBY-idl7O-yaMgffiGDh50UXEZWFN2C4hePCRGMp6IzKDcfd7g7Iq9r-Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🇮🇷
#تکمیلی #اختصاصی_پرشیانا؛ منصور عظیمی تا ساعات آینده راهی امارات خواهد شد تا رضایت نامه این بازیکن رو به الوحده پرداخت کنه. انتقال محمد قربانی به تراکتور نهایی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26639" target="_blank">📅 22:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26638">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNvzLhdu8J9ERA_moJ6UeuTL7OGUabdBKAO6CPtTo4EViF8wN4MbtrjJRseehHs_1mU1orAgkQLN9t4LB-UHqXZzXnS_kKvfLsuDjCXZ0Y7Q36QdkgYfsnZSEasFkmNJ2OgcoluCDiippe6IXIUmg5LRR7NDvXgmoVGOqnCgOw0jM9Q2RdodsSSck-i1k1eJJyjsLSCTbr9DWfWDbk_SajSMg95TbrUmVy6VVMhv9esv8AKOVKxcmo6OPp76HRpXVePq8XJT3H_TAgzTMtjKoUjMRoUpvSI4QSw10-OPL-3t529JSczqPZiYrHI1c9ACY9U64t3ae2uzDx9u7BNjww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
خبرنگارشبکه‌باشگاه رئال‌مادرید: به احتمال فراوان فلورنتینو پرز بعد از جذب رودری برای جذب الساندرو باستونی مدافع اینترمیلان اقدام میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26638" target="_blank">📅 21:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26637">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iezHALUDPyaKTAqYMvG-PnaIoT5cHYaRc3D8AAjNsodqW5oNoeZ9AU3QG0svI-3uPOdb9DshS2XcJaWZH1_1fqhSgnV4I_JFMPXXldh4LLCCdkyGNWK2Nn1_xoHS4JafCkF_LOR3m1WValHMag0YM4iFkFw0RAGV6IKL5L2BcbyCcx4n8QfOsih9extUUgza3EjyNO4cU-PmMxlCEr-ootie28c9f4Lyh6fkVH72wvKgXlQ0uBaQ4raS7xoevD9d8UQVqStsm49_faZAYjuEF8yiljFkFVbC4uOWCWm-qULeR_2Wg1SMvhpzq90PTIXPiT7FoMhysgqqOhPG_rKT6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رسانه‌های عربستانی: باشگاه الهلال عربستان در جدید ترین اقدام خود با پیشنهاد سه ساله سالانه به ارزش 65 میلیون یورو به دنبال جذب لوئیز دیازه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26637" target="_blank">📅 21:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26636">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KtBUYlzzlckbmENEqs-U8zU1VUv71umgjviTahPSTeHavnN2eINxgcDTsMBDZ5DeGevG-jEKu7eldg4MZa-ga9spMBNTLru-ZlUHqVuMmYERb9JZ5hE03_fBFUYSnwvt79Va6auw8MUEB196LYx56ew4Yvc5dhnVFe6qNtOODJoiiyqJKJscTEH8JrryK7nk62PWHJr23nFD-L-af-kQhVqBk3YDK_TzL4JRX3Kmyd-9QCgWCorJdd6Ml1wV9Uee7c9H1kJzW19qqf4AccIHjFphtbmzXMARyR2EUBG0J9SKfHJ-bMC_yZavUT1MqlVPl8CWxojYnb_4SkWZgB3yzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
فلورین‌پلتنبرگ: ژابی‌آلونسو برای تقویت خط حمله باشگاه چلسی خواستار جذب دنی ولبک مهاجم انگلیسی 35 ساله سابق باشگاه آرسنال شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26636" target="_blank">📅 21:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26635">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-YY6c6hOq38GAzxNkazs6j1fBrQuC4EVSHFYYRTkfq4mD44qCcfZLQDbk0Ux-9LHWgdRjK8CCLwXIY0BnGE8kaz2WYSMELXf5-dQD0PaJ-pYsJR-7uPjSgNGXxTYt6McZpXw1FeGpmAQ4WgQRaFRtGZ4cm_gkozpcIlb3pHvn_3hrDDaX7JB55R2JMW6HVdpuZ60-lGHwUzPK1WlA4W4YdZDQw09X-g7xnlctj26g7S1dUT4EQENSnlnDH2kTFFcZIVsb_w4U3Ml-HJYDgRw7UYNX7AXLxnZwwGV5y5HeEtwdMiZKM_euT0BQTJ5At7oV_BKiZewySmMGpHZ0GEZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آتزوری‌درحال‌شخصیت‌گرفتن؛بعدِانتخاب روبرتو مانچینی‌بعنوان‌سرمربی؛حالا پائولو مالدینی اسطوره میلانی‌ها بعنوان‌مدیرفنی تیم‌ملی‌ایتالیا انتخاب سد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26635" target="_blank">📅 20:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26634">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAmRyG0X2EzkBwzC-xNfK7swdTP1WWT1qvO--b2VpBpQUeu6d2Afbo_7cU5E6H_FDMFxlUgAyNc7uny0lRvaImek2AdLDYnjYzdu4si9bjlx298CQi97P-6gSkXAh81XBRDai3I9gf2oX36a9ZX0eRXci9qk9yBTsujtk-nlah0ilkM2p5R0ImklVqFu3Pq4kBQJds02isWrEx_1t8BSKSr_1qZJ3_hWE0cuUKm4iZNVqspHHWemxfaVC5cVgq68NqTgYaf10csMpZ5mAWN-BpkBYZz88M4gDSHgqM-PDUMKtjLgzdQLMhXWhOxE6FEV-UcBSoUDepEEugTFqsshgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه اتلتیکو دالاس که درسطح 2 آمریکاس و سال 2024 تاسیس‌شدامروز به عنوان نخستین قرار داد تاریخ‌باشگاهشون با چیچاریتوی مهاجم ۳۸ ساله سابق منچستر یونایتد و رئال مادرید امضا کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26634" target="_blank">📅 20:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26633">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ILwcI6l_FxAkbEQCMtYw9vY0lu_7J1FoFM4fsxS-yR9lYrT6vxDJDbDvEgmlC-AZLaADizNxUNboJrz8E0b4ymlJ7d9SKCD9xUimR8N39viGQts4DiC5Nfv8hFceRtWqYS3A-DncJre7FTNd5uFUiZtUVH44y1skULJmNOimgtgV0PSfeFsfHW1usIvtPAMlh1apC2V4lIVhUhKWfULrwr9ezE7N8YcDlRBCpRWVgwQMQ1phHWR0bYtSt9H549h2YW7lvKbJ-w8sMQLa00xMAM3S-E2uBgKtwKqgqCCewIOFRa-GOLJOeMAP9Fx3OgZ9djSQnA4xm4tVoGwQ-3MtsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد کرمی دهن سرویس بلاگر محبوب ایلامی تواین‌وضعیت‌که‌میبینید داره شیر آلات تبلیغ میکنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26633" target="_blank">📅 20:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26632">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GaPX3G3naPV1DONar4F68pkr01FCXBs614zkdp_WVAkW8FwYuqxGFSckAhfUhiT6e9PWUv811DPtlu3NlkBZ8x_5RwOrvBlvR3F_vbI37MOkoze2YlUQpfPR-dSdbcFTRXnRpYBigAPXrZ3AWe3f9Ipa2udUWm_prvXbjKXlyP6OcyVLXR1x9f9Z6zX0LEh6RkE3rEboOJlNn0f_07uRITUgUUbUAHNz662mMJUrgPMqNemZnGz7kky5scrMHv7pfXF95uU7HESBbYJ2A452aq1k_IeTibTpzTfFr4-JFUSm2NN8ocEo-vLPUeWTRZ7QTvYkXTUIc75FvZkksRCT2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ روزبه چشمی کاپیتان33ساله استقلال ظرف فردا یا نهایتا پس فردا با حضور در ساختمان باشگاه استقلال قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26632" target="_blank">📅 19:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26631">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/utSoEEl0N-OwwmDkm5vWlrHsbCDqOTK5x051EzGBcIyuUuzYIhMZuHYZwQ-rhL47SJmjrOCXyn5B4iJhiGP-KGMUeYXXdiVlJsq3A1NqnzUnZTC-Mj6pIwnxRThgOmZUMC5cdxyCmbFDfK88dV7Jv9Ihx2r-fN6WKEtsYB2WX8X7XW50MguFfqDTWV13-88L1uIY10A4KIJTon53ga0DqcP6AtnedeTQWm541vdH-KwJLH_NKkedR45VefQvzWgWzDvNU_1AdJY9jTxddYvjEagY6f2cOxKcoNmSMlENp2XKLA1EIrFgIIvxD57oQ9uVIFXtAONjxvRXfdlksJUq4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
فلورین‌پلتنبرگ:
ژابی‌آلونسو برای تقویت خط حمله باشگاه چلسی خواستار جذب دنی ولبک مهاجم انگلیسی 35 ساله سابق باشگاه آرسنال شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26631" target="_blank">📅 19:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26630">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srlagS2x-rU6E0T4NnmrXJbA5qNp6cjVHfvDS-3NcRTUdbYjLHt1yaiURFAIY0YSFwP-SHlB0Pm0NGJxV7sdbESxu2fl-jJZ5KB1jbJUXci0Q7ZZ47xCITtqVmxJDoF5bIlWHwQqxLPLOfIISVvm_59auZekALf4y41Rp__Jelgl8Zph0vmtx4lOmDbBZNrFC0OMTGaDqnNd6sN8Q2gc8FVsp_bYvC94T-naCvw-iQRxCv-_lsBd9xaMBThEIRjrUD0wBwfRpGVMcUiBH4zb-Ds3-iB4FF9Cben1pLjLDusVumeo6jF5nHjjNAT55apxNsP6JUg2gxPJi3KcVbz1Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه چوروم اسپور برای جذب مامه تیام 150 هزار دلار به به باشگاه‌ایوپ‌اسپور پرداخت کرده بود و 750 هزاردلارهم به تیام برای 1.5 فصل؛ روی هم جذب این ستاره زیر یک میلیون دلار هزینه داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26630" target="_blank">📅 19:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26629">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSo64z5yMndjTUD8V65LdQM3_aQK4bjAaeqLQRRca2zJD3OPrSpGsW9nrDhnmHkC1ubYCHajxQJ1EFXQDU9uWZ58-zQtTE7QBl7fxbPAYMNvK1GjUuqFoOx0OvPp-jqFrglFVKKUT4FDZoXBhbtUJjsnbYL3IBE1es4t-XiCT4VpMlHQND6Kyay4QVz6B-HYiuOZqik0TU94SxkktzIrvpto-_t31s2YN6NXB04UED2ee-e99AzlvzWuMHMPvsrcQHLShZtXBjNNOhPbugRWAP03hGjDHzzZlRHYJGkDlAuz14roqgQ_AOe9msgcOEiU7qw2AR8qV_ZyoJLu7SjgwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرصت 24 ساعته نساجی به پرسپولیس! اگرپول ندهید دو بازیکن راهی استقلال میشوند!
‼️
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال امروز ساعت 11:00 باشهاب زندی مدیرعامل باشگاه نساجی تماس میگیره و به او اعلام میکنه که حاضره رقم رضایت نامه کسری طاهری و دانیال ایری…</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26629" target="_blank">📅 18:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26628">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pvy0Kg6RBM41PS5pGuc0lNNu4V9a3v9KcvoSfoPO_1-hmITolKlADd1wPvcJzze5ZyI17qtsjs0GscpXcqHxhft9AXFvYo_eUuX4FHo6xCdRxx_bUfXWLvZECazYSRUL3k2sQjRejf3WfKE7JR2TuhvMA51vhNanh99n5ypz0O0MP9fNcrteDE2FFi1lamTFplkVI7nzxoX6dA7GmV61P7PyLOLTi0VVaH-GLc-iyCP3E3yn5luBs_j1L85M8mUuwVqWDiyD5NZr38Vqj442GB-VGp_vuwmcb7sjnjW5fZJeVboTxJRB1kcFmzUZ4trY-iv8pMBdgrYEJ28mkhQuQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فوری؛ نشریه مارکا: الساندرو باستونی مدافع میانی اینتر میلان درآستانه عقدقراردادی چهار ساله با رئال مادرید قرار گرفته. توافقات شخصی صورت گرفته و باپرداخت50الی60 میلیون یورو بند فسخ باستونی 27 ساله توسط افعی‌ها فعال خواهد شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26628" target="_blank">📅 18:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26627">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b902abcc5.mp4?token=KgOOvWlbBGoLfjmzaihEk-gbj4eXeZ7ZRkLTo5FkXE5zM1K6hC8tkRzRgD4vGpax0UkzGqjPpKbHi-IKObXgnSynFPcyCTUEIAbxAlEskNs_hv8_6CGUXnPlxSfcPq_vRaGXZZVKN55XS5J_qYto614Ll5csAeli4PX7iBZSGl8gsR503V5aaHPr-P16cUWle1P14pWnecVd6Z2ugHnAmpmVlucKXG2tfu_UI9cfteDBfHx2ZRWAujnjbsVX1MjWPr2qFr5Em9drOV3axxW9RSRR5bp5twfV4XaaYPbiqkg0TEEdNWjn0vJyZN2vgtvIvnU8vOjfuBRwqQFD7RPOgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b902abcc5.mp4?token=KgOOvWlbBGoLfjmzaihEk-gbj4eXeZ7ZRkLTo5FkXE5zM1K6hC8tkRzRgD4vGpax0UkzGqjPpKbHi-IKObXgnSynFPcyCTUEIAbxAlEskNs_hv8_6CGUXnPlxSfcPq_vRaGXZZVKN55XS5J_qYto614Ll5csAeli4PX7iBZSGl8gsR503V5aaHPr-P16cUWle1P14pWnecVd6Z2ugHnAmpmVlucKXG2tfu_UI9cfteDBfHx2ZRWAujnjbsVX1MjWPr2qFr5Em9drOV3axxW9RSRR5bp5twfV4XaaYPbiqkg0TEEdNWjn0vJyZN2vgtvIvnU8vOjfuBRwqQFD7RPOgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
8 سیو دیدنی وزینیا گلر کیپ ورد در بازی مقابل آرژانتین؛ پبجش از 18 میلیون به 20 میلیون رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26627" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26626">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3df251c94b.mp4?token=qbIy_rHpbNuTmHLO4QcmV3kOM2hQwzHVnuKFzBdIocMb_YrQ3VyL026aV6HU_NGO33wte0oS94AoDkAB4MohiGS6vIonjn9l1QK32XGRwkbwWMNqnQungNuvL6xQ2_ufsnt5Pl8NB3Eag83EsGi6679xFRVko3aAPnDaifxJ_fEp4wGgaQawChBstHL-ZkipVbwiYUfbxyWsQcqQb-JwBQHtWPtmmUr9F8cLtSvzORZQCnOAe6UydeuffRQFdFUd5Js8OY0sGF9Fk02_y7EHV1Mmn8Rf6W6v-ov29cRkXIvL18YQogkJeG3rwBtNeXVvez0dSBjh0DeNE_XX9bW4MoItBcrPb0pZXzpYbldBRFP4MU_aI0jizQOrnym7lbxQ-RA0bgIOWYm1hF9S_Bj3tkbvqZsjVUvSn3La2n7xHhjbcvPwq43Ds0boWg-LXt8UxTPkRYnksFTh3kJFvRJf4kHAppjjphD-GRW31dyx9tlbAepwLIJLJ5yPX74QRvk2_-d1c2U1XjeYZjYedcWx2DQ4y546YFKlTTrmTFA_8Rp1PlmrHmxut0vvLrf6-cPVHfytNHgrZqrsNT4vKVZvMuurkz7M4LIaginn2uIazeEatO-6y8Z-8rUJ6VcRLZz1i8P9Vz79VlFaFKo5wGGtQ8HbqIT9vy0d57QCO6UlR8U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3df251c94b.mp4?token=qbIy_rHpbNuTmHLO4QcmV3kOM2hQwzHVnuKFzBdIocMb_YrQ3VyL026aV6HU_NGO33wte0oS94AoDkAB4MohiGS6vIonjn9l1QK32XGRwkbwWMNqnQungNuvL6xQ2_ufsnt5Pl8NB3Eag83EsGi6679xFRVko3aAPnDaifxJ_fEp4wGgaQawChBstHL-ZkipVbwiYUfbxyWsQcqQb-JwBQHtWPtmmUr9F8cLtSvzORZQCnOAe6UydeuffRQFdFUd5Js8OY0sGF9Fk02_y7EHV1Mmn8Rf6W6v-ov29cRkXIvL18YQogkJeG3rwBtNeXVvez0dSBjh0DeNE_XX9bW4MoItBcrPb0pZXzpYbldBRFP4MU_aI0jizQOrnym7lbxQ-RA0bgIOWYm1hF9S_Bj3tkbvqZsjVUvSn3La2n7xHhjbcvPwq43Ds0boWg-LXt8UxTPkRYnksFTh3kJFvRJf4kHAppjjphD-GRW31dyx9tlbAepwLIJLJ5yPX74QRvk2_-d1c2U1XjeYZjYedcWx2DQ4y546YFKlTTrmTFA_8Rp1PlmrHmxut0vvLrf6-cPVHfytNHgrZqrsNT4vKVZvMuurkz7M4LIaginn2uIazeEatO-6y8Z-8rUJ6VcRLZz1i8P9Vz79VlFaFKo5wGGtQ8HbqIT9vy0d57QCO6UlR8U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
تیم ملی والیبال زنان ترکیه با برتری سه بر یک مقابل تیم ملی برزیل قهرمان لیگ ملت های والیبال زنان شدند. زهراگونیش‌بهترین‌بازیکن تورنمنت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26626" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26624">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sna7-9oEzZqAz7dXvf-h-qwIhUm_Z6YegaYkaQuMak-4nb67EuX-MMqvAIvw8d3-8A5hc0hzL-wUVFyQjde0asoSdjdPf17Bxuqcl1frp66TmgCTEMNgwdf9WIlCMlJhAoC-jDjoHceuqyO9jH9OSThsSsnfF-4akXlN09hSOmiIUyg85H4R1Utu8Sjg1kbdczdSY4OP5Sm8eOLyABmr-OpPVqjfRsjg12sY30HnbBlVzrp1tqurmbMtCYto460KwyFjjsxw5NwRa3Jl73yxbwkVO5GfiVX9nKr-xgty40Xd03zsnH6q7dlB33XVKCR-n2CKErXb8nknLTL-2X4Qtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#مهم؛ اینکه‌بعضی‌کانال‌ها میگن زندی مدیر عامل باشگاه نساجی‌پول‌پاشی کرده که با قیمت بالا تری دانیال‌ایری‌وکسری‌طاهری‌رو به پرسپولیس بده واقعاصحت‌نداره. زندی‌بارها تو جلسات با مدیرعامل پرسپولیس حاضر شد و گفت حتی حاضره با همون رقمی‌که طاهری رو از روس‌ها گرفت…</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26624" target="_blank">📅 18:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26623">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l27Tc31hNk1P4xVgN6zpBGEpPU7cMdh-iyEbTWcvoOUsI8AMp1Uk9ovOvMWtJ6pjeVR386A9FBWDGnWitI3gzk_AdXEKZSJ3rRZXP_RA26RZO-YaJzPTQO9Zp2UhXbGrNuy1qz1ZxZfhZ5HeUFkcY8W97vn0YvN5bDcK-SvyRtEEUSWkfLuWl1ICsxTskhYhf-6FpPe0HMIOIkUsXij9_vAy1Xuk_ktZbN76eDBvPa_C_TGfx-5vO92HrmImQHHvLu63qzbd9Xh2984KS3B66ZLNGJp-qBK4X4ww1u6RkVnNeRUlR8v5ghknwThf2o6SDF4ThkKvrhFlid2dWhB4Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇪🇸
🇧🇷
خوزه فلیکس دیاز: باشگاه رئال مادرید برای فروش وینیسیوس جونیور ستاره برزیلی خود رقمی بین 160 الی 200 میلیون یورو میخواهد.
‼️
آرسنال آمادس تاحقوق‌هفتگی بیش از 450 هزار پوند به وینی بده که در تاریخ این تیم بی‌سابقه‌ست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26623" target="_blank">📅 17:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26622">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZ2UBaHX1_KTfQmqTXvyWEstLksD0WvMZOeef35uuw6gczCW3-gpGqhSTGN_nvLOGrDdYrWcG8-PdKf4to4jq9g0PsPz4YydwVFXqbF66QyrYxsqJzIpnmQgHltDI4_Z7wNqaS56ZkPNd31t2ndeH5pRcn5hThpjCTyA33Wjkqpe9mQ94Kr7rRluYl1dlGHTXNI5yeGcQl8zgrP192xGrABs2wUfxyVsHFsNthoCcUzzeW1a5_gZEbBL27ZebVa6JwPALTugfRrfkfWSYkGjdYFdo0ln8TcKf_5u6tDXhrgjAa9xdhjYBPSO5nMFxA8MrI4HE3BXSA3b2CXUZLRPPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام فابریزیو رومانو و علی رغم شدید مایکل اولیسه به پیوستن به‌رئال‌مادرید؛ این ستاره فرانسوی این فصل هم دربایرن‌مونیخ موندنی شد اما تابستون سال بعد به احتمال زیاد این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26622" target="_blank">📅 17:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26621">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q41YLdq5Cq2VFjiWfnoXFpZbkP8hA1oEZhsZ-ekoZ8FLeVEAMoblZoc4ddRcIxB4PobGW9ozLBi1LdRBo5eS2pSF1pygvrW-dozaI4y4eHGQ7jNxVCxA5b0tH3arUgY5_AUuLk1dzXK7cKQTIm-ICZOarnxFg5SzvAKw-RVRrMY3mLM-oDhHzQj2WU_wbCw-Wv6pqt9gFjFXyoJeMWCZEcGaTJW_va-wY5E1EfhkveAWZ20H3SQy4qo6IEG68kKsnzp6UB4eBKwaAFq_sHMGE2j1hpAS2FovfBZ5fprAW85uo3Q9OF-FxJR2TcHsnlXMBAoqWF0pPNeokBzeH9yfDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
فرناندو سانتوس‌سرمربی‌سابق تیم ملی پرتغال:
حقیقتا من هنوز از این‌که رونالدو رو در جام جهانی 2022نیمکت‌نشین‌کردم پشیمونم. ازاون زمان تاالان‌باکریس صحبت نکردم و رابطه‌خوبی نداشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26621" target="_blank">📅 17:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26619">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1a0b40618.mp4?token=hGKmS8mByh0igh4qmUVx6XIezwf5pVGoKn5C64OwJQVmx7moJQgieSGJB9lD4W2imMYFZjSXLmBpPlRFyh0uUaccfrnnoukbPOXu35i26mhd4R-KBZsCYM0jMULYJ0CVTpiAv0fAgFOr_TeuNr3YN5QWj8fB0zSYhNbTqJKKDmCHAWa8ujvAKazhfL9RzebXgm4O3IsXVZ6YdSOTSYg8tS44s3pWRiZ-uu-wRfLAna8RTpTutWJSLVXzgyetvOQDGnSqFHw-WVJqpx2n_Kg_QI8nq01lyrqMK87l0wx8f9OfYbyDWcASRNvTUh1IQ2XCOBg9Jag8C4TptZ_ublUNhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1a0b40618.mp4?token=hGKmS8mByh0igh4qmUVx6XIezwf5pVGoKn5C64OwJQVmx7moJQgieSGJB9lD4W2imMYFZjSXLmBpPlRFyh0uUaccfrnnoukbPOXu35i26mhd4R-KBZsCYM0jMULYJ0CVTpiAv0fAgFOr_TeuNr3YN5QWj8fB0zSYhNbTqJKKDmCHAWa8ujvAKazhfL9RzebXgm4O3IsXVZ6YdSOTSYg8tS44s3pWRiZ-uu-wRfLAna8RTpTutWJSLVXzgyetvOQDGnSqFHw-WVJqpx2n_Kg_QI8nq01lyrqMK87l0wx8f9OfYbyDWcASRNvTUh1IQ2XCOBg9Jag8C4TptZ_ublUNhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
تاتیانا دوس‌ دختر هکتور فورت ستاره جوان بارسلونا و حامی تیم ملی اسپانیا در جام‌ جهانی 2026؛ گفته چه آرژانتین چه انگلیس بیان فینال قطعا اسپانیایی‌ها توان‌شکست دادنش رو دارند.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26619" target="_blank">📅 16:54 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26618">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KtnsUOUbGxqlhmP2vCzjq8tMevWzL_qlVVRWHroRxLs4yhZr9c-78jEyUy-SI9SQwfof6-H9DOz6KZZfq6XJAKvpOSatUI58Ey8YgU51wKD7UXJUQ6jsLkdbg2F_bpVrcUbXqMN-oMjFCGucaOv_CMNZ3PGkcjMKyl7rqhlD_2sCC1CDSLVi5NzhKtOKeCr6Ch35S4uA3O3GFEAiyYNNQm23VVyk29D2-YIa_uo5H0SGAW3xVpGX4N7oJ8FpKrywETbAtKaKYWvy6Gv5YhuapZSZWRzsk5lrf0OUt0qU1TQxuJaBNucdOafYAOmbilemrMTduaOx7--qg7y3W4iTSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26618" target="_blank">📅 16:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26617">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-RBMqCbB_mJ1bSeffB6dEj-pI9RMpWQIzneoPcJFT-g71Ims6MWA7FMwLO-8N_c4jhzVtZmrE2qwF_FkDLY-Wz9Q9rqPnEpnFBoVLDN-V6dz3EfSyLWFBIVorJB30xLlkzwr7_QHK5S2qjdt0uvWEhJU2dS98vrlmW9IWxxuoSG3Mvj4zJFyIyoPfVpEw_nfq0vx-9nsG-ae1k4N_V_wAGzZsOf7RL6JpankftoBO0OB0V1fhD8wtmvRmjYWzWXIal4pUy4G4KesZquky-ZiuEyMEIOrvPXW4-mKRQ7eeP3yAEUitUJALXXaS6fmUWhLsF-4PtY9GMBFNMjtxUjzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26617" target="_blank">📅 16:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26616">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjfnwX4WGWR9qXpEjptLWxoRUIGaDK_lNuy-fX-S0qTdKUGGb62cZ1y2oj-1f1IG4Ps6mntnEasWJzMz7x0YUBmPeIxGa0Xoz7D78b0OTpFAJy_IhGPMnM3OZLFE7sjQOsjITnWEBktW1kp-4KJ08duvacx91XRCk3zy0a2MGM8n94fhjRAtMN-Rpbkor54drFYCMINyFOYMxv-iOVxyEcbakc2fl2Hse4S5ZiqpAccsBUv-9MFhon_tNUcRYMRaww0EdAqwrN8Ju0EqN3dR9GDXvps_peMo_hvNMtidDhm0TiukKUs8RirBUAaxIJETqRGXwiSF5jlkUnJhGi4nng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پاختاکور ساعاتی‌قبل با مدیریت تراکتور برای جذب خامروبکوف‌به‌ارزش 800 هزار دلار به توافق رسید.
‼️
درحالیکه مدیریت تیم تراکتور با پرداخت رقم 2 میلیون دلار برای رضایت نامه محمد قربانی مخالفت کرده‌بودحالا بافروش خامروبکوف…</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26616" target="_blank">📅 16:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26615">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrVieBooMwWfQk5l8figlLAnL7v91ddnh_UqIWUnqFDUz5HujobwHgblLp_yVVTCAW_Hq6FZlT-F4lP0GJY5GYXoG8GitVbD6AQEKpHInSPibMPrI18y9Fm9inhx9_zLzCQN6ld73NiPTJlIEorpRXb_LTmRgHFWNn05cFbzSwVV69aYpyg5zSG4uJCvMmQdYyEAhbKryZEVfmnHYN3FWtvjCRMTTTE35fpjMfoBxJ6HwzYXYxwhzePvRdmJ7rKSReR9Ra5BRBJFLsPmk9fwe8EFV_AJiiYZdXlc90dtLpxvTFtuRJXRBI9zRiftot1dAfpZNwcymQgqjIvB3BrtKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
طبق اخبار دریافتی رسانه پرشیانا
؛ باشگاه پاختاکور ساعاتی‌قبل با مدیریت تراکتور برای جذب خامروبکوف‌به‌ارزش 800 هزار دلار به توافق رسید.
‼️
درحالیکه مدیریت تیم تراکتور با پرداخت رقم 2 میلیون دلار برای رضایت نامه محمد قربانی مخالفت کرده‌بودحالا بافروش خامروبکوف بزودی برای جذب ستاره 23 ساله باشگاه الوحده اقدام خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26615" target="_blank">📅 16:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26614">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dw7Z6WCDLwYtrvIiAiy8fcqM68WK7qqHzXQsxpEqjn2Mo_KmkMiuOLkw1HLef7hCB071su5UtEXRzQTPSB42vUQf3KY0-wA5y5SruKtzRkegKyNsGEQyXodzk9r22ZiF2Nsto3V0uPOCuVysh50ygBn70norzFMYuJvAj9QVae6YPRACiOIEefxU_9GFD8tq_YUkrNJ-NMq68p-c2L0nCen0zawaCbbdQ4BYPiHLzNtkdXLi9_nAdnc-KgFkiObhrQhKEsKiBC_ljlyl8imPAGDa1lf52toMoadC9AH-c4hoPN9ocZO0-M3gFTz_fhMg28vMmL-XBpEz_OkZ74LkzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرصت 24 ساعته نساجی به پرسپولیس! اگرپول ندهید دو بازیکن راهی استقلال میشوند!
‼️
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال امروز ساعت 11:00 باشهاب زندی مدیرعامل باشگاه نساجی تماس میگیره و به او اعلام میکنه که حاضره رقم رضایت نامه کسری طاهری و دانیال ایری…</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26614" target="_blank">📅 16:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26613">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOST9ed34vYDpGe2iF4bo8HKvefD1H3jKh6OQIsXoODHyoVO1MA580D2E8KSMEhZP-eVPtAWHle1P9LHHsCc-SZda-sVD4H_JAyTJWbRo-PN2c49VJ6MH8ZnBz4QgN1H2_cND7Njqxz58pb8PlTXU4Ha8mGFNDaGIxC6m-gnHtI_yb9Hy2a7Z26v6rTEKY46CjfLZ-Michf1YisiljXA63Ul18AfG0a3wooqVgcG-eINNihrhAZ9nWH97h-s3bhknWyJ19gr7J-2jEtW5FzxNST379G5QHptlkn_b4jsO4C2uAQ5fuYRqHTNpdZJFFLfXW65QbwgyBnTPy8JtO-HSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
طبق اخبار دریافتی رسانه پرشیانا
؛ پس از کش‌وقوس های فراوان و مذاکرات با باشگاه های لیگ برتر؛ دقایقی قبل جواد نکونام با مدیران ایران خودرو برای عقد قرارداد یکساله با پیکان به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26613" target="_blank">📅 15:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26612">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HS_SvZZlfEmN-GCvz7xzg5G3w5v8WOjhcCvm8tqFnaiBtkqr-cqvZo4KuWQlGRypoLdV0ZYQkKiqAq-vfa9Ib7XiFzJPMzFaKQUije4Jf6S1dP_XefZ4cEY5l0QYrpCwhopYADUSc4QmHtrvN0ntehLK0VSiAkqs8YHOvQYVijbYAYH2fLrmKs1tJZrurt2gxh6OKGlWzLWdEcZ8wIP05nfnhfpvDYSBhSloJ-zqmVNXO7yItBz5y7rUOansBTtOvBJo1zhYoo9tVrH6NHRcUt-q2VPmXaCjuATTA7-NzrGUZ8SAZNU_bCPCd-qfz_i3H4h81U8D5cXW6ZNAquT5cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
یان دیومانده ستاره جدید رئال مادرید بعد از پیوستن به این تیم این تصاویر رو منتشر کرد تا نشون بده از بچگی فن رئال و رونالدو بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26612" target="_blank">📅 15:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26611">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWPy-nrhsaP8ZvTbxuhF1O5oWuCW55ecq86kddDWE0EcbhnyXzGQ4VF78bkNcTW1NjMglgIujl1ez7I1v0TEVlvLm4hkYZOjq4YQUbkmTHKIqYUThXPfhosiJwyxR_JXGEIubyoyrC4on66aDnifRhSKKMZDNQQamoCRi3CtucpMBdI5snySuVClgWvHiP6gGjfaFh6jVU-pzReDFlVAGMqimZihDbktUiezkO7BQuGfY8Z2vBvGMGlhmA4p4V5jMQedPU9hN3X5ijF98-ZpYRxTNbXBunanUfzgQrhD-fT1DDrEinKFLQYYvAgVcFTbrp7Hhx9HTsxsQb8RscYI4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی 14 روز پیش پرشیانا؛ با اعلام‌باشگاه‌پرسپولیس قرارداد محمد امین کاظمیان توافقی‌ فسخ‌شد. امین کاظمیان پارسال در شرایطی به پرسپولیس اومد که لقب فوق ستاره به او دادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26611" target="_blank">📅 14:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26610">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNvuiCPWv-uhBOynnp3_3SOvIStepyxTsE0Q1aJ-gfP_y6qL9r7o1BfgRoeEBIjRvWTqskNxqSbHnEAsfLLrsTHVBOJ8T5suX2_rKPAsnPF7N1PUzd__yijVhQP7btF_uPMT3ei594zfza6xAc97lLz5jorVHnV6sRGwCqzbmyuV9cRXfcLrp4TOMaXNA-6_EXeUHO49llgLmkmIiVRoVFJePEQcCattkLFM9U0s-MssUhubu9mGeV8isbPy4fM_m4hT6y_vPnxp3GawqR5cOKzwNTiNnMJee0IStfKi2b2-pvD4kFwD3IdXuGF4NhAlFVNGui6yyRNYKj2J4sOIEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرصت 24 ساعته نساجی به پرسپولیس! اگرپول ندهید دو بازیکن راهی استقلال میشوند!
‼️
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال امروز ساعت 11:00 باشهاب زندی مدیرعامل باشگاه نساجی تماس میگیره و به او اعلام میکنه که حاضره رقم رضایت نامه کسری طاهری و دانیال ایری…</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26610" target="_blank">📅 14:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26609">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b74811f44.mp4?token=U-b3b_2hIywAqT-XJqwIn9fDdJMPPoMmXHYnfVpNElDV97ZXihOZaO68cy8fPIQiFm7J19Kbbfe81W8P3VaryPXnjPTt6b5Eh9h7cuEo0eP22jDxvvUhiZ_Ng0Y2VUjup0VjTKCGdoj92P8eiwXdBcBOanyYmLcw30XjJilCUgmAR1_S6xNx-XtakXYaXY8hxhy6MkbqUCGrg_w-15kTQ0Ek-CLmNAYSXop3hJ61PXCU4uzGBH-o-OhinTcLCDKbcNTeh-S2jNZx90uTqG2NpLIGlQ3fhDrOrv7Y8Hdb1RfJGWTGQtSpZAJQYoaden8SxNzSRKK1JoZhO1Nyw8AIiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b74811f44.mp4?token=U-b3b_2hIywAqT-XJqwIn9fDdJMPPoMmXHYnfVpNElDV97ZXihOZaO68cy8fPIQiFm7J19Kbbfe81W8P3VaryPXnjPTt6b5Eh9h7cuEo0eP22jDxvvUhiZ_Ng0Y2VUjup0VjTKCGdoj92P8eiwXdBcBOanyYmLcw30XjJilCUgmAR1_S6xNx-XtakXYaXY8hxhy6MkbqUCGrg_w-15kTQ0Ek-CLmNAYSXop3hJ61PXCU4uzGBH-o-OhinTcLCDKbcNTeh-S2jNZx90uTqG2NpLIGlQ3fhDrOrv7Y8Hdb1RfJGWTGQtSpZAJQYoaden8SxNzSRKK1JoZhO1Nyw8AIiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
پوستر باشگاه آث میلان برای روبن آموریم سر مربی جدید روسونری؛ قرارداد سه ساله امضا شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/26609" target="_blank">📅 14:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26608">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SL2RWQHyKpEaWoUHAxAKme5fXNaNnZr17drwZSF7cL-QM1bGWwInLxNWL6j3fL3iiKwvF_OYISNbpyVv3qrFpc0YRm-0mBE-XL2DtKwpFOtHjoUBjjPbXM0NTEAxImjPD4ac1h30FY2D3wGhEuCrXov565GR5UJMwhK5v9s4YJoMZMHGZj4UV2V2QvlBw8mH4OE7jndlosEzJMbqsAB7fFeihnRBE5MuNy9HQAK4wmoDgRPKX2bEEWbIpTTOMeIiQ8BpiIusByy6uJpCgaw2MS57GuAVInz5ZkVAIk9Z2jA9yGuHn8oNF6en9Rl4ozTtCxSViAi29LjJG3Kk9v2WKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه نساجی دقایقی قبل رسما بر سررقم رضایت نامه دانیال ایری با باشگاه پرسپولیس به توافق نهایی رسید و به‌زودی رضایت‌نامه این‌بازیکن رو صادر خواهد کرد و باشگاه پرسپولیس پوستر ایری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/persiana_Soccer/26608" target="_blank">📅 14:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26607">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_v7g00cTf--__ylWCnaiKXBuh2eDtim0BMtorn8_TR4-t9sF_VBoPZ2ELTcyh2tSRN-1p_TL_9knKrcQyKj42EgnDXpj8ieetK8CpZCv9acd9dtEb976Evgi0KaOXqkDq2vK3Jaq_7JlBmO3qkXuyH1Gnqj7tu61kTfLmHqrCQ-2MIy7A7xqW2V81NG_ujknU7y8LlBUmPZnbgy4WcTJ1rJhhgUnmphCeapRCvBOuGYvu1ijhstDZqy2a1DBqRcP9q50WmgQKRkIFbUQFaq6BdhdPBbWQbv9KHwhSaSeJnJu0MKwt9ywxxs_CjqOwelCsr3IhrxIJ3a-bcvNdwjNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جایگاه لیگ‌ های آسیایی از نگاه Opta Power Rankings؛لیگ‌برتر جام خلیج فارس ایران در رتبه پنجم قاره آسیا و 61 ام جهان قرار گرفت.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26607" target="_blank">📅 14:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26606">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_P8uRAurcet2llC_ADoy77ec9bHbjpriZeuy73WoxjSsq_aoyTaD94VA3Byt5uGP7QNwlzgPy8IfzD3WoeosDJotlw2Bh27l7ZsQ5SorStPpVnOFAui_8AeC9RzevxjZoQdW3iXxiTs9ZJopP9AUtvLwoFX5jCnfwrDOWJaTj1yEWqAAoqdOm7FyvynvAES1M4ne7Nr5Z_LH5E6HNBGTLO9xjBx6OW4QqEl6JS1ilinxm8b97moa8MiMBrV_GmIak2wURHKKyYo14WDcpBL7QZ057AbNlrCyjn2KkktopZSxpHomEY_783S9hs9D54MhYhLdCaODjZHJU1mkzSR2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌شنیده‌های‌پرشیانا؛ باشگاه نساجی مازندران با هومن ربیع زاده مدافع‌میانی 27 ساله‌تیم شمس‌آذر به توافق رسیده و این بازیکن‌جانشین دانیال ایری در این‌تیم خواهد شد. جالبه‌بدونید که ربیع زاده با اینکه مدافع آخره پارسال در لیگ برتر شش گل زده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26606" target="_blank">📅 13:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26605">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbxUcbHaYmqMq9w9rNRO2I-kn-RzINkHJmsyoa8SrAQvphfW2XcM1l6uR9ypfn-9gyVkF9cLfUJ9sz9ZHtUSwH9agWatRRcWf00ULa-vewlyx1WF37KssAuaJg9dtfla9IxXngukxY47t7of_zCDDxu_QZKfrQexxyBYy-rQumF3vVNFPznBB80x1XfRneIs4M4G1sIFlpdqVfHKQ0UIiliL1Y3fkmXb6MGMCQ0m6S4tP8bHi59NLeJH0Y9tqNJmXfHfdExPcB-3fuPMVNyE3495p4wPl5tyMS-xcMcwJygjzgtdgSLEiyXsi_20H3TEjwhYEfgjWoEIy3bCB-6csQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🟠
فوتبال ایران فوق العاده‌ست
؛ داوود نوشی صوفیانی پری روز رفت باشگاه مس شهر بانک پیش پرداختی گرفت و رونمایی شد. دیشب پول رو پس داد و امروز با ذوب آهن اصفهان تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26605" target="_blank">📅 13:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26604">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jyDk6i6YrrQMddNMqxAVjZfWa-GgrplZTb3JYiNX6q4xFaRrMiXKpueyu8GcYKvl3OroGeRn87nVhq47N9s69msMJ2eOWdEHU_eJmmRZWsCahI_xLam6kfrdkoyFgHED4O-CxnaITEDU53wRvfMuIb3o4QzMZS0i91Hievv5Uf1Z9Uhjyoro_6SShKmlMIScaT0msaObPKmJZ-mbcWQdENy1ZmP52TtxGuDZp1HCH8CjV1n8i3tPjROIuZ2dV5bvHWMMURErCmzuL83F62zQhURKpNJqlag0fvwFuNCo-o7MZvxYnTd1pTanRFFgU4CP91siuz8H5mU4LMrEK4GCFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌گفته وکیل‌ایتالیایی‌باشگاه استقلال؛ ظرف امروز و فردا دادگاه‌عالی‌ورزش CAS رای نهایی خود رادرباره پنجره‌آبی‌پوشان‌خواهدداد. یا پنجره رو بازی میکنه یا بسته میمونه تا نقل‌وانتقالات زمستون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26604" target="_blank">📅 13:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26603">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0cb160c99.mp4?token=T1b2Z20ZkeBkLZdfi0Uh-tRsm1KdgDRbVIqkifgK9PS-n3Ykjn9NukkULfmLJ_DsNgclYPDXABXdExueaceNC3MRWEkU1CJLufkd9VKKnCz_o0Xoiw-R5RF8Yh49y7hfhMPTAjx0Mv1U5SAC_tJJezoEvd0znrNPlm9XEvvCHFHk4TDhM0vhjL0jbUM9eK7jSE1fiPiK4pSoQ_LsTTd7gXQlnkiidCqfakQnozI4XiKk187xJ1EJi3cY0maY092eN4yigbGUqsaBsPu2RGAg9F5tS2K7CRCyncmr0wJ8VrNm3OaUH8uF4W57MxHRx2lVpr4xHSTr9QuMDo2OmYbg6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0cb160c99.mp4?token=T1b2Z20ZkeBkLZdfi0Uh-tRsm1KdgDRbVIqkifgK9PS-n3Ykjn9NukkULfmLJ_DsNgclYPDXABXdExueaceNC3MRWEkU1CJLufkd9VKKnCz_o0Xoiw-R5RF8Yh49y7hfhMPTAjx0Mv1U5SAC_tJJezoEvd0znrNPlm9XEvvCHFHk4TDhM0vhjL0jbUM9eK7jSE1fiPiK4pSoQ_LsTTd7gXQlnkiidCqfakQnozI4XiKk187xJ1EJi3cY0maY092eN4yigbGUqsaBsPu2RGAg9F5tS2K7CRCyncmr0wJ8VrNm3OaUH8uF4W57MxHRx2lVpr4xHSTr9QuMDo2OmYbg6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علاقه بسیار شدید غزاله اکرمی بازیگر سینما و تلویزیون به مهاجم سابق استقلال: غلامرضا عنایتی ستاره سابق استقلال کراش دوران نوجوانی‌ام بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26603" target="_blank">📅 12:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26602">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ciq3W64Af3R96zkiu-xRNok1qGAz5nrSZjnBJSm_zsFQCLYLyh7aGqE98HweXzCY5JRGbEUo0GbavUYeC1N9GiAevHz3laEDRD4L4t03MppFJfpsv7za9xpVASr5L9ygqeuGmY5YTZ4U-3Amsbi555Qe33hmndFi_Y5kiH7Z2SSslg4vt9d1CVFRPqaMkDPVPiiWjBdegV3_8Ak43h4Qe-sBy3mK9GT7B6Qkr3UfzssMUeE0-nH9BVjQ1n3npmZ1py-112l7Q7MYBeszFlKvlKeRUJWRcEPflaH5hZrRNvIQvlUaFl0Gp7fcphRomCKJzMCKE5Cj8vlpTVRO73Rj0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ویدیویی‌خاطره‌ای‌انگیز ازسوپرگل‌های لئو مسی از روی ضربات ایستگاهی در دوران حضور در بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26602" target="_blank">📅 12:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26601">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWIWOvc6sS_tyAORvWxHFXk9cTiACewi3GKTbmzUPG6_Ttz-UhkMXpW4Hx8sFoVYXTGGbqKNZEuDumd5KDwu0Xyd1uCSu8ZXIQ50v1wiRmyif_H2HYn6hOskdI04uv-3alhmF_XOshBhPk7DQEnQNgRrI0gvARtN1abHPuPS1QVwN7VVxH0DN2zAta6dzYbIWvdzI8yULLON7c9EGzNlQOML5A626l_hr4ov7-BPN_Nf4RBLL_QLstNjxta1FkbD7QiPPXao3y38SPaC3msFD47S2ICixJZgs5nEAUrHCq5AX_WWqu1CwRaWi_QRa5yrwPmlWyDVt_uBrzuTmsabEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛باشگاه استقلال باردیگر به منیر الحدادی فوق‌ستاره سابق خود تماس گرفته و به او اطمینان خاطر داده که بهترین شرایط برای او و خانواده‌اش در تهران فراهم خواهند کرد و هیچ مشکلی برای او خانواده اش پیش نخواهد آمد‌. بایستی صبر کرد و دید منیر…</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26601" target="_blank">📅 12:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26600">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OX0e3CFEkAD2sPP8dC7jpVhMNmTc91gvc_LEgWb90ddfVzYa724M1p76cJ3KacWF8dODcrPKsvWfahw-z1s94Gin3GJGgtdh6fA1XvGqp9JOnjhW9ujpsszVhenR3dGLk4B4myFZdt4LBQtUWcgHMGWbDvWYRvSyJ4Fu3685cz1UsB4tZirIvg03NMmxHMt9sENWTFGXnm3PTm1Lv-td7ltB7ZRrJ00MJNRL-B8En5mUAkq8H1odrcMIFetJWWkiJ7YDs99TJmp3mj5WGR0AbIM7NpZHAlTA7oeNJmTPOuolOmvBZk8TWkHaqFmR0ATKf93SR9-lSJni_yYu5Cz8UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رئیس جمهور چک در اقدامی جالب و در حمایت ازتمام عکاسان به عکاسی مسابقات فرمول یک رفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26600" target="_blank">📅 12:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26599">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AanUVBFQ0qZxU9fpuYKiXvYkJGgc-R1-2eWh1JtUfYYdftpW7Upx9-b0m8oNyGOnJJl_utbK1YfD0oRP6cUZhBokq99GkrT5yd4CdLbGKXaHNxPUU0gFft_UDqi5MlK5TSydidM93FvLi8MSgI6KyvYqL95uZge-VJi2iIl8Byen8a_LsxXZIBBb9pyVn9o1j_ELWpUYxEleIRYkcFmRPRCDgwrgf7gvgJEhQy4DQR7rZQ_niznq0AoaYB-W-2kob_G3z4RZ3EQ5DdDFk51KrP9EiEjEYVzmHvsw0M-kNXaXYW56_czRePRfbCMIJVVSWzklW4V70Ts6zsGwa3LiMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باشگاه پرسپولیس صبح امروز به درخواست مهدی تارتار؛ باارسال‌نامه‌ای رسمی به باشگاه تراکتور خواستار جذب صادق محرمی مدافع پرشورها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26599" target="_blank">📅 12:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26597">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2x9gJsuGtiwQg-Yaqju9ANz2EE1FSeJsI9WhKeetwprSyxUl0dkz57bQDWgJ3JnZmc24Qb7Tl_inNQcYWGjSA1xLdiwCKEDRvWNTx8jK2lvsvkvxCEUfm-CqoqO9zKlizs-TH90P9HfPjNPCi6OfZ2NUyw23sxXZNB16fVsHa6I4e-kD5cezEYziPRaX4tbAfME3cpWvfXJPWlRC8i3I6ujhQVd4LphiOauY3bK_BwYV1j601PoSPiSVHHN6-eIojjpN1pnEloThodZeELP9MVKsjBZcuo78pQ__k6mpAwhmeMq0jagZn3fkMRrIVU1gUEPr8_tRYAyG9mMiDju2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه‌گاتزتامدعی‌شده که آندره‌آ پیرلو درگیر یک پرونده شرط‌بندی درروسیه‌شده و به احتمال فراوان فدراسیون فوتبال ایتالیا قید توافق با او رو میزنه و روبرتو مانچینی پرافتخار سرمربی آتزوزی میشود.
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26597" target="_blank">📅 12:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26596">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a36a095cf.mp4?token=cLm0IeLZ9Fp25TYKz36Jdlov3LddtQDnH1ApCQPNFUXiWV2XmOFUcMowpgCvpfnfswkemuFFdOEeUjowRtPWM5RurDrP1NKWR1Yaoy-AbQcleyEr_BP8H0gsqCrYTH3pYqWAy2y-33OMnVU6PEG1D4TtVWt2ve9CwTTtezZ1FuSiP-GWthLqkincHXbl7ZNV-aDw_fU-_1a70zVc8d-Ka41pYFYT3xAOo2IB3nhUVoJEYAg0evRf6-EzPEawpl1hvyQQeSFgnhVWJ8FpaGoJ-KnshuxlZJhjY5LeYswrJTwwFRDVzudo5UkDDVCrWIizrdK5-0rCFTZhDf0zFNSVaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a36a095cf.mp4?token=cLm0IeLZ9Fp25TYKz36Jdlov3LddtQDnH1ApCQPNFUXiWV2XmOFUcMowpgCvpfnfswkemuFFdOEeUjowRtPWM5RurDrP1NKWR1Yaoy-AbQcleyEr_BP8H0gsqCrYTH3pYqWAy2y-33OMnVU6PEG1D4TtVWt2ve9CwTTtezZ1FuSiP-GWthLqkincHXbl7ZNV-aDw_fU-_1a70zVc8d-Ka41pYFYT3xAOo2IB3nhUVoJEYAg0evRf6-EzPEawpl1hvyQQeSFgnhVWJ8FpaGoJ-KnshuxlZJhjY5LeYswrJTwwFRDVzudo5UkDDVCrWIizrdK5-0rCFTZhDf0zFNSVaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی از تمام‌کنندگی محشر لوئیز سوارز فوق ستاره سابق بارسا؛ یکی از بهترین مهاجم‌های تاریخ‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26596" target="_blank">📅 11:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26595">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZj4jK4TpzpQjxm0tNgGBcjGGhk2W5w8ycByY93NacUczOBryO-6feqnVF869uJwXH07NTw53vf07lhV2N6IXFLN6WbQW4hcKWF3C4XXsAEo2Nk0rdeHuW4bKgNF3wKeyQWoDnZb2iKfMXB9BPvMTU6TplaheTkPxn7F1e043FtMP1D-l_8KLEeahraQhE1fK8HfI1XkE2P2uDc1PjWAuOjaZAN_yf0dw-2pf9MlnJPyVf97pFAsuan1H7ojuyWZPs4RGicjf_-VsrAexOhlQmqAR_4N0ybH4ipzHa3Ltg6rgwWz73dgr8M-CVRagx6snWRKph6DkgemApzgikH7Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رودری اگه به رئال‌مادریدبپیونده؛ احوال‌پرسش با وینیسیوس جونیور در اولین جلسه تمرینی این تیم:
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26595" target="_blank">📅 11:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26594">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CbcDmkzei5PZRpFBQwKDiF6LJT_XWfsFQNae-6Kf3LaMtmnP1Ccru45quyj0h8tTKBIKvITIzuCURqqk9ijlq7AL_D80FH2ce8UH3mIgYPpzCGcBIW4_v-klmkOtCYh0bgc7IYXhWHyN03mpOiAORg4HJW-Tk1aPRR1SX0P_rBxa_D699HMtmMkplrM-qzUQL7fav1vB04c0SOjArOkPMZskjjiiY8ck1vzEAAf7TkN_MZjgVl838PiI5x3PSqCUsnyT6Vi-n9uvNtaz25wJTaHQAMS8qiabyrO5v8TDcp8AxGRd86LLeZL_cU-gnXKEWEIZCK3QXrDzk13WrcNDUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باشگاه پرسپولیس صبح امروز به درخواست مهدی تارتار؛ باارسال‌نامه‌ای رسمی به باشگاه تراکتور خواستار جذب صادق محرمی مدافع پرشورها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26594" target="_blank">📅 10:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26593">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DnUned-hjPhoGCCZFnr6GC_2NxbUlBEq7PuPcAQo3h6y81eTgVnW66bTdrOi2U7QAx_pABLADRFQX1XFQVRb1UU8fnOMH8rSED3nV41TEU8Lq0NYWeMwCpcu1rwPJdBy5bffAv-s1KWmyYnqT2RsWsMHu9JSPKCqDezbGHI5bxbSdZ8Yptn5d31P_GXK8YH4QeKQjitXEng8R0dHjW0ZFB8p8qqtZXH6k4184O5PNC077LZ-sWSqY4QsIvFF7kiRSFF-rcPQZgqR58yLiccf5gME-9olz5UWJrV7OKM2Yw9crwFEi-niUDqfAFN3SOFyg59wu5S_--Qz4eBCLmkkzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ دقایقی قبل سیدمهدی رحمتی شخصا با محمدرضا اخباری دروازه بان فصل‌قبل سپاهان تماس گرفته و از او خواسته به گل گهر برود و قید حضور در تیم پرسپولیس رو بزند. قرار بود امشب محمدرضا اخباری پرسپولیسی شود ولی به احتمال زیاد راهی گل گهر سیرجان…</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26593" target="_blank">📅 10:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26592">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfju_1UO968yBngSJ2nyuHh9-OLIqx3oaFC6ccAiByffxV4w1LxnZQmWAStmEynn-A6p3VDj9GkZ3MJyYUy5LrVWEoGSmG9DAwIPZ1vcDnJII6k4Ru6_O0Q2yB8L0nVzDP8leqesgW6iyubKeh1PKi7bTGymC5mQIyBICZdfzi2vr5UHYOxZPdEdlBr8KuRBE2X8AGQqkcWi_XI_XkeoaxRgb52fCgfjbyduMndvRb6IWQAK7tYeHU7bEyaKa9da5D-6bDwNvP2NYMPJ7uPWFkTP_vR821FbuO9P8SJ1PcqOECFTqMM7jwA8Gra2yI-8wbBDuVVGaVjkRzNhEtpQoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
چیواله وکیل ایتالیایی‌باشگاه استقلال: روز دوشنبه یا سه‌شنبه هفته‌آینده دادگاه عالی ورزش رای نهایی‌خود را درباره پرونده‌باشگاه‌استقلال میدهد. ما مستندات رو کامل‌به‌فیفا و CAS ارائه‌کردیم و بسیار امیدوار هستیم که پنجره باشگاه استقلال باز شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26592" target="_blank">📅 10:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26591">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FgTHOKH3ptf2Nig26LOpI0yKcspkwrYpC_zmg2yX5a_IXEeuS7fhJ5hYAfaUcqizShjpfUip8eTix4RN6o2neqYPDHfs1E3R03jgix-9QdWVGpWhmK_OiCWOdEaYwt9MMrB7eSVAnCG5nxUa8hRJpJ6nOCWjOFzjIOBOZ5gtV8YWT4Jc2rey0-eIiRVh625sVojBhGm6AD3b4n8yCIm1dZ5_tzc8VmxUs9KZ-lgzbdIYWBOthZaQvjySmUzmzgLxgiFfQh05-prqFFsdMz281fpqJ_LZ26WxaxKi4xgvQxb-MZvq-2tbh2nOGmxc_ZS34b89ZLSmSa2npPF-BUwVsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#نقل‌وانتقالات|باشگاه آث‌میلان با پرداخت 50 میلیون‌یورو به‌PSGگونزالو راموس مهاجم 25 ساله این تیم رو به خدمت گرفت. قرارداد ستاره پرتغالی باروسونری تا سال 2031 اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26591" target="_blank">📅 10:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26590">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAEot4BYGUAaEbnLBjsPA_bLX9YVBLou3oPhO-c_hui4ROKQ_0woanr6jDicfL9Hn4MXh2-qIcUeBA5QnM-sRkMPR_g15omLzv11xbm8RBlxEX_brOXsavVy3-8MiZGPYaCpp2DgcXo_L4DgY_g_kB4Ztizwzu3VxsDiyvkL_yL8d-40ST3HszRdgx6eadv043axWHt_kcgWCPzwhel9iVEu2ayza-6ez-iBLWPEufPkC_1F9GfEiYNCJ3LYNl8j-PbRkiDfOuaiMmZ0NlV2lViUNuvgNB4KhnIJH9toAdBudi9g1DU4JE8DUpIhSx46SjA0VEBZfF-YuyzpKlrE5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26590" target="_blank">📅 09:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26589">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKHJcz6zH8-fVszVal2S9NLJFxqaQ2eUSDNm6Vj7cqwmXoBwWHY67DfgHItZ-xtc_J2nx2Ohom8fttZ3SVflFHhm6P4QnaiT3-pqIsl9OTq_5QT4IQOJA2HpFkognu0330feIdSA4_3gdaUIEvIQD_MppPJ-CI2gO9ooW-XtCM7nyvAe8QofPE58ClsZllA5FlkLwMB66rTdz0Fc6d2Yv4V1qDfFt4bjGdo_VNfY8QrIIA_3dWDvyL6UrYTGKEArarWaZHeHUk8rVlV_JJi_miw5kJ7kneXLKt0QwNHE7dUYzPB6EQyFZo3AQoix4JS4snGOrKtojuG_fwBciL3uow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرام جوینده در ادامه‌ مصاحبه‌اش گفته که سپهر حیدری تو روابط‌جنسی کم‌کاری کرده و اونجوری که من میخواستم هیچوقت نتونسته من رو ارضا کنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26589" target="_blank">📅 09:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26588">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c7b549a0c.mp4?token=Bp5zTtdHaqabbCtjKnC5q4K8MxPTnEn1ZJPwxakR7-E_6k8fuSPwV3Jopa6P1ZjIIWg1gSksqhblJoyTEtfZZzFmiHOhGJfSsyapz4CkwpVQBjxAz1bC4KeUVVT6NProLF3rQhezy7rtRg61HviCnWHB6ROI9E-DthXoad8DuWndhHtxZzxFAYveykY1Se79KeS2nlnXDxTad2OQ7ZwAB-mvKn0SuNDjlghaI1YjqlGUQcvU5l3793jKUCfJpIaqAlVtN1LKl8PKHKu0F6_nld7e29zEXBj5n6TqzQSWZwsiiD4wVHTKYln4E9eMDW72XAfYVgAQIZuFuJ2Kg16edg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c7b549a0c.mp4?token=Bp5zTtdHaqabbCtjKnC5q4K8MxPTnEn1ZJPwxakR7-E_6k8fuSPwV3Jopa6P1ZjIIWg1gSksqhblJoyTEtfZZzFmiHOhGJfSsyapz4CkwpVQBjxAz1bC4KeUVVT6NProLF3rQhezy7rtRg61HviCnWHB6ROI9E-DthXoad8DuWndhHtxZzxFAYveykY1Se79KeS2nlnXDxTad2OQ7ZwAB-mvKn0SuNDjlghaI1YjqlGUQcvU5l3793jKUCfJpIaqAlVtN1LKl8PKHKu0F6_nld7e29zEXBj5n6TqzQSWZwsiiD4wVHTKYln4E9eMDW72XAfYVgAQIZuFuJ2Kg16edg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇪🇸
🇧🇷
خوزه فلیکس دیاز: باشگاه رئال مادرید برای فروش وینیسیوس جونیور ستاره برزیلی خود رقمی بین 160 الی 200 میلیون یورو میخواهد.
‼️
آرسنال آمادس تاحقوق‌هفتگی بیش از 450 هزار پوند به وینی بده که در تاریخ این تیم بی‌سابقه‌ست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26588" target="_blank">📅 09:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26587">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLJuzLo0QXkcqa8jPw1MVOJtnInh9vbUod3c_YZiigE9GAV-Zj-L0MPFb1eyyczmeNxiW-agYbH_mf2DHnGC6kivmdHxNDcGivI9YBBURHNy9UrJX7Zgn1-IzX6atyJdK9dKEHqzjm2a21tk8xeuGL3cSMPcMiTzjicKQGpySR4G1RouzY7UmsQjWuWs3nAYxRr40wxGXiEPsSvdVOrCkHhrMWIkBUe0hbKszMOi3JdzlSVb4nupOgI2TepBxXuc7ACP4thrwfAXSndNt0L9eZWDabjd6UEEj6UQdj4CuUxiOeD2umkhCS4teZVeSlCCLZAoZ1Sg8bk0xfvV0IqZOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه جالب عملکرد رامین رضاییان و یکی از مدعیان توپ طلا درکنار کین و دمبله در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26587" target="_blank">📅 09:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26585">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a_1GbvNwxim8zPxptN1VPlQsOPdMVobwkYnbS4Mkh9F6dYcklMg7whQQddLWcJmo2H5FhIAY-hAQ8LRkYn30iv7Mhn9i5QjAmIXJrdDHhn-bG2U4QlDFYA7FUMPOq1XPGLtriGvLsCEKTtAl6ew_cH-Vxu0PZ5QMcAu1lRaYflKhXklcAqScibw7Blv37aw5_ZiL3foiw9E2s6lQpn0Jen2Iselh4fPOgVys0e3MgHx_YXu-FrmIXYqsk3N5_NApbFpSfBIh7mhERWvwNd0CVE7Kquoaww-VVfDQwHIWLLfkqGWtHR5VHV5wXXfCwkCS9k7Wgmnd6k76T4ot6RaD0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f3jXLjlLI8c7Jezfq9uI2O8M8KfByntf6XAPEID3VbqjCLrow6bVgw77uvtdkoYCsU5atwMDMzjIcdYgSgc8TgcynUK11uVM7TQrbnL-GwjWqgv3apKU4GxA7z30poi863gjBhveCQC2h5G8g3VIAa3M1K851NzzopKBh_qmw3aZ6JWHpd_T6__6-q9hs5NN88GOoWSXU9UTcUr-_F0oN0kdhgvjh2zXjjd5MWUPX86X2eF6f8Tny5yEja4dkX8j7ukol7TaY-z3j1zuf0aWTqTbi9wcgpMc-Sc98yMzx1EXiRRl3gSKyHofh3tp_igI1sEPfyC6yZ8n7Im3PyRPcw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
آقای دیومانده بازیکن جدید رئال‌ مادرید هم مثل عثمان دمبله قبلا یه مصاحبه اسیدی کرده: الگوی من رونالدو عه؛ خبرنگار: مسی یا رونالدو؟ قطعا مسی!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26585" target="_blank">📅 08:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26584">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SAnOhKN1F3150ad10K99eSaGyjAq6N-0B2Fao15BGhO0Duu_w_DKao6cfj0x9OWvkVYLFWo9O1uDGPXr7v2H1XVj_szhsLGqWY3hi1-IpQbaPUbturBgau3sU4V1gpHDZVx2SeKbYX44JaHO6fMjPf9mRo7wEVOWPMIo0nKkwhKy5VTjcrmfzDltSN8AhxGKZZvO1GzjFNXaiqFDiYrNDjELgNpDVsOFtSdAcWSaIo3BhuGXxn4aHBY3l7qtL6Oi-oLgjknpRuX5OYlBIBW7pIYEGhc73588F2-wEh5yGxy9gpXuWVa-JWNz12S1wgZ7q_a4ZxfToSSdBYfpYGitfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه نساجی دقایقی قبل رسما بر سررقم رضایت نامه دانیال ایری با باشگاه پرسپولیس به توافق نهایی رسید و به‌زودی رضایت‌نامه این‌بازیکن رو صادر خواهد کرد و باشگاه پرسپولیس پوستر ایری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26584" target="_blank">📅 00:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26583">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_EkuSYlmBcM7pqwZ9_89UgO_AhaMD_vPULe__6yQWUBUdG6DjZaiuXIWddoS9XhE6gjENRmn7yxxG1AV7gNJ1lhuou6GW4PsF-BuRqmHQhPoaBE4HDp_Y-NigLfYD67G0F1n9ncXcDOBoFjRTbLUfs1ccIkSZDH67VwMPAXfyw9X3wh034Aoy_h2YIHGwDRh9G-AhjgJ5Qa6WAN2pj9AwQ-uSti5FL31IF4VV2xIzEmVQWh2TBgxkXQxMIfxHFpMs1UJXtCJQd9tGFVafoqL0jCmPg09WyTv8iMdSVO9TbgOGq8hhw3J_X-hqrw5fvH2P1Ue5yJz8ak_-AP8jQQ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26583" target="_blank">📅 00:43 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
