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
<img src="https://cdn4.telesco.pe/file/pdXbTOwkacVpV2dQELJmT3lFEfwlITurzrTxF2gjyCyXb55TzY5djh_Uh5DElnH9mzeYwFRPPETZwLwXHIiGaWwh2qCThZQg6OTgXWbirdNX2vasxI0K8NEj6R9srDJegOJcKOPV949ThSQh1ERJpIMzAiqGJfp3z-QXRne28o4qVw8-yiG47ws5siGKftGyYXROdnAhdmr-uaFrIz40TN-C-P4zvi8kws9Sktlc-T1-zegZvp_x8sqVXkJdAoFPcBEcLk4AGQQL13VbRrcZ8Il4N2QqzHgM0iStfDS3l9g6KcgKCm0TG0tqWHeoW_pLe_9j62WtiLtuaWgTMxjvJA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 185K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 15:33:43</div>
<hr>

<div class="tg-post" id="msg-79232">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ویناک عجب چیزی داد</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/funhiphop/79232" target="_blank">📅 15:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79231">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اگه فان هیپ هاپ نبود بازم تلگرام میومدید؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 885 · <a href="https://t.me/funhiphop/79231" target="_blank">📅 15:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79230">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAli</strong></div>
<div class="tg-text">رفسنجانی این بی جنبه بازی هارو در نیاورد
که خامنه‌ای رهبر کرد
بعد همون خامنه‌ای کشتش
این بخاطر چند میل پول داره خودشو جر میده</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/funhiphop/79230" target="_blank">📅 15:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79229">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">این کصکشا بهترین ترکای دو سه سال اخیرشون فیتاشون باهم بود، ریدن تو همچی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/funhiphop/79229" target="_blank">📅 15:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79228">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVinak</strong></div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/funhiphop/79228" target="_blank">📅 14:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79227">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">درکل کل رفاقتا رپفارس سر منفعته، همه اینایی که میبینید تو رو باهم رفیقن پشت سر هم تو پیوی اینو اون ناموسی میکشن به هم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/funhiphop/79227" target="_blank">📅 14:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79226">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">چمن کونی پاشو ۷۵۰ هزار تومن بدهیتو بیار بده</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/funhiphop/79226" target="_blank">📅 14:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79225">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/funhiphop/79225" target="_blank">📅 14:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79224">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">پول کاگانم نداده
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/funhiphop/79224" target="_blank">📅 14:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79223">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/funhiphop/79223" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دکی ۳۳۰‌ میلیون تومن پول ویناکو خورده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/funhiphop/79223" target="_blank">📅 14:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79222">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">کونکش برداشته به باباشم زنگ زده
😂
😂
😂</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/funhiphop/79222" target="_blank">📅 14:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79221">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🗣️
چاقال چاقالا چاقال چاقال
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/funhiphop/79221" target="_blank">📅 14:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79220">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بابا
😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/funhiphop/79220" target="_blank">📅 13:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79217">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVinak</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/funhiphop/79217" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/funhiphop/79217" target="_blank">📅 13:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79216">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dei6iP3rNvowWIWrkQmYtluGHU5Jm3yFueYgVkHIUIMi2U-mTIbwNVJVhxYbFBRYJKFz2cU2yPRUOrj1wn75CvnknfS6l8psg203BBrOlIIh3EKsSjGTxiWoHmA3ZCxKRie7rM9ZS_Hj3Ir2OuoUrZiKVYihvkHJvqJ7L7zmP-DS2KFCPRYW3HN9LpSGx2RFddLEsAANB1JA1zvfs8ea4IrioLmfkg-VYbXUGsZnxXPc8n344_d93qRcsC4FKMo28xdCG_w-2q7ltToPqUtMwaB1oB-A7zA9jUGDzNghBXzYRcXArYRVy0ZEuEpsXzfF8zAf2qSLuhAt8mem2wx69g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز تا قبل تعویض شدن مادوئکه کل موقعیت های انگلیس رو مادوئکه ساخته بود
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/funhiphop/79216" target="_blank">📅 13:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79215">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">تاج: پیگیر هستیم به پاس افتخار آفرینی بازیکنان تیم ملی کشورمون به هر کدومشون به عنوان پاداش خودروی لوکس یا خونه بدیم.
- جوابش با شما.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/funhiphop/79215" target="_blank">📅 13:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79214">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">بهترین تصمیم زندگیم ندیدن سریال و فیلم هاییه که ترند میشن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/funhiphop/79214" target="_blank">📅 13:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79213">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uh5KLcgQoyWTAu0TS3N_wm51Lqkk4OT26x0SwtAlTmCF8AVbqbBuTpFjIpKGlK9cf9P70bFuaB6AXjP8f4zn8ChjFSUYTaNUjtHUNjwc3YrWziJXAHoNDaDKSRo06X4N7r265Iu_2qjuL6_0QEaMeR3zseYN3OIW89hRNPscfSjpDfOsOmSpXL59-dsOf-lzKXiZi0r7EKpYwCSR2Oxe9EOEztWbhkWAwzsvk9-gMrw8bwZoTEmkWVnxr_ENA1WUyhXH1ubdQWqL74EouI8eFM4WJhmyeTxgKyZLEwqx6AbuZ3faW5najy4UwIz6LhteCh2Kf_mN28XlycjfoG_4kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنجشنبه ها با محمود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/funhiphop/79213" target="_blank">📅 13:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79212">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVTMzk7mBrzjPuVS0dGbqe0QrIO65lNWwxt7E1NwiULy32zLcupA3EE8H46cyMScMRiPRBzN8RrTg4yLmkR4Q2hgG_3Ut1Ka9Jgs-uOobSKM5tIgB2NPDS2FMUliA-cLhsNiqCfcbrqtUomz4YNTjMqV7v5KzSPUqbQs4Z1WGn_dBoD3Xo9WnK9v6pucbAVCQ6uWse70yJqHNi3XjNKAhfdNEzFrk0mdW3B5pbsxTHzBe94STK3_YjFrMUaD8G9R0foIdQ28otPcwvRxS1Fq0nl30ss7GSxCxbz607uUhaBOHWaGmD5KxB_DfCEmvWUaev__jcQ5l97BxslKnZKBpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پرتغال
🇵🇹
-
🇭🇷
کرواسی
🏆
یک‌شانزدهم‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
بامداد جمعه ساعت ۰۲:۳۰
📍
ورزشگاه تورنتو
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
✍️
اطلاعات و شرایط بازی:
- پرتغال با ۵ امتیاز، به عنوان تیم دوم به این مرحله صعود کرده‌ است.
- کرواسی نیز با ۶ امتیاز، به عنوان تیم دوم گروه خود، به این مرحله صعود کرده‌ است.
- برنده این دیدار باید در مرحله یک‌هشتم‌نهایی به مصاف برنده بازی اسپانیا و اتریش برود.
- با توجه به ستارگان و قدرت دو تیم، گزینه صعود پرتغال می‌تواند انتخاب مناسبی برای پیش‌بینی باشد.
🧠
اگر مجبور به پنهان‌کاری شدید، مسیر اشتباه است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن اختصاصی
R11
🅰
💻
@BetForward</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/funhiphop/79212" target="_blank">📅 13:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79211">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PiilKVF6Z9mzrlsuI_tbBBn9D4dLEixSzrN0CpsQ3_OGUOAZ-BJUDYuGlxqjuo5b5JvsCuc4mQnwIJR83H0TPYp_R79D_btGIoIgqZDCW9VNr91hCVERtCWVInLWhlgo8rikBl2EY6VUu2_XwQf6zRKOqrx1wWKy4GmV3Zf9EnVfb8PL29dV27YpPsHTfhrBbn90v8aC3xQfEbGOYhhf74wwwGj65VWBCOYW5K7x3S7F29dWfDP4E1XIRX39HrYEiQM8rD6PdkN0WsfTE5ToyYunxQUMJ135GRHaRZliWb7RBkhnavKo5MQ-_Z1w9G-9M4RJixAwicifptjBj9lfdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاج: پیگیر هستیم تا به افتخار آفرینان تیم ملی خودرو یا ویلا به عنوان پاداش داده بشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/funhiphop/79211" target="_blank">📅 11:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79205">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">تتلو زندانه یا استودیو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/79205" target="_blank">📅 02:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79204">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sabmpOkOoC-vA2wGiRwXvOAHnQ4mpQcShM-ZAYDXUeIzRqTO7ZqaxxLOIZGUiESgrrwtgAJT1fQGmylfVeVW3zLebTN7oJogYXjzEUBsQDoT8c1VEk7iGUayDgAbChTyu5JNm9n1JM9aKiE-qsST5MPWVllwvxzOm0d5luMg3GWH9Xwkt-47IqRD7vPHcbUBFnn0dfYoJQuDV-JYu8CbT0KraT3vqsxG1EISjCjETb8ElvTzy748mpdCLUZ87E9eiMwHGqyzJv8I3Ql2eyO7zmDbPZ0o1VE8cY2tSrr3sI-d8y4-k0DdrQBC0CSuDDuntZIemwzmL4d6O4i01sRp4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید تتلو  به نام تریلی ریلیز شد.
🔥
Youtube
🧃
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/79204" target="_blank">📅 02:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79203">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سنگال عجب تیم کثیفیه</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/79203" target="_blank">📅 02:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79202">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xqf2DLh4dadQyDVnnSka4AfW--WM7RXnUMcKisxRTWU2LvCqj1jabtI5yTW4dlwwKNaJSuDyTFuvDVb4jVpOzWg33Y3LiSttlH2so68Pj_TMVseSJg66WtuUDNEOG0fPmh7Av9M9bpY7875_NwWl6mGq-3HqvYWyaIm_7tTN8XHm7gsU0ubf5QKd5j7lFHPJAAphddwgiay7_GQWcxikSgvh_XtJ-kf_PMmXCVsQIFb3bcpbyNRLUx5ZiVbB3qutrFjbGJvkjmVuo7miYCsYI7ono7jIyYr8AoGlNQ9hsm2H7AwX0yVxYP-_98zmB5lY3zIImKZ_2WRD-_vjsv2IZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخرین فرمانده باقی مونده حماس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/79202" target="_blank">📅 01:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79201">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">یاد ژاپن بلژیک ۲۰۱۸ افتادم</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/79201" target="_blank">📅 01:24 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79200">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">پشمام</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/79200" target="_blank">📅 01:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79198">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rGLSWv6xjib49PoGBDk7U-NaRHBik13y3OgNoAwxgw2DBtjptBqMvWOqTHMZz3Yu99RiI1GRTp7gX0bF1Rrb6_5O7rMMrqXsz-ebtTHw7t_AonEyhe17IXOpdVw_eJNnonX1G6kZSn716akc8mRiUnFyS3PszVeBc0Af8pu6PIiSEEHp62LvdzvNHSL11sa4VlNNfO0GiXJAp5f19llmSgdJwBrkmDml669Z9UMEMQJcVz1bTn0XVCtei3U6uJ8R9451wBGGut-XBMW4Fyq4-V8mQp5oYSBtTlcsfyMjh0KbeWSSvYitIK9dCoJpNTXz9EMoThqlfhiT8IZXqHPT2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RiI5mXL16W5LCO1a1u7veLsDCHdcTNMly0skLNBiPuwJH8H243UcIq6hJ7QFqp575VL62uxMrFSNDkueNDdgxHDSdP1utsO-xtao5Aystn5M00oGi8Z04LqYQNxjxslzaMBlk90LXI0QMn-46BivuV-8qbVb-auo2WYBV7ZNCHohKiaylFqhmn9tei8rHxljKh4M-nuXHNejlMB7P1XgCJLL0bekfZImEZwPt1piH2UuI3eMdkyOJxC4a74iB-TmzSSDlJWReU-g9r3hLTeozppBCfPq-RAB7AOLjoVer_zY7XCbNk1JG956MPB2c1zBrlC5M-EX0A3Zh5OqTnQUpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">احمد الشرع می‌خواد برا سوریه یه مجلس گذار موقت تشکیل بده که چند نفر از اعضاش رو هم خودش مستقیما مشخص می‌کنه.
بعد لیست اعضایی که برا این مجلس مشخص کرده رو پخش کرده و این بانو هم توش بوده که خیلی سر و صدا کرده چون بانو تخصص خاصی نداره و صرفا بازیگره.
انگار احمد الشرع با خودش گفته ببین می‌دونم یکم ضایع‌ست ولی مگه کی قراره جلومو بگیره؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/79198" target="_blank">📅 00:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79197">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDf3SgOfPWy2CW-Y0QvqePM6T-ubq1T8revaeqMLoorrc8lXNk_eO_kqTgXIMW0cJQvPUrnQKbWw7ne9AWIHpp1sT4CO4MkQ8JChkrtYKM1OHvb86EyJETRSsIRLDdVMyEvHSj4ROP18T97MeRKF-yRc9ZLMpqEk-ZA5aE8QExyXm-OAStBVZuNrq2dMh3v9KLiZXTnMLvPtMU5Ofp7hYMkujb2u1tBNTzYkgnwlxnW5kbUC4VTJqmdS_cXtypEPqT3uTBGaa3GL4EDQ-pnFPFP6XgLGPaWqfGodwd25Bz_kcweYEFxGd3F9Ln2wVtbU9b8yotbZhLUYLtr2t_B5Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخجون میم جدید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/79197" target="_blank">📅 00:34 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79196">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPYTwJaIoOUOgkmcal_6PrIeMHuxMFb9Qi4n58DlO-hMrtCvfkK0DH62pKshIimHHgBxoxOgYxnk381YhwsLSogWkLd1E32FdPbJB-MBfwoGMP0uG7xe6wzcQm1o11YieuuvMhNfCCA8PnPBVKojsNDMtLwiNgesl7kdAMu0_BTBHaU_dgpj3Z7-hu3WTcYeIS8C136AcuTSZHJfkAu53Vfc6XjqYdRw_8TCAWYC53LNpQ562Dbp5akRomUTxNmqEBN0lU4CyzyTVAQ0sIweOQ9a9vUJCYv3PXQziB2HnY_JcbqJw7UTDN28G8b0MXmoQE9jp-XlVMZR1pp0QqdEpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چقد گی زیاده تو سنگال  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/79196" target="_blank">📅 23:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79195">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">چقد گی زیاده تو سنگال
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/79195" target="_blank">📅 23:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79194">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">حسم میگه سنگال صعود میکنه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/79194" target="_blank">📅 23:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79193">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">قهرمان جام جهانی بنظرتون؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/79193" target="_blank">📅 23:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79191">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">قهرمان جام جهانی بنظرتون؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/79191" target="_blank">📅 23:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79190">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQBN2vI17sEg4ErlZ1GHFebY5dw0Xq9aJohHL4tP2t4OJqg4SZDxdgOqhi2L9O8gmp0FErb289FwE67aGiTA-tRswq0FvjFMlra3igX2VXaaD1F0_54dxhjmIr7UiVwArLyvOumeVmqtevjOrDDiNkNgeOxsZ-ZgxynEunA2Rr6sMhcbZwJ3b1bgYw7L5Kyh93SI5fEYG8cNw-9BSdmO3aWv0F5vFrK00kVrlW_GPXdLJ_tZwg8_lHav2IJlQvW0sAXR88d4zP_0NsakQv8IuTu3urAuKphwxF0Bd_sw6fLBl5N6XaqxjAVZftUlCTTAi5LV5aj9tZEf62RlwlpTKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید حسین تی ام  به نام “اقاقیا” منتشر شد:
🔴
Youtube
🧃
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/79190" target="_blank">📅 20:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79181">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">خدایا با حذف انگلیس یک بار دیگه فوتبال رو نجات بده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/79181" target="_blank">📅 20:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79180">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Parvaz</div>
  <div class="tg-doc-extra">Arian</div>
