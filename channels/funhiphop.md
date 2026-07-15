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
<img src="https://cdn4.telesco.pe/file/lNsezOxA2BHXfY6tRgOFhECqXX5ssgKeCQ-EQwdmZv1AtCTmpoEASS4_0m4s7dY8Lo-txw1bSOIgvI9oTcj0j5lFWtD9fjbGmiBzwUBsxCFzqO5mCruOQr9LKjqjU4MK7J_bvEMy49XgLGxsYhlpPY5yl_0FiEN-MR0aABDFVWR2BPr3H4qicfQrCmDiepWsPiyBtPvmNBkmvmGY_7iLZbqhCalV_tXdogu7hF5ls57LG3NxaTPy1T6hJt1soh72eys9kSU-_MfCARxdiNgQFkpZSY4e3gfUz9bDSLBUy54n-dM-upj3ea1--iESkonEEi5ax-8YsHvZGSbuHFbwjQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 195K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 16:18:20</div>
<hr>

<div class="tg-post" id="msg-80400">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترک جدید لنا و مهیاد به نام اشک ریلیز شد  Spotify  @FunHipHop | Mmd</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/funhiphop/80400" target="_blank">📅 16:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80399">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QlfA_KT3Tt3cZWFBYiXKVkFBphNY2J5Vbwh6dQgDTJUopUuA5bsVaKf8gJjAtGOWsay_atkgBaSu33HPv_qXAe3SPwWDbBsr1-OpOx-rlHxdx0HboLnIQpNGYF-q87eSA13p0VTGHi3o4ds6S7bVyn-J6QOXPvEql0XMR8oAmv5OLNnGf8HwpMSheWV17nTi1iDk7w6fl4EaRWBgkPxfypWa_iFyXTLeb3KpCsRLmxDMQ5ibrs9OcWlnqe5YuzcizQS--lL3si0GlwD8ggLGQmYAFT5--Sc9CebZG9tjT3ZVVpQTFD6vFSKXYqkQT05v7zWpsVN1k6EA0dTL4_Lzow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید لنا و مهیاد به نام
اشک
ریلیز شد
Spotify
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/funhiphop/80399" target="_blank">📅 16:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80398">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">عجب ترکی دادن لنا و مهیاد</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/funhiphop/80398" target="_blank">📅 16:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80397">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTrL3-0lfhkxwJoLq8uL574VzwxlI0OMy76hSRMKLz4xsImHNzWGCQaukvNj2fP1eudmO73xMldo8qIi1Evvk9wPc7S9TK-mHFfzJbY3Fjf7qFJWo9xKRLeIaqAHWsjuY2VjknSVQ-59OCfXXC1L-AQF4R4jYCHL8Zl9P3BgdvRy3zQwHTrrtyev2dAOaZoK1PC6O3NCZqURyv3fuxc-yZn_Zp4jDS3YkC4L8mXYBzasDuKb_xY-8TWZA0IAoDswjWeDrPDhjl63sVvLMMwzCsnxLD_SHj5797k1uVc1MmpCd63hLhPEndgeQf_2X6PpcPNhD6-YeWJwbjc5oMKEwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به پیر به پیغمبر من خشخاش نکاشتم، دست از سرم بردارید  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/funhiphop/80397" target="_blank">📅 14:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80395">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">جدی مملکت هیچوقت اینقد رو هوا نبوده
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/funhiphop/80395" target="_blank">📅 14:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80394">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">امتحانات نهایی سال دوازدهم در ۴ استان هرمزگان، خوزستان، بوشهر و سیستان و بلوچستان لغو شد  @Funhiphop | Farid</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/funhiphop/80394" target="_blank">📅 14:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80393">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">امتحانات نهایی سال دوازدهم در ۴ استان هرمزگان، خوزستان، بوشهر و سیستان و بلوچستان لغو شد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/funhiphop/80393" target="_blank">📅 14:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80392">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">که اولیسه و امباپه و دمبله قرار بود کوبارسیو جنده کنن</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/funhiphop/80392" target="_blank">📅 14:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80390">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">زمان جنگ میگفتن نیروگاه بزنن هم ما برق کم نمیاریم، حالا که نیروگاه هم نزدن روزی ۴ ساعت برق نداریم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/80390" target="_blank">📅 13:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80389">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">تا کی باید تاوان جنگ طلب بودن چارتا پلشت مثل جلیلی و رسایی و امثالهم رو مردم بی‌گناه بدن؟ دیروز بچه های میناب امروز چارتا سرباز بدبخت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/80389" target="_blank">📅 12:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80388">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">حقیقتا تصور خوبی از این که همزمان با محاصره سیلو گندم میزنن ندارم، خدا رحم کنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/80388" target="_blank">📅 12:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80387">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">محمد امینی دهاقانی، از معترضین دی ماه، متاسفانه در بامداد امروز اعدام شد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/80387" target="_blank">📅 11:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80386">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">با اعلام دفتر رهبری، مجتبی خامنه‌ای روز سه شنبه در مصلی تهران برای مراسم پدرش حضور پیدا خواهد کرد.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/80386" target="_blank">📅 11:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80385">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">وزیر خزانه داری آمریکا اعلام کرد چند کیف پول دیجیتال مرتبط با بانک مرکزی ایران را تحریم و بیش از ۱۳۰ میلیون دلار فاند و بلاک کرده.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/80385" target="_blank">📅 10:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80384">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMycaFqEqKacy73Jn3yRvwmtlYkbh1VhxclVB0hbatgXczb9s9v8ATk2St3TiTwUEmTuFTi6lAQrE-l336VnxHu2K1hw-DiA0C8Ofcl1yfX_Myw21YuG1eX7OJdFgn3mq88yV26TaJBQx0mSUz9vcgd2THng0hvvK7wngQ_QIrE3N5UqWN_EaXJx5EG1flBiO03xAOSgKHdzUqrPxvwsdElxoe5TJtD_5zyOK8nMMgn5u4d7_GRrvWTaHZyQFGUsHbNp_EI00diO_Cp4TDngnBuv9eNPQQSz6YfzrnE_Z5_EeNoz0ODQEAnUuxGlsbnq5iEroqcynFVgaPtLG48-bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوکوریا تا الان توی مرحله حذفی جام‌جهانی یدونه دریبل هم نخورده.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/80384" target="_blank">📅 10:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80383">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hMi2z4ClKSpIN3jQiGBgfb_xfqBuSGeqiDMY8UtD5lmy-ix_TWkDOffi6NqBPw-IFCA0xXuFDWmOTquaQQYRip6Jaz9_Lra3TC9y_tWs9j3C55hfYr8m6GllcZC4Z7lItNHHgZ5PQ1BxEQkHAfSNUwTv1SY0kR3OJfMwBee_mxIhOLPX7rdbR7tV_f38ud4AdmStDDUoBj9nc_ggZUDE6B6E1IOoLIBPntNWNFrG6yHluoJ-aKQAQ8WUptmHQCaiVd2P0qjoPnpNt8L3J0-8K2tNGZ8PBiRU8Md8aa7UP8VsjZegqzOyiMfqWL5OeM-c9uMC9oHFgGuZYpncUC0SFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید داداش یامال و طرفداراش :
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/80383" target="_blank">📅 10:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80382">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dk5b33Kmknr7ZsM5ESzohBYHfeN2rtDUg9Ya2I8qfvV_iYPSSmJrGmb6e12to_P7gW5qxZdej_5UVombXnPXzije3zLway4TCZQIWCZ0oYv8eggFx9ezyX9AtDo0IhqlKUrnfJ_BAmNCzpc-oViQSfIopI8w8oItrQsH39INvS0vZgfu-86b8YziqVISEyurNNe65BxM3hc6IF5TdKW-YQH1WPO37wKHJ1mEqAfNwkhY3A3_Qm5Nwo_vdzIuxj2uImW5EBDIkO7gBKm6aSIeQ4ew0ZM2_dqCLNCsBCoQO1Feoifch26a6n9pdsztSh64-FiRAIJAiEWfygt19R6BeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
-
🇦🇷
آرژانتین
🏆
نیمه‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
چهارشنبه ساعت ۲۲:۳۰
📍
ورزشگاه آتلانتا (مرسدس-بنز)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
‌‏
⚽️
نکاتی در مورد بازی‌های رودررو:
در
۸
تقابل اخیر دو تیم، انگلیس موفق به کسب
۴
پیروزی شده، آرژانتین تنها
۱ بار
به برتری رسیده و
۳
بازی نیز با نتیجه تساوی به پایان رسیده است.
⚽️
حقایق داور:
🟨
میانگین کارت زرد:
۳.۸۴
کارت در هر بازی
🟥
میانگین کارت قرمز:
۰.۲۶
کارت در هر بازی
🧠
بودجه‌ی تفریح از بودجه ضروریات زندگی جداست.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r24
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/80382" target="_blank">📅 10:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80381">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">جمهوری اسلامی ایران اعلام کرده زیر ساخت های استارلینک متعلق به شرکت اسپیس ایکس جزو اهداف مشروعش خواهد بود.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/80381" target="_blank">📅 09:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80380">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">متاسفانه طبق گزارشات، آسایشگاه سربازان در ایرانشهر با موشک هدف قرار گرفته و تعداد زیادی از سربازا جونشونو از دست دادن و آمار مجروحین هم خیلی بالاست.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/80380" target="_blank">📅 05:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80379">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">متاسفانه طبق گزارشات، آسایشگاه سربازان در ایرانشهر با موشک هدف قرار گرفته و تعداد زیادی از سربازا جونشونو از دست دادن و آمار مجروحین هم خیلی بالاست.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/80379" target="_blank">📅 04:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80377">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">روزتون چطور گذشت؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/80377" target="_blank">📅 02:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80376">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">باز که شروع کردی تاجر
ترامپ: ما امشب، فردا و پس‌فردا به ایران با قدرت ضربه خواهیم زد و در مرحله نهایی، نیروگاه‌ها و پل‌ها رو هدف قرار خواهیم داد.
اگر اونا با بازگشت به میز مذاکره موافقت نکنن، تمامی پل‌هارو هدف قرار خواهیم داد
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/80376" target="_blank">📅 01:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80375">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">بهترین فرصته ویناک هم با یکی شرط ببنده سر پول جیگرای اونشبی که شاهی با دوس دخترش خورد و فرار کرد
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/80375" target="_blank">📅 01:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80374">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اینام میدونن ویناک نمیگیره هی دنده میدن به همدیگه
اگه خیلی پولدارید ویناک نگرفت 333 میلیون بدید خیریه با سندو مدرک
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/80374" target="_blank">📅 01:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80373">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اقا رپفارسی درست شد
ادرویت و شاهی رو بازی فرداشب بستن
هرکی ببازه باید بدهی دکیو بده به ویناک
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/80373" target="_blank">📅 01:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80372">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/80372" target="_blank">📅 01:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80371">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">تنها دلخوشیم ویسای شبهه علی داییه
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/80371" target="_blank">📅 01:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80370">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">دیکتاتور بعد از باخت سنگین از شدت خشم به ترامپ دستور داد به جنوب ایران حمله کنه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/80370" target="_blank">📅 01:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80369">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سرنوشت دیکتاتور سقوطه امباپه جان</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/80369" target="_blank">📅 00:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80367">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">بارها گفتم تو فوتبال تا خط هافبک درست حسابی نداشته باشی هیچ گوهی نمیشی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/80367" target="_blank">📅 00:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80366">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihOrlXsHWtm3AZExh3PMXESKCvC6UdaTEfF_DwSSgdHj108Pwf_3GfJu4DkcwSqUezGcxS8B_uH2EtkNe7jVbqTEjMhRpfvaV5kgSn66eP09eItsUHirAXv-Jsqq3nL1vQNKjJoOVQTt3aa_YCGiZan7zJvP_WuKQoR-gZyel22ZLkzJc7qp3eHdUgmT0RaY5kEsQ03q4F0lEJEIUuL8hqLVnyU7c6TuCK36JzSwlY_IvKJrqrJnooM18d4Q3vZArf-S-BHBmKwQsiWD38BoypGf4MkaClFjEPfC44JvrgTASbKkUCtepFPAoeY5Ah_MLdKRnREDTxQnX7sGNQBV0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیرم تو این بازیکن اسماعیل، کیرم تو این بازیکن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/80366" target="_blank">📅 00:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80365">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KFkVjx63JQb6t242WdpXfcvho-SzzM95KWdQXKaMlf_9n57s-pfhn1Cy3T5_BdjBQgfUI96_cMjZZvxnhFN8YcP5B9OnCo__msof0j8-MDu4wgM0BT8VTv9NqemI1RtB8r-cWHOVTWo4yz3bCtP5yNuj0k9isy3KQ-RTY8i7KhrGsLrD_FQZOzEUlQ10_l01S9RXEmVMSdxVzTeYvwwRgnLItGu3OtkpwEM_snTQC2HknOphonogJVed4Lc5qGxofSce3HaSCFdyy6ffzXw7fHyBbAxR82cMWCEeeE3g8klVagbawhQVxFBy_XG2I7qDA0AewRTWRA4_gqVFfAxOeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه برگشت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/80365" target="_blank">📅 00:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80364">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">سرنوشت دیکتاتور سقوطه امباپه جان</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/80364" target="_blank">📅 00:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80363">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">با اختلاف این گوه ترین جام جهانی بود که تو زندگیم دیدم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/80363" target="_blank">📅 00:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80362">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">امباپه فشاری رو
😂
😂
😂
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/80362" target="_blank">📅 00:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80359">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">امباپه دیکتاتوری که ایستاده سقوط کرد (رید)
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/80359" target="_blank">📅 00:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80358">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSajad Shahi</strong></div>
<div class="tg-text">سنگین بستم رو فرانسه</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/80358" target="_blank">📅 00:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80357">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded froma.r.m.27</strong></div>
<div class="tg-text">از وقتی شاهی گفت سوئگ دارم مایکل اولیسه یروز خوشم ندید</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/80357" target="_blank">📅 00:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80354">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">گریه امباپه ضریبش چنده ببندیم روش
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/80354" target="_blank">📅 00:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80344">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">چه بتایی که امشب لوز میشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/80344" target="_blank">📅 23:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80326">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سلام آقا فرید همین الان اهواز رو زدن
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/80326" target="_blank">📅 22:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80323">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">امشب اگه فرانسه برد نفری ی شارژ بیست تومنی ازتون میگیرم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/80323" target="_blank">📅 22:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80322">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">جنوب، همون همیشگیا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/80322" target="_blank">📅 22:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80321">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">بارسایی بدبخت شدی
دیونگ چون جلو مراکش با مصدومیت بازی کرده رباط زانوش پاره شده و نصف فصلو از دست داد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/80321" target="_blank">📅 21:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80320">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اگر دنبال یه پلتفرم کامل برای فیلم، سریال، انیمه و انیمیشن هستی، وقتشه Meowvie رو امتحان کنی.
✨
امکانات Meowvie:
🎥
آرشیو گسترده فیلم، سریال، انیمه و انیمیشن
🤖
هوش مصنوعی اختصاصی برای پاسخ به سوالات و پیشنهاد محتوا
🌐
نسخه تحت وب (قابل استفاده روی iPhone، iPad و همه مرورگرها)
📱
اندروید
💻
ویندوز
🍎
macOS (Intel و Apple Silicon)
📺
Android TV
⚡
اگر فیلم یا سریال موردنظرت داخل آرشیو نبود، کافیه فقط درخواست ثبت کنی؛ پس از بررسی توسط پشتیبانی، در سریع‌ترین زمان ممکن (معمولاً تا ۳۰ دقیقه) به آرشیو اضافه می‌شود.
🇮🇷
حتی در صورت اختلال یا قطع اینترنت بین‌الملل، Meowvie برای کاربران داخل ایران در دسترس خواهد بود.
🔥
همین حالا می‌تونی وارد Meowvie بشی و تجربه‌اش کنی.
🔗
لینک دانلود و ورود:
meowvie.ir
@meowvie_ir</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/80320" target="_blank">📅 21:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80319">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">خبر خوب برای دانش اموزا
آموزش‌وپرورش: حوزه‌های امتحانی نزدیک مراکز حساس و نظامی جابه‌جا شدن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/80319" target="_blank">📅 21:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80318">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">طوری که بحرین رو زدن احتمالا امشب تهرانم میزنن</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/80318" target="_blank">📅 21:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80317">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">فرانسه فقط حملش سوپره مگر نه خط هافبک و دفاع جالبی نداره
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/80317" target="_blank">📅 20:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80316">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgqGCMyNtDWyedc0umZDJT_WoCs0NzfZxaro2zchlRr8kdqPCh1ipu7-aWIJ_RAcsnu0DPd5LSNMkUIxtlRDK1zPEDce4ArgHl07ohDodb9ZMSzprOF4Jf0X5BQvt2S7vmWVyZR8wi_ebmPVT5cKPg3pLRkylNfA0MzeExcIrNmnjh6OBwYlFRKQTK5SdHnsLwxdHnE6eVkvhBUdFJVLXDMdhmDxztSjs-D_gWjIElm7vCymnG80F5dIWJgMU7jdItbKnXDipiWYnDeOyGpYQ03bmiE-dbSqgFgDGtrfEhsXJLcmo7A6vtotUIHDHLF_58ehFjoJm4KaXzIKzBbf1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب فرانسه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/80316" target="_blank">📅 20:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80315">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gURlkB91p_WxsNEeHnnNGzn79WHJ9tKuBk3N1_EM1xskEwrMOCWJajAyt4w4bvuWPEtVszrc6WtqmoDlR8o2bJysZPqpDrgE0J2FxdOoHk7C--yqZlJQK3M8cTJIDZiwTiPpAVxhNGSxSeqJOvFpul4RUkggLvTCJgoX-aWU1GPhkRW2J2dLuPvCZnxaDUouFEz3IsvHXDS8fZFGvDNTL2iXgOTqxOGBEtPO8XgbHTTOSNryKsumFDYrXGvx_to62KElhDPpxFVYsDiYUgrVn7XmCb33Tj9dpxNwbL9WvZ_bK_Rge6-B9Z9BEmmJWDHNJE01qpOclNECtOcVAXOJwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بابا کصمادرت با این ترکیب چیدنت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/80315" target="_blank">📅 20:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80314">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">داش میدونیم مادرت کونیه لازم نیس یادمون بندازی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/80314" target="_blank">📅 20:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80313">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">یامال باز استوری گذاشت، هر چی دارید ببندید رو صعود فرانسه.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/80313" target="_blank">📅 19:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80312">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96d014ea48.mp4?token=gR9t8fsxM7g7QSHCmebZGdwWvfnfDvUjHF2Na0dBLgdk48wjg8E96EI2rclHXhg3gy5lUOCwnKfdO85S0_OP3T8wXI7SxbVzfxyOjmjcm8b0rszEWFGQA9Raum1P_OcyHFtBbVm4bhXZg_3J3BygYsW99qbsbccU8XsrgY8Kq9j7K8lFFzCcuScxMe3VoHzaqn4e2KtfBlhuqzAyNafVbTYwU90d5gUEq0hv58VynCp-DoVkdcXq566OnRKxHdlA1GVDKIjqhrjHGE_4NLJ94FGFaQ8wQQz0drnBg-gE1zZhk-cApnO2hOzP8MN6qAwGQ30OWSty0XUUz0oIBqhKKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96d014ea48.mp4?token=gR9t8fsxM7g7QSHCmebZGdwWvfnfDvUjHF2Na0dBLgdk48wjg8E96EI2rclHXhg3gy5lUOCwnKfdO85S0_OP3T8wXI7SxbVzfxyOjmjcm8b0rszEWFGQA9Raum1P_OcyHFtBbVm4bhXZg_3J3BygYsW99qbsbccU8XsrgY8Kq9j7K8lFFzCcuScxMe3VoHzaqn4e2KtfBlhuqzAyNafVbTYwU90d5gUEq0hv58VynCp-DoVkdcXq566OnRKxHdlA1GVDKIjqhrjHGE_4NLJ94FGFaQ8wQQz0drnBg-gE1zZhk-cApnO2hOzP8MN6qAwGQ30OWSty0XUUz0oIBqhKKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسئولین بد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/80312" target="_blank">📅 19:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80311">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aefqbpYfKQh5Bjm2QWNERi62abMgrZteQONazgF7pM-JZpU4T6VOivcS7Kc71CK6OIaa8G1hj9hTP4sPE3BZslqjB6MULWCaXk9BVFm8dTtHexXtcBAaTSVx2aob7r8a94-k-i2in2-RzAs70ERM5QOmC4QJuON9WZkjExTgD147K4olqy4bGAAlnvD7AN8_dRtPPBUAZlzKaFpPULoGLcpnEftP9DGePP3g_vN2RwQ4bWXh7FZeSL7cpRVoz_pGnLpuVsKDmDCyQHgs7nq4Eir5liJ3rCKLsn2ps7OVvtp8RO6hRQ2tKq1QCCwxdHnbzO5Ws9AAlQV-iXCaAUwCug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یامال باز استوری گذاشت، هر چی دارید ببندید رو صعود فرانسه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/80311" target="_blank">📅 19:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80310">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">هرچی دارید بزنید رو صعود اسپانیا به فینال جام جهانی
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/80310" target="_blank">📅 19:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80309">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">بر اساس تحلیل های بخش نظامی سازمان فان هیپ هاپ، در موج های بعدی تهران، سمنان، کرج، مشهد، اصفهان و تبریز به شهرهای هدف حملات آمریکایی در ایران اضافه خواهند شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/80309" target="_blank">📅 18:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80308">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">بنظرتون با پنج درصد شارژ میشه ۷۰ دقیقه دووم اورد؟</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/80308" target="_blank">📅 18:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80307">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d49901ac45.mp4?token=FYVlY6Di4FICUnQsnf3BdcX3_1FcfrclSF0z4F-tGey4plKlG0daPTm_ZQJAf5uz9TnJmDymbZZELHj-_PWeO6YK8m7XwNsEW-jVcrsW1WU_GM7FiZTPkzU-PtJjPwkMHWx4Nc-dzUraxXFLTMNzV7sfywq4F5D34QBIMLv-RGTWskHEBXf_w4i2YyY3UWLI3URbfsWskvnuHWOtRNmgCjVGpnltyN3eHZyzJYXELeO8S9QChAUSFVPbpqr6u7EUf0-oHoSKR2inIvQ7NsJDul6ewKFZBmmMTo22kNolqXHFHZPzlFtf5ONYjxs5WBuYLpGxtK-lWm8lOYYOxmjCjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d49901ac45.mp4?token=FYVlY6Di4FICUnQsnf3BdcX3_1FcfrclSF0z4F-tGey4plKlG0daPTm_ZQJAf5uz9TnJmDymbZZELHj-_PWeO6YK8m7XwNsEW-jVcrsW1WU_GM7FiZTPkzU-PtJjPwkMHWx4Nc-dzUraxXFLTMNzV7sfywq4F5D34QBIMLv-RGTWskHEBXf_w4i2YyY3UWLI3URbfsWskvnuHWOtRNmgCjVGpnltyN3eHZyzJYXELeO8S9QChAUSFVPbpqr6u7EUf0-oHoSKR2inIvQ7NsJDul6ewKFZBmmMTo22kNolqXHFHZPzlFtf5ONYjxs5WBuYLpGxtK-lWm8lOYYOxmjCjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداش لطفا نخون دیگه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/80307" target="_blank">📅 18:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80306">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">میگن پرستاران و کادر درمان در شیراز و یزد دست به اعتراض زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/80306" target="_blank">📅 18:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80304">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YVTu0dF_pxX8bSTduacDbDaRabGF1GeN9pq6QDA1iuOTHB16RPVrsn3F0phhrbdj3h5fwss8cwAzxrv_eSuSW2meCHJcWkUYY2B0tBtVfqfx4gtLHEuGixWoZwr7XLzeXurYVG3Y_Q7gvAeWubMehPCt249VOIXUq4LEj6x4jlq1X5YC0VuGlQkuGCuB2TrJCfo-FdADe72bdVxK_o-s5w0-9b7XjgFRt7cNzI7BIgLxp7NxF7HEkcQyhbcgo0V4kWjEjrBHkqI83JqHTWv4SZS1PWrp2A68AkdJLbYQwztdbwPKStvrnJAQBX2AbAG5-MybIX7h_y2Fs3F6HUe6BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/drDeW6aF2V_2yrHk5gBXsy_ahh-afp6OezlmZvnIf5ArebmWiqfemlMLm-V3DB6oTplWILbKx-feNLvhthjx4cbUHWLYA5eadldG3EldVHGDo5tiE_RZH1NoUCdRUJFGF7YZebEwC4jrQTd2ry33Y-pblq7FUXvudfhf_duQ-izTijayDz6z14sfHkZLZkGvm1YAEBjKlTjK1WZQ-8N7zJUnspYmRxPY_R7_42MaJ-8qIc-qOUfbce2N8yxTc6cwzXdIeVkNPIQSSUtOmfrvhedG45Lkk1lEd59Cbzj1t4g5CfaVycC3L3du9juLwvJGL_xjXqNVrg4NilmqZUHz7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنیفر لوپز ۵۶ ساله.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/80304" target="_blank">📅 18:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80303">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HhHFel5oqk_eve7socBbcDFX6eSiBh1u1AM33jAEMSoGf88upLymq_T0Ate3LloZ5HYRoEo16WctXJ81nDaI8cTEPSnzT1at2Tyz6NzPVkkRufast4gW841A7gwWQKw28yQu9PNcGMNaX6DX_piTqv0cgWm3wMtOjHrvKS-1gn0pbM5JHPwwFFeR90Er7fTMLNJaV9s81QLu1GK3iDx0G-_iqqZhO64cDm_ZAqXuwUgK3BdzgvlJy_wz3ZB7vrAXJ4iPFY52mkhQpHuuNeZGMgDRSVdyhIclSHPHRJwvc374TeKqr2lIvBgovRjcaNrBKFb2fR7zdvW-OGvYaP7ncg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
فرانسه
🇫🇷
-
🇪🇸
اسپانیا
🏆
نیمه‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
سه‌شنبه ساعت ۲۲:۳۰
📍
ورزشگاه دالاس (ای تی اند تی)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
✍️
اطلاعات و شرایط بازی:
- فرانسه در دور قبل در یک دیدار جذاب، با نتیجه دو بر صفر مراکش را شکست داد.
- اسپانیا نیز در مرحله قبل موفق شد در یک دیدار نزدیک، بلژیک را با نتیجه دو بر یک شکست دهد.
- برنده این دیدار باید در فینال به مصاف برنده بازی انگلیس و آرژانتین برود.
- با توجه شکست‌ناپذیری مداوم دو تیم و نزدیک بودن بازی، تساوی یا پیروزی خفیف فرانسه گزینه‌های مناسبی هستند.
🧠
وقتی بازی با فکر انجام شود، باختی وجود ندارد.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g23
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/80303" target="_blank">📅 18:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80302">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zqz1zfF2lhW6AGamgRuyaBW8tHmVSHpA8VSI6FO77xIW1UvK6ITGoNwGJi0FHGf4zEaB-usM3YFc4ySjRY9ypNOW1fDf4Af9IKC3UOVuEYE-WIS6bId_VZ2TxHQX7b528MhiajiUn6wNIfSc3yKQWZ_Xx2J9_mzZPbobULZTaBP43EazEneOQaOPgMIbSYoMwJH86Hw_x9QQ-Ruz3sRrFhgsmNy4FpQ5zbRK0EGFtSZq5pucW97K8ose-T_eluu4dFL-oPfDP9OK24LoSFCF-5iG8KxzI1TY2UkLD_yNz5r4oGplimbzA6l34ymBUGVM6p8WY0X8nOkqkGlOo26X5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوه اوه   @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/80302" target="_blank">📅 16:28 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80301">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxoAdfuMVQqDXBg6Id8QESouMATWPGMwvGTWqpGBfAWrIwyoYElenmI5FFO47HBfBLXUrGKl7TPtGT5PECtCFYikd5rY4juU_mfAXawGYsFGo4IvfuOj43Gz08mta3a9Np9MMkcUvvnz51Kr8eOM2DATrNB5HBaC6Ya7k8C2dGUZ879zIrc46zAyuVSfWdD8fqo0rmNL3t_J3Kq9QA9NTClcWQsgGgarsi8N5qkhn6sk8U6MgH6D-m6E5RyLg404neJQRv0HInPQCWkPplZVjy0u4Al18RgxfP9JUzCmdRb52yh7niYJdX37Q6MrmzgkbRUl1B_-hzLHFv7m24ReSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوه اوه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/80301" target="_blank">📅 16:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80300">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6dPJEhmj7NLsgi4ekDRApRaxYw0xVJZq3Pup8-OZcxH0UyfNXn3nWqhOt8wKRxf-Dz4FB25LARQS5YHWaGmieKqBFbg-IazEaSwg-omrV4XkdQqHzDEv8pPVcClzm4H9cZLayIbXPHWREDgeu_Sl_zUSsc5cV2dARZOGJm5N3LuhX8O1OMcCSU3ScihEf15dIQ_DPONsihrA6RZJtkYgqAuQJIqhldRn8f0-5pKVXZICj9NzbKpBiQOrpRvAowxscckppoFna8jAPaFvUf3xk45vRsN0AKngpnuOijjVjAz5th08tTtHgQMQ7l2KnZ7X1BB8VC-U9Yfqg_CSFh9gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/80300" target="_blank">📅 15:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80298">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v86oINZcNVYIc1WVdkYNHjMJxXNZGbVwIiXGKVDKOSh4Ldrmv-_qzTF787aqfr2IK7iqIJ8ZvMP_Iot3Z6NyE9luGmhr6F-ywPF7CwOsZ8-lkJ8NKftEI4j6jtnGLtXhIqVwLxstbvyD3UXDkfULTjqYm_7Acm58PeChBAPtnyHLlBxK1l_IZuQsJhwAAPL6wT4s6YIt8puiz6FRVNxXb4K7Dqm8StLbSwYRPWXEZLfyGKltbk7wKOn9gwJPeP72_8_36ETr2JLdGSqu6w8fs6-bN-3Q9V5mdt7WVNgb9WLtmUGDOj4oQCZimffBKKzB7IabFTVeAT_vW0fBLKQMyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JLexSyTrXhPOobO-l9ilyUvrxNDQFm_PMgOrxF39oBSNTUIVKVhl329QOTtxivBLnp6k-u9kQGNEtpw-O40jUJGa_tMCEAJB2Qf6sXdCL2bmpSpYedOZM7DS_Ql8uzmgRmF10GbP7roXRs2r1mnORapsGb6ZK036E5NQemCR6ROLD9bZHB9UjYaKOT-7Bp5iENj3qvS27LOG9j-pYHYSoHjrnpneejydabm3fA60zJ3tgcoJzH3AnNGvJ9AAHjwcdO6eyiSgb5p-QxQPc37novEPzvUA_yC3lkR79TpdJQdcpAyRx4MqnayPYgv52iWhMnV4OywsqCNUa_dhdG0Kkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/80298" target="_blank">📅 15:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80297">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">امتحان ادبیات امروزتون چطور بود؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/80297" target="_blank">📅 14:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80296">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">امتحان ادبیات امروزتون چطور بود؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/80296" target="_blank">📅 14:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80294">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">الان سکته میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/80294" target="_blank">📅 14:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80293">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">Shoti ke vinak az chateah ba kagan pakhsh karde.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/80293" target="_blank">📅 14:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80292">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">چه فشاری شد حاجی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/80292" target="_blank">📅 14:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80291">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTtSgk-QJC7MqnnATdnkduFJTJRNVMPRRhJupiTztrX21vtT_WCc5x68DmwIio877bQyn7EP7u6DIatfh74iE1-8c2qQnkijK7k-8Xhch68gkL-kzHtgz3UrlMiJTEATnaRc0CKXZELtcE_pS0fd_DV0XO9vOPcBKFnQAxrXTiD4dlHp2se5FTxaLLCj3kE74po_vQ_qaEl6CRvRVtlV9qmC6vBpFxCRP9XYeW597mlmSXnV8UFjM7C8rxBxg6rZ1LA_CnS6kZJRqm46Icr9K0XqNW0iobxY-pejv1JiqJuC118OzQv1eS_QEP_B_Iq510GOAszYbA4fruzpt_vR3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Shoti ke vinak az chateah ba kagan pakhsh karde.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/80291" target="_blank">📅 14:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80290">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/80290" target="_blank">📅 13:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80289">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">پسر دوش آب سرد بگیر
😂
😂
😂
😂
😂
😂
😂
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/80289" target="_blank">📅 13:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80288">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">مامان عمو پورنگ درگذشت
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/80288" target="_blank">📅 13:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80287">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ Fun HipHop ](Young Arash)</strong></div>
<div class="tg-text">امروز روز فلانه و کیرخر‌.
@FuunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/80287" target="_blank">📅 13:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80286">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">انفجار دوباره در جنوب برای ترور مجدد چرسی در جبران ترور ناموفق قبلی.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/80286" target="_blank">📅 12:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80285">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">حرفای ترامپ بوی "من همین الان یه تماس از ایران دریافت کردم که میخوان توافق کنند پس یه فرصت دو هفته ای بهشون میدم" میده  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/80285" target="_blank">📅 12:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80284">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">عجب امتحان پیام های آسمانی سختی بود.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/80284" target="_blank">📅 12:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80283">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/80283" target="_blank">📅 12:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80280">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">حالا ویناک که گوز کونی نیست ولی همه این سلبریتیایی که دارید ازشون دفاع میکنید وقتی ایران بودن خایمال بودن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/80280" target="_blank">📅 12:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80275">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PVCsmSvbJ2M9c4zMriQOROZN1hudkf4iDay7XMN3FiAFG3W9tko3-DSxxY8ccSzFlqyuwqm9QGeYqBYO4ZuCBpe9VrQB-gnMJBGfAnXz1OKgY16k7XwUCjySAOl4CBIxbIA4Mb68uAeFWf1FQ5Oac4EUNsmAHwf-8RVafxDiDZ1x0TEu_-77B-NW3lHwxqVPSlqjjRnMCx-QkHa_lrajuEQNTsX2OiBNSKI8yYHuC-oZZCU9M0thKGOd8OIi2B4uOl4z3aWNa1WabNn5R6IScXZ0GUArbk2ZjSYr3LRUMk2gmktcwSQyl3czmJdTSWNRzGJDPGiJ2CH984x74KuAsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hy3v6QAfevethvOK03yk28ILhkTKKAyOA_f8E33axg7HDeR0Gd0-x8u8nzUnK9y-oS0bQzDkkxlZqODhga5QQhbZ05sf3UO9euj6qwKKI6IntEyviqLFQEUW3PpjND4IveIJvvDc71KIFW64U6Llf7Fwwiiz0p9a1WraK1O2DG5jE0tIzHJt7YZIhz1UawMT4K49eGaJQQpNzXYju-uwt9qg-UFGs1ugjmaUrenBzpmf94R5gMBvN55RpAqkE6QtBZPzM_y5vv1k5K9_aJ-6HeV5mA2Ts0xseVSq557r6fDgLDkRzZhX43zA9eHCCiGTWZYfIm-1UX5IGP5j9Hptdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iCndelyjuoaFebiQuITihKNY2F0Ut7BhPAXzoeB0fgrFHt1Dq2-10Evxiff4ueCsXxbVqQE_Ks6a0m9eFtZ6fVcZuEVhCE3mCLSACH_jn4kxv8hYrZGXL8URya0WZlzhHtPuFqEc3kiJmm4ksm_oY3Q-HV4-1CIsncH4HTb5ifGlGPGK7MgjyNVY0-iJmsOVEW8svUrKreiqAJp0CWJvqImCmUNx2EqWrnCqk2NL0yAelDz_pP_jkOSV2MRJRJbMEQTNO1QGAw0WwGlqGA4pBgXCg5-W4Vlq2iKclkN2zpzycxkW33MuQBUfgP2uYq8plPi7tUkcchSVE-yXRDLuYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jrqC4wOYBt0jyqJ0mSMu9E_SeKEk9TwEHroJhdHZjP-8okGQdOCG7tx2bVb9hK6migCw90yKhGmmg9g8KkzmdjH0j_8tDMcuky4Lrq4RPiRBdgueGWWWfQ68cPxPOw8ntbsFXAWsPe0CfH74vJVAgMyc0gkuAh-7nPhi2SWhtyG5WDwFLMXbMcjjoysQmEvVx9qQ-MmkU9ypevO7Vs_Sg3w3x_vYaSbeTU3AoP9Uz9kB7dTTIPRYxlwpXFHIJGZ6T9VcpW_EbFrUlqkhNVN4Lj_GKg0BtWlbA9KZEhgJHbhjbsbsnpmPsYUX05RJp197sI8zyMPrZY-MlIl-m4aSog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hw9gRfc-PzKtO9UH8pJpVvmqPXf9FEG9vAE2Gh4_ZOfRh2PaHhiXMMjnqD9gZDl8svo6kcRg_vNQ4OBBNIGdMFGETGgW0CZ_ZVViIKBlUMHV05Q7q_wMJtXwJSLZeSp7rIDETLiXUrqOEySUY7Gsr409MAsmDhBhqjWN3hYBtC2TX6RMVn16ebFBg-u48JPDth-leb2lX0rBBtyM6XWE4_gbeZPRp6Ymsrv6vyO7oX-A6jYyVobkxAZYOhWwMd6tt7qGmEBm17H2Wi4fjTQqLZlyLn6mDnpEGk-pG1RZOqb9wcJUwVRGyA4c1wtyoWNTfjJyaTl2o9DcdDk1e5RhTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ویناک اینارم از ۴۰۱ گذاشته و میگه من اون موقع هم خایمال نبودم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/80275" target="_blank">📅 11:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80274">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73eef393f7.mp4?token=jUdsPuueAguDdNByj3IdRjZl2UfS5VdZ7VQMIJgdywEZwFBdRtFwqs8gen9_c69tLTSsBU-UAccgsGun8Oqi7NmqloErHnuEb9FqypJGbzaP97wL4iTKGptRKZQ_WMAyxyhqWnM07yXUe0dw5w_roY4_iCtbRXHmzHgyySGlNyoU6hWDzv7FbE0pLqICbPScBjPB7s1D0ck5B4XR-wYRVkYGFwJeIRZevkxfmyvU7Nd2lYPXBMQlZGOg2_6o5y_HTGf_ysjixb2VUC-Q_kGmyiZKnxL_wL88pxf1kzG2Mg_e8ebSUgzLyo1AEaQIWL98_X3Bf1O58aaG-oTAeCQ4Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73eef393f7.mp4?token=jUdsPuueAguDdNByj3IdRjZl2UfS5VdZ7VQMIJgdywEZwFBdRtFwqs8gen9_c69tLTSsBU-UAccgsGun8Oqi7NmqloErHnuEb9FqypJGbzaP97wL4iTKGptRKZQ_WMAyxyhqWnM07yXUe0dw5w_roY4_iCtbRXHmzHgyySGlNyoU6hWDzv7FbE0pLqICbPScBjPB7s1D0ck5B4XR-wYRVkYGFwJeIRZevkxfmyvU7Nd2lYPXBMQlZGOg2_6o5y_HTGf_ysjixb2VUC-Q_kGmyiZKnxL_wL88pxf1kzG2Mg_e8ebSUgzLyo1AEaQIWL98_X3Bf1O58aaG-oTAeCQ4Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویناک یه اجرا از دکی گذاشت چنلش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/80274" target="_blank">📅 11:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80273">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ui1Dm77S56XsIZ5wRNB0800gJ433Yz79DYqMNLSZc9YxweV-kNJTNdZZoxJcZ2G167x3JrkfRMDqLXobpO8ItxK6S2KVCTscGRsTnyCCUAx_nplaPjCJOaLb3VaH_vTlNz0exumPvdsTGNveblRx_jxc2sV7UnAb3c1UJoCi0IaVxKlzriGQ8XVJ3fcsH5DCKQrhzQQfzs5wTimfHCRMKYO16bUI7s6gHzZFq-BZO-DRYsffclvE1vlMdR2NwvZOpBTo957Fre8ODVPPb59VZGpik5VPAJZjdlh-o7rOqdBAZu8zE5X-fJHeg9YjuWmsLR3DDP61Ky0v8RrAYjlEoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
فرانسه
🇫🇷
-
🇪🇸
اسپانیا
🏆
نیمه‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
سه‌شنبه ساعت ۲۲:۳۰
📍
ورزشگاه دالاس (ای تی اند تی)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
✍️
اطلاعات و شرایط بازی:
- فرانسه در دور قبل در یک دیدار جذاب، با نتیجه دو بر صفر مراکش را شکست داد.
- اسپانیا نیز در مرحله قبل موفق شد در یک دیدار نزدیک، بلژیک را با نتیجه دو بر یک شکست دهد.
- برنده این دیدار باید در فینال به مصاف برنده بازی انگلیس و آرژانتین برود.
- با توجه شکست‌ناپذیری مداوم دو تیم و نزدیک بودن بازی، تساوی یا پیروزی خفیف فرانسه گزینه‌های مناسبی هستند.
🧠
وقتی بازی با فکر انجام شود، باختی وجود ندارد.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r23
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/80273" target="_blank">📅 11:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80272">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4TAC_J8yFT3WH9HQCuq1nLgVFbE_h2zLGc-hwjpJlzcgOpjNwaKpJ0h1USg3Kef66RCvYSGuz_Zj7zlthfBUD8wvb4QCcGgLw8hueN__n7R5O6bwgf4aZCX1cxmeUQ7owqO-Cjm5W5eefCLZ9yHJ6sUff0LdZ3URVpUUM8BDMvlceM6ER6xCTURhYR3m-5M3X3wW-pHwQhso-LhN_DqfRB3vRUHyVqwleZOEYwB00eYtGKKnJAntbfs8tanphQ1yHf5E9LKb3p0QVCA5jU8EZZCsIE7gzzuj_v1C_kJhIsB9wlLInEyPkeJIJJXTOiHrvsxUuzhUYGxxMrFt3oy4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواهر لیندزی گراهام جانشین او شد
فرماندار کارولینای جنوبی هنری مک مستر، خواهر لیندزی گراهام، دارلین گراهام را به عنوان جایگزین او ، سناتور این ایالت منصوب کرد.
با توجه به پیروزی لیندزی گراهام در انتخابات مقدماتی،خواهرش یک دوره شش ساله کامل در سنای آمریکا خواهد بود.
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/80272" target="_blank">📅 10:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80271">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامپ دلقک از تنگه هرمز هم میخواد بیست درصد تعرفه بگیره.
سازمان دریانوردی بین المللی اومده گفته این نقض فاحش حقوق بشره.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/80271" target="_blank">📅 08:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80270">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اسرائیل نیست خوب لانچرا رو کشیدن بیرونا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/80270" target="_blank">📅 04:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80269">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">الان که شما خوابید آقا آرش بیداره و موج دوم حملات آمریکا به جنوب هم شروع شده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/80269" target="_blank">📅 03:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80268">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">نفت شق کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/80268" target="_blank">📅 02:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80267">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">کنکوری های عزیز ایران بخوابید، کمک در راه نیست.
ترامپ: معتقدم دستیابی به توافق با ایران همچنان امکان‌پذیره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/80267" target="_blank">📅 01:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80266">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">حالا که مجبورید امتحان بدید حداقل بخونید تا دوازده سال از عمرتون که اینطوری گذشت بگا نره و ی ثمره ای داشته باشه، با آرزوی موفقیت برای تک تک شما در امتحانات پیش رو.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/80266" target="_blank">📅 01:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80265">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">من که میدونم این سری هم جنگ نمیشه ولی نمیگم که دانش آموزا همچنان امیدوار بمونن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/80265" target="_blank">📅 01:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80264">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ایرانم به رسم همیشه عربارو داره میکوبه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/80264" target="_blank">📅 01:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80263">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">آمریکا هم یاد گرفته ها
دیگه جنگنده بلند نمیکنه هزینه الکی داشته باشه
یدفه صدتا راکت شلیک میکنه</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/80263" target="_blank">📅 01:09 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80262">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jSzlYjBZrPEvZQovOx0JyoR7627zDSUIXoxh-N-LWpZWnKaXv84d-2d91W8cUimuImwf_heg1aGXG2ny5i00aj1DJWpmiUMXba8FAJH2th4nkVVPEaHORj29UIBosoINboXNOkjXJR9F8p1bTKZ0sWkr6kSsZ9F1frxxOwP-NZlDEki-eeCjBz5vqRs0RckErTVjftpC_NVDpCq23sRQhpemMcyNzKApT9nKUCflEQJCBh7NQmHuS--Ilu_zp5SWKs0fha4knLocvasiHw4UeBgjlbqKQWOag_J9G5blJCejGEi8gNm7d_0xitMS7xd--Ku_-YfwnV7ug47mRvhPrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا موشک کم اورده داره لانچر پرت میکنه</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/80262" target="_blank">📅 01:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80261">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17049dea80.mp4?token=Vp5gxJyWbyMBKFRMME9T5C4KTCO7YDADDwURN48o82hl8sPd1S5A_fYwXI_T2-aqcnAVe8fDRtag6gG8tABcE8nHRIJwCy1OL3_DZGNQSjvOL-8HEtoWp1IAXXG54zX4g5faD8mqUj_Ef5RUzZ1OopUIsRWFRiDmzKAZwhHWyavTIAAx4e4YD5LSuTQMvpQ29OSXhfpyISZ-QiPB__1j700TqiW9nBekdrKVaj6KLSxwK7Ngtix_ylRAiDVyq36xB3FOdQ5yqaii_R4nt-CvTcMa0Xdjd7TX5zHIj4kkYEL72Ik1XPVNCmor5i5_C5s9PVnPUDujlpuLd721KZ34Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17049dea80.mp4?token=Vp5gxJyWbyMBKFRMME9T5C4KTCO7YDADDwURN48o82hl8sPd1S5A_fYwXI_T2-aqcnAVe8fDRtag6gG8tABcE8nHRIJwCy1OL3_DZGNQSjvOL-8HEtoWp1IAXXG54zX4g5faD8mqUj_Ef5RUzZ1OopUIsRWFRiDmzKAZwhHWyavTIAAx4e4YD5LSuTQMvpQ29OSXhfpyISZ-QiPB__1j700TqiW9nBekdrKVaj6KLSxwK7Ngtix_ylRAiDVyq36xB3FOdQ5yqaii_R4nt-CvTcMa0Xdjd7TX5zHIj4kkYEL72Ik1XPVNCmor5i5_C5s9PVnPUDujlpuLd721KZ34Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت حملات از جنگ ۴۰ روزه بیشتر نباشه کمتر نیست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/80261" target="_blank">📅 01:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80260">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">حداقل کشورو بسپارید به فلیک شاید فرجی شد</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/80260" target="_blank">📅 01:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80259">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">جدی بعنوان کشوری که یدونه پدافند درست حسابی هم نداره بیش از حد کیرگوزی میکنید پسر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/80259" target="_blank">📅 00:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80258">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">مایی که خونمون نزدیک اسکله س چی؟</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/80258" target="_blank">📅 00:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80257">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTheMojoMan</strong></div>
<div class="tg-text">مایی که خونمون نزدیک اسکله س چی؟</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/80257" target="_blank">📅 00:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80256">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اگه جنوب کشورید به هیچ وجه نزدیک اسکله و ساحل ها نشید، وضعیت خیلی کیریه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/80256" target="_blank">📅 00:56 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
