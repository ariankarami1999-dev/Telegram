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
<img src="https://cdn4.telesco.pe/file/QPDqdNK6_B69JK0GFe_xMSOaPkXXAY7bO3yekoNQsveZ8qva10AXwF6bBGa6SoxzX-ucHu6nFI83hnwYHea8PbR58iPyWQBFGF6RJ9NyxegVHZGLOwLWriwGR3NT18DNOgbd3V_T8_yGDIcE1AyJn3e_romHYbetIKa107iL5gwYEpz5yCD2q6TxXXaPu9QNKdCp0AxEsgx8lKdLuzfwEAmXsR2n-wtOyGXiKQy1KmVeMN9p7Kmv4GOvYMgh3MHwr_3TQmumq0DwRAC4aQcUfobuCy6RoAPM9VQUcDt9eHmpUPaunnAv-l1BC2EgHxLfMT1zNwbqsuTfpCQpJX0wqQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-20 01:40:53</div>
<hr>

<div class="tg-post" id="msg-467852">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/300a10123e.mp4?token=Ky3NFoLZub8gaL9Az6BCslKcAL_KW9wj4WljFi4ttMvSwGnYWZ-GExCvWM9rsXvGAHR7INyZWU2w3TEihUwv2rpnekYuMt3gMx4oC0P8I_YTCvSNzACGTjlXIOM9tQjrsB5R_jzJCTprFylLjBLEQCSz3cFNidcGq5uNKiaSXDFDMhvqqDT0H6_euDq_dHEc9X3_vFiJT5JpoGCvJvFfXCu58fIJQPtSJG79b9UhnVNcG1F6ZX50YKxXZZJzXJxb8_ZaEZFHI-wzhmZX6GXGyrkJsl7-Oa7tGmWgCSXFlWSWlPFY__KmRVk2-m3j7tOZoWiSQVx0ZwSo8MW5qWGE-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/300a10123e.mp4?token=Ky3NFoLZub8gaL9Az6BCslKcAL_KW9wj4WljFi4ttMvSwGnYWZ-GExCvWM9rsXvGAHR7INyZWU2w3TEihUwv2rpnekYuMt3gMx4oC0P8I_YTCvSNzACGTjlXIOM9tQjrsB5R_jzJCTprFylLjBLEQCSz3cFNidcGq5uNKiaSXDFDMhvqqDT0H6_euDq_dHEc9X3_vFiJT5JpoGCvJvFfXCu58fIJQPtSJG79b9UhnVNcG1F6ZX50YKxXZZJzXJxb8_ZaEZFHI-wzhmZX6GXGyrkJsl7-Oa7tGmWgCSXFlWSWlPFY__KmRVk2-m3j7tOZoWiSQVx0ZwSo8MW5qWGE-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خیال‌بافی بن‌گویر: کل غزه متعلق به ماست
🔹
وزیر امنیت داخلی رژیم صهیونیستی بار دیگر از رویابافی‌های خود سخن گفت و مدعی شد تمام نوار غزه متعلق به اسرائیل است.
🔹
او گفت: من رؤیای تصرف، یا بهتر بگویم، آزادسازی کل نوار غزه را دارم. رؤیای بازگشت به تمام غزه را در سر دارم، زیرا همهٔ آن متعلق به ماست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/farsna/467852" target="_blank">📅 01:20 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467851">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f5e0e3e33.mp4?token=UmOsLJtosCypXWVJMoBUMYL3m5c-0IFlPQU3Bo-YOvXxuvt9JSC7kVKuXboUUL6iBuV9npJZHD7HKlHrKRyHLguUFJPPdBy4jjkERY8jYPAUrVY7zoLjwAsAGPLkWnqBNlu3qi3orUKziGk3Gbis-w2VaMFXdmwk-YdjEsXpndBA_dBhLsM8W7S-tm5LjcniXdnhH9XcDGMOP-3Qfya2tia6kWJ6dNuLGRuuRHgmRfJea0v_eJwErlqWccE6IP_sajMtFtRS8zBJcliAln_Avus2tAtVZ_PzdOfYgo0lqYlhA2yHyrURXkLV1xrLzwpp6KeCYDP2lZn7jbq8w1e9bxsavi9SvVp78sXxqQJgeRTs7dUq22jDitqzqfCmY_C2iT3GzdYaonM1VtZuEua1X6bGyiZ9epZFhS62HuWBMbWMRuZmK2IjKRqwvC9Qrs_MEhzZ9aPJZXQgZMqaFG0pfLns6mmQID6n_M1sgqe15vOUXBvZ-sIOOlctamP68_cCPSyMzgTaoJWY-hIR94mfl9lWJDAHdPwDPrXUSQ9e_wn7tG0krzBuF2jRzMuF5OrO82EWUI0x7Ss4IzZw3_zi5Q-9vr8exv9a2_nABQxgF_B1NYcm0FzA6jsPSppSYW-sqXdfgCmfvfnMLcQRbsE8spLRCczqHbkN6F5UFcmAEpY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f5e0e3e33.mp4?token=UmOsLJtosCypXWVJMoBUMYL3m5c-0IFlPQU3Bo-YOvXxuvt9JSC7kVKuXboUUL6iBuV9npJZHD7HKlHrKRyHLguUFJPPdBy4jjkERY8jYPAUrVY7zoLjwAsAGPLkWnqBNlu3qi3orUKziGk3Gbis-w2VaMFXdmwk-YdjEsXpndBA_dBhLsM8W7S-tm5LjcniXdnhH9XcDGMOP-3Qfya2tia6kWJ6dNuLGRuuRHgmRfJea0v_eJwErlqWccE6IP_sajMtFtRS8zBJcliAln_Avus2tAtVZ_PzdOfYgo0lqYlhA2yHyrURXkLV1xrLzwpp6KeCYDP2lZn7jbq8w1e9bxsavi9SvVp78sXxqQJgeRTs7dUq22jDitqzqfCmY_C2iT3GzdYaonM1VtZuEua1X6bGyiZ9epZFhS62HuWBMbWMRuZmK2IjKRqwvC9Qrs_MEhzZ9aPJZXQgZMqaFG0pfLns6mmQID6n_M1sgqe15vOUXBvZ-sIOOlctamP68_cCPSyMzgTaoJWY-hIR94mfl9lWJDAHdPwDPrXUSQ9e_wn7tG0krzBuF2jRzMuF5OrO82EWUI0x7Ss4IzZw3_zi5Q-9vr8exv9a2_nABQxgF_B1NYcm0FzA6jsPSppSYW-sqXdfgCmfvfnMLcQRbsE8spLRCczqHbkN6F5UFcmAEpY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انیمیشن لگویی جدید، با مداحی انگلیسی محمود کریمی
🔸
این نبرد بین خیر و شر، هزاران سال است که ادامه دارد؛ نیاکان ما راه را به ما نشان داده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/farsna/467851" target="_blank">📅 01:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467850">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJ176w1yyErSFzaZa53I6ZAguCR44hS0rzjOLrVWNYZniJD0szpdiD3rdriSrdWtbf9Vd4SOrqtPm9JeXytPW74fEksOlA7bOPtml1DvBFmK8DEOGq-L-z30NmtycaWurH78Sd_Sv60JabwswC25ZCMrULxbHlvWCx385nwEqrMaHA7ThpRBHta-KHv-H-bCFIBz5YsHXpCOCtdbN8k3rDyEVLpt8OF54Rh30RbfuKr2l3wFHELTzENLjizS-EoSx1rDGMgC5hyYNFtsKfNHO01Sk7qB6R1FoBZmUj0DcPbfJl8mBrU2Vw1Sk_ri-iePf_Q9ELr4HJ72TpQsD93p3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افشاگری یک سناتور دربارهٔ میزان خسارات ایران به آمریکا
🔹
کریس مورفی عضو دموکرات مجلس سنای آمریکا گفته پنتاگون مانع بازدید او از یکی از پایگاه‌های مهم آمریکا در قطر شده است.
🔹
با این‌حال، او در جریان بازدید از سفارت آمریکا در عربستان سعودی، خساراتی مشاهده…</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/farsna/467850" target="_blank">📅 00:58 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467849">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">دیوار چین</div>
  <div class="tg-doc-extra">قسمت ۱</div>
