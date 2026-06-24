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
<img src="https://cdn5.telesco.pe/file/cv7jVK8Vl6vgifbZX9sOzIMHsn3Vr7zsBF3F20X6V7-0eXZ6wJSrZ_f68NCWpXY5SIRg45Er9-IDf04K7DMBUrYf1e4YCEo24aiU6t4kPcFKZ4xR772S-Sh8AMaPvyX8Tq1-DxwUhDTI-yizf2JtIk4eX2BD7ZaCG3R7BXzZjL7aI2ZiSA-M7UIsQsKdkb5A6grdABeHERZiwA2INKYW60qRPShAiaulEMKfb4ms8DiTs9ZC-0oICj1e9rVc6UPUUs6NKy_ZsvInR2Yk5OrQTu7jWbdFl8MnWQMEU0QeFsycjtiOAlDdXfzljTgFNaaVsjOLmlWJk1mKlG1STYgXQA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 711K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 18:45:45</div>
<hr>

<div class="tg-post" id="msg-95643">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3u9b-DkyoI3z8V7ylIFzX6Mg3R41TDEj0u4zHF2twIyzkw1s8paMoZPvGdR8VuFY2cdNdonQ7nURmqtv4a9ek1V-ZYSgzWzjcLudteu-vvQJSUcAYJt-3GPl5wVXQo47EnUfnWksPGp0Vzx8DwyDg7IM1j4Dt4vs4ybUk9NtTxX2J2kazyL7ReNhG9kTq-6hsK0xNnPNf9DLJ1DyxwXRaaeHH4EqlV13IKmIOhOZlx7pmgX_nXlCI7xCkeNifd9n-oo9W6EyMhoCXhVEScZEBe1MlFQ9K_enaIPAS6cCwheWcUlRWHPpHgLYg_BxpTqaxAZZQqBM5BtrfCtSSy0Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
لیونل مسی ۳۸ سالگی‌اش را پشت سر گذاشت و وارد ۳۹ سالگی شد. آمار او در ۳۸ سالگی:
⚽️
50 بازی
⚽️
50 گل
🎯
30 پاس گل
مسی در مجموع روی 80 گل در 50 بازی تأثیر مستقیم داشته است.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/Futball180TV/95643" target="_blank">📅 18:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95642">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cOwwKOfBT_uwAEVt5aQZY35cOJsgAmnFfACtQHVGAL97f8XzbkVYvKVMATQbH7ExIIap_4PNjejZvisPqE3C9UluG2YgPazlkxL21i3HQnp4hKVOeHDSpHTTWuACTtbAa6r0-3LIkwJTTfN-GSM0ghanE4Gsr4pAbaWT1FvgwJiSI-MWUh_k8pj-sU0g272T5vbza827ehZbsojniL2OvdEw9n0jnM098RzESzvxhXEoaEybOsSP_qE3hi13np48KeOsWKsSn5DmqIHniw4p2UEu58XSnRgBQ05kNgq_Adxe_oaKeQR5OTOZjXJo3dfaXB0Rj1aTKPp7UiSSQAfhWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نانا کواکو بونسام (جادوگر غنایی)
: من، کواکو بونسام، قدرتمندترین جادوگر جهان هستم. هری کین را شکست دادم. دیشب بازی او را دیدید؟ او حتی توپ را هم ندید. چه برسد به اینکه بخواهد گل بزند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/Futball180TV/95642" target="_blank">📅 18:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95641">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/95641" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/Futball180TV/95641" target="_blank">📅 18:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95640">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=coKxj7yx4F5qIH-q0TL0qDlEOTyrIi6SqCkZfFVKj92u_LowBXK2NskndOKinWtzP3T0gaSPU8W8U7KaZpIOXJpwAScZANQgbz2rcZ2isX97u6N-RoyxAI_H8XDGGGO67C6RM91l2FA7l4pHUo5lIzAHhQac3LupBPCawg6HQjrhoXMC0XoVYHBpftw-z0Wut3Zuc4r2DGBNh_Qax-AahRePzBbesp6NWI8mMYzabIP_GkxJQ-1H7IbgupnP3CN7ZQ6DeRyaV8Bm4vQpTdkuqIHMZgfT4m-ERbphOL-aFnifUsNjxjPY7xJHtD6jbRYPuY4BtIXXGElqgSVz28tItpiBMGgoPTgMvAvpjDNx78V-2pzBpF0oGnBbIGlo68ZJzuFOVAlhuQEpwpbmGeA9JiyRfYXQnS92iQ41PH9yV-8ZPWKmuh6k5TwYzMDzdfkC37RDOeyPNRlEBc5hg-T6umXrzWHiRomaepRuqMiASbVVuLNUIIUHcgj-3JkzwQl8RdlDr9kD8gIJGVvqeg1--2wGZ9bHzd0MWK18B18CPGGONh08CGnArZkuqjgJY8H-V9HtbOUPy51Za1JUHDWg7tvI4e6RzoC_CiPDOmqu5m5lOnXkhhiJgSHPIOyhr0g0S-Yi4wylSsFLT55tIDj3TkUZZMD5BaPU6G4t7cvHwbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=coKxj7yx4F5qIH-q0TL0qDlEOTyrIi6SqCkZfFVKj92u_LowBXK2NskndOKinWtzP3T0gaSPU8W8U7KaZpIOXJpwAScZANQgbz2rcZ2isX97u6N-RoyxAI_H8XDGGGO67C6RM91l2FA7l4pHUo5lIzAHhQac3LupBPCawg6HQjrhoXMC0XoVYHBpftw-z0Wut3Zuc4r2DGBNh_Qax-AahRePzBbesp6NWI8mMYzabIP_GkxJQ-1H7IbgupnP3CN7ZQ6DeRyaV8Bm4vQpTdkuqIHMZgfT4m-ERbphOL-aFnifUsNjxjPY7xJHtD6jbRYPuY4BtIXXGElqgSVz28tItpiBMGgoPTgMvAvpjDNx78V-2pzBpF0oGnBbIGlo68ZJzuFOVAlhuQEpwpbmGeA9JiyRfYXQnS92iQ41PH9yV-8ZPWKmuh6k5TwYzMDzdfkC37RDOeyPNRlEBc5hg-T6umXrzWHiRomaepRuqMiASbVVuLNUIIUHcgj-3JkzwQl8RdlDr9kD8gIJGVvqeg1--2wGZ9bHzd0MWK18B18CPGGONh08CGnArZkuqjgJY8H-V9HtbOUPy51Za1JUHDWg7tvI4e6RzoC_CiPDOmqu5m5lOnXkhhiJgSHPIOyhr0g0S-Yi4wylSsFLT55tIDj3TkUZZMD5BaPU6G4t7cvHwbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/Futball180TV/95640" target="_blank">📅 18:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95639">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SaPji9fvB6bclTkdt32OZfvEdxOCqcCcxxy0GsAXOlC4l5no3Z0rHs094D_u5BEm4ExqjAxM0vRKBL998R034CFWQJg3b4jqrvuTXjV7f8zpvRtEyacYZsjJceogoJ5nyTJ3_DRShX4DT2SR7gF6zi-mZehUEtKPlZfAobZKhaBaNBHUvoXFgU3QF0KwHaz1TcEz1X6zrM-Ocy89t1GxNX3IKtAI5TR2OQJy5-VSqRqi5ZoDx_mrJuEiZ8ghM8Y5hOByCpRmoKaqri50Nq38SUN6Zgsp02rX_lYMYkTNaB1ulZYK8NiX21R7j-P2F0-_Tph01VZQFN85F17mrXK9jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🔥
فورییییی از کارلو آنچلوتی: نیمار کاملا بهبود یافته و آمادست تا 90 دقیقه برای برزیل بازی کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/Futball180TV/95639" target="_blank">📅 18:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95638">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51d71eb644.mp4?token=PRfoRL9IaMW_lebkPnrscVIFyeUk1DTLiUP06lySVKD7ie5uBBK4QtnpRogJJtYD79wTXOD-p9OEPxX1w2J4wNheKmRDutz9UZZGGOuP7s0X_-odf64I3O7NcO00FdlZikhx0S-ZNXbeqOkZTUTKhIpzskJSIqNfaipniWOn0KBECaj9iKDVTZJ6CVE04vmCcfwVhn_zMSlnH7fbmkZag3WT-bEIQ2oHTv_FPldjhOD7qXLYtOpqsLSq30p-RiHEmLqR8QS8vL7jnyVw3LAHoYPc5DeXhwSDt3BMQIM3Fl5lUn80CIU-A4XK1NtN26Ge3jDMGGfIl2ZN-H5ioJnfPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51d71eb644.mp4?token=PRfoRL9IaMW_lebkPnrscVIFyeUk1DTLiUP06lySVKD7ie5uBBK4QtnpRogJJtYD79wTXOD-p9OEPxX1w2J4wNheKmRDutz9UZZGGOuP7s0X_-odf64I3O7NcO00FdlZikhx0S-ZNXbeqOkZTUTKhIpzskJSIqNfaipniWOn0KBECaj9iKDVTZJ6CVE04vmCcfwVhn_zMSlnH7fbmkZag3WT-bEIQ2oHTv_FPldjhOD7qXLYtOpqsLSq30p-RiHEmLqR8QS8vL7jnyVw3LAHoYPc5DeXhwSDt3BMQIM3Fl5lUn80CIU-A4XK1NtN26Ge3jDMGGfIl2ZN-H5ioJnfPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
⚠️
حالا این‌وسط بانکا چرا قطعه؟
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/Futball180TV/95638" target="_blank">📅 18:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95637">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/028dc79cec.mp4?token=gCfhYKlxI30-c_hvPQnMyen1Ww3JCSjDqu_LpkIoARpQP1a_0ZCAhCsWRVSdbMwceddyrFoCXYVIpPretwsvTCwydnMf7sjlzYEiHQtYc4yQK5s_832XUWa_79KM3vG9Ljts4V4CUafO4NsYmZT92n-7d1tNWy-gU1bqIKpwTr7ipiC87ii1NINtV2t4Z8A0omaI1pBWx7WBl026EXLx5rsvlxFIwF8Biuhh6QTbIW7U58HElPh_iI5s4BiC3d5WaW0_mx7nTCpNITHz5n9uScLEu1ctnjwtbHulgv4SlS2_jt8Y-xwIe1Vvir8q8fxDKBriY_a6bd1HChuERHXeew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/028dc79cec.mp4?token=gCfhYKlxI30-c_hvPQnMyen1Ww3JCSjDqu_LpkIoARpQP1a_0ZCAhCsWRVSdbMwceddyrFoCXYVIpPretwsvTCwydnMf7sjlzYEiHQtYc4yQK5s_832XUWa_79KM3vG9Ljts4V4CUafO4NsYmZT92n-7d1tNWy-gU1bqIKpwTr7ipiC87ii1NINtV2t4Z8A0omaI1pBWx7WBl026EXLx5rsvlxFIwF8Biuhh6QTbIW7U58HElPh_iI5s4BiC3d5WaW0_mx7nTCpNITHz5n9uScLEu1ctnjwtbHulgv4SlS2_jt8Y-xwIe1Vvir8q8fxDKBriY_a6bd1HChuERHXeew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هوادار انگلیسی تو بازی دیشب پشماش ریخته از حرکت مردم غنا و فکر میکنه دلیل نبردنشون سحر و جادو بوده
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/95637" target="_blank">📅 17:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95636">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXPy352SyxT67lJDeX4QpVlf0NxY5adY9WSrHjFQHFKVARNt2qv0y5o-LGMq0kOC3g-Zhs-9iEiIhJ0aGk9qtpJC9S-y06UBdp891ZrmQgOejW_ctpwmnx4CfYr5hZ_6uxsJaghd50tjnaoXujkFnHawScOE-5A9QB1FZ0Tvnle3qrXEFypydAHkCmChUCyIlqTYdTcqLgbmkNcrcneAPxGE8HNkKQhREp4C4kUeUYGc9rpXgVrR4wnNTnKoXH3gWmesocDLcI-4TK84lX2PKQ2lWIEOUxrRoEp-TK2NJ4HziSD2SQqpjy0g99_ap1ukWZuL7Lr5ne5WxHNjObmOOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔵
متئو مورتو:
🔺
پیشنهاد جدید بارسلونا به اتلتیکو برای خولیان آلوارز با پاداش به ۱۳۰-۱۴۰ میلیون یورو خواهد رسید؛ قراره مذاکرات بین بارسلونا و اتلتیکو مادرید تو این چند روز از سر گرفته بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/95636" target="_blank">📅 17:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95635">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1224d3d31b.mp4?token=KruNV0Ke_h8CvJsCXmkd28ii3DuZYAq94JlvDDs_mZJ1KaIQYQRHE8jfgCQjCIw0ePx93tfQM1D4oAv0QBXCROV5BRMCQoMIEG-WgG9IFwazlK0MEE71wkdSEibDGcc18Ey0rXeNm_px9Bo4AxnA9uUI2XuLEKSqdi9VRKHs9jbQtBsxhYr3gxBaigQUS_4NIMg5f3hRL7kYiUkIe_cqZ17uLi3CTFfDbMSamqjrx-tgjkN1UnJ1kJumKmyA_-GuGrc8gElYd9BSUV6X82vVN_8KIa1mWPY-Qo5iPwF_dOYXbyFQJvS2kVItq4ferIVOARbrf8uaPgP-9T6qQj1AJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1224d3d31b.mp4?token=KruNV0Ke_h8CvJsCXmkd28ii3DuZYAq94JlvDDs_mZJ1KaIQYQRHE8jfgCQjCIw0ePx93tfQM1D4oAv0QBXCROV5BRMCQoMIEG-WgG9IFwazlK0MEE71wkdSEibDGcc18Ey0rXeNm_px9Bo4AxnA9uUI2XuLEKSqdi9VRKHs9jbQtBsxhYr3gxBaigQUS_4NIMg5f3hRL7kYiUkIe_cqZ17uLi3CTFfDbMSamqjrx-tgjkN1UnJ1kJumKmyA_-GuGrc8gElYd9BSUV6X82vVN_8KIa1mWPY-Qo5iPwF_dOYXbyFQJvS2kVItq4ferIVOARbrf8uaPgP-9T6qQj1AJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
💥
لیونل‌مسی در اولین روز ۳۹ سالگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/95635" target="_blank">📅 17:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95634">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
‼️
هوادار خانم منتخب ایران با پرچم جمهوری‌ اسلامی خطاب به کسایی که پرچم شیر و خورشید دارن: همگی بیاید برید تو کونم
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/95634" target="_blank">📅 17:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95633">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eYoByDCWKdEcIn_uEsQQ34w6l5GGxqwPZQtLN4qG8ugayuo1ncLWtb2gO_l_Gs_04F_9S25ZQSXewFNog07Gxw9GzEnPt_RZoMEnJtp3SRcsKU_4RkAAKwq86NCvlpvQd4qaD8hhV1UFj41Un9gI2r1Ary49jnZufvgYFAnVNFF0UJU-_dlOSefkU9uTXK4MvL856U9YY0iGpQ9ZYyBoHB24BxuU-Mjs5CXkG5WG3jcrnqDzbWAPfGYjz0_-CULvCMRa9fLcM46PoXXc9gMbQKRFmg8R4Lio76a294_ILNG4GmD7yMH0xzSTCUtGoJVYF_psv2rF9sCxpWpJ2BZ5kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
علیرضا فغانی به عنوان داور دیدار پرتغال و کلمبیا انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/95633" target="_blank">📅 16:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95632">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b14e7b150.mp4?token=dy132QBnIfrBQEflAGRMUnOLh10Hz_NuJGZFveICfeAXReE5enMgZwUekcZdWQ1d_mplIEfP7jSudOnwneXubrFOc0yS0zA-KGKj4CLHwI_UjU9nrJaLBdW743-NjvV5xycbOvJY1j47eGf5TEf71oVN1fb2G_KyZ1sAuyWmHfv4qHA98o2At4gY2EsQnBFrQ7q3SmNhqY4qwxsKEbCCZzvQ0nMEE4eSvX495L1Mn26u5g9hdOy1v6SpTUQyET6mrS3lLV504vcTZCRqaDMw4rLKIuTDkKXAuT5trCjxB7xK7rOuIvTT1T1ZMCnF5twe3iabwF4yce_GlaxrEqBltg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b14e7b150.mp4?token=dy132QBnIfrBQEflAGRMUnOLh10Hz_NuJGZFveICfeAXReE5enMgZwUekcZdWQ1d_mplIEfP7jSudOnwneXubrFOc0yS0zA-KGKj4CLHwI_UjU9nrJaLBdW743-NjvV5xycbOvJY1j47eGf5TEf71oVN1fb2G_KyZ1sAuyWmHfv4qHA98o2At4gY2EsQnBFrQ7q3SmNhqY4qwxsKEbCCZzvQ0nMEE4eSvX495L1Mn26u5g9hdOy1v6SpTUQyET6mrS3lLV504vcTZCRqaDMw4rLKIuTDkKXAuT5trCjxB7xK7rOuIvTT1T1ZMCnF5twe3iabwF4yce_GlaxrEqBltg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
💥
پای شخصیت‌های وایکینگ‌ها هم به جام‌جهانی باز شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/95632" target="_blank">📅 16:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95631">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
ترامپ: بازرسان آمریکایی برای بازرسی سایت های هسته ای ایران به آژانس بین المللی انرژی اتمی می پیوندند‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/95631" target="_blank">📅 16:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95630">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c083e67433.mp4?token=S-lXnlpNFl78pswweDggcx6NvWtitq_YtzWuktF_wsaRgqyyg-jmLqXdQky3msnpwn4Ib0j2DRSI1D9PzpO_W5rh-uAYFix1IIssqUybz9FcHSYFcqOsQRCNfCHaHs5vpbfY9c19sDyI7xW9oUSf-uZjBNHYF9Um3vzHs1pqmdVoxuYkt7OO3HzUGYym3s44BdauaNAkvnKLxuKbC3YkBKlW6PAlU-22FqcUXE5D20kd4UwFlMhwQL88yp-a3CSjZUxN5IqND9k5yMSC4EYz4XBsL_u1fueHC5ZFbf8TY11MxW887xpG2fNynqvcfm0CVfLNGLGyOj_NLQ-KXOrd0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c083e67433.mp4?token=S-lXnlpNFl78pswweDggcx6NvWtitq_YtzWuktF_wsaRgqyyg-jmLqXdQky3msnpwn4Ib0j2DRSI1D9PzpO_W5rh-uAYFix1IIssqUybz9FcHSYFcqOsQRCNfCHaHs5vpbfY9c19sDyI7xW9oUSf-uZjBNHYF9Um3vzHs1pqmdVoxuYkt7OO3HzUGYym3s44BdauaNAkvnKLxuKbC3YkBKlW6PAlU-22FqcUXE5D20kd4UwFlMhwQL88yp-a3CSjZUxN5IqND9k5yMSC4EYz4XBsL_u1fueHC5ZFbf8TY11MxW887xpG2fNynqvcfm0CVfLNGLGyOj_NLQ-KXOrd0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
این ویدیو خداستتتت. خداداد عزیزی مغزش از کسشرای خیابانی هنگ کرده
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/95630" target="_blank">📅 16:02 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95629">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvwkO3Zkx5nnM6oubKZ3BjYReoTZQ06owH8nRjRIpDWAuUje94aDjCq2ALIIbUWeb8Db4hMRJ0ApV20CqKiIYTTKEfhg20z7K03Rkvu4WE7lzQoPRD5wqGAUWDSyQCq_PNWEwpmT2X2fTJKmW0CxcaLgMD1wF8jCue1bc8nKpzDYfRC0oIFPLo7rSSYVAq6sy_v67fMg6Lm1VYA5m6WrY3YWAYo13FSYoEVAxst9AoOeF-5h_iXJ6lz3tXs_boq45zzXGHPfqtpFN_6IukXN7mkba5rIiT-rWOYCujx6aBf-ohWRmX8YsL5SN-QyoQW2tYnwSs22t6Oc9GgfDNIPnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یان دیومندی بازیکن ساحل عاج در جام جهانی 2026 ، 16 دریبل ثبت کرد که بیش از هر بازیکن دیگری در دو هفته اول بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/95629" target="_blank">📅 15:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95628">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa4e18637e.mp4?token=Ta-6TwD0Z3XFA5F2oryQK4-fF_KraXRwUtnjHXoN8PcP-X2Y7Kxm0ML-wVB3rIYgpfL36cZpjeMJK3CzuNNFr7i8A1of_hzthZCNDbuA6W7u55-BP67kfYo9ka9s4G7uEsKMrQTPb7-62oSSN9bEsQ_ye3oaOTrL0rAHvRavHvWCo20jmVmMwxtZpMiCiIXRTUVjjtcSmaiwJVD_VYc8ScDElrWdnzGgcVwS7OGKx0tvm_Q4Bo_ff_VEHJ06Rr5-ED3hT7EKbNkRJT_6uWDnKjZmyVoidb4KrCfU9CS-r9yxYOLM79x0FcThcV9DCWmXmYTltBdvrr3Hm-AwBikPRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa4e18637e.mp4?token=Ta-6TwD0Z3XFA5F2oryQK4-fF_KraXRwUtnjHXoN8PcP-X2Y7Kxm0ML-wVB3rIYgpfL36cZpjeMJK3CzuNNFr7i8A1of_hzthZCNDbuA6W7u55-BP67kfYo9ka9s4G7uEsKMrQTPb7-62oSSN9bEsQ_ye3oaOTrL0rAHvRavHvWCo20jmVmMwxtZpMiCiIXRTUVjjtcSmaiwJVD_VYc8ScDElrWdnzGgcVwS7OGKx0tvm_Q4Bo_ff_VEHJ06Rr5-ED3hT7EKbNkRJT_6uWDnKjZmyVoidb4KrCfU9CS-r9yxYOLM79x0FcThcV9DCWmXmYTltBdvrr3Hm-AwBikPRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
جالبترین شادی‌معروف نروژی‌ها تا امروز
😂
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/95628" target="_blank">📅 15:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95627">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PnEaAO2HsEuLgOWAFlZm7TVWVsn6y5CI8KxV0EUdj9ktWlQdJoIeV0FNzZAVjPU3P82D4ih2oD1QOTnnd2ak7pm4rlp1cwHyfrVGNVehQRIp8Q-73uxPMvmagggdgdC8-16yZYRkFrySuFuO-OBPM2cIwUYNk_NAd7CIbnmSXQek3YEJnL7HUx46f-n1e84uF799jh3yAKtu1-8NdKdQyvgJfTUak-cdWkMXSTkj4b916xYfnbhEWV2p_0r51kREJ1VbXcH35WXTzxMTnYuqPE23DRpL8hClCcJUKPvMfIZpCx3d1bETT08VEU0x27C3ycct02mVJvSuAuW31p635A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
بیشترین تعداد شوت در چارچوب در این جام جهانی توسط این بازیکنا انجام شده:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/95627" target="_blank">📅 15:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95626">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23666a9bc9.mp4?token=MwZwA2vjEAxxRW1I4Fv06J2cPz18_raYuIIM69M9M9jkMHO6TLVQnnjzZ0Py4WhErpsNpxRcq06NAD3H8kanmFrnzOiNPeoccPyBzW6knTkgSQGJ9uqwQ35uXK6WC2fJ-7ENd_qOWkUTqa8bTlwOy8nvi9Y7-2E-ba5Nsf0IQVmcBxKEcgzS2Qd2el9Yy5Y-RemI-an207hp6qJwQ1zwUqKOEh9I3vea6Pyh9dBBuAvu-d0LQihckuV4r2IN9_ck4L0ncstAGAQ1Cxq0K7p2U-TrjAw2NkpJ-RHfd4XEAjrUFXVfHKZdB4DVpVG7QY3-3-zXn7Slm9l_vlf4NJa1vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23666a9bc9.mp4?token=MwZwA2vjEAxxRW1I4Fv06J2cPz18_raYuIIM69M9M9jkMHO6TLVQnnjzZ0Py4WhErpsNpxRcq06NAD3H8kanmFrnzOiNPeoccPyBzW6knTkgSQGJ9uqwQ35uXK6WC2fJ-7ENd_qOWkUTqa8bTlwOy8nvi9Y7-2E-ba5Nsf0IQVmcBxKEcgzS2Qd2el9Yy5Y-RemI-an207hp6qJwQ1zwUqKOEh9I3vea6Pyh9dBBuAvu-d0LQihckuV4r2IN9_ck4L0ncstAGAQ1Cxq0K7p2U-TrjAw2NkpJ-RHfd4XEAjrUFXVfHKZdB4DVpVG7QY3-3-zXn7Slm9l_vlf4NJa1vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😛
آرژانتینی‌ جماعت وقتی میخواد فوتبال ببینه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/95626" target="_blank">📅 15:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95623">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cbxKDvdjefgjz5Pr8N3Od-9dgvGPIEtfLCwjwJUn5t5mMs3wnMi-Yf7Hl2VcKQv3tD-FLFY8e97Ik4M1S4hnQb7mSIqY2bOxYy_ODy3-x_IQlC9nTSjxRrzbOtok-4PAtGZ6-dIeI-1B27LIOSXrBLOKOFhxVTNYsSaChzAKa-aCP_maakmCorPSwMZbuYKYdS9Q4yAz3EJLfDzPJUNYdMmMXeSvee6j0PAgOEduNBqZJPx0CaVBDi5Hg6U-xoycoau4FshG3WKpBePK5Xwoz3q4-SYpQM9LxznQrV4HhsimzX7S_vY9RvXCDYnAiHi96CyCpq8c8dSLoMpIJDCmAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rmj3s_czz7Wud4uJqIdVMEGPXPqBVxcbiezd3tU5d2IcMr8xfAbrvdouu-Qc0dTXCklVz6y8inppctcdRKPJeRlO0V25Qj-rsbiOOTocs8TJPS7Z-PWwXpU229djcuxVj8q0cE3uw7ITusE345_jPnlx9CrG8YneJvWl9huey8rmBee4QhkctZz5VztnmqOVg5YAJ3lY9lkVL1o0eNAPsUNDRROz_W8GuqiFE8T1xhTqVQIK5qWZnW4hLU5LJM8oV_R8VNzkndSHrQmINajklw_IWDwYT66hsnwoZJpdIpRn6oV798bGwrquhTK6bVV42iTSMA1KtZ9q82q7fbZs_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bBHYWjCy1S9IgMY3ynm5v6eh41rKJ335W4UCV3uR87a7dj6wJuiyOl5bwIZl61hIGcE1EuZGX7Mj2fHBHT6fM9CTC6sBRCpjT6m6xYGnvXDhwoKiqKKs3J0o7j7rWll1d_kWePPZy3uhQVM41RfnFOCrQ-jq4V99Tg8S5Yw_nVfpN_93qieC1ZcnAQOxsSa_5cH9cxat_U0t5OTTRFRmJZbZPYpF3hVRZLClXvKjPYlvsd5T7TL_mtUwIL3a99uQZv1gsR59z-powVKkLdMqcswAM2OqRK3thBsWNeAJhzHld1obfiZyJST4H6Ec-pG2fkn5fs9CFW7RzoAfLxThnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🇮🇹
12 سال از این ابر شاهکار سوارز گذشت
😆
🔺
فیفا بعد بازی سوارز رو که دو بار دیگم سابقه گاز گرفتن داشت رو 4 ماه از فعالیت‌های فوتبالی محروم کرد.
🎙
مصاحبه کیه‌لینی تو سال 2020: من شیطنتش رو تحسین میکنم. نیازی نیست از من عذرخواهی کند چون من هم داخل زمین فوتبال یک پسر پفیوزم و بهش افتخار میکنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/95623" target="_blank">📅 15:19 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95622">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30a14dc199.mp4?token=etZ-y2msNAh7IV0PwG09FGLVL8_LNqqzKpZos7YX3go41IgKSYOe9OSPsIWv8huygI00ZwCC3bZcYXqauT-pAz4t5m4f-BtatGNm_Bc4hLtOrskqQ9gu6cKWXtqruSMTqvV9NrnMrznsG-_nh3eVXZ3PGdVDEQWhVIKu-nG9Lcv64c-N0MStVQdOWWYyONfAnDrIDDjPZulJd1ZaGzRXagbkWZ9ULLG08ZOwS6xhzd9GuTUr8o1FUl8Ys37viSzNg31MqSxssNB6sDrw2LQgVHqNekAbcniyeXjD8Je8zt3j3d5Rfx63zmokbTcCBSAVnl4id4_tsXGo153v-bWHOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30a14dc199.mp4?token=etZ-y2msNAh7IV0PwG09FGLVL8_LNqqzKpZos7YX3go41IgKSYOe9OSPsIWv8huygI00ZwCC3bZcYXqauT-pAz4t5m4f-BtatGNm_Bc4hLtOrskqQ9gu6cKWXtqruSMTqvV9NrnMrznsG-_nh3eVXZ3PGdVDEQWhVIKu-nG9Lcv64c-N0MStVQdOWWYyONfAnDrIDDjPZulJd1ZaGzRXagbkWZ9ULLG08ZOwS6xhzd9GuTUr8o1FUl8Ys37viSzNg31MqSxssNB6sDrw2LQgVHqNekAbcniyeXjD8Je8zt3j3d5Rfx63zmokbTcCBSAVnl4id4_tsXGo153v-bWHOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
دیشب صداوسیما این نماهنگ رو برای تیم ملی پخش کرده و اینقدر شاهکار بوده که از آرشیو شبکه سه حذفش کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/95622" target="_blank">📅 15:06 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95621">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZbHprvJj319ehSU5kIxDPcMGzjTmPbheFmiAk0qjVpuh-R1CmgtR-WwAlHSNHTwp7QrG9z1kKA8jjnkWhIOKTGBTFyidz0vQJ2lhW8GjS8Rrje7SPadEX9ts4r_9dCrbS1p6OcDYvYZvd6jMqzDwc46VX7hcq0mnWdGbmrmlSMoG7PD5IynacldwLnNOXOJd_MlHN97McHSpWpr60QbU7pQFZorHwOaRu6zZP4tC7zp1yKsPI7WtfzzBUmtU_68Upfry85TKQEV6BISMb7nxmlfTZl4gUvZQFTo39c36uMGDVFj30VS8cdef8PP8sqKDw3syJIGyhUN5DvM9iqSFwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
بانوی‌ایرانی حاضر در استادیوم لس‌آنجلس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/95621" target="_blank">📅 15:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95620">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99e258c37c.mp4?token=mxHwVwU_fCOzsZjgcfyVl12bVyi8mWL87ZADdsGuVsMAxoIoKsr0hxefeY3eOR4yUHAEu8z3prwd3vMG-fv0GSyp_smPHChAq9_Ry5r3vgZzZaT5bAht7j2QwFb9BmitJNIkbTB53pRcfSboU5OvCJazs0w-o7nKmeFTdxprtsl1TpQkJ-I40pD0pPesp4dVdbwpLyw3e-pZ03ImTGlq4-Gd0y73nz6JNuJb_6G3QwOVYvIZAu5sjIittGyOiMZ-V2QVhs8pduWtu30ENoRVV0Iy_kt1PSRFiTqbPco5mh7vfo0aWclTKiIFMn0qoSH6VnlRKXuHJ_ikVIdGQQYFgTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99e258c37c.mp4?token=mxHwVwU_fCOzsZjgcfyVl12bVyi8mWL87ZADdsGuVsMAxoIoKsr0hxefeY3eOR4yUHAEu8z3prwd3vMG-fv0GSyp_smPHChAq9_Ry5r3vgZzZaT5bAht7j2QwFb9BmitJNIkbTB53pRcfSboU5OvCJazs0w-o7nKmeFTdxprtsl1TpQkJ-I40pD0pPesp4dVdbwpLyw3e-pZ03ImTGlq4-Gd0y73nz6JNuJb_6G3QwOVYvIZAu5sjIittGyOiMZ-V2QVhs8pduWtu30ENoRVV0Iy_kt1PSRFiTqbPco5mh7vfo0aWclTKiIFMn0qoSH6VnlRKXuHJ_ikVIdGQQYFgTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل‌زاده: ایرانی‌ها در خارج از کشور خیلی به ما لطف داشتند و جوری ما را تشویق کردند که شاید بشود گفت جو استادیوم لس‌آنجلس از ورزشگاه آزادی هم بهتر بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/95620" target="_blank">📅 15:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95618">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFK9x0DqICrpQOZtJ1c4hyssjnuF0GUjFN71nx_CRYbPZjnvLO2u5AO2-Nc4hNnUX38hXzRBCPzhaUtMWZX0juQKya2ZIeXDtej2jrsejtt338i1gyCGc_xUt05KiyXqke_AASyfHCRFCbtw74uBJWAcwkjNmMOoMllJlzSKF8PP1viQJ1re6qUysndFhP3Y0fpLqAVduG6Huff7IL_XeqLgAOgNz87zSAhW58d5vHYvIfhOSQ8WWddl9On86u-TmmwDzmxFHzbKbGCDnfSiK7_Yogxi2zKRJTgN41svkQzHrwbT8aCirzsWtM4k0BCvyHi8KAOaB-C5fkI46eMTHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◀️
تیم منتخب هفته دوم مرحله گروهی جام جهانی از نگاه هواسکورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/95618" target="_blank">📅 15:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95617">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a274e0a122.mp4?token=sr67tATcCCIaa67LopO2jijFNr-dT7DrG1_C1ml5DzQFf9cH7Nm-nXrAbMuOZi1JswX6po1vJsOUjMh7wijKhxNTmDAUSzcOEYPCbLwsNNaIwP8dzXyslvrpeJGgoERdfNwtxWLzaUqz0WFf_paWlmHA7bu_cYKe2Bk8J6jjK3o-Zpj_rxODFzAEhjcm5FlU3GhciW76eYX46uEqqVD9bkLxZXi7dEG06QSq0qhnnedYqOXDP2kV-cIyRxAfLfJT2MWOPj7WgBzWlnWHlnAjOghEasIjkKVgRGNGTFqdPWkBvU0PXR2A0gcU0A-eIgn_U3tBi-cbmQaxqiojbCSx7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a274e0a122.mp4?token=sr67tATcCCIaa67LopO2jijFNr-dT7DrG1_C1ml5DzQFf9cH7Nm-nXrAbMuOZi1JswX6po1vJsOUjMh7wijKhxNTmDAUSzcOEYPCbLwsNNaIwP8dzXyslvrpeJGgoERdfNwtxWLzaUqz0WFf_paWlmHA7bu_cYKe2Bk8J6jjK3o-Zpj_rxODFzAEhjcm5FlU3GhciW76eYX46uEqqVD9bkLxZXi7dEG06QSq0qhnnedYqOXDP2kV-cIyRxAfLfJT2MWOPj7WgBzWlnWHlnAjOghEasIjkKVgRGNGTFqdPWkBvU0PXR2A0gcU0A-eIgn_U3tBi-cbmQaxqiojbCSx7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
‼️
خداداد: من خودم چک‌زن هستم ولی میترسم عابدزاده به من چک بزند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/95617" target="_blank">📅 14:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95616">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9BbG04fCcPs7xwqeExwLtipz8aoQK5VKCzAcCKwb1ZlYCGJZgPFvXAsumST-Wyou6Bw0BFnFxCgRVJMdU4oWtuYlcliEavBvdy0K3mJB3NOmBIaDLjBUJn8_NmOf3spShvHWGiuhwoAne0cBCCsa9bTJLO9gVozp8Nx9ArQlDempZokPdOJtHsJWMIBUUnrkfhREVaEeVhH_NOzx-PkAqC4fldRzqw8_IVF1zOjBqxAJ1oeYUVli4EjivuYUU3xnsXNt9lyH9vXBzSliVXTIGBgvaUq2VgLy5jZ3V_LT08LC3mHhGK4_wenrPTu-JbZ4ZrG2sHGtMiElrZ_Y7ncOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🔵
خبر پیشنهاد الهلال به دمبله صحت نداره و تیم عربستانی خواستار رافینیا شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/95616" target="_blank">📅 14:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95615">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3892238805.mp4?token=OLnKS0phTNxg-1AdAB-TuY0BvoIUD193tZ0oBhwcKnJOLMF5dnovc3L2dxsG6AcC6T1EYm3WlfA9ouQisxNVIjLdrfywEN_f2d2pBPOK_7FwiR21iL2u_Z3ebk8XkqlHjpVBPG_04SzACjp40S5g9iDtFd821DUO7DLe8LXCRrF1MEnqCEkuq0HLu3TsQfYSmCXS8b1WJYTDayHMUF8NoxZGmuNkMc5R0R022Y09hLNwa6865PVbUrcsBgLgSgt-exk-hJdxGNSGsBVSnhFUb0XeJcr2Dh4hWfb72eiQlZfGZA5rZ_1t14O0Eprcygw7yjaTQ51AO5z4HCMDXe1kHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3892238805.mp4?token=OLnKS0phTNxg-1AdAB-TuY0BvoIUD193tZ0oBhwcKnJOLMF5dnovc3L2dxsG6AcC6T1EYm3WlfA9ouQisxNVIjLdrfywEN_f2d2pBPOK_7FwiR21iL2u_Z3ebk8XkqlHjpVBPG_04SzACjp40S5g9iDtFd821DUO7DLe8LXCRrF1MEnqCEkuq0HLu3TsQfYSmCXS8b1WJYTDayHMUF8NoxZGmuNkMc5R0R022Y09hLNwa6865PVbUrcsBgLgSgt-exk-hJdxGNSGsBVSnhFUb0XeJcr2Dh4hWfb72eiQlZfGZA5rZ_1t14O0Eprcygw7yjaTQ51AO5z4HCMDXe1kHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مردم بنگلادش که بدبخت تر از ما ایرانیا هستن، این روزا تمام فکر و ذکرشون شده مسی
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/95615" target="_blank">📅 14:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95614">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRNDH8IpUKf6Og99R9SeLlUyY9tNXH5urBg1wgahTbXPvb-1mhCo1309mQ571_vywvNRvFoEfrewgU7Gg4CGd35jdZ2U-PZCfIrNl_JY33TluW1fZYNv7BZoLm8LDn8rckBkdd-4ELdp5EQLpOoP5QAJk0zVRVV3I-QdvlXjnMI4X9nThyE3hXl-E7yMvLAq7O_UMp-wtESQ9-5ojs-j0iLvXMH8q5ekXEnXrmKsIURZgJdM7PHz9lRzTWLypnfwmZL0k09L_pgIjMxhRsq0ihLfkzieBXWWaoPkmYGQV_UPaYlW-GW3-6cftalg1kCCpJfs8B39ywx4Kz6ZYsmNjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💋
📊
لیونل مسی پس از پایان هفته دوم بیشترین شوت در چارچوب رو در جام جهانی ثبت کرده ؛ ۸ شوت که ۵ تاش گل شده
‼️
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/95614" target="_blank">📅 14:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95613">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8e892beb9.mp4?token=pKcL8XhfYZYrpqetMWjbnTvXMT1gkGz006CPzOX5dMZ3CTahNDlrpsnJ4dC1nH8PzXnow4Y08rWkF2LXWl0zCRGpJKLsUrgIlHwp7cl8j1Csf8Dfn9u_9r7vnAcoe311Cyi2wp1_HG064QpihHlHMOBoYh0GwuMfYM82ROdAq3JcR2iWQRDhBGQ680hORJD77jNnZp2u_B4ZMPxsrMgwo6p0UJDAcVREOkt5Ep6CbkrpBgMma8faBZObJYu75oLiobByZV_PHhsPEeEj3xg3rUSztOV-IZ130yyPX1FrGKPvJ2T5TufC1gW8Fa8DIV5OOf8UrTxZV7PgaIUQjcYGZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8e892beb9.mp4?token=pKcL8XhfYZYrpqetMWjbnTvXMT1gkGz006CPzOX5dMZ3CTahNDlrpsnJ4dC1nH8PzXnow4Y08rWkF2LXWl0zCRGpJKLsUrgIlHwp7cl8j1Csf8Dfn9u_9r7vnAcoe311Cyi2wp1_HG064QpihHlHMOBoYh0GwuMfYM82ROdAq3JcR2iWQRDhBGQ680hORJD77jNnZp2u_B4ZMPxsrMgwo6p0UJDAcVREOkt5Ep6CbkrpBgMma8faBZObJYu75oLiobByZV_PHhsPEeEj3xg3rUSztOV-IZ130yyPX1FrGKPvJ2T5TufC1gW8Fa8DIV5OOf8UrTxZV7PgaIUQjcYGZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شادی عجیب هوادار آرژانتین بعد گلزنی مسی
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/95613" target="_blank">📅 14:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95612">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/013e39db64.mp4?token=PWHUJTOpjSrlT_pXSu85jI1XBT1OkFNfhleB9_NUWmVJxABLW0gh-2vxdFKYblkQuwRmIC1LBABTNJuCkQ26fd4GyzJdheJfE8uXYnbAHNqPBV_XGfE5aWJG94OX7IjeYw-kDCpNHKs0Ju1uF5rt3vE4JNPIxM325-f6WxLRc8okNzss89v3-rQKqmald2dB1GspyC99RrrK5XxzH0fI3-MCDOt_6QnSGUiPQmCn_Yv95K0qvUG-ts5H8QVWcqQ0ybkXobw8WwNET8xA02qKJwBJIsCJU4oLIzqSKp51nCs7qlPpzQcwT4dpjK06Wjk3MF_eh2TukDCcD_3IRbn54Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/013e39db64.mp4?token=PWHUJTOpjSrlT_pXSu85jI1XBT1OkFNfhleB9_NUWmVJxABLW0gh-2vxdFKYblkQuwRmIC1LBABTNJuCkQ26fd4GyzJdheJfE8uXYnbAHNqPBV_XGfE5aWJG94OX7IjeYw-kDCpNHKs0Ju1uF5rt3vE4JNPIxM325-f6WxLRc8okNzss89v3-rQKqmald2dB1GspyC99RrrK5XxzH0fI3-MCDOt_6QnSGUiPQmCn_Yv95K0qvUG-ts5H8QVWcqQ0ybkXobw8WwNET8xA02qKJwBJIsCJU4oLIzqSKp51nCs7qlPpzQcwT4dpjK06Wjk3MF_eh2TukDCcD_3IRbn54Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بلاگرهای کف‌خیابونای جام‌جهانی رو می‌بینید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/95612" target="_blank">📅 13:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95611">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gef3VwsZJyjTRS8LmsNrvtHDFgmbJsNo8UZtVJzYd990I-VR4FJhm0hO-D0QPZdgxVhgzangtmssRIn_RoNMeCqD7gng_2VzbSqDpP7aI0YQATZsnzbi5u-ElkrG-Ccp_njTjEZKpmxduODKSvOGSSW3i08hhU7zgjvQwxqWKTDyRNPjZI6H06H8B5iHln6fEMf6GDO986qWvNEKn4ZKXyKgKx-DyvRDVIHismG3Wqv_7rKzCUqrthhaYHIpqh1Hucwe-R1IpCjQeooZGse7lsf5C2EUNXBxKCsyejhxCn9CBg23u3ZiDOepMa_7dyugjMZ-uteOghcP1qMTdJiJBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
آیا میخوای چند سال دیگر به بازی ادامه بدی؟
🎙
لیونل مسی: "بله، بله... مدتی ادامه خواهم داد، تا زمانی که بتوانم کمک کنم، احساس وضعیت بدنی خوبی داشته باشم و به هم‌تیمی‌هایم کمک کنم... به بازی ادامه خواهم داد."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/95611" target="_blank">📅 13:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95610">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbB5t5bvUxUtZPzzU-BuqyOh_H3e5GtYmwZWr9mhFfSsIDa5NYDYPBOiboqm8PUUYfHTNnc7dsMJXHQhqVV5IHGDSqiYeUhUBL5arwa2y9P1GR-18VN2xpAIMrTFbTOQx7rGeSYwQ5p0DQaxRCufpnZl6UPHneMoEEEG6D0ZbflOTox-gUSE1rY77CZySLdOobQrgfF5Je6bupgXc-dN0HMnYl15M-tL2aa6Sj0pcMoD-Pv_V4QJqg7ypu0UxVM_yu0j34OaWXd_YUKXDJV9gq71AoHvB9r_RB_4cSJPM6exKYZTFPCwrUvTsaBJFh_Vkiv9Zxb9pFVm1E-wL8ecYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
ماریو کورتیگانا:
مورینیو دوست دارد باشگاه رئال یک مهاجم نوک کلاسیک شبیه خوسلو جذب کند، اما این موضوع فعلا اولویت اصلی نیست و برای عملی شدنش، حداقل یک بازیکن باید از تیم جدا شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/95610" target="_blank">📅 13:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95609">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fgivY98dYHu1aP4qO9WvICXDPSXjV3I-8J0bEYWD2QXqmtCe7u2ilpFgDtpfo4uunS7Ritz-JeRA1i1aFbcyPhki7HWgHMKLyG4lcOtoiJS_fCjONKxF-mAHbvf8owXRwpG0cMkQgjm4HwF0hFmwCSvDBF6DFGS9IcA0MX3LZhDn8QKNDUUSvAhNysaSForwzNb_DCDdek_eVHTe4cJhpwcNi2NkZhLN1RZyyOW6H-aEwYkARHaM6YDqBElh3SOGW2kDc-lyakG0hGWV2WrYpf7aijeN0NdpCwKapWYUyjcA1jdVgJM4XZ05_T0Gy1RRtuGNf6f3M0N7GpY5rkrp0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">7 بازی آخر مسی تو جام‌جهانی
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/95609" target="_blank">📅 13:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95608">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97d2bcd8ab.mp4?token=BeWL7FsQDwb39M-4BLqEyhP8HEEZVIaLirm-qj5aPnwwvkucudC9n9od4BouFPT2lHz56ef84YR123Ol8MgEdoplBQWizkOfa6qKKDwmXsNmplb4wuenjzkxLa6jHTG_HidWXxiwpA0AxmV9oMvsVIZ1I5bV0shXOwjbuwArJEmAVdb7J2n6iqlgrGrOq4s_09Jzosfx1xmqUNxzeseALojwTj3eItRg1Oi3y-A2drGyWb8lq4s1nWe8Obk6XKf8dc-O4Z-jxZwR6VvUVFfD_j8h16x6oYOpJMiUb0yQQkTVIjSLpSjlHD7_exm6C2UQJfCXL6gKNF2Cv84d_ZWjSkMkPJ9pOqMQEVh1iw7m7_QxTMEAWYLwNpZP8_i2hkLDQ0JIc4zsFTWMrrcgIsPUq7tO0LFZsKm7R4ZsR0eontF_TBiFFAcoVPHOw_tqHCOKOSqDYsx5xNR6NuNEwABrNjsYY9FeLpCUa0XuOb602BgaqqjkgVRYo-KzT1N_Ledf64iKNrF4S__z7HbTMrjuH838ZXFx4AMpssgIHcI_G9T6-2e6Scax9-uXpRI4ZnMoSHGR6SnP6od1OXzMUZJ-f_o_L27_S9gOGe-gJu4_uVWnWPGPZ2c1xHIHBRNAlgx87Js2X2adywu-7DVjE1XaxsVI5aEMliqL1dwMXBV2ojs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97d2bcd8ab.mp4?token=BeWL7FsQDwb39M-4BLqEyhP8HEEZVIaLirm-qj5aPnwwvkucudC9n9od4BouFPT2lHz56ef84YR123Ol8MgEdoplBQWizkOfa6qKKDwmXsNmplb4wuenjzkxLa6jHTG_HidWXxiwpA0AxmV9oMvsVIZ1I5bV0shXOwjbuwArJEmAVdb7J2n6iqlgrGrOq4s_09Jzosfx1xmqUNxzeseALojwTj3eItRg1Oi3y-A2drGyWb8lq4s1nWe8Obk6XKf8dc-O4Z-jxZwR6VvUVFfD_j8h16x6oYOpJMiUb0yQQkTVIjSLpSjlHD7_exm6C2UQJfCXL6gKNF2Cv84d_ZWjSkMkPJ9pOqMQEVh1iw7m7_QxTMEAWYLwNpZP8_i2hkLDQ0JIc4zsFTWMrrcgIsPUq7tO0LFZsKm7R4ZsR0eontF_TBiFFAcoVPHOw_tqHCOKOSqDYsx5xNR6NuNEwABrNjsYY9FeLpCUa0XuOb602BgaqqjkgVRYo-KzT1N_Ledf64iKNrF4S__z7HbTMrjuH838ZXFx4AMpssgIHcI_G9T6-2e6Scax9-uXpRI4ZnMoSHGR6SnP6od1OXzMUZJ-f_o_L27_S9gOGe-gJu4_uVWnWPGPZ2c1xHIHBRNAlgx87Js2X2adywu-7DVjE1XaxsVI5aEMliqL1dwMXBV2ojs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل‌زاده: علیرضا بیرانوند وسیله بود و دست خدا بود که اجازه نداد شوت بازیکن بلژیک گل شود/ در حق بیرانوند خیلی نامهربانی کردند و حالا کل دنیا در خصوص بیرانوند صحبت می‌کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/95608" target="_blank">📅 13:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95607">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYeUJCdcdHT0W_5ukCJPB42aIJYfnJRymqZKJzaX1J8hC0QrtDSxxsP5RA2emUPTAxxDJmueSDQTdHi9tOlEyjx30TxH4Fq2iNDgzYcZaEjKnvS2ksYzTbst0zU0Gs_4_GS8HS6hwUlJaXtBoh8WGt0Q4bnd-oylW5TV564RrLEaVOJD7FVF7nZaaflUqva6GoMGbQRBzU-hzKzKsvBfQ5Jsr-coLCiVFpBJtLuvNMRuF2d8r0RAcrhqx3fE1tZcwrRxpKGZckxXtXdqmJrz5oxII9_4l1kkG1pnql2np-PJ-3wBA0UOWiEtA8Vzkfz5cVc0bu6fIUwwOA0PFoXomA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🏆
🇦🇷
زوج آرژانتینی با یه بچه تو شکم اینجوری رفتن اسطورشون رو تشویق کنن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/95607" target="_blank">📅 13:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95606">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5b5dc5848.mp4?token=Cm28Cf7m_0AlW1m9HbAg6i_VjyQWLU5fb9pQu404ygraB7uDSzVbww6Tbopymo8p0JBm1YdwgBMDY6r22tTkzehxpaDb2tBr-3f3bvj1LtYnJd655TGsk5a3INhFRkiyCmFXoTtq1pZoXDdzIzh_zRd1CblCpOjCutZwp4uFJgWs75rcHtZUKjZnR65pwAtEXSfZ6V6GZhTG3Z4g5uhyb5Vpwod_xxK-j7g32NylrynpREmdO9Q-QLOuc-WV6gAG4-fWyb16GequGZr-9DjzzWeHSQu9hRA8ZKDXRxV0lu7f1PrcLFvCInOx0Qo9cCVgWwZhvdihDT1-CP6dpsPFw5hO5tPqqQySpsy8oFm5UEwwGFqqLNV__zsEB6qdAaMlb-pX8bmeOCZSB3fmlLTx_k_Jv_5Mh9EU11MW5bogXLAYrACszfjr67LQaLtkLI-4svD_aAaTKMeabxzScWjLE-xjl7n9gCxLsljJ50L6Ko51vv_crZ2L1gcfKUUbYsH46OuhjrG46g25N7mPXSR5skTXRXBbEsBGZKAjV-iJrn8l3qNuFN5QxcXyDcLve1bDRZK2jdNxZ0E9SzD2IzvXmYazGk0_Ko3BZgzb_rXQTZCmuFtuZ-Bik-xBcRjX4Qi5P-g8Wy-zWKVrcjQ46jAia7OsAtaf1mkGRXNXCmJj5Nc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5b5dc5848.mp4?token=Cm28Cf7m_0AlW1m9HbAg6i_VjyQWLU5fb9pQu404ygraB7uDSzVbww6Tbopymo8p0JBm1YdwgBMDY6r22tTkzehxpaDb2tBr-3f3bvj1LtYnJd655TGsk5a3INhFRkiyCmFXoTtq1pZoXDdzIzh_zRd1CblCpOjCutZwp4uFJgWs75rcHtZUKjZnR65pwAtEXSfZ6V6GZhTG3Z4g5uhyb5Vpwod_xxK-j7g32NylrynpREmdO9Q-QLOuc-WV6gAG4-fWyb16GequGZr-9DjzzWeHSQu9hRA8ZKDXRxV0lu7f1PrcLFvCInOx0Qo9cCVgWwZhvdihDT1-CP6dpsPFw5hO5tPqqQySpsy8oFm5UEwwGFqqLNV__zsEB6qdAaMlb-pX8bmeOCZSB3fmlLTx_k_Jv_5Mh9EU11MW5bogXLAYrACszfjr67LQaLtkLI-4svD_aAaTKMeabxzScWjLE-xjl7n9gCxLsljJ50L6Ko51vv_crZ2L1gcfKUUbYsH46OuhjrG46g25N7mPXSR5skTXRXBbEsBGZKAjV-iJrn8l3qNuFN5QxcXyDcLve1bDRZK2jdNxZ0E9SzD2IzvXmYazGk0_Ko3BZgzb_rXQTZCmuFtuZ-Bik-xBcRjX4Qi5P-g8Wy-zWKVrcjQ46jAia7OsAtaf1mkGRXNXCmJj5Nc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداش یامال شاهکاره
😂
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/95606" target="_blank">📅 13:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95605">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srPT8VmAf76DxD_NR9BxmK5JmX-5mlvNPgBg-R6Dssa8s3mDrvuvmOY3kDygZOk87JeoW5FXdHEbiSFmqWMZ5-O7vCP8wddcRYEl0I0tn7yEMshFe6pzQQEGqoXjtvGo6eFoEe1tab73X6NtDtqypsL9qJfqKYyvplcs7Ansi3R7kJhVLd15blih-QT-u6mFuPeS3UOdVH1dbvptqVn7d40v7abbWTPbTeduUU_CkhQ-datFfQPXe6qdhGeO7tGZXldWeaqHRkzdh1TDfUSA83TaOqtHIAYyvI1GlgtpBr1YkB7d3ixBL3tq8VhfAl1lknWTE2HN9Jt-wttYW805Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد لیونل‌مسی به تفکیک هر دوره جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/95605" target="_blank">📅 13:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95604">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">💥
🙂
یه خانم ایرانی از مراحل استادیوم رفتنش در جام‌جهانی شامل حموم رفتن، لباس پوشیدن و ... برامون ویدیو گذاشته و گفته ببینید
😔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/95604" target="_blank">📅 12:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95603">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdb84abe0b.mp4?token=Jn9rxb-jDd5RCRKCydnV4X2U6gh3xlhvElPqWXpOV2FxBErMQA7Zgf509V1F54-onKlibYcpRsfPCBetiSAY9_CN_CBxBVVONQyke0z1QAEOd0x_zRjvuqXLassX2EkBmvXkewAcK8HJqcEFOXKQSNdK5i2p5AQJpdU3j_JkROk8cYgOHFLM5SlQzUr_k9sW5VLhSaj9jws65oAUIkQLbuGu4C70mU5NsQNzxF4DUh7DBqYY_i6bq1N2Fe2uKArqMFUZoPmFhZoE4-CeMY65gPlJHVGmbomRPe7LD_cianxst_J2gSyrxRazl15WhCYUph6GpgDEMK0aGGu2RcFFmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdb84abe0b.mp4?token=Jn9rxb-jDd5RCRKCydnV4X2U6gh3xlhvElPqWXpOV2FxBErMQA7Zgf509V1F54-onKlibYcpRsfPCBetiSAY9_CN_CBxBVVONQyke0z1QAEOd0x_zRjvuqXLassX2EkBmvXkewAcK8HJqcEFOXKQSNdK5i2p5AQJpdU3j_JkROk8cYgOHFLM5SlQzUr_k9sW5VLhSaj9jws65oAUIkQLbuGu4C70mU5NsQNzxF4DUh7DBqYY_i6bq1N2Fe2uKArqMFUZoPmFhZoE4-CeMY65gPlJHVGmbomRPe7LD_cianxst_J2gSyrxRazl15WhCYUph6GpgDEMK0aGGu2RcFFmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای‌مسی ببین کاراتو دل کیارو بردی
💥
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/95603" target="_blank">📅 12:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95602">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44b24eddb0.mp4?token=oRdx6AJlCOfNnxsB-hpUX0EgFXeXC83wKsTQ2Hx8Zbg9adD2c_tGzCagNrn1ryZM5NKkwQpkHT4YauO3lTMpV7AX-BjE-OioI55s-bKHrwTaEVd9RU0wMPRzMxIQ0WcfhE9wH-IwsEaDBC3z9gNFkhOXMruMbbOeATm_WIezLhHry8Q0c0VDnG-8pGYWy_GZF8yAK2quLMCEy4rdLwVkpMJuBv2QVondwcU40nSaxp-jl-RWkG0htZ9kXayQNbrvsCfljN_WfpbbAoAElCN8059tn8BPMBbFt05PM5w31HwuhWoPzQjfw8lGRcqC-O6Yyd-MS8le-iwCK5rHTqezzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44b24eddb0.mp4?token=oRdx6AJlCOfNnxsB-hpUX0EgFXeXC83wKsTQ2Hx8Zbg9adD2c_tGzCagNrn1ryZM5NKkwQpkHT4YauO3lTMpV7AX-BjE-OioI55s-bKHrwTaEVd9RU0wMPRzMxIQ0WcfhE9wH-IwsEaDBC3z9gNFkhOXMruMbbOeATm_WIezLhHry8Q0c0VDnG-8pGYWy_GZF8yAK2quLMCEy4rdLwVkpMJuBv2QVondwcU40nSaxp-jl-RWkG0htZ9kXayQNbrvsCfljN_WfpbbAoAElCN8059tn8BPMBbFt05PM5w31HwuhWoPzQjfw8lGRcqC-O6Yyd-MS8le-iwCK5rHTqezzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👍
توصیف عادل‌فردوسی‌پور از لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/95602" target="_blank">📅 12:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95601">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d01060f01.mp4?token=tUIb6pCb5016XgWJIUB0w2DyCJYZQdUTmmVj6H5ixBivB58AG2hN92K9vIdWSPAFwxkftld4BYEeiEgFNWoufk4Sz77AWRjtah7-FdZzBKg4P01BasH7H8LQBuOIKRbtXJfNL6YJhXQVAhRYo7WU25NCaeWNc2USj6Bml9Ugs9twlUk5b_d6GDxM6bHEEyCZuvy3DkdzorwqKEVAzTE-CsSWh_oFOEW9fr2bYWvIA4iOmdN51EUAbQ5QzInGg9JBCHgUrgxEJGt4ERHOXllfvaYiEN23T71kBVaIzxNxHt5Dk3VeR-o5Gyo3ZT-jQmPWN1e4uKjFzloC6sxOBZI-VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d01060f01.mp4?token=tUIb6pCb5016XgWJIUB0w2DyCJYZQdUTmmVj6H5ixBivB58AG2hN92K9vIdWSPAFwxkftld4BYEeiEgFNWoufk4Sz77AWRjtah7-FdZzBKg4P01BasH7H8LQBuOIKRbtXJfNL6YJhXQVAhRYo7WU25NCaeWNc2USj6Bml9Ugs9twlUk5b_d6GDxM6bHEEyCZuvy3DkdzorwqKEVAzTE-CsSWh_oFOEW9fr2bYWvIA4iOmdN51EUAbQ5QzInGg9JBCHgUrgxEJGt4ERHOXllfvaYiEN23T71kBVaIzxNxHt5Dk3VeR-o5Gyo3ZT-jQmPWN1e4uKjFzloC6sxOBZI-VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🏆
اثرات‌هنری خیابانی در ایام جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/95601" target="_blank">📅 11:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95600">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e418f52b9.mp4?token=T6lI7GwVmzf-mcKaM2-7uzXhdB-1dBWWg9triviatCvaP2oa7zkPR79wV5nPbS8IkocElhfJoPH9oVe3BWNutOmoALFZhPo2B8GoZ9R3CM3LorK_P7W-u7A6x1mljIsPXLguVapnRUTjv_Y78solvHZubH-kdQBOkEo3D07suneu5Qsf--OSJXfRaA3rJZoSr4hILu2kxuHhsFPSU-DNL0jT3Gm9s0INqWgpDxh3hB5zzbDZQ_vmKJiPAw-WtkhfFsbHzmOp16wU8Br7-A75SNh-EiEocPT3KE8YUHew-gb8AreNAYXqr0wMEsDbrhNwNVn3yssLDPxy8giIST4hew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e418f52b9.mp4?token=T6lI7GwVmzf-mcKaM2-7uzXhdB-1dBWWg9triviatCvaP2oa7zkPR79wV5nPbS8IkocElhfJoPH9oVe3BWNutOmoALFZhPo2B8GoZ9R3CM3LorK_P7W-u7A6x1mljIsPXLguVapnRUTjv_Y78solvHZubH-kdQBOkEo3D07suneu5Qsf--OSJXfRaA3rJZoSr4hILu2kxuHhsFPSU-DNL0jT3Gm9s0INqWgpDxh3hB5zzbDZQ_vmKJiPAw-WtkhfFsbHzmOp16wU8Br7-A75SNh-EiEocPT3KE8YUHew-gb8AreNAYXqr0wMEsDbrhNwNVn3yssLDPxy8giIST4hew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
⚠️
پاسخ پیروز قربانی به اظهارات یکی از اعضای کادر فنی ایران که گفته بود: «شانس آوردیم فجر سیاسی تو گروهمون نیست وگرنه کارمون برای صعود خیلی سخت می‌شد.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/95600" target="_blank">📅 11:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95599">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/428b85f0a6.mp4?token=P2Y79AJLZXFyUaAlM3CesDnfg5SKKPnoh2CTD__2WEWp-VJt7CldJm9WotLdiZ6FTF2ehd0qDqzsZVC4TG9XB1E8MO6YvDXXmcNzEl34Nun5hJcJ9aFXI-Bgz9c1o9oae5eOgC_PutIuidpx1aaXE8y-xDiW90RY9wXrD2NtUWQBhBHcIpLO2HR_gxjj1c-MeMd89Cp9yJnWOEVKEGYFBJzYgIHMqiEJ8x3AzeKR9i6nKQioFZewk-fPUBfMavMCONng5zJs6EKe3tCwIlu-iy9GzsxzfkNXr4hZNrJSkKEy09JDA9cwYvh2W6C180jXBKc4XXMLly3tE-GmoA60jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/428b85f0a6.mp4?token=P2Y79AJLZXFyUaAlM3CesDnfg5SKKPnoh2CTD__2WEWp-VJt7CldJm9WotLdiZ6FTF2ehd0qDqzsZVC4TG9XB1E8MO6YvDXXmcNzEl34Nun5hJcJ9aFXI-Bgz9c1o9oae5eOgC_PutIuidpx1aaXE8y-xDiW90RY9wXrD2NtUWQBhBHcIpLO2HR_gxjj1c-MeMd89Cp9yJnWOEVKEGYFBJzYgIHMqiEJ8x3AzeKR9i6nKQioFZewk-fPUBfMavMCONng5zJs6EKe3tCwIlu-iy9GzsxzfkNXr4hZNrJSkKEy09JDA9cwYvh2W6C180jXBKc4XXMLly3tE-GmoA60jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🔥
خاطرات جالب کاکا از حضورش در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/95599" target="_blank">📅 11:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95598">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da82d3a5fe.mp4?token=EIcQKramfZsaFPvPdzM2E6lbreFZflHTAPKtwrUkD0Wt6KtWlhiAfbtRZGeXjrgdrR1vA-OdUItbbW-T1C_YgfJ-5f5ncV7vb1aiW-BwbQYgYQx_hfnF0k6KJDwDsuVFcy7tEyQSC8k4N8Jerz8J0UVdbgMxQY-0y7hc6lQd08ZR-VXSLrJ681-3_bFTbRTQ7OGSb2NZ37HSjReaohiKQviik57Y3AEk7KVMhjUcpHMX_pjwQdmdSuDbjIGeExfhkk9xb3hFnlOO0KrZ_WU874oTzhRNK7nmS7lS6IgjRLuLNteBHVs94dmj8ARLIMDv1iqKe9e7EcMLjwBhxpMM7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da82d3a5fe.mp4?token=EIcQKramfZsaFPvPdzM2E6lbreFZflHTAPKtwrUkD0Wt6KtWlhiAfbtRZGeXjrgdrR1vA-OdUItbbW-T1C_YgfJ-5f5ncV7vb1aiW-BwbQYgYQx_hfnF0k6KJDwDsuVFcy7tEyQSC8k4N8Jerz8J0UVdbgMxQY-0y7hc6lQd08ZR-VXSLrJ681-3_bFTbRTQ7OGSb2NZ37HSjReaohiKQviik57Y3AEk7KVMhjUcpHMX_pjwQdmdSuDbjIGeExfhkk9xb3hFnlOO0KrZ_WU874oTzhRNK7nmS7lS6IgjRLuLNteBHVs94dmj8ARLIMDv1iqKe9e7EcMLjwBhxpMM7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای‌رونالدو بالاخره دختران سرزمین‌م خوشحال کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/95598" target="_blank">📅 10:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95597">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2607379b.mp4?token=JyPR4ZpsvcpaWA0AYDYas9NGFCZiiDp9vFAsOJL6G7_kLVT92tm4RGTu2grgPoiGNm6fprf7Y8rBiDnOFp86NOn_4HUMiqN2idlI2p_Nnwfw27msbsXPdWW-i_WzG27D3y9TUNO4RNM4oOwcrd9IfdYxLRktNDzHADoo3PonjmMglxNg5cQuKszJxtYbyP2FG_AjwiAdsJm59RaWIs9jgI28UqWEsRmcLXPdQI3BxWRTeDAdV222jCofK6PYPonbF1er2mNltyP0QRunuxo0LYvUKLKgSw9HYbq-nLQEXZ043yvw-iY7uaRi3C-qSDWekdTKizrbSqcqbyTzj3jPlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2607379b.mp4?token=JyPR4ZpsvcpaWA0AYDYas9NGFCZiiDp9vFAsOJL6G7_kLVT92tm4RGTu2grgPoiGNm6fprf7Y8rBiDnOFp86NOn_4HUMiqN2idlI2p_Nnwfw27msbsXPdWW-i_WzG27D3y9TUNO4RNM4oOwcrd9IfdYxLRktNDzHADoo3PonjmMglxNg5cQuKszJxtYbyP2FG_AjwiAdsJm59RaWIs9jgI28UqWEsRmcLXPdQI3BxWRTeDAdV222jCofK6PYPonbF1er2mNltyP0QRunuxo0LYvUKLKgSw9HYbq-nLQEXZ043yvw-iY7uaRi3C-qSDWekdTKizrbSqcqbyTzj3jPlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇶
#منهای‌ورزش
؛ ویدیو افشا شده در جهان از عیاشی و عشق بازی مدیرکل پروژه‌های نفتی شمال عراق با منشی خودش که مثل بمب تو جهان ترکونده. ظاهرا این فرد دستگیر شده و وزیر نفت عراق هم قراره اخراج بشه
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/95597" target="_blank">📅 10:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95596">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a6f6841f1.mp4?token=TKotApQPN7K5rR7pigk7iP2jeiIqnHa5VAbcQN98owedEFyZXKGNC4KkMI3hUNPbTctEwCP9qjTh0mp2k-RfW2SkcBXJ5g9TsGKR52R7XmvGGwtX9Yf2RaokWW2Lb_CNXWxww65HWUnUhMsI4VyJcJd_xJHQaN-K9L6XhZq4bvqzvKtX83OJeU3ts0KZlCAEqHTNNUX6ZEg8gTkzYYqZZmo9ahI7HzUf-Y69io9sXgTSy_kKjBy53aThu36UyclVGBtYYaqv5OWvy0LoZkpoZaym8WO4NSDqRqSDMBOGppg4cGe0ncAFc8Y4m74DNm7elc5EpUOLaLtzIIlTiS3Bkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a6f6841f1.mp4?token=TKotApQPN7K5rR7pigk7iP2jeiIqnHa5VAbcQN98owedEFyZXKGNC4KkMI3hUNPbTctEwCP9qjTh0mp2k-RfW2SkcBXJ5g9TsGKR52R7XmvGGwtX9Yf2RaokWW2Lb_CNXWxww65HWUnUhMsI4VyJcJd_xJHQaN-K9L6XhZq4bvqzvKtX83OJeU3ts0KZlCAEqHTNNUX6ZEg8gTkzYYqZZmo9ahI7HzUf-Y69io9sXgTSy_kKjBy53aThu36UyclVGBtYYaqv5OWvy0LoZkpoZaym8WO4NSDqRqSDMBOGppg4cGe0ncAFc8Y4m74DNm7elc5EpUOLaLtzIIlTiS3Bkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
وضعیت بیرانوند دایرکت دخترا بعد بازی بلژیک:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/95596" target="_blank">📅 10:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95595">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVSi-X9JX9Kueru6VzoZUa_1oAlaOf-2CBRWdmUtS-nv41Qu1x99YYtBf7wu-zBbFTNrBo6FVwlZJvCfd4w70erAt_-MlNyC21tjTX6ywpN8Trio8GP5jDBMfpQrDIlGh9rEMtq_uz-XsXncgpu-fg_qP4uy3knAlbTyDBHHqh5QCRx5s2-2TwA3VDjYQvAkteYXhcR4Ka0lFJJ0ptIjA2edxsWnQ53FksAW0fAJXU32MSLFF77Mf5ooduttdhR9JYIe60G0HqJnf7yHwmLM0uZchl4j6Lq6nyVRZTSv9TcsDAOVXmzFpSVb71jSq4QBr1BCrmc1hIRkTZk7DOtCmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تن و بدن بوفون تو گور لرزید
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/95595" target="_blank">📅 10:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95594">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acf00b678f.mp4?token=WN4n8FbLnWUS4dW6yvkB5C2Zug7MN4GpPmpCon55HKqxFCWmckjxnwpbRs7xIcQEdV59jbnQfJTpMDKyryPGIU_cuFybrWZY-ggnuPWm3L2gpquuxYHhQsVapBxRcKLjoY_B22PGouQYU957n1YFYkAgd6kNUfKjFyx8p4-Pxplhi_mGNrvNe_cC9xgTmxgJl9W0LgvUifOiNXajKSC2dJSsD3o6favrDLm-L6oBxYZtC3GtwpxQRMqiJBHiupU52n6guql4talzrb786iUSutCjixG8P3aovSYLniBv8U9Eu_VukalAkedThG7xsPQPt1IiROcdEZp3kNPTGNfMRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acf00b678f.mp4?token=WN4n8FbLnWUS4dW6yvkB5C2Zug7MN4GpPmpCon55HKqxFCWmckjxnwpbRs7xIcQEdV59jbnQfJTpMDKyryPGIU_cuFybrWZY-ggnuPWm3L2gpquuxYHhQsVapBxRcKLjoY_B22PGouQYU957n1YFYkAgd6kNUfKjFyx8p4-Pxplhi_mGNrvNe_cC9xgTmxgJl9W0LgvUifOiNXajKSC2dJSsD3o6favrDLm-L6oBxYZtC3GtwpxQRMqiJBHiupU52n6guql4talzrb786iUSutCjixG8P3aovSYLniBv8U9Eu_VukalAkedThG7xsPQPt1IiROcdEZp3kNPTGNfMRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
حسین‌کعبی: از ابتدا استقلالی بودم.‌ پس از حضور در پرسپولیس با برادرم دعوا کردم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/95594" target="_blank">📅 09:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95593">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/413019d639.mp4?token=bHrN2tZwKe18_0xG5eKxYJb_PRFocv7JMtWlOEE7uDI6XetcqfgnXV8_4ZYPakjO250QVAZnsHaZde9tlfbnf6oOdFU75NTilb7T0HwCrbv0hBNPoSwcFD0MCau5960TBLK-UlcVpMNq8c5ypr6BCOr2VAJGYMKdb1h8mU3VqquQxosucK7b_6f03xnUvwrBSt_YkRstKCbUGr-MS1L6f1FQ8fZy08VpjQPGsYh-PHCtL1QFFit73mKdKndAawejO_yIEcIyBXm3sosxvhmc7h9yWPHnRMzftoubgO9yC5Nvfub8yjgKPjaISaakPMgI5HMsW-BDr1DxSIfW_I_n6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/413019d639.mp4?token=bHrN2tZwKe18_0xG5eKxYJb_PRFocv7JMtWlOEE7uDI6XetcqfgnXV8_4ZYPakjO250QVAZnsHaZde9tlfbnf6oOdFU75NTilb7T0HwCrbv0hBNPoSwcFD0MCau5960TBLK-UlcVpMNq8c5ypr6BCOr2VAJGYMKdb1h8mU3VqquQxosucK7b_6f03xnUvwrBSt_YkRstKCbUGr-MS1L6f1FQ8fZy08VpjQPGsYh-PHCtL1QFFit73mKdKndAawejO_yIEcIyBXm3sosxvhmc7h9yWPHnRMzftoubgO9yC5Nvfub8yjgKPjaISaakPMgI5HMsW-BDr1DxSIfW_I_n6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">8
سال قبل در چنین روزی؛ تونی کروس از زاویه بسته دروازه سوئد را باز کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/95593" target="_blank">📅 09:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95592">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cab47625ee.mp4?token=Up1sQ5kqMjI-xpi_ncMKK9B0BflXyedWqg2uDkGJaUKa3hFq4xzuCYDY2_aMdz_VqLbhqB6xXPsaeeT-J6nk0Fm2iKX6vPtJKLaoPvK9IjyXYYEnDbasY0T_VPtzO5eQMfPmt6ZFT5O96wnav54f1GnYLVceumvaoAgg9eilpJiP33La6x0keX9y52fQE9yhQSaWasWGluNTGmLiQdbG-qjdbgBWtqUv_IVfNQbwCDWpMuBgwU7fwTCt9tud09iEQrXxvQQ8QPhXUICBDENBsx38svwgvthahg715OQf2p-aSylS4Zu7Fqtu9aUicROdMcCsNqXK3yzTmEJ10ej4DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cab47625ee.mp4?token=Up1sQ5kqMjI-xpi_ncMKK9B0BflXyedWqg2uDkGJaUKa3hFq4xzuCYDY2_aMdz_VqLbhqB6xXPsaeeT-J6nk0Fm2iKX6vPtJKLaoPvK9IjyXYYEnDbasY0T_VPtzO5eQMfPmt6ZFT5O96wnav54f1GnYLVceumvaoAgg9eilpJiP33La6x0keX9y52fQE9yhQSaWasWGluNTGmLiQdbG-qjdbgBWtqUv_IVfNQbwCDWpMuBgwU7fwTCt9tud09iEQrXxvQQ8QPhXUICBDENBsx38svwgvthahg715OQf2p-aSylS4Zu7Fqtu9aUicROdMcCsNqXK3yzTmEJ10ej4DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
پشت‌صحنه بلاگرهای جام‌جهانی
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/95592" target="_blank">📅 09:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95591">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69b286c983.mp4?token=dwWdd-lka9XbZvdm-WTxcfxNqsrhPufvm-24R1nw4JJO2CvggHjJW5104-Hk0w7ZWC_ceoboirGK2ThVyzWXDxvR5hscKXJOQpCI1HrfmvZBI4S2ILXMMiVWCXAaQoOLjDS6lysM4lwNLJ3Guuw1-nZHKdgz4PG0TCiNwrORhJXa3QDdSsoLhwG8nCveOlWHlsokrxwtjJNUOf8M0TWC3sUDujS-dK0d0bO9goGDeYCdyNhV9idmhU0tqQr55ibkW6ZkNLNXTTJ45vMzzdZg98iOFdq5X62b9nxndW9Xnh4vlU8fdIJnA8ynPBxSN5jNMqNTzrcdqsyBtwXioYLIDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69b286c983.mp4?token=dwWdd-lka9XbZvdm-WTxcfxNqsrhPufvm-24R1nw4JJO2CvggHjJW5104-Hk0w7ZWC_ceoboirGK2ThVyzWXDxvR5hscKXJOQpCI1HrfmvZBI4S2ILXMMiVWCXAaQoOLjDS6lysM4lwNLJ3Guuw1-nZHKdgz4PG0TCiNwrORhJXa3QDdSsoLhwG8nCveOlWHlsokrxwtjJNUOf8M0TWC3sUDujS-dK0d0bO9goGDeYCdyNhV9idmhU0tqQr55ibkW6ZkNLNXTTJ45vMzzdZg98iOFdq5X62b9nxndW9Xnh4vlU8fdIJnA8ynPBxSN5jNMqNTzrcdqsyBtwXioYLIDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
دختر ایرونی عاشق مسی رو ببینید و بشنوید که یه ذره بی اعصابم هست
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/95591" target="_blank">📅 09:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95590">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZh94vyhr4JyvJ3ZR4tYrJwvhm0LNdH5TumZDikP5_g4l1RSyoM8bCZyY90whlSJC3Pwm4G4btcK9UMdlMP_jdrC5nje1U7jtgzI7qQ7xaRUprprtnOP766R4XyPQsILoKSU0bfOZXs-ZrlUDbmeF0G8htyVanVULqL_CU5muI1_kClFZUkY0J9ZL7XJ4RdAxuMUHrHTi_Way7USROLKdhN28_rMXZZ8m_AzxhS0YNgimM6VpUpJUuHSZ9L3l2PG6cGdrqmixhr9j5LT5uKvKzUaO50myt8vpnOCm-TI2dMyQxOi5rC9OU_iYjs2N1cFNvCF9o9o9PJ92Kd6phBzBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
رومانو
: باشگاه چلسی طی ساعات آینده قرارداد مارک‌بالیسترا ستاره آتالانتا ایتالیا را به ارزش ۵۵ میلیون یورو نهایی خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/95590" target="_blank">📅 08:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95589">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_ZBUPk2jd1BJd-eLcoWEIh2yrAkidQ9ZQt2YjIlpKdeZBUQ9bFjEt4bLkvDGmlnlldDwe4MUF28SiSNa6cbZjh4DFkYQdzKJ4tznQJq7F9fRi2owY-8Cd5EeLH_kk-Wnl-Dat2um2D_OmUX9YO_roTRZ-flHTwV2My58z2fw77M7UhjHXbaY_pU1rSNZHjbhCtM0V5f6kagfAA_Qqp1iRYpvk9M547iYCzXxT1jbcY1JCv_bL9ADRlEKMGewUWYiZ8gXGUJruRpL_2yH4I-neFd-N8LpCjNF394nWeh4jAH-Czgm9p4RErhu4FCGEjZQfX2Ahj-oUGXjYRycf_v4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
📊
مروری بر ۱۲ گروه جام‌جهانی تا اینجا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/95589" target="_blank">📅 07:54 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95588">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uzxi7tclmeyp48QVQfjOUU_G8Vdv2OQG9j2Hjvu3uMis0eGLHs8TChS_s5A-pCpD4vSICOwFZ4BS96H2FOOKZ3d8yFON1t8mAyEnuuPdR0VvauSJJYnfRO3Kr2bWtUPlAyX2mihh2kMPi7iD3Kr3Mfnb4ejgJ5K4O2qUbCGoYkK-sB_lfltSJs4hWxeTaHEz-jkV88224aD9lFNkorp1l_cXznBvQY3NOCs-dsEnWkEYbS57nfRXwuvpqKxFT0sYupfPThDtSq1NZqWe9FvrRv-K4kTgTj2IyuTseRCkkR5QBs2y8oXean2zDAEV2NGJ6eqaLu8hNKQ3amli2CmcCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
جدول حساس و نفس‌گیر بهترین پاسورهای جام‌جهانی تا پایان هفته دوم مرحله‌گروهی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/95588" target="_blank">📅 07:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95587">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCkkKqytklimfPziONN5_6t5QJEncb6qS24CWyNJE31m4dWUCLyKRNZp8YsmrALpsNL2Sy4H83FuK0yotEyKG6zjA7rXHmApBcGMdsyLHWAFrnVPnsu9zFBeAs2GcHmhTxQeLzEBEugU8LVYXP1P3roc4tq-t-g0lWEm6O1GEJJ5YVCOjktiTLgHfpffFZJNPlud2V49BOtYS_Wv3XJlKqXS76oDciApF-Hps4rd_DXQBs9UVrtL-b7Chv-hovCVv0DVbYkYGLs0eUo_iYIyzG_JCLX6Y-wgNKaO7yZdf6Hk6DxDz5c-E_ljsT3j4N36HITDXoDuKT3Vd0Qjdl79Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
جدول داغ و جذاب بهترین گلزنان جام‌جهانی تا پایان هفته دوم مرحله‌گروهی
⚽️
لیونل‌مسی ۵گل
⚽️
ارلینگ هالند ۴گل
⚽️
کیلیان امباپه ۴ گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/95587" target="_blank">📅 07:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95586">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFQXEsw34afQillSwgfdJw2ilUWc7KffEiZLgTehM7KipBND7tsT-sayuqq92tjZA64ov9erkgR4KMiJH-t8w2bFxRnw4Adtw41fO-JM3Scv-h5lEKlZMXu1yq4CfKlSASYCqJYkM3f5_iYRmwSp6v2s83MfGeODeT1LnWwxikrUrMZkVr_1_Ps0o-awlZD-wVoOKwOrCeaEXkL7wm8y5l0gaBggaHVE0-J_IDM0VrsU6F2ulLy-hGxCWunMWXg8KaCfodx4ENbqDoQofbob6yyH54BfTUDitF-1LrDxA6ctM9ipEcVDNr-TxAB2gPgNJp88BzvQyFugzI5MZ4okxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
آپدیت تیم‌های راه‌یافته به مرحله حذفی جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/95586" target="_blank">📅 07:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95585">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgaWmxOAPw5q-NTQM9H6txhbJtxGANZeAJrWJmuK9kIcYnS-GhD4EYF4wavt2xwBqkATUv99nJYal4b0Xw_WsfnlYST6UN5YkJks3AonloxFDZLMnt9QnreC--ZXIWctwzzwR79kdkBUfZduQ_0-mtiELskcyuBvoU92NYWn50OF7KYP6iNsZDu3rAuAOH04IULNmQsJqjX2T2cw3ilowSIFiIRiAP0iJ3O7COGqr7K-8GL6i8fNw6aAE0yiWCXZjmUEnEsji84XaFxnpi6XA-jYyTa_fWhtLBrkbBLjgTcbAHX_Ty9EJHgxnJPvS8Hm8O5tzh7r_wi_4oGpnUEQPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
جدول رده‌بندی بهترین تیم‌های سوم جام‌جهانی پس از پایان هفته‌دوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/95585" target="_blank">📅 07:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95584">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnq2uAWyFJ_6DwHt4doXXHZ-fkwoeW8Bwbdy_El4Ea79RmgIgrO_Kc7LbOnfQMdiPYGCDtT4RwBR_ACQZ2R8fxyEzXi68jXWFfcW67WSDBDz-1J37ZpzZ4yYSaRmn994uval-k4J0A_ca4DlwSJVnNr70KIDT-uNZ89h48yi4ywOtZnLTq28kAN9NxtKbT0WqjRoDd-YGjg5kF8d3j43_7OCOZ1rOshFFh5YNLXPFwO32OnRA7pEJ_KcOwy83HCVP66cmizuE9UvhVoJ9HoYvIKShZ5xv12HlBwqyMbSYXCY3SlnJLNptZhpjmIz2ncv1njUIpKHJdn-UojuS4yMzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
کلمبیا راهی مرحله حذفی جام‌جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/95584" target="_blank">📅 07:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95583">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHbJJZTCll15kVP4ftAPkIWpDBQQ50ub6099H1sMIYIR2RTfJ-qtCD2kaz2lqNRhmMfYieGvgQAOJnlX1T5z7q4jEXSPGrbd5E0lADq_-nchCsvRwgnc6-5mmrbPqw6N5w_s-QyMtr4vd8hBoeuKBtfQGyJkqKMjFCIKdH2SN3R1tKR0k8USyso-Dr7VazjVKPulGc91deOSxfqwkGXg2xa8HcdT8Cy9cwGBX9KrZLI5s1ODm1wAdD9U_7qsGLHlpq7W4ZVxjUECKlM2MhGhe4jBg30MM6rsPPkWt0TKmYMyYNHlcvno9ZMa2QIC4mnVntf-8gi8YysEF0kqRgfXcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
کلمبیا راهی مرحله حذفی جام‌جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/95583" target="_blank">📅 07:30 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95582">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9fd0b47af9.mp4?token=SVUflY4q8KJjD3Zu5rgHF3Yf37wRIwTDe57gfUmIZS90q9PUx3GGyiYmXUQNqxdrP3jhyQcyid86v6yGfvV0zO-IFYRRCJ3yjZ7pTDqBhfQjoMdoHDX5TsSSvOEeDUXNU6AZfKBBYueXf5QJLh22UCVdc2oZhNBK_dFsvSSUL9ttp6mbkRvrYfwA_gPyCepq5h1y48IyPLBPDgCog-gUCR2l8z6dRfB1OIIQONtpqNzyozPhiv0lW1OpfXqpCIkh6LA4tHbf_Vl0G-TgPYyR2xFQxMrD1mnbkKe-mol_90at7h4PyaMWDflvSU4qIPR7GWGKl1xEftRBki0jgecaKg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9fd0b47af9.mp4?token=SVUflY4q8KJjD3Zu5rgHF3Yf37wRIwTDe57gfUmIZS90q9PUx3GGyiYmXUQNqxdrP3jhyQcyid86v6yGfvV0zO-IFYRRCJ3yjZ7pTDqBhfQjoMdoHDX5TsSSvOEeDUXNU6AZfKBBYueXf5QJLh22UCVdc2oZhNBK_dFsvSSUL9ttp6mbkRvrYfwA_gPyCepq5h1y48IyPLBPDgCog-gUCR2l8z6dRfB1OIIQONtpqNzyozPhiv0lW1OpfXqpCIkh6LA4tHbf_Vl0G-TgPYyR2xFQxMrD1mnbkKe-mol_90at7h4PyaMWDflvSU4qIPR7GWGKl1xEftRBki0jgecaKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇨🇴
گل‌اول کلمبیا به کنگو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/95582" target="_blank">📅 07:17 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95579">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YJSeXrVq8V_J9jBLSzoW2BB7O2rZoWYcDDM-OkOQkVk6Fi20bLaeITef1tI4RHJhfcy3boTcqX5hTopgGDwnc3v6TnTW2j3RdVgQYtdp-Jt9P13u0MJNQyvWPC4ogAN2txKbwbBChGhXXmKK-yAJJL6X28J11tUq0Y4ACKKInW8pSggvSYgwH7ShnDiHtqFtcVMcmLhZkGJfaIqnTxZy9QiAPBomZyacY4RdUy9f2MlvC_8Exzy_gI-rg5a7eZVpq4AIjLYi8bM4QK6ZLlSCOezYr5z2Vy0OehkVXfa5tmmpdTBDMQJJijHi_fAgbw4MNstlpqYmdww_OCziGVTSKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uTy728XtvZc9VgH3v8KK0C_PQfLQ21cZC-I9jTj5So7QWEGJjuNlVMsVU-d1HTjUYV2Q34WP2LbU2XvpwOHtDEhbYIMJNwZcx03AYvGvAE05cFgftc2NOfd_Idu9yPVBV_TCA2DSrSGNJJOXXSIFvpGCMVuBUgpbj92nnu8t7FmEebzHOoFkOG4M0mO98-5WQq8HR8xPLpsNMXYr1hqQutMR8q8xGaVaEVPX9EuFQfjwcjMO7KhRiZNl1_RrP3YR4WghTygSHKoxEC0IMIur6KifDfPr0PpZ1TuZ52wV_RA2lZUKYH-0T7odVTEIVaoyJHzrv7G4U_wJL55q6qYwDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jS9WjiS2QjVXjFKeckE74IRm4nIxcDHSfW8SBkBmffvN1d6F3mY2JQba8qaTfrywDAZ8cJ3jFqy38LHTO87hv-3XXD8qlCw8Ttc6B32ku-XniblbA4qzTphRh_9g_EW_K9ThH8qFMuy51dyi7mL1v5B_MByUAPOQIcTUEH9va7Invthnf0oov1BzECOrw8D6ZA8ZpoOVwDv9He5j-vfiL21xDKEZWR4eeEfwiJlSAgFD2n3oND9BAoj8IYWaiappB3LBvdajFqrJCfuPaojXjBMpuiftNMAJH7TveNNqr48GVnK91ciFYy5dn89OPVelzQC3d-gkn6I5Wxp5ITUi_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ما که خیلی وقته بخاطر خامس طرفدار کلمبیا هستیم
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/95579" target="_blank">📅 05:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95578">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">رد شد.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/95578" target="_blank">📅 05:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95577">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">گللللللل کلمبیا زد.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/95577" target="_blank">📅 05:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95574">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EPkClAD1ltFds7UWG9qOLNG4u9eraNAf8m0hQmy3zDLp1krdWTo40PT-79-RaqMFG76K34uJhd7Q5-YLJp9N-_EpzMR1fQVvqItP1ZImgAMXpGpdDAL5fo136eBAwnYA55ooNCNXnJqp3X451QP3wndjJISy-fEygO27wuZd5WvIQDT9Q7HTZDL7w5nV9XrvUqSCwCEDBbe70iiWXf7VgjAB0sw5aLylSOEleMfshLz1vCpr3I6i6HNRXkuynzYHTJUPZMPHguSCpEtaWnbQb0tszxpS_EaGWgwG17DYCIE_t4-lFIs4VjoYDh7d0dqY4kOr8KZTLYZ4KJzI-w3UYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S3ziO9ljeFbDtBPOXZ5bJj6bCVOhjh1GTHgV5RMUeCv78b6Bi11uwJHGBqdkZK1Z-MgC5On3BWPiv-Hnm_LZHHT_0Fz7vbdcpxdpPSrMq0KJmc8W2MH-n3KFBbDVjagmwpAVl5b9P7lteqY2lJ4pXDD21uw1PBcpgAKhzZdH3bFBhWvOuAnlLOYMqz63Ykp--4C0rvlmnRH7a8jb69US6z_9hvPkwnU_o4L7ZueHN8gfXyTKeAKu1ZYjlmC-DzObAo5KTgICDXrkjbjGa65yLs-BhHWGvCiDmqTpHtyDFuqmi5i_QQ9BB-lQo5XUXGHiGIivZBrsWlqc70sgRhfh9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RdyvEBuffxZuORGNqyrma5Q_wAB3nIg1Mz_oa7i1o5Oh5t7ZR3dqIGKk8yZu_fDZ3y6Gl6y35l_ifidEE4iuwHNzsfE9bmihw7B1Y2OvaPw9mmZLoh67DKIXm8ifN0SqKQFdYFCU_CHML4hDVOlIGJdoShTegXvzZAGuJAmabP44nGKCU407-vqeA3HsfaqSQustaC2Z5vNTzraZ3h0sSR-Ud_Ry6lxdGA9tdjq4zV8gqJKIFnOJH04Oh0cDCKQFkl5-_5AlurVGBUuwaBclRICaCsyGIUvUCAt85bw1WeWkE-GyunQS3jGhuVBJ7EWVrk3cTHEXwFC4Ygdyvwzxyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
🔥
جشن بازیکنای کرواسی به مناسبت رسیدن شراب ناب به 200 بازی ملی:
⚽️
200 بازی
⚽️
29 گل
🔥
31 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/95574" target="_blank">📅 05:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95573">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">بریم سراغ بازی کلمبیا - کنگو
تنها نکته مثبت این بازی حضور فیکس خامسه.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/95573" target="_blank">📅 05:29 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95572">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zu0cri7e1lLaZA6NZrdVnWMBkOdG6t7YI3_5GcG8jLwWbGn4SgrK3fTMbOTLbIiLs1OcxpSVOb8q-enijn7Y3IF7RYfM9bC70xYPC5osdkri6eM67c1NfKW9_SxUodX_zGxYzE8UBD0VxI2apj3y5vEWZihvYdQYfDr5EypUuaVFsXg2VM69jkTerchLLx2iNglu9wnSQ-6Cx3UVtQgJgCidXTNWns0odmx87H842TFjEYzdBhi-dM1ssxqFkXj463FWxLjmsE_BylyEjA1woP2uT_As_xltqZGX8w2B0-5JTpYzDwKh58mmCOwU0iPR7C54E7709P2F4ZQX1_XRiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تکراری ترین عکس این چند روز چنلای ورزشی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/95572" target="_blank">📅 05:27 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95568">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qvi7kprhKfeYjnrgY_n7_QrLAcoaeK12J5qxwPCm52Zdvm5J-I404qEdp8UQCxMSARspCzBBM2GG6gLPXzZ_COk269NVM_NX6Xb0QZmy5SX8z9SdUh1DjqfyPeBF-fyuEc_AbbpFWUuGuYsSG3bUb_zGMKT9pN0DRcclvw3OaSM9uCBiYEX0IvBNQVKXKtP3ReSpgJRSYSMD256NTP1Is8d2772v6H3km6dUY_d6VbcFibhp3zK3F_EOxtcGw3Zofitbc2i12RczYChwOHy79ZEqTy2mBlbHl6QHM7TXp_6UB2YiMsRu2vrNir9SbXq7gJZTWgApQwMOAhwafg7T7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b_qfymHf4M22NL29QN9Ex4CBaawcl2FkPDzhPFXPtSkJLn4dSmEE0iH9drRqBLM8-dyNdGCYg2SyZJkOz14CZMtB-C3_liVlA7a1RVPlojyTUNTI8WXD6eyX_8xSW-ki_qYtrE4I1Ae27hpv7WoB4b9hWCCzXINFraRasjq4VQH5VUDPclhMNEYzZgb72Hd3wduciFbm3AysG5wC0MlihYgMyRS625ssttEkXqkOB_jrVcETVJ9G-Phk7lBFEPd1d1W4832hmtgETdIkFy8XmU1L8LbGxcRBqBX4kA-GH_WvZFsD110lZegzS_xeC289-HvaN0s2bEVqdjbkDtoW1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KUmx_AiqGvc3plhHhC72d_nOZKoMPMl-e0uJiTqKgGll-tynZz1v59XS8NQHtW0oZStIcEjGDJu7O1Tw4SIGQJQHTltG7adsjvN5PtOB7KVi7PFbD1of0kc88AjH011FgEUMfJFtP1kTx-phT4oxO5hi3xfIdIbof0haST_stq9XwcHlEBMfQT-iDu1MrnHZpBiA4wcFYdDzFB8SDqcJJi3CaI7yN65XawoHWRaHsS_RWDSnoatcH6drK2EV5pXMA5wEBIy_ARV1AeoagveO7OzC6lfalYWVYBbXRsaxiQzYYPwRIdvf2rGFGKUDoFc3Cn7sYUSeNiJ27ABkypv33g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sqwhpbS9AZTIMTGRlhy-uY2VZUCM-2-buXC4-LbpXKUyx7VBXO7SbQPd4_geT6Orgjlrk_sNhRyx7zQEFHKyfX1vsDzH8kJk7KU36ymreLPxa1r3SdH2C5xATLOdgSRdTbci5Qgr_CUF7cxKITffN2MY-H3uJovgitAHIBiB47oChqOYusENBcbifF_H96jbrhik1qqIvpNQBbBjPmVd8qlv9OaAbGeRxAYmOfHRBoF1HRNYUqx-v4HCYA-j_UdZ_Wo99rD8uaximmSuYA_wW_7MQshxjEsGmTDRZDgyCEFpeTzPAvd0JaD3UmOQ_D21u7BfLKBN9yFBhy9Oz14SMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این عکسا چند سال دیگه می‌ره تو دل تاریخ
🍷
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/95568" target="_blank">📅 05:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95567">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBwBXBtTnqGm7aRWoqeo1m-_1cwUicdCPtj7gMM1_kOG4iEitrW2KVBaYwSjMU1FalNYyJqEpaf7r9zmpjS3ngWt6vK_xnOUPmHRlYzvnmL7gX1-S1D0oC6_pNMcmrteJhVkB1aztRVXuH3ewO71fDv6HrpSWdU2JV7R0AfzRkGy4yOTJUZvtchMU2Qb3V9cwXt0k-f_NRHtJnIJORLHU9Cxjsdn5ynyAl3FK94qE_iVPRK-1tX3jN1yMTl48uiYCK2jOFCVvmAbGdiBkOOfF-9d9_iZhEoOqaajHNdNcCszpe2PNXpaZfUx3gZTZ6L7hpVOETh7rAz8mXSv0MluwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🔥
فورییییی از کارلو آنچلوتی:
نیمار کاملا بهبود یافته و آمادست تا 90 دقیقه برای برزیل بازی کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/95567" target="_blank">📅 05:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95565">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cBkCvs5q_iLlU1Ux8Dy4yUhC1O0hSRhBwM3VZ98qNmhpAJsTSl0QXY7oQIPJNYe_iIcBrMi7JjDAygekOUyEWgqYZ-w3s12P381N4zbUf2Gd5FeeYijIg62gzvxDa54ucUz2-sGrkJU5I7H5hLsS9PfkdoiaLFYHPRHJhOHfkHtlLG0tJlxW0MLAPHP02op8kaKHOdS2euVmqYg0gWGJUMAL9XjJYZmwg-pVrRK6YIjWWbuQPMUMIuar-JdcpKopYVXAHrHxek9i8lr7CDaMtfWSptpIkmN8HRECxIP_mjIHpt-kxRtzH7oL0YVLI9dj_qvHTpLzX0jG7ec7F2PNzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oW76aFWUtboIUyPgnFWNPb3ZJFZnYo5z43OMhES30XOFochb9FNyOC2xrB_QKggn9WLo1itRV5UdzAVPfWdmv_585mRe-LBvCkMiQpLKHxXckhw4bLCbQvL9LjxhSu-tlXfAlTigYb5LCQB4hClwzcDazHBiDUlWfeyqghfeYc-EeyCsCS8sD9o8vAikTW1fanxUC-ZdsMpcduEvCcVQ1ofc4N67qCXEB5VX8K5QyRxYvszKlEEsAxQUi4OkBc2ixnZhP7BFvqMK2BGNp9Q8_H-hMqEs_VSOw87DS0zGq0FsmGxVt-hIgrKczTEdC5WdsDGfuBX7lvQLTZiH8o8QVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇨🇴
🇨🇩
ترکیب کلمبیا و کنگو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/95565" target="_blank">📅 05:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95564">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/svF6prRgAPfcV9j_kF2HhQRZccwNYqZHwBJ-glKChUcgdGx3QDg6XQKDo86rgStooj2kMjMhtNiK0qkja2j2rCPy31agbWMCYGyXuzjoXjf-bA1puixMfLZ-pZo5WxLlZKYdooMvAoSK8aB6LaO_W0BQGQQmY8ptIpOlUIcqPQfL6rsyy6dr6u-kWuOW-oNR_Oq-HmH2P1uD7NHC7pi7Ln8ogJ0hDWpSX5EKtMmE2c6WwCUDHXUyV_RrXYtQPiXlszBya-JldG9orMEsoaarynWaxHe5Csk6BPjCQws_bUK8gX3wNYGAPEW8FMSxfeq_bEyaymNbOb90ela6E0XRng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
📊
فقط ۴ تیم تاکنون در جام جهانی ۲۰۲۶ هیچ گلی دریافت نکرده‌اند:
🇬🇭
غنا - 0
🇦🇷
آرژانتین - 0
🇪🇸
اسپانیا - 0
🇲🇽
مکزیک - 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/95564" target="_blank">📅 04:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95563">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TaAAW3hjlI0lAIpeOt5ExANSddV0QTt_C2trost1t7MmMojohPIsiZ5l783Lf--CjIoKHR-oNTqGpXp1OopIMLLligkymGckKzW4YubOCsRX_KFblXSZfT16BHx3EeWpCasQcfAb_7RXRkEiVJZW8-tyOBEOC1RwH0dROGNfjT4fEhSAbGpF5JL5Un7OaZ_UEWKacHaRe8gkF31SjQGUmQ2Vpkq5xiaWeHpoMoaqXEtIOvQtoLm_t7295bsbxcF45o4Z__5bdkzCh5CXn6rL4mui55efPxZGyjDs4SCZ40dj3BcuexoFc258FSeBsTI-a7aSBuuk1Ir7Ii_eQm1vtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
❌
🏆
تیم‌های حذف شده از جام جهانی ۲۰۲۶ تاکنون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/95563" target="_blank">📅 04:49 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95562">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6qgYxtl95Z0Z87CbR61nqbY8buvsVJ_0xsdtndZgd5s7gzUlmr373TM-6hyZNr_oCmIxJRJvm0Un-HWTWXnJu72wlfDFA5OVFCtXQ-g1gdFxPCQrLqqjg73EeqVNPW5pZX2jkFrKHftsmh6zbP5wDksmDRvW_uKC6Og9LKYYiX_CmdVqklMYp3PP2NeNIUh-uZ49r-BG8JObKajJUoI1ga0DlZxnkuhPUTvFTpNpRISi8Rqorx7avASE1UUMqveCAf5IxjZHvBAzhhfjli0Y07prBNUB_d55591vGmsdeXke5M6I-CMUG-Iy2Djvf3H_JE6ddFdHBtAuKVaz6-vug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
جدول گروه L جام‌جهانی با صدرنشینی انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/95562" target="_blank">📅 04:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95561">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/htbvsWZx0aIb7ZaYIr9Jk5_SmvZslJMjZXofbi9lPbtKvGUr-TCQesZ1HqirBnM4m4dM0aiRLHJh_qNWOc6Y-1OloIrTSrhmOPHuWNZau2crP4MZasNnifrMlQioV5VNm-w4u_FnJcfww6FQnh24uudG_Dk30TRXoomFZ5pFzql9PIs8OusUv7CMUQWIDvgWzyFaGiVIdJ4sENi8sa8vC_xYSx9vzEjS0VK4RxUGJwpCLj-vualMfSCW7jmUQXM13qpSbV_fBDVR34YVJnxLwW7kYYeh2s96kVn3DbIiaYE7YO1ZQaQ4sxIfNVjqM43gD2B44m9CkS796AGOyyD3Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | بای بای پاناما؛ زنده ماندن امید کروات‌ها به لطف تک گل بودیمیر
🇭🇷
کرواسی 1 -
🇵🇦
پاناما 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/95561" target="_blank">📅 04:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95560">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54adb67650.mp4?token=BdlUNUyAyj0cZjQuNRI3EIGpqZoF4FWcw2KHk_9vj1y8O2Yp5g_4eEFrRpma5-IfdFJSSXf_BOj3siMPobzVkC7ND5NtuzXLpsSuVhL_Crgq9y-PAPIREijf33AFqAdnap2flv4RzznPvr44cRwmO8O1SXAYFbzqcAXTXitDnaf3W6N88RRq8VCB9HT56g3kbFTgxnbH-K8KQbE0sLFznIF-yYknI1WSvi3vtW2tXvbTAhUgfzZhNmeKCEJ1gfksKcDIvXgYK868dAsf3oQwmTvASBie88QW51CUzDHP3sY2YqFqt9d1eRtkGhJirTrM3HzwPo5h7LJrq1U8-QJL2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54adb67650.mp4?token=BdlUNUyAyj0cZjQuNRI3EIGpqZoF4FWcw2KHk_9vj1y8O2Yp5g_4eEFrRpma5-IfdFJSSXf_BOj3siMPobzVkC7ND5NtuzXLpsSuVhL_Crgq9y-PAPIREijf33AFqAdnap2flv4RzznPvr44cRwmO8O1SXAYFbzqcAXTXitDnaf3W6N88RRq8VCB9HT56g3kbFTgxnbH-K8KQbE0sLFznIF-yYknI1WSvi3vtW2tXvbTAhUgfzZhNmeKCEJ1gfksKcDIvXgYK868dAsf3oQwmTvASBie88QW51CUzDHP3sY2YqFqt9d1eRtkGhJirTrM3HzwPo5h7LJrq1U8-QJL2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بودیمیر به این شکل کون کرواسیو نجات داد و تک گل کرواسی به پاناما رو زد
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/95560" target="_blank">📅 04:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95559">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kt47UDpcbwBB6m94yYlSVQIA_jGtvm0dma7pyBNbpyJSIlU-Txb9-KKiR81efF1LjfYRzZKolUILVXUQM5vO1t4antVUfsgQ1FHkMduG3HTp0Mn6dkyEcwyxbQxjeIV7gfPD_C49pZTboeOpY8NSqV3JvZqWonJF6gy2pYwfYvS-VVXdTx4WyesfU62pu6hUB0LXRUFkYdmeeLoHWG3vesRQwqAiUcRTmcbIlw7z6CPXrmWYhGoBGtyFvgTYTkmMQsQvePwEjSvVT1Dv-bHIOBnBou31UmxzwHGflHgeetXmxEMS-AAXtD_h5n11Mzy0aKhWw-ASQVP03UBfar_vjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو:
جولیان آلوارز احساس میکند اتلتیکو مادرید به او خیانت کرده است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/95559" target="_blank">📅 02:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95558">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADMgJdezPKM2uorx5rw56sDe61ZFobrMEVWeFlZIxGl7pwuvXKi7vdVk_Cy6vV72aQx7p-wEub1BuehUkZdYCCBgvam_SqxBxKAsNHLbnzoDZD6I3-6sIPkjOTQFhqPnIek25daebb-l0P_wbOK7G2dPBuGRL7iqt6hIstU2KcvcX8UnTF3sSbEFQPIvbXgT1-JlmkHTP66-ZQ8vNIpBlQLi1bmsYIV7BF053cGe5CVBpAf8qwVP0lSL-hrekjhL4TWWOIPz8jizMkRtPXMWbe5qkja_6ox-smVuBhrBgaJS_91ijuCkaTdeELwTKlG6DajTpnBFtp_FOMtRGcKp_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
برونو فرناندز:
کریستیانو برای گل ها زندگی می کند و ما به او نیاز داریم که بیشتر گل بزند. او همیشه یک گلزن استثنایی بوده و همیشه تشنه گلزنی بوده است.
ما به مهاجمان خود خدمت می کنیم، نه فقط کریستیانو، اگرچه او سلاح اصلی ماست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/95558" target="_blank">📅 02:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95555">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WvAY1qSWQ_X5RyHdjqh7cHBQHO7MuieXg6HlJdZVUxOtOTF5HjuByai2xDs9UsypuxLBoQrjAjSHWBNliIZuUMVBk4VUysDN50EtRiIaF6-YZJn0N4_Hsx0ZRXF6haNBsKhCKcsoWqx7dZZL1ANIgrr4WVJCDDjKuWUibUK5CT1pp2vw49NTbqC2Y55rgZ2JodFm-gqjuknhXR3QOAO1oU6hx1YRk4umAgsSI_Fc1fJvSvrkzHtcGKGcKuzo-KzCfW_xa9Ki224YCnqUh-7kLYwHTCoPCHjQzqEnThja6OIh7PfB_jmpo849K-rvnPd4uoh5U9cJdV9h8CJMlyNOeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v25c4RS0KlYbxO_7Pl0e0nHvk1_NF7nm3ZyaFQ8EhmhU5Wb681GODtSCxoltrGw7l2_6Cne7NnmkXONM-t3VZcViz7zANT_4YFDwpel1gdwW8wv9fZUtUuPSPoV7LrYRS2rFnKgEwoUiKZoNTUWRNr6Tds908TaEgYdv8oBt2yCa8pviSE_T_dXNCM1_OWrR3BF54IHLl2ij_F8PKd5sOh7in0DCHw624JC215QvQBYgfvbSwnF89-UNYPULQ7fS-pFInGqarDS80PEydXiftetpYWtfbZr7rOnDyrQpaFVn0QrlSIt3-tYl11PfbHynH05oX58ROfgG18FNyMoj_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JhQ6kit3a3ddq8Q_-iNIZNM-i9qZgP_hJTNUkQxuKpFsuYVb4gVSJVLijT8FEBbjwfXM6hh4CSGsJhi2T394YpQa3zAaIAcrH8gK4QNZlSM6UVsqQySpBP9LMrTI1xqAEj0vsqmlrXLr98qD-BwfG64gyBXaihZLWKS899OCaVeVErNHkoIPYXmr07l_rjErgReYz2ENqBR5_2y5tOJwkABqwrzoZ5l8RNYUqnd52Z4-XGW3dz8-bWodVjZZw-zxPvvtI9BnU0M7nN1x0OGlusIV3c9xUdf4Re9Ma1vPpke3NesmaWLLFZWS57d-1czT5a5vmIVcOifyc93ITRg5LA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بانو ایوانا برای حمایت از کرواسی تو ورزشگاه حضور داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/95555" target="_blank">📅 02:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95554">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dfd384cab.mp4?token=KSP-TafQD81zt9PJ_1S-2bTJW5njkrjnQrlYvUp0Z49lPvq20Ta4S8Z2Ul3JNns8cohp4AN_4Zbe1SOde6NiCIxfz-ElK3Vk99to0SH5Xp5cOCsa_uEHKyO0fDy95XuDuMFBL7LSW-_jBnhgiZ3n28h1CurqaQJ2ZT_Ms4MVme9zV378wU0NidTfrd0BLS0pgNzAS84hqaBSxuhWoMHF4Tk2-bw7EPu1N2v82Xm10Bw6EJf4usZz-50Rl4KNXe7OlAvbeGadkZyff1_kUWOKB96PpCJ5XJ3BW2OFzm_MYIc16KOxDY-bElfOFDk7ruLSoIpA2fQ-aikFqVQV-8TnLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dfd384cab.mp4?token=KSP-TafQD81zt9PJ_1S-2bTJW5njkrjnQrlYvUp0Z49lPvq20Ta4S8Z2Ul3JNns8cohp4AN_4Zbe1SOde6NiCIxfz-ElK3Vk99to0SH5Xp5cOCsa_uEHKyO0fDy95XuDuMFBL7LSW-_jBnhgiZ3n28h1CurqaQJ2ZT_Ms4MVme9zV378wU0NidTfrd0BLS0pgNzAS84hqaBSxuhWoMHF4Tk2-bw7EPu1N2v82Xm10Bw6EJf4usZz-50Rl4KNXe7OlAvbeGadkZyff1_kUWOKB96PpCJ5XJ3BW2OFzm_MYIc16KOxDY-bElfOFDk7ruLSoIpA2fQ-aikFqVQV-8TnLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انگلیس در مقابل غنا 78.8% مالکیت توپ رو ثبت کرد
این بالاترین میزان مالکیت توپ ثبت شده (از سال 1966) توسط تیمی در یک مسابقه جام جهانی بدون زدن گل است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/95554" target="_blank">📅 01:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95553">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZ7STULWYyFUajeMtB2YfFXBjFTwqo6Ggjn7b1RWwTS0BjqMT7kKYxezelV7BtkMnviPVVSLG-3hsyd281l91Nfx9NMxrmanfru5DiAJYlk679jBYxvcitekuKWQh1kZ7FsL3xguj9tZ5La4dnQeuj7W5wfyjK9w7W6jfNqnLudtoa-k06Hv0LasNzQRPxIhp-saXpJlzA3hAcNJPsiOjzjUwR77mCWcxaQP07XbgwBhmSJkB-FMwzVbFWWTZGqwmvrgQv8XLBGUUakBKt0qwdBe3BawfbKP65xmW6gdjNbt1ntzVST4MpGGfbdAKh8gwq_h99cAv5acLbb25k3H1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیونل مسی 39 ساله شد
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/95553" target="_blank">📅 01:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95552">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/95552" target="_blank">📅 01:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95551">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FzANFafTIxgAci-UUqkHYdxraUvRbi94Y-eMKpRu2b7uzTD11ShXf3KJyBMWuUWADvJQddertoFqwM7fstWCsUxsjqKkjHcdEPUUCkNB2XCoeojp5os_vdG5QEPWHtXfI4b82K2_8cDpx2Oj-9oSUThhJ6uCrvUC7oXbI7YEKw1Pj4VZcFyqNT-tiagGJMgNFVflp96ZWaSf8lq2bB_ZeKshindX5JdAUVI7JE425b4plbEZhwKkS1IOYI0z2-0Mw_oypy8n23T8pnMUpaVYAjTkZY05wBg_zIe0k1A1BCFozRxLdRDKPw8WaBoBlPZBq6coSuW1VaCm8tnjooxMgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/95551" target="_blank">📅 01:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95550">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxpTSgPr6pMEu7qHvnB3hD-IgICIQDWPdfDUZ4IVoB1WG_AgkVDHztMV_-w3LpMvXMmQmNrsDj-nOZGSDU1mSe3OQ0ni51JyqyqXl7LR2aNx10RtY1tz4B-iYT80TrkZvUi6bdtgD_bQknILPZLfo5RY2da6iHvTTbM5XPl97zthXVVpbYZxu57P76BA3NqR0XghcWQ5ED-NezCR5dUDYA0fxVrdd2JJ45meSr_Fiw2cRIgO6XGlNK4Zz15FNzdjWS_7xEs8tu0GX-DMP69cX5-fGPCILaXudOZNLn_CxMdg3aB4X2_rf4_HaVSljGVMzurYHyK3f9qb--hu40K1Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جود بلینگهام بهترین بازیکن زمین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/95550" target="_blank">📅 01:36 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95549">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oB8Z0Zf2jbzFT2MMotdtqn4bbi96W-3CqVLqVMgi9SGANxTf5s59app2ccir0wHdqThEHADgXvs-Opqjl46GVh7H5VVESzMJ_zGEAtmlL9FgFVGEgeLKNrILnOcoFxyww5MkpmasAmqxzHdklfuZLfCRHLsDTyFe9m4rqV9lFIHwh4iqAErsv4Bo7a5l2rPGmIeIYF-jY_5WtTNBxL7HzFlaafEn1wimFexkFlKGVnT-liYiH0Kqvudhd80th5LiQupoBODZA66k2XsKLuhSquUkzR4tALz8eYZFp-0CYF9zTaFeL7tTPfJZmDRbPtHctOcu4rR6ps7rghT2uxbAjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | شاگردان کی‌روش با اتوبوس از حریف قدرتمند خود امتیاز گرفتند
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس 0 -
🇬🇭
غنا 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/95549" target="_blank">📅 01:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95548">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGAhZlJZPTZfvaugDM101fmTaxomgKQSHCddI_P0tBbaRX_SAfV_eWM1Ltwpx49RptqazoiKxSrygdimF_cY5q8l0H8Ct_7afSGeq09btburur2q0mXGAVp3RjTPhU2Z29pv6WSTHdHuvlN87I9a-FWLcKLZW7Vp2sqcK9SwDh_5EBmYw1_wEAWSdat0lADV7I-NlDCUQwsXEWWexm5_RjEn6IsUQbW6xAgK9ZEZX93ISdMShwnQ5U9VIXEhNJ_apxzv50HnyXIL8FIlXSPyfqzsyHjTKAE43Rcs6lPVaWsJBmzSm2aUUdXjseBjfC6iSCU-gM6hOMT_6UutLOlAsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
موقعیتی که کین نزد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/95548" target="_blank">📅 01:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95547">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">چجوری این توپارو انگلیس گل نکرد</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/95547" target="_blank">📅 01:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95546">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">پشمام غنا چی رو گل نکرد</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/95546" target="_blank">📅 01:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95545">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQmKi1G2Q73yYX3aqmWHu13JhuDHrQ2off75PBiLZy_EPsosRZkBA7rjMgU2i868Qkjla3nmDwH-VCPjK16M6cKra4Br0sO2iX87VcMqagimgfl15BjqXhcv2EVOMJbfbO6FaKWwAsdXR3yD7dcUQcGR6n5YFevjw-9Bn4rHmu4oW41GHNQ03poeXZVvhOTn8R32fjPVhJa30eGb95k0uSAUTr3l7sA7OqC_R9dWmWc3pjTBJjCjBFoJ1JNMJ2h5yMDi6rq0yfmu_F9o6_yRTaUu5ywF1_KwD2EKq80pIIQL60zGP4ENKjeY0AC-By8OubrHYox1QqjzCcJTgwNZtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇦
🇭🇷
ترکیب پاناما و کرواسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/95545" target="_blank">📅 01:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95544">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-jHyuSodp1V91iVtKzCV1l0youcNw1B97jbTeyDiC7J3sIthTYtN8o4_lzHy3kZ_GL02tqkjRb6PtZwAyKAdTv_t4mr2rtZKmajW6pQ4u4cIFvRq6Kp5mQjbaYtRpz5xnV6lMTWg_aRgIsWILQGtzrsdQcQiOiA-Ppea2m2vOp7miMVm5yFpvqsURTe1eZBRp157eIQXAVtGFsFNzxTBdWcrHOnJE0ds3KVvq9641pdgy_wDQkNi2gJXH7_VYF4PtmfjbvC1Ubs60roXDXB6DM8YWLU4nomJk2MF5IiQxGbdX_aT9K55Bv_X0m_UMiSYKtcdsXUKtGPkMHnpw5iFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کی‌روش داره حرامبال رو به بقیه یاد میده</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/95544" target="_blank">📅 01:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95543">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caad3dc61a.mp4?token=qU5GqWa3-8aqVJglxce0G08WhfXdD0v4ZJEYCG9f4aFvv8gF38JurNiZ6Dx-YTtI5nehlQo3iYXUVbRGnEcS-wkSzE63jr6Nr3qnNJuh02MJuAQvnohHqfx_S301VohFx9tQD81nqzMM3gzIsJrJi1-NWh-T3b89dqeYYA7un26x_HddkVA554hiFH7OFzc7QKdoTzFa2ZAzNsA7lZCKGT8gfwpdt-VYqWb2ChDD4R-D2DyRPDM_wgh3Umaf0hQPfOvqyovZEqLlonu5SJvP-cMuSalfaNxD_0JflteTPUe6kcPblzuMqOloqr_IREuMlvdAYHsp5br6xk6TwYyZbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caad3dc61a.mp4?token=qU5GqWa3-8aqVJglxce0G08WhfXdD0v4ZJEYCG9f4aFvv8gF38JurNiZ6Dx-YTtI5nehlQo3iYXUVbRGnEcS-wkSzE63jr6Nr3qnNJuh02MJuAQvnohHqfx_S301VohFx9tQD81nqzMM3gzIsJrJi1-NWh-T3b89dqeYYA7un26x_HddkVA554hiFH7OFzc7QKdoTzFa2ZAzNsA7lZCKGT8gfwpdt-VYqWb2ChDD4R-D2DyRPDM_wgh3Umaf0hQPfOvqyovZEqLlonu5SJvP-cMuSalfaNxD_0JflteTPUe6kcPblzuMqOloqr_IREuMlvdAYHsp5br6xk6TwYyZbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🔥
رونالدو بعد از دبل مقابل ازبکستان:
"یه جوری رفتار می‌کردن که انگار من دیگه از فوتبال خداحافظی کردم و تموم شدم! اما من تحمل کردم، مثل همیشه؛ چون من بیشتر از هر چیزی به کار و تلاش اعتقاد دارم. سخت بود، باید بهش اعتراف کنم، اما خب... ما دوباره برگشتیم!"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/95543" target="_blank">📅 01:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95542">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">غنا چه دفاعی میکنه</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/95542" target="_blank">📅 00:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95541">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">بریم واسه نیمه دوم بازی</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/95541" target="_blank">📅 00:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95540">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUn2Tu_aaSaECRgdBq6kfaNQAOHwLGfcEeF-ob-yC39gP90HMt1R9hYMs8X9JgtzCd-DwyCAdUr26jCUxR8lcWYtLg6tA2k3HeR7f-gUTyn7X6widGu0vZNoq45rBjerJ3_8zMUagaVH1yk_2-JNRvqEQ8cMixUHWJvNmiFXHKYyaFE7wtE3Fdxy6-joJoqFisnFLjda4SAAjnKSXPCvpurltqW2x3pdy0J0fpvytRaa43ylJUkpBKAYsNafdV1TPYCYBJHgVk9sWzyse3aBKj0FWb8ZOjfAFsW2XsAhh_dFAI8YW2QXS1JxVP3xRahWLobOYYv3Xf2vzZJ6QkQAog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دالوت تو اینستا : عین بچه‌ها میخنده
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/95540" target="_blank">📅 00:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95539">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Em8hzDlgC1yXoFzeDmLgjgPR9-ZvSqcQEYYmvey2smlfEVa2a068zUSyidm7Kd20FzgcoT_7nKzNnha3_DVFFdyIN57qIL3md1Or00W2-Z0SjkGqOpvKn6tMJc5Bq22MYckX5FqCnJx51cz3PdjAxb4f3JWcIbZsV32s80nefp5RESMKiwaD5VBFLSzU0ACagwsYpCv6PCIoTkPzhSEPE1B75ubIyZkhoyaF62rMHLOZgQ-V5ImLbrS7lPOcC8XPrHJ7EzXYzEX053Ay21i2ofEFzBzpBMpEuP_ht0Nq4rhFykMJWXP-BAaLoEcrmLniq31Lzi4PcuNRJ2rnU1IS6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیونل مسی 39 ساله شد
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/95539" target="_blank">📅 00:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95538">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پایان نیمه اول
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس 0 -
🇬🇭
غنا 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/95538" target="_blank">📅 00:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95537">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVOFx6cg9D7f0wSa-_ifm4BNC6gC7Z1D9C5chjhpKlObwPmXpxxR8cx3lf3wpuYWvQomS4e3hLvzCwbWW1khR4zw7tpHkn4UeAN6epC5aFBg0reydBtpexfSA2lRMtxn913mjv5dHhp1yztr2PBhWNFGCqOaAZhJ8FuJNEAmEUx-StzBF0H_qrap64CpexPCEI41gml0gfWeUktR1WkrccHvnhwyi3y_qKzOB5iczX0GIgwPc-4nbSwR7BEr0IZUhx-FUKHlwkO7gomBZ3me9tQqw2E-B1M_gWzhzJR7KNKBbd6qz945LcOaIAbP3uUV_-oEyIk-EFo_BntEAOP4Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیوید بکهام تو ورزشگاه حضور داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/95537" target="_blank">📅 00:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95536">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YT0l6QS-KzN90JtON2HEXHnP6kayRZa7liyxhMnvuDwlxwSGOy53Rs4JKeC9-5NKHxI5IwVDUKch0RlyPprEd32T4M0MuWMxHc0O5jB4342GsVUJQOyoScHy9qvib2Ry3oAUJZ01-cqYgse_kI4pakuM-975K4Jy52gPcfvjujo82EKVJkTyLH5ChYRQTgAcdzE73_GiFps_ck6FKCJyNICv6d5GvtbaBqnmmjBRpQxeGUwgz2rgiqMFm9Bjkz-yXRgD6tYS2-68SIJFwR7C8YTmuhkvrHQ5cDhwJZsSFkrRMCeSCCsjeLNxQrNqANLNRsyPH4x-Xk3gYNA-iukwSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🏆
نظرت راجب گلزنی لیونل‌مسی چیه؟
🎙
‼️
رونالدو: تو جام‌جهانی هالند‌ و امباپه هم گلزنی کردن! چرا سوالی از اینا نمیپرسید؟!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/95536" target="_blank">📅 00:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95535">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">شجاع خلیل‌زاده: اگر بازی‌های تدارکاتی خوبی برگزار می‌کردیم، قطعا نیوزیلند را می‌بردیم/ امیدوارم در آخر دشمن شاد نشویم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/95535" target="_blank">📅 00:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95534">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/095322bde5.mp4?token=TABO5s5c1HrL0c0_b4DL1CXP9C4H1gTBGThCk6u6_DYLQZq63URMNvMFwmZqmHLYTQG-qi8jYuRqkeApOgaF8EgtJehxMcEQYmkyU-T-XIPqG0lgpO7e40eEDTT2-zc2NmyOJkZoDvirok40NjFOWRhIAVJzRO8g-iTFble8xCUrcz06ovpgLeTcB8kjt-3zmDyMzJT6b4hemEvDw_lXR9VFC5cfsRdF6KBQI8N_ubtxv1OASMXJLEYrq5oOugyW4dhYLx_rmc620GJgQBU0PoqwddbpqxRbia6zWDoamrS_dh2iA1eEquXbrCl3Txa-2jsjCsTvaDx2_-RF0XcHSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/095322bde5.mp4?token=TABO5s5c1HrL0c0_b4DL1CXP9C4H1gTBGThCk6u6_DYLQZq63URMNvMFwmZqmHLYTQG-qi8jYuRqkeApOgaF8EgtJehxMcEQYmkyU-T-XIPqG0lgpO7e40eEDTT2-zc2NmyOJkZoDvirok40NjFOWRhIAVJzRO8g-iTFble8xCUrcz06ovpgLeTcB8kjt-3zmDyMzJT6b4hemEvDw_lXR9VFC5cfsRdF6KBQI8N_ubtxv1OASMXJLEYrq5oOugyW4dhYLx_rmc620GJgQBU0PoqwddbpqxRbia6zWDoamrS_dh2iA1eEquXbrCl3Txa-2jsjCsTvaDx2_-RF0XcHSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل‌زاده: اگر مقابل مصر نتیجه نگیریم فایده‌ای ندارد و مثل جام‌های جهانی قبلی باید برگردیم/ بازی با مصر خیلی سخت‌تر از بازی با بلژیک است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/95534" target="_blank">📅 00:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95533">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzzq2gxKMknWvHdpz_FeicCZVLju5UelVz8VMrhEVCUx7zilYfAD0WwLn4ZVI_7SFMpihdNByGAgrvZeurn-KUlcUu1Z91HMmQ6Cu1Ef2McyZJXq39ESs4Hlqv4OfTbKloKABpEN8cv9SQHV6nblf3QoT4KHA4E4ezVjEyJ3KefIkXKIbUIbo1EQPzzoNlAQa1Bf8q7K5YMeYTR2p8TkOFL3FxVGgfcU3vv2ayhgs1j0l1KabZ8ssQcEVAoOvP29t3UwJ5A3UB7HVNk70wIlJjwq_Wa9-8SJYElWenZ6-kChPV3IGrvU2_KDm80ZwQYLCHrCpSf_93yA_dtWElVYlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
🔵
همسر رافینیا درباره شایعات مشکلات مالی این بازیکن و احتمال پذیرش پیشنهاد نجومی الهلال
:
راستش اگه بخوام صادق باشم باید بگم اگه حتی ۱ درصد درآمد فعلی رافینیا رو داشته باشید به راحتی جزو طبقه ثروتمند هستید. خانواده ما یک جت شخصی، چندین آپارتمان لوکس در سراسر نقاط اروپا و برزیل داره و فکر نمیکنم این موارد به منزله مشکلات مالی باشه. امیدوارم رسانه‌ها برای فشار به ما حرفای خنده دار و مسخره نزنن چون دلقک فضای مجازی میشن
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/95533" target="_blank">📅 00:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95532">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">کی‌روش داره حرامبال رو به بقیه یاد میده</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/95532" target="_blank">📅 23:48 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95531">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGWtt1gSnr0e--riaNCZXUvGp1_yRctczpU69MNkUA7M3sx01flCWvXlDdxkXUDToE1HB6KtZlAPIaoxAKDAwGl_LLJCrPHtUThWZxuMzChq8DwEdMtUOlwXMHcbL6ob-PYkjReJCLu9zQoKxqd6Y88mscMUYv-suk5pt5h4zkQb7DKAcdL1rC8-fuN3TAamFlvCfiqbcWgRO80VqeWnUYbiT-zzIhjf3h5cj_14UpOQZPeKQpRtLyvWUR0vNbHGXKeAKdCd_4_NsA4y-lOHrGLeX71-UwoAvTMYiIZcpl_QU8L84oEm4wFfJ3naTzdVhjWvbswYlF_38lBqX--2Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بلینگهام با 22 سال و 359 روز سن، جوان‌ترین بازیکنی شد که به 50 بازی ملی برای انگلیس میرسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/95531" target="_blank">📅 23:46 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
