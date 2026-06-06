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
<img src="https://cdn4.telesco.pe/file/ocVDeNuEXmKXrvs81S0SGTH5H5z3hTpsPbe_l8ABthcUER6a0N4eW4b2C9KxKSvXTXHVqdMGKBp1V7e1DFTBibWv-Y_oDh2tV-TbDncxW3vcShMCdKuiZHHb_IiaL3CmQ84YLCoSsbMyB8J-39gwEM9SckanTj8XOoy9bUCyOZDosSIzjhHYhTKmSFeTHezUk1BGiG4n5pOCtjq_0-MpTpnep7VpGGEYQglsrUmbo5i_H-AacVVfFGppkT4xGlzoSYmCxup5v7vX0TrhtJCuVGOp3L9q2TSKyRYg1OlukP9WM17Kk8zc7V1dSDUhOEuAy_IeVH_p8UuV_msetfnbCg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 291K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 01:05:00</div>
<hr>

<div class="tg-post" id="msg-13655">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">از روی استوری تو اینستا وارد کامنت میشی کامنت دیده میشه ولی از پیج خود شاهزاده وارد میشی دیده نمیشه تقریبا هم ۶ هزارتا لایک خورده. من فکر کنم همه به ادمین پیج باید اعتراض کنن چون من خودم زیر یک پست دیگه اعتراض کردم اونم هیدن شد الان دوباره کامنت گذاشتم که…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/withyashar/13655" target="_blank">📅 00:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13654">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSoheil</strong></div>
<div class="tg-text">از روی استوری تو اینستا وارد کامنت میشی کامنت دیده میشه ولی از پیج خود شاهزاده وارد میشی دیده نمیشه تقریبا هم ۶ هزارتا لایک خورده.
من فکر کنم همه به ادمین پیج باید اعتراض کنن چون من خودم زیر یک پست دیگه اعتراض کردم اونم هیدن شد
الان دوباره کامنت گذاشتم که این جور ادمین بودن خودش دیکتاتوریه</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/withyashar/13654" target="_blank">📅 00:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13653">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">رویترز: ایالات متحده در حال بررسی راه‌هایی است تا دارایی‌های ایرانی را در اختیار متحدان خلیج فارس قرار دهد تا به تأمین مالی بازسازی و تعمیرات ناشی از حملات ایران کمک کند
@withyashar</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/withyashar/13653" target="_blank">📅 00:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13652">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkvBCIv8r0qa5rX55VMwo3dMXtzNNXfqOfai38t75jM_uQj6PkDrugDfVsKDua87T9goANorn7GpGd4nXNHE9xBKutu6v4EDiEClI--STvDOVjgWdSGmWt3KJatsny4zAg3kpAuDIoSWYE0AcPWbvG-YXoQ2wkMa0bvDqttyQKLSUgB7QfBTz-BmKXjxfTovtYbAeg5J_szRfoTCeeteCvRDIh_LLvFrPhFV81crYlKvUXz6R7y0wL-tLYylrb-6-tIzusDmdKQD-P8BVvtj_3fIlFUps2XbbcuLIBHvPolV7oB_43HpU-5s1Z08MUgMFVAZpN-OvHELDTAoCq-skw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ در تروث شبیه آخر ویدیوی هست که پست کردم شبه حمله
😃
@withyashar</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/withyashar/13652" target="_blank">📅 00:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13651">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/withyashar/13651" target="_blank">📅 23:55 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13650">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">https://www.instagram.com/reel/DZQKl3sRlmS/?comment_id=17866790943686477  پست جدید اینستاگرام ، کیا منتظر شب‌حمله هستن ؟!</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/withyashar/13650" target="_blank">📅 23:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13649">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">مهم ‌محمدجواد لاریجانی: سایه ترورها وجود دارد، آن‌ها هم باید بدانند که حتما بهایش را می‌پردازند و ترور، ترور دارد
کارشناس ارشد مسائل بین‌الملل: اینکه فکر کنیم در صورت تحویل اورانیوم‌ها و حق غنی‌سازی جنگ تمام می‌شود، اشتباه محاسباتی است
@withyashar</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/withyashar/13649" target="_blank">📅 23:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13648">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/withyashar/13648" target="_blank">📅 23:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13647">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">خبرگزاری ایرنا به نقل از وزیر کشور پاکستان: «پیامی که برای رهبر ایران می‌برم مهم است و امیدوارم اوضاع خوب پیش برود.»
@withyashar</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/withyashar/13647" target="_blank">📅 23:17 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13646">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">https://www.instagram.com/reel/DZQKl3sRlmS/?comment_id=17866790943686477  پست جدید اینستاگرام ، کیا منتظر شب‌حمله هستن ؟!</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/withyashar/13646" target="_blank">📅 23:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13645">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">مهر: صدای انفجار در خارگ مربوط به خنثی سازی مهمات است @withyashar</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/withyashar/13645" target="_blank">📅 22:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13644">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">https://www.instagram.com/reel/DZQKl3sRlmS/?comment_id=17866790943686477
پست جدید اینستاگرام ، کیا منتظر شب‌حمله هستن ؟!</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/withyashar/13644" target="_blank">📅 22:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13643">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">نیویورک‌تایمز: اسرائیل مکالمات مربوط به مذاکرات آمریکا با جمهوری اسلامی رو شنود کرده.
اسرائیل تلاش‌های خود برای شنود مقام‌های ارشد آمریکایی از جمله ویتکاف و البریج کولبی، معاون وزیر جنگ آمریکا، رو افزایش داده.
@withyashar</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/withyashar/13643" target="_blank">📅 22:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13642">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a15cea3880.mp4?token=eZ32zuemNTIK0yrsN6PpUm9X7n72vHt4730sLRaJZEc80DflcAHthj0jpj3STh2BOTywhOcp2uW2Jf2elmKTBn5EDQMQmElxtRPib6GWT2elDNELX9owh6MuEwaO4zb4tlh2ZAK_pqh2Smdu7KcZErJ2yxZWWxvJPOtwueQsQpuYW-gyUJNCFhdYSac_4TVGLfmdxopSS77mk1cGnYPYm0vmptJFLVWUzOwDKGZaQWKY7xknIn-d3LsqTQGqoqVGOZfho4ecxWY8GviUQ2u7QDa7YRXBuY-SzAewsPrhiXwyS5G0aFJThhU1ymDb7YzYE_-afBmPD8Ex7EocSb7xFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a15cea3880.mp4?token=eZ32zuemNTIK0yrsN6PpUm9X7n72vHt4730sLRaJZEc80DflcAHthj0jpj3STh2BOTywhOcp2uW2Jf2elmKTBn5EDQMQmElxtRPib6GWT2elDNELX9owh6MuEwaO4zb4tlh2ZAK_pqh2Smdu7KcZErJ2yxZWWxvJPOtwueQsQpuYW-gyUJNCFhdYSac_4TVGLfmdxopSS77mk1cGnYPYm0vmptJFLVWUzOwDKGZaQWKY7xknIn-d3LsqTQGqoqVGOZfho4ecxWY8GviUQ2u7QDa7YRXBuY-SzAewsPrhiXwyS5G0aFJThhU1ymDb7YzYE_-afBmPD8Ex7EocSb7xFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نورتروپ گرومن سامانه دفاعی
«AN/AAQ-24 LAIRCM»
را برای هواگردها توسعه داده است؛ سامانه‌ای که برای مقابله با موشک‌های حرارتی و دوش‌پرتاب طراحی شده و به‌صورت خودکار با استفاده از لیزر، جستجوگر موشک را منحرف می‌کند تا به هدف نرسد.
رسانه‌ها آن را به تهدیدهای منطقه‌ای علیه هواگردهای آمریکایی و اسرائیلی در خاورمیانه وصل می‌کنند. نورتروپ گرومن می‌گوید همکنون این فناوری روی بیش از ۱۵۰۰ هواگرد از ۸۵ نوع مختلف به کار رفته است.
@withyashar</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/withyashar/13642" target="_blank">📅 22:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13641">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f3cd7dfbe.mp4?token=W7K1Y00llGlYJ5KXG04uRuZRHLg-CdXJTDCSjPQYN5z9O2uYEB1PJ4dGy_EIx8jZx4o5jal6LxQ7fX7LB9EK9ljxuaO-pJZqTjLHSfCVwKhIrVForlayv_YiGmJDzCqP8EDgW3GzvQbZOU0ek3qMUMocfTig34Iznue011nIoKEzxnjdvKLPQp2fhjTOfEP1FI_TIB0IxF_VH0kMOZLIfbGpSKJ5GSoAOCHkAFG1t23EA71fd2kcFrJdHi2VOsWjebp00O_mRNmCbTo6KzBJqq-w68lkyvSik248ekgNmkMQiU59MoncwgxVTlSEV-L3W81tYCxOneTbW8qm3peiwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f3cd7dfbe.mp4?token=W7K1Y00llGlYJ5KXG04uRuZRHLg-CdXJTDCSjPQYN5z9O2uYEB1PJ4dGy_EIx8jZx4o5jal6LxQ7fX7LB9EK9ljxuaO-pJZqTjLHSfCVwKhIrVForlayv_YiGmJDzCqP8EDgW3GzvQbZOU0ek3qMUMocfTig34Iznue011nIoKEzxnjdvKLPQp2fhjTOfEP1FI_TIB0IxF_VH0kMOZLIfbGpSKJ5GSoAOCHkAFG1t23EA71fd2kcFrJdHi2VOsWjebp00O_mRNmCbTo6KzBJqq-w68lkyvSik248ekgNmkMQiU59MoncwgxVTlSEV-L3W81tYCxOneTbW8qm3peiwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین الان بابل پهپاد شناسایی دیدن با کلاشینکف دارن میزنند
🥴
@withyashar</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/withyashar/13641" target="_blank">📅 21:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13639">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">مهر: صدای انفجار در خارگ مربوط به خنثی سازی مهمات است
@withyashar</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/withyashar/13639" target="_blank">📅 21:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13638">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLgoEMJChIjogF-UOLubZ860R_5wl8HcVMc8z0l6zn0ENI4yNzxNbyBXqFoGX0p7EsnzkzvqxnnzKMUDVox83WRjHpjo6C8whkrMUh8TT-bU_8-B4u3yLrVoeD0X9b-LCwsymBkc_kYFTIHI_1bocuHZHrf8cXtkIVjrkyXK9fLO72m2au3pg4rDvnb9S2R7-WY5CUa25D07ede1KWS7WPrxymf0EF8mB66jN92R_zqzBcj8TL8sR5oP9WEppN4So-3PjwTUtQgBw0TuHw2kwlo4i9iLH1ZFhY_7NbrMRbC9Po0Vr9o2ulTKOUWTQbS5Qrs-Efb23n7LXjG9Wq9kJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار وزرای کشور ایران و پاکستان
@withyashar</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/withyashar/13638" target="_blank">📅 21:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13637">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">کامنت رو رفتم زیر پست جدید پیج دوم شاهزاده   https://www.instagram.com/reel/DZQKl3sRlmS/?igsh=NzNsemFkNW9lcml0</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/withyashar/13637" target="_blank">📅 21:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13636">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/withyashar/13636" target="_blank">📅 21:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13635">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">کامنت رو رفتم زیر پست جدید پیج دوم شاهزاده
https://www.instagram.com/reel/DZQKl3sRlmS/?igsh=NzNsemFkNW9lcml0</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/withyashar/13635" target="_blank">📅 21:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13634">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d77683181b.mp4?token=Y4gY1Vad3aDJbnn4ISHt5_xugJMFx3fJ7v3ONc0ag_08bsgGbGu6Ppx5SGAu27g3KIqKTodMgWK0LyB777USSNnFt0PHmAs3GxLGqFsn_3ErKHmuj77bXMUQnQpxjNXPWhQmPN2GBeqhqLgKOi5OjIL-jjMkEDdEJzfWOtxzgNkB2057Pxgrq59M-sbXVnX0d0ZBvCPCZKRNg-r6C9n86N5KGGlCc3T9rK_WrNSYnJbyuFCknzt5S7FRh03fpHr4gmhHDdAjtcLMpqbAUwPK2xng-UBi7LvnUKaNuXmUMfqVS8dNdlq6gKhbxyJmny3J_0X48LPucggZEsW6fEf6zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d77683181b.mp4?token=Y4gY1Vad3aDJbnn4ISHt5_xugJMFx3fJ7v3ONc0ag_08bsgGbGu6Ppx5SGAu27g3KIqKTodMgWK0LyB777USSNnFt0PHmAs3GxLGqFsn_3ErKHmuj77bXMUQnQpxjNXPWhQmPN2GBeqhqLgKOi5OjIL-jjMkEDdEJzfWOtxzgNkB2057Pxgrq59M-sbXVnX0d0ZBvCPCZKRNg-r6C9n86N5KGGlCc3T9rK_WrNSYnJbyuFCknzt5S7FRh03fpHr4gmhHDdAjtcLMpqbAUwPK2xng-UBi7LvnUKaNuXmUMfqVS8dNdlq6gKhbxyJmny3J_0X48LPucggZEsW6fEf6zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش فعالیت جنگندهای ناشناس در آسمان بندرعباس
🚨
@withyashar</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/withyashar/13634" target="_blank">📅 20:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13633">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/withyashar/13633" target="_blank">📅 20:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13632">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a6234155d.mp4?token=flxsIbmjffuaym_-_Nz9tZow3VLJjs062SWhNkfay2sciGJk0JQsMFb7fmYxejG6UKNh5aw4ngd5ljhl8ujoJTaXE5TpyaYaNwGTSA6CTav0IAm2OFrDN4JGKwlb9VBO5-rqzPJINeDyPjaYAnQPqWFe5WzJUTgzAcc7iDajfIf27d0JtS2hhh7Bv4miQMG1L9XM8VIeUBgixYFEsOe4JmHXBbZgrPdo8GPDtmxQJngUG42Ws61kFxzXXv3nZjPQo3P43hfIZJNnQiv_93b8ynK16gMpFl9SrVEFOL9GsSYqdh6UBMF4f_hxJFyeBzRBWNODOZkAp4uZ7B_j6w9c3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a6234155d.mp4?token=flxsIbmjffuaym_-_Nz9tZow3VLJjs062SWhNkfay2sciGJk0JQsMFb7fmYxejG6UKNh5aw4ngd5ljhl8ujoJTaXE5TpyaYaNwGTSA6CTav0IAm2OFrDN4JGKwlb9VBO5-rqzPJINeDyPjaYAnQPqWFe5WzJUTgzAcc7iDajfIf27d0JtS2hhh7Bv4miQMG1L9XM8VIeUBgixYFEsOe4JmHXBbZgrPdo8GPDtmxQJngUG42Ws61kFxzXXv3nZjPQo3P43hfIZJNnQiv_93b8ynK16gMpFl9SrVEFOL9GsSYqdh6UBMF4f_hxJFyeBzRBWNODOZkAp4uZ7B_j6w9c3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/withyashar/13632" target="_blank">📅 20:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13631">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/withyashar/13631" target="_blank">📅 20:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13630">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yk5TAG6x6Wv_jhWmbGVectuSAI-f3cSVGZIKc4WoVc0NTgFN5dYj4wFLlb9MSVHAx1X5ThyGStp7Vk84Mtgloar4joGKoSQafxdABFMyUi1UKOFmZlRcjeTEFLZbZWWyi6Ut0UG7O4mEyMWMz2DX8EZga0I_2zoFZfSBgp5dg0-wRTdtiQNvZcrIgghod29_TY9fVjhArNytWt_JQzSauSug2lkLRx2qh7OMWgHX8Aar7fpp0AnQ1c-rVJGEBytwukslV8Wu5WOaxIV0LhyPQgvHb5xeRxc4lVP3shRCb-y4fc7AU38TetfMlorOhz8-0v9Rj3Q1BuL00tVoHm-dmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ ایران و بستن تنگه هرمز، به صادرات تکنولوژی‌های پاک چین مانند باتری، خودروی برقی و ... منجر شده و به بیشتر از ماهی ۲۰ میلیارد دلار رسیده است
@withyashar</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/13630" target="_blank">📅 19:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13627">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">العربیه:
ترامپ به میانجی‌ها اطلاع داد که مذاکرات با ایران بیش از 60 روز ادامه نخواهد داشت که این مهلت در روز های آینده به پایان می‌رسد و ایران باید به‌سرعت پاسخ دهد.
« این خبر فیکه که پخش شده »
@withyashar</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/withyashar/13627" target="_blank">📅 18:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13626">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d35551fc6.mp4?token=LhJerVz967QOzlYqgHYrRJAS0ol73U8vkmC3EfYcKOglskixqP1bQla27znj4t6yLgzOJ--dWQtmz9C-WTrcvQT-2iD8knw9cp5fa6hVVk2hVzrSIvyJ7F6YxW8xk4Jp4Olk-WrSMEv08MJQq_tUi3f0LE7uBBB1zppYsfoLrn6mNkIgwjgrOIdqAIOMbqSzB_HBGaBC3juvt0DtRu5TSgGuH8RjuzLAAOJGnBEb5nC70M2HUWHyA_lhmbIuZD4-r5NY-R63oFdyqa9XumBdH1DxnumSKxx6czni6qhHoKBKb02FYe4PnFRa_yr2kBtzuMz6bBM-YF8iq-XAPFneRmzDIHT5OlkV_vxu2V41zyfWMpg_BfouJyKR1SEKUsZ3ZGDBT8d-cETFGPtBFZPZx1-Ju_2bEXbi1jPng-WMw-U5pqBBejJHLv48njoqRxYz2YCSifvX2BXOduTAo7w-g1k-qqgkCyZV2RluCPQTc2dZsNTzYqxM0xfk7xL6ZaSyfngexWoLtchoh9_-_sJNrrSLwESXdEymT5y-lllje_YGcFXCX0zogX6nxqoVWL6trcGHRaKeRnZfQLczL462CTYOgNxb5QMtodIqlQO2ta6i11ZqEPPinqg4oFy9gH2IsVUyfyUwNCxeWa5FDwqe26ZaHKTAV6j0IDgYx4TnIZI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d35551fc6.mp4?token=LhJerVz967QOzlYqgHYrRJAS0ol73U8vkmC3EfYcKOglskixqP1bQla27znj4t6yLgzOJ--dWQtmz9C-WTrcvQT-2iD8knw9cp5fa6hVVk2hVzrSIvyJ7F6YxW8xk4Jp4Olk-WrSMEv08MJQq_tUi3f0LE7uBBB1zppYsfoLrn6mNkIgwjgrOIdqAIOMbqSzB_HBGaBC3juvt0DtRu5TSgGuH8RjuzLAAOJGnBEb5nC70M2HUWHyA_lhmbIuZD4-r5NY-R63oFdyqa9XumBdH1DxnumSKxx6czni6qhHoKBKb02FYe4PnFRa_yr2kBtzuMz6bBM-YF8iq-XAPFneRmzDIHT5OlkV_vxu2V41zyfWMpg_BfouJyKR1SEKUsZ3ZGDBT8d-cETFGPtBFZPZx1-Ju_2bEXbi1jPng-WMw-U5pqBBejJHLv48njoqRxYz2YCSifvX2BXOduTAo7w-g1k-qqgkCyZV2RluCPQTc2dZsNTzYqxM0xfk7xL6ZaSyfngexWoLtchoh9_-_sJNrrSLwESXdEymT5y-lllje_YGcFXCX0zogX6nxqoVWL6trcGHRaKeRnZfQLczL462CTYOgNxb5QMtodIqlQO2ta6i11ZqEPPinqg4oFy9gH2IsVUyfyUwNCxeWa5FDwqe26ZaHKTAV6j0IDgYx4TnIZI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید ترامپ در تروث
@withyashar</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/withyashar/13626" target="_blank">📅 16:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13625">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkV0rVsLRey94qqvoZrx2xTcFQarjoXeZ85sU8paLlvlnjoIz2hikpCct4hrOQl8Nppk2Q4Bl1VA5EyLpgNQ8NT76bpxLyn0D3nzXsvQpyG_jQTS44zzgCYZfzY-XN4r_kKyrghPS0bg5TgntCSdOtaqn06-hqZwT5hL4iUcgaAg0dGq8JxXnP-D4OjvghhBFGtCr861xrK6j-kncBDixoM69BT1qAgmlxtJUHiZY-gVGAkQmn29krebZn7uyX5RfDY9Vnr4RH4N7ticN41NYIlvfUZwRCbStIn7Wh9Y7XOhnP2uX4m0yhi9HsgKFEjDL7yREarbTu061HH_yaamzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دکل مخابراتی پایگاه شهید راهبر نیرو دریایی سپاه در بندر سیریک که شب گذشته، هدف پرتابه‌های آمریکایی قرار گرفت
پیش‌تر اسکله این پایگاه در طول جنگ هدف بمباران آمریکایی ها قرار گرفته بود.
@withyashar</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/withyashar/13625" target="_blank">📅 15:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13624">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">وزرای کشور کشورهای عضو شورای همکاری خلیج فارس (GCC) جلسه اضطراری تشکیل می‌دهند.
@withyashar</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/13624" target="_blank">📅 15:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13623">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">مدیرعامل آسیاتک: اینترنت دیتاسنترها همچنان قطع است
مدیرعامل شرکت آسیاتک، با اشاره به تداوم مشکلات دسترسی به شبکه در بخش‌های تخصصی، اعلام کرد که برخلاف برخی اظهارنظرها مبنی بر بازگشت وضعیت اینترنت بین‌الملل به شرایط پیش از دی‌ماه سال گذشته، دسترسی مشتریان مراکز داده (دیتاسنترها) همچنان برقرار نشده و کسب‌وکارهای اینترنتی کماکان با چالش مواجه‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/13623" target="_blank">📅 15:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13622">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامپ به میانجی‌ها گفته ایران باید زود جواب بده
@withyashar</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/withyashar/13622" target="_blank">📅 14:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13621">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">الحدث: ایران خواستار مذاکرات سه‌ماهه درباره جزئیات پرونده هسته‌ای است
@withyashar</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/withyashar/13621" target="_blank">📅 13:41 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13620">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">صدای انفجار قشم
🚨
@withyashar</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/13620" target="_blank">📅 13:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13619">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">(IG @yashar)‎⁨منتظریم کی شب حمله فرا می‌رسد⁩</div>
  <div class="tg-doc-extra">اتاق جنگ با یاشار (t.me/withyashar)</div>