</div>
<a href="https://t.me/funhiphop/79180" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@ariansongs</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/79180" target="_blank">📅 20:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79178">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بنام خدا گل برای کنگو</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/79178" target="_blank">📅 19:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79177">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVwPDLeC3j2j_-yuwAeBHlHBGS6KMQa2kvwUTJcWHVfPF_chpws2VMZ-OAJTcD8MdX_H1NLkb304hirfc2NzdhktKvxKoVZ-DKSwq_mHLv7joLijkhauNUferO3fc6x5DjMqTpgS-8BMHxPIUOSsP4IoIX_M5z2pwy8W7QhOu96c16TtRneYL4ZfxmimdUkFqCqbWmJA_cOU_1a7K1VYCV-e2VcsqsPzzhzKC__qKta6j8bHaUgRE6yTr8QVpZdOpTRiZLIy6gIyWHFVIX-C_FF03MDrAYjnv-bGjkqRxPrPB43l3KboYdsswT88VIOgs2c5eTu3FF35L41UDaDtiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یامال: اگر قهرمان جام جهانی شوم تتو نمی‌زنم چون‌ تتو در اسلام حرام است و من مسلمانم، الحمدلله.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/79177" target="_blank">📅 18:41 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79176">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b3f4634aa.mp4?token=sHFBy7MkTuV1S8NdAPBFRBdPNagpbbx4ylznI6k83o3toYQ4LZJtcZnOyM_wfMnbhcKI3hxyaDFfr0I4dJZAGbopB-8NKiNdVFriNd5Q6DivUeNqjOaylKYQw-1voAqbyhn1VpByiGE2C0OZDHPUB6P9g_NlJ38bKME7bYWGR30STfoRlo0e6WEaYaMn3M3SpSH7ZRD3GGNiPoBz8l1o3cNiONhCpiR4NzzTHQYNOhchATMqowYMTW2Cfy1cfGRNrSN3d5-dBNUaGI_v5XCNFgHK6MTZb60RqrsaGFZXdXrShBhedKRjd7gL8oHrXq4FOgKjpi3IquRCGuCFaPVNEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b3f4634aa.mp4?token=sHFBy7MkTuV1S8NdAPBFRBdPNagpbbx4ylznI6k83o3toYQ4LZJtcZnOyM_wfMnbhcKI3hxyaDFfr0I4dJZAGbopB-8NKiNdVFriNd5Q6DivUeNqjOaylKYQw-1voAqbyhn1VpByiGE2C0OZDHPUB6P9g_NlJ38bKME7bYWGR30STfoRlo0e6WEaYaMn3M3SpSH7ZRD3GGNiPoBz8l1o3cNiONhCpiR4NzzTHQYNOhchATMqowYMTW2Cfy1cfGRNrSN3d5-dBNUaGI_v5XCNFgHK6MTZb60RqrsaGFZXdXrShBhedKRjd7gL8oHrXq4FOgKjpi3IquRCGuCFaPVNEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پارههههههههههه شدمممممممم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/79176" target="_blank">📅 18:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79175">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ویناک فردا ترک میده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/79175" target="_blank">📅 18:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79173">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TiS5qzTyfLDNcRYepuxHGX5oaoHnctHEnlsOp34mf31q95ziWyV-mVsf29WpKNE4PPj9Dl_3_YkiOJ3DVL1eUeI4xJODhhGApdQiK8ENL8qJdc05-soVVyWLttUUqTcuVjwR7Mz4jrt3eJNKeROYZrNL8qZUE-C6L-YJ6di2l1QdKxDRURjhPSf6qziyCsW7X0A_G8rl1aO-oHjE_xveVoxUbB8EK-n7oQaBptyhmoTZEjtmUf8iFvbeve69Xsc0s9CN72_LPAp3uWIx_srJXDrAaCG5hHI3QOr1glrWxWhPGGe5TnlVKLh75TWu3nG8UpvRJT9BPat4CEWK-8vgmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OG_Nk5K-Ls5aFHkKZbuKjcTu8XFUBd7kKveInC5xWSanWYUaHqvIJO6pBeoTH0NLJFnF5l8nCvrvRtcDkUW4a31Vfq8436SKtbaHad78TuDTENwdVRWRsU8LdHI1cMvuIq6hIRbfCyCB3qCLyS7MpLrJhbVaNZMJqS2yV-ksr2M_zSImbg6NHTAHfcXKMDkLtVrVElSBEBtG5HXQnhq7fedofEyozcBLgbqPWg_YcaMnQsYVN-bFvDcHHrpWQcFf0VojeyUoK7mEwcR1TahtnF2n7eBHgMaonA3tsWGxmBTBGECp-e8DHbKCk7sh8bKza5fiSGjG8NrkG6cfK3bxqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خلاصه حواستون باشه عمو رو بازی ندید.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/79173" target="_blank">📅 17:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79172">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHhAN9rQpWYrvN78OI_UdpIe2oUUJZEWlF45DMBs9uKv1M744939gaC30ERRMkkXwOH90J8tuPl8HG4x_Ma_H-YlMqFqUIadwH0dRwCJYpreZSiIY2q4RH876M8Z3dyZ9TiLyIZsuV8-K9bKvnfSck8xRssFpZZ4fOsBWjjsUq_NSHmobceMPs_zytGMfJc3zayDBkeu1FVUyb3FaqyhoCEpu5jEdSPD_CAjrwGDj6bMrUcvtIsK4dHEDigKqApnvs9fU2CixyzChd29Rxm7-fOfWf4oPMceSNeNdiWBo-ZAfpjIu-C68p-3pcEoanCJArP2trK71R3fh-h43MDpMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
بلژیک
🇧🇪
-
🇸🇳
سنگال
🏆
یک‌شانزدهم‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
چهارشنبه ساعت ۲۳:۳۰
📍
ورزشگاه سیاتل (لومن فیلد)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
ضرایب شگفت‌انگیز
✍️
اطلاعات و شرایط بازی:
- بلژیک با ۵ امتیاز، به عنوان صدرنشین از گروه خود صعود کرده‌ است.
- سنگال با ۳ امتیاز، به عنوان تیم سوم به این مرحله صعود کرده‌ است.
- برنده این دیدار باید در مرحله یک‌هشتم‌نهایی به مصاف برنده بازی آمریکا و بوسنی برود.
- با توجه به عملکرد دو تیم در این تورنمنت، باید شاهد یک بازی نزدیک و غیرقابل پیش‌بینی باشیم.
🧠
پیش‌بینی آگاهانه، تمرینی برای نظم ذهن است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن اختصاصی
🅰
r10
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/79172" target="_blank">📅 17:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79170">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oigwoOZrqESamxjLW8aDrn_nUXhP16OtXqMdkE_y8lyWWzI_UmbLmFAvlZ5rX_0DO9yZzDAXLBGlGIviVP1bd7xBQc-5KTmjPlY2t14JPDcspD4nh1a6kwxRzKAZ83CobhKxsvJ2ceLOMqqlkC88c4tWdeRIJJoPD_-g7dpj7XXJUfzezKJFR1ry0uKlP8RTVPubL0cCWdQ2wiF8FhAI8qZyequuzUeJX5SvZyaHkV7APCwPkEgCQEWcU_-yQIUMK4byfENE5wtf5_ytiH1WOGuuhgsQCUScHZEAUvN_E0Mgqxv7FWfh1BiWhbqsm2AKPhpeiinkbsjelOr51l76_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RPDZCbGDxRgXU0n5Nf01E0FLoJBQMs7wYbRZgF7GqRlsCXiyzQNh2KJJMGmiiZgtox377-H4F8S5i4XoowF0BBIekDxPR39zM0PAULOL8FXQWvmfjT5vqTLXUroj6kE25Wbtn3ijWttgqmX-SITWRg_e0yPJ7srgnLJPda4clNxCekBgabMu6vfvot-B9AdQJf-uLbZ1zcM5-YkicwL-OAucXyycCPpEYHS1hBQDOYaLYu99uBM5RAXooBUM_SieVBmcwvPxJgBi7kGW2ZO0dJuE538eKuGJi96VCiOA2BzmbYvcnUIVer00Q9HertILq0gVnoYcnSL9UFPKcXdgHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امان از این پرتقال فروشا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/79170" target="_blank">📅 17:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79169">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OY5bVxhcd4v9Bf03UzbHSQ9PnaPMaok8MLu8tIqeR0hbGfB1_PsjvDWCcynpIF12kUZAdJoVwUWWn5tQTtORKktvW8F2KLe0-hPKsOID3zCI80kGEo8J0786GL-a0SVdEvHimJrB_d48WtmbpuEbCfJVY64rtZetD8dozaVwlB_Wr_bYA6g4TyWFQ_2y7n3FE2gqfGe2GpG4uht_67HPtLpDjm1xlshm5SGirYDOLXdvPof_a2WNSHXktajh_wubSiZuyW0BDVd0Qfwq_FKRJzskI4g-_-Eq53a29V2sRiHL_YR0RwwyGmyl7IipO4xOnUx65Xrk1T-kSVPMJ3kyXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سعید آساره فعال مدنی اهل شهرستان ملکشاهی امروز سه شنبه ۹تیرماه ۱۴۰۵ توسط  وزارت اطلاعات بازداشت شد. تاکنون از وضعیت و محل نگهداری این فعال فرهنگی -مدنی  اهل ملکشاهی اطلاعی در دست نیست.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/79169" target="_blank">📅 16:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79166">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b10d6b449f.mp4?token=puy0Elnibd_FmVgUl0Yf8IIli60U9paq5MOYLko3UUiGndladBO-pWBDDehVS__P1xK0ebUx4mUVnnEumZblHlEniCNNiwhMA59ty7ZSmdi1Nhd8bU294i9zkt1WuhWI-svScm6OgjawNrMlHg8l--Ad_XSbTBkz4X9-xIdz77KRl9WP9TENeRChj2Ybi8YeEI9yJV-28oFbQ4v6S_ILH7YehBkMUbU6dRxCkRAYooRHErJegnMga4SGmVu8nXuylTg3A_WjnHfG8QFQt9zfGB3dGU84whVFp0xwJR2dSRzu0b4XV3Vk9UAVzJQ-Rl79D81Y1Sh-VXRr8rEAt5eaGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b10d6b449f.mp4?token=puy0Elnibd_FmVgUl0Yf8IIli60U9paq5MOYLko3UUiGndladBO-pWBDDehVS__P1xK0ebUx4mUVnnEumZblHlEniCNNiwhMA59ty7ZSmdi1Nhd8bU294i9zkt1WuhWI-svScm6OgjawNrMlHg8l--Ad_XSbTBkz4X9-xIdz77KRl9WP9TENeRChj2Ybi8YeEI9yJV-28oFbQ4v6S_ILH7YehBkMUbU6dRxCkRAYooRHErJegnMga4SGmVu8nXuylTg3A_WjnHfG8QFQt9zfGB3dGU84whVFp0xwJR2dSRzu0b4XV3Vk9UAVzJQ-Rl79D81Y1Sh-VXRr8rEAt5eaGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بی صبرانه منتظر ترول کردنت هستم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/79166" target="_blank">📅 16:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79165">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5ZcPXR65HkJfe4HOB1jboZ2-1i1sGPC15_ZWvKyXOUOHKnN02_4_BeVaZ4uqgsvFH-JsW9OkSJ6rtXvHtLMnCzJzCnxuWmtsE-MA_4-7pM9aV0em9iQAoqHnsYCXg1e6_qnKUE4XkqJTBf9A1Xf0mn16UvoKTeaPnmlV3YRLKZzsp45F6L5jqOlb0bAc3oCrI-jhkccmxYkBWM9QYFscIaTKKn9ZH0Q5ZMNDVdBzZbbi-1YCS6reqT9phHSG2nB8nddmlmFP0V1qf0XhCUmHoUhtRqaHlimgev7rHRvACgEFcgUI6yYM9doXE7JtJm7ik2Wpx2iIeUdvC1Ym8XqEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/79165" target="_blank">📅 15:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79164">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">وضعیت جوریه یامال مراکشو بعنوان تیم ملی انتخاب میکرد شانس بیشتری برا قهرمانی داشت تا الان که اسپانیا رو انتخاب کرده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/79164" target="_blank">📅 15:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79163">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">بازی رفت بارسا و رعال تو لالیگا افتاده ۳ آبان تو نیوکمپ.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79163" target="_blank">📅 14:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79162">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">کانال ۱۲ اسرائیل: ترامپ درحال بررسی بازگشت به جنگ تمام عیار با ایرانه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/79162" target="_blank">📅 13:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79161">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">تو زندگیم اشتباه زیاد داشتم،
(یکیش ادمینی همین چنله)
ولی هیچوقت عشق ابدی ندیدم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/79161" target="_blank">📅 12:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79160">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6094ff0128.mp4?token=sZHZzwNYk1PjIQZErEJqjbABZzO-BAMgNS1S07YTyy0MJRkzmsbrlRvmTWgrYh2R_05Jwv-ySb4QVtfhD0721vI85zYupughs3JQNc25H3fgHv_nTMFU4B_cU8W2NVuFn3BHB0OBUydbVoZAIRKabsU2lbvH1kt1i88SCvWL2tgp4B36ORU4fcvje--rVgO8ZLw7qfMFgtj4B4Mtw0Me4PuMATQ4yHXfzDDu9sG0SijcGNbWlP-gLDRazQCr25OU3620c4wi5aRXfDZS-Qao3pToV2Yx2gWJlEK0Phcy7qa67hY6jhmgvj_WfKbJZVF89WlazmOBo147Vx_gGj_PHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6094ff0128.mp4?token=sZHZzwNYk1PjIQZErEJqjbABZzO-BAMgNS1S07YTyy0MJRkzmsbrlRvmTWgrYh2R_05Jwv-ySb4QVtfhD0721vI85zYupughs3JQNc25H3fgHv_nTMFU4B_cU8W2NVuFn3BHB0OBUydbVoZAIRKabsU2lbvH1kt1i88SCvWL2tgp4B36ORU4fcvje--rVgO8ZLw7qfMFgtj4B4Mtw0Me4PuMATQ4yHXfzDDu9sG0SijcGNbWlP-gLDRazQCr25OU3620c4wi5aRXfDZS-Qao3pToV2Yx2gWJlEK0Phcy7qa67hY6jhmgvj_WfKbJZVF89WlazmOBo147Vx_gGj_PHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرم معکوس با فان هیپ هاپ
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/79160" target="_blank">📅 11:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79159">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9OUzARItdstWrjtHE6NoLbKusrWdjeQHxCKytotEEhgs4yQwIM51EjV0u-Xm2UhKxA9JXAJ_qWbfWj4dCgR5-4rQiy_mqcKdZtcnXIChew_KvkALDL6ebXFo3M5FTeHl7agmFE4ldjneiXOzkPHgl7nfdHHcglO3j5bg_mJJDu8HovdHFLF7Ie-DaEbsAcdBXuMCqahMTATVt-tpOhx0cqDKENuXyJ9NTWHKuNgC5K59sL1dDdPaxD1TUIAue8NRgJ6-Z-M4s8eC33yGZrRyIPrccOjU5opxdYW6ldgdiGaVmwIJQwAv3Q2SZL79BgWuuWfQ2N4LNMMHp3WlfBfJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت صندلی قدرت تو ایران
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/79159" target="_blank">📅 11:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79158">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3r9RbAwoLa4IFXmX-wV57oGL7aKQP8WVtFO8RL6xK6jp47uJn7xBkpC5r_6qbZEgDGm7gDN-C3ynEYGL7vDJBFQmklQDUCSKBGCjZu9K0jqP8-RJSDtYYN7G3_gV2nIEf5qXCgbFfQYJuSYxPuRLTwX8x2sCSyIvF4kbrBUlhIORcfo5kbyh_vaIy3eYtgDEp5y_Kdx813QHy055BuzWJMmo2HF0qP1Smp6Zx1rWf3HAW9FBc1B2__1_ZlvIUg07vTo0DUB-s_ASSB76ZJn8LFQ7z_jag0brLQsORtsSHZdMtzHO2dCZ4eumNNHSQ7OPSaNDnEs9D5RUMs7Gxswdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
بلژیک
🇧🇪
-
🇸🇳
سنگال
🏆
یک‌شانزدهم‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
چهارشنبه ساعت ۲۳:۳۰
📍
ورزشگاه سیاتل (لومن فیلد)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
ضرایب شگفت‌انگیز
✍️
اطلاعات و شرایط بازی:
- بلژیک با ۵ امتیاز، به عنوان صدرنشین از گروه خود صعود کرده‌ است.
- سنگال با ۳ امتیاز، به عنوان تیم سوم به این مرحله صعود کرده‌ است.
- برنده این دیدار باید در مرحله یک‌هشتم‌نهایی به مصاف برنده بازی آمریکا و بوسنی برود.
- با توجه به عملکرد دو تیم در این تورنمنت، باید شاهد یک بازی نزدیک و غیرقابل پیش‌بینی باشیم.
🧠
پیش‌بینی آگاهانه، تمرینی برای نظم ذهن است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن اختصاصی
🅰
r10
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/79158" target="_blank">📅 11:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79157">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">۰۲۱کید تورو خدا یه کصشر جدید بخون هرجا تو اینستا میبینمت داری میگی "فیفا ترانا بن مای فلگ" خسته شدم گاییدی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/79157" target="_blank">📅 10:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79156">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39eac96d35.mp4?token=cVE92FLxA8NGuSZ35fv3aO63_UYbwUkPqybXNjeb1iAUkfiWIXdL4didlEqeFb5cydD6UCaZgm7jSrmHenI-R0xHg4VV5D4PtJR60aIGIXvaAzKsXH5Y17BGUJjHSRZqM64q1vlg7QiSlIHLHS4x_4bN3DzY4CmKhtRR948zCb1jQV8IcGKDDYZa3WGbB471NdlduVQXH0rdyF4a3RzY9eVYXCR0mOH-VnzwCov-WDspnuwTvnDZU4r5326ZhYaX6Awn-uFzseMnQdgimnlJeWzH5LvJMQ66HfW-dcZRucq1rMI4RiFDn-Wbq1HtBpfNyIMCE3Q5InOyZ0ZdI8-fYTk-doesGYvFtR3PGtkLtzSwwMLM6MH8q7KsUQgrxgJxu32vduFiX4K_3CYUudjIPL9rU-G6_ZVlgwBn68eEvGWgqRierG5A3v5yqx45_2AygHibg0UDJ81WWvJImCZPvgJcpb7hf2kAiOnJCk_SGdgJKA2DRqRZWvnFFe_LnuC9njIaXkYCdoK1a6bVvQeGxZIB0nBnTAQRNgOeq4sTEh3xzGWCZF2a2_7iaEHRDG-pRWBo7YFpGcNwcnbDZnxo10F5OlyCFKM4P2bmmrqsf8mvh3Z_-SX56JUdSt5XfGj-E1DOWQ5vkS0bKmHPBpxZyhDXAyS6FexSMN9Q8rWXBX8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39eac96d35.mp4?token=cVE92FLxA8NGuSZ35fv3aO63_UYbwUkPqybXNjeb1iAUkfiWIXdL4didlEqeFb5cydD6UCaZgm7jSrmHenI-R0xHg4VV5D4PtJR60aIGIXvaAzKsXH5Y17BGUJjHSRZqM64q1vlg7QiSlIHLHS4x_4bN3DzY4CmKhtRR948zCb1jQV8IcGKDDYZa3WGbB471NdlduVQXH0rdyF4a3RzY9eVYXCR0mOH-VnzwCov-WDspnuwTvnDZU4r5326ZhYaX6Awn-uFzseMnQdgimnlJeWzH5LvJMQ66HfW-dcZRucq1rMI4RiFDn-Wbq1HtBpfNyIMCE3Q5InOyZ0ZdI8-fYTk-doesGYvFtR3PGtkLtzSwwMLM6MH8q7KsUQgrxgJxu32vduFiX4K_3CYUudjIPL9rU-G6_ZVlgwBn68eEvGWgqRierG5A3v5yqx45_2AygHibg0UDJ81WWvJImCZPvgJcpb7hf2kAiOnJCk_SGdgJKA2DRqRZWvnFFe_LnuC9njIaXkYCdoK1a6bVvQeGxZIB0nBnTAQRNgOeq4sTEh3xzGWCZF2a2_7iaEHRDG-pRWBo7YFpGcNwcnbDZnxo10F5OlyCFKM4P2bmmrqsf8mvh3Z_-SX56JUdSt5XfGj-E1DOWQ5vkS0bKmHPBpxZyhDXAyS6FexSMN9Q8rWXBX8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فری استایل جدید یانگ کید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/79156" target="_blank">📅 08:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79155">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">بی جنبه ترین پلیر های تاریخ ایرانیایی هستن که میرن چیت میخرن تا با چیت لول آپ کنن خودشونو.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/79155" target="_blank">📅 04:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79154">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AisHsLG1aELILWoqKhVluMwUBhz4oCEjKf9M4txVIV6C3UGBrsRY05fGHS6Nb6HwNpWNn_Q3XmXd-yLVY2R7gIS8a7FqhfCnRS3SsuUxfZ-D76peVnLxSumc3fBs_KzAVcAwwixpY5C-ILkSIqfQf0QUoU1vowQSUh3O5_MlhNhS5dpKTzXGX7bgc2B3uwFo7dVddgzlngNapBvZObCEEaigVvycSI2wJ1Hc2q7lv60mxsXM1yidlt8aeoMFtxQ1YHlp9oW5P5v2bUBsyhsX6iQZjCKEkc42oPJXytrq31eGmVXuZyBJ04tnh6NGLHzyNAmUQbWPDjSfhcfU6GhiVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت فعلی جام
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/79154" target="_blank">📅 02:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79153">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">مکزیک قطعا اکوادور رو میبره
شب خوش
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/79153" target="_blank">📅 02:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79146">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">فرمانده نیروی زمینی سپاه درمورد جنگ زمینی:  یک دفاع ملی چندلایه برای ایران آماده شده است که ساختاری غیرمتمرکز و رویکردی نامتقارن دارد که جنگ را برای دشمن سخت و غیرقابل کنترل می‌کند. جغرافیای ایران زندان و مردابی برای هر مهاجم زمینی‌ای است. نمونه‌اش ماموریت…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/79146" target="_blank">📅 01:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79145">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3o6EPzVoDRdMKnCjlIU_ajap2fV9-jXHfyFiEIyWZ8m5aSj9KHXCrHReFd_IjddMyAN2Pwj_a4QwPFrCjNQYUZFbucaSf0KJtv4DSCVH4NOR_IA0jvXcXYx0vU2nlJ5rCuhuPDuOyJ7n6DWO7pDSw1pThn4VMn-4_qxqfxtxg1mUy8Ap3tbA4OQfom9NjggfpMPKcStW-HmVYOKTlK0fINQns8v1TA-uh2UoZWoR9_HBLKVikyhxLtZ6haRm10foC62Qwa0AZkavdJXIH5Nn5XslkC9-CjYljbQ7_KgDLSEpHPM4iXYaFvoJNmB5rML7JpXzyf_DCyR-ZRVAmOiYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده حمله زمینی امریکا باشید
ناوهای آبی خاکی USS Boxer و USS Portland آمریکا شامل چندین هزار تفنگدار دریایی وارد منطقه خاورمیانه شدن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/79145" target="_blank">📅 01:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79144">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اولیسه و امباپه جوری کنار هم خوبن من بارسایی هم یه لحظه دلم خواست اولیسه بیاد رئال</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/79144" target="_blank">📅 01:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79143">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">امباپههه
فرانسه برگشت
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/79143" target="_blank">📅 01:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79142">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اولیسه داشت گل قرن رو میزد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/79142" target="_blank">📅 01:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79141">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">امباپه زد ولی افساید
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/79141" target="_blank">📅 00:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79139">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHK2k9jAxYCk74tj2_ii8kUXmHKzXE6AJSifSwIJbHsE3N4mcKmZSOeJhrk_pie_HQ53crqEakWQMSdLxMqjMBeElRQLl26Yl5NdTKq1AicAWfk77n3ZmEdGM5GQ3DagPzHKkPKo9wxWzryLeP2_ZJmat8VnUrtu2mT1eJODbhACriaCfJEbUo1Y_aum9sfv3r-cdF6gGtFzRdz6mujy3iuknqaMwhedm_bKy8ScSaXsJanEMdPN4geuyBQxTXTePM4hE0LONUG9oWyZn4KwibP-eyS_S9CAuqo1TdX-6QIN4alrsJHVc1E6A0_ctyh38g_3hGI-f82FjFSIUSSVTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس تابوت علی خامنه ای منتشر شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/79139" target="_blank">📅 23:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79137">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">صداسیما سخنرانی ممدباقرو قطع کرد
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/79137" target="_blank">📅 22:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79136">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbOQjh8HGAmomXVgQxgJGgSNWDSovruU5Pt20YSsryOJDbfuzO9_GVOqb4neMivy-I2k5KW-vATXXJH1zDU15Tb0FzltHHLX2u4kKSMm17SotNqBNmnsLDKkLTFAQDf08vagHZJwZPekttZJNULnmYEW3Z_FUaz9nKeI66CahG9day319uU07FPsWngDQ_F2U69WvALdMTcbkeVxEmrbxpXMjJVG3WkL7R-9ISKSMNccI7k2i25SXLwGCGsAYpmeiRxBE-RMlzF-fIh7--8aMh-oL6WM6HDFcajFBgluUCf4CBWtFffugNEjHCzv8bon-SZDxLPzuhQH-Au1bVzGZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسنوپ داگ
:
«یک نفر دارم که تمام‌وقت کنار من کار می‌کند و تنها وظیفه‌اش این است که به شکل حرفه‌ای برای من ماری‌جوانا و گل بپیچد. در رزومه آن شخص، در بخش مهارت‌ها واقعاً نوشته شده «پیچنده حرفه‌ای» این تخصص اوست.
من سالانه بین ۴۰ تا ۵۰ هزار دلار به او حقوق می‌دادم و تمام هزینه‌هایش را هم پرداخت می‌کردم. اما اخیراً متوجه شدم تورم در آمریکا خیلی بالا رفته و همه‌چیز گران‌تر شده است. مجبور شدم حقوقش را بیشتر کنم. تورم آمریکا عجیب بالا رفته.»
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/79136" target="_blank">📅 22:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79132">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">۶۰ گل ملی در ۵۳ بازی برای هالند
😐
🔥
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/79132" target="_blank">📅 22:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79130">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cd63244ad.mp4?token=tJU6hYDJZ29laKIdzMpqJPJQ_27TvTjgP2J8FOmSeJNUpI42Olv5_qv40M0XTaKs8qQe8I7Lpq46j76eExsgy_Jby5-q3qFh-6Wxp1kSwiKb_-i83JzLoWHpDXiVvL7-vFm7G50yXl2UFMLHvvPpEocqh6lxFWIWsg5WepRVtyQB69-KkbzzhxI2osQ4mOCLTFDh9U7JDNCNLCUxbwqlo5vYBKrge4sROQL3PxPx0v5P3tHwXlWIxv0ExVxiVwC1npIrgWZcOmzZgVA-HpU0rnlQEMkTM9zKqtDGiucEd3IV_5M92S_BrnxdfQEJ5-YI71S_HyADiB-_cXbexpa5AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cd63244ad.mp4?token=tJU6hYDJZ29laKIdzMpqJPJQ_27TvTjgP2J8FOmSeJNUpI42Olv5_qv40M0XTaKs8qQe8I7Lpq46j76eExsgy_Jby5-q3qFh-6Wxp1kSwiKb_-i83JzLoWHpDXiVvL7-vFm7G50yXl2UFMLHvvPpEocqh6lxFWIWsg5WepRVtyQB69-KkbzzhxI2osQ4mOCLTFDh9U7JDNCNLCUxbwqlo5vYBKrge4sROQL3PxPx0v5P3tHwXlWIxv0ExVxiVwC1npIrgWZcOmzZgVA-HpU0rnlQEMkTM9zKqtDGiucEd3IV_5M92S_BrnxdfQEJ5-YI71S_HyADiB-_cXbexpa5AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خالد مشعل یکی از رهبران حماس درکمال گستاخی اومده گفته رهبر معظم انقلاب اسلامی زبونم لال فوت شدن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/79130" target="_blank">📅 22:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79127">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ساحل عاج واقعا شایستگی یدونه گل زدن رو داره</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/79127" target="_blank">📅 22:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79126">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">میثاقی: بیرانوند از بشیکتاش ترکیه پیشنهاد داره  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79126" target="_blank">📅 21:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79125">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">میثاقی: بیرانوند از بشیکتاش ترکیه پیشنهاد داره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/79125" target="_blank">📅 21:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79121">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ساحل عاج فعلا بهتر از نروژ بوده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/79121" target="_blank">📅 21:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79120">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">نروژ یکی از استان های خوب ایران
به امید برد فرزندان کوروش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/79120" target="_blank">📅 20:49 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79119">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=uKcr8AndkKrZHRkfPyh2qscjnzqiN8CkPL8gEVajBECcRMiaQvTYbgZXrqtjBrFSBap-1gnlayzw5YDKp4L4zutpxymKMUg6tk0ow7nXzeY4fizDzXpElWDuxGiyiEIXU0QNc6oKqS7IwxGehL9xsq0MYCHhTgkhGLiWto6dAzWnAuWSBDzywMgK6GsQlWnMX_EzW_2az0xUNWH4llDCBaKh2D1315q2io11fxUChz9ytPBsT-Mgkr7H8sQFwjIF4KM8VtCvhGxrHvlq5OCTTw-Jr3i9SZj1Z0yZQwZLjVwXHfv1VGKmrhUzsv5PekWH_yasfiG1dBGnNmmEv7KWZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=uKcr8AndkKrZHRkfPyh2qscjnzqiN8CkPL8gEVajBECcRMiaQvTYbgZXrqtjBrFSBap-1gnlayzw5YDKp4L4zutpxymKMUg6tk0ow7nXzeY4fizDzXpElWDuxGiyiEIXU0QNc6oKqS7IwxGehL9xsq0MYCHhTgkhGLiWto6dAzWnAuWSBDzywMgK6GsQlWnMX_EzW_2az0xUNWH4llDCBaKh2D1315q2io11fxUChz9ytPBsT-Mgkr7H8sQFwjIF4KM8VtCvhGxrHvlq5OCTTw-Jr3i9SZj1Z0yZQwZLjVwXHfv1VGKmrhUzsv5PekWH_yasfiG1dBGnNmmEv7KWZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تحلیلگر صداسیما:
جنگ تموم نشده در وقت استراحت بین دو نیمه هستیم؛ نیمه اول هم ایران یجور زد گاییدشون که کل جهان خایه کردن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/79119" target="_blank">📅 19:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79117">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">یه بروزرسانی داشته باشیم از اتفاقات اخیر: محسن پاک‌نژاد، وزیر نفت رژیم جمهوری اسلامی استعفا داد. محمد اکبرزاده، معاون سیاسی دفتر نماینده رهبر جمهوری اسلامی در نیروی دریایی سپاه پاسداران در یک حادثه رانندگی در استان کرمان کشته شد. فرزاد جمشیدی، مجری صداوسیما…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/79117" target="_blank">📅 19:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79116">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">یه بروزرسانی داشته باشیم از اتفاقات اخیر:
محسن پاک‌نژاد، وزیر نفت رژیم جمهوری اسلامی استعفا داد.
محمد اکبرزاده، معاون سیاسی دفتر نماینده رهبر جمهوری اسلامی در نیروی دریایی سپاه پاسداران در یک حادثه رانندگی در استان کرمان کشته شد.
فرزاد جمشیدی، مجری صداوسیما که در تجمعات شبانه بار ها علیه تیم مذاکره‌ کننده ایران سخنرانی و از آنان انتقاد میکرد، به صورت ناگهانی سکته کرد و مرد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/79116" target="_blank">📅 19:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79114">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">به نام خدا
بریم سراغ پیشبینی دقیق بازی های امشب
۱: صعود نروژ
۲: صعود فرانسه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/79114" target="_blank">📅 18:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79113">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25d3fbfab9.mp4?token=WIL6212LxYNkpXNyTSBXVY7JnRhukCM44N9jSrTJCyfcY-b55Ei6x5HTWOEYxFiGySTDF91hKnH-0DuTaj0rk1Sk5YzUjtYFB2mdEYmCO-eHZxAEhvBebvMZZf54zsHSRKkhQJZmfNNE1m_K5my1IQ0jkpX4b--bGlyABg6Sxw6aiOQdHNqeGsIzrUvl_1eDX6s3Px1S8HOdl7_t882M5imogiXtr-ygFhFcwdFMSMW9LQXNFLUN7UAEzXRO2RQHD90MNJx4mPcZf1ENSg_nTEDvMGmn9Lmt5tt5nz-SLuFilL1OamCZ4PzDvQI5h6TDjodxuY3fmmHXlC4j7JnJTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25d3fbfab9.mp4?token=WIL6212LxYNkpXNyTSBXVY7JnRhukCM44N9jSrTJCyfcY-b55Ei6x5HTWOEYxFiGySTDF91hKnH-0DuTaj0rk1Sk5YzUjtYFB2mdEYmCO-eHZxAEhvBebvMZZf54zsHSRKkhQJZmfNNE1m_K5my1IQ0jkpX4b--bGlyABg6Sxw6aiOQdHNqeGsIzrUvl_1eDX6s3Px1S8HOdl7_t882M5imogiXtr-ygFhFcwdFMSMW9LQXNFLUN7UAEzXRO2RQHD90MNJx4mPcZf1ENSg_nTEDvMGmn9Lmt5tt5nz-SLuFilL1OamCZ4PzDvQI5h6TDjodxuY3fmmHXlC4j7JnJTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیزر تبلیغاتی جدید فیلم اسپایدرمن با حضور بهترین تاریخ
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/79113" target="_blank">📅 18:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79111">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qyfAZKositia2dttYPoTw_mHXUxEYcdogFfnz4MyIRkr2ANQliEIrwwDPHIWPYAkILrp6T3IvTBnZOG32QgVAfdXIOTpPtKgVqD55WCetso1TQyur7Eyp073OShsbC5yCZEsuGJoC67WeAWZgYHA6Q7e8gzqY6PsJrgLOgVYZPclsOs45Uk_S_NuuS7B-cnbArI6Dzu0NrUvHlLO5GZClIoBgSogYWkXGp37L24YDcWZu7UZ3U4936S0OQIxdAjM9pnLqHbxKVO1Ly1MZLmUcpVwHop0WH5AytjEq0ZdRQAQip7bHizlYd4Su4TvWiwBMYSpAS5H5sYf5mGziu9IMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا و ارژانتین رو هم حذف شده بدونید.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/79111" target="_blank">📅 18:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79110">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">شبکه i24:
ارتش اسرائیل در حال آماده‌سازی برای ازسرگیری فوری عملیات نظامی علیه جمهوری اسلامی است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/79110" target="_blank">📅 17:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79109">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHWUnkvlvbfzZJP_9hx-dUubASaTEW0fsol_qpW1XZ5BPD7I1rO9_laZSyj3D0gyam7tlvkUbpabqWGDvt70wRav0xtWG28BW3WCHEEo2O1_SKy76GpbZvLYOp0hkXJUYi-Xd3Lsb1kt43ip3aDX2QS9tfsLFGJNWYlx8W-8o3GCrDBVjxPZ6EDtVHduQu42Au_aR-hedAqbVTCUlkhva6pFwJm4j47x4gj65IBQuKQu2Du8HJr1pv3G_CHkPFZMKKijvxNCeWvDcmuidTduVyEJHpzi2fw1iTX59_fNw6D4oskUKw-Dp8-PcTF2mif4x7sFMY7ohaRUYp_lIHQw6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برج اسکم در علم نجوم در آستانه‌ی خط تورات که به معنای انبوه است قرار گرفته، اسکم انبوه در راه است
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79109" target="_blank">📅 17:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79108">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ttuus6K5UD4R-JqIZwg5FTxfUo8azh42uDytDPjK6PvU9U-2lE9tLOyxeMTGZJHXJrYf4B3ZZJBjKCGG5yJdeGKvtfyd0nw3NgrhlrPh1vJmVkJwlQdCJmd0mka7X-vsNF9XK1KrNfoFs-ywEsSydzq-q6pZjgnD-S2dJl-wQfyLu-SYUbzvJqv54cD5ZdpilD2Xhd1c2wB8h93cO_3PYxvR1Abm5TLjDcC6tsJXV16OuXmIK0B00h58AOYPneTS3cmCCtNmgh7ClGM3WSzCEDhRF3m-JKfmchJ8fFkAAhGUY7dQBS6XernHQeCJTgBx8jziD_ybXP5MhUgLwheU2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هفته توی ارومیه یه نفر بچه‌اش که دختر بوده بدنیا میاد و چون از بچه‌ی دختر خوشش نمی اومده، یه پسرو از بیمارستان میدزده و فرار می‌کنه. پلیس و پدر و مادر پسربچه الان دنبال این فردن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/79108" target="_blank">📅 17:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79107">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BztP5AthKfZ1-zfwwArvOJbJDJpAyiq5S8bQE0vrKBfkwVAel4lfGJaztsyrEvwlJeBnVcjOHKYcvvJu8r6arODLR0IjFUtABHO1YiGLJZTApVAHa0TGqO74soRTOg9ATOGBMsUwdtf85wPeBBoGxZIQF-LfHVypyUxJ4z7vtXzekVS88ton2RqW5ydPYJTb29QMJFQ0lWbHANtqB06hFpfg-L3W9A8yzd2XtlzF9nhNifSz7cclhyIwkZ3QhI_iL6NPxCsvc54-fGsYe_Jd6N7vDrYis5Zwe2nkarD9MTijfjgvYybJ9zT40ZKtsISBAwj8fONxhlsLXiLPeOrU-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپویل: فن خال سرمربی هلند شد</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/79107" target="_blank">📅 16:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79106">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oz-KX0806IRGep1Y29qAhb7gAd31v1xsH_HMCbc_5XUzMtlLrk5rIUA5PxcW0QjCO8SAAnRyU0nC2qZ43n7eKd9zkFjKhJWpqtViKtTkIRyQgcgrZeNdZ6z9qZz3Rb8DjP5SVRISwuhxEpfI84s3Nxxl8IeCyKIHYBfgYANd5vjr_1Dllz5QtJGwXD9j_QOCzv36CMB8jlXMay_1_noM-ObS2cqj5C-Pn89PP0liDjkqXvPVWLOZsXosu2a2y_1bWC0xc8d2SUwQQc6kBNs6ZMn8hMtEuP-T7ibjCAgOc6JUTCx8plWp-lXoo6vw07Chyyb8OnM_EbsK0XX2UOoMFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینو کی زده گاییده</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/79106" target="_blank">📅 15:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79105">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">یسرائیل کاتز، وزیر دفاع اسرائيل گفت مجتبی خامنه‌ای، رهبر جدید جمهوری اسلامی «برای مرگ نشانه‌گذاری شده است.»
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/79105" target="_blank">📅 15:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79104">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">جدی انتظار دارید آنجلوتی وینی رو بزاره نیمکت به نیمار بازی بده؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/79104" target="_blank">📅 15:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79103">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQdyQcOByDNbL4CQkPbuc1VUOl-Bi5GN1ZOdtub5jbQNM8wzmC_dsvGfnurmOLWzSeiJzqsczkYUxitOEic_2a8h5ZH1pWphauGClmt2O9woTstl6lEMOHAXNR-lL3-YRt1ZXJpY084bBRvNzrdz-HtlvEKsqh4UhVJktTgFWG0HKsXLgfXfC4W5qIY45iO5178Y-NOrh7n2Jhr3VTTF1zWLIXwyZ316xMp8YG4hsjp8EkyXsVjdfwpWjN3sEjTDrrRQmJuKL44i-rwGFsoGob1aCxMzGq1jeDbZZl_3tmDchMLs6wa-p-FRM6y5twykVqPCQbGO8GC01ChMYAokZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/79103" target="_blank">📅 13:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79102">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">شوک به تیم ملی؛ سعید عزت‌اللهی به دلیل ۲ کارته بودن بازی جمعه مقابل سوئیس رو از دست داد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/79102" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79100">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DF3lyVj81Ax39c_utQLllqZ7oEJCBfq4TrGMmUmn08w7-0S1DEbokmOYK3Qu-KKFY6Xcw7UwBLKzyxhA1s4yaK03vvImaGE9-jf4Zn03shkYVGqt9ZdCVyPp-POE79LQcxBeetlYsyvczXxOLl1CR1Ey1O7hC8VTIPheEvTqTdAMVNRmlnIgli0P8p_tgAfViUSlWnG9r-GMC9mQCujQrWzYr_bMmSkjZuEqqFGCjU_9EmSwcyVCCsTwGZF08hld8viohM2sI8n3KdLYg7bJrQyPvRgYdeuRxe9vbzzHYvFOX3kGn2BHPQob4c7-jJc_1kV4nG9L3TKS_obYmu7fHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این کونکشم داره آرشیو برنامه هاشو میبینه هرکیو مسخره کرده رو دعوت میکنه
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/79100" target="_blank">📅 12:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79099">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">از الان خودتونو برا ورژن ۲۰۳۰ مراکش آماده کنید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/79099" target="_blank">📅 12:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79098">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApejYAlbYC0XL9csK3hKN8kEsmHBumDaMTucWDzv75B6ccJA6nSMhu3ktSdxh4yHFtumgoNKnOMkrcREvgfbdN2clvsTl4FtbMAKI3ScgkwKktyDwHCOCTovYpvG8lI7L_i1q8l3HAxw421-uOBq6fN6ja2fjCr0zA_O-9Z5YV3z4pg0tBNzqBp3At8sTztxEtANQKLAAYnyfvFmjoz1meDLdut_rd3F67Okd4cX9a19OqP1tGmvk3-txLxxTmxK7fE0BwQD3hkK0RglN8UioV7BUAE75U3xIV9KzIV-GuT3EDIZQ2M71d3hz7ASbGuYK63jt8xItonSYtk6UtuA_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امان از کرم داشتن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/79098" target="_blank">📅 11:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79095">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">کی قراره دست از این که مراکشو یه تیم ضعیف میبینید بردارید و بفهمید اتفاقی نرسیدن نیمه نهایی جام‌جهانی قطر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/79095" target="_blank">📅 10:46 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79094">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBjAUtJJk_258w7ytB82628n4aTFI-Z2D8PfGuuOF_L2Eaj7vBnzYjydr1q9_EHiyOafvIoHM0gw6DDXWwsED6xlOimYSSZXQa471H8p-LiCvBT5xqvKcFL2DflqZhKXuH_v_t_rDrctSl9QrMuVCGobd_lNik91g3zuo5QFhjY9_D7WiMNPbjekiQt-s0EpgIxP2gZULShPzpBX_OpAyHOR34wT8TXzrBc8hhUEjNmNGuapcfudi38ay7ba6cJmLi7nTM1bipTy6FMIkXepVeGkDgq3nRsFb73vd3i4Vhe0U2bbUF8MBRIAI7pq_8s3vkDr1x1BIqN5m7ledsXnjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام دوستان تازه بیدار شدم مشکلی پیش امده؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/79094" target="_blank">📅 10:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79093">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">چه جام جهانی عجیبیه تیمای بزرگی مثل آلمان و هلند و ایران حذف شدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/79093" target="_blank">📅 07:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79092">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGJT3HIsdKzG2d53VnqWviGgZEbhSnT6vRzznRopy5q6Nb3Gwsgv165OTVuBr68U58a2B1KIi8xWr7huz5Rv8qaaTg4qmnal-rreNWk8gqTclcFPkENNYjeAOrQG86PYcNzLXDwVL9prwiGBGzsy2RfZxJ3kpTsM8_NCyT8EmOvK-rhBkspaffvwOwqMBViXUFdbAwukB8pSI3eEmdwKCKcaSHEulvsSPYNGut6Fur2O9dTYiPM9nBPQr3zY-MCyKbPxtqm5EZmYam79p4Xd82LitSvmoE3SRJtD3n7XAIilU9Ej5SRRXQu2tyDqCkKLOSHej4eK4Y7YlWBbNh9MvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سبحان الله
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/79092" target="_blank">📅 07:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79091">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">هلند هم حذف شد
😂
😂
😂
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/79091" target="_blank">📅 07:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79082">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">فرید خوش چشم نظری راجب بازی هلند مراکش نداره؟</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/79082" target="_blank">📅 03:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79081">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ناگلزمن در مصاحبه بعد بازی:
واقعا نتیجه عادلانه نبود ولی خب اینم شاید یه آزمایشیه خدا داره منو میکنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/79081" target="_blank">📅 03:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79080">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دیگه هیچ نماینده تابعیتی و ژنتیکی‌ای تو جام جهانی نداریم
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/79080" target="_blank">📅 03:14 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
