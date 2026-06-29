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
<img src="https://cdn5.telesco.pe/file/Uo1KV1i3JQ99jogJx65kuC8P7tIK5U3iCG10r0xX-QB0oaC7QHtPQ6zw6THi-ra7gZIlEKFDK7DsbD1YJGzlcd64BZPVzNqNuzZkO44OdYSyZyKn-cbC0bBjUb4tUIBRiob9r411c-AsYJ_bQpQ5dbEr0ygtLULoAYPAz7EHxCKqCqc-mkQmRLx-h0A9Aa4EoQoTYnZsKnXU71WiygkawXfwTpFF5tZJ6zc9GRk42XJWpuFSkrGrYBnVaLU6w566eGPKZpi3KcFsuWa0XkTJULeAZF55dUU5fcFakpdlU8cgdV-8GvzDy-kxo1JdMadfCduQJgXvGoLvd7CrFPctOA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 683K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 02:04:32</div>
<hr>

<div class="tg-post" id="msg-96923">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🏆
پایان بازی در وقت قانونی
🇩🇪
آلمان
😃
-
😃
پاراگوئه
🇵🇾
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 610 · <a href="https://t.me/Futball180TV/96923" target="_blank">📅 02:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96922">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🏆
پایان بازی در وقت قانونی
🇩🇪
آلمان
😃
-
😃
پاراگوئه
🇵🇾
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/Futball180TV/96922" target="_blank">📅 01:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96921">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">▶️
🏆
🇧🇷
🇯🇵
خلاصه‌بازی جذاب امشب دو تیم ژاپن و برزیل با صدای عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/Futball180TV/96921" target="_blank">📅 01:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96920">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">همچنان بازی آلمان و پاراگوئه در دقایق پایانی بازی مساوی دنبال میشه</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/Futball180TV/96920" target="_blank">📅 01:49 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96918">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BC3LXf6WvdPBQ_EspYT62980KiTAzDPpHbXucVQ2PdDs-zDDW7s3Xjb_8KqZhZZ84p0Dat4uHtgZN-q8KoFEDgudh4AViXDg3tkUipR1Pi-IOcgmjJvn5SiQ2Oa4DM9J1tjwsZmIv3mXM3VKr-CeaqeAcjs9_S5F0OCfS502GwbKUFx_51_U6TDzBfSiCDyGE6Qrt2T70ukrgWScBWOnEk46wAVmHQiPNbFbDL3BecW6HBbQsmhAJx7K9ew7fM90FiRJQYLWWC6Ximh5bo9G-wKuCRRqUyx9WgGnqYPH6YPWtwcMJa2lJUZw0U96pzsJw-8FK2lwQcLfUANZnQxdnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/knomW7aIKk9p4KL4jj--Zr23AmxUQT2ocaXeNsapBZXufB2V1vqlIbX46LUv5unIwPcSwzLym0pws45jpnJ8BUJzEkjeR4boxB9FdPon6hnifyo0sCs9qijIm9iKIGC00xVjIP__mriJNE28Fi8YjQ7Pmi87cVRjvUILHWAPpqTPg5rMVQ90OUgN7FYy8Q1rK1iBmEEpzon2-YjbdASeCRD-UXI9ryyYNHYn57-04SqAx3Vz2F9Eja3Q_Wlsy1LuFZEVJ5DbKWZV5B0fJrLNYFSmXgSkGka5THoQVz1-dXAAZzMcnVhPVg4MqA7H9jDiu2B7Tj4Sc7-qgJ7JBJ8CKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
👀
🏆
یه پیج‌خارجی ۲۴ ساعت پیش اومده مسابقات مرحله‌یک‌شانزدهم رو پیش‌بینی کرده که دوتا بازی قبلی درست در اومده و گفته آلمان هم امشب دو به یک برنده میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/Futball180TV/96918" target="_blank">📅 01:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96917">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">پشمام چیو آلمان نزد</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/Futball180TV/96917" target="_blank">📅 01:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96916">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">آلمان زددد</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/Futball180TV/96916" target="_blank">📅 01:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96915">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/Futball180TV/96915" target="_blank">📅 01:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96914">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUK1FYD9TZJUmqwillT1M2bDbJ7n7513CXm7unmWCNTgZXIL99OjT7b4Ks85u_rflJRpImj7QJc4oYT9zkNveS3upJPb7-3zj-aY7DNdSLy7kVE3u0W2MgY8WoWo1LFoNAOkdXyOHqE2OhbHVF1eSDMRJzmyMUveq7KLPWcsUS_yeBnyD14RH0RoiTuio6o62hz5cDFBPpKoQgDOEdZbPPLHVMAH36-3-haLCRH9IcZeUBQ7lyJCYcDplJlRzSMwiI_f7prEgrnkMPrZSaGDJM1Q03gtdI_aTEvfT4GgmrTUcxNzkgieEfTEM2kuDH_dCQZBoMP2yYONBXR8Qg7vaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نویر تو 10 بازی متوالی برای آلمان تو جام جهانی نتونسته کلیین شیت کنه!</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/96914" target="_blank">📅 00:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96913">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaqmwbtfvMjwN0wnMZ08vqRDbVvYJWtigc_eeXePvGWRWKH6VHY4WzQcUtFtNRcisQBbCMzgcK9Td7LXcpXiLUzr9qBu_hfnkziuzMVfabvvSNtZB6_n0dLzSBusQ7yzDEdsJ3D5ppv-i8AjhrTDcWbq1GfryqIX9YwCNUAe5i679MMDP8Z_qYbd5pWg4aWeTVrhPDYRSdhBS1bw-FtIGr5aeP1N1K81poBvaYrN5WnCQqCN8LxbUlYdh2z7g2XTvsTUKAZxK11YUB-fy8ZrqUozRYStElj6gv0UUFnxgj-PxcM7HYAnvq53FbgYwhyxAkm8oKK9STbFo2F_DokkoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون آنچلوتی قدیمی برگشته..
🍸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/96913" target="_blank">📅 00:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96912">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6aO-lE1MmOGCodTRx3R9s-LdJ_PyJFnaIFVuLaIadReBqwHDmPGqtfQxiv3q9sakbYP8O9kxBJLRPvP_J2t_v26GuoA2TQbY9Z8oICdttLWqqXGgPH_xUU8BKKXovpHG6WphUq_vcMbofPRlu1Vmok2OWAjrqmb9eatzNWi9fy1yxRhrKsj0YpxnNrTDfUc3Y2KMSktB9cj_cT64At1gqE8aZvWj6QzyqhX-qPlEhpMq0n1ymrAWMvvHpIbqO0YIuWNXrZL5wnSDQ7747mR251iJm3GAz3A9vdaw_FjmEOVgJgbgV70HhMkpwfLblk7nHmCRitp-Ya7_vYAQ0DFUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/Futball180TV/96912" target="_blank">📅 00:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96911">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">آلمان با این بازی کیریش بعیده کامبک بزنه</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/Futball180TV/96911" target="_blank">📅 00:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96910">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پایان نیمه اول
پاراگوئه 1 - آلمان 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/96910" target="_blank">📅 00:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96909">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97406f3448.mp4?token=al2c1xvQNzR8_0sTVtTUG0SoQ1HsAw4_NuOTj1F0uGiIpWc_zHMoJZhC1x4C7eDnBke540t5fDQD9PxG5IUfyFT4rJtAwMW3IL-IMHGLjYUMCak1Oyt_GkL_OBP7skdDZ08b46cw6C8kbf7xb01_2mr9Q8QJ1bV-u_oAMpiU3aFBlAUNFCatV-llqU_DpZzgTHVYKRXSIGhLBTvPTCUAlTgyVgGtVdrZB15cV0c7y0t2fFpD_yEg3C-VfdP1Oldgu08t1FV6Iv8h4LX0lHxyUXEOSrCjQ9OKVHfOszb3uODkCXCrukZfhzuvBqKgAvqOd0n0YGdPUgtUPJvUznPFDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97406f3448.mp4?token=al2c1xvQNzR8_0sTVtTUG0SoQ1HsAw4_NuOTj1F0uGiIpWc_zHMoJZhC1x4C7eDnBke540t5fDQD9PxG5IUfyFT4rJtAwMW3IL-IMHGLjYUMCak1Oyt_GkL_OBP7skdDZ08b46cw6C8kbf7xb01_2mr9Q8QJ1bV-u_oAMpiU3aFBlAUNFCatV-llqU_DpZzgTHVYKRXSIGhLBTvPTCUAlTgyVgGtVdrZB15cV0c7y0t2fFpD_yEg3C-VfdP1Oldgu08t1FV6Iv8h4LX0lHxyUXEOSrCjQ9OKVHfOszb3uODkCXCrukZfhzuvBqKgAvqOd0n0YGdPUgtUPJvUznPFDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گلللل پاراگوئه به آلمان
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/96909" target="_blank">📅 00:49 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96908">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">نویر تو 10 بازی متوالی برای آلمان تو جام جهانی نتونسته کلیین شیت کنه!</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/96908" target="_blank">📅 00:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96907">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">این آلمان چرا اینقدر لوزر شده</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/96907" target="_blank">📅 00:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96906">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">پاراگوئه زددددد</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/96906" target="_blank">📅 00:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96905">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">گلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/96905" target="_blank">📅 00:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96904">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">پاراگوئه زد
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/96904" target="_blank">📅 00:42 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