</div>
<a href="https://t.me/withyashar/13619" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🌐
instagram.com/yashar
🌐
t.me/withyashar</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/withyashar/13619" target="_blank">📅 13:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13617">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">وزیر کشور پاکستان(
سناتور سید محسن رضا نقوی
)امروز به تهران می‌آید تا تلاش کند در مسئله دارایی‌های ایرانی مسدود شده، پیشرفتی حاصل شود
@withyashar</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/withyashar/13617" target="_blank">📅 12:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13616">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8d357648b.mp4?token=HyF3VRf3gzB3XciSVQpEql8v3KXQX2CUpbsE2-hzEW17L7MkYtFLU_r94nRQ8ejdjxscVrAsSmRwtmrJzn9OVUU_AR2ONYOSAtTXmJ3Px6ql40th55VtVIWudYYtLt-mLrLWlzlfexCNdkoUKNFpudikim5lOe_XFlI2qSIQSK3NZmv5cYsYjL2D2PRH4WF3Z9L6J5QjJ8WqE90rpuV_equhz4HjCwrq2c3JBemLPupqZgd3Yn3g54_5ETqfRqgqEvNQPa0FFJwAiNfd_qzZRXZ4vr_UBuykuatEE__s5IEpX2ecHLRYpJMsuyfi2d--LVtZx3rTW1lR_Kmlo7uJFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8d357648b.mp4?token=HyF3VRf3gzB3XciSVQpEql8v3KXQX2CUpbsE2-hzEW17L7MkYtFLU_r94nRQ8ejdjxscVrAsSmRwtmrJzn9OVUU_AR2ONYOSAtTXmJ3Px6ql40th55VtVIWudYYtLt-mLrLWlzlfexCNdkoUKNFpudikim5lOe_XFlI2qSIQSK3NZmv5cYsYjL2D2PRH4WF3Z9L6J5QjJ8WqE90rpuV_equhz4HjCwrq2c3JBemLPupqZgd3Yn3g54_5ETqfRqgqEvNQPa0FFJwAiNfd_qzZRXZ4vr_UBuykuatEE__s5IEpX2ecHLRYpJMsuyfi2d--LVtZx3rTW1lR_Kmlo7uJFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همکنون پرواز هواپیمای اف-۵ ئی
تایگر ۲( تک نفره )متعلق به هوانیروز جمهوری اسلامی برفراز مشهد
@withyashar</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/13616" target="_blank">📅 12:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13615">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dA_sLc83uWf4ZByTzNIobycm-WSJxcfo5hNL6AXkR3vuqJCKUPl5SsgSr3uwU3YDtxDzBroYigt25R2UrQQmvzoVHAOS6URJegOVB6VDNBoytND8WbilBP1OJX8uxMvHXSoHcDIT_6vvzEIAyNqYVmQ6ZJdrbljJq57y4WE2nA3JDX2mB67yGpbuXaZ_QBaYVMFrE5NR9YnsslrpIR_MHjI68DUsS-KN8-o6JwoT9JbYzw519XmTEXC4KbZIHbf1jDM5TKAKK38Jtk6UkyXVpRyNWMV-f-UE8x19fBVXfeN8Ka060rEfk_7Rh1dxFkrVhlxOLx6uQfKLcHoPF3PPbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس های جدید پایگاه هفتم شکاری شیراز بعد از جنگ
@withyashar</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/13615" target="_blank">📅 11:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13614">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ورزش سه :  آمریکا به 15 نفر‌ از اعضای تیم‌ ملی ویزا نداده و رفتن ایران به جام جهانی در هاله ای از ابهام‌ قرار‌گرفته.
رویترز : کسایی که ویزا نگرفتن برخی از مربیان و هیئت همراه هستن وگرنه تمام بازیکنا ویزا گرفتن.
آمریکا اعلام کرده اجازه نمیده افراد غیرورزشی به بهانه ورزش به آمریکا بیان
@withyashar</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/withyashar/13614" target="_blank">📅 10:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13613">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سنتکام: ۷ موشک بالستیک ایران به سمت کویت و بحرین شلیک شد
فرماندهی مرکزی ایالات متحده (CENTCOM) اعلام کرد ایران هفت موشک بالستیک به سمت کویت و بحرین شلیک کرده است.
بر اساس ادعای سنتکام، شش موشک توسط سامانه‌های دفاعی رهگیری و منهدم شده و موشک هفتم نیز به هدف مورد نظر خود نرسیده است. سنتکام همچنین اعلام کرد هیچ آسیبی به نیروهای آمریکایی وارد نشده است.
@withyashar</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/13613" target="_blank">📅 10:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13612">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32ba7b496b.mp4?token=sCX-m_dbTdj0ApT7cYk3Gb4ov0jr1OOAndzK163_0w1U2-xhsWlfJfgghj2OnCpbpAbBy5qEeTtPlfCvSChXwIHDEMFkwAhYXD5upJwZ1oIthhnizvJxKUNBFBFkW0v9i5zQOyQJW1o6NCNuAioaGVEUKhkmUrwiAzz3XHO7Cmx1IhouBiF1n5xeluJWqS_aefymnPZSCT7pV5C2MQb9LW1v6YMymrJCTI8IGgQxXq9kt2gO-_L5pIY8mp2n7u1WcnJLiJOvfPoP2jv8KTUB_zYfpx1lCmKDrYFhY7Ez-sqjWVRTPET1tmQd3ewKANgueDh_sP5cs6GJPNRfraqxbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32ba7b496b.mp4?token=sCX-m_dbTdj0ApT7cYk3Gb4ov0jr1OOAndzK163_0w1U2-xhsWlfJfgghj2OnCpbpAbBy5qEeTtPlfCvSChXwIHDEMFkwAhYXD5upJwZ1oIthhnizvJxKUNBFBFkW0v9i5zQOyQJW1o6NCNuAioaGVEUKhkmUrwiAzz3XHO7Cmx1IhouBiF1n5xeluJWqS_aefymnPZSCT7pV5C2MQb9LW1v6YMymrJCTI8IGgQxXq9kt2gO-_L5pIY8mp2n7u1WcnJLiJOvfPoP2jv8KTUB_zYfpx1lCmKDrYFhY7Ez-sqjWVRTPET1tmQd3ewKANgueDh_sP5cs6GJPNRfraqxbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام ویدئوهای حمله به سایت‌های رادار ساحلی‌ایران در سیریک و جزیره قشم را منتشر کرد و
کفت
حملات تلافی‌جویانه ایران به بحرین و کویت رهگیری شده است
@withyashar</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/withyashar/13612" target="_blank">📅 10:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13611">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ارسالی : من بابامم تعریف میکرد که زمان جنگ عراق و کویت صدا های بمب هارو میشنیدن خرمشهر
@withyashar
گزارش های زیاد از شنیده شدن انفجار کویت از خرمشهر !</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/withyashar/13611" target="_blank">📅 04:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13610">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBX6F8AVpCtxeGqbr2axo2ebcrLpDNiy81BjOvjeGu4H5dxRdTJkemha-JWfNyP6Sy7suk3m4sFOHUu6ECPeJTFNbgoOVw2hg3o_hA1TFV-9-exN1PNZ4myLq89z9WSphVfqCejaYJ834g0fRyVEQ0Pyzv0BcxJNDQ26R_QDcrrcyASATYlw7CfLQnwz_QFxZfYDIZZ_0ZlG87mewft-TL6Efv6uIiASf_QCRbNdzG3GBS97vF0eTD-nRJWqA4LTtTNcJuKOP9MZ9j9Y7O_QJ2l73EShIgTCNtQ-R2ZMwO-u3mq1Mdu4M7AYjHdAJxXNcXAutucpQQaEN31lHNBOng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی : کویت آلارم اومد الان ، ۳پا موشک زده سمتش !
@withyashar</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/withyashar/13610" target="_blank">📅 04:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13609">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/622170a597.mp4?token=armPFxFBawHIK7P3PPDeP00k69dagBQucZPrT1gJ-D3uNWnbgc6nuPcl6pysWGrqZepF3HnaCZU3J6XwuBMmFEyUonKAKN5wDlHPBqKe0CSxGV50eKeqxgrBQVe27Dmz_JM6kgAYu4x_w58XTyNzi_utR9jZDpTm0A0TNSdcRYUQ6aImTpLW_KUtLlWSBt6o7fczRxck4fr-HBZbAFh1wZbKjoT-HVcLDaRZ_j69CG7THOsYGkCqEQpH_dyGakKTx3IuzRGPm8chl3H5bAxC7t5qLouAHkXZpFadMOJcS8NQyYd4NIWQmUyOUukuXm4s44NdoT8q5eFYlKB_TLUpMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/622170a597.mp4?token=armPFxFBawHIK7P3PPDeP00k69dagBQucZPrT1gJ-D3uNWnbgc6nuPcl6pysWGrqZepF3HnaCZU3J6XwuBMmFEyUonKAKN5wDlHPBqKe0CSxGV50eKeqxgrBQVe27Dmz_JM6kgAYu4x_w58XTyNzi_utR9jZDpTm0A0TNSdcRYUQ6aImTpLW_KUtLlWSBt6o7fczRxck4fr-HBZbAFh1wZbKjoT-HVcLDaRZ_j69CG7THOsYGkCqEQpH_dyGakKTx3IuzRGPm8chl3H5bAxC7t5qLouAHkXZpFadMOJcS8NQyYd4NIWQmUyOUukuXm4s44NdoT8q5eFYlKB_TLUpMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید ترامپ در‌تروث : نیروی دریایی ایران
@withyashar</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/withyashar/13609" target="_blank">📅 03:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13608">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda12e11f6.mp4?token=i0RzWZ8UNgednUqtdaQ4lPrOlobLMuc3cUkpkdrK5GPq11J0YsvPHwW9YVOz6vxafevrAqj5XvIBYRuMqjIvuKR6GZkxUPmev_Af71GRDGK480HPxlZSGKJ6-_L2X7NXXM-l6YSm2i3bpdCNEmsQhVWyk4Q9Za8hoRSdRle4TIUyWZKeKr_P70P7ms-iVLtc7ZuxEZmQ4OBkSYex9-Ava7laIEe9UhRMCoSPKCGk06kz3D4EvII1xzNflW0HGiwaYoGNBGKWqzww_UCdzJE6FaGz8JPsoxCkPszGq6kfqQahjJmxgDn2pfCSUeJyLr9i4zkbmQ7gAtoPdYSGP1RkhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda12e11f6.mp4?token=i0RzWZ8UNgednUqtdaQ4lPrOlobLMuc3cUkpkdrK5GPq11J0YsvPHwW9YVOz6vxafevrAqj5XvIBYRuMqjIvuKR6GZkxUPmev_Af71GRDGK480HPxlZSGKJ6-_L2X7NXXM-l6YSm2i3bpdCNEmsQhVWyk4Q9Za8hoRSdRle4TIUyWZKeKr_P70P7ms-iVLtc7ZuxEZmQ4OBkSYex9-Ava7laIEe9UhRMCoSPKCGk06kz3D4EvII1xzNflW0HGiwaYoGNBGKWqzww_UCdzJE6FaGz8JPsoxCkPszGq6kfqQahjJmxgDn2pfCSUeJyLr9i4zkbmQ7gAtoPdYSGP1RkhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همکنون
جت‌های جنگنده آمریکایی در حال پرواز بر فراز استان بصره عراق نزدیک مرز ایران هستند.
@withyashar</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/withyashar/13608" target="_blank">📅 03:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13607">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ea974c1bb.mp4?token=CYBKNU88NR5fWDMXVq_T9TZET1s4v1Lka8hEEd6nrfFKwIB7WfUgCImA5PBeUz4cFZ8vvHTnrnR9Q7WkpCn7Y8PXilGh0s2H6ZbUVL5SBNpEyhNNci3ePkVG8oCddylq2MM0bf_eLkrrj4YQPsiGH2R-0qZo9ka9gW2gTxUbweIcX2BDm3s-uVn7J1h3rK1BUqgNLEJNfqByW-eCmumaRX_Fu4QUvd05dqOmkp_M6D3KEypHDAWMVkF9ACLxh5NYipaPt545js9IoB5TgyC3zSmT40HrF0vGScYg9DViWvIwTkc5gQ-QvJ7ifdeW5ouFy7AlPuU__A6q5hPEKR3UYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ea974c1bb.mp4?token=CYBKNU88NR5fWDMXVq_T9TZET1s4v1Lka8hEEd6nrfFKwIB7WfUgCImA5PBeUz4cFZ8vvHTnrnR9Q7WkpCn7Y8PXilGh0s2H6ZbUVL5SBNpEyhNNci3ePkVG8oCddylq2MM0bf_eLkrrj4YQPsiGH2R-0qZo9ka9gW2gTxUbweIcX2BDm3s-uVn7J1h3rK1BUqgNLEJNfqByW-eCmumaRX_Fu4QUvd05dqOmkp_M6D3KEypHDAWMVkF9ACLxh5NYipaPt545js9IoB5TgyC3zSmT40HrF0vGScYg9DViWvIwTkc5gQ-QvJ7ifdeW5ouFy7AlPuU__A6q5hPEKR3UYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشتک نیم وارو پهپاد های شناسایی اسمون بندر عباس همین الان
@withyashar</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/withyashar/13607" target="_blank">📅 03:17 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13606">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/withyashar/13606" target="_blank">📅 03:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13605">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/withyashar/13605" target="_blank">📅 03:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13604">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb45455c0d.mp4?token=igoagHH2lYINNQq_1vW-AYx0_zoD2iGbheHzdwOMqfW98WA7CNv1-ogzop22IIjHICeIzNd8KVwyT4vdTssjfQhNyx15Es0Yv6n6vtGPetU3coqFTdTWg7glq0W0BUB7mJSo-MasaZZE88LukG6n-OcNQT6ICp3X--dxCKf0GyeVgtYbwbnI9wSBzW_56ibEbUYntAApAZQmfcTJcC_x8pmFBVUJqfVQT-ZnBURijeI4Q_hhILvQb4_baU9T3DS5guRWGtGYnKkzf0_BPa2oMeiMFeEDnChKSQ5kt8R0U8qZOf2CPsm-FBnoU1LZvKERmL_00I_K_gD1dIr6kpwx3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb45455c0d.mp4?token=igoagHH2lYINNQq_1vW-AYx0_zoD2iGbheHzdwOMqfW98WA7CNv1-ogzop22IIjHICeIzNd8KVwyT4vdTssjfQhNyx15Es0Yv6n6vtGPetU3coqFTdTWg7glq0W0BUB7mJSo-MasaZZE88LukG6n-OcNQT6ICp3X--dxCKf0GyeVgtYbwbnI9wSBzW_56ibEbUYntAApAZQmfcTJcC_x8pmFBVUJqfVQT-ZnBURijeI4Q_hhILvQb4_baU9T3DS5guRWGtGYnKkzf0_BPa2oMeiMFeEDnChKSQ5kt8R0U8qZOf2CPsm-FBnoU1LZvKERmL_00I_K_gD1dIr6kpwx3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@withyashar
منتظر زارتان زورتان</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/withyashar/13604" target="_blank">📅 03:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13603">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">۳پا باید یه جوابی بده چیزی‌ دیدن یا شنیدین بگین</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/withyashar/13603" target="_blank">📅 02:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13602">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">چندین انفجار در سيريك
🚨
🚨
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/withyashar/13602" target="_blank">📅 02:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13601">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">کانال ۱۴: همه امیدوار بودند که آتش بس برقرار شود، اما بازی به طور کامل در حال تغییر است. برای یک آخر هفته فوق العاده گرم در خاورمیانه آماده می شوند، زیرا ایران و آمریکا از اعتصابات تصادفی شبانه به رویارویی های روز روشن تغییر می کنند!
@withyashar</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/withyashar/13601" target="_blank">📅 02:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13600">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سنتکام : چند لحظه پیش، نیروهای سنتکام چهار پهپاد تهاجمی یک‌طرفهٔ ایرانی را که به سمت تنگهٔ هرمز پرتاب شده بودند، سرنگون کردند. این پهپادهای تهاجمی تهدیدی فوری برای تردد دریایی منطقه ایجاد کرده بودند. در ادامه، نیروهای آمریکا برای دفاع در برابر حملات بیشتر، سایت‌های رادار مراقبت ساحلی ایران در گورک و جزیرهٔ قشم را هدف قرار دادند.
نیروهای آمریکایی همچنان هوشیار هستند و برای پاسخ‌دادن به تجاوز بی‌دلیل ایران در چارچوب دفاع از خود، در حالت آماده‌باش قرار دارند.
🚨
🚨
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/withyashar/13600" target="_blank">📅 02:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13599">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
سنتکام از حمله به سایت های راداری قشم خبر داد!
@withyashar</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/withyashar/13599" target="_blank">📅 02:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13598">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">چندین انفجار در سيريك
🚨
🚨
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/withyashar/13598" target="_blank">📅 02:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13597">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سی‌بی‌اس نیوز به نقل از یک مقام آمریکایی: نیروهای آمریکایی حداقل ۴ پهپاد را که توسط ایران به سمت تنگه هرمز پرتاب شده بود، سرنگون کرده‌اند.
🚨
@withyashar
بچه جنگ شده باز</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/withyashar/13597" target="_blank">📅 02:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13596">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">⚠️
@withyashar
گول نخوری !</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/withyashar/13596" target="_blank">📅 01:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13595">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">فقط در ۴ ماه ! بسوزید عرزشی ها</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/withyashar/13595" target="_blank">📅 01:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13594">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">💥
290k عرزشی سوز ترین کانال تلگرام</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/13594" target="_blank">📅 01:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13593">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">گزارش هایی از قطع شدن اینترنت
@withyashar</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/withyashar/13593" target="_blank">📅 01:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13592">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">سی ان ان : منابع می گوید ایران چندین پهپاد را به سمت تنگه هرمز پرتاب کرده است. نیروهای ایالات متحده حداقل 3 تا از آنها را رهگیری کردند
@withyashar
🚨</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/withyashar/13592" target="_blank">📅 01:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13591">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">دوتا صدای انفجار الان ومد همین الان قشم
🚨
@withyashar</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/13591" target="_blank">📅 01:41 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13590">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">مجری ان‌بی‌سی: رهبران جمهوری اسلامی معتقد نیستن که به‌طور کامل شکست خوردن.
ترامپ: ایران به دلیل تصور برخورداری از قدرت کافی، از امضای توافق خودداری کرده. ایران در نهایت گزینه‌ای جز توافق نخواهد داشت.
@withyashar</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/13590" target="_blank">📅 01:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13589">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترامپ به ان بی سی:
خیلی از مقاماتشون مغرورن، یه سری کارها هست که هیچوقت فکر نمی‌کردن مجبور بشن انجام بدن ولی الان مجبور شدن، راه دیگه‌ای ندارن و این قضیه زمان می‌بره.
داریم درباره 47 سال حرف میزنیم که هر کاری خواستن انجام دادن.
@withyashar</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/withyashar/13589" target="_blank">📅 01:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13588">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ترامپ به NBC : وضعیت برای اونا واقعاً سخته
یه جورایی استقلال زیادی هم دارن، ولی سال‌ها با یه رهبری ضعیف و بی‌اثر از طرف آمریکا و بعضی کشورهای دیگه طرف بودن؛
طوری که عملاً گذاشتن هر کاری دلشون خواست بکنن.
من فکر می‌کنم خودشون هم الان باورشون نمی‌شه به اینجا رسیدن؛ جایی که عملاً خیلی ضعیف شدن
@withyashar</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/withyashar/13588" target="_blank">📅 01:30 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13587">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترامپ به شبکه ان بی سی: رهبران ایران چاره ای جز رسیدن به توافق ندارند‌‌
@withyashar</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/withyashar/13587" target="_blank">📅 01:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13586">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامپ به شبکه ان بی سی: ایران بین 21 تا 22 درصد موشکهای خود را در اختیار دارد‌‌ @withyashar</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/withyashar/13586" target="_blank">📅 01:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13585">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامپ به شبکه ان بی سی: ایران بین 21 تا 22 درصد موشکهای خود را در اختیار دارد‌‌
@withyashar</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/withyashar/13585" target="_blank">📅 01:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13584">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">به نظر می‌رسد جنگنده‌های اسرائیلی از عراق به سمت ایران می‌آیند
@withyashar</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/withyashar/13584" target="_blank">📅 01:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13583">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ارسالی : پدافند ۱۷ شهریور گنبد کاووس فعال شد @withyashar</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/withyashar/13583" target="_blank">📅 01:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13582">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ارسالی : پدافند ۱۷ شهریور گنبد کاووس فعال شد
@withyashar</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/withyashar/13582" target="_blank">📅 01:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13581">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">به خبرای هست ولی نمیتونم ثابت کنم</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/13581" target="_blank">📅 01:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13580">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/withyashar/13580" target="_blank">📅 01:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13579">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">گزارشهایی از صدای جنگنده و پدافند در شمال کشور
🚨
@withyashar</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/withyashar/13579" target="_blank">📅 00:58 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13578">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامپ: ما خیلی سریع از ایران خارج خواهیم شد و نتیجه آن، به هر شکل، بسیار قوی خواهد بود؛ چه از طریق یک تکه کاغذ (توافق) و چه از راهی بسیار سخت‌تر. شاید حتی راه بسیار سخت‌تر، آسان‌تر هم باشد.
اما ما از این مسئله عبور خواهیم کرد و قیمت کود شیمیایی شما به‌شدت کاهش خواهد یافت، درست همان‌طور که چهار ماه پیش بود. قیمت کود شیمیایی اکنون هم کاهش یافته است.
قیمت انرژی، نفت و گاز نیز همگی به‌طور قابل‌توجهی پایین خواهند آمد. و صادقانه بگویم، من تصور می‌کردم قیمت‌ها بسیار بیشتر از این افزایش پیدا کنند.
@withyashar</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/withyashar/13578" target="_blank">📅 00:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13577">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">گزارش های تایید نشده : چندین جت جنگنده آمریکایی حمله‌ای را به بندرعباس و مناطق اطراف جزیره خارک آغاز کردند و چندین بندر از جمله فرودگاه بندرعباس را هدف قرار دادند. پدافند هوایی فعال شد و درگیر نبرد شدیدی با جت‌های جنگنده شد.
@withyashar</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/withyashar/13577" target="_blank">📅 00:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13576">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گزارش هایی از شلیک نیروهای ایرانی به سمت ناو های آمریکایی
🚨
@withyashar</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/13576" target="_blank">📅 00:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13575">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">شنیده شدن صدای انفجار در جزیره خارک
🚨
@withyashar</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/withyashar/13575" target="_blank">📅 00:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13574">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">@withyashar
only for pro members</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/withyashar/13574" target="_blank">📅 00:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13573">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">@withyashar
operation economic fury</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/withyashar/13573" target="_blank">📅 00:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13572">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/withyashar/13572" target="_blank">📅 00:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13571">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">انفجار ناشناس در نزدیکی کنسولگری ایران در استان سلیمانیه در شمال عراق.
@withyashar</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/withyashar/13571" target="_blank">📅 23:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13570">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQXoxSErWxrH8ySeQCufQPWQJXUepTJJlLXite4fshR4xmTTTbGBqopUJIISpDhfR2t8WTwcazQ-Vpl7-szs2lMmMujVnLv0vqK6VoI1HV27gsRvp7ITC1cEMFlN0LXZjdXOBLC1RZAz8g3aJdCDmAje3621WUjUlZX4qHlFzXi-S7D7-sJ__scfgpdgXaeSAzWO5AfZAj6pKvGdvpOzDCVXL6wcSJoTSz8-9O0TDSb_UfcPSJQFLmtrMGsNMzfnXEdDjiCd_YfsZD0EgP7a2eAhQpabVrOEefNA7imJeOB2YB8DlLfsge2PQYONlPipPN9R-K2V5KjLqfD5fFUEow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواستگاری جنجالی قیصر از الهام چرخنده در تجمعات حکومتی
قیصر در یکی از تجمعات حکومتی، به‌صورت علنی از الهام چرخنده، بازیگر سابق تلویزیون ایران، درخواست ازدواج کرد. این اتفاق غیرمنتظره خیلی زود در فضای مجازی و رسانه‌ای مورد توجه قرار گرفت و واکنش‌های زیادی را به دنبال داشت
@withyashar</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/withyashar/13570" target="_blank">📅 23:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13569">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">شبکه ۱۲ اسرائیل به نقل از رئیس ستاد ارتش این رژیم: قصد نداریم از سرزمین‌هایی که در لبنان پیشروی کرده‌ایم، خارج شویم
@withyashar</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/withyashar/13569" target="_blank">📅 22:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13568">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اکسیوس: استیو ویتکاف و جرد کوشنر به طور مخفیانه از تأسیسات هسته‌ای اوک ریج در تنسی بازدید کردند تا با برترین کارشناسان هسته‌ای آمریکا دیدار کنند، در حالی که مذاکرات با ایران وارد مرحله حساسی شده است. @withyashar</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/withyashar/13568" target="_blank">📅 22:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13567">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">اکسیوس: استیو ویتکاف و جرد کوشنر به طور مخفیانه از تأسیسات هسته‌ای اوک ریج در تنسی بازدید کردند تا با برترین کارشناسان هسته‌ای آمریکا دیدار کنند، در حالی که مذاکرات با ایران وارد مرحله حساسی شده است.
@withyashar</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/withyashar/13567" target="_blank">📅 22:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13566">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">گزارشگر: بازی که شما می‌روید  ببینید ارزان‌ترین قیمت بلیت ۸۰۰۰ دلار است. مردم عادی آمریکا نمی‌توانند بلیت این رویدادهای ورزشی را بخرند.
ترامپ: می‌توانید آن را از تلویزیون تماشا کنید. تماشای آن از تلویزیون تا حدی رایگان است.
@withyashar</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/withyashar/13566" target="_blank">📅 21:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13565">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ترامپ درباره پوتین و زلنسکی:
بگذارید خودشان حل کنند. من کسی هستم که آن‌ها را به این موقعیت رساندم.
@withyashar</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/withyashar/13565" target="_blank">📅 21:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13564">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ درباره جان بولتون:
فکر می‌کردم او در زمینه جنگ رادیکال است، نه در زمینه چیزهای دیگر.
او می‌خواست با هر کسی که دهانش را باز می‌کرد وارد جنگ شود.
او همیشه می‌خواست مردم را بکشد. من هرگز به او گوش ندادم.
@withyashar</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/withyashar/13564" target="_blank">📅 21:33 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13563">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ درباره ایران دم مسترا:
ما در رابطه با ایران موفقیت‌های بزرگی کسب کرده‌ایم.
آنها در موقعیتی نیستند که سلاح هسته‌ای داشته باشند.
ترامپ:
پیت هگستث معلوم شد که یک گوهر است.
@withyashar</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/withyashar/13563" target="_blank">📅 21:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13562">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/682cd2dd57.mp4?token=W788ZZdY_iEufFfnCSXboCI0NHzpdSMgrkSgdL9YRDcvjCLoFCb2H7qmNWAQ-FhrFDcHnyFRvDZGS89EysNy9ppqqG9VbclQoYfwpmC-W2tjc6Lxb1agW_CfU8aMJA8lfxokWINa25c8u7fzTSAbAVI8HACI4VE1oJ6-gtScJJ39ZHC7KoH8dZxMGaCNVeSjJgAQva8Z3XSAopxRo6iU2XH7CKCvQgtG3lEJ4IT4uxM8UjUIEgDOzvUeJmmSjAujyVaDLnNoNHFswbzuMAPxTFAmouFEFvt0zqJuLjQhmfv13mLKF_4H-joDF8nTisX231TgG0UJuyIVUuRDgg30rzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/682cd2dd57.mp4?token=W788ZZdY_iEufFfnCSXboCI0NHzpdSMgrkSgdL9YRDcvjCLoFCb2H7qmNWAQ-FhrFDcHnyFRvDZGS89EysNy9ppqqG9VbclQoYfwpmC-W2tjc6Lxb1agW_CfU8aMJA8lfxokWINa25c8u7fzTSAbAVI8HACI4VE1oJ6-gtScJJ39ZHC7KoH8dZxMGaCNVeSjJgAQva8Z3XSAopxRo6iU2XH7CKCvQgtG3lEJ4IT4uxM8UjUIEgDOzvUeJmmSjAujyVaDLnNoNHFswbzuMAPxTFAmouFEFvt0zqJuLjQhmfv13mLKF_4H-joDF8nTisX231TgG0UJuyIVUuRDgg30rzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ بیرون کاخ سفید با خبرنگارا حرف نزد، و قبل از سوار شدن به ایر فورس وان هم هیچ مصاحبه‌ای نکرد، ببینیم دم توالت چیزی میگه یا نه
@withyashar</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/withyashar/13562" target="_blank">📅 21:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13561">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">جروزالم پست:  منابع اطلاعاتی اسرائیل معاون رئیس‌جمهور جِی‌دی ونس را متهم می‌کنند که نقشه موساد برای استفاده از نیروهای کرد علیه ایران را مستقیماً به اردوغان لو داده است، که سپس اردوغان به ترامپ فشار آورد تا آن را لغو کند. خط قرمز اردوغان: هیچ نیروی نظامی کردی…</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/withyashar/13561" target="_blank">📅 20:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13560">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">جروزالم پست:  منابع اطلاعاتی اسرائیل معاون رئیس‌جمهور جِی‌دی ونس را متهم می‌کنند که نقشه موساد برای استفاده از نیروهای کرد علیه ایران را مستقیماً به اردوغان لو داده است، که سپس اردوغان به ترامپ فشار آورد تا آن را لغو کند.
خط قرمز اردوغان: هیچ نیروی نظامی کردی در نزدیکی مرزهای ترکیه نباشد.
@withyashar</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/withyashar/13560" target="_blank">📅 20:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13559">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بلومبرگ: طبق داده‌های ناوبری، رفت‌وآمد کشتی‌ها از تنگه هرمز تو ۲۴ ساعت گذشته به‌شدت کم شده
@withyashar</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/withyashar/13559" target="_blank">📅 20:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13558">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">️حمام خون در بازار کریپتو!  بیش از ۶۳۵ میلیارد دلار تنها در کمتر از ۵ روز از ارزش کل بازار رمزارزها محو شده است. @withyashar</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/13558" target="_blank">📅 19:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13557">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">آلمان با صدور هشدار امنیتی برای شهروندانش، نسبت به سفر به خاورمیانه هشدار داد و دلیل اون رو احتمال تشدید دوباره تنش‌ها و اختلال در پروازها عنوان کرد.
@withyashar</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/withyashar/13557" target="_blank">📅 18:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13556">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">سنتکام:
ادعای نادرست: ایران ادعا میکنه که به سمت کشتی‌های جنگی ایالات متحده در خلیج عمان تیر هشدار شلیک کرده و کشتی‌های آمریکایی رو مجبور به «عقب‌نشینی» به سمت اقیانوس هند کرده.
حقیقت: نیروهای ایرانی به کشتی‌های جنگی نیروی دریایی ایالات متحده حمله نکرده یا به سمت آنها شلیک نکردن. انجام این کار نقض فاحش آتش‌بس خواهد بود. نیروهای آمریکایی همچنان آزادانه در آب‌های منطقه‌ای فعالیت می‌کنند و در عین حال محاصره مداوم علیه ایران رو به طور کامل اجرا می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/withyashar/13556" target="_blank">📅 17:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13555">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Gloria2018Remaster(IG @yashar)</div>
  <div class="tg-doc-extra">Umberto Tozzi (t.me/withyashar)</div>
