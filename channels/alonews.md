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
<img src="https://cdn4.telesco.pe/file/aDRmO3NZzgxaVfRk9jagTLRmv0MpmbkQFhixgaqJx4_wnCwABufaAnZ47PZmD3PreB3qJZpA92ARjyUebxDUZa3J46iwOSO8Zqg-_Sr_VnqxRUoNXPl8BGXYdLmUEXwyDiDAON6ncqwu5dHwTxz5nCbDLnm6_hxqiSyO1mkYq-0Cny2OOqavDcOaegwjZsa8CPtJQaF9vAfeypOJHH08ln4Rg2md-vYTVsLcl5rcrFzdjdKxkm-0VdJKaVB_xozIoeY39GGZS6fXaj-Hm3p69do-YiWm4pE8rJ0GSQdIMeDiBZrtLEFITnai5MyfequVW7ingUYPYuMvLypysAkO_A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-19 21:42:35</div>
<hr>

<div class="tg-post" id="msg-152175">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
میلی گلد: پول همه مردم رو دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/alonews/152175" target="_blank">📅 21:40 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152174">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
زلنسکی: روسیه پس‌از اعلام آتش‌بس انرژی توسط ترامپ، به تأسیسات انرژی اوکراین در کی‌یف و خارکیف حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/152174" target="_blank">📅 21:35 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152173">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4da4f9104c.mp4?token=v34oLCYqfPxkwpZwPL79hGNc635A_ui_qWiekmbHqkGhz3AZkZWyVW6GCICVBGAdd51OhckR2q5bsGIGAaiseukJjwvc1MMYtUE8G7Jaq5eiIoUMZP96V2UhKW4Y9YWRaCEtVHtOWWqmKu2WIC2D-ZfcQsCRAFzDhHbIxExj0rtzIy1oKKgWMf3yBfa1_ecQemjnBgpm_NB_Z-RmYT5llasUpNUfeqU1UB-JXs3m9VO5wCqxC58oMIpIg1eA0kWqa8xs1zW4EnEmP3wHIeuItI-8VWCp1bqYj9gqaX_hZpVkUkKzjxYP3yMI0TtSkNYmNNkr1GPyDTBK02BpGFoHlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4da4f9104c.mp4?token=v34oLCYqfPxkwpZwPL79hGNc635A_ui_qWiekmbHqkGhz3AZkZWyVW6GCICVBGAdd51OhckR2q5bsGIGAaiseukJjwvc1MMYtUE8G7Jaq5eiIoUMZP96V2UhKW4Y9YWRaCEtVHtOWWqmKu2WIC2D-ZfcQsCRAFzDhHbIxExj0rtzIy1oKKgWMf3yBfa1_ecQemjnBgpm_NB_Z-RmYT5llasUpNUfeqU1UB-JXs3m9VO5wCqxC58oMIpIg1eA0kWqa8xs1zW4EnEmP3wHIeuItI-8VWCp1bqYj9gqaX_hZpVkUkKzjxYP3yMI0TtSkNYmNNkr1GPyDTBK02BpGFoHlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروی دریایی سپاه: دومین سوپر نفتکش با مین دریایی در تنگۀ هرمز برخورد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/152173" target="_blank">📅 21:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152172">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1fb405cce0.mp4?token=E3hLPFYNuB9tgPWILd-sWCqrQV_YDIJf3TiIlIY-NZO3oCJNv6zIgJLLOTNysOU53J1ZB5YQqQB2AHYpCMnsGqKCmTyJJYpfVm7vGtsMAwnm2Yz5kifNzETLO6O_lJLyj5J0klaYPKzlDo3nVQ3acMkN-wzCHj5BCOzLzBAzj21mluZb6Kyo8lCOC142oCTmunzkKN8uhl2mPZzvXflWrlltrSSLRrVbLogIZ7l1QhRsR-QJMo1oXzSMJkTKJbfN8_EFcDffFOGAXGI8432lSRLfjR79F2q4V25dTJ2F1-vsMkcWn7Lg4INMOm5YpZamZcdPA2V9OeXvgEqWhMf0JA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1fb405cce0.mp4?token=E3hLPFYNuB9tgPWILd-sWCqrQV_YDIJf3TiIlIY-NZO3oCJNv6zIgJLLOTNysOU53J1ZB5YQqQB2AHYpCMnsGqKCmTyJJYpfVm7vGtsMAwnm2Yz5kifNzETLO6O_lJLyj5J0klaYPKzlDo3nVQ3acMkN-wzCHj5BCOzLzBAzj21mluZb6Kyo8lCOC142oCTmunzkKN8uhl2mPZzvXflWrlltrSSLRrVbLogIZ7l1QhRsR-QJMo1oXzSMJkTKJbfN8_EFcDffFOGAXGI8432lSRLfjR79F2q4V25dTJ2F1-vsMkcWn7Lg4INMOm5YpZamZcdPA2V9OeXvgEqWhMf0JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دعوای گروهی دختران تینیجر سر پسرای ۴۰کیلویی در رضوانشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/152172" target="_blank">📅 21:20 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152171">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d829e5c716.mp4?token=Ha42xqSI_tgrKzPu5Rqcr2qibVQmLGd-U1FOmwO0HW1yLjXy9BPc79SbpgyiaP-EOMx1UEzcaSPhLAtN8uclOhI9o7E6_eAB76es7bIX4by1qn7Fvp7FQwOjYmXryo3GKW1vdY5ewUfKoOWQ3RCvRvy6MNv8wZ0j4HJqHQxrqKayHLs0KbjwVIq_zkHi7bOYlOqJ_osuuJAxLk7NsGxuYiRJ22zLOmvNWYIWbFQ9ygdjr7OnkzTMmPc39u6QKsOGz2RO075pognzgMgwp7OwxAylxGOGQXdYTTdUlG9B8PZkQwDnrCwijzmByxOOXil_NQBovx_AvX1cSpQ8f8dmbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d829e5c716.mp4?token=Ha42xqSI_tgrKzPu5Rqcr2qibVQmLGd-U1FOmwO0HW1yLjXy9BPc79SbpgyiaP-EOMx1UEzcaSPhLAtN8uclOhI9o7E6_eAB76es7bIX4by1qn7Fvp7FQwOjYmXryo3GKW1vdY5ewUfKoOWQ3RCvRvy6MNv8wZ0j4HJqHQxrqKayHLs0KbjwVIq_zkHi7bOYlOqJ_osuuJAxLk7NsGxuYiRJ22zLOmvNWYIWbFQ9ygdjr7OnkzTMmPc39u6QKsOGz2RO075pognzgMgwp7OwxAylxGOGQXdYTTdUlG9B8PZkQwDnrCwijzmByxOOXil_NQBovx_AvX1cSpQ8f8dmbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ظریف:
اگر لازم باشد باید برای بقای کشور به توافق‌نامه‌ای شبیه ترکمنچای تن بدهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/152171" target="_blank">📅 21:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152170">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
هیمتی: اقای بسنت وعده ای که دادی چیشد؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/152170" target="_blank">📅 21:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152169">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
بیانیه مشترک عربستان سعودی، ترکیه، پاکستان و مصر: ما حملات مداوم شبه‌نظامیان حوثی به عربستان سعودی را محکوم می‌کنیم
🔴
این حملات تشدید خطرناک تنش‌ها است و ما از پادشاهی [عربستان سعودی] در اقداماتی که برای مقابله با آنها انجام می‌دهد، حمایت می‌کنیم.
🔴
ما شبه‌نظامیان حوثی را مسئول این حملات می‌دانیم و از آنها می‌خواهیم که فوراً آنها را متوقف کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/152169" target="_blank">📅 20:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152168">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
نخست وزیر پاکستان: ۶ تبعه پاکستانی در حمله به فرودگاه ریاض زخمی شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/152168" target="_blank">📅 20:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152167">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfVox9u0VlG4K0IqbsSlArPfJvlF0Cn6zJ_Or1gtBUQ-Lu8amTV1KJ8np5zYjgORn_42bheKgf9XNh5ly0yF4uN4Im8Dh7fWzf7KuEweE8HF2iZMdtOc80Q9NnCMoR6abPVRH8M55JC0TpImAPuezyOe7fRaENRgru5BwvgF6wRp3xO_ANXo09m5D8WgmIZ9o509ASRMikiTzYkOp1RZRMmATmu1zruLAGJqQA983iUuAM120p3UfoqEJGciOJWsC_1O1ICOj4J6DKM_i4G_kLk_nslKjHy_i5I8YhNNW4UBLKdtgyRZ_uYd7QxMcN2LZcrLKRt8uBxncsHAcwUzcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باهنر خبر داد: زینب ابوطالبی مجری جنجالی «مملکت مال حزب‌اللهی هاست، هر کس نمی‌خواهد جمع کند از ایران برود»، از کشور رفت!
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/152167" target="_blank">📅 20:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152166">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">آیا دلار 300هزار میشه
⁉️
تحلیل عجیب نوستراداموس ایرانی
👇
https://t.me/+ViT7_yfzcKRmOTNk
https://t.me/+ViT7_yfzcKRmOTNk</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/152166" target="_blank">📅 20:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152165">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/604f2b0c98.mp4?token=GyZG1URhR1p0h9WEK8lVE93y1pvnHMOastwzi3SgUb1gnWxc3aNtFd6DRn9wU40mn-Py_S5D4pJ6hRj7Pzs1DSWdncJ-4SlWs66i6xO6uKcghPuM9Q10FgnHCcaC34B_Jk3Su9p6ZZLXVgRTWyW_T6KKhSuQsYUOryYSyTJcM-QaPvAMmxXqBytwWAMpCCyftgfpoGXTvNhkHyuI5xN01iUMuMw5KsOpImFIvBiKRKnf5k92sgyCZpl2rHSnoABU4dHdAgDF1ueXeVn7QBkDpVgVgvA7PYaL8AAa487-xvdmAUZEAIth4Gui961jLxqZK0OzWZtQo3E007ahwO18_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/604f2b0c98.mp4?token=GyZG1URhR1p0h9WEK8lVE93y1pvnHMOastwzi3SgUb1gnWxc3aNtFd6DRn9wU40mn-Py_S5D4pJ6hRj7Pzs1DSWdncJ-4SlWs66i6xO6uKcghPuM9Q10FgnHCcaC34B_Jk3Su9p6ZZLXVgRTWyW_T6KKhSuQsYUOryYSyTJcM-QaPvAMmxXqBytwWAMpCCyftgfpoGXTvNhkHyuI5xN01iUMuMw5KsOpImFIvBiKRKnf5k92sgyCZpl2rHSnoABU4dHdAgDF1ueXeVn7QBkDpVgVgvA7PYaL8AAa487-xvdmAUZEAIth4Gui961jLxqZK0OzWZtQo3E007ahwO18_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مرشایمر، نظریه پرداز معروف آمریکایی: ترامپ با امضای تفاهم‌نامه اسلام‌آباد سند شکست آمریکا را امضا کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/152165" target="_blank">📅 20:42 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152164">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdvtSG18k0dhx7Y81AjLeUsIpvh-sc9aqExuqvYT9BpHbhN5foPk3NqsLdC5Wg8mgwbZn0SBCdM0cDOXILXhe6ZyNP4tEC6GbUt16S4WPXLsFurlWtyhmAxua2bTE-EDl7Jg1p746clrfITRl2ZTnyuSMYirn06BdcthsiuxgYqMNyfQB2XePK6C3-PF8GO4DlmsrdaNhtdeGb6GTc8kLC7c3AgJqFSX3YX_qFqE8g6Y3aAEZjDO3nzcdwqAMfsxPtAtG3ZLaU3kznLYcZxHW30YABM_mSjvYqd5yL3Sr22XvoTHZ7DHCdms10VIbcNJbx3AWm-IjewDGTbl4B-FUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ در تروث سوشال:
اگر ممدانی می‌تواند با ترامپ به خوبی کنار بیاید، چرا شومر و جفریز نمی‌توانند؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/152164" target="_blank">📅 20:37 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152163">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
اسرائیل امشب در مورد ایران جلسه امنیتی برگزار می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/152163" target="_blank">📅 20:32 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152162">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/189ea383a3.mp4?token=AssNwKAZkkLZ5h5NcmMfsz6EzjJBqowNAf5etjYHOUjIAH5STd_CTZyCnbxqB3vw6m1ZOUPP5do6qIaVaCj2Pm_ZY67ZBaJjxBaK-pDbt7kb2W0nHOMpOdVDBPnDlvG71MlP2uSzkTkEld6BcEiVDAfksYStV0VcPcsDSYvQZG0xnWv_vCzlnOno7VCrDgYUmwICU1sDsJbGvdPi4VvS2NCGhvJ5GBydaVZcFzySmyFmzhxOQfXI_rntj7PSCiYsRSikL8a3l4iRf_Dr06Ewpl4gRc1pMXSSsyDlHLHXioWxeBs_YzwuvkabONPQdpRR9kJiT4Ig4cUXmLOhmUwMKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/189ea383a3.mp4?token=AssNwKAZkkLZ5h5NcmMfsz6EzjJBqowNAf5etjYHOUjIAH5STd_CTZyCnbxqB3vw6m1ZOUPP5do6qIaVaCj2Pm_ZY67ZBaJjxBaK-pDbt7kb2W0nHOMpOdVDBPnDlvG71MlP2uSzkTkEld6BcEiVDAfksYStV0VcPcsDSYvQZG0xnWv_vCzlnOno7VCrDgYUmwICU1sDsJbGvdPi4VvS2NCGhvJ5GBydaVZcFzySmyFmzhxOQfXI_rntj7PSCiYsRSikL8a3l4iRf_Dr06Ewpl4gRc1pMXSSsyDlHLHXioWxeBs_YzwuvkabONPQdpRR9kJiT4Ig4cUXmLOhmUwMKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
طوفان روحانی و ظریف علیه حجاب اجباری
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/152162" target="_blank">📅 20:22 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152161">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
فایننشال تایمز به نقل از مقامات ۵ سازمان اطلاعاتی اروپایی گزارش داد روسیه در حال گسترش برنامه‌های ترور مدیران ارشد صنایع دفاعی، به‌ویژه تأمین‌کنندگان پهپاد برای اوکراین است
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/152161" target="_blank">📅 20:19 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152160">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: دیگر پاسخی به پیشنهاد های آمریکا برای توافق نمی‌دهیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/152160" target="_blank">📅 20:13 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152159">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
وزارت دفاع روسیه: ما یک مرکز لجستیکی در میکولايف و یک کشتی باری نظامی که به سمت بندر چورنومورسک در حرکت بود را هدف قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/152159" target="_blank">📅 20:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152158">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
سخنگوی نیروهای مسلح یمن (حوثی ها): از آسمان فرودگاه‌های سعودی دور شوید
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/152158" target="_blank">📅 20:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152157">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7Kr2zAge10P_GjRZ4if9wzyNnKaDlMSZLv8rCw8-N08dpep6G6o0gHL-n3JVXrcb3hif2nh6fxteSPUuTIXgDCvNEp187Ec91Q3fBHerpJ-PJ7UTXvjYTItV_-uT9XgzAtag421F1MiIZ4qt6oHTBDINVRhz84prlJbg1eOAgUjfcpdNKca-4iRRrbz5iP8Gzu3O4nWpJO8cWxNJ-QFqq8vPNGK83P2p1cg6EMTJGaADxOkQnLi16X9oUGYB4SR0GBHEWwlML9ux6cYLacnK-mgq3ipPnEQiA4PjGgHZIsMxPNkxSdM7hY1RqWyNoKLMbOx-5baads7AYyN8mMrdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ده سال پیش با ۳۵ تومن میتونستی پژو پارس بخری، ولی امروز با ۴۰ تومن میتونی داشبورد پژو پارس رو بخری
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/152157" target="_blank">📅 19:47 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152156">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
هم اکنون گزارش شلیک موشک از جنوب ایران به سمت تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/152156" target="_blank">📅 19:42 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152155">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
انفجارهای جدیدی در شهر ریاض، پایتخت عربستان سعودی، رخ داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/152155" target="_blank">📅 19:39 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152154">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
زلنسکی: هم اکنون با مقام‌های ایالات متحده صحبت کردم، اوکراین از آتش‌بس انرژی حمایت می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/152154" target="_blank">📅 19:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152153">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: می‌توانستیم تنگه هرمز را کاملاً ببندیم، اما به دلایل انسان‌دوستانه این کار را نکردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/152153" target="_blank">📅 19:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152152">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
دونالد توسک، نخست‌وزیر لهستان، می‌گوید مردی که مشکوک به توطئه برای حمله به او است، دستگیر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/152152" target="_blank">📅 19:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152151">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
المیادین: نیروهای مسلح یمن به ۷ کیلومتری شهر تعز رسیده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/152151" target="_blank">📅 19:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152150">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: تهران به رویه‌های دیپلماتیک گذشتۀ خود باز نخواهد گشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/152150" target="_blank">📅 18:55 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152149">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‌
👈
فیلد مارشال محسن رضایی: آمریکا دارایی‌های بسیار گران‌قیمتی در امارات و پیرامون تنگهٔ هرمز دارد که ما هنوز آن‌ها را در میان اهداف خود نگنجانده‌ایم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/152149" target="_blank">📅 18:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152148">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: اگه دوباره جنگ بشه اینبار به تاسیسات هوش مصنوعی و دارایی های ایلان ماسک تو منطقه هم حمله میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/152148" target="_blank">📅 18:41 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152147">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
سراج نماینده مجلس: ۹۰٪ مردم خواهان انتقام از دشمنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/152147" target="_blank">📅 18:37 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152146">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
ولادیمیر زلنسکی، رئیس‌جمهور اوکراین درباره خاورمیانه: همه می‌فهمند که به دلیل جنگ در خاورمیانه، قیمت‌ها در حال افزایش هستند. آن‌ها به دلیل جنگ در خاورمیانه و مسدود شدن تنگه هرمز افزایش می‌یابند.
🔴
همه این را می‌فهمند. اگر می‌خواهیم با مردم به‌صورت منصفانه صحبت کنیم، اگر می‌خواهیم شفاف باشیم، اگر می‌خواهیم با ملت‌هایمان به‌صورت بازگشایی صحبت کنیم، مردم باید واقعیت را بشنوند
🔴
با مردم بازی نکنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/152146" target="_blank">📅 18:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152145">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1924f0c44.mp4?token=egHkD9bfqtXkwqbgojXWRTCBE3UZEReiC7QK0MV5zGvu_tCMImxvdc-ogzTQ0KkrMplE88gjxMPsgOrZYLkgTbcwvDPmE_Wg7075kCdGGD8N-7JUEND5CghAcpymBdwAbhOeBclTGE5AUBkUkEW_SWiHKOrFs5RJvNcLWAp0pdaLBPNlqwSmpO68qQgPdOD6AUsbXewEtScCRtr4BFdP6CERIN805M07Vf6s4bekkRE0FCyounImadtkszpKcY94LV19ik4uuoI57OOUtjHWWZH71kp2LrXVyFu3Ht3hdBNtZjm5nT2nOiK09vbYjkk5E5VCWcBBgm_DhiWiDLVSSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1924f0c44.mp4?token=egHkD9bfqtXkwqbgojXWRTCBE3UZEReiC7QK0MV5zGvu_tCMImxvdc-ogzTQ0KkrMplE88gjxMPsgOrZYLkgTbcwvDPmE_Wg7075kCdGGD8N-7JUEND5CghAcpymBdwAbhOeBclTGE5AUBkUkEW_SWiHKOrFs5RJvNcLWAp0pdaLBPNlqwSmpO68qQgPdOD6AUsbXewEtScCRtr4BFdP6CERIN805M07Vf6s4bekkRE0FCyounImadtkszpKcY94LV19ik4uuoI57OOUtjHWWZH71kp2LrXVyFu3Ht3hdBNtZjm5nT2nOiK09vbYjkk5E5VCWcBBgm_DhiWiDLVSSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یکی از فرماندهان جوخه نوخبا که در ربودن اسرائیلی ها در 7 اکتبر شرکت داشت در عملیات مشترک ارتش اسرائیل (IDF) و شین بت کشته شد. او یکی از رهبران حمله به پاسگاه کیسوفیم بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/152145" target="_blank">📅 18:32 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152144">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f80c226d.mp4?token=ieUYGwZt-VaalxiPc5aP31b2-i7GkNhBWi_q2VBkavtc-Qf_AORizeYGGrc-Vh-YlDL6LXxitYIsKq6p1JnudVpsOc3GihTFoaN7SB53PmXAk8yDOTXHJLaDClULgyzChnL-r1AU572VARF4rHM0eu9IexzIcd1w2dXC49EhfamichRQQ-09Fa4qYISdxL5Ly1e1a6LSOJRVoH_k_FqkRNDeziO1RTKvEr5sHOWY4wj6j9dIrstce-YNMkUDKvmpVkQN_rykGB-6JTPceA8asVJyfQtlRvha1s5tHjHLRbFD2p8LgdD-u4lJFq9fA1Z_8wcwb9-xKHldq2vEeylr5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f80c226d.mp4?token=ieUYGwZt-VaalxiPc5aP31b2-i7GkNhBWi_q2VBkavtc-Qf_AORizeYGGrc-Vh-YlDL6LXxitYIsKq6p1JnudVpsOc3GihTFoaN7SB53PmXAk8yDOTXHJLaDClULgyzChnL-r1AU572VARF4rHM0eu9IexzIcd1w2dXC49EhfamichRQQ-09Fa4qYISdxL5Ly1e1a6LSOJRVoH_k_FqkRNDeziO1RTKvEr5sHOWY4wj6j9dIrstce-YNMkUDKvmpVkQN_rykGB-6JTPceA8asVJyfQtlRvha1s5tHjHLRbFD2p8LgdD-u4lJFq9fA1Z_8wcwb9-xKHldq2vEeylr5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ولادیمیر زلنسکی، رئیس‌جمهور اوکراین:
ترامپ گفت که اوکراین به یک رئیس‌جمهور جدید نیاز دارد.
🔴
با تمام احترامی که برای رئیس‌جمهور ترامپ قائلیم، انتخاب رهبر به عهده مردم ماست
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/152144" target="_blank">📅 18:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152143">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f92ae82a3.mp4?token=vJbi3PABjdQxua7yKubCM2wYJYx_a2zcAKSLF4n99jMHrbERBp78txEPxgJc00cEn6j2xjL8WXDlPQuB9TYKzivmALiVc0n1iijsoYseDPB0vyzLpa6QZHL_rdarBEOxLjSo33-jBPncz3-KMFHM35_D2j6IsY3wfb03XXrNpeFPi9mQzP20LNlvlgbrO03RPrmoicL3ceMYISZkbWVL1Mj3ATv11yyNZuiJt_WBA404pXeB8X3AsJ54pKCjkUOdHAFk37qaKlBQTg4p7T0G9k_gQYJ-OwQ84Cbv9QAkMXh5lCCi0KvoMOrJuyQYwhJOLBnd0JqbSunDlFSeQbnY6Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f92ae82a3.mp4?token=vJbi3PABjdQxua7yKubCM2wYJYx_a2zcAKSLF4n99jMHrbERBp78txEPxgJc00cEn6j2xjL8WXDlPQuB9TYKzivmALiVc0n1iijsoYseDPB0vyzLpa6QZHL_rdarBEOxLjSo33-jBPncz3-KMFHM35_D2j6IsY3wfb03XXrNpeFPi9mQzP20LNlvlgbrO03RPrmoicL3ceMYISZkbWVL1Mj3ATv11yyNZuiJt_WBA404pXeB8X3AsJ54pKCjkUOdHAFk37qaKlBQTg4p7T0G9k_gQYJ-OwQ84Cbv9QAkMXh5lCCi0KvoMOrJuyQYwhJOLBnd0JqbSunDlFSeQbnY6Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ولادیمیر زلنسکی، رئیس‌جمهور اوکراین:
اگر ترامپ واقعاً می‌خواهد انتخاباتی در اوکراین برگزار شود، لطفاً به پوتین بگویید: به ما دو ماه، ۶۰ روز آتش‌بس کامل — ۶۰ روز — بدهید و ما انتخابات را سازماندهی خواهیم کرد
🔴
البته، ما برای هر انتخابی از سوی مردممان آماده خواهیم بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/152143" target="_blank">📅 18:21 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152142">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f68a497b55.mp4?token=sUVxWwcosuP4LBrZm-tBrMnkzw1PbxcdM4mdNDfMgFjKXQwMCiIyO_sEGeaqYS1z7l1MKrTUKisHOomufRhseTpUQ52T0S5IqNz5uWLdaoaTQhO7FqNT78gOrpRuSUO8gh6V-xLtYXeGi1mONDFyIA40oZ8ql-xirQ-SoxQqrX2JU6wWzyUwUSVAyNQiQTlXv-PdfZLEWS-S6qOHkGmPDcYe1imDC9RgAzeLPB2blt7xBvu4dcLbukVH40BtVOXFjuGBEm18wK3lMokkRWN6aNTX1p3c_fwIziR7_ZeYw6S4sMC0bRZvW9nF25Y8WLXsCcdlPamPTqeJ8BnOiE7naA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f68a497b55.mp4?token=sUVxWwcosuP4LBrZm-tBrMnkzw1PbxcdM4mdNDfMgFjKXQwMCiIyO_sEGeaqYS1z7l1MKrTUKisHOomufRhseTpUQ52T0S5IqNz5uWLdaoaTQhO7FqNT78gOrpRuSUO8gh6V-xLtYXeGi1mONDFyIA40oZ8ql-xirQ-SoxQqrX2JU6wWzyUwUSVAyNQiQTlXv-PdfZLEWS-S6qOHkGmPDcYe1imDC9RgAzeLPB2blt7xBvu4dcLbukVH40BtVOXFjuGBEm18wK3lMokkRWN6aNTX1p3c_fwIziR7_ZeYw6S4sMC0bRZvW9nF25Y8WLXsCcdlPamPTqeJ8BnOiE7naA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ولادیمیر زلنسکی، رئیس‌جمهور اوکراین
:
اگر به دنبال آتش‌بس انرژی هستند، ما برای این موضوع آماده‌ایم
🔴
ما را حمله نکنید؛ بچه‌هایمان را نکشید. ما حمله به دیزل شما را متوقف خواهیم کرد.
فکر می‌کنم این یک توافق منصفانه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/152142" target="_blank">📅 18:20 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152141">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
اسکات بسنت : ترامپ انتظار نداره تا حداقل بعد از انتخابات میان‌دوره‌ای، شاهد درگیری‌های نظامی جدی باشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/152141" target="_blank">📅 18:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152140">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
فوری / سخنگوی ائتلاف به رهبری عربستان سعودی اعلام کرد که دقایقی پیش یک پرتابه به ترمینال شماره 4 در فرودگاه بین‌المللی ملک خالد شهر ریاض اصابت کرد.
🔴
در حال حاضر، مقامات در حال رسیدگی به آتش‌سوزی ناشی از این حمله هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/152140" target="_blank">📅 18:09 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152139">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qa_TGxrsGzdVVLBMNMasCGy7zqtusIQAjUNtAj8GN7WBBRGi_zkD6TYa-efnfcdXPnwq8LtfImGr9wouPxHXcdFyaf2a_rxs6RKWBxm3isxBLUQtPG5__JpOx3pWIZPWH4ZZ0ZxYGr6AFOFlDInIJbN3ETfGhprbj9uZErL7CD5uDI4OHhlKeQ-uJkurvaemEp0UURbqxo95gWnaajD8VsH7dTjH0lDdeJIGhnEaRvCS5MWGW5AdiRF-XXjhVKG5yxFf3rSMuoge80hExEKFLqOT7QTu_FiPDTgsJ0Po0uYzXPbVkuGmqRXlGqSsendC6_CncQYZxkotUdQb61HGaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نتانیاهو: اسرائیل چشم‌انداز یک خاورمیانه‌ی قوی را در نظر دارد؛ خاورمیانه‌ای که در برابر تهدیدات متحد باشد، از مردم خود محافظت کند و آینده‌ای از امنیت، همکاری و رفاه را برای تمامی مردم منطقه رقم بزند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/152139" target="_blank">📅 18:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152138">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6sIy6HgtY4m2-tcnQYMVfNNqma799Bc991UF1THZv-IkUFZUJEopEFzC0aNf9w86WceFh0bbGg2uRi3W-f42RCk4eFW22JErKdu3gEb-0uN5Q-_zlFVU9gKLU2pcuLZFrheNLhsPWbpKp3XI7rj62RtvRXWMXEfJM4KpeB8hqaNTFBwfDZk3pH9PYFPQfWwkPPoqouXIVZLi2tU3Q-U6QywPZp0SwgbDGeFYfBmcpOTubAX2es3DuizWm383yW4AW-9ONzbz4YMeEIZyDhjYYFWK0ryY_pbzFDUsdyLybJnOjTLsv4_JuTNz-psov5wU31g3xYYaghhjRCHUDl5_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: از این لحظه به بعد، یک "توافق آتش‌بس انرژی" در جنگ بین روسیه و اوکراین برقرار می‌شود.
🔴
هر دو طرف با این موضوع موافقت کرده‌اند. لطفاً این توافق را نقض نکنید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/152138" target="_blank">📅 17:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152137">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
اسکات بسنت :
ترامپ انتظار نداره تا حداقل بعد از انتخابات میان‌دوره‌ای، شاهد درگیری‌های نظامی جدی باشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/152137" target="_blank">📅 17:51 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152136">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cfeac3aa6.mp4?token=krqdB9xM0TJehzHAlFz3pzZr0a3TiGAmWzcNKRC8XS1t41Qe74CT3jKwOjper_RkT_Rr511S7IJK6dkySsj_4N3srcCeHaedmbQn40E39DN1Fa0HZ17TP7z9KhztD-fIU_CGRXzGig3MyG8LViHB57eXP2DtMgTVOtsuUlysSEyURxBJkXEt5VGBENUPBDeKCpGdKLkNNI4hdRJcL8PEx6oIUzWdePbFWGuCCdR2vW4wtBOOMrKlsbHy23y2kxr-VE5zOmNMFYou3idU8_CfMG8LNS8jsCF1Cgor_bhS52aoMmWLZspGXmdXsV5e3HgWVosQazRyXjizDrDU5AzFGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cfeac3aa6.mp4?token=krqdB9xM0TJehzHAlFz3pzZr0a3TiGAmWzcNKRC8XS1t41Qe74CT3jKwOjper_RkT_Rr511S7IJK6dkySsj_4N3srcCeHaedmbQn40E39DN1Fa0HZ17TP7z9KhztD-fIU_CGRXzGig3MyG8LViHB57eXP2DtMgTVOtsuUlysSEyURxBJkXEt5VGBENUPBDeKCpGdKLkNNI4hdRJcL8PEx6oIUzWdePbFWGuCCdR2vW4wtBOOMrKlsbHy23y2kxr-VE5zOmNMFYou3idU8_CfMG8LNS8jsCF1Cgor_bhS52aoMmWLZspGXmdXsV5e3HgWVosQazRyXjizDrDU5AzFGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسکات بسنت، وزیر خزانه‌داری ایالات متحده:
بزرگ‌ترین بازنده در اینجا رژیم ایران است.
آن‌ها سعی کردند یک نقطه گلوگیری بر تنگه هرمز داشته باشند. این کار جواب نداد.
آن‌ها سعی کردند نقطه گلوگیری بر قیمت دیزل داشته باشند. حالا این هم جواب نمی‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/152136" target="_blank">📅 17:47 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152135">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4be03fff7.mp4?token=MbU6lFCXV2AAGJHAtwUxPZz_BHOL_34ofRPBAwNNhc_QUdevGavnLLRMtUQF10vKj5xcZX35vwj8U7YENRCZsyvUrw84cbhNLzvAtlbieIKZtgLrvbAhEfGRgFsIlMxsFi8ByQPyCKK903N2GmvDjnAj2gWMXKdAtC3Sot9SJS9okW8qsWirQ2Xq3f1RUJubkhYUmqaEOWcrOnJDmmD_FFMIyEOb2xD9useOC11vGQvrN02-p49E8GLaWeCI5MAcKREP8nXEzM6ya9urcUKL49n6-AtmWe9Ym53KmWhOtRustqjl9ESBNRgqq0yf5mdyI2MNmqrQ4rMVw-aa88fs_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4be03fff7.mp4?token=MbU6lFCXV2AAGJHAtwUxPZz_BHOL_34ofRPBAwNNhc_QUdevGavnLLRMtUQF10vKj5xcZX35vwj8U7YENRCZsyvUrw84cbhNLzvAtlbieIKZtgLrvbAhEfGRgFsIlMxsFi8ByQPyCKK903N2GmvDjnAj2gWMXKdAtC3Sot9SJS9okW8qsWirQ2Xq3f1RUJubkhYUmqaEOWcrOnJDmmD_FFMIyEOb2xD9useOC11vGQvrN02-p49E8GLaWeCI5MAcKREP8nXEzM6ya9urcUKL49n6-AtmWe9Ym53KmWhOtRustqjl9ESBNRgqq0yf5mdyI2MNmqrQ4rMVw-aa88fs_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسکات بسنت، وزیر خزانه‌داری ایالات متحده:
اگر این ایرانیان کشورشان را دوست دارند، تبریک می‌گویم، می‌توانید آنجا بمانید.
این موضوع به نخبگان ضربه می‌زند. آن‌ها نمی‌توانند به دیدن خویشاوندانشان در لندن، دوست‌دخترانشان در پاریس یا پول‌هایشان در سوئیس بروند.
آن‌ها از جهان قطع شده‌اند. ما فشار را ادامه خواهیم داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/152135" target="_blank">📅 17:43 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152134">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
سفارت استرالیا از شهروندان خود در ریاض خواست که در محل امن بمانند و پناه بگیرند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/152134" target="_blank">📅 17:22 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152133">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
فاکس نیوز به نقل از وزیر خزانه داری آمریکا: ایران دیگر نفتی در کشتی های خود ندارد و جریان نقدینگی آن منفی شده است.‌‌
🔴
پس از کمپین فشار حداکثری علیه ایران، اکنون به سمت کمپین انزوای کامل رفته ایم.‌‌
🔴
کمپین انزوای کامل با هدف قطع روابط ایران با جهان خارج…</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/152133" target="_blank">📅 17:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152132">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
فاکس نیوز به نقل از وزیر خزانه داری آمریکا: ایران دیگر نفتی در کشتی های خود ندارد و جریان نقدینگی آن منفی شده است.‌‌
🔴
پس از کمپین فشار حداکثری علیه ایران، اکنون به سمت کمپین انزوای کامل رفته ایم.‌‌
🔴
کمپین انزوای کامل با هدف قطع روابط ایران با جهان خارج است.‌‌
🔴
با مصادره ارزهای رمزپایه و تشدید محاصره دریایی به ایران فشار خواهیم آورد.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/152132" target="_blank">📅 17:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152131">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
فارس: با پایان دو هفته، وعده بسنت درباره فروپاشی اقتصاد ایران محقق نشد و دلار از ۲۷۲ هزارتومان به ۲۶۵ هزارتومان رسیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/152131" target="_blank">📅 16:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152130">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52393bf294.mp4?token=lVzD_fWXfccI7lNIDDBbJF3q2u0OkhPhtLqDicTBShipHl4qUMB4cNVAowCsfUxfYRJiawor-G5O7aEhjvrqtI2Vd4UpeRXdX9KvCexs44Zme9qOtth2oLdsXdCVsdtc4rBoGVISsSbfhJiiWccr58q0fUoEy2t6C5tLdwkbpAovT9C3le9EJnQZpFrqcW2WlGiYq2XOMwhoG1VCxuHnw9uUjryVUivtGE0FeXbG3kgoQJOxFjhnexLuYZNq3kp4vij7HwJeQgIVNmOMixNg49g-QGU1DUh7vif7DqUEFTdciPPgXIOqPzqapnMKVVpRBB_lzRYfbG4eljVB9riJfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52393bf294.mp4?token=lVzD_fWXfccI7lNIDDBbJF3q2u0OkhPhtLqDicTBShipHl4qUMB4cNVAowCsfUxfYRJiawor-G5O7aEhjvrqtI2Vd4UpeRXdX9KvCexs44Zme9qOtth2oLdsXdCVsdtc4rBoGVISsSbfhJiiWccr58q0fUoEy2t6C5tLdwkbpAovT9C3le9EJnQZpFrqcW2WlGiYq2XOMwhoG1VCxuHnw9uUjryVUivtGE0FeXbG3kgoQJOxFjhnexLuYZNq3kp4vij7HwJeQgIVNmOMixNg49g-QGU1DUh7vif7DqUEFTdciPPgXIOqPzqapnMKVVpRBB_lzRYfbG4eljVB9riJfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شعار امروز بسیجی‌ها مقابل سفارت فرانسه:
🔴
مکرون حیا کن دانش آموز رو رها کن
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/152130" target="_blank">📅 16:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152129">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
صداوسیما:
درود به شرف اعتراض کننده های فرانسه
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/152129" target="_blank">📅 16:35 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152128">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: با پاکستان و ترکیه همکاری می‌کنیم تا همه مسیرهای زمینی ایران را قطع کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/152128" target="_blank">📅 16:21 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152127">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
حسام الدین اشنا:
راننده تاکسی بازنشسته سپاه بهم گفت شما اینقدر نامردید و لج منو در اوردید، که از لج شما می گویم رضا پهلوی
تا بسوزید و این بلارو شما به سر من اوردید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/152127" target="_blank">📅 16:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152124">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sC_PUqHDvbKuvinN1OJNyioOSrhLq14IG0hZpGsMeuBBO-Pcx3G4mchvPCrU7UuzV7c9ZwSgebVRe_2Hloa3aGwGHkeeN_vbKVJzrnu2osekLEGvWFNre9ep5T56Ui3z-CLymJjCqeKETIf0QcwXPUyue5VVXH6HviWAh3yFUow3bJeh49CEKTqkqPT7f0g5V5IQAq_qHiSpgDVtcs-NBPOYVNdVN8_yIyiq5M5Qo9H6kv8pnSUNOACS2OBk1Rc0KG1j0HRaR-NKYCyFFmJgXBDQDCfVUqVFPAkqWGpUZdj-_YkztIYzN_FAJO0C9sLadsuQQoZN3DQXlqfw9gt36g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X9MI13mPAepaPrtMwkhGqHv25myT87xTZkNOgzvtKBtMGN2RgTzbOUG7gn9nlaWTa-f7F1oX2bj__mB8S52SG-gxR7jkkXte5mwhkdIc0G-WWbAD1teIiJkjNuSym3mrKQCwSM2hdz_Vr5Pt9Fu65fyTITlzxQ9CkKIThSFC6GGviFcuD0Amwgf9e8Sx_H3lr1W9EOnP130EkkV7mocfGMyFORbX_dAHBj85WUCQ_4VU1m56YC1qSSiI1BEyRV3TEEG_yOdPUbM_qbDkDGKUzbd-KIcFRPgCRXJ4EKte5I-ep-BAgiVbI8kl4go-eIgMxtu4GmTG2j-vcbUJRdm95w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jKDcvqk6XS1IJXNAcoKPDt58OfV__OdyEpnfHIJ028zBgVyNCGRevZAyNPdy9A1Bvpg_F46coYxxaBx4zkJWjEk65QBm_cmRGo2nllNI7AFLPJPC8V2iJTrdPh9FZeKMRM63iC4UOjPpmYvGcWxwXcs49gv30hXUvXV3QwYQwr6zRBjZli_Dp8A9s_a5DSAod5p19atLXqS0WH3tLYx-oJgnJqLFYNLbEk6mZXW9UtKHquy-lXEmeOhKHTvj7PoPZmNdc8BKiWOmJmKRJzDPc3GDh1Xe9OL4NPRtybgi5tAUiq4xc-wWdrqs3BVu91ozGMK--8E6vM7iaOvmYSm_PQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
هوای تهران امروز خیلی تمیز شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/152124" target="_blank">📅 16:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152123">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
فلای‌دبی به‌ دلیل تداوم شرایط ناپایدار امنیتی، لغو پروازهای خود به مقصد و از مبدأ تل‌آویو را تا پایان اکتبر تمدید کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/152123" target="_blank">📅 15:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152122">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cf041a409.mp4?token=gWKjZFiRKOn55CrOyEANtfl8yw-IpXCeIS797HgIpxBSIr-d2bZNvjdQXURkPcvL8pz91pQURAOSmOea6v5col80QJnUo-zMrQ1GE4KSIljt3xAS4v2yF4DPAMIWhtQSfkSpTzVqUSa8jkl3OzAz11vrdVDWFOZTZV2McRLzi2hRpF_cxuxUR9dOhe5C2GzapyVCnOMXfcCRHfww7DqwC-8SGuNt0lZN2stLhxtf7XbBxdUDf3kmozls1V9t_hIBiITQevYjjIra8ybMssUx0bvmAWWFpb6sZy1Oo1Gc-Gxa8MRPT2QN12-BI5tkOsdTvOl7p23u9n-Le_pP4CWKtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cf041a409.mp4?token=gWKjZFiRKOn55CrOyEANtfl8yw-IpXCeIS797HgIpxBSIr-d2bZNvjdQXURkPcvL8pz91pQURAOSmOea6v5col80QJnUo-zMrQ1GE4KSIljt3xAS4v2yF4DPAMIWhtQSfkSpTzVqUSa8jkl3OzAz11vrdVDWFOZTZV2McRLzi2hRpF_cxuxUR9dOhe5C2GzapyVCnOMXfcCRHfww7DqwC-8SGuNt0lZN2stLhxtf7XbBxdUDf3kmozls1V9t_hIBiITQevYjjIra8ybMssUx0bvmAWWFpb6sZy1Oo1Gc-Gxa8MRPT2QN12-BI5tkOsdTvOl7p23u9n-Le_pP4CWKtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر جدید از حمله به فرودگاه ریاض که دیروز رخ داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/152122" target="_blank">📅 15:51 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152121">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
گفته می‌شه آمریکا پیش از شروع جنگ، نیروهای نخبه‌اش رو برای عملیات‌های خاص تو ایران مستقر کرده. هنوز هیچ مقامی این ادعا رو تایید نکرده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/152121" target="_blank">📅 15:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152120">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
مرکز آمار: جمعیت فعلی ۸۷میلیون نفر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/152120" target="_blank">📅 15:43 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152118">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oQRVaSirYta2EHyg6vjoKy4Iva_2kcKqVLf0Qu3rKZzDEZZDsVlAfqrUgi9poqXM7pfvReUt1wzK74tFae55kpShr-9rbybe4I1kXHhpivlEZEbM2xmQVACeC5yAawWUkqrDkNbYX6xZ0TF7wVxsRMZVaUryHhsPlWxRvJ0Zpw1FlODqr9l-hqLErHbF5p1vwfoOcBufcTiDxzJkvLVWGyJOYe3YVTYGnE8RiBPXa-Pdb-mi8jmfE9uDZL_xAocIAwQkbQCl3Bc5i0jIl_vEXcuhcpGSLxFupipPzUKoQKhzrYe82TuwJp18EKd11fQybHSzv58NHvTCv4U7-OxoZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U29ugYadJ62psep8NeGpIPTPerDFcib02TxYC0JxM263_rmPKM-8yD1t3lhREOcfMuiTY7BvIg0u8_LZieo75YWqD-Picj2T1HQR0JUu-PTqZTiESIG4mfDAOA14V13gPtjxtQPjSksQxzvtf1u-MyWidjzBbkpIdNjZeECON39bQpJQflfRCyBpkb4-QrWfVkUCZSXvSOKSE7hYU462bhNyTCUGhQKYFpepL82hu7X1pco_tNvJFIz4gP5bckAY1qGprZnFDsE2-vCxGjg_QScmOd216EqXF1j6bvVKQ23tamQXzlwpyAJsO-JQma-ivHvNsWrynLNAiuOeUxOIpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر وایرال شده از رزمایش امروز جانفداها تو خراسان جنوبی و استفاده از کودکان.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/152118" target="_blank">📅 15:37 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152117">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
شرکت فلای‌دبی لغو پروازهای خود به تل‌آویو و از تل‌آویو را تا پایان ماه جاری تمدید می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/152117" target="_blank">📅 15:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152116">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
خبرنگار رویترز: آمریکا ممکن است نیروهای نخبه را برای عملیات های خاص قبل از شروع جنگ در ایران مستقر کرده باشد.‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/152116" target="_blank">📅 15:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152115">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aea388dc62.mp4?token=MDJGKdbWxXZRT5KX2JPC4LOSklG0XqfP8LDaAIlasUjX6rOzkqnBbjfIBWwEJD-Fa2RlxTn4dyC5VMDlYfnNdgnGsR7h3qKDGA4P245vvi5aXYwV5kjeR9P4TRZBKTL5R2HweI5UxdmDBEq7wEqWoAmb48DjpiqeekWtw8hrV2OwVJtXi8dzs7RyYArypTa3qE5cR_QnNWIGBHv7FwHYz6cmjDs-SV3s3ZltUSfbQH30A5lg5oFHkaI_7f7CacDQA9YkUiGAVqr9jklYszw2GvCVhihO4xdo4d50s20d0Rd0sWm1xnF4j-E173zgipHG8FoiqMDTb2rE0N6XUFPMIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aea388dc62.mp4?token=MDJGKdbWxXZRT5KX2JPC4LOSklG0XqfP8LDaAIlasUjX6rOzkqnBbjfIBWwEJD-Fa2RlxTn4dyC5VMDlYfnNdgnGsR7h3qKDGA4P245vvi5aXYwV5kjeR9P4TRZBKTL5R2HweI5UxdmDBEq7wEqWoAmb48DjpiqeekWtw8hrV2OwVJtXi8dzs7RyYArypTa3qE5cR_QnNWIGBHv7FwHYz6cmjDs-SV3s3ZltUSfbQH30A5lg5oFHkaI_7f7CacDQA9YkUiGAVqr9jklYszw2GvCVhihO4xdo4d50s20d0Rd0sWm1xnF4j-E173zgipHG8FoiqMDTb2rE0N6XUFPMIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای آتش‌سوزی‌ای را در سواحل عمان در پی هدف قرار گرفتن یک کشتی ثبت کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/152115" target="_blank">📅 15:21 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152114">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
لبنان بزودی به پیمان ابراهیم خواهد پیوست
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/152114" target="_blank">📅 15:16 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152113">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
احتمال تماس تلفنی اعلام‌نشده پوتین و ترامپ
🔴
دیمیتری پسکوف، سخنگوی کرملین، اعلام کرد که ولادیمیر پوتین، رئیس‌جمهور روسیه و دونالد ترامپ، رئیس‌جمهور آمریکا، ممکن است تماس تلفنی دیگری داشته‌اند که به‌صورت عمومی اعلام نشده است.
🔴
پیش‌تر، یوری اوشاکوف، دستیار پوتین، درباره تماس اخیر دو رئیس‌جمهور گفته بود که هیچ‌کس نمی‌خواست اولین نفری باشد که تماس را قطع می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/152113" target="_blank">📅 15:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152112">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMXuJwL4MPK-MYPS05Uk53Joctqt_Hr6mwWdsSIuDcGZ30fzpAVSstMOU-kwXaLdau8eXT0JKKOAj5syts2V1IdHgSS6ziTpkHqI8pWQ0P2gUEXpXAUuqmb4dcjDGQBitFzkmU09JgQUNYBsp7UMfTf2_w_tZdWilqL3NAWICPD_SkGUz8AwuyTBGluo36aP7xExhc3xZ1K0NOYMXKHB2MAZMT1rW6wt_EaVnrXBX7SprI7yslrLFhDITF8oa531FlDHWNGDtUms_3Sv6qE1AUuEuZVEfyXGxI_LINGoD0LcrMDNyRjGrow3e_WZe2vr6KBvRl0SRhPctFLDcCzwGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جروزالم پست: در میان 8 کشور، کویت، لبنان و سوریه در صدر گزینه‌ها برای گسترش توافق‌نامه‌های ابراهیم (عادی‌سازی روابط) قرار دارند؛ طبق گزارشی از شورای امنیت ملی آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/152112" target="_blank">📅 15:10 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152111">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUlo84umKfmQchJ35Mnueidmc79lWLlzoSpByNOIy2S1vuPuUCjzwgkgsuFSLX8q66ow2T0e5yeenSkzoSxWh2XdNSdKwpf1pCOWxEfyejiX3xzq3fdYd6m2QRPuF8MvxA8ay4uwfExHyHhOYxHH5lCRAXGJ1KXIw4d03WaLmTs67c8B7UNr7H1zt-h_nsq6AvAt-UASlGLj6Qu4rDZZV_UocvXTHIjd0c6vc1kbf4VUQjZJDdJz_q8g0qt-L13qhO6b2USzRPf0FRZE0ktBXClRTidQZe01eTtgcBjzo2mU8qJcZCV5sUpp7h9donBhtBS-HMKSzkymQFGd_YeylA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم‌زمان با هدف قرار گرفتن یک کشتی در تنگه هرمز، آتش‌سوزی در این تنگه در فاصله 25 کیلومتری از سواحل عمان مشاهده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/152111" target="_blank">📅 15:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152110">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
رئیس مرکز آمار ایران: برآورد فعلی جمعیت کشور، مطابق برآوردهای پیش‌تر اعلام‌شده، حدود ۸۷ میلیون نفر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/152110" target="_blank">📅 14:55 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152109">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
گزارش انفجار در تنگه
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/152109" target="_blank">📅 14:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152108">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
پزشکیان: در همه برنامه‌‌های آموزش و پرورش دنبال عدالت هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/152108" target="_blank">📅 14:44 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152107">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
سخنگوی سازمان مدیریت بحران کشور: تا این لحظه ۴ نفر در اثر سیلاب و ۳ نفر بر اثر رعد و برق جان خود را از دست داده‌اند و دو نفر دیگر نیز در استان گلستان مفقود هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/152107" target="_blank">📅 14:41 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152106">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
صداسیما خیلی جدی معترضان فرانسوی رو دعوت کرد بیان ایران تا همونجوری که میخوان زندگی کنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/152106" target="_blank">📅 14:36 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152105">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
شهباز شریف: مصمم به تقویت روابط با ایران هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/152105" target="_blank">📅 14:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152104">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
دنبال یه کانفیگ ارزون با سرعت بالایی؟
🔥
با ووکس حتی تو قطعی اینترنت هم وصلی
💢
@VOXNET_BOT
💢
@VOXNET_BOT
✔️
میتونید با خیال راحت تهیه کنید</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/152104" target="_blank">📅 14:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152103">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67683d5f7d.mp4?token=XtHsXYpyDWTdTYu1hZEQVk2AxAwWWSYuteKewqKgMuBQPjVFiiQZ4mEI4MGPGG2Rvfunu_wajp_QpHqkfgDQKaIiVHYJXfTFRGXPrvRNppG1p200hav40EZVRDNa4GQHF2UQB2USvqeJj7Sc_6ZokPuRzU8Bm1VrbuTg1bDK1OMC3_YOp1zE9EFV2qx2qHyoTJ1G6L1f2uLxoVpde4UIbwLW8HglMPr8m6Z8NsXCSxUhyhOcm1OK0qZfjFsWRherpBDGG6K15IlnkXCgrjFiKhoJa4jICI9mDjvqP_MCCrZUf4Xy5arVtyM-G3TfOY3JWQY_dI0INe85lbf3AAuxog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67683d5f7d.mp4?token=XtHsXYpyDWTdTYu1hZEQVk2AxAwWWSYuteKewqKgMuBQPjVFiiQZ4mEI4MGPGG2Rvfunu_wajp_QpHqkfgDQKaIiVHYJXfTFRGXPrvRNppG1p200hav40EZVRDNa4GQHF2UQB2USvqeJj7Sc_6ZokPuRzU8Bm1VrbuTg1bDK1OMC3_YOp1zE9EFV2qx2qHyoTJ1G6L1f2uLxoVpde4UIbwLW8HglMPr8m6Z8NsXCSxUhyhOcm1OK0qZfjFsWRherpBDGG6K15IlnkXCgrjFiKhoJa4jICI9mDjvqP_MCCrZUf4Xy5arVtyM-G3TfOY3JWQY_dI0INe85lbf3AAuxog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از سیل وحشتناک در نپال
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/152103" target="_blank">📅 14:13 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152102">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
شرکت آب: قبض آب یه برج تهرانی شده ۳۰ میلیارد، مردم رعایت کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/152102" target="_blank">📅 14:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152100">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/r-k6Nrd2D6o-VGgAXfZlJLI2CdsP3LfTCngN5BQbr5uRkT2YQPrrD-KWJKMIuXO3BwArzu1ImnA8lsIhs8rakMDv-UO3HWW9WfArOal-czAZJPutA2M5PBmNcRDbxI9X7N0VcyecDltLiC-oFqUEMuSZ7WHeq2-o-tLT4UYblbZ3J6WijuL73k7b3GCbhJAWDU0eYcEbSF8PSBJyzVIAa_fedXp_FwGVat8Mgji-d0GmOm-mrPJJchn9wpwUX074WnNwyyb1QhsmVPw6UGaS-BgX4W9euOTRmnsvxBia1pwXlj5ZIlIX6_Nl10kMwJlrMlsWXtPc_bzch1yhUuXTWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mo83coDloXJCQleUQTR9hd2omMBBsTWyOOPGlMcE-VEdcEwvSneGQN_Rz1XDogPhak6ztenY4lmO2SYWF5w9pJOToCKcen4QBRegADhduwVW9kfkjzej8sF6l2HrYh9d1OXFJn9iUIR7uiqqfATG5FiRo3hLNPyGUbPBVmrX6WhkjzEHYMOpLT2UHwsYPtPpIk3U2_V35OMC5NUF8n4y6M32AzqiNHoSDlk1Qc42dacl57U7XA-DR38K0USACIMFytxGaLDv7X0ws91AY2wX59oLk7w4E7H8Ce9nbahnCUmbOwb2qVbXQvu4FC8uDKl-9KppsG5Zb0QLWAo0NnFmug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر وایرال شده از رزمایش امروز جانفداها تو خراسان جنوبی
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/152100" target="_blank">📅 13:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152099">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
روایت المانیتور از سردرگمی در تل‌آویو در مورد قدم بعدی ترامپ: منابع سیاسی در اسرائیل می‌گویند نگرانیم ترامپ با پایان جنگ موافقت کند و درباره برنامه هسته‌ای تهران امتیاز‌هایی بدهد
🔴
در تلاشیم بر آنچه در حال رخ دادن است، تأثیر بگذاریم
🔴
آمریکایی‌ها به تدریج از ادبیات برچیدن کامل ظرفیت غنی‌سازی و خارج کردن ذخایر از ایران، به سمت کاهش چشم‌گیر ظرفیت غنی‌سازی و رقیق کردن ذخایر حرکت می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/152099" target="_blank">📅 13:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152098">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
سخنگوی سازمان انرژی اتمی: اگر منافع ما در دیپلماسی به دست آید، چه بهتر
🔴
صنعت هسته‌ای ریشه در ایران دارد و نمی‌تواند با ضربه از بین برود
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/152098" target="_blank">📅 13:38 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152097">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
زلنسکی: اوکراین آماده است تا حملات خود به پالایشگاه‌های نفت روسیه را متوقف کند، اگر روسیه نیز حملات خود به زیرساخت‌های انرژی ما را متوقف کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/152097" target="_blank">📅 13:31 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152096">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
سازمان ملل: در پی غرق شدن یک قایق در سواحل جیبوتی، 109 نفر جان باختند و 116 نفر مفقود شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/152096" target="_blank">📅 13:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152095">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
دادگستری استان اصفهان: شناسایی افراد «تن‌نما و ولنگار» در بحث حجاب و عفاف آغاز شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/152095" target="_blank">📅 13:20 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152094">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
خبرگزاری رویترز گزارش داد که پلیس لهستان اطلاعاتی درباره حمله احتمالی به نخست وزیر و وزیر دفاع دریافت کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/152094" target="_blank">📅 13:10 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152093">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d64a23e4e.mp4?token=QogJURzoTNmg2bv7pKssPemc6qoahtULW_i6ZV0ZAXN4MNvTHH_hbaRyfBg2qUyz64beMjUb5Ve4Jo4xXX-S8eLk_d84cfUgHsx4MwKHBv59zDnKaPqo-OAqvSa7MGLuzzwDIaaQ7q_0CXQWi4LdTwXAxurb35s6BzLC4bsYT38vhbLE4FsqEH03FvAzOBUwkI0p-lDPpz7INgCCDr0_NGLMnKvRBIh3mHNI8aonq1sfwI4VApK1WT81dQ_0DKWulPed0jENEvhgKRohQ-Eg44-z5jjN3KMAqNDg8znRcWNO6FMQWMe5VY2Bkva-Ta7OFxWkX1dcSMk7NbhttUc43A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d64a23e4e.mp4?token=QogJURzoTNmg2bv7pKssPemc6qoahtULW_i6ZV0ZAXN4MNvTHH_hbaRyfBg2qUyz64beMjUb5Ve4Jo4xXX-S8eLk_d84cfUgHsx4MwKHBv59zDnKaPqo-OAqvSa7MGLuzzwDIaaQ7q_0CXQWi4LdTwXAxurb35s6BzLC4bsYT38vhbLE4FsqEH03FvAzOBUwkI0p-lDPpz7INgCCDr0_NGLMnKvRBIh3mHNI8aonq1sfwI4VApK1WT81dQ_0DKWulPed0jENEvhgKRohQ-Eg44-z5jjN3KMAqNDg8znRcWNO6FMQWMe5VY2Bkva-Ta7OFxWkX1dcSMk7NbhttUc43A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیش‌بینی جدید قاسمیان:ورود عربستان به جنگ بوی آخرالزمان می‌دهد
🔴
قاسمیان سال ۱۴۰۲ گفته بود ‌اسرائیل ۳ سال دیگر نابود خواهد شد؛ بعد هم مکه را فتح می‌کنیم؛ حضرت در آنجا ظهور می کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/152093" target="_blank">📅 12:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152092">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af1c43edbe.mp4?token=j_QfmZVtLungIMDhyFv6a-ohedkFqUhW4uLfALkayvcWxWhV1R0SQZzJmCI2SjjKViSzUm-wY5pDhtzvWSWte_0asvTi-UZjrxCO4Hfk8oLV57EkOAPP3ZGFQquKXWwyCJBsH2gs0A2wyvdCWS4vS5a_UrRJplJaag2Rd0sVHkZ1bdqEmRw2OYkOU2IQVCrQEW915dAIPLAl0rkdcWE7Ysev0G05NAXZEGLBeJ0R-cH7Yyporl3ShBr2J_R7UwONcSemg3ok0kZO84IoBoIwmaDfnFsX2CaKOSEaujxL42McT-YfRNaL-o91enFqA6QfxM-QYtCJXpG1IiqAvrbhRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af1c43edbe.mp4?token=j_QfmZVtLungIMDhyFv6a-ohedkFqUhW4uLfALkayvcWxWhV1R0SQZzJmCI2SjjKViSzUm-wY5pDhtzvWSWte_0asvTi-UZjrxCO4Hfk8oLV57EkOAPP3ZGFQquKXWwyCJBsH2gs0A2wyvdCWS4vS5a_UrRJplJaag2Rd0sVHkZ1bdqEmRw2OYkOU2IQVCrQEW915dAIPLAl0rkdcWE7Ysev0G05NAXZEGLBeJ0R-cH7Yyporl3ShBr2J_R7UwONcSemg3ok0kZO84IoBoIwmaDfnFsX2CaKOSEaujxL42McT-YfRNaL-o91enFqA6QfxM-QYtCJXpG1IiqAvrbhRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه آخوند: بعضی از پایگاه های آمریکا تا ۵۰ سال آینده قابل بازسازی نیستند؛به نقطه رهایی رسیدیم/سپر دفاعی اسرائیل از بین رفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/152092" target="_blank">📅 12:49 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152091">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
وزیر دفاع بریتانیا: حمله به فرودگاه ریاض، تشدید تنش خطرناک و اقدامی بزدلانه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/152091" target="_blank">📅 12:42 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152090">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5u9-2jW4DedwbuDQPbIW-ES1wIGXgfAEiutbY5vj7_tjcVpk4CG9hBINWDp1gbxj7NK6a1yZKa0VbCo5_KSsf1-Ae6Q5_rnFwSc_QT1o2sBVETzzTUdOCW0YoizCxW0WyrbgkaTq-fWtp_O2owdfN6-_rK9sFNEGaYXKG4HCGoE0khEHb3ampHxj0iBQFC057a3b_lJ4OrY91rkJ4gBhLWreDAbNj8KZihJ1c63CmVFNo7L4sXpSie0xJTSpVXiAQQvN9Ueo3NgmTy0ybm_TVwcWZKiu-bC4u2UmNjwEPfxHlX_V9cP3df0D3qWoCZoW6vF7ZPqtoge-y2v4w12QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گزارش شلیک موشک از بیدگنه تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/152090" target="_blank">📅 12:36 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152089">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
گزارش شلیک موشک از بیدگنه تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/152089" target="_blank">📅 12:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152088">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bc3bacae2.mp4?token=lsCnf-bEId1rMoukVg7oaf7CtYtRFT-NYOY0IiJnUeZbTMvMW4MRPpa74w5YpthMS6-6ZtY5I1ZyxR7tinpEouzKqQteJFUQgvO6eMUrzsn4tN65msFP80k1vdMfsNOOqTESCgInW48e9y8S-gNvTcUP6sx13tvF-toC5526eZ4DIWKBs5QmXi9mzRCURwTOVRplVf1-SI_puWCHAF4P9JlHTYTo1tcGfMXRcrRJUk52zpJZBelsKcaL47cmKfV23yZPnhSTB7j5ARjOXDY19OiLwS7VD8Kbhymd3oMtlCCqRB9TTScXlM7mx6mTo1Vz4Wy9s4aGTC6x7z6DYQvCAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bc3bacae2.mp4?token=lsCnf-bEId1rMoukVg7oaf7CtYtRFT-NYOY0IiJnUeZbTMvMW4MRPpa74w5YpthMS6-6ZtY5I1ZyxR7tinpEouzKqQteJFUQgvO6eMUrzsn4tN65msFP80k1vdMfsNOOqTESCgInW48e9y8S-gNvTcUP6sx13tvF-toC5526eZ4DIWKBs5QmXi9mzRCURwTOVRplVf1-SI_puWCHAF4P9JlHTYTo1tcGfMXRcrRJUk52zpJZBelsKcaL47cmKfV23yZPnhSTB7j5ARjOXDY19OiLwS7VD8Kbhymd3oMtlCCqRB9TTScXlM7mx6mTo1Vz4Wy9s4aGTC6x7z6DYQvCAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصویر هوایی برخورد یک ابرنفتکش عربستانی حامل ۲ میلیون بشکه نفت خام با دو مین دریایی ایران در تنگهٔ هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/152088" target="_blank">📅 12:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152087">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
رسانه های وابسته به انصارالله حوثی ها از دو حمله هوایی عربستان به منطقه نهم در استان صنعا خبر دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/152087" target="_blank">📅 12:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152086">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFHoQwAP179kvW79-iKGtLKALY3S1vrVxFX-Gwyq4JHz-t6SOtkxRgoD4k81mMd5tvK8IzqakhwC4l5U_VrCgRXtU7Ovl_Av339H3qpfJoMb_XmYwP8zjTBCLcQ7K1p4Wq6tP1dQF0UYdOLIIgM9rhxwQekT0wbV1ihqccBf7HNUjFpWqph1mc0NZXDDgmeI9uFud6iK4UdZYxviIP7yHFYCgXu_aKku84mi6DihK9Ni7z-d3xausy9_k8wXUIs-ps72dAgnia6ZVTu-ZS9ldf_XOowooRVyzU1gGwOCTbRKqCZJYDxhdhfDmU1NZMfNSaDtx3FllU5Ad9nrfqy6Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ظریف: باید با آمریکا توافق کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/152086" target="_blank">📅 12:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152085">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
عراقچی: حملات اخیر به تأسیسات نفتی، پالایشگاهی، انرژی و هسته‌ای ایران، خطرات جدی زیست‌محیطی ایجاد کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/152085" target="_blank">📅 12:22 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152084">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
روزنامه خراسان نزدیک به قالیباف: واشنگتن و تل آویو تصمیم برای شروع جنگ بعدی را گرفته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/152084" target="_blank">📅 12:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152083">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
مسئول سیاست خارجی اتحادیه اروپا: وزرای امور خارجه اتحادیه فردا، دوشنبه، درباره افزایش تنش‌ها در خاورمیانه بحث و گفتگو خواهند کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/152083" target="_blank">📅 11:56 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152082">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
معاریو به نقل از منبع نظامی اسرائیلی:
نتانیاهو احتمال حمله به ایران را رد نمی‌کند
🔴
آمریکایی‌ها سردرگم هستند؛ یک روز چنان به نظر می‌رسند که گویی در آستانه حمله هستند، اما روز بعد ترامپ اعلام می‌کند پیش از انتخابات میان دوره‌ای حمله نخواهد کرد
🔴
تل‌آویو آمادگی گسترده‌ای برای احتمال تشدید تنش‌ها پیدا کرده
🔴
ارتش اسرائیل برای حمله پیش‌دستانه علیه ایران، آماده نمی‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/152082" target="_blank">📅 11:47 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152081">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3XPzKYxD5kxTca9pJd5sMqvN2C0BMUm0pNI8WjSS2THoqDWveas6B1x6Riyb43ExPZ26IyJ0JGciczZHDZi1JL2sxDvkC8jV3r6_FQCIve0sK-4kppSLKAbR-nydB_A-KZT0GRO7r2uIzLb4eVYa06Q7iY_yM2KWlPkM8-_RXIMkDh0whm3XeGlYfdpuUlikcDQjVqfdbCk5k3Xh1SV4xNTkYJd5VgMpKMkygT4y7zLg_ITaLop6JvQ8-kB9GbGXVKF0QUHO6Li40aqmITWE-KiANQqDY9NmolkEi3XIpwLW42tjm3_LBxqmGpHafdF5OsCxvmeRVsq_BWwfAx5UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک فروند هواپیمای ترابری نظامی C-17 نیروی هوایی آمریکا، دقایقی پیش پایگاه هوایی الخرج در جنوب ریاض، پایتخت عربستان سعودی، را ترک کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/152081" target="_blank">📅 11:42 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152080">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b97936751.mp4?token=gCcJoAuwW3tPYCzj9DLws75MvsSM5WZiwJmdmivNNPM0pKWh9xMm5cx038d9ElTLu7XyFDzxv5DWdswFdgnilY7uigsPyl6-b_DPFl5YXI-mMswt7V2ZkusupkErfNLTg0SME8tB4B2wPiIHbQ-0lgJorCD75oCFm2bpigty09OT-VHnwazhOtdytFc7YlzfNLUOqg0DG8IxcbzDi7KrDCHBKVf2xhJaLiOmCumTP9V-i0S-c8esBFuXLVYv4CGTjvCirAP7D-6im0ve2eVlWyfOkYmAcU8gVeNiJ7cnApvaLCY8Ja9nD_pXKyTT-espetpLvow2-th1xcra18MYYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b97936751.mp4?token=gCcJoAuwW3tPYCzj9DLws75MvsSM5WZiwJmdmivNNPM0pKWh9xMm5cx038d9ElTLu7XyFDzxv5DWdswFdgnilY7uigsPyl6-b_DPFl5YXI-mMswt7V2ZkusupkErfNLTg0SME8tB4B2wPiIHbQ-0lgJorCD75oCFm2bpigty09OT-VHnwazhOtdytFc7YlzfNLUOqg0DG8IxcbzDi7KrDCHBKVf2xhJaLiOmCumTP9V-i0S-c8esBFuXLVYv4CGTjvCirAP7D-6im0ve2eVlWyfOkYmAcU8gVeNiJ7cnApvaLCY8Ja9nD_pXKyTT-espetpLvow2-th1xcra18MYYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
طغیان رودخانه و سیل ناگهانی در شمال نپال
‏
🔴
ساکنان حاشیه رودخانه «بودی گانداکی» در شمال مرکزی نپال امروز (یکشنبه) به دلیل تخریب خانه‌ها و سایر سازه‌های منطقه بر اثر سیل ناگهانی، تخلیه شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/152080" target="_blank">📅 11:36 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152079">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFoDaLzhDPWvfvTVb70ajAXjlNWLYdPYnX7kaUUGPwr_ioXa8Mm4L8F80RkwBnjjS7BgFcrEfBFMOuyN2psg0C67FyadtH5WhRloGs2ZKiziymXdYLhuzQ3gwFpt37tMfV6YZr4M7z5R95dJBp5S_Dhs4NP28An9_5lrRFCLCqGW1PyUd4cm9_kvB3Ogxx5PAnwkByClaEAtUmUlAzbn5NM4PWubAe_6Bj9SzdZYCuKb0N9JtFgVN493VS5ZRHW3o64faj7cu9mXz4mbgbZSsQ-Gr4t3naN5ouyme85yHGHXh2xS2mq3u_idPHe1Fy9ASeapiGiqYmVIICQr7-q5vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هفته ملی کودک مبارک
❤️
[تصویر تزئینی]
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/152079" target="_blank">📅 11:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152078">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
یک هواپیمای سوخت‌گیری هوایی KC-46 پگاسوس آمریکایی وارد العدید قطر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/152078" target="_blank">📅 11:23 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152077">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/001aba2a7b.mp4?token=Tuno61f_XQD2W9dREqbKXa9uWdUBulPflmdOs3YPNHUat7badwiL8oXs-5kdHuO0Y2Xj5GXsJq8vFgRXSqAdsZCRleJFNWwxiYcotdrDonkpZ7oNkxSmN1xRCtAV2VoXf0daq60HhogRw9pT8x9eAKS1gvmj-OMJWVS0vYaz0ZOh9BExG2ZuKMOZgMjwLoQ9AvG21K2dpr23hfvE1RHpb22hRxKoiwFhCWTqgRogHtbFw7X2Jnp6O0NBVrYOZ2TPPVl1Scr5xisRuHX1WrD8cbj-U3k__g6Xk71pDejDWtWYtcu_hC1wwM5LmCB_hEztzrv5jzSGtAI-4fIoSbavWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/001aba2a7b.mp4?token=Tuno61f_XQD2W9dREqbKXa9uWdUBulPflmdOs3YPNHUat7badwiL8oXs-5kdHuO0Y2Xj5GXsJq8vFgRXSqAdsZCRleJFNWwxiYcotdrDonkpZ7oNkxSmN1xRCtAV2VoXf0daq60HhogRw9pT8x9eAKS1gvmj-OMJWVS0vYaz0ZOh9BExG2ZuKMOZgMjwLoQ9AvG21K2dpr23hfvE1RHpb22hRxKoiwFhCWTqgRogHtbFw7X2Jnp6O0NBVrYOZ2TPPVl1Scr5xisRuHX1WrD8cbj-U3k__g6Xk71pDejDWtWYtcu_hC1wwM5LmCB_hEztzrv5jzSGtAI-4fIoSbavWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ذوق‌زدگی و اشک یک دانش‌آموز از دیدن پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/152077" target="_blank">📅 11:19 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152076">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee1585d3f8.mp4?token=eHFsFMqns-MEbO_50ag_vMKhpTp57amSaitUtuC3v7maGJHACsg2pV5ZPUD92XHZxXACqv2gStwguuNSIgjovenr9_3B8vJ0yKq16EyL43MirVjC7aAgr7UO1WmK3SziUYxyKSBoQC-LqxdFj2ppMFZ-VJTEzeGzC_Bpm4o2fhbe8l8Fj5_9NeT5QyihecZJJgno1Iz8_Wf3sYjpNBAZbTB2yHtGSNvfBHkdj8PhCd58kZnkT5NXu1iqkKUxVyqhtzFmfcN5WwC0Hn7FQnIZwkKR41g5EW8CCbCbZtgVsF2jZEBrMlwiq2zpef8laIODVjbEr3ZJcC_GsxuwIT2B4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee1585d3f8.mp4?token=eHFsFMqns-MEbO_50ag_vMKhpTp57amSaitUtuC3v7maGJHACsg2pV5ZPUD92XHZxXACqv2gStwguuNSIgjovenr9_3B8vJ0yKq16EyL43MirVjC7aAgr7UO1WmK3SziUYxyKSBoQC-LqxdFj2ppMFZ-VJTEzeGzC_Bpm4o2fhbe8l8Fj5_9NeT5QyihecZJJgno1Iz8_Wf3sYjpNBAZbTB2yHtGSNvfBHkdj8PhCd58kZnkT5NXu1iqkKUxVyqhtzFmfcN5WwC0Hn7FQnIZwkKR41g5EW8CCbCbZtgVsF2jZEBrMlwiq2zpef8laIODVjbEr3ZJcC_GsxuwIT2B4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وقتی پوتین، عوستاد و تحلیل پا منقلیش رو ک... کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/152076" target="_blank">📅 11:16 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152075">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
بچه‌ها هر لحظه احتمال جنگ وجود داره و پشتش هم قطعی اینترنت
🔴
این ربات vpn داشته باشید و سرویساش قطعی نداره
💢
@VOXNET_BOT
💢
@VOXNET_BOT
✔️
میتونید با خیال راحت تهیه کنید و تو قطعی اینترنت هم متصل باشید</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/152075" target="_blank">📅 11:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152074">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
لحظه فرار سارقان موتورسوار که گوشی و طلای مردم رو میدزدیدن از دست ماموران پلیس که اخرشم با شلیک گلوله متوقف شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/152074" target="_blank">📅 11:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152072">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24c374bd2b.mp4?token=nH1qLkNZuQGXYUGSvArrbHfKbQHmGXghYREasJWFhz71vQ6ztKye5SNUFaNHuv9PBBLJfinaK-qMnmarBnVKVNha6j4jYN3fm2vJ9sQtizlWVelZVQ75pyQafLsrdY6ko05ryq0RyDlf8xDnveQSfcQPFq1VzSqkDyC7iv6Jzny69O7ckFr13e059Wgchm0YkcFNMFVLwVrhQlTo834KWxtH47WKXy4W_5yrWku_dJmaK0uKp6qgruERq2_dgbRDph_fHNPfEWGbGQOQ1wcCri7e0y-O4wZLuBKtunte000bu2a3kTLsDuVtGRRE1DQV4NciRTVDZ9BlgX8JanNkLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24c374bd2b.mp4?token=nH1qLkNZuQGXYUGSvArrbHfKbQHmGXghYREasJWFhz71vQ6ztKye5SNUFaNHuv9PBBLJfinaK-qMnmarBnVKVNha6j4jYN3fm2vJ9sQtizlWVelZVQ75pyQafLsrdY6ko05ryq0RyDlf8xDnveQSfcQPFq1VzSqkDyC7iv6Jzny69O7ckFr13e059Wgchm0YkcFNMFVLwVrhQlTo834KWxtH47WKXy4W_5yrWku_dJmaK0uKp6qgruERq2_dgbRDph_fHNPfEWGbGQOQ1wcCri7e0y-O4wZLuBKtunte000bu2a3kTLsDuVtGRRE1DQV4NciRTVDZ9BlgX8JanNkLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اوکراین لحظاتی پیش در واکنش به پیشنهاد ترامپ مبنی بر مذاکره، مرکز داده یاندکس در منطقه ولادیمیر روسیه را هدف قرار داد و باعث از دسترس خارج شدن و اختلال در خدمات سراسری روسیه شد، خدماتی که شرکت‌هایی در سراسر روسیه به آن وابسته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/152072" target="_blank">📅 11:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152071">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
تسنیم: طبق گفته بسنت اقتصاد ایران باید امروز فرو می پاشید اما باز هم این آمریکا بود که شکست خورد و اقتصاد ما کاملا سر حال ایستاده
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/152071" target="_blank">📅 10:55 · 19 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
