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
<img src="https://cdn4.telesco.pe/file/jps70UmWBNGMv3gYiRllI7lmTGF_g0G669pexvfo9sPdIjwm0PpMRWG0EEBskWPK1zOyTaCcsCqutzErXhSZG1tKL46R0UoaXU1KUYZbFgsBSSSX_iPVxLlPvBZ-lu_XU4m5PBNU0oCsoSluMVju3_ou30nSehIjkQg3xjfE2lijmsiXAUMpsWP-IUn563-xt9VP_k8ZBLVkljaiQKe-SFQ6EDx1we89A160IEYzIEk1juyNieCvhlyPWbje4uENF5TYUis9WTLaskE5UMGbgTO_IQ2d0ZbB6ZPgYLKD1ZnSl1an71qZwz0SZ8uEDeBDgXA1go2OiC4OQ8-5llq9VA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 953K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-11 15:40:45</div>
<hr>

<div class="tg-post" id="msg-145169">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
گروسی مدیرکل آژانس بین‌المللی انرژی اتمی و سفیر جدید ایالات متحده نزد سازمان‌های بین‌المللی مستقر در وین، در آستانه نشست فصلی شورای حکام دیدار و درباره برخی موضوعات در دستورکار این نشست تبادل‌نظر کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/alonews/145169" target="_blank">📅 15:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145167">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
شبکه اسرائیلی i24: دستیاران ترامپ تلاش می‌کنند پیش از انتخابات میان‌دوره‌ای، جنگ با ایران را «آرام و کنترل‌شده» نگه دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/145167" target="_blank">📅 15:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145166">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MaadOrpITy2qQGoK0PX4ufKIAiJh11VQlJnUkilX2M24imxVa-0YGAKn2b3SeTYNFk2Dzcft0eWloCSSrAh5zd4ORMrcMmLbfVgyShu337Zlzd-dGzZetna4II3hHDaatcpePI4PZM2r_vR8hkykJ1eoWzDPJs2APZw4vqx6LhC6bnHIMu_8l6s_hfZOSdiXlnEPXA3ZZ0kQaK6lWXY2vV0ByheKYAOP6XiWQWmoAXPmKdFggoBTEoyDstOlLYLrG_sVW6_hgrbAcfHCVpuOQRhR1xNBwoRkzlAzdTKOVwwOoYVZTsPPTjH-idGdfVA67KZNJO8DzSlTRN1--2UCDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت بدترین گوشی قابل خرید در بازار :
🔴
آذر پارسال، ۷/۵ میلیون تومان
🔴
قیمت امروز ۵۰ میلیون تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/145166" target="_blank">📅 15:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145165">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا به فاکس نیوز گفت: پیام من به همه این است که از ایران دوری کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/145165" target="_blank">📅 15:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145164">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OTzg9nYcDN8p5at-k5gxDRymr4JuLGkMWxDBQbyW3LPJZBngv1kuXTG1VzP0t-oqIgOHWP6UAypG7lpolsq8I7smrEMlECRhu738RD07MNKtH8xLjGL7fMUee9MTxQB1d6oGwO0Yr5zbcRdKK6zCzGJIV52GHSbezVKlL-l0Ok9WjRjHd82ouRzCNVehpAg3njgKU4RJ3my0qJpk1RqGc9PJSXlEcEp6B6KWHvSNlh_cF5lgyzYsU3_vrSswYIAMlqxttvrHgyOTzlL-bovBEl1_ufeNcOTNSZE46TlGijPEAlTIAbHjEtMdaVaCW3yFayMOFxMn3oE0T6ekUcDXfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دفتر عملیات تجارت دریایی بریتانیا (UKMTO) از وقوع یک حادثه امنیتی مرتبط با یک نفتکش خبر داد که در پی آن دو نفر کشته یا زخمی شده‌اند و این حادثه در حال بررسی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/145164" target="_blank">📅 15:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145163">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
حاجی دلیگانی، مجلس: پایگاه های آمریکا در اروپا باید هدف قرار گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/145163" target="_blank">📅 15:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145162">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VHz1Nm1ImWHmAm5QVajJpLCF3z9LPp0kQPue4JzByjLWLIN1xsO8tbLIgXoJU3VfLaaJNl1CRb-xqvxRhA5cKgyK6U98gdl-nUzSgLH83kd_OqElrqSgvhiY9JnKBIqzgBQ1bJViUurzkJqiDV8ahbS4oQsazgHyeEAbw5hJ4h-x1Nl-7TFjKG6M40yy1NUvr2zA0rQPgxJoFR2APRQhPqp_qfSQaIyoSx7i5Yj19LHgTWOXD8AugYESl8ILTbfvBilGZgXapfQkJbg7Uz2WT1ruOBfC7UqcE0vjNq7-uqvvgvDR0kIftJBCFYAjI11pRJzEovAK9fZTO9LvbCVoEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شرکت شورون (Chevron) اعلام کرد پس از رسیدن به توافق با دولت ونزوئلا، فعالیت‌های خود را در کمربند نفتی اورینوکو در این کشور گسترش خواهد داد.
🔴
این شرکت قصد دارد طی پنج سال آینده بیش از ۷ میلیارد دلار سرمایه‌گذاری کند و تولید نفت را بیش از دو برابر کرده و به حدود ۶۰۰ هزار بشکه در روز برساند.
🔴
شورون اعلام کرد انتظار می‌رود هزینه کل پروژه‌ها کمتر از ۲۰ دلار به ازای هر بشکه باشد و ونزوئلا را بستری برای رشد بلندمدت و کم‌هزینه تولید نفت توصیف کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/145162" target="_blank">📅 15:08 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145161">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qu1joHPbJAvTrOmDPjcc3ZV85p0mz3gaBK776d_RleJCja0XfRaZ-IDDvi5QtpDfWjUA2tlKKNX6ZithvWa15z25UT8d1SFD0x2yXILgwf1Kb3WPYaoZqzfqWQ2OanEFWzrHy0txEC5nODYGMdBjPNLBVT1UWqiUwXkB-ap9f7PzPqJogJmQohcJkH7Rk5JVWe2OoyRbIxeORdkyfaieiitjNyyej4He8kbG5k65CRfW1-JMHDQ4teGfbRXbvbs8nuWVzYDBttLqHjtcERgtcdcqri_pim53xWnk7DYjJK8Ihn3w3P6GWnj7Z1hktMIGdH2zaa3Wj5O1W8WR0qFgUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلدمارشال محسن رضایی: با این همه تلاش‌های بیهوده، نه تنها از این وضعیت وخیمی که خودتان برای خودتان ایجاد کرده‌اید، خارج نخواهید شد، بلکه به زودی متوجه خواهید شد که استراتژی جدید ایران در میدان نبرد، در عرصه دیپلماسی و در مقابله با محاصره اقتصادی، بنیان‌های شما را به طور کامل فرو خواهد ریخت
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/145161" target="_blank">📅 15:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145160">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32e2c83d9a.mp4?token=lDd5facbXeEYnd57-Zbs3bZX4Unp1H3f0E3K2IaEAqCGl4aaIxY4m2q8cf9UMVQbm6Frc4WlycSMAO5uXwekMHgTvTnxxf-WJ4suzLSIznq0GzccVnrEV9kWuu25_jVOxH-EgLBOs9JB9r4K46ItsrgzJu3iAci1NwOy6BRHpK8FZrX3LVA7AhMaYqIDBnO2K0YBkyr5a4ktMG_sz_LA-1skaWjq6uMfuWS61IV3wB7P0NqlKfzcbcuMRYb4AOFf59nhIuyyQNR5B4OQ6IU3ES4z48s2vXcCgl_7o6QRw18bMfQBOHUKIq28niS9AeXDxA8atzJq79zEkCHBtpDVGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32e2c83d9a.mp4?token=lDd5facbXeEYnd57-Zbs3bZX4Unp1H3f0E3K2IaEAqCGl4aaIxY4m2q8cf9UMVQbm6Frc4WlycSMAO5uXwekMHgTvTnxxf-WJ4suzLSIznq0GzccVnrEV9kWuu25_jVOxH-EgLBOs9JB9r4K46ItsrgzJu3iAci1NwOy6BRHpK8FZrX3LVA7AhMaYqIDBnO2K0YBkyr5a4ktMG_sz_LA-1skaWjq6uMfuWS61IV3wB7P0NqlKfzcbcuMRYb4AOFf59nhIuyyQNR5B4OQ6IU3ES4z48s2vXcCgl_7o6QRw18bMfQBOHUKIq28niS9AeXDxA8atzJq79zEkCHBtpDVGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پوتین : به ارتش دستور داده‌ام زیرساخت‌های انرژی اوکراین را به شدت هدف قرار دهند زیرا آنها به زیرساخت های انرژی ما آسیب رسانده‌اند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/145160" target="_blank">📅 14:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145159">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
العربی الجدید به نقل از رئیس‌جمهور چین: پکن آماده است با کشورهای خاورمیانه برای حفاظت از امنیت خطوط کشتیرانی بین‌المللی همکاری کند.
🔴
از قدرت‌های خارجی می‌خواهم استانداردهای دوگانه خود را در قبال خاورمیانه کنار بگذارند.
🔴
پکن و قاهره همکاری‌های امنیتی را تقویت کرده و از تلاش‌های یکدیگر برای مبارزه با تروریسم حمایت می‌کنند.
🔴
مردم خاورمیانه باید همچنان سرنوشت امور خود را در دست داشته باشند و با مداخله خارجی مخالفت کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/145159" target="_blank">📅 14:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145158">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
رویترز: نفت با تشدید دوباره درگیری آمریکا و ایران، به بالاترین سطح چند هفته اخیر رسید
🔴
نفت برنت در معاملات امروز تا ۹۷.۰۴ دلار و نفت آمریکا تا ۹۲.۲۹ دلار در هر بشکه صعود کرد.
🔴
تیم واترر، تحلیلگر ارشد بازار، به رویترز گفت: اگر مرحله کنونی تشدید درگیری ادامه پیدا کند، بازگشت نفت به محدوده ۱۰۰ دلار را نمی‌توان منتفی دانست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/145158" target="_blank">📅 14:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145157">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
کرملین: در جریان مذاکرات رئیس‌جمهور ایران با پوتین، هیچ درخواستی از سوی رئیس‌جمهور ایران برای میانجیگری با واشنگتن دریافت نکردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/145157" target="_blank">📅 14:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145156">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
ریاست‌جمهوری مصر: مصر و چین بر ضرورت در اولویت قرار دادن دیپلماسی برای دستیابی به توافقی جامع جهت توقف جنگ در خاورمیانه توافق کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/145156" target="_blank">📅 14:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145155">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejn3Xo1dpJGm4fSfZilarGmilfWs_m0pxCWtAxU2bqY4WMz2EFm5qyZaeoJuTWxuvbMXLs96tV7IsEQDy3BYhuo6HIzJ9TVM4MCFs6jwNS4nHTmFn7AiRj1Apkl4uzYi_B1dKEX8YlBmgJPC5RIjTLlnETHFi7V7AO93pqm_zPlyijMSGf6CHYjPDLkoHohzCiz6dE_TMNJ1WMHrLVv4i9PwQBfM2AY6NS7XUo_o6bXPwPCK7lJjUSoc2oBU32g_CZSLk0uB-QnZmC2A-QE-PWd0AEv8u48AiCv2YpLGTubfOPqHUdZeZiXffx61ipxAo3V9uJEoBF2Gqv0oYIpF2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمید رسایی: آقای پزشکیان! موشک‌های آمریکایی با کارت دعوت شما به عروسی سیریک رفتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/145155" target="_blank">📅 14:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145154">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DV2AmnN3NZsSriPnhwjTRmwC4SNihvF3jCpCSK1BrdTikNYwdcljyNAMU-6AU6U4r1kCS6QQ-YzLRg60YR_xytWz8HlqI4U-UpT3250pefKyvuxUT4msGRB7NdRWcORSrA8lZQfILl3NRmmuwbfoK7rHjDFl0iXxbkMw_SBLM3hz66UMMDVDLaGr5TLBzEaoGS2rZ8gH7-aIFElqcFg_m0jza5tFWhAbyLIat70uO9E-P1h9qYRUtrM_1FLuqCor489R38biOJtRYcRAt0aqSzewwzH-tdLydO64F1yf6gPRvhEP-7egT4zRisEqEeCePAvSCBEWB4szgcsH7hwKRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیمای باری روسی متعلق به نیروی‌ هوایی روسیه در آسمان کرج
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/145154" target="_blank">📅 14:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145153">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
چین تنها عضو گروه G20 بود که در نشست وزیران دارایی در کارولینای شمالی، با اجماع مخالفت کرد و با درج عباراتی در حمایت از آزادی کشتیرانی در تنگه هرمز مخالفت کرد.
🔴
چین همچنین با درج عباراتی که
مدل اقتصادی صادرات‌محور این کشور و مازاد تجاری آن
را مورد انتقاد قرار می‌داد، مخالفت کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/145153" target="_blank">📅 14:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145152">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه روسیه به الجزیره: از تشدید تنش‌های اخیر پیرامون ایران متأسفیم و تمام تلاش خود را برای کاهش شدت آن به کار می‌گیریم.
🔴
آنچه در منطقه خلیج فارس رخ می‌دهد، یک ماجراجویی هولناک است که پیامدهای وخیمی به دنبال داشته است.
🔴
بازگشت تشدید تنش‌ها، پیش‌بینی‌های ما را تأیید می‌کند که توافق آتش‌بس اجرا نشده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/145152" target="_blank">📅 14:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145151">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
سفارت آمریکا در عربستان سعودی:به شهروندان آمریکایی مقیم خاورمیانه توصیه می‌شود با توجه به تنش‌های موجود در منطقه، احتیاط لازم را به عمل آورند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/145151" target="_blank">📅 13:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145150">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
آبفا: حدود ۴۱۰ نقطه از تأسیسات آب، فاضلاب و صنعت ما در جنگ ۴۰ روزه، مورد هدف قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/145150" target="_blank">📅 13:48 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145149">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd3cdbaf85.mp4?token=jgBpf---f4r1wyTgsXxxmNfYeBwowsd_nHLgEEMQHx4HRiUWHVbs4Zvg0GxzZMBSZZ8GMfBi_dgKXUmNDZ3N70cyTYfcBw4WBz_0dxHmmVP3fP-u0b83w5CK_IxDSnbzh5eaBjSe2ZxCSe41ynM3U23Y3x-gAK3F1zhBHeljnp2wa2PFJRnxcRhbOyxBzddIbhtQtWSq-_jr_PaE4ssrqU0xmgHtFG4lEhDpWIkSHzuYojwuKqZ_7cPwgL3jru8YD367OaMCH7wmr4wHPL2NsxXvSM78-IAogdd9dET3izFbQHU3UfUhtzYdjNgChboysODW4EIOvJxkiO9C1DT-qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd3cdbaf85.mp4?token=jgBpf---f4r1wyTgsXxxmNfYeBwowsd_nHLgEEMQHx4HRiUWHVbs4Zvg0GxzZMBSZZ8GMfBi_dgKXUmNDZ3N70cyTYfcBw4WBz_0dxHmmVP3fP-u0b83w5CK_IxDSnbzh5eaBjSe2ZxCSe41ynM3U23Y3x-gAK3F1zhBHeljnp2wa2PFJRnxcRhbOyxBzddIbhtQtWSq-_jr_PaE4ssrqU0xmgHtFG4lEhDpWIkSHzuYojwuKqZ_7cPwgL3jru8YD367OaMCH7wmr4wHPL2NsxXvSM78-IAogdd9dET3izFbQHU3UfUhtzYdjNgChboysODW4EIOvJxkiO9C1DT-qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات دقایقی قبل اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/145149" target="_blank">📅 13:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145148">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWBnP5DtkTIYDTJlab8y8ld-y8e9anUMgSdkgtQ8CkUwaV6Dma4dBr7LEoPrLMTN4sSIQ_JvC6Mj7MsiAWbwX7Uhj2gFXk6Xbews01DGNtke_PLvzrKtGFJ-TwdIg6RRis-kjxoeMW85HigxagezVz8hPvO5eM_R7IbtvvTlsu-GFUiVS5hRLxLLjvq9y_vPrEKI-ROPP27LQJjR81UhHDSnHPRVax-lMyQEGDiFu9S2BjOekoTE5xeNgmm1xS1dXQsoJh6fVVZsVB8MluWqRSQbuLB1xUKEP2Zh-DIBPQAxOKQgdrWMNjVMsGsVFu3Jwmj-HAp41GKFJmytK0EPnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر سامانه FIRMS ناسا، وقوع آتش‌سوزی در دو نقطه از فرودگاه بین‌المللی اربیل را پس از حملات شب گذشته ایران نشان می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/145148" target="_blank">📅 13:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145147">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/116dfeb2e5.mp4?token=C8MT2kVnava3m5l0rZOUuvQf0d5TfmYFne6p5QOODGVrdYZHDxD8bp8Yjk9sPCaZl9GtRM7wwrvvQNm1Up4wgfLbsbbvnEBrSNN1FxW73B709Kk3pwISbJQ7wi9Tkv40Rgqc8knhoErW01BBfaakUTV1lN4m9scxcEpiCHu1zwb-Od7bMkzyTEimJTRFiqrB78_zm9nAZWAl8tgbzamL7vZnoN__u_LIPhymKqVjPQqUny--g2VXg0wiJnCiKsEcF1xzR4sXJYoFTKQoE07AxvOKbj5qQBymWttcNqOcAk7S1hCsXllSSe_VOjgPhfmFTL9SDjPhFl10cy2HmmtC8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/116dfeb2e5.mp4?token=C8MT2kVnava3m5l0rZOUuvQf0d5TfmYFne6p5QOODGVrdYZHDxD8bp8Yjk9sPCaZl9GtRM7wwrvvQNm1Up4wgfLbsbbvnEBrSNN1FxW73B709Kk3pwISbJQ7wi9Tkv40Rgqc8knhoErW01BBfaakUTV1lN4m9scxcEpiCHu1zwb-Od7bMkzyTEimJTRFiqrB78_zm9nAZWAl8tgbzamL7vZnoN__u_LIPhymKqVjPQqUny--g2VXg0wiJnCiKsEcF1xzR4sXJYoFTKQoE07AxvOKbj5qQBymWttcNqOcAk7S1hCsXllSSe_VOjgPhfmFTL9SDjPhFl10cy2HmmtC8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کلش ریپورت: ویدئویی که نشان می‌دهد پهپاد شاهد-۱۳۶ ایران صبح امروز به مقر ناوگان پنجم ایالات متحده در منامه، بحرین، اصابت کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/145147" target="_blank">📅 13:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145146">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a6a11bf6.mp4?token=HlqTK5VPiCAK8mQYKJAh5tnQ8gcvKC0YIuSKxY8E4NiECajPpcuUhGx8n0N8USgIDgxx50zThfJeI15FAOc3IfJDnKJz295H9ZjPlfcKrQHw5kyIImEkE7HCJcG1veOnR_q8BR2H1d6nIlnwlr29PEUc3h3p-aibXZ1DGLAMQW5rYK3BK7X-lgtQ_mIEw3RWSxs2Ma_lFqxefeyNuNXJl7Fgtp7otknZHMwDK2L0TRhzIPq2-spSz0vp5DPFV8b_gcREFZfdtBeaYYpW-pK_0Qe2xY4oWszIhSw-ZYFLQdtZTnj6nfE6w7-dURIOm0Ql0rLRw1J6IvvrvVfPgEddqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a6a11bf6.mp4?token=HlqTK5VPiCAK8mQYKJAh5tnQ8gcvKC0YIuSKxY8E4NiECajPpcuUhGx8n0N8USgIDgxx50zThfJeI15FAOc3IfJDnKJz295H9ZjPlfcKrQHw5kyIImEkE7HCJcG1veOnR_q8BR2H1d6nIlnwlr29PEUc3h3p-aibXZ1DGLAMQW5rYK3BK7X-lgtQ_mIEw3RWSxs2Ma_lFqxefeyNuNXJl7Fgtp7otknZHMwDK2L0TRhzIPq2-spSz0vp5DPFV8b_gcREFZfdtBeaYYpW-pK_0Qe2xY4oWszIhSw-ZYFLQdtZTnj6nfE6w7-dURIOm0Ql0rLRw1J6IvvrvVfPgEddqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کلش ریپورت: ناو جنگی ایالات متحده «ابراهام لینکلن» پس از ۲۸۶ روز متوالی در دریا، رکوردی مدرن برای نیروی دریایی ایالات متحده، در ۲ سپتامبر به بندر لِم چابانگ تایلند رسید.
🔴
انتظار می‌رود هزاران نفر از پرسنل این ناو به شهر پاتایای نزدیک سفر کنند و کسب‌وکارهای محلی برای افزایش گردشگری و هزینه‌کرد آماده‌سازی شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/145146" target="_blank">📅 13:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145145">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
مجلس دوفوریت طرح برخورد با ماینرهای غیرمجاز را تصویب کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/145145" target="_blank">📅 13:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145144">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
سفارت آمریکا در بغداد و کنسولگری آن در اربیل در یک هشدار امنیتی فوری از تمام اتباع این کشور در عراق خواستند که خود را برای شرایط اضطراری آماده کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/145144" target="_blank">📅 13:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145143">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
شرکت ملی کشتیرانی عربستان سعودی وقوع حادثه برای نفتکش «سدر» در حین عبور از تنگه هرمز را تائید کرد.
🔴
بر اساس اعلام این شرکت ، این حادثه که در تاریخ ۳۱ اوت رخ داد، دو نفر جان خود را از دست دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/145143" target="_blank">📅 13:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145142">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
اختلال در تأسیسات آب‌شیرین‌کن اسرائیل
🔴
توقف هم‌زمان فعالیت چند تأسیسات آب‌شیرین‌کن در جنوب اسرائیل، گمانه‌زنی‌هایی را درباره احتمال یک حمله سایبری به زیرساخت‌های حیاتی آب به دنبال داشته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/145142" target="_blank">📅 13:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145141">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WuqaJ_R0j67lEDXHVF5CkLxdB6xrPohbecLarScWR2iaSyEiwIyoONhO_LIKl-2SyBlUqtz_GUvfxvjF8Tez95RIaY-2DL71MFBoKqgsonz3urauHMIYByov7wpmG1kZGM7ZpveoypLLUCsW5ehunSwcecsWXy7sMXIIq1eAuZJYAU_W-5vgHAWblLZWMZmwadX1ecqrmbMBbW1qGrDWHTKmT8U7Nl2ElFa-EQdFtUmmuYvX5AX0WnaK8BuH9hucZqTcRQWCSJYYBP9z-TOHNXEAg126LL4e10TA_1UbRwqqPzK2mnvlqs3iNmCax_i6mnLrGmNoqiz4za8UIptsiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارسال پیام وضعیت اضطراری از سوی یک فروند بالگرد آمریکایی بر فراز آسمان امارات
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/145141" target="_blank">📅 12:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145140">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
پولیتیکو گزارش داده طرح ۱۰۰ میلیارد دلاری ترامپ برای افزایش تولید نفت ونزوئلا با تردید جدی کارشناسان صنعت روبه‌رو شده است.
🔴
به گفته کارشناسان، توسعه میادین نفتی این کشور می‌تواند دست‌کم یک دهه زمان و صدها میلیارد دلار سرمایه نیاز داشته باشد؛ زیرا بسیاری از میادین با کمبود زیرساخت‌هایی مانند خطوط لوله، برق و تجهیزات تولید مواجه‌اند.
🔴
همزمان، پرسش‌هایی درباره وجاهت حقوقی توافق، دوام سیاسی آن و توان شرکت نسبتاً ناشناخته طرف پروژه برای مدیریت چنین طرح عظیمی مطرح شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/145140" target="_blank">📅 12:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145139">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
سازمان دارو: واکسن آنفلوآنزا نیست، ماسک بزنید!
🔴
انجمن داروسازان اعلام کرده امسال به تعداد بسیار کم برای بیماران خاص، زنان باردار و کادر درمان واکسن آنفلوآنزا وارد شده، اما عملا این واکسن در کشور وجود ندارد چون مسیرهای انتقال ارز و دارو بسته است و سازمان غذا و دارو نتوانسته به‌موقع واکسن سفارش دهد. سفارش واکسن باید شش تا هشت ماه قبل انجام شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/145139" target="_blank">📅 12:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145138">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
چین: تنگه باید گشاد شه
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/145138" target="_blank">📅 12:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145137">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
فایننشال تایمز: تنش‌ها میان اسرائیل و انگلیس بیشتر می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/145137" target="_blank">📅 12:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145136">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/600c9063c3.mp4?token=GxisldFMMqfJJEphkBIs8i1P7ZQM90rSFAY6xByUTSCHz5n8LDODIrbDynLfeH2Hv3XrNMWDxNK1nPXW3VbrMkFiqnHtjydAWRGiiA9i537_wokxxtjEnU5NytsyRipI4jQ-BGI5ugQ1HiQd4nZxLYK93OzTUbmjHn6vzbU28Q8HnfL0OAoIgzCbnGRHjf0T8-kzRi02o3ZVfEa6Mkqhz0tP5BQvp1H4Uk08QaX5FU-PgWfnfvgc1iSy6DuPUSj9J1EeSzLey89kP-2eVeWOs9shEqGt98ZsCRgqqIzVzx21UaA8srqhbQtquG3vIhU8DkOukxO6wA7lbiuwQPc1kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/600c9063c3.mp4?token=GxisldFMMqfJJEphkBIs8i1P7ZQM90rSFAY6xByUTSCHz5n8LDODIrbDynLfeH2Hv3XrNMWDxNK1nPXW3VbrMkFiqnHtjydAWRGiiA9i537_wokxxtjEnU5NytsyRipI4jQ-BGI5ugQ1HiQd4nZxLYK93OzTUbmjHn6vzbU28Q8HnfL0OAoIgzCbnGRHjf0T8-kzRi02o3ZVfEa6Mkqhz0tP5BQvp1H4Uk08QaX5FU-PgWfnfvgc1iSy6DuPUSj9J1EeSzLey89kP-2eVeWOs9shEqGt98ZsCRgqqIzVzx21UaA8srqhbQtquG3vIhU8DkOukxO6wA7lbiuwQPc1kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مردی در نیویورک آمریکا پس از برخورد مستقیم صاعقه به پایش جان سالم به در برد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/145136" target="_blank">📅 12:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145135">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
روابط عمومی سپاه : دو فروند کشتی نفتکش متخلف با رفتن روی مین منفجر و متوقف شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/145135" target="_blank">📅 12:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145134">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=IHQS7Wa2R2zslIZ3vtMgswkM7W53DlusFxbdxt11V0dECgtHeUsJ3zOvAaOclbCdfkLQaKnllVl_ZFlu4fIG1y-FFkZKOYwYRjlbj4XMFBHrXR-mB6UO8OFu4D3yzWUT8IWr-XwoySfQSd87lIjl79m3g2aLE2GLYhS5ZDEkwnRYi5vYJnqGI7kV0tsSk2-9T5d8B0OwU36Zg_PtMQa9pa3VKQfriOoiBy-h4VCVn3xafnRj5ZmOhmml1w5wwdnxuH0imPuaxBVQd6DmmqWK4wsDpon8N_MxicCsSW5iKtARkL6bCZ4wCYn_Q5dNl022P510LRX_L67wLJUYicmcag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=IHQS7Wa2R2zslIZ3vtMgswkM7W53DlusFxbdxt11V0dECgtHeUsJ3zOvAaOclbCdfkLQaKnllVl_ZFlu4fIG1y-FFkZKOYwYRjlbj4XMFBHrXR-mB6UO8OFu4D3yzWUT8IWr-XwoySfQSd87lIjl79m3g2aLE2GLYhS5ZDEkwnRYi5vYJnqGI7kV0tsSk2-9T5d8B0OwU36Zg_PtMQa9pa3VKQfriOoiBy-h4VCVn3xafnRj5ZmOhmml1w5wwdnxuH0imPuaxBVQd6DmmqWK4wsDpon8N_MxicCsSW5iKtARkL6bCZ4wCYn_Q5dNl022P510LRX_L67wLJUYicmcag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
طلای ۱۸عیار 22,500,000
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/145134" target="_blank">📅 12:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145133">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
دلار 220هزار تومان
‼️
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/145133" target="_blank">📅 11:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145132">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
قالیباف: تمام اقدامات آمریکا به تقلید از شیطانه و خود آمریکا هم شیطان بزرگه
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/145132" target="_blank">📅 11:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145131">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
بلومبرگ:قیمت گاز در اروپا بار دیگر افزایش یافت، در حالی که نگرانی‌ها در مورد خطرات احتمالی مربوط به تأمین انرژی از خاورمیانه افزایش یافته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/145131" target="_blank">📅 11:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145130">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
رویترز: قیمت نفت با ۰.۸ درصد افزایش، به ۹۵ دلار و ۴۰ سنت در هر بشکه رسید
🔴
نرخ هر اونس طلا با ۰.۶ درصد کاهش، به ۴ هزار و ۳۰۲ دلار و ۹۹ سنت رسید که پایین‌ترین سطح از ۱۶ مرداد است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/145130" target="_blank">📅 11:36 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145129">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJyuIH8_jkf9ivII5GuW5r1-cS3UszSFYlP_YyJPrDXmAv1F6v0_1kNKl12gca9I-iqJBuvpodb9AAKTBSpMLRCOoKDf2K6Gvl_i7fVW4i8x8I2MwipXtETPvX8IGZL_zPhA0O8EtxJxynvZjqH9bDVhNPUAlMfnu63ruQSkATobPJxGOGLQ-WEmEB63V454gOWDhBTfM6HsrSmII-LxQdZ6pL9sVI45ldcxJWBFmxlH0EgAkRUYPtODo9bk4EkTwkZDsDmlTHqfeU4BoR98eVj3xexPb5oG7Kfnxvc2d5QI63QzCP__id64nq1wQs7lb6ydmIts-sMNY-1G0eabNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از اصابت مستقیم موشک آمریکایی به محل عروسی در کوهستک سیریک
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/145129" target="_blank">📅 11:36 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145128">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل کاتز: هرچه فشارهای اقتصادی بر ایران بیشتر می‌شود، احتمال اینکه آن‌ها به ما حمله کنند، افزایش می‌یابد. آن‌ها معمولاً در تعطیلات یهودیان به حملات اقدام می‌کنند؛ ما برای دفاع و حمله آماده هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/145128" target="_blank">📅 11:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145127">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7nHsVXvW_OESr2bOSnqdzfpH6SWO0joNDMncwljJPwMIxdn6RsNdySZzn7ZQ-M6QbWTTlPbJW5Ya2P6Q85ockErfmlCqbkD2wd4ZJVQ7och2-fKY1cYE0I4I2RiIpcOPm3MswS72YIgFAKmDIFw1rMsSkuQKX6fjrUADdW1dj2z6afIw4f8IVNmwC17xhXMsw9MScdB0eQyXnUqZzJPAEBZuvSen0mQDp_9TiDKOq9ljaktDn9Yf3RUOzPjhPX5W8m_JoaZEbRlEq-IY5lmAT6zZ01iiD4E1fs9VxipMvtiMwWAnGH55dzBJudbIUCicT1HErlrFxumlYf_Zm85lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمد صادقی، بازیگر و از افراد کادر اپوزیسیون با انتشار یک پست از رضا پهلوی اعلام برائت کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/145127" target="_blank">📅 11:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145125">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/517285c58a.mp4?token=JXqA2Nm66pRcDI5H8peOeV94UgM2YKTm4nrTvt3CCiaBhO6QfOy2AuT5AYFX5wj4XqA8mzEi6ADblpcznnRPnQ45mxflPkoW6nnj8ZxK1-HcrxdR3F8N9JX1jW5g0jENTBMEcjIz-CiC4olqlZkKuUIUfP9UrbMVmuJs6x_A_rRkH3sQNnVC-ex04KQ2EDCBtH6VjpG3Bv3AHCLX3gd0k45Ecc4leoYCy8lu-gwgxanU8mLa2sSayFisupmVoV7F8TNbuw_RdgBG_pRt1HadWCspj37MIv-Mf0wi5IJYddXIALnPKiHpjFuTn4Vzq7-wOfhMnuQ4X5mtwcE6EYzjfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/517285c58a.mp4?token=JXqA2Nm66pRcDI5H8peOeV94UgM2YKTm4nrTvt3CCiaBhO6QfOy2AuT5AYFX5wj4XqA8mzEi6ADblpcznnRPnQ45mxflPkoW6nnj8ZxK1-HcrxdR3F8N9JX1jW5g0jENTBMEcjIz-CiC4olqlZkKuUIUfP9UrbMVmuJs6x_A_rRkH3sQNnVC-ex04KQ2EDCBtH6VjpG3Bv3AHCLX3gd0k45Ecc4leoYCy8lu-gwgxanU8mLa2sSayFisupmVoV7F8TNbuw_RdgBG_pRt1HadWCspj37MIv-Mf0wi5IJYddXIALnPKiHpjFuTn4Vzq7-wOfhMnuQ4X5mtwcE6EYzjfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
‏ جی.دی.ونس: در حال حاضر، سعی می‌کنم تا حد امکان بر انجام کار خدا تمرکز کنم. واگر این کار در نهایت به آخرالزمان منجر شود، اشکالی ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/145125" target="_blank">📅 11:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145124">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bpf5vOQ6kdqu4V8lI1EE701lym9NlhW0Su_QH7yTXqltBbBRF1cR-LTH3h7tylTiqYqneVMZv5Vsz5FeSHG4LN1MnzzpeMxYLVUSaZA6niarvprqU8kU_panZXAY1MswTYTSKoiBq6ckwQOmbWqJs5udfibk9X3vswjLoO_elsoZ3HRtSN5jioy8kg4Fg6Eq0rgFv-vkrgt3C03z0y2AnvdvOMvwTXca_scQZ0agx6RwChsOYzrDq7i6vuuTSNvViqghD3KafeN43YcXbmWQBAeREPKp8mJ3S-PhQTZLWBwwNn5X6T5T8LcVptasqEujPeLAJ6sBdjn99n45cWL3Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فاصله بین دکل مخابراتی و محل عروسی در کوهستک سیریک حدود ۱۳۶ متر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/145124" target="_blank">📅 11:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145123">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
وزارت امور خارجه پاکستان: ما نسبت به بازگشت آمریکا و ایران به میز مذاکره خوش‌بین هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/145123" target="_blank">📅 11:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145122">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
اسکات بسنت: واشنگتن منتظر خواهد ماند تا ببیند تهران چه زمانی آماده رسیدن به توافق است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/145122" target="_blank">📅 11:08 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145121">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
شجاع خلیل زاده: دو سال فحاشی به من شد و تمامی این فحش‌ها تقدیم به عادل فردوسی پور و خانواده‌اش!
🔴
پ.ن : جوابش با شما
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/145121" target="_blank">📅 11:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145120">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GEHOwpVtD5HScQKTno3dXKhhrNOkMDxrTcdH5O81rGp8dLe6IRMRQ0mqrPXUFuto2B8_dU41cYHJvBNPytfF9i-i8pOtX79OluGMzHOPSFRhotH_fnBdNjDaL4pBVERR-MDeZ-AMQnbsV9iZiaTPUP2rUdLs7AgIMnJK604Ix999eHsI1rl2YmCmMlBjpA6okfcGbIlxKfkeDz4r7lEe51f5rkNGHKr_b17AuVPMxJAJf1DBp9u-QALLKzfkSgff7RZq-ocLgJSy3fgjmBAyqJEbVWHLjoSlVm51y3peMuZF3vjl2y-MIhhyrjos0YT2jLWRh6CQzsdpvpKW5wCAnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کنایه خبرنگار WSJ به ترامپ: از «کمک در راه است» تا «چه زمانی مردم ایران قیام و مبارزه خواهند کرد؟»
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/145120" target="_blank">📅 10:59 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145119">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/2f144f954a.mp4?token=NvvJGMSuwiBwLVkxZPULVTtu-LCtmXym07H2oGuWL2LK15BvjyZZQh3VZALeQUeZGrcuSRYXPrn_g51Q5O0RI-S-TxpjFGSSAMzTiKu--2BXauJZB0PwGJ23k2J6nLYcRlyIUXx5joPpxtiIkZ_PUpNg1ZQBGDKwG_So1GsC3rcVBuRGEQt6lLKah9oMOa33jPHGYbTLoo7BEHp9rnjOpKcrs2hcqhtH6Du4YIbpeUxsKHVE5dB03Zl7wQdabd0a8jIyaSb1K1PZH3AAdhoerMbDoKgI9V00oR14HQQ5O5aP9ztrM-J47dnnndeOYS-XLKdydAOiOUtLa3btLVg7eg" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/2f144f954a.mp4?token=NvvJGMSuwiBwLVkxZPULVTtu-LCtmXym07H2oGuWL2LK15BvjyZZQh3VZALeQUeZGrcuSRYXPrn_g51Q5O0RI-S-TxpjFGSSAMzTiKu--2BXauJZB0PwGJ23k2J6nLYcRlyIUXx5joPpxtiIkZ_PUpNg1ZQBGDKwG_So1GsC3rcVBuRGEQt6lLKah9oMOa33jPHGYbTLoo7BEHp9rnjOpKcrs2hcqhtH6Du4YIbpeUxsKHVE5dB03Zl7wQdabd0a8jIyaSb1K1PZH3AAdhoerMbDoKgI9V00oR14HQQ5O5aP9ztrM-J47dnnndeOYS-XLKdydAOiOUtLa3btLVg7eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سنتکام (CENTCOM) تصاویری از حملات به اهدافی در ایران منتشر کرد؛ از جمله یک شناور ناشناس و یک سامانه پرتابگر چندگانه راکتی (MLRS)
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/145119" target="_blank">📅 10:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145118">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
وزارت امور خارجه پاکستان: ما نسبت به بازگشت آمریکا و ایران به میز مذاکره خوش‌بین هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/145118" target="_blank">📅 10:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145117">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8lWQsRQkZGGVD3d4FztfhRuwKCj-gqJQtou2kHt-95j5lvYEV-SoV_kgXaJR4-a94ob4dp5ukvHjuOl73Tw9K-6UT6s17TNSAAGcOXyTQ0jEOUA5gPN8IzQQrsXBBMTfyLBSyt3y5iIB8vqkfGEsd1mkW1cYKjGhZ9KvUMCBtZHWNriWQNjBehujB9Je00bgirCg4Ui3tlmzXxaxhYf3vRdvGRF3lkVGzMtJh8xkzVQ-ljjSxK5omiEZG5AVMV2n8_rlKVe9YOyEFvdx8hftbN1GoImRt5EG9cB6VDS4RmC5jlJCtJ1sOWMdwRc4OAVzWLDxJ0nYM_hr_jgwy9U6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرعشی؛ دبیرکل حزب کارگزاران سازندگی:
قالیباف میخواست بره چین ولی راهش ندادن. گفتن اول این ۴ شرط رو اجرا کن بعدا بیا.
۱. تنگه هرمز رو باز کن.
۲. هیچ عوارضی از کشتی ها نگیر.
۳. مشکلاتت رو با عربستان حل کن.
۴. با آمریکا توافق کن.
🔴
گفتن تا اینا رو انجام ندادی این طرفا نیا. دیگه خوددانی.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/145117" target="_blank">📅 10:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145116">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
ارتش اسرائیل: در ساعات آینده حملات بزرگی به حزب الله در لبنان انجام خواهیم داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/145116" target="_blank">📅 10:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145115">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
#بمب‌اتم     این ادعا که تو کانال های تلگرامی راجع به بمب اتم میگن مزخرفه. امریکا از بمب اتم استفاده نمیکنه، مگر در شرایطی که همه کشورها با هم درگیر و وارد جنگ بشن!  تنها رییس جمهور امریکا که از بمب اتم استفاده کرد “ترومن” بود.  هیچ تحصیلات دانشگاهی نداشت!…</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/145115" target="_blank">📅 10:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145114">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f87c5dd8a3.mp4?token=kJpP7Uvr3nj-_cZ9prYqWajP0UGjhUSxx8k_-2_gBUMtnLPTwlg1mwjdFc87c1CdmSeVaEe9oWCDoU39aKEmxmd67zuh25v0NMZ_A45c0mDnzPCLMk0spOFVAElM6i6KD6crVewKOdojwenaK1sHGBIHlzFYngvNCzcowfiDnDbZJxxWsax8Gz1zOB0U0q70nbJ58bMPEdl2JdC60Q_8Ky5draPdAG9PzlZdB-QxkjliN18l1T5iteMHxvATXda8q7VTxynvxNYFvTths4vIahlbzz_yd2YXsVuLoXlmGOkk7SdDDl6FQJWl58jZDV6kATm5vdqw6wHPgEm1xNnT2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f87c5dd8a3.mp4?token=kJpP7Uvr3nj-_cZ9prYqWajP0UGjhUSxx8k_-2_gBUMtnLPTwlg1mwjdFc87c1CdmSeVaEe9oWCDoU39aKEmxmd67zuh25v0NMZ_A45c0mDnzPCLMk0spOFVAElM6i6KD6crVewKOdojwenaK1sHGBIHlzFYngvNCzcowfiDnDbZJxxWsax8Gz1zOB0U0q70nbJ58bMPEdl2JdC60Q_8Ky5draPdAG9PzlZdB-QxkjliN18l1T5iteMHxvATXda8q7VTxynvxNYFvTths4vIahlbzz_yd2YXsVuLoXlmGOkk7SdDDl6FQJWl58jZDV6kATm5vdqw6wHPgEm1xNnT2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بسننت، وزیر خزانه‌داری:
بقیه جهان می‌خواهند بیشتر شبیه ما باشند.
🔴
ما اقتصاد بزرگی داریم و در حال شتاب گرفتن و فاصله گرفتن از بقیه جهان هستیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/145114" target="_blank">📅 10:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145113">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
وزارت خارجه قطر : ما بر ضرورت توقف فوری و کامل تمامی عملیات نظامی و حملاتی که امنیت و ثبات منطقه را تهدید می‌کنند، تاکید می‌کنیم.
🔴
ما خواستار بازگشت جدی به مسیر گفتگو و مذاکره و پایبندی به توافقاتی هستیم که از طریق تلاش‌های دیپلماتیک به دست آمده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/145113" target="_blank">📅 10:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145112">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
رویترز، با استناد به داده‌های کپلر: ترافیک کشتیرانی از طریق تنگه هرمز همچنان کم‌تر از میانگین ۱۰ روزه است
🔴
دیروز چهار کشتی باری از تنگه هرمز عبور کردند که نسبت به ۱۰ کشتی روز قبل از آن کاهش یافته و کم‌تر از میانگین ۱۰ روزه ۱۳ کشتی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/145112" target="_blank">📅 10:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145111">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMKXOvAFhMycvyXDcmr2CFvQ-P545-qP5-HWIsFdy4aANSmfTXblH2m2o6IShq7YpjfDtlq6ON7993hJ-nhQXr5mM3mDwifhKHRrPwNd_oqwevSJvRfV_Tb-X60i0KgbAKon375ZClLqfB-jAELL68CNwcknHpKkC-qeLSnCHprZYhB0oxBcrQMTLx-HppjlOTHnQy5wZgGlSaNRrSirZwdFtVEuGF096W-jawDDV_BFvfNfmK6ohz7fF1XDEQEqHpMJr2ZwQWCugAJYfmCU99xooBiJlD2tr-L7_p804XiIHAbFZeO-6j4wOdV98Kof-WAm7xaBPwCn_LmLsD1JAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مناطقی که توسط سپاه پس از حمله آمریکا مورد هدف قرار گرفتند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/145111" target="_blank">📅 09:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145110">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_ctH_0w7feQl7Ifzb9A8ZdRHSLHS20UyDSLSQHYIXnG9tEc_hditjLkjnrhycRzZ-4WoLZ1496qCtzCghx8zT0ahZgwauJcu9BlfNBWXealZeKKLDs5Ygh8lxrEzSfGII5NPU1CnjR8Oqm1CazTx-kUeqbwzfT6GYxf6clB5ZeGjOgnBDmJ3uPocSDbIIc_FeYWlWrf5IK-j6ht8SiNI3Znh1sTqz4jcn3qgtioiXP6C7vBjSXIUNjijzf7wrsraqjPp-J2A0OQt0aUps0TpF8s7LTvumgo9tRN-U55Sa07BlBKf2r7g2whtIx3cIh-49APZX-HQWa9nbDcec0m6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فعالیت‌های نظامی گسترده آمریکا در نزدیکی تنگه هرمز.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/145110" target="_blank">📅 09:48 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145109">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
صادرات نفت عراق و کویت نسبت به قبل از جنگ ۳۶ درصد، قطر ۴۸ درصد و عربستان ۴۸ درصد کاهش یافته
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/145109" target="_blank">📅 09:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145108">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
آکسیوس به نقل از مقام‌های آمریکایی: روز سه‌شنبه ایالات متحده دو نفتکش متعلق به ایران را هدف قرار داد
🔴
این اقدام بخشی از سیاست جدید «نفتکش در برابر نفتکش» است که ترامپ برای بازدارندگی حملات تهران به نفتکش‌های عبوری از تنگه هرمز، تصویب کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/145108" target="_blank">📅 09:38 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145107">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
آژانس بین‌المللی انرژی اتمی مدعی وجود یک سایت هسته‌ای اعلام نشده در سوریه شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/145107" target="_blank">📅 09:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145106">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
رئیس کمیسیون امنیت ملی: یک سوپر نفتکش عربستانی با ۲ میلیون بشکه نفت در تنگه هرمز مورد هدف قرار گرفت
🔴
قفل تنگه هرمز دست نیروهای مسلح کشور است و تا آمریکا به قانون جدید ایران تمکین نکنند، تنگه بازشدنی نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/145106" target="_blank">📅 09:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145105">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1o77ecc158wO3-BXx6M0VimbmsClA8qHiWpOxu_AehTCaJO8BHQyCMPCsi-riDr1S25ykqOUrc_re72Ul4dg8JITarkfOSX8-5bokempamP8pB6bfPUfEUCLvdW6JG5Smg5CFvRb0DEodn6FEMSd7SRmYqahbtEPYTCF8DYdyzjQ2SJRTlWnK9Hpn5ab9TjZrCGB0G4z6ZK2aQ79gbZhrLdIMT2NYlUMvad94W8FICKTjeGeSYayrofO9myKd-2F23VJT2kOgA5bc8bM3_rfH1efQyMSEnxXbWbsUayNFTKvQFtEivQ3Q6bpZRW24jxE3-K2sIa_CLFN0fkobgEPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: من اصلاً دنبال این نیستم که ایران رو مجبور کنم بیاد پای میز مذاکره.
🔴
برخلاف چیزی که ABC فیک‌نیوز گفته و اصلاً برام مهم نیست که بخوان یه توافق بی‌ارزش امضا کنن یا نه.
🔴
من شرایط الانمون رو خیلی بیشتر دوست دارم تقریباً کنترل کامل تنگه هرمز دست ماست و اقتصاد ایران هم داره کاملاً فرو میپاشه. اونا فقط دارن اتفاق اجتناب‌ناپذیر رو عقب می‌ندازن.
🔴
واقعاً مردم ایران کِی می‌خوان بلند شن و بجنگن؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/145105" target="_blank">📅 09:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145104">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
تانکرترکرز گزارش داده صادرات نفت عراق و کویت نسبت به پیش از جنگ حدود ۳۶ درصد کاهش یافته است.
🔴
براساس این گزارش، افت صادرات نفت قطر و عربستان نیز هرکدام به حدود ۴۸ درصد رسیده است.
🔴
این کاهش‌ها نشان می‌دهد اختلال در مسیرهای انرژی منطقه، فقط ایران را تحت تأثیر قرار نداده و صادرات نفت سایر کشورهای خلیج فارس نیز با فشار جدی روبه‌رو شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/145104" target="_blank">📅 09:08 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145103">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
ترامپ: نمی‌خواهم ایران را به میز مذاکره بیاورم
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/145103" target="_blank">📅 09:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145102">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
عضو کمیسیون صنایع غذایی اتاق ایران:
محاصره دریایی تبعات اقتصادی و اجتماعی دارد و هرچند کالاهای اساسی کم نمی آورند، نگرانی اصلی از وضعیت انرژی است و دیگر زمان از دست دادن نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/145102" target="_blank">📅 09:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145101">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cK53G9SVEPYhC1ynUgwaN1jjWKPpLl68wnr83XLJh7qAsZzANBOPHDATtCpD9Nu-Ye10-P7ley2V5iAPCXxcNVzwBjzL-N6B4hhRnop6wBnZU8eAADU_tRJgoAfXev1g9sutG5G2w8ERMW4rfleb8O9eI4tBquyix5EHb8osGynPesDKl2vLkhceqYSwAfFJjHAZJ0HY-wFxc09jTSEfsahG_SEnDO2_2kv5N_Oq_XuNLM4AaFyPa3jBlKXkhArtLlHIKREsrybyd82ieXooabvQIgU8kMaPDJd03DljPvrwv7IHcYgjjwHo4gTNmKU5Z5ny9zRNe3OJTs7MQG26AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیش از ۲۰ مقام ارشد نظامی آمریکایی در طول دوره تصدی پیت هگست (وزیر جنگ آمریکا)، استعفا داده‌ یا اخراج شده‌اند.
🔴
یک مقام آمریکایی: "هگست تعداد بیشتری از ژنرال‌های آمریکایی را نسبت به ژنرال‌های ایرانی کنار گذاشه است"
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/145101" target="_blank">📅 08:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145100">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0559400749.mp4?token=jgce8OKx0u13GFdm-y3SVxFQDRjvmrqSbQH2wB6U_9O_kmHmEYSV4eDDr31gBq3xdjdmcwHBP1wFl8mqoatLHTZyB4LI0cZHWyflA7KP0d9P1hn-ir4QEOI1Ff19TfAt3LBNXS0rrlTf3JW-k6aWpasli1QPeqvGXJAuSLPDL7WoQ4878wNA_e3HsFm0pZJrGPCnm0vNN9r_kZdJfYYro1jy01xByVrPyhzSuFDI2bf0LI2t-4si9mUSVBQJc-Iw7sGaaLssdvqcK5JSgllteiY2vV-_SK2p_QMoG30jfq8VxMj6IXUBK-0uidKTfrUfGmU2OoQSdxmsEbml1SAZ4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0559400749.mp4?token=jgce8OKx0u13GFdm-y3SVxFQDRjvmrqSbQH2wB6U_9O_kmHmEYSV4eDDr31gBq3xdjdmcwHBP1wFl8mqoatLHTZyB4LI0cZHWyflA7KP0d9P1hn-ir4QEOI1Ff19TfAt3LBNXS0rrlTf3JW-k6aWpasli1QPeqvGXJAuSLPDL7WoQ4878wNA_e3HsFm0pZJrGPCnm0vNN9r_kZdJfYYro1jy01xByVrPyhzSuFDI2bf0LI2t-4si9mUSVBQJc-Iw7sGaaLssdvqcK5JSgllteiY2vV-_SK2p_QMoG30jfq8VxMj6IXUBK-0uidKTfrUfGmU2OoQSdxmsEbml1SAZ4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله اسرائیل به شهرک المنصوری در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/145100" target="_blank">📅 08:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145099">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
آکسیوس: ترامپ دستور حمله به نفتکش‌های ایرانی را صادر کرده است
🔴
آکسیوس به نقل از مقام‌های آمریکایی مدعی شد ارتش آمریکا روز سه‌شنبه دو نفتکش ایرانی را در نزدیکی سواحل ایران هدف قرار داده است؛ نفتکش‌هایی که به گفته این رسانه، در شمال خط محاصره دریایی آمریکا لنگر انداخته بودند.
🔴
براساس این گزارش، پهپادهای آمریکایی با موشک موتورخانه این دو نفتکش را هدف قرار داده‌اند و این نخستین بار است که واشنگتن در اقدامی تلافی‌جویانه، نفتکش‌های ایرانی را مستقیماً هدف قرار می‌دهد.
🔴
یک مقام آمریکایی این رویکرد را بخشی از سیاست جدید دولت ترامپ با عنوان «نفتکش در برابر نفتکش» توصیف کرده؛ سیاستی که هدف آن افزایش فشار و بازدارندگی در برابر حملات به کشتی‌های عبوری از تنگه هرمز عنوان شده است.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/145099" target="_blank">📅 08:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145098">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TT08lOgr9fOF9lEw2ajxbht0ESjQDySe8FgKkhFpTlw5QoWIYyXQYB-E5ujXPPNqcHlyy1-SDP8g2MY-HcTHhu3nw-bd1MR_QIArh_eCUSUZAnqVX1pOTRquLoU6XWsCbxOVhb2gBvP5sBJXtlxyarSHsMaVA-S-nj0RQc-2OLMNIxoE9zV94uBMKz4CoNxRJTYPcUsoRAMpzMw10EDBx7KYYB_KCNQCWag3qXsfxaU5tcmYEjZo-HP2gZH4-XodbJFozwv1KW4XKGpX4tElOCQHn1NH59_58W4BmhNJNoFTvqATFg1bPT_NaIoBWpSNs4kGr_cWiRrFUtcbEDWA3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / الجزیره: ارتش اسرائیل اعلام کرد در پی ورود احتمالی چند پهپاد به منطقه ی«کفار یوفال»، آژیرهای خطر به صدا درآمدند و تحقیقات درخصوص جزئیات این حادثه درحال انجام است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/145098" target="_blank">📅 08:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145097">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JuTsWyu6ax2W4HmHtvSFbaMUrXkGKIUDxvKJmP415X-7JBvcHZj6MZY_PWbzu5rkDJ_XoSvw9nJw4MrBPpYek8JaabMHEnaF7m3GN98K1YhKce_3arh3D5yVpj-VkxoRvs318GIIs28vIZGyWh7e6roVLVUNQggfzLo_ohemXITMyzfoSzEROomQ_Pu9sjCYU1T5VU8izDTqeWYvMBOtIYByYxFtWKtcK7kEmjsW0Eiap8tn1v_6AizAk-FF8E7-CTeHnaryw7GGJVA1Kw3bfPJRZ7vO3XUyL7Q3JOzH0_78SPIb39fc2sAEzz4xK9QCvTI4LNXw51i_183feYXQYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت آسمان ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/145097" target="_blank">📅 08:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145096">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sj-Zmm57zOFpqGu2cKx1lVRHqrIb5AEudW1j0Miy-crkupc58DSwpiZuV_wKoTkE0yOZacI6SAlE2-YL0s5dIgAn0wUB3kOGjBMVYIUtBfGQfUCwdPV-2VMeT9Ou72wFKXvXLkoequXshO5IXxe6uJzrvGAsLUKGOn-E9N2LvYjvvOjGVUt2zs0A6v83uAeNZ4t5jMLsIPui_8kr-iPK1YRBUBJ_yvmZPoazCUx3wL4MqPgFj8UR63ZUuPW22q7AoL_e5mh8J52NGoKmw0tNMbXXBxdJt6-Zp6JsbkeMVdfjFXg5cavrr2lbHc8ghJGQ4DJXZWSk7POwc7wdUWxtTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
قیمت نفت برنت ساعتی قبل از ۹۶ دلار هم عبور کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/145096" target="_blank">📅 08:38 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145095">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
فرانسه رئیس دوره‌ای شورای امنیت سازمان ملل: موضوع هسته‌ای ایران و تعهداتش محور اصلی بحث‌ها درباره ایران در این ماه خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/145095" target="_blank">📅 08:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145094">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_-Z8NmD9iZyF1z-4jjEXhA4mWrSpAFmUj9sUXuTxvV2_1h-xEZXzT3C_lhoVcsw2OYNxUxoMKcE8lrWB4NG7nuqToCGnQTFA9iyIWXGpZpwBOWgaPgsJrcC6-RDLeAxRzmAYW9S2Ua7WuGcDLGsimFP4nDC8JSP2uu9PkfB-o0be5EYzXWB2kj4EdskZei6ah-fRh9ywxSGbQoKg8xEhtSqCo9cma7txGJWcJEcY-sE6O9MJcTfxW_yAuRaR7WndLSndVhTdddJJkQ7HXXOd755toczgK87DfwwEL32vG9xoh8EafN5tUXCGg9FPv66Xt1ueSKhkIb4xkF4h3tqmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اوضاع اقتصادی به قدری خرابه که جانبازان شیمیایی هم مجبور به مسافرکشی شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/alonews/145094" target="_blank">📅 07:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145093">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a69ee6e2c8.mp4?token=CBeAocYblVG0EJV5YMH86FVpqy19MD9hotekPSsIzN0Xybw4CRy-MR49d1wgZkNpZYnQzNGS46L-IdNYPNuHb3Btx-oHjqPUp9RPiiLg6Gxu3wNjWYTVRzW_2xJr-zT8qiCu7aufJlh0lZd-XOIZ61ws0mfho-GHCTflzHIGS32k96kdkHnroIS-mleDWZIg3XqKjUEJqSGoWpOI1L1tAzFLb56mTPMvbIFpHVFwmRoQRbPN3SYmOAZyMNV6_JjBc2A8apTJmr_vzApmxCsiLta5sYZ6H5QEtsDHOZUIVDw7zbZrQn2v-65Dilid9M-ZbN53KVya8AqtoIYfg4drC2FCY0Ba-JYjSEXXCdbFGCkvrLExTQImMu0pcgRSGyOzDZxMtytLn8_RXfuhVnEe9wE9zVPUi5mbqXfcURd2i89ClwftWg1b80vQyZH7lz6LpAKO8wca7ty45JxcLD9w6IqlS_L1bmF0Q860tGsA1EhYJqPTKKT54FycIcnph6oQA9iPBAGGmPKhZJ1RneL9SeJ-834yvQlPsugD7rqWqcFcdHUUHltPHnJbyU1Igj9zQUMxfzYMMzaDjIO65ZMdSz_WRNa-gBQRS7F4PbDLkDY267TQutGx3AqyrKRPMfD8R43RBQFWOKqnhxWAOTv7pLdvtJu2EOQ9-aTlCLbcvJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a69ee6e2c8.mp4?token=CBeAocYblVG0EJV5YMH86FVpqy19MD9hotekPSsIzN0Xybw4CRy-MR49d1wgZkNpZYnQzNGS46L-IdNYPNuHb3Btx-oHjqPUp9RPiiLg6Gxu3wNjWYTVRzW_2xJr-zT8qiCu7aufJlh0lZd-XOIZ61ws0mfho-GHCTflzHIGS32k96kdkHnroIS-mleDWZIg3XqKjUEJqSGoWpOI1L1tAzFLb56mTPMvbIFpHVFwmRoQRbPN3SYmOAZyMNV6_JjBc2A8apTJmr_vzApmxCsiLta5sYZ6H5QEtsDHOZUIVDw7zbZrQn2v-65Dilid9M-ZbN53KVya8AqtoIYfg4drC2FCY0Ba-JYjSEXXCdbFGCkvrLExTQImMu0pcgRSGyOzDZxMtytLn8_RXfuhVnEe9wE9zVPUi5mbqXfcURd2i89ClwftWg1b80vQyZH7lz6LpAKO8wca7ty45JxcLD9w6IqlS_L1bmF0Q860tGsA1EhYJqPTKKT54FycIcnph6oQA9iPBAGGmPKhZJ1RneL9SeJ-834yvQlPsugD7rqWqcFcdHUUHltPHnJbyU1Igj9zQUMxfzYMMzaDjIO65ZMdSz_WRNa-gBQRS7F4PbDLkDY267TQutGx3AqyrKRPMfD8R43RBQFWOKqnhxWAOTv7pLdvtJu2EOQ9-aTlCLbcvJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سپاه پاسداران تصاویری از حملات موشکی به اهداف آمریکایی در اردن را منتشر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/alonews/145093" target="_blank">📅 07:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145092">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMe_Ugg6l4p7Sax-kGLkbs-bICpx_uz9XupVuMJGoSp0DNljNsvmbW34WNNq0tkgW9bGA1YAJUOsFbHIoEQp8DCISGT7cdNBuw9eUibcdPVdtIsTLpbqWduN8CPQUiF_1AV7CftDoYtKZ4lmnDIpVdSYIMuvvBQz9pYx_w3ptwr5mEliB_2QuFhHWCnEDXTVOSwPjtvfsGJ6Jee_l6AMEag8E5VneZa7d2J_ehxjLESVwVpK2tCI6i0jw-b-4rKVnyYuPkzBblqc5IZKl4Txt6PJKe1L20CP6tVertB0TQRPGsfxcVz4mooeqKIGP_RCDEWr5sBB8hcRpYMZanW0sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
دریافت مدرک رسمی «دیپلم تا دکتری» فقط در ۱۰ روز!
✅
قانونی، قابل استعلام، کاملاً غیرحضوری
✅
مناسب مهاجرت، استخدام، ارتقاء شغلی و ادامه تحصیل
✅
ترجمه رسمی و تأیید توسط تمامی نهادها
☎️
مشاوره تخصصی و رایگان
:
https://t.me/irantahsilat_chat
📺
عضویت در کانال
:
https://t.me/+1I9Ex4YFtcZkOTY0
https://t.me/+1I9Ex4YFtcZkOTY0</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/alonews/145092" target="_blank">📅 02:08 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145091">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
فرماندهی مرکزی آمریکا: موج حملات علیه اهداف نظامی ایران را با موفقیت به پایان رساندیم‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/145091" target="_blank">📅 02:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145090">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24346d9299.mp4?token=qqsJ92C033bnam3UcojGCx_8tp0aNe4jvf0HjOKH6zmhQ49kzpDQ2MqVRcWQyO00p1zgaw1O9IIE-NcYmzmrVIAv3tA2MFp0q5WB3D8TCePY8l6-2yLvw5JJZ1OrJcVPtnJLndSberAgp8hOmhSCgIeIafh1_hyw24Yexmh57hkReQj3uT_M71XIDn4i8B0GfE2Cb1fC6Eaor_SEWo9KA8vBA_r2kJlkzXWdV7aU2vbFBVpuZheRljId7nxfAX7eXsvihv2S82DxFzMdgp-MCp9adK-UkWZxG4FJl4st8xumyWp1BH4E2tfTQAdd1mYXJwSqzONduCTKooHsRoP7Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24346d9299.mp4?token=qqsJ92C033bnam3UcojGCx_8tp0aNe4jvf0HjOKH6zmhQ49kzpDQ2MqVRcWQyO00p1zgaw1O9IIE-NcYmzmrVIAv3tA2MFp0q5WB3D8TCePY8l6-2yLvw5JJZ1OrJcVPtnJLndSberAgp8hOmhSCgIeIafh1_hyw24Yexmh57hkReQj3uT_M71XIDn4i8B0GfE2Cb1fC6Eaor_SEWo9KA8vBA_r2kJlkzXWdV7aU2vbFBVpuZheRljId7nxfAX7eXsvihv2S82DxFzMdgp-MCp9adK-UkWZxG4FJl4st8xumyWp1BH4E2tfTQAdd1mYXJwSqzONduCTKooHsRoP7Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسکات بسنت:
یا سپاه پاسداران علیه یکدیگر برخواهند خاست، یا مردم علیه آن‌ها برخواهند خاست، یا به میز مذاکره خواهند آمد و خواهان توافق‌نامه‌ای خواهند بود که بتوانند به آن پایبند بمانند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/alonews/145090" target="_blank">📅 01:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145089">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1d43669ea.mp4?token=fa3qeNOKRdVycbDdB7G0AAB7dkMZBoX1ei-JGZYHHkVBJut1NupUlRZW3Fx9rmGsC4MvtM4rs7ANJ3K4AIINIxz6KbTDLDb3PNMpA_1mkI_-CENcz5lluBCsaTEg4vBf2NHSXSR1tsx-thny3nOmOHZxZFV-ATY4AcUKyALWTakif9DizbbDeQW1IjV0UcQZ__KbIGfSHlYCl2BWbMIrbOXE0ajp9titLoK-bj_PR5u91b8jWME06i417FHh-lyPZkFKi-SCzsL400002DJ3ME8qRmqpVYeSqAs6OvAwMGr3Kw4y4tF_rsr99KtoiTV6-YNPVlcPLWrmwNcHGQ04FFrI2E7xCLOw8iKuABQnyjlEt5wMLs6A9RDaEAFUYuX5Aw3n5-ECn3-XV3mCEn9-EEMMfYhL7WApCVKh1Gqerw-69vJ6wJLOLbCr1Z3-OEj62rFvilRmniU3fKRnfZPQ2jZ_RmaAMR8egdJY1KB3TLEZYFN3G0O3Sraon3pGLOgEJXJjrx3eiGiDCKMXJ2oT_5lODX1vnovSVwWyPjguXAuzWxbZ-hY1G0Kwl39M03YbdObZMHIn6kdq_s4KtK6gotYFJBmZQq3wJwQVvnbd91vQQDFt9sD0PqGhSbuvoDW_qIcpeT1uDAwuPzUE0ErAr796pomz7hyTV9CE3bRZ3gM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1d43669ea.mp4?token=fa3qeNOKRdVycbDdB7G0AAB7dkMZBoX1ei-JGZYHHkVBJut1NupUlRZW3Fx9rmGsC4MvtM4rs7ANJ3K4AIINIxz6KbTDLDb3PNMpA_1mkI_-CENcz5lluBCsaTEg4vBf2NHSXSR1tsx-thny3nOmOHZxZFV-ATY4AcUKyALWTakif9DizbbDeQW1IjV0UcQZ__KbIGfSHlYCl2BWbMIrbOXE0ajp9titLoK-bj_PR5u91b8jWME06i417FHh-lyPZkFKi-SCzsL400002DJ3ME8qRmqpVYeSqAs6OvAwMGr3Kw4y4tF_rsr99KtoiTV6-YNPVlcPLWrmwNcHGQ04FFrI2E7xCLOw8iKuABQnyjlEt5wMLs6A9RDaEAFUYuX5Aw3n5-ECn3-XV3mCEn9-EEMMfYhL7WApCVKh1Gqerw-69vJ6wJLOLbCr1Z3-OEj62rFvilRmniU3fKRnfZPQ2jZ_RmaAMR8egdJY1KB3TLEZYFN3G0O3Sraon3pGLOgEJXJjrx3eiGiDCKMXJ2oT_5lODX1vnovSVwWyPjguXAuzWxbZ-hY1G0Kwl39M03YbdObZMHIn6kdq_s4KtK6gotYFJBmZQq3wJwQVvnbd91vQQDFt9sD0PqGhSbuvoDW_qIcpeT1uDAwuPzUE0ErAr796pomz7hyTV9CE3bRZ3gM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسکات بسنت:
یکی از بهترین متحدان ایران، رسانه‌ها هستند.
رسانه‌ها بلافاصله تمام دروغ‌هایی که ایران می‌گوید را منتشر می‌کنند.
هیچ مینی در تنگه وجود ندارد. دو کشتی به مین نخوردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 99.7K · <a href="https://t.me/alonews/145089" target="_blank">📅 01:56 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145088">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70bc81282a.mp4?token=GHTpEBvqPhMjY75kFdX5LSoIrQsysAJ-11sf4ciMVqzw4wupRqQo8JrzTU-jI0kEfwkuvnv8iOcmQ1YclwgoNIaZL9eA3xVvu_r_OTJOB3R2Z360SuO0TfQOy2SyS2yExzXZxduRvOXY-FbHExynBHC2rjtsoUeODxL_8PT7eUckNSgiz_r1RX9FpdrFVkxYUraZMkwrkH5gORvomxvEwhFop5iB_jSOlkJrMyC4_GbipEcuKD_VidxAP1gWN_zjfYcYUEgHCxXe-FENsGw9Z197CufW7vLRAY5hdy5h_mo1OfI_cIp3nOEJSF4gW-NTv5kPolc-VFbTWNPC6dM1ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70bc81282a.mp4?token=GHTpEBvqPhMjY75kFdX5LSoIrQsysAJ-11sf4ciMVqzw4wupRqQo8JrzTU-jI0kEfwkuvnv8iOcmQ1YclwgoNIaZL9eA3xVvu_r_OTJOB3R2Z360SuO0TfQOy2SyS2yExzXZxduRvOXY-FbHExynBHC2rjtsoUeODxL_8PT7eUckNSgiz_r1RX9FpdrFVkxYUraZMkwrkH5gORvomxvEwhFop5iB_jSOlkJrMyC4_GbipEcuKD_VidxAP1gWN_zjfYcYUEgHCxXe-FENsGw9Z197CufW7vLRAY5hdy5h_mo1OfI_cIp3nOEJSF4gW-NTv5kPolc-VFbTWNPC6dM1ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسکات بِسنت:
فکر می‌کنم دیروز حدود ۱۷ میلیون بشکه نفت خام را خارج کردیم.
این کنترل تهران بر تنگه نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/alonews/145088" target="_blank">📅 01:56 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145087">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/114145c9fd.mp4?token=UX3NwZywpsQrQU4Vpvxu-1iI4IsHnhCxdDUaqnc_h5EHIwDYstDUkiA_zWWFVy7F5uRhgK37apnJAN3m6Iuog0xi6xoNpmPU5mg-lPoeRCtq3hZXe4V7w4eXlLiszDy8SnJ7bSm3caczSP0T92ggJS0a-IwXeYev2ri-87Ccao-0ZNIP-nqI9deMeEId80C1ubTS_XCYpci1dWDKV9AxG56b33agV2rcAAjAxseqsQSys2braFII-YB5iWjPNy_T_6SH7KDySoFgDmegco08qAS60J-QdXegzHzOzHUIBJIf2siWJX5yNhHrCWS3bU7vgrNDmnJwGl4yebejpf6E0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/114145c9fd.mp4?token=UX3NwZywpsQrQU4Vpvxu-1iI4IsHnhCxdDUaqnc_h5EHIwDYstDUkiA_zWWFVy7F5uRhgK37apnJAN3m6Iuog0xi6xoNpmPU5mg-lPoeRCtq3hZXe4V7w4eXlLiszDy8SnJ7bSm3caczSP0T92ggJS0a-IwXeYev2ri-87Ccao-0ZNIP-nqI9deMeEId80C1ubTS_XCYpci1dWDKV9AxG56b33agV2rcAAjAxseqsQSys2braFII-YB5iWjPNy_T_6SH7KDySoFgDmegco08qAS60J-QdXegzHzOzHUIBJIf2siWJX5yNhHrCWS3bU7vgrNDmnJwGl4yebejpf6E0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر
: تهران تهدید به حملات تازه به پایگاه‌های نظامی ایالات متحده می‌کند.
🔴
اسکات بِسنت:
آن‌ها تهدید نمی‌کنند، آن‌ها در حال انجام آن هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/alonews/145087" target="_blank">📅 01:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145086">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
گزارشگر
: آیا می‌توانید تهران را به میز مذاکره بیاورید، در حالی که چین همچنان از آن‌ها حمایت مالی می‌کند؟
🔴
اسکات بسنت:
فکر می‌کنم چارچوب‌بندی شما در اینجا نادرست است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/alonews/145086" target="_blank">📅 01:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145085">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
ارتش کویت: درحال مقابله با حملات پهپادی از جانب ایران هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/alonews/145085" target="_blank">📅 01:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145084">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
انفجار در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 99.3K · <a href="https://t.me/alonews/145084" target="_blank">📅 01:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145083">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c60b2185fb.mp4?token=J1_Up-E1YCR5ENg6qqruGAf7yz8pIckCUEKDLymW72UB8PH1Btn2wi7EMWwmPUnZkyFp-4vVR5X9_pwHSocPsMiz-9RMwE6q0Ft68umPbhuOb-r6_8XS8c5CwKyezdoWx4JNWNnhEegV6C4tUGeGegjy_Ybn8N-Ibr0198dw8eO37mBvKHfkeD7C0pMdjvYI048hIsg7V5duesumwAe9LPp8tg_sgdxxZN_ZaHTmq78s3nVUNvn2DbJIG3ntvGXLkm1YaXjaMzf6YXe7Yhcc886_H5lXaJuX8l0lbaC70gv-dxip0X3H44x0XFqCN2aUz0iiHrlAFf8s9XhaIPxmbw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c60b2185fb.mp4?token=J1_Up-E1YCR5ENg6qqruGAf7yz8pIckCUEKDLymW72UB8PH1Btn2wi7EMWwmPUnZkyFp-4vVR5X9_pwHSocPsMiz-9RMwE6q0Ft68umPbhuOb-r6_8XS8c5CwKyezdoWx4JNWNnhEegV6C4tUGeGegjy_Ybn8N-Ibr0198dw8eO37mBvKHfkeD7C0pMdjvYI048hIsg7V5duesumwAe9LPp8tg_sgdxxZN_ZaHTmq78s3nVUNvn2DbJIG3ntvGXLkm1YaXjaMzf6YXe7Yhcc886_H5lXaJuX8l0lbaC70gv-dxip0X3H44x0XFqCN2aUz0iiHrlAFf8s9XhaIPxmbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شبکه خبر خراسان رضوی دربارهٔ زیر گرفتن تجمع کنندگان پرچمی
:
🔴
تصادف بوده، عمدی نبوده، راننده حالت عادی نداشته‌.
پلیس راهور: یک دستگاه هیوندای با سرعت بالا با یک دستگاه چانگان در مسیر موازی برخورد کرده که در پی این برخورد تعادل خودرو بر هم خورده و با جمعیتی که در حمایت از نظام و نیروهای مسلح در حاشیه خیابان حضور داشتند، برخورد می‌کند
راننده حالت عادی نداشته و پس از برخورد با بشکه‌ها و علائم ترافیکی، با جمعیت برخورد می‌کند و در نتیجه این حادثه تعدادی از شهروندان فوت می‌کنند و برخی نیز مصدوم می شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/alonews/145083" target="_blank">📅 01:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145082">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‏
👈
دادستانی مشهد: راننده مست حادثه پس از برخورد بازداشت شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/alonews/145082" target="_blank">📅 01:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145081">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
‏یک مقام آمریکایی به الجزیره گفت: حملات به سایت‌های داخل ایران هنوز ادامه دارد و ما پایان آنها را به محض تکمیل اعلام خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/alonews/145081" target="_blank">📅 01:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145080">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djp_XbmM0NLx6KBVoXnxRD__eDo6hDTXuL_uiSFVKTZz1UF4PNkHnLOobmfEIaBGNmQ47rPmZlltvooZi-BeUx05BLsRSQzH5GA4_vO9ybuldyR9s_WlSi5v7LqXlp8Y5bcgGmyl-rhunYk8019ikDXMdKrRjpGIxh6ZLNXsRALGD-Lh1otYlV9XUitZvGA50f_2vPIm3bNYqg_Z3zzcCAo01R5Yz0wKTk1JfCegp0M9hogw0owBlRHx5XCG-ABr_Lslvf2xh_ReEbyt2zBfaaPRBTqMe6n8j2IJ-ZDL7rwORAM5g4n3UIt1wGdES3Sv69npaxORnk90wm03wemFjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اولین تصویر از راننده‌های که با خودرو به تجمع پرچمی‌ها در مشهد حمله کرد
🔴
مشاهده فوری</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/alonews/145080" target="_blank">📅 00:59 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145078">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
نیروهای مسلح اردن:
🔴
سامانه‌های پدافند هوایی ۱۳ موشک بالستیک را که وارد حریم هوایی این کشور شده بودند، دفع کردند.
🔴
۱۰ موشک رهگیری و منهدم شد، ۳ موشک در مناطقی دور از مراکز مسکونی سقوط کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/alonews/145078" target="_blank">📅 00:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145077">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
یه قانونی هست، وقتی هیچ جوره دفاع نمیتونی کنی بیجا میکنی دشمن تراشی میکنی و همش دنبال جنجالی
✅
@AloNews</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/alonews/145077" target="_blank">📅 00:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145076">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
یه قانونی هست، وقتی هیچ جوره دفاع نمیتونی کنی بیجا میکنی دشمن تراشی میکنی و همش دنبال جنجالی
✅
@AloNews</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/alonews/145076" target="_blank">📅 00:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145074">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
فوری/شلیک موشک از اصفهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/alonews/145074" target="_blank">📅 00:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145073">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FLRTAPL6r_RqMxSacrrb8A9zUfdFSRe4ykanRXo00OAGB5hBjbvHqhnphOXJIBiafS1lziil4mjy3Jx5FcN-AGNF2kIF4KtrUCVovVxdnMXtVUkxViAds0ruWc9kdl3eUgxTaf2tqOMZAnQJeO4Tp6Wj7RPVwXLu3pyaGIhOOErtD4RWDRj0lr73y-VRG81OgFgC1eFeeXRqfjYDTcwB3zYAVrsy9kfDNmhPjPTgT2rMZbUvwAzaQDWB1aZVTIohMVl3FdklspBOhAUFBQt5TTLUXvF_O0n-wSaGaKNHMTQ35jRF-HgkUWUbrkiD6U1gIq08AI9fZ1BBo06cgrPeyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
متاسفانه در حمله ساعاتی قبل آمریکا به سیریک، یک کودک جان باخت
✅
@AloNews</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/alonews/145073" target="_blank">📅 00:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145072">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
هشدار دلار   تارگت دلار رو چندبار تو این موج مشخص کردم!!!  الان دیگه چون سریع تر داره به اعداد میرسه به شدت پر ریسک تر شده یعنی حباب گرفته دلار هم!  یعنی یه خبر مثبت بیاد (که احتمالاً) میاد همتی نوسان رو گرفته رفته.   این هشدار رو جدی بگیرید!!!   @mahaneconomy</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/alonews/145072" target="_blank">📅 00:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145071">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
تعداد زخمی‌ها در مشهد به 25نفر رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/alonews/145071" target="_blank">📅 00:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145070">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
فوری/پروازهای نجف به ایران کنسل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/alonews/145070" target="_blank">📅 00:17 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145069">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
بیانیه سپاه پاسداران در خصوص حملات امشب:
در پی حمله سنگین موشک های بالستیک به پادگان تفنگداران آمریکایی در اردن موسوم به کمپ تیتین، واقع در سواحل خلیج عقبه، تعداد زیادی از نیروهای آمریکایی را به درک واصل کرده و چند تاسیسات مهم و بالگردهای هجومی دشمن منهدم شدند.
🔴
عملیات انتقامی نیروهای اسلام ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/alonews/145069" target="_blank">📅 00:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145067">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CyrLrAcZ0-uPxNyBrSjwGH2AiQE6Nzs-UCvjMyjyMp75cmPgNpuus6vbng0Q7L8QyjQFK-0sw2WRSndkkZ8Nk2l7KxhuzizJUoKqW58HaycaOnRp7KXWGBX4xmRkg_6aqmyWCANFQaPs0wUx2cz6CkkVqI57I_gLfWe5MQDtSZ1pRXD3NqGe3Kzwgsy3RXiD1ZGOb-icwVFDGnpbOaa6ekZw3GnpcTKVrgAgmlhHxWslESkenM2E9u1awBhZGGKQ7k28Zgek7ZvvO6TgqqlzhPfiw4sTq6DFSQp7JTSwYQSoIsyexndte8zwcY-4Qp5OMhUc_8LCf9K7viT-8kRCsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tpY0BrBQK5nLVausumGAOb35tR_LO5ul0N_8b644TaPe8I7srrG8RWfqXj-LOedq_47-H9HFzUWiqAZD3FV14JKZi4K2vEuylX0WpqRf22GftPUTLVE7GAJsMN-W9AHcpUJt2J8TNXknV47Shr7XU0ZA-gHaSoYdRnSG9Dc5NtB4oQyDB0jCcMCrc90ryGPlsi6m8_K4B48ntaJwUBevs2SRFt8e9Kfgyv2kL00Nubl9APclKp4A80q9Q1KML4lpfBS47YE8YSm-0HjxFO_U91N5jIPi8MPjBnQWAEEH5YdC_ahe-HcZReVfEqpG5U1sVm-iDkwfghunUnnc29hYeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
گویا حمله به تجمع شبانه مشهد دقیقا در همان مکانی بود که جاویدنام حمید مهدوی جان باخته بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/alonews/145067" target="_blank">📅 00:08 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145066">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sWj7vpR8kcJDmvhxkG3hWu1ofMlr_ZcWfMbWOnuejEF7o2JN33q9g8DaG3uE6FLCejSxX_6MV4V3HJRWXnuyAUZrzDp5MNNtS5FROAQISIrLpsZCU3RUJuR8-1OVBVQUm8YQMuQNNOqun6QnM16LOJDWJ8LRhmtNsSkkVMfjZBjnygb9sK0-YSe2OMXLfiBvybIdqYY6hx45Rx82skVhQypQr55bZHKvBLqeV5lTS5GqnGGqzB0dYcxAImZtxKBSztux6EA8g_P08nne-VJCPVkCwGLAVXuoGVpyU_5DEHsGDQw4-DEu7EWvVTuc3FeNB-DojRu7gPFDArdwS2BIWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زیرگیری بسیجی‌ها اینبار در شیراز
‼️
🔴
یک خودروی ناشناس در شهرک گلستان شیراز، زنانی در خیابان تجمعات شبانه کرده بودند، زیر گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/alonews/145066" target="_blank">📅 00:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145065">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاکوپینگ | EcoPing</strong></div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/145065" target="_blank">📅 00:01 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
