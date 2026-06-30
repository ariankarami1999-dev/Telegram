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
<img src="https://cdn4.telesco.pe/file/YfYmMYGlAljqFMpz_7R2JV81bwOUIDkDdeyey4huGmcQ0afAsCg8QLoi3VayvyQo69aulDPI_lzzPp5dt8uwk0_JBK4TAueq2iadNzoqLCJAA3-rUXCJiZ11HUQjQCt4eK__zrOSazy3-e47cfCfhyuVCDHB11p9DRRfsvoC391PDpAwiUyHqx5Y-xZYO1xatqjcnKyNme8AJUbKWdVT-VLuQUSpfpLrrYD3cwk7zi9-DRDoXelNnvkUwyhA6K_ECiN2UH19lKvt6yNxg52bQJE62M2TeA9p-ZLELDPDJsFIb06Bkov47iybr45KfWBa_xG6X31rhznsnt-RZD-kHQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 20:51:17</div>
<hr>

<div class="tg-post" id="msg-445694">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9407c8629.mp4?token=Yd-8H0zkvmYuZYf5wJhZhuRh7D28uyPH_YQJbSc8uVHuL2I3fveqPN_7XDuc42iM3LgyvdJT0ff6ICo1z_FRulwM4CS8e9Zh9tugKkX2JE9uKgU3MSkr-fYBjaPiRvYlStZGmCsMZYgwCCbuTwNpsRE4x3xoSWuo6ss0ObE3hJjG_BKkj9yrbr3w4v49Y3bwb_-Y9_9pc6MPp_SFLPjB3sBy2jyZiGrK1uBJKYH5FAM_-1z-GQZdkasZ2T5RiupxKld5wYaKrcXAJrwgPug8Vbxvm2Y8mADrVRkcMDlf-SR2NrPrwvEhqjqgHeEcsArp9kldLr5zFxsk4Sb84npWNoS4QbvO2xBrHHmfuhyBVxMfY0WXfvFm2ChlWk1X_rQWO4enbn1g_jQdZ7O2Ef9frQ6yFry8wuksBkQbOX2kAeOWHaXBW_KhtooPRax0Hj1e9zrffYyujNJg_bKRFn8rlEMSa8G4PgqUuxG9aFXjRtNdQqW2q7UbCAo4LT0pJNLb8Xn3zio8h6w-dRWSD0ARxXB4su5dHRh3eFcBNoQa0KVFaSDAdHbZGfqrGotqn0cUj4o3-lvJtRzpJeRLueKPKks6hfNnP9Rs9TNl-MgSZ-DJG2ZVBtgRubO_cwRu07VNPJ9o4JZbNVBQ3zyZh_QqfB-v9wNvjtZLf3CldoPSn_s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9407c8629.mp4?token=Yd-8H0zkvmYuZYf5wJhZhuRh7D28uyPH_YQJbSc8uVHuL2I3fveqPN_7XDuc42iM3LgyvdJT0ff6ICo1z_FRulwM4CS8e9Zh9tugKkX2JE9uKgU3MSkr-fYBjaPiRvYlStZGmCsMZYgwCCbuTwNpsRE4x3xoSWuo6ss0ObE3hJjG_BKkj9yrbr3w4v49Y3bwb_-Y9_9pc6MPp_SFLPjB3sBy2jyZiGrK1uBJKYH5FAM_-1z-GQZdkasZ2T5RiupxKld5wYaKrcXAJrwgPug8Vbxvm2Y8mADrVRkcMDlf-SR2NrPrwvEhqjqgHeEcsArp9kldLr5zFxsk4Sb84npWNoS4QbvO2xBrHHmfuhyBVxMfY0WXfvFm2ChlWk1X_rQWO4enbn1g_jQdZ7O2Ef9frQ6yFry8wuksBkQbOX2kAeOWHaXBW_KhtooPRax0Hj1e9zrffYyujNJg_bKRFn8rlEMSa8G4PgqUuxG9aFXjRtNdQqW2q7UbCAo4LT0pJNLb8Xn3zio8h6w-dRWSD0ARxXB4su5dHRh3eFcBNoQa0KVFaSDAdHbZGfqrGotqn0cUj4o3-lvJtRzpJeRLueKPKks6hfNnP9Rs9TNl-MgSZ-DJG2ZVBtgRubO_cwRu07VNPJ9o4JZbNVBQ3zyZh_QqfB-v9wNvjtZLf3CldoPSn_s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دَرِ خانهٔ تهرانی‌ها به روی زائران تشییع رهبر شهید باز است
@Farsna</div>
<div class="tg-footer">👁️ 434 · <a href="https://t.me/farsna/445694" target="_blank">📅 20:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445693">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCLs-2lONAUWnsGoxAVugssuc88DIb5yDOdT4tu3TNrDZ1Zjll_k3ap6L_m2oLz2sOioMlfsK1LMnPxljJ4b6nKtbNmKm8NB7HU83F2pSSbniHNJOX41bbeATxvr32lOuk9aixWQkd3FcEzfxJQgGc-AmVfTyAnUOKQt9gXuHNmZL1961lnAQQgTkyp9-4L9izwxxzjWAqADbHZ2lUHySvlGY7-IKpyarP1KaMGlO95nvCj1DxUK3GY1Z_9r7x-EQLUgbjG2S_tMEbRIb9LElVqcf3vvVh_Wnwl3cmWtTql52heQYt2gRrU1UiinS7tHjh98EjcvS05bXxKDEkegIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
حجت‌الاسلام مروی، تولیت آستان قدس به نیابت از رهبر انقلاب از حجت‌الاسلام راشد یزدی، استاد اخلاق و خطیب برجسته که در بستر بیماری به‌سر می‌برد عیادت کرد.
@Farsna</div>
<div class="tg-footer">👁️ 998 · <a href="https://t.me/farsna/445693" target="_blank">📅 20:49 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445692">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgTbZzKCJR1p81FAvHnW2aLwgLT6BTa9qTRttgjHMNKpdnPes4MfV2F1ep0DtRIfcXyphpeqJhZaraWlz0xlxGtB0g5oYfWGXV67WSYMVKXIzTLPQLrf7iGVRbU8Syh5kad5qA8L5IikLIl-UsR0Ey_EPLddx8S6W-q6gD8jj_UwOPWTKvxmkI9oaoGVqt0PUm2Dem4HMw8kdc6VQjK1qAJZfc4OU8nsAOHzMn8JuB8HwzJW_-HF9ahBmaqJ6ygwqPYi-0XzakDe6MA8yjPTXUr61Dw4lN5nkjGky8cOA0ev8pkopuvySS0IqGDYuCIbmpnbSsHCjDEoJaLQ_6KJRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توصیه‌های مهم برای مراقبت از پا در پیاده‌روی تشییع رهبر شهید
🔹
کارشناسان توصیه می‌کنند که زائران در انتخاب کفش مناسب، تعویض روزانه جوراب، استفاده از پودر تالک برای جذب رطوبت دقت بیشتری داشته باشند.
🔹
همچنین چسباندن نوار یا چسب در محل تماس کفش و پوست می‌تواند تا بخش زیادی از بروز تاول یا زخم شدن پاها جلوگیری کند.
🔹
محل تاول‌ها تمیز و خشک نگه داشته شود و از ترکاندن آن‌ها خودداری شود.
🔹
برای درمان تاول بسته می‌توان از ضدعفونی‌کننده بتادین استفاده کرد، اما برای پوشاندن تاول‌ها نباید از چسب استفاده شود.
🔹
استفاده از کمپرس سرد برای کاهش درد، پوشاندن تاول ترکیده با باند غیرچسبنده و چرب، تعویض منظم بانداژ و پرهیز از چیدن یا کشیدن پوست روی تاول از دیگر توصیه‌های مطرح‌شده توسط کارشناسان است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/farsna/445692" target="_blank">📅 20:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445691">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bb250fe5b.mp4?token=qPksAViGkw9_v-_q6-9ywpLrpV_PS6gURkND2kJfMCXMlm5riHHDwx9QlfbGBGr3ABG0h8kp8oFsc6iQ-Vse8eHP9Yvl2p-RKPmqShn4o_ngQRN61NcpYStbeWw2ZSie2kYiHowYMHOQ7wJ_kaBDdBoZ0n4gEqc3L55E98fqUVWac0o8Tfe3UyFHY3IYgWh1hSQzdrv9XwunKXZjDxx_74AiWtOPnysX1x5E9O1nBq_nUhKUTPo4Ku4WVwTs3WuWkAGeFOTIRvMxbbjCeHvNhdRHcEqx5N4fWHWSx8sVjUIZDgwcO2pSR92GpAJveXP3apQQ_LPQBqER8XyZF49MEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bb250fe5b.mp4?token=qPksAViGkw9_v-_q6-9ywpLrpV_PS6gURkND2kJfMCXMlm5riHHDwx9QlfbGBGr3ABG0h8kp8oFsc6iQ-Vse8eHP9Yvl2p-RKPmqShn4o_ngQRN61NcpYStbeWw2ZSie2kYiHowYMHOQ7wJ_kaBDdBoZ0n4gEqc3L55E98fqUVWac0o8Tfe3UyFHY3IYgWh1hSQzdrv9XwunKXZjDxx_74AiWtOPnysX1x5E9O1nBq_nUhKUTPo4Ku4WVwTs3WuWkAGeFOTIRvMxbbjCeHvNhdRHcEqx5N4fWHWSx8sVjUIZDgwcO2pSR92GpAJveXP3apQQ_LPQBqER8XyZF49MEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جمکران در تدارک بدرقۀ رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/farsna/445691" target="_blank">📅 20:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445690">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57c3f5ced9.mp4?token=WSsilOuo3x1gKt6zU_lNNopkLAmqlN4AowbAIqMYaI1s2QKB7Gwn8AlKIqcKoQnHYxgmvGIZzQtR393LJaCcLHcFJsb7Hb9vkWN2YYvslMcv3E-0yk6ty6jyjgx98IrDY-l1OdRPDk4XywSfwlivwdAJ_8Gtauvs6eYa6378h4E_omb-YnP8YKzSyZsqnOJMwJic2BLcza7IvG07pO7ZAHPEUm3QdZQsFNvAGAMccwRmW38fHBlnXQs7lGg4onuapwAWA4gySmdImBnHZ2zgq9LWtnp_PDY-uU4tHhrBqKZurYkMvH19MbUSscW3UDAnJNR1XSJDp3XUZpkBUnLtbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57c3f5ced9.mp4?token=WSsilOuo3x1gKt6zU_lNNopkLAmqlN4AowbAIqMYaI1s2QKB7Gwn8AlKIqcKoQnHYxgmvGIZzQtR393LJaCcLHcFJsb7Hb9vkWN2YYvslMcv3E-0yk6ty6jyjgx98IrDY-l1OdRPDk4XywSfwlivwdAJ_8Gtauvs6eYa6378h4E_omb-YnP8YKzSyZsqnOJMwJic2BLcza7IvG07pO7ZAHPEUm3QdZQsFNvAGAMccwRmW38fHBlnXQs7lGg4onuapwAWA4gySmdImBnHZ2zgq9LWtnp_PDY-uU4tHhrBqKZurYkMvH19MbUSscW3UDAnJNR1XSJDp3XUZpkBUnLtbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میثاقی: ما همیشه با برد تیم ملی خوشحال می‌شویم و با باخت آن ناراحت
🔹
البته باید عملکردها را تحلیل و نقد کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/farsna/445690" target="_blank">📅 20:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445689">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: در نشست فردا عمدتاً در مورد دریافت پول‌های بلوکه‌شده و آتش‌بس در لبنان بحث خواهیم کرد. @Farsna</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/farsna/445689" target="_blank">📅 20:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445688">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: تاکید داریم که هم باید توقف جنگ باید محقق شود هم خاتمۀ اشغال‌گری [صهیونیست‌ها در لبنان]. @Farsna</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/farsna/445688" target="_blank">📅 20:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445687">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtV1IIL9ojQ-eh9znO-K0KgUT_BsV_anukwO9k5LD-EuZR65l6fU-mRVDKj625GwdBnP7sc8PLuDvMDIf4iEbY7WyKHIzOl1S_5XJA6rYGtBqEmSSjjuFvwu2ukQcMh4Aclpgzu75nBOdBsmaJUZnKhoqP9vOFK16Y7PkDvjEZ9QX1SsyG7PtYEiWcPyZAHd0XQ-UaN3e29ojRyAtL4ChwRN6ONVHtGP-3HyYnb2k1_OZzIzATlMTdFpJIwPeJh3A_27shXXolql44Bw3vf0b5u87aIncGMon_Y54iz3_sQv28L1EZ9l-DqKICMurxbzvLyI_TdUXN6udScAeE_bhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دروغ مذاکراتی ترامپ برای کاهش قیمت نفت
🔹
ترامپ دیشب گفت، امروز با ایران مذاکره می‌کنیم و قیمت نفت وارد کانال ۶۰ دلاری شد؛ اما امروز سخنگوی وزارت امور خارجه، اسماعیل بقایی، این سخنان را تکذیب کرد و گفت: «هیچ برنامه‌ای برای دیدار با آمریکایی‌ها نداریم.»
🔹
با تکذیب ایران، روند افزایشی قیمت نفت شروع و امروز هم این روند ادامه یافت و قیمت نفت برنت به ۷۴.۶۷ دلار رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/farsna/445687" target="_blank">📅 20:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445686">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: با طرف آمریکایی در قطر مذاکره‌ای نداریم
🔹
اعزام هیئت کارشناسی ایران به دوحه در راستای پیگیری اجرای تفاهم‌نامه است و طرف بحث قطر خواهد بود.
🔹
هیئت کارشناسی ایران به ریاست غریب‌آبادی، معاون حقوقی وزارت خارجه اعزام شده است. @Farsna</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/farsna/445686" target="_blank">📅 20:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445685">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: با طرف آمریکایی در قطر مذاکره‌ای نداریم
🔹
اعزام هیئت کارشناسی ایران به دوحه در راستای پیگیری اجرای تفاهم‌نامه است و طرف بحث قطر خواهد بود.
🔹
هیئت کارشناسی ایران به ریاست غریب‌آبادی، معاون حقوقی وزارت خارجه اعزام شده است.
@Farsna</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/farsna/445685" target="_blank">📅 20:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445684">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">نتانیاهو: آمریکا و دولت لبنان با ماندن ما در منطقهٔ امنیتی جنوب لبنان موافقت کرده‌اند
🔹
اسرائیل و لبنان بر سر دو منطقه امنیتی برای راستی‌آزمایی و خلع سلاح حزب الله توافق کردند.
🔹
توافق با لبنان را به لطف ضربات مهلکی که به حزب‌الله وارد کردیم، به سرانجام رساندیم.…</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/farsna/445684" target="_blank">📅 19:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445683">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zp0V7EesIbQAtMAX1xsdb5n-upSlsu6-yeahSH2Nar5IBUw_Q8UN5rAcE2ClnBAZX-2CqsaPvyQGMHhFPfNBsEBflLVuJY5CyDZk-Pb-VjCUervLoHh5U3JyA7vJ2a6VhqzOUKkWssskYe4nQZzLa5tWN7E15Gk_1SbymVL35OR01DIhjWKFZJTcX6SFjpJvt_z2v75g7pIrY8D7y9iskTj-zh1regbwazbidOKuAqltwaftPyWacPzUHyThIx1rbQdLT-r9j-G3RNFd3V2xsmRqPwp9OACBYU1YXtnpCzCl2FB3817oFBFMDqB3v6GqTaj7f-jag3Huu1zf6oDTOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور گرجستان به مراسم تشییع رهبر شهید انقلاب می‌آید
🔹
دفتر ریاست‌جمهوری گرجستان اعلام کرد که میخائیل کاولاشویلی، رئیس‌جمهور این کشور، در مراسم تشییع پیکر رهبر شهید ایران، شرکت خواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/farsna/445683" target="_blank">📅 19:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445682">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75485d6e4b.mp4?token=iYw56p5p530TRHbspo-HTFn2a-D9b1UxY_Ejlg3FIZ2KtID8wXjvOHCvQRScV2kiQo3Bh1ncifogD0WJKiANver-VV6P0DsU38Y9RvID8thsgf1gLZL5Voi8B8JK2ekYXKODa6pyz1xRrarm3yGO58VQisPVi-JEzAyoLKEf42lr--SCAbZ8EKrjmXjVCoGcTPHg2iGDYmQE1KjOlu8FN7eWimAp0rWIavHTgrKitn4xh3xdOcCQTU0GFXaakmXmH1cWAr_KsqJsnXOsTp46bk1Vx0jBtGMQsV7fjhZh46DeFsCQ9RnKo3PpRcjyPSugiii8Bz_bg9ZN8KJK-2Ajbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75485d6e4b.mp4?token=iYw56p5p530TRHbspo-HTFn2a-D9b1UxY_Ejlg3FIZ2KtID8wXjvOHCvQRScV2kiQo3Bh1ncifogD0WJKiANver-VV6P0DsU38Y9RvID8thsgf1gLZL5Voi8B8JK2ekYXKODa6pyz1xRrarm3yGO58VQisPVi-JEzAyoLKEf42lr--SCAbZ8EKrjmXjVCoGcTPHg2iGDYmQE1KjOlu8FN7eWimAp0rWIavHTgrKitn4xh3xdOcCQTU0GFXaakmXmH1cWAr_KsqJsnXOsTp46bk1Vx0jBtGMQsV7fjhZh46DeFsCQ9RnKo3PpRcjyPSugiii8Bz_bg9ZN8KJK-2Ajbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور رهبر شهید انقلاب در حرم امام رضا(ع) در سال ۱۳۶۴
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/farsna/445682" target="_blank">📅 19:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445681">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">بورس ۳ روز نخست هفتهٔ آینده تعطیل شد
🔹
با تصویب شورای‌عالی بورس، روزهای شنبه، یکشنبه و دوشنبه ۱۳، ۱۴ و ۱۵ تیر، بازار سرمایه فعالیتی نخواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/farsna/445681" target="_blank">📅 19:33 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445680">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ACoGa3nUU-ZbKc5_Sn7YKrpmJCJhXbI1te9jIJuxaU5T0DOezCsq4F2AlVtHbgy8_FgDzQB1OUfRUUVaya8rBNUbFssXV9b9qMTglbMxJ0I64YiovKJwjLR6hnmzJhlhhdEdTqZHK8_4SqKRkB4ZZYfQFyHTSok_10enVYU29DU88XWRgE0hLl_156fI75D_SUPo_-P-5NR4hGDkNUyIpCAGNVqSAj9btLoiadYqRsGDziaiDWe2N4_Z3EgQNQksaU8vNpIU3mR02rS-urfZ4_cK0xh71wNd3oSMBvG-T1_EwuFmq5JaqUzaG6CDBlld818zZd0ugJdbU-kpVWRs2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عارف: ایران برای وداع با رهبر شهید تمام‌قد به میدان خواهد آمد
🔹
تاریخ شیعه پر از بغضِ تشییع‌های غریبانه و مظلومانه است؛ از مدینه تا طوس.
🔹
اما تقدیر ما و آزادگان جهان، رقم زدن تشییعی به وسعت یک جهان، شکوهمند و بی‌نظیر برای امامِ شهیدمان، خامنه‌ای عزیز است.
🔹
باور دارم ایران مقتدر و امت اسلام برای این وداع تاریخی تمام‌قد به میدان خواهند آمد.
@Farsna</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/farsna/445680" target="_blank">📅 19:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445679">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o1nk2j3LasWJQ6dLu13w3JaWXHXd3Zo-IMhThrtnvHdY41LQ1_1paqAFdAFd7-EWqPxmYNvqp0GB9oe2XZHocWXe-Rd41luOjd5Cne3sIiYgdlmsjTX0AD8HwyPY_ARMzGF1p7Ul0KwtCwcUMePMxhn5IlGuYuiCMRYAsXXQC8H0fHtapzEax5gaPbx6yb33-0P_uUiTwixXtaZMFNmsPG7QsLuTxMoosc9ldgI9W6crxpqS-rFbfqzyZJWIg03sL6L2udR42qJjVuDGjSIy1KMMVXvNoSZajErxvVjz44Ji_xX2K1hasT5yMjLcHWMZjDJm-bfPFBrEtlBt8QlNwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طیبی مرد سال فوتسال ایران شد
🔹
حسین طیبی فوق‌ستاره فوتسال ایران با رای کارشناسان به‌عنوان مرد سال فوتسال ایران انتخاب شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/farsna/445679" target="_blank">📅 19:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445678">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9risdhTR3isW7YO3evOf7SpgLC7N2M1R7RTrrnksC1W6NXMyScKswSIBvCuwjED4mCY_HBdbkUI-pg5aP-YN9fiofOrBj3r8NSZ2DTNG3cgFZcq7_CXcWQilvludTJPNp78bYLB5DYiH4M78JVyA6AX6Pq0du8udsFAcbHlS0_sjxdIsDZjlMqjuBr8Iz43_BdSSvuYYkUtnZIxfGFMoep29e3jhuBao6Xs3N4sxXN4tc1JQgPa6wjlA278G3zLRF0OiQU-PaMjWms210LAFuljbnaTFYV2nUFbHmY2LNiE2J5x8aUbxHTZ5hvCTwy3x0yzzMl17dBFg1JhR4aHYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایپا شرایط خرید ۵ میلیارد و ۶۰۰ میلیونی چانگان را اعلام کرد
🔹
متقاضیان خرید این خودرو می‌توانند از ساعت ۱۰ چهارشنبه ۱۰ تیر تا ساعت ۱۶ چهارشنبه ۱۷ تیر نسبت به وکالتی‌کردن حساب خود به مبلغ ۵۰۰ میلیون تومان اقدام کنند؛ زمان تحویل این خودرو ۱۲۰ روزه است.
🔹
قیمت فعلی چانگان CS55 پلاس ۵ میلیارد و ۶۲۰ میلیون تومان تعیین شده درحالی‌که قیمت قبلی  حدود ۲ میلیارد و ۶۹۰ میلیون تومان بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/farsna/445678" target="_blank">📅 19:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445677">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🎥
قلعه‌نویی پیش از ترک تیخوانا خطاب به مردم مکزیک: اینجا را ترک می‌کنیم اما قلب و وجودمان اینجاست.
@Farsna</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/farsna/445677" target="_blank">📅 19:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445676">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/farsna/445676" target="_blank">📅 19:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445675">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">بازداشت تبعۀ آمریکایی در اسرائیل به اتهام جاسوسی برای ایران
🔹
رسانه‌های رژیم صهیونیستی مدعی شدند یک تبعۀ ۲۰ سالۀ آمریکاییِ ساکن قدس اشغالی به اتهام همکاری اطلاعاتی با ایران بازداشت شده است.
🔹
به ادعای پلیس اسرائیل، این فرد از ۹ ژوئن بازداشت شده و مأموریت‌هایی مانند مستندسازی و عکس‌برداری از اماکن حساس را انجام می‌داده است.
🔹
پلیس مدعی است او برای هر مأموریت، مبالغی بین ده‌ها تا صدها دلار دریافت می‌کرده و قرار است طی روزهای آینده علیه او کیفرخواست صادر شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/farsna/445675" target="_blank">📅 19:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445673">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFyHV0G1OA0wNhhjZVozofgkb_KaI2KQUlkMLqRv16G6BJEUCpHhwkemUJuKB8-mVhirh72w9Eki8UDQQJ46wv1WpiwrQMAgU0dU8Osclxl93ecLk0DpKjfdH0J4B19zZ7syqIJZl8diEmbK1y81XAiBaxWZTuxSAWrYmbaEv69XHaahohy7DFgUcTgDgFAoMoBp7XAK1-uBbHPZeohRgfj1VHp4aHPA59_rP9m4K15zce3w4GJM7KSzzq4TVRuZhqErxF_QGaeXNmc1CN_gRtyhDkrRaxxGUxOG9SxvY5tJxPQ16OVIjNFLQLPYIcjOwSztb8ZW_RdDUAYAZAc7hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراسم استقبال از تیم ملی فوتبال ایران با حضور عموم مردم، فردا چهارشنبه ساعت ۱۳:۳۰ در ترمینال ۴ فرودگاه مهرآباد برگزار خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/farsna/445673" target="_blank">📅 19:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445671">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس پرس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p7_lTBBDFBLwu9d1psJ3cZAwc-ZxgDDV-E-MlxcxYG0bGUq6cQh7rOPIs8WxIiRCWBiG0oOPVu0lIekul9NzQOMo17UizJcKYJFnOM6-rFBa4Ps_84R14K7OPETq3mJ0jiEpygIj4B4olN0GNc218SKwa3KWKZYtfXZfzM_F0Eu-QpkBN5wyo8PJYZynkGWduDzlLSklhTlCDmCWVeaIh-t0w1GXBoePUggRB0lcBoVZqpOgY9RTZ6fC9CXot8eObYlYISZXmSnSZe1I6BoR1qBG2W-sBliTsB5SrK43CFF7N9tJ3cayol2DxFXrScpsDk5iGXR0O6njeAcLCA5kkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P7dSu0S_8klnIKfh6qe4wsrz02ZSK6cGhsh2gWouLL4O9T22hSxfHV6-TrVDKPEDsQERORaSkdBQoIK46YsBdVabYAT6rdB_OG7CNyPvxETZKBNs77UHc-6ox_skLz1-mmAW5hOq7BeOwad54Bqb5dfrFkxiiLY39rO2saG8Bvn7tUNppCdKGtJ3y26O1VpQn58aJYKGJhNqEZQfbe3BYhDHPAvaZqqd3g99sjCRcicSNh3IAFy1VVSo9DjaWaVf9Vi9PO_9cUUqrN118jW-XLdMsdMQgJiYj2slvQbw-rjEbMFmPE5hqKg1LEIjopeMOlxRjcx1ZiOosJ8SZRNXog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔸
مس ایران در مسیر ارتقای شاخص‌های تولید؛
🔰
ثبت سه رکورد تاریخی تولید مس در سرچشمه و سونگون
🔻
مجتمع‌های مس سرچشمه و سونگون در خردادماه ۱۴۰۵ با ثبت سه رکورد جدید در شاخص‌های کلیدی تولید، عملکردی بی‌سابقه را به ثبت رساندند. این رکوردها شامل بالاترین میزان تولید آند در تاریخ مجتمع مس سرچشمه و ثبت رکورد تولید کنسانتره مس و خوراک ورودی کارخانه‌های تغلیظ در مجتمع مس سونگون است.
🔹
در خردادماه ۱۴۰۵ میزان تولید آند در مجتمع مس سرچشمه برای نخستین‌بار در تاریخ بهره‌برداری این مجتمع به ۲۳هزار و ۳۲۳ تن رسید؛ رقمی که از رکورد پیشین ۲۳هزار و ۱۱۶ تن در خردادماه ۱۴۰۲ نیز فراتر رفت.
🔹
این در حالی است که برنامه تولید آند ماهانه کارخانه ذوب مجتمع در این ماه ۲۱هزار و ۲۲۵ تن تعیین شده بود و عملکرد ثبت‌شده، حدود ۱۰درصد بیش از برنامه و معادل ۲هزار و ۹۸ تن افزایش تولید را نشان می‌دهد.
ادامه خبر در پایگاه خبری مس‌پرس:
https://mespress.ir/x6Rm
@mespress_ir</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/farsna/445671" target="_blank">📅 19:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445670">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/farsna/445670" target="_blank">📅 19:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445665">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHT92n6TDndjn590jXApvmkuEL1zfLb4U3G1_U8QAe8D9nr3AugHPzRt6mRYm-9EXgyxkkNBAkBlQZ898kx1CaukNyGulGPDxcu2V8nOkrXGMa-2cSv9i3-PkcB15bQJmjYkgPtn8LeIod9Zr6v0bdBuaCXkkqoVQt0Vls7yneSxLEciBKHQoRYd0cDnyRZbG8RmrSBOSn1-1-VCE-DSW19V7XJnHlwT-KN0G870DReaLr74JRE_ASlAWTuqZh91aWcZNKVDlatpKsy6YaGvNPXKdStr5pqjDuEVGTdPBEd-BKp2aca6BIJt30IcPBTiPQvZh0HiYvcO_7htgEzj1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قانون حمل سلاح محیط‌بانان بالاخره اصلاح می‌شود؟
🔹
فرمانده یگان حفاظت محیط‌‌زیست می‌گوید که اصلاح قانون حمل و به‌کارگیری سلاح محیط‌بانان، مجوز ۳ کمیسیون کشاورزی، امنیت ملی و حقوقی مجلس را دریافت کرده اما به‌دلیل تعطیلی مجلس هنوز فرصت طرح در صحن علنی و تصویب نهایی را پیدا نکرده است.
🔹
قانون فعلی که سال‌ها پیش تصویب شده، به مأموران یگان حفاظت محیط‌زیست تنها زمانی اجازه استفاده از سلاح می‌دهد که ابتدا هدف گلوله قرار گرفته باشند؛ گلوله‌ای که ممکن است پیش از هر واکنشی، جانشان را بگیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/farsna/445665" target="_blank">📅 18:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445664">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3YOZgFOczY18Eo19JfWmgsq3Z7N5JOCQBP9k_COFEhZOPJ4T2FivNZiSlZfvgMgPXNRZBlL5BdCTsVylzHq1bsDnd9bMdv4AMqC-kn4X_etMRfCnriuTt6F_jBzZHUmuQxGmO21edIMNfX7PKjeBehFO2_Tj6KXsNkC37fTkh2y5VVtKKpuB7kC06iNRQ5Cb7Yc_x6uxRpqMr1k5yn0in6u0oTPt4ZM_WX1yO1Ad-gJ89ZJpmsN9mTrTK7OEEsIvpTjXirX8CX8HtMgxCKiwKHsiV-xY0-zNBk0Lizjp3XiQFomn2lJnf4RtN66s0Mb1aUR2x-wWurwdy26vWR4pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چین: گفت‌وگو بهتر از جنگیدن با ایران است
🔹
وزیر خارجهٔ چین: اولویت کنونی، حفظ و اجرای تفاهم‌نامه، تداوم شتاب مذاکرات و تلاش برای دستیابی زودهنگام به توافقی جامع است که مورد توافق هر ۲ کشور ایران و آمریکا، مورد قبول برای کشورهای منطقه و مورد استقبال جامعهٔ بین‌المللی باشد.
🔹
آتش‌بس کنونی همچنان شکننده است، اما گفت‌وگو بهتر از جنگیدن و دیالوگ بهتر از رویارویی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/farsna/445664" target="_blank">📅 18:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445663">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVfqcngRNVOgmqSUKlFLnvBj90szcqkQDbXVjG9GJtdhj6iJyUFOhWZU1UqSIcN4Dw1D52a9S41xS8iq2jwRg2aeT7evUVCID005QRWBSIFGPALsae3HzTIoSFgH4uM1uT4NNKPGbZx_Z0UpEKEEn0pj-l8V3Sna6HrDrx98NPWYaEj6cVKIZbUwZlccoL1vECGCo_VWntoWR7Wj0xeS3Dh_jkrTHMv8ShnLTnod5wFSWlbXUTLysAllwvL8EsZj5hC5N0LS1BNz0NOLVK41_MD7d1GuPzSkIJLGG-k43dWAB98DF3edKN9H8_iSps2if_VN9VvSG46uUHwo2tM4yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات صدور اعلان قرمز اینترپل برای سران گروه‌های تروریستی کردی
🔹
تنهایی، وکیل پرونده تعدادی از قربانیان اقدامات گروه‌های تروریستی کُردی در گفت‌وگو با فارس: صدور احکام قضایی، اعلان قرمز اینترپل و درخواست استرداد برای شماری از سران و اعضای گروه‌های پژاک، دمکرات،…</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/farsna/445663" target="_blank">📅 18:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445662">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/II7t0ad4gA813ik6bw5MSXR2zcrc3VSxDAU9DMOu3HIzYVj76bNGoKyoT3AZyFXTnWA19jFD4prdpB7owuhmVWvNUgHDzgICOXAXyDUp9R2l_wm-tb1F9YOCfAMuJtR5dIIH0uXlLb_MIBQNuGIFv_0kY3N4kNV0jkyng0xPs6zhfFKf9mytdzduYtB3wFPC1Y7meJStJ4OFBPD6smyXhw7gK1y7aUABqxwH54GfOyA7Px7AUQcMO7pcz5Lpk4SRmZ8I1SzFsjTxEvRxfZ3B5Rg0xZ21QhexgrBOLE8x7PDtXW6OUTrRX-jIY9VZiszBeBQHWk1UWkMGdaF7k7UR5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاچاقچی سابقه‌دار سلاح در لرستان دستگیر شد
🔹
فرماندهٔ انتظامی لرستان: مأموران مخفیگاه یک قاچاقچی سابقه‌دار را مورد بازرسی قرار دادند که در نتیجهٔ آن، تعداد ۱۶ قبضه کلت کمری به همراه ۳۲ تیغهٔ خشاب که به‌صورت ماهرانه‌ای جاسازی شده بود، کشف شد.
🔹
این قاچاقچی سابقه‌دار به همراه پروندهٔ تشکیل‌شده برای سیر مراحل قانونی به مراجع قضائی معرفی شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farsna/445662" target="_blank">📅 18:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445661">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0_3Odd0Lzys34Cd1PgfwOVPZls7E5RV-6hsk6A9enreVSs4jRKLkPlVzdk6_KRJ2abTTL9Vw2AA344hpMSETDPkvi5E0pozediUuyCRG-rI1KJeRWilv6CLJfvhme1kECdGdPhI68fmVCqGeSrUW11rOGsuODLYQCeGIaU2l_ULpT24UR3lgBJ02U89E1-Tf8qVMz5HYZUuQf58LIGtj2yuj01ijlGh1iLwoecwmIPLbd5336N2Gtof1vepQLESZig0gcARdJH6k4ziGkN3Zi1isdyv3YHP6PbNNU_RnMbI1ISWSW1gfHme2HNVI5Wl2JfAFivocSzThVRUbK4ung.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قربانی اپستین از ترس انتقام ترامپ مخفی شده است
🔹
یکی از بستگان زنی که در پروندهٔ جفری اپستین، ترامپ را به تعرض جنسی متهم کرده، می‌گوید او از ترس انتقام ترامپ خود را پنهان کرده است.
🔹
این زن در سال ۲۰۱۹، ۴ بار با مأموران اف‌بی‌آی مصاحبه کرد. او گفت که در دههٔ ۱۹۸۰ ابتدا از سوی اپستین مورد آزار قرار گرفته و سپس، در حالی که بین ۱۳ تا ۱۵ سال سن داشته، از سوی ترامپ به او تعرض شده است.
🔹
این اتهامات هرگز در دادگاه اثبات نشد، اما او یکی از معدود قربانیان پروندٔه اپستین است که مستقیماً ترامپ را متهم کرده است. کاخ سفید اتهامات او را «کاملاً بی‌اساس» خوانده است.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/445661" target="_blank">📅 17:46 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445660">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
خبرنگار شبکهٔ المنار گزارش داد که توپخانهٔ ارتش رژیم صهیونیستی شهرک بیت یاحون را در جنوب لبنان هدف گرفت
.
@Farsna</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/farsna/445660" target="_blank">📅 17:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445659">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a3acef7d.mp4?token=fPiocJdlR9BSlmOb04-Yh_JSeMKIB82Yg8em_FHoS68--jvC0TY4Lm4ljEHXr3cT4uD8yNP_74lxkNJiuLrwVCpgpLnXisGUMSeutbgQMmETzdZdJG0ojtFrT5dOYxFIOS-dRRfSEUXC90t7VczwYmVx0sKTvCdusNwl1mw9NmYNzqw6ngbiFVcL9ZlxGHPa7R9jSo08JjaA6tWDpCpmWxhE32soZjjQmfS9vqj59s1oUC3Fa24sYQ8REFb45-HGW0POXyscwrbcqP7k3N-uguhb8Pcbz7PkWJ03IRCb3Csy1PGH49lIg1-Je5LdDbTDlg5_H3SDyJfF2lZz4xXXgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a3acef7d.mp4?token=fPiocJdlR9BSlmOb04-Yh_JSeMKIB82Yg8em_FHoS68--jvC0TY4Lm4ljEHXr3cT4uD8yNP_74lxkNJiuLrwVCpgpLnXisGUMSeutbgQMmETzdZdJG0ojtFrT5dOYxFIOS-dRRfSEUXC90t7VczwYmVx0sKTvCdusNwl1mw9NmYNzqw6ngbiFVcL9ZlxGHPa7R9jSo08JjaA6tWDpCpmWxhE32soZjjQmfS9vqj59s1oUC3Fa24sYQ8REFb45-HGW0POXyscwrbcqP7k3N-uguhb8Pcbz7PkWJ03IRCb3Csy1PGH49lIg1-Je5LdDbTDlg5_H3SDyJfF2lZz4xXXgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«شاه‌بوف» بزرگ‌ترین جغد ایرانی در قاب دوربین محیط‌بانان آبیک
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/farsna/445659" target="_blank">📅 17:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445658">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YrRO20t-RzQoxHpQWkJDvx3eL-foZSdS95ejE7CIhSsRIe0Vru8EP4Y9S-SwhoFFFQBh6SWHJF-nAFpwa6KwTiCM8bhMupGJ20fasGlsjjKcTySoJp5MbTw-vCA1rQs29U1W2VG22iwDveZWBTj8o22k6zL-IEPVc_tIGsJ2YTRCwJYqQp20zhXPeziMoE7EodrhCSb19LgM8GoM3UP4y1dyaDV8Aw7wrtHurD4PeuekciyZsTFiULEeMU_4Ljyo6uv5A2iM6av0Vcj-FjWlNzQQ1T6f-94Pmp-Zd5Pd1uBGfcpc3lTFKTv8LQwEdafIRCbGWWO3YhopksOFkfJUXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکست حقوقی متا در پروندهٔ آسیب به کودکان
🔹
رویترز: ایالت‌های شاکی می‌گویند متا با طراحی ویژگی‌هایی مانند اسکرول بی‌پایان، اعلان‌های مداوم و سازوکارهای تشویق‌کننده تعامل، کودکان و نوجوانان را به استفاده افراطی از پلتفرم‌های خود وابسته کرده است.
🔹
قاضی پرونده همچنین به نفع ایالت‌ها حکم داد که متا در برخی موارد الزامات قانون حفاظت از حریم خصوصی کودکان در اینترنت آمریکا (COPPA) را رعایت نکرده و نتوانسته رضایت والدین و اطلاع‌رسانی لازم را به‌درستی انجام دهد.
🔹
این پرونده بخشی از موج گستردهٔ شکایت‌ها علیه شرکت‌های شبکهٔ اجتماعی در آمریکاست؛ جایی که هزاران پرونده، شرکت‌های فناوری را به ایجاد اعتیاد دیجیتال، آسیب‌های روانی و به خطر انداختن سلامت کودکان متهم کرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/445658" target="_blank">📅 17:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445657">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYuXG-RwgoJiCxeQSoR90P2hURqobuMZgT4E2g3J5gBpn0hSjoRN-i9b5nkeAPaH9EE6Yi-mF5yZso6VdfdlEDLJ8qAomRU_SOwYETcu1RLQ3bRdoWIzZBJdBGwIQvDATGyubzloXAFyhB4vU8LJzhmkWmLaugkvTTpwZ2yl44u1WJNO7CFlcAB_6c8lM9HXFd1pnN4WPntZ3otsON83u2MNO8Ggs89vp7Fd68KaadSagQFcXNbsW74UAqrfhYLFiIEaDrETmsC33eaR7IiqaYhmnuTaDUouRWdyMM56DPtF8XSEvzSNyuwh7UP0q2bimrwXdOO3gZHR9hDiAJN6xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۹۰۰ مدرسۀ مشهد میزبان زائران تشییع رهبر شهید
🔹
وزیر آموزش‌وپرورش از آماده‌سازی ۹۰۰ مدرسه در مشهد برای اسکان زائران مراسم تشییع و تدفین رهبر شهید خبر داد و گفت: این مدارس به‌صورت ۲۴ ساعته خدمات اسکان و پشتیبانی به زائران ارائه خواهند کرد. @Farsna - Link</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/farsna/445657" target="_blank">📅 17:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445656">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ff5c8d2b9.mp4?token=T_DZ9LNKbaLZ9yKMouz_ZPIF6JTMH7VbPILcDuO9SuiezPOLkX7af2jdoEFy6avO8Mg5U9w2F_OJoTZ_gJz0meiHQIxZUHN4rz6mGAD8luWs39cza9fjP_V_nnKpk_uaEezYdYjFcf4X_lR087JOHREF90fLnQXmNDEV9-GlNwtNZjAGhQxuQ4hAeIqaTeb1GdIimYFHCGwWRfa9CQ74QmJ01LwgmrcDP58pQ3EyXdWwomP8CI8_cjXOIz_8mm4o1MeR1PYOjoDUHIQxXaaLttT8sXZMQm-GLzF-uQ14nlotIcEyT1kjJcmKRmAumG-ZXDGveIc_XZjfJGqWT8kl-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ff5c8d2b9.mp4?token=T_DZ9LNKbaLZ9yKMouz_ZPIF6JTMH7VbPILcDuO9SuiezPOLkX7af2jdoEFy6avO8Mg5U9w2F_OJoTZ_gJz0meiHQIxZUHN4rz6mGAD8luWs39cza9fjP_V_nnKpk_uaEezYdYjFcf4X_lR087JOHREF90fLnQXmNDEV9-GlNwtNZjAGhQxuQ4hAeIqaTeb1GdIimYFHCGwWRfa9CQ74QmJ01LwgmrcDP58pQ3EyXdWwomP8CI8_cjXOIz_8mm4o1MeR1PYOjoDUHIQxXaaLttT8sXZMQm-GLzF-uQ14nlotIcEyT1kjJcmKRmAumG-ZXDGveIc_XZjfJGqWT8kl-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقوع انفجار در تل آویو
🔹
منابع خبری گزارش دادند یک خودرو در منطقه «حولون» در تل آویو منفجر شده است.
🔹
منابع صهیونیستی اذعان کردند در این انفجار ، یک اسرائیلی به هلاکت رسیده است.  @FarsNewsInt - Link</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/445656" target="_blank">📅 17:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445655">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d4b01308a.mp4?token=dXvQV7B9T6QU0kjRsmEoKNl-WEd1a_oKNBOtF2udCq7xf6ZSiftst1SOoWBkUb2AtBg15L-_V5VuL1KrxnP24Z26Pf67b9g3QlqSCcdrGQ8vu_IybP_qzbfIdyrHat6vhxTI8NnJ4zBEB7dVhrgVWurv1ingGY5LYKyJhMwCS3VcwAhRk6oKAljAlSgEXGMHZjsN2w_YNvo4954602E6DPV90hRLLrEztj4I-A-1xQC1RBxmwbHjN_YzhupZA-FTOUSeHOIeiRvxTfu5yxv7sOjJ8zhv1Fm6y-uJ4iCSmQk-SEGRbcnQt4iaam97yAkhVgEhhodT6KFFPSFfeSI3wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d4b01308a.mp4?token=dXvQV7B9T6QU0kjRsmEoKNl-WEd1a_oKNBOtF2udCq7xf6ZSiftst1SOoWBkUb2AtBg15L-_V5VuL1KrxnP24Z26Pf67b9g3QlqSCcdrGQ8vu_IybP_qzbfIdyrHat6vhxTI8NnJ4zBEB7dVhrgVWurv1ingGY5LYKyJhMwCS3VcwAhRk6oKAljAlSgEXGMHZjsN2w_YNvo4954602E6DPV90hRLLrEztj4I-A-1xQC1RBxmwbHjN_YzhupZA-FTOUSeHOIeiRvxTfu5yxv7sOjJ8zhv1Fm6y-uJ4iCSmQk-SEGRbcnQt4iaam97yAkhVgEhhodT6KFFPSFfeSI3wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملات گسترده به شیعیان روستایی در حمص توسط عناصر وابسته به الجولانی
🔸
منابع محلی مدعی شدند عناصر وابسته به الجولانی در روستای المزرعه، دست به عملیات گستردهٔ بازداشت، برخوردهای خشونت‌آمیز علیه ساکنان شیعه زده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/445655" target="_blank">📅 17:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445654">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iF6Nf9JmbLycq99RYkAqrDOx-H0QEfSncsrsQid-JiIX8ftHFPYOpiZiKEjOUbS1ps5IDZIC0M6lJdN6kJI67hz_EJ4fsffsU47GdHFST6Dp-EcqupHlXCuyrIrZCwqJ-Cg09EAAfIp3MclVA3c0UqUExqvP0H7wLC6KNd2OqpGfhvvmIuLh0PSo8WGW_WRs3fkOy7JYp4LZ1CVomBFz4Rh5KU3PygJMtcM4B_4oL06lydRPTYM1LdizHfDe6zwq85YZtTYZCyBHz53Y1M1_hTF46WypXtXfAG-fxUeVPNZVa1CZDSFN9yHDdQFYuXUi5b-060d-23GvNn9dvhhejw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکاتی برای استفاده از موبایل در مراسم تشییع رهبر شهید
🔹
قبل از حضور در مراسم، تلفن همراه خود را به طور کامل شارژ و محل ملاقات با همراهان خود را از قبل مشخص کنید.
🔹
در صورت امکان، پیامک را جایگزین تماس صوتی کنید و اگر تماس برقرار نشد، چند دقیقه بعد دوباره برای برقراری ارتباط اقدام کنید.
🔹
ارسال عکس و ویدئو را به پس از پایان مراسم موکول کنید و از مصرف غیرضروری اینترنت و بارگذاری فایل‌های حجیم خودداری کنید .
🔹
برای صرفه‌جویی در مصرف باتری و داده، برنامه‌های غیرضروری فعال در پس‌زمینه تلفن همراه را ببندید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/445654" target="_blank">📅 16:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445649">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HwPk35v41h91LbbMV_I6zYJgJUGQ0ADXaikwUxy933gEghC19X3c3uEU3Ot3vBL3NRdHqrLxe7Jb34aDFV65buPe34ItiHInvRBFJvu_4UArKWcX625_hf3ThKJ01gM6_8ztoju7uZTHugwzA9SnI9dFhed9ICiUKrV5KDnSG0lwqg3FYJgJttKyjU-9Fw-L4DSoMAZ5VDh9w59J8SDu8_owtLDKTXkeI4BzB_Hge1Bi-Mt-jj4MJETudwlcptk3Fiu99iywALKwQNg1S7-oHXFmIqgy3b_du9MI7D8mACht7o1mtmteB_re9JGfnPYWlWUC17wBMM7iUDxhHNpQuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LNUJ8xS-O6bUMrlXKAtisTx9yqes-lxT8WnbJzJ7GmVfWs2jQzBQzkoZQQXqbUGu8cGXklO5gD4-UhvcL02arbSi-g5g48erqiaDN80hwxKxQ3MFq0MKG-f6B7J5qrOc937byr5zkv4lng-q377AAHnqLIJ1g1c5_ikY7V1-OuNUP5kd6M7l0UaYf1r2FXcbb4W2XnNjRPqWEn1WLTRpPYOwOD0QONPjgMPdoZ25F5i1FWmftlhjEetyQQCjn8KTbyBtgXP9ILDVInqIK6qHDqmkZoVz6Z6XXkGnK0N04xXVu0N0ZlmqzTBktV_o3k0wWEyfUyPmSyWgd8b3b3OZqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hrLHoKU4nx-Yj2Cd_95nq9P3dF6D9Phrbcop-2XA0VKgkDb0CgScx4aDWnMa5lDL-lIHHdUqDrX_0_UmHTYd0qMeom718iY9-klHloufChmOwQVVyP6z0eGMFHLbHfIkSvWDkUfZZBPQMlRIlLwNpF_o4aM9oZWpbloY3ShbLhbk4KxN5CFathNX_yeY7MkdTdw33QznIpr1s56ESjZ8KK3A-E_mdSPJNYkIjQYawiEH42ZHvCjBBcpZK4cdZHg3Ej2jwu0N56JefavyIIRezQpUXDwHxd0fN0fFSZcCLCd2mjLrTmy3pBPgUZIqTYmbrawx0nnyMIlUKpoHqp-wKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QITKDclW8Iz3dBEhnovZTGxb1ru6sOUTQ3hJCovRNYzvq0siFRfz9M4DK6PLYSl7FEShTQ1upitIfKxc5I9S9RN9EztA-wc4Va638JaxIuHSvv81j2OuTFQmeXenCUoNQU6VbR6Un3823I4T0I9fsBcvXhWYBeVMFGuEebLJa6FkERc1Wylsu0uu0Yl66S6eAMzMKpcgd6l8b7vdFVP6Nijz6YJaASsVyNlPo0b_Cy7OheoD3KVQT7104cZD8rKyp6pX2nCjNSjCmWoX1yj2Aj9kPsRPvOXatx51PiFy0cT3AHbekQBj_zOsWEyh5ygWPOfTnw_81FFAxU0FoiCWjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QRQJH3YLEX-qplwMvqU-7h2HW48mk2YRxrxcild5RS1n5fSdhkEu50fneHFwDBmJ8XilAUXCy4HGkOMmAKzfWeFftWI0HjxbSswvzkW_Pm5936aaBH0HBOxPjSnQucMo-rkcg2ukzqE38GK5eHso45DUhkuDaMXA_MJr8iyAcjKneP7yYBIKlenL5NOhJ8SwnzxKUVk67uf6Gfpwtinr8MtqWZc8Ow9V8XhPkhmSr8TPJADWusGPrvJ3rixhMzFKwjKDZaF9ziRBdQUdthDteq8tNeCOY-npU9jbICGL_X58fEm_eYtbMGVrRRe_Bc_Mr9lYAZyXwJ5QkEQfiEFsAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
رونمایی از اسناد منتشر نشدۀ رهبر شهید
انقلاب
عکس:
هادی ه‍یربدوش
@Farsna</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/445649" target="_blank">📅 16:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445648">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c148238fc4.mp4?token=REEbT6kWa6r8LGvY7J2Gv-s7ZF5V5i1Ad0EeTK471gUJ41Wy1eo3nIjY9Mm6aYIKND3k-dfoO_qy3DdTZqpLtZd33SRpYYK8gaQdWrdwtMy0uUx530muSxs6OlywCJqgtvHim8KDfMeUA4k7DGwCyESi4vJZOPR5ZupSAhHrUCOzsLqQdhcjYRYYJ0HCbGxXQT-0D4fR-nYKbxcgtvGuwOoxhKt_IZELUzARMHh628CTlqy429uR5lyAf0mDi-ja1ZMsbupO0VqxPv_RYmJlsfzJHmEQ19te0rDxQRkdHb051IHOQfHCmv8gZJc5I8FA7tXv1oNmU2sZOlG2dOMs2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c148238fc4.mp4?token=REEbT6kWa6r8LGvY7J2Gv-s7ZF5V5i1Ad0EeTK471gUJ41Wy1eo3nIjY9Mm6aYIKND3k-dfoO_qy3DdTZqpLtZd33SRpYYK8gaQdWrdwtMy0uUx530muSxs6OlywCJqgtvHim8KDfMeUA4k7DGwCyESi4vJZOPR5ZupSAhHrUCOzsLqQdhcjYRYYJ0HCbGxXQT-0D4fR-nYKbxcgtvGuwOoxhKt_IZELUzARMHh628CTlqy429uR5lyAf0mDi-ja1ZMsbupO0VqxPv_RYmJlsfzJHmEQ19te0rDxQRkdHb051IHOQfHCmv8gZJc5I8FA7tXv1oNmU2sZOlG2dOMs2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس پلیس راهور: ممکن است نیاز شود برای تخلیۀ جمعیت برخی آزادراه‌ها مثل تهران-قم یا بالعکس را یک‌طرفه کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/445648" target="_blank">📅 16:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445647">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cfdee404f.mp4?token=BraJ5YPd9Fvz1Eu1TVvXqQ0XjNhoeBbcoDwSuyByOLZpBuq_rnf6uvFw2lUMyLTfgNcTBBGZw0YOG6A52afG2HJi9oVng1sE1FBRjkgYajucVoM9gGKCf7yE47ZNXGznAeu8LvgUPnXQK_mw8fMd7tDsWqpqbO6eSScnysZjhLLuETImcWXntDVT1o2YaZqcD3dfH5jLa5msfmmyjXUF2NvyxfuOGSM6S7TGU43sYtnKXstCzg7nWpQTK_0q_lkIsUQq81iRjILEZytvwhf19KxsycjPB7A-HCLd9sY3Jz36auAVxVEfDpzj5RluJvtK_FCMwMGO2f9vMRPHI2u8Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cfdee404f.mp4?token=BraJ5YPd9Fvz1Eu1TVvXqQ0XjNhoeBbcoDwSuyByOLZpBuq_rnf6uvFw2lUMyLTfgNcTBBGZw0YOG6A52afG2HJi9oVng1sE1FBRjkgYajucVoM9gGKCf7yE47ZNXGznAeu8LvgUPnXQK_mw8fMd7tDsWqpqbO6eSScnysZjhLLuETImcWXntDVT1o2YaZqcD3dfH5jLa5msfmmyjXUF2NvyxfuOGSM6S7TGU43sYtnKXstCzg7nWpQTK_0q_lkIsUQq81iRjILEZytvwhf19KxsycjPB7A-HCLd9sY3Jz36auAVxVEfDpzj5RluJvtK_FCMwMGO2f9vMRPHI2u8Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در غزه حتی کودکی هم به یک رویا بدل شده است
🔹
در ویرانه‌های غزه، جایی که کودکی زیر بمباران مدفون شده، محمد ۱۰ ساله تصویر جدیدی از زندگی برای خود ترسیم کرده: ایستادن روی پروتز، پوشیدن پیراهن تیم ملی و بردن جام جهانی؛ تصویری که فعلاً فقط در چشمان مادری که هم‌بازی‌اش شده منعکس می‌شود.
🔹
همزمان با اینکه میلیاردها نفر در سراسر جهان جام جهانی را تماشا می‌کنند، محمد با چشمانی مصمم می‌گوید: «من ۱۰ سالم است و هر دو پا و دست راستم را در جنگ اسرائیل علیه غزه از دست داده‌ام. رویای این را دارم که با دوستانم فوتبال بازی کنم؛ فقط بازی کنم؛ بازی. می‌خواهم به خارج بروم، پروتز بگیرم، با پسرها فوتبال بازی کنم. من همچنین دلم می‌خواهد به جام جهانی بروم چون عاشق فوتبالم و آرزوی برنده‌شدن در جام جهانی را دارم.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/farsna/445647" target="_blank">📅 16:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445646">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LI0Kclbr95eT19ZG0gQF0OHujhfHdajT2UhfIFpKdyYVrTm_2b4v7biPPq-j0QPJHY8NpoLRXbU44ocdzE_lBCmpl8McXY41R3Vs0c6NhcLrk9R5tfdJsA_VNdUwABikx34cvIAn_PDij-zRi23higi9UD_Wlmw_HDmci3FftkM_5LU8-1ODBlWnJ88Gh6NE4WBibcko1D4fp61aZmCWgopOv96GicztT7J0emZXAVXWFVk2YCh950iaz7p_VTIMDi-cM6frdL90qwIcr88626lnoGpCWOFP_aoKK21w-Hc4XCC_dKgfT7dmG8XwbsqIiiDldY27v3MTMlS6JYqL8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با اعلام باشگاه سپاهان، محرم نویدکیا فصل آینده هم سرمربی این تیم خواهد بود
@Farsna</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/445646" target="_blank">📅 16:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445644">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1a081ef12.mp4?token=Ca8fIi9gyO-NytP6yZxyJO9B3Eu-gAIIeBdOQ0ZTsfIhlHl2m8O0uUi-Aqz7hiYkXssD9gO4HQ43C1xyuLIeHCOh0FyWwSNVBOfHsf_37eQWwZN32q_7AteUzdU0PgtVkfucZLRiM_fqrwrc6x11nbUS_aBY44uEq0YQa5-KVkEfTbhIV65rMiG5qHNkX5iWugTzRqaucpGMl-F__s9YhQ-0GwQhQmUS-s2efZl_7d1Ji_fRq15aGsshyUdY7lUy3oE2iSdXxLJt84zZwpTjTSrrZjt1roIfTbJHrjIdgkBKvtlwIwPJyGI-fPK-PJBkEsHDEnKWFoXbYGBeM80eJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1a081ef12.mp4?token=Ca8fIi9gyO-NytP6yZxyJO9B3Eu-gAIIeBdOQ0ZTsfIhlHl2m8O0uUi-Aqz7hiYkXssD9gO4HQ43C1xyuLIeHCOh0FyWwSNVBOfHsf_37eQWwZN32q_7AteUzdU0PgtVkfucZLRiM_fqrwrc6x11nbUS_aBY44uEq0YQa5-KVkEfTbhIV65rMiG5qHNkX5iWugTzRqaucpGMl-F__s9YhQ-0GwQhQmUS-s2efZl_7d1Ji_fRq15aGsshyUdY7lUy3oE2iSdXxLJt84zZwpTjTSrrZjt1roIfTbJHrjIdgkBKvtlwIwPJyGI-fPK-PJBkEsHDEnKWFoXbYGBeM80eJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آجرلو، عضو رسانه‌‌ای تیم مذاکره‌کننده: فروش نفت ما کاملا به شرایط پیش‌از جنگ برگشته
🔹
ما قبل از این مدت‌ها ارزان‌تر از قیمت جهانی، نفت می‌‌فروختیم اما حالا بالاتر از قیمت جهانی می‌فروشیم.
🔹
همچنین حدود ۲۰ تا ۳۰ درصد بازار جدید در فروش نفت پیدا کرده‌‎ایم.…</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/445644" target="_blank">📅 15:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445643">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7sgGoAd9BWURamVHLYLGiHL7H0W27UAWGzrsJVkfkvAqKKZmpzPLg6am0fKyyOYT5f5zS0CWCUD9RrqP7OJKuw0ehf9lgBVsdcEsbW-nSeq2jsqgO_Yc7WRIaU_HuHLI_G5uAOJmtEQvdD8RNMdO_xq9wC3z33j5u6aWOHnrACF0V2G42T6KRiWVKFrsg8JCstGnegGDJp-OtJN1B238HL-MFShEGIfFwDQT9piOTYGPqykztg2YxKuUboSfz1og3wh7-z-E_pYGAh6KsKPxXCnjLzVNx0zUulGGETO6Hw0n4RTrbDgpd2yYnK9SD_5CAIH79dFiNiR6HL-NkXfZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات صدور اعلان قرمز اینترپل برای سران گروه‌های تروریستی کردی
🔹
تنهایی، وکیل پرونده تعدادی از قربانیان اقدامات گروه‌های تروریستی کُردی در گفت‌وگو با فارس: صدور احکام قضایی، اعلان قرمز اینترپل و درخواست استرداد برای شماری از سران و اعضای گروه‌های پژاک، دمکرات، کومله و پاک پس از بیش از دو سال پیگیری قضایی و بررسی شکایت‌های متعدد قربانیان صادر شد و درخواست استرداد متهمان به دولت عراق و برخی کشورهای اروپایی ارسال شده است.
🔹
شمار شاکیان این پرونده‌ها بیش از ۶۰ نفر است و ابعاد جنایات و تعداد قربانیان این گروه‌ها بسیار گسترده‌تر از مواردی است که تاکنون رسانه‌ای شده است.
🔹
عمده قربانیان این پرونده‌ها مردم عادی، به‌ویژه هموطنان کُرد و اهل سنت ساکن مناطق کردنشین هستند که سال‌ها از اقدامات خشونت‌آمیز این گروه‌ها آسیب دیده‌اند.
🔹
اکنون دولت‌های میزبان این افراد باید به تعهدات بین‌المللی خود در مبارزه با تروریسم عمل کرده و زمینه استرداد و محاکمه متهمان را فراهم کنند.
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/445643" target="_blank">📅 15:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445642">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0a535da08.mp4?token=eAaedld3o3SM8CkpQelF3dxJkRE1OaHtP5k9afc_UCkYa_KLw6cSjB70xlKKb9KkKxxdmlvDgWwVBvcXPaVyEm6aS5jepitHt4zyQ7b7sy-esrK8bsFQIiVQBrpqCoQPTfMcAB4ODx8vwtxW1QkkqgTTa63rdprodLbJwRnQgCndHbWH9gbUuM4UqoDrVcb1YLWdGC9axSyEe3t6yqEu23NSivQKchm81XL0L6xJ0N7TBGKb0hCAoTkG_A7mCHdN3zzbhJw5I3qAy0aLH_6u1KOFXkNaRiEa2nXJp2QTaiwTOIAIcCnN06sFwZL_GbkWTRK8U2iek0sxre2QbX2Y3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0a535da08.mp4?token=eAaedld3o3SM8CkpQelF3dxJkRE1OaHtP5k9afc_UCkYa_KLw6cSjB70xlKKb9KkKxxdmlvDgWwVBvcXPaVyEm6aS5jepitHt4zyQ7b7sy-esrK8bsFQIiVQBrpqCoQPTfMcAB4ODx8vwtxW1QkkqgTTa63rdprodLbJwRnQgCndHbWH9gbUuM4UqoDrVcb1YLWdGC9axSyEe3t6yqEu23NSivQKchm81XL0L6xJ0N7TBGKb0hCAoTkG_A7mCHdN3zzbhJw5I3qAy0aLH_6u1KOFXkNaRiEa2nXJp2QTaiwTOIAIcCnN06sFwZL_GbkWTRK8U2iek0sxre2QbX2Y3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: قالیباف قرار است به چین سفر کند؛ زمان سفر هنوز مشخص نیست.  @Farsna</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/445642" target="_blank">📅 15:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445641">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3028570678.mp4?token=V22q9Zvu8TDc35rwkINbLlpxnX_QFydbzdqcg17ZFH6Dl-JMIC9m-eoCN2gwnKLaHP_Ecyze3B4yRRPZkConQdIt6buexlkAr6_Elh4YwCBuNK0smmFR4nZN0A3c8FW-2cw3dw0eeAQjJW99Eacas5CU91oPh2Kd3QKE38kZ6DME-jq0VstH-bfPl1nM8Ai9DYKsUHdFGmokxE08tj2lOjeIGGQi7qvQ6JI9TP9_SR8YhLVAkstoG1eI9LfWCsTXzd0cXCOiB1Fuw7quGHjCfCt0QUlSWTn8-Bdx7O_HNXqWDSFwXKi46P0jbn2YTICqbeFXiyJvoAvmd5ahWcdh3y03aUOlcMC3_v3r1_NtoBKemEXBk0xoVAf_wgQzcFuWNsl9iW_NM2pyCen1vmpUPQiTi4k7DQGOh1TzQWLkiC3fo21--0XDyeW-CowG6tvTiT_bmGeOtEiw0h_eNGjDde10mt3imsYMFe0kSj0kUxlhiyqHdxQYXCHhxAUKmBc0hs-Xu-jZOP9WGfydOC3nTv3EhBVftQGu0Hi2vQo6AcsmpNSHICEamhx7lYdTnF8j-MU_dz6rovjjQNE4RD_kHNlf7w4SU_qie7n2iDuy4z_C2RZYTEk8dXuEVmxby8W57f69pEVFGk_pbQH929yMRU4C6195LmNBqhJve9MGmAc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3028570678.mp4?token=V22q9Zvu8TDc35rwkINbLlpxnX_QFydbzdqcg17ZFH6Dl-JMIC9m-eoCN2gwnKLaHP_Ecyze3B4yRRPZkConQdIt6buexlkAr6_Elh4YwCBuNK0smmFR4nZN0A3c8FW-2cw3dw0eeAQjJW99Eacas5CU91oPh2Kd3QKE38kZ6DME-jq0VstH-bfPl1nM8Ai9DYKsUHdFGmokxE08tj2lOjeIGGQi7qvQ6JI9TP9_SR8YhLVAkstoG1eI9LfWCsTXzd0cXCOiB1Fuw7quGHjCfCt0QUlSWTn8-Bdx7O_HNXqWDSFwXKi46P0jbn2YTICqbeFXiyJvoAvmd5ahWcdh3y03aUOlcMC3_v3r1_NtoBKemEXBk0xoVAf_wgQzcFuWNsl9iW_NM2pyCen1vmpUPQiTi4k7DQGOh1TzQWLkiC3fo21--0XDyeW-CowG6tvTiT_bmGeOtEiw0h_eNGjDde10mt3imsYMFe0kSj0kUxlhiyqHdxQYXCHhxAUKmBc0hs-Xu-jZOP9WGfydOC3nTv3EhBVftQGu0Hi2vQo6AcsmpNSHICEamhx7lYdTnF8j-MU_dz6rovjjQNE4RD_kHNlf7w4SU_qie7n2iDuy4z_C2RZYTEk8dXuEVmxby8W57f69pEVFGk_pbQH929yMRU4C6195LmNBqhJve9MGmAc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مصلی آمادۀ یک وداع
🔹
۳ روز تا آغاز مراسم وداع با پیکر رهبر شهید انقلاب در مصلی تهران باقی مانده و  مسئولان از آمادگی ۸۰ درصدی محل وداع و میزبانی از زائران خبر می‌دهد.  @Farsna</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/farsna/445641" target="_blank">📅 15:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445640">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6721e5386c.mp4?token=OtaKt32wloDQ2S6xJW32duKBgNd7tVcK7yJv1gXP0WIfbDF9NRltrKibWxBmUHxmNNaDbi4D8QrO1bq0AUSV_1w7AGOb5zZaVIvky6FjvRFxo9XLzmXm6xoBH1Xe91CN6DG26Eu_P0kQ0yyDgHbqrq1lC25Bu1pG6yaOfsLunfW-oBcPl9ZbdxHdLTXIaoBupTeT9RuEodb21jHYAswhcvUXFy_xVtuLuV2mlrS7pAJQHr48SVF0K5HwbuJkQRTazGJdi2zponZI4HbP3eAiJ_0C7wZQDLBS80h1sfQWqTYBbW1hoNiEIgifeZgP9Apr6Fqfyr-r-4FDy3D2JPMYdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6721e5386c.mp4?token=OtaKt32wloDQ2S6xJW32duKBgNd7tVcK7yJv1gXP0WIfbDF9NRltrKibWxBmUHxmNNaDbi4D8QrO1bq0AUSV_1w7AGOb5zZaVIvky6FjvRFxo9XLzmXm6xoBH1Xe91CN6DG26Eu_P0kQ0yyDgHbqrq1lC25Bu1pG6yaOfsLunfW-oBcPl9ZbdxHdLTXIaoBupTeT9RuEodb21jHYAswhcvUXFy_xVtuLuV2mlrS7pAJQHr48SVF0K5HwbuJkQRTazGJdi2zponZI4HbP3eAiJ_0C7wZQDLBS80h1sfQWqTYBbW1hoNiEIgifeZgP9Apr6Fqfyr-r-4FDy3D2JPMYdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک، خبرنگار حوزۀ مقاومت: ۵ هزار لبنانی در جنگ اخیر شهید شده‌اند.  @Farsna</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/farsna/445640" target="_blank">📅 15:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445639">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09b27c5566.mp4?token=r0WGaX-DSsQLO5IBbi7Pwqx2pMm9RFLyESx5olPj8-nKvdCmunPO9iCz1sxC6cbcslTmqEUBLOKkDsBfMGnMdCkxMFBEHGc3Lt9bfo8mWdGtwjsXscgljnWmD1QNiS9AroSsy3zlWKHN1zjr8c8TIjuuVZRZ0un2ClrCsxr3ZE0DINiBgM5InvrM5W3dSyv3nkYdXj9GIEglArSSo2dg3y0PTMz4s1lVBuJAvvgJNOBCHQEozKBxFrHStibwPgwBvoQJlEygmzKXn4suzmaLOAivD5AJSMIQiZZ04WAkOOCkl7K1c1qpXEwOF2OmS2-aCoUjl6qrw-qlGVPUK5_fog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09b27c5566.mp4?token=r0WGaX-DSsQLO5IBbi7Pwqx2pMm9RFLyESx5olPj8-nKvdCmunPO9iCz1sxC6cbcslTmqEUBLOKkDsBfMGnMdCkxMFBEHGc3Lt9bfo8mWdGtwjsXscgljnWmD1QNiS9AroSsy3zlWKHN1zjr8c8TIjuuVZRZ0un2ClrCsxr3ZE0DINiBgM5InvrM5W3dSyv3nkYdXj9GIEglArSSo2dg3y0PTMz4s1lVBuJAvvgJNOBCHQEozKBxFrHStibwPgwBvoQJlEygmzKXn4suzmaLOAivD5AJSMIQiZZ04WAkOOCkl7K1c1qpXEwOF2OmS2-aCoUjl6qrw-qlGVPUK5_fog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رقص شادی وزیر آمریکایی پس‌از حذف ایران از جام جهانی!
🔹
مولین، وزیر امنیت داخلی آمریکا: خوشحالم که ایرانی‌ها حذف شدند و دیگر برنمی‌گردند؛ وقتی ویزاهایشان را گرفتیم از خوشحالی آهنگ خواندم و رقصیدم.
🔸
پیش‌تر فدراسیون فوتبال و اعضای تیم ملی ایران از برخوردهای…</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/farsna/445639" target="_blank">📅 15:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445638">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/993e148d52.mp4?token=SCznZDRYyIdWoDte8aS3nyA8ROkdZwq0LtLcbOGCKEOnF9DoVycRyUFjVwAzp6555_Nn57m4JmCq9T7vPrCwkTyGNSrWhFignF9QciaAgmkCaMPTPxCXnm_jnxE2eOdS131X8KdbWCrSlBbuEHTO0VYs69LU2ncY09L9hiSMPaFE3pPGYZ-cPRnBWq48C-vowuxj5FddZNouBJI3e4HGEZAckYzkZNMgkm_PTT6fFol_Yg85SYlLjMJXRB9OWIcZDqGSrH8M16zmPnEXorAMqZkIbc4JkZcDLVmhNj9VzUmsuAkHf6ziDMMZzPso3MmMOxxhYbe28H6SkayAFGXpqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/993e148d52.mp4?token=SCznZDRYyIdWoDte8aS3nyA8ROkdZwq0LtLcbOGCKEOnF9DoVycRyUFjVwAzp6555_Nn57m4JmCq9T7vPrCwkTyGNSrWhFignF9QciaAgmkCaMPTPxCXnm_jnxE2eOdS131X8KdbWCrSlBbuEHTO0VYs69LU2ncY09L9hiSMPaFE3pPGYZ-cPRnBWq48C-vowuxj5FddZNouBJI3e4HGEZAckYzkZNMgkm_PTT6fFol_Yg85SYlLjMJXRB9OWIcZDqGSrH8M16zmPnEXorAMqZkIbc4JkZcDLVmhNj9VzUmsuAkHf6ziDMMZzPso3MmMOxxhYbe28H6SkayAFGXpqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز مرحلۀ سوم ثبت‌نام طرح مسکن استیجاری
🔹
طبق اعلام وزارت شهرسازی مرحلۀ سوم طرح آشیان؛ ویژۀ استان‌های گلستان، ایلام و کرمانشاه، از ساعت ۱۲ امروز آغاز و تا پایان روز چهارشنبه ۱۰ تیر ادامه دارد.
@Farsna</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/farsna/445638" target="_blank">📅 15:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445637">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2b1316d32.mp4?token=KGbF82PXyYxwB8WtvGnWLwG04ssBauy3BWC2DwgULQjtkwCxGHvrh7PL6NryEEkHDSvion7pq3FMJqt3JgbcQfoSVqtEv_euXmbJpw_j39spYiRKCXrQLCfeoDp9-_PVZs3bGGR2gS-Qx3eT7VkILcJj9GWOWtIF8UNepPUshxTSLKftCm930uY6dAxZgYFPYVo_UZWJcTk4h8mHBRuTUtqxQBNrkt30xWmFPHsTZfsjJmlaiEuv0YSbvmDO01RwTzH-aGU77mJpk8mfeiw569ma5KmFPO3SdtRTJvAP3m7vmFrAtg98NGdstZ23IQR1tCWtAikGvF8cvSVvy-hreA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2b1316d32.mp4?token=KGbF82PXyYxwB8WtvGnWLwG04ssBauy3BWC2DwgULQjtkwCxGHvrh7PL6NryEEkHDSvion7pq3FMJqt3JgbcQfoSVqtEv_euXmbJpw_j39spYiRKCXrQLCfeoDp9-_PVZs3bGGR2gS-Qx3eT7VkILcJj9GWOWtIF8UNepPUshxTSLKftCm930uY6dAxZgYFPYVo_UZWJcTk4h8mHBRuTUtqxQBNrkt30xWmFPHsTZfsjJmlaiEuv0YSbvmDO01RwTzH-aGU77mJpk8mfeiw569ma5KmFPO3SdtRTJvAP3m7vmFrAtg98NGdstZ23IQR1tCWtAikGvF8cvSVvy-hreA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: برای شرکت در مراسم تشییع رهبر شهید کشورهای زیادی در سطح سران اعلام آمادگی کرده‌اند
🔹
جزئیات حضور مقامات خارجی در مراسم طی روزهای آینده اطلاع رسانی خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/farsna/445637" target="_blank">📅 15:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445636">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7187261dd.mp4?token=DEAo1Fyoupfj7bEKcAgjTHdZUiEjhNYPoD8wDHN6wdhB7dJOfl3UzqqF347XMUfSy9MDjWNkLy-C6zHtmVBbLqIw4IWTtkbT6YB-x91PuWeKeYkbExoSWVWtmbzj006TFWzFAeoIed31hrqrFFiXy_dqHMmugPrWGgfsAnmPk-H1_T2wKvqgSNPzR1HsHKvJuClaESzHFIf1kIECuyBB1BO85g4jZUMELDE9dZhhAz4TsRfSxLuZL-7x2lIN1teY4G_RPvQjJeNAMmYX-xAVC_LRT3qzktE_3ZwNBhpGGv8eF-ubjWdmqTnKezaL0yqoQl04EAkW9sRUa49Duo7Wbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7187261dd.mp4?token=DEAo1Fyoupfj7bEKcAgjTHdZUiEjhNYPoD8wDHN6wdhB7dJOfl3UzqqF347XMUfSy9MDjWNkLy-C6zHtmVBbLqIw4IWTtkbT6YB-x91PuWeKeYkbExoSWVWtmbzj006TFWzFAeoIed31hrqrFFiXy_dqHMmugPrWGgfsAnmPk-H1_T2wKvqgSNPzR1HsHKvJuClaESzHFIf1kIECuyBB1BO85g4jZUMELDE9dZhhAz4TsRfSxLuZL-7x2lIN1teY4G_RPvQjJeNAMmYX-xAVC_LRT3qzktE_3ZwNBhpGGv8eF-ubjWdmqTnKezaL0yqoQl04EAkW9sRUa49Duo7Wbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دَرِ فردو و نطنز چه زمانی برای بازرسان آژانس باز می‌شود؟
🔹
به گزارش خبرنگار فارس، براساس شنیده‌ها از متن تفاهمنامهٔ مذاکرات هسته‌ای، نقش آژانس بین‌المللی انرژی اتمی صرفاً در مرحلهٔ پس از توافق نهایی تعریف شده است.
🔹
براساس مادهٔ ۸ این تفاهمنامه، در اجرای…</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farsna/445636" target="_blank">📅 15:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445635">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XyxZq8GIR7GVb-KnIEKH2bKTkoTjg6Tsk-SH36Buo42wCmuuphMsrBjG7SAF25UsY-miUsoIHzt65btaD7SgiN97s0l4fSNQoTh-DvjIvGpK-niPwe2UtplLMxfOfWBZejuXQHMVLGL1h9ySfLOLp7uAoif8ayd47m3vCD8bEvcqnC12GIeMEibL0bgV6BdOz5UrTovwJns3KVRmMmYrjmgdwlzhzZLiwLzGWImUZb8dpkTTKLjJ8IHqcwKF5jqOuAfMVDjscp4kHrLYnU997_vp7u7IIaa5SUPCK7q_b7a3t1YyapS2WIjk6STsYWwPpaHuF3hIIrKzK4tiNQu2DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایمیل‌ها و پسوردهای میلیون‌ها ژاپنی لو رفت
🔹
درپی یک حملهٔ سایبری به سامانهٔ ایمیل شرکت KDDI ژاپن، اطلاعات بیش‌از ۱۴ میلیون حساب کاربری شامل ایمیل و گذرواژه افشا شد.
🔹
این رخداد ۶ ارائه‌دهندهٔ بزرگ خدمات اینترنتی این کشور را تحت تأثیر قرار داده و نگرانی‌ها دربارهٔ امنیت زیرساخت‌های ارتباطی ژاپن را افزایش داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/445635" target="_blank">📅 15:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445634">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98ccfea6f6.mp4?token=LnEs3gpPSsHGLs6H22UQse942OnYE1AKfwaErKohtuaiYR5wh3sF9ui5TytOlKY7IWV1krE6u6KiSLUNFkZSkOkZWnQ2AkLvgQS4ZlnQfl3yAwSHaziRXm5URTcp6zJpQHVxponjBTcrkwXjd8o1KMb3GTatu17s-Bu5Hv55Dp9dFepMTGxQ142OgMBL-AZkg6Uaz_MVizZC0sNHmD4veYtK7PAc-Ht0JJ-XFeMA7y9Fs9cR3OCsPa4GF7j-0awplww0ph_DbbmrVt9ZlkqlgGwFtgyzSV8KZPuy3zU5KHbt-Uv9FpI1F5L1NFHiYfktXObHGAfc3RWeUpa7jSiR7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98ccfea6f6.mp4?token=LnEs3gpPSsHGLs6H22UQse942OnYE1AKfwaErKohtuaiYR5wh3sF9ui5TytOlKY7IWV1krE6u6KiSLUNFkZSkOkZWnQ2AkLvgQS4ZlnQfl3yAwSHaziRXm5URTcp6zJpQHVxponjBTcrkwXjd8o1KMb3GTatu17s-Bu5Hv55Dp9dFepMTGxQ142OgMBL-AZkg6Uaz_MVizZC0sNHmD4veYtK7PAc-Ht0JJ-XFeMA7y9Fs9cR3OCsPa4GF7j-0awplww0ph_DbbmrVt9ZlkqlgGwFtgyzSV8KZPuy3zU5KHbt-Uv9FpI1F5L1NFHiYfktXObHGAfc3RWeUpa7jSiR7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: ما تا زمانی تعهداتمان را اجرا می‌کنیم که طرف مقابل هم تعهداتش را اجرا کند
🔹
متن یادداشت تفاهم خیلی دقیق و روشن تعهدات دوطرف را مشخص کرده است. آمریکا به‌عنوان طرف دیگر توافق وظیفهٔ متوقف‌کردن رژیم صهیونیستی در لبنان را بر عهده دارد. @Farsna</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/farsna/445634" target="_blank">📅 15:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445633">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2784e891c.mp4?token=dyy46p5rQNfu6zc49DJ_9234AkbEmkGz9zdnrouH67ANkYdhL72PtzcL6-5sBojCHyONHRzU79QF8i-0QEizazpRUkjHR0fdpObGVyh8StNZz1hpGcYxFGO-A8NRDFgMar0I7baiyi04i8iJSH2MnTa9aYJUvyNewxsQ-FxxFZnDk_paGsNAoaJnPG8Ub1pcXSyUVziBE8LA3qd_oPJvRMYZBB93xvwpk-ukZVa4KkIdEdxeOFTJoo6G6Fdc3ZcJe7xnmawdwGtc5q24lLL4HmHneEdCW29I7VDk7mpmEMgKLoGBotboBzBMBr9v-Lf2DogLt7dsWqzhCeVPJcYjug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2784e891c.mp4?token=dyy46p5rQNfu6zc49DJ_9234AkbEmkGz9zdnrouH67ANkYdhL72PtzcL6-5sBojCHyONHRzU79QF8i-0QEizazpRUkjHR0fdpObGVyh8StNZz1hpGcYxFGO-A8NRDFgMar0I7baiyi04i8iJSH2MnTa9aYJUvyNewxsQ-FxxFZnDk_paGsNAoaJnPG8Ub1pcXSyUVziBE8LA3qd_oPJvRMYZBB93xvwpk-ukZVa4KkIdEdxeOFTJoo6G6Fdc3ZcJe7xnmawdwGtc5q24lLL4HmHneEdCW29I7VDk7mpmEMgKLoGBotboBzBMBr9v-Lf2DogLt7dsWqzhCeVPJcYjug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: اتفاقات سوریه پردهٔ دیگری از اقدام‌های رژیم صهیونیستی مثل اشغال فلسطین و لبنان است
🔹
اقدامات رژیم صهیونیستی هم نقض حاکمیت سوریه است و هم امنیت منطقه را تهدید می‌کند. طرف‌هایی مثل آمریکا که از این رژیم حمایت می‌کنند، باید در مقابل اقدامات آن پاسخگو باشند.
@Farsna</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/farsna/445633" target="_blank">📅 15:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445632">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cbeddcc25.mp4?token=j3aaU9vEeRp99G8F6WlmxsKmJmO8ujEOwSzZpg81Vd7j3nM965Kttb8kMpTRI4al8ad69WIbPWJ0dKeZl0LWVsC6Tz5uwVlr8jIzV8WIAKNRKvbEX1AO8JY4K_zdTyIkFFP0cpBFY89pBkAjvuYFFI4w9F5f5ahWKJXrzUEUIQltnJo5b__7Ah3nL3lItFs_gDb__sGTSbbV_Z8O0307CkOjtQoIIPWSdlG6KNzwTqmAVIFtYM5Nsg35jbRpUdzYc7T71Pk1FpRslEjYsQ5g319w5w2A0VJtkg9wGwkS7zaQSTj_ylUZMOP4TV3R90WmUvt9Ylo7MdIKo1SB1kfvOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cbeddcc25.mp4?token=j3aaU9vEeRp99G8F6WlmxsKmJmO8ujEOwSzZpg81Vd7j3nM965Kttb8kMpTRI4al8ad69WIbPWJ0dKeZl0LWVsC6Tz5uwVlr8jIzV8WIAKNRKvbEX1AO8JY4K_zdTyIkFFP0cpBFY89pBkAjvuYFFI4w9F5f5ahWKJXrzUEUIQltnJo5b__7Ah3nL3lItFs_gDb__sGTSbbV_Z8O0307CkOjtQoIIPWSdlG6KNzwTqmAVIFtYM5Nsg35jbRpUdzYc7T71Pk1FpRslEjYsQ5g319w5w2A0VJtkg9wGwkS7zaQSTj_ylUZMOP4TV3R90WmUvt9Ylo7MdIKo1SB1kfvOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: ما تا زمانی تعهداتمان را اجرا می‌کنیم که طرف مقابل هم تعهداتش را اجرا کند
🔹
متن یادداشت تفاهم خیلی دقیق و روشن تعهدات دوطرف را مشخص کرده است. آمریکا به‌عنوان طرف دیگر توافق وظیفهٔ متوقف‌کردن رژیم صهیونیستی در لبنان را بر عهده دارد.
@Farsna</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/445632" target="_blank">📅 15:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445631">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a1313967e.mp4?token=hwD4YfFj25KF7gHe3jA6w47Ah8HBXlvDFjMxU75tLrwae3u1MW5_8yfwe9v-llC1gnwFD8hgyMCcltQSnPBtTrEiRYrErtjsHcAMGOQWifriJ3oEspKSuKSPOMLyy_q0wZaRekX8S7ZIm6V7FPLkQd0S8eaYZu_ULpkRttsyMEtnJI-e2Aab7DTH0gSHVfLcMDAGvmH6MqEEdF5i94bVK6Qsq5lq2VzN4OM7Kyb5Lu7du7aNcH7S4rE7_S12It-sQa1nYtLIPmS6VK7TL2LiDeNuplhnRtJd8yDsbPiHeulIZNv1BYTF6qhOdByHkMl7jG7BZPeC7rS-BQ0WCC_Oyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a1313967e.mp4?token=hwD4YfFj25KF7gHe3jA6w47Ah8HBXlvDFjMxU75tLrwae3u1MW5_8yfwe9v-llC1gnwFD8hgyMCcltQSnPBtTrEiRYrErtjsHcAMGOQWifriJ3oEspKSuKSPOMLyy_q0wZaRekX8S7ZIm6V7FPLkQd0S8eaYZu_ULpkRttsyMEtnJI-e2Aab7DTH0gSHVfLcMDAGvmH6MqEEdF5i94bVK6Qsq5lq2VzN4OM7Kyb5Lu7du7aNcH7S4rE7_S12It-sQa1nYtLIPmS6VK7TL2LiDeNuplhnRtJd8yDsbPiHeulIZNv1BYTF6qhOdByHkMl7jG7BZPeC7rS-BQ0WCC_Oyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: این که در جامعهٔ ما نظرات مختلف بیان می‌شود را باید قدر بدانیم
🔹
هر تصمیمی دربارهٔ وظایف دستگاه دیپلماسی با همکاری تمام ارکان نظام گرفته می‌شود و اینطور نیست که یک وزارتخانه به‌تنهایی دراین‌باره تصمیم بگیرد.
@Farsna</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/445631" target="_blank">📅 15:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445630">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUhU8BT53DDfuvWvHWtXYv9vknlUJU0LAJwHUr75u1nBlVwmvhEZJJketmfRfzIasoMxLx19sY3Dq8XsKWSsD26VKjFl3F5hiLIIvyKuHMZBb9yix__X8xjsvnOhRopkg8WjEiW5kepwVwW4da7oCnFuI235ONkrR4HsKr91X-fdTW35ijnyDtBGlisjMz1DBrX8RQMOdzibZTNgnach4vRwqVObMZf-KuwadWv9NASvET6PC8Y44TYX_R2IWjbMSUph3JWiDLhfNKmNM8C9lHLZwTq0sPi8FZ5apLeYPN4KjTbMecZLyUXL2mVVl5qq1CTQoeQx3dJzxJT5KooT7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرداری تهران: ایستگاه‌های متروی مصلی، بهشتی و میرزای ‌شیرازی در روزهای جمعه، شنبه و یکشنبه تعطیل است.
@Farsna</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/farsna/445630" target="_blank">📅 15:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445629">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d605389536.mp4?token=aqoAAcUAc3q_0Ua-rksxAefOG4Rh9vD_TThS2hQxsDUMHvJ7-Rg93hb9V2c-ji-W--6aE5GMy75GdAPsephMVVOkSr1JvlVoZm2eUizY5cn0r4nLEsRMP-5i-Hcp4gV0Vj3pcZDJvxEvEUV26MlR8SnZLFbXH5k4pgDJfvHf6EoQmYhUZLuuXpVq2K9RfUsyw5lZKaBgsQH3UTyFy-r8hhQsCFi4aWl_j9OVzWfpz47F8-PU1Ub7deJo7ih4Rq5VGKLdSC7QDV9k7cmR_pV3uQ_h7QXDRi-4hBLdaYOeoC6XDo7egkQkPEb61cE9T1LxdAwH7u80Hg8RMA1bWMG-fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d605389536.mp4?token=aqoAAcUAc3q_0Ua-rksxAefOG4Rh9vD_TThS2hQxsDUMHvJ7-Rg93hb9V2c-ji-W--6aE5GMy75GdAPsephMVVOkSr1JvlVoZm2eUizY5cn0r4nLEsRMP-5i-Hcp4gV0Vj3pcZDJvxEvEUV26MlR8SnZLFbXH5k4pgDJfvHf6EoQmYhUZLuuXpVq2K9RfUsyw5lZKaBgsQH3UTyFy-r8hhQsCFi4aWl_j9OVzWfpz47F8-PU1Ub7deJo7ih4Rq5VGKLdSC7QDV9k7cmR_pV3uQ_h7QXDRi-4hBLdaYOeoC6XDo7egkQkPEb61cE9T1LxdAwH7u80Hg8RMA1bWMG-fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: از ابتدا برای ما روشن بود که ناتو در راه‌اندازی جنگ علیه ایران دخالت دارد و این موضوع را در محاکم بین‌المللی پیگیری خواهیم کرد.
@Farsna</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/farsna/445629" target="_blank">📅 15:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445628">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1a57a9722.mp4?token=Q-HwoDvC7VUh1DBfSNdi1Sxl7N_RDRQqYVFWQiKUprlsBSujkfVTIa3FNxDHwHy8kiwxVl5-s_y8LEr_gT3TGoN_TMsr3RunRgk8us5xKQP-NYf16EFZ3w8vccDyCu5wuUytpl1opZvby_e6r91tmPQaWhmz6gT2DWhFfNQP1T-7CjoHFREK9wqZBHlvjeb828QExt1gq2FfjYJDiBWPcBVUloJoATSgpYBlh068XCxIMcS5arhHt4eNKR_MysITuctP8Zmn27ft1ejS3bup9j3bHwYARQK-Ru2YpXFeWmRSL2atnr-f-DA9mjtLPoY94N8VhrGY68if11r4Eoy7XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1a57a9722.mp4?token=Q-HwoDvC7VUh1DBfSNdi1Sxl7N_RDRQqYVFWQiKUprlsBSujkfVTIa3FNxDHwHy8kiwxVl5-s_y8LEr_gT3TGoN_TMsr3RunRgk8us5xKQP-NYf16EFZ3w8vccDyCu5wuUytpl1opZvby_e6r91tmPQaWhmz6gT2DWhFfNQP1T-7CjoHFREK9wqZBHlvjeb828QExt1gq2FfjYJDiBWPcBVUloJoATSgpYBlh068XCxIMcS5arhHt4eNKR_MysITuctP8Zmn27ft1ejS3bup9j3bHwYARQK-Ru2YpXFeWmRSL2atnr-f-DA9mjtLPoY94N8VhrGY68if11r4Eoy7XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی وزارت خارجهٔ قطر: اموال مسدودشدهٔ ایران آزاد نشده و آزادی آن به پیشرفت مذاکرات ایران و آمریکا بستگی دارد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/445628" target="_blank">📅 14:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445627">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tla4tSogDf1kMZUwBozOlSNt1yba9AHHOqlht5kO8gvvPMN-gnupuEmeC1ebWI0HMk5gw_o-3GCRec5CZsJ1EZ7GyteLovg2OV1BpkFJUsvFHsXH6rk5ErsZni6EIJguaYI_G0xY3MP9KaxivbUp-WIjrW_1BlWVtW4m1czYxvXLAfOtZrZQETBhjodSsKqCo8AY64ctC-OGcF4TAzStDwxJ6g9jEAcSdMX7TkkwP0Mt_KwydbVWFRivW8zG_pA20kd1_CFXTM1ZYYmbQE5GiABnGFh47gcz1YBvEUpTFVcTz94CaRadQIS7n151BFj7RBELvNv3IbpMjSgGyYQZ1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران یک چهارم قهرمان جام جهانی پاداش گرفت
🔹
تیم ملی فوتبال کشورمان هرچند در مرحله گروهی جام جهانی ۲۰۲۶ حذف شد اما طبق افزایش چندین برابری پاداش‌ها شاگردان قلعه‌نویی مبلغ ۱۲.۵ میلیون دلار پاداش از فیفا دریافت کردند.
🔹
پاداشی که تیم ملی فوتبال ایران از شرکت در جام جهانی کسب کرده معادل ۹۳ شمش یک کیلویی طلا است.
🔹
نشریه آس می‌نویسد که قهرمان جام جهانی ۲۰۲۶ قرار است ۵۰ میلیون دلار پاداش بگیرد که معادل ۳۷۳ کیلو گرم طلاست.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/farsna/445627" target="_blank">📅 14:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445625">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95eb2851b8.mp4?token=KH7EhfD8FYVHdDWJ-kY7-d-peqDlyJftlrTVnyONBI4FBIbg87Fuhoio0DmvO2230NzM68r9wqwiK0wPpGwR0Md4r0YD2KKlNpSdvZOxjf6udj90ToNQeuu_TAPkWM9bwVKkkNZhDFuLrVm349r7HF30ScoYHXDN412_xFYyGUGlbImrXivkrml7oPSbrhjKpdMBuyehhL1ap5Ztud3zE9dQeIjs-TQT2lt4jfRvDlwAyZnC6RKisv_l_fZ_e-jxJhfiuZ8gcrujCh_Zd1C9i2_vBen1G9X9cLTkssUwG6kvA4_8F4Gz_WYmF7mhmhuJy8VXOvNUC4jeSeFMkMWuqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95eb2851b8.mp4?token=KH7EhfD8FYVHdDWJ-kY7-d-peqDlyJftlrTVnyONBI4FBIbg87Fuhoio0DmvO2230NzM68r9wqwiK0wPpGwR0Md4r0YD2KKlNpSdvZOxjf6udj90ToNQeuu_TAPkWM9bwVKkkNZhDFuLrVm349r7HF30ScoYHXDN412_xFYyGUGlbImrXivkrml7oPSbrhjKpdMBuyehhL1ap5Ztud3zE9dQeIjs-TQT2lt4jfRvDlwAyZnC6RKisv_l_fZ_e-jxJhfiuZ8gcrujCh_Zd1C9i2_vBen1G9X9cLTkssUwG6kvA4_8F4Gz_WYmF7mhmhuJy8VXOvNUC4jeSeFMkMWuqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: آمریکا صراحتاً دربارهٔ پایان جنگ در لبنان تعهد داده و باید به تعهدش عمل کند.
@Farsna</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/farsna/445625" target="_blank">📅 14:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445624">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94d0f8bf94.mp4?token=BM6rYpgqK8Hq99pDergxNRsNhzwpvFfAOjspqVDilGpIh_OAWZhNa7xL1h5buVPjmS1-iuYhl0fbVys1nF5zPQmRUGu6BXXUbwJtygS8vl02QH1f-SuZ8W0uLq5KFVh_Kr0nGvJYdC8qlWK217pph8KP0_YWGNmMdXIiNI03ABQrnRXBAYF3wLsM9gAc4acigjOlUKOScchKlBSIcSzGP6AIgUd5MEvqmv35sdanZmLSrQ87ZGpsoqeW9EIJsr7gLLLk9XZqaBN0979I9TuGoC_8eO1nNAXxpqBAs-9DkwwhzGc-AWn8S8IwSGvOTLdElwsu1JDyXKZxpehp5FPy8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94d0f8bf94.mp4?token=BM6rYpgqK8Hq99pDergxNRsNhzwpvFfAOjspqVDilGpIh_OAWZhNa7xL1h5buVPjmS1-iuYhl0fbVys1nF5zPQmRUGu6BXXUbwJtygS8vl02QH1f-SuZ8W0uLq5KFVh_Kr0nGvJYdC8qlWK217pph8KP0_YWGNmMdXIiNI03ABQrnRXBAYF3wLsM9gAc4acigjOlUKOScchKlBSIcSzGP6AIgUd5MEvqmv35sdanZmLSrQ87ZGpsoqeW9EIJsr7gLLLk9XZqaBN0979I9TuGoC_8eO1nNAXxpqBAs-9DkwwhzGc-AWn8S8IwSGvOTLdElwsu1JDyXKZxpehp5FPy8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک، خبرنگار حوزۀ مقاومت: ۵ هزار لبنانی در جنگ اخیر شهید شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/farsna/445624" target="_blank">📅 14:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445623">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/781702a3b6.mp4?token=Wn4Jwqj7xsP239roIQJ2zGdvYXN4RBIkKGWxV8ERGMnvKedIxDnNONMBOE5HGhAwXf6-ZV9NM1YWjbiu2vPZOzWiP_q10bJgdR3MVu_DOj3ZzE5BXJBHopUsqU80gxf9zMxBidTqec9JeGoxrBh3zsT4o_AA2H0YoyKGqD4b9kE6WN_Q1JCmmgT1xFxAB4bSiqAf1YTLy3L_an4x3y_as0LaKLyIRlejhQ5RTKdzDJXz1UvZj__NIg0SqZJzL5nkP6KGQ0WOSECCsq7hKNXpiEADnB6j27ByidGew-xktj1oFfAuhDkCLTDi4FFp7x9hGInSU6xnShNoOyt_Zsompw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/781702a3b6.mp4?token=Wn4Jwqj7xsP239roIQJ2zGdvYXN4RBIkKGWxV8ERGMnvKedIxDnNONMBOE5HGhAwXf6-ZV9NM1YWjbiu2vPZOzWiP_q10bJgdR3MVu_DOj3ZzE5BXJBHopUsqU80gxf9zMxBidTqec9JeGoxrBh3zsT4o_AA2H0YoyKGqD4b9kE6WN_Q1JCmmgT1xFxAB4bSiqAf1YTLy3L_an4x3y_as0LaKLyIRlejhQ5RTKdzDJXz1UvZj__NIg0SqZJzL5nkP6KGQ0WOSECCsq7hKNXpiEADnB6j27ByidGew-xktj1oFfAuhDkCLTDi4FFp7x9hGInSU6xnShNoOyt_Zsompw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون وزیر خارجه: اجازه نخواهیم داد هیچ‌ کشوری در تنگهٔ هرمز مین‌زدایی کند و جلوی آن را خواهیم گرفت؛ مین‌زدایی را فقط خودمان انجام می‌دهیم.  @Farsna</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/445623" target="_blank">📅 14:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445622">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXAN_Nwp2A6G5mZLQGuhZ1-Dj-lXEUlF8p-jUhonRLbhgv077RSsM8efUBKeoTVnlkirODAtPyTGu0A3ui0py5By4s1zanH5K-mEgAZGN4z1jOzGn-eYDoYM9XOznWr0yxbJBcpscabYsgCYAAsHTvsBO_uX4wgCEGPxiq3moY7zhrymXz5xFrtitTql75jdguyUzIdbePbQklycA8IxWWjlhu63_4PoaiIXnF2lT2ups2aZmRk9KCqi1expwwivmxPHkDoJk0QIof4aXO4U-lrr5g_hTUML56zurN7iSNs5YH-vQymHylJ3ZPASpHvFKCf_sTaNhY4TYzMKnxfP5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ فدراسیون فوتبال: اقدام دولت آمریکا در ندادن ویزا کینه‌توزانه و کاملا سیاسی است
🔹
در آستانه آغاز جام جهانی، دولت آمریکا در ادامۀ اقدامات کینه‌توزانه خود علیه تیم ایران در تصمیمی غیرورزشی و البته کاملا سیاسی از صدور ویزای ارکان مهم مدیریتی و اداری تیم ملی…</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/445622" target="_blank">📅 14:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445620">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6116f4d7b.mp4?token=lz4l_YM6FtEXei7KQlB_P3tH8zqO21qj6EYe2hHGBM7gHnYyTKLhenDUpcXo99DkPWB1CBI4_HBlYh3iiQtZvuBXoEPKlHMA4mKkck2Tx3dSBJsNqMN-jn4KEjb617e1zACy1nntyKyU2b5AXx_bYbbw1U7RJ6LuE-UTx3H6GkJQCjwzyiTm0b_IgPLbgRbpawtryIWY4bvrwOmFK7L7L2xxgDrQDhmZ-FQvccC4iNfpX-Q119K7hZYgWXe0itpM3wybbRDXrAkO4Twy2xliTql8mz2Cf9pv0VdhNwI9ErJYhk8lnD1m4n_kKMoroB-lDijyaBHMHtlun9EVgi5oSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6116f4d7b.mp4?token=lz4l_YM6FtEXei7KQlB_P3tH8zqO21qj6EYe2hHGBM7gHnYyTKLhenDUpcXo99DkPWB1CBI4_HBlYh3iiQtZvuBXoEPKlHMA4mKkck2Tx3dSBJsNqMN-jn4KEjb617e1zACy1nntyKyU2b5AXx_bYbbw1U7RJ6LuE-UTx3H6GkJQCjwzyiTm0b_IgPLbgRbpawtryIWY4bvrwOmFK7L7L2xxgDrQDhmZ-FQvccC4iNfpX-Q119K7hZYgWXe0itpM3wybbRDXrAkO4Twy2xliTql8mz2Cf9pv0VdhNwI9ErJYhk8lnD1m4n_kKMoroB-lDijyaBHMHtlun9EVgi5oSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اولین وصیت‌نامه رهبر شهید انقلاب
🔹
رهبر شهید انقلاب در خاطرات خود که در تاریخ شفاهی مرکز اسناد انقلاب اسلامی ثبت شده، اولین وصیت‌نامه خود را که در دوران مبارزات نهضت اسلامی در دهه چهل نگاشته شده است، قرائت کردند.
@Farsna</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/445620" target="_blank">📅 14:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445619">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c51995b92.mp4?token=BmmtA58zwzZArPNwLv92zbq9TsaXcjHPXXOxGzXoh0ViX2NvOs9QTEbRNvYCQhnujAkZ108jjtGf25LCcfleqXA-to4khbRHk_XNN9Sd6OfqbNRiRqyhmHpt7MOdQ_rYGbuZKIs0Dq3ZqLB3gjR6zZZx7eC9PhNjudonHEZ420uV0thedB-3f62y_LMB-hxs3B1aUYOQP91oJeeQGSxwg6hLwG5DYFdJCrISnnfGcOY-HEBb1dNSwDIO0glk2vmU4I8kqNCFKiGT6pH4UY5sV82hlWVF_QWMvJWtPRQU7Lq4AU2E0CD2F3pn23J1GTkWTlVpyBBQ-CHKn9bHoaG2JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c51995b92.mp4?token=BmmtA58zwzZArPNwLv92zbq9TsaXcjHPXXOxGzXoh0ViX2NvOs9QTEbRNvYCQhnujAkZ108jjtGf25LCcfleqXA-to4khbRHk_XNN9Sd6OfqbNRiRqyhmHpt7MOdQ_rYGbuZKIs0Dq3ZqLB3gjR6zZZx7eC9PhNjudonHEZ420uV0thedB-3f62y_LMB-hxs3B1aUYOQP91oJeeQGSxwg6hLwG5DYFdJCrISnnfGcOY-HEBb1dNSwDIO0glk2vmU4I8kqNCFKiGT6pH4UY5sV82hlWVF_QWMvJWtPRQU7Lq4AU2E0CD2F3pn23J1GTkWTlVpyBBQ-CHKn9bHoaG2JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فیلمی دیده‌نشده از نوه شهید رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/445619" target="_blank">📅 14:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445618">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6af5efa9d2.mp4?token=kUPmO5AJxBQbu6tbeRBqi07K0IM3wEctUtjPASEiCgwLmXw0WAU7ko0-B2ECPVzvXc7E_6WPATZ8T70SmAWs0Wod09yJqeY_fa2ZGDmVxghJUSeSlD772IN5yqxH01O01dLI_omSrw02q4PGV5DHpYApaqO8WVXmmFNmSa7qVpFU0NlRXaSRkQY7zDJ4EOj3pDA5dAaU853AE0YKMCiLDcgvAcl328CK-O8ogfdha-v34haEJgZlE3ZNB1TuGRqU5mtSGzcSjXtSLOi2GB-59LteiPNtJwWOts5-Ts7KvaI_nqrgIwXZrNtxa48KZtaOxlTadsociT44AuxF0gnzyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6af5efa9d2.mp4?token=kUPmO5AJxBQbu6tbeRBqi07K0IM3wEctUtjPASEiCgwLmXw0WAU7ko0-B2ECPVzvXc7E_6WPATZ8T70SmAWs0Wod09yJqeY_fa2ZGDmVxghJUSeSlD772IN5yqxH01O01dLI_omSrw02q4PGV5DHpYApaqO8WVXmmFNmSa7qVpFU0NlRXaSRkQY7zDJ4EOj3pDA5dAaU853AE0YKMCiLDcgvAcl328CK-O8ogfdha-v34haEJgZlE3ZNB1TuGRqU5mtSGzcSjXtSLOi2GB-59LteiPNtJwWOts5-Ts7KvaI_nqrgIwXZrNtxa48KZtaOxlTadsociT44AuxF0gnzyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
علائم گرمازدگی را بشناسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/445618" target="_blank">📅 14:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445617">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0vLvLb7HjQKbfzQ5ARiSBrCPHImjzxv2M6dv3GRZCgmyXbXPzXh5nOjBHbm5zJpB3KzPNVJ1ABcSYynAa1_uaN-2hXTxwZ81OAGNwVIbFVKMkj2zCyUtdqz2r-zSnweXeKDYcIdmgOTG2SAdOU9dXv8V8QI0AAdJxiCwJt7QnjGiyRIBhOwMMUx3SI8InTTHjmnReGI81myUPgmbr-nU5XmRJH0XVIq8dIbaDbqZs8lJz1JkFmIfBLBH0FzSbm0fo3Xx8gFqDtrp7qhKYpAKF2dlXnblf4NIJUnDdnZWBU3K46nFSbpZ1QbVtNCo46KjfK3CrtaldGvzA1_oH5GaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: ۶ میلیارد دلار از منابع مسدودشدهٔ ایران در قطر آزاد می‌شود
🔹
رئیس‌جمهور در دیدار با آیت‌الله‌ شبیری زنجانی: توافق اخیر، پیروزی بزرگی برای مردم ایران محسوب می‌شود و در چارچوب آن، تحریم‌های نفتی و پتروشیمی برداشته شده است.
🔹
دولت نیز هم‌زمان با پیگیری…</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/445617" target="_blank">📅 14:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445616">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0fc779408.mp4?token=rg-_IcdMHWgO1JNKjsI2MR0zFP28n-Gv8f45lor19JxyUKducJbcUiY0Jar6a-KDsCze9SeoA6RDjIgIrO6i9LsTb86wt-Woi8cfK7PoZXMnS0qu3e2H6jFaw2BXG4qzNQQcS_61CHN5aCAyoyZbgjq_UzcTktY8SnPjFtcKh7Y22o8HQrydHuUhC7q2iwPyGt6EP__ScH6nVuJ3_GQ7nYSZHSsinGOgTxzk3HnP412Bdoz8KinF_mRDW3QoMhhRK2eaCYpIdU5U_tOQsZaeOUWVbK4AK8ihhv_h_OOpBITUdnU7kz5egOIunkMQiELdhU_kx7iRxp8caczZzYXgGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0fc779408.mp4?token=rg-_IcdMHWgO1JNKjsI2MR0zFP28n-Gv8f45lor19JxyUKducJbcUiY0Jar6a-KDsCze9SeoA6RDjIgIrO6i9LsTb86wt-Woi8cfK7PoZXMnS0qu3e2H6jFaw2BXG4qzNQQcS_61CHN5aCAyoyZbgjq_UzcTktY8SnPjFtcKh7Y22o8HQrydHuUhC7q2iwPyGt6EP__ScH6nVuJ3_GQ7nYSZHSsinGOgTxzk3HnP412Bdoz8KinF_mRDW3QoMhhRK2eaCYpIdU5U_tOQsZaeOUWVbK4AK8ihhv_h_OOpBITUdnU7kz5egOIunkMQiELdhU_kx7iRxp8caczZzYXgGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حلقۀ اول و دوم محدودیت ترافیکی در پایتخت
🔹
رئیس پلیس راهور تهران با اعلام حلقه‌هایِ مرکزی این مراسم گفت: در محدوده‌های اعلام‌شده، محدودیت‌های ترافیکیِ موقت برقرار میشود.
@Farsna</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/445616" target="_blank">📅 14:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445615">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22deb930a5.mp4?token=Nx7oIU_y-OkmvKBGjd-P48Q5NyiNmf_wsCV2pLoADgg6NS0yENAN5bpUs-5ZSjffzU-SazeFjUeVSASZ90OmVXSlhD4s7DTrbCKYj1TjlRNCO_Vr1ONqqTgGnDywiCsEugSwkn8LOOvirZL97Xd4KuZZa4IJb0YeeZp6yI3WpRplkxpLDGumBE3KAYOAebhjd2ZtJH85CiGFsC-CkRjtMXYdjAOkLXjO4CHHEunsilApn5Siu9fya7n1SrghojX1quSwx6bJ2F1yTXNa2kzhmrydOE9BGw9aufyKI9JR33BuofawnN0K3PDDc5by6CxTSYaem7Sg4FEL-U_NNree1IzIfL-k6ZijGtehdNdhLCm_RlXJf9sjUJm3Igd1a5FahwEfD6T506llDPZjdaaRKtJqJN_-poeEghc02yWjYVI21vp6yxgVQtJD6yHyeFuPrg0RvLS1149XuOt4_hiLEp9IwEf1nHoq8ahjpAfppdGwOgKo-PjLnsrfVM_s1hCUXWTK7w_rlZ0bYG8VAUHE7esqbi6IY2uefYSRnPFYXHREI3VqC63L6jY-LAskd3bzf6Q3KJ8jTSDQutJPYfS8tIwolYi-dLnG_fBOpw2vArIK2m8zy0Sl9NnaOZU_65KRUCn7ykETWDQQxJw-DMWoRCW51N-tv48Bn4tXRIqoUiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22deb930a5.mp4?token=Nx7oIU_y-OkmvKBGjd-P48Q5NyiNmf_wsCV2pLoADgg6NS0yENAN5bpUs-5ZSjffzU-SazeFjUeVSASZ90OmVXSlhD4s7DTrbCKYj1TjlRNCO_Vr1ONqqTgGnDywiCsEugSwkn8LOOvirZL97Xd4KuZZa4IJb0YeeZp6yI3WpRplkxpLDGumBE3KAYOAebhjd2ZtJH85CiGFsC-CkRjtMXYdjAOkLXjO4CHHEunsilApn5Siu9fya7n1SrghojX1quSwx6bJ2F1yTXNa2kzhmrydOE9BGw9aufyKI9JR33BuofawnN0K3PDDc5by6CxTSYaem7Sg4FEL-U_NNree1IzIfL-k6ZijGtehdNdhLCm_RlXJf9sjUJm3Igd1a5FahwEfD6T506llDPZjdaaRKtJqJN_-poeEghc02yWjYVI21vp6yxgVQtJD6yHyeFuPrg0RvLS1149XuOt4_hiLEp9IwEf1nHoq8ahjpAfppdGwOgKo-PjLnsrfVM_s1hCUXWTK7w_rlZ0bYG8VAUHE7esqbi6IY2uefYSRnPFYXHREI3VqC63L6jY-LAskd3bzf6Q3KJ8jTSDQutJPYfS8tIwolYi-dLnG_fBOpw2vArIK2m8zy0Sl9NnaOZU_65KRUCn7ykETWDQQxJw-DMWoRCW51N-tv48Bn4tXRIqoUiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن‌زاده: شبانه‌روز درحال آماده‌سازی مراسم وداع با رهبر شهید هستیم  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/445615" target="_blank">📅 14:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445614">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0638c37fdc.mp4?token=h5xcB_D4LvYryx555KI8nzzfGqq-aLHOPCBMCTw61eVaXMh74D_59iO_4TFZyeTJzHPPSk5ErrRifxzglcjRv_W11WisT1816iOSf5Xf5jmJHK1jLK3avKp2Z-_rgd22na5awnAxAHtP9p9hPaXoy4Anu0_GiH64lnUwMSHRh4Y9Kw3IDg9tqD_-97h0DFTQyY2iIbnM27dHl9A-yqCCvxoKjFFHZZaLaaZH2TQo-WJHCAcTYJ38xtcCwiNxzuQ_1Rjfrj1VX8Q7fFG-ahRkshnKjZmamzepiyme6ZoUhD3amABaCtBXiwHUsYaW51HYO3DxDmTqtZz2l7qp6uV1kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0638c37fdc.mp4?token=h5xcB_D4LvYryx555KI8nzzfGqq-aLHOPCBMCTw61eVaXMh74D_59iO_4TFZyeTJzHPPSk5ErrRifxzglcjRv_W11WisT1816iOSf5Xf5jmJHK1jLK3avKp2Z-_rgd22na5awnAxAHtP9p9hPaXoy4Anu0_GiH64lnUwMSHRh4Y9Kw3IDg9tqD_-97h0DFTQyY2iIbnM27dHl9A-yqCCvxoKjFFHZZaLaaZH2TQo-WJHCAcTYJ38xtcCwiNxzuQ_1Rjfrj1VX8Q7fFG-ahRkshnKjZmamzepiyme6ZoUhD3amABaCtBXiwHUsYaW51HYO3DxDmTqtZz2l7qp6uV1kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مذاکره در خارج، گفتمان در داخل!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/445614" target="_blank">📅 14:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445613">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🎥
معاون وزیر خارجه: در طول هفته جاری هیچ برنامه‌ای برای مذاکره با آمریکا نداریم
🔹
حضور مقامات آمریکایی در دوحه ارتباطی با حضور هیئت‌های کارشناسی ایرانی در دوحه ندارد.
🔹
کارشناسان ما برای پیگیری تعهدات آمریکا از سوی قطر به دوحه خواهند رفت.
🔹
هیچ نشست و برنامه‌ای…</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farsna/445613" target="_blank">📅 14:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445612">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4rYNM292Jbc-N4mXnWHYTNejRRiJL1E7WvZWfOKj6HwK6iwjssqEJX-iOfLNz3QQf-rxAOXobswNaisK476gI3Q1Nnuf8ta7F1BaWdM4CgBXGWNkO4GMCoTMLu2_CHULo_Ek8OrHRQKg7hPFBpqrwX8-iPRVlTYDlT3Phh5q9Rr5nhvuzH2YjaKaVlHFdq_f-j9h-hfz34G6vQStE0tNc33GdfP9_uXJ-3BEBkqfAZPUzQcoxTOuUuu-F3N4fVAUsaYcrxkHykLMg3kLMVu2UPjYtlCS2oXgrasLqGYhc3PN30UYlVLIBGWeLazd6BxHGOvRzNwWfnTlsscTCQzGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌پورجمشیدیان: محل تدفین رهبر شهید نقطه‌ای انتخاب شده که در آینده امکان زیارت هم‌زمان برای بانوان و آقایان به راحتی فراهم باشد
🔹
دبیر ستاد مراسمات بدرقه و تشییع رهبر شهید: برای مراسم تدفین پیکر مطهر رهبر شهید، یک آیین محدود پیش‌بینی شده است تا بدون هیچ‌گونه…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/445612" target="_blank">📅 14:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445611">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70e58b6322.mp4?token=K2ZWp8ZYAFQBs9U_F_jcmvuM9NQP_5jRzY7tPYKzt4BDTmwdV2XhFMKSAzDirhIfnqBiX27det-soQm7UEsYKaVun6TH-eRK89t0-joPjkLhzayuFnDTEhFKqcp-4j2b7E_aU9952TqoS7X6YtSwwV_kxvM0o8cU9isOfMNCKIl_dCnRqXGHTg0Ka1V-SHd5InAhzRY0p6QN_O2IcWWbSeTFTtXIGkpVbHAwABxhKIVhm9HGG2kI_lnvU8OxlxlhXKkhKK2XiMtiB9TRWceC2aEQb_2tPrZpQe-fXHNoyf3AHLs2bYZaCvnSiImdfIwxVwNIZ3kpk5MMNQBp-HhpoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70e58b6322.mp4?token=K2ZWp8ZYAFQBs9U_F_jcmvuM9NQP_5jRzY7tPYKzt4BDTmwdV2XhFMKSAzDirhIfnqBiX27det-soQm7UEsYKaVun6TH-eRK89t0-joPjkLhzayuFnDTEhFKqcp-4j2b7E_aU9952TqoS7X6YtSwwV_kxvM0o8cU9isOfMNCKIl_dCnRqXGHTg0Ka1V-SHd5InAhzRY0p6QN_O2IcWWbSeTFTtXIGkpVbHAwABxhKIVhm9HGG2kI_lnvU8OxlxlhXKkhKK2XiMtiB9TRWceC2aEQb_2tPrZpQe-fXHNoyf3AHLs2bYZaCvnSiImdfIwxVwNIZ3kpk5MMNQBp-HhpoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آماده‌سازی جایگاه وداع با رهبر شهید در مصلی تهران  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/farsna/445611" target="_blank">📅 13:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445610">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2GWgajw-Xg5N2OJ0DWI48mVbe1i1AA5rU3SqxZBAQvGtj_k26LQ-4Zoa-6llRySw2d0CTmEPYftSEXvExu8jX09pMBu-ABjaotE1ZaP5AF0OpzuFTCl4WZE7d6bsiKmxQ0z_YnO56MKiXbBWkRutZ0j2iEuLZe9oPXFED5dOnHcMfYPBJGlmbNrFie4QLsc8Mfojd64qybq4mT7DC9c8umSjOGcxP3A1WkUXAzE6ACdhEhfaQwbGuQaTBgq8_M51YTknmWMiUox2bU8zzuQtKE7GsEEAaIjY1fCFuDRMIZcIvuoT8I-VtafZmDx_D8IwoM11DATscSFDYH8ob0GQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خروج تودهٔ ۹ کیلویی از یک بیمار در شهرکرد
🔹
منصوری، متخصص زنان‌وزایمان: در عمل جراحی یک بیمار ۴۹ ساله در شهرکرد یک توده به‌وزن ۹ کیلوگرم خارج شد؛ این جراحی با موفقیت به پایان رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/445610" target="_blank">📅 13:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445609">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8Q2ur1TrjKD1PDVwfAE6P3vS9tRK82ViUdl49_g-HzH25sJ46I1gpNWy21FW7jcRBgKwIezI_A8Eyf_PY9fmSjERbRcljDv1F19rcT1olmldRAQ5w1kFsLlR1_f-sx0IAtaF2mzcyDMKz-uB_QC7B2zvJACgT66lXUSpV1RHJFJxb2Gx2XmRDimc6B3ylrvf8pQ1K9kLVq5seYgjNIKqG3ajAOHyXgv5wPGyKbzS1Gp91Pl_4V4ABOP31TaBQ1LNgE_2jizpvxPkkQ3kFxt45KuDiw_fBvp_g3236Wkg9UVwqJF9tMY1LyF4CEof6ojq0Cnt5aVEcOiMWDx0EuT0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺️
#پوشش_بیمه_ای_زائران
و شرکت‌کنندگان در مراسم تشییع رهبر شهید
🔹
صنعت بیمه کشور در راستای ایفای مسئولیت اجتماعی و تامین آرامش خاطر مردم، تمامی شرکت‌کنندگان در مراسم وداع، تشییع و تدفین قائد عظیم‌الشأن انقلاب را تحت پوشش کامل بیمه‌ای قرار می‌دهد.
🔹️
به گفته موسی رضایی رئیس کل بیمه مرکزی، کنسرسیومی متشکل از ۷ شرکت بزرگ بیمه‌ای (ایران، آسیا، البرز، دانا، سامان، نوین و آرمان) تشکیل شده است تا پوشش‌های بیمه‌ای لازم را در چارچوب قوانین و مقررات مربوطه عرضه کنند.</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/445609" target="_blank">📅 13:33 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445608">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromشرکت پارس خودرو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGc7mRlz6-hJHu5CAUieMlL8hbNRXxfb6q7lfbTKgC0OlnC86zXOznZVp2N-6MU7NXI388f0nWmWwPdzdhJIbgjxO4VTPPFuJy4nCdvnXGzGGdWQZ1A3i42x2mw3oBc7Ev3yJQK1AdQ509O5vBcu43rebC3lxDJGd04ujDPSRMxjXr5-J4_wWEAbu64_f5pt6JUcKO6pPmY5JVYoScBDOVvq5yoi1EOejwtqBQJVJUEmWdzbfdMQIjPVkTqclGhC2m72b4sfxt9BjvOXsN6gx4ySQDhtPF7n4txH_tfNkw444pYBlgEuo3Fav6130AI9CbuGOkX-P7XqaIJsdSrDxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمایت بانک ملی ایران از توسعه همکاری‌های مالی با پارس‌خودرو
معاونان ارشد بانک ملی ایران در بازدید از شرکت پارس‌خودرو، با اشاره به ظرفیت‌های این مجموعه خودروسازی در سطح ملی و منطقه‌ای، بر حمایت از برنامه‌های توسعه‌ای، تأمین مالی زنجیره‌ای و تقویت همکاری‌های مشترک برای رونق تولید، اشتغال‌زایی و نوآوری در صنعت خودرو تأکید کردند.
بیژن نصرتی، عضو هیات عامل و معاون بانکداری شرکتی بانک ملی ایران، در این بازدید با ابراز خرسندی از حضور در پارس‌خودرو اظهار کرد: «خوشبختانه امروز از نزدیک شاهد پیشرفت شرکتی هستیم که یکی از نمادهای خودروسازی ایران، منطقه و حتی جهان به شمار می‌رود.»
جزئیات بیشتر:
https://news.parskhodro.ir/news-archive/id/5082
#پارس_خودرو_توسعه_تولید
➡️
@parskhodro_pk</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/445608" target="_blank">📅 13:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445607">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/445607" target="_blank">📅 13:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445606">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIY4bWDodPzteYmOy4e31wA4HCvTqx9AHQsfFRQtrzyjNMNvkqw3U2NvYLgCXRIMHuwegizAH1m2NytRCL3kAE-TQaK_WX63X_7rl9rfOFjuDJHOXih9WUMDlmX5UefRYihhUk8xa0_5B-osmTyEtzuiqgrO3OGv8pbXx3tZr33Co4qkxg0eUjKN-drvtVXhzRndWeLplU-OdXdk_yjf62kntflt2Lr7Ya_UfpR6RsBClNdwHcOwF5Ce0UYSVkgSRjJ4u9xWPe1R29pAbs9ujk661IplRx470wS5FuemTkq9Mgc1FZnSu8gq7gg8FMKNVRmyZzFtIuM94Zsetwidow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
پورجمشیدیان: ۱۷ تیر پیکرهای مطهر به عراق منتقل خواهد شد
🔹
دبیر ستاد ملی مراسم وداع و تشییع رهبر شهید: در یکی از دو فرودگاه بغداد یا نجف مراسم استقبال رسمی با حضور سران این کشور از جمله جناب نخست‌وزیر برگزار خواهد شد. در ادامه، تشییع و طواف در کربلا و نجف…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/445606" target="_blank">📅 12:49 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445605">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6c15c2103.mp4?token=dcbSgQ2n7_cAAWy5_cirwa7PpcDTn-KzL4oJukrWhv00ph0RaPoxJV29mrLz95OYcNaAHr8Ky4rv2K1oAOUh6jVZAzJpNhaDM3-iDynNu35xtUssLw145ik-HzUyfQVdZ3iivdBB9sf6Sai3EmmVIeiloBTt0VKuml7iWrsEkntmwQLIx8awFf8tkTlrdAi_m463KWEslhbXPvNP9908D-lMnyzHJ5156z_2IfbluRpzOsgsdn4dS_fYvGWMb9NG4jnI_9wgkRAAO8GMArrbKCtEK22Ms0o9qeXp8plG0y_geL1MKsX8UwRh3UOQsV1sF0pYI0uSiK6fj_tCt9LlBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6c15c2103.mp4?token=dcbSgQ2n7_cAAWy5_cirwa7PpcDTn-KzL4oJukrWhv00ph0RaPoxJV29mrLz95OYcNaAHr8Ky4rv2K1oAOUh6jVZAzJpNhaDM3-iDynNu35xtUssLw145ik-HzUyfQVdZ3iivdBB9sf6Sai3EmmVIeiloBTt0VKuml7iWrsEkntmwQLIx8awFf8tkTlrdAi_m463KWEslhbXPvNP9908D-lMnyzHJ5156z_2IfbluRpzOsgsdn4dS_fYvGWMb9NG4jnI_9wgkRAAO8GMArrbKCtEK22Ms0o9qeXp8plG0y_geL1MKsX8UwRh3UOQsV1sF0pYI0uSiK6fj_tCt9LlBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس پلیس راهور: ممکن است نیاز شود برای تخلیۀ جمعیت برخی آزادراه‌ها مثل تهران-قم یا بالعکس را یک‌طرفه کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/445605" target="_blank">📅 12:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445604">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a798239640.mp4?token=sBV3WVIgLKyozTSVE63Yac-FPpjEi8nm8uaPWh3jJ0QO4hYhwgcu1JH8oDyaHMH1HgAMpgD3yvmccLVs6Rtqbz_03wWr_b_h2dekuuVJt7uEfSxj2ct-WRP4whL4QCTZPE-MEmD9X_qNj904ACsrpE0JZygtKPwZsXPn5b9xe4awaIufRqyR-sSIGV5fTTH2Nit5BJo4emuK4VPTiwZUJwxUqH9gEIxVVU70hEvam4rul0FLgGug71vMlnlrh3tfTrwlTHUz4zUrw5ZMtv4_xL7I-QuWsL8cZmeMhzIHBWF3MQBGfQK8BwU21caVeU2Xd2YPJUU-Prhu10iTXI4mFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a798239640.mp4?token=sBV3WVIgLKyozTSVE63Yac-FPpjEi8nm8uaPWh3jJ0QO4hYhwgcu1JH8oDyaHMH1HgAMpgD3yvmccLVs6Rtqbz_03wWr_b_h2dekuuVJt7uEfSxj2ct-WRP4whL4QCTZPE-MEmD9X_qNj904ACsrpE0JZygtKPwZsXPn5b9xe4awaIufRqyR-sSIGV5fTTH2Nit5BJo4emuK4VPTiwZUJwxUqH9gEIxVVU70hEvam4rul0FLgGug71vMlnlrh3tfTrwlTHUz4zUrw5ZMtv4_xL7I-QuWsL8cZmeMhzIHBWF3MQBGfQK8BwU21caVeU2Xd2YPJUU-Prhu10iTXI4mFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پلیس راهور: از هموطنان درخواست می‌کنیم در صورت امکان از خودروهای شخصی خود استفاده کنند
🔹
همان‌گونه که هر سال در مأموریت بزرگ اربعین با محدودیت ظرفیت ناوگان عمومی مواجه هستیم، در مراسم تشییع رهبر شهید نیز در هر ۳ شهر تهران، قم و مشهد چنین شرایطی وجود دارد.…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/445604" target="_blank">📅 12:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445603">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twga028AO3x1m9qxm6h2KokxTm6ZHSTD2RlalBM3raG1jmhxQ7mHZTg2GS1triUhedwknyzs6Reh0709udKWahu7NxuWr3axmNy4p5EumM2rcl9g0USEfzoUgwNxSYlzku2mo9ziejPkDzS5fqfKWU0bJK6ETCzFCLXhY4vfgTh1kNc4TCeOW0eb8moJqnUtTMpamK4yU9OmqrgI0m86igRDsMIs4TifSjo5tBh5uHdE855KJwmDrJyJ3hxXYbN8Q9JeQudsPdr9RKDoPRXcVDDRhVtOjwYivh7Q8HFxE6DgV2eizg6yskXi-mwyHOPqKNUdo3dfE1JHGn7iaNlYOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با جهش ۶۸ هزار واحدی به ۵ میلیون و ۱۲۸ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/445603" target="_blank">📅 12:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445602">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01275ed274.mp4?token=Rqnd3nXt5oiFqOGKSu3M8sZZxJdn8jVJ2VvT6Y-dYqUExLzhhuTFvbtL_FwNH_zFXUrSXvrRr5ZydlX97ZdvBBi3H3Ym1NdzeT1lCRJGG36qWsDusD68xEwIol2b0o2m4nCHlL2oE_KJDQmj6UncMDp6v80DKelidkhmOGdUBSLNBMGP__sRmWsMsjAPP-okLHMIJVR_mHf6i2ME8mDf_lmVUrTUvm9PJqS-QN3MLPTkWFEnxo25wW7lf7pHxVR0Q2XBtjeE1a7o1TjQvdycLw6i7PlOppimWU9AnxclARl_GtxxbrZLAEFCLHXlBJjCmuE9wC0SbssAtFMJUxxQNTegIuxvcA5YegJEB5AGaQL8fDbgvYSqY3-zSt1hBp6ycAZuonCiGn1DHvZknt6Oe12lx0mgo8B3MIsQ6CzqFHPLj8SW6zv8rdcLg3Kpf4AlDsKJAjohItwDy5OyVSeyI9f84_GtoRjPFLfNJ4Xo5V9GQC1Tdj5gRQQGPKzL3AyLQTQo3fgT8Zf_za8eM1j-CiFdzAjyElIuazrOe2Dfk7DQl__mUmg8eyHGWc2vSYPGkR5DSxcPC-lWnvhPXlw_2-5foK4WkOLOi_FbBRi7EG9I_7O-kirTi0H5LuXvd0nNFH-LJOKZaahKfYoiclC7Uu_27ahFhzGDwMmwGDZwhGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01275ed274.mp4?token=Rqnd3nXt5oiFqOGKSu3M8sZZxJdn8jVJ2VvT6Y-dYqUExLzhhuTFvbtL_FwNH_zFXUrSXvrRr5ZydlX97ZdvBBi3H3Ym1NdzeT1lCRJGG36qWsDusD68xEwIol2b0o2m4nCHlL2oE_KJDQmj6UncMDp6v80DKelidkhmOGdUBSLNBMGP__sRmWsMsjAPP-okLHMIJVR_mHf6i2ME8mDf_lmVUrTUvm9PJqS-QN3MLPTkWFEnxo25wW7lf7pHxVR0Q2XBtjeE1a7o1TjQvdycLw6i7PlOppimWU9AnxclARl_GtxxbrZLAEFCLHXlBJjCmuE9wC0SbssAtFMJUxxQNTegIuxvcA5YegJEB5AGaQL8fDbgvYSqY3-zSt1hBp6ycAZuonCiGn1DHvZknt6Oe12lx0mgo8B3MIsQ6CzqFHPLj8SW6zv8rdcLg3Kpf4AlDsKJAjohItwDy5OyVSeyI9f84_GtoRjPFLfNJ4Xo5V9GQC1Tdj5gRQQGPKzL3AyLQTQo3fgT8Zf_za8eM1j-CiFdzAjyElIuazrOe2Dfk7DQl__mUmg8eyHGWc2vSYPGkR5DSxcPC-lWnvhPXlw_2-5foK4WkOLOi_FbBRi7EG9I_7O-kirTi0H5LuXvd0nNFH-LJOKZaahKfYoiclC7Uu_27ahFhzGDwMmwGDZwhGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمادگی مردم قزوین برای میزبانی از دلدادگان رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/farsna/445602" target="_blank">📅 12:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445601">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjDiMGoC0t18B9LuZIJevp7K38NpHtjcgKWaZO7boFdWsV5cnArzCkgQugfDKoT10Ntx04EvGVfcTGNIECkRkT8Bo2CCPMdRzdEdpSFga_6_ALHHrme-FZd6C9ztGkd5A91yzQBqEatM8rB8jgUKuqyLfbYxDHLvdV5U3s-hwRavRls8yGdKcEMT_HYd2mfD5oT-9FSv9Ckvj5U1I4IC3nTHAkb2nW_qzBAJYOlRgPcw3FP9Y8mnF_Xk0kvSLXXwpyXkuiM8m2DNjmikV33keaDELoS6Tp_neaOCvt6jh_R5TaXdUO5g47VbQPuj-PHcTpaqlAWsxVRgzQ_JMtnNhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش‌از یک میلیون ظرفیت اسکان برای تشییع رهبر شهید در تهران
🔹
استاندار تهران: برای مراسم تشییع رهبر شهید در تهران، حدود ۷۰۰ آمبولانس، ۳۸ اتوبوس‌آمبولانس و ۳۰۰ موتورلانس در مسیرها و نقاط تجمع مستقر خواهند شد.
🔹
همچنین بیش از یک میلیون ظرفیت اسکان در اماکن عمومی آماده شده است؛ برای مقابله با گرمازدگی نیز اتاق‌های سرد در مناطق پرتراکم پیش‌بینی شده است.
🔹
بیش از ۶۰۰ خبرنگار خارجی برای پوشش رسانه‌ای مراسم حضور خواهند داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/445601" target="_blank">📅 12:33 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445600">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/334b14fe3d.mp4?token=nO76pfIoQnhY7M22G--WeYIVm_KoexPrifONOXA0hy4SkPCxRNWF2dR7RCSbELLJrOE2_686a4g19AvtqylVQqGbHeEkyHuTDPsFGyU7vGK8oajgtHoxhzcr6fuyDfMSxa3UkuXennAWUnwIUt9vmMTT7y5wbw6bGvBBbv_5EzzD2BWhAVF8oqgAsOYVAm5cm8S3QzPqamGS15TphrWLj5mP41J3VvNJWcisb1cpX2kGYGm071PPOeg6uM03iTBgilOes7PnRHETpho9JkM_laJFQAp8irFmL0OYj0Hw14YFyg5Sw81R6wQgSTKp13v4mZ55vLSwYQN3D8D0tZKzLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/334b14fe3d.mp4?token=nO76pfIoQnhY7M22G--WeYIVm_KoexPrifONOXA0hy4SkPCxRNWF2dR7RCSbELLJrOE2_686a4g19AvtqylVQqGbHeEkyHuTDPsFGyU7vGK8oajgtHoxhzcr6fuyDfMSxa3UkuXennAWUnwIUt9vmMTT7y5wbw6bGvBBbv_5EzzD2BWhAVF8oqgAsOYVAm5cm8S3QzPqamGS15TphrWLj5mP41J3VvNJWcisb1cpX2kGYGm071PPOeg6uM03iTBgilOes7PnRHETpho9JkM_laJFQAp8irFmL0OYj0Hw14YFyg5Sw81R6wQgSTKp13v4mZ55vLSwYQN3D8D0tZKzLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پورجمشیدیان: ۱۷ تیر پیکرهای مطهر به عراق منتقل خواهد شد
🔹
دبیر ستاد ملی مراسم وداع و تشییع رهبر شهید: در یکی از دو فرودگاه بغداد یا نجف مراسم استقبال رسمی با حضور سران این کشور از جمله جناب نخست‌وزیر برگزار خواهد شد. در ادامه، تشییع و طواف در کربلا و نجف…</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/445600" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445599">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7BlMv3F9eHVHpZ2gtL_GIfB3_2oVZxCL3yvDdmmy69zVPtGKxJfTuI6L_hhTYQaojHt1d-lwbZnTPcnGpzdmFsmrBhNBszlPaipzqL7Tt2DeRL9N5mIGluUfO7dIHWVEcCVgQpqtXyvd4MOEVymeKkCjZdAKO7haYT71oLNqG1_Ab3vPtjcIFZpupJhF6LhIF-cEiBgkHyFfn_c_n7L5BkBO8WAkiCPMpNLFbZMy8O-lB00eQAm8bFcliNC3SKz2lvKlBS3V6BTo2O_H1xlYDjynfpBt_ynwrnUxsAkMfs8mV5VPxRL1efArOh1_h9BzklJoYBV4rVPOcm2opv78w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متلاشی‌شدن یک گروهک‌ تجزیه‌طلب در مرزهای شمال‌غرب
🔹
قرارگاه حمزه سیدالشهدا(ع) نیروی زمینی سپاه: درپی ورود یک تیم از گروهک‌های معاند و تجزیه‌طلب به مرزهای شمال‌غرب کشور برای اقدامات خراب‌کارانه و تروریستی، این اشرار در کمین رزمندگان قرارگاه حمزه گرفتار و به صورت کامل متلاشی شدند.
🔹
این درگیری در ارتفاعات مابین شهرستان‌های مهاباد و پیرانشهر و با پشتیبانی آتش ادوات صورت پذیرفت.
🔹
در آن درگیری، این تیم ۶ نفره به‌طور کامل منهدم شد و اجساد ۴ نفر از اشرار به همراه انواع سلاح و تجهیزات در اختیار رزمندگان اسلام قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/445599" target="_blank">📅 12:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445598">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab10b6d9fb.mp4?token=Zbjbdh2varFRsCv3WJxp1vIDJToKrjHEDLdzvvjBIphJ4qlrYnTfyJSSCU44D6wPNkPgj-R02o4M56Slpf37XtLfHlfUV9U_9AJuxVvgxN0NhOovwlJHzv9WMm8hXNf1ed9lm_VwbM-cAtCKEYtEU3oEdAWE-Lj3hfpLQ6GDAEGp6asYT9JTXWhGpdH9gJqqfauUFMjUi5kuxWFjE6SgjJ0rayHShkjt19S5xPc_jRYEkLOFG8Th5WiBW17iLHbW45DTSDVwCF_a5p6HX-LcTEOOVtxFk2v7NsV6NFHHy8o4wWAsiVXI5Y9IS3YUdTaoX8wTV3mQPqwk-19HPFVX_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab10b6d9fb.mp4?token=Zbjbdh2varFRsCv3WJxp1vIDJToKrjHEDLdzvvjBIphJ4qlrYnTfyJSSCU44D6wPNkPgj-R02o4M56Slpf37XtLfHlfUV9U_9AJuxVvgxN0NhOovwlJHzv9WMm8hXNf1ed9lm_VwbM-cAtCKEYtEU3oEdAWE-Lj3hfpLQ6GDAEGp6asYT9JTXWhGpdH9gJqqfauUFMjUi5kuxWFjE6SgjJ0rayHShkjt19S5xPc_jRYEkLOFG8Th5WiBW17iLHbW45DTSDVwCF_a5p6HX-LcTEOOVtxFk2v7NsV6NFHHy8o4wWAsiVXI5Y9IS3YUdTaoX8wTV3mQPqwk-19HPFVX_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روبیو: تفاهم‌نامه با ایران فقط یک تکه کاغذ است
🔹
در حالی که این دونالد ترامپ بوده که برجام را پاره کرده و از آن خارج شد، اکنون مقامات دولت دوم این رئیس‌جمهور اذعان کرده‌اند که برجام «یک توافق واقعی بوده» و تفاهم‌نامه جدید با ایران قابل مقایسه با برجام امضا شده در دوران باراک اوباما نیست.
🔹
کاملاگر داو، نماینده کنگره آمریکا، بخش‌هایی از صحبت‌های تلفنی روز گذشته وزیر خارجه آمریکا مارکو روبیو در مورد تفاهم‌نامه ایران و آمریکا را افشا کرده است.
🔹
به گفته این نماینده آمریکایی، روبیو در این گفت‌وگوی تلفنی تأکید کرده که «این تفاهم‌نامه فقط یک تکه کاغذ امضا شده است که می‌گوید ما به صحبت درباره صحبت کردن ادامه خواهیم داد.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/445598" target="_blank">📅 12:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445597">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8611085f0d.mp4?token=AVNW2ppG3Hp9gsSxHPUCXgXGle_yaSsN71p2dJ_t7L4dNsOJttRazKI0AG12qzBHNTidkQbWCTMGjzLYjuUpK_AVfIfya__EMJWMJa7MoVa1X_xCsB56qp5zAKvFqMUbGLdX-tSPFeVRBOSw3rxvYub5Z2Uqn_c-QC3C8QfwmDCzpvlU1WFrU74w7TNVZb7KdyTzeILHR2Nc5fUFMAmGRpkKc4ex__zAGdQPMB_XWDwkx9HUJCAoDiTQzN0Ru6s4rLZJL20uoQZ8r1Nqp3OMHeMMjqJ9WZe5bpgpGtr1_zCPVUO7hpgFj8TVP_emZzvNO2RE2CTrF2yyRrCOhpQJkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8611085f0d.mp4?token=AVNW2ppG3Hp9gsSxHPUCXgXGle_yaSsN71p2dJ_t7L4dNsOJttRazKI0AG12qzBHNTidkQbWCTMGjzLYjuUpK_AVfIfya__EMJWMJa7MoVa1X_xCsB56qp5zAKvFqMUbGLdX-tSPFeVRBOSw3rxvYub5Z2Uqn_c-QC3C8QfwmDCzpvlU1WFrU74w7TNVZb7KdyTzeILHR2Nc5fUFMAmGRpkKc4ex__zAGdQPMB_XWDwkx9HUJCAoDiTQzN0Ru6s4rLZJL20uoQZ8r1Nqp3OMHeMMjqJ9WZe5bpgpGtr1_zCPVUO7hpgFj8TVP_emZzvNO2RE2CTrF2yyRrCOhpQJkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پورجمشیدیان: مراسم اقامه نماز و تشییع پیکر رهبر شهید در قم ۱۶ تیر برگزار می‌شود
🔹
نماز توسط یکی از مراجع تقلید در مسجد جمکران اقامه خواهد شد.
🔹
بسته به فراهم بودن شرایط، مراسم تشییع نیز در شهر قم برگزار خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/445597" target="_blank">📅 12:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445596">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63a4107893.mp4?token=VJ2Mb-zNiC7r34VM-RrX9Hm2aLqolhloT8hv6VmZGNuHNxGyJPoM2M0rGWvrh4XETQleQk_NWWNrxTw-1cvd4E0niDo9obJohuCGq2-Da3jUCdwNa504rBOauy-XFv8dsq0yTIVT2mCeLRQ0g0aw7MfsFfTRh19u4LP7Mh3RS15AwLA2blQQ5HfL5CHYLgOtItI1ycxhv8ddh2YSTP7Ly5YyXE_IVzTK9yuYMqWHSVN4PaO-0panzR77JqQbGMlznPaecmfwP6KyhC6u77SQlyz7AZgimHP1uOUP-WjRzb9RZMVmSbd7FVuf8IW3xrTB0r32WxwxjX9VPA-d3ahXFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63a4107893.mp4?token=VJ2Mb-zNiC7r34VM-RrX9Hm2aLqolhloT8hv6VmZGNuHNxGyJPoM2M0rGWvrh4XETQleQk_NWWNrxTw-1cvd4E0niDo9obJohuCGq2-Da3jUCdwNa504rBOauy-XFv8dsq0yTIVT2mCeLRQ0g0aw7MfsFfTRh19u4LP7Mh3RS15AwLA2blQQ5HfL5CHYLgOtItI1ycxhv8ddh2YSTP7Ly5YyXE_IVzTK9yuYMqWHSVN4PaO-0panzR77JqQbGMlznPaecmfwP6KyhC6u77SQlyz7AZgimHP1uOUP-WjRzb9RZMVmSbd7FVuf8IW3xrTB0r32WxwxjX9VPA-d3ahXFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۴ تیرماه نماز بر پیکر رهبر شهید در تهران اقامه می‌شود
🔹
دبیر ستاد ملی مراسم وداع و تشییع رهبر شهید: چهاردهم تیرماه برنامه نماز بر پیکر مطهر رهبر شهید انقلاب اسلامی و خانواده گرانقدر ایشان در مصلای حضرت امام خمینی(ره) در شهر تهران برگزار خواهد شد.
🔹
پانزدهم…</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/445596" target="_blank">📅 12:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445595">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f9544187d.mp4?token=o-2nbfoTUlq3HYmAl5Ltp1TRrwxk6jDq0cQv_hoTPNu_Xsbw9JDkVVb9j5NsM5lRyv4QjR482zbl9-A_rEpf56aaOrBZ7FblzIVq3lwXtrDSbGbAZVB0PcFlcgnFbMGdmx3FEeNfDedpL-bbfAPAf4iYJWudI2LBjLdCSpfXlnIdazSXLlYkt3Y1iEfM5JGtnVfwLSEw4ObqjcAAc-aBfyBNOTKrnLGC94QuxHNR-qxpNGYnQdPwgxFUVDf6IiprsoZ8RzVUMhYa3BDL52t1zLHL8MAuwGMrh6yTIOMF9WLpLqfVvs7jPFsSX48iwtjaN9gqgMTFjGX94eY030wxug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f9544187d.mp4?token=o-2nbfoTUlq3HYmAl5Ltp1TRrwxk6jDq0cQv_hoTPNu_Xsbw9JDkVVb9j5NsM5lRyv4QjR482zbl9-A_rEpf56aaOrBZ7FblzIVq3lwXtrDSbGbAZVB0PcFlcgnFbMGdmx3FEeNfDedpL-bbfAPAf4iYJWudI2LBjLdCSpfXlnIdazSXLlYkt3Y1iEfM5JGtnVfwLSEw4ObqjcAAc-aBfyBNOTKrnLGC94QuxHNR-qxpNGYnQdPwgxFUVDf6IiprsoZ8RzVUMhYa3BDL52t1zLHL8MAuwGMrh6yTIOMF9WLpLqfVvs7jPFsSX48iwtjaN9gqgMTFjGX94eY030wxug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌پورجمشیدیان: تاکنون بیش از ۳۰ کشور تقاضای حضور در مراسم ادای احترام به پیکر رهبر شهید را داشتند
🔹
سران ادیان و مذاهب و دانشمندان بیش از ۹۰ کشور  اعلام آمادگی کردند که در مراسم حضور پیدا کنند.  @Farsna</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/445595" target="_blank">📅 12:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445594">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AqgJZH_4XEVhkEjwJTBW0S-3w2ukpliUuEI29FHieFEF2rB7etOVpZWKq_KUyZvfJzC2KmN2nCDUljHKW9A9qs38uv3blJu3OTRGLh_ZY1ck5E9jR8cjyF0rld75vmZ7E7KUa8eTy1n4jdx5-ODK_VzChy0KdpkBYcbV-OZmEzd-2Ydb4SM5EVIOPawqJuj4_tW0zABfisIMjkW40N5_jgkazS2tnlwWyK2uHrBdujcZWx8Pb3y6X2Vrd_sahsofctqU_XbhW5LazlXL0deH3UxAKb9n9IHMzoeDP65oSmmirHhw-a3oNEMCQBaCjalwtXwzfGSFz5l-0P6_i8bO5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پورجمشیدیان: آیین تشییع قائد شهید با ملاحظات شورای‌عالی امنیت ملی برگزار می‌شود
🔹
دبیر ستاد مراسمات بدرقه و تشییع رهبر شهید: مراسم تشییع پیکر مطهر رهبر شهید ایران، به‌منظور فراهم‌سازی بستر لازم جهت برگزاری آیینی بزرگ در تراز ملی و بین‌المللی، با تدبیر بیت…</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/445594" target="_blank">📅 12:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445593">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vzR8mD4y_qnWzm-ZUXEMfd5AkidCTafnjIeNZxN0Mz2VK2pcinhQurCTJem-kAMvJ0jaMP-XxHe36-nphvoLtJVn2DqZ77zreeH2mgig1T_ac6I39r99N4mLwhPfCwm9sheJGozFy37N7bs8n4O35Q4dXGEw2UCYTrnT3XmZ6ejoLsyYUx8xZouRAZDf7HfBXg5yXkPxe7M2zlU5JxK4RSQKtaCFbTTOKdcikPybOA80155XmqlPkvsEB8LHgK-8oJSHvZ4jCD4eGJkQXgwbBTmaniRGtDYwNQTynWEO9NEr19BHnj-lk2U7VdbUVUKoz-URpHOdNWT0Cp4I-ljqlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرزاد جمشیدی، مجری تلویزیون بر اثر سکتهٔ قلبی درگذشت
🔹
بنا بر اطلاعات منتشرشده، جمشیدیِ ۵۶ ساله بدون سابقهٔ بیماری و در اثر سکته فوت شده است.
عکس: امیر رستمی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/445593" target="_blank">📅 11:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445592">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E6GA3lw3ZivR-CXmSoYVTLKyF5lG9qRSysycyUQFVVh6BUOMLUFPAh6k3EmbxsljQcYYEFLDb7CpIry8pG_MCIvoxLYWVvk6W6eEXynuOih_KwpQ6no6vIxA2l0-WadILc7TLC_RsjGXhPPkpwEZV9bd6JxWOGRhplUIyLArdF5Zl5Q17d0u-a6uPYD4lxkBwDXSUzduPADk_xDLVkwxdiG4rQjX4ftwK0pOvcEnD7lX_-KbPHVpyg43LJvEljtyw_SSai5JUSsCHwuihZxnZy6mMMqIl85B7gJw_Z5EDkSveGmkCb6v6WdlTZGxRN3VWj5S6h924_lfzxbH_4FEtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پورجمشیدیان: آیین تشییع قائد شهید با ملاحظات شورای‌عالی امنیت ملی برگزار می‌شود
🔹
دبیر ستاد مراسمات بدرقه و تشییع رهبر شهید: مراسم تشییع پیکر مطهر رهبر شهید ایران، به‌منظور فراهم‌سازی بستر لازم جهت برگزاری آیینی بزرگ در تراز ملی و بین‌المللی، با تدبیر بیت معظم ایشان و رهبر جدید انقلاب اسلامی، حضرت آیت‌الله سید مجتبی حسینی خامنه‌ای، ظرف روزهای آینده برگزار خواهد شد.
🔹
برنامه‌ریزی این مراسم ابتدا با لحاظ ملاحظات شورای عالی امنیت ملی و سپس منطبق بر دیدگاه‌های دفتر و بیت شریف مقام معظم رهبری تدوین شده است.
🔹
در همین راستا و با مصوبه هیئت دولت، «ستاد ملی برگزاری مراسم وداع و تشییع قائد اعظم امت اسلامی» به مسئولیت و محوریت دکتر عارف، معاون اول رئیس‌جمهور و دبیری وزارت کشور تشکیل گردیده است.
🔹
این ستاد با مشارکت همه‌جانبه نهادهای دولتی، نظامی و تشکل‌های مردمی، مدیریت و اجرای این آیین باشکوه را بر عهده دارد و جزئیات برنامه‌ها به‌زودی به اطلاع عموم خواهد رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/445592" target="_blank">📅 11:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445591">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">راهنمای پارک خودروها.pdf</div>
  <div class="tg-doc-extra">1.2 MB</div>
