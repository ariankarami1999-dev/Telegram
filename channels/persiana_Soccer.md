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
<img src="https://cdn4.telesco.pe/file/tZ1CiN2Qtmi1p-7tx9iFkCrLSN0ZyybLcO1J49ho7ZJHIdzNTU-X7cZBlxC8xryoYRAQBxRm3I0QZTQ_f4zXJnZKE8KyFe--_12N13iVYz49FGHAMbBh9n63JfvePFo_MdSMWZFhWZS_5nc5p8pCnzPAhDz20zJyhv_RKapKNTDPc-z2Ahb7EkLHaO5DIhchLR6kDkZl9kq73MXUnGOewshSZER5N5_1rwIA4B9YBdijpDB19nbcoAOiIRaX73WORcUGYPX5WqqSU0PX-HCO3QfwiQQ0eYMvtL9_1zKz7kmkDjSSdoImkDHfS_vGfCfQcJTCEZXRfxFTTRJxIo2oBg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 354K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 17:41:53</div>
<hr>

<div class="tg-post" id="msg-24755">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRq2fCDXZuftFze_hnX_ozeAyhB30sAiQlJX-RcIRziXO1ddeeFSKqvzqLk7jGIWg6G5qJ0a-oiWIzhTXYQh6n-w7JQdB65yQsSjD4kxsOt9BgOhkI4PVoJcuptmbuSJCkoBHdaZDywMzRmTfnDzHshtMPbRuDa4oy4jQ6oyNnr-jrK5ih2nSe-xat3iR_S3NOt3FpqhQXhA4OhbeYvIblMoBNrbLcQ0rlDiTb3u49Q24A6OVdo60-7QymQFSkh_l3rm-aF5YMcM9hbSqBryTq2L2Y9LLQ50f2GM6i-nPDXJXuCEYxKdlumU_ueFwPnbNnppCa1mUsWTdFOxRuZ0WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ طبق آخرین اخباردریافتی‌رسانه‌پرشیانا؛ اوسمار ویرا دقایقی قبل رسما قراردادش رو با باشگاه پرسپولیس فسخ کرد و از جمع سرخپوشان پایتخت جدا شد‌. بزودی بخش رسانه ای باشگاه پوستر او رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/persiana_Soccer/24755" target="_blank">📅 17:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24754">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dba2ae9cd.mp4?token=vUTPMXYYQ86Ia6mPJ_-miqTxv4eOD52xkKDLBgTu5wMybTeYAyzIHYgxr8xED_oIGXXGoEJ919QLPoql9fA_QMFP6q5xR8xJ1KVM3oIQoGwr4QfdwKzV_-kuygcIIjxfLWpsl2XFphV4UZlMBzS6jg1Sbl5KSuKo5MWJlVqWonrDQluvyXNxPpzcXvUEJr_Y9DHGV77ory8RvSKgusk3tu_NhYg_lFnKCTReSV3HpmG926QWYWWsWkPqEgVjujqgu-mnhwlBKQbT6nzUIZISy8S4Gk_-OOwAUEaNOYZj0Nu1ZK6a3La_EOyUDBF0cf21D_jtTFB1cUbiudxqqbttan1rPo2K9fx6bucvQlbyNHiJtkBK_sIUIUIk6kxF6uGnZjC8xua27Yp-T2oEaEq2e0zp2Q9oAvkfqP-ec7ScvmImMBXnY1fJEkIpKQMDjp6WG0u-jf3azy7fACTA31EavD4EhoM_QJ3PEmLg9sNISq_VXl6Tp6l65hPke23t0DBthkSCqX97fGYOyjeUWsV8Mfr_4zmNiGVKjZhPbHZgU_uZQxAYi2CJIFXNjiP86yFI3XXA6EQv1IbprWOAzh8p1QZXJE7qxBFq6Bn3d9OaWyssRMh6lQ_6p1WluBmu92J4O1Hh5as-CrBVoJrE80GOO875OwRm2c4fkjqGrYRow70" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dba2ae9cd.mp4?token=vUTPMXYYQ86Ia6mPJ_-miqTxv4eOD52xkKDLBgTu5wMybTeYAyzIHYgxr8xED_oIGXXGoEJ919QLPoql9fA_QMFP6q5xR8xJ1KVM3oIQoGwr4QfdwKzV_-kuygcIIjxfLWpsl2XFphV4UZlMBzS6jg1Sbl5KSuKo5MWJlVqWonrDQluvyXNxPpzcXvUEJr_Y9DHGV77ory8RvSKgusk3tu_NhYg_lFnKCTReSV3HpmG926QWYWWsWkPqEgVjujqgu-mnhwlBKQbT6nzUIZISy8S4Gk_-OOwAUEaNOYZj0Nu1ZK6a3La_EOyUDBF0cf21D_jtTFB1cUbiudxqqbttan1rPo2K9fx6bucvQlbyNHiJtkBK_sIUIUIk6kxF6uGnZjC8xua27Yp-T2oEaEq2e0zp2Q9oAvkfqP-ec7ScvmImMBXnY1fJEkIpKQMDjp6WG0u-jf3azy7fACTA31EavD4EhoM_QJ3PEmLg9sNISq_VXl6Tp6l65hPke23t0DBthkSCqX97fGYOyjeUWsV8Mfr_4zmNiGVKjZhPbHZgU_uZQxAYi2CJIFXNjiP86yFI3XXA6EQv1IbprWOAzh8p1QZXJE7qxBFq6Bn3d9OaWyssRMh6lQ_6p1WluBmu92J4O1Hh5as-CrBVoJrE80GOO875OwRm2c4fkjqGrYRow70" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
برسی‌کامل‌ودقیق‌شدیدترین‌مصدومیتهای مرحله گروهی جام جهانی 2026؛ عالی بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/persiana_Soccer/24754" target="_blank">📅 16:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24753">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bce6bf7fb.mp4?token=KHEsPo2TEIpHe0zC_AtwSGCqE_Jms9BHb8o1yBbXdGlu3C46nLnp1j6hAq1WHgvVpGxIoJWoTJ3K5FOt6i5QqJ8nPGT97cNW9jJU_tJqEBqcP0lIG-42vbpDx1pt747bVINWukCgpzQ2c00mJ7ogLYfmTc0a5PtNn8cUS2-qoqGI45OKFhfnSHkLU17-S2CRllohfccXZgg0Wj9C_x_-d-H8fbrXEaJAtv7iqlS4ILeAK5FeKuieZ_rZP6cp6DZrgDRcP7LMEqVzLkMMMJAiLMlfod7PPDSpaNL95vCGaU8jPDjX5Ggrl8axz3U6SVb9ikkL7U-zwdnN44fMaZHE9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bce6bf7fb.mp4?token=KHEsPo2TEIpHe0zC_AtwSGCqE_Jms9BHb8o1yBbXdGlu3C46nLnp1j6hAq1WHgvVpGxIoJWoTJ3K5FOt6i5QqJ8nPGT97cNW9jJU_tJqEBqcP0lIG-42vbpDx1pt747bVINWukCgpzQ2c00mJ7ogLYfmTc0a5PtNn8cUS2-qoqGI45OKFhfnSHkLU17-S2CRllohfccXZgg0Wj9C_x_-d-H8fbrXEaJAtv7iqlS4ILeAK5FeKuieZ_rZP6cp6DZrgDRcP7LMEqVzLkMMMJAiLMlfod7PPDSpaNL95vCGaU8jPDjX5Ggrl8axz3U6SVb9ikkL7U-zwdnN44fMaZHE9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های‌فیروزکریمی‌درباره‌مراسم فدراسیون برای استقبال از شاگردان‌قلعه‌نویی: اس چه تقبالی؟ خودِ فدراسیون از این کارش خجالت نمیشکه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/persiana_Soccer/24753" target="_blank">📅 16:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24752">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRnw_GU1CytL86oa5O7CG0tOlyL69GvoDfJehcNntEwngaPuomeDvaHP9Y14RhoamHHkOoGKvsvQH0BA0ooyY-0xP-Zf5ahHMD34oIOjVxH1kyyar5hVCbYw6rEFg3KOlvMWlvtsIrmP7mZFdp-o1jseskgjopA3o6_78Rm5rfjfrK_XYVJRGYM2WFUJtPJDmpYduic4qeBk-8bWyMHAw4_y33irZf1ybed6NdSkASsX3PryfwRNv_LbPZxn0MnkQEtEh1it3TMg9yPIDovlfnBsgdauRPji6j7011_s91APQfPXFAf5ZzcY1kxawlStE2A_q3y4zNRDybaMov_OTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ به احتمال بسیار زیاد بخش رسانه ای باشگاه پرسپولیس فردا پوستر رونمایی از دراگان اسکوچیچ سرمربی‌جدید خود رو منتشر خواهد کرد‌.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/24752" target="_blank">📅 16:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24751">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdee128ed3.mp4?token=DicaOTwROlBfv_Mm0qCKAi1ImVwnT4gX_yO13MWqUDw0XrzoTZCTbxeUMAdGmQ9urj6xUFbydxc5GE6UqU0cJPUFuZSSfY8I4xycpaANH4mXWfxowV5BZOUtB_c-l0YYusXe_5xci1coOe1yn6vdGesoObdRgnpPcl5ifmRj2oN3SHoECkZcvvMgaHC3GOt9GPAWLY9Q1YwHZZTrk0WmLvlZRvLyPmELEMogedZHqZssmlP4gieC-hsqpFVg_pGLQWf88S1hLMi3F0JSlCo6zovIuw9vrXf62cCkIbUbPshZtcJ-1BZ-fs0rlCL3MH4zJCHEyJchDa1bC1b0rRGRPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdee128ed3.mp4?token=DicaOTwROlBfv_Mm0qCKAi1ImVwnT4gX_yO13MWqUDw0XrzoTZCTbxeUMAdGmQ9urj6xUFbydxc5GE6UqU0cJPUFuZSSfY8I4xycpaANH4mXWfxowV5BZOUtB_c-l0YYusXe_5xci1coOe1yn6vdGesoObdRgnpPcl5ifmRj2oN3SHoECkZcvvMgaHC3GOt9GPAWLY9Q1YwHZZTrk0WmLvlZRvLyPmELEMogedZHqZssmlP4gieC-hsqpFVg_pGLQWf88S1hLMi3F0JSlCo6zovIuw9vrXf62cCkIbUbPshZtcJ-1BZ-fs0rlCL3MH4zJCHEyJchDa1bC1b0rRGRPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#نقل‌انتقالات
|شهاب زاهدی مهاجم سابق آویسپا فوکوکا به تیم‌جوهوردارلتعظیم قهرمان فصل گذشته مالزی پیوست تافصل آینده در لیگ نخبگان بازی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/persiana_Soccer/24751" target="_blank">📅 15:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24750">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‼️
دیگه وقتی سرمربیت اینجوری بهت تعظیم میکنه فقط یه بازیکن ساده نیستی؛ کیلیان دیکتاتور
😂
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/24750" target="_blank">📅 15:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24749">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b031fa7a0.mp4?token=cl78DbGVKdChXjVzJxyTBFzU8vuthMM45JDPZ1VxYst6j33lwnJfd2m3FZxLOzPStywNmZUUgH9s1v7wt1guqBq0owugpD2iYHaTrHpMlL4HPBRCCioJzvfQEwWJo6ZAt6LkYGbJwqAWVj65hzH0GUQ5OUeHoA0UEf_1-WDLAwYaOYnHjGYa43SdaVTPnwx1_1kV5_WobGE-9CcpGRsf2mzpvRdj1TWwpK1S6W0IYHXDQnisUhqIHYjLw5r_bWTl86vzBOvsi1lEaQpftknt747lHU3_6uYuQuAzIuBkGbnhzLvZ--FXwlZ-DVrP9eUefbTt6PcV0_C9MTI2y_YxBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b031fa7a0.mp4?token=cl78DbGVKdChXjVzJxyTBFzU8vuthMM45JDPZ1VxYst6j33lwnJfd2m3FZxLOzPStywNmZUUgH9s1v7wt1guqBq0owugpD2iYHaTrHpMlL4HPBRCCioJzvfQEwWJo6ZAt6LkYGbJwqAWVj65hzH0GUQ5OUeHoA0UEf_1-WDLAwYaOYnHjGYa43SdaVTPnwx1_1kV5_WobGE-9CcpGRsf2mzpvRdj1TWwpK1S6W0IYHXDQnisUhqIHYjLw5r_bWTl86vzBOvsi1lEaQpftknt747lHU3_6uYuQuAzIuBkGbnhzLvZ--FXwlZ-DVrP9eUefbTt6PcV0_C9MTI2y_YxBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یه‌فلش‌بک بزنیم به این صحبت‌های مهدی طارمی بعد از دیدار ایران - ازبکستان در کاپ کافا: اگه تو جام جهانی پنالتی برای‌مابگیرند من نباشم کی میتونه توپ رو گل کنه. جز من هیشکی نمیتونه پنالتی بزنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/24749" target="_blank">📅 14:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24748">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RhtbR9qeh9prcM24m5ScxjAF1n0l4_ZVTIbjGZ-84A9hwA6D8b9YD98npou6_wsgJachA0_4ePHNL9TeE7F1UQpen3QOfWGnTMvlQr0D53dDbPBboRbK0a5ukgc0tXCj6aHWnpicQ6aOYS9zc79YZKJQ5JY8I3Y9UphLs8DkP_Bt6zDcl60Vr1ZnoIQb98BcR8DywdU9woqdrMRqyd60MG0OGYqX28LZogwM4Zy65Bf8i-ivJDSQPshAT9aPenb_siYTfDmIqWKXHwpoPmrzsLtu78rJ6Qf68srxce6EwnvXcMvzRYwiZGUFG6c7QwW0NxCqB3UWH4kC_nZx6vnpGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرمربی اکوادور که خیلی عکسش از لب گرفتن از همسرش بعد برد جلوی آلمان وایرال شده بود، بعد باخت جلو مکزیک استعفا داد. اونوقت فدراسیون ما برای‌حذف‌از آسون‌ترین گروه مراسم استقبال میزاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/24748" target="_blank">📅 14:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24747">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrsXn43jIztpHSZgNdu2NvMZ2F27R86l2uIOIJanMRpBU-Cj74m2myE_yV4qV1eaU8G3fS7jDx0EZJYKFfxCQJms60UIdd-hwCPVxfCv9jH0OVsnx3_rIbAh9JK1ucgOjfwxogQFVi59fDJTB8Rii-D14Xsts_MlP9TqmIm5zt4r5Oql4gND0EwoGp8WHrlxk9QyRMeRqNMguJGFC3rVA1Ja6YYQnlZ3LqOoivhY9xtFk26ZfRrUtphLK2OP_blKzr20OyDvPy7e5CCkyMywh0CSJtLvmT2dGZWaGaCO86_QlmLAK3QkHyXabOUaaG6LBpA03WTDxu9g0MrlxuhqWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به بهانه تمدید قرارداد هنریک میخاریان با اینتر میلان به‌مدت.یک فصل دیگر؛ یادی کنیم از روزی که او به ایران اومد و در تیم صمد خان مرفاوی شرکت کرد اما این سرمربی او رو به دلیل جثه ضعیفش رد کرد. خدا دوسش داشت‌که مرفاوی ردکرد. جالبه بعد از اون اتفاق میختاریان…</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/24747" target="_blank">📅 14:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24746">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XB-hH--4xNvW6DXy_FryZMXSay6XXmVnArwoRRdSx5Dk0R3AMtupTVEEeL4Nb_m5THZljkldfsPeeXSAnvsuitl0VeAcKiaICvcnOV43n1_5ApDVRNpBSC-FW3ua9g5L6DQSqBUivHT9f8qlKk7NohIWs7-il03jnq6uftU_EJfrA8UMEA7BybMZ2cxUXV00rRMYIq6Yx0qFtPdZsTyy2bf9HMOgyKs3g91VrULrWuMakHg64nPErNrKULxecqtD5t1cusq8fbcge4MiM44bnq1eRlXyeBsFlaRM6mBn3mL-AGC3_rgF65yh3-3wEmAeNEXiCSucw6-SVijkFhRm1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به بهانه تمدید قرارداد هنریک میخاریان با اینتر میلان به‌مدت.یک فصل دیگر؛ یادی کنیم از روزی که او به ایران اومد و در تیم صمد خان مرفاوی شرکت کرد اما این سرمربی او رو به دلیل جثه ضعیفش رد کرد. خدا دوسش داشت‌که مرفاوی ردکرد. جالبه بعد از اون اتفاق میختاریان با باشگاه دورتموند بست.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/24746" target="_blank">📅 13:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24745">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPre9ioh-hKOJgI44WR59pZv5Vsm_kptPaO42V2FF79ueg0rai5VtSMMCG3FTJ_9lTsNb6-EJzmo3dv8xuIya2kbu0n2RVrjVyC8t1FGcOsjUO0fiW2WOA-AGzYpjp3CI8iM5iPLnUsCfqaxDweq_-S1QfvW6XBv4fLOY83muluyfPJeJ_4Hjhgby0BKIleA9Zm5wKaDRoB1ysoZxPcsv38PsNWiW2UXjY32LcAZSdPPHwG--ZStkShDg6gGM5E52H1XeLgdia5XghbPJHa21w8QwNdRMABxijX8LN8FqnilL2MDY9eA1DAZAObgbmwscpuFYwbi1IaQvPVLOpG-ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا بیرانوند دروازه‌بان تیم تراکتور از شهریور ماه سربازه و احتمالا راهی سربازی خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/24745" target="_blank">📅 13:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24744">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16504ba5c1.mp4?token=efHD2zE_n4hZzSQI77dvR-c3BQoR37mvSGgaqZcTUXp108BM2lqa9pjfvN_oIyfZty8eHxugl4KEp2gJjk-psnpHGdQj-7uDGUtBnkoo8IGa7jC-Jb9EvQgnOcA_5lRLVcOwE5sBNDM6Q_jfUGKcjqCg0PJpM1J_sT-eeiFKJu5ollCyGfHFpY92Djh_EGwrGXZy7xsMDz_CAsaLvW9FT3k9vmdRhdYdeqUh46yCLDQFUAZHs9m86a492u_8cF0INQi_wQ8X5av-_uz-VARKo5ftCo29J1Lk6BY6oRZMhD5yOCXdl9wRcROdoKZcqMx49rJV73Stx3e-yGhNMfYRCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16504ba5c1.mp4?token=efHD2zE_n4hZzSQI77dvR-c3BQoR37mvSGgaqZcTUXp108BM2lqa9pjfvN_oIyfZty8eHxugl4KEp2gJjk-psnpHGdQj-7uDGUtBnkoo8IGa7jC-Jb9EvQgnOcA_5lRLVcOwE5sBNDM6Q_jfUGKcjqCg0PJpM1J_sT-eeiFKJu5ollCyGfHFpY92Djh_EGwrGXZy7xsMDz_CAsaLvW9FT3k9vmdRhdYdeqUh46yCLDQFUAZHs9m86a492u_8cF0INQi_wQ8X5av-_uz-VARKo5ftCo29J1Lk6BY6oRZMhD5yOCXdl9wRcROdoKZcqMx49rJV73Stx3e-yGhNMfYRCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خاویر ارناندس ملقب‌به‌چیچاریتو که در تیمایی چون منچستریونایتد، رئال مادرید، بایرن لورکوزن و وستهام بود، از افتخارات میشه به دو قهرمانی لیگ جزیره، یک قهرمانی سوپر جام انگلیس، قهرمانی در جام باشگاه های جهان و قهرمانی در جام کونکاکاف اشاره کرد، وی به دلیل طلاق از همسرش به شدت از اوج خود دور ماند و دچار افسردگی بسیار شدید شد و در نهایت سن 36 سالگی از فوتبال خدافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/24744" target="_blank">📅 13:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24743">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ob746JB0WeVNTF3h6qcimO651er4NBPIHgDyApgrv3U40JdzSBK7i--sOXFOmMfJIPfa_oNaDgT8DJqZxxijeCuIP3oacWYxMfedKwsuWNZM4LfTWU2ECWtx09XsWjVgrD8vlewJes0AzojFJLsajKIu4k8PxCIGWqXbLwuJE-GL7df3yvb-XTm0c9hzcoHg1zmvgDts0PHHS285xLW0mruDaRQCQNi4OYz4sB0hrMSgnQ0q7OXIr24DZx0cCBpc-f4jh96LK0HyrwYp_YurlVNtMO78A5xttMODAPAAtLGp1tHQjh1jx_wK8pxYTxNoSN4AJGESy3T4D0R-O1AG2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛باشگاه تراکتور به‌ سید حسین حسینی اعلام کرده مدیر برنامه هایش روتغییر بدهد با او قراردادی 3 ساله امضا خواهد کرد. پرشورها قصد دارند در صورتیکه علیرضا بیرانوند در این تیم نماند با گلر سابق استقلال قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/24743" target="_blank">📅 13:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24742">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rz4eyzebVm5kHOPACGjyRJiAoKLCpVgh62rBG8K7d85g0RBNVbARhpnm-Oni1CQxKu2l0XYFJMdHhNwI4mvAk8dYJLXqLn8neAlVMRZnKAPyAbRfhfCLS1BaL7UZ23q2H2gRKWQlb-uX9CquuQtgezDDjcS_5UJ7NuqhDXhUtgpmlruDShL8KHQT8Aw5-lmb87GbhA8z5h4tcUsMcEawTVuTgA6PaOdszHy__NqjR46Kuh7Sfew79ht-Letja7TtKqo4emCcgEboy2EOswlbPimGVUaVU1FHdaBy_j7J27tr3Z7Acnbr-5XLCQ9r88VWEYLAMIsirzXaIMNEdVI1hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل‌ سایبری ستاره مراکش در جام جهانی ۲۰۲۶ و بازیکن‌باشگاه‌پی‌اس‌وی آیندهوون که اکنون در آستانه انتقالی بزرگ به بایرن مونیخ قرار دارد، مسیر همواری را برای رسیدن به این جایگاه پشت سر نگذاشته است؛ او در ۱۴ سالگی به دلیل اضافه وزن و عدم آمادگی فیزیکی با…</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/24742" target="_blank">📅 12:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24741">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/290b5bc8ca.mp4?token=W4wtMGmHr9F5dKngkKMNH9V9tYcC1iKyaBJ2DGWL2MFLMLEzYbI0WXP0KFBSjypE193BjXEYOVPqUBq5AhQ_eECUGhUrrfF-DdGHUCN5dwRVhJeXU4a_StmGPtFWvGKvKRHZIoE3iQn_9r4Hea-YTQ13yzsPi1rtohJjS3erUn8QN4Lu4NcAf_kmYqQy_A6MbkmmZKQIMXti643wc_k80ZoDxbPndXJHsq2sb7B8iO47LOfNgoYgobdy0QLTqjcMIRFL4_4pg7j0ydQqG7X5O5s8GjrSQHRs0s5PKPrDhrzc6C-Bb6HQtbIS0NID6ntsRe34--s6x5OzWNEbfaKw6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/290b5bc8ca.mp4?token=W4wtMGmHr9F5dKngkKMNH9V9tYcC1iKyaBJ2DGWL2MFLMLEzYbI0WXP0KFBSjypE193BjXEYOVPqUBq5AhQ_eECUGhUrrfF-DdGHUCN5dwRVhJeXU4a_StmGPtFWvGKvKRHZIoE3iQn_9r4Hea-YTQ13yzsPi1rtohJjS3erUn8QN4Lu4NcAf_kmYqQy_A6MbkmmZKQIMXti643wc_k80ZoDxbPndXJHsq2sb7B8iO47LOfNgoYgobdy0QLTqjcMIRFL4_4pg7j0ydQqG7X5O5s8GjrSQHRs0s5PKPrDhrzc6C-Bb6HQtbIS0NID6ntsRe34--s6x5OzWNEbfaKw6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ته این داستان شد عزت یا آزمایش ژنرال؟
امیر قلعه نویی سرمربی تیم ملی در جمع مردم تیخوانا در زمان خداحافظی: خیلی دستاورد بدست آوردیم، این عزتی بود که خدا بهمون داد؛ وی پس از بازی با مصر گفته بود گویا خدا دارد من را آزمایش میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/24741" target="_blank">📅 12:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24740">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwyRuQIirGdXgfndOOwf2a1XJtJ_E7fAXhzyvesTkPDmhMb7ZnZpomFL7C0Z2g_JLAYJytqw95sNictfJNQfPXu7rlgglg2053fshV24D5S5SWYyvxZOsuV1jyyHVRWtgMW9DzBJphdQyo8Jm1lNftq6aD0-vkHArJIiKgwdutrxJXLUkJgjoMfBfDcnzMgwgLNb-4COCtaDIyMIWUPXpC8fuOhPYf0EpoxuSB8Zd_E3Wtu2QtxjIF73HWUuINsmtqzCIf52Mw2Gew5YLyawuFFqWHKe9Id8cv8Pe6Zm-0LRY0rgKIJpYRORu9ZfKWCxIS5xWqiNP0q8MzmEcFjX_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
فابریزیو رومانو: ماتئدس فرناندز که علاقه زیادی به پیوستن‌به‌منچستریونایتد داشت در نهایت با عقد قراردادی‌چهارساله به تاتنهام پیوست‌‌ فرناندز بخاطریونایتد پیشنهاد رئال مادرید رو رد کرد اما به یک باره با رقم فوق نجومی سر از تاتنهام دراورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/24740" target="_blank">📅 12:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24739">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLFMIRWy2Bbn9kltYxkND_ifcuVQMmXg9wIJNmXtzZkH2GH3HgOvnmY_zIaiLCgeubrbOra94Z-FeYIBrliROz3Xt-0mdNfQ8HV1mT-h_1yobRThjCNy2w8raGt4csO7VQBg2406RuEHf_PyztPGS1AkD1kREysLZNjSndL-Vg78YdSa3FQigiyacq7i5rEkErfXaTjeOsYxCTd03iKhYfX8xwr_Vm-QsWCTooIl5sDXne3f2l-IAL9HUr6GOMS24SYCM1JcqVXf29HDwbldQhbjbBa6XT6MvG9Bg3DzW4b-9PPPbdW04UKERzKSw4Ok0RsLO8uTujENT9i8RZ-F4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تقویم
؛ سال 2016 دقیقا در چنین روزی؛
باشگاه منچستر یونایتد با عقد قراردادی آزاد زلاتان ابراهیموویچ رو به‌خدمت‌ گرفت. زلاتان در مصاحبه بعد از عقدقرارداد گفت به‌جرات میتونم بگم که من بهترین‌خرید باشگاه منچستریونایتد خواهم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/24739" target="_blank">📅 12:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24738">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z46iLgyDfubLh61UGJFX4MvZTALScrsF-JS6Z__d4g73TNDpzivcH-FxKqcl7E3EgZBWw3M_lDZ7JyCY8ALXAd7okLhXJnt0INxRiO2Dzf4Tbm40Q1BYBOJ8q_HXZIV4IJcwhMwV-tJNWaw7KQUJVmvlkL9PMiv-zCVIQRWx4UW2R5MujcE3e-XP008Bw2RL8_9njrzSd9NyWdzBoAACBrLM7Q6xuxngeTWrxCKagffJtXbXbM0NMUaX9vH8fNqD8e3QdQA1Wr6NK_lYe_SiiIBDH8X4II_SSSaPrvZAzlkzzt57P-VKs7Y_-qlY9Yrerf_epDSCfv5GgzEIzhW2AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
اسکای‌اسپورت:
کلوپ‌ سرمربی‌سابق لیورپول درآستانه عقدقراردادی چهار ساله با فدراسیون فوتبال المان برای پذیرفتن سکان هدایت‌تیم‌ملی‌این کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/24738" target="_blank">📅 11:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24737">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_NRjHhyeueiwmdJCNgOrRnoy-eiQko1aQ5zeprmfq6dA1Cw6IY8KbTd8A0iamH0VTBlbGEPuXNrD5p_vzUbpe-2FZtCHzTsi2JauP6jlYae-kX0qa0UCaGJzCzn1YSmsB80ugmJ_Z5YGoW69Ov_R9QDAx5SCLnQZ43FN1_WREglfWynr8TUlsg9fS0a0Ffu1rhaSQPN6CbDtBGyNDv2-LrX04CRb2luvMCq7If_qhSAjSFTJGDZQwTN_6VBoWTk9vVm3LHL8ONaGIneSsfBEC1n9NxHiR2olPCkIqzFX4HZn7CLKiOhBOiWUUS-qKp_a0t9DE2xMb9J1z51GTC_iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
جدول رده بندی بهترین گلزنان تاریخ جام‌ های‌جهانی+جدول بهترین‌گلزنان جام جهانی  2026؛ کیلیان امباپه تنها یک‌گل برای رسیدن به رکورد مسی درجدول بهترین گلزن تاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/24737" target="_blank">📅 11:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24736">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc031d7910.mp4?token=sGB6aaVs9gZNjZyg_DF5PBDnQi9PyOk3fNk1IBH67EaGlBnuXA99gLQNbUzscC_p-pBm-oyX9_z0i3AEvy8WblfDiyuKfNLGzg-N4KwQ4nQDn-UrcP-ZQ4_czUmrak2BQEAHKvcWjFxi8zAIMLmnf8gwrABO9BK1zhnQxcMOGaXAiu6nDl4lelbK4B5bKmrOCym6Iah7_sGrilqyr7MXMD82pVXrOrX9ELqIzdfqgLNXaYZD5V0ZSDiidhM0whC2VXkMt5xuEmClvnbzIkDaMHTO2sAvHsxPeAji41-UETzSHL73gczw0khD9lf9AYTaxEMn4v4f45-I3doGdE52iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc031d7910.mp4?token=sGB6aaVs9gZNjZyg_DF5PBDnQi9PyOk3fNk1IBH67EaGlBnuXA99gLQNbUzscC_p-pBm-oyX9_z0i3AEvy8WblfDiyuKfNLGzg-N4KwQ4nQDn-UrcP-ZQ4_czUmrak2BQEAHKvcWjFxi8zAIMLmnf8gwrABO9BK1zhnQxcMOGaXAiu6nDl4lelbK4B5bKmrOCym6Iah7_sGrilqyr7MXMD82pVXrOrX9ELqIzdfqgLNXaYZD5V0ZSDiidhM0whC2VXkMt5xuEmClvnbzIkDaMHTO2sAvHsxPeAji41-UETzSHL73gczw0khD9lf9AYTaxEMn4v4f45-I3doGdE52iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه‌جدید آقای‌امیرقلعه‌نویی، سلطان اعتماد به سقف بعد از حذف از جام‌جهانی با یه ادیت عالی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/24736" target="_blank">📅 11:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24735">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbe8695009.mp4?token=sKo9RXdtSU1PJAXKD-a18j2PUyjy6r1Tx0Y0TEteOcecrsjjLPf715shImjr_1W1O1aj5Lpel-kiBs8cO2snU2dQEF9T-HRsz9ln9ey2K5oWa7V4larNu_SuSa_7zK-MqJhE4JRzRKh6pJuZwO3Y3aYE0XRlQNX8jeqowimgFIedjtYlXn-DzIOIMtbF3FLHZpjpBaepL78RlnglGS6cW0-ZhmjCOKFSvpwUuBjM--o6IFYdgGE0LgNQO9SckuFoEJB_8K2rGbsfDhFnqpZASuwyTvwvZh76SiO6aaHOKatfax4YI6O-izcFvh2GLJQQmDMiwddIfHEIxAJ3jI2-5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbe8695009.mp4?token=sKo9RXdtSU1PJAXKD-a18j2PUyjy6r1Tx0Y0TEteOcecrsjjLPf715shImjr_1W1O1aj5Lpel-kiBs8cO2snU2dQEF9T-HRsz9ln9ey2K5oWa7V4larNu_SuSa_7zK-MqJhE4JRzRKh6pJuZwO3Y3aYE0XRlQNX8jeqowimgFIedjtYlXn-DzIOIMtbF3FLHZpjpBaepL78RlnglGS6cW0-ZhmjCOKFSvpwUuBjM--o6IFYdgGE0LgNQO9SckuFoEJB_8K2rGbsfDhFnqpZASuwyTvwvZh76SiO6aaHOKatfax4YI6O-izcFvh2GLJQQmDMiwddIfHEIxAJ3jI2-5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
منصف مثل سید مهدی رحمتی
؛ ارزیابی حضور هشت ساله کارلوس کی‌روش روی نیمکت تیم ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/24735" target="_blank">📅 11:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24734">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/myOLGEiF7A9ziOEttpZLJ3Al0jx7iyiETdy3sIPhJEYWEw9Y-FBLSAzA_o0sdlxvWnMRSHFI_Wxf0VOmaTcgA3jVEPt_yZkP4fa0IcIpoaL0EIZjhsbmKp8i8VJn_XF-j2JyjIfClOUEXjAVs30LSmRyzgcFA42wnuVm4Ot_CedDPnIZmnMTcIMRLUVhf_gsLUVwhsC_r-lNax6pceQQP4eFLBNs9uBAqW95oA30rGhwvyukdTJbOn826Xsx45G93YHQxH0AqXDieqWI1ZsNfykGHE-csT6UgMDoLfT8YipoUBKpeXTq2bci3CGVwyEE7OTUQObuhRPHsDiIMDZFMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
توصیه میکنم بازی های جام جهانی رو فقط توی سایت بت اینجا پیشبینی کنید
🅰️
📌
اینقدرنتایج‌امسال‌عجیب و غیر قابل پیش بینی بوده که ما تصمیم گرفتیم به شما کمک کنیم:
🤩
🤩
🅰️
بابت هر شارژ موجوی اضافی بگیر
🤩
🤩
🅰️
کش بک بابت هر باخت
✅
این بونوس ها بدون
#قیدو
شرط و نامحدود هست
.
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
r10
@betinjabet</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/24734" target="_blank">📅 11:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24733">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcb_Lqvr5YtQjEDErz4S6vQSuIuZEs3RgakOC_u3kA6UK0i3uoLV8Vv5y3F9aA883V1nAjRUK48zvbn_qRWvIM21evfNJaAVd8UbdxVtKNsvBUMF-4UDxABd1n-87W-ORDRRomNy7X2Tm4UvqHI9r_bmHBqGd7Pfs6jkTQVprSCylOF7DZY36KCkQByZfaFTTlH2AHPEKG3c-OHLvIJ1r0O3kfZ8le8Qmsso5tBqw9ZMZ0NuntCse-u63PHq78FUteIkYLx5eday3fKzsDPc4Wh_teTlwfmAUTPzWIuSgbzHKP7zCpYum_gyZQ-2hN1sgHvvaUIUsWCrHykTid2VSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هلدینگ خلیج فارس و باشگاه استقلال برای پرونده بازشدن پنجره نقل و انتقالاتی آبی‌ها روی هم 850 هزار دلار هزینه کرده اند. وکیل ایتالیایی آبی‌ها هم‌امروز ظهر ایمیل جدید به باشگاه فرستاده و گفته شما تموم کارهای‌نقل‌وانتقالاتی‌خودتون روانجام بدید فیفا پنجره نقل‌وانتقالاتی…</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/24733" target="_blank">📅 10:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24732">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/118e0a09b6.mp4?token=g45jWN2Q8QV9ezA7ar65aja5cMsCoySYGyvlbwLEUJPLYR3wDwlbNWWlAkIpfdDlW5uArBgeWYaWHPipHrVPlE2BgrgTu7JZDpsle8Q6vE8Z1F6LExtusD5HDO0JV7nBCkl86d0jjtzSXv9VTuWRqOtFXXhhh_Qo1EJJAgpdxIruAbVu_yQf8GnW8Xc0YdYHFIT9aRcPoZs6zED3r77vO0GMG05c-D94HKh2JNaHIgUW9wwWPl2ioQCkkLzQJJshfDjX8bkrAA0FY8zQC-8bpYhbK3ICs1qyq1hJ8Yo67Hj0vqz7O4AYM_IE-0upcGVuFyvKeQauU6thfy-Lk04_Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/118e0a09b6.mp4?token=g45jWN2Q8QV9ezA7ar65aja5cMsCoySYGyvlbwLEUJPLYR3wDwlbNWWlAkIpfdDlW5uArBgeWYaWHPipHrVPlE2BgrgTu7JZDpsle8Q6vE8Z1F6LExtusD5HDO0JV7nBCkl86d0jjtzSXv9VTuWRqOtFXXhhh_Qo1EJJAgpdxIruAbVu_yQf8GnW8Xc0YdYHFIT9aRcPoZs6zED3r77vO0GMG05c-D94HKh2JNaHIgUW9wwWPl2ioQCkkLzQJJshfDjX8bkrAA0FY8zQC-8bpYhbK3ICs1qyq1hJ8Yo67Hj0vqz7O4AYM_IE-0upcGVuFyvKeQauU6thfy-Lk04_Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/24732" target="_blank">📅 10:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24731">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=JG4n5pb3ckofMgw0fBbW8uBmJVwUdPXvSUcxDvssKP7Ioa_xVQa9KhAGfVTM1PU2sswFIIZgZM7DH6HnIcLojbJ5O3IRk4M3jKF7ZGR2Yd3aIAtvwUxdBHqXZbx2Xebf9i0xgj1cVucKTutFvXIsZdAtqjSLiT3Hdj-S-SXLIGJZdrEm2LD2XyaK-xzzErjS7ydMavpVxqJ9GetqvYhTkcy8o2spYvZf-WNji_tsArKD1wihFNQwQP_rqqKtW2zIhYJKTJApofz33D7uJh7KB5g8U2KdYwL4lsKDoGjtO-ShRS0i6kWYh7t4MiSQoY-8Us2uE6GHqUMq-y3ff67RlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=JG4n5pb3ckofMgw0fBbW8uBmJVwUdPXvSUcxDvssKP7Ioa_xVQa9KhAGfVTM1PU2sswFIIZgZM7DH6HnIcLojbJ5O3IRk4M3jKF7ZGR2Yd3aIAtvwUxdBHqXZbx2Xebf9i0xgj1cVucKTutFvXIsZdAtqjSLiT3Hdj-S-SXLIGJZdrEm2LD2XyaK-xzzErjS7ydMavpVxqJ9GetqvYhTkcy8o2spYvZf-WNji_tsArKD1wihFNQwQP_rqqKtW2zIhYJKTJApofz33D7uJh7KB5g8U2KdYwL4lsKDoGjtO-ShRS0i6kWYh7t4MiSQoY-8Us2uE6GHqUMq-y3ff67RlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فوری
؛بااعلام‌دولت؛
سه‌شنبه ۱۶ تیر ماه استان تهران تعطیله. همون چیزی که قلعه نویی گفت اتفاق افتاد و یک هفته تعطیل شد. شنبه و یکشنبه و‌ سه شنبه تهران. دوشنبه کل کشور. پنجشنبه مشهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24731" target="_blank">📅 09:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24730">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mfc3BHrrrzcw6g9E8HhQ_aDgAQ-wgs98DBByYEDbshdF9KNmLPo51cYdgb2UWMZwvO8whuPhAmREQyXipFsbFIjNDal92T7K9VTDhrv7Z1Bp-wsEDWzehVmFjDGYvJJVImXfSW4PewDPPETfkZ4HUZJk7gHu9e163vW_m4tjoZ0C9bEY_B5CwBlxvGRDUdq5MsirXg_e_X-nMPd_Mnxo1oLaV8C6o-BqGb9GtDHeINsDpQjI2yVUuaqa13pHEjXY4bKX5ty8fLX-UVGKILuhR_zBz19GbIG9GwR7leajJ9-O0yT_JvHZ5GzwmxE71uNF0UtPmOPdvjUELrbIyyyRug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی جام جهانی 2026؛ فرانسهِ دشان حریف پاراگوئه در یک هشتم نهایی جام شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/24730" target="_blank">📅 09:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24729">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6Mn3CtNQeb9hgydjDkcaJR_13o3gOrxvvJmCALpjD_9AIKRu4AIBiRIxpZ-Vk3ViKgxyZycIdOFjFxrc3wGM_7SqQ2RGAw51ktKHYIwp1Vaqw3SeHpbxIvuU4-uFWQFOIbxd-XBHLVkX16cbjyfZwNvPDsp64RNgpV2QQTUU-PUyQW5BbBOtzfA7YLP8cGKyqLdrgIaQMJFzp_3qD_Qg-naBhK1UsOjvVSykPznkXrja4lQj-c6f1K6PgYMH0FZ8zU6Ze4LxbSmMNwp3UD1p6_mbqltoQR2oVTXWmiz4rPyyTNZodh39cBEySSV_7gdUxKfMf0j4a6ahd8JZEyJDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ اوسمار ویرا برای عقد قرارداد سه ساله با باشگاه تراکتور خواستار مبلغ 5.5 میلیون‌دلار برای‌ خودش و اعضای کادر فنی اش شده. درصورتیکه مدیریت باشگاه تراکتور با این درخواست موافقت کنند اوسمار راهی تبریز میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/24729" target="_blank">📅 09:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24728">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AbX-ibAAS3hFZJv2y8mSDjip5zonAvrdHnI7B1w3iKAL-0la-jyF5gEy5m4xEFELq9__HxeRxSI8JRXOr2zgGs7u1TPbCau0cX3BU_zgKYcUg-DF3G_U-NIPWzzeSVrk78cNVVHsQrwAFtCRtSrqPZECc7XTRD3SzR5DhZwbexs7untRP8mjwsMi8u2mUhmzYNRmURrtBKnB2ySJjJi1w1JlDL3QDAtX8CoXF4EX2f3N4qABsKzqgxzD40WMTS34Ovx4D4iVNc7q1mQqf8hJSJFexhjTr1bgwuJoupnpQQ-zV2zepGE2M-43EmVz6dt8yRdZPNFpcOmBfIcktnxyKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک شانردهم نهایی جام جهانی؛ خروس ها با درخشش کیلیان امباپه قاطعانه راهی مرحله بعدی شدند. گل‌های این دیدار دیدنی رو مشاهده کنید.
🇸🇪
سوئد
0️⃣
-
3️⃣
فرانسه
🇫🇷
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24728" target="_blank">📅 02:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24727">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0rLHbb4ZEJaAcot4TxCYne9pQPGcOjONcDWnqrsUWt1jpfelEAMv6P6To_hrgMpfhTsmAyX8WNG1WNixItfAd7UHdpstYdV-D_GyEN2ibosiYiHwSKTRulFlIzgOe8hTA78hweq42AvoRsz0x8GLGZbkCUXMJt-be2zIJA0XZnq4tNgeUn3-ayemRpXNDBWy-okUAwNh5ac8Hpd4C9x8J6H2fEobV6mAWS0A2ZeL0GU8igR11bKG9fjW1HFhWbDwihqlU39QwJUpvel92Fh8qfbyrs71E2kyo5g-NBRud8D29vtLYKuBePnQKs625F21b9BXIAr3yaz-Uzr2BAsmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24727" target="_blank">📅 02:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24726">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✅
برنامه‌‌‌دیدارها‌ی‌‌امروز؛ از مصاف سه‌شیرها مقابل کنگو تا دوئل جذاب یاران امباپه
🆚
گیوکرش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24726" target="_blank">📅 02:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24723">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e80e84f3dd.mp4?token=mCEqEwtJPBAAyKGXWVEC2Y9LEoZnd_Q-9VgUIL1bSNx7OsVDm4lWUhDEmupHcmP3sk9QLWrEUCSh8u_lzDHpf7YUSM8V8PylQ1IhMFjYhHVpDTu-ObtIvjOJKypZ8DTT--LOEfYh5Nq9nLhYGupw7dg7sSzNKPsNXj0Tx-049GnWf9KmEFOEC6WRL_36AZfiDeYcUcNxX9x12rSjnsqsjQLnAqaQTN5n2K9QUSdDX7xVJHGe0GTXodQjoard8okVbNC1kyCcsUqG5NmmszfjzJ_O-8DsuIsSBCBrzLpkZr7Mp4I9K6uXYpXHiyVypDi4qt-VJOgZIOBufTSNxc2sQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e80e84f3dd.mp4?token=mCEqEwtJPBAAyKGXWVEC2Y9LEoZnd_Q-9VgUIL1bSNx7OsVDm4lWUhDEmupHcmP3sk9QLWrEUCSh8u_lzDHpf7YUSM8V8PylQ1IhMFjYhHVpDTu-ObtIvjOJKypZ8DTT--LOEfYh5Nq9nLhYGupw7dg7sSzNKPsNXj0Tx-049GnWf9KmEFOEC6WRL_36AZfiDeYcUcNxX9x12rSjnsqsjQLnAqaQTN5n2K9QUSdDX7xVJHGe0GTXodQjoard8okVbNC1kyCcsUqG5NmmszfjzJ_O-8DsuIsSBCBrzLpkZr7Mp4I9K6uXYpXHiyVypDi4qt-VJOgZIOBufTSNxc2sQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇯🇵
اشتباه مرگ‌بار و فاجعه‌بازیکنان‌تیم ژاپن در بازی شب‌گذشته‌مقابل برزیل که باعث حذف این تیم شایسته از جام جهانی شد؛ با گزارش عادل ببینید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24723" target="_blank">📅 02:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24722">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AUyW3YB-Sp1S_qnfjWsGirAtuRMYSV2_6kXAvyod8t8Hx-m2RGlX072W6lNTCmy0YX-_Z-l9cda-CIFMhNA0thbk0s1E90bQ0xB_PvM-PKL6sNqpk1_SjP46ivF1ErJSBcKcPtsPD8_znWBLLwY6HNkdT6mXeZXZ9h-aQRiMsKaWXEvYcXYkrinA4crBJym4Nw_m2JsGguHcggdZt8A__mXFOVPLmkeyLM3wkvoMrfF1ImpTVWoqDcB02eX1hDxu8FkP44eM7Ibi69jHFSd9wgi-rf6g84NsVCXc7Kv6vFilYwfo13neq-ESjul2bA4eUlzdYz8FyRfN41Ua_mY9-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بعداز آسانی؛ منیر الحدادی نیز چراغ سبز نشون داد: تاابتدای هفته‌آینده با خانواده‌ام به تهران برمیگردیم. بااستقلال قرارداد دارم و به آن متعهدم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24722" target="_blank">📅 01:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24721">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de066ea2ae.mp4?token=QKxgbAEXPDSfn7SWJNIb9p8H2JLtdM4cPnN4k2lwjOEFxA70VblR2-j1fB_y12785uSrmPXyBJZSCdJdhCClj3ICFWhlGyxZ5GwIOOnpR5-V45W2zhDs0HkXDnqsCiH24m2H7V4kiMhrgrGhUgqtsu9Vto4aQ4RGPRKiUhN3ltne76YVKpCshvzaqGC56C4BUIbrB_LiX6s89tJryY4C0xermvE7euI8zbHD3O-o-foJ9QdGDM5p451kaqagf9bfGIlrvMf30GRSc18IWUONIKT4xkc6FOH1ROkiWjEDDr5oiJ4QFv-nBmnvzVL3yr4ttaq_-dy1YpdgjQKL_JWgdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de066ea2ae.mp4?token=QKxgbAEXPDSfn7SWJNIb9p8H2JLtdM4cPnN4k2lwjOEFxA70VblR2-j1fB_y12785uSrmPXyBJZSCdJdhCClj3ICFWhlGyxZ5GwIOOnpR5-V45W2zhDs0HkXDnqsCiH24m2H7V4kiMhrgrGhUgqtsu9Vto4aQ4RGPRKiUhN3ltne76YVKpCshvzaqGC56C4BUIbrB_LiX6s89tJryY4C0xermvE7euI8zbHD3O-o-foJ9QdGDM5p451kaqagf9bfGIlrvMf30GRSc18IWUONIKT4xkc6FOH1ROkiWjEDDr5oiJ4QFv-nBmnvzVL3yr4ttaq_-dy1YpdgjQKL_JWgdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
داستان عجیب ازدواج و جدایی محسن مسلمان ستاره سال‌های نچندان‌دور باشگاه پرسپولیس: دو تا خونه و ۱۱۴سکه‌به‌نیت ۱۱۴ معصوم توهمون سال ۹۶ دادم رفت! دیگه هیجوقت سمت زن گرفتن نمیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24721" target="_blank">📅 01:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24720">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPLxBCO7AsWahYDe4x7h7f93J_KOREbycyZoDqFcxx2eITwSG9ag4DZyVTBFwPfpQAeEqnjRchd0Gf2cQMukWbECQFojKQPFQXXxaHkEB7jxlsk85DyTyooNraAR2hSlvY9sdKFZqrhMcslQipmg4D5lgiheTpWQyXArFYwqVUcc8cYukSrKGlYpL7k48pA8kxmqfJfluJ5DNLcf5sJsg5xsfJ7uV_YzPH6-XzJVckTPHdWZrfuzj67o7hU5yKcmAO_moULB20WeJjs45d8IbJmMHXTd_cmb6ngqLbJHk6G1Z1c0NXO44yHZB0DVFULl79tn4cP37KKKL9HNlfHWIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نشریه بیلد: هری کین اگه با بایرن مونیخ قراردادش رو تمدید نکنه مقصد بعدی او قطعا بارسا خواهد بود اما الان هدف اصلی بارسا جذب آلوارز و هدف کین تمدید قراردادش با باواریایی‌هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24720" target="_blank">📅 01:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24718">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qS8jajTrKHZVoR6PdyEXYnauw2KvGq9WFrsTymU2lqrZ0a8YAoE0B8dv4BE92bWSVRPUCRVznwu6pcsPMQs_exJsvrXjwhCqWhoHjiJHeZt47gxIrHlt7YajCEAov-U9P2S_79yVsQM5ZNQ2W_C5aX0ebFxHJuJ_BrAZIkP2IhcqKWqs_O2ZvTb5liuZloKHf44WGWKLiVjft0zsFUPsWbx2HqLXs4S7VUieW4IxyF66cdjEAL94OS6eZ0LHR5XRXIn6p1gkFK87HfQgkfzoJ7VVccqw76G-ne9ntRTpZ_xww712QRnwyUcXCkGR8JX7YnWHNLJpEdvY4ZzMKMqOeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
نشریهESPN
: علیرضا فغانی باعملکرد فوق العاده خود در رقابت های جام جهانی به اصلی ترین گزینه فیفا برای‌‌قضاوت بازی فینال جام تبدیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24718" target="_blank">📅 01:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24717">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iV3bo_qOUnXIMHXuEwgAq8q1t1B6C8hc-ozDtGFAqRK1eN-SXJA32yYiS5x8y-l3QNbg1mEEbg1ppxd4zXsKF2lfgCoBRqlS-KE0fel_4VYOvEI09_VfsI3dhi-EcT99qGoKTAydneAMkLeUbKcw3TZ-_9Demy9slRRfZTGe3ehuHIJbszr-vbOKioZLzFmYOEXv-hhKQfCjINd83Xi_bF0hg9jRtlmAjNRGg9VSiplhmeGqdUSxswHu_NxSSZ61B8MJEk7jgrihBSvpW5IZQpasMEUJG3_v-hC_pWSiVNKsXTDKrnsGLNwizIMrpkTDsbMP2Zoe6ecf_Su5iLYPfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه پرسپولیس در قراردادش با خداداد عزیزی بند پاداش آسیایی 12 میلیارد تومانی گنجانده بود که بعد از اینکه سرخپوشان از صعود به مرحله گروهی سطح دو آسیا جاموندند عزیزی نیز به باتوجه به پیشنهاد بهتر زنوزی در تراکتور موند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24717" target="_blank">📅 01:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24715">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XyTb4-6BKjFzleS2ClRy5UL6LqFN1AcMZXYitzwTBi2czK0l21daanWCZ7o4Jg5-ckqUpzgvgL2ZsNcUvUiM7soeKd1vSATFnDqCY4Yl0mu4RI5NOUSfs1UQ2icHC5-MVMry36DQcouDql6ffnwVm1BZ7QVYXIcbHUUAA8lCkSHh_vDULfjPf3CKQXMvBhjl3MarY99JKEdnZKxAE_hhn9wC0gYeeD2YPC5V9efuGVU4586YWmboLCrPX5Tkm9BbE1S4hTCU-vHwUNMcoWAYXqc8Od-bxskslk92TgVZnYP8sUxQfqso4St33GDxqaGw6tPB8ABJCEqVHOl0mY3LLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
جیانی‌اینفانتینو رئیس‌فیفا تو دوهفته گذشته 24 مسابقه رو تو جام‌‌جهانی از نزدیک نگاه کرد و بیش از 50 هزار کیلومتر رو در یک جت خصوصی گذروند.
‼️
براساس‌برآوردهای بی بی سی، تاثیر آب و هوایی سفر جت اینفانتینو در این دو هفته با انتشار سالانه گازهای گلخانه ای حدود…</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24715" target="_blank">📅 01:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24714">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NF0Ui55ifdBC39fPfdAYNvWgePEv56fQbPE99goLpFOgdjfYHs4tKbWdvvYW3e-6TLwHEtI2ndvlZ_AdP7ko0T4oXDjNoiewpCGDijQ-URdxNlDQJg7EjOzci4tHMkuQ3lPtJKu3PHYK3UhI5SOTBxugUrpa10m7jJGvWU2zkUkcxY5gfeuF1li0Ksa5AOdhTFkmwmtA4K4WYcA5xio5BFTZi4DvWKk_FSdgPIWRMob_r0OtSGOrcfsAT8JPtikZK43fKZs0esMBBZ_sbYisjA7EouKJuQpuBn7cmHFFXqZi_uFbqpM-pL2R8V7Pfe8z11vH90aI_C_X6RKlL4rWIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏این‌چجوری‌هرروزکل‌بازیارومیبینه‌اصلا میخوابه چیزی میخوره؟ چجوری به‌این‌سرعت جابجا میشه؟ منی‌که‌میدونم از اینفانتینو دو تا هست ولی نمیتونم ثابت کنم‌. مگه‌میشه‌به‌این سرعت استادیوما رو بره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24714" target="_blank">📅 00:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24713">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-HQ4Htnfn9SZIdmjfD4e0KImW7d0JCWAqhNYyPsRF-IHR5vMJvTRzKMNHvpB_GfPFC_ZtKJW4hXEwzGeX8Y-h_nILEDPWnw20Kcd8Tr_0_SVVTgB74vuRJNfiwq0M6LuGaeno9mLb6dO_LjSF103w3fIbCZN58JHhR6wMh-c9x5SwYLyEFcLFcfMANYx_fCXbnzNiSBuYnCrkQXQssN5XtXw7Bd0jsf-bo0U3TsVv6sMz8E_1U53HTUx9cjxAgIZqics3OytRBiRwL7-O1h1vsRK7BV3RkzgHtyxhw1fCXFsYzn8rRsO1sdZjGx58T_E1LbdKocXARtQ38-LQTzCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ اگراتفاق خاصی رخ‌ندهد گابریل پین مربی ایتالیایی سابق تیم ملی ایتالیا با عقد قرار دادی 1+1 ساله به جمع آبی پوشان پایتخت باز خواهد گشت. توافقات نهایی بین طرفین در ساعات گذشته انجام شده و با دریافت پیش پرداختی قرارداد…</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24713" target="_blank">📅 00:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24712">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GU2rFQr6Ns18bggjwtoUTISZziiOauN-fIPCzZMTDZp9B2v147Kw1Mau1wzFROen5D41Vcx92WzQhM_tM1_Zoffqbv4zzUGuBA52bqtakLEhQ9IEKi6eCiuxeVJpGmOZOp5iF7EdAA4dOXXDxsJsRsBC9vcSgxd_eVhWI_QB5_BtC1co7MNnZW7jDWJ9aef-NRzdbtnlAfFZNhQGMYcD-7N59HmoyyNzSTfc9_RjXTL0yZPy6itnknQNLlzbjnh1_fkWIAAtNOjUgSX-FwD8b3AfUElxVfLdkusfqvC_A__bsagw9XN49d_TIBZckt8N0sMJ3rEw5r23qiIYvK8lxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه پرسپولیس در قراردادش با خداداد عزیزی بند پاداش آسیایی 12 میلیارد تومانی گنجانده بود که بعد از اینکه سرخپوشان از صعود به مرحله گروهی سطح دو آسیا جاموندند عزیزی نیز به باتوجه به پیشنهاد بهتر زنوزی در تراکتور موند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24712" target="_blank">📅 00:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24710">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhqLMqkgu5rXeTUCFu7ZrF9iKLw6Iep7G5Y_UpI2b64WV9E5_uDYfgzy6A2nKjZpJpLVXM61c-YELNu-rZVS3Xgwh5lil9RrFVchzv6ijOD_A7CCEjkZeZjcqI1iUmLzyLr37rtVe2xG2eaFGX_dc7xd09jCHazAJPuR1walSGpWndsaS56HBCMCSW1pSU0Jn2JUyEpkN3qwttBvtJ0IiA-bFey1O21vVVtLY4Uh2RqLgCAx2IN1g6PNbJT8XdYhjiftkuNUeQwShTdJbgi3dgae81rywX12Ltr7G2DvnekhysFdSXIck6B206vYFoIsZOTtJ-mKcgWGQ12Pg0Awbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌دیدارها‌ی‌‌امروز؛
از مصاف سه‌شیرها مقابل کنگو تا دوئل جذاب یاران امباپه
🆚
گیوکرش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24710" target="_blank">📅 23:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24709">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4EeXEZQ-Stlyy4k36CdsXm1kJhxeYPiHwUiciVhzigWrX-UsZDL3q3zXTd5g7Zk0ileoMkcmgjLQVX092xkYa6N6xZcrpQ_rnknJ1vCx7wzXIkP3i-Q_nXKPBUBZ_z2wXOtCgAn3LJD_aFECfBRuifRFE7t8vLbHBU_59mNHD2kTdfVxbCAoJhLNVXVTUmdzsXkkarIuw10zXV_YsbhJnwEIChH_aB2wm85vsN63EOo73clIO80lfAQh6JdT63RvwGMavYCZVVqMy8YZH2W0jjSx20_ClUG0RJETJ9bGFrlzLkxSfVQeZasdn5Io0JQOG0Os4j7vGAtCs6QGTw0gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای دیروز؛
از وداع زودهنگام هلند و آلمان با جام‌جهانی تا برتری بزرگ نروژ با گلزنی هالند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24709" target="_blank">📅 23:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24708">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GcwDDB7ddJULHketEZDrXGeIFYmu8IBuy9fzulwwCwN6Z5GAv-ceY4GlShIpx31wErO7OSu8Hsp2rzErGlk1AApzr0yxh5fPB0WO0uqLLWvEm3kqm3dfG6hwC6JoqUNenaCvwQ1AHNL-gcXc-usqze6F8-Co9NL4kv1N3aGjOyCjbk-h4rNjMisdhwDxcOPPLwzdLYWxbTO9kZ_4QCkperPuROJQ2ck3oW8NfueJ7B6BnIHedJlB_FC81KH-H0iwpi37b5WOt_109xOfRzRcaqj2OuREAvCut2bX6nLD66NzYBiwcTzyNNDag1vDh3iNGbnAlaNwrx2tXTxZCJkrdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
مقایسه جذاب عملکرد بردلی بارکولا و لامین یامال دوستاره‌پاریسن‌ژرمن
🆚
بارسلونا در کل دوران حرفه‌ایشون؛ بارکولا بسیار علاقمنده که بعد از رقابت های جام جهانی از PSG جدا و راهی بارسا بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24708" target="_blank">📅 23:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24707">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6DOo1vQRzMZWI4IhRx9hAv_9XmZNHqRUherfbZHRxvfB85T65FVK7KQgiBixmJUsVkRYBb4DbODEkA4njCcXoig8VSz2vXg9NKcCqJ7WoRyAJi4BPOjqzwGMBKSOAHO7rBmfjsczbs9yfWVfD-8tTBtIWM_udJIeptVtOvsjAyN3gO5Qjpk6k75tENv6xdO0va7xATmFjAHuzrUth3IEiAnjrDe_C2r6gJXriS4hZdsY49KZFCqp_LO-J_1xHzoXnl-ZdzYh9p9ykg3LG9KuCyHr3Y_g2ztx8IlOryaXdxObnZvJBUrOaK0wjXdD7lgfBY6Xw449EORTXKYLtUQcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نروژ باگل دقیقه 86 هالند ساحل‌عاج‌رو شکست داد و حریف برزیل در یک هشتم جام جهانی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24707" target="_blank">📅 23:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24705">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e80mhr-aSiHzDoTa_4fnI85jqkZyFJxJKKq5SfJMlQnGce_JhprcjrtatZYRN8z6Ij9nVg_zKHFTJgHWqjOWm_Rk30peapxNpEPmb1ngpm1HCfVfwhbxb5QUvpDudFOUmyvQw-ofPOU0GMkouVD1UzUfAypBoF1a-yi3JgBZiGFjrBMU5N_NoCvNXPvqusXZOj-RR17IVss0rGholBaFl2WjPoxlqI9TmHXKwyu9jzI05j9xCbwbl9PS0ac6h3pMXDGZV-aEiIh22Ix5mD4HRb3reNf_A9hvr-zXr8IKKskq1yyVTJzjmU2LPjFtZP2wyc7BSIE5bJoSPOQVQrCyAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ElPG6d1KuRPG7Lk53fySbt553652PMEb-ds4aRN162V8VsBpfWwCBaPtVyD157flCGb4PRZAdGW2qioRUVmLxMemOP81UIVKIzPkavU3-91KsPWq7n2tv13_KwMTZxP6vfRS0MXmiG8n-Mv0jwjktxMTKfwroqWxqAwErubaigj-S-xRDtSMum6mGZN0PMSz-n-hy50eCGtjLN4n23OWhbe0Cag3KI6LZLRbupLjnzIDhe2le_j8pzxVhuUvGkdD_8DLoDUtXUnJfxDBQeX2kLlaF829cqaTETq7adeJAbGvIDONVGahDKLyc5TBFD-Snaf980WGoTtNEDH1tQoxzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇲🇽
🆚
🇻🇪
🗓️
۱۰ تیر
⏰
۰۴:۳۰
مکزیک
🆚
ونزوئلا
صعود مکزیک یا شگفتی ونزوئلا؟
⚽
🔥
مکزیکِ به عنوان یکی از میزبانها این رقابتها برای ادامه مسیر به میدان می‌آید، اما ونزوئلا با انگیزه ادامه شگفتی‌هایش به دنبال حذف یکی از میزبانان است.
👀
⚡️
میزبان صعود می‌کند یا شگفتی در این جام ادامه دارد؟
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24705" target="_blank">📅 23:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24703">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aYl5baUKrB-Q_K84ngB0qDz4dLZIROnL7ybU0-IWmm3Fb2SRJEbJ8kboMYk4kRBta8qxPPvMi9XyLMq0X4W5lD92HVBKYumTKYl7U5LggbLVLxpnEDIvDJy0oWQ6LjXUtUO0eKaoHJ6z9yCnPHfMnmIBLkO5-y0QHIr3IJDYx86tn-uqMg5Q61vt_kloxV2oOb3ehJUWyob06xgakwvrsblyoz7GxZF6sXIWH7tkfpu-WPgxo9ISDchxmS1QsqZdH3hb73a9KUI_6sW8gxlBV8ugJiyAifmKj3YrGX4fzKN4G3PXA4STALHI0hEKqZ4iszFFh9Q58ET7hSYBlNmx3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O5FVpEJiI74GKK6bnre3NPFqFgjh9yzUkl3dXbEdiqaAKmK-PRdVgrllMOkkjGCRuOl2jUgSwa2X5jb9SxS9Pmwa1m5flTvqq9TbFV_SA4lpG0kZdz02f6FD7RbZCIwsb_9Ve30-JfJFX-hyeuT3dpzLRon_d3A6iLaU5ojycMdoZA89jEuaXnW18joZgNRSBqig9UrQoS8wmiaEI05SV8aNI-4qfayAEcNCy_LUZPpj3Th-nO_WJ2k1mmK005QtOCR3ObNYNLDobzhNWcS27StUsi0MQYdJdW9_aD31_yXrpW-QinEXmhot_MIUk61Nij0Ijzeh2sp2bqyaMJXltw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌هفته‌اول لالیگا و الکلاسیکوهای رفت و برگشت پس از انجام قرعه‌کشی فصل جدی
د
‼️
دیدار رفت ال‌کلاسیکو:‌ یکشنبه 3 آبان 1405 در نوکمپ؛ دیدار برگشت ال‌کلاسیکو:‌ یکشنبه 19 اردیبهشت ماه 1406 در ورزشگاه برنابئو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24703" target="_blank">📅 23:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24702">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJQD6UtDh34Yghw-b7FMiYZ65ZTmrcynBQ2JdiscgFfUoFNN47YYmlB2foMRjrIOgbLp4nQOYqzjCZO3uv3jZdq5P9rWHg8KJmHnGGTUKOK7dulFM6TV8xoh1k5B5S8IfGKxebjWHZDkZpCpCOL3TdzFYymBxjTEKSHs_9KQBqH6UxXNv3G_Z8xSkjzj7EEK3Ie-s10ZLamDb1-og8cM4MGPzy6q8kRow9C__f0zFSUzkZBIlCXQVnHs00ihBgacQxMdd-ADISzsQ1QGx_qQG-3TCMX_Ek5C76obXoA1o6RG7bOLAxa7F55DG2bFHnb-qIj-x7Zdr3QzXld12d_RgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخباردریافتی پرشیانا؛ باشگاه پرسپولیس تا پایان‌هفته‌از دراگان اسکوچیچ، مهدی تیکدری و کسری طاهری سه خرید جدید خود رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24702" target="_blank">📅 22:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24701">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Autjrw_kXr5X4BigjLw-nUistVfSvkxKLR_T7muLBBvtci_9UGDJ-TAOOIu7X4NJuCkPS_RG2U5kNS3-NDjL7MkdTCflWWZkgXC16ydvfbKGE_wh4w1pIDm3_FXBDMFYYRzmONfgQtpe2g1iaiwXP-rnMWYGUk7psmHrnRgUJh3eavCRyI6pK5XBdFLUmJ6qhGOV5jPWYJ9PS8TtnidA1QLsbPYAnEiEaP8y-ctRBx36c2SElEh8oSqysUYZQyTq90ed3d5giGTV7ZfjIhBgMQ5HGLd_X0GJVj3Rtf5XFd3ZbdE22IXVLT6gM6IZve4bkAZ4anoQLOP4o6_OmkouMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تااینجای‌جام‌جهانی 2026؛ خطرناک‌ترین چیز نه پنالتی بوده، نه وار فقط و فقط یه عکس یادگاری!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24701" target="_blank">📅 22:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24700">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LF6PUN6msho2m19rgcM3edJdp-WeBeCOCXSSeREvbfXVnobTmgbcSuBr2Vo5wBCoPYWAjNj4iXokl4ogNvous438hd09mmonxtHhN6-_ujbJg9rQtgGVvXDQQZTaU1kiYNj1syZQzpNOAE65D2R8fDYvOjA8lsVfFLv8nn1TPOrtL2vBGp-m9oINYxZZ0kmRmfbJroOpzeed-pWv9yHIkZpeuNUKRTO0jvHoPhEujlv8z8JtL6-1yk7AUCDSCl0q22dqH-t_MEZm1Ai5Hho2Q30zSHo-k_GslCoakkmvWRqXmYB7hGBFQZlWYPldtfmlC3lHWkvimRujn4i6MAjK6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇳🇴
سوپرگل‌دیدنی نروژی‌ها در بازی امشب مقابل ساحل عاج در یک شانردهم نهایی؛ چه کاتی برداشت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24700" target="_blank">📅 22:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24699">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZ0XzcC9qksnSiz4k_Sac2Quu5-5-mFlthAG6RrK47skrNitjQkbBIBlvUypQ5Ip2rSx73CgWrsYle5RsDqt2oijUV6E0m6dJPNRbXIWEJRT4odx4rUbf5iVaqOh5z0damnJDXsfXNjI-nPVw9CeC08H8DxoAiPAjP--VsPnRPGyonIH2iPseWzMlp37PxBiAz--AUDpSFwy_nXi8Rk5dJRDm6IWq5-PQ-q1WiMm8a-PwTkaGXABfELOBhSjUwzVlZZT9OmdwlkkvsC27lH-Qiot9o_PgA8-f2FWA5bxnIQg1KLAZh16LqsQIYVqgzHRlehCi1xgmMnZqwJl9LuAzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ به احتمال بسیار زیاد بخش رسانه ای باشگاه پرسپولیس فردا پوستر رونمایی از دراگان اسکوچیچ سرمربی‌جدید خود رو منتشر خواهد کرد‌.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/24699" target="_blank">📅 22:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24698">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDbm5WswOecO4JcSYaYJu2ExSvQPmQKLD262SKqytUirhxJXiFD0Fq1TXvbncwjtRl8QvvM19kkInRIgn14GjmTJd_hiP3uxfkx5-BsQ8bAMpJOQjnzd8bZQi1WH561yShp5pd0JPFveMb30PgttNMi_jF084YTNiidjLVTQ3CjmG_50kZXZdK8hJ8ADvGYsdBgv5iLTrdpzeRfwp30kjrP2PIrT1P0jcgPDF6hzws72QyJLQDdayxNvTRMYggnUbMeNC7uHlp2Wdu01dthJBpgh7Wa1cx8IL1SVvbmjn610kBNhJTBVGDn6o6V5t_zV-kQ1hiR9mGoh4GVaeXvXCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خداداد عزیزی در ویژه برنامه امشب جام جهانی اعلام کرد بنا به دلایلی پیوستنش به تیم پرسپولیس منتفی شده و فصل بعد نیز در تراکتور خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/24698" target="_blank">📅 22:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24697">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b011e22cad.mp4?token=coRNR8hVELjyG3xTIAc0t0xw4VFCjbeeEOEW4V1vhvphbZnbBrIDtDbyJ1QK_N0IMAaiYIcfR2UoPx8tIHbhimDAPNLeIEU4VwbpTIYcp-Ii0_ZzH5xI3Cz3uPdeLjmA7cNQerPyU-xcO4guBgLbhBNtnBc8WyE3lvoh02lI0fTWFERHy4WImlFA0cWDH2mASsnnBghYIMFjl07gRoM5CPyAMx7SJNitIOCjXmH00jp9KoFU1crXPsax0Qv4PPzNGoaf3y-p9Jt4anyPHA4K2XokfeJBDKKGnHqKOV3Lwvvf3wgZaCv5thlQ9xCE5JBFbU3To0Rh78-vhBvl_HaHVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b011e22cad.mp4?token=coRNR8hVELjyG3xTIAc0t0xw4VFCjbeeEOEW4V1vhvphbZnbBrIDtDbyJ1QK_N0IMAaiYIcfR2UoPx8tIHbhimDAPNLeIEU4VwbpTIYcp-Ii0_ZzH5xI3Cz3uPdeLjmA7cNQerPyU-xcO4guBgLbhBNtnBc8WyE3lvoh02lI0fTWFERHy4WImlFA0cWDH2mASsnnBghYIMFjl07gRoM5CPyAMx7SJNitIOCjXmH00jp9KoFU1crXPsax0Qv4PPzNGoaf3y-p9Jt4anyPHA4K2XokfeJBDKKGnHqKOV3Lwvvf3wgZaCv5thlQ9xCE5JBFbU3To0Rh78-vhBvl_HaHVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اون‌بازیکن‌تیم‌ملی‌هائیتی‌که‌کارش‌هندونه کاشتن و فروختنه، وقتی میفهمه من رو کلین شیت مراکش بت زدم: این چه سوپرگل برگ ریزونی بود که زدن!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/24697" target="_blank">📅 21:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24696">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6gv7eFdL24K7SXrOaBfIFAYp-q9Lx8yP2p9qlRITOtc3Lv-0aUxqUfcFlX3-Vh6CppmmT-moB-VuYPIjHtRIZWO86GmwPS5LAHKyTJdfDUAjvGLhxE0YkMMiuNBHzOFByA3nOXg4A_sdFro_uXyKS7lcxmo62ebZh4MaBR3wRDU0BJMjh5-dNyueHSzh4_Z6glef8I8lIdUyR1lasRolrOG2I5QA9pA0Bwstu4qmP0TdcsyF2fGe7lQrXXSnBE3Maf42GYxskpuHh-ksIxdo-Nf08R2imUenLAElIeiGG301GVmVlTooz89S0cEmYszHD5G76835b2N3M_QWU9tRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
لامین‌یامال:
شانس تیم‌ملی اسپانیا برای قهرمانی درجام‌جهانی‌بسیار بیشتر از بقیه تیم هاست. فرانسه بسیار ضعیف‌شده و تیمی نیست که بخواد ما روتهدیدکنه. هرچند بازی دیگه با اونا داشته باشیم باز هم با اختلاف میبریمشون؛ ضمن این‌که تو عکسه هم خبرنگاره سرشوخی رو با سپهر حیدری هم بازی کرد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/24696" target="_blank">📅 21:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24695">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9726fa772b.mp4?token=Fdhi2ukHscQZmaTI_YnWZ3i3tV8g_iTX1zmpnqcvTcZMJZK7Ponfu5YSWSy4eVBd3bMlutJckFvCZc2TISsnQ7RV89d9UKTySCKgzee5CRNNX7zLAo2XRcgZJ-En8pZd7R2fZMJ8rqARl4k3P_ZeEGZ7_Isu9Z_QgrpJ14zj4xUeSoGCyVq3ScRfmRmK-Sle8s-fFiKSH7CsmNbtJwHqvmsPeu-hxujVXzpsfgLyiJ-DYCjaC5hvf80VHF_x9TdEytkp7On0QofyTJ-MP0qWRKYM3Zlc2TnmBgXVKbFO56dh1loAbmC8NnfA4GUV3svsUb944LYXEeeWo7XdXn1j-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9726fa772b.mp4?token=Fdhi2ukHscQZmaTI_YnWZ3i3tV8g_iTX1zmpnqcvTcZMJZK7Ponfu5YSWSy4eVBd3bMlutJckFvCZc2TISsnQ7RV89d9UKTySCKgzee5CRNNX7zLAo2XRcgZJ-En8pZd7R2fZMJ8rqARl4k3P_ZeEGZ7_Isu9Z_QgrpJ14zj4xUeSoGCyVq3ScRfmRmK-Sle8s-fFiKSH7CsmNbtJwHqvmsPeu-hxujVXzpsfgLyiJ-DYCjaC5hvf80VHF_x9TdEytkp7On0QofyTJ-MP0qWRKYM3Zlc2TnmBgXVKbFO56dh1loAbmC8NnfA4GUV3svsUb944LYXEeeWo7XdXn1j-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌‌ دیدار ها‌ی‌ فردا؛ از مصاف مانشافت برابر پاراگوئه تا نبرد تماشایی هلند vs مراکش و جدال حساس یاران هالند مقابل ساحل عاج
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/24695" target="_blank">📅 21:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24694">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a72b5a564e.mp4?token=ota5NK2VcyU3sMHgSCsL_chQpachGA8utspSyVh_2xHStnHTf0m76sGAMXaiR6ik5YAe0dZpqZLKTf7V1cz7JwD9nsdwdKYQG5gvW32naxGp1Tf-Fw8mBN7eqDElvKkT8MKzM1rNaDYF7AWUpVsrtYxSbJs2PASj7zn25CP4jtQmxK3K9xkgGbxdPr0XTaSq9g2Nf10fpYRNBYAN2HSmcDirX6ll_N4QkpksUwsAOEJbgk9UNdrKwg_o58pQ9ak_wgyDh2Ts93kl1MTset1Y4VZ6-mv_IkkffEDMAggfnDJYizMqnfCwAJOB5x0UT2rTgglDyecNgRHRi6QOBaeomQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a72b5a564e.mp4?token=ota5NK2VcyU3sMHgSCsL_chQpachGA8utspSyVh_2xHStnHTf0m76sGAMXaiR6ik5YAe0dZpqZLKTf7V1cz7JwD9nsdwdKYQG5gvW32naxGp1Tf-Fw8mBN7eqDElvKkT8MKzM1rNaDYF7AWUpVsrtYxSbJs2PASj7zn25CP4jtQmxK3K9xkgGbxdPr0XTaSq9g2Nf10fpYRNBYAN2HSmcDirX6ll_N4QkpksUwsAOEJbgk9UNdrKwg_o58pQ9ak_wgyDh2Ts93kl1MTset1Y4VZ6-mv_IkkffEDMAggfnDJYizMqnfCwAJOB5x0UT2rTgglDyecNgRHRi6QOBaeomQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
👤
باشگاه پرسپولیس در اقدامی عجیب در روزهای گذشته با خداداد عزیزی سرپرست فصل قبل تراکتورصحبت‌‌های‌‌مفصلی  داشته‌اند و قصد دارند که او رو برای فصل بعنوان بعنوان سرپرست جدید سرخ ها انتخاب کنند. فعلا قراردادی امضانشده اما احتمال اینکه عزیزی به پرسپولیس بیاید…</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/24694" target="_blank">📅 20:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24693">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFNuk9trhedxO_UNJcUGoJ3zn345MlD2UoaOfCp32dHrzAY-NmbOAtu_tuxMXG1fOr3luXX1hm_XubDp6QRcb9toXgIRHQsW_IXI3l9YT1galz7adPUYqqyTEsYLDEIjziCneXQsEefKf7ojIGd010G83vIEfYWuzhUDT8OgIjQWD8Ok_w8nWuoO6xuPQHH-O2JXq4_4kJlIBbp9VJ7GEJ3bINxQA7r47VBDjhMfmtJ5f4ZWopiYpEA1X3TDK7mNcuEh9HUFFeG6RGY8PuAeRMh2SJuNQss5RjH3hd92_jZAalYSP26sYM8gpID1_9GM-MDD16jsnJTIObRLf2d_Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
همانطور که پیش‌تر خبر دادیم؛ یاسر آسانی ستاره آلبانیایی استقلال بامدادفردا وارد تهران خواهد شد و در تمرینات آبی پوشان پایتخت شرکت خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/24693" target="_blank">📅 20:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24692">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJ78bEoERsChAZvgaGsQskhD4AKh1zAiO4KctZbaf2E5P77ibMCKO76TOcV6M_aunQH3EPO2qD94htGq6jaoMiRWSYZ1ivfgnbkEgkHch3cz1NQ1rgKFwrmBt6t-qGvKP6S3bDVc-dRwOi5v5cMwY07E0bLjhfwkqIQDD4YknfZOZiSmsHwO5CZ-0dqKa0unDS3-DXCxu-LNHAoij-GZDIVKEvEKTgpO9QCTe9cCvlw7PtyuOaSDHlcW2hwAd4I3YaR9OyWzmYy8AjaJRJFWeIYEg3IYYN7L6MFp753C4Fhxe0eN15NN1O7cv1hu2A3Mj93P9C7NIp9C7BnNsYcyLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فلورین‌پلتنبرگ: سران‌منچستریونایتد با ماتئوس فرناندز برای عقد قراردادی پنج ساله به توافق کامل رسیده و حالا توافق با وستهم باقی مونده است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/24692" target="_blank">📅 20:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24691">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3hCCuav1kY6M26EUzAGmWsZKEEK3k8jIx5tq_bs7I22YcCiz49ftvWyQxp489FhLtcC-OEVsdqp58Tekmx31oLqWhU-GCRGxJvhYIKWPpCE2x2zw9FEpMnC3nA-uMpn9GGy-wz7tgmhT3bzzNUDeCVMKxoEEtP5Y-shJzU3X-T3nUgd5XtUY7kaY-DCL6Qlo-dWN7BfuHQeDLxA2ZL4qe_EeaDe-TzE6_rOnTneGM5Ln1VctKHsyOU0PlneNhaqqxIOmJ3_DITS6ss_AEi_Pxez0ClKqnKJCgummIi8Kfi0JqH84vmAnO03Y8P78fmcv05MbvyCfIstWwmVgscDjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ باشگاه پرسپولیس درتلاشه امروز برای دراگان اسکوچیچ بلیط‌تهیه‌کنه و این سرمربی کروات ظرف 48 ساعت‌آینده با دستیارانش وارد تهران شود.
‼️
بعد از رونمایی‌ از سنگ‌ اندازی این مدت بازیکن کهنه‌کارباندباز سرخپوشان‌پایتخت خواهیم گفت. این بازیکن از وقتی فهمید…</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/24691" target="_blank">📅 19:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24690">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3HYF2-y8EmgJpqs6x18aMG2NqqWKUuu2tetoxk9mBpjG1vipUY1cVkdsk1aEcW-Eqr9Ic9NdlCcHs5hkRMrrwcrrMvQ6pjoz4Jv3TrMJiI0Idn6rG2sSBKZzXwy28xX6wQ77VcqVT6fSw3fosLw1QFmUjwlU9wGUlOKxEb162OhDwie5bvcIUYCDU-MuK5LLZurY4916HJbXgGd9MS454zv7gTKBtVcMWE9KuJDLbz78peVfnIlI-3oyXla6BH75B3WHVJ0kqm6psFLVSdJdOaDVklk33MthtiXaPrqSzbWX--r2D4Fc43ugpdn1ak3fQaCDn1jmWAPn5o43XyYdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛باشگاه پرسپولیس و بانک شهر مبلغ توافق شده به اوسمار ویرا و کادرش روفراهم کرده و فرداصبح قراره‌این‌مبلغ به حساب او واریز کنه و رسما پوستر برکناری‌اش رو منتشر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/24690" target="_blank">📅 19:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24689">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfDIaTfz0iyR-bgi0nYvkIBut-BjxhUgJODMhpjwdx-eWRwtm_AwekvKgLuBcPUhkurXkl7P1HDGurehmKWZOtOZBIbnejyHPib8byUE6siXofWdsD_fRamW-iEqKi0bn3KM9PrIWJpFMsFzB5syLFyTMqs9kQblT9hfqW8Yn5KnHjsDghzrDHQCLOuYkh_6JjGDBDAlzF9e98R9UDMUKonSI_KoMQpqVMZiYY4jSNGkPHURLTFBjPSe2jpyPmcaUzEX_-nZT-TMPlwjZxP4COfd45ZUGUffw0VrgkE4guRuKM71oCMSES2kLhtsmFsiCTrHbvWnpuzUTQ9mKqunOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ضربات پنالتی دیدار امشب آلمان
🆚
پاراگوئه در مرحله یک شانردهم نهایی رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/24689" target="_blank">📅 19:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24686">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85e47b5880.mp4?token=WqXJpALKs_7vZj691qcXQEX-r-YSo754z1RKYByjT95vffYK7mKaJ34xZIsxW9Ggti_ieNUD_InEs8xag4Qf_i-Xhif_7ArGWWn0ePWSVy_ile79RsI5fHBybwBsRCrxK20AzZUPlbH0ox_reKvG-8YPfXswInC1uKClOKtwZb-DNNtw-VvX171Xqq3PqA_NbNNvZp6bjiAWp59PMpme_mVH-oRkGFQOXsrmqm3FSL5YGiIGvFjWqZjHrU4re53xd48anVXxHOoKXI2_tu9kpzNsVHvAzhaWoQi6BOwCPpk20tWuyAJkPgTi1fmbQyEgU6q8S2Y3ftAD6eu7PXlurg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85e47b5880.mp4?token=WqXJpALKs_7vZj691qcXQEX-r-YSo754z1RKYByjT95vffYK7mKaJ34xZIsxW9Ggti_ieNUD_InEs8xag4Qf_i-Xhif_7ArGWWn0ePWSVy_ile79RsI5fHBybwBsRCrxK20AzZUPlbH0ox_reKvG-8YPfXswInC1uKClOKtwZb-DNNtw-VvX171Xqq3PqA_NbNNvZp6bjiAWp59PMpme_mVH-oRkGFQOXsrmqm3FSL5YGiIGvFjWqZjHrU4re53xd48anVXxHOoKXI2_tu9kpzNsVHvAzhaWoQi6BOwCPpk20tWuyAJkPgTi1fmbQyEgU6q8S2Y3ftAD6eu7PXlurg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
سبک خاص و جذاب پنالتی گرفتن یاسین بونو که قبلا هم دیده بودیمش؛ پنالتی امروز صبح هلند رو به صورت عادی شیرجه میبست عمرا میگرفتش ولی اینطوری راحت سیوش کرد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24686" target="_blank">📅 18:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24685">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c85d949fba.mp4?token=QJaIs3ZtWLVbyWES0fzVcuocjwtU2dMA7o3KXKIqNoJHp1IDE1NBlY33RevjwY4vg_Jn9BtbwYfhYOhcA2e3GatGpRhYh_4nwyYQSskWdjMZFmK51DGdMlN4tZZL7WT0qBg5YsPynCaYZ3TNwfT9lnqCj3BYmFBIJlttOm9TIBi-Bqo3y9-fu8BeT7YS08dZJaI8aIwlaoQwJZL0b6jkg29YcQZwoVXwPVEFMyxa7VPDWNG1mmK8SSZqk7BgaeDyZ2DGanQEFA5jcs1Uq3zMKSZoA3X5QA9BtCWprJBd_ZqOxXONnYBL5Gv0pyQ4_NlO6ftGbbxuG-PtyG0cdKTAMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c85d949fba.mp4?token=QJaIs3ZtWLVbyWES0fzVcuocjwtU2dMA7o3KXKIqNoJHp1IDE1NBlY33RevjwY4vg_Jn9BtbwYfhYOhcA2e3GatGpRhYh_4nwyYQSskWdjMZFmK51DGdMlN4tZZL7WT0qBg5YsPynCaYZ3TNwfT9lnqCj3BYmFBIJlttOm9TIBi-Bqo3y9-fu8BeT7YS08dZJaI8aIwlaoQwJZL0b6jkg29YcQZwoVXwPVEFMyxa7VPDWNG1mmK8SSZqk7BgaeDyZ2DGanQEFA5jcs1Uq3zMKSZoA3X5QA9BtCWprJBd_ZqOxXONnYBL5Gv0pyQ4_NlO6ftGbbxuG-PtyG0cdKTAMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
تیم‌ملی‌آلمان همینجا حذف شد، نه مقابل تیم ملی پاراگوئه؛ اصلا بعداین‌دیگه نتونستن درست بازی کنند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24685" target="_blank">📅 18:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24684">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMnsevb6rvpdI9WNzHkxZxBDfMP1Lu6v3-26G9oZ1gGKx9wpzDjYNDhqbSb1RtZl5Hu7aVkjbjnAYBLiH_ghkt4qYdhPT-rzesIu8vAciVzCaw5mZwdLrm3OJWPA1IyBe0h-mMG6qOvsN4L4-1YBoSJOgRX298JWgA5ThDcvwo1k_jxK_8DZkPZ6fp0qOtRG6_sJjfuVUtLeL6zu9FbeZ4HQ5-wszoa97f1WHheAlsaqljwMNEkKAoeqsP0Kcw4jN9fFWXYcuGhn0omw0De5g-kf6t-m6nFbJson3r3yzilJRAeR5brnBXM4swAvEkMsliGk8DzqUD5IojE91-1Mfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
جادوگر تیم ملی غنا: در طالع و سرنوشت کریستیانو رونالدو نوشته‌شده‌که امسال قهرمان جام جهانی 2026 خواهد شد. سخت و دراماتیک است اماپرتعال بشکل باور نکردنی قهرمان خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24684" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24683">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBIv60t7lQpWuUMLBYF4x9HK3P4jFMdaEmboPFL5NAOGPXQ8EFp--sl0L1zVdy7QTi9VIBfzICBddha0vtu-Ge_pdt6H-FWNr9Tau5rI9NvqUCE3Bwxp6cqZf1Fz8egn_ySCsJUibnk9rRqnPA1BEMQYcaTnbtYbxW4DuLzdcDmyWQk3MrWtILWcW2ofyM-YHjKtvC7tHAs-dIyS-TEV8qomdIXX7we7aDnXeZXpIQD_S6LXFFyNcsosLQAZO6jBt_1nkkDVvEPG5GucvDaHQnwMAoJjQb8KxOE4hqw8fPyEHvPCUbtwR691PpIT3XCYfZQxFWd3MEUg_cX-mqb15Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: باتوجه به علاقه اینترمیلان به نیکو پاز؛ فلورنتینو پرز میخواد او رو با الساندرو باستونی مدافع 27 ساله این باشگاه معاوضه کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24683" target="_blank">📅 17:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24682">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUYrjVDYnfliMNkMvHyOznlWgqIULASINLm2f0ZRMYhgfoxM4B6Tg8DLbmK_qfdp37tZeFaHfP3y1lmE8rHZkxd0l0nIQ_1WyRrh7DCCOErL4yr4N6BiL88sRtPW1zHemJrXLIwlQSjEbCakt-lcbe-WNUj0JonKty-ls5_1QfKBC4kxlaP2K1nazjPIObEDVKg9ZG1F_OVuDeJ_8zwo-TXL6DwjiBk5A1YZZHejbDDVoiKDcmA6Ne6_DIgs1a6T_o7OxH5NRQdv38Tc7RLcJB8ndHf_oCXSQ658YzxQro6guoQfNo6IzQhM4vJmrr-sCeJk9mU8HrzhIJNihgYRjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/24682" target="_blank">📅 17:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24681">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b6727cd80.mp4?token=WLtBMUzcEWedRlBB6hAKCCk6pEPYBaiar5jgdYxm9xrabgdMYkY_NKIWpawNjlRJpC-bouP8Q5_3bYJgC3hYC6fJhw8ry-m8wBosQC6RKSJTD_pDhUv4DdOVlb6SwIR2I1HJuuYdl0w68mzYOVC7qgSwb3slhD89F6HHmhDlbRIaJkuThuOL8xElA-D1mPXvVTwn1QbER2QP5f5NsfqwFZTLiD7MpfdRhWQT3rcfynkmoiYIO4DlNPSOT4xAIcrSWWCtegciap3v6tfJdfoVP_N5CgGS9Lzdb1JYnqKwzbv5PKnugW_Cc0-j6RkuuPBH0glRKp1kltxyxrmxU4l_Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b6727cd80.mp4?token=WLtBMUzcEWedRlBB6hAKCCk6pEPYBaiar5jgdYxm9xrabgdMYkY_NKIWpawNjlRJpC-bouP8Q5_3bYJgC3hYC6fJhw8ry-m8wBosQC6RKSJTD_pDhUv4DdOVlb6SwIR2I1HJuuYdl0w68mzYOVC7qgSwb3slhD89F6HHmhDlbRIaJkuThuOL8xElA-D1mPXvVTwn1QbER2QP5f5NsfqwFZTLiD7MpfdRhWQT3rcfynkmoiYIO4DlNPSOT4xAIcrSWWCtegciap3v6tfJdfoVP_N5CgGS9Lzdb1JYnqKwzbv5PKnugW_Cc0-j6RkuuPBH0glRKp1kltxyxrmxU4l_Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇩🇪
#تکمیلی؛ بعد از حذف آلمان از جام جهانی؛ مانوئل نویر گلر 40 ساله ژرمن‌ها رسما اعلام کرد که از بازی های ملی خداحافظی کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24681" target="_blank">📅 17:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24680">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6hyEByEyivp8KtymleIExrkZ9bgWciPo_MMM22-Iw-n0r4SHzosmFSm9b7QxLQPR3Il0C9iR61o0QT1TjhbP4WcdZhmG0PDs5nuQdcFYUd98543Z0Sm_XPkApdVb47i8fvej0VAjJQQDiaAQjS2IGUKta9vfZUD2haHctb3PYzjM406JKp1d8XsLGyt1prm_DwMn997cUZI52coJ5vnzfZzpLvrNrEGPmCcqs6OIlhA4CI6Lf53z57MawDSEbQ-UNdoC0xr9lu9LD58vYqrc4_1M9NE1VcAuFWG7w0ZbJO4Nf9o02LDXKoV1pmboblXY-MNw-dZbsZ1Dcf3NfI2sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
مسیر به‌ظاهرآسون تیم‌ملی آرژانتین و لیونل مسی برای رسیدن به فینال جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24680" target="_blank">📅 17:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24679">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBExxbAS_68cRCmWtsXz6lBGufRZqYOcO1o5ojhDlvGbKnKOPTywrVgnmklHvOUHajIHc8F0fdrGxpPmN_ICXEXogcuoRlHeRnrJjenI1UGqn3VmAyMj9QC8J6U9uVqcklM9Zj-D2k-T8UvAfrdBX-kkN-66DkIKfQmB5I8uqEaCtrhES_nyW_qm7CnaoCcqzeK9eA8ro8W3kjt1bI1xNdYaPXfozW-rVDgMvMiy5Q-rEfdd2jypVgJbFddHu2i7kq9YyIs8YzDtmFrK41qG140GWAyy_BlWkum4nr12s7GMw58-4W7qTOM_tNsCdGi0D_6zxL0HLLihKsF7PdQtmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تااینجای‌جام‌جهانی 2026؛ خطرناک‌ترین چیز نه پنالتی بوده، نه وار فقط و فقط یه عکس یادگاری!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24679" target="_blank">📅 16:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24678">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DeM6sUEDDm9dVhllTePdop19pTu8GO7epvpr80teOpAmzCjjUz-lGtNbWk2w20loKLQqdfPicPDEMhyzfKyNxFT7pgcp6Ug8nV-6o4mDjFELhXDcMZuqo-t3ZHHg7TiMPAea_q6AHsrjSX0a1755Vgg_PiaNtI9reVALEaeyVStQfOEa6WfolbQusrxzBZb6EJ4t0PMpwlr0rk43-KppSD1rnliQE-KSPcO8h9XppAZl59qPUTPSFCF52j8tiSRu71qV3sfkD3lAXdfizGbpBC5WvTA54vVemqsk_YJJLX58JCGthpFIUPEXJbgpdJQAEia1eCAE583mP281faAX8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بااعلام‌ایجنت دوماگوی دروژدک مهاجم کروات تراکتور؛ قرارداد این‌مهاجم‌گلزن بااین باشگاه به پایان رسید و هم‌اکنون بازیکن‌آزاد بشمار می‌آید. دو باشگاه پرسپولیس و سپاهان به دنبال جذب او هستند.
‼️
اولش دراگان اسکوچیچ باهاش حرف زد... بعدش مدیریت باشگاه سپاهان با…</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24678" target="_blank">📅 16:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24677">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sC1KTcC9SGWZoMwZkHDM8sOgN7h-iH6jWy9C3_bi6akS7aom6N9RQpOd304XQ1YvDXJZUZKXdVnCkQLHYPuxkCscByzwz3K9udLyB0Qhi2LgcC8lm41KwK_LhVk6VirZJBb-1DjKm9lXmnP9bKrbCUFMWSm1tUDCKN_EBMxxWhB7fSX_Donre5pS-B-Te1N0phgy1iPZw31EuavMtpLzOdBF6K4mWHzbtfJWYXPzsAkLuiDLzetfH4lcdZlbiN4JrrD4rESiCAiBaHjTmYI8vwy6i-Jf1a1QqK2T9ZGs7R8xRlJzf2YiQB-2CQGPTyZPzAjlDIY4_OkdCqgHRNaNZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
شش بازی بین آمریکای جنوبی و اروپا در جام جهانی 2026: 5 برد یا صعود تیمهای آمریکای جنوبی. 1برد تیمهای اروپایی. فوتبال اروپا این دوره بد ریده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/24677" target="_blank">📅 15:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24676">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJJADNaQ9gbCeBrGm0fbOIQiqxMojrU4f-4SBwOMl_ukhM3cc_0_IoIdL_3ennfSWBVtT2GBa2vwuKkh6mRILcm7Opsk48WjdhyUEGb3cB0tvGvmDG_B9o2ayzYeQAtuQMTg5bC2dAL7i7eEl4GyViiNyGseZQDWIjAlpxxB9oBgzpwYOx3BCqW2j0GoCeN33Fd7Em79Z2Dv6IWjKfSYmoZbt6oX8vOSHy2Kph9mdezbD0EpDjqcgoYrYhbg76JD8HAbAFPaStigIHDxqbpbI410_M4YT1JaFl3al8KhBkGvZ_55TMDYnIq4QD9d-hrKMr-F10OH6VZm0y8D4qKXMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛باشگاه تراکتور به‌ سید حسین حسینی اعلام کرده مدیر برنامه هایش روتغییر بدهد با او قراردادی 3 ساله امضا خواهد کرد. پرشورها قصد دارند در صورتیکه علیرضا بیرانوند در این تیم نماند با گلر سابق استقلال قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/24676" target="_blank">📅 15:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24675">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpYvYWykXsI0DxuyU5dEhJ4NY5ONJcKkyixzYCa6rCbXHHmfWCjD3g-d1Jw99A8FUTMdvPc2anRPRSYf77avIXMzCPlX5ntbN83GyQfa-KqHe-DT8PLv6C3NDpOet6NEuBLpiHLMUc5ghnwETDsVlpuxE-W_ceaM6GYPIwlbqAPiw6LcqxYpbXzwdkAebb7CBu5t0zze2a-ATxKBQwcgklu_XDyx-24dpUo4YF8Oq_J7xEVkHaM9CMAPCtVuYa9nbCq08SdBYKAyEnVQYvVl8cfhI_wtMaOsMhy8o7i5KTYCWKovbWdL4cKIAlCGVI--m51NylajKjW3EZZ2jQzWFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی؛  حذف تلخ و زود هنگام لاله‌ های‌ نارنجی‌ برابر یاران اشرف حکیمی در مراکش در ضربات پنالتی؛ مراکش در دیداری سخت و نفس گیر راهی مرحله بعدی رقابت‌های جام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24675" target="_blank">📅 14:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24674">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMrIuyObbMSA-7OjDNHCjrG3AHMRYwvZ6iKztA-KIxJnSkyG5fOko7wSHD7sR8AslmS4kwbLkomYuHbViMIJk2_T07VVPH1ROt019GVt4nkMlxUTKLoutAv3ZWppj6yB1kocTd0ujHeCWfVyY6qIb8r6cYjm-dEv1ELl0fAGwvNfCrjdBwWQMj80PqLe1xd6fwJ3J1A70QLxvkj95uCT-qggQkpgT-f0cS7IUqgxrFr--crjoFXM1ZvlgdxqgEow25FWLFuCZ00fiVlYr-4N5P8HcZsjokTk9GqaVZhbjWhTDJypVIWfpIKVOsNnvDdOOXPwT8GM7GzyFtDLLgYHJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه تراکتور در روزهای گذشته علاوه بر تمدید قرار داد دانیال اسماعیلی‌ فر؛ قرارداد خلیل زاده به مدت یک‌ فصل و قرار داد محمد نادری رو به مدت دو فصل با پرشورها تمدید کرده‌است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24674" target="_blank">📅 14:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24673">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nvrffbHCjuhlzqa_PmpxdbHAioqmdxjP4YHDk_srsFH93mLN0EAs7bQJFj_m6wpJkgf8xmh-4pTQPBBw20Tgpw_sy53kxtlaFSkXw-Ct9zjIYtGUCZP3hIHH3s7EbvQr5XJEgN9s10RnsyFN0UgUcNILt_YoFvr8BKTmJNHfDkU2bAChcW6po-w9w1eMf5iAteAyDuE6ttzWS9YAxcAR1EVryDRUa4qAkzTi5smrbyoriJN8TmsLH4kSmrrucDCVTewvAhFiqOr1nFdLAB_17WMeI_Q0qM7nGWcbI2QRLt2WJzIi9P5c0DyGBeLW2AWDohVnERdwdHmggLKRLZRIrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌استقلال باید مبلغ 150 هزار دلار نیز به حساب جوئل کوجو بابت فسخ قراردادش واریز کنه تا پرونده این بازیکن به فیفا کشیده نشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24673" target="_blank">📅 14:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24672">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82624c7740.mp4?token=u_nYcFkKmSUHHUYC3fyc4M10X_4203dx9M9eJVs-uCUOIT-qpWb-35NEz-RH5jqBCCRp3wMy8qRtdNfuYDdt3wYgs1F7Qn8uPV1d_2tkhX8gGsZXzq74dJD5SHUYpghBW_U1UHZeBElELNgrFFAa3nW2tdebB1mJ3f4LrFvIxqEiYlxLpBNgCZzYKR6ArIzF-XI2UHwli3DS_Zz_g_b5x_BsIcTCfSbxhSyBJIKUSFipzoLwVzkSLcuEH9gJdkfIvld1Gx_a5weY_gdy481OoyUQPv7ol7iHSW9JsF8WSOnWNuDBhAblFvst-d4ViOiSovz9qmevQINxd7ViYFXIQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82624c7740.mp4?token=u_nYcFkKmSUHHUYC3fyc4M10X_4203dx9M9eJVs-uCUOIT-qpWb-35NEz-RH5jqBCCRp3wMy8qRtdNfuYDdt3wYgs1F7Qn8uPV1d_2tkhX8gGsZXzq74dJD5SHUYpghBW_U1UHZeBElELNgrFFAa3nW2tdebB1mJ3f4LrFvIxqEiYlxLpBNgCZzYKR6ArIzF-XI2UHwli3DS_Zz_g_b5x_BsIcTCfSbxhSyBJIKUSFipzoLwVzkSLcuEH9gJdkfIvld1Gx_a5weY_gdy481OoyUQPv7ol7iHSW9JsF8WSOnWNuDBhAblFvst-d4ViOiSovz9qmevQINxd7ViYFXIQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
میثاقی ژاپنی که بعنوان بهترین تیم اسیا اونم نه مقابل هرتیمی مثل‌نیوزیلند و مصر، بلکه مقابل برزیل پرافتخار ترین تیم جام‌ جهانی حذف شد رو مسخره میکنه؛ جوری میگه منتظر 2050 باشین اینا میخوان قهرمان‌جهان‌بشن انگارخودمون‌خیلی‌وضعمون خوبه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24672" target="_blank">📅 13:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24671">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-rzsLw4BUDzfwiHZawoYHLqYqd7iJI65ou0ygt63iHFykM8UF3HpalX0jcS4-y2LWaUo-0GPjpzdMOq19yHqh5st-IC3sZudhjZljyuHrtQv6UzWz_iOhMmRJWjBBaWPhO3pMwSNAu7S-1vgANvjDnXC4p6DVmagVXW7aT-1kr5Nohi9VkEgn7IR0jQ6QGzMI6vXSFb4GlIf-B7m19f3TET4pjXjuDbCVnLNQcmAHajjLZg2kzF-dgvphYBlWcRBht9nz8QHtJwsQqhcgHJnMo38cEd82DRz_TtH6mAh42MfkMJtGWIZs-Fk1-LvXDCgspFuP0AtleINMstr-t5AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنهابازی‌مهم‌امروز؛ گذر شاگردان آنجلوتی از سد سامورایی‌ها با گل نجات‌بخش مارتینلی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24671" target="_blank">📅 13:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24670">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1lZrsSDWBopr4Luo56-eR1O3ZNXp5egZ2Cmn8MRWrJrgFDLxytSFzjm_GyeHse5u1mqHnjGCOHZLfpgY4bT59YGwdSF14A1AekOAfprcTVYG7DqHA12GBOJLV-SPVrDzbWkB6csffRGO9w8FMeZGgIpgv-AOjc_8zinUuqLhfDK9IEvCPGbKoMEwj4s0VcnEWdHc8vLKCaeyelhHOBX9D5CojSbuS2qBMuF-1pS8VXJocYx8nD6GxFYUmvPCNhsN_U83zQEnSww1qAB8mUDR9S7hyy0dpiPFTbu0_DjqsbOd5i0Xb8ZhTMGVaeWjGIWfPMk1gEYOqM9VihubMRcxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24670" target="_blank">📅 12:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24669">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68e8477068.mp4?token=qd8glc-Yq0LJaTYlX2kXcr1ORs6fYISH5m10AZOIhseN3NeUB2kF-DVhKD5R0-QqFFRnAV0CdFlLRLj2lTDanx02UtoRYMFqBUHqPahAb82hy7qrw03qYnwhb5K3ipgdfNsS7iNSCooDNq5yMHGcOmFQwBCOTcqo2zJr2dhNTWLhlXHeOn7mfp4yiT-NMyFf2iq2feiobrLT-sEFAfUmEAmDxRJtjAHJCxdiKNiQzPq5eTt1J9YaELVdh-HamZdcQWzG1y-iuT7320d3tmUMSpwy2WIjLJFHxEDHdQMb01nz5KMrkMODc0qYtVPgq0bj5JtARVqxkZqRnCejfYdJeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68e8477068.mp4?token=qd8glc-Yq0LJaTYlX2kXcr1ORs6fYISH5m10AZOIhseN3NeUB2kF-DVhKD5R0-QqFFRnAV0CdFlLRLj2lTDanx02UtoRYMFqBUHqPahAb82hy7qrw03qYnwhb5K3ipgdfNsS7iNSCooDNq5yMHGcOmFQwBCOTcqo2zJr2dhNTWLhlXHeOn7mfp4yiT-NMyFf2iq2feiobrLT-sEFAfUmEAmDxRJtjAHJCxdiKNiQzPq5eTt1J9YaELVdh-HamZdcQWzG1y-iuT7320d3tmUMSpwy2WIjLJFHxEDHdQMb01nz5KMrkMODc0qYtVPgq0bj5JtARVqxkZqRnCejfYdJeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
یان سومر دروازه‌بان37ساله سوئیسی‌ تیم اینتر میلان بعد از چند فصل حضور در این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24669" target="_blank">📅 12:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24668">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/786ffe7041.mp4?token=JEc5kNjxFCzKGGTVTPTML1DM3_D7Spqf0lzMeMKVfvyG76RwRSFtfCflVzXQJvvRDsMCqZlViv75M7IkHN8KymuygQa3TEydjIWqnj4jXJO7sXBsy_qlFCLHIYyXrxeBqes1jqjFhVZ68VNN-8Gz9gXsfkYcGUceB4QZvtUugqExgYyfEHzB_MHPauqRWJOnF8jVec4kY6Ju_YOgESYki5qN1I3bMBPWUL637HUFLpkY2zbefL1I6LSWO0dKlm6C13mksONggchB_7OhDXzZkiYo_7WOKtW3olkOrRn_LG9oO6FCAxeSAA-yaVMx3ozLr525NnFoVSveT1lRIeQ4SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/786ffe7041.mp4?token=JEc5kNjxFCzKGGTVTPTML1DM3_D7Spqf0lzMeMKVfvyG76RwRSFtfCflVzXQJvvRDsMCqZlViv75M7IkHN8KymuygQa3TEydjIWqnj4jXJO7sXBsy_qlFCLHIYyXrxeBqes1jqjFhVZ68VNN-8Gz9gXsfkYcGUceB4QZvtUugqExgYyfEHzB_MHPauqRWJOnF8jVec4kY6Ju_YOgESYki5qN1I3bMBPWUL637HUFLpkY2zbefL1I6LSWO0dKlm6C13mksONggchB_7OhDXzZkiYo_7WOKtW3olkOrRn_LG9oO6FCAxeSAA-yaVMx3ozLr525NnFoVSveT1lRIeQ4SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی درگفتگو با ESPN گفته شک ندارم که آرژانتین باتموم‌ ستاره‌هاش مقابل کیپ ورد غافل‌گیرمیشه و خیلی‌زود از جام 2026 کنار میره!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24668" target="_blank">📅 11:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24667">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d5676f715.mp4?token=si3fo0LPrOAWibVRSxIk3BH6WPRuV0z-GbW5lrj5VpAdMMnaafPORlkUILkQJ_BjooZW9Vs_qW0hy3Cl37oZyWD4DuLBW5WId3QjFZ1CETbpGJUw4RaOgONyMLeFstTDsajnDdzn1B4eiqyNwhTIIZBVT0TlzSkBkAdPZ4YQDtypN8ScoeFjUYzZ3Ru_GATG4FTs64tdbUGtVpXtlggtyKB4OMMJTLjpiXpjvFOvmiNibTplFo39V7jAFLrBCCiOfiQLTvp4inLGcarnauQbGvSteZFIUwGK3fc1P0ecmY27P7REaxIY3DDSZC2ZZ2wYpXOmdccxRWDR7ataju5c_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d5676f715.mp4?token=si3fo0LPrOAWibVRSxIk3BH6WPRuV0z-GbW5lrj5VpAdMMnaafPORlkUILkQJ_BjooZW9Vs_qW0hy3Cl37oZyWD4DuLBW5WId3QjFZ1CETbpGJUw4RaOgONyMLeFstTDsajnDdzn1B4eiqyNwhTIIZBVT0TlzSkBkAdPZ4YQDtypN8ScoeFjUYzZ3Ru_GATG4FTs64tdbUGtVpXtlggtyKB4OMMJTLjpiXpjvFOvmiNibTplFo39V7jAFLrBCCiOfiQLTvp4inLGcarnauQbGvSteZFIUwGK3fc1P0ecmY27P7REaxIY3DDSZC2ZZ2wYpXOmdccxRWDR7ataju5c_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صداگذاری‌باورنکردنی جوادخیابانی مجری ویژه برنامه جام جهانی روی آرناتوویچ و خداداد عزیزی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24667" target="_blank">📅 11:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24666">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0F41k83nzrYpEEdUD13Xq_rwuce0IyqcxVomb_JAO556dm2AztMNQ4pZJl2r_8nOW6eTBQIVEvd9gzMfLYBiUXWQfgPQrOykFJclzkCEZTFUE_WUiX8I-ziMHbsbLNdaRmgriD4-hfZdJkiCbdWwofe8kkd5Lu8aYMWOGVqIR3zo0hLoHHExqloFaJ8Ic_z4M4zNiSJyrBCr2HoKxKJFEuivWs8iAl_D81oIcBEJnO6xwuil2GViH4DNdezse9w00t7IHwBhZvdcyqA6TYFmgqXQFLr10UIFmp2baut5K7QlsquGDOtCfg0R3oo0lobl5epu3umXmm9YYoWDUe7HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه‌پرشیانا؛
به احتمال فراوان باشگاه استاندارد لیژ قرارداد دنیس اکرت مهاجم 28 ساله خود را فسخ خواهد کرد و این مهاجم ایرانی الاصل احتمالا به لیگ برتر ایران خواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24666" target="_blank">📅 11:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24665">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYNRozfPm4RDMyi8d715jFHltHa-hUChfs2AVqqWANA4cyF2Oj0g1rYLHZDjRNtZauuHxcFwYpHb_hXTysZA09z5kLUxLZHQZEcH5wmTO7LRCaHwcCAVopFZMhB9fKoMt-oPuWRvBbqzwtRQhpEDtk_m15zytn57fPhZAI_GcYiYVKwZh3Wj83yoSgmqLfU4inTiVvTm_FUim53_tRJlSPCXhjN_F9khhPGIttunw9bbzOCua7wsEGW5PeSrZZbjkS3gFRi7GAO4c8yPMxnGKO26i-u5gtJ1pFHw41lFV0G92-wbGQ73QS6E_puna0CAqTcDe9lIdQ-brNf2doMhzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک شانزدهم نهایی جام جهانی 2026؛ صعود ارزشمند و شیرین کانادا به یک‌هشتم نهایی رقابت‌ها باپیروزی دیر هنگام و سخت مقابل آفریقای جنوبی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24665" target="_blank">📅 11:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24663">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sLefPxoo4wICBsjxh3smpVSdI9VF52b27LzAzjSojv0vIWJDOlLKGDcyTmxCr1hYBOP9S1vU7_wBeFS9diTbYH8kiya83SLk-bPnP0deuTp8mP6ckkijB7Zm9qSyJyjownlPoQxj0RZUhNCaKe8bZp47kj-R8rPVI7h2HEVgU5vw-Q8PtWTaVrEnrPhgxlgNtAapqmM7iDIMpH6vx1ols4LKXUhOtzWdU5PxjCl7-iIpyhX7GmZMwTC5B2ylViFB8LH37l4s2n_2iNIu3oDBDwU8F9v8p-dYucd8jHNj0BVCwIzmZN9lMI690ELhOt-DRh0A80PJXBIlI7wOrBN5xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ باشگاه پرسپولیس درتلاشه امروز برای دراگان اسکوچیچ بلیط‌تهیه‌کنه و این سرمربی کروات ظرف 48 ساعت‌آینده با دستیارانش وارد تهران شود.
‼️
بعد از رونمایی‌ از سنگ‌ اندازی این مدت بازیکن کهنه‌کارباندباز سرخپوشان‌پایتخت خواهیم گفت. این بازیکن از وقتی فهمید…</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24663" target="_blank">📅 10:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24661">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/572d6647db.mp4?token=cKHwMunaxSLLA3fHfbhYLgsyuvicG5FY_MgQHZySrhqmLyqqoslbEcMPUknj7YB2xw72n91Aa4ld9rptBBnIkxkMZKFJRjsDZuJJoZQWUtOriczS7_Hlq7UnmTSdNbJ5pnxtKSdgDHbbgBZnoh87VNV1UP49c2y1adkqkk2w7QJteH7bd2xpTHDhQq3rczruqrCBu5Na_XI64QQ4qtiVxRVtcb9Q5vzQ-g1c6VJbk12OplOD-QwzmSUVbWxbQgZ479ZwFijQjUgFwX5KFJp6HefeWvj3RpiEP4ncKyhsWyoNcyA4GeSUX_zjBLk_2Crfoc1tUqA_GNDZrtlNxXYTJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/572d6647db.mp4?token=cKHwMunaxSLLA3fHfbhYLgsyuvicG5FY_MgQHZySrhqmLyqqoslbEcMPUknj7YB2xw72n91Aa4ld9rptBBnIkxkMZKFJRjsDZuJJoZQWUtOriczS7_Hlq7UnmTSdNbJ5pnxtKSdgDHbbgBZnoh87VNV1UP49c2y1adkqkk2w7QJteH7bd2xpTHDhQq3rczruqrCBu5Na_XI64QQ4qtiVxRVtcb9Q5vzQ-g1c6VJbk12OplOD-QwzmSUVbWxbQgZ479ZwFijQjUgFwX5KFJp6HefeWvj3RpiEP4ncKyhsWyoNcyA4GeSUX_zjBLk_2Crfoc1tUqA_GNDZrtlNxXYTJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
صحبت‌ها و عذرخواهی هاجیمه موریاسو پس از حذف ژاپن مقابل برزیل بدون بهونه اوردن و گیر دادن به زمین و زمان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24661" target="_blank">📅 09:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24660">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LC97IL_qIVGPRWxdIy3pdFnUcATA3EGnReYcFYzq2fnN8DVasMY5CzWd0FEhXsB7mnXiPkR4zxnf8n06VY3Yi-19crDiFLjYTVRNSftSf_JJhiclI0A93gOlgmut2xwVgFni1urbRC47uhaQ3HqauMJjcBEpQsw5pw9xOduW4KK9p7J7KmpWJT7j29C_PZSXlId5S4Q8nFNZEc_Gah9v1kD0r-WhAayFib-rl1d0OktyyBvOLyB2e1jizXGGsf04SNs6_WSMPGIClzNJ43W0TSHxTHhm4STFQu1KeFwUfp5yN2zibV9lKZ0ZMam7BSSUKgEukQe171u38JX38F39-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
سه‌فینال‌آینده‌جام‌جهانی فوتبال در این ورزشگاه ها برگزار خواهد شد؛ کدام ورزشگاه باشکوه‌تره؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24660" target="_blank">📅 09:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24659">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی؛  حذف تلخ و زود هنگام لاله‌ های‌ نارنجی‌ برابر یاران اشرف حکیمی در مراکش در ضربات پنالتی؛ مراکش در دیداری سخت و نفس گیر راهی مرحله بعدی رقابت‌های جام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24659" target="_blank">📅 08:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24658">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kp1WihNeqEo72bFVnHbnVq7IZKIB2vvf-8AiEdwhxWPHwOtTzNIy72ixnKGyAVzHB0_8oulG60rO5vURi4gNE3bLLm0XBXG9BStFt2Jrc3Rpp3LqkqJbPjJe0TA09oQC3LQYYRsxp4qcMbRQyjrQ_IKE90CI5VfI-zpeVfHYnIXvsC1UYT2IUkngmk44USBxnkysi_tBMlcKsmnhh-tHayWOQhMZ5bcke19BHRoXCUVL_hqcVCst2X4hsVdXg75_bU_BNwjJELNd7wSagH39pYJSGtFLkktdv-HooGHsXY2bCuMDdP944N9h-4TCByuP7Id5EniCnqnSMey7nHZSmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی؛  حذف تلخ و زود هنگام لاله‌ های‌ نارنجی‌ برابر یاران اشرف حکیمی در مراکش در ضربات پنالتی؛ مراکش در دیداری سخت و نفس گیر راهی مرحله بعدی رقابت‌های جام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24658" target="_blank">📅 08:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24657">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/inanrIuRVQRGYvYVKwMnS9ISEAKuR5X9Csueqvx1b-aJ57NT7UuzaBzcm0QpDdm6xjvdiO3CBFXfFjbm3tyaK4KmfnLh1PLLpGcxRNsBqLyDqdULTTDCbKAGJqz_OjV7GzPaLDyPJWL2PMdh2lTBf9-HhysVVRY8E6VfIfzvr-npRQaG0cHkECtFY62-EHN9OTfRKtK7RQMVml3E_6E19PRp-En_OkTw2jRDmO1622wJMAA0F53Kq84wOaPJXndYypSetWaUUQ4J6euHG0T_q6k45GkuIksAyO3hmsh9TXocWc7PFOG_u1BBJG0aBMGbumMmXCuLRY1dzQB5bV-Mow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی جام جهانی بعد از صعود برزیل و پاراگوئه به مرحله یک هشتم نهایی جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24657" target="_blank">📅 08:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24656">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56f71a194a.mp4?token=XdrMYvE_ILZyzJXedKZbezCUZDTlPCpaSAqea9mV6y5gVgyn1i7DaIoXcH5Q0uqZ6vgJJ0JnErdGIh6h-vd9_q-QXz_S4q-DbCU6qW6B7_A4uoTLuT5F1Ut2ELAdvuyB5n4sa4XeDxKV3dl3gROM2FD3gqIxXAkPH24tU3rlbceZB8yo8OzHiQHOwM9PljSeXtZzQ3shF8xl-DWinLUTPgOtGLf6Oem3dRnIXx_MyXpg0VmodI_nhVV27orGl2ZvJslZVkZYLJts7LNzuHCeck4yeqj6WTM0cz0bLvdO2JVthcFdyw-djunuLiKUpumlNnukel6o3iUBl4aWYanuGHvPHHCJjX2QXs8tYdwD5EQbEfWw4gQfIG0jgyfO8RVaNI9AHQpVI_BUuljRkhMZ2FQxi1yRGodUtA5hH7gRjMTYVkoElPELPf3OMBJYoO0_dQTMSk5jY_wlb6Z_U0tmbUA-jlHwLDnm5oWWcTpfivMXmeNgBwUDlwuMryZ0dftvBIJWwrFgn3rAS_JUMoc7RRaJF_KYhh_PAGhOg-d72Bd6cWVSmjh4Jk5BppWLVuGbUzq3qEo9vgOmnomWlNNAM18PBwZrvf-UC5Ofx3EelnbdLaysfw4ptfhRIG0ceriYocKG6cFwXz_OaFhp4zJD40qU0xhpKWjE6IjOAmn9DOM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56f71a194a.mp4?token=XdrMYvE_ILZyzJXedKZbezCUZDTlPCpaSAqea9mV6y5gVgyn1i7DaIoXcH5Q0uqZ6vgJJ0JnErdGIh6h-vd9_q-QXz_S4q-DbCU6qW6B7_A4uoTLuT5F1Ut2ELAdvuyB5n4sa4XeDxKV3dl3gROM2FD3gqIxXAkPH24tU3rlbceZB8yo8OzHiQHOwM9PljSeXtZzQ3shF8xl-DWinLUTPgOtGLf6Oem3dRnIXx_MyXpg0VmodI_nhVV27orGl2ZvJslZVkZYLJts7LNzuHCeck4yeqj6WTM0cz0bLvdO2JVthcFdyw-djunuLiKUpumlNnukel6o3iUBl4aWYanuGHvPHHCJjX2QXs8tYdwD5EQbEfWw4gQfIG0jgyfO8RVaNI9AHQpVI_BUuljRkhMZ2FQxi1yRGodUtA5hH7gRjMTYVkoElPELPf3OMBJYoO0_dQTMSk5jY_wlb6Z_U0tmbUA-jlHwLDnm5oWWcTpfivMXmeNgBwUDlwuMryZ0dftvBIJWwrFgn3rAS_JUMoc7RRaJF_KYhh_PAGhOg-d72Bd6cWVSmjh4Jk5BppWLVuGbUzq3qEo9vgOmnomWlNNAM18PBwZrvf-UC5Ofx3EelnbdLaysfw4ptfhRIG0ceriYocKG6cFwXz_OaFhp4zJD40qU0xhpKWjE6IjOAmn9DOM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛‌شگفتی کامل شد؛ صعود تاریخی پاراگوئه به‌یک‌هشتم‌نهایی جام جهانی باپیروزی ارزشمند مقابل ژرمن‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24656" target="_blank">📅 03:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24655">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14530aa1d.mp4?token=lTVq9EsDGztQCa_YGgdf4wsD8srtrEZSp_InMrstL6GQ1JR0vNSM5bEHl33iCw7TmlqQFtFgoyR_sB_fYfgZZKAt7dN_Tcz7IuxIL01LtVzpxN-XoXPHFFMmSd_eQ3KkWFXEJvQKDO48NpxbAlxnl3f3aCKABGOXYL5Y2EjHwP76e-rw9eHjjl3Xxnrefz-AVBfVSXvjsyzncuz4Zx_qaKnQBLe7vFUFQ4hqHPpw4yoQ1WKrBvZIu55wKMtA0UReHN82_LaDUOoCNAY89td925qjlbPN__sxwMO1sLznJlgIXbVlDWmPbcP9tndzi18iYHURNTrBDQkp3QJy1oBIo7N41Nl3UiKMZMR6ZsVw_5xmin_frzNbp54UIfTDbGtdncyzYYpS29rB2VFTaP7U6cfTBpiKSBpgJyAWQvJpghXiScYpFLR_PH7HRxlJ0tbWNc3H647CWVjaOAVCE8CEAUjWneUS10t-SpqdYJtakG8DEeZnuL0VJDaumYm0XxGz8vwdnNbnXNpPMBC4o_Z34dqdguXurhFpqbN6DpDOAIztvgW1R-jHE-8bPT8Qbm15YZofrAcH5Oswc8VZKPmm7IGFdFYapP2eArwrpMGkdZAEHiyrqO4ncj3_yZqlgTFmOzraKC-tncUmy6KpQIIWMFTKWqydjfFxUzQCDBgzBqE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14530aa1d.mp4?token=lTVq9EsDGztQCa_YGgdf4wsD8srtrEZSp_InMrstL6GQ1JR0vNSM5bEHl33iCw7TmlqQFtFgoyR_sB_fYfgZZKAt7dN_Tcz7IuxIL01LtVzpxN-XoXPHFFMmSd_eQ3KkWFXEJvQKDO48NpxbAlxnl3f3aCKABGOXYL5Y2EjHwP76e-rw9eHjjl3Xxnrefz-AVBfVSXvjsyzncuz4Zx_qaKnQBLe7vFUFQ4hqHPpw4yoQ1WKrBvZIu55wKMtA0UReHN82_LaDUOoCNAY89td925qjlbPN__sxwMO1sLznJlgIXbVlDWmPbcP9tndzi18iYHURNTrBDQkp3QJy1oBIo7N41Nl3UiKMZMR6ZsVw_5xmin_frzNbp54UIfTDbGtdncyzYYpS29rB2VFTaP7U6cfTBpiKSBpgJyAWQvJpghXiScYpFLR_PH7HRxlJ0tbWNc3H647CWVjaOAVCE8CEAUjWneUS10t-SpqdYJtakG8DEeZnuL0VJDaumYm0XxGz8vwdnNbnXNpPMBC4o_Z34dqdguXurhFpqbN6DpDOAIztvgW1R-jHE-8bPT8Qbm15YZofrAcH5Oswc8VZKPmm7IGFdFYapP2eArwrpMGkdZAEHiyrqO4ncj3_yZqlgTFmOzraKC-tncUmy6KpQIIWMFTKWqydjfFxUzQCDBgzBqE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛‌شگفتی کامل شد؛ صعود تاریخی پاراگوئه به‌یک‌هشتم‌نهایی جام جهانی باپیروزی ارزشمند مقابل ژرمن‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24655" target="_blank">📅 03:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24654">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I66HKyozwhD00OUHRCKLu2t3BlpzxPguo306aY6IBLGFNepAjnTuJSZSpTLseQg_7qJOxgekIefAUNd6NRujKnDof5nhEQyL933uw6ZTAd_GCqqPZWXaUtUdJQs6f9CM9ArhhDsEG_OH9YzOGnXVy51POl7SK1-nyuu1zPRuyo2L0fJYFAuLCvdbpoDsj17hEWLtQ3VGhd4IjNbsgXXXtr-o6dDXZMi7pzEMZ4r7I9HJcM5sfScfaUXvoAjQOon4WLdJ7IyqFOOd3e48-BADdDxMWWLBMoOZMemRoyY8DZ9SlxrK2qoFVgjXod7QZhlhwkGrDoWP0yGy5sDpgli2mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛‌شگفتی کامل شد؛ صعود تاریخی پاراگوئه به‌یک‌هشتم‌نهایی جام جهانی باپیروزی ارزشمند مقابل ژرمن‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24654" target="_blank">📅 03:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24653">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef2bb58ba6.mp4?token=leFT6kCxHKyAKMFr1icnPUHhlNiJ5OMz9RGExFnW7pqJNBhSMUdW3raTRktHSxLb7ymIti7-BQFAY0yOxqGYV8DmxGGScCNy2sqirV3Q4awOyW2It13RXbj-GglXGoRnEqHYFKBORCxwHwm2BBxFD7Q5yG5ymDQK_4Qz6USKDVZT49mUO7hydk8_scg7lkPyYLPlembXmr8u5EaS0eb2vcbullyjjZ2XiCl-q-Y9MsPbrTEqsv-LXoPkCsxIC0HYv79H5Zy9BK1GPkKKAi8RU0MkOK8XslEPEobJ4pRy6AFYlMfKmqin1IXYqxznHO530rA1fol_kwW0vyy3FE-yyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef2bb58ba6.mp4?token=leFT6kCxHKyAKMFr1icnPUHhlNiJ5OMz9RGExFnW7pqJNBhSMUdW3raTRktHSxLb7ymIti7-BQFAY0yOxqGYV8DmxGGScCNy2sqirV3Q4awOyW2It13RXbj-GglXGoRnEqHYFKBORCxwHwm2BBxFD7Q5yG5ymDQK_4Qz6USKDVZT49mUO7hydk8_scg7lkPyYLPlembXmr8u5EaS0eb2vcbullyjjZ2XiCl-q-Y9MsPbrTEqsv-LXoPkCsxIC0HYv79H5Zy9BK1GPkKKAi8RU0MkOK8XslEPEobJ4pRy6AFYlMfKmqin1IXYqxznHO530rA1fol_kwW0vyy3FE-yyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هالک‌ایرانی‌درگفتگوباابوطالب‌حسینی:
شمشیر خوردم و مانع کشته شدن یه بنده خدایی شدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24653" target="_blank">📅 03:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24652">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3s-AUsufI_1jiGN0KNefewAiOOfP29UgIRppEzckFs3apz8Zc-pqvfFV8WtDiAOr-Wdrwogzoew8N8vyITynB5RfL_ungizuQq87PHD9x06hh2ctFOvH-8P-jcVncXwIaLps7wgyoO8XVjCmb4Uwr58Lnvk_lN_HGmtuM-EBeCbDz6N9weV88mwOOB0stY8tEmsltVfl8lGN9-Od5T0RyNiZtwQty9V_2wOFWivAIi0Sjp3XPyNF58wtDHl19SWX7l38SwcfwuMrmJmglkYyyrACxIoZ6JmnTEeuZvwvVfoSBDjzJ14cEopqmxuzYMs1q1yqT3RaSA4peq9rQAzaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛‌شگفتی کامل شد؛ صعود تاریخی پاراگوئه به‌یک‌هشتم‌نهایی جام جهانی باپیروزی ارزشمند مقابل ژرمن‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24652" target="_blank">📅 03:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24651">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApMLF_GTj3lSLMaZutz7WeadzqaMEtFuLJvHf2ZN6J7E8hxF2fNaTQWLzL5uMXh96CIeeOi3k1Ma14fWCURwYyVuqD84bL9t6finQUU0ZqdoBKs5eVbBSM9VJ-H9S5NbnwGVb7XFUCL39ubnL05oV5duOhIHRwfxWPI118KsR9R-jTcZhnT7d7m6JISSwuWHA_pTeoU4OL7QUZLgLZzLGKMzBZJqvGEN0TwbIlaYjBF8MIQrLWXxFucwhSdT05tsmmXjXXLvT2iDo7PWLoIteDmUnDMG3IRFV1WG4KkEjivPXsX-VpiC3JjXuuwhGFCuG410_6lCr79JG9ZAhlxKBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آلمان‌امشب‌از پاراگوئه‌گل‌خورد؛ آخرین کلین‌شیت نویر و آلمان توجام‌جهانی‌برمیگرده به فینال 2014:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24651" target="_blank">📅 02:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24650">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8d0fcfa32.mp4?token=lGrpMka6RNR6e44EopLvyvFAujUiyk3HP_2VkCaHsrYpGYu-kohcVKA1iEGeaXTv64Y6wHS75WenqFNgArAfGc-O7oPx6n3-c1QCrmDICzo-GDPzFJa2WNni8hkg2tPUCk36IVTAF7lh1FR-8z3d-GZucfPH5aDwCjaZiVhGVnYrCX4VMstjhVu_1_ZttVWWzNoGGfbp7SZKWxSzrqv2ru6ZUkmspRazsj5mzhNphN888fhrVkPOqpwdyy45oDBRqkB847F99VhrIBpu9kR9649pPxi_EuHAzjvocyn_W6b10GYfez5VIt6_9KHai8GSWigaSd1c8CA4wMjyjsx2v0vfYLKvQdWGMg2y-Of9dGc64jVwjKar_O-V04XTTRT9eNsoTl6lCNj5MJnCmVvp-2iNo1RtmffZ0bI9j0fqgwg6czvuVOabP2FceoHbUtodRdqQBPBlLlvi4glnyr9tXe3Hr9v-l8HYkXwkEBBAf1dIyU0SLKn0CJs3H860u-FhfR7ZdpWjtw8Zsmz0TH7RGWIMnKdUR021_yHs1klilctwe5mehfmDxO4Bf8rYBiqZn9Hrn-pvzX4yEts3x9hnRkEoznnFkND-Wr1WKOetlboq_kix3jKb4cCmEshLNe8Z-_0drUkVQ5zV_INwMmo6yMTUF0TpUs0n-_43YA-h6ZI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8d0fcfa32.mp4?token=lGrpMka6RNR6e44EopLvyvFAujUiyk3HP_2VkCaHsrYpGYu-kohcVKA1iEGeaXTv64Y6wHS75WenqFNgArAfGc-O7oPx6n3-c1QCrmDICzo-GDPzFJa2WNni8hkg2tPUCk36IVTAF7lh1FR-8z3d-GZucfPH5aDwCjaZiVhGVnYrCX4VMstjhVu_1_ZttVWWzNoGGfbp7SZKWxSzrqv2ru6ZUkmspRazsj5mzhNphN888fhrVkPOqpwdyy45oDBRqkB847F99VhrIBpu9kR9649pPxi_EuHAzjvocyn_W6b10GYfez5VIt6_9KHai8GSWigaSd1c8CA4wMjyjsx2v0vfYLKvQdWGMg2y-Of9dGc64jVwjKar_O-V04XTTRT9eNsoTl6lCNj5MJnCmVvp-2iNo1RtmffZ0bI9j0fqgwg6czvuVOabP2FceoHbUtodRdqQBPBlLlvi4glnyr9tXe3Hr9v-l8HYkXwkEBBAf1dIyU0SLKn0CJs3H860u-FhfR7ZdpWjtw8Zsmz0TH7RGWIMnKdUR021_yHs1klilctwe5mehfmDxO4Bf8rYBiqZn9Hrn-pvzX4yEts3x9hnRkEoznnFkND-Wr1WKOetlboq_kix3jKb4cCmEshLNe8Z-_0drUkVQ5zV_INwMmo6yMTUF0TpUs0n-_43YA-h6ZI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
👤
صحبت های عادل فردوسی پور در تعریف و تمجیداز رامین‌رضاییان‌ ستاره36ساله فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24650" target="_blank">📅 02:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24648">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3a278b0.mp4?token=spA-pEJ2Qk9rupROgakP36oZHvi7GHW03kqetwPAGW9oSUl-OB8kFnZ9CXlonUdCkJ4CW8fG0FzWms7E-zBQdcw61jeUjXlPxvYhgFZ9kXdUEues3lJzFqIbmsMt0uupUcmPcw79ghfLBhHKAu2JFbjowj-lPKN8afMbzwPXueSfCCeS6zsJmWLFUPyzzu-XXFZ99UrnDsYM-qsq39u2KiTs5fNzYjKdMSHC7JS3Zet8WdUfhdml4SYFusAHGB5Em6JeXslMQeO36pi7FLO_gjXpu-jneRixSf3LcdNOLlFYXLBqGmxT9q2e8VZtpfQwN9Mt7sB4NyYKihCnq3OdaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3a278b0.mp4?token=spA-pEJ2Qk9rupROgakP36oZHvi7GHW03kqetwPAGW9oSUl-OB8kFnZ9CXlonUdCkJ4CW8fG0FzWms7E-zBQdcw61jeUjXlPxvYhgFZ9kXdUEues3lJzFqIbmsMt0uupUcmPcw79ghfLBhHKAu2JFbjowj-lPKN8afMbzwPXueSfCCeS6zsJmWLFUPyzzu-XXFZ99UrnDsYM-qsq39u2KiTs5fNzYjKdMSHC7JS3Zet8WdUfhdml4SYFusAHGB5Em6JeXslMQeO36pi7FLO_gjXpu-jneRixSf3LcdNOLlFYXLBqGmxT9q2e8VZtpfQwN9Mt7sB4NyYKihCnq3OdaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
اینطوری که پیش میره مکزیک سال بعد یه افزایش جمعیت چشم گیر رو خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24648" target="_blank">📅 02:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24647">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NEdi8mhgaDRSL0NNmQIxX_0zJ08AAj130rdMkYIMnrkN37xRxYsTOC60q-eqy4D4HOurRcFuJvrBhLwLmzsDUDx0bwjsrJuXcfktVYwrOX2cWGwzxmq5WhtHzI-45fU7EDzWcUx_zSOEskqKWVjfiz_wlwgTvaLPF0Plvjk3ZSZj_LAzfYqEvefAaESVVxMTPz7B4Eb68X2jPS5jnW-T4Xe0XMj6RQ6IKMMHqDXmhRGlcsia345pdC8aww4Zd6KqKWMlDI6V6ACmDxRhK7Ear0qLe22TCocTxEtK7HK8oVozDGK3zSwDMpteP5UqmbB7Lm19m9lhz93j97ziXz_r6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جواد آقایی‌پور مهاجم‌سپاهان:مردم عزیز اگه تو رشت هستید و نیاز به کمک ضروری دارید به من پیام بدید، کاری از دستم بر بیاد براتون انجام میدم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24647" target="_blank">📅 02:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24646">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‼️
بازیکنان چادرملو به لیدری رضا میرزایی وینگر این‌تیم سرود قهرمانی این تیم تو آسیا رو خوندند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24646" target="_blank">📅 02:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24644">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A0WjMPukZXwvi__psH3ypfAdL0DhdiZdoYZpxY-bgOWLhPtgLBRognOP8LmcD_QS7pfvTavyBw9DlI8C0J1De_svanjJhAyTWZqw5PVLjm5dh-oVEAcavKHL7W2B0qNVO-3z5u_TKpfQfhstMzecIlPo168ky-6nur4k3qUEVAoDaQvUtwlL0k3DXvQI0KEjW_GuOtAHcv6OWp0cndXek7AIbUiZPJPWXoJD9w3h9Ebp2L0SrhO64amyIiJA6mHPRU800CSVq3m4SmreqgDenhZ7oGXCC_yDgYNztEazC3a9LGOlKlusfJjnItapHGlj26eg7Ltfd9BOXDBErhZEoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
#فکت؛ علیرضا بیرانوند تو جام جهانی 2026 :1 کلین شیت نویر تو جام جهانی 2026 :‌ 0 کلین شیت
‼️
تعداد کلین‌شیت درسه‌جام‌جهانی اخیر: بیرانوند دو کلین شیت داشته. مانویل نویر - 0 کلین شیت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24644" target="_blank">📅 01:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24643">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxwalQcsA3Fzc6a9lnTirc6RYIfK4QQUIj9Qbl9OroJhginK3NSij7C9AvuRFJLKm035g4F3x0n_Ga9-KvFfzwG8_sjJqkVH0kg41MLYBZfMhneSaRS-wfiTyHuNWlLWtGSLQ07J0Jx6t4yy9D0taitVswpjOTsw0lfb9aQ9v2UUjxxOKN7lNTTXC2X8KUlMOR9YVaWy821TrOEZAthSHbXgP22gDywOnBOyE7IpdiBiAhcLi1RRTcc_DtOO7GanJJAGQ_aymSAh48tOhwUmqX2GWq8wvQW3NyBEhRFiBU3oQBflelzFQRuw1sIk_-FvdYl7l1KRButYWWaBGyNXiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24643" target="_blank">📅 00:45 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
