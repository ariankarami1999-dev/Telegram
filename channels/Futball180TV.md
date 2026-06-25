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
<img src="https://cdn5.telesco.pe/file/sP7IuOnoEyfCSWWMsQho6qEvmTbDcEeMrfmZwXgQJSs_rOi7UgDa6MgtI-aqFPlMFcmOIVdyjf7EFfVJMZ3H_-xSkjEwIoNpoqKSL-ccuWUSSNnJgfitez3v1K4RP0XOKB4qMmwn1wTJak6wrMXzcBpNrgC6sNKky-9kY5b4qKVwqKm09TNFCziG9xpaF27MhLZKcwd--1UOqBTeMawzoZ4l9p0d1hT8_wjBb3JExjY0UvIsyR6AD9TG1NDWLBovrR0N1jtcH_mDAI_wpR4WgykxR7Fiqu1RU1DsxC8aguQi-Xw35qMf2dlioaFqt7uNEny0ITcsuDVvvWMe5SWbHg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 701K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 19:28:13</div>
<hr>

<div class="tg-post" id="msg-95865">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHEm2fdyKifcuAZt1vNqD0pBh79oUaPCADGjD3F6R3rLwdvscpXlqmW2iYbCPdN1Dz6Q7iWyjFf4sb9lCdBkelQsV1FokdeP7FHJIWIBlT8TuvLaZPsEWbvXnaFRCquuex6f0m4OuuUDFZtbYqWyKbF7eg8QQAubXpBB7XGA8x7BjFWvnEBapc4INzIqSPkq7zJol-f7njjj5HniAbffFedVQ5_QGZGNUuJSv4XTJgPFk2m_QqvN-QnWDjmHiapLMCdQVbTRMFGcMFNAGS6nP_5oaQZHXPTGal9wXbSUugZvTgIKTOV87aqLhl2Ml0QWhtSd8DSpUcaPF9enB9aVew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
خبرنگار: «میم‌های توییتری خودت با اندریک رو دیدی؟»
🇧🇷
آنچلوتی: «بله، خیلی خنده‌دار است»
🎙
خبرنگار: «خب پس اندریک در ترکیب اصلی خواهد بود؟»
🇧🇷
آنچلوتی: «کی؟»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/Futball180TV/95865" target="_blank">📅 19:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95864">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50eb40e5b1.mp4?token=SjZy_00U1ZsGR_5oqcbNBBn5Fw3fySCSoiiFkSdiDyw8YYeW5lCYgKIFgMPsbzHR1c29DMXVQhpC7NuZd2v7J8WFTLXyxDHo2qU5bhUQtlhWwejwGMFdBgPUwIK6iRI4TXjw38--w1dAxBmdpbUvHRd6saDyyg7AETQZPueap8jIhy0RMj2G9QVG3-8phmsy2wT8SlpZr5PAY6J20FCoIHgvjlZAuXS330bjpPZzE0zvh1nip6Y57OBunkV50qdqejFxt00ivtnwT0niaj-MLJEpfBIsh7WPD0APETyFdkwuTbS9OKyg78s1xGDT40zIJTE3pTi9-eToOPEZISSmIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50eb40e5b1.mp4?token=SjZy_00U1ZsGR_5oqcbNBBn5Fw3fySCSoiiFkSdiDyw8YYeW5lCYgKIFgMPsbzHR1c29DMXVQhpC7NuZd2v7J8WFTLXyxDHo2qU5bhUQtlhWwejwGMFdBgPUwIK6iRI4TXjw38--w1dAxBmdpbUvHRd6saDyyg7AETQZPueap8jIhy0RMj2G9QVG3-8phmsy2wT8SlpZr5PAY6J20FCoIHgvjlZAuXS330bjpPZzE0zvh1nip6Y57OBunkV50qdqejFxt00ivtnwT0niaj-MLJEpfBIsh7WPD0APETyFdkwuTbS9OKyg78s1xGDT40zIJTE3pTi9-eToOPEZISSmIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لاشیا رو ببین نعمت خدا رو چجوری حیف و میل میکنن
😢
😢
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/Futball180TV/95864" target="_blank">📅 18:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95863">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTGFNfrMyj8Ft821oLW4NJ_3C3EQBsXRiJeXwn8mCMVLgmiIsZK5uS8bR9rw7pCpvaZbsO2yr1_0bx28s8z7Qhr3Abksuf1n1q3JRhGYaYM3GUd0hvlfT1vqIIgqNMX6osBQ6X1dSu3c9vicMl7uUhUnENGmKJPzfaJoriJrsXhWMICKTFrDrIPvsZyOkOFOdRNikY3pTkw4b-70WzlquQngWJFlLgNTlZ4OEiAPTs2M_Xq3mlQza65eoXf5_Taiog09lGiEQ7zow7xlEAFNSFi0MuTYfaHAVjbgiRP2pCsc1Lkw2GQp-hKp1NPhcnYLzHpjNUb6iPGoMcqNg6iD0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
🔵
فوری از رومانو:
رئال مادرید بند بازخرید ۹ میلیون یورویی نیکو پاز رو فعال کرد و او به باشگاه برمیگرده. کومو تا دوشنبه فرصت داره با ۶۰ میلیون یورو او رو دائمی کنه، در غیر این صورت نیکو دوباره به رئال برمیگرده و وارد بازار نقل‌وانتقالات میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/Futball180TV/95863" target="_blank">📅 18:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95861">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nbBMvDABdciw9EWnZ7Ol7aVgNbmL0kTnXK3-KzRoGl4RSunu_6Cnq6P-iLgkCoVVt0_fnnqrWe1QpRAgDD_queIrQ78N1eMwJgIH94Z-tL-8yQ1Tndp_39ElZLgZeKh2AACvV3D4wCuOS0M7cntgBmv24mjYUQincSsRlNfFb-8y0KbyeC7nH1CB9iTOmWsxJIyqTNkpTmIM7QQec9FfW_jD-yI5Y6HSH1BaqOo7gAz0wJ0waUcskdU-8QqBNnufP_DxfYLOjH-i2n4ATh6WpxC_8hb10VsjlINLoHyIQg4pv-kQA4Q40IvZbibHSmurKsT1XAl7c6kRfSmY_2bVKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hmroZanE3ZfDElKtOxJbR5cCKH910EwLy9rWHjd3trdZ2Zcucr0dmabxcOOwHZkgIxLHDEa7we9xOsAX6lhf5iN07pfQiT-j8Rk5B4lvkY11nWF0Un9FAr8h0fTiR06ZBqCtmDNMm5krVdhBHsTmA829hiJ2XA3WxTjBzZX9dUZmrAU0cl4wthxWYNwdBcaOe4yaTfpiGdNikiIuuV3UHuZ5u4YjiKvGyzXYkU-lmNbb60C3bLjcCIRz_SJK4UuDJ0cMcylFJt4NEL-65vO1pD-XN8upyfo4kxPG2gQKHwbaIKurMkzBKhguBvhZOR8Niw3ZNLlSVO4M36r6vmfIPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نانا کواکو بونسام (جادوگر غنایی) : من، کواکو بونسام، قدرتمندترین جادوگر جهان هستم. هری کین را شکست دادم. دیشب بازی او را دیدید؟ او حتی توپ را هم ندید. چه برسد به اینکه بخواهد گل بزند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/Futball180TV/95861" target="_blank">📅 18:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95860">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d86caa5adc.mp4?token=a3x39tkFm97jcTtXmeyjHFtwaAOzereXK0BH6rqoKtk7LYpIpjLfVynFI7ZjaLGm4dYjR9YWZlq2__dWBwM7_9FU37pQdcl8FX8X2eFKUKO6XkUOSix6MvauHYYEdJRs_A0abVvAN4tZcIYbGtf1Nv3hnWPM9xE0-2SrEQwqF2QONhTMho3XJc5YglRF5r4a4GAcvdHSsercMVgNhBkJw8iPhnBuQI_qxZTbzbXKxqIkCpaQ1VIWcbaDIMRPES19ZVTSjS7dwU_JNLuphoITwyU-FspS06MNURmses687DJJ7s2c9BJdZBMh09JMjkMKfPRvJBlHAfeo-XkfH-DWFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d86caa5adc.mp4?token=a3x39tkFm97jcTtXmeyjHFtwaAOzereXK0BH6rqoKtk7LYpIpjLfVynFI7ZjaLGm4dYjR9YWZlq2__dWBwM7_9FU37pQdcl8FX8X2eFKUKO6XkUOSix6MvauHYYEdJRs_A0abVvAN4tZcIYbGtf1Nv3hnWPM9xE0-2SrEQwqF2QONhTMho3XJc5YglRF5r4a4GAcvdHSsercMVgNhBkJw8iPhnBuQI_qxZTbzbXKxqIkCpaQ1VIWcbaDIMRPES19ZVTSjS7dwU_JNLuphoITwyU-FspS06MNURmses687DJJ7s2c9BJdZBMh09JMjkMKfPRvJBlHAfeo-XkfH-DWFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کل‌کل دیشب هوادار هائیتی و مراکش
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/Futball180TV/95860" target="_blank">📅 18:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95859">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e9810d64f.mp4?token=sa2G9n6-94s6oOv0uihvkRnNUXILR1HAhUP4LjUCPNCdS3R_SZzRaj6iz5_mVObml3XjadDcsK70lktq4UWKvnTHi3t7B4UvJxdbghIjfVE4vxAo8_FeTmAlLXQU3ZbGaFERdp0hA034_eEsqmyoMsCaGFKVi_pPeD7_sc4B_IF8jAqyOsFI3n6zzqbPpuOhpUmwOBQDp-E32wirDQrMmY3F6OTFZqz4JsFNkRExzcHqmJssW675VtYrolnhX4w52BW-UteViqvsKAjraaByJ8narZ6-TEUkPWLjn-8Aslmks9NENwuJLjwaDowY_msxN9tLg71D6HYKxmptzOlLfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e9810d64f.mp4?token=sa2G9n6-94s6oOv0uihvkRnNUXILR1HAhUP4LjUCPNCdS3R_SZzRaj6iz5_mVObml3XjadDcsK70lktq4UWKvnTHi3t7B4UvJxdbghIjfVE4vxAo8_FeTmAlLXQU3ZbGaFERdp0hA034_eEsqmyoMsCaGFKVi_pPeD7_sc4B_IF8jAqyOsFI3n6zzqbPpuOhpUmwOBQDp-E32wirDQrMmY3F6OTFZqz4JsFNkRExzcHqmJssW675VtYrolnhX4w52BW-UteViqvsKAjraaByJ8narZ6-TEUkPWLjn-8Aslmks9NENwuJLjwaDowY_msxN9tLg71D6HYKxmptzOlLfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
عادی‌ترین هوادار تیم‌ملی غنا در جام‌جهانی
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/95859" target="_blank">📅 18:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95858">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUUwSc0bFVb9Ix2pB1hEQztC4doHMhKRzgFZQHIYcbrskR0iZPIoqS3hkjvStOk_XtjUzGniJt6oYsQOLLQ6IcnKWp330rIq-mjLv0s5z8fe0dXPJ8P6mO-XaiQQsYhbraMriwaocX7ucGyXnjsLI7d0Zpnarp3ryH7ZCIqpdDbLe1k8pKdI0EQ-XY3zFC4uEoDykZBd6OOW3WzcqpK6Fuv-OsondDNat_29tQTJuVucOdW5auycWDahrRJ1GPsk1pSDZevwDZ6hAX1pnIr4KRUMvg-tA9uqfpyKZ8d3GKGpOamlEF7-GaTQ5eaz2zKvFu_GmXdrZ92zNhM6tFtOiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید رونالدو به همراه بانو جورجینا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/95858" target="_blank">📅 17:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95857">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yp1E4zN8Isr1eZMSYoaNv_cXzseT_kjsansw1P6K86QqPe8SgbR-ViN8m4M5rfA5JPYqz0oqLjXPA_Pn-lcMrYxDtktjqjXf66LRymZAIpeNDtf6ValAcmb38wE0JyXce3J8SDmjyxwaXH0MR850y64HFlw8jqPvXhcCpVHdHOqD0fdpbemfdZtDw3xn2zGIK6gPjcu7IYKGXGvp13vlPmFRqH6MUDia93BOpa9qdy5VnybpTdPTg0JOK7MZ76yy4MRBdUIeP4uqaAfJTrS0wrFpzFrT2NXMtv2SWxgv1NgkekCd7nRKSnCTxVjzy5legqg1tcXwC2v2QQtwcziRXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تبریک تولد مسی توسط اینفانتینو:
تولدت مبارک لیونل، تو با استعدادت مردم دنیا رو عاشق فوتبال کردی، ممنونیم برای همه چیز؛ امیدوارم در جام جهانی هم موفق باشی و همچنان الهام‌بخش میلیون‌ها نفر بمونی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/95857" target="_blank">📅 17:44 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95856">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQrT7PmfWkWDzdXBXbFl_Ze6wNpb7MkBmveKu-S8OVXKzvLWstGLw4Y3hznp31u2YLhvIsHE72hTIjsCDNHbIt6IhRM2uyL-ghKJVl3awEeDA_pumV92W48eYK8RcKBZ6Fg4wjT-twTgOMsPfW00g1s9UPKh1wbXb4-7hlw6rpN86KP5f6LFpMc_1hSx_kWvyse1XAMK9dgBgMwylg5R-oBpu9_-wDMcfFHMdp8w26QxcMEZ-_drqPJpLJyd7HHgDkmLZTkRRBLWDF3F_OOeyJ7YWStwOI5SJc-OfEi0SgCy6i4BtpaU4YhMQ7jP7IBNoMp3iysbG9SKTtCROTF-dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بیلد آلمان:
لایپزیگ پیشنهاد 116 میلیون یورویی لیورپول برای جذب یان دیوماند را رد کرد!‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/95856" target="_blank">📅 17:43 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95855">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/904edba416.mp4?token=Ip2ZNZMKRQvJB-bnfjEKfC_6FiBP8MSOF9wJd7a11ivh0n8FrQ-ku45c40MfgIlZSCG5Zd_jWwXE7oEWLJ-QKQ8wAG1UYqN9BdJzqkVPcPceDcS-6Wq7xwCwJNarH4DHkD3Wus3NDlG3cdEulvIPgxr_KI8rZKdV6m5trDD-CLGXy6CMX8BhJMFd1TJ4jUpIz2QmP4QkJgNJuK3S15qdD3OuPVZiSdRJbqgg2UF53ULrn9vDIp4aB7WEDfosZIrPwO5es-wpERltzW-uuCHEO7cbFj8XFehKsFSGWdG7TuFDFvnFSeO9YIcc8z7TFJ1SGPiNISqec9fUJE1xkkR3Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/904edba416.mp4?token=Ip2ZNZMKRQvJB-bnfjEKfC_6FiBP8MSOF9wJd7a11ivh0n8FrQ-ku45c40MfgIlZSCG5Zd_jWwXE7oEWLJ-QKQ8wAG1UYqN9BdJzqkVPcPceDcS-6Wq7xwCwJNarH4DHkD3Wus3NDlG3cdEulvIPgxr_KI8rZKdV6m5trDD-CLGXy6CMX8BhJMFd1TJ4jUpIz2QmP4QkJgNJuK3S15qdD3OuPVZiSdRJbqgg2UF53ULrn9vDIp4aB7WEDfosZIrPwO5es-wpERltzW-uuCHEO7cbFj8XFehKsFSGWdG7TuFDFvnFSeO9YIcc8z7TFJ1SGPiNISqec9fUJE1xkkR3Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
▶️
نیمار و دختر خوشگلش‌ تو بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/95855" target="_blank">📅 17:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95854">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDb2luhPpunZRaNPn8-KLmp2xAMhnmoSGFKhYOXJcaq-Lv1CnWddZQcl0UUROhZbrmJJs7gzGuxNRHI_UC7Tqo8HEzNxrkms1GLlHTJ3X-vTtWox-ij-VjgsI-erJemZq3lmd5II9FNqPnOpBPaUG9go3EVdhJVPzCMW3V7d9Az6GNmoKoZGkEXEH47rEF5COyhRuNvxaSqfYLseG1EXCpF8CPkv19af8EqLQUvww6c8FQOLIYQmiu2D7Lnw0IxQ1dYOTxXRyVWOg65QcXTvfa_BwoOSFRgz5nG9ikoC-ojlizfLZmnz6Ax56ywj8YGZd5Yerelo4HlNl6YkV3CTLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇨🇼
کوراسائو روش متفاوتی رو در پیش گرفت. برخلاف بیشتر تیم‌ها که بازیکنا رو تو طول تورنمنت تنها نگه میدارن، کوراسائو خانواده رو در اولویت گذاشته و اجازه داده بازیکنا کنار همسر و خانواده‌شون تو یه اتاق باشن. حتی فدراسیون هزینه جابه‌جایی خانواده‌ها رو هم داده تا کنار تیم بمونن؛ این تصمیم کاملا نشونه فرهنگ گرم و خانوادگی این کشوره که حس تنهایی تو تیم نباشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/95854" target="_blank">📅 17:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95853">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCU4j6WW1tfNuJACMwFPVCX8h7UYi6cY4LXPdbOjJMFLSgsDBfwk1cDKTRGwSAldxeeXocWydDI5E6L2IdAw8_ixXKGfT2YUNSE8rRUXCvglVi_oLJuTzr8_DafhKjB4cbK8qjXL4fCGYEeDu3r0rsDpdpaxTFp8qVejWCI6aVqDaDFTuDBErxni0eX4V3mAbdW6hivw269RukdxH6d_TxYPk15YevgsSmEReRcmRjNNxpKSN1hXOkp_nllk-rnyMx-dcCVVRnlGaqpS0VrUrswwzVZa_tji6IqQkUNhGAMjtw30lUBTtqKosZgaZJsLvFQUMuLCP9zyVNIK7XknAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلزنی تو هر 3 بازی مرحله گروهی کاریه که فقط اسطوره‌ها میتونن انجام بدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/95853" target="_blank">📅 17:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95852">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aa271917c.mp4?token=elKoDplTT4d29St-fVy3I4wFjU7ASLXPZTQfh9lRF7A6bcRi1x3jZG--0Rpa5zxtlAXHmpcgzT1-eawRG8Hdtqt9QMqMfsO1XlbrSB6NGbgvs7aY8e-kbe1UKdQ4DZ4QSPZA8UTSIfN8bDxGI0HvQ0obkSgfiC2fhExYm3xXO9O10ViA8rnuRdJdA3mBJykpwVFU9L67kOLligzfDO_55NulYE77w2nyUf_AkINgh4h7eNfa4gEQ6d__Pbg2hUX62Kg9bHH4GC68vcMCBSgl6jh9zMB93-b1v_QT2Xbkv_WqkQpZCeFWy954MVzqfQMyfvHjk5-ODD0rCJqwdz9VZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aa271917c.mp4?token=elKoDplTT4d29St-fVy3I4wFjU7ASLXPZTQfh9lRF7A6bcRi1x3jZG--0Rpa5zxtlAXHmpcgzT1-eawRG8Hdtqt9QMqMfsO1XlbrSB6NGbgvs7aY8e-kbe1UKdQ4DZ4QSPZA8UTSIfN8bDxGI0HvQ0obkSgfiC2fhExYm3xXO9O10ViA8rnuRdJdA3mBJykpwVFU9L67kOLligzfDO_55NulYE77w2nyUf_AkINgh4h7eNfa4gEQ6d__Pbg2hUX62Kg9bHH4GC68vcMCBSgl6jh9zMB93-b1v_QT2Xbkv_WqkQpZCeFWy954MVzqfQMyfvHjk5-ODD0rCJqwdz9VZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
▶️
روایت ایستگاه آتش‌نشانی تهران سط بازی ایران بلژیک که بهشون ماموریت محول شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/95852" target="_blank">📅 17:05 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95851">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24bf6ca2bb.mp4?token=BAZD8hdAbueM-i4nwqK3Jam14XO6gRy1B66csVCX0o4a2P4xBZOXjo0IkwL2OCMBtuKnDuCCnlHCD8s2Zs2YFbi3y02nFcXqaVpExLw-TvWoTQOFFqBTLEK3qgO4Xc1wsYTmwofXcdLDxJYw1zXsMr5eNhtJOB6QbQ3D8LzEO1kDHWrmQgaLU4suJpkYarDglyB2BuI2sCZQr49kUQLn9UceiG4p6H61ZmNJfbuv88lCPzbt2gjvGzf59v4HrwOWNj9G8L84-OQFFeZyGMkwnrsr2MyqLeWDZYOZx0Sp-qFXDM0DD_oHQYxXdUjEZrmIkswL7VGF6MCWsQKD4Ih19nD9b_UW7G27BlLkeUkU3xJoLMosg1fmg-w2wur2n7fTi16ookX5u6-Y2FCf77QtMZNa4Hw9uSOmd25TTdu72EyxDb77Ut3rd_uoXF0qOunBSyHCcafVOA0XPoHTctLqHR2WkmaWb8espghLa6geNAP46E6peL38QaRTF22ClgJd2-qcHHTFLA0FlsbPQnQUlBHVXEnLyBsQzvxMNq2xcx1TC-Rbo2mE8BeJbue209VO1oDmsSUab1x-OgA7X6TcZs7o7Vu6kvP7C1si-gbNaLGPCs92tyXJ38jnrRZX7Xh58Tg7ABGkyN-nY-uWvt18qgAQwRqRVCvGWEwj2PQZbPE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24bf6ca2bb.mp4?token=BAZD8hdAbueM-i4nwqK3Jam14XO6gRy1B66csVCX0o4a2P4xBZOXjo0IkwL2OCMBtuKnDuCCnlHCD8s2Zs2YFbi3y02nFcXqaVpExLw-TvWoTQOFFqBTLEK3qgO4Xc1wsYTmwofXcdLDxJYw1zXsMr5eNhtJOB6QbQ3D8LzEO1kDHWrmQgaLU4suJpkYarDglyB2BuI2sCZQr49kUQLn9UceiG4p6H61ZmNJfbuv88lCPzbt2gjvGzf59v4HrwOWNj9G8L84-OQFFeZyGMkwnrsr2MyqLeWDZYOZx0Sp-qFXDM0DD_oHQYxXdUjEZrmIkswL7VGF6MCWsQKD4Ih19nD9b_UW7G27BlLkeUkU3xJoLMosg1fmg-w2wur2n7fTi16ookX5u6-Y2FCf77QtMZNa4Hw9uSOmd25TTdu72EyxDb77Ut3rd_uoXF0qOunBSyHCcafVOA0XPoHTctLqHR2WkmaWb8espghLa6geNAP46E6peL38QaRTF22ClgJd2-qcHHTFLA0FlsbPQnQUlBHVXEnLyBsQzvxMNq2xcx1TC-Rbo2mE8BeJbue209VO1oDmsSUab1x-OgA7X6TcZs7o7Vu6kvP7C1si-gbNaLGPCs92tyXJ38jnrRZX7Xh58Tg7ABGkyN-nY-uWvt18qgAQwRqRVCvGWEwj2PQZbPE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
به‌مناسبت تولد لیونل‌مسی این صحبت‌های زیبای دکتر صدر راجب اسطوره رو بشنویم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/95851" target="_blank">📅 16:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95850">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a8197a2d3.mp4?token=lfWxJQWTz_0c34pnmjZZLvgq6e-sUqbFdCq85BXjQYvdgdisqDCzlu9KtvNFPQ55dYwIjx2v2MjDPxf7TQnuX_JRNsbR9-KdgB4BPK6_XUgxvfIYBm9Hdzi-nSsAYK6vIjeIjvapOcGBYzp1l6NtbkQ6EppXjMhPTApYF48v2LFNrL424Juklvrwsvhfc3xQxsmbAvzMbtYcL_lfGvHqP0CWxZpp63gCSGMsZu_kRLCo6e9l3ztCs-T7JsFGDWx8dENbADU6Or178P_9RnX0seYXp4HJsYKXiriPw-GgwfSb4v72AxOppVlF9HDRHF5kyzBbRmvFQQq1QAq8k51oqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a8197a2d3.mp4?token=lfWxJQWTz_0c34pnmjZZLvgq6e-sUqbFdCq85BXjQYvdgdisqDCzlu9KtvNFPQ55dYwIjx2v2MjDPxf7TQnuX_JRNsbR9-KdgB4BPK6_XUgxvfIYBm9Hdzi-nSsAYK6vIjeIjvapOcGBYzp1l6NtbkQ6EppXjMhPTApYF48v2LFNrL424Juklvrwsvhfc3xQxsmbAvzMbtYcL_lfGvHqP0CWxZpp63gCSGMsZu_kRLCo6e9l3ztCs-T7JsFGDWx8dENbADU6Or178P_9RnX0seYXp4HJsYKXiriPw-GgwfSb4v72AxOppVlF9HDRHF5kyzBbRmvFQQq1QAq8k51oqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
وقتی قند تو دل هوادارای فوتبال آب شد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/95850" target="_blank">📅 16:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95849">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0437caa8c.mp4?token=QWMQb6H_8c29Rx-KRSruLPazY6l-hdoWCBYlLz_Yn8dTSD2quS1nISZ2TqHo1cIRN30FcxNkXUetY_QN7W5n0KQ2eAv9eCOv89cHNkWC8-oZSLHXkIUHp32_W5SxjZdbGPeVQUOocILMQGH7niEZLNddu55DAVIWu056eHFWQVK6yVHEeSy5C5HllVFT7QmTjiPdny8LzaiVfc5EeCNKdj6vzesEHqBEO5Z7BWnVtXaakqyBvGtMuxZYn83wQFjZgGP5Fl7ZzWI_1nhRinjrcapjU6_7lQy95NVT6xSYFxWjaRRksUsVyCaLonb89r9INzy3vt8o1nT6uN33iNFhIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0437caa8c.mp4?token=QWMQb6H_8c29Rx-KRSruLPazY6l-hdoWCBYlLz_Yn8dTSD2quS1nISZ2TqHo1cIRN30FcxNkXUetY_QN7W5n0KQ2eAv9eCOv89cHNkWC8-oZSLHXkIUHp32_W5SxjZdbGPeVQUOocILMQGH7niEZLNddu55DAVIWu056eHFWQVK6yVHEeSy5C5HllVFT7QmTjiPdny8LzaiVfc5EeCNKdj6vzesEHqBEO5Z7BWnVtXaakqyBvGtMuxZYn83wQFjZgGP5Fl7ZzWI_1nhRinjrcapjU6_7lQy95NVT6xSYFxWjaRRksUsVyCaLonb89r9INzy3vt8o1nT6uN33iNFhIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🙂
🇲🇽
هوادار مکزیکی قول داده بود که اگه کلمبیا از گروهش صعود کنه یه حالی به پسراشون بده که به قولش عالی عمل کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/95849" target="_blank">📅 15:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95848">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33a7bc6828.mp4?token=pKYKSJpGUP_gb5CWF0llH11ndpGQX1IytykfuDlSa5kyZw6TaoFfLUg9GqQC6cU69j7w_keGZyu4Hl6qTj-6k4qvvERll-jY1LrW-2Q8qS4_ytG6b4oKH-s66JxHi0DLeGCBtGfe7ZnLnVp_MQc01xY0t3_iQ2DrSycLCs1sVzawCx1T5vVIk9Hp9gTK_vWojLKrYViT5jZ609mJvSMcOUz3JJJemX00OdMba7aD87Z9h43rh0Eq-jVX6zFrxYLQoHjN4GaljnyDTeIRNiRXoAwQhgXEYJOYVYvI988pBGkMwdiXhZriRTtyZMuyIFUns3FESeu1f2OSaeq7oWXk0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33a7bc6828.mp4?token=pKYKSJpGUP_gb5CWF0llH11ndpGQX1IytykfuDlSa5kyZw6TaoFfLUg9GqQC6cU69j7w_keGZyu4Hl6qTj-6k4qvvERll-jY1LrW-2Q8qS4_ytG6b4oKH-s66JxHi0DLeGCBtGfe7ZnLnVp_MQc01xY0t3_iQ2DrSycLCs1sVzawCx1T5vVIk9Hp9gTK_vWojLKrYViT5jZ609mJvSMcOUz3JJJemX00OdMba7aD87Z9h43rh0Eq-jVX6zFrxYLQoHjN4GaljnyDTeIRNiRXoAwQhgXEYJOYVYvI988pBGkMwdiXhZriRTtyZMuyIFUns3FESeu1f2OSaeq7oWXk0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🤣
جواد حسین‌نژاد از سوال خیابانی هنگ کرد؛ چجوری میتونه اینقدر کسشر بگه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/95848" target="_blank">📅 15:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95847">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d0561433a.mp4?token=eV223XCW5AgtUz4O8P5Yd-CjJ2MPTmsPd2W4I4PUyclYjbojqG6RAdHm2SMEPZaA4uuGnNrxW7JfnfLQuDxs3OmxBTJ7ldGE3N5LoUsJEjFhZug-jZIidRDgi4W7SDkq8hm6Uulf58R5lFjT2hTs6VXk1-iDSbeiH_7uPYOYZ5o8fZKk0NHU48_fikKp24GYWK5cwwib33GPMkmdQo8cGj922P0jpOogYzPH-IRotyGU0Il7bA1kDqfrKRc37gC1iy7wuUAavr7uIREZfn_besclzLzT5bM12Yjiicpn5g9X1tjOiGsJu6wnMpGiTh8r7G0-K77g9Gg9AgOrUoKLmwR-GmBK7g6zr-OteRiwWUxaM42t-laTrgmZAVENb9ndiqMtpcNolXeMhsXz_Mxxundasa_qYqA6xiPGQ8SByne2OWanwIKuVLZGbIHc0zIgc-Bfy9NA8vOJdFjOAhqvVtTIFbAy8no0MFsj0FPPvTxZKZra98_32tUeMTKv-z9iX4-Y1azgagXmQTjWQd4aguBEgH0yh6jnwzLe7qxCdS66fZWYYyk7b8nGp3yUjfkbgYMGQdwh3NCGOyuV_FH4KB2rUIHZkPGdcAG1esf-WSgGQN-voIBIAv4GrD7MgH62BnDFrgxKrrgxx8ahl2s2jx_dvibFF_H_5CK0Sjk7-RU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d0561433a.mp4?token=eV223XCW5AgtUz4O8P5Yd-CjJ2MPTmsPd2W4I4PUyclYjbojqG6RAdHm2SMEPZaA4uuGnNrxW7JfnfLQuDxs3OmxBTJ7ldGE3N5LoUsJEjFhZug-jZIidRDgi4W7SDkq8hm6Uulf58R5lFjT2hTs6VXk1-iDSbeiH_7uPYOYZ5o8fZKk0NHU48_fikKp24GYWK5cwwib33GPMkmdQo8cGj922P0jpOogYzPH-IRotyGU0Il7bA1kDqfrKRc37gC1iy7wuUAavr7uIREZfn_besclzLzT5bM12Yjiicpn5g9X1tjOiGsJu6wnMpGiTh8r7G0-K77g9Gg9AgOrUoKLmwR-GmBK7g6zr-OteRiwWUxaM42t-laTrgmZAVENb9ndiqMtpcNolXeMhsXz_Mxxundasa_qYqA6xiPGQ8SByne2OWanwIKuVLZGbIHc0zIgc-Bfy9NA8vOJdFjOAhqvVtTIFbAy8no0MFsj0FPPvTxZKZra98_32tUeMTKv-z9iX4-Y1azgagXmQTjWQd4aguBEgH0yh6jnwzLe7qxCdS66fZWYYyk7b8nGp3yUjfkbgYMGQdwh3NCGOyuV_FH4KB2rUIHZkPGdcAG1esf-WSgGQN-voIBIAv4GrD7MgH62BnDFrgxKrrgxx8ahl2s2jx_dvibFF_H_5CK0Sjk7-RU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
این‌صحبت‌های زنده‌یاد صدر باید با طلا نوشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/95847" target="_blank">📅 14:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95846">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dda5255345.mp4?token=fQkGFLieZtsEzqwq-S1vX3Jd88wmpgcZik95qgyosQuPtTdSfdLbVEeB81JRcf_A-46OnWv8c4F5rO9uxFAh_TqL4mTUfTSuB5mt_4-XOPPnmBhx7fjiONO3kDW_B__JPsen9vqCBbp1uVHDxPfAqj4LWXhuvcLLb4QDZQVM7DyYtAc9m8mD1Exui1D_PkzWrV8hBmIeuSqvPCd8zq6553pbALps8mpFjH5RXSC8SlQagTRiJ9BBE_rCWq9kpRl9dgJj8dSMDqbhHfgeS0vwFmJbXgZi3fJBXAEhXsabPr6Wp0Hh4SYft1rZCuQPi3V0zgDn-LCpxTa1nHS8QzROkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dda5255345.mp4?token=fQkGFLieZtsEzqwq-S1vX3Jd88wmpgcZik95qgyosQuPtTdSfdLbVEeB81JRcf_A-46OnWv8c4F5rO9uxFAh_TqL4mTUfTSuB5mt_4-XOPPnmBhx7fjiONO3kDW_B__JPsen9vqCBbp1uVHDxPfAqj4LWXhuvcLLb4QDZQVM7DyYtAc9m8mD1Exui1D_PkzWrV8hBmIeuSqvPCd8zq6553pbALps8mpFjH5RXSC8SlQagTRiJ9BBE_rCWq9kpRl9dgJj8dSMDqbhHfgeS0vwFmJbXgZi3fJBXAEhXsabPr6Wp0Hh4SYft1rZCuQPi3V0zgDn-LCpxTa1nHS8QzROkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👀
داستان ریشه عمیق ارتباط صمیمی بین کره‌ای ها و مکزیکی‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/95846" target="_blank">📅 14:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95845">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efbf385023.mp4?token=Q7-ecDn68Sk0uRQiP6KsaS481Y4fGKTeih1NjFk5k7ZKXdqUy650QZo0aC2SPg_AnIVPoqnmIPcIFAFJ1Pdk-N04OK4NGCfSevxRGAQ-sBxa7rNiY-qNI0kr6gU5Awoiup4JAxpQYE6tzTBZMK0T2ElRX_uxy11U3L_64Jfkphzqh0apXY8TH7qi7jB6zO9KzY14fn18_MDNzpNQpTzyKqOSMWWxx27jH3P8JN3frj1qvJNVsfJhTsebsbA_itgsRxwOCYDHGp7BS6iIcr7ZuzOdyaFiOMjvN70fP8x3-Tgi15YQyi8yIZCO15MxNMT7uXJZ1ThiH61WtnKBnVbxhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efbf385023.mp4?token=Q7-ecDn68Sk0uRQiP6KsaS481Y4fGKTeih1NjFk5k7ZKXdqUy650QZo0aC2SPg_AnIVPoqnmIPcIFAFJ1Pdk-N04OK4NGCfSevxRGAQ-sBxa7rNiY-qNI0kr6gU5Awoiup4JAxpQYE6tzTBZMK0T2ElRX_uxy11U3L_64Jfkphzqh0apXY8TH7qi7jB6zO9KzY14fn18_MDNzpNQpTzyKqOSMWWxx27jH3P8JN3frj1qvJNVsfJhTsebsbA_itgsRxwOCYDHGp7BS6iIcr7ZuzOdyaFiOMjvN70fP8x3-Tgi15YQyi8yIZCO15MxNMT7uXJZ1ThiH61WtnKBnVbxhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
این دخترای مکزیکی چرا اینطورین، ولشون کنی همشون از توریستای جام جهانی حامله میشن
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/95845" target="_blank">📅 14:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95844">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🚨
🏆
🇮🇷
🇪🇬
تلگراف
:
فیفا درخواست جمهوری اسلامی و مصر برای ممنوعیت پرچم‌های رنگین‌کمان در بازی دو تیم رو رد کرد. طبق اعلام فیفا، هواداران می‌تونن با پرچم‌های رنگین‌کمان وارد ورزشگاه شوند؛ این مسابقه هم‌زمان با جشن Pride در سیاتل برگزار می‌شه.
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/95844" target="_blank">📅 14:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95843">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b91edd4555.mp4?token=bWtmTWPVLaNYFvdeIb9qXQ4ew7uI9O5QkCgxCuRt-gXm0LRJADo4hdirMVu5MccsbAYNVIOdydSTP6f22SqxVHaRyj8i6f5f_EjSA9K7Jt_W4r8rB10pPcpUqwnJMWQ98sLuGMBlue-U7q_f40eP4hmEiwzjvR7fawRfw4j52P6HW_WeIdLtudkXz2rotx5-4pJIPT6Jvf62-0KNATauXsz4T3pyI1q7swND0LsytJjnjT62xiKz4nRtVwpOddb3pawGdpxltXlcyPV6f5RrRM_P70sx3eaVwFLPs2Im--FVgLlQIX5Nona2eRqxupX-ScK3q-vgJPPagFBpzXbEkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b91edd4555.mp4?token=bWtmTWPVLaNYFvdeIb9qXQ4ew7uI9O5QkCgxCuRt-gXm0LRJADo4hdirMVu5MccsbAYNVIOdydSTP6f22SqxVHaRyj8i6f5f_EjSA9K7Jt_W4r8rB10pPcpUqwnJMWQ98sLuGMBlue-U7q_f40eP4hmEiwzjvR7fawRfw4j52P6HW_WeIdLtudkXz2rotx5-4pJIPT6Jvf62-0KNATauXsz4T3pyI1q7swND0LsytJjnjT62xiKz4nRtVwpOddb3pawGdpxltXlcyPV6f5RrRM_P70sx3eaVwFLPs2Im--FVgLlQIX5Nona2eRqxupX-ScK3q-vgJPPagFBpzXbEkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
▶️
کار‌جدید حمید سحری به مناسبت تولد مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/95843" target="_blank">📅 14:04 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95841">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XcnPGg3WRnWBWQT9bTrrQ6S0nHnHxjNGzjdjDCGiC_zPHzRu3UFIwq4lgvpuIcLsg3Y98AEKBWCW_Ksz9YCaM_p_WB1gXPOzmmXsVRL7mCFYVm2hQDIbSAFD2nwDl7SwFbJ9nQ_s2VHy_jUItVbAq_Jkj65e043BBXDwBCkjhqvO3nqEihaqAIMGCRFVFRMwB15xt09sSzyN90Xo1u6GOKb02MHztpnzpO2Ogle3VOMymx9jrYI-bQZhz_xBqVGrmx-jVKkNLaZCGCVkXd86eZDHUQxPiii8BZbF_hmpMDSLpfo7wJvI19eD4XCG7bwTDEfAnEUh3-8_D_Fy54jL4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/le6G32TIdy49JFOV4DqiIOuAAORLXYhju8oJlYCdgv-vmVj_MqAvox-0z1Cu_kD1yU8upuKSODr-LPaS1c-_ubroUtnXNaU1AFvuLo2BhszWNBFHLAhcSi9HlA5kuMICFTWEYtiFCwmX-e4alS9EJApktV74Pj5Y26oOM_XtdJaY9H5cq6jsq1shosQlYKfAu9If8sztktNORI5_13xrNbQIhWSHf0rxiXcYefjSjoBRPEkHk2Nx2sH9dgCB7r43sHGwpzz4c8PHt3b5VqBJNFIOObHmRJ-UcUC4BQ3-i15Eq0W1bOU55yvvyb57btOyEvSOy5hpmjuW1TWWkrUAdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">لطفا هوش مصنوعی رو متوقف کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/95841" target="_blank">📅 13:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95840">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03f0c754bd.mp4?token=W44rYk7lqKYudgdq3MYJiT55D9IZj6pC-Z9Ll2vH6TTnYcOHY96FDsqnGXsW20nXCIAgs2ckWZAluJKFuhxCEHoFhKy1FmYRNvOzmvnKn3auW4HN-0kdSSEP9mo0bMlxROyz3wKS8dMcJu7ZEt9NjZGYBJvjAbEy5gXu6CqVkYohFsAAlB72AGxWZ_nerX32-GfGMxLp0GygFatN8dFtu_ONpRFQdCEqgY4qy9xbOayqxke74uu349NDov42opjdf8elTNUE14-eGIFg207NMudd2ek3DVABd8se6GMIdprDvHvDdfjTo36JvN2p9o2PxlHkzm9Rg07AUiGn_IejDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03f0c754bd.mp4?token=W44rYk7lqKYudgdq3MYJiT55D9IZj6pC-Z9Ll2vH6TTnYcOHY96FDsqnGXsW20nXCIAgs2ckWZAluJKFuhxCEHoFhKy1FmYRNvOzmvnKn3auW4HN-0kdSSEP9mo0bMlxROyz3wKS8dMcJu7ZEt9NjZGYBJvjAbEy5gXu6CqVkYohFsAAlB72AGxWZ_nerX32-GfGMxLp0GygFatN8dFtu_ONpRFQdCEqgY4qy9xbOayqxke74uu349NDov42opjdf8elTNUE14-eGIFg207NMudd2ek3DVABd8se6GMIdprDvHvDdfjTo36JvN2p9o2PxlHkzm9Rg07AUiGn_IejDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
😛
سطح اعتماد به نفس بلاگر نچرال وطنی: فوتبالیستا و بازیگرا میان دایرکتم؛ طرف باید ماهی 300 میلیون خرجم کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/95840" target="_blank">📅 13:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95839">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9758eff507.mp4?token=YCxlgmCDNHRBNZghH5OJggHclbEEYYsC0s3zvpBWuDknvNR8mmKi8JuGxchN_70IDI3Sn6HuvUQ5McFicQKBKH0oARmZYnQtFUtt8jXJaPJtE_Nht1jBhtQ_CkJXfqSiWgu79H5PwynZTSR2i3qLsE7z3Kr2W6soWslSC6uIVvRuCy2fJ041hC7SyXfaqIkpzEfDE50Fz82jAwo-QfAaVN_spX-2bKKdps9SHA67XJdSqU3svdxZ_07ZyilsX69VuqrkourLuC0OuktCaZG9SxqkP_mrXKiA7vGwilMQPXks2rcmB_81gfcBJYTygcnvT0tmG6p4TEbatm4AaD74JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9758eff507.mp4?token=YCxlgmCDNHRBNZghH5OJggHclbEEYYsC0s3zvpBWuDknvNR8mmKi8JuGxchN_70IDI3Sn6HuvUQ5McFicQKBKH0oARmZYnQtFUtt8jXJaPJtE_Nht1jBhtQ_CkJXfqSiWgu79H5PwynZTSR2i3qLsE7z3Kr2W6soWslSC6uIVvRuCy2fJ041hC7SyXfaqIkpzEfDE50Fz82jAwo-QfAaVN_spX-2bKKdps9SHA67XJdSqU3svdxZ_07ZyilsX69VuqrkourLuC0OuktCaZG9SxqkP_mrXKiA7vGwilMQPXks2rcmB_81gfcBJYTygcnvT0tmG6p4TEbatm4AaD74JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با کریستیانو از این‌شوخیا نکنین
😁
😁
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/95839" target="_blank">📅 13:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95838">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSSEay9aLRJBlcNXLxghD4JYyAEVf_-Yph5yhHiFbJpWOBCdv4Z-QQbgnZL_kFmb2kXMdMw4E7IXQBEtmqaElU-abzOytKWYYtnqE-QQ3hxG4XXwbQ7Nkm7r8TWxxy4QG6pBVlPAgJIRBJTY8_h2offruFHEtzAz3TnF-UcvAYROv0VbuR7H038cLhxrzkq-KUbH182S9VZw1Gayc2SKsaJPmejrXSVhe9mYpevsF1cevjZYp3t4ZBycw3z-y2vK4aQzic3072Us_37Lzp7eQds_Ve5XDwTeCJyIQBRoMDwWvt-W4OHfDxuAGc6hBOHg7YSDHK1vyWvDaaYmOpCxDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🎙
🇧🇷
🔸
وینیسیوس جونیور
:
🔺
کارلو بهترین مربی جهان است، و می‌تواند بازیکنانی که در اختیار دارد را بسیار خوب درک کند، او کاملاً با بازیکنان سازگار می‌شود و بهترین ترکیب را برای هر تیمی که مربیگری می‌کند، انتخاب می‌کند.
🔺
او به اینجا رسیده و فهمیده که چگونه باید بازی کنیم، و من فکر می‌کنم این موضوع موفق بوده است. او در طول مسابقات بسیار پیشرفت خواهد کرد. من معتقدم کسی که مسابقات را بهتر درک کند و در جریان مسابقات پیشرفت کند، برنده خواهد شد.
🔺
در مورد نیمار، بدون شک این لحظه بسیار مهمی برای همه ماست، زیرا الگوی ما بازمی‌گردد، کسی که همیشه مبارزه کرده و همه کارها را انجام داده تا اینجا باشد.
🔺
او پس از مصدومیت بازگشته است و امیدوارم که به پیشرفت و بهبود خود ادامه دهد و در طول مسابقات به ما کمک کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/95838" target="_blank">📅 13:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95837">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9Pktg3QtTL8L-RucVMHwe-xhFnTFV76gmfOwqejUCf3tA-3RxBwtod-dX1ZuiwdoHtxSps-nOS0w-3RsdPEkft3Q2ZH5zOK9nuO_X5K7yGAP-JXe_14iVY0ebNEkAdVKWmFYS-MLeiREh-JAtaL91_ANfCswqs_J2kIs01sNAsTlnIX6zyTgs6fc1nirQbxqpSlkDzi6Fh2WI4fd9FAsR31YDQBbPJJGknz8hvjnn_aCpcmwkmGKQQTQeKcjbvUeEZ3CYU-O0FsIO79ErOZJbf8ahMCGB1STrRj77jnFoYFo9cbgrLIEI9gQpz1a-lyiqzSrY1E5_GP7jPO2qOKJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ترکیب منتخب گروه A مسابقات جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/95837" target="_blank">📅 13:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95836">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5626b0ff4.mp4?token=mzqrqFhw33MaPbxGDVb6waXIj6N0x6vS-JIYIQTVUGDqgXlJ0lotfl7zBIc0RFKsvaxw7fGphpZO0cCT-izHhVcFDQoycPK8K0IaU0SkaE1PVnjGjPLcNJXOAAQ5WSs9hjlcFHpYP5ESMUifimJeTBnvnWZ3LvH6HM7mzOrCwLQHM0Z2aw9aKwoJGGB9ElDn-uBhUgPdtO0XoDmbMD9SmhoKSZ72YxQdlLfuBirHZqS_SnnmzualePlbsA8BKv6lC22O6VV3J7RScZ89yDLThgMcqJFLyLMaLVh8ZVAL_zkJPGxyCrDhwBKzp6apA1clzNd5JGcs2dSD09Z-4MB3tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5626b0ff4.mp4?token=mzqrqFhw33MaPbxGDVb6waXIj6N0x6vS-JIYIQTVUGDqgXlJ0lotfl7zBIc0RFKsvaxw7fGphpZO0cCT-izHhVcFDQoycPK8K0IaU0SkaE1PVnjGjPLcNJXOAAQ5WSs9hjlcFHpYP5ESMUifimJeTBnvnWZ3LvH6HM7mzOrCwLQHM0Z2aw9aKwoJGGB9ElDn-uBhUgPdtO0XoDmbMD9SmhoKSZ72YxQdlLfuBirHZqS_SnnmzualePlbsA8BKv6lC22O6VV3J7RScZ89yDLThgMcqJFLyLMaLVh8ZVAL_zkJPGxyCrDhwBKzp6apA1clzNd5JGcs2dSD09Z-4MB3tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💥
🇲🇽
هواداران مکزیکی این‌شکلی بعد گل دوم دیشب کشورشون عشق‌حال راه انداختن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/95836" target="_blank">📅 13:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95835">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.2 MB</div>
</div>
<a href="https://t.me/Futball180TV/95835" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
نسخه آپدیت شده اپلیکیشن ملبت
🔶
• لینک سایت مخصوص کاربران خارجیMELBET:
🌐
t.me/ConnectMELBET
🔶
• آدرس سایتMELBET
🌐
bitly.uk/connectmelbet
🟠
نکته: اپلیکیشن بدون فیلترشکن کار میکنه برای ورود به سایت باید سرور فیلترشکنتون رو کشور های اسیایی یا کانادا یا ترکیه تنظیم کنید</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/95835" target="_blank">📅 13:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95834">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpTzQAtew7eda9ItDlLtIEd0ZC-VlWJGJaPM5b7tLtCF1_DH2wZzdeLKfCoC52IokkY5G6Cw03T-pI9OgfV3DBhyBrqhhydysM-3yLnFajrs-fTs0s52nOK_uNrAy10zVEhzFyRgQFCsIi7SQdXSlpmfhq56dGqs7sZOjnABzxRT-JD9iLSXdmm6LH_-0ZODHl_yvyBxdpGCx07Qyu3BQQlyN-LqAD2fZJJ_UaGQj1_C-G58xB_U2SktzNzwTHsnHk3qlflLZzNZnS7JdsA9g1QafTkWmEZa1BEGHhO8lmtZB6mzFkEalB1ga8hNgjn_ptnhK7O1xUHsWaMLWmmsGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
بهترین سایت برای بت زدن سایت MELBET هست که مورد تایید ماست و خودمونم چندین ساله توش بت میزنیم
💸
با اولین واریز اگر با کد هدیه
ml_459049
ثبت نام کنید تا سقف 100 دلار 130% بیشتر شارژ میشید
واستون لینک و اپلیکیشن ملبت رو میزارم که ثبت نام کنید
🌐
https://refpa3665.com/L?tag=d_3312431m_45415c_&site=3312431&ad=45415</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/95834" target="_blank">📅 13:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95833">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3soYolMU7XbeBXBrh-yngcOErIPuZdihpDU1gNaHRzEEkrmru5yDV9fE1OA2YD8KDw0dnRk1f08GDVtVhbUSJYnkhgJwSbPIwDv_T2BMEvQ2xF8JxjVInvYS0DBF70fzynY9uHVAL6iZBzAX8lMc8OhBHGwu4ggtTynfwAvAkNoWo3uabGcJey9LGLQ9ZWQVk6KKBTfVItRzxDdA7yijQEqdjTXlRd3NuBpXbOekJIexVtcK4Uc_xc1gQWl1VB7XcYmmAW0oTiBQpvzgK2asrh-ih7d3d_FUZx9itlm-4eLarA7YjN_-mouRCMrYvD-YkFtNvxHNc4KY2gm06nimg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمع همه خوبا امشب حسابی جمعه
🍸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/95833" target="_blank">📅 13:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95832">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e72f9cd3a.mp4?token=B8HzFu58RB3O0xRpqIb8n8JhPpBA_wSgbWPNIISxTWNj3H6IcGkBh93cu025p0oh5MQgkvcZem4DcWWBoOTDRssRo2Bw6v8zI8o2P_ZYZZwqEh5YEk0N8Ot7RSd9_AvM2ckfZ2vEDW3KACJYFTBIw1J0o491r4kbwbpWQzeFmBhZtcYRXumw67sgwsbxjTohzp_R8S0Ksf2UcKlUKuG35UK2Bbzt-XP40PMCS1dIGOcbJyBgwNvwZVwk7-gQneuqXtX1YhlSZ3BAxz_ySEFP77wC9MDJLNgxPXefjfT5_EH6d0lnpP2u5xNMIy0YQ1mvlqhUDPep-PkPS4zJncqa6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e72f9cd3a.mp4?token=B8HzFu58RB3O0xRpqIb8n8JhPpBA_wSgbWPNIISxTWNj3H6IcGkBh93cu025p0oh5MQgkvcZem4DcWWBoOTDRssRo2Bw6v8zI8o2P_ZYZZwqEh5YEk0N8Ot7RSd9_AvM2ckfZ2vEDW3KACJYFTBIw1J0o491r4kbwbpWQzeFmBhZtcYRXumw67sgwsbxjTohzp_R8S0Ksf2UcKlUKuG35UK2Bbzt-XP40PMCS1dIGOcbJyBgwNvwZVwk7-gQneuqXtX1YhlSZ3BAxz_ySEFP77wC9MDJLNgxPXefjfT5_EH6d0lnpP2u5xNMIy0YQ1mvlqhUDPep-PkPS4zJncqa6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🏆
روایتی‌جالب از حضور روانشناس خِبره در اردوی تیم‌ملی برزیل و کادرفنی آنجلوتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/95832" target="_blank">📅 13:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95831">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnUzCoOiZ_Wm0WlS_ubQbMNV2zx9_NlTo7MsA1YBOSTP7X9fqDhJ7lgCglNNPOZJrKcufABGRnJtmHettmkmWmcx6kphsNheVHYJt0HGj0WmT3Oiztw_zo8jDg1W6F9sfoedAOGIrEHljZOI8L3GgU78NI0vp1zkwoq3Uj-RGDtWqgOY7e8NAjlsf5hA7nBGvCT6-Z3z7APdf5_olDyLp3WnTLnWS1QkuR57yCkrlyIjs6O-H1gOgCYiLckeyTonD7WRbQ5NyGueMGZdjNDOIlv26dZRAGIzLE7eAJHpl4j1xMWQIHAzE1-d-7BpJlV5c172c-7yQHOjRPnk_37OXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه تعداد گل زده رونالدو با مجموع گل‌های ابراهیموویچ و آنری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/95831" target="_blank">📅 13:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95830">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcgPq9e26ZKQjMsrt3Mgi3aSmFuf7VkerNQowb1dQnv3CacOZRju0KmUtsIqBE07N1A16B6SiaOwmWi2V78YfnLBv4l3lYwXBKKmTB3jRditNTudAEqUQ9LbAKVCFvExivEPBO9jUP1usaKg2Teijd3DwXLI0ucYFne11ZNr6vGOPYU2NCzbhgDT6tdnP5TniB_Ft4MlEewkzIt-WPuPFI0YFgvrcOHqavx8mdy75ya-R9MvcLCoU-eBlE-hOXBM-tqthl8BWeWU7M2MhAB4379R6vpUDqvYN1Db3LUyq6Bqup7hRd5LV5Rf_mAmZYLc3zGt_-eivh2SmjkaFFi0Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
وضعیت سون بعد باخت کره مقابل آفریقای جنوبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/95830" target="_blank">📅 12:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95829">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSKnlGGn8UEY3cnEHv2muecKwjrKAGaH6qoCV1_NhgGOjFr-REsJLdiI47lc7085-3nQW85RmdjfBFDmka_LeM4WSRbiMIwTdFQTHb74uNzQaJgJhEd56As7MLWb-CTR4dNJ-dBnKO3MpjXJLaX8j-rSyrD-JsgFu7W06R1TBscMUlBgAPOXkx4nBjrSL0M6nYtTSYTIH-zZ947cSNq5olvWUcrHNh37DsqieUtsNN7xL9ZLyWKvrb2EIWgNt4OwZLkFmnj48IPlasnoBsFagHXjVfbLlQYG59h5uQSX_4EIkjBLAeWYtJ3KcxMudu10rCGakYpdcEJnbRVk16wNIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعد از صحبت‌های اخیر تیری آنری و زلاتان درباره کریستیانو رونالدو، هوادارا تو شبکه‌های اجتماعی میگن این دوتا هنوز از یه سری اتفاقات قدیمی دلخورن و از کریس کینه دارن. بعضیا هم میگن دلیل این حرفا میتونه باخت‌های قدیمشون جلوی رونالدو باشه؛ مثل وقتی رونالدو ۱۹ ساله آرسنالِ آنری رو تو خونه شکست داد و رکورد ۳۲ بازی بدون باختشون رو زد، یا وقتی رونالدو با هت‌تریکش سوئدِ زلاتان رو از جام جهانی ۲۰۱۴ حذف کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/95829" target="_blank">📅 12:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95828">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea0ae093d8.mp4?token=CkhX_aTVOlHKrPK-0s_0fTsu2CTvgRkWOq-wJtvf994TZxLgZPff6_lVHOLEcAJGlRx9jlTn79_06reTQtB_2rnKKPZLJYx1rGbUYbcQvrlqAWh_Q9cpUx81ZYO_C2dc6oleILtF1bTT_T7t4P91EMgPMIHuOhDOkuWHaF_h7fhKIKrnWnBl7wE4trO_UnNqosGShl_2B7HyZOxYMm_oZ1a8wPm-Dn0K2wEuFhe-EfudeocgYszeD5OU_Gl9pvvlv1Q8Eevd3J0o-dexYjF0Z5vq_nPUhOT59g2n54YYYk8B7Wpy508rs3TVxyoRgkLATXMOuKsr7tQzJlA6XhvCcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea0ae093d8.mp4?token=CkhX_aTVOlHKrPK-0s_0fTsu2CTvgRkWOq-wJtvf994TZxLgZPff6_lVHOLEcAJGlRx9jlTn79_06reTQtB_2rnKKPZLJYx1rGbUYbcQvrlqAWh_Q9cpUx81ZYO_C2dc6oleILtF1bTT_T7t4P91EMgPMIHuOhDOkuWHaF_h7fhKIKrnWnBl7wE4trO_UnNqosGShl_2B7HyZOxYMm_oZ1a8wPm-Dn0K2wEuFhe-EfudeocgYszeD5OU_Gl9pvvlv1Q8Eevd3J0o-dexYjF0Z5vq_nPUhOT59g2n54YYYk8B7Wpy508rs3TVxyoRgkLATXMOuKsr7tQzJlA6XhvCcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
یکی از جذاب‌ترین ویدیو‌های چالش آهنگ شکیرا که میلیون‌ها بازدید خورده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/95828" target="_blank">📅 12:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95827">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8fd331e04.mp4?token=lB6A3tk1tBRby0_XaAgQgnJIl3eVC5b3gaw_pMK4m6DL3fTXsyzVn0rx8UPKU3EzZXU9UuhchW84QEHcSBmQFsSuaiNBEwEfBeP8yFpEscGU9nX_7BSuvB_WZfVKUNagqgX7a86RnsN4WRBcVZZ9Wl8pdPeVVONZ8cnAd2e4hLyKqo2Mq8-A6ts4N-PEdw2vlGTsx1h337zCvkoyOgJtfKkRHaD_OT0SFhtWI_YuQ6Wk8GQeiA9hNaUNBWtFqgkrysQ3azIm7dZMAyet0Q7kvATzxKfAyelXY1X1dbGEyp_vri1mPnAC9drWIzi13rw4pAVB2KgwdF534lf84h-MAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8fd331e04.mp4?token=lB6A3tk1tBRby0_XaAgQgnJIl3eVC5b3gaw_pMK4m6DL3fTXsyzVn0rx8UPKU3EzZXU9UuhchW84QEHcSBmQFsSuaiNBEwEfBeP8yFpEscGU9nX_7BSuvB_WZfVKUNagqgX7a86RnsN4WRBcVZZ9Wl8pdPeVVONZ8cnAd2e4hLyKqo2Mq8-A6ts4N-PEdw2vlGTsx1h337zCvkoyOgJtfKkRHaD_OT0SFhtWI_YuQ6Wk8GQeiA9hNaUNBWtFqgkrysQ3azIm7dZMAyet0Q7kvATzxKfAyelXY1X1dbGEyp_vri1mPnAC9drWIzi13rw4pAVB2KgwdF534lf84h-MAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
ژروم‌بواتنگ مدافع سابق بایرن‌مونیخ: «مسی باعث شد فکر کنید احمقم»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/95827" target="_blank">📅 12:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95826">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/521d31d087.mp4?token=K5szUh9xCWf6IvQS8-issbgGFG_lwNevBtlUbJ0j0_dEY8aRgXycmsOQ02bXYuBIb0rulqg_9J7IVUHcuCd5QVD10aaOx_Y2REv2uI6l63uGjB689HIhBAGq6qlwqub3AkcF4yRwbDTVsXIqezNn8geJ8w1mxbPZnrgymBRKBAjZkrp2ZY3JyJT2Az6HL7oIsVIAl870Q-7hdvopR82aZZ_gUW6roeHIKeB-E1510DfiFXqtjN7BjC2kxUQLXPJ6jDxnZn6KTlf12DJwb7yIV5hkkTM7YDlUxeU_Q7EQX2U6Sud_0ylqNulPnHZj63aIzOHrEFs3JGRWPd6RJ6tjNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/521d31d087.mp4?token=K5szUh9xCWf6IvQS8-issbgGFG_lwNevBtlUbJ0j0_dEY8aRgXycmsOQ02bXYuBIb0rulqg_9J7IVUHcuCd5QVD10aaOx_Y2REv2uI6l63uGjB689HIhBAGq6qlwqub3AkcF4yRwbDTVsXIqezNn8geJ8w1mxbPZnrgymBRKBAjZkrp2ZY3JyJT2Az6HL7oIsVIAl870Q-7hdvopR82aZZ_gUW6roeHIKeB-E1510DfiFXqtjN7BjC2kxUQLXPJ6jDxnZn6KTlf12DJwb7yIV5hkkTM7YDlUxeU_Q7EQX2U6Sud_0ylqNulPnHZj63aIzOHrEFs3JGRWPd6RJ6tjNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
امباپه: «کین، هالند، من؟ بهترین لیونل مسی است، همراه با کریستیانو.»
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/95826" target="_blank">📅 12:03 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95825">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00614f2668.mp4?token=H9tVwhsRx6MbzSmym4ke3pPJHFtyJ5Z-v17TQoZmj6ojx3LRo3RUKLLEpj89UvZh7RoqPsFPeQazPCag8QxdM2FQKH4wy-yIwchFkTlk6KYEXjolQGwvbTtpK2ykUJGkloZBIiPrhqxHSS9JMjWx6WFiJvgF6CmU-evt6i_WbXb9QQwXaoT3cFETqNYajnHkUT8vmpzaZLtetE948Lv5oR_FE1Rqu-66ARD3nK2pfrxq5I_hTPkbwb10sHFinhaJih_aLzQq2lyZr8pJFMohlTMZWBJZnH9VA0oxD4SexGNwEQtYiLQUwvY5TSyA-iVfKs0uswqIuGDcmIgInr1D9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00614f2668.mp4?token=H9tVwhsRx6MbzSmym4ke3pPJHFtyJ5Z-v17TQoZmj6ojx3LRo3RUKLLEpj89UvZh7RoqPsFPeQazPCag8QxdM2FQKH4wy-yIwchFkTlk6KYEXjolQGwvbTtpK2ykUJGkloZBIiPrhqxHSS9JMjWx6WFiJvgF6CmU-evt6i_WbXb9QQwXaoT3cFETqNYajnHkUT8vmpzaZLtetE948Lv5oR_FE1Rqu-66ARD3nK2pfrxq5I_hTPkbwb10sHFinhaJih_aLzQq2lyZr8pJFMohlTMZWBJZnH9VA0oxD4SexGNwEQtYiLQUwvY5TSyA-iVfKs0uswqIuGDcmIgInr1D9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
پیشنهاد جالب و شنیدنی محرم نویدکیا به فیفا
⚽️
@Futball180TV
‼️</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/95825" target="_blank">📅 11:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95824">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de2dfa1b85.mp4?token=J8Ic5Mem5Ofna8I2bkjzAHY11nKTtW-pP5Sl1YEWTgBgejhLBsO75v0MYz0ilKdy0Joshftm-H6nFoZlirRShwm87tSdit2Oj-bhQdlAvD7Lb7RzcjLkjyMZGwqSmveq4fDkb6_xIjKFocEH_NzsFAFlj4hK6SZwbzqk7lVhw2MAa00VopURWIoqGpbYXtoNWCGDlB8dtz2zS3MkCFmWezeuKEs1H4CIfxxMC8lpZjRUqGj0xE31d8wfGexMAZU_ecm1gXs4o-ihjPK5rz6vfyygG5_32sZgk_PiMS4gsmwiSJpdbpaWo6tUDareIjvRTxdHotFmIr7s4R8k8hkxsWrKwnkirT_8AgugLVbQtt-XldHEW-kyteI8dTDL3txQwT8I1VXo9aFF2-Q-Az8T0XTN91CQl98tUFCCTqBmax-95waiQYD3dJS9RvOdPgtNNWi8pm7hs1qlTmFeBDNqGAN5w0hxB6AQ4Pppx8-AMN1Mylru0JEOGnD-_9fXycWT8ST4qN4HfZpDZLS-h4dmv-e7Qaarsbj5A0LSZ993W5kxUuNDZSxqQzL0cpho_4NCwELnYhTt3kMnCgmpepTdj0L6nN5NmtITjUvVxbEHPVRsY5BnLkaiihblysWu9Ig6MWJgttziymyqAQf5c781MxyV9MaqbAS4GFHjKWRxI90" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de2dfa1b85.mp4?token=J8Ic5Mem5Ofna8I2bkjzAHY11nKTtW-pP5Sl1YEWTgBgejhLBsO75v0MYz0ilKdy0Joshftm-H6nFoZlirRShwm87tSdit2Oj-bhQdlAvD7Lb7RzcjLkjyMZGwqSmveq4fDkb6_xIjKFocEH_NzsFAFlj4hK6SZwbzqk7lVhw2MAa00VopURWIoqGpbYXtoNWCGDlB8dtz2zS3MkCFmWezeuKEs1H4CIfxxMC8lpZjRUqGj0xE31d8wfGexMAZU_ecm1gXs4o-ihjPK5rz6vfyygG5_32sZgk_PiMS4gsmwiSJpdbpaWo6tUDareIjvRTxdHotFmIr7s4R8k8hkxsWrKwnkirT_8AgugLVbQtt-XldHEW-kyteI8dTDL3txQwT8I1VXo9aFF2-Q-Az8T0XTN91CQl98tUFCCTqBmax-95waiQYD3dJS9RvOdPgtNNWi8pm7hs1qlTmFeBDNqGAN5w0hxB6AQ4Pppx8-AMN1Mylru0JEOGnD-_9fXycWT8ST4qN4HfZpDZLS-h4dmv-e7Qaarsbj5A0LSZ993W5kxUuNDZSxqQzL0cpho_4NCwELnYhTt3kMnCgmpepTdj0L6nN5NmtITjUvVxbEHPVRsY5BnLkaiihblysWu9Ig6MWJgttziymyqAQf5c781MxyV9MaqbAS4GFHjKWRxI90" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
💥
دوتا تشویق تماشایی که در سراسر جهان ترکونده؛ تشویق ایسلندی یورو ۲۰۱۶ و‌ تشویق نروژی(وایکینگ‌ها) جام‌جهانی۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/95824" target="_blank">📅 11:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95823">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1-CzcSQqev5FYaBcaWH7ibHjqiOvrtbGBn1Gt1TkJGtmL4viX2z6olMVUao21lMw2Pl7v_rPAD4TbseARYwD7CNvwNX4KzezcXhGdq1gaeRdFXPzis2LqMBmNkNYjzaIWP3gCS1Hn2Z2fjvMoZppIalOirvHGYQh92_NLUvr5lTilKWnRddtlYDH_thTULLrd9kvrJ9Jeg3UvTSG9B8L5eI5W4Xd777YpTKWUYLNdHWOdZ0kxQomSRwKO5aZMY_AUVnhXrrNqaSZT5nVdseKo9D6BLVrSHxh-Zh5Zgdmelro3mdpS8qODn2UVAJTAtgPlIpFV6dmZYBm3hyhwEczg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇺🇸
پوستر جنجالی فدراسیون والیبال برای بازی امشب مقابل تیم‌ملی آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/95823" target="_blank">📅 10:59 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95822">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qscJ7ue4QUhbuOCp2zF5R761dhyfQI08XYYzO3Oq0hzaxzQGr1i6wVIBfeXwUnZYA4FKXowy7EwmeVzyH1HQQ9laVHvIRlvL-AIoTcM0fU2QsUFtSEzh6O2av79CGLLOGfXrWw4lPkcFmUWufyYXfO92tHHxK1OU9p89FtFqyFDQmyrSg_UmZIM4ZGlHdOZ2rzy2ESdMcGd7p7kVUb2fITKpjE6HKGN8WkWF6rxv1mlKesGQ1hHLEkAT__hut8IQVY2dnSYMAD_v9afBc1QGWwcsiqiMZ30qqtI7t7Gd3boxh49_0JlaGo49PL-3QH63MreRl83A2egdpzv4Sy3jVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇪🇸
🇮🇹
رومانو: رئال‌مادرید به کومو پیشنهاد خرید نیکوپاز به ارزش ۶۰ میلیون یورو را داده که اگر باشگاه ایتالیایی مخالفت کند، رئال مجبور به قبول پیشنهاد سایر باشگاه‌ها برای ستاره جوان آرژانتینی خودش خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/95822" target="_blank">📅 10:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95821">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e47Uyqy6kHtY7IHUIHrAHsrBIJEv7jlEBT6I4Kp7cTFyRZF10LpbPFylVXBWS9227bfqqYLHwcVndofEvAYvEfKLLa344TFZ4zin2L78P9YH4Mj7BoedCSvdeTxGReYvU9rP2pTiyE8zl7wXDWY01zB1Pi5SKjD5rQ0t-ycomzr3RrRaoH8rtCSAOLTfRkGLqnQ5OFgKKah6MKBp-oy0-Um_cofO5wpAm8mwa3XJJfJFfIuTj4yVf6fcazQO0dh4qCnlpiBfpOHYPHaeCGpdNSgN3gK-EaUU9AtHQeKxA9CCrYY06EpimrlrSwwRTNlSGyVhGQYFQRlenHDFU7SAVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
احتمالات صعود هر تیم در گروه F:
🇳🇱
— هلند برای تضمین صعود نیاز به برد یا تساوی دارد
✅
🇯🇵
— ژاپن برای تضمین صعود نیاز به برد یا تساوی دارد
✅
🇸🇪
— سوئد برای تضمین صعود مستقیم نیاز به برد دارد
✅
— سوئد، هلند و ژاپن برای صدرنشینی رقابت می‌کنند و هلند به دلیل تفاضل گل برتری دارد
🇳🇱
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/95821" target="_blank">📅 10:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95820">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-KxdI6NZSBPKRua9yATkB0ZFIbNLgcFE0DxhwOf_vcBQ2xy4mRKmjrtHUo-yX3FKl-7RXcnCpkM9gQx-0TqvE2vZxwayhYvO1HXHwQw8wnHub_VnkkHvg4byxc50bgGvyi8eSOc66CIF_qoVFYeaO1CXqY6aWUvPX8XQj6QF5imwFc-zSKYqjcZCyZIF9oXrCO52LwNrNsG08TeTWpsiCfk4MTPF6pDu1CLwm_4AY833FnHgebGKkacMaU1XLN6we-RHA39xtrtMG6yhQZbfvZn3M6uPxNp6VlqjwI5yq1v6eWQBa87dy-NW3gfZWJwG66fqCBuCz8NHYzTum0NTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
احتمالات صعود هر تیم در گروه E:
🇩🇪
— آلمان به طور مستقیم با تضمین جایگاه اول بدون نیاز به بازی سوم صعود کرده است
✅
🇨🇮
— ساحل عاج برای صعود نیاز به برد یا تساوی مقابل کوراسائو دارد
✅
🇪🇨
— اکوادور برای صعود باید آلمان را شکست دهد
✅
و منتظر لغزش ساحل عاج باشد
🇨🇼
— کوراسائو برای صعود باید ساحل عاج را شکست دهد
✅
و منتظر نتیجه اکوادور باشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/95820" target="_blank">📅 10:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95819">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grS8NltFdKASdbtUeB-LEooqO6FD_aF6r-BVVJw2QF8QYQv3GNia6LI5PwT1uH8IGaMsu1Zg8ekyhUTtozl2e2kgsV84hzkwFG1Kr2liVMcpYjDtUgYc7iz0RQTsKQ4gv_lCrKuNJYZBSrY0uZN6cY_Hs3Ri1JcYj9sM1icGM9Wx4suuPwLdT_QpTH-xrHzeL0CkTNsVXzcu6yKhBYwQd_wNme5hrVp6VK8hKB0fKwQz_3apgxjihwWLnBZAeW0034vmPF9dIQN_jFoyIOpK9Ne_-mEHOlxYFgGc6Ky-L4Ot6HnW8R4jJVFu2ZXi4ZPzc3q3CTy0BYDtICozzwq4qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
گل‌های لیونل‌مسی و رونالدو در جام‌جهانی به تیم‌های مختلف که ایران هم جزوشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/95819" target="_blank">📅 10:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95818">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d96e4bea9.mp4?token=WVbfjXjbACs-Ogq_b6vj03jvRkla7nvDahsWN_iCVNEJDChkEBefzQJDr5OI7fy8IioWgF_p1jmfu3Gl0xAXIXjqczuNAZfuS_FXohFHfPzAfAbg8Xqzr3Oelo_zE8L2U1J6nmBfEfYfUMCdgWs6FyODe0UJeMzQkn6mjQle__J4VeYu6W2Z8v7c62b6t7zJVsH60aqGUVtZSF8SRRbU99xaUEwshaJLOCtdJm_PJCuoFyjDkf3B4Vkb7vupu6_fVMHRBoVjjlSzN0Nni7IlLb_pxee9CNKa266w7K4mJ1_vaX9GsP0W0OK53TSQsSV21QWj_vTu8zHmhkcfbDI2n515qRhPQ5uEdGu-FKQWqAra1CN4YzMomnc_BAhe8Eo5E5_oVDmbrN9U-qKX0U7uu3Ek7384045LKJqPCM4avs5umg35D6MN5z6tiLv8kWwERIbdttRNE73Biu7DnxiPs5wMaNy63NNSmaOaDS2usx2Ww7Epl8FY0ZkUtt8GSaod67tdt4WOBhyQ4Gj_SiQ_Ksl6maEA1LEF7R02uLGKcj8I3UammAWDMS3EMZ9VZkb1XdmtqzNHYlDTcyQFtTNPaNLnJEStCIfTF19Xh0D7K7UKvgJYUXZnL_lcYnS2yVK6m7bvYiqbrpQp1LBHJyuyPb4_qewGDjd1XC3Xhx0XYXo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d96e4bea9.mp4?token=WVbfjXjbACs-Ogq_b6vj03jvRkla7nvDahsWN_iCVNEJDChkEBefzQJDr5OI7fy8IioWgF_p1jmfu3Gl0xAXIXjqczuNAZfuS_FXohFHfPzAfAbg8Xqzr3Oelo_zE8L2U1J6nmBfEfYfUMCdgWs6FyODe0UJeMzQkn6mjQle__J4VeYu6W2Z8v7c62b6t7zJVsH60aqGUVtZSF8SRRbU99xaUEwshaJLOCtdJm_PJCuoFyjDkf3B4Vkb7vupu6_fVMHRBoVjjlSzN0Nni7IlLb_pxee9CNKa266w7K4mJ1_vaX9GsP0W0OK53TSQsSV21QWj_vTu8zHmhkcfbDI2n515qRhPQ5uEdGu-FKQWqAra1CN4YzMomnc_BAhe8Eo5E5_oVDmbrN9U-qKX0U7uu3Ek7384045LKJqPCM4avs5umg35D6MN5z6tiLv8kWwERIbdttRNE73Biu7DnxiPs5wMaNy63NNSmaOaDS2usx2Ww7Epl8FY0ZkUtt8GSaod67tdt4WOBhyQ4Gj_SiQ_Ksl6maEA1LEF7R02uLGKcj8I3UammAWDMS3EMZ9VZkb1XdmtqzNHYlDTcyQFtTNPaNLnJEStCIfTF19Xh0D7K7UKvgJYUXZnL_lcYnS2yVK6m7bvYiqbrpQp1LBHJyuyPb4_qewGDjd1XC3Xhx0XYXo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😛
🔥
تشویق وایکینگ‌ها به قائم‌شهر رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/95818" target="_blank">📅 10:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95817">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c1bc7f4f.mp4?token=qxcLWlPBPYUCp9CzaMOTRElt8ain5uUlmvBO0BuuKf7XyPgtVAu8-44o0yJmGzJ58DFfpQbBSGHtGccEH9eLdSUv5MqnAD6DTIn6ifzujdvz0WYWbxWcUQ9TKhO8ye-EnPQoppWLVyPgrql2e9aNKtCYJuMTiM9HS0ED_wOFONZ3MPilcuU4SZicTVcoWgtjgQtvq_6A4gFfjcvNdVqz4eSGOMeGSiFA897sRfu4sPySIEBDz28AcYcDYJiPs17b82r51wUwwt01tQcKuQhuoGmh2TebPqL1zn0GDTvkCQloChM1n8wOmA-uKnTbEYhWqfH-p9qql1FNBx8QTgB7bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c1bc7f4f.mp4?token=qxcLWlPBPYUCp9CzaMOTRElt8ain5uUlmvBO0BuuKf7XyPgtVAu8-44o0yJmGzJ58DFfpQbBSGHtGccEH9eLdSUv5MqnAD6DTIn6ifzujdvz0WYWbxWcUQ9TKhO8ye-EnPQoppWLVyPgrql2e9aNKtCYJuMTiM9HS0ED_wOFONZ3MPilcuU4SZicTVcoWgtjgQtvq_6A4gFfjcvNdVqz4eSGOMeGSiFA897sRfu4sPySIEBDz28AcYcDYJiPs17b82r51wUwwt01tQcKuQhuoGmh2TebPqL1zn0GDTvkCQloChM1n8wOmA-uKnTbEYhWqfH-p9qql1FNBx8QTgB7bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لذت دیدن لیونل‌مسی در جوار دوس‌دختر که ما ایرانیا ازش بهره‌مند نیستیم
😔
😔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/95817" target="_blank">📅 10:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95816">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/434fc842d7.mp4?token=haE_97SEcp6sLlWiuxOdlZBvRwsjdoj64eCATvwLgnPONylAmaHfE5TPB2Or_YbzCkZaYEBbxNCg57G215jpel1McSsnUZgDL7L03mL7y4Xw5B7vTNg1RHOoJN72mdIUgL26hBcE0CkyI-nUgMVs85XfJ17fp3yOc4BgAkk6GCm4O5pU8Jatc4K72XR0fCm_5nFba0JOlrDHdV2E-ZzMPutUTaF4b7aQivTkQ6Hbs1oD3LQNyQKqVI651VtNGuW9yWknm1221qk9VJqBUukoFK-D3OgYo7KB43RSEDtsnjLaXbnS1dJ613FPueGV3gfaRiad3YUUEvkv_MG3PYtSQx63DPK0OI5oiv7WPPReJSQecjwmTpaG_iM8jAzChKiwK3Y46gkX6GY-UbtRxIoeDhMCqSFh8ulkCbhtRcz7FknUJqV8mi3yiexYsFBnHvY63yx3ewR_8qXvN7OCIh_mSZ08go3_D6Lqjjy-1mnpu4Bmg0EZczireO-npv94nY-TIfz3J6kZpf1d5-Fe6nB52AcU_-z9dK4oQ9Ba4UM9TtWF_x34JpHJTQ4xPWc7qBQ-tVT2-vhtgAIRCfT_GAHhaUG6KYtuN_StWqjiXdSL8vf_KGMl9OTZKZMBndmi6fNjrPBHN2bi9-__c5loph_NbvzdDfHSiAcgpEvGVCJpS10" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/434fc842d7.mp4?token=haE_97SEcp6sLlWiuxOdlZBvRwsjdoj64eCATvwLgnPONylAmaHfE5TPB2Or_YbzCkZaYEBbxNCg57G215jpel1McSsnUZgDL7L03mL7y4Xw5B7vTNg1RHOoJN72mdIUgL26hBcE0CkyI-nUgMVs85XfJ17fp3yOc4BgAkk6GCm4O5pU8Jatc4K72XR0fCm_5nFba0JOlrDHdV2E-ZzMPutUTaF4b7aQivTkQ6Hbs1oD3LQNyQKqVI651VtNGuW9yWknm1221qk9VJqBUukoFK-D3OgYo7KB43RSEDtsnjLaXbnS1dJ613FPueGV3gfaRiad3YUUEvkv_MG3PYtSQx63DPK0OI5oiv7WPPReJSQecjwmTpaG_iM8jAzChKiwK3Y46gkX6GY-UbtRxIoeDhMCqSFh8ulkCbhtRcz7FknUJqV8mi3yiexYsFBnHvY63yx3ewR_8qXvN7OCIh_mSZ08go3_D6Lqjjy-1mnpu4Bmg0EZczireO-npv94nY-TIfz3J6kZpf1d5-Fe6nB52AcU_-z9dK4oQ9Ba4UM9TtWF_x34JpHJTQ4xPWc7qBQ-tVT2-vhtgAIRCfT_GAHhaUG6KYtuN_StWqjiXdSL8vf_KGMl9OTZKZMBndmi6fNjrPBHN2bi9-__c5loph_NbvzdDfHSiAcgpEvGVCJpS10" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇧🇷
خوش‌وبش گرم اندریک و بوسیدن شکم همسرش که بارداره بعد بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/95816" target="_blank">📅 09:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95815">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8a29a82bd.mp4?token=EVRZXGd3H5Qnaco3ANcMrhtTLxLzZFp3nprsR81PvrEMzvO4wPOz-OFH3I9rh1xmboTXyuVBMwJrAjGMVrRjAgBlul2zvMOB2nIEZN413GuJkzy9l68Jd3hwb7SD6cUIn1JvXJR9pyWUgbNJOmDiQZJgtTk0pa-SzihnjZ_UoQ94NNyBuBHp5BiChI2r9RTSCocXrJe7gblLraNcsT9RWItzCYS6JztWjtLUegD7xjpGUcjDLQKkn_Jn_kvTskRauVbKLRkqkjifDjUdBr3AYr406ZM5gM3T9-YtEiuQN2mA_PqyjOytn-kuMrQZAFz0p6REi90sXGl-is9iilH37w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8a29a82bd.mp4?token=EVRZXGd3H5Qnaco3ANcMrhtTLxLzZFp3nprsR81PvrEMzvO4wPOz-OFH3I9rh1xmboTXyuVBMwJrAjGMVrRjAgBlul2zvMOB2nIEZN413GuJkzy9l68Jd3hwb7SD6cUIn1JvXJR9pyWUgbNJOmDiQZJgtTk0pa-SzihnjZ_UoQ94NNyBuBHp5BiChI2r9RTSCocXrJe7gblLraNcsT9RWItzCYS6JztWjtLUegD7xjpGUcjDLQKkn_Jn_kvTskRauVbKLRkqkjifDjUdBr3AYr406ZM5gM3T9-YtEiuQN2mA_PqyjOytn-kuMrQZAFz0p6REi90sXGl-is9iilH37w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
سلیقه موسیقی میثاقی آپدیت شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/95815" target="_blank">📅 09:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95814">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0ec300703.mp4?token=na9PGCq-qTELb6JEaDlx4zXlAZk_GbYyKmSH9EyGAtR6a2bqnqgioxrczdXTXFEWBetCCVA2oojUVdRgLDAvUtbrwm3w6UZJm-Tt1dj2ftbCgEOyvR9CD3eEKqejHwRbBxdnjQB7S4fE_eRYwfWwyFe8LsVUsSQlKmQqarQs-3Tgv_T4843tZVeEcrlQElXua66XtsiGSKSctk2SWeUfiOmTO8IQNNrEOaySaiycneePm3Up8mAkwEsxfwxdcQ3eVKzZ4ehb4ncgUQ7RK-RhznhfUO43rLPMtmpfpNfKX_F3NgvkonVKCHt_Iopq_hKUQ-fpbt5nNajurWkwHZUuvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0ec300703.mp4?token=na9PGCq-qTELb6JEaDlx4zXlAZk_GbYyKmSH9EyGAtR6a2bqnqgioxrczdXTXFEWBetCCVA2oojUVdRgLDAvUtbrwm3w6UZJm-Tt1dj2ftbCgEOyvR9CD3eEKqejHwRbBxdnjQB7S4fE_eRYwfWwyFe8LsVUsSQlKmQqarQs-3Tgv_T4843tZVeEcrlQElXua66XtsiGSKSctk2SWeUfiOmTO8IQNNrEOaySaiycneePm3Up8mAkwEsxfwxdcQ3eVKzZ4ehb4ncgUQ7RK-RhznhfUO43rLPMtmpfpNfKX_F3NgvkonVKCHt_Iopq_hKUQ-fpbt5nNajurWkwHZUuvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
✔️
🇵🇹
فداکاری ویژه کریس رونالدو در دادن کاشته به نونو مندش و تعریف این ذهنیت از زبان هوگو آلمیدا؛ تیم > فرد!
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/95814" target="_blank">📅 09:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95813">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClE41-DjOb6BQTekGmrPBwbsR398Q2Iejw5dYMRGepOlaLrCUWyHjL7VoemwvaZFF7skXi3SSgQbYSdb8Cjs1SlkZNdSgBwqtCnjNlPbNvoVAdnoBALgFVFL2q-YF9h5ZH7qsh6CcxUCQGgU33A-HIDozfG9fOKxN_Qnmr1q4g0yO4rXqOmPFE8mqI-YdXJWEHJaOIwGVF9ZLAt6hYoJYcniGr8NBU65Hi5H0VXcUTfFvsxQsCnZc8Xe08qFCVWxKD0mArEcWiUb72OkFv-uaAR7Gw5Fz8G-5o58uSJIcR_VAJP6OUllQUvEQAZZ-heLx5-tEyuHE-zJBNlqPUNIKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
نمودار درختی مرحله حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/95813" target="_blank">📅 08:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95812">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZsOvQjeLwxyIw_1jjumWrQ7SbKnGZ6Dnxpyz2J0P2Su2evGXaeXkHBjB2rjzQ_qQ4R7L0mLr6QZzY8_6pnmJKvLxBfIHagJdbObEORnPaIvFD7KXtBaA9JfVUWyLVqFlZtVFxKq0rwo4SAfKeGG2YO4QSbjpDTFSKUH_OENFxZHCZJzrmyCZ_6VxGjKl8Is_3-YkkNhbtPwSjshyHUjJctDWpd0iyzta7SL38cH4iR8XEu10wbIJqy98DEz6n3vsqkXDvB4e1JbF5D3Xt_Ra6s6FlkZgGKVhqC3nmb57wxspGBOu6IN3f5YTSwNRqF6NZiUAIQ0fvH1h3_VZFcooA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌بندی گروه A جام‌جهانی؛ در مرحله حذفی، آفریقای جنوبی به مصاف کانادا خواهد رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/95812" target="_blank">📅 08:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95811">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUB7HqnKAbhLOM4Gy6nUJ8FwP9oXda7A4NXglLzsw8ZTrLpX_t2Q20m6_HUkp2FDOGktici-EYYgzOFHMNKmpi_BVH97nv9AeUgs-n3TftJTyl20RYf6bHNVk8_UY8qU6FnkepB6wuRO1dgT9449AHc4pCF2a6Ll19Wr3WY1E53Qvs3iPnopYoEspDofi9MEm4udDno-oRqzwJUR2uTiBp-dfu3JP_n_l0DZI5PfJa7jDMmd3pA0KRrdS0NXZpd2KQWYV5waZ_QEwj67bEhwiSLmVVdeF7KB6d1AlXY62mz2c6Ui_czPO8XOqH9ebehoZqnRdRf5yYVFIkIwlYu9bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌بندی گروه A جام‌جهانی؛ در مرحله حذفی، آفریقای جنوبی به مصاف کانادا خواهد رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/95811" target="_blank">📅 08:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95810">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پایان نیمه اول بازیای جام‌جهانی</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/95810" target="_blank">📅 05:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95808">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rkMR5g1VExs1Wt99Yrf491dCqpJxBCrPssYX0Pvt5fZK5UZGEJLy_Lznp_kOoU0q7Z9xW9ndVs_rExbY2OaG5HJbrIjZimRm2RkHeby6f8Nm6XTAiIGhAkvxmyUli4jA1va-7uPMtDSHKjH9-Okbyj6fvDEIkT-_ok9LQ5kUk-eLY5ERCjCU9UnHZCHXHPPwQ_npgVLiWQQYq86V7ihlnugmsrvdvlX488lxYt3VK4TleWx-OqBuossR40qCuRFPt1KHwHdaLdYrfryhKzShK2l5hf2gray-RB2VjdKzleimjcUF_-YyXIBrEQK_EbTz3ZqkS0jfj4_wp9LRCWLgxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VTyYAVBP9twgI8uylpB7wQduEb567xqtCMyd7g-CDUl7bpVLzgdGcXC1Yn5Old8lF9Z5ln5w8leff2I89q0535y5awAyRTWxRHrYzycc-vYJ0YHN0MbRIfcRpBmIc8HPMqlYpcX61WSPIY-VZlzelF7YqkfHs1v-EYezKrQo5hDuaY6N2D9TXmmWNf4gWGFzUDXBQ3eGUDmPDn-x30nfRBHBz9WmwnDdV5z6gKrNshwcspdy3VeGORqKXex9LZOvFISXD58KGAf71WX1J-cJL6mfWvRFohcwyFc5ITBtBuetCvnzFFAEAMkhqmoKypZVvTI5wW4EmeUsCOueuhNUzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
👀
تعداد گل‌ها و پاس‌گل ها در جام جهانی:
🔹
وینیسیوس : 5 گل و 3 پاس گل
🔺
رافینیا : 0 تاثیر گذاری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/95808" target="_blank">📅 05:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95807">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdKVBSbAElphcIO_X9anNtD28bjAGKYOUK5HdZyXTco_Nd0R6L6BYIZaemFvd3cLUhcbLx2t6v8u51lYW8kQUTEHU_X6idjbj7iQhuI-afQcSGzJkPW2TMKnBjxrQcTXwrZO7T_AkdHLVys4tgUzUgjjuT4jO5eeEpx4kV2-NVWb_uDo-9YZ766jLqQLIYQwtpINLrDqf1Gnkbvntt1zzP-3ol_IrOzR_4tOrQkJvlWs7lRBi9hoGuyRvtoNyl2B6H_Cc8ZdRGyu2AyhZozlXPQxHR3SDjP5-XwNt2JrE1Y0FA4uO2nDK-wqLV5867jEbRx1TpgC3mWMbm8o-yLR0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوادارای بوسنی راضی از برد؛ ما هم قطعا از برد بوسنی راضی هستیم
🇧🇦
🍸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/95807" target="_blank">📅 04:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95804">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T5mZReOFLsF-SDmnkr8MBNff86XGezcqnGVi5o7mHcVyBIOGmEk67kLRdUSv3PmrlLzIobMHmcUp8Hk7d-T_kz6OqQ5qM1XpUCr_gG6t7vVVu35cEvpc8OyPWyAe4kxwAjMVNrFTVOKwxzISfS9-VtnM0udAwa_gLgh4N1FDaYkBaZ6TFphlc2xqObnDmddnbfjWk79uMDXWlvd4IJ5B3_Zn5SXeaTX-gE8dvGXp6anrHRjSuVg045hX0z13qXV-Qot6K9a_PnYX8pcZ2rzJ0a1Dm1VBDD0-poYuaVPELKD7DBKA8OXBEWPUUi0Pdg1WgBcjNme_2DkRM3BqFbOvkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MBpJIfhDsUPUnoGqbzg5P2B3gtC99XIxnOKRpser8zbP45djWgPzkS5ACnbka5opvczzIhEKcNZfUWXL9O5xmEwm0KuRdr5LsEXay7fJ_I7PoH9z26FvhpJuW4V_hSPC39d6onxjzzz1ORGoOvx5Nn2KqVahmapYRp9bUUg1YHMRtFmaOhb_Vw4I-9ord2cR6E5YST9hOi_21yp5e6oaEMkKEoy-xLa9VCGssoDIufTpH6OgqtUaAFc_9d6mZ8bXeB8VtL3-Ft1d6VGZQLbQGAVdbevgnLYIQY4KIi8ol1LuINcX7PCNqsi15L2U6WJSLhCFHTMzE-z8nQw4nySu6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I1SmGtdraCDhPpwK9aWrgMtidsCqwkvh_KXi4URMIndNDctu9BvHNd7hkgnEA_VkfdSQWbrXM0asqeAMpIjxsiv0HBSH7g4IvJ0t3AVjiFDUC-pjmIwawD5wvhzzKDViNx7EyUqwnr_XFmmgaw-SFDMSK_6D30ciKtF4i2JC_bO4PYjI1ppmJC7KHWAG-HwPGM_oQ5rMUiBDJz9m8U6HM4scaK8Jy-TsGVBXjGCI9sgN2ZILxqNrDeXawsSwDqeVaC5Q0XuMXB46jEJzANHXQ-pbpqj1sr6vlivQ0eF9v-6W-0ib4ROjsA2ZiGTrxbd3oqx7N9h4meGZNOAygWe9Vw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اشک‌های نیمار بعد از پایان بازی
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/95804" target="_blank">📅 04:46 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95803">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">شروع بازی های آفریقای جنوبی - کره جنوبی و جمهوری چک - مکزیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/95803" target="_blank">📅 04:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95802">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BerGDO12uN_sAFvPV1iXkP0w2xhjXmaVZhNu4o1MUEYXtVgE7rRcmvcbLFa5hTC-5fxLnyIiTWhEKFYVEeS3ebzZJJjog9naVWMu_jF-4t-nRjDRkmqe_pfAvxA-cuFLQblWgrZNmP7zcuKgVM0QUrGSeyemYWI1SNvaffDlGDF--BnywmrTH2LrTI3jl0z-55GzMr3Ikn_lB4cv04h3dyIXngLx60IjGYyQsX6RnlFqtel3TFdQkWe4VdTuGtpMsnVpPOjfCioncQzIy_V7BxNcrIA0owbLjV5xLOVxAohDRx1G1DEJBSsht8r05y_kOV1qvuOCAAef_h6oyYUqQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
وینیسیوس:
من به آنچلوتی قول دادم که یک ضربه سر بزنم و او به من گفت این غیرممکن است و اگر این کار را انجام دهم به من هدیه خواهد داد و الان منتظر هدیه هستم.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/95802" target="_blank">📅 04:13 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95801">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlSRH_HhjL6gr16LRJeg4JPtWuZYmaTVS7HaCa55ktdnzw1mz42sfMQxZnK78GQk-kcjGuBUKl0_A7hAxcabUS9vSXx7jgQ45wtkW_DljDXlz8CdsCDBLbdm6lcheojzdqBln_qAfmb-2lMcKmbTwn0dxGKX_a6lRTC2fwGaHPkJzby89JQEH1fr0oubsGD-xB0iZGMXSqDU9iZViowVVNnBXiiwGYZap20Ho9Q-MLlTLDq7wSLHziApBS1UatImZhdD58AMW14CGHGqUVPFOGAK7dIMuLGPx7Y4Tz1bRcwF1bnu7rVe6Z-tpv02687CzBZP3H1RimzOipUIZSp56w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قشنگترین عکسی که امروز میتونید ببینید، نیمار و دختر گوگولیش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/95801" target="_blank">📅 03:56 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95800">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8jumoAdKryGQRIciE61OcHhpypNbCnCL4cNrnqjSYBp9J_OWz1-qf9nl-gdyhYdIH4ROWt5C9byjJgxFmQmML_ycWWvOWbNXhgl5ZlnWXlnMAzW6AmZy1AvlEsp0mzaTty5TPQJLUiQQLKWNlBuqdKa2nGFJSdcA0rF6AcVixYQo_rh7TWe3y9oWrpO6OmpmD1ZEdrP869rSZdxz-tXTCaJ92vaiacmijGtuem_BGorXKsE-twolyrTEA8SJBX7RBcjq1xuPX9SY7nwu8mvlwkpfTDbwfYo7cX4uppJ8_KiY3vzDogtZXTIf-qkiWwVRrrhd0OEU83DmwndsYFqUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بوسنی رسما به عنوان بهترین تیم سوم به مرحله یک شانزدهم نهایی جام جهانی راه یافت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/95800" target="_blank">📅 03:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95799">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKMEU5jmMUuymN4zualKtMD9u7Moy27xRzCzlu0Mhvdv_wgDKNpQq63Bgd9HqnY4GXdm23Bz9XbP91AroSj8Vv2HLywruTh3B_FGKxKCV7QJVqUyYqWXLhkHwNnPFh94_ad72Ke8Z6AUY7xUGdsy3dNj216Kp9PO3EGF3KLOuFZyyRKQUEyzEybd16Ogju_YV9b-O0GMAqGPSiDIzxrsudOv9hnDzt-31x49qaYY8qrF6dsOU8bUeCGljjrZPhHhJ59e3KSAdca2eyfXrP1fVQxxShk1zciHJlDezj6COS3WSpTqqRbgvTIDfXrRPLaLZ2sYOdG_2idgBYVKy_zDfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این دوست عزیزی که روی نبردن مراکش با 2 گل یا بیشتر بت زده بود 3.6 میلیون یارو بگا داد
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/95799" target="_blank">📅 03:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95798">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELZL6fKiAeJsJy8xZV0ujHSU83EB59KgAoMp_uabPZ-iwgTiZrd3gkemQJZYz3uVWNPIrN8o6TPgMsqtEm4ib-3PUCYWZS0rf9ly9fB00-9gEvbZgSs0BJ5GzLjM2zrYGUfNe8G9mbF4wcTelFLcHD-b3l72fLmtiSYlzkzHuFTFNcf3BUagPikCxL8P044RkIL0if6jM1UrlzNW3hValI1hWM3Ru4paKqxQZd55SxnkWrMSeYpzthCTEp66IrnwXdwjIWLUUVCoxlVXFmzBGzmqdRz1ELTcMMw36f0zrJomuHG4XbgORR1MEjPx0NzLPedpbp2glRqOpIRUn3rQEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
❌
نیمار مقابل اسکاتلند تو 15 دقیقه 9 بار توپ لو داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/95798" target="_blank">📅 03:44 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95797">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkflHDD-gLgMtaV1gBhrfuqaKuZRPuvctVTp6ZPXmWgaSol7pwow7h-8aZX8vrUobY-3QCpx49wkNVa9J8F4WvZizAA6jFaDfA7En_F7SbRzkAVhgCxgEITrIG9uvwlcKxbupoZIX2WEAwlVdMCngOHORRKzfLJ-wT93jdAGnUMq_7vkwKIF4s2M94tWXzot-nmoLpVhaMR3yQCY5ZBbzc-6zx2t44f9d9Y02RBD24ogCvqmPSiThIVxgdQuAAnVqLFkb0e1Z5fv_VO9LFudrslx4k3xJA3ljdyESj9DGM7Uf9BZIMIWiiZ878sKsNO6zcf6tVWK-EYGDsL76lRTWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تیم ملی مراکش اولین تیم عربی است که دو بار متوالی به دور دوم جام جهانی راه یافته است.
- جام جهانی 2022
- جام جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/95797" target="_blank">📅 03:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95796">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MuxERI24h_UwEukaqrzITTkjBkWnm3IpKnIzEipECNJ5ZTe1ORpAnnvPV4PAkysNwGqYeutMXfJaFqfXctwCL8Xu-Vbj8cC-0HjllbjkVmceOjC8McbvkcGZwnwagcYRCDFgCnuGB4C4LJxvWIe-qhzIfdYcLMII23wstx6zMdCxAiW2TEzbfc7ARYESmMZBH9rcX11q0hxPpivPt1H7dPkkX4dmW2r5BH5c0McXrPt_KeewLwNryWeRW0PWnckm6YZRlsZNE-3WsN2Ur4o3q-o2_M2mWWMaEkuhc54_c2wp0LeFFg55_yE20NGdGbwSxYmdBj4OhJyc5XINl11W_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینیسیوس برای سومین بازی متوالی بهترین بازیکن بازی شد
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/95796" target="_blank">📅 03:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95795">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLPoHxZBf6Nj34Ku7gLECMwukinAO-SX6BJDIz851mH9ybR9iHEn6LxOalV2fB6DaO5LFDqwqr-ZzAMZtqsxWlBtqjegDZT61VSCux-eWca22Pf2uFjWaPQ4r59BOKq5EZCox_fa2nUUtFfbqlfsccDIWSlD7ISgRuYcq1TsCBxgJH_bxyTH67J-ek8h1kwim75W7EvK7HZ7yEzTjw-GfPHm84WnwvGvVXbk7rWwNVjvRaecXgZfl8E9mZitB7-IXcPqxlY3U9Zs9QbydiPwM-9dCtWOcNBV0paCPQw_lI6xWcl18ipHzWRZ2ZnMNsDu5pcKy9ObrojsJXfh1SlSqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
جدول گروه C جام‌جهانی با برزیل و صعود مراکش به عنوان تیم دوم گروه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/95795" target="_blank">📅 03:38 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95794">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8FXg5a4R5C92l8IPlXvdwPQkMl4rB01CtP5fYw0lRM2jQdHyouxPk1ru1rPLOYwg4ZqzT84tKeoN4cs3F6c-uD7aJ43bxmR95YlDIaYPEffuBhrgvKKW3I1cvAH2o-lV8lFb9BfaXsEDQ07YZ_qTA8qn5Ycvm8NhPIbvO0cXkQclJj8hrrRhbNoaw4KKaBuK38iCefGDbpLddY52MQLw-ekaDKmy0f_8oDuoEndFh36r_b2_BS5n5X0Hh9rGEfjAXCrYo2Js7xSQJ5_DegvQUrRd6o8bj_ChMuuRiRL0VN0M4PE9qtMOKB8vD3HBoZxuvcLvsTzaPOqbvEVJuvv-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | کامبک مراکش مقابل هائیتیِ حذف شده
🇲🇦
مراکش 4-2
🇭🇹
هائیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/95794" target="_blank">📅 03:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95793">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUpWbtmgFdgEYPZOnvJ6-7dE1_IXQ4Z3V_azmieZ9-_FVAba_8pb9LctuQ1ZCH3oU2T5GsWVl8spKEPXN8CO83uR0HcB08r94K_oNJpMw9aFNkxszMHRdyKn9jn9TTInOhssc41l0W-LpBlXWYjW9EcYKt4gidfU9mbNcMCwivxglmO8rcYhwe0c26MWOQ5_joI8BKl7rdxZBj7GtrxjEJt_dFXE9f9eT3HMCyEJAdgwiqkLsetRiG3ie9wfIRP7EVcUmahwNI0HYJMwbquQZHPtHfR4vFmVNT2rRBQXJCUvYyr-toLrDAWiY_pnvP3OI-8VSDz3B9UrVWvdxYPtiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | برتری قاطع سلسائو مقابل اسکاتلند و صعود به دور بعدی
🇧🇷
برزیل 3 - 0
🏴󠁧󠁢󠁳󠁣󠁴󠁿
اسکاتلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/95793" target="_blank">📅 03:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95792">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMwRnmOtRz1isaq97n51bXFQUW4Jbo5j-bM2mfDUPBo_Q_XHw6dza7efpJalPoSS_AdHz91GEBHhAs2VpXBRnXuOOZ9dOmWIKFZJu8JkhRw-OLipZOOg1hxEG9JPVjLHAIb2yfObn_CQzXaYYG2W8looBQowsgUmOm3AaxdLqOHwSYZapdSWdi_vz22Ka7SFaTXmMOQ6EI1p2QBeFAJ0GM-LYNdziA94OO-kk6ypLScjpvzz-s6JkTMgw9WrtVeNtdaiCdIGWMNCA2KkQj1GWKs6oMgaLfZwByX_FQWXvc5gsyzL2Ys9mtnDp6oH9CNmsJIgymUDVpIVhahF5m1TDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
برزیل رسما به مرحله یک شانزدهم نهایی جام‌جهانی صعود کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/95792" target="_blank">📅 03:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95791">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/95791" target="_blank">📅 03:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95789">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sdKWMUKD-xdIovUtGxNzr_rf3CsGtshXs9RKN8nU76tScQOXLtPQbQELTZihqXrL3U1ZLckGFIy7qlUS9vz3pbFm6JCOA-_VNBgRUMG1LRzwlcthQwUoj24tMCtfs4yCZczE4H9yiYgf9f-MAwnOGhNmmqdJIQbwFMlt4-YVIsyaH8Kg6ESVgE9Hd-MjREiPa6Tl5NP3dALFMggpnKJUZ4VOQ35-w6v1We0kZ_-s6eSwbqspVGibCngN1f6pAvYESZKWwREHe_y-Kzkr5PEwapq4BoLTet_9e04EyCTIo5fksZn4xBuepdGPgcoF6oVlxVJw87v155RwK_Vkjnlmaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bO25MOIUifB9yL4gHMV6_2aV9oUKb6p1Jt-caJTEHnuXsGLaNZ50op2AyaVUsTp7lEt4DBgDHL4fswuh326dU--c-5KyR00TMMBTpUlSVenC5TYNcl5QR45XVvKSrEQJrQzDVSO90WBZole05g1dh2z5O8WfocEqgTUQJnNFpEaxWLKWMPJm-dztE6uAl6yU_3aqh0t341m9rWsIuVJql2NRkq4bwAcdXJiZpoddVbcxmuz-fV04FGW16KL9CqTIKtzB7952-vml-urarEJzSYv3uobNPWLItqUotWOE-6JkWk9KmVvcaRh-E-KY6idRK7eh5paMC-7VnjLXvhQYFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇲🇽
🇨🇿
ترکیب رسمی جمهوری‌چک و مکزیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/95789" target="_blank">📅 03:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95788">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3Xin9NaDlUntgGMqkJHW3bfrc33Lb3jSXFKMWXMWWbTJGNBYyi9QvzdiUiWUHSReBCn4p-6VoGeByjHvDOpqvo-h3oQ0YzuVfLXjpDEoEDYuDGW3zj8RA1ldUwPCcfvJVwBb3P68OI5XZWtLOU00Twqz_1Asq7ctH_gGiLADdwHQjKbnraEJ0UTDx8DyOAJjU3PvVvYywTRd1LVlWJLv0sn8V-q2dh0x7xZA4FCD4Q7n_GMHypuFgk1clD9Vz5UEhUfmtJK6pBlMlWmgznTzkWV3e1erjZlOZz9kSo-dq-pDKxmauMJpf6Z0xBz9QrDbNqI4xFQJ7PeLT7AyQkmnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/95788" target="_blank">📅 03:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95787">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/86c7a40c8c.mp4?token=aoZoB4LSUHp60Mt3qwGak3IlEZi1_4x3eKqLfROgljB02HOFsP4ORvEZhWAXA55Y2hHGMWZCcKJW8b9k0H6-YM6ct6_VRlOXftGfwpK2MX4sGZNYqkL4U55DqmGtlkl5BqkkHeKbV442JHEmTgaYVxiR3gVdKr_uKn8pPpLSSnguKDl5qVojoa4suTZwCZbbZmApQlqpgal1yVDK1GO5DaHLrpv46SRVrBucxlFEuy3RbApHl_D8aGppIynjZEUGy8sVfJJpBsxbP_pfrlb8ll7b62kkq1MjUuqyVa6UBdKr_eMKP_w7lXd98ZEsbgaEMi3ECtAOPMFMZhOTRn46LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/86c7a40c8c.mp4?token=aoZoB4LSUHp60Mt3qwGak3IlEZi1_4x3eKqLfROgljB02HOFsP4ORvEZhWAXA55Y2hHGMWZCcKJW8b9k0H6-YM6ct6_VRlOXftGfwpK2MX4sGZNYqkL4U55DqmGtlkl5BqkkHeKbV442JHEmTgaYVxiR3gVdKr_uKn8pPpLSSnguKDl5qVojoa4suTZwCZbbZmApQlqpgal1yVDK1GO5DaHLrpv46SRVrBucxlFEuy3RbApHl_D8aGppIynjZEUGy8sVfJJpBsxbP_pfrlb8ll7b62kkq1MjUuqyVa6UBdKr_eMKP_w7lXd98ZEsbgaEMi3ECtAOPMFMZhOTRn46LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل چهارم مراکش به هائیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/95787" target="_blank">📅 03:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95786">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">مراکش چهارمی هم زد</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/95786" target="_blank">📅 03:22 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95785">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اندریک افسانه ای هم وارد زمین شد</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/95785" target="_blank">📅 03:17 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95784">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fbcdc6d3fd.mp4?token=SqlXJI5MuHymLzEg-tP1aMzwWBVUryyATZkI1F_D5fk2BIt7lvFtubJr6Ji-xnef_C9WkhAonzxypLlyu_T_Ohyq2f-Y3l4rKuBLhqKhUrE511qpMTgodNMrmmB3ZZGbo0oj6zPq8cpyFD5yVjlBtD-oh4QZQRR3BQBkYlphjwv5a83tIiGZE9PSrNLFiJpe3QOrjllE5hNK1_f68tSMTIHFuZxwhEnGHJzTAz4YsitVjXyEzqjf9FrCA8zSlJkYNsgwkEa3HMjbITnMFrCXKl3scaTWLCJ3cgaEKBSKSqHVmIrIaaEx3w3HddNdY05BSbjFtr5Sa6F-r4GMSPkfTw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fbcdc6d3fd.mp4?token=SqlXJI5MuHymLzEg-tP1aMzwWBVUryyATZkI1F_D5fk2BIt7lvFtubJr6Ji-xnef_C9WkhAonzxypLlyu_T_Ohyq2f-Y3l4rKuBLhqKhUrE511qpMTgodNMrmmB3ZZGbo0oj6zPq8cpyFD5yVjlBtD-oh4QZQRR3BQBkYlphjwv5a83tIiGZE9PSrNLFiJpe3QOrjllE5hNK1_f68tSMTIHFuZxwhEnGHJzTAz4YsitVjXyEzqjf9FrCA8zSlJkYNsgwkEa3HMjbITnMFrCXKl3scaTWLCJ3cgaEKBSKSqHVmIrIaaEx3w3HddNdY05BSbjFtr5Sa6F-r4GMSPkfTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل سوم مراکش به هائیتی توسط رحیمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/95784" target="_blank">📅 03:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95783">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">مراکش سومی هم زد</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/95783" target="_blank">📅 03:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95782">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/95782" target="_blank">📅 03:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95780">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/34ae550cec.mp4?token=udB4XT16ZFBD7Snw8CYClZZcSbgNHoP6OnkZMMsxS6nQl5fCDHs_EfbzLJjiWJr8HL_JRhmPqpXAnA-jQcRUK1aUl2fZfVPMC2rV0Asjg2TjP4m1Bz04iOosPbIoppY3yuoMvlu8pd_RZ6HCO4a9fbirBzHkJUT_haxp9gU4AtpbIdEg7Laoku6FxdrG8dLtnKHOOUAmnxnHERxem2w-LbGDaF6xm5sL-Bg37g6bFmujh4HGdt0ueCv6QW9sO_adVL-X1nU1TNJsvEV4_M9iMrHhChnH3E3Rt8OQOW-fIm9bgB_YvoF9J0n1A3bNy5D7yj76ZyICQk4DDddFQIpq6w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/34ae550cec.mp4?token=udB4XT16ZFBD7Snw8CYClZZcSbgNHoP6OnkZMMsxS6nQl5fCDHs_EfbzLJjiWJr8HL_JRhmPqpXAnA-jQcRUK1aUl2fZfVPMC2rV0Asjg2TjP4m1Bz04iOosPbIoppY3yuoMvlu8pd_RZ6HCO4a9fbirBzHkJUT_haxp9gU4AtpbIdEg7Laoku6FxdrG8dLtnKHOOUAmnxnHERxem2w-LbGDaF6xm5sL-Bg37g6bFmujh4HGdt0ueCv6QW9sO_adVL-X1nU1TNJsvEV4_M9iMrHhChnH3E3Rt8OQOW-fIm9bgB_YvoF9J0n1A3bNy5D7yj76ZyICQk4DDddFQIpq6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/95780" target="_blank">📅 03:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95779">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">نیمار بالاخره وارد زمین شد</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/95779" target="_blank">📅 03:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95777">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gXlxMqNTRxNyuMn7aUZUcdQhvszFI3BZI8S-pimmSTOpCQbhE1Skcuv1fsCwFzsZ15eTVIwaQsjbVoKSPwY_lmtbXwofpohIc5CBM8MdlVKB7kg1EClxbaKonKey783UzyA5xJ7huFz5AtTi69rbey_WsYsC7doWx0La-MNhRL2bC2Tv12-7q-hjyZiz0ieO3BxjyU19rbcgI0oouyXUR_MiubwvORMsV5WeJb70U55NWYnkgG9TGZ2-c9f_dYCSMOAkbTwH-impsFyY9lkSRBO7F2LJjoAH8UtFGhQl-DqhXHtF5GY3ZIiyjM4mOk4aY0kwsCuB20zKTJV8IYb3Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tqsyc8FyP10E2TuipoApFMcce4JaJyB5wYtbBCEeg05T8WN1za3sVClwIIF_eOn4c2cXGTfrhJTAl3wHfeJXbhAMPLHBRXvdY-k8BArbjv_azTrn0YdozK9hj019Z8jpbY3QCb6dd88ZYepBYzykQs5v8CBsl_U6-0-b62J80hRWMhtM829f6T5UObyxkDYOMC4gCM2WZsOAOVabTgbyWZ1ysZEgG_9NudsniE8XdbR8K1SbG9Md2xyOnJFqE6EaJ1ljmDvBvGZTRgqJ8rIF8kWuvWdtJqR0B7MzaV5KNYBJA-nPh-durdbyvwAHqbNZNwgR_YOpSR8ZFk_kTciBhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇿🇦
🇰🇷
ترکیب رسمی آفریقای جنوبی و کره جنوبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/95777" target="_blank">📅 03:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95776">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxOWGJvslnOqhClwiePuv-KiNZYmrCZBKr2UO3UpHqEsULL1p5FCGPqc1_8x-Re4t6jl9PHMnbPvI4HHGpamnlBqhrdadmB6nV_co-u-jG7hfCXIBYRv8wrWTBs0oc7nwmTvu6_Desjtx5FL_Z6DyV8lDbRJlc1rwZbQgjBxSiuLQrT8BamKVC6V7Po-npL-ks8Z_q2LLEb31aTAas9zNdUpaQWX_mtuPtJd0QjsWXGP2VNau3JUbWgM_LMmGMv5GxtoVlhVaSHfMzASlvKjDVqRPyqd56RQA8y809ngupVI-UzWSG83M4gJRKzvjOmdldxVsegDIDS4vLbGDnxdHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرفدارای برزیل تو ورزشگاه
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/95776" target="_blank">📅 03:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95775">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/97d7c9274d.mp4?token=FXQHA1TR1mlhR2mQL8upPRbIlUuZZyts1SWuJ0y-P7S3XOVDIKYaU0lIogXVVVa3PsfMujPlqLdH0f1TiWAiS6whOeo1sHvVxx7gzsX25JF13Qk3sKLEeDXh6wnjUu5RYqIhMb-TXUq7zwdnPvAAzXT_4Hbi7PsPB4KmQlayPw5knKojXAcGVFnwtfaJFoinIoGEV4O94tNA3BPRnk-roWgXed2znwlG7GzKWa968KnZtIyL1Mo0-Ft6nU_uTXDgJmmF8nlOm27QJABKx5mlSECV1V32FqHCjQRQBkygWlfk9YuJ2Oj5OS9VJyXegzgBjW6UZ44sHXilx41LbP4ffkHmGaz3XOZ4AjHyfAjXEdIw7QuNb6sQb97Q3fsRsXoGR3FRqM-zYjZwuzUejD9x58c8hygW16qLbI3MnTNMmGXeX6h3HKm4vj7VUu3UILxNkGN2f_xBh77V3saif_NbwOr4o_9QY8YwqjTJT2Uml3fe-VJMJszz1q8papC7mSLQpzKSJtngvDr7vxRL3DXY_GpbJJooEaGbINeFXaroXxl0AO6OlTK0zI_8dLhqOsE2a_XPztFm9seQgnKeJrUaoZIH8xwtfnJEOL0mjNL5EMnr8S6d9g3HASb7FfqyRwPbhli6xGfQZ4bHjEHeXa2VJOVWYytAGWFym4F5wOw09TI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/97d7c9274d.mp4?token=FXQHA1TR1mlhR2mQL8upPRbIlUuZZyts1SWuJ0y-P7S3XOVDIKYaU0lIogXVVVa3PsfMujPlqLdH0f1TiWAiS6whOeo1sHvVxx7gzsX25JF13Qk3sKLEeDXh6wnjUu5RYqIhMb-TXUq7zwdnPvAAzXT_4Hbi7PsPB4KmQlayPw5knKojXAcGVFnwtfaJFoinIoGEV4O94tNA3BPRnk-roWgXed2znwlG7GzKWa968KnZtIyL1Mo0-Ft6nU_uTXDgJmmF8nlOm27QJABKx5mlSECV1V32FqHCjQRQBkygWlfk9YuJ2Oj5OS9VJyXegzgBjW6UZ44sHXilx41LbP4ffkHmGaz3XOZ4AjHyfAjXEdIw7QuNb6sQb97Q3fsRsXoGR3FRqM-zYjZwuzUejD9x58c8hygW16qLbI3MnTNMmGXeX6h3HKm4vj7VUu3UILxNkGN2f_xBh77V3saif_NbwOr4o_9QY8YwqjTJT2Uml3fe-VJMJszz1q8papC7mSLQpzKSJtngvDr7vxRL3DXY_GpbJJooEaGbINeFXaroXxl0AO6OlTK0zI_8dLhqOsE2a_XPztFm9seQgnKeJrUaoZIH8xwtfnJEOL0mjNL5EMnr8S6d9g3HASb7FfqyRwPbhli6xGfQZ4bHjEHeXa2VJOVWYytAGWFym4F5wOw09TI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل سوم برزیل به اسکاتلند توسط کونیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/95775" target="_blank">📅 02:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95774">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">کونیااااااا زددددد</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/95774" target="_blank">📅 02:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95773">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">برزیلللللل</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/95773" target="_blank">📅 02:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95772">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">گلگلگگلگلگل سووووومممم</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/95772" target="_blank">📅 02:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95771">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da82426b1d.mp4?token=HOiTD5rxBw0m8ocD19s_70Nq8MJyR527HW7k2mJf0Fk6gVbG-gTSxHZ_W2-ePttPFmbFUab5NGRpvG0Jv9F8awqAkm6IYJsRfftuHYlF5YyUAdDCkAd9NPhF8L9107Phlcie0U6tMzkJdraU4Mdv7RE18Vv2ON_hhVfoX229mOeE6ZZdkoYdzbOa5WGyfJMARF4v4TdDxsZrjffAFx_tiJcaNFbj4BkmFCKORGCR2vnZVDbSI5q1s0jtGAua4Tc4S1OjUSjToBSEwGn2rE-ayEkLq-cPYe6YaiBuPGWBSCR2qaPj1SiqzLashBnJj34mwIShJdIoFRcJXqoaLP-M3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da82426b1d.mp4?token=HOiTD5rxBw0m8ocD19s_70Nq8MJyR527HW7k2mJf0Fk6gVbG-gTSxHZ_W2-ePttPFmbFUab5NGRpvG0Jv9F8awqAkm6IYJsRfftuHYlF5YyUAdDCkAd9NPhF8L9107Phlcie0U6tMzkJdraU4Mdv7RE18Vv2ON_hhVfoX229mOeE6ZZdkoYdzbOa5WGyfJMARF4v4TdDxsZrjffAFx_tiJcaNFbj4BkmFCKORGCR2vnZVDbSI5q1s0jtGAua4Tc4S1OjUSjToBSEwGn2rE-ayEkLq-cPYe6YaiBuPGWBSCR2qaPj1SiqzLashBnJj34mwIShJdIoFRcJXqoaLP-M3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
پشمامممممم زلزله رو ببین ناموسا
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/95771" target="_blank">📅 02:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95770">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb072de7f.mp4?token=r6Wkjsvl_6EFa-Tm5Sq0nBU3sU80Nhc-nzzKkuN5_MOoOo49ukGRpSd9AGjZqh5GJ-LocvDYL6wJRifkSXPuMSPg0gcuAPmmGuDS7-vvIuobvkHU9iL1LhT5AXobSLuNlTMohXCqdk4EoNKpXCq54QlnBPvMqVM7x-geKTBESNEbZBENs8TkCpTmLfCABV9k9ZHrOlr4qLruJEpf2boYxsNQljVqf64dGSxn-nfp9dnutVgfzgn6P1eZXaLD4Ck_qElg3_DDItCbQNN0Ji1c4ws9JLMKQihKnMvb9ZuiL2Kw6gOyf0g1Yp6tLzF-vCyhpbgwkmM0Nto9tQAKRRWsQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb072de7f.mp4?token=r6Wkjsvl_6EFa-Tm5Sq0nBU3sU80Nhc-nzzKkuN5_MOoOo49ukGRpSd9AGjZqh5GJ-LocvDYL6wJRifkSXPuMSPg0gcuAPmmGuDS7-vvIuobvkHU9iL1LhT5AXobSLuNlTMohXCqdk4EoNKpXCq54QlnBPvMqVM7x-geKTBESNEbZBENs8TkCpTmLfCABV9k9ZHrOlr4qLruJEpf2boYxsNQljVqf64dGSxn-nfp9dnutVgfzgn6P1eZXaLD4Ck_qElg3_DDItCbQNN0Ji1c4ws9JLMKQihKnMvb9ZuiL2Kw6gOyf0g1Yp6tLzF-vCyhpbgwkmM0Nto9tQAKRRWsQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
تو کاراکاس ونزوئلا زلزله شدید رخ داده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/95770" target="_blank">📅 02:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95769">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">هوادارای برزیل از آنچلوتی میخوان نیمار رو بازی بده</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/95769" target="_blank">📅 02:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95768">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">شروع نیمه دوم بازی‌های امشب</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/95768" target="_blank">📅 02:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95767">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">این آدم فضاییای ما چی شدن؟</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/95767" target="_blank">📅 02:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95766">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqOJAM6PYWDqSYHDDT5ZrZz_VxZ3cSmttnyXIUbOJoolAgOBL8G_kTBthpCqfXHR8R7FXA6d_7eJFpxviXMx_5a_aTEd2dWtpfGT_BT635j-UhEsdbabkzsi_AFJHbSlPLllcjefGJkJfBRTmROFVQS_c8arFdgoo-FfgwOjvaT10bwudBknPYbbqgk_ORW00iR_l24A9deNP_PC8baVGI3qmR_pIjZt1y4cPMbbS648Nhaf_N3Zlncar7skjs1xszDox_jDvB4m-OgXiwfO1QX_SYNIuXnnp3SB4PtApVS85ALIHBwRbcs0OauNNHtkZk4RJgktUcxQhi3gyLTBxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
وینیسیوس جونیور تعداد گل های خود را زیر نظر کارلو آنچلوتی به 97 رساند. بازیکنانی با بیشترین گل‌زده تحت هدایت کارلتو:
‏
🥇
فیلیپو اینزاگی — ۱۶۱ گل
‏
🥈
کریم بنزما — ۱۲۱ گل
‏
🥉
کریستیانو رونالدو — ۱۱۲ گل
‏
😀
آندری شِوچنکو — ۱۰۳ گل
‏
😄
وینیسیوس جونیور — ۹۷ گل
🆕
‏
😃
کاکا — ۹۵ گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/95766" target="_blank">📅 02:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95765">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRdyW3X0XIG4ZvE1LVYLWjA4nn8d9GN5JGQt2DJo1DWXhnLRKVL7UVlmKToopR_8zvKQHj-opIvA_JjsuZqYimmMkNfkncw2P8FkRUkN4pZB5cWUP92SC1BsHVSPUVTKHm7Rel5G9Bj6hVC_jb8S8uX5eEoAlb4x2KFjDH_DT1HyuKVvU0jsrvJVQGaI2jUCrsTkRQ1y2iMkQe95M8_n3cpZn3QNOrpFD67qv81cYSytml_ilXm7bUtwj56gUm90NXDAublXD9OA4fewGSph34q7h-Q5mV8zZlTlWvVeaadssyUBwknl_y1otZkqtISYkl9YNyRejkNrXCX-ukAvZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🇲🇦
عملکرد درخشان اسماعیل سایباری ستاره تیم مراکش و باشگاه بایرن‌مونیخ در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/95765" target="_blank">📅 02:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95764">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FaWGWH5VcPfnMshe2jN3KwjEBdX4Rm7Op8vl1-2R_PPLRlk3V9YWtrgrt89d5Z3RhSzwmmjkouhtTOlYi-9ZHzFMVe24vK2mAvES7vcw3-zgTqizqb_Crr42ihQXs5qH-trAeSd-DJlqE0kM-EP8ajp5YXd9j6GBe-CT3vkPCHHmKhxncDQqHkI0zIrz4Mv04xIWjJ2MV7ENpnGLi1PEJ_cV-Yz3BQC3f3BZ6AGWTItnGOF1i3wwxzJEBernnxOulJLz_7PLxQ3nu9BEhNQChBeJNmsSz6vWrEH-rtYE4DKXWS-ApgoJwHQEi1Gt-V8YOWLIFxaGyq_9szE2dsKorg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینیسیوس تو جام جهانی 2022:
• 4 بازی
• 1 گل
• 2 پاس گل
وینیسیوس تو جام جهانی 2026:
• 3 بازی
• 4 گل
• 1 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/95764" target="_blank">📅 02:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95763">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/95763" target="_blank">📅 02:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95762">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Yb8nyVFz4nlK7ec4b98cMwxJcZLjFKG5eNFo11mZP_E0A76hKzXIsEbReqorFGsjtmL-ZE7ojZsNmfpxtEEn-jwLr7gjl-zuIaA_cvoejYod3HlWC4Isnk1ObWlDM51iSdCo6RH85f_urIOpp5tjQ0MVUY4FJIKft0mY-lyyB7quZ96QwBjV8p8z6Dt_QKM0zWL2-c7PnMvKy2XHN5iK2pLuOYdWecJw19HgU2Aup5v48vhAh0qWxRTOv4tjxZqPWEsmnII31ujBc-U5rdubsCeHjuW_Q2FS590KuqIkroKqz3oRi05r57eLk1bwDllET9A4CCOTvmCpRqjf0TcsKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/95762" target="_blank">📅 02:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95761">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">پایان دو بازی در نیمه اول
🇧🇷
برزیل 2 -
🏴󠁧󠁢󠁳󠁣󠁴󠁿
اسکاتلند 0
🇲🇦
مراکش 2 -
🇭🇹
هائیتی 2
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/95761" target="_blank">📅 02:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95760">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/62fc82ea80.mp4?token=TTQEZdkRHmpAYm_FEVZSwytiFgekGIAv550uCUl219rEJdsugsLen-U1XIPlhoZLrpynAfuenUuJzY09tBjO3_epzEv5zyuO-o2-esIVyAa6CHNdWz_KHnUyNJ4TxtPVe7eiWbol-8W4lLmMC06-RgtELQ_YtXWCuwJk8K5D8dZZOP3rseDUKIMEmCQ7Si1jw-0dCJ613ymZsnksH5EApfPpp8lda7AG7Mz5qpP84s-9ImrVT1eIXB8dRN6PK5KIAK6Clq_r8Lq5qnsIcxF3-sVEXob3XHD5N5La4vwZD5pV9MH3UgKY57Ql9N9Zo4HCO3mYf8-wj8DEuEer2nBZaoPD7O0QzG2hL-USLFDu3ypuMAbgshwUq2pbuE0wwUKjOV59qXsAh1PktSBOOR2Wwzw89TwhcHMzzSnQUycjzN7ecY5_ogPRUUU8PTw1sMmOxxZDlv3GlinZSncach2PznvYVrpv0wEVqsF7vrkGs_-eJB2nJ9X7OhbdAS77E57ZLhSCszFzoA1NABxY2ONOT1lVjQ_3MfqNM5XYwWGJF_9dbweoQi3Uyn_9gIFaD1z1FS_ypwVb3TgjHC5lbc6fIaNq3gcbjjSDtD9kWtTwn3E9Vg3W3iTXKYMaVMbrg4cDq8-_MfBTai9PqF1owgxqsouTgOUP3A2SSAk6gvnOe6k" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/62fc82ea80.mp4?token=TTQEZdkRHmpAYm_FEVZSwytiFgekGIAv550uCUl219rEJdsugsLen-U1XIPlhoZLrpynAfuenUuJzY09tBjO3_epzEv5zyuO-o2-esIVyAa6CHNdWz_KHnUyNJ4TxtPVe7eiWbol-8W4lLmMC06-RgtELQ_YtXWCuwJk8K5D8dZZOP3rseDUKIMEmCQ7Si1jw-0dCJ613ymZsnksH5EApfPpp8lda7AG7Mz5qpP84s-9ImrVT1eIXB8dRN6PK5KIAK6Clq_r8Lq5qnsIcxF3-sVEXob3XHD5N5La4vwZD5pV9MH3UgKY57Ql9N9Zo4HCO3mYf8-wj8DEuEer2nBZaoPD7O0QzG2hL-USLFDu3ypuMAbgshwUq2pbuE0wwUKjOV59qXsAh1PktSBOOR2Wwzw89TwhcHMzzSnQUycjzN7ecY5_ogPRUUU8PTw1sMmOxxZDlv3GlinZSncach2PznvYVrpv0wEVqsF7vrkGs_-eJB2nJ9X7OhbdAS77E57ZLhSCszFzoA1NABxY2ONOT1lVjQ_3MfqNM5XYwWGJF_9dbweoQi3Uyn_9gIFaD1z1FS_ypwVb3TgjHC5lbc6fIaNq3gcbjjSDtD9kWtTwn3E9Vg3W3iTXKYMaVMbrg4cDq8-_MfBTai9PqF1owgxqsouTgOUP3A2SSAk6gvnOe6k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم برزیل به اسکاتلند توسط وینیسیوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/95760" target="_blank">📅 02:22 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95759">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56d87f861e.mp4?token=NuvS5DBGQzc3iUJ_LC1owm8FdG5kr3mLBvqGfyrzFRIUIKa2xlAFOpTL36Q3p1V_3y1qdD8nUe5ecqbFG8r7PWdOzRLICwg0tzIKuKTJ8QVL_uO5hXrhnKwi96CoxNiiMJU-CT4XRYIqRYBnTqDykYspKH_lBbMYA4duOrSrWEX9YZdqnj3B9V0l9N2FWtfiNRJmdZhlunRCJbe3X1-w9FU7TAaBCuZ8EWIVi3JBC9hO-ZPHUUhxwNy5Y580iJzZDvk9zwaRsn3jBajG47wNTtSWL-wm70yJ0HHN7YXboaCr6-szjRGWgBG01hHUrqmU-wwnLFQWWLH1x1PkKpKGCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56d87f861e.mp4?token=NuvS5DBGQzc3iUJ_LC1owm8FdG5kr3mLBvqGfyrzFRIUIKa2xlAFOpTL36Q3p1V_3y1qdD8nUe5ecqbFG8r7PWdOzRLICwg0tzIKuKTJ8QVL_uO5hXrhnKwi96CoxNiiMJU-CT4XRYIqRYBnTqDykYspKH_lBbMYA4duOrSrWEX9YZdqnj3B9V0l9N2FWtfiNRJmdZhlunRCJbe3X1-w9FU7TAaBCuZ8EWIVi3JBC9hO-ZPHUUhxwNy5Y580iJzZDvk9zwaRsn3jBajG47wNTtSWL-wm70yJ0HHN7YXboaCr6-szjRGWgBG01hHUrqmU-wwnLFQWWLH1x1PkKpKGCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم مراکش به هائیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/95759" target="_blank">📅 02:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95758">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">وینیسیوس دبل کرد</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/95758" target="_blank">📅 02:19 · 04 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