</div>
<a href="https://t.me/farsna/445591" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📎
خودروهای خود را
در مراسم بدرقهٔ آقای شهید کجا پارک کنیم؟
🔸
۲۴ پارکینگ با ظرفیت بیش از ۲۰۰ هزار خودرو در مجاورت ایستگاه‌های مترو و اتوبوس برای مراسم تشییع رهبر شهید در تهران در نظر گرفته شده است.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/445591" target="_blank">📅 11:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445590">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0106a9c18d.mp4?token=CtuxrbpOnjmZaoaOOCWcvKGyFPVJps3hV95tiJi11_TwM0sW2IIdkIT8RE3Ft94HuO2husLrSS4uRSx8dQVlIWH9xC0Q2EFAolsnOIpiEG7uW8sTs-dVs-RFXuxZeC7e69g4aniNPdXewxbeYZTowD9TtnXkE8Q5tIZcHseOVtCuyEdpHfAt03koXU-x2CF9p7wlGA-EvrC229haEq8Cm8ghceZBRUyn327AGsqkAPUT9kW7Z34G8r6iZdyAK_Y873FHue8FgJ_4smgWERRjKwOdN203lJvoGKQ3-BqoYJ0Ff-OsWep0ZZqGpw4QGLyEpAtQA3-mOMPtjfU8zP8UBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0106a9c18d.mp4?token=CtuxrbpOnjmZaoaOOCWcvKGyFPVJps3hV95tiJi11_TwM0sW2IIdkIT8RE3Ft94HuO2husLrSS4uRSx8dQVlIWH9xC0Q2EFAolsnOIpiEG7uW8sTs-dVs-RFXuxZeC7e69g4aniNPdXewxbeYZTowD9TtnXkE8Q5tIZcHseOVtCuyEdpHfAt03koXU-x2CF9p7wlGA-EvrC229haEq8Cm8ghceZBRUyn327AGsqkAPUT9kW7Z34G8r6iZdyAK_Y873FHue8FgJ_4smgWERRjKwOdN203lJvoGKQ3-BqoYJ0Ff-OsWep0ZZqGpw4QGLyEpAtQA3-mOMPtjfU8zP8UBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ سخنگوی قوه‌قضائیه: ۱۵ نفر از زندانیان اوین متواری هستند
🔹
بعد از بررسی‌های دقیق و آزمایشات دی.ان.ای مشخص شد که ۳ نفر از کسانی که فکر می‌کردیم از زندان اوین متواری هستند در بین فوت‌شدگان بودند لذا ۷۳ نفر متواری شناخته شدند.
🔹
۵۸ نفر به زندان خودشان را معرفی…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/445590" target="_blank">📅 11:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445589">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda7967e79.mp4?token=Avjn7ptl79YI20puZExOJiU4IWK6eky_rJNlC_9t_16NNMaUPme6OtGycBDyGUVk7PbRrHNwwk8pwwALoOn6thomUH0HPl7n1Le_YOxR1C-khNftSrbGZK82e8TDUIQGpTf8J-K23bHF1wQ1-8ilTyIjC3uy3f1skCsVls9D1-gRwqkKka-OXQZcT-bFZbcumuUVnLA0qLU5swLYdyR7Tiz2xH2QX0BazoPNvqo6QqcivDxBpGS5mfLfD3o4Ol3YJDMxH5gH4N4BBAAhQhjyzDZCzEUQm1eD7-OixoDa5wFxstwTfyJ9NCSdS-VWmP2yE3ZYF-Aw8ZhXS9LDjNX7Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda7967e79.mp4?token=Avjn7ptl79YI20puZExOJiU4IWK6eky_rJNlC_9t_16NNMaUPme6OtGycBDyGUVk7PbRrHNwwk8pwwALoOn6thomUH0HPl7n1Le_YOxR1C-khNftSrbGZK82e8TDUIQGpTf8J-K23bHF1wQ1-8ilTyIjC3uy3f1skCsVls9D1-gRwqkKka-OXQZcT-bFZbcumuUVnLA0qLU5swLYdyR7Tiz2xH2QX0BazoPNvqo6QqcivDxBpGS5mfLfD3o4Ol3YJDMxH5gH4N4BBAAhQhjyzDZCzEUQm1eD7-OixoDa5wFxstwTfyJ9NCSdS-VWmP2yE3ZYF-Aw8ZhXS9LDjNX7Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: سختی کار پزشکی‌قانونی در جنگ باید در تاریخ بماند تا آیندگان بدانند این جبهه چطور در کنار جبهه‌های دیگر ایستادگی کرد.  @Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/445589" target="_blank">📅 10:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445588">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79e864848c.mp4?token=NP4qmURpvF-BN0XxTvD72xehLOJLGqXMBS517Ag9DTNOEUWAlWkHcVWjMBRKRUtExEBMW2wvpvJ-M1N2p8DKE2R0KdMKn1wiAydsb4bckcA9tzLr4v8HzPaIR55UkrMJmY7PjZi7mxK1BkBIxmL9nAB4alr689csE6mgzhLECJPQermywn_n18mSU_hlWXaiKGXspte6dWwp3dxvRFMTNbjOiNkxTMl_w9GyBvRDcVy9lHRHZpuv_MAOUef-I7pa-I_eWnv0sHFTbXyldPPE4z7SlzrJYk-zKYv6K2sktspMqcxWrRHRQc-k7bjRX1b8xRekqKKx06DFeymJ9th6yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79e864848c.mp4?token=NP4qmURpvF-BN0XxTvD72xehLOJLGqXMBS517Ag9DTNOEUWAlWkHcVWjMBRKRUtExEBMW2wvpvJ-M1N2p8DKE2R0KdMKn1wiAydsb4bckcA9tzLr4v8HzPaIR55UkrMJmY7PjZi7mxK1BkBIxmL9nAB4alr689csE6mgzhLECJPQermywn_n18mSU_hlWXaiKGXspte6dWwp3dxvRFMTNbjOiNkxTMl_w9GyBvRDcVy9lHRHZpuv_MAOUef-I7pa-I_eWnv0sHFTbXyldPPE4z7SlzrJYk-zKYv6K2sktspMqcxWrRHRQc-k7bjRX1b8xRekqKKx06DFeymJ9th6yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: سختی کار پزشکی‌قانونی در جنگ باید در تاریخ بماند تا آیندگان بدانند این جبهه چطور در کنار جبهه‌های دیگر ایستادگی کرد.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/445588" target="_blank">📅 10:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445587">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ارجاع پروندۀ تخلف یک بانک دولتی به دیوان محاسبات
🔹
در بررسی عملکرد شرکت‌های زیرمجموعۀ یکی از بانک‌های دولتی ناتراز، مواردی از عدم رعایت صرفه و صلاح دولت در اجرای تکالیف قانونی مرتبط با مولدسازی دارایی‌های مازاد شناسایی و پرونده جهت رسیدگی به  دادسرای دیوان محاسبات کشور ارجاع شد.
🔹
بررسی‌ها نشان می‌دهد در فرآیند انتخاب کارشناس، قیمت‌گذاری و تصمیمات اتخاذ‌شده برای تهاتر دارایی‌ها، اشکالات موثری وجود داشته و در یک مورد بالغ بر ۱۰۰۰ میلیارد تومان انحراف در قیمت احصا شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/445587" target="_blank">📅 10:49 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445586">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce089e9c7d.mp4?token=cRkCMn5Y027Ts6_Oe2cLdb-SFQ-WTbgTSCb_epGZehF1egVMeJXieTC1lZgZ_DCHELzaWvOCWvNe_qac03c9ImOqUEOVH7H1SqHN8KLBpZJYj8Q-hSyrZyd2rElZx47MvPC0VhKdB4L9RZ7dpSWwdnaUAiE-5IxDvmMDSVoAJD2QOwJ0q4vYjuKfPew1h7TRT6CIJ1yh7McsPt-HG0xkr1U4M0mV0NE19HOpOEgkniS0eZrLD601lygDIgdqM_Vv72vVMmprUN7zmAfruSaOOl3Co2sGmzU2wABDI7COddY5pE3x80GiykHSvdGzcSyIpIoftrCwhCKH90B1cz47rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce089e9c7d.mp4?token=cRkCMn5Y027Ts6_Oe2cLdb-SFQ-WTbgTSCb_epGZehF1egVMeJXieTC1lZgZ_DCHELzaWvOCWvNe_qac03c9ImOqUEOVH7H1SqHN8KLBpZJYj8Q-hSyrZyd2rElZx47MvPC0VhKdB4L9RZ7dpSWwdnaUAiE-5IxDvmMDSVoAJD2QOwJ0q4vYjuKfPew1h7TRT6CIJ1yh7McsPt-HG0xkr1U4M0mV0NE19HOpOEgkniS0eZrLD601lygDIgdqM_Vv72vVMmprUN7zmAfruSaOOl3Co2sGmzU2wABDI7COddY5pE3x80GiykHSvdGzcSyIpIoftrCwhCKH90B1cz47rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آماده‌سازی جایگاه وداع با رهبر شهید در مصلی تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/445586" target="_blank">📅 10:46 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445585">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCZUHxq4WWJMZ_q_96WHn-9qyTkNZonfQLxkUjqDOKPsaRoetrVhQMw0w8UjJccV2vKKsYv4ZB_qWuecd4xg6k-ATNVyOEr7q7We-uExlmOxS89esA81iLLIOtF5p1E3QTyntsVZnrn2vuybzLkTGSIovqdIoi9PWSFxjD_H0qCgx9Uyj0Z2QvQvoAu4xc-9iEdbJiUqCC1BgWwXeGnaQowuTEMpKJDwuwLqOiN8I02cN0znQP6VZpAYFRZh3dbJ864Z4xl9Jsn9r2dcjxK7QlCyaGNIFr6P05OBuOkt5Fk-JBWt1rJTuhrAQ9LIY1XPDogfxfaAoB_p_NjAA2dLkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌ شورای‌شهر تهران: شایعهٔ مسدودشدن ورودی‌های تهران برای مراسم وداع با رهبر شهید صحت ندارد
.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/445585" target="_blank">📅 10:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445584">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZw9AF6XTjt94GcU3yot5gtuAVb_eAnMfFhyXTsNC_J5ch7DUFMS70YXna2q6bddlj6U0boFmsANn06207fkRop1DPqVvPyV1w1uYJlhLza0ToRwn7cMOYXY5TiAPAtXj7olzz_G1XqfgFXm-CwOpJC1iClDe94xZ3FDCgm6X1fHJzwL2YhHBNHQAal41ZhNo1exf52MHYmaDhebfhzNWbm91a8lIqCk_tJCCr1clgQtv2cKO87YOtfKosMUAHEJs4_QLxA-qSBR6mfCu1t7YZzYsW348yyyygGzsL8YsfBj4fyw_sXCsedXl9z2vP5zFIvoA93ylhNbmusf_FQWkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرپرست وزارت دفاع: بدون تردید به نقض آتش‌بس پاسخ می‌دهیم
🔹
سردار ابن‌الرضا در گفت‌وگوی تلفنی با وزیر دولت در امور دفاع قطر: با اعتماد به برادرانمان، به دشمن اعتماد نداریم و دستانمان روی ماشه قرار دارد و بدون تردید، در صورت هرگونه نقض مفاد آتش‌بس، اقدام و واکنش متناسب و لازم را خواهیم داشت.
🔹
تنگۀ هرمز نباید مورد سوءاستفاده کشورهای فرامنطقه‌ای قرار گیرد. حضور نیروهای بیگانه نه‌تنها امنیت‌آفرین نیست، بلکه موجب افزایش سوءتفاهم، بی‌اعتمادی و ناامنی می‌شود.
🔹
حمایت‌های آمریکا به جنایت‌های رژیم صهیونیستی در غزه، سوریه، لبنان، قطر و ایران موجب تداوم حیات و گستاخی این رژیم شده و موجودیت و حیات آن در گرو ایجاد بحران و تنش در منطقه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/445584" target="_blank">📅 10:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445583">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a10ae23b8.mp4?token=tdctmrX3AZJW3fJjMgVsNRmJfq3v_YvAYhp6nAy3War61cU3zhBiCyaBaRpQJgAdHQ_djSzrtPLjkDwyJ9MX9wXwK5Um0Q4uOsLRbBc1IloyXQW767i3_R6tuvVsQSDXvnDa6cUE7EQriXl91ZirndY1DWpBRUTd1MEKIXMQ2q6BAT51YYazshjQ39z_AIYYnFHXUf2f2DgJZO7D-cxMJLE4ZFb-4QL0v8NWHxA21ycWFhkkFjRmq5qTATabdkKE-sJlmHhaT-OSaH1y2t7z0eVl-iiGEYgc4fsqkiHMak7vmznRC8-IILWcia-p9sWyzURsC3gJZrlWjhqhHk-O-i9hAUev1zYQ4V4NLc4FWDoKMbZTjJ_1K9CIVSQWMhPxZX5EYdHtYg8H-OrtXRVR-67jFGPoqF2Pt30wi1tAtLJ6J3fBcZxZ59f828USRaClA3njDdS0-8tbRJzNbV0tXLfbE5WnTZkRNzxE1hCOCAZvxUgEyXd7EysmgWmaZIftrG9fph4Y-jti3SYjZXKuylp8rKzm9KS1SbKOGja9fHpNkJnCk5m_7_C_OaPf4MMXYwi9b7TQdmWz1IX71UM_Keeg5H66gKXbBGTmMSQ9jH6NhQGOmeaX3LzRTT-7TP5woZlAl79oUV1Dn8GgsscT3mvmM7zxSlElwXzkUb8o7TM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a10ae23b8.mp4?token=tdctmrX3AZJW3fJjMgVsNRmJfq3v_YvAYhp6nAy3War61cU3zhBiCyaBaRpQJgAdHQ_djSzrtPLjkDwyJ9MX9wXwK5Um0Q4uOsLRbBc1IloyXQW767i3_R6tuvVsQSDXvnDa6cUE7EQriXl91ZirndY1DWpBRUTd1MEKIXMQ2q6BAT51YYazshjQ39z_AIYYnFHXUf2f2DgJZO7D-cxMJLE4ZFb-4QL0v8NWHxA21ycWFhkkFjRmq5qTATabdkKE-sJlmHhaT-OSaH1y2t7z0eVl-iiGEYgc4fsqkiHMak7vmznRC8-IILWcia-p9sWyzURsC3gJZrlWjhqhHk-O-i9hAUev1zYQ4V4NLc4FWDoKMbZTjJ_1K9CIVSQWMhPxZX5EYdHtYg8H-OrtXRVR-67jFGPoqF2Pt30wi1tAtLJ6J3fBcZxZ59f828USRaClA3njDdS0-8tbRJzNbV0tXLfbE5WnTZkRNzxE1hCOCAZvxUgEyXd7EysmgWmaZIftrG9fph4Y-jti3SYjZXKuylp8rKzm9KS1SbKOGja9fHpNkJnCk5m_7_C_OaPf4MMXYwi9b7TQdmWz1IX71UM_Keeg5H66gKXbBGTmMSQ9jH6NhQGOmeaX3LzRTT-7TP5woZlAl79oUV1Dn8GgsscT3mvmM7zxSlElwXzkUb8o7TM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشییع رهبر شهید نگرانی اینترنشنال شده است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/445583" target="_blank">📅 10:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445582">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JamW718f-oLttuZHx4KnSsnou_rMsH6ZQ7eZgPSsjRA4fRhdchkPQdLO_OXR3IqeiRLDASBRrpqt-HNjj2oium6YXqIThm5uqWT1VDjZ6tHD0RHQ2ToT_Hbu3LFvvzxc9tE32c3D4_ekFJQT9P8CG2zgHsCWc0UnuSQWiv__gFJBjI8rtoEBvZMpWb-Ztyw8TlNWmrRkxGtjpBrNu8aIZceH_1GiqCnxiRAA6CBHqjdMxgQvkdOi6WqZhRYxVVxQTdMXXzP1twiQYl_NohBqnJ6HIdv7fBWFlXyi6Tr3xqrOLwzoFA76aAjZ7jVhaP8-uBrp4v-OdIRWVp3S6xNDig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش‌ به جان پالایشگاه هندی-آمریکایی افتاد
🔹
آتش‌سوزی در پالایشگاه شرکت هالدیا در ایالت بنگال غربی هند به دلایل نامعلوم، ده‌ها زخمی به‌جا گذاشت و حال برخی از مجروحان وخیم است.
🔸
شرکت پتروشیمی هالدیا یک واحد اتیلن با ظرفیت ۷۰۰ هزار تن در سال را در ایالت بنگال غربی هند اداره می‌کند که بخش عمدهٔ سهام شرکت متعلق به شرکت خصوصی در آمریکا به نام «گروه چاترجی» (TCG) است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/445582" target="_blank">📅 10:09 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
