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
<img src="https://cdn4.telesco.pe/file/OaS3uoQ9MA3zcDhwryMZ7vZ9wwqovitJoW-SLG8y2uQoxCx6VpDv6WskDf2vJt-Kxl7Gbx3nuCUcjS0GvsUez4gGK-3rzXRDOYWfYJaSCem6AubDqD7Vme9DsBw3qa2qo3XPM686ntk7XeRRspD7tVGgNeOkjNMLqDm3cZaDeoEydfYkq6eHA8aF3zxVnAKGtSJ3WNeiaREpsavvqpCp2oWatBfsAkTRsErDX1KqFg3MWWLNW7Le6gt7uksJphxWuXAONDvRBy6asIKWoY2jV2MyW0ABhgQ8fGM2zHryQe5tC2e8WqPbe2fzb1F6IPU5T6l8qZKT8DB0zR-DwzV4pQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 134K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-10 19:30:02</div>
<hr>

<div class="tg-post" id="msg-90573">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hwrSLoZeNy7yI6C1xXJl9nTBoWp1LUbk3haTgBcCPt9jpwi4wEOjNSGYPsOHvsZVX3UqMj6wYLM2H7ClfzhnzGPiiSGVgal6sUyqfIcTAKV6VMIrpunW843vA3tL-714PLF7SlF_57O3WHp1NERnS2a4sK8c70_R3YjVBRnzcQ4Q33MH5ndamQY-D_m14QXTmJtGc4iZTrrlQjS0boSutmD4rfoMm576Wye40NePU6OShC0goRJTawmxSjyXROLs_LgdGLFLqKXdcbJZWZEvFC837Qq895III8dbbERPmJDigPppNGtLWSgo5HuVhVNsL1pox3qm9DTOXts8yWw5rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
کواراتسخلیا به‌عنوان بهترین بازیکن فصل لیگ‌قهرمانان انتخاب شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 610 · <a href="https://t.me/Futball180TV/90573" target="_blank">📅 19:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90572">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">💩
⚠️
دیگه #فریب بونوس های الکی سایت های سودجو رو نخورید
❌
💲
بیا توی سایت مورد تایید ما یعنی #وینرو و با عضویت 500 هزار تومان اعتبار بی قیدو شرط بگیر
👏
🤩
با عضویت
🤩
🤩
🤩
هزار تومان اعتبار رایگان بگیر!
⌛
پشتیبانی 24 ساعته
🌐
Winro.io
🌐
Winro.io  کانال بونوس…</div>
<div class="tg-footer">👁️ 310 · <a href="https://t.me/Futball180TV/90572" target="_blank">📅 19:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90571">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrHfqDgZecFseSwc3Cace1SG1PV0DPtPKOt4OrJCOCKX_G5A0wn-QHAjqCKFVuzAIo3eStAoTzpYUc6qdTw-ZDWThAwLdPCM251awVW-sxWUcAsGZrHxxAty55Ks2W9kYJpx_jQ_DS7maL31mjUXvztr1fqQ9XE2kIRCf-WugcReyx62VJpRvZsoN3pnxLyxtJDzuFciA-k8zSrFX5ZMskbNuRmmvyPqVdkzg2pe4EXITat01aDhGSBdq-IqhhDBFB_UQUfdZs9zqBXdNbRASBXZh90SV0_3Bzv3wO9VwEHxJp6yHLHYeXQRo_7zV84zf6zgDoixY-ujxE9h7ruOgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💩
⚠️
دیگه
#فریب
بونوس های الکی سایت های سودجو رو نخورید
❌
💲
بیا توی سایت مورد تایید ما یعنی
#وینرو
و با عضویت 500 هزار تومان اعتبار بی قیدو شرط بگیر
👏
🤩
با عضویت
🤩
🤩
🤩
هزار تومان اعتبار رایگان بگیر!
⌛
پشتیبانی 24 ساعته
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
g10
📱
@winro_io</div>
<div class="tg-footer">👁️ 611 · <a href="https://t.me/Futball180TV/90571" target="_blank">📅 19:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90570">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
اتفاق عجیب در یکی از بازی‌های آمریکای جنوبی؛ یه بازیکن وسط بازی سکته ناقص میزنه که با خوش شانسی محض و اقدام سریع، جون سالم به در میبره
😕
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/Futball180TV/90570" target="_blank">📅 19:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90569">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">کنفدراسیون آسیا با مجوز حرفه ای سپاهان موافقت نکرد و بدین ترتیب فدراسیون باید یک تیم دیگر رو انتخاب کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/Futball180TV/90569" target="_blank">📅 19:11 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90568">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gV8b35O3lmnviE3lImB--wH_i7zeKZ45nVAj-VubsIPuAXK5t0zSwAr0upB5gulCu4x9zU1RRe0C6U9lM0qsXdk0aRl03ZqUJfAVXBZSCl6tELz9q2QWuTLt5_nyvaMI24bDZr4wEvSYhcT2LJ6bXrLafZC4aTuLpQzZ8DZDB7zOBGiQK6L60IsvfoHNDKwIShcE4VPhax8c9_WMRgzZGuk8C96MlcjUKK3wh_brkg2rnGj3FrVvqrl1y3WDNj8NrFdDeJ41y5u8eUK8eDCU4UurMlkdxyZ4gcdU7lqgcsLJ2AyOrNY4M8-NJFxmphs7EWCS-595ENxITNTLUO7K2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم‌ منتخب لیگ قهرمانان اروپا فصل 2025/26
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/Futball180TV/90568" target="_blank">📅 19:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90566">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AX_6oqcIhDdsCcuN44wYYS5F5L7Q5WWfGhyxQ61dNgS6dqRexWSnDkfSFLwMNLXbZtY4CR4P_Oygw95JMrw1bWEPCvVCFwGDMqa3B6kPxvNjiYm7hHiyYWklSWgmi3eLjRYU266Ixa_X8uP-WybUq6yZdlYXUtvfbpPlks5HqtyUWC6v7uDOmTHbA9slo-9Dj7IGUH8adNRqFDtOdn9JCAh5QMAwdJuysLRos_JgsvoNqFITIpCbnuOgqA-JnraELnQdA59EMXG5e32nA-QZx_pkMf4UMEq863D1xBw2hhNYPEhQqNKfTlfj8AqzV523a27SY0v8FPT8F2pJBtmPNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حدود 1 میلیون نفر تو جشن قهرمانی آرسنال شرکت کردن
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/Futball180TV/90566" target="_blank">📅 18:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90565">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c385efd6aa.mp4?token=fDCp1Bjki2xyAg4n0Zcr1vIj__BLhaQ_r5fqXIXFOQ4iEoxhuT6uLV6IE0-rRiVjjoP17zGtdpvKn82X6M5P6f_QWSFHmQL2Bs83gtPbtcrcJwWdDsgXak64ngwLyLPxnV8qT2uHcoFyCAmIz8H7Zd-9UHHpLizZ5uq1ajPS1rp7A5riRTgvrlTE1b4cGNEPxCapBXctf9uG7QjPmL2P3ZTkETPaUTZGPv1thnhRQDlTWPTFjWHXpdpIhVqvATn6a6LHDkwy2Ve51OBYetNg53SBTN2B5Kfq6X0uBV8mSX_NaeUxc1JMHHjUsKaZFcAm1ffqc7AXOc30F-gyK7TpMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c385efd6aa.mp4?token=fDCp1Bjki2xyAg4n0Zcr1vIj__BLhaQ_r5fqXIXFOQ4iEoxhuT6uLV6IE0-rRiVjjoP17zGtdpvKn82X6M5P6f_QWSFHmQL2Bs83gtPbtcrcJwWdDsgXak64ngwLyLPxnV8qT2uHcoFyCAmIz8H7Zd-9UHHpLizZ5uq1ajPS1rp7A5riRTgvrlTE1b4cGNEPxCapBXctf9uG7QjPmL2P3ZTkETPaUTZGPv1thnhRQDlTWPTFjWHXpdpIhVqvATn6a6LHDkwy2Ve51OBYetNg53SBTN2B5Kfq6X0uBV8mSX_NaeUxc1JMHHjUsKaZFcAm1ffqc7AXOc30F-gyK7TpMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست اکانت باشگاه الچه
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/Futball180TV/90565" target="_blank">📅 17:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90564">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOMcnDISgE_R83OcCH2gEvCwcw_-OwW7xGeiQcZLATzlhQwOx8RorBSRH92k6Fj7uwUAgkO5zjzOq8nA5nRwu6jDydKSEGVIzx4vyL6BHYZ0hogJkUQUoxnCgLkUHFlraibJFV-0iGYs52gPAMw7lFfwJkI7aLcBEafTM1DN2L4I1qOkNdExo2EShykIydnY1C4vkHSwsBqcEMJbTGW9qjizpJOO22FxUf4w6NKfjcLY2N5fCBl6pZBBx69bS8JM6_paHLnW8vMBsgDcPzWhDvgiLSJ1kBaxP6UcBPqlehrq30bmEGogbe3ZXVlmhA-h1xx6aTugw_sAIcCy11XexA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
بیشترین تاثیر گذاری تو لیگ قهرمانان این فصل
🇬🇪
کواراتسخلیا : 16 گل و پاس گل
🇬🇧
هری کین : 16 گل و پاس گل
🇫🇷
کیلیان امباپه 16 گل و پاس گل
🇦🇷
‌ خولیان آلوارز 14 گل و پاس گل
🇬🇧
آنتونی گوردون 12 گل و پاس گل
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/Futball180TV/90564" target="_blank">📅 17:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90563">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f90b184b2c.mp4?token=IiliLULFDMN0AVcTyqSFMO4BWXgoboQbXEw6VRQYC-0JRtcusG0Z2JfdYueyTM3tnLMih0tQ9vAZnCwgJ7dcxzXC735XIDpzfbc6-ye_QIQmwb3TcQWjggxgn6Zra5gVzf1nNYsa1ao1HxnPz-EZoIsuAHWO6tC4oP03CR22fJgXwY4S9r0Jaf9JJjvJ6JWPsyJXtNZwbN4-evEwIPug1pyKmCyfs6YDVHmZdmPc0LH32tAcRdQq8Fl1JThZK4NeUFX-o3xgmVQfl6e5z6g3QGhVPhi5RPXsTd45oWYMV4TY2_q5vYPUGTyoPGI2NKsIdItxcXRCYIQUQnBCoDK_1jQZNTDU7rSJ4CTSZWGJZyCxZzKSwWLPntkctarDMuQrJ_ptJswCto6q9w9Oo4zvcuM6QtJk88N8mTrq6MbqWuzoE9FPuM8eJiYSPZFQNuBKYzLjpsUO8vj3gEX3dzINmyZUrrL002PSRjK6oQcrsX90c9Glh0Xri7vNCvB2fiBUqVICxFTXXTsrUEtkZRsmL9HMi37prTl9MmJLVjyIIo0WpDZnsJ-o_I3mgBkIzatI6mQhRSXFxZiJ-27c77GNbVueH9mQVVm95Qln_SxDevwObSbSP_Z_4Qov26-Rb7twKmRcgjdRcO1GhMn18tRFydTyBKYP_HXTZSKw1jIIElM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f90b184b2c.mp4?token=IiliLULFDMN0AVcTyqSFMO4BWXgoboQbXEw6VRQYC-0JRtcusG0Z2JfdYueyTM3tnLMih0tQ9vAZnCwgJ7dcxzXC735XIDpzfbc6-ye_QIQmwb3TcQWjggxgn6Zra5gVzf1nNYsa1ao1HxnPz-EZoIsuAHWO6tC4oP03CR22fJgXwY4S9r0Jaf9JJjvJ6JWPsyJXtNZwbN4-evEwIPug1pyKmCyfs6YDVHmZdmPc0LH32tAcRdQq8Fl1JThZK4NeUFX-o3xgmVQfl6e5z6g3QGhVPhi5RPXsTd45oWYMV4TY2_q5vYPUGTyoPGI2NKsIdItxcXRCYIQUQnBCoDK_1jQZNTDU7rSJ4CTSZWGJZyCxZzKSwWLPntkctarDMuQrJ_ptJswCto6q9w9Oo4zvcuM6QtJk88N8mTrq6MbqWuzoE9FPuM8eJiYSPZFQNuBKYzLjpsUO8vj3gEX3dzINmyZUrrL002PSRjK6oQcrsX90c9Glh0Xri7vNCvB2fiBUqVICxFTXXTsrUEtkZRsmL9HMi37prTl9MmJLVjyIIo0WpDZnsJ-o_I3mgBkIzatI6mQhRSXFxZiJ-27c77GNbVueH9mQVVm95Qln_SxDevwObSbSP_Z_4Qov26-Rb7twKmRcgjdRcO1GhMn18tRFydTyBKYP_HXTZSKw1jIIElM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برزیل از همین الان یکی از مدعیای اصلی جام‌جهانیه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/Futball180TV/90563" target="_blank">📅 17:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90562">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-RRhS96wDzHelGW49bvokcHk3IEoc-mgdZZYD4I6Uol674xxNPDeZS-gt7h4vDGFFAW8N9BnxA2tehKr7RHrSDJczOzk-HToVFZiPo78ARU9XxqbEUDpWJZqTM2FBYtK8bzRpXMd1UDrZ-d2Unt3bQ-ZLWh2X48A_Yh4L2ZS-6-zjNoRCUq3u0HQTJFFKP4-hwAMMLokVr9ID_HGcXyCbNFRb7zBn6Sn8ElYXEJzd1Dd_t93I78K08deuky3iuGAAb0XdFO6562PZ1T_8IuZxpf6rW9tn15iwaxHbngZxzsb-PiLTF6ec49ppuVLAnX-pjgbYW-WCync7JC9JEnRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نونو مندس ‌23 ساله با 19 قهرمانی
🔥
1 لیگ پرتغال
5 لیگ 1 فرانسه
1 سوپرجام اروپا
1 سوپرجام پرتغال
4 سوپرجام فرانسه
1 لیگ ملت‌های اروپا
2 جام حذفی فرانسه
2 لیگ قهرمانان اروپا
1 جام اتحادیه پرتغال
1 جام بین‌المللی فیفا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/Futball180TV/90562" target="_blank">📅 16:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90561">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WOYgUXLwDrjPUUPgNUaUVIcXGigc2uewYjU7k2MftcouljbV1ZKn5Wivlt623OEHQKCxI7202WZ-mySDXYIjWZrknck1kOMGW1oe0UXRYfJI5LdnIN8Odrv4JKjbr26VIe9Ljw712FXMSBSk5Kom-sfpc5_jCzJGiFMv-U4qHfvtF0vTqTn1hm8SGYjvRF27iaytQBUBAMGn7rM6ItZTWB6v7NwpwmPwoYuj53KBN8d6-sEFlEouiUDd1NOvrU90V2RJm_h-9uHqanZYzPVVyjdmd4GlGpQJJiKofIq2cBxzg6spfLJACzz0_otvm6VQQxSuu1qIhxEScpN6YaH1JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤯
🤯
🤯
فکتتتتت پشم‌ریزون اینکه ویلیام پاچو مدافع پاری‌سن‌ژرمن این‌فصل در اروپا هر ۱۷ تا مسابقه رو کامل و بدون تعویض شدن بازی کرده که یک رکورد خارق‌العاده حساب میشه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/Futball180TV/90561" target="_blank">📅 14:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90560">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2LwK687ckn6F24kGUPwGxDPmL4trM5-xi2JDJNqnFgRooAHkSRMjZjaS-hcgvtmCpqiRsE9JN0nZTTxDD4ctlWzgP0aEyB_-NXTyvCSY6CiBdRKwdbYf1AR_HRVUKSxutUfVMjxTG55PLVXxwguCMEDxajj5atW6scUmcDF963NCpOL0C6b_xyW2uUugNxO0DGFDchk1twrRNUQ5WIXXrEbE5VyhDB-tcRZKMlKsKKiK7cd9_jp4qAJREaLIlfv9rU-EJ1xgy0D9GBcRoysd7NVY_cZ1Txn1GYHYeX71znK75Kl4sqr95LUzSvmxePja0LqE2F2R9jLTS9Tt-YWXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤯
🇫🇷
وقتی صحبت از ثبات میشه؛ کافیه بدونین ترکیب اصلی تیم پاری‌سن‌ژرمن نسبت به فینال پارسال تنها یک تغییر داشت و اونم گلر بود. خلاصه که نون تو ثباته و ناصر خلاف خوب بعد چند سال فهمیده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/Futball180TV/90560" target="_blank">📅 14:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90559">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ity-OR9VQ9Cq_8gJWi4HBaVOG4lQ2MRE9du-tpBJYZ7Ie0LQxNQMQl4esPAwKe5Bdi1jh3xLV4h1iBrIlSXK6YWDkJsckayUxXKdX33cXq_2DYNWOeHzOZ8plnsReosIc1WL47jhEehQeV47wh-Ho8lYGbxS8RDtDr8yQkQeWfZnX0vzdqktDo6B9JA8n3MtFRSvHrA0MkYD6KVNDW8leidLsOcXWPz871NnvCCZBsKGMJ7LnbGs8XRtPpNVkRQjVUckRE37kKz3bKMcKig4CeyJrJZCmalSv6vugjiaD-wRi0P_A6iRteNqLN0jfD51oqFLdrQA1cZ_vP3-ZIilRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استایل جدید صابر ابر بازیگر سینما
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/Futball180TV/90559" target="_blank">📅 14:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90558">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iP1ZdIqkg7vq_wi7bmGKufNeJa5axL0ylY7yuOUC_IXSScREfcKpz4q-kpAg_gunjK_mx-bDcTjQNKa6eWHk8jdtjqGCI8pL3rJJ--Md1Y03l4OEKL_FuaTkN8xrll8OMe9eo-_k444FuJTplZ9ZY8vOTDpVV_Zj6fYATetGuFiv917tAAx9j5UJe-vikzj76Ne2Ig2xm0PRNoA7xraZBYzku2JGmLCK9b8zBKrYkyfLyrj8GB0mLvhvHPbNZRNty6fZ0vYZ1R-ftkfTkHTCjR6j5k7rz3_xiQglbNZRbx-0IjvpDaHwdhq2mGbBtTPX_gSY-ZGPnLZpnYQyGUCTkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
‼️
کوارتسخلیا: بازیکنان آرسنال بویی از رقابت جوانمردانه نبرده بودن. اونا خیلی سعی کردن منو به بدترین شکل مصدوم کنن هرچند تا حدودی موفق بودن ولی درس خوبی بهشون دادیم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/Futball180TV/90558" target="_blank">📅 14:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90557">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nTjM167hiqZqGI0cPvn2A4HbujWtT6pZHKeKrcu4rpG9XMLcRzNLa44JdTn3JeEXsm3fGWvqKxBUqosqu1wrSXyxRadZDMWaWEkVEGWnaWXRgJRSG-J9JiLkKGlhbzuFhlbh9RagoMVviyTa-d55fE5g1GXkSSfCRxIR98Ho2KZwlsdKLwf8IFa7c2W5r1CLJsTG-fju4B289kCV-7nT8WLhtwy7tWnGvTzUgd1dIL0NLEoZJlEy0kCbH7fh4zUbhEDXHj90IsHvzGiRpoTyCcLE8ZkEmn7FUeN3XyTFffJkmJMQep8mnNvKNgieOBPqoDUC8gAs_dqd9SzMAtYJrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
وزیر کشور فرانسه: در‌ پی آشوب دیشب خیابانی در شهر پاریس، بیش از ۷۰۰ نفر بازداشت شده‌اند و حدود ۶۰ مامور پلیس شدیدا مجروح شده‌اند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/90557" target="_blank">📅 13:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90556">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUEVL3IrgD_XO-EGPshuURdjyeyB1cYml_2Q0usAlSV8CttXHJ2A0olymWCDHpZ8yTysqbLKKN3Ux1coBrFaaXvJbpBh7RYlU7Gu7kysPfdMqwy2Bg0ylUNDDJiU9PQsVvkj8t6PEX9RqpiO5anNFc5JNmFWQfZEvKxQOq_1qSDl5Z907GXLL23eqwYkjySWfTnZRZBm_axLb4i-lRLy8Sm5QSys2Hid7Q3keflxlDmeQyAaDHNJ9WPkBaynz3ZT04eh3GNmElPw8Mxs-ZS0I-Jfss-oAAZwMP7lK6yw1y2dcP5Yow6c65t44GvbIe-i0Tf4V9ZTEs__qjkt_gDD3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
وضعیت وینیسیوس و دمبله با و‌ بدون امباپه:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/Futball180TV/90556" target="_blank">📅 13:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90555">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p573C5BthfaTH5Cm4X0Jr_iaN65mCSMpusXiHGvaFoNvtrP0VTaARDX5wBytrs5bqybB3XJR4Emz9bh4YQGpR-l26jzUIAwWM-Yy62bUZeFf5v9DmPJVMfmLQeGquroz93IjXwOzSKqUN0YJb8ugpgDDpyHkGq5RI5DB14V9OlaW_QAogbsc-S_r3F0ZIO70eb8DGSIFRuTu2RkT09EfrusD-Ry4PAs1tahQ5okQ2UI8m0Mr8Ce4ov-Kl5DU3j7HH2VH2IQt2pdUVSsBtIxtigpyfK-vu5dlxY5AvTY4zLC-Dmstlj5UQi3RUFb4ecYDOJl8K1NRoqDSfYCky5JYmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مونیرالحدادی بازیکن استقلال و همسرش در تعطیلات
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/Futball180TV/90555" target="_blank">📅 13:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90554">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
❌
🎉
کافیه فقط عضو بشی تا #وینرو  بهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io…</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/Futball180TV/90554" target="_blank">📅 13:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90553">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuZ38GJ0AEYqhg05vFPm1u_pdPFSw6OhQ8UrPlfj1wYQvl6sfiFJxc_dJ4SEyJgn8Rz9YUSBBEW91HLeLqF7bVQOPhzq-hA-9gVKhF2Yxk9TAdBO9Wn6yzGofwRNTHRQco1UHFfjXkufRt3cP73WACLCzQTS1mC3XBLa4CjqgFuRIANPBeK3awP68qyBfLLU_S-DHkz1If_f369dphgQHIQxsa5iUwT20XvWmYpWjacC1yypo6ZoetIVsU4WkoPO6UtVeAtjvC-XOhac7rHPGDtdJDtCpZ7i5uupWkihdsaCEXTNWhvT9ZblsKpSaRCmUuus4oEd999yLs1IzA8GXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
❌
🎉
کافیه فقط عضو بشی تا
#وینرو
بهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
r10
📱
@winro_io</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/Futball180TV/90553" target="_blank">📅 13:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90551">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba8df4a4da.mp4?token=FeM0dpG5xP6nmvd4uQygcutB8VNADPOvNncLjV-ikfTtolV6fYrzw_5xaDFed7QRssCZuDMGqr5CQg02tc4wvpdP7IBw9fpTPdcPIgD78Un2_ga8Wnbnl4wzlXP1hPHvFeQ-U34Z09OWLdsFx0j4jpQn22ZO7yYgLUFHN2GhtWMHti1AwAlF5nLkRReVQsbKn9APhh24FqJOEvDX6iMdp8azi5Np_PqPIrtxdVwbFoLzUCT8ZsJVXu1q3fQLORQWVhFIX-4oCVMaJu1emEv2QBEPJgGRMzqYtjL1B53e4Qi19hGYbZEuCoGxVl9YjyVFfiCl39jyDyjQvJZlhcBkiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba8df4a4da.mp4?token=FeM0dpG5xP6nmvd4uQygcutB8VNADPOvNncLjV-ikfTtolV6fYrzw_5xaDFed7QRssCZuDMGqr5CQg02tc4wvpdP7IBw9fpTPdcPIgD78Un2_ga8Wnbnl4wzlXP1hPHvFeQ-U34Z09OWLdsFx0j4jpQn22ZO7yYgLUFHN2GhtWMHti1AwAlF5nLkRReVQsbKn9APhh24FqJOEvDX6iMdp8azi5Np_PqPIrtxdVwbFoLzUCT8ZsJVXu1q3fQLORQWVhFIX-4oCVMaJu1emEv2QBEPJgGRMzqYtjL1B53e4Qi19hGYbZEuCoGxVl9YjyVFfiCl39jyDyjQvJZlhcBkiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لوس بازی‌های قبل ازدواج لامین‌یامال و دوس‌دخترش که در فضای مجازی وایرال شده. فک کنید ده روزه دیگه بازی داره زیدش هم اینجوری میذاره دهنش
🙁
😔
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/Futball180TV/90551" target="_blank">📅 13:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90550">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEjC5g-VbbfK7Z27_N2dzxZQOodhGCVm7fdRLU9AoTajvWyH4JE31PAQomcaPfe78om9kN0-4MnziYiUgvtb4J24lDExOPq9en79oV41Mvtf8qy6lsBfj8yMIadwKuPR9PDi1qViT0aYbYS-1eUQC7v5oeg9SIzVjBkwJU7pzIl3hlaW-wtyHYZWT2aseoay-a0ZQ-Is2QpIu5NQf1oR5sJq1C2GAofkOID9jRMAPm5WU8zgSkUvVxi12nDkc9TeRDsJYFN7hVp_wgIDjY2fMSWn6HuXQM7IQd4nz978NPAk0ugb-fZ8dsQd5uRxQrEKDNhAb4pHZ_FACDcmm6v1WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
؛ روزنامه‌ اکیپ فرانسه مدعی شد که ناصرالخلیفی به مارکینیوش پیشنهاد داده که بعد از جام‌جهانی به تیم الدحیل قطر ملحق شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/Futball180TV/90550" target="_blank">📅 13:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90549">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHLft1j3pHXjwKpdfhFMpSzTZP4_kWNZeOquJbr4bOtuXcRuLSHib1APDrKYI2NHCsUlAAiLugX_FE--b-iTs4TfGm08Evxo1og6f8rfeIQixAZV7sFOjcomTB_QlkU3O9yHf8_ol6981REk1bnWsjI9dX5gRHcl_VDe-NOrT56NCAD5gh76gow5V1ZqBOAcmdqYId5xg_H5qL9WevzHsM2mNf_KWF6Ev69pjUvfjgBrsI5O-wKo9TVYihqgyvORBLaTc0M8z4d9fScmwzJteP37bqSL0MojEZMUoKQDTLUN5hg5wc0Lo6L1GibyHlb-KBkgyhXLs9EasioNxwZpvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخت و اقبال آقای امباپه رو مشاهده می‌کنید:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/Futball180TV/90549" target="_blank">📅 12:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90547">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11672147cd.mp4?token=gmsIOBCnrF2ip3i99B6qkuURpKjnagtfRZRjXrrvz4s4UGwdQ83ADn2qSlq8D4tMnOZSqhQMoCCefmoW8vkAV1N32UE4DaOS5cCCBaLy-xn3GWCDgZ19JTfFcDu4LD6F7mJvoHVgNrVTqQWS1jFpWaz6rmWixFCwFHaBdv2F1BJ81bEHan7VYPIzzXXBjlfvYLz0WkoAg8EbveJ-VNFSwDGGvPMWCjKIpz3gBxj5CrFanoSc66kgmSqcZvoqAJFItV8JDyslgGRIntePKDyqujsupc7dnwKQUI_yilFIVcUlyjZut6HTLaMBsknO27168yv5vVSyTXZhuNoAJnuskmWuqm72wFhKsdUy13R4kTyiSttYTZ73ez1TrR_ARfnN-5oiFLqWk77i6wGog9G5utzI-pHstQXcUxKmFYXoodfa8_Xr5QwN-Lxhh9FcHDaG02rijzEfEVXpBRmLpD7e9920MvoCKEuWaTqNqM8Tt6cuzLF6cNaZC4LWHHsBPYetdseUiJtPx2erLA7A0J8xLbC41Tt-zBMPVLP9nTXSM0j_LGugS_pGWrEADLoQ-2K9kdh1_NG5nnQuBMei68gN6o_8yj5hsXFvUqXthryRCQEsF8jENhMR1wFXvQpuREwYVcwUKbx96n8Bgs5HLMtNq8ksULGR50Zvu71O13uU6Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11672147cd.mp4?token=gmsIOBCnrF2ip3i99B6qkuURpKjnagtfRZRjXrrvz4s4UGwdQ83ADn2qSlq8D4tMnOZSqhQMoCCefmoW8vkAV1N32UE4DaOS5cCCBaLy-xn3GWCDgZ19JTfFcDu4LD6F7mJvoHVgNrVTqQWS1jFpWaz6rmWixFCwFHaBdv2F1BJ81bEHan7VYPIzzXXBjlfvYLz0WkoAg8EbveJ-VNFSwDGGvPMWCjKIpz3gBxj5CrFanoSc66kgmSqcZvoqAJFItV8JDyslgGRIntePKDyqujsupc7dnwKQUI_yilFIVcUlyjZut6HTLaMBsknO27168yv5vVSyTXZhuNoAJnuskmWuqm72wFhKsdUy13R4kTyiSttYTZ73ez1TrR_ARfnN-5oiFLqWk77i6wGog9G5utzI-pHstQXcUxKmFYXoodfa8_Xr5QwN-Lxhh9FcHDaG02rijzEfEVXpBRmLpD7e9920MvoCKEuWaTqNqM8Tt6cuzLF6cNaZC4LWHHsBPYetdseUiJtPx2erLA7A0J8xLbC41Tt-zBMPVLP9nTXSM0j_LGugS_pGWrEADLoQ-2K9kdh1_NG5nnQuBMei68gN6o_8yj5hsXFvUqXthryRCQEsF8jENhMR1wFXvQpuREwYVcwUKbx96n8Bgs5HLMtNq8ksULGR50Zvu71O13uU6Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکا اومده یه ویدیو گذاشته از اقدامات سریع در حین فینال دیشب و جمع‌آوری صحنه کنسرت قبل شروع بازی در کمتر از ۲ دقیقه
حالا این سرعت رو مقایسه کنید با پریمیرلیگ جذاب ایران که خدا میدونه همین‌رو چقدر طولش میدن تا جمع کنن
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/Futball180TV/90547" target="_blank">📅 12:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90546">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👀
لحظه دیوانه‌وار قهرمانی پاری‌سن‌ژرمن در ورزشگاه خانگی در پاریس؛ دقیقا استارت آشوب دیشب تو پاریس از همین جا بوده!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/Futball180TV/90546" target="_blank">📅 12:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90545">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GO8uqxLzCnV3FLmph8c8F8BkNVaCx2GKvYG-yZvkZdIW2pFL0lf7UClKkQ94YU6odWn1lCLJlJ2xzY9NxnhPxBkWuWQtwT8qYl2XihdAGGdTrgKOOL1-c5alM3jz2X0zoTvc0SgcuLnhbruowgbwC_dOOym8WIo1yE4NfdXOqN5h6gc2UtNiRjxEKhBaMx220LbVIc2l0tW-a7kjjx5eQlXIWxmdbaa-m7IDCF_eGIAPVGX4MF3l8dlBSIjrPQXuKl01JRg2vyfvinxVjEomP34LbyU89VDg7HV6RtXB4hjD6Hh-ZqHS83kaTDVugcN2zjsUTkNP57RQiVRQx3FrkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوپرکاپ اروپا
استون ویلا Vs پاریسن ژرمن
22 مرداد
آر‌ بی آرنا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/Futball180TV/90545" target="_blank">📅 11:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90544">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4dd57d3d9.mp4?token=USNOIbCWKDsFiq6pOFpM5789jAViSo2ePYoyRs_rMQ9Ufm2lo4V1BZMEcR4rIhr6__gft6ChAIGZZS1u4Ly5L6a7_jg4Eiv7gDqAlEQupvucReDKq5trwFxewpHIEj1Vi6IbnmiNOcA1snnUZuoz2N90ZLO-OQuoEeQYEYaJNUnLFpd0dfMl97kLP-78-I-NGtEQEatgh7KfUy3wSOiSGyXjbETkiUi-5rAoydd-htH0Vk_fG27nYYVmlVsizdxRlW1OUdoYLOnHiDtNle0le_vXVSO7h84d4vM8WQXOhqFudDTmj85s8ekma_MBYOmInDWN7bVlkR4gfZKUhfB-NIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4dd57d3d9.mp4?token=USNOIbCWKDsFiq6pOFpM5789jAViSo2ePYoyRs_rMQ9Ufm2lo4V1BZMEcR4rIhr6__gft6ChAIGZZS1u4Ly5L6a7_jg4Eiv7gDqAlEQupvucReDKq5trwFxewpHIEj1Vi6IbnmiNOcA1snnUZuoz2N90ZLO-OQuoEeQYEYaJNUnLFpd0dfMl97kLP-78-I-NGtEQEatgh7KfUy3wSOiSGyXjbETkiUi-5rAoydd-htH0Vk_fG27nYYVmlVsizdxRlW1OUdoYLOnHiDtNle0le_vXVSO7h84d4vM8WQXOhqFudDTmj85s8ekma_MBYOmInDWN7bVlkR4gfZKUhfB-NIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدیو هم تو فضای مجازی دست به دست میشه از این بلاگری که قبل خراب شدن پنالتی دیشب گابریل، میگه توپ گل نشده و پاریس قهرمان شده
😂
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/Futball180TV/90544" target="_blank">📅 11:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90543">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔵
عاشقانه‌های بازیکنان psg با زن و بچه هاشون بعد فینال دیشب:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/Futball180TV/90543" target="_blank">📅 11:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90542">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a6ea91f0b.mp4?token=ha0pvnrbVxMIQAETNkIiWPl_gwbTZt36BaRaI_EI-2d7bWKwHUnNz8xhPa5i3rupD-npWy9qa-4kXnzVRnV1QCVkJWxVqXFDPx3E_-_ysnuJ8NIzfEp-x49wMvR7UB9tIKr6JRfJkVoVW1Fp36W5j2adFTP04y2tz1HOrW15M6vTuR5uYmnGkVc3FlucugPxstI6UcjtjcQeWiq7zd0irT_jIBysB3S3sGGqFzYNznaTSbXWRJIRzeHvqICV9CRjQ08-eUXuhqFUIAXc_--kY0T6uFU7v6aUHGrFXu4-fjxTfAwDrXEFTlOvgg6ngZP9FI54NVflvngkNaU9CWjiLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a6ea91f0b.mp4?token=ha0pvnrbVxMIQAETNkIiWPl_gwbTZt36BaRaI_EI-2d7bWKwHUnNz8xhPa5i3rupD-npWy9qa-4kXnzVRnV1QCVkJWxVqXFDPx3E_-_ysnuJ8NIzfEp-x49wMvR7UB9tIKr6JRfJkVoVW1Fp36W5j2adFTP04y2tz1HOrW15M6vTuR5uYmnGkVc3FlucugPxstI6UcjtjcQeWiq7zd0irT_jIBysB3S3sGGqFzYNznaTSbXWRJIRzeHvqICV9CRjQ08-eUXuhqFUIAXc_--kY0T6uFU7v6aUHGrFXu4-fjxTfAwDrXEFTlOvgg6ngZP9FI54NVflvngkNaU9CWjiLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسانه‌های انگلیسی از این واکنش دیشب رایا وسط پنالتی‌ها پشماشون ریخته و عملا گفتن این گلر کسخل مسخل از کجا آوردید که قبل زدن ضربه شیرجه میزنه
😂
😂
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/90542" target="_blank">📅 11:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90541">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1dc755209.mp4?token=o_qWvkqM7jZNL5z0z2lSlfI4hxk2YQhrspn4H1hBwwvD_TvodlU0_DO3hFhpmFSXAkvHjQb335H9foalY6Bvkn1PinS4ylbI6ZJpSBOUiyhLmssqNzB8BHKE-fRydsaQ28j3gfguy64LydmicSHR746E93FStko6tPdzGjdhDmqFPRj46b0w-qtnxP2Wd5KLng8QuKh3ha1UbEqzh9l9o7csJL-DNPr6iksADUQBxAe5zFcQkgM_AVl3h_wArSFPo8uvaYQ6xwbz9JA8VGRNEf7PCDZjFGRC3YmQ6DAZtvfojKWSnoPCJ2yQVm_4qBV8HErUHRng5hckVX9xPCgqUjrSXUEvW4_axCvpSyB7ler8RR_IffEGpxTvBoNbLq6JrjKIFYUSIPsQ4kmcpfV_HPcAQJzSJQb9SIFbtdMWw-gP_GgFN3pQG6zJE1V27XTMQvNph1dtW4u0VQadRJg-Y1lJyvwRK1v0nZzFX2p9eYWZptAiw_Ww3Ibd_qlei_nfOdn7um_pTIkhDp0s0L4O9UQK7OMAZqNIuq60yV_cGqsDra3VUgTZd_Sz7ooKyrmxThLt9z5_lczNTBk941ohFxE8XixxJf7UlfJ8wq2KpKznPFwAUpiruigzWBiFP-KoqhzPlE1zLPMw92S9CwttejLk043-3R3vK6EB3oMDr30" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1dc755209.mp4?token=o_qWvkqM7jZNL5z0z2lSlfI4hxk2YQhrspn4H1hBwwvD_TvodlU0_DO3hFhpmFSXAkvHjQb335H9foalY6Bvkn1PinS4ylbI6ZJpSBOUiyhLmssqNzB8BHKE-fRydsaQ28j3gfguy64LydmicSHR746E93FStko6tPdzGjdhDmqFPRj46b0w-qtnxP2Wd5KLng8QuKh3ha1UbEqzh9l9o7csJL-DNPr6iksADUQBxAe5zFcQkgM_AVl3h_wArSFPo8uvaYQ6xwbz9JA8VGRNEf7PCDZjFGRC3YmQ6DAZtvfojKWSnoPCJ2yQVm_4qBV8HErUHRng5hckVX9xPCgqUjrSXUEvW4_axCvpSyB7ler8RR_IffEGpxTvBoNbLq6JrjKIFYUSIPsQ4kmcpfV_HPcAQJzSJQb9SIFbtdMWw-gP_GgFN3pQG6zJE1V27XTMQvNph1dtW4u0VQadRJg-Y1lJyvwRK1v0nZzFX2p9eYWZptAiw_Ww3Ibd_qlei_nfOdn7um_pTIkhDp0s0L4O9UQK7OMAZqNIuq60yV_cGqsDra3VUgTZd_Sz7ooKyrmxThLt9z5_lczNTBk941ohFxE8XixxJf7UlfJ8wq2KpKznPFwAUpiruigzWBiFP-KoqhzPlE1zLPMw92S9CwttejLk043-3R3vK6EB3oMDr30" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قیچی‌برگردون‌های پشم‌ریزون پریمیرلیگ در سالیان اخیر؛ واقعا هرگلش یه پوشکاشه
😮‍💨
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/Futball180TV/90541" target="_blank">📅 10:41 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90540">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a27edc87ad.mp4?token=QsDbo9hxqG6b-ef0NO_woSPNg1MNIzPWa7WCNK9tlcTtpIfm-fAMgXGqTEv8dYGlITMt6ZeOBmw85-3TDm0N3fPCHbY0ZYiKUVqVMz3B8AFpE1-iWX9IPqUmbqef6r0ohzVgq77q-iMdseYmaiv4xcLPNZz5DoCNO6IxUpNs5h6wPGpuXeSZyEEtKRjO1-4AbEhu_PkYjKcq-D7V41C3nBaFeIGh-Lqq_6uqUoCGD0r6zXgzlFn36w99W0ZzTcjv1qmD9m5BsxqjCzZoY08eIGGOaRep-jY0MvdvH0kQiDDYA-tXg1zUuKNHX0MNlaZMfMiI3MRy_Y70ggAruD_mpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a27edc87ad.mp4?token=QsDbo9hxqG6b-ef0NO_woSPNg1MNIzPWa7WCNK9tlcTtpIfm-fAMgXGqTEv8dYGlITMt6ZeOBmw85-3TDm0N3fPCHbY0ZYiKUVqVMz3B8AFpE1-iWX9IPqUmbqef6r0ohzVgq77q-iMdseYmaiv4xcLPNZz5DoCNO6IxUpNs5h6wPGpuXeSZyEEtKRjO1-4AbEhu_PkYjKcq-D7V41C3nBaFeIGh-Lqq_6uqUoCGD0r6zXgzlFn36w99W0ZzTcjv1qmD9m5BsxqjCzZoY08eIGGOaRep-jY0MvdvH0kQiDDYA-tXg1zUuKNHX0MNlaZMfMiI3MRy_Y70ggAruD_mpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضدحال عجیب و غریب به تماشاگران سر صحنه پنالتی آخر دیشب گابریل
😂
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/Futball180TV/90540" target="_blank">📅 10:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90539">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLdFWotBQldN8n_r-1kSgMmHX9MIUdivu-qWVaAlsH8F-W6hVrOFSMN3q29sGbns6k0YiKnURv2m8S8T2pjKrDER_CUnGXWKvWh1Ngcb-qlrK70ULTofUTwxC_DbaM1klg2IPYa3Pbh8wJ_FukZAPuG2ZMVmn6CKbXp6sGrlKzFThCKQOcisdXIXfN2HKDeTDUXMRobPHwaGgX0JeY0bTtsLNlsTOZLiSs3EDkZgyoc_mJax8uf0OWlwxdm4TQfQkMTdUvZT7rIJROwqzPUj7oXma_yj-GQRCrD_m7IVIIS3kothoqB63MFjP5TZNZBNU77T7U_A-Xc7QZrWMAEeDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رافائل لیائو هم این وسط اعلام کرد که دوران بازی در میلان تموم شده و تابستون جدا میشه.
مقصد احتمالی: پریمیرلیگ انگلیس
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/Futball180TV/90539" target="_blank">📅 10:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90538">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/888a4aa5cf.mp4?token=cDKDFQJBVy-n8o0wkrwxvww63UBQHLRCObDdCmQbw2OcLLPTIY6S4KvK3tzNm79gsopKQco4qrj2W4aCw6n4wTMVFyyMB-aPtGSw4QNuXxXacGJyrWz_ZysafDShMiblJOz-Ej_IlKBreX94xTqR00Yb5y6DRCjQ2sVvOEGJLocJdT8tHE3l5soe5dmQ3tmb7DId-pKWPumt5ZZNe37xHX7FkIXk749zYB0cRRbgTePTg0HPgloeQ3_fWPufSQ1lgYIQY7fM4xDvXQPXOJ_OMKA1bymsqfdNMRJPq7u1dw8C0R-MNncnkrnEQ3MAuzVmyMvesfXO1UCxJueAuMuirg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/888a4aa5cf.mp4?token=cDKDFQJBVy-n8o0wkrwxvww63UBQHLRCObDdCmQbw2OcLLPTIY6S4KvK3tzNm79gsopKQco4qrj2W4aCw6n4wTMVFyyMB-aPtGSw4QNuXxXacGJyrWz_ZysafDShMiblJOz-Ej_IlKBreX94xTqR00Yb5y6DRCjQ2sVvOEGJLocJdT8tHE3l5soe5dmQ3tmb7DId-pKWPumt5ZZNe37xHX7FkIXk749zYB0cRRbgTePTg0HPgloeQ3_fWPufSQ1lgYIQY7fM4xDvXQPXOJ_OMKA1bymsqfdNMRJPq7u1dw8C0R-MNncnkrnEQ3MAuzVmyMvesfXO1UCxJueAuMuirg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو مسابقات پایه ایران، یه گلر وقتی تیمش جلو بود اینجوری برا حریف کری میخوند که در نهایت ...
خودتون ببینید عاقبت گنده‌گوزی چی میشه
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/Futball180TV/90538" target="_blank">📅 10:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90537">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔥
برندگان جایزه پوشکاش در ده سال اخیر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/Futball180TV/90537" target="_blank">📅 09:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90536">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a192f49940.mp4?token=HG9QGwqoh9MN9-IthtStdVtObpjTJkZtb4BTwCvzVidhMTn2myRbBVB6NOakUL0AfU2bgiyzOA26Uh3HMsCvO8j-WTXO5GhvdV3fM1bMxDzNWzvK02Bwa-fHebJ1AhIjN1eJRpM5YVC3NSN79mGUHyX-_SWJklM3205ao2VVSOu4t3i5LfjRK86_2R9nRpCB6HUCI0F9bcH5Z3IwPdH-Pc0tmCd8-tF_qfnvSnMalqTMaXJVHdPuABCHV-8tuTzh4Hos9DWOj37Moj8zhecQOaI3mcw4vlcSz1LwazOPlGIzoAuW1v_VnvDETXYzfzMD4XrEV1XTY3pDJs14ydLzjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a192f49940.mp4?token=HG9QGwqoh9MN9-IthtStdVtObpjTJkZtb4BTwCvzVidhMTn2myRbBVB6NOakUL0AfU2bgiyzOA26Uh3HMsCvO8j-WTXO5GhvdV3fM1bMxDzNWzvK02Bwa-fHebJ1AhIjN1eJRpM5YVC3NSN79mGUHyX-_SWJklM3205ao2VVSOu4t3i5LfjRK86_2R9nRpCB6HUCI0F9bcH5Z3IwPdH-Pc0tmCd8-tF_qfnvSnMalqTMaXJVHdPuABCHV-8tuTzh4Hos9DWOj37Moj8zhecQOaI3mcw4vlcSz1LwazOPlGIzoAuW1v_VnvDETXYzfzMD4XrEV1XTY3pDJs14ydLzjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
چیزی که اینروزا اتلتیکو بجای آلوارز به بارسا داده:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/Futball180TV/90536" target="_blank">📅 09:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90535">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae10b6cdcd.mp4?token=FyqOBX827So63V-Tld8VCAgiPXiQKf6YfJT9PqQiLMXjhFogmGHj-1VB5pjr_ZvbhXZu-KpdnkRV_FS717UOo73TvenDhCb76MTVTuWWvJewGo1oun21Nt36CUVLw0Re-DxQT5MmdbrS3QqyPGi-QAjvvZfjqj_ToD3Vb1QZy1Fv1B4z6im_7AVnr1mQS975SmprxKnjpvlHuOMlN002fgfIy-4TAshILbrJ6a1ifmRPvEJP6qtWQqa0qudHjI6Xh9iUHtP1cEPXNRi7Dc7kensLOOt-1GxBgWF1suie3S0_pU3TIrwI7qE3oK7NrX2h9_MBOBHPnDBZl0RZttS54g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae10b6cdcd.mp4?token=FyqOBX827So63V-Tld8VCAgiPXiQKf6YfJT9PqQiLMXjhFogmGHj-1VB5pjr_ZvbhXZu-KpdnkRV_FS717UOo73TvenDhCb76MTVTuWWvJewGo1oun21Nt36CUVLw0Re-DxQT5MmdbrS3QqyPGi-QAjvvZfjqj_ToD3Vb1QZy1Fv1B4z6im_7AVnr1mQS975SmprxKnjpvlHuOMlN002fgfIy-4TAshILbrJ6a1ifmRPvEJP6qtWQqa0qudHjI6Xh9iUHtP1cEPXNRi7Dc7kensLOOt-1GxBgWF1suie3S0_pU3TIrwI7qE3oK7NrX2h9_MBOBHPnDBZl0RZttS54g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لوتی‌بازی مارکینیوش و دلداری دادن به هموطنش گابریل بعد خراب کردن پنالتی
❤️
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/Futball180TV/90535" target="_blank">📅 08:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90534">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c5c5d95ce.mp4?token=YEKNqQ7cm__zDXjoxY8lDCHe9leVfLMamswax9gs5DCzVAwGmVNjIllbf0-rG07-muG-uWOjXe9TnsXdip9DVTLFth8XRCMTD16yyuPcs8GcTdRx3VaOvG17_QjWC8Q19uNqvUfJ-_7waeGNKrtvWl4YwhndaimLuKZKMKNmrMzdg4nB7XqVRYAHwCs5cdVbaygaAWNlElY_4Hniz5paez_eNGencQ3IReCBycH7QeNe_bDcjETZ8YU0AioFRNje7o-uIgUZMjSlDssCrWORGWcF5xrsxgECrsmtlMowsC9ecSyGiTXZiOq1LaoVYrY44WCrRRFB7ochcOjiMzxAfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c5c5d95ce.mp4?token=YEKNqQ7cm__zDXjoxY8lDCHe9leVfLMamswax9gs5DCzVAwGmVNjIllbf0-rG07-muG-uWOjXe9TnsXdip9DVTLFth8XRCMTD16yyuPcs8GcTdRx3VaOvG17_QjWC8Q19uNqvUfJ-_7waeGNKrtvWl4YwhndaimLuKZKMKNmrMzdg4nB7XqVRYAHwCs5cdVbaygaAWNlElY_4Hniz5paez_eNGencQ3IReCBycH7QeNe_bDcjETZ8YU0AioFRNje7o-uIgUZMjSlDssCrWORGWcF5xrsxgECrsmtlMowsC9ecSyGiTXZiOq1LaoVYrY44WCrRRFB7ochcOjiMzxAfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاریس دو سه تا دیگه قهرمانی چمپیونزلیگ بیاره از اون شهر فقط یه خاطره میمونه
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90534" target="_blank">📅 08:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90533">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">💡
میخوای یاد بگیری چطوری با همین گوشی تو دستت از پیش بینی فوتبال سود کنی؟ سیگنال ضریب بالا و کم ریسک میخوای؟ فرصتو از دست نده همین الان عضو کانال VIP یونی بت شو
👇
➖
➖
➖
➖
➖
🎁
کسب درامد از پیش بینی فوتبال راحته اگ این کانال داشته باشی چون کارش بلده ae9: https:/…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90533" target="_blank">📅 01:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90532">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UiXklXdLj0e4THvjj_OIz_7YBNAaQ1WeV6dnf7XCI8oQ1Xk5yOaPE0HMFhaPAggzrfU6W6hTnKLGPvnPn1bmKb_wnaQX4txqlr6Mp-dAJLGPsod8x8elKwkzrloIbuBNgr4WJWiKtQmE3-betw4QC6aiPemJsgBmAsg3uCwWk1t_RMPPQvqLUBemsk4e1WfGstbliPc6SVYtXCvxSJx2_Gw1Iudytlo0gFQRRwJl5ZOcD42JmKVS7Vl4GDZ-_cI_aQFewVLWxR0xVtX2x7SyUSJ4kLSPN7RYfRs_Y4Xoyv1CrtGFtf1vh2XxZ2r01rOJ_WCICmc5ryEYZa4LMy4qdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💡
میخوای یاد بگیری چطوری با همین گوشی تو دستت از پیش بینی فوتبال سود کنی؟ سیگنال ضریب بالا و کم ریسک میخوای؟ فرصتو از دست نده همین الان عضو کانال VIP
یونی بت
شو
👇
➖
➖
➖
➖
➖
🎁
کسب درامد از پیش بینی فوتبال راحته اگ این کانال داشته باشی چون کارش بلده ae9:
https://t.me/+YwYFluMQ5-kyNmY8
https://t.me/+YwYFluMQ5-kyNmY8</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90532" target="_blank">📅 01:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90531">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbXtmMHiUwlaTyvGqyfA6oqEYU1ms7C_Dh_mB-eGZOdcIGslSD0dJ4eOOVTPj8fNxT_0DuzoBhZF2qGQ6OuvAhkXiZlrveMOWAkbRfm6bbY0GcBSgXpP2C3g5zW8ctDLWGeuCjW8AoIQCYdXqAtMQVcVlY19wxLkNfeMMivz7hd1M9kpRYndu3QL9lTkX9ls3SGuCHsmuE33pmho64sFgVT2yASvYnTAg3E37oKje2qLhjNdXz_DJbjre6P1nVuXVbMsUhoSPVS3sOjmTlv96HXZWJxLXg2q4OaJd8qHEr55_BMJQZXbrVK0d-Cgo4q1na1GK2RroKxDZYWkUkazcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
شماره 10 برزیل رسما از وینیسیوس گرفته شد و به نیمار دادن. البته قبلش توافق صورت گرفته بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90531" target="_blank">📅 00:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90530">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aac643b260.mp4?token=WFt8-KMO0UiDrleBACjmsbo_9dgygZojUN7wMXLJYHOyiD5BkIUIRSORBfHIYzlbx012lteBZQqjBDbmjmkqNyG-sH2HzQmQpysOCM0e_hfrtSc-1JHhfFj3lEcHEe-icQVVgQHfFAcWcMeQ-4Yd8oGZLlD4IWd7hPVeIiKUaBYiks1kiRt7fWbhPAprKzwdWkNAYla406bGKnnrb03CNQnP6Zu33l97Q7Z9eMaMi0-0cOsAfx30nG6mPmfPJJkNnkQ_gY3bWWJADVIxNQ4xr931x-dYP9UtOTV5MxYKV4K5uGdXm_jxoYa3lT7KMeeOzECImyX15yP3tGXM9nRlJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aac643b260.mp4?token=WFt8-KMO0UiDrleBACjmsbo_9dgygZojUN7wMXLJYHOyiD5BkIUIRSORBfHIYzlbx012lteBZQqjBDbmjmkqNyG-sH2HzQmQpysOCM0e_hfrtSc-1JHhfFj3lEcHEe-icQVVgQHfFAcWcMeQ-4Yd8oGZLlD4IWd7hPVeIiKUaBYiks1kiRt7fWbhPAprKzwdWkNAYla406bGKnnrb03CNQnP6Zu33l97Q7Z9eMaMi0-0cOsAfx30nG6mPmfPJJkNnkQ_gY3bWWJADVIxNQ4xr931x-dYP9UtOTV5MxYKV4K5uGdXm_jxoYa3lT7KMeeOzECImyX15yP3tGXM9nRlJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت جام‌جهانی نصف شب با گزارش سرهنگ:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90530" target="_blank">📅 00:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90529">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEooXv4bGZQk6VC8ADlhm1mMNPsCmG9pKxrV5wBvcZKGD-zpTYElK6WOwcWNv3N5yDNMm0zcnAfG29KjviX8KUfITBrEJBOzbhIpM7Z6R-O_AMmFyz51twMeUb9_RYzty7EW-YNP7wyp4Pru-Tqhwr6-jAvABSZK0Dfio87zHKJW2LLRsjnTayVm10sa4Bw2ZFSX8SJGpSNU4YBcLJRbUoHNObsJrsaVJhasTeZcOxiY3QgYppDsqBz2NugSAtySf51E29JqosakMxwsLYrQ6M9TRzye9a8FEF41mSqmY_u_VoieXcPEww78nSUtGY9ErSWxtA6Zxb9EoMw8CSLY6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امباپه با 15 گل زده آقای گل این فصل چمپیونزلیگ شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90529" target="_blank">📅 00:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90528">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00937b1a6d.mp4?token=ZQWBkTb6eASFItgI4q9oThS5iFcSh2xWNgfHwmNEx3sQgkRwyb_s4avY8rzlt9b5dQT3wPwZWuQuSSqwlhn35koS9N1NdBYCE9LZ2czYCfAHl-q8ElO4vu4bEKFrE1s0CBNxOKnGXSIcG-ugDOq71Y85_fFwwicP66gQHoPEZTZNFD0Ybn6rVg5OXg1qI7iEPmOG78uWv13hNDJKYLhmGgasI4YnhqBBlbE_CWerbhYgMAiB8AogPyeHw3RJTkr5Y4jQWKLsD4yNRB2UNKCmYg6FcsT5prlViF6cRQYdtnfx1d8pGSHYtIcW2ZK42oQ0Spr6Ym_NlcRSptBc6WdFag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00937b1a6d.mp4?token=ZQWBkTb6eASFItgI4q9oThS5iFcSh2xWNgfHwmNEx3sQgkRwyb_s4avY8rzlt9b5dQT3wPwZWuQuSSqwlhn35koS9N1NdBYCE9LZ2czYCfAHl-q8ElO4vu4bEKFrE1s0CBNxOKnGXSIcG-ugDOq71Y85_fFwwicP66gQHoPEZTZNFD0Ybn6rVg5OXg1qI7iEPmOG78uWv13hNDJKYLhmGgasI4YnhqBBlbE_CWerbhYgMAiB8AogPyeHw3RJTkr5Y4jQWKLsD4yNRB2UNKCmYg6FcsT5prlViF6cRQYdtnfx1d8pGSHYtIcW2ZK42oQ0Spr6Ym_NlcRSptBc6WdFag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادل گزارش امشبش رو به این شکل شروع کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90528" target="_blank">📅 00:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90527">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEFF6tiFu00JTRKSY0w5Z7_isn02kpNQTEq6tyof-Hd3tqeKELBnx9QbsOqwQXXh6Vjg5kfGs7CJPaEaLYLQAtffBhKF21UNTVO85d1CLNVNOo3o2vTA-cNomcfw4EmEnQJicYR-LzDxMgEWo4HSLSNwSJ1NI8Q41Enaur-lvXlAIuFfPpVKocjAfExXgXuJee9yRHiU2MZOQs8EszTE__pYszfETHQYM96cnjl1dbJ7W4c1QYfnuukwp4tgDNSZ9_QIE8FjKifCRXOXHBTgU2wxLIlEK75Mcqc6iL4oPRMQHshyzgA3ov50EHxzLfXGg0_SPOl1_9tx_bb8qooXYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست کریستال پالاس برای ترول آرسنال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90527" target="_blank">📅 00:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90525">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qz7Bfe45kBsvH0QRnb5Hu4anpCBu6l1uROrqoulN-asZYRtYr_WOLXoWM9WDwm7KElkg3PxADiZvjj1vuB9B1Qs7Cc6hXvL5XBXkwivRcvFrAe4TgyLoZw71QttQ-qalTYjZDtixvSHPKL9_M3y4Khtg8W-V-37M02KS4Llkmpgs967q70zWsRngl5f3D-U1EphjngnYOo1zGaeHLHIOSHEZ_KssNOKzHLHEldJxTisSeflQ6EoSH7ha9EiGsp1m2ksrGq6sHxXX5-r6uYm7qOySvAMbr-cpC0LFHgnvV8EC0Mo6f_hg_PcakZfUvBDzh85fKcSI1FiTR8XRxkZWCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکل آرتتا:
می‌خواهم به پاریس سن ژرمن تبریک بگویم، به ویژه لوئیس انریکه. آنها بهترین تیم جهان هستند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90525" target="_blank">📅 23:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90524">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDUKIyR4akDESRIa4Jn7stYsyejDS55iqPEW3s9slEZgHN5ouR6uQT1NGc-xGcvVGQ6dJAl0PKAhKna3dAjJQ06TfoSSpIaRCoUHyoxFESYeTFCWL2oA8-0keV4CWJ3of-BQFOVItALEYxJLgU5rPlnprbnGvtYo6Ol3WTrQwjmjI_S6LFqbBwjARP18PyrTaM9cM2ZlUyvuKuRYpBAZtl2VvI2L_PaZSHpzQEhM_xupUcnqgd6YQM5xUGYqr3rNR9gMLiNPEWi1HSyJw_OWwIn0u33yf7qSokeDQZz4nB1rza9cuX_GlEFEvReUtN6mk1MOOZIxC4hdEofMczXuRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید چلسی بعد از باخت آرسنال : به لندن بیاید و از این جام بازدید کنید
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/90524" target="_blank">📅 23:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90518">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LUKwGwyUay_TNZYUh5SwDB7frAlAEP0cfnbmiUxSHwaIb1InBg3P1BREMVH1-gBIwXisMccLb-o_YxxsNLtKbznKoDJnPPlJGtMcc1PzdMaBWQbg017vsQlr5pAiLHZrWL0T3BloFYV_JON7gU7gyMHUlPOCVMb7XKa0y7xhTHQElZoZIQb2JlP8KmubS2LEJFnStVkaYzdI-HzfZK4n7vydcVRuw7CJ1qDT_DoQU-b-_BYy0nc7bu3veagk5KX7QEL5mCzj6lfYO7r6nnP7TDGYo1NmUXKMns9aRD-atJM63kzsx-CVwJi20fkb12deuWTVfljZo0L4JUFewjIE_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cxW1SyfsabYk9C239zdHP5rT7--fdaMP8P4SpmvB9uPk35R08S8onrGl7pmd-qEnvW5RNVXcImwC39nKb77fixKHaXgplq0Ni1k4xkKvGZqM_ueKxvEQdJm3aHyojaUjoCq8Tc3Kpxt09BQ7NIWeMVVr3nbEbN3GcCNe36hCqzDmHZBjMOkfw2bnUi3iBXk1Cnm3TaenV17bgo7qk_9D9Pp-25LoQ5mlemLq0QH6CJkQ0y7joh28SZhQHN9jTfMS2JnptomMr2C1D0IxnS8BlizVzzEwD9avntEXl6Q61shOgnNdgi2Ln2LIj5RYKuiEqPeNfiiTcuAo5RdSbCkLpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QF0gRPgZ3_iGY62BU2NtVtRhzT-EsoJdLrDOWuSfhpDs8A77_IUUbuEXLjh5gwsnu_VTJo38kveqDvb61FvOJog3heJuv2IbhUyRYuzSEBGWZTiQbdvGMHaZWXRBUVJHbWMXN5LsdvaC9DEXWgs1Nqzxdkc3IdJqrF8OspoabljGygDLJN2bX_gr8SebNprW1w41cZVK9490DW8PDYUWj1c1hIuZZW8eSCVwxPb0HBwZRsGHyJqwkxWTs_WYQg2Yw4-034E60oKomY_gz_FabXN4RsFwsyHfHKam5959TEhRSYlWsEjInIotz6Pws_uq6tI-EiJ6MVuWGDIMI8Nhzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VScfe9IOJw_3zPjSedJjb0bwJMv_qs5m9CewOlshfM8GAHY1oWUGIINhUduXJEt93-CzkJSXEJTlOtdplnuRcV8_4LzO-GAIGRzAsMDeLNjSiDKSZht8-rIVAHwCil_dqVxk44EOFbG6JXjXBply6EOeYclkno0gHUgm4UKZ0XeWjSIYA19eMT5EBTb7MjPwxLUVt4GGCKXhL1YavwHh-Ucsakqqx_CP5GpxnqMNQxO62kMtnf9GBSzi0KgI56SrH06Byn_HEDKO11vC14AvNAYNNpKM0YEn0eFYnYY_ojMOO8BmTzbtk3bPqoPv8_aHqfHcheGwsUBZoIJ-CY_vRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vzZVn9UCo6BFVKN1yx5YzUVfK8AdXbh9aKnstKxrrvTWeaBYFJvYLO1kTAeKa3fwPZ2W8sl-AsaaWGQ5GzuiSkSSDji7HuO0V1DhbhNtZ1_lSGPbjm8tt5XYpKwV4LwAuohNxjohxR-TrZOn4s2ojXGYW_XcREGzKihw0WBpfELQbfCL2FjEpZusKqPCMi4tF-weD6kFGONKSsztTrYnu_XMUCWly6EkAgWCLon5qA6ucUW60IsmoOWf6CCFnw5_jtRkd1YRVOP_1cPFowDuMXnFZlmhUNxTeaF2tfsVSj-x4Ttbm3wMafnKTrfOddARd9-LqHuhI1gttR4Mn2uHNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oQuH2_ub59R146xfuGdKC-FlabE90m-H4NFA-_mF3Lsp9YPY3gYCQUmvjTKTKMi27DFfCmg9KaI3K4bLYO8TTiUW251LC-XamfsEcTYjsvdFyCDseD-IIiO1wEw7oMcpKjeDz8MX1n7jq8fsqSk5f2ursbFQSU1jhChVHq84XbgZ7SDn_983pSX11YGBBUVaXVSJMwcCAWLVjmqYFGico67s0mw9S-cYzGwNprfQos9oyIfq7pVv4mIS8WTlQeizjsjmypvo6Xn0Ts9qVzfB23DAUUQZwqw31F5uPrw6BS9Rq__vOUUxz7QIH3FHehw49f8ey3WXTtKVWsxA83tNEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری از جشن قهرمانی پاریسی ها پس از دبل قهرمانی در اروپا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90518" target="_blank">📅 23:08 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90517">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">عجیب ولی باور نکردنی!
امباپه دو سال بعد از ترک پاریس: 0 جام
پاریس بعد از ترک امباپه: ۲ چمپ(بماند باقی جام ها!!)
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90517" target="_blank">📅 22:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90516">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/elthntzkPkCnSkCqR1dKc3njDAhPO6h5074f5wnbcUfJKr4fv_KWWmRGb76c49tB8O6j5Yxd_0Tyk8Ys4HinUELOHBtJ89LSzJ5sWWQRFofbRubsDmDsIZ7lUiVIgg4o5-XPVIbo2EyYVyPMaEjq1h9s335w9SiyYi3t7ITGHDipgB8gOQTxU_2rN2nnuH5w-5dHb__qIm8aHS-Rz_WuCbMWgJQ6PGgaimP_xUf2mCLQQCN18jH8xMBhU6A2krvHAlaeGaUYj_ZKiZIdh11AXoVJeNZzxTCZgFgnPxhZ07qynwcvwgZ7f6I22GBFNPgJNRCU-duKztnb1DIrmYCUqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
آلمان
🇩🇪
-
🇫🇮
فنلاند
🏆
رقابت‌های دوستانه بین المللی
🌍
⏰
یکشنبه ساعت ۲۲:۱۵
🏟
ورزشگاه میوا آرنا
🎲
با بیش از ۳۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
آلمان در
۱۰
دیدار اخیر خود،
هفت
بازی را برده و در
سه
دیدار شکست خورده است.
✅
فنلاند در
۱۰
دیدار اخیر خود،
چهار
برد و
یک
تساوی کسب کرده و در
پنج
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر آلمان
۳.۶
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر فنلاند
۲.۶
گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از
۲.۵
- ضریب :
۱.۳۰
🧠
قبل از ورود، بدترین سناریو را مرور کنید.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90516" target="_blank">📅 22:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90515">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">پاریس دومین سی ال متوالی رو کسب کرد و باز آرسنال ناکام در کسب قهرمانی سی ال
🔥
🔥
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90515" target="_blank">📅 22:31 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90514">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">تمامممممممممم</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90514" target="_blank">📅 22:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90513">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">گابریلللل زد بیرونننننن</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90513" target="_blank">📅 22:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90512">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">زد بیرونننن</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90512" target="_blank">📅 22:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90511">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اگه آرسنال نزنه تمومه</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90511" target="_blank">📅 22:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90510">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گلگلگل برالدو هم زد</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90510" target="_blank">📅 22:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90509">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">گلگلگل مارتینلییی</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90509" target="_blank">📅 22:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90508">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">عجیبه صداسیما تاخیری نداره</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90508" target="_blank">📅 22:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90507">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گلگلگلگل حکیمی هم زد</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90507" target="_blank">📅 22:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90506">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">گلگلگل رایس زددد</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90506" target="_blank">📅 22:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90505">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">رایا پنالتی نونو مندز رو گرفتتتت</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90505" target="_blank">📅 22:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90504">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">رایا گرفتتتتت</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90504" target="_blank">📅 22:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90503">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ازه زد بیروننننن</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90503" target="_blank">📅 22:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90502">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دوئه گلگل</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90502" target="_blank">📅 22:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90501">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">گیوکرش هم گلش کرد</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90501" target="_blank">📅 22:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90500">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">راموس اولی رو گل کرد</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90500" target="_blank">📅 22:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90499">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">بازی آرسنال پاریس به ضربات پنالتی رفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90499" target="_blank">📅 22:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90498">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">امروز خبر اومد چشمی جام جهانی رو بدلیل مصدومیت از دست داد ولی چشمی امروز در تمرینات تیم ملی شرکت کرد!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/90498" target="_blank">📅 22:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90497">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
⚽️
⚽️
⚽️
اخبار داغ حواشی فوتبالی و تحلیل‌های لحظه‌ای جام جهانی را از این کانال دنبال کنید
👀
اگه می‌خوای جا نمونی، همین الان بیا داخل�،
👇
👇
👇
👇
👇
👇
👇
https://t.me/+5NhkIyyAtBhmMzM1
https://t.me/+5NhkIyyAtBhmMzM1
https://t.me/+5NhkIyyAtBhmMzM1
✨
اخبار داغ  و کانال معتبر
👌
👆
👆</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/Futball180TV/90497" target="_blank">📅 22:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90496">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDBl6DlbbQbn_Az4IZ9ZeQw5V5RFPb1GKH__xybD1kRRqdwh_wuz4UPPC73lJ_1iJUKPzgX4PmnicEv9rzb3m6oNgpmZZ9aTeowkqu7V5e-CPhGyCaslcjfbjv1rz0vyY7ucpXAG_EOeYZQbNLgbYvxXYDOlOta4fj0K-rYlBWsTANQhkVGV0i0qVLG9J4Lum_69vHkMMPBqYbJ28JiZZdpCd9aiTjZGnj1jGDspHlxxhi87OejEFTSY3iXodSS6NxUCdfsGBMXPgzhfb27KJbNmb7-O2Ety5d4mMP6VuMyTYmkgr3EmfI2tihQgpw3aLOfmZ9stHw81wGrTNzJ6aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری جدید یاسر آسانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/Futball180TV/90496" target="_blank">📅 21:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90495">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">موقعیت های مشکوک به پنالتی جذاب تر از خود بازی بوده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/Futball180TV/90495" target="_blank">📅 21:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90494">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">پایان ۹۰ دقیقه
پاریس ۱_۱ آرسنال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90494" target="_blank">📅 21:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90493">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/375a1431bc.mp4?token=iTY9Sogl_0tof0S3nJRoMf0KrHT106Kb4UZAgMqUffRdD2StAalgQi3DT42uMTiHwjz6qKf-n_g_qRXd6ozmWf01GycHgrdrDzmn9YPbZq1IOuGAmfC0S0il59x-isexkYbv_lEhwlFDGUNnkyRHahAkSQ-_oZSuOORsLfGqtyCrcA_v4JNPWjvw-AKAId0K8HIp9fbE1in61uwnSA-_61lJSwyZxLTp0to2DO6AgUzbmjiOORTqC-T9IQK1iNOPPXon9TaRe--JdhbrcafpVkyqtuEHsM1c4NQu-xX-CQuPIlD3ZL0hG1wjpHuL0YHZX1JoCgtBmZUq29slP83yVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/375a1431bc.mp4?token=iTY9Sogl_0tof0S3nJRoMf0KrHT106Kb4UZAgMqUffRdD2StAalgQi3DT42uMTiHwjz6qKf-n_g_qRXd6ozmWf01GycHgrdrDzmn9YPbZq1IOuGAmfC0S0il59x-isexkYbv_lEhwlFDGUNnkyRHahAkSQ-_oZSuOORsLfGqtyCrcA_v4JNPWjvw-AKAId0K8HIp9fbE1in61uwnSA-_61lJSwyZxLTp0to2DO6AgUzbmjiOORTqC-T9IQK1iNOPPXon9TaRe--JdhbrcafpVkyqtuEHsM1c4NQu-xX-CQuPIlD3ZL0hG1wjpHuL0YHZX1JoCgtBmZUq29slP83yVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
گل‌اول پاری‌سن‌ژرمن به آرسنال توسط دمبله
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90493" target="_blank">📅 21:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90492">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">گلگللگگلگل برای پاریس توسط دمبله از روی نقطه پنالتییی</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/Futball180TV/90492" target="_blank">📅 20:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90491">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پایان نیمه اول| آرسنال 1_0 پاریس
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/Futball180TV/90491" target="_blank">📅 20:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90490">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">چییی خراب کرد پاریسسسس</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/Futball180TV/90490" target="_blank">📅 20:14 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90489">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUasNkCQ3ylPLvciHyl2fIysWFzy5BcWFFae9WS5NPwT27mR8p2r1YKoBn6Ap09CF26_WWHaVhCha2rpEfI24DJ6wqnGJ-oXE9xfYye4sOvUlvorpvyk95FdrxCtPec1gMxrS5OKV3_ETlYE9ies_Hwcdq5_-Hm0iHEWX2-L-fV7h8fZOLewKki4aOUqsHmyaRH6tk9Dwgc8W4TpydlEKDLm2lreHT8ofj3TS-Zy9HYqd1iAjFGc5PwnIfirBmWUJni4r0xqdOZPxxEE6rTPOAiEVaKUykB5UEQehDdsyYt0wx26TamsPUTA5k7aq2zgrzToHbPG54q00t-HEEUahw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرنه اسلوت گزینه اصلی مربیگری میلان در فصل آینده است!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90489" target="_blank">📅 20:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90488">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3cUgwcSXGvtuIKyVFDDYHCW4k2s4omur_ZvDo59Q8x_Aev12NolF7xMO7JAKN76cHDb6zPdWl0Ym4GE0N731xq4BGhlUaGcd6-7U8-_pjC3VAUb7UtyTdAvrnTliJOimPQu5xeaGpPcvsAJawuyoH0IiYqEuJWT4bopKXBXu1YYvlhBfI68NwRkQANL8ftbzzfFGtblySUpwjaG5FHiS8LjwSKfxFcu3ZFoh_cAIld0vH6s83mJVo73c3f8aNlkbO0qVEUZDdmX3nw4NN9F9MLruvIqVKg7lEKhs0hu6BmqaFVMmnoepY_nfgvdrg2kzSueoR_4Br11agn9xUNskw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنالتی پاریس گرفته نشد!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/Futball180TV/90488" target="_blank">📅 19:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90487">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/Futball180TV/90487" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
#اپلیکیشن
اندروید سایت جهانی دربی بت
👍
اسپانسر لیگ انگلیس
👍
🔥
امکان شارژ امن از طریق کارت بانکی
➖
➖
➖
➖
➖
➖
➖
➖
➖
🪙
همین حالا عضو شوید
👇
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/Futball180TV/90487" target="_blank">📅 19:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90486">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXS35DSv9CpqdmybJ7iwWcDwsxubUoe7HXDsVcc904sT_rmksYFIGAt-KbrQJ5galR8dDlxul6u3xZEc2Pc8N5Ay7FbVrflxZa-0BnAZ_8wP090ALftXuMbNZP6V0qc4dTxVMVzqqbXp-XctB6cTgM2HMacPDkfREraBxXZR-0gblsYOgdgXiie15_SUaJgEec3RvkFS5S9v2cMGuTT8a8OoycfSqTXEduuD3sJU64UN2Avw6EiGu5oUZCCxD43iGjiVkBfdb14zas2KORmLG5IP6GAkf6_9hzIj1448stntnwV8lQAFN9OD1vIva2lENVPvLDxD36z1zWLBSxqriA.jpg" alt="photo" loading="lazy"/></div>
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
⚠
️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت G9:
🪙
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/Futball180TV/90486" target="_blank">📅 19:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90485">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbgwSm7Iz6Sb1C5gXJDMy-duIzbWtQdV5qdpDZ7UnFFfumXB42PkogAcupMClO_4ePFUZbjvHDXSBAV6U5n8KAQIuOIXhhjoGSwlKUpKGHMPpPQ7jp7v5PZ49zNCdeeRwjo7liMCMBYw3fGnlFdbWiXR8AcgstHsmPMXWoWoq1R2SjPZKf4-79uPPZ83ukix_g4CEUpDalu5lhkhJm40IXb2KMUBaNrFX65W7pLZjHEgEZjmRf-qewIlWpcczJgWiBJ7JZwec3gdpbMpa-MQgoBMnD4HHRIpjFDL1j-L_9Yupm4ha03yhYXlx3p-DLjk-G3I9Xa1abfFSqYl-5qBrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنالتی پاریس گرفته نشد!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/Futball180TV/90485" target="_blank">📅 19:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90484">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/71e697023e.mp4?token=THaGBLdO4FQXQALZzfa3VdVBq3ET3ZfVtle1ZaUYZXrF0SNZ8ODlmfIKvUxgRsypdvE_e_1M5iX-1Tkt1O76rB9xeiiAbWS7vAQk6Sjc5NvNO9Vdcg2JnpgIJlO3TimQ2xAONhHwg_09O5MZlcrl_q8hXG82UugoThvyrPArtcX5tH4KoTpTYYgIJZawWzMWQs5lFdY9bkGocmpVKsYRCamj94l9dtv4HmMkrTU4xtrYK7fnnSAAXP7ZHkY1Bh5-JnE9sFmOnf5vkmrdey8gwnsp3IJpon3lsFIiVZndMcnCaF-LNdmc7xekQmCIfiKttbF86NOmgr-TSjt7Arj8EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/71e697023e.mp4?token=THaGBLdO4FQXQALZzfa3VdVBq3ET3ZfVtle1ZaUYZXrF0SNZ8ODlmfIKvUxgRsypdvE_e_1M5iX-1Tkt1O76rB9xeiiAbWS7vAQk6Sjc5NvNO9Vdcg2JnpgIJlO3TimQ2xAONhHwg_09O5MZlcrl_q8hXG82UugoThvyrPArtcX5tH4KoTpTYYgIJZawWzMWQs5lFdY9bkGocmpVKsYRCamj94l9dtv4HmMkrTU4xtrYK7fnnSAAXP7ZHkY1Bh5-JnE9sFmOnf5vkmrdey8gwnsp3IJpon3lsFIiVZndMcnCaF-LNdmc7xekQmCIfiKttbF86NOmgr-TSjt7Arj8EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول آرسنال به پاری‌سن‌ژرمن توسط هاورتز
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/Futball180TV/90484" target="_blank">📅 19:40 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90483">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">سوپرررررررگلللللل کای هاورتززززززززز
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/Futball180TV/90483" target="_blank">📅 19:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90482">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">آرسنااااااللللللل
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/Futball180TV/90482" target="_blank">📅 19:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90481">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">گلگلگللگگلگلگلگلگلگل اوپوپوپوووللللل</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/Futball180TV/90481" target="_blank">📅 19:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90480">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWlypJLxL4CuMupH4QyL-B53ocARSqnpoP-Bguj-0ftZVBOTgPLhE6LkeTUkS_YS7F-JKaghXtvp63mI1VSaduNJfUbODahJvHFkU47fJgcJq67fsSeeXj0_pi1ZakuIG1zUjvwJEo7cWBPK_1oDk5VabnU5noj9ZAlIF3PRGsKPInVVldDjHz3ftj4x0QfGdxJKuLXPCkbtfHt470kfYLpWHpry1GbD-MDYdJfzbAcP_0-uzMzb2GBCTANTmCc7TZwFFbBPovtkVxMjI4SS3SKiaqIR5GsX27jsAV45XtNb0ho4mbLLl2VVw8LO9lAM2Q8nFHRvuMBJohVkI3_MRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تتوی یک هوادار آرسنالی از پیشبینیش از بازی امشب سی ال!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90480" target="_blank">📅 19:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90478">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P3HSXa8MELatoZ97A43oUyq65ddnuqoa43-XRS0z428FF-N_PMyWzRSP7WqEOQdYuTJz8_te54JpfPUSCVm3OUGeOV5n2D86YEE142ccTqpvv1e4zo7QQuhFFH94JYaD3Zux1VwFtyXdn9iAV4_05uaF2tAEQGvo499bRERjvgrg2heKZ6Aldhwq8ZTJV7guizhGDoaot-NtEa_xS-RnQom9-rfoSh_PT4bNzUUaPGw3ub0VudT0OMm7cAGsk00BcvAZTHzVPYloMrsrBw3BHxoHj1dUpKfBWqmgZg2goB48WnhhaXE3d2KbtLQ3BdDpeldkN1pw1yXpRAo2qMWDJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z55MBrAl8ZENkoGgVwvOPC64I4YyYKI0Nkg2B7b_dL6JKQ-5le6oZZQk6k6FmV9vBqID5SrByiNotGZhKcogd_rQr0HL_5Y0Hx5pSgvp2tEzs8JBKcQycuo--fHf7nCPA5PBO52ddN4CM549tLDe2YfvAEAG6Gh_aDrtUWV6qhhs9su3UiaZyJ5XbLj0YBaqzNgoIhX_X6QlbgtIVaYdrCo3qRSZ_P5W0P-eIvym7xizcKE8S0lfru-mqrJEJ8qcEhe__5Wm5W4i42Q3xfOLP5snJxgYZOaoywGXRhwOxcACYFVTh97VbcJDrTVdDDRV16Vwkc9gEUSK7DLFIG_FLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسکواد دو فینالیست ج.ج قبلی و مدعی های ج.ج امسال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90478" target="_blank">📅 18:20 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90476">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wv7Zx8sraaUsmVeHbujkZr1YYxqRUC3hCDa_nzRQDB7-Q2dSR4jqvMzwwpO981PJOAHJuNjMm4tQL1R85eCgqQZ2unC-R-vYxfgZsgRbOy4nD-0UOlDpOXuUcG-ch8lbsohtaAYSdGYaYMBhdWMhpBRPt0Z7PGTEBz7WCZ2tOpZO6E7HoHHvViV0hrzsQdy-k_rcLksx8O9xAtYqRX6-vdxRoAoAr7zEajmVksuzMN2ZOpPIEALAL5V6BSs1YQxmtyTNkAMu7YwOX-d77igGpP0e4avIurH4t0YWYGfryiqWO9e1q2kJBMQd7fG3NRCQ4Ii12O-V61o9U60WDxOqLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aVirYTXLFxRHtEZW_0b8U0--43CjDaKCeM3oQeF57ERAmqpB5VevqmhsR88y7stk9zbp8k52eKWK6Az2BTcSjM61ztt0oBX4fT8k0snqvqCTeaj2c_qwVh8hYrnSajMcirNNkcSO2u1CWW5UD6NJGqwJOQMqFUZ5BN1ALu4HUh2ASZc4GfD_nyfTReDrC63hatjO2x56j-DE5l8lJsdmPa-ADjkftL-knHM42Fz715L7h56MQcqiqjzXE98DUHfGodYjN0n63Wvg4a3BDAEd4734p1T8sdDlkCBBVEvtERjDu6enwlDJtdKLaR0kWsnOpj8d4fMGW1jq94bgIYbJ1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
ترکیب دوتیم پاریس و آرسنال برای فیناللل
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90476" target="_blank">📅 18:14 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90475">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
❌
🇪🇺
با اعلام دبیرکل فدراسیون فوتبال، لیگ‌برتر رسما به پایان رسید و نمایندگان ایران در آسیا مطابق جدول فعلی معرفی خواهند شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90475" target="_blank">📅 17:47 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90474">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TsrKrsNA1vwMUeUrvJadevLKpyV6IeFa79I-Fv-yp3Ql9anNj6j3JRmP_bioXDWifpuuxUn5MF_r6qlHciThnejBZCDz88o1nqIwNmm7652vYT_YrW5_HcFOuYYwxIrbDF2wIj9GEd8mm8Olzgf8ZU8V50wqgZ58sTwgTcnn-Ohr5X_PtOznjzutCexIki1n_invie1vLdr7tdnjuSX4rnUJ_KPPUv0TlK5v7J2qAeAAkrwtZcmFDZqKFx7m8YKrVHj9-Pj2XiWjftKlVO9hoi1zNLzg7EzVrX-lUJVtlhNsp6bpDsyT7a-gYJTTvMLL5gO19ZINYW-v6so-hqF40Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشتک
#FreeJulian
ترند شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90474" target="_blank">📅 17:47 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90473">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZSzS5Npy9LkVsBnjVlhPCR7BqcWklr1anqhINr-la2CIiTnZ8Qm-9bnwpxLVeKAsJpT1Pdu1dTjZSvM-R5VCzC7iAkNuThud_CYBei4P_sd0BDtgkQUsfwMVsf0YLFDfpk8MINPYb6jSM7mi43XMl3uBkIFcstNjCHmArOynquNnt1aXBG6mzPzRJqBIaWbyzYpO9hQ2UnpiQUoCM0VQotvV2l64GdtyoQnC2ZmjssKrkVdpKgUIjoaAMjeREAsZSUY6oUxIF6FLpzYAgxVZJKoWI2w5flS8Lt6pc6lKsRGgl3O5xww0wadK0BW8H2gFAVulTz2qkvh72ZQCuPRSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
کوپه :
بارسلونا درحال مذاکره برای خرید گواردیول است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90473" target="_blank">📅 17:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90472">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46a77e89da.mp4?token=Z-s5NullBCD6g1kHYAYZsXxjx7U6_v_u1fVcwvrQ7YpmMF4ayW-n_6oY3gbe-Ws4NRuC0BVqpJqACQb8K7GxIyeHxKu6mhtKVfKC4vS16GQRKPMhI9PpGAWK_2TNxYVR0NDJcMZqMBKShZC-8lNIMOv273-9HPBUTWSlHlfv3bNG4mDdFLQH2nvNZwmzvkSOfgRImzzDl3e-7alQKVmufzUfrSRLSWxi7K-qnK0l0ZzI7uWQgG5vYW4xk4uZbSk9CapAYRhGY-z2BjN_7p1oiTxZcxy1K8ShIGcFaKZ6aaTu-kwBuuIV2K7nOVXN-OnRZfdzsHVoqCyKV-YjdKp4WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46a77e89da.mp4?token=Z-s5NullBCD6g1kHYAYZsXxjx7U6_v_u1fVcwvrQ7YpmMF4ayW-n_6oY3gbe-Ws4NRuC0BVqpJqACQb8K7GxIyeHxKu6mhtKVfKC4vS16GQRKPMhI9PpGAWK_2TNxYVR0NDJcMZqMBKShZC-8lNIMOv273-9HPBUTWSlHlfv3bNG4mDdFLQH2nvNZwmzvkSOfgRImzzDl3e-7alQKVmufzUfrSRLSWxi7K-qnK0l0ZzI7uWQgG5vYW4xk4uZbSk9CapAYRhGY-z2BjN_7p1oiTxZcxy1K8ShIGcFaKZ6aaTu-kwBuuIV2K7nOVXN-OnRZfdzsHVoqCyKV-YjdKp4WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای اینکه بدونید دعوای بارسلونا و اتلتیکو سر آلوارز دقیقا بخاطر چیه فقط این ویدیو رو ببینید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90472" target="_blank">📅 16:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90471">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pX0SfhTaLWsBmueoXV16SlaZc5Aiog8leImkK849HjZlXB6wvu3G9fmjE7a6Bj_Yz39FGZI58Oj2KspadzgBkRLPDMSLVhgliTMBDM7xuEYZZ2FKXIcM3vTw5Uku8_bHSRJA24egrXgWoFQps-QhInZybewtfjWF2V3JfPEpFq8wsrIkR2jM9Dq6l0yy34lovQOOuUc4Dt6xwc3oqukQj_wfpjL30DWvIT_9HPNfkAj-0ydz1bYJk6R7mxWsf9SaB3l3LLAucizf10M6TRg5IxZO0OBreP4pW7lRbUWCNTnKWJujsjSAteDAWLD51fR5-Hc4DarN58Dy4zbGsLa5nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تمامی افتخارات ملی لیونل‌مسی در آرژانتین
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90471" target="_blank">📅 16:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90470">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9c775485a.mp4?token=ERVJwI3vamaYXIVbtZhBPwdkdQcroAxp3731rDNORf6OZXf06AgRGu_Mgm7kEUe7hcEGq3gCQ0Tv8YWUXcK50b7iFuWBDTMsNR_igREAdUjWQE2ZZnz61OaSegObCL3F5u--B-EIBETh2L02dKZ6pfbJh3Po41wSf6cpS-FZt1fFHC3yxt6U_UbZtyXw_6Z3T5O2PIo09gvSZHSLAfmG_DApPc0R-TYQphSvLaDl7Nl-O8x8FfSZjImK08A-0iYuTfAx78a60tiMXm5Qs9owos9y5ksdqsCkom6n-PW85yWg-DFTLYo_uSuEOI9_N3hIyaUJ05Gmpn5pyqmJCQw2cH4S8ZE33KJg7LVAR23kDfOo6cOwyl9RwSCrGuCw07AilB97xfJFtoUtiIHWGFFV7pA_E1HFDT1GhszWWtEgbX_-H0b-P-odPPBlejMohZZ0Ye8CN4TUElzXAF53Cmmy9QrvjNzwFhY-ePryiTbihPd7QNJpC8cDgZrPmgNpyrXGO1-JAGICKsPy_IxufDVJNOEAlxHEqUO9Lyyb8QcUbpHENqddQ8Tpj3d7knBtUwoXGlQo5bwOLtHcg_1t1VUM2crXM-heNt1MO-mYhVH0GaMhmw7-Nq6bcjnQz8oS_isL1fyp1DqPYThlVROC6Q8j7PQfyJ3Mly7setzfR8pKwjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9c775485a.mp4?token=ERVJwI3vamaYXIVbtZhBPwdkdQcroAxp3731rDNORf6OZXf06AgRGu_Mgm7kEUe7hcEGq3gCQ0Tv8YWUXcK50b7iFuWBDTMsNR_igREAdUjWQE2ZZnz61OaSegObCL3F5u--B-EIBETh2L02dKZ6pfbJh3Po41wSf6cpS-FZt1fFHC3yxt6U_UbZtyXw_6Z3T5O2PIo09gvSZHSLAfmG_DApPc0R-TYQphSvLaDl7Nl-O8x8FfSZjImK08A-0iYuTfAx78a60tiMXm5Qs9owos9y5ksdqsCkom6n-PW85yWg-DFTLYo_uSuEOI9_N3hIyaUJ05Gmpn5pyqmJCQw2cH4S8ZE33KJg7LVAR23kDfOo6cOwyl9RwSCrGuCw07AilB97xfJFtoUtiIHWGFFV7pA_E1HFDT1GhszWWtEgbX_-H0b-P-odPPBlejMohZZ0Ye8CN4TUElzXAF53Cmmy9QrvjNzwFhY-ePryiTbihPd7QNJpC8cDgZrPmgNpyrXGO1-JAGICKsPy_IxufDVJNOEAlxHEqUO9Lyyb8QcUbpHENqddQ8Tpj3d7knBtUwoXGlQo5bwOLtHcg_1t1VUM2crXM-heNt1MO-mYhVH0GaMhmw7-Nq6bcjnQz8oS_isL1fyp1DqPYThlVROC6Q8j7PQfyJ3Mly7setzfR8pKwjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
همسر پورحیدری: روز عروسی من و منصور، داریوش زندان بود، ستار برای ما خواند!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90470" target="_blank">📅 16:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90469">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09651a8d65.mp4?token=YVJHeAZLrT0TIdK1_Eymps-PU1yTWnyrECnbnyD0Dqlox_gvc3DsHkx_9dY5rklGLi9SSCWFah45dKrbKhLQ6bErSe6O8Jop55IVAJC_Om-Ny5IO1muIZwqNkTzprg1aUohZr0AE9hzbyIl-kj6zf_7zV8dptkhmC3fe7VfU1BZ9jiXWqGOWlqwu1pLFXextpn7s44xdGy9gSVhI2IbJYDOyqnAd65SR1vtsgeRob0d6UbMVjynuaxH775Jz0CFVxTUyX0IphkcNKrGH1i9YsAu1a2YvIaFkEZuChYu4giYTbCXcyeGaEylhhzbK4dzff_t1eUToNwuBTV6vc1BscQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09651a8d65.mp4?token=YVJHeAZLrT0TIdK1_Eymps-PU1yTWnyrECnbnyD0Dqlox_gvc3DsHkx_9dY5rklGLi9SSCWFah45dKrbKhLQ6bErSe6O8Jop55IVAJC_Om-Ny5IO1muIZwqNkTzprg1aUohZr0AE9hzbyIl-kj6zf_7zV8dptkhmC3fe7VfU1BZ9jiXWqGOWlqwu1pLFXextpn7s44xdGy9gSVhI2IbJYDOyqnAd65SR1vtsgeRob0d6UbMVjynuaxH775Jz0CFVxTUyX0IphkcNKrGH1i9YsAu1a2YvIaFkEZuChYu4giYTbCXcyeGaEylhhzbK4dzff_t1eUToNwuBTV6vc1BscQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
و تا ساعاتی دیگر، فینال جذاب و نفس‌گیر لیگ‌قهرمانان اروپا به میزبانی مجارستان
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90469" target="_blank">📅 15:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90468">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بهترین‌گل‌های فصل‌گذشته پریمیرلیگ انگلیس
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90468" target="_blank">📅 15:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90467">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ با اعلام‌رومانو، آرنه‌اسلوت از هدایت تیم‌فوتبال لیورپول اخراج شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90467" target="_blank">📅 14:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90466">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mv2INFBwkPP5mCZm3EyY87h06dba7MS6mbSLhAcUwWk5L0LaXchmpz99xnsCuzxuU-jctXaCan3fZ_6xC5s6rCmFUH1hkIHKkgauSHLe-tDQtKGDq05szQCImRWewdMmxmORbDWws_rfEcqN9LVN2Ip3dPpf-EIFrdN6Dpopa623D7VJsnXGlPwle720pXzcxyqvdb33SmLRB7MHxDqag214Vb2iT2u6Ot6IvJRwcBiNG5B1-rqc__X2AWIw2B7Qjs90ryMpnNDZ20-2rIA-rj3V-8a3QyMObCxJzTkHlBYvSOAoH_wJWc9yz7-lO6F-WNd90AIPFrriBRx7a1JTDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ با اعلام‌رومانو، آرنه‌اسلوت از هدایت تیم‌فوتبال لیورپول اخراج شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90466" target="_blank">📅 14:47 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90465">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQSPPmqnyiiyblh2mZOFJLVScSp72lVD2B8agHutz1Z3URbMgsDmYObZ2PVggyEar9XW20KM655Y0b0zVNCQ1GZVtGWiNz1YolcXtIRvX1dv0ATdLI-yOu-07Ul7E7AoAVh5sc04SToFNCJuKJ_rNCapOPKspYSF-durEvaMwxogsswPfpdAbB_88XYZGnpP3Ov8zRVkfnMT3gBLeq3TejV1-e7pHxzpA8eMxxRVUJY4w6pareNqlH8QpTCiXfvGYbLr-KpBjG4P0lsO3QCCdh6bxmFNyP_Cy0IdORmHMvkVfMrI0aZ86j8ChJzmxs0kjgtFS00yYWQcZq6HYI1Dsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری
؛ با اعلام‌رومانو، آرنه‌اسلوت از هدایت تیم‌فوتبال لیورپول اخراج شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/Futball180TV/90465" target="_blank">📅 14:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90463">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nf58uPssm4I796ZH-NbNmzEdadR3QVa90ASJgF8fgAJCq0qIgglrdjvCegRY0TG48ap7g0YzmDwR8dgvmqYRh80O8WAVYCYXYpDCb3XDTRSbqAKl3d8_5O1ZI8kmfvnpE3hGS-2KFvFgs0hot2xdB16v4Mj9-uhUIY3F-HJRQRLA0GGJ-BaWDx9K7kK934WAP6PqNg5Q-LTxQOHoxTV0f_MxM-tGfgJFLjuZ3H8hkF0DydzbakbKzY6dRdOz1354Kbxn0bbgPEsuIhgrlqje7WASkkMTwWSAmHDUFkdXk8lYAMbLvwyCQwbqbb5X_SS5K3QzMQkCZ5HQIhUfVXvI_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cF_rRamSeYBN6GzH7lDQyI05PDLUMr0Hw_ULD8NGaen-mWwm_15nPWqi25mLKB7Kg0EQlR0rvCkCVhDVuRuL0cvOp9qnt2oSWvxuuvHDCJNthV8F5DyNe97bj1Ue63CnbXdrSHzANAN1yyAfJa-63fvorp7TORuKo-mJJAAYd5yjtxWKfU4nNZTdkwxe3_SpKQZW-BXkJ_Wh7KMCz2M7rMcvtvRrLLblxB3EpszNujNCKs4Z_5QGuFGZXFuMGNEgjdxckPjDaCUe5rUoR-luX2kJM_JUoDcyYjWHU58U55_y61bbssalzwNH1I_q3OAlPv7VIrRDJ7WzwDRvhV7QKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
ترکیب احتمالی پاری‌سن‌ژرمن و آرسنال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90463" target="_blank">📅 14:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90462">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0ec9fa176.mp4?token=YWiO6JKl7PWOu_kDA5aYw5T--WsuOYy1EDuKAaT1ji6MBKGVCd8Bw1fegqT3h-xsrpI0coA_qZaiiK1QVl12VQxgc7gjpxRaKC4azAYKSGvOCtmjL3WHON_0z1ipehiJp7b5rAe-QyF4hQP-tS3S2b4_RGIA38iIO4oJdQG0kqGoiaXVMqXxynUI_7mU_JEjEi3QW3UR59C3tJdhOSzW-OnyQTm3RjvPpvEr2g2yIcgJI_OGqNZq-l8q5dHikxiIK-cy1eaGyXmIRTAvEjw7n5w1DKTYhHs-TfqUvlxWO7SBBz3fre48-3o93be19KdV0iA1RxgoX3whXB48Xa5sH5eecrvcHu7e9Dxcha2ENTQX_AhHTEzarNCerEE7Vnpo1m_82-pGsuEEA6dygawfSbz8pDZq3u8cuvvrE1VZQ1IP5czd3KfFt_5X5eXS7ZVxX-yNFYELMmy7DbKxGVrCoMZ9LHKPvkquxHOoeVyGBz5mI6TuruKDkVC2Qsflvn8ymrBd66zPkJNTYD2WDKGxhl-Cxf1rk7WpYA2XhBB06D4L7MMyoQ9uS-3eBTVwjn8L-zR1rM7Ueo2lMwGxHYYlvamo0_qZhGdRSuNqpUHAgYHWurvCXCsiddTav6Ji0tRfjNeXDs9zTR8szrJegZ3MskSFAMItIdnh_QxsEiSSMvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0ec9fa176.mp4?token=YWiO6JKl7PWOu_kDA5aYw5T--WsuOYy1EDuKAaT1ji6MBKGVCd8Bw1fegqT3h-xsrpI0coA_qZaiiK1QVl12VQxgc7gjpxRaKC4azAYKSGvOCtmjL3WHON_0z1ipehiJp7b5rAe-QyF4hQP-tS3S2b4_RGIA38iIO4oJdQG0kqGoiaXVMqXxynUI_7mU_JEjEi3QW3UR59C3tJdhOSzW-OnyQTm3RjvPpvEr2g2yIcgJI_OGqNZq-l8q5dHikxiIK-cy1eaGyXmIRTAvEjw7n5w1DKTYhHs-TfqUvlxWO7SBBz3fre48-3o93be19KdV0iA1RxgoX3whXB48Xa5sH5eecrvcHu7e9Dxcha2ENTQX_AhHTEzarNCerEE7Vnpo1m_82-pGsuEEA6dygawfSbz8pDZq3u8cuvvrE1VZQ1IP5czd3KfFt_5X5eXS7ZVxX-yNFYELMmy7DbKxGVrCoMZ9LHKPvkquxHOoeVyGBz5mI6TuruKDkVC2Qsflvn8ymrBd66zPkJNTYD2WDKGxhl-Cxf1rk7WpYA2XhBB06D4L7MMyoQ9uS-3eBTVwjn8L-zR1rM7Ueo2lMwGxHYYlvamo0_qZhGdRSuNqpUHAgYHWurvCXCsiddTav6Ji0tRfjNeXDs9zTR8szrJegZ3MskSFAMItIdnh_QxsEiSSMvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
به چالش كشيدن اردلان آشتيانى از حميد استيلى تا مچ پايى كه در دوران فوتبالش شكست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90462" target="_blank">📅 14:33 · 09 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
