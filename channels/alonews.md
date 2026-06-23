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
<img src="https://cdn4.telesco.pe/file/CJyCIUPhVO5NWmVKZlnon13tPJ7RRghp6_B3Y-RgkDd97qtf5WAhrqiTXEwZ-SXvTuER-i7vHjpIZrYuJRoy5SaPRStAgpnWCEOBGp_j9qnrT-A5lvQjiGnIWPNHZL7nSDm6_FdEKSYsxy_q2doVHVBU-HlKx0auFB27iW-yUzAfUROc7v_WJ_E5BNWPTna_rYgS8RGIK9baCXki0TEbHNz2EAM-0RQWkauGAwVLq7hvtXoULdIc8jLv8XbTslUIwXuymHj-dr0od_04C157iyi2ri08Vdk3IjJYGKgV8zR6INwPH95CmoKAysIgeoZy0Cvq_Dx8uaq0QtKdRzhOug.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 948K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-02 17:59:56</div>
<hr>

<div class="tg-post" id="msg-129879">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
فایننشال‌تایمز:
با وجود افزایش سطح تردد کشتی‌ها در تنگه هرمز، مالکان همچنان سردرگم هستند؛ این وضعیت در حالی شکل گرفته که ایران کشتی‌ها را تهدید به عبور از مسیر نزدیک سواحل خود کرده و آمریکا مسیر عمان را پیشنهاد می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/alonews/129879" target="_blank">📅 17:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129878">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed01390a1c.mp4?token=pYUzNMpz-gnjzp--nwiuj58j9kqGJDZWUQT6tFbVhjc6PGVEmNjgNUmXkCmOudMDfLyJVPzYRuREuv4W1AkwHVlcS2UPsfapeHcEOnQ5tlCxtRuBxBBC-XICejtODa0kYkZ7hf0u36nPWQFOM5AtkC_6NwV3EWCRizpYj8ukYIBapH2MS1hddxNT3o6CiFqoI6sSHcOSimdme0XwrMR2xdjVzszSAZiLzP3KGERHjyU3CKGDEvND89jJNw1tiaczbts8J_tEJ8N5h43718Oq-B1X69Hv6kz6pk8krrH1PaPvRBitq2xhhWrvBI71ZC0ow6YsCPjtTYXDYapoaM249w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed01390a1c.mp4?token=pYUzNMpz-gnjzp--nwiuj58j9kqGJDZWUQT6tFbVhjc6PGVEmNjgNUmXkCmOudMDfLyJVPzYRuREuv4W1AkwHVlcS2UPsfapeHcEOnQ5tlCxtRuBxBBC-XICejtODa0kYkZ7hf0u36nPWQFOM5AtkC_6NwV3EWCRizpYj8ukYIBapH2MS1hddxNT3o6CiFqoI6sSHcOSimdme0XwrMR2xdjVzszSAZiLzP3KGERHjyU3CKGDEvND89jJNw1tiaczbts8J_tEJ8N5h43718Oq-B1X69Hv6kz6pk8krrH1PaPvRBitq2xhhWrvBI71ZC0ow6YsCPjtTYXDYapoaM249w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آیت الله العظمی سید صادق شیرازی، مرجع بزرگ شیعیان: در دوران پیغمبر و امیرالمومنین یک نفر کشته سیاسی هم وجود نداشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/129878" target="_blank">📅 17:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129877">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
عاصم منیر به دیدار پزشکیان رفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/129877" target="_blank">📅 17:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129876">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
واکنش تیم مذاکره کننده به مذاکره موشکی: خلاف است و از اساس تکذیب می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/129876" target="_blank">📅 17:06 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129875">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gb7Yh7C68GnD64Doy5VKyK1HN2ufZbeeaPg_hgLwG-qhRTq0qRuZZbK1uKAPPZnaT7i9PP8EkBZWUVP8CJ7GtQw1EbmoDMH1h9icAJWi5EgSLV8Y6DLmN4XEkGCw87No0SJhikUGsdTkvtswpacxqX1PWeBVvK18uR4S6Rt8jdnDX82VcSC4OWdLLuf-vSTfzc1ng0A8PN5mZRyMIF9yrir5Sb64lx2UZY7CNmYZnKtlxkuXfcWzCHzJT5jjPK37AKAuAyFQSKP9Fl-EsPTxSb1F8ubj09ejYVlOZZYW_9F033ILVd4ppaNQB8URPAJkFDDIJ7ME6eza9wl1hB2wPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت‌ها در بازار طلا، سکه و ارز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/129875" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129874">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AadpCUku4RkIgi2B7EQ5I8wXr5MXNLnlfU70bR9JJIzKqeYh8Fgnf3O-o--hFPr3Auy8RHsGTbkQ2IPRjDhkKXOq-grpvQJqQODApf5E01kXR5VVlp9Sa6vEuAJLypM35pce7s0zPXHdABpE5F4_l1cD3qgIBNhq9KF4EJqBIk5qnOZQx5855Z5dqPaLdWtqJJTA0MTISDdNIOKmJXmbF2kx7oWa-9uwxlPphu2adZK6JwCgGhSDl_sudbSCn96D8sE_W8uQ2L1BeIOKh2cTY45Kn__NjxhKAYq_7-0thc3q3217XrenOxxN40geFRJl3DQS_adaHVeDEIJ2T0HcSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک پست در تازه‌ترین جلد خود، توافق ترامپ با ایران را به تمسخر گرفته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/129874" target="_blank">📅 16:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129873">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
العربیه:
"سعید ایروانی، نماینده ایران در سازمان ملل‌ میگوید انتقال اورانیوم غنی‌شده ایران به خاک روسیه، یکی از گزینه‌های روی میز در مذاکرات است."
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/129873" target="_blank">📅 16:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129872">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQYNC_jVt8YcmYFJ2UFtNTBfeGG_7TSlqW59F7JXpp4Ikpr1wjP3vnlLxEAcOGIcYJgFTj9qbtiEIX0vGQd7jWsTSoKrnE_RVPHFm9BOU_ouwPPenbz1iPo1JAxeMRU6dw8HLyRkdQGKf-Kza0EPOvPkofAHzE94fOYkcE_Uxtz_cQHV20qirBgXHyBmhthdWfi7QE4WY6BVI0-j4WF0cNHa70ltd9h8VEPlwnoHmW7u-vtcIgkEGuPwHGV0qps6mEdpQmjOQWQu1cft5CE1v8cDDCCYN-i01VOGimpftoeWXY5xmncSjEaczQkYtqXhR9prhPh_b1Yu5TRBW-Vydg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجلس از عملکرد عالی وزیر ارتباطات در ایام جنگ تقدیر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/129872" target="_blank">📅 16:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129871">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16bfcc9aaf.mp4?token=mea74tqnUR08bfdxn8TUpJVHm5I_4k9WAF2H4ps7ulOx6iJWqMwo2dKmAgDrg2K1jZaLXr4Ncvrg5T39B7s0QSkwAaRW7NzXulcynMMfjQd7TKHuOkcnbjR1S2XGQebdwfzkYjTu8Waoe6xjMuakNg7q2s8-_Gt7so_gHu10vf1fRuR4imSstpjVm5muWnhAPTXRTFttcGSYJ9Rl0mN9D7Q0qVz4tGFqkDHIl2Ydtg5clqmKmvwfa-qVX1tlNWcEn3-yoTyCdbKli_ucTJJb0Bzi4mx7TeiTBGsD3bl0tyHbiHZzIzEWkNLBezqO2p0ATS7q8TZt3hOeR5r7g4OgZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16bfcc9aaf.mp4?token=mea74tqnUR08bfdxn8TUpJVHm5I_4k9WAF2H4ps7ulOx6iJWqMwo2dKmAgDrg2K1jZaLXr4Ncvrg5T39B7s0QSkwAaRW7NzXulcynMMfjQd7TKHuOkcnbjR1S2XGQebdwfzkYjTu8Waoe6xjMuakNg7q2s8-_Gt7so_gHu10vf1fRuR4imSstpjVm5muWnhAPTXRTFttcGSYJ9Rl0mN9D7Q0qVz4tGFqkDHIl2Ydtg5clqmKmvwfa-qVX1tlNWcEn3-yoTyCdbKli_ucTJJb0Bzi4mx7TeiTBGsD3bl0tyHbiHZzIzEWkNLBezqO2p0ATS7q8TZt3hOeR5r7g4OgZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی دوتا دسته میرسن به هم
مداحاشون:
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/129871" target="_blank">📅 15:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129870">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
وزیر قطع ارتباطات:
تا زمان عادی‌شدن کامل شرایط بانک‌ها، خدمات مشترکان تلفن همراه و ثابت به‌دلیل پرداخت‌نشدن قبوض، قطع نخواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/129870" target="_blank">📅 15:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129869">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
لیست بانک‌هایی که همچنان با اختلال مواجه هستند:
ملت
تجارت
کشاورزی
ملی
صادرات
دی
بلو
کارآفرین
اختلال
❌
نفروختن دلار و طلا
✔️
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/129869" target="_blank">📅 15:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129868">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
شهباز شریف: توافق ایران و آمریکا یک تحول خوشایند است
🔴
نخست‌وزیر پاکستان: پیشرفت مثبت بین دو طرف، نه تنها برای خاورمیانه، بلکه در سطح بین‌المللی نیز یک تحول خوشایند است.
🔴
توافق ایران و آمریکا گامی مهم در جهت تقویت امنیت و ثبات در منطقه است.
🔴
مذاکرات همچنین…</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/129868" target="_blank">📅 15:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129867">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
زنده از ادمین ارسالی به کربلا/آزار و اذیت شش امامی‌ها توسط دوازده امامی‌ها در حرم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/129867" target="_blank">📅 15:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129866">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaaTePv5Hj_uQTsZ4UY05JlHip8bF62jmsYgTqn4J22iZW5criCKLh__pzBdO0ZTPhBYTqRLjdCtls2nwNJi95rycP6joD4mi_lhn6evTK3lEAv_cQ2WIeOeJsVZZkQQHhBF7Kf7C0bpQY07jJFZIoMiGjI2SjQ0u7aHrLbcseDFhW-PdewEAxAVUeRrTt1jM0iaXehJF38BEPxBNiYXgi_Z0C455EWxV7TFvsEKakJtVePUqPYaaeNfhJAFeVjWA8mcdYabKXdmR7zbG8P6MevSFOWvU7h5l3c_KzVSoqtk9c3aIxLppoTvl6fv2eojDW1stxGQq05BBaKMaDI7Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لحظه ورود عاشقانه پزشکیان به پاکستان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/129866" target="_blank">📅 15:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129865">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aee9776a17.mp4?token=RmSgShCdJR7_XwiQRKqUvddHOUeihQuVNU32EsMoXqyTGvaVzpnpfE24Pwjp6UQJbWiqJ9h_yljDBwA13d7UJ9TkMxrd0YTZA13M08ECjDwzY2By-mbogs-fCLOk4RyjLFtTrbr6_3vEaWQjJz4zyGbOHH92jYMBcG4aKvQ-Gmr5GH_EMO751AHPxENztOxQeRwRgFQnEwLI7klTRKGsrTfgTGB5rHvCWHzFjXPEJS3pUeRZ707Ul3Za7B8bvZt9JQ3VECP_pKX2DhEwlsZUUcClSDribbT87FCDvUEw8YYNzneT8wIsym8yRAZg4GxMhj1hkRRG-m4UnHJ65zbHFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aee9776a17.mp4?token=RmSgShCdJR7_XwiQRKqUvddHOUeihQuVNU32EsMoXqyTGvaVzpnpfE24Pwjp6UQJbWiqJ9h_yljDBwA13d7UJ9TkMxrd0YTZA13M08ECjDwzY2By-mbogs-fCLOk4RyjLFtTrbr6_3vEaWQjJz4zyGbOHH92jYMBcG4aKvQ-Gmr5GH_EMO751AHPxENztOxQeRwRgFQnEwLI7klTRKGsrTfgTGB5rHvCWHzFjXPEJS3pUeRZ707Ul3Za7B8bvZt9JQ3VECP_pKX2DhEwlsZUUcClSDribbT87FCDvUEw8YYNzneT8wIsym8yRAZg4GxMhj1hkRRG-m4UnHJ65zbHFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیوی منتشر شده از عباس عراقچی و همتی که وسط مذاکرات با آمریکا پا شدن رفتن بازی ایران و بلژیکو تماشا کردن
🔴
اینجا گفته بودن مذاکرات ترک میکنیم اما رفتن فوتبال ببینن
🔴
فقط اونجاش که گفت الکی الکی رفتیم سمت دروازه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/129865" target="_blank">📅 15:13 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129864">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4XwEMuOlZNvomy9uQ9DZDeQi7vxSdv591TDMRmLNnTMchXruKyxQhvZoYNayZVZXE1z5lzElxq9jTY2ddWS2ZwDqDnkTpUlUKzGCfrBM5sC4yf4EcZTk95I5P5fpd9-HgHVC2OWRYoOQlPHa_kMFPRNn4-MZrHK0RZmy0Smfvl9idX_MbqAMIcjyHDHNuHDzbTbwaoDvXW2Qi2En57H303aq8xzWVWfL2EF8EkPzPVHDDkOPTXHtXvSOoc8wxUndZtYDNipGKF_ULDiAqPmr_CL5snB_J2ooev27fF5tK-FVQpWjrZjCEBuD1ZHilS1Iz1sd5p7fxDUV1ZBpuQyTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: دیروز 19 میلیون بشکه نفت از تنگه هرمز عبور کرد
دونالد ترامپ در تروث سوشیال:
🔴
«دیروز ۱۹ میلیون بشکه نفت از تنگه هرمز خارج شد که یک رکورد تاریخی است.
🔴
قیمت نفت در حال کاهش است و جهان مکانی بسیار امن‌تر شده است!!!»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/129864" target="_blank">📅 15:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129863">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
زنده از کربلا/بیرون کردن شش امامی‌ها توسط دوازده امامی‌ها(اکثرا عرزشیا)
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/129863" target="_blank">📅 15:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129862">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44e336ac3a.mp4?token=ectkXx6USHIRvioXzdHpbIg2G5WzS3sQuce2h9tf0zxlfufkVLfBCgw6GBmOUUwDzfdurEwIU0IASujUHt2ZoPjHV63humjYUVOf-JHzqvZqPibYdtimtNmTSpZcAVwNdzhTsDx9xYLOV8dTprWivn5UC1hZqFpujeJ6eq0uEwzQwdmedxqlZ4neimLzPUs5iFoLrHhT4o-fe-FjMNLvSbrbiLlYhPt6cI0cyP2ZOs16OkJUiI8tiZpN0Z7tity6Ax4a4Ha4E-gS-zeoSN_OYOD9lLbpVS7Ts8TviE2lr7tNg9SbPGM-YA3owE_NNJcrXguREOrTvmMgY4O1iwOb8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44e336ac3a.mp4?token=ectkXx6USHIRvioXzdHpbIg2G5WzS3sQuce2h9tf0zxlfufkVLfBCgw6GBmOUUwDzfdurEwIU0IASujUHt2ZoPjHV63humjYUVOf-JHzqvZqPibYdtimtNmTSpZcAVwNdzhTsDx9xYLOV8dTprWivn5UC1hZqFpujeJ6eq0uEwzQwdmedxqlZ4neimLzPUs5iFoLrHhT4o-fe-FjMNLvSbrbiLlYhPt6cI0cyP2ZOs16OkJUiI8tiZpN0Z7tity6Ax4a4Ha4E-gS-zeoSN_OYOD9lLbpVS7Ts8TviE2lr7tNg9SbPGM-YA3owE_NNJcrXguREOrTvmMgY4O1iwOb8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زنده از کربلا/بیرون کردن شش امامی‌ها توسط دوازده امامی‌ها(اکثرا عرزشیا)
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/129862" target="_blank">📅 15:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129861">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFyBMY7s4kj1ZNnuVjb1eWmvaAl5CkStrAWpAhNMxZrdQty2A2qkxElt7yxxgB9xqEqJ3k4X5IUvCJ_e5btvrYQIynqfDMEDHfvzXa56wR0pc1zvsLAuS1vIpJDwOF73rl8cx7xNNF1InTFK3U8nfm8T67xWBsPxgY1SiUG_Qvo2CEnMRllIDO6dHeXPxz3KMG3l1wYCjEkSI1TKnMiq7WpVFdMM0BVfChwhg9tidjJrbKlyiXIo4EcLrhWdZ5qAC_SvjuBoKOB1_S_fqClEI8NpMcwN5Zx2tQeh5XTpG0gMe7HQubQztRkhLTYo1PajuPRVRG5fgiiINAE-Q-dJng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: با وجود اعتراضات آنها و اظهارات نادرست درباره‌ی خلاف آن، همراه با تبلیغات گسترده اخبار جعلی که تمام تلاش خود را می‌کنند تا پیروزی آمریکا را هرچه کوچک‌تر و بی‌اهمیت‌تر نشان دهند، ایران کاملاً و به طور کامل با بالاترین سطح بازرسی‌های هسته‌ای برای سال‌های طولانی آینده (بی‌نهایت!!!) موافقت کرده است. این امر «صداقت هسته‌ای» را تضمین خواهد کرد.
🔴
اگر آنها با این موضوع موافقت نمی‌کردند، هیچ مذاکره‌ی بیشتری صورت نمی‌گرفت! بر اساس این و دیگر امتیازات بزرگ که ایران داده است، من موافقت کردم که تنگه هرمز باز بماند، بدون هیچ محاصره دریایی بیشتر.
🔴
با این حال، همه کشتی‌ها در محل باقی می‌مانند در صورت نیاز به بازگرداندن محاصره، که در حال حاضر بسیار بعید به نظر می‌رسد. پول و/یا تحریم‌هایی که خزانه‌داری آمریکا آزاد می‌کند، به صورت سپرده مشروط تحت کنترل آمریکا قرار می‌گیرد و برای خرید مواد غذایی و کالاهای پزشکی، منحصراً از ایالات متحده، از جمله ذرت، گندم و سویا از کشاورزان بزرگ آمریکایی ما استفاده خواهد شد.
🔴
این‌ها چیزهایی هستند که ایران به شدت به آنها نیاز دارد. این یک بحران انسانی است و من ضروری می‌دانم که اکنون کمک کنیم، قبل از اینکه خیلی دیر شود. مذاکرات خوب پیش می‌رود!
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/129861" target="_blank">📅 15:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129860">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
ناآرامی در حرم امام حسین
🔴
بیرون کردن شش امامی‌ها از حرم توسط دوازده امامی‌های ایرانی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/129860" target="_blank">📅 14:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129859">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
شهباز شریف: توافق ایران و آمریکا یک تحول خوشایند است
🔴
نخست‌وزیر پاکستان: پیشرفت مثبت بین دو طرف، نه تنها برای خاورمیانه، بلکه در سطح بین‌المللی نیز یک تحول خوشایند است.
🔴
توافق ایران و آمریکا گامی مهم در جهت تقویت امنیت و ثبات در منطقه است.
🔴
مذاکرات همچنین شامل دارایی‌های هسته‌ای، موشک‌های بالستیک و دارایی‌های مسدود شده ایران خواهد بود.
🔴
ما کاملا امیدواریم که این تفاهم‌نامه طی ۶۰ روز آینده به یک توافق بلندمدت تبدیل شود و منجر به صلح در جهان شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/129859" target="_blank">📅 14:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129858">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0051256b1.mp4?token=jyBBkP0u4lhG4o97AmaY828dQdVIudJXkAHvKwuDRC_E15lGwQRKgsFQJk7SYQCWhuMngnku9PU39FZh35EeaArea6HpTWbn3uYwg2Ut5K6up2AdeTPrL_yw3WWArtkCUMvRPr7JESx2pYE6WNW9l6RNx34hNIOEoQXLOPXFOCebTMes7TvlxbgkQhfvpFDvS0UTnutLJ1uRKZc6rxTlOKJIJ1U7JLuibT4vzs3_mbEnVAfMZpU38mxuGRnxuUE9TSXl2T3MVsA0NcQGOmIS1UUA2ZeLwqwNIdXkSUCw84f3vySpKpF5do77PJno7uBsO6ppOrweugTbVzf-bK-AYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0051256b1.mp4?token=jyBBkP0u4lhG4o97AmaY828dQdVIudJXkAHvKwuDRC_E15lGwQRKgsFQJk7SYQCWhuMngnku9PU39FZh35EeaArea6HpTWbn3uYwg2Ut5K6up2AdeTPrL_yw3WWArtkCUMvRPr7JESx2pYE6WNW9l6RNx34hNIOEoQXLOPXFOCebTMes7TvlxbgkQhfvpFDvS0UTnutLJ1uRKZc6rxTlOKJIJ1U7JLuibT4vzs3_mbEnVAfMZpU38mxuGRnxuUE9TSXl2T3MVsA0NcQGOmIS1UUA2ZeLwqwNIdXkSUCw84f3vySpKpF5do77PJno7uBsO6ppOrweugTbVzf-bK-AYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سیل هجوم ملت به شمال
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/129858" target="_blank">📅 14:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129857">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
کل کل شش امامی‌ها و دوازده امامی‌ها به صحن حرم امام حسین کشیده شد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/129857" target="_blank">📅 14:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129856">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53c18f2de.mp4?token=X5dgygxfvJmT4g70RgZvggt7j8w_e2H-So0A7XCPIi6tLyd6hjRrmOi6kW8YEj09v34n0I2BsKlzAY_mXpkS9ftLqGie6lzUVpopPdG-YqgPVcWvLfrOVMqtXhwjmQn5xc_H0XX-UyVNM3YyqJunmpjfYp6cVgTJ7bOyN0jskM3gANRBy2NMHnO0qHWQ6SsQE3TxZDVeV_MxwPyj3AWMrGW-Xf9D05O1OdktosuxdFosg7WORDqrYIQh8zSVES9sqJD7fFzkwIdoCnl4idJpMc3eYrSfEK-N5SX8EYnpKITYbygJU0Na9jFFjteZ3zsGb7OaB1_RzXF5zf4FoqkSqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53c18f2de.mp4?token=X5dgygxfvJmT4g70RgZvggt7j8w_e2H-So0A7XCPIi6tLyd6hjRrmOi6kW8YEj09v34n0I2BsKlzAY_mXpkS9ftLqGie6lzUVpopPdG-YqgPVcWvLfrOVMqtXhwjmQn5xc_H0XX-UyVNM3YyqJunmpjfYp6cVgTJ7bOyN0jskM3gANRBy2NMHnO0qHWQ6SsQE3TxZDVeV_MxwPyj3AWMrGW-Xf9D05O1OdktosuxdFosg7WORDqrYIQh8zSVES9sqJD7fFzkwIdoCnl4idJpMc3eYrSfEK-N5SX8EYnpKITYbygJU0Na9jFFjteZ3zsGb7OaB1_RzXF5zf4FoqkSqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کل کل شش امامی‌ها و دوازده امامی‌ها به صحن حرم امام حسین کشیده شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/129856" target="_blank">📅 14:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129855">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69da8218d5.mp4?token=Mpu6wi-bVJ_7Hx3Fvc8h39hCXMgxnbzE-ZCjSpNmtYZEpPT1EcWU099wT9UocfB1dDTztgI3-Ar5eVAq_Zv2tylg4Kv3kwezQQ6FGSTR4E8JEctJYiDDkyCrcH4iPn8M2rN6D-odewaUBhXt5nfBNg7F-py2HYZ-Tu1C58RbXGAnv6IjxtuIk0QGQRpShqxVmiyF1YkZJ5PthRumRIOv-ZdP5YromtRc93USUeCSyNO5yoR-nyjpZGb2fEkM7eOZDddVUkiH4Lz-cbU6x9Hgit9KzFswfBYDanTQ-1hF7z3cCgEckDEm8vrJ7y8htHsHswsLqRX5wrfLecmSzKWxVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69da8218d5.mp4?token=Mpu6wi-bVJ_7Hx3Fvc8h39hCXMgxnbzE-ZCjSpNmtYZEpPT1EcWU099wT9UocfB1dDTztgI3-Ar5eVAq_Zv2tylg4Kv3kwezQQ6FGSTR4E8JEctJYiDDkyCrcH4iPn8M2rN6D-odewaUBhXt5nfBNg7F-py2HYZ-Tu1C58RbXGAnv6IjxtuIk0QGQRpShqxVmiyF1YkZJ5PthRumRIOv-ZdP5YromtRc93USUeCSyNO5yoR-nyjpZGb2fEkM7eOZDddVUkiH4Lz-cbU6x9Hgit9KzFswfBYDanTQ-1hF7z3cCgEckDEm8vrJ7y8htHsHswsLqRX5wrfLecmSzKWxVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دعوای 6امامی‌ها و 12امامی‌ها در کربلا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/129855" target="_blank">📅 14:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129854">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
تعطیلی استان تهران در۱۳ و ۱۴ تیر؛ دوشنبه ۱۵ تیر کل کشور تعطیل شد
🔴
بر اساس تصویب دولت روز‌های شنبه و یکشنبه ۱۳ و ۱۴ تیر استان تهران و دوشنبه ۱۵ تیر کل کشور تعطیل است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/129854" target="_blank">📅 14:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129853">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f83b16848.mp4?token=RpIZIovCIUuDjx-RuCBnAdvYo1-6ihjLmMp-jXMsgWyVQfl_X5Rnk66_LAmebMT92eGA-6f69lkgl2-8eos4vAdbXQT-BO_t7M0Vl5Up3HlXsWm930m4g3APZDPA8tvDUeEmOYA0bactNiGtdo5zx7QXlVHW-uzoeIbPZ2RTXEHTZDSjy7v1Ae4ASKjggT69JLxcwyxo21EnYoxsGlyViOovcIo-66h2YKyOd-Oc1nwUao87AHZFFb6RJCpczHt0ziv5KPbDDv4LX1O9KYyqB4y7nHyHyCxOokMpRiuKjf28aAqKbqbhtyDaU3hRzFfNXzM2y720PxGYJ267caRHY1iSxkh-pFk1C1xBp_AdmKT_W1dyJIYwAaWahQd9ekiAuzQxAYUIpJetClG_NX-WfrST7iUsDgbaZsQWTZCIA0sGCDbEoAx0GY2INIZb0dpjl9iu5ugeeBf4Qqo2CnSrT2lNQsccmeGoIv25ILpWyV7NZNPYiXvkoArXpDTqhTqtSzC9i9ifaXysXe2ExrzHlDBZhBY_wUEXE29YLH_ju5WfNr9SzOV5ya0in-PO2YHXnlrY_Tp4MH-LIENyIfM-nc2QA25AjEJW5mw5OfAlDPocJ-Ewd2CVo9MxUoyUk2l39Lg5P1GEV9T6r4j7LCU43vUxmDzm6fHCKGAztuNa9KM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f83b16848.mp4?token=RpIZIovCIUuDjx-RuCBnAdvYo1-6ihjLmMp-jXMsgWyVQfl_X5Rnk66_LAmebMT92eGA-6f69lkgl2-8eos4vAdbXQT-BO_t7M0Vl5Up3HlXsWm930m4g3APZDPA8tvDUeEmOYA0bactNiGtdo5zx7QXlVHW-uzoeIbPZ2RTXEHTZDSjy7v1Ae4ASKjggT69JLxcwyxo21EnYoxsGlyViOovcIo-66h2YKyOd-Oc1nwUao87AHZFFb6RJCpczHt0ziv5KPbDDv4LX1O9KYyqB4y7nHyHyCxOokMpRiuKjf28aAqKbqbhtyDaU3hRzFfNXzM2y720PxGYJ267caRHY1iSxkh-pFk1C1xBp_AdmKT_W1dyJIYwAaWahQd9ekiAuzQxAYUIpJetClG_NX-WfrST7iUsDgbaZsQWTZCIA0sGCDbEoAx0GY2INIZb0dpjl9iu5ugeeBf4Qqo2CnSrT2lNQsccmeGoIv25ILpWyV7NZNPYiXvkoArXpDTqhTqtSzC9i9ifaXysXe2ExrzHlDBZhBY_wUEXE29YLH_ju5WfNr9SzOV5ya0in-PO2YHXnlrY_Tp4MH-LIENyIfM-nc2QA25AjEJW5mw5OfAlDPocJ-Ewd2CVo9MxUoyUk2l39Lg5P1GEV9T6r4j7LCU43vUxmDzm6fHCKGAztuNa9KM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیدار عراقچی با رئیس جمهور و نخست وزیر پاکستان ساعاتی قبل از ورود پزشکیان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/129853" target="_blank">📅 14:13 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129852">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
اختلال گسترده در شبکه بانکی کشور
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/129852" target="_blank">📅 13:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129851">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
نتانیاهو: ما ضربات سنگینی به جمهوری اسلامی و حزب الله وارد کردیم ولی پروسه ما هنوز تمام نشده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/129851" target="_blank">📅 13:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129850">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
شهباز شریف نخست وزیر پاکستان تصریح کرد پیشرفت مثبت در مذاکرات بین دو طرف نه تنها در سطح خاورمیانه، بلکه در سطح بین‌المللی نیز یک تحول خوشایند است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/129850" target="_blank">📅 13:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129849">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
منابع العربیه: عباس عراقچی، وزیر خارجه ایران گفت‌وگوهای جداگانه‌ای با مقامات پاکستانی انجام خواهد داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/129849" target="_blank">📅 13:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129848">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
نماینده دائمی ایران در سازمان ملل: تنگه هرمز باز است و هیچ‌گونه عوارضی برای عبور از آن دریافت نمی‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/129848" target="_blank">📅 13:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129847">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
نتانیاهو: حمایت دوستان آمریکایی‌مان را بسیار ارج می‌نهم، اما نیازمند رهایی از وابستگی و ساخت یک نظام تسلیحاتی مستقل هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/129847" target="_blank">📅 12:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129846">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
سخنگوی هیئت مذکره کننده:
آنچه در مذاکرات به دست آمده، تنها بخشی از حقوق تضییع‌شده ایران است
🔴
لغو محاصره دریایی به معنای اعطای امتیاز به ایران نیست، بلکه به معنای بازگرداندن حقوقی است که پیش‌تر از ایران سلب شده بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/129846" target="_blank">📅 12:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129845">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ba9HECCh-VqczHYWsKXMNItyjv3BNW807w7Qv1JjbYSG9TeRRu_UdnH-4e7uwTFx89XDWvjsYxRVXSeGYwmEm_Q2w01d7QPlotWp7Z-WuSRDiAA0i03x_8keXQFWEhIyN19Oet6i4DFXTd46ROvMN_98VGpHIb-EZL-7iEF0xbUmyMnqYM5Hh2H22I_wLSjtJwNO32uBKvzp5P9nXTj8AST7NeKSBn9SqvkZEg5teWlv6z1BxPayyI1qJIG-rFVKzd5CQ_TIRysZk-qnALV6tQ60lgWoEVgFsy1aHC7z0CkpEN3DWGcBWZGEKESzYGyKg1vqyQWmXxv1VQqj6Zv7Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت نیروگاه برق کرچ روسیه که امروز مورد حمله اوکراین قرار گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/129845" target="_blank">📅 12:41 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129844">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vn3kHHJcmP6zz4EMUmOZ6-2n-wUV3xlt8_yi2MTeSwapa6DgNKTdfG-uFJzmh0RgLRuAOl9_rF7s_9HxxUL5PIdzrxG8WUIk2Rn1BoXd62gYn7BzNndaTdR_uq0CQi-FU9XVoYWsMT7Ko_QAQ6TJnpKsRRyhQhsdVfL3UX5RKleON2QUpv1Zeq_seTyohgD7MhOcMYTefxIS8Vy8u75iYGjgCBbn2dJhsHdBHaz4ATkS31fQZrBBTrmhr6UBxf62vTxRW4n-mrfZYyTpXXCl5s1Ttg_vZFWBgtaHr0lLJZPMZmSgoKEVch_EQo8lRk2c00gGCN8u3flnrEZfJtkjAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
المیادین: عراقچی یکشنبه به بغداد سفر می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/129844" target="_blank">📅 12:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129843">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4VxpbWwdK1cCf6KJc2SVmQ6aILcilK79AYqoTLRdyjauXE3Kr8UNPzsnbmDgAdQZScssRCY_w_uik1bDNOFBeV9uTm6bVdxxgWPtLw2NLEqKMiNYW9ES4gw2vew2X7tSMROfYfCfH-R8y3O26jwbEjU25a8WN_2Ruv9Ftw5rTdjc0eASJbYV3ursRA114MD0hU_Sf6lj9pfR7TqhK3ATyz1lvwAeBzKQcZGmZ5xgUgS-usqqVhsnxhvoAB15HcT81ZrtePHXHyDIHpeX0E94C7lH3-qnsLbdEao0GpzTibiM6-cBRf_cBsNcAslvy0cf6pC6GS76015giMyvd1OwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات ارتش اسرائیل به کفر تبنیت جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/129843" target="_blank">📅 12:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129842">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
رادیو ارتش اسرائیل: تا زمانی که حزب‌الله کاملاً منحل نشود، از منطقه الشقیف در لبنان عقب‌نشینی نمی‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/129842" target="_blank">📅 12:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129841">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: جلسه چهارجانبه با حضور ایران، آمریکا و دو میانجی حدود یک ساعت و نیم ادامه پیدا کرد؛ قرار بر این شد که پس از یک وقفه کوتاه نیم‌ساعته، جلسه ادامه پیدا کند
🔴
نشست چهارجانبه پس از تهدید ترامپ تشکیل نشد و بحثی که ادامه یافت، تبادل پیام از طریق میانجی‌ها بود
🔴
پس از تصمیم به توقف مذاکرات، هیچ تماس مستقیمی با طرف آمریکایی نداشتیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/129841" target="_blank">📅 12:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129840">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: دربارهٔ اموال آزادشدهٔ ایران هر طور صلاح بدانیم تصمیم می‌گیریم و هیچ محدودیتی دراین‌باره وجود ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/129840" target="_blank">📅 12:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129834">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sc0rn_BOyNNLojS4xckMr_A4jRplsgMpJYyRm8xipD-ASRth6mAaWzDn_wCwhrvr-I_fL-s3ceMoyS1kUehN_7BwvfIhTD82jdHXDJXiqlthwI5IjqErS57fbrlzcHxr-ZHsGFHgrv72JgU8BF5VzKQ3_KBiWZlxSx83D-7BhaHUspxVf6jWtkXtE_e9PWBxkSEKMIKRDkgVtzABAPkylhm5R0yiktvI5jsk-n-tEb0ihJQHdjb2_9e9Hjv99vh33cnjIN5h4y5AON_9tjDbYOhpPIQyr1tajXtoSqMSO4aerFrWzALRrgyqo9MZRjBb8rydaveG3usN4Lv-2aAkoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F4YF2uCUXRsvWLwe3OZSrwandbYQxFso-aADpVIArTNRRkouj_LSG3uEmZcmRu54KG2fPpj3znfOyj2uWLK08uPnclXQqlpJdu7eMRFvtb2RLpyL8H32xuODwVhJo7uK6v5DyRIsU9Gq1BjJjErcDJ6RQuegfUtgyTBs_mmyn1nnHKRyphUHkD-Wa4_HNvqo4hxrbvjXpOaM6uSJmVjPxO7qCgQRmkQC_CChXfDa7w2hUdrDWncC5T_s0D9_DUCs3b5mIreX3UTqDA0JAh7jGjzLcNJfIumh1mugCj7FdgUVw1-L18lkQsd-DT8TzxUizM3np4U3fxLbWZJ_L4FByw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ONBFtNWOzrnLmy1pW2AWivFgcX6Bma_A0tSYC05HQfC2Zvfzf-omEPDYhjlb8y-BRe1jOFsSYAljqLtrFBJnykydmJBs4sEpt0c2n6WQGWMIn_ufnxv3CujNR_re0NWUYea6F3pPUfM6IXWIO-_XjHVfjlb0DHN86Uj0ToaoDkkqjU18qNHpjjFJbbj1kQTdLSkV5Td850xsSY_ZzCoVqa3_4avW2Auxl-0qVGcT2nAP1fCITwF-ngvN2vxgLwJf0Ss6kRIG2fjTY4PJF0fwBa4CBIXVQ8b1s6HNwLLIZqa06HiB7IdLlPpKdHBm-5-BKC7Yw9aiZ8Y5tl8DyOw59Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KEZon6bCoKEIvCqu0_-S2h5gpJSd8SkwmMmzLkR_P33TyWhDwcmMVLXvVWpDZ56f5mwvsyxdrY-5Nc6WacSPj3ww9SP37UJpNfjAof5MHJ_reuqXN3SiNZL5WJtVwamQGHZtwH1PQWxuEEbjejp8ao9v--SmmrE77_fM9XyOSLc73J7sQ50-cu8sQALxl5RYMxhUAuX643kHxubvXxEjxQ7qWsv2WyM6auE7hvvC5FPvORzABJx7pf36iZNlzLfHTx5Lu_WUW5x_4lT6hbUIgcTsLOraiyAOKM7BCv-1WXPQB8rfvePrvwsRabFLQZ-nnnYa8DMw0XzAVjbF6qGfOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R3k4MX2sDCyGAirZ1tIxA0YWTjlkPln7_JjPAAdegSpH5ay1s-uWPfxqO28jfhKt-Uy0M_5vEm94j_uTtDi4Xy8CQ0Z5LATYAy7kuTazHkNSWRhLQcYYDu2e_1fsUS0tO6PiTmGXz7HY4CCRuNIahuQprNM_UJfvHabmweQX6OcGaOjNi6KeB2FYNv3leR3mA0gPrXjsF9aKPV-9oJXuCzaOrfBgg4e_uQGIoXxYFK694KkjREhZ95Weq5nYcAITZzD67qQu-lSDwU60iQdOJgYls4WN0akQkXIo9m3h11otswf0e1LJ_SQybb_3QHCGCvSvkLm0HA2oWwWlTTiwwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uTdOcn5MFOmIFiDXrJHMe0m0O0CM4nYTuUvYAyhcYHVCkGZrmwcO6yz8pvLWqyaMprzH9jglCawOxpEBMgfsCla49KpzR0xBZ5S9efFxhz0bd8if5RJXWcnRBAPWyHvQMb2T9Bw2xXE1Y2m-7WzUZrQy1kOsOO2ZhSFCLCB5s37j3Wy-zIoghoO2DRunvCyVuB-3ZvdYQ4WVxhbu5d09aUbBB37RaPMZxwkgHUc3a8546oXy8aczHyTRFZjq8tuxXmaiVDKk8P7QB9v7N2NpYfMufC1aGo5ShqG5BfCRJdd1jeoxNpBVL5zWQIRid1I1gZff6l1PztTH4omNjnSa6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویری از دیدار و رایزنی  قالیباف و هیئت همراه با سلطان عمان در مسقط با دستور کار ترتیبات مدیریت تنگه هرمز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/129834" target="_blank">📅 11:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129833">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a802fb01d.mp4?token=HbKPI0OgATmf2ISRVzDOxIGVYs1oq-PeJcyJ4JvSlb-TVEdiiZ8ZLS2Xv1gfDm2tWfwQaJJltJYjjeOwDBLc6yu06rDR-nV1bqmwrybzX7-Qiggl_okG-qPijY5m55aoGskaWZEhdZEXiDOOipuy0PcPLVTxWvJrhkIJZIsd2SB9zvGyJYEfLQVrCls7JKoZBPYTTLUJD0viwnJ2IjLfY9E0QoaMsQKTMFffnU0HSYhfPLe5OfzKUj5Pz2Bw1kHLQs7fxd5ejwrATvQg_LphzzLpvJBvEWkUlsUNrcRZN1x4rzhqbc0-XJ2P3Ymn5NZvhrb9-RvraC1I2zrRC1BULQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a802fb01d.mp4?token=HbKPI0OgATmf2ISRVzDOxIGVYs1oq-PeJcyJ4JvSlb-TVEdiiZ8ZLS2Xv1gfDm2tWfwQaJJltJYjjeOwDBLc6yu06rDR-nV1bqmwrybzX7-Qiggl_okG-qPijY5m55aoGskaWZEhdZEXiDOOipuy0PcPLVTxWvJrhkIJZIsd2SB9zvGyJYEfLQVrCls7JKoZBPYTTLUJD0viwnJ2IjLfY9E0QoaMsQKTMFffnU0HSYhfPLe5OfzKUj5Pz2Bw1kHLQs7fxd5ejwrATvQg_LphzzLpvJBvEWkUlsUNrcRZN1x4rzhqbc0-XJ2P3Ymn5NZvhrb9-RvraC1I2zrRC1BULQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی: تا ۳۰ روز پس از توافق نهایی، نیروهای نظامی آمریکا باید از منطقه پیرامونی ایران خارج شوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/129833" target="_blank">📅 11:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129832">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18a1a4f110.mp4?token=mS0bK1ZbH2ftn6JJgXKjl4Y3d8mTNZLd2OqfE3cyOBjR2X5VqJ1uu4g-9AMYo8l78_q2h0oPO5l7Dz2N5f3mqNMPSqvnut39yStdSsD_NbOVCavaEdbv-IeRLfP0W_f3QgZZd4ha_j4HbQg-xEhfc-sL50EPGynFBKKOQoTAPB0VLFppRFz6Z41dBfGFs59ZpGUnUYO8hVJ3eyUPYv3zYjzKKYKp1w_SLJrbVIcA90LN2ZZw5rspJKnUimUyQ0o3MlIWMoGeGOCH8_-lFBqA_G1vgq6a8_tLQ92W1Fxpz_FGGShcnh5x9G58-Hs82yIcJtLFP2LBCD0AqLUDUqwJLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18a1a4f110.mp4?token=mS0bK1ZbH2ftn6JJgXKjl4Y3d8mTNZLd2OqfE3cyOBjR2X5VqJ1uu4g-9AMYo8l78_q2h0oPO5l7Dz2N5f3mqNMPSqvnut39yStdSsD_NbOVCavaEdbv-IeRLfP0W_f3QgZZd4ha_j4HbQg-xEhfc-sL50EPGynFBKKOQoTAPB0VLFppRFz6Z41dBfGFs59ZpGUnUYO8hVJ3eyUPYv3zYjzKKYKp1w_SLJrbVIcA90LN2ZZw5rspJKnUimUyQ0o3MlIWMoGeGOCH8_-lFBqA_G1vgq6a8_tLQ92W1Fxpz_FGGShcnh5x9G58-Hs82yIcJtLFP2LBCD0AqLUDUqwJLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی: ما در توافق با آمریکا امتیازی دریافت نکردیم؛ تا الان صرفا بخشی از حقوق تضییع شده ایران را پس گرفتیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/129832" target="_blank">📅 11:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129831">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b58a20450c.mp4?token=lgvigIb0XsxNprgTyldhGV2O_VlkUXMMtvwXT_os04ZckZUNpfJaCd4cPdzD7Ko5y4t296dOZK19suMV12RRjaHu4ZmoGdabcTzN47-0nd5Q2G7Fv2KAHKQksgLekTK_7BVhzo5rSU6S_SbVVpbK2ARe0jfxJ7WQWITGZrGF3yzhBZHnLFZK_Ra_LtC89PjJ4k9aIb2FN5KfCfcmMbLZJSmZczn0JtT8-6XrdtYzPSvRkfQ-WB4W8vcFtTX0Gbhr-xdqFKkolpTjUOpOrC_qNIG_31Ag_EtthquDBOWWRFty4hmnfI6MTCgZnm0iDv_4WSk2ZbmpC3mzdl-pl-9DxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b58a20450c.mp4?token=lgvigIb0XsxNprgTyldhGV2O_VlkUXMMtvwXT_os04ZckZUNpfJaCd4cPdzD7Ko5y4t296dOZK19suMV12RRjaHu4ZmoGdabcTzN47-0nd5Q2G7Fv2KAHKQksgLekTK_7BVhzo5rSU6S_SbVVpbK2ARe0jfxJ7WQWITGZrGF3yzhBZHnLFZK_Ra_LtC89PjJ4k9aIb2FN5KfCfcmMbLZJSmZczn0JtT8-6XrdtYzPSvRkfQ-WB4W8vcFtTX0Gbhr-xdqFKkolpTjUOpOrC_qNIG_31Ag_EtthquDBOWWRFty4hmnfI6MTCgZnm0iDv_4WSk2ZbmpC3mzdl-pl-9DxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی : قالیباف به چین میرود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/129831" target="_blank">📅 11:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129830">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fec08cc90a.mp4?token=U4BgPv7I36fJe_0vEmjIAiVp3YnWXezHSXvLmmSUWAAH8mKL7mVC_0U37UjwRGf7XyJjIanpdiKdxtnXo3aHIc29MRW1Cmi-_U5ku78dw-ybbXKEiKhq9Kuifr_-SnGpYGEM0I4YaOnz35J5IO8DT1KcsRz3HZq-zclC5xeG4scHfZ8WzSMncjVoeqSnzdFxmBdQ8s3jl_44DVQ69T9czPgb7tiz0TLy-1dNQdoGiCMfe8lW1-eqpwIqXffZVx62NG-lx95VOY8BGf3t854JvTYAC6ZlncMS87CIouk2ZzuKSvBYqLxkXhk6BlPomcpXxrJ5xDGaWps8APgebXJuow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fec08cc90a.mp4?token=U4BgPv7I36fJe_0vEmjIAiVp3YnWXezHSXvLmmSUWAAH8mKL7mVC_0U37UjwRGf7XyJjIanpdiKdxtnXo3aHIc29MRW1Cmi-_U5ku78dw-ybbXKEiKhq9Kuifr_-SnGpYGEM0I4YaOnz35J5IO8DT1KcsRz3HZq-zclC5xeG4scHfZ8WzSMncjVoeqSnzdFxmBdQ8s3jl_44DVQ69T9czPgb7tiz0TLy-1dNQdoGiCMfe8lW1-eqpwIqXffZVx62NG-lx95VOY8BGf3t854JvTYAC6ZlncMS87CIouk2ZzuKSvBYqLxkXhk6BlPomcpXxrJ5xDGaWps8APgebXJuow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: مجوز فروش نفت و محصولات پتروشیمی دیروز صادر شد و از همان زمان قابلیت اجرا دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/129830" target="_blank">📅 11:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129829">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9061886b7c.mp4?token=tl0zx4hFvlTFR_SP5q5UTSaab3M6YGQy4Ej2zCd4AsZTNp5DdOGsVCdFLdkFSWwK1CaaWkVjwal_gDD_BeBUevw9sa179C6qsag5FFx7wrJ63EMg7a0Qs3xvNq0ymvTbXCAo_i44Pg4cSrR_YV0IeTnmm30gF2fB6P4Q_7N2OOYgv7eFr-jRyeCaPU2TEEayKRbW-nfiLa_G9KtYkwQQr_u4sngetnyMZSO5EWZ1BoyzQXMJ5On9TJ78qyRBLUzJl0MXd99ZiAAJX3f9ct5ISoIydHoCD9F6XaaqzCcZwIG2NZ7SC6u8vhau0f_BZDckL8g4lU0ASKZ6_G5F7XgIKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9061886b7c.mp4?token=tl0zx4hFvlTFR_SP5q5UTSaab3M6YGQy4Ej2zCd4AsZTNp5DdOGsVCdFLdkFSWwK1CaaWkVjwal_gDD_BeBUevw9sa179C6qsag5FFx7wrJ63EMg7a0Qs3xvNq0ymvTbXCAo_i44Pg4cSrR_YV0IeTnmm30gF2fB6P4Q_7N2OOYgv7eFr-jRyeCaPU2TEEayKRbW-nfiLa_G9KtYkwQQr_u4sngetnyMZSO5EWZ1BoyzQXMJ5On9TJ78qyRBLUzJl0MXd99ZiAAJX3f9ct5ISoIydHoCD9F6XaaqzCcZwIG2NZ7SC6u8vhau0f_BZDckL8g4lU0ASKZ6_G5F7XgIKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی: طرف ما بر اساس یادداشت تفاهم ۲۸ خرداد دولت آمریکا است/ تعهد ما مبتنی بر تعهد طرف مقابل است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/129829" target="_blank">📅 11:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129828">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5565eeff1.mp4?token=JHnqE-bNyn9vvIOJzIXMuAQJE_7CkHky-lt1r0I4iiVQlWDakinF14Q__fpvwgf80-Nao5nlHbe-hoW_4DREBB52sz49jBLUcc4A4wi2QBGHT9tUMQU8qEY35rYt3mv57_dys7EnVIvvVitOjfazncuAKwSUkAcpSu3lso9pPSSonBewM_fj7BkJORvfwFxzEOmBu3Dy5nswQ2bCgZOmG1YmmZhR7wyaq8W-ZK_Gw4bIdzMgO9gWMYf2s7cOeukg6uIJwPmED2R6UmjYork99_FMp1rPI6Uz8Az3IfPDpZVs6UJoeCC4tKv4rFOaXTR4fsZH072Jvt5JsuZleCh0Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5565eeff1.mp4?token=JHnqE-bNyn9vvIOJzIXMuAQJE_7CkHky-lt1r0I4iiVQlWDakinF14Q__fpvwgf80-Nao5nlHbe-hoW_4DREBB52sz49jBLUcc4A4wi2QBGHT9tUMQU8qEY35rYt3mv57_dys7EnVIvvVitOjfazncuAKwSUkAcpSu3lso9pPSSonBewM_fj7BkJORvfwFxzEOmBu3Dy5nswQ2bCgZOmG1YmmZhR7wyaq8W-ZK_Gw4bIdzMgO9gWMYf2s7cOeukg6uIJwPmED2R6UmjYork99_FMp1rPI6Uz8Az3IfPDpZVs6UJoeCC4tKv4rFOaXTR4fsZH072Jvt5JsuZleCh0Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
توضیحات بقایی درباره خروج خبرنگاران از سالن اجلاس چهارجانبه: ما برای کار رسانه‌ای و تبلیغاتی به سوئیس نرفته بودیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/129828" target="_blank">📅 11:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129827">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
مایک والتز، سفیر آمریکا در سازمان ملل:
جمهوری اسلامی با بازگشت بازرسان هسته‌ای به ایران موافقت کرده و این اولین گام برای توافقی گسترده‌تره.
🔴
برخلاف برجام، این بار بازرسی‌ها باید در هر زمان و هر مکان ممکن باشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/129827" target="_blank">📅 11:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129826">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60eb3a2c96.mp4?token=X0KdLSdztyh2AwKnL6VDSI01kNHEurRb5zxC_Of4leUot36BLMci0AOy3ukz-99oaS-hXMPvSTf61YHJAnmd3MPdzmAwNk38FwVtKW8GxwymTYxC2nKEAjvsV6ApgugBvgO-srs1Dh1KEL24Wpuy-UAGuhJqWeeZhJ5KTiB8SBRlaB59SvwYPFLOTxGDiHldW9I6zCFZ-VW6kvXaWR8pIsXlYcP0qwll2xiRp23itg7xaotRZS9PJUVSGef7GPgeFzt5o8X90JceZ07YvxZp0CqI6Yu0CRbJmu7TTpH9OU3-eFleeGy8fRhSzKnsW1ldVcEG4UdUH5J1LIX8ZlPmgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60eb3a2c96.mp4?token=X0KdLSdztyh2AwKnL6VDSI01kNHEurRb5zxC_Of4leUot36BLMci0AOy3ukz-99oaS-hXMPvSTf61YHJAnmd3MPdzmAwNk38FwVtKW8GxwymTYxC2nKEAjvsV6ApgugBvgO-srs1Dh1KEL24Wpuy-UAGuhJqWeeZhJ5KTiB8SBRlaB59SvwYPFLOTxGDiHldW9I6zCFZ-VW6kvXaWR8pIsXlYcP0qwll2xiRp23itg7xaotRZS9PJUVSGef7GPgeFzt5o8X90JceZ07YvxZp0CqI6Yu0CRbJmu7TTpH9OU3-eFleeGy8fRhSzKnsW1ldVcEG4UdUH5J1LIX8ZlPmgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی: توانمندی دفاعی و موشکی ایران هیچگاه موضوع مذاکره با هیچ طرفی نخواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/129826" target="_blank">📅 11:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129825">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27922d07c6.mp4?token=W99GhJYuFDL67cudiZ43pRaGZEZrXiq4RlQEI7156lWyBNotNth0_2ShE50zWTm1FuGdDRqlLOLO3CkU3yOP0nzUd6xj0beTFEii_fXrxtww7bz7nfcfFaREGDUNWCub_q0yTEetf851vJYYpEIdraL6bbW05rxvIRtPB6zlZlxmcGkFWP5PNJLMviWwhSdgew_aWdqqczJyRxID_g_yQzxVSHvNSJpYCYteekcmFxU7DaejjM1XF1qrTeCRfMb6s9Mx_PiCfirPX4otm7Jz8Rz868cJOisUMb7qU1YDYhp4F-F9yJOvxsneBpVStq1vnAfZ66J1jCXvPjf9Dy1sJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27922d07c6.mp4?token=W99GhJYuFDL67cudiZ43pRaGZEZrXiq4RlQEI7156lWyBNotNth0_2ShE50zWTm1FuGdDRqlLOLO3CkU3yOP0nzUd6xj0beTFEii_fXrxtww7bz7nfcfFaREGDUNWCub_q0yTEetf851vJYYpEIdraL6bbW05rxvIRtPB6zlZlxmcGkFWP5PNJLMviWwhSdgew_aWdqqczJyRxID_g_yQzxVSHvNSJpYCYteekcmFxU7DaejjM1XF1qrTeCRfMb6s9Mx_PiCfirPX4otm7Jz8Rz868cJOisUMb7qU1YDYhp4F-F9yJOvxsneBpVStq1vnAfZ66J1jCXvPjf9Dy1sJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی: مجوز فروش نفت و محصولات پتروشیمی دیروز صادر شد و از همان زمان قابلیت اجرا دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/129825" target="_blank">📅 11:36 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129824">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: برای ما جالب است که فلسفه و هدف جنگ، که قبلاً اعلام کرده بودند از بین بردن تمدن و فروپاشی ایران است، تقلیل پیدا کرده به ثروتمندتر کردن کشاورزان آمریکایی.
🔴
ما در رابطه با اموال آزادشده ایران، هر طور که به صرفه و صلاح کشور باشد، تصمیم می‌گیریم. در رابطه با خرید کالا، وزارت کشاورزی ما و سایر بخش‌هایی که متولی امر هستند، هر آن‌طور که تشخیص بدهند، هم بر اساس قیمت و هم بر اساس کیفیت، تصمیم می‌گیرند. لذا هیچ محدودیتی در این رابطه وجود ندارد.
🔴
مجوزهایی که در رابطه با بحث فروش نفت صادر شد، از دیروز اجرایی شده است. سایر موارد هم مشخصاً در رابطه با هزینه‌کرد از دارایی‌های محدودشده یا مسدودشده ایران به همین ترتیب است.
🔴
آقای همتی دیروز توضیحات مفصلی در این رابطه داد. مهم این است که اموال مسدودشده ایران در دسترس است و برای استفاده آزادانه ایران، هر طور که تشخیص بدهد، برای تأمین کالاهایی که مدنظر کشور است، قابل استفاده خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/129824" target="_blank">📅 11:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129823">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
بر اساس مصوبه امروز شورای شهر تهران، مترو و اتوبوس‌های بی‌آرتی تا ۱۹ تیر رايگان می‌ماند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/129823" target="_blank">📅 11:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129822">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
الجزیره: «تغییری بزرگ» در سیاست آمریکا؛ ایران اکنون می‌تواند نفت خود را با قیمت کامل بفروشد
🔴
این اقدام صد‌ها میلیون دلار درآمد اضافی برای اقتصاد ایران به همراه خواهد داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/129822" target="_blank">📅 11:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129821">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d72b824858.mp4?token=f-CjY6gqBkMAnv6QQA0r0hvdlX1HiT_ZdpMAcD1RSiCtcHfv673clIRc0-sySI9YD1oVawIl4HZ25a8toCF4ApF6nHZ0Fjd06B5e5sj6W0T16K2-Hx5Ofa2YHvz47xr7_-P85fA7a9quCbwzE9Q1W6gTbWfBjaIb_cBFLgUx6II5w8GwaVfO4rIz67R-j3CytubCIi7Xqqa21Yh3edULMXExrABrKvofD_pg3Bk4LU7iVZXtJTNaSOE6ZwLvXkT8pmP_ekB-QC_d3v3-l8rmABpbnZLid587zZfaKzU2lcnzDkGQPK52e31njIwNrw3xZVZmSvVgrOiep588Dnk_Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d72b824858.mp4?token=f-CjY6gqBkMAnv6QQA0r0hvdlX1HiT_ZdpMAcD1RSiCtcHfv673clIRc0-sySI9YD1oVawIl4HZ25a8toCF4ApF6nHZ0Fjd06B5e5sj6W0T16K2-Hx5Ofa2YHvz47xr7_-P85fA7a9quCbwzE9Q1W6gTbWfBjaIb_cBFLgUx6II5w8GwaVfO4rIz67R-j3CytubCIi7Xqqa21Yh3edULMXExrABrKvofD_pg3Bk4LU7iVZXtJTNaSOE6ZwLvXkT8pmP_ekB-QC_d3v3-l8rmABpbnZLid587zZfaKzU2lcnzDkGQPK52e31njIwNrw3xZVZmSvVgrOiep588Dnk_Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی تکذیب کرد: نه دیداری با گروسی داشتیم و نه برنامه‌ای برای بازرسی آژانس از تاسیسات هسته‌ای آسیب‌دیده ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/129821" target="_blank">📅 11:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129820">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9MBclp_xAb_kk5FtAjzv5JDOLThg45QbB4xu-eT2o8G51yEJ1nizxtq2iyWsl11A5URKaPW_ZaMf2hBJqZW3QW4kuou82FenVWKpEq5u4-yXZJReY5TR1VSAyZXC1WLmkT0N9sl9PX2DayXbNltJhoSHZhr938fXQEya4X7O2gvOkogfV_OYLmYIR65Nm1dY-sP2yNiaLbh1SilNdzsuHOED0sFRms1hjszJPTarCALzrETTXHC-FhfJAgKdTiCyZEDMKr-U2FLYbZGYdLLYf2Jlw8m91h6FmvRXRNXQK6bhaFRrA6ZgJaEb7X_bsYB3wyALf3t9A7_9Cone7NC3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز:  روبیو با وظیفه سختی برای متقاعد کردن متحدان محتاط خلیج فارس در مورد بازگرداندن روابط با ایران روبرو است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/129820" target="_blank">📅 11:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129819">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
سازمان ملل: برای نخستین بار از مارس هیچ حمله هوایی در لبنان ثبت نشد
🔴
استفان دوجاریک، سخنگوی سازمان ملل، اعلام کرد که روز یکشنبه نخستین روز از زمان آغاز درگیری‌ها در دوم مارس بود که نیروهای حافظ صلح سازمان ملل در جنوب لبنان هیچ پرتابه یا رهگیری هوایی ثبت نکردند. او افزود که این وضعیت تا صبح دوشنبه نیز ادامه داشته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/129819" target="_blank">📅 11:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129818">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sXPP5_ab-ts5lUhpnDggMZZ6vORrceY8Q3PH9OJ6I_BuUxwux8KPOWrKsPllAlfiTTyCL6XSr0pOuriOL06Gd8sZs3edNwdzYrHqteYsIqTlDFdPVONSntHJRGAay87Sl3ncmisaeS2nZX2ZKQxoSoI3Rg84BHBWp7AegPx-opcimwjd2GiinFUtCLs09_RQeJBgl9lVdsZmv2PB9hGtsQ_kgevexYZmZ-rtmh6sVdY7_R8_xR02RnDCcFZhCtlDcarmooZ8G1OUrJM9xqLBgFg9-FjGReWoFAca1512nz8puvDfvhK0AcZ9aT6-QERGYRiCBELJGe01o6fPqIrF8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سلیمی، نماینده تهران: با توجه به تغییر شرایط، آن دلیل ابتدایی که موجب می‌شد صحن تعطیل باشد، دیگر منتفی شده و ان‌شاءالله به زودی شاهد بازگشایی صحن خواهیم بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/129818" target="_blank">📅 11:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129817">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpiqPZcp4KsQDYX4iI13ZQB99j9LIs2ktJJWNU8tV5SnPQIR6y2lSE8Gy9ocVGu4Ad_IPzN4tCVIFBj-OQqk7meO3OoGOO3nsJE0HfiAmjJkGc1zzRuv8H-2Q5TLegfoAe1wn_aZuIGp3-_pad6hJnfFtLK4LMkGNXTAWTUPK_YRPOKJmSHKszhhn1DatrlHuvapl1Y52ME5JcylCPWHnkwVyr3B6fCOcVa5H4xHshajVykHnyh3sC4opmxvS0CFCPszrXqvkIVVt1KspYMPT0VOnzv_192I4UZeKB17EWFSFmkId5e_KT6HGOte5mEwPNqp7Wrxkq90JnSnN3EbyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: اونا مردمشون رو گشنه نگه داشتن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/129817" target="_blank">📅 10:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129816">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
وزیر دفاع پاکستان: حصول توافق میان ایران و آمریکا ممکن است به پایانِ حیات سیاسی نتانیاهو و حتی بازداشت او منجر شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/alonews/129816" target="_blank">📅 10:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129815">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
پزشکیان عازم پاکستان شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/129815" target="_blank">📅 10:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129814">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EB9RRw9IVQEFFQsduGOCNlP3FxcS9QcKxL2cScXmXuEbp5Iyw9_h6dpo0gCZTUsDJeR9T59LuNXTspyxaV0k35Eo4oQWRTa_N21ZJMYXWRAjHjjCbF7SR_v8TXlLkCNhknq0kGc4srL90sruyBG0u0s9oucbdCViEiJEDN3D-CIDJRYo0CBA0RTc0uUTybgZ4jDMbnQrZ6DF05rq4oKnFhwwswjSE_Ief77Xno97meLzgwGltV3iI63O7j7uEI9IuHCmygG8xYRcOGkkxiuMx1OkaFgtW4DikKNWJAmy7lcrFP3FMqFzvfW2FUZ3wnrx1kzDK3o7EDU5SkQiBeIZYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زنگنه، نماینده مجلس:
یکشنبه آتی، صحن مجلس، کار خود را آغاز می کند/ احتمالا با موضوع بررسی روند اجرای تفاهم نامه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/alonews/129814" target="_blank">📅 10:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129813">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16290e355b.mp4?token=G5m_tu-BlhIs3C3FixoszW81IdejwxufeXT-mTWN77aKUv8VA35Y9JW2MiExl4MsG0Bv4UNtCs2-5Zi_z-0fyxep99kjADqC7N9hrWEOn2dJcLbdDy2lAXjRwI1eXRtYxknlswbyijQDh3IwrwGzNwGFhufGyYLN-AoY8CJP4WoT8OxRgtGq3zVEx9DDCZEL82Pr3mlHB9ip3p30Tr4fZWJOwrf1b3d0oJEpA3tt1nvxJ9sch7nQYH2xKgS6SjXpwicNvJVhgX-sLL_WOse3__AqcqM03YW6UkgmGHCVok459jR9aEiWJrnhH7cwZIh9YIu_Ms53_NJ10r4uQH2W6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16290e355b.mp4?token=G5m_tu-BlhIs3C3FixoszW81IdejwxufeXT-mTWN77aKUv8VA35Y9JW2MiExl4MsG0Bv4UNtCs2-5Zi_z-0fyxep99kjADqC7N9hrWEOn2dJcLbdDy2lAXjRwI1eXRtYxknlswbyijQDh3IwrwGzNwGFhufGyYLN-AoY8CJP4WoT8OxRgtGq3zVEx9DDCZEL82Pr3mlHB9ip3p30Tr4fZWJOwrf1b3d0oJEpA3tt1nvxJ9sch7nQYH2xKgS6SjXpwicNvJVhgX-sLL_WOse3__AqcqM03YW6UkgmGHCVok459jR9aEiWJrnhH7cwZIh9YIu_Ms53_NJ10r4uQH2W6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وقوع یک آتش‌سوزی در شهر هیوستون ایالت تگزاس آمریکا موجب برخاستن ستون‌های عظیم دود بر فراز این شهر شد
🔴
تا این لحظه جزئیات دقیقی درباره دلیل آغاز آتش‌سوزی، میزان خسارات احتمالی یا تلفات انسانی منتشر نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/129813" target="_blank">📅 10:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129812">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R681S-JmZv48xhBR_j6AMw_usULnuPv8yfJxwPrzGnyl9XNRVcFdQDJ4Yx3aPPo5834dAvo-GGy-cMolgCxCt-2XgnnChYyBdrsJkMs4tXdTU363-lCVknxQGHLZA-e4UkQchM-AWQ-5UNJNRErVXbV-nV7CMx9x3FC-50bF5teKvSHYeWhibUnuHmZPORcKLgXh3ayjY-xHi_5TxQeogjyr4IcPpdxvnhTUFYmsGNjH4ERIfIBszS9ySEiQ7-hBxvi0jhJpFs81NRDP0dXILss5G8cUXJDbhe2maXgQesfSEdEz19UwMy9iKoW8AAph_69TgkglffYnkIDd0t27tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مقامات بهداشتی کشور کنگو اعلام کردند با تشدید شیوع ویروس ابولا، شمار مرگ‌ومیر ناشی از این بیماری به 267 نفر افزایش یافته است.
🔴
تا کنون 1048 مورد ابتلای قطعی به این ویروس مرگبار در این کشور به ثبت رسیده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/129812" target="_blank">📅 10:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129811">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
روانشناس اسرائیلی ، اوری گلر روانشناس مطرح جهان به کانال 14 اسرائیل: ایران از سلاح الکترو مغناطیسی با فرکانس پایین برای شستشوی مغزی و تحت تأثیر قرار دادن ترامپ برای پذیرش تفاهم‌ نامه استفاده میکند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/129811" target="_blank">📅 10:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129810">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
کاخ سفید : به هئیت مذاکره کننده اعتماد کنید
🔴
آنها به مذاکرات ادامه خواهند داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/129810" target="_blank">📅 10:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129809">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
داده‌های کشتیرانی: طی 24 ساعت گذشته، دست‌کم 20 کشتی از تنگه هرمز عبور کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/alonews/129809" target="_blank">📅 09:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129808">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
مرکز ارزشیابی و تضمین کیفیت نظام آموزش و پرورش :بر این اساس، امتحانات نهایی پایه یازدهم از ۲۰ تیر ۱۴۰۵ و پایه دوازدهم از ۲۱ تیر ۱۴۰۵ طبق برنامه اعلام‌شده برگزار خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/alonews/129808" target="_blank">📅 09:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129807">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
نتانیاهو و وزیر دفاع، کاتس :
ارتش قراره همین‌طور ادامه بده تهدیدها رو خنثی کنه و تو منطقه امنیتی جنوب لُبنان بمونه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/alonews/129807" target="_blank">📅 09:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129805">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
ترامپ: خودروسازان آمریکایی تولید سلاح را آغاز خواهند کرد
🔴
رئیس جمهور آمریکا در کاخ سفید به خبرنگاران گفت: «آنها برنامه‌هایی برای تغییر کاربری کارخانه‌ها دارند. ما قصد داریم سلاح‌هایی از جمله موشک‌های پاتریوت، موشک‌های تاماهاک و موارد دیگر تولید کنیم.»
🔴
طبق گزارش‌های متعدد رسانه‌ای، درگیری با ایران زرادخانه‌های ایالات متحده را به طور قابل توجهی تخلیه کرده و خطر جنگ‌های جدید را ایجاد کرده است.
🔴
در ماه آوریل، کانال‌های تلویزیونی ایالات متحده ادعا کردند که تنها در هفت هفته، ایالات متحده تقریبا نیمی از ذخایر موشک‌های پاتریوت و حدود ۳۰ درصد از موشک‌های تاماهاک خود را استفاده کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/alonews/129805" target="_blank">📅 09:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129804">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d480841643.mp4?token=Nnw5ScSp2iZZYMstbtJwFeSLjdIL1usqNf-7S3FZNE6RScAtBhthyzLqMj1ygZ-nwVDcW26r4wRHvkLh3C42uFMDEXOCPsLXoUeVp_Y01Q8RP4bw4U8cOxbNciLri3zifG2qoDiyCexqcKkGMeZAHNdRFPohIxWx1NFFnfFWJooXc0AVudbfyIJ4lKZh07AYN3LwOiIDmoDXrXCmhWoSV1Ckw4otp4_XjAIyGcxnHpDNap9BLreIEnZB_9pzldrY4xM_HfBPZd_TGv7wSGLVbR7nhPzuHZt13AJlpYz750B2YHY2X8_wZUOzYsf4w5mISMR5XbTQGKQv0SXADXEj4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d480841643.mp4?token=Nnw5ScSp2iZZYMstbtJwFeSLjdIL1usqNf-7S3FZNE6RScAtBhthyzLqMj1ygZ-nwVDcW26r4wRHvkLh3C42uFMDEXOCPsLXoUeVp_Y01Q8RP4bw4U8cOxbNciLri3zifG2qoDiyCexqcKkGMeZAHNdRFPohIxWx1NFFnfFWJooXc0AVudbfyIJ4lKZh07AYN3LwOiIDmoDXrXCmhWoSV1Ckw4otp4_XjAIyGcxnHpDNap9BLreIEnZB_9pzldrY4xM_HfBPZd_TGv7wSGLVbR7nhPzuHZt13AJlpYz750B2YHY2X8_wZUOzYsf4w5mISMR5XbTQGKQv0SXADXEj4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک روحانی: اسم بچه‌هاتون رو امیر نزارید، ریشه این اسم بهایی هست
🔴
امیرها همه آدمای مشکل دار و ناجوری هستن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/129804" target="_blank">📅 08:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129803">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4BhoW5XZOkvesHiu0MOMujDhyKEtN1XI4qQc4DT0fkXpCligyN8BIzRaUTeuPJFeULRXnu_86GWRFKJmnCkSSMlI3sukLKB5T_k4CzwsRnAFU52lG2MiW2ueWJ-vqK0mwHJyjNh-P_WCc6hc_xistKprbTWSXb8hET0tin0Dtg2qA1W6rcznzu65ngtiEYvk2EQgFYCkxne_9LLKcGMRxNsgQnUHoMaAkjSzERUDj66DGOm8ZA3Hit8ITlXpD70AjGPI_dIxg8KKDYVqPRcxrZWjVyD2N2fohCAiet6ouLPxIxUnBtv4IkvLnQpdWliYjD2qNMSUNSLAxVqrTmYNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
غضنفروف نماینده مجلس: جمعی از نمایندگان یکشنبه به مجلس خواهند رفت؛ اگر در بسته بود همانجا تحصن می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/129803" target="_blank">📅 07:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129802">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZbSrQ1quUijeshaen7jH9B4Mw8YNGxSLhFkRjNOs5Evkw5wUfLA23sU3om-6kVZAbklTonn4ofGmS49j_qhrUbkdK-v4Djz_fMxIrW4RXJWQhE4O_MFkUejpKr-xY_fbXh-WhSbnVDtuXZeExAw7D-i2N50Yi76bhwrwYnqqI678pMcza_WrLmszjYCVT2UCO-6nwFmZEB7AtkGhCDoBYDoxxWCBGIlS-sJW7AIY8TkC98XUKHJf8lLkwE722t-sVsaRfUYeGZp79xichlhcXtzLblZAbvH38De0kDwG_aJDjNg_t_Ac3OdTBpDounsbavonIC-rwi2-G7LwFFhEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی: مفتی مفتی تنگه رو دادیم رفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/129802" target="_blank">📅 07:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129801">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبارفوری مذاکره | مذاکرات ایران امریکا</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldSRH4GLpseb7oaGxQR4l7vYAqPiloE-L3fr3t3rVj6rTqbt-cXlGBDpVMz8ph-qNjOxmfmpgH1bwm54SeD0yKcr-Ix2_GkBc778X-TtsY2hiy6k5F4pav06OXnwMBt3EQ_O-gXXofhEKcAXrAcb3Ih5q89WD5SiMO573kltMIzsWdyKio_ex-Py8270rMMebguYxtUXKrCrpTlKZ0baOr8AJR3t3Xnc_xFFGhFudbXm7y2M9IDFp06iThhzO6ihYPqjqwpEzvD94CX0tmjIaZu1h5gJp2CraylEorUkU05_TBjcMPtHKK34Q9bBJpCI_tgiQNCuCWyPZn7YsiC6tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
📈
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/alonews/129801" target="_blank">📅 01:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129800">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxU-TmEIw4VRdBgu5_UidhYnZA2vl_YXKqgfwwHcLEy_jquGacUGpAFS54aLuY_yIhJ7bTvQ7i3PLLNTBTW-MXxw4hM5VQH839z17C5RRg-ILrni37Ne2hbx3_9PzkLIrL3hraZStYwcOtJTh9w3liJklaqhecgnrhPOk4M_ZLJhAuUlotBzQGTqZc6Zt9dsj3imbleCFMYCsalJGNiLwmYQweqBQhLf4BOfNX2W34qIYX84hUclI1sMh3yfTG4pKBkxUHWd3KZWFANC59fYqYOXfRyzHWGY8ElYnd8noCYY2ifHQ8thDJ4aM-iN16LKXNR2r3gnYH4R0COuBtIqqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عماد الدین باقی: طبق بند 2 توافق ایران و آمریکا، از این به بعد شعار مرگ بر آمریکا یا سوزاندن پرچم این کشور و لگد کردنش تو مراسم‌ها و اجتماعات رسمی (مثل نماز جمعه) ممنوعه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/alonews/129800" target="_blank">📅 01:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129799">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
وزیر خارجه عمان: به قانون بین‌المللی و تضمین عبور امن و بدون اخذ عوارض از تنگه هرمز  پایبندیم. به مذاکره‌کنندگان ایرانی بر تعهد خود به قانون بین‌المللی در ارتباط با تنگه هرمز، تاکید کردیم. مذاکرات سازنده‌ای با قالیباف و عراقچی درباره یادداشت تفاهم انجام دادیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/129799" target="_blank">📅 01:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129798">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQmYSpOM7ADXZd5B6wH2X3rw-giRkShw84uuihGYMAFIkfaDSpVZj1N8hKQQtuWpfIJPUSUPbgD5brdTzLtCzVUqZeFeNlp273louEHHxfLWyh9_3vsbeZhV26y2jl5YUeR0iLcXlvVliYOt33X58hBz_xqr10YX5PL3_ahckB1WMfOpUix8INdtpGjKiTcBDyQF5ASFJRiI0zOlGQRiyiSIDELTdt4_RneW3TB0yNCgzBjc2KRSfSkV92ZcMy39ARSmS0yqK-0jbJHjj8fN7l-la-rFfpzO5pDkxFrM4SyUe8MBMUNSA2O3IHdmTW9S6zkBAM-6fu7lwzJHRWO0Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چند روز دیگه
✅
@AloNews</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/alonews/129798" target="_blank">📅 01:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129796">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
گویا علاوه بر سویا و گندم، قرار است سیب زمینی دشت مغان هم از آمریکا خریداری بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/129796" target="_blank">📅 00:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129794">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HMRdVUecyk9H40RupmRkKHReUHlRblq6XofDAwaha50a9buuMcA4efasOLANDMaN92VoSQq8f5TbnYq2PoGZfpp9Lkar6HxVbbq8wAlPixuMDfyPbZNHFxBJK_LBolWrjZqZFp55wxQVKBNzzxCTFzVxadPpHg19uvkLBLnj_HwXC4M2YHHxB0huZFTuEHs84iqVPfcy_3v63wPiu8oeVxc34XdsMuX3hZ6x9GpL-FLoCzayQ0mYc33HuHhBXJhfP7VQPCHwkBXfRY_IfDgRwTJ7rsosji2rbgtbWWUE5reQh2GgWppKq0yG_ReWizflor7urDJrYbjVkPVW1xQHRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NWZ_TijuFGS5Fyk2bm1kXB-sc9cv47j9vio2xMERZr-d0DrBHElVaH12-h7SBkgmee_X5QReSbpiGnDGwldFtRkqWrzmVd57pWgor3vY2vKueV-A5QEeb6LBMALWf13nDW20fXU3Vb8D7IFxf_K00Lm06UbK0aKdR-sP7sGTieXgSatrgu7Rcq-0X2zOcs5c2l9uIIe8yPvMr4ukTELB_QVQhGTzhDGiVetDng3oOm8Sa5WDtMFjh5Nj1GHOqqLc4_0rMfvJCCy-FXR_ind45dmRN10db6YclvIK_YdUEP5O8nwp2tX3nKMmD-PJndbIcTpPEym0hhjmGYJzZ-VqkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ایران صاحب پیرترین ترکیب تاریخ جام جهانی شد
!
تیم ملی ایران در دیدار مقابل بلژیک با میانگین سنی ۳۲.۵ سال، پیرترین ترکیب اصلی تاریخ جام‌های جهانی را به میدان فرستاد و رکوردی تاریخی را به نام خود ثبت کرد.
@AloSport</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/129794" target="_blank">📅 00:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129793">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
یکی نفت رو میگیره بجاش سنگ پا و سوزن نخ کن میده یکی هم پولا نمیده و بجاش سویا میده
🔴
دیس ایز ایسلامیک ریپابلیک آو ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/129793" target="_blank">📅 00:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129792">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11e0b59223.mp4?token=ewA3AM7OO_HdZJztuOqU3hAtfsTCsvi03vkxl6CBA7pxq4I_FxBo1PoJ0TXWUEzaNHoy38t6aQHn9d_DkupE-UTE0MUVbBkpcMrT3NIsrCrj1B7E-QeznFD4-MiLOHqwPL5i4ssdW8XJoXrIfpJOB1HhHVdvrj5--yP6sh9cmBAks959GD-2yDMT0Nav9VWPx8drMciHRSdLVjOCBRmh6nGO5zObWN_jK3yTCit8brL2CDp43gsItBDn8QjgHkhjBhSKPh26Sb91hneK-II7gOM6uamrcdYeMdsF4_EGABZ_kPhylypspqYfsJW_EewJZkjXzRhN06CmqtPW5eiisg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11e0b59223.mp4?token=ewA3AM7OO_HdZJztuOqU3hAtfsTCsvi03vkxl6CBA7pxq4I_FxBo1PoJ0TXWUEzaNHoy38t6aQHn9d_DkupE-UTE0MUVbBkpcMrT3NIsrCrj1B7E-QeznFD4-MiLOHqwPL5i4ssdW8XJoXrIfpJOB1HhHVdvrj5--yP6sh9cmBAks959GD-2yDMT0Nav9VWPx8drMciHRSdLVjOCBRmh6nGO5zObWN_jK3yTCit8brL2CDp43gsItBDn8QjgHkhjBhSKPh26Sb91hneK-II7gOM6uamrcdYeMdsF4_EGABZ_kPhylypspqYfsJW_EewJZkjXzRhN06CmqtPW5eiisg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف و تیم مذاکره‌کننده وقتی ۱۲میلیارد دلار رو میدن تا از آمریکایی‌ها سویا و گندم بخرن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/129792" target="_blank">📅 00:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129791">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frommorteza</strong></div>
<div class="tg-text">داداش حساب کردم پشمات میریزه .نفری ۷۰ کیلو غلات میرسه بهمون</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/129791" target="_blank">📅 00:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129790">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TeC-wLSSn8ggqD2Az2zW465G1Q922jPRMFTTD05cvnrfoiQ1D1ZFtDuoDcfMojbpDuXS8DZ2my7vxbEfPSaPLrzjuXa2FedDDnQw0HdJ_bfNTTDgO0W4Mp_kAXWPHtg5NQYEsgwabNUiDfRD_tLy2Rmnb8hadN9WmvOwSTmUJ3dBfdgOuaQ8QzSqJybiSMubrlCAaiYwf-dQ1gCD-g-VWEu8kmqseEv6i7dudguBc0t46tuxL7PKggXFQK48i1_vWwZgN4P9REGCIZGpB1U7NdKCab54u40pxEjdfyITb-TrAUAN6bqopfBJUS_zoicQrj8_FGQN9wgyb8rByTp4tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
همتی: اگه آمریکایی‌ها قیمت سویا و نهاده‌ها رو خوب بگن ازشون میخریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/129790" target="_blank">📅 00:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129789">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_IVIS3Tst-W6no-8MKv4Tk-ySGplN0g47N9alHTW2rWqhZCWCRlhAIxpYC7OCaVeZY4DrMfLM80Jf-kkLUQfsZv953Z-UQbRaheTbFVPsyuXnk_347oN188Sicga5lehHic3grjGTgTVvAWg5Mlk6LNsVVdKbV3yd2SssmqeEPNZeaDmVHX4NK35S3-VvLvKe2BhcRs4g8oAV_1H5TNZf-5A1jWUk6qpncFxq4fSgeWvyUyfloZ88swEWgn8GKQesV2qPmxZuJzGr_IzX1u8KlNkjl22YJ_77x1RufpkYSHRqbbMgKZVIfpJqlEr0fwx71erzuc1zV6_8QSOdbQuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش چشم:
هر پولی بیاد ما موشک میسازیم تا اسرائیل رو نابود کنیم و به آرزومون برسیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/129789" target="_blank">📅 00:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129788">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OAGjEIwYFl0GhOWvNZVHtVWXQyX-kuwZ85_OYC0H7N6nWYATLxsHR-753Z8IIwpkxiZwYqA_kljncZAQr7gyeY3kBlbdApZWtkqt1Em0yvYuSfdPeNSy6oomcjq5MyHwjid_VZgbyPxDOmLWujU3egZ29MCLzCxQ0PIFPeJmXf2N8UMSgzkgMCUFlYEr2-3iu5R978qY3YJqSynraaJq6HKG-0pvVKRqHQkVXlO1SeEpe6SdeFaQx2XP7OQg_2a7UPY3XX8PKINEHX67hX8sNwKVtfZzyDmMIeCKfyOIRI7PYKdLYCC_7EJdlUwsj6ayQqf95akq8N043WTCwcIlXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: با آمریکایی‌ها عکس نمیگیریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/129788" target="_blank">📅 00:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129787">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
خبرنگار : سالگرد عملیات جکش نیمه شب هست، اگه برگردید عقب، چیزی رو عوض می‌کنید؟
🔴
ترامپ : نه، هیچ چیز
این موفق‌ترین حمله‌ای بود که کسی تا حالا با بمب‌افکن دیده؛ کاملاً توان هسته‌ای‌شون رو از بین برد
🔴
اگه اون کار رو نمی‌کردیم، الان اسرائیل وجود نداشت و بخش زیادی از خاورمیانه هم از بین رفته بود
🔴
اونا فقط دو هفته با ساخت سلاح هسته‌ای فاصله داشتن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/129787" target="_blank">📅 00:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129786">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
رئیس‌جمهور ترامپ درباره ناتو و ایران:
ایتالیا خیلی بد بود. آلمان خیلی بد بود. ناتو برای ما نبود.
ما سالانه صدها میلیون دلار برای دفاع از آن‌ها در برابر روسیه هزینه می‌کنیم، و سپس آن‌ها به ما می‌گویند، «ما ترجیح می‌دهیم کمک نکنیم.» حرف احمقانه‌ای است.
چون ما می‌توانیم این حرف را به آن‌ها بزنیم اگر بخواهیم، و ممکن است این کار را بکنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/129786" target="_blank">📅 00:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129785">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
رئیس‌جمهور ترامپ درباره ناتو و ایران:
من حتی به کمک آن‌ها نیاز نداشتم. بیشتر از هر چیز کنجکاو بودم.
از آن‌ها خواستیم بیایند، اما برای ما نبودند. احمقانه بود که نبودند.
استارمر آنجا نبود و مردم بریتانیا از نبود او خوششان نیامد.
استارمر به ما گفت: «به محض اینکه شما پیروز شوید، ما آنجا خواهیم بود.» من گفتم: «وقتی ما پیروز شویم، به شما نیاز نداریم.» این وینستون چرچیل نبود که با او طرف بودیم؛ این را می‌توانم به شما بگویم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/129785" target="_blank">📅 00:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129784">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
ترامپ: اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من آنچه باید انجام دهم را انجام خواهم داد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/129784" target="_blank">📅 23:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129783">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
ترامپ: اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من آنچه باید انجام دهم را انجام خواهم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/129783" target="_blank">📅 23:56 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129782">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb4f50edba.mp4?token=v1L-iLoq4ordOoC0mAwLbVg7QsgA_WrLgsPvKRcrBMe484TkdALSOm2WkjjjYPT1_Tf05Gx5sAA_ABOIHDaKDZtsG7cJBU31KZAA7lWKcDzj_JFClie5-nJkHkKn-k7fD2ggP6NPoWtWcvm52u8jqmfi6w40xbSb1NQEB1iy2yD2ozu4k271Ibyj4OP7M0qMPJoMDW7XBABCuL9PZsBx5MZ-bKHEXNoNWUGOu7MFbfWp5FB78LWWT5qOBJVu22YV4PsM289yJFagrfUzXnja1ubGEvL4auSVkO0u85vsCGy3Y8AISAc0LQXAvOVjHzTmsKTgZMbju4x5M5nLf5LGDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb4f50edba.mp4?token=v1L-iLoq4ordOoC0mAwLbVg7QsgA_WrLgsPvKRcrBMe484TkdALSOm2WkjjjYPT1_Tf05Gx5sAA_ABOIHDaKDZtsG7cJBU31KZAA7lWKcDzj_JFClie5-nJkHkKn-k7fD2ggP6NPoWtWcvm52u8jqmfi6w40xbSb1NQEB1iy2yD2ozu4k271Ibyj4OP7M0qMPJoMDW7XBABCuL9PZsBx5MZ-bKHEXNoNWUGOu7MFbfWp5FB78LWWT5qOBJVu22YV4PsM289yJFagrfUzXnja1ubGEvL4auSVkO0u85vsCGy3Y8AISAc0LQXAvOVjHzTmsKTgZMbju4x5M5nLf5LGDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف: اگر به سوئیس نمی‌رفتیم، هر لحظه خون بیشتری از مسلمانان و شیعیان لبنان ریخته می‌شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/129782" target="_blank">📅 23:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129781">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/054f327a6d.mp4?token=JjBFaun1nDLwpgdLfCFSCq8yyLd51iOWRSG9R3OPxPsfPfq3SxhfPztS9IIh2pnm2flI-bxgv1NE-QlH8Fx9hSXf36B4LFiOvA82d6AFPo48JnyEdmA3X9jXT-uY64Iryy73Som2KJvW4xhj-iuYtl89nQCk8Ptn61DGDHQxPu5L835ledJM3YFz-XiQfE5z5e2UaDp-feImHDcuJYDpzSzJN92LB_YAo7-KJCOmugDGLgNz36A3cyVsnEFCWdugncKbfzHNAhTQPmBmQzQPUuwwa6LGiDHOgXadXKgFbaPRUOUzLNwp6cHSI20ISbpLMr98CAY7xowqV2GHDkFzaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/054f327a6d.mp4?token=JjBFaun1nDLwpgdLfCFSCq8yyLd51iOWRSG9R3OPxPsfPfq3SxhfPztS9IIh2pnm2flI-bxgv1NE-QlH8Fx9hSXf36B4LFiOvA82d6AFPo48JnyEdmA3X9jXT-uY64Iryy73Som2KJvW4xhj-iuYtl89nQCk8Ptn61DGDHQxPu5L835ledJM3YFz-XiQfE5z5e2UaDp-feImHDcuJYDpzSzJN92LB_YAo7-KJCOmugDGLgNz36A3cyVsnEFCWdugncKbfzHNAhTQPmBmQzQPUuwwa6LGiDHOgXadXKgFbaPRUOUzLNwp6cHSI20ISbpLMr98CAY7xowqV2GHDkFzaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: نتانیاهو می‌گوید نیروهایش لبنان را ترک نمی‌کنند
ترامپ:
🔴
ما قرار است به این موضوع نگاهی بیندازیم. من یک حل‌کننده مشکل هستم؛ می‌توانم مشکلات را سریع حل کنم، از جمله با بیبی.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/129781" target="_blank">📅 23:48 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129780">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc43c98ca.mp4?token=Pz-cH6zyc6J4GjOffqoDAQDRCob9P9QgwL4DsBSJmSMSEYr1hJZ3gdxq6PhuYJcfjtWXCoe5Pzb6hEIYPE8GAzM314LxeRWjJePB7LYKYIi2iuCfruXO2cUKjWzjAD9-oZsdBFCeh22Tr5k1NIP-UOTOg7rAsqPIsjv7pJvojyHN-ja1jNDnPJ7i4fvz2hDUVuBPkWn66MkSMxccSA-HJwAOebIRTFMZO1NH805PsjJn6ChVT6Au2lSSMFTtc-yTpxBnhMTJblxV8wu2uAlsgzMsbaZUQOBCd7LilJeWo06obf3kebifpGBdy0jfpWVFdCVMLO7i5yfi0XDHIdW31w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc43c98ca.mp4?token=Pz-cH6zyc6J4GjOffqoDAQDRCob9P9QgwL4DsBSJmSMSEYr1hJZ3gdxq6PhuYJcfjtWXCoe5Pzb6hEIYPE8GAzM314LxeRWjJePB7LYKYIi2iuCfruXO2cUKjWzjAD9-oZsdBFCeh22Tr5k1NIP-UOTOg7rAsqPIsjv7pJvojyHN-ja1jNDnPJ7i4fvz2hDUVuBPkWn66MkSMxccSA-HJwAOebIRTFMZO1NH805PsjJn6ChVT6Au2lSSMFTtc-yTpxBnhMTJblxV8wu2uAlsgzMsbaZUQOBCd7LilJeWo06obf3kebifpGBdy0jfpWVFdCVMLO7i5yfi0XDHIdW31w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور ترامپ درباره ایران:
باید مکالمات آن‌ها را بشنوید: «چه کسی می‌خواهد رئیس‌جمهور شود؟» «من نمی‌خواهم.»
هیچ‌کس نمی‌خواهد رئیس‌جمهور شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/alonews/129780" target="_blank">📅 23:48 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129779">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15fe6d2c2d.mp4?token=no5-QAYRpMFeEUKVWC5aN5gct0deNsGL9WiCGZSNLpVL_ybzK2cWcnqAaOz0s5a6xjzAc_Uoy25d9GZcX5ZzoZ_yeRZdOaTRMDEGU7wOWLr5Yu2KnZwM5AocgCaeIPJXJ2lfNQLquKjhRPu3_S91J9qs2FfTzm0jsFmmdOA3BG-BFBRkRUFLzK8VSBky_uz99_1AqG3fkI5Cvbud6GCf62Wvgtck2Eco9AqvlbxTrZWvHJ_XyxRPoeGLG_mOC69j3M7xPEWl1ebtyZxup1OXDnCODUyvhdjNwXx2qXPL4uuTSaesB0wxqkxby0KSPAOYrrjopeuqASkbOcJkVADTJEcnmbGrDG7L8T1vHTC30EOs6nUanQIbuqmVbVz_FrcZ0hrXKSPpAq9147U_6cTl5KhKxX0Q6Wd7zfztzORWgfUEdB6TZyEKQMvNUXhDE2c2X-1CnttqJLiCoOX-n9gg1kYc8fblALp8aFQXHRYCmRIXX-KNj4q4SvIaI1WUIdGRanUYci0-qtF2ijHTmzIqdSp9PyOv70vLB9a5EzCOt5AMHDopbJdho_TplqjOXA7aiuTpRGLcHF841xcZGyenxKmLSlHuaJmN9CKZxHb_HFGpZcB3EaJvyOJsmNlwq97gE2yqeMnjW1bYEkwDTI3wCxDmpdcaAVQfUzrhxvOp4E8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15fe6d2c2d.mp4?token=no5-QAYRpMFeEUKVWC5aN5gct0deNsGL9WiCGZSNLpVL_ybzK2cWcnqAaOz0s5a6xjzAc_Uoy25d9GZcX5ZzoZ_yeRZdOaTRMDEGU7wOWLr5Yu2KnZwM5AocgCaeIPJXJ2lfNQLquKjhRPu3_S91J9qs2FfTzm0jsFmmdOA3BG-BFBRkRUFLzK8VSBky_uz99_1AqG3fkI5Cvbud6GCf62Wvgtck2Eco9AqvlbxTrZWvHJ_XyxRPoeGLG_mOC69j3M7xPEWl1ebtyZxup1OXDnCODUyvhdjNwXx2qXPL4uuTSaesB0wxqkxby0KSPAOYrrjopeuqASkbOcJkVADTJEcnmbGrDG7L8T1vHTC30EOs6nUanQIbuqmVbVz_FrcZ0hrXKSPpAq9147U_6cTl5KhKxX0Q6Wd7zfztzORWgfUEdB6TZyEKQMvNUXhDE2c2X-1CnttqJLiCoOX-n9gg1kYc8fblALp8aFQXHRYCmRIXX-KNj4q4SvIaI1WUIdGRanUYci0-qtF2ijHTmzIqdSp9PyOv70vLB9a5EzCOt5AMHDopbJdho_TplqjOXA7aiuTpRGLcHF841xcZGyenxKmLSlHuaJmN9CKZxHb_HFGpZcB3EaJvyOJsmNlwq97gE2yqeMnjW1bYEkwDTI3wCxDmpdcaAVQfUzrhxvOp4E8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور ترامپ درباره ایران:
ایران چهار ماه پیش نیروی دریایی و هوایی قدرتمندی داشت. بیشتر موشک‌ها، پرتابگرها و تأسیسات تولیدی آن‌ها از بین رفته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/129779" target="_blank">📅 23:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129778">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75e37a8b38.mp4?token=PAWvTuv5cKfX9QPLlVvKS7ePkcldTyQqVi1Ex5DaCIdcm7G0ytDYHxJS7MKZMdIvEoZuSiF7OOQXAoT7CfyV4mPQqHQ9DhcSOCd4IlMGKZ5hZB8O1NERUr1LHV5SBZ0yC-G62OUQngvcFzLcDAAYrZoRx5itrEEAnlnAkh13-bBukoyTtdXOh6swJllNeGS9v02xC7DfSroW5u12beUAbIOtWvOnwCQIgOv2e4ZQTp8sdvAESrKw3CnsOtldVppQ5P26525tJdm_mzanrwHTAtAxP_l_t97vZdMsj10elSaDYU1XqQbYl9u9RGzcgcQjecrAx6im_0wbQZ0FJKrYhJ0_ARTFIlRXuWMoSwK5DwBsZUq7uj2-B8BeHp5XIVIVl3-FspNa9G_6bVdb0oJynGEoY9vUNT8YaoU3tc0to3FMb66JY5itqzKhjZqn_6x5aXWxCwRCSSoZDD7RiwwMj1PAfl61Bv2INRBFmgz95DNOVlS0CLNgP9k8N31V17S1JFcsqcRB2oBDR8VnWc7AYS8sG0mBX2jGGnQb-LZHfFhEN-cMd53WQKaZ-CdDqqpMoELHPw9FdKbklL5PLPb2e5BqxSGT2JaRavADj09IkmGQX5fjvO3vQpgPxNfE5d0ptLDvA7nspr5BOiuUToYYCq6gbFTp5Jh1aGbLCNFYgMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75e37a8b38.mp4?token=PAWvTuv5cKfX9QPLlVvKS7ePkcldTyQqVi1Ex5DaCIdcm7G0ytDYHxJS7MKZMdIvEoZuSiF7OOQXAoT7CfyV4mPQqHQ9DhcSOCd4IlMGKZ5hZB8O1NERUr1LHV5SBZ0yC-G62OUQngvcFzLcDAAYrZoRx5itrEEAnlnAkh13-bBukoyTtdXOh6swJllNeGS9v02xC7DfSroW5u12beUAbIOtWvOnwCQIgOv2e4ZQTp8sdvAESrKw3CnsOtldVppQ5P26525tJdm_mzanrwHTAtAxP_l_t97vZdMsj10elSaDYU1XqQbYl9u9RGzcgcQjecrAx6im_0wbQZ0FJKrYhJ0_ARTFIlRXuWMoSwK5DwBsZUq7uj2-B8BeHp5XIVIVl3-FspNa9G_6bVdb0oJynGEoY9vUNT8YaoU3tc0to3FMb66JY5itqzKhjZqn_6x5aXWxCwRCSSoZDD7RiwwMj1PAfl61Bv2INRBFmgz95DNOVlS0CLNgP9k8N31V17S1JFcsqcRB2oBDR8VnWc7AYS8sG0mBX2jGGnQb-LZHfFhEN-cMd53WQKaZ-CdDqqpMoELHPw9FdKbklL5PLPb2e5BqxSGT2JaRavADj09IkmGQX5fjvO3vQpgPxNfE5d0ptLDvA7nspr5BOiuUToYYCq6gbFTp5Jh1aGbLCNFYgMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار:
آیا می‌توانید تضمین کنید که ایرانی‌ها از سود فروش نفت برای بازسازی ارتش خود استفاده نکنند و فقط برای دولت بعدی آماده شوند؟
🔴
ترامپ:
خب، آن‌ها قرار نیست این کار را بکنند، قربان. خواهیم دید، اما قرار است پول را برای خرید غذا برای مردمشان استفاده کنند، چون در حال حاضر مردمشان خیلی گرسنه هستند و آن را فقط از ما می‌خرند — ذرت، سویا.
باید پول زیادی باشد. امیدوارم پول زیادی باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/129778" target="_blank">📅 23:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129777">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbc98d2cf2.mp4?token=ugcSdq9QgFZc1F6im4OoLru3-cNd9CPe6EjO2MENIitBIVSKoY5upyoqbOtS1S4jHLFAca1V6TKZWW-UK_Y4yIdz1ECii-T72-J4qCX_zAFRHZp1L9hdvHUBpeZtBmJ6YLeL1lgc55i1IyymvYnskKL68XA4I3AoX_nJB-jg-z707-EEtfsK2SPiB_SJPwDvT6A77mICb-7weKrt3edwN9zDd01W9eDd74jaQ0DWtyzVbnqv1pFY1wFCrCHpnp2p4w1ML7IIW6p3A3tFMqBPpOWzy3QpeomL4BXbsWYCAM23CZ-shxheE5eeK8hjc1Ex37C5hiv8WVNjwHlk_yy7OjJO56pr6BwFA06kJCL_7SQiRJdTf-UbMDv0xSZfud0HkPo_Em2nUZwJB2xd148XITuj7o-jrbNWdTPvGDsDMr1ZDe8Mawgs0m47O9K9vT3x-NlYNAVzjOFoI4XbDQPQ2OeY6FA9bPVdFyNgiHPECJbwXIwqgQ0lNut-3niuGKRXF4K6cD6pB46DLul2TiSRalzA0ruTgX7_nDsbQowB6F-X4GJc8eiQY8Z0hqdboLFCSTvhyFukXc8he6lQOrqF7yCKFDA_SZ0fKH6UFtBd2guPWyviVtflL-ABqyf_qQBC6IUVg1oq-N-bB8XDphwITdbYocOuxQudXjDtj3lBsmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbc98d2cf2.mp4?token=ugcSdq9QgFZc1F6im4OoLru3-cNd9CPe6EjO2MENIitBIVSKoY5upyoqbOtS1S4jHLFAca1V6TKZWW-UK_Y4yIdz1ECii-T72-J4qCX_zAFRHZp1L9hdvHUBpeZtBmJ6YLeL1lgc55i1IyymvYnskKL68XA4I3AoX_nJB-jg-z707-EEtfsK2SPiB_SJPwDvT6A77mICb-7weKrt3edwN9zDd01W9eDd74jaQ0DWtyzVbnqv1pFY1wFCrCHpnp2p4w1ML7IIW6p3A3tFMqBPpOWzy3QpeomL4BXbsWYCAM23CZ-shxheE5eeK8hjc1Ex37C5hiv8WVNjwHlk_yy7OjJO56pr6BwFA06kJCL_7SQiRJdTf-UbMDv0xSZfud0HkPo_Em2nUZwJB2xd148XITuj7o-jrbNWdTPvGDsDMr1ZDe8Mawgs0m47O9K9vT3x-NlYNAVzjOFoI4XbDQPQ2OeY6FA9bPVdFyNgiHPECJbwXIwqgQ0lNut-3niuGKRXF4K6cD6pB46DLul2TiSRalzA0ruTgX7_nDsbQowB6F-X4GJc8eiQY8Z0hqdboLFCSTvhyFukXc8he6lQOrqF7yCKFDA_SZ0fKH6UFtBd2guPWyviVtflL-ABqyf_qQBC6IUVg1oq-N-bB8XDphwITdbYocOuxQudXjDtj3lBsmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار:
خزانه‌داری تحریم‌های نفتی ایران را برداشت.
🔴
ترامپ:
من باید دقیقاً وضعیت را بفهمم، اما اگر تحریم‌ها برداشته شوند، پول به این کشور وارد خواهد شد. تمام آن پول بازمی‌گردد. آنها ۹۱ میلیون نفر جمعیت دارند؛ نمی‌توانند آنها را تغذیه کنند. پول عمدتاً به کشاورزان ما خواهد رسید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/129777" target="_blank">📅 23:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129776">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G81fsycFBjYYUeEk0oQXj0x7jqRCfotIEbcAz4E1wm0GE9DTLhwIEHAW4FTbOqi9dF4sPJkyD72Slnk8kXhz0rTOgpJfmRc8v4jdQOta42Pzunvxk10jaYsJmGdem4bHnXBuirBZgdXbSdJEfHnBFRqmz-wdqXF23TPQvfAV-PcWUmK7_fHf_ztmB2VqEIZl4_YUTdMH6Ix90drv5z9PsKla9eqp4ZuBlomSE1WG5NMnlo7meRpQkrkpKpBBFqThX9TH2BB3K5TqJUvsCalDVtHQYmk2sIrRmzENK4Sg0q44rs1xGnC5g_oB33rnjP92KGbokV_M974FtwRA-yBn1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: ۱۲میلیارد دلار رو آزاد کردیم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/alonews/129776" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129775">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-JdifPamPHuemvLlFvBNrc8tv1oDootls6ZdM2axF1DHbcEcy-sR8WtxTckQSxw8EM5Qc3-6WBzTGdUkb2YSiLSkRYh236tn0ST-p4iWQA8dlji3iBUQzO38suSiN4FSBdTrdjTwYKIn56Si7eC92Ra5rELmrqj4rlTMh9UTliI3Z444Pa5DuIkczox7iImELQ2quZXkUdUXLQ0iv2pZsoRoXMcdz-BjtoqA0xC42iR7c9F8jmfe9xSXp9WahG8BPWEM8_b1_PwRb9wIqcfNSrw3nSA9kDDtcLYs37j4u7blz0ufxBFfTQ9Yh9tjVuJNqMQpCz-ZfX4OidVIdbxYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: ۱۲میلیارد دلار رو آزاد کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/129775" target="_blank">📅 23:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129774">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd99c1a494.mp4?token=GatuH9kMPbnGWiQXpCtkT4oxZ4bgTWqed35QQjJwlJjE3mmoLw35ITll_8RwAAdFIfkStk-3RJJoTKvLYA4K7wOTiL45BI8vSVcIAkxuBXpFXnN-riQ5EPx6BdB6yEhj01kO7vJlAkNpYuLP8Mo-8M5nhigPspH8Osn-2fwZLG5kk5Qn1d8Kisogn1LqUzqe3hd-NqQ7Colymq9y2sEt7bqoWGhDAJNi8-ACkWnO6qizCHXIxImL2QUOa_l2nFAW1A2vUR32QE2wWnW-mZPsD6tlaNy-6mMLzoyoWSGtBYpSho8i_ZAdbEFrNB-0EVAs7Znf-GJJWwVEn10knyg9cSYENAwUVhi6nyWeXph3S7mMglUWIzfBp_X7xSKTvlwOjQulE7AULqiC3QbIwm4ZbDYfI1pDACo8CEdcMBhGJT_hUIzsd_Tfp_rPFzJhs756ZhWhZy7nWEZwKVfkJjE4eSxDKtYzMNx8L8eZ3W9Hte0ei9bFVjwoaXTrwCNw0mYyjyMXOwMMQS-sfFM6-ZYEsclrS7oa5i_G635FD0iGzKA5Gi4BNCaU6XKerADBmiWkHb3Qb8_R22SgGvQzSA87FwvXxVTg-n_qpYgwrl08O7itpK58zIpjggpuwNbIsqSl_6mApRagfMfjD9yrDfjhMQ-_SMqtX4FP8s46hwuDPJc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd99c1a494.mp4?token=GatuH9kMPbnGWiQXpCtkT4oxZ4bgTWqed35QQjJwlJjE3mmoLw35ITll_8RwAAdFIfkStk-3RJJoTKvLYA4K7wOTiL45BI8vSVcIAkxuBXpFXnN-riQ5EPx6BdB6yEhj01kO7vJlAkNpYuLP8Mo-8M5nhigPspH8Osn-2fwZLG5kk5Qn1d8Kisogn1LqUzqe3hd-NqQ7Colymq9y2sEt7bqoWGhDAJNi8-ACkWnO6qizCHXIxImL2QUOa_l2nFAW1A2vUR32QE2wWnW-mZPsD6tlaNy-6mMLzoyoWSGtBYpSho8i_ZAdbEFrNB-0EVAs7Znf-GJJWwVEn10knyg9cSYENAwUVhi6nyWeXph3S7mMglUWIzfBp_X7xSKTvlwOjQulE7AULqiC3QbIwm4ZbDYfI1pDACo8CEdcMBhGJT_hUIzsd_Tfp_rPFzJhs756ZhWhZy7nWEZwKVfkJjE4eSxDKtYzMNx8L8eZ3W9Hte0ei9bFVjwoaXTrwCNw0mYyjyMXOwMMQS-sfFM6-ZYEsclrS7oa5i_G635FD0iGzKA5Gi4BNCaU6XKerADBmiWkHb3Qb8_R22SgGvQzSA87FwvXxVTg-n_qpYgwrl08O7itpK58zIpjggpuwNbIsqSl_6mApRagfMfjD9yrDfjhMQ-_SMqtX4FP8s46hwuDPJc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور ترامپ درباره ایران:
ما در مورد تنگه هرمز بسیار خوب عمل می‌کنیم.
دیروز نفت بیشتری نسبت به هر زمان دیگری که از این تنگه عبور کرده، دریافت کردیم. تنگه کاملاً باز است.
ما دو چیز داریم: یک تنگه باز و کشوری که هرگز سلاح هسته‌ای نخواهد داشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/129774" target="_blank">📅 23:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129773">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fa7c9b7e2.mp4?token=v7csy0IZBX_qVSQM-9v5KpbJ87cwrvTqpmUqnnoYoIm2sLs3rO3DoBao1bgVUWrjc1b-Q9LTBF09SjquwjdLDQHe1S1SYChLByDpAfrnOXIKtTjN-OvFYXj3ooJNINiYd6QJi5GM4GkkpE8nM-pfN3CnkWefHeVv_N88tlI5ys0idDsjeDq8ce6dajqpB9hikz5jAXoKeVCwcjm0RjMzrCu1ZOC6vxyAGNhQmL_DbSz5V-7sbr_aQs0wr-4jADCZPTShYJJpfwHX7DzHUvjlbrU5_8aeU6blpHp-EZWkihds7F6c88AQE0t_WZnhO0rGrT8rb7d1M27lrCfT_-CEoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fa7c9b7e2.mp4?token=v7csy0IZBX_qVSQM-9v5KpbJ87cwrvTqpmUqnnoYoIm2sLs3rO3DoBao1bgVUWrjc1b-Q9LTBF09SjquwjdLDQHe1S1SYChLByDpAfrnOXIKtTjN-OvFYXj3ooJNINiYd6QJi5GM4GkkpE8nM-pfN3CnkWefHeVv_N88tlI5ys0idDsjeDq8ce6dajqpB9hikz5jAXoKeVCwcjm0RjMzrCu1ZOC6vxyAGNhQmL_DbSz5V-7sbr_aQs0wr-4jADCZPTShYJJpfwHX7DzHUvjlbrU5_8aeU6blpHp-EZWkihds7F6c88AQE0t_WZnhO0rGrT8rb7d1M27lrCfT_-CEoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:
پول‌هایی که در حال آزاد شدن هستند، برای خرید مواد غذایی استفاده خواهند شد و این مواد غذایی به‌طور انحصاری از ایالات متحده و از کشاورزان آمریکایی خریداری می‌شوند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/alonews/129773" target="_blank">📅 23:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129772">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
وزیر دفاع پاکستان:
اسرائیل تنها تهدید توافق ایران و آمریکا است
🔴
اسرائیل به هر دری خواهد زد تا در مسیر توافق خرابکاری کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/129772" target="_blank">📅 23:25 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
