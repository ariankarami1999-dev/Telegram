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
<img src="https://cdn5.telesco.pe/file/Fd4sep041-ilQNu3R6IIKNWK40mdLlzA8aN0zC60LGxl3lgi8uJIfh5qDA8HpLoiWCjtbijxMsXJLbUZ89p_kP1yeMkKv4p5nxmSJJLyx0USWAyFIHdbnhVH-Es1Wf4CKCb7LHy2j89fOrrpvUtLI2qf2ypzdNgHfQe0CSwhzay6FGXGz2lovEnbhkeXLYP9z1VCROc7dPLmRPB9HlWo-ak1dfipvW-QY5KK6Fd6hndKQmkxKep_KlEmwnuK8a03ohqY-0LZyEPXxr560xX3o5feJo1trd0x-_Ip0CGo0kyB4Jx0kmhw0pU71sga17_ebxUqwysDbBWC6MJ9-Nl5eQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 476K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-20 18:20:19</div>
<hr>

<div class="tg-post" id="msg-103378">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPwUQSEWjvOaj_crCjVi9IeKQ7p6tUCGe1tV9fAW_Q5X8jj2aojlSw79mLPveJqbUyCOcNJo2du0sPEOV0mGaAU15DBpalSG0frLz21OtXrjLmu1JZvnuce6_D29iq4ZROeoc1TZB8qWCHJcD6W1d3_-gt0ZjInk_ECbaB3Ln34kgOzPR-TSb_6lCanmTLIT47CC84SoAkzF8Cy_OgkltP4kyNtcNoJYN6qG-Xx2fVyPOxTYI2jvA-Uxm07xRg4O9t1bMjuCCwchPwA5uTEoP4It4J6Ej2227CRPy2uHSmObDkN_5wm4sIaGVTNQdsWK4dg3rfRiOhjMhGoSw6uy7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میبینی رودیگر از امباپه و وینیسیوس دریبل نمیخوره ولی میزاره گولر بهش لایی بزنه.
⚽️
@Futball180TV
| بایرام حقگو</div>
<div class="tg-footer">👁️ 8 · <a href="https://t.me/Futball180TV/103378" target="_blank">📅 18:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103377">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad153bb5d9.mp4?token=hHveOCTuoCKLJR-E5Aa5faf3xagTQqYJXkFoijZ1OiCVKR4MrAFlpEgkv93ujN4ruKVrZ5JMKepAYIOU3m-73xm0H8f-NEGmts0LlZ9idv6a870Bjyx5HBA8-WHQtX_aodzTtoJDFE-KnDMgza7aBmp9bd8yugZNUHewlq3yXEWvI7sEq1JxMNz3CWKLv4zjLGMhyS-uEzCnUQNwoa1lRSGjs_vNdjSCwzxdPDfYYoGrtRwvEQpD9O6EaJIQPjztyhTuH7QOaiYbmcQ4csYlV4T56xHInKqUoZEBg0M9xvt4d6rotzwhqxYZHGpyVlkolyphgy5zwDfSi2PEyQmCNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad153bb5d9.mp4?token=hHveOCTuoCKLJR-E5Aa5faf3xagTQqYJXkFoijZ1OiCVKR4MrAFlpEgkv93ujN4ruKVrZ5JMKepAYIOU3m-73xm0H8f-NEGmts0LlZ9idv6a870Bjyx5HBA8-WHQtX_aodzTtoJDFE-KnDMgza7aBmp9bd8yugZNUHewlq3yXEWvI7sEq1JxMNz3CWKLv4zjLGMhyS-uEzCnUQNwoa1lRSGjs_vNdjSCwzxdPDfYYoGrtRwvEQpD9O6EaJIQPjztyhTuH7QOaiYbmcQ4csYlV4T56xHInKqUoZEBg0M9xvt4d6rotzwhqxYZHGpyVlkolyphgy5zwDfSi2PEyQmCNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
محتواهای فاخر صداوسیما درباره فوتبال:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/Futball180TV/103377" target="_blank">📅 18:11 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103376">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f850200c.mp4?token=Wwu9RCGBO_OSXSnU_cQSb7B82k7kZDRoUKB3vuDhGWmrHmgY6XYfeKWISqubcWih_76vobycykKGE_8xuaZnGkCkMQXSd_2HZ5NVhCbpIhTQqagYg1exUPYwa7_WFsWH7otcqW9nfEkHQ5adScp10WIww61Z3osH5knrUCbIoJkgAqws-kYAmbq6w8ejuzYoOZulHeFxaUa8mUp0ywUVB2lvGBayd_thWPuO5SHY4wF0GYyW-W4nvMXCWn1_0sWIthdXhscjygddKCTYQZRaU_JkyIn55lIqYgBfxcDpR36EFAvBDYWtNa6BCWMMobiR7tLnugMNb_yY5M1_MZii92VgJV6MeW_O9NWalymHZzCbsoAAWxU-IaT8m3em0-HDmpvaVQwx1INu__4wSWfGx50lDh1OLJmCGen2InrMNQz2-ffyxJktwj84a3MijOwHdrdv0rIPdcuu4-VBo_LDTmy2r1XUYLx7UuF6ZFybIWLuAu_qq5LPOCkk2TQpNSdqtc-3A3jtak_4Z5SvSBbpLsi4DXzYjGsFVID01OKzGyAonXl71SUvv9HIjZg7Bx7jAyK3PQjBZp1yyt1KRiaKP6ez6rqlwNhqmRokUaIRgLkIIKH2elAn5veLP9JY17bGjDr0IfaYm_yiq_FNo70MseDRTWWg7_PZgYh1kbcq5M0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f850200c.mp4?token=Wwu9RCGBO_OSXSnU_cQSb7B82k7kZDRoUKB3vuDhGWmrHmgY6XYfeKWISqubcWih_76vobycykKGE_8xuaZnGkCkMQXSd_2HZ5NVhCbpIhTQqagYg1exUPYwa7_WFsWH7otcqW9nfEkHQ5adScp10WIww61Z3osH5knrUCbIoJkgAqws-kYAmbq6w8ejuzYoOZulHeFxaUa8mUp0ywUVB2lvGBayd_thWPuO5SHY4wF0GYyW-W4nvMXCWn1_0sWIthdXhscjygddKCTYQZRaU_JkyIn55lIqYgBfxcDpR36EFAvBDYWtNa6BCWMMobiR7tLnugMNb_yY5M1_MZii92VgJV6MeW_O9NWalymHZzCbsoAAWxU-IaT8m3em0-HDmpvaVQwx1INu__4wSWfGx50lDh1OLJmCGen2InrMNQz2-ffyxJktwj84a3MijOwHdrdv0rIPdcuu4-VBo_LDTmy2r1XUYLx7UuF6ZFybIWLuAu_qq5LPOCkk2TQpNSdqtc-3A3jtak_4Z5SvSBbpLsi4DXzYjGsFVID01OKzGyAonXl71SUvv9HIjZg7Bx7jAyK3PQjBZp1yyt1KRiaKP6ez6rqlwNhqmRokUaIRgLkIIKH2elAn5veLP9JY17bGjDr0IfaYm_yiq_FNo70MseDRTWWg7_PZgYh1kbcq5M0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
مرتضی فنونی‌زاده رازی رو افشا کرد که امیر قلعه‌نویی در جلسه‌ای که با علی پروین برگزار و در تمرین پرسپولیس شرکت کرده بود، فقط یک امضا تا سرخپوش شدن فاصله داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/Futball180TV/103376" target="_blank">📅 17:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103375">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">با ۱۱۳ میلیون شروع کردیم ‌و موجودی الانمون یک میلیارد و نود میلیون شده
✔️
پول در آوردن کار هر کسی نیست آنالیزور شماره ۱ ایران
🔥</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/Futball180TV/103375" target="_blank">📅 17:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103374">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38501d45fd.mp4?token=XigcRJVGSLXUDxtOIF3vz0qXNvUIfApU7qTEeLyjiNEyT9JcTnI9Hh9NtgGKqXL2bK287jvVo2OULo9EihQ9mvmP_tDG9Yf76EQv0XKNXBVEMq-HaqXFGJp-seS0zM8ch2xEtdJ5-beSbDBbNJCnI306xcsS75j-TURm4QgHMtuTCLi68mWziCOgquwkcLarLCaM2jor7vDuw6kq7rPnPrPV_rgyKmfLcocnpS8kOZjHo2M6oD7q-P17n6l7j6BfGoB66srgyKcckUXUiYjO-uQCnSUnQpr2HkQ0KNMe71wxqW1RO9Lg838rVjhC7F2mEiLNAqUogqfkqJTO81OhAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38501d45fd.mp4?token=XigcRJVGSLXUDxtOIF3vz0qXNvUIfApU7qTEeLyjiNEyT9JcTnI9Hh9NtgGKqXL2bK287jvVo2OULo9EihQ9mvmP_tDG9Yf76EQv0XKNXBVEMq-HaqXFGJp-seS0zM8ch2xEtdJ5-beSbDBbNJCnI306xcsS75j-TURm4QgHMtuTCLi68mWziCOgquwkcLarLCaM2jor7vDuw6kq7rPnPrPV_rgyKmfLcocnpS8kOZjHo2M6oD7q-P17n6l7j6BfGoB66srgyKcckUXUiYjO-uQCnSUnQpr2HkQ0KNMe71wxqW1RO9Lg838rVjhC7F2mEiLNAqUogqfkqJTO81OhAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📌
این آمار  شرطبندی یک روز آنالیزور کانال تراست بت هستش
✔️
💦
پول در آوردن با استراتژی درست میاد نه ادعا کردن .
https://t.me/+RhwG-FuAQRI4YWFk
🔸
🔸
🔸
🔸
🔸
🔸
🔸
https://t.me/+RhwG-FuAQRI4YWFk
z20
⚠️
لینک یک ساعت باز میمونه و ظرفیت فقط ۴۵ ممبر</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/Futball180TV/103374" target="_blank">📅 17:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103373">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f83944eb6b.mp4?token=nnC2HKQ65I5Bxb4-NvlhXBRe7wzHbuiARMXFJJ2ptXx_EGGcYpVlEwJFeFJJTyZ0ZW2vUB9zkxckEyPcDlvScBbAgm9AErsW4h8i3O7inwX-Lfqdgs-X4P_MZvjbORtcLYURmBg62XlIxQBM8VKHndmVMtSepl-M-gZHrN1UoZitFOpAst2iqxQgXqOQ7Rw1EK99xkb5Fb8kh_ro7IlafiQ4eK252t0LhkCWr8xyyscYp7jJ9hOdf1Y6PhLJqzCFgD4DAY9U3_5N4V3vZgzlowXFdVEYkxQgEPsCI-xBU1mddDyi99BIgqWDZh7TpAFoq14qw-HiMXrWkeNRDhvnsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f83944eb6b.mp4?token=nnC2HKQ65I5Bxb4-NvlhXBRe7wzHbuiARMXFJJ2ptXx_EGGcYpVlEwJFeFJJTyZ0ZW2vUB9zkxckEyPcDlvScBbAgm9AErsW4h8i3O7inwX-Lfqdgs-X4P_MZvjbORtcLYURmBg62XlIxQBM8VKHndmVMtSepl-M-gZHrN1UoZitFOpAst2iqxQgXqOQ7Rw1EK99xkb5Fb8kh_ro7IlafiQ4eK252t0LhkCWr8xyyscYp7jJ9hOdf1Y6PhLJqzCFgD4DAY9U3_5N4V3vZgzlowXFdVEYkxQgEPsCI-xBU1mddDyi99BIgqWDZh7TpAFoq14qw-HiMXrWkeNRDhvnsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبر بسیار بباید پدر پیر فلک را
تا دگر‌ مادر گیتی چو تو فرزند بزاید...
نام و یاد استاد محمود فرشچیان گرامی‌باد
🖤
برشی از صحبت‌های استاد فرشچیان در دانشگاه هاروارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/Futball180TV/103373" target="_blank">📅 17:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103372">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUW_yyBVq_D-QMLA3gWw0wsHoQO3VdvRHQC3DHVNK15LVt11FHuQxQ8Qjm13_iE7Pf2vF2C0-qnY2YNaQVmVUg5dbBhOCx5LVQpXgkx_UB17Bg-N-TCsl_S_yr2j4QVoM2PC16rcZmxkaBIID58Mun6rjbOkAF5SdNEZoiM0LgDlC6jzcB-sWoGOMR2bNCSr290vab6wz4W-pgu_1YEm5xaQriHFJH_TQbDfbfQBZoEEfD3tsP2pAxjbge2DVtTqRvRlwONOENQL9m6tIKGuCByp-R-ZEERltdMmp52Nc-W7jHaeij1j9v1ipj603BGz1R_XslYlFN8X5aD7zdZQ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
❌
بیانیه رسمی باشگاه بارسلونا: رونی بارداگجی رباط پاره کرد و به زودی جراحی میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/Futball180TV/103372" target="_blank">📅 17:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103371">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-eCj6SIqb2uhAET3xAWDiz9oQl3KnYd5Ie2-5YnqkF1YKGOP10g0oGeVT6IKSRyfMLieq_eDkYLsXN6l9j56uIaDEVScyQrD-Sn8OrIDkXC7P94xDXZT_ZsSik7TDlZEmT28GAmePSGNCtdt-wes843CGjzngaDF9QxOIG2k-MVG-EQzuENIq0mXgqSzy6P3yKC5nvuUXfq2diH7IX2hcpusQLjk2gYi_70S9C0uB9Gh3bQujFzyeO1YuKnm03rybUpmiRruNE4QHaPN0SRDrwyWkdiTuYwpn3OVGemP28v_X3uNNDn0HN11UxcAfwXb8nSE60zJllTBqtN4_yYxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
فنرباغچه همه استعدادای بگا رفته اروپا رو تو یه تیم جمع کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/Futball180TV/103371" target="_blank">📅 17:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103370">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N56nUWWQMdCYsJ-oLmyRQBNMWi8f2U1VLA4GC2FXjXVyNsXuRlrNIXx_OnrxosC6YlJCZeQ27H60ZeVKtqvf9HE2tMq0K_uNgMB46ftIuQ3-qLf9zQjSWxPVaHNc0fCVl9YzAJxa3cbsxitfwcOjRk0xjJstrPEYAGplNAJJrnol8y2i8-AnMKbKssXt0yeSikGqlF3ePBC3cZ9mS_QCF8SZD3_RFfJOyHrst8KySf-GiyWMBfi7eHCsPulSXf8TE2KC6i0d5zemHq5gjZwNn7xgXujp1QvLZEKvQHR6avP13vXaep5D3zLkUkmDrnTsK2RF82_HtZvuRCDMB_PwXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
لونین دروازه‌بان رئال مادرید بهمراه همسرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/Futball180TV/103370" target="_blank">📅 17:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103369">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9fc92de2f.mp4?token=UolY6FxOkUG1ti7Yo1SNEdhzbIKrFxs5d8r5LmLQKCDmKO-a8z27mCdgp63tY0SgWzWrglyRsfd26b_wkZ5I8uQOCRrDFxoILm90w2Y6xfG25PfxsOo69aqBaB0wb4M72tqCkFkAFhjwQ0HLsaltOHCqcR3kInnI9t7L2a5K_42gMg9o2e808tHe7fA2JUWgwLODr5WWDQKzW-xeCZfB2nMf42OzPkdI-SW7yS3LmzgD-e-PnTGe4fS5v6mM6LME_ryhFcbNrHel9vDVLjoJwk0GR8s4miKNVfg_XqwqgYlNdJd5WSQ1a7lkKoit8404-xUpsIPc3XmWry5lxBQain-zqabYOWsLtFfL4J0JxJ773DV7LNGVYEuja1IQ1MXWPzETQvCguQT8kNRv2yfj5p9ac2HiIEDJZzID8uQY_onxjiHNDn42Sm7sY24HrJIlzxXfsHqiy864w7falz0ep7XODTy-e2FWjO-f8eqGbepbt3JmYorg38-9Tq6pTdpE4TrbM8y4WBvcxJvF8WOsynOccqe6hpN8RKwcfU249XkYJGeCoaovaYDZQPmRdszVNNoMA54n9S4AYukPLpRgMhM9Lk-Gm1_xY5dZlWhcBZa0-zlKdHk92ZbAotEktOOe6XJ-pTzIKbcM1u4PiRkk5HavHaSVWYqVz3BRY8qApb4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9fc92de2f.mp4?token=UolY6FxOkUG1ti7Yo1SNEdhzbIKrFxs5d8r5LmLQKCDmKO-a8z27mCdgp63tY0SgWzWrglyRsfd26b_wkZ5I8uQOCRrDFxoILm90w2Y6xfG25PfxsOo69aqBaB0wb4M72tqCkFkAFhjwQ0HLsaltOHCqcR3kInnI9t7L2a5K_42gMg9o2e808tHe7fA2JUWgwLODr5WWDQKzW-xeCZfB2nMf42OzPkdI-SW7yS3LmzgD-e-PnTGe4fS5v6mM6LME_ryhFcbNrHel9vDVLjoJwk0GR8s4miKNVfg_XqwqgYlNdJd5WSQ1a7lkKoit8404-xUpsIPc3XmWry5lxBQain-zqabYOWsLtFfL4J0JxJ773DV7LNGVYEuja1IQ1MXWPzETQvCguQT8kNRv2yfj5p9ac2HiIEDJZzID8uQY_onxjiHNDn42Sm7sY24HrJIlzxXfsHqiy864w7falz0ep7XODTy-e2FWjO-f8eqGbepbt3JmYorg38-9Tq6pTdpE4TrbM8y4WBvcxJvF8WOsynOccqe6hpN8RKwcfU249XkYJGeCoaovaYDZQPmRdszVNNoMA54n9S4AYukPLpRgMhM9Lk-Gm1_xY5dZlWhcBZa0-zlKdHk92ZbAotEktOOe6XJ-pTzIKbcM1u4PiRkk5HavHaSVWYqVz3BRY8qApb4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
▶️
لوئیس سوارز ورژن ترسناک و جوان آژاکس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/Futball180TV/103369" target="_blank">📅 16:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103368">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITZFn9Clgfwkm8a-fQZSRUe0jGYErWxJ-7b-8vRLnZfnzOwxBW8RpXvzweeQsNG2KrZhB7QCwbmGkArNoqG4pLnXm_JB20qaZnVylAOREGnP3bxy47t4Uk7_MkwH8W2dKWXLI4te7rLhJLcTi8cjpExF4yu9Nhgr3qHsowMouNAS3C9epOdVlUuc1WIz8NKQVLNghmo8fz9PD-WS39lHTOzRcmwF1ALCI7ehMJlW8mCY3yUdWOkQYuyNiMZzkT2R0i2Nreqr1jx-dQ2oHTU2qRpNBBRP24OMNxySfMGOX8uUOvh9J1CXPKWJFBdLUTv4lisgSbA0E08xsvxJDsN3Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❤️
رومانو؛ باشگاه بشیکتاش، پیشنهاد نهایی خود را به دوشان ولاهوویچ ارسال کرده است تا در ساعات آینده به توافق برسند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/Futball180TV/103368" target="_blank">📅 16:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103367">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b011d4118.mp4?token=NAYL2TeT9KAOOyxMQIqE9s5q4kzNUt3M8lpMFb0FzWu-BhGQsoaSCI3Dg3Wh4nCn4m_h71PDAr_Y4s6b3MbU-yCbYYvC4hYPp_RDIyv-_ooUdqXSM2XPS7WhJAHtHVc-v-PTBaIY2twDjWVpjI-BJLS9-l1zioLN__LD90ChyLKVGT6H_kNb92U5wAIHJA0Lyn2XluxdH9tLftyLmwow4GohZVaIasUYMuWnkZaxvJGU84Wh-XjHaqR4sWQt4y9j78G_5IsQOLXUO87-JfsJqrsDfUUH8JaCraPx4LJUCWSnAxs0Rc55IA0XEkBTiZLYy7_0TgIeL-0pqOO_d8TY8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b011d4118.mp4?token=NAYL2TeT9KAOOyxMQIqE9s5q4kzNUt3M8lpMFb0FzWu-BhGQsoaSCI3Dg3Wh4nCn4m_h71PDAr_Y4s6b3MbU-yCbYYvC4hYPp_RDIyv-_ooUdqXSM2XPS7WhJAHtHVc-v-PTBaIY2twDjWVpjI-BJLS9-l1zioLN__LD90ChyLKVGT6H_kNb92U5wAIHJA0Lyn2XluxdH9tLftyLmwow4GohZVaIasUYMuWnkZaxvJGU84Wh-XjHaqR4sWQt4y9j78G_5IsQOLXUO87-JfsJqrsDfUUH8JaCraPx4LJUCWSnAxs0Rc55IA0XEkBTiZLYy7_0TgIeL-0pqOO_d8TY8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
پشمام؛ روایت یه وکیل از جنجالی ترین پرونده خیانتی که داشته: زنی که از انگلیس پا میشه میاد ایران برای خیانت به شوهرش....
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/Futball180TV/103367" target="_blank">📅 16:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103366">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcFayvvg1l1blujTUDRIhpSLlga98UNHTYpJbW0dRv9braaWDFooc4mOnYUn7TjeezK_I9L1ZupwWL6csDR3aM630OR5rHGhRDA9sNKByEkrCcdMqVTz8-a3fkTI5SNQ-OlCuBwsl3qoUNC5vUqAN7YyihUdCyiEi3ZrAQjRBbvMZW-U9JsNIHpXFH3xBlTJGbpmJb45o3C-qu4ZbxDF6xu7YPuE84PLxj381p8lsKxQfaVxdHZwkFPeM-2Soo7V40EhNepaBhQUo5onKE_VVt668zXFM_O_suoMJuZWpsobO5HkwXpcbI5gQajpAScaqbRxj-4altHZKE3GsDP5IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔴
آلوارز در تمرینات اتلتیکو مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/Futball180TV/103366" target="_blank">📅 16:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103365">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D2UC70vMnGniwCw7VB79EH2eGDvLEIlVwOgrxjXZ4ZNlaLBrlCviCd_mwL9Tm3KewgmFQb0MMxkZepat3xfH98wOafBX6cGPW8xUfKB2D-KTyivp04KHCNFw9B7xBUjVaWXDJp9J7zZ5nJ4yewQA3z_hNQbs-fucNvzCZWSUlz5iZahj0DzrTXgh-Qbg_EXOAouxGDDqeA4WfPI7tCH0oZcWq5LCpf8jKrDcAmuZk6N5H5OzhR2FA9qmUKYkVN2VrfnFZbBaulQZcU_3ycB-ResPTTOudDKFGCjxNvWPks26ugSergwItKRBwxDqaU4ALNBzoH0ph6UjKo1TQlltFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇪🇸
لیست نفرات رئال‌مادرید برای دیدار فردا مقابل دپورتیوو لاکرونیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/Futball180TV/103365" target="_blank">📅 16:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103364">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2091ae4f3.mp4?token=QuT-mgg-UQ9Fgwc3U6Go9qQ2r7oSHIP2GzuPx_0u2U791OtXq4PCArl0UwbiQ_8wQyt69Y0xZKeI0yg9Djws1n2dDScQyY5BhBkfQkXmR29hiOkyr1LBjtBysjt1RYKoiZ8IIC5KRzwe9AU7vD4_fKVrnIEIkG6gSC1HMLkyHwC-QOTCl1xxh3zXQmzPf4kjeQ2p9RswCzKkGayVSDRQSkYONPebuokBwJNMc_RbURwEAZFI6GfTzeZbmDH33L_ogIFOm0aFLoHQZm7l-lrMdf66MZgKrrNGL1AaiRsF0hnSXOBODqAD4WT39UP_2EARBtt1LLE62GfAvDzoZHUYcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2091ae4f3.mp4?token=QuT-mgg-UQ9Fgwc3U6Go9qQ2r7oSHIP2GzuPx_0u2U791OtXq4PCArl0UwbiQ_8wQyt69Y0xZKeI0yg9Djws1n2dDScQyY5BhBkfQkXmR29hiOkyr1LBjtBysjt1RYKoiZ8IIC5KRzwe9AU7vD4_fKVrnIEIkG6gSC1HMLkyHwC-QOTCl1xxh3zXQmzPf4kjeQ2p9RswCzKkGayVSDRQSkYONPebuokBwJNMc_RbURwEAZFI6GfTzeZbmDH33L_ogIFOm0aFLoHQZm7l-lrMdf66MZgKrrNGL1AaiRsF0hnSXOBODqAD4WT39UP_2EARBtt1LLE62GfAvDzoZHUYcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
رفاقت ورزشکاران
💞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/Futball180TV/103364" target="_blank">📅 16:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103363">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_Ht_QswgzMLV6UKWxQEzflSSlcceAhNVyYD_isYUjQ_Yjw494zDH2na-VO6Jpt_6MgIMO4ARm3zBXvZvGUvlXRaPnl-Ai2nMH76FHZix5w57rOwSc38uv8tUEyV-JgEnx5UUMWoiCRX9wYu2Y1EdnlT98XH44XYedsqgZqMzFylX8o-WdKTcFz8MjPa-_emrOqBb2x94msuxVbylmNLAn6T3KlDwNq_rj0NaScCWtlxSJtdVdC1VhbEgoEtlTojBdylYBnI3YxztrqZQtUDTJ35LvyZ2YfoP3EDmMUyLxXMd9Un07L2hp2z_wEc7eEqOFEGRK3ZlLgyZLxtlPKQEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دخترا: پسرا وفادار نیستن.
پسرا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/103363" target="_blank">📅 15:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103362">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFpOVJGeqUzrMiauv70EY0zceCmlnCnvRZBM7Ea-aw_PupmWFdgPKRJVGJkf57c3mMwT2FfQ5ReuO_kj7xzth3LgDYMpXyuFBqjnf5LW561V8ZIPIAM0kKKi8T_80EHqRUfZgteTeY3lX1D_AvNM-DQDXG5BrXD2Ol05aCpIZAdafid0V3Bo2GW_6QbR2XWGvtI48XFoJUtSkfZ5xAxftuBQHZJPwdSonj81xipQft7uvatqTpgoq2g4R97c7GrCuwe9m-d9axqf7JiW28trCn9k0Qzrkp1gYiXZqIbfzBiuDUuq0Uey4sCoWZFFET8ePh7nCuWVe4VbqylDN1KloA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
✅
فابريزيو رومانو:
اینتری‌ها میخوان هر جور شده اسپنس رو به میلان ییارن. اون میخوان این انتقال رو با کمتر از 40 میلیون یورو نهایی کنن و مذاکرات بین دو باشگاه به زودی از سر گرفته خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/103362" target="_blank">📅 15:18 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103361">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bea6d735e.mp4?token=EeGGPe6AjWiAkmkXx4LqTOxF_PrgRlFhP4lTAKuN5jhCe5WR_VSwtsbshPZCgQquoW0CH8P5rcaynGIA7-YJAAW0dpbYQWS8jvwvq6osHQkZa8-9hZLF7IB1doixQlfGFjWQHq_Pe528dwjLHr6h32OSm1R0-Kwb_8wd2rdPpTTZUjKgp00B9r2d4RLFTKelDCbhbQ-2KwAEZ_B0TF4YxfN41ZOaL315T7cEjaACvYFj1Im1hKfDinariY3zXXJczOBYfwT7rY9BfnLAvUPpg_vxaOHZfg7ImVb3hGi1ZXhZhzLJ7Q838yBUTQkM-onmk9DdwBi_RFEnitG5KYyKyjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bea6d735e.mp4?token=EeGGPe6AjWiAkmkXx4LqTOxF_PrgRlFhP4lTAKuN5jhCe5WR_VSwtsbshPZCgQquoW0CH8P5rcaynGIA7-YJAAW0dpbYQWS8jvwvq6osHQkZa8-9hZLF7IB1doixQlfGFjWQHq_Pe528dwjLHr6h32OSm1R0-Kwb_8wd2rdPpTTZUjKgp00B9r2d4RLFTKelDCbhbQ-2KwAEZ_B0TF4YxfN41ZOaL315T7cEjaACvYFj1Im1hKfDinariY3zXXJczOBYfwT7rY9BfnLAvUPpg_vxaOHZfg7ImVb3hGi1ZXhZhzLJ7Q838yBUTQkM-onmk9DdwBi_RFEnitG5KYyKyjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادل و دستای پشت پرده فوتبال
😂
خنده بازار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/103361" target="_blank">📅 15:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103360">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsGQY9ozOkQYydFzLY5YVdvCZdhFJyH_3U29I9_LI43bEZmJ-u-tyjipxGtuF7mRZ7WXmKeaVFX89rnsjPXsIKXVOnSqew3sAIkwVoajNRa6l-PfjjUZ1QrUnkvEcSngqbpRLZrKgyhZVYK6IqsNPf0vDbZctK_uBT3fJuARKU89_iHt8GKTckybzkbiC8rd0Xf4A6jzdc7Q2DJrTKTxSEZjdfUZovKo0eLbOFhd_14-zCoGt_6_0Yahv017jsz-fXnGmD-IpGA5evw6B8inw2fnfzYttnCLDMCgVrAgpS94CClznN36XDJ5Z9ApjxEgipbCwyY-NQujT7TbjbuIWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
🔵
فابریزیو رومانو: فلیپس با قراردادی قرضی از منچستر سیتی به شفیلد یونایتد پیوست.
𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/103360" target="_blank">📅 15:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103359">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aRm9yt2BPEI3i-UYsZAcn0syX_HAxCR4zs8p1vLJOcffOWqKYHsl4Wy9aMJlDsefdMvz9LbWutts-mNRQeNLmQjno5LzEYsm3OjnUCTLU5gMBr9zYU9umPs2vy4hGbhPtfFMOGOcDgAUlbKWyj8jhyockqqlFNlts7HHFX_0FwJhwdijdYDhlOz4lhjteEpD96BJiVUsPbK4Bdd-BFiuDGDEd_tcqlsDUSDBwBPbuJMT60nF49EA9646DKHAjN5k9zFnZEkQ0g-9gT3Bm5tU2pq4jJPXPc_Snd-uWJvvcZwBHa9h4BkAaIlqddknFp-kIFJfK-pAqZyC_Cw7rfpXjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
🔹
خط دفاعی یوونتوس در فصل 2016/17 لیگ قهرمانان اروپا فقط 2 گل خورده بود تا اینکه در فینال به رئال مادرید رسید..
⚪️
اونا تو فینال 4 گل خوردن و جام رو تقدیم رونالدو کردن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/103359" target="_blank">📅 15:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103358">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1146b9d2c3.mp4?token=Q78oXehsHLOThOpiEMrWc-Ekq5axqG1VuZzXSka4gPOuXbnFtyRI3HzAvS65E4E0Q3UHQnmzmCjYoYCBKvst7hwiw-xqaqtF1ZSbSg8pZ9tOb5Yomv5RaljLAC5xVsw4zBgR7YTmX3jLYZW7hJn2WIjOf_fMwAJHvxrmkVBGnetST8OvZ2FS0fvhIRY8Mk5aLvmsX6k-C-lyXha_GzOPWq9WXhg80r4lZBI67_k9c2CouBkPV2XQRBHj88IXBB6XS10qEG2Zbs1Gy0gRIfGzN-GpliRt2gtgv611L9vseQRoHNrRi5fhJS_Rdx3tfD6ABKJApIL2t1vQeawDw6q9jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1146b9d2c3.mp4?token=Q78oXehsHLOThOpiEMrWc-Ekq5axqG1VuZzXSka4gPOuXbnFtyRI3HzAvS65E4E0Q3UHQnmzmCjYoYCBKvst7hwiw-xqaqtF1ZSbSg8pZ9tOb5Yomv5RaljLAC5xVsw4zBgR7YTmX3jLYZW7hJn2WIjOf_fMwAJHvxrmkVBGnetST8OvZ2FS0fvhIRY8Mk5aLvmsX6k-C-lyXha_GzOPWq9WXhg80r4lZBI67_k9c2CouBkPV2XQRBHj88IXBB6XS10qEG2Zbs1Gy0gRIfGzN-GpliRt2gtgv611L9vseQRoHNrRi5fhJS_Rdx3tfD6ABKJApIL2t1vQeawDw6q9jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
تعریف و تمجید ستاره‌های سابق از لئو مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/103358" target="_blank">📅 14:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103357">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfxlXhm5V9CLVIb0FdIGzkjFiY3Xhj84B076Z86Ivi5eOSHwO5nyOV9qMIUUbwPokUQ52UyRb8zsRs8UzNgu3rB45S-DcBqD-oFHnFr0QEihWILNswNDavDMdl4mSh9EguJtb37vgHtxxBbkrBsyqd4c_WpzHwLO9uN1_hf9EWWkgo4Au9bcie4r20PA19jCzq1dDJ7UbM93gDtUbVFIypW_NOtsnykdY1tHJq3xpKzg6BiBol1KAm7v2wxBytNuxjYi4AQl_4BP4yvaQuEVBFVZyN4aOO0jOeGJbHTiwDhqpnOSVgBGmRkqJ5_HmLn2wcmYathaeQYz8sMAUsSLGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
#فوووووری از رومانو: دیگه مثل سابق قصد حضور فعال در اخبار نقل‌وانتقالات رو ندارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/103357" target="_blank">📅 14:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103356">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/befb00f0c7.mp4?token=gBZJJ-1l30sqou2IkV3Si2purOSZBmHDYR5dZN3VfFdbzESuZ2g4XDFSlM7bhV7Nd4OJAKXgl6hJsJWs5nxZWg99wAhpRLTbeqDFAl7bZSTsnfVHLjik-6kd7dKRXxACkiaV7zbmolLr8xmRtptqSfG39HQ3kT7r8VnId-J6awrShcFuB32kt4uxWoHlGGPkTzWRx8cceviRlbjA_t2syBAxZs-n8xCCfxgzRxitcZBVHu0Qh_jNj78nCTrfJGJ1dhic1POWqNQzzayD9MDAIWUcInA7P7CNOVC5W8EGkv_1ZNeSHe_oF1O2a98GiMK5H3dQaUCoGK-zCc-AfQg5DJDdE3fhVM1i2LVdix-U3AQilQ9wSqv-j1btrE8y0MxHrpTWnwWIGIUl35hf6loTYB7XSxU6HxqtaaNRILHfrtu_-3UzD1cwYyf2QWdVXaW_d8wUqQQrLMdXS0D7o8u__yQueW6SPjyKCApH9imxCX1AQ_tHu7Mi6_YqaLRr41LsjausmjprPulex0IIVkOBFZIB6MgOqSLhoCdaJJzASEs4kI4_2CYIAMHfnCEce8N0SsXLma68opmrXBpRkbPvGBXeB_GuAIN8v1xBCOdvTl6KjfUke9HqrELq9sFHwCRMa-X31-PY3_wLJbLPjaEiawkS467-ax9d7kp1HY5p47E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/befb00f0c7.mp4?token=gBZJJ-1l30sqou2IkV3Si2purOSZBmHDYR5dZN3VfFdbzESuZ2g4XDFSlM7bhV7Nd4OJAKXgl6hJsJWs5nxZWg99wAhpRLTbeqDFAl7bZSTsnfVHLjik-6kd7dKRXxACkiaV7zbmolLr8xmRtptqSfG39HQ3kT7r8VnId-J6awrShcFuB32kt4uxWoHlGGPkTzWRx8cceviRlbjA_t2syBAxZs-n8xCCfxgzRxitcZBVHu0Qh_jNj78nCTrfJGJ1dhic1POWqNQzzayD9MDAIWUcInA7P7CNOVC5W8EGkv_1ZNeSHe_oF1O2a98GiMK5H3dQaUCoGK-zCc-AfQg5DJDdE3fhVM1i2LVdix-U3AQilQ9wSqv-j1btrE8y0MxHrpTWnwWIGIUl35hf6loTYB7XSxU6HxqtaaNRILHfrtu_-3UzD1cwYyf2QWdVXaW_d8wUqQQrLMdXS0D7o8u__yQueW6SPjyKCApH9imxCX1AQ_tHu7Mi6_YqaLRr41LsjausmjprPulex0IIVkOBFZIB6MgOqSLhoCdaJJzASEs4kI4_2CYIAMHfnCEce8N0SsXLma68opmrXBpRkbPvGBXeB_GuAIN8v1xBCOdvTl6KjfUke9HqrELq9sFHwCRMa-X31-PY3_wLJbLPjaEiawkS467-ax9d7kp1HY5p47E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇪🇸
لحظه‌شماری بارسایی‌ها برای جذب رودری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/103356" target="_blank">📅 14:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103355">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kggoDH1UpMvLvHJ9cn48Hdbftutf8qhQdGsXTKnfOvFvUI8jbGtwwRiat1aiHXrD3xr-xAxsihXSXJTOYoU5SseoHSs0do7ZpKhGCPMtfVrE9MUSoRK2SOcmjTbhzd_qp6IOKiy9gxlplBk0tYuA4lC20pKhq34MGo03jO26x29JOoo5YaTo0d_wy7dSJezKU0l1VZpo2CdzispHlKBaR14oyDguU30lj9YcBQB8d-yIVTnP3O3Vos9zw_dyJGnuwX2DKEm-ImVJsZQr_1hzLvcPLM_e69jfQRHYUrK26VbQRlpL6k3YgZxchLTtUebgZgKiNeVEJ8eUvzWPCEjzOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/103355" target="_blank">📅 14:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103353">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
#فوووووری
از رومانو: دیگه مثل سابق قصد حضور فعال در اخبار نقل‌وانتقالات رو ندارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/103353" target="_blank">📅 13:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103352">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KO2PIRfkUJJRsMt58kTSUJvuAH6vuaYXwi2fmen6Fxom3FH5VY8VP0aKsMLQvodGn9UO26vwKaonAXeZmrSCoh-IRkgltT-BNpX3rb14yZt8t8W_JQaOmf-cOJNSJnC3yWBrnOCYfpnokLDdGxImbaHoylId_G6fX7uW2UqzhDHqLFkbwedQR_DhzXuKJjNj2NPNsoiMnhuCmFwYKuVj1s14r_tv9slRAq2enT-ealyJb642rI3G2M_EOGHz59JmYX_VHRxP6-YYVWLNuH35QiUYKH0Gyow82eTomhXeDw-noDSy8PGA2pCijs99AaHeCn_c66ef3UafMCeJIHBuWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
😆
سال 2021 قبل از بازی منچستر یونایتد و لیورپول، لیورپولیا میدونستن که هوادارای یونایتد میخوان جلوی اتوبوس تیم رو که داشت به سمت اولدترافورد میرفت بگیرن و نذارن تیم به ورزشگاه برسه.
🔻
برای همین لیورپول یک اتوبوس خالی رو در مسیر هوادارای یونایتد فرستاد، در حالیکه بازیکنان و کادر فنی لیورپول به طور مخفیانه از یک مسیر دیگر به ورزشگاه رفتند.
🔻
نقشه‌شون دقیقاً همون‌طور که میخواستن پیش رفت و هوادارای یونایتد اتوبوس خالی رو متوقف کردن و حتی لاستیک‌هاش رو هم پنچر کردن، بدون اینکه اصلاً خبر داشته باشن اتوبوس واقعی لیورپول خیلی آروم و بی‌دردسر از یه مسیر دیگه به سمت اولدترافورد رفت. لیورپول تونست برای اولین بار بعد از هفت سال توی اولدترافورد یونایتد رو شکست بده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/103352" target="_blank">📅 13:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103351">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9708df2d85.mp4?token=BMwGioKqYB_TrOI5YDCuIA7-FX89agrIKk-diBjqa9CKl84uyoZ-obz4KwJDYbu8vY072cR898rDnqHUBBWZ8uZQIv0wPDofFXi8zo4bL9vP7cNmCV3_Z6GSVHVKEfeEiRdHKrIj1cWniSQgK2yoC-EHsMQ9bsc5BlhSfZ6ZQ1Qh9vJtP2XLVZJ7PtWn-nU7B-Pbxd_8X8WjXyCO0TzsMXe8mLgtefxa47fMePPiNXMySi_aRIzNj65bQtxRLx57WSrsvv456jeescorgysMyyyIhOZmdPObZvuH3eMqgHF_UYOzBMngqmT-eocADdydNnEi8mw2weCjzqqYkaQvtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9708df2d85.mp4?token=BMwGioKqYB_TrOI5YDCuIA7-FX89agrIKk-diBjqa9CKl84uyoZ-obz4KwJDYbu8vY072cR898rDnqHUBBWZ8uZQIv0wPDofFXi8zo4bL9vP7cNmCV3_Z6GSVHVKEfeEiRdHKrIj1cWniSQgK2yoC-EHsMQ9bsc5BlhSfZ6ZQ1Qh9vJtP2XLVZJ7PtWn-nU7B-Pbxd_8X8WjXyCO0TzsMXe8mLgtefxa47fMePPiNXMySi_aRIzNj65bQtxRLx57WSrsvv456jeescorgysMyyyIhOZmdPObZvuH3eMqgHF_UYOzBMngqmT-eocADdydNnEi8mw2weCjzqqYkaQvtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
مقایسه مراسم معارفه در تبریز و ترکیه؛ فاصله جغرافیایی زیاد نیست اما فاصله سخت‌افزاری کیلومتر‌ها دیده میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/103351" target="_blank">📅 13:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103350">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIrN9xX0Zw8EUeaxmeOsV8ist_DkTIgoa4LeHarpjzv_VmjMU-g1L12CAQrMEhNArr5HyFvTIwgXn9HoNwQHH2R77xLhIGWIgjDs-l91e4wCofvyPgxBZu8CrIqVdm7xafRv-EKEN0VkCApXccKrY1_hIq20HNrtrzwSltZQ2QYxsOuUsj7hOdbn-olZ9ARulUsaI5qd8lWi_3q9cpUragFoCfBU3z0Pf40hNM6CdY2N0KPSUsU_gk2HTfa8JKpPpjfNGodXsPXBHLwq5Z_HSl8wCpitqTjuZGtRttMWZt3crRS-gWoxsFP01RVCNZsT-OelHoMEr8no2u7UlOjO4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری
؛ ورود خولیان آلوارز با وکیلش به محل تمرینات اتلتیکومادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/103350" target="_blank">📅 13:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103349">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/705d7fe27d.mp4?token=MucmOacTlP7ZGyCw6dqt4JJEvEcvvM4_Cg_u2nlqj_aFvOg99Hu5HvoTqlYq2yUVKqyZR2fBmbi_WFVASVfx-cW6WK8rfxCAfbf6fX3ua2KW2qYJB3nObw42yOhzW5kmcC4bOGBFel50GdWM7tP298UxQm4icasCfiCy4CLzBs06ONRVUwUpFZyoY0At0h-sYcijmeQ3pAIQqv7G85E6G0pmzXfJupv2I5ZxfmklQ_uTbz-gK-rq6ZyQApmX2rF322qdtWcDhI-MdPVJVraKefv8QuM_SHngYVmvRmV-UACI2EDGgjcL93Rb-NCdINbokcOYgnvfXDx-oy7AaCXu5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/705d7fe27d.mp4?token=MucmOacTlP7ZGyCw6dqt4JJEvEcvvM4_Cg_u2nlqj_aFvOg99Hu5HvoTqlYq2yUVKqyZR2fBmbi_WFVASVfx-cW6WK8rfxCAfbf6fX3ua2KW2qYJB3nObw42yOhzW5kmcC4bOGBFel50GdWM7tP298UxQm4icasCfiCy4CLzBs06ONRVUwUpFZyoY0At0h-sYcijmeQ3pAIQqv7G85E6G0pmzXfJupv2I5ZxfmklQ_uTbz-gK-rq6ZyQApmX2rF322qdtWcDhI-MdPVJVraKefv8QuM_SHngYVmvRmV-UACI2EDGgjcL93Rb-NCdINbokcOYgnvfXDx-oy7AaCXu5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🚨
‼️
تاج: قلعه‌نویی اول با ما ۱۸ میلیارد تومان قرارداد بست بعد قراردادش به ۳۰ میلیارد تومان رسید. ۷۰ میلیارد هم برای جام جهانی به قلعه‌نویی پاداش پرداخت کردیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/103349" target="_blank">📅 13:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103348">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
🗞
رومانو؛ سوزوکی به پاری‌سن‌ژرمن   HERE WE GO
🔥
🔥
🔥
🔥
✅
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/103348" target="_blank">📅 12:57 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103347">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gv2KrIXWiO6Ewt6jCujX1KtgpR2xAC_-rMNl4DBZfmvAJD8ACsmYgBVJEwE24J7FZAaWB4UiZ5-QKsjncQn_xHKR6-QNVII1_gcKp6VPJaznVVKyUTZEqAwLRTriq7nbpQmb_dFoOfoZT-ausEmOvCaA063rC6Xq6cWCkUr_Z2FDI0TlFwGE_MO8Oh0jImd9ekjOq1rEJync0Jtyhcrmu0xS0s7BDSSeK495ju7EI2hgVWQ78S1XPzkM6JXog2_c2BrYLGtfTMb5H6ZrmXhOg0UVBHs9dmoz3YpZg3W-IdBDNIGHDLjNSBv3Hlht6bM2JwVlP8ULndzhKE-y9S9NFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
✅
هاوکینز: باشگاه پاری‌سن‌ژرمن با مبلغ ۳۵ میلیون یورو موفق به جذب سوزوکی گلر تیم‌ملی ژاپن از باشگاه پارما شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/103347" target="_blank">📅 12:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103346">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQ-yXGhcsg7VjR9ltvrqwgJUDt5m3ZNgo_VLfSq5O0-GMP0plzovhtpFfdJ_ynJUHhGvx9FPlDbPNsBeBXEQfccZD3njL0L4SEl-fJV-Hq-kxG3lZta6RXCXAok03tuW7YlnWMx_FkgnuqYDkidAkF1m6oSWpyqiJGfBao_kghk55QVLOXtOuZHpNCvcO986jtelQPsoMPE057g_Cvq66du-cEWJbOFgqmoEhhug6aHoRduJdfOjriPhflCTlLo_PtZrNKEYYELHaqrThRRtMx7IOYHrpE6F64F3yTxWb0WV0YNrsUOsKTGz8Pl9PyTWm-65n_AS76qIEnM1Cw6ZIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
✅
هاوکینز: باشگاه پاری‌سن‌ژرمن با مبلغ ۳۵ میلیون یورو موفق به جذب سوزوکی گلر تیم‌ملی ژاپن از باشگاه پارما شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/103346" target="_blank">📅 12:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103345">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از بن‌جیکوبز:
🔺
منچسترسیتی اگر بخواهد با انزو فرناندز قرارداد ببندد، باید رقمی بیش از ۱۳۰ میلیون یورو به چلسی پرداخت کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/103345" target="_blank">📅 12:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103344">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LshF0JEsg1k3pW54jPwIXk53V0mtNkpN3vgSj13gV3a0EY-QCXBcLZjQEwkpPjEIsS56Kj9st3ngMoFvkffk9KndKmUZjd3uavpX1YuPAHNh3DhWV2sEZ36acAjgp6TOtLmzivCXtFg84TgkKm_uTO3NzwTHZcLo9wo0FyBXpke5_M3_b4MslyQC_hW2SlC43A-GTsj2sIl4kr5o0WnVaZ_AFoHRHdUGsj_uL5fpqJEvyEM-aDRbLBBcMYuOoxVTveaSsyw4FUOT7f8x3KSI_kxP2Y5oa9IORLjlABA7h6GEU7YUlFlMrWDnZY3qiSrhi9gqTi-LVkZwSmm3Ybjcaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📱
استوری کنایه‌آمیز سیدحسین حسینی
که احتمالا مخاطبش رامین‌رضاییان هست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/103344" target="_blank">📅 12:48 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103342">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JUEaeV_2ioUf8Wpwx8A7FfBzoMdc2_Gs40DJspKYeXnfqp7ivTIbGTaNf3zh3jdwxS023f7XITlGdFf3QrzzRMi4ZNu1X_Uf79YCXqnLLsb3DXVSOKuBwX3Og_fzdlezgDOWanoDizG8Qirdr1w4fwacgs3YwwJr3pK_RnjjjtwL5OVU4EoIZDc3RgMdLPQnp94HsBFHKsiR5WFuwrsWoRzJRCF9tj_cDw-sWRX-PPw-sruZ9vFvHFIDLuOUvrR25QepOm0b61GEM72BnZ3xR2CV1LXjgPgqgI_FyfR5Z4lbDrV9spakYKt0xIu5WMCdI8tQrKzvsAAOzCJN9Jc8XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kQdYGzRKDRkICaft145KsjKAaXou0p_qdQc9JJ61BcY8k0WaJFop0eq_PWqUTMrcBa6AJe-ZpFYeP3nV35HEKhFoNMDIN9kociMDWvNhqmX3dSANPsF6vykgiMx_wxZVAUTwiw4tVxMis3kjWbzSpBmqNiJqOckVXZfZheAxizg9nGqcpyKIsVEj_1Sl0eKUYSIc_3uITBWHIWPDWBoptvLGfo20orVYkar66V0nlqmnCHm2_SXCZsrxIqpVU84tICz1Qc5pGLSU9UPbYLvOgVz2gafd70qd8IH8cysCiHnLVG16C5GkEV5UYI48pZcBkqV7VIZrlpqYLQOWFG4YCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇫🇷
لیست پاری‌سن‌ژرمن برای دیدار سوپرکاپ اروپا فرداشب مقابل استون‌ویلا انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/103342" target="_blank">📅 12:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103341">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yyb0O03rAUd6aj_XMH3CcZ7Gk9wwCOIkl2Hzex5FZCiROOsh6VuHgQ0ox_zxvPpdfiurZCI5pVKeN6WpvZ6M0hds8soQJmbji89wlXZNyAennwdLyttSt9mQMsxjEzQD_C8bSxg4th1uZy-YX8kRuapIVHCpRzp1A-2z4YU8HN-YZy0RKiJ-nMrUWKaCjVWe6rTmVTDRpbKcPKc8u5kUPK8FV-iIuA1lSpbY9LIFXW-0Z8M8sH2J94DXcvj1Z3SygsqnEKR6_O7781usWHH6cQEAUSjVyvfiBLFT6oTs0RiWLQJMKwjo0xKVLs77b7rpyFEU1EuOgoFYHopzv4333Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شما اصن تیمو ببین..
بهترین بازیکنا رو تو هر پست داشتن ولی طرف اینقدر عقل نداشت که مسی رو هافبک بازی میداد. همه جوره این تیم تکمیل بود ولی فک کن قهرمانی لیگم حتی با درخشش فردی بازیکنا میگرفتن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/103341" target="_blank">📅 12:27 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103340">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/roEjJbxw8WxwHZ3me4smK4NTsp69bvCL_vgUvtA6U3QTRe4su6z3tXy-QVUodxqk_IHbQCcmFYfUKTAdo4Pf-bUhvK0bEt1eVR_dbeGlFbkD7nVV42Ts_XQh_M-z8lXGFxzXgPVSIFxahLjcqNKGHyGCOdEef5KcMm0MtbLIg8abJWClsIB7S8IYGDY8KVuc1r9g8iChmWs2IAUBf5-XrL__njRq02x4fvQa7MOh7a9iLenxP68FzyuKMvNChXd-Ps3v__YguM3nNcriBpLwL1KxBNiqNbwanFUCavN4CXeo31l0HW5O_fCeHB0uJf5b7jy1GyBGFgeErnmGaEIPwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رومانو:
روملو لوکاکو به فنرباغچه:
HERE WE Go
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/103340" target="_blank">📅 12:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103339">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnAoaeHgTkxVzvmJQzqwsGcVedPLSCRN7kwM3abX741_lZuXifVkwE_FSx1-Qy87k4s2gN8eWKaU2ae0QbDN6m3djVzxecBBiWH_F8-W2zttjgNYTdmsEi5qImLNtfAfc0czGVdPW7I_dwPuDU5tL-jUdPdOQLKueJBJHgr0jrEJzdmLYuCnPi7WyO626rpPvfzzFqmlHsOf7oO_tz6M2w_H0uJtswBHM4QJUXcihVbT6SRj7VNAWhnP8mE1Ew8WsXZtUrYfCorqfclHBgV6ThnWMh4-qSEXz_ag50kPG2QMmoC6sNLMVDghS9G5YqlQQ9yFMsNy12hSS1hFrhBviQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
مقایسه بازیکنان خط‌حمله وحشی بایرن‌مونیخ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/103339" target="_blank">📅 12:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103338">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AYzaQQ9UW0Q0KGDo86gOVTZfTLiKpq-UQ1aAnU3pRM2JmFU4RZ-lSmAE4skcRf31Z6cTlLYJJB6YUx-Lep_lT-PmKf4vYRkPA91uj-OM5BlXccR4KfrXObrdTlgvyTXSZsCvPTAgQUWEJIQUnOQE_K5mjj_o0ewa8j_Gm9pwnGIQeOa4dOD9EGhVSmHTLH47rsQMQrDvdKMwCdr_zqicUh1JI5nK65Rb_DfQmdjnhG_qTwq1CJdc2ZYC3jIo_ywGGy8_1fMTjf7Eg86KzBloUC4jLTstC2iFHDxx8AQqPLtnipZWpwSe-TNXUav0GIN4BGEfCVeWo1PZiTlAXcqesg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
پیراهن دوم و سکسی دورتمند برای فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/103338" target="_blank">📅 12:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103337">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSi_Z441lT1zDhdDnslyYKxniEYjf3N6DSNfinvEtKxoWNTY5CGFJLLfwZd2Vpsz3cIoVMZmjioBhCogmBeo1B4P_Y2NPInsdv4VV_dzm-rE02j1Q5p_Q1cRyY04ZE4A0OBw_O0iHI1_apNc1MSWUfFnRTO5539TKsLrAgy6ho5xdqozHy6n3TIxWmtxiNPhrSg2xyAoIOcRuN5e_ZxccxbWghFo8E5iTvy35ra5UxdlczQ8DCNJexZxb1yYJ8y3rhmL4o5hcgGBrdUU_1ZPzaxpxGlP5RzD_V2rQAgR6dIY4u9pTjngwShhFKvkd-r2GWtFhUssEtHskw9o1m2CBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری بامزه جواد کاظمیان
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/103337" target="_blank">📅 11:48 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103336">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38d8c12332.mp4?token=CGi0oysZR3eMk9a-rR-2V_X3_iIte_tid2vjFksNJ2vF3wSOwfYaIBW2HJPNw8120ZqTM4sqW3GOvdBQb8AwwGZTA12RySA-gGBJ2_vAshRqff6sOZhto_X0VOX2cWUZtf10aKvz_Crbrfwi3sz2Rereeom04_r7SbJgLin4AqKaxPB4_X8auB_emjeDCXfjbkqdz1VA_ZL9vc5acddDCoZgjQyrbzhtQgUIpLy5MsIfB6PPBa_e3tKuUBJNAIMKsl08cB5O3f8XuslYCderDBaa5dypqwH6n-4V4IIXhuN9XNgBRJYTVRSjKeSPG5THxYZzJmweN35KPYoAum2-oSicI3FBBYl51-1_i3ZFZoq4HIk5Ky3fDQf1ykAqyCGPiqyK2zZLRHQL2mRzXvpvsd0e9dXCyzDlz_1kxnBrkEElzTMarFb5ZF5xKIMRlCqm9aqKgCY940us625lr0H55Zys1R_CDXZ9cPc02sBBpN6B5a1UI30j2kIwGUtA_QHuZC_iXjnzqIEh4UdZcWeM4YJ63VZcvMbijJkpPIMlTmPzxna3oE2LF8wiGXKBfM94PNASTg1fC1eWtNP9lukAxUjzkN1At06fj4c_JWvLdjNhyZyyFgOi8zNtVZniekyZioa2njzVXSmPhpRgLP9KfXtOBNZk4wqmQisxhjuLGTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38d8c12332.mp4?token=CGi0oysZR3eMk9a-rR-2V_X3_iIte_tid2vjFksNJ2vF3wSOwfYaIBW2HJPNw8120ZqTM4sqW3GOvdBQb8AwwGZTA12RySA-gGBJ2_vAshRqff6sOZhto_X0VOX2cWUZtf10aKvz_Crbrfwi3sz2Rereeom04_r7SbJgLin4AqKaxPB4_X8auB_emjeDCXfjbkqdz1VA_ZL9vc5acddDCoZgjQyrbzhtQgUIpLy5MsIfB6PPBa_e3tKuUBJNAIMKsl08cB5O3f8XuslYCderDBaa5dypqwH6n-4V4IIXhuN9XNgBRJYTVRSjKeSPG5THxYZzJmweN35KPYoAum2-oSicI3FBBYl51-1_i3ZFZoq4HIk5Ky3fDQf1ykAqyCGPiqyK2zZLRHQL2mRzXvpvsd0e9dXCyzDlz_1kxnBrkEElzTMarFb5ZF5xKIMRlCqm9aqKgCY940us625lr0H55Zys1R_CDXZ9cPc02sBBpN6B5a1UI30j2kIwGUtA_QHuZC_iXjnzqIEh4UdZcWeM4YJ63VZcvMbijJkpPIMlTmPzxna3oE2LF8wiGXKBfM94PNASTg1fC1eWtNP9lukAxUjzkN1At06fj4c_JWvLdjNhyZyyFgOi8zNtVZniekyZioa2njzVXSmPhpRgLP9KfXtOBNZk4wqmQisxhjuLGTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
برخی از جذاب‌ترین گل‌های آردا گولر ترکیه‌ای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/103336" target="_blank">📅 11:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103335">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🇪🇸
#فوووووری
از اسپورت: سه باشگاه آرسنال، بایرن‌مونیخ و پاری‌سن‌ژرمن به جذب ژول‌کونده علاقه‌مند هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/103335" target="_blank">📅 11:30 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103334">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79dfe7c98c.mp4?token=DFsvKBcp0XghDCn7LiEO5G1akNBMUUinAN5u9NPunLdortdcIKLpgza-lvIBr-C0sypIweo_Kizc0fdME3wz557llUOhbwywTRmsq_qMpg0OLwFWHyieLc44D3-rxQYOuWVEdLUBktYt9PMPv1FNsauhfbbXVrp61pjpwPFiuFCeysS8AQhoEcvFEtI9hEQQlQ4d3HGhwMrXXAuE_jvYEFzl1TZKrDs0MhHaWwMp64iec2zz9i43sIs4I9kBc2MRaiVfzZ4rDlkCRFvxNnxr1g4m07lmkHTZuyDee3whOVwqo75MqD22pLCw1c98FKrfXRpDf2osqAQLE3tqBw25eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79dfe7c98c.mp4?token=DFsvKBcp0XghDCn7LiEO5G1akNBMUUinAN5u9NPunLdortdcIKLpgza-lvIBr-C0sypIweo_Kizc0fdME3wz557llUOhbwywTRmsq_qMpg0OLwFWHyieLc44D3-rxQYOuWVEdLUBktYt9PMPv1FNsauhfbbXVrp61pjpwPFiuFCeysS8AQhoEcvFEtI9hEQQlQ4d3HGhwMrXXAuE_jvYEFzl1TZKrDs0MhHaWwMp64iec2zz9i43sIs4I9kBc2MRaiVfzZ4rDlkCRFvxNnxr1g4m07lmkHTZuyDee3whOVwqo75MqD22pLCw1c98FKrfXRpDf2osqAQLE3tqBw25eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
ترشتگن در اولین بازی خودش برای آژاکس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/103334" target="_blank">📅 11:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103333">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3329c503a4.mp4?token=hfrEWfy4OjzKqmj3AhOCz_O-rP1k4ddOIkWQCmvxTTAtt6vV8MaaMvYdiIsClewh1yyWt9A7IZZVgBIDSQlv4OLpWDS0eK7BbwdILgAVmBf4AhhPQDj3TZjUAd5IcjBKb94lrPoK0e2eFbUFH8rTnWDVrDj4RPP7rOtvCb1IjjSPxNOJEG1zFI65RO84SxhIwJdOifaFq2BepHiB9o3nz6OPVEo0NunwyV3MIua0n2UWkzXyTwJqnRWKsU5VEtm9OlOgboyCXXh7EtHg3Y1I1zJwMf9uAui6RQgU6_Z_YKKT_QCsmG1UcQkbkqVIHxec7bCd2rAke9Ewi8AhV8riEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3329c503a4.mp4?token=hfrEWfy4OjzKqmj3AhOCz_O-rP1k4ddOIkWQCmvxTTAtt6vV8MaaMvYdiIsClewh1yyWt9A7IZZVgBIDSQlv4OLpWDS0eK7BbwdILgAVmBf4AhhPQDj3TZjUAd5IcjBKb94lrPoK0e2eFbUFH8rTnWDVrDj4RPP7rOtvCb1IjjSPxNOJEG1zFI65RO84SxhIwJdOifaFq2BepHiB9o3nz6OPVEo0NunwyV3MIua0n2UWkzXyTwJqnRWKsU5VEtm9OlOgboyCXXh7EtHg3Y1I1zJwMf9uAui6RQgU6_Z_YKKT_QCsmG1UcQkbkqVIHxec7bCd2rAke9Ewi8AhV8riEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⚠️
لحظه انفجار در جایگاه CNG یکی از نقاط استان کرمانشاه که با کشته‌شدن یک نفر و زخمی شدن ۳ نفر همراه بوده!
❌
دیدن ویدیو مناسب برای همه افراد نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/103333" target="_blank">📅 10:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103332">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cdc7b28e6.mp4?token=B7GzQxMU2uL72AeRI2gRYODa-5leIihUZAVp8pxGdtF0Fvn-A1x4lgv6jAq6e3ME7cdQEfSOYx07VYo4f5r7kwGtAUovsubOCfYn3WptIF8iDlpF4Z2ic-6zeBtuBbU_cNtFpxBGkWI-rv9OebFTQOYt9VbqfQeDOnKl1jRZmN2LC_AdBJ21C978qQjiLudQsoP3EJnrdsovs0e35b9oI_R7LLDCHOTUG9LxH_Y4UFswUoefTwwRUcjelwxHjuYiDTVl0UX42QkPfAE6IOEOpinhPTSPbO8sxlIQTFFGYqbgY2lHayQZpgZUkF2N5QPYPHMDGtrZYNWgegTYVAmitQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cdc7b28e6.mp4?token=B7GzQxMU2uL72AeRI2gRYODa-5leIihUZAVp8pxGdtF0Fvn-A1x4lgv6jAq6e3ME7cdQEfSOYx07VYo4f5r7kwGtAUovsubOCfYn3WptIF8iDlpF4Z2ic-6zeBtuBbU_cNtFpxBGkWI-rv9OebFTQOYt9VbqfQeDOnKl1jRZmN2LC_AdBJ21C978qQjiLudQsoP3EJnrdsovs0e35b9oI_R7LLDCHOTUG9LxH_Y4UFswUoefTwwRUcjelwxHjuYiDTVl0UX42QkPfAE6IOEOpinhPTSPbO8sxlIQTFFGYqbgY2lHayQZpgZUkF2N5QPYPHMDGtrZYNWgegTYVAmitQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
❌
تصاویری از صحنهٔ گروگان‌گیری دقایقی پیش در خیابان ولیعصر تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/103332" target="_blank">📅 10:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103331">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d3e540db5.mp4?token=MXydRqRkQrhJo_2t7kx0v5Ns0vWe3oGkOaXfL3JVJ30nWJRb36yCFSzp_kLDBNAQagEhSXgxbKAr5Ci05Tk_5fMyZuIKZ8YISNEw-EbcC185D03qOdy6qGsydq2Wo_0EvMLZWqoVZBUnUDqwc5mUonsG1AJGqgYI84pZyQXWlDw9B5gvsJFKq0XvZT-oppxOPdZ8aXwhlIvlM7db5YybihdGrPJsQsj5Fkdtqat-UaW3RNzn0tRHUbNV4ym7X01AshWrz5kw4zglge0r78V6oCzQLTTRNcZvpbRzGB4CFvGm0sBP_gA-5Rh5MIXYyH5vdPXo9nQCe9EbAZvRkNNDgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d3e540db5.mp4?token=MXydRqRkQrhJo_2t7kx0v5Ns0vWe3oGkOaXfL3JVJ30nWJRb36yCFSzp_kLDBNAQagEhSXgxbKAr5Ci05Tk_5fMyZuIKZ8YISNEw-EbcC185D03qOdy6qGsydq2Wo_0EvMLZWqoVZBUnUDqwc5mUonsG1AJGqgYI84pZyQXWlDw9B5gvsJFKq0XvZT-oppxOPdZ8aXwhlIvlM7db5YybihdGrPJsQsj5Fkdtqat-UaW3RNzn0tRHUbNV4ym7X01AshWrz5kw4zglge0r78V6oCzQLTTRNcZvpbRzGB4CFvGm0sBP_gA-5Rh5MIXYyH5vdPXo9nQCe9EbAZvRkNNDgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
چرا همسرت همیشه صورتشو میپوشونه؟
🎙
عثمان دمبله: همسر من یک زن بسیار مذهبیه، پوشوندن صورت تو اسلام اجباری نیست، اما اون واقعا بهش پایبنده گاهی بهش میگم که حداقل صورتتو تو جمع نشون بده، اما اون همیشه به من میگه: عثمان من میخوام فقط تو صورت من رو ببینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/103331" target="_blank">📅 10:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103330">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YovHjvjDzXCRIYspgEhEGa5h6shyw6GnXu6FM2TFvjR-5HCyehX1i4slngrEsxRD_sQiunU5vlcOYef_45zh_nq0BMXdFRRVpQjqhviWpRFgtJHy_Dw4nBG_1xgsHyIZ6fuSOzX27O--hHgd_JntOH6TtubEjDD7F9KhIuwNBPPor3rHvpPSt4KDzJTbIjGoJo-idTVBk0k_de6Z_E86d9jpcoUzCLlGTPYS77KL7dNYXWyjbp-CNhGCckCxqjaZQk5-LQaMyOe6xDJgiTJQ2hroKws4DFVNv4rCQj-lq1Yckq1q64RL7TbaMz2WPDMOzVyssyo2LjB4ahCn5_VUGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🗞
کوپه: ولاهوویچ می‌خواد به بارسلونا بیاد اما دکو و فلیک اعتقادی به او ندارن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/103330" target="_blank">📅 10:12 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103329">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/Futball180TV/103329" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
👑
امکان شارژ و برداشت با کارت بانکی
⚠️
برای ورود فیلترشکن روشن کرده روی کانادا یا سنگاپور یا آلمان و ....
📢
😀
Telegram Channel
👇
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/103329" target="_blank">📅 10:12 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103328">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGupVjJGMuRQrEyiPekX36jgidDgOIo6xfglFSDQ0h9sqBQuqQVnAtyweOVV8BVy-Xy8IvSyTTJtMsrQinrwO4fCjs_pw4YnEB0t3cSiZmjiaBVILCfnHXPOD9kjEpKjOwE5prznT5NwY_jYuwKIwY7ZDvQfq91hlsVM4Rs0mmB88sksJbzcBzTbFTVhgmmNyEgjM5ZEMODXlOng6LkjmjWbcoGsEA6veCQNiS9eDL1Xfq9t1rWqFgcrTjuUFjXtUMMudtMJOd51UBre2EBRTSZwqfE0mttGwhdjVvsFbGWegPTQREZPEfC5oJjuVKf3IS3GqTFMCU-Yi6r6GgYTaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
میخوای مسابقات فوتبال پیش بینی کنی؟!
🥇
پس نیاز داری به یه سایت بین المللی و معتبر
🥇
⛔
دربی بت
همون انتخاب  100%
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
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠
️
برای دانلود اپلکیشن کلیک کنید
👉
r20
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/103328" target="_blank">📅 10:12 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103327">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgZhv30MsOAkEEEQCG99S46GHdEAIQWOX5Dt0esVIK65VQrUpBt2_V3VIREahuercTg1st8YlNte4_dVg-g1dr_etJvj4NyKUOetSKEvo-Tddxij_N2q2NhbHGCvEKZVvty7_vkokHG94kiQhQ0rGOVcdpe0sugh6LziOYWeAIkcHFoRcjuKjFzAfYYoL3IQYTdYBnrCWN2bVuKcRQg85ufsW1BvR0rAE1SuEvXv2wVCA4_erfINDsA122TdkI2ot98RjBC9kji-iF7RCBvjlxlkkOQrKx_WZ3GA7PSjE7FkmfGnR6f7X-noHMNHLZBZUN_8y4I232QemGyE0QEF0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔺
دیاریو اسپورت:
بارسلونا اقدام برای جذب لائوتارو مارتینز رو تکذیب کرده و گفته در حال حاضر لائوتارو گزینه جایگزین خولیان آلوارز نیست و باشگاه اصلا روی جذب او کار نمیکنه و گزینه‌های دیگری مدنظر هستن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/103327" target="_blank">📅 09:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103326">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54347f49a9.mp4?token=aY069K8wvRyQxb-Jp_YUPu7MBU_T0W82umY1xhovvAWhEXLWa3q33Ssv1vT2xI3jTAYbxIEDrtzzLsACf3xXqg2je6eJ6Lm71_La_9wcPvIFl0AE1B4mN_jSQdA0CkgbzQosxFhHTVNwPqOX0xXyDAX7BupGSEFNCTyPHQllK2NusTBhyFsujTqXhKKXyORGoheKOEwolww5ifbSpSwWBUomIY14aCpo2pq4P73IFna9v6YbGhx_JIvMVqLGWNN9p4-TrMvpZbghT2SjSoQp_PJhXv3tw6-1hoZTsOvF8doWFbtHxftnHtRq9XwkjTLqXFEcmSVdvKfglk3dkMrHwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54347f49a9.mp4?token=aY069K8wvRyQxb-Jp_YUPu7MBU_T0W82umY1xhovvAWhEXLWa3q33Ssv1vT2xI3jTAYbxIEDrtzzLsACf3xXqg2je6eJ6Lm71_La_9wcPvIFl0AE1B4mN_jSQdA0CkgbzQosxFhHTVNwPqOX0xXyDAX7BupGSEFNCTyPHQllK2NusTBhyFsujTqXhKKXyORGoheKOEwolww5ifbSpSwWBUomIY14aCpo2pq4P73IFna9v6YbGhx_JIvMVqLGWNN9p4-TrMvpZbghT2SjSoQp_PJhXv3tw6-1hoZTsOvF8doWFbtHxftnHtRq9XwkjTLqXFEcmSVdvKfglk3dkMrHwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
😐
😐
سقوط آزاد جرارد پیکه تو مراسم فوتبالی که دیشب دعوت شده بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/103326" target="_blank">📅 09:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103325">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XATEdCgjFt5T5YipB_HrbkLXma-N25xQ-cSwAO_UNwP25l5wtpfh1Korn_y2cAEgB3rxRHmLjMoppgv0UTCYFhpbEo6xqjhAJPYNzuVNJCKp-W8G9Ezp2VfgrSopuPkltxUeWGmnZA2Yoy2EQpKGOL8aIOVo44Z2p_-m8qEwP1CZpurvNRO-hyUDQh0Kpx_6xInML9MCcRPxEH9YEn0K9RYfMv6_Zif4tUfl5mGeSQdqWtVqGymbER0v402-GAbsWVJIgMQ6p-f54RHMYT6Go0LX_156Wjjao5qPpkiWBkFqjsnko3m7jpqBh5dD1KeI6-7t1GDQG2Y4B00HNPuhuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
در ژانویه ۲۰۲۵، بالای لوگوی پاری‌سن‌ژرمن هیچ ستاره‌ای نبود... اما حالا دو ستاره روی لوگوی باشگاه دیده میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/103325" target="_blank">📅 09:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103324">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3hug-1SJCk9zkpNUbDq49Ir3r_TtgP6Raf4wXNzAGHldj-rIGvqu_WTelxCwxAtDwIlXuohGzq5YLgRNLk7vcOrteFbt8Twq559G6RforjR20u7fDAYIcM7qp9yDCE0NtI2leBan5fO740RWUlLatiuN8JfZQBFXtP5vz13xW7O5FaFXKQFk1RhUoLuPfS6erddcQ6xLW6pBzrv2b1t2M9_2nrgR1td1sjWGwJCGyXnxJroExNJ9bZJDHJw_1_I2BbM_KNC6MDlceRSohlsoMsej9ptB_89QPGWGMB7THT4czqUU35oFyFoH_wsLTc4DMilvDtviKIJdZParXoiNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
اسامی داوران هفته‌اول پریمیرلیگ ایران
🔵
استقلال - مس‌شهربابک/موعود بنیادی‌فر
🟡
سپاهان - چادرملو اردکان/امیر عرب‌براقی
🔴
پرسپولیس - شمس‌آذر/بیژن حیدری
🔴
تراکتور - پیکان/کوپال ناظمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/103324" target="_blank">📅 09:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103323">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPLEvNcPuTKZghqE7_nI409Xl6eQdJ9qQ4epyCnzylldxjQjutGHjCGJmrfL0LcR-pHV5vlxieoa3mOgmtqHPanPxSczNJK-twurNJzaoA03uXlX-1xCvRfz1fiBhQP0sTUM_jEK-ltZQg-mWmOcz8ve19-1KBhkR491dO_YlJ9pb3eS30BMQEBas9b2krc5642KB6-14SiHAIZHgju0_TbrVrpX43y33gxPmZHXNHCDGSaB0fPBwbi-bXH6cmkrbxgu-CZXmb8TZ38o0ztyTHT2qe61emPZpLDSGxpzBpRKgBsKwYd7FQqRHTOV4ULIVI9IhCHdcCjifmDOig02QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
گلت تو فینال جام جهانی؟
🎙
فران تورس:
من 99 بار از 100 بار توپو بیرون میزدم ولی چشم ‌49 میلیون انسان به من بود و باید گل میکردم‌.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/103323" target="_blank">📅 09:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103322">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbfNON912o-xvns0VyuG1jVrnYRABlOlK9IHAS1412iTjoBntaH6XeG5pAn5b8dTQpOM2ygN-UXXQPBKRClMRQlufDmhcOeB5DN7Q6PMtU8n91j0ZHl-GRmjKqPZfuTvr82wXBEvwpsdiPOMIJPYTqhlXC8yl-kteZgCSvewTYxy-VkbvJvMTxhgPD1n_0cUiKfSJHD-4Im6eTotpcS76V_pCMngDeC9ucNC1R6vS79TE3fddOJriWNWWsajmkYWyS423qLsEiaBQJQt-dv6Q9QLIRM_IKiknTt9k7HCA8wgd3V78mP035WEWcTMFZOwblo9NwyW4e4zGUSTTJd-hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
❌
پائولو مالدینی توضیح داد چرا پپ گواردیولا پیشنهاد هدایت تیم ملی ایتالیا را رد کرد:
مالدینی تاکید کرد که موضوع اصلا پول نبود؛ پپ بعد از سال‌های پرفشار و دیوانه‌وار حضور در لیگ برتر انگلیس، فقط احساس میکرد به استراحت نیاز داره و به همین دلیل پیشنهاد ایتالیا رو نپذیرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/103322" target="_blank">📅 08:56 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103320">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KtDBf-fGS2KFfIdaqR7pge0cux3w7xTEhq_hjlgnY1vINO9E0Aex7M7wf_rw8vn2j4KM3sg2BD7hZ6iaGV1Eqmk85nJzltJOt4PML6XZdflMBjQTZg61LyrouhO0_z9wtSzEgSGciEpBgXbvmKpEE5JE3bU_UuzTNz-2f_hNxtJlN70jcj8fWt7fHKadjASNg3qzW3PkhPyJMika6N9J8_mG4KVrA-ubh51vZt5299xN5ngvLyLwsf4h2ZSt1QHKZ-frRRrC1gEBlo_nAzOlEFkJLAALhTBxSQYIo-Kv6pukmniO2fK-CQV1eGW2r_DiYv4Fi828M4IjTQnAGwQHOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ewaOXQZ_OX8e26rRwoiArpo5UH0uwKx--vEhFmustJKoPm_kSDVlrPmH_H6Y6Vv147S7mgQhiUxavebXvHgm4X1DdDijtbUZzXptxL2Ec2UeO8L7arE1UW6wYJVWrVq5uB1CbvhHF_TiGCqj-SEtNThkdLdKaVv7AIZNd9aVvh6CHcH1YdHmwMJo4fu9g6_9WH7oojDDqlJ60zp3lM7aTYCUCVOyKrgqe_R4iudSLu_f9rqs5JQOcUFmh2hmtr4Uhht7BD3HRyIofTldeXbioMml_NEtf_Vu8DRsN9kg4A_54afin-11Ts2YkBIxs1n_Rvgmq15ryOGCztNv16H7sA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚫️
⚪️
کریستیانو رونالدو فقط طی ۵ ماه در هر دو باشگاه، هم آقای گل رئال مادرید شد و هم یوونتوس.
🔺
۲۸ گل برای رئال مادرید
🔺
۱۶ گل برای یوونتوس
فقط توی ۵ ماه حضور در هر تیم، بهترین گلزن اون تیم شد.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/103320" target="_blank">📅 08:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103319">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1nLx3RzdQjLbOyUlFNlPgjrSU-hLdXq_dVeUpiXIGkxxww6-qatn4ylHdf4Jbn_e0fYfAhcQtP_aW0RPNdzCA38RJy2zuvBe7GgI016FXeJPb-wnMyXBnW0vfUPu01SBN13HLQoYA5sayz1q9mNsTdi1-x2EvAM4aF4lMLr7Crub3AXS0Pw46HObPA_Bh9EedgN4Ur7e5XmL0LB5gHoQJFbEPJ70d-tOAhPv5WCT3OzxIMEnWEPYtZrhKKnLPIrGSfntroakksXAl9OAnQL7E-kCjUFN8GsEmSrDdoTwDxC5Doh3Xv0aaZyNIpkZj_n6RmkMqH4_Tb1Dtsmf_arWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
⚽️
ترامپ:
فدراسیون بین‌المللی فوتبال (فیفا) مرتکب یک اشتباه بزرگ خواهد شد اگر به هر دلیلی، به فکر جایگزینی رئیس، جیانی اینفانتینو، بیفتد. او فوق‌العاده است. او به تازگی موفق‌ترین جام جهانی تاریخ را، برای چهارمین بار، برگزار کرده است. اگر او برود، دیگر موفق یا سودآور نخواهد بود. از توجه شما به این موضوع سپاسگزارم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/103319" target="_blank">📅 08:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103318">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-qq2MkViB9XND40kbUy2ImebWWaEZKkZiecwQN-arZn34s-O7J5u-5e0Jd2GKwJfageFwzYgzUSy2SjchYVKdZny_gluR0pkFL5qPaZFhjGrCdOF6YETVLhyTjSjloXRsjhSRGbWMiYwTlwVFn5mP__xYUjdx1FCQCy1ocJmEtpJq45n39tVvv3sEJOKmFGEaefnzvof_L8CbsAn0NTb4uQnnYe3GtpaO35b1UcHyfv529Hd98hmBq4HdZDmmWzPdGLX26jwYcKYUAYsqK68AwsgzAgy92DfHQstSZzUzCp8UcPj3UkvGSYqEE5aZiksjkhUF_-dLjm4tlX4TiI0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
شایعاتی درباره رابطه لامین یامال با کِلی ریالس کونئو، مدل ۲۸ ساله کلمبیایی، در شبکه‌های اجتماعی منتشر شده، اما تا این لحظه هیچ عکس یا ویدیوی مشترکی از این دو کنارهم منتشر نشده و نه یامال و نه کلی ریالس این شایعه رو تایید یا تکذیب نکردن؛ تنها نکته‌ای که توجه کاربران رو جلب کرده، دیده نشدن اینس گارسیا، پارتنر یامال، در تعطیلات او در کلمبیاست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/103318" target="_blank">📅 08:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103317">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BSqgBwpcMqjQmZRL_hyzagz4BZ77ISHeMFi6wD08pSnZb158IJn6mVuQnIwP0H6mXqaV9OkNSOV3nPwMGL9BChaVFj7gVUuFrqzYIvbU3bdjOBKxQrxae_x3ahhnmVGD0WC546Z3Pnhj28pBUSy3DDc7c5hIraVVtN74C_6kikCRIvdXvcw9qGr1Ri0yzwNlQ9DT4epAxeTY7wjo-E7cN3L_dzAPHhGBYLeNdP9r2UzPHXCcuFCpk0-AW232YnPWXHGkV4TNdBBiuBRqYGHTVwiXX2NTmMu7YVxcVR4DulOlFBC3cwfU2UiKiNZI-EYNpmzJN4Y2f6pU7NZOBp_2tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
مارکا:
باشگاه رئال مادرید واسه فده والورده پیشنهاد دریافت کرد. اما خود والورده حتی حاضر نشد هیچ گزینه یا پیشنهادی رو بررسی کنه و از همون اول تصمیمش این بود که در رئال مادرید بمونه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/103317" target="_blank">📅 08:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103316">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49775a0c61.mp4?token=axWxg1_jN4LR10fkHX7-HeuO3WZyzZOudNQx7KJ4_HyVuUUJVjtcottLfXaeGwnF-FI6JoR9c4_K5qjpJzR4daQSDWiGZ2Nv6YA5HyLMsWmJhPQJR4VI8Cmf9TCLpBlrt1LWjF-NS3MF6Ipt_BevnvZ7NmxD03ARuP_s5hKyNC27eRs6CLeKJeIxS4mwOOn1HGU1FQZe1Ik-iKTRLGTkWHl3oAH0sW0fAVBKk0ZjIuBRTy5-Vh2BlXEs-xRX8RACHoGL1dGPSjOUZqtfpzOEQ9NQBfHFJ4o2zOe9A5tqdUuaMRv7G-dsM3pnbAa2sPnXpD88XCoeiL_OqJlILgY8FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49775a0c61.mp4?token=axWxg1_jN4LR10fkHX7-HeuO3WZyzZOudNQx7KJ4_HyVuUUJVjtcottLfXaeGwnF-FI6JoR9c4_K5qjpJzR4daQSDWiGZ2Nv6YA5HyLMsWmJhPQJR4VI8Cmf9TCLpBlrt1LWjF-NS3MF6Ipt_BevnvZ7NmxD03ARuP_s5hKyNC27eRs6CLeKJeIxS4mwOOn1HGU1FQZe1Ik-iKTRLGTkWHl3oAH0sW0fAVBKk0ZjIuBRTy5-Vh2BlXEs-xRX8RACHoGL1dGPSjOUZqtfpzOEQ9NQBfHFJ4o2zOe9A5tqdUuaMRv7G-dsM3pnbAa2sPnXpD88XCoeiL_OqJlILgY8FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
✅
⚽️
رامین رضاییان: ما هم بلدیم تیپ های خاکی بزنیم به خدا ما هم بچه روستاییم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/103316" target="_blank">📅 02:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103315">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eedc94ace.mp4?token=ratzsIuRJraVwCPnfU3lsuIl326Q4oFJHoEkoP3PMnwBYCfo5hgFsWNQv-hT-m8mnN6q2GnuSH3oA5bqcLQI6e9HWfmgBmqzmrvovjhcEs6PFC37rZn8xWHMdKd3ZQnRrrm5y-qELlb2N1evuI17_DFy-G2xad2pIeQ8JKvP3VfCRKoQ38AVCjhTMrG6jTFUYBtvKIEin2vemMzOaWovh9qQOBRVWLS_M7e7DIid6589AMiVXeyMw7qOn0TyGkN_cxtRm95guD1gBf8shu0HyHpQF-p24NWB6OYlnn5FsEeIbehiK13rgNWTwOoOmWg4lbZeHXWhlazXZcBtWGo3ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eedc94ace.mp4?token=ratzsIuRJraVwCPnfU3lsuIl326Q4oFJHoEkoP3PMnwBYCfo5hgFsWNQv-hT-m8mnN6q2GnuSH3oA5bqcLQI6e9HWfmgBmqzmrvovjhcEs6PFC37rZn8xWHMdKd3ZQnRrrm5y-qELlb2N1evuI17_DFy-G2xad2pIeQ8JKvP3VfCRKoQ38AVCjhTMrG6jTFUYBtvKIEin2vemMzOaWovh9qQOBRVWLS_M7e7DIid6589AMiVXeyMw7qOn0TyGkN_cxtRm95guD1gBf8shu0HyHpQF-p24NWB6OYlnn5FsEeIbehiK13rgNWTwOoOmWg4lbZeHXWhlazXZcBtWGo3ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
👤
رامین رضاییان: مذاکره با کادیز اسپانیا؟ صحبت هایی بوده است/  در 48 ساعت آینده تیم  جدیدم را مشخص خواهم کرد. خودم دوست دارم در ایران و هیاهوی فوتبال ایران باشم تا مردم از هیجان رامین استفاده کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/103315" target="_blank">📅 02:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103314">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❗️
▶️
👤
صحبت‌های شنیدنی و تلخ این جانباز عزیز؛ امیدواریم برسه دست اسطوره علی‌آقادایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/103314" target="_blank">📅 02:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103313">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/103313" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
a19
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/103313" target="_blank">📅 02:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103312">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/axcFtVALYu79yaiLCxTHnZFy7NrQSdYDBAwG9NaPvOF8UixPweJB_4gec3Ll3ssRvpkMJga8keVkDbC6bJXUOO9iEIH9tenhQSrb5YgEmnAwxaDj4Audt1jY3qI7188K8Rs2LhN9miY98ZpbbR8y54Mfrd1ouw6dZw_8isDo_fLz3KH2vJwuQ0TKddTfzSPHczVw9P3ZZGc6OqYrOOSG1BIQkq4cRJxiN79ZObxBeaUWufK00GeczKTPN7oJK_rwpweJ10ynAFhGzKjuei_Z-JX7iQ9tYoQdGwws_cW-vL5gFK_PUiLZspfnEpsvtJUwnioAYCtVDwG-cR7ufRpSQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
a19
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/103312" target="_blank">📅 02:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103311">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9e8aa4ed3.mp4?token=P42nBBsJEsK7jmuif7v5IwYt07k9ixG-fslMjzHAmO7lMbhH-0dDBbvuEPb2KZwB0psFtKo21DwI3XQWn4aSXd2ux8pV2DETug0f0d9cb4VouM_5gD0GyhpzCFQ41QGMpVM54bzp66ioSmnuxGU2_Gmclz4cSBScYmJoARkF9xUItLBKCzkA3Qo5rFMaLgJ9HJJNknLMujsnoHn7oB7E0UTFR7bcbHdtoxJoXaFr67hG7WylP_9EZHEntODx-UmicwMzOEpudXXDGjOt77ioYtomlRbgMmdTivJVoYo14xrdM_cFp3VpvJZZUvdMJqsqVCztxHPkBTALWI-prLVMXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9e8aa4ed3.mp4?token=P42nBBsJEsK7jmuif7v5IwYt07k9ixG-fslMjzHAmO7lMbhH-0dDBbvuEPb2KZwB0psFtKo21DwI3XQWn4aSXd2ux8pV2DETug0f0d9cb4VouM_5gD0GyhpzCFQ41QGMpVM54bzp66ioSmnuxGU2_Gmclz4cSBScYmJoARkF9xUItLBKCzkA3Qo5rFMaLgJ9HJJNknLMujsnoHn7oB7E0UTFR7bcbHdtoxJoXaFr67hG7WylP_9EZHEntODx-UmicwMzOEpudXXDGjOt77ioYtomlRbgMmdTivJVoYo14xrdM_cFp3VpvJZZUvdMJqsqVCztxHPkBTALWI-prLVMXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🎙
🔵
رامین رضاییان: مشکل با آسانی و حردانی؟ من برای یاسر آسانی آرزوی موفقیت می کنم/ من همه بازیکنان استقلال را دوست دارم. با همه بازیکنان استقلال ارتباط خوبی دارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/103311" target="_blank">📅 01:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103310">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5-9t3pM1vzIyz8opMrDgz5UHC-9J87w6mDTKu7iiYhPHe9Hpc53gfnooI19hmSEqKHOpdE1bQotxxDQRIZWhQSjX9m5yGp9Wodl1W-hi5QwYbY5-QFg7PULO-tQGtXm-Kbz944CXYZ6VnlzNkAVPHcpoxq_O0UztJ57Ouwajda1EmB3QeZbloxh5VKW9FLCt8Ln9Lsfp9Lq_Dom0Pdzm6xoMMbBmilqz_z0cm81ofo4DFsr_ukciKjjEO3tGUKKgCp84CxY3ZyXohYOhXHXvK1bSLd4Oyaw9Uu5BsguGvROjKrzA2TDPvRrGi8sPtOGND6Evh8zHkXsSIxmbGx64w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📱
استوری کنایه‌آمیز لحظاتی‌پیش یاسر آسانی با صالح حردانی، هم پست و رقیب رامین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/103310" target="_blank">📅 01:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103309">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b865ccd71.mp4?token=Q-IeXVs6wVCytKXLYpKExONTWVmDWmUdcM0gO8TTPh6WyqQ0u5RzGhRleifD1zeWKe0SGDqyKruuHmYa0Qcipmo4NVohTqO3Mds4U0ibcNDf7yQnVM_SzjqYwAtDDdu4tr7pMAzp0RIbNQTn6W0Rk8WlibgefIz7l9nsmWvJ6hhmkZlz_U2dl3yWAyRx_nbZQzuEvCTNBf9rdNxOB-WCUwFhMNrr0o6N3WV6cUwHV710Na64a4zRov9IFPJKt-s-lSdXGdw7H2ZWZJfWWXOav9bhjI1cuxYGwEADHgkgjY0TXQWtkRDU21ANess321JNJYblY-L-TEr2YrecB0tQ31MHX-kj4LXrpAa4KOlxHY9rYQBTf0Yd0VjK6Fk0FqVhezntH03di9VpW7hihj3X9iS1PyeHytTxwgR9kPa_Onh3I-30se2xPQPsepeP0X5K2ci5IP4cHBSr5WK-Yw9KZrViD6zy_d-VF6L9vH6bPQSJU62eTbcKeOR4goukh-kB6OefSEBvQFm3BQdyugO4RFoFdYnZvpRCSN0UCHPV1bBXAUmIMqWfwoh6r1Dnzkubs71Is_OeDylRAee0x_fVrXWhCydZw0DloxmqtXaFndQtCF4lOT3Vcl8FF91wqWDlZY0FK0wZZcYsSsYaG2bpsoUEJtKdL5IwqM36cTB-u6Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b865ccd71.mp4?token=Q-IeXVs6wVCytKXLYpKExONTWVmDWmUdcM0gO8TTPh6WyqQ0u5RzGhRleifD1zeWKe0SGDqyKruuHmYa0Qcipmo4NVohTqO3Mds4U0ibcNDf7yQnVM_SzjqYwAtDDdu4tr7pMAzp0RIbNQTn6W0Rk8WlibgefIz7l9nsmWvJ6hhmkZlz_U2dl3yWAyRx_nbZQzuEvCTNBf9rdNxOB-WCUwFhMNrr0o6N3WV6cUwHV710Na64a4zRov9IFPJKt-s-lSdXGdw7H2ZWZJfWWXOav9bhjI1cuxYGwEADHgkgjY0TXQWtkRDU21ANess321JNJYblY-L-TEr2YrecB0tQ31MHX-kj4LXrpAa4KOlxHY9rYQBTf0Yd0VjK6Fk0FqVhezntH03di9VpW7hihj3X9iS1PyeHytTxwgR9kPa_Onh3I-30se2xPQPsepeP0X5K2ci5IP4cHBSr5WK-Yw9KZrViD6zy_d-VF6L9vH6bPQSJU62eTbcKeOR4goukh-kB6OefSEBvQFm3BQdyugO4RFoFdYnZvpRCSN0UCHPV1bBXAUmIMqWfwoh6r1Dnzkubs71Is_OeDylRAee0x_fVrXWhCydZw0DloxmqtXaFndQtCF4lOT3Vcl8FF91wqWDlZY0FK0wZZcYsSsYaG2bpsoUEJtKdL5IwqM36cTB-u6Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
رامین رضاییان: کوچک تر از آن هستم که بخواهم بازوبند تیم استقلال را بر بازویم ببندم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/103309" target="_blank">📅 01:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103308">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e54f7dedb.mp4?token=RtOEaB4zI24HTMs_wEVTuctduBCEEW6bKRjrDVYG48CtJUBk2KJhmIhBNKVx2f2bdDysI2jSDdpkwouY61tz-xqe2PL0RtPYpmhnq8Yj9QLn3BsQxTzYOMpXUnZEEe_YrXRsQa-D22-VK17-xG34xbrJBMwcNqGc-ox2D4YVPVSkOLaBux2NEQxssNuSIeYBOuPUzf6K4mz7NMFJoQuHA9X7HiOovONxUf_XNsVuqF03BDyngkzrZB7WlfOYAUTILSBG-E2lIhc5xBnDiYvkso7HfcPwqRXPDV1K5qI0NYXsQqWD6E1erCmHvOdhe3kziKx7hh9WIyBopE2QqLwJv2m_hulA_6nL1CwL6sQ_Uj4qeauYUEGtcP10H-MzQdLozLYTJ02drvYycKe3DJApMJoM3RQJSRu4eN2wGYadkaRVzp9494CincT1hzrO8jXxZwbEnMTaO2YqpWtokXFpjHyVeVJefCwOgapvL0gNgWAXW6lRgMu57W8PtsSmb4HX-wC2Fx2bd_iaSe3VNLT2YLew3MWOQ-EpoxXPO-iQptGpoD16GQiao8boOvjwXbkJFVT4afnY15XLEMz1xzEuWjuRh8gQQpvOuGKy_hFidwY0unkXexnmETA9BrC5BtkWUvpi4IBGqrP4wy0GDiKLHpiL3Z7AVi4HXBZzKUHNdkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e54f7dedb.mp4?token=RtOEaB4zI24HTMs_wEVTuctduBCEEW6bKRjrDVYG48CtJUBk2KJhmIhBNKVx2f2bdDysI2jSDdpkwouY61tz-xqe2PL0RtPYpmhnq8Yj9QLn3BsQxTzYOMpXUnZEEe_YrXRsQa-D22-VK17-xG34xbrJBMwcNqGc-ox2D4YVPVSkOLaBux2NEQxssNuSIeYBOuPUzf6K4mz7NMFJoQuHA9X7HiOovONxUf_XNsVuqF03BDyngkzrZB7WlfOYAUTILSBG-E2lIhc5xBnDiYvkso7HfcPwqRXPDV1K5qI0NYXsQqWD6E1erCmHvOdhe3kziKx7hh9WIyBopE2QqLwJv2m_hulA_6nL1CwL6sQ_Uj4qeauYUEGtcP10H-MzQdLozLYTJ02drvYycKe3DJApMJoM3RQJSRu4eN2wGYadkaRVzp9494CincT1hzrO8jXxZwbEnMTaO2YqpWtokXFpjHyVeVJefCwOgapvL0gNgWAXW6lRgMu57W8PtsSmb4HX-wC2Fx2bd_iaSe3VNLT2YLew3MWOQ-EpoxXPO-iQptGpoD16GQiao8boOvjwXbkJFVT4afnY15XLEMz1xzEuWjuRh8gQQpvOuGKy_hFidwY0unkXexnmETA9BrC5BtkWUvpi4IBGqrP4wy0GDiKLHpiL3Z7AVi4HXBZzKUHNdkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔴
رامین رضاییان: من یک سال برای پرسپولیس رایگان بازی کردم/ برانکو من را نخواست
سالی 2.5 میلیون دلار از الدحیل گرفتم/ دو ماه حقوقم را بخشیدم به پرسپولیس بروم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/103308" target="_blank">📅 01:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103307">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/926f821e41.mp4?token=Y77CVMH3Yd8khlIbqBJQ9VQtvNowQrYko1Afcr6EjfFtNlesXa0_3fmBIN-jXKPocmQUkr23FNGTmR1kycciDJ1ivrhPhC1Z8h1Q_bSdQ0bSfKYZ1nZqaIw2a47ixZ3yf0N9SGanB0lypuK81KAA-kKkl0VgYfyIvHoPCphgZ6LAZjGGoA5Hb4dwAnCjp3ICeLevekof60D8zIQTusIBAWQAkogjEupzh8YQKNPYh2p4oVEir4kjw7z64MEgVHZHNoLoYYeJ6MWOsJNJKm0O4EiY0YPVA0jEreiLsGrXReEKXK-KT9Y6JHkZEbXDI7iAJc6qz18xDdKqFIrKLKqF7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/926f821e41.mp4?token=Y77CVMH3Yd8khlIbqBJQ9VQtvNowQrYko1Afcr6EjfFtNlesXa0_3fmBIN-jXKPocmQUkr23FNGTmR1kycciDJ1ivrhPhC1Z8h1Q_bSdQ0bSfKYZ1nZqaIw2a47ixZ3yf0N9SGanB0lypuK81KAA-kKkl0VgYfyIvHoPCphgZ6LAZjGGoA5Hb4dwAnCjp3ICeLevekof60D8zIQTusIBAWQAkogjEupzh8YQKNPYh2p4oVEir4kjw7z64MEgVHZHNoLoYYeJ6MWOsJNJKm0O4EiY0YPVA0jEreiLsGrXReEKXK-KT9Y6JHkZEbXDI7iAJc6qz18xDdKqFIrKLKqF7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
رامین رضاییان: چه کار کنم که سنم 35 سال است ولی اندازه یک بازیکن 25 ساله دوندگی دارم؟ چرا همه زوم شدید روی رامین رضاییان؟ چرا می خواهید فوتبال من را زود تمام کنید؟ چرا؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/103307" target="_blank">📅 01:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103306">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f842dcdc91.mp4?token=SE1UCEjj5UUrmzKaIRv3XyETyk2-6WZV2kSrnP87fYV9rvToyIOlhpTQ3UNkjcAx1eP-Odv_X62KRoiMJweKELHDY9iWDVXhMYuq921BsYCbTLiZEH4CJArxAclXviRHCuIQbhjcId_HY0NL-5DMOCD5QfBwMo9W-_RXcfbM2_l3W_Yxruq26zQi2bCLw56LKCKXNIdsF17DxxpvuU1i11bcM8nP4nQOlZkFb3cboGKfc6qU5eDcGZEY1ErD6vnUkwkPfVbrw2jEQ8Brg4MgWqvPR2W3sqA3KtuJvuHKnAHXkD0bY9ZBNZgeVRgRGqzdzUhWi_IFpDFLeegvJXMgWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f842dcdc91.mp4?token=SE1UCEjj5UUrmzKaIRv3XyETyk2-6WZV2kSrnP87fYV9rvToyIOlhpTQ3UNkjcAx1eP-Odv_X62KRoiMJweKELHDY9iWDVXhMYuq921BsYCbTLiZEH4CJArxAclXviRHCuIQbhjcId_HY0NL-5DMOCD5QfBwMo9W-_RXcfbM2_l3W_Yxruq26zQi2bCLw56LKCKXNIdsF17DxxpvuU1i11bcM8nP4nQOlZkFb3cboGKfc6qU5eDcGZEY1ErD6vnUkwkPfVbrw2jEQ8Brg4MgWqvPR2W3sqA3KtuJvuHKnAHXkD0bY9ZBNZgeVRgRGqzdzUhWi_IFpDFLeegvJXMgWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
رامین رضاییان: مگر می‌شود بازیکنی مثل من اخلاق نداشته باشد و 8 سال در تیم ملی باشد؟ چرا دل من را می شکنید دلم شکسته است چرا من را جلوی هواداران می گذارید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/103306" target="_blank">📅 01:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103305">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abb1415693.mp4?token=YaJ2dj7jY1JLwYFNcouj2bkmFzpscoc_sxY0lzNjNLOn-6KpPapwOY8eQ-IM9py0JrUAfNeCg3QRvPEmY-C21rq7RtOW_v7815geLTMllpMrbRiEumHhX9UDAwpvIIvoimLsCHFMdcmCDuJqUwpxaOHYiAYpn1Ls7nvDbsHPr56QNqmYOQAbdZ5YYOqPK_8q2QMo8OfcNTG5ZwOr2o-HG87QhbbV2-hwXvEY9CezboGAbhPORU6nDCOfkOq_dyOLUkVmwKzpbEiK4nlSy_Z0aynRR0oBl_XjneFlhZTlsVwDGYr-pjxY2RNDIfI1HEVbdUm3gWWbi9z36qMbtgz6DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abb1415693.mp4?token=YaJ2dj7jY1JLwYFNcouj2bkmFzpscoc_sxY0lzNjNLOn-6KpPapwOY8eQ-IM9py0JrUAfNeCg3QRvPEmY-C21rq7RtOW_v7815geLTMllpMrbRiEumHhX9UDAwpvIIvoimLsCHFMdcmCDuJqUwpxaOHYiAYpn1Ls7nvDbsHPr56QNqmYOQAbdZ5YYOqPK_8q2QMo8OfcNTG5ZwOr2o-HG87QhbbV2-hwXvEY9CezboGAbhPORU6nDCOfkOq_dyOLUkVmwKzpbEiK4nlSy_Z0aynRR0oBl_XjneFlhZTlsVwDGYr-pjxY2RNDIfI1HEVbdUm3gWWbi9z36qMbtgz6DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🙂
رامین رضاییان: روزبه چشمی 7 روز پیش با من تماس گرفت گفت چه خبر؟ گفتم هیچ کسی از باشگاه استقلال با من برای مذاکره تماس نگرفته است، روزبه گفت من شب با آقا سهراب صحبت می کنم خبرش را می دهم، هنوز که هنوز منتظر زنگ روزبه هستم
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/103305" target="_blank">📅 00:57 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103304">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/853e2a52d7.mp4?token=lXShz4okuB2x3ZXII7uPQANDTLZNaERK2CsTB7Ss_aWbYh9r07lxKM4l52HFmhYKejmAkUze0rMJF-Cs-6vfw_jC4dyt1RVo4KRmSoEDK0MxxO0ej2eg7clP-YOz4HEm5aniDKiHNe3zWlch7Fr1BVzRJk4grBUkCkb1cL5vDyoFbLtIfRINw0naFYrQ6nrkC8jkSoLr3xqOipK885xdjRScCul6Bcd3ipat5rffGLdUbXBWDows1qQZfMD8Iq8jYxNKMweHdqDLirGg9_6vuU1YeRem4e768_dGTC6N_NL8arhr8r2pNKeoLAMAssLJFhWAyPk0jI5c3VT3t8f0Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/853e2a52d7.mp4?token=lXShz4okuB2x3ZXII7uPQANDTLZNaERK2CsTB7Ss_aWbYh9r07lxKM4l52HFmhYKejmAkUze0rMJF-Cs-6vfw_jC4dyt1RVo4KRmSoEDK0MxxO0ej2eg7clP-YOz4HEm5aniDKiHNe3zWlch7Fr1BVzRJk4grBUkCkb1cL5vDyoFbLtIfRINw0naFYrQ6nrkC8jkSoLr3xqOipK885xdjRScCul6Bcd3ipat5rffGLdUbXBWDows1qQZfMD8Iq8jYxNKMweHdqDLirGg9_6vuU1YeRem4e768_dGTC6N_NL8arhr8r2pNKeoLAMAssLJFhWAyPk0jI5c3VT3t8f0Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
😐
رامین رضاییان
وسط برنامه پا شد لباسشو نشون میده میگه ببینید بخدا نه مارک نه هیچی، منم بچه کف خیابونم فقر کشیدم، ببخشید اگه یا تیپ و استایلم دلتونو شکوندم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/103304" target="_blank">📅 00:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103303">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0631b46480.mp4?token=eGfBPO3t47fhEAzuz8_w3nEzgROe1EE7x3GL-5I2P_ieQi4YInc6lvt4bKL9QGrKTPrBP83Hpg7ERIN45ZIh-4OCqICGDv1ELYJOdTW0X81fquVfHAyMeBvxqUXLdMlaWPoM5Gzb0ixVZayv_K-_qf-QZXmu6uEmh3Okcy3UoSjXbegaI6445nM7pEKBvfL4pLorHHAHJ5dUx68kKM7XV_Bes7kwok1j7GrAO22z_yKyacyVBfLvbe8DIA9pvuyFhYUFugn3QgwPdH_9alE7auXBHDDO_HsDO6yn5HPFCL5_GAa5ZIPkAnTLb7v-bEIuUNIQp_mT-Lw1wx8QG_t8sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0631b46480.mp4?token=eGfBPO3t47fhEAzuz8_w3nEzgROe1EE7x3GL-5I2P_ieQi4YInc6lvt4bKL9QGrKTPrBP83Hpg7ERIN45ZIh-4OCqICGDv1ELYJOdTW0X81fquVfHAyMeBvxqUXLdMlaWPoM5Gzb0ixVZayv_K-_qf-QZXmu6uEmh3Okcy3UoSjXbegaI6445nM7pEKBvfL4pLorHHAHJ5dUx68kKM7XV_Bes7kwok1j7GrAO22z_yKyacyVBfLvbe8DIA9pvuyFhYUFugn3QgwPdH_9alE7auXBHDDO_HsDO6yn5HPFCL5_GAa5ZIPkAnTLb7v-bEIuUNIQp_mT-Lw1wx8QG_t8sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
رامین رضاییان: من قراردادم را با استقلال فسخ نکردم؛ باشگاه استقلال با من فسخ کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/103303" target="_blank">📅 00:53 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103302">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc0b3587c2.mp4?token=Rt0jz9Km-P8b4uQoPaC5CBcOMcg-b04vpnRcUACx6HuqEjjjfzotxfKDvE3-3L-vYS9K29Kwm_iJA6g3fb8A1yyQvz9eFhI5H_rTqu28MTcDE8mAyz2YjxfqQbLj9d9aqxBfdvo9nYjJoKvNpE2UNpLX6j9jxdNYuxh8_M0TcPBDPusUHqGmlF0_o66Fa5tcSYxnphMl9dVcR0oIuHfwZtHixGsbCAyHhD4nWeoalPx-CkVKPz6tngs81ol-iBhOOzosOaatyiVcARfpWJf4naS4P8DnTxG9puiPfCbx1X4C4VDpd581iCS78wqUpqqpvx0juN5hfvzIOfAZKmPcgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc0b3587c2.mp4?token=Rt0jz9Km-P8b4uQoPaC5CBcOMcg-b04vpnRcUACx6HuqEjjjfzotxfKDvE3-3L-vYS9K29Kwm_iJA6g3fb8A1yyQvz9eFhI5H_rTqu28MTcDE8mAyz2YjxfqQbLj9d9aqxBfdvo9nYjJoKvNpE2UNpLX6j9jxdNYuxh8_M0TcPBDPusUHqGmlF0_o66Fa5tcSYxnphMl9dVcR0oIuHfwZtHixGsbCAyHhD4nWeoalPx-CkVKPz6tngs81ol-iBhOOzosOaatyiVcARfpWJf4naS4P8DnTxG9puiPfCbx1X4C4VDpd581iCS78wqUpqqpvx0juN5hfvzIOfAZKmPcgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
رامین رضاییان: آقای تاجرنیا با وکیل من صحبت کرد و گفت من رامین را دوست دارم ولی..
میثاقی: ولی سرمربی استقلال رامین رضاییان را نمی خواهد
رضاییان: خب این را نمی توانستید تلفنی به من بگویید؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/103302" target="_blank">📅 00:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103301">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66453415a0.mp4?token=MdUscSalQsgMWoerbbVpjZEbyQxnGpiaG3B9dy1M68jrGURnvlwkAp1bE20KQAIFTHODhEGNmY7vE_iiUXwlmBAycecg1x9q-89a_5U4qZdEX3MSsY_EqCVJLcqCVwp0lYixlW4HRrYRviGT9xzymmAfgk3L5hpPDVpmgLmdQpKw0cEYvxOwt7OJAZ051QsHbfzJ6uSzhSIdD_u0cC6tj2R1dLzfat7xiw4UjiE95Om3MhE4_DHD6vJotSM7Bm_E8gKXcz_B4F_AaTVjbfyjyT6k5GqoKPV7TX72CddxVR82wiE0ren2EqRTytU9z5SfgBD5w4OKpxY_asJ8AdGLZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66453415a0.mp4?token=MdUscSalQsgMWoerbbVpjZEbyQxnGpiaG3B9dy1M68jrGURnvlwkAp1bE20KQAIFTHODhEGNmY7vE_iiUXwlmBAycecg1x9q-89a_5U4qZdEX3MSsY_EqCVJLcqCVwp0lYixlW4HRrYRviGT9xzymmAfgk3L5hpPDVpmgLmdQpKw0cEYvxOwt7OJAZ051QsHbfzJ6uSzhSIdD_u0cC6tj2R1dLzfat7xiw4UjiE95Om3MhE4_DHD6vJotSM7Bm_E8gKXcz_B4F_AaTVjbfyjyT6k5GqoKPV7TX72CddxVR82wiE0ren2EqRTytU9z5SfgBD5w4OKpxY_asJ8AdGLZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🟠
🔵
رامین رضاییان: رفتنم به جام جهانی را مدیون باشگاه فولاد هستم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/103301" target="_blank">📅 00:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103300">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c728b778f4.mp4?token=DvDMHrFIBXiWOGI0fDlXfRshFJKt5j5z011G9kIge_MRpuE7fKpGQ95a1SXnwv0r7POP5UpO53c0EP0V9-qhkdt6n36uSvhinTTKjz1JcH2m81wbAvp52EjJZ7O6Cz8n0EsK1PvFmyvJNFA5q_CGbWxVgqcH07AP1M2ehT6JoStcXH6G8jVQjKg0uX4nGEEHdgfgE7KdPN6ojTPLS04tWm846yJWPQRp1IhjkebVeYWkt4MMh6O3BIgTIS0_BYXlavkRMfSO_UHPurw_ZJMXTVm9b2PHfa_pbEjGSXIPfJY9l7Ud8eqKB10P623bmUI_KiGT-tjrurNfPC37_6FwhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c728b778f4.mp4?token=DvDMHrFIBXiWOGI0fDlXfRshFJKt5j5z011G9kIge_MRpuE7fKpGQ95a1SXnwv0r7POP5UpO53c0EP0V9-qhkdt6n36uSvhinTTKjz1JcH2m81wbAvp52EjJZ7O6Cz8n0EsK1PvFmyvJNFA5q_CGbWxVgqcH07AP1M2ehT6JoStcXH6G8jVQjKg0uX4nGEEHdgfgE7KdPN6ojTPLS04tWm846yJWPQRp1IhjkebVeYWkt4MMh6O3BIgTIS0_BYXlavkRMfSO_UHPurw_ZJMXTVm9b2PHfa_pbEjGSXIPfJY9l7Ud8eqKB10P623bmUI_KiGT-tjrurNfPC37_6FwhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺
🟠
رامین رضاییان: آقای گرشاسبی مدیرعامل فولاد برای جذب من با پای خودش به باشگاه استقلال آمد شاید هیچ مدیری این کارا را نمی کر
د
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/103300" target="_blank">📅 00:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103299">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKc2HT2EyMfX-GmsPmNLYYye59WmOoOS3lIIVbYuK_WLhYwJ2tczmStmpCnTNUTCSG_9fK5HyYWRMsEoN9wV5MHyUaIj9bPF7YJI2tJfiOBknHpDwObtN-er3u558wpgrEgi4VXlQZqO160Cw8C-FhfBq-pQclz29IWyqVkdbrui4keSAYX7aK8yAQYgbDEcGlXLTDizTmUhtF50SAaZME-76dmlkbjJ4g1DaL84_NvJLwPcMX13PtkZ4xb9zigedEiYPgRfIJx6EByBXpwBqa778bnfpORb5jFvscCrSKGGkbr25h7GZzqT1RkxL-M7EAoe8A6A9D5qHh6Na7ovvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔵
#فوووووری
؛
🔺
هلدینگ‌خلیج‌فارس اعلام کرد که سهام باشگاه استقلال بزودی به چند شرکت یا شخص متمول هوادار آبی‌ها به فروش خواهد رسید. مذاکرات در این زمینه آغاز شده و بزودی نتیجه نهایی به مردم اطلاع‌رسانی می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/103299" target="_blank">📅 00:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103298">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e9ef8ef85.mp4?token=UtJCIlEVlALKYtOoXcCGGla3ObOJ2t4DV2i3O5gnwkeB3XUwCvimpEEy3T4lgtrYoRfOkBTREbJm7bzH_3bt31nBctb4SbI1_u1CauBpj1qCGKTzAeVoPGXOekdaBQ2Oa8GhsI4qphJQ0Dk_jSgVY6ZUL2N7td2k6m9jF346har5yDqwf0wUADQ0J76Yl4-VjwDnr2ilxUvvq9R9jBA1MKdyatXIBvrDsBXEewnK410yq9x4uiPdGzuiQN_ypPIGsscvWgDlIGcmym3huc5MI9DMmPek3kzY09cfGO7Dk8B5LEIpgHjG4Q0tBqggSaX4zip3o2sIwNi2pl-rj-zbug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e9ef8ef85.mp4?token=UtJCIlEVlALKYtOoXcCGGla3ObOJ2t4DV2i3O5gnwkeB3XUwCvimpEEy3T4lgtrYoRfOkBTREbJm7bzH_3bt31nBctb4SbI1_u1CauBpj1qCGKTzAeVoPGXOekdaBQ2Oa8GhsI4qphJQ0Dk_jSgVY6ZUL2N7td2k6m9jF346har5yDqwf0wUADQ0J76Yl4-VjwDnr2ilxUvvq9R9jBA1MKdyatXIBvrDsBXEewnK410yq9x4uiPdGzuiQN_ypPIGsscvWgDlIGcmym3huc5MI9DMmPek3kzY09cfGO7Dk8B5LEIpgHjG4Q0tBqggSaX4zip3o2sIwNi2pl-rj-zbug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
✅
رامین رضاییان: با جان و دل برای استقلال زحمت کشیدم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/103298" target="_blank">📅 00:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103297">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcad8628a9.mp4?token=u9Chgm2swyxi8whzxp3xqVz75jKgKOfzzqXiSTmTJvfpk28AgBqTnDnv-EIjtkShRtc9XMWBJMAiZ2uPhs1gFV3SXKjrFsYP-HvXIgYDNWyitFnIkvSlRhnX8Ki5_rne3dluDV9cRJHLEGFISCc1jq5WvtPgKZwJoDpqdu02Q1ASJYZTy4uhro-QmPiS_AOpV80-Nd5m24c3gC0azl52MpieQAhj-6RP8-ZZqFvVBGe8aDdFHMQcwGiiK3mbHHTXfYTpuxQcc686h5ZFFFcIXyFg4hx27GlExPrclWZHI2TksnwVIcLWrsYXpf3379I6gA7rSR_-CVi3r35BDZCj4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcad8628a9.mp4?token=u9Chgm2swyxi8whzxp3xqVz75jKgKOfzzqXiSTmTJvfpk28AgBqTnDnv-EIjtkShRtc9XMWBJMAiZ2uPhs1gFV3SXKjrFsYP-HvXIgYDNWyitFnIkvSlRhnX8Ki5_rne3dluDV9cRJHLEGFISCc1jq5WvtPgKZwJoDpqdu02Q1ASJYZTy4uhro-QmPiS_AOpV80-Nd5m24c3gC0azl52MpieQAhj-6RP8-ZZqFvVBGe8aDdFHMQcwGiiK3mbHHTXfYTpuxQcc686h5ZFFFcIXyFg4hx27GlExPrclWZHI2TksnwVIcLWrsYXpf3379I6gA7rSR_-CVi3r35BDZCj4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
🔵
رامین رضاییان: در استقلال تنها ترین بودم. ساپینتو سر تمرین راهم نمیداد به همین دلیل در خیابان تمرین می کردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/103297" target="_blank">📅 00:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103296">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08091e808e.mp4?token=r-BQJwjjZREXaNfoehGaahB-ClS_VBCAXwtI9dRxnKizV2eoK7GqJ8wrQLj_fSCdAX-iSfAMgjHtqEMCabtayIcNh5lDpXfBjty6q8yC6ZWF9YdPJSMhhs-_wv6VElUqfyO3bkgTPEPZpAKi5PQC8WMVcBDw2YViAyiSgs6ZJLcncZwqRQJ_w0_S5_Wn4xwkiX9wjmagBqLTMI_zvr61VcGvhZwb6oAzlbFKYkXtGb4_c2UJFqqITi7Sr-v-u1I6hqJz9G8NS-QxKIL9Ce8nMffkmYvhxntDF6XX6_LA92A43hj-q1ibeKcNfohfGO9YsYtkLvlSrnuJfGVgRvVkdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08091e808e.mp4?token=r-BQJwjjZREXaNfoehGaahB-ClS_VBCAXwtI9dRxnKizV2eoK7GqJ8wrQLj_fSCdAX-iSfAMgjHtqEMCabtayIcNh5lDpXfBjty6q8yC6ZWF9YdPJSMhhs-_wv6VElUqfyO3bkgTPEPZpAKi5PQC8WMVcBDw2YViAyiSgs6ZJLcncZwqRQJ_w0_S5_Wn4xwkiX9wjmagBqLTMI_zvr61VcGvhZwb6oAzlbFKYkXtGb4_c2UJFqqITi7Sr-v-u1I6hqJz9G8NS-QxKIL9Ce8nMffkmYvhxntDF6XX6_LA92A43hj-q1ibeKcNfohfGO9YsYtkLvlSrnuJfGVgRvVkdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
🔵
رامین رضاییان:
🔺
واقعا استقلال برای من یک تیم ملی بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/103296" target="_blank">📅 23:52 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103295">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18ddc57b23.mp4?token=XlmsKv3nJy3NfDe0UqSIMYQzf6BrgS8c_1BP6TMMY3tF5SdtRQ3T7-rgS8xZFGkvmn5H38GT4KN8T987GkkHrN43tAlP-ebVZ_V0aEX74z7CbKFSFey-HPrh_9HGIIx5vQjwfxSmxiR-KPgA5auZKebShtPpzfWPqqb8XGeKZeY9mLcsOfmhXRAZY6z4extxznrVz7jtBTncd7k5LxyuQvsngmhvzW76O-ZBBo90hdsfu-fq_Q0gAq6ZZgo66VSWA7vUwa357jWzV5W60ZXP7IT4O7C1cfmbpj-v1Faqf0gznRLwCeYpz953flMrikH6yN8Gbc-DZmyThGoj8pcXwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18ddc57b23.mp4?token=XlmsKv3nJy3NfDe0UqSIMYQzf6BrgS8c_1BP6TMMY3tF5SdtRQ3T7-rgS8xZFGkvmn5H38GT4KN8T987GkkHrN43tAlP-ebVZ_V0aEX74z7CbKFSFey-HPrh_9HGIIx5vQjwfxSmxiR-KPgA5auZKebShtPpzfWPqqb8XGeKZeY9mLcsOfmhXRAZY6z4extxznrVz7jtBTncd7k5LxyuQvsngmhvzW76O-ZBBo90hdsfu-fq_Q0gAq6ZZgo66VSWA7vUwa357jWzV5W60ZXP7IT4O7C1cfmbpj-v1Faqf0gznRLwCeYpz953flMrikH6yN8Gbc-DZmyThGoj8pcXwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
🔵
رامین رضاییان: وقتی به استقلال آمدم به شرافتم قسم خوردم که با تمام وجود بازی خواهم کرد و خواهم جنگید/ واقعا تا زمانی که در استقلال بودم هم جنگیدم هم بیرون از زمین تعصب این تیم را داشتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/103295" target="_blank">📅 23:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103294">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKTyagBJx0r1mTSlhVmz4-0LCyfbRAKSqtEI66GqkfBWf-ayPD-xd9QlIXECyP5vtfiKbxJyTbezaaN_QF_Xzcn9-xhQNvpS-FT2Q_REdl4-_jKJeiKacrGFK-29iOGSxjHvjEmQ3LMPoI8EextfPSpa0AxpGU--t3IfPq2Lz_E7ffSA7Pah7pJKGKTkm9ZMKR0WU8GdCUnpibF2O1FMapcMGWYcKJK5kgJ_8dQWPVqteFpS7QhSItRDiYz8B2L96VPYKg1c7p2FosjKR0ZAwOzDbTb5ZCN34bKwSRww94xtWz8b0bnJcT5GjV7vN_uSZKoLoFB4FIcFqVMo5tpfmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚪️
🔺
خوزه فلیکس دیاز: اندریک در رئال ماندگار شد و جدا نمیشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/103294" target="_blank">📅 23:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103293">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a29c3e62b2.mp4?token=XSzb0Td94YUp_gewk0BYwsGHTRMkOdTTrps7tm__xzfTdeK-swqM2gEndUerKIzXgyN4fFfXDlo-5NXAXt1wxXcyfjbKWoeqFINCBj_AfZs4LyRODW7dq21wBWhvaKmnXTNHHoBBlIGLMmFKJAatiUB8wQ0tQMyjY87QWMZCTPa7EDX_raFWmTVgLFZv8XtIz-Imx2kCHf9Sa-HEPth4nh4M_XfXbhxDlYa978SjjFnaXl5mxpbpY8bss8Dq_yEmi-MxUhYpy5lpPmbUOrS1GUJNOWSVwlzZNaB2OR1fPyL5o8O76USxLF8CWc4cQAoa_H4pwFnTwZakffKaiQGEZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a29c3e62b2.mp4?token=XSzb0Td94YUp_gewk0BYwsGHTRMkOdTTrps7tm__xzfTdeK-swqM2gEndUerKIzXgyN4fFfXDlo-5NXAXt1wxXcyfjbKWoeqFINCBj_AfZs4LyRODW7dq21wBWhvaKmnXTNHHoBBlIGLMmFKJAatiUB8wQ0tQMyjY87QWMZCTPa7EDX_raFWmTVgLFZv8XtIz-Imx2kCHf9Sa-HEPth4nh4M_XfXbhxDlYa978SjjFnaXl5mxpbpY8bss8Dq_yEmi-MxUhYpy5lpPmbUOrS1GUJNOWSVwlzZNaB2OR1fPyL5o8O76USxLF8CWc4cQAoa_H4pwFnTwZakffKaiQGEZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🔵
#فوووووری
از مهدی‌تاج: احتمال دارد در جشن برترین هایی که قرار است برگزار شود جام قهرمانی به استقلال داده شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/103293" target="_blank">📅 23:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103292">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPmkvdx0LSuOp9fx93GsVp7qAi1JFDnwKTW6nSiwDWGhytfOxFyorzgQh9WBA0Z1bP1RULpurVh2gUficz-pTYAGhpmp1Zdo2fhH6JhP3q-8s3H8v5tA12Qh-P7oDzarLRvN0XtO8as46T-I3Gn8dTIcWMUrStVk2ZWnJrJUIsoBkO1r5DG5hdXUDlGtDKT9XGUq8vYQkJu9ZkgNwe7dj9uRLKt5B3_zacc38CM9n7ZZ6aZQK29zO9zLGZVucRMyRZiE98sPbpXxVTISHSE_a2hQjae5aqikhloyNBK5TzRRwgLoey5L4P49yHjAe9hVgrnsLDcFQjTdqbmmb9la_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی
؛ قرارداد میکی‌ون‌دفن ستاره هلندی با تاتنهام انگلیس تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/103292" target="_blank">📅 23:39 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103291">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec95bffbb1.mp4?token=cg9i_s1B2EI19pN6TZoJPx2eZul7s9j3_gXdmyiPbS5AhJpXLmKEHUuAe9S7CjlIZEJRIiHLZbGnKaNeSl5ESvK1Cc1P4IfFgJK7DgbBlNf9I3JWED5aeN4t4RLcXNkH7N_j6fhqu3ATcjul7_wdtxfIfrUnMqJHCoM15mwJutTXMU4mMbSvEY_jGnwGsbVeon-Ar7_xMtpoeTPmk6EjhD_PpeK0_4t7DBxkVSE9-yDJYEhCSxR1dGJhBj9j2Yy8JcIT1mV7rl-I2qWetSM6XuzMr-kixwx4Y5Rc_sWdNt4fRz9xKEvNJ6Ezu_fZL2rhVmrqEacq2M0XSSi83ZBqzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec95bffbb1.mp4?token=cg9i_s1B2EI19pN6TZoJPx2eZul7s9j3_gXdmyiPbS5AhJpXLmKEHUuAe9S7CjlIZEJRIiHLZbGnKaNeSl5ESvK1Cc1P4IfFgJK7DgbBlNf9I3JWED5aeN4t4RLcXNkH7N_j6fhqu3ATcjul7_wdtxfIfrUnMqJHCoM15mwJutTXMU4mMbSvEY_jGnwGsbVeon-Ar7_xMtpoeTPmk6EjhD_PpeK0_4t7DBxkVSE9-yDJYEhCSxR1dGJhBj9j2Yy8JcIT1mV7rl-I2qWetSM6XuzMr-kixwx4Y5Rc_sWdNt4fRz9xKEvNJ6Ezu_fZL2rhVmrqEacq2M0XSSi83ZBqzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
میثاقی: ممبینی مگر هافبک چپ است که با تیم ملی به ترکیه رفته بود؟
تاج: حالا دیگر رفته بود که کمک کند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/103291" target="_blank">📅 23:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103290">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/586f4ea605.mp4?token=WKHwcbCQsVZ_qUvAEVdX0e7VNM5RnK-hYPjL2hirMxXsLpWYJ-tchP6YPJN_9p68dCUfMwJDcuzT7M8hXIc-2L5Od6wSfpYOCeOl7LP0TCgAWTaJFJSDZA3u0Y6fDr1CEkOjgCDW9NDh0m997y7RDw4QDTJ5ob1iThP2k_8w83syaqv6A9tOQPye13Ls1jXMtw1obNonq4wrxaXctZSARvgGVQrLvoPLZfDiWAhfUFsJh7V8gKtb1ZRyERMHYyX6hMvWY5AhiVSLXaw5KYnfE4DA6l9Jd4CwEl4rVOWDsLLc0sgd0K0_UMuytX1AhVakqGhB21NE9TC8oo55Ku6CSZOz4urLx5vAuxbdtb2kvCuPZyY2RZetidD-VceddTqolgWOPyLH63G2nzZaSyZlE9iS-N1E8GYA8Qk3j2ACx2HtiFat21O6QjExTlVAPQ4zZqD7jzcWd1vFHo4K74hTGP4_1Br18pvyli1gyZ4ONLLhiCsvExqM4wp6zz50XvNIQVV6SoNW-wuBuVdvJgFpvhmEZ2PHheWeGTylSpeV8R2uFsZP4_trFF4pXAdei6vNrpE7drQeV2ru1xk0aLedE0lCfF2YVj0AszI3pdR84lIShNz_4VdpWhWG9iQZF7BiHj-LqH4fxl6j-cq4Qzpx4WWEm__g_fdRmMMDiMf7OVo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/586f4ea605.mp4?token=WKHwcbCQsVZ_qUvAEVdX0e7VNM5RnK-hYPjL2hirMxXsLpWYJ-tchP6YPJN_9p68dCUfMwJDcuzT7M8hXIc-2L5Od6wSfpYOCeOl7LP0TCgAWTaJFJSDZA3u0Y6fDr1CEkOjgCDW9NDh0m997y7RDw4QDTJ5ob1iThP2k_8w83syaqv6A9tOQPye13Ls1jXMtw1obNonq4wrxaXctZSARvgGVQrLvoPLZfDiWAhfUFsJh7V8gKtb1ZRyERMHYyX6hMvWY5AhiVSLXaw5KYnfE4DA6l9Jd4CwEl4rVOWDsLLc0sgd0K0_UMuytX1AhVakqGhB21NE9TC8oo55Ku6CSZOz4urLx5vAuxbdtb2kvCuPZyY2RZetidD-VceddTqolgWOPyLH63G2nzZaSyZlE9iS-N1E8GYA8Qk3j2ACx2HtiFat21O6QjExTlVAPQ4zZqD7jzcWd1vFHo4K74hTGP4_1Br18pvyli1gyZ4ONLLhiCsvExqM4wp6zz50XvNIQVV6SoNW-wuBuVdvJgFpvhmEZ2PHheWeGTylSpeV8R2uFsZP4_trFF4pXAdei6vNrpE7drQeV2ru1xk0aLedE0lCfF2YVj0AszI3pdR84lIShNz_4VdpWhWG9iQZF7BiHj-LqH4fxl6j-cq4Qzpx4WWEm__g_fdRmMMDiMf7OVo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⚪️
تاج: قرارداد قلعه نویی و کادرش را قصد داریم برای جام ملتهای آسیا هم تمدید کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/103290" target="_blank">📅 22:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103289">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGPTlwtUOEp8Py0YDFpclU9m7mCXvrblVmc8PmmnhvFoX8G55GYuCAzltbdfkeCaNt3zEgBLYIfBzyJ8PEFlWQEiHnP-4io59oCXjVodTQ2v2a5pmi4G6FmO5BlA-LC3nTG7jC09DELCM3TaaCYnzXw19SRsilPrMjt-VmnuZaXh8-7U5fDCqUufBBnF12Pid8ym9hdfUZlN58Bwqh2D6q9SBzNjth9gC89HbLrc6jCbqXEC17XOYL199QOckqrH9i9F_PpGi0eHHzMMKFK0Kcjya2w6IRLBN9PsqsJYYyDAwTPwaDNUBS7Hlpm2Q_3syiASOOoAWzjGPihjs70V3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورهان خبرنگار ورزشی مشهور ترکیه به دلیل نشر خبر دروغ انتقال موسیالا از بایرن به گالاتاسرای بازداشت شده.
در حالیکه مهمترین رسانه‌های فوتبالی جمهوری اسلامی (فوتبال برتر + ورزش سه) در اختیار مجرمین پرونده فساد مس رفسنجانه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/103289" target="_blank">📅 22:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103288">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUYUIwROiw_3_xFiis4WW7WQxeX61uNjO8HPX-SWdpRZE1SHnuY4yi2q4NdMj3BQD1JmJM9yc7Q2Q7zI5zhHeGGiRqY7JsQbB6zT3sBO1Djt6zFbBnCKOWERvhc7xm9v5r4827zd2P9rMLF0-7AEN351jOxKOEWv_5sMwrJbHaDOfpSQZn8pKV0PAzmr3o2-d18E8UDN8gXgsd-FBex_yTyy_Ik5_J_QllY-MKinG-L39gb2m8vq1oZU0uxcSzHp3-GC3uyh11X8yXVzL94zVbhpGEv-3NodZwXlBJKRY_LLTvX65PjQG-MMWvJ-Ism-2bka2msZwNFwBKFzD34BUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🟣
مارکا
: اینتر میامی در حال حاضر محتمل‌ترین مقصد نیمار بعد از تموم شدن قراردادش با سانتوس به حساب میاد.
🔺
اگه این انتقال انجام بشه، یکی از جذاب‌ترین انگیزه‌های نیمار از نظر ورزشی و تجاری، دوباره کنار هم قرار گرفتن مثلث معروف MSN یعنی مسی، سوارز و نیمار در اینتر میامی خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/103288" target="_blank">📅 21:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103285">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pdgCuSruRA6XjQmnqRrboMDxdKOLCkefNAh2HLHHDnLEvB2yE-Gg0i2-aUA1vstIsEX4JUD7TEFqNe6elr3DsA-oPt1hwksq9JP09Zdkafw4tbJnJNn2eSX75SvB7UEsSli4iawOMmB_3RdnTvFzxih43Mmf9rIX2qoAmKja6dB_XVclyLmxypiJUkQmWhlw1bjJF4CvCU-gdYO-A2dY4OidXpmApwL4M8drxDU5-ZS_8kb9SmsQFZXBNLSF5Ul_mHdmxeGdeF0dRyqRzbNWtMJdCdTGSNoTG7Vu0lmfX7roqZRsufci8_ojaKwfdPKDzamJCO9T7qWqisEu8F3Sag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dFs9tPwNWt6Zc03ojlWrayJDz0Af7n_MA2P1o1Q8414ASk37nJDvVj1n65jFyssDprS_iPs44l4w4JCtfn0Pog36e1gtNUwFSwyWOQI0sLNflcxZUIzrfLE9HP3wCD8aRSSdxmVhcfbtAivHN4yk4EArfaaTgjaM4JUcCV7tLlNfWtUYUAx36OQuRLvbMRHH_29LiUnTv0IFFAGGJ3YdSMn0VA6fcvXVbhHMYMrEo7XVaVvc-e1wfWvKEcQ4uELmqTb6hg1FQeNuzFHwXN6Akh_IIjKOfMa9TgEPl6uT1Yms9bfJnqcORW3iejcn-fpuh6ftRKSIYJizlrOJLj6YDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RBv2YuYxBvCNTepwjv4B6QTn-PnIeoRDnmZW1J5ceJW_u1ZWwDXqVvmI6l6HLmOZgUDOEBo1wXbpsBXBRL15rnfY1lQtf6V_lju8E46loomNELFJSyXsudiTYeaVTG17xjjZXfMMSUOZmb0FC1iuOpxY_l9k8A2z6WFEPYUjs9nY2qPdwB-dPBnkjNTtkJuQfhIWXLeL0tuml6TiX0bryPFW0Y09-cHhnVv0LOApFGoq_fgnfKxwPPK76bPDrzJOK666SnQzvSL2z_xwUErtb1JAPP20MPJd3nVqukZIKP6g0Uq8hXsfH5NSGG_n_ZuopBkPR5rkKrXLdplhR4IPUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
✅
🏴󠁧󠁢󠁥󠁮󠁧󠁿
اولین تمرین رونالد آرائوخو در لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/103285" target="_blank">📅 21:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103284">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فوووووری از رومرو: آلوارز امروز با وکیلش جلسه داشته و گفته که به اتلتیکومادرید بگه فقط میخواد به بارسلونا بره و راهی برای موندن نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/103284" target="_blank">📅 21:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103283">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
از میگل‌ گالان (وکیل ورزشی اسپانیایی)
🔻
احتمالا‌ آلوارز از اتلتیکو به دادگاه ورزشی شکایت کنه تا بتونه یک طرفه فسخ قرارداد بکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/103283" target="_blank">📅 21:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103282">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lja2Qt66ZPQ0B6o0u8Ilx1rb3hqUAxU4-JU6qc4RbOXS2eg1qvINl54tmF9TdrWVv9SheUU7rP3EnrtIQP_3fVw5TMmyZJIjl_yqpWRXcH8qq_G7jFZGdxEeJ7oMaNdxwfDVauH_FcJtsXNVoVa2tOqb7xL_KhNoOKUDIXYmfRPFmZ5OF92AHJVU9r9nm4MozvmpKZ-uYMNuD70ZWpW-KTVeugJQIwJTvN6sSczcheNtl3nqahm_zFJPrTz5kPi7ngJqDj9gh-QaVXzSpRfok0B_t_qUzie1nyDmAv8RHTmEB61vvDllrH7LJQtzIlS2x95hY2ZSip6vrsbVLrLFOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فوووووری
از رومرو: آلوارز امروز با وکیلش جلسه داشته و گفته که به اتلتیکومادرید بگه فقط میخواد به بارسلونا بره و راهی برای موندن نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/103282" target="_blank">📅 21:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103281">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjuegvS1th58HEuSaaPg256IRvQ4NhYHUrZDYfrloKUCjLKCMXkQmyVwG2cXIxdimP-_AL5AtcKBaNxY1wY3hk-3086eAG7zRCGSLH57Ntz6YU1yCfE7hVTDsBU8gwr_zcI9_hzt4zH-quLMmEceyiZQZqSbjjqUzRfpzjAPlRhRYhe52XnoiPxfLy7ELM360BwUfMjSxjq8IEIsRjpV0pnk0yUeDAmsE6O2S1zpMnD0hFevCX5ELnm5-VGNAMeCm1Hopol0ZUXTq-Oe0DfO8qe6yFKcQdN6mOOZV67cPiB2AI2_duydnRP9hXyKixJGSIF0CFLUBsaUIQZG6gw9fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔴
رونالد آرائوخو رسماً به لیورپول پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/103281" target="_blank">📅 21:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103280">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nzck62usUAzcBctLEknBEr_ouFgl7rKaVAOLdl5VJzR1pEDWIg0GUfMtm7PtO34br071yfW_Ao-tRMIWeEYYFJeGKxrMXztusjBD5EH4jZ1Ct-inu2DzyR6qU2l6KkYsK87BgaD0i0-J-chVR89OvfH4NRZe-A5RNCnPv5chohnGSe1hvXz_qfLaxbJCVjllwJha3a04tpR7WL0WpKYjVVB6NSfBGhSzkCi5nRXs1WPYVo-16mIeYRnb7ULRE-nqOqmxJ4DEtmZ8GwWGxHenwhNt_3t04ZBFupVBCMf8qDaTEPJbCQLP-4O7c9cMF4obwLYDwyldnLBttmzP3CHGeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
رسانه TNT برزیل: بارسلونا برای جایگزینی آرائوخو به جذب ناتان، مدافع بتیس فکر می‌کند. بارسا در مورد امکان جذب این بازیکن از بتیس پرس‌وجو کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/103280" target="_blank">📅 20:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103279">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ye61dRm-P9gIlZy0wfSWTay2P0-oCecSGqcCHXEWVVoIFVP0fpzi66tkIKlsNr3F9SylgWKpf8sI34hF3MNVZac8l_IxsBd7U-QxQvIrQRP2C2krHp9ugUd-EQyxpXr2AHkg0AQ4mXDcnkHQf6igj5Hh8vQHzSl4z3rBLuxc3YysmlNfiswh6EPegAjiBj_-e_AuZYumpNEQBzMBcomSLnLwRN_J1RFJuK6JxJLE2sAkVf8GgNIT9yPD9-C8lTySzdZbIe_h1vGqvPYb0ojMGhOR_fXUQqz4segPwz4TwqB7CK6jZLKodoy3m9UrhgQk4dwMkr3Am6ujNkakaY2wgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
پائول هیرست
:
⚽️
منچسترسیتی برای فروش رودری ۷۰ میلیون یورو می‌خواهد. بارسا اماده است ۶۴ + ۶ بپردازد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/103279" target="_blank">📅 20:41 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103278">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtExIaMSdzWk4ZK4an8ujVYIovOPntjtGbcKZiT5F4dFSfXJAsR6DLL99DJv5M_jiJ-9Lb4lJmuTcJuVZ6kdky9uK0aBgXDnMO4AvtwYyjRVP4CcKc50kYR4_rH68HAOsrDSFp4otRlccsQ3NKfWjpw93DNng8hsn4WQNVi9lIliqGYStY7n_FXRQjEiYR17eP2bydOBy2nUSp_fXSdIf9emdtU2VzPx4mlirHaPUcilXQFpgfbPt0FzRAxpEN97LOqjN45oxfrS7B3tnXNpITVzoref6FLklMW0nxV4IQbPaTWySP2TW6qz0tmZSwoe94k1JIMNh044vZ0fEWrvHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😐
ترامپ:
ایران خواستار غرامت خسارات درگیری نظامی ۵ ماهه است و من هم از آنها غرامت می‌خواهم
چون سربازان امریکایی را کشته اند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/103278" target="_blank">📅 20:12 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103277">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLMGpEgDva4yeMkMgOb17TUb5ZGBBdMon2NqeU0RqAXSi2tS_ot9y0gzywMwW4gqSUc5tpy617PJ3f-Q92rB9Nk83gfKRP5dfo0LEeIqvxtyro8-qvDXm5CCmGVF2FqId-tgm9vooGIvs7l9uCwzlF3gF6qgfesUZQ_K1IbrI_WqQSwIdjcvONO2P8O0Z3eq2f_f9KEjVYjcanYmLg4DOdvIHwQ93Yddrw4R6tIszpy0KQfeHToY0k2V2mn0erax0GLCrpovOlnqDS3cBrCRLCQ_HwtxtB_0Za0L5XqqF8KFZsyoJVMOVZ_rT9DptlQU70IDw9Dc1Is89D4hUdyh2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووری
از داوید ایبانز:
🔺
🔻
لاوتارو مارتینز پلن B  بارسلونا در صورت شکست انتقال خولیان آلوارز است. هانسی فلیک و دکو از او خوششان می‌آید و این مهاجم آرژانتینی را زیر نظر دارند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/103277" target="_blank">📅 19:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103276">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MktgeJRx49RnaMiHFqehy4Y5z690tfbxcWu3Gd0ZY5tGZZPpO9HPDCGqnWs_7jocqdWJnFkeuHijwEMhA9y45x9Z1fiIDKo-B2Gq4SRqPzOx5Mc7Cc0GHtZqaRCyaEgd0tJ4q8s0-1i_Hz8kndvZ_20t53sP5Zr_iSlvIbs9LV3-B91ucx7nwsQq0y4H1QzwUg9RvwZOPE4RkMdDQLwwfnrEGmqFv1l35-54YtMYbVLNcRS5ap197YMtL60188Tqhosr1rEe2C75APFSZjc3VI5d93nJIYueEGIdYq5MGI-RdUWQIsAWHV5mKW7RtHIDC_hy5piEmZMMUJdUkYQx0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پریمیرلیگ در این تابستان بیشتر از مجموع چهار لیگ اصلی دیگر اروپا هزینه کرده است!
🇬🇧
پریمیرلیگ:
۲.۰۵ میلیارد یورو هزینه شده است.
🇫🇷
🇪🇸
🇮🇹
🇩🇪
لیگ 1 + لالیگا + سری آ + بوندسلیگا 2.047 میلیارد یورو خرج شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/103276" target="_blank">📅 19:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103275">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vAZ3QLe_sTbuCWJ4lZe0JuhzXniWe_gAfVdkWwHM94jxS2LLaVg44KSmDpccTZxRCxhouaOR-IX7wUkIu8bEZ87Ip3QqVt4sd406MYUy-181UvIk_h5onkr1tlTl04gZVt4-31TjDhaODNR8kX8qIIMCt5O0Am_mQg9oHwThvnFsXZV2YKiS_j7pd4Y6DyErYeLAZclydROwmz7CGZhPXNW69AMg-J2-o3ySQimtqZUEjTi3GWlAQ8Tq95ZdmXZXG1khL_Cb2xsbR_FqZNw82FRc4GPLNzFfv_X2bCmWs8JQg709z9rhTYV8n3Qq8l0FrjOLMzpXyuDkxgZiqq89gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
اولین بازیش برای PSG تو فینال سوپرجام اروپا مقابل تیم سابقش استون ویلا خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/103275" target="_blank">📅 19:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103274">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8023c35480.mp4?token=HNT2SxSC1aUW0vpneZ9FenY0g372HXbfJg9nroO_WeIvbcGTi2lk9hsR2LEBZY7XGBeDS3rk8EEmX9guyxNV4TCq2B976BHP_JC4WL4EgmNNxx19kTohKWSYEWQD9LeTEnfvFfjVhUcVvtm0NmjQROJHr2KyDrIzzl6Ty3bxvAq3p94QJUz3b2fshXeWpLP9wcSoNJyQrbNZ2Yql0Mdr3UhHhSZow4awQ2aMbffmNwThIl9jySyzep6mJ4GRG0UZAZ_23laMkpHn3PmJutF__wuUS3OUIeRA8mo4CLpRQNm_Drsegi_RmiwDE-qgyl7PLLPqkftmV3Hvrtz5bODBJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8023c35480.mp4?token=HNT2SxSC1aUW0vpneZ9FenY0g372HXbfJg9nroO_WeIvbcGTi2lk9hsR2LEBZY7XGBeDS3rk8EEmX9guyxNV4TCq2B976BHP_JC4WL4EgmNNxx19kTohKWSYEWQD9LeTEnfvFfjVhUcVvtm0NmjQROJHr2KyDrIzzl6Ty3bxvAq3p94QJUz3b2fshXeWpLP9wcSoNJyQrbNZ2Yql0Mdr3UhHhSZow4awQ2aMbffmNwThIl9jySyzep6mJ4GRG0UZAZ_23laMkpHn3PmJutF__wuUS3OUIeRA8mo4CLpRQNm_Drsegi_RmiwDE-qgyl7PLLPqkftmV3Hvrtz5bODBJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهکار دوست پسر استر اکسپوزیتو تو اولین تمرینش با مورینیو
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/103274" target="_blank">📅 19:21 · 19 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
