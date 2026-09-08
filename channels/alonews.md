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
<img src="https://cdn4.telesco.pe/file/iFi5XvlBLPrOdghwSKbo3rsmT6J8NefTDpmM2MaujNGFLpc5Xr1HKyLPdEtFEaxMFPYVCg0qxZ6Xg6CoXXKBY9t7Lf2pQdt2cWu3UCJHDtc7nMpnRha9UAQG35ErEkEFqjN1Tl64xZTnYiHlyGcsgQD8ssZVrbwLZncwkcg8WCyP3WCJOAX8RMDstqNtLGyRte2ACBX_54xpjFmNhJCUW19pIZdHFrRZv5Sgb7-lKBG4p8FIjYk2Fmwew-feTTLKhm9drDRErod1H2I_GStVyJtl_KlMH79YifL_NurBwTUnN9gXeY9rLMeYElRwVMimV_q44xRcUtMhPHwiu4VybA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 928K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-17 13:27:39</div>
<hr>

<div class="tg-post" id="msg-146221">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
سخنگوی کمیسیون انرژی مجلس: خودروهای نوشماره و وارداتی طبق روال قبل سهمیه‌های خود را دارند و برای آنها محدودیتی در نظر گرفته نشده ولی باید هزینه نرخ سوم را بپردازند.
🔴
در مناطق آزاد، نرخ سوم برای خودروهای وارداتی اعمال می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/alonews/146221" target="_blank">📅 13:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146220">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
زلنسکی: «به نظر من، ما همچنین در حال حرکت به سمت مذاکرات سه‌جانبه هستیم.
🔴
نشست سه‌جانبه بعدی می‌تواند در امارات، سوئیس، ترکیه یا کشور دیگری برگزار شود.
🔴
ما در این کشورها تجربه برگزاری مذاکرات را داریم و از سوی چند کشور نیز دعوت‌نامه دریافت کرده‌ایم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/alonews/146220" target="_blank">📅 13:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146219">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahN0U7Z_S9lDA2scBQaDuTlQZsfcNWkj0f0WWSVJfYBGef498oTcUq4QL12tqU9JoQ4g-xJrcFITfyPpx8LS59Ds5DiGvg1nt-wK3nUUfutGztg1tj2w-0rITnCS67749pKXXcg51C9YOaS7v9uZqrPwmsMSlBrBVTdKh8ILmV4h8pH579Kf9i8ZzBRznkmMKTKOkEwC9WepoebBzkt2UP24Gve4buDfpx6T2uGiQZ4bljAeAciRGNETdOHakGZ7NTPIfhQs2QCCrhdLtQyke58g2YJLgfDFshNUY5fRRoHaZj4VELru74Af12Oy09kv40HV-S30eeCdKXmV0W4LiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار وزرای خارجه روسیه و عربستان درباره ایران و تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/146219" target="_blank">📅 13:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146218">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ee5639fcf.mp4?token=N_xXH8JQWNlms5e4sVftTG434fidv5_25OOQd6fOVrxXD0o2YvvVAV7BBKTCSS3O2FDFeR1Bp59y7xfXBHhiR17wYbFAGs7d-75DSTGbuKN0xVuNrzjrD_m3i6XiPXw-v_E5wrLM4j0F-Fc96sxgKT1QZAnu4_yq8PVeAYxrKEMJDGeqLNMRvtd8OgYtfOr_k1CyKRZlUJ-Cd4dq9_6SQUYq6ePiFi1XcIqm_TGit_xzFdgdj0qrQa8Ntn0-8_LupTK8jMEpPw2oEZ-aC-JN-GLaMrsEx8A7jOwZOtmMZw6et8OAm-WifmIDB2rQe_KN5ktvTBL_BUZ7Gq28Z0KV2Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ee5639fcf.mp4?token=N_xXH8JQWNlms5e4sVftTG434fidv5_25OOQd6fOVrxXD0o2YvvVAV7BBKTCSS3O2FDFeR1Bp59y7xfXBHhiR17wYbFAGs7d-75DSTGbuKN0xVuNrzjrD_m3i6XiPXw-v_E5wrLM4j0F-Fc96sxgKT1QZAnu4_yq8PVeAYxrKEMJDGeqLNMRvtd8OgYtfOr_k1CyKRZlUJ-Cd4dq9_6SQUYq6ePiFi1XcIqm_TGit_xzFdgdj0qrQa8Ntn0-8_LupTK8jMEpPw2oEZ-aC-JN-GLaMrsEx8A7jOwZOtmMZw6et8OAm-WifmIDB2rQe_KN5ktvTBL_BUZ7Gq28Z0KV2Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلنسکی: «ما به بسته‌های موشک‌های بالستیک از آمریکا نیاز داریم.
🔴
آنها به‌طور دقیق شنیدند که به چه چیزهایی و در چه زمانی نیاز داریم
.
🔴
من روی دیدار با دونالد ترامپ در ۲۰ سپتامبر حساب می‌کنم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/146218" target="_blank">📅 13:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146217">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82015a4d76.mp4?token=dCnfzXGXgRX2h1HGw5FFQfe9mLeWAIa6J39e3ab6BtzlWJJNu-NbiH7TYxhMmEw2HFzPIG3eWiRBnqHY5u9PWeahgFAO6iIRrKEyQxJ02st4S9EA6PnhZh_XmaVa71IC_gZLNefJreVc8m6aBEc91GAAo7CKkZXhDnYPzrrHtOQispUGV_VyomXBRNTIVdtJRLMB5AXcVIyGq_RpKPMmFUTw-sMb7QOQeJL5-X2_FnDXSMc3WJCPf3QMyC-Dj9L6YkJK9uDk1DU6MC03SgeLcskrygk8U7RcZed-f0v0lnzG1jQoNOLQALDljlvWJRprJjEO5JyDp8_9sYHNo5wfhXiKAUK6FiOxXujC3Q8TrJmvx1svYJtsUFUj_IrJiPhk88U78iSMxsG4v9efo1iq-v431b9osJcZSlToFNGVIgwzzpMED3mlMTDZbCDi4zLfEjq_zwQHDeOrJFv8Zeq63K003ofqB7PVDzsMsPjJfrlPi_K4K1wmXh55ucL5xJByWjgpW0ajV49y_gIQb2aCAov3rlyWBu-BNEHoPhcgmrAC70LKBf0EUd0LIsh0IrAWKUqmCLiTQl0Id-F2Xl8pRBG9694cWCBeKL4eD9s9DFFSAjusifaf4sESWKrND4HgxygWQJ2yjqUIUjZ1Dq6wKqIi27_0TKRKfS-7StDT5Jc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82015a4d76.mp4?token=dCnfzXGXgRX2h1HGw5FFQfe9mLeWAIa6J39e3ab6BtzlWJJNu-NbiH7TYxhMmEw2HFzPIG3eWiRBnqHY5u9PWeahgFAO6iIRrKEyQxJ02st4S9EA6PnhZh_XmaVa71IC_gZLNefJreVc8m6aBEc91GAAo7CKkZXhDnYPzrrHtOQispUGV_VyomXBRNTIVdtJRLMB5AXcVIyGq_RpKPMmFUTw-sMb7QOQeJL5-X2_FnDXSMc3WJCPf3QMyC-Dj9L6YkJK9uDk1DU6MC03SgeLcskrygk8U7RcZed-f0v0lnzG1jQoNOLQALDljlvWJRprJjEO5JyDp8_9sYHNo5wfhXiKAUK6FiOxXujC3Q8TrJmvx1svYJtsUFUj_IrJiPhk88U78iSMxsG4v9efo1iq-v431b9osJcZSlToFNGVIgwzzpMED3mlMTDZbCDi4zLfEjq_zwQHDeOrJFv8Zeq63K003ofqB7PVDzsMsPjJfrlPi_K4K1wmXh55ucL5xJByWjgpW0ajV49y_gIQb2aCAov3rlyWBu-BNEHoPhcgmrAC70LKBf0EUd0LIsh0IrAWKUqmCLiTQl0Id-F2Xl8pRBG9694cWCBeKL4eD9s9DFFSAjusifaf4sESWKrND4HgxygWQJ2yjqUIUjZ1Dq6wKqIi27_0TKRKfS-7StDT5Jc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مایک هاکبی، سفیر آمریکا در اسرائیل:
«اگر بریتانیا واقعاً به دنبال برخورد با مسائلی است که آنها را نادرست می‌داند، پس تحریم‌ها علیه کره شمالی، چین و روسیه کجاست؟»
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/146217" target="_blank">📅 12:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146216">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b2ae4bae8.mp4?token=P3y6fiiuVymaQ8GpzE1MbL8Nagf7UHzUXb4N2Iun3oN3Yfd4rmMnggEgPnz9eeSkuqnwl8BWthJIl6-517M7JLG0JRnSav1In3t5u8K7W6bfubdRJMD88qkx0O5S53RkwNVrtDqjQdWzRFuLOPM21JJneevjTriucKkSobK2opi6szCRMqxHlJkz8lSLywLW7rNPslxVy1rUDLbw92FeF1AgBMlU35zizCHITXibbDmq8ZJM2jtzthTOeuJI4dbToZp4Lcbbdjd7GI19KZHLNhN8361c70KRzIGAciiScgGNgy_AagBcEBwA7csvVEY0ufBzUqDDIYzaVzFu6s1aYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b2ae4bae8.mp4?token=P3y6fiiuVymaQ8GpzE1MbL8Nagf7UHzUXb4N2Iun3oN3Yfd4rmMnggEgPnz9eeSkuqnwl8BWthJIl6-517M7JLG0JRnSav1In3t5u8K7W6bfubdRJMD88qkx0O5S53RkwNVrtDqjQdWzRFuLOPM21JJneevjTriucKkSobK2opi6szCRMqxHlJkz8lSLywLW7rNPslxVy1rUDLbw92FeF1AgBMlU35zizCHITXibbDmq8ZJM2jtzthTOeuJI4dbToZp4Lcbbdjd7GI19KZHLNhN8361c70KRzIGAciiScgGNgy_AagBcEBwA7csvVEY0ufBzUqDDIYzaVzFu6s1aYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصویر منتشر شده در رسانه‌‌ها از انفجار در تاسیسات آرامکو در پی حملات حوثی های یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/146216" target="_blank">📅 12:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146215">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
خبرگزاری رسمی بحرین: پادشاهی بحرین حملات مجدد حوثی‌ها به غیرنظامیان و تأسیسات حیاتی در عربستان را به شدت محکوم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/146215" target="_blank">📅 12:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146214">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
نماینده مجلس لرستان: کشور با اعتراضی روبه‌رو نیست و مشکلات معیشتی در حد گرانی‌های جزئی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/146214" target="_blank">📅 12:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146213">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
عارف، معاون اول پزشکیان: حتی قیمت سوم بنزین با نرخ ۱۰ هزار تومن هم فاصله زیادی با هزینه واقعی واردات داره؛ هزینه واردات هر لیتر بنزین برای دولت بیش از ۷۰ هزار تومنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/146213" target="_blank">📅 12:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146212">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6de408d162.mp4?token=qMAsREY5Cay7nA5LDttWqVglDQSaLUt8-IZizHAtil07JdPLPFc2rbUCeqDDqQfmWwOlHZ1w7tJqRBNQKrUKqnoBzkNtPHERLEp8NFiWm-GW-U_3ZlJuToqgciqn_pZ-3jirqBc12DOe5ACM0A3jNtoONiZvbNA5WWYkn1BgCN7lkx0_4VbLyKlxHJiLemMGyaIyKdcgw8CgJ2rlW2MCf57kx8F7WLrWedhlgFMNo61t4uBW6iNVJ64104MLBpDETSwU1s5T7LC2P_azlKYFoeEOAjRPhcqho7cUUJOwUZ1IE8EkV4fZE7dQRY6HCSej0V8wmLxXkBZdtV_PLavPTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6de408d162.mp4?token=qMAsREY5Cay7nA5LDttWqVglDQSaLUt8-IZizHAtil07JdPLPFc2rbUCeqDDqQfmWwOlHZ1w7tJqRBNQKrUKqnoBzkNtPHERLEp8NFiWm-GW-U_3ZlJuToqgciqn_pZ-3jirqBc12DOe5ACM0A3jNtoONiZvbNA5WWYkn1BgCN7lkx0_4VbLyKlxHJiLemMGyaIyKdcgw8CgJ2rlW2MCf57kx8F7WLrWedhlgFMNo61t4uBW6iNVJ64104MLBpDETSwU1s5T7LC2P_azlKYFoeEOAjRPhcqho7cUUJOwUZ1IE8EkV4fZE7dQRY6HCSej0V8wmLxXkBZdtV_PLavPTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مهاجرانی: قیمت بنزین سهمیه‌ای افزایشی نخواهد داشت و فعلاً همان ۱۰ هزار تومان خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/146212" target="_blank">📅 12:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146211">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
پیروزی AfD در آلمان؛ فرانسه نگران تکرار تاریخ در قلب اروپاست
🔴
پیروزی تاریخی راست‌گرایان در انتخابات زاکسن-آنهالت، تنها آلمان را با یک تحول سیاسی کم‌سابقه روبه‌رو نکرده، بلکه در فرانسه نیز زنگ‌های خطر را به صدا درآورده و آن‌ها نگران تکرار تاریخ در قلب اروپا هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/146211" target="_blank">📅 12:07 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146210">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
نشست فصلی شورای حکام از امروز در حضور نمایندگان ۳۵ کشور، با محوریت ایران برگزار می شود
🔴
آمریکا و سه کشور اروپایی در این نشست چند روزه به دنبال ارائه قطعنامه‌ای برای ارسال پرونده هسته ای ایران به شورای امنیت سازمان ملل متحد به دلیل نقض تعهدات منع گسترش سلاح‌های هسته‌ای هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/146210" target="_blank">📅 11:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146209">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
زلنسکی: آمریکا به‌دنبال کاهش تنش روسیه و اوکراین در زمستان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/146209" target="_blank">📅 11:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146208">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRiZpKISLFcSnsDxkb-e9LbYMar31FsqGPI6fL9WYKGRHNlt8CcB2XsbIdsb-vuGr1ccPKbf_AopxDfmSJnBAhmjc850WDDDX3HyIwqwIXh3wG_so0C6r3YfblREPpfaNDKv0V1ubJ2-cC58KXOSyMmbHDB0CTU-aqTSBKO7W_F8ZzLSkvDH2vQSD0hJ6Kz2oRUNUkXqe6840LyRj3re8Holizy5omXjH4jPcG5sAoRO0tmXPhVxB5Uh1nx7ItDP9Axfg9la3htNGwu_wInbVYILK6TDhcJZIRO0uQ1QgxZSguwRFFgwI4Ac9qMJOJWau3q4Qah9ZIOqxhy-Fn0byw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت، ۹۹ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/146208" target="_blank">📅 11:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146207">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
حوثی‌های یمن (انصارالله) اعلام کردند که ده‌ها موشک بالستیک و پهپاد را در طول شب به تأسیسات شرکت آرامکو در شهرهای ابها، نجران، شهر اقتصادی و نیز شهر جیزان، و همچنین پایگاه هوایی خمیس مشیت در جنوب عربستان سعودی شلیک کرده‌اند.
🔴
حوثی‌ها مدعی شدند که این حملات "آسیب‌های جدی" وارد کرده و هشدار دادند که حملات بیشتر عربستان، "حملات قوی‌تر و گسترده‌تری" را به دنبال خواهد داشت.
🔴
این گروه اعلام کرد که این حملات، انتقام حملات هوایی عربستان به مناطق مأرب، البیضا، الحدیده، تعز و الجوف در سه روز گذشته (121 حمله هوایی) بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/146207" target="_blank">📅 11:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146205">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cC9LuRxgwPQd4Y4XPyN6vQwNd8JgWPatJdYf8d8f24SFM682WpNg7iwCu41Bl_ts5u1K5r8SPEXZCU3F5P-vMlSd35-qmGEs-u5wOikgmtdiTDHDCNagBqeM_1wokFG19oXTWFdnVb5h7RrEYJLfBpcmubsgLwiFKgcgNjNqqWfHkHKsNO09ShgeQcLFXrQhdGEQNB5DSpRt7Qnl2eVDfucRgo7agFkugLvnTQK9CLRopFvOgj_EqK3pPHCB18bfmDk45FMcV0Svdr-DaCY1LIQjHOs2ufEyFQ8Z25_rm6A00r9-fP79QpUebyCBK5xw-K0blxlxIxRovos6qywLDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g7CdsD3N6AFIY6wm_MdgGBWGho4DbbARb_VbaCNAEdnUNudaJ2ZW_xo4jtkKqysw3nD7Ms5Ft5zZX2HhQJ7ng7-E9edB_RAEd5ua-7j6iW8JcMSf7m_fz1MHCw9B5WZCQBeRrQTFrQIK0YJOC1VlfDhpmj9n9ge2CH5tuekFI3QppuNEsxCsNiDQWoMT1gFJZ2VrY25Gtr3d6nPjHjUL-G7X0t6fdjn2L4F8w5Vo4ShwdD6qjytLtW4Phc4HrNK3Jaf9xcj1OIZi_nV-1k7BZhKYYPhZRZOc3cV5nBW6ECPGUfgmo7aF_CVmbqT1gY68lE4orKLU1Spva1DHSLX51w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
پالایشگاه جازان همچنان در حال سوختن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/146205" target="_blank">📅 11:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146204">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51b51a6424.mp4?token=ZhFm02DkfHhh1BdwolGSLcNNtc4dgAzdnKuZDpwzTmhwmATSyPnRp-B2qF0AeALOmcogwXPtbuSO4M1NJVtYgaG7LFYoepDCm-y8LSAtyVlBeW_RbaPfFsRZMfZyXrtx8jPVCUIf0XjKO9RG-EFhhfOjJy81vpDHuofmvWCmvgmoO6dbzBgJkI--FzEl5CXMPc57A_3cuYY67T1qxn4xAOB8Y08CQ595yJVRzB4Lv7xzKNWQ4U9gEwECAfJQTvjxquBTnvkcXhEW5kh9euUe49D14HK6j1KOqUh4Ot7fsTWI9uFlPSdbQ5PnZCEYRwyVFkGmlWmIePXyZdCNGU634Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51b51a6424.mp4?token=ZhFm02DkfHhh1BdwolGSLcNNtc4dgAzdnKuZDpwzTmhwmATSyPnRp-B2qF0AeALOmcogwXPtbuSO4M1NJVtYgaG7LFYoepDCm-y8LSAtyVlBeW_RbaPfFsRZMfZyXrtx8jPVCUIf0XjKO9RG-EFhhfOjJy81vpDHuofmvWCmvgmoO6dbzBgJkI--FzEl5CXMPc57A_3cuYY67T1qxn4xAOB8Y08CQ595yJVRzB4Lv7xzKNWQ4U9gEwECAfJQTvjxquBTnvkcXhEW5kh9euUe49D14HK6j1KOqUh4Ot7fsTWI9uFlPSdbQ5PnZCEYRwyVFkGmlWmIePXyZdCNGU634Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیشب تو شب نشینی خیابونی برای مجتبی خامنه ای تولد گرفتن
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/alonews/146204" target="_blank">📅 11:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146203">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8b78bcc6b.mp4?token=NNAQYqc3rTHAAGo9jC5N354RI1--Y7gwORH_DBxqGya9Zwc5lhBabuE8Pv5GTdTjt7-nSc8nGJFsTIWliXH60aTLAK8-_ey_Li5xDDQ5h6jWgqEnvwkvVsGR1lOvCkfai_ayHDwle-99RfG5KL44sQY8w7i_xKQOgb4IFDkRINZ-W65xgkXHfjBOPZIkA7QCjfVKUfx-6bKkgiRdIJMzwLicqtiwcSjhzplaPxeJLCpXPPJs0xooU3LscUpaaS51kraFujJsCdHPKwlk3hV9YQ_CeGZIoQXiK9mqhZCAJDbyjm89vlj0ZdOW7ca3JS6Iy_Qxofzi4S4U0oLXm79LjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8b78bcc6b.mp4?token=NNAQYqc3rTHAAGo9jC5N354RI1--Y7gwORH_DBxqGya9Zwc5lhBabuE8Pv5GTdTjt7-nSc8nGJFsTIWliXH60aTLAK8-_ey_Li5xDDQ5h6jWgqEnvwkvVsGR1lOvCkfai_ayHDwle-99RfG5KL44sQY8w7i_xKQOgb4IFDkRINZ-W65xgkXHfjBOPZIkA7QCjfVKUfx-6bKkgiRdIJMzwLicqtiwcSjhzplaPxeJLCpXPPJs0xooU3LscUpaaS51kraFujJsCdHPKwlk3hV9YQ_CeGZIoQXiK9mqhZCAJDbyjm89vlj0ZdOW7ca3JS6Iy_Qxofzi4S4U0oLXm79LjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بامداد امروز، بارش کم سابقه و سیل آسای باران در بابل
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/146203" target="_blank">📅 11:26 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146202">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
رییس کمیسیون برنامه و بودجه مجلس:
مقاومت هزینه دارد و مردم شریف ما صبوری بیشتری خواهند کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/146202" target="_blank">📅 11:21 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146201">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
خبرگزاری آر تی ترکیه: آمریکا پیشنهاد جدیدی را از طریق میانجی‌ها به تهران ارسال کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/146201" target="_blank">📅 11:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146200">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
حموم بودم برق رفت! خدمت آقای وزیر نیرو
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/146200" target="_blank">📅 11:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146199">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-pPzclf5GvqVfZ-XHNvlwoUa7rnI3bFIm2AQJawRuZJr3KqW45rmkLkoISjuivreDjJxmm8NmZb8u3LTzGSzhZ8S-WpbCEGppY-MRgroikhZ5i5LTw09Dg8xDAd4PaMN2FJmWWJrBSxqp9dc2OMwsdxGL78V49M57F95Exvv5kZ45U0rtYD1GylC7n07xHNDFrkn6e3M_BdZjSLq1YSV0iViAa-qqKz7ocUC0RuBacmnaJlu6oX3NUaRjSxpcvTkkd8T8pTWEw4aD-Wfh2Jc_tTgRpKvimQAs5hfqe1MS2a0Dw0qc7ATPP7syTtImnOOYDRzmgnSEBV3w_XUrJIXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهند که آتش‌سوزی در یک نقطه از پایگاه هوایی ملک خالد در خمیس مشیط، در اثر حملات یمن، رخ داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/146199" target="_blank">📅 11:06 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146198">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
مسکو: ایران خواهان ساخت نیروگاه‌های هسته‌ای جدید است
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/146198" target="_blank">📅 11:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146197">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMtBxBYks4MuzfA3EWtm5Q8touaehsPBxCdJ6E3IzVMUXWFaXwc9-krlMUNTqzOLFcMUok-j5_1AO1OKU3ppA03tgneiJ2NOMBFQSmB4t4pJEBHHvoiVu1L_pqaCyeZoPmgQLni8dFs9vthvaXWmHNTl6SUnWI5TQJ_ypdY8O3iNdXlzSA85_A52bD3IzhdmTCMlxBUbOuJyskFyj47xY0QC7VAir2RPX8lovIpdYwEEmG6R--eWkbY_XbgKVysrn-4_fz27xNtzUUVDcSeCzs9lfh4039E_5mV92Kmw2j-gZ9ldqCPnHTs7oMTFYKsMM1aOzlkKDqm4nMDkGdCcig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهند که نیروهای یمنی به انبارهای نفت و گاز در ایستگاه مرکزی تولید برق عسیر در شهر ابها حمله کرده‌اند. این تأسیسات، منطقه جنوبی را به انرژی مورد نیاز تأمین می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/146197" target="_blank">📅 10:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146196">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIuW47-KWW4ywRUQjHI8hG_4XmY6If6YMWTdT2PkFiv1MilTnk0Q6zGaN1GLrn3FcozMZMZwbhWYrglLB5Q0X2_nKQILkQbjD_5VsI_10W2XE0SPg_hWsG_Hj4poHXsXOrWxeGmwdKlVLIUg6TGyf63kHK7FU7gPh6pDK8mDN1vDFA5dJO4v5aFul2zg5gQyej58kdtjMXeCaCAbxCJNGlqR53N1jBu8M576p98t48MnqLGdDRgx9tGZ7KgWwRC1eDqZpYYEC94zf10WOVtGjf0P9YL5PyL_qn55BuHzUOrYQ2vkjr2HOKZ2J8cq9ps3Ykcdqi17OzASWXWX_qCR7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مهران رجبی:
گرونیا مهم‌ نیست! مهم‌حفظ نظام عزیزمونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/146196" target="_blank">📅 10:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146195">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WHNSZZXcYdeEuN_opjyEE7IAZSXyLyEO_6TccGsQfhXpShDn4mUsDm8InHhY8UjcDuixXi5XncNxYOEwuqmGAGj6Ru7SrfldGuZDssAd_enak19376etQSDfnYsPXKGE0rB1mcUxLpLwRyRGRqlenMDzazOp8YiIR0IPtOGvzoWTn27Xh4crpSrI71-UURbFdvfV9PWIeov8k5LOxOftAvVRN_yI7oNLsPGX-Nz_wgXk1UykCmauQBeJg_skXC6GLHuiQ6J5NQF_B0tAWlTwiu3mNNtZHerp-bpCRAWRJFOj6UswEujHIe4p8iPLp-T1Qu2o95nlrzw-Zk_5WsaoVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دسترسی کاربران به برنامه پیام‌رسان تلگرام در کشورهایی متعدد شامل سنگاپور، آمریکا و هند با اختلال روبرو شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/146195" target="_blank">📅 10:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146194">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
نیکزاد نایب‌رئیس تحریکی مجلس: به‌خاطر حجاب در سفرها دچار تردید می‌شوم که واقعا اینجا ایران است یا خیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/alonews/146194" target="_blank">📅 10:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146193">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
کارت زرد مجلس به وزیر ارتباطات
🔴
در جلسۀ امروز صحن علنی، سوال علی جعفری‌آذر از وزیر ارتباطات و فناوری اطلاعات با موضوع پوشش‌دهی ضعیف تلفن در جاده‌ها و روستاها، بسته‌های اینترنتی بی‌کیفیت، بلاتکلیفی بازنشستگان مخابرات، رهاشدگی فضای مجازی و بحران تلفن ثابت مطرح شد که نمایندگان از پاسخ ستار هاشمی قانع نشدند و به او کارت زرد دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/alonews/146193" target="_blank">📅 10:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146192">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bc77723ed.mp4?token=Ro2ncjnNuAvOtSIBpcfdl3XgC3KFLXTLQ65cDye5M5GyVOqf5hf3Z4vm1SpQg5rJRlpfMm6lYcjzEWF50eZ_VMIQYZX3ukjYYmcz37slPIR-vIMV8Y1l83YTzavh0x6WF_43vRA_rQ4M3kUnuqWbGinlQBwI9AMBmkYGK1BztLi-l7rzYwobM6yFz2Dcko2V2tjDdMRpD8LNKScGc4e5a62N1xFSarqBFxsZI-KXcLkfdCHMX2hbFE_TM--FCJ2AfEDQrVV_9weRwU0cugha2KiAUfsSKhF7X8jRnsCPR-y2qtwX00t_19sE71wHcaF3W_Hi5Nuaja9PgxcGmn0W0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bc77723ed.mp4?token=Ro2ncjnNuAvOtSIBpcfdl3XgC3KFLXTLQ65cDye5M5GyVOqf5hf3Z4vm1SpQg5rJRlpfMm6lYcjzEWF50eZ_VMIQYZX3ukjYYmcz37slPIR-vIMV8Y1l83YTzavh0x6WF_43vRA_rQ4M3kUnuqWbGinlQBwI9AMBmkYGK1BztLi-l7rzYwobM6yFz2Dcko2V2tjDdMRpD8LNKScGc4e5a62N1xFSarqBFxsZI-KXcLkfdCHMX2hbFE_TM--FCJ2AfEDQrVV_9weRwU0cugha2KiAUfsSKhF7X8jRnsCPR-y2qtwX00t_19sE71wHcaF3W_Hi5Nuaja9PgxcGmn0W0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شاکر بوری بلاگر آبادانی به دلیل شکایت موسی غظنفرنژاد به ۱۴ماه زندان محکوم شد
🔴
شاکر میگه اونی که اختلاس دبش رو کر ه ۱سال رفته زندان اما من که قضیه رو گفتم ۱۴ماه؟ همچنین گفته دوتا باجناق لواط کردن آزادن اما من که گفتمش باید برم زندان؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/alonews/146192" target="_blank">📅 10:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146191">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27ea4f701f.mp4?token=l-TFw1Ul4VXOapFF327eYi8J-jkhLWnaNMVT9PzPO7ATQnWml7q5XbIvGsIudGWgbEsIiE1ujomKJuT7topbGL8tSaAExfYsE8ynef0cZc0BhPvtyO30FIxkpF5Yf-EmnRTcwlyKmsSl0YPLG6k98gNRMGumbSPLVWBhy7HFLenO6YLzvJRbtt6cF1DYww-7Vu-h2-B9x3Q4p0a5FHQTDprzpnOlTL7jvgMYpuTrycfY-lkosicO5to6niUFTn9CE2-9MFA9y38cZZ--ezaO40Y_nnf1D6X3WJcYctmZrBzPugE97Az0yYwHXlZeKcVOI4YFwVXP_yn8QnTJ4x-I3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27ea4f701f.mp4?token=l-TFw1Ul4VXOapFF327eYi8J-jkhLWnaNMVT9PzPO7ATQnWml7q5XbIvGsIudGWgbEsIiE1ujomKJuT7topbGL8tSaAExfYsE8ynef0cZc0BhPvtyO30FIxkpF5Yf-EmnRTcwlyKmsSl0YPLG6k98gNRMGumbSPLVWBhy7HFLenO6YLzvJRbtt6cF1DYww-7Vu-h2-B9x3Q4p0a5FHQTDprzpnOlTL7jvgMYpuTrycfY-lkosicO5to6niUFTn9CE2-9MFA9y38cZZ--ezaO40Y_nnf1D6X3WJcYctmZrBzPugE97Az0yYwHXlZeKcVOI4YFwVXP_yn8QnTJ4x-I3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چند روز پیش تو سمنان چندتا دانشجوری عراقی حشدالشعبی به یه دختر ایرانی تعرض کردن و جوانان سمنان هم اونارو گرفتن کتک زدن
🔴
حالا رئیس دانشگاه بیغیرت رفته از این عراقیا عذرخواهی کرده! و کم مونده دختر خودشو هم به اون حرومیا پیشنهاد بده
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/alonews/146191" target="_blank">📅 10:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146190">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_eHcDxawDxRtXCp5cNGCZB55V2L4PDwI7tIuFljyM1TBHQMpfMmMT3kjbWGzd8gLZJGUfRoYa0t1antI_2TYQEIMQkFOKbELs4uTS9yQcasc5N-GbirqGX3yCFnYOc6o_EwN9-tYrdlp5e21qNb0JKJ2qZ05CE5Ch9gF7FBN8bF6ZQJBwQCfesC7fcZph9XVvx2ZVxgoH0UJ4A4cM5idX7SeU_N5Gff0AUPGfG-EeYbvXIq3Z5tHJSGikrl9z0b33I0v-Z4qdjD28m0sumYezZmMhD83uPvaXunkr4B5JQq20YUvZ1lFz63ww5XUIRgaHQRkZLATc_l_lg5lRzOjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهند که آتش‌سوزی در کارخانه محصولات نفتی شرکت آرامکو در شهر ابها، عربستان سعودی، رخ داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/alonews/146190" target="_blank">📅 10:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146189">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAaqzVfFOQFvh0MHMIoRgzY_cg4Cv41Pq0XJst06iydI-7JkuDM_2TnJsGF-GV4ASMUwje4goJRJTHMPnLPNKE1iYVnH673o0Cg_QkhwMvbE_lIsWcTwlw_hdJqm5hSICsHxKsXEWfWQ9CZhUd86OB3Yj9eHQXFA9qjLE2cIYFyc7GIF_CTAJXLfwYYQmPvmDHE3r-OEd7IL45CvC9PkqduHJN2BjzHX3NDLYMGTN3x1gPal-stuAvts1Fu-Knf9dNhDvo_jRaJJmj7iUCtiZYrq8U9UjgPjPy8RK8VjdywTOt_dv5dU1x99JBUrgTFKumy1ty0Vx-nqZIANsHp7Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آتش‌سوزی در پالایشگاه جیزان، عربستان سعودی.
🔴
تصاویر ماهواره‌ای نشان می‌دهند که آتش در پالایشگاه جیزان در حال سوختن است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/alonews/146189" target="_blank">📅 10:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146188">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dde6ff7c1c.mp4?token=PI64q_fIuDuQTNoYBT_hEgkWltGEx0Q_GOp-6TWAGr69X_upS6t62-N76HcytuTB95pF5opJwn2in_FvB3t764N5-5VbLMj4a3geOLMOt14BEX-0hiT6o6ZULvOCRxB-XzA04H6-tfxDXQN1DI-s3dvFk0-vxOTw8j8eQn5LjIfH3roynscgWdugHIRMPIjTiWliRycCSaxCLfdkXFJKkAVVJcYIUnAJZRH67f5ulHlnx5tfr-fEWXRxYE7GqgOcblVhzZ-Q4ts3V-ul4OakVVnlSVDfuZBOS4sHRsQPPn6EXlNDHEvAcLixH9KMo_s4Ty4iqJ4vQM-Y2EMTBcaYSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dde6ff7c1c.mp4?token=PI64q_fIuDuQTNoYBT_hEgkWltGEx0Q_GOp-6TWAGr69X_upS6t62-N76HcytuTB95pF5opJwn2in_FvB3t764N5-5VbLMj4a3geOLMOt14BEX-0hiT6o6ZULvOCRxB-XzA04H6-tfxDXQN1DI-s3dvFk0-vxOTw8j8eQn5LjIfH3roynscgWdugHIRMPIjTiWliRycCSaxCLfdkXFJKkAVVJcYIUnAJZRH67f5ulHlnx5tfr-fEWXRxYE7GqgOcblVhzZ-Q4ts3V-ul4OakVVnlSVDfuZBOS4sHRsQPPn6EXlNDHEvAcLixH9KMo_s4Ty4iqJ4vQM-Y2EMTBcaYSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چهارمین فرونشست در ده روز گذشته در خیابان رباط اصفهان!
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/146188" target="_blank">📅 10:08 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146187">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsgZ7uQf2xRl3wdFhpXgow4dgC-6zp68i4_rKuN9AU9WgasxsClu48DF3ZdTHAQqVpz4tx5XTh4MZjHBHNXh-Rzj7Mzww_LGT-2LigcD44TyAME7bwn1e5PUnAc_xnOTBy_hbpkRYnIIwkHRHEYWxMJn4mlLOM4hOCMwTyAbScfr2C6AcR6lqUcn8RjtkR-hmLC-vIbNTVUYp1mTV9qRfp7tP4EFbtX5lH8je1o-mUGPAUWA5-hvNiYU9iQld4MyPUrXabI9gTP3JT5nzGRl7BeG_5VX5OLJgDZi_ZC5PuWSKRFj3GzFFDWh42y4OTxCCZLP69qHG1LblJkd3ts_1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل (IDF) طی ۲۴ ساعت گذشته ۵۰ حمله در سراسر جنوب لبنان انجام داده است.
🔴
مناطق هدف قرارگرفته:
🔴
کفررمان
🔴
نبطیه الفوقا
🔴
عرب‌سلیم
🔴
دیرالزهرانی
🔴
زوطر الشرقیه
🔴
قنطارہ
🔴
بنی حیّان
🔴
نبطیه
🔴
ریحان
🔴
المنصوری
🔴
تولین
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/alonews/146187" target="_blank">📅 10:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146186">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTfinooXkTJPK4BUFb6FkyS3UQm8812SpsdX3_O8_bt_LOABkcxTSbIYvMs5owxd6_NJSkofzwQAJFeVs3jQzQnoOxyI6a-FyRVqMBa9rfU8ZRPPrMSUzjNoRBsvMTDohW6hL7uWKot2uYBX_qf22oNSV5Vg6pnP7e1dMXgm9tjosrzKcYAd7f9Lj1CvJ5CnDOpprIv0rhCOynhJVnzlWi64GbOo0ul0pDh_cMfLpr_yphT5Vp7gT4n2as5qOCb135HdYTLhWJT9ebuXixhhiC053Y-q3Bc5TlJbzC8DlC3Lsjx58hdStIBRWcCNd1k1HXtEtLwnFtGBdtxJLMdLrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی تحلیلگر نزدیک حکومت :از دست رفتن جبهه یمن، موضع ایران را در قبال امارات و عربستان تضعیف خواهد کرد و نباید اشتباه جبهه لبنان درباره حزب‌الله را تکرار کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/146186" target="_blank">📅 09:58 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146185">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGeQfyZ89mGWevg-9Fx6XyC4fZABfSjvp2R26vqo2ahv_ytXZeqyTEhiFT1CNBE1w3SHxdL22VPebB_b5D7SYjP29JTWFPGlHGnounJFAYeNizthP923T9zHxmBglVLsh0gNFgxac8XJKSmV9I-1VQyYVbQ49eY3dKDhc7_G6kW41RWHMO8teRo58SrF1KuVtMHOI6AS4_dD1E6c9Vms0e47p8kdxYIzsdEynHs3x58CyQPwBCxK1mghYNb7R50qNYnSjxahGMIkshyqBY9iGTJVGWmHQpGlG_7gyO4yJllzGFAmSzIe6V2yYBka8EL83wund4KwZuBpYNn7aM5dzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش ابطحی به نگاه غیرحرفه ای صدا و سیما به اظهارات اخیر حسن روحانی
🔴
صداوسیما حتی یک خط آن را پخش نمی کند.
🔴
اما دریک رفتار غیراخلاقی وزشت و غیر منصفانه کارشناس های جناحی و افراطی را ردیف می کند، تا علیه بیانیه خوانده نشده در صدا وسیما، در صدا وسیما فحاشی ونقادی و توهین نمایند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/146185" target="_blank">📅 09:46 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146184">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
نفت ۰.۳۵ درصد افزایش یافت و به ۹۷.۳۴ دلار در هر بشکه رسید
🔴
قیمت نفت به روند صعودی خود ادامه داده است. معاملات آتی نفت برنت تا ساعت ۰۰:۰۰ به وقت گرینویچ، ۳۴ سنت، معادل ۰.۳۵ درصد، افزایش یافت و به ۹۷.۳۴ دلار در هر بشکه رسید‌.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/146184" target="_blank">📅 09:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146183">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IouVngmucy_d6r9KrftbiDWLxuuDpbtPAUFhuGwZAfr3Hx6Uum3YMDFOu8kFQYk4dhQbA17lpgSkHVrI5OkGf_8fu4uDhmLwUYmMMo6n12N-QzJy3nDC6ZSGmEP7kCC9tAufRiC5X7lLl_wYURjU-9rkNq0Ojo9OVgUhzFMw1mBu6-wsJgXb2Z3oo5-HCeuTycOCc0fvMVpxJIyjKzcppDrBb5qWgSn64f7rgblsWW7VJvpsz8qfs046XCS__vFkr4dp22HF3WIWtHSRM3RKWDEWJjXnFc0xjo82baWi2KTvfzPpAHiK_4uuXQaAr9nmjdR98n0Big7SOYlkp5uSWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش روزنامه هاآرتز، رئیس جمهور امارات متحده عربی، محمد بن زاید، حدود ۱۰ روز قبل از ۷ اکتبر ۲۰۲۳، به نخست وزیر اسرائیل، بنیامین نتانیاهو، هشدار داد که رهبر حماس، یاحی سینوار، در حال آماده‌سازی یک عملیات بزرگ علیه اسرائیل است.
🔴
در طول یک گفتگوی ۴۵ دقیقه‌ای، نتانیاهو پاسخ داد که حماس بر روی کرانه باختری متمرکز است و به بن زاید اطمینان داد که اسرائیل برای هر سناریویی آماده است.
🔴
بن زاید بعداً هشداری مشابه را به ویلیام برنز، مدیر سازمان سیا، نیز منتقل کرد و گفت: "به نظر می‌رسد اتفاقی در حال وقوع است."
🔴
نتانیاهو، به رؤسای سازمان‌های امنیتی شین بت، موساد و ارتش اسرائیل، درباره این هشدار از سوی امارات، گزارشی ارائه نداد. برخی از مقامات ارشد امنیتی گفتند که این اطلاعات می‌توانست بر ارزیابی آن‌ها از نیات حماس تأثیر بگذارد.
🔴
این هشدار، پس از هشدارهای قبلی در ماه سپتامبر صورت گرفت، زمانی که واسطه‌ها پیام‌هایی از سینوار را منتقل کردند که به یک "زلزله" قریب الوقوع اشاره داشت.
🔴
دفتر نتانیاهو این ادعا را که نخست وزیر، هشداری از سوی بن زاید، رئیس جمهور امارات، دریافت کرده است، رد کرده و آن را یک "دروغ آشکار" خوانده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/146183" target="_blank">📅 09:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146182">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smwJFg0q1JC1yNn0Gfssvgt5jDy7vLJQ7ku1XH6lpd1uv9qpc9PaEayxj25_vLq9uVMshyvw0qFFVrSHWLwYs_tafyG_L6EDiX0Nq_P9C9kGMpnXLLisZ1avOCMBhCw3n-S8qph8Z9RxC5aBaw-VO9YpLgAhz4xO5oNMSa-M2RZVq0Yy15pfzVshKKyHIcITlmKPLF8ZsLhN_TeLoflfJtAHL7rwHUg6yL4gmTytlmtW5x2C3Ct2lihsIftKVpoS7MkP35TyiKcAA-hDILDBlq8jTsmtrzwYsKcFieYt5POlqjtUQWr0B57Vt-j6W7CmSPaV8xdbbeaDQCUdtBmD4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال، محسن رضایی:
در روزهای اخیر، واشنگتن هشداری آشکار از سوی موشک‌های جدید ایران دریافت کرده است.
🔴
جنگ اقتصادی با ایجاد یک منطقه ممنوعه دریایی در سراسر خلیج فارس تا محدوده محاصره، پاسخ داده خواهد شد.
🔴
وضعیت عملیاتی در قبال ناوها و پایگاه‌های آمریکایی به طور اساسی بازنگری شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/alonews/146182" target="_blank">📅 09:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146181">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
داده‌های کشتیرانی گردآوری‌شده توسط شرکت کپلر و منتشرشده به نقل از رویترز نشان می‌دهد روز دوشنبه هفت کشتی حامل کالا از تنگه هرمز عبور کرده‌اند؛ این رقم در روز قبل هشت کشتی بود.
🔴
این آمار جدید نشان‌دهنده ادامه کاهش شدید تردد دریایی از این آبراه حیاتی در شرایط تداوم تنش‌های منطقه‌ای است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/146181" target="_blank">📅 09:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146180">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
وزارت انرژی عربستان سعودی اعلام کرد که چندین تاسیسات و زیرساخت مرتبط با بخش انرژی در منطقه جنوبی این کشور، مورد هدف حملات حوثی‌ها (انصارالله) قرار گرفته است.
🔴
این حملات باعث ایجاد آتش‌سوزی و به طور موقت، اختلال در برخی از فعالیت‌ها شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/146180" target="_blank">📅 09:08 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146179">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70365c549f.mp4?token=p27x9HZC202y6FgV61oUrXLHUqHOWVKgSt_o8OJF-yWGIpNE_qbaDj8uv77Rd49wWJ_IR6Jy2R9JwQxmYzmls8EQDi_rWUv1dxsXn4nqA3axxKg5gqldif3nQ3TPEuHuDNa00X8ugnY4Wia6fWy1B5gPmSNs9Fy1JyUZhy-L_EEHclQW5GuRzPDXChzywaf7NwU9590pPt4OLm7Na3heihv2FeCxeOZnoECl8lNd7vK1h95ii1Z61BC9zuya_jjXXPUnOYFjomsE5C2ZZojN51b25y9Se_PDm6J3-Z914sjFfZjJuulZNO0ofYXthH8seCtd1-MsUgz48fHUqys7YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70365c549f.mp4?token=p27x9HZC202y6FgV61oUrXLHUqHOWVKgSt_o8OJF-yWGIpNE_qbaDj8uv77Rd49wWJ_IR6Jy2R9JwQxmYzmls8EQDi_rWUv1dxsXn4nqA3axxKg5gqldif3nQ3TPEuHuDNa00X8ugnY4Wia6fWy1B5gPmSNs9Fy1JyUZhy-L_EEHclQW5GuRzPDXChzywaf7NwU9590pPt4OLm7Na3heihv2FeCxeOZnoECl8lNd7vK1h95ii1Z61BC9zuya_jjXXPUnOYFjomsE5C2ZZojN51b25y9Se_PDm6J3-Z914sjFfZjJuulZNO0ofYXthH8seCtd1-MsUgz48fHUqys7YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آب‌گرفتگی منازل در پی بارش و طوفان شدید در مازندران
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/146179" target="_blank">📅 08:57 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146178">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8osYrdaY6hCLhkhMJXF3EYyzmpi7YBZ2gzoT6NZt1a5td8qKy9P5cYj0TwmfN-kVofZVcAevoU1yBI4lbmcnC9qNV2OCTI7uMXPHR4Bga9MZaTNf3AlhPl3J8Uh569HKAEOszoGnHDc0bh_g7ePL73JK-07UnhndHzjBhb6vzZ0wYYLMR-gqNK3ejXUNUoG6xr9PnoPGXMTtKie7rymujiiNRbV1jGMjmna2Fpi5qfTyQYcVhsr3DcXOOjR2y4PyydBMjzC_e-Ekd11uasZUd6FKM2_LjF-4lb0Vdz_WaWf1Wzd74QeJUkm8x9_y3Tg9fxMFXYdl12oJyOYz7Qqrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایتامار بن گویر، وزیر امنیت ملی اسرائیل، از دولت اسرائیل خواست تا تحریم‌هایی را علیه بریتانیا به دلیل "اشغال" جزایر فالکلند آرژانتین اعمال کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/alonews/146178" target="_blank">📅 08:52 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146177">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d0ce49abf.mp4?token=TjD1xnum1E2mmQq_0Fw1rm_gDDXCGF4CtUWa5IU7a5N0iMiY8nUhhbVsx-vF8bmWHb96XiVcGIZXhgV8VGXj4YniH6TypInbPpTZrKB41aQx8X2H2OXJMD5SU_3hCNkS7jO3GZcSrQzd_lDpng89z70fUzWa2nCbGylMyFJ12cNctZMBvPGo-wCva4T8_n-dhpwEopDBoB8368m10Vx72zcIrUSOaDbsDmpBV5tvhANh2My5bzJdIpkwldbbEqlMZz_4zzc5ZRrOH_0D-XAqnUe5-A6j1LfEodBx5VoYfXI2IN_nr5rX22jOcr2mZvFy_9jgPRrJgRqzxWuQGRfoPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d0ce49abf.mp4?token=TjD1xnum1E2mmQq_0Fw1rm_gDDXCGF4CtUWa5IU7a5N0iMiY8nUhhbVsx-vF8bmWHb96XiVcGIZXhgV8VGXj4YniH6TypInbPpTZrKB41aQx8X2H2OXJMD5SU_3hCNkS7jO3GZcSrQzd_lDpng89z70fUzWa2nCbGylMyFJ12cNctZMBvPGo-wCva4T8_n-dhpwEopDBoB8368m10Vx72zcIrUSOaDbsDmpBV5tvhANh2My5bzJdIpkwldbbEqlMZz_4zzc5ZRrOH_0D-XAqnUe5-A6j1LfEodBx5VoYfXI2IN_nr5rX22jOcr2mZvFy_9jgPRrJgRqzxWuQGRfoPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این زن ایرانی اسمش فاطمه حقیقت پژوه هست، سال 1381 تو خونش خواب بود یهو صدای جیغ میشنوه و از خواب بیدار میشه، میبینه صدای جیغ از تو خونه ی خودشه، میگرده میبینه صدای جیغ از تو اتاق دختر 14 سالش میاد، درو باز میکنه میبینه شوهرش لخت تو اتاق دخترشه و داره به دخترش تجاوز میکنه، از شدت عصبانیت و در دفاع از دخترش شوهرشو میکشه، تیکه تیکش میکنه و میندازش تو رودخونه اطراف تهران، پلیس میگیرش تو دادگاه ثابت میکنه داشت از دختر و ناموسش دفاع میکرد و به 7 سال زندان محکوم شد اما دیوان عالی حکمشو تغییر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/alonews/146177" target="_blank">📅 08:46 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146176">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه آمریکا به الجزیره گفت: ما در حال هماهنگی با شرکای خود هستیم تا اطمینان حاصل کنیم که مانع‌تراشی ایران در ناوبری قابل قبول نخواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/146176" target="_blank">📅 08:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146175">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c6mxpPz1Krf9TIFiC4Se8PlSHYXX_BWCaN2TTliqKna2gMx80agXs9UwPnF4K5l9QJfXN-GwXtriUP119MS_Gd5psokv5M5e8F_QLadC8GdYpKF_2dflopYoTdtO9CuemlU5nzxR-zu2LE_xzYeUCY11rL5fKIHSnT8E0McrRCEl3_fT2j0EzcoNDOpQ67KAiAonerEh0q933wUGcAhBIg5FRXBkXl1FvKOppuW12Kl7orypZLI-f1FINxLUhpEOg0H8IGzjH8XSuhE19aDMMZ0Q4XCnuF7pohH8c3chnHgTJS19sf1R09gnQquivYCzfEHeoBwdARRdXhbgCOTrow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پهپادهای اوکراینی بامداد امروز پالایشگاه نفت ساراتوف در جنوب‌غرب روسیه را هدف قرار دادند و موجب وقوع آتش‌سوزی در این مجتمع شدند.
🔴
پالایشگاه ساراتوف از مراکز مهم پالایشی منطقه بوده و در ماه‌های اخیر نیز هدف حملات پهپادی اوکراین قرار گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/alonews/146175" target="_blank">📅 08:37 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146174">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
ترامپ اعلام کرد که شرکت هواپیماسازی کانادایی «بومباردیه» دیگر اجازه فروش محصولات خود در ایالات متحده را نخواهد داشت، مگر اینکه خطوط تولید خود را به داخل این کشور منتقل کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/alonews/146174" target="_blank">📅 08:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146173">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjuKWL-fsiOe__cjz-wFGCHWLOCQgfTtRtN2ubBm3kXkMqEsqA7e9VeIrPIHYvBYUBHCnFY65D4ztGKE4jYZ_J5YmUBwQCHmPdP6NzJ1LTiLja1Gyca4skwUT4XuBitY9KsUnlZIPoxjNWBko8URxjRxqlt6wv1LJImv0tEoF2jjlZuoX5iQY-N5GHFrj68idotn2OIBXEap-5WZ7xapFRuuMbmSbaM8cqi8S8RdPilParcynExnv_XZo5UVZZ7JTeUW34bJ4gBktvHU3XTZNN-AeG3quidKRbqglDrkALepP2de3JTRbjS8xjDVEJnYXs4Cklj811oICvofSKMOAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانادا رسماً تعرفه‌های تلافی‌جویانه‌ای تا سقف 50 درصد را برای صدها محصول آمریکایی اعلام کرد، در پاسخ به تعرفه‌هایی که رئیس جمهور ترامپ اعمال کرده است.
🔴
این اقدامات شامل حدود 20 میلیارد دلار کالا از آمریکا می‌شود، از جمله فولاد، آلومینیوم، پنیر، لوازم خانگی، پوشاک، لوازم آرایشی، موتورسیکلت و تجهیزات کشاورزی.
🔴
نرخ تعرفه‌ها از 15 درصد تا 50 درصد متغیر است، و بالاترین نرخ برای فولاد آمریکا اعمال می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/146173" target="_blank">📅 08:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146172">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTi_rHQR5Gcw01KnYaTIXzZUjSvuKombOSQXHq4h-OEvjG1xzr7U2UsQqWLjRbwJls8aHQMbzCd1fH79bpGDFS7Fn32gSzuwjpxmqDp0byXInjIx5XF2Avwf8A5Wvrt0s-DTCrFRCbv9n7oNl_fiqw0ZxWCtjjz7NfcNVjjQaCEw61AH6ok5QQmGBaKtbm2dYpgcFha5ndNouAkZahlie5e-KPK-qdRY7AjByUt-l4vqabPPZoAONP-zbqXcLTLRUXQPWqn8T73rYXy09Lp0PG0FGZrqkBj3yKE5z3gvBI_aGjHtaXtM9-E0xd-npo0im3uXiLWXwEDulzF-sTHbEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : قیمت نفت به شدت کاهش خواهد یافت، درست مانند کاهش قیمت همه چیزهای دیگر (اما بیشتر!). زمانی که ما در جنگ با ایران پیروز شویم، این اتفاق خواهد افتاد.
🔴
قیمت هر گالن به سه دلار خواهد رسید، اما در نهایت، از دو دلار به ازای هر گالن کمتر خواهد شد.
🔴
این اتفاقات به سرعت رخ خواهند داد و ایران هرگز سلاح هسته‌ای نخواهد داشت. ما دوباره آمریکا را بزرگ خواهیم کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/146172" target="_blank">📅 08:08 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146171">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
چندین اسکادران جنگنده اسرائیلی به همراه سوخت‌رسان‌های آمریکایی در حال پرواز به سمت یمن هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/alonews/146171" target="_blank">📅 02:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146170">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
ارتش عربستان: عملیات نظامی در یمن هم‌اکنون ادامه دارد و در ساعات آینده نیز به قوت خود باقی خواهد ماند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/alonews/146170" target="_blank">📅 02:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146169">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51336edb7a.mp4?token=QU4X0lL_PoMKr0F-ebBDNh2XiAmwdTCgFNhzTMSS_jOBjuvHXEb2tBKd_l_KY8lWUzEL3PbhIIWFQxxqdEQJfY-HiRZW0oAdZ9mcXeurwoenDrhh7S8dzb0dghxUoL0zkJGakvoKc3RDKQUzCni2tFJmGpJZ6OpV0wcR3X8O4qXMeDVDSNX_Ian4DMsXaUvyGJ7xsTL9P_s0Ypef_Ug8j3W1hXBH52ozokyyvMRbwFFLUnT4pNaXVVzlkO4iLun-viEjGkfEFrkW2jB7l-Kg0wlVplad0M5XLfJ6UCxhvNF_ln3ThGhMLCr4P0Hxyi01Go4a9NAjUptQ-IdG23toBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51336edb7a.mp4?token=QU4X0lL_PoMKr0F-ebBDNh2XiAmwdTCgFNhzTMSS_jOBjuvHXEb2tBKd_l_KY8lWUzEL3PbhIIWFQxxqdEQJfY-HiRZW0oAdZ9mcXeurwoenDrhh7S8dzb0dghxUoL0zkJGakvoKc3RDKQUzCni2tFJmGpJZ6OpV0wcR3X8O4qXMeDVDSNX_Ian4DMsXaUvyGJ7xsTL9P_s0Ypef_Ug8j3W1hXBH52ozokyyvMRbwFFLUnT4pNaXVVzlkO4iLun-viEjGkfEFrkW2jB7l-Kg0wlVplad0M5XLfJ6UCxhvNF_ln3ThGhMLCr4P0Hxyi01Go4a9NAjUptQ-IdG23toBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
موشک‌هایی از یمن به طور مداوم در حال شلیک شدن به سمت عربستان سعودی هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/146169" target="_blank">📅 01:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146168">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
عربستان، یمن رو بدجور بمبارون میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/146168" target="_blank">📅 01:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146167">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b9JweW-7fsBdA-YCr0kjGohub7oGBj0-WKM8tEa6cCfDCdyEfhCyoEEoBDczupgH74JoJy5A4SpmplHiGp9LiEygLcPEpEFMj666UrEHICicDkvm6YRgdj0J76-a0nexRnh56ExdxQnf0sbO4PngY0B4MViN5DakD3wOtN6uTO9CKm6lKJPD3kiCvh902EPamsQ6gxHWCE3RSUGpn6oafBLBR-SXkRB80-8JXLJcwuDd3U267t4pGhMMAIXnNzyz520rjuomDYKcAlmgPj9epcOebKFSfzgeQoVCCaWGPMkbZLtfJ01Bc8PH3nRve5GX3BSzHNUS9ftLDxBVCeqHcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این وسط فیلم....... بازیگر تگزاس در اومده
😐
📥
مشاهده فیلم</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/alonews/146167" target="_blank">📅 01:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146166">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LsCgADqKydrtw9NDvm5udN-gKM4Nw-2GylGutKKkuizvo7uvwKSjFC6VNuQgEWpv2KBCPG27kN5R0eKR6MotcP0G4WIvQb9mxJMDRmGDQZYGP-Fho7ylAwVXWEX1en0dpSCKaCoTLbT9Vp69wvcE4hHEYLgrhBLrjpS_2NRj7Hwt8Ab2F1tF8tgj3QGqkPSA8qmyQXnngvbfxc7DjXirbz7ptZm55EkyJgd9i35iReT2Oy13I16fkSyl60xoaZAshy7ty9-WURzcgzVsZntYgXxfUDrtm6P-CMp2DCDdDR6-Wgikc3vmn0Cmo6ubEM2rj7eA01fo0QjPZjZPgQiogw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طی اتفاقی عجیب بابک زنجانی بخش قابل توجهی از املاکش(مال مردم) رو به نام خواهرش نوبهار زد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/146166" target="_blank">📅 01:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146165">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a515fc01ca.mp4?token=FzlW7ERisQG1nPScmjV6wNxIXBvKSUAzqpxHyIZz6vVtzEOgM3LN7uWb7SYw-jNzm4O2QZlZrH90FgAmlHj1reF9Vyjxr63vOHfw-XfTK1H35T2rZfkuDTJnLUxX4iQ76sUd0Hmud1FJyjLoVVpqRXdBpc0gFWPMUQwbCZxUOO8ZnMktzTe2IMOGwPnC5_dtw0YM4eRpaxiiJSSk04UrztzuhU_aE9C_sTSvPM8_IGNmcOPkGJ9tUJIrb67W9ynv0urGFWm1Fwlr2oVzWrjZufde-AM61iKFA3-k1HYT7SGfPGr6sXQhnyQkqTUdjHKYONjtFzZTLLpFo_DJcdHduw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a515fc01ca.mp4?token=FzlW7ERisQG1nPScmjV6wNxIXBvKSUAzqpxHyIZz6vVtzEOgM3LN7uWb7SYw-jNzm4O2QZlZrH90FgAmlHj1reF9Vyjxr63vOHfw-XfTK1H35T2rZfkuDTJnLUxX4iQ76sUd0Hmud1FJyjLoVVpqRXdBpc0gFWPMUQwbCZxUOO8ZnMktzTe2IMOGwPnC5_dtw0YM4eRpaxiiJSSk04UrztzuhU_aE9C_sTSvPM8_IGNmcOPkGJ9tUJIrb67W9ynv0urGFWm1Fwlr2oVzWrjZufde-AM61iKFA3-k1HYT7SGfPGr6sXQhnyQkqTUdjHKYONjtFzZTLLpFo_DJcdHduw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انقدر ارزش پولمون تخمیه که تعداد صفرهای قیمت بنزین جا نمیشد و اومدن کنار نمایشگر‌های جایگاه بصورت دستی یه 0 اضافه کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/alonews/146165" target="_blank">📅 01:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146164">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
هم اکنون حملات هوایی شدید عربستان سعودی به مواضع حوثی ها در جنوب یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/alonews/146164" target="_blank">📅 00:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146161">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WUZvprctvwtXX5p9U0cNMqDvCoUHl6U9gIVIMyi1GxcfoWa2MFiL2MmRU598j2UwjarE-LXumVh-0EON_TDyjL-KOBAZfIymroqkCQz24HkDOb5Uvbn7nyJ-yYrJu8UkPgYFpI_RhFRfn8NQW3FoAWfu8xdW-1J5UhqR1gyqRqsAXINYn01ZCsd4NneBjaQ_W0rAwZQ9H27KeVYVK3kCBJN52w7TKwgtKRS1BKl9IJMvCIxTOP8F5EiwyLaCYWrohojv3-UnXel2aKY6htJ0najnvuTHImhIwpl9GzVdsIgacjUJmt82TcaACT4GnnipViKO4hdD8iSZZzZBaUBXRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8833895957.mp4?token=D1Huk5YBcn7GOw_pwOld591pDZwr8Bi9LRuiRWfVAVQBbqr6vLapunPVLyP4XwuQ4UAKTWJoMy8yNPbPeB-VF0iR9OIOMLoMfNbltWHMw6TBgSh9JcquS4eRiQmhvHBAitOb_78nzq7y4XccY66iag9YN_4Oxcul2am5tMGBcrI3CFf12VicIO4SdUvXFUM1ywkpN_gLm-E6jjHS5SNIPvjfy5siYWaYP5JDlJT_0lM7kK9elAlvXIXTzpzSwWCyrjRsyQ3PIwaqWFR-RC0zJJ5z7uOMZvy2Xxa6Qludo74d6dnFuVbHe_XFjvUSsC_aNSAjGkOWMTYBs2BarTb0NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8833895957.mp4?token=D1Huk5YBcn7GOw_pwOld591pDZwr8Bi9LRuiRWfVAVQBbqr6vLapunPVLyP4XwuQ4UAKTWJoMy8yNPbPeB-VF0iR9OIOMLoMfNbltWHMw6TBgSh9JcquS4eRiQmhvHBAitOb_78nzq7y4XccY66iag9YN_4Oxcul2am5tMGBcrI3CFf12VicIO4SdUvXFUM1ywkpN_gLm-E6jjHS5SNIPvjfy5siYWaYP5JDlJT_0lM7kK9elAlvXIXTzpzSwWCyrjRsyQ3PIwaqWFR-RC0zJJ5z7uOMZvy2Xxa6Qludo74d6dnFuVbHe_XFjvUSsC_aNSAjGkOWMTYBs2BarTb0NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این وسط تو رشت سیل اومده
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/alonews/146161" target="_blank">📅 00:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146160">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKBEnKrUM0ondKnuWW2yzEF_weN3Ve3WYMEz6J5jDlI-WM77B06dcq7sAvSs6y6bZR421nk2B-DoOF4nXtbSa-yqVGYxI06t16gKikQk04BkhSF1Y117sN0yZFuvz3Ch1gQwq7GpficNtM3oFn4x-9kKFOhfTVhpbUci0XTm5sQyNaAHBr8MvfVpv_tfJe8c52gRgWCY0PY18Sj-BDL9iXe_myyAS9Frmsfp3nuqvZdsA_bLy1VAYJBPdwzgrMMPVwApVC3ZXXwcPdcCp7ZbEQgESqBr9yuSuzIMVCT4Wb2ldo8RAEoAsGlhHZPih6haQtWsTgupumKfm-fWLDN4-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز تولد سید مجتبی خامنه‌ای هست
🔴
وی حدود ۶ماه در غیبت صغری است
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/alonews/146160" target="_blank">📅 00:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146159">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">وضعیت این روزای ایران خیلیامون رو به بن بست کشونده
درآمد 95 درصد مردم الان ریالیه اما قیمت همه چی به دلاره
اگر بخوایم از زندگی عقب نمونیم
و جزو اون 95 درصد مردم نباشیم چاره ای نداریم جز اینکه درآمدمون دلاری باشه
همه وارد کانال زیر بشید لینکشو گذاشتم  همه رو به درآمد دلاری میرسونه لینک کانالشو میزارم عضوش بشید
👇
👇
https://t.me/+fDXpi2Dbi185ZjRk
https://t.me/+fDXpi2Dbi185ZjRk</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/alonews/146159" target="_blank">📅 00:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146158">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25e221ca09.mp4?token=O4czq_HIPVmgn_qELh4XeMtuyWnDu7bQO2Hlz7kh9LFnG5Ft_040k8yqzFfj5VJsp8lPxkoCPaDSyGjP5a2C-fCpCsX0OSauXoEySSKvojSG5FIB1xQGFPFy7HaAEqOrku0k_-W5Ik50sszgRPpCOVNH2WJqjE2EDHD7d31gZiwM13gYwE7iWfSkXmcrgyYn4jfUa_p2nRGoRy8MEu5Ch0O80doCBE0JFsG0KKre_h2QP55iqBGNNP0nZvrrHygZt3ygVznJoo5NT93d8P_ZqLsOVKaVTMxTnumIUDCV2td5daeHk3bwOQwYX6p-ajuBVF7hHZtk5Wo5Lb3-Vzyfrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25e221ca09.mp4?token=O4czq_HIPVmgn_qELh4XeMtuyWnDu7bQO2Hlz7kh9LFnG5Ft_040k8yqzFfj5VJsp8lPxkoCPaDSyGjP5a2C-fCpCsX0OSauXoEySSKvojSG5FIB1xQGFPFy7HaAEqOrku0k_-W5Ik50sszgRPpCOVNH2WJqjE2EDHD7d31gZiwM13gYwE7iWfSkXmcrgyYn4jfUa_p2nRGoRy8MEu5Ch0O80doCBE0JFsG0KKre_h2QP55iqBGNNP0nZvrrHygZt3ygVznJoo5NT93d8P_ZqLsOVKaVTMxTnumIUDCV2td5daeHk3bwOQwYX6p-ajuBVF7hHZtk5Wo5Lb3-Vzyfrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سردار ابن‌الرضا: توان زدن ناوهای محاصره‌کننده آمریکایی را داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/alonews/146158" target="_blank">📅 00:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146157">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
سردار ابن‌الرضا: توان زدن ناوهای محاصره‌کننده آمریکایی را داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/alonews/146157" target="_blank">📅 00:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146156">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
همزمان با ۱۰تومنی شدن نرخ بنزین، جو شدید امنیتی در برخی شهرها حاکم است
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/alonews/146156" target="_blank">📅 00:08 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146155">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2eac7169fd.mp4?token=Xt0L04fHqze4AnwuUc1r0mx3rqHO0h7Bn_MLYcNdMwQbQUCaGVcqr0wwBWdQxP2tVXUDDeAGKF1ZYbsK3WRgQFb3WxdsN3by2NPTsaG9D3rCd61CirYcXERQMuMYl-pu7ct0c09ymhn6KFUVQYbsSdF7CcFJr7NNIFXMeJmj5lq28CtOEquPo8m4EV1Y08XZItgCib60X4zNsUdytP4yvHVTIFyaqXZuKfPBpwMI94TJSuvVK4fHJl53LL3_RXKlEV0yT_M6BS2-UFt7QUxP44PIZqQkd1i7GeYhN2rYgAzERQo6oN6H4akNqsTJmwcNMFpwjXJZF8C73-KXZJEDww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2eac7169fd.mp4?token=Xt0L04fHqze4AnwuUc1r0mx3rqHO0h7Bn_MLYcNdMwQbQUCaGVcqr0wwBWdQxP2tVXUDDeAGKF1ZYbsK3WRgQFb3WxdsN3by2NPTsaG9D3rCd61CirYcXERQMuMYl-pu7ct0c09ymhn6KFUVQYbsSdF7CcFJr7NNIFXMeJmj5lq28CtOEquPo8m4EV1Y08XZItgCib60X4zNsUdytP4yvHVTIFyaqXZuKfPBpwMI94TJSuvVK4fHJl53LL3_RXKlEV0yT_M6BS2-UFt7QUxP44PIZqQkd1i7GeYhN2rYgAzERQo6oN6H4akNqsTJmwcNMFpwjXJZF8C73-KXZJEDww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عادل فردوسی‌پور: خداداد عزیزی احساس می‌کند کسی باهاش کاری ندارد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/alonews/146155" target="_blank">📅 00:05 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146154">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61664472bf.mp4?token=njWLWsfEFjdsi5mNQT_l58Xdc0FFDx4z8s_u1nEs4hq1MNBXXDJY0uvn12vQmzz0CAZmNfl9TgvXetljCs8FSgsKkRlluEgxT7Dx6Qncs-96CqAaKKWbCxhGGHOVN759KDzBe5NJYLBL-6gQLickCg2HMDOJ2qCG8jrp_PTymp-FjY_zvBVI8amgzVdAmcOctyjQvxOqN4FicVfV0mjmcLraHwS35PrM8Htipv7OnAgyYzr4n3UscOsmX_ZGlfXUXOsXNWXvS_epwPBSxiSkU_g3HyYaF6OK_45TUJEK74-xs2bThMpbRRqMcHs6oQ7tCD3CA7rKJkqcXkEd-bxtPTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61664472bf.mp4?token=njWLWsfEFjdsi5mNQT_l58Xdc0FFDx4z8s_u1nEs4hq1MNBXXDJY0uvn12vQmzz0CAZmNfl9TgvXetljCs8FSgsKkRlluEgxT7Dx6Qncs-96CqAaKKWbCxhGGHOVN759KDzBe5NJYLBL-6gQLickCg2HMDOJ2qCG8jrp_PTymp-FjY_zvBVI8amgzVdAmcOctyjQvxOqN4FicVfV0mjmcLraHwS35PrM8Htipv7OnAgyYzr4n3UscOsmX_ZGlfXUXOsXNWXvS_epwPBSxiSkU_g3HyYaF6OK_45TUJEK74-xs2bThMpbRRqMcHs6oQ7tCD3CA7rKJkqcXkEd-bxtPTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرواز جنگنده پیشرفته جی-۳۵ چین با کمک سامانه پرتاب الکترومغناطیسی ناو هواپیمابر
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/alonews/146154" target="_blank">📅 00:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146153">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvRurqTRm9jioeFVwoTUaVIVmzFV1pugAKwBMltDkEwJM0l4raHFoJtJUpgWDtRND1ihfGR_is3DVJYK8xUCM-T6IMca4ikDHpYxw7o7rjdIGoBn_ceujXRved84LbkvVyP38hI7KMwPswAJFu5uhVSJ-IixSjha5TKhrFpfPBMAspRD1GYzQYagiNsAScdRez7MCfjiuXjeTAaNkCBpbLLSQ3GCl8HeLbcax8uUBJJkS6ymNJ23yEuUJhPzsWREfNmMt7F-3QNmNc6gm5NPAn76bo_qTcWgL1UaAqN1BZkJG3NVA1-OF7xK2mddxU8Q7de2PCOTVWXplDlKvtMEag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تورم خوراکی‌ها در مرداد ماه به ۱۲۸ درصد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/alonews/146153" target="_blank">📅 23:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146152">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
تانکر بزرگ قطری حامل LNG از مسیر تعیین شده توسط ایران عبور کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/146152" target="_blank">📅 23:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146151">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnYRsPFJVgOpT0B_aU59UI8LV2rF7ALTsrssqJtJJmXoNmWI16lJqh4IL9Ex9Ww9b6M553-xVtxsJGrERj4eT5VGwRLGYkc4pfMUflXmIeE194ELaDcBOdqpy8GR9BvuIAQfU4td0DZSpwzgQDEvoGs4d1szaRe95BaI7d0vK9TVfJxswRUjUe8G_dS6RQpPBh1-3fS3VfE_NjmHcypPsPBK_n7bpYfr-gVHBnhyQ5PknUDeMkl9QLBc1VgqPwG48VECpWIJfzsiqTjr8WTzA5hejJHgNJ5QaHBQV1U9SLJ3HoBdzNIR6MYBbyT2fYakPfCy0E63fALU4-i8sst2ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دوستان این تبلیغاتی که پایین کانال نمایش داده میشه کلاهبرداریه حواستون باشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/alonews/146151" target="_blank">📅 23:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146150">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
خانعلی‌زاده، تحلیلگر صدا و سیما یک سال پیش: تنگه هرمز و باب‌المندب را ببندیم نفت ۴۰۰ دلار می‌شود، این تازه ابتدای ماجراست
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/alonews/146150" target="_blank">📅 23:27 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146149">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/684d994c3b.mp4?token=ZcxlWy-E-cVwYLXRmPOKudqU4lurnmQKkjqLh-nnRucCdcuo5v4LgyaLpOH0Fkyoa1DIXC5hL869oPmFWD1i1kr-iS1ZjxqNt8qHmH7P1BdNz28jRV4HshldgFOtl7BBlKY09c3Du-sL89v6qqbKhCV5alYy_6KjjBZ-z1XD0yaWL6RDQqd0EA-8SgSMtqbDir9gFwsitxH9mGTfEHNAu7LbGavinul72bqZwxvq1swnvY6gSX0v092pwo-xOlNmb_aFFJoXIbJ4kHVZzvSRltQXkC9IoTsL_jFCI7ogLCbKCtSLe7rGHFFmkEBVqZM5XsiRBBCHT4E9b_QCGBfsmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/684d994c3b.mp4?token=ZcxlWy-E-cVwYLXRmPOKudqU4lurnmQKkjqLh-nnRucCdcuo5v4LgyaLpOH0Fkyoa1DIXC5hL869oPmFWD1i1kr-iS1ZjxqNt8qHmH7P1BdNz28jRV4HshldgFOtl7BBlKY09c3Du-sL89v6qqbKhCV5alYy_6KjjBZ-z1XD0yaWL6RDQqd0EA-8SgSMtqbDir9gFwsitxH9mGTfEHNAu7LbGavinul72bqZwxvq1swnvY6gSX0v092pwo-xOlNmb_aFFJoXIbJ4kHVZzvSRltQXkC9IoTsL_jFCI7ogLCbKCtSLe7rGHFFmkEBVqZM5XsiRBBCHT4E9b_QCGBfsmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خانعلی‌زاده، تحلیلگر صدا و سیما یک سال پیش: تنگه هرمز و باب‌المندب را ببندیم نفت ۴۰۰ دلار می‌شود، این تازه ابتدای ماجراست
✅
@AloNews</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/alonews/146149" target="_blank">📅 23:23 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146148">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b7e0f35c4.mp4?token=ZIszTYcV_9b2dM1L7R6UG0qebzWX5pRZkzPs5ZuON6xpC1f-iYBllov18m0l8wPD7nT2M-mSh_rsenxkMS-EMLgWtvs0dqa64WAbu7mN92irorgztyRIPrCOtrGRBefAAHmgq8dHiJ9S5Rinq-PFgmyvy_DP0UNS1drIkaG595mTop-D8UnG7vLAey7QhzIZXY8E8Dj5rfONFZUD6tmLQZIb3ouvmYj-7-pMBxLBREuswhH3IGMUUMUdcC-TrEujiA4S0P8ujA3_dYRQWtt9OKm28u7UrIJM-Le1CujDZwbi9E7XEjW_Pbs7I_f7H3oX5393_gfKCaOGmQHJ5g0rSyETRWdzcICKI714lu5zjnXFK23aAkFV71zdzOHkldqYG1ytIzLHGIslaf9HZi6J-MaBUhDyWvLx4w5JXzFXsKZMqz8H_XOVjskHtFJpt1iLuJVw-OyZrQOPdjA6c2FvgFifHtUqA4RlhS0bTBaZqnCjb_cyuCje0f4sUskqOSjCOPF3MM-1sAd5PCwM5pVd3mfDBW_80QPLbmx_cx4p88dGUbzoKYerVhZbs_h8dv9PeP295if5ZQFGXjj8TqIwzzhPjw3yEyVbI_y61FL9FO-p5jD-m1MRpw3a_lHXyvf2u2XHTWAGmsySxCk5cQVV2hP3o-ehRvWPT-urTNgyElU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b7e0f35c4.mp4?token=ZIszTYcV_9b2dM1L7R6UG0qebzWX5pRZkzPs5ZuON6xpC1f-iYBllov18m0l8wPD7nT2M-mSh_rsenxkMS-EMLgWtvs0dqa64WAbu7mN92irorgztyRIPrCOtrGRBefAAHmgq8dHiJ9S5Rinq-PFgmyvy_DP0UNS1drIkaG595mTop-D8UnG7vLAey7QhzIZXY8E8Dj5rfONFZUD6tmLQZIb3ouvmYj-7-pMBxLBREuswhH3IGMUUMUdcC-TrEujiA4S0P8ujA3_dYRQWtt9OKm28u7UrIJM-Le1CujDZwbi9E7XEjW_Pbs7I_f7H3oX5393_gfKCaOGmQHJ5g0rSyETRWdzcICKI714lu5zjnXFK23aAkFV71zdzOHkldqYG1ytIzLHGIslaf9HZi6J-MaBUhDyWvLx4w5JXzFXsKZMqz8H_XOVjskHtFJpt1iLuJVw-OyZrQOPdjA6c2FvgFifHtUqA4RlhS0bTBaZqnCjb_cyuCje0f4sUskqOSjCOPF3MM-1sAd5PCwM5pVd3mfDBW_80QPLbmx_cx4p88dGUbzoKYerVhZbs_h8dv9PeP295if5ZQFGXjj8TqIwzzhPjw3yEyVbI_y61FL9FO-p5jD-m1MRpw3a_lHXyvf2u2XHTWAGmsySxCk5cQVV2hP3o-ehRvWPT-urTNgyElU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی سازمان امور مالیاتی: از سال گذشته تاکنون حدود ۶ هزار شرکت سوری شناسایی شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/alonews/146148" target="_blank">📅 23:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146147">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
طارق صالح، عضو شورای رهبری یمن:
حملات زمینی و هوایی را در تمام جبهه های شمال، شرق و جنوب یمن بر علیه حوثی ها آغاز کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/146147" target="_blank">📅 22:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146146">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
معاون اول پزشکیان: یارانه واردات بنزین به‌تدریج حذف می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/alonews/146146" target="_blank">📅 22:47 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146145">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qd1nN9emdhUIZLjLr9Eg7pcQjLGq5EF_i-nDPr2L7lJGMUAby3Cxn-P2gs1-oCVSSJAHRf5u00FaqOXiWS2b1lY7KpZDhlz4_MnCW8JZz2J8IraKWRE7Odchg0fWRqD1pWLniduw54L8sZJCwAbaWgzFjB_isckdz00IURYh4CtcvYgXOeaIoKfKH8w2i1rQeXuZ9i-Ge4aYO8M1QPtIdLUM9xhXnspXhc8gF_--NNXYjwOj4C6ade5ijFf2laccZr2DtfcKZsZO3ub42-SjKvbKF5RiJmamAfqToY5-J4lpWSz-gfpTQElIDBeN-BLC5qdBaixaEO2lLGy4ZW04RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از جنگنده های سوخو ۳۵ روسی که بهم برخورد کردند.
🔴
یک خلبان کشته و خلبان دیگر زخمی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/alonews/146145" target="_blank">📅 22:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146144">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb6864bbb8.mp4?token=Up1G6irR5YY4WSefRuzAoYwdIVKuzsBRb0NjoMdL3bModGKC-2D9ykihKQ7k0eMFj7ZWBIv8yJ8KwVohpUn27r26-62Zbc0IvbZ2ATucT4Jb_DDKtpkkrbSqlBAkzlp19uFNkB7w4hIiig6eO3hFLZvVtIGos80JihfDyJzuMc7so9D4iwdtAM7K9TbJMsGnbhA3YMuhHk6eqb9QP_h1NULqN9S-WaDutsxZjGBujpb1LOsmmQjAzF8JrCgGRTTWAkHJmhj-TAwc97xyHnlzdg1BIfJX_hV-Mhh42f9Pna6118caP55g3oqFUSTs325tIo7BFqMIrliA3z2gDVPKpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb6864bbb8.mp4?token=Up1G6irR5YY4WSefRuzAoYwdIVKuzsBRb0NjoMdL3bModGKC-2D9ykihKQ7k0eMFj7ZWBIv8yJ8KwVohpUn27r26-62Zbc0IvbZ2ATucT4Jb_DDKtpkkrbSqlBAkzlp19uFNkB7w4hIiig6eO3hFLZvVtIGos80JihfDyJzuMc7so9D4iwdtAM7K9TbJMsGnbhA3YMuhHk6eqb9QP_h1NULqN9S-WaDutsxZjGBujpb1LOsmmQjAzF8JrCgGRTTWAkHJmhj-TAwc97xyHnlzdg1BIfJX_hV-Mhh42f9Pna6118caP55g3oqFUSTs325tIo7BFqMIrliA3z2gDVPKpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تو رشت یه خانم به این شکل با ماشین زد به یه موتور سوار و عجیب تر اینکه موقع دور زدن یبار دیگه زیرش کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/146144" target="_blank">📅 22:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146143">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
گفت‌وگوی تلفنی ترامپ و نخست‌وزیر انگلیس درباره تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/146143" target="_blank">📅 22:24 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146142">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L-MgWtMpxMpTsES47lc2FocTnqpX28LbvcweFUqYxusHwX6UrqFGXiST_-RoWGgxZEmC4Yfdc3NDX0abwzfKW35nozEQkHL-y-m39IvX1HoA1K3pBiGWiH5eCmjXuKuv5bmBZuP4oYcOa0_QEJN3EsB3PIjct5NUWUiK-5wmV0CD6PZm6HKW0QMWqXVk4eZtJQ6aXz5pEyWV1VK13B1s9bBoM64lx4I8GiUzujtEMkZwE1td-OTKqwbvU7NBvEojn8xkxSUjiHXI3-_ZflwUGChUE32xMNqQkmIM8PihpF2gispyslwpEmhgT5BkRgEHYduND64z-SxHnlYZLUTR1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تانکر بزرگ قطری حامل LNG از مسیر تعیین شده توسط ایران عبور کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/alonews/146142" target="_blank">📅 22:16 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146139">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c412317904.mp4?token=PQiIb2Xp37KPYEm32VGMCTJblrmSacJDfdEHeYtGRevRNzMS3x8nDBnt29sz3F5SMA9YljdaJXFbljskg8I_BR9nXONn1JZ44CXqCX-KYdptRl3notww8hH0O3aGxJBWEgc6zBRuv-0Of0AQhdgVb897_DcgfBKIdOyTSEWyidQYPU0Z_wCyRtErBac80Jax4LaYJRRqD3YOlny5yJ84cJYfLwITCcewwnHNmG-MaEzBwOuWQlsUSFOVku74dLDDxeShAgn9c8ijVuUg1BhTgDO3ThJevupZhOIoOt4tivCApVdpdPOzR4DcdijKRSHi0JP6MBKsmyIz1KbGnWVyO7X935yCjDfV1tZ4EqAEW-QT-ETsNW1dwYB6iGw6vYqdUrJ9AYl6yOgvP-APNVa581KNsjtd0mENIfRO60ficwYB1RmjrORpc1Qlm1o9T8byon1VnYsSzzlPZHJgY2OlH30znmfCChSCdOnBylcnYpoJuDYHqQCtlaEjVaaB4_ZAMqc9l6A4bZ2R2OxnOEDtySISTOVImmYQ-pLr1hC1IV_1k9ppsizWEipk90PcYY12VdBQOWWOOLnFnwcmmOc6ODxLwJy9u-0fNTQxlVZTro3qaUxVa6VjB5k_Khw9vMLy-lk0PguOMCxqoLJIi_0CfP4_o0_tOt9YWuBkTtVAExI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c412317904.mp4?token=PQiIb2Xp37KPYEm32VGMCTJblrmSacJDfdEHeYtGRevRNzMS3x8nDBnt29sz3F5SMA9YljdaJXFbljskg8I_BR9nXONn1JZ44CXqCX-KYdptRl3notww8hH0O3aGxJBWEgc6zBRuv-0Of0AQhdgVb897_DcgfBKIdOyTSEWyidQYPU0Z_wCyRtErBac80Jax4LaYJRRqD3YOlny5yJ84cJYfLwITCcewwnHNmG-MaEzBwOuWQlsUSFOVku74dLDDxeShAgn9c8ijVuUg1BhTgDO3ThJevupZhOIoOt4tivCApVdpdPOzR4DcdijKRSHi0JP6MBKsmyIz1KbGnWVyO7X935yCjDfV1tZ4EqAEW-QT-ETsNW1dwYB6iGw6vYqdUrJ9AYl6yOgvP-APNVa581KNsjtd0mENIfRO60ficwYB1RmjrORpc1Qlm1o9T8byon1VnYsSzzlPZHJgY2OlH30znmfCChSCdOnBylcnYpoJuDYHqQCtlaEjVaaB4_ZAMqc9l6A4bZ2R2OxnOEDtySISTOVImmYQ-pLr1hC1IV_1k9ppsizWEipk90PcYY12VdBQOWWOOLnFnwcmmOc6ODxLwJy9u-0fNTQxlVZTro3qaUxVa6VjB5k_Khw9vMLy-lk0PguOMCxqoLJIi_0CfP4_o0_tOt9YWuBkTtVAExI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بارش شدید باران در آستارا، املش و تالش
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/alonews/146139" target="_blank">📅 22:09 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146138">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
مدیر طرح CNG شرکت ملی پخش:
با استفاده از همه ظرفیت، هزینه سوخت خانوارهای پرمصرف سالانه تا ۵۰ میلیون تومان کم می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/alonews/146138" target="_blank">📅 22:05 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146137">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fb225132d.mp4?token=BX65LisUSKYfniar-F3u_-6nra6zQYOUwTsdYog6-1lhARD9whajPSuNkveZ6736jzf248sdHeIUrw-86205i3SaTehepzZjbhCCgjh-q14bgF0AT4xIyhV2NPc23i8UXkRXGgkHLkISIT6NhVZNLsNiCFmyVJv6ykrdcM1kNCRJmTwVDlEg7moB5clvfbbjP8NJCvOFAyyiJdrlH6KTB_5mgmV27RJBmO1qwdKweeQRKVo53BO2_ett-w7IECTu8UJkEIXcY68EWNcSspWtEf_lnErMZV2bgx3FdO7B-aTM2P_dKzovVswkBuxkkZTrRFzpmj6_cUjDaIwzy23QbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fb225132d.mp4?token=BX65LisUSKYfniar-F3u_-6nra6zQYOUwTsdYog6-1lhARD9whajPSuNkveZ6736jzf248sdHeIUrw-86205i3SaTehepzZjbhCCgjh-q14bgF0AT4xIyhV2NPc23i8UXkRXGgkHLkISIT6NhVZNLsNiCFmyVJv6ykrdcM1kNCRJmTwVDlEg7moB5clvfbbjP8NJCvOFAyyiJdrlH6KTB_5mgmV27RJBmO1qwdKweeQRKVo53BO2_ett-w7IECTu8UJkEIXcY68EWNcSspWtEf_lnErMZV2bgx3FdO7B-aTM2P_dKzovVswkBuxkkZTrRFzpmj6_cUjDaIwzy23QbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مصاحبه جدید صدا و سیما پس از گران شدن بنزین: یک لیتر بنزین کمتر مصرف کن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/alonews/146137" target="_blank">📅 22:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146136">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBKawRs0OEqQ2Hz7RFjE-5Sdj_Q2rGqClN_-_apdCctHpsC4QCKrq0pOpOVtNE_fYBtlDbNvQViAiKvnoT4GtbDx4q7TgPIJWtlIfDncn4l_Qv98OA389KzMYUrSUH2R7Vqs6yE2Vfo-vQ5u7w-VEpC5tJjWDfuUlaRXaUSXmQwlHnUVHX2B6XnrSKzxi6TfR_a4eZKESh29mtgnlHnZ1YBNW4OmYPdU3x7SR7T-KkPXWHDgJlx3vIaTj8x5WR7FbABi0MG8O4eKr6IyKoJddxixxVxaGemjoq-w-hMq3mSXAC3bDikv_HdLv3Ki8iaRQrODg3GDcTmTyct69P1xJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون گزارش های اولیه از شلیک چندین موشک از جنوب ایران به سمت تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/alonews/146136" target="_blank">📅 21:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146135">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a30ef5442.mp4?token=ehIS1nZB3OTaq0ZZ9WuhFK4Krb6ChfjedvHt2dRwupJ-fAdZKDPXKQGuizv7NEI2Ne3eHyWX96Xkuj_hHrijE1sDzcZACGsNv1p-buZFdLUinB9ge6oEIrV3qIXKiSjpFHH284BrjX2KPgIJbS_yy0vUKM5dMVkLcm_gw9W2FYYozBaaRcm3OM1G48FDZy_eumxqDh3gbWn5LgHpuSR8rnBuOpZZ7c_9TiGZXBThcX9maj0kTitP3mXKZCkGWZ_FIxGK05mOgVmCPJsgq0TqGCW9aPo2y8GhLAXrrgX_cKoIQ-5DbclTH98ED-zqGjfROxyQ-7rpVcok5yXkljcIsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a30ef5442.mp4?token=ehIS1nZB3OTaq0ZZ9WuhFK4Krb6ChfjedvHt2dRwupJ-fAdZKDPXKQGuizv7NEI2Ne3eHyWX96Xkuj_hHrijE1sDzcZACGsNv1p-buZFdLUinB9ge6oEIrV3qIXKiSjpFHH284BrjX2KPgIJbS_yy0vUKM5dMVkLcm_gw9W2FYYozBaaRcm3OM1G48FDZy_eumxqDh3gbWn5LgHpuSR8rnBuOpZZ7c_9TiGZXBThcX9maj0kTitP3mXKZCkGWZ_FIxGK05mOgVmCPJsgq0TqGCW9aPo2y8GhLAXrrgX_cKoIQ-5DbclTH98ED-zqGjfROxyQ-7rpVcok5yXkljcIsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارش ها از حمله اسرائیل به منطقه النبطیه الفوقا در جنوب لبنان گزارش می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/alonews/146135" target="_blank">📅 21:48 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146134">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
هواشناسی: شدت بارش‌های امروز و فردا منجر به صدور هشدار نارنجی شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/alonews/146134" target="_blank">📅 21:46 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146133">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
هم اکنون گزارش های اولیه از شلیک چندین موشک از جنوب ایران به سمت تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/146133" target="_blank">📅 21:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146132">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
زلنسکی به اکسیوس: واشنگتن به دنبال کاهش تنش‌ها بین روسیه و اوکراین در طول زمستان و از سرگیری مذاکرات صلح است
🔴
احتمال برگزاری دور سه‌جانبه مذاکرات آمریکا، اوکراین و روسیه وجود دارد، اما هنوز تصمیمی در این مورد گرفته نشده است.
🔴
اوکراین تمام امتیازات ممکن را داده است و هر مسیر دیپلماتیکی مستلزم تضمین‌های امنیتی و حمایت اقتصادی است.
🔴
آنچه از دیدار ویتکوف و کوشنر فهمیدیم این است که پوتین آماده است تا در مورد ایده‌هایی برای پیشبرد مذاکرات بحث کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/146132" target="_blank">📅 21:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146131">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/suCXyU1vc6t0UYJtRBk5TotqQOAo6RaJ4Nsh3sA5JUutbx2MsopI70kRuh13KIqwbXzXp_xPoqJ5HBIlnxRxom6z05mvsZZf4IBtbXu1-vtwzIwLr59IhTgeup4qmKCUOH5Eu22AJL7UEYBJK4potQQwnfoRbqcDBBMioByCSRKD7l_nmsgZkRZ4wrVzG07Ylb9AvrXWVMSaygeG_zYKCVRRT4kmLGQieT-vFR89tboKRDf0TrOF3yZPHeebAgWzw_LdlBzMApuPzVy4bn8Jg10u5DPdx4mu01wIY35g8i4WznZp_dLIYF-E7miN2AWOw8JxFFBY4P_8q-4ygqXTeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : دیگر هیچ فروش محصولات شرکت بمباردیه در ایالات متحده مجاز نیست! محصولات آن‌ها به اندازه‌ای باکیفیت نیستند! بیش از 50 درصد درآمد آن‌ها از ایالات متحده به دست می‌آید. آن‌ها از خریداران آمریکایی، شرکت‌های آمریکایی، فرودگاه‌های آمریکایی و خدمات آمریکایی ارتزاق می‌کنند. در حالی که کانادا، بانک‌ها و شرکت‌های بزرگ آمریکایی را در سراسر ایالات متحده تحریم می‌کند.
🔴
آن‌ها حتی شرکت Gulfstream Aerospace را از انجام تجارت در کانادا منع کردند. این کاملاً ناعادلانه و غیرمنصفانه است! آن دوران به پایان رسیده است! اگر آن‌ها می‌خواهند از بازار ما استفاده کنند، باید در اینجا تولید کنند و از رفتار با آمریکا به عنوان یک "جعبه سپرده" دست بردارند.
🔴
محصولات آمریکایی را بخرید. با خطوط هوایی آمریکایی پرواز کنید. از مشروبات الکلی و نوشیدنی‌های آمریکایی لذت ببرید. در دریاچه آمریکا قایق‌سواری کنید. آمریکا اول!
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/146131" target="_blank">📅 21:27 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146130">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
طبق گزارش رسانه های عربستان،
چندین قبیله بزرگ در شرق یمن برای جنگ با حوثی ها در حال بسیج نیرو های خود می‌باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/alonews/146130" target="_blank">📅 21:23 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146129">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/todZFt65BmtlVoQUVeXJBPXq1KbG7Wrvb7Co0JVssjCv2nm51aVcVSN9D9e--B4YpfNF5x-G1zNwgmie8JvgeTh5I9TWy3W-QqYFbNEHonHdkAY73ry67c39ZnhZqHlLeL44x14USRJXRYaY6Uh89llvsFEnN0xfy65BR2Sj-Tu095zUC6TIvogjQXNMKq3d-FtHZ-dJIIqTSGQYLF8bzdimO4v_1SM63KfeZcUGcJbqe2WwLOAyY81eL1mLQ9QpSL4ybrmSsWLU0kjQE9KDCwLoUQqXXpVJIxrNifCJ3LRHuRzyyT7xOqZhfEZ400kgLXk3D9pJ8jBhTNIxkyldXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
این پیام میتونه زندگیتو تغییر بده !
می‌خوای از ترید سود بگیری؟ بدون اخبار و تحلیل درست، فقط داری شانسی بازی می‌کنی!
💎
ما اینجاییم که بهت بگیم:
💰
آموزش گرفتن درآمد دلاری بدون ریسک و سود تضمینی !
اگه می‌خوای به درامد دلاری ثابت برسی جات اینجاست
✅
👇
https://t.me/+fDXpi2Dbi185ZjRk
https://t.me/+fDXpi2Dbi185ZjRk</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/146129" target="_blank">📅 21:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146128">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
بسیج عمومی در سراسر یمن در حال وقوع است، یمن بار دیگر پس از 5 سال درگیر یک جنگ داخلی تمام‌عیار شده است و نبردهای متعددی در تقریباً تمام جبهه‌های یمن در جریان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/146128" target="_blank">📅 21:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146127">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
آنکارا: اسرائیل تفاهم‌نامه اسلام‌آباد را خراب کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/146127" target="_blank">📅 21:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146126">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNz3BSCLebiUyytzXiVOCWXPw3yPHviQTrgRN2lhAFOUaFLXnEBKcQZWd1QsZP7gjs7S7oWcJ1IfemN26c97zBk4iE-4xrrcUb_8k3dUbVHAJuyQE4Rf7pjjwZqImf0vFtc8n7Gkoq-K2Dvphe1WrzEanylZjeCTVlAmV5QTQlgWATPtvdk-jCdAEkw7O2MQebY6DT5uL9FbfPzOT182bwyReuDzmzn7WQim6nxw-TxA5hEb9WqFjGcxPwAFH4ftFw6wxAYa2SVACUS6VZqfzydPn-i1UkTu_fRec6XUgTD1ffUQf1jYXDKl2MIl64flRaZcs9BetnBB9s5xypK7aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روزنامه تلگراف انگلیس: رئیس جمهوری سابق ایران ( روحانی) خواهان برگزاری رفراندوم برای پایان جنگ شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/146126" target="_blank">📅 20:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146125">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XR_oTMItRyvqEGiEp84WupsFwBupwwptKstapWmP1cWPYFDoK5v1cPmQLvVLmEfv0d05VPUPc3z2vbEGpXUln00kvj7YufCHtRkGUkpJ7qwRvcc8ShauGzZVKf9lAP9WmYKVCA2oFtTDZta9S7aUr3SSw5xWQST_8STgRDMRGGHcWwbPSUY8e9gl_IAAyrUDM_HlPRXjAGwTzB-2KXEosAjykkRfO6vo04mTi7ATUA6wfCDJo51L1v-Tko7HJqG4n1Ycd4zyKvaI83d2wHyK8c01ST1xM5ec3LRxJvTU3hn5pQpWtVvwEfsWCNr5IzckPbxUn-MYTVcBnK_tdo32Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۴ ماه محرومیت و جریمه ۲ میلیاردی برای خداداد عزیزی
🔴
عالیشاه هم ۴ جلسه محروم شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/alonews/146125" target="_blank">📅 20:48 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146124">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
پرواز چهار فروند بمب‌افکن استراتژیک Tu-160M از پایگاه هوایی اوکرایینکا در روسیه. انتظار می‌رود این بمب‌افکن‌ها در ساعات آینده، موشک‌های کروز Kh-101 را علیه اوکراین شلیک کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/146124" target="_blank">📅 20:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146123">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه قطر در گفت‌وگو با CNN: ما نمی‌خواهیم درگیری را متوقف کنیم و پس از ماه‌ها دوباره به آن برگردیم.
🔴
اولویت ما باز کردن تنگه هرمز و کاهش فشار اقتصادی بر مردم منطقه از جمله ایران است.
🔴
ما در تلاشیم تا از تشدید تنش، حملات موشکی به مناطق مسکونی در خلیج فارس و حملات به ایران جلوگیری کنیم.
🔴
ما به اقدام جمعی منطقه‌ای برای آغاز گفتگوی فراگیر که شامل همه باشد، نیاز داریم.
🔴
تحریم‌ها ابزاری دیپلماتیک هستند که مدتی است در منطقه مورد استفاده قرار گرفته‌اند، اما به نتایج مطلوب نرسیده‌اند.
🔴
ما چندین ایده ارائه داده‌ایم که برخی از آنها شامل یک یادداشت تفاهم است و ما همچنان در حال توسعه راه‌حل‌های بیشتر هستیم.
🔴
تاکتیک‌های فشاری که توسط هر دو طرف به کار گرفته می‌شود، در نهایت به بندهایی در توافق تبدیل خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/146123" target="_blank">📅 20:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146122">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YIrz98B5Sfd6JGT6dTgAtsVnsawE1aLuENDAaU0LAuF_SJjkqh-urPoSZxTuewiqyLNzgcTMZKx9PZkDuvEAFWYLSSriSFk7lcmMPwS542g8VmNm4MjPyv52WV43XEy4jCIe_dG4Ss7PXS1iZvZa-hdT5HSkEnQbJ1zDIwDtw8qz31zODXtjvIqwZEnjthx4OJRX3FOWy2PxNBUEkL2laQs3lJpcuFqlpghb4ET_DQEZiri4E3R5EAaPQ1jRWorx5L-ZhFL91f65NPfCTg9BydaBn-kjsi9_wMFckXdv8qxh9ztbY8NCruiLYpYNRJKBZy55KEdFg-hlYtIIg7n_Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چند روز پیش از رونمایی طرح اقتصادی «فشار حداکثری» علیه ایران، وزیر خزانه‌داری آمریکا در یک نشست خصوصی مدعی شده بود پس از اجرای این طرح، ارزش ریال در برابر دلار در تهران به‌سرعت دو برابر خواهد شد.
🔴
مرندی این ادعا را تکرار وعده‌های قبلی آمریکا دانست و به وعده «سقوط تهران در ۱۰۰ ساعت» اشاره کرد.
🔴
وی تأکید کرد این نوع پیش‌بینی‌ها همچنان ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/146122" target="_blank">📅 20:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146121">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
اتحادیه اروپا و گرینلند با امضای توافقنامه‌ای جدید، بسته سرمایه‌گذاری ۲۰۰ میلیون یورویی برای سال‌های ۲۰۲۶ و ۲۰۲۷ را نهایی کردند؛ توافقی که در بحبوحه ادعاهای دوباره دولت آمریکا درباره الحاق گرینلند، بر تقویت روابط اقتصادی، مقابله با تهدیدهای ترکیبی و افزایش تاب‌آوری منطقه قطب شمال متمرکز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/146121" target="_blank">📅 20:26 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146120">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
گروسی: اینکه ایران می گوید سایت‌های اصلی هسته‌ای برای بازدید بیش از حد ناامن هستند را مانع نمی‌بینیم
🔴
همچنان هیچ گزارشی از سوی ایران درباره این سایت‌ها دریافت نکرده‌ایم؛ این گزارش باید شامل هرگونه تغییر در موجودی مواد هسته‌ای و وضعیت دسترسی‌پذیری سایت‌ها می‌بود
🔴
به ما گفته می‌شود که تا زمانی که در مذاکرات گسترده‌تری که در حال انجام آن هستند به توافقی دست پیدا نکنند، همکاری نخواهند کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/alonews/146120" target="_blank">📅 20:20 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146119">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qbSgPveklCgwvf6vMNFcOiPOUmzYODJ8vyHZIyNtnAK9_JcGO0vdzgVQ3b663p2pR8LPmz1TXt0n5vHIilwAZ19FN0PYsA5_pcG8W4eW8jg_zfKCs66Zx_OCqRkshnSSbgZY2TBG52qR7WwL3Z_KL-yrFYKrVqVZtPIPzCg1nH6hsHkOiT6N0uKqVVT5hTwTHdCPHKoeoO2zliePYOrBxiAE_SVBxY2leYJQlJfGksAKXAR4hivbMARCAyeZN2IXFO29rfxfGftjTwtm_pXCXArt3uLygIWqVNU3ugbKiKVp1aicfQeFjr5KYyg6h5ElS3I5-V1MnoB3oFY-cHFmpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانال تلگرامی «جنگنده بمب‌افکن» که ارتباط نزدیکی با نیروی هوایی و فضایی روسیه دارد، گزارش می‌دهد که دو جنگنده سوخو-۳۵اس در منطقه کورسک روسیه با یکدیگر برخورد کرده‌اند.
🔴
این کانال اشاره کرد که علت این حادثه در حال بررسی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/146119" target="_blank">📅 20:13 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146118">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8c7c5ba81a.mp4?token=BjxYqnVMNoNc64ZEJQ4Jvh_XGME--wrLXJwnTPGpFVoOK8Uhb0uEoxafYidTm6chdFUWZdKT7XNxeFKwUP-WBAi2iGMuZ4OBGc1KDQtq0TY88Uh8za2xCb-YQiyChsdsnUJvn5H0_Cc5JccGW9g2ENpoPrUZMbVGmbPKyPTvKb9nYTgtzw_2lGZ0tWPn-AglZUSmhYPi0QOOJDm04FnfXs45NfCHG5LNbgs5HkOYbsiUpPJysvOoTT6-utBP2Y-ajm50kRG5lguPc2ZY8UqUci6Ftg1bNNUyxiwIGfXLvXT2Q21xWFGlviX0IRv9U1G7uaH3f5nXXMGqzdV3bYwV6A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8c7c5ba81a.mp4?token=BjxYqnVMNoNc64ZEJQ4Jvh_XGME--wrLXJwnTPGpFVoOK8Uhb0uEoxafYidTm6chdFUWZdKT7XNxeFKwUP-WBAi2iGMuZ4OBGc1KDQtq0TY88Uh8za2xCb-YQiyChsdsnUJvn5H0_Cc5JccGW9g2ENpoPrUZMbVGmbPKyPTvKb9nYTgtzw_2lGZ0tWPn-AglZUSmhYPi0QOOJDm04FnfXs45NfCHG5LNbgs5HkOYbsiUpPJysvOoTT6-utBP2Y-ajm50kRG5lguPc2ZY8UqUci6Ftg1bNNUyxiwIGfXLvXT2Q21xWFGlviX0IRv9U1G7uaH3f5nXXMGqzdV3bYwV6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حرکات زمینی نیروهای ائتلاف در استان الجوف، در میان گزارش‌هایی از یک تهاجم زمینی در این منطقه
🔴
همچنین یک حمله هوایی علیه زندانی که توسط انصارالله اداره می‌شد در الجوف انجام شد که منجر به محبوس شدن ده‌ها نفر گردید
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/146118" target="_blank">📅 20:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146117">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
مقام ارشد آمریکایی: تنگه هرمز کاملاً باز است و توسط نیروی دریایی آمریکا کنترل می‌شود
🔴
به لطف محاصره تاریخی و موفق، هیچ چیزی به ایران نمی‌رسد و تنگه هرمز برای همه باز است.
🔴
روزانه میلیون‌ها بشکه نفت از تنگه هرمز عبور می‌کند.
🔴
ایران از طریق یک فرآیند اقتصادی و موفق‌ترین محاصره تاریخ، از نظر اقتصادی در تنگنا قرار گرفته است.
🔴
از پاکسازی هرمز از مین‌ها، حمل و نقل به بنادر غیر ایرانی و از مبدا آنها به طور قابل توجهی افزایش خواهد یافت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/146117" target="_blank">📅 20:00 · 16 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