</div>
<a href="https://t.me/farsna/467849" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
#روایت_شب
|
طوفان در امپراتوری
🔹
کین‌فو که مردی ثروتمند و قدرتمند است، سرمایه‌گذاری‌هایش به شکست می‌انجامد و در آستانهٔ از دست‌دادن همه‌چیز قرار می‌گیرد.
@Farsna</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/farsna/467849" target="_blank">📅 00:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467848">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HtfFE_KA0OTSMPU6mNwUcRTqgstnosITykAAQzEs5POUgcOSbgVMI6C4iDtHLH11EeZXSs4KrFBQkY7U-gxljJOqpxJ7YgCJJqApleXX6mDyCW5-px3Gp5JfKzbnWmjtjkrnoEfzMMVYfdqmTofsWK5P8ztyOxriT76ie2a4Plz9lyE3Tcq9tSTxaEmvVIOvwUYIwqo72bl3UqfPOXRwhEMrlqXSAcvJXln45rhQ2g83J3Ie59pTAlAuvySjVF9UJYDlhvk2Lx0f7et056YMAykDmloWguGP5C9-H24DYfNLJYy2gPMLsI2m5zDnHSRllXy4OmRD3vnD9D6JeJ151A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سرلشکر رضایی: ترامپ پس از ناکامی ناوگان آمریکا در بازکردن تنگهٔ هرمز، به قاچاق روی آورده است
🔹
دبیر شورای‌عالی امنیت ملی: ترامپ که با توهم فتح ایران، یکی از احمقانه‌ترین جنگ‌های تاریخ بشر را با فریب‌خوردن از نتانیاهو راه انداخت، اکنون پس از ناکامی ناوگان…</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/farsna/467848" target="_blank">📅 00:35 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467847">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CpsI9g3z_vh8YOsRrz-ImBJ07hhYHyHsS7LwDQ-U1wO6Rf0HzqWO6nBNzsYYgZTIjjLiJ50YmyniF_FdK5c0KPKYZXbZPuvYDonl8r4O8t-A1a74rSPULW9-Iq0ESOxw5XJZEDSlocQQ20UQhliE2WR-C5YeObtCol1d4O2Pl85h9LPtYbg8NTMRAksOFLOPiCTN8EHdwTRgARMbGRm6i46qRH__qsvwv1I32L8t-a8P6USsOzZkMfyNO5WlIv_qRlCwx96hc3GoK6eydN87n7-17karXJsxV-cNk2xILa78hgUzuDw0aBPH4jgPtMUyoG3TLuWPCwkheavtrPISBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
دبیر شورای‌عالی امنیت ملی: ترامپ با استخدام تعدادی از اشرار که در آب‌های ساحلی عمان فعالیت می‌کنند، به قاچاق روی آورده است
🔹
او هر روز ادعا می‌کند که تنگهٔ هرمز باز است اما در پاسخ می‌گویم: شما درحال قاچاق هستید، اما تنگه تحت کنترل ایران است و ما آن را…</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/farsna/467847" target="_blank">📅 00:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467846">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f6c789ff8.mp4?token=kh35uH0YkDMwX1Qg9i_2KooD_fg87PeYFNJT47L3m4dN7mbOjKdsiXXFlrpVJ6qMnfRj7PPqOcFIeTblSeo2Z_vggq7pj9eouH8nqe9SpCYazUjXCtQyTTbvmYqH-SjuZCNgIn_vX96bqnh1bSMxNRwaaiTPEPsfBOrQ2z_QRhgIQxw12nA6YhLy93_Il7kjNLzXOb8PkmS4eWQiHrAXIwEHi2a3-XDeLznymnY1Z9pop0qQONK-MLf1G67g-LsYoLGyu7iia8ZLia1GmqRyotDb9WTLhyH07mGLbrKToduA3nkv69fy-FBzRKec2WC-9zif7YXjR3rIzP3lszqy6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f6c789ff8.mp4?token=kh35uH0YkDMwX1Qg9i_2KooD_fg87PeYFNJT47L3m4dN7mbOjKdsiXXFlrpVJ6qMnfRj7PPqOcFIeTblSeo2Z_vggq7pj9eouH8nqe9SpCYazUjXCtQyTTbvmYqH-SjuZCNgIn_vX96bqnh1bSMxNRwaaiTPEPsfBOrQ2z_QRhgIQxw12nA6YhLy93_Il7kjNLzXOb8PkmS4eWQiHrAXIwEHi2a3-XDeLznymnY1Z9pop0qQONK-MLf1G67g-LsYoLGyu7iia8ZLia1GmqRyotDb9WTLhyH07mGLbrKToduA3nkv69fy-FBzRKec2WC-9zif7YXjR3rIzP3lszqy6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سومین نفتکش متخلف امروز به مین دریایی برخورد کرد و دچار آتش‌سوزی شدید شد
🔹
نیروی دریایی سپاه: یک نفتکش شاتل حامل ۷۵۰ هزار بشکه نفت خام، بعدازظهر امروز با بی‌توجهی به هشدارها و اخطارهای نیروی دریایی سپاه، تلاش کرد از مسیر غیرمجاز عبور کند و درپی برخورد با مین دریایی، دچار انفجار و آتش‌سوزی شدید شد.
@Farsna</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/farsna/467846" target="_blank">📅 00:20 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467845">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8nELDQsMiAl7zXJm4DGfUHdzg5-ZtzYH9K03-OB6BPsmP8UrqeX4RcpbbPMehFKzH9sjMm1tuyEHVHgKVJLHoTItDjbPBkxg7n2tJ9gMKqE6003KpHYTc80n0D_1yvEADL0x3sSAClcJOh1BB-BUVA9som2KWpk6yBWcApKnMpF_Vo5G1iEpIo-MP3jBSVMKIIY4Jc5XBGQ4wm_aW54byHEjkCB4110snp_H3C6Bu2g0csYF88RSN-AlHgBL0UoW7fzLHOPKVhQa56_itj9K6ybZ1t981Y722GDx_M0z7aK4PMYmR_JlDWixNOB1z1mdsbV-1p08eQxzKmrFDHq5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چاهی که گور شیر مغرور شد
🔹
در مرغزاری سرسبز و زیبا، جانوران زیادی در ترس و وحشت از شیری درنده زندگی می‌کردند. سرانجام تصمیم گرفتند با شیر پیمانی ببندند تا آرامش به بیشه بازگردد. به او پیشنهاد دادند: «تو دیگر شکار نکن و زحمت مکش؛ ما هر روز قرعه می‌کشیم و یک حیوان را به عنوان غذای روزانه به پیشگاهت می‌فرستیم.» شیر پذیرفت و کار مدتی به همین روال گذشت.
🔹
روزی قرعهٔ مرگ به نام خرگوش افتاد. دیگر جانوران خواستند او را روانه کنند، اما خرگوش با زیرکی گفت: «اگر به من فرصت دهید و بگذارید با تدبیر خودم پیش بروم، شما را برای همیشه از شرّ این شیر راحت می‌کنم.» حیوانات پذیرفتند.
🔹
خرگوش عمداً راه را لفت داد و آن‌قدر معطل کرد تا زمان ناهار شیر گذشت و شیر از فرط گرسنگی خشمگین و بی‌تاب شد. نزدیک غروب، خرگوش با ظاهری ترسیده و شتابان نزد شیر رفت. شیر غرید و گفت: «از کجا می‌آیی و چرا دیر کردی؟ چرا حیوانات چنین طعمهٔ کوچک و ناچیزی برای من فرستاده‌اند؟»
🔹
خرگوش گفت: «ای پادشاه! همراه با خرگوشی دیگر که چاق و درشت بود برای شما می‌آمدیم؛ اما در راه شیری دیگر جلوی ما را گرفت و آن خرگوش را قاپید. هرچه گفتم این پیشکشِ سلطان این بیشه است، گفت: من پادشاه واقعی این سرزمینم و آن شیر لاف‌زن را خرد خواهم کرد!»
🔹
شیر خشمگین شد و فریاد زد: «او کجاست؟ مکانش را نشانم بده!» خرگوش شیر را به کنار چاهی عمیق و پرآب برد و گفت: «او درون همین دژ پنهان شده است.»
🔹
شیر بر لبهٔ چاه آمد و درون آب زلال نگریست؛ عکس خود و خرگوش را که در بغل داشت در آب دید. گمان کرد همان شیر سرکش است که خرگوشش را به چنگ گرفته است!
🔹
شیر بی‌درنگ و از شدت خشم، برای نبرد به درون چاه پرید، در آب غرق و هلاک شد.
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/farsna/467845" target="_blank">📅 00:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467844">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKCOkXNL2_Zk9-wXTl5zvdRUIRJRM6tCnWEBcNqUlUoQ0iRFT30p-svlK8DIdFA6kP9bFV8Eu6D3U2sicFXVdEop4ufWeO-mJqTY1o1Vl4sEjKMo1FYDXJRtUoUtkGkNNjnWneHnBI3iUcFbNUaF8yvwYyuOLOtU3B6qYfzgZu19OmO1oMAPInf9ikv1C3ajI2KdHbBVTYw9S4soTU1ZMzdod7KJ6CujvW8glSQaGFUp8wBiFhNXAAPzW2xQOrVhIy1fyOTy4EpJZes3gCuHOgejY_bqj6CsJlD2v_1eByM3aEOPLDP-GDU6O1gfCiLQyvaTTexV5nAeKXdiAni2bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس را بدون اختلال دنبال کنید
🔸
به‌دلیل محدودیت‌های ناشی از تحریم‌های آمریکا و عدم ارائهٔ برخی خدمات زیرساختی به خبرگزاری فارس، دسترسی به وب‌سایت فارس برای برخی کاربران با اختلال مواجه شده است.
🔸
برای دسترسی پایدار به اخبار فارس، آخرین نسخهٔ اپلیکیشن فارس را
به‌صورت مستقیم
یا از
کافه‌بازار
و
مایکت
دانلود کنید.
@Farsna</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/farsna/467844" target="_blank">📅 00:03 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467843">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c83a2a0a36.mp4?token=sBZadEGScDXeV0zj_YC5MI0zwY3oFgd2e-A8ql7XrabB0K7E3eJg4a4kC7E8AiFxZmlO3-8MMIWZSdXpoGM55s1hrLkE8Df6eVxYc9E9x46y67jwTI_Ud2d_ktH5B8nMLgaaFchBSOZLXh0K6ThLctHSTHRjSG2x0YmwUpiccX-HpeZuvJNF1kty1-s257WubR_9MAnzJ1ckGC4QCUIaRLosgiACbdAf7V-Rk9uORcmEdmFhwOTqzK4wm4HBK1Eo5P_HwIJswiZirIZLxwbsFOKGV4flJEi8Bb2s7rKd7vHG1f8h_ye2SDNLqAFuziZsQEwKjxVCF48JZGLy2yCWLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c83a2a0a36.mp4?token=sBZadEGScDXeV0zj_YC5MI0zwY3oFgd2e-A8ql7XrabB0K7E3eJg4a4kC7E8AiFxZmlO3-8MMIWZSdXpoGM55s1hrLkE8Df6eVxYc9E9x46y67jwTI_Ud2d_ktH5B8nMLgaaFchBSOZLXh0K6ThLctHSTHRjSG2x0YmwUpiccX-HpeZuvJNF1kty1-s257WubR_9MAnzJ1ckGC4QCUIaRLosgiACbdAf7V-Rk9uORcmEdmFhwOTqzK4wm4HBK1Eo5P_HwIJswiZirIZLxwbsFOKGV4flJEi8Bb2s7rKd7vHG1f8h_ye2SDNLqAFuziZsQEwKjxVCF48JZGLy2yCWLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گره فیبرنوری در تهران کی باز می‌شود؟
🔹
وزیر ارتباطات: در جلسه‌ای با حضور استاندار، شهردار و معاون اول رئیس‌جمهور، به‌سامان‌رسیدن این موضوع پیگیری خواهد شد. خیلی خوش‌بین هستم که بتوانیم خبر خوبی به مردم بدهیم. @Farsna</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/farsna/467843" target="_blank">📅 23:47 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467839">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XChR9BZn7pela01IrN6lSwBIaaDhki6233cTUYolbWgCO9eT7yeHHzVkCJElPPmcdvHgUWA8_p7Y_igqqCvnmeTZGVYB3AySevsmBZ0AawGtL6UlOsIze6xX3_5KoIioUpbZxn0Esb7sU8zkfCcSQTyZrugiCCyF4mlbRo2BchByd0HNnuwQ6INvOSiNmHGiZF8osW5UfdOgB-pcVi-RFzHOLKGsZLj1Njbw6oaltMAcJucu0DfmZfI10c-b7PDTh82PZx1sXHeeh3pfQF7DWZfZtiMh1V81z9G8FW8-36Q4JjKm2VYny7wUeEG5vrBF6LYK1VJ98pO3EXN3VLHTgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VgB5TCcomwhnJwnYg6BETDsdpNndT9rRm8jt2lBiH94NT363qRu84QLF4HUiBA6viKnstP_wquvl3I7eI8b78hTGzbO_8IYGGF6GOzBOigKo4KRwaBwpqKjYNB9y1pmJkiYMSE0fJTZxxWk33XSWC12RyasusGIt94l7KOgL7sQhCuIcX5jq7bISYVNMhqGOcixlbC078FLJwVzGNYQ2xwhTVyq4uX9Ca-aZgiUpK-hGIQSNbWbjKl3-koB2Q31s9Lv3qGvkfXULVEM_WzdGQLZ8V6LPLkgwLvVWc7RbfffPPxa1-F9OLjqvXU5qbmWzHNxPZPa_FVfzW2CYuKigsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/puSs43brthqM6O2o0zJYOPH0mPLef5IGMjoSCjmnoUO2vP8kWRwzKBFYm4H99HYJR6mMJiiYl9W-yJgkqGBBpk59Aa6GVNLfV9H8eKuStC9huCT_9DQJ7IP4TB-xIk0vNjTz3GHB8-91gIKN1AyUy1Rl6bXIYaEEUUW7l1pNSEjsb4zeDFHDQ7g8gotzUYkR7MxopL34CB2TOnKf5xVj81ZnFlWYDq4nOlk-9oDCl-3xdminDGpJ-4z3B-eiORN45KWgy33eVOwL_OOmR2bvT8KuP-KT4LNLg9VkBoYVtx_OeR9eBd4qJm2gALKi1sVYIQlQV63AvBssnJqb-uQwBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jINSaLREHUvP09-QDa-0XITsMy1esKZcnR6wQR46-0tvxjtGCTRoH9dEANDrlmSWGh2jKsUUR4FAK4Mh8p4s5PgEgs2vxfPN4E5wVx3pXAlczebZFw-7HApDXzbk6b0H3ZDAyXsiIv4Xxdp3ysTS3gRBWr3WQvdHhNfrKdk_gSF54c9teQK34-wNF2nVAReRwHKks2nQPAkQ2KXV-wAcvvhC0dTDI1LB-UL3MTz5UJmKzocJ7tp0SzczIh0DocNP7jSXmGCHaOMex9pN6JosdDVZoAFEAi2H7V80qEUOjWsNW0n4i1tt9LS35l67fi0zonAjqLlqsJQoSwGcpmGrdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مهر آیت‌الله شبیری‌زنجانی شکسته شد
🔹
مراسم شکستن مهر مرحوم آیت‌الله شبیری‌زنجانی از مراجع تقلید شیعه، باحضور جمعی از علما و اساتید حوزهٔ علمیه قم و اعضای بیت او برگزار شد.
🔸
شکستن مهر مراجع معظم تقلید پس از رحلت، از سنت‌های دیرینهٔ حوزه‌های علمیه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/farsna/467839" target="_blank">📅 23:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467832">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V-vXlz0CWigfAID3jSsUzCgmcbW5e-SYlsd6fKwDS0bFfFF3oeDybjOJRIk6FqENA9TTT7RrqaqF-ABu5iiIHuQoq3IEcaqj6e5DKrJ45Y4nliEZ71gha_Wt6dTlVXnjVu1rJ7OQRfBRiY4I_BfmmIOYZaR3TBtjGj-iqvyzIXuwICM3V5EmWv40PgEhNKtCbHIXMFQx9SaD8ygBvPFp3DPJ5qoKQjbGgYPWH6UISQ2Dp97sASp0RidM49K7IJZF39NjBZCHgkwP61B1uvwj4bNj-_ce8kyU8hwPBXjKnHKio7cbRmWl81TdO731N7irt7bzevns-m-MTV4TyvWpKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FnkGrFfKU4vJe21-WGNsme5lygn5djORyd5ct40YimUWyZ6xXbmSdRWjK2F8GeIgng7Pq_goKNnEGpIm3tpG5dgxdxb48KqnDj_eeVoPkUUPEfnHmNQ537y88IddEqMcJnfVijgosHERsWO4zNT9Kl5j3LTtSd1VR7yLbpcmFXxoDjeHwKXRINt50Mhc-J7Vfox9LU06g6DOS-vIOQEMSDfIZ0g-MhvGVqeMwtYlOvWe0u2Z50bFzsINVcMmL8CM2kDRMfCU9-AsyTNqaYWlepsO7mAtgbQhTAQUk5zDuuN2KhgsYuIl3h8hdQj-IP1DfSPtYDetXmMJfY5v1chVwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YmU9tUBmlatPRbKadU2CUcERXzmDRRmrEQtRPpl0vmWnrpuyT9-Ga-FH4mt2hHQuAWxVvN1U3ph6sb9946biKPER4EP7QTnEGRNgC6UaYueWw4Sv7DY9hJ-ixihWaN11C_bLlmWxYmngPfbi95uZjOIqT-h0MP-i7fisFRN0pmpVEad9A5bRPjyCJlpNB4BB_aGY4-XdYlyF-0Sq09r7Oof-X4M4KuAoKaW3-wAWB1yKi1zcSe-_GtA06NWD_XbQj7ZAZX3B2ugKzi2A5hlYOoZQ2O8d4NWdAECCg51jHBHHRJljfkGCoKuTWASFQGtBZU6hc8s_nHCPT1W8NnMrVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BNB6J3GNo8swbbVWWwUxEufm1S-Hue3tLDRxxarg6bNiK5FAAlOVDsq1rum1VtKT6MB_PMEat9JpZlTdTZTW1fJA0lVWX7rHVKl54blr-_52ymv_E0a--nTgZHrbdxQQBv0RArWUe5BiMChZllNq0iTliY0XQzcclgTiDZtZwV2MRAzR9zZig8PoeZZEkRMEjOzmvgKx5DnwU9L3f5eh34RNtESX9DNxGj0ex-_aBYq-d4p3giqV7k0qWGbd71Edfi99OM2befvLR64adDXxMKDSf9t6yvo9opW6d7T5Uj9nF9HglDX2XeRMHVn7LpyT-hbSte_5jo0NJ7lQaPfAbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HghlGUS45D9d6q3ani6tmET4cii6dOmilNzJp3dDABtLQvfmUfBWGTIP4NoGKW2wAyorXo7OaMXwmppF969zLY3c4lKGFSFGEAEHx7Y48gLSrZB7rJ7ESRUZrdQA_laCdHS9XOXuNaQuCr_Mlv14dVp8Y-m5-0lxjQOIHtSKE2YIPIpgBME_VDPFYk1IJSESTWyb4Rw6mjguSSF3vyO_dhUpWWGd3snLRrpGTBbU484FEUPYvs6niAyn3mevRrJolruVkkw4vaWaK1H5biDxPQJHRLDGNI8b6sVoqHDXUKVqhugn1aAYmWzbt1ONGzik5gs5RlacGUWJQpj9MQAAOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J_iss19LdMhk4Th82NLZHgJ9bIyA0dgVuMGTZoAg5kMqGCW331xIdtR8kh8sFEwdapWY1rKYGyF8VuiYN4j5yFsKrAhW3InsgZMPFKjshOLmsty9SJsjgtWffyDW9epJwCYEqXuJCQjNQB8uxHTbW-zmi9007ElYFCSYzcG_9t3-6YbPaYk6RU7_4LVmlGF5K1rEFlY7G1I1f8aLoHBzZYrgMFjWJR8kuWmNKS3qRmiJbrLdsBZHubq9ky0g39LDA99yFbP99-ZCMwjDJR0SWAhC5e1tdoS8eIjZ1slp6WVVBFCiXg0ovCxKWE6D_ExTC-yCKxF4JUBc9eYDRhS8KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LjvolhSpN3-rrG0Ppn4Xwow9iEeSc1oHqgT4MayDjMhU-uisXP3Sklb3Z-rqVYykrAyFnrFm9En3wH-QtbDhbtSarqaQgfrKdA8T0i4KIEqHNkbh6kQ3si2ydrpRJuKqGdjylsMc4HZxnTJnKCp9UEMeCVvt9JZYaIocrqiA2gPBYrtIA1kRwsGqWmytH8dz7k9U1EOMcLecPYLn2HUArpDddRp3J2gO1apAlhlSgH5bSwdCtH2bSk0bh2HBli1_BObY0-qzd1xcBBZ4Y_kKylH45M99GvvMoiUXxgIPp254-fx68c5aNaQnfJ0yY6ovTmfGi_tUSzIoUYaMqLEtyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
ردپای سردار سلیمانی در منطقۀ صعب‌العبور
🔹
سفرهای میدانی شهید غلامرضا سلیمانی، رئیس شهید سازمان بسیج، به مناطق محروم چهارمحال‌وبختیاری، به‌ویژه دهستان دیناران و روستاهای صعب‌العبور دهدلی، زمینه‌ساز اجرای طرح‌های محرومیت‌زدایی از جمله ساخت مدرسه، انتقال آب شرب و کشاورزی، بهسازی راه‌ها و نصب پنل‌های خورشیدی شد.
عکس:
رضا کمالی دهکردی
@Farsna</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/farsna/467832" target="_blank">📅 23:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467831">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnQiwnMBV9h1LO8mzolav-RQK3RocR6NXE1WU470c_DDazUGibc6DDop0QSkP3XR_UE3JE5-sZX_x56NSD3azBmaVfwzXBcH6U_f0lSZadDAD9_erxZoDDQNLotPJkv_-h_x80zM2MDmrUmXSkSk3D4doung8jGV2oBQLv9r3lwd7t71oms8IZKCvmmybSL4ioFQ2W_CDage-a_3bDvbLLMwNyPuW011f7vhahXAZQhHDJsxTE6fLmNDXPCk8cqw90F6lxotw1t5k7PVuwymZcMkCzTQ_uKlCk1-aGmZyk__8H_Y4rOaYSIglx2NtOfklMAhU8M2jekvjn5J6sJ-Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سخنگوی سپاه با انتشار تصویری در فضای‌مجازی نوشت: ما منتظریم
@Farsna</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/467831" target="_blank">📅 23:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467830">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0a28e7693.mp4?token=OV2V0BJkIBFv6s-yTZXvq_BuL4O44rf2d2tcKLt2anZXe2Byk7uW7aa-_uv972BJDjflC9ymIODMm1tFCBuKFWdY97FXjd4LuxF0gUhlJxhlWggF74DBvlo3i28N3YcXmlHX75a3VwQ34v5oGoDrABjDCuN5sEfMV14fUpVY79QBnrQHIIgI9OxHfI0a0CClPiXrdM0n6VPGNEOrJvw4r-EGSouZB0OWK88PS0QfvWqcQazxvTiLZchCOrDWISizCELcEfSuzGfxT19ocobid8XQDoCdkbbGDFXiad1EAlafX9ArBWnJbRshh6LVajXxLcC9SpMcCagGmaFiEINIbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0a28e7693.mp4?token=OV2V0BJkIBFv6s-yTZXvq_BuL4O44rf2d2tcKLt2anZXe2Byk7uW7aa-_uv972BJDjflC9ymIODMm1tFCBuKFWdY97FXjd4LuxF0gUhlJxhlWggF74DBvlo3i28N3YcXmlHX75a3VwQ34v5oGoDrABjDCuN5sEfMV14fUpVY79QBnrQHIIgI9OxHfI0a0CClPiXrdM0n6VPGNEOrJvw4r-EGSouZB0OWK88PS0QfvWqcQazxvTiLZchCOrDWISizCELcEfSuzGfxT19ocobid8XQDoCdkbbGDFXiad1EAlafX9ArBWnJbRshh6LVajXxLcC9SpMcCagGmaFiEINIbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مردم برای افزایش رقم کالابرگ چه کنند؟
🔹
کالابرگ ۳ دهک پایین جامعه یعنی افراد نهادهای حمایتی بدون خوداظهاری افزایش می‌یابد.
🔹
اما ۲ دهک کم درآمد دیگر بعداز خوداظهاری آنها مبنی‌بر اینکه درآمد خانوار از یک رقمی کمتر باشد مشمول افزایش رقم کالا برگ خواهند شد. …</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farsna/467830" target="_blank">📅 23:19 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467829">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/531c641946.mp4?token=TUpS6e2qgwtQb_9lix1TMdI37-Y39NMa3YSxKI4JmjRRPR4DDCvL4w-z6LxmVDxtemy9XpyTR7l0RgrMs0O6u2UQrhQh8LFI5ur5QtblwtWgM2sP7--7gVgxTReihao4lrfuG8ppAry9xtyiHIuj4J-6_zpV_bkAUM0boveMsL09-O2nNnJyTvax-k1aT1hWzZm9BomE97iT8lv5_0F6U9p5etON7bd5J3uHFR8tgnIK-VGfxsr1nCEOXZXBgLMFqmX6_C_aK7Ai_Bt6DR-UGfIG0Tbj80LuR7Zez6IZxJqWzv31uG7mbaeq5LdH1-Em21jF4AsQ9pOLX5NmsTHTqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/531c641946.mp4?token=TUpS6e2qgwtQb_9lix1TMdI37-Y39NMa3YSxKI4JmjRRPR4DDCvL4w-z6LxmVDxtemy9XpyTR7l0RgrMs0O6u2UQrhQh8LFI5ur5QtblwtWgM2sP7--7gVgxTReihao4lrfuG8ppAry9xtyiHIuj4J-6_zpV_bkAUM0boveMsL09-O2nNnJyTvax-k1aT1hWzZm9BomE97iT8lv5_0F6U9p5etON7bd5J3uHFR8tgnIK-VGfxsr1nCEOXZXBgLMFqmX6_C_aK7Ai_Bt6DR-UGfIG0Tbj80LuR7Zez6IZxJqWzv31uG7mbaeq5LdH1-Em21jF4AsQ9pOLX5NmsTHTqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ظریف این‌گونه ترکمانچای را تئوریزه کرد
🔹
ظریف در ابتدای دولت معاون رئیس‌جمهور بود که به‌دلیل تابعیت ایرانی-آمریکایی فرزندانش مطابق قانون برکنار شد.
@Fars_Plus</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/467829" target="_blank">📅 23:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467828">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93b56e2de7.mp4?token=myglTLK5ZIfwjD3Kr75z46PQuvMkFscC-XtGdrudrNY7hDBDG2XGau9BQqLyvMXj6Uvz9er_ErBoZPBb4Xw9PYtpv8LmxD3OWY_I3CsXz_872Wztl7PXm5kPfaT0nUEO5-SMtgZDs7kBBr4KfTWvW4hfPstT8HeOEWTwupJgPsMRlYqJS359VlR0eMtSxoHUPTVfD_ryhSdz5DI39mgBWUFcJL6ysjmvX9gZUpSoq1cryAOv86ijX1_ykJU_-15JxTiGV45rxZanhmevI2RNZqaEZpIHVvc6XfHHrMvTdr9nKsYHYa1Tr6azvmrdmnyAef1QVrHcCyIDQUCQGBGV9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93b56e2de7.mp4?token=myglTLK5ZIfwjD3Kr75z46PQuvMkFscC-XtGdrudrNY7hDBDG2XGau9BQqLyvMXj6Uvz9er_ErBoZPBb4Xw9PYtpv8LmxD3OWY_I3CsXz_872Wztl7PXm5kPfaT0nUEO5-SMtgZDs7kBBr4KfTWvW4hfPstT8HeOEWTwupJgPsMRlYqJS359VlR0eMtSxoHUPTVfD_ryhSdz5DI39mgBWUFcJL6ysjmvX9gZUpSoq1cryAOv86ijX1_ykJU_-15JxTiGV45rxZanhmevI2RNZqaEZpIHVvc6XfHHrMvTdr9nKsYHYa1Tr6azvmrdmnyAef1QVrHcCyIDQUCQGBGV9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم ۲۲۴ شب با حضورشان نشان دادند که پای عهدشان ایستاده‌اند
@Farsna</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/467828" target="_blank">📅 23:10 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467827">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQOP4TClrAPG9J09360l0gnxnvv_QEmcJD3WVWueZt8kPv8Cx44WNHpwnCritzlx09190nqASdhK0fwkGa4eXbURqoOP6ioOkJWaEkyUUQnhkPxxrwPTLIDN1qOF2JptPRTuLQ6AFnJ1z5lpP7oKBy4lt6DHVqxLvYl0mJzhqoCZo0lkpNn9ZOfCRIm6Jv7Fr1mw3q3rC56gFpGJdCwVsIYV-q5Cw7jAr-QvFo8nSkiOaOxPAWIlzOliVAI5P2f8YF4-4mhJA1a7iFZ-6_wp-eIlul9BzYo-YlsxHuoaSeqIv2uu3hLYlij40Wr-f4JHEk9ecmuoVtX7n9dAAo-Rhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ تعیین تکلیف آمریکا برای عراق علی‌رغم پایان حضور نظامی
🔸
باوجود پایان حضور نظامی آمریکا در عراق و تکمیل خروج نیروهای تروریست آمریکایی از خاک این کشور، واشنگتن همچنان برای بغداد تعیین تکلیف می‌کند.
🔹
المیادین به نقل از یک مقام آمریکایی گزارش داد که واشنگتن…</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/467827" target="_blank">📅 23:07 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467826">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f25751012c.mp4?token=LW3hYNn-PPaxH35sGwKmsilLO8TsIoU_TNvb_7N3uLD58Z-PiTzET9vNsvSmAjrfeJbXFHkHOCiTdW37LW8_R4kKd_z4KWVsaHw0FsXd4r2DyDyJIKqv2QoWGLtzpQtuvAS9F13mG_aD4mxB6cKsg_5IwN2OPJ_HU3B1jdSiMMNohVLNT4yc5B6WidIFivP0Ae1lkZ502oVi4iETcqMi6ZgYAr5X5WOZmK0uzHb7Erc-lfmHr5t6G0mRuj7ur6S1ceotcaMleat3ku91wnfC_lnWi_CK_Vw9HtEUiOBU2ViFxKoI_ogFbvCEG6pOXIS6DwkmjuGGEJtHUoUtdDQ2lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f25751012c.mp4?token=LW3hYNn-PPaxH35sGwKmsilLO8TsIoU_TNvb_7N3uLD58Z-PiTzET9vNsvSmAjrfeJbXFHkHOCiTdW37LW8_R4kKd_z4KWVsaHw0FsXd4r2DyDyJIKqv2QoWGLtzpQtuvAS9F13mG_aD4mxB6cKsg_5IwN2OPJ_HU3B1jdSiMMNohVLNT4yc5B6WidIFivP0Ae1lkZ502oVi4iETcqMi6ZgYAr5X5WOZmK0uzHb7Erc-lfmHr5t6G0mRuj7ur6S1ceotcaMleat3ku91wnfC_lnWi_CK_Vw9HtEUiOBU2ViFxKoI_ogFbvCEG6pOXIS6DwkmjuGGEJtHUoUtdDQ2lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرا سرعت اینترنت پایین است
🔹
وزیر ارتباطات: علت اصلی کیفیت ضعیف اینترنت، تمرکز ارتباطات کشور بر شبکه همراه و ضعف شبکه ثابت است. برای حل این مشکل، پروژه فیبرنوری در دستورکار جدی وزارت ارتباطات قرار دارد. همزمان ارتقای شبکه همراه نیز پیگیری می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/farsna/467826" target="_blank">📅 23:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467825">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee6e4c0d2c.mp4?token=SSePB69vVnPGMVNaJh7I1rIYFU3HrPcir83ar7qk6y_hC4goDtVB3PELK03iICkPCxuZEVG73U6mtPj-uYrQgNup_nm0Ow6fqWwO29LtjJaP8FRiFyNPebweWalbRFNlW-LWnnAFR7wQOPbpuWJCuVpyMUOUrGFyHAEi8b57-biP7-JIqtUH9u95MhBvppP0spQPeUDXPH23S2jQkop_cin0DMBv0KT86Qyqyl3noXhoYctT2Yy3_VryWPwKVUGZiLzML1kUEpVnrbaYIFEvYqQQlUXR3_oYBdzKMD4Ma0X9u0q5Y5jtgfLQXJZh_6ZVSjk7DlhGS5aMEYK-4Z6gTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee6e4c0d2c.mp4?token=SSePB69vVnPGMVNaJh7I1rIYFU3HrPcir83ar7qk6y_hC4goDtVB3PELK03iICkPCxuZEVG73U6mtPj-uYrQgNup_nm0Ow6fqWwO29LtjJaP8FRiFyNPebweWalbRFNlW-LWnnAFR7wQOPbpuWJCuVpyMUOUrGFyHAEi8b57-biP7-JIqtUH9u95MhBvppP0spQPeUDXPH23S2jQkop_cin0DMBv0KT86Qyqyl3noXhoYctT2Yy3_VryWPwKVUGZiLzML1kUEpVnrbaYIFEvYqQQlUXR3_oYBdzKMD4Ma0X9u0q5Y5jtgfLQXJZh_6ZVSjk7DlhGS5aMEYK-4Z6gTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجید مجیدی: مردم شجاع ایران سر تعظیم فرود نیاورده و نخواهند آورد
🔹
کارگردان مطرح سینمای ایران در جشنواره فیلم بوسان کره‌جنوبی: ویرانی‌ها را خواهیم ساخت و مقاوم خواهیم ایستاد؛ تنها جرم مردم من این است که می‌خواهند استقلال داشته باشند.
🔹
اجازه می‌خواهم که نمایش فیلم را از طرف خودم و شما به مردم شجاع و دلیر ایران و ۱۶۸ کودک مظلوم میناب که در روز اول جنگ قتل عام شدند تقدیم کنم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/467825" target="_blank">📅 22:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467824">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19fd6e811b.mp4?token=KeZh9PmDhTIBxK-57rRZh1MzkaVUXmjhoqTCRymeR0udDzbfehnykc0b4wiCjCnFS4OE3LrEoWJS-hguFfuxmNIAXaXHl08kGZA1-VKP6pGWPbOfjAWs5VJHIvU-i3lLr6tDnGy9cqXx44XO_s18MHAWisonr0RzYavABNx3uPdxDyxuTzxG7e7ipZl_RK9-ELvBGkImhRDTo9O6poo2E-VzkB-bIsh_b2pppAMJABxXNs-ijQm1PqUB66G92kkOS0OtTMYSpTkGMCRzWpmgt8y0s2S1pwIqfNFKVTQB8qurwelE_EzXVT5doTed0RHG01764NjGK_msXpU_ouhqwSk9RrWvfPM_-E3ZhK5Wd7a3e32XO7GBeAUoiGSgaa-9I547XbL-kEuJjCy7kuPT2fGh7MOGsFsn_EBX4XqYm6AnGyWGQWp1PkdiWNfoG5kLZTiHLnPYOCsuod6kXGgvOJnfUNZWU2BHt0szOcg-VTOcImsFlfENOCVHx9wilN9l68lO3G2254yL9XgsyD4Mb_3YSytJxh61piBc6N-0jndfrjwsbdfathorv9M4Zga7oO6Z7RH6qRWukUfBiCDaGmi40MMMzxCQxKfzq8yoa9b0b_LQeTXTFOwQTU4kCpGSmRhHhX1i20t-VwDb6VyqHLdNqZmJ91buSKhyDBCU0BI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19fd6e811b.mp4?token=KeZh9PmDhTIBxK-57rRZh1MzkaVUXmjhoqTCRymeR0udDzbfehnykc0b4wiCjCnFS4OE3LrEoWJS-hguFfuxmNIAXaXHl08kGZA1-VKP6pGWPbOfjAWs5VJHIvU-i3lLr6tDnGy9cqXx44XO_s18MHAWisonr0RzYavABNx3uPdxDyxuTzxG7e7ipZl_RK9-ELvBGkImhRDTo9O6poo2E-VzkB-bIsh_b2pppAMJABxXNs-ijQm1PqUB66G92kkOS0OtTMYSpTkGMCRzWpmgt8y0s2S1pwIqfNFKVTQB8qurwelE_EzXVT5doTed0RHG01764NjGK_msXpU_ouhqwSk9RrWvfPM_-E3ZhK5Wd7a3e32XO7GBeAUoiGSgaa-9I547XbL-kEuJjCy7kuPT2fGh7MOGsFsn_EBX4XqYm6AnGyWGQWp1PkdiWNfoG5kLZTiHLnPYOCsuod6kXGgvOJnfUNZWU2BHt0szOcg-VTOcImsFlfENOCVHx9wilN9l68lO3G2254yL9XgsyD4Mb_3YSytJxh61piBc6N-0jndfrjwsbdfathorv9M4Zga7oO6Z7RH6qRWukUfBiCDaGmi40MMMzxCQxKfzq8yoa9b0b_LQeTXTFOwQTU4kCpGSmRhHhX1i20t-VwDb6VyqHLdNqZmJ91buSKhyDBCU0BI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور وزیر ارتباطات در خبرگزاری فارس  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/467824" target="_blank">📅 22:44 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467823">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f20e92e4b6.mp4?token=cMeABTUuZMnFFBhfjYDEK8wRpK4WgtAbHrhL76EUEOMkcqobB3X_PJ7uQo-UAI5RqSWxz4Q2cGYpwH7uvat0xv0NDjrXomLkt04MZsU63v1aomyY3yRIKExNtzblSNhcZLlnR3OWNNOguNIEeDL9aGUShytmaVom33ey3QBn_vujvPfINg0yfSCrrlly19Mvdp3aZlE6GDE9ATBFFUI3SwlLQI8WBOaHTDosXQmkJxZCZXZsjLmZaZ7tNKAAdz3THErLS9ePh5ZWubcHlWLDVGO2sedzpOezmzPHBw_XEUPvd8V5SYt94eIbjASa3WBwpS-ikmlrmKmlkK5YBT3Co26Kst9JQJ1INRwBb8ZfKlExYcglWwny2-Reg635qcf1JkMZ87POc-6vYHA6qWDrMYkznIU9XgD4kcSsimhZcFkGOwVWfelRsvQvOfRREuYc8hFsHJdRNjQGnISpUyGayT2n72iqpXvKHAyyULDH2GlSGX2VrUXafagX_OScYxLm-GoX3aLNpF8lAxQ5UUhHfL--WSVSYIkpjjTkOyEyurK1P0Uas3MgYODsq4t2lxrdQEAyh6ACh1BEAKSEvk2E5mr_w3VVubaYgRHaxH9Ptj5nWYdPNwhKwFm202Pf8ZEWCiVEJm0g1WvX57Tjlnh8c5c3K4JbN5wGPPXijSeP-8o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f20e92e4b6.mp4?token=cMeABTUuZMnFFBhfjYDEK8wRpK4WgtAbHrhL76EUEOMkcqobB3X_PJ7uQo-UAI5RqSWxz4Q2cGYpwH7uvat0xv0NDjrXomLkt04MZsU63v1aomyY3yRIKExNtzblSNhcZLlnR3OWNNOguNIEeDL9aGUShytmaVom33ey3QBn_vujvPfINg0yfSCrrlly19Mvdp3aZlE6GDE9ATBFFUI3SwlLQI8WBOaHTDosXQmkJxZCZXZsjLmZaZ7tNKAAdz3THErLS9ePh5ZWubcHlWLDVGO2sedzpOezmzPHBw_XEUPvd8V5SYt94eIbjASa3WBwpS-ikmlrmKmlkK5YBT3Co26Kst9JQJ1INRwBb8ZfKlExYcglWwny2-Reg635qcf1JkMZ87POc-6vYHA6qWDrMYkznIU9XgD4kcSsimhZcFkGOwVWfelRsvQvOfRREuYc8hFsHJdRNjQGnISpUyGayT2n72iqpXvKHAyyULDH2GlSGX2VrUXafagX_OScYxLm-GoX3aLNpF8lAxQ5UUhHfL--WSVSYIkpjjTkOyEyurK1P0Uas3MgYODsq4t2lxrdQEAyh6ACh1BEAKSEvk2E5mr_w3VVubaYgRHaxH9Ptj5nWYdPNwhKwFm202Pf8ZEWCiVEJm0g1WvX57Tjlnh8c5c3K4JbN5wGPPXijSeP-8o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جلوه‌ای از شکوه حماسی کاشمری‌ها در ۲۲۵ شب اقتدار
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/467823" target="_blank">📅 22:41 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467822">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔹
فرودگاه بین‌المللی ملک فهد در دمام مورد اصابت مستقیم موشک قرار گرفت و درپی آن پروازهای این فرودگاه لغو شد.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/467822" target="_blank">📅 22:23 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467821">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‌ تعطیلی فرودگاه ریاض ۲۴ ساعت دیگر تمدید شد
🔹
وبگاه «فلایت رادار» اعلام کرد که تعطیلی فرودگاه بین‌المللی ملک خالد در ریاض برای ۲۴ ساعت دیگر تمدید شده و این فرودگاه تا ساعت ۰۰:۳۰ بامداد فردا به‌وقت تهران بسته خواهد ماند. @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/467821" target="_blank">📅 22:17 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467820">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1snTUaGzbhpNBdokQdC5c7ayJix3_fL4yveCeOpyLhD7dtzdUfGvtw-SZgWq31Mp3twsqN04YQvlV4clJsKDH-4esZpYjn9sibxouyZIKC2-oP1uu5k7Gjcylcgcj9yN7u6ScFir7RpyXVqYAuUH69QwHoWAUXNrxfyokNERnHmPUuuUOV36XT7mTtR2y6LDcHRSN5rJTdwK__ozm49vNNlXbuxgeZUERMFslhr1nUZSKJgEnwEHn1ja00wkbK0jLuLQXZHYlF60GdxsmDMf2_HQTs8dARpFx9QnHySeaD73CixDCtsEwpZ5y4a-eL0PES1RdbgsvRMDAKyK_Ft6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
فرمانده نیروی دریایی سپاه: تمام کشتی‌های در محدودۀ تنگۀ هرمز که سامانه‌های ناوبری و شناسایی خود را خاموش کنند، به عنوان متخاصم شناسایی و با آن به شدت و قاطعیت برخورد خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/467820" target="_blank">📅 22:13 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467819">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2d71afbb8.mp4?token=kgavGyZZ65TniFEiLiMw1568Gq8Brr9vMtoueYUVld15CCz6dj9e7i0zA7YtmYKuDqXV4BlF1YVJpCArM521eGEhB18LaitVLu7kDN-4aOsE-uui2bJugJoWimQJ-aYV-gNCw3NX-YrgqsxTmfSsampWBa_IxLLdt6uLlJcztHpz5iWkEYyS64QbWtpoFil8x-s3YJmZi3friJLn0HYw_skbFs4JmPvNVvg_JL7aljz0ccxkVI7HntLkpte_SJZUBSDfnQrU7AIiqbDX0iNfopk5vy2Gm5OUVWrVQ18lsp-QAfscpTM9byHzN_BawZz4t774WZvyYHgr5qjTuM6F9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2d71afbb8.mp4?token=kgavGyZZ65TniFEiLiMw1568Gq8Brr9vMtoueYUVld15CCz6dj9e7i0zA7YtmYKuDqXV4BlF1YVJpCArM521eGEhB18LaitVLu7kDN-4aOsE-uui2bJugJoWimQJ-aYV-gNCw3NX-YrgqsxTmfSsampWBa_IxLLdt6uLlJcztHpz5iWkEYyS64QbWtpoFil8x-s3YJmZi3friJLn0HYw_skbFs4JmPvNVvg_JL7aljz0ccxkVI7HntLkpte_SJZUBSDfnQrU7AIiqbDX0iNfopk5vy2Gm5OUVWrVQ18lsp-QAfscpTM9byHzN_BawZz4t774WZvyYHgr5qjTuM6F9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور سردار عظمایی فرماندهٔ نیروی دریایی سپاه در اجتماع مردمی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/467819" target="_blank">📅 22:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467818">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t91uwYjY9_BU3qgGYCEsQkR0zun8-Lo7zTLelJRWXeW2qv1ZWNovBCo27vCYd0MtAL8P9LpfAVd7VuNPauQ1xUq9EGRpDCBfHQoglIVilF38yKPHtvskm48EB30qNLyB_Iyfw9YwirkK4SplrshfPXdYnXsOggfwfhbuYfhXRCCBE0RLUrFXH6uxN_L4TQTXmKkJecicEzGog8fqX13vo5-kdWQY9hhx5UUz13fZUeMO-s625co_cfiIVfnTOkIhx7jg1XZ_465MRsClw0xGsX_i6e7j2Jn73DiI7YVDhkBuw8d-tmJ6KRniyVg6TAuWtl4XCY-oy14XISD2JBLNlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سخنگوی سپاه: در نبرد نهایی تمدن غربی با خفت به خلیج خوک‌ها باز خواهد گشت
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/467818" target="_blank">📅 22:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467817">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
نیروی دریایی سپاه: دومین سوپر نفتکش با مین دریایی در تنگۀ هرمز برخورد کرد
🔹
روابط‌عمومی نیروی دریایی سپاه: یک فروند سوپر نفتکش متخلف با برخورد به  یک مین دریایی عصر امروز در محدودۀ جنوب تنگه هرمز دچار انفجار و آتش سوزی  در موتورخانه گردید.
🔹
این کشتی با…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/467817" target="_blank">📅 21:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467816">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88b101e387.mp4?token=J_-PhcvBWV5dH3GG107pjI7X1c5xKGI0HYpmeCzTjZ-5SBosLgPWT0Dap30yBrtzNzx506GSGgBMgvuHhxT9iHnaDbSiZLpd3knC5cfQzoGUFOdAssmoPPLYlKOjpvz6z2FDUgTbbmaQog_8t67xGm_t7F5PF0SWpLtmTkrIww6sPG6sHaXYTz-V7xJxmRAyQwqsFDts6-bERjCMo7LBKDpqLfq4nke6oMi4wKJBDccYWcGICy9VUE5a6b1x4Z6oBCGO7rjU9uSPs9YE6vZB3E-6dC6LC8ToyfpAjCqaW872p-Ui0tAC_5ubTS_GG84wyiXes58jfNnBAeWywzijyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88b101e387.mp4?token=J_-PhcvBWV5dH3GG107pjI7X1c5xKGI0HYpmeCzTjZ-5SBosLgPWT0Dap30yBrtzNzx506GSGgBMgvuHhxT9iHnaDbSiZLpd3knC5cfQzoGUFOdAssmoPPLYlKOjpvz6z2FDUgTbbmaQog_8t67xGm_t7F5PF0SWpLtmTkrIww6sPG6sHaXYTz-V7xJxmRAyQwqsFDts6-bERjCMo7LBKDpqLfq4nke6oMi4wKJBDccYWcGICy9VUE5a6b1x4Z6oBCGO7rjU9uSPs9YE6vZB3E-6dC6LC8ToyfpAjCqaW872p-Ui0tAC_5ubTS_GG84wyiXes58jfNnBAeWywzijyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم بجنورد در هوای سرد، میدان را گرم نگه‌داشتند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/467816" target="_blank">📅 21:54 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467815">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c696c0995.mp4?token=aOoRewVIA-JW0xac2hQeJkTlzRRTRhaL_p2MK6se1xsGtwkaAiYbAlBfuZ5lrezUzHDN4yIbWXY4XdZpvxufzgisp_o-xZ9DelykHFuiH7cKaYrhOLvmRJnD-W4M1XAC_Pu0VkBi9ZjW8lcrn-TxVqR4ymuo_NGJ_9IpNc3jtlFxcBSGv5yTaC0o5yqbG2NVWRDhhy7jKCsQxOYxIX2b1GitSYrVzTUyz_2rEo8PKdXH1tPLUX2MUnGWTERpDfo46E-PMO5ZBsmqJ5GVpv2rulPObkPZc7SeO69tImUIdfaZRaL7fB-JuBeJhP8uNqzGJ2kXvil44tOIFW6tJA72Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c696c0995.mp4?token=aOoRewVIA-JW0xac2hQeJkTlzRRTRhaL_p2MK6se1xsGtwkaAiYbAlBfuZ5lrezUzHDN4yIbWXY4XdZpvxufzgisp_o-xZ9DelykHFuiH7cKaYrhOLvmRJnD-W4M1XAC_Pu0VkBi9ZjW8lcrn-TxVqR4ymuo_NGJ_9IpNc3jtlFxcBSGv5yTaC0o5yqbG2NVWRDhhy7jKCsQxOYxIX2b1GitSYrVzTUyz_2rEo8PKdXH1tPLUX2MUnGWTERpDfo46E-PMO5ZBsmqJ5GVpv2rulPObkPZc7SeO69tImUIdfaZRaL7fB-JuBeJhP8uNqzGJ2kXvil44tOIFW6tJA72Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرا مراکز خصوصی زیر بار تعهد قانونی برای درمان ناباروری نمی‌روند؟
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/467815" target="_blank">📅 21:51 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467812">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d6-EwUqZY81aZPUk8prEdvJ128e8p0NcRALTWSzf6MbJLeYeJDgTtMUgI5c5ZomaDrdK0z8gnQMtoOsqkMvkrsvzX1RBMr6fmIIqcKlAsUwNWiHLy6yKqQmrCTkM02eo-eMulYRtT2xcgd2NyuWJW02aV8wpXZLii05RiUWJnT5UsuELE77R-Rs2xEjowkDlLAbBiA2BiijtFbl-mTljDehnbLnj1ReFDfOZJgHpUg2pcX5q3FeHuP6n5fI2KSFZMU45kj54DDewtGPMO8CeWRevTlDqATtinoNAOSjhcUvv_40r4-Gky-GoPzJixzmY678yUkT4vkuCWyU4jLEO-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r-LJ_F6bQuFeOrmTbsG2ovbuWKeyxJEYacVGBx9KAhzhnNODbNAkSn3hTE9o8PuwVUsFG24jPvXcEUm4QVr721cn1awS6s1rmDmDxoqbitPV516L1KXWX2UUZzZMMjSVGFQhtcfvX4v38SiSnQhlY5AkRchQ6l_PN-6GC7mnHNb1NcfrtFSc8Q_XuKfFAebK1XHNhRv7eMYRmrIrZtd9LnWi1cQBM6dZnkwP3-FeMGzbz7tHzdQVpUeNWu-IL8m-DewruzUFkHOxH1BbQak16S5-lEtpCC0MHDA0vjYAvrKlMpc_XzwZu8mYwmCVtMM2VVZT1E-H_5Vt4tY6ilX7Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dEeSZD1et-m0YXJNYE-qDY3BHAbYGbKeZlQVYujSP5Gh0gkc55GBSNkcJSx3_AvS-E-gWBZPUA1pJxvfd8N8AAvlzTcan4s7GsHgmdmFeWKguW5txcBdBl6Zlt3kiZNH50JU7q6LUs7ZrO6w9JistM73IMsgz8BqDoWJPsm2757jfdnae2c5tWOXCJFwYWSR47VWMbFttmOIWn5Fd2rXiFVYAUf7XKd2xosZOQn4pH5Nh-o52qZoahnNPGV3ZuASim4xie4xgFFKd6oB5LPaDbWRE2H9V7hr5g1slnY9zU1KT1vNGYYo78_NKoUBMc0J-5Oj6684DbeJgs9EKqor3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
اخبار امیدآفرین ۲۴ ساعت گذشته را یک‌جا بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/467812" target="_blank">📅 21:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467811">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVmEPLAzO7sWpYM_K3mpJeSaAz6xjQmuCGHl9DmSnB3AbrUVPzt0sRLB8j3Vb-l3l6AuTukzGzgDRcNrvEWhkaGA1zkpUWrIagTf4wGwNCyjIqYX8tyZarCECXQzkLrVf2v2gz_l44swHdxSV7GqsziKqfeOUcHjJTsYZapjZ1o8didaFn9hU8qjnxFI9jwExRUmB3ESjBE8hyyJ3L_iPjLsZzhnnJ1ic2TcU0SAsmkFFgmMcgxaKeRXaiyO6dTZE6fQRFSJobI1QBB0ZAHAw9nv7Qc7e_HplxlMgtzEFO8FRFhnjl_3vgP7Vz2w5ULOJB4CiPeJiKzxmRRraszDCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محافظی که از آغاز رهبری تا شهادت همراه آقای شهید ایران بود
🔹
شهید سیّدمجید طباطبائیان از مسئولان عالی‌رتبه‌ی تیم حفاظت رهبر شهید انقلاب بود که از سال ۱۳۶۸ عمر خود را در مسیر رازداری، فداکاری و خدمت به رهبر شهید انقلاب گذراند و سرانجام در نهم اسفندماه ۱۴۰۴ در دفتر رهبری و همراه با ایشان به شهادت رسید.
🔹
خانوادۀ او روایت می‌کند که «با اینکه خیلی‌ها اصرار داشتند که ایشان بازنشسته شود و استراحت کند، امّا پدر انگار تا آخرین نفَس، تنها یک خواسته داشت: ماندن در کنار آقا. برای پدر، بعد از امام زمان عج، مهم‌ترین نقطه و اوج زندگی دقیقاً همان جایی بود که در کنار رهبر حضور داشت.
🔹
او با تمام وجود کار می‌کرد و ما با تمام ایمانمان باور داریم که همین تمامیّت حضور و همین کار کردن با تمام جان بود که ایشان را به سوی شهادت برد.»
🔹
شهید طباطبائیان برای دخترش تعریف کرده بود که آقای شهید به محافظان توصیه می‌کرد: «باید مراعات حال مردم را کرد؛ نباید مردم را اذیّت کرد و نباید با آنها برخورد تند داشت.»
🔹
همین نگاه ایشان بود که باعث می‌شد تیم حفاظت، فراتر از یک وظیفه‌ی امنیّتی، با یک منش اخلاقی رفتار کنند. این رعایت ظرافت‌ها حتّی در حسّاس‌ترین موقعیّت‌ها نیز دیده می‌شد.
🔹
برای مثال، وقتی قرار بود ایشان به خانه‌ی خانواده‌های شهدا سر بزنند، اصرار داشتند که کوچک‌ترین برخوردی باعث ناراحتی نشود؛ حتّی در مورد شهدای اقلیّت‌ها هم همین‌طور بود؛ آقا تأکید می‌کردند که وقتی میوه یا شیرینی‌ گذاشته می‌شود، حتماً میل شود و همه با میل و رغبت بخورند.
@Farsna</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/467811" target="_blank">📅 21:47 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467810">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o1Fxhy96X7VYsXN1b1YvV501p9ae64nML0aJoikLKrR9uPsMnbAeG6QcqRIWJIDNfMnVtsdLhegKSk-e7xXMUAxb_kikBuZurUj1oVU5zrQjh71mSKSQjY4mF7YN_ROFm1jtVSBQvTgl7OiGZyGpYZ3piGbeUY1zW5Ui-aNDvi8E500iEbIM3MtkXL6XEgV9u6VMAhB9kImDGId0AE9-Ez14Ogy2NyMU6xA8dBsNJwdFs8G06eH8x5kxWK1lQR_6ip3UHT_ecmz-5LPXbj6kx4bEdZUa7k0SQqOUo5LXbUS5zRqcrYeMWk1xNar-t3fzEpbdy7tL580p0cub-mXkqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همتی: وعدۀ ۲ هفته‌ای بسنت تمام شد؛ اقتصاد ایران فرو نپاشید
🔹
رئیس بانک مرکزی: امروز آخرین روز مهلت دوهفته‌ای بود که وزیر خزانه‌داری آمریکا برای فروپاشی اقتصاد ایران وعده داده بود؛ اما به‌جای پاسخ‌گویی درباره نتیجه این وعده، دوباره از چاپ پول در ایران سخن گفته است.
🔹
واقعیت‌های اقتصادی را باید با شاخص‌های قابل‌اندازه‌گیری سنجید، نه مواضع سیاسی.
🔹
رشد نقدینگی در شهریور به کمترین میزان خود، یعنی ۱.۳ درصد، رسید و با مداخله بانک مرکزی در بازار ارز، روند افزایشی نرخ ارز متوقف شد و حتی کاهش یافت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/467810" target="_blank">📅 21:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467809">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDCdJE3Vrg_jMVASi-e9GYHVuuHAFOE-19MdfwMUbMPFnzHoOi9io0ylGo6rQERUBR9kNlpuMizqyOAXA_mJfZseqI-MqBZR8yCwL9R7jzduqUUo61X8XmQrCBAM1daF2Tb-_yUHP5cw-x0eyVCwskllJryYFD_hF-NQI_qWq3gpNhqRQcB0aN7TqtW8AQo97FaNom6Q8RnQTanrFAOutPr0RAsHvQj7BveiZAzuNWh3gGdn56Ly_8JC3BorOdsYvbP8akqwir4YqiagO36_ozlvaL8wEXJGrjNXxDNEOjzYWfKdfwLRRiA_isJTGJ-lI3u_rDkYAxQVqUroEqyWwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلنسکی در جریان آتش‌بس انرژی ترامپ نیست!
🔹
الجزیره: «زلنسکی در گفت‌و‌گویی جدید گفته: خبر آتش‌بس انرژی برای من تازگی داشت؛ اگر ترامپ دراین‌باره با پوتین مذاکره کرده، لطفاً به ما بگویید که این آتش‌بس چه زمانی آغاز می‌شود.» @Farsna</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/467809" target="_blank">📅 21:27 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467807">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af4e4aef18.mp4?token=jPLY_uc5z6GEPpke-drF58J2lHDLA67qpv1xQSbDrttEUSOX2BGgWshn5sobQjE3jzeRuoKhrFjXnQ2w9hXOV0mj4JFFOxQlbWD_bARoP0hyqMk2STf_7Jy8tMLm1NaiHFMOf3Q1SMtllxATdGCSQHDYgppOuwqKtcVmczpBkhj3UBuYycqfoUcSglL1-3PcfV15Gcq4fQRqHfWE5KwMC7bZr3X3NLhVGyhPQtbG1pqaHtztyzL5tvQumOnwJ5khIuYFkIC5AddlQJId7epHPmM3CPa4ZWm_uM2I6zetvOjgA3JPPY7xSmFrhXWX6-7iL8wvypI11D3_lZo70sL3NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af4e4aef18.mp4?token=jPLY_uc5z6GEPpke-drF58J2lHDLA67qpv1xQSbDrttEUSOX2BGgWshn5sobQjE3jzeRuoKhrFjXnQ2w9hXOV0mj4JFFOxQlbWD_bARoP0hyqMk2STf_7Jy8tMLm1NaiHFMOf3Q1SMtllxATdGCSQHDYgppOuwqKtcVmczpBkhj3UBuYycqfoUcSglL1-3PcfV15Gcq4fQRqHfWE5KwMC7bZr3X3NLhVGyhPQtbG1pqaHtztyzL5tvQumOnwJ5khIuYFkIC5AddlQJId7epHPmM3CPa4ZWm_uM2I6zetvOjgA3JPPY7xSmFrhXWX6-7iL8wvypI11D3_lZo70sL3NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای تبادل یک جاسوس در دولت روحانی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/467807" target="_blank">📅 21:23 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467806">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d40bda8e91.mp4?token=L4nt3g4fEGOHGzjTkTvd9MihqjTxLAlVmEbwEdO6zK1JrzUqRXaa-ibi5L6wE7zSDpc3k32xv_esbHOahQ_rvYN5GahMSSeAo7kUDL46iwA4jGf5kdWN3pSkfSeYh2Q6XnRRx4HcuffFNZSrZzXXkCTw6kMOvDLahYncGLT9vyamChmtsPQqYL2OtJYE8dvYNgQ0s0rP-ww_0Ug5eS-QQvH93FwoDt5fIkH2U94cniXx8y1orYDF1fPxpG0ossCS5BAa8PY5LUPkVYnGMR6hzKAV5_57EtNyVPy5o8cnZmhYpYe0yw84Wj_GhKWBIdw-OX1l3XOvyN72RODyxJ__eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d40bda8e91.mp4?token=L4nt3g4fEGOHGzjTkTvd9MihqjTxLAlVmEbwEdO6zK1JrzUqRXaa-ibi5L6wE7zSDpc3k32xv_esbHOahQ_rvYN5GahMSSeAo7kUDL46iwA4jGf5kdWN3pSkfSeYh2Q6XnRRx4HcuffFNZSrZzXXkCTw6kMOvDLahYncGLT9vyamChmtsPQqYL2OtJYE8dvYNgQ0s0rP-ww_0Ug5eS-QQvH93FwoDt5fIkH2U94cniXx8y1orYDF1fPxpG0ossCS5BAa8PY5LUPkVYnGMR6hzKAV5_57EtNyVPy5o8cnZmhYpYe0yw84Wj_GhKWBIdw-OX1l3XOvyN72RODyxJ__eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرشایمر: ایران باید هرکاری از دستش برمی‌آید را انجام دهد تا به آمریکا و جهان فشار اقتصادی زیادی وارد کند
🔹
درگیری بین انصارالله و سعودی‌ها هم فشار اقتصادی زیادی به آمریکا وارد می‌کند. @Farsna</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/467806" target="_blank">📅 21:22 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467805">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">زلنسکی در جریان آتش‌بس انرژی ترامپ نیست!
🔹
الجزیره: «زلنسکی در گفت‌و‌گویی جدید گفته: خبر آتش‌بس انرژی برای من تازگی داشت؛ اگر ترامپ دراین‌باره با پوتین مذاکره کرده، لطفاً به ما بگویید که این آتش‌بس چه زمانی آغاز می‌شود.» @Farsna</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/farsna/467805" target="_blank">📅 21:19 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467804">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7fdbd4bef.mp4?token=vt9W53zFtDMZm3KVRZ48ZmOFzEHCgMPc7FpuFtEM_rMbdvDN7imP-ewuGh2dnTvtUmINwMoDfQkTtmRp_CfCc4SMQAbWpsP1P_xmm8A2mJX-cUrKR5zGVoQ78r2xw8rnvuhWgV9cFLxwg5RSNixeBsQzP3d1dagoUPFp_6dR2yz0nzHpAP2GA_rmwJs-xq1c_eCbmLSBRJdRg1MIZOdbPuj-6DoCVIsshw99K1oWpMK0_O_Zc-fw4ok1AMcmnPnS10qyuMcOcPKSzHh0obRvyQ12A7RnCvbA7yZRwjg6wr56m86xcKG8laaHUDjH8w34tnrJOv6iRB-ZvUyXt49HqQCsdlfNDrwjARWB8a_UhbSTouf1okQVKOjAcnilZVoua_rWSnXVZr2sI1BjBWFS_KpJKeHPFkVficSsJSw0mYvp0KaEgS5HVkJNyb2WVMhOKvunJswaoKJEthSUUop59XtuBYzU_WegEibLYa20nvLHA4xRTVhNcfaXbLPYOP3VC6PtFWtITthZro0VogeI5xnNzK_Ackzr0UA1lHjUBeflo5Eji1PVuA5UxL6RRFzXr0teeUdxi0GST44hJ7YaBwwDkbHaYUF88UFPmgNV86AgaWbnbMQdGYlabltKJuAoF2CqN-dtqse3m9mshPakrGDDwa8W_JzkTNT7fFNdrHI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7fdbd4bef.mp4?token=vt9W53zFtDMZm3KVRZ48ZmOFzEHCgMPc7FpuFtEM_rMbdvDN7imP-ewuGh2dnTvtUmINwMoDfQkTtmRp_CfCc4SMQAbWpsP1P_xmm8A2mJX-cUrKR5zGVoQ78r2xw8rnvuhWgV9cFLxwg5RSNixeBsQzP3d1dagoUPFp_6dR2yz0nzHpAP2GA_rmwJs-xq1c_eCbmLSBRJdRg1MIZOdbPuj-6DoCVIsshw99K1oWpMK0_O_Zc-fw4ok1AMcmnPnS10qyuMcOcPKSzHh0obRvyQ12A7RnCvbA7yZRwjg6wr56m86xcKG8laaHUDjH8w34tnrJOv6iRB-ZvUyXt49HqQCsdlfNDrwjARWB8a_UhbSTouf1okQVKOjAcnilZVoua_rWSnXVZr2sI1BjBWFS_KpJKeHPFkVficSsJSw0mYvp0KaEgS5HVkJNyb2WVMhOKvunJswaoKJEthSUUop59XtuBYzU_WegEibLYa20nvLHA4xRTVhNcfaXbLPYOP3VC6PtFWtITthZro0VogeI5xnNzK_Ackzr0UA1lHjUBeflo5Eji1PVuA5UxL6RRFzXr0teeUdxi0GST44hJ7YaBwwDkbHaYUF88UFPmgNV86AgaWbnbMQdGYlabltKJuAoF2CqN-dtqse3m9mshPakrGDDwa8W_JzkTNT7fFNdrHI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۵ خبری که حسابی در فضای مجازی سروصدا کردند؛ ماجرا چه بود؟
@Farsna</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/467804" target="_blank">📅 21:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467803">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca0414b153.mp4?token=t3xQheEUkHZDak0brZAGKroGTaw_187eJ3sK24oIcGnmnxlUWNhiNGinLLO2fpmyiucWDfZPPgR2KJERIXC7vge_Mh8mMzWOUMaj-3Es40AQbqt2PaokhHMZ9oBjK2f9A0oOq2Oi8DJ9SswS4pOQXSDKOXY9_QAqzEUn1104BCflD6qx0Cl81Bm-kdne2rVGeEKTINkJJVDiQS_RfdbnhT0igHxbnVWQSRDKb6X8xZcxX2BBv4cPFmjfs-iHYhS1mYSXnnIfxBuLhUmnoswioZOFYNP2dDKgT-qEYnjLvLAQSvzjUeVmxY82AxmTN0rhyMf5GXpXMGRs5opPPsePlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca0414b153.mp4?token=t3xQheEUkHZDak0brZAGKroGTaw_187eJ3sK24oIcGnmnxlUWNhiNGinLLO2fpmyiucWDfZPPgR2KJERIXC7vge_Mh8mMzWOUMaj-3Es40AQbqt2PaokhHMZ9oBjK2f9A0oOq2Oi8DJ9SswS4pOQXSDKOXY9_QAqzEUn1104BCflD6qx0Cl81Bm-kdne2rVGeEKTINkJJVDiQS_RfdbnhT0igHxbnVWQSRDKb6X8xZcxX2BBv4cPFmjfs-iHYhS1mYSXnnIfxBuLhUmnoswioZOFYNP2dDKgT-qEYnjLvLAQSvzjUeVmxY82AxmTN0rhyMf5GXpXMGRs5opPPsePlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرشایمر: آمریکا باید به این باور برسد که توافق‌نکردن با ایران پیامدهای اقتصادی سنگینی برایش خواهد داشت
🔹
آمریکا باید مجبور شود به اسرائیل فشار بیاورد تا به تعهداتش در تفاهم‌نامۀ احتمالی عمل کند. @Farsna</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/467803" target="_blank">📅 21:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467800">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
نیروی دریایی سپاه: دومین سوپر نفتکش با مین دریایی در تنگۀ هرمز برخورد کرد
🔹
روابط‌عمومی نیروی دریایی سپاه: یک فروند سوپر نفتکش متخلف با برخورد به  یک مین دریایی عصر امروز در محدودۀ جنوب تنگه هرمز دچار انفجار و آتش سوزی  در موتورخانه گردید.
🔹
این کشتی با…</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/467800" target="_blank">📅 20:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467799">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/399ef09449.mp4?token=uq0JSaHZygHj-_8peaV_uxPaXPK53bp9iHTaFtCJBOMkLyX2STmdEpMt2MVrvvLgduMq5ejEdEqOY5sskt3GNzPdAe3auoX89IxmpETHzarl4-VMeY9rpLKHZfN6MVKijd96VCijn1CbB8-4HluNdTt4TnIpdERpoGRDrxyIDjrTSYsuYfgrzB8PowRoi6KG2_jiBQ1SPzTeskWgrXzwD0CLxj-lcQUF3lvlDCBEey3MWdQxDqMZeBnra17wxueLlXgxBcu0e80hlcwQAT3A_jSwkqIDRwqsRs1tGUs9ehpHiQz5_AGTYuOpBCtiu3lsT5cMyZGmaDGBNC-TvfBPJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/399ef09449.mp4?token=uq0JSaHZygHj-_8peaV_uxPaXPK53bp9iHTaFtCJBOMkLyX2STmdEpMt2MVrvvLgduMq5ejEdEqOY5sskt3GNzPdAe3auoX89IxmpETHzarl4-VMeY9rpLKHZfN6MVKijd96VCijn1CbB8-4HluNdTt4TnIpdERpoGRDrxyIDjrTSYsuYfgrzB8PowRoi6KG2_jiBQ1SPzTeskWgrXzwD0CLxj-lcQUF3lvlDCBEey3MWdQxDqMZeBnra17wxueLlXgxBcu0e80hlcwQAT3A_jSwkqIDRwqsRs1tGUs9ehpHiQz5_AGTYuOpBCtiu3lsT5cMyZGmaDGBNC-TvfBPJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی سپاه: سوپرنفتکش متخلف در یک آتش عظیم درحال سوختن است
🔹
یک سوپرنفتکش حامل نفت خام که قصد داشت از مسیر غیرمجاز از تنگه هرمز خارج شود، پس از ورود به مسیر پرخطر اعلام‌شده و برخورد با «مین دریایی»، دچار انفجار شدید شده است.
🔹
این نفتکش با خاموش‌کردن…</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/467799" target="_blank">📅 20:58 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467798">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b3ea8efe6.mp4?token=DA6KSkOpq42mxRqjvdGiHm_B9CBoIMSUpdEI_oNsPNh2gsUafSHRuKV3XFcvbdFEQLZvVjh6SJTGdMWv-0lV_phtHqtQz_IX6cqVfpOoYJLilJbiOp-Dy7VeChYMHT2G0hxovEdGjSMTbtpmHYVyUmC3fg8wRWVISIgUf8QTQEdbE8Rd_1bqzU2qtIbIcHd96ueqzET4qV1uXAtbLeGztXW9YrT34MHAxm0jzQuswrErQEB4TfPnu13xPAnLU_pLxkhnpLQZmsAVT6qnRiNXMdgaY500Oj1WP21pfjuEBo01E3hYWSUvpiDd6yEncy9RBsYE6w9FtHUUYUqGwN1dGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b3ea8efe6.mp4?token=DA6KSkOpq42mxRqjvdGiHm_B9CBoIMSUpdEI_oNsPNh2gsUafSHRuKV3XFcvbdFEQLZvVjh6SJTGdMWv-0lV_phtHqtQz_IX6cqVfpOoYJLilJbiOp-Dy7VeChYMHT2G0hxovEdGjSMTbtpmHYVyUmC3fg8wRWVISIgUf8QTQEdbE8Rd_1bqzU2qtIbIcHd96ueqzET4qV1uXAtbLeGztXW9YrT34MHAxm0jzQuswrErQEB4TfPnu13xPAnLU_pLxkhnpLQZmsAVT6qnRiNXMdgaY500Oj1WP21pfjuEBo01E3hYWSUvpiDd6yEncy9RBsYE6w9FtHUUYUqGwN1dGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم در میدان به یاوه‌گویی‌های مقامات آمریکایی‌ پاسخ دادند
@Farsna</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/farsna/467798" target="_blank">📅 20:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467797">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdd9c4b0eb.mp4?token=gSCUJX92Lm4sIUcKTvjCDj59_Pj3rZwdjSKf4L0Q8Py6ygTg7r9g1hYuxxjHOFxPksMvu78NzgH8zOuyoFHbPBOZNdgQhcuG69CO1b_VMvJYprAjPrJKwHKC7e_f9mB2Zsn503dIRhZB4AYRhmPd2R7FSeKT1UsiD2_p1BpxS1aCF0wrPFom2A2zGG26TJyhPRFrbxvkxULRoqED9me6pdY5zcnGP7DIQ6uUHBYISgtUPGduZbBY_TG8Ej3ncadojvNllP34fZmTW10HDYDL-sFyDYx8ACbJ9-8RoAepXOeY6Qaw-luF6Hb2S1pEKMSglmKS8NxQ6pkYw3FYV4INiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdd9c4b0eb.mp4?token=gSCUJX92Lm4sIUcKTvjCDj59_Pj3rZwdjSKf4L0Q8Py6ygTg7r9g1hYuxxjHOFxPksMvu78NzgH8zOuyoFHbPBOZNdgQhcuG69CO1b_VMvJYprAjPrJKwHKC7e_f9mB2Zsn503dIRhZB4AYRhmPd2R7FSeKT1UsiD2_p1BpxS1aCF0wrPFom2A2zGG26TJyhPRFrbxvkxULRoqED9me6pdY5zcnGP7DIQ6uUHBYISgtUPGduZbBY_TG8Ej3ncadojvNllP34fZmTW10HDYDL-sFyDYx8ACbJ9-8RoAepXOeY6Qaw-luF6Hb2S1pEKMSglmKS8NxQ6pkYw3FYV4INiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرشایمر: فعال‌کردن مسیر عمانی در تنگۀ هرمز اولین مسئله‌ای بود که نشان داد تفاهم‌نامه دارد از هم می‌پاشد.  @Farsna</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/467797" target="_blank">📅 20:54 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467796">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bebfe86521.mp4?token=O60X0twTC5yCGtewybgnJA5qOznwGkU1U6apfSCv90FlPwJuIKSfYzd3Ofo_si05O59MbpfK0mWfXcFqTq8GQPJPnDgWA0_Hjnb_zmPyvFCLMdwUfcWguFtxqSHhIQ5ODtJGUHACzeJwJ-y_uFiZ2mdSxwbt1eGYm3DXEAp11X69WXHb1bGKaH88x9XkwoLvTYerhfVQFsYfjsZ_1MDiYKpfTzKWlZ2bI-VINW5ax7QZz6Hvl4TgqpBKkZJiEd4F2FKN44d7zFR2sko2KTwMGQK9pFtl0YcHb4qTwW8prbvpBrl3WdzM06fE36jmH_44-lNAjtje-05zGKf-R_TcKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bebfe86521.mp4?token=O60X0twTC5yCGtewybgnJA5qOznwGkU1U6apfSCv90FlPwJuIKSfYzd3Ofo_si05O59MbpfK0mWfXcFqTq8GQPJPnDgWA0_Hjnb_zmPyvFCLMdwUfcWguFtxqSHhIQ5ODtJGUHACzeJwJ-y_uFiZ2mdSxwbt1eGYm3DXEAp11X69WXHb1bGKaH88x9XkwoLvTYerhfVQFsYfjsZ_1MDiYKpfTzKWlZ2bI-VINW5ax7QZz6Hvl4TgqpBKkZJiEd4F2FKN44d7zFR2sko2KTwMGQK9pFtl0YcHb4qTwW8prbvpBrl3WdzM06fE36jmH_44-lNAjtje-05zGKf-R_TcKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرشایمر: اگر ایرانی‌ها مصمم باشند که به‌نظرم هستند، باید راهی پیداکنند که آمریکا برای توافق احتمالی وادار شود اسرائیل را مجبور به خروج از جنوب لبنان کند.  @Farsna</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/farsna/467796" target="_blank">📅 20:51 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467795">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2a086e117.mp4?token=MjuP1Xi9Q3I8FEKS_e3ES0Z7qYHNnXujPKJS6Rw3HCyFyo7fTAEiXqOr6H5SwWv_dJkrIrIJy3_hL0b-N4zodlwmlqIovlRf8iQ1Tq9b3YC2AMLh_4iBsskXSYP3d-LITjV4I35Eav8irfJ5HGzwws0a60rx0iHZC8smq0NfIWkqxZmxMRWkFMLA0k0fyC_i-tZzKFy5POyhtM5fC-hx8SwQVKnhF9ZKfZpF1krQN2ao1pAUi7bQQl3u18-QmJfRrw5NctfMkNbctKL0M9_4QIT4XUvCdSn2tHDCcsBOkMPQ_dV8n7LD368LRca8q9h4_W9fTBqk3yDoeNlLaKc8iTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2a086e117.mp4?token=MjuP1Xi9Q3I8FEKS_e3ES0Z7qYHNnXujPKJS6Rw3HCyFyo7fTAEiXqOr6H5SwWv_dJkrIrIJy3_hL0b-N4zodlwmlqIovlRf8iQ1Tq9b3YC2AMLh_4iBsskXSYP3d-LITjV4I35Eav8irfJ5HGzwws0a60rx0iHZC8smq0NfIWkqxZmxMRWkFMLA0k0fyC_i-tZzKFy5POyhtM5fC-hx8SwQVKnhF9ZKfZpF1krQN2ao1pAUi7bQQl3u18-QmJfRrw5NctfMkNbctKL0M9_4QIT4XUvCdSn2tHDCcsBOkMPQ_dV8n7LD368LRca8q9h4_W9fTBqk3yDoeNlLaKc8iTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرشایمر: بعید می‌دانم اسرائیل بتواند به‌تنهایی به ایران حمله کند و پیروز شود؛ چون ضربات سنگینی از ایران خواهد خورد
🔹
اسرائیل با کمک آمریکا هم نتوانست در جنگ با ایران پیروز شود، چطور به‌تنهایی می‌تواند چنین کاری کند؟ @Farsna</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/467795" target="_blank">📅 20:49 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467794">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0662c3fbe.mp4?token=lDEL7NsIoat1JBOBvD441nXf2toJV1r6iKT-6vnq0iXiMPiAg_4PyJX4ExixXpFTG0Agg4xGV2BI0kQzDN770F7Ei_NEa4h8TrZBbCovYIlfFhm9UVihVavcGSHIrURR2vYp8VQMfXRAp4bXGe9yRxdRBkDvuZi1eOWMrOwq7oDor7tIicL8V95makoiSIpdbiW6OeVohQl6KWurJpP2EBE6bWjhkZAhRbvthWTxJdyRXhOrlIziEZ_aWR1uZIT6HFLSl2kbdPXyw1OWgGFaJaZbu9lN_E6cdrmDJ2_acNLxiwp8yEO9poKFE44eWdebcwdVCd_ca3-xVoEjv59f_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0662c3fbe.mp4?token=lDEL7NsIoat1JBOBvD441nXf2toJV1r6iKT-6vnq0iXiMPiAg_4PyJX4ExixXpFTG0Agg4xGV2BI0kQzDN770F7Ei_NEa4h8TrZBbCovYIlfFhm9UVihVavcGSHIrURR2vYp8VQMfXRAp4bXGe9yRxdRBkDvuZi1eOWMrOwq7oDor7tIicL8V95makoiSIpdbiW6OeVohQl6KWurJpP2EBE6bWjhkZAhRbvthWTxJdyRXhOrlIziEZ_aWR1uZIT6HFLSl2kbdPXyw1OWgGFaJaZbu9lN_E6cdrmDJ2_acNLxiwp8yEO9poKFE44eWdebcwdVCd_ca3-xVoEjv59f_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرشایمر، نظریه‌پرداز نورئالیسم تهاجمی: پیامدهای اقتصادی ادامۀ جنگ با ایران فاجعه‌بار خواهد شد
🔹
وضعیت اقتصاد جهانی و اقتصاد آمریکا وارد محدودۀ خطر شده است. باید دید آیا آمریکا آن‌قدر تحت فشار قرار می‌گیرد تا مجبور به توافقی به‌نفع ایران شود یا نه. @Farsna</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/467794" target="_blank">📅 20:40 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467791">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nhOb41KT-Gx7k1in-EyPH7714ujNFUe1eSm5goL3nyK3pNHSGzQtJhsq5sivCZ5ZhiGDaXN0NCCYtoammkVGn7vK1sgc2XaKkfwFI1TkBLO7xgIsUIUQwPLCOpvzanK67JsQ-pWKW2A4u0lThXI66USpQpPkk8g7dEUTBe0PcX5qfSHY8Qb1jjPtw1UA9pW467N9QW9JvG8PV03nK4lsYfSocgRxUQo6UXLGiOjo4yWs-Ov3df-tFPqCf79ONrIq9MOE7g-jcjNNjXmYVB0vVN50TGwQ8lTMCOXPNv3x6xzF-cQ1zPeaARUj5rsRUTdo56k1561Mn5eX23ASbUj_vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y2vS9PymB8vCAuaRkMbN6kyFXzJvd1uOZjkexo5KT1Wwpjhnre8XxNCTjpGWKyxco25jYCkLbEFm7l0AUgSpCuTJMn-Vz2JvlnybxZkfGeqhxCjj0UYBMraFMD3Lmd1rnoeFYfr9oLpZ5agDUdAy7b9hFDgOc6Z5jHywcfUaroKxgoguS9me1jzY_tulqbj266OZkS_JBWqSszJshI2rB0LSIl8x58zULwn_OOzLSPYOeidjZK7JZrALi7_xG6Jcg3fVsopI_5Hk5EBePSeramMfeixFGOPqCrI1yBjxkXCkoU_4NyOtZNt-QTd7xGtMgGQC6xlTRoSAVlh0a4183w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bckcV9I6skuq2lVuPaWBnDUOnS1AIvXy_rxv9KOKw_5OqHocdH7HhgvIT0VnVfwaOpg4ZpCDX7y3DdfBcqIINrGsB4u9Gq-QMpEANpYhLfJRCl_7Jd4yYK4Scn4AQFeuU4LI39Qym9wxh_vhhjVGzqbHjiPK9LqGmWRybYyBqPplrQeErJLKZaD2a9DH0BTUJY3KOAhB_1gGYw54fTmXno1Y1GBXajpe-LRHWIgzofsyvFmzgt17-9DCiAhdHZA1l6TwjdJjCr_2vSqtuhICGfl0odNNb0yn2ZXbJ8mDva0EZzN9d1RNgYrMVCY5vAhnBe0fVn0Pb4y2u3unrEfvfw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عراقچی: مسئولیت واقعی ما ثبت حقیقت و پاسخ‌گو کردن عاملان و آمران جنایت میناب است
🔹
وزیر خارجه که امروز نامه‌ای از فاطمه‌زهرا شیخ‌آبادی، دانش‌آموز بازماندۀ مدرسۀ میناب را دریافت کرده دراین‌باره نوشت: نام کودکان میناب و لامرد نباید تنها در خاطره‌ها زنده بماند؛ این نام‌ها باید در مسیر دادخواهی نیز ماندگار شوند.
🔹
وظیفه خود می‌دانم صدای فاطمه‌زهرا و روایت کودکان میناب را به مجامع بین‌المللی برسانم و اجازه ندهم گذر زمان، حقیقت این فاجعه و ضرورت پاسخ‌گویی در قبال آن را به حاشیه براند.
@Farsna</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/farsna/467791" target="_blank">📅 20:39 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467790">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSwv3-XA0X_I6TlxgTZ1zFJk1CnyG6-MDkksYYv9bu89Vu6Hsr4hr1plOwTJrT2X_v2cB9mY-TyNmcc44D0A4ZKGPNOw-4DTv_-ztDIni4erCX7em7cL8gaITxjAfyBD0nWzLaojwajjb2jONXV8Y9Bp0gitFOEOuFq5_s8gJQIxGr4QueTGFWr_d2kFPCCBJ6z4ivHnClFSXMEeKCRItIZtNnS6_HG1BSE6pI5yeLMJYFtdxCPD6r4sm_5di6KMLgZ-2M8_eR5nA9W0WB7r2m4iiA31yC_OyavH6xu6oiypViNXy660TYCPpYNZXOAQ3I0PCrBy025v9nNJhh50uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان: مسافران با اتوبوس از دبی به ریاض بیایند
🔹
کنسولگری عربستان در دبی: مسافرانی که به علت بسته‌شدن فرودگاه ملک خالد در دبی معطل مانده‌اند، با اتوبوس به ریاض سفر کنند.
@Farsna</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/farsna/467790" target="_blank">📅 20:35 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467789">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a5a9100aa.mp4?token=o9cbu8Fd0vp3K5_KclqBJOkY2URjQNCRFroqAKxNzk3mW16OBTbeU35rZN0uD_Adz2saB5oIlRYGw0RLlM39gIgOraM0b40oqfycY3iRhnJDLhwrcQEFEl8INP3XNWTO149e2V-TsEIDWQfJIMj9hJCW7vfJek58Oofnl3N9y2nXZg5-ljGWMX4t2QawIEJkhy6c1vpsg7zgjekbN4sCV1UJlw0D2k4dezao6OHk81tVykgkbx55FFfqMrmXx9bCTZo5hCCsUh-uF4tQy9I7EGZL9VLyL7eTjSFFNSHC6frN00zUspKTDgHCKgKriMxeNgojb1Fs8AKnzBYgbVwneQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a5a9100aa.mp4?token=o9cbu8Fd0vp3K5_KclqBJOkY2URjQNCRFroqAKxNzk3mW16OBTbeU35rZN0uD_Adz2saB5oIlRYGw0RLlM39gIgOraM0b40oqfycY3iRhnJDLhwrcQEFEl8INP3XNWTO149e2V-TsEIDWQfJIMj9hJCW7vfJek58Oofnl3N9y2nXZg5-ljGWMX4t2QawIEJkhy6c1vpsg7zgjekbN4sCV1UJlw0D2k4dezao6OHk81tVykgkbx55FFfqMrmXx9bCTZo5hCCsUh-uF4tQy9I7EGZL9VLyL7eTjSFFNSHC6frN00zUspKTDgHCKgKriMxeNgojb1Fs8AKnzBYgbVwneQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرشایمر، نظریه‌پرداز مطرح آمریکایی: ترامپ وقتی فهمید هیچ گزینۀ نظامی در برابر ایران ندارد، تفاهم‌نامه را امضا کرد
🔹
اگر ایران می‌خواهد آمریکا را به امضای توافقی به نفع‌ ایران وادار کند باید به آمریکا و اقتصاد جهانی فشار زیادی بیاورد. @Farsna</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/467789" target="_blank">📅 20:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467788">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">مهلت انتخاب‌رشته کنکور تا ۲۰ مهر تمدید شد
🔹
سازمان سنجش: مهلت ویرایش و انتخاب رشته برای آزمون سراسری، دانشجو‌معلم و پذیرش صرفاً بر اساس سوابق تحصیلی، تا پایان روز دوشنبه ۲۰ مهر تمدید شد.
🔹
این مهلت به هیچ وجه تمدید نخواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/farsna/467788" target="_blank">📅 20:29 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467787">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19508bd484.mp4?token=ftXhOGSSg2lpxdSM2XyrbUwXOfEFABnE1pWNEu8Ri_ImUNOgfhJiKUi557aGIbKZyHOi2ywwHkED4BsopmjSpGNdr-WSH1pvDZeoMzoCffKigkCWI--bCeP6wd9MVyMNmtqP6MbsaMVJpsMA0s5LRO7DXdMOjh0PUS2IUCRxbYkAejoVWrlYp9q-eVN6oAMFclvb-ykXrepdFjyohNLD9XeG1-dBqNWgEVlmagAYPPth5JsilYhiHcHlh7ogoQPfkqSC7bFQ3n94prSDimcHMFsJAyMtV0ps2LKySpLaHFV5-5TQWX4Xm51AgPMnPvCyD6G0SDPnMtUAZNCekUnE6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19508bd484.mp4?token=ftXhOGSSg2lpxdSM2XyrbUwXOfEFABnE1pWNEu8Ri_ImUNOgfhJiKUi557aGIbKZyHOi2ywwHkED4BsopmjSpGNdr-WSH1pvDZeoMzoCffKigkCWI--bCeP6wd9MVyMNmtqP6MbsaMVJpsMA0s5LRO7DXdMOjh0PUS2IUCRxbYkAejoVWrlYp9q-eVN6oAMFclvb-ykXrepdFjyohNLD9XeG1-dBqNWgEVlmagAYPPth5JsilYhiHcHlh7ogoQPfkqSC7bFQ3n94prSDimcHMFsJAyMtV0ps2LKySpLaHFV5-5TQWX4Xm51AgPMnPvCyD6G0SDPnMtUAZNCekUnE6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرشایمر، نظریه‌پرداز مطرح آمریکایی: تنها چیزی که می‌تواند آمریکا را وادار کند که به خواسته‌های ایران تن دهد، فشاری است که می‌تواند آمریکا را مجبور به توافق کند.  @Farsna</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/farsna/467787" target="_blank">📅 20:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467786">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbd387f614.mp4?token=IbIKrJDwTz-SEO1AqIgBKsxWoTgtb3kFLwhEe9n80XI1LWcWUibSYxizz_mMSR_9AZoRaG9c-4W-667pbouH6teCxFuWA0ELybuykrpluQXafDwAI26w9rHhlofnYNFF1LnPE0SFPXZzvDegxMbyVlohlgAl3uXiGnJWyICy5DY_V3JfYOZG3iADSU9iKiW_ObfY4uvvT3SPDYAnaNng321TiCrXZ89EXdGaVIUfCqVJSAnbzPVMKOGpS57HO2K9xASzla2tyrrOSC1gm6itZ3FdU2XYxO5-l7YtxgfnPgR5ZvRY_r82ETLmBqiIkF1dwmeVPOzZnao7RVNEz77IlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbd387f614.mp4?token=IbIKrJDwTz-SEO1AqIgBKsxWoTgtb3kFLwhEe9n80XI1LWcWUibSYxizz_mMSR_9AZoRaG9c-4W-667pbouH6teCxFuWA0ELybuykrpluQXafDwAI26w9rHhlofnYNFF1LnPE0SFPXZzvDegxMbyVlohlgAl3uXiGnJWyICy5DY_V3JfYOZG3iADSU9iKiW_ObfY4uvvT3SPDYAnaNng321TiCrXZ89EXdGaVIUfCqVJSAnbzPVMKOGpS57HO2K9xASzla2tyrrOSC1gm6itZ3FdU2XYxO5-l7YtxgfnPgR5ZvRY_r82ETLmBqiIkF1dwmeVPOzZnao7RVNEz77IlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرشایمر، نظریه‌پرداز مطرح آمریکایی: کلید موفقیت ایران این است که فشار اقتصادی زیادی به آمریکا وارد کند
🔹
این فشار آمریکا را باید وادار کند که به توافقی تن بدهد که از نظر ایران مطلوب است. @Farsna</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/farsna/467786" target="_blank">📅 20:23 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467785">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfebfb5d38.mp4?token=nR2Yjsg1xq2oB2ZDMdJkSLpJAAU5xbmzJ4VuqgH0JOzBqg-oDv2BitnkgEHDpsyavUnp_qMtx0GD9BRmDh3NQWfQmQ9kM_kKXV5xVSqlEJ0BWepRu-S5PnE1NMHO_G6UwadBKteTu538a1J7fDW8zczRtJVf5VAb43EetE4UVMv8ottPIZj0GLsAKxG_oSjeHePJCEts18D5bxoc1YfsKx0MW0slPfdxna7Ums58AfIkRxDZuBQotS2YFDF5BZdgufm3Go2wnz-kqlGV9dlUSJ2nkW10nRi5kMdpLvT9LeJyYNht3501D2MvnX_U6HupPdiDrB_YlfAqgA2FZQflOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfebfb5d38.mp4?token=nR2Yjsg1xq2oB2ZDMdJkSLpJAAU5xbmzJ4VuqgH0JOzBqg-oDv2BitnkgEHDpsyavUnp_qMtx0GD9BRmDh3NQWfQmQ9kM_kKXV5xVSqlEJ0BWepRu-S5PnE1NMHO_G6UwadBKteTu538a1J7fDW8zczRtJVf5VAb43EetE4UVMv8ottPIZj0GLsAKxG_oSjeHePJCEts18D5bxoc1YfsKx0MW0slPfdxna7Ums58AfIkRxDZuBQotS2YFDF5BZdgufm3Go2wnz-kqlGV9dlUSJ2nkW10nRi5kMdpLvT9LeJyYNht3501D2MvnX_U6HupPdiDrB_YlfAqgA2FZQflOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرشایمر، نظریه‌پرداز مطرح آمریکایی: کلید موفقیت ایران این است که فشار اقتصادی زیادی به آمریکا وارد کند
🔹
این فشار آمریکا را باید وادار کند که به توافقی تن بدهد که از نظر ایران مطلوب است.
@Farsna</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farsna/467785" target="_blank">📅 20:21 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467784">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ورود مجلس به موضوع به‌کارگیری مدیران بازنشسته
مهرداد لاهوتی، عضو کمیسیون برنامه و بودجه مجلس، با اشاره به موضوع به‌کارگیری مدیران بازنشسته در دستگاه‌های اجرایی، اظهار کرد: موضوع استفاده از مدیران بازنشسته، از جمله در سازمان بورس، محل بحث و چالش است و انتظار می‌رود دولت در چینش مدیران خود به ظرفیت نیروهای جوان و توانمند توجه بیشتری داشته باشد.
وی با تأکید بر ضرورت رعایت قانون ممنوعیت به‌کارگیری بازنشستگان افزود: مدیران بازنشسته باید در چارچوب قانون جای خود را به نیروهای جوان، باانگیزه و توانمند بدهند تا زمینه استفاده از ظرفیت نسل جدید مدیران در دستگاه‌های اجرایی فراهم شود.
عضو کمیسیون برنامه و بودجه مجلس تصریح کرد: انتظار داریم رئیس‌جمهور و معاون اول ایشان در انتخاب و انتصاب مدیران دستگاه‌های اجرایی، از نیروهای جوان و باانگیزه استفاده کنند و این موضوع را در تصمیم‌گیری‌های مدیریتی مورد توجه قرار دهند.
@Farsna</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/farsna/467784" target="_blank">📅 20:21 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467783">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUTq-r_C4RNCr5wxVAbZBJ4mTp6_1aolyc0RxXHx0HbnSD45r2GGudMpVfQmrzQ6kaFYhChGmNED_0s9_hNXgHDzKZkgzJGOqJcJw3kQGEb-tmFlU00LxRr7QparPuvpQSUxG3lec133ZNzMyFGDfftSdUxhLtDQ3MqRUEIryD5EKsUjdq9okh8E-ZiY0XkywbZ9mz1MZCP7apn2cTxzjmV-OMgguuBEYVCDQE4AU3xarjq7kIp00GDK_9EvSOx9dHQYEXWXI94XiIzf6qbf8gPw-V0c4V7HegIcdrggg2-UNayuOig9KaBy7Olvon3YOMY4aES4PQTka5o39MxESw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❇️
سالن مبله برای ختم
❇️
❇️
همایش های آموزشی
❇️
🔹
۷۰۰ صندلی
🔸
پارکینگ وسیع
🔹
تهیه بسته پذیرایی
🔸
هماهنگی واعظ و مداح
🔹
گل مصنوعی به نفع خیریه
🔸
سرو ناهار و شام در سالن
🔹
فیلمبرداری مراسم و صوت با کیفیت
🔸
دسترسی آسان به بزرگراه
شهید همت، شهید حکیم، شهید فهمیده(کرج)
📲
۰۹۱۰۲۲۷۷۱۹۹
☎️
۰۲۱۴۴۰۰۴۰۴۰
📣
امکان رزرو شبستان مسجد
📌
آدرس مسجد
🔻
فلکه دوم صادقیه،بزرگراه شهید اشرفی اصفهانی ره ، جنب بوستان صبا
🔸
مسجدجامع‌امام‌سجاد(علیه السلام)</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/farsna/467783" target="_blank">📅 20:20 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467782">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/farsna/467782" target="_blank">📅 20:20 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467781">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/137513140f.mp4?token=OM-uENZTQtLiuDpzG6RXWoQh47nYGNEmfeSC-YHM_1c6Rgq2-vDgSxRAQ6sSS3gteWlfOtN2tz_9MLLGFp15YH8xmaGo09CtapxNIj4dZQGXuAmkBzZoOXEnPl7tgsk4MviKBj8lzIcKxsea5_cTPsxicKk_NisOrSkIzbHQxC-uUzYV3GyNnTw0f0a5tEQSQ2M1j8EoI6SM_56SSxhTH0EOS4nMrg1-I27b2Cc4Dz5vYvtJlGysRICMlJpYIaw6BHG6ggNbZbyRviD4BU7JEbEJKXmhFTJ-JPcuze7yjEc5W3w0FhmuIj3mIOXuhLxNAwCXm8CnAhFRsNfPg1y0hprcb1q02TsbMGNklRP55bUJORZwaHtP-D043gib4srpIk2x4tEXUrnwRpL4qrv_yP1A5dyUEmtsWZMkmDmMUBc14_YV8TK5aVPwMSNkUHkPocoxhfxd_D9qeOTEOSh7B3VFe6zjwXTXFKJ07b1c7zeBOL44l5GuVEPxEw0MohEd5RsLH-YvkTS84mLn9plwK8cb-ht7qYfQjKPzXVufISv7ukvy356fw8gXcuC4ajtoYkjpTjwYX4O783gGpqx9kvjG5S3cvFKCX1RZFH6KFh8OKpjE_VYwF3LSpIknjDtyd2K4S8WpYqv35sL2sJfexV1__1mqjXp1tZunYIoy0Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/137513140f.mp4?token=OM-uENZTQtLiuDpzG6RXWoQh47nYGNEmfeSC-YHM_1c6Rgq2-vDgSxRAQ6sSS3gteWlfOtN2tz_9MLLGFp15YH8xmaGo09CtapxNIj4dZQGXuAmkBzZoOXEnPl7tgsk4MviKBj8lzIcKxsea5_cTPsxicKk_NisOrSkIzbHQxC-uUzYV3GyNnTw0f0a5tEQSQ2M1j8EoI6SM_56SSxhTH0EOS4nMrg1-I27b2Cc4Dz5vYvtJlGysRICMlJpYIaw6BHG6ggNbZbyRviD4BU7JEbEJKXmhFTJ-JPcuze7yjEc5W3w0FhmuIj3mIOXuhLxNAwCXm8CnAhFRsNfPg1y0hprcb1q02TsbMGNklRP55bUJORZwaHtP-D043gib4srpIk2x4tEXUrnwRpL4qrv_yP1A5dyUEmtsWZMkmDmMUBc14_YV8TK5aVPwMSNkUHkPocoxhfxd_D9qeOTEOSh7B3VFe6zjwXTXFKJ07b1c7zeBOL44l5GuVEPxEw0MohEd5RsLH-YvkTS84mLn9plwK8cb-ht7qYfQjKPzXVufISv7ukvy356fw8gXcuC4ajtoYkjpTjwYX4O783gGpqx9kvjG5S3cvFKCX1RZFH6KFh8OKpjE_VYwF3LSpIknjDtyd2K4S8WpYqv35sL2sJfexV1__1mqjXp1tZunYIoy0Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تلاش برای بازگشایی مسیر روستاهای شرق گلستان پس‌از سیلاب
🔹
با وقوع سیلاب در شرق استان گلستان و انسداد راه‌های ارتباطی برخی روستاها، نیروهای امدادی در مناطق آسیب‌دیده حضور یافتند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/farsna/467781" target="_blank">📅 20:06 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467780">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdBSlUvkEYp3ZZkoA8893gF1yH8hfisXrwZL9JvUoDlQHEmnFJaZ2mJb7BbU0wI249Zm9IXNBxDWhsx4qK-8aA2sKPG_khhzr_1jwvjqJvUM2ybti_bNh74NbSumUpAMKytRyP2VcMLOiHXgTclJDsxikJmRVD6YOYXZDgp5WIIcXfjz99bj2QxD97zEpzXJbe4QPU0W0DoRKhGR7xWTgKta9-IuABp3Pu23LprDmbphY7SEyQ2-kDZI0V0O7cGslIK6lkiktffUporcID1Klu-RELM2KLVT5QBPCurSSnptbigW8yOchwndYck-VgTofmpybT7umT1cYPrfiZ3gZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنگهٔ هرمز یا وابستگی مالی به آمریکا؛ دلیل گرانی عراق چیست؟
🔹
بازار ارز عراق پس از تصمیم دولت برای کاهش ارزش دینار همچنان ملتهب است و آثار این تصمیم حالا بیش از هر چیز در قیمت کالاها و قدرت خرید مردم خود را نشان می‌دهد.
🔹
پس از حدود ۳ سال ثبات نرخ رسمی ارز در عراق، دولت این کشور نرخ دلار را از حدود ۱۳۲۰ به ۱۵۲۰ دینار افزایش داد؛ تغییری که ارزش رسمی دینار در برابر دلار را حدود ۱۴.۵ درصد کاهش می‌دهد و اکنون آثار آن در بازار و قیمت کالاها در حال نمایان شدن است.
🔹
گزارش‌های میدانی پیش از کاهش ارزش دینار نیز از افزایش قیمت کالاهای وارداتی حکایت داشت. برخی فروشندگان عراقی گفته‌اند قیمت کالاهای وارداتی در ماه‌های اخیر به دلیل افزایش هزینه حمل‌ونقل و اختلال در زنجیره تأمین بالا رفته و در برخی موارد افزایش قیمت کالاهای وارداتی به ۲۵ تا ۳۰ درصد رسیده است.
🔸
اکنون کاهش ارزش دینار فشار تازه‌ای به این روند وارد کرده است؛ بنابراین خانواری که درآمدش به دینار است، برای خرید کالایی که قیمت آن به دلار یا بر مبنای هزینه واردات تعیین می‌شود، باید پول بیشتری بپردازد.
🖼
اما ماجرای این گرانی‌ها در عراق چیست؟
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/farsna/467780" target="_blank">📅 20:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467779">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJKIVEcAIgpSe6QhZ9l0k24AuZ8k5lSkbTxBROKMFjeJSpceoBtIOPgiTrjPnSSfOeNFqQHILpz4wBfsMz3-RBi-YKVz5eG21kp3n4t8l8IotoFWIk5sN-vmQ1hmWoJKXHmBEc8hMLwSRZ_8KDUGN_otxqIEAwluLripXBI5XTicKPen6vOW8W1Duqzw1yFFHEhTyAqqvkPAPY1S_ZJjXihAx7oifY7P_euh2dZ8LzIdrGmAOLahoSLsSsX-pNN24Dt6sMPtKZvugE9UJ3_dxfUT8P_tGRxUY93eG-u-p_t_j9GzOuvaN_rsX9ChEI7cJqEnsltZpKn_IzOAwyfcEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«پلتفرم یلا» با پول انگلیس جنگ روانی در عراق راه انداخت
🔹
کریدل: براساس اسنادی که به بیرون درز کرده است،  پلتفرم «یلّا» که ادعا می‌کند رسانه‌ای مستقل برای جوانان عراقی است، در قلب پروژه نفوذ پنهان انگلیس در عراق قرار داشته است.
🔹
«یلّا» یک پیام‌رسان نیست؛ بلکه یک رسانه خبری و شبکه اجتماعی است که مخاطب آن را دنبال می‌کند، نه اینکه با آن چت خصوصی کند.
🔹
یلّا خود را رسانه‌ای معرفی می‌کند که نه کسی به آن می‌گوید چه بنویسد و چه منتشر کند، و نه پولش را از جایی می‌گیرد که مجبور باشد حرف آن جایی را بزند.
🔹
پروندهٔ رسمی این پلتفرم هم می‌گوید «یلّا» با سایر رسانه‌های عراقی فرق دارد، چون به این یا آن گروه سیاسی وابسته نیست و از هیچ جناح خاصی دستور نمی‌گیرد.
🔹
اما اسناد درزکرده نشان می‌دهد این ادعا با واقعیت فاصله دارد؛ چون در سال مالی ۲۰۱۹–۲۰۲۰، ۴.۳ میلیون پوند و برای سال بعد ۴ میلیون پوند دیگر از سوی دولت انگلیس به این پلتفرم تزریق شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/farsna/467779" target="_blank">📅 19:54 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467777">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‌  سخنگوی نیروهای مسلح یمن: مزدوارن سعودی را وادار به فرار کردیم
🔹
یحیی سریع: نیروهای مسلح ما، یک عملیات پهپادی موشکی علیه تجمع‌های مزدوران سعودی در مناطق رأس العاره و السقیا انجام دادند که ده‌ها کشته و زخمی برجا گذاشت.
🔹
همچنین عملیات موشکی علیه یگان‌های…</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/farsna/467777" target="_blank">📅 19:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467776">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">۴ عملیات موفق یمن در چهارگوشۀ سعودی در یک روز
🔹
سخنگوی نیروهای مسلح یمن: در ۲۴ ساعت گذشته، ۴ عملیات مهم با موشک‌های بالستیک، کروز و پهپاد در خاک عربستان انجام شد:
🔹
فرودگاه بین‌المللی ملک خالد در ریاض را در ۳ مرحله هدف قرار دادیم که منجر به اختلال در پروازها…</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/467776" target="_blank">📅 19:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467775">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">۴ عملیات موفق یمن در چهارگوشۀ سعودی در یک روز
🔹
سخنگوی نیروهای مسلح یمن: در ۲۴ ساعت گذشته،
۴
عملیات مهم با موشک‌های بالستیک، کروز و پهپاد در خاک عربستان انجام شد:
🔹
فرودگاه بین‌المللی ملک خالد در ریاض را در ۳ مرحله هدف قرار دادیم که منجر به اختلال در پروازها و تعطیلی کامل فرودگاه شد.
🔹
ایستگاه پمپاژ گاز شرکت آرامکو در منطقۀ شرقی عربستان منفجر و دچار آتش‌سوزی گسترده شد.
🔹
پالایشگاه نفتی آرامکو را در شرق عربستان هدف قرار دادیم که منجر به آتش‌سوزی در آن شد.
🔹
فرودگاه بین‌المللی ملک فهد در دمام مورد اصابت مستقیم موشک قرار گرفت و درپی آن پروازهای این فرودگاه لغو شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/467775" target="_blank">📅 19:39 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467774">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‌
🔴
عربستان سعودی اصابت موشک و وقوع آتش‌سوزی در فرودگاه ملک خالد ریاض را تایید کرد. @Farsna</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/467774" target="_blank">📅 19:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467773">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORhDTC719iOzQ15Zx4pb6P0nZZs-KVGse5b8gpgRRbljvY1JglVFdK41pDheD5erNWCzc1u0klnAKcd22ynB-K3371m3Nlq14ko2i_P7zmBQtau0s7zt49wDuvBeMB2Ko_ka-GrjdB2ULxGI5V1G54qtuyQ8tOzo21XHKG3gKqddeasL1mpbBlLo8eVv10gowU5WlC_VT42bnZpemEcI5kaR8xuTXPdz8RMLwLlU_Itc818cd9FVOfoTYYAEntc8nCroJFN5cOiBLXT6IArDcqWaqcob_LzcMSkuYplSRiR1nvJHdaRRtHPFUveUhkCoZKFKhzMqM7LUm_8WRhk6Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روس‌اتم: واحد یک نیروگاه بوشهر با ۱۰۰ درصد ظرفیت فعالیت می‌کند
🔹
مدیرعامل شرکت روس‌اتم الکسی: در حال حاضر ۶۳ متخصص روس در نیروگاه اتمی بوشهر حضور دارند.
🔹
لیخاچف در بیانیه‌ای با اشاره به روند ساخت‌و‌ساز در این نیروگاه گفت: در حال حاضر، تلاش‌های ساخت‌وساز بر…</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/467773" target="_blank">📅 19:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467772">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‌
🔴
دبیر شورای‌عالی امنیت ملی: آمریکایی‌ها در تلاش‌اند تا راهی برای خروج از این مخمصه پیدا کنند، اما شکست خورده‌اند
🔹
دلیل آن این است که آن‌ها قدرت عظیمی را که در ایران وجود دارد، درک نمی‌کنند. @Farsna</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/467772" target="_blank">📅 19:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467771">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‌
🔴
دبیر شورای‌عالی امنیت ملی: بدون مدیریت ایران بر تنگهٔ هرمز، خلیج فارس نمی‌تواند امن باشد
🔹
کنترل بر تنگهٔ هرمز نمایانگر ثروت ملی عظیم و یک دارایی ملی بزرگ است.
🔹
منظور ما صرفاً بستن گذرگاه و دریافت عوارض عبور نیست. منافع ما بسیار فراتر از این‌هاست. البته…</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/farsna/467771" target="_blank">📅 19:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467770">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‌
🔴
دبیر شورای‌عالی امنیت ملی: آمریکایی‌ها به ۷ شرط ما پاسخ دادند اما ما آن را ناکافی می‌دانیم
🔹
طی ۲ ماه گذشته، آمریکایی‌ها از ۳ کانال مختلف یعنی پاکستان، قطر و حتی عراق به سراغ ما آمده‌اند و از ما خواسته‌اند پیشنهاداتمان را به آن‌ها ارائه دهیم.
🔹
حدود ۲…</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/467770" target="_blank">📅 19:21 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467769">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‌
🔴
دبیر شورای‌عالی امنیت ملی: روش دیپلماسی ما تغییر کرده و ما دیگر به دیپلماسی گذشته برنمی‌گردیم
🔹
ما ۳ دور مذاکره برگزار کردیم و در هر دور، آمریکایی‌ها مذاکرات را نیمه‌کاره رها و به ایران حمله کردند. بنابراین، ما دیگر به الگوهای دیپلماتیک قبلی برنمی‌‌گردیم.…</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/467769" target="_blank">📅 19:17 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467765">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‌
🔴
دبیر شورای‌عالی امنیت ملی: ما درحال بررسی تأسیس یک «شورای جنگ اقتصادی» هستیم
🔹
احتمالاً چنین شورایی تشکیل خواهد شد و ما به ترامپ و بسنت نشان خواهیم داد جنگ اقتصادی واقعاً به چه معناست و آن‌ها در این نبرد در چه جایگاهی قرار دارند.  @Farsna</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/467765" target="_blank">📅 19:13 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467758">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dtLrvNWsnDLDHSzho821qNZguSYRyyo_VEHF08hs6H-uz0L5ui1TYPDooHUeBF6yMEaz92XKq74lqT_bnWRjedSg7rvEuSpOwmh8ukXjK1Aiqz_GLEw1D4qohmaswYojJ6Te93GyMqabz93M6wlx7hi2_ZF93QoW7fz460fe4RWW7FUDaiavCUiQ3Xeka-M43aBocjhX-760u9P0ET-yvoS_beF9nL4SHYUsxbmewmFQXwoL4flBZ6FL6k-Uz414SD03N6qxur-ROkdvVtf2xPc5aocIJuUFTXuTbGgHM-OrIxEZ8EecN2zxzaKszBcGT9t7Qy_1bbtGQU6ANKTi_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rx9xDN8z33_geXLkU-meha4XT5-U0nrcOhRf9qDV6iuPNGPzYhkD8jcZMvU3UdbHyjwZJ6DCLEPSXBL8Y-tNbUecVz-iwY5tVCXoVja30mYbHwRF9AuHoNLlJuMVKakfGfWdyC7SIbsnBoAwj1LDTPeX3ZZ4rwJdTUO2tbFZo3qfYp_dwRqqtCHsht41QAPwc0Wvk_Jaidfypzo4SJ74PpggqPON4tm1ihoELZcCFqtq842Ajd9xnvaWHdccghXABaD2Y6TZDexHRC70KyLk_1UjoLZBIEAFgfBPk6yDHdctDGLm6eUQG1Z5qCK9OSekuyQ46BuH2xmMcF7gU04c_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RED4UKfd-ialnVTB7fyYalESec1LlCo5ObZFy6t2J_T1QDQTlebqOnfOIR_7pS1CpUb-7gpokGKSWLMzNVN5BFa5MpbI1zOkWAPZtpEWNdQWHsjnWX0DGoJvF5eX0pyUAO9d52GI1hq-iSP1bBNWMVjUKHnFAVstk6Tprm4uYckfedSOWJsy3IoEYPeo9Lz2amhvABEpOYaL3BJhgTVOPeSsi7vbvU-SNNTMvJRWqAr2FHIUy9uJuqFZS98eilp9u4mCeu8a-042hba-YuDXb3LXbgrYrvTqNrypHd4soDuFBcgB0WpuJ9F9GdBg-brwWeu4O1qMPVsiNV0XUVctGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gbiRrOEjc65UQTHATWwpSQofR9j9BqpWMiTpdXoUUkWZ-EpmOcqcEtECyMel3q-NYEIqtAEXXxLVVIiaJ1x91rgjO0aEa5E-v4mlFdqYfS53n4Z1LnXFyvh6iuyhv5xuybqTtK_t4p9UmAN6hlv7T2tBruCUkV0XZpzgDm2VfGxwJDIQy8hDTWDhcHx1_3q65v1rS964-_2W5vpdji4H9CywuSR4rrNUVQFl-9nQwbKvin1MsNvyHnKZi9_t9DbaijXE9ikIx-LbsGzWGWK-c3jxH4FIlp-EAg6dHmUe9PjknEk29EcyMGKOCw-ONhenSjlg-DzPm9RFKJ0Hs4lJ3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RJs4ilTQjdALmT9oR_XLV2R8fJi-abDLifgYlq_2iIQCz3DRT5zrmnbd_hKo3Qw1SobDf6UaKUpNrsLYdFECW4zTXUoiQPgMp_Es6NsTemn2VkzK0VA3juHwzGyfO9bgQD0GgviDrT-qAdQD7Qb4bGZWv8WL2X7r2m1m9MXyrV7yeGqSsrRrcF0SS4LWMPBWrbxWZwMrf4Uo2v51boji7MgUMeR9-lT45d5Bwt4lA2R443zddeC-hEHfmleOEpKkIbvfr7WrxK-vdJXRKTrp_WBO_EJeR0_fc3EkJEVlw9kyeXgfrqqNIRt5nsxFwtSXlQUt3x2szXqJ57SjDGZthA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V0xfKd1_5VdYbaCPcpnxmrOuOv78Ejy88WfAn_yOXhRmasGu9zBjIEJCZJvllM4JEwhx7kJkalLecIzPmEXORXamoOR-bonRAtgmZxwfhWO2Igt06hfFjDRgPo0AKt56D_8a8FiCrvK9qnArGbYotmnNP81GDzXoYfmWVO0EAwL1jneKhrX9bod8Sn0rrD2eV60-rj7XwXs-LmQ1mfYmtoSl9vVEDBA28nhhJSex-p3irjcR4Xa40eIG9sCoz6hRgiEQgdRCpv-R37O7rhIcbiIt3AcaE4bcI63lCkBUN6yMsSepLu9PcjRD7X9M_9BpcoGs83nYl3s02Eam2Oj15A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nPX-hT6XThl3FFKp810u8MeYBq9u9PKC_uIKyht3qmHDuZUsJoVWflfRAQSZr16BOD1bp856Y4hsovGjy8zaRDfNe7HHr3GzPEiyamQWpmYAX-Acfs-P5cS42f83jMkyq1RnTeBsQ1rhTiLC0Rz1znPB3Gd20VTQtDgixYoRHE0y9I1eQMXknejRFeRcbZqHFa2VvuZLZbmXN9Wq5AK6W3iEMhzxTJ_4DhhcSiQXla5vA9lOln1Djhdndsg927-MYiHkRAQB9P6NIhT856JxDoEX1ZZOnRm0IzTocVNPsLpOjw3iY36AMqKVe99Ks-AI6K_Rc_qwx-13k4HM45iliw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اینجا کیف بچه‌ها کوک است
عکس:
محمدجواد فرخاری
@Farsna</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/467758" target="_blank">📅 19:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467757">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">زخمی‌شدن سرباز صهیونیست در مرز لبنان
🔹
رسانه‌های صهیونیستی: یک سرباز ارتش اسرائیل در یک عملیات در مرز با لبنان به شدت مجروح و با بالگرد به بیمارستان منتقل شد.
@Farsna</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/farsna/467757" target="_blank">📅 19:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467756">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86149a52c2.mp4?token=BDBJGCDMALTSDBdpmrJDxhH0myOglX-DV3G9LuKu-rKURyrAKzibGAb2-x_wJq7GIAH5dl6myV59Fom-r-OMw-jQBTXPxVmFsW8kIX0-iLIyh51N-jQ6MFM4vM1duY4E5HtUcLjY5jGquShPVkky2Dl1IzUNdEDuegoeHuWP8wPUUVIG0FcevJU5cmuU5V66jDeNbmomfyl7RO-4F02HU16lHm_2FHOtGS8SSFrNs8zdNYVjAwBQbPdwwFmtU69ocmlw7iYWHyzVji214FSxsBVDTUQZEwE5i86MZzAKWN5Ut7row7YlQlbYhJY-veIG5FwuAiM9dXOvOAdPBikujB1SjHN3BRKkav3UC5pLp2KThrx2lQ98gbTYEgb8mg-1ux1c8mrUHJh3sOfRGE0gEw58fFiQD0NBDXMduEKKK7YzzIgr4-A_BMWCAEDoGZWLSJITFmplbT3dOI0DjJg_dZNKjxQxdg60vww5yRq4J00mo9GNXWnwqp1jhvvbaIm9no-RdxaRGWjWm1tCxe_ruqR4POR_zZGndOOJ2XgTVUcvc6V6nHNJIEtBdEFpmVkuwZJaSOd9Ps5ZOh5tEqBd69PQ8tOFo8JmlLFSS3KkN2OYTsTCGL94LlEj1sIOPSQImDkbeaAtQTvmdMYixrcquhlIOua0ngM3umT90tJiUjk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86149a52c2.mp4?token=BDBJGCDMALTSDBdpmrJDxhH0myOglX-DV3G9LuKu-rKURyrAKzibGAb2-x_wJq7GIAH5dl6myV59Fom-r-OMw-jQBTXPxVmFsW8kIX0-iLIyh51N-jQ6MFM4vM1duY4E5HtUcLjY5jGquShPVkky2Dl1IzUNdEDuegoeHuWP8wPUUVIG0FcevJU5cmuU5V66jDeNbmomfyl7RO-4F02HU16lHm_2FHOtGS8SSFrNs8zdNYVjAwBQbPdwwFmtU69ocmlw7iYWHyzVji214FSxsBVDTUQZEwE5i86MZzAKWN5Ut7row7YlQlbYhJY-veIG5FwuAiM9dXOvOAdPBikujB1SjHN3BRKkav3UC5pLp2KThrx2lQ98gbTYEgb8mg-1ux1c8mrUHJh3sOfRGE0gEw58fFiQD0NBDXMduEKKK7YzzIgr4-A_BMWCAEDoGZWLSJITFmplbT3dOI0DjJg_dZNKjxQxdg60vww5yRq4J00mo9GNXWnwqp1jhvvbaIm9no-RdxaRGWjWm1tCxe_ruqR4POR_zZGndOOJ2XgTVUcvc6V6nHNJIEtBdEFpmVkuwZJaSOd9Ps5ZOh5tEqBd69PQ8tOFo8JmlLFSS3KkN2OYTsTCGL94LlEj1sIOPSQImDkbeaAtQTvmdMYixrcquhlIOua0ngM3umT90tJiUjk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر منتشر نشده از حضور آیت‌الله سیدمجتبی خامنه‌ای رهبر انقلاب در دیدار با علامه مصباح یزدی
‌
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/farsna/467756" target="_blank">📅 19:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467755">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‌
🔴
دبیر شورای‌عالی امنیت ملی: بسنت در آمریکا به عنوان یک «وزیر دروغ‌گو» شناخته می‌شود
🔹
وزیر خزانه‌داری ترامپ بیش از یک سال است که بیانیه‌ها و وعده‌هایی داده که در انجام آن‌ها شکست خورده است.
🔹
این مرد کسی است که می‌خواهد با ملت ایران دربیفتد و جنگی علیه…</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/farsna/467755" target="_blank">📅 19:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467754">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‌
🔴
دبیر شورای‌عالی امنیت ملی خطاب به آمریکا: ایرانی‌ها هرگز در برابر شما تسلیم نخواهند شد و تا زمانی که حقوق خود را از شما نگیرند، هرگز از مطالبات خود عقب‌نشینی نخواهند کرد. @Farsna</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/467754" target="_blank">📅 19:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467753">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‌
🔴
دبیر شورای‌عالی امنیت ملی: یک پیام برای روبیو دارم
🔹
سرلشکر رضایی: من پیامی برای وزیر خارجهٔ آمریکا دارم: «مردم بسیار بزرگ‌تر از شما بارها در طول هزاران سال آرزوی آمدن به ایران و اشغال این کشور را در سر پرورانده‌اند.
🔹
قدرت‌های گوناگونی رویای ورود به ایران،…</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/farsna/467753" target="_blank">📅 18:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467752">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‌
🔴
دبیر شورای‌عالی امنیت ملی: ما با مجموعه‌ای از افراد بی‌سواد در آمریکا مواجه هستیم
🔹
ما با گروهی از افراد نادان و احمق در ایالات متحده روبه‌رو هستیم که تاریخ را مطالعه نکرده‌اند و ملت ایران را نمی‌شناسند؛ در نتیجه به چنین وضعیتی رسیده‌ایم. @Farsna</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/467752" target="_blank">📅 18:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467750">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMPdetIDryVfnrdknZYmONtG5V46IEbL5lNQpmoQX8RI3orYH0-i0RsQlKr2M3seMopy6jydaC8kofKKz__nB3X1Agnqq9CDt8i99NaioPjxidtKnYDWtclZM7hpM4Lk6J3lvU0a81JkzWihCZiPzyMXKIxB2iH7J4udGWd3bURKnMQWO_Hk7nMzCrFEDBWkZMnIXHc6hSQ8nR0CEimA-9lZxsyBp1UeL-QTJVjV87lDT9uCNyyPe1TedBKR9OxhMA8Hew0TPCwuKEid2hPcrR8tnJ63nLnHqMoPSmCud4lyQ0mHMEy9Np975JF9HE6Xdt3gAt0GvRSRobXgkdi6JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسب‌ها هم از دست بلاگرها در امان نماندند
🔹
رویداد پاراسوارکاری روز پنجشنبه در باشگاه سوارکاری ابرش برگزار شد، اما حواشی این برنامه از حضور بلاگرها و هزینه‌های تبلیغاتی گرفته تا برهم خوردن سکوی قهرمانی بر اثر طوفان و ماجرای برخورد با یک عکاس، این رویداد را تحت تأثیر قرار داد.
🔹
بر اساس اطلاعات واصله، اسپانسر این رویداد که یک شرکت واردکننده خودرو بوده و برای حضور در این برنامه هزینه زیادی کرده است. گفته می‌شود این شرکت هزینه‌های هنگفتی نیز برای دعوت از بلاگرها و تبلیغ رویداد پرداخت کرده و برخی از این افراد با پوشش غیرمتعارف در محل برگزاری مسابقه حاضر شدند.
🔹
در میانه برگزاری برنامه، وزش طوفان نیز شرایط را تغییر داد و سکوی قهرمانی را برهم زد تا این رویداد با حاشیه‌ای دیگر همراه شود.
🔹
علاوه بر این عکاس خبرگزاری فارس که برای ثبت تصاویر این رویداد در محل حضور داشته، اما با برخورد نامناسب اسپانسر مواجه شده است و محافظان اسپانسر قصد داشتند دوربین وی را به زور ضبط کنند که با دخالت عوامل فدراسیون، این اقدام متوقف شده است.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/farsna/467750" target="_blank">📅 18:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467749">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‌
🔴
دبیر شورای‌عالی امنیت ملی: تهران به رویه‌های دیپلماتیک گذشتۀ خود باز نخواهد گشت. @Farsna</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/farsna/467749" target="_blank">📅 18:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467748">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkuZgWrYpgu_nyBfchBiD3hi2uJVgQkaidS2eO9y54F2nK8DOxKdZfklEQYcihzdSrK-rW2O2B4A7hOWidHiFWpcG1imJxEtDTG43d4cZx6q79h-SMkGX_TsgjXN1wnXDhcyZ3sbB6Pl3B6IvyAdPLtyNYxXqRKwuH4eQSAY1gjEMJVz4x_h__0psA2y2Yat5ggaKfmQbSesxdKfqNx2QADklhdJ0QIOFNYO6kXHgbiKb90oN13_ltrxvueLxg1ixD5FqQLGqHvg07l3fdAkjwe2TtVSenjyQGiyFi_9oH6xBSnWxaU5p_4nx_JzdqSUevRxbZEahay5959NDFV-Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مخبر: ایران فراتر از مرزهایش به دشمن ضربه می‌زند
🔹
ایرانیان، مهاجمان مغول را مسلمان کردند و فرماندهان امپراتوری روم را با خفت به زنجیر کشیدند.
🔹
مهاجمان جدید که با مغزهای کوچک، تصور غلبه بر این ملت تاریخی را دارند، این بار در تنگۀ هرمز غرق خواهند شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/467748" target="_blank">📅 18:49 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467747">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">پیشروی ارتش یمن در دروازه غربی شهر «تعز»
🔹
منابع خبری گزارش دادند نیروهای مسلح یمن در حال پیشروی در ارتفاعات «صبر» هستند که مشرف بر شهر تعز است.
🔸
همزمان با این مسئله، ارتش یمن بخش‌های گسترده‌ای از ارتفاعات راهبردی «هان» را تحت تسلط خود در آورده است. این منطقه،…</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/467747" target="_blank">📅 18:47 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467746">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‌
🔴
دبیر شورای‌عالی امنیت ملی: امروز اگر رویارویی دیگری رخ دهد، قطعاً با برنامه‌ای بسیار وسیع‌تر و گسترده‌تر به استقبال دشمن خواهیم رفت
🔹
کابل‌ها، دیتاسنترها و تأسیسات هوش مصنوعی موجود در منطقه بیش از ۲ تریلیون دلار ارزش دارد. @Farsna</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/467746" target="_blank">📅 18:38 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467745">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtPx2KDGhE_1d4XOJ8x4wpqo9fZV8U0uOaiyQdJ-n2qKJ1GO3iO5o0EQi3TapUdTzANJo5JDQfODZIP63opnnGa82FMWOjD9evSkKwjwYbbU3RMo31dqBDTmw3A26m12xOVFWr1aEfREJgLMad8yUTSrKBtaI8pUhqvUZnn0HS5JpOy2Irn1X_qp97saVaxZGNTOiu2A3Md9R2mmcXEI_lbcWtBWaMYuNixmMmA6dR9TMrdIboICQ41EnL6kUxV_GMMaznBX9_fZYjP_Sx6iQ4iznXQJCg1kILfbtG9fL4KUSihbrZACc9hlFB7GL7WEHZcUwsnCvN2i4WuDCGsdYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ تلاش ترامپ برای کنترل قیمت نفت این‌بار با آتش‌بس انرژی
🔹
رئیس‌جمهور آمریکا در تازه‌ترین اظهارنظر خود گفته: «بین روسیه و اوکراین یک آتش‌بس انرژی برقرار شد و هر دو طرف توافق کرده‌اند؛ آن را نقض نکنید!» @Farsna</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/467745" target="_blank">📅 18:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467744">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‌
🔴
دبیر شورای‌عالی امنیت ملی: اگر دوباره جنگی در بگیرد، بسیاری از کابل‌ها، دیتاسنترها، تأسیسات هوش مصنوعی و سایت‌های دیگر موجود در منطقه نابود خواهند شد. @Farsna</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/467744" target="_blank">📅 18:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467743">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‌
🔴
دبیر شورای‌عالی امنیت ملی: آمریکا دارایی‌های بسیار گران‌قیمتی در امارات و پیرامون تنگهٔ هرمز دارد که ما هنوز آن‌ها را در میان اهداف خود نگنجانده‌ایم. @Farsna</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farsna/467743" target="_blank">📅 18:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467742">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‌‌
🔴
دبیر شورای‌عالی امنیت ملی: ما کاملاً آماده‌ایم که اگر جنگ دوباره آغاز شود، توانمندی‌های جدیدی را به‌نمایش بگذاریم. @Farsna</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/farsna/467742" target="_blank">📅 18:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467741">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‌
🔴
دبیر شورای‌عالی امنیت ملی: فرمانده سنت‌کام کارهای قاچاق را رهبری می‌کند و او همچنین از ارتش امارات استفاده می‌کند
🔹
آن‌ها از ۵ یا ۶ شناور کوچک برای انتقال نفت به نفتکش‌های بزرگ‌تر استفاده می‌کنند، اما ما نیز هر شب ۵ یا ۶ فروند از آن‌ها را هدف قرار می‌دهیم.…</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/467741" target="_blank">📅 18:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467740">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای انفجار در ریاض پایتخت عربستان خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/467740" target="_blank">📅 18:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467739">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aece21a246.mp4?token=oAq8iwHh_P-pE9_LJJgWgCdOmJkPvLQrPJSZopO_tRhvRZezJo6BfwSQENy8pHLUMxSFoPBl05m4XS-MXj-iRBUioB8t7qmJwOSGqmLmI44_S5nXvp4kbTBVLEGyTsL4pOJPpsfgieTDqNPU0riC3GIqdIZOUtDcMvomRp0Xi9zfSZxyJraGAn9Hd6s2XbuMPZKfdkAbfr1aKSLGLHrCNkQQeXiUwhxksBpXJl9z5BE0o0SbCAzEixIsUZ4miRHbLWOujQeXuC61MEgzLN8xJru8L24BrkTshQE812VP6s5odFDwVXtm3-BkNQqgeroRC00yPKjPYGisACTop39Ijw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aece21a246.mp4?token=oAq8iwHh_P-pE9_LJJgWgCdOmJkPvLQrPJSZopO_tRhvRZezJo6BfwSQENy8pHLUMxSFoPBl05m4XS-MXj-iRBUioB8t7qmJwOSGqmLmI44_S5nXvp4kbTBVLEGyTsL4pOJPpsfgieTDqNPU0riC3GIqdIZOUtDcMvomRp0Xi9zfSZxyJraGAn9Hd6s2XbuMPZKfdkAbfr1aKSLGLHrCNkQQeXiUwhxksBpXJl9z5BE0o0SbCAzEixIsUZ4miRHbLWOujQeXuC61MEgzLN8xJru8L24BrkTshQE812VP6s5odFDwVXtm3-BkNQqgeroRC00yPKjPYGisACTop39Ijw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت بی‌واسطه ثریا از سرزمین اژدها
🔸
از شنبه تا پنج‌شنبه، ساعت ۱۸، شبکه یک
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/467739" target="_blank">📅 18:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467738">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🎥
ترامپ: فکر می‌کنم وقت آن رسیده که اوکراین یک رئیس‌جمهور جدید داشته باشد
🔹
پیشنهاد می‌کنم که آن‌ها یک رهبر جدید روی کار بیاورند که بتواند توافق کند. زلنسکی می‌توانست توافق‌های زیادی انجام دهد، اما به دلایلی هرگز این کار را نمی‌کند. @Farsna</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/467738" target="_blank">📅 17:58 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467737">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mr0sXwVnJLlUnKfWjGgkvJQX2xkpRKx5295h08zN_JeR9LjwzS2_To60VhynKBwkqyDnBR9x8QphzdXEO0uI_iUrBQJAqRUcVJPO6aG7BHNHPFSUZizGY0BOFe-2z1SoJu84YInb_B9qYMPgzrTO7xpAT69hv9ND4MNYhtYDl_YK_OYv4fptb4-prGr1aHfGCJbD6RA_vnBnuWQDPCIQqW1GX41FDGb1fFqp4FrazaCnJIJxANo8cmN-O92BfGH8gWmozXip7oEjGlVFG8H4dapTrjjpsUY9Ant8HDTDzKxFhfYtpMFLyAXgZZcntLT4E0Lpu7fJvUI1MGPsIdreCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بن‌سلمان برای مقابله با یمن دست به دامن صهیونیست‌ها شد
🔹
روزنامه عبری «اسرائیل هیوم» گزارش داد که محمد بن سلمان ولیعهد سعودی از طریق آمریکا به این رژیم پیام داده و برای جلوگیری از تشدید تنش در دریای سرخ و باب‌المندب به دست انصارالله درخواست کمک کرده است. …</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/467737" target="_blank">📅 17:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467736">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‌
🔴
دبیر شورای‌عالی امنیت ملی: طی چند ماه گذشته، ما هر شب در تنگهٔ هرمز ۵ فروند از کشتی‌هایی را که قاچاقچیان استفاده می‌کردند هدف قرار داده‌ایم.  @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/467736" target="_blank">📅 17:35 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467735">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‌
🔴
دبیر شورای‌عالی امنیت ملی: ترامپ با استخدام تعدادی از اشرار که در آب‌های ساحلی عمان فعالیت می‌کنند، به قاچاق روی آورده است
🔹
او هر روز ادعا می‌کند که تنگهٔ هرمز باز است اما در پاسخ می‌گویم: شما درحال قاچاق هستید، اما تنگه تحت کنترل ایران است و ما آن را…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/467735" target="_blank">📅 17:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467734">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
دبیر شورای‌عالی امنیت ملی: عاقبت قدرت‌هایی بزرگ‌تر از آمریکا که تلاش کرده‌اند ایران را فتح کنند، زباله‌دان تاریخ بوده است.  @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/467734" target="_blank">📅 17:33 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467733">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
دبیر شورای‌عالی امنیت ملی: عاقبت قدرت‌هایی بزرگ‌تر از آمریکا که تلاش کرده‌اند ایران را فتح کنند، زباله‌دان تاریخ بوده است.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/467733" target="_blank">📅 17:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467732">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای انفجار در ریاض پایتخت عربستان خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/467732" target="_blank">📅 17:17 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467731">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/962b87eb94.mp4?token=R9Rpbxk2M0PAPPd3eQ-STj4k-UlraYw-qPxLNmn6y9MVo9MkOaAwcnTASdWx1jFIJ-dQZEGwK2BCXmZ6gdgucU2N09WEsiuq3AV2H_pHCUfnEKHURsJyfmxJGRwFzrZI5eUDXP6_hPX7nE0cdzjgcVEutES1F48hivqs9kqHDs-Mnk73w16cTf_kYoINhva_yZiLzuSB8rnJ4prmZLQMAwfn0NhIb3fGcWefG4Ef88hSOvnODXOowhO4VydRqYlOvPzoWAMSqozjvP1UlPw5fCF5Cn7M28OGRyU_VhOgz6ep14Fm9ay-icQI7oyVhdP4DFCVMc1U9oiMthyYPy7yjTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/962b87eb94.mp4?token=R9Rpbxk2M0PAPPd3eQ-STj4k-UlraYw-qPxLNmn6y9MVo9MkOaAwcnTASdWx1jFIJ-dQZEGwK2BCXmZ6gdgucU2N09WEsiuq3AV2H_pHCUfnEKHURsJyfmxJGRwFzrZI5eUDXP6_hPX7nE0cdzjgcVEutES1F48hivqs9kqHDs-Mnk73w16cTf_kYoINhva_yZiLzuSB8rnJ4prmZLQMAwfn0NhIb3fGcWefG4Ef88hSOvnODXOowhO4VydRqYlOvPzoWAMSqozjvP1UlPw5fCF5Cn7M28OGRyU_VhOgz6ep14Fm9ay-icQI7oyVhdP4DFCVMc1U9oiMthyYPy7yjTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساروی: حسن آقای یزدانی الگوی همه ما است
🎙
محمدهادی ساروی کاپیتان تیم ملی کشتی فرنگی در گفت‌و‌گو با فارس:
🔹
برای همه قهرمانان احترام قائلم. قهرمانانی که الان در کنارمان هستند، قهرمانان جهان و المپیک، برای همه آنها احترام زیادی قائلم. آقای حسن یزدانی، زارع و پهلوانان کشتی فرنگی مثل امین میرزازاده و اسماعیلی، از بزرگان کشتی ما و از افتخارات کشتی هستند. من برای همه آنها احترام قائلم.
🔹
این نسل از بچه‌ها واقعاً بی‌نظیر هستند هم در کشتی فرنگی و هم در آزاد. از بزرگان کشتی هم آقای پهلوان یزدانی واقعاً کسی است که همه از او الگو می‌گیریم و به وجودشان افتخار می‌کنیم. او خیلی انگیزه‌بخش است و ما از او درس اخلاق و درس قهرمانی یاد می‌گیریم.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/467731" target="_blank">📅 17:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467729">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rL70ryJdFvE2Lr3lfT1dT3VcciTAhDT1j8Usp9pRLJSLBLmMxqxM8mdERlMD-rAs6QhvxueGzKXHsyuSFdRhLtMI14gI2PibwbcaghA-fZ5IITtSxJnkhrv9x0Dq40LczFoETNYrYaY-pzPmnpGwzCSLS_gZuu6QjhtX9qjlFU6_4GmEOcRgsVHBzeZmj7gbio4rY3vDfwhuAWt9MjIrDb_8hPi1S7u560nTLJfo6OYKZzUUAPSbWPTPpcoSeJpP7uLrJgR4BV1ccBKs8Y8UA5XuHSIZMDCvY5ccyyJjswK10ZrbD386MeVTQyYtfi7NbNJGiV6Y5WXzWqAZhLoCIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
منابع خبری از آتش‌سوزی یک کشتی در مسیر جنوبی تنگهٔ هرمز بر اثر اصابت یک پرتابه خبر دادند.
🔹
برخی ماهواره‌های حرارتی هم یک آتش‌سوزی بزرگ در این منطقه را ثبت کرده‌اند. @Farsna</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/467729" target="_blank">📅 16:51 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467728">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ueFci2ZyoljWythgUJCvVRVb0Yw0JzP6IfcyOEdNSsIZs8FZVoGbo7IDawJg69gk-6CDKcEQYDd0xltZlHA10QAanYN4uUtJZ33haiG1MutBhMzzhtl8-wuC_xvHsMamHW-M7YwCxgtChqK_HqhmW3EyGZsu3uiHyqoHvZz4I1D_UJFWwnrXqB7VcXkwJGvFD56vgmr-ATjPWb0yhuV7i2e7EqWGZwaajuJFQB8Qd7a7wYZf3XTYTK3uzsO3NOx1zoehgM9fxN75smW2_66-nroWrcuCuZZG7ScNA905d41uoCiZb9QbbKxJwdtiM-GBEGSWmqQN-23oFa4f4AlmVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرار پول از خلیج فارس رکورد زد
🔹
کارگران خارجی شاغل در کشورهای عربی خلیج فارس نزدیک به ۱۶۱ میلیارد دلار از درآمد خود را به کشورهایشان فرستادند که این رقم نسبت به سال قبل ۱۳.۶ درصد بیشتر شده است.
🔹
این خروج گسترده پول، در شرایطی رخ می دهد که جنگ، ناامنی کشتیرانی و گرانی تأمین مالی، اقتصادهای عربی منطقه را تحت فشار گذاشته است.
🔹
کارشناسان اقتصادی در کشورهای حاشیهٔ خلیج فارس هشدار می‌دهند، اگر بخشی از این پول با ابزارهای پس انداز و سرمایه گذاری در بازارهای خلیج فارس نگه داشته نشود، اقتصاد این کشورها بیش از پیش ضعیف خواهد شد.
🔹
براساس داده های مرکز آماری شورای همکاری خلیج فارس، پول ارسالی کارگران خارجی در مقایسه با سال ۲۰۲۴ حدود ۱۹ میلیارد دلار افزایش یافته است.
🔹
بانک جهانی گفته،‌ وضعیت جنگی، تجارت در منطقه را مختل کرده، تولید نفت خلیج فارس را کاهش داده و فشار بر گردشگری، هواپیمایی، لجستیک، بازارهای مالی و قیمت غذا و انرژی را بیشتر کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/467728" target="_blank">📅 16:44 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467727">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d916f969ed.mp4?token=EuyxeEF1yDYtCPl_e4gTYQvJse3blddAPB4XFYXQ_fa84BAbHPlCLrXEkyCFnSVMsKvo8UOctNZOwhi5T-tt6BucRW-vjuXeXroQWffGRV4bT7hlHUgxr7-6vUCTFg5Vx83vHJpbr5GSvfcsOQkWB-PHSY5RhSAfkqtRWKY_D-eio5o5GFOEN9WmwvTsunx18PxiVuhe6kipoZnnVcf8kCKRDIsbrVXzBWSTN2Cft_Zvsz380ximDiw0HOkkFFKvoJYdeevP5Gyd3gqC5wXMzfuTSHNwhOAjMA8ps2SZw2PmNbtfcmCuy8MBaLmw0haqYbOumnCO_gZrWmpTAD4BdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d916f969ed.mp4?token=EuyxeEF1yDYtCPl_e4gTYQvJse3blddAPB4XFYXQ_fa84BAbHPlCLrXEkyCFnSVMsKvo8UOctNZOwhi5T-tt6BucRW-vjuXeXroQWffGRV4bT7hlHUgxr7-6vUCTFg5Vx83vHJpbr5GSvfcsOQkWB-PHSY5RhSAfkqtRWKY_D-eio5o5GFOEN9WmwvTsunx18PxiVuhe6kipoZnnVcf8kCKRDIsbrVXzBWSTN2Cft_Zvsz380ximDiw0HOkkFFKvoJYdeevP5Gyd3gqC5wXMzfuTSHNwhOAjMA8ps2SZw2PmNbtfcmCuy8MBaLmw0haqYbOumnCO_gZrWmpTAD4BdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر شهید انقلاب: چند جوان بی‌تجربۀ سعودی توحش را بر سیاست عربستان غلبه دادند؛ این به ضررشان تمام خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/farsna/467727" target="_blank">📅 16:35 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467726">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bInp_a-vDeP1Y4qnsqfll2TjBVm8WTFTJUAxKtvNa9aObL-99C43fMRuJXG5nS9u9saBLH0BgIqx9FusfE15WLep_7HQ-jHGPUR0dPppQt8Ep9TebZGKEcxEl1KPRyAcrtRaOcOXb0IjwwATNVQ4CqCOiihd_M2CJOESRiT25nNo5pnKV7q4uuUz7sdQ8x_Snm41y5M_KzLKpzXnakosGVuU-gDLssB5rk2uAQjgkgtR6pjhjwOAaPmCiJ4dlh3kMuk69kUbvmN212OHP3Ezj3epxxxVJbebyOwrXFDGbghVgJnpFpMlSge1jxLa6xtJGHpmSHKJYtUQp9Y3XBprQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
همتی به بسنت: از قول ۲ هفته‌ای که برای فروپاشی اقتصاد ایران داده بودید ۵ روز بیشتر نمانده و من به شما می‌گویم که چنین اتفاقی هرگز نخواهد افتاد  @Farsna</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/467726" target="_blank">📅 16:27 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467719">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XboHF2X3mecGTEF8tU_3IT0HmCSwQjqfcbbPdYsxvLwAS0-JFFKHXT0Y1wHZ1pYvH1G9sNa9dNz9o6vgoj5Lciaw3Uspw6wQu0XdI-XBqSxEpDNC1hHxZwGeSdiCAfbX76xQHYjI_yjKJgn6zZjSlSy7wNxQe1Vnz9PGh45394vexj9RB8KcHSXzfj9zVMUBldPe0gHaz3sSHQodeksj6GZscVuLqNCoFNqEJbFfJ_SVFDmtm5QWRDxCBOuqHhRwwyYiYGDNLijG0kJSIgYKD8dzS4etmrdJ5xfJeyFt2y9tJcSwpga5njygZ59xC9eWgtleeirP2k6VXyRLDkeIKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oz-kXdpTVTQSt-E5E_tyJ-DoXyn1f_PTaFaB4ADzjdHe_AJ3fEywCeEK7-u3J-paEMw0q2j6nFkTqmc6LsfQmSImGigFdKNzCdVbfoOLCgPDmXWZJKBhBejRG2EcdapjXTWMX3h_89q4ALjOD5HSk7VlO9NiAB5cjNpE0R0vscaBzzgTOAMMP9WUevOmjObXdN4m98v0pMedaiG8Bu9mypVzdfNJez-n0PrTLHDcrMEedz5hrM7okW2PtCXfmERQwVbHxPZyVEKnll9FIn_lKGR8fPzTec-SgncdHq9K4lWlP2oNKc4y0_PIJvmad2lwmCZTono4WAdT_253PM9gGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZHbLGTRfk1m4WVQeqq8u_dykrJVbZdjVQGgFVilwnvDZlbQDXbaPJjT6uBRdqS3hriwNMaDhTSI6f1i1KkZlTIPQ_MAYaPykRGK9jpLWydz1ms8m74nkqotWHoop8kT_8E-vXkz18AuJ8oZqaPIOXfmTkwsaYHQNuozp_JYzz1LmKthSfFrQkp8Zsa786J-K22fhN6F56usfVCIqP8wVWNlmXy4JYi3wNXf5i9i_iLIpC3552ia2ur6GTeHbJnwidlKGKzI4ulMd1SgAd16TrCVw222d7WBBGhEHccHXHG6VXW0CFlWbeYYJIyNNIF_KhBXyVp6vZqIYAkZPcATzHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q0Y-KbITwo2KURlYeWTfTnPfbGc-UnvtxeVGwRQXeAGxzACHV7elr4zbcLmrH_kzP52rYdGF5QK8ZBUQ01BfD-w5iT6jPUFIUIOWyt65_UmBO_CB0fpAMPDmY4HKh0tfDxNzMa-JuJuGewf8C5Yy9P2Qk5w5FATjNddzc2cbEVLhLhaw_pFmhUSbLMB1z-Pr9Bc50pxUhJu08o6Aw-XLr_GouAw2AciUSCFvJp5ltzKnq0vjmbxMwUxIOUAo9PaxLoa_dPx95gBhYNVODTCGoLLPhwaXbNvcmVXImQkGUaH8xkgkPwdIOQSiFxsuX3SBslvC3lvcWgYWYtbkTFAYfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nXdp82-oSGoWJIcfxSGicZMLv0_vfgEp_KOWQAegTeafLd73F1wDNpnEHv90FbZAZR7SrpVNRfSLIliDVn68fxf5ziGPAJzQVGk0MQ1nUZncdFrvhN8DxF_wjEmhdIhroNJZGl0tnHWGd8aTl759jWc03lJ7C15xK6evifzyRzRTWxPDdPPBtrWIzxBSLGKYIRr3-St1NBZMFqDDMnzmDqbVL1j7C3iN_c3QBbdYvlqfWk_5pnl56IEgj4P-zeeWbd2V981fd6HcZTaD0DbDcxTeHNnDGofs2APSrFBDA1UXuLi8tRzNAWexY8XthoW98sY-vfcFQfH7XRZNNpAfTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VoS9Zmim9D7AxnH5JnuB494TK24IyOymSaOJiM0jmwkfHKpydRNw7IGqS2ezvruxxYnSZVC0q0Ts6QGNxx56AcVSnHiSyP7N5qibkeRAAvd8pLa6ir11YNRml_43G0-4vNOnx-8fnmqg7avEeWvK56_rogqE14Ai3mAaZiJAINtLg_kQG3yCtnzdwCGSbvxSJ_SFzhVmPLxTzQcvPm8gLFYnVB0Ly9aSrgb1HssbEwl4HV5owPo2ko8x0k6eOtohFDbT_tMCDrlWk_gZT34c9Fe2DAjrBz96zt5q8hqAdYxaHO9vzTZpqE5u1_Y1GFZ5O2uKUxueN6e2BIbvuVCI3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gumbp27uOAOoXDA884QDZ1TKq2szsN6B5qmCFUHSBWYWHl1g33rJ9kFDnU4N4NMiaJya5ZKEOL7kEOdVG0g9yDy4SpEX96i0XCXl-ODUFkrVHGwk-LHivogMjk-3SxtMSKQHUTq_NcqBWvR6UmpWP-5wD363VuT_4Afc_KLBCe0ilYbfqyfnev2SHNViK-OFJj5yblM5Zl9iZMCCDBqCRY41GFfovgn5rftHLAR8NsDWcnEyZx8TdI0FSs7fwOz_44-BAdcZ6dXm1EKQmog4InR1DZxDWrJRT-zFI4f86bsC8OE1nk9Tj8oDKYJ7W-4pYJC60z4w6G13SZRpyQXlgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تشییع شهید حملۀ تروریستی زاهدان در حرم حضرت معصومه(س)
◾️
پیکر عباس آقایی از تکاوران نیروی انتظامی که در حادثۀ تروریستی زاهدان به شهادت رسید، در حرم حضرت معصومه (س) تشییع و در گلزار شهدای علی ابن جعفر(ع) قم دفن شد.
عکس:
حسین شاه‌بداغی
@Farsna</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/farsna/467719" target="_blank">📅 16:23 · 19 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