</div>
<a href="https://t.me/withyashar/13555" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🌐
@withyashar
🌐
instagram.com/yashar</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/withyashar/13555" target="_blank">📅 17:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13554">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f252f83e0d.mp4?token=JSkxS_Dmw4lUPnDyW_vlp7pVsJ3syWPaJpYQ9L4kjsXgewNr1KUWnXBm2sPizWygzoKZbrEfHpXxXUEdH7dWDHRJ0KmTSp2BtOFwmC8ns8RqmWCO3E8hUlviu7J8yVlHea7n_OcYThzwNwqI_go990SJMn_M1T3J_EzEBwd95VMzgkarh-cvLw0jkhw_rAreZnm0nTT2EcuJiwauhp9pGdrzT17hLjWkZGHv1tpPyLqY1F8HdTDN5S2sJrz6_Q9qs7ULfD07zCblwjtq8NHE3BAqMsAzr3Ivok2Xkym9MpBMSE3dnbCZtPBgn6piFY2sjWdDKX_ixLRGNFIhZoB5hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f252f83e0d.mp4?token=JSkxS_Dmw4lUPnDyW_vlp7pVsJ3syWPaJpYQ9L4kjsXgewNr1KUWnXBm2sPizWygzoKZbrEfHpXxXUEdH7dWDHRJ0KmTSp2BtOFwmC8ns8RqmWCO3E8hUlviu7J8yVlHea7n_OcYThzwNwqI_go990SJMn_M1T3J_EzEBwd95VMzgkarh-cvLw0jkhw_rAreZnm0nTT2EcuJiwauhp9pGdrzT17hLjWkZGHv1tpPyLqY1F8HdTDN5S2sJrz6_Q9qs7ULfD07zCblwjtq8NHE3BAqMsAzr3Ivok2Xkym9MpBMSE3dnbCZtPBgn6piFY2sjWdDKX_ixLRGNFIhZoB5hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ ویدئویی جدیدی در شبکه تروث منتشر کرد که در حال بازی گلف است و یک ضربه فوق‌العاده میزند. همچنین از آهنگ معروف گلوريا لذت میبرد.
یاشار: آخرین باری که این آهنگ ویرال شد در فیلم گرگ وال استریت بود. مضمون این آهنگ این است که
کنترل نکردن زندگی احساسی می‌تواند خطرناک باشد
توجه زیاد دیگران همیشه خوشبختی نمی‌آورد
باید قبل از اینکه دیر شود، آرام‌تر شد و به خود رسید
@withyashar</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/13554" target="_blank">📅 16:58 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13553">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">رئیس‌جمهور لبنان، ژوزف عون، در مصاحبه‌ای با سی‌ان‌ان ایران را متهم کرد که در رویارویی با آمریکا و اسرائیل از کشور او به‌عنوان یک برگ چانه‌زنی استفاده می‌کند و گفت: «این کشور، کشور شما نیست.»
عون همچنین افزود که مردم لبنان از جنگ میان اسرائیل و حزب‌الله خسته شده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/withyashar/13553" target="_blank">📅 16:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13552">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ماجرای پرواز جنگنده‌ها در ارتفاع پایین بر فراز اصفهان چه بود؟
دقایقی قبل پرواز چند فروند جنگنده در ارتفاع نسبتاً پایین بر فراز برخی مناطق شهر اصفهان مشاهده شد که صدای آن نیز توسط شهروندان شنیده شد.
این جنگنده‌ها متعلق به نیروهای مسلح کشورمان بوده و پرواز آنها در چارچوب مأموریت‌های عملیاتی یا تمرینی انجام شده است و جای نگرانی برای شهروندان وجود ندارد
@withyashar</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/withyashar/13552" target="_blank">📅 16:11 · 15 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
