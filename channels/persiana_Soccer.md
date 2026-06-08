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
<img src="https://cdn4.telesco.pe/file/UFZFuPpqtpqT17vPpDYcbvd4_m-jOuj-h8lHn3VLkjmDE2_LEzB9IvJYi5qsXUv_U9GbRilzhets7WB2rtCE3NwdMwYxnmFblglfyAUr0jJ3PBHY_Rm7wJBvaHJvweAMFUhVE3J6QxPp7M5rIfRwB-UhRFppFqGSVqWyu81tlyb5-l7aCBdpPF-nP7UyOZO6pAOteLFjD423rRiiELGcGN79GMAIiBNMnnhORec27RNHW-fgi2cSIz1e6Fjm6hkisI0zt80OwNmi8FOz52aQvBa-IH_SXOG-sKzke8VH2wjng-Yu7-VBAbhrscwKesoQONwExcgC6WXFNb3PyWiZxA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 171K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 09:59:14</div>
<hr>

<div class="tg-post" id="msg-22980">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABFqe0H-uFihG2HaTn2h9KSkStoaz-YIQORI2yTLezkaEhx8kyo2Ip8gqUPEDDPdEfjuH52C1ADBTZ2xXpo32IVzvNId2RrPENCDTYfSr0TkDfAOanSDh5l19A9XUvuXBjw782c5arQx9wXmtH1J2JTDXZ05y719QlVpMN-RLkT6HtUYisvpI0CykOqmEnBTZelZbOWZrBCyevqlqmALDoGY8qZ5RPsU8uiPkHtZ2-C4qUXRaB5wZCOARuTr03umSZIDq1HZxqv1ACwJwcN92gSqiyvwAVBW63Ffol9miGfxKo9kHB-61y4WtE4-kmnyesIxgD_q8VUprFGNu4TqKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌انتقالات
|موندو:
مارک‌کوکوریا به سران چلسی گفته که دراین‌تابستون‌میخواد از این تیم جدا شه. اولویت‌او بازگشت به بارساست. چلسی برای این انتقال حدود 50 میلیون یورو از بارسا میخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 907 · <a href="https://t.me/persiana_Soccer/22980" target="_blank">📅 09:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22979">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzAkWB1DsOlrW_k0KtqBK-AGZWFeDPsnapwCm4Oayl4U9loSg7LPYostj_PBFykrWEoRaG-DdKviOkmmvgJIp931TMC565A6UazmF99Ywz1sLNXiwNITFCByyg5Hnm1OXufve_OBN7x_0tJFROYvRQT5OZdXpaDvLsbr3fuxsO3BJxVqV-WBs5KtlEyKiXp_95oPUFx1yL4FnbEUhYv-D7Tk0tgZENh80s7U3JaoJw5gKf-c1CoTm0I_ordSISx0WTkE7ZLwTNFU51l_iYYb6Me_Uy_fEDwkH4NyyT9S-49cpylZnuLGx21vQzCu08t1vIqiSMHyKrSBY6Th3w7AnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تموم شبکه‌ های ماهواره ای مختلف که قراره رقابت‌های جام جهانی رو با کیفیت پوشش بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/persiana_Soccer/22979" target="_blank">📅 09:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22978">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UIE9vQmgE1qoW2rf85IcfpRiUndCYoGEWKPivsR2VDHq-gw1mUkuhjT4cKqc8kAXYVDU8oWrc2upECrAFYGPhorCxj1JF3ZZlL98DdKWm06BxAjIM9HsYDcQKZoZYRSGdS_ebokRiHdaJMhmt2Tj4Nzi-86PQ4CWK7i1jhrG6_20165boovtfIlZkvkEXKzmiBW7W_R0PLyv3WXLGYbVozb4AVDOIp7v_BwN45j3OA1kVR78MKNLC_44CVyZw49P1YIENrtqVNfyrGzZrhka00VZ7DfnSUqK5CefqfJC-Fndpo6VkmPm292Tp-G1GaYYvqeDmo-BbU3KNHxj9w1MwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/persiana_Soccer/22978" target="_blank">📅 02:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22977">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KaQCrrPK8s2Qbqv19fem8IUU6mEpdT0F27Cc8hi8AW-PNkZ1UF7JEzCjxls6Icje2Bhwx2QYvTNLTmfQA09pqMX3yy2UIUxmnVhN1PkpA6nFHds5AWKZwBDf4CuAek-SdOponpd9gqRnRFSD1mZ9_qs6CLc3qrp7mYuBBrkrll2vMXK2-aLGHZennjpK-8CzfrucPas6guM3O-OvLHp3hSTIRQuz8wWDuKi483c_ll30_vZfFdfSkul3KESfYq9TSVJ5vau755acbMEtnLvRDz7yEUEHxtAXorUkhNoeTQ_UPmcNtyNQOjrK0kNTyTlMdjD4iQcEKwbeNrEll1rDvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/persiana_Soccer/22977" target="_blank">📅 01:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22976">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epXM9Z743yxwr9HqDlH8gMkJb1hQppwcLqE6Jua8b7aFsSP_0xa0S5walrqQhlIqpDweROqPeQHtkLubQxbEQuy7VughmlxLdA4njIZmJjzNG11L2B6TUSaEgJF4HbTiuAAOi-qSpJLvqcTLmaJBLZp34k7SN2b1Jzb9eWJBeSkFC7_LHmsoijR-ib5LTS7Ycp2vt9W7F1bPoPdPj0RezIDPEVGQNdaJ0zGpgvCwagQ220vj8Vj5cUVLLS6_XY-XOMi1i9nqAZz4xvhrfimFp0EvX6PFGLMwaZM7UggBoUYKVb_oEBTn9b1AjFpGkych48omXVBcPvQFjEeBT2CZJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛پرسپولیسی‌های‌حاضر دراردوی تیم ملی از آریا یوسفی مدافع‌راست سپاهان خواسته‌ اند که برای فصل بعد راهی این تیم شود. یوسفی از پرسپولیس آفر قابل توجهی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/22976" target="_blank">📅 01:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22974">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CH4NGGtslGiOpVbFM2qU7guRchiWiL2u8gdLXj3hW__n3xUjKL2f4KoCqOmDo3hGmvQnezxCUFuH7hfVPFs-_O0PNyRfaF6quXNhqYE0FuQXFVPw4xrlxOqkd53fOBM3rOvWOEz-rQTookPzU9Fk5s8YJxv2PTyrXsBVgGrQ1YrQ6NrT2xWcXipWzkjEv7X8GyeCIX7wkqjtUsxjyszuS3iei3pjW--Cx_dLfB1yNVeY7NJY1eSRucn_IQuE2CF94eJRMlYo5d3WfwfoxNhNzXvOU211ejzpoAb-ofxkrSydPn_HwKozMfZxrWSqomtiCvA5DuNJ2j7dxAvfs9-8gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌دیدارهای‌‌‌امروز؛
از دوئل تدارکاتی شاگردان کومان و کاناوارو تا آخرین بازی فرانسوی‌ها پیش‌ از سفر به کشور آمریکا و جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/persiana_Soccer/22974" target="_blank">📅 01:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22973">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q88iFgAdV9f5DsmgSTXajP90NwILN8UwZIKSpATBC85s4LSfJ4JqxoX4tDiLBs91rd_Ld_rci2vsw0pvPal8omDxqdfpZ6HUNlwIjm8OCidzyHH5dTvNQIxSJ0ELTQSlGotq38v9HFhXTkfDpkUZhuJR4-aZHy0N3Q8o1K6O63D22lEme_qxcN0ilvhna8FWLf9h-L-z0rCDTdG05240DIva-2cDfiBUDh_i4RnQeaLxuepzX4qC3lNOYHFzsveeIFrBh0tNDaHa2gNJBkqO69hVZuE9WRm3eVpb2KSFYLKIZ1vs9-hQj70uH50lVNpSnLR22hqvjWRuBcmqfWIV7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌روزگذشته؛
از برد آرژانتینی‌ها در شب‌‌استراحت‌مسی‌تاتساوی درجدال نروژ و مراکش
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/22973" target="_blank">📅 01:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22972">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tt2u4z1-X-5hY1Mo4E3orj8DoQRxsUWX6aYBDhH_QqA-tNm-h_mZCsQJXfzxOmqeVH8tEYXVg0FIjigdN3WggW1hsB6g5-qDk0ix1yhGA6-spaRz5xZQstgTIuXTLcVc8aFSxqdEK5V11HS8v_VhBcVDAMB7DTs6rryI5Dn_7AeyoJmm-3cr5l5haqgiA3m6CiuNRtyddZ1IpPvwApCkwQSO2Jpwu_gbQE60dEUJU51MuJjJDflBzbpvgbMeD2PWoNxNhTvcwAeI5fNryfvxB1wbHNHKB2zcOko4QZMzkTH5ORIvLPtYmnE-nx3nPHJsi9dXcBvPzC5Gx-uxcPB6bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوشش‌کامل‌اخبار جنگ در کانال مردمی مجله 21؛ نمیدونم چرا سرنوشت ماها اینجوریه. انگار نباید آب خوش از گلومون پایین بره. امیدواریم که حداقل نت‌ ها باز قطع نشه که هم اخبار داغ نقل و انتقالات تیما رو بزاریم و هم برای جام جهانی دور هم باشیم بازی هارو پوشش بدیم…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/22972" target="_blank">📅 01:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22971">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4a6fa71d1.mp4?token=AcGdokDVD2PuhbhPzJ0dQX1057Z0a2HDZmeogSLYmw-gbnXdbFbbyHOSDSDKqcfhULXgGT3iHHyCmHon2qSBtw1EmCMH05UTzhG41QqC6sOOwyfYkPp7TL7ZACUbvL_Z6k26ySkpPAoDAblqLYirvql4g-P9ynpsFZt7BXv9e2_85acec4MgMIs0v8E47oWlrMPTtb6X7GVZIUrCFl5pXAFwLoVFu5UY_XF_Jue6lVfviJgN-B_Ac_0K_XENUoUdACt89KyR6TGd34unmdZNakGftxmsY4Zj8QoG40V5GTOPW3IFqSEC_MmQibkBr9E8OWSXYeBazT-gMUCaxr0lQqnQ0p3l-3Z5KhzYJDOzAc2j66jePH_c79EsjwzaACv7uwLa1OBLAIh3a2255pQRu2pYYowwDtvpuSoJauc8PXn_-GIjPzp7AKGlauN-6i3hHTH8t_G7bFqnAJQji-ri2JvlH2rGBdVlnGSctNfsgAWsmhq6B24oGPEm-eQhox3Ykp6jYHZ6Smm4g_Fpe_X4ccUlmjIHOAChLeQDiduPhQ2lO9K2ujuUXCs11XYhLc7pTMoPAdcKs6X4GCK-IO65AcSEoHper-a1FroPAR0_nw7v610_MKpKs7ioM3m3WjHWIqnmV2nTw5O0j7cNl2YnY3Vmnl7USAk8UF382yvKH1c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4a6fa71d1.mp4?token=AcGdokDVD2PuhbhPzJ0dQX1057Z0a2HDZmeogSLYmw-gbnXdbFbbyHOSDSDKqcfhULXgGT3iHHyCmHon2qSBtw1EmCMH05UTzhG41QqC6sOOwyfYkPp7TL7ZACUbvL_Z6k26ySkpPAoDAblqLYirvql4g-P9ynpsFZt7BXv9e2_85acec4MgMIs0v8E47oWlrMPTtb6X7GVZIUrCFl5pXAFwLoVFu5UY_XF_Jue6lVfviJgN-B_Ac_0K_XENUoUdACt89KyR6TGd34unmdZNakGftxmsY4Zj8QoG40V5GTOPW3IFqSEC_MmQibkBr9E8OWSXYeBazT-gMUCaxr0lQqnQ0p3l-3Z5KhzYJDOzAc2j66jePH_c79EsjwzaACv7uwLa1OBLAIh3a2255pQRu2pYYowwDtvpuSoJauc8PXn_-GIjPzp7AKGlauN-6i3hHTH8t_G7bFqnAJQji-ri2JvlH2rGBdVlnGSctNfsgAWsmhq6B24oGPEm-eQhox3Ykp6jYHZ6Smm4g_Fpe_X4ccUlmjIHOAChLeQDiduPhQ2lO9K2ujuUXCs11XYhLc7pTMoPAdcKs6X4GCK-IO65AcSEoHper-a1FroPAR0_nw7v610_MKpKs7ioM3m3WjHWIqnmV2nTw5O0j7cNl2YnY3Vmnl7USAk8UF382yvKH1c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از کواراتسخلیا و کول پالمر تا میتوما و فرمین لوپز؛ 30 غایب بزرگ جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/22971" target="_blank">📅 01:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22970">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32598b0bc1.mp4?token=jFW8rHNLU_UPoPrGVcNyGvangmKgEkxDvTnrCk48U3OKV_c47XvfESUmFstNTCSzBcyYR4_XjtYG5E6Ddl-ILkcOyPktw_C7H2fvAYhRtfVimbkqt8s-iYsoraQouG0uHy-cJcRV56QPJMCxa4kOtLO8kGpFbCsrZsJ4lN4Qb1QQywWQZ0PrXc95cs7xvyN7Bw2JkCMH0V9nB6BLV8Y8g4EUZsjwqIueFnf1Pe69BcIKPAPKu1NCBwesv8vn5QRz_KmYPy5uqixPJUkzJDAeESp6wOad8QtGfY76e4Km1IUb9ipiMrzP_kY47JwQftm8E1EDm1uN7sD23sC31M7O-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32598b0bc1.mp4?token=jFW8rHNLU_UPoPrGVcNyGvangmKgEkxDvTnrCk48U3OKV_c47XvfESUmFstNTCSzBcyYR4_XjtYG5E6Ddl-ILkcOyPktw_C7H2fvAYhRtfVimbkqt8s-iYsoraQouG0uHy-cJcRV56QPJMCxa4kOtLO8kGpFbCsrZsJ4lN4Qb1QQywWQZ0PrXc95cs7xvyN7Bw2JkCMH0V9nB6BLV8Y8g4EUZsjwqIueFnf1Pe69BcIKPAPKu1NCBwesv8vn5QRz_KmYPy5uqixPJUkzJDAeESp6wOad8QtGfY76e4Km1IUb9ipiMrzP_kY47JwQftm8E1EDm1uN7sD23sC31M7O-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ایکرکاسیاس گلراسبق رئال‌مادرید در مصاحبه با روماریو: «مسی خواب‌وخوراک‌رو ازم گرفته بود.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/persiana_Soccer/22970" target="_blank">📅 01:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22969">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0wRSkyturcpluakDmEZW8yTAnVpaJuyDlhtxk5XTjbHc4vYeFEXHuA2HVGvRKN56CUOPihu4wJYwzLnlCJ5VT_cA_f4jOn9tlgfNN0RbsDnx_Qn04LVgD0znJUXxv82uraJAq-nXHUkkWJD1GgIrewW3ptV5nz_v0inPtKPx2BGy6yYdcP7mUCbkqhMUloef4k270V6Zof6XRopF-ttENqZYTEHjhsJO60bie41ObtSbW6LZ4oGH8VuZ3GV5qVGkviKx00kBtZVTGLxj7P3CvT6w-siuRuXp5JF3Hr7YBFOwyQCd07s8JvfKwzbvsJC9giC4QZY7qtHZhdOS3qn_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
🚨
کد هدیه ثبت نام:
GG007
⚠️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت :
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/persiana_Soccer/22969" target="_blank">📅 01:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22968">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOPCxBX5qafRvlvFvRzL7sPiJyo4N54A-2SJtIpx2x-zMF5xeJruX96HnWtiFf_U3sjSTULHLJHZMvNj-Rz-ZsH2ohM-jgBtiabNUm_G0JVOoGxSczOI59j3GANvN4ZmU20ExkKbYmF6p-Dx2Rne1TZxkZrmEKLgM7jn9NT_mdQZZSMHKvbyfmwIb23ARejynYHBqrA-3DIVZErhAa-axECzrwNhoL19gPfuWeZHKbLCx65rLV4_WDBsQyH8XOyJTzkqaLH-z_uRl9nCHeJTrV3luTSUNzf-mw47fvAoKZG1vb5SFWbs4vSUMGj179n2ncYrnZI7iAfGnqqeIuYNvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای رسانه‌های روسیه‌ای: دو باشگاه ایرانی خواستار برای جذب کسری طاهری ستاره 20 ساله روبین کازان روسیه به این باشگاه نامه زده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/persiana_Soccer/22968" target="_blank">📅 00:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22967">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca6abec005.mp4?token=jHIgSgrA6F9-3Zqi0TyFisSG5orbcWYz5kcsrihc7OzncSIYr9BFnBr8Me2eH-Te1b1_ggwzNioajX7bXzfFOM8kq-6FjYAqG0EtEMN96DAi6YMJznNPlE1k2SCMGB9umiJBmeD6hA5GMO2rT7umlwk9D4VZhg2FvuDJppn0yOzTs2w0W5QVgEtsUfPWI9yH_LfUe4k80_Musd1QVQvE4iDwzmCUz8I2oC_e3LE84bKFAvktDyzvbJu1p8HBktAMhXcs2IZPMZaSc2avaXHNZBzEv9PwmJYRG8OENPHB3K5fXTUBaZAFnAPwzxUD9FMiDXHpd1NZK_Lh-hIeyrsdeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca6abec005.mp4?token=jHIgSgrA6F9-3Zqi0TyFisSG5orbcWYz5kcsrihc7OzncSIYr9BFnBr8Me2eH-Te1b1_ggwzNioajX7bXzfFOM8kq-6FjYAqG0EtEMN96DAi6YMJznNPlE1k2SCMGB9umiJBmeD6hA5GMO2rT7umlwk9D4VZhg2FvuDJppn0yOzTs2w0W5QVgEtsUfPWI9yH_LfUe4k80_Musd1QVQvE4iDwzmCUz8I2oC_e3LE84bKFAvktDyzvbJu1p8HBktAMhXcs2IZPMZaSc2avaXHNZBzEv9PwmJYRG8OENPHB3K5fXTUBaZAFnAPwzxUD9FMiDXHpd1NZK_Lh-hIeyrsdeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
🇵🇹
امسال مدعی ترین پرتغال رو پس از سال‌ ها در جام جهانی داریم اما جای یه نفر خیلی خالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/22967" target="_blank">📅 00:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22966">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8bUwpG07T2EG2NMPiq7HUABoNlDxWfRdhRi8jCWPpBeflRg_IqxqpX9BomlQh7p2Ke-0VrO3mMKLBnMUo0PJDTq_eBPNBzEYwLluiPyB77P8nH_J-QVnlwf94q7wcqPLv2YX2XrlqbzQHu2penFyH4GC7VgTCka0817w7ICBEp9uBAMRAoBHaGpUWpcrUEzn8Qerfu_CaHlZPksJtGgcF8gQ15dovp3hH4vLxcBDmX8bQYastY9BaUGgwvZr92EyQY9zwUBRAGshiEBIgAhxk6rKE6LtghYrerS-PwGkldzFVqUN31oH4Wa1eIM4I1gNqkZKe7YwOcJ2WNUJ4I6MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال خطاب به‌تیم‌های خارجی که خواهان به‌خدمت‌گرفتن امیر محمد رزاقی نیا هافبک 19 ساله این باشگاه هستند: 3 میلیون یورو پرداخت کنید رضایت نامه این بازیکن رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22966" target="_blank">📅 23:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22965">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGXoc-m_AoLPQ14aBAkM26QvQXEavkyGgs5MDQqRLUud-1tSwWo8hIjlEHOADpEVZsE9HBOvDjXLEI3NLdPkXxd4Qq1Kgiv88xZgmFzaP78xCoXy8wWMPwVEq998S8VYxH__2vZPGKcId0zUxHBTg8Dm0kGeCcNUIPDGebpYnsk-kiSV36rB5XBGxUlj5Kn_tR63bTUXX3P-Gs85aZYl5D3U97ObPzFimrqK5aC0hr2pj6DYn5pfNjxyUZXBfD_FLzBxERqymqCzFdO89VhiLjw_YdtL0ZRUtzefcxWT2XJEhDLIO-FNSAMapWpK52_nObuj5-xV-pFWM8Ikvwb7Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوشش‌کامل‌اخبار جنگ در کانال مردمی مجله 21؛ نمیدونم چرا سرنوشت ماها اینجوریه. انگار نباید آب خوش از گلومون پایین بره. امیدواریم که حداقل نت‌ ها باز قطع نشه که هم اخبار داغ نقل و انتقالات تیما رو بزاریم و هم برای جام جهانی دور هم باشیم بازی هارو پوشش بدیم…</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22965" target="_blank">📅 23:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22964">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eaff3256e.mp4?token=HMuF_LGFPmdc4-5yj_We-HFtjYXzuz-eYOM4NKKhlN_bQFtVh2A74q4G3Gp0ewFDP4m60mqfe5gtHe9aJgc0dO6G2WE5HSPJXM1P9Iop4nvauDOWOjrH7--cuFszpyigzdC5xIN9Rq5Sy7LvoB_bvxgPV5TU5k71_M6NUhHdbrRANWEMZVFSq7jNFnR3EfpkVuyIKccEvfXwnnkKgboU2YAfy2A1j-lbMkgyAgDC9ZqblIcaog3rg1hCTPY8kiEtnpznZrLGuyVkH2A1YszcGY-KkQt-n8nG_dBghAYw-V5Ef_x-XRDcAihy4ilcsVnHrv3nddwxKTP1oD-QHJmB6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eaff3256e.mp4?token=HMuF_LGFPmdc4-5yj_We-HFtjYXzuz-eYOM4NKKhlN_bQFtVh2A74q4G3Gp0ewFDP4m60mqfe5gtHe9aJgc0dO6G2WE5HSPJXM1P9Iop4nvauDOWOjrH7--cuFszpyigzdC5xIN9Rq5Sy7LvoB_bvxgPV5TU5k71_M6NUhHdbrRANWEMZVFSq7jNFnR3EfpkVuyIKccEvfXwnnkKgboU2YAfy2A1j-lbMkgyAgDC9ZqblIcaog3rg1hCTPY8kiEtnpznZrLGuyVkH2A1YszcGY-KkQt-n8nG_dBghAYw-V5Ef_x-XRDcAihy4ilcsVnHrv3nddwxKTP1oD-QHJmB6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22964" target="_blank">📅 23:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22963">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇮🇱
🚨
شمال اسرائیل آژیر ها روشن شد دوباره  موشک ها از تبریز و کرمانشاه ارسال شد</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22963" target="_blank">📅 23:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22962">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NxKUUOK0veXjaU-URZBCmCN2qsl-Kkqt25FbjtZE1hoB-GLVXSDpUgV1zfLTJeUpsCePXtUVxQLwgzo8MrYfdADaxlQdiQicY6AYakBTHuLVcnQF8Sk5BbzRZF3ZemhfswGnuubucQnG3A3FB84w2k3SHiYzc47PKgAue89TgGYU8isMGqgQUpT4ZiVugZ6wZSawgVFF8RKPR5rmrcZMgHUzHrYBH1z7J7nRgyydN1ZSCLm4RWjzQkxRP5DlWou9MTXJUhXku1lb9HVHrS2dlSycRfGEGXRw32w4-k3TGz5IOzso4HEf375nIg31Ls4IhgmKqtALOqkZj5fjMurirQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اتحادیه‌فوتبال دانمارک رسما اعلام کرد کریستین اریکسن هوشیاره و تحت شرایط خوبی قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22962" target="_blank">📅 22:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22961">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmMPa18yyZ3Uq1itibpjHMiIt48VcFZbB9LYD0dvcAltfE1RWERzoqCmHRsbqV_90hxJBsSIJ6MUbI1rtEN2X6U9sa-DQLxctjv4PCF9KpsAFFoDtbta3ZrRCwKR_Sq2XSFD6siVF8X3uNAhdEVS11x9u9QgQa9W2S87EwN9b5CRDTGZmuIr46YvCr5oXyzajJoZX9_6i_5yxun7xZ1s2qqgm_0cuz3gIDvtMnCjOhCWQC16EdmI94mlTsxozTztXOBnfvDEHmoIifa-WDhANGSvbQKb38f6ok5-eer2Rw9sjtJH9O2oXgENRXOc8J6KNaZ4OKOZYM5c-9MWf8a1EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ انریکه ریکلمه از پس پرز برنیامد؛ فلورنتینو پرز بااختلاف‌آرای بعنوان رئیس‌باشگاه رئال مادرید به مدت چهار سال دیگر رسما انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22961" target="_blank">📅 22:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22960">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uW5xHiADNCzQQJZvMe8Ie2Ffbs12QZ2h3qkfxjgshjIFejvJrJCCag1QHqNWgG4iTm92T9QgHwc2XULigigZFQQwmSTvVpuviyIyvs98RSm3e3kT8cPiWFa6_kyNvX1efZ0SVBgqNm34UAE8xUEIrU0SXxnBryHEHpeVrbUflyo68I_XzqV_ClA3IhiKfucmQKKymajexekBXYekGQbf-YFcUWrJkHq41gESQQkf_5g1_V5N4OY2UmylrDPcpD4ouK5l6MSNm3FSqTZiQzpRMDnc8lTWhM-2uakNqqJdqme-J2HER0D4yvcdxLnCDxXuJFEc3KXNdwiYEFI9mufRQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری
؛ شنیده‌میشود محمد عباس زاده مهاجم سابق پرسپولیس، فولاد، نساجی و تراکتور به دلیل مشکل قلبی از دنیای فوتبال خداحافظی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22960" target="_blank">📅 22:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22959">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j32RGU7pAzFhewz1alEYdHiSJqRPqPZ-ihV6kSMrwWszcENa-P3xEfQHcj4i7opAHwwa0iefQmAG-r1IY3IjRUY4dMXsLA053OEUlR3ZeL69RctcZnSwJx0lCpAtQtxl_V8B32D1KWIK8MdAQ60hZn-pP32eyTQKYWlO06J1BRMsdilQO38l5Lcw0M6EwdQL0ncjS1n87HMyCo0Mzc27HaOorjes0Qj4vWQeIpsTo9cjWmmTLkz_PtvQlOQ6hPBkc5_weM2ZsLHOkFMrDs1F5QWARCdLvO9ZLuUrbMU9PswtXk_zU1SFiN2SBcU2j4GFCxG-yuWEZHcpFK6p7RI6TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#فوری؛ کاپیتان‌دانمارکی‌ها بازهم سکته کرد؟!
‼️
دردقیقه64بازی‌دوستانه‌امشب‌دانمارک-اوکراین؛ کریستین اریکسن کاپیتان دانمارکی ها همچون یورو 2020 دوباره بیهوش شد و بازی نیمع تموم به پایام رسید؛ امیدواریم اتفاق حادی رخ نداده باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22959" target="_blank">📅 22:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22958">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bffa01c1d.mp4?token=pPPyzydwm8yWNg2uhDNL0xR9xgFgrqc8NEXNccridLAPP7AU9-9-OlfAJKwcYiO7whEnLxf1fFmcHIkb2g0L8DHTiZx5h9rD9IUZJCUBiD9eaDv48VT2U8-fydINkh3RwOXLYWyavTaLnM2ettwdvHPcK7gAnM1qWEdtjrtBLtsS08-9ln2Qe11mqEeJVlTjHZ73GbGkysEq962Z2IDPdcTjIk9BnutZNxe-XfRHZjRnlXW21JXj0nRYtRo6MDvB47qRllc0PsOuXFdUEUk67DD5QWttvzTcu794Eko0i6vLW_BpWdrA1NBatCyYu7t7tdk1OepF8XADiaARh2QCIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bffa01c1d.mp4?token=pPPyzydwm8yWNg2uhDNL0xR9xgFgrqc8NEXNccridLAPP7AU9-9-OlfAJKwcYiO7whEnLxf1fFmcHIkb2g0L8DHTiZx5h9rD9IUZJCUBiD9eaDv48VT2U8-fydINkh3RwOXLYWyavTaLnM2ettwdvHPcK7gAnM1qWEdtjrtBLtsS08-9ln2Qe11mqEeJVlTjHZ73GbGkysEq962Z2IDPdcTjIk9BnutZNxe-XfRHZjRnlXW21JXj0nRYtRo6MDvB47qRllc0PsOuXFdUEUk67DD5QWttvzTcu794Eko0i6vLW_BpWdrA1NBatCyYu7t7tdk1OepF8XADiaARh2QCIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
#فوری؛ کاپیتان‌دانمارکی‌ها بازهم سکته کرد؟!
‼️
دردقیقه64بازی‌دوستانه‌امشب‌دانمارک-اوکراین؛ کریستین اریکسن کاپیتان دانمارکی ها همچون یورو 2020 دوباره بیهوش شد و بازی نیمع تموم به پایام رسید؛ امیدواریم اتفاق حادی رخ نداده باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22958" target="_blank">📅 22:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22957">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HuFuZli9fjbryQPR1XTvAgaq-qm8fVsCmL4WeJprNrWPK3cJTLNrUny22f0rO79ca67q_QfKU0U-p84x_CDVywX36Xx-HAOepSnf7EOIpC7asnaNE9EDNzHCYPzSofOLNAGcA9w6X4XrKnxGaDaAKN6Ly4tcp6CpPlNueajR5CwsPuCb0cl3niuaxqBOCwbbFdSy5yn7zxMPEf6rI9N_hqhQtoAjWig4lkZn0AZWngpGWqS3cHn6O1vjyFVtnsr_C2XKCKMsVWeVsazv283jKsER9WtTYApAMwuriZMbJ32C9C8VOxOIF_ImBmj7Rm6_dBLyW57s1s33mSMuJ35jlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛ به‌احتمال فراوان آنتونیو آدان راهی لیگ امارات خواهدشد. او دو آفر از باشگاه‌ های اماراتی‌دریافت‌کرده.همانطور در روزهای‌قبل خبر دادیم جدایی آدان از استقلال قطعی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22957" target="_blank">📅 21:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22956">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b1b174faf.mp4?token=CEX-S0jo6nlNrQChqpoKUY4ICrj9nSN5Fns-jIVAMUnrcWNj71ovqj3bRsc6MzCEINvoyvWQ2WF5gVvSjl_OM91wGrEOj2FjlFJGYSAxYgLxjnidO3gHpzaBxR5158fKtfeReenKt4RKLn6bVqkQkVo2Q-tvGuF3NnjEx0PGdA0A_ShV2_yygAaRxV-LJIkbymzpBi-bY5hc60RAQqUMn1B3TDjhFwwUuHu5NiKsJRHFhSyMSBzFZoWyrepV5jxu4q2KJwKEF5niOi7TZHV3cbjI--vBr_wgxys7gloXvbVVlZ5_-HRge0howF5Bj6WO1HgbQPXqEHjj0-KcefQ7vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b1b174faf.mp4?token=CEX-S0jo6nlNrQChqpoKUY4ICrj9nSN5Fns-jIVAMUnrcWNj71ovqj3bRsc6MzCEINvoyvWQ2WF5gVvSjl_OM91wGrEOj2FjlFJGYSAxYgLxjnidO3gHpzaBxR5158fKtfeReenKt4RKLn6bVqkQkVo2Q-tvGuF3NnjEx0PGdA0A_ShV2_yygAaRxV-LJIkbymzpBi-bY5hc60RAQqUMn1B3TDjhFwwUuHu5NiKsJRHFhSyMSBzFZoWyrepV5jxu4q2KJwKEF5niOi7TZHV3cbjI--vBr_wgxys7gloXvbVVlZ5_-HRge0howF5Bj6WO1HgbQPXqEHjj0-KcefQ7vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
#فوری
؛ کاپیتان‌دانمارکی‌ها بازهم سکته کرد؟!
‼️
دردقیقه64بازی‌دوستانه‌امشب‌دانمارک-اوکراین؛ کریستین اریکسن کاپیتان دانمارکی ها همچون یورو 2020 دوباره بیهوش شد و بازی نیمع تموم به پایام رسید؛ امیدواریم اتفاق حادی رخ نداده باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22956" target="_blank">📅 21:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22955">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQmodqtEOyN3Dl7AiJlRQpDlAWBHasd5g-_0XAEh0kWil8Yi-NBbZt_BrrGbhLWGW-jXLLiVsJdUwLN5WpVBN-xApzpXPBeVR14tEHb8o4JNer4QiZXdeAA1A3FunajRmCEctQgMhVrv3KQcbgLzw1wTp5eSi6vn10JgNvpUNzwlCy0aupNfkH08T4JU7XHrvjYrw53A6BDjH36Ixp4_rQO275MupepFmmqjHtjFvaQDduSDpUNDVKfyiGeBWPe9fZmIHYZ19cpSh1JSRWH5LZNIoHjmzC5ij2Zgv_JQCU8qgsmyB_5O8BN5jZu5za-6fuj0GYPfW81A_18lpc9F4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#تکمیلی؛ کادناسر: بعیده که‌سرانPSG ویتینیا یا ژائو نوس رو با رقم 150 میلیون یورو بفروشند. برای هرکدوم از این دو نفر حداقل 200M€ میخواهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22955" target="_blank">📅 21:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22953">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LM9_E62DzvswS8k5xk_4riDE7M5_-V71lzM32t0GvjWhP2l2s6VSzg3-8IPq7-S5Q2J7l0CSxeO0ZlfNbaWjtSJYn7eWyE6zL8KUebEqHVtueOxQ2-dnK13CL44S6cGCqwrChTYqsNN9Syzg4nCPXucJStwWCwr3eWbmAtUaHfvtslb_wbGJ3S_D-ilq-OXafo0ZOz8ZN-eK8-CczK-8EWII8kKjtHYTVElYjU6Chzqxk8pCcnUi5dcK4Zu2vTj2Ak0ncBX7QDCXgliBJSVPZg07hepTBDmkMp-KtcL5g0e1_tugDXEN1fJ1QE_KjX4P5Wpk8sjaGNOeJAaPGPlJEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GTJ5WmtDVnBRsmuJgS58glpS6A1rPzbu-zxj0NnAvIOA_6_MkSwZ6HDdzr3kfnJeUsHsGqwsag0fey20G1rSPWhi1TwB9nOShSiyVOc5URVgtqS76wYsUTFvQoCA6z_DHSNekTFJo9lHwsoFiEADvg3ydyvnaaA78g0fwbU1-IHjxMtxOk5XHo7NC8SwLRntoEzB77V22WhIdQAvSjT2r9s5VYD1sbiDrhjnsCjUToRNPX5-H8iikxq666lGbEkDtejEw7qMbzbLLmZR8xcMW0MOqAsE6i4QyYkQHj1P8Yn_LVjwfbq8waZQitdZ5EgxaB2TnJ3FWJSzsVELdLVT3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ انریکه ریکلمه از پس پرز برنیامد؛ فلورنتینو پرز بااختلاف‌آرای بعنوان رئیس‌باشگاه رئال مادرید به مدت چهار سال دیگر رسما انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/22953" target="_blank">📅 21:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22952">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCIS2NnV1F1gju_WzWTMQ8dmZzOBl5qdFVRJ0QI4kjBAI_s5LORDpbO3fxtRnevLXxXCO29B3JbArsN4mfm0Q8lGnlEEVzz9TZJBqdjvRgf5rH-RQoQ9vGDbWPg4iyxqd0ZdWTU7Pl2EUzQraw_lm-J6QY8itteZrUVD4rpQpPVM6NbWUS2y-mZ-qRWDux7iECDEXaDZtDOV1XhjECJiJdKk2fVxGQAwIjX256jzoYr7oGztNRiGnL0DP4jkkdoa8_sOJ1i3-N7TPsePfNDuBnrU9rdPgFFoi3oDY-HHiWT5SbnFQLRw8Omb4Qy-pw4PbMwToOppxgDGxf_q9lRBAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
حواشی‌ دیدارآینده ایران
🆚
مصر در رقابت‌ های جام جهانی 2026 از نگاه هوش مصنوعی ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/22952" target="_blank">📅 21:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22951">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c25ae3aa7.mp4?token=cyzmWESdjdvtCtozeRJj8IpPAxkuEvrBiOQ0bbTpbbxsgOLmki9bFa5KW3XvglLz3l0NH9usmBDnF7n6DyRov2BvWw6H6QAYFzaZQjpjZmpmmUMVV2W04BGaDS-M4Evh-tuAJLyQuHo4Vg-saaJwsTWImlgxkzQIBT5VeSagwCbQRVOSgPPoNxzw3Q7tRMIGAmp1QduTO0ywv8CbcTSGI3vpjt8e73KyJKPBjlceIjEvMBnBUerbhYevEaMt1ErovrARKsYK7HmgddIJ6mySPjbCECzjOZDLfP6i3JYPPilFGqkoEt8bjH9Jk4BxG0kU08cio42kkPdVgr2Z3vTSYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c25ae3aa7.mp4?token=cyzmWESdjdvtCtozeRJj8IpPAxkuEvrBiOQ0bbTpbbxsgOLmki9bFa5KW3XvglLz3l0NH9usmBDnF7n6DyRov2BvWw6H6QAYFzaZQjpjZmpmmUMVV2W04BGaDS-M4Evh-tuAJLyQuHo4Vg-saaJwsTWImlgxkzQIBT5VeSagwCbQRVOSgPPoNxzw3Q7tRMIGAmp1QduTO0ywv8CbcTSGI3vpjt8e73KyJKPBjlceIjEvMBnBUerbhYevEaMt1ErovrARKsYK7HmgddIJ6mySPjbCECzjOZDLfP6i3JYPPilFGqkoEt8bjH9Jk4BxG0kU08cio42kkPdVgr2Z3vTSYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
تیکه‌های سنگین ابوطالب حسینی به تاج رئیس فدراسیون فوتبال درباره عدم صادر شدن ویزاش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22951" target="_blank">📅 20:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22950">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YsKf5fgX286fINTpSKVJnhoT-wz3E7-IVqtOXZIPfcYsaVVrUlZw6pmjR_cAAPxSsJX06q7yBnpPeadyo3PwsuHUZubzHtB4AIzKrDnmRTBJxhaUnSt0veyqgtqba6OxDi6VYqGEo2E_DxGFJNWheCtbaRovfajI6odPz49q_P0v-RjnzRF8lP35gM1oNm0VZykHM1MzJcEdVt0ZEyA7dbD_0DemIJQ4qjpAwOIYlj1UyGNrldsZnPKCJ8x_f3UppFbnOu8EfP2y4WQunxMmcfwmeGSqNWwyS9IngMdXWUkhV1WMwj_vNIAK_-JtB-QhRqFw6rfcHvqp45CcQQXtzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ سهراب بختیاری‌زاده سرمربی‌فعلی‌آبی‌پوشان موافقت خود را با پذیزفتن دستیاری دراگان اسکوچیچ درصورت عقد قرارداد با استقلال به علی تاجرنیا اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22950" target="_blank">📅 20:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22949">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wcg8NMXFZTL-gdB5smYCsDpbrgfqthThHBmLaAT8oKC6lVNxrYoonD8LGT2iItCPf-lGrNv5NzPhUPLLZPEg_mNtSUiVmAaDLR7k1Y9wN8WznD0ICYerYV4Ok6dZiqYSm4KDNn3UFoeSVcF7lnB6tfsDHwwVABFRUU8PVN4mOYTdg7bEeUM3_kB56b8Ei7b94giSEe2OH_eyij7RWE8QFJtqZrZmGuP7TUU6jnmyH1GXtmXi1E8hkIircIps-55IMSY27Np3L1ItKEy6IuyVcg6ThfWTmSnviInIq7u82XyUQssyrvChnQmnJGoIR5ax4yi-jaeJyKpaZ6zZA51xdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#فکت؛ اگه کریس رونالدو در جام جهانی 2026 موفق به گلزنی شود؛ به مسن ترین بازیکن تاریخ این رقابت ها تبدیل خواهد شد که گلزنی کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/22949" target="_blank">📅 19:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22948">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PKfmF1WVBWNk9elGaZbgT3hqENcsF6QLtzkkLx5BpTd-5l3PGGgSituD8P0bCocmlCpJl3QSshutfq9XDwewEkyvfHvM4CYxLgafK1RI791njEF_FARLAijSnhbVKstJy7x3TXjObnasEcAPo_iPrYWzxRwpSsRkt9HOZChwp8GY0C5uevMsSorB790zlcoHDc2gI5bdcXfpXXem9UmC6Kp7MorOZfuzdBjrpGJZ1WVHlmGaqJFbAp0rDX3uZOxI_kMCQBxYXNEoCH_SIoYwx2PpH09SOq3ruwZly5qIQ3zqDRhj8W66Emh2_zE9oKHeStplq5f2nj24LEQTIMAtQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ باشگاه روبین‌کازان‌روسیه به مدیر برنامه‌های کسری طاهری اعلام کرده هر باشگاهی که کسری طاهری رومیخواهد باید مبلغ یک میلیون دلار بعنوان رضایت‌ نامه به‌ باشگاه ما پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/22948" target="_blank">📅 19:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22947">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c78767e61.mp4?token=WOtwHFZ1oPIMnZ4JY3VsYGvg5pboyQGnK7XaLbncYSSQ6JYQEVL-lIQQqx2IeVWUf6L151W3Qf6UZ4z-7jmRGnQDRGPD_2RDkOLMVGVHR8v49dQ964IbX06ANQtMWqYz_67gmU5k_FAfGv-yUemf46Pus-SHtGtKlUJ-nSk4_wgqNSID_SXnMVMRZ3lxOPHxYqdJyxBKUR8sYx1prN9YUeefdUtknDTbtHvJjWB8lb7Jtap9Dw3CHHH4E21zgoNXnKJF4Sd2X2BBB35h82AzBXJ5eYEfrjxYf065xMZ7Sj13w020KQNUFu1RV5ZpA5MffrHEeXL6_vsL3l6RKKXbOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c78767e61.mp4?token=WOtwHFZ1oPIMnZ4JY3VsYGvg5pboyQGnK7XaLbncYSSQ6JYQEVL-lIQQqx2IeVWUf6L151W3Qf6UZ4z-7jmRGnQDRGPD_2RDkOLMVGVHR8v49dQ964IbX06ANQtMWqYz_67gmU5k_FAfGv-yUemf46Pus-SHtGtKlUJ-nSk4_wgqNSID_SXnMVMRZ3lxOPHxYqdJyxBKUR8sYx1prN9YUeefdUtknDTbtHvJjWB8lb7Jtap9Dw3CHHH4E21zgoNXnKJF4Sd2X2BBB35h82AzBXJ5eYEfrjxYf065xMZ7Sj13w020KQNUFu1RV5ZpA5MffrHEeXL6_vsL3l6RKKXbOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
آقای‌ممفیس‌دپای‌هستن مهاجم هلندی اسبق بارسا منچستر و اتلتیکو که داخل و بیرون زمین می‌نوازد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22947" target="_blank">📅 19:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22946">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kl1YxZPBvCTSfEnsn9CqMiqVb-Vo5NDqEdwAcMN5WTj5AnQaKtGh-6Kkw98Yh4CeVNdV5FLN5PDTXTJwX2KuF30pe_hAIwmB3uAlQfzW_gvvUdW3Sp5bG5lNFIt-NVpGk1sojNFWsZITvGZbbWTnK0XbOP0IVKQ-yAeGC9fKuJ2tlbv-B2cyKlQvVcqZ60Wr2PFv2mIaPhQly4VDX5Mq-z20wkNIc6ev1iW-K5rgY94RLBj2EbuWJYfFV77zKXCTMEyJHgQTFM74ZOWM1zWRaZBuNopb4B_tkZm_N2md0T3824xgoRjcvXRErCJ3aEKQtcfgoMoHaRiijgvfLphSxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💳
در
#رومابت
با ارز دیجیتال حسابت رو شارژ کن
🅰️
🅰️
🅰️
شارژ اضافی بگیر
✅
🎁
20% بونوس برای شارژ با رمز ارز
💰
10% کش بک روی تیم محبوبت
💰
100% بونوس خوشامدگویی
🎁
20% کش بک بازی های کازینویی و انفجار
🔥
همراه با درگاه‌
#ریالی
#RomaBet
📣
‌
#بدون_احراز_هویت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⛔
در صورت فیلتر بودن از طریق VPN غیر از سرور انگلیس ( سرور
🇺🇸
🇩🇪
🇨🇦
🇫🇮
🇹🇷
👇
👇
)
🇪🇺
https://trentivo6402.bar
✅
کانال تلگرامی
#رومابت
16
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/22946" target="_blank">📅 19:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22945">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aquf5iRIRqKKN_ZtXyCr87EKG9mjK3b35ta2iBBOtiXv4oxXl_WaCdWOpi7F0F5jlwwK2MffG9KvIT1CnuP28q0EcKAvsFQw0vwvh8SNlUgbZdDMCw6bzrUutMVLXa3tPmj6jr_Z_mrVqIxKS1pP2IcwMZrQBPJatN3QOguXSlvLA4rLm70ZcFl3Z2AF_7Q-rUok4VznUiMyV1vHEMtMADmbpOkY-bZCt6-HaSqQXw3D-1oQkF6Tg07OuBcP5SKWcYvLDFq5Q088UKhsIIldUa0pXqTijKbuhYUhmEpEO5cHXVLWK_dj1VU4uq41XhIhjPGfciFh1tkSJB4zEfVMEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ترکیب‌تیم‌منتخب مسن‌ترین بازیکنان رقابت های جام جهانی 2026 آمریکا؛ به احتمال‌زیاد این آخرین جام جهانی این یازده فوق ستاره خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/22945" target="_blank">📅 18:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22944">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4y-d7HUKC4KSkdBVESedmNt-ckhAvP34uKzQJnKsVsfK3BH3YMsYD0xjl1udykpYQ98dcsLXt2LJrRYZQFRQ9oIqQ01zFAAyPq3RPuBTSh4Wvm8ZrmdOLJupC3N27CHIRLUZvSp7Jknndw0Rqyti0B2KUscl_D6pi5MEiFAvhE8v2QTid-mnm5X0A6Oxo6xAzRdSk3qyzEQpSbPUPK_uLWBWB4v3DeObhsKQXXZLri7SjS9qBX5uxQF3OW3IEW7qO06nyWFKVIugzlb_sEBeWGsjNSYu_wq2kRuBmlZmS9XL_RWMTd87nryf-UguEtp-UP2Vq-7yCVc_eC-GLBrwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریزیو رومانو: منتظرحمله‌این هفته فلورنتینو پرز برای نهایی کردن قرار داد مایکل اولیسه از بایرن مونیخ باشید. پرز قصد داره به هر قیمتی که شده فوق‌ستاره‌فرانسوی باواریایی‌ها رو جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/22944" target="_blank">📅 18:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22943">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OnwCOwMmg__OFP-jonZhYxNtuIzaOFGY_PE9xMctFmlK1xk8IIB-sbqdWy4AJ3CBsLbj8c7LugZZ3qfg-kGzMBYIyO8zSWW-LaDdOY0UJOF7s4xljWYBh0-7Qc0uarBcl-UEu8ze_GcTMJ82zOMGpodXqgJMTpqTPIFG8amaPOEeJo9hfVOz8_X1ecb_G7bbMopNv-WePZMYctgxtxxMuxHu_7u7lnHgANGXV7ouQ8YLv4zrl72jz2FlyNzEUiGlKxaacvAposUSu3YzDeE3jv4xdzuUMqhfX-szx5k_Altba6P6I3dG3yd9UpjNE9USPU5tS2ZItFhl7vyfpbUYDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ انریکه ریکلمه از پس پرز برنیامد؛ فلورنتینو پرز بااختلاف‌آرای بعنوان رئیس‌باشگاه رئال مادرید به مدت چهار سال دیگر رسما انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/22943" target="_blank">📅 18:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22942">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19ebed3078.mp4?token=gTlgjBiGEzBv6o8A9r8bI_uQXTmxP4pC-YQEqkWVeQ-rjLSgA43HbVRYL4L7c4y5_dFS3WqjrRv2_ZDnoEKyhh2Po_wj86n30t_rnm5-5_WloygI5_HalAa9rlJ3PfYMrWfDHMjWHsVNqUXF_4L2DW3e7NyKvt-0bu2x5WeADMVaMXkF6sUWAWfM2L36bLf9nF7tsJneiB9TYywyJze8r7Oo_rXP3ZFT17m_sUgbPLY0FwLTfTK0mdVNG4oRmkFEjU67tIDdVtpe43VSTF-fk1EzkrV7wuCwfe8rcES0Pteao3qvRmH3KXbKsByF0rqgtpFQOC1_sNChgx25PfDPpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19ebed3078.mp4?token=gTlgjBiGEzBv6o8A9r8bI_uQXTmxP4pC-YQEqkWVeQ-rjLSgA43HbVRYL4L7c4y5_dFS3WqjrRv2_ZDnoEKyhh2Po_wj86n30t_rnm5-5_WloygI5_HalAa9rlJ3PfYMrWfDHMjWHsVNqUXF_4L2DW3e7NyKvt-0bu2x5WeADMVaMXkF6sUWAWfM2L36bLf9nF7tsJneiB9TYywyJze8r7Oo_rXP3ZFT17m_sUgbPLY0FwLTfTK0mdVNG4oRmkFEjU67tIDdVtpe43VSTF-fk1EzkrV7wuCwfe8rcES0Pteao3qvRmH3KXbKsByF0rqgtpFQOC1_sNChgx25PfDPpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظاتی‌از مسابقه‌کاراته‌معلولین؛ این چه حرکتی بود تو زدی آخه؟ چرا از روی‌ویلچره انداختیش پایین؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22942" target="_blank">📅 17:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22941">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUOckB2bjWIYN0xZZ6dCKuJM6pHwvk5jUttDXM7mQZGN7BHqjSzklTHWrjZWX2UvuwmriqDZxmlxTiAIsMEzyaIDc-ab3EhkK2ub9cTQMCWiaK1G38JY8TDPoCwufVy6KM6TPclTrE8tA9_X6fqqmLk859abVuylk0s2WdH3ULOVwjqKDbRtl3e60z9I0LXZJPQ7URUJJGelLvYDn4u7h8LlVHwE-RjtDSpfYb9SMpcMbMNypQyTnuxarOB6wXr56cHx4S7zHoqDEM8pTH0oLfUOOEv5hR2pXTTyBG5SKrAp7Kibd9S4Oe50MIne-YMxgKj2cbkoTWiLcGeGbS6vOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رکورد بیشترین بازی ملی برای بازیکنان حاضر در رقابت های جام جهانی؛ کریس رونالدو در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/22941" target="_blank">📅 17:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22940">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SwEi5HzLXj61AzlNa7NfpEmjqN2FNHjsolhsT_eFNYwws4uQiVBxsfmxEve5g_q910l3QoZHRSsQj_CNikrI3_TEMdTIysvVqriHguVXqMV3Ls9dkCb4NMlKgl4hLP8thw9SwEI7DkjNx9FmqCH00bp8KZzQFvlIgdJq4-FLaBf4Piu_VJPKsGN-VMdhtqaAqBM2V0TjRDsjomcsOWZJzqyk14A1ryDAFuTdoIdq_Kk8MqzAzBPQtWPLgWfwVr_JX2QDLQtABra5tGh5naAgspaaVUlM9-Z3aL2tQ8zB2ZPX0q6yyiDW9-JQ26X9SP5P-Tqr7NKLNXC3BFanfG0v2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ مدیریت باشگاه استقلال به دراگان اسکوچیچ پیشنهادداده‌که تنها دستیاری ایرانی‌اش در فصل آینده سهراب بختیاری‌زاده باشد که درصورتیکه جنگ پیش آمد و اسکوچیچ مجبور به ترک ایران شد بختیاری زاده سکان هدایت تیم رو بر عهده بگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22940" target="_blank">📅 17:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22939">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KyCEEn6UWsnEEknB3v74sHVIMOrf_u6yoLshuGDhRWmc4cMRPEG3OeX90_s0GNmLBOP8u-KqgO-M5xWRo1_z37CxzhZnu-cwrZaK9RwAHM_dXGfYDf8cggcfzaG9BQ0mCraG4579Wlm2lxYPFDM4giTMdwTSE--vh1utytaPt7gi4UvYTzUoNiZbP439ZOL3X3YHE408hzHHQhsqEKlkmoQDegqu8qzgkRbvfRLNbgEp2u23gQ2JjlPk2NuefNceZjbLXi3Cm15cfcnDIhrQ0m0cWpP6XFhIu4K6o9n1CDa10eo6Su_6CAzUCAcSl-tf09TIPz13de-FOs9N48xtNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق شنیده‌ های رسانه پرشیانا؛ باشگاه پرسپولیس در تلاشه که مجوز فعالیت افشین پیروانی در لیگ برتر رو از نهادهای ذیربط بگیره و در فصل جدید رقابت‌ها به نیمکت سرخپوشان برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22939" target="_blank">📅 17:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22938">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUOGywcYr8M2eOm3_Iw6_5XF9OXFMiVykQaMGcBnCR8HI2ssBXQsMN3M5Jx0o2A71Vic40fdDhGE6qjtPlu1Kjl9Otehwsdnp6uAbi5BIEVdc0viTqRlgp9YF5StMeYI8HaxwHaYHgbVULA8ezEQIrRplQKTKQyXGM4f2kkzQ8eouXuhLJFa1OoNvax7gbFWb0RiU-bO_l6q7oot6YixThQVzfFPlXPr3s-CnOHcHxHnnfUclmWepJx8r4iywwmVpQUbJ24rJJ52GaT0TSKgkI7Lm31FIldIl1OjPfX0PzMj5tW4Pso7BW-Szp-8HkR4t64JTK0gVtIuHIILPbzbGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
تا این لحظه فلورنتینو پرز در شمارش آرا از انریکه ریکلمه جلوتره و به احتمال زیاد امشب او بار دیگر بمدت 4 سال رئیس‌باشگاه رئال مادرید خواهد شد و از مورینیو،کوناته و دامفریس رونمایی خواهد کرد و سپس روز سه شنبه آفر 150 میلیون یورویی خود را برای جذب مایکل اولیسه…</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22938" target="_blank">📅 17:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22937">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ca0d90aad.mp4?token=q_9e8d6dLF-tYBAGP9xMgFy8aIjdhF-yB-1cZEOgpFq_q6FOMzoC04Vh8FrIWEQlfwPoPhw2dw6J_koPVXmVhIOxv7HhPpU4e6SjMY8hylIW2umJrYEPvbFyoXOJ8PRtA0e71jbgW4E8rFfOyD-Lg9c6Fukmoj4e96X9sMlRyqcwW4ZxH8TUDEBN7QG11k7FrWeP0hLrQ3FZdjIDT-FhbfqgJhw6M45LcD2S3b5KX8uWZUH_ZKutq3xXsT44Kg61zpGfpfJegOLtznhxhk1IgDU3ypeDDK0m_MQ1W4kHmihH5-8TwKhKEkBGUVAiwn5q6eF1q6L6qpT1ELGYZ60a7QnGnX3JWo3EN4v8tUTJgbl32WXDEkXyAI0DzKvMdOXzENaDVZGpg-7tzapQkDQ1-4Frzt-nhFBpe4z-y2TNlzWQpbBtkKzaClYFoeyHa3ZSynEet-pp1DYLL1r3zCuahaEhwlo9XPMBGgzoSfUb_Hn30X9jQxhhio9uD0BAxAhZ-WRdKVEcSQ_Ls3Pe9cBfJ_8KZUJutLPKZEUL7_WoVv79dwzL-MPJPmrqz_j8dbdD7NWCGzKgwkDDRdi9uTctULxgH8c_juFac8pF-a46-9G-DREeKrUcN6oj3G4WHuDXhs42G-2BtY4JodSmZ4JIRqeCHLV7Igq2Uod3Nx-ot9c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ca0d90aad.mp4?token=q_9e8d6dLF-tYBAGP9xMgFy8aIjdhF-yB-1cZEOgpFq_q6FOMzoC04Vh8FrIWEQlfwPoPhw2dw6J_koPVXmVhIOxv7HhPpU4e6SjMY8hylIW2umJrYEPvbFyoXOJ8PRtA0e71jbgW4E8rFfOyD-Lg9c6Fukmoj4e96X9sMlRyqcwW4ZxH8TUDEBN7QG11k7FrWeP0hLrQ3FZdjIDT-FhbfqgJhw6M45LcD2S3b5KX8uWZUH_ZKutq3xXsT44Kg61zpGfpfJegOLtznhxhk1IgDU3ypeDDK0m_MQ1W4kHmihH5-8TwKhKEkBGUVAiwn5q6eF1q6L6qpT1ELGYZ60a7QnGnX3JWo3EN4v8tUTJgbl32WXDEkXyAI0DzKvMdOXzENaDVZGpg-7tzapQkDQ1-4Frzt-nhFBpe4z-y2TNlzWQpbBtkKzaClYFoeyHa3ZSynEet-pp1DYLL1r3zCuahaEhwlo9XPMBGgzoSfUb_Hn30X9jQxhhio9uD0BAxAhZ-WRdKVEcSQ_Ls3Pe9cBfJ_8KZUJutLPKZEUL7_WoVv79dwzL-MPJPmrqz_j8dbdD7NWCGzKgwkDDRdi9uTctULxgH8c_juFac8pF-a46-9G-DREeKrUcN6oj3G4WHuDXhs42G-2BtY4JodSmZ4JIRqeCHLV7Igq2Uod3Nx-ot9c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اجرا چالش فوق العاده سخت ورزشکار روسی توسط یک ورزشکار ایرانی با رکورد زنی روسی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22937" target="_blank">📅 16:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22936">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iX-hPrx0XQeQ4NjTm7ONj5fnHsOdB_etadWSf5bm0dtOJZMQdctFqn4ISzvzm-Ts92tbsaNIKydj_tlJ_tKAnWgey1Hh8pwbBdiN2fkHcAz5ei5PxPB90fh5yJoncPTvpCbtSkjzDKJEZCOUed_5wGPUThQhkiCLOKLSfQV3xIX33Z_vPbFWBc8P74jtpz3gK9CxvC5qiy2kCUGJcvsMzklHR_EUeiKihG-BBQTUM-tqHYS_6c6GsSV5j_QvYdQ539DmmzqHa9q3SlwwKKzMTXqD_zB4gn1Uuul9VQpP85U6CYT9YWk7iyidQbGOxe-Z8kMjYa1-7zb7HvClkG0NeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات|با اعلام رومانو؛ دوشان ولاهوویچ از باشگاه یوونتوس جدا شد و قراردادش تمدید نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22936" target="_blank">📅 16:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22935">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzvXN6K9J3VOWZrrRC5cv_Xj4z0yRRiTSp5NWAhBjBqHG1G-MFkCjEcVCtYrOFtWqfdJY30vyZlkg2q9KwWd6GQJs1UHyV0WCUUefdiqxf0A93Xa-sU082NnaatShJuPJ4-mvu8tP5O8lKCGERgtbmgaR_HhTOY7cHw-C4zrLhHFDZLUFNpe6Lum2gmhz9BXYTSPu0SFE6YEzOShcHGnjdJcbsSxlOeLsXbDcRAqxem_wQm82-FT9x25P8pEATcsLSzrlgRvYtqs319ALMIzsHWdQ5IFoUY2xep4FJMksCzPSoa_B__ZY58GaUmKRc-m-mnQSkwaPUTklgux5GCV3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#نقل‌انتقالات|گستون‌ایدول‌ خبرنگار آرژانتینی: با جرأت بگم که آلوارز درنهایت از اتلتیکومادرید جدا میشه. مقصد بعدی آلوارز صدرصدر بارسلوناست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22935" target="_blank">📅 16:18 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22934">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cbc8NUM6WhNm1sLjEiHxlUFnO7DV8k0E5KbxXGL7TtkU8cFvlnAfzWCWIhcFF7d7esGk_7E4FD6LGSASHugIcQO3kO_s4xZPTe033MM9e6FwOn-6S2jO5YANJ3RNwxXQg0wosxKPwSIC7L-f1eZcgti9uXdh658aGcms_PBZYgbbpl9XX2O0tQIijOyvPVwItJEshEHfYGS2t-gLrDBlqwGMCfPPis5JN9XGuSkLmcynGHSDabDKGah3EUdAzA6WXWszy_ynAUtgmCsUaSdhkG03PBkxPHZ3h1Sx4of_BSJbzvmZkOru-HWbfngP3jtd6nL8nOmegqzVsHlsdtNz3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
تا این لحظه فلورنتینو پرز در شمارش آرا از انریکه ریکلمه جلوتره و به احتمال زیاد امشب او بار دیگر بمدت 4 سال رئیس‌باشگاه رئال مادرید خواهد شد و از مورینیو،کوناته و دامفریس رونمایی خواهد کرد و سپس روز سه شنبه آفر 150 میلیون یورویی خود را برای جذب مایکل اولیسه…</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22934" target="_blank">📅 16:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22933">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139c25f87f.mp4?token=asZfy_8TxAPLyOyY_thUvstTjPk9H5uswT06Lf7Kv-Hu1ORsn3LZEys-2WSzVHDHjbZj7rc9CE3W3_ncApxIqZ5ffY1Looe80lVA-BHRIsr0FeaIr7j4D1ItQ7vU4IY145hDClGWcGpz5t7_YLfuabRDxWtlyRX0xG978zWJda8DrMltM3m9TzEKo_iII3W3O0tstky6t3L-fdYvkKbLg6KmLwKoEqWRTY673IEbSKSj-WNJDiALJvD4ErQ_dcnkif-bFX8CwobGGykq76rhI8XFemqrxsQVW6eGwuafQIE_bZ7ZAAvrd5SdXMB6fkaelRiHIknsUxdK63tZZ_dMSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139c25f87f.mp4?token=asZfy_8TxAPLyOyY_thUvstTjPk9H5uswT06Lf7Kv-Hu1ORsn3LZEys-2WSzVHDHjbZj7rc9CE3W3_ncApxIqZ5ffY1Looe80lVA-BHRIsr0FeaIr7j4D1ItQ7vU4IY145hDClGWcGpz5t7_YLfuabRDxWtlyRX0xG978zWJda8DrMltM3m9TzEKo_iII3W3O0tstky6t3L-fdYvkKbLg6KmLwKoEqWRTY673IEbSKSj-WNJDiALJvD4ErQ_dcnkif-bFX8CwobGGykq76rhI8XFemqrxsQVW6eGwuafQIE_bZ7ZAAvrd5SdXMB6fkaelRiHIknsUxdK63tZZ_dMSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
آدریانا اولیوارس مدل مکزیکیم رو بدنش عکس تک تک بازیکنای جام‌جهانی رو چسبوند و از دخترای مکزیکی دیگم خواست این چالشو انجام بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22933" target="_blank">📅 15:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22932">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2rH-V1paSuEvmuqq1lYu3fy0YK35UbZyFrUeO8p1WNUEyrFCgrWsggjR2lwdlR4WEa7anaCtmaWNZ5I6cMwqqYg96tmjJbOtvfyzUvMfsDzOyZD0vWaFkMQvGmHTjbFOL2pu_E0kZ9raBwoeyrvoKpUxaJUG9S-6Xa4blsl4usIyQg6YTQ51bWswkzWP_akv664nTIEaRUO8ke94iJndsCucO9FlFVME80891MIMm5ziDfbJ3nCjq5DtIM-NEumReXL0wclBZHBuyhZiEFuOvoiyWpw_s9DKP6a8QkRxt5zSdDPE8NK1hpWVxVf1R09kpSSAwrPyznZPPD0pKvjKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
انتخابات‌ریاست‌باشگاه رئال‌مادرید از دقایقی قبل شروع شده و تاپایان امشب هم مشخص خواهد شد ریاست کهکشانی‌ها به کی خواهد رسید. شانس فلورنتینو پرز بسیار بیشتر از انریکه خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22932" target="_blank">📅 15:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22931">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3PcFR3pUV-XOvcHBZuXt1o5s9aIqFKeB-oTns7UZLQfL6EzWxNO2VHYI50kLg-iuX_kSiKFeamTLfqLchUrsAvF49FiDp8KCL5ZiMJbos-9oM7xhUfaoYV3ypEnBVsvu0otlbShrZ3iKOItYag5uzp6XJzB_UXrgggijmBoF287KZkk49thnaWQgJNSy9aJvtareHWWfMu61JDLtJbotBrJa-gYWisYLpEjqVixCAa9Ot1aeO3cCtaAovRo-wz21uPQWsB1UnuN_mtBd426CrTMlZDG9KVDhP1GpcEeyFGbSNiwFoaJYyWv_3qtOvU8gLeJAriTQkSG2h70b7CxPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال خطاب به‌تیم‌های خارجی که خواهان به‌خدمت‌گرفتن امیر محمد رزاقی نیا هافبک 19 ساله این باشگاه هستند: 3 میلیون یورو پرداخت کنید رضایت نامه این بازیکن رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22931" target="_blank">📅 15:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22930">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ge-rcTRIaKsA5_59WmZy-azvkKNQrfpUbcZup87WgFmnl6yu4Y_jEqRLEAwXoi3JeCele6wl8st2pdy0d4usqgIC6t8t4IhUSY1etCoDCuuwpheft--hBaTachhgPisvR4tK6xHf-DkLnur6Us3-ENKSDAoc1IKsbAvpxZ61vFQPOBabC1GmP0RGabGw3Flc1CvySHa5zPHimeDEoNDsmp0HI6ALHlDXPYxSkkkUNOHkBMhBAs7YpIKwxXalkJcaRLo3peIYkJAt0ZtEJFhOo1ugZPMIVEPHuvjPA4Q-09L3O_Kz8HBZOvK2i6d8OtvSN3YpcGyBGAZezCV_wV9_Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
معرفی دو تیم بلژیک و مصر برای رقابت‌های جام جهانی؛ جفت تیم‌ها حریفان تیم قلعه نویین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/22930" target="_blank">📅 14:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22929">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUbyHUeW9i1WPb9R48DtKf5A-CrQfI_xE21oiLKj56ZIXRaYGNfkBfz1wO-sA1iKxKQsYQo5aE-jA33iZHg4Bab8Ban2mWnSQwzp2jGktCPb_U4YXr5H00wA5hqkNbX1VGqtyRzn6gOu43aFhh9UdChoCk26zlOhVRLJ1CwuehfdGyUqVtprgISvzoST7ZGeGBOIWadunR-C_WhUWZOBJkmywhUpASBd62E6Vq946ny1wapNXfwro96TJa5YVb8NGCrdcehjchrZm9A0tyTsWa9fwDZKDquXA46DR9x59V2Wxw9r-nzTVsTarxIwYzhggx65mF0t65TtNT30YrdFdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رکورد بیشترین بازی ملی برای بازیکنان حاضر در رقابت های جام جهانی؛ کریس رونالدو در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22929" target="_blank">📅 14:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22927">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vsNvgUyn6j5X5Cxdur22XssRL6WkXrnSp9FV_PBxtC8J1ObiAy3sCiT-7VE7Xui3ed3mCDYH9NQRhMCd--6MMvuqrb_Zu5YdxSL6OzKdmUozLTvAkkLkYWovzNMysjv3nFxJv0aKG-mqPe6XEplYH5n0uKk4dU4oYyAnP8HFkrZq0eqdNat7Na3E6-Yg2yB0zOWSoP45tzkvrCroQhgQQdmqCRNpFSRf7k6GU5GeM_DDuaZHDTSlmGz4oIwBBeeqz1cA-EC3vrdOgn4tSeyfmX1puQmLOmo2LLfrUv9VUrTyW8DjxEjr73k29mguIKZkVj5Vh-LPRAjCVv-OZ0nTXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hA1lFd6gs_je-nywPB1oOSqBAww0oIMniQ3GlKdHPP3Z4Ko1IaLw3O7g3mVI_2U4LYgndFy_F3MG56pQnj6SrS5dEdIGr1Hcx87tFs3W7Ix9lTVFy7hwFjQ9Kd9VknyzUFIl_oNL_7K_zabdfAVQejGnEB7J9UAwC0Bt6-6c5FY275idgZFB3uGQZh-Fl75BUet1Q9kkRSTIZosSPnhl28AI5PY3q-83SbauwRrY1lUuBmTzpz8otUitsEeLUFVhfkBkIkDv5vsud6m9makOQNRrrnQU__mme68Tqmq1ni3RRpGUBw9-D9JiBGnhg2U0XrGtBM7FnmVWL3PsmPK2Pw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
معرفی دو تیم بلژیک و مصر برای رقابت‌های جام جهانی؛ جفت تیم‌ها حریفان تیم قلعه نویین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22927" target="_blank">📅 14:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22926">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VrkwoG7vpUAjeHJ2K1uZGNHv7HH_Pt-XAGZRlwNe_LQHGEkuGDGvqCM0GDAjBVEg3nlknBgVoAUOi4jOGcq5H5JAr0y6WybF7YMvsW9Ochv3-lt2wsQ9kLT4IL7zQe86YEresdEWf-IAbeIGKgIRrQdHbOsgOZekKaCGex3uDv7z2yHHMN52eLIR83nuZ6DwKUAhw-hdxRyteO0OJA2v-Om9phtUyOQggJwWGTR_kEtF3_ZduBsaqjfzXrxLNewl-zr-Ts17Cz1hg7UAtSe1zdZbMA4wVvJTkE6u0M4-csjQ1tbtfeTQt8QBRx3VB9i_rIQpTdoFu_Eq7B5ph2IqjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رکورد بیشترین بازی ملی برای بازیکنان حاضر در رقابت های جام جهانی؛ کریس رونالدو در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22926" target="_blank">📅 13:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22925">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNlEddedSEnyan1ydU7B-6ZU3yUl26NNZtH7UDJ6YINOW1CwGMxfHNouyVdNWhfcbpemKOmg3ckN2AjCdeJLblFlGbEB9FMFCmBnaAnd1D7PYrPaHy7gpZWC1Ezwnm2ncJHwo4RWrlxtOMSvjOgSm3Yg8BEHQ3Ro8YcuulMg70tp0cDIOayHXWC3MdxyTU6OV0iKQrp1wPZaZPDGrVZBPqZFV1MXgeeKepewE5OtXxD-7kCw-2G-EKV0pDDVmLhvtf43ExqeDudLOkH5nTPWA7Rb2Ve5373A09YTUhBOvAURmRPZvoWWlNZqnzy1V4gNBrmnGtMzkggLR9hhzz2YBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادی‌کنیم از این ویویو بسیار قدیمی امیر تتلو درباره استقلالی و پرسپولیسی‌بودنش در زمان‌های مختلف
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22925" target="_blank">📅 12:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22924">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqq4B065WAdOGBhSc-Ar7XRBBMzO2u8jz6F4BSJSyDR8yhXhxD3IWA4LtSPn5vM0d_Kio5YZg2vpGkjp9T_YZDgHrWTeT_2qJDxOgrCGTx-EWOfQaI020F0ENWS6wB8hK83BejVg04YPy6SsOS63DpftvWA65dC1YvWACtxRPiVsqTrKeHmrT84RmsgBWjEEoo1PePREYQXTOhJ5eCFKbs22IXlubtFri6prCesRMjxTWpqXd2id0fqtdnA-Obb8hLHGZ5p2OCmGwF6wNmymtum7svy2pgfWlMs4ycdW0ZRgcqWsnk0Jhgn3A3yveYPgOTvAjrE4THBgaQTCBwroTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
؛ هفت سال پیش در چنین روزی؛
ادن هازاد باعقدقراردادی به‌ارزش بیش از 100 میلیون یورو از چلسی به رئال مادرید پیوست. او در طول 4 فصل حضور در‌این‌تیم 76 بازی انجام داد و تنها تونست که 7 گل بثمربرسونه مابقیش مصدوم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22924" target="_blank">📅 12:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22923">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a46a056081.mp4?token=CLa2DRoykEvuVTNXV3PgQQahmMBzmz4EkqTqp_iVW1MR0p4kKbQPnm26w72pHyrBxdba7aTtuF8LmY-G413D9MHncC4VTgO-bQhM1nhi7lTuqOECgs0wiHtfn8pOr2ET05HjDhWzpryqEIe5o1ritq6l0XXuls9H76YuaubIAKh8iX9XVoOlvzyhZRRl8qWJ6c-D_OKuNVIauHwyqxvihb8YiotIP514tYjVFqeTTXRMq6_YmvqLcLxbuYv1U30gUIEtTTYGVd7c3-l4087LKT93hiEfY9-tzKC4vndWGXVLkDsJgkAoATumFBO8XFIU65I4x_nmubut-A1-RSTSRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a46a056081.mp4?token=CLa2DRoykEvuVTNXV3PgQQahmMBzmz4EkqTqp_iVW1MR0p4kKbQPnm26w72pHyrBxdba7aTtuF8LmY-G413D9MHncC4VTgO-bQhM1nhi7lTuqOECgs0wiHtfn8pOr2ET05HjDhWzpryqEIe5o1ritq6l0XXuls9H76YuaubIAKh8iX9XVoOlvzyhZRRl8qWJ6c-D_OKuNVIauHwyqxvihb8YiotIP514tYjVFqeTTXRMq6_YmvqLcLxbuYv1U30gUIEtTTYGVd7c3-l4087LKT93hiEfY9-tzKC4vndWGXVLkDsJgkAoATumFBO8XFIU65I4x_nmubut-A1-RSTSRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
وضعیت‌‌آکادمی‌های‌ژاپن؛
قشنگ‌ مشخصه دارند برنامه میریزن که یه روزی قهرمان جام‌جهانی بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/22923" target="_blank">📅 12:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22922">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jSc2hG_8WvSAl6lmrPE2I057xjCfZ1ggaXX6GC-tG6kiwrYFD2ofz056B6L8gW2uPk79Ihc16YffAG6Hy6NqVo2qSer9dSWWa04LnSi9QQhByIMkjnraVuFk5UjoJDFGGm4VwpErGw-UPsXG6Ow9mT0kN4CtPxv1We-XHNwlFxZUjMvWOdOpaOFSECWHeFiC6VEAMqicbF8szY7KNIfH4cXaf5ZHOffF2eG8gzATv8hnNojfNQhyl2dLV70Nhh5xgqp1BQ5bI6_co7YJr5Wm8YDDDIBNqQKgUMykbFHkhfFqDd0oDF5A4dZiHTCRtvgYZTytAQIMyXbZFpkXsL4AjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ حدادی مدیر عامل باشگاه پرسپولیس هفته آینده جلسه‌ای با مدیربرنامه مارکو باکیچ برگزار خواهد کرد تا تکلیف نهایی موندن یا رفتن این ستاره مونته‌نگرویی مشخص‌شه. باکیچ علاقمند به موندنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22922" target="_blank">📅 11:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22921">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad2a01aafa.mp4?token=kVGOfec_9hjJZa7xi-cNAWWWvduqr7KDeMc6hkK-JHGaMQNm6ex9SHvTwBmzqgY3tTOzlo8KeFf_9t-f7phpZYJ207BuV2WrcZjBmLCcgCIqVD60KxEqgOoHZNDMwr8Gq2H358PI3O0TrMFT5EPpiE5yqjivYl_xjzekefHud5fjdw4U800XRzq3HBw5jy8eStZmGq1q0E6kg4QRbG1_DJiuSx5h23denO5bCN6Hr4-6jL87Rkvh-br4ulaS7HbnX0pAI0bWFuU1kKWmDAdbd2gJ2rtX5p_2QEWhSJPKFnb9zhfhhYlcf9QRRCUisjlQQDJHAnnMm-phbFi5kElqow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad2a01aafa.mp4?token=kVGOfec_9hjJZa7xi-cNAWWWvduqr7KDeMc6hkK-JHGaMQNm6ex9SHvTwBmzqgY3tTOzlo8KeFf_9t-f7phpZYJ207BuV2WrcZjBmLCcgCIqVD60KxEqgOoHZNDMwr8Gq2H358PI3O0TrMFT5EPpiE5yqjivYl_xjzekefHud5fjdw4U800XRzq3HBw5jy8eStZmGq1q0E6kg4QRbG1_DJiuSx5h23denO5bCN6Hr4-6jL87Rkvh-br4ulaS7HbnX0pAI0bWFuU1kKWmDAdbd2gJ2rtX5p_2QEWhSJPKFnb9zhfhhYlcf9QRRCUisjlQQDJHAnnMm-phbFi5kElqow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیبروین یجوری به تیبو کورتوا پاس میده که انگار هنوز از دستش‌بابت دزدیدن دوست‌دخترش فشاریه و میخواد کاری کنه در تیم ملی سوتی بده:)
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22921" target="_blank">📅 11:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22920">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">💛
هنوز توی MelBet با این همه آپشن خفن و ضرایب فوق العاده ثبتنام نکردی
⁉️
بعد میاید سوال میکنید کدوم سایت معتبره
❗️
👀
اگه میخواید توی شرطبندی موفق باشید و درآمد کسب کنید در اولین قدم باید سایتی با آپشن های بی نظیر و ضرایب استاندارد و امنیت مالی بالا داشته باشید
✔️
🎚️
همین حالا از طریق لینک زیر ثبتنام کنید و وارد دنیای جدیدی از شرطبندی بشید
🆕
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22920" target="_blank">📅 11:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22919">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgvxquKitPnXu0PG5urlF6UMVx-erpbGgLtabkx2-n4dAxpOiXlsrdwrfcOaNgzkXwhZDGYmjnck4V4GP11orYXipJx0OGbLS4EjLI2Dt6RP0qxujqOy6LwPaSvUkDINK-PwocJqKZWeYQ_75IsfEeXEUE_CY_mKyo3tb6xYmPUVrbAecdGP8AP_UCdW2hT-fFAaN4JzC8dxO4cGEKiHxPtace0yfYq6RrLRcOb6ir2mo6hmC_UiTV712PrJGezrxYlDMgaY4XOLlf1UER0a12RLD7vLvPal2fmzObTNtEYi3BJqrJTkKJO1PQ0j9ssJI70f0GdMzwTgezoIX9tvHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه فلیکس دیاز: با توجه به شناختی که ازفلورنتینو پرز دارم به‌احتمال 99.99 درصد مایکل اولیسه این‌تابستان‌باهرمبلغی‌که شده به رئال مادرید خواهد پیوست. پرز این قول رو به مورینیو داده که با هر قیمتی اولیسه رو به برنابئو خواهد آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/22919" target="_blank">📅 11:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22918">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZtpzKMs_S51HTt3UMCCU3g3KIMC9atfPPXYii79s0vrRcu5kaNA0JoiTLRuPKYIIyjp6M3r59X3PBllMbxvGrCcDzFsTWUSQ9ZOznP5y39rzzDqRLZNa7KqkNAbyuEyqbM2RPMpS65ZN6cVMmrL7v-ywxnNaq3Zlqkf2DBVAM7uFemxl_12pTFf843YNjWFftbRp2nqeEmkPmts25mG3CPhKqjH6gW0sthZTa6Dj37GlatJ4dVMZmJnSWgc8lOHsDdHuvapsMPOKTsLdpMmlDrzbumn9hYw5PkK6xv9K1yTLaativGVqjGJw6S1Uo_i3T-Bo_Qm_bnl6Z_-hi9cDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/22918" target="_blank">📅 10:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22917">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d705d6a743.mp4?token=RcT-m9FdCvFouwhEGlGHRtSjLQmJCqs5xTK7jzRVibnleNIePrTWLcUefuRdSiIAyRdJoZUhy7HJIRJprrCLwc8JBjkdfU-VhG_6rCVTCT3FkWuwr-w4Cn3toB3B-gZP6SWMy-l0J6a31Zyt10cR2q2oDa4PDHBcW9FlhpKiM2MhbnUa5D_KofGje7rFl17x7uLrN1aE-xaxr49r8N8GiY26aPVa3QJFvBZAUeiIu6XWNZMwc8A6iWHYAbci8LN9uzqYtCeomWxF-XGQ8LUg6gcqM2AKYg3F1e9vmo7zWBuoksfP56NhfXLLvv5LxicqJTiR0SdOV1_R7VCfxeVMoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d705d6a743.mp4?token=RcT-m9FdCvFouwhEGlGHRtSjLQmJCqs5xTK7jzRVibnleNIePrTWLcUefuRdSiIAyRdJoZUhy7HJIRJprrCLwc8JBjkdfU-VhG_6rCVTCT3FkWuwr-w4Cn3toB3B-gZP6SWMy-l0J6a31Zyt10cR2q2oDa4PDHBcW9FlhpKiM2MhbnUa5D_KofGje7rFl17x7uLrN1aE-xaxr49r8N8GiY26aPVa3QJFvBZAUeiIu6XWNZMwc8A6iWHYAbci8LN9uzqYtCeomWxF-XGQ8LUg6gcqM2AKYg3F1e9vmo7zWBuoksfP56NhfXLLvv5LxicqJTiR0SdOV1_R7VCfxeVMoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جایگزین تشویق ایسلندی رونمایی شد، تشویق وایکینگی هوادارای نروژ؛ تو جام‌جهانی اینکارو بکنن ارلینگ هالند جوگیر میشه به هر تیم 5 6 گل میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/22917" target="_blank">📅 09:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22916">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eylSR44lMZ-0dNlRPVGfaVBSxQoE1bBEPwkfXfqK6upVD5-PhHW9TZHNR80kOwwLVDCzhKlKWZ419j_UpxoITX_57es-m3LqAXuHgIcG6HTxEWLPkcEQAnJ5pcHQuauHT1_b9fdd5yMElcP1n3cCrxKp0kC3DRFe_VpSA8aogmPNvQyzfhwMyS6gzaydtmMTTVIHird_n2N-b-AIb5_dnNTMowl8PqV-JXA-M9y3cgsRWblwMJlqbOxP6Xvo_0o3YnKZo5ShEY9R5SKyIPt76Hbm5NjkvBI-ecxYdsk1vY_tDd0CLS5ASQ7sqPnRnkWo9FXgJmd650S81vzc6Fmfbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مصاحبه تاریخیی کاکا:
برام مهم نیست که بچه‌ هام بدونن یه زمانی بهترین بازیکن دنیا بودم؛ فقط می‌خوام منو به‌عنوان بهترین پدر دنیا بشناسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/22916" target="_blank">📅 09:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22914">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHU2ZejepZwXcZJi2mcsGHejIxUxn6oi6hNrkGD7EUcWabFV-JXr6ErywzbysCKFSIEzh0etsz4_L1NLw1gB6Sn10taB19PG3adrZP7IKxdJ51ji-cWnh-HxkzzcZRvrTmBaAYzFFhwNbKXWjW9d_1VDvVyYgKSQdJJhLM3RkOtxF88taqZA7RRNFi9ByzUXkTy8iO9KXvGrAIfefIMyXbeMJ8HETRztrgCnBZAY6-C765QH3Q_J_9iJHGOo4vW3RWsJU4w8Dk1jNd3V3Cut6BfDRmUXvrelvHs_pwtpxV8ISOm4h3vuyAKtXmYsgl17mEdj82Dn5Ea5OrJ9e9wiUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌دیدارهای‌‌‌امروز؛
تقابل شاگردان کارلتو با مصری‌ها و جدال یاران مسی برابر هندوراس
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/22914" target="_blank">📅 01:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22913">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/is9kUdBLUPOatju-iccvzScdDFMYsuOUiv6nkTUzb6sNF0EvTSDazkwZ21qHMPwRZeV16DdADUVjuHNa69jpZvej1zaNt5W-HeGQo1_c4wvRJEX6r_0gZ0gyDIf09IxRcVB4fqKsZfCIayXo9Mz8t5PYlesu-YR1bsJdA9eqx_rGmMRMd-81hTcae7lZX-udNkDFrUvWjwBGQy7lar77LR6c2xgRXAmWMSzIho_VmI6HmyQoVndhW02UqYWxLRMYlGGvFaGjM_zYzu4tsTJBJd7pH8_awffM31BqdmJDFy3FkawFBlpTQvzYDlY4DF5NkbZq3CYK-JftqHrWXVy4dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌روزگذشته؛
از بردپرگل بلژیکی‌ها مقابل تونس تا برتری تیم ملی پرتغال برابر شیلی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/22913" target="_blank">📅 01:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22912">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAO69l8RDdsAv0AbXoKDVdf3UMxhFfM3MNt8g_DXjbO8xv2y2asx_lLb-7Mdnr_f2KHcMmS257uhdILT5ysdhuB2giAGA71fBdhf0ULexFwwxJZsfrTEDKIJod24fFRW438bU1KRp8_-8leBSmwsmxlHzKIMbiNjk8_VclO76t_CGq_TT-twveiiLOAypSZoQIgVP5I2Gw7Z8y2Ibja0i2DuYmQBMXEpawA3ZWKAFHG8oXhkIzvt0dzHLefQDoX2Gz7xOqULyKo2JUGmlJLifT-bdejjmAOgyqKYx6o_Rx3k_e93rLoxOPL6AmwTZWXmkby1sXVubz6t3Wg06icftg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ طبق اطلاعات موثق به دست اومده پرشیانا؛ باشگاه استقلال افر سه‌ساله سالانه به ارزش 1.2 میلیون‌دلار به دراگان اسکوچیچ سرمربی کروات سابق‌تراکتور داده است. همانطور که در روزهای اخیر خبر دادیم تنها شرط اسکوچیچ امنیت منطقه است. گفته جنگ کامل تموم بشه دوباره…</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/22912" target="_blank">📅 00:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22911">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc9d6ea65a.mp4?token=mQ8kDBZCNQVof7WQDa7hPDMo7Tqd74yFxCGiJlXdqWGBbFZE5Jd2PYf6pPINjHIEwFV1y-doCSWjG73UhoY1u2DqmcKD2EHHbTotVD-oodXQf8rAGFxZFxGyroAvXNhDayiFpaXR6iXBvk9umZSioUvgk9JUVFVjh-zbe_1dhMYn2K895WLOL6E-qmOXjqfJSQ1husvPSXfy98I3X7yCWdaOrmLzoRIdWPpeC2L0nRX37hY7WgDdaqbeYylT0jP55FUwD46kk0j8FLdwBcmWS_PtMGcKobU8FX-66T-llOoKt3QoXirA_c_c5Vj_bt6z9JWDGT0ZzwF_VOYv8_ig2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc9d6ea65a.mp4?token=mQ8kDBZCNQVof7WQDa7hPDMo7Tqd74yFxCGiJlXdqWGBbFZE5Jd2PYf6pPINjHIEwFV1y-doCSWjG73UhoY1u2DqmcKD2EHHbTotVD-oodXQf8rAGFxZFxGyroAvXNhDayiFpaXR6iXBvk9umZSioUvgk9JUVFVjh-zbe_1dhMYn2K895WLOL6E-qmOXjqfJSQ1husvPSXfy98I3X7yCWdaOrmLzoRIdWPpeC2L0nRX37hY7WgDdaqbeYylT0jP55FUwD46kk0j8FLdwBcmWS_PtMGcKobU8FX-66T-llOoKt3QoXirA_c_c5Vj_bt6z9JWDGT0ZzwF_VOYv8_ig2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصدومیت شدید مهاجم صنعت نفت؛ ویدیویی که روزتونو میسازه؛ فقط کامنت‌ها رو بخونید
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/22911" target="_blank">📅 00:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22910">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7334e55a73.mp4?token=OW1IXKrvEbLdVLQmzEzmUUnbKu8ESRqhe8alrGLMMh7GaaYxgLow_RChZ0-4wsr3rgbcyd6eJtp_sMJekpOdCL07WIOWC8GC7_sQDTqFZg4sZ-fLoqDtZ5HHCmQslfThuN0V9XiardApBU1DNDOkfsc2-qUdSd839UVLuqtN6gTP4Q-bH_g_g2BLEJJ4_HdORyhoM9dMRPGdcAxua36cDFU4Xi1qGITviIGOLCzSnplmd02c9Z9Cp84hdbIyOR0yGrtpZ2RmeuamGqbyRHW8ILDkONC3brXF3AvyaAHLxvqhIp9a6XAalHa6Iq-rbODFja4OLUSe0ZzYI-1nKuUByQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7334e55a73.mp4?token=OW1IXKrvEbLdVLQmzEzmUUnbKu8ESRqhe8alrGLMMh7GaaYxgLow_RChZ0-4wsr3rgbcyd6eJtp_sMJekpOdCL07WIOWC8GC7_sQDTqFZg4sZ-fLoqDtZ5HHCmQslfThuN0V9XiardApBU1DNDOkfsc2-qUdSd839UVLuqtN6gTP4Q-bH_g_g2BLEJJ4_HdORyhoM9dMRPGdcAxua36cDFU4Xi1qGITviIGOLCzSnplmd02c9Z9Cp84hdbIyOR0yGrtpZ2RmeuamGqbyRHW8ILDkONC3brXF3AvyaAHLxvqhIp9a6XAalHa6Iq-rbODFja4OLUSe0ZzYI-1nKuUByQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
امباپه27سالش‌شده؛هالند 25، اولیسه امسال وارد 25 سالگی میشه. اینم لیونل مسیه در 25 سالگی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/22910" target="_blank">📅 00:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22907">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c2e44c05.mp4?token=m3x9U5XqY09bJR2CuYX6XpQT4LEnDK8ipELXQdn9guZ1aSdB40I8-tOYeVTXOy76QdrgVWf8zJun3qeI8r99jGMs8ca83TXf83T85S93k8zMaSdmwIRM4zGBIC4L4Nbk2aPE-HDNKIAMTWtETR5Fyzd-bX93XREesqYU1FYrqFRglknebxjxvgTzBxQEvvaewSuLJS3kcUykFMagAdwt0uKxBfbqkOLG_xuO_GumtutKjk_qwVeTsUYGqffqKTT7bl3gUDFPKTwJenuyUcJMXh1XEGapnogTBPS9j_hlQI9c8uWLcAUliYJhIbNuFbbPGkTwqXzPSRFgR31ahjtxnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c2e44c05.mp4?token=m3x9U5XqY09bJR2CuYX6XpQT4LEnDK8ipELXQdn9guZ1aSdB40I8-tOYeVTXOy76QdrgVWf8zJun3qeI8r99jGMs8ca83TXf83T85S93k8zMaSdmwIRM4zGBIC4L4Nbk2aPE-HDNKIAMTWtETR5Fyzd-bX93XREesqYU1FYrqFRglknebxjxvgTzBxQEvvaewSuLJS3kcUykFMagAdwt0uKxBfbqkOLG_xuO_GumtutKjk_qwVeTsUYGqffqKTT7bl3gUDFPKTwJenuyUcJMXh1XEGapnogTBPS9j_hlQI9c8uWLcAUliYJhIbNuFbbPGkTwqXzPSRFgR31ahjtxnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
وقتی‌داماد مجلس خیلی فوتبالیه، کریس رونالدو فن هست و به‌هیچ‌وجه هم اضطراب اجتماعی نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/22907" target="_blank">📅 00:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22906">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/762477e8bc.mp4?token=txJCxg4MgiTcwryQShlNBvAu57QsSUAS5a3G2Tuvwp2RVCSpBSBY__KUUetsCQgI0AtpHJRt1SScSD-C0FJLX7FsSa6VEZL-K1H9NLE4oTROe3VHTMqwdtuwxYwU-PkgosL-NdcTIB_Hg4JCApoT7v7oXed61dsjAGzIIIF067EZ2S6sqreAHk5LXBD_Fi56rPi1Neklx_9L4n1DEj06OMLMRmhr0NV61ZoMs8M4HjLH71WW8PmVRzYSoTtSkgXIr0-VWdQsWUAnmeBGALyPv49nOXfxbl6gyB2HN61VxWmdZVvOyLXOweXpzrpnhBpplAbld1AZpoNvav9SjkbSUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/762477e8bc.mp4?token=txJCxg4MgiTcwryQShlNBvAu57QsSUAS5a3G2Tuvwp2RVCSpBSBY__KUUetsCQgI0AtpHJRt1SScSD-C0FJLX7FsSa6VEZL-K1H9NLE4oTROe3VHTMqwdtuwxYwU-PkgosL-NdcTIB_Hg4JCApoT7v7oXed61dsjAGzIIIF067EZ2S6sqreAHk5LXBD_Fi56rPi1Neklx_9L4n1DEj06OMLMRmhr0NV61ZoMs8M4HjLH71WW8PmVRzYSoTtSkgXIr0-VWdQsWUAnmeBGALyPv49nOXfxbl6gyB2HN61VxWmdZVvOyLXOweXpzrpnhBpplAbld1AZpoNvav9SjkbSUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ژائو نوس ستاره‌تیم‌ملی‌پرتغال و باشگاه PSG که در 21 سالگی‌فوتبالیست‌حرفه‌ایه، 2 بار قهرمان UCL شده، میلیونره و با دختری که عاشقشه زندگی میکنه؛ برادر در داخل و بیرون زمین زندگی رو کاملا برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/22906" target="_blank">📅 23:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22905">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QipUOygQZPsu1ZlxB3yUWB-eHHy_8E-BBVr73Sewm-Cp4rvNBbgB1wr2YZSemAFsH6QiwP3rewjoP6aohEoTlMHZ6ausGZ791cxM-o0y0QdABxatd6RgRvFNk6oXVkUPqxEu0twS9SphjIO6J3XzfdQUyBnRyANzVIFAUr02H4gx7iXdyKf8F3jYtUrQofSv57xfKy-EiKN1HwKoQBk3VJ2TQjitFd7tFakjpsQ6Nd2NhEZVhUbadGsGNeDEwKfhzFxG7Djer75sjHcWn4CO_o1H4auWuHEeKu3ugjzq2YcpLBxTEQp5ptFnYJajRmWm_qXMZPYxkNtQUCCfeBGFtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇪🇸
#تکمیلی؛خوزه‌فلیکس دیاز: مایکل اولیسه از طریق‌نماینده‌اش‌به‌مدیران بایرن مونیخ اعلام کرده که بعداز جام جهانی 2026 تمایلی به ماندن در آلیانز آرنا نداره و قصد داره راهی باشگاه رئال مادرید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/22905" target="_blank">📅 23:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22904">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUQOFVbE5c_Bi7Khawla5cxY_Md8qKrjuN4P7UatG9Dn0LIa_tnG3pkKT-BxJ_aox-3bmBTSqHeE_croK9UhLYuC4lsSkG2Sj2MnAqjmqnI9KiXd38qsLnRbGhbnVwaZirMS509orSMw_V-jex0BG6ERnT83p1rs5aLzrF57znswCLg3D52yWBpVVryuZUEn10nbhq9nOVrC9WxqdlDWzz8Vcp9Q6YwWtfGX0WN5hmbUoHfiVS1_fLx4lHzZRtSFVTz6VAQ-xXIgrM8YLLSZIL6LqJf6lLZMKBKxPD5B3yndxD50L90If7kEzpKEqjBTblMhdJWkJTum6OXt3en3jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق گفته رسانه ها؛ یوتیوب بزودی طی روزهای آینده بطورکامل رفع فیلتر خواهد شد و همین الانشم روبعضی اپراتورها مثل مخابرات رفع فیلتر شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/22904" target="_blank">📅 22:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22903">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SyCQUrqIBQJ3p8TTiTbpQRdPCedxZq7gEkS9SaNHaP8crKLRKttb07_LnNGPx-03kh4ikraiU6Z63kJkt6MwWnLt74thddZMU-jKB9NTzXuXxFFtZ-H1CA4hu3grMFRQ56QmgwmxidzwmM_XxgOT7tDiovaD2_ZOI3Zb2RRhG3__u5SFIpQdjENHncxzvwYHlOtogTesgEx6i4kdv5lKHdmhSe4IChGUpNhSWdcdfB3-6_1Uad9ZaACypvk4bAqltHrivwAWEsIYZkfZOF9TagQgxpK0uq70DckR87TYJWmJJ49oI3vQNDoqXxkz1DwQuwUkyC81EwASqWz21jvKoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌اخباردریافتی‌رسانه پرشیانا
؛ ریکاردو آلوز ستاره پرتغالی سپاهان که با شروع فصل جدید چهار ماه از همراهی طلایی پوشان محروم خواهد بود به مدیران این باشگاه اعلام کرده درصورتی که محرومیت او لغو نشود یا به حالت تعلیقی در نیاید قید حضور در فوتبال ایران رو خواهد زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/22903" target="_blank">📅 22:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22902">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOPY0rV8Iu_UiKixvJfWAqApe8oJN-DvD-gwUfyQ1JHem8uNWTr2_gWqvqeLbnCFkeAovhE_XG6ndGJGxZGrGc-5AUzOE2wZ4ew5NNPlKhcoEp24l5vsGTgxlJ5ED8ZcUgPla0voHCZ0m0pAr2N1rwfwcuFZolHIHxvKz3H6l5HyyBGUh8AzEr1ZEdgu2kf14FY3YcCqONDxZkdDKM03qIRydPu_ih_GQobC7o6czX5pXa9W728DMd5Zs2FVtCceSbIjNfi4CrEjXF94o0JJZ83mNyBkokQcNcr_SBQfEWL4pnqR1PozmvmeqjR1ibLAxIMTlsUjvHrQ0CZjMrcCdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ پنج مکمل‌ ضروری و مهم برای رفقایی که بدنسازی کارمیکنند. هرچند با این شرایط اسفناک اقتصادی مملکت خریدشون شاید سخت باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/22902" target="_blank">📅 21:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22900">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d07szMiy9vmDD8yy_SpUQFLDYXFWwbm9LjdULk40sUVVM3JigZ8BG4jFKUfLQUthwZPT6RmIBs5PCRLPqNsWYWC5syNgozhuANffMn5-grf-KG8mATZ-a28VndyAh_BvYLf7DVQecMK1lq5ykzSS2Uo4Xri_BU8ZGvBqm1FxoIn-cCCE0FghLcWxtH_ngbBACXI87-8tfwc_2-NbvDdgEliqDGomDzrjSK_D6zKY5wrJuBeuVnQ0wGt9Be6L8-eyh5ikoQS9qzsdTK7z7ndBDmhqnDh5vGAWjCEvnJ5tCT0dYsseyrR7KeHHNkb3om4bzzdPRl1FsxJTZmmm3JOXKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Quwg6pSkwLsa830GVpsg0il2KHW_5fyqMaAS_iyC8PNYHUlx298N7rjaxE_ZrfNK2Ii-JI7Hqjn6p5aeyPatThWT2KMctVaTg1krxvBeiRyYH1eiRV6te5g4qn9crkrtBcIoHg8IvQGRCBJxQcC3EIRvUBDWFtYDEl9pj8NRQGFCX3IweBciiq6V1-SOEpbQXNc5yZ22Ccn2r_knPK4nIqDnr3PXSPXlb6MxtpZdq4ZsZv8HuYf4aozYgE2fRYTQNEFJsmzwfIYieMaPCj1PsdmnWSdeYk_RR1hm9P_NDDQ1S8FHGZIr9fngCPaPCF61qGy57QxtrNBNawyX0DUvrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
بماند به یادگار
؛ یه ریاضی‌ دان آلمانی به نام Joachim Klement که قهرمان سه جام جهانی اخیر را با مدل خود درست پیش‌ بینی کرده، معتقده قهرمان جام جهانی ۲۰۲۶ هلنده.
مدل او که عواملی مانند تولید ناخالص داخلی، جمعیت، فرهنگ و رتبه‌بندی را در نظر می‌گیرد سناریوی نسبتا جالبی را پیش‌ بینی کرده: تیم ملی برزیل در مرحله یک‌شانزدهم نهایی توسط ژاپن حذف میشه، آرژانتین تنها نماینده آمریکای جنوبی در ¼ نهایی خواهد بود و در آن مرحله مقابل پرتغال‌میخوره و در نهایت‌ فینال بین هلند - پرتغال برگزار شده و تیم ملی هلند نیز قهرمان می‌شود. البته این فقط یک پیش‌بینی آماریه و تضمینی برای رخ دادن قطعی آن وجود ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/22900" target="_blank">📅 21:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22899">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgS4tJb3D-PgLGvXwvbg5ztsMbsnHQbpiV371sU6kc7hGh80CGdWHdJCdIvrHeNN3fZ4Oyly978BgREaLFbjrYYKhK88ivdm9vvs1_yUthUb5VmmmnxeaEPZmigkiq3XsyELkEeENjCRNtjKYYHZ-2DU2fjozXAq1T79mNT7_bvrYPGf1G6f8iE3n041GGDW6uHbAQGzmWKbjqmmvMQTuEFpijzbQ4IbE-N32XjcybbHMwXQVNDEGIoGS54-1O_LaE5dEdJrAQsJsbBUshW8Peu9g9G5KnHET8y00ATvCLFMTpUMr5TBY__e2Y-eAzqnONYLhWWJQ1UimIxJbKVRUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22899" target="_blank">📅 21:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22898">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pf_GmRZj_tds9fWVsOzzmpy3GbV0Jl6Qd8IpnBNSuCm6tHkPpLpefCnoj2H-IhDF_a4FFdPa7pnMVxAtOmQWeCCWTLu9_T3pX_7ChAh3jOiVYPzhtnngUGyTB8sEM6Io7zbP1c-6_y3qevZArmFVxkqtipfgQvI0PGw_t6EqhSjxhVAdc3yQRlJ1dSqe7dvdrblDLGu0KmjebqFdn7gieRblVIdfGdNePbCdjf8KObzpfzi0gYtxlrRMPcWY-HzP-AHbGNdbIboRgl3FYx_ML-_vBOLKjx3zVrKKlZREQnBWG8V2cmFH5Egz6OXklOJwtVDzi3k6eeO2eGU05b0wmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌استقلال با فروش جوئل کوجو به تیم نفتچی ازبکستان‌موافقت‌کرده و بزودی این انتقال‌ صورت میگیره و کوجو رسما از استقلال‌جدا میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/22898" target="_blank">📅 20:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22897">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f73008adba.mp4?token=WznarOc3ssvI4PmO8ryXuPIri3Gm_HCn9JpwZJQnN4s5Xcz21Pt_fzlV-1DNDU0V9qh4CURAab-gZvBr67wLHK4vj9tK7wH22lbH0jKZSY75qrSHfFDDQ3RsZRPJl9axwXfAeRfmsCXiOREkd6Q97yatdR-4uWAxjlo1rl1HHXJKudAjh8FdWWVY5lfTLKXPAzzvdVW7agYA6s-bNWsZgTW4Mrye4xwxYqjN02RPx8ul98QNNjFvf-fYxuLyTKjM12hu9UDkDYbnVwJS2C6Y4Oyshq2hYNnk8hoFKjIfNGh_iPSh_nfhS8YjyRMeZDo-fZxCzk7hFkZrigKR6suSTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f73008adba.mp4?token=WznarOc3ssvI4PmO8ryXuPIri3Gm_HCn9JpwZJQnN4s5Xcz21Pt_fzlV-1DNDU0V9qh4CURAab-gZvBr67wLHK4vj9tK7wH22lbH0jKZSY75qrSHfFDDQ3RsZRPJl9axwXfAeRfmsCXiOREkd6Q97yatdR-4uWAxjlo1rl1HHXJKudAjh8FdWWVY5lfTLKXPAzzvdVW7agYA6s-bNWsZgTW4Mrye4xwxYqjN02RPx8ul98QNNjFvf-fYxuLyTKjM12hu9UDkDYbnVwJS2C6Y4Oyshq2hYNnk8hoFKjIfNGh_iPSh_nfhS8YjyRMeZDo-fZxCzk7hFkZrigKR6suSTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبیکه‌مسی شخصیت‌منفی بود؛
آرژانتین ـ هلند؛ یک چهارم نهایی‌جام‌جهانی 2022. درگیری بین بازیکنا به حدی زیاد بود که به نیمکت دو تیم کشیده شده بود و این موضوع باعث‌شد مسی به قدری عصبی‌شه که یه نسخه از خودشو نشون بده که کسی تاحالا ندیده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22897" target="_blank">📅 20:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22895">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxcGq9zBdCTdYYfXxYp7gf9D1QPsgt7A320fz56BeSezb__E913aBpy8Pk-IItlqtbaJhIhEAScqMz6YJxOC42qJ7Wl5N_MPaAA-8r93rEPAJFIP2Ro_Xv9GC3MBnQZWaSjX8DTd1L-nNJ3gvns3_FlGdFngeJCCn_YcP5F_iEhOKmkuTMEhKqshoVrBD627FLsfmhVnjjO63371A4Cg0jyf9GUP9ujYNOZYGgBbOdvaRxJatLDSSSejueiPw866kurc-iyybUau5Ot2bl4HEVMW8STGpuAwrG3SsA7NF2XSnPEYcnR06HvyRe1S14sK_r-WMxw3K1E1UVs34fHMZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/22895" target="_blank">📅 20:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22894">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc1ec4c74.mp4?token=enr8tAXCSf0UrD6RjU70Axl6gPx2MJnbDudxszEK4KS_0LpzOcL0yBpoogxwZEMpTHi4FOdV6chf0kjG_NZN2msSMu-DQfXh19B2UsALojjwQLcHg3th0s8rEn6DHZibYI5laga_I9WUdzdqn0VrlYlDju5sXAbq49GMB1n-StmikuQS6Y5HgAZUhAWAURusvnUCxgU-ylGp9gP5vScNaF3jDDe9c2tZC2AAkHfgW4caZ55HXOM10ikh2OHoE9RLfxjBDxfgJl7AierKfg13oqeR02rUS77d6wb9vk4MTqLClUXksdFB9HjTipcdzI-SgcJKfM_SEM_wC9LLnbOs6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc1ec4c74.mp4?token=enr8tAXCSf0UrD6RjU70Axl6gPx2MJnbDudxszEK4KS_0LpzOcL0yBpoogxwZEMpTHi4FOdV6chf0kjG_NZN2msSMu-DQfXh19B2UsALojjwQLcHg3th0s8rEn6DHZibYI5laga_I9WUdzdqn0VrlYlDju5sXAbq49GMB1n-StmikuQS6Y5HgAZUhAWAURusvnUCxgU-ylGp9gP5vScNaF3jDDe9c2tZC2AAkHfgW4caZ55HXOM10ikh2OHoE9RLfxjBDxfgJl7AierKfg13oqeR02rUS77d6wb9vk4MTqLClUXksdFB9HjTipcdzI-SgcJKfM_SEM_wC9LLnbOs6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇨🇴
وقتی بازی‌های باشگاهی تموم شده و از بازی در کنار هری کین میرسی به بازی در کنار این:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/22894" target="_blank">📅 20:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22893">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6yiDNu6v07BuBQc46vE8_LcYt2GuUqGVI3t5tEi7SdiG_pvYwl8RFNc-c01_ho6JVq_uXXJz9mKys_Tlj7iAX6KhGmIMmsisoU9RLwiKv-kkk4F9vF-HN6d1sFhLp97CSK7UZilOkrfIQMWE64BZWSlncq_IcPd7QKxvjoci7l6n8GOs01zD6S_UFLx46ia3i9_Fx4Ci3H-1dlrR4SzvdwoXrbSxJXQxS418Ly_B9NHrZ1uMbhxlY1MtilyT8otlXTyoQZY7Lmzt-cB7N54ocPPdMB9iRvNbFV8Z7eKxU6gl60XBNMtvoB6z6-YvpLg1UOe0dgdtJ8l3nRvQ8LgBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه فلیکس دیاز: با توجه به شناختی که ازفلورنتینو پرز دارم به‌احتمال 99.99 درصد مایکل اولیسه این‌تابستان‌باهرمبلغی‌که شده به رئال مادرید خواهد پیوست. پرز این قول رو به مورینیو داده که با هر قیمتی اولیسه رو به برنابئو خواهد آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/22893" target="_blank">📅 19:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22892">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjN6fUikySg-QznQLY_gxldnyMBo83Mv_oYWN_yMT2oZbqOCM1Fjm_5x_m2yPvK4Slm-dJw60OBuJPIk4lRh_fqoKHnaBMKXqPtmhrFDbf3JE_Ro5ZoFy00L6-U8B-lXmeDab7Zp5QSFislgTmt6fj2Ida3aAkW4L-j-kWeuMu3bIeO-DMKGBQXu3g4kEhebuPL1M2KAoYsQ0OUG3sEKjp6eYguglsRDnZYyhlf-O-oFRTWznvepR6DTv_4hwCw6YgC3Xlb43TlzNlarQQ7KKcp3FIZ0GDkkA9GwAZN3L82uINQuDv6fGw9ZuiE1iXDWin0tl-Vn8W-WJkAlM1vzmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
در تازه ترین رده بندی فیفا و آخرین رنکینگ اعلامی قبل‌ازجام‌جهانی 2026؛ شاگردان قلعه نویی با یک پله صعود در رنکینگ فیفا در جایگاه دوم آسیا و بیستم جهان قرار گرفت. ژاپن بام آسیا ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22892" target="_blank">📅 19:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22891">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf50298d76.mp4?token=OAcqXnbRf19y6Ye7ClRUcPO8m_FoRwprsUibiQ8nRjDzYzYmORGnj8eMts1JTJjJ-X75ysHCkMAE375FcBDuoZh8MQQ7Ulo9UQ7QZtA-_xTcTfe86VQVV8nxf-aSlI7hKWe9Kkl0Z6nCUeh204P0K95EyZrRRBlURiR3cnhqbZjpGLTDbVIpR1R9VKuwOZ_FwbLbwVJZhs3JEBY4NePWexDJ0PIwjw4RkJE1TBOHixeLxH28izI689uVhZ6rR2GqisdIgoe-jL5lX-DpO6lPc8_B2z844aDZYv-o6KILWzawjk7Eyqe1xxdoIEJQi4ykewWLo3wZvYoYhuNGUjNsWF0Smu4voCiATleaPM0ImwVon-_KG2G40A5txnVacxSqL_AN_hW5wZD83N0aZmPqnekqDUaYKcYSTigI77tj-i9Msu5rX6E1poAepRBhDZopqBCnwzp2lJ8DxNDxqIktIeTu7EP4ouFcmU42pdjB_5d28WTmPWRtc1k6xy8oW1GkxD65f_WtFvoDJqMFPszdILbVdla9wwXGyD5lntyVIr4UqeVLxvt-23SWe3G8Sixe96MtHlv54UK56MK-r8ex2q4DbPngHSFVJy_dQ5VAN1PLCFNmPyS09aWD1NS6tvs3m11K90hrd9BkvOx5BZBlY2jhjj0e91qnPZ51neLeRtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf50298d76.mp4?token=OAcqXnbRf19y6Ye7ClRUcPO8m_FoRwprsUibiQ8nRjDzYzYmORGnj8eMts1JTJjJ-X75ysHCkMAE375FcBDuoZh8MQQ7Ulo9UQ7QZtA-_xTcTfe86VQVV8nxf-aSlI7hKWe9Kkl0Z6nCUeh204P0K95EyZrRRBlURiR3cnhqbZjpGLTDbVIpR1R9VKuwOZ_FwbLbwVJZhs3JEBY4NePWexDJ0PIwjw4RkJE1TBOHixeLxH28izI689uVhZ6rR2GqisdIgoe-jL5lX-DpO6lPc8_B2z844aDZYv-o6KILWzawjk7Eyqe1xxdoIEJQi4ykewWLo3wZvYoYhuNGUjNsWF0Smu4voCiATleaPM0ImwVon-_KG2G40A5txnVacxSqL_AN_hW5wZD83N0aZmPqnekqDUaYKcYSTigI77tj-i9Msu5rX6E1poAepRBhDZopqBCnwzp2lJ8DxNDxqIktIeTu7EP4ouFcmU42pdjB_5d28WTmPWRtc1k6xy8oW1GkxD65f_WtFvoDJqMFPszdILbVdla9wwXGyD5lntyVIr4UqeVLxvt-23SWe3G8Sixe96MtHlv54UK56MK-r8ex2q4DbPngHSFVJy_dQ5VAN1PLCFNmPyS09aWD1NS6tvs3m11K90hrd9BkvOx5BZBlY2jhjj0e91qnPZ51neLeRtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
شنیده‌های‌پرشیانا
؛ایجنت‌مطرح فوتبال ایران که ارتباط‌خوبی باستاره‌های‌خارجی‌داره؛ بار دیگر ارتباط خود را با خامس رودریگز ستاره 34 ساله سابق رئال مادرید و بایرن مونیخ برقرار کرده تا درصورت تمایل او رو برای فصل آینده به لیگ برتر ایران بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/22891" target="_blank">📅 19:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22890">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06fdcd2c12.mp4?token=smB8Q69qu1dwIHngb1O_y-cdsGPR6cOVhTJBJP0OQXrWquk-WsVyDide96zyuPCUfzx6nFe9ozUb7rmk_KbalWCTq41UGg42YjvjyC8-O8VK1QnW8-tlSTkkBu--otZW0cP7KxMczoyL2n9w9Qb1fofxqbetP8KN8BuP3gYMk7v4aeTKeO3BMPsibZosB5cikKXIE4Br-CvY5zGllXUO8PiiwxU3DEVMtF24GSXl2TAByyRE9Jf0Zy4VF8ChJ2GydoGP6SXYt1qP8oBctuOI2CMQhnHWtD4JMSXkA52H_R4Rzj-MSL11teIfvnXMDkQJeL-4lNG987imk1vWZVpz5z7raSdZJzQ_QLpJGRD-EZYl8VySJm920xW2lzpqcODsHo3MgRoi5V9tD3HNxs56UNO9jDzqVmYDG6vTEewYerfJO4Zg_oB0vJGoR3Gixx63p7vsEvGI0XcBB9QDkdY0e_gfiEdEIQUOH660OC5eKSzFCxkhP6bLKOoQd9lmG5jDgNpRU27hEVr0woy6-EJRJEWXnl7osYGI5q_xZdYCNdLt3hcjBWniWJKE2Vcub1jvJKe7YDdZnDP8nXN4ULj0wAJzWRcDP1y3_ahaf7HNFPfmPnyt3rkQtWuaTCJLg6b62XMbLlGoier_G8cQiaNBVnn1i0CVikoiuwwEGUm_QOs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06fdcd2c12.mp4?token=smB8Q69qu1dwIHngb1O_y-cdsGPR6cOVhTJBJP0OQXrWquk-WsVyDide96zyuPCUfzx6nFe9ozUb7rmk_KbalWCTq41UGg42YjvjyC8-O8VK1QnW8-tlSTkkBu--otZW0cP7KxMczoyL2n9w9Qb1fofxqbetP8KN8BuP3gYMk7v4aeTKeO3BMPsibZosB5cikKXIE4Br-CvY5zGllXUO8PiiwxU3DEVMtF24GSXl2TAByyRE9Jf0Zy4VF8ChJ2GydoGP6SXYt1qP8oBctuOI2CMQhnHWtD4JMSXkA52H_R4Rzj-MSL11teIfvnXMDkQJeL-4lNG987imk1vWZVpz5z7raSdZJzQ_QLpJGRD-EZYl8VySJm920xW2lzpqcODsHo3MgRoi5V9tD3HNxs56UNO9jDzqVmYDG6vTEewYerfJO4Zg_oB0vJGoR3Gixx63p7vsEvGI0XcBB9QDkdY0e_gfiEdEIQUOH660OC5eKSzFCxkhP6bLKOoQd9lmG5jDgNpRU27hEVr0woy6-EJRJEWXnl7osYGI5q_xZdYCNdLt3hcjBWniWJKE2Vcub1jvJKe7YDdZnDP8nXN4ULj0wAJzWRcDP1y3_ahaf7HNFPfmPnyt3rkQtWuaTCJLg6b62XMbLlGoier_G8cQiaNBVnn1i0CVikoiuwwEGUm_QOs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
5 سوپرگل دیدنی‌از روی ضربات ایستگاهی؛
از بین این پنج تا کدومش رو بیشتر دوس داشتی؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/22890" target="_blank">📅 18:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22889">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9o3HP1iBs9aqSO4SjPtBRhsOARv3Bd-IyqZd9Eb7qmsugZ9cxES4EC7k4G-whT6QjKBmIPx5Y73wrHkHwdBshCurDfyKkVH6XkcArYxDCJxV4EhlSY4OyMOO8p__63q7Pa1EZY0n6KNlHV9bCNCrguhpRoaSXF835stdIO7PSVycM5CY0zlDfxMF4mts-R546pUdbRFS-1sbXj3lq8RlGSxS_TZj9RSqfi9yBUze9pS4DRa8mco3zsHriEXxqH9UOmflqPOoVBFNW9sgz9XWPbyCRCpxzNuyHN0l-NENgVuwXZ_NnzG1dAWmNmoHQ9Tdm3UUBkH_dTbfSI-vxgrNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
در تازه ترین رده بندی فیفا و آخرین رنکینگ اعلامی قبل‌ازجام‌جهانی 2026؛ شاگردان قلعه نویی با یک پله صعود در رنکینگ فیفا در جایگاه دوم آسیا و بیستم جهان قرار گرفت. ژاپن بام آسیا ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/22889" target="_blank">📅 18:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22888">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fb97f5a2f.mp4?token=pgpqlPYYYGRnkYFR6mIyjMu9bUXtaEuZ7mzxpNGpOlu5aeUuNfa2sTBHfAp_wf0CHQFdidJmES6pWoCN-CYq2UHgZviuMs4OWr8nZiLxJh7RjuVR8lHvuAqYrefuCfNyYgrUSOF9R6MMPudZ4zA2098MSoD3dsfmKAyLbY76w0G70103zpNH4NpozXNaV3tcLWOcjE9lHSUitBANyFR0GdcElZYUOpvy3h3A9OfJbJMDv9py-7zgowrGUZRyAjV2tvRlhPX9tkLfo8LqDSXEnq31aetTWwQGkO9fbRqsK6HtSTQbyOboqHJIJMFkYwYEc4AhzM3oK2um972K7hjiTWHqXbavnQajh0cZR-XIqnyhL-4swvSgJSr_r3HvpWuxnHkLlRKVU-GusIR9We95hA2kOZE0yY8-ulyIosZdjkWwM2jh-CRyMx_EYvanNm-Ri6CXDfAWhZRNr5Nr-MajaNLYDQKRKMnnWWRIPkaDkJ3NucL_s5KT3DaCDcd5gC2RbRPS2_LlZ5rYAKn96MmkfFlvlkfRAC6KwmZFbuXC92pjhQP8RwK4RXUp-dFalWBpwQgvBSN8XZsd9SBLc3EV5EEA7Bl-xz3IBR6Mq850D2u6i3VXzxOb8y4ZlcLYVWGYDIZR91CWfqRdvoZQzb-E90Xatci6z6JwuFkTKUngIuY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fb97f5a2f.mp4?token=pgpqlPYYYGRnkYFR6mIyjMu9bUXtaEuZ7mzxpNGpOlu5aeUuNfa2sTBHfAp_wf0CHQFdidJmES6pWoCN-CYq2UHgZviuMs4OWr8nZiLxJh7RjuVR8lHvuAqYrefuCfNyYgrUSOF9R6MMPudZ4zA2098MSoD3dsfmKAyLbY76w0G70103zpNH4NpozXNaV3tcLWOcjE9lHSUitBANyFR0GdcElZYUOpvy3h3A9OfJbJMDv9py-7zgowrGUZRyAjV2tvRlhPX9tkLfo8LqDSXEnq31aetTWwQGkO9fbRqsK6HtSTQbyOboqHJIJMFkYwYEc4AhzM3oK2um972K7hjiTWHqXbavnQajh0cZR-XIqnyhL-4swvSgJSr_r3HvpWuxnHkLlRKVU-GusIR9We95hA2kOZE0yY8-ulyIosZdjkWwM2jh-CRyMx_EYvanNm-Ri6CXDfAWhZRNr5Nr-MajaNLYDQKRKMnnWWRIPkaDkJ3NucL_s5KT3DaCDcd5gC2RbRPS2_LlZ5rYAKn96MmkfFlvlkfRAC6KwmZFbuXC92pjhQP8RwK4RXUp-dFalWBpwQgvBSN8XZsd9SBLc3EV5EEA7Bl-xz3IBR6Mq850D2u6i3VXzxOb8y4ZlcLYVWGYDIZR91CWfqRdvoZQzb-E90Xatci6z6JwuFkTKUngIuY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
انریکه بال؛
سبک بازی فوق‌العاده و تماشایی تیم پاری سن ژرمن که ۲ ساله هیچ رقیبی نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22888" target="_blank">📅 18:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22887">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVhSmY2H1ixV7XdY8WMwjmUonvvM5EqS3ccnCAn4XY0F7_iwFXPKTrVDXK_TR4GOAy5jP6z3tRNX8n8u1n3A8tBUW-IPYr8KmmEeY2cAai0NDCSuKyWzuFqxVYjlg78wjQhx0Suc4ROjGwxGDIpoJzAVItlSVV64vAHNavqNUUII_jgxU-60yPw6r9sRGu0Jg3JVu6DT6LQJRFB7Us1IC6QFNl_21mFMDeEV5IWKDIPVrPmZMjoUZfi4p29j1nBQEOjr9FfQ716L0D83o_ABkb9jaZOA839GP_FhJJ9lA3DrJod9zXhqKvNzDOnLdW_PEZTHp9divTzfxN1agHyS6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌ بندی لیگ برتر بعد از سه هیچ شدن بازی گل گهر - چادرملو بسودشاگردان مهدی تارتار؛ پرسپولیسِ اوسمار ویرا برتبه پنجم راه پیدا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/22887" target="_blank">📅 16:57 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22886">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efa86e852f.mp4?token=LdrN9NCASuYvlF5Gbz9QTAx7w_NvxITVnHJd0YohoQnw9q_iImlOzyFFgOhZWbQpGkM_aFOfvb_mguxTD3PctafdvKDl82lyMb5bQJB9D35qYz_DVTJfcmIkb32KsfwC9ZL5dkJilXw5NiFrOUM1UuVDdvR_sXX02qgPuV3RkLqaDVOA16gtPsUDsuHDqqH1qvReU357cL7NgKbR1x_BjtOnWEbb0x4tZlBjyqyVQsvbYLj8lgkPmgUiXNi_Jnnt73pLKHFQS_HQbQgF1rRTzFJvuwTzdSiZPzipOthdj3mpgTG9seTEfcwlY4d-y7xhTIXM0Ip7ZH-d-Ul160iIzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efa86e852f.mp4?token=LdrN9NCASuYvlF5Gbz9QTAx7w_NvxITVnHJd0YohoQnw9q_iImlOzyFFgOhZWbQpGkM_aFOfvb_mguxTD3PctafdvKDl82lyMb5bQJB9D35qYz_DVTJfcmIkb32KsfwC9ZL5dkJilXw5NiFrOUM1UuVDdvR_sXX02qgPuV3RkLqaDVOA16gtPsUDsuHDqqH1qvReU357cL7NgKbR1x_BjtOnWEbb0x4tZlBjyqyVQsvbYLj8lgkPmgUiXNi_Jnnt73pLKHFQS_HQbQgF1rRTzFJvuwTzdSiZPzipOthdj3mpgTG9seTEfcwlY4d-y7xhTIXM0Ip7ZH-d-Ul160iIzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرد‌هاوقتی‌میبازن
🆚
وقتی‌میبرن؛ لبخند برای پنهان کردن درد و اشک برای رها شدن از سال‌ها جنگیدن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/22886" target="_blank">📅 16:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22884">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kO85vkIXvsCf_ILOdTO74KZmbN_ZlNLFKfHeBipiG4aqIWfWsQqicB5BuCcNzhzhijVf6ROaIAIT9gsXOVwqySoAMpe3jIfICK0xTBdGAECBRPEXxQHBlfJIvNtEpXjxYPmLLYgZGcnXesNFH6VnR3f7izOv8TJvo3Oj8Xf3iqYrzSMeQdn3ZNTMA77UgfsnBDJ9N6THQKOhs5VqicTOGTgfcPkvHNqIoi5zjmfessMFwGc0sgqwUELSQVkDgFeCD2fJWBSVdyTIXW8ZgdXjLy139ZHmHcYXvuAqQO3ZO_hMYc8FNDpyTyP7pt_g5umGpobyasmITvNw3BFT-3R-oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O5I24PBeDT7X5v7LRRLLggxuamsQLGpFnQhKr5DXC5eyGBjwpZ9LlJI32fS_9CXz0Q-_POgzOHDocARSOnzoZEocswkboZYv3qLI9-rVM20Tj2DHVm1euiRVxAb-tNF-gmY7b3lDE69DGels5LBMpP0ibIhtcaf8vOwtO8lhTe-s1qhTuIpR0h2MEejo9FpTRZZQrZ1lhSYSEbU1TfoLLnahzsPxLPTg2h8QjlYXuqixAoSewRevRzlN7hfP_O0DFff87mdCH-2h5oIYAnd0SL93v2RPtq89TaFmd81pGUwJoAcfX7-ABvsbsrWkcqJucekexNMxHScl_zaPanxyHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🟡
🔴
#نقل‌انتقالات
|شنیده‌ میشود آتوسا یوسفی خواهر آریا یوسفی ستاره‌بانوان سپاهان مدنظر تیم بانوان‌پرسپولیس قرارگرفته. آریا هم مدنظر تیم آقایون پرسپولیس قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/22884" target="_blank">📅 16:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22883">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LeT50jujXuZiNeOMWuf-3onqm23RUKMfVrNN69w52AvvFORsGd0seoJLmaUkhySmNDIbSEmkz5YfJq5Ro6DqyKtG_5Xiws_Y-sOC9Lt7RZqaOZsHQlB-hCYklfO5qLqP1jnhGw_ETjXEB8mgSWDkpkiHZ3g8wKFap_T0qzH-xIbzJivlnpm-wSkhayBwroqLjXJhvBTT0wnE72c3SZDb4ccqlHNeOVHeHVy_UsNri70FkqC4qtxN9BofqsWxe0_hNmwa6Pf3HFIaBKkoI_NvmYkB0okJFY8M1eCXI9QnpTP6bTtxh00twBhySEV9Q-YCiwlX4sStapoDnynkH0K2HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
#تکمیلی؛دولت‌آمریکا: به افرادی‌که حضورشون درجام جهانی ضروری‌بود ویزا دادیم. دلیلی نداره به تروریست های جمهوری اسلامی هم برای حضور در جام جهانی ویزا بدهیم. ما هرگز اجازه نخواهیم داد پای همچین افرادی به خاک آمریکا باز شود.
‼️
مهدی‌تاج:اصلا درخواست ویزا ندادم…</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/22883" target="_blank">📅 16:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22882">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUkpO8ZpM63cAujzf_wRQv3_qnLs1tzQdB1tp5T95wgZKjBGytxvDLRtwiJ7QQSJdecSbfJR91ajRb-c0M9ipoIWsQn72jcqzLAGMuzp6SXKKi3xSRRz017v4Oxun1pFQeUWGURJ545bVSVarVtTCZdAVwsjipIAhk8wFWBK-71LvwqfrD9SWenVT-UHWuB8SpLKuG3L8-DOrKy0lKEYRRlIBkFl5SfjHEcPiTyUwVPfGel7OMtcXnR2in6SRS02Cirb1SYptLvwyWlY3_0kwLRUJ4EyE6Nu3n18ZfkxVNjlVRzcpML4RlyuYIAaahdbMdm_4kkXeW0sRyX7acSDgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ باشگاه روبین‌کازان‌روسیه به مدیر برنامه‌های کسری طاهری اعلام کرده هر باشگاهی که کسری طاهری رومیخواهد باید مبلغ یک میلیون دلار بعنوان رضایت‌ نامه به‌ باشگاه ما پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/22882" target="_blank">📅 16:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22881">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvYYrPwxzQoFwjlFowiGgLr4XYQ0TfITKGry-OYoYntQxri5pRPttaJuud_LS6E6zxYEAOYUk5q-z6wzrw7-qIX1Mscs32cjOghH5fhwwFq8iFwrYMfIzxhl-nOZ_YYfKzPedaNScitqXt2J9cVOlhF8lkqE_0RiA899tSM6rpAhNZdIAvaQx-6Ovz_DiNvBxy2CXZJ1z8a1ccJeDv4xpdqQHjn7Mibxu0W0BkwvONoIOvry-rdaggH_pZmeMXBgAKyaO5cTit9mSTZdWaFIAeD5ZOM-REtnv99Md6qIWwrldKnTScZtqFCDK26-tZ3tPmRQD4guiSxazWOtlvgFTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نیویورک‌تایمز: ویزای‌موقت بازیکنان ایرانی برای حضور در آمریکا صادر شد. ایالات متحده رسما اعلام کرده که اجازه‌نمیدهد که بازیکنان ایران مدت طولانی در خاکش بمانند و تیم مجبوره پس از هر بازی سریعا دو ساعت بعدبازی‌آمریکاراترک‌کند و برگردن مکزیک.
‼️
همچنین‌گفته‌میشه…</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/22881" target="_blank">📅 14:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22879">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MwTq_AqV3SYW6p9lyOb_G_NEjDQWvDVbpm7smC-XjoZHxFE95sk4WsquLmHcMbltj0LA9TrxKExgY4dVeZb4Fb1jbf6YBYCJcY9hiFSaTq2LTuwgO443FG4JG6nZavFNNWvVQ3laDtJfb0MQR4vEi6NnNCRlQIYQgeSMnwJ5sAgSYlOegdvq_bs5usUBbL58V4lbC-CCLsuLC_GZdxbhq8h_N1bvv0X9ag32PladLe3GLEqTU94RdBJdOwkCk3pfzg4umbNQDyeyFALfoAGSXxF-UXrb0fKiey8cSYlXcNEKuUMSnsgOUiiXFsGr1hNSmGrC1f1Ms1PmHi9LBAcAUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IcTPW5KfMb-H9_KLAgHF6yT0MIY-wehG0geJEYF_K3MpvCl1SbnqC4FUfcAxR7WPDrSsxNMWly7eEuSuiDKCoswjTlvxFv_kFpYorGgtP5BBMpo49ABuOjcEDVhqbiuxY87ZCLmGoIQKiBoZldiAuVA7zyWKnyqC8oZfsG4eegQm-JpRA17yRgrmIl7XNxrHLUxXae_tVtqX8dVYpn0iIoexJMbsczmRZheKZ9voUJc6JKoweBtSOMD_kHOgwt12uQAC5Tdxe55oF_0iRRMO0hfXkeFNlFYpmPFpALiLBaOxTKybGP0j9pJF_OtQqQbZr2yyn_OCbg854gyuk8ykmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
خط حمله هشت تیم مدعی اصلی قهرمانی در رقبت‌های جام جهانی 2026 آمریکا
😍
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/22879" target="_blank">📅 14:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22878">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djOEXLeFoL8O7g3G-buO8SkqNPIgwAZ_9Y2kw-4FVgHPvpf2Aq2xU9mdCoPXW0UTFysJxDllIPaZ4JihBqbTBnSLL7tlAOll7cQNaljHFxJkS6_p_hAQB6iNHqXdhDRSueefJIMfQdpYvCSoCMhByjIXoGpd0Cgzx0ePm_GXkNoVWJ-hGuCxIGec7w2EfVqrjc7eL5DDfgwnPZmJcI3ul308rvwb8OHbeRho9IvZR5qEx8BQZGkgtlWmCoBHmrQcY14YfNjNQadrLg0YxkRgGGxs4yIukcoQ9t22VA6CX-lSrG0wweuHVq4fp0I-mF9kjfVMMU3XWuRekTjEmbJc1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/22878" target="_blank">📅 14:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22876">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZCihZyud7pR9I38D-jfiJ7kVzX1DWO61oymaxiC1_lYlzBfISKF1G3BfX2m3kb6tN_kCQnvltsbPC7SS6jA995dJkR4mT0N-QL-7eIj2Y19ot2QAMj60K6fuIdADzsvC6l-4Uk89Fkgr9mokwtbuMM6l7Wzwau06nhlp_RaZ_i47QL-VE_YeW1T1FfHO98Cn8DTkMhOW856EolA__r0kkT1H7hHxv0h3fuGFORZaUuQGRnjPnSechCmtdxzA9TXvWJPoepGKt_xNZFPBlDVsHS3R928UvGBzuIX_CBMRcf9k0r8eQA-32tPYnT6rgglvCOBGiTTEA1VXo--gu1LPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه استقلال با مدیر برنامه‌های موسی جنپو برای فسخ توافقی‌ قرارداد این بازیکن‌به‌توافق کامل رسید‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/22876" target="_blank">📅 13:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22875">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=UWOHWi_8nN9_3R3UbZVR_X58F6MQbReYJd8tEgGiWI2BHmswXHlZBdr2MEqlvLqJQ1dapQYRWeK9fj5QgzyMT5GqpcB3VRZcSptQ42hWcFYfzx38OCj4c1Sqi-JfN9oySWzyCuH5jPlzR6EfSkQbwCFnP_NhRvdXKEdYjQdQ5uK2GaltQb8VGpL9kZahixhbbzu3vEDhgxWPkMa13s78WGpUJYoqN0lV_axZzPHMuXGxE3SBgbBgscIGrv6Cx4i2VeSQwBAgJi3UhRWGnPPfr1yPhecXP7pdhQ_MzJWtmf0GoNZSajE15rf3fFnCDSTPh1X7SWqByUK_BmzlLzYE6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=UWOHWi_8nN9_3R3UbZVR_X58F6MQbReYJd8tEgGiWI2BHmswXHlZBdr2MEqlvLqJQ1dapQYRWeK9fj5QgzyMT5GqpcB3VRZcSptQ42hWcFYfzx38OCj4c1Sqi-JfN9oySWzyCuH5jPlzR6EfSkQbwCFnP_NhRvdXKEdYjQdQ5uK2GaltQb8VGpL9kZahixhbbzu3vEDhgxWPkMa13s78WGpUJYoqN0lV_axZzPHMuXGxE3SBgbBgscIGrv6Cx4i2VeSQwBAgJi3UhRWGnPPfr1yPhecXP7pdhQ_MzJWtmf0GoNZSajE15rf3fFnCDSTPh1X7SWqByUK_BmzlLzYE6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
نیویورک‌تایمز: ویزای‌موقت بازیکنان ایرانی برای حضور در آمریکا صادر شد. ایالات متحده رسما اعلام کرده که اجازه‌نمیدهد که بازیکنان ایران مدت طولانی در خاکش بمانند و تیم مجبوره پس از هر بازی سریعا دو ساعت بعدبازی‌آمریکاراترک‌کند و برگردن مکزیک.
‼️
همچنین‌گفته‌میشه…</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/22875" target="_blank">📅 13:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22874">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lt6Md8C8kzTHIrIpPa_YMU5vu4TsYFxbq0Kjg3qUpBYLqFxD3rP_NjRw1PRNY9VVJpOq_m3SQkrSHd49P5AxQEjylgk3Fk1LypfZ3sk02ykYhtqa6P2G_iWJ7Dqz_SlW-oKp_mG449mQB15qSh9Lm-bW7hjuMPKaYenuNNRiK32fqiarjW_3SuGe3SuQPH9aqeYsmcMThdMG9qpD1ykeO5mQ6d2cBqE2AH3wz5U4LUywFZ9c3EfbXzY1R3IBZidslomrf20hbeLMOokHtc2TNTrhRUlFnF8WuktLVVaSDuLLtVY5t5HlJ2X0U2vnOZslrpP891Z2_sZ7ZrdmYTfCKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نیویورک‌تایمز: ویزای‌موقت بازیکنان ایرانی برای حضور در آمریکا صادر شد. ایالات متحده رسما اعلام کرده که اجازه‌نمیدهد که بازیکنان ایران مدت طولانی در خاکش بمانند و تیم مجبوره پس از هر بازی سریعا دو ساعت بعدبازی‌آمریکاراترک‌کند و برگردن مکزیک.
‼️
همچنین‌گفته‌میشه…</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/22874" target="_blank">📅 12:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22873">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nEymLvHmjeUcvPpCgFQ8-n0pZqLu2LyG_YkPF8gpgSrIbuUUQ33rGvkGFwvxP1jSF7d8iqOKPwbOXBGnsSfRkNSi3H40UfZX_Ajzr8DVBVZJWjimhJuTfR1rr6kTxjaumeYKGOzkWMg1tuzIE_srYKluu1mSXnN1kv4hljuYtA66mFZboJNeCJoO9yL74RlkSWyAPBwszpMLGqcevtZsyGe0-TgWiXGV3Ad3oLCgQ1tDQu4O6Ery1s5HOaOxLsAizpZUN9Pu7dbjL17c3CX33vfaPkaffOfMRBD_GCAby5GlzJJz86aHCJePdgiJo-NwrzjVLRul1wBTdo5ufn-OQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟢
#تکمیلی؛باشگاه‌آلومینیوم‌اراک: در روزهای اخیر مذاکرات مثبتی با یکی از اعضای هیات مدیره باشگاه استقلال برای فروش محمد خلیفه و بهرام گودرزی دو ستاره جوان خود به آبی پوشان به توافق کامل رسیدیم و به احتمال فراوان این انتقال بزودی رسمی خواهد شد و پول خوبی به‌باشگاه…</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/22873" target="_blank">📅 12:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22872">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKgVyT7mF-d69gU5zKx6PWC3pMencMEq11xB8fxrnO87UFcVVXCWLM_1zWtgveLqQk-Ml-PqcO81JWL8yCdM8F0XorJ7GVqL_iu_FmsRNOxisS0mgZw4h7rcZaBggCL4Hb-JaZwnoUZNvW_YvTZVNx7MHcIijBRm-4bXC1G8h2EoIsYqL8eCxFKdcN-b8ftbi4Na-bnMrh4U3vyTx6unEPYibPIuTZhT4yQaVHoYx94lj5z2fPlZMhQLI937EVYmZ1ZUxtb-TlkLmrKSH0ZqIPdVwqtmH6JsrJfzQLHg19eBnUt-rgBNnx4QYJJql3uA1L6E_UkB4EF0_FiDcc-43A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیست‌کامل‌نفراتی که دولت آمریکا براشون ویزا صادر نکرده و گفته حق ورود به آمریکا رو ندارید.
‼️
مهدی‌تاج رئیس‌فدراسیون، مهدی محمدنبی مدیر تیم، هدایت‌ممبینی دبیرکل فدراسیون، محسن معتمد کیا مدیررسانه‌ای، مهدی‌خراطی مدیراجرایی، مسعود اردشیر افسر امنیتی، مهدی ملک…</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/22872" target="_blank">📅 11:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22871">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/shmvV62UGvWCLdWGvBr5i3mlaOElKoTD4be_N6paCvK2tog1DUEtY7Z9oK2kXATSThCjn6k6ufnC0dW56rcqY3jOO0Vx1ZrtFxZAhqBAbKh0Y4byzfMQQIu1dck1RV_Vom80Biga5L2QxWTANQX0ESNGUXbpewZeiPozgh9e4xgzdHiX9tXfk8Rt80f1yVgu7t6wHN-SoA_Ee5IvWi6NLG1fzuSZ39NMmrPpuUHPsGzWgS5zmxt8jTneAr4DR_1X00HZCgKyO_C5MG3fYj0EqdgakzyUZ7lqJ3yRxDvF94yMSjdN9IjneM7EzcZfGcizyHdMIewR-2ClGC5-l3L3VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ تمام رسانه‌های معتبر خارجی از غیب احتمالی چندبازیکن تیم‌ملی ایران در رقابت‌های جام جهانی 2026 به دلیل عدم صادر کردن ویزا از سوی دولت آمریکا به دلیل خدمت در سپاه خبر میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22871" target="_blank">📅 11:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22870">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35d2a48cbb.mp4?token=HO9WCFz9vG4Lj5mVwPKzWO5rFJweKxOVjkBjU4qoUatHh-6G2woJ0mRJBDK4wY_sU7J6V2p8s6A3t1th55EBxSENHVR9tbQ9_eDAKKWcFFKrrkG8BgTTd-Grt9bpLLJ24LTkW43b9zP9xNlSxbXOJ9ab1cUNx52fAThpK9pveOc6hPx1pKoWbFEwkD5RBIOWAPN_1phFwxFjt33sBOGcNhwX-uOpnJ4hAtB1Nirr_xBZ1YdVjgSlMss_4KD5-g0aqh2g_uM8Gx5A38eH7UP_6TY6BQdGPZWWJg5CIogq07XVjD2H2kzs4rP4n23CvbvtZLo5AYSwE23XwcCim9yGUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35d2a48cbb.mp4?token=HO9WCFz9vG4Lj5mVwPKzWO5rFJweKxOVjkBjU4qoUatHh-6G2woJ0mRJBDK4wY_sU7J6V2p8s6A3t1th55EBxSENHVR9tbQ9_eDAKKWcFFKrrkG8BgTTd-Grt9bpLLJ24LTkW43b9zP9xNlSxbXOJ9ab1cUNx52fAThpK9pveOc6hPx1pKoWbFEwkD5RBIOWAPN_1phFwxFjt33sBOGcNhwX-uOpnJ4hAtB1Nirr_xBZ1YdVjgSlMss_4KD5-g0aqh2g_uM8Gx5A38eH7UP_6TY6BQdGPZWWJg5CIogq07XVjD2H2kzs4rP4n23CvbvtZLo5AYSwE23XwcCim9yGUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
اجرا‌ها و موزیک‌ ویدیو‌های شکیرا برای جام‌های جهانی ازسال 2006 تا 2026؛ کدومشون بهتر بود؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/22870" target="_blank">📅 11:48 · 16 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
