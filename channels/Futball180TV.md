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
<img src="https://cdn5.telesco.pe/file/K5KdHhrqbYE3bN8Xqoz16yQipHvGbIU501F09ppmQ5BVP_FyjxoxjHVINnFfTkgOVd5LGo2qhKgDtpYbkTPV1lHdlKG_vUl5zKeR51IwQ8JLqOxRMRzDNkXbk822GMzPU9lq9zQhxd0XRybI50iUYnB3iXkyqxxyr-5A3n_OtngYmTJR2oJ5nJykqYO6hor6Lt5fIsGP4MzzuHlMdLnLJP7C_3Fwrrdk5aUmCrlsWoez7WDOfDbLsujT8zDiDkoUW9ev624_IV2qPCEAunnjQ2wMXfIIXZ0askuf_XPUNuggih5o4Irct_TAGrAJoTcnIYI73cFl16fAXSKsKWb1Fw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 694K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 21:36:53</div>
<hr>

<div class="tg-post" id="msg-96693">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4IvaIn9_0yV5dpHEK3aQHejoPzOmL-fpcDZjc9tWWqXdHeFpvvIKaeAdm8mRhBu6kOw51bg5BMdllplP6HL_o33pnr5tdWKJnBPP7c_dr-kq7fkGDE0sXu5SwvIcR7Fua4MOWrKG-4Lbq2t3LghJ4oIgGvWGH7250RzH6G_j2jIb6QJVq9amRi7zUXTx65bidoJEEk8nzdmU2oSNqbnhRfwO-g4P6-EXfShQ3K4TBvRD-N1k8eVmhZQbDbUw1Qrvf8fQvtler-k_34xgwUkpEe4w9IMJMGdW2-DYVOrluJQlwXeQ2nItu1woo3X1Wayxasegu3WMJSi6YNtdiNOfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
👀
رونالدو نازاریو : نیمار؟ امیدوارم عملکردش همه کسایی که فوتبالشو تموم شده میدونن رو ساکت کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8 · <a href="https://t.me/Futball180TV/96693" target="_blank">📅 21:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96692">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووری
؛ فابریزو رومانو:
آلوارز بارسلونا و بارسلونا و بارسلونا را می‌خواهد. من مطمئنم بارسلونا دوباره به خاطر او باز خواهد گشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/Futball180TV/96692" target="_blank">📅 21:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96690">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uKPJb9NT92IGPOufbib5xdnjY3quPAiF91_55zWBCO-XuqmlLJHc4ly2Vigi692xNdMVeTv9zp6-ACMyeOKaqX1Zfk9LDrSeaWCY9FUIlghe2ifyO6-ijv0Cp6gE1qpqCLnhRAAQHQ8iz1jOnf0IUXf4xFg-CeofrTQu2uXO3KKiUfPkXx1rXnL3JKKCDqEEUCosDr3mZqOp2Nr--13lCWzG2oh8OCyDtIbSWknEi6MPeaojppE8rUMQRvSfwrz16aOvEBaurWkWgsl7fie2rT6N4U5tTIlY4YxLcaS4h1bACHzaYTFaCN6YV5ap8zqqRXvaXxECHfHc0P9jfVjfkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/frv4e8RpEHXTj0TxypKKb--cE9x-BOseWIQb_2Ycj9cK3DPACXMHpGpOAio-pYFp7yfcWaapFOeNEMUAu0MiZv266TIquyLMeLpATnLAIxFHxC2uhnnPAod0_buRyQ4I2JztktgB2iK0w5OJd-6Wvy1f7hyTzw-oS8V4dkPqTHtPXR7HA3HFMNCSeflEW3FFi3ljI76qzxG523KWOV_Djmrl40Qur-ZPIZ704yRKqaOdirjqzNS-I9apRkSy0Yp29bJ5lDEF_091QP2VjDTttxvZRNGS3Xcj85XWOrvUWFfD6r02MN7rB5eQAAKz8g45Ph9vOd4QgavAEniQ8PHBdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇿🇦
🇨🇦
ترکیب آفریقای جنوبی و کانادا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/Futball180TV/96690" target="_blank">📅 21:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96689">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGqhnr8eDbGzRUQpFE_juOf48HccKNkBva2JbiJ_ozUNap5pYI4_j6hXAiKx8F0YDLczqm8rzGtuEkxR3s5PK1Q98rVf4GOkyG8HVcrBB3OiZTMngbbkBWydm__8npzlQ8nshc1rGi4vJ0BIMn4Wv2UyhgSHDuV1he9wSLBMjN1R9Uu8IgsRO1ic3wiYR0SRP95zJlSwZgrWAA6vWMAhHmwedaoZHFGKl9utC4AFy3viJ3UW7k6bQOp2RnZgr7rBRatLA7Og5v2Y3fYYzKcsjAznBAj0taqQOy5QE93UjBzzuVccU7Qae9a2Jh4Qp65WVMlxdmP6D1rAmj_3LLQPow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو:
روبرت لواندوفسکی به شیکاگو فایر آمریکا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/Futball180TV/96689" target="_blank">📅 21:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96688">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/96688" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/Futball180TV/96688" target="_blank">📅 21:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96687">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxnYfvSTPEw-AliczptmDSiXxsAKsxGp5qpDxx-PjNZQopiKxL8ZiSYOxrTgdDELkK7WcwcuBugYZlSdhf4TySHh9uYbDlvRKAKG8zLpnNohB-OaJ-4b5UvThzncOI7HF8eQ3OzsT1ida3aVzLXyOhfZ0jZJksSH65E1-RklENRXd2dp3AlGn3b6Vb5qtucwwR7UO0vvd6SyoNamFvgS-uGxcDDwhfS8Lx9YRDBiCqhazeE19szJjTcrh8jsujO4ZNyz3j_mqGCuRAIqq_ak0u_nKfqgsGYrdHgar-1dawe5a3dUilAL1YwDJYJtdQ5ZzLAikhaNShb_6o466RLeXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وان‌ ایکس بت برترین و خفن ترین سایت پیشبینی بین المللی که به کاربران  ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
1x_1566529
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر  بازپرداخت هدیه میدهد
🌐
Link:
bitly.uk/connect1xbet
🌐
Link:
bitly.uk/connect1xbet
🔑
برای ورود به سایت از کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
⬇️
اپلیکیشن وان‌ایکس بت
🔽
🔽</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/Futball180TV/96687" target="_blank">📅 21:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96686">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1560dfcd3a.mp4?token=NlXheUCjWEEIc-yhEnuw8Ye7U3xHcv0wkc_uuB3KRfze7WdZn9JD4-302ifPp6i6FI-jdWstewTJ1BEcNtqgiGBDKiNvcLGfH-CVDGB6R1-fPlvQJtTO-OhFRTrkYy3l7vYA8Kh54Z7vmV3E1uv5a7v7C2gBZwWkY6dezzCenGtNYbD1PNBzSw9GNKeh6pDxsS_ITv0JGiTOTFNY3P90RD0FHa_L8pcJ2qxSQPO6S9AGXbTRYmS4WKl3iZuwJTLojaeu0ctT2tyXVa78EYvtNw-AyvXbqaZ7AGpMkZ6TxBEd0QKTI_e1vrA8tl2Do1rugQSMWrk-pNdQvExqS0_cMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1560dfcd3a.mp4?token=NlXheUCjWEEIc-yhEnuw8Ye7U3xHcv0wkc_uuB3KRfze7WdZn9JD4-302ifPp6i6FI-jdWstewTJ1BEcNtqgiGBDKiNvcLGfH-CVDGB6R1-fPlvQJtTO-OhFRTrkYy3l7vYA8Kh54Z7vmV3E1uv5a7v7C2gBZwWkY6dezzCenGtNYbD1PNBzSw9GNKeh6pDxsS_ITv0JGiTOTFNY3P90RD0FHa_L8pcJ2qxSQPO6S9AGXbTRYmS4WKl3iZuwJTLojaeu0ctT2tyXVa78EYvtNw-AyvXbqaZ7AGpMkZ6TxBEd0QKTI_e1vrA8tl2Do1rugQSMWrk-pNdQvExqS0_cMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
بخت یه جوون ایرانی وقتی ساعت ۷ صبح به امید صعود تیم‌ قلعه‌نویی از خوابش میزنه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/Futball180TV/96686" target="_blank">📅 21:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96685">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2POhQD5Mme3zY2RE-rtO-QIX2wGoZPQQ_wftPxQrYwqW56nZF0UlIaq1X3oCoS7To5rKX1NfWsc8gnhvE1Bo45ODXQ8UXVv3l2Y3KR-jsK2wB6L0F_TXdgnllWWOtA2O6XJP-FIyiqFbXefgGWauhVXqWRoXGqg-mbHjAv_FqQE8_UXrZZOQnItyVkKK-r8qV-jSJPTW62EV59k2arBv_-k5NeSsR-yg58GJDEtLPUoS4OCC4Zgw8wwaWtxuitZbW4vexVlIUYkClsnU3WbSYlRbX3eKGkI9Ehs0qqkbyIqFjRmbnHYOSMA6krqMEY5zwrHE3NH0Co4PISBecUgiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیکلی نیکول اکس سابق یامال تو کیت آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/96685" target="_blank">📅 20:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96684">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a512c25b6.mp4?token=u7uKC8bdJ3yT72G4WOCECded5clOiC_Uo2alKiguLZgVJa-Go3-PewQRlo8cxfLefwNuys_mAscmwXA-DGDXkSgnDJj1alJNdHeRjYn52Lc8_UbDuVrO9RaRLe5Xc5W2hCAo4TzdTUONVh591TcyyJ46uc29B_blTBZDCOE5wFcwiN3jnd4pR3imtqL9F5GrVqtKnG4OmKUoVZrRmcCT04M4mW9sbFRNXfyHP-BB4G3SenD8eWE7pM6EEuadDEkQAUs2F1PH7080zfJTflVCn67snuJ1UDcn71yHf_tl4KheRg5HuEFVw7pKwFBxlxL6Qf78SBzGqM3WwB0VKGthaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a512c25b6.mp4?token=u7uKC8bdJ3yT72G4WOCECded5clOiC_Uo2alKiguLZgVJa-Go3-PewQRlo8cxfLefwNuys_mAscmwXA-DGDXkSgnDJj1alJNdHeRjYn52Lc8_UbDuVrO9RaRLe5Xc5W2hCAo4TzdTUONVh591TcyyJ46uc29B_blTBZDCOE5wFcwiN3jnd4pR3imtqL9F5GrVqtKnG4OmKUoVZrRmcCT04M4mW9sbFRNXfyHP-BB4G3SenD8eWE7pM6EEuadDEkQAUs2F1PH7080zfJTflVCn67snuJ1UDcn71yHf_tl4KheRg5HuEFVw7pKwFBxlxL6Qf78SBzGqM3WwB0VKGthaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
😁
دختر جذاب ایرانی با پدرش تو ورزشگاه سیاتل که به لطف‌طارمی ناراحت رفتن خونه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/96684" target="_blank">📅 20:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96683">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/207e25de79.mp4?token=ZZ5GhGDDtSx4_t6SS8VT-VhXKBN0Yo6psn1Fl0YyL1Cd2jxNczae_xCpXqVhcMjolCeTuUHdcS9h_HT6Kn3Qf5SD1grGRanMukhREvHlzR3DjGG7DIJHf3BLKC_3RZuRhl2xSbKabpXeglDSV2wfhpJCYuhx9r_-gOIXhowKF-5y799SCV5WWSiuApw5o4-Bhjj7le8BaJu-zIBtLGEWb7oSXksI9E3BzzEMfb00hjwniWGnP0xwF8wUd0JDjVzsby-GeLA77WUiEu_D38a65xz84pk_vhS3ld86DQiBdIcCAggNwpqXGfqZvMTLhU0GpUOcwZagpKW88vW-AhFeT1g5uqhaXLpj4QkWp3pjsMgwylrxpU96RH3oU1F9M-83IA6It1RG_VHQhkxILPl0sL-U2b7cU75iguekuF8_8mu-uGKxZdrRflRxi1wA3g1TUr0XkrFdC36hE9CjO1hgPLfO4N1-I_wQT6XnYf_O2HeIXt4oH0PnJLQDnl9yH0f1ZY3AlWQQNJPwbnHhBQYInMedzKoi8vkm0jZuZDDW5PG6iXgUmtdcdk0aDFIK03KwDMEnMXTKO28Tw0tVBEkKcYi6xkHo3YDbZT4Qm3nhk6v3CVgPCCGok6RpGMJVcApzcFp1ZEIeIiH8eg1BloO3AQCfn0QgXW3vPpBJYTS8KwU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/207e25de79.mp4?token=ZZ5GhGDDtSx4_t6SS8VT-VhXKBN0Yo6psn1Fl0YyL1Cd2jxNczae_xCpXqVhcMjolCeTuUHdcS9h_HT6Kn3Qf5SD1grGRanMukhREvHlzR3DjGG7DIJHf3BLKC_3RZuRhl2xSbKabpXeglDSV2wfhpJCYuhx9r_-gOIXhowKF-5y799SCV5WWSiuApw5o4-Bhjj7le8BaJu-zIBtLGEWb7oSXksI9E3BzzEMfb00hjwniWGnP0xwF8wUd0JDjVzsby-GeLA77WUiEu_D38a65xz84pk_vhS3ld86DQiBdIcCAggNwpqXGfqZvMTLhU0GpUOcwZagpKW88vW-AhFeT1g5uqhaXLpj4QkWp3pjsMgwylrxpU96RH3oU1F9M-83IA6It1RG_VHQhkxILPl0sL-U2b7cU75iguekuF8_8mu-uGKxZdrRflRxi1wA3g1TUr0XkrFdC36hE9CjO1hgPLfO4N1-I_wQT6XnYf_O2HeIXt4oH0PnJLQDnl9yH0f1ZY3AlWQQNJPwbnHhBQYInMedzKoi8vkm0jZuZDDW5PG6iXgUmtdcdk0aDFIK03KwDMEnMXTKO28Tw0tVBEkKcYi6xkHo3YDbZT4Qm3nhk6v3CVgPCCGok6RpGMJVcApzcFp1ZEIeIiH8eg1BloO3AQCfn0QgXW3vPpBJYTS8KwU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپید بین هوادارای نروژ : چه خبرتونه کصکشا؟  من اومدم هالندو ببینیم ولی چرا کلی هالند بین تماشاگراست؟ اینا همشون شکل هالندن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/96683" target="_blank">📅 20:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96682">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktz8DQ4dU2K-4gBYS_-hITKDL18U7x6PJ329-BDUeUimDd9c3PtonUp8XEPeb0Je90dXR3Wn6Jr3BnSet6E7-EZhQ8ytwq_UJeG7DpbFTTffSLKLz28enfFLPVziAJTke2H-fTdqCjNY7vNKsPxgC4GB03AzraGZtk9nkgma7vfCFOo8faZo247h1fkKtnliUJ-UM0RTIw3-wxlbYTlxTBzjP1SnUMcwwiOTyUAMrOfqoWNzqtuBzl_bU2v8AyDEPkGfipgC6-26wUM95olhHj115JT3PHxEMknFyNze2qHU9TLGVE3nFIMqEaMTX02PZS13Ir2UUuEytGg08ubVCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
لوکاس تریخو، مدافع آرژانتینی که در لیگ ونزوئلا بازی میکرد، قرار بوده برای بچه هاش کادو بخره ولی چون مجبور بوده برای تیمش یک مسابقه انجام بده گفت: وقتی بازیم تموم شد، براتون کادو میارم..
🔺
بعد متوجه میشه تو شهری که خانوادش زندگی میکنن زلزله اومده و بلافاصله برمیگرده به خونه‌شون که میبینه ساختمان کاملاً فرو ریخته. بعد از جستجو متاسفانه لوکاس، همسر و بچه هاش رو از دست داد.
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/96682" target="_blank">📅 20:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96681">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af312cfcd3.mp4?token=b2LVYG39gy9fEKLS_jFQS1SMl0EW3sEh5V9feiuSt7skhDKjfgBNy9eyd7YCR1ybe5t38vv6Prchh1DYth5k6VZQKA2TMYTZvBKyYNc1bChF9U-hsA9juW_xfdwQTOaIq-bMYTQ0xDnaZlKWvxTODuR2UAvmJFwKR6XSqnHD0AJ4i1Am-rAUKRc8aHvS4TZC1LcAEXxjRR_pVMhR8REKS_5zHC5QjdMGYhKXMcaLHqtK2PJ6ZiugHK6SxtxIGlFmsYi3_d9yxBmwkrSKqfcY_s5AmVx1MCgJAcmdsgQ7OxK-5BK46LGCCINco9mDTJlBwiRKKmi9xvBAnGTf70smVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af312cfcd3.mp4?token=b2LVYG39gy9fEKLS_jFQS1SMl0EW3sEh5V9feiuSt7skhDKjfgBNy9eyd7YCR1ybe5t38vv6Prchh1DYth5k6VZQKA2TMYTZvBKyYNc1bChF9U-hsA9juW_xfdwQTOaIq-bMYTQ0xDnaZlKWvxTODuR2UAvmJFwKR6XSqnHD0AJ4i1Am-rAUKRc8aHvS4TZC1LcAEXxjRR_pVMhR8REKS_5zHC5QjdMGYhKXMcaLHqtK2PJ6ZiugHK6SxtxIGlFmsYi3_d9yxBmwkrSKqfcY_s5AmVx1MCgJAcmdsgQ7OxK-5BK46LGCCINco9mDTJlBwiRKKmi9xvBAnGTf70smVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
▶️
وضعیت نفرات تیم‌منتخب ایران بعد از گل تساوی اتریش مقابل الجزایر و شادی مردم از حذف شدن تیم قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/96681" target="_blank">📅 20:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96680">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTYsvJvfzH6hu4-j0V5ob6GgdE-iBGnZc60xMGQdjRKo8rzVXvEqSjPTmy_zWyY6vL9su5FobwA0r1tnR-5xP_ShUMSnz8XWb8qzITzQO96DESD6rmSPyi27ZAdsWXE6pZq1YeGYckV8y5n2NJmFidxxkL3USd_yVKpHthDTcBMoqUjPuKDeiIB_6r6HZ3dJ3EpDVVSsu0ek0jdL-7X4sdhLxnbiFlxRcWIxV4vBt4erO5DSk_OkuGHiG49oWe5GqiE6nFJvZYXjFhAPbYSnT-HLJUfDBQcY8hteZ65G9Mk_iWGq7hx9tNhfvPpQZ_Be7TI1Di8vuuNlDKT1cydkIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
🇵🇹
وقتی‌بازیکنان پرتغال حرص این‌دوتا بانوی جذاب رو در میارن و سوژه رسانه‌ها میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/96680" target="_blank">📅 20:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96671">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hoe7SEvRNFhldGRbdMoilkg1mL4Kc3tVK71cUgRmkPLENSJ1wRNoG4xMHwt-CuJjASbsw9rzlXElmdg0k4rmhwI_qXxRx34Cp17H0i2nBiIxIndDUDPWA8pZcsSwdx0sJmJUuMoU2_MtaekheyYKII_RYcWuW9IHw4LCdb9kTgy-rElgiIRVtawLwA-qIiZxxbEiGGn3c92OrwicIBVNM2nxY4_Njp-GXhio0fjAHP6MKshQ4qFRA7oyJyjRwDSK-BOpb3OrMZzFpYusN2sXpxj0apKxbAwSQwxEsh57crSiZBPu8XbF9251j6xP3RoPFDWBTqzG85AK30BANI_wUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QJiGhs7i1RQlO2-veb6lGjIeG-Snx13AUITp-YPliEkhNE0PfldiqA1fcbqf0tdDakpdAQjt1VqK-LSac66gZwzbmq-ZEZJCokDQzQ-YY6oLXjeQf-74mtjCTdQTjfZXEG-f6b3xMBc_JhQ3fMRo_FkwrfWfCmbdFt0JCN76BhjdPzoRBXmZMnNxAUTEdpCM9xcDk9SOpFmuDKisXmNP9zz7VB3x2nyil0DwTeqZgbQwtjmXbRWvsCmNoedEXd4OnIgNh9ZP4lAyDbBaR4KR8S0A1SqAcinuSrlWlaKxZUMfNGEk6yW3MQlwI7GcOEUsqzX3i4X46lQwYGlsjnk6nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Seqz263jj7lsDNF8fSrDcZ2mzXN8SisGR2dppJ7n5nRYpAzJo-JxWj5JveJL0ZuOfIbKGr0aFnh_vHPBewvSySBcO2GM2DrEXU8StjW_j6_kg7K-52g9W4c_Q5YrW6__vH4Znh0y30xjgqcMG7KsLTjuzQVYAfnQXyRAmS8AGeiUGq8GL1e-g6FbcQUXqU1Og4GIJyHopg-6t5n6JleRisoz8nCpxfy_sFpdEIDvcEdJ4GUC9W7J-E4QpvavHrPNRsuWT2bN2QlXu6F3rdvJLZNB2E3u3PUNDYjOvTHY4H713voljKGyuhKtSDaRMTbv_2oMoxJeIj_P4cN8Wyrhgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZJFSk7oZrDkQsgZE7k4BqmGgHLXFIKPx-LMvXAIgGYZQF9YWPw0hUysYKkFkg398cI8qKveWVP8uNnryOllnDZeLDgtiV7Hca0Ai_I4qp_xo-TwtIhmy41Mo8NOzdVJ0ytOZCxBMXYxBUGgtcQze-mNSF6iJwcWAPbKX261bx0SGSBOKgQE7mdCg9pdUXj4eB-jzoimB9ePj-rGPM-A0HQeq1weMzn1wVkiBYv-hq1gmK-PrUkhJM-PPn-z_zMpvCLQAq7T5MSwsGm0vyWpdIzh34swQ8I73SJS8Yxkb17q-zQ7_yN4PgAKuglUyj7p1wvQu9prkGXn7EzoBRSIUww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p52Cnc0e6z9njLp1kp_yqZRvDy9A8UubstRvT2_JabDXk8ScQGuzc5PL-PwBfj-VqQdXHpDJu4HaTYkmo_cnsHIo7nf5hxUWYPh4BBhze-39rpnYiCCyKHEP1YG-jHzDQW4xcGrjZhV-A5Ufr_Psk3iaX9igN3J2yzMgFgNxUBud7xFlyFIbs5UdI7DT9wGhPeMapTdVQsKcKY7RAn_ftD1ykjMRpBPX6Pj1oLCjNTHybMreE2lkM44nYzTDsgQaG8BzJiTVOznZHxwaYtKMnHdZ2JGcnjOQZx7-bdMRluDC3m3bGNFhh4UYmvZ4tWWxBD2glyXqwfOfjIC6VZI5OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/onkTsbrwcVWnG8tSmNy6mFAjMEkuqhAs5Uzq2tSyACJjxFP-LGAhaFku5b9m4qkxgbHeWqgUhEI_Gg6ACisiq-r8c7Hl8FGNOgXub_ql0kdGFpCwV2wznjEWHj6UHjA18BnwNGnPo7idJIGbINoBjzW2G2kLMdfAPeJmoQm0LLj80y6Rm_DmkT0hL1B5vnxP3u-cprBkgVXjUmta1rmERcbqej2Sl6U1TdyPZBvGDv7ME0KM0-dkE_vDnfOgds9_rDcghbRX_kgaM9JzE7f2ZQfEVV4ljdfyHNib4oRv7QhiKTcFBqegPMjqWvQilWCUi_rD1vGpy6Wlef2wLvjzgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ha42RFq3Ovcm-IinnnfkLw8xE48pd0cegPgFYkXADKG5Gnqc11ZmQtN_x6PlGLMGLBVlHF-DntA3VlAtECmMzbowr54qzuMtPwchnwKbf0ZKAc33HvHM8-tLicENbF-NnR96F92cpGyFH_k4CnLBYE2gkMoyOLTCxi3JkRctGEfHszQMyC06zzNL6Luqs5ZcSmFfjHJhISE9-xsawAjJvV430WUh6yg_Uo-U4baYSo8syxEdd_FaeZj5daIOwUlmcVZ5vR1cW_YKv5u1wC6uxyyYiORvWY96v7X6C5qGhAZYAkApuTogbvOFocfyJALjCiQiQT78WRom3IE4xdTWsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WNxoNYaDjBO14pKd0ofvjy_8nIuXEBBb-eMdl3V-C86il2eLjFHhb-7iTbc--eHVmpb1wcXMO08PJBRH_Bz_VRKCm7QssK6wKu3OWh3Verp6kDiDEdIe4eVBkvwsGWviG7MVeDNjCUL-3t7NAuJ1mvl1_MvsYbTN6b_r1cjVIebUnAJuGzKqyKGTB0rJELZF7Yp0fhaaSQJmD5MdjJFzeFWceUWtlW2eZ7VK03tAs_3icmqUJ6BjOJen-HNVTud-lV-w35j9U7ZqjJnTn4tAziAqo0e8be0gcy9fWti8qXv3t5FO9s0JyDM2wIwDkol5NKtRNWxon77jnY-Ff2vJHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V3pQ0h1qCgIZQSqQCEpJuA1ahgns8Fb8zpoKnELxddtmwdXIW38lWj_efgVQW_yDpAfoMaE__twxlSgiRomlbEMN46-ysQ3cq1wdM6lRo3Gfjff3EX1xHbEQ5PXD6NvjmMXOnJLZ0E6zTlbeqNe9XgByaGV4-igR51YwXwYXG6jX4qc-8tAcmcL1alK-u4NiX9sNE52IaA9i9gz9_OmfQFtDKaBQYk115eJSCuZnV7A2jE_8TuX6wkz5QzkN1JyqbUcUxQAvVkP8JXWV-t2Z-nSCHLWL1SJVSeUuDwMm2sa83cTMXaXneXbVGlkqomGJTXyz0sUlvj_P-h7mp_oexA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😐
🇲🇽
تصاویر ازدواج نیکی‌هرناندز بازیکن تیم‌ملی بانوان مکزیک
💍
💍
💍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/96671" target="_blank">📅 20:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96670">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29e4bda6f8.mp4?token=GUCWLjEXfDwDXh3keW9yLG35PxKguKABgMx5uHVRJQRrt38sHL9EzYP6cP2IhT0i6114zH_sha8wjpbBlbj64iKR6cytLUD-3MvcyNq14AaV_Uzb2k1k-FADv8IQfQfdpHpsc1yN2OYBFRrzQs9xaoriMTeKwMc0-X4HjBBRw8ytka7go2bdICyQc8dpaIQ9Hrh9kTlW6s3qgYhB98RIfn9Hdbn3pQabyHTM7d0dN808WWHyg5p3hSlYYrwTNinabFc02f3VAY6EV8omNz0irZMuO53GNk-JcEAsbVtqkloDEY3FLm4XBuXjLObTPNleQwkMyCcozJ9lURa-8kTaxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29e4bda6f8.mp4?token=GUCWLjEXfDwDXh3keW9yLG35PxKguKABgMx5uHVRJQRrt38sHL9EzYP6cP2IhT0i6114zH_sha8wjpbBlbj64iKR6cytLUD-3MvcyNq14AaV_Uzb2k1k-FADv8IQfQfdpHpsc1yN2OYBFRrzQs9xaoriMTeKwMc0-X4HjBBRw8ytka7go2bdICyQc8dpaIQ9Hrh9kTlW6s3qgYhB98RIfn9Hdbn3pQabyHTM7d0dN808WWHyg5p3hSlYYrwTNinabFc02f3VAY6EV8omNz0irZMuO53GNk-JcEAsbVtqkloDEY3FLm4XBuXjLObTPNleQwkMyCcozJ9lURa-8kTaxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
✔️
🇰🇷
سرمربی کره‌جنوبی بدین‌شکل ضمن ابراز شرمساری و عذرخواهی فراوان از مردم کشورش، از هدایت این‌تیم بعد حذف از جام‌جهانی استعفا داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/96670" target="_blank">📅 19:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96669">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWaiLvpD0zeTx_IuuPih9B4srXhBAy4sl50ViSTFNq4cUacuBS99TQL8b0s_UM7uSSqzyhIC97D6TFjrzus2mll1lSEP_VgVBVdsRpU3ZIPZQbaK-p9QrgZDoReb7DpmzAZgyWhXQGb9OpSU3K-1UChuCxa_F0197YN7orwCWzPqQUgjrRGyk1uNlZpNCztoNKd_7C2yrqaLcpCcVHANsn9d7AWrBVdPboA-xGJDpcor_gMpuDhzuBUpkQGA6WsVPVyxnclNdB6cR7sx7bFA5cS3ldUxwVx5Tv5UQ1uQpzNMZ9pD5myOvFchDm0FVdRbIx7SNn1vhmXNXLUwr7X4Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باشگاه منچستریونایتد اعلام کرد که مانوئل اوگارته، دچار پارگی رباط زانو شده و برای مدت طولانی غایب خواهد بود.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/96669" target="_blank">📅 19:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96668">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3b44065a1.mp4?token=pa_IcLNrbo5UiA_KcCiCy7R_NWlCrvLQlWTWzrXBntbwAa_Rzr7UTqie144oRBBR5zcpM70vinAlc9GCre2bzGMXmCrIcwY6c3XYcS-r6YYPLuHM0DTbidiTQXE4BJDw5Wn5ZwsLc2e2V6wiJnB1OZ-ahbr5KWx6Y8Q99CvbMwwm_SaPcJSTpSLFRW1NEeP711t7nktobeCRKa9AfzSMcw6J3l3c7sDIyZ-c1DtX_0YQNqkvON1AbvUvPSIs0Ku39VE0FGWqZrki21qyGShQYZTUM9cUJCbYBUwXwBEVQQumH-IvbNIKShxHjVbTPuXyJ9O-Opjcnl7Q6QyKvmRKlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3b44065a1.mp4?token=pa_IcLNrbo5UiA_KcCiCy7R_NWlCrvLQlWTWzrXBntbwAa_Rzr7UTqie144oRBBR5zcpM70vinAlc9GCre2bzGMXmCrIcwY6c3XYcS-r6YYPLuHM0DTbidiTQXE4BJDw5Wn5ZwsLc2e2V6wiJnB1OZ-ahbr5KWx6Y8Q99CvbMwwm_SaPcJSTpSLFRW1NEeP711t7nktobeCRKa9AfzSMcw6J3l3c7sDIyZ-c1DtX_0YQNqkvON1AbvUvPSIs0Ku39VE0FGWqZrki21qyGShQYZTUM9cUJCbYBUwXwBEVQQumH-IvbNIKShxHjVbTPuXyJ9O-Opjcnl7Q6QyKvmRKlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
📊
🇩🇿
پاس‌های فراوان الجزایر پیش از گل در بازی مقابل اتریش که رکورد جالبی به ثبت رسونده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/96668" target="_blank">📅 19:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96667">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IRKFaa9t7MuiMcMN1QylkVdT65KfaTsfDenSq8YbshfBkYanGCVkxWis23GoooemuZH6dQj0TTfXnZ6DBbfHCtWqA1-uF91R75cOtUc-XBTyYQsP7kWAYVIkRk8xn7Wgp1MkA6QMHjQ5QalrIkNGvISKYFCxzl0x6mhrLJjvFh68D8StvytvvzHocEm1_xQjwEohP8_oLPE8d_CYXPWghtYLR-WXBP9CubkGUutkiUVXQBOXz439aOnHnDoueUuYA_sRkvanlZue2RaWjXnVuwyn0l0ZeLcfyU8ItWDDVT-vTfR7Ydd2uDodAT89K3kGfbRKXHEkT5fuz0KGs6c-6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
😐
جاسم بازیکن کسخل اردن بعد بازی با آرژانتین برای تمسخر مسی این عکس رو پست کرده که جمعیت عظیم فوتبال دوستان زیر پستش از خجالتش در اومدن و مجبور شد کامنتاشو ببنده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/96667" target="_blank">📅 19:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96666">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94d5bf8566.mp4?token=Jis9mRTP45zq4ECdWnbamGp2Ah1fyCfQivu4bqp1UdqskVUcK4NbhH6njsr1uz8zYTkWxlwaQhtY_IJoVKLkdoz7jMo1OrAMhM3bzwpWL7RsoFKapG8ggfD5QkqqsUOZ4aUCJWePy0kGTpF2SyvcNaYAAxR3bND7XytyeaW8RP7wC2LmYhqhjgyW9LemqZt5IB3FsZPKF28pX6FptM9ZuoNVsNYPxW_PJkkSN5vUCAVGl6GvNF1ilvxvqb-duAg2YbTfBMbdjfMrh3JS5fnNQO84p3O1n6-JTiLPdvKcALIe-fNZofIPWH0-Ok5_hnJSntF3cfLqnoHSSLdY5LraBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94d5bf8566.mp4?token=Jis9mRTP45zq4ECdWnbamGp2Ah1fyCfQivu4bqp1UdqskVUcK4NbhH6njsr1uz8zYTkWxlwaQhtY_IJoVKLkdoz7jMo1OrAMhM3bzwpWL7RsoFKapG8ggfD5QkqqsUOZ4aUCJWePy0kGTpF2SyvcNaYAAxR3bND7XytyeaW8RP7wC2LmYhqhjgyW9LemqZt5IB3FsZPKF28pX6FptM9ZuoNVsNYPxW_PJkkSN5vUCAVGl6GvNF1ilvxvqb-duAg2YbTfBMbdjfMrh3JS5fnNQO84p3O1n6-JTiLPdvKcALIe-fNZofIPWH0-Ok5_hnJSntF3cfLqnoHSSLdY5LraBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
😢
🇩🇿
خوشحالی الجزایری‌ها از دریافت گل‌سوم مقابل اتریش و عدم برخورد با اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/96666" target="_blank">📅 19:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96665">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXePFfY5spNHuZ6WamMoSY-t5aCVPvdN6oMqHNwykNPQcALXRALyDmkSWXNDEzjIgU-mdYJhRckXr23J0S3f3duKwzbSQB5z6nRa_rQJiwj8d8Of03dYg7Tw-pEhwjYJ7kxJBdXLGlhNyypn6XzEifFS4kHb2Hw5rBrgXr_LxO0G2lxVdvGQkPiDVnScBGuJecQu82YXnpjvs_J-h49pCs6MIxHYpYUdmi-cx8dtglv7S6BKx4NnPLN8zVU2DCEGQaSiCDegJI_kMeMGGu_PEpRMhDLQNMpMsCtEnBu-O7CIJkDiVHtj6XTnjjSUH2F7WdvIQmuNpSYAb4PTZTiUiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇵🇹
🇵🇹
کریستیانو رونالدو  :
• ۲۰۰۶ مقام چهارم.
• ۲۰۱۰ مرحله یک هشتم نهایی.
• ۲۰۱۴ مرحله گروهی.
• ۲۰۱۸ مرحله یک هشتم نهایی.
• ۲۰۲۲ یک چهارم نهایی.
• ۲۰۲۶ صعود به مرحله ۳۲+.
🏆
- عدم کسب جام جهانی
❌
.
📊
🇦🇷
🤩
لیونل مسی  :
• ۲۰۰۶ یک چهارم نهایی.
• ۲۰۱۰ یک چهارم نهایی.
• ۲۰۱۴ نایب قهرمان.
• ۲۰۱۸ مرحله یک هشتم نهایی.
• ۲۰۲۲ قهرمان.
• ۲۰۲۶ صعود به مرحله ۳۲+.
🏆
- یک بار قهرمان جام جهانی شده است
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/96665" target="_blank">📅 18:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96664">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWY_Qpo4w3TuKLt7yPIr4QU7lNyAuRYCqfqknm-Qpv4yjUf6ozEs1q2ZqkGI0EoApa0A9_c_c91-UdgkzIPR3S-n_kgbuYvoe9h-aK4ekCnvh-zF6pCO7EcFemID6m3hZ5jN1DrhUpWRviscxb2x09SWX8ZmYRW6TInMdS9E0Ea876v_41a_SDgYngP_hIHW_lWNrE70kxxqJ2SbecZtpKb9E_p8mFNEq_NkhmmyKP8g4u39tBG8_AL4pcsvC9MnJs-mslSUf1hk84aaCfu8uQfiOw3kK10KrJB6xyz_jH59-ug6Wdic5uqQD91Mgva_lOLkCPyUUO5G3xS3qxkk5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇦
🏆
🇿🇦
پیش‌بینی اوپتا از اول بازی امشب مرحله حذفی بین کانادا و آفریقای‌جنوبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/96664" target="_blank">📅 18:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96661">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZO7nFyMK7kurZlSf5Id_wTSbAw6TCmXiDYfyqJV496kImmDNmxRdzqiXbbEWWKm1ns4l2O4mt-5ut6y_9z5f03XSaQ3t9HDC8-3CGNHDIV4yZxTx1EfLt_HZJmVy-RzIwDsbLwHsgn7qVXS_2pzAQ2ZggOHlBzh_PeYVXCsJxEVDnU1por8Odiut60XjY6Sino6ZvjZ_iBAzpZ-LQQV36Bex0Tg79sH2UBS5Fo3gFzSlXpKpCIMRulDYHzB2m8hkWMlDfEZV5zZFfUByMYFbjDSdN1LKsU74h7vQ8P7wnpXNBcgPueiCAfSikX9gipKhlnyBCZ7N6Ob1HbVaiF-UTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oA0tiCQPiHpcX67DZGYZyLCKB06-nkg9u909E9EjaiLqHA35az7wi9zsApLOox9I1eRIRTsW1a9z2v-1JFasxbjrT7AbKBkF0Dal8hcGWcxok7ev4gnOkjvAFeqkG-A8ndkI-ltI18zEZ4KO243RF7J4Sl_JbJW89j8Ce1EUvn9Ijf03B_D5iTymI8CIgZvHsNlulyzen0Jr8dpv-znxygdBTgzdrGzb_vRQCyNYfCreRV2sTCvgTVVq6MW02TDUhLv5IdAPQ94IKV94BDfUM0DPl6_YYqRb0eO4rIYfdD9Lkgf7amIgaxG7AvRsQ4zkgLNmEfwAbp4a9ix3WUvHnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/phMI55Co7H1ryIiHVR6-p__MSvuxLVjsD5ns3yFLifpQKK5lXD8iwqzX2xo12scgpNOZXAvOkJ2QB4gfQnQGaCknros1RQ1RFxBDT56dVLC4sr_G0HQdONm-Zywn-qd9REaZOF7pK6jLVyBkXcca0OMopiuNQBAoICAEZYUKYv88ISpuhaoLDTwvhliedIAY7UuNAuErCk6al13MBg-fCv8EEQc4Q431qTPPRGGCm63fGMpCbJLDyG8QlfSgcj9hcWyicCLtiubA7YNnKxiUWCRiW6iuCIX1Zld9gRfLWoj27S5m8i9mezc1PuTQIXGPYCaa8dw1rCHSXVxxvhS5ew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
🥇
رئال مادرید مرحله گروهی جام جهانی را با بیشترین تعداد جوایز بهترین بازیکن بازی به پایان رساند، با ۸ جایزه، پیشتاز نسبت به لیورپول با ۴ جایزه، و پاری سن ژرمن و بایرن مونیخ با ۳ جایزه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/96661" target="_blank">📅 18:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96660">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2382f7a63a.mp4?token=AjFtGCtGpuNxpyOl8BzyPrIXrehtQ3nOZQxn2CoDoivjf1eSC5gfeWvxdGGp0gnpYCwL6v071wEnu6SmSd5jMkKQw7JCFoRY50jbrXaG5aiNGfuhnkbJ5GbCNJaZ4yE3X61nhUbnUsGGCpHkzN88sJiJNBz8VZtyB3xeMnrIO2XH-gnXxNrIpW_AntxZbwBGEWiefj8Bn_9cz3W_qYFUUt_OumxoZj2UuQbG-QbRiIfjSS0K0awkfLoLxNxiwCHHGuzZT7xTENTNcd-49urHtPSqRGiLMCmZNoOcQ2fiiS8nyBI_ZTyeS6bifBBAxSa3gvug7A_8UjvOxm4fhJhHQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2382f7a63a.mp4?token=AjFtGCtGpuNxpyOl8BzyPrIXrehtQ3nOZQxn2CoDoivjf1eSC5gfeWvxdGGp0gnpYCwL6v071wEnu6SmSd5jMkKQw7JCFoRY50jbrXaG5aiNGfuhnkbJ5GbCNJaZ4yE3X61nhUbnUsGGCpHkzN88sJiJNBz8VZtyB3xeMnrIO2XH-gnXxNrIpW_AntxZbwBGEWiefj8Bn_9cz3W_qYFUUt_OumxoZj2UuQbG-QbRiIfjSS0K0awkfLoLxNxiwCHHGuzZT7xTENTNcd-49urHtPSqRGiLMCmZNoOcQ2fiiS8nyBI_ZTyeS6bifBBAxSa3gvug7A_8UjvOxm4fhJhHQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کلیپ کاربردی برای بازیکن های تیم ملی ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/96660" target="_blank">📅 18:13 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96658">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vo4McMsm6DDst9ABZBvqIit5x268PPu5aVIMzs-Q-bihQ0MraujsuC5B25OsODvpCfwtsTOY206MwxXjdnhvKh218NgdlVI6J50ljeWn_G6KP1dk-KhltLtnH-2Q7dDcg_kXThxMlOrwGzI1ShgGKsW2Keb3gN74kU4R0Q5d3NPhbRu6f8ScQmgTDHKBTtSTCTnUFSFy83U8IFRWvi2Cg5MQMWvvPm471-ZT_w3rM_6Np1BITJWDGhON-E7arFNl73DrQ3Mv6yGSpBjBO7UJS5dEipyXB6bUE2hFT7BdOZdhCxj4cH_06TXt3l_ARBEJfmrrDXPkOFe10kZaIkUQ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/myoxrrvRZLoG6WC0X2IW-dLRUZmd9tKQGmHIJvsGZaHTBp-rOyN_KY6a2BYPdQ7mAxMzyQa8_DfjweRDvg5LkNKQzCHPOLitWAUtPoKXGCSJRzej7-y0jOjltTgoO8QudILFdZ0f0bxpfx7GLfJ0RA7tEwAChlos0G-3A-aXBYua5dV1OarS75FMLHdbmXkYb-fgeMA0aqlz93bVqVNJbQe7M46mcwW3EhM2_SSBzMAvO1Q9WQRZqRSLE2ES5mue-ScHnZn-ZpjkYn-J7R4rRYpQVYGGAN0kTsv5BLVxQb47Qo3o3AzPj8le38BW5uAxWSYui4vd-_FXYfFbEMTVnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
یورگن کلوپ:
یه استوری از سادیو مانه دیدم که عکس تیم ملی مصر توش بود و براش قلب گذاشته بود. از اون پست اسکرین‌شات گرفتم و برای محمد صلاح فرستادم، فقط برای اینکه مطمئن بشم دیده! اینا همون خاطرات قشنگیه که همیشه بین ما سه نفر وجود داشته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/96658" target="_blank">📅 17:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96657">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gt456INXgWqIQnrZufnjZv_HQLpAE1F6Hpcdw5Pl4KlHvi3_VXvQu_bnbGBpit9vx3eodRVGbb2JxfvPH6YM8SQLnf1J0X6p80d29h3Jj-4quc69rGmJWvmkq53XbKomJiuUzPpssTpZZgfQj5arr5EtZ85XiOHgo80BfKEKYAEok7avPr_cFX7s792-_veXJdBJ1Uvau6nNHSdP8gO45gHUp98h5gUDg93dSeotaXjq2urMe6Cd7OlOAKiHt2oUugeBTky5zDaK5pPt0kPg-tn4yFB4bvy_FdrVan-aOB7dmbdLmQattG6-fORpHnC7Eqdj2yAYX4DHEFPO-vvd5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آرشیووار:
در بازی کلمبیا و پرتغال یک فاجعه رخ داده و گل کلمبیا که 100% صحیح بود، مردود اعلام شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/96657" target="_blank">📅 17:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96656">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDpUqeTBeuLDPZwMhjgO059FR3hEchi4ZlgJPf9E5tIrbC5K3QdQ6n3HwA8BwQBwNZ3YcycqIhn-5XVjjlLMTvA2fUiJSxxM9Zkc9zqCfGu4ZG1dXxq0QkClGWwJ6fn554g8nr6k6dFj4JipAGkqDTnunjIQqx-avFEm8EutaxdkKT7Wbd7VesCedP9F3vmSRes5epqCaEqWfjLNod0iDq2vzyKisRY9oeBoGJa-omGtLv_u9b7aBRBdcq9O_DV1nX296e6rfEJMhZfve8vZoQqpvYzWfQ0u3kXQ-gRJGT4Pzm_9F6uV38nlnA-zplOdkEOD46VrawkKDAf7s2X_QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان والیبال ایران و کوبا با برتری شاگردان پیاتزا
🇮🇷
3 | 25 | 25 | 20 | 30
🇨🇺
1 | 22 | 21 | 25 | 28
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/96656" target="_blank">📅 17:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96655">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjUn_7ZOprzf36HeOK9M7rhXi8pDVBO_SwRzHjYxyH_K9pHCYB6C4PxlaVKt0pd3BhjAC_vuqg6Ib5iVt5F4z5vlweFmoOO4lrk-W6Z6z9AVC351xXwdfyzT2_IBbetwf4OAo9tmnK3TBA779qgxgKX2aJy4Vau5tghwx23s4jP8kkz1U_OR21DGgQafMVFh-4dAMUv6X2TkKgzpLyeOszmAOlIOnAzY16BaxLkCZRsHR5r3VhFlEiezOM6ahakiFinX9IWit2Ql4xc8UR2l5ipPBN_vKNZS5iYCzYVTFyiwzo0pCoaqN3P7Jel_KirIenLgni0SHM33MJG9cb66AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سراسر حق محمد خاکپور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/96655" target="_blank">📅 16:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96654">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNEM1RBZQtcPAcvBJf_YRVAMOrKCYjj_7X-7gHm7oWZZ9nr6wJQLyqrm0OzfEaQxbsMsqN5GZ4Z_u4tfz2-zQNH8OasOAYWSZnfh5Xxh2wKGIlWrF8uVwpW1W4Ethac5XtoF67KWpyX5e8zAOZQuf1T1pBqHlVzE5fj-nIgtcsgfuaJa6yDijG-O3Uhhgzh7dyyMmEPEagZbt0HA8fpfWM9N4MWHLniOqKtWcc2KL2hDCqvHFpCbTjhni93qnob2SvVJs1Jd-_8ppSGOZQqp_aHNYYuDKiSdOc2RR9r4y_zbmX8E4ybLiEYwAyUNEkph1Sorpy84cA79IhBPg5MTOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
ارلینگ هالند [
🇳🇴
]:
🇫🇷
فرانسه خیلی خوش‌شانس است که امباپه را دارد، کاش او برای نروژ بازی می‌کرد، او خیلی سریع و خیلی قوی است، او بازیکن شگفت‌انگیزی است
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/96654" target="_blank">📅 16:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96653">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8757cd458c.mp4?token=cu1PM37_TZ8D_FbEPFep6JDaTHA7SRhF1xWZc2yyjBbboGzAcz9CEbwx1O6D52OUTua_U-wKqHCNiKgPkH3HecZOVi7zm7cxLxCBy_jfafUHbI_Lt6fRPIjApNsWC6BFc-RP-cA0UUvQH_RSdjKKfnodjrGEcZ9LZzLzoyxMfkX-i5YJKyCIYxHLmPATPw7mjhqlI6fEWybUtjA2j1u4ivg4sBPHYFqA-B1AoibiNEHBQ0RTQoAJN0sN7aENnMW-LVV2CywsjuZ-xg6cDNvdSwlkQ0psxw0y1tiY1gZA8g4GXvuq_T1YF4dEbAkpWw_AqOTodEqBldcPnnbpspEqkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8757cd458c.mp4?token=cu1PM37_TZ8D_FbEPFep6JDaTHA7SRhF1xWZc2yyjBbboGzAcz9CEbwx1O6D52OUTua_U-wKqHCNiKgPkH3HecZOVi7zm7cxLxCBy_jfafUHbI_Lt6fRPIjApNsWC6BFc-RP-cA0UUvQH_RSdjKKfnodjrGEcZ9LZzLzoyxMfkX-i5YJKyCIYxHLmPATPw7mjhqlI6fEWybUtjA2j1u4ivg4sBPHYFqA-B1AoibiNEHBQ0RTQoAJN0sN7aENnMW-LVV2CywsjuZ-xg6cDNvdSwlkQ0psxw0y1tiY1gZA8g4GXvuq_T1YF4dEbAkpWw_AqOTodEqBldcPnnbpspEqkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
😂
صدف‌بیوتی و رفیقای‌شیرین عقلش وقتی صحنه آفساید شجاع خلیل‌زاده رو تحلیل میکردن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/96653" target="_blank">📅 16:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96652">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZxgULz0fmfE5dFU37i3WEYzsAtEl4phWgM7nz9XD-yFx0Zh4O-mlLuz0IBQMIMTWmv9tKe6v2lVuixOGZwcxI23A1bqSVpHJK_TKmPdTBQEwB5dVud7ipKKsomXl55RihmsmejIL-ONJE58PiavJzL0guJ1ctHGvN1xxhO_R37IxFtwcbHq5mAcbBBYqxVfXDDJhlxzWnH9XGS773-S-Fx68v3jS2kJTreoJWj_87HQUq-fTtKPYMOFX1MoJiKDNhuhruDbK7TKciZlVqQNaYM9FxsxdL2mom40dMj0EMGziI1-nv625XJ2m8cJUhjZ2o6DFQpXD-16iCqiwqqgPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⌛
پست جدید اینفانتینو تو اینستاگرام:
تبریک مجدد به تو لیونل مسی؛ تو رکورد جدیدی شکستی و به اولین بازیکن تاریخ فوتبال تبدیل شدی که در هفت مسابقه متوالی در جام جهانی گلزنی کرده است. تو در دور گروهی عملکرد شگفت‌انگیزی داشتی و امیدوارم در دور حذفی هم بدرخشی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/96652" target="_blank">📅 16:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96651">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8146eb2115.mp4?token=mpY_uZ5qucNNnToYSiGyE3RW_Ia1Y4CofDx0hEO37FRvgRZFIiXBZ2y1QhGl0vUIjPGZxNtYBMO8kkQHCtHaeBGwReYT0Plc2ycFzHKtBNH4k_LiZkAKjkuITO6cnlfTAT0ICTnRdfp1YCeT1bvy87o2SU3wQxiGnjVgq4xN1hKqBXTIKgZN_sJq3GtIktSAP0fefwKdSj55tPTTCOeMV5Xedj3Jy8_dtXTOnmv7eIqj6vlBaWLtdoA8uQ1Z9dsPjXZjOfeBx75QLDnOgDEXqtdrRIjsMOvy2Yty_DYj2Z4hXDRQK814inYA7RwuKA_6sJ2vp9ESK76j_GagCmSRKA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8146eb2115.mp4?token=mpY_uZ5qucNNnToYSiGyE3RW_Ia1Y4CofDx0hEO37FRvgRZFIiXBZ2y1QhGl0vUIjPGZxNtYBMO8kkQHCtHaeBGwReYT0Plc2ycFzHKtBNH4k_LiZkAKjkuITO6cnlfTAT0ICTnRdfp1YCeT1bvy87o2SU3wQxiGnjVgq4xN1hKqBXTIKgZN_sJq3GtIktSAP0fefwKdSj55tPTTCOeMV5Xedj3Jy8_dtXTOnmv7eIqj6vlBaWLtdoA8uQ1Z9dsPjXZjOfeBx75QLDnOgDEXqtdrRIjsMOvy2Yty_DYj2Z4hXDRQK814inYA7RwuKA_6sJ2vp9ESK76j_GagCmSRKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
لحظه مصدومیت وحشتناک والیبالیست تیم ملی کوبا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/96651" target="_blank">📅 16:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96650">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4b9d9dec8.mp4?token=v2rVY7t9CByWlE0ZUZe91qFHMN-BcHxrlg5sgKW4xy23XOXH2Cle8m0ae_P6I5R_p2UUl9SZcKW7p7wAuy4d6AQ9hkIQwPLPVCOF95Ge54N3hg-yqcp5f4ck_7ufkLD8pAf66DX9OY3wza2sbqLfpTY_HOW-IhWoEi4YizWI939dA_05xIQVYKXKnxJJGQstANNXKkpTZJ3svem3Zwutj8mJbO-dLW5GErdsV0j0WTIV-S9YgVqRtzxocIt0t_P9rbuRb9ajbr3i0HnZGMN2bWhBbsdCApkjwapRvdzrTiC_awjmqiV3Jx8ffqqP5zfWOhxrLAWkl46rJ8XZnnMshw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4b9d9dec8.mp4?token=v2rVY7t9CByWlE0ZUZe91qFHMN-BcHxrlg5sgKW4xy23XOXH2Cle8m0ae_P6I5R_p2UUl9SZcKW7p7wAuy4d6AQ9hkIQwPLPVCOF95Ge54N3hg-yqcp5f4ck_7ufkLD8pAf66DX9OY3wza2sbqLfpTY_HOW-IhWoEi4YizWI939dA_05xIQVYKXKnxJJGQstANNXKkpTZJ3svem3Zwutj8mJbO-dLW5GErdsV0j0WTIV-S9YgVqRtzxocIt0t_P9rbuRb9ajbr3i0HnZGMN2bWhBbsdCApkjwapRvdzrTiC_awjmqiV3Jx8ffqqP5zfWOhxrLAWkl46rJ8XZnnMshw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗽
تو مرحله گروهی که واقعا میزبان شایسته ای بودن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/96650" target="_blank">📅 16:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96649">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxneN4wqOXnTwdqq_kRiJMYDwn2v4qcyLJpZBSnCyWHzJKwjiYQeGeM1Q4kBi3fhNcshPHKgkhxytjbDauauZQFavuUSo-nDNC55xSKE39Uyg5oLc0beiqSkoBDa6nItg4Ry0S7gCzKzQcLfEYpaXFQALTgKG6x4OlSixDd_98SXZf2RKxcXKwK4x-rNuzL9JMhS-WbDJkmWtDYp1szC8-G1-RNafTpaCLCsT7xovqgT7HyUllDPTA7yhA7XNOVqnCSe6SnAAKPgh7bNNq8e3Fyju4wx1BTe04H4DY73s1_YEOBICYa_lLv1vstVa4TR0oPuJR5uB8JEw56hxBXdzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم منتخب مرحله گروهی جام جهانی ۲۰۲۶ از نگاه هواسکورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/96649" target="_blank">📅 15:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96648">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQm2ksja9yh8liEaGAjxb1W0RfWYhniyhdyPkesGN-Rv8avDClk3g1UNAhiTGwC2K19eRevUfG2NCh7bkbH9fuMFMBSFeRjPMjEYhTDoNap02BFssG3cLU5z7K1O0GS6NkfK-gbDZkcr6PqjPEjh87UWbEBg5A4bylmn59OMZboi2HCB3LMTWXpBWT1YyltNRjDXsPZD91zAWF1R-KCB5_x6uBLJ_L0UeCvXx2nMJ7UrY536JY8TKirCjiemwTFZsMdKEL8RR5oScBCSR0WTPjb807RNDWMVhAREwVMogdgwMQV8ksFtRzwKhkQc8__v2vDv9d3p8mZ_mu_u0mxKiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
زلاتان ابراهیموویچ:
رونالدو بعد از بازی با ازبکستان گفت "من برگشتم"، اما کلمبیا تو بازی دیشب بهش گفت: "به دنیای واقعی خوش اومدی!"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/96648" target="_blank">📅 15:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96647">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d23322c7e.mp4?token=ATZ9DKztYBfdbjfrl_ZT1i9iK_RBaqNgUmb4LUqPzOM70VgpdseJFP905WzQP12QaE8D6uj47I2sL1rvFn770V7h3KtY7XxRqVpmiy2rTCr-VH4370BSydFDaex06cGp7WCE5BkUWz99dml3ILGakfJCirHfr06L2LZ_p9HoSYzSnx77-VYxB7ExJtzKkNv2wBEuC6orTbL_ebr1SEd9Cxg3G8fjwAvtz0PC2VJd5cXYLmGyAnb4HYhV6Us1Ro2oBbiiYtSnwNJ9FKX-zGre_E_j8cUFBIqqD6LYsiJ3RIAfkL7dC0N4V0UGd974G8jOgBC5R3o6fioJhnAHywiG1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d23322c7e.mp4?token=ATZ9DKztYBfdbjfrl_ZT1i9iK_RBaqNgUmb4LUqPzOM70VgpdseJFP905WzQP12QaE8D6uj47I2sL1rvFn770V7h3KtY7XxRqVpmiy2rTCr-VH4370BSydFDaex06cGp7WCE5BkUWz99dml3ILGakfJCirHfr06L2LZ_p9HoSYzSnx77-VYxB7ExJtzKkNv2wBEuC6orTbL_ebr1SEd9Cxg3G8fjwAvtz0PC2VJd5cXYLmGyAnb4HYhV6Us1Ro2oBbiiYtSnwNJ9FKX-zGre_E_j8cUFBIqqD6LYsiJ3RIAfkL7dC0N4V0UGd974G8jOgBC5R3o6fioJhnAHywiG1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇪🇬
🇮🇷
خلاصه‌دیگر از بازی ایران و مصر :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/96647" target="_blank">📅 15:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96646">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbgAXvV2Kc6BbywqXxn_ZUW1TGo7A5Qhs-Y6xSEyx7Jp7xX47jr5BtO4ml6GpcnFNqTfyXY7umGA3Y5QlWg7m_QDeJsdEL8Tys0-dx-gjmP6x8LHRGdYGbx7U_O8Cz02Oa49NJ3fUa_huxFOShwRoinBlIJMUxw8CHRhJ22PFGJd4U_ZM_Bp2qzk0-o1q0pqY2o7moL1EchqMRVwex9aVqb1pMWpd1Emabh15DWNg5miRRHiWTSv3bSpdM3ZMsLdwWCTIiRj_b8DjVDf12OClg8bJoz7tX_tgmMHaNGvK4UMo0EQN-3LS78AMv8GAQC6IGG04lz1Nxbe67zwDi-jsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنر چند هوادار ولزی : ما اومدیم اینجا و به همسرامون گفتیم ولز صعود کرده به جام جهانی
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/96646" target="_blank">📅 15:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96645">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dg4bOqmbqdzrpiX575JkTBGele2OrbBuuZi67aRofjXTjbtWlfe9mp8jYtsvgwoIwQcSMsdaSz0R1qEd9l7gzC64Cy-1bZq5qqDKxKkFk00WSSIOZenqpwFA0-aXT04sKCel1clbz_RB9Db-UrfyqOz4-Ac3Ym6wJs8bGcg9bWtRpbt_jcBCkZyBg_81-rveXFDMoxXdCK_wNoFPnIJB7BudDs8PObTYZI64zw0Y_8CWGiFQcjjXrAY89UfBTXloXHUNN0I0OodbuNgHgv0iqbuClxCKJFR7JgDIn1VY-vD-so6KlV-k1jBGyz9swl0aq-C7wKzfbcbGOmWoptdB2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇬
مصریا بیخیال کون شجاع نمیشن.
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/96645" target="_blank">📅 15:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96644">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‼️
🙂
علی‌نظر محمدی سرمربی شهرداری نوشهر رو مشاهده می‌کنید که درحال ماستمالی ریدمان تیمش تو لیگ‌یک هست. این برادر بزرگوار سابقه طولانی تو ریدن به تیم‌های شمالی کشور داره و داشته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/96644" target="_blank">📅 15:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96643">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc66af2245.mp4?token=Dbuo_aAwWyhLYpt3B9xIMFXYnZ98f2c7TVcT56Iii73O_tAV-i9sqfQp57M-5l-tTaO3v-7giZ-410EZWGO_1VNmhT1a6UZbdLmZcavK-lG63vxYK5-UXIKKtkOEUjbpK3oxlEkS1bwB2Lh903e-Z3sgSgT8YdzdREtFxizdjlJCLh4phnK94gXvmMhEa5dP64Ly5V-TLlDonl2_veqPGnXCnSnWn6pV0O24Gl5wBznHIzuXop3tTIi0PZWXiN16GeAibAtOHCPWOjCGcAjm_TLuC2etS5NSh64vALKjJXYjJ7WHqHTSZECOqOM0UgM77yedFW39Z0Xv2MtGILY4jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc66af2245.mp4?token=Dbuo_aAwWyhLYpt3B9xIMFXYnZ98f2c7TVcT56Iii73O_tAV-i9sqfQp57M-5l-tTaO3v-7giZ-410EZWGO_1VNmhT1a6UZbdLmZcavK-lG63vxYK5-UXIKKtkOEUjbpK3oxlEkS1bwB2Lh903e-Z3sgSgT8YdzdREtFxizdjlJCLh4phnK94gXvmMhEa5dP64Ly5V-TLlDonl2_veqPGnXCnSnWn6pV0O24Gl5wBznHIzuXop3tTIi0PZWXiN16GeAibAtOHCPWOjCGcAjm_TLuC2etS5NSh64vALKjJXYjJ7WHqHTSZECOqOM0UgM77yedFW39Z0Xv2MtGILY4jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😏
اسپید از شدت ریدمان دیشب رونالدو کلش کیری شد و وسط بازی از ورزشگاه رفت
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/96643" target="_blank">📅 15:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96642">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVZAgKRBMaSdqAoQtGNIyPyijScRZRB45-5Do0sO_RoT-a31_HVB6-LxP3GnhP9l6VK_1XDrTG3br5X5GRDqyXJJnfT4S3x-uPU-seoy0-KrOad0REp5ZRDCaZEQuyVb17VbOY5VKLz9c1B4e64KO5qVQz_1GeYeglD-G2SVuH9u6KLmdUUZRX0HQFcDVkaqmCYPvQXS_g2D-TmSq95hdduRbDTWamFxwaxJrTHHQoHgyTeq3paZvaGgYY-XV3IpFtsKzr5M73QoI_PDCpK7cjk2Rpj3uPofcGmlz3laRne0Yrrxw6rp-CLDVYvKu34GfGRSv42YGlJ5EZPNEQhUpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇺
🏐
🇮🇷
اعلام ترکیب والیبال ایران مقابل کوبا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/96642" target="_blank">📅 14:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96641">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fd01d9791.mp4?token=HIIW148jcOJXU-uE6wDHOfw3whQyFZXFUX4X4r7orfFL7T_d8nKd1kqZnIEJKMDnmLevszKHrPjKpGCcP0DdJg8KfoOSLStkBUQ10HYOBwpST_l0yT05o55-_vX1p4ostmOTEdWfJj9qqm6RJvPJiAOxta38EGiNmBVtPVL9iVpfAJQyrohTyoSrjQxaKpBfc_iUzeKTdtqsrcZv6AsrrffJxQKOOPIC9qrVbuivmR-ttT5Bp76-0Hs36xi7JzU4QaY3wmjSDMxJWnx84e_ziim4uAf4UCoU9V8V0rqzGuxt2FsottV0KtGAPReNWf8CPhgdbDQNKzsbPFCfwlZSiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fd01d9791.mp4?token=HIIW148jcOJXU-uE6wDHOfw3whQyFZXFUX4X4r7orfFL7T_d8nKd1kqZnIEJKMDnmLevszKHrPjKpGCcP0DdJg8KfoOSLStkBUQ10HYOBwpST_l0yT05o55-_vX1p4ostmOTEdWfJj9qqm6RJvPJiAOxta38EGiNmBVtPVL9iVpfAJQyrohTyoSrjQxaKpBfc_iUzeKTdtqsrcZv6AsrrffJxQKOOPIC9qrVbuivmR-ttT5Bp76-0Hs36xi7JzU4QaY3wmjSDMxJWnx84e_ziim4uAf4UCoU9V8V0rqzGuxt2FsottV0KtGAPReNWf8CPhgdbDQNKzsbPFCfwlZSiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
وضعیت ایرانی‌جماعت بعد ریدمان اردشیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/96641" target="_blank">📅 14:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96640">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzFOC5usqJss6dW5JXW9T8ZZpexorEo6pQB5jFUnPs57ghjVpeMfKbXuUa2_fdxW20IG5S_AKMQebLxTtTSmT5KJsdXb5J4FM8J5WFBWRnkNjz0q5cf1g84Fq1nv1oM943GusOwj6PqK2NL9p1EJXTzv4mW6SpFI5xhawi6e8-mxLnoR9waEso3TVXKXw_0WBF2dwQpuCMzZr7P4nvdfbGgfQJE2m0f9xe52JP5f6-OR23S_vP5tTOXfv-JSuR4AaAuttqy-8A5en8WwYVlgsVbeqXSa9GRGSbNiNJb_O7Fk-I1UhPmDpQkJCJZPAhxZs0VHZrsVFPmUVGe1CdStag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤯
فکتی پشم‌ریزون از هالند که نمی‌دونستید
👀
مهاجم تیم ملی نروژ و همسرش، ایزابل هاوگسنگ یوهانسن، در سال ۲۰۲۴ صاحب یک پسر شدند، اما تا امروز نه اسم فرزندشان را رسانه‌ای کرده‌اند و نه عکسی منتشر کرده‌اند که چهره‌اش مشخص باشد
🇳🇴
در دورانی که تقریبا همه لحظه‌های زندگی در شبکه‌های اجتماعی به اشتراک گذاشته می‌شود، هالند مسیر متفاوتی را انتخاب کرده؛ او زندگی خانوادگی‌اش را دور از حاشیه نگه داشته و از حریم خصوصی فرزندش محافظت می‌کند
❤️
👶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/96640" target="_blank">📅 14:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96639">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/96639" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/96639" target="_blank">📅 14:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96638">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=iRyaHBJmJWGSFzvcPOSzIjaxBvn-gPbj-jqXnGsGcsnN_c_6CNHUg2MYzrzxhxhGIZGi8mio8FP3fFLF_XWn8J4ntxVA3pZcYupI-20_i0tf_5xInFEkQUpUWS7aO5O77FtPE2HNJrfWonkQ3GnBUGlN_jPdyC-6GI15-i57VM6mLt_z37wW_PjHCAFGDux2GKn54gOdv5V-ttJhlpdGqLWdpLlHBvJmPn3Zc6415z_C9zDlHyFEvba8ib3na976-taX5n9tCjpz8838vra7DrDwHl-jqF3HnpJU4HX9ePnpTZ2h4hfYoHW-waXD8VMfHQ_axy-XO9l6EjiEen4Ktl_bf9JIkvZqmqNcy7BTT0ePWq_1f1IRZ5YcPX2xFhndpN5Zoc208b7FVERMH5k4wIK-6BiLZpdwr9dOBtv0HdRpaCvclZDd_GHrYMfOQxjGT65Tl2UOvhdj30Us6eAeceOdsxLakhfodY_jL_9b7bT7bRmwkq-IyJDtZDSdpY9Xw21W-WEYMJQlYdiSykSgg4F5JFHDWEKfGFML6iBQiRaawllF7v_5eCej0K629-jwwSZYdzHDWjUMai5PqHVcKBSSEm30B1HdR7TpQlXzY6cDktCsdJsLxHDaSnr1tF_VB5GfXN0ogC8aZ_e_sD-e2WGOnNznjSZCisGG-phFZ90" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=iRyaHBJmJWGSFzvcPOSzIjaxBvn-gPbj-jqXnGsGcsnN_c_6CNHUg2MYzrzxhxhGIZGi8mio8FP3fFLF_XWn8J4ntxVA3pZcYupI-20_i0tf_5xInFEkQUpUWS7aO5O77FtPE2HNJrfWonkQ3GnBUGlN_jPdyC-6GI15-i57VM6mLt_z37wW_PjHCAFGDux2GKn54gOdv5V-ttJhlpdGqLWdpLlHBvJmPn3Zc6415z_C9zDlHyFEvba8ib3na976-taX5n9tCjpz8838vra7DrDwHl-jqF3HnpJU4HX9ePnpTZ2h4hfYoHW-waXD8VMfHQ_axy-XO9l6EjiEen4Ktl_bf9JIkvZqmqNcy7BTT0ePWq_1f1IRZ5YcPX2xFhndpN5Zoc208b7FVERMH5k4wIK-6BiLZpdwr9dOBtv0HdRpaCvclZDd_GHrYMfOQxjGT65Tl2UOvhdj30Us6eAeceOdsxLakhfodY_jL_9b7bT7bRmwkq-IyJDtZDSdpY9Xw21W-WEYMJQlYdiSykSgg4F5JFHDWEKfGFML6iBQiRaawllF7v_5eCej0K629-jwwSZYdzHDWjUMai5PqHVcKBSSEm30B1HdR7TpQlXzY6cDktCsdJsLxHDaSnr1tF_VB5GfXN0ogC8aZ_e_sD-e2WGOnNznjSZCisGG-phFZ90" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/96638" target="_blank">📅 14:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96637">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dee3960474.mp4?token=g-1tPIywVuw9BnF7tGqU9RW5gl1xbAMtL_pwLhX_FfGr6q82-60aD2xRB6Rv5Gs88v6WT3tw9c7wfw0eTdqHAZgcpoDmVHKOVJDwkQGvU8Nh-Fpp5NM-PUkHCwqUPn40IQVbZsWeXSCsU0ouPySprI4K9TKo6Jyc4dFeuLKMZEFGmjmo6k0EovHsZ8KpyfRT7HKvxb8Fep-xYNh39NcH4sMU6WOwLy-UY6Q3nU0aLuyb22wNIK13NwwACJDiyyPnGyys99bz9wFVguRrwOPdP7amt2f9AiUPVF4UaHGfzw9KQOWMOYAFGLZA5riQXXP5q2rEkXIWqrDOGZ-88HprPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dee3960474.mp4?token=g-1tPIywVuw9BnF7tGqU9RW5gl1xbAMtL_pwLhX_FfGr6q82-60aD2xRB6Rv5Gs88v6WT3tw9c7wfw0eTdqHAZgcpoDmVHKOVJDwkQGvU8Nh-Fpp5NM-PUkHCwqUPn40IQVbZsWeXSCsU0ouPySprI4K9TKo6Jyc4dFeuLKMZEFGmjmo6k0EovHsZ8KpyfRT7HKvxb8Fep-xYNh39NcH4sMU6WOwLy-UY6Q3nU0aLuyb22wNIK13NwwACJDiyyPnGyys99bz9wFVguRrwOPdP7amt2f9AiUPVF4UaHGfzw9KQOWMOYAFGLZA5riQXXP5q2rEkXIWqrDOGZ-88HprPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استعدادی که فیروز کریمی تو بازیگر شدن داره رو هیچوقت تو فوتبال نشون نداد
😁
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/96637" target="_blank">📅 14:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96633">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FhGFN7x3RiZsIo9GUYOzc4dDF5eWIcAfal1MaS34AIhm6VebtMmd7QUzJmm-snjpN6kC2HjlNncRCadvPCdlWNPU6xdO_G0Xo0I53xqPYpeBlOZSVLLVEWrLA9CnXphRV9krqyxedzMYoApWEzE18wuN5QgmdYSZiFVqloa8iyES-UAK8LqfzTJjlYATZaHOhrDI32MGBVKkBq4wiStxyDgyaM859f6TP0HQc7ssuDynJjcjYA_YsnJBV7a_3rN-joGrh6GwyLH4sCrcmM-mwHSlht9doAgRWLCENriHTurvbF3geQdogrNYCAiWMWO_SydVHC-ac8KYAgZB08oI5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UL3zV9QE4KNG_tw-XnV-Z5ERfkeURLXmHNpqcE3tsWADnAC_dviMlA83MC-ZAUdlzH8iaqBhgZWZukE4ZJLlD9ROFrOuj_wMYlRuRqnGgCoLs9vNGUbZ6CJcSpVlA8WbbXuTDl4uTMJ35SfngLe0pXUTcBrKm-LgFHHE4skO1AyPnIAc-yKtLMoF5lH5YqaLZF3VMuEQCe3_kgKFXM91w-EeHMUb8b3Nz8w3fPk4uXqiKjUIYj3z6oA0Mu2kaI3AtKcvRXUOoV1iGPv5dusp_Eyh2riVlN-5JQedosdzBfavSx27kB8C5tdW3c77p4_Wv3qQXhfmXoCe2CvNYxiZnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ruS0srm9o8yB_PniWhMBm0gRNUvhpwE47GXObZncUbUmSmPzE5gBEP5Gn1LiiX1FLGPlq7UcUDVYcL6L2RhE4Ho4jl5DG2Ra-1U3v3xMkZkk42wuqfz91PhA-E0NBFW_Kk74168TAZ3OACgzuQ0bJG0GTtM9js8KzHFooI4Rg2GFp0n4bxohqJg29xOxMxY9fBX8TQQvJCFGTAGKxTz2xjKYYBSfYFCRIWVvU849e_43s4qyTE8zKbXDDiElhCxr5-FJ9g8_gCkcKnX7kwHSkW8kv7TQ2_sOxNHg5kZn1gl6erAYYQ1naaTdt725OI7y9yjVeGIyb9VplBW0OpKYsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NybKXU4kg-8rep4TgR4MD-u0ASz4GzaWJ26juyl_kWoSUqEzANPpetTC9yely0SDfliSVal3-r5SmGOP3bk_PLOcOUk5F1k1DW-OLTUeFydwUIGOgs7CEiy2VGnEPYbTtfyON3VGIzbXQiNl0fyiLw9slhFaQIXyyLe-4RVbz1QGSBx4oEKMjkfmfMsfw6QOrm27ySuQ8RzeZfREMb9OuX6KKUdqtcXWzwk1KP05gPwkPru2SnjC8sOtrrCn_JitWEeD0wWRdXRmae2GLzim7XYa3vO3MPqJBASBW4v20O_ElCTQAi4s7FdDvIbuOZhcP2epNv1kmJkT_9FL2GsjfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پس بگو چرا کلمبیا صعود کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/96633" target="_blank">📅 14:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96632">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6330122b85.mp4?token=U78NYvdWSBJnvXV8YcADaj9Oz3x9VfGqrZS_Sjm3qBH7a5Gwx6AL0tbP-WvWqilkOo3r8VcwcwrEOGqGS8gaiopQxkOz3BExbQBX73KMr_oU-yJ5pbpHLZhFTkJ_iswmGUEEsJxCm7SKFiJGTTOHp5Wrar93uWNgWhlyno6cAlgHL6ZtQ7NDGzzrTGqnqXJWAUjnDRndM9jrl5Toaht1bzUArE1jTnLGjREbeaWr4SCPw1mMWeApF-hqmxXhWWK5PpmeooldAvGZkXOiICFZZ_ACXI6ansK9lhHkkElQlduob-WLFUMxvE-T3VIk6Yyg9knCdRDz3MDg7mbtSoduMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6330122b85.mp4?token=U78NYvdWSBJnvXV8YcADaj9Oz3x9VfGqrZS_Sjm3qBH7a5Gwx6AL0tbP-WvWqilkOo3r8VcwcwrEOGqGS8gaiopQxkOz3BExbQBX73KMr_oU-yJ5pbpHLZhFTkJ_iswmGUEEsJxCm7SKFiJGTTOHp5Wrar93uWNgWhlyno6cAlgHL6ZtQ7NDGzzrTGqnqXJWAUjnDRndM9jrl5Toaht1bzUArE1jTnLGjREbeaWr4SCPw1mMWeApF-hqmxXhWWK5PpmeooldAvGZkXOiICFZZ_ACXI6ansK9lhHkkElQlduob-WLFUMxvE-T3VIk6Yyg9knCdRDz3MDg7mbtSoduMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
‼️
وقتی کله‌سحر تو ایران فوتبال میبینی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/96632" target="_blank">📅 14:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96631">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54816ed9d.mp4?token=WyQv9XgMpZQCd71SJyPmN-Ptk-giqNZJTl3-6QPkhRBALJYYytjSEpjyUi1TH5nqccN4thoLe9L74qLK56ep3HCcgdyRKdWOUAqw3DxirhtmkmkjBf14XPFmMchtlzz8o5l9sDFHU0jzEieHuDOg4lh_mo9XNpGpdZowDmmPSNdxRNbrWCm9Ctw7hDttaEQSvsPSiTSlrT0DD4rpf3XZXEB2IQ2tvlNSMJH2yff3jt884FRlmjIcF9rV-lWgpoWdYPxaXIS9ESERBHMFcDTDcwn-bTfoijhO15VT7nr8-1A3GrjvmZ8bieuNCQTxGdbyZrbqeNGee2bFalqgSZ_XIIqC9O8QuElyT6IEKlasZf267n_sDJeKHnmxHlLvsk0p3Pdj35FCjUYfDZ9lbH5qYxwSw1lCDsbS_b4MW-X1HF-xwdNLZLdFNJX4LyTb2n5SmW6jx0uXgnWzQh-81Z-NzE0tnHjeFrUY3RMMp5i7kXVNKd6PZrmbe95gGYkShpByHoCRBA2TiKJBqECblVMRtTfx1MLdrI36FxML6a1y8Lhf3xlEYi4mFVtWP_xzhQSneTF6AS_GgGD0ruN8LTLubhABNTPBFdV3tQ7cfUARsr_BvZ-iqhIEacqE7TWzjjlLzAB3_ihp9JjrphMc0AWmcUCupEn_RNm8tHSN63Z1KWs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54816ed9d.mp4?token=WyQv9XgMpZQCd71SJyPmN-Ptk-giqNZJTl3-6QPkhRBALJYYytjSEpjyUi1TH5nqccN4thoLe9L74qLK56ep3HCcgdyRKdWOUAqw3DxirhtmkmkjBf14XPFmMchtlzz8o5l9sDFHU0jzEieHuDOg4lh_mo9XNpGpdZowDmmPSNdxRNbrWCm9Ctw7hDttaEQSvsPSiTSlrT0DD4rpf3XZXEB2IQ2tvlNSMJH2yff3jt884FRlmjIcF9rV-lWgpoWdYPxaXIS9ESERBHMFcDTDcwn-bTfoijhO15VT7nr8-1A3GrjvmZ8bieuNCQTxGdbyZrbqeNGee2bFalqgSZ_XIIqC9O8QuElyT6IEKlasZf267n_sDJeKHnmxHlLvsk0p3Pdj35FCjUYfDZ9lbH5qYxwSw1lCDsbS_b4MW-X1HF-xwdNLZLdFNJX4LyTb2n5SmW6jx0uXgnWzQh-81Z-NzE0tnHjeFrUY3RMMp5i7kXVNKd6PZrmbe95gGYkShpByHoCRBA2TiKJBqECblVMRtTfx1MLdrI36FxML6a1y8Lhf3xlEYi4mFVtWP_xzhQSneTF6AS_GgGD0ruN8LTLubhABNTPBFdV3tQ7cfUARsr_BvZ-iqhIEacqE7TWzjjlLzAB3_ihp9JjrphMc0AWmcUCupEn_RNm8tHSN63Z1KWs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
کنایه‌شدید مجتبی پوربخش مجری ورزشی اسبق صداوسیما به افزایش قیمت‌نان...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/96631" target="_blank">📅 13:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96630">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GOd9KRGmY96oYWOpgx-F8DfTo_ouHr1EHlwnKSsfTwPYzdYiw9-zPrdH7iz2YICXk6dmehl1wW-MqpdoT_H2OnVAz5VM7uw1VSHUqCAkMKK7mSD5A-8G-1gaHTqyZDLvDVSHOPijKnSs3ROz1zfPAu8ZmCJtaijXzXKjfffcKJJanGcf9HRDZ0xWIO5Srb_IKdvk6wOnrCVWRq4mIaueJtzhx7SnLLSKziJ7HGg8MfmbMiqOfCrIzOhqhkhVRxlV3i7MMwuorqSbh2pPD0Qk-G6xheiZDZ4URW8yh6uF6jsUFb0FKyQ6LFVyPrsIjzpS4ZUKQnREx5WySA7XgfxQ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
بیشترین گل‌های ثبت شده از ضربات آزاد مستقیم در تاریخ:
۷۸ گل —
🇧🇷
مارسِلینیو کاریوکا
۷۴ گل —
🇧🇷
روبرتو دینامیت
۷۲ گل —
🇦🇷
لیونل مسی
🆕
۷۲ گل —
🇧🇷
جونینیو بیرنامبوکانو
۶۸ گل —
🇧🇷
مارکوس آسونسائو
۶۷ گل —
🇷🇸
سینیشا میهایلوویچ
۶۴ گل —
🇵🇹
کریستیانو رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/96630" target="_blank">📅 13:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96629">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f50e7c88e9.mp4?token=OgWmP5jaM3V1NhuZcaVgMcFD71p-pWc5POq35dSlUELkNz5qEpW06xBp1-AWGXdfUKM_l4qYf5bl0wBqCHHreTjm_QuhngAUxWCkPhKisDOIvAyle7b9V_bfu1L_Yzb-y81YrEDjNdGSJdfyiU8cpPgEy9rzT5EMUBx72bRUKk0x8lUvPH1FDAsCJ9_jbihhlplvPDmjOVQSY7X4wkzi_O_LRCwEqHVr0gY5P0aBGt8uX1s1Uo9D7QNhXKtryZIweFyqoM5Z8f3fjFCXxgrNyuy_NVxsfnI38AcpOPacTC9g4-caDq9cFrhZ6IXhoB5VskjXZopdGHWfQvnjhGJwbIvGls5fMMW_FuZfrTLG79IVS1SYeTzQNHMhzoVCf_E3lZk2PnhpvpvjaTIyxIxSTDHIMTYL-plwJlBphLMwNJCyb9fIgcFdKxhBxH3Tp3PW2aqbT4sLgt7PPCPzKGWS8OKoQeMASAIL-t827mFF65HryvRJiQ-lpE-7JbAhevzJIrFGAYfQMdmQLMoW5Oa6TyE3veMq53od_AsI-KNlk-Eb0-iOQ398XEreo8G9hssdAYCtWOKD-4hC2MoY8G_F5_Ia81ZEtmAsWErobr07YJfAwhEgLNlCDHl3-fihUwFbYVg0IercbjyS_32dUy4-FZ2v7iWX-D0pKjHt-nIQ0lM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f50e7c88e9.mp4?token=OgWmP5jaM3V1NhuZcaVgMcFD71p-pWc5POq35dSlUELkNz5qEpW06xBp1-AWGXdfUKM_l4qYf5bl0wBqCHHreTjm_QuhngAUxWCkPhKisDOIvAyle7b9V_bfu1L_Yzb-y81YrEDjNdGSJdfyiU8cpPgEy9rzT5EMUBx72bRUKk0x8lUvPH1FDAsCJ9_jbihhlplvPDmjOVQSY7X4wkzi_O_LRCwEqHVr0gY5P0aBGt8uX1s1Uo9D7QNhXKtryZIweFyqoM5Z8f3fjFCXxgrNyuy_NVxsfnI38AcpOPacTC9g4-caDq9cFrhZ6IXhoB5VskjXZopdGHWfQvnjhGJwbIvGls5fMMW_FuZfrTLG79IVS1SYeTzQNHMhzoVCf_E3lZk2PnhpvpvjaTIyxIxSTDHIMTYL-plwJlBphLMwNJCyb9fIgcFdKxhBxH3Tp3PW2aqbT4sLgt7PPCPzKGWS8OKoQeMASAIL-t827mFF65HryvRJiQ-lpE-7JbAhevzJIrFGAYfQMdmQLMoW5Oa6TyE3veMq53od_AsI-KNlk-Eb0-iOQ398XEreo8G9hssdAYCtWOKD-4hC2MoY8G_F5_Ia81ZEtmAsWErobr07YJfAwhEgLNlCDHl3-fihUwFbYVg0IercbjyS_32dUy4-FZ2v7iWX-D0pKjHt-nIQ0lM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
افشین قطبی: کارما در زندگی‌وجود دارد
یک دایره ای در زندگی است و هر اتفاقاتی که رخ می دهد بخاطر تصمیم های قبلی در زندگی خودمان است و سرنوشتمان به دست خودمان است. گاهی فردا بیشتر به خودمان فکر می کنیم شاید پنالتی طارمی میتوانست باعث جشن صعود شود و حیف که این بازی را نبردیم.⁩⁩
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/96629" target="_blank">📅 13:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96628">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad26229b05.mp4?token=UaCg0u4sbCtzihLN2HaXxuTVJubL-X9a2unwwlS_YbLAF-XqpGaH25NQx8nBYqrQsH77P2GJYWyq4Ah-rlHtYedNt4i3G9HjUAezrkJACoBEfT4jkyWUDSf7mBFeqddZalBzVg5jdA8JF7x8SPEIKPxTX8RqvRG6FANLayHcYVsr73pXzJyugzeNkOL8uai5loPiYGzOmg8J62ZxISwAk1YR5WmzqkbO-3AenY3dED4W79brncjTTokMiG-NO3xvbdhnpJG8UMJbow48PDYrxu6qtJd2aIrpONI7fcU9cwPejRx3SvR59zNDdge4UQeAsl0PAkZPfNIg5npfsKFJ_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad26229b05.mp4?token=UaCg0u4sbCtzihLN2HaXxuTVJubL-X9a2unwwlS_YbLAF-XqpGaH25NQx8nBYqrQsH77P2GJYWyq4Ah-rlHtYedNt4i3G9HjUAezrkJACoBEfT4jkyWUDSf7mBFeqddZalBzVg5jdA8JF7x8SPEIKPxTX8RqvRG6FANLayHcYVsr73pXzJyugzeNkOL8uai5loPiYGzOmg8J62ZxISwAk1YR5WmzqkbO-3AenY3dED4W79brncjTTokMiG-NO3xvbdhnpJG8UMJbow48PDYrxu6qtJd2aIrpONI7fcU9cwPejRx3SvR59zNDdge4UQeAsl0PAkZPfNIg5npfsKFJ_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
🇪🇬
مصری‌های جذاب بعد از تساوی با ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/Futball180TV/96628" target="_blank">📅 13:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96627">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/456a3c4775.mp4?token=R2vb9FDSmv3r8QWTdnDcPEt5RtBz_ehjHNaiKuwqBGEcLN3z3Vj0HPnh7PPljGkOotYOftMZJc0pssv8KHKkibGoJoa8yeiVTf_CqViPz43tNcEPfncGzpMMnIBVGgYLaS4kbBitt6xSqmOp8mmV6GbNhkrm3m7lguQ7Q0NgiVH69kMgFbTiMDrF2FXW5_hyptBEH7PBUHGCfSOakon_tB-l9zIoqUyDp8Rc4LMhcpil7T-oemtX1z-mHD_MoL8LpSxeAA9fOlMr352Rz4WwKFj7kLHf-h4PD6cgyNqOL6AaFDK2rxMnI1kI0xhol9n4v15PapQdMkGhMnkRl3lFKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/456a3c4775.mp4?token=R2vb9FDSmv3r8QWTdnDcPEt5RtBz_ehjHNaiKuwqBGEcLN3z3Vj0HPnh7PPljGkOotYOftMZJc0pssv8KHKkibGoJoa8yeiVTf_CqViPz43tNcEPfncGzpMMnIBVGgYLaS4kbBitt6xSqmOp8mmV6GbNhkrm3m7lguQ7Q0NgiVH69kMgFbTiMDrF2FXW5_hyptBEH7PBUHGCfSOakon_tB-l9zIoqUyDp8Rc4LMhcpil7T-oemtX1z-mHD_MoL8LpSxeAA9fOlMr352Rz4WwKFj7kLHf-h4PD6cgyNqOL6AaFDK2rxMnI1kI0xhol9n4v15PapQdMkGhMnkRl3lFKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🤩
حمله شدید وحید قلیچ به بازیکنان پرسپولیس بعد از تساوی شکست مقابل چادرملو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/Futball180TV/96627" target="_blank">📅 12:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96626">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjZClGGyJjKI4BihB3xB7jH1p-DcK0e3BPgB6bL3N_vs9ycufbinTUa94VMOlrLHgimhzTao9EJ0CxeizvejQrG4m2jelsywjLWLa0CK1z8fTjKBjJVgkPibJRbVFlC_ZRQ2XlMfBHVpvxM9EbS3dDRe7kpUTy69ZhsBA1vuGOMxWThwisZrAXdPoq65AIavEa3tpDmI1QcMk212hIQnSPzEPl6y4R5xFJyjAZTmyRTiGd34ivera_lgzt3B3UoT7JgzatwIkCGeGHYbpUHv9UT15Z21Kp4BX1ocWrOhbw3VJhc46jXjbW9Gw4X6Xr6HAtA8FHnOi4FaiN8iQxRDqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ابرکامپیوتر اوپتا:
فرانسه قهرمان جام جهانی میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/Futball180TV/96626" target="_blank">📅 12:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96625">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_UkLrU84_wHx3r4wj9rrMJzHas9WPepkM1YenOwtQklu50wwpbEsDvtKk_2KWM1EfQhYeEd_Z8uMa5DcEnpYaRzjPQs8bK5HFIDBQEPYHMQ5aCKaQPXI6LsTIAN51aBl-tUiv-eFlAtCXLTdp8NZ2C_1yF31JI02K3I4MyPeSH60185hZVsZ6n-8Ul0d8TzfwiEt56_85phWFaNi5wV6xJEZuAXjTFFcGQbUJ7bRIyLF4CKiF0u932YHSk_UMGZkI2Likl9c7rRXPsAahZ6bgHjO6Rn-LT5a5Q5sS7JA_iz_nV4D8ytbg5aKdYTcf2CzMQo0SBDjsNk0yg2XPjP7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🇦🇷
🇦🇷
مسی در مسابقات جام جهانی:
‏تا سن ۳۴ سالگی:
‏
۱۹ بازی
🏟️
‏۶ گل
⚽️
‏بعد از سن ۳۵ سالگی:
‏
۱۰ بازی
🏟️
‏۱۳ گل
⚽️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/Futball180TV/96625" target="_blank">📅 12:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96624">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b6ecbf93e.mp4?token=bCnrF2sWpKBBttCOdnrgnFV0FbcAsjdy5BjqBC25H8BHQvk0VkFjKfjOaEBaqCVnVa-1n9c8eWeHMvPivhO6TsD7E9Wfhw9HVvP1Jd28J4_wNDsUxJ9oPMZstY8VIRYz17B9Enb_AA69oBde9Qsxzg42mEAnBWhRvnp9KtgWPn5e_u1viV7p7ZzaueDyMBfhi79xc1KfF3d3t6ilRzBb8AShv_6eo4LE63rM5xiK8TRjRUO5VLIeL4yJjrw2XIksW3RvUZ2_fRaauCIGYpU7HsHCNheo5SI7O0ZvWu5vO-zRYjOVNJbtrnAL4lyevbyEZRu48r3ZNWn4qEdYRXpiSqeO28OhorLblurc2QN4_iMVQbNhKwj0XwQWVQNFy7oGPAKqhTB3cEMbR27Z34pOcD_PqmF38_hAdeOxPHnx7775_JOpamTftq-lMBtMeYtxc2PqwFNCdQmI8dxAR1jpHayZj185EGXu8NCs45FyiYscL9saW2ol3vJEp4KB_mbnWQg7LqRJmTpXuRSks5Iz6W43CEZF4zmLicyCBGUtK2YSNRlJ2pjmYqPlNZulXzh6ovdv8RfssUcJ4PkkpjoVCUk72_Dv6MsOmn13NVVGwV77JnGvCPe9563l9e6hS_9CIkFa0R7xjh7z0nCl4o0HVSUnjGXRHMxf0FuAbmuzKPE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b6ecbf93e.mp4?token=bCnrF2sWpKBBttCOdnrgnFV0FbcAsjdy5BjqBC25H8BHQvk0VkFjKfjOaEBaqCVnVa-1n9c8eWeHMvPivhO6TsD7E9Wfhw9HVvP1Jd28J4_wNDsUxJ9oPMZstY8VIRYz17B9Enb_AA69oBde9Qsxzg42mEAnBWhRvnp9KtgWPn5e_u1viV7p7ZzaueDyMBfhi79xc1KfF3d3t6ilRzBb8AShv_6eo4LE63rM5xiK8TRjRUO5VLIeL4yJjrw2XIksW3RvUZ2_fRaauCIGYpU7HsHCNheo5SI7O0ZvWu5vO-zRYjOVNJbtrnAL4lyevbyEZRu48r3ZNWn4qEdYRXpiSqeO28OhorLblurc2QN4_iMVQbNhKwj0XwQWVQNFy7oGPAKqhTB3cEMbR27Z34pOcD_PqmF38_hAdeOxPHnx7775_JOpamTftq-lMBtMeYtxc2PqwFNCdQmI8dxAR1jpHayZj185EGXu8NCs45FyiYscL9saW2ol3vJEp4KB_mbnWQg7LqRJmTpXuRSks5Iz6W43CEZF4zmLicyCBGUtK2YSNRlJ2pjmYqPlNZulXzh6ovdv8RfssUcJ4PkkpjoVCUk72_Dv6MsOmn13NVVGwV77JnGvCPe9563l9e6hS_9CIkFa0R7xjh7z0nCl4o0HVSUnjGXRHMxf0FuAbmuzKPE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😁
جلو جلو ذوق‌کنی کیرررر میشی(قسمت ۲)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/Futball180TV/96624" target="_blank">📅 12:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96623">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/773c01efc8.mp4?token=bLgiy9eXngfW9gkqV_l0AEhu3QPh2wFgKxBArYygAXNOaUj239lbbI-3O-9YwPhmuRFhnXnQ1VsBPo9LGTfHAdzyciVW5TMMazixsFWBoqBTXyQahxkZuCxVtglXsOF1Wd76jcQOir3R7YL7eJwj0ekZWFU8y0C9rgoEtWticx0zfnMEOAtqf0JcyP_omTve40yJ78P5F4lptTsLnAFrVqlqGWnqEBylojoJY-Ydp7jMP3OTy557dlouAqDEMTgJJ2jOwNXwqevaIRsm7intetYA4r5JSq42ygxTmqGoNHEClu7pa1JuM3X-FKLdouxjrwrMsUUvpY3G9u4iHHj8Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/773c01efc8.mp4?token=bLgiy9eXngfW9gkqV_l0AEhu3QPh2wFgKxBArYygAXNOaUj239lbbI-3O-9YwPhmuRFhnXnQ1VsBPo9LGTfHAdzyciVW5TMMazixsFWBoqBTXyQahxkZuCxVtglXsOF1Wd76jcQOir3R7YL7eJwj0ekZWFU8y0C9rgoEtWticx0zfnMEOAtqf0JcyP_omTve40yJ78P5F4lptTsLnAFrVqlqGWnqEBylojoJY-Ydp7jMP3OTy557dlouAqDEMTgJJ2jOwNXwqevaIRsm7intetYA4r5JSq42ygxTmqGoNHEClu7pa1JuM3X-FKLdouxjrwrMsUUvpY3G9u4iHHj8Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
👀
ایران رکورددار گل مردود در جام جهانی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/Futball180TV/96623" target="_blank">📅 12:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96622">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QXFmaTBs487OPgx22lLZp6XQydiNW7CKHiTh56qf7SWLp8oJPTkoAlHRgw2OMxuvdGXkpJAkahOfNk0I3OULeNqSrt6B_fA4BjFJVIndBgepZZjgXihj5FPMGoR0cLL2wBJI7SOCeSSoXv4omZzP-swI-uyAlAB5iNOrH8bHJmy49k45FqDX2E7h06awgF_FO1XyA8TYHdz6bprXFgp9S7Uby33liXh5b1yGMQDNxSXpny30pXqmIo55GFo1FcrNrTxja9ydOhqgHcONpesyZ72WRZopYp65uzowelrxgTDFk3P2FjfLckdkik1V58NsG3EnNw2bbLZpjoHZLPjSkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تیری هانری:
قبلاً گفتم، مسی رکوردها را دنبال نمی کند، رکوردها او را تعقیب می کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/96622" target="_blank">📅 11:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96621">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fp-ge_-doH8lPtlkWpagMe20xKlVuD6sHM5ZNqSCG_T4pEj5ML0B98kFa_nUb60SuaBsGkVPLWpAE9gXORU39N9pVCNjxxr4-YTaonRJR0VI2sGaUM8S15e2HVYdWiG3noK4aYQ4NXFv2cuqH5tgghN1j9D5NieD1tmmLIjyqcnbUaLbiKMo4-VU__7B3ei4QcKcGhNdjw-8R9I970nUyfYJOrV2-bBG9unQ3BmtvhZ6Pz14asR9yWaz6Yju5c7ey2qM5c7vvrwyFe7fIdNVWvdpBEqt2Ti0WC97-542Uj5Vju8yb0MCBARyElE29qj_fY39KuCbIELYU8QSTQ3mYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
مسیر تیم ملی پرتغال در جام جهانی ۲۰۲۶.
• مرحله یک‌شانزدهم: کرواسی
🇭🇷
.
• مرحله ⅛: اسپانیا
🇪🇸
یا اتریش
🇦🇹
.
• یک‌چهارم نهایی: بلژیک
🇧🇪
یا آمریکا
🇺🇸
یا سنگال
🇸🇳
.
• نیمه نهایی: فرانسه
🇫🇷
یا آلمان
🇩🇪
یا هلند
🇳🇱
یا مراکش
🇲🇦
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/Futball180TV/96621" target="_blank">📅 11:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96620">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVNp_yY--9XzuuW9TzRnPJUhaEzIebEKJha7yc338TUPFz93lzjAUxbdrX97gCrOrrIVVU_4wBT661JUe-ME1uoGltX0hvuD7sUbFDd873BXhsYR5EkFGC7qiYAfJD5VI92L6fda2CWVwJGU0e-T1VSyZqp1v42aJ43NuWALRyLQbHSDqJraFeBoPZ4sgiI934ARvQ9CtB5CcbPS_uWi37k9wT_oD7QMiDeyY7cRDp80Sh3cRNNPvHK41ZJvjexu8ZS_VAP4Q5vkRnT7jTCrjayNIORAvdAZ5TTkVWpolehNFQocsuIqlxFIFyckLS0SsRR0Y2ap7oR4kitb-WLOtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
🇺🇸
ترامپ: مسی دیدنی است. او تنها بازیکنی است که می‌توانی بگویی بهتر از پله است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/Futball180TV/96620" target="_blank">📅 11:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96619">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/957600e824.mp4?token=ehEtpiZga7lrmrePOYsguNuBfOYMJkuGZcqJhqFAQTauis6cv_e8TINWyDyXosfyzTmjUh4h7gxnYC2Sdwfn4n11__yckNPoAYbIVWOJ1yexpaP01M1TCHA-Q-gjoqGgFTvoZRz7uhc8OSxozh1yxuS7PN5F5pDaUKCM2UtfL8Jev6MzRxLNiyB6ZF-UAmwxoAWHcBr-UMjd1G2Ix1sC522tar0bypELEuFbpXo08xGpLhOkcWKGNWitutxb7dW5ed5GSJfxVbyytjrdc1-1AY9z3Z12KOnSy_cYR1188_2TNt-qmqAhOQQYa4Ao-MmNXuk_PV_bIMvPeGh2U_Z6hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/957600e824.mp4?token=ehEtpiZga7lrmrePOYsguNuBfOYMJkuGZcqJhqFAQTauis6cv_e8TINWyDyXosfyzTmjUh4h7gxnYC2Sdwfn4n11__yckNPoAYbIVWOJ1yexpaP01M1TCHA-Q-gjoqGgFTvoZRz7uhc8OSxozh1yxuS7PN5F5pDaUKCM2UtfL8Jev6MzRxLNiyB6ZF-UAmwxoAWHcBr-UMjd1G2Ix1sC522tar0bypELEuFbpXo08xGpLhOkcWKGNWitutxb7dW5ed5GSJfxVbyytjrdc1-1AY9z3Z12KOnSy_cYR1188_2TNt-qmqAhOQQYa4Ao-MmNXuk_PV_bIMvPeGh2U_Z6hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
مصاحبه چندماه پیش استاد مهدی‌طارمی :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/Futball180TV/96619" target="_blank">📅 11:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96618">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f29e12c0b7.mp4?token=HDQxFJaaY24Z5I43vNUiIbNLgCyGD7qtAZPqzakgGqmuF3I6qfe7V15xziQDVdXuxjRr8NcCINo4n71We9AezKqgMGc5R0Vy2eILWfyLxcY03jzFyGCnialUASqiUxSZQMXrZRpryNwdlBAtoXeGI08feBdETo_UufqjhozK5d2VOe4gVMDnSFjV8p9o4NMgSrrqSNC44zvnEKZJkShR2lYh0U-fNjmebpyqOaBOqhjp5N2ntFo932KgK9UF-g5UlSY5wm1urxqIoamwKYr7EpqbOSqkOtt8u2XMdKSlkKydgYkfohJmBcM8QqlwEzE8GVPshNa9rD6y77JP2PdA2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f29e12c0b7.mp4?token=HDQxFJaaY24Z5I43vNUiIbNLgCyGD7qtAZPqzakgGqmuF3I6qfe7V15xziQDVdXuxjRr8NcCINo4n71We9AezKqgMGc5R0Vy2eILWfyLxcY03jzFyGCnialUASqiUxSZQMXrZRpryNwdlBAtoXeGI08feBdETo_UufqjhozK5d2VOe4gVMDnSFjV8p9o4NMgSrrqSNC44zvnEKZJkShR2lYh0U-fNjmebpyqOaBOqhjp5N2ntFo932KgK9UF-g5UlSY5wm1urxqIoamwKYr7EpqbOSqkOtt8u2XMdKSlkKydgYkfohJmBcM8QqlwEzE8GVPshNa9rD6y77JP2PdA2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
تصاویر جنجالی در حاشیه بازی ایران و مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/Futball180TV/96618" target="_blank">📅 11:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96617">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
‼️
درگیری شدید هواداران ایرانی بعد بازی دیروز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/Futball180TV/96617" target="_blank">📅 11:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96616">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🥲
🥲
شادی‌ عجیب اعضای تیم‌منتخب ایران در هتل تیخوانا پس از گل سوم الجزایر به اتریش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/Futball180TV/96616" target="_blank">📅 10:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96615">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/paofHeoMGw_aMoexasD7aBDAyR_dGgab59MIkeEE5iiJOxwM8VB9EjVZ3LaJCBPrQHcglxCvdEbajPr29ClrAy54UBLBhT6cKrrVP3dN9UrL3SN5n3PbVqIQX0T7KlA2MpSV1l5HxZ9Zab--pv5uSoGLsLlfzQrOIv66OjuySDjfRnIQMDmWzvKJ4U2ysOx6TlDXNjSQg3YEXi_RYA6BfiBMac7bpb1DQ5sLoFkJ9U3OqDGg0p5gLZW3d45NbGb-13lm6x6exAcuol8LXvQ3aumTELgbZ2KOhxUWdNQkvHZPgNRJvqYGEVe2uksibOQ1y5LeKoyUtmf2fhRggGvp7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇦🇷
اسکالونی سرمربی آرژانتین
:
🗣️
لیونل‌مسی امروز با من صحبت کرد و گفت میخواد نیمکت‌بشینه تا فرصت بازی به سایر نفرات برسه. این نشون دهنده شخصیت بزرگ این بازیکنه درحالی که میتونست به رکوردشکنی خودش ادامه بده اما تیم رو به خودش ترجیح داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/Futball180TV/96615" target="_blank">📅 10:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96614">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47a4bb6889.mp4?token=fBdmhWB3bHSkp6W80parhojLiHeD3ISidu9UKLm2dKhwz-YlmTa0j7deEbpER2XXr41CCl3PcS_oCZ-d6_k0KcaFCBPVpUYegKK96X25ObJNP2mAYHSEO4rWzrFYFgh6anvTxDMgIvRMs9tZetUSH0D_jrFOxpaI4ORQP8O0DfZL6vnwxV1UO1og4I9G9q10iTOgTAhGDZH3psY_yFL7mpd-g3OxPn-0yprBjUAXZXzRc9Vp0BT-kdOo-O0aZ8OpGbKsklrQb9swBixGfYh8LoX_Dtpub4IYQKfApH3SEHC7NOrqK081vGd0-Jo2gOcBhcS0mgD7LXp344VFwzja9nDu7jSrbJCIr7TBvs0rp2YeK--cNNkdLKRWbuUR8AIO-1s-6ZU2F4RC0UTRCEY04UVMe-zUAGnidfB9E35GqLJ6Gdesquw84SfxK8cWsukIxyHprAtJTJ5mSO2N1hMEgZwxbwMKu-TDkLs_rrMHi9TuZfI74EqjsJdIXqR5cKb_mXWEWAMmlwZ3aWEDYbyfO3JValB2HUMo4vlPb1Tgre21UFv7xagIzLVsTgtx0MDP4AkWMbok2tBWVtYu6-EmLofF4A_ge4GrK_pD4U52JJTyZlyFdEejrrSc86O92-NcXB0t2-TgOkDsi_nfYRf_0HqxAeaH_ycpoWT9qO8-oyI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47a4bb6889.mp4?token=fBdmhWB3bHSkp6W80parhojLiHeD3ISidu9UKLm2dKhwz-YlmTa0j7deEbpER2XXr41CCl3PcS_oCZ-d6_k0KcaFCBPVpUYegKK96X25ObJNP2mAYHSEO4rWzrFYFgh6anvTxDMgIvRMs9tZetUSH0D_jrFOxpaI4ORQP8O0DfZL6vnwxV1UO1og4I9G9q10iTOgTAhGDZH3psY_yFL7mpd-g3OxPn-0yprBjUAXZXzRc9Vp0BT-kdOo-O0aZ8OpGbKsklrQb9swBixGfYh8LoX_Dtpub4IYQKfApH3SEHC7NOrqK081vGd0-Jo2gOcBhcS0mgD7LXp344VFwzja9nDu7jSrbJCIr7TBvs0rp2YeK--cNNkdLKRWbuUR8AIO-1s-6ZU2F4RC0UTRCEY04UVMe-zUAGnidfB9E35GqLJ6Gdesquw84SfxK8cWsukIxyHprAtJTJ5mSO2N1hMEgZwxbwMKu-TDkLs_rrMHi9TuZfI74EqjsJdIXqR5cKb_mXWEWAMmlwZ3aWEDYbyfO3JValB2HUMo4vlPb1Tgre21UFv7xagIzLVsTgtx0MDP4AkWMbok2tBWVtYu6-EmLofF4A_ge4GrK_pD4U52JJTyZlyFdEejrrSc86O92-NcXB0t2-TgOkDsi_nfYRf_0HqxAeaH_ycpoWT9qO8-oyI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺
این 3 دقیقه هم ببینید جالبه؛ گزارشگر داشت بعد گل سوم الجزایر خودشو پاره میکرد که یک کشور مسلمان به داد یک کشور مسلمان دیگه رسید. به دقیقه نکشید بعدش الجزایر گل مساوی رو خورد.
😦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/Futball180TV/96614" target="_blank">📅 10:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96613">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/949f56bccd.mp4?token=AxXLRUJL4mP1mqwG2JkAZAJXXJvgMzgZSZBWqRbP_yZ5qXOucKlwehkmpDwud5qIpZ5ya6fJEjq3n27KrB-5D19w0YyYyBhWxk1QhfeEwxiY3cP_jOqY8TtZM5_l-Y4sa8j50d9m_VaAN7BbKHbrI-3opn_J-RdB26QcG5mWCQVx7agdrRvbA-_P6VnwrZRTQmoIf6GK0-I6UeuUpRX0ADnFCxPpBWv8VkKRcbgl6keAOuUopirp-3i2rgH7bvmlb0a0H9xyyy5kog974Fl1cx-fIXAPU7zu-fqrEMdrqm29tmd03JeLKVYmA-vPL96cba-7REOM179agfRo_zvFLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/949f56bccd.mp4?token=AxXLRUJL4mP1mqwG2JkAZAJXXJvgMzgZSZBWqRbP_yZ5qXOucKlwehkmpDwud5qIpZ5ya6fJEjq3n27KrB-5D19w0YyYyBhWxk1QhfeEwxiY3cP_jOqY8TtZM5_l-Y4sa8j50d9m_VaAN7BbKHbrI-3opn_J-RdB26QcG5mWCQVx7agdrRvbA-_P6VnwrZRTQmoIf6GK0-I6UeuUpRX0ADnFCxPpBWv8VkKRcbgl6keAOuUopirp-3i2rgH7bvmlb0a0H9xyyy5kog974Fl1cx-fIXAPU7zu-fqrEMdrqm29tmd03JeLKVYmA-vPL96cba-7REOM179agfRo_zvFLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
آقای‌طارمی حقیقتا خاک‌تو سرت
😁
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/Futball180TV/96613" target="_blank">📅 10:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96608">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L1l23Zw2Nja9CjtoFEa19J6l5rIo5SuAerGC7KRTZOQsc_MbsFducxRmdlyxk9iO3VDFZIklD0gaGeeKvIaWpq7g2EDb4ztegHsOkX6sBx84tVd7t0KRd35uGlI1u3injpf4zbUOtBarvTY3YKVXkZIN9Lh96AEaqSGeLBUCwukaPptSg_TvQBWJhSDgYtgkKqXs8dId_ruuJTcY1d8Ogp8YIvjuGqNvTFtwm9AcCNfpZ8Uv58NAvOWHyhaMlwUC0QzNoncN8XVs3Y8x2Aj5Tfsij7fjT9xJLtK3gkD5qZ1lqYlkggXhE8t5akengWaauUKGb-2fFDybba9YUL3uWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E9rcAOPSz0_ct4MSt-Sqc0mkPsWaaFs6KCO0MRuRXJwlmQduIDIUGbd6IH83uOzUi1E96k4TjTz7sKtC30zdO8ChAQkfQUSoLzf28kmFUDmMJl2y4ReOzZSavDuI7AbiyloIo_Xfy0tcx5lr-Zl2BxPUtm60M1fuiTtI-rkwgtECr_OlnGOkSrjaBja0w-0yZsTUbFsZhqwHRNzrOzdTzaq-iipTulXXnLW3LnO49c5n-3tF2ngnMTuSfDYWcb-R9KX1Z0ofW0bLSDXVbRQ872MOY5ESlKiAg-PG630ASMQA8M5AK_Ig3az0kvLKYaHIcPddbmq1lObc5rsdKMmsSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HdDeRHU_KiG3NkaZDvesO_gl3KNl20jUhxmTMUcquEZ_Tl8JIjcEHmo78vzjgV8rTWoW9mh5ZDIQt-tYJ0q7DHbjNnJpSR23dS1d3lCn2_gC4CsLgFOHH7O70OkKqf7rjA5647WNEkQmnJwAasDrRpz3U8xpco5I6Tm-RgQWNb7IUySBbBfEIT4_A-Cb3kvwreOuslSlosLHg7iubjzcoUBwX9X-9EDANcPqoIlm7NUnI2--iXFBy1Bsuaj8b2Yy0j00PZcJ0tNh-CRZhEl_Zt_3jj0ZtWFRsQE8KQfZYsNrZBPlUDRcwljLuRBOZeOv0dd9vVYKomR5TlaAV5G3kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p2GWQw10QGZnEsjfdwnVrHJvt-jqKKh6CNLtX5tcCr0kuveLaW8fB-XD7KhbycZboqOs70wYgLqqEsfC7GwMv10KjrWk205-W_leZh29hvJF5qKI6qqjAL8Ea9vOyp3zTLNhGcb109aeVQzMwIkG-drlodBh69OGFTbUqBSzfJWS3UBG9ap2BYQguwJ-wwiqpCyeCh337Pio3k0iuXpvPk2ON6DlGbwLO9Sw7R9lXWZxZnx8YkdPUoXaWF-sFBilj2_twKk7VaDdcBdo-DC7fQENIR8RZ1nMmeKLLnCpjzfzSTL0_4hnoNnppcsG_veNBsPi6L5sqoDPWWvMyybAqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VM3MlzlVxaRvaVh9oi1Bv1iCB5CalGbw-okOqvg1ldkLbcAwXf-1FHCOl1bEogAIBFhqJgP63lufX5JcligMUUQUPEo7gh7-KhRDoPqvyqoIgq9t0ySJK3WQhXJIbF4bfGKD6ek21wEfz4McLUwKBMD6wS3usKrTQ4pbtvCOhIdCTUjz0bunQsCtgl4SzldujLEPUFiNKJKB1w1VXOoZQAXu0QrUVw6Pby-h1YaRbhSbaXHMdeeZJT8KeVw5F9j_PewroOZGgeGRJc00uFMtpX8Xtak58y7XnBjq7eBOqOcsMke1V_RaYC--lBILgoSLn0GQiLBT6s7-VuHRxFdBFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
🇵🇹
دوست‌دختر زیبای آقای ژوائو نوس تو بازی بامداد امروز کلمبیا و پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/Futball180TV/96608" target="_blank">📅 09:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96607">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4afef79198.mp4?token=Dqi7znXa60CRjp446pBcdJwRDYN7NO0mEF_Hd9cLzJIB5eTsrm8dmRyZG1gegt80CE8d2q2C5-iphroHcYzNI7jqRIGa7Esm4z0jy3XOrAFAeX25TvvpYbaliLKwkq9PL6LuAZKwO0Sz6-xNHlrucKdMQBG5DTABpHrzQHcK10UOW-EpN4_DCkp7zaDxFkuAS3wQdNbTitrIDuOJdEBh2a-nUVZQo4AlFKFQqrNlTQXsAzONeldbKCZy0A4I6JLIN8Dl980PJhKFz83xFcP2RSlzGEfA90OvMrR0n9XGDoFb8-cVI8-uJhD17-EN4bTxqFr4BSDMSN2RA0H8ketMMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4afef79198.mp4?token=Dqi7znXa60CRjp446pBcdJwRDYN7NO0mEF_Hd9cLzJIB5eTsrm8dmRyZG1gegt80CE8d2q2C5-iphroHcYzNI7jqRIGa7Esm4z0jy3XOrAFAeX25TvvpYbaliLKwkq9PL6LuAZKwO0Sz6-xNHlrucKdMQBG5DTABpHrzQHcK10UOW-EpN4_DCkp7zaDxFkuAS3wQdNbTitrIDuOJdEBh2a-nUVZQo4AlFKFQqrNlTQXsAzONeldbKCZy0A4I6JLIN8Dl980PJhKFz83xFcP2RSlzGEfA90OvMrR0n9XGDoFb8-cVI8-uJhD17-EN4bTxqFr4BSDMSN2RA0H8ketMMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اثرات نبردن بازی با مصر که کله صبح باعث شده مردم اعصابشون کیری بشه
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/Futball180TV/96607" target="_blank">📅 09:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96606">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4378d23f3.mp4?token=Po-zYqFkVswBelMrp8QkS4MD6Sp2wjeDPbGRTIqMaMWRhbQZAEtgFamUWfiucsBeO2cVEtUqlQLnTOsJaC6NwEO0zwhbIHayT_2SrlEZTnUnogEs1gH58ug1WRRiKEHppDI58nkvUcqJ2___IuUJJOiHQO4Gu_kKoEaLgwbuJL942cDPYe3fhYJNgvTGT3HhpFKals2-xUMfF_hvrTcZG5eBijnEI9mpJAtlw90ibEHUaKmI8m4b6kM9w67wuPwgtGLnNj5GI6x1tJtOY48LL_rTx2UZMcrB_4Du8rMz4oXOeJtbIvYF0JGNbb6Htn-2FsZFK_Ccl4p7ehO1zaJJOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4378d23f3.mp4?token=Po-zYqFkVswBelMrp8QkS4MD6Sp2wjeDPbGRTIqMaMWRhbQZAEtgFamUWfiucsBeO2cVEtUqlQLnTOsJaC6NwEO0zwhbIHayT_2SrlEZTnUnogEs1gH58ug1WRRiKEHppDI58nkvUcqJ2___IuUJJOiHQO4Gu_kKoEaLgwbuJL942cDPYe3fhYJNgvTGT3HhpFKals2-xUMfF_hvrTcZG5eBijnEI9mpJAtlw90ibEHUaKmI8m4b6kM9w67wuPwgtGLnNj5GI6x1tJtOY48LL_rTx2UZMcrB_4Du8rMz4oXOeJtbIvYF0JGNbb6Htn-2FsZFK_Ccl4p7ehO1zaJJOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
هوادار ایرانی ساکن آمریکا بعد بازی مصر خطاب به امیر قلعه‌نویی و بازیکناش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/Futball180TV/96606" target="_blank">📅 09:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96604">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XmOOvH_kab3F_2Ce5wibqLcpWQULajPgUe46D6HYlY0TXm9U7LoHwErkC3huEVlt9OIJNHj9jFPfC7zEOeS_8G88G3VKqTAt4LPWuqHXJf8LuWLxQFV2jaM-35hI6NmzBU5RzuoiVaFawYAUtJb7P4PUERLqXJeJS8q3XAuZoMV8Ah3ElLivWiJ7Vw2ehY6NTH4lo695ntlaAPZOV5Cnvk1Ki8nvy4LfquvgEv9LJF_LSkoG3gKZc4buIOnl47nMFyyO5eYA2OgFnhcOjdEQednG9uhtGXUhXgFX6ryPJ294RT_414R51dizzTiSF3yhVwpGBNeQBXbIMMqLsfyWJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bUScTUoVpSbDezrybew5rmnYobu-7KME77OxmdTsp1F0vKwJJNhw8S368ekmHKktZhvwBXM2GAEvm8zws0hlHIy4NphFnKUqDW_Wi4zYiFovlDoy_c39AVj2fSQRJPnYDw_jNtTdBgajaDBVTnUk6tLhQeDn5MSgACO4K4Lgq2kL1s3Ym1EbZDodOZwWnypy-IIAwSyeAQDZ5nsq19MPB0rZxQJ8v_OCD3U3s_nC836h9ZL8dyqVmgVU5M9epc0zXAifztuw18ENK1oVejnS5_H8p7uu8Lu4PtpgyBCXQwMmMPsOgLMY9LVVDLoiKU-VvOsFRcD9ROmCjKhSBRT94w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
‼️
📊
آمار از سایت StatMuse:
۷ بازی پیاپی با گلزنی در جام جهانی
😮‍💨
🇦🇷
🆚
۷ بازی پیاپی بدون دریبل موفق در جام جهانی
🧐
🇵🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/Futball180TV/96604" target="_blank">📅 08:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96602">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
😛
😛
میثاقی: بازیکنان الجزایر‌ و اتریش به شکل آشکاری درحال تبانی‌کردن بودند اما نمی‌توانیم به جایی شکایت یا اثبات کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/Futball180TV/96602" target="_blank">📅 07:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96601">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8kWqroMHQ-FQWcEeEwQ0fwpgMeYDO652ZvgvL_db9TnphD6vi_5rwFoIfjQcNatiUiWy3zAU9LygRm9rathKazjSivaxt-Q4h22KBuxuJmPHVr7dUE0Txllyc63BUiQvBTNJMOHOWO7KF32ZjuW36d1CntdKlI3eW3uF9JYIlu_czNj4-SFQcqajxtkFWdKJTSyk0YITiP3-82N0X8LrKKtP9ejRBrBgFDU6rqvsrTeEguASvKZSsZdLWnPy46XncHMzDXSCPLWh36gr2KxpfG02Ph2t7yMdE-Z5XZZ_zMDxNWgIBEyqlH1K6MBglPnZ2yKsv-i5Z69wqxK1lHdtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
📊
🏆
جدول بهترین گلزنان جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/Futball180TV/96601" target="_blank">📅 07:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96600">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWjT_vikeMvgwmSCG324Y3Kgqy6FyrjB5ICJKnGpiaYF1r2SRB2T5nE_sCPDxSh4TeJMeLWM_63rtCfqyslbYRlE0pb0d5-xyjoabVPzr8IDJRGA-jqUdeNnPBdO3bVqOvO57Jw2I5mGcH3BdBifQmH_FkMba2J_tfBfAN0SJeB_BRLoaZUkCswON6JXJ4danQs4XGRYCgmh-WG8e-f8_RwmKakKZq65y_LT73LZenyZsusvYuNdW3PYE9SC59rDATtnPVSi8sCQBJHZHMp8UbGg7jMDauzkCOv7_RCXBn2cU-RyBBK2EqSUqShxQ5aq16vTCDcfocfAeTVtIPzccQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس پیج تیم ملی مصر به شجاع
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/Futball180TV/96600" target="_blank">📅 07:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96599">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjtUeprLKcE_tdNUQ_K_tWp0BArpwx3BLHV3X7yw-IHLMCMRo06Vg1aeBwPC_Ux-SKLwF5ajmAq8AP2WDwc3uUwI4RyPzAhadNWSd-RtYao6FbnhaCtk-Mae_-AUv6oDTYtwZL6ZoHkeIXfUVQvbif9tpzO87iDYWpGe3z3VOlONU358DwZAnK8NwpdqTF8LzGqxywrXwuMGCGcyylM2-7viZGGHaK-tA2ZisdWGhojReg08v_qiZthc0Hi6xwc7QDkCAyx6Rqo3owEigf8uLdQm9JOm_ohjLzgGcIyn6MZC0NFyqatxwwytNznS_-0DMlnGGWbJzMl9WqUehaoatg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
لیونل مسی تبدیل به سومین تعویضی تاریخ جام جهانی شد که از روی ضربه ایستگاهی گل میزند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/Futball180TV/96599" target="_blank">📅 07:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96598">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXeKHqWsGmMLeKU7wtagOkXBiCJZjznS9Zpmw6uUs7ZD8vbARI3y2IzjwgU1WkAn3bCmP3HNPhdvE9sGvC2Xv_fF8R6OC0cNuoUSSA34zBGr0cekg6w1e9g-Yv3TKcypqLYuAGCLN0ielAPUsoQe2pC2y2e_Wt2p3T6BJfY350KPMiHtYsmCDmTLd2YFH0JLh0eDSDOZ_fvJ7_O-nRLIn7fp7Fjz7bO1FywFDkSsu9z95BuLkbQ0P7e0t5SWTWPs23YUoprFHsEoJErqPP852NKM2tg2bfOQ0yydTdfJ-w58GtDMGAajZBb2pC1eroqpjcec6INKKACmiciZvif8XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🤯
مسی در ۱۰ بازی آخرش در جام جهانی
🐐
🏟️
— ۱۰ بازی
؛
۱۳ گل
؛
۳ پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/Futball180TV/96598" target="_blank">📅 07:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96596">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🏆
نمودار درختی جام‌جهانی تکمیل شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/Futball180TV/96596" target="_blank">📅 07:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96595">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTPm4KVxjbJLfKTLE-m7qYABWXToHF5n472dm6WXve03gtydC8v4ZXuJYhY2gT4wAxquEkjc708hN3KID64oNH7OUiVgCTjGnTdlTgPTWB2Q9COSu0EOmW4DhjAUTQ-qClsd4vJfgrVVtDP7XJipB-cvbY5zhiUwK4yYnUjcYDq2Ia5Hs0M0I3wToQOKh-SJ0GdFsP3AWCmLerKzy1IvNnTB4kX7lSwg5GH3xGAhrGz3Kqk2MML7DqH5g9siUHMlBRgOh3Md_RdILEDgvWbFrxTks1KIsE3ExItwkW-icqJySdks7wGFG0V51x-E0ybB_NORs0at_KBmxpcRZD8big.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
نمودار درختی جام‌جهانی تکمیل شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/Futball180TV/96595" target="_blank">📅 07:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96594">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
ایران رسما از جام‌جهانی حذف شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/Futball180TV/96594" target="_blank">📅 07:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96593">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">قشنگ قلعه رو سکته دادن</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/Futball180TV/96593" target="_blank">📅 07:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96592">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">پشمام عجب بازی ای شد</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/Futball180TV/96592" target="_blank">📅 07:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96591">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اتریش مساوی رو زددد</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/Futball180TV/96591" target="_blank">📅 07:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96590">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">😂
😂
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/Futball180TV/96590" target="_blank">📅 07:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96589">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">چه دقیقه ای زد</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/Futball180TV/96589" target="_blank">📅 07:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96588">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">پشمام الجزایر سومی رو زددد</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/Futball180TV/96588" target="_blank">📅 07:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96586">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pdd-gmU57I05Ic7MdEjlHVa8B4wu45QCenKtG7Ij1AYQRmkFc2CxihnJwmjk-vjdsUdNzya5TI9jTuhNXyR7oTrhUw4509PRosJz0k_9hqH_rwl5iE03VXFo7Co-2f3yhTEmjjbZv_hl2FsQyRUC3nll7UiySdPSgYj9etu2BejAA42BwYn9P6Ob_lN9LXNFnocaBRIyt8is8Srfy8OGL5_Zv_u3q-saORXvQ6LW8Syo5p38gp0QUIuQrmOxF5mj9lecUfubKmBDgH8dnQml2UyKR7B2TeLsHn9RQgx9_zuMn-HNmSCpgkRqQfgAzfbQ8AqYOyCy7ssuZkkmNG2i7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bMWBvPsxN5yALdvy-DzIWbiEy7RRs8Bd5aViwYjvYvVb-CharJAslFeFwqGpncoCs_EZR2tICP5-wH54-dFOSutcXe14F8ApeyT0zfStFGnX8c-b85evuG8b3iLe3GRVZOmM4DRTU1vKydLUZ4G72UFHMh3A8YpdGp5CRuozFXt_ACJcqgEP-ZNqYoNTTaC0np6J9_3bPQCj2wtiID5Cso6xCVfZOn6JOgYYXZadYW0AtkqiF9dsgGL352Vwp4tn4Vj1DHDOw_OU-WFdh9dr7hJSWTOOFxcraOr8FBBXupjf7h-3BLWi5c5aPdGQOHbdLBG3kOBle7r0x7740QdTgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شادی مسی و بانو تو ورزشگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/Futball180TV/96586" target="_blank">📅 07:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96585">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F25jvwKETGpkamisCXBIXOmBdDvgVHdLjHydJAbTFHLHnUWU33LrmKuWoHUB4B_F01JRhVRBvDWy_HzhKkXg_Gjhs-DPMe4py3MxI90iOtDL7Joy1oY__o27MfsPZDIstX9lky6WpQOqDumCVkDt5Vruyh-SDoQKRyalTQFjHkrQ4CH9RTNWwdCKsmVlfXVTemlvrPuQDREOzkz-tYA8V5bKzJ2xFkXDsaJAJGPKpjDUfWV22b-JMOhbZLy4FAZ6KPz3rS1z4gyX3_sNBK_05KikZLD_8RWaTxVtdPJNuW-1_P0qwKEubKTNv9JirVJwCidfGhW8oGKF-Xr3kvZtcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
1331 GOAL & ASSIST
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/Futball180TV/96585" target="_blank">📅 07:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96584">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2ad9070b5.mp4?token=UwnIN09htETMojp8rJBkoN-NG3rDH3-2F8x_Hd4bIvc5iH_x5y39yoSeeP3psa4s3Ng9fn9nfwmYSq7KM4SbqcL3Lf0RRNja_0AcUFu3CARcrUCWLeVSRlPlI6cE021k7M7NtegWJo8dXmpiLvNzkvkbYWG2l--KIfqAasbz-_yJCgUuuTfjBnGYsdS4t7wnjZhO_Prv3DPe21aQOkFHIp1Cwy_Iwnmfx2NX3ZpTKspb_o744yn1aJro2QygRI_gIDRA6hZkYd22hCTNXCewUg3pMiMWmFOkfwovMk_e3GgfD6AqqZPbVcXrrCwE7Yc4pGeJJ9ervwSat4otccxPQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2ad9070b5.mp4?token=UwnIN09htETMojp8rJBkoN-NG3rDH3-2F8x_Hd4bIvc5iH_x5y39yoSeeP3psa4s3Ng9fn9nfwmYSq7KM4SbqcL3Lf0RRNja_0AcUFu3CARcrUCWLeVSRlPlI6cE021k7M7NtegWJo8dXmpiLvNzkvkbYWG2l--KIfqAasbz-_yJCgUuuTfjBnGYsdS4t7wnjZhO_Prv3DPe21aQOkFHIp1Cwy_Iwnmfx2NX3ZpTKspb_o744yn1aJro2QygRI_gIDRA6hZkYd22hCTNXCewUg3pMiMWmFOkfwovMk_e3GgfD6AqqZPbVcXrrCwE7Yc4pGeJJ9ervwSat4otccxPQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
سوپرگل لیونل‌مسی از نمای تماشاگران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/Futball180TV/96584" target="_blank">📅 07:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96583">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avTG_BAllrGtOEItNvGVpF-0qL1sNH61oAihTXez8r1Zy0wv74B20NBpRIwKuKXxJXCiAt9l8lu5QojPHoWvfDrD3Tk7X1wDv4_nTlUg_YIhWu7ETbhzw8gU-nF1NawElAfVHbQrxGPkLp6dMGFL7GemV94C_M5Kw-4Dm_q0JjSfhipOkVNl1dSn7askfFooIPAlRRSLqOvNrohWU4B4hblhs7RZWsM6rMVtQs_xt8LSiJeBZX4CUi-j5sUvEu4S7Wx41oaiZ4NHwYlLxZcPyCXOme4zGVGGX1bSwPoyQYDl3380MpvgBArETZO-abjm17SjX9cHUKcJfn4_D1SJ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
لیونل مسی به اولین بازیکن تاریخ جام جهانی تبدیل شد که در هفت بازی متوالی گلزنی می کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/96583" target="_blank">📅 07:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96582">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/687290f3c6.mp4?token=kZc6GjjGElaImaWgQPqhY_qMIVl0DbTU0K-87wpl04LxygLeqrYHFrhJWwdhKeahUmyFmZCtOXB9NsxxoZ5wPHZ9fd5X70tnSdNwfegjMwXXgtCTa2mHdc4hMSJxNM1yiK0JkaZQdoNlSvUMVYAeYujbA68uXUNfOveGEWfLEgLrOSrGt1oEWGNPC0DoNLvqSQPW8VlynA8ofrOrgvVGnmi-1u6ndM8jGnBvOW4hS1hyv2PLRdf_bRq6rfXDVegVKCRnmYjk-FbI3QNGxK8slpMMlCBUTHonsFMm7hcQC0ZgGNZIrBnmezYCkol5BkjBBFy54Fxr9agEdhaLHgaw2Ltxh3O9VbJMOfQ8E_s80p_WNFUKdodh-j-9jRUapmak3tJLkSO4eDfmrL9hBLWbXRKMNuiBm6igHXwPgAcxSRovD9NroTtGKU6kEG-XMeppC-qhCCB5VyXwrUSLbveBIv4HXYa85pO8-VAg1WlbRdDKDpspRDNae1BrSjFx2k1AX-oSakO8kOP-lQwCXc_fFjOHlejFU2P_iU3gox4-a16zXOrgFXzdvlJuT0Jmgo2393gVK5QofWNXywKh5bnIe7-fAi0qdCkjshb5Uam-NcS28msxSuAmIVqJDjaXeouAUoK_pJF7RLX_COkmBRD1DDuAYIKUvDfftOwkOhskGIc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/687290f3c6.mp4?token=kZc6GjjGElaImaWgQPqhY_qMIVl0DbTU0K-87wpl04LxygLeqrYHFrhJWwdhKeahUmyFmZCtOXB9NsxxoZ5wPHZ9fd5X70tnSdNwfegjMwXXgtCTa2mHdc4hMSJxNM1yiK0JkaZQdoNlSvUMVYAeYujbA68uXUNfOveGEWfLEgLrOSrGt1oEWGNPC0DoNLvqSQPW8VlynA8ofrOrgvVGnmi-1u6ndM8jGnBvOW4hS1hyv2PLRdf_bRq6rfXDVegVKCRnmYjk-FbI3QNGxK8slpMMlCBUTHonsFMm7hcQC0ZgGNZIrBnmezYCkol5BkjBBFy54Fxr9agEdhaLHgaw2Ltxh3O9VbJMOfQ8E_s80p_WNFUKdodh-j-9jRUapmak3tJLkSO4eDfmrL9hBLWbXRKMNuiBm6igHXwPgAcxSRovD9NroTtGKU6kEG-XMeppC-qhCCB5VyXwrUSLbveBIv4HXYa85pO8-VAg1WlbRdDKDpspRDNae1BrSjFx2k1AX-oSakO8kOP-lQwCXc_fFjOHlejFU2P_iU3gox4-a16zXOrgFXzdvlJuT0Jmgo2393gVK5QofWNXywKh5bnIe7-fAi0qdCkjshb5Uam-NcS28msxSuAmIVqJDjaXeouAUoK_pJF7RLX_COkmBRD1DDuAYIKUvDfftOwkOhskGIc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل سوم آرژانتین به اردن توسط مسی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/96582" target="_blank">📅 07:13 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96581">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">مسی ایستگاهی زددد</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/96581" target="_blank">📅 07:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96580">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/96580" target="_blank">📅 07:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96579">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">مسی هم به بازی اومد
🔥</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/96579" target="_blank">📅 06:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96578">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d80fe6f9b5.mp4?token=CBhs_QC2WI9trRv8TZQkoqvU0rXCwQOGsKk84QqsFlQ-X2DiLGLu2cs5NXmCEBavnTzavjgAm9vvEViuv8x-lG4LEspRd52RAMJy3kU7pMzZAMu1aguFKbHthHWk5lba_6VyKMVGzWw5WsS4OnXrCLcFdPXdEBPbInh6wabltBNDTwEHlTMB21My6qFLv3Klnvsh1nAD5YF-jUR-NxtPF0tlMUOhLR6NLNGVU5dWX2XRzwS6YnpAyt7uDujeSWtDvBhIu1SYnoRjQ4ir-c2rqs2PhWbchJhmGezSJaipkr6-0HR3NudTU9pjXFcapg8PJFOigm6yEW3MYdUBsmEI1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d80fe6f9b5.mp4?token=CBhs_QC2WI9trRv8TZQkoqvU0rXCwQOGsKk84QqsFlQ-X2DiLGLu2cs5NXmCEBavnTzavjgAm9vvEViuv8x-lG4LEspRd52RAMJy3kU7pMzZAMu1aguFKbHthHWk5lba_6VyKMVGzWw5WsS4OnXrCLcFdPXdEBPbInh6wabltBNDTwEHlTMB21My6qFLv3Klnvsh1nAD5YF-jUR-NxtPF0tlMUOhLR6NLNGVU5dWX2XRzwS6YnpAyt7uDujeSWtDvBhIu1SYnoRjQ4ir-c2rqs2PhWbchJhmGezSJaipkr6-0HR3NudTU9pjXFcapg8PJFOigm6yEW3MYdUBsmEI1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇴
گلللل اول اردن به آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/96578" target="_blank">📅 06:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96577">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">الجزایر گل مساوی رو زددددد</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/96577" target="_blank">📅 06:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96576">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/958bddc7c4.mp4?token=P9QdTqugc8ObJBuP0QLOZtapF4W_8usCK_748GSiSrLjPmwl6WNUbr_J-7j755IZfXp561lJqSrwvMyZV2ziKgJeZjs2AUpCPLsF67vEmNWJ-L0iqxByaWxl7A2D1IKAwljT0XbqM0RQpjfoiCk2l3HZPOFA6xkmO1u3982-fYZ008jatAMAOY8P2yRyS68Y7HsTPkk-gI_QiqFjkn_SH8HG6jVsx7K7eSq411ioa-5leiH0WXvgGQS4jp40sVRbwJHs7AQhlgkYe48GcMXXE1eGJxWcHtq77vzzcBgU3XzzEIaNx6Zutq2Ca4TtiHo-fhb-kBY3PhZlqoapYuXHnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/958bddc7c4.mp4?token=P9QdTqugc8ObJBuP0QLOZtapF4W_8usCK_748GSiSrLjPmwl6WNUbr_J-7j755IZfXp561lJqSrwvMyZV2ziKgJeZjs2AUpCPLsF67vEmNWJ-L0iqxByaWxl7A2D1IKAwljT0XbqM0RQpjfoiCk2l3HZPOFA6xkmO1u3982-fYZ008jatAMAOY8P2yRyS68Y7HsTPkk-gI_QiqFjkn_SH8HG6jVsx7K7eSq411ioa-5leiH0WXvgGQS4jp40sVRbwJHs7AQhlgkYe48GcMXXE1eGJxWcHtq77vzzcBgU3XzzEIaNx6Zutq2Ca4TtiHo-fhb-kBY3PhZlqoapYuXHnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇹
گل دوم اتریش به الجزایر توسط سابیتزر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/96576" target="_blank">📅 06:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96575">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/96575" target="_blank">📅 06:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96574">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">سابیتزر</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/96574" target="_blank">📅 06:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96573">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اتریش زد
🤣
🤣</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/96573" target="_blank">📅 06:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96572">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">پشماممممممممم</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/96572" target="_blank">📅 06:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96571">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اردنننننننن</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/96571" target="_blank">📅 06:47 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
