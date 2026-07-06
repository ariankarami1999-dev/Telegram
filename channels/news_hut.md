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
<img src="https://cdn4.telesco.pe/file/Mc9KBt3uUFjBj7OblSlHJSBVtcsquzDO8NIehmIP4XNSfYSW74sB4OQQ9vFFm7d39C1oaeixtLiUBpH7mxBNk704wbzbZNje2ajnO_xekYLdCA2G2qwcb2pgw8gQ9NNkeD1tQwE-9CZLnHzu18qeogCzc8C9TyFbMrbxsBBR83RtrJtDxDCxZwtgPkTVJR-PUB05B3Yh26FlwqVMMMqfOuzESJ_cfmJVqQDJbxZ4gtYbpkOjPCI-Zpz2PJvigT9mXPLO8VtJm_Dv6xy2oWP7e36OJ_Mg1UN5WFE0PX0TosUYLqRQLeiHJ_d5H1MM_RAVpsysoM1wvh0g7phFiegx7g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 201K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 11:41:22</div>
<hr>

<div class="tg-post" id="msg-67370">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a17dafc375.mp4?token=FzyEjmjiQV0df-pqQlfMETuJyKXdLlwoO-HdITmYi4BS7J6F57c4p82ZKkwSce8EXW2rDk2O60-cVziNHytelnQGQoAZGLC8a4i807wGNxKxdUkRQz8uk-48Xs76T1Siy9-49Dx2t0-legX_dCzFPnC4kgUg0eMbsktqoQEeKDHSD2jSk-o0W0iOKjhwFpmyWkAbnu71zC99GbNnW9VAu_BNxHL7ftW492KivQPlAjl0zYKEl4rT1AmNgU5EDC9mR4goYsecEd0CsP2DKOIyloe9FOAuSS6ajnZW8uUJilGfyVdFksLcnRJ8jIlU9lyZEDiWdBvsqJ6ewg8pj80ZDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a17dafc375.mp4?token=FzyEjmjiQV0df-pqQlfMETuJyKXdLlwoO-HdITmYi4BS7J6F57c4p82ZKkwSce8EXW2rDk2O60-cVziNHytelnQGQoAZGLC8a4i807wGNxKxdUkRQz8uk-48Xs76T1Siy9-49Dx2t0-legX_dCzFPnC4kgUg0eMbsktqoQEeKDHSD2jSk-o0W0iOKjhwFpmyWkAbnu71zC99GbNnW9VAu_BNxHL7ftW492KivQPlAjl0zYKEl4rT1AmNgU5EDC9mR4goYsecEd0CsP2DKOIyloe9FOAuSS6ajnZW8uUJilGfyVdFksLcnRJ8jIlU9lyZEDiWdBvsqJ6ewg8pj80ZDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وحیدی فرمانده کل سپاه با موتور اومده مراسم
@News_Hut</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/news_hut/67370" target="_blank">📅 11:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67369">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abfc46c7e6.mp4?token=jzEZOSoAotmv2J8cQkgJ1Y3IKq4RpbQKhlxGPwaH_gCiquI_lwXdOSeM9tDwRYFFIHPuN8ntAXB49PMG1s8dedNX2AlD-_pJttkbtgLTUGLtRNezGLJ2AF2qvZiG-mhtbrGLqQNOemSviKgAOYPCq2vFEmGqinGnVtd8HfZgQbWWyV1XSJOlK5T34lafiGSu5xyQV82Ox6vdp7xcv2kbuUVjVJ_JQksIm9-bF7TJuDdZJeCRQBKRJ92St7Y0Zc3Z6kcRl04lE6sgrRPzRDW1CCIzzMlFrnYX7fqdWIdzTj4X7SMDedOUiZOxXqQTT3vGXnY-hZ01cADtnUH2B9qrng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abfc46c7e6.mp4?token=jzEZOSoAotmv2J8cQkgJ1Y3IKq4RpbQKhlxGPwaH_gCiquI_lwXdOSeM9tDwRYFFIHPuN8ntAXB49PMG1s8dedNX2AlD-_pJttkbtgLTUGLtRNezGLJ2AF2qvZiG-mhtbrGLqQNOemSviKgAOYPCq2vFEmGqinGnVtd8HfZgQbWWyV1XSJOlK5T34lafiGSu5xyQV82Ox6vdp7xcv2kbuUVjVJ_JQksIm9-bF7TJuDdZJeCRQBKRJ92St7Y0Zc3Z6kcRl04lE6sgrRPzRDW1CCIzzMlFrnYX7fqdWIdzTj4X7SMDedOUiZOxXqQTT3vGXnY-hZ01cADtnUH2B9qrng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عباس موزون، مجری صداوسیما:
چند بار [روح علی خامنه‌ای] از بدنش جدا شده بود و تا ارتفاعی بالا رفته بود.
«اصلا بعید نیست آنهایی که علیه بشریت عمل می‌کنند، از نیروهای شیطانی کمک گرفته باشند.»
چی میگه این
😢
@News_Hut</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/news_hut/67369" target="_blank">📅 11:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67368">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCGmu_G7lKVEjBQbjDGNK9EKoiF3o8wE6vhI4efs_lNVrll75pb1C4rfdBxML7TqNjIDRhyg2IYrn_W_0HJD9y1R2fhT0wJu3ll1O8fVwPP7rf4f-Zrj8lVybwQFx7axDUeHhRR8UeJtqmSv64ahdeDjuF4pUoghUzyyi4Hp8EuKIXd1d9ESKWmVizX0bKH85qFNSRWzIHMc3RY9sGaQVb-olUEhLfVjwYvO7jZELGfMKee8OR47shZ5RQwwBV1674VzyoSW-1t4KjwtviJLdjE96YE5l12D5jT008uUTeljloE6syj1lZoOnBFmyiSY0rVIs8I3p4-1YXpsFWbc8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اکبر هاشمی رفسنجانی،24 اردیبهشت 1370:
سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
@News_Hut</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/news_hut/67368" target="_blank">📅 10:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67367">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38c47b7b97.mp4?token=cBttqZZX1RASI2Xd7kLdGcBk0tte5siUZsGK2kiPnPF6q0l8kHina9hDDGF15HqdxWQOCXedK2XgGklhADwHF5o1F49ZaUOSYbelKG68ESPGgdJrTj9d3wD6wx-x3wiTbDbhcPRKp_UFD0OgBHoV207KYrqJfbesY_ofgYzyATksXScb15fFQPoKGfqvrau79t5rNRXbeLnecj2hJWPc5ENVC7XkNHpTFn9jvalkfT85z4lPhZ7sJLwoc6LMgSNZtGRHV1w9zJfpG9UYvZTeG9Tt4ffgCt8u6qTjYdyoaTY-BIo8R9pHGmW1PFR3kIOVBgNdoucAcpphVRzlFYiZhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38c47b7b97.mp4?token=cBttqZZX1RASI2Xd7kLdGcBk0tte5siUZsGK2kiPnPF6q0l8kHina9hDDGF15HqdxWQOCXedK2XgGklhADwHF5o1F49ZaUOSYbelKG68ESPGgdJrTj9d3wD6wx-x3wiTbDbhcPRKp_UFD0OgBHoV207KYrqJfbesY_ofgYzyATksXScb15fFQPoKGfqvrau79t5rNRXbeLnecj2hJWPc5ENVC7XkNHpTFn9jvalkfT85z4lPhZ7sJLwoc6LMgSNZtGRHV1w9zJfpG9UYvZTeG9Tt4ffgCt8u6qTjYdyoaTY-BIo8R9pHGmW1PFR3kIOVBgNdoucAcpphVRzlFYiZhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده یاد مانوک خدابخشیان:
خرافات پدر ایران رو در آورده.
آینده ایران در یک جمله است؛رنسانس.
@News_Hut</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/news_hut/67367" target="_blank">📅 10:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67366">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33573d06e9.mp4?token=rCU-rqqHnRDqzmN6-q6xiHygvmHiJKusNZPs--WBKhdmFptLSl4HnmCIclBFSorki9XM6f0RRzXun1XtUktd9EZkMFNv4tXelU1AA9bEJZ2pEhfcpu9wYmQBiMg0HoBs7H_0qmTZz4P3bPhiWAZNH9OO8GLCAYnimJ30s59CSl8w3phkJ8zjl1BdANuXvUYNKqo1bdMioWVCqfgiuRIf-FZK7lXzqH_mo0WMpP8n7liODLuA7Y2kn61Us3NkbPaZrYdvW65otJ-nA4Y9NZl1z6gG3MZejfoNwi4SufpSd9mQX13DkQTsTghcb0cr4e3YUWEnUMLg4l9q9nwZl7VozA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33573d06e9.mp4?token=rCU-rqqHnRDqzmN6-q6xiHygvmHiJKusNZPs--WBKhdmFptLSl4HnmCIclBFSorki9XM6f0RRzXun1XtUktd9EZkMFNv4tXelU1AA9bEJZ2pEhfcpu9wYmQBiMg0HoBs7H_0qmTZz4P3bPhiWAZNH9OO8GLCAYnimJ30s59CSl8w3phkJ8zjl1BdANuXvUYNKqo1bdMioWVCqfgiuRIf-FZK7lXzqH_mo0WMpP8n7liODLuA7Y2kn61Us3NkbPaZrYdvW65otJ-nA4Y9NZl1z6gG3MZejfoNwi4SufpSd9mQX13DkQTsTghcb0cr4e3YUWEnUMLg4l9q9nwZl7VozA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو مراسم وداع با جنازه علی خامنه‌ای، وقتی نوه‌های خمینی میرن جلوی تابوت سید علی خامنه ای، قاری این آیه از سوره نساء رو به کنایه می‌خونه:
آن گروه از مؤمنانی که بدون بیماری جسمی در خانه نشسته‌ان، با مجاهدانی که در راه خدا با اموال و جان‌هایشان جهاد کردند، برابر نیستند.
اونا هم برمی‌خوره بهشون وسط آیه ول میکنن میرن.
@News_Hut</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/67366" target="_blank">📅 09:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67365">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InBe6CyMcedOzNWnh8cTop-GOT0XTTR4aUzGS99NfZwPrD-6dWJkWz2sjc6996UWW7NNnQZEsmRRuwJQOe0jE7ElFI6TzONmlQ101p8Ui31RUQNIXia1rnn7RMmYzBGv_FcdyXAjXSo-n-jHeEbQLG69QhZy9PC13MDg5YXo7BTkRuOhxpzjjSPOGf9r9ZaXQ6jxuWBMKdE2mz9Gg7D-QP0ARSc_1Q45UzgQiSwXIDUf_h5N2hLuGk3vt4l2oViNq9vgoCE4DIP06b7gN4trAV7HfYTu3De1kZXxHm4uGwv8oQX9xGtI60edh1mmPbLNEuN2AyZR-ICdOC7OywagHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
قالیباف در گفتگو با محمد درویش، رئیس شورای حماس:صلحی با آمریکا وجود ندارد و اسرائیل را به رسمیت نمی‌شناسیم!
🔴
دیپلماسی باید در خدمت حفظ و تثبیت دستاوردهای نظامی باشد.
🔴
مذاکره زمانی موفق خواهد بود که کشور همزمان آمادگی دفاعی خود را حفظ کند.
🔴
ایران بر حفظ تمامیت ارضی کشورهای منطقه و پایان جنگ علیه متحدان خود در محور مقاومت تأکید کرده است.
🔴
جمهوری اسلامی صلحی با آمریکا ندارد و اسرائیل را به رسمیت نمی‌شناسد و حمایت از جبهه مقاومت را در قالب‌های مختلف ادامه خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/67365" target="_blank">📅 09:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67364">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/67364" target="_blank">📅 03:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67362">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kb60kppNtGUbRxgL1M0jKjiAdO22VNs5mlwzt8WUtf3pAZLVoOWy7G92d64OKOg-cFL_RtjQBV0QRP9uQjSGH3wTuzzoU9XABDOc1RIBp18kU9p1tBAV37TVgnIgG5n3oSC2z5E1cw_ugP1PR4d_qf7Movvx2vmNXWkv9INkZA15yb51ObV6w8UZAiVRTBr-viY5ymilp9dIS135sTTP8kI7FAe3c1KvTgp5C0TbdIvp7-oeIdmIA_ugtl7mUujIF7R1NZsIPYNS76Zz1qvmfldQcBnlZXppwJxKySyOAQEBmkXKNbX70etdE6y5KtdSVWLAPxOpWq8rq8mQqkQn5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/67362" target="_blank">📅 02:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67361">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a1fe48304.mp4?token=WxFit6KpQSLJQaiTdnpj3tWxZOIHlpc29-8ALtwJNHayqytyztfrcU9sW2W99q98AEUX-oaL4yWd3l6Rb65e59tQKMd8NmxwAJ_faW-QX3mZskNWmE_DgmQcL1_JNLNsscmBq9i5m5-a1is2Q_ursuKm-yO9bRz0m56MzOLFRRv5oDPMxSHvIijQ1nab5rIBtXedWVZynvpNj3OChxXatr6rphRMbR-xOa-UBIvCzPek_lsN8ZlMWD9RfOpxpXLKl8JoxvqAZByFd3S-hogPaKe7_puy4ujn00xwD7dV0KPvzdZmHzOCBJrpdosogE3cCZaEn8SdHLv4Grvtetz2Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a1fe48304.mp4?token=WxFit6KpQSLJQaiTdnpj3tWxZOIHlpc29-8ALtwJNHayqytyztfrcU9sW2W99q98AEUX-oaL4yWd3l6Rb65e59tQKMd8NmxwAJ_faW-QX3mZskNWmE_DgmQcL1_JNLNsscmBq9i5m5-a1is2Q_ursuKm-yO9bRz0m56MzOLFRRv5oDPMxSHvIijQ1nab5rIBtXedWVZynvpNj3OChxXatr6rphRMbR-xOa-UBIvCzPek_lsN8ZlMWD9RfOpxpXLKl8JoxvqAZByFd3S-hogPaKe7_puy4ujn00xwD7dV0KPvzdZmHzOCBJrpdosogE3cCZaEn8SdHLv4Grvtetz2Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
ارتش دفاعی اسرائیل:
پس از فعالیت در نزدیکی نیروها: ارتش اسرائیل یک هسته تروریستی وابسته به سازمان تروریستی حزب‌الله را در منطقه العقیده هدف حمله قرار داد
امروز (یکشنبه)، نیروهای تیپ کماندو یک هسته تروریستی وابسته به سازمان تروریستی حزب‌الله را که با موتورسیکلت در منطقه العقیده، در نزدیکی منطقه امنیتی محل فعالیت نیروهای ارتش اسرائیل، در حال فعالیت بود شناسایی کردند.
فعالیت این تروریست‌ها تهدیدی برای نیروهای ما محسوب می‌شد.
پس از شناسایی، ارتش اسرائیل در یک حمله دقیق، این تروریست‌ها را با هدف رفع تهدید هدف قرار داد.
ارتش اسرائیل به فعالیت برای رفع هرگونه تهدید علیه نیروهای خود ادامه خواهد داد و به سازمان تروریستی حزب‌الله اجازه نخواهد داد به شهروندان اسرائیل و نیروهای ارتش اسرائیل آسیب برساند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67361" target="_blank">📅 01:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67359">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WaPT6RWhqkjXN-jyalnLJmnY73C10zKmf_aUKn0nCBhGp_M8m0GyscTMAzmfOe2ER8cw7QU5yrriXAN2Oi13jnnllXjTkrGkwf2ceUXWHCYTEtlwQ_OzoMERXimQA_5nx8xyUFQd1dakNrpE8pnibOgMtpsYfYynwmLoV4rdZ-Wdeq06MZD5qDlFkFnt4RPV-LOXVUaSh35a478xG1PnE1hGEEIUx48VVbt68LTUNOdar4QtnlCBuN6e2SoXm3uhCPMrUYB-83wG4HC7FnuI1FAeOGwA_o2c3eKsyfiWa0nTayBnSooBChqjkX0BRPnGYOecb2EyNz1RYb5DDbhCeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کانال ۱۴ اسرائیل:
انتظار می‌رود نخست‌وزیر اسرائیل(نتانیاهو)هفته آینده برای دیدار با رئیس‌جمهور ترامپ — که هشتمین دیدار آن‌ها از زمان بازگشت وی به قدرت خواهد بود — راهی واشنگتن شود؛ دیداری که در آن برنامه هسته‌ای ایران و خرید احتمالی جنگنده‌های اف-۳۵ توسط ترکیه در صدر دستور کار قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67359" target="_blank">📅 01:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67358">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6d2fa6e6a.mp4?token=jWJ6SorMn5Zr-SwtbwPjVbeY6MCOlB95OLobrHAb-5YH4ZW8z5ekY3k5vPzJEBt37wbmcPoPgmTG2c-CzE24705AeS75jyInVyrEmCa_w1uHxuqZ3oqE6WS3x_3_ok0yqTCbcsHLBVMKHZ6GB5QVtQrTtzRWPuhh6q82VBmDpl2rQWSYRzEqStcj646jAFjHGGVJ7H2VbIIkhKNEJN8a0VTnsRZI-3uccJuuMR2Qg6y4_kuukABofHwzk1A1diOJiCUi9N3m5vQbJZVw3soUPa1FEaHDMSgkcj4wo0jGmBiFS_iaBYLQu-XPCJnDrYBU9g3N_KEz24PyQKLQdBq2dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6d2fa6e6a.mp4?token=jWJ6SorMn5Zr-SwtbwPjVbeY6MCOlB95OLobrHAb-5YH4ZW8z5ekY3k5vPzJEBt37wbmcPoPgmTG2c-CzE24705AeS75jyInVyrEmCa_w1uHxuqZ3oqE6WS3x_3_ok0yqTCbcsHLBVMKHZ6GB5QVtQrTtzRWPuhh6q82VBmDpl2rQWSYRzEqStcj646jAFjHGGVJ7H2VbIIkhKNEJN8a0VTnsRZI-3uccJuuMR2Qg6y4_kuukABofHwzk1A1diOJiCUi9N3m5vQbJZVw3soUPa1FEaHDMSgkcj4wo0jGmBiFS_iaBYLQu-XPCJnDrYBU9g3N_KEz24PyQKLQdBq2dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو ای که فرستادن به صداوسیما از لحظه حمله به خونه نتانیاهو و ترامپ و گرفتن انتقام علی خامنه‌ای
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67358" target="_blank">📅 00:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67357">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/237c10defa.mp4?token=AlsN1BKTid6YKlGhg_i7FbS9ltXuECCvw9grH_o5rIKpR92RfRG_n3MjCBZxQeuf3ivOJcUe93e_wXcp4dFPrEPtesE6582qMmBh1imaD7eNyqIL1fXWAzUETVJJvIDGNu6JBMRaXP0hpmkwGgT30u-hH-GfsVfYy2VSkCWQp1PdPKaIZl3FfxIPpgfH8Xxu0zrQSsP3u3x7Zpo_wOc5X-UT1l_FyXq55otUMEAgrg653hvoMrcZD6L8KuGS_Gig-SBWvGsRJjo_5epeQW-VvoQQHmPGBJXuwYW2326Z1gww8ROt5NLOjfkXMVMtvbASx4KgC3ZhG9l8p3mQ5bdUGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/237c10defa.mp4?token=AlsN1BKTid6YKlGhg_i7FbS9ltXuECCvw9grH_o5rIKpR92RfRG_n3MjCBZxQeuf3ivOJcUe93e_wXcp4dFPrEPtesE6582qMmBh1imaD7eNyqIL1fXWAzUETVJJvIDGNu6JBMRaXP0hpmkwGgT30u-hH-GfsVfYy2VSkCWQp1PdPKaIZl3FfxIPpgfH8Xxu0zrQSsP3u3x7Zpo_wOc5X-UT1l_FyXq55otUMEAgrg653hvoMrcZD6L8KuGS_Gig-SBWvGsRJjo_5epeQW-VvoQQHmPGBJXuwYW2326Z1gww8ROt5NLOjfkXMVMtvbASx4KgC3ZhG9l8p3mQ5bdUGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پهپاد اوکراینی یه سرباز روس ـ افریقایی رو تو یه مزرعه تو شرق اوکراین بدون شلوار حین دسشویی کردن گیر اورده و افتاده دنبالش
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67357" target="_blank">📅 23:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67356">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhJBO20txXNK-eJMxl80OtCM6OkOkmy1I5mIrlYyCNMLXudaDRCgz6kruFnNLrWuypjbI8HOSlwOMeQ3333R86WLA9sXAnxmxG0h5ZHymNV6iiP59HkHPv8b7S09CWB1qKZ6P8ysTOhezXL4PAml1QXgr639F4Rjiq71cJYkmCSakrtSSbRs8N_Dlem9S0_4UrRY5tZdxhOHxt1QJOpe--UBEraHOCLW4y93CUL-g2GxgCoQ6AjUoYood3H0qBbIJBcwdTyEKZRrWqTjiDUm52ou83HnGk6shSZkygK2p34opp8IgVVyiK6yXvtuhNchO0bU6XUDC_pwbZVU_z9q2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سنتکام:
یک چترباز ارتش ایالات متحده اعزام به خاورمیانه، آموزش تیراندازی انجام می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67356" target="_blank">📅 23:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67355">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb140a8f9.mp4?token=Js9yI2rJH0o_b3MXy2BsbAIiVtZHlr9fbRCoZpItnBG_l8d4xwKDO4dZ6jrs3cU5vWiZBYeheIr9zzyNcxNVg7oHDP13fGwifHJOh1ysLxAIMzFYd8hG8Cg1TPaEIvh3yL1ofpH7WDGFtnPoBXMnXqMZqcePW5Mt1BpScR6j-Y_LMrbG9PBhHy0za5ni_BPe2hsCZqriBEzLIrx6yIyYKBwhwA3wonrEb0g0OE4OSGeW7KZzNwHwPrQ66W-Z6wfgIwWVKhqhqAeEzU4QPu9PEKmFMwxql2J_rgeFjs3Zyd0Z0ImzP0EkVTHd8Mbel_jIxsVHeGgpGvffdioXWAtO5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb140a8f9.mp4?token=Js9yI2rJH0o_b3MXy2BsbAIiVtZHlr9fbRCoZpItnBG_l8d4xwKDO4dZ6jrs3cU5vWiZBYeheIr9zzyNcxNVg7oHDP13fGwifHJOh1ysLxAIMzFYd8hG8Cg1TPaEIvh3yL1ofpH7WDGFtnPoBXMnXqMZqcePW5Mt1BpScR6j-Y_LMrbG9PBhHy0za5ni_BPe2hsCZqriBEzLIrx6yIyYKBwhwA3wonrEb0g0OE4OSGeW7KZzNwHwPrQ66W-Z6wfgIwWVKhqhqAeEzU4QPu9PEKmFMwxql2J_rgeFjs3Zyd0Z0ImzP0EkVTHd8Mbel_jIxsVHeGgpGvffdioXWAtO5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خایه کنین؛ توی اردبیل چند تا آقا نشستن با یه خرس نون و پنیر میخورن
🗿
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67355" target="_blank">📅 22:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67353">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AkU0dNc-yWf0fHB26KWF1oDP8sJMsSKcnmZ0BTxutwW_Ou9g-auz1-J0oa-eHrP23ndQ6J6fxZEAqc-a7nRQjloWknmQEw9Ls4VeObLOmDpA_TJCWtXjSyegZ8cqTG_IcE73ifnaovtFj-QgVD-lV-_ZWxqBQmCf__g2RX8tdxkBPIqz4Yq-OdivF8QEym6R3HFRXHCcqgkH-y7SqKwPQkyYq8j-crRAYGUEgPO4nC2xmO0W4oN4_nPs7I8jc_GHZRTHQDoyQOmd4_pf7BQnIn25oSN3Waf1wuVGy-xfoYTkrKW0PX_za1xKQaVu58qAc0jktLjf4sExkrK8_K3HwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسرائیل به فارسی:
مثل اینکه مجتبی هم بوده
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67353" target="_blank">📅 22:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67352">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc47a54d3f.mp4?token=tuArcdsdB7t7gTc-O2AD9A9lzfZjwvlqZr_zwHmsb1xLw71nBwdn4gNHQnNayHXfORlk8C9eKzAEJ8bcuGOhlEiKDoRaHltAJLYqFvfe1JMZRkJg9jhmgOUeBAkZfuSB_ejNQ9b7ZQtBAOWfzvcwTtpTmO0XGIrSJeKIHZtMlrFhjgi1JuuSbvjQ_Wei95AswwXvlkng63qZCgzqsqoOsIOlzS_FlYPRjBJD4JLZRQf9nTzsMzP9qSovJkKJW9XVV8U68kEyBBHlBHRSpz_cwthyYvGb2NwvNTR55uPMl9W86UwZgO-JI6dChdYJzds4bh8DiG0WEVS2XCZdZgWZJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc47a54d3f.mp4?token=tuArcdsdB7t7gTc-O2AD9A9lzfZjwvlqZr_zwHmsb1xLw71nBwdn4gNHQnNayHXfORlk8C9eKzAEJ8bcuGOhlEiKDoRaHltAJLYqFvfe1JMZRkJg9jhmgOUeBAkZfuSB_ejNQ9b7ZQtBAOWfzvcwTtpTmO0XGIrSJeKIHZtMlrFhjgi1JuuSbvjQ_Wei95AswwXvlkng63qZCgzqsqoOsIOlzS_FlYPRjBJD4JLZRQf9nTzsMzP9qSovJkKJW9XVV8U68kEyBBHlBHRSpz_cwthyYvGb2NwvNTR55uPMl9W86UwZgO-JI6dChdYJzds4bh8DiG0WEVS2XCZdZgWZJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمزه صفوی :
یکی از گرون‌ترین سیستم‌های حفاظت در بین رهبران جهان مربوط به علی خامنه‌ای بود، اما نتونستیم اونو حفاظت و پنهان کنیم و از دستش دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67352" target="_blank">📅 21:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67351">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
ترامپ:  از فیفا برای انجام کار درست و جبران یک بی‌عدالتی بزرگ سپاسگزارم!  @News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67351" target="_blank">📅 21:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67350">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obf9JaJGHQ4m9bN2JAeDjK1Eo9P_86JBQn7MlAcYpcRYtdoBwNovuKRIX4dk3GYI72fIlglaMxSaqYIgNo0AjzT2Qnkzcm9Hc6AOzfFefITtKTpN6pOMQ9aXep4b5_Y8QvLV6ADQJG5ZylgKaYfnixn8y5BZJiB13TwXBCxCDIsLot2SqPerV24118IlHnpWFkHqzQzjbtZ3Lq6EfSe_ACUoUpP665FiLDI4yRUCwBYJqIZ_RPDQ2Z68NZw_WxNxdPiySYwSpEThgX7siPR4W4sS8IkF0Y_LvPYvIAjEtxCsO9coXl6oxy0pgDETcIU92oODTj9cq0UaTAIZmkrgYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ:
از فیفا برای انجام کار درست و جبران یک بی‌عدالتی بزرگ سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67350" target="_blank">📅 21:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67349">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d12e972bb.mp4?token=Ooh3yFt3X3f_7PcEZTRxbzNHfUILqxAJsAYpDG3QabT37qhKupFb8tYCqF5qMP9IcLtsayHbOfHDzZ9OYM92vVDSTXClv8-VpGBD2-RSdN3FoJ8j4i-UDrygmRD_qRHbYO7PSerNftSbsL0U3nz6oKz4VedfHahcEOCgZHuSsjbC7qGVyg86kFGwuiEklaVlu5t5ihr-PC3HppXqjNr-GVjVNeA5Thu6t1gmbYqrFTcdKgJAcx7awopHVOtzldgwb6iwi80a9Xt4ytE2ElbIA37k3MThIKsKWjGGE6BD25YJzMINpZ942CIrqtXB3vWQVJFM6h6nHxDTpFYT8eGOXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d12e972bb.mp4?token=Ooh3yFt3X3f_7PcEZTRxbzNHfUILqxAJsAYpDG3QabT37qhKupFb8tYCqF5qMP9IcLtsayHbOfHDzZ9OYM92vVDSTXClv8-VpGBD2-RSdN3FoJ8j4i-UDrygmRD_qRHbYO7PSerNftSbsL0U3nz6oKz4VedfHahcEOCgZHuSsjbC7qGVyg86kFGwuiEklaVlu5t5ihr-PC3HppXqjNr-GVjVNeA5Thu6t1gmbYqrFTcdKgJAcx7awopHVOtzldgwb6iwi80a9Xt4ytE2ElbIA37k3MThIKsKWjGGE6BD25YJzMINpZ942CIrqtXB3vWQVJFM6h6nHxDTpFYT8eGOXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمد مخبر مشاور علی خامنه‌ای:
قاتلان امام شهید به مرگ طبیعی نخواهند مرد و نظام آنها را به قتل خواهد رساند.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67349" target="_blank">📅 20:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67348">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5503b743a2.mp4?token=e9QNADRIU7DvGH08h80HsGcb85GAmeoEz9Z7feq08wY6qyvgCKQCOV0j3I0PaiXfQJ4pcMGed0cXicLo0mmG_-Vo3MAgvhBS_FPaOGx0wsnovHINPTcoq20ZB1-Rnpr3BaLZNEsqQ197aZGVkTgDzo9VYs9W_R4-XqYxGzVDCtIbWKQA4kN2pq4Q2IXPaJivXaSIElUW-iYupXWc6uj41GEK3Koli20jz-6pLH3AEa4oc0ceDyDg3FmLrXpGqywDjcvhus6lQIc5uvkqGLYRGU97WzW-W72o_Ho931cVyxQuSOHXdLfrYyux0b2SqPME_e_skR4OMj6I9kimLBCuaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5503b743a2.mp4?token=e9QNADRIU7DvGH08h80HsGcb85GAmeoEz9Z7feq08wY6qyvgCKQCOV0j3I0PaiXfQJ4pcMGed0cXicLo0mmG_-Vo3MAgvhBS_FPaOGx0wsnovHINPTcoq20ZB1-Rnpr3BaLZNEsqQ197aZGVkTgDzo9VYs9W_R4-XqYxGzVDCtIbWKQA4kN2pq4Q2IXPaJivXaSIElUW-iYupXWc6uj41GEK3Koli20jz-6pLH3AEa4oc0ceDyDg3FmLrXpGqywDjcvhus6lQIc5uvkqGLYRGU97WzW-W72o_Ho931cVyxQuSOHXdLfrYyux0b2SqPME_e_skR4OMj6I9kimLBCuaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
قول میدم راه امام شهید رو ادامه بدم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67348" target="_blank">📅 20:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67345">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ET0K2pTvdh2_72WDOvTMmVIQGr4NKss1hbEDBygUEnd7fwWOcbY16NE3-B-uLbvnp5UMno9nDK7zbckoaZSVRaAj3kb5KXAbwcqh3enbf26VhBqw1VUHjKoebq5sf0QT37Gp5O23e1fWcVBrY6aR74SHwPtoqx0xVCfay94FGNClqRjgor0lRACom3N-y44mDn0y8CqBNk_MZqD4ptRgUfSVXhyEUtx06q3BtlyWS-OnjHzizG-zHqdr5DgImhQ8AyxjkIVTRZJV10j1zv32-Z8ZQWzZB5oWeoDdiXYZ5l8ypMsu2zVUZkAJHv1LnI6rI6AJT7-xKe8IC7XLl2wu1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u5djCapQrqonqHvkxK29FL85i-gIXhM_oate_qaOnlakFBsyYkE4Pr011yKxUdxGV3wKv7YUlue-3AN_Jq_tPdr9Mh1IWf810dCl8fmOSYBJxuFCtuxBt7_yvoO3dF_hK-Rhj5komyD-MrpXeFBRi4qkT5pW2pD_nDTDIBC6CNd3CntziyOZDBQ9mazCQ2rYefdWL2xlrX-KU-1jBVOZicvqlfus_dkGeKqVNfBhAulA7ejOqM3A8_kGTuM3btglAGKu97QfNDDN6BS0E_ch0pWHJVAMedBkEPGGOI-FJU1zHDw9bAXbfxLfDqZ5okanLb5eTxNpPX0Jj5atrkAPmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a975887416.mp4?token=T_rJ3vF-o89IUehsLlyxRQzuMsyASEeG_kTW6g1La28N8B141AI4lSLQ-xtL4EjpQSzxcukHu-MuXe4qkLFdF-p3-dJ_MhMJlHRLo_Pzz494M-r52vzJ0Dps7rrwZK21A51HpV5nAKTsUhg5KVONyHVMXjiwjNJxyxUmyvt5PZk93G7b1yU69Hrf5Ss-QYl5bdcSuIxHpu0J93ixEjwNBupbZPwPw6Yh7gdlYC4hTWvhY3iNnq7Fu5wmPW4Hx9Hxb0WZy6xSDwsieI_c4MW0jAr5K38D58vdygj5X44WqYH8E9Pb_VKNmYm3zHIKiz5eQ5SypKvRFfuf5zqlAue_fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a975887416.mp4?token=T_rJ3vF-o89IUehsLlyxRQzuMsyASEeG_kTW6g1La28N8B141AI4lSLQ-xtL4EjpQSzxcukHu-MuXe4qkLFdF-p3-dJ_MhMJlHRLo_Pzz494M-r52vzJ0Dps7rrwZK21A51HpV5nAKTsUhg5KVONyHVMXjiwjNJxyxUmyvt5PZk93G7b1yU69Hrf5Ss-QYl5bdcSuIxHpu0J93ixEjwNBupbZPwPw6Yh7gdlYC4hTWvhY3iNnq7Fu5wmPW4Hx9Hxb0WZy6xSDwsieI_c4MW0jAr5K38D58vdygj5X44WqYH8E9Pb_VKNmYm3zHIKiz5eQ5SypKvRFfuf5zqlAue_fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
حملات ارتش اسرائیل به نبطیه الفوقا در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67345" target="_blank">📅 19:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67344">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af4c05c580.mp4?token=Qq_d8uXwz73zftBg8SdynQiFCRHRpwtPiXl3yOWmRByILy75g921WZe_XMz7nH7JK1tPfiiF9-d8p2RJaJm9-RO9GafSptKG_RMSlQF9QIYnvsJ2zDUBKU_VpSbQAnvlqrWVBhEKWpgkcFVUsXItWo8TNw4QBo5mGuR3UQ1EL_-OVRzQRvL1cMzl66VlfvUglJ-wn7TSLVf3OdmREV-WG0r0dhRuB10cDG05mnVLHdKuJQXYz7EIviYyJEbgMOJWDz6bFwpQE72X7hnZz2MHyQROBOW1-LQ4m6u9HbQ5DGyJWkiBPNtRjTM1tS4SdLREWVXdJbUCI5El0ynhr3QX6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af4c05c580.mp4?token=Qq_d8uXwz73zftBg8SdynQiFCRHRpwtPiXl3yOWmRByILy75g921WZe_XMz7nH7JK1tPfiiF9-d8p2RJaJm9-RO9GafSptKG_RMSlQF9QIYnvsJ2zDUBKU_VpSbQAnvlqrWVBhEKWpgkcFVUsXItWo8TNw4QBo5mGuR3UQ1EL_-OVRzQRvL1cMzl66VlfvUglJ-wn7TSLVf3OdmREV-WG0r0dhRuB10cDG05mnVLHdKuJQXYz7EIviYyJEbgMOJWDz6bFwpQE72X7hnZz2MHyQROBOW1-LQ4m6u9HbQ5DGyJWkiBPNtRjTM1tS4SdLREWVXdJbUCI5El0ynhr3QX6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
ما در وضعیت دائمی جنگ نیستیم.
من خودم، به همراه رئیس‌جمهور ترامپ، چهار توافق صلح را به پیش بردیم.
تنها مسیحیان لبنان نیستند که از ما درخواست حفاظت می‌کنند.
دروزی‌ها هستند، مسلمانان هستند، مسلمانان سنی هستند و حتی تعدادی از مسلمانان شیعه نیز همین‌طور.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67344" target="_blank">📅 19:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67343">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a4244b191.mp4?token=Ot2xX3Qe0BVcSm3Az5FkyAu3m6lAjOfz06-scvX6KmyucukzOpqLRMRLcDO37CH8FZhd67muR13c3JNW2ixjYQdz-_6fOzCNZpQOd5eWqSKr26GuHTh86ZhtNR1c5Nx544Q3OwLoSdo7ra5_qRbYkIr7kTkQV4kXuqHFrEPQZE2ANegKhaSFG8fqOn2j9ld9n2n51GWQ2CPphUH_VJ61hqjZ5v8g9nB_gqvPPOvKs0-pX9RgMzaeVmsQJyL6Wf2I_2EXY0rwXW-bR5Beq_fIlInDf1zRiw2L8CUGOL3eCPW16mDFLIHOCLve_tQp8zjOrhjgJ_9Y_MuDmEjrDW_B4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a4244b191.mp4?token=Ot2xX3Qe0BVcSm3Az5FkyAu3m6lAjOfz06-scvX6KmyucukzOpqLRMRLcDO37CH8FZhd67muR13c3JNW2ixjYQdz-_6fOzCNZpQOd5eWqSKr26GuHTh86ZhtNR1c5Nx544Q3OwLoSdo7ra5_qRbYkIr7kTkQV4kXuqHFrEPQZE2ANegKhaSFG8fqOn2j9ld9n2n51GWQ2CPphUH_VJ61hqjZ5v8g9nB_gqvPPOvKs0-pX9RgMzaeVmsQJyL6Wf2I_2EXY0rwXW-bR5Beq_fIlInDf1zRiw2L8CUGOL3eCPW16mDFLIHOCLve_tQp8zjOrhjgJ_9Y_MuDmEjrDW_B4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
روستاهای مسیحی در لبنان...
برخی از آن‌ها در واقع درخواست الحاق به اسرائیل را داده‌اند زیرا ما آن‌ها را در برابر حزب‌الله محافظت می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67343" target="_blank">📅 19:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67341">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd048f948.mp4?token=D8fJOmLLB0pEBLT56F_y9qQVLZwGRXwbNlzmxzmHkXpRHfV05zrBrlCPrNtxp4bMjSfdvSqWWVpAfjMEIyttB3F83-ERuJQkSSbyJq9Qk_-DqfDaXqCPZViR0iOrKt_fZ9BTzbjPPuDqEzSyY7XX8GGzrPbEvr8yc0C2FY0YN4e4eF8D1Prb2XzlcEoE9SK48TwU7lAL4bj8PHjtxiRiSrvBezrjOC1Y-pvpayvy1S8FtU66An4V2HdjvJ3hZgEj1c8eeNnxE1-5QXeJAdHH6e_n0NzCKEqpTNQAPBqGb-sZ2aFfdUHamkFRig62RJhnfFOkVTvYqVNMcWtK7uct3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd048f948.mp4?token=D8fJOmLLB0pEBLT56F_y9qQVLZwGRXwbNlzmxzmHkXpRHfV05zrBrlCPrNtxp4bMjSfdvSqWWVpAfjMEIyttB3F83-ERuJQkSSbyJq9Qk_-DqfDaXqCPZViR0iOrKt_fZ9BTzbjPPuDqEzSyY7XX8GGzrPbEvr8yc0C2FY0YN4e4eF8D1Prb2XzlcEoE9SK48TwU7lAL4bj8PHjtxiRiSrvBezrjOC1Y-pvpayvy1S8FtU66An4V2HdjvJ3hZgEj1c8eeNnxE1-5QXeJAdHH6e_n0NzCKEqpTNQAPBqGb-sZ2aFfdUHamkFRig62RJhnfFOkVTvYqVNMcWtK7uct3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار تسنیم : نظرتون درباره رهبری مجتبی چیه؟
🔴
زن عرزشی : چی بگم؟! نمی‌دونم ما که همه منتظر بودیم مجتبی حداقل برای تشییع جنازه پدرش بیاد و حضوری باهامون صحبت کنه، ولی بازم نیومد!
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67341" target="_blank">📅 18:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67340">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c05464482.mp4?token=DfRMw0dHMvD-N6phX6M1xUAUIvp6kcTrxaB5xYOMeNLcAU1_HGQ8_qWOPzJd3_XKaFxBZMLyOExf64sYYqkxHbLka9cCFi-_s91Lcb7ttrBAzXmuH2Lh8VJfhnoTabDiUgNy16ITTrU-F7UlaLldLeqa0S_xaOAliR0XDuRgNvtoPfLO8-PEDs5OYLk_AMifA9o1LM0LaeSiqZZmRKKmmicQlquKI5SlK3W5DjeeljYEvrrPXv9c4IEvXDn55hD61AEq8cW42KQPbEUm41qZPrUZqadiwPPPCw0Xk4swcOLvlmHNFtkg0hUFhTTOvHbfQhS4jR6lfoCeyaxWGwxPPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c05464482.mp4?token=DfRMw0dHMvD-N6phX6M1xUAUIvp6kcTrxaB5xYOMeNLcAU1_HGQ8_qWOPzJd3_XKaFxBZMLyOExf64sYYqkxHbLka9cCFi-_s91Lcb7ttrBAzXmuH2Lh8VJfhnoTabDiUgNy16ITTrU-F7UlaLldLeqa0S_xaOAliR0XDuRgNvtoPfLO8-PEDs5OYLk_AMifA9o1LM0LaeSiqZZmRKKmmicQlquKI5SlK3W5DjeeljYEvrrPXv9c4IEvXDn55hD61AEq8cW42KQPbEUm41qZPrUZqadiwPPPCw0Xk4swcOLvlmHNFtkg0hUFhTTOvHbfQhS4jR6lfoCeyaxWGwxPPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زینب سلیمانی:
شهادت آقا برای ما سنگین‌تر از شهادت حاج قاسم بود
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67340" target="_blank">📅 18:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67339">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQXjc8QzcIEGBTRcDhFaKnltlqnJpinE4fnJ15sPTzsP5xYf8KiEOi1BIpwlmk_y-nCYOr2yWPNISu9VPIA5eMGkqJOuNQhzSBN4cvj8tvF3i8rhV85haGw85v30_utDozbPXg5GsrkElUIaLHq1DZM5gJLcjKLVVUDv1zpBg1jXwn07aJIt5UkwU1UoRo4K69aL5L1fjsOzVeG75MSowivGC_drcQxtXlL9ubI5tY3WNcQjMyUS9QfhJPN9Eck471qZ3DC3G_ujepozgSt7EouYeGCmZOrUGxbtr2SZxlfpOyQ1DLWuiWFVQlXhbAB0AVDf1AC_iwLV2-kot_voyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دفتر شاهزاده رضا پهلوی:
🔴
‏تلویزیون بی‌بی‌سی فارسی در صفحات رسمی خود، با انتشار بخش‌هایی تقطیع‌شده از گفت‌وگوی شاهزاده رضا پهلوی، تصویری نادرست و گمراه‌کننده از اظهارات ایشان ارائه کرده است. تیتر و متن این پست، با اتکا به نقل‌قول‌هایی ناقص که پیش‌تر نیز توسط رسانه‌ها و حساب‌های وابسته به جمهوری اسلامی برای تحریف سخنان ایشان بازنشر شده بود، به‌گونه‌ای تنظیم شده که به مخاطب این برداشت نادرست را القا می‌کند که شاهزاده رضا پهلوی آغاز جنگ یا تصمیم به حمله را به سفر خود به اسرائیل نسبت داده‌اند. برداشتی که هیچ نسبتی با محتوای کامل گفت‌وگو ندارد.
🔴
آنچه شاهزاده رضا پهلوی تصریح کرده‌اند، این است که سفر ایشان به اسرائیل، در کنار تلاش‌های گسترده میلیون‌ها ایرانی، به روشن‌تر شدن این واقعیت برای افکار عمومی جهان کمک کرد که مردم ایران دشمن جهان آزاد نیستند، و از این رو دنیا در برخورد با جمهوری اسلامی باید حساب مردم ایران را از این رژیم جدا کند. اینکه مسئول اصلی بحران، جنگ و بی‌ثباتی در ایران و منطقه، جمهوری اسلامی است. ایشان همچنین بارها تأکید کرده‌اند که هدفشان پیروزی مبارزه ملت ایران با کمترین هزینه انسانی ممکن است. چنان‌که در همین گفت‌وگو نیز تصریح کردند: «تمام هدف من این است که این مبارزه با کمترین تلفات جانی به نتیجه برسد… هر انسانی که جانش را از دست بدهد برای من واقعاً دردناک است.»
🔴
این‌گونه رفتارهای غیرحرفه‌ای و تحریف‌های آشکار از سوی بی‌بی‌سی فارسی در حالی صورت می‌گیرد که چندی پیش، مدیرعامل کل بنگاه رسانه‌ای بی‌بی‌سی و رئیس بخش خبر این سازمان به دلیل رسواییِ دستکاری، جرح‌وتعدیل و ادیت مغرضانه سخنان و مصاحبه‌ها ناچار به استعفا شدند. از رسانه‌ای که هزینه آن از مالیات شهروندان بریتانیایی تأمین می‌شود و با وجود ادعای راستی‌آزمایی، به دلیل نقض مکرر استانداردهای بی‌طرفی با بحران جدی اعتبار مواجه است، انتظار می‌رود فوراً نسبت به اصلاح این گزارش مغرضانه اقدام کرده و سخنان شاهزاده رضا پهلوی را به طور دقیق و امانت‌دارانه منعکس نماید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67339" target="_blank">📅 17:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67338">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d7e9ec8c8.mp4?token=WvxTibZcDqfxR3lAWHv_463Rx_tugxn3aWhG4Iz2gYMzqrHWN-XpbhdRfh3roEuCKFtOJcTrkKaa2Mjgnw-z0MyKrldpIU88-eqJIquSrKMMzjirdI_SXunrG5IyTqpzCK92abzMqjwVKFfCBODGrcdvQ69kdvBsk7idp7qHGoy9zkZkPJm8BCSehO2GvV5D9aPoRaXJUTqGOqgpsPlIPRk7bmkeF7JHmF2Rsku1MKUlC6UEm3YQlYk3C2Ox-AeyJYHk68jIeCsjdc6jN_R8mw8EiES8ZboSG6J2lOkfj05o72nWB3emx97lq9-qCBgAIlKQB23uk5JivzIImQWCGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d7e9ec8c8.mp4?token=WvxTibZcDqfxR3lAWHv_463Rx_tugxn3aWhG4Iz2gYMzqrHWN-XpbhdRfh3roEuCKFtOJcTrkKaa2Mjgnw-z0MyKrldpIU88-eqJIquSrKMMzjirdI_SXunrG5IyTqpzCK92abzMqjwVKFfCBODGrcdvQ69kdvBsk7idp7qHGoy9zkZkPJm8BCSehO2GvV5D9aPoRaXJUTqGOqgpsPlIPRk7bmkeF7JHmF2Rsku1MKUlC6UEm3YQlYk3C2Ox-AeyJYHk68jIeCsjdc6jN_R8mw8EiES8ZboSG6J2lOkfj05o72nWB3emx97lq9-qCBgAIlKQB23uk5JivzIImQWCGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بزرگترین آتش بازی تاریخ آمریکا در واشنگتن دی سی به مناسبت ۴ جولای روز استقلال آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67338" target="_blank">📅 17:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67337">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yf1eXgRl9T6Fj46BbfoOfa_M-8ZB4ymQS603qTWiwkXTxMVIXl2T9shYqu0Edb6y8pd2Ta9Pqf9iuFYOCGPKQiTcP3Q9wA48DILsdhyOSqamdjvdhb0_ErDl6KjBIphf9mptXFAMSR9mpmZ9eyj6RrFrJ51Gqjm_DHedRbPGalcnGR-tgfKW0yryAX_dnC2u-bGiHn_xHruYuR0i_DjA_liZkG3Z_wBy1hkLpXWOoxtpEvmHoVcvqostL_txCw1BN_1AWLjhsh0k1ALaddDLjjWf3y8sRNjJFA4SD1pmDtjWspalImxZwKi74d6iF0QDb26rsk42PFhCewYzFwYbcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
❌
دیوید کیس مشاور و سخنگوی پیشین نخست‌وزیر اسرائیل:
تنها دلیلی که ما امروز تشییع جنازه خامنه‌ای را بمباران نکردیم آن است که 10 هزار مأمور موساد در میان آنان داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67337" target="_blank">📅 16:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67336">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e644784ac.mp4?token=PZqy86jLwGrKmKVmvBjfh3XJ0-y0o27UPCxHZhQMZfWB3TDa64fhU7kYPmA6XHr9W3x-Jtf-eleEu6pDwyMmOz5Ld7PVVkApJYbTsE9j-LX8IS7wQt8zV6PDerJETJyyzycNT5vICB6BHcivxEoBoBWyu0KYkrTX7itA4I0vi6oOa_0daWpPq1zXCo7ojjmy_qv36WPTeSGfTqFSaP8XjN8RQCeKdSQGP3snMGkuE2Mn0lhCuXgqVG4nTAUsBA9KXki8Lgr8weMMJEOdCclNf4xQjsCG-eXPkP6EnOF-QB1PXPuSL2gtBmHUT2u9AKOo9OV_0foBAW4sBY4pmILc0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e644784ac.mp4?token=PZqy86jLwGrKmKVmvBjfh3XJ0-y0o27UPCxHZhQMZfWB3TDa64fhU7kYPmA6XHr9W3x-Jtf-eleEu6pDwyMmOz5Ld7PVVkApJYbTsE9j-LX8IS7wQt8zV6PDerJETJyyzycNT5vICB6BHcivxEoBoBWyu0KYkrTX7itA4I0vi6oOa_0daWpPq1zXCo7ojjmy_qv36WPTeSGfTqFSaP8XjN8RQCeKdSQGP3snMGkuE2Mn0lhCuXgqVG4nTAUsBA9KXki8Lgr8weMMJEOdCclNf4xQjsCG-eXPkP6EnOF-QB1PXPuSL2gtBmHUT2u9AKOo9OV_0foBAW4sBY4pmILc0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اگه اهل دعواهای خیابونی هستی، این ویدیو از استاد طِقه زنی رو تا آخر ببین تا به امید خدا پیروز میدان نبرد بشی؛
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67336" target="_blank">📅 16:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67335">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/67335" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67335" target="_blank">📅 16:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67334">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67334" target="_blank">📅 16:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67333">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YRg0SnM4-rCfMUW_gM8YamiTOzhCTJYEM9f9-GK1aVgl6NWo6aFJQZnKq3dBuxzZbAUd_sL2Hb1WcGZVTSViZVMpAN9Nmm5scQ6cXNf4ujZHiq2tL3DKPUzUmc0H4NGWpj-0WEXNpo1gEF2M0bYHptS46sL7882SycJ6ADpbpKDjxn_gij7Am216DH1sTzGefjhnHI96i7MJNtxTpQ0YT0bQ8jqWOWC4JX9hPfL_RBCdbgbIUvAwU6eWb8pi502CRi8taEZwwkeHCltFxGOUQAl4sfTcNbB7V3a1ANNUXwy7DnognZ8UxRSAKuGvaiC8pNzBfpmVkIk4jwdiwuxBrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گویا کامیون حمل جنازه علی خامنه‌ای مبلغ2,298,000 هزار تومان خلافی داره
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67333" target="_blank">📅 16:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67332">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMYNK9bInSA4NLTPeO1EgqtxEo9ElyvXbH4fVO1m4s45YPCRlPBCdoecNAjBPu5500oHBp2C8wRatg5BcR25-RkzRguCL_eLyQDXzTqZVQjgbyGRIDWOfxrs1Gbt-g9a0x55PhdYgXhbD6d_5f5jXm2HS0W4zdR18sKU4BCIL9zu2f3uUzj2O_dddLvfVtu64A0yOj4fT69h4Th-kgucBtjE5HojUoGjZO3SixVKcUbjL_bkLhckdd9bQzJF3XIhnTW8Z_irujUjpU_CpN0yFMRsIrfPkvrcnYxeLKkgI-N7vwxxNVCTfyS3QRimvakKSGuA7X9N01nOsw2AyhCKYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
محمد اکرمی‌نیا سخنگوی ارتش:
«هرگونه اشتباهی از سوی دشمن، با پاسخ قاطع نیروهای مسلح ایران مواجه خواهد شد. ما بارها اعلام کرده‌ایم که از فرصت آتش‌بس برای ارتقای توانمندی‌های رزمی خود بهره می‌بریم. ما حتی یک لحظه را هم هدر نمی‌دهیم و تمرکز خود را از این مأموریت برنمی‌داریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67332" target="_blank">📅 15:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67331">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو در جلسه دولت:
شنیدم در رسانه‌ها گفته شده که رئیس‌جمهور ترامپ خواسته علیه تونل‌های تروریستی در لبنان اقدامی انجام نشود. این یک افسانه و خبر جعلی است.
او حتی یک کلمه هم در این باره به من نگفت و من هم از او چیزی نپرسیدم. ما بر اساس ملاحظات و تصمیمات خودمان عمل می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67331" target="_blank">📅 15:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67330">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqNyzjDzHeFagBb7XNhcm3IFr6O_IujzC8rs_FWaEqxD1-SuEi6BQ25yrfui9eG9Uk_RBDumMg0HJNQO1bRG9bsYLRtnmcM99dXlJOIbJ-_LewrjjhkcS4wp4XaS0wou6ubcD-T8ToOIl6mIUZTuVv6RPPr1gi_Ez_J2bNj75QSTDdQkbCDe1bcCTdBOpml83U8tgGv_WTmZ36crRcf62BDkuL-7h6h9TORt3LIh8BmHIJ2bLm2VVaDXZJfxUGTvUvnB9YnPDy19iAHXGl0LFNb-TKTROKSTI76LwRs5TIS4tOGNMs75BPI51JwXu509CKVJZtR89M7uZk2EJuwRcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویر ترامپ در مراسم وداع با جنازه علی خامنه‌ای که روش نوشته شده:
خواهیم دید چه می شود
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67330" target="_blank">📅 14:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67329">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5c6NmTwT0f9MnG_y7sJIteIK6KVSC68rHMKbgG7HOB1LNwD4M2q0n0vuXOk7sCa_1opk5rg36O-6z1MZ2qTBhXaVNQF4ai7Lg1dfwARn4Z8gOwi2wrFVhZtyJZ_NZYDlLl7_QObwnyl0O7rulOwTHDKoJyYdBzvjPMERfyRGz7Mnx0eaHffN_LTZyYVbru4G3YnfjtBF7aPM5U7DI6BeAv6gdDlIOa25CQtBGApRuNG9HGMeuFVmCuax5bLtAPg4Y_NDf9oE-mxX9WQtCklSdFI-5dIoYA10k4WL21Ea3c6DHpDk9BKEeRaJd8UTwP4gooCquZQDTbPsOnrw2yesA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسرائیل به فارسی:
بهرام که گور میگرفتی همه عمر
دیدی که چگونه گور بهرام گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67329" target="_blank">📅 14:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67328">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b8ead8806.mp4?token=XYpiDt012Zrfvy2qyHAci29S_wVUj5qq48nOp3QJ7a_RNAhPD75j2F6gG9SGtYgvgipc0dNtl-hqozRkGXoJORPU1cVw2KiAO896bIxc9JI5FJ8jhn_E6gJQQcpoC_7iIuayC2A41hkKLJOXxRgZkBktaJutotC0C0Z3z6rQ7_W-V3kqK_KrAEoZlzZ8dHsCoZlQ2xLdTmq1IkIAdDWnJkPA1OdKvCfn8ScIh3frtHq_4vvCCFlDJLnGOS01R6AZ_lxBVpj1vidic4s7o2reRUTAMjzGF_XsrzDLLh_i5BGqzorCNzKmcl2jsQANDBi-tGIfi1UDbOW18xp6RSLJtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b8ead8806.mp4?token=XYpiDt012Zrfvy2qyHAci29S_wVUj5qq48nOp3QJ7a_RNAhPD75j2F6gG9SGtYgvgipc0dNtl-hqozRkGXoJORPU1cVw2KiAO896bIxc9JI5FJ8jhn_E6gJQQcpoC_7iIuayC2A41hkKLJOXxRgZkBktaJutotC0C0Z3z6rQ7_W-V3kqK_KrAEoZlzZ8dHsCoZlQ2xLdTmq1IkIAdDWnJkPA1OdKvCfn8ScIh3frtHq_4vvCCFlDJLnGOS01R6AZ_lxBVpj1vidic4s7o2reRUTAMjzGF_XsrzDLLh_i5BGqzorCNzKmcl2jsQANDBi-tGIfi1UDbOW18xp6RSLJtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این بزرگوار که قبلا گفته بود بخاطر یه تیکه نون به سگ دادم اومده داره ترامپو تهدید میکنه میگه بیا کوت عبدالله ببین چیکارت میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67328" target="_blank">📅 13:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67327">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
❌
دیوید کیس مشاور و سخنگوی پیشین نخست‌وزیر اسرائیل:
تنها دلیلی که ما امروز تشییع جنازه خامنه‌ای را بمباران نکردیم آن است که 10 هزار مأمور موساد در میان آنان داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67327" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67326">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0be756a04.mp4?token=tC5_30zV7z_0Lfg5PTiJ9qKeIa4eaQbdbwC9NNrSIOG9ARTzK7xhCYlbg7q1pYqhLgTbBx5AgZCBPPkeCgYla-iOSpvzAOfkD5YLvBkkYMe7jmfESZuLnu0HW6AKykkX1wOwmJtUlAyFYwtSOmInhNwX0xj1whUGZGQVqOjY_tGJayI0NlXcI9zGyC6EedtRWYJvksWysNSQhho5aZ37BV3EYl5Nl6kosc1TGkcj_c8aXhwISegB3GUH434WQUKJC-HzOwdQ1a1h84rwZBJUMYcOHpaoCAMYQRaNwJu59kH_2hVd7mMaTuZkqLBYT8t83NsX1Z253It6EquLLNtYLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0be756a04.mp4?token=tC5_30zV7z_0Lfg5PTiJ9qKeIa4eaQbdbwC9NNrSIOG9ARTzK7xhCYlbg7q1pYqhLgTbBx5AgZCBPPkeCgYla-iOSpvzAOfkD5YLvBkkYMe7jmfESZuLnu0HW6AKykkX1wOwmJtUlAyFYwtSOmInhNwX0xj1whUGZGQVqOjY_tGJayI0NlXcI9zGyC6EedtRWYJvksWysNSQhho5aZ37BV3EYl5Nl6kosc1TGkcj_c8aXhwISegB3GUH434WQUKJC-HzOwdQ1a1h84rwZBJUMYcOHpaoCAMYQRaNwJu59kH_2hVd7mMaTuZkqLBYT8t83NsX1Z253It6EquLLNtYLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جمهوری اسلامی پس از ۴۷ سال در مهم‌ترین رژه‌ی خود حتی به‌اندازه‌ی بند پوتین‌های ارتش شاهنشاهی هم نظم نداشت.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67326" target="_blank">📅 12:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67325">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uK9Aqm_ScF5lVDQKbx49u5n1Jv752uyviNOkLsyQHFIeW8o6BCqLszmOZbxU7BLQoRDfbxUjhiDS2l3wRVbjA1dosFuBGte9Rvjlspp00jp65h7qYmkQEQCrLDOzYaYQcbk8gPvRQv4vAImncPCdLND6hy5WiCchGcJKVxhIi3MCgA03xlKiAoeuMfpXUGUTjAWMgVs5HT0EEnNAMCaABlnwioP4GFpv0dah0koEQtKPjFlXBqsBiEuVkG4cae_-ckBt9v4U9Yyi7oFaGFueD_54AapSOwEpGnnihgHQ9jrc68YCpMPF2r12oRpB-yNncywO8LtrqgImuIEsdCN49A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هرمزلتر:
🔴
نیروی دریایی سپاه با استفاده از قایق‌های تندرو، کریدور مورد حمایت آمریکا در تنگه هرمز را به طور کامل متوقف کرده و در نیم روز هیچ شناوری از این مسیر عبور نکرده
🔴
سپاه صبح امروز از طریق بی‌سیم به تمامی کشتی‌ ها هشدار داد و همزمان قایق‌های گشتی نیروهای ویژه را برای اعمال کنترل ایران بر تنگه هرمز مستقر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67325" target="_blank">📅 12:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67323">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQWd9ivcvcoNacivrizosL_4oW0J7dCaFmtzpQm-8lINB6sNy0yF8jXf-nliBun5dtCnFa-IyH8EFq41poFL2ByI8xd6J5nKtsope1WAhJ_QlJFcRnEFH3QQlc5JRttJZOpaH-TnH6Og4gdXRQSkdwxp_aIGXV4oIcN33KpvvML9D4pGRR3lQOAx6MY6RMkn9YlrNLDtrE_5va27WPyZlEyNGj6nDK5AyVo5L3luYGKn4qYvbD5qkdVTz3NMbUKtjLJkU2dA3FMIT7j3KLd4YWnuxRrHOazDWQ7HIRqyWI7_3Wqb7kcu0N8whr7OT9ACLTn8i0pxCHnsBje7rsrmvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f22dc07ca.mp4?token=B6LWHYWK5IIAgy3DGcJaCp4xm6m9nk4ACKkSYvjdHIcBbtpZ_Jv0W_AJxez63vgCAdVPhTfZ6u76GD2ZG1UZDEYpkT5N_uhG1xJJqCED97d32jtOwgTXv_UvtvqKZzVEhU6aj-rvKKpU9kKkmOhlhG54mDlU-EKyGy-gBk_Nfo2nQbJRQZPhKobS1YpHtN3iXeMwtIQDuoa3KTDTVb3UYGgri1T6hOEFq8Oi5GhwPRwPwdA2gAcT7U0urBpXlYi3aIISjIz89oP9bNvpbqc2o1XJAJG65WCKdYIxHxrmet9zzzoy39m5NFvncGj3lxAymlm7Drtt2ayjMyBKjf-dkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f22dc07ca.mp4?token=B6LWHYWK5IIAgy3DGcJaCp4xm6m9nk4ACKkSYvjdHIcBbtpZ_Jv0W_AJxez63vgCAdVPhTfZ6u76GD2ZG1UZDEYpkT5N_uhG1xJJqCED97d32jtOwgTXv_UvtvqKZzVEhU6aj-rvKKpU9kKkmOhlhG54mDlU-EKyGy-gBk_Nfo2nQbJRQZPhKobS1YpHtN3iXeMwtIQDuoa3KTDTVb3UYGgri1T6hOEFq8Oi5GhwPRwPwdA2gAcT7U0urBpXlYi3aIISjIz89oP9bNvpbqc2o1XJAJG65WCKdYIxHxrmet9zzzoy39m5NFvncGj3lxAymlm7Drtt2ayjMyBKjf-dkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
و بعد از چهار ماه همچنان عامل این جنایت و قاتل فرزندان ایران چال نشده و اجازه چال کردنش رو از قاتلش گرفتن!
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67323" target="_blank">📅 11:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67322">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5f6d58549.mp4?token=IMlcRQJNHs4RJNvMZ5-CjkC9yCUfrZ6lZpWP7AnvMZiyY8iRxbTQcrExJl3-8y0O8Vbn4exsiwGg6s2Cd3bwEdFZxoNhtvpe4lNGcXLQqh2gRElt7ydAS_76Rogo2KOgEg1nWOzVh3sLY6-uqOd_gXrbacXlAwThoMJwsayKH06MLRubmgMh4FL8gyHa1O9etq_LhmD-Daw_gNd6gm1-228S9LZ6NjU2ETnAvyLXEhh_U4dtiQZyghWMpDTcmpf-4tbQPgT_SnDvWxT-ULYUrVA9TK0z2w7sxZGBsAy7SfvQmI_eeO-CpQqKfPqFYbyRN6uRc5urIVzcm06l3HWoCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5f6d58549.mp4?token=IMlcRQJNHs4RJNvMZ5-CjkC9yCUfrZ6lZpWP7AnvMZiyY8iRxbTQcrExJl3-8y0O8Vbn4exsiwGg6s2Cd3bwEdFZxoNhtvpe4lNGcXLQqh2gRElt7ydAS_76Rogo2KOgEg1nWOzVh3sLY6-uqOd_gXrbacXlAwThoMJwsayKH06MLRubmgMh4FL8gyHa1O9etq_LhmD-Daw_gNd6gm1-228S9LZ6NjU2ETnAvyLXEhh_U4dtiQZyghWMpDTcmpf-4tbQPgT_SnDvWxT-ULYUrVA9TK0z2w7sxZGBsAy7SfvQmI_eeO-CpQqKfPqFYbyRN6uRc5urIVzcm06l3HWoCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهدی رسولی  مداح بیت رهبری میگه برای خون‌خواهی اومدیم؛
شما هنوز خونخواهی سلیمانی و... رو نگرفتید بعد میخواید اینو بگیرید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67322" target="_blank">📅 11:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67321">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5807c7f54.mp4?token=NqBP-_eha5UUawcpZnVb9oNZK4akzJJYFjbIWuiMTA5Pt-QA6WTebJtmlpU9Vx2dc_9K989j_TeYQDU-elK6qIbH89QhA0RJH8UrXlROmmzygL_IYcyqTHKOuVwSsYRPubVFicxqsrro-rk8ys3M-SVroYsrYRz4boR_tbVTVCdrLm-aqdf-8sAqVuQx6miVXQY2e3xIzWv0RGjsJHI73iySkrj_GWbwOA4XuFz8cJnSqQ3GqezXXJUO4vIoy-MQwBGlOjtMPfHTdYk-xt1AAXC0qvnru775Tw6YN5FGAGO21vmXwrscX2LaQLk-x3YIZIu6fS1QrK8bq4JydWuz1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5807c7f54.mp4?token=NqBP-_eha5UUawcpZnVb9oNZK4akzJJYFjbIWuiMTA5Pt-QA6WTebJtmlpU9Vx2dc_9K989j_TeYQDU-elK6qIbH89QhA0RJH8UrXlROmmzygL_IYcyqTHKOuVwSsYRPubVFicxqsrro-rk8ys3M-SVroYsrYRz4boR_tbVTVCdrLm-aqdf-8sAqVuQx6miVXQY2e3xIzWv0RGjsJHI73iySkrj_GWbwOA4XuFz8cJnSqQ3GqezXXJUO4vIoy-MQwBGlOjtMPfHTdYk-xt1AAXC0qvnru775Tw6YN5FGAGO21vmXwrscX2LaQLk-x3YIZIu6fS1QrK8bq4JydWuz1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف یه 20-30 سالی هست درحال گریه کردنه
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67321" target="_blank">📅 10:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67320">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/810ada8a67.mp4?token=vE8_YGwjxQcTbAHgbcXFUM2EMY5L3PTYHbBT5XwqqGvjlez1A53KUDVfBHk42Fh98sL7WV_t-KXylAP-3jNPeOVbl1okNRTwJ7LVEQzI4_TA1zIO3W5ErzWKbwZkVQ_YPjyz4rl-bvWnsp6tjvryyUesC8Bp4gWIxd8ikE-2ifVUGzWQFkRw2vmvJQWFEWiNUPpm2Y4SyXnu9JDxMmCjG9YveqQ1l0oey12vPpRiRqHZhFLQ4pHPZGjSrV73MZsyK6Qy7-mdM9ID4WNWxBHDa2WTxWl3bZjomp7UDTjacw-lS-9uMXsM7lFeW4QPE5kqJeF5p-LY6yFjNIKg6_8xcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/810ada8a67.mp4?token=vE8_YGwjxQcTbAHgbcXFUM2EMY5L3PTYHbBT5XwqqGvjlez1A53KUDVfBHk42Fh98sL7WV_t-KXylAP-3jNPeOVbl1okNRTwJ7LVEQzI4_TA1zIO3W5ErzWKbwZkVQ_YPjyz4rl-bvWnsp6tjvryyUesC8Bp4gWIxd8ikE-2ifVUGzWQFkRw2vmvJQWFEWiNUPpm2Y4SyXnu9JDxMmCjG9YveqQ1l0oey12vPpRiRqHZhFLQ4pHPZGjSrV73MZsyK6Qy7-mdM9ID4WNWxBHDa2WTxWl3bZjomp7UDTjacw-lS-9uMXsM7lFeW4QPE5kqJeF5p-LY6yFjNIKg6_8xcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در جریان مراسم افتتاحیه مسابقات «فولسوم پرو رودئو» در ایالت کالیفرنیای آمریکا، یک چترباز پس از آنکه پرچم همراهش به درختی گیر کرد، تعادل خود را از دست داد و به شکل خطرناکی روی یک چادر سقوط کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67320" target="_blank">📅 10:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67319">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ca0cec0e0.mp4?token=bMVBzOxQFrlCwGoJ4WBH1c7l0khwcDtUz4OQncdo1kYKlMpNfnFW2-ik8vlr5GPiVAS2toUZbFbQYgNWkfa2yH56shnrZRZKgTal6zz7xJFrK3tTS2vnILWdAhSwyE_k8Kx4p88BfhpY1tunyzHlQhOe6-ixIcdibgEarxbiLseo3386qK26uyilQT3xChBjcut4yQ6UFNcwuG6jmHwZ-df58glm5_Z5yVZ00hkNFSxuNJ18TrpuStbruPYJEkGMY0SdGuV0TErcpnE7GYAS6xWYrmXTsdW5lten2P2qOwJmQNra6QYcepd31GoNSeoLR-JwOXhnoKpq6M1eSVXlng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ca0cec0e0.mp4?token=bMVBzOxQFrlCwGoJ4WBH1c7l0khwcDtUz4OQncdo1kYKlMpNfnFW2-ik8vlr5GPiVAS2toUZbFbQYgNWkfa2yH56shnrZRZKgTal6zz7xJFrK3tTS2vnILWdAhSwyE_k8Kx4p88BfhpY1tunyzHlQhOe6-ixIcdibgEarxbiLseo3386qK26uyilQT3xChBjcut4yQ6UFNcwuG6jmHwZ-df58glm5_Z5yVZ00hkNFSxuNJ18TrpuStbruPYJEkGMY0SdGuV0TErcpnE7GYAS6xWYrmXTsdW5lten2P2qOwJmQNra6QYcepd31GoNSeoLR-JwOXhnoKpq6M1eSVXlng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولین حضور عمومی مصطفی، میثم و مسعود، سه پسر علی خامنه‌ای، در مراسم تشییع او در مصلای تهران.
مجتبی خامنه‌ای، جانشین علی خامنه‌ای، اما همچنان در انظار عمومی ظاهر نشده و در این مراسم غایب بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67319" target="_blank">📅 09:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67318">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd6157bafc.mp4?token=uG_J-ddmDwuvuGYtcnQUTTV-eCmG_nvK1Nig1CgxesoKEnqlPmNe8BCP3hnPpDVyGAUKwQ3MKhBf-W0hG8dM_h29G0sfEfLwgfLT1fQAGyo1OUr74AK-Pi47KsmC7ZOZgP5zPsvbbV3Ccn5xKu_IwBA_Y26_B5LuJBvdhekc722Sf53rJcjAcxd38Xb4IZ8g-YmjCB0IGM_Z_8OGFxvKT89JKnfqh3_a4wxvhwuNR1GrGIkHXf_j9Uwxnp5N7ifibRDSvb88C3cruoKbVGQ5cKX-2yA_pHHRx-q7C_I10rExcZD5-3hWZTGc4aa2KoDWxlKeJCAYGIoRf6mdjZ4dpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd6157bafc.mp4?token=uG_J-ddmDwuvuGYtcnQUTTV-eCmG_nvK1Nig1CgxesoKEnqlPmNe8BCP3hnPpDVyGAUKwQ3MKhBf-W0hG8dM_h29G0sfEfLwgfLT1fQAGyo1OUr74AK-Pi47KsmC7ZOZgP5zPsvbbV3Ccn5xKu_IwBA_Y26_B5LuJBvdhekc722Sf53rJcjAcxd38Xb4IZ8g-YmjCB0IGM_Z_8OGFxvKT89JKnfqh3_a4wxvhwuNR1GrGIkHXf_j9Uwxnp5N7ifibRDSvb88C3cruoKbVGQ5cKX-2yA_pHHRx-q7C_I10rExcZD5-3hWZTGc4aa2KoDWxlKeJCAYGIoRf6mdjZ4dpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زاکانی و برخی از مسئولین تو حاشیه مراسم رفتن چلوکباب خوردن، عرزشیا هم اون بیرون زیر آفتاب، صف وایسادن تا تخم مرغ آب پز بخورن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67318" target="_blank">📅 09:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67317">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/itNGPJl3X8BtJjIBztNBorQ-0swGTqpYnitXuq3fMgWJV3AnOiDLMF0fzPsoGGp3XBKSD0AjFmmP7v4VN55hTqH118sbSU1gcr5RLpCMJcA4-poZs066ajlw_Cz1-N8mVJt7C9Wd81S-3erCofu5jvgcIEq0MkrzbVWLtFIrYpGfgeKRLFvaVyDBDNpFXINTJ-whtEuCOntLS7mWVNZC3sygrtzusx0Icrl4f1BO6wVOjkHtQWvPl751mYlOom9QGr2m50euMOnDu8ksoBDrvCd3F_89NX30LaOLyt3ovsFamRtzIWW9TBwBUsEMRf8Snr1H0d-TI7sW3-mwMlzDWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
8فروند جنگنده A-10 Warthog در پایگاه هوایی موفق سلطی اردن مستقر شده‌اند.
🔴
این جنگنده ها برای پشتیبانی عملیات زمینی استفاده میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67317" target="_blank">📅 09:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67316">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67316" target="_blank">📅 02:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67315">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CiAYi3mIl8LKMDPsYyuRWExSxqstUZmd1_suRm4QJ4ZXyl4ZnvmNBXrP_1lAm-9CGsPSs8_f2AJCa-D8Ur8Bjn9n07_IGW3AdQQu-iN7zZzjINmMhoxh_PHRP8IHfcI8x4PD2-eLAS-CldFbttPNh-MY1vH7T8Dxws5DYVqayPM-0PPP_MlxWhBcmfwQUi1ZmCwAddWgT9zr7N0RU9nRTqvCpmsd_flWHohyOAEOfBEiJM9UCEk2dm6PIUDNNkDiKbzcGoBdv6ihdUVkquuI4DolDlfcDpV0kk17ONoHT5IT2zweN4JbkPzrAz1aSlyxwh-Gd3h1uTm072BeT-VgBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67315" target="_blank">📅 02:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67314">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bP_Uep3GWnbCcZRxxMizpoaSPi7ye_gZditecepXWVlbfViv_Zy56dFZ1G17a3_lxnN34Q7cIfPewefIWUOc-r33YCc0MeVQEU5feXV5IDwXNf_pgRCvpRpBqi5wIIsvsFRKCXyqSDGjwiuPlxJgL-iOo2FhZROnxG5AnTeuvJXa4DCoF6m9DZQAj_MWVjfhNiHKDhApiBOtHHrdJRrfAyQf3g4wQ0D_2iKuB7-N6egePgKksiYcS7XHkVll_ZByuMvs-owRPWVy-Xei3IQMtU_xV6301ovTuvB3qbR6zsTQhFtv-NgR2Tp38l8vJSVZNtoUgZP-KoYFCkcmHz6PvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
ولادیمیر پوتین، رئیس‌جمهور روسیه، با دونالد ترامپ تماس گرفت و دویست و پنجاهمین سالگرد استقلال ایالات متحده را به او تبریک گفت. کرملین اعلام کرد که این گفتگو یک ساعت و نیم به طول انجامید. پوتین از ترامپ برای سفر به روسیه دعوت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67314" target="_blank">📅 02:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67313">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79806b6dec.mp4?token=gkfgwUo1p3B38Pc1XND5ZfJQBj8tdD84ej11zQkVjGrAYKRd9TAbDei5DCSskZCRg0TbXduMD0vrp787SqSpWWyolUxzAI-D59Id9izjkIbkeBjMfByL-qrXl7O9ArXeL8mwKL42IU_L30seXY0khoAI5gRW_D6Oy2DyCGU5M1o4lSFA1rqMu15LzpiGFfaRLKt8VF1gyWeBMoWXI8ZHVbjbnfqE2BB3hkY-06-oSHOnVRaqQad3d_etgtGBeCko0MuxUrgXogtMc4tjI9Jx4rv4kEGS26pM88aopRbKzvbixfoUV58Jn2pglTRz2Pk0f5wpeoxHRvyjPMBcJq771Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79806b6dec.mp4?token=gkfgwUo1p3B38Pc1XND5ZfJQBj8tdD84ej11zQkVjGrAYKRd9TAbDei5DCSskZCRg0TbXduMD0vrp787SqSpWWyolUxzAI-D59Id9izjkIbkeBjMfByL-qrXl7O9ArXeL8mwKL42IU_L30seXY0khoAI5gRW_D6Oy2DyCGU5M1o4lSFA1rqMu15LzpiGFfaRLKt8VF1gyWeBMoWXI8ZHVbjbnfqE2BB3hkY-06-oSHOnVRaqQad3d_etgtGBeCko0MuxUrgXogtMc4tjI9Jx4rv4kEGS26pM88aopRbKzvbixfoUV58Jn2pglTRz2Pk0f5wpeoxHRvyjPMBcJq771Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جمعیت هموطنانمون در تجمع چند ماه پیش تورنتو رو ببینید و با جمعیتی که در مراسم تشییع جنازه علی خامنه‌ای اومدن مقایسه کنید
🔴
فرقش میدونید چیه؟ ۸۰ درصد جمعیت در مراسم خامنه ای اصلا ایرانی نیستند. کلی لبنانی عراقی یمنی و فاطمیون افغانی گرسنه رو با پول و... آوردن بازهم نتونستن مصلی رو پر کنن!
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67313" target="_blank">📅 01:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67312">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTvAaKxZyKU2mH98XmiOYMvdZUnkuSsSRYCdjoZY6FSgVlBro-L7_Gq1a-3n3HgFTLNKhGcLtDxoKiRMqMckU5nyMOP_joH3Y-_4ccu6zdb1IdXVajzR3o9wQ22rtCPxPL8sReaUlTU_oU_-YJbHfDv8tyIo9W1s3_BhzYxpLEJfbIA4hEcHrDmZBx1Wmuy1GeQZv3Nb_nfhkl0AOeiO3gtcC4qMe4e7r-rScw1bzWgGxoU70h2WswcYjhPFzZLrBmtEKsoM1ie3P_5xbAVHwb2lxqLMORWFtIgbB11dAo2C7jKq0IpXqWcf5qoH3L1Kij6oiMhbz5MBf5HGeTppNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نیروهای ارتش اسرائیل در حال عملیات در منطقه حداتا در جنوب لبنان هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67312" target="_blank">📅 00:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67311">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5be218b45.mp4?token=LoXF1hCd8eb1C11U7T6gbUaiy3l-fhnl5sry1u5oaQL6CiBN-SO-eMi3KKxlPk4GakkHwfe0drj73V82z-HBpbm3M4o0znr_muJR4Z3A_TovwbJGw1UCxODs0jUYUl6mMqOw6iX4bpd-YfAkLOLD_ccHk9rhQmW81lFBQTXfexiBVwDAclnS0zzn1Yt4yFWloIZz1Pr9hvGh9yb0uh0V6wSFQVp3HH0UVYuLqrvkhCAkBcnrZcvsBcq3hIZrHoFlRJC8ajgXdP27c6ujTTwX9hDxxubTMGEhuvJT3gNPzFsaP7kHt4SCI2c6e0rH80cht-P7OqcFPKcS698u0A_USA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5be218b45.mp4?token=LoXF1hCd8eb1C11U7T6gbUaiy3l-fhnl5sry1u5oaQL6CiBN-SO-eMi3KKxlPk4GakkHwfe0drj73V82z-HBpbm3M4o0znr_muJR4Z3A_TovwbJGw1UCxODs0jUYUl6mMqOw6iX4bpd-YfAkLOLD_ccHk9rhQmW81lFBQTXfexiBVwDAclnS0zzn1Yt4yFWloIZz1Pr9hvGh9yb0uh0V6wSFQVp3HH0UVYuLqrvkhCAkBcnrZcvsBcq3hIZrHoFlRJC8ajgXdP27c6ujTTwX9hDxxubTMGEhuvJT3gNPzFsaP7kHt4SCI2c6e0rH80cht-P7OqcFPKcS698u0A_USA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی خامنه‌ای،‌ 3 بهمن 1403:
ده‌ها متوهم به درک واصل شده‌اند. من به شما عرض می‌کنم به فضل الهی این تجربه تکرار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67311" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67310">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67310" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67309">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GToduZiCp0Ze3qS1-fQB8DhtQtCnqNKhGDwHkAObIkQisgkZGoGLGh1AE-r92O10gsSj38ZXQyrW8RGwFQ6efFpD8aEr7RJVrHYmydQMIk2OWwRoAlYKoWkcfrQrZEKqOnSehJ6zCwEGoRAZTWe-gElO2Dss50DJzZGw3vNR0FJhq1bxG2AVnGqPICu85e8Sd4pZWBLBTu6FyJGl4y2jaVZv7jZha8ZuG8XI6buVh9ZSqcX6xH1YeQrPM8er6T_s174Ag1hQTKf01L1Eidj9_J9j7fbpf15-2OO38FjGorF8Fj9_1tt6vQGhQYZkFl-1weVSNETlsiogqdZdoPgdEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67309" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67308">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/842bb5b4aa.mp4?token=AvWjsczTMEulfTM2vRf0gxO5vLgpkFe8gq1ZNKwbmlhlf1DNhlVPe8vXNDcJN0KhqtHwqrmTCrrjadAe3etRogwnhoajdD6a1Hqr5-PeuQGO4qoV7dbCTz4IIw0twrI_bBD2b_bo31PVWIau9T91HRMPhfqqmQf_GsUIgr2H7nEC-uJGBNJD5x0xCgO10dGpvIJHfPajWpxorlADT2rBTX64QF4ExK1lkI26EpgzVYNP3u4OdQcNRQAEtQnJIIt5we8GfiE5vVBroqcZuWlXOHCMc8Dsn-FA5B61NTCBzsX0IsnhjcLA8fP8Gsoku3V3bzNxTfBuO2LGV23msgP3sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/842bb5b4aa.mp4?token=AvWjsczTMEulfTM2vRf0gxO5vLgpkFe8gq1ZNKwbmlhlf1DNhlVPe8vXNDcJN0KhqtHwqrmTCrrjadAe3etRogwnhoajdD6a1Hqr5-PeuQGO4qoV7dbCTz4IIw0twrI_bBD2b_bo31PVWIau9T91HRMPhfqqmQf_GsUIgr2H7nEC-uJGBNJD5x0xCgO10dGpvIJHfPajWpxorlADT2rBTX64QF4ExK1lkI26EpgzVYNP3u4OdQcNRQAEtQnJIIt5we8GfiE5vVBroqcZuWlXOHCMc8Dsn-FA5B61NTCBzsX0IsnhjcLA8fP8Gsoku3V3bzNxTfBuO2LGV23msgP3sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویس‌هایی لو رفته از ابویسانی، معاون وزیر اموزش پرورش حین گفت‌وگو با دانش‌اموزان معترض ؛
دانش آموز:
نه اجازه میدین تشییع رهبرمون شرکت کنیم ، نه اجازه می‌دین پیاده‌روی اربعین شرکت کنیم، چه کار مهمی الان دارین؟
+ ابویسانی :
اربعین بخوره کمرتون!
دانش آموز:
ما می‌خوایم تشییع آقا رو شرکت کنیم.
ابویسانی:
برو بابا تشییع تشییع..
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67308" target="_blank">📅 00:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67306">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNu-5lXo_m2RnRnfAQW-8W3fQzwNQSrXB1edhlSkVn9iJoasNzP2J9MSVe2I2kotvETq_wDwUlQlKIt4T5bGzZrf6E7Vtw23ZKsoU9zN3vDJfUP8RobAmfe-Zdy0mDSvwXXQ-7yONonoubcRDQkdCHh7saDaHWP2xm41iU1Qc6n7mKtAuoEgRwZNhPUhlofgzF0iaqrvYIJswdnFtp_tLBlzaXjRW6qe__9HhOeirkrhZMSmlf-qjZVAd4NchBlsf5U2gwlmrLKyxTJwatYl5x3-eeDxt_VdnXTTL3MqgXM2h4CdBypbI1LlRc7EONEOChjs8neLJ7e8Y5W7LgwNXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7ffa7579f.mp4?token=lSvsoCTuRj9B4S2hCUL7LZlSTb6AQXGOo71XNQ2XuBp39imqjmxRg_70dEI7riE1wb6DkpRMKd7uxRHAvX5btQXmlX--f9MV_e1Gv9JWvox6QGz1bkLjzDjT203PJe7Zg3VYQBCRl32aW4NVhSPZ2GTQfd56z7E9V19nHQmjv60Ykms1B4AuLL9BaVcN6eimioIf11dIqmLcaUGe8xu2VG7w_EWExKWEqS7V3HnHJ8XMKXI81AAA1-kQKdfL7XN7F4B0FYBB5BSZ__Ry-W4OpfphEj4_s54DToaiMBSxxAh9k_oa2uLIr4kD2ojQcqx_jJBpFzIDroTNtB99OW57Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7ffa7579f.mp4?token=lSvsoCTuRj9B4S2hCUL7LZlSTb6AQXGOo71XNQ2XuBp39imqjmxRg_70dEI7riE1wb6DkpRMKd7uxRHAvX5btQXmlX--f9MV_e1Gv9JWvox6QGz1bkLjzDjT203PJe7Zg3VYQBCRl32aW4NVhSPZ2GTQfd56z7E9V19nHQmjv60Ykms1B4AuLL9BaVcN6eimioIf11dIqmLcaUGe8xu2VG7w_EWExKWEqS7V3HnHJ8XMKXI81AAA1-kQKdfL7XN7F4B0FYBB5BSZ__Ry-W4OpfphEj4_s54DToaiMBSxxAh9k_oa2uLIr4kD2ojQcqx_jJBpFzIDroTNtB99OW57Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعد از مزدوران نیجریه‌ای حالا یک فاطی کماندو از بوسنی و هرزگوین ببینید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67306" target="_blank">📅 23:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67305">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af68b2c3a9.mp4?token=qYCVuho1WhbQ4H07ISRPOvVxrZztE4VlQhqS1vjlnma85ifrbtbvdXYaIJzvvwpKi4V2DP2G6PPXhxuJrypJfNRQDPec9e5km4HxVxwdZ4Xh9YAz2O7-O4XkSc23NBnF3kAV_SbIJvpFGl0hDAkjX5HbYMicFGI_ZjsC9ACGeHUl06C-Z3vuxCHdmUVvSI1s2yvyqEvpTYeRo1SaUSPhnPN1m9QHSymFttT78qeq8XZg16XrBNTNhXE7CWZp7vwKfv65YLiByK-YdcnG7SRmNQn0BfM36jYFvP2__I9oKV50g6kl_p9Uy3uN8MQJ9hECZYcLstJMbOTWsGP6s7L4Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af68b2c3a9.mp4?token=qYCVuho1WhbQ4H07ISRPOvVxrZztE4VlQhqS1vjlnma85ifrbtbvdXYaIJzvvwpKi4V2DP2G6PPXhxuJrypJfNRQDPec9e5km4HxVxwdZ4Xh9YAz2O7-O4XkSc23NBnF3kAV_SbIJvpFGl0hDAkjX5HbYMicFGI_ZjsC9ACGeHUl06C-Z3vuxCHdmUVvSI1s2yvyqEvpTYeRo1SaUSPhnPN1m9QHSymFttT78qeq8XZg16XrBNTNhXE7CWZp7vwKfv65YLiByK-YdcnG7SRmNQn0BfM36jYFvP2__I9oKV50g6kl_p9Uy3uN8MQJ9hECZYcLstJMbOTWsGP6s7L4Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلم خاکسپاری رضاشاه بزرگ در تهران، زمانی که جمعیت تهران فقط ۹۰۰ هزار نفر بود و بیش از ۲۰۰ هزار نفر در مراسم شرکت کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67305" target="_blank">📅 23:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67303">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tc4VuFTb66hDPuCQmIbN55xyWSYTxS09OmBqS3v5Ubvbm_9G2dmkMzmXklDD-y3nKDFEEsjQj5Uy0_FBe-PV3C4jwwaFYfV1XvEyQI4OjosKnSlns-w9PTTSod2FoGedlxSS1ElXJ_9aGA2HkFkv5MBcwlKEUa8GZbAma9H1fgTezJw7tz6KlZ8QJpruhxqrwg7fiJc7xm55tKZJMstzsuAEsdiqIEnfe8zUqsJJQdgu0PitK7LohjBskadrk1DYwNnxm2XFZtxTtmTybk3uLUs21HiDzRXO66Ye5orNIeG5qhNrJ5PZjVFxL6svXKDyvRivac8d8yfyV2i_9g6JNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NBkrz4qjyWpQ_OY5e6IoQDtmrMC3qsCpfD2yasQ4ZyGwp5sYa5rzwz-p2Y4kWbIAE21PywqXVl1fgRanU-IF_XjJQdRY9QsALhX4JyytwLT-Qtaq5PL6cWtAdwS6Kn-gDRNZ4Kwo7LMtx10KqD04IumPb4uBma6cJFA4E5-ht2n75fMFiQbEeZEKnMrIj69IroiqCaH0Nr-BWVUfZzRlBJixb1Bt_8RdeUf5MlDkczBbaxdO9qSUZBEFwtjexehDYmCWjNfiB1k3diJp2I25u9ViBqX823XLh7yhHB5QPs7pPaGKx7cjJWLyAcWC_hDsvYRcca_-0Q5cbf3Kq2dCTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
زمین گرده...
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67303" target="_blank">📅 23:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67302">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJyBw-ZWJEagfuOcQtV2f3S1yda3fjT5Ig4QlM7UIXDCFbmVAc5Swz8dkj93p9vhdyoAPXFGmjC5LRfzEFRLbJBHohGSrGQHyTlx5CEylji6ZHHWueSzv7BJ0RoEAXlSNv0OlHycYQdsscN_78L9H7qQVcSPu8EEDJFXE7RJeVtEIVDI8-nmoyrg3NPdOYqqab7HRwDgQD5QzxdJ34nt0k71WLAfgvC7vajBjEesSa8TuypPGOKgaF7hPxk2JaL4897ipO-QmFOLALnkW0rB7nDUdEfnET5tOk6TFnOWodfSTBr25X3kjoDbKKUgy3UmQKLwsAbibe7-WGJJ6ZlghQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
دو مقام آمریکایی به من گفتند که مسیر جنوبی در تنگه هرمز همچنان فعال است.
یک مقام آمریکایی مدعی شد که اکثر کشتی‌ها با سامانه شناسایی الکترونیکی خاموش تردد می‌کنند تا توسط پلتفرم‌های اطلاعاتیِ «منبع‌باز» (Open-source) رصد نشوند.
این مقام تأیید کرد که ایرانی‌ها تلاش می‌کنند از طریق رادیو VHF برای کشتی‌ها ایجاد ارعاب کنند.
مقام دوم آمریکایی اظهار داشت که سرعت تردد در مسیر جنوبی طی روزهای اخیر افزایش یافته است (حدود ۵۰ کشتی عبور کرده‌اند) و این مسیر همچنان باز است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67302" target="_blank">📅 23:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67301">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0711bc2f95.mp4?token=aMlXxBzmeQk3iSoF10jkw5qAfswgtipn_uMTQvNUtgezQTHoYtK0ijESySdHfaNQ4vS7-1XO46E9VhPA5YXeoN2akUjqXAUHBtBhXZobqy8KNOfCq2G2lUNox2nSPnnw1oqvEtlpjS-VJaR6CPQLq4oIUnC9GEpA4U1Wy6hqxMW2wX7gnwD6mJ_2K4LdMghxX0621rD6MV8j-oIgJLcNnsI_6X-REUrrTZGeZjAftgo1wTRT7B0-XwZZz6w7ddB2BgBTpeoklBOd6ZG6js_iJfU_sVImkkK8b4H9_W6AfUsLUvDFBct7PWHxaz5bo_sWh2HWEf0nHSZn1BqBRqtflg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0711bc2f95.mp4?token=aMlXxBzmeQk3iSoF10jkw5qAfswgtipn_uMTQvNUtgezQTHoYtK0ijESySdHfaNQ4vS7-1XO46E9VhPA5YXeoN2akUjqXAUHBtBhXZobqy8KNOfCq2G2lUNox2nSPnnw1oqvEtlpjS-VJaR6CPQLq4oIUnC9GEpA4U1Wy6hqxMW2wX7gnwD6mJ_2K4LdMghxX0621rD6MV8j-oIgJLcNnsI_6X-REUrrTZGeZjAftgo1wTRT7B0-XwZZz6w7ddB2BgBTpeoklBOd6ZG6js_iJfU_sVImkkK8b4H9_W6AfUsLUvDFBct7PWHxaz5bo_sWh2HWEf0nHSZn1BqBRqtflg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مردم اروپا با دمای نهایت ۳۶ درجه
🆚
مردم خاورمیانه با دمای حداقل ۵۰ درجه
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67301" target="_blank">📅 22:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67300">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eda932d9d3.mp4?token=FVt7o-MW79CBsT0WsvXLtnD3pbuz9jUljvhP8_a8VGiXteTHTQ3fhwiYtHjVYfZj045mIH-a4p1y9IsB1gzdbrMQePtrV3hmi7WbyXkZIAPlCOabYN-QnU6F6mCpJY1_E9cSED6QThTtk1vO6MQO3k25byKsKqdAHHuzNsWwNgHs8eFLnCOnUdGdVsYrilFzKe50_Hw6Hmv8HwQF47E_r0Bd8xmhbYrFimjUAYjyOUGwglhnSL_ZHjN94Q1wn7V8hw8fg32VljmP_LWzvWjLeeDfZU0xU6Y3vYqSCtrOOnsl3fJRwSENHb_o3UjVv9_H4oXozY9VOksn7YISiQaPyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eda932d9d3.mp4?token=FVt7o-MW79CBsT0WsvXLtnD3pbuz9jUljvhP8_a8VGiXteTHTQ3fhwiYtHjVYfZj045mIH-a4p1y9IsB1gzdbrMQePtrV3hmi7WbyXkZIAPlCOabYN-QnU6F6mCpJY1_E9cSED6QThTtk1vO6MQO3k25byKsKqdAHHuzNsWwNgHs8eFLnCOnUdGdVsYrilFzKe50_Hw6Hmv8HwQF47E_r0Bd8xmhbYrFimjUAYjyOUGwglhnSL_ZHjN94Q1wn7V8hw8fg32VljmP_LWzvWjLeeDfZU0xU6Y3vYqSCtrOOnsl3fJRwSENHb_o3UjVv9_H4oXozY9VOksn7YISiQaPyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیام نتانیاهو به آمریکا به مناسبت دویست و پنجاهمین سالگرد استقلال:
🔴
«۲۵۰ سال آزادی. ۲۵۰ سال دفاع از آزادی.» او این مناسبت را به عملیات «انتبه» در ۵۰ سال پیش (که در آن برادرش «یونی» حین نجات گروگان‌ها جان باخت) پیوند داد و اظهار داشت که آمریکا و اسرائیل در ارزش‌ها، سرنوشت و مبارزه با مستبدانی که شعار «مرگ بر آمریکا» و «مرگ بر اسرائیل» سر می‌دهند، اشتراک دارند. یادآوریِ یک اتحاد مستحکم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67300" target="_blank">📅 22:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67299">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHoK1lioWhhGdo36SkW8E1b5ia4nyYo4sQOL28iM1CMvCBJ9p5NBXyhjoTja14BRI3Lpz-sOGCug9TskhURIqYHfZEPjUE-nGam_Ly25wjoxmFqS6KEarNQ7DlxlJp3X5T9Df8NCNEDrJ5UuJWRvANYdqDVrNbbtfCc-W4WBUN4xxLqPoyeGD7y0TwzdCaetFdotPfOhVLuF0PUS2KxRstIBNbyA8z--0owvrWH3xzrygM_wJkyaWSVfyOHF9VrjIaGbTiaNV3dcAt_uIBP_xxd0ukTVugu5_GyUBqATwIYyWK86fbydrgcPcYwixKIU1nbrIIzrUt-OAUCweldt_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
العربیه:
دور بعدی مذاکرات ایالات متحده آمریکا و ایران در تاریخ 11 ژوئیه (21 تیر) به میزبانی پاکستان در اسلام آباد برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67299" target="_blank">📅 21:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67298">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yh6wGm_30s5Ye6TxQfJQiV1f1CvVrUjjqKbXHYbZeOScIUH5goZFRKmbb1hAs-5AMcfiG9Dj7UDIQnsn0KA7JH10n9LHTboNvLQ1eEiNt6AfSYtQzKRN3pYBcT0sC5odiUzLve3yS7d1q5hX2X0OuHnSdNXYe_QlMc-2vY6MjMFoVpqehR_LYIFS_mBKDrDagdemlEnHbOS1Bp6YwnNWK5_nCV9Gnp3e8WmgfubSZq-gNrhp_0FKxd5azAzZgrN564Tmamtw4NMuS3imlah0_d7JVEXIP1NFY-OgX76DLi4k-5G0Gek8j-YbU0PYrtQheTb0u6NqKmlK8YKfPZrd8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترامپ:
فکر می‌کنم آن اشک‌ها مصنوعی بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67298" target="_blank">📅 21:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67297">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ASibVsYJZo3uoZPqmedf7brD198-WXcyKb9X21S7LHCEPDZu0PinS-gRrpjSITNCS8bx6W9efdGQQXkhJ-mKwj-T6f1wulQWZHvnkcEWjx4SgDbZdvXx-UIPJxeZiRl0LqxYsZpDzSl9dqOAhK8tnJnBg7ky5sMQD_01DYe6HCIPFSK1qUqM2IQqm4dkf7Aqv8eM2TlE0LEX6JbYWLYy50oWanDLN0jdg9G5L7lBEC0xWyVZWfeLpP_pGBvxetxvKMI2pD6F1EKXEEwBbdlLlXh3ghKOWoIn75K3ijSPi9O73usQ8vBgGggtkNG47pYtiI8VGLcw4fcmh_1gI4RkBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ به آکسیوس:
نتانیاهو میداند رئیس کیست.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67297" target="_blank">📅 20:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67296">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
پرزیدنت ترامپ:
نتانیاهو درخواست ملاقات در کاخ سفید کرده است و این ملاقات ممکن است همین هفته آینده رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67296" target="_blank">📅 20:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67295">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ به اکسیوس:
از دیدن ایرانی‌هایی که در مراسم خاکسپاری خامنه‌ای گریه می‌کردند، شگفت‌زده شدم. من فکر می‌کردم مردم از او متنفر بودند.فکر می‌کنم آن اشک‌ها مصنوعی بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67295" target="_blank">📅 20:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67294">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
پرزیدنت ترامپ به آکسیوس:
«همه آن‌ها آنجا هستند. یک گلوله [و می‌توانیم همه آن‌ها را از بین ببریم]، اما ما این کار را نخواهیم کرد، زیرا در آن صورت، هیچ‌کس برای مذاکره با ما نخواهد ماند.»
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67294" target="_blank">📅 20:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67293">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/589cc62912.mp4?token=QiBmmm61klLFpHO6sakDbZorEmQeOzA1zO4xm6iK64kzvTyE8M8uY8JDjIuBmd8B-ytTqP6kNj5yQvNxpXhwnW41qneQRpScqIgks8jYAV8Fj9AZxwuXOeRlrCfovYgWcrHSitczNrIllvfVGpQDS5Mw1HnzvT6BoiU7H5Pm8P6rBuJIeEtC0vCJvnIrbVAR0rQX_lTDuSMDuPDSh7qJjWrIqBNM1sDFcCGc-0ZeQIclMsWZ1LVDcH81Ki8DZC7YAMBFyxu71k7G6jQn-bMkHgwYWeqmjwHAaksCVfJuD60E-VY6k_hucy33loVy1nifznjox8esnW407d3cwmwtrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/589cc62912.mp4?token=QiBmmm61klLFpHO6sakDbZorEmQeOzA1zO4xm6iK64kzvTyE8M8uY8JDjIuBmd8B-ytTqP6kNj5yQvNxpXhwnW41qneQRpScqIgks8jYAV8Fj9AZxwuXOeRlrCfovYgWcrHSitczNrIllvfVGpQDS5Mw1HnzvT6BoiU7H5Pm8P6rBuJIeEtC0vCJvnIrbVAR0rQX_lTDuSMDuPDSh7qJjWrIqBNM1sDFcCGc-0ZeQIclMsWZ1LVDcH81Ki8DZC7YAMBFyxu71k7G6jQn-bMkHgwYWeqmjwHAaksCVfJuD60E-VY6k_hucy33loVy1nifznjox8esnW407d3cwmwtrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
۲۸ دسامبر ۲۰۱۱؛ مراسم تشییع جنازه کیم جونگ ایل، رهبر کره شمالی؛ مراسمی که تصاویرش به یکی از عجیب‌ترین صحنه‌های تاریخ معاصر تبدیل شد.
وقتی این تصاویر را می‌بینیم، شاید اولین واکنشمان تعجب از شدت گریه و شیون مردم باشد. اما واقعیت احتمالاً پیچیده‌تر از چیزی است که در چند ثانیه ویدئو دیده می‌شود. در کره شمالی، مردم دهه‌هاست در یکی از بسته‌ترین نظام‌های جهان زندگی می‌کنند. از کودکی به آن‌ها آموزش داده می‌شود که رهبر، شخصیتی فراتر از یک سیاستمدار است و باید بی‌چون‌وچرا به او وفادار بود.
از سوی دیگر، در چنین حکومت‌هایی، ابراز احساسات در مراسم‌های رسمی همیشه یک انتخاب شخصی نیست. بسیاری از تحلیلگران معتقدند که آنچه در این تصاویر می‌بینیم، ترکیبی از باور واقعی، سال‌ها تبلیغات حکومتی، فشار اجتماعی، ترس از حکومت و گاهی هم منافع شخصی است.
شاید مهم‌ترین درس این تصاویر این باشد که وقتی دسترسی مردم به اطلاعات آزاد محدود شود و فقط یک روایت سال‌ها تکرار شود، همان روایت می‌تواند واقعیت ذهن بسیاری از افراد را شکل دهد.
تاریخ بارها نشان داده که پرستش شخصیت، فقط به یک کشور محدود نیست؛ هر جامعه‌ای که آزادی بیان، نقد و گردش آزاد اطلاعات را از دست بدهد، ممکن است در همان مسیر قدم بگذارد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67293" target="_blank">📅 20:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67292">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/648e669177.mp4?token=DyTT5rMROvfb55juNsrZHxD95B96Gkyeb59qiGKs1zC-g_dOKNTEqBY_i-PJXVwmrI6TUUPZbSbXM76zUiGp2aaJ0gC6Gyv0qULBvskRdxm653l8ZEJBayRS3_rAySFwFHrPaPV0oXX2CJAF2pUoMGKWVL864J-dCq2KGFhqxTU-jeRVKzxuBglJigXXwic0uGQxPmeRmlPcSKmjSPFHaoCVR27Ab7O_iG0p9Y-2GXS0GYJw5T2HOIZAFWiy7PBA_3IcKBmpaG4qTaxV9PR6XXEzGp7WSyZlmK1qzdPsZHJI7ZQRpnsxHX2g6WFqWDd5x3VdqTaObL9uYhTznDIroQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/648e669177.mp4?token=DyTT5rMROvfb55juNsrZHxD95B96Gkyeb59qiGKs1zC-g_dOKNTEqBY_i-PJXVwmrI6TUUPZbSbXM76zUiGp2aaJ0gC6Gyv0qULBvskRdxm653l8ZEJBayRS3_rAySFwFHrPaPV0oXX2CJAF2pUoMGKWVL864J-dCq2KGFhqxTU-jeRVKzxuBglJigXXwic0uGQxPmeRmlPcSKmjSPFHaoCVR27Ab7O_iG0p9Y-2GXS0GYJw5T2HOIZAFWiy7PBA_3IcKBmpaG4qTaxV9PR6XXEzGp7WSyZlmK1qzdPsZHJI7ZQRpnsxHX2g6WFqWDd5x3VdqTaObL9uYhTznDIroQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
▶️
داده‌های تارنمای ردیابی پرواز «فلایت رادار ۲۴» (Flightradar24) نشان می‌دهد که یک خلبان آمریکایی در آستانه چهارم ژوئیه، روز استقلال ایالات متحده، با طراحی مسیر پرواز خود بر فراز ایالت اوهایو، عبارت «USA 250th» را در کنار نقشه جغرافیایی آمریکا ترسیم کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67292" target="_blank">📅 20:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67291">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر : مراجع تقلیدی که‌ قراره نمازِ علی خامنه‌ای رو بخونن که همچنان خبری از مجتبی خامنه‌ای نیست!
تهران : سبحانی
قم : عبدالله جوادی آملی
مشهد : نوری همدانی
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67291" target="_blank">📅 19:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67290">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cc795d411.mp4?token=ejifXsifOVafhkTQyLG_QZ5OLC4eOYhcBRO4pBBWJR55d_XQ_HkGTH0Sp-vspbIqrhpYRK96EvVOQSx9JChtk2BtfAOF-1HplgrO6Hf2dbWD2b-4T8LcYhW_AQy0noErv2Q1xygE51NE799RAVEHQq89Qk2XFlkpudf2-lU4kEoGnFMwbAPMMoEpw6Q8Rbfnpm3pvENGYTtkka7c70ek61MyPCg4LizgTsxtOGJzk6TdAWT09FR5bPvxl0dOM7OMYt2VxL8t7POlvHIY2S4sGyIdSW3LyUAgc60gp36k-mx7EtVM33cKB6i4Ni7t9sUlbuzEOnDUfV8vLt_X_rusCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cc795d411.mp4?token=ejifXsifOVafhkTQyLG_QZ5OLC4eOYhcBRO4pBBWJR55d_XQ_HkGTH0Sp-vspbIqrhpYRK96EvVOQSx9JChtk2BtfAOF-1HplgrO6Hf2dbWD2b-4T8LcYhW_AQy0noErv2Q1xygE51NE799RAVEHQq89Qk2XFlkpudf2-lU4kEoGnFMwbAPMMoEpw6Q8Rbfnpm3pvENGYTtkka7c70ek61MyPCg4LizgTsxtOGJzk6TdAWT09FR5bPvxl0dOM7OMYt2VxL8t7POlvHIY2S4sGyIdSW3LyUAgc60gp36k-mx7EtVM33cKB6i4Ni7t9sUlbuzEOnDUfV8vLt_X_rusCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
یحیی رحیم صفوی:
بین ایران و اسراییل جنگ موجودیتی است یکی باید بماند
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67290" target="_blank">📅 18:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67289">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNZSxZtKqWSySskjkv2fVQLToQMz-2bLnLqLkwxSQhn5uycI4zRrUUp8DuJN3LMtDCl3f6O_IcaZduwNCqmHQp9t2tlkv46puBLTa1SralEr0njfrmqqrhaI9WQrOJS6WNhjm5leZHRjxKr22baAaqit6W73T4010HpYP9DRETLh4rd6qb4LlLmj8NV44OlvSsHA-COOrhMxl_gKcwkjFVg3RK_dPKqi_T30zKrsJioTKKmqPjJa5OptclnZh-NzXOMsOTaAGlgyfdlvOL3F3OTg3XMorIw5kUNEzOULPMkMRiseR0FMSWmNXK7Xy44798at-Z90ULmEbGimyiUWYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شاهزاده رضا پهلوی:
🔴
خطاب به نمایندگان خارجی حاضر در تهران برای سوگواری علی خامنه‌ای، دیکتاتور فقید ایران: ایران در سوگ او نیست.
🔴
ایران سوگوار بیش از ۴۰ هزار فرزند خود است که در روزهای ۸ و ۹ ژانویه به دست خامنه‌ای، قالیباف و ماشین سرکوب آن‌ها به خاک و خون کشیده شدند.
🔴
رژیم مبالغ هنگفتی از ثروت مردم ایران را صرف برپایی این نمایش تبلیغاتی می‌کند، حال آنکه حتی یک رهبر دموکراتیک نیز در آن حضور نیافت.
🔴
آنچه امروز می‌بینید، ملتی نیست که در سوگ حاکم خود نشسته باشد؛
🔴
بلکه ملتی است سرشار از خشم برحق، و همین خشم و دلیریِ قهرمانانه، بساطِ باقی‌مانده‌ی این رژیم جنایتکار را درهم خواهد پیچید.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67289" target="_blank">📅 17:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67288">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20335e95a0.mp4?token=kJw1HVEvYREvPPKssuhabavogcaWEU5Ghh4vEoLp1-PoCUzjR30bJkgOjhhv93nD28N49wvVDB0PrfJEVj-_a-Cr9vYVL1JUUdieIW0ZaihEafMuHM7p4z9HktNrs6T3Bm1SlKlIYxmDw2x8wTRIlTLDJSFJdy5JRwYIt6Bwo4rGxEpRkI8LJYVJyP9kBvEvkHDSTru3_G-_kQo7A6XYuIRwZEG5-H1yeZDFXJfJVeikH3HWB8-6XXeJp9pYiBKSAvpEJJYbOCa1wpIlBACg2JgzBN_CFA4jSMiC4wHR7KPwFE13c9Ks0COL9j2KZZmje5xC0RRU-QSgJn5uapHUmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20335e95a0.mp4?token=kJw1HVEvYREvPPKssuhabavogcaWEU5Ghh4vEoLp1-PoCUzjR30bJkgOjhhv93nD28N49wvVDB0PrfJEVj-_a-Cr9vYVL1JUUdieIW0ZaihEafMuHM7p4z9HktNrs6T3Bm1SlKlIYxmDw2x8wTRIlTLDJSFJdy5JRwYIt6Bwo4rGxEpRkI8LJYVJyP9kBvEvkHDSTru3_G-_kQo7A6XYuIRwZEG5-H1yeZDFXJfJVeikH3HWB8-6XXeJp9pYiBKSAvpEJJYbOCa1wpIlBACg2JgzBN_CFA4jSMiC4wHR7KPwFE13c9Ks0COL9j2KZZmje5xC0RRU-QSgJn5uapHUmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
روایتی تصویری از شاهنشاه آریامهر محمدرضا شاه پهلوی:
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67288" target="_blank">📅 17:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67287">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‼️
ادعای نیویورک تایمز به نقل از ۴ مقام ایرانی:
پزشکیان به مجتبی اطلاع داده بود که در صورت عدم توافق، از سمت خود استعفا خواهد داد.
نامه‌ای از رئیس بانک مرکزی ایران باعث شد مجتبی با یادداشت تفاهم موافقت کند.
پزشکیان، قبل از امضای توافق، به مجتبی خامنه‌ای اطلاع داد که محاصره دریایی، ایران را فلج خواهد کرد
.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67287" target="_blank">📅 16:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67286">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90b7a34aa.mp4?token=stsnR4faCJeit07wHck9U4aLv-qtG2YmQQBQaiuMxTaXfDr1Rk4WqeZH3IPzPO-5wd3YfY79h7qgHhqLUCjRgwc6NMuOd5FvoC9bFBULQ1DIlQoufyfhK6sC_r3isuymQ9Bu43nth3ta3VWEXE92kVqWFRX5wHJoPND3LOzKoYHHmYAj3BKoxTMxftVomVzzXF1kNlvKOXSej0KiJa-2XmxqIwwIJno9uTvfS0Na30BWc7Dz34XAt_6joLD_TGJ_9j-oIcDVQ47e_jgk0mGPedH8fgeAAki7lUyecceGiwF34RDQJLGK3cEgKGThvrV4fnEOcv5h7enj1p_DRabq6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90b7a34aa.mp4?token=stsnR4faCJeit07wHck9U4aLv-qtG2YmQQBQaiuMxTaXfDr1Rk4WqeZH3IPzPO-5wd3YfY79h7qgHhqLUCjRgwc6NMuOd5FvoC9bFBULQ1DIlQoufyfhK6sC_r3isuymQ9Bu43nth3ta3VWEXE92kVqWFRX5wHJoPND3LOzKoYHHmYAj3BKoxTMxftVomVzzXF1kNlvKOXSej0KiJa-2XmxqIwwIJno9uTvfS0Na30BWc7Dz34XAt_6joLD_TGJ_9j-oIcDVQ47e_jgk0mGPedH8fgeAAki7lUyecceGiwF34RDQJLGK3cEgKGThvrV4fnEOcv5h7enj1p_DRabq6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعارهای عجیب در تجمع شبانه علیه قالیباف و آمریکا
😂
😐
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67286" target="_blank">📅 16:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67285">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/441130dd0d.mp4?token=eOmvjK9-VEj3_8jYpbCUcwXj8ZTLte4TZWa6KBcHNafNsaJ5101SY7zcQNcYNljoITn0H52o4XFYccSvk3Ia2dVInGsd5Pfix96_i0FDyr00JL75wmK60SqDZqDF7ZZkQRwo9tBvPzgYAkSjKVgL6K01U1mPqIeQeJwaFQGrJsVuNtPHQosTw7WUkwXtxbEQvcNz6f4YmgW_xtLOZOD9JCBDqiUirEY4eL0IJr_YVrWTgXs9P7u-JXu5faVwD1-76LZoCx9m25ixK02JEEKp82aWzvTh4EmdnOV1fyXFjHisrWVrDqeX-msgXOa0OGVcatnN0Fbq_gBYb8-mBmPZWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/441130dd0d.mp4?token=eOmvjK9-VEj3_8jYpbCUcwXj8ZTLte4TZWa6KBcHNafNsaJ5101SY7zcQNcYNljoITn0H52o4XFYccSvk3Ia2dVInGsd5Pfix96_i0FDyr00JL75wmK60SqDZqDF7ZZkQRwo9tBvPzgYAkSjKVgL6K01U1mPqIeQeJwaFQGrJsVuNtPHQosTw7WUkwXtxbEQvcNz6f4YmgW_xtLOZOD9JCBDqiUirEY4eL0IJr_YVrWTgXs9P7u-JXu5faVwD1-76LZoCx9m25ixK02JEEKp82aWzvTh4EmdnOV1fyXFjHisrWVrDqeX-msgXOa0OGVcatnN0Fbq_gBYb8-mBmPZWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
😐
ویدیوی این بسیجی که در مراسم تشییع علی خامنه‌ای وایرال شد!
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67285" target="_blank">📅 16:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67284">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/67284" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67284" target="_blank">📅 16:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67283">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67283" target="_blank">📅 16:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67282">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgcTk0ZC4Kqp_7lOHGQuNB5s-_krSoCsuqMnAWyMJ_ifeJ6bqeIHg-wTOrFFbC5H8o4C_yf8hxfSE2kQG3yArcj0AQ1aT7TblLr2If9G1b5LHDNWbuhRZLfmQNLhc-7DhEitKIjqdTKemokAkNYiKo6LBnXTFWMzbayRiOLxTZ2Rz4rK5J2Bu95O31KUyldW1bQWne-65Zqg1NO5yBa2b_YU8GmlJyb8vbNonZPY1Fqqv6lD6zvKYZQILurCuAAQfZkKhwV2h_gWSY6dEVneqnMNP9HGXYwp1oOTLm7aoYJNgiT9Pt2QgfdP4Pyl01vYw29J8drxyHA02L9XSEiojA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علی عظمایی فرمانده جدید نیرو دریایی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67282" target="_blank">📅 16:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67281">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
با تصمیم هیئت دولت، کل کشور فردا تعطیل شد
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67281" target="_blank">📅 16:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67280">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6GMbz03mlQ4LZ7xnhY5t39MliKV1hzom-26VKwPc4jhfkuRJSbKx9IxrvSKCQXrOIHNOClSaNutSIfrBa0htJloITn11SxSsJ7klWKuC_OA6k5HCldQcX0X2E_DzjvAMXQfMhlcMUGevIHAsAT9_KxY6PQ07sKGpChrfvss2Qkpg_iRCJjHl5KO9KC75dTUx06cBPJfGBVRJL6WRDMxzYB90g2OfdcESL2Ajku7ZYnwhKDlMc1ZRyHNUkMJBT7CFlKILHHqUjOQlDYEPLWg65QuKsDTcfyxICpB13Q2NVz4XQFtRIywJ0aM1gvCIHVpJ_Qlke0DCdo5H-7fPcDVxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نیویورک تایمز به نقل از منابع آگاه:
🔴
مجتبی خامنه‌ای به مقام‌ها گفته است می‌خواهد در مراسم تدفین پدرش در حرم امام هشتم شیعیان در مشهد، که برای ۱۸ تیر برنامه‌ریزی شده، شرکت کند و نماز میت را بخواند.
🔴
مقام‌های امنیتی تاکنون با حضور مجتبی خامنه‌ای در این مراسم مخالفت کرده‌اند، زیرا نگران هستند اسرائیل از این مراسم برای کشتن او یا ردیابی محل اختفایش استفاده کند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67280" target="_blank">📅 15:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67277">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ORiILZTg9HDT_P_Hpd7qB9ZqYHHDvllPISrAldyrx3fYIcs9Qcz8gW_9gTBwgDKsTdDJs9UbRMWOq1fGQuieKerGJqO4YLAb8lEGiF6Q7_24pgj8rk0E3puni6hGVMgNufmkIwfB5j1vIDdEDEBsZdggsL1rr6jPh68IJplXKItAUctYQdgLUHf2B_XZPSbGOEkCY0AGktizZfCk7IbbgJI0jA31LZp1YmsMVAyLrdKKjpjiSwu6eZRzl7STioXaDiDjCV7BfI8hQ0y5iUNBAOL_qrt0QeG45TiAodVbm8lrsNV0dfZmrGlLcag3gtwNiqkPyhqRd8-G8pGZoRp1uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rkYS_GF7BZu0h4beT4W-9tNgICOyMznNMy0eqjhkDrpLOQuIlgfJ7g3WISNkJLuTOQoKv98fqq-cWCO6HuqKVG2lpQzVgf8BP91G4Mpmz99fgIvaTJvm8fDBNoJovJv1eJdRiz5gN7PSYL4pMwUEGgYkcYe2H4XKIBqkV6owY1O9VAdjK6iTCOUhuiWttcQHUYvzGPqi4UWRssC3s929591zlOBkFyXUX0TsJAW5kxc3TO_Uq2ujiKeezTCUDyqawkHw7tmBcf5Ca6xwGpQ3tGgjlKoYpkim-8kKUjmxVDTUNngnsjnldJTKcgF1SwicSKVwtQP_qV7rPp0gyYY8Og.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/502fac7d76.mp4?token=eaM82hMRN7STbgBWfhKob3GPiysUqZ4ZcfEpexbbvSBoCckGeIf1tdoA2mTrXEbgHZqom9xG_GhmB5G-hiF5RomF7g0KY4khEKrZKblvYYLAiR9S-jelg0Ez0WSw5hnAT3wxruu5rFcO32nGlzyp8-Omax3pXi25IaCeorZGamcqs1HjzSRRb9HFKTvPVFmtCv0dzfWhFMKdUyo6Xo1OFPWWAfv2mmVWPH3GVpYV-_IgFPDcg3bgKY3oOntRwWvl1nxYJvCJOBhFafNAtU1gqb6y117-5GgzsqTXsoDH68XDlVKy6ZgRDgHAsuH4x9KlJwFvtmJN-jcj-eiFm_8wSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/502fac7d76.mp4?token=eaM82hMRN7STbgBWfhKob3GPiysUqZ4ZcfEpexbbvSBoCckGeIf1tdoA2mTrXEbgHZqom9xG_GhmB5G-hiF5RomF7g0KY4khEKrZKblvYYLAiR9S-jelg0Ez0WSw5hnAT3wxruu5rFcO32nGlzyp8-Omax3pXi25IaCeorZGamcqs1HjzSRRb9HFKTvPVFmtCv0dzfWhFMKdUyo6Xo1OFPWWAfv2mmVWPH3GVpYV-_IgFPDcg3bgKY3oOntRwWvl1nxYJvCJOBhFafNAtU1gqb6y117-5GgzsqTXsoDH68XDlVKy6ZgRDgHAsuH4x9KlJwFvtmJN-jcj-eiFm_8wSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیشب، برخورد یک صاعقه با برج وان ورلد ترید سنتر در نیویورک
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67277" target="_blank">📅 15:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67276">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d41icN7TqQBMwQV8t0CBN63BqHb18nDR0e0acCiW4tDccIeRENP_Dald8EH9VLT-TWrMq5aT_Ktcmr5MHz9SaylBKV6dTI8ozmCJts4sIRO_E-AzlFiZxPtqCaIkJ9uotXKi5HNJvDnynbB8H_JQ-dGdI52S39MirPpaY8HSLLmptQcwzNf4brRfmk7l08JjUJinoRrPJla8MdeLK1x3WPjh9a8YyJfud4S0Xy5ZQsA5svG_0HyrHiJUegS62FiFUieVBLCie0IWedf4NGVgO4u1nvN9x2SmlrBnRl4Bgox7-3GrLxt7UF_zzof6rAyYMW__UHmxtW9NJBA6xaRZPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدودوف معاون رئیس شورای امنیت روسیه:
🔴
ج ا به‌جای سلاح هسته‌ای، به سلاح دیگری دست یافته که دست‌کمی از سلاح هسته‌ای ندارد: تنگه هرمز.
🔴
بحث‌ها اکنون بر سر این است که در آینده، درباره نحوه کارکرد و وضعیت این تنگه چه توافق‌هایی حاصل خواهد شد.
🔴
مقام‌های ایرانی همچنین یک «سلاح ترمونوکلئار» دیگر هم در اختیار دارند: تنگه باب‌المندب.
🔴
اگر این گذرگاه بسته شود، همه محموله‌های نفتی و سایر مسیرهای حمل‌ونقل عملاً قفل خواهند شد
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67276" target="_blank">📅 15:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67275">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MbiQHc4b4h4t1lrVRpzNtyWnf-GfWnj37MEfT268iUY0S0g6tliEcJEhDwFKoyDUQ0dy95OVr_1rO9YTcCXKUqvp6OspaHDDxXPwE-9BKmnSjHaYG9fo-WdXBqmRiO7-JupeFFFLovegFnZE-COUkBaRqmaFL_16jQGnehH8E5D31Q2OpUhlw-VMGktKE9QScVqjIL1hPC_7Jz2oRksEVRQoCIDn6DNDYUixC0UhTO3TlkvwWMTxgx8P6CG5fgiMF25mlbio01FqMZ32VIvBGd6ECAne-PZVGWQ4l0cWSWvJzsG9Z4Iv0-s70WzquXwxVJ0XM3_7OcjTOSdST5UStA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمال مجازی‌شدن مدارس و دانشگاه‌ها در سال جاری!
🔴
میزان کسری گاز به حدود ۶۳۰ میلیون مترمکعب رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67275" target="_blank">📅 14:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67274">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HrtFFKd7NgBRtmNrPct_eZplXsTpQJspyd1n2FLFhYA__Q6LGd3vHvK8Q4OECdbbPh31kv1mF6kIZa33u1lpmoNG3pR8EeeZ89mNHtQjCpazWW4jf4eVCHHADyHigZQrpYe-BFjfeuLeqcoK6kddYgma4IixE_VBYv3uJRXa-gqC3zJhBxpJzd0mo1bbuJSafwUizgRCgnh7kizfgff4URmVOjuOvl0JKasCWy37IFLl5-xL-SeyzffWKdTFaYy24efp20A9aqm-qhhyoSLXHlUKjm_EBMgekcvQPf98emwurJSr3mqs0e9URzkQ2zYE5osLeNp6dmaGB5ik9s1sew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برافراشتن پرچم «ترامپ را بکشید» در مراسم وداع با جسد علی خامنه‌ای:
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67274" target="_blank">📅 13:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67273">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2883f7592b.mp4?token=uix4Ydv5n_N8CzJ7LFMWgHz-XOIyX9aX-ncM7d4IV0VleNDBtqPASRcvtVlYZnXxcXx_eGwlEUlX81aA8bExtrQ0hloT3meKytYh44XTQYSWYST1D80LryIcvTLbBQrEk_y2co-aoP8f574nloVgj6XuyYZtY-mp1Ff-cWBo1k7aTXej4kj5Xx5yiDonO9JuyAvYTPmuuEHHVa7yxod8IsM01Kg1vicwOB5z8qhmi9aNQGMwu8ore8tUPuNSTxembEIIv1ehmILuewnZp7RrkLX17wRc2ba072UOabq5YV_QAboUz6ihIwRQM874pQRMlXYKtlcHryBcQgpwOrnqKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2883f7592b.mp4?token=uix4Ydv5n_N8CzJ7LFMWgHz-XOIyX9aX-ncM7d4IV0VleNDBtqPASRcvtVlYZnXxcXx_eGwlEUlX81aA8bExtrQ0hloT3meKytYh44XTQYSWYST1D80LryIcvTLbBQrEk_y2co-aoP8f574nloVgj6XuyYZtY-mp1Ff-cWBo1k7aTXej4kj5Xx5yiDonO9JuyAvYTPmuuEHHVa7yxod8IsM01Kg1vicwOB5z8qhmi9aNQGMwu8ore8tUPuNSTxembEIIv1ehmILuewnZp7RrkLX17wRc2ba072UOabq5YV_QAboUz6ihIwRQM874pQRMlXYKtlcHryBcQgpwOrnqKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش نکیر و منکر بعد از ۱۲۰ روز
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67273" target="_blank">📅 13:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67272">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGwBT1plqeeFOzHTRkNHKGXxAuyq4Nktsx21G6StV37ckkSBMGvfIpEPJnx_VOILS4Wf7pHVX6UgiORKY0orXNocUZvpY-hm2aoBJemMCM33MRZ5oF2Ab5c4dLfJhFRJeO5Owk9mxSqh-C0XzCt805yTCD4U2abtOGjcITf5Sfhcg4gPptHxqkKkpuIxy5IpUIUgS0N3sPgykMmIbGousrLS0WLKHRmvGlyfUGn68iJ0BU3hTOSisVpsklcH28swrfQ0UjrbrywCtlUbJNil-oNKtixJkC5Sp70KvnE-UffOPecBGonBH7-dRonijAzKeWspFNr-KCNng4sXSLl7fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
التماس رسانه حکومتی در ایتا برای حضور در مراسم ؛ جمعیت کم است...
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67272" target="_blank">📅 12:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67271">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc8da4a29b.mp4?token=NRuvMalvYJWakJtDvLr2SjALGS5JzTVxHTI3Kbz5JxLJrn-JEcwwWQVUDV9HpFPf5lcxHV3AojsmQwFlNK_-hhE5c5sIuXggHdwh3yox7b79jnhYEx76wme-w2WbbKd5WaD9DOh1LCk4poKK6JUm3hekFP6PyqbWFHyDWk_jov9OeZIk1Z2qUvwZpg-cuTiLmJCSEbfxjEN174sWUGGUxIvGkQHhDi04LkQsjDWtiHwI9hugr59GoELsz8wmd4srOdBvfd4sBu-BCzac9u9xxSWDd-qBdC8dJiUQv3dmz6eHa0Bsejq5bF4mgve_pMR8yIm9iO7fAGGG6ocrBf0QqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc8da4a29b.mp4?token=NRuvMalvYJWakJtDvLr2SjALGS5JzTVxHTI3Kbz5JxLJrn-JEcwwWQVUDV9HpFPf5lcxHV3AojsmQwFlNK_-hhE5c5sIuXggHdwh3yox7b79jnhYEx76wme-w2WbbKd5WaD9DOh1LCk4poKK6JUm3hekFP6PyqbWFHyDWk_jov9OeZIk1Z2qUvwZpg-cuTiLmJCSEbfxjEN174sWUGGUxIvGkQHhDi04LkQsjDWtiHwI9hugr59GoELsz8wmd4srOdBvfd4sBu-BCzac9u9xxSWDd-qBdC8dJiUQv3dmz6eHa0Bsejq5bF4mgve_pMR8yIm9iO7fAGGG6ocrBf0QqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
ویدیو ای
از بمباران بیت رهبری9 اسفند 1404
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67271" target="_blank">📅 11:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67270">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccea9f87ad.mp4?token=VXdvt1CxVZDvKsJ3x-Z68NlE90QmcDeprLYVEe2aKh6MzoU9oJWqlcV33pe3EQxZj6nuIIX5jpz6dEQ0GGOfJTwJeQLM5daZ5_FwwTG_28ddELygpLY9VGfolxr1K3Oqd2rfENYHyj35ri0YHCZXPW4o51f_QcFHq2nCRbrB13J9PFbKThMOu4iAtJV_U9aAcns-HBLvjn0EmMzBoD0phUa9EDXVCe0vJarX847ya_5Ew2Sep5NPBwZV4iK4JT44CFvwSWiFDHtj5HXpzHZSg7uqmlkha9M5JygywgxmRrfcP5QrJZkLngodAPs9aUzy6Fyruksd-JocuXRNcPqRvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccea9f87ad.mp4?token=VXdvt1CxVZDvKsJ3x-Z68NlE90QmcDeprLYVEe2aKh6MzoU9oJWqlcV33pe3EQxZj6nuIIX5jpz6dEQ0GGOfJTwJeQLM5daZ5_FwwTG_28ddELygpLY9VGfolxr1K3Oqd2rfENYHyj35ri0YHCZXPW4o51f_QcFHq2nCRbrB13J9PFbKThMOu4iAtJV_U9aAcns-HBLvjn0EmMzBoD0phUa9EDXVCe0vJarX847ya_5Ew2Sep5NPBwZV4iK4JT44CFvwSWiFDHtj5HXpzHZSg7uqmlkha9M5JygywgxmRrfcP5QrJZkLngodAPs9aUzy6Fyruksd-JocuXRNcPqRvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سر دادن شعار مرگ بر آمریکا در مراسم وداع با جنازه علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67270" target="_blank">📅 11:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67268">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0d436c597.mp4?token=E-ZeTWWer0Z6DkWwcPJTExGmUEkEB7GxVysd4kIoKQw_KIA_ATPcUiv8WLYxxucSNJNp09_4iUNy857vpJx_j9r6wA83oWEMUU9l1BI8zGn-HDmmZtB8-KX4yZOE2qabz_NOpXJqfJ-OmLuPXqu7n9MToOFWkNqcwLufWUNbDCnPN8uJhFuZNKvBwN8qHLM7RzVFvpC8c9D06Sdpfe35YVMS9Q-WC6HCgMoTj-SxqJ9Cjs-OyylEtTdYJlPJxWKeMeGbqwLkSBbtRxxPY1UTdRyiFrFIiOIeZ_ShZ8-nFclv7h0yJLDb0r56OMbUy3KH3MQ3J4PxjJnLRt00D8AnsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0d436c597.mp4?token=E-ZeTWWer0Z6DkWwcPJTExGmUEkEB7GxVysd4kIoKQw_KIA_ATPcUiv8WLYxxucSNJNp09_4iUNy857vpJx_j9r6wA83oWEMUU9l1BI8zGn-HDmmZtB8-KX4yZOE2qabz_NOpXJqfJ-OmLuPXqu7n9MToOFWkNqcwLufWUNbDCnPN8uJhFuZNKvBwN8qHLM7RzVFvpC8c9D06Sdpfe35YVMS9Q-WC6HCgMoTj-SxqJ9Cjs-OyylEtTdYJlPJxWKeMeGbqwLkSBbtRxxPY1UTdRyiFrFIiOIeZ_ShZ8-nFclv7h0yJLDb0r56OMbUy3KH3MQ3J4PxjJnLRt00D8AnsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای از پرواز جنگنده‌های اسرائیلی بر فراز بیروت در مراسم تشییع جنازه حسن نصرالله دبیر کل حزب‌الله لبنان بین سالهای1992تا2024!
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67268" target="_blank">📅 11:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67267">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64adeed1d2.mp4?token=RDwBGX2inBaX5kjHkU0Ogj2d8AEHPGnZpiM_3-hhP3_Si6vRFgv9MhHkCxl6iheXqmX0Ky8fDJEvTU4NzrA-5T71hZRacT26PVioOs9tDRWk1RYdNGrEVapCtaDhpLdpSWS0WbVNXtoef9Lenx_m3JZIWhdaaUniJVJ5aA0-bKIZqYuif-w9sUAlBbqUxpbL4S0XxoAVZeKEb_LrfTn91vSZyGCWUrebtwwHrf2rafMxWNEgaxsuv3I7JX1gufmF3gNzv8VNIKgZjzrJNAc2_LIltgc4EA4F8yxxvXb3CEBAgADQPxewS4PzsMq2sHF6OeH5WIsqR-A4ANUbmxkW5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64adeed1d2.mp4?token=RDwBGX2inBaX5kjHkU0Ogj2d8AEHPGnZpiM_3-hhP3_Si6vRFgv9MhHkCxl6iheXqmX0Ky8fDJEvTU4NzrA-5T71hZRacT26PVioOs9tDRWk1RYdNGrEVapCtaDhpLdpSWS0WbVNXtoef9Lenx_m3JZIWhdaaUniJVJ5aA0-bKIZqYuif-w9sUAlBbqUxpbL4S0XxoAVZeKEb_LrfTn91vSZyGCWUrebtwwHrf2rafMxWNEgaxsuv3I7JX1gufmF3gNzv8VNIKgZjzrJNAc2_LIltgc4EA4F8yxxvXb3CEBAgADQPxewS4PzsMq2sHF6OeH5WIsqR-A4ANUbmxkW5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مایک والتز نماینده ایالات متحده خطاب به نماینده جمهوری اسلامی در شورای امنیت سازمان ملل :
🔴
اینجا تهران نیست که بخواهید همه را خفه کنید ، اینجا آمریکا است ، اینجا سازمان ملل است. این اسناد حملات شما به مناطق مسکونی بحرین است که دروغ نمی‌گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67267" target="_blank">📅 10:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67266">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b206a5500f.mp4?token=Ao51biJdUamppGssiEdafjSwHKXZflb-HUzYhonEfkgSRdTzv4vl7870nRDj13OuYrx650cj2hon38zxCikcI4kvRWNFOD0mtnttswlg14Uc6PeMoqov1AYmdNVUKqJ-gHSs9a9djLZA34-O-gSx86JeaNw9IGqr37bXsfFKG0wXucnbZ6T1-gJEkQKhIgcMhydr8JmCmRjBrpofo_jBX7J5-un8G63eJLKSvJirn8t6lVlD7IXKyTpx3YjaVqI5L4_6Zsdudx_UvO5MwMmO7UW0daA3g-nPpGMZyGqwd-ahCBmgE8Fj8xvli8gutWNv-e8U3UsrKmu6dNbqAqdAPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b206a5500f.mp4?token=Ao51biJdUamppGssiEdafjSwHKXZflb-HUzYhonEfkgSRdTzv4vl7870nRDj13OuYrx650cj2hon38zxCikcI4kvRWNFOD0mtnttswlg14Uc6PeMoqov1AYmdNVUKqJ-gHSs9a9djLZA34-O-gSx86JeaNw9IGqr37bXsfFKG0wXucnbZ6T1-gJEkQKhIgcMhydr8JmCmRjBrpofo_jBX7J5-un8G63eJLKSvJirn8t6lVlD7IXKyTpx3YjaVqI5L4_6Zsdudx_UvO5MwMmO7UW0daA3g-nPpGMZyGqwd-ahCBmgE8Fj8xvli8gutWNv-e8U3UsrKmu6dNbqAqdAPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚬
وقتی تو ایران میخوای پیشرفت کنی
واکنش آخوندا:
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67266" target="_blank">📅 10:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67265">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b88ddeb40.mp4?token=hMnJWOEHcaGmPr0scBokTfVoAVDCCICw9Xo8r_FMyNywhyz966IlUXq8WmkNX_pZFZXLq7U0yMTQi8o54lg3haCekoXpehGXpZHeV5AiQMqJlC__5qWM3uq9wimriJ0wrO3p-I1R9P2mRwS-Mgxvrt-Gt0Bwro_Gxwd_JztBQUvQtN8w7w4FmzUIP3vzSpjo_t1gTAf0W_AYo41uTFJrkaMzOH3ZEH9EZ_a2SqJS3AHYNHakS4XXl1k5mdGp2zdXRztdBIsBP9y658Rjpn2CwVRiyCjHn2WNaRmP6lxUU8_sIGlnYweNgzO7NfDxO2SA23Q3lkKTQRz3m6V4B5Xhzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b88ddeb40.mp4?token=hMnJWOEHcaGmPr0scBokTfVoAVDCCICw9Xo8r_FMyNywhyz966IlUXq8WmkNX_pZFZXLq7U0yMTQi8o54lg3haCekoXpehGXpZHeV5AiQMqJlC__5qWM3uq9wimriJ0wrO3p-I1R9P2mRwS-Mgxvrt-Gt0Bwro_Gxwd_JztBQUvQtN8w7w4FmzUIP3vzSpjo_t1gTAf0W_AYo41uTFJrkaMzOH3ZEH9EZ_a2SqJS3AHYNHakS4XXl1k5mdGp2zdXRztdBIsBP9y658Rjpn2CwVRiyCjHn2WNaRmP6lxUU8_sIGlnYweNgzO7NfDxO2SA23Q3lkKTQRz3m6V4B5Xhzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
ما ایران را حسابی درهم کوبیدیم. آن‌ها برای توافق لحظه‌شماری می‌کنند؛ به‌شدت خواهان توافق هستند. ما به خاطر یک مراسم خاکسپاری، یک هفته به آن‌ها مهلت دادیم، چون آدم‌های خوبی هستیم. واقعیت همین است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67265" target="_blank">📅 09:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67264">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb8124f389.mp4?token=PWdtbLcDSidfZwgFFDNv0ZWPwELy2goQYGhjJ1enpZRR2QxpVSACHfkHNDf15V8T5-QfJwZPbv6qR38qVbZkvwoYiHAn1vlvO3NT8ELR03dewZ78N1OAXhWwx7L1nYof9bumamsc0aIsoSuKWdLH0kTLpn_9sNm81LXyiS8DarVZ-HkbkT-tiCrxeMMuKGA7XmZ4UltbKSisr1TLAHDpssa5hnQPQzdWA3tDtJTYHNjpDean2baBvbM7fbeoYDvpWq3o0KCCMrX3bt2pwmIOpvJzSP41-TvGjkk_8UiFnXcBhcjB_jM3RzvpFWMUfEQPe3r4Ow1Gz9FdgqjewABgKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb8124f389.mp4?token=PWdtbLcDSidfZwgFFDNv0ZWPwELy2goQYGhjJ1enpZRR2QxpVSACHfkHNDf15V8T5-QfJwZPbv6qR38qVbZkvwoYiHAn1vlvO3NT8ELR03dewZ78N1OAXhWwx7L1nYof9bumamsc0aIsoSuKWdLH0kTLpn_9sNm81LXyiS8DarVZ-HkbkT-tiCrxeMMuKGA7XmZ4UltbKSisr1TLAHDpssa5hnQPQzdWA3tDtJTYHNjpDean2baBvbM7fbeoYDvpWq3o0KCCMrX3bt2pwmIOpvJzSP41-TvGjkk_8UiFnXcBhcjB_jM3RzvpFWMUfEQPe3r4Ow1Gz9FdgqjewABgKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده یاد مانوک خدابخشیان:
آمریکا یکی از داکترین هاش برای به زانو درآوردن کشور مقابل اینه که هزینه ملیشون رو بالا میبره مانند شوروی که همینجور کمرش رو شکوند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67264" target="_blank">📅 09:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67263">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">⏸
مستند کامل و 46دقیقه ای شبکه 14 اسرائیل به نام از «چشمان جاسوسی در تهران»:
این مستند جنجالی دیشب از شبکه 14 اسرائیل پخش شد.این نسخه زیر نویس فارسی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67263" target="_blank">📅 09:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67262">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/i6ecCrfa0k0CtT76AbJOvZFXMc_WON8L8dbC0Y7CveIuwQciu837JIQPq_GfhvlPkd_BKJf2nFMUdIOsyKd58a8JVQyJJb1_M8Xc3nKKKpL6xuxp_CCxqeq5MsJ9wTAS-VU46RBL52yyFjckSBIGvmP_bjh1F5GQqAXJE_XWtXj3XR855zFxiOM3ByvalfzogE1cZDFkh03GsmrFuFnUy9WHF2x8T-3EbgJP6RBfeKVHEP6mW2GZb3kaWhM5Xl1tWbXTmmsMkPFchf7uFZbJHLdVSDexisJw1vgVlxf2JGw0gRgZx8vvXEeiCSFGnBgMfEA9NbMHpFosjIaUV9LDxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
انقلابی در صنعت هوش مصنوعی
🔥
🔥
🔥
🔴
میدونی هوش مصنوعی ترند دنیاست و اینده ی اقتصاده ولی بلد نیستی ازش استفاده کنی و درامدزایی کنی؟
هوش مصنوعی TimeTrade این مشکلو حل کرده
✅
هرکسی با هرمقدار علمو دانشی میتونه ازین هوش مصنوعی استفاده کنه و با سیستم auto trade به صورت لایو و روزانه درامد داشته باشه
🔥
👇
https://t.me/+hcwmoHXpF6k5Y2Q0</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67262" target="_blank">📅 01:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67261">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@Vision_Bet @Vision_Bet @Vision_Bet @Vision_Bet</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67261" target="_blank">📅 01:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67260">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sKBTO32rdsAzY0x6QStqNajxBcS1eYQmmYaeDN_uEMSsJYreVKdeqNJ0hkPx-KK3DMtMF4lVwn9MkDvUrTVIGASN9J7je06pXbTqh8soAmi7NT4LLWA3FDweCtOMWWNbRfSnL5fITDHdBDe7XKESvqTc5E8C2ngzX6TcVxSdIJIkYunSDrCV4vgOYwuF16p01BhzchGbX-QbZz9aQ3D7jclj_KK-QaP02V_HWXq_RO7pjah7ZpWVKzbjLD9lkMniA29Rslfh0NHlF1-K5ADLkJxZx3Seq0zoDPio4E2DMHNQhrR9lJ_Zb31381DsrduA9d6ylb5cfxeA3S7V2gdAkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@Vision_Bet
@Vision_Bet
@Vision_Bet
@Vision_Bet</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67260" target="_blank">📅 01:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67259">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی ارتش اسرائیل:
اسرائیل آماده است به صورت مستقل با جمهوری اسلامی وارد نبرد تمام عیار شود.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67259" target="_blank">📅 00:53 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
