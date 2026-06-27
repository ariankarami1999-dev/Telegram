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
<img src="https://cdn5.telesco.pe/file/d8FMdeVjuv8LA-TrPQ7By5mi-gnmKO12JacByxiSGIREAuZl3OlK04IMWDx-HoZEd_-0vE5wW5hETgz9GIji41EZDVnR2FVOrPZy70IvNbEFVwTDQPfO7CkY-LkbehH9SwEv7ti9RPtVx-LDdO_0dWWP9bQIbfbUDtCJ-lqmpyiWDkYGMbZ52WPMKlfYtNGn3XMYt-YzZ6d2uXrERmdikaaM_knNDpjcCXfibgqACK9XL9tEgOqZLE0yViOirAroPwjhxQtu2O-cU2KtXn2MPq5ATvL8R4pLTCFW4dLLwUToIgWV-FBKzIqmrkat64yHmpqHnpR8H5U96IleP3o4Sg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 697K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 09:53:06</div>
<hr>

<div class="tg-post" id="msg-96340">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97e7871462.mp4?token=fR7-GE1cpTGmgz3h4bupssXvaJOx0V8z_5G9y34Atr6iEisogY4BkVguRXGYMtjKjyil1QaT5Z9VNIUsMm_kpKkwAv998erw9dVQ8mARj3CGFuzK_xchGQhnfNjNqpTV4Xukzt8YpSDJDgK0ZFlhdWVdIe5hetFlqfeVGmY7fK6FxFleJB8h3SzAC8H6hEB7Sm5pfhNILS3PfOtyK3Km_F6SbP9aKhaNl892kY4j3JsZt6u46GSF3gIF7qNnzQX7HpcMlvOispLAOCfvUAMhbYvJ5DyimR77fqzGy6CFqk1b9Idp31w81IKtIzCeJKUqoNAG3NGSWnkokl58PTJVpFL93_7V8wU8MoKlgfMc5X1I4F-V0NAsfUOmAflDENabtvI6-dSzcZWxtjPyb40shgIcWASiDZYoOYC1oMZbPRkRMIDj9mjsbgp4MJOE0xEkuq_-fzrONfWumgLo1zNO_Ia1SG8T3afpEFv9Xhh6Z11rWvOXsId5dOpMeAdzFNR2ui5iL70QA4ue7oBRNVNyoUqkbLSXhB16hW7GQxvSIcKL8qXJnTMabkIsxzYRBROINTPYhwPi__Y6YveluM6MkG03P6Uq9GPCmo-DjxgFEhKkE-Qm_kqXbbB_g24JoeLCzLNOBsm73vgu_93Qdq_7baCSDZXyLUHEUnJ7cKGdPJk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97e7871462.mp4?token=fR7-GE1cpTGmgz3h4bupssXvaJOx0V8z_5G9y34Atr6iEisogY4BkVguRXGYMtjKjyil1QaT5Z9VNIUsMm_kpKkwAv998erw9dVQ8mARj3CGFuzK_xchGQhnfNjNqpTV4Xukzt8YpSDJDgK0ZFlhdWVdIe5hetFlqfeVGmY7fK6FxFleJB8h3SzAC8H6hEB7Sm5pfhNILS3PfOtyK3Km_F6SbP9aKhaNl892kY4j3JsZt6u46GSF3gIF7qNnzQX7HpcMlvOispLAOCfvUAMhbYvJ5DyimR77fqzGy6CFqk1b9Idp31w81IKtIzCeJKUqoNAG3NGSWnkokl58PTJVpFL93_7V8wU8MoKlgfMc5X1I4F-V0NAsfUOmAflDENabtvI6-dSzcZWxtjPyb40shgIcWASiDZYoOYC1oMZbPRkRMIDj9mjsbgp4MJOE0xEkuq_-fzrONfWumgLo1zNO_Ia1SG8T3afpEFv9Xhh6Z11rWvOXsId5dOpMeAdzFNR2ui5iL70QA4ue7oBRNVNyoUqkbLSXhB16hW7GQxvSIcKL8qXJnTMabkIsxzYRBROINTPYhwPi__Y6YveluM6MkG03P6Uq9GPCmo-DjxgFEhKkE-Qm_kqXbbB_g24JoeLCzLNOBsm73vgu_93Qdq_7baCSDZXyLUHEUnJ7cKGdPJk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🏆
این یارو هم از شدت خوشحالی سر گل دوم و مردود ایران نزدیک بود جررررر بخوره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/Futball180TV/96340" target="_blank">📅 09:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96339">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🎙
میثاقی: اگر بازی در لیگ خودمون برگزار میشد، چون هوش مصنوعی و تجهیزات پیشرفته var نداریم الان گلمون آفساید نبود و برده بودیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/96339" target="_blank">📅 09:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96338">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03b41f5781.mp4?token=opl5hkDbMMBWreOm269f8m_3O1qW1607lvZ3_CwXb-FCEVNVcn2QNRzwXEJBTDkJ9gY1yGsxZD2ZVvzQ7Ds2WPExs-xUHrAagRLOvjjHnkKW-IlpP4l3iQhjspJeL4Uqm-GEW-ktXzd51lC2K-6cdIL3HwPxNKgbVGky7TqvGgbR6pNm5LbFfioxV4RYoAPKCSGajppmc7ACu19nQGTsGUB22M81A9yMyahU-kHuSbo7eLk9Aft9-gqxS7yqXJGRPSCCnAVG4LKakgYC64CxHM1e2ny4i4g7YvHG5HCsv0ldSvcz3OiL6XLFG6n7I3mSHr_SyHSAlmhbOfd0Wdw6sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03b41f5781.mp4?token=opl5hkDbMMBWreOm269f8m_3O1qW1607lvZ3_CwXb-FCEVNVcn2QNRzwXEJBTDkJ9gY1yGsxZD2ZVvzQ7Ds2WPExs-xUHrAagRLOvjjHnkKW-IlpP4l3iQhjspJeL4Uqm-GEW-ktXzd51lC2K-6cdIL3HwPxNKgbVGky7TqvGgbR6pNm5LbFfioxV4RYoAPKCSGajppmc7ACu19nQGTsGUB22M81A9yMyahU-kHuSbo7eLk9Aft9-gqxS7yqXJGRPSCCnAVG4LKakgYC64CxHM1e2ny4i4g7YvHG5HCsv0ldSvcz3OiL6XLFG6n7I3mSHr_SyHSAlmhbOfd0Wdw6sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
وقتی وسط سیاتل تریاک ناب گیرت میاد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/Futball180TV/96338" target="_blank">📅 09:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96337">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdrwaaTm8YCgQZZ2uogvtaK_35xs8sxyDDo3TIeO1NooB1_t-337PIIVU0e9nZskDMhwVBZqCJdclzHgrfSbjv-LXhN1b2ndoNpFw14dwNwTyWgRv4vrHyjRojedYIfL5WuWXEfIHY3AbU7K-BqL9RBLG9-osHE4oIXRKO9i01yvZBW-xuYPdlsFRQudNf2Fji7pf2L7XQkd0AqTpkJh_Lj-A96HeRY9kffAUMPe_EGzyeMohX1qtVWEglyC70AiuKeB43J-HEBsE2Gb8emcugqEIWyCUqUdNQFuHO4guYkbrh_8kzSzj3-C8MBP126lYigXg7qei2Xp6kTDV0jCIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اتاق var بازی ایران و مصر
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/96337" target="_blank">📅 09:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96336">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NG6WfDXaQfyNpuE1ofCJb5I5qIfeFdSXBj-L9-vDgsfjzg6kSLWyp-9PetEx_sBpajUvuhFDYVexjXik8AbEqAkhNADk5kAbpBVsQotFTFQ10VzndC64T4_M6OWXh-3jxs5J4pWp16ZGyaXJjisz_7kJNNl0tQxZfPeCObmoERtiNFHzT00BcrTEiKWBIRdxRM4eGfvvaByaZ3bfI1ao0Hoi9tb_DVK8GhrclB0OMpPWhDdksKlu4bY8t9P6pJBvVClRnCE4q91XjaeZmB2lGR5i0P-qWLYLkYv1TGAGXlrEoEK7mBzpbCSxdw8vADbCm5WAqnEk7WMjfMmvBEIn9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤣
🤣
تفاوت‌سطح از این عکس مشخصه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/96336" target="_blank">📅 09:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96335">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57704b3690.mp4?token=TyFdyfw334wbLuDdV5TW0h4G-TEXEt_VfgsuoiIZhBzhuRAPTmUJa4AYbboL2WPi2gZXJRTHKOQth13Gt2PQ8J_yOHpECRLAqyxOo4pBzuNw_mx7R14-aA2r3nsvxl8O5O18Zje-Iojedb8yjI02IlMdr2szFR_bGs-MX6z2KqmGhV87jor7O3TZHg0dzldK2WsXSVN1EEfbT0RySP-zBcyiYHUlLnVwA53ak5xRGF9ZWZLMNW2Q9p56X6vACQYcwtMn5c0t6oke6bbOvJLtbCt45cOgZ9hoHHT_ceGJJYv-2whADqsIu5GsZSTOB8kW1yM90j6BzMauL2GHz2h3rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57704b3690.mp4?token=TyFdyfw334wbLuDdV5TW0h4G-TEXEt_VfgsuoiIZhBzhuRAPTmUJa4AYbboL2WPi2gZXJRTHKOQth13Gt2PQ8J_yOHpECRLAqyxOo4pBzuNw_mx7R14-aA2r3nsvxl8O5O18Zje-Iojedb8yjI02IlMdr2szFR_bGs-MX6z2KqmGhV87jor7O3TZHg0dzldK2WsXSVN1EEfbT0RySP-zBcyiYHUlLnVwA53ak5xRGF9ZWZLMNW2Q9p56X6vACQYcwtMn5c0t6oke6bbOvJLtbCt45cOgZ9hoHHT_ceGJJYv-2whADqsIu5GsZSTOB8kW1yM90j6BzMauL2GHz2h3rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
قلعه نویی:
شاید خدا داره منو میکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/96335" target="_blank">📅 09:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96334">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmR0KwTnxaVLzvGNdDoNSuVNnOdqzQObb5P80jLeM7D1GjOQaM91aLBjdLD557e7LFAk8jMIa9vUBb6XYAdU4Dv71Ko5BG93uaZgB13EaGRwRncAPZvkyuqxBU5l6ChrWLY1K-wEA5ykbvawGSyEyG0JN0FKHrZjHaoeCZ4SQH72NiW83MR85fC4CTlbBmC73fzFO007_VeA5-po9PrptIP_T8zURUuR2eWgR0jxN-Safj0KggcCsTlTSB7F2vrbzOgk9ATyjYw4HkRtE3TYQJIdR1Jkz03rE3VtGFWVjfPruLbRXdJNxcOSsNmio2OlGCuutvc0r4tIPjY1eUnOYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یک حالت از سه حالت رخ بدهد، منتخب ایران صعود می‌کند
🇩🇿
🇦🇹
گروه j بازی الجزایر اتریش باید برنده داشته باشد.
🇺🇿
گروه K ازبکستان مقابل کنگو شکست نخورد.
🇬🇭
گروه L برد غنا برابر کرواسی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/96334" target="_blank">📅 09:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96333">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ztlh4B5_PEqsGdPWTpZY_aHlXUb7TZUCFDHlZdsw7Xt7GHnUyrcJFWIRRy3yAGmPJn75P33NogWhOLKlRPtpCVa0Qx2c9ol9Z3WTYuTwjMNMqzWPbQW8FNdykpZdvf2t-O2od7yZBGncZXVxUsYrEk07hG3UwlAXzh2oVnuX7Y2rD2WE3J2d1xSDFh3rOC_1Tb5yrMLIiTewS5Rh6crmkQaM1eBGnJXOG35xWmQf2tPL_Ki1H3kWf8W5ykTjstl4Hzzdz1t113QIdfv7s38wJMthYP4CqH9KPVHFiR2-P50Rq6cS7MA6gMANR7PEqCfPWtjgl9XxjGlZR9lpIbKz6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
جدول‌فعلی بهترین تیم‌های سوم مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/96333" target="_blank">📅 09:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96332">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHYwkwHK_jjqAaMWxbfs1CErAz3cSNkJ2_6ab8d-SwxuX3BduyXgRDYYF15jIQz-kd5qPw5wNl08H_ipRqlA2t-Fk-x-3kywo2weedQBEgaNmVngYFNKAs1CrXCCFk5QqnrdX5nwF_C4ToSfRN2V_GoY3S3--f0mqlOFKI-DGtBKTGShR06kCPsv8GlIHmUePmGM1N2lXknQe19KaCi2oSddbwToLuQPtb6makL8FW2Enswu_mxpDUW2ZL8MqNVCqnwfDbzgeXPysYMQ5hXWmJWzEbqcx4_QaL81aYAKxoUL19OvRK_unn8GKcNyS9IUaS6NEsjmmdAmdZnqzUubYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خلاصه ی بازی واسه کسایی که خوابیدن ندیدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/96332" target="_blank">📅 08:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96331">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MMN5OaVt-VYBJl2L6naIvRV2fnFnIk2qGTxIudr0mUHrWPiDEbullveZZgLfn4taSR6siH0uBwApB3Saw7th2L9ToJv1QzeaRDhg0KfwUW-TjjFyGiduVKqJOISyTFbT2iX8pfmZxiMXYxS_3l51-WyA0xuKsJeLvjS3XxJXoDfjzLd_2ZyNw5406GPeMAmrETtzIx-5qiPGDqwcBUjVUhHQQaP8HEJt6EBALOtmvYpw4Xft1xJZ6ucVxkgQB2hI3GtUr0O-f6Q3onUDblXqIt0CgrtH-F4LwOq0fec9zNA_yGuaNQc4J8EHLCERx2mPNwd1pDj1Zjxwvp5MqOLh4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
سه‌بازی حساس برای منتخب ایران:
🇬🇭
غنا - کرواسی
🇭🇷
ساعت 00:30 بامداد
🇺🇿
ازبکستان-کنگو
🇨🇩
ساعت 03:30 بامداد
🇩🇿
الجزایر-اتریش
🇦🇹
ساعت 05:30 صبح
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/96331" target="_blank">📅 08:54 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96330">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKJvVbD9JMcffL2sMoKNZ2BHbPT3Zrj6VTdNXosm32QfRJlfv6ZtKIDecW_1SQ7bJTvIppK1e5iv-SMAXyOOZSB0079YmQFTAQlEWx4AGHhU9M26cDHvs-YGQ2TxGYUPcP_GHoEAkAUkMksbWDLJq6ludn4ous1F3PzUV4Sv-_IwsTY6dVfo120-_kYuFynDGozVu8Q5gqPXTQ6Eka4cAFTkr8un1M--3xA5i9S7hl25lsHw200DxyyUatdcdbRc7WgdJj-hOxdxCtoReBVxPkYLNuJyZXKFKi2zHLUb7n_yFZ4bQujp2Is6KkybH72SUETxBJHhvmxdGZlXLBuIxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤣
جلو جلو ذوق کنی، کیررررررر میشی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/96330" target="_blank">📅 08:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96329">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
یک حالت از سه حالت رخ بدهد، منتخب ایران صعود می‌کند
🇩🇿
🇦🇹
گروه j بازی الجزایر اتریش باید برنده داشته باشد.
🇺🇿
گروه K ازبکستان مقابل کنگو شکست نخورد.
🇬🇭
گروه L برد غنا برابر کرواسی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/96329" target="_blank">📅 08:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96328">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
یک حالت از سه حالت رخ بدهد، منتخب ایران صعود می‌کند
🇩🇿
🇦🇹
گروه j بازی الجزایر اتریش باید برنده داشته باشد.
🇺🇿
گروه K ازبکستان مقابل کنگو شکست نخورد.
🇬🇭
گروه L برد غنا برابر کرواسی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/96328" target="_blank">📅 08:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96327">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2BPYuZdCHuji-Wn6Gp9ImtXWCJYpkrF4O-AgVeaYL3cSBcKFfCedpt4pHffqBGVPv3q4aMu1SZJNY-upEPAhM7QRQKT1TnB2Vm0nz3oa1CI7nlFCOWM-Cf25D1wnvhS3ab5lNcb0qvmLw-xHgblC44B-7ChvqAK7oAEDF9RQyBWac631cuJatuxCCbvMxmnoNf8CeACCfJnIrC59C4Gyr1ifurAmXNlLk-T2lKll281usClNsgsgDLy4fORHep-WzwIVFn2NTEFpU8LWHAFFGHrycA4IdeYU79L1HrHa3dxh10JVSLAom8BzyOM-y3tRXxzscg2IcWpkE8Nvdle-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
مرحله یک‌شانزدهم نهایی جام‌جهانی
🇪🇬
مصر
🆚
استرالیا
🇦🇺
🗓
جمعه 12 تیرماه ساعت 21:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/96327" target="_blank">📅 08:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96326">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTTS8DF2rnBAg-A8vyR89CG-8J3wlZy5qcmJE-Eo067nuCND1xcAxTV41B4Iw07YlOr3ahbsRf4XN7IpC68VHSvUu99zCe1dFvHTHh_Kio3X67mw8TdTtq744Ht06ctbs5DiABarEnJJWJjtKhj1Ldkceel-_Dv3akq1Szt9KxRoSKaIULk9XOhJyDfAI6aEtTLRG9__X0XIbE7GT42ZoXk6kStCkJ0YalkafwTsZnVtHShK81LVwqJb14PqWUgzXFVMPY4fiAa7qrxsqbNot4HINztrpocTr7IOzcx8RXgosQiwpI8jJXPNrDrvsqRpxh4KpiO-8incafTmoAkjFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
تیم‌های راه‌یافته به مرحله حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/96326" target="_blank">📅 08:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96325">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZ7Ts01mLxNULB8iA4TE5uBkUSTirQ7vn599cZUYZM9tbEsuEwuOLNhQ_oDFCf6HMQUoyXTwpe4_XS73yCft0WKhlfFbloBbIe9mxSlXYtOpaHl2TArTY70dFxWc885V2-52KsNEE60w8hg5Xi8dN457nsWr4hfI3e573xyJnRFJux3if6UO1DK4mCHfofQWzbyPCJnu-RLfpp2Qh7kpCqS1y75tIlw3AZKlf7gZSc99FVQyyDv43Y7po552a9z0_H2hla4TVLOv_cz2Yvu-hHiiPFyo6mp2RyuF7EBCl4gkUI7SAU7c4dJtorjv63FblQrEmDkJXRTXmJBZzlV38A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی؛ بازی کثیف و زشت تیم قلعه‌نویی در روزی که برای صعود نیاز به برد داشت؛ منتخب ایران حالا باید منتظر معجزه باشد
🇪🇬
مصر
😃
😃
منتخب ایران
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/96325" target="_blank">📅 08:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96324">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🇧🇪
تیم‌ملی بلژیک به عنوان صدرنشین راهی مرحله حذفی مسابقات شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/96324" target="_blank">📅 08:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96323">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zanyo73ie3fztOgvX5pTm1i1njJdFD1BRsIq0bxWkrJ0XxDYslmMU-g_HM-aTCnpgo1Kb69INLudzlsXAvJVcSNWPYydKoMQ0XaAzYgypb_tk8FPRGOGxd17nnHZBesfsccaW2pYnFK2wG0FTyVmfjzMRmMQIH3uYdOrKLb2ZdRQpi9SguXMUlnIAioz5MSH8biEuaGNAT29_kI7hVrRJjsUFuKGXawLImsslJ3GKLroFauUyfhosegoLt0S3PCoqJZJdsn7o6XH-TfmIZR2bR-gFXOK_kSHObhSRQWsfwpHcoWT4Tf91whfBMZDlJpYoe5myRNYECLqqUJxsL4jag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
گل‌مردود منتخب ایران به مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/96323" target="_blank">📅 08:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96322">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/37f359e5c0.mp4?token=fumWQx2A2G9RtHgza5l_XNEfiT8S-xEZTQBfptu90O7sdg1oPJP3Op6bVT9IqP3n0wihzWiWh4bMjpwcqDfzTzOrUU78GwthA4WlFjuBD-qZiPVlaxjtWwzndWepH-h8xuRUcOVPedHs7jO42FbGB4SyEfyOJ_xiCmmYoLrDIwjLgVilqnSMiGGreaTskYhSIvceNZ5X4lidDCrk0uZ9T-nC4-GMIMkiiU3Gu_BDd0929nqMR46Pb9nfBTQg3RlSusuGw7GpOsuMEi6ZrUDmPkLHT0LW2iIPT9-m9hWjuXUycBw3EcmfP5P_9fZcwcMHUZscHxIL3XF43tWx00AObg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/37f359e5c0.mp4?token=fumWQx2A2G9RtHgza5l_XNEfiT8S-xEZTQBfptu90O7sdg1oPJP3Op6bVT9IqP3n0wihzWiWh4bMjpwcqDfzTzOrUU78GwthA4WlFjuBD-qZiPVlaxjtWwzndWepH-h8xuRUcOVPedHs7jO42FbGB4SyEfyOJ_xiCmmYoLrDIwjLgVilqnSMiGGreaTskYhSIvceNZ5X4lidDCrk0uZ9T-nC4-GMIMkiiU3Gu_BDd0929nqMR46Pb9nfBTQg3RlSusuGw7GpOsuMEi6ZrUDmPkLHT0LW2iIPT9-m9hWjuXUycBw3EcmfP5P_9fZcwcMHUZscHxIL3XF43tWx00AObg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
گل‌مردود منتخب ایران به مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/96322" target="_blank">📅 08:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96321">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">گل رد شددددددد</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/96321" target="_blank">📅 08:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96320">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">گل رد شددددددد</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/96320" target="_blank">📅 08:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96319">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">بنظر گل مردوده</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/96319" target="_blank">📅 08:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96318">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">صحنه رفته وار</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/96318" target="_blank">📅 08:28 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96317">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">شجاع خلیل‌زادهههههه
🤣
🤣
🤣
🤣
🤣</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/96317" target="_blank">📅 08:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96316">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">😂
😂
😂
🔥
🔥
😂</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/96316" target="_blank">📅 08:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96315">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">گل برای ایران شجاع</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/96315" target="_blank">📅 08:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96314">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ایرااااان زدددددد</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/96314" target="_blank">📅 08:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96313">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">گلگگلگلگلگلگگل</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/96313" target="_blank">📅 08:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96312">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">۶ دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/96312" target="_blank">📅 08:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96311">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">جهانبخش رو آورد زمین
😂
😂</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/96311" target="_blank">📅 08:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96310">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">پشمامممم چی گل نشدددد</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/96310" target="_blank">📅 08:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96309">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">بعد بازی قراره رسانه‌ها قلعه‌نویی رو دوتا شکم دیگه حامله کنن منتظر باشید
😂
😂</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/96309" target="_blank">📅 08:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96308">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">منتخب ایران بخاطر وقت‌کشی داره هو میشه
😂
😐</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/96308" target="_blank">📅 08:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96307">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">قلعه‌نویی تو این گرما چرا کاپشن پوشیده
😐</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/96307" target="_blank">📅 08:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96306">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fb07e42f4b.mp4?token=qcCeid236muFqsYbYi7jKEnnWbtwmF4jwblzBmtCQOJKWKX8wOpn3sX5nr74bomI-yjPAS1BHSZ9L_h1IIlyceUArvFFzegZBjcuGzppGzHyGcrPfxTP3Gph65IsIQOD9MGLzWk3jjM-gxBducWtRlHVfTX5TLqS6n_dx__Md9tqDyQ77gnTk2TiaCs3XTti__A9Qwq_OMN5YgrcPXTnU-gCRsrADhwcWUXOyZmBMKM_kR0dK2c3ppEsmdqEu4rnlOum_a2ZYMDQHKpGq9PTej2cQA8SF38tGPoW9uX-OakU5lHksCXQLzLWzxkQnFMoVXqjx7OrEWp3mHY9XxAT5w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fb07e42f4b.mp4?token=qcCeid236muFqsYbYi7jKEnnWbtwmF4jwblzBmtCQOJKWKX8wOpn3sX5nr74bomI-yjPAS1BHSZ9L_h1IIlyceUArvFFzegZBjcuGzppGzHyGcrPfxTP3Gph65IsIQOD9MGLzWk3jjM-gxBducWtRlHVfTX5TLqS6n_dx__Md9tqDyQ77gnTk2TiaCs3XTti__A9Qwq_OMN5YgrcPXTnU-gCRsrADhwcWUXOyZmBMKM_kR0dK2c3ppEsmdqEu4rnlOum_a2ZYMDQHKpGq9PTej2cQA8SF38tGPoW9uX-OakU5lHksCXQLzLWzxkQnFMoVXqjx7OrEWp3mHY9XxAT5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌چهارم بلژیک به نیوزیلند توسط لوکاکو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/96306" target="_blank">📅 08:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96305">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">مصر صعود کرده کیرشه
تیم قلعه‌نویی ۹۹ درصد حذفه داره وقت کشی میکنه
😂
😂
😂</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/96305" target="_blank">📅 08:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96304">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a3fbcca7fc.mp4?token=g8XqZNsvYjhRDtr74wgKD7h7AQ-mFL08g4oqJchNZFjYCrQcn_ZD-5rmRk_CC7Gcqpb9rxKUOPft_sHhUMwSVZ8l8inxzitnm_au2hmhlUVLVg5VCxhncZM4nSM_u7_8fMPMZOu5NFLD-55NVmCXC2h0FdjKcIBCw2qTelD4WP6zpsy7uWb4M_F_VOmOw0bm31YmywFcsd9FrGi4_dpmffKRJQni0kGj9Kn4Vxn5Sk5icRov_SCMDPb5qeXp9AbxYq5LHQ5GkMiKcF9FmUOaC0THvRYCXFp-fJkjpkcNDejvCxLw_NQgk3-TqiCMjX-4mVGsT0n1cM42vWJn6kmQFg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a3fbcca7fc.mp4?token=g8XqZNsvYjhRDtr74wgKD7h7AQ-mFL08g4oqJchNZFjYCrQcn_ZD-5rmRk_CC7Gcqpb9rxKUOPft_sHhUMwSVZ8l8inxzitnm_au2hmhlUVLVg5VCxhncZM4nSM_u7_8fMPMZOu5NFLD-55NVmCXC2h0FdjKcIBCw2qTelD4WP6zpsy7uWb4M_F_VOmOw0bm31YmywFcsd9FrGi4_dpmffKRJQni0kGj9Kn4Vxn5Sk5icRov_SCMDPb5qeXp9AbxYq5LHQ5GkMiKcF9FmUOaC0THvRYCXFp-fJkjpkcNDejvCxLw_NQgk3-TqiCMjX-4mVGsT0n1cM42vWJn6kmQFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌اول نیوزیلند به بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/96304" target="_blank">📅 08:18 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96303">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">بلژیک چهارمی رو زد</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/96303" target="_blank">📅 08:18 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96302">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">گللللل</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/96302" target="_blank">📅 08:18 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96301">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">سعید سحرخیزان، آزمون، کسری طاهری و ... چی کم داشتن که نیاوردی
😂
حداقل میفهمیدن مردم که بازیکنای با کیفیتی هستن
دنیس درگاهی رو آورده بجاشون که نه میدونیم کیه نه بازیشو دیدیم
😂
😂</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/96301" target="_blank">📅 08:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96300">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">گلگلگگلگلگلگا</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/96300" target="_blank">📅 08:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96299">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">گلگلگگلگلگلگا</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/96299" target="_blank">📅 08:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96298">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ژنرال داره تشویق میکنه سربازاشو</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/96298" target="_blank">📅 08:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96297">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">کارت زرد برای عزت‌اللهی که داره زنش از خستگی گاییده میشه</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/96297" target="_blank">📅 08:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96296">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">طارمی از تیم‌ملی خداحافظی کنه سنگین تره</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/96296" target="_blank">📅 08:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96295">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tke0Vmlr-glCE-kPABpOiqoB8Jv0WL4fEQx4-giSuhmxWzaaaUoTbj19BPSGHNQZ-Q6oa9Wr51gZBQWF3uhIvyDAzK8qDSgnf8UBm_Rc-lUCGGnNKsxJaZRFusYDi4wKfP3hBuKXsnH11xyEkzI_oBtnNTfHl8gdlJXaZedctlBEsGWTziwY04KhkPWHqdFhQZz4YWBNXrmmafubCVPyg9oUmmB0kLeuuMjv2CbrRyxZ3QbdLl2sfELnMi7yQ4vEUR2KeWmbHSlxCouZAGaulzzqexMCs6n8ioGXeqcuDyPCQBAMyqvzuET8eN-vVm0KsIflGuio-1_rwRBSSd3RyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
گویا صداوسیما هم دلش رنگین‌کمونی میخواد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/96295" target="_blank">📅 08:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96294">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">مصر داره پشت سر هم تعویض میکنه بعد قلعه‌نویی که میدونه برد میخواد کاری نمیکنه
😂
😂
بابا اون قایدی و علیپور و بقیه کسخلایی که داری رو بیار مردک رولکسی</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/96294" target="_blank">📅 08:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96293">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3b7e026fb5.mp4?token=X_85-aeaZagJdCQ__iPnzxWkZFZa8XhIqUnTWIx6hwdwWl8GcFe7xZr9ncTUEL94D5B-8bIhCC47_vANAKmwQZj-kWO3RA-fhUmrUHKoKOYXtxGNtasMbhX8RVajx_229wpnKKlqA5NYFWyf40AmTMFJsFYqClSY7Jg9khh1CFfCbiaZBBhUn3oV2OJV-VX8IjduBirHHrINPMC7bDQw31bKxm5VVDuwolrjKtOOe40JGgHduZyO_xHSIXK-GNY62mkraaiDUSn_9B4PWUINwIWCqc_mqQPZTFlUGvnvewrH2oXLn2szJjVj3n6nf1PLWPardd4Qd5IXXjfm-JyAwg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3b7e026fb5.mp4?token=X_85-aeaZagJdCQ__iPnzxWkZFZa8XhIqUnTWIx6hwdwWl8GcFe7xZr9ncTUEL94D5B-8bIhCC47_vANAKmwQZj-kWO3RA-fhUmrUHKoKOYXtxGNtasMbhX8RVajx_229wpnKKlqA5NYFWyf40AmTMFJsFYqClSY7Jg9khh1CFfCbiaZBBhUn3oV2OJV-VX8IjduBirHHrINPMC7bDQw31bKxm5VVDuwolrjKtOOe40JGgHduZyO_xHSIXK-GNY62mkraaiDUSn_9B4PWUINwIWCqc_mqQPZTFlUGvnvewrH2oXLn2szJjVj3n6nf1PLWPardd4Qd5IXXjfm-JyAwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌سوم بلژیک به نیوزیلند توسط دیبروین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/96293" target="_blank">📅 08:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96292">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">بلژیک سومی هم زد</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/96292" target="_blank">📅 07:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96291">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">نزدیک بود مصر بزنه</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/96291" target="_blank">📅 07:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96290">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">صلاح تعویض شد</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/96290" target="_blank">📅 07:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96289">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6ulDHYa8AA-KWM9bvNp_rOwWosZ67PldQsgWUHw66YZhsbWmdrGcgcZuOWjMNEs9BIKoAvkFxwmSkaFmy_eS-BTCFWK4uFAvQhIgyvSxRIfNgWI27ybS26G4ZTMS7MuGHcV0FETNUEkdXmFvo78T2SBGHWIqcsTlJQivm1Z6RM4UFltNR5YBIDhamZz7mR3_WWaAgSSITIGesR-FLj5mfwEkQniddFp1EGInzInTELfT_OA0ENuiNOXBGguywNcyK1G_rFD32_hZ2VjuADU9AWLjlJKAZgUQr1X1i8OFAf7xSWD9u2qvSeguU7i8Vzk8oFoqeFiDV7ALm9tEIuGTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😐
تصویر جنجالی نصب‌شده در استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/96289" target="_blank">📅 07:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96288">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سرمربی مصر چقدر پیش فعاله</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/96288" target="_blank">📅 07:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96287">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">چجوری اینا گفته بودن حداقل ۴ امتیاز میگیریم
😐
😂</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/96287" target="_blank">📅 07:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96286">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نزدیک بود مصرررررر بزنه</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/96286" target="_blank">📅 07:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96285">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/96285" target="_blank">📅 07:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96284">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ایران گل میخواد بیرانوند وقت‌کشی میکنه
😂
🤣</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/96284" target="_blank">📅 07:45 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96283">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f272e1c110.mp4?token=mZQav9Zjv38zdxQhmoySYCter4dsOlWqO4GreymkQoB9_TngVX6lRhhSmzzhi-Qsg8V-v1BxrE_AdkKAhgeUPOCD4OqyzYMoRnsig-2jD0i77AsVA-Ih3T1osyYDejxR_lL4ugSoioFtHAC2V_cZXPmWNsMay7nTPWF9flgroy-Rvef0m6GgU_xPNlo-L7uznTRsLlEROuVi3bxd69CUkd9Y9PqE9Q7eM3GEEImEkMtcABud0mCTWMGBoIjHaNQCX38ED1pVEfudbkmtIZycTJHU-P9VkIb9E-DRQJmvQ_eohFqzRTmSW0ANqxRr1RTO95uh6SYCSnL-3Yw37sc_Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f272e1c110.mp4?token=mZQav9Zjv38zdxQhmoySYCter4dsOlWqO4GreymkQoB9_TngVX6lRhhSmzzhi-Qsg8V-v1BxrE_AdkKAhgeUPOCD4OqyzYMoRnsig-2jD0i77AsVA-Ih3T1osyYDejxR_lL4ugSoioFtHAC2V_cZXPmWNsMay7nTPWF9flgroy-Rvef0m6GgU_xPNlo-L7uznTRsLlEROuVi3bxd69CUkd9Y9PqE9Q7eM3GEEImEkMtcABud0mCTWMGBoIjHaNQCX38ED1pVEfudbkmtIZycTJHU-P9VkIb9E-DRQJmvQ_eohFqzRTmSW0ANqxRr1RTO95uh6SYCSnL-3Yw37sc_Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌دوم بلژیک به نیوزیلند توسط تروسارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/96283" target="_blank">📅 07:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96282">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">تروسارد گل دوم رو واسه بلژیک زد</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/96282" target="_blank">📅 07:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96281">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">بلژیکککککک دومی رو زددددد</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/96281" target="_blank">📅 07:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96280">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">گلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/96280" target="_blank">📅 07:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96279">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دنیس درگاهی رو کسی یادش هست؟</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/96279" target="_blank">📅 07:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96278">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDzgQkQ1VW7DXW77SnOsYXB_6NtK5-TaSLSrRCpBn-ns6SIZuJGw1HgJb4DkfL1ylkWQuFJ3hK2C0BcOReb2bSP1lL7nFRLm_EYG82szxvcfwhf6bZFV4daavLcOGOzoZLX2P_kOOftB9jCbrpXQ8Ufuw56wJ9Fivp8sLjIphUJrFq8N1WPK3fE1D9sFlwIp3zkd8rI5Zh_ddjTzHV6ggNXkHKeUGvy49tDDB75cWMJstzIm25ggu2J8ytNxno0cRTpvXgUZulrt-0HUTi_KnOF4UmkLrqwMLEV8af-M64wtxQ3N-t2gWkCUYh7tam6buf5Vc_DWUTFLiKeCx865Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
از اون فکتا که دوست دارید:
- رامین رضاییان: 3 گل تو جام‌جهانی
- رونالدینیو: 2 گل تو جام‌جهانی
- زلاتان: 0 گل تو جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/96278" target="_blank">📅 07:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96277">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">عمر مرموش هم برای مصر اومد</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/96277" target="_blank">📅 07:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96276">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">حردانی بجای کنعانی وارد زمین شد</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/96276" target="_blank">📅 07:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96275">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مرموش قراره وارد زمین بشه</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/96275" target="_blank">📅 07:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96274">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
آغاز نیمه‌دوم تقابل‌های امروز</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/96274" target="_blank">📅 07:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96273">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XESIvb89CFb3pbi6mH9bA8gI_CvRmrVoWUByJaNXt2o1OEI0p13IAXqFU8e4Jk6kzrGMi-u7fHg9tYPTOEzMOp68fwEcuhPjnW5_4V0Iz9V_Yxz2vZSYoVg_JpKIftcbaBOaaedcYItkkdW_0yuIjP5ILYBKprV0SnLUupwfJd3LmD-tOpVm8e--UeHwWJV3_1ydA-Iq0f15xD_FV1El1qg17h9WSUKMnvRikrUmFxJfG5LKphASApKxb8UKS3cqFBwv1hR4MvrsUulMwNlmI_3ejl62KmnlxlWrSmOfGZvj6CVXSPDfe-8TCJBamfFvZuwOU1EqHSCXVPvrhV9zMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار کامل بازی در پایان نیمه اول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/96273" target="_blank">📅 07:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96272">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t3F3Fks1M-nQ7BBHvqTOwcd0iqlneh2kwSIA0o4MJZnoXe9nI4OtP3eF73sIOw62QfCetJtAlHeC8tQ5qWKjnm4Xwk0MrHhyK-Fgb6CMzYcL2DDbUERstyALCJcWopnpEYP6CSZtMuhEvXBHkgbsZmmN8NrUeaZv_pZyGZeXYakz0MRmlrW4clxj7WmLay8HNnjmSZLf5Lz_40f19cW0Fb1YPcuTHnC4xqGvomeRdzDY26UOP3WvGRkFuCMVonJkn3wjgRDow5nrcrdiveEwadUsoH1bsnoSzzkllb2bAUDc6VITx5C9vfQ3q0dFPikZfBGeP2rGtvSNG3S1M5t1iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمره بازیکنان منتخب ایران در مصاف با مصر از دید سایت سوفااسکور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/96272" target="_blank">📅 07:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96271">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🏆
پایان نیمه‌اول مسابقه
🇮🇷
منتخب ایران
😃
😃
تیم‌ملی مصر
🇪🇬
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/96271" target="_blank">📅 07:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96270">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7ee8935bfb.mp4?token=h3Ryg16qBdstphD4IZi9g_MrLfxDZfht6ZarU7Plthn_hIpx94ctl_kNUNG_U0caYhT5uOuUbxB6Nm5QiZAaY0opogbiiE5GPDDRWim2PfqRRTmOSEsO0zU0z5E50iCFSMS68lRm7i3ZP4bd3MiYTdwTjFbfnbyAjduf8PEooreJn51nAYoPd_1Oo0eI1ov09aRfLDaHxLBJ0rCegBf6nvHo8O2NgNQUspYapNVUqfFVj7ifoXAPtJpqRbuP7BlL3JxXd4gbV4whAguGW5czlko1ViJtpd7J5k6NGSrI_cRqbrS8venziCeR2UNZq6KOG9d5eW46qPEFrjNt9uTbrDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7ee8935bfb.mp4?token=h3Ryg16qBdstphD4IZi9g_MrLfxDZfht6ZarU7Plthn_hIpx94ctl_kNUNG_U0caYhT5uOuUbxB6Nm5QiZAaY0opogbiiE5GPDDRWim2PfqRRTmOSEsO0zU0z5E50iCFSMS68lRm7i3ZP4bd3MiYTdwTjFbfnbyAjduf8PEooreJn51nAYoPd_1Oo0eI1ov09aRfLDaHxLBJ0rCegBf6nvHo8O2NgNQUspYapNVUqfFVj7ifoXAPtJpqRbuP7BlL3JxXd4gbV4whAguGW5czlko1ViJtpd7J5k6NGSrI_cRqbrS8venziCeR2UNZq6KOG9d5eW46qPEFrjNt9uTbrDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌اول بلژیک‌ به نیوزیلند توسط تروسارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/96270" target="_blank">📅 07:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96268">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">تروسارد زد</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/96268" target="_blank">📅 06:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96267">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">گلللللللللل بلژیک</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/96267" target="_blank">📅 06:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96265">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ro8Na5g0KWp05Ops9PXiSdZgfhFMfRUOiNh4BvU28B3ztmU942ty7t6wrdwq3Ox5RfU9RNAIWYifRBkpu2tCPS-7wNxEhbDrG7i570dnfiA2lBQ7_VAEMltAcA6XPrOCP4HVzk-IaWmmXee7q1r8LLbfTje2cNWOskIIxtFDmRJhp57GrU8KmBG74JwI66JVyqnh4RHgnVnQ9_XF2olvu1trpULNx1cCQwuYBzDqD6hNSoQUaZNP-fpLDgo46gBvSfBXbdzJhMDkhUrb4MsL4r__r1tKgTDvuiIcEM7qe02Q1c4EQ-e0eDOpnJEB0EXdSDJfY0V_SDWhf5PKhW40nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاشیا نگفته بودن رونالدو تو ترکیبشونه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/96265" target="_blank">📅 06:54 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96264">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">داور رفته وار برررسی کنه</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/96264" target="_blank">📅 06:53 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96263">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">برای بلژیکککککککک</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/96263" target="_blank">📅 06:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96262">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
پنالتییییییییبی</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/96262" target="_blank">📅 06:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96261">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
پنالتییییییییبی</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/96261" target="_blank">📅 06:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96260">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اوه اوه
کارت زرد برای بازیکن مصر</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/96260" target="_blank">📅 06:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96259">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hlfv7U_PcWeA6-xnwH8SaFRxWg6QwTEoiC2iGkI6EZqLQgscoGdtpxazTycNloDvxPmQN9c-C-4GN8g9L7hQyXzsF9ZyB24KpolZgaR4pAYbiyvJzf4ZKQBy68_iILaAmhYBvV8i0l8isGhp0wXbH4N1vRLQkzhuE8Fa927XcOKL-HEtEyINLzfAxumRUejghwowbozPLx5L04UXytXYrE72jE9bjBf_Bh0E1ZpBtg8XhafbLawzNKragojvP1yjIJhOWNeWCvwu4S4nJOPY-vL3CYVnNolw3kpT2glIjBk85kZckwK1dBHUrDDOii4LdD8YMw8yF-zx5KteEiZVJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرز حرکت کن که وقتشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/96259" target="_blank">📅 06:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96258">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">رقابت رامین با مسی امباپه دمبله هالند برای کفش طلای جام جهانی
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/96258" target="_blank">📅 06:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96257">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
گل‌تساوی منتخب ایران توسط رامین‌رضاییان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/96257" target="_blank">📅 06:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96256">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/df56d1c2f2.mp4?token=CDA3zov9aA1Z1WfZ3dtoSxm-HeKeN9kXJlSJEKS5bYMtkyDsZiF6y9EY8xXTM67thgDzK4BcECTb5mhWBm4rE6XhZk4eJSX9JHOhzD5DROkYr2edqW35l9GzNW2OmRrAQra4d0jY3yNG0DvgG2ri8Zt56jN6cbj2zAV1cd1rHegf4h-I_Pdo2ngEeFOfLkXX9oyfX_BpsyeV1AvM573V1ftwpzTsW5AdkBYhCs4QSErJi2L1xpyNuFTNJDU7NEyTBvNOaI3_TzdJU0CXX6QAI0vPTddz5tywLLOiYstiNTTOtITlRdHt-ewOsT1ZT3j2YXdzz7SuEiqqQBjEDRbl2A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/df56d1c2f2.mp4?token=CDA3zov9aA1Z1WfZ3dtoSxm-HeKeN9kXJlSJEKS5bYMtkyDsZiF6y9EY8xXTM67thgDzK4BcECTb5mhWBm4rE6XhZk4eJSX9JHOhzD5DROkYr2edqW35l9GzNW2OmRrAQra4d0jY3yNG0DvgG2ri8Zt56jN6cbj2zAV1cd1rHegf4h-I_Pdo2ngEeFOfLkXX9oyfX_BpsyeV1AvM573V1ftwpzTsW5AdkBYhCs4QSErJi2L1xpyNuFTNJDU7NEyTBvNOaI3_TzdJU0CXX6QAI0vPTddz5tywLLOiYstiNTTOtITlRdHt-ewOsT1ZT3j2YXdzz7SuEiqqQBjEDRbl2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گل‌تساوی منتخب ایران توسط رامین‌رضاییان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/96256" target="_blank">📅 06:45 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96255">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔥
🔥
🔥
🔥
رامین‌رضاییانننننننننننن</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/96255" target="_blank">📅 06:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96254">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">منتخب ایراااان</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/96254" target="_blank">📅 06:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96253">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">گلگاگلگلگلگگاگلل</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/96253" target="_blank">📅 06:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96252">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a4c1184f7c.mp4?token=S_puN-lCNb0kFk_rDoXfNnnpoP9FZy9sdCi7JiOo8bkf_2KX-DnUqi4HwkyKlaW5ybneBY6C6ibYTmbRFRvEOUxnvW5CYoXO8y30EzJyBxLeGHo_3F0KBrghUYeYzWWfohxigmIf5Z8dutTxIa3R7o435gMWS3YAfopB7vXoFlJi1K5kfrNH92elHJKR0T00xuMvGmfb9Fe5hh5iZmObNKE4Ceb90y8wTITgiqEtuZ_FK8hk6w3-MDTgZmVN00DGO6z6_PrG-dVmB86Ro2u1JuUyVc_8gNh2QzT4gg7CgeIYKFO-8yeZPKz0plNmLWWx6QoGZz2IrOeaq2h93V2Z2w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a4c1184f7c.mp4?token=S_puN-lCNb0kFk_rDoXfNnnpoP9FZy9sdCi7JiOo8bkf_2KX-DnUqi4HwkyKlaW5ybneBY6C6ibYTmbRFRvEOUxnvW5CYoXO8y30EzJyBxLeGHo_3F0KBrghUYeYzWWfohxigmIf5Z8dutTxIa3R7o435gMWS3YAfopB7vXoFlJi1K5kfrNH92elHJKR0T00xuMvGmfb9Fe5hh5iZmObNKE4Ceb90y8wTITgiqEtuZ_FK8hk6w3-MDTgZmVN00DGO6z6_PrG-dVmB86Ro2u1JuUyVc_8gNh2QzT4gg7CgeIYKFO-8yeZPKz0plNmLWWx6QoGZz2IrOeaq2h93V2Z2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
پنالتی از دست رفته مهدی‌طارمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/96252" target="_blank">📅 06:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96251">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">طارمی بعد جام‌جهانی ۲۰۱۸ قصد داره مجدد دست گل به آب بده
😂
😂
🤣</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/96251" target="_blank">📅 06:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96250">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">طارمی زدددد</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/96250" target="_blank">📅 06:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96249">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">طارمی زدددد</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/96249" target="_blank">📅 06:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96247">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">تایییددددد شددد</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/96247" target="_blank">📅 06:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96246">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">برای منتخب ایراننننن</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/96246" target="_blank">📅 06:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96245">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پنالتیییییی</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/96245" target="_blank">📅 06:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96244">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/831cc909f5.mp4?token=KF67bI_mXQl35JmnOWtm547z3WgyLwUVtOEfYNzXlXkNkRLll6IUibrREv7x7H2pXCH_5dQmqHNrxgWNxDlbzQen0MMjHg-O2ofeqn7i_-PaBTc4LhTuzgXRJna7vuVu9mmoAUGx0hQHffPg-E0lok-NcIxOSaVzDdCohPMA4MjZW8_jlgpcoyS4Ty9j6nN_Fie2pTo9LSDg_8XxefzWuevtzqFudoB3HUuAQWe-AcrHLWgYjDP2GrO404vCt_ADQMlQztpvtDhjzjurlBD4FO6qJ4472p2NSEV2HDJK0z9VUiypIYNQCVei0JWBtpnyR5V7zXwLfXHlTmMn_mk-dg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/831cc909f5.mp4?token=KF67bI_mXQl35JmnOWtm547z3WgyLwUVtOEfYNzXlXkNkRLll6IUibrREv7x7H2pXCH_5dQmqHNrxgWNxDlbzQen0MMjHg-O2ofeqn7i_-PaBTc4LhTuzgXRJna7vuVu9mmoAUGx0hQHffPg-E0lok-NcIxOSaVzDdCohPMA4MjZW8_jlgpcoyS4Ty9j6nN_Fie2pTo9LSDg_8XxefzWuevtzqFudoB3HUuAQWe-AcrHLWgYjDP2GrO404vCt_ADQMlQztpvtDhjzjurlBD4FO6qJ4472p2NSEV2HDJK0z9VUiypIYNQCVei0JWBtpnyR5V7zXwLfXHlTmMn_mk-dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇬
گل‌اول مصر به منتخب ایران توسط صابر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/96244" target="_blank">📅 06:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96243">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">حاجی دفاعوووو
😂
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/96243" target="_blank">📅 06:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96242">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">بچه ها فقط بدوووین فقط بدووووین</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/96242" target="_blank">📅 06:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96241">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">تنگه علیرضااااا باز شددددددد</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/96241" target="_blank">📅 06:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96240">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">مصرررررررر زدددددددد</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/96240" target="_blank">📅 06:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96239">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">گلگلگلگلگگلگلگلگلگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/96239" target="_blank">📅 06:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96238">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">گل برای مصر</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/96238" target="_blank">📅 06:35 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
