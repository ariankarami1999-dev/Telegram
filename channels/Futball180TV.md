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
<img src="https://cdn5.telesco.pe/file/pDL0E12lylfR7sm5ETUI21Ip7F8QQKI51pFHdy_ibHNW578jEdUeyJM-eKHGqnJZUo3yn__hSIR1lXA9BMTVBnZAOGR_Y2Sx-3waRg3SMzm9bysaC0QiBq3u8uO5RqpUmW-NJVc1nOTmFm35fnojqYuueAHE7laFLbuhguPkZxpYKjeDfWAb8XebhC3XyFc2wNOtt8IKqtIIfumhZXnOquL8bxW1Ys687WkKEKbA-G4jaQQrC9rXQPyYddnKIqQEfIhrTpBkik3vRS-cCDplYxPkwmvKscbkzkQrNlwY4rFEvI41h8TN4_EnwxyeFG7kDKI_TdEHLFAtIcA3l4jtfw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 385K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-19 16:40:45</div>
<hr>

<div class="tg-post" id="msg-108343">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dG0qJvueh3wjg6sRxuxxhY-I5ewDX8qm72hlV8K5FvybPZeyfyA3rTwMpXqX14TaeAkJohI3x_1zp5hc-c3NshVNIEEUzIJ4VQsZIL83uMQIx7sgG9PrjDLCtaYtqMTOb-ZWgd1DfJKk7Z8Y-OatkwxUPjlyL5O4yH-3BImk9arm5Y1CsjEGpN6bO4kPRMNSYU64S9itX2C7DyeQYRroIJRaDW-cdaGI29C0svIxmnSk3M0UtWbamQlBTsPsfIEljjsrqNo8sexA4owenGzpJFSWMjxu6-Ec3w5dIveRxwaVSTKT0V-ySXWr1iHojr-YmdKK7DktCqoVjRO194lBrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
با اصرار یاسر‌آسانی، پزشکان استقلال تا ساعاتی‌دیگر تست پزشکی از این بازیکن خواهد گرفت و در صورت بهبود نسبی امکان حضور کوتاه مدت مقابل الغرافه وجود دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/Futball180TV/108343" target="_blank">📅 15:56 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108342">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkhgCnF8dnpnyOc6lDgrvEtNy4Kpcj0q6acG0SdHPQgSmdpV-J0rtafZaMWNXBy2slX7cRzyR50cQcMnH2EWPRs4Vo2gfvEvaSika2DGxBDdGetq2mmr9Q_a5phPOfFiz9QXJi-hmhgKLURonxejKcRCzxqAY6HFEcYYZBMRKUiThQ0TDK5-fkc1rzZ2iNLR70N2VSzU7M_7k3BoaGyz0CHrpua41QFXU-kymENRNTRjY4uKY4oKUpra6zXH9RY4SfZjpYJYVVWseZJi4UO6eWljMZYtqVehOLty78bYsHb6dBnJLxXePNVkMWP6yCnQxbBQKh7EI6zs4VtfAHYyNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
🙂
وینیسیوس جونیور: من فقط قصد مرتب کردن موهای بازیکن ویارئال را داشتم ولی نمی‌دانم چرا کارت قرمز به من داده شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/Futball180TV/108342" target="_blank">📅 15:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108341">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bT2VNlNg-pK1c34UjdRZ44dtifmKKy2hKnccHE2a7EtBwPLkdXJs6OizjEo5UBOcwFAzRfQ1n3zZML9rnnLSZCUQjnMYUpQR7ophxj_yNFCrj_LaTA_UBQ8P02-JAR1-DN_xBYI6jrhtwz-Cb2Ba2s3Bfzu5jYEtQWEnF6ye8PZZwjmVcvTHQivLisMVpTD1TGmF3p6Ift2PsUjZKq7MzkgKHW6duuQHL-v4GR06CerSYF4gOec-c5CObystHmqqF970M57KfgiPahm4fmNLv0Upv8l4xJlGmAvDxbF6RED6bktDqHCbqYQ1V9Udtvm_W6aZjlkaoHyiEFnG9_kbGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
📊
آمار تقابل‌های رو در رو لیورپول و منچستر سیتی در طول تاریخ
🏴󠁧󠁢󠁥󠁮󠁧󠁿
110 برد لیورپول
🤝
58 مساوی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
63 برد منچسترسیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/Futball180TV/108341" target="_blank">📅 15:44 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108340">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10aaacd99e.mp4?token=XQNxR6SOMX6xM4wlHLf--Wf9eWXS5a9D-7ftFBTNu52UkFeRqHNwscFxS0ipULeFY4rpAi_4zS9GzUi7Zcw67vtudMVO0PYW9oM57XItL2f0XjIhKd6LZcl_K9CmqlYrk1S7dx1JieqWkbeJnqEX_E2BbEX5ahQzKP9pRaauiCAS7dKtSOxpswVyTtWJh_khjpsVF1ngADCsclZEbai1wOPbZWYsEVdkgfdoIn8Fej5aaLfplS5-l5Fv2z0WpUPVw7grjSUS-EHHZff73ORL7akBs2XWvqEei1gTzIpT-fWsjswHf71quIkLyJW5SjOYeme62Wdc48LoIJGC41nEIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10aaacd99e.mp4?token=XQNxR6SOMX6xM4wlHLf--Wf9eWXS5a9D-7ftFBTNu52UkFeRqHNwscFxS0ipULeFY4rpAi_4zS9GzUi7Zcw67vtudMVO0PYW9oM57XItL2f0XjIhKd6LZcl_K9CmqlYrk1S7dx1JieqWkbeJnqEX_E2BbEX5ahQzKP9pRaauiCAS7dKtSOxpswVyTtWJh_khjpsVF1ngADCsclZEbai1wOPbZWYsEVdkgfdoIn8Fej5aaLfplS5-l5Fv2z0WpUPVw7grjSUS-EHHZff73ORL7akBs2XWvqEei1gTzIpT-fWsjswHf71quIkLyJW5SjOYeme62Wdc48LoIJGC41nEIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
واکنش مهدی توتونچی به مصاحبه علیرضا بیرانوند پس از بازی با استقلال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/Futball180TV/108340" target="_blank">📅 14:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108339">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7ac5629ca.mp4?token=n1anh2m39FGLfmLtgFo6cb_u3CkIi6QRaIpfOHjjL4s8ik6HU4QTZz0wNyVDy5ClvhFy2BmgsdOslNRoSnDIRSVysDrjNs6ASviO6uJyvu4ijP6wz3NTqcl2AVI_lK1USm0QpM_A9zHguYlaDBYUGds5Xu6Cp-40U2XSPy8hZk9s6mM_HCIhvVFetDwY__v6q-8cumioUzlase7jjLkO1136cRH9pqe57s4pUDCOdfik84hYWPaa4Dbrjxgqm-zUMCXCnaTKJQs5GC2qrE5xb9PZ5R6dwKi09CbWhpUdAIwcR5TsvJ6nq1s_zShOVzSnO90T6OE4Y-noe1W-RXhbtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7ac5629ca.mp4?token=n1anh2m39FGLfmLtgFo6cb_u3CkIi6QRaIpfOHjjL4s8ik6HU4QTZz0wNyVDy5ClvhFy2BmgsdOslNRoSnDIRSVysDrjNs6ASviO6uJyvu4ijP6wz3NTqcl2AVI_lK1USm0QpM_A9zHguYlaDBYUGds5Xu6Cp-40U2XSPy8hZk9s6mM_HCIhvVFetDwY__v6q-8cumioUzlase7jjLkO1136cRH9pqe57s4pUDCOdfik84hYWPaa4Dbrjxgqm-zUMCXCnaTKJQs5GC2qrE5xb9PZ5R6dwKi09CbWhpUdAIwcR5TsvJ6nq1s_zShOVzSnO90T6OE4Y-noe1W-RXhbtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کنایه‌سنگین ابوطالب‌حسینی به ژوله
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/Futball180TV/108339" target="_blank">📅 14:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108338">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c84731f90c.mp4?token=MaWVN8IMKuAvAgOwqijKggApXwuQJhTZtPFap5KiYaevko4oq5vmNPCeF0gYI6KHBH-OxZHnxqfyJfG26qEMnGBek3u8DEX3V9UM_kVIVA4kyMq5vFENTz6rDwpI-eKC6lIdw8OJgjyd1u12OJRkx-orSa0zusHkaIGItXTqYDeRf1V5Fw2BNG9rw3OyWmEZY1mLxMDglUzGCj0mHxZaE6RoQYLtwiQt9_hgcV-4ERcmETZsfIRTGJrYcRl0pqicqzOmhlNhzxLgtrtPjMSYPCLccgWXivalj278Hz2naLmzVpJyE8aI0bwNpNQtHd8TfR4sb8NzbPB8X7yaS_FC1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c84731f90c.mp4?token=MaWVN8IMKuAvAgOwqijKggApXwuQJhTZtPFap5KiYaevko4oq5vmNPCeF0gYI6KHBH-OxZHnxqfyJfG26qEMnGBek3u8DEX3V9UM_kVIVA4kyMq5vFENTz6rDwpI-eKC6lIdw8OJgjyd1u12OJRkx-orSa0zusHkaIGItXTqYDeRf1V5Fw2BNG9rw3OyWmEZY1mLxMDglUzGCj0mHxZaE6RoQYLtwiQt9_hgcV-4ERcmETZsfIRTGJrYcRl0pqicqzOmhlNhzxLgtrtPjMSYPCLccgWXivalj278Hz2naLmzVpJyE8aI0bwNpNQtHd8TfR4sb8NzbPB8X7yaS_FC1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🙂
واکنش گلزار به ساخت کلیپ‌های هوش مصنوعی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/108338" target="_blank">📅 13:35 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108337">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbt-7Qyswj2KuE_Ht8w7X9pXVecBL4RX4UPM2MzK4H-usJODevYJaUTOuZI03GiAPFp8TNepQI26LBeybe3IYB4HJ2MQNlc1s-UqWYPbkOlHg7Aeys_klwnhcrEOjkQQzmfnR65bd1EzmVZfR_g0C_sWo-zLYSWtgjUXGunZ8NF_8m_TOFGBSTKLC3oItjzRYHqE2LX0TjiELdspGWn4msqFwPnz7FWd8V5JwSRbFo7rZr66FppH6rODyz70HwQ-GxVsjY_ko_icWKzMS92_cJFhJcBkG3jMv-8CYboSsc8eV5aj-t3GDvWSupnB3vX93ye58nRQOm1hso6HmSdrgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پوستر باشگاه استقلال ایران برای بازی الغرافه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/108337" target="_blank">📅 13:17 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108336">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392cea7f43.mp4?token=bk-M5Zs5TONLLnhovo2a-Mgh5EOO0BmxfINmt01dxe0laJNohCOAHYlFmW9cULJn4dsN8eJp1WL3qcpt0xDohrEktN5mKLcmyTI1X9xV4EgOxQIyLEdPM4PuUAunfPWt3KjN0IufUC25xVHID0_yBI9DQolghgzRazOimFw5kblTOAzsapFgaBqEIORs9vENfYep6sBIVO4wErj81JuVSUOB8RFsF4iK7IEgZc8s5xyBhFSJ9Y5F-2Z48dmbUDSGCTKM55-tPRP9yFCgl_puGtADhZmz_tRYtTdnJHMfWN8up4NmEa41XzFn8-iROiRU7yHjebZqgePfxUtZQlOnaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392cea7f43.mp4?token=bk-M5Zs5TONLLnhovo2a-Mgh5EOO0BmxfINmt01dxe0laJNohCOAHYlFmW9cULJn4dsN8eJp1WL3qcpt0xDohrEktN5mKLcmyTI1X9xV4EgOxQIyLEdPM4PuUAunfPWt3KjN0IufUC25xVHID0_yBI9DQolghgzRazOimFw5kblTOAzsapFgaBqEIORs9vENfYep6sBIVO4wErj81JuVSUOB8RFsF4iK7IEgZc8s5xyBhFSJ9Y5F-2Z48dmbUDSGCTKM55-tPRP9yFCgl_puGtADhZmz_tRYtTdnJHMfWN8up4NmEa41XzFn8-iROiRU7yHjebZqgePfxUtZQlOnaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
تذکر تند رضا گلزار به قیاسی درباره ایرج طهماسب؛ گلزار با تاکید بر جایگاه طهماسب به‌عنوان یکی از چهره‌های باسابقه و پیشکسوت سینما، از نحوه صحبت قیاسی درباره او انتقاد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/108336" target="_blank">📅 13:10 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108335">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8012d7509c.mp4?token=L6Q29dHBAPEyL1cAbK99V6mLL2SaFJ9bh1r4ZhiRG-dzHsgjJNFFt1E-X-eyPd4I3mDfEpE5WzwGCQTzX8soqdrQaw-KMACy1g6RThi_HEcdgpBE8aonPMixALG4QpgvR8wqX3Aog_g2qSJhsjLtVVJRf7UsUNEQES1wML-mx-qPSUl8dJU-O0OuGM_QFgdkDjuUHb9MSTihvmNdTA3Q4-kdAfiOf34gnLt7OS54UUQgGqntJKjLylt3_mfmZTvpc94g88-dccHMMABPrY4S8N0_aNoWtBjQOvzGVM8Q7ihDR6UbGbqzqaIszAdiBKe-44j45xsYPYQXMJWVJ9Ukcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8012d7509c.mp4?token=L6Q29dHBAPEyL1cAbK99V6mLL2SaFJ9bh1r4ZhiRG-dzHsgjJNFFt1E-X-eyPd4I3mDfEpE5WzwGCQTzX8soqdrQaw-KMACy1g6RThi_HEcdgpBE8aonPMixALG4QpgvR8wqX3Aog_g2qSJhsjLtVVJRf7UsUNEQES1wML-mx-qPSUl8dJU-O0OuGM_QFgdkDjuUHb9MSTihvmNdTA3Q4-kdAfiOf34gnLt7OS54UUQgGqntJKjLylt3_mfmZTvpc94g88-dccHMMABPrY4S8N0_aNoWtBjQOvzGVM8Q7ihDR6UbGbqzqaIszAdiBKe-44j45xsYPYQXMJWVJ9Ukcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وینی داشت به فوتبال برمیگشت که ناگهان ...
🙁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/108335" target="_blank">📅 12:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108334">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOrOvD1JIWfdr9zNglo-3XWNYmYglQ3qG1kpj8QbtqcirdfN2PwYknguNIWY2HnYv_CmP8_ArKgPqnq3dMFjk1SSozhrfYUnPX9vHvCn4D6vQbvARTTyzPxRXfsk335y6FX4Uz5O3QUmnayWS9CIFTmb6Y0CqTDL2U0c-sReEoVLmKtpl7ZoMfYpYfgkXuOMJMirMV-RmzZhhCSgIARtBnJB8_Kxfg03ZvZtebYhCZ8E4S-NqePvyjljMxkHzvC83Qq8P08kQPW63MkBkb2f_5t2Di_GJsfqmEo5_PnN5P3AZh72p1YIHSi8zA6VI5aDHeTJSk-LXB4ZizM7E6ZRuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇶🇦
پوستر الغرافه قطر برای بازی با استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/108334" target="_blank">📅 12:56 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108333">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
‼️
⚽️
⚽️
پشت پرده دستگیری مهدی طارمی و سروش رفیعی در جاده شمال؛ رویانیان ۱۲ شب به داد فوتبالیست های معروف رسید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/108333" target="_blank">📅 12:41 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108332">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f5ee05132.mp4?token=XfS8jmy7u-FUIs36Chhl2Bq8cCwxhkN1GrW6qrUdgG0wpNp2uf_JkLFdPj46GAynbrILxP_MwypgmaSJqI-BHwTxv2vUMGJIJlaoCs_5QQ1GBzCdBeKu6K5mZfOLqfqaJjPKA4Fn9n5B4jNv6tkBr6WgFCHslMJsRGFn0dERsOg01jvZiZpMDydGSkgTyufng1FfqF37VWzspUk12QuFg6eWsU_Ak1a7FLn_NEHcG2J5-8ZYMC4SEPa0NumKN51d72VImatRQ9UkaY6D5VgSfl_8SFimfzF0mdPfdUaTF8s7d8T8J6hla1yC20jq2vxv6dIxS9eoeLRRp24lyNimlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f5ee05132.mp4?token=XfS8jmy7u-FUIs36Chhl2Bq8cCwxhkN1GrW6qrUdgG0wpNp2uf_JkLFdPj46GAynbrILxP_MwypgmaSJqI-BHwTxv2vUMGJIJlaoCs_5QQ1GBzCdBeKu6K5mZfOLqfqaJjPKA4Fn9n5B4jNv6tkBr6WgFCHslMJsRGFn0dERsOg01jvZiZpMDydGSkgTyufng1FfqF37VWzspUk12QuFg6eWsU_Ak1a7FLn_NEHcG2J5-8ZYMC4SEPa0NumKN51d72VImatRQ9UkaY6D5VgSfl_8SFimfzF0mdPfdUaTF8s7d8T8J6hla1yC20jq2vxv6dIxS9eoeLRRp24lyNimlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🙂
وینیسیوس جونیور: من فقط قصد مرتب کردن موهای بازیکن ویارئال را داشتم ولی نمی‌دانم چرا کارت قرمز به من داده شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/108332" target="_blank">📅 12:19 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108331">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aae7130b3.mp4?token=GreshrBEiI8pumCOam4NL8IdZBF3T9ZmLH9uCxRqfTmM_zCVXVSw_Izs9rua-_ekQjfSMwQ7Fa4L5g1NfGg1jvzXpH3oDy_a_2KI3mGbeAHOChwDmhlByIJrCCkYv69uXZHtENUGOsGYzYuXj00tL1j9I9U57MXifiwwGx6MrTvTNDaynYZ8Bl_CxDapgK-e9Ga9ZYEnB8iO71wk9HjvWf-Y9FXD709WaJb9g25Xr3aIGHEQ_kOkRrocAGNGPxFmEGR5jcHCwXXar7CnDNi1RGNnjwKgitvPUFdOOtwrsPKjs9jEcYK-F4OlI2DJT9wYGUvklgvQG5_C0zKwvHp_QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aae7130b3.mp4?token=GreshrBEiI8pumCOam4NL8IdZBF3T9ZmLH9uCxRqfTmM_zCVXVSw_Izs9rua-_ekQjfSMwQ7Fa4L5g1NfGg1jvzXpH3oDy_a_2KI3mGbeAHOChwDmhlByIJrCCkYv69uXZHtENUGOsGYzYuXj00tL1j9I9U57MXifiwwGx6MrTvTNDaynYZ8Bl_CxDapgK-e9Ga9ZYEnB8iO71wk9HjvWf-Y9FXD709WaJb9g25Xr3aIGHEQ_kOkRrocAGNGPxFmEGR5jcHCwXXar7CnDNi1RGNnjwKgitvPUFdOOtwrsPKjs9jEcYK-F4OlI2DJT9wYGUvklgvQG5_C0zKwvHp_QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای کروس کجایی؟ رئال مادرید بعد از رفتنت دیگه پادشاهی نکرد.
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/108331" target="_blank">📅 11:55 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108330">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b24f4518d4.mp4?token=UyVqIaA9nMJe_9Tuw078q9zGeqCivIJrvwH66g2KItPvjMqxcy-TQQi0Y5BN3Rmn3wb7NQfcvnnUx6v17_Ac6sgVVPDGdBujhTYzgzZVdgPDgRKywtHq_35oqSMCS108p4UOCurT67QhHzDY80xcY91-xpIeYsv7FMWSwhPh6Da8ioqwJFimJqGNKwtkyIRB55j-PyigP7a6O0YTGW64nyqSlIpdmQIyUWTliiX3GVxV2lpD-CTwhBMUTwZMKNAKBdjr6gTuEMdKoiCMO55aeCcSsIWrK_sSOxnX8EUvkL7d2f1FcbskjS6ds3yZ1R-VNEOoeeAVkgHTSjR3ibYsqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b24f4518d4.mp4?token=UyVqIaA9nMJe_9Tuw078q9zGeqCivIJrvwH66g2KItPvjMqxcy-TQQi0Y5BN3Rmn3wb7NQfcvnnUx6v17_Ac6sgVVPDGdBujhTYzgzZVdgPDgRKywtHq_35oqSMCS108p4UOCurT67QhHzDY80xcY91-xpIeYsv7FMWSwhPh6Da8ioqwJFimJqGNKwtkyIRB55j-PyigP7a6O0YTGW64nyqSlIpdmQIyUWTliiX3GVxV2lpD-CTwhBMUTwZMKNAKBdjr6gTuEMdKoiCMO55aeCcSsIWrK_sSOxnX8EUvkL7d2f1FcbskjS6ds3yZ1R-VNEOoeeAVkgHTSjR3ibYsqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ختم چالش رو اعلام میکنم
🦦
🙂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/108330" target="_blank">📅 11:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108329">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eea953a73d.mp4?token=ZrpTwxiBytRLI3GFoWEf6v213mXynsPxt0Y89msXaTHSAE0TYbBm0xXTzoEu-zqoO7t2LbDa-rk_o8j0gXypFmEdophkZraZEjtPDw1hJwFwBSzI87v0WmMVDsJkzw_JN6CgyEjGCuKNVTZBK3qsjwgEYKlBwXLUY2F4423nI-sYqsh-AdpqESfjDL4YKfdiONdjKPFner2Onr7h0iriVMVjEcztvEVbtPfKHncD8G9EQKLguuziJTFmZzYBsa4pHphZ3yfHyXxn6p1t7gfHNQH_aPWSQxT-DogVD2dfbGxoYRME2ndNg_IQIUpM8NYUt6oOL-6tdrDVTtPd4YDR0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eea953a73d.mp4?token=ZrpTwxiBytRLI3GFoWEf6v213mXynsPxt0Y89msXaTHSAE0TYbBm0xXTzoEu-zqoO7t2LbDa-rk_o8j0gXypFmEdophkZraZEjtPDw1hJwFwBSzI87v0WmMVDsJkzw_JN6CgyEjGCuKNVTZBK3qsjwgEYKlBwXLUY2F4423nI-sYqsh-AdpqESfjDL4YKfdiONdjKPFner2Onr7h0iriVMVjEcztvEVbtPfKHncD8G9EQKLguuziJTFmZzYBsa4pHphZ3yfHyXxn6p1t7gfHNQH_aPWSQxT-DogVD2dfbGxoYRME2ndNg_IQIUpM8NYUt6oOL-6tdrDVTtPd4YDR0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
جادوی دیشب اسطوره لیونل‌مسی در اینترمیامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/108329" target="_blank">📅 11:07 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108328">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fad3757da.mp4?token=r71V1d4vprvPFBR4XtesKi-qePyu195U54LI1AAs5oiiP7P574CaHszLjutfPGUn87bjMp6Q-jv3Kspd4qHTdZWFP5DT4I-ChWxGpg5koXD_NTbJWvoM-ZaSun0PTX8SBal3aivSwsXxOhCmovy1jXru2LUWBqifcP2KBlLYGU5hji2IjYuYo4pCX3Y21fnRXu8HThZjys0WKe7LwfgboOEVk4PxilFQDcSNnGcjXQkVxYBHiXXfXPDGv7MSddrkTKXBERmuJFRJ8zJ9xV_oB_7DNimO3NM6o0TptvdIfIMad_ZE40p4nO0ggOgkBOSJs5lr4Zy2WKzZPntHLMBs4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fad3757da.mp4?token=r71V1d4vprvPFBR4XtesKi-qePyu195U54LI1AAs5oiiP7P574CaHszLjutfPGUn87bjMp6Q-jv3Kspd4qHTdZWFP5DT4I-ChWxGpg5koXD_NTbJWvoM-ZaSun0PTX8SBal3aivSwsXxOhCmovy1jXru2LUWBqifcP2KBlLYGU5hji2IjYuYo4pCX3Y21fnRXu8HThZjys0WKe7LwfgboOEVk4PxilFQDcSNnGcjXQkVxYBHiXXfXPDGv7MSddrkTKXBERmuJFRJ8zJ9xV_oB_7DNimO3NM6o0TptvdIfIMad_ZE40p4nO0ggOgkBOSJs5lr4Zy2WKzZPntHLMBs4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نسل یک فوتبال
❤️
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/108328" target="_blank">📅 10:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108327">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/108327" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/108327" target="_blank">📅 10:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108326">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZQoOL3CNIgUHF-U0fp44rDoVZoZney9NatzdKfM5zP7xcO7ZpgV2fJH84TvywVlznyvWXbFCGXaBEI8SIHv1a5-hwBTUecWsI23VT1FTY7BSOeWOKXGaRdhpxlo_WWSYx41WMKAQYtZtQgCFBzvElksUAvvjWQm7V_5g4VCANyZ3yua9GO3J2mKEPk8Gg35Alaxr3EMdWjzKh1ghlngPMKAe2mQVYWMYaVCaSStq5hTfN-90SP00E1sJOn3vj5-HcEwnICLx-Sb9LHwDJWvLfTWwVXUNiSPEjKUC3imua3rEa-ONV81EC-TgDge8H3pk6u4vtzjbo5AR_9Jts0uGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
ناتینگهام‌فارست
🆚
کریستال‌پالاس
اورتون
🆚
هال
منچسترسیتی
🆚
لیورپول
اوساسونا
🆚
راسینگ سانتاندر
رم
🆚
کومو
مونزا
🆚
لاتزیو
میلان
🆚
ساسولو
فروزینونه
🆚
ناپولی
یوونتوس
🆚
کالیاری
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/108326" target="_blank">📅 10:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108325">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxII3TBqq_yfTM_wK6QgMC6R4rwCYkcbohnQSPqTu7bDQTvnCgMYnq_wcqlY6NuSAzD-4uXmbI-jhAIDTWwUAkGBKVQBLduYIz0b2g-Bdp_IB0c2pdllIl63I_zjZnDkC8RlvlPZEsfJICeKdnsyz8CMbHLM4WGkOWm0CqhnGc4Uy9YY3pNFW2p9ogYdKPtfxRWObaM-TA9zBZhkBxvuCFtAW0-bi8cbO5GC1ga7l5t4jN9XisGym_1ImCtLSrdQHl2AtsUpF6bt4x9iPKBqatpiL3xak8494KAn6F1a-55yfUKmid-asHssOSbi5DLSBVf4MUga0Bf7iSP9mbNHSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇶🇦
پوستر الغرافه قطر برای بازی با استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/108325" target="_blank">📅 10:35 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108324">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd22708e12.mp4?token=lek-uwQOa1ey5-0VNkrAeKg0XhEW0uMsnzzG-Bw-KpOlLYfbd-jvPO97eqF3iFwqlII7uiNPQbCKi-mPyuT-FDJk5LyYpg5fdMGLbEtPgvGa3OgjgwPtRnc-p3DTfuZ9UQzurlb6nZRCFeBHpwBmri_Z9ZPiPW66KhU7C6UnhCMni0K_qQeWmt-1l6h1aOlqIsPyxScVJmFp7FEiMC3I2APoRRJdPoSyx46FN2oMubdaQD6J1BHOj1vkutfCH9wJ-6KtmNumb2KUKr7r8jlNQkRvkC1IRbWp4XmBod0VdPLiRg12B6I5r08METP0NLIk-gqX_eqSxWm1f2soX_L9TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd22708e12.mp4?token=lek-uwQOa1ey5-0VNkrAeKg0XhEW0uMsnzzG-Bw-KpOlLYfbd-jvPO97eqF3iFwqlII7uiNPQbCKi-mPyuT-FDJk5LyYpg5fdMGLbEtPgvGa3OgjgwPtRnc-p3DTfuZ9UQzurlb6nZRCFeBHpwBmri_Z9ZPiPW66KhU7C6UnhCMni0K_qQeWmt-1l6h1aOlqIsPyxScVJmFp7FEiMC3I2APoRRJdPoSyx46FN2oMubdaQD6J1BHOj1vkutfCH9wJ-6KtmNumb2KUKr7r8jlNQkRvkC1IRbWp4XmBod0VdPLiRg12B6I5r08METP0NLIk-gqX_eqSxWm1f2soX_L9TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
نادر قاضی پور، نماینده پیشین مجلس: تراکتور پرطرفدارترین تیم جهان هست. از رئال و بارسا هم پرطرفدار هستیم. کل مردم ترکیه و ترکمنستان و آلمان طرفدار تراکتور هستن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/108324" target="_blank">📅 10:32 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108323">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9c7bf0fb8.mp4?token=QhlSyFMwZFX7vDVFV87AHizn1IuVGJyFipvSUrvNOUUatzpFnpXAZgaGAx4VbllHtGcVsVO_8ZWH-Bl8QcuWHYok_SSyEXI5_uIpQWuH-DjZfyXwRHPxx2ZvVg8JoBUuMFoMd13urXZdB-r667hJhn_qNF2_QdKssXxloIHAH28OW333CGy2wQPCks3TlfrLdTXfCfAZepylgTv7YAnYBj846KAgJpxhFLhSMSV4MhlkmPMJZHzsRB84wPIhrWfzLDQQQ2kH9YC0t7me71WvNAsGlBv9FPKssG3tQfQ-Mzn9wJikClMVcBRIndDEyj7FHnwnPsafyKqMRJQUWRKLQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9c7bf0fb8.mp4?token=QhlSyFMwZFX7vDVFV87AHizn1IuVGJyFipvSUrvNOUUatzpFnpXAZgaGAx4VbllHtGcVsVO_8ZWH-Bl8QcuWHYok_SSyEXI5_uIpQWuH-DjZfyXwRHPxx2ZvVg8JoBUuMFoMd13urXZdB-r667hJhn_qNF2_QdKssXxloIHAH28OW333CGy2wQPCks3TlfrLdTXfCfAZepylgTv7YAnYBj846KAgJpxhFLhSMSV4MhlkmPMJZHzsRB84wPIhrWfzLDQQQ2kH9YC0t7me71WvNAsGlBv9FPKssG3tQfQ-Mzn9wJikClMVcBRIndDEyj7FHnwnPsafyKqMRJQUWRKLQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
‼️
بیژن بزغاله 2008 روزی 4تا رونالدو و مسی به عنوان صبحانه می‌خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/108323" target="_blank">📅 10:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108322">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
❌
🇮🇷
🇶🇦
با اعلام پزشکان باشگاه استقلال، یاسر‌آسانی به طور قطع بازی روز دوشنبه استقلال مقابل الغرافه را از دست خواهد داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/108322" target="_blank">📅 10:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108321">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🇮🇷
🎙
رسول باختر، کارشناس حقوقی فوتبال ایران در گفت و گو با فارس درباره یاسر‌آسانی:
🗣️
درباره بحث مندیت از آنجایی که این موضوع به منزله فسخ نیست اصلا نمی‌توان به آن پرداخت. شاید باشگاه پرسپولیس بخواهد از این سند به عنوان قرینه‌ای برای اثبات فسخ قرارداد استفاده کند که در این صورت باز هم فارغ از اینکه فسخ صورت گرفته یا نگرفته باشد، باز هم تفاوتی در ماهیت ماجرا ندارد. چرا که آسانی بازیکن جدید استقلال محسوب نمی‌شود و به همین دلیل از نظر من بازی کردن او غیرقانونی نیست.
🗣️
اگر بخواهیم طبق نظر فدراسیون فوتبال پیش برویم که مشکلی وجود ندارد. در زاویه مقابل ماجرا هم حتی اگر قرارداد را فسخ شده در نظر بگیریم که بدترین حالت ممکن است، باز یاسر آسانی بازیکن جدید استقلال نیست و قاعدتا نباید مشکلی برای بازی کردن او وجود داشته باشد‌.
🗣️
کارت بازی بازیکنان توسط سازمان لیگ و فدراسیون صادر شده و نبود پروانه کار این نفرات در نهایت نمی‌تواند باعث تغییر نتیجه یک مسابقه یا اعلام غیرقانونی بودن حضور آنها در زمین شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/108321" target="_blank">📅 10:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108320">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c33311a6d.mp4?token=YPKho9fFhdZfzCW8fAvRnk4WLTrqJhIkXxXbdTCb-oiY8Nna0Oj2rR_-fMWaiF2XdGZloKWqrn6bYs3ZfKNy5dLJSEEM2rvZ0nf_SzUTXqCx6t1Bv3_6NJa-Iaufv-8zHnRk6AbxPTVJLIEo62CSBlNDzp_vIzeaH-01jEr0yoHU_E65eS73SSgM_qAxOuduy1f6zVyTTLvxXZxw1h_4d-5mAI85g5XbITFY_ReBeOaIH7yDsrA2p8luzg4aPw59WnLp08wUuRpbHv83bWT3EoI8w2V39qVuXL3oFLDzOReRDVAmo8jp9Ne8nH5KgrhuFTywNFbfpOoyztFeQBGwOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c33311a6d.mp4?token=YPKho9fFhdZfzCW8fAvRnk4WLTrqJhIkXxXbdTCb-oiY8Nna0Oj2rR_-fMWaiF2XdGZloKWqrn6bYs3ZfKNy5dLJSEEM2rvZ0nf_SzUTXqCx6t1Bv3_6NJa-Iaufv-8zHnRk6AbxPTVJLIEo62CSBlNDzp_vIzeaH-01jEr0yoHU_E65eS73SSgM_qAxOuduy1f6zVyTTLvxXZxw1h_4d-5mAI85g5XbITFY_ReBeOaIH7yDsrA2p8luzg4aPw59WnLp08wUuRpbHv83bWT3EoI8w2V39qVuXL3oFLDzOReRDVAmo8jp9Ne8nH5KgrhuFTywNFbfpOoyztFeQBGwOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
🇪🇸
پاسخ زیبای سیمئونه به سوال درباره مقایسه مسی و مارادونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/108320" target="_blank">📅 09:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108319">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf0b43363d.mp4?token=Rs0sseDYA45qpdC08u8A5RySqriBxRfpJTRO06RLC4IGJoYdZeLzw5ASi4tg4iRdYmnzBCUZTu1Iu60Ou8-AV8cc-63Sv5qNGWAm-dBHbYkWvNyQmzlbs1IMc7WU12SEOa6LhPQgg6FGOwi_5H81OL9fQWFAQjamKyp8HRRBxd9v6Cbf_zDV-I5sBTiDoSrMErnd7UARr_rFWPipo9anIiZdlkV2ca1oiSspDZWo_1CvT5S5wn-dEy8XxVhkxlsSTR_Jqo7c-75tMO6LLRkJ7aiazvvI62T3uiuRYx7QPjO44s9aewMSX1vF7dmk-6kXcYIXYA8KqiG9mjLGwhizqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf0b43363d.mp4?token=Rs0sseDYA45qpdC08u8A5RySqriBxRfpJTRO06RLC4IGJoYdZeLzw5ASi4tg4iRdYmnzBCUZTu1Iu60Ou8-AV8cc-63Sv5qNGWAm-dBHbYkWvNyQmzlbs1IMc7WU12SEOa6LhPQgg6FGOwi_5H81OL9fQWFAQjamKyp8HRRBxd9v6Cbf_zDV-I5sBTiDoSrMErnd7UARr_rFWPipo9anIiZdlkV2ca1oiSspDZWo_1CvT5S5wn-dEy8XxVhkxlsSTR_Jqo7c-75tMO6LLRkJ7aiazvvI62T3uiuRYx7QPjO44s9aewMSX1vF7dmk-6kXcYIXYA8KqiG9mjLGwhizqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
گلشیفته فراهانی توی جدیدترین فیلمش از جان سینا اسطوره کشتی کج و قهرمان دوران بچگی خیلی‌هامون لب‌ گرفته و حسابی خبرساز شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/108319" target="_blank">📅 09:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108318">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf40f375f6.mp4?token=NO2piQbqpptF86NVhHoWEfzsLOT9XSBjPZ7E9XgSamySS6Pj-K-MNRH-G1kETWZy4Dk9DkKl5WVnCAIov2JiUgOkahm8xLIMulc1zH0hArofi7_VimVPEPrHVk5bvdHFvg--l6bhCwj75CA-Ol4q_tNQQ39RbRgeSd2Cpses5qWjLQ2OmgKe4L9x-1xWxLCJCLMPLFkkbUGHvvaWHXdVrQHr7r0aazbtuBORkRXTFe6TOJAZUhBXiglsJj_TADGJ79yBrPNOxX-sdTxGA-LteyTHrLjV6K1v-Sp2dKd8QMkGMqrQJg0SHbpyBZSVI4_GZRT3B34qKHLC7stzEiATfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf40f375f6.mp4?token=NO2piQbqpptF86NVhHoWEfzsLOT9XSBjPZ7E9XgSamySS6Pj-K-MNRH-G1kETWZy4Dk9DkKl5WVnCAIov2JiUgOkahm8xLIMulc1zH0hArofi7_VimVPEPrHVk5bvdHFvg--l6bhCwj75CA-Ol4q_tNQQ39RbRgeSd2Cpses5qWjLQ2OmgKe4L9x-1xWxLCJCLMPLFkkbUGHvvaWHXdVrQHr7r0aazbtuBORkRXTFe6TOJAZUhBXiglsJj_TADGJ79yBrPNOxX-sdTxGA-LteyTHrLjV6K1v-Sp2dKd8QMkGMqrQJg0SHbpyBZSVI4_GZRT3B34qKHLC7stzEiATfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
وضعیت هوادارای بارسا در این روزها.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/108318" target="_blank">📅 08:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108317">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/108317" target="_blank">📅 01:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108316">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/108316" target="_blank">📅 01:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108315">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Efxg--wUSExz0XfNXuQaNv3V8MiigM4UZ2AJ18gRmXdiY7JWaZlx991AlZd-YNHYqHdRKq9vYfF8_Qnq-QoQoQEZY9LGFga_M7zPHoPX7_Gn6M6AT6qPzCo1rMxJyQZhcMmRrmvdeI6Fri4xtz5a2Vdwp6pMKbz0FhW45lrvK_XduuLjjRZEi7drVtiVKMJyUBd6NQu2bmfEnvVDsDkT3FBAIAEqlvi8Y77YCr7yQLtN39MKZY4fT3fuhIqY29nXUfSLpiOMN1-7ynJF5HWaJI0vFQJyXke4kvuFMyQquFG1UdDNirVmzk9AXjx3iKHxRCWkMvnyJagwq6l1t3184w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
📱
وینیسیوس با انتشار این استوری نوشت: همیشه تمامی صحنه‌هایی که کارت زرد و قرمز دارد متعلق به وینیسیوس است‌. چه رسوایی بزرگی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/108315" target="_blank">📅 01:55 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108314">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWsNektcDE9XdJMkA71G3duZc4bPq5fE6b0Pqq4b7n4SHLbCeYd1xCv0j0U9KgI73bOh1czp5vU8Hos4ASsuUNdQbslR9znjGatgupPI5k5lYzOh4v_E_mRoyWwqDFDKfCdpXimWKq5NWVPBNi6C-A6zW62g9LRWgzd7qrBi3dW8N-rF6umMZqqjEzL5a8jEUDI9wTvXOwVOCEJ_wxpQIG9MSsponNZWl9HrZ5Z9autiStBnOqfENFHkqkgmEYLIcbNkLALwWukcTXY3wFtwxwovjwRqjvqZ1J6DX_HWDgnlwO5f9h_VRDoQ7mICQUOpj_Tg0HF6GDQPub_ECe2Ahw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🟥
#رسمییییییی؛ طبق گزارش داور بازی امشب رئال، وینیسیوس بدلیل پرخاشگری و رفتار غیرورزشی از زمین اخراج شده و دوبازی بعدی رئال‌مادرید مقابل سویا و بارسلونا محروم خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/108314" target="_blank">📅 01:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108313">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSfaowJ1uZbJKPkrTZIodPtlxzFYr2hMVnOEhJooiPHaNSZ_Tb8aGsie-UJw2zuy0lO4zb97BQU3nGp41qo4iOrH97I344ul7RnZ_a6th8uU5KVgJDiud-g4v7bRheOZSbWClwMbGa9KE5hlK-F2HqiT2xgI7nCL_jN9oEswhc4lpPv40iHSayzNTEXEWStoxV4UkxA-FrDx91HtNQcmn0JFLGv8_LNA0xhg4If1TeVXCD_XlRQ2llqehN5P-8INOz70lPU1JpSshD41nRrebkDEPC2XxVBXDt2XwMGxE4LuPRRnQFa6cDIbHpkbicIb-Sz9FVoBWb_Jwo1_TaI7kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
🇪🇸
وینیسیوس بدلیل حرکت غیر ورزشی حداقل ۲ جلسه از میادین محرومه و الکلاسیکو رو از دست میده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/108313" target="_blank">📅 01:47 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108310">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcXMkAKL2Itu0IBHwFArH94DpjkhwS0NTlh2f476sLHfmJH4oyu4mvIkjqRPHWRqi9l0kTSkIG2l9eIC26jQGAafTgj5h796BWveNo4vHP8B9wVeqv2ZndQCGHA0KXypiu0MOvIx-TpN8LhbP93WKTkdmprY-rXH2YkqqQd6fzkFaZywi14WaAMGgTjRZU6vq7VhDQunCTXZjsy5gBpuEN7rDM6rcpLZilokl9l3iGI9u1iHot6sN7JiuYTWeMa25iJ_VaIz34DDcV_Mt6Kfi62Pf6rsIK-Va7o5iMefiFHG3ajl5pbmgHqpB9TndQE5d5DsxQqKOr_nYjeRRoM5WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📱
🇪🇸
پست وینیسیوس در اینستاگرام
: من هنوز هم خوشحالم. می‌خواهم از هم‌تیمی‌هایم و هواداران رئال مادرید عذرخواهی کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/108310" target="_blank">📅 01:23 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108309">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVangJ-6_3b3-wQ-mZnSn4y7EncnN3Ge61su4Dchc9xRda3ibXmrRaHxHs3mcgS7RDqNwMAGu-JmXYN3nI0gJjDc1TPr6AtTmX0zbQ8XoSgK3v1chbg-PiZPbNv_gKsZWvAr81UM5-1MEYZelk7hNkHtBkVzg1RYduhIdHsEzE5vaG6JzuNhlabHjaGfYPfO6AoAYGCz2RSWhDoxO3CtAHI-jYc-DX3gi4wHzd4X6Kt_oLus5ky2n_o_-RcgyxUVwqIxHU4jcZXlVTQIhiaguFU4o_zrM4V_vEHF-B4Y7qmnsUYJ0MmCsnWBgnZ8FvUesMD4bZvghCjR0b9qOa7zkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇪🇸
مورینیو بدلیل حواشی مربوط به وینیسیوس و احتمال غیبت در ال‌کلاسیکو در نشست خبری بعد از بازی حاضر نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/108309" target="_blank">📅 01:18 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108308">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HH0MCfYU9jN6e-qf8WWE_4clrahu79_2ROjKayg98qTSEznerJCdTav6yA1ydbr2F4ry4jBUAcmGaWgUXt4IhV1_3POfywwJZ7dDCnQmr7o7drSyIu8QUVPB8AJ8-aJQx3dJDeMAuuFBCklFlxChXX32km4Gh6v90GaNiJ1QIDgzohr09QiS1Ir12DdB1kBPhwHjWM94QyO1o2vTbfg4Vb7bkmtKu8LEMJBwaQrBEkMQVNfrxlbfb7G3hPP1NMl10Eh2urjyUSxx71uo5ixd7pb6X4fpZsViRJszunL8rmgPVkOGd-qKdT7FwrcENM-JkYDJLO4VsnoUpWnEDSBhtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استوری رودریگو بازیکن رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/108308" target="_blank">📅 01:17 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108307">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
پایان بازی با برتری رئال‌مادرید مقابل ویارئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/108307" target="_blank">📅 00:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108306">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
بلند تر فریاد بزن نگررررررررریراااااااا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/108306" target="_blank">📅 00:16 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108305">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
بلند تر فریاد بزن نگررررررررریراااااااا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/108305" target="_blank">📅 00:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108304">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
بلند تر فریاد بزن نگررررررررریراااااااا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/108304" target="_blank">📅 00:09 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108303">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vN5u2iFdeYI8bTGJogWLquRpR1CPByQnNXYhVkxgfB-0s8OBQ78FpXlckasMzIXhGv-tiwHuHBiQn4x7xwWYl68nEcAkqv4CRMjgbJAB9aBWStKk3wnmV15Hh8BbHBzuPgYzZ6C0S0hCV9XbppiBYmLEDXxJr9tAfC11qntGsSGIcVhI5q5Qd_lHCLuIF406Ts61rcB8d3bx6M3A_qBCPp9tsPaJWvXwvaljpn1P3oC3Gs2v2jymTEQ3NQuSU2C5prs2ST9c6QS4VQcBzrSmp6KR5gQyDE4LVz8hai7luxxY_H1otzWtiBniWCz2nNaXpC9ydUwvBZAPuPWkogGB4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟥
🇪🇸
گل وینیسیوس جونیور که بخاطر کشیدن موی بازیکن ویارئال مردود شد و بعدش هم از زمین مسابقه اخراج شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/108303" target="_blank">📅 00:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108302">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ba8666e1e.mp4?token=LsnC_I3MnBeMejsw60bO6wP7Ij0X2SfcE_4aYjmCj5qHYxxgYWY9UMgAGaUvvVCUdorgnOhm6sqpYGxhpddshtKiCTgouI6HXRM0TeppymVgohLdJEwtShBWA38A3nzz-KzOPUGdlN9ckpjDfea8DvIpF2hBHLTRr1ioLA6YLX7wJ0HLPt_NlUeLKMZiXSWlcAPYyi6A6kqntpHmmCF6jHeG_eOcjQYUnEbJF55AqlYEyjrSDEL-0BVc3fm3Aasl6rVmEipAIoecf4mlsElJf3t_q6V05eO6LW7RrzE0MswkRV6jOg_-adcR2ccEkJS85KaijyhQkGKxRLbHwOWoCDi501SoaVOqMn5dtsYXAqRg0VfL565MLUMOlt3KiJliqfk8uxeeoswGzsFMixaoW1HMd5Xz9fLmFK9WBYc-NZ3w9SGu4kT7xgXd5jRNsC0yyZg9hJ4KRfE1Cqv0oEBGuV_xs9ErkkF6y3l29la343VlWuMwHm1yVo5Zc8p82LxTMuPRBK6XPDBka03lHYrP96aUX_TImZZ1vDsYGHK_fZKMP-o8fMiax-VIEvWt1W4lHGrGfYYAxUkIH3ODh90Nx7dkf_hmqbFCsvzcXc8SsXMRvEQi_ykukHOUSHc9bHudk816kjTOV9mXFt_7gnr_1DP8l-myGpePwF6Y8G1rNCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ba8666e1e.mp4?token=LsnC_I3MnBeMejsw60bO6wP7Ij0X2SfcE_4aYjmCj5qHYxxgYWY9UMgAGaUvvVCUdorgnOhm6sqpYGxhpddshtKiCTgouI6HXRM0TeppymVgohLdJEwtShBWA38A3nzz-KzOPUGdlN9ckpjDfea8DvIpF2hBHLTRr1ioLA6YLX7wJ0HLPt_NlUeLKMZiXSWlcAPYyi6A6kqntpHmmCF6jHeG_eOcjQYUnEbJF55AqlYEyjrSDEL-0BVc3fm3Aasl6rVmEipAIoecf4mlsElJf3t_q6V05eO6LW7RrzE0MswkRV6jOg_-adcR2ccEkJS85KaijyhQkGKxRLbHwOWoCDi501SoaVOqMn5dtsYXAqRg0VfL565MLUMOlt3KiJliqfk8uxeeoswGzsFMixaoW1HMd5Xz9fLmFK9WBYc-NZ3w9SGu4kT7xgXd5jRNsC0yyZg9hJ4KRfE1Cqv0oEBGuV_xs9ErkkF6y3l29la343VlWuMwHm1yVo5Zc8p82LxTMuPRBK6XPDBka03lHYrP96aUX_TImZZ1vDsYGHK_fZKMP-o8fMiax-VIEvWt1W4lHGrGfYYAxUkIH3ODh90Nx7dkf_hmqbFCsvzcXc8SsXMRvEQi_ykukHOUSHc9bHudk816kjTOV9mXFt_7gnr_1DP8l-myGpePwF6Y8G1rNCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🟥
🇪🇸
گل وینیسیوس جونیور که بخاطر کشیدن موی بازیکن ویارئال مردود شد و بعدش هم از زمین مسابقه اخراج شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/108302" target="_blank">📅 00:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108301">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0RMZ5B1cU7j-hXkjZv4pAdct5w-mqGiWMAIXl2LdzlSFsYXfENyFXJP81auBARwvsq58iKymgMXlZNTiCiGq5h7d32AyekJ6Y-DT08VRO7IzdFugY0oVTfcxBq61P7bf-PfF3VkusQCR1ykSyv_qJAZUFyP01cOyq8kIp_HjmwfG_GvLxDMLne91Mr_gDC5Pb8xD5vErpU3nPdtox0KkNq74y8nFfx-x8O6ZXsNR42f-IOC9tn_x6Q7IFSfuUHFrxtxCKQpqHlZ5RdbQ3DGK_c6ZhK-VNH3-MhI9iBVsCeM4G54kOWPoq14WrkiOwOE6xl5qp0vnKs41L3M9rMHTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشماممممم بخاطر این صحنه اخراج شد
😐
😐
🚨</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/108301" target="_blank">📅 00:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108300">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QoxS_jNK6T-dZcUP09ToJ-WU_lJUdA8QVRezJlW_yjm8fMPoNxVVY3JPbVdZsuJjZb5x_a71rSJ4H3_Ln2TzYyBFT_PB5ntX_6IPer1pO8u1AfoPgenxLGQhXeTh1r4qM33hmZwi4nfJADcwIrO5F3BIB13auRu7s-3NvYXD0Ee_wR8D8aw9LQW04yz20Svm3urHBbEqw1dzhBlU0-06xL1S9_GbldwY2A976LZ0nknhotsKI_gLqymsv5OAaxcA1bVage3wFw9P2GEhqgIT-aczaVccIMV3gh1J-T_vtT1iwF2wF6wBVnzwdW2resELAZhvWRjNgsnv3El8Iq7jyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینیسیوس اخراج شد
😐
😐
😐
😐
😐
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/108300" target="_blank">📅 00:02 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108299">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">بدل وینیسیوس گل زدددددددددد</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/108299" target="_blank">📅 00:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108298">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">بدل وینیسیوس گل زدددددددددد</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/108298" target="_blank">📅 00:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108297">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">گلگلگللگلگلگگلگلگل</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/108297" target="_blank">📅 00:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108296">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9c230ecca1.mp4?token=k2g8_VfCVWl-iLrBO5aybg14KgUqP6VEs2YCPH9uw-fNqGge3jZVyJ3F5MC53ddZ-w05HFMJsf7ZELQzNirbU5ipxFFuLLC3UOMt2ngXaczpPAGLwG_pkaQWFSVUZAnV_p0ijm3mIvFbEVDT9BvN94LRXvgr38gxee3GKR-nXprycJMt1C5rW7vtJopZoACo831OUsWI_qg_tu6IUUz6XCe6gu4AOC0Xjs3nXfrGQE-KzhFsPuq5lEP6GkmhXrKIP01WVpezPt1ZnTvMMV6Ma70QOp_JdhaYa-8hx9mO4jljUNjiUJgCPD_6ez28gVEIYrxXLBC8--vC9oPKmvBMroi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9c230ecca1.mp4?token=k2g8_VfCVWl-iLrBO5aybg14KgUqP6VEs2YCPH9uw-fNqGge3jZVyJ3F5MC53ddZ-w05HFMJsf7ZELQzNirbU5ipxFFuLLC3UOMt2ngXaczpPAGLwG_pkaQWFSVUZAnV_p0ijm3mIvFbEVDT9BvN94LRXvgr38gxee3GKR-nXprycJMt1C5rW7vtJopZoACo831OUsWI_qg_tu6IUUz6XCe6gu4AOC0Xjs3nXfrGQE-KzhFsPuq5lEP6GkmhXrKIP01WVpezPt1ZnTvMMV6Ma70QOp_JdhaYa-8hx9mO4jljUNjiUJgCPD_6ez28gVEIYrxXLBC8--vC9oPKmvBMroi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇪🇸
گل‌اول رئال‌مادرید به ویارئال توسط دیامونده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/108296" target="_blank">📅 23:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108295">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">نیمه‌اول بازی رئال‌مادرید بدون گل تموم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/108295" target="_blank">📅 23:19 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108294">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‼️
واکنش علیرضا خمسه به ویدئوی «خلوت کنید آقای خمسه هستن»: من پول بادیگارد ندارم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/108294" target="_blank">📅 22:36 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108293">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">برررریم سراغ بازی رئال‌مادرید و ویارئال</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/108293" target="_blank">📅 22:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108292">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U04mjJbbENx-h_CnmCXTtAvTrJWgxBK_IoaYkt76wcqvwufq3LoZpQ8XyLufvvFH4EepSTeGa6YeOjuXnSwxB5PxnxbSmTV1YftVwp2FTZxnnURQFizn0lxiPJCSy8oaA_nQk582qtAfovjjANzq0pSnuAhKBmMESPvrA49kpA7hH5fGpcQIfGAlcAZEeu8B1hxpXM5KqwK9YWEQ4HU_cN25V6RGJr9g4aC04w1NeLUPaFLazzo3vklb6Zc8pGATgWYgJ7QiMBIy0y_w8SmliQdhTypKMkigVmxzy9KyhI-ivOohMVuoZQTVlyXhppL2UfkUPLAxlH8txrIyqlu8Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هفته‌هشتم لالیگا؛ برتری قاطع و آسان در خانه؛ بدون حضور رافینیا هم برنده شدند
🇪🇸
بارسلونا
3️⃣
-
0️⃣
ختافه
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/108292" target="_blank">📅 22:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108291">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcRB65QYNrHJvpQdG1eukS0JJxuLmGTI3RJnopp7BEXsbCgB5gFPexmHVpyyB8kT2dQFALDIoWzzClDOnXXKAn6_lqHrhfJ-L2Hh5W7AcJSJGscB2s32WIOCjTv521dzk3n-5xf90G0GhlsWXTgkTvOFwBqjFKZ1Mo1AfiqCp1lKDQ_elZYJlgk3gjzkMywM2SM3vnTrHCgbk0nrQoYkGeZBt7ykwFAR1q6zcdIhbsJMOJwnrWsWDxxsVlY2sgYYIxxzfmPgW4UvBbnfeJeBQBTs88FkQkNFw8TdiRC6x8rw1cSiBDSYAUR-Newt3Ybj5VPl5VUgsz00IkEW9pyz2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
لیگ برتر انگلیس| منچستریونایتد از پس تاتنهامِ ١٠ نفره هم بر نیامد؛ مساوی که به درد هیچکدام از دو تیم نمی‌خورد
🔸
منچستریونایتد یک - تاتنهام یک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/108291" target="_blank">📅 21:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108290">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/eee0ed7a62.mp4?token=ndkEgWsMePWXMkj6XK2Jy5O_A0lRSQCuXbz4k6HV-JAE8vo0Xc84eq05DKCxg0iQRJp5FGcpSghsxo67F5XWPSIMGcHggnV3GTgjikoPkciZnUWZvuPdXVsqzmXc3TMrPmycZN3YnQTwTIszq2Z6FsLtBq7vUghHWVhzMv1Md5_I2fHFyk9a2zJ7VpYyw0sDEPeaWa47jgut30UXLbr8ZX3F-JA-trMhPq6b1uvuoMgqeHR-tOu4fm8zef9NTF6w7Ls4sYfhbOZtK-Y3mnsm2SvSUWGcy4NvkR6dVsSfCps9d5-GvUMabTkKNE29gwdq11j4xIKGqTaT3FE5DBDZ75vxvdPsvvHhM90Q-ByyxpxDXS2NTwAi-2YLmnKf8RzJoFpUpDyW2o2agk7nAUcDJ1xRXP6h9LmsLt2QDZtlhHB5XsPLun8Ujt30G5SnR-LUpw5kRdzdTimstCIvm0yg_Cfr9Ry-TUoCaxAL5SDyQvQqhjLOHV3VWOT1sHSmBmMsx0kknCChv8NBI8khJ-lBAJXsaX3TN5lIdEu11LQJwlIwQgRWowM3xKvoCzYo3DzCMbejeLMjMO4uKt6-P2vgh2C7_IbFZg8YqOBtMaOa_jBkgQ8blkc3oNiE3PV7pdfNdSj_dhwWKtJLQ-fqQ5EWWd0NLDmirw6IrDWxNKPp10Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/eee0ed7a62.mp4?token=ndkEgWsMePWXMkj6XK2Jy5O_A0lRSQCuXbz4k6HV-JAE8vo0Xc84eq05DKCxg0iQRJp5FGcpSghsxo67F5XWPSIMGcHggnV3GTgjikoPkciZnUWZvuPdXVsqzmXc3TMrPmycZN3YnQTwTIszq2Z6FsLtBq7vUghHWVhzMv1Md5_I2fHFyk9a2zJ7VpYyw0sDEPeaWa47jgut30UXLbr8ZX3F-JA-trMhPq6b1uvuoMgqeHR-tOu4fm8zef9NTF6w7Ls4sYfhbOZtK-Y3mnsm2SvSUWGcy4NvkR6dVsSfCps9d5-GvUMabTkKNE29gwdq11j4xIKGqTaT3FE5DBDZ75vxvdPsvvHhM90Q-ByyxpxDXS2NTwAi-2YLmnKf8RzJoFpUpDyW2o2agk7nAUcDJ1xRXP6h9LmsLt2QDZtlhHB5XsPLun8Ujt30G5SnR-LUpw5kRdzdTimstCIvm0yg_Cfr9Ry-TUoCaxAL5SDyQvQqhjLOHV3VWOT1sHSmBmMsx0kknCChv8NBI8khJ-lBAJXsaX3TN5lIdEu11LQJwlIwQgRWowM3xKvoCzYo3DzCMbejeLMjMO4uKt6-P2vgh2C7_IbFZg8YqOBtMaOa_jBkgQ8blkc3oNiE3PV7pdfNdSj_dhwWKtJLQ-fqQ5EWWd0NLDmirw6IrDWxNKPp10Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌سوم بارسلونا به ختافه توسط کونده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/108290" target="_blank">📅 21:52 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108289">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">کوندهههههه</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/108289" target="_blank">📅 21:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108288">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گلگلگلگگلگلگلگ سوم بارسلونا</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/108288" target="_blank">📅 21:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108287">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3LEh2qNnkzO3HGXuO0MCW2eC4hFgdslwYHbYe4ot4lOdKR_LWXq8_IAr0_EdutM4-wg6J3zRoA8IZSZGawkdWOtudCKVc4PoxP7CzXszquuKlvwsXpLA_1rLKcvy_EPZZ-WsVrhkyT2iOhfCfncFEayWIBdgb36-HmXCaQ2QjOG_RpV0IinJF4exfkcHq2JBvU6sZQ3mG1yG8rSO8DKgNQG1Yp2UPdmuckHazSKzFbhBOXyu6TMUpCcuRwrlY1EBCRbvpNbjVmcVkBteo77-8aVbXt9v85UrXMwtLSR6ahuUjxsDQ1sMY3hSa5ITz5AhAQtH2cQBK2ukovnEqHnvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب رئال‌مادرید مقابل ویارئال؛ ۲۲:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/108287" target="_blank">📅 21:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108285">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0tdCaLVkDlB5WC5qt1FOh7K8EJlGjEko7CVCuCdzzvYa0IbmPvRJ9z6D-KiK8u87enpmWPu_PG0QEZCsFZYoE5bkJ1lNJyZlQcuBUY6m4x1FrEEWSYYTSktXTLerl_UXYY55p3mUOtWTJub4o8eP291duz4-17rXRWyBYWBKmHfq7va33CR9fnmEVGvDvhN3iebIzjejxO9RQAcz-KWRmvHQzMuebphxXen8HYOIP8tKuDGdV91iz9aAv12CDvcMeyiO4q8pPjbHwQP0AI9EJDqwoOqVh_pYMGUfkXTWxl05AOE9-IT0IFHGgkN6A8kDxCxo-Ym33wmWOKunxF4dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇵🇹
فدراسیون فوتبال پرتغال از بازگشت رونالدو به تیم‌ملی در فیفادی نوامبر خبر داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/108285" target="_blank">📅 20:57 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108284">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9c23307a24.mp4?token=MKXuwreS0uYSEWaBI8w5KJ4sv6RSr7IbRA2tMYA8cRClqyxmXUXehbYq7UdUYK2HbjFaKJh34UyFvIqntg4lwqf4CT4faTTxSsvWZYgQj0T0njkwmvda1cFHYqr2oH--Sv1eBIaLcdSYkwG0rfypevkZuwEs6bzR4HvSG3e5WoT9wyvCEAyhdk4pHlIJPESCHqTuTm6AbqKbVdqHoYOxO_ppgw6gQ3YjE5HgQBAWlr2zlhmCLTSSNjm7VePhrQFRugxM-CplN_8ZrvB6ZzVgKOTP73moXRzz1t83xzZPnnL9b5Pcy9OTcqHuX-LMwixsYuIHHqju0PTwxMdEIQGFHi_W846R0GZFBHMEZXvZEw6TxhUhuviY84VQX571tzoCRd60n5jAGrkvzHvFgrrsPVae8Y7PIxGjaTRsw6XpV9lfQx8Ewg66IcjQv3cmmj43kKB2-tfdHYgehTJDCoiExS-1YdNqznspL3_Q1NyNBU14515L80TrUtuKUenr30M6moLYE1OzgCM7mLcznifVX4S6xYhrHQt4m6QPuU688AgbrWBQf2hUDfJH9Pgr_dwnT9HXTJi8bsaODIOIa3MFZhI2aenldEaawupNcdNjn6tnPnkurWH_nVTiqtVJrwmvJG-DIUvuAKL9gnXhNcDmZUxHz2TDbhkGLMKeQwvbclc" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9c23307a24.mp4?token=MKXuwreS0uYSEWaBI8w5KJ4sv6RSr7IbRA2tMYA8cRClqyxmXUXehbYq7UdUYK2HbjFaKJh34UyFvIqntg4lwqf4CT4faTTxSsvWZYgQj0T0njkwmvda1cFHYqr2oH--Sv1eBIaLcdSYkwG0rfypevkZuwEs6bzR4HvSG3e5WoT9wyvCEAyhdk4pHlIJPESCHqTuTm6AbqKbVdqHoYOxO_ppgw6gQ3YjE5HgQBAWlr2zlhmCLTSSNjm7VePhrQFRugxM-CplN_8ZrvB6ZzVgKOTP73moXRzz1t83xzZPnnL9b5Pcy9OTcqHuX-LMwixsYuIHHqju0PTwxMdEIQGFHi_W846R0GZFBHMEZXvZEw6TxhUhuviY84VQX571tzoCRd60n5jAGrkvzHvFgrrsPVae8Y7PIxGjaTRsw6XpV9lfQx8Ewg66IcjQv3cmmj43kKB2-tfdHYgehTJDCoiExS-1YdNqznspL3_Q1NyNBU14515L80TrUtuKUenr30M6moLYE1OzgCM7mLcznifVX4S6xYhrHQt4m6QPuU688AgbrWBQf2hUDfJH9Pgr_dwnT9HXTJi8bsaODIOIa3MFZhI2aenldEaawupNcdNjn6tnPnkurWH_nVTiqtVJrwmvJG-DIUvuAKL9gnXhNcDmZUxHz2TDbhkGLMKeQwvbclc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌دوم بارسلونا به ختافه توسط گابریل ژسوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/108284" target="_blank">📅 20:37 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108283">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔥
🔥
🔥
🔥
گابریل ژسووووووووووووس</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/108283" target="_blank">📅 20:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108282">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">بارساااااا دومیووووو زدددددد</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/108282" target="_blank">📅 20:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108281">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">گلگلگگلگلگلگلگل</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/108281" target="_blank">📅 20:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108280">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9dcb84758.mp4?token=X95UTF16r2WWyQk1PEFi2wOzgmRGv6HvNqtVfiOhE6weyWy6nXg4x3uLEjk_9JY5wZBleIKOJKRDJYtuwCm85N6HdTM72aqRjpgjKDwlKKgqdsRS-UKVxprzAOgHHkUyw5RwgwdNrmB64J-T4yIqEuZstyFb5P-oQDFW9NA8_5dGIFfmgf1GvWBTC2g9QVuW4czkL8YwwogtOBBUt-9HmNojd0DU6O0URPPdUWnPn6JUBMe8gE5yPiyURKGxp0lzxRgqug_rVxor6XJGSCQ9-ufSgSlMPC0xmARrZeulT0fd2TKi40Zut3cYNCeFlqOH8CujYRcXEsQuUQT2iVeZnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9dcb84758.mp4?token=X95UTF16r2WWyQk1PEFi2wOzgmRGv6HvNqtVfiOhE6weyWy6nXg4x3uLEjk_9JY5wZBleIKOJKRDJYtuwCm85N6HdTM72aqRjpgjKDwlKKgqdsRS-UKVxprzAOgHHkUyw5RwgwdNrmB64J-T4yIqEuZstyFb5P-oQDFW9NA8_5dGIFfmgf1GvWBTC2g9QVuW4czkL8YwwogtOBBUt-9HmNojd0DU6O0URPPdUWnPn6JUBMe8gE5yPiyURKGxp0lzxRgqug_rVxor6XJGSCQ9-ufSgSlMPC0xmARrZeulT0fd2TKi40Zut3cYNCeFlqOH8CujYRcXEsQuUQT2iVeZnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
حجت احمدی: سیلی نبود، آقا ساکت بهم خسته نباشید گفت؛ پیشنهاد استقلال؟ خبری ندارم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/108280" target="_blank">📅 20:28 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108279">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/faa2aa1c08.mp4?token=P-JP_YQ1yMWA3UYNkS4429JyY8D1MhMYe6rkJOw_dm_k3cQLx4Uu7XKXDQ57njdq72ZVrNK1Af6s2c8aZKobWduKgkSCv0WOTIG-dooJjAcopYB0DFyVWJf2SRdl9mCYwc0Am_KrdTpYp5XzjLAiuHo21Y34amrYj7kcsjACLP6Fv77oM_FhAvjZ02NyDH3F2-fW-aMNp1BMAxpLTALuRzCB6N0t0I3s2jZXRrP4qEKOSqhRTACXz8GIXI8zXN0IPAsWZ9o2d6G8uX8e-kv6DUXY91ntQ3UTsYnccHR61LqnZVhCgWyTOHdZTrDwPLYeZgoFnl2H1P1dF37IjQrXlAYJNOJ6waeKgg5EXBJTL02_-1qR_sIhgFxd0aErebuUdbRyeChpTI3b6-RTfB6PiPzqQg1BBFatnNkWsQ9jVBx4kaISLZnWoFecPF3CH3k1EB9hrwCl8xx6cwRiySy1GkdETLWxHA61L_3CNnY-ejXWJI-m9W6qACip-iFpUdgjeELzsuGdMrOpFXYiHgX7mmF4dq0RLeJCrPaQ7MMPDoRnHmRmPHAhDJQQ06XkZCzY96aDWBPWh0jdMMvZTfWtjddjfhuzFyNQzfCrBbfZLh6CDkNbCWsd7yj60aNWoGfzerUq7-crBmJimkQNwHs8YL3jSBv09IqyrPh9KHti9Kk" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/faa2aa1c08.mp4?token=P-JP_YQ1yMWA3UYNkS4429JyY8D1MhMYe6rkJOw_dm_k3cQLx4Uu7XKXDQ57njdq72ZVrNK1Af6s2c8aZKobWduKgkSCv0WOTIG-dooJjAcopYB0DFyVWJf2SRdl9mCYwc0Am_KrdTpYp5XzjLAiuHo21Y34amrYj7kcsjACLP6Fv77oM_FhAvjZ02NyDH3F2-fW-aMNp1BMAxpLTALuRzCB6N0t0I3s2jZXRrP4qEKOSqhRTACXz8GIXI8zXN0IPAsWZ9o2d6G8uX8e-kv6DUXY91ntQ3UTsYnccHR61LqnZVhCgWyTOHdZTrDwPLYeZgoFnl2H1P1dF37IjQrXlAYJNOJ6waeKgg5EXBJTL02_-1qR_sIhgFxd0aErebuUdbRyeChpTI3b6-RTfB6PiPzqQg1BBFatnNkWsQ9jVBx4kaISLZnWoFecPF3CH3k1EB9hrwCl8xx6cwRiySy1GkdETLWxHA61L_3CNnY-ejXWJI-m9W6qACip-iFpUdgjeELzsuGdMrOpFXYiHgX7mmF4dq0RLeJCrPaQ7MMPDoRnHmRmPHAhDJQQ06XkZCzY96aDWBPWh0jdMMvZTfWtjddjfhuzFyNQzfCrBbfZLh6CDkNbCWsd7yj60aNWoGfzerUq7-crBmJimkQNwHs8YL3jSBv09IqyrPh9KHti9Kk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌اول بارسلونا به ختافه توسط آنتونی گوردون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/108279" target="_blank">📅 20:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108278">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">آنتونی گوردون</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/108278" target="_blank">📅 20:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108277">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">بارسلونا دقیقه ۲ گل زددددددد</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/108277" target="_blank">📅 20:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108276">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گلگلگلگلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/108276" target="_blank">📅 20:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108275">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/326220841f.mp4?token=JyWkXyDJTYuqKWFjPUCP0A8sitF5YBrZ7xXpSa68E98p7EFYHB7-oa1sDf5iTAEZsKhyhy4nTMSpYvrFWH4TMXXmaxA50iqE-wZELS1K8x3I312XWDFQ83xRGduRh_P_Uq2VmFyHZ1wzxAlERftLuhqj5T5unnh-qxfDTfBwDtAZjJk854peu-jDRDw_ob47d_45nBHek6CYau4MzeRdTB7BQ7V4omY6fGVldtvMup1pTDYCABcvL37n9Lc6_NwPvSFQWz6qyL2pyGAn6qcEg7w8nX0i-f5P1FL-JQvADQOfPvLrDZsjbIQQWc7tnwYWqs79vHRKNBFEw8FUcvXVLxt8fM_8K1BWquhx12Yqxvzivl6m5wQk3ttg_xG2LBmNZlIF2SAXm6vmQ9EZfhbQxVsaMRnLfSABXf59VczN4OwjuYqZjbjTXQP-GepiOUJ2GlAVqiT0POiGKxJX5NbOE_p-Z6nasmJI6-bgVCN6p7dmk-G2KpaidIPt9jpDF-qoeCaaVx6dFDsACL8ADBfCF5sOtOBxiNweLq6R6qtf0Y5DFLlOjxtzHBZZVegQldX70DeDXMSLh8zyDSp6xW6bh8RS9egQKJZ15yCwQiju92b3CNHPdv58EQ7KA1UjTVTG1IX5SpEScLDjKBavoa0_nSFg4mD9-8KIpyQQceJfLUY" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/326220841f.mp4?token=JyWkXyDJTYuqKWFjPUCP0A8sitF5YBrZ7xXpSa68E98p7EFYHB7-oa1sDf5iTAEZsKhyhy4nTMSpYvrFWH4TMXXmaxA50iqE-wZELS1K8x3I312XWDFQ83xRGduRh_P_Uq2VmFyHZ1wzxAlERftLuhqj5T5unnh-qxfDTfBwDtAZjJk854peu-jDRDw_ob47d_45nBHek6CYau4MzeRdTB7BQ7V4omY6fGVldtvMup1pTDYCABcvL37n9Lc6_NwPvSFQWz6qyL2pyGAn6qcEg7w8nX0i-f5P1FL-JQvADQOfPvLrDZsjbIQQWc7tnwYWqs79vHRKNBFEw8FUcvXVLxt8fM_8K1BWquhx12Yqxvzivl6m5wQk3ttg_xG2LBmNZlIF2SAXm6vmQ9EZfhbQxVsaMRnLfSABXf59VczN4OwjuYqZjbjTXQP-GepiOUJ2GlAVqiT0POiGKxJX5NbOE_p-Z6nasmJI6-bgVCN6p7dmk-G2KpaidIPt9jpDF-qoeCaaVx6dFDsACL8ADBfCF5sOtOBxiNweLq6R6qtf0Y5DFLlOjxtzHBZZVegQldX70DeDXMSLh8zyDSp6xW6bh8RS9egQKJZ15yCwQiju92b3CNHPdv58EQ7KA1UjTVTG1IX5SpEScLDjKBavoa0_nSFg4mD9-8KIpyQQceJfLUY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇪🇸
اتلتیکومادرید با این گل دقایق پایانی کوتی رومرو مقابل آلاوس دو بر یک برنده شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/108275" target="_blank">📅 19:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108274">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هایلایت بازی چلسی پنج - یک بورنموث
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/108274" target="_blank">📅 19:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108273">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec5d3b26d2.mp4?token=KIPG9__pztrEbjn_n8oLt2LrcN6TU7ksYQjiyBh-t1yq8hAVe8SkGD_UAY1cliRUe_bSYPlmATfiYJaPKGLNuS4ICU-1iVFblQtZIDZR2RvPieolUFh4qYInXv-2vfdPYv_lg_VfQphFMhkXk2wFEmTUKTZZYhTuTd4LIpPQFsmdTAfSWF4Bv6JnqVjFI12c3dALnDKaw1NB2eReNmSsOujRGE5eQA6GpswVVpHbjTLOb5cl7lZ2L24moqmnU97f9m0IMzi0uP-uNgrhHI_Jh6ua9qW3HZ1PQuc-Nvo5wQlw8mAqpt4kVDlbupkBeCbALAU1GRQXk1nEw8uhLx5f8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec5d3b26d2.mp4?token=KIPG9__pztrEbjn_n8oLt2LrcN6TU7ksYQjiyBh-t1yq8hAVe8SkGD_UAY1cliRUe_bSYPlmATfiYJaPKGLNuS4ICU-1iVFblQtZIDZR2RvPieolUFh4qYInXv-2vfdPYv_lg_VfQphFMhkXk2wFEmTUKTZZYhTuTd4LIpPQFsmdTAfSWF4Bv6JnqVjFI12c3dALnDKaw1NB2eReNmSsOujRGE5eQA6GpswVVpHbjTLOb5cl7lZ2L24moqmnU97f9m0IMzi0uP-uNgrhHI_Jh6ua9qW3HZ1PQuc-Nvo5wQlw8mAqpt4kVDlbupkBeCbALAU1GRQXk1nEw8uhLx5f8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
سوپرگل دیدنی و کاشته هندرسون بازیکن چلسی مقابل بورنموث
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/108273" target="_blank">📅 19:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108272">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b95f1bafa.mp4?token=qZICAMjbsERN3N9qrtvVFu3_49lhiK8dOp5iJdYWokt-yh4GSdI7Tgxq5rv6PtkI3r_qivYkJtPxkkewGbg7pK_edgIR59jy_DNvt0Eh1GoFKn2DfLPyNt9ufaREkHlCPxhSBbnV9INtKuIsPIdx-kPFdBg91sqABIVRkLqUDls-dG5qF9brZdTTNPLAuDSd02Fql79j7GfTxwuIxGVT_tTfC8PR2e89y5yz-peXFFdaUehK0fUcYHWzWzf14eeN5ToQmtZfEaQ8ps_SIJLcYWnT0hCIMEqoK1DXyQC6e_5wAORB7QSv-yE9af17UjEuvXSJgsiPpB-ySuXjWqeDG3tpt2t87rnj53XGlFn6DW7700_hu3_6IkBCiz-Rdo9NNQ0QYT1APSt1x6BjMe64LPTdys_xdldjeqLCU0QrGja9JJwuxfJWLToOyyP2kegGJ3F6oqdsM04ghaEtj8u6JMQ-nbFtXhxDy-IV19Z8KD300sJZ5w9QmrirGgTQ9XR6ayjHAUPJrMAcp-TNUG5vR89Jr3UNLcuK9pZHEKnjnu0xrBPPwtBfyRF2PkzGa9fVNfh8WBZbOnk2EZuof3BzS1AmT0C4haL2-qgc7kfN6HttyjBIypIineiNUB_2Jk-G5-mvElx02_HSAqlL1SjRg3RWpmYEr0KKsRq4Oqf19YI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b95f1bafa.mp4?token=qZICAMjbsERN3N9qrtvVFu3_49lhiK8dOp5iJdYWokt-yh4GSdI7Tgxq5rv6PtkI3r_qivYkJtPxkkewGbg7pK_edgIR59jy_DNvt0Eh1GoFKn2DfLPyNt9ufaREkHlCPxhSBbnV9INtKuIsPIdx-kPFdBg91sqABIVRkLqUDls-dG5qF9brZdTTNPLAuDSd02Fql79j7GfTxwuIxGVT_tTfC8PR2e89y5yz-peXFFdaUehK0fUcYHWzWzf14eeN5ToQmtZfEaQ8ps_SIJLcYWnT0hCIMEqoK1DXyQC6e_5wAORB7QSv-yE9af17UjEuvXSJgsiPpB-ySuXjWqeDG3tpt2t87rnj53XGlFn6DW7700_hu3_6IkBCiz-Rdo9NNQ0QYT1APSt1x6BjMe64LPTdys_xdldjeqLCU0QrGja9JJwuxfJWLToOyyP2kegGJ3F6oqdsM04ghaEtj8u6JMQ-nbFtXhxDy-IV19Z8KD300sJZ5w9QmrirGgTQ9XR6ayjHAUPJrMAcp-TNUG5vR89Jr3UNLcuK9pZHEKnjnu0xrBPPwtBfyRF2PkzGa9fVNfh8WBZbOnk2EZuof3BzS1AmT0C4haL2-qgc7kfN6HttyjBIypIineiNUB_2Jk-G5-mvElx02_HSAqlL1SjRg3RWpmYEr0KKsRq4Oqf19YI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
گل های دیدار آگزبورگ دو - دو بایرن مونیخ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/108272" target="_blank">📅 19:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108271">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UA8oxp7EZE57uO-VoUh4vUn-bfPL_fWGbtD1GEJfCyuHFJUKn9rZZq_3s7QAcOSkOWCcBAVN6B9rd1qjFv6-e_4P0kvbWdSxegXYbolLzj3x22OmfQPTQtH1311eBZPwBb4S52tZJd2ugzAEZRxRw6hmKcR7xreZSIlvSan1O4Sx8ZVrvK4MiZk6zQZRMj0ZYoEXX9VEpkATi2uzy44xcz7LGuhzCwUGJNNpx96USBzOVcDkaixIVyaKQkuoy5wX-LjjIwVgtd07Q3rUnC6hY4xIGjt5x-r5zaiPKW2GpskWt8eqJdOchstoaxHLp1cJ7vfQ3xjf7RWPlHvTPXD9Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
پایان بازی هفته پنجم بوندسلیگا
⚽️
بايرن مونیخ 2 - 2 آگزبورگ
⚽️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/108271" target="_blank">📅 19:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108270">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jk0ccyc-6H8_rmxEPv_j4O_GcnSOEx8We3rBodfMvL8vtHtKcC3vh1mSLVGBoDo9LguXbtxL8jOlmc3817cMzNi7ejZ0CQwefTIleXLR0g_pHwJ-Su-PaDLHpQQRgHHfau7MidFxAUSb6TX3BPgdThpZ29akhAX_UCUIa6SCwmWZhseCVFpi9RkauR28a3jhf_jxJK0UPDMNn3BDVIMCcW87en1iVhXO8VMB6vB45uPrNz8B7MPX3P9z6DzzwhMQUySUTCkavHloZcf1F2QpRIQ0pA8WzqxmNSS-oTL4ix05kSB0OiKfKDIZbFzqYcvVnx2X-VFjqF5mdtNnIVHJQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب بارسلونا مقابل ختافه؛ ساعت ۲۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/108270" target="_blank">📅 18:49 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108268">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BfsWSGKFw0ogbFFcqay33x0uEI-_vGIH2aAfj4yVWZrdskgQpabTEvkEwaglkqyAqBXuHK3avyJ80UDHQRYW9reTxWn9ZYnUlvUlXl4DnXRlkyUKJq4vSo5peBbnIbLfJVbMcpLG-KzmpeHVuqGtYR-8n2-UnSQDcKBRonmZQxHxuwFOaKEGmYpa6ERTgnWq5t5SPtqsuF7WOvohpb8_abTv0NFvlrMEk5Fr3_cmZkd8z2ALHdM25OnBVACYU9Vz459n5fJEi2xQS1oje1wxOgslLw7NT9O0g4z3Ws-kOwY_jBK_fTLMzqWuIjYH5JW7Cpk_bxngh5jIqCg_Ospdig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/txjCzACv1qScIX0egXk_0Yu-s36AMbbkQGAjvzwG5bjywruGLCyv_nVC-hfiEFsZBeUj_vmhaQ5o-UUxRi3bNGf5dgyargnH-8qtGY1pS540F-A2DeWNYVnVPRtTBQS43vYhqwps71Cwyef1aKUbjIlgXwjnfLc_y1BKsON8EGMUa4z2_pXMawGoHYy6ORoiyio6x3OOliVPLdPFR_mmwG8AISv1ZO9qUy2iTYaIG5fgIquFsnfaDOUxaMYjuIdFPo15eMhkE-LDrCp5BrMLQWQwJyKeuqfujZo1vsUmS2C5n9PIQ5l8UNW5vw6DKOMcv2PFwS-7tj4xVjuydtp6uQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب تاتنهام و منچستریونایتد؛
⏰
ساعت ۲۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/108268" target="_blank">📅 18:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108267">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQCNLIDW0RUAkToVJS3_153ZUlVSQL1Kwq-pUIX8LfqjP59XrxaGrFkKOpiJOwGIJaNvshDZAjtaVl3yLz1js4uLN6909oSHVEDm-tTjjqmfI4zROg7vyMXGfhsHywiPgLll2bg6AVo023fqtx9kATMBfdXoXZ_5o2YowFR3gaz9F6goFrf-dkvSljCn4ln-PorHDy6LxyhPCD0k_TjSZrHVEOW7ir6w-QiVsY3edEqePX5AKwu3bubl0hEmL1voOWZoOC-RpCEh0bmqWfT_8KvmW-Nm2z8QyaQ1jvzVfTtyVNBVfDJ4wNKdJbViKQ1fYOzviaIiuxGZPobi1DhSUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب بارسلونا مقابل ختافه؛ ساعت ۲۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/108267" target="_blank">📅 18:46 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108266">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udaB3pm6ommf9a6Qqd-R0E3tGeB6N1Hq4gP0vAtUA96tiRuJjG2sSdBShCkYc-LaAfK9ZbirP53HTMwg_SyF1E9_IY7jkUmHDYm-vDZF5Hx42L1ijXV8dnvYP9ZBp9PH4JbCoVPLiU_iM9zkB2CrPrBjtUYhN3NNIqap4E8JtNC_KWxFp5ixVrlzeaiCe4jWYlEjRrfcAsK_GayXVChFFvdkh4_bwtU8awWBXOP8m-1a9lgq9GzQEFKKaMxS0MSVd1OYfP46-KfCsZobyQMSmQQrVvHDVeuVH4pWSUjfMfwrbnHVPxvTVLjsUE3AhDv9ujJQ9XXkCo5qJkYJOMk9Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
‼️
با تصمیم محمدرضا زنوزی، علیرضا بیرانوند تا اطلاع ثانوی و پیش از سربازی خود در هتل تیم امید تراکتور مستقر خواهد شد و حق حضور در کنار تیم اصلی را نخواهد داشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/108266" target="_blank">📅 18:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108265">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33630db290.mp4?token=VJeP4NRmZonP7Jrp-YKxU9xkucTGXlqGrPhxjDHcbiqZDJoj8gvZWJtDQVCJwjA1tq7wDFdBT4avtYWpY-iiVRh1clA-dASTkZvLPl70mqyXxUQcZn8TUE3xFM9kcFdjcLJnaktMEUXjpmozNIbKzc7PbtG6jsf2Ej9lbGwlBfHZEY_IwiL9Qkz65pk9oUmUl0tDIQsVQwnjw1pkGrIw76UKXJLvFhAC-Pu5erWY6zfu2ram8_VdQf2CCqRWHCCwFVFnNiFqQs9Gvyyw4dGPgJnHBEsWV81ia6bs7wCHHfgAdETAfAZupdbuVlbzt8-EeAnNsTyLVUesYTGCS-ZNKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33630db290.mp4?token=VJeP4NRmZonP7Jrp-YKxU9xkucTGXlqGrPhxjDHcbiqZDJoj8gvZWJtDQVCJwjA1tq7wDFdBT4avtYWpY-iiVRh1clA-dASTkZvLPl70mqyXxUQcZn8TUE3xFM9kcFdjcLJnaktMEUXjpmozNIbKzc7PbtG6jsf2Ej9lbGwlBfHZEY_IwiL9Qkz65pk9oUmUl0tDIQsVQwnjw1pkGrIw76UKXJLvFhAC-Pu5erWY6zfu2ram8_VdQf2CCqRWHCCwFVFnNiFqQs9Gvyyw4dGPgJnHBEsWV81ia6bs7wCHHfgAdETAfAZupdbuVlbzt8-EeAnNsTyLVUesYTGCS-ZNKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🇮🇷
سیلی ساکت‌الهامی سرمربی پیکان به بازیکن تیمش پس از سوت پایان نیمه‌اول با شمس‌آذر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/108265" target="_blank">📅 18:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108264">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ep8wpuSfg1TqFtbbqwIV6Nc-MKAlbdpVUxGBxGgvdMQhF_9s62vhemZDD1izqr1WurUNI8s17MmHH0htBippGYdQK-H1lmKKlAtT_qs-iNcIDjbE1beimjMdoSIwvkDyPqtrodyehWdOaEMXUXciJK4snVnHV7pAM_5mIYKsHhWD-EXFf8temjmwf7DdxqZFxaQDcAKDRaeeVIOuQSSiRbklsxv6m4-BQs5JWH_Y7DdeLP36FrIoVz6NutYvYwBAENgrUOo3fjhve_XneByI0p3Si0o2JGkRhdSJHCeDaMFI7UNBj6dlL8u5NYZAKLIaG5a7lzMM91bsIgQeODem9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی های بارسا و رئال تا قبل الکلاسیکو
⚽️
⚽️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/108264" target="_blank">📅 18:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108263">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/974d9df6d8.mp4?token=SeolMFKcrV3IWxTSh0rbacZG2rDr6S3UGSwZlPlVgQo7FJsZadzjvnFh0K8Qeq63dMoZQ9xI1pdyxBrx-9a3B3xPmKPtofukPK72EU_SzNTQBu4mMq2jMuhX1guVfSVkFexGIKe7qbKKbIZFiFAciGpvdclxCuAj0buE63BaY-SWAKdoA--APziCTJ1iyOCd0W_QJetrV2coNwohR325ETAX8UE_qHPNqmToAMUZ4ALBR2Tf86ICEzWnRIox1mv4sFjfjj8fTcw3CzbznRn236sK5PWTgblt_GQLB3SKojGEtpmrBjAZtA8CmSBx8FsudUS1-SQoaTs6_VcbN0GLfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/974d9df6d8.mp4?token=SeolMFKcrV3IWxTSh0rbacZG2rDr6S3UGSwZlPlVgQo7FJsZadzjvnFh0K8Qeq63dMoZQ9xI1pdyxBrx-9a3B3xPmKPtofukPK72EU_SzNTQBu4mMq2jMuhX1guVfSVkFexGIKe7qbKKbIZFiFAciGpvdclxCuAj0buE63BaY-SWAKdoA--APziCTJ1iyOCd0W_QJetrV2coNwohR325ETAX8UE_qHPNqmToAMUZ4ALBR2Tf86ICEzWnRIox1mv4sFjfjj8fTcw3CzbznRn236sK5PWTgblt_GQLB3SKojGEtpmrBjAZtA8CmSBx8FsudUS1-SQoaTs6_VcbN0GLfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
‼️
یامال نسخه ایرانی هم خوب داف میزنه زمین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/108263" target="_blank">📅 17:30 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108260">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d61d77833.mp4?token=bjgazl9BVqrccbwMQvDNDPswfUhHR71mJKucTQe6tQwNkVCsNdw3LAG4UJbmgbYB7AoEBkc3R3oFHWxw5lUjYIfy35iGXPxpVlBt7R2hcgFHYhOlMivwSrOZ8ViqLeRtZ1oXQo7sefQcZua_h1cI6geCB8JdGa9fdvy1fgMDL9RGpcO2f36ui4SC3dvacI-dXSiupUN8FwC93zQ1XxSJv8x9Ws7fWvGOIfAomjIpww45WOl7-zxrf0FBDN_GxZ_-ZqvnPPfwLD01vyyY1-K4ngO-D3zS3DnWrj9xexRyBfNwr-RjcWZGqGzYLi_QDJvkxgbST23B7sARNnmDxJ6nyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d61d77833.mp4?token=bjgazl9BVqrccbwMQvDNDPswfUhHR71mJKucTQe6tQwNkVCsNdw3LAG4UJbmgbYB7AoEBkc3R3oFHWxw5lUjYIfy35iGXPxpVlBt7R2hcgFHYhOlMivwSrOZ8ViqLeRtZ1oXQo7sefQcZua_h1cI6geCB8JdGa9fdvy1fgMDL9RGpcO2f36ui4SC3dvacI-dXSiupUN8FwC93zQ1XxSJv8x9Ws7fWvGOIfAomjIpww45WOl7-zxrf0FBDN_GxZ_-ZqvnPPfwLD01vyyY1-K4ngO-D3zS3DnWrj9xexRyBfNwr-RjcWZGqGzYLi_QDJvkxgbST23B7sARNnmDxJ6nyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
بخشی از دادگاه انقلابی امیرعباس هویدا که وایرال شده است :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/108260" target="_blank">📅 17:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108259">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6680dee71.mp4?token=DTfnuX6KBrSIBOm0khleYry3Qvv7JO2T41A6fib1-MaLTWR-rfl2ZI4eI9sjWwCu8cJElQvjwwT7vVOTOcnmIlD42ZlzqzwId8Q6yR0nM69aCkIG7xK8uYgvbpqGH1KncgI4w0_XQsFpdCxJCgMRuMGZYYtfGfcUilBg8nWEl4MSpyRm2ZdxV7Om0UizN3fadG-blT4CKaLyGZj5KBzGfrZ7OoKCYp5WKfPvlOPo7NQ3FCFztCPHkuiy_cRjg3iIU31L6BEiSks8HQOpFA07pYPy5W_q_GHTvirQqk4B1RQYg197IsTUatsU9T37pGv7FTcK1X-F5MztQno-J6aZdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6680dee71.mp4?token=DTfnuX6KBrSIBOm0khleYry3Qvv7JO2T41A6fib1-MaLTWR-rfl2ZI4eI9sjWwCu8cJElQvjwwT7vVOTOcnmIlD42ZlzqzwId8Q6yR0nM69aCkIG7xK8uYgvbpqGH1KncgI4w0_XQsFpdCxJCgMRuMGZYYtfGfcUilBg8nWEl4MSpyRm2ZdxV7Om0UizN3fadG-blT4CKaLyGZj5KBzGfrZ7OoKCYp5WKfPvlOPo7NQ3FCFztCPHkuiy_cRjg3iIU31L6BEiSks8HQOpFA07pYPy5W_q_GHTvirQqk4B1RQYg197IsTUatsU9T37pGv7FTcK1X-F5MztQno-J6aZdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اشتباه عجیب مانوئل نویر؛
گل آگزبورگ به بایرن مونیخ در ثانیه 5 بازی
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/108259" target="_blank">📅 17:11 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108258">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‼️
⚠️
‼️
‼️
⚠️
میرسلیم: مردم باید بنزین را لیتری ۲۵ هزار تومان بخرند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/108258" target="_blank">📅 17:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108257">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bead49b429.mp4?token=S-z1Qmv5Taj-T9CvhjZMoCa9OtnNbRwcfIDQfhZJ-bqRy9-znnfJbGSv_nXitGVoFHTB2yF9u42uisdHGcuCCc-rzAtuCvqJadHj_t2rGsMgOEq7oE9SmjyQbKRyCqaYNbRlA94Ln7gS4oC3kzxVlP6OdyBMU8AnBXQE4gl46VOlIEPG5Fr3nahulp3XwwitncwlgMpmwycCLEUjawU42BaW8jhN80mdHTaqOQFuFfhe8DjLegX0kNDyNkBwKwNf-3n6luAQBVsR9d1sudMtRMIo7SVq1g0xjN-tvOZ5iwyIa5xdSJfg_xW2n_d7mYNZUSYPNcTjh_AzhqW_f29m3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bead49b429.mp4?token=S-z1Qmv5Taj-T9CvhjZMoCa9OtnNbRwcfIDQfhZJ-bqRy9-znnfJbGSv_nXitGVoFHTB2yF9u42uisdHGcuCCc-rzAtuCvqJadHj_t2rGsMgOEq7oE9SmjyQbKRyCqaYNbRlA94Ln7gS4oC3kzxVlP6OdyBMU8AnBXQE4gl46VOlIEPG5Fr3nahulp3XwwitncwlgMpmwycCLEUjawU42BaW8jhN80mdHTaqOQFuFfhe8DjLegX0kNDyNkBwKwNf-3n6luAQBVsR9d1sudMtRMIo7SVq1g0xjN-tvOZ5iwyIa5xdSJfg_xW2n_d7mYNZUSYPNcTjh_AzhqW_f29m3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
امیرحسین صادقی پیشکسوت استقلال: علیرضا بیرانوند به استقلال برود، من دیگر هوادار این باشگاه نخواهم بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/108257" target="_blank">📅 16:57 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108256">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h35o8ZqLLGq3n1LjsWAHYFFjLWcVBZqNRoyUMyO2g-HZG6qb_-jkR4Q9wd-68rbkQVoXjcUdL6nSzIXKl3nXh9lwsWiTLJRa6I_vjvVmBpmisbhbj24Rps2dkTFB0yP9WKFjwoYMEyGw9sqMEYblUusMbYGJkpVLSdo2Fh_9-eBJr2LLj56eOuyv4oOQaVa5HltfNvq8f6H-HVkxLZOB6WcXkyP-zvwDiANO6heojXNYNm3Lh3AgQ5YYPvgXXzPvH3utSIJSO0yjsMrDXWGPbQd_ubYGAqC44GnQhZfvOLC7EDELH90KTGvnGn9xLRyB-YIFq1oOJR4Y48DI3MznHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل دوم آرسنال به لیدز توسط برونو گیمارش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/108256" target="_blank">📅 16:56 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108255">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpkP8HChyJ4KBc-bIZ6mL-mBZ6LddnUgIFefR3HBU4siCie7bRkeIY1Y-aHd8EAKP45dvfWbaVFM1zkL_iu8r_voC7qJuzzOWL3i4OPKMOriXj9bC7NgaGToEGt7I-LGUuW_Q3vQ4P2coq4F_pF7coz5hsLD0bssxnOqOSuoKiDELgPwGSu0mF9v4x6Hhnjvh72rmyt5j0ghmN1qchHWchjK5l9MaenLzYPHvKGzdN6iMnn2QwhcdSJXr45F9TL6wKqUR8BJ_3UUf2JAZeDVWREFTnYsInvRu_H4Si3Lvw6XPjPAZ34CbTmMdkTrUq_GvmZet8dRHZGFUPaFCauwNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇮🇷
کاروان استقلال لحظاتی‌پیش با پروازی مستقیم از تهران راهی دوحه شد. مدیران آبی‌ها در ساعات گذشته توانستند محاصره هوایی ایران را موقتا دور زده و مجوز مستقیم حضور در دوحه رو کسب کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/108255" target="_blank">📅 16:38 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108254">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a64417ab8f.mp4?token=TDBMUzsjQ716euaOF8yAgqDTCmTNwWNWabxbhXKIhLK-qiPYwgpPLn0BbEMyovJjflB8dHB-LMPc63l5GAwCGi1seIauT3ggdRUnoMY9czkzA1b9wul5z5k1XhDSLpeIQRKQWrSofChroXnH3sT8OzTNXYGDi9XPdw-u4Mbs0cBiQ8cxwBxzbnmJu6YYpfbrGxcMaWoPxaWSi363fUjEujOD0LrQApyrY6c_CIxJgWvl2h0NqCP5SZPzopoLsDhbJ3WJJbibcVULhkE8IKwbltL47P7blq6l-i6gDmJAH7JFpeAoAJ1VpCGU1vHXwZK_yEBvlV9clPDEC-QxhCX1Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a64417ab8f.mp4?token=TDBMUzsjQ716euaOF8yAgqDTCmTNwWNWabxbhXKIhLK-qiPYwgpPLn0BbEMyovJjflB8dHB-LMPc63l5GAwCGi1seIauT3ggdRUnoMY9czkzA1b9wul5z5k1XhDSLpeIQRKQWrSofChroXnH3sT8OzTNXYGDi9XPdw-u4Mbs0cBiQ8cxwBxzbnmJu6YYpfbrGxcMaWoPxaWSi363fUjEujOD0LrQApyrY6c_CIxJgWvl2h0NqCP5SZPzopoLsDhbJ3WJJbibcVULhkE8IKwbltL47P7blq6l-i6gDmJAH7JFpeAoAJ1VpCGU1vHXwZK_yEBvlV9clPDEC-QxhCX1Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل دوم آرسنال به لیدز توسط برونو گیمارش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/108254" target="_blank">📅 16:32 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108253">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fb6a1e8ef.mp4?token=bH0gbKZjmV3lREl0XiUkr95vqZnuoYf_IafsolKTOo2uNnr9I-59inx-9JrY5hqMEDPijNxpB9jrtxpQd9LAeWkBEHgEdRUAtpIcfwwdEVjn5hz6YOcIKgK5t18RBNIp4_OLs9JAOv6iJIfDNraM_07PQ46OmSS4jc488vkIrQEsyj_LEZIkSH9NaBDUaXm93dqDHWWuf1Y9nOT87ZbhSFBJzhXmVNBkPJd82mhMSSeg4dAWu1r5KxeprkatXZTFZdd_0EACeudKKlQMLJ4F89JK_QTF9tIS6ylLsd8Lelf3Q83wB0tUw4owni5cnBWk3FDq643QT3iO7RYvaYlEaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fb6a1e8ef.mp4?token=bH0gbKZjmV3lREl0XiUkr95vqZnuoYf_IafsolKTOo2uNnr9I-59inx-9JrY5hqMEDPijNxpB9jrtxpQd9LAeWkBEHgEdRUAtpIcfwwdEVjn5hz6YOcIKgK5t18RBNIp4_OLs9JAOv6iJIfDNraM_07PQ46OmSS4jc488vkIrQEsyj_LEZIkSH9NaBDUaXm93dqDHWWuf1Y9nOT87ZbhSFBJzhXmVNBkPJd82mhMSSeg4dAWu1r5KxeprkatXZTFZdd_0EACeudKKlQMLJ4F89JK_QTF9tIS6ylLsd8Lelf3Q83wB0tUw4owni5cnBWk3FDq643QT3iO7RYvaYlEaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل اول آرسنال به لیدز یونایتد توسط کالافیوری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/108253" target="_blank">📅 16:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108252">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13447d981f.mp4?token=kMlZATfk4tNe9EC1Yv2ZdJqdUeMPm9v0qivHZ143amGCUjZKt9cgpPFVU-oolSG5u6sBVvDiymPHNn9EQlWDWAVlCl8_sF-EsCxFkyESmooP5piAqmY4L4-6wMi3UV-RGj6O7mJZd4Bd4q_-XabFZUaxUsJS3cfUQN0dAx9AohdE2GLWJJBzDgfS30F1ZXVjYUiMiqdkoHiCnOk3btZhYVEABAGsdKD9-1KFxAmoIsLTXaDO51NQL4rL0Y1_ds6-HEcD0dqbl2TTsyZQN2s338UXHjNIkI7fSaBvOpmwR2Tzy9ZV-sx-XEzgoNsqLPTNpf90gxkpxu0UESKJkmd8VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13447d981f.mp4?token=kMlZATfk4tNe9EC1Yv2ZdJqdUeMPm9v0qivHZ143amGCUjZKt9cgpPFVU-oolSG5u6sBVvDiymPHNn9EQlWDWAVlCl8_sF-EsCxFkyESmooP5piAqmY4L4-6wMi3UV-RGj6O7mJZd4Bd4q_-XabFZUaxUsJS3cfUQN0dAx9AohdE2GLWJJBzDgfS30F1ZXVjYUiMiqdkoHiCnOk3btZhYVEABAGsdKD9-1KFxAmoIsLTXaDO51NQL4rL0Y1_ds6-HEcD0dqbl2TTsyZQN2s338UXHjNIkI7fSaBvOpmwR2Tzy9ZV-sx-XEzgoNsqLPTNpf90gxkpxu0UESKJkmd8VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل اول لیدزیونایتد یونایتد به آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/108252" target="_blank">📅 16:18 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108251">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CcRVn8rnbOpgUZYWk_4FxJVF6WG8kwRbXPRc6qdgefYMcRfbl3szuCd4H1d9hdI9SEAtRs9Bl1buvVIgJOvp--tfxjBQm1mqC3hT2MNEih_zST3zo-VatBrurpy-tZ7hkZywop4p36QvASwsfSBtG8tTSsBVm9dvpJHcl8dnNfo2CClulMqaxvm3Snrvkhcc1aD_g1ppg4-5dQ0tq7xRW0SO5O2LX2KXhBKvWomAtoE_2neLffsk0uNEPj8lIfIVCAatYzUzrQEu2IxIcYoX_V82dI9RThpYeXsrgpICOH-7b8xAXnj_w115zWoC2XcnRE012NiRs_bWINUUD_QsCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
در فاصله دو روز مانده به بازی استقلال و الغرافه قطر، هواداران پرسپولیس درحال کامنت گذاری زیر پیج این تیم قطری درباره یاسر‌آسانی هستند. این درحالیست که آسانی بدلیل مصدومیت مقابل الغرافه به میدان نخواهد رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/108251" target="_blank">📅 16:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108250">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfPZN2lO1dLS-FR-rr3indR1gKB2L5NK8d1VEu5dWFY-SHs0nLjQyEny0XjtxOdKc-zyDca4dtm-PzPA4lcjBw28L4ZWXS61dsF0u1IBiDujWhVMo9wKtoicMwYMdnbGa0GChIYyc7z0FHSj8E9yOVprbwa6aMwx4FzIDWas5UN7bRRjq4qo6Go3kN6OtG2Buwxu7iwL_l088UVg599aChb4qQi9suOloycVCfRxc_W62EK1ronS7mzagnnsQonnsGWtQG8jeLVYy1D2Rg3132ZoPeuHxZ5xYS64KqSiZ8kqH8g6PkKxknIlVIdh3jiG0tzvtuA5XVWl32IZDQ7pdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇩🇪
شماتیک ترکیب بایرن‌مونیخ مقابل آکزبورگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/108250" target="_blank">📅 16:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108249">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85108132e1.mp4?token=aZ656RorSmv4EXKXxrqw4ZPx85WGLQb8DS59yNSSn5lf8w0zczu3Fhy7sr_xUk0xa0WscU4vts14p8hCUfXKvop9pNN4VmR0fr1BYtNFoZe9P-PNYPWjf9GlF4bjCP70W0UjGGHT4A0r-knS5vzkaZ8M_4MG_DBgCf0mh-Yy6BXpIfeo0-xrVNgZPy7R36UEwCYZm85sRmtX1-rUTkuJjezsm4EC9uDdI_bg3kAP82Ik8InsIbxARyKzBuTIkDurwkVtpTE9LQJT1hNv4r-r_AalaDHurzOZpg9VW5BbW8pumZTPBBJ-Q3vvR1qWwK8g55mNilPY0viFwOUUkptdt7xOCgbCkGyI47Bs4q3F4qeRpHDoqyChYolBCTNXa4eJ_nVSq1enSjpXjaCLRB2TPpGQ7MaskYbRmQonsPYYg1aPV4oPoFsFTi0nV0i6LkYy7pkaJ7erCkFW2GsGUPJsgI63LROIPa7WnuxWF715K_kzbV4TwC44OjVCK8-IEiXKwC3fr5NJodnuHtWyAfX8eIqlD4BZA1TX1Q7yeJjKcZEfqt12QswFfm8uV-rQOTya6H2qosGnhPI-zA9FhdFO3sxCnOEp9tstYRR-N88bBdpQfOl1XwNMPW4saaHW8FCuPu33pQNNoXEG-VmGPyM3xWiyb98RzosY4tysVu2XFz0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85108132e1.mp4?token=aZ656RorSmv4EXKXxrqw4ZPx85WGLQb8DS59yNSSn5lf8w0zczu3Fhy7sr_xUk0xa0WscU4vts14p8hCUfXKvop9pNN4VmR0fr1BYtNFoZe9P-PNYPWjf9GlF4bjCP70W0UjGGHT4A0r-knS5vzkaZ8M_4MG_DBgCf0mh-Yy6BXpIfeo0-xrVNgZPy7R36UEwCYZm85sRmtX1-rUTkuJjezsm4EC9uDdI_bg3kAP82Ik8InsIbxARyKzBuTIkDurwkVtpTE9LQJT1hNv4r-r_AalaDHurzOZpg9VW5BbW8pumZTPBBJ-Q3vvR1qWwK8g55mNilPY0viFwOUUkptdt7xOCgbCkGyI47Bs4q3F4qeRpHDoqyChYolBCTNXa4eJ_nVSq1enSjpXjaCLRB2TPpGQ7MaskYbRmQonsPYYg1aPV4oPoFsFTi0nV0i6LkYy7pkaJ7erCkFW2GsGUPJsgI63LROIPa7WnuxWF715K_kzbV4TwC44OjVCK8-IEiXKwC3fr5NJodnuHtWyAfX8eIqlD4BZA1TX1Q7yeJjKcZEfqt12QswFfm8uV-rQOTya6H2qosGnhPI-zA9FhdFO3sxCnOEp9tstYRR-N88bBdpQfOl1XwNMPW4saaHW8FCuPu33pQNNoXEG-VmGPyM3xWiyb98RzosY4tysVu2XFz0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
ماجرای خرید تراکتور توسط زنوزی به زبان نماینده مجلس سابق(عای هیمتی)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/108249" target="_blank">📅 16:05 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108248">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4HQIo1hI93OvqTLvkY3zJRLqH1HWcOn5Bb9Mz0AHZqMETjNFHooIsWuRa8fnvcryuBreJ8UJA5B3AWfVCHsfW-Z6qerua41B0Drms7zgz3rARNY9mknRnwcydO7puAnqAUFNeWIrXLrR9ltVPkrLTFHJLJq4y_s9FQBx0esSrhSWPJJEfCeyyUjF52ax8Yzf_axiyRZTY9S-r806L3PejJ72hLBfcJDT42rAcNlKD-mAudyXYIDAtLSqq6ct5l8vQkyMRQwful0LHBE8l46Sid2FbP6KxUZsqxY-jkT7NgC9T3xj0rXnZgMXvCvU-ZEitLZuhioND_ksI2Q0s0Bqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
😳
مصطفی میرسلیم، عضو کسخل مجمع تشخیص مصلحت نظام: تیبا با خودروهای خارجی قابلیت رقابت دارد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/108248" target="_blank">📅 15:49 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108247">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d024a83d11.mp4?token=XkseNjrgGEGt7yCz2ZYemwYthbYvnK9f8nR--IQirY786aDPcZV7zz6U6A8yxPk37b0qCC_adcbSbkz9vww0kBy2vcgATsKF1V-tPDk-nCGqJ7cQM_iAcw78JwG8uLf2aLA8DcYWDwBjQKix29RQfyLzejph03fhy_DfTlwbNAmVY_4e7BEqXTtM2EP3Bxef1nOx4s-4scLBT5b2uPlqzabWoTBpjyg7nNV0dCpVqm3G89Hyvuv3Y8ABdlM813ApCz73ycdwnC7na7XvO9TgmMFnRJ_YRmY8h5J7Xey2xCtvQ7evd4fkxfb61hYq1D-0ivS35FjOFfjlJDoJvt0EspbzmsumzRT5i1cn-M8JCxtDPzWd5-0lIK-_w7Ef0_d-LIySif2upXAjNHs0z2e_zbRHLVcZ4fqXAupclrCiAxTTwgP4IU33Uqy9Oso4ERWFYi5J0J7BI4A6Fo9BsXzTYdD3q6puChomkslNvWNtFeQT7ODLkIgTYetgjeWHRBYSUp7fVlTsUGW7PS9MMN8G7p1sSa-xDjJHZTIkKM1IB5wcgotjBMBTRO8IN9Myg03bgO-W1mIHsIe2H0eNF5TjV2vv7FxPSCTgO9q0CHtVNSy3GjAZ2jxSSmsq3H7EhuoDqqG_c8t-LHRAz6_UE03v5GLZzEn_Vgc7J3TnKfyeoHI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d024a83d11.mp4?token=XkseNjrgGEGt7yCz2ZYemwYthbYvnK9f8nR--IQirY786aDPcZV7zz6U6A8yxPk37b0qCC_adcbSbkz9vww0kBy2vcgATsKF1V-tPDk-nCGqJ7cQM_iAcw78JwG8uLf2aLA8DcYWDwBjQKix29RQfyLzejph03fhy_DfTlwbNAmVY_4e7BEqXTtM2EP3Bxef1nOx4s-4scLBT5b2uPlqzabWoTBpjyg7nNV0dCpVqm3G89Hyvuv3Y8ABdlM813ApCz73ycdwnC7na7XvO9TgmMFnRJ_YRmY8h5J7Xey2xCtvQ7evd4fkxfb61hYq1D-0ivS35FjOFfjlJDoJvt0EspbzmsumzRT5i1cn-M8JCxtDPzWd5-0lIK-_w7Ef0_d-LIySif2upXAjNHs0z2e_zbRHLVcZ4fqXAupclrCiAxTTwgP4IU33Uqy9Oso4ERWFYi5J0J7BI4A6Fo9BsXzTYdD3q6puChomkslNvWNtFeQT7ODLkIgTYetgjeWHRBYSUp7fVlTsUGW7PS9MMN8G7p1sSa-xDjJHZTIkKM1IB5wcgotjBMBTRO8IN9Myg03bgO-W1mIHsIe2H0eNF5TjV2vv7FxPSCTgO9q0CHtVNSy3GjAZ2jxSSmsq3H7EhuoDqqG_c8t-LHRAz6_UE03v5GLZzEn_Vgc7J3TnKfyeoHI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
🚨
‼️
عزیزی در فرودگاه بغداد: فقط ۲ تا سگ دنبال مهدی شیری و اعضای تیم افتاده بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/108247" target="_blank">📅 15:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108246">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1ba40b7cc.mp4?token=C4ZcSouptowSMCTW7IQOxD7He77-BJIr7SVYtB2yHttsNTXfCDy9TDIZuMKIt-GrB_xddcn6MG3QTyaXM78srPK2_TJR2_16bUn0mWCLvnCS5-vQ8U6qHEFRAyTM6R7L4KEbSXpBMLSuIoewxZmSPOxBVqfNjLGaz1v8RFv4JwFuRChE7vbtfngc8rHWpZ0MY3QJdQHFLOB1sCI9dUiMw5HC7FrR0k58DbCGxRdQnS-XvfT0rKYpiI_0vea_tsl9KFJoDiwa40sN6wduli0Vb0FZIvCp2znxTBN5TSOZI0LcS4x2i5dPFQttwqJI0sqfI9iA6zDjmkXLmsHPeCwhhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1ba40b7cc.mp4?token=C4ZcSouptowSMCTW7IQOxD7He77-BJIr7SVYtB2yHttsNTXfCDy9TDIZuMKIt-GrB_xddcn6MG3QTyaXM78srPK2_TJR2_16bUn0mWCLvnCS5-vQ8U6qHEFRAyTM6R7L4KEbSXpBMLSuIoewxZmSPOxBVqfNjLGaz1v8RFv4JwFuRChE7vbtfngc8rHWpZ0MY3QJdQHFLOB1sCI9dUiMw5HC7FrR0k58DbCGxRdQnS-XvfT0rKYpiI_0vea_tsl9KFJoDiwa40sN6wduli0Vb0FZIvCp2znxTBN5TSOZI0LcS4x2i5dPFQttwqJI0sqfI9iA6zDjmkXLmsHPeCwhhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد مدت‌ها فردوسی پور و میثاقی رودرو شدن
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/108246" target="_blank">📅 15:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108245">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a5e7db4ee.mp4?token=vxFLP86rSvCECBC8E4X2h1ky5T0F-QXApTBfhtQ0663W-8nbktR9306FA-zMUYY3Sulk8Ndl_p_02bdfP4oeY4YtUDu8NubZL1RfloiLNgqIDuveOQo-Z7MmcW3rFZd1qHK7DVpsQiz1xpyu_JLYaNiV0w3nOLJmZhOzMH-LEnDZLYDpWQ0Q2zV4YT3DmadffyRq_HNY6hyiHmWYu4UMmvnEbtvR5FvgH-itsYacXJyyGlSZah5uqjVfxKgDe4n2n0vieTtNVKPSShI2Pttw-VTEvlULSmY1Wjk9E1Tm_sln9FJvKz8IjJK143tFuB-g1yY3ApfJ0rqE6ZcHiIw9EAM9Lqny_aOyH_QZM-ZItTUr5Ute4PsK_LLa6_Bg0PI7VopR02N1ma66E_qrh9oETZvL8HuWmTswvRxGNlBQp5HYMmL6ssvEVHt5P__z0irVmQYJTNTSYQOA_qCLBfY4yQDA0o_DFInF01NvQ6nbFlHvUW8H7TRzTz4Frmf9ypt1_-82TXnAdphGLZW8UdAspv7f_Z1w8LTtNqhrWPyf9R5OAMRvp1o6CBCwi733UpByA-WvlnFgvr2dxhQBahcWc0euGR2h-pyiQO9MIsNKLCddfSEs9WchZNpCC0pKFONz3MJThxPC6Y0FSh1R2Qxuo8bWhiN5n2sUwQ83VIEaDCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a5e7db4ee.mp4?token=vxFLP86rSvCECBC8E4X2h1ky5T0F-QXApTBfhtQ0663W-8nbktR9306FA-zMUYY3Sulk8Ndl_p_02bdfP4oeY4YtUDu8NubZL1RfloiLNgqIDuveOQo-Z7MmcW3rFZd1qHK7DVpsQiz1xpyu_JLYaNiV0w3nOLJmZhOzMH-LEnDZLYDpWQ0Q2zV4YT3DmadffyRq_HNY6hyiHmWYu4UMmvnEbtvR5FvgH-itsYacXJyyGlSZah5uqjVfxKgDe4n2n0vieTtNVKPSShI2Pttw-VTEvlULSmY1Wjk9E1Tm_sln9FJvKz8IjJK143tFuB-g1yY3ApfJ0rqE6ZcHiIw9EAM9Lqny_aOyH_QZM-ZItTUr5Ute4PsK_LLa6_Bg0PI7VopR02N1ma66E_qrh9oETZvL8HuWmTswvRxGNlBQp5HYMmL6ssvEVHt5P__z0irVmQYJTNTSYQOA_qCLBfY4yQDA0o_DFInF01NvQ6nbFlHvUW8H7TRzTz4Frmf9ypt1_-82TXnAdphGLZW8UdAspv7f_Z1w8LTtNqhrWPyf9R5OAMRvp1o6CBCwi733UpByA-WvlnFgvr2dxhQBahcWc0euGR2h-pyiQO9MIsNKLCddfSEs9WchZNpCC0pKFONz3MJThxPC6Y0FSh1R2Qxuo8bWhiN5n2sUwQ83VIEaDCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🇮🇷
آنالیز ساختار دفاعی استقلال در این‌فصل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/108245" target="_blank">📅 14:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108244">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bed940014.mp4?token=NIc2KT1l5CxfPKgdXfVRk5QwN-mwPtYF0YAwfU9Gh0wYmnd3aNiE7ITHN8W76fL9UwNcrVhMM6MHZxu2Cjlsta0BD7EDTS6sDx_85UJTd8Lx1PpuBZ1fg5zPSfYz4h7jkoGL7lksVHvoqHNSDFk73wmEXMlnS_v8W2LLznHAuf7mslWGCDMor1rldgpJwg4UAxZGXNiF6O0gmJWUSW8pSjFPRINsQhAdUUVIPNF4_XE68m9ltVwB3tu7JcKEfNntcPaH9wUX3fGomk7V0Bksyiyzr1a-48i-HxCvhwK3NWsIDojTV708O6KafipEpJkr-Q9rWSbgcxCqcCKlmH01ynYt4y_5m1D5Ji6XO5l3txuVvoQEnXYt67tN6XbMu7Zigu9AsoMdqbxVi_xkyf0B8FVy8GGZOCY7TdJSocV-YboS6HzeJKRlXLLSN2n9BI2BnwVW8fGWXqQI_QOpwji1SGa5mMBS-ISyGjHsc4su46BuoBH3frxwCjUWr1wqhHlvy9NmrFfDfbLHdCClRI6Sj6MGVig-8a5ujAplOE827qPDthg-oj39FdtVGcj_7bSUiaqeWh4YoQe2CC2vDP_qKioBaboaAPSbYv9-2CziPlOJKGJ_uFdQWyr8tTpIMm8WYMmV5uY1I-FAGy_O483GkwwLJNWFJcOZSB3AXsJZAoM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bed940014.mp4?token=NIc2KT1l5CxfPKgdXfVRk5QwN-mwPtYF0YAwfU9Gh0wYmnd3aNiE7ITHN8W76fL9UwNcrVhMM6MHZxu2Cjlsta0BD7EDTS6sDx_85UJTd8Lx1PpuBZ1fg5zPSfYz4h7jkoGL7lksVHvoqHNSDFk73wmEXMlnS_v8W2LLznHAuf7mslWGCDMor1rldgpJwg4UAxZGXNiF6O0gmJWUSW8pSjFPRINsQhAdUUVIPNF4_XE68m9ltVwB3tu7JcKEfNntcPaH9wUX3fGomk7V0Bksyiyzr1a-48i-HxCvhwK3NWsIDojTV708O6KafipEpJkr-Q9rWSbgcxCqcCKlmH01ynYt4y_5m1D5Ji6XO5l3txuVvoQEnXYt67tN6XbMu7Zigu9AsoMdqbxVi_xkyf0B8FVy8GGZOCY7TdJSocV-YboS6HzeJKRlXLLSN2n9BI2BnwVW8fGWXqQI_QOpwji1SGa5mMBS-ISyGjHsc4su46BuoBH3frxwCjUWr1wqhHlvy9NmrFfDfbLHdCClRI6Sj6MGVig-8a5ujAplOE827qPDthg-oj39FdtVGcj_7bSUiaqeWh4YoQe2CC2vDP_qKioBaboaAPSbYv9-2CziPlOJKGJ_uFdQWyr8tTpIMm8WYMmV5uY1I-FAGy_O483GkwwLJNWFJcOZSB3AXsJZAoM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🎙
🇮🇷
على تاجرنيا رئیس هیئت‌مدیره استقلال: از فحاشى هواداران به مادرم خيلى ناراحتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/108244" target="_blank">📅 14:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108243">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/879a0a76f5.mp4?token=CWIxUKx2TrZ8J7rJYr0tJRQVjW09NGhAnaP-AOinQrfhzY9LPTBIXsk1e0-LhQmMd7Q4-IR-oQZn3Zzo3wZ7ToYgS61cmv-3SxHnOjHN8J2OtNJ0NeltrIVGZGQS2KfJQ80C6Metbfrm80YO_Ib3xX6n92Wqq0JL2cf46JKrJM0Sxi7ST6hukUZI20CfLJnVG5uy3mQHFTYBDk1WGXehdzfGcyQ-IPTILUp_lCFWWfxlNW0dsHQR8uUtvgOkT4L_FJ9JGrqbOGjwk2rVKxNkHYqkOlSWxKFtKR3kjE0lv-3Mtics9GFdzN9fnqq5_UYWLOaApMEbxu6hzTd5agl4UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/879a0a76f5.mp4?token=CWIxUKx2TrZ8J7rJYr0tJRQVjW09NGhAnaP-AOinQrfhzY9LPTBIXsk1e0-LhQmMd7Q4-IR-oQZn3Zzo3wZ7ToYgS61cmv-3SxHnOjHN8J2OtNJ0NeltrIVGZGQS2KfJQ80C6Metbfrm80YO_Ib3xX6n92Wqq0JL2cf46JKrJM0Sxi7ST6hukUZI20CfLJnVG5uy3mQHFTYBDk1WGXehdzfGcyQ-IPTILUp_lCFWWfxlNW0dsHQR8uUtvgOkT4L_FJ9JGrqbOGjwk2rVKxNkHYqkOlSWxKFtKR3kjE0lv-3Mtics9GFdzN9fnqq5_UYWLOaApMEbxu6hzTd5agl4UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برادر چالش را پر قدرت ادامه می‌دهد
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/108243" target="_blank">📅 14:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108242">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SV4uo6ZDhrJaZMxbJ_kOxcFeVEoeoMxgDPKwRwYc9kiD1IxIuGxI1z0jSuUYNz07TSt_1Rfomn_SI6nBzgIX1X9cA7V4htvjih6uwKJTOi-50F4j5-fJRIYBY8Ez-8CyqXS5i_BAgs6NyeH46y9jYM9o622G0Pb7b0GagpvBCwjeo7u2lHo3b_wSf2Kga4M09ljsPsk7upVBJ4u3wGNvt0dydxhT-DN8WBfv3Eb2MGqC314OVXdYJ1L1TQTK44Er9P1fd5ltwZPURdvIdtlfozCGEjya0EOrnU0ktsJ3Frwsn4QDfPlF1FZSLwTetDPBo2QbtO33_qGrcvdsBn1b6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
لیست بارسلونا برای بازی با ختافه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/108242" target="_blank">📅 13:49 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108241">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5kDH0_GcSEQlbjhZlg1ovmd16LDVTTtsTOLkQNJbEbtUQHh5buAL4_m_lT1hHVbAz-zyK-2ceXu1Z8iTGJv4m4hRCgCWoTYPgoKPek8Lhx4gzhe-hboRVh-Sy426tBd4S-l1-nejK9Sgtt23EnbeiZH1xj9_3OBC3HkoNXvsMvuQw9dPlKbyhDrrrV6CdJ4X0-UrBikEEWXK4ajY5DRTndH1VZBfb1HFXGLtROTBF3GK97iMONbbqsFYtSdjO6tj6kNy3Y0SeJ_7G-zjtBHcmrRVGYWVL1FLIvMnFhZHSXBVPTZEE-mUc5PTXs2vJQciSUfooUAw-PPsrDtK9HmuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب آرسنال برای بازی مقابل لیدز؛ ساعت ۱۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/108241" target="_blank">📅 13:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108240">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCk-lsDrZCg4KoBuTMMbvrWC1aKt3Q9gA1H-3SAUHGXX2M0S23sZAOwhdgA8Y9NMQP0UcDU6AOu8VtN2-NQZyomwzXtIhxQJI7OD0a7HbmJrhdZL7JF4nLze6VqK8BMMGSWlQJpW8TD3PM_zlTyVX8sXT8TOnC9BKHKAC2b3O-c_Ro7LkMzBthfz2X2bOAwlJii8n4fkyz16qC0Qdu18cbrSb_ErkF5TCU6OopAjN2T3cYROLCyd_3Vv6iCGHb59r-DVYgbFPzIQOeZcD7GYZkswFud7l2S6HO32TIvfwsrzlj3CHZpbQxaeIvAOv6Z3fzICD2rraMAPB9uUjPF_Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚔️
🔥
بازی‌های باشگاهی بالاخره برگشتن و قراره طی ۴۸ ساعت آینده این بازی‌هارو داشته باشیم:
😍
🇪🇸
بارسلونا
🆚
ختافه
🇪🇸
🇪🇸
رئال‌مادرید
🆚
ویارئال
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچستریونایتد
🆚
تاتنهام
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیورپول
🆚
منچسترسیتی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/108240" target="_blank">📅 13:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108239">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90ee39992.mp4?token=hRi06-wSGl7_8xc4D0EnHCd7gmXbqQuGD15FhAXlMx_PMUTYla8YFEztrNriy8Rgtx6gHkoGd_NTHpsMREHUGVV2mioNsRNplpFOr1QS8_iWvmsKLQFuNGy-LMq2FhOJiO8uGPF6lw6vt8NoOFZUKVzCMQx-1JjscwvjRPO9A2gzVExqaPG6blVtVFTX3XyEPftXPSQZ5n9N1-SnOHEnB3M7kgAOhzAfKzXljifFVUHwCxvUsJP74ogad6SbVezzF4TlfzepHA-xQFDzejsyOMa5L2S_b8mZ9vrveSpCwQZZ9VsnNl2891rggw4vmKcAH6wQLebW3pie-i4knMsn6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90ee39992.mp4?token=hRi06-wSGl7_8xc4D0EnHCd7gmXbqQuGD15FhAXlMx_PMUTYla8YFEztrNriy8Rgtx6gHkoGd_NTHpsMREHUGVV2mioNsRNplpFOr1QS8_iWvmsKLQFuNGy-LMq2FhOJiO8uGPF6lw6vt8NoOFZUKVzCMQx-1JjscwvjRPO9A2gzVExqaPG6blVtVFTX3XyEPftXPSQZ5n9N1-SnOHEnB3M7kgAOhzAfKzXljifFVUHwCxvUsJP74ogad6SbVezzF4TlfzepHA-xQFDzejsyOMa5L2S_b8mZ9vrveSpCwQZZ9VsnNl2891rggw4vmKcAH6wQLebW3pie-i4knMsn6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
باهنر: ایرانی که صداوسیما نشان می‌دهد کجاست که ما به آن پناهنده شویم؟!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/108239" target="_blank">📅 13:35 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108238">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MuMw4nni9-q_vdlYo6pAllmrXa2kkSvmIw7z_DyhtMDehH9c1_zDb2OTP7b7FBqePuES2E99p9WDWp7grSDvN4BTq5YHk2cWJDeqCEIy6yJZV9UKBNgwccEGrgvB_mOxQPAviOjAgTOhLnwLtyh5COL8N4DKa7-mtBVHqCDpbn4GE55OKKc3JAiTuuw68HmrE_Iju5g_amiClQIld-FVDkPmr3-7g6xmyMrKnXladDpSu5CTeVt41iiCBx1roR3Cu-AdBO1Xwd4EGj3HO6kJIUrN3v8_8ghWtpsG8TDWq8kfJwwPEaYPTlpBsQv6dcgN1Mr44w7uoz2de01BPhW54Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
قرارداد کول‌پالمر با چلسی تا سال 2034 میلادی تمدید شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/108238" target="_blank">📅 13:24 · 18 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
