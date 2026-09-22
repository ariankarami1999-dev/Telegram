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
<img src="https://cdn4.telesco.pe/file/vVIXrgJFeMi6eb0LnMzBxNjGM24XjofyA3_4f3C96VH4I2DpJxaRkAKNWVmt1GgcW5PHEJTtoX3YvSd6IGmwTc7XkDX19dFdc0J6zdnn4gu2Zx9COCeJfGQ_KoBV4dqv3qjZ0uxra3SzVdcQWK7_u-cBp8CNOzF89gf8ASXCtnE1Se9etS24G1Swa_VI7UdvwR383NiAT9rB_D1XHSwv_f8qHY6Ea-vyKR7SraXMY2kvdvQ0H7h06ZdTS7_iftVJWz3ix3gpcxtZLND6qnwR1Doom5dMQlMXukk7KmWEb7Cxe5kt7eWmt1DCQRoj3qcWBar6Ivi2kHQPbqUMXlrlnQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.78M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-31 22:30:47</div>
<hr>

<div class="tg-post" id="msg-463745">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/986e451529.mp4?token=vqZ5E0mtN9AOhpvypjpXuevHSURvpQLLo5S_dKUnYvLGj_IHX_iVgKtfEF60ioX_Rhr_whzoAKRhYCuwVCHjJOD9ji2n3mfOAnQCLQAKGE--WMfBKk0qWPQ2pkYk0AxuWfxMobLwKdDUdQ-fC1mJEWqXouX_Cz3QDMUZgtddfydxWx_ZzQVhWQLGj7TpcrtYjIzjaTyP7aKQmvoXs_vA943LTLahXZXzqCijCyFvkw2N7gUt5DlrJPBQfIndwarQ9q6YWw-YUDl_dae-bFuFSNzsPb38Tv3FOqeSVeY-gLfBm_xnmqGxh1hTpWkP1auoq5KaIGaYhamEsjWxzoumYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/986e451529.mp4?token=vqZ5E0mtN9AOhpvypjpXuevHSURvpQLLo5S_dKUnYvLGj_IHX_iVgKtfEF60ioX_Rhr_whzoAKRhYCuwVCHjJOD9ji2n3mfOAnQCLQAKGE--WMfBKk0qWPQ2pkYk0AxuWfxMobLwKdDUdQ-fC1mJEWqXouX_Cz3QDMUZgtddfydxWx_ZzQVhWQLGj7TpcrtYjIzjaTyP7aKQmvoXs_vA943LTLahXZXzqCijCyFvkw2N7gUt5DlrJPBQfIndwarQ9q6YWw-YUDl_dae-bFuFSNzsPb38Tv3FOqeSVeY-gLfBm_xnmqGxh1hTpWkP1auoq5KaIGaYhamEsjWxzoumYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر صفوی: آمریکا می‌خواست تنگۀ هرمز را باز کند اما تنگۀ باب‌المندب هم دچار مشکل شد  @Farsna</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farsna/463745" target="_blank">📅 22:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463744">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🎥
تصاویر سرنگون‌شدن اف-۱۵ سعودی توسط یمنی‌ها  @Farsna</div>
<div class="tg-footer">👁️ 680 · <a href="https://t.me/farsna/463744" target="_blank">📅 22:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463743">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/416a1505f7.mp4?token=T8yzXFcwIu9po2f4yu90okJONU7PfMgLXtIzk7rhFGW1gdvsOjjGegEnIBsiftGUWatOgVkRXOjkKKL9-29_aaRk9RQizjTPUgcmkiPwO1WVXvvQLhz9mW7qkeNFC7AJHTCvGqQ3QWeLxTjDLrwZEf_J8SckNL3WK5AAlCII_Zc1ewMCm27EcHiDsdoVWsdQXTSc5WzmNAS-IFFw72Bc4CNNrIiiqj208GWr_Rw8aAV-FZoeUX8YoJ2nJaFI7_BVnpdlMuHElcMM2SXpUCBi-4VnDCk9IcFnQOhy_DEEqJBl-_6CKkt1RjV4bD6U73RNnuLpqbVXQJqen98Pbc_IKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/416a1505f7.mp4?token=T8yzXFcwIu9po2f4yu90okJONU7PfMgLXtIzk7rhFGW1gdvsOjjGegEnIBsiftGUWatOgVkRXOjkKKL9-29_aaRk9RQizjTPUgcmkiPwO1WVXvvQLhz9mW7qkeNFC7AJHTCvGqQ3QWeLxTjDLrwZEf_J8SckNL3WK5AAlCII_Zc1ewMCm27EcHiDsdoVWsdQXTSc5WzmNAS-IFFw72Bc4CNNrIiiqj208GWr_Rw8aAV-FZoeUX8YoJ2nJaFI7_BVnpdlMuHElcMM2SXpUCBi-4VnDCk9IcFnQOhy_DEEqJBl-_6CKkt1RjV4bD6U73RNnuLpqbVXQJqen98Pbc_IKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یمن تصاویر شکار مزدوران سعودی را منتشر کرد  @Farsna</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/farsna/463743" target="_blank">📅 22:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463742">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04d3d62672.mp4?token=BDbhcuBAX-_uS8YpyY1c6QN2lKD2anJ2nxzjx0iQVRKeRfuafJjkNWXN3QLuZ65wF2EkXi34c8dhLKF0RKvwdDQ9vSCHDsCf1DoLqPES2uZTGAEgZtU-nHUGUKUD70KLGAch4QkTwBu80b4xjAU7YtIzkHbKyW38zZD2vVJPepZ487tRq5IdEKQLgiDPJJRuV9iQAIC41XdqBOeMhvf3KTjvogdOScaZF8GXNhG5ik7_fSumHLuii73bjLl9ruJeNOdrR-XxYyUkuopMXvMBKUum_1z4XH6JXRxazmyeHl5DfaPwlv1GJarux252kDOvAnybdbALJTZa9UOfMdd7cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04d3d62672.mp4?token=BDbhcuBAX-_uS8YpyY1c6QN2lKD2anJ2nxzjx0iQVRKeRfuafJjkNWXN3QLuZ65wF2EkXi34c8dhLKF0RKvwdDQ9vSCHDsCf1DoLqPES2uZTGAEgZtU-nHUGUKUD70KLGAch4QkTwBu80b4xjAU7YtIzkHbKyW38zZD2vVJPepZ487tRq5IdEKQLgiDPJJRuV9iQAIC41XdqBOeMhvf3KTjvogdOScaZF8GXNhG5ik7_fSumHLuii73bjLl9ruJeNOdrR-XxYyUkuopMXvMBKUum_1z4XH6JXRxazmyeHl5DfaPwlv1GJarux252kDOvAnybdbALJTZa9UOfMdd7cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر صفوی: آمریکا می‌خواست تنگۀ هرمز را باز کند اما تنگۀ باب‌المندب هم دچار مشکل شد
@Farsna</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/farsna/463742" target="_blank">📅 22:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463741">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">واکنش مقام ایرانی به ادعای ترامپ: در صورت تجاوز دشمن برای توسعهٔ جنگ آماده‌ایم
🔹
یک منبع ارشد امنیتی در تماس با فارس در واکنش به صحبت‌های غروب سه‌شنبهٔ ترامپ در سازمان ملل اعلام کرد: آمریکا خط قرمزی در منطقه باقی نگذاشته و ایران برای تمامی سناریوهای موجود آماده است.
🔹
به‌گفتهٔ این منبع ارشد، در صورت آغاز جنگ جدید، ایران از «توسعه جنگ» هراسی ندارد و آماده است پیروزی بزرگتری از پیروزی قبلی در جنگ پیشین را به دشمن تحمیل کند.
🔹
این منبع امنیتی با تشریح اینکه ایران از آغاز جنگ جدید چند مدل مختلف از انواع موشک‌های ضدناو و زمین‌به‌زمین را با موفقیت آزمایش کرده، تأکید کرد تحقیق و توسعه و ساخت سلاح‌ در ایران به‌طور کامل به زیر زمین منتقل شده و به صورت ۲۴ ساعته ادامه دارد.
🔸
ترامپ ساعتی قبل در سخنرانی سالانه خود در مقر سازمان ملل در سخنانی گزافه‌گویانه مجددا «ایران را تهدید به نابودی» کرده بود.
@Farsna</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/farsna/463741" target="_blank">📅 22:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463740">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YqzUAkiLDcnYF1kbLHxrRPpcUa1sta4CxtFdeV487C9SukS-e0NjWTHeDNcib0is0ATyPFmKWkPtyMxoLy2l8ajBu-kvk4tWJqX8LsuYppxlzlTKCIIHEsbO9f0ePmx9TmnRZOS9-PH1dIoVFjnHr8_huDGEipXsw7AdIVp32adU_kaPa618RaHETklkm2ASqFBXCjO8gwRfmjIyyTyLfPCyUy0n-uGdSw7CelEbX36SAdh6WPqjKPe7t2SEy0TlAVTUn_d14mh9p-igHo746ZKMns6wWJGWD6v5iglPlMIWy6Ryz-ZsfHqerm55PX-jju6rTC3r68Ol2kWdAxvFwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: اروپا مسیر مماشات با قلدری آمریکا را برگزیده است
🔹
وزیر خارجه در گفتگو با مسئول سیاست خارجی اتحادیۀ اروپا: پیمان‌شکنی مکرر آمریکا تنها عامل اخلال در روندهای دیپلماتیک بوده و اتحادیۀ اروپا نیز متاسفانه در موارد متعدد به جای پایبندی به اصول مورد ادعای…</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/farsna/463740" target="_blank">📅 22:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463739">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6ZgrkYLiC3DWt0H2WuiHdE-ZfCbssvSn9lHF7wmvfoUXhz_DN1fMhElGdlQQwGUVRw3fjs7Dk4LrItbtqyD5EUxuAga1L-GApj7_oqN9IBwx3b_52H0XEDgStstZ6jac3CIYFcl88vrE1-ujO4XxCsIwRZrH3_Jf7j6VRKCrV89YeeCUchwa-x7i95TCT6w2B3wjQ3cs3UgKU2ItKYpq-Rv715Y6qYa4ZUHNkRGle8c0f5l-QGMti0nQY18BDZ07D15I9AXD_7AfPySW7kQMy-Z9WSlp5CMsY7oYk9TknUwEb9YwJzUzyBRHTMUCRcWDmhBGUPA91FOsAeF4-LWew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
عراقچی با مسئول سیاست خارجی اتحادیۀ اروپا در حاشیۀ مجمع عمومی سازمان ملل متحد دیدار و گفتگو کرد @Farsna</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/farsna/463739" target="_blank">📅 22:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463738">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdfde8fd33.mp4?token=oH9pvQf4X9AxR3tHS94I-19TOgC0_4d-H7GloCbcJWIubymg6smL6IXr7K7l4bOWOqWNTpQBMVDori4h1nsBfaquoEgdKrEP2m3TPE0sPVY8E8sG4jMznHqWSqDNH6XXtlvs4ZwJoymgUGnf6gLF2Syrh6YOvmioPJXZEGelPoTkR1-kiFmw18a2aMkA_4anzASdsmVWlQ8IbjM_rshau08kfEKXhoPqO4AHsI0AmNu2p0JA16cL06tE5cu9P4xkFkzT06sPzf6fvvn_zlABwNaiiyQIA11ZmffPmjVzvGsw5BmtwxehzczVbdDKdEIlayj6Sl5UlViB79WZ1EKd9Vq4KKaMrkHaMkz605VEqf4aJamB2EudXKpGxtNHsoFNYInOha_gXo0TYFSPx1GIlVQDPdJuw32dZsWcJyEofI4MOGZBThAF30NPHP43F-frR1hQ0WLDeTT6VhvMxiRSmcRXxa1Shd0E3pZ0LjGql1Cyf8HOX3GRhQM-GzndQOG83oM6n3k22vdRRFAsgy6EuE_unhKsrejJNHVRFwmXmQagOlzST-1kzYm8-cbx8bZhMHlJx8uipC50qrywsf51bNDHwEyAn4E7i3AZ4f-CRaZhFs8Y9Dav-l2P4ygqlyG3OM-jWnJGT22QOcsKZiCmak7Xl8OXWTXd8o5FRz0BHCo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdfde8fd33.mp4?token=oH9pvQf4X9AxR3tHS94I-19TOgC0_4d-H7GloCbcJWIubymg6smL6IXr7K7l4bOWOqWNTpQBMVDori4h1nsBfaquoEgdKrEP2m3TPE0sPVY8E8sG4jMznHqWSqDNH6XXtlvs4ZwJoymgUGnf6gLF2Syrh6YOvmioPJXZEGelPoTkR1-kiFmw18a2aMkA_4anzASdsmVWlQ8IbjM_rshau08kfEKXhoPqO4AHsI0AmNu2p0JA16cL06tE5cu9P4xkFkzT06sPzf6fvvn_zlABwNaiiyQIA11ZmffPmjVzvGsw5BmtwxehzczVbdDKdEIlayj6Sl5UlViB79WZ1EKd9Vq4KKaMrkHaMkz605VEqf4aJamB2EudXKpGxtNHsoFNYInOha_gXo0TYFSPx1GIlVQDPdJuw32dZsWcJyEofI4MOGZBThAF30NPHP43F-frR1hQ0WLDeTT6VhvMxiRSmcRXxa1Shd0E3pZ0LjGql1Cyf8HOX3GRhQM-GzndQOG83oM6n3k22vdRRFAsgy6EuE_unhKsrejJNHVRFwmXmQagOlzST-1kzYm8-cbx8bZhMHlJx8uipC50qrywsf51bNDHwEyAn4E7i3AZ4f-CRaZhFs8Y9Dav-l2P4ygqlyG3OM-jWnJGT22QOcsKZiCmak7Xl8OXWTXd8o5FRz0BHCo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم ۲۰۶ شب را ساختند؛ خیابان هنوز شاهد حضورشان است
@Farsna</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/farsna/463738" target="_blank">📅 22:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463737">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6504102bd7.mp4?token=BKQ7jRSwQF8w52wsExzZmp9lwJqlVcUujzdBHy1-QYox2jkgWwumV-As88sGAS3tUuj37ETQ9dawW2fHvxurZqDD2_IeWYcK4PjBUAL65IA8gY6--sei1mNSHD5MkwQMKSYsgHcEP670tEIf31NAl3wgJb08h0JAWMe6NNsDlwwpwYMRBX9V3TigjWvTIGuCacqMCmmv2hFD8QGC3FyCp4XYOiR8OMGlBKEBZAal1ZCbfs2E6sndjlnZNzPPU1wzmZPdsYbt2bE7sMoQDwSJlnLADciRi8wA-mJyLkPYuNM2mUdXpELqi1J9359bgVd_j5BqbsBy3FXHw1wYb8LoZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6504102bd7.mp4?token=BKQ7jRSwQF8w52wsExzZmp9lwJqlVcUujzdBHy1-QYox2jkgWwumV-As88sGAS3tUuj37ETQ9dawW2fHvxurZqDD2_IeWYcK4PjBUAL65IA8gY6--sei1mNSHD5MkwQMKSYsgHcEP670tEIf31NAl3wgJb08h0JAWMe6NNsDlwwpwYMRBX9V3TigjWvTIGuCacqMCmmv2hFD8QGC3FyCp4XYOiR8OMGlBKEBZAal1ZCbfs2E6sndjlnZNzPPU1wzmZPdsYbt2bE7sMoQDwSJlnLADciRi8wA-mJyLkPYuNM2mUdXpELqi1J9359bgVd_j5BqbsBy3FXHw1wYb8LoZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی سپاه: نحوۀ پاسخ ما به حملۀ جدید آمریکا از اسرار نظامی است
🔹
اگر آمریکا به کوه کلنگ یا هر نقطه‌ای دیگر از ایران حمله کند با قدرت پاسخ خواهیم داد.
🔹
این‌که پاسخ ما چگونه است از اسرار نظامی است؛ ما اسرار نظامی خود را فاش نمی‌کنیم اما در میدان عمل نشان…</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/farsna/463737" target="_blank">📅 22:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463736">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmBo0hFuyJHSMuj0DcPV9GbuEVv8fGpdMwhiZocP4ziNEvVV0QiMsBqRvomgXWtg-Yaux2edTcFXutTodumV5FpH58zVzHclDcbUAxA6U6OlL08JcjjwcNIJjX9TVF0PkxAQbR_3zPjvCDmSfZBHzLMBSQbETPAHPx61g7XcLna_MrFleTY5jJBKK8eyHSFlCkJwR_xXn_7FiyOrwAyw-Vv5cx8iHh2I-q4gYtOYZduMtB6MTwdc6gxh8LEGM5c51xZcN3Ek2HTbejOuXEvwDOsuxoYNffG7giQibYp7Vfi8oZeqW8bc4l8CCehgSRppcucplHrLKqbcm6mYCHJIHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش متفاوت رهبر انقلاب برای تدریس درس خارج
🔹
حجت‌الاسلام محمدجواد قاسمی، از شاگردان آیت‌الله سید مجتبی خامنه‌ای: حضرت آقا به‌عنوان استاد ما، این را نمی‌خواستند و اجازه نمی‌دادند که طلبه در درس خارج فقه تبدیل به یک تماشاگر شود.
🔹
یکی از شیوه‌های ایشان این بود…</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/farsna/463736" target="_blank">📅 21:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463735">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6XKUnWyTBTDBuRrAm_QNklHGknyzX2UpN7ADu7rr4TeMeZ9BiGrwgU88y40D4dmLjW-Om1oBNVerxvxZf4woyCK7c7eMblhICyeIzyz5GfnBocmlaz1xGtnSGIjCw2fCiOlZBHt4ckmnbp1dqlZTsS-LhxvwY1eAcVJj7P7yzDN59ak1Ns8Zir7DuJK-bD1Z3cVwdc6rT8cTmXAXQQEDsrFHZ2IqJOVhkuws49KK-NySqK7Isn5EHh-gtGCEI3or9AgmBWQDW7Z_Wuig66M9eJgZuF4VEMpcj09wGM_TooKuCYNS2xsdRy7LYtY_5SOeKmlbYXTTokkeuacpgO7nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز پرداخت بخشی از مطالبات پمپ‌بنزین‌ها از فردا
🔹
سخنگوی صنف جایگاه‌های سوخت کشور: با تأخیر ۶ماهه در تصویب و اجرای حق‌العمل ۱۴۰۵، تسویه علی‌الحساب ۴۰ درصد از مطالبات جایگاه‌‌ها از فردا آغاز می‌شود تا مصوبه نهایی ابلاغ شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/farsna/463735" target="_blank">📅 21:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463734">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f86f57de1.mp4?token=jDG1R-V9PXdmdpncKuH1e-5BCvudpi-kI5d386nyS1javthWMgXHCS4mdF-5R19YJMFZXPtIgi51DADBtGPZhW4N0tSGqV5AjKP_0W0DKFbXQBWnylkXNAjY4Zwq-pgq58P6X_lwdqJ209rv_QMx-CbbMLOqL2aqTSweoYG47GTAQ7kEAaFy88E5O82fi8GjRqfjSbUpLNOraH24xfm-2CvGH9EIOvtnmZT-29HLMtSSP-5DzDArWrkbnS9AxkFohrKsllNXpGYMhAuKeqCnXUzzwmnX_bQ2XR_GdhCZ0GibkvyBWh_3bfAz5T93kXCKA8e-utQWJ2yfTv7S7hgBUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f86f57de1.mp4?token=jDG1R-V9PXdmdpncKuH1e-5BCvudpi-kI5d386nyS1javthWMgXHCS4mdF-5R19YJMFZXPtIgi51DADBtGPZhW4N0tSGqV5AjKP_0W0DKFbXQBWnylkXNAjY4Zwq-pgq58P6X_lwdqJ209rv_QMx-CbbMLOqL2aqTSweoYG47GTAQ7kEAaFy88E5O82fi8GjRqfjSbUpLNOraH24xfm-2CvGH9EIOvtnmZT-29HLMtSSP-5DzDArWrkbnS9AxkFohrKsllNXpGYMhAuKeqCnXUzzwmnX_bQ2XR_GdhCZ0GibkvyBWh_3bfAz5T93kXCKA8e-utQWJ2yfTv7S7hgBUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی سپاه: از نظر ما بازدارندگی یعنی هر متجاوزی باید هزینۀ تجاوز را طوری بپردازد که دیگر آن را تکرار نکند  @Farsna</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/farsna/463734" target="_blank">📅 21:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463732">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a57e6ffd6.mp4?token=isdjZebcTRD3m8QGTuqnD7Y4XjXPMgKVGrn5L7zDsKrqivzClWPLcn65_DUfPcmKTM8KtSgrPOLhliWurk9G_0wtQw7dpOCW3VCKQXm5cv9blPNPvGDVj0OZZYY_OrteVq6Cel5bx2yKrBmXVb9bYQe3D2aHPAMI9QzmhIy8xkVcbjEQi3zH7d8ObWhHHhsmv4_CUBLx_f2QLuma1zRbbwFp_2YqnwhJmVYaooVD_F-fkg9WbbaOGT_HQoVcc42c_sUeJbmpHmjvEY5xO_xQlPBa2fjjj11ktMcs38PoFudh1JuQrLuTUGhD1jwqAjFX-eXjjggm6VgfRbGtFiWDTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a57e6ffd6.mp4?token=isdjZebcTRD3m8QGTuqnD7Y4XjXPMgKVGrn5L7zDsKrqivzClWPLcn65_DUfPcmKTM8KtSgrPOLhliWurk9G_0wtQw7dpOCW3VCKQXm5cv9blPNPvGDVj0OZZYY_OrteVq6Cel5bx2yKrBmXVb9bYQe3D2aHPAMI9QzmhIy8xkVcbjEQi3zH7d8ObWhHHhsmv4_CUBLx_f2QLuma1zRbbwFp_2YqnwhJmVYaooVD_F-fkg9WbbaOGT_HQoVcc42c_sUeJbmpHmjvEY5xO_xQlPBa2fjjj11ktMcs38PoFudh1JuQrLuTUGhD1jwqAjFX-eXjjggm6VgfRbGtFiWDTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی سپاه: از نظر ما بازدارندگی یعنی هر متجاوزی باید هزینۀ تجاوز را طوری بپردازد که دیگر آن را تکرار نکند
@Farsna</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/463732" target="_blank">📅 21:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463731">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">عملیات فریب آمریکا با اسم رمز «تفاهم کوتاه‌مدت»
🔹
در شرایطی که تنگهٔ هرمز بسته شده و همین موضوع، بازار انرژی را تحت فشار شدید گذاشته است، ذخایر نفت خام آمریکا به کمترین میزان ۴۴ سال اخیر رسیده است.
🔹
قیمت گازوئیل رکورد تاریخی زده و جهش نرخ بهره اوراق قرضه، واشنگتن را وادار کرده از وعدهٔ انتخاباتی ترامپ عقب‌نشینی کند و نرخ بهره را بالا ببرد.
🔹
در چنین وضعیتی، به نظر می‌رسد آمریکا دنبال یک تنش‌زدایی کوتاه‌مدت تا پیش از انتخابات میان‌دوره‌ای است؛ همان چیزی که کارشناسان امنیتی و اقتصادی آمریکا هم در فضای ایکس بارها به آن اشاره کرده‌اند.
🔹
نشانه‌های این تلاش حالا دارد جمع می‌شود: کاروان سوپرنفتکش‌های سعودی حامل میلیون‌ها بشکهٔ نفت در خلیج فارس پشت تنگهٔ هرمز تجمع کرده‌اند.
🔹
قطر انرژی هم نفت خام میادین الشاهین و قطر مارین را برای ۲ ماه آینده با تحویل قطعی پیش‌فروش کرده است.
🔹
دیروز سخنگوی وزارت خارجهٔ قطر از دستیابی به یک توافق کوتاه‌مدت میان ایران و آمریکا برای شروع مذاکرات خبر داده بود.
🔹
جمع این نشانه‌ها این برداشت را تقویت می‌کند که واشنگتن می‌خواهد با یک تخلیه تنش کوتاه‌مدت، قیمت‌های انرژی را تا قبل از انتخابات میان‌دوره‌ای کنترل کند.
🔹
به نظر می‌رسد این طراحی آمریکا برای گذر از ۲ ماه حساس پیش از انتخابات است تا آنچنان که برخی کارشناسان می‌گویند، تشدید تنش را پس از انتخابات میان‌دوره‌ای از سر بگیرد.
🔹
مجید شاکری، اقتصاددان، هم می‌گوید اگر ایران تنش را تا پیش از انتخابات میان‌دوره‌ای آمریکا تشدید نکند، آمریکا پس از انتخابات تنش را تشدید خواهد کرد.
🔹
در مقابل، جعفر قائم‌پناه، معاون رئیس‌جمهور، معتقد است ایران پیروزی خود را در عمل به اثبات رسانده است و اکنون نوبت پیروزی بر دشمن با رفع تحریم‌ها و فراهم شدن امکان صادرات آزاد نفت است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/463731" target="_blank">📅 21:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463730">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a801167fbd.mp4?token=YmkcXDFGK8PWzJmlzgHdLuCWgC9ihlmsR0TjHMuvXVc8UusnjUybSYJQnR5bBgfo4NLab-r_djy_6dB7oMU5wHniqOnt7qHnb98QeRsb_mch81_QI5JqKTHa529l_4fUUHLEDydDjcsX5shPkwm6-7OGo-xR8kLW7iVtAoyoVohtiMl0fL5jbK5bk4PBejdSOT7ouTyQsYfZa_reUGy1WpRkXvtplMvPEgzD70lOqkVXZC4LjMwgyCwipxNZ1nQa0ORQOhcnjpp7Dpn_-ZUf_-SiI9goUXHqevdGPlK4Zs7AJNxo71ouC-QdIgFWNtYL3Mol_ESrWsD-aePR0WaXwZXrDzGA6dcPHbl_SmeupeJzjsqEHfm0Da2Jbb-aHIImzOGR4wcKC8np84WaJ6H9GtMN6SCES_o4eWNND58hDFIsjuSrn0efEybXp63vVQmvxkiE8mKpknuLZ0Ux2zFWXBmfGw0EqkptxuufZyGyqvJOw7oCdRiTF86GbwprbSWpAwuHQJo4qnWetp_qDk4YBQAa2wcVzlYLe0AK4dAJmtmfKXwmRNQGmME1X8M1IhOQOHOMROcUknDS2MTTaR5xJum_0sxlzPjm0gmChVcnbd3pMUUr-JpcG3LoZQ5d0goqzsT1a4TvL69ZLAyehB6dPB3jFezd3rvrEtSChz5DnbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a801167fbd.mp4?token=YmkcXDFGK8PWzJmlzgHdLuCWgC9ihlmsR0TjHMuvXVc8UusnjUybSYJQnR5bBgfo4NLab-r_djy_6dB7oMU5wHniqOnt7qHnb98QeRsb_mch81_QI5JqKTHa529l_4fUUHLEDydDjcsX5shPkwm6-7OGo-xR8kLW7iVtAoyoVohtiMl0fL5jbK5bk4PBejdSOT7ouTyQsYfZa_reUGy1WpRkXvtplMvPEgzD70lOqkVXZC4LjMwgyCwipxNZ1nQa0ORQOhcnjpp7Dpn_-ZUf_-SiI9goUXHqevdGPlK4Zs7AJNxo71ouC-QdIgFWNtYL3Mol_ESrWsD-aePR0WaXwZXrDzGA6dcPHbl_SmeupeJzjsqEHfm0Da2Jbb-aHIImzOGR4wcKC8np84WaJ6H9GtMN6SCES_o4eWNND58hDFIsjuSrn0efEybXp63vVQmvxkiE8mKpknuLZ0Ux2zFWXBmfGw0EqkptxuufZyGyqvJOw7oCdRiTF86GbwprbSWpAwuHQJo4qnWetp_qDk4YBQAa2wcVzlYLe0AK4dAJmtmfKXwmRNQGmME1X8M1IhOQOHOMROcUknDS2MTTaR5xJum_0sxlzPjm0gmChVcnbd3pMUUr-JpcG3LoZQ5d0goqzsT1a4TvL69ZLAyehB6dPB3jFezd3rvrEtSChz5DnbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم مبعوث در شب ۲۰۵ هم میدان را خالی نکردند
@Farsna</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/463730" target="_blank">📅 21:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463729">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b504b9fd0.mp4?token=tm2WE4PQfOuT3MwaJv7qlEduHS6-B9kEVgqlTHt3COvHCd-1FXiP40S-spKHIuVvPJjIBTWxpqsGzpLXb6xndcSnPz8BMFNwu-y_sk4jPCjuiMZvyFY3HOfekyazPLenO0lNHuKEOL1ft1Q5DSr2VsxVVsR3pR6LdU5gg1ZZ-EzG2X1cl1LEpWSaXLCcQ5CJD3TEAzXDPKgGdOyyvaYZW28d87cvJKlrAXS8_XEKR-ib0YbiCKIQxn1KK6XR00-ackNU0-4Rk_mEvyr70-xfL5NkE-EHexOnVWZ2O0auqcaY1Qj4Rp3UKTzakb2ihMUhBr2KNCvaS0ksRfp0mqhqog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b504b9fd0.mp4?token=tm2WE4PQfOuT3MwaJv7qlEduHS6-B9kEVgqlTHt3COvHCd-1FXiP40S-spKHIuVvPJjIBTWxpqsGzpLXb6xndcSnPz8BMFNwu-y_sk4jPCjuiMZvyFY3HOfekyazPLenO0lNHuKEOL1ft1Q5DSr2VsxVVsR3pR6LdU5gg1ZZ-EzG2X1cl1LEpWSaXLCcQ5CJD3TEAzXDPKgGdOyyvaYZW28d87cvJKlrAXS8_XEKR-ib0YbiCKIQxn1KK6XR00-ackNU0-4Rk_mEvyr70-xfL5NkE-EHexOnVWZ2O0auqcaY1Qj4Rp3UKTzakb2ihMUhBr2KNCvaS0ksRfp0mqhqog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گلایهٔ‌ وزیر صمت از خودروسازان: مردم از کیفیت خودروهای ساخت داخل راضی نیستند
@Farsna</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/463729" target="_blank">📅 20:59 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463728">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbe171e06.mp4?token=Rc429BVSGorPy_D-clZqu9jwAwLFYRakkTDwl4DsT9vpxcdlqGr-g9EyYr5Zsp9c3PThreA0_Iqs702qhxHiOqxqVIcL71dOF6rSBaa4Ke2yyGFyX9rdx4Y5W4LnywR2MVID42C-PV8gZUSljrTLSIQwW-w8dYhsHFCxn2DyYcIPBiXnHTUWAqtgQWZo8uqcxvu1Oms726scSS15QjOrMExnPua9HbNeASek0J8ZEh5P2yvUPQ5IIbApr2v7hWFzJAUJR7QKsp6TR38Kl_i0s0WxW7uKybYBqchNZMCKlfyi_wRIoIK9PxTj2AYj95CejXIzPdIMo94SNx2qeuj6aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbe171e06.mp4?token=Rc429BVSGorPy_D-clZqu9jwAwLFYRakkTDwl4DsT9vpxcdlqGr-g9EyYr5Zsp9c3PThreA0_Iqs702qhxHiOqxqVIcL71dOF6rSBaa4Ke2yyGFyX9rdx4Y5W4LnywR2MVID42C-PV8gZUSljrTLSIQwW-w8dYhsHFCxn2DyYcIPBiXnHTUWAqtgQWZo8uqcxvu1Oms726scSS15QjOrMExnPua9HbNeASek0J8ZEh5P2yvUPQ5IIbApr2v7hWFzJAUJR7QKsp6TR38Kl_i0s0WxW7uKybYBqchNZMCKlfyi_wRIoIK9PxTj2AYj95CejXIzPdIMo94SNx2qeuj6aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌و‌هوای دانش‌آموزان در آخرین روز تابستان
@Farsna</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/farsna/463728" target="_blank">📅 20:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463727">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a6009e251.mp4?token=RC-3qqOLoO_qUgh182MlK2wjOJkajNfGUDrWm-Rp1QlN38wLPYh2AFqYIDdiGdl5-v2KRwkMg-WIoFhSCW6EvF9EIX4f2OJ-2UX_SuLcrGA6EiAdY1I0OiyUbySFePDUj9ei8v9CdlwyxaGVVicgiM4ltXhc2xgo7dmmVZPqTI5G4hVimDzd1cAQ7SMQcWjQv0pubzSCinfdMxMTz_mH4RtCOTD9SDCvbiFtidf3nAX9368w3ayoRBvP3jbALdFT4xeWsVmyYrN5NMuo5FR9JM9ySrMwFR0s-mFXkoZpC5nJAj9EQwNZ59zHILXNJ69uwYbqn7vII6KKozDjJXfHeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a6009e251.mp4?token=RC-3qqOLoO_qUgh182MlK2wjOJkajNfGUDrWm-Rp1QlN38wLPYh2AFqYIDdiGdl5-v2KRwkMg-WIoFhSCW6EvF9EIX4f2OJ-2UX_SuLcrGA6EiAdY1I0OiyUbySFePDUj9ei8v9CdlwyxaGVVicgiM4ltXhc2xgo7dmmVZPqTI5G4hVimDzd1cAQ7SMQcWjQv0pubzSCinfdMxMTz_mH4RtCOTD9SDCvbiFtidf3nAX9368w3ayoRBvP3jbALdFT4xeWsVmyYrN5NMuo5FR9JM9ySrMwFR0s-mFXkoZpC5nJAj9EQwNZ59zHILXNJ69uwYbqn7vII6KKozDjJXfHeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اینستاگردی جولانی حین سخنرانی اردوغان در سازمان ملل متحد
@Farsna</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/463727" target="_blank">📅 20:48 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463720">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fUtHdFG0tAoSDvoA_Hn97lbp5ywD95K2qiFJcBuwrWsBRxxffDYiHec3EIqnhm2g8xg8jJnEs5JPFOx6FiZDzmd0y6oyZ3TS4bLt6M6lGV5Jd6eKXaWEnIh_1Hg8eU_Nf2o4tpbNWZi31c-19pT8vgnjwmjCYOYhPTQqQYn5pEwHUdexuiVr1zLEZWsZRn433iODl69SEaIQKtR8-xbs2sURUciBUChsL8jA6WVpRqQZ6VNuIGlKz8RbYd598V08frFZrNQB8pkZzqPfzTKy4aj3jdtqsOnZalk9BzI_28lzumsRe60NNXuNqZg1sHE4u9TXAZVKfAm1yULA2jF52Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/leXQQZObcbcWRo0CAZgZFNDnMLfNzTcTKdHo15YPznN6dTXPsZUC9BykYc6m129CNjpAPJXQdISZb2spl6Im-SM3K5WgSI0uZGx7UyWS31c81YPW9AGBIvpgzAKhski62hgmnhOFOWm-qhDgocmva6QCQcB65SDzKRUFa2y1x8T_FZ6fSWIxWrwapzOIVSMDQhS42ujXCtsQqZeaaG65hqIyErQBZwb2tcUYVcI1TPUnUbZ4_Qgu4LWdKYx2iEzVxytjcCWbFD19Y9mnnxwP6fLOx_qH38eORU7xZqOX9ba7NNFBlyQqdKCydb-r9lCUsZ6pcIznjVEvk2pCwb3nnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h3HgM65MSyZB66jdpLF4FSraYLIlkddnC5tLArB5zUluRr4Z_upsRQb4Ec8bZCNpinb-P_IGJ07dbrGOQ3nPAqwRWT4FTPy766BjR7lJzt9WrQxNnc9ehtOa9trpWHmbnvgkLDGZhvNUiyf09X1RML_NRhOoeop18sJwY_nAUxLWQDg0X9V-J7-0sRXf8iJMso9_-_-d1qR0xir32fKed8VgHiLKhZChMxc2XfxnyftpV-5fhQfN6OvnKcqk6n-ksdkR90kcT59xRgKo0BQr4U4jqT_B3LRxzP12UV-5k3xCZT2iIXomPWDZ6axEsHQnfo79aONQs0XeSrJWE4ZQCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ISsQW0Ip9q4GprUkHaIQfaXMmRYjSRXH8ClwmxBDNoVAM6eWhS84Q15MVRzDdWp0DAJb2R0F8-kl3rMxGc8eXqHkoR4I40fjU46QaoWSN0iwyFoFRGMgiszdADtegE4fOKY1fKkDirdayJfaCItmYOX0vhqWD7BFqOImHtppjQCaQpoz_7CfsQcrbc1EpN8Lep3qx4apmxRvFiB7yE0aQO45vyT8M_9SW75fwxNs3VBwlgWpS10Vq_miExRX0sIERoORanD6ije58r5iS5PyC5F-mY6iL52pI8MAkW_VT9GfbgpygAdqa4R3B9ZLTWyej-WDDpKHU95HS5TqnpzJMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U-p8SrHj5fxu1xwIMWYmh_vEZ3Ez_BQpU27HBx-okGhE0vdfCuJsyzixFfUg26Hd97FwzJGcNh6SHxbLLWIwXqdWsDDooiCBNE9ULemyvK56gjHK6NdJKGPZWX6JDz5nhsgGAVjOhS-4CdUVqx9ZnOWkgi5kvMyTJL2AP57bAcLgPFY279tlf_JxWcIlHmJfZH1eiq7qDXSsKcNr2ir9WPaO9E2oVkUAE3-34eukheuLGJzHgfsGM-J74QZqgdpN27YT4mfoGUd2xc2uSloRc33JM92l7toelSnrzJqPMQPKBuJdsJSrF5-CntrN1eQskegSK_-a4W60mSjNxdPecA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fhzW324hnmWakj_wmpD7YP1M84am5IKDCVVWl6nz8vqndzbtHutTM58OmliM3jX7N4sw3JfdQEaWc-mKlXR_IllopUhJd-Waus_ugzgizksOrXcpiGavuPP_rK9HVekbalyWYe4NEt6VmXdbIs9WyYH-03eFBQ32F4rU62lWySl3lLozWRf605QQka39p9Jbc2JsnvQeiF2c2O3IJiPxezUzDwBctRJZq70DaY8ruQkxD2nzw26P1AU47fj96-wg4TLxEeCcCcGSFwGXfCjWgmMy4X3i7mIeRsMKAvkMDVqk_QnWUO-1qFK9gGMz04CpC00EGrTHlJ5LZH-XNhNy2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K95ZY9ANvIdt6bl63oNtX0e3ayIZWhnzl5-JvoPpYGLiOJk1bGkNJN6jTjAnRQpoz7TCZ2-cuDLZVx5GdpXD6fH4gsMyUXH9Xs1YfIP2l9K0auaGqnadoTvwSYw92zFrIfYdEhdJB6aa4pg5eCBQSFpXwFd59ASALcHrZmuQe9UekY5GXACLW-a1nLznW_9S9c6t1buiGsqvulruCQQdeOt9MRQPIitNh-J8A58AWi73B5lAbqL6SIKhnXcEifz1uwU42T8tWk_wjI1JPBKewf3aFAz6vWxstBRtH1FejYLzrAaNlDx_4uCOGCNv3IV4TzS7FVcizQa8UQGN87Oagg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
رژۀ موتوری و خودرویی نیروهای مسلح در همدان
عکس:
مبینا لطیفی
@Farsna</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/463720" target="_blank">📅 20:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463719">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kLfisVFsZIBvxpfjoFV80eBLcGStjCXWRNjw3nFS21n5O_aPFdrSjmeV9um-ttoLhPXGxcZqORTx1NUoJkpLPsg45b6hIDPHA_kJYg-5aD6B0IeRuOQiJkQsHU_C6TEWeex74tQ0XVaEh2T6VE9NYGGvyxkee91IygT1JAEqfHv6khZH7qtpFjiel4N3TJiaoZinoWt_jZBaBd1Ofj01zxfDyR8C5DQcy5NTG_vmoCB97vWMYlNfZGgj-DTuf2HCSynNEw8s3LV5dGmFeaoU-FZXG8OYNJGt2EXEalMHUW4uQx4SeNoHq6F6d23rWuwzvDGBO12saPBmHXpmHSO5JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی نیروهای مسلح یمن: جنایات وحشیانه‌ای که دشمن سعودی مرتکب شده، عواقب وخیمی را برای آنان به همراه خواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/463719" target="_blank">📅 20:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463718">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rLDotHKC9WSdLH9LqNPh_7F_xyHcJ5DnwJnakjxp0nErSi03mHF4s93su_lNeCshbEyluz_R1sGDAhvumhHKWWxx_Eclgv2bBnHSMPkHypIqIQk_4ekud4lzu1R17xBOrvhktx4KjiWYlc9wZ0OfOjUQEYZk1cHLpQytG948w3QZ2JCs72SlXM4k3536LZiULW5eIg_PykLbOdqIwNNm9qUEThQqTNh2amC9ajcpizLb-oih3KoIr5S60X1DDHw1uwMgVOsoQPjvaVnbjxUkP6GsDMsKfHEpUEGEuDjHEiUGx5ppAH0y6h9hlVm_X7JDLjcNeJvdi9a7qLZbn3n6kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
حضور زاکانی در گلزار شهدای دانش‌آموز میناب
🔹
زنگ آغاز سال نو تحصیلی مدارس فردا با حضور شهردار تهران و از جوار مزار شهدای جنایت آمریکا در مدرسه شجره طیبه میناب نواخته می‌شود. @Farsna - Link</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/463718" target="_blank">📅 20:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463715">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AnF9ySwvjgQ3rbHV2Y0n3mUKdkoSHHfv1XZKI60aa7RpBKdd9d0SXdsut0bTdX9VpvPG8CihR0ub-kOk_qldMUueLG6LTYit5O7zaqo5_fTTkEsQPcGgodtA2HnpKdg_gRD8rgqprvBBy-ZFUgdgWFdg3PtrKVk63focxvg-j4tdb5su9E5GdQb0AaWCmYynLIAVICTdUz5r67eHTePdJR9zQzTo_vnBFFWDHt1QwPsGmRz32LpF3rk7P4WOFphFRYjsTOkaSvE9k5dsXzqrwawhk8LqKTR22hknaS_pSv61NDxKhHBLVhtUojI_T7LseGVBJEocwrSZgPNaSepZjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CwWNsOVbFp2oSt23vkvEEJLsXqY2RTYioevI98rXSUnWYnXx5G6_wKxvIUseEdHL2mA3W2Jns22q2dS9NXA5GT4Mw_tW6lbKsL4j_d7Bkg5D7driXckWBTZOlqEYtQGrn_Rs6D2HlnXDXXnJQ_CDRgVQKkuxXUYzfHJtuH8H_Hx3scb6-EL3EQ6HLAhvY7NIn_9n5XnENCsC5BHlXRXsb5xWKEitZ5Q7dbR9kRqtc0G77CNrNjbDoNiJa4xnbqsZEcsrX1Itb2rCDjJ4SFjfA8LnBODxw1FnmeLTEmDzug9kKF3su3oH-NUOIAvGId0tXnlpA1PHMmYF4NcuEv3ejg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1de3dbf71c.mp4?token=fYbODYJNeDSVPE4OIJrzIqoBRzrUuMAfnsziGDs6985RNvLRetjemuKaJ7s711MrTaSM17hlPZjWgpkohut6q5nmHTtygRfn6E2x_yxlfRB5gsJ3WsAGUAd2qYG9h5xmapDSpc98fOQijxxiPigCsK5uqHjbDenBYPUBfuImpmUGtbBkXbV1_jPyK8EGqSDJ1tmEG2cWFYX3DsXgwrknQAyP8zFO2vFSS1GUuQa7fIvf1M1fMw0KHzHVKAWeHwGbzn8WtuOx35fLY2ZrZ-nYa3l6kdde7rFIn9Wr3L4KnynQY3r13KuOfPNHH4jbo0DkQ36N_Q4HEyPFkQHp2CNejQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1de3dbf71c.mp4?token=fYbODYJNeDSVPE4OIJrzIqoBRzrUuMAfnsziGDs6985RNvLRetjemuKaJ7s711MrTaSM17hlPZjWgpkohut6q5nmHTtygRfn6E2x_yxlfRB5gsJ3WsAGUAd2qYG9h5xmapDSpc98fOQijxxiPigCsK5uqHjbDenBYPUBfuImpmUGtbBkXbV1_jPyK8EGqSDJ1tmEG2cWFYX3DsXgwrknQAyP8zFO2vFSS1GUuQa7fIvf1M1fMw0KHzHVKAWeHwGbzn8WtuOx35fLY2ZrZ-nYa3l6kdde7rFIn9Wr3L4KnynQY3r13KuOfPNHH4jbo0DkQ36N_Q4HEyPFkQHp2CNejQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
عراقچی با مسئول سیاست خارجی اتحادیۀ اروپا در حاشیۀ مجمع عمومی سازمان ملل متحد دیدار و گفتگو کرد @Farsna</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/farsna/463715" target="_blank">📅 20:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463714">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y6eLm19OD_De26Fct_3gZ8mzAPPuXiDXGGjktt408ylnxqh2b8Opwkoq5pGJMVwvFKjWpVEvxgXyTJ3gB377fQZML832zV-afhQWZvn1k2rxVSo3QLYHOqhVH1N63bwILsd1iD4vR4yGVIf079Lgvhh9n5tfRrYLkyTQBl0H2JKSab3fgrYZVbktJ1kNf25EI5b9iBtltB37RxEulDsZu78S9YyRh_ldeyORWZtrU4sQkbZV_tEL7rJV-lSgJy2x8wtER_RBJgx5pjE4dX48IRKJhGcNvx-7cic4Nf8cQtACe-A42i3SPyC9J53XIhsdGMWLaJ5xmRtp9Fv4fLp6RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غذای متبرک حرم امام رضا(ع) را چگونه دریافت کنیم؟
🔹
زائران و مجاوران حرم مطهر امام رضا(ع) برای دریافت غذای متبرک رضوی می‌توانند از طریق سایت یا اپلیکیشن
نسیم رضوان
درخواست خود را ثبت و وعدهٔ غذایی موردنظرشان را رزرو کنند.
🔹
متقاضی ابتدا باید وارد سایت یا اپلیکیشن این سامانه شده و از بخش «پیشخوان خدمات»، گزینه «مهمانسرا» را انتخاب کند.
🔹
در ادامه، در صورت نیاز، شماره تلفن همراه در سامانه ثبت می‌شود و پس از آن امکان انتخاب وعده غذایی موردنظر فراهم خواهد بود.
🔗
هر شماره همراه برای چند نفر امکان رزرو غذا دارد؟
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/463714" target="_blank">📅 20:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463713">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgPvUc3iw_Wryw88m3UZ3-SVnQFrZLTd572SbRmZGJRckCq0xpoS1aoP5-7V6dzCFEcWQpYgm8vHnRiVb2uXKMh5VzPn1x_ZgGkhu8HRip-X1pBXfg6YNXdZEaBectsBFUKjMjPrGuFYcPGxaZYGg0nZe8M-j1c4LwmVJkt2CxUitH6rD3mAQHuKHPUKCGD5cp4QNcYLShw34U6rvGV9wQtZkdmVthbGejLMj3ScHBYmR6gwhpx_rRp73UkXiatMSvuQ6cg1Vf9LyybN32StsM17DTMj8U0hqdJgJkDPJv2nCOVpI42wA56dlNC_DjPxoTZ3u-5GF0H3sq-VfQXX_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعت کاری جدید ادارات از اول مهر: از ۸ تا ۱۳
🔹
رئیس سازمان اداری و استخدامی کشور در بخشنامه‌ای ساعت کاری دستگاه‌های اجرایی را از ابتدای مهر تا پایان سال جاری، از ساعت ۸ تا ۱۳ تعیین کرد. @Farsna</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/farsna/463713" target="_blank">📅 20:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463712">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XG1pU-u--DRzWXzfOLI5AHvxrkGFXftKlvgnqNszrEQ_M8irO1HgeXVFemicoX4MkqXaVQ3Sg0Z0iso9zIKFavTeUrNw2m-VsLXEhJcgQ8djqGO5fjU2FoMvNb8VMUw9tHPXgT3_FB_ze6JMHhX2wF_kQszHY_9IG66ySzEDCXUUMY5UI90gAJDlrwYgG7jy-h1pYwpRg0Ov5qFFdTZpS2-TkodhjU-q1raGjoFPrl0fCDwEgXYJNAlT_XhwVyvr5GxFGezkMuS-yNRKVZZRREqFmutGuxDK6Y7XuSQJDY8xFkuoELh8XauCJH0gxL-nH2MiBFu4JsuCo7uc9sKpMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دستخط رهبر معظم انقلاب خطاب به سردار سید مجید موسوی فرمانده هوافضای سپاه
بسم‌الله الرحمن الرحیم
🔸
برادر مجاهد و دلیر، جناب سردار سید مجید موسوی، حفظه‌الله و ایّده
بعدالتحیات و السلام؛
🔸
۱. بحمدالله، گزارش ارائه‌شده که قبلاً هم نسخه‌ای از آن را دریافت نموده بودم، دلگرم‌کننده و دلنشین است.
🔸
از مجاهدت‌های خود و همرزمان گمنام و مظلومتان خیلی کم نوشته‌اید؛ همچنان‌که رفتار مخلصین همواره این‌طور بوده است.
🔸
امّا اثری که به حکمت الهیه از این خصوصیت ناشی می‌شود ان‌شاءالله، محبت و اعتباری است که حضرت حق جلّ و علا برای صاحبان اخلاص قرار می‌دهند و انواع برکت‌ها و پیروزی‌ها.
🔸
۲. در مورد زنجیره تأمین، ان‌شاءالله تلاش‌ها ادامه یابد و گزارش آن مرتباً به اینجانب منعکس گردد.
🔸
۳. مراقبت از جان عزیز خودتان و همه برادران خواسته مؤکد اینجانب است. امید است با دعای خیر و پربرکت سرورمان، عجّل‌الله‌فرجه‌الشریف، امور سامان گیرد.
سید مجتبی خامنه‌ای
۱۰/ مرداد/ ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/463712" target="_blank">📅 20:04 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463711">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">📣
ایرانسل با نوسازی مدرسه سنقر به استقبال سال تحصیلی جدید رفت
🔸
هم‌زمان با آغاز سال تحصیلی جدید، ایرانسل با بهره‌برداری از پروژه بازسازی و بهسازی مدرسه‌ای در سنقر کرمانشاه، گام دیگری برای توسعه عدالت آموزشی و فراهم‌کردن فرصت‌های برابر آموزشی در مناطق محروم برداشت.
🔸
در این پروژه، بخش‌های مختلف فضای داخلی و بیرونی مدرسه، بهسازی و محیط آموزشی تجهیز و زیباسازی شد تا دانش‌آموزان سال تحصیلی را در فضایی ایمن، استاندارد و مناسب برای یادگیری آغاز کنند.
🔸
علاوه بر آن، بسته‌های حمایت تحصیلی شامل کوله‌پشتی و نوشت‌افزار، در اختیار دانش‌آموزان این مدرسه قرار گرفت.
🔸
ایرانسل، توسعه عدالت آموزشی و کاهش نابرابری در دسترسی به فرصت‌های یادگیری را یکی از محورهای سرمایه‌گذاری اجتماعی خود قرار داده و در سال‌های گذشته، مجموعه‌ای از اقدامات را در حوزه احداث، بازسازی، تجهیز و توانمندسازی مدارس اجرا کرده است.
👈
جزئیات بیشتر
@irancellnews1</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/farsna/463711" target="_blank">📅 20:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463710">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-text">✨
طرح ملی «زرین تأمین»
🟡
از دارایی مولد، تا تأمین سرمایه‌ای پایدار
🔹
بانک رفاه کارگران با طرح «زرین ‌تأمین» درگاه مشارکت
«صندوق مولد طلا»
را راه‌اندازی کرده و از این طریق امکان
خرید اقساطی و ثبت سفارش طلا به‌صورت ریالی یا مقداری
و بازپرداخت بهای آن در
۳ قسط ماهانه، بدون سود و کارمزد
را فراهم می کند.
🔹
بازنشستگان و مستمری‌بگیران عزیز تأمین اجتماعی می‌توانند با مراجعه به نشانی اینترنتی
refah.zarrintamin.ir
اطلاعات کامل این طرح ، نحوه ثبت نام‌ و مشارکت در آن را مشاهده کنند.
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/farsna/463710" target="_blank">📅 20:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463709">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/farsna/463709" target="_blank">📅 20:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463708">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2DAfqqW-YblZG91bEB8tiCS-Um1n4n8HoJFmNCk1R8Yt1daXpRM7a8FIEuCUC_PME3fwnMxbUmB9k5gpZI7eFoOYTUV_7kgW47LQSeGXbX9Al3rJGz91rWzw01VOWHO3puwzQmK9hH0SzR_nvB9VN7okkP9co7tiTlyWkRQtlpTUL9a8AHn6oU1UWZqBJUL_4B4LHkpTTYQYBplp65RiJwKylfVF0zfYEM7ehbGmtkGrCm45rEVM_LSRN4wR0GVcRUFS0kKhi2nSMc5ygSb4WQzv17OMzKbuu4dg_saXmVDyLDMWWaVklhY0rvqK7uFT4GoJ7ioMcJPNtrYmmyN3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنبش نجبا: به کوری چشم ترامپ، مقاومت عراق باقی خواهد ماند
🔹
معاون نظامی جنبش مقاومت نجبای عراق: مقاومت باقی خواهد ماند و الحشد الشعبی نیز به کوری چشم ترامپ جنایتکار و دلال صهیونیست او باقی خواهد ماند.
🔸
منظور عبدالقادر کربلایی از دلال صهیونیست همان تام باراک، فرستاده آمریکا در امور عراق و سوریه است که پروندۀ خلع سلاح گروه‌های مقاومت را در دستور کار خود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/farsna/463708" target="_blank">📅 19:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463707">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWazl88lHpG_C5TdiAXZtZNUBRbUHD2vjq9xmEVgJ-mHiojLucvcVuMSJZb0-MD5svndo9_gS45DBtPSCL3GKivTimrVkxVPlGtb-jOYjy7lKTs0kPMU-Z_AnvcMjFrns-tmsdpSifvZsjjEmWi5j47UGE4grnkYRD60G_RY4KCfsYJg181SO1Q5KtphSf3Qw-WqLYYW0Lsft71ProWM2dcThfb1Vct0csAooQtwiAgYCF1ch6L2aO2sIkSW9EmmIikP5TyUzuJu2MM72w3wG1-uI_wN1eCyT30R4goaetk_Ey1Gj3onEdQRkq1j6ImdnhXHWI8qBOpnQeGxXcuvkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چت‌بات چینی پاسخگوی شورای امنیت می‌شود
🔹
رویترز: شرکت چینی دیپ‌سیک قرار است این هفته در نشستی با شورای امنیت سازمان ملل درباره خطرات و پیامدهای هوش مصنوعی توضیحاتی ارائه کند؛ نشستی که هم‌زمان با برگزاری مجمع عمومی سازمان ملل در نیویورک برگزار می‌شود.
🔹
نمایندگانی از دیپ‌سیک و چند شرکت هوش مصنوعی دیگر از جمله مون‌شات برای مشارکت در این نشست دعوت شده‌اند، اما لیانگ وِن‌فِنگ، بنیان‌گذار دیپ‌سیک، شخصاً در جلسه حاضر نخواهد بود. سم آلتمن، مدیرعامل اپن‌ای‌آی و نمایندگان ارشد آنتروپیک نیز قرار است در این نشست حضور داشته باشند.
🔹
شورای امنیت قرار است درباره نگرانی‌های امنیتی ناشی از توسعه سریع هوش مصنوعی بحث کند؛ از جمله احتمال پیشرفت سامانه‌های خودمختار و دشوار شدن کنترل آنها توسط انسان. این شورا پیش‌تر نیز در سال ۲۰۲۳ برای نخستین‌بار موضوع هوش مصنوعی را بررسی کرده بود.
🔹
این نشست در شرایطی برگزار می‌شود که اختلاف آمریکا و چین بر سر نحوه مدیریت خطرات هوش مصنوعی ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/farsna/463707" target="_blank">📅 19:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463706">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MliiEpeeBvMZ5pMu4g_hfq-VxgEI9w7aSJDI3bBrQpupTwhw3z4RRqeOjJyyETxzABbZfC9kEgj7H3UFgTyMKs6Lqftbjje3GhhXYF41J9GHTyeCc9FpWI7wXThdma8Dqd7ytJfPrlEUToIsuUgOvr7AlImrAcNM_z1Z-zIqyzJdIbP9nTXkYIb8FIWnGjOW4xEK9C3Q8QfMjI_u0HhCWuJ6oh-LwJlmRI1aqPwN4zPFxblxkee9y11ZIMLPI2XUTgaHDDMndoFiAZIh4C6EPe8CPXx3B3wPs6hSNoWXnbClVjLyGDKRVWqIOWKjQ9HSXWl2dCKGrZoSN6Q1CkpZwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یمن: عربستان عامدانه به زیرساخت‌ها و تأسیسات غیرنظامی حمله می‌کند
🔹
رئیس پارلمان یمن در نامه‌ای به سازمان ملل و شورای امنیت: سعودی‌ها در کنار محاصرۀ ظالمانه، عمداً به زیرساخت‌ها و تأسیسات اقتصادی و خدماتی نظیر جاده‌ها، پل‌ها، مساجد و مدارس حمله می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/farsna/463706" target="_blank">📅 19:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463705">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFXc3Qn49XqS_c2pWefbH7ifxKL1GCGGnBIRdnkRP8CP4l_nr8nGfO2uTfJIDi4anynVfBBLpWaB2aESqlL-5SmqImKumUiFu_mi2mlQuC1csL1D4O1sSic6yy8QiDtS-imBAus9-oFsa1l4HLh86pEiu2rwFJLTUEnPHxX3T8NbFrofzwsKnrXen6trW8Q8XktVpd0pQqDGIsI9a6r0MElXbUG28Bq5i0si0uaoDNNoCt29R2i6eawPRHMVQCVDkzYUju8cPRjFinBkdFldOgzbBB8xw6xA2A6O9BTkrdufpwT1Uo3A3OZZNJiy0tZYYVoLytHMYsd-IuCrVtgfRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
عراقچی در افتتاحیهٔ هشتادو‌یکمین نشست مجمع عمومی سازمان ملل حضور یافت.  @Farsna</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/farsna/463705" target="_blank">📅 19:44 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463704">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e550a00fb.mp4?token=Zj1eDvLN-cXxLee4Fe_o-CeCaS-4nK0L6p7Js87O7b6Ay2Z0XTexmmI1wc656JTPobVtHeiEjd9sD5zYcj5I1z-YNWeLYVBC1CXdaFTj1ZrejE4etntlHfaz49hqJnszCyJ2tBJHpY73tIZsYQx3uXNNPJaGNeIv28CGQ8jhEWstP2rdeY5IjWS77BPkuXbp2QNYAHXjGXEXoLbxyOheimAHXOxTWfnZVs9YD_2Fb4sngjnW3PwdKSaYayfujgXaHmcNFYKmh-yh_ENN3gN-7oljWOL0ohSXa9WAHdkAKnYWbLCmJubyh5cpyz_niRf_w1L5KiWZsk_cFhu37ihALg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e550a00fb.mp4?token=Zj1eDvLN-cXxLee4Fe_o-CeCaS-4nK0L6p7Js87O7b6Ay2Z0XTexmmI1wc656JTPobVtHeiEjd9sD5zYcj5I1z-YNWeLYVBC1CXdaFTj1ZrejE4etntlHfaz49hqJnszCyJ2tBJHpY73tIZsYQx3uXNNPJaGNeIv28CGQ8jhEWstP2rdeY5IjWS77BPkuXbp2QNYAHXjGXEXoLbxyOheimAHXOxTWfnZVs9YD_2Fb4sngjnW3PwdKSaYayfujgXaHmcNFYKmh-yh_ENN3gN-7oljWOL0ohSXa9WAHdkAKnYWbLCmJubyh5cpyz_niRf_w1L5KiWZsk_cFhu37ihALg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور زاکانی در گلزار شهدای دانش‌آموز میناب
🔹
زنگ آغاز سال نو تحصیلی مدارس فردا با حضور شهردار تهران و از جوار مزار شهدای جنایت آمریکا در مدرسه شجره طیبه میناب نواخته می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/farsna/463704" target="_blank">📅 19:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463703">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۳۷.pdf</div>
  <div class="tg-doc-extra">2.9 MB</div>
