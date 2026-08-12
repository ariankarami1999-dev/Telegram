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
<img src="https://cdn5.telesco.pe/file/nEo9_qyHk4y-qkv4wdwRuZNyycILKwknw8fXXCAlnEROtOZNuwVSajMkaAF-9tRvZFfjB1MPVySuDtHW4vnw8Px9D0XpZHFfTEMdpJW1CUv0hDYjAXGqFk-19JvLL2nyRWsbqTSDfV7q_JZw_DhDXcaRMqs7Q57Q7FzYo-ZWT9CRP-3lz_fXT_tYcidu7WgygFzI_0xG9ISafolMsHW5a2eG-Jte8xLTQmTDi1VAUG-KdbmRhieQpmVWhwjOd6WnHFMEBdseRbwbMEEtSKMGr6vQgi272qIORfysR000zof2UCgW1lTS5PyT9OiEE2GV98K5bHaBJSlNzmtAr4sunA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 474K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 17:44:53</div>
<hr>

<div class="tg-post" id="msg-103461">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b308ef230f.mp4?token=le0tgxt09DHdvlidp4uQmOuU6s7Pfq997CJPmi1rP6VdsoanoGaTv5jcgjh1_McTDFtjrtb_SPirkg2ro8VR-_SFqXWD9FqaY7m-2ua8GAQFm4ki89cTmne0RWr_szeawUD1oKsyZZ0T0vflqtR69L_shJUsxiiNwqOdZjPWRT7mlVt6Fc1UCF_gbJuW_iLlt1pg6fhbMkWSBbCgqYunryrVHN0DMWhRh1ewExdMucSO9GhMEiVY9t9WpiNpfkSCzHCEMltjpwunZipZdmbjrPBZ7oH4HK1CWLGllTLyI_iqUOGO_BYRBVjqjNb06a0MQdMmMjuqzK-em36A7_b9LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b308ef230f.mp4?token=le0tgxt09DHdvlidp4uQmOuU6s7Pfq997CJPmi1rP6VdsoanoGaTv5jcgjh1_McTDFtjrtb_SPirkg2ro8VR-_SFqXWD9FqaY7m-2ua8GAQFm4ki89cTmne0RWr_szeawUD1oKsyZZ0T0vflqtR69L_shJUsxiiNwqOdZjPWRT7mlVt6Fc1UCF_gbJuW_iLlt1pg6fhbMkWSBbCgqYunryrVHN0DMWhRh1ewExdMucSO9GhMEiVY9t9WpiNpfkSCzHCEMltjpwunZipZdmbjrPBZ7oH4HK1CWLGllTLyI_iqUOGO_BYRBVjqjNb06a0MQdMmMjuqzK-em36A7_b9LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همیشه اخلاق رو تو ورزش سرلوحه قرار بدید
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 308 · <a href="https://t.me/Futball180TV/103461" target="_blank">📅 17:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103460">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBwE-czU5oYw7nujG-hTaWFIYCRuUJpnGqFxoZv4s5g1BIy-dQic2BFj63nyej8ns7_V5pjJMJsPpzrkr2yHVXvS5Q4BmTcShohPvF9WOT8TRo01HA4Q6s9UAJXYoqcysbMipCc9B3vcOEyPUDJAMmoFEHFC9Re8eWnz5HKltAPucEV4bcaM4D-3RmldW99Szn3FSk78liAFZtvlUVnjkshauS-glVQ3b1uIPI5eVfqFRUObA48iSr-wHWvnHjHx4dILU__-u_mlo20gR5KSEKT-zKwy_UiRXIcLfPRfFq4kOGYqRq36XXA9Y42C4LbxdiDk43MLWkGg7_BxvalNnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
✅
فابريزيو رومانو: جد اسپنس از تاتنهام به اینتر میلان پیوست.
𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/Futball180TV/103460" target="_blank">📅 17:23 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103459">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b42b3af2b9.mp4?token=QrT3rmFO5C_k3hhvLCknR-9dEyOAFwRalwEI1lDGWu4KD13KLy_iRBHN-cRwgN6o2NnHNZIrrEbUempMLpX3K3Tsv7ltF9JNWx14uRvQNIYCqAFEIq4ii592B7RQ2SLFVXsxlefibMEgMLS7XnkPbMEOGCFLhx-0HCl6F9qu-J7P_gS_pQSIhThYZ751bVR4LUdo-mz5OCMJ8CeEKlVK1wbpViRj9TcnMf4w3GhwFYnnOgYfQLEaXdPLNAcz6mai8SGGJUTK7cJFxMcrXuEW1xLr61c0a5Mf56IAho-DdDhfGZoA_oscWEbQx3C9S6XupJhjb2WlOaxJPVyrG0c7jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b42b3af2b9.mp4?token=QrT3rmFO5C_k3hhvLCknR-9dEyOAFwRalwEI1lDGWu4KD13KLy_iRBHN-cRwgN6o2NnHNZIrrEbUempMLpX3K3Tsv7ltF9JNWx14uRvQNIYCqAFEIq4ii592B7RQ2SLFVXsxlefibMEgMLS7XnkPbMEOGCFLhx-0HCl6F9qu-J7P_gS_pQSIhThYZ751bVR4LUdo-mz5OCMJ8CeEKlVK1wbpViRj9TcnMf4w3GhwFYnnOgYfQLEaXdPLNAcz6mai8SGGJUTK7cJFxMcrXuEW1xLr61c0a5Mf56IAho-DdDhfGZoA_oscWEbQx3C9S6XupJhjb2WlOaxJPVyrG0c7jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
استفن‌کری اسطوره بسکتبال امریکا و فناش
😎
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/Futball180TV/103459" target="_blank">📅 17:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103458">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e09EGPOpNALmZB-ZV050JhQfsUJkSgGDzhg-gfesgJdnTDdGMbzhJe_XV-UEHHk5t51C8exoAHeFokFRfvk7k-ODKZWTraOQp8U8xAl6LhpN7L08G4rqYgvEy-1QefVlaMIQmpbKkeUZG23tH6YXk9vJalQVTYoaE6iR7Ik30JxQcle4F6VbIW13X-MMpXCpKXyiZkSpxlyzlsK34eHIo53uV5dk9dN0bU1YBiiuYjpyU3iJvXrai0Xa69pHEJbLEE_GVIoy3UAAE2YNW9jtFcczYn70Fg9n8yXHUBgyP0MyWBohNBQzdoxv1mSFgs0MbXnva346kCAFj8GXYLMQfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامنت کریستیانو رونالدو برای مسی: لئو، در این دوران سخت، تو و خانواده‌ات را عمیقاً در آغوش می‌گیرم. به تو قدرت فراوان می‌دهم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/Futball180TV/103458" target="_blank">📅 17:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103457">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKIMMND9TJXXRPsP8xruKlG8cQy0_cV0cC3hmu37L-rjoSC1m4sSUH9jKhfdZt4lOuezOT65P6XiGTsfg8Qqdvzxyp9Lt3P1IbDNdc4CId5I8MZO8EsrGIqqd1RiXMnETYTtSsMmJhIp4d4tTI0IXLRBEL5RNpc58buqjtJacHfW6SuFe56JNXG3C2uwwM9OR95hu7gumDF_ZATNHKYbYqvd0-MR2P8NQzPPJ11H5x4mKAJVqWjZkpGCqbkyaCSzlw3_v4nmLvDodupU4Z9J3YWZjN2T4jdt74JMgaQ3W01RX5ID-8RX67b8tz1W0KLhDwbczkS5SqtovdHj3V1ckw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📷
⚽️
بخشی از پست احساسی لیونل مسی خطاب به پدر مرحومش:  نمی‌دونم بدون تو چطوری باید ادامه بدم؛ تمام زندگی من فوتبال بود و الان واقعاً شک دارم که بتونم خیلی دیگه ادامه بدم یا نه؛ تو از همون اول کنارم بودی؛ تو پدر، دوست و مدیر برنامه‌های من بودی؛ با اینکه گاهی…</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/Futball180TV/103457" target="_blank">📅 16:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103456">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b48116d0ce.mp4?token=DIlqguUXZIf8IS5U-oVA8EhAEZ-X8nuX-7P9dQd_UbDP-I-VjAjdAasfu95qaJB-oKtrc-HW_7tsCFHOOA1IBIA7x0nabUpdlEeoHfHMAId77fEZ5o3uOP7nXN4m0He7Q4OnPMYBPwHK93dyMX-h2UiimIfhNmKR89lkEca5BBFyvkDN83smpFhELF9n1z5MUQynW87n60CshVb2GXWZxjUFtjow8lSgnSZpYFu6hYBLf4-4ynX32W0Scq0A-foSQP8mHvSuzxK7R_rFAywuIrH8ChtvLWNl-4vaUi43FXbLiSAIJhTOAKNXJ-FXDvqk88K7kOZFNYH_1Wnyv3SMtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b48116d0ce.mp4?token=DIlqguUXZIf8IS5U-oVA8EhAEZ-X8nuX-7P9dQd_UbDP-I-VjAjdAasfu95qaJB-oKtrc-HW_7tsCFHOOA1IBIA7x0nabUpdlEeoHfHMAId77fEZ5o3uOP7nXN4m0He7Q4OnPMYBPwHK93dyMX-h2UiimIfhNmKR89lkEca5BBFyvkDN83smpFhELF9n1z5MUQynW87n60CshVb2GXWZxjUFtjow8lSgnSZpYFu6hYBLf4-4ynX32W0Scq0A-foSQP8mHvSuzxK7R_rFAywuIrH8ChtvLWNl-4vaUi43FXbLiSAIJhTOAKNXJ-FXDvqk88K7kOZFNYH_1Wnyv3SMtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
روایت‌ قدیمی و شنیدنی ژوزه‌مورینیو از شکست مقابل‌بایرن‌مونیخ تو نیمه‌نهایی چمپیونزلیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/Futball180TV/103456" target="_blank">📅 16:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103455">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nch9XcLqFNHd8naPmzasEAgw0LIEsSeR23lSbAuapNUxRzapF7xYzgWViyZCNnNZv18EAtQx6DmVSfvy_6rOn63TokDyL8O7DazQPIXx4Oky6NYNH3yaKu0wGVZV7rIQkPZq3EB28zw3Q893ust6XvbWHyGmhXYDan6aGDOgONjKPCSAAE7iUJfjeRoZrTfRJk4aFXZyhmxaDU-58Sx326u1q3C-qWhqeS8UgsFfobcoASjsPWo1tYYARgu2weBUnIIW99r9MftynMKQG64e0TiKbteskx3rcjFsydazVntsUl9AGYcYqCUdBDO5BMrAAPyuEyMPNDuyLS9Mc9Dugw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📷
⚽️
بخشی از پست احساسی لیونل مسی خطاب به پدر مرحومش:
نمی‌دونم بدون تو چطوری باید ادامه بدم؛ تمام زندگی من فوتبال بود و الان واقعاً شک دارم که بتونم خیلی دیگه ادامه بدم یا نه؛ تو از همون اول کنارم بودی؛ تو پدر، دوست و مدیر برنامه‌های من بودی؛ با اینکه گاهی با هم بحث می‌کردیم، اما همیشه حق با تو بود؛ خیلی دلم برات تنگ می‌شه، اما همیشه در تربیت بچه‌هام حضور خواهی داشت؛ ممنون برای همه چیز، دوستت دارم پدر
🖤
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/Futball180TV/103455" target="_blank">📅 16:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103454">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1e1915bb6.mp4?token=gd50LWeOC2Ex3MIu142iWqu3EwPDpmhhmWxlU9JN--lTtqjqpbo5xTAJgv9dhUExa-Ld_NjcP98dReelgL4faclGz-k4jKZr6wuAzYdv1pqlbIikL--hFqptN9C5HYrQQLmQ7AGirTjjtAPWrjnqJ1gqrWLxwyR5jTCQcJNgLZnkTQENOtivaMLnNO--Vat_bMrZKQf9COMVSb4bB3CZUEO2OmaCvFFaWrXBwD6zgJcPP_Qn77Qj1gVK6gDQQB2P9wddKD8JehGJsQRBGuxaSkA6DCkYqRd7dcJ6fVJKiZBpTD51eqxML70VuD12kP95pS9gkyqrelzGB0B4GtdHoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1e1915bb6.mp4?token=gd50LWeOC2Ex3MIu142iWqu3EwPDpmhhmWxlU9JN--lTtqjqpbo5xTAJgv9dhUExa-Ld_NjcP98dReelgL4faclGz-k4jKZr6wuAzYdv1pqlbIikL--hFqptN9C5HYrQQLmQ7AGirTjjtAPWrjnqJ1gqrWLxwyR5jTCQcJNgLZnkTQENOtivaMLnNO--Vat_bMrZKQf9COMVSb4bB3CZUEO2OmaCvFFaWrXBwD6zgJcPP_Qn77Qj1gVK6gDQQB2P9wddKD8JehGJsQRBGuxaSkA6DCkYqRd7dcJ6fVJKiZBpTD51eqxML70VuD12kP95pS9gkyqrelzGB0B4GtdHoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ورزش کشتی در بخش بانوان
🔥
😅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/Futball180TV/103454" target="_blank">📅 16:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103452">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q8bgnc8W0WGrhzmRT87OrcrnDzEqfnovbeQdCKzxA-0_s9BfilpROe4kPcYSrWT_D_QtO2jHjMDsAA4OG6rSMagNuN8d0qZ3ZVlutNtARDW7HYFgLm4XcenLroEiHdthD88ONBhJD5BjYj9hXC1vDz8ch1Z_RuGPF3YQ6X_XOfNriSX8d7y-FvuO_k1569rioo6kLS99Jvw6dvo4aFZz9MFAe0eJJYDYAA9vKHiT7AhZzCLdP3vYIkfnpooxRwRzC6W1wlJrwkY80GNNdquhLZExg-sEh3PcXEXakiQeXCUsnmoDvC8els8KcXX3zPmJdq4d-SISjziBm-TLNw1nJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/He0xV3tNsX4k5NczZxlb7nFIpObIvwHwEqV8R4myBLTJlzkUKSCy5uVSjAKsGpNbSHT6BZu3oLkTWeXeqDnzh4Hx9yD4AanxNyYMe0zZPq-RDUQ3Xwj5YK4Bta7eMwBhbQ3OF166--DuqEwjtsnqS5qw4cZd5pADcS8kPFl-aZTzwpg7wDkwo6UclYTVP2upnx1qV6max2yDbo7TPLb4xEMqezkNMlFsOQvVwS-PvzE2tkf8SDoDLmXBehlSJVjx46sItTdbWVhnyuC9eKLVzTbjyAQXpkj0EGHnjeX5mm5l0RCCnQwgF9mvD4ms65aqlRuQGSwbQ0Hck0EJWL1Z0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😃
😃
میلیتائو چرا داره خودشو شبیه شخصیت کراش میکنه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/Futball180TV/103452" target="_blank">📅 16:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103451">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3653017ea0.mp4?token=P8H42N-V_vntJdOygUz07PDyXIy6QH97kwKdIwTep_wRggWdAB_oRKWcK7EBqgLBX-9czW4ixB415QshMDaPhQ6wF5XxUmqo7wxA779HzumCSYcsYduZ7_0DtKn-21Lz1f_zOf5ecgHU8yAIBrFRzEGrgmEsy-IUmHFrNflaHL4tYRbssiFdEtzUjOZNnGZV5_XoC4qxqol9a0PjOuPcrHQa_sSG_3Z4INoWdUu926E6QMWGlTsCgqCKZNEdnRksm6yK_EnuZyMSxlryg8zIBVZlq9sznnRiw0qmX5CnSj6oBqHYunKPccaXqey2GpwbX_U10k3Cb_HnIs1ZVLw1LnUCPSOT2VgDjmBBG54YwByqiVFwPUe75Sg3hQR8T9P3PZXuXhPKo9L_lQIq3dwVio0G4hsblMzWs_DrqF1hg2D4Nv51s-s-lVel-Ev3EZhNC3FsJmzVehbput4AQvKwdqQvAPj1EYKUbFxN8vWU7GZLdRNReEVsBwlWrA42i69Vxfdr1rCS7iLDYdvUXis99-uvSq-aun301deKYsFoRlDXx3K6-w76Pw8X7pzeURfNzZKFNqHjYcUOPdcM7j8BJDj1gw1Id2CFW6n6bO-hRMXpvkYNgJzDvE2zo2aeK0Fg-xkTY14Z-CexVnqZcUwYXIc1AkD82ERTp3g7ds511hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3653017ea0.mp4?token=P8H42N-V_vntJdOygUz07PDyXIy6QH97kwKdIwTep_wRggWdAB_oRKWcK7EBqgLBX-9czW4ixB415QshMDaPhQ6wF5XxUmqo7wxA779HzumCSYcsYduZ7_0DtKn-21Lz1f_zOf5ecgHU8yAIBrFRzEGrgmEsy-IUmHFrNflaHL4tYRbssiFdEtzUjOZNnGZV5_XoC4qxqol9a0PjOuPcrHQa_sSG_3Z4INoWdUu926E6QMWGlTsCgqCKZNEdnRksm6yK_EnuZyMSxlryg8zIBVZlq9sznnRiw0qmX5CnSj6oBqHYunKPccaXqey2GpwbX_U10k3Cb_HnIs1ZVLw1LnUCPSOT2VgDjmBBG54YwByqiVFwPUe75Sg3hQR8T9P3PZXuXhPKo9L_lQIq3dwVio0G4hsblMzWs_DrqF1hg2D4Nv51s-s-lVel-Ev3EZhNC3FsJmzVehbput4AQvKwdqQvAPj1EYKUbFxN8vWU7GZLdRNReEVsBwlWrA42i69Vxfdr1rCS7iLDYdvUXis99-uvSq-aun301deKYsFoRlDXx3K6-w76Pw8X7pzeURfNzZKFNqHjYcUOPdcM7j8BJDj1gw1Id2CFW6n6bO-hRMXpvkYNgJzDvE2zo2aeK0Fg-xkTY14Z-CexVnqZcUwYXIc1AkD82ERTp3g7ds511hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فوتبال در هوای بارانی در کشور هند
😬
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/Futball180TV/103451" target="_blank">📅 16:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103449">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a91054b37.mp4?token=Dn9SwONU2gBL5ZobcHHKHLobDN_IfcWzT5JEv8_BDoaC04WlftnUBV6kzOfrcuh4qMvtL131xUIubn_3ENeEUa7YIpyW-hcRbz_DnYrsF31HexxXby87395a0GuzKcjkc_4dFkP2cE7Jo7QN6gpKLxbe0ufLKh38yMQlibiGybdKZ3PA76hKSTsk1Ecsq83zsP3YmvMsAttfJJetQKWMrFRFiZu3wmeRaS-fvoCQgW88LC7dkxOZKUsS_dAtx9qef5cOLNfUE2q5G1WTeD55jXMILELjRZvp9_30E4Cm0n6gp_EjOkIhYuUAP16QOwne9NYh15zIlFk5hDWG70U_BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a91054b37.mp4?token=Dn9SwONU2gBL5ZobcHHKHLobDN_IfcWzT5JEv8_BDoaC04WlftnUBV6kzOfrcuh4qMvtL131xUIubn_3ENeEUa7YIpyW-hcRbz_DnYrsF31HexxXby87395a0GuzKcjkc_4dFkP2cE7Jo7QN6gpKLxbe0ufLKh38yMQlibiGybdKZ3PA76hKSTsk1Ecsq83zsP3YmvMsAttfJJetQKWMrFRFiZu3wmeRaS-fvoCQgW88LC7dkxOZKUsS_dAtx9qef5cOLNfUE2q5G1WTeD55jXMILELjRZvp9_30E4Cm0n6gp_EjOkIhYuUAP16QOwne9NYh15zIlFk5hDWG70U_BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
▶️
یه یارویی به اسم «پدرو» فلج مغزی داشت و آرزوش شرکت تو مسابقات سنگین IRONMAN بود. برادرش «میگل» تصمیم می‌گیره با تجهیزات خاص، پدرو رو توی تمام مسیر مسابقه که شامل شنا، دوچرخه‌سواری و ماراتن بود همراه خودش بکشه تا رؤیاشو واقعی کنه؛ حرکتی که به پروژه «برادران آهنین» معروف شد تا هم به بقیه امید بده و هم ثابت کنه بزرگ‌ترین پیروزی، مسیر قشنگیه که دونفری طی میشه.‌.‌.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/Futball180TV/103449" target="_blank">📅 15:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103448">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X951I_-k7d_ckjWo73xcG5uicmjwH3q1Milwn2L0447ISjOOJcCNupbDGAYvDOryu46He_CE56DLPDb0B3tN0G7fUqJ8rhml7m9_wwnO4D7tRyq8fprZo7rBUQiFpTT4VbxcHGqZSmM3S3F1dqQ4o5S6Ne1OQ40yvvcY0AVOvV_ePRbYVzsa4WijUKt3dBPPz4FDzfQ458bxVRXmZaYY4pSuMqhKT62-DqEd2MxQMd6OuSP4k0vexPWw8S_7-JU_X2qyVeTguU9_LuQ_alH9_2gPxSmXaOwHebqJQKfK3waHmdo1rB3Y2KxqMUmw7lP9KO0Mju7-URX4U4pACuQm8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
•
پنج باشگاهی که بیشترین درآمد رو از فروش بازیکن تو بازار نقل و انتقالات این فصل داشتن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/Futball180TV/103448" target="_blank">📅 15:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103447">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1a4a8150c.mp4?token=JA-Bk8WJtAexUKM3rNyfijCsuWLSg5mr1UydJhtae0ig5S4HNJsCjYIBkXhcn2vetOV8d2fYbA6y6eKPK1SAzz0xVsrIAuk2AYgTui9wDJbNYJbYxvmBHiIqrnArE1PnHLVGXZlcCpT_QBQHOJoJ3MNaMBkoINJhJbNpXDQfOwblLkuBZXgLZTTy8FsoaI5dYQ-2EADc7M846F1pLovV4Qqc2m9sCNQCKrUyFBKpAC1tvGTBzvR3m4JzcSdYxfJMCZOr01hJkb2hOoNA4ReneYpDG-49rFf68JPORPpshYt26gntmIm1TtNDL4hqDvq2pIkXgF-s_WLt4bS50F2UKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1a4a8150c.mp4?token=JA-Bk8WJtAexUKM3rNyfijCsuWLSg5mr1UydJhtae0ig5S4HNJsCjYIBkXhcn2vetOV8d2fYbA6y6eKPK1SAzz0xVsrIAuk2AYgTui9wDJbNYJbYxvmBHiIqrnArE1PnHLVGXZlcCpT_QBQHOJoJ3MNaMBkoINJhJbNpXDQfOwblLkuBZXgLZTTy8FsoaI5dYQ-2EADc7M846F1pLovV4Qqc2m9sCNQCKrUyFBKpAC1tvGTBzvR3m4JzcSdYxfJMCZOr01hJkb2hOoNA4ReneYpDG-49rFf68JPORPpshYt26gntmIm1TtNDL4hqDvq2pIkXgF-s_WLt4bS50F2UKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇪🇸
رویایی روز و شب بارسایی‌ها‌در یک‌نگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/Futball180TV/103447" target="_blank">📅 15:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103446">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7IFeWOYAoBJNZxG4VBxc0tRwko2vnGyTtzXdAvadnJenWFciz8OFcB4zsyH6vOPC_nUM-KnIOLsBEgi9zpR5xI500OFtt6Xkr2tftEghwYYYLelNrdimwkU07OotGV-IMQ3YKDJJ_lx5Uq4oIaVrxazy2R3j00fXWFpHabJFwTlktiWacW1WrWs4fB-dBn4D9JO3vxVFtMk-5xZGPhqMgTWt47pkc_TrlpGZvMprSY7FM83bnwN_sd-Afso126OiiKZaIZ_59BFuVkZND9jXkNDzof2Jnun_VYazttKdGrQDuZW1KqC4LaPlZc34Q3N0-oMNVNTkCtLExJiy35IRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فابریزیو رومانو:
پیشنهاد جدید بارسلونا برای جذب رودری به دست مدیران سیتی رسید؛ 60 میلیون یورو ثابت + آپشن
🔺
مدیران منچسترسیتی باز هم بیشتر از 60 میلیون یورو میخوان اما دکو داره مذاکره می‌کنه که به توافق برسن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/103446" target="_blank">📅 14:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103445">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/186aaefcf2.mp4?token=eQvFM77_BTvcfnoWj_i5dE2HZaYYkRLXuv6TTB5YUbL3kTv1z8nNHW3p4ha9OyDsNJp0bY9AeOlyadmMOs-FwDsILlkrkfq0_HoTTa1TkaUYtms-SuGuNINyBHaq0uEV2KSe42-IlRkVfw-L2E3O6p1UH_oamvpyW-Hq1PUQznCMF-rp_iSfS3zI1caDc89a5WysN11rXGkS5DbiQcJGsqLsnGfkQa462nW3LbffQX7LnqFL5df7hRriAY3SILEV79FSnmkn6P_jTEmJm759Xy1mnTxhVk6Y2Dg8t4oYC7tx5jkZirB4WZ081_-nyrs7QWgOZ_WuniE2zYXzl33McqsE135JK9Vt2w39nSIPbKriHo92gHnOHZPHGhhHktKToow2j4dvCxHriwRLJsqQw_p5oDE4rjFe84zmmf0HjyqQpuNcQIaOAjFroykRhDocpoSWgSOCN11DxA1t2FD3TzUKvL4vKnKG21RsfQ2QCMvNWHSFEFUvx3KJGmrAWWwelOnoVviIviHv7fuUGHnVHLtu8e5JqO2Kw-8bMx9RpHntKYd9WxdbRywF7WXDXlXnoVX5VJf1f9sFxP0qfoJZ_WFsIAwxcX0tMbPLNsTZh17RDd43Irror-Azt6aLBt9WP3JEnMXja4Tc9RASlVgHiwKUVenxggtC-1gMo7myt34" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/186aaefcf2.mp4?token=eQvFM77_BTvcfnoWj_i5dE2HZaYYkRLXuv6TTB5YUbL3kTv1z8nNHW3p4ha9OyDsNJp0bY9AeOlyadmMOs-FwDsILlkrkfq0_HoTTa1TkaUYtms-SuGuNINyBHaq0uEV2KSe42-IlRkVfw-L2E3O6p1UH_oamvpyW-Hq1PUQznCMF-rp_iSfS3zI1caDc89a5WysN11rXGkS5DbiQcJGsqLsnGfkQa462nW3LbffQX7LnqFL5df7hRriAY3SILEV79FSnmkn6P_jTEmJm759Xy1mnTxhVk6Y2Dg8t4oYC7tx5jkZirB4WZ081_-nyrs7QWgOZ_WuniE2zYXzl33McqsE135JK9Vt2w39nSIPbKriHo92gHnOHZPHGhhHktKToow2j4dvCxHriwRLJsqQw_p5oDE4rjFe84zmmf0HjyqQpuNcQIaOAjFroykRhDocpoSWgSOCN11DxA1t2FD3TzUKvL4vKnKG21RsfQ2QCMvNWHSFEFUvx3KJGmrAWWwelOnoVviIviHv7fuUGHnVHLtu8e5JqO2Kw-8bMx9RpHntKYd9WxdbRywF7WXDXlXnoVX5VJf1f9sFxP0qfoJZ_WFsIAwxcX0tMbPLNsTZh17RDd43Irror-Azt6aLBt9WP3JEnMXja4Tc9RASlVgHiwKUVenxggtC-1gMo7myt34" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🤯
لحظاتی ناب با اسطوره زین‌الدین زیدان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/103445" target="_blank">📅 14:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103444">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81d1d4d2c8.mp4?token=lvBRETZpE40h-7pzmq1Qva_8IYxcQ-kgGjyjND8u6zoRZrA9fQSzed7UJhX6hza2BQ23-9lnwTtwP9yJCL0He05E8YOXUIDyHMprywPFLhSiLTSu_fF6paxuq8rPcnRMLKaho7LtV7v2EIYDiJFnNh6YOslhoxnw236_Tx58EnKGJCzD0HXSiI1D0Yj4T8_kJHbtqVxbFDoWWZUtRCWexArMbOZ5hGLLN1_4Y57Xj9RBxnedonZdA2oWP6FYlD6w4PgIfv5Fa8Wrq-JWwoEB3wKIfIo_glUZSaXiAVHyQtY-jc36MazB1Enp_PrUs7I9xw5ljbkbdzYCZkbZhkZghA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81d1d4d2c8.mp4?token=lvBRETZpE40h-7pzmq1Qva_8IYxcQ-kgGjyjND8u6zoRZrA9fQSzed7UJhX6hza2BQ23-9lnwTtwP9yJCL0He05E8YOXUIDyHMprywPFLhSiLTSu_fF6paxuq8rPcnRMLKaho7LtV7v2EIYDiJFnNh6YOslhoxnw236_Tx58EnKGJCzD0HXSiI1D0Yj4T8_kJHbtqVxbFDoWWZUtRCWexArMbOZ5hGLLN1_4Y57Xj9RBxnedonZdA2oWP6FYlD6w4PgIfv5Fa8Wrq-JWwoEB3wKIfIo_glUZSaXiAVHyQtY-jc36MazB1Enp_PrUs7I9xw5ljbkbdzYCZkbZhkZghA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
دل‌هارو ببریم به سمت دوستان فوتبال‌باز قدیمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/103444" target="_blank">📅 14:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103443">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fba285851.mp4?token=UHpGNDZoQ_3H6F2N5lX3pEvQiNA84jE6v8n1WR_PpdlNl0rsu4KHiDXJyU0kro7F_DSNZBc9Bm5WWZ3-ycu2jcE0E4JALZdVvZXQMwtl6R3_0vpZKfSSY12DCwLxs20juVKWLNmygSezswusDeBS7xWCVwtUEIfHXRRpg-ZVuc2ajATaOXts2QC1g2eeATVLBvZRJEHRJ-2gLykgDOB6Z7XxaJoxMAHrDchokpeDrFjFV4IR30fS7nDPAmn1WgFqWM17NmdgOTaGp3GuY1OuyoYPqiUywQVdwF3dZGdrRVGmG-btoR3-ZL-hoegT3eIIGavzg1_ac6f_EVFhfD5KfzssS-yiXO5hsEYguMXhiYylyxyPUB335RqKa4D0v59j6qtrUjAetb5Wrub2cY4_ofM147XDpKs_v5vIPDVncNPFqzg9ofOXzLla-N4sUbS_7t-CvQZwT42IDkqAhNfa4ytRxL0PENV47SAPUMhcZHpupFeydIx-rxCSmeCmfqAyDhY71ukoZjGNv0cWlQ0StuvwP3bAG7-lQdC5TsCcYAnROvE_bErp9xUhqM16Mlo0rQLOHQWcSGKPVFaPmGsxuPHSq5cCKSFJH20qMgbnORpwiK2MQcY3aMPVbqeoys4zSM-36T51X6_PsqGimwRQTCbmTiFtViZgkL7a2jXIvv4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fba285851.mp4?token=UHpGNDZoQ_3H6F2N5lX3pEvQiNA84jE6v8n1WR_PpdlNl0rsu4KHiDXJyU0kro7F_DSNZBc9Bm5WWZ3-ycu2jcE0E4JALZdVvZXQMwtl6R3_0vpZKfSSY12DCwLxs20juVKWLNmygSezswusDeBS7xWCVwtUEIfHXRRpg-ZVuc2ajATaOXts2QC1g2eeATVLBvZRJEHRJ-2gLykgDOB6Z7XxaJoxMAHrDchokpeDrFjFV4IR30fS7nDPAmn1WgFqWM17NmdgOTaGp3GuY1OuyoYPqiUywQVdwF3dZGdrRVGmG-btoR3-ZL-hoegT3eIIGavzg1_ac6f_EVFhfD5KfzssS-yiXO5hsEYguMXhiYylyxyPUB335RqKa4D0v59j6qtrUjAetb5Wrub2cY4_ofM147XDpKs_v5vIPDVncNPFqzg9ofOXzLla-N4sUbS_7t-CvQZwT42IDkqAhNfa4ytRxL0PENV47SAPUMhcZHpupFeydIx-rxCSmeCmfqAyDhY71ukoZjGNv0cWlQ0StuvwP3bAG7-lQdC5TsCcYAnROvE_bErp9xUhqM16Mlo0rQLOHQWcSGKPVFaPmGsxuPHSq5cCKSFJH20qMgbnORpwiK2MQcY3aMPVbqeoys4zSM-36T51X6_PsqGimwRQTCbmTiFtViZgkL7a2jXIvv4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
⚽️
چالش‌جذاب و دیدنی تمرینات لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/103443" target="_blank">📅 13:35 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103442">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOVbDxsxFAwhgDQU6dh9v1ZTbbpnLdZ9dQwU3Sf6320iF_SqB4QHjBcPkZKuOI40c5-j3P57AVZP067-w6S9a8iJFVsu0_5XGjeKWq8SUrRq_i5wMn4kVYjDgNamDNWA_pSCMjg60XybYiZFOkNOWK7c3GfBSJQjSviB2s8WkxOnobc3djP-pQ-_IOuWL_amaeQRN3SciRYaRGHDdh_ecUOwce0Xf_LlhBYpHJm7Ga-fC8VFTgcafdgLksDX2j2tSGCyw6wTgO2jDrGJM7zuoJ-8sVqYowmvawHBrWsFGjiyxWMtA4afwSeWuwb7U_Uxrnt4ZHvhb1AH1eh4PRiyiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
مودریچ و کارواخال، پرافتخارترین بازیکنان در رقابت‌های سوپرجام اروپا با کسب ۵ عنوان قهرمانی.
🚨
📊
🏆
کواچیچ، با کسب سه عنوان قهرمانی از سه باشگاه مختلف، رکورددار است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/103442" target="_blank">📅 13:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103441">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc3b0e5a8.mp4?token=hj-CnmPBeRfbkQSiaz5crrKDWKSMo-kpSryMGcx7rzp80CEYljiiCrhpNGfjNw-7hh6-IQWfSZZwJYALeemJrkeZaM28EZHc5VvUzFRjO68IqErnffasOBRHGFuN7wybYFlYfNQXQEQJI-yStN_iQZ1J1kKLA9cbYbdU8SXh4aWjEci_puWkknUYywXyan0-eeOitZCuhVclwTi6Hw-5r_8H3cWCbSMJM_TcsiW8GPqlJPBr5Ho_8Dk5trISrLJklz9pWSVWJWOGJvcpI48_huPG0yRJ7BcvBBriaF64XGkos7cXP9IVa005owgDFju30fuCLAphUuTxsLjWhiLExQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc3b0e5a8.mp4?token=hj-CnmPBeRfbkQSiaz5crrKDWKSMo-kpSryMGcx7rzp80CEYljiiCrhpNGfjNw-7hh6-IQWfSZZwJYALeemJrkeZaM28EZHc5VvUzFRjO68IqErnffasOBRHGFuN7wybYFlYfNQXQEQJI-yStN_iQZ1J1kKLA9cbYbdU8SXh4aWjEci_puWkknUYywXyan0-eeOitZCuhVclwTi6Hw-5r_8H3cWCbSMJM_TcsiW8GPqlJPBr5Ho_8Dk5trISrLJklz9pWSVWJWOGJvcpI48_huPG0yRJ7BcvBBriaF64XGkos7cXP9IVa005owgDFju30fuCLAphUuTxsLjWhiLExQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🤯
💸
وقتی استاد فیروز کریمی بیشترین دستمزدی که در فوتبال گرفته رو لو میده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/103441" target="_blank">📅 13:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103440">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79bf3a3f4d.mp4?token=ZllDaVjz8YlkkaPb1rufhhsQcBhbpub1RR6xcrlF8OrKAvBskWSmW6LdT4XVZX23Cdvrh5ZeWyx5znjyFoy4KErjKC63Dk-NTNJn5FS0G8aKrBRa_LVcI1--XoMqlHCHn1vLZ8035ZFjryB-uNr4puXphH-qV9gKDJhmhRsgCW5ou9y-rbEqq0GJoPqaf3EkvfqKEKUgnJAlyrFko8Yy5_JnjFCdXdsfHfrvB9Q7Dpg6OObtiYNB-ypfjV3So7OFMNuo9jZAvlb8vIlwseG6eYm9bpYgyNcH_BiIfclLEEnbHFX4Vk_Bk8qLZLwaqlyjGeCsR8zky7OMTMtHnEJZMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79bf3a3f4d.mp4?token=ZllDaVjz8YlkkaPb1rufhhsQcBhbpub1RR6xcrlF8OrKAvBskWSmW6LdT4XVZX23Cdvrh5ZeWyx5znjyFoy4KErjKC63Dk-NTNJn5FS0G8aKrBRa_LVcI1--XoMqlHCHn1vLZ8035ZFjryB-uNr4puXphH-qV9gKDJhmhRsgCW5ou9y-rbEqq0GJoPqaf3EkvfqKEKUgnJAlyrFko8Yy5_JnjFCdXdsfHfrvB9Q7Dpg6OObtiYNB-ypfjV3So7OFMNuo9jZAvlb8vIlwseG6eYm9bpYgyNcH_BiIfclLEEnbHFX4Vk_Bk8qLZLwaqlyjGeCsR8zky7OMTMtHnEJZMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
✅
بواتنگ از خاطراتش در بارسلونا و استعداد بی نظیر مسی میگه...
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/103440" target="_blank">📅 12:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103439">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o46hayq4efUwFr0hQcRZzjyRF75q0gR70m25VS7DqXqT-5WNc6HjjzeNiFM2bC2M2j2lgmKZB9YnjdmNt6D9mjFyJ-NFx23TY3yPfaOUsE6yvIhryuoIcOsTn_a_ZrYss32mO1xufkTTi6kT6Db2ub7bkS3D2_8YkYQMgZcXmUdReeXAMfbQn6Ql5hlrRFmiFkMCO_tm-az-99kb-yNRTQBYBlkZjOATIumNLjz2Y2oH-oHtTihUjSpLEKxxI-behQTWsb3yyzk_Uo-e4ZI7rgbsvSAX8RbqhyUUeh1blxGZGkowK394DJ66NECkLpn7iv9N5mSr-T-vsv6uDjirJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
🇮🇹
🗞
رومانو: دو باشگاه اینتر و لاتزیو درحال مذاکره نهایی برای جابه‌جایی داوید فراتسی هستند. رقم پیشنهادی لاتزیو ۱۵ میلیون یورو است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/103439" target="_blank">📅 12:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103438">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/531604864b.mp4?token=REFX26g8WM8HScE_169m9YQpNjj4VGUQ2l6kGIR1cdEvPwxqLr13CEjI6vYTbPKuWFjf9-4pMP2WmBG6UVeXZChd6iURgKmJx4SQjr-OICHX6G_UIopZvEhj8Y9OacWxvIxroZagcmaD-E44RE8OLclywBS4OP2g3SwTPrdFk3_NhApwC4ihF5SZM0vMNX_w1XMLGWfVLqw76x9EPsm5Nhs6t-mdf6GTbfEWncFZ8Fc5CyFeBevw-6P_2LnDlAn-_o-wtSa7xgVF_mhYaw31cySFzy30fZJA32tuSPsjVtB0Ko-C0W9SgqzEoDUv4sNxw2H1FX9WQfHkldMM43pkhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/531604864b.mp4?token=REFX26g8WM8HScE_169m9YQpNjj4VGUQ2l6kGIR1cdEvPwxqLr13CEjI6vYTbPKuWFjf9-4pMP2WmBG6UVeXZChd6iURgKmJx4SQjr-OICHX6G_UIopZvEhj8Y9OacWxvIxroZagcmaD-E44RE8OLclywBS4OP2g3SwTPrdFk3_NhApwC4ihF5SZM0vMNX_w1XMLGWfVLqw76x9EPsm5Nhs6t-mdf6GTbfEWncFZ8Fc5CyFeBevw-6P_2LnDlAn-_o-wtSa7xgVF_mhYaw31cySFzy30fZJA32tuSPsjVtB0Ko-C0W9SgqzEoDUv4sNxw2H1FX9WQfHkldMM43pkhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رامین رضاییان بزرگ
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/103438" target="_blank">📅 12:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103437">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHVnJ1GgZLSKz7gB96UEA61lcWRS8n7SsrM_gbn59sdVw7uCuJInITBGn0UC3HydcAnf8conSUaUeo2ToaBwxGB97IOZP5MZMVggnZ37FSC92NgeqNvaXpr5EzB8pV7QrIMfun7JbfUS8IP9IvTmIh9VApBSeVqazuFRlWnt56j0Gq75EQVO1gYQRcyCKAMQvV6-2cOwvrZ2gCTytvI1cMB89t8JwXygQXfNM_yig2dwh60lIzq12C3Y1lQ1lTbAHW-U4MAj_9esb9SN2glTZX2IL4xJxznXwZimElIEob3oGi6b-YrwP2RDM0J9S8gnGwjfvbPg6eHlvBmFNNgyOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
✅
#فوووووری
و
#رسمیییییی
؛
🇹🇷
روملو لوکاکو با عقد قراردادی به فنرباغچه پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/103437" target="_blank">📅 12:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103435">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XZUkuYZEWONV46xhwXx90j_C4-fY4eW-34upcw9J383ZUDK-Hw2XJXN5bmWi5aoqIxpNn9V0EP9BmPmuQro7s5iHbfqo5imOAGULhYyAwkr6Fj8r6I1GhdNiBl8sIUeT60RrNZmQSSlUQ9gVHQqG5JaV1SVbp2GFZaNkJCiK2vDp0px7Q7RiCZP2XGH6N0OyN9HitkbTAzAQsTTJ7DZrTBe10Uex1KqYCCnDhF2Z1ZTpmxqKU7nfrSuAjzunsbMOPxPu13Bw1PSQMsEljjaZYnaatjtQbO7yyQJoQh9W0wlRHgaWubKOjhFNCkKhDsSn7CQgryctYxvGImgHGQ0huA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YEOTBJAAAib5GwjdVZydyUrRf44vwCTahYd6gUz2yW9x6EZm9-S_7zqYJYdUUkutb18XUtJz5gaX0XdL6ZkaGJl7UOQyIOEtQMkUKu1e_9eddo7Teh7Mxx7zDMN9mz9RjHM_5k0GI4pptNUjf1HUQKGOwcMPO-F2gymVsJpO6WJMQ6TQbDbSO4DqdAw9HWbSxH9bIOnLoBAF2SdfioOuMzEXsvQR-pDUbkY-VizMGYmd-3AyQR9QMgSBQApeyldde9WYuhT9YwFaVp_UC5ztgPCWtH9Kp1XcbIanyDs6ih49upNyT8CDuUMUJ0yzDIF-WzRs5J-NfWP5XWmIAE1gNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇷
تمرینات امروز اتلتیکومادرید با حضور آلوارز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/103435" target="_blank">📅 12:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103434">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba2ab6526.mp4?token=FwVHgexyrsMgghrVs3X43PHCd_pPuZOW66vd2Cv2dzUCLWQi_XVtpZ78ZRYAfvGjQi6NfkeK7JBH87lQ6qdCJon3j02KVGhlBhj3Q-A6YxNe7DvVXb42LoIVgcpMc3m0ANixdy594vM0U35m_03WNQs3PIPMuveVj53L_l2jlLNzVCeCV5_S-jiD2dei899_HiLQEudZasC7ciWLGiXlo4iFwLlVoDpoaMus56rSQbeSx8FLAsY8LI91lK06aOJA4ZQTaKwh6yQwX22yxLeT5cUpQkADui1UBI36MLZBAnbzbKifNysS-k4gCTnmMQUE2WX5NmiwFwPZUnhn5X09rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba2ab6526.mp4?token=FwVHgexyrsMgghrVs3X43PHCd_pPuZOW66vd2Cv2dzUCLWQi_XVtpZ78ZRYAfvGjQi6NfkeK7JBH87lQ6qdCJon3j02KVGhlBhj3Q-A6YxNe7DvVXb42LoIVgcpMc3m0ANixdy594vM0U35m_03WNQs3PIPMuveVj53L_l2jlLNzVCeCV5_S-jiD2dei899_HiLQEudZasC7ciWLGiXlo4iFwLlVoDpoaMus56rSQbeSx8FLAsY8LI91lK06aOJA4ZQTaKwh6yQwX22yxLeT5cUpQkADui1UBI36MLZBAnbzbKifNysS-k4gCTnmMQUE2WX5NmiwFwPZUnhn5X09rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراسم ازدواج رونالدو و جورجینا.
🎉
😍
💍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/103434" target="_blank">📅 12:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103433">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aav3XhgwTNSeu7vwujwjo-w93KgtUcg5r75-0pFlTUh2kmBhrEHU_J9MlHCWkbQReNH2gkFtiPVyKETZMMz-EYbPvWxltMBfF2XSHcfyzDkRzxdSkwH0JefIfGKB3rCf-lWOAzuj9Uhz7saFMXmK6zSaA5w_EZyo_OCLYOE4-mP9S6LOeSXr1qOOPKkH5NEwEDqSpRNoFuXsVost39Q03tmMnIC2OD9pweoYboqGvndA1uF5AKf6Ro5Vrj0kRjDD3UxTSt93kw0iRix2iYUZtbPsDwSs0GPtqgv76kDy9Fq9lQK8_enibTf8d67QUVn74c49DJr4kYq2Wu4cQpazGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📱
❌
استوری تند روزبه‌سینکی دروازه‌بان شریف فوتبال ایران علیه رامین‌رضاییان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/103433" target="_blank">📅 11:48 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103432">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uilfk-YrW9mWl2ECOBon1nmDiAig7okE4P0uHt9xq78axI7sBbpSN_0a2-kr3sbTeyRaZuY7FO0F0kRgmJKvDLTJagrT0tW3NPb1VohJYTTAWIYb0LLeJEO8aYrem05ICk00ns01r_bCebcVC-pPa2yKSkqClWvpdP8ZjPWa8y10tdeoDZ45b5PiHo1QJkyrVpl9HVizzULgNUd7YZvsDUc1v3jBHQCGIq1T8pJjYIdzTBbb3SiMWP1YRPSVa5hdUJy2AR-vwKJK75Nm7vw1k8RVARExF0I4eX_ATmNi_XkvSvcCLEu39Rj58GUOpWqY8i6tZPedXNeOhskaDjlI_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
قیمت‌بلیت بازی تیم‌های فوتبال استقلال و مس‌شهربابک ناقابل ۳۰۰ هزار تومان وجه‌رایج مملکته
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/103432" target="_blank">📅 11:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103431">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AnD5J9DrIfQHc_IQBBVEemy9Q20_1G3kLBrfwHJTvPIN5rXlueuC6NwRe-gkyllgEngATTFlyYPlCodUPThlACcKecooadrH4pQfg6viErkO7m6AfgvOrd2UZUL9yFZ7OZMicBHu1BGOxX9E0F7qZMqAiNA8p_aCjzv0HFnSG2s6x7Mzcgew_xXorjHon81gUSCqXXDATKCtqS9YEQOptAQ_2IraBcR80RhHtxBfaNFrlB8Bq04tfQaQS-X-fp0UY9zP6FATN7xXi5tBqMo6R6LwTSDaawvcZBVIuJgPydT8U0E8AB2roCQpzVP8iR-2xvxJ7LtKiEUDDWGmViybrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
رونمایی‌رسمی از کیت‌اول قهرمان‌فوتبال آسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/103431" target="_blank">📅 11:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103430">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emL1tD9i5SDeaUv_6saGmTLoGWl3ZawLGtaIK1cE3br7HRxmmI0g86lFbF4UJK0525yVLm7jQi71yIC2UdrZW7-PyfrGAHN71W_v_f0KXEcrLCnQN4N1Oha5dFM8D5ohuSO1nFl1XUJ5hMy1D1yt-8pSCSR0QKlhYVJc2R5tRvPHlLEtFqB5J-fQ5feUjT5peTPmS_Xy5mNk4Gz8P9operWQCNIai6UPdLTtmRpCMQP9EXAPPT1GH0LK0WUaAY1gbEhkHICa7Vhqg6Z-PEsiAPK1JaAifU4meSa6AQ0Z758tyc48QoRCKKh-sSCnc-NsxiXRonCew4DDs0nGjjeK9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
✅
⚽️
#رسمیییییی
؛ باشگاه چلسی رسماً اعلام کرد که با پپ چاواریا از باشگاه رایو وایکانو به مبلغ 21 میلیون یورو (همراه با موارد اضافی) قرارداد امضا کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/103430" target="_blank">📅 11:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103429">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWjH9KVwxvPHl95F2DxT1iM8u6Q9EqvZpUgEyj879aoWJKzfiwb47gu_Fv0XmRZ08druEM0xTcTw_SPugeBmr2lezyJ7WfVERzdH53uRw4isVKolBcuDxWHm5lfttTJ1aRVCwiyeBFzfpDcaPr9HkXSvrybbYusptpAidVCEFCP67YiflZ4kfKWNcJPWL709XW2E_JxfAlP1IxbxuKuMkg1wU48O4EH74ohFRIwQI8QX0ahgGS198b6dcsk9o3D9LbZ6teR37XNThnBiObbGrhJZUgWQI-ok9XcPXDlXxDzbKrfEOa07326mV_MBQ4plmBQRjEckQrytRmuWOf-2hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📰
فابریزیو رومانو:
🇪🇸
پیشنها دوم بارسلونا برای رودری به مبلغ ۶۰ میلیون ارسال شد
🚫
🏴󠁧󠁢󠁥󠁮󠁧󠁿
سیتی ۸۰ میلیون یورو می‌خواد
💸
✅
انتظار میره روی مبلغی بین ۶۰ و ۸۰ میلیون توافق بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/103429" target="_blank">📅 11:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103428">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4QJ7iQZtXf2M7fdvAxt5Fa6bSobr_IL5vCNkA6eidhjPjHUNnXECrzHeYMTJyI7mjlT5nAABNOoc9gwDDa4D_p14w3NVJtjqJNEHYmIu7zLKFUTU7maeMBHnilz4-ViYti9LiNNqDsVzzuut0SyQWQaD1H6ZnMc8ItZTa0D7YA1Vus8ZCCmzDvfP8ZXU2SRo0oeF1j21GZXH0CSBOrfvvxeqCWDlru83dwJ5tEZhDLPujOaa6oJSsB8ZjKWvmUoWQ6AxTM5i7spYz26-TmVEi2CtlGEZSKAKxdQW5otsXpyom0Cj_7HBtmXm4VvIzw9Txu2D2LxCMXMLK0vTifqZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رونمایی‌رسمی از کیت‌سوم و صورتی رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/103428" target="_blank">📅 11:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103427">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/103427" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✈️
اپلیکیشن MelBet
🥇
🎁
کد هدیه 100 دلاری:
Sport100
🔒
برای تعیین رمز ورود حداقل از 8 کاراکتر و حروف بزرگ و کوچک انگلیسی و اعداد انگلیسی استفاده کنید، مانند Hamid120
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/103427" target="_blank">📅 11:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103426">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ylz-pekCZih7kiaY5WUfip2oclBUtsZQEgs0jrZjxt9-lB1ShALHPgRNNwiV4b5Ey2pbfMgncsShVg4Yka19qeE1nz-G-zlw3coxB5z-gmQqeflhgG4LcYCXFIDkPIvSzpVKYoqgaHAgKkJLbNuZcrxIIRhzjAW0EOwrdSr9dA8FhA0maCtcP5p3hO6q0_wCpaM50AJbFsNYB4NvA4wb2cYMzQyc1jROwh1iW46rYN_ypQwbG-UwOGrV_tmtD3w3upKR7aDd2pipnoTTvomH7BxuvFyv2rTBrtD9FVZ3G19GezR4GwGylAug4FS_kStaq9QN-vHv8Q-yWwN8ux_9tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌     ‌ ‌ ‌ ‌ ‌    ‌‌ ‌‌‌  ‌
💯
‌
فینال سوپر کاپ اروپا
💯
🆕
دیدار فوق حسااااااس
پاری‌سن ژرمن
و
استون ویلا
رو با آپشن های تخصصی در
MelBet
پیشبینی کنید!
💯
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
📱
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه ای، مطمئن و در کلاس جهانی پیشبینی کنید!
برای ورود به سایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/103426" target="_blank">📅 11:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103425">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/870f9db185.mp4?token=pASKbcx1dQE0VjT1_kzbSiTkxVoMsgmf7ZlrCmrHl8z8JP_HtHsJSkU28Kh0_YL-n2U7VyP94djIjw5B53VYE11Nh71A1T_jEdnE7yeyilpeldgpVhr51UCiUAlJUY2lXuVzG2sWI-wb-kTwJXh_WbeqZhRtFHeNMUDwAAqhV4GsWDyQyl-XPxMbg64VxIkrDY_e812gitJsrj6VJZDCp7I3xfzo_KiO_sMiYKLhk1zY8SXCQOTqLrMBD4iHKGEdG9uf0VDStr8I7ER-uwDKwYqi5WCnzxTfONxA1KAd3O_SRpirQ6HMxetl2bC8NHrcj00vn0S4SVI6N7A43wwFU4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/870f9db185.mp4?token=pASKbcx1dQE0VjT1_kzbSiTkxVoMsgmf7ZlrCmrHl8z8JP_HtHsJSkU28Kh0_YL-n2U7VyP94djIjw5B53VYE11Nh71A1T_jEdnE7yeyilpeldgpVhr51UCiUAlJUY2lXuVzG2sWI-wb-kTwJXh_WbeqZhRtFHeNMUDwAAqhV4GsWDyQyl-XPxMbg64VxIkrDY_e812gitJsrj6VJZDCp7I3xfzo_KiO_sMiYKLhk1zY8SXCQOTqLrMBD4iHKGEdG9uf0VDStr8I7ER-uwDKwYqi5WCnzxTfONxA1KAd3O_SRpirQ6HMxetl2bC8NHrcj00vn0S4SVI6N7A43wwFU4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
😃
لو رفته از مراسم ازدواج رونالدو و جورجینا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/103425" target="_blank">📅 11:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103424">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6KuGbX2dg58CD8Ipk9p-54vV86QNv7cTg9mNNU4Fol9ctu9WQ9QiQF7lJi_my-aY9Pz_qIxXv4btlbYy7VFziGr-wiRarD-oXgAeK5kqH1BbGrH8-mLQoFV9SI1Vf5w6_wfTdQ_JIhnL-g7SbYOahIt0CbvYTh5RuqvQ6jIj1y2kL0F8SrfHIaGVIiTFFmAapdrS_1U_OKh6dicrEPKZy6_G7bRNquUi6bVkdem4YzbtrZFjR7ZWZcKc7bA3dxyJpes_MTO2L_E9Dsq3z-hsS_96HRWpXKcVLKtWHX-auP0KJn3kpLNPwWeudWqBu5WNVOxr82l7SRbENr6q01DmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
مقایسه افتخارات یامال و امباپه در ۱۹ سالگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/103424" target="_blank">📅 10:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103423">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c644437b15.mp4?token=rvCOMk0ApYNDxSrSDgeep4sWmHzILYlFKz0wDPvmML5TqFhEyVWqGVU2tacNwOupPoXc31fhp94y4EbFeYNIYHPZ0R9El-JEXA2gXVLKt8IhwStaSJ1760PbCgSUBf6xLrqCwjtPCdebl3W1Tjm_LsPu4kqutGS3cXyZ3Fk_drYGHrnQFqEtnTz7wrg03dJzIgApBtf0fRWmTkJtIC-vGbK7hN0jiNs9YnlwVJgDvk985jSgTVBZ-n1-TGSZiAHZVRyZTbMaJ4hTGkcRR4J4htEp-Hy8sBImt2c-YjfTrS1uE2GaLpg4T0GMd6XzOGRuKB7zXrvHuG7XEzuERZ2HmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c644437b15.mp4?token=rvCOMk0ApYNDxSrSDgeep4sWmHzILYlFKz0wDPvmML5TqFhEyVWqGVU2tacNwOupPoXc31fhp94y4EbFeYNIYHPZ0R9El-JEXA2gXVLKt8IhwStaSJ1760PbCgSUBf6xLrqCwjtPCdebl3W1Tjm_LsPu4kqutGS3cXyZ3Fk_drYGHrnQFqEtnTz7wrg03dJzIgApBtf0fRWmTkJtIC-vGbK7hN0jiNs9YnlwVJgDvk985jSgTVBZ-n1-TGSZiAHZVRyZTbMaJ4hTGkcRR4J4htEp-Hy8sBImt2c-YjfTrS1uE2GaLpg4T0GMd6XzOGRuKB7zXrvHuG7XEzuERZ2HmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
🇪🇸
اولین‌حضور پدری در تمرینات بارسلونا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/103423" target="_blank">📅 10:21 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103422">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gom1mcBYpapmKn8AeYYiRyEhrCgNZBETsiU26PY_yIrRzTAv-APx007-Gbq9v5GjG_FQOdbvBQUKzsX7I_HjRnx9ShWQEvuX_tfeoMM48UODFDLiZJU2janVUjGTPf5d0PauyPp3DOUJpNAuLs6uVoBdSbXKQpVs_bGngsUyurVrCahEb7Cy8RPWz7d5hUvXPUVJttR2CZb8nBnIsMgPJSERyZHCUW8C9E6C8cZHBd0rCXb1N4it6zZHCMuK7CqYs2WN9emTYH88e1Zq-YTlNPYdZOeaVVyXPNPW0_gm0iesDAmL4Ir14nlqMo_RcHzd7sZee-MkzAGaBs9tVvk2MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
❌
جرارد رومرو: هانسی فلیک علاقه ای به اوسیمن ، ولاهوییچ یا لائوتارو نداره و فقط خولیان الوارز رو میخواد
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/103422" target="_blank">📅 10:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103421">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDmTF2Ylssby6oGHC1tvu0fu2tvnnZAKlUSOT34jM7z14ifUcMleCC2hw9E0_4iC0KPDIoTX-LBGkKWr3Vkgo0aDY8JliyfQAC62A8rWBlzdNOfAnXb3paCr0xszHtPlnvbuUZgChJ0mUwT18kQPH5WFtHvdwQdM5rWTU2ujTNqJQ8m--5Ij6E5g-YW1TcNqB36jCxWelvF31dSx0mRe5MMj4lvwIjNz8F3ppR7D52B7mnFg27OvJQ2VTrXvZ--U2IP1CSqIQGkVI7cgxWhOZIhvqsCAxeo-C1TaTzR5DzUeV2FyEYjXkHvV1Y3bXPz0gngGL2r_14EkxmWA_3RL2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
✅
تمامی قهرمانان سوپرجام اروپا به بهانه بازی امشب تیم‌های پاری‌سن‌ژرمن و استون‌ویلا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/103421" target="_blank">📅 09:49 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103420">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cY0GsCXFv4j--HUJJ962-TNtLO7ETJR2cbqfa3VNyUz5lVV0S2YJEadEpVtJP5SgyoEDq5_NZYHFjykIznHqWlGCKwCqs6kTHFkaGE0FpMn_mwaXEIxinufAsXHPLWZcG9KyrOmiLbEGxzi_nrLlFJj-q3AHKvb6Mus20GRf0eUBFjHxQpGaT9TEyNaLF-S42Rqjhbb0dL2KBwKZUjaLpL77t10OQGan6Axu9ozIKYNAHUKeN8aaCEFHlUcHUJXg95ephvcCQjUHx0EqqpLRa4yBZRhB2cv9z8zQNJytlRo4lbsZCIt8AMWtH9Hx4BPZbRskaAt-GWLkbpAnJTTNNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
اولین باری که رونالدو و جورجینا این دو مرغ عشق باهم دیده شدن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/103420" target="_blank">📅 09:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103419">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea09ff2dc9.mp4?token=H1WSLL0zFPpeZOmFPIS48SQZjo_8C6ADPQvsq7W8RENy5mgyr1H3kz_pcvSZGdkgHi1C-jzUqqeNLIZ5UBMDg04-E9n453DytZBhHE7mFu8Au-FAaA3kpC5IHfkRZlYz-516VbpA2wjxXwLST157x1L7H2vP2lr97LKZ57Cm1X7e9h3zMpE11veH8Pkm3xir_7lYG7W3nPLvz0Et6I1etEOFpWEXgKQ0Xq0tYMsVKEtDuFQRcqQOnzz2Xz4aqWZmDHxByvZRgr77nK6nZmAxMwH98Hh3xctL7eMbU4GtENLHIB-qKOftA1knheU8dVmnyOFdug8udvyxo5XHf2PGEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea09ff2dc9.mp4?token=H1WSLL0zFPpeZOmFPIS48SQZjo_8C6ADPQvsq7W8RENy5mgyr1H3kz_pcvSZGdkgHi1C-jzUqqeNLIZ5UBMDg04-E9n453DytZBhHE7mFu8Au-FAaA3kpC5IHfkRZlYz-516VbpA2wjxXwLST157x1L7H2vP2lr97LKZ57Cm1X7e9h3zMpE11veH8Pkm3xir_7lYG7W3nPLvz0Et6I1etEOFpWEXgKQ0Xq0tYMsVKEtDuFQRcqQOnzz2Xz4aqWZmDHxByvZRgr77nK6nZmAxMwH98Hh3xctL7eMbU4GtENLHIB-qKOftA1knheU8dVmnyOFdug8udvyxo5XHf2PGEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاوووو عاوووو رامین‌رضاییان چه کوفتیه دیگه قرمساق
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/103419" target="_blank">📅 09:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103418">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZna2gX0v_AH-fScEaM505wyrLalrWFvnGonBBviMhknq4awn9Bhqspsv9TSntu-QhHbvoDEUqV1VP3j54m1SWlWYKPHAKfgPViGy1gAI4j0V6x-JJUtqPVcMuaCFxKGMRGRCGKHQDwmGFvgFOQHAtwtNCLPBCsoytT_MwPL8XZfNmZk6jbwiTs-2KsK-eI2_eaaRd-m0A98cyMasmsozysCRPt70rSJUaxolp-uETOTL0gLCFJZbzO54uSF7glA9PCV3MZ-BQsoo_hEHKBjN_g_tTAWfgw5EWXHgEUhNSdJ_DDmIh8S6PVdL2zLGcVT5BAR1mlZtFnwns4fOjgMZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇹🇷
رومانو: دوشان ولاهوویچ به بشیکتاش
HERE WE GO
✅
✅
✅
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/103418" target="_blank">📅 09:07 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103417">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fcd964c7b.mp4?token=akoQ48m3AjDixnrhyxPAkHFzfjG-H_p8k14wCtqCf36Es1CiOKnFDE4zyjHT8nfJk5b6xvByLwY6tXKvPE_-7rQHdd1Rocnq9K412lrDNpIElwBSvqwRypG4xPAgsTIx-vsS7d10QozTV_fM05heCzUdETXnGlC0_2-9fS-FWPWYdP460t4UPHxwHTPgB2wYOR_vGb58bzVyzhoItJxgMzChTaUrcANNvqnJ0iKYb8_WWpr89i3JNl1KDGsP5FKqmlDVEEYlvYUQ9B57ABg5G3xWA5mphzts6wPsG67-lrADUc92KsFx3dBKluyk9gxXBhyyug5foCT6VH5ZUleDOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fcd964c7b.mp4?token=akoQ48m3AjDixnrhyxPAkHFzfjG-H_p8k14wCtqCf36Es1CiOKnFDE4zyjHT8nfJk5b6xvByLwY6tXKvPE_-7rQHdd1Rocnq9K412lrDNpIElwBSvqwRypG4xPAgsTIx-vsS7d10QozTV_fM05heCzUdETXnGlC0_2-9fS-FWPWYdP460t4UPHxwHTPgB2wYOR_vGb58bzVyzhoItJxgMzChTaUrcANNvqnJ0iKYb8_WWpr89i3JNl1KDGsP5FKqmlDVEEYlvYUQ9B57ABg5G3xWA5mphzts6wPsG67-lrADUc92KsFx3dBKluyk9gxXBhyyug5foCT6VH5ZUleDOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عشق و احترام لیونل‌مسی و پدر فقیدش
🖤
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/103417" target="_blank">📅 08:35 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103416">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22164b16b5.mp4?token=ANVK5zThBsj_LcJDUA35emlTB4Kpu60mb7r_k9pz-NwadKCaeRuWbrk7uF3lu_QbiGn-PxWqmbD4ZqeSkwRz2QuKUBPc-G598c017GATgqbyy0dmzyqe1Hxu2t3gxkSsGxDMBXIjgiVHStJsufMUiG304rhJwvynLwAhKQ8hHdYXdVISbXFt493q9JqR2Why8P3fvN-WFnBj01NRPGsZLNI1aK4I1ksPnUnD4mPYaVgnuZ8N1YX6P5x5MVFBY_6Bf0pepgf1_SxogIbfvN4s9xbuFl9ptGVd5f37wAzhcHH_VIfmEAcXgIYVVteUcIKAwL04Z95Ey_RC3rmQtSjxDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22164b16b5.mp4?token=ANVK5zThBsj_LcJDUA35emlTB4Kpu60mb7r_k9pz-NwadKCaeRuWbrk7uF3lu_QbiGn-PxWqmbD4ZqeSkwRz2QuKUBPc-G598c017GATgqbyy0dmzyqe1Hxu2t3gxkSsGxDMBXIjgiVHStJsufMUiG304rhJwvynLwAhKQ8hHdYXdVISbXFt493q9JqR2Why8P3fvN-WFnBj01NRPGsZLNI1aK4I1ksPnUnD4mPYaVgnuZ8N1YX6P5x5MVFBY_6Bf0pepgf1_SxogIbfvN4s9xbuFl9ptGVd5f37wAzhcHH_VIfmEAcXgIYVVteUcIKAwL04Z95Ey_RC3rmQtSjxDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
▶️
یه‌ویدیو کاملا کاربردی برای دوستانی که باشگاه میرن و میخوان بدونن هر حرکت برای تقویت کدوم ناحیه از بدنشون هست. حتما ببینید و برای دوستانتون بفرستید
❤️
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/103416" target="_blank">📅 01:34 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103415">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qT1blmqPo7kJ7jMq2yV_9e5d4Qn6cTRln8r9_oeF0SCl30ycZGX2z4ZYTDzoQSdiH6l5joHXy8Cbvi1qYWUGh_2yoYDnODRhHnxK6ygsj6RmkyAH1H-eTXZ_8Ku8YsU1zuJxO4lwS-GXvadiQ-MM17zs3BOlKKkLNalHswBba6w_lbRYvIMlOeeVa2Qb1K1NPQm6vMbniuzN8C9skMNec94EjpUEvQ-LGDJXq2NtJMe0Vm0l8ZLVlhVnQBxIF9MZVViE3gb-riCozZs1sjnQrqsQEtSGYNpq-vlKkGnLvSZOHbWPgp3Fja8qS1S22XOV-s6HsvL4ikMF3OESZALWAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
رومانو: HERE WE GO فران تورس بزودی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/103415" target="_blank">📅 01:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103414">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/038cd39016.mp4?token=rIvON15YNBCZ2at9CAmM63uiffkAS0dl7kGTSZzzSjbKMiCneLbsu_z_E_zXgeYcNuwshpcKaCuWYCZfdIZptCjQ7n3RExxoLbLf8D64IYzkB8yRvRlO4_XaFDuFfZ96lnj96q1vvtuJtrWGP4UWdbQ-_U8EXns_7CQVA6SHPG_UEwTJCNSv3MSsOzFXfoy7H6q3oWqpP9jHIk-1zCjE7Bzuk86D0ili7ttyjgEMt_gb3f0yz3mbe4p3S1t9JwnvOlR0-LoJFiEBcjOnuPUknY1gPmCwfL-rTYQas-GbWxkkvmuoimSJvsPDEOdEY2RjNRnZGBQILXeQi1EdzN1zyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/038cd39016.mp4?token=rIvON15YNBCZ2at9CAmM63uiffkAS0dl7kGTSZzzSjbKMiCneLbsu_z_E_zXgeYcNuwshpcKaCuWYCZfdIZptCjQ7n3RExxoLbLf8D64IYzkB8yRvRlO4_XaFDuFfZ96lnj96q1vvtuJtrWGP4UWdbQ-_U8EXns_7CQVA6SHPG_UEwTJCNSv3MSsOzFXfoy7H6q3oWqpP9jHIk-1zCjE7Bzuk86D0ili7ttyjgEMt_gb3f0yz3mbe4p3S1t9JwnvOlR0-LoJFiEBcjOnuPUknY1gPmCwfL-rTYQas-GbWxkkvmuoimSJvsPDEOdEY2RjNRnZGBQILXeQi1EdzN1zyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😞
😢
مسی وقتی می‌بینه رونالدو و جورجینا حداقل تا چهلم پدرش صبر نکردن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/103414" target="_blank">📅 01:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103413">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VpXz6zPfOCBzvr4WyHUSG1hzUKs1T5dv3CkyjWJddcO4NCfuNGKWdvQafjyhAjSGW_UvLxcM-wpdVW6jf8ar3KsSg59tbWfZfwq2nLJxc31CvFl9-3b1VUQomBciwchVk-kQprTyIycelQx5GLcywPwyZ-5fiAHYM-lUVvNKbalHaRUkAwypRe5fryqQbcAm8BRIx8Lua3jG06qjGIKhlqp2JGHVKPwqdKNP7txZCMTcCWXFeyMNMfhfMGL9ZoyUSL13p6lYdTf-a5gEW2181pGnMkSKKta2Wp8m5EyBQnpUDqysz-b8anG2VbJ_7sri2PZ14-tcYt-Nwix0jVu--A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
#فوووووری از رومانو: مذاکرات دو تیم استون‌ویلا و اتلتیکومادرید درباره متئو روجری در وضعیت پیشرفته قرار داره و بزودی توافق حاصل میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/103413" target="_blank">📅 00:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103412">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKrI26iejkKh2ZJ8QK-qpRuJep8n6mTYrIM9Ba1lp5_IRcLHK3Ea5DzCLqJviC6NfK0Q5ymo8luzMsngd2fLlTi50oZLMI4v8Tq_iAoobYeUIyM-HkqJVUdKKmESV-NAhlb-vlnBfVh5AwzG3kpJCYky1jDmNutzMXo_pBFZRWdwTPF3XNpqOt6QKtT3pH7l15Ex93G9e0LhCP0nieyJa8_jOxH38CqdzrygVaDaB8voOQnuemwJuAYWCzj7xrHbBjTgR6qPhJveoCSjadR1oduw0W9PrrtkD1L1N-gsS1GwGqtiK8YOKtlcitCFHD9_bX2Z4AAiaRjMUefe63kq7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوووووری
از جرارد رومرو:
🤯
🤯
🔥
🔥
🔥
دکو مدیر ورزشی بارسا با وکیل لائوتارو مارتینز ملاقات کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/103412" target="_blank">📅 00:44 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103411">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLuEJx8Qp37o39CquVsNqDLpdvA10u4KyBcnt0tvUVQCn6y1CJa8F7hDCcVtZLRmtD5z8s4yLNzGJzI7MejfuwqVMPFTjWygSMtRIL5KeimgMCHJxTn0oZHR656uCy9dZpfJuT4B3tr2uPlYKEqJmwOW1CD-kX5gDrzyrOQHarcFSKL1DwV_D3wLZyyueLEd4kfS6ubZxD5vqS03U6saCFgOCEAKKHjjU6M7XsYRSQ7Vi1K6aI99-KudsSs0CcUJ_W-Ex1qkjKKUOlJJYQppb5i6dP7TG5-KbAWzVtVyp4YI9RgFH28y028f5-ozLKpna7VT93PiedDWKgjuvBG4Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇫🇷
#فوووووری
از اسپورت :
🔻
بارسا و‌پاریس برای فران‌تورس به توافق نهایی رسیدن. ۵۰ میلیون ثابت + ۵ میلیون یورو متغیرات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/103411" target="_blank">📅 00:42 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103410">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObaWZ-ibng1FXVcZjOC5pmcMIW8Glh2pKummKVTiqhRDJnw0js40IDLe8qyYnIn19SLdyObl779PWgoQ3HfyL6-Qp9k4EkmVydP_3TjaFDi3cSH2OLt8x-tb-JP5N3fB2hXWw4XXsbOhSPyInON_ydkTuX4W2cd8a_aGItIL8-Dqkbs5fuYesKi72K3BmS2QgPyabBUdUE5UEXOFDqIJEUMaGXI9pkNB0mlLlRJB-PSE_mjiXCLZ90GrYviBm7Kinlqv0jOx8IUY3_cwseyHSInKEwmf7YHkmPW6z3An-GATUKUBx5hFif9ZZKod-nPcd6liQ8YWe96NPdewmwUSLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
🇺🇸
#فوووووری
از نشریه The Athletic:
🔻
دونالد ترامپ بزودی شخصا با روسای جمهور کشورهای مختلف تماس خواهد گرفت تا صندلی ریاست فیفا را برای جیانی اینفانتینو تضمین کند. ترامپ بدلیل روابط صمیمی با رئیس فیفا به وی قول داده که تا زمان حضورش به عنوان ریاست جمهوری آمریکا هرگز اینفانتینو از فیفا برکنار نمی‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/103410" target="_blank">📅 00:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103409">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c334f75417.mp4?token=J8h6E_9FOr1wrGBdLk1ZcA__m2TrWDiUTbWPijNUL1kQuk7ExcY4Wced-yZUUXiWThhJXk4f2bLgc1Cwl_YPUA5RZOmLTtuFWcnTgtW51mojwBufc0DQ4RBJDQAi3aRq1oF6FfN_vbkqm2rYRlEXeDfCi-8vQt5lyUqA1ZcOyqsHMq9fAvxAaZBoOdvh7akGr-ShvvrcecFDOhE3V5GvZTOl-Th2xU1YLP1dr_zC4muAlrT6pfD-6Sl1Qc9Bus_o5jSZP3pZ1kJbD72loOBxyhF6g-BTSmpRZleKcLtxRXBBwdsV_MrMgEvwKSYy4qeYv91aMkDi2rpIF0aKiXQniA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c334f75417.mp4?token=J8h6E_9FOr1wrGBdLk1ZcA__m2TrWDiUTbWPijNUL1kQuk7ExcY4Wced-yZUUXiWThhJXk4f2bLgc1Cwl_YPUA5RZOmLTtuFWcnTgtW51mojwBufc0DQ4RBJDQAi3aRq1oF6FfN_vbkqm2rYRlEXeDfCi-8vQt5lyUqA1ZcOyqsHMq9fAvxAaZBoOdvh7akGr-ShvvrcecFDOhE3V5GvZTOl-Th2xU1YLP1dr_zC4muAlrT6pfD-6Sl1Qc9Bus_o5jSZP3pZ1kJbD72loOBxyhF6g-BTSmpRZleKcLtxRXBBwdsV_MrMgEvwKSYy4qeYv91aMkDi2rpIF0aKiXQniA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
✔️
ده روز تا آغاز لیگ برتر انگلستان باقی مانده است. پائولو دی‌کانیو، شماره ۱۰ وست‌هم و ستاره‌ای مشهور به خشونت، در سال ۲۰۰۱ جایزه بازی جوانمردانه فیفا را دریافت کرد؛ زیرا در بازی مقابل اورتون، به جای گلزنی از موقعیت حریف، دروازه‌بان آسیب‌دیده را کمک کرد. او ثابت کرد انسان‌ها سیاه و سفید نیستند.
همان‌طور که تالستوی در رستاخیز نوشت:
انسان‌ها مانند رودخانه‌ای هستند که آب درون همهٔ آن‌ها یکی است. هر رودخانه در جایی باریک و تنگ، در جایی تند و خروشان، در جایی گل‌آلود و در جایی زلال است. به همین سان، هر انسانی همهٔ قابلیت‌های انسانی را در خود دارد.
👍
دی‌کانیو با این کار نوع‌دوستی ثبت کرد، هرچند رفتارهای بعدی‌اش بسیاری را ناامید ساخت. اما هیچ وجودی بدون تضاد ممکن نیست. نفرت یک انتخاب است، اما باید فراموش نکنیم که جهان سراسر خاکستری است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/103409" target="_blank">📅 00:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103408">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/103408" target="_blank">📅 00:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103407">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=Q_qe8OOV0ZjL_CDShBLbgh6Xqwcqs-r_3GbwNiCMhzMNlOFG_06jhwymXspYAlYpaPPrunYrbGPleE_sv138XeRLsfFxVWlSV1uOHbeGNoHfUd3ui1bsJR5_6_VxtskYM03iU9ipNOE9jVwlNu7_Mg8aPR3iAzPU7SDrslAeJYXzOZzLw_P5kZAR58uGeJVbbghVYEePxazy0c403_b3iT7vEbd-j5kYAQQLkqzrH9n5xdqt7cXlV4JskgLRiPOQ-_5PyCL8Bjjp6wnll5K8cPw2JoG47DfBp4eWTdff7xKAiE-Uqn-U4ipXSJZsTXi6S4DiI9S25i6blTkHKyjdMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=Q_qe8OOV0ZjL_CDShBLbgh6Xqwcqs-r_3GbwNiCMhzMNlOFG_06jhwymXspYAlYpaPPrunYrbGPleE_sv138XeRLsfFxVWlSV1uOHbeGNoHfUd3ui1bsJR5_6_VxtskYM03iU9ipNOE9jVwlNu7_Mg8aPR3iAzPU7SDrslAeJYXzOZzLw_P5kZAR58uGeJVbbghVYEePxazy0c403_b3iT7vEbd-j5kYAQQLkqzrH9n5xdqt7cXlV4JskgLRiPOQ-_5PyCL8Bjjp6wnll5K8cPw2JoG47DfBp4eWTdff7xKAiE-Uqn-U4ipXSJZsTXi6S4DiI9S25i6blTkHKyjdMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
➕
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
a20
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/103407" target="_blank">📅 00:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103406">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swUFrPWEox8Bai0gsxNeNMjqZbYT-PDsz46tZnFjx1GWMPJo1voBk01rH4i-BOPPZIZEtlT4Y9pEiQJxNeow87MgNpASaNaz1YgQvneQlWvbzXKlt7hzl0TGDul4ridmnlbakjyuFjLRnCKkjGRk_jsSHyte4ScYlNjD-BYhFEfTZoB2npoBGlWCnfXFL5yvQGYfh4P6muGOFdgY2V0n6NrRfMkQac04oXd3odCncwIjCFWCheICg1jLmEWKewxmCzopcBuhiVOXGDLzWFY8UnHk82nmuJrn0EOo9PiGpcFC6YxycV618WNE1E3n9sA3kIbELMc5CTbgse20R3wUWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇷
کسری‌طاهری بازیکن نساجی با عقد قراردادی به تیم‌فوتبال سپاهان اصفهان پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/103406" target="_blank">📅 00:01 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103405">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkfCBra3R6l4GPKGYHh9X4MB5jzk8YscQnOnc2pvv8hPR0P32ygdqKbRZqggO_AN4LYt4Xt0jIiom8fA2y7XQwsh0hPWVOWyQEqmxXGZBGP5hIGb989zgrs5KJ3FIU-8gY1kuqtRrNI54XQPxLiioeU8LPM6fW1BhTO7R5JlzwxPrZL_mPvKG4GWyTTcT4IiC06_1VuulL-Sr_oL4lFFtoMN1bd6mF7YxhUtmMpDmFz_okcH4-dn4naASZW3E6S5iDGaNxn-eVzeyxfaQUjFGK9iRWKGEDxwlouaQmtJUV5XdccBSAKJRLaJLq05zGbHJQbUWsw7k280g2Zgq5fUJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
ستارگانی که ‌تو لیگ آمریکا و عربستان بازی میکنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/103405" target="_blank">📅 23:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103404">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/agvf0lgaH9sp_zDmdl6P8INPKedFgwI5b5ThFwtyNYdYVtCTKMZqqUKU1MuNr813e3afEjEpdvLTickRvO8Of5lOw1jigT9fQef5EMfkZCRkKY5xHcRWw7tutH_9Gwj36zYz2ltkwtf_WYPgy6wkIVKUsOLBZrjDK7iQVR2rU-Mst2Z6CIKb_RGpsD-IMlhVkdjetEuRTv0p_rBp70BzzSCJ8pW47YdlZ-0X8makB8YaX-eZObI3jhrjf0bk26MpkB84iWUE4X313HXZuAGoU5zGqU9XdzaxaooLwEGY1sqL55oOv0rGhMWLtN6dKi7jJEmKHA49JuZ3rphPsQ1uwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
باشگاه کورنتیانس برزیل اعلام کرد که بخاطر مشکلات مالی توان تمدید قرارداد با دیپای‌ ستاره هلندی خودش رو نداره و این بازیکن پس از دو فصل از این تیم بالاجبار جدا میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/103404" target="_blank">📅 23:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103403">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmTQXJhuWc9HYT5t5222jzqcEHm9i3cwa4Xt5LQV_4QbumKhN8D_W6RJ5dld2WuVN8t1Qr-cV1XMXPlNz3AotblWMyHOqk-6jNxmEwwA-Lpo4Wh_71JA6asKQVz97uT-YwWxek-a_4TD2-__v1Q0hYEDiUUJAY4cgx6O1dAgrkhyufAJk-bcKl98gyksHFK1LxXHD_IpSaWoi14Yg-cRo350xOEmN9dnthrz4mTXrdjBDpJGlXRQMrDSqJnotgZI_NrYB3DZh0WdYyvR_ngaXA7sz57Sti_95MP1UD9-HBdVa6cyJ15ftkMzL2dlrs5-WZU3aMBEZfv8eX5rWoPFyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🐐
🎙
مورینیو (در مستند جدیدش) درباره اسطوره لیونل مسی:
او یک کابوس همیشگی برایم بود.
☠️
☠️
☠️
ما چه کاری می‌توانستیم انجام دهیم تا جلوی او را بگیریم؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/103403" target="_blank">📅 23:52 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103402">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUo-T6O_HQfhtJUiUGeJh3ZDSIDt6_r51Pya6TZIYqI6fN-CL3ekyHBhyuxx-qXYIY3NboTcvi9rmhKVFyR0Inc8g8mN0GL6lI_YAnXRoXj8QewNZDB3Hwq6QZmVSB8WaYn2NktFcHYUOE6MznwdEeP24TSo-NotjdQjRZ_RUbP-BtcNZJpbUZnjbEn_2MqKzO6nenPsf7dXXEUaOU5SlVanYaPBp-B-up-PXUjmjN1Q-7R_hCLCjKfyNqFK7BXSuCtRlWk9MecwoThGZNe-Yijrq3oHeWOTrtlRZin3aBVO2rtv-RSLf6azqkV4NKr3jj-BDyB16UwKDmXZgxzU-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رونالدو و جورجینا رسما زن و شوهر شدن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/103402" target="_blank">📅 23:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103401">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bjn4vxwaYU8-MamzzqYeG1mMtQQcWr6DdkOSU0WE8HPRY9DVcc_S3ZYuIUkSxfxJdGscVVhgFoWPMHmpy39Sn3_7o578kG4tH55Yw3nmwcGTIEYjoH9wUDyEk82kiblqgUqmYezO8jMGo7rsBuWFUEQqh6bURfHxsOKAv-V9o7_wkiCSqCmyvKrCuZ0MTePBeqHPRnzE6k1YMcKA1UYf18uDnrRAghg003-uOZI3l-FIiKyxTo6GICd7-0mIDTa6U3UQrZwVvsHP7HzkTBlVC0zOd19XEahEK3bIDJjFhdk-rzjjjfho8glHssP6vJDEaDmAjHHDIGBCfm139kyv-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از رومانو: چلسی برای فروش انزو فرناندز به سیتیزن‌ها رقم ۱۲۰ میلیون پوند میخواد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/103401" target="_blank">📅 21:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103400">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M93KxMN6wktTspCLvoJqivnl_F2kE1Xo2JnxLhs46fdLPtzJcEsJUm4Dp3KRm_nSJ7gJMmTmQEQhQ1dqdbULur67c-F0b65aIKuSWmThNdqOIHVoaIcxNuwvlUmW7g7qaH-dImLY3IYlQxAsUV2WsYCfzmkvIiOMUdjXQFaLE0ti0YMSqjT8ooeRA-KFeR-Q0D8PspWewHnEoH4LdDAsuFN9iHKBuEa7L_cZvVNqDlnBcZQPbY4-jpc-izbsqo8D0-1HNLJ0-VlUzFSgjOJyenG5yOuZ6Uz_oaHLjBJdjDTMi1hYsnqcKgajorrtWsvgi4RK_MAx7BkbCFOsVl8MKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
لیست ۱۶ تیم نهایی لیگ‌نخبگان آسیا؛ استقلال در سید اول و تراکتور در سید سوم قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/103400" target="_blank">📅 21:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103399">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/km_KLNVY6uWoCZW77W8-YLgjPdJq92HCD0fBhcthc95mR_p25ICoB2IzQ_5MNxJQCM_vavaIxqzaiGanBqUhaJvEu6G-IVagQCUOcawzhsHduxdF_NIh9h_YiXUCzpcB-nsaPdpoaXxLHegY7sJde5sAoe0LkLzNiZbmhqjSxsgPiusFMvXgJstEePoDrd5r28E1masnJMjC0Et4MBr8QnJLOSs948Y_rMsY6yb3PeH7NROyjwKFqB5HlhSGM-zw9Nmx-g0t1NcRMJDX1SRIJ0m_pqVH4mD9ZBlmwVXGd9Er0lMH7uzRXzGwAXQsDsEV4tpq8BOHsfZIGOl_h_jZKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇫🇷
#فوووووری
از روزنامه اکیپ
:
🔻
باشگاه موناکو بدلیل مصدومیت پل پوگبا قصد دارد قرارداد خود با این بازیکن را فسخ کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/103399" target="_blank">📅 21:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103398">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SefApAw1HNtXjZS8ztme6soyIxLN588AI2NqhV3qyVUb-3drM5PvFdO8UxXTdUKIHXFfGrTLblyROje_jJ2Z7po7P3yS95vp6eTXFJ8C4Nk40mDyH_dGy_uENaORPNGo9dSeluynYOn_W02mk4J0nY8NeAX0MR4oXqObou4Dc_C6VUF1VDwCZZKsjYfSmAY7j0_Z3GcwU5KIcmL7yuM9P1aYsIr_DA7gd6YW0f20vUP4UpQVDCDFHdwWFh30T8HkV7I9GHs4A-a5VObyXO0xnx-oemzLmW5DQfNA7O5Qq_qxCsmRgKcoehHo9DPp7MHo5AyNgsV7Oe9gefiZ-X-msw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ویتینیا:
توپ طلا باید به یکی از بازیکنان پاریس برسه و انتخاب من کوارتسخلیاست،‌اما نباید بازیکنانی مثل امباپه و هری کین رو ندید بگیریم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/103398" target="_blank">📅 20:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103397">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rb_J_35RiznwI8SZ0FDhcHh-GqwWDXa11CDTXIqK7mWKqBp_JJNPtlfqkPcGg3kzrLam6xrmT3rU9gQ2YjgLgHz2sKvAdIUeXKUW0A_x6ZFBJ_HHiWDDo0N36TH73lTAZkz6TD69J097b3u-_0slc5Oy4KvovhPi3dOBJ8iEaNiqjRWVXx7r5r6hL7upqHjUfHj9ohoMWiTw5kzAh86g--erRi03iqaHvStf9qdJLZ7263yTJoeHsMmeAm92bObL6obIRXB8P9FbgpWQjBjtNHp-sPFkXvB7nVavn0wBZk2-_db4edaca6dUbyFHeSA3xUKKLSmFe5hldE0UgQT5VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔵
#فوووووری؛
🔺
هلدینگ‌خلیج‌فارس اعلام کرد که سهام باشگاه استقلال بزودی به چند شرکت یا شخص متمول هوادار آبی‌ها به فروش خواهد رسید. مذاکرات در این زمینه آغاز شده و بزودی نتیجه نهایی به مردم اطلاع‌رسانی می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/103397" target="_blank">📅 20:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103396">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KpbSO25A70iOVbfL89RBRkf5t3cap_i_dmYhMaXPmpNKJHWB3FU1Ac4HHAeWKlLSaKp-HNIvwJ83-UEkepTL4brAQasJejveBX6_uKN2Zmy2i4f7awARFBdTyJRNDN1Ivnz4DIQgKCqWYarC00bfLUZNJMt6CG-6PDOI4YJ34sWj8L_YBXdodt-2Z91ZkNGDa1onKcGZd5dQTaJrSeSYUjYz1fieETe6ZbXO5os5OSUlkR2EhekNr5niQA3zk-u5AhO5oqTu_ekW9SVF5v5clmxqHWmTmvXHYQ9VdsE_-8QDWo0lvwG5mHrWg9TZOPE4zBxqM2SiNp6uYHltSwgjBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
⚽️
باشگاه پاختاکور ازبکستان با برتری مقابل الحسین اردن راهی مرحله گروهی لیگ‌نخبگان آسیا شد. مرتضی پورعلی‌گنجی در این مسابقه برای پاختاکور حضور نداشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/103396" target="_blank">📅 20:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103395">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZs4szVYRaCWAcBMblBTjS0CrAElk1wM7lpr-Sfs5VH0I8mGqtpzzrY-hwGWDItpS1irIFRKZSzabTjKUrMIIUyRZF_Vn-Go19gcTL-HCYx_d-NCfMmwhwTqS_lb9HFYtjFhX0sXW8eRw13J41TSYi93bx2WvpD2I_5qu6h_1Q4RjbyE0FmDB5BmcRJsPYj6R2HFj6gDeF4U8ABxaCF-fVD8uGvcvRywTgmu3TWPvxtGlnkmt566TlfpSvagBx04Ttz6J6LsH_zPPW9zKvDB4XyxwGgKHBAJO_ZDRNuej82uHPoscBTPzFmoT2I9zAiWL9UBcWOw75kCXLAE8OuSjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صحبتای جالب مورینیو دربارهٔ کاسیاس در مستند جدیدش که از نتفلیکس پخش شده:
"اولین سه باری که با ایکر، کاپیتان تیم، صحبت کردم، اولین چیزی که بهم گفت این بود: «اومدم درخواست کنم به بازیکن‌های تیم ملی تعطیلات بیشتری بدید.»"
"دومین بار که باهام صحبت کرد ازم خواست تمرینات رو یک ساعت عقب بندازم، چون ساعتی که من می‌خواستم تمرین کنیم، توی مادرید ترافیک زیادی بود."
"سومین باری که با هم صحبت کردیم، بهم گفت: «ما نمی‌خوایم به هتل بریم. ترجیح می‌دیم روز بازی همدیگه رو ببینیم و مستقیم بریم ورزشگاه و بازی کنیم.»"
"خیلی زود متوجه شدم که حسابی لوس و نازپرورده شده بودن."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/103395" target="_blank">📅 20:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103394">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAtt3s3_IjR8_zKoZjW_ILU2qtVnlPVBD-crUboGq2ZDm34IsiDCQ_n8GHMUSuFQ3xGheZrLOx5Wm1pkU-oc0JhB1KM-LBCVGxtRGEqthc8EkOtshGEwk3ETaWzdoSjvWzhmK7cM1itBcDQS--sCJfrRoFct6wSXcBpG4aIVzBNLf31mltlQMnqbx59sevfJJ78RDEzb7VmwDs_XAXvi4dPVGYrtMph8gmQZJe0zE0rdA6y9wOx1TTNRCBEYkKM9fG87yUvTssCxkNjAsKyLBBjw9EWdEtmj4YsNyTlLiEzmhonmaNL5XLNgPkKQNWD_o_MsQgFy7stdDieRFuQ4qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار خط حمله اصلی رئال مادرید در فصل گذشته:
🔺
وینیسیوس جونیور: ۵۳ بازی، ۲۲ گل و ۱۴ پاس گل.
🔺
کیلیان امباپه: ۴۴ بازی، ۴۲ گل و ۷ پاس گل.
🔺
یان دیومانده: ۳۶ بازی، ۱۳ گل و ۱۰ پاس گل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/103394" target="_blank">📅 20:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103392">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jI1F2SATI0hhIP3zOBV67EgF-mHLuHt-oxcESG8YCgW7oMoVQH-_eaEnG-pg02povc9klmoxl8nyI3A6xPHdYjl52EUck6pu687NbMP6USnhXNE6nP7Dq1hLOzBhtjHTNoN1EZk-2_P54mnwcVM5O-dwcwY6zI0JgWMSP3EXRz72Ogumi4OjKNHiayr6zMwk1X43nMV5gESoZE6IcqwDC35pCW8TmnUaZEFEM43Ly9892ZaR8ps5MZDrkFzIixpXflp-1uYmv7sOW99tb5XVcpIgkCarxUMXql3oS9lFNH6Piu4oNIhQPmFKQLVBN6OuUiDo88ynTy78vwXSlGzVmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fZkg51DN6Nv-_TAo7bkaeh5dqV9V6ojtU5wsANo1Hv6uhMf-7ffenhp14dQ0poW_xWvYdAdvYIaIgXGKH2dh-H21-nVBbq-vT7wVxhXCVvVfk4KVnjqXpsnBNIoZglFy-liEE30VYq86S0Xd1QpuEnRfPsGgsPeRcLfg5ViaEgKj1UWBoQOsfw5bjzmdpjQOUv6E_qPmnu4E1thjmjSE6d32gNJcmWx4DGsv07ZsshqwI7RuqsLZDAFa60oawilkP9TXi1paDf8cEopqZFpB6CG_yX6uW7b8PR20fq-88ot8uxDI-BwTS66b9Fz8cigTu-Enf1mJVK7KjogXC6Y-2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👟
تبلیغ موزی پدری برای آدیداس
🍌
♥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/103392" target="_blank">📅 19:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103391">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EILlzq9p5ls_RgSQMrZ32IqTYw3NugslMc-he4WBOSp5Bdjxr-02OOWXp_JXxIwqLNkojdMrbQIPFe7XjJYTWLuKaXrKQtsqT57_4ddNornvjmng6_mtWai1_eUOmN-Iyh7wkZk8mty4dwtiIOcUH2lC9PhU-rrvr57CgLMM2av0xbgBEc36jUSispbRm4hVagrrmKDGHeoTzNbbNerUVYNW_TwimAMiaWfBAo-9wrJozJNoYk-uVr50U5Bg23lKif1fC77920bc73Yck_nGtJC6SMg3-5ElCnGlhSj3_jc7aUQtVSDWjNCrtWEXc9m0kWqxt9-Vw2UD4Jdojrg0Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دوست دختر جدید گارناچو؛ خارج از زمین فوتبال اوضاع واسه گارناچو خوب پیش میره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/103391" target="_blank">📅 19:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103390">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf2ed3bb71.mp4?token=UvbA-LYk3izK2CnZWgBCzMzMckDRRYUpACLEjx5vfMVhiKzmIZvLIXSsw9gkgii1koN093HalxXaOz-XwOtaPPZphOG02RxxlWuO2GYKyUteyx4JyZqMuflceJu8AaOjJSxao56MhbPqbrGLq6bPBuErkqAbqgroj19eOQ2bqANUkZIXZbNoePfj-WIOCnFOXv1YjAmtqRAUlrODbXQNnFmjHjj_TTWYCjch6UROOM4LxnYQ8GRLC6TCSm8rnYAi9v5i-uQdSsYCOIDsu1T0zmW_T2v4CA9F_Mw8BV7EjinJAgHjlUpUzKe0LPaEbEt_KlI9NqXxjWmIhg7lgE-Ptg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf2ed3bb71.mp4?token=UvbA-LYk3izK2CnZWgBCzMzMckDRRYUpACLEjx5vfMVhiKzmIZvLIXSsw9gkgii1koN093HalxXaOz-XwOtaPPZphOG02RxxlWuO2GYKyUteyx4JyZqMuflceJu8AaOjJSxao56MhbPqbrGLq6bPBuErkqAbqgroj19eOQ2bqANUkZIXZbNoePfj-WIOCnFOXv1YjAmtqRAUlrODbXQNnFmjHjj_TTWYCjch6UROOM4LxnYQ8GRLC6TCSm8rnYAi9v5i-uQdSsYCOIDsu1T0zmW_T2v4CA9F_Mw8BV7EjinJAgHjlUpUzKe0LPaEbEt_KlI9NqXxjWmIhg7lgE-Ptg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
کالوین فیلیپس هافبک دفاعی سیتیزن‌ها با قرارداد قرضی یک ساله به شفیلدیونایتد پیوست
منچسترسیتی در سال 2022 برای جذب فیلیپس 50 میلیون یورو هزینه کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/103390" target="_blank">📅 19:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103389">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EHg50gMAoi0v_TC2hHDXhLkcGqQ1KwRIti5-twKMYM4sfz9dLFbthCATzdONddSU28aiSFxd5nbBZm1cN6mBtLLXlqztYSJa9j1GueQlUPQz13lLcP0gc7Yyhap7WthNF8aUfCEgAQA1pbHsFj1YxJa5WLBrk1ga7dZlg_RDRdWD6rHOd_xHFVREMhp-Yre3aNSXhqTCwhjMCQ1V854rwwtzekeDE0lCZFy5MuZ0tG8SNltEHcX7AaTnzmjb_f9GlnuXRrYCAbGrmS7FYiAWdNBmX0pJV4BhUhPbpYnJ06MxNc4K02NVMiL0GNvfStAyhLKqsqxz-ETL6vyv6_h5Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇦🇷
خولیان آلوارز بعد از تمرین صبح، مجددا به مقر تمرینی اتلتیکو برگشت اما این بار به همراه ایجنتش!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/103389" target="_blank">📅 19:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103388">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🇦🇷
خولیان آلوارز بعد از تمرین صبح، مجددا به مقر تمرینی اتلتیکو برگشت اما این بار به همراه ایجنتش
!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/103388" target="_blank">📅 19:30 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103386">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DwiRwpEOi5hhqZ9UR4u6gV9owQbAVd3WMJqFgU-9r20--eFCjJ0MABC8HXy6yvMoKDiJc6jh2WvOTri_nwT99_VtF8VY-Y8sw4yijN8bu2VNN2vdTaw3i1DnzG5Kknys20KQ7H9eunyyoK1AIZ5ipr2QkOTXwiU5lUzsEn9ZuR4jixBFgqsXbR-sgWFeE6R9rVK3DgOeW20EmUKptAdfcIP6uela9VvLyDI9I0yFbsetWoaZ0Yh1ADRVbO0mXVEOVcYUb6UeejaH7pw7YPrY0siloNnKaF6HdtqS5oF6xqMVryome9-wVnQnr-Dpna7dthr07TNviEEw39D11W_rvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bv_9H-piqgCEUQ__VS5DyQLo2L3h_CQncfFBCyERA7rw7_oSQ3dCmLivqzKM7VixXZZ6W5cJR9tsSx5BoqhN4L4yp3tZG8-MQMO2ToZdSrWeIjAdjodWvg8KVchxbbCc3nH7BMntU2LfI4EuJlMU71pI5e9HhsqSBNTIYjcMHhntz_UMjN5UCuko6D_1qIQDQrJPGkx5Yv4k5gs7dMHoWNHuOw2NCTBPlWiGAOkoua3QhtZY4Twn-ZG6OiOoKBmOFXKl8E1LMkgeuyEkV9kaim7tjkpTr37XeOGj91t99swB_wPoFA5_DQjVKlqewctBLkHQ_Zz7UnOYmY1S6ihrig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
امباپه و استر اکسپوزیتو در ایبیزا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/103386" target="_blank">📅 19:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103385">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwwzRAfnzXL-bokPbalFzoLF9u0Q38XzKbF674niDzpsjgVdUyIHjnrUSyBt-lQZGjf7cewaLNRGdrhL0N_ydPYYnkP_JWiyVON49r4Dowu6981yG8x0vLpvSnqHFV7QV67vTyTfCgKdCTWeSbQ4LbPjDE1TVO4O4iGivWQedGR5QL-b99XnPlfKVdTs4_3qf9ishUrdBgNe6XRaaWDzLNMlkveGbSX1UhrpV3Y7fSxrdlNbkZoPuPWjmbojJC22_btDHcbyXtA87l7IdnjH9qQc06lGyo_e0yN2qkGH4wD017YW-TlJysy6Yr72YQvkanuT40JH2dHEgVufF3RgIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
واکنش روزبه سینکی به صحبتای دیشب رضاییان:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/103385" target="_blank">📅 19:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103384">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DENRsVL4CTIB5aDzLWMXMZrSkf8em5ZaF_2M5f8EwyxfHH_fGYR3yS59iQkvJb4xLw3zQQBIFkLxo2716v4Dwuue5-MHnvfARhpaBPG_VC_ogKVMGCCitIE3TbBjHZmptpMy7V21BMcgQt6ZOF4oGP9uIhyL8aQ6_Zh7yp3cT1zI8oSshTxIC5Pnfr9b4hFI-8LodTLtnmQJUjxZvAMqCI5k4m-LQ5QUr3s97SRRLP4H2ecw_N7JvOQq5q1QQ1sGhlV-Y7_xqTdaeG2z-dq9ZuiEYFKiGbMT0lYK-bSYIgjzY0jh5w9Das772dRl0rWF4BJqIc7OyjosraXDLeyYGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🎙
ویتینیا درباره جایزه توپ طلا:
🔺
‏
"به نظر من، طبیعی است که یک بازیکن از پاریس، مانند کوارتسخلیا بعد از فصل درخشانی که در لیگ قهرمانان اروپا داشت، یا دمبله بعد از فصل فوق‌العاده‌اش، یا فابیان که همه جام‌ها را برده است، این جایزه را ببرد. به نظر من، رقابت بین این سه بازیکن خواهد بود و من به یک بازیکن از پاریس در توپ طلا رای خواهم داد."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/103384" target="_blank">📅 19:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103383">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63fe3eb369.mp4?token=hrU8mNDQAlfIkumX9LgcRRbHmpDU0jjDAW_fmX_t4w2elNTF_4fpChqcOQDiv3s4biTPMPT07qRFz1zlKH5O3YwDW4nwbp2F51ctDmSd0FA-cloQpdYMMBkg25eNMQ6XjDNVVN33-1_14wwWMQCibbPJY50z57ZVAuPqkkDHaKURos7TgZw7eKVay0rI4VyDT_Ef-r3s70RVmyQkztQWRERVIPLYIVOkQIw7lV8PvvDSEvYor68uGkU_De5n18cA4Ez40nan9M4NSEHo2uyWcnyDmnnp6qpn2QJiKmPa7zd6S-LZe7rQlnfl02Zb6I8X4bUCmQ5fvsy_xBiEb8soBCbcHWdTXHRdrS0eQeHFywI7tbmFFDNHElhcpIutzABy-IHjExsHQncHA2DEeeRxkofCygyTVPcz0oYpPFmNq744bS0hVgEFymE3q6LBfG6Ol5ZdRsIjwsZyQTzeK0R5XFWPxViulmQKJSgLoCjoh423eSpNQYCvdPmXMdyOOJ9B5tB3e6ktSXwQpWiNu6JGPSV9OibmX1B91WXOJhSXep7L43co4ygNA7v72dlYeKs1aOlL79J9GhLfoHFup3TIA8MezqPBSJl__SQVRPVFlQ5ypFy0xg1XoGpQ4JD5WzfNMEz9BO1MEX8jbpoCAmrqTRp3n1RtPVDKP_3wWVNiOCc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63fe3eb369.mp4?token=hrU8mNDQAlfIkumX9LgcRRbHmpDU0jjDAW_fmX_t4w2elNTF_4fpChqcOQDiv3s4biTPMPT07qRFz1zlKH5O3YwDW4nwbp2F51ctDmSd0FA-cloQpdYMMBkg25eNMQ6XjDNVVN33-1_14wwWMQCibbPJY50z57ZVAuPqkkDHaKURos7TgZw7eKVay0rI4VyDT_Ef-r3s70RVmyQkztQWRERVIPLYIVOkQIw7lV8PvvDSEvYor68uGkU_De5n18cA4Ez40nan9M4NSEHo2uyWcnyDmnnp6qpn2QJiKmPa7zd6S-LZe7rQlnfl02Zb6I8X4bUCmQ5fvsy_xBiEb8soBCbcHWdTXHRdrS0eQeHFywI7tbmFFDNHElhcpIutzABy-IHjExsHQncHA2DEeeRxkofCygyTVPcz0oYpPFmNq744bS0hVgEFymE3q6LBfG6Ol5ZdRsIjwsZyQTzeK0R5XFWPxViulmQKJSgLoCjoh423eSpNQYCvdPmXMdyOOJ9B5tB3e6ktSXwQpWiNu6JGPSV9OibmX1B91WXOJhSXep7L43co4ygNA7v72dlYeKs1aOlL79J9GhLfoHFup3TIA8MezqPBSJl__SQVRPVFlQ5ypFy0xg1XoGpQ4JD5WzfNMEz9BO1MEX8jbpoCAmrqTRp3n1RtPVDKP_3wWVNiOCc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
رختکن جدید و سکسی استادیوم نیوکمپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/103383" target="_blank">📅 19:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103382">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bbef9d0be.mp4?token=oMySH0oGFS6yIA0WSF5rIFy0__StAerwyt6M0EdPzt6C8RPHEYWeAQrChLyK3p7abnl1x39vInlVRqzB2Knpg35OoD2KQ4BRTbCTl08DLlcHz_4f6ippkKRs31oF0r_5ShKqodc_MgZsa9p6wOIbCllkIQmSN06Yg1o2uwX3noHXYGk7vjy_rFG1cLZbDVUvp4-k5_wKKqkSln_5XkvPyUwYAjXjm24mBYVSXrSg05mdxI5rc1MmTJp5DG1RL7fcrEsKFwHB22QZT2ZuOX9P2_ldEub5XHJBiZ41W2ZqBjpXG7BHlOgaAhpVOqmHNP-nDfTgKcxaGOEpDPx9-NL0pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bbef9d0be.mp4?token=oMySH0oGFS6yIA0WSF5rIFy0__StAerwyt6M0EdPzt6C8RPHEYWeAQrChLyK3p7abnl1x39vInlVRqzB2Knpg35OoD2KQ4BRTbCTl08DLlcHz_4f6ippkKRs31oF0r_5ShKqodc_MgZsa9p6wOIbCllkIQmSN06Yg1o2uwX3noHXYGk7vjy_rFG1cLZbDVUvp4-k5_wKKqkSln_5XkvPyUwYAjXjm24mBYVSXrSg05mdxI5rc1MmTJp5DG1RL7fcrEsKFwHB22QZT2ZuOX9P2_ldEub5XHJBiZ41W2ZqBjpXG7BHlOgaAhpVOqmHNP-nDfTgKcxaGOEpDPx9-NL0pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرواز زمینی چه کوفتیه
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/103382" target="_blank">📅 19:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103381">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی We pari همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/103381" target="_blank">📅 19:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103380">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nof88paJfYnP6PH2ANZZoGPVTQJ8m6ztgFL_sUMqQFUco3ni6V97Y3J7S2ZRfgMNj7kX9F0_zKMQf-XjzNU0vrQXpJA-YRyLJy49txZWPAcGgKOpSfH6gTj9PbCjdHCJ3PSAdrTJNPlcNLNGXsjvqFUkHipVk6tExIH2VenpYlAvGeyjZE54RCfDdgslPUqGVmSU2S304knIih_rKzjcqyCjCTkEjoAbtLcmFP4mBmVaP7CSL4nUmSRQPjxFQbP2ZV_tWO3oeiQm4r-hFZHWD_W-Kja7xYyEWjRyWRZxdet4AWZkk4iHON8NuiCz4k8HGTa2MntfeetO0RoTnEjYCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی
We pari
همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر
💖
واریز اول و هر شنبه 2 برابر شارژ میشین
💖
تسویه حساب سریع و بدون احراز
💖
دارای مجوز رسمی Anjuan و curacao
💖
فعالیت بدون تخلف در کشورهای مختلف دنیا
💖
بازگشت بخشی از باخت به صورت هفتگی
💖
اسپانسر سوپر  لیگ ترکیه
😃
😃
😃
😃
👑
کد هدیه ثبت نام:GG007
👑
ادرس سایت:
http://til.ac/z5jcpGT
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا،کشورهای اسیایی
👑
دانلود اپلیکیشن اندروید
➡️
🔥
کانال اطلاع رسانی ایران:
👇
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/103380" target="_blank">📅 19:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103378">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZlsmJnCU-bOlmhaD0lgXe_tnsnvUdSgGk8uhQrGHyKwqyhfeQv4jjXI4XNA56V1D5i8iF4RFMz0NsUIcSBShLij5CutFGo3BLYpRyMN8OTgC6LW2RT_m2fu9CcanrAPisSfX9Yc3IvqIU-fKH3sGVTSMx0sZuDvLGXGy_8PQu32Y4NOk7TE8lDRXFVC07buXJp7nSn4qV3pjYwvddHBBLmdm_MbVeTmdCDw2BneEAZ1MTPN5ia2gUxSy_-1p2Ya6dybSG4N8BFjW6DLLRAlddI8TqLaLRMhUCuDbKroOUoH_A4074c_RaLY36rcRyngt2i6DFMKfd6PXMBR2H6YfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میبینی رودیگر از امباپه و وینیسیوس دریبل نمیخوره ولی میزاره گولر بهش لایی بزنه.
⚽️
@Futball180TV
| بایرام حقگو</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/103378" target="_blank">📅 18:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103377">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad153bb5d9.mp4?token=AQEz76li2viwjEtbrnRv8S2EkxyolDbjOnoeMZ74fzI0jtjni1-_-qY-G2PJv0Fw_zrdYihjFwZBo0T3zps706sHGMtunjHJuVFzeLtn8Xn6DatN00r7v7G6XkMt8cKLmOTyuHMRdwcBxHOkwFyyceKpYivyaBkb2da5jIc0vk6lzeb4pxpuqcrmjQIk46IRUlw5YkgoJOcuHYKhvZpy1tTjnCATkTgQaAT9Vwdx7QQbiYBv1smOUaEmmb7Gi7tJxUY4hbJ9J1jHz-IcgQfa2Vq2n_qUPbPW4jtJMnudMxYg7BKL78QwYjy7SWkEUqyHduW2uyZ0ujj5lh6oXUFj1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad153bb5d9.mp4?token=AQEz76li2viwjEtbrnRv8S2EkxyolDbjOnoeMZ74fzI0jtjni1-_-qY-G2PJv0Fw_zrdYihjFwZBo0T3zps706sHGMtunjHJuVFzeLtn8Xn6DatN00r7v7G6XkMt8cKLmOTyuHMRdwcBxHOkwFyyceKpYivyaBkb2da5jIc0vk6lzeb4pxpuqcrmjQIk46IRUlw5YkgoJOcuHYKhvZpy1tTjnCATkTgQaAT9Vwdx7QQbiYBv1smOUaEmmb7Gi7tJxUY4hbJ9J1jHz-IcgQfa2Vq2n_qUPbPW4jtJMnudMxYg7BKL78QwYjy7SWkEUqyHduW2uyZ0ujj5lh6oXUFj1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
محتواهای فاخر صداوسیما درباره فوتبال:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/103377" target="_blank">📅 18:11 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103376">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f850200c.mp4?token=iRPvE3oYAMt6CufrrLJtCUEIZETc2fKHVdYUKu3jnZ8ISZYJO_-QVHnLAs4Fgmrshs51wuvaLQnNZKc7VliLU2N6MyLlccDpQOWayAyDuofNpxkAKT76WprpVw0YTkz5sj42UOq613ISJLZhwoIkeJdowN8maWs5vikeY6sIahy0Z15YMuxPtZO6JsSJxoVbQBBkIokzsMAFp8jZs2LvRCoznfftPXyN9Qcw8JZQhJL3CmXeT-T4fssNXCnU5EdTjauP_e3moMRevBDXHItPMzgnzYRLOU1_bGhgVWxoJR1FbxtOSwRIGA1_qasq4L8jLt0MqxgMqeuud9-TR0j_zk4RRRiSWng2cackHoUwPYLk3RPUBdUaGQFtOL6Ho6nDgOYSiDWF3kF4sBdf0jCsUw0YenzX5McgkMObSvPjvgLg5_GvhfngPX-wfApPXWdJAUV5MgGP5m62h48-1hSr0zqco8vreR_itwZuaSOktvW7VajnR6EuixXQROmu06-ftxhvDjQ6cSkz-j-fjZqvwvtoa9ulUrArhGEMdExrw3TUiK8ao2zgusxczcAQNCAXKlJrhnjN1AI13eyL8nvQTb-CbnIo04oGQVwlUBYmEot4HPPPW-M7McUFy_7iFeTyPGdEWcORSA1E26O1wScKFINHxGb8ULcMHBXSTLw3FYo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f850200c.mp4?token=iRPvE3oYAMt6CufrrLJtCUEIZETc2fKHVdYUKu3jnZ8ISZYJO_-QVHnLAs4Fgmrshs51wuvaLQnNZKc7VliLU2N6MyLlccDpQOWayAyDuofNpxkAKT76WprpVw0YTkz5sj42UOq613ISJLZhwoIkeJdowN8maWs5vikeY6sIahy0Z15YMuxPtZO6JsSJxoVbQBBkIokzsMAFp8jZs2LvRCoznfftPXyN9Qcw8JZQhJL3CmXeT-T4fssNXCnU5EdTjauP_e3moMRevBDXHItPMzgnzYRLOU1_bGhgVWxoJR1FbxtOSwRIGA1_qasq4L8jLt0MqxgMqeuud9-TR0j_zk4RRRiSWng2cackHoUwPYLk3RPUBdUaGQFtOL6Ho6nDgOYSiDWF3kF4sBdf0jCsUw0YenzX5McgkMObSvPjvgLg5_GvhfngPX-wfApPXWdJAUV5MgGP5m62h48-1hSr0zqco8vreR_itwZuaSOktvW7VajnR6EuixXQROmu06-ftxhvDjQ6cSkz-j-fjZqvwvtoa9ulUrArhGEMdExrw3TUiK8ao2zgusxczcAQNCAXKlJrhnjN1AI13eyL8nvQTb-CbnIo04oGQVwlUBYmEot4HPPPW-M7McUFy_7iFeTyPGdEWcORSA1E26O1wScKFINHxGb8ULcMHBXSTLw3FYo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
مرتضی فنونی‌زاده رازی رو افشا کرد که امیر قلعه‌نویی در جلسه‌ای که با علی پروین برگزار و در تمرین پرسپولیس شرکت کرده بود، فقط یک امضا تا سرخپوش شدن فاصله داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/103376" target="_blank">📅 17:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103373">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f83944eb6b.mp4?token=VE0V50tHDRZ2izDjOpIZRofk0m6UxByiyamRh_tRBvgaikO2jVei0J7bZYzTSt96ZotwZX86tH4W8qhwDKrK9gpdHLix1W-mytuhmG8lQ2-bH94XpEv-dyCEG2t61uTZbAnM8jC3h2Qk0hpVXEwi4ukxSod3BP6AbvwT_KIqeTgnq0FE1BY0KADS3VqmkCBYkDMH_zYlw7Midoi5GzXeXGRjjNqsbZrQt6ppbq7fMcJOECvLeJDcm8xkky2nl_MuORA1x5HHe711OdyGXBGf8DqpuHmJjr3HeSJOCOaX8LXYTpsfvkkczjHaLd7NcIqZ5y6_wlDz4L1VVd3N6b97mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f83944eb6b.mp4?token=VE0V50tHDRZ2izDjOpIZRofk0m6UxByiyamRh_tRBvgaikO2jVei0J7bZYzTSt96ZotwZX86tH4W8qhwDKrK9gpdHLix1W-mytuhmG8lQ2-bH94XpEv-dyCEG2t61uTZbAnM8jC3h2Qk0hpVXEwi4ukxSod3BP6AbvwT_KIqeTgnq0FE1BY0KADS3VqmkCBYkDMH_zYlw7Midoi5GzXeXGRjjNqsbZrQt6ppbq7fMcJOECvLeJDcm8xkky2nl_MuORA1x5HHe711OdyGXBGf8DqpuHmJjr3HeSJOCOaX8LXYTpsfvkkczjHaLd7NcIqZ5y6_wlDz4L1VVd3N6b97mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبر بسیار بباید پدر پیر فلک را
تا دگر‌ مادر گیتی چو تو فرزند بزاید...
نام و یاد استاد محمود فرشچیان گرامی‌باد
🖤
برشی از صحبت‌های استاد فرشچیان در دانشگاه هاروارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/103373" target="_blank">📅 17:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103372">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vty2T38L7dXYk3VKS_iCVYfbwEhfq2zwPCu3KA8foAivEBIFDpIGXGonajYf7JyzjX9USZEO0Y34B7MYsYBoS8dGiO0U2tUrsdTxQlA4c_B95VDYrMMrrxHlNnTItv6XjOhUfJDV86ipXvDhtqq-iMOopLBTdQMf6_BtmmMa8bN7KxWuUJt0VwM52kbSofq-K6ZicSji_VkfM76EfALJOjTprYhS5bc-Gc2oRUCRIxDU1wJD0HVcHwACwBfEwFjwRBhUaO5OCS6u97G3aSuSIuLc4bY6aSouqMVTLVIA35A5kXFd7L0wUv0VzPpEDLStiL30LB4L6nQZAYZxXvw77A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
❌
بیانیه رسمی باشگاه بارسلونا: رونی بارداگجی رباط پاره کرد و به زودی جراحی میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/103372" target="_blank">📅 17:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103371">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1XbJ-7xf8AraFoQ9ydL1enRrZ3DxGqP_8x7k03wPDYoIdzStB0S-CS5AWJewIuSPPDo0fN3PkQSoA1wfh0QaZ-1VkZcrDRxuJutaboX7lrSG7yBnz-lzF4TjQ_BT32EGaOOD90onzdZjmNFBxCM-3JRCFD-LMbRdKauU3TD1yqPINt8eAPlOq3hxg6-gXaoEJ7sYcEdcdz7QeI1GyNur_i5RDEG0pVlJnVfCf0FgJFjmh2IWNh_arrQkRSTtIEN2-ZxfMKOsTsdvcIpFtOhfzyVILE6fy2ARi76aDlpo5kkq5OiwH-feyxO3iFrCXWsGj7O7DNK3DrT_CV5R6iXPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
فنرباغچه همه استعدادای بگا رفته اروپا رو تو یه تیم جمع کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/103371" target="_blank">📅 17:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103370">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEQctEpae8Y6Bvc55xGxE7xKqfTQgWYK7eP6SJ4WMwfgDPsL7dwMDxcaJLd41qD4hZDADHAobzbbfFRn4EF7XVQ0MEQdkePhPY5TMW5U1yPNHLfzuvvDhmMU4chBtIkFtgZJHLXZjzGFkd2qWtY9A__dRQXtW1TrbdzMDcPG3ch_E_KJRPUuWS6KysuuKDkcAyiGinraiXcYQf6IwM9oLtETEOG-zODzgaVQv4PCddJQpsCNZ4OEhAEhwdd-6ztot169lnhiPlBBKtGt_l8ReNh1JLQGyKVfx0quJFKS99dzOwFWvJLaqrIgS_rlZR-Lcpuozf4QtnWlZOmhuxXEjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
لونین دروازه‌بان رئال مادرید بهمراه همسرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/103370" target="_blank">📅 17:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103369">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9fc92de2f.mp4?token=GjLfrzOjbdk49cmYqllVZrHLUV8BJ0C_6nzZISKMIz1F3YSXD-Broh0vqZjpsvIe-xDrG9U-E4PfY695wrR5aQ0enX7Pafm1H-I24AZEUI8h0toRXP2LLOhIV-QaMlIa0bg1sJS7HwbENF3jKTYGkvM33MBYwOQo0WspS_vbKdkdDTZWTJRI-0HHQYYk9t8svinVIOBPk2TjPwS9rrbcwPJ2s6Lcfx-ALO_4bFR5pl9CrqNwVfpvNQ2uXjeDXPgS6F1-ntaNZfYd5850HLyQxkWhVDEmtdxiM82d0djYT6phlQ-TJI98AF0LhbaEDkGq7WZUahNKGyyc7LuFDhZc7YNlzKKx1MDmiVD_nnpZAKnVGjdeM6T67NbgF6HB52-INwlOt29MaPxUkcB8efHJsKU7gKRDc8m_k-KeeBwHjLhljVb6rrFZvMtAkxLwZodaR7Y6MEbnjBgnzFTU9xegIsi06n8Zou5IRw-WCIMjRJKKI9_bxyBZhWWAAGEg_hdXlI6_JUY9FLVIS2DFOzXXKVLp0W6enKMeGFTjRNkAkaF3Kk_was0m9JxmZS6kWgXH6RupX2XI6_iPn---6GfBJPaOEZKJ9yYWLKTgmSOtC3zzptDfrq1_vqk6CYnN4fj8aORecVagHDbo5zy5YUL3uWX78CDqgKxzKFa0ccxOlTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9fc92de2f.mp4?token=GjLfrzOjbdk49cmYqllVZrHLUV8BJ0C_6nzZISKMIz1F3YSXD-Broh0vqZjpsvIe-xDrG9U-E4PfY695wrR5aQ0enX7Pafm1H-I24AZEUI8h0toRXP2LLOhIV-QaMlIa0bg1sJS7HwbENF3jKTYGkvM33MBYwOQo0WspS_vbKdkdDTZWTJRI-0HHQYYk9t8svinVIOBPk2TjPwS9rrbcwPJ2s6Lcfx-ALO_4bFR5pl9CrqNwVfpvNQ2uXjeDXPgS6F1-ntaNZfYd5850HLyQxkWhVDEmtdxiM82d0djYT6phlQ-TJI98AF0LhbaEDkGq7WZUahNKGyyc7LuFDhZc7YNlzKKx1MDmiVD_nnpZAKnVGjdeM6T67NbgF6HB52-INwlOt29MaPxUkcB8efHJsKU7gKRDc8m_k-KeeBwHjLhljVb6rrFZvMtAkxLwZodaR7Y6MEbnjBgnzFTU9xegIsi06n8Zou5IRw-WCIMjRJKKI9_bxyBZhWWAAGEg_hdXlI6_JUY9FLVIS2DFOzXXKVLp0W6enKMeGFTjRNkAkaF3Kk_was0m9JxmZS6kWgXH6RupX2XI6_iPn---6GfBJPaOEZKJ9yYWLKTgmSOtC3zzptDfrq1_vqk6CYnN4fj8aORecVagHDbo5zy5YUL3uWX78CDqgKxzKFa0ccxOlTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
▶️
لوئیس سوارز ورژن ترسناک و جوان آژاکس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/103369" target="_blank">📅 16:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103368">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwL8cPTm-U6AQ24hwp5tEmoafVbGuMolw0uIhaK5s-Mn8_jhcLln5yB-mCt0wwdsx51nWEM9XEI-6NUaqTOkoycHZVpaC62C6u2JrcnkuAdC8aEPwkj-FsBxMzhzOX2CbQt13T6zhvBWY36AK7EnO6PHf04HvOflsEOxRgTwcdQ82Y7naZNIEpxnWFmUy3xHHetyWq2ID6aWM0OWCyf0e5sfcelVVPEtsXrQ5Nvp78g_L5akU_sQGncPqCPzkOUbbqstPQqaXI0P0PDdBhUlQPYfp4l3E7kfYfrXLYDyLTVK89nzo76yg1pFYofsrdXn3mBTLi5lg0ovYJbUlfi7dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❤️
رومانو؛ باشگاه بشیکتاش، پیشنهاد نهایی خود را به دوشان ولاهوویچ ارسال کرده است تا در ساعات آینده به توافق برسند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/103368" target="_blank">📅 16:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103367">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b011d4118.mp4?token=v3BKGwy-WVKMhml_eZEIf3w8ighsqyYnNt93iL3HFz7ySxddPWaDVUD-y-Tvmnq_RcszYpiUadTgle2muJzQdvgmp1V_JomnZP7eOylO3IfPqj9Hf2wSUCp53dorTKy0UrWaihoIssOiLQAZIY3EWxU831OKH3gjB3EwbiBVfoqmofpZz6uHq3U_z2Nay3r0tZrMIXdN5iQe4kH4HaqcN3vdlqoLc1R7zRA3t0DSMB1RnSl2EGAkYwLg-YNQ9Wy3G8hcpZBxtYRkjRX9Z1m1R3co88htj1ReAfb69xt8Cmg7ySW9LAf62Idqg5h4bbYe2DQjMoUifM6_XIPKsqAk2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b011d4118.mp4?token=v3BKGwy-WVKMhml_eZEIf3w8ighsqyYnNt93iL3HFz7ySxddPWaDVUD-y-Tvmnq_RcszYpiUadTgle2muJzQdvgmp1V_JomnZP7eOylO3IfPqj9Hf2wSUCp53dorTKy0UrWaihoIssOiLQAZIY3EWxU831OKH3gjB3EwbiBVfoqmofpZz6uHq3U_z2Nay3r0tZrMIXdN5iQe4kH4HaqcN3vdlqoLc1R7zRA3t0DSMB1RnSl2EGAkYwLg-YNQ9Wy3G8hcpZBxtYRkjRX9Z1m1R3co88htj1ReAfb69xt8Cmg7ySW9LAf62Idqg5h4bbYe2DQjMoUifM6_XIPKsqAk2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
پشمام؛ روایت یه وکیل از جنجالی ترین پرونده خیانتی که داشته: زنی که از انگلیس پا میشه میاد ایران برای خیانت به شوهرش....
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/103367" target="_blank">📅 16:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103366">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2LcNhIVGXBef-14KsC_3VCpoqW0cM5H_QEb0aG8CdgYL9bYat_lZulaI6qh3EplIKhZ3y6sDg6zUrsoR1DxxZweYTe6AJFpfKrusC69NW2Rfwl40oCw5yby0vsFN3Wq_CmlBPUKqGywhs9EYO0mAtT1dAKGWioFWcTYzyDYKaN98D19yYHevyX8LbyEnN8dz2FOFlI9RLc1vG-rr-ZHArwTPhfOo2BPfiOPwulk7PDXu_JmcTYlVt_Y0gCIpMkzAAjgK40U7WrHriBlduzmj1ndSzNAXDO7pLe--O1QvGfxok1aRf7OBwzHX_IR8Qj8DtYdkRzF7Y-n5lsnhIZZ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔴
آلوارز در تمرینات اتلتیکو مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/103366" target="_blank">📅 16:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103365">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nauZDDcdpcSQ4kJXH__mB6hSfOfGqq6ebESpJ6yLuBl2lmiAMiqwXzgTcp_rQSeA_s9Ezp0StvE6cDH7Cf3AtE7bE1CrWSoMPOsDs2O9w4IRft4-SKJdJ7QHtYKWllU3Cnb5bHFSm-5_QBPfkc8qlomEzZwhBJ0aRbcCSZJgHsF-M7tvLHiQFdMsbmCoKWA0QnRupWbDp4YyhoMDVtDdDRd76pwfDlGwwYjYPEJtg3ozLu_iAdGqVjF2bCyvIu-CmoxivytSjjyx1uhRcVGkFxJBjMTEKD8NDuqlFn1ShNdhU89s00aRE099MLqMhsRpnfGR-pXPBlVFb5fDXSy9mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇪🇸
لیست نفرات رئال‌مادرید برای دیدار فردا مقابل دپورتیوو لاکرونیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/103365" target="_blank">📅 16:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103364">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2091ae4f3.mp4?token=EEL9DvYydwKqoXmT7dSsZ_DnDUf27Nki0IISROwGPURuZsRojJTiWA3T2kVNBpC7PaLgh6kWD-vkpQPJYW4taPfqy_FLB9_-7tBVJUg12WlGR7bVit4K6HhM7gVALUJCNywGB0Xk15fqjNYDVqdHlx0QCsccKNEsVWEoQA4834wTSVRjIXgP76AVvkgspWH18eSoFveOMKhTgINEs72gST_2SploRl2mKa8r-rNGezEqKb75UDt-46eTSQRe7RZe3Yx5c9V9HaB1OiAbhW8Nt093okRf89byXm9wuOLTcUgyl3B2qwm_648LTCL1JIKL27urIV2BPHrQ6wW7Zk0LwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2091ae4f3.mp4?token=EEL9DvYydwKqoXmT7dSsZ_DnDUf27Nki0IISROwGPURuZsRojJTiWA3T2kVNBpC7PaLgh6kWD-vkpQPJYW4taPfqy_FLB9_-7tBVJUg12WlGR7bVit4K6HhM7gVALUJCNywGB0Xk15fqjNYDVqdHlx0QCsccKNEsVWEoQA4834wTSVRjIXgP76AVvkgspWH18eSoFveOMKhTgINEs72gST_2SploRl2mKa8r-rNGezEqKb75UDt-46eTSQRe7RZe3Yx5c9V9HaB1OiAbhW8Nt093okRf89byXm9wuOLTcUgyl3B2qwm_648LTCL1JIKL27urIV2BPHrQ6wW7Zk0LwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
رفاقت ورزشکاران
💞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/103364" target="_blank">📅 16:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103363">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5hcAB3qgARkTNtxx5rwSHiH3vS5UOIuCRkibs3t5xtswknJ01JNpuH19-xAPZmuRFSjBgiAfnInWlpcGSks3lKSIiiicnkl_6bFu1tZTj8r2O55dqrsFzsVLDPW3tlsCZ7peoTzAb4JOcZ4mg_92Le0Oolx1Y4iw8jkjhWTPxOL49fb3TuMNuUiCkPhpahTvEf5gg9jHTW0Ae3tmbbJINfbQ07S8VwCy38uDqYVQr4hw-qAn7Kk_qN-BOp9qw-jzErkbWErt40WVxGXhICciInMhcjKIskAd0S17UauL1C7-Dn6hmyk0xW_M5U_Z-iXIKWnlhnKTX2sRPcXd0BkfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دخترا: پسرا وفادار نیستن.
پسرا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/103363" target="_blank">📅 15:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103362">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vGgPapilgNiU1TfurXXoHQnaQjlHWow9tONnOJYBVvcm6PkeHnAaFeLZcRjGpg7DlP_i9IXSNTnfxFAw4F32wl-cC7pEUY4r6t_3Z14YiXpAQQlc41B5t11BTLmYAFVc9uSNP-OeuiIBvRjSAjHnoJRWqoYZYZtP8qjaTXiBWQYOcHwb02STT05dKzRqY3XfwVV7Yc2WtfLQZ0QVipZyOMxoFZMlcbEWPx46HaTWsXTuX-x97L0atbs8tfT1l7URlSrSG4wM7-8yEpMuUZpW0F8Sh3Nz5bOgcCbyZzQf04kmBbvqssSeRUeO6lknX_kT0MgjASG911g0OPEOtdkkCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
✅
فابريزيو رومانو:
اینتری‌ها میخوان هر جور شده اسپنس رو به میلان ییارن. اون میخوان این انتقال رو با کمتر از 40 میلیون یورو نهایی کنن و مذاکرات بین دو باشگاه به زودی از سر گرفته خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/103362" target="_blank">📅 15:18 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103361">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bea6d735e.mp4?token=Z2XNynr4eIGYfLwgzxOLAAC2eYdFIFi7BF6Ew9vmCmalIbOhZ_tvIebd53ELdksQuvafpcZmsSFiK9sooe_OA6XYmEPP_ux3ngmbVTKixno1OxeH5Vh_OedYnDayjJBIb_-rmGhn9KdXdbdQ0JN9WoqWggWoefdSfYmuD-Lw_3_-2dJz-qbJDqX658-r-2Nu6teUNl4O2vaopE_W0tb-K7yZxtFc5Plaha44yItQ60Gufnwe5Unuo2rd9RZoyctPVy7TeBgvYhTTEpJcHTPDGJaL-ED8hcoxBhdAHPR7sZZuNI0hBGGenXlx6MptA3863sruR7AHj7eqFeGHFOJl-DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bea6d735e.mp4?token=Z2XNynr4eIGYfLwgzxOLAAC2eYdFIFi7BF6Ew9vmCmalIbOhZ_tvIebd53ELdksQuvafpcZmsSFiK9sooe_OA6XYmEPP_ux3ngmbVTKixno1OxeH5Vh_OedYnDayjJBIb_-rmGhn9KdXdbdQ0JN9WoqWggWoefdSfYmuD-Lw_3_-2dJz-qbJDqX658-r-2Nu6teUNl4O2vaopE_W0tb-K7yZxtFc5Plaha44yItQ60Gufnwe5Unuo2rd9RZoyctPVy7TeBgvYhTTEpJcHTPDGJaL-ED8hcoxBhdAHPR7sZZuNI0hBGGenXlx6MptA3863sruR7AHj7eqFeGHFOJl-DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادل و دستای پشت پرده فوتبال
😂
خنده بازار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/103361" target="_blank">📅 15:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103360">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TaJUU5Yq3K6mqFlTzJBXJNnu58WTUTcUPjIiFlqavi70hrbz1qnsV4CXvObRWLnhrN1GInMb8TAsaKzl9GEDef3TjYdjOWNGp9pcNpDGT9gTIShBnXCVHWFVOOgI4wROq-4e7FB6Id7OluneQ3JpLynOvdpu1GWidotGbQNZWPruP_-m5EWLXjn9Sh3eVsihAe4EM4tX5UJdKaE57B-m8YdF2jjDabuFnp8NDA5K6Mn77kX9UxA-aT32JrB-3nG8_Rby1Q5IEwO_i5GPOOjsZ0QgjZ4sFpVXgUyq0CyO5vxW6PccJORG4VTFEd5_VpGSzeWUGbJ3O-Cv26GW8SkrpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
🔵
فابریزیو رومانو: فلیپس با قراردادی قرضی از منچستر سیتی به شفیلد یونایتد پیوست.
𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/103360" target="_blank">📅 15:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103359">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-06gVrepOf0dKrzcmtPNz5q5jVec-7X2vufCGNLp94ffzlhOwpA8MwafVwdxd3eekrnYOrUfs-xLyrHUPv7s1sGv0ay1HJPuabMZzOY7zKL6fJLXAwg1ZXUx_45KlC4mfUbrS4RepbSZR6INolV23KcVDHsXpjKx3g8DnvQ5T-QZDcWA2nkrruzpadRjboJlPjLJN13xV_jRQje7loG0euqInIhKRrFaVlwOZAJR1zFJP22oHqAIZmmLrCuZws7wiI8uTmG0dgCnd4E_XmFVsc1wSZNM9KeKeQTJEwiaIadznhp2QUzx6417L_nivEjY1yZ0mqZqFU05UFCdfH3ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
🔹
خط دفاعی یوونتوس در فصل 2016/17 لیگ قهرمانان اروپا فقط 2 گل خورده بود تا اینکه در فینال به رئال مادرید رسید..
⚪️
اونا تو فینال 4 گل خوردن و جام رو تقدیم رونالدو کردن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/103359" target="_blank">📅 15:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103358">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1146b9d2c3.mp4?token=Kx8f5Qaz6XX5mYXmkX0gOwliZeJ8EH1bfyiBJMVjydOH7y9j1LF0lQZ9Rdaf0GiE4DD-9KBa9EZPWeLd1I-9APTPfsjWPwZlKlE_A_wgnOaKdV1fj-euxoJ9AsHDxT6bfKsdT_fbGyxOypexM7oD0BdHmIHGkrMQuFSRUnN64XbVZu7ENiCUyQVWv9rCumZE4qu3G1xxef1G6rDt-ELY19bYdG1iNR9vidX23_46yRra2NraQ8t9cuiz1E-_hQ87JS0GsT4eqloexITHEwGpGBps7LvpdnPmFcH_gxiPLfe-CSWXavGzMmVwIGu3LPtvguGz7fnIuWn8-ONFt1ed2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1146b9d2c3.mp4?token=Kx8f5Qaz6XX5mYXmkX0gOwliZeJ8EH1bfyiBJMVjydOH7y9j1LF0lQZ9Rdaf0GiE4DD-9KBa9EZPWeLd1I-9APTPfsjWPwZlKlE_A_wgnOaKdV1fj-euxoJ9AsHDxT6bfKsdT_fbGyxOypexM7oD0BdHmIHGkrMQuFSRUnN64XbVZu7ENiCUyQVWv9rCumZE4qu3G1xxef1G6rDt-ELY19bYdG1iNR9vidX23_46yRra2NraQ8t9cuiz1E-_hQ87JS0GsT4eqloexITHEwGpGBps7LvpdnPmFcH_gxiPLfe-CSWXavGzMmVwIGu3LPtvguGz7fnIuWn8-ONFt1ed2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
تعریف و تمجید ستاره‌های سابق از لئو مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/103358" target="_blank">📅 14:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103357">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4lJWmrNiJLqm8iZa299gfkGd3OeTqWGonZzAjO0WVjqXA9W4HaQep2TJJqOWOoYSiM0_lAnqPdhAFkZ7Lx-x44a3WuH_ryQL-dzR6CIj8Z9cyCDrL7wALMp3DGEc8GS-8W9K-ibWyQ2Htobfb3RGf4bCmrg3bvwO95QOyrLO-tHKiKcZzOt06-1EnFk4UCfaEeO1bF5DEMevOL_Ar09jxgYRcea4_WYhjvXrTyAQusi_pwIPD7yVZkc2nPNIuSJra7GEymM4KpWu28q-9jz17FC6fiTMfm85l0bpBMfFa3a0kn8FiEUi6W2xrfljeJ_qpiVxGJ3lhFqCmQVnueRBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
#فوووووری از رومانو: دیگه مثل سابق قصد حضور فعال در اخبار نقل‌وانتقالات رو ندارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/103357" target="_blank">📅 14:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103356">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/befb00f0c7.mp4?token=SYntFSyr_bows__st-cKR2XnMlJ2WLnSwkK7xx5aepkVtFGqGKR87pww6OjNP4w5rTc1AoiQwn1kbCP210YaanRHPoneHs5PZmBUDG93z3ugwikqhhYBqCt5fHM4e2I7YMTo6inRliqyG-J-YzfQaSfxeL0YYCjGVl3O2IBiS8P_6TCyjhFq4JilYFJEvuN6GMBH2H-NLFzxjRUhYz0pBdwJN_sBrWeW1L6r6I9Zf4edigEeNHoFYw68-5aClbLdHm1oBzpCvOPHnyU07GN6yeTL7rPkGOG_IBM58K_zs0uyRUH3d0dMi9wLrsaNnay6c89FEeT3ErngW3MOZiO9YQW9KFAbC1yXmaYWDnSXaJkD6miTzoqruz09sINQmNXcTUF3TaDnDAMd7rWyh0LcnMhDR35I0Ykjhm-tRGyeoCNHrnI4hCSHPpOt9-W8XLbUUDPLLQBWrJyAbqqm1oQHbX4oFebVLUSx3b92sZjbcfDb5STUuIbQngXX7PNluuDs7HvwtOS1hUNZnB7WPlHDNbsvDxqblfj7GP2ysn0M2z3G8o7tcmeb3BZZaZHIwFuLsVfPkqAN3UiTqOzxSt2QvLUoP1X-L1BQdFzhVUmuTkKtkhg5WPApFaqD1k9DNVC2xyzcaDo6Jf_AA2nlDX7zvK3WS0fhQqI83eqGtoUZ3DU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/befb00f0c7.mp4?token=SYntFSyr_bows__st-cKR2XnMlJ2WLnSwkK7xx5aepkVtFGqGKR87pww6OjNP4w5rTc1AoiQwn1kbCP210YaanRHPoneHs5PZmBUDG93z3ugwikqhhYBqCt5fHM4e2I7YMTo6inRliqyG-J-YzfQaSfxeL0YYCjGVl3O2IBiS8P_6TCyjhFq4JilYFJEvuN6GMBH2H-NLFzxjRUhYz0pBdwJN_sBrWeW1L6r6I9Zf4edigEeNHoFYw68-5aClbLdHm1oBzpCvOPHnyU07GN6yeTL7rPkGOG_IBM58K_zs0uyRUH3d0dMi9wLrsaNnay6c89FEeT3ErngW3MOZiO9YQW9KFAbC1yXmaYWDnSXaJkD6miTzoqruz09sINQmNXcTUF3TaDnDAMd7rWyh0LcnMhDR35I0Ykjhm-tRGyeoCNHrnI4hCSHPpOt9-W8XLbUUDPLLQBWrJyAbqqm1oQHbX4oFebVLUSx3b92sZjbcfDb5STUuIbQngXX7PNluuDs7HvwtOS1hUNZnB7WPlHDNbsvDxqblfj7GP2ysn0M2z3G8o7tcmeb3BZZaZHIwFuLsVfPkqAN3UiTqOzxSt2QvLUoP1X-L1BQdFzhVUmuTkKtkhg5WPApFaqD1k9DNVC2xyzcaDo6Jf_AA2nlDX7zvK3WS0fhQqI83eqGtoUZ3DU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇪🇸
لحظه‌شماری بارسایی‌ها برای جذب رودری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/103356" target="_blank">📅 14:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103355">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wvv7BFJCBHbuKbbyUZWb35OMcPGpcbAL7sJ0jxWZ9_lFpVrDCgH1MXQx7hEhokEnm8hMuTGO1KuF8yTFvIWLqes9N1tk-IIZeVx0TmfUzycSm7IbOPNrcFAr416pZGCQCwCxqRLCM61fqbBbwJkJ8u3To-kEU36fST8TFluPliOWOgp6JSOFEhONmdEF8Vhv5dZeyK7R_Ui6jmesQwDTlBSrxlFd4pM73box-tyXOOKY1ksEd4pZh6yGEBN1fzu1v0JBKFTE-kphBIa8q1WG6RmpXc7Ma8wRYpi-vNFQqKGKzoxhsqLBCpXaVSmBDiYSYLwZKLhxotsKyfIUoiSDNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔺
🔻
دو تیم ایتالیایی که برای آخرین بار قهرمان لیگ قهرمانان اروپا شده‌اند:
🔴
2007: میلان
🔵
2010: اینتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/103355" target="_blank">📅 14:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103353">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
#فوووووری
از رومانو: دیگه مثل سابق قصد حضور فعال در اخبار نقل‌وانتقالات رو ندارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/103353" target="_blank">📅 13:58 · 20 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