</div>
<a href="https://t.me/farsna/463703" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۳۶.pdf</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/463703" target="_blank">📅 19:39 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463702">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2n7KjUjQKfrPXG1VWX29y6gIMtznPfBwTsycVABq6VZKQSSN3dInUUC6Peqn8I7HBaYf5nj631ONzcNrEbRP3whUJsmY08e5AxRnadsaDUH00SM8vHrGD5ia0PtX1b8P37qrAimZrVRJUMBnASQ9utyHBN14YQR18LCbaTmCgqoDZ34S-SuQ5wOU8X8QVBBcS01RO9XvXz-DuVA2CpQjaih6awnPvIGgSs5_Ypm_uIWVyiR_JSylgTcOs59U-Liu0SUuEZxL0Myak2I9W5eelw3TnUQHKqaHX5X1_Eo8KAW54zQC6E-qSF5rfit_YeEXKsecNpxQ3a5eWv0o_VMfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشت‌پردهٔ ترخیص خودروهای لوکس از زبان دستیار همتی
🔹
دستیار ارزی رئیس کل بانک مرکزی: «این تصور که بانک مرکزی از محدودیت منابع ارزی می‌گوید و بعد به واردات خودرو ارز تخصیص دهد، درست نیست.
🔹
مسئله این است که خودرو وارد گمرک می‌شود و با فشار و با این عنوان که کالا نباید در گمرک دپو شود و خطرناک است، آن را ترخیص می‌کنند.»
🔸
این مسئله پیش از این نیز دربارهٔ کالاهای دیگر در قالب «ترخیص درصدی» مطرح شده بود؛ یعنی کالا وارد گمرک شده و ۹۰ درصد آن پیش از تأمین کامل ارز ترخیص می‌شد که اعتراض بانک مرکزی را در پی داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/farsna/463702" target="_blank">📅 19:35 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463701">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">مجلس خبرگان: هیچ راهی به‌جز مقاومت وجود ندارد
🔹
حفظ انسجام و اتحاد حول محور ولایت فقیه و رهنمودهای رهبر انقلاب، ضرورت امروز کشور است و مسئولان باید با تلاش بیشتر برای کاهش مشکلات معیشتی، حفظ ارزش پول ملی و آرامش بازار اقدام کنند.
🔹
در شرایط جنگ ترکیبی دشمن، استمرار حضور مردم در صحنه تا حصول پیروزی قاطع ضروری است و هیچ اقدامی که موجب تضعیف این حضور شود، پذیرفتنی نیست.
🔹
تجربه ماه‌های گذشته بار دیگر نشان داد که در برابر دشمن متجاوز راهی جز جهاد و مقاومت وجود ندارد و طرح موضوعاتی مانند رفراندوم و صلح شرافتمندانه در این شرایط، موجب تشویش افکار عمومی و تفرقه‌افکنی است.
🔹
هر سخن تفرقه افکنانه، ناسنجیده، ناهماهنگ یا مخالف سیاست‌های اعلام شده به ویژه سخنان اخیر درباره رفراندم و صلح شرافتمندانه در برابر تهاجم دشمنی که درمیانه مذاکرات به کشور عزیز ما حمله کرده و به جز تسلیم محض به چیز دیگری راضی نمی‌شود، به معنای تسلیم در برابر دشمن و تشویش افکار عمومی و جرمی نابخشودنی است.
🔹
حمایت از جبهه مقاومت، حزب‌الله لبنان و انصارالله یمن، سیاستی راهبردی است و مسئولان نباید در هیچ شرایطی از این تکلیف غفلت کنند؛ همچنین باید نسبت به ناهنجاری‌های فرهنگی و ساماندهی فضای مجازی با جدیت اقدام شود.
🔹
رسانهٔ ملی در رساندن پیام مقاومت و روایت مظلومیت و اقتدار ملت ایران نقش مهمی داشته است و باید از آن حمایت شود؛ همچنین پیگیری مجازات آمران و عاملان جنایات علیه ایران نباید مورد غفلت قرار گیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/farsna/463701" target="_blank">📅 19:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463700">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">استانداری هرمزگان خبر غیرحضوری‌شدن مدارس استان برای دو ماه آینده را تکذیب کرد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/463700" target="_blank">📅 19:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463699">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">جریمۀ عبور غیرمجاز از هرمز: ۲۰ درصد ارزش بار کشتی متخلف
🔹
سخنگوی کمیسیون امنیت ملی مجلس: بر اساس مواد قانونی جدید تصویب شده در‌ رابطه با تنگۀ هرمز در کمیسیون، متخلفان در عبور از تنگۀ هرمز علاوه بر پرداخت جریمه‌ای معادل ۲۰ درصد از ارزش محموله، با توقیف موقت شناور تا زمان پرداخت جریمه نیز مواجه خواهند شد.
🔹
قوه قضاییه موظف است جهت تضمین اجرای دقیق قانون، نسبت به تشکیل شعبات تخصصی با حضور قضات و کارشناسان متخصص در حقوق دریایی و حقوق بین‌الملل دریاها اقدام کند.
🔹
طبق تبصره این ماده تصویب شده، هرگونه توافق‌نامه یا سند تعهدآور ۲ یا چند جانبه دیگر بین‌المللی در خصوص تنگه هرمز، باید در چارچوب اصول ۷۷، ۱۲۵، ۱۷۶ و ۵۷ قانون اساسی جمهوری اسلامی ایران منعقد شود.
🔹
همچنین ستاد کل نیروهای مسلح هر سه ماه یک بار از طریق ستاد کل یا وزارت دفاع، گزارشی از وضعیت اجرای این قانون را به کمیسیون امنیت ملی و سیاست خارجی مجلس ارائه خواهد داد.
@Farsna</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/463699" target="_blank">📅 19:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463691">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kF9TM6r13DtwR5gKfF9fz0nIBPCpKLCvHerI-Df_YcMfh3MBVaj6wPLQNmsf9DStyK5GdoUG6WGntZpQ7ifX_2iowzFCblGxjv0Mj0IS-ju1AN-AKSUED-9K1Pf0jp1yXE-NUYjUcG_ipdhAOOUY91iShmTnflK5GWRcEHg_JCOjMh4BOugYW8Dy52Gg5yw3EFjNddnQeGQt2DuW1cwWZvJWneTFI9L3B4T4wRRv6wnMarbblQEz2_tTObDMO6NZzXCNmucA7ikXp7vNSiBQOBxMGXGcFMksKDLeiV616gD6sXis-GfKQwI_2QumZYHaFSwiobPtJX8rGA75MecEYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YGz-Tu1GKQmN-D9KNehZfqysve2mCh5LWuSPKrKJ2CQet1gDQtsgruct7Mcm8uyVHCRIJLp3tdwP4R7KQoN3rYrvfZEh73F4kAJha5mfZEPCPxFI2bc-OamAdyEgxzRfbBKNfYLxyvFNggVn_BW0S4g7AbFJvJEPFnjgzL-Y2P0AvH2Cawg-XbEG-3p0yQlOaGP0W9j8EdfTReARg8UfvR1QlCT95yBw_0j80cRzFFZgxOCmooLzE_3O1mXPe_3HfKzOD151L4dWDUybiRf3RYSRyPaX8HslcUkBoxTHo27qEYI0WRmKYMNmVesNPplsOsvCEw7WCycjD4UJ13xq7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K8X9ReT9-3kJeHkxgfhZBkb0x995cLeUyZLb5sPJe8Fal3jEOOSG1Eq1dI53Dz4uJb6p5_ADZsjG7gOQSBE5rqS-VDHGMh8kaul45Z5DINHqkmIGUvi_vAQg2oE3mgCvYqC7MLGp_Swa7-c3PldWnLReVqot0SnxdZ7dVAdgNPM8mwwQrI4qW-peEfD4c4jDC0OAkrVs2BeXZRi5VS4Pworq53bTtkhSP3s_GFLdc1K9ba_vvFoS6xGprSekTBfCWdqOYHopqD8ajVkLCZTKx9wQ-Cg4mYtqwGc5ad5VvAi9INt_0fDl49MeAZeIRUTBVQOSxs0Qc6RYcsZmpZa5mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LnmtzhkX5R5pR0kC4uqTruFuPpeOdr6P4mIc07VLzMStjJ-NR6Dl1pt1a3PfwR7afFkI5ldx0aN3HWOrEVp8tQtJXLSJgYnYR7PGVJiL6rnFr8upZg-DbOpTuYBYJVwmP12woUkCdw7C3O-udwGGBFRERWFawA3zYL4wp5NaUUI4j4Gg6M2TZeLPvpGrfP0SA5hiVXei1hxBd9ASxttfpYVK_yHqQhpR42Kb79GXw5GSxoHyO4VhjZBx0A-a0Y137LwvYgJqBv7m00IyHOQ7Hllupx3ruQL-JqatyyxXe-xHlJ9ytgOEZwSBdpz3gPLKgPAiCVd6t_m9p6CNTpuoLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KGTAX7MCJovuCwqn_5Hov78CpxkaB1kDgaujuCJbU5Ixt2NqDBcPQTWoszNdtJwaH1QvdPMytxtrfE1m5LEwWTNtm24XnWuVdQ-br5a7QEjcESiiWJmW7xjUSsGJs3sEGQH8MG-6CrMg3eMi1_wjvxxIa-14c5WzKe9Q9Dpc8oyopcCkwk4Tk6daF8v4TnQVr1ydPou7AN3N4XAVJ4zDuvz725yT-eqkdU5kIy-E8WbxYku09mSdXUfXqX2t6zgf3F9SYevND_DHwrk7LcHIzFxKvqweA9lJBVk8xlx3HMaFPH3VbLIeYHUpPeIboiSV_W6yEXB2n_Ud6pjzCGoF_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KAlOc17tgBKuX_sv8q9WrHHpMKDBY6_tLRQz92DuSPdDnCARqNWXB1Js_sHmO682LlB-UTDisqR9sELkx4yl9B74rBTdx76uY5oNtCmTkV1a5BP1WyCcw6iukpg2Ar55M6SMXKNn5xwq-y85WygjT8VmS54RqJaWOICBOtkQceY-iZdl2j_Q5_Ctadq04HGH1h_2umlINRjCgKN2d3B6F89IKBrnkyyMEy2omammSvW9kBHDfEHx3JFnlJ0nV4JLI6aI9ZaU-zO6_dtmkelMGjIwdIb4oDdsqEZ9zn0_KwAfdh-K8YauxiQOUUdP-I7udeaDmQ3OKns1Lc7CHjPEng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YLVfaGiXQp01nhp23K3G18pCeeZY1-4feGWiOtWPtmsV5oQqfqajDtHScR7I9N-oRmht2SMNPEcOyZTUMR1dJ2WQlFLf5INt7ZdrBE2qHIWditaKBaBGJc-VSZhbd21b1aVqgG4H9IOPpXG_QKGQcw5b2Kdlpgj6nSm2YMjsrXzlXjnC_6jNbe4IdS9xXkP91CoP3HVqoWhulLCN9YGsF7WqvxjHcZV9QtYH8Bduvhm7Ig8qjLnAvLuiAWEpyHIPRBaTDNB2XnGfmIEVDBQjxVd9b_-o1zIqS1IhIcL8Tt6yczDErXyGgg4-lk4nznvuxW2Jc6AbGdvT74ObJQ4BTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اینجا نام ۲۷۵۰ شهید زنده است
🔸
قاب‌هایی از دومین کنگرۀ ملی ۲۷۵۰ شهید چهارمحال‌وبختیاری
عکس‌:
رضا کمالی دهکردی
@Farsna</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/463691" target="_blank">📅 19:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463690">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4313e9a0ff.mp4?token=AkQSD4YLrSPUFfaoEJU9-XDKMKltKE4Al-F1b8W9wNPqfn_X4QsfWqVtHHyqK4ZZ2GoUQeilupKE1Nguf3lyhOm1LaOUuA8LtmKf5ow3uKUcT7OOYeC5VmHZ7ISCWvv3Igc6RWHWWZTox0lcDgzEtjM_R10sqE1GL0j7GZhh9WWQSFnyqZUx-bRK9n1ZsskBHiAtWRQN9kMneLqZWkhhaYJKkldZeh2eh-D2aWGvUOHnKnyW5-30lvRqKaI74wFE55pUVtT2IZ5CggzJZ9j_hSbnTaL87J1FJZbj2-kPoGkT4sHg9YRNQYs8-q3bTyUXjyw_A8Kd7CsnEVumeaMDEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4313e9a0ff.mp4?token=AkQSD4YLrSPUFfaoEJU9-XDKMKltKE4Al-F1b8W9wNPqfn_X4QsfWqVtHHyqK4ZZ2GoUQeilupKE1Nguf3lyhOm1LaOUuA8LtmKf5ow3uKUcT7OOYeC5VmHZ7ISCWvv3Igc6RWHWWZTox0lcDgzEtjM_R10sqE1GL0j7GZhh9WWQSFnyqZUx-bRK9n1ZsskBHiAtWRQN9kMneLqZWkhhaYJKkldZeh2eh-D2aWGvUOHnKnyW5-30lvRqKaI74wFE55pUVtT2IZ5CggzJZ9j_hSbnTaL87J1FJZbj2-kPoGkT4sHg9YRNQYs8-q3bTyUXjyw_A8Kd7CsnEVumeaMDEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: رژیم کوبا بیش از هر زمان دیگری درحال فروپاشی است و سقوط خواهد کرد
🔹
دولت من همچنین به‌دنبال ایجاد تغییری اساسی در وضعیت کوباست. مارکو روبیو مسئول مذاکرات است. او مذاکرات عمیقی با کوبا دارد. باید ببینیم چه اتفاقی می‌افتد.
🔹
ما اجازه نخواهیم داد در…</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/463690" target="_blank">📅 18:53 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463688">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b34d22f9d.mp4?token=eqvGTM1pMv7fq5MLF5OQBz6XHeJQI8UW0uRJEZfXN0C2Pn5tEYrftUa9ssKYyK86STE6MDQc_6na9i2d7Dr-xpFV3wZRK0mztziAjLYURs63iugavP7QAvtfY7YToOQtJVUFXcYtQo5r6g1uFWuT9hwwD4RxCLEmauG9Iy1ZkfsrhAAaqHtsyybpint8txNekM6T3QRKwr9xoyVIfm7Ng1n16xmUUN4MGZlN5a_FlBtPxq_yFP2Yo-eXQeprkKWyo4k0-NXmXiXj0swH857brqmkXxOF4nvZSgGWuZy1mu1qyZKqsfq-0TWACwW_uI4G4YA_N5B-R8fCsCjCE-GbzmHmhM9XBZeHGuYELq1ZMdwJhfS6V1D2E1dJEjWJ4rJ2TKK9WjGL1SRljBNKHhQIw-n7GY3s1EKykktoNDjSYSw--drRyowHsZ00pKqU0AKQDTBRC40wx-bTeMcN_ed7-a_TY4E5j5jLFHe53YOy9YS5DgpNwMaJD-90Xw49nMComlKzswvi3M2_puBrfOu_g7x0BwAJspNhskfsUcgYcaB4oQcmoBfd2c85GmiwPRm88p_2SFcIM-zHb3qBau27S3imjDD3ktLcj__3F3no5mVnCt7qVyWNI2dhNdPqlWNUc9sAQf58YTnYrG687HK-CT5nEok300zKnm3iBP7jEfI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b34d22f9d.mp4?token=eqvGTM1pMv7fq5MLF5OQBz6XHeJQI8UW0uRJEZfXN0C2Pn5tEYrftUa9ssKYyK86STE6MDQc_6na9i2d7Dr-xpFV3wZRK0mztziAjLYURs63iugavP7QAvtfY7YToOQtJVUFXcYtQo5r6g1uFWuT9hwwD4RxCLEmauG9Iy1ZkfsrhAAaqHtsyybpint8txNekM6T3QRKwr9xoyVIfm7Ng1n16xmUUN4MGZlN5a_FlBtPxq_yFP2Yo-eXQeprkKWyo4k0-NXmXiXj0swH857brqmkXxOF4nvZSgGWuZy1mu1qyZKqsfq-0TWACwW_uI4G4YA_N5B-R8fCsCjCE-GbzmHmhM9XBZeHGuYELq1ZMdwJhfS6V1D2E1dJEjWJ4rJ2TKK9WjGL1SRljBNKHhQIw-n7GY3s1EKykktoNDjSYSw--drRyowHsZ00pKqU0AKQDTBRC40wx-bTeMcN_ed7-a_TY4E5j5jLFHe53YOy9YS5DgpNwMaJD-90Xw49nMComlKzswvi3M2_puBrfOu_g7x0BwAJspNhskfsUcgYcaB4oQcmoBfd2c85GmiwPRm88p_2SFcIM-zHb3qBau27S3imjDD3ktLcj__3F3no5mVnCt7qVyWNI2dhNdPqlWNUc9sAQf58YTnYrG687HK-CT5nEok300zKnm3iBP7jEfI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: ایرانی‌ها موشکی ساختند که قادر بود اروپا را هدف قرار دهد و به آن بسیار افتخار می‌کردند؛ امیدوارم اروپایی‌ها این موضوع را درک کنند.
🔹
هدف ایران این بود که در پشت این سپر موشک‌های بالستیک متعارف، ساخت بمب هسته‌ای خود را تکمیل کند. @Farsna</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/463688" target="_blank">📅 18:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463687">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8079078330.mp4?token=sygITB35jHfZ_M1e5KKwAWU7pJEmRc2Xn1nwK32ffeiVxe6rqbXqW4PxLMx7c_1SGwl0fNVamLt4HVZWb6d6RuB_QaKwddeEQL_clA8MWgdWWZrzCNKF3AebCCVu0KC1OxbwaFSa3clh70FzHsjFhIM_gF_CebAbHxjfe0VUDs88BDmERcbSaKmigpvy_pMLeRnVOBia5A7pERhwy7oQrs9_6n0AHp8cIbktDhzUZBc2mDc-bqon-WXd3HRuYC72boPOSr26mGMaQ6z1Q_aWlpgsprIq7bnHtDsTGix0n6jBgX88hNdQBRTATdntjDaIpmR1U4E1PMOUe7m0LrHZLzHkGUyk8SayvrgCVmUe8e5sGFT6crBZquNiJ0oxYrClBCRSFdkH5UCufMkB6oby0oEy90Q52YnTS7DP_B1UXfijLHuGQBBOyZnJaDK9GD2yEuPjz9VC-wEX1mvBvCBKdydROrxjPWnXKlUyeu7fpMSuxQoecCkl3QI5ydNCfdU_Dai7IQ758kfGmPH8Xmichrsc0B2yFqfsRKRPiyiQ_H4TIyg4Dh7X0yAJ6lv-73QL8MWBra4JAcXmniHbENNMDZpr3lav2mFyeHgC1GV7J7UBlBrfxejnCnZ2V0PDws-BwEazbb4Km0tiTD7upyy48I-RGoiBYBsbM2jFhAUp-3c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8079078330.mp4?token=sygITB35jHfZ_M1e5KKwAWU7pJEmRc2Xn1nwK32ffeiVxe6rqbXqW4PxLMx7c_1SGwl0fNVamLt4HVZWb6d6RuB_QaKwddeEQL_clA8MWgdWWZrzCNKF3AebCCVu0KC1OxbwaFSa3clh70FzHsjFhIM_gF_CebAbHxjfe0VUDs88BDmERcbSaKmigpvy_pMLeRnVOBia5A7pERhwy7oQrs9_6n0AHp8cIbktDhzUZBc2mDc-bqon-WXd3HRuYC72boPOSr26mGMaQ6z1Q_aWlpgsprIq7bnHtDsTGix0n6jBgX88hNdQBRTATdntjDaIpmR1U4E1PMOUe7m0LrHZLzHkGUyk8SayvrgCVmUe8e5sGFT6crBZquNiJ0oxYrClBCRSFdkH5UCufMkB6oby0oEy90Q52YnTS7DP_B1UXfijLHuGQBBOyZnJaDK9GD2yEuPjz9VC-wEX1mvBvCBKdydROrxjPWnXKlUyeu7fpMSuxQoecCkl3QI5ydNCfdU_Dai7IQ758kfGmPH8Xmichrsc0B2yFqfsRKRPiyiQ_H4TIyg4Dh7X0yAJ6lv-73QL8MWBra4JAcXmniHbENNMDZpr3lav2mFyeHgC1GV7J7UBlBrfxejnCnZ2V0PDws-BwEazbb4Km0tiTD7upyy48I-RGoiBYBsbM2jFhAUp-3c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: همۀ کشورها باید از دیوان لاهه خارج شوند
🔹
آمریکا همچنین با نهاد خارج از کنترلی که «دیوان کیفری بین‌المللی» نام دارد، مخالف است.
🔹
ما هرگز اجازه نخواهیم داد نظامیان آمریکایی یا هیچ فرد دیگری از سوی یک دادگاه ضدآمریکایی که هیچ صلاحیتی در قبال ما ندارد،…</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/463687" target="_blank">📅 18:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463685">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55dde2e202.mp4?token=aWfr6mcuM0YeLTDtMt61kZ16t2Cm-OZ8kshrfHsBSdi_7yRFnii7f3NGRyldEKo9NeLGXF7Jmd8z4oso8MsCNxskdLqKOpSsgWjCdwmeAzxux_p3IWRmSkbWkXUp4tXa6U7rfZQXBrK0TZQM5vyi6BWR0oWpmEu2CijFW7FsnsRSjKs693RXaQJl-4kHQzOWRCNi6F9Phs3PKthlEdu-LdlKmmliJLcNTLPnMiNijEZWyZfEDidqcPvBpsQUbowEFqgRAmko34UfKETxNsFWqyU3_BBTONsD8N1NC_LyRDvwvk64OiZvjMuCcCJDTdLnNSpl4wGqudax3-VqMQYmGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55dde2e202.mp4?token=aWfr6mcuM0YeLTDtMt61kZ16t2Cm-OZ8kshrfHsBSdi_7yRFnii7f3NGRyldEKo9NeLGXF7Jmd8z4oso8MsCNxskdLqKOpSsgWjCdwmeAzxux_p3IWRmSkbWkXUp4tXa6U7rfZQXBrK0TZQM5vyi6BWR0oWpmEu2CijFW7FsnsRSjKs693RXaQJl-4kHQzOWRCNi6F9Phs3PKthlEdu-LdlKmmliJLcNTLPnMiNijEZWyZfEDidqcPvBpsQUbowEFqgRAmko34UfKETxNsFWqyU3_BBTONsD8N1NC_LyRDvwvk64OiZvjMuCcCJDTdLnNSpl4wGqudax3-VqMQYmGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: دیگر هرگز به هیچ‌یک از دشمنان آمریکا اجازه داده نخواهد شد بدون موافقت کتبی و صریح ما، در گرینلند حضور نظامی داشته باشند.
🔹
۲ پایگاه نظامی بسیار بزرگ در گریلند احداث خواهیم کرد. @Farsna</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/463685" target="_blank">📅 18:42 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463684">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/241fce7529.mp4?token=Tg7mj9FiKzhQAz7kkTeb7hNxhiAMc-s8rQZd5kW7PHIGMSmaxZMaYaIiN3jL3vgrPakgCrs_yycSD9c4byxJMicbJWzzv8y0-ufOrS3DwMNhxQpPHuh06kjRoEkrWOokv-wpUfONj9ka50ubkVKEwPacPlCjn8zK9G7adGAFQyN-Ndx5Eb6G3fB-dlOPX-SOH2F5KnM-KsHn9sJZUYZG6NMy6aAbC3NZhQtA5T_e7dvnm8hRx9eA4oHrzyLzWjiksCRI2HcJrIEDGECDhEQ399AIh7fNbv8NJYTMhHpt_nA7SFE-aX0BYxZI1l2zwSavysn3TUjJ9771KwlXsiV-Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/241fce7529.mp4?token=Tg7mj9FiKzhQAz7kkTeb7hNxhiAMc-s8rQZd5kW7PHIGMSmaxZMaYaIiN3jL3vgrPakgCrs_yycSD9c4byxJMicbJWzzv8y0-ufOrS3DwMNhxQpPHuh06kjRoEkrWOokv-wpUfONj9ka50ubkVKEwPacPlCjn8zK9G7adGAFQyN-Ndx5Eb6G3fB-dlOPX-SOH2F5KnM-KsHn9sJZUYZG6NMy6aAbC3NZhQtA5T_e7dvnm8hRx9eA4oHrzyLzWjiksCRI2HcJrIEDGECDhEQ399AIh7fNbv8NJYTMhHpt_nA7SFE-aX0BYxZI1l2zwSavysn3TUjJ9771KwlXsiV-Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: رژیم کوبا بیش از هر زمان دیگری درحال فروپاشی است و سقوط خواهد کرد
🔹
دولت من همچنین به‌دنبال ایجاد تغییری اساسی در وضعیت کوباست. مارکو روبیو مسئول مذاکرات است. او مذاکرات عمیقی با کوبا دارد. باید ببینیم چه اتفاقی می‌افتد.
🔹
ما اجازه نخواهیم داد در…</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/463684" target="_blank">📅 18:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463683">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd1b131b72.mp4?token=bnRHr-5jFbqdYEbobSrEhSDizH_zm29nhk2S-hpNa7NrqUzu0B-V46ocWaCoNV1xHfPXhYZwKOjPod8CzxuYNKwnogzhIwDYtXhVN2EJwmC5FMVZQCRFrfkPi6CpocFbc4yFRpVRHGyZEOwMvuMHavf8-1IZv3SdK6PlfUvelcuEssXzqEOwOji1KU7JeaESYzwTLnDyG9BsT-zM_XJ7aQ5asYxezPp1cSnY6aVwM-_0w94awT1flOnqrFNdiV6RV-V5zGyQjAoRNSG-YQ8Ccz-XcCBiBCElLMUqn8GbozMGC3SuUsXUxx7XltAP6TcH8PCD81qph0bnkgMvpIzrUV0bKSXse0hjukBT34ebk4rxLT1L6vG4oUUcJwotn_A-ZuFJ7bsPqfSChJ_JDikHYNguKgYdxGxruwyqiJcCk55THdQ85MX5IAonMPtKtGShXe8YEt8fZDlBbOYZRwuODeVy4fIpgIoyQL-mU_r_bIorEm2sGZB95Z-l7bP18prt9UU52TK_56CR6pwIo459GtnTfuD_22PTDd-hxkicR54_xy-mOsv45ZdDLPTHoZWPowk6BIRboabKroDCDzTa-VkIq78PkMYrbj9Ye5-qb4unH1qEF-PtUTFnWYrda2aE-3yZAOuWJBR1j4D9xjNPClHAI4wwho_RJ0-Ul-Rbhro" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd1b131b72.mp4?token=bnRHr-5jFbqdYEbobSrEhSDizH_zm29nhk2S-hpNa7NrqUzu0B-V46ocWaCoNV1xHfPXhYZwKOjPod8CzxuYNKwnogzhIwDYtXhVN2EJwmC5FMVZQCRFrfkPi6CpocFbc4yFRpVRHGyZEOwMvuMHavf8-1IZv3SdK6PlfUvelcuEssXzqEOwOji1KU7JeaESYzwTLnDyG9BsT-zM_XJ7aQ5asYxezPp1cSnY6aVwM-_0w94awT1flOnqrFNdiV6RV-V5zGyQjAoRNSG-YQ8Ccz-XcCBiBCElLMUqn8GbozMGC3SuUsXUxx7XltAP6TcH8PCD81qph0bnkgMvpIzrUV0bKSXse0hjukBT34ebk4rxLT1L6vG4oUUcJwotn_A-ZuFJ7bsPqfSChJ_JDikHYNguKgYdxGxruwyqiJcCk55THdQ85MX5IAonMPtKtGShXe8YEt8fZDlBbOYZRwuODeVy4fIpgIoyQL-mU_r_bIorEm2sGZB95Z-l7bP18prt9UU52TK_56CR6pwIo459GtnTfuD_22PTDd-hxkicR54_xy-mOsv45ZdDLPTHoZWPowk6BIRboabKroDCDzTa-VkIq78PkMYrbj9Ye5-qb4unH1qEF-PtUTFnWYrda2aE-3yZAOuWJBR1j4D9xjNPClHAI4wwho_RJ0-Ul-Rbhro" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: مکزیک باید کنترل خاک خود را از دست دشمنان بشریت پس بگیرد؛ قابل‌قبول نیست که آمریکا مرزی ۲ هزار مایلی با سرزمینی داشته باشد که تحت کنترل کارتل‌های دشمن باشد.  @Farsna</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farsna/463683" target="_blank">📅 18:38 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463682">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31e6fdec04.mp4?token=MY-4ItVFX21pK9aaOIO7qNtC5Q5RRRGQasu5c5Kx28Ifmn4imN4gqwL2xctsZzsasMpjsb1uM0Jn4ughKUL-UoVZ8yg6rMwZUZBQaedxYlCR9Qc9KuD2oawDbFdTJ2Y60fT8us6_7Qac3c_vUApnK9nTH8E0yVhRa36QtwMpMxwRGNIQUHY58v4UehuhS9AQ0mhtBpxkrxXemBuaMIvSMAwoaWs7HDA2_qTwhhNPYPnmEUdEm6N1HUGqaI13CElN2yXscLPLkbb3nq7BWs8KrLLoh6VCxipMYlCXic0XTwkqnUM9YgMwQq_H3sf7M8FA_cIKOuWkPPsT9e-Kww74kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31e6fdec04.mp4?token=MY-4ItVFX21pK9aaOIO7qNtC5Q5RRRGQasu5c5Kx28Ifmn4imN4gqwL2xctsZzsasMpjsb1uM0Jn4ughKUL-UoVZ8yg6rMwZUZBQaedxYlCR9Qc9KuD2oawDbFdTJ2Y60fT8us6_7Qac3c_vUApnK9nTH8E0yVhRa36QtwMpMxwRGNIQUHY58v4UehuhS9AQ0mhtBpxkrxXemBuaMIvSMAwoaWs7HDA2_qTwhhNPYPnmEUdEm6N1HUGqaI13CElN2yXscLPLkbb3nq7BWs8KrLLoh6VCxipMYlCXic0XTwkqnUM9YgMwQq_H3sf7M8FA_cIKOuWkPPsT9e-Kww74kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: وقتی آمریکا و ونزوئلا را با هم در نظر بگیرید، بیش از ۶۰ درصد نفت جهان را در اختیار داریم
🔹
جنگ بود، اما شاید بزرگ‌ترین توافقی باشد که تاکنون انجام شده است؛ «غنایم از آنِ پیروز است.» همه شما این جمله را شنیده‌اید.
🔹
اقدامات ما در ونزوئلا نشان می‌دهد…</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/463682" target="_blank">📅 18:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463680">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c088ad7e9.mp4?token=I7EF_xawBGhWViAbJHkh6rMOPs55stYzGj0jZvkxsvkehSjVx1zjJlEpgSGjiPHhkoFETtuCRZUOig6SnaMRaJuQuO7CvTCnvbwbA-tf-wsCVly0F3I_vf9z-F__rN_JVhravewdheuV6nfXpXAnoERTEBfiEBIKsx98_p5-aM8AfkV7MEnBVa6jXueUDeblHGqirsmraivrJxXtVNH7jVM-I_BTaPdogD6kr5W9aZ0ZLXUltfUOXkNqnEehvuu5m1VEkHZL6r6fLODdp5Ar24ZSvaSrK7NRggrayz9uBM9gR8TvFkVC3ABAUbua4Vt37z-g3CSXnNo0hFBD4d639A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c088ad7e9.mp4?token=I7EF_xawBGhWViAbJHkh6rMOPs55stYzGj0jZvkxsvkehSjVx1zjJlEpgSGjiPHhkoFETtuCRZUOig6SnaMRaJuQuO7CvTCnvbwbA-tf-wsCVly0F3I_vf9z-F__rN_JVhravewdheuV6nfXpXAnoERTEBfiEBIKsx98_p5-aM8AfkV7MEnBVa6jXueUDeblHGqirsmraivrJxXtVNH7jVM-I_BTaPdogD6kr5W9aZ0ZLXUltfUOXkNqnEehvuu5m1VEkHZL6r6fLODdp5Ar24ZSvaSrK7NRggrayz9uBM9gR8TvFkVC3ABAUbua4Vt37z-g3CSXnNo0hFBD4d639A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: بزدل‌ها و خائن‌ها دوست دارند بگویند آمریکا با کمبود مهمات مواجه است، اما این‌طور نیست.  @Farsna</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/463680" target="_blank">📅 18:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463679">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fecabc4311.mp4?token=aru-fzsW-UZABMoH0P8IFhPJeclA_PSj3VDrjkSmwfdso8cLewsCRgmWH1zTMPD_-_X78ZWADTjFnQFqz_KDmrv41k5liz-t7zD7JcWzJuPaSLtuQ0BmAEPjh06AFIlmK4CQwq6RwlQ3FMz7FLBQ8X8xcb2Ih3a67cFK9TGOhowIcsBdGS0YOmAKh96aspP2-3bAwyh5Ga8Nr-nMgXE0NWOntBcEe1PRPEvrT0gmlaX1nRGd24p9v6SW-pul54bFWQPy-IBb5SOAJqZARmPCd8vcEhfhLw9PrdrtbIMGi7CDs07Bec4WxEmgj_9rDYo6-w7tIEIvwyaPjtyWYt0vfqPzjYIImiLIlit-8nzVYEs1oaQG2PVU-2nRrZOQaJNDD2hcAwiXpf2-ysOuoAIiwdC4JLjWWW2u7kCrOUWeXMoT8m2-0GW2yEw8Ihl0VMO8rgVuKU5NTxvf4bM9ZDmjo8aPwGvzllX_vru7YuNReQxbJ45y51Fyhp4Ioynn2vQn3V6GZ7uxmkCNcO2lFq7UrvLyNLL3j58_eyP2GgcoGJHNuCkQjVD8OlhKpuh27Ue3TnZEHFoptrhjncZJ5HFz2mrLrd6MyB9J_6n3roJlfjJZMJRpLwmXXK1Mp2Xweb3ivJiz8Aiy1BUFIqAU3QgaDzIxIGkZ-23iNYMsQkF5a48" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fecabc4311.mp4?token=aru-fzsW-UZABMoH0P8IFhPJeclA_PSj3VDrjkSmwfdso8cLewsCRgmWH1zTMPD_-_X78ZWADTjFnQFqz_KDmrv41k5liz-t7zD7JcWzJuPaSLtuQ0BmAEPjh06AFIlmK4CQwq6RwlQ3FMz7FLBQ8X8xcb2Ih3a67cFK9TGOhowIcsBdGS0YOmAKh96aspP2-3bAwyh5Ga8Nr-nMgXE0NWOntBcEe1PRPEvrT0gmlaX1nRGd24p9v6SW-pul54bFWQPy-IBb5SOAJqZARmPCd8vcEhfhLw9PrdrtbIMGi7CDs07Bec4WxEmgj_9rDYo6-w7tIEIvwyaPjtyWYt0vfqPzjYIImiLIlit-8nzVYEs1oaQG2PVU-2nRrZOQaJNDD2hcAwiXpf2-ysOuoAIiwdC4JLjWWW2u7kCrOUWeXMoT8m2-0GW2yEw8Ihl0VMO8rgVuKU5NTxvf4bM9ZDmjo8aPwGvzllX_vru7YuNReQxbJ45y51Fyhp4Ioynn2vQn3V6GZ7uxmkCNcO2lFq7UrvLyNLL3j58_eyP2GgcoGJHNuCkQjVD8OlhKpuh27Ue3TnZEHFoptrhjncZJ5HFz2mrLrd6MyB9J_6n3roJlfjJZMJRpLwmXXK1Mp2Xweb3ivJiz8Aiy1BUFIqAU3QgaDzIxIGkZ-23iNYMsQkF5a48" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: ایرانی‌ها موشکی ساختند که قادر بود اروپا را هدف قرار دهد و به آن بسیار افتخار می‌کردند؛ امیدوارم اروپایی‌ها این موضوع را درک کنند.
🔹
هدف ایران این بود که در پشت این سپر موشک‌های بالستیک متعارف، ساخت بمب هسته‌ای خود را تکمیل کند. @Farsna</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/463679" target="_blank">📅 18:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463678">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fb9cc48d1.mp4?token=AmrTPedpzzZpljSd-RLD_1l8rcwspKVDiPhLolYljDQWwvNH2IUUVdUwNK_2NqXbAW1fcHasayK-IhbpbXM120GZmdWjdo3sArxRO--2s6Z9wMWg-1PVAr0DA2fs-rm0XEY2EXldXeT6aWAIoLKZbmO0F0qjstFlj8qAs3t1jj_a9XAOJ6e4RmRQB36DpVcrjpMWQC5GhmgTXVitSnWBVH1YT8cKK4dJwQLzuStUeSK0m_tXyobaZ4cfWUrmX2H_2hqhXpruNwLKPe3hJKM2pKEbkpOMOYDdBG4UYPMkqenSfWlTTo-CrayhhKQxDl-okwpiZMAm8fCag_YmlZsftw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fb9cc48d1.mp4?token=AmrTPedpzzZpljSd-RLD_1l8rcwspKVDiPhLolYljDQWwvNH2IUUVdUwNK_2NqXbAW1fcHasayK-IhbpbXM120GZmdWjdo3sArxRO--2s6Z9wMWg-1PVAr0DA2fs-rm0XEY2EXldXeT6aWAIoLKZbmO0F0qjstFlj8qAs3t1jj_a9XAOJ6e4RmRQB36DpVcrjpMWQC5GhmgTXVitSnWBVH1YT8cKK4dJwQLzuStUeSK0m_tXyobaZ4cfWUrmX2H_2hqhXpruNwLKPe3hJKM2pKEbkpOMOYDdBG4UYPMkqenSfWlTTo-CrayhhKQxDl-okwpiZMAm8fCag_YmlZsftw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:  ایرانی‌ها قلدرِ خاورمیانه بودند، اما دیگر قلدر نیستند
🔹
از همان روز نخستِ ورودم به عرصۀ سیاست، موضعی تزلزل‌ناپذیر داشته‌ام: هرگز اجازه نخواهم داد ایران به سلاح هسته‌ای دست یابد. @Farsna</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/463678" target="_blank">📅 18:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463677">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترامپ:  ایرانی‌ها قلدرِ خاورمیانه بودند، اما دیگر قلدر نیستند
🔹
از همان روز نخستِ ورودم به عرصۀ سیاست، موضعی تزلزل‌ناپذیر داشته‌ام: هرگز اجازه نخواهم داد ایران به سلاح هسته‌ای دست یابد.
@Farsna</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/farsna/463677" target="_blank">📅 18:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463676">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NniDftPetY89TlqN7nmGwiJfNcJNDKhJqDoFlKHEFReJ7NdqZfK9q9sNoNME6bX6WMeSRn_2eTvZOdQvtzo4OQvpMwTbODuoyN0o_XAvihSpAfIOslxjqTS6XYHuc_qpaMflpTN5F5Ws6L5MQjvQTXNLdfLnaCphlm5OUu2LpVOVqTTFQPjy5addxIscSUNVqwFfDnIp5EyZpgZEiDaR0_v1ubAvADd8ocd4bhUp2RyfTKmVwUi3kwxmv1LW_3Odpe1472vCXl68HcS5-edIOBcrJdBXWdLoAgc6zo-jXDqcUHxdSq_yPQJ-6qKgRN6tISxYaM87bEkBiCa1dJpI_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ رهبر انقلاب: معلمان شایستۀ آن هستند که در مجامع و زمان‌های مختلف مورد تکریم همگان باشند
🔹
ما همه وامدار معلّمان خود در هر مقطعی از دورة‌ تحصیلی هستیم. این قشر عزیز و محبوب که اغلب با خالص‌ترین عواطف شاگردان‌شان مواجه می‌شوند، شایسته آن هستند که در مجامع…</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/463676" target="_blank">📅 18:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463675">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">رهبر انقلاب: در آستانه سال تحصیلی جدید یاد دانش‌آموزان شهیدمان را گرامی می‌داریم
🔹
اینک که دروازۀ سال تحصیلی تازه‌ای بر روی خیل عظیم دانش‌آموزان و دانشجویان گشوده می‌شود و راه‌نَوَردان علم و حکمت با امید به توفیق الهی دوره‌ای جدید از کسب دانش و معرفت و مهارت…</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farsna/463675" target="_blank">📅 18:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463674">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Is33ZmhpuX8sQVAyeacWUYjMp_ad1L3kDiCTc9XIzHENUwGppQwSmMILOELyF-D08IyUGcEe3KssP4VwcsV2PHN4Jlc8lI5ZB13UZjgb3It0VYRgOdLhLnOL0Hr-OO3-B2Tj839YunwclSwouOK9stMcbr3TOMrQh7QIh2m7JyULzOi1Sk2Vjpo5hn-94pqs4ueLFae4UdODH_lkyeHRYb3kR2Fk1R9AVAWXKBlD9QlNgItf8DJj3fZjcMGjMUmegekcfw32QZnXUOlRrzghLUenodCcp2HWMX6y1Eyke-f7sdNFDIh9LE18NnaRdbcN-2Zc2aQUPkSUUexKNv_lHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ رهبر انقلاب: آغاز سال تحصیلی نویدبخش حرکت به‌سوی آینده‌ای شکوهمند است
🔹
طلیعۀ سال نو تحصیلی و بازگشایی خانه‌های علم و ادب در مدرسه و دانشگاه‌، نویدبخش نشاط، امید، و حرکت پرشتاب ملّت به‌سوی آینده‌ای روشن و شکوهمند می‌باشد.
🔹
آینده‌ای که تحقّق آن در دستان…</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/farsna/463674" target="_blank">📅 18:04 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463673">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">رهبر انقلاب خطاب به دانش‌آموزان و دانشجویان: مرزهای دانش را بشکنید و قلّه‌های پیشرفت را فتح کنید
🔹
مسئولیّت امروز دانش‌آموزان و دانشجویان، سعی در مجهّز شدن به علم و تقوا، امید و اخلاق، و دانایی و توانایی و زدودن پرده‌های جهل و تاریکی است تا آنگاه که با شکستن…</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/farsna/463673" target="_blank">📅 18:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463672">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsHVJQaGjZACPftDlGvCDxBUZtNcVwvy-srDnd2QJMzmWOfPDoct-6-OagLXK2w6WAFKc9rlA90Zm5Pi4RrNdJS8tlE-4ck4sxMp6kEqGnHZZs5q6zSZJX1FeNh5tL5YAlHca_BRXjgWN0hkORKkPTsoMPj6WeKG6uOIM3JEWo1tTohq0BjmWMHy8kCRGa-LhVLbA6zPXHQpJu-u5koY3MuD8O3m5zlt93wo1lus50k2ATbHEkBbdDm7U-UEbf62TdY4GR_OsvQuwX0bbLGDVohIFcyOgnsTsULnaeek930OHf0jI4tPQB4uEnzko_Fd7OWEQfD3EnUMmNLEVUnWjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ رهبر انقلاب: قدرت برآمده از دانش همراه با تقوا؛ سپری در برابر توحش نظام سلطه است
🔹
اکنون در روزگاری که توحّش نظام سلطه خصوصاً دولت جنایتکار امریکا و نظام جعلی صهیونی بیداد می‌کند، قدرت برآمده از دانش همراه با تقوا و اخلاق، چونان سپری پولادین و شمشیری بُرّان…</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/farsna/463672" target="_blank">📅 18:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463671">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‌ رهبر انقلاب: فتح قلّه‌های پیشرفت، مأموریت تاریخیِ دانش‌آموزان و دانشجویان است
🔹
مسئولیّت امروز دانش‌آموزان و دانشجویان، سعی در مجهّز شدن به علم و تقوا، امید و اخلاق، و دانایی و توانایی و زدودن پرده‌های جهل و تاریکی است تا آنگاه که با شکستن مرزهای دانش و…</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/farsna/463671" target="_blank">📅 18:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463670">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
تا ساعتی دیگر پیام رهبر معظم انقلاب به‌مناسبت بازگشایی مدارس و دانشگاه‌ها‌ منتشر خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/farsna/463670" target="_blank">📅 18:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463669">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iVuLo5IKfl3-bBwHguIKJoWWbLhc9JvJmED1Zn2_wqGOydv9JaQj4LaJXPVCrETTVtafY8dKjLEM2l3Fcqv2oYoTR1EQozo-jxe1hACza8X4OFfID-I1IdyNREug_loqTo-3nWXtHC4tCFKZa3IGmx4oPr-P9zk49DMlYAu8qIUCJgSn-isQDQMF567VEwkhqNMjnqVOR-GYqo3eLSUhnZw8NHAFs5vv0xyY_oHuj-4E8cLIVCLx1rxpKlyu9wExNvA1qLpf5nqK-cAqlrv-bJ6xFRNI-zsTUQU_ZjzgzxF_8b2rhgJJ9ALSalBEzheDjvkY35uPQ7scOQY_SunZRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش‌ها از سقوط جنگندۀ آمریکایی در آلمان
🔹
رسانه‌ها خبر می‌دهند که یک جنگندۀ اف-۱۶ آمریکا بعدازظهر امروز در پایگاه هوایی اسپنگدالم آمریکا در غرب آلمان سقوط کرده است.
🔹
شاهدان عینی می‌گویند که یک جت را در حال کاهش سریع ارتفاع دیده‌اند و سپس ستون بزرگی از دود سیاه در نزدیکی باند فرودگاه مشاهده شده است.
@Farsna</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/463669" target="_blank">📅 17:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463668">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس من</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VckHnc6hfOPzCMwODLvkrbxlvIUB7-R1VVblDB9JcfiYVdOJyry7JogImUs8l-SOqI_eESBBazebwhqeLt4XNDsCHHCFghM6QZisy8FWo2qjr9pq4Ml3q_kxqWXumUfq2BfpVQ-SqUbAY2YQJL_MVRrLxgInfEEBPzQgjaK3gTvFZRCktSHmeM82fa7GNCF5JG_CLLrLVnwF_rPyRGfMxCxBCLsELpzC0oYBAxrrPoaDywRJy_bpVu5bJ4QBsYetQPUD2mSNRSH2Oz013JECWYVuSmR__uXBb-FIeWhK5JAWnHfFW8lorkzMhKQNNNMxanDUMevCBEeuKKNCSWmOow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنزین خودروهای فرسوده با یک شرط قطع نمی‌شود
🔹
طبق اعلام مدیر نوسازی ناوگان حمل‌ونقل ایدرو، مالکان خودروها و موتورسیکلت‌های فرسوده که امکان نوسازی فوری ندارند، می‌توانند با ثبت‌نام در
سامانۀ نوسازی و اسقاط
، از تعلیق ۵ ساله محدودیت‌های قانون هوای پاک از جمله حذف سهمیه بنزین یارانه‌ای بهره‌مند شوند.
🔹
این امکان از امروز، سه‌شنبه ۳۱ شهریور، فراهم شده است.
🔹
پیش از این، جمعی از مالکان خودروهای فرسوده در پویشی در «
فارس من
» خواستار
تجدیدنظر در قطع سهمیه بنزین یارانه‌ای
شده بودند.
🔸
ثبت‌نام و استفاده از معافیت قانونی، راهکار فعلی برای حفظ سهمیه سوخت خودروهای فرسوده است.
@Farsnews_My
-
Link</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/farsna/463668" target="_blank">📅 17:42 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463666">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvX4iG_SaICQvNighR928-Pptn3dR6RWYxTmFv73Bdy9vW3Gemib17McVEWCcFVnJAZYC-I_JJsnzMZ5_6hczJekOhVpv1-wMlcv3gXqXKUMYk7ncq94_Bx5CA1MwsvC33bHBolqcT9_C4n2DM5wfBENcD7uUHWDsddtAxywai15EJYbTxdM1-qG-IeIfVOiAHWPrYD29Sd96e7glQtWhGzOdayOzKDaamMZKye5Fu1HWvOBZYEo-aK8-4SsHaRPQ-hTp5B4ujl6vvXseDsdZF0637b4fyB4BwModD3I6efUCajKApGK99hUIIb4Hil8Ev2RjKKptsFDL4UysXbghg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تا ساعتی دیگر پیام رهبر معظم انقلاب به‌مناسبت بازگشایی مدارس و دانشگاه‌ها‌ منتشر خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/463666" target="_blank">📅 17:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463665">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ff2847b8e.mp4?token=PVq1CUKc0YGoMRD6MOhRu7o2Pf5RlNVqraOhJicJl8blRfP7PncWEDeJYYyygOHpXY9f00iFSp19uuzhXUq4XEYmdXQc4PTib2R5hxFJryHah1vLhndOVALRhGOkfK5kheClEwCv1jneuN7Qk3wTWLxyJkDgj96cB19TYEMdj-OBdjIOUEWd47MaRpKOkwHcYofW-wDrHOTzOIw4-42n3gj1d_SVcQSkwlDAclx447pXWjlv74onhOrqasHrFh24j5vrSVBcOmk6x4ezfzM1DsvMYrIlVSYq28CzCD9KzGkx2tppBojhPwB1D4D-idYHVcjXooj4t_TET6ilidKOTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ff2847b8e.mp4?token=PVq1CUKc0YGoMRD6MOhRu7o2Pf5RlNVqraOhJicJl8blRfP7PncWEDeJYYyygOHpXY9f00iFSp19uuzhXUq4XEYmdXQc4PTib2R5hxFJryHah1vLhndOVALRhGOkfK5kheClEwCv1jneuN7Qk3wTWLxyJkDgj96cB19TYEMdj-OBdjIOUEWd47MaRpKOkwHcYofW-wDrHOTzOIw4-42n3gj1d_SVcQSkwlDAclx447pXWjlv74onhOrqasHrFh24j5vrSVBcOmk6x4ezfzM1DsvMYrIlVSYq28CzCD9KzGkx2tppBojhPwB1D4D-idYHVcjXooj4t_TET6ilidKOTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی با وزیر خارجهٔ ایتالیا دیدار کرد  @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/463665" target="_blank">📅 17:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463664">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_ceDN_tv11bLRY5Vsvc5O8PS59_MSGC1COqH_J0PsyX1hl_cS196Q5ztLUpfCAzWKuy28XnJ5ileJjhqHvGMCxbK8NhZ6ICxgsGoF_0Xgmrhi4hsHPTZNuKZ2uoS8dB--jwSuB-V9iu0DSTq31Pa0iW0kAyfQZMfHVLBDXsr9HX6pPapdetPo7NbbftE8SWsxQGmcbi6sOlzXYGDI8mGh72hkhoCihkv_XRU0dZFpAweOrImKDTiSUOK1GuusDzLdrAFjxSWEaYraQzFnTw_Xodq08JYmgK7Vbv6E5IxhdB9WSVyvLdNXnddrCVoR9eWuffzPFqc84dkZLG7DRBrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعهٔ مذاکرات، نفت را پایین کشید
🔹
انتشار همزمان اخبار مثبت درباره مذاکرات ایران و آمریکا و احتمال بازگشایی تنگهٔ هرمز، بار دیگر بازار نفت را تحت تأثیر قرار داد و قیمت‌ها را کاهش داد.
🔹
در تازه‌ترین مورد، کیودو و رویترز به‌نقل از منابع ایرانی مدعی شدند تهران…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/463664" target="_blank">📅 17:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463663">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e713acdda.mp4?token=ZYzIDP6bijko3EMO4qiE0HRzazTHoxoBGwRfY6EmDNAr9QL_DjnquBRIbfYKpcwRFmO7ZJllddT6IDR4aSeY50IsMC9DSv4jV-kbi4zKL4o0hYC4LLAhkRLRWBhCYoxft52xD9whQXCqjgIowX2we2KlZ7XBrrWJaOrFtKO2WKymWP7opR5w4RUJ-5-Z3v_oLXotXWE41_83_SI55STTRq3u5-bzRMvkxuVBq5tuCJBriS4aOpRJFA_IC3sO1WoreLGWflYhjDJB6_t-jj1xCHd1kP1hJta5Gj524orxS5f6SRoAamUQTcQl86KYKyKWW2APeAhnQAQ4wSm1QkkwPxK22aox1XrY8EajaKm6GHHyQFAYFxymj9IQISxmBo1erlmXiPj7qKt3Eo-GSa3CmsWiSx-bWRhCQjACn4OkpiOoXVEpyRNSsv2CFJFBGkK2yr5cfXQ5CehlVB2AiEwmqO7MKmCM4e_mft0a9YsWQLZk7CAAi-6RGtS7N7C14TuCEHhOcHmyPEl2cTX1xWnPibjN4jJdjXA76ZG-aH2uuA0Tyls__mMbQMGaMOCdSQY2aHkiy7SQAdd42WxnuURzE4WmA_bamNgROlVwbah4sZBsNqpe_jq9IVznCH7jG9XygAFRd5uB4gnFpM7gQLmXVvniKeYsJWp6n23cwUrRQIc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e713acdda.mp4?token=ZYzIDP6bijko3EMO4qiE0HRzazTHoxoBGwRfY6EmDNAr9QL_DjnquBRIbfYKpcwRFmO7ZJllddT6IDR4aSeY50IsMC9DSv4jV-kbi4zKL4o0hYC4LLAhkRLRWBhCYoxft52xD9whQXCqjgIowX2we2KlZ7XBrrWJaOrFtKO2WKymWP7opR5w4RUJ-5-Z3v_oLXotXWE41_83_SI55STTRq3u5-bzRMvkxuVBq5tuCJBriS4aOpRJFA_IC3sO1WoreLGWflYhjDJB6_t-jj1xCHd1kP1hJta5Gj524orxS5f6SRoAamUQTcQl86KYKyKWW2APeAhnQAQ4wSm1QkkwPxK22aox1XrY8EajaKm6GHHyQFAYFxymj9IQISxmBo1erlmXiPj7qKt3Eo-GSa3CmsWiSx-bWRhCQjACn4OkpiOoXVEpyRNSsv2CFJFBGkK2yr5cfXQ5CehlVB2AiEwmqO7MKmCM4e_mft0a9YsWQLZk7CAAi-6RGtS7N7C14TuCEHhOcHmyPEl2cTX1xWnPibjN4jJdjXA76ZG-aH2uuA0Tyls__mMbQMGaMOCdSQY2aHkiy7SQAdd42WxnuURzE4WmA_bamNgROlVwbah4sZBsNqpe_jq9IVznCH7jG9XygAFRd5uB4gnFpM7gQLmXVvniKeYsJWp6n23cwUrRQIc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از تلفات سعودی در حملۀ نیروهای مسلح یمن به تجهیزات و ماشین‌آلات نظامی مزدوران در استان الجوف  @Farsna</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/463663" target="_blank">📅 16:54 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463662">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‌ چراغ سبز سعودی‌ها به افزایش سهمیۀ حج ایران
🔹
معاون سازمان حج‌وزیارت: برای افزایش سهمیۀ حجاج ایرانی در سال ۱۴۰۶ با سعودی‌ها مذاکره کرده‌ایم که چراغ سبز نشان دادند.
🔸
ایران در حج گذشته سهمیه ۸۵ هزار نفری داشت، اما به‌دلیل جنگ رمضان و مشکلات انتقال ارز، حدود…</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/463662" target="_blank">📅 16:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463661">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bca659922b.mp4?token=MkKe1fBqa-zsD6ZaaTksC831BI5Tq5i_AsSPjc8WP3FIPrAoQGkGna4S5ILlMFx2BakzRaeLLNDvTLiLIYPcyDpO3aBlyz2l_Q2ReHABGAuSFvRKGrtnt_StxU7F0vp3sLeVo0j2m3TVU6_cAybexjQb-XGI4wnWWD7q1PpuPT0ufU6Qz09eQmObawvwugs27lh8O_bgyknp6DjGGKotlDjxWKIhajL7-lc_FVdCHVzxWEptjrVr60JiKKtgowFil4zP7xu7YBf1FRiSYaGvAGY6QieXcNC8B0sG3MtmzpiAEhOJ_jp70j0vDE7lz9VVV61rwhAl_IVxcuFeyG9Ljg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bca659922b.mp4?token=MkKe1fBqa-zsD6ZaaTksC831BI5Tq5i_AsSPjc8WP3FIPrAoQGkGna4S5ILlMFx2BakzRaeLLNDvTLiLIYPcyDpO3aBlyz2l_Q2ReHABGAuSFvRKGrtnt_StxU7F0vp3sLeVo0j2m3TVU6_cAybexjQb-XGI4wnWWD7q1PpuPT0ufU6Qz09eQmObawvwugs27lh8O_bgyknp6DjGGKotlDjxWKIhajL7-lc_FVdCHVzxWEptjrVr60JiKKtgowFil4zP7xu7YBf1FRiSYaGvAGY6QieXcNC8B0sG3MtmzpiAEhOJ_jp70j0vDE7lz9VVV61rwhAl_IVxcuFeyG9Ljg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی در حاشیهٔ نشست مجمع عمومی سازمان ملل با وزیر خارجهٔ سوئیس دیدار کرد.  @Farsna</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/463661" target="_blank">📅 16:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463660">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aee677ae2.mp4?token=DYY0KHSXdkuLFRbi_M8EZKHr8CZ7xMA_C7SEEM796Bgmzbq-nqoqVUrW618SeX7i_uvHfIWYGPp6fvLnAPEFi8gW9cA-wyWlNIorc6GJiGKGuZ6x62IvsC2lNZAaxK3buFS0V3HQ9Sr2LPqsZLDE-F4gO4LNP_bJpkBLMkLYc6hnJkSROXDYXJkosrl2bDoRnACif4-0KfjFXyeapQtA_gPTRidyS21NpGsmPQMWd4kpLJA94Px1ccUUQh8u_1Z48usY2Vi3FqvUQBhStYm7UsoZ-wlR2rG4midb4aXqhu4Dkh30cG0KivOYNBan_1Qjm3XFhDt_Cet1yzncwKcyAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aee677ae2.mp4?token=DYY0KHSXdkuLFRbi_M8EZKHr8CZ7xMA_C7SEEM796Bgmzbq-nqoqVUrW618SeX7i_uvHfIWYGPp6fvLnAPEFi8gW9cA-wyWlNIorc6GJiGKGuZ6x62IvsC2lNZAaxK3buFS0V3HQ9Sr2LPqsZLDE-F4gO4LNP_bJpkBLMkLYc6hnJkSROXDYXJkosrl2bDoRnACif4-0KfjFXyeapQtA_gPTRidyS21NpGsmPQMWd4kpLJA94Px1ccUUQh8u_1Z48usY2Vi3FqvUQBhStYm7UsoZ-wlR2rG4midb4aXqhu4Dkh30cG0KivOYNBan_1Qjm3XFhDt_Cet1yzncwKcyAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر بهداشت: کرونا نیاز به واکسن ندارد و شرایط تحت کنترل است
🔹
مردم توصیه‌های بهداشتی را رعایت کنند.
@Farsna</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/463660" target="_blank">📅 16:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463653">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lfsfZLck0Rq0AoVdEQIbOkZXJGDfLNVj-y4Lsm9ry3BUfQRn_Ck5JhryXQieFabrcsTtq_PKP9pqoXpCpZFZNJHsyqUiQ8PKgXqro8DVNYzpLY1zqt2lNgFmSRj4lwMIRxXTHth7i3Que2MLhsdtBoqR2b7DWgvyUf0WhgF-3AENEtREPnrOpscIa3u4qr8JcKt-xpn8YkcJtGAH_6zaRDaHgmKIRo2Ax8uSWFQF2S8VuchQKy13pfJH3a6foECelxQkd4-kHXFgxx932iyX59EmSLl8U6n_JkpcC5KEj70wvWDZCqSM7LFT4on8Vh6IaDpMEstAwkEJIvUeetSPew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RBTPSNA6EKGhZoI8zLboWZS9XPMUYLz2fGXMgbHc-t0mrcOgUAhy6So24iM9qGEpTeZLewf2NJ-arWkqvucGRDwk6rFG-BQtFAuLz7HD_b_UfB837wau8TVrSePXUBbOJGN0YiKErpFngYzBTQJa92b7zAS53JProPwHi_ThObimlX-_Xm56FaFYhU2_b81MfAULM-vwETIFCukYzekyWrIeeXRax0tcC24-5aGTCZiOC2ksXp9q1lsgb7x6yXgYZoA1uAvxYxVhDDXnslaLyzNiBODF5IvGaFgI8BYKxoj1wC904yuWuCf3b-ul7WhFu_tI1_LiL8EoFjvMuZdKJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YnfPHaXw-FAjsncz_1KaDdgRJO6dC0tS1erqGRlF5FxyXXpFYK2crzNXlkzqPA0Lqa0R9sd734Lao1hKnSdbG9CKyYFUxEaZ2VVGYuNEWiS1c_XT5AOsv2h8FKruJtz5-GEJ9HLPep7KO0Lagh4_PwpCzVCpzPzFhSMkkRXFh4FxJDpbufX_28_inGlwtdOxX3Jr2-d0HCTjn1f10RB0XdNqEDFvaKYErKadrBaUoYz9iWYpchHcAmXDv-LNGwlbbqdG0YaRCLjwz1FgXmummFAKFHOIvelh3rgug1jBRk7_V7DN5IjHSdpA7ffkfIaKKr4zu-PujBNDngTry7l33A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BOiRDHFD0ehvXxRQL18eunN4yw_9iKnoKsYxTny-4uOiInMKfZGFXUIiWNXPM9zflF58Gvq1hoyUcc-BTXldfxp_PlSSCwF3b4MzJu39OUowacHePfyeVd6vaZkArJh7xMTWCrm63RUK_BdXS1PvjDD15Pbnnlg6wUlElo4uqpBlse2_PidFBy0J3hFbxk_Fvey8FNnJA4vMOYLORuzs81RjGYSXphO-NlVWMQO2V5ISZcB6SpyFNdRcbNOaOTkX3vlkSwP8itS1t8_6-3N44DknCJZw_1UoVGnJWr7FYSTSm_s_URA2juvPIrLfYmIpHszmigM_bMmFNIuVIWh5RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IVHoRRttVJ4s6uYWTcxD1HPagSZi0A_jvrNXwuNqEdFXCKFePE2H_pXr_nBwR6Y0ze5C_HwT6ibpqENzKxwU1dj6GA3x5fooq_pX3T8iGQzeCNM4VXszWyARdyisQHoWqxiCHMRmfGaAipQejJxUyAmupubFzEGbMdCgsFTySxnpOmo7SIMT8o_W-5mqd0b4JGpqN8LoDmg6vbLw-QQ-LLs3nBDZqlQpwZXPDxhP0_CaKinwOzrnDOKpNhDr567xdQLxDiEsHH1EiF-J0CvwmSqp907wp2v73V32-hgW-HQC9UIN-ZZ0xoDKdWK2_ApBnUOS7qd-bBrtjG6k_JvoQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h1JEgqGxmPpEioP1ZDPRU1CtXZ7lC74_nZyqtV4vGplj-N5sxkcT8frjB4y3S1UUx2ysI0ESKDURqM1uRuPP0cIXD3bstzEaLsIzw-dsonMZ7noiwZX7pJJaD8je2wnsRIo8dWZp5hAVCT_FDJ4jBCfgTYsrpdxy7reDQyJjvCWu12ie7j2l9pbqE1IaC3OciKH9Q5HexDin43DF9c0q4cOpeH7GG1NbwrJsjTImbULWtzqSq2Obdam7Ro2LVR-FWeEHpekSLOK5FP6TUvlJFIZebaIF753BBrPcrP2mwnnA288aUKD5ZelOE4Xl5kMxfkX5Y9af8XJBw12jtWwD_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ARtlOlMaqwPSHTEC3vYwz8jXldd1-4IGK_rUzZz_1bMv4AwEHW8vFqBLTqeK1112aJbZ0fhQfGphnYqY6FFSCL4br5VEQDVXjE3LdnHphZ0vxfgw1P8xRDNTIke2p0DTmfml0P98WKSKKu9xfCG4ltEgB2nGwiJj3mWFcDXtTiKv09UyZWHydkoHDs6wIxR611il9zon_9LnbYoyHJuEqdFLc6Rs-giGxkKDXLtbcUhJfyRa1m0lcq8czIEGWbH_tcKLCyrxjBGPmrBkNp0NgUln0-Ma9FJdbdiHbU2VlJwi3NWzwZS1ydXVci3Yd3NG1EBkRCE29jSHTlvPuRk9hQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
قاب‌هایی از حضور رهبر شهید انقلاب در جبهۀ حق علیه باطل در دوران ۸ سال دفاع مقدس</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/463653" target="_blank">📅 16:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463652">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc565ba1d2.mp4?token=Ina6uGWP5_iSwsMtfn7GXqhJygiHE-20jz5hcRRacH6NuM8av7pCVx2kj51cruejEbtK07tFJ5TOTSkuGvxg3yA2YH8ZFCrBJvYe42cWzwJkaB5nmb0mCug-hOklwI3FFBoEyVjsEFWq799v7gCkZsjvEqqpYDg-xkanD8nbyHxb1phu3gCIxtH20_irQEGNeqrJnzeE8rwwwyLE1o2X1sO5Nlv9w6oID9dpjApTqIozaWGcZ28_1Tc2XzvWrhYcduNdqUgcXtDOp56QiPQCcUCae4k9wIPMnHc9gmfw7H6xx70wYOu8xQzsG-BRVWOUzST0T088tb8N6RQL_Pff9Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc565ba1d2.mp4?token=Ina6uGWP5_iSwsMtfn7GXqhJygiHE-20jz5hcRRacH6NuM8av7pCVx2kj51cruejEbtK07tFJ5TOTSkuGvxg3yA2YH8ZFCrBJvYe42cWzwJkaB5nmb0mCug-hOklwI3FFBoEyVjsEFWq799v7gCkZsjvEqqpYDg-xkanD8nbyHxb1phu3gCIxtH20_irQEGNeqrJnzeE8rwwwyLE1o2X1sO5Nlv9w6oID9dpjApTqIozaWGcZ28_1Tc2XzvWrhYcduNdqUgcXtDOp56QiPQCcUCae4k9wIPMnHc9gmfw7H6xx70wYOu8xQzsG-BRVWOUzST0T088tb8N6RQL_Pff9Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چند دقیقه‌ با قهرمانان سرآشپز  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/463652" target="_blank">📅 16:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463651">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3d78d3aaa.mp4?token=J-CKByoKk_RXCmiz2BzfR3kUCU0B32M1WSp5REizHW0AJcZYsDK_LB8wpLt8NfU7PEMe1mg7KudDuFQPMi_rYz_VNg-ZokGmT3_GRv3xXmy0l9AB7yIV5gIFJYYBJN--aODiEuyx_LdiLKH9Qbrpz9jjJVTVGooQhXMnj24OqdoZM_NhHpLj4YAvnqOHQhXof5BoKqgj54cvOGMTfnSsjLISjhntOnDXI-k-pB3QnidfIlXJSJC2m8WXKxoBPB1sNdcXNNeErMDVD2V1FbCPxlAq-8xhIxHZ2ozkzni1d-Sk_TinWYhZET_T9tmSCrXB-w7EQhVhDWrPqdb0Ny5MMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3d78d3aaa.mp4?token=J-CKByoKk_RXCmiz2BzfR3kUCU0B32M1WSp5REizHW0AJcZYsDK_LB8wpLt8NfU7PEMe1mg7KudDuFQPMi_rYz_VNg-ZokGmT3_GRv3xXmy0l9AB7yIV5gIFJYYBJN--aODiEuyx_LdiLKH9Qbrpz9jjJVTVGooQhXMnj24OqdoZM_NhHpLj4YAvnqOHQhXof5BoKqgj54cvOGMTfnSsjLISjhntOnDXI-k-pB3QnidfIlXJSJC2m8WXKxoBPB1sNdcXNNeErMDVD2V1FbCPxlAq-8xhIxHZ2ozkzni1d-Sk_TinWYhZET_T9tmSCrXB-w7EQhVhDWrPqdb0Ny5MMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
پزشکیان در سفر به نیویورک، در توقفی کوتاه با وزیر کشور الجزایر دیدار کرد.  @Farsna</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/463651" target="_blank">📅 16:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463650">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYvgAPYfSjMEeZOcHt4Snx0Wn2cvmPlhSRchnNS5uGPoNheMFGFafh4xIUl_W5wDG_tJb9lQispOpjBgLO069hYvHoGU1hsOBM0Q8Djx2bfSANwPKwITWPQjhaM-G_Ns0xfLsRnDEz95h9BbUvI8PXQN5_prcd-NueJSSoRY9he1X5eZ-XpNLCrrGQhX9u-oxAbCgfVmHgBwZT3XhlGlQ2dYtBkMX2r9Sf4bYF8Y_i3MMEyzmuWsMOA3yUdDpNghNaZOLDEsTGvUmfu2iTrDTCacpmhU3LXoexivI2__uVHZCh-OuRfkKExGvCd-VqmpCy00Gr_XlQaJV6gWwRFV2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوای تهران فعلا پایدار است؛ باران هفتۀ آینده می‌آید
🔹
هواشناسی استان تهران: گرمای هوایی که بر استان حاکم است تا پایان هفته باقی خواهد ماند؛ از هفتۀ آینده با ورود یک سامانۀ جوی شاهد بارش‌هایی خواهیم بود که باعث افت دما در سطح استان نیز می‌شود.
عکس: محمدعلی برنو
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/463650" target="_blank">📅 16:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463649">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b25661b35.mp4?token=HyH5LWjl7xIg2Nk1rOGmG6zHxQgTsS7MU5BIWzkFRfEPxy9GpiJY6-haHuw-UvEZ-NspNniM7zEZASiZPKaapXXvkVSUh5oiXoJElwFowtA4FvTO3oWu2_XfSPBkTJMYbkc4Vjqstx1GFEGQ1MpTJT038exU9bua1NBpzTivgyxr_B9-Hs8CPDZnAH845l1Bvzj0MsEOaCTCw5JpnKZs2M6pszGWQ2FNLxyPpxNWGNjFypjqsJ1QMYolbSHGLgTADEEjPHl-DSCFJuP63OpC61eFqhX9FkmnLlBkvo4CqyISjiPatE7TNMG7CoJsIP89pRSWNafQeloTpcwb7JtyN0_fIO_pruocouO2Q8sLSAd37fkEXM3hVXevddNOpniDtTiL9Ingp7oar8JpXV-AcgTvdsaqfkDWInCdYkcLp70wrDs5lIV5Y3m6kZY1sJK2pdHbVDdZsO46N_TqKqnozFcPPFAII__YJxUBnShSQuHNtGc1uPDNWDeTxRJS-CWJ1eDNu7_j8ulwcfQM6zOma25JrCrNM4SmXILQcgsjS-JBb9WcfGB5450OIaaZMt41TiIZ80kkukZkHxu3OyT2NqPDnXnIBll3Vdhm96Qeq2ZbOz1EBePV9lv5s4Du05WxbS0Al7qzCsaZbLlhWLh7T6dk65grsKC4kLOIROMjutw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b25661b35.mp4?token=HyH5LWjl7xIg2Nk1rOGmG6zHxQgTsS7MU5BIWzkFRfEPxy9GpiJY6-haHuw-UvEZ-NspNniM7zEZASiZPKaapXXvkVSUh5oiXoJElwFowtA4FvTO3oWu2_XfSPBkTJMYbkc4Vjqstx1GFEGQ1MpTJT038exU9bua1NBpzTivgyxr_B9-Hs8CPDZnAH845l1Bvzj0MsEOaCTCw5JpnKZs2M6pszGWQ2FNLxyPpxNWGNjFypjqsJ1QMYolbSHGLgTADEEjPHl-DSCFJuP63OpC61eFqhX9FkmnLlBkvo4CqyISjiPatE7TNMG7CoJsIP89pRSWNafQeloTpcwb7JtyN0_fIO_pruocouO2Q8sLSAd37fkEXM3hVXevddNOpniDtTiL9Ingp7oar8JpXV-AcgTvdsaqfkDWInCdYkcLp70wrDs5lIV5Y3m6kZY1sJK2pdHbVDdZsO46N_TqKqnozFcPPFAII__YJxUBnShSQuHNtGc1uPDNWDeTxRJS-CWJ1eDNu7_j8ulwcfQM6zOma25JrCrNM4SmXILQcgsjS-JBb9WcfGB5450OIaaZMt41TiIZ80kkukZkHxu3OyT2NqPDnXnIBll3Vdhm96Qeq2ZbOz1EBePV9lv5s4Du05WxbS0Al7qzCsaZbLlhWLh7T6dk65grsKC4kLOIROMjutw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۰۰۰ بسته کیف و لوازم‌التحریر در چهارباغ البرز توزیع شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/463649" target="_blank">📅 16:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463648">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhKUYbJviSaFak2vEzYAF33QLEMA-gouZt28zwEy3pw4STCpu5uhaTz0gOD10bqV6Svvoh9XvQCb3MEHfvwGPv43sOUw8lXJY5oqTlJ33fqbtSg0VgnX_kzpqIOML4teeUhKFr0lcl8j06dIOirwQt2uKt6eIMvK_ns7jZm4Co4IAU30eV7v_sXqfRPPKi5Dp5jFQaD83rru2zoLyKgKOIoj8I2alTyKgiZlCtF0ymUTdt6M1WsQgiLfSnhGTKfvUDFjFxMkvEKujsuffwvroUEpSdFUU8FZafJ5wEcus09vhQZ913vg35B0AuR8HgB0Aq8Jkdcwit53hV6oJrHVAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعات کاری جدید فعالیت سامانهٔ چکاوک اعلام شد
🔹
بانک مرکزی: ساعت پایان واگذاری برای چک‌های عادی ۱۰:۳۰ و پایان تعیین وضعیت آن‌ها ۱۳:۳۰ است.
🔹
همچنین برای چک‌های رمزدار و تضمین‌شده، ساعت پایان واگذاری ۱۱:۳۰ و ساعت پایان تعیین وضعیت ۱۲:۳۰ در نظر گرفته شده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/463648" target="_blank">📅 16:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463647">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دریای مازندران تعطیل شد
🔹
هواشناسی مازندران: فعالیت‌های دریایی در خزر به‌دلیل وزش بادهای شدید و افزایش ارتفاع امواج، برای امروز تعطیل است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/farsna/463647" target="_blank">📅 16:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463646">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aecabb426.mp4?token=TSQS5eM7q13POttOkl8XP3JeYyrdHCRHJNk34AwYQOVynoqLmj8C8WfXVeDTcFTQM6DtMOwSN5jWPoVhXXCdnsVtYi6qWA0I3RQQkfz4P2n3ZcEjrWNAyC1TTM7rVj6WebZ4B1encn4sfIx4XYYWjYPhDJUKlumnEwflOshU3t-U8ywXHcjq_czkwudfvNGiWJilEKP2KRpFImfpHekxa8U7GLFsH0yvua4e2I3ueE9wcDnOnNq5vRFWiYQKHeq6d5P0kkdXtnnB7W5qLhyz9bHGA5pZ2L6K1G2TcrIp1HBrfU_EthcHuuuZvjr2HZ5De6tRr01wKDCbcqDjX88aJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aecabb426.mp4?token=TSQS5eM7q13POttOkl8XP3JeYyrdHCRHJNk34AwYQOVynoqLmj8C8WfXVeDTcFTQM6DtMOwSN5jWPoVhXXCdnsVtYi6qWA0I3RQQkfz4P2n3ZcEjrWNAyC1TTM7rVj6WebZ4B1encn4sfIx4XYYWjYPhDJUKlumnEwflOshU3t-U8ywXHcjq_czkwudfvNGiWJilEKP2KRpFImfpHekxa8U7GLFsH0yvua4e2I3ueE9wcDnOnNq5vRFWiYQKHeq6d5P0kkdXtnnB7W5qLhyz9bHGA5pZ2L6K1G2TcrIp1HBrfU_EthcHuuuZvjr2HZ5De6tRr01wKDCbcqDjX88aJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی: در تریبون سازمان ملل مواضع بر حق ایران را بیان می‌کنیم
🔹
وزیر امور خارجه در بدو ورود به نیویورک در تشریح اهداف سفرش گفت: امسال پس از جنگی که صورت گرفت، طبیعی است که تریبون سازمان ملل، محلی خواهد بود برای اینکه مظلومیت مردم ایران، شهدای ایران، شهدای…</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/463646" target="_blank">📅 15:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463639">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BFnfJt31MYwYlpZrimq_nKFDIx6Y_JK4Hsh0UaYZL3y0dTFeLfGVdx6XPkArj5-1dOt6B1J9yxDVCfaOuQQ-yPwf_3qryI7Khl6g4r6k2I3IqTCtqPzBRbG4TwW6RtEy8P_ZbTpsT5IHbMYRcIhRvq79JgoB8BsVni1hrslyz0SCA0GvTNHER9TOb3lpx-o3gczfC4vkv4QpE9aKxSs27hNllvscJoxdXg56dkTJ0rNK_WYmDT_2G9iTDONus1D-ViKtvCe4cQ2GEh8JkyUoDN8Ily4D5_Ov4OYaniwFNPK8cTpct7qvHyZsYYDdpuTrVglHha5N_KeSq8M1vGwSDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fp1K3WUOdyNDoSPXcQtv_UOZTjvQMbzT2SGc7t4Uhjwhaafkg4JBELNTQDM6xDRcbca3uugaWOQfZBIGDzJT7LRqBIYVOz3ey2YaS7jtxk0-pAZqPLG6O8KFfdqFhnG6GQXs2aItf4-51Ta06yDasPlPCPduMyhaPYZx67caP5Z5CK1yO3yOfENuf0SZJg0cHSstZii2GD3_SPCmFo4DJPG48m_RfHeJviDUDIZRorX5Qu7lvA5Z7OWWbefamgiPAMyBu5wvJoNtZxJKa2lZDEsHEw5tGv0H99dJj0JW2kGcUIOEhwL-pIc4RfV7SiHBDQuH-tjpsdO-I2U3oFyDVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R6PkO54Mc0OCYUiuEQneukO77QbOkd2o9BGWPeoh7eTy9-ypsCvTRLwhXKz8ncrLvq1Pk1UghBK93sQftKnak7dEIVrelvPrLBrmii43e5OEsAlpQeeYbQW579oC5Cv_z72qNnfyh9tl1H7chu61xCrTDWEeSZG3sgcR-lvs9EoeGdo7xrhDc5S1va-wzxQRvDxTecrHNWIntdfq693pQIV1uBt2m63koeiRZgxPC9WuO-lREsR7ZJNN2QV1SeasyDF9ntHIhKbl-YVtUGm1nlXmGGjbY9ux13fq7YGtGsCZVhQC-06v3yEXSaJ5K5Jfr83w3dOi-z3-ieauOG0rmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y2CMUgGVEXjyOiyWLtkE7vWDiJUAq0Pm8WpciU6B55Cq-jJuJVRHlwDpim2498zhMUShUgsp584VCpI-Z35jbt5XpkgaJnQmm25V1Kc5l1Os8rsoyevIWH5FrOKqZmRkZgwkvH_c6tq18ZD4zx5oRGCEoHWoe0tXKYk7lW1OFu0Wb9jppYg3FuwoNLosdGssLVtW5YNMBIlndcLs4Sgwhvaehar_2mFF2pyO3nMrvfVmFezljm29ioMLv-_3O64mwSiqe7ZdEabYvAqRtf_cJgP8QzReef-UGzwT49Quz8UokSC8e9Gr7lgdshzlTVYPSdb9skbWhP8hvlIdCdj8kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YUToucCeQP8S1Nd7xxAtjFIo403GDFxoraf22sQz734OkmzJ-1qLTMnEXN8w5lHH4PlbuXexlFsDHRmJJTu9hKTYEOquYQUjDVgtYsiXZcdS6sttzenQ_A0Nt6bBztkAIJKkLKRDTHhkFdSg3wXbs20OYa-8QD7nBi1vLJ2RIOW-dRZ6QGTcNOAvURjuM7KCCVGwiYfoh-LbOC-zE943MeAulTGCjNgFRP44q2ozUCBe-Hdhb5DA8rG7nEQuq7sagR3C1lySpTVpfGIn_ozj1BgRvovbgYWHeE-OhnA-5zXzKoX_C09RXhTzzxi9iJvzgOUz7vUIexmrzTYo5wqpCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BISlwwUnyhiWGVCYVtMZ1Ayf84nzBr2WcgtF7nILQY6HR_KXrk6MtY-FRQVVDore_eqLSPc_y4X0jXJHtaVFDrvwk8_m27LskKfrNCkd640S9vBmFgFFQ4M0BaArr9KpITdy1UIEkyzm2pKU7PK5MeRsv2fL7JInEiC2SzmY6j4YK6r_Kzro6haFCUrqiP2rQZgNNDq-bQNOO4_wdqRftJCrQWBRQAVaqnb5HinoJAgIPR4lw0xNp1xAK_G0bWPrRHgzhMFE7jvZXcyi7yf9vxtNvPfxO9EfJaSFEctu0Nm4Uy__rSwqiwNgaqYw5tv6tUkbgh5DSGmdYpvhpHwJ0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LDUcofUnj_etv6Hr6Rxw1un94mVGJqNSi2q5Zumr8gy0T0r_KzTEvgldEUR_IPVJ-cnTOxa0MDOE4SRwPoRW0oZYI2eHyBnfb2Y-JtkLuNhl81wDJW0Bp_mr1E9UN1hjxa3XxHlgyQ_GnwZZjsap3RX-OTb7506_qKYfPwb-jCzWhbJUUzxPJdEBSXXhrLCDHHEPO1H3XAKQt3bv6_zp6RPY37IMDmGAJJwtr8DV5UMedT7HgLauWczKo_qpqhhzkgeFTwpS7o4bDeZxG7PdeNYfIUPJ8mtYRXwbOBG83sf-vWZl8YBG2TZjfYx8lodFMgPw24m6ikTYb1Uc2B79ag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور دسته‌های عزاداری در حرم حضرت معصومه(س)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/farsna/463639" target="_blank">📅 15:53 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463638">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7ce7b7633.mp4?token=fGm98n_XxgucfVoRGiGUagR4cI00aRZIv3YG9snuYNsHE3hlADOEYYDZHXzJbT2yGGM67JDeN6KFbkTWo0jXT9dwyrpV1MsW6TZo_SAuCakJoZaP9FeyClFEpzOBwkoUFsiQATCfP-BSxMCvO-ZJN56mXUKmlNC-U8wOi37QZz3vvq9_08zzjieWsnPon6_nSwbukDtQZ-g2xeMPOgsCDLy5k84hJabpbJYmZfjYhtBBHssZE_vtBwot5zZPP__yb602LAems3v3TzzB-SrUXiSWW3aknoa445t4uGBQDdgxk7MQK0SZxFOzWr8wBONQI57n9IQDYHV8G9RjEQKbXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7ce7b7633.mp4?token=fGm98n_XxgucfVoRGiGUagR4cI00aRZIv3YG9snuYNsHE3hlADOEYYDZHXzJbT2yGGM67JDeN6KFbkTWo0jXT9dwyrpV1MsW6TZo_SAuCakJoZaP9FeyClFEpzOBwkoUFsiQATCfP-BSxMCvO-ZJN56mXUKmlNC-U8wOi37QZz3vvq9_08zzjieWsnPon6_nSwbukDtQZ-g2xeMPOgsCDLy5k84hJabpbJYmZfjYhtBBHssZE_vtBwot5zZPP__yb602LAems3v3TzzB-SrUXiSWW3aknoa445t4uGBQDdgxk7MQK0SZxFOzWr8wBONQI57n9IQDYHV8G9RjEQKbXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شکایت ۳ رسانهٔ بزرگ آمریکا از دولت ترامپ برای بازگشت به کاخ‌سفید
🔹
شبکه‌های خبری سی‌ان‌ان، ام‌اس ناو و پولیتیکو برای بازپس‌گیری دسترسی خود به کاخ سفید از دولت ترامپ شکایت و اعلام کردند که «هدف از این اقدام، جلوگیری از دخالت دولت در تصمیم‌گیری درباره محتوای…</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/463638" target="_blank">📅 15:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463637">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6uM2d1IidGm7-JqnkrxqU5TA7tBy6hkIdAlNGrowEPHtceyxXRC_Qgk7WnEYrzVIBt6H0-fNcKU4cvkeGgswaSBIS0BXeV2R-aI_qZC9L7XR549NWg8Wk36vle0yZtIlRxA9JgO4BpCpqfEqKVvH5T-zkwiE53YqZmoCVwgBmGsSEf_wokylJG7iQ50bw4j0AtA38HfTNyInIZAsFsbvdx7pecnO_BJjuMxsFLRa_2FlF3H_9NoSOc_tzzEs2S3z2ELrvoh-7AxS3BmcUcmRju-v2hKoK_ahlW0N5fxWg0XMW3zoG1gX3vZZSF5qhcD-yQpLrjZX5N8tms9ALfsgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور پسر مهدی رحمتی در لیگ یک
🔹
سیدعلی رحمتی، فرزند مهدی رحمتی به تیم هوادار تهران پیوست.
@Sportfars</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/463637" target="_blank">📅 15:39 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463636">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/104b583a2f.mp4?token=Z-kkpvXiL0tvWu2alH-pD0qo8Y48OIBZelXkw2NUqHB94vFQJW-sjbdaXASX0HSZXR642plCxPnXFbUfwSmIx0MM0aF1TMm9X5BTkGfjhgdgEu0FtoS_s1vUhqFjnrSfYhJB0r44HcxovpXFhY5QIPl-H5o_XxEepBoguL5Yr7p6XJUbIUnZ_BXeo_uz4lbG07ulRCWqZnUGAZNLHLSV5l37E3Em2NNHEaKMEfRbS8y_0zCwKtQQqfXlotnDahExVqbsyPasErvDIWg0xPdgz4DpBNIQPOTgkGsiNSKRXcY2IElZgKKxsBJlyfEkCxjLmFL0DUAFPg1wOoXXz-Sb1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/104b583a2f.mp4?token=Z-kkpvXiL0tvWu2alH-pD0qo8Y48OIBZelXkw2NUqHB94vFQJW-sjbdaXASX0HSZXR642plCxPnXFbUfwSmIx0MM0aF1TMm9X5BTkGfjhgdgEu0FtoS_s1vUhqFjnrSfYhJB0r44HcxovpXFhY5QIPl-H5o_XxEepBoguL5Yr7p6XJUbIUnZ_BXeo_uz4lbG07ulRCWqZnUGAZNLHLSV5l37E3Em2NNHEaKMEfRbS8y_0zCwKtQQqfXlotnDahExVqbsyPasErvDIWg0xPdgz4DpBNIQPOTgkGsiNSKRXcY2IElZgKKxsBJlyfEkCxjLmFL0DUAFPg1wOoXXz-Sb1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هادی‌زاده، کارشناس مسائل بین‌الملل: ترامپ به‌دنبال ساخت تصویری ضعیف از ایران است؛ جهان می‌گوید ترامپ شکست خورده اما او می‌خواهد تصویری نشان دهد و بگوید که ایرانِ شکست‌خورده را پای میز مذاکره کشانده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/463636" target="_blank">📅 15:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463635">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb5f07b210.mp4?token=VCQaBwZnsP7Kx-zOaqA7_BKjOaGJmoK5nlv3iQFiOtKHqRq116cRw_2QFDc_KOOzA3tab0jxPZ5Inu_kogxPbet2Xy5tWclx-jPKKNkwyPGVHiUaYwo0Ae-E0Y0XEOSafojFaC25Jlt-3ytOIeu0ms4LMXe4VKOIit13n9RDlXN77bFF6HjbolfcgNPjV2Ylxi0N1YGB7Peeup69tQFNwDi2EezBrkduozl6-zol5UATS1nPW-JDdNxAXQ0KIw8GJtamn3dKKQChJp9NQAqJrhojEf1RDH7f88FaXlBNRSE-WxS4VAoxcB6kOIQT1WQ_fk6UXwKhmxjlUoOePGWnUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb5f07b210.mp4?token=VCQaBwZnsP7Kx-zOaqA7_BKjOaGJmoK5nlv3iQFiOtKHqRq116cRw_2QFDc_KOOzA3tab0jxPZ5Inu_kogxPbet2Xy5tWclx-jPKKNkwyPGVHiUaYwo0Ae-E0Y0XEOSafojFaC25Jlt-3ytOIeu0ms4LMXe4VKOIit13n9RDlXN77bFF6HjbolfcgNPjV2Ylxi0N1YGB7Peeup69tQFNwDi2EezBrkduozl6-zol5UATS1nPW-JDdNxAXQ0KIw8GJtamn3dKKQChJp9NQAqJrhojEf1RDH7f88FaXlBNRSE-WxS4VAoxcB6kOIQT1WQ_fk6UXwKhmxjlUoOePGWnUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر آموزش‌وپرورش: بیش‌از ۱۰۰۰ مدرسهٔ کپری و سنگی بالای ۱۰ دانش‌آموز در کشور جمع‌آوری شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/463635" target="_blank">📅 15:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463634">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWsW_SJfAG28YWQexcLyDlwtZdRLRhR3aI-ttC8t-B5DwCqRavEntcVoZ45CJ2aqyC9hwduIvTlaxbw8aRoCIxCj0pJ3_CrvZrllIXq4Zi4YqtK7kHkHkN2RuCBfaMam1qWWIwHshP9RqunaVfdlTALqRh1cJUiL0iSSELBzi_xPCMff1AG0H517xtUx860xYes4W2lv69WDfod2Bm-WGHZ70JA-XRoM3S6QGc_h7Ti0eTyCNrN4EO2N4f4kV97YhkBCzmYddcOB2FlvXEXskhIYx8AJvQTerVFhh-WtkV3VWXoKMRLiFLSIZG7DhcBrfdvAx0oK3rKTvkA0yc98lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس راهور: تردد خودروهای دارای پلاک مناطق آزاد کیش و قشم تا پایان آذر در سراسر کشور مجاز است
🔹
سردار تیمور حسینی: صاحبان خودروهای دارای پلاک سایر مناطق آزاد برای خروج از محدودهٔ مصوب باید با هماهنگی سازمان‌های مرتبط، مرخصی و پلاک گذر موقت دریافت کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/463634" target="_blank">📅 15:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463633">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20a49d3d78.mp4?token=rJ46mHgvmR8o0FBkVHTr9woNmtrQdMktUkaaxz6gtISScya3rIRpL7GYj5-GIP5ecXq-5RgiDmpQ5mcMjdOWKMxiQHcil9sHjRBgYMokayH-yFBLiP07lptH52H8Y0ZZyItP0iL8iMpDFSmTJm0XLOoraRnykpbrTFgbjLQUEwbS6jYFQEd3Rc24Mgl-yjHxdkntWtMGkg0D-m1Vr43LnOH3lyOY6_oCK8Det0NeqI7Zt2H1TDVdY6x2hHyYigvvah3xO1fhu__olOQ2j74lVGUs2ogBK4I4Hz_VMAVhtedvAY0IkF6fyTRitmHgeOY3YcXHQE5glu2yo2DLvLfDuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20a49d3d78.mp4?token=rJ46mHgvmR8o0FBkVHTr9woNmtrQdMktUkaaxz6gtISScya3rIRpL7GYj5-GIP5ecXq-5RgiDmpQ5mcMjdOWKMxiQHcil9sHjRBgYMokayH-yFBLiP07lptH52H8Y0ZZyItP0iL8iMpDFSmTJm0XLOoraRnykpbrTFgbjLQUEwbS6jYFQEd3Rc24Mgl-yjHxdkntWtMGkg0D-m1Vr43LnOH3lyOY6_oCK8Det0NeqI7Zt2H1TDVdY6x2hHyYigvvah3xO1fhu__olOQ2j74lVGUs2ogBK4I4Hz_VMAVhtedvAY0IkF6fyTRitmHgeOY3YcXHQE5glu2yo2DLvLfDuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر کشور پاکستان در سفر به تهران با وزیر کشور دیدار کرد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/463633" target="_blank">📅 15:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463632">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMJDb_vn2n3t-oZGD_cAtA561XaGTzrGN58OOgKU5hqEWjD-Gmaw3t6sDscirloorSdZqtQccjlD3kLPXPMEAaBAwghA_PokbRAyCoEcwC7c4Pn0yq4W5ZkqUfl1b2VWIKz6f1izodFeZHLZXDdkpD3mNNFENjaCtE_1LwSYfwg4RUYBifGXuuV39Sgx3ot_A2gqnXJuTy0eJqmM7gfEFdhg1Xy_ikgW21F0CEWw5n5iS5NajaKUVXZ10hhR9bHlgg21ASxyModGJc24v0I4q9d09McnWaLzNK5RmTsEfPFbU4OVXKnLEQX-qp7o_HU0ODdZwdNd90_cNgM5fbPvLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
انتظار رئیس‌جمهور از سفر به نیویورک
🔹
پزشکیان: امیدوارم مردم جهان از رفتارهای ظالمانه‌ای که در منطقه صورت می‌گیرد، آگاه شوند و مجمعی که با شعار «اعتماد» برگزار می‌شود، اعتماد را به جهان بازگرداند و برای پایان جنگ و خونریزی تلاش کند.
🔹
مظلومیت کودکان ما در…</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/463632" target="_blank">📅 15:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463631">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smAWikNq0GAwBShG8YnoyAAcWHCoNYswYSzwvsUme7SrIn-OYsh-myLbPpxGGjxQ0nJp6TLIx6EeHsHbSIJr4JP1y2NhjXe0xrbkdGjjqaDrm6GtQ4gT3LT49tgJYECd8Dgb1l1U1dXx4a9mKEN5bB_bgQ0gBVErOdriaNlFyR0iBXRRGufR3Dym-39lZXMCCNSeRZfwNYYO3Z1Tx6CyjfvtnlhBYm93V3zLL0bne9t5mGJEooJ85hUbl46nP4gqp0hPFzWkrPwOn1Y6TKl36LuOvnmtGWjlFCatoXEQV3H-aasWqrEMKncwtogimSbiGqyArGAkrNmxFsg3Zh7vnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تراستی‌ها چگونه کنترل و نظارت می‌شوند؟  @Farsna</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/463631" target="_blank">📅 15:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463630">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c2476eebc.mp4?token=LXkoLGlkF7YZXOqQLRkVLXwyE4FvBwl9jIGsGntKvehRVFCGn7YaZXOrs_o6KCXIfCuR-qRyaJpnZXOtBqqA49lAQt424hFfkH9J8IuxQ-xY1wRGwBhFIHgCr_qMVqjlD_yi73w1atuzBoroinSX7DAe9ingWzp5WThtaQreyH5ku-_51MeOkrvLoL8yIKDSX-JeY1JrOhU2AX3-xg-pLJB8TvVd0Fk6D46lIxikgbq7Y_LB9gs8U200P6OglfErr1HieiO_X-vp0Lx3NUveNvW7buVpMWNUQA1u49kX-bSHR1frBQZF_9j4r5G6wx9be5AXz_qr0G8pS-9Cb9iVNi6TWrtMQuTIFt4I8fK73FEN_1-7YjkTF1RwKWfWAVx8APdFLSNjUQfIg1nmZi86tIkwIFCj5QxPoAEZvw9Ywgpts0bysUCZpENT-i-FUcs6qr5jKopLiwEbXKexj26OWzM6_rkCuhkZMM5YdaaX207r30hvU974c91dFyr8YIEZNQLlLQE2wIHti2a1AJEAv0k8XZJY7U4c-AMDDyzF_Cds68dYtwH0oV9KC5TLj-lLvV_2LJLi-wbAhgOnWHKZp-x9l_pyOPQl6oPuwbo8octYaLaDWznfOmfn_T0hWIefrsz13NvB-8e9k1k7Vf-DBCh9BnevjPrtLFbuOa-tyMs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c2476eebc.mp4?token=LXkoLGlkF7YZXOqQLRkVLXwyE4FvBwl9jIGsGntKvehRVFCGn7YaZXOrs_o6KCXIfCuR-qRyaJpnZXOtBqqA49lAQt424hFfkH9J8IuxQ-xY1wRGwBhFIHgCr_qMVqjlD_yi73w1atuzBoroinSX7DAe9ingWzp5WThtaQreyH5ku-_51MeOkrvLoL8yIKDSX-JeY1JrOhU2AX3-xg-pLJB8TvVd0Fk6D46lIxikgbq7Y_LB9gs8U200P6OglfErr1HieiO_X-vp0Lx3NUveNvW7buVpMWNUQA1u49kX-bSHR1frBQZF_9j4r5G6wx9be5AXz_qr0G8pS-9Cb9iVNi6TWrtMQuTIFt4I8fK73FEN_1-7YjkTF1RwKWfWAVx8APdFLSNjUQfIg1nmZi86tIkwIFCj5QxPoAEZvw9Ywgpts0bysUCZpENT-i-FUcs6qr5jKopLiwEbXKexj26OWzM6_rkCuhkZMM5YdaaX207r30hvU974c91dFyr8YIEZNQLlLQE2wIHti2a1AJEAv0k8XZJY7U4c-AMDDyzF_Cds68dYtwH0oV9KC5TLj-lLvV_2LJLi-wbAhgOnWHKZp-x9l_pyOPQl6oPuwbo8octYaLaDWznfOmfn_T0hWIefrsz13NvB-8e9k1k7Vf-DBCh9BnevjPrtLFbuOa-tyMs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲۰۵ شب از حماسهٔ تاریخی ملت ایران می‌گذرد
@Farsna</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/farsna/463630" target="_blank">📅 15:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463629">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bby_tajgw3ToeF252tqYnV7skcUC4itgLdRNe9xrQvqYzKOLaA6apYzIfXzhHoxa7pZXBw6kT8cB-kM3_nJbb3MAN5m8XY39j2S9q-omQllKAZVWP5NOm6u145f_zahO1l72YrVdijA8JU5jzdQbMxtPKUr71V8oBt3MA-pp6-24pcG7JNAOzr1wQEkwGEUg68zE855bExaKaYHHG8bofCYJbdWGgcxLzhN2sYlyVWyuaoHxNoUY8hXMTNU7rzitUH5CW9p0sJBpqQzXa_iM4Ej6Bd9Q6ld-yy-wiZzjkbj677b5ZS90GzcdR-AV6Kgx6IM8rRIbNR9vpTwwdEyFng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر انقلاب: آیت‌الله‌ شبیری‌زنجانی عالمی محقق و ژرف‌نگر بود
🔹
پیام رهبر معظم انقلاب در پی ارتحال حضرت آیت‌الله‌العظمی شبیری‌زنجانی: این عالم بزرگوار همهٔ عمر شریف خود به‌جز چند سال اوّل طفولیّت را در مسیر تعلّم و تعلیم و تحقیق گذراندند و همواره از سوی هم‌ترازانِ…</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/463629" target="_blank">📅 15:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463627">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4601dd6ca8.mp4?token=anWhOXxy5GpErwviwb1EUY1YSaSGjMQAlVzD6F5gctt-sKUG4FuLhtEeEBu5oeQdHizU64ls0jqE5eAoyuS9ULpbOKsZmm9PIzKvACJ65aqQAjuG1dw_yQ2HyyvQ52OxbjUrSvWpnQ3quVVZsBez8iCrrGGTTWnsl2CEfYFCcC4YQ4Lb2prQSSPQOXHTbARdUvKK26mnKJYXBGhT38PiOFLX3CnX82svNXttJOX-pdaxoHBe35c4P5nZlQ_ywNHLrjLccCaj57HPeh8tRTvb9-bTYLz65OY7Bcuxpq52NReFrwNJdJeDVwktuBcptPDzsTQWK9okpEZ217mnoanLPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4601dd6ca8.mp4?token=anWhOXxy5GpErwviwb1EUY1YSaSGjMQAlVzD6F5gctt-sKUG4FuLhtEeEBu5oeQdHizU64ls0jqE5eAoyuS9ULpbOKsZmm9PIzKvACJ65aqQAjuG1dw_yQ2HyyvQ52OxbjUrSvWpnQ3quVVZsBez8iCrrGGTTWnsl2CEfYFCcC4YQ4Lb2prQSSPQOXHTbARdUvKK26mnKJYXBGhT38PiOFLX3CnX82svNXttJOX-pdaxoHBe35c4P5nZlQ_ywNHLrjLccCaj57HPeh8tRTvb9-bTYLz65OY7Bcuxpq52NReFrwNJdJeDVwktuBcptPDzsTQWK9okpEZ217mnoanLPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۶۸ دانش‌آموزی که جایشان در آغاز سال تحصیلی خالی است
@Farsna</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/farsna/463627" target="_blank">📅 15:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463626">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdsIuMnoP_hcNkX5d6j4yrJpH5KDa1UATFzIP4q-dSIq0YK9MkLFUEB-rT0yldg7kSoSHs52Bf8v1n6LJRlOfmHfify98KKu9b1Nimwu4CSpwmsetqaBcnA91jF6Z8LyIB7KjYs1oJ_-vYMq9flsbVO-G5fQ_28KNvRMfsyrCPLlpqBsvtSDJN8w0_c-LJa1mUqNqQvbzMIKgQw6TWitfNh5O842mCAlxhei3pjBLATpS7Ma35is32zvC02FU162AVALm1OnpWFH7YHz9rMxg0MxtiJR9IFPIgRnBQi0O0UWxmYfUxreihiSn9hrmnTaEQ91d6a2_5Mdjzi8jj4XfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترافیک سنگین در چالوس و هراز
🔹
سازمان حمل‌ونقل جاده‌ای: ترافیک وسایل نقلیه در محدوده پیچ‌های جاجرود در محور قدیم تهران - بومهن و حدفاصل پل فردیس تا پل کلاک در آزادراه قزوین - کرج - تهران سنگین است.
🔹
همچنین ترافیک وسایل نقلیه در محدوده رضی‌آباد در محور شهریار - تهران، محدوده قلعه‌نو در بزرگراه ورامین - تهران و محدوده شهرک صنعتی خاوران در بزرگراه پاکدشت - تهران سنگین است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/463626" target="_blank">📅 15:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463625">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4680134550.mp4?token=ZFzJxrLdG1Bqh4X2VhCc9lA_sZdSDKHDOmFpFMmdAsoDTqGce0nnxqcu0RXsHapxUYotHhYIKOrXiyj5x46KawXCGbEOaucW8hT1JKPp_zxiBS8mBT_oJ7sh9eJL9aPMePpv0i6stACKry2Uch4nYm0P1cFubEWO1iEq8-oXIFvZEANRhSpE4xn5bQjA219WAsZkx70bBmMFBMCCbvqZFviu3N8JN4cDEqF4G_w1wz4FJi9W2InW_1lJU2oxFN1k45VOUYlUudeoFK8g5JgP1GQjYZpWzLEQREPX5wik9gwO6IGbODE_0LTM6siFRQ-XGRw-Vd6QhtfQMGJqkY6I_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4680134550.mp4?token=ZFzJxrLdG1Bqh4X2VhCc9lA_sZdSDKHDOmFpFMmdAsoDTqGce0nnxqcu0RXsHapxUYotHhYIKOrXiyj5x46KawXCGbEOaucW8hT1JKPp_zxiBS8mBT_oJ7sh9eJL9aPMePpv0i6stACKry2Uch4nYm0P1cFubEWO1iEq8-oXIFvZEANRhSpE4xn5bQjA219WAsZkx70bBmMFBMCCbvqZFviu3N8JN4cDEqF4G_w1wz4FJi9W2InW_1lJU2oxFN1k45VOUYlUudeoFK8g5JgP1GQjYZpWzLEQREPX5wik9gwO6IGbODE_0LTM6siFRQ-XGRw-Vd6QhtfQMGJqkY6I_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سی‌ان‌ان: هرمز بحرانی بزرگ‌تر از کرونا است
@Farsna</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/farsna/463625" target="_blank">📅 15:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463624">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/622fb68d3c.mp4?token=YPjR0eaglwwJcsZcPNdnoo_18o0nDVEQNikLZH67SgU8ZU478CfSVkoAXubzCyQUH8VPv5Zra1_VgudQNhkMym1E6ejvlMOEyoGHMvRLvXslX5IcjMLOHLom5CoU2wNuKWsswHjzRnwaOtPFhCYSsWdCCSYEMXot5segJsl9U_wvwoS9kiXxrEXW-QoP2baMuencjB1s7QY-AKanIww3f7c4ZTyxRiVqYP_HNvKWWB3Ugm4RjB3FtlCLxwQtRfy4cH39tDQjz7oigPugkYsENjYIels0WjhlsYLTWu3diLlUwVxfS-zHhHOEKpJS-ZDvPIhqRQgth4A1RizZjn1Fyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/622fb68d3c.mp4?token=YPjR0eaglwwJcsZcPNdnoo_18o0nDVEQNikLZH67SgU8ZU478CfSVkoAXubzCyQUH8VPv5Zra1_VgudQNhkMym1E6ejvlMOEyoGHMvRLvXslX5IcjMLOHLom5CoU2wNuKWsswHjzRnwaOtPFhCYSsWdCCSYEMXot5segJsl9U_wvwoS9kiXxrEXW-QoP2baMuencjB1s7QY-AKanIww3f7c4ZTyxRiVqYP_HNvKWWB3Ugm4RjB3FtlCLxwQtRfy4cH39tDQjz7oigPugkYsENjYIels0WjhlsYLTWu3diLlUwVxfS-zHhHOEKpJS-ZDvPIhqRQgth4A1RizZjn1Fyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۸ محصول دانش‌بنیان برتر در نمایشگاه پارک فناوری پردیس رونمایی شدند
@Farsna</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/463624" target="_blank">📅 14:57 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463623">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">۳ فوتی در برخورد موتورسیکلت با قطار در نهاوند
🔹
اورژانس همدان: در حادثه برخورد قطار به یک موتورسیکلت در محدودۀ شهرستان فیروزان نهاوند یک مرد، یک دختربچه و یک پسربچه جان خود را از دست دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/463623" target="_blank">📅 14:53 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463622">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d27d0edf56.mp4?token=VU8UFsfxXF67n0LA7zmw-UiwdZZsTswMMKSA4e_r1Jg1UAFxjdi45HBGV0IoSQaC5PKpK2pufT7SXeZ4FZBGueTd4P02ILYzLhEk1loUI0QPOhgOdeGGHpiL0wos3WnOSxK-SC9BOQKBv4WixDzCED7cyPVsY12Y0VKKAFxmFY85dovhnppUVAi5W_6rvdzkO95eB6ksIJor5t7pfhQQXCeFbeOD4PEVEsQTxsmFXB2MUxy59biSPN-lmuob55gpUy1KZ5avco2lqMod2F8UDXu87ylqmMa33v22f9D77G9YxD_O-pfImhccwJBiNpd3XVIskzK7HhoYpLiuTxj7Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d27d0edf56.mp4?token=VU8UFsfxXF67n0LA7zmw-UiwdZZsTswMMKSA4e_r1Jg1UAFxjdi45HBGV0IoSQaC5PKpK2pufT7SXeZ4FZBGueTd4P02ILYzLhEk1loUI0QPOhgOdeGGHpiL0wos3WnOSxK-SC9BOQKBv4WixDzCED7cyPVsY12Y0VKKAFxmFY85dovhnppUVAi5W_6rvdzkO95eB6ksIJor5t7pfhQQXCeFbeOD4PEVEsQTxsmFXB2MUxy59biSPN-lmuob55gpUy1KZ5avco2lqMod2F8UDXu87ylqmMa33v22f9D77G9YxD_O-pfImhccwJBiNpd3XVIskzK7HhoYpLiuTxj7Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
درد پا به دیسک کمر هم ربط دارد
🔹
توضیحات مهم جراح مغز و اعصاب، درباره ارتباط عصبی برخی بیماری‌ها با بخش‌های مختلف بدن
@Farsna</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/463622" target="_blank">📅 14:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463621">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCY_qKR4kRP1IT3AxVpMsr-abjsnWr5PGx5SAhZrtOrUIoX0qOno5g0mIU9HF8VFqXmSRW33Unfio06Y1ToC3qcL6Zlrp8D1BcCTYYnI4DAZPA_z2SafprF16oRP3_9Cm2ZXQbFyovc46AtO7sfJhirHCnW0pq3O5bOjy4I1ljqFXNIfeVwbaTISUM639ZfGJkRSTB4uTnI5Cv6XAtJZVg3nD1G9I4PX3Wluva7BcHEtSfSGlQC9tKEZIOyzVaHg4Ymp89GJSNlXNqtL3D4dBq-43q-9y_20x_8mPtmUmDH0u6_kLemm1iiG0-ZgxHaDtkem0-D9jZkvkrA_P9Hz2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده‌کل ارتش: شخصیت شهید نصیرزاده حاصل پیوند دانش، تجربه و میدان بود
🔹
امیر حاتمی در دیدار با خانواده سرلشکر شهید نصیرزاده: شهید نصیرزاده در مسئولیت‌های مختلف، از فرماندهی نیروی هوایی تا جانشینی ستاد کل و وزارت دفاع، با نگاه راهبردی و شناخت دقیق از تحولات منطقه و محیط پیرامونی کشور، در مسیر تقویت قدرت ملی و ارتقای بازدارندگی جمهوری اسلامی ایران گام برداشت.
🔹
آنچه شهید نصیرزاده را در کنار توانمندی‌های علمی و نظامی برجسته می‌کرد، شخصیت انسانی و اخلاقی ایشان بود؛ فرمانده‌ای شجاع، مؤمن، متواضع و متشرع که مسئولیت را برای خدمت فی سبیل الله می‌خواست.
@Farsna</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/farsna/463621" target="_blank">📅 14:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463620">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7H1qebvZcKo2xPfN5jNiSdFm2hnVyEXNE1RpFUi4qoNSO5jx7CfvyQ2-CVe30zJ_AcR35s_gU-TftaXdVLjRF04EH0IxIBiTpkLERdqRwGU2WVvdSYN_wTjJhhJhGG_NT0MVu4vFcQ7uRaf2IoRzSkrIWZFTSqD4vVoOOH33wJTvkIA9R0DFOlKkp90BpXS81vY7hvD22Lpez-I8TKCuY2WmX-mSgCnjPH8B41hH8T41zU2Ld-Q1HkKyx5CSOetVQwwtGj8ZNwE4s-yUw7qytwcjKKNSv9_LGD4MZvA97axjm3t5lWfG07TvESt290RuOFOr7GsA8w3Xmu8Mu6beA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان در دیدار با وزیر کشور پاکستان: ایران و پاکستان از قدرت‌های منطقه هستند
🔹
امیدواریم با توسعۀ سرمایه‌گذاری‌های مشترک و تسهیل همکاری‌های اقتصادی، شاهد تعمیق هرچه بیشتر روابط ایران و پاکستان باشیم.
🔹
اقدامات و فشارهای آمریکا، زمینه‌ساز افزایش هم‌گرایی…</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/463620" target="_blank">📅 14:39 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463619">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wljn7f4wblRSDL9hx0juxQBAWu4_pEYGRikZqkp1bXh57ShSfvjCFsBfDSG6QiXccv6N3dEJcc9ardLTosHi3Pa5UucRAK7akzUZxE1fUzuPQpWJDfUeK-ht4N7jELKoDacRritoavNrpMxe-qySY58knxovoPwI34-s5OYCTZJLZ0_u1rr5V_kA_jX4R8IqOja4fIydqG7sAjmfwYMlC3EcgazdCNwhN5q9hKmvHONhQl4HT_SFDruhLefePuL4ENtZUA9HOl7anRS2fwCgkEEzDqd_uxnvuyExbGWpd_1o7Ye5bMBSPqRRSwhI27ChZBU-WQeXPiEqq4TYa21Vcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروازهای فرودگاه امام به ۱۹ کشور برقرار است
🔹
مدیرعامل فرودگاه امام خمینی(ره) تهران: طی ۲۹ روزِ شهریور امسال، در مجموع ۳۱۰۹ پرواز ورودی و خروجی در فرودگاه انجام و ۴۴۵ هزار و ۱۱۳ مسافر در مسیرهای بین‌المللی جابه‌جا شدند.
🔹
این پروازها به ۱۹ کشور شامل ترکیه، عراق، چین، گرجستان، ارمنستان، امارات، عمان، روسیه، افغانستان، پاکستان، آذربایجان، تاجیکستان، تایلند، ویتنام، ازبکستان، مالزی، تونس، قرقیزستان و ماکائو انجام شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/463619" target="_blank">📅 14:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463618">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4d0565582.mp4?token=JzRBuA2GKuH4gXjUltWHoZt-CVT4-Sm1BCqZGwuyD7t9vobIRmaqp9-ODkkKF7uLqYIlG9aGwkGPdudpdVNSCwHoQjGSozXJm-LZQKG26D4Ml8pfK-vWbYYGAZmUOarg3M7DN1KDgXqqJv_XQaqHHfjc1SzTEaWuOOCd99Xv3uUKhhxGHuBpB2P7A_08DFrwGSQzHPb29e2yQYRRB8CCkWiYAPwHx7J2D1r8GlLGioO8978FVyHJvcRncayuOCO-lDylQxZwufU6s80d-E4z4Hl7JMZvVHUR0S7PmDCmSp_e8jUlFu-LP_lwJC6xloZRKQCQ9TfkhtRgEGsDnT90TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4d0565582.mp4?token=JzRBuA2GKuH4gXjUltWHoZt-CVT4-Sm1BCqZGwuyD7t9vobIRmaqp9-ODkkKF7uLqYIlG9aGwkGPdudpdVNSCwHoQjGSozXJm-LZQKG26D4Ml8pfK-vWbYYGAZmUOarg3M7DN1KDgXqqJv_XQaqHHfjc1SzTEaWuOOCd99Xv3uUKhhxGHuBpB2P7A_08DFrwGSQzHPb29e2yQYRRB8CCkWiYAPwHx7J2D1r8GlLGioO8978FVyHJvcRncayuOCO-lDylQxZwufU6s80d-E4z4Hl7JMZvVHUR0S7PmDCmSp_e8jUlFu-LP_lwJC6xloZRKQCQ9TfkhtRgEGsDnT90TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سازمانی که صداهای حق و ناحق زیادی را در این روز شنیده است
@Farsna</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/463618" target="_blank">📅 14:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463617">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d64b04866.mp4?token=KgQZyBl70ALpP6EXeJe9koVgRfK12rM-PatZeF8yfTT5TYDvDufTcHiTeJpDr5fZhH54dccAIB3R7g1yLTOdJf7Srm-J4RbjNPXSkyyMhgCe3ZIjYsOKhJH9BBcFnhRUBh6o_qQ2kLNZ6RDzva__qC2vhhKjRyOqIusc6wvlpg8HAQJQRGpbmqFYHCh2z-0ZHkxi0U1DbH0_96y9Kp42xwCH2EE9t8so3XSOfqsLVDk3TYfpui3z6cQ4usdxwSJbI9_cWcFhIGwxaRbaTx8xflnfYOz_7wn9hUhiZsNQBVnoeluMP2p5KOYArZkqqr1MvnBogf3VyDV7pl33sk03Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d64b04866.mp4?token=KgQZyBl70ALpP6EXeJe9koVgRfK12rM-PatZeF8yfTT5TYDvDufTcHiTeJpDr5fZhH54dccAIB3R7g1yLTOdJf7Srm-J4RbjNPXSkyyMhgCe3ZIjYsOKhJH9BBcFnhRUBh6o_qQ2kLNZ6RDzva__qC2vhhKjRyOqIusc6wvlpg8HAQJQRGpbmqFYHCh2z-0ZHkxi0U1DbH0_96y9Kp42xwCH2EE9t8so3XSOfqsLVDk3TYfpui3z6cQ4usdxwSJbI9_cWcFhIGwxaRbaTx8xflnfYOz_7wn9hUhiZsNQBVnoeluMP2p5KOYArZkqqr1MvnBogf3VyDV7pl33sk03Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی سپاه: اگر آمریکا به کوه کلنگ یا هر مکانی حمله کند، مقابل آن می‌ایستیم
🔹
به سردمداران و هیئت حاکمه آمریکا توصیه می‌کنم مواردی را که قبلاً تجربه کرده و در آن تجربه شکست خورده‌اند، بار دیگر تکرار نکنند؛ چرا که آزموده را آزمودن خطاست.
🔹
ترامپ عادت دارد دائماً تهدید کند و فراموش می‌کند که پیش‌تر نیز تهدیداتی مطرح کرده، اما نتوانسته آن‌ها را عملیاتی کند و اکنون دوباره تهدیدات جدیدی را مطرح می‌کند.
🔹
اگر آمریکا بخواهد به هر نقطه از ایران نه فقط کوه کلنگ و نه فقط مکانی که مورد تهدید قرار داده، حمله کند، ما با آمادگی کامل در مقابل حمله آمریکا می‌ایستیم و تجاربی که آمریکا پیش‌تر از نوع مقابله ما کسب کرده و در واقع مانع رسیدن آمریکا به اهدافش شده، مجدداً برای آمریکا تکرار خواهد شد.
🔹
ما برای هر سناریوی دشمن آمادگی داریم و دشمن در هر عرصه‌ای که بخواهد وارد عمل شود، قطعاً پاسخ دندان‌شکنی به دشمن خواهیم داد.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/463617" target="_blank">📅 14:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463616">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JYwA2G6VFgUYGEMUC4XSq9ObRiJOMQoqvUIMxYSmH4cb1TY_-xwaGBtVuvplo81HYZ4RtjXRm88HjIQCrBc5UgTq34p8pWARbGQPvvDn2G9lvQaFUUxuxxNilccsk4af1wyzQ3HxcawbPDvf-ns0Wt9idnly2tWNVz3JPxeixdMItJ0pm1gU1bK4qQfp2OrjuFQ6RYp7iFhZG79VUCZFjcfEwJfI3_XxSt9Z-yC-yS8finUtx4USF8HYHchCHKilfAE73cG4BTIZpQ9HGdFiC0UjnpHiWc0RkBNLB0cH74s6-UkV52h7GDw3HQ8yI7E-qPuYUtP11uXMWTkOZPDzRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر ایزدی: توانایی هدف قرار دادن شناورهای عظیم دشمن را داریم
🔹
جانشین فرمانده کل سپاه: پیام ما به کشورهای منطقه این است که باید با یکدیگر امنیت منطقه را برقرار کنیم و آن‌ها مشاهده کردند که پایگاه‌های متعدد دشمن در ۱۲ کشور به نتیجه نرسید.
🔹
امروز رزمندگان اسلام در ایران از وضعیت و قابلیتی برخوردار هستند که می‌توانند با موشک‌های بالستیک، شناورهای عظیم دشمنان را هدف قرار دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/463616" target="_blank">📅 14:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463615">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">احتمال مجازی‌شدن مدارس در برخی مناطق جنوبی کشور
🔹
وزیر آموزش‌وپرورش: در کل کشور مدارس به‌صورت حضوری فعالیت می‌کنند؛ ممکن است در بعضی نقاط، به‌ویژه در حاشیهٔ خلیج فارس، مشکلاتی وجود داشته باشد که در این موارد استانداران تصمیم خواهند گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/463615" target="_blank">📅 13:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463614">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J6agn9-B-IZPx3cV5n-J38w8v9NrYKEerhZST9Nbb5KDBkUiFe2lSCS0YoSfEiVAuRpSIrEtGAYN3Bn1kiVYD21Y4NVTbtNq2IAPU-YwjDfTcoex2EmrWz1QrVowe1eK-JbeXOvBlmhs0nlLoXZetLXMBAimg-E7rFjceFolNNUnX0sCLDzJ58kP4AAYMmBqMFks6D1Zs1fxEGoU9TKnCmfwVtXPOw9CfMjZImOT_HqXOdTJ2XO7iwJTEBD8ZEUt7H7dKfrJ6vl4vBq33Gxm9stjTs0t8D1kf_C6ByBp3mmJ2EKPJvNQUM8h2i2Bub3KBgc4PKvQ8OE9qKIDvxbaPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان در پلی‌استیشن هم حریف ایران نشد
🔹
در رقابت‌های بازی‌های آسیایی ورزش‌های الکترونیک، ابوالفضل آقایی‌نسب از ایران در رشتۀ eFootball Mobile امجد عثمان از عربستان سعودی را ۳ بر صفر شکست داد.
🔹
حسن پاجانی هم در رشتۀ eFootball PC عبدالعزیز فلاح از عربستان را یک بر صفر برد.
🔹
بازیکنان ایران در بازی دوم مقابل کره‌جنوبی هم یک برد و یک تساوی به‌دست آوردند. در بازی سوم هم ۲ بار قطر را شکست دادند و به مرحلۀ حذفی رفتند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/463614" target="_blank">📅 13:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463613">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-r-OsWwSDqryN_0cPik2jfLtYGR8v_lCW2_mnElcymLh_qSH_yU3aRy9nB6fRBSiFV9L5J0Ofyr8A50_mjEOBPyx4c6y-NnSLh1wyAmOZVjr2w6eMnmxMc47HHS2R8wn7vca5Y8UbfDRNJc_Y7FsXSClXqYfAfJPx9Pyno6jgwmTmHbMrtUzlEUk6-Ohm8v38KgYjW6Nwkduq7lZ5rXAt_wG9rCXyxx8LwvuwyfyO4jzcOHCYvFDrLOTWGbtS82gXfTJJm5cPN34kZ4d83qpdQixV8zSW95EMW6pCM2F5J19QB3gGMnMNFuhLOuPkwUY5uxV2TnnEsew9aiwMu3eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدون تیم رسانه‌ای عازم آمریکا می‌شود.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/463613" target="_blank">📅 12:49 · 31 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
