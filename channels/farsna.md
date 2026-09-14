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
<img src="https://cdn4.telesco.pe/file/bW6ZOHDRiJ7isjHmAw30g7F0CM8osxjz0rsXHRM9mPErjNGoYWG-fqpbALY9hCiFnJcFMpsecnmW6xXqbdvnnlJIltgZ6E_Dwg-hA0F2HQiVSd-x4K-7DNoFDW_M1WALRwJKkl09rQ4UCPFQ-MLt35YAC2GBy71J13p2UqmROYvHLG2SO9kELF0meo3hldsfCAlb3Cb4n8SV04fFOTcE5OH3MZR1QOpgmgfO_sFJkaWGIllV7VSeNY5l6MbSEX3-OtgV9DTlk1zvpbKil4tXIG_FpthxdDpMMeq67S3p8lVXq9r7yvb8uUb8dzOKSJtq899C1zVEVvxACkhANJYEKg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-23 18:37:23</div>
<hr>

<div class="tg-post" id="msg-462029">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b3843af59.mp4?token=nNvRhgnxsFhDsxD-T0oWea_K3LuN4ZW7EaoM85VD_rn3XUgbLNx0UYSRymwHHACIa7LlL0Z-Tbzjhz4UJESMTx6BXQQQfxELc9ZZhTlIwcQTKHiZNoTQOqtqwtRTDdibsGNXzdJLd6WTlE92VNElZbim_No8xZdT_6rIVQEzBqRd5ZCwx1fkNcJ3pXckXvmq_ZBcBSgSRn-hwjdLvjsiR-Ry5_mMYVisBMGVTlKggzI0kD3ojD3T42x4_rrKNSPjKGN0_LX0AQ07jl1E4UhCIwZT-VzzVpzDPECS6Rtp1T4lgGlBQwiAbbWLVf7Re0OxuUB9OQ4LItttruix7E3RQj1XwrCPcc5bu3C0EsEBXuXgEEG0pKBoi1W065b7nAUk2IvtY7Eg71zHfGxTJrShKLIC1n_0jiIC0McPY3MEx5-wLyCQ_smqtNuOKaYmG4xe08NrK8yOgdmqmuBVBksaU72MuI7E60jiiw-gNEw60Jn5Nsa65VlDFXyPqz_hcdNoG6lrRnBWKA3tFFW6rIyXuTVynaMZ-QC_ClCbjGGD7fu7D4yFmX00YkULmp4OMiCya9XhAl4Ggg6mgpnf7L438oEmT1rM1503__XhinmjpBH6saZ7BqbOTzIYgnfAU2728B0j5AhZV47hD4naDOg-W1i6GGIURiCK9o8bI3arV5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b3843af59.mp4?token=nNvRhgnxsFhDsxD-T0oWea_K3LuN4ZW7EaoM85VD_rn3XUgbLNx0UYSRymwHHACIa7LlL0Z-Tbzjhz4UJESMTx6BXQQQfxELc9ZZhTlIwcQTKHiZNoTQOqtqwtRTDdibsGNXzdJLd6WTlE92VNElZbim_No8xZdT_6rIVQEzBqRd5ZCwx1fkNcJ3pXckXvmq_ZBcBSgSRn-hwjdLvjsiR-Ry5_mMYVisBMGVTlKggzI0kD3ojD3T42x4_rrKNSPjKGN0_LX0AQ07jl1E4UhCIwZT-VzzVpzDPECS6Rtp1T4lgGlBQwiAbbWLVf7Re0OxuUB9OQ4LItttruix7E3RQj1XwrCPcc5bu3C0EsEBXuXgEEG0pKBoi1W065b7nAUk2IvtY7Eg71zHfGxTJrShKLIC1n_0jiIC0McPY3MEx5-wLyCQ_smqtNuOKaYmG4xe08NrK8yOgdmqmuBVBksaU72MuI7E60jiiw-gNEw60Jn5Nsa65VlDFXyPqz_hcdNoG6lrRnBWKA3tFFW6rIyXuTVynaMZ-QC_ClCbjGGD7fu7D4yFmX00YkULmp4OMiCya9XhAl4Ggg6mgpnf7L438oEmT1rM1503__XhinmjpBH6saZ7BqbOTzIYgnfAU2728B0j5AhZV47hD4naDOg-W1i6GGIURiCK9o8bI3arV5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهادت امام جماعت اهل سنت مسجد محمد رسول‌الله زاهدان
🔹
مولوی یوسف گرگیچ امام جماعت اهل سنت مسجد محمد رسول‌الله شهرستان زاهدان توسط افراد مسلح ناشناس به شهادت رسید. @Farsna - Link</div>
<div class="tg-footer">👁️ 350 · <a href="https://t.me/farsna/462029" target="_blank">📅 18:36 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462028">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gb_2zvZOw3OCpJgOHkAq9BQDCvsKWeDgnSpvKsdvENHUCSYo_fuaZC0U544sgtnsXsBsI0-08G5oDtijix1W7jnC0vnlrvaK8DiNpNFxhBraZvevxOBH-cZkn4aqGNdwSE2fb_Ru-H3sn5mroW9xZwWYmvx4AWqj5URoQLWhWoE4Pl8hb1wIBzm8iUsYrvzu65zBZuc5ESsSZugd-MJMqKm0iVHRm8-35Di9hPxS-iK_LgR1VIOVwnVjnH1JW4D1O2Y5D3CZlZmRgtOFnqBhO0BJYAE5n392ONrf2GY3cQpUHarhoDaz3FEICRtU1rXJ-AsmYvquNLYaG-Emkz1nzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورود خودروهای مناطق آزاد به کشور با ۲۰ درصد تخفیف
🔹
مدیرکل دفتر واردات گمرک: به مالکان خودروهای مناطق آزاد اجازه داده می‌شود با ۲۰ درصد تخفیف، خودروهای خود را به پلاک ملی تبدیل کنند.
🔹
این فرصت فقط تا پایان سال ۱۴۰۵ اعتبار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 996 · <a href="https://t.me/farsna/462028" target="_blank">📅 18:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462027">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7o_xomr9OTUc-oAT1VrkpWh6Z4aliCfwGZ9lujnI3Vgc0ZO7zFlnTb_0e02KVTstXA3EaKM2wZZcOk655PdU_4lyubHieEgwKRAEbXzXmgUPzsUGZt2ioUewzrv2RcDLPguV1gGZTeAIJ69MTeJEDjmo-iJwopDzchR6I-Vm0sS9OrIgW1eCnduppJqIiS4Qgbln8b1D0ylZWs7UPjQK7Rl6LDfV5G7knh0MUGSje04eQZhIl15EM62C2o6UXxUWZ__tjm60FUqzE1kF3Wa00bXfmSOkgiROFi_3wRw9tDibsEIqyGcFNTAIsoXjv3O9dJcWSitF18R33qW-InF3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عضو ارشد انصارالله: ادعای ترامپ دربارهٔ تماس ما با آمریکا یاوه‌گویی است
🔹
حزام‌الاسد در پاسخ به ادعای ترامپ مبنی بر «تماس حوثی‌ها و درخواست برای مداخله‌نکردن آمریکا» نوشت: ترامپ که طبق معمول به یاوه‌گویی و دروغ‌پردازی روی آورده این بار هم روایت‌هایی بی‌اساس…</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/farsna/462027" target="_blank">📅 18:23 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462026">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">علیرضا بیرانوند: هراسی از رفتن به سربازی ندارم
🔹
هر تصمیمی که قانون بگیرد، مطیع آن هستم.  @Farsna - Link</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/farsna/462026" target="_blank">📅 18:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462025">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0e6c285df.mp4?token=iYvQT4Qr1pkfYTCdHUU_n1HFIqNS5LFgV1JUVohMqNav9ZRFb4B9JLadl0J-XloLuIHPbVPPVMBemzjETedXRdJrEtr4Gz0iCPUoXcGQDKI3C6K_-y53gEG9vhVHW5ZD5W4PEdCG9NnF_ktVSow5oCh8u71k1IX-mEhEYMvr-lJ_atJhZquq9QTbE62caLCN0-0OZwavVtZ8wEWDbmHQZen_K7MKcRhk2v6LnQG8GWm5s35_jZ3JNMqS1MTWaQOSut5JMpBfmRhTgloPtvPmfAsGAjG2Wk1J5nGkF4y2dsVTgj41sRTeKJ70996EboJoPdEUzVKbCy6WTVA0w5np1jRS30DZIBJ0qcNbagzP6s7hs1J0PmV0AKAESSq7UnSt2-B2K4BQNh4X20WHDGvTy8JwSTWr3Dd01Bc4hrWmezs0ettlMSH68VnmuZlVPgdSjXXHmXcXRaPH792qtSVgYnak-52nkXJZmdc-5f0JDU8byRhgvQhHRItntUY2BVlYwLUaBihpvM4no6kNEaaGdGZJvbJxHW35sLSKoBjnNLzODdBM83JDZ19tsLZoWIKZxC42wGEJK7L-SrYWOkzYekcDrZm_Czm2pLWKyrch15KyN83oeHgnkcJYXzhqlJU3uGT0qDW4tw6OXNtJtTdAwe9OFC7CHXeuyZdFYONnbUM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0e6c285df.mp4?token=iYvQT4Qr1pkfYTCdHUU_n1HFIqNS5LFgV1JUVohMqNav9ZRFb4B9JLadl0J-XloLuIHPbVPPVMBemzjETedXRdJrEtr4Gz0iCPUoXcGQDKI3C6K_-y53gEG9vhVHW5ZD5W4PEdCG9NnF_ktVSow5oCh8u71k1IX-mEhEYMvr-lJ_atJhZquq9QTbE62caLCN0-0OZwavVtZ8wEWDbmHQZen_K7MKcRhk2v6LnQG8GWm5s35_jZ3JNMqS1MTWaQOSut5JMpBfmRhTgloPtvPmfAsGAjG2Wk1J5nGkF4y2dsVTgj41sRTeKJ70996EboJoPdEUzVKbCy6WTVA0w5np1jRS30DZIBJ0qcNbagzP6s7hs1J0PmV0AKAESSq7UnSt2-B2K4BQNh4X20WHDGvTy8JwSTWr3Dd01Bc4hrWmezs0ettlMSH68VnmuZlVPgdSjXXHmXcXRaPH792qtSVgYnak-52nkXJZmdc-5f0JDU8byRhgvQhHRItntUY2BVlYwLUaBihpvM4no6kNEaaGdGZJvbJxHW35sLSKoBjnNLzODdBM83JDZ19tsLZoWIKZxC42wGEJK7L-SrYWOkzYekcDrZm_Czm2pLWKyrch15KyN83oeHgnkcJYXzhqlJU3uGT0qDW4tw6OXNtJtTdAwe9OFC7CHXeuyZdFYONnbUM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اعزام ۲۲ نفر ایرانی برای مسابقه جهانی مهارت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/farsna/462025" target="_blank">📅 18:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462023">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WtvOwkl9TQlOXzN0V-e-NmZ-wBchbL-5PVPJd3SKlhLpexrdSnfWv86pIrnT1xJo3leo5NUZlJ11toFuEeh-b7e3zZfgi3fixbxpd38QKlgprSBTvCT4KBOob97ejL65WRDaDLeh5g8D490dYgaZCV9bcFt9AvF04qsY9xrUS93XpJn-tZ5ObPMMG9GtAs_pG_tLl0hpjCi2V_7RcSCa-IXEjUv7NwOBGp935YmtL1EUmxKXD-2Fyjm8C_cqTWPZAPljQRsvSdTdec-4be0PrMJJozbPuXRjD-1evmpeBnAGET9DKcnEnAOrvhTKiupUbFepWJQEY89DzTQp8eerOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J3WrkIz_EoTyjoyjLch4vhkoIB_YNHCVCkLVtKIV75QplBJX8gpXH9G4ii2JGFEDGJuI9S0KXr3QOnLSSG3sBx0K-oWQGLgqAIpF6mrGbdma3nh3AWKOgMK3PvknHyd_eDs9ammv5bvl0UeEt1p0fXX47OqrMi753NGDkjD1HqMPSP0HRunQj322lZ8Flfc_g4fHP0O1K8kkz9yb77IubPg98pijAnTMGf8uPOJZamd0Szxq6DSrUuOu6hfrYW82urAgmmnKDBnw8lU9eJqPkV1LgWu0Btds33S5OTEZTQGE7INJgfdte1XhH2fD3Gffoe8-KjHWZlNYJVPim_jV2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حذف شیر و خورشید؛ وزیر خارجه عمان اشتباهش را اصلاح کرد
🔹
وزیر خارجه عمان بدر البوسعیدی امروز نسخۀ اصلاح‌شده پیام خود درباره لغو نشست اعراب با ایران را در شبکه اجتماعی ایکس منتشر کرد.
🔹
وزیر خارجه عمان نیز در این پیام به‌جای پرچم مزین به نام «الله» از پرچم شیر و خورشید استفاده کرده بود، اقدامی که واکنش منفی رسانه‌های کشور را درپی داشت.
🔹
حال، وزیر خارجه عمان با حذف کامل پیام پیشین، پیام جدیدی را منتشر کرده که در آن تمامی پرچم‌ها را حذف کرده است.
🔸
شبکۀ اجتماعی ایکس از سال گذشته در اقدامی ضدایرانی پرچم کشور را از ایموجی‌های خود حذف نموده و پرچم شیر و خورشید را جایگزین کرده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/farsna/462023" target="_blank">📅 18:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462020">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNh_6xfZRz_sJBsUfLzaytPNIkU32beZGJxEnOhAmsCgXnsGu3CW0nUFIC8pu-juy5XWGSfiWnCefA2hWmNNSlZh8F3btzxCMfLwmDRNcHW00dCDbPFnP5w_uJJ_NCpVAQyr7Jtj5WyaoREXJDD0OjFWMwslx98oIqVfyu39aJm1V-7KVOz1qxKRu7MWKn6b96PTJgx571lATUS4KBqrPm2FmdlQGJb0YR7qH_W4W-WLPCRrnMPCX9dN9waappIsCJYnL6BPGCmeeLiak-jb7AjioGAD_K_PitlR7K1VMcTDT6J3EWOdpAfvSCHYM0ww2_X4kSPe1BPBlW7Co3L0ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت امام جماعت اهل سنت مسجد محمد رسول‌الله زاهدان
🔹
مولوی یوسف گرگیچ امام جماعت اهل سنت مسجد محمد رسول‌الله شهرستان زاهدان توسط افراد مسلح ناشناس به شهادت رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/farsna/462020" target="_blank">📅 18:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462019">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۳۴.pdf</div>
  <div class="tg-doc-extra">2.8 MB</div>
</div>
<a href="https://t.me/farsna/462019" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۳۳.pdf</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/farsna/462019" target="_blank">📅 18:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462018">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRslVqIfjekO-P9Mzr8blCuEaTWcRA5euheWWocjG4-rtFFguHF4H04AmUfXjiQcZyI9sBdQVdeE6qWIlDTkLT1lFZZ_Nj8RQxReVbSkyooBinGrgsa2SQVnyQncFLcXXo1-dP98ZroLLj_EZAAeP5etWty13oObYbDJ1MoQs69P1feSyQYYOpwVCdY0p6EYBW1YuWdH2gSV49Ad_SFCyBl50exZhm5HXe-mD8A5ErTb-OVIsvgQrfoBIy8MLPhbdzjeAJZwIRfA5a-8bqKJwP339_RBivbiKwTVr1S5U94DsyFrO50dAiUoJEqhRwcrkVxORNvtfvs0fCXPfQz6Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
نقشۀ راه پیشرفتِ اقتصاد
🔹
مروری بر مطالبات اقتصادی مطرح شده از سوی رهبر معظّم انقلاب در پیام به ‌مناسبت هفتۀ دولت
@Farsna</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/farsna/462018" target="_blank">📅 17:45 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462017">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">پول‌هایی که دولت می‌گفت نیست، اینجاست
🔹
بودجهٔ دولت تا پایان تیرماه فقط ۲۱.۵ درصد کسری داشته در حالی که منابع حاصل از فروش نفت و گاز تحقق ۱۰۱ درصدی داشته است.
🔹
طبق اعلام دیوان محاسبات ۳۱ هزار میلیارد تومان منابع سازمان بهینه‌سازی و مدیریت راهبردی انرژی در حساب این سازمان رسوب کرده و بلا استفاده مانده است.
🔹
همچنین مدیرکل اسبق خزانه در این‌باره می‌گوید که بسیاری از منابع دولت پیش از ورود به خزانه به حساب شرکت‌ها واریز می‌شود و در این فرآیند، منابع بودجه‌ای عملاً به منابع فرابودجه‌ای تبدیل می‌شود.
🔹
این یعنی هم‌زمان با اعلام کسری بودجه، پول دولت از مسیر اصلی بودجه و خزانه خارج شده و در دسترس دولت نیز قرار نمی‌گیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/farsna/462017" target="_blank">📅 17:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462016">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">تلفات مزدوران سعودی در حملات یمن به صحرای الجوف
🔹
رسانه‌های یمنی به نقل از یک منبع نظامی یمن: محل تجمع مزدوران سعودی در صحرای الجوف در شمال یمن مورد هدف قرار گرفته است.
🔹
این منبع با اشاره به اینکه در حمله مذکور، تجهیزات نظامی سعودی‌ها منهدم شد، خبر داد در این عملیات چندین نفر از این مزدوران کشته و زخمی شدند.
@Farsna</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/farsna/462016" target="_blank">📅 17:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462015">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32ce8b023e.mp4?token=AgQYa9I8KZTxiNF8gvOvlDI_bmck78THVnMgk6mOvIbxenM2RV7dCcFq31gUfovENyqesc1Ww9LzqZL1LIvk9Wi2kd38dGWEQZsusXktS6pDUC5YVjFVyZ-WMwmLBmIxDcRy6MKAmmrWHmkB1cxVXQFrIN8SHk4OxhWwaWXIWOfsbTPLKlzwRPEtlnT2lzrZkCpIbsmatq0pI-mMhsXTFglBLXHK8gOQxkZhpV3XcpWRTJrc4fACpGa7iK9H8HoAq-w7l-WKVelv5r-tiDFNnHrGcUASfrSWKJJTyMOWft_bbsCbRpkr0ZsatySc4090FXFYfx6XFGBAzXxcbh8IOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32ce8b023e.mp4?token=AgQYa9I8KZTxiNF8gvOvlDI_bmck78THVnMgk6mOvIbxenM2RV7dCcFq31gUfovENyqesc1Ww9LzqZL1LIvk9Wi2kd38dGWEQZsusXktS6pDUC5YVjFVyZ-WMwmLBmIxDcRy6MKAmmrWHmkB1cxVXQFrIN8SHk4OxhWwaWXIWOfsbTPLKlzwRPEtlnT2lzrZkCpIbsmatq0pI-mMhsXTFglBLXHK8gOQxkZhpV3XcpWRTJrc4fACpGa7iK9H8HoAq-w7l-WKVelv5r-tiDFNnHrGcUASfrSWKJJTyMOWft_bbsCbRpkr0ZsatySc4090FXFYfx6XFGBAzXxcbh8IOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر مطهر یکی‌از شهدای دوران دفاع مقدس در طلاییه کشف شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/farsna/462015" target="_blank">📅 17:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462014">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUELn5z5Vy2qGPc6KwRFfvznJiyJQoWrFLs7lG5F9pk4ZtLocH1TA2-CiOcwrZDr6iMMomJP2pNQP3o2cElctONP3P4HFTe8ULhScoZlWpat1iyGpRkNjzLWmywRWoMyhJTED9Jb_q_TAvVHC7w9pBL31m0sDOYoLRskiyxhYUn2rfRKY2CQTU6Hv1N8OBcGkXODA8a6WiI8n8waKRTGmR9S42mNetbX8l7sReE6NgexKUKPHE60nW-sCZr41teeshgLGBXzv53uT9Wco19Pm5g16AXEJLTRCQ8g2b8CUj5YjevNSKy8Namc_jw26EdKyUjUWo9eitF7lF27Jwzl1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدعیان آزادی اینترنت، ایرا‌نی‌ها را محدود می‌کنند
🔹
اکبری، معاون وزیر ارتباطات: حدود ۳۰ درصد از چندصدهزار دامنه و پلتفرم بین‌المللی که در سامانهٔ پایش این شرکت رصد می‌شوند، برای کاربران ایرانی تحریم است.
🔹
همهٔ پلتفرم‌های پرکاربرد هوش مصنوعی نیز برای کاربران ایرانی بسته هستند و تمامی APIهای گوگل روی آی‌پی‌های ایران باز نمی‌شود.
🔹
حتی برخی بازی‌ها و سرویس‌های مورد استفادهٔ کودکان نیز برای ایرانی‌ها تحریم است؛ آن هم در شرایطی که کاربر ایرانی حاضر باشد هزینهٔ استفاده از این خدمات را پرداخت کند.
🔹
این محدودیت‌های بزرگ توسط کشورهایی انجام می‌شود که در عین حال شعار آزادی دسترسی به خدمات دیجیتال و حمایت از مردم ایران را ‌می‌دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/farsna/462014" target="_blank">📅 17:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462013">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f967a1195a.mp4?token=Mz5MSQkhPeH_eyNwiSnwHOI-LmbucwdM2QhNaCzZ2TS4b84nYNJvvF2ias8wwC8qh7lqE1VIMbv95HdIPrFsh2dik_Tpo0plzkoQltbmIWRbZN_ySivwxQ_rxpDXptxALClTROQU6_idhueCTFLIYbMVWCi9VWQ10ZN6GjDAJdkq_J2xHIpHEhR7goj9FoCfmrqJfk5NSaAFy6QDuPaDgzIUvLcLLjNxnYGHzgNJV7vOrG2fHsoIhIMDK3e5vfWteWpMW1fQcJ2W2_4nD24IdCh5po0SuIbAHpjSM77_1sHBMHGnzk0c0iQoYMpqr5G-BhCruXEV49yhR1Du25rEbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f967a1195a.mp4?token=Mz5MSQkhPeH_eyNwiSnwHOI-LmbucwdM2QhNaCzZ2TS4b84nYNJvvF2ias8wwC8qh7lqE1VIMbv95HdIPrFsh2dik_Tpo0plzkoQltbmIWRbZN_ySivwxQ_rxpDXptxALClTROQU6_idhueCTFLIYbMVWCi9VWQ10ZN6GjDAJdkq_J2xHIpHEhR7goj9FoCfmrqJfk5NSaAFy6QDuPaDgzIUvLcLLjNxnYGHzgNJV7vOrG2fHsoIhIMDK3e5vfWteWpMW1fQcJ2W2_4nD24IdCh5po0SuIbAHpjSM77_1sHBMHGnzk0c0iQoYMpqr5G-BhCruXEV49yhR1Du25rEbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرریز شدن سد خمینی‌شهر بشاگرد پس از بارش‌های تابستانه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/farsna/462013" target="_blank">📅 17:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462012">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3fIpyiIhDooNEGAzYp66Yz2jqhbNpxj3OCmLDwrqXg6U1O92k7sq4ftK341ir25XWhXjfx6u69czi-SY72D2gzjgJ8Kj5GmbdQ20Yr9IRUBI3dqlmkY-LpTB6FSZukYb9kIfVRpw7sL_Tn2hxaIBF10QONXO6uB820UWoEvdBvbWDteRnzbVWP_zt9ztioCfa9b6al185Vd-G6__ussz1o8rhmGBSBIeOlw5Z9OawodincOPJGpG-dGGfDeNJwbaf0wTsyYqCp-_BcVHl3BbbrZZsNLV8vOKRWHNR9Od_mTGh_M3nn1lGBYceC4sNzBpE38wqur9tr17TbhyMuPNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت گاز اروپا به قلهٔ ۳ ‌ساله رسید
🔹
قیمت گاز اروپا امروز با جهشی ۵ درصدی به ۸۴ یورو در هر مگاوات‌ساعت رسید که بالاترین سطح از ابتدای سال ۲۰۲۳ تاکنون محسوب می‌شود.
🔹
قراردادهای ماه اکتبر در هاب TTF هلند که شاخص اصلی بازار گاز اروپاست، از مرز ۸۴ یورو عبور کردند و به بالاترین سطح خود در بیش از ۳ سال گذشته رسیدند.
🔹
قبل از شروع جنگ آمریکا و اسرائیل علیه ایران در اواخر فوریه ۲۰۲۶، قیمت گاز در اروپا حدود ۳۰ تا ۳۳ یورو در هر مگاوات‌ساعت بود.
🔸
با آغاز درگیری‌ها و بسته شدن تنگهٔ هرمز در اوایل مارس، قیمت‌ها به سرعت جهش کرد و در ۹ مارس ۲۰۲۶ به ۶۹.۵ یورو رسید که در آن زمان بالاترین سطح از ژانویه ۲۰۲۳ بود.
🔹
با این حساب، قیمت گاز اروپا از حدود ۳۰ یورو پیش از جنگ به ۸۴ یورو در سپتامبر رسیده است؛ یعنی حدود ۲.۸ برابر افزایش یافته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/farsna/462012" target="_blank">📅 17:18 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462011">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">تکیۀ ۱۵۰۰ مدیر متخلف بر مناصب شرکت‌های دولتی
🔹
رئیس قوه‌قضاییه امروز گفت: «۱۵۳۵ نفر به‌صورت غیرقانونی در هیئت‌مدیره شرکت‌های دولتی عضو بودند که برخی از آنها با تذکر استعفا دادند.»؛ این درحالی‌است که طبق قانون افراد شاغل در دولت و بازنشسته‌ها نمی‌توانند در این مناصب قرار بگیرند.
🔹
چندی پیش نیز رئیس سازمان بازرسی گفته بود که برخی از اعضای هیئت‌مدیره شرکت‌های دولتی در ۱۰ شرکت عضو بوده‌ و بعضی از آنها بازنشسته بوده‌اند.
🔸
هیئت‌مدیره‌ها مسئول اداره و عملکرد این شرکت‌ها هستند و نوع عملکرد آن‌ها مستقیم بر روی بودجۀ کشور اثر می‌گذارد؛ طبق اعلام دیوان محاسبات، تنها حدود نیمی از ۳۴۲ شرکت دولتی سودده هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/farsna/462011" target="_blank">📅 17:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462010">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9WqWRpFQGcgSjKR11GiQoln5E48N9I92BYCFedk7qUpcM1hB1Vv9byIc4jg_En3Fpjzq1MvlrVsoiAXYO10Nv3eINWJMexLgJD-DC1-WjsXULXtP39CxCjYBqBKcf55wjC3mFHnah1QZn6fZziUGjAVJHYkUUt3m96cLzXXGA3ZtVqACa4SOt6_DWpDCaCGBW6yHIJTAzj2qyYlbwABbYnMQ-29AJxxFPKlZkXxpwhPbNgZp62qKXVHum7R7qDJET9GwyZmwJ8XEHL64QOLfatmVjoIuXPgpn61RpzC9MV5-g9vCmBotfPN68_aG7dWmSuXT_jc53jvo_uDG139xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مستند خلبان آمریکایی؛ پروژه جعلی پنتاگون برای دستاوردسازی از جنگ نامحبوب
🔹
به دنبال پخش مصاحبه شبکه سی‌بی‌اس با یکی از دو خلبان آمریکایی که جنگنده آنها در آسمان ایران ساقط شد، بسیاری از رسانه‌های آمریکایی آن را قهرمان‌سازی و روایت‌سازی جعلی پنتاگون برای دستاوردسازی…</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farsna/462010" target="_blank">📅 16:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462009">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: اقدام اتریش در صادرنکردن روادید برای رئیس سازمان انرژی اتمی ایران ناموجه است
🔹
اتریش به‌عنوان میزبان سازمان بین‌المللی انرژی اتمی وظیفه داشته روادید هیئت ایرانی را صادر کند. @Farsna</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/farsna/462009" target="_blank">📅 16:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462007">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2fc5d82c0.mp4?token=fuiWCRd_80Kwt9vRLO5o2LuWjRgPFae1MSkaZ1KRbvh5KZE9rjCS9oY3KgLQUAxSUsaH4oT3ZudA4JBXeE8G5F71USUs0wPA0MPWRi-GrXEUZ8Ifqi0UW90SpPhKlB8o4dg57gl7_kcC1JqKF9Y3PlLNTfcDyZWHlp5sRzkbMYjuk_Yg1nYfP0ag04FjPGvqCExVqphLNtYW1SEpIM_xR10mpTl36nFH7he7eoUSJXoWACZrSCiCnWCYLiRh78GV9L34eK7G6IeI-ypvwtgWPPW3GdOzzLv1zypkEEDHLGa2iElOOXClxN_OllxWV2aEqphUqF5QdN4Q5QGKZdCViA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2fc5d82c0.mp4?token=fuiWCRd_80Kwt9vRLO5o2LuWjRgPFae1MSkaZ1KRbvh5KZE9rjCS9oY3KgLQUAxSUsaH4oT3ZudA4JBXeE8G5F71USUs0wPA0MPWRi-GrXEUZ8Ifqi0UW90SpPhKlB8o4dg57gl7_kcC1JqKF9Y3PlLNTfcDyZWHlp5sRzkbMYjuk_Yg1nYfP0ag04FjPGvqCExVqphLNtYW1SEpIM_xR10mpTl36nFH7he7eoUSJXoWACZrSCiCnWCYLiRh78GV9L34eK7G6IeI-ypvwtgWPPW3GdOzzLv1zypkEEDHLGa2iElOOXClxN_OllxWV2aEqphUqF5QdN4Q5QGKZdCViA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون حقوقی فدراسیون فوتبال: از یاشار سلطانی شکایت کردیم
@Sportfars</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/farsna/462007" target="_blank">📅 16:26 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462006">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOg-n4XOoChbsb94cazgmL3yMQzVc3qVDU7cJDLE6jDUxMtIr7iNmaITghvJcm8iVGGyRHD9g-f_NPfTLPXqe3r0XBff_g4a26w2Gz1CDMHRUJYIqzfZiRhkRoQDzf3TTxx92pwAyNIDY4Pe2liZNkTv_R14Swud6rLB9uHWkz_3qLHgVjNyhnA_UXV-FFykun9Alz0FDVYe-HS2h4Pf6uGH37ubMlpVFHTA8g4VY0BTYuXfGL-k0o2vLz7oBIDl9kxxsYn1vuGpERLEo_RLTSW6qfsEXRQak_haTFFqsVzfjY91hIgjeSkKkoQaGA4M-WDk_i-eA1ja9HbSoF9xkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا باز دربارۀ هرمز خالی بست
🔹
وزیر انرژی آمریکا دربارۀ وضعیت تنگۀ هرمز مدعی شد عبور نفتکش‌ها از این تنگه شبانه و با همراهی نیروی دریایی آمریکا انجام می‌شود.
🔹
رایت همچنین با رد آمار نهادهای رهگیری دریایی مدعی شده داده‌های ما درباره عبور کشتی‌ها از تنگه هرمز تخمین نیست، بلکه واقعیت‌های دقیق است.
🔹
این اظهارات در حالی مطرح می‌شود که بر اساس داده‌های رهگیری کشتی‌ها تردد شناورها از تنگۀ هرمز در روزهای پایانی هفتۀ گذشته تک‌رقمی بوده و همچنان بسیار پایین‌تر از میانگین ۱۴ فروندی ۱۰ روز گذشته است.
🔸
برای مثال شنبۀ گذشته تنها یک نفتکش چینی با سامانۀ ردیابی روشن موفق به عبور از تنگۀ هرمز شد؛ درحالی که پیش از جنگ آمریکا و اسرائیل علیه ایران روزانه بیش از ۱۰۰ کشتی از این تنگه عبور می‌کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/farsna/462006" target="_blank">📅 15:58 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462005">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRq9qUcW5KZRgISRL48aiRYY7m5_YmgcAb0qI8_PqWMJ4W4TBKe7BJbsjk_ZIksZA7jE-wOg__gkZ-NmDGPRkYHFby2GdEugN5n55upThzXDe1_ZGQHSp1cE1S18C3NQfHG8GQ1AsWj0gGt6gHoZyd2NRsgZRt5yr3XVHclpK32o_FMIDA7voi5La1A_hoUYKNvnmqdHdzx2QzteWXeKlLBs-OPrfbx4Z-Vjpy1NkYcbst8J8-du1jKdbbUGn4FC2gjcJl7Zb5YrGymGdvUF0miplGraDrBS-ZNe5zGhiWyzjiWzddTVQbZg29Mqudr8OcgjVABMTT52dC96XsLVjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مستند خلبان آمریکایی؛ پروژه جعلی پنتاگون برای دستاوردسازی از جنگ نامحبوب
🔹
به دنبال پخش مصاحبه شبکه سی‌بی‌اس با یکی از دو خلبان آمریکایی که جنگنده آنها در آسمان ایران ساقط شد، بسیاری از رسانه‌های آمریکایی آن را قهرمان‌سازی و روایت‌سازی جعلی پنتاگون برای دستاوردسازی از جنگ نامحبوب علیه ایران خوانده‌اند.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/farsna/462005" target="_blank">📅 15:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462004">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ثبت‌نام آزمون وکالت ۱۴۰۵ آغاز شد
🔹
سازمان سنجش: متقاضیان آزمون پذیرش پروانه کارآموزی وکالت کانون‌های وکلای دادگستری سال ۱۴۰۵ می‌توانند با مراجعه به
درگاه اطلاع‌رسانی سازمان سنجش
نسبت به مطالعه آگهی آزمون و ثبت‌نام در آن اقدام کنند.
🔹
ثبت‌نام این آزمون از امروز، دوشنبه ۲۳ شهریور، آغاز شده و تا روز دوشنبه ۷ مهر ادامه خواهد داشت؛ آزمون پذیرش کارآموزی وکالت سال ۱۴۰۵ روز پنجشنبه ۱۴ آبان سال جاری برگزار خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/farsna/462004" target="_blank">📅 15:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462003">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6mFzPBfXO4elX6ivEsy-fKFOOowUGTUn6iJhqffCVIZqeXZSRS35kUD_Gwu0OJIUaLLjx8zEHg8Zv_QH-bXiT-ZEWVAteqkDkOGjIhqsSDonEGxvJ_qaWPRJMZOanFGfgyoRoJPNo8kEzifW-ZrDpPAWztQQhrRKCtrAKoOASDZrGP5YQwaqHJsy4f48JQlDwKD0DwlTlmbQkNm2sIk5-xyMga8Y1FxllD44r8O83AZi3Mg1bswleH7_9GN2vrQX5v_nE2TxwyrvQL4df8AFZIdkq4P4CMIqG1gA5yYRQ-Yf2iictgCGNocWHzSKeRqCviGLSOEM9flOeImZHigGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین واکنش‌ها پیرامون صحبت‌های لاله مرزبان را در فارس بخوانید
تازه‌ترین مطالب و یادداشت‌های:
🔸
جواد قارایی
🔸
احسان رستگار
🔸
سید علیرضا آل‌داود
🔸
داریوش سجادی
🔸
مهدیه شادمانی
🔸
علیرضا پورجعفری
را می‌توانید در صفحه اختصاصی هر یک از این افراد در فارس تعاملی مطالعه کنید.
@Farsna</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/farsna/462003" target="_blank">📅 15:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462002">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfd25c9786.mp4?token=Mo5btmJyFXWYYXmfJtVttn0iVCDYQvI6kUjvTrn53BP7-bkz4e7Hv8jxfpqFGggAObBttPfRU3V2zKTDr0UBiZ2IWZLfUVQbjCmTlpQE32mNu5JqHLChJB0x48iHRBj9S2i6CO5pIpSzgjeDu98b8K3vYmXwgdZ-34SLWlJY-zYsvpaIKRDxdlm1rSGgP3TgX-7nYHcCCn3T5Xlo0oRmF2HVLDLoFzT8Tv4UiLM0P_C98dgaSRU-tiaq6kUjRmg-xkn7YJFNfu9jnCyz_0rV1ZNp8vPl-0uaKSeyAMCaUaVjIwpqu0uJ2rvrz5dM5SpqtBrzFgC9EVBOzWtL8FgyUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfd25c9786.mp4?token=Mo5btmJyFXWYYXmfJtVttn0iVCDYQvI6kUjvTrn53BP7-bkz4e7Hv8jxfpqFGggAObBttPfRU3V2zKTDr0UBiZ2IWZLfUVQbjCmTlpQE32mNu5JqHLChJB0x48iHRBj9S2i6CO5pIpSzgjeDu98b8K3vYmXwgdZ-34SLWlJY-zYsvpaIKRDxdlm1rSGgP3TgX-7nYHcCCn3T5Xlo0oRmF2HVLDLoFzT8Tv4UiLM0P_C98dgaSRU-tiaq6kUjRmg-xkn7YJFNfu9jnCyz_0rV1ZNp8vPl-0uaKSeyAMCaUaVjIwpqu0uJ2rvrz5dM5SpqtBrzFgC9EVBOzWtL8FgyUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سریال کوری سلبریتی‌های ایرانی روی فرش قرمز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/farsna/462002" target="_blank">📅 15:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462001">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">تمدید مهلت ثبت‌نام سرویس مدارس تا پایان شهریور
🔹
اتحادیه حمل‌ونقل مسافر شهری: امکان ثبت درخواست سرویس مدرسه در
سامانۀ سپند
برای جاماندگان تا ۳۱ شهریور تمدید شد.
@Farsna</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/462001" target="_blank">📅 15:23 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462000">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d29dfe3f76.mp4?token=VDnrL47N_EKpespZcANbo_F8uUPXGwNUCn8jUGMrILhRFAqYwIIzp-Sgm8JZkdO7pEHeiLsbVYduQhodyY2u2acNSdXUQ1Gm_oiTNGz2VvMOHtaGjnhxPyWR_2n4MySlIsgkoIfxkBZ8wHv0XsSc1aT6wtGppWS4sQRHeU5bDTwNv2cwWJtKmjLr3FKUhrjXeTbCRME6iwCELXqSuBMz6t1ySapwMd58dmI4J0x9KyaCYdoZrQ1K66m6H-_3vbxpgOshV9TQfclEFMLoGnoBh8m8ktp0zxgU5Ld62cYMq5uePg0PMeiX7HA_o_uogQQ8VPDJIVDPs26K7Akpf196Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d29dfe3f76.mp4?token=VDnrL47N_EKpespZcANbo_F8uUPXGwNUCn8jUGMrILhRFAqYwIIzp-Sgm8JZkdO7pEHeiLsbVYduQhodyY2u2acNSdXUQ1Gm_oiTNGz2VvMOHtaGjnhxPyWR_2n4MySlIsgkoIfxkBZ8wHv0XsSc1aT6wtGppWS4sQRHeU5bDTwNv2cwWJtKmjLr3FKUhrjXeTbCRME6iwCELXqSuBMz6t1ySapwMd58dmI4J0x9KyaCYdoZrQ1K66m6H-_3vbxpgOshV9TQfclEFMLoGnoBh8m8ktp0zxgU5Ld62cYMq5uePg0PMeiX7HA_o_uogQQ8VPDJIVDPs26K7Akpf196Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی صنعت آب: پرشدگی سدهای کشور کمتر از ۵۰ درصد است
🔹
منابع آبی پشت سدها نسبت به سال گذشته بیش‌از ۶ میلیارد مترمکعب بیشتر است؛ اما درصد پرشدگی سدها کمتر از ۵۰ درصد است و این میزان در تهران به نصف می‌رسد.
@Farsna</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/462000" target="_blank">📅 15:20 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461999">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79376310ee.mp4?token=ELI5G6lnJOtPjTr71r9MIyZPZKfGvKERN21iBJeh0068Cj39imz8zrVU_R_zDJdNmv_9weIhnjXlSTZ0g5MSoCFjoqJpbcv2Jr7yjYs0cvQRTNiBgv2GsU5Rcngj-L86rifzQnNQSzG0pP9UqPK9BSQ3-4uX0eQo7O80pgpY6KiJ693zrpgYVN0nNXayQNaOSBBYwLOlODmNEz732e7vTK9dXdxJW1I2XjkbsBlFtWqcBRpmeXx7kCrdjLRE3Uj6Ef5gzEW1I6toki3s-pmA-LMBnUE6aDfej4SG6p5oKypb-Xtf0AwJyabCctlnFKjVZCjPFKuujRZwVMRgw-bJkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79376310ee.mp4?token=ELI5G6lnJOtPjTr71r9MIyZPZKfGvKERN21iBJeh0068Cj39imz8zrVU_R_zDJdNmv_9weIhnjXlSTZ0g5MSoCFjoqJpbcv2Jr7yjYs0cvQRTNiBgv2GsU5Rcngj-L86rifzQnNQSzG0pP9UqPK9BSQ3-4uX0eQo7O80pgpY6KiJ693zrpgYVN0nNXayQNaOSBBYwLOlODmNEz732e7vTK9dXdxJW1I2XjkbsBlFtWqcBRpmeXx7kCrdjLRE3Uj6Ef5gzEW1I6toki3s-pmA-LMBnUE6aDfej4SG6p5oKypb-Xtf0AwJyabCctlnFKjVZCjPFKuujRZwVMRgw-bJkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کابوس نفتی جهان با بحران در ۲ شاهراه انرژی به اوج رسید
@Farsna</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/461999" target="_blank">📅 15:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461998">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe4903cea3.mp4?token=Alx4Bxay-SMJ7OeuPRkxjqUEutWGh2MU2diZ7aiaMI8UyBdzA4kiePYf6ZQ47sczAXplgXHza4pee74SdBD0eJXU-BYsKMje0qqejBePDu3MFSothUBlnyLqGq8rVka2GuFxlq1_-z7Tf9f-bghyHJrsEL0EWOdA23e946l46UQfd4ku4ghNV3W2dhTGGOgcpNCn5nnTZcPeO3b4-sxZ0gn7cFD1XqSoa2i_GzIvhf7QRPDLa2gzJvaoMTIOcL-MZonmLxJApolfQlHIlcycmgGciAkkTxQPRZhozFX_X4wBr0pRZHPxilJe7az83KekjLbhr9nLRP4K4Rdu0zvVyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe4903cea3.mp4?token=Alx4Bxay-SMJ7OeuPRkxjqUEutWGh2MU2diZ7aiaMI8UyBdzA4kiePYf6ZQ47sczAXplgXHza4pee74SdBD0eJXU-BYsKMje0qqejBePDu3MFSothUBlnyLqGq8rVka2GuFxlq1_-z7Tf9f-bghyHJrsEL0EWOdA23e946l46UQfd4ku4ghNV3W2dhTGGOgcpNCn5nnTZcPeO3b4-sxZ0gn7cFD1XqSoa2i_GzIvhf7QRPDLa2gzJvaoMTIOcL-MZonmLxJApolfQlHIlcycmgGciAkkTxQPRZhozFX_X4wBr0pRZHPxilJe7az83KekjLbhr9nLRP4K4Rdu0zvVyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: از پنجشنبه سامانهٔ بارشی جدید وارد کشور خواهد شد
@Farsna</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farsna/461998" target="_blank">📅 15:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461997">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af78b96837.mp4?token=TPdJQxjfodmSGWP6g0plb09wHenc9AMZlhDxNNjEftmV5mJFuYYJ6i3ItEjQ5TYUi4oQVjnAEc7fgfTD0ChqjiHKP0X62V5ieIOTUrvhJEwsuAaNcAUQBZyME0aW625nWCYCrHfBBUaEK5lRLwF1nDvNbipeB53OtDTWYoRTjEkxiUR6s0M-cUctRm9C2NCGkFyFX4kl2KKQd8T98XaaMqUa3vQATFY7aF0uFhzK0rlidNnaq65t4RGrahrcn3xZ3OLvky-8FGE4V1NV_ugc4WU1RM6QrQ5m5loYTaiMpxSb3BJvpIpuYvyapl4STh5mC0fXdB8i-AAo_3aKiShzVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af78b96837.mp4?token=TPdJQxjfodmSGWP6g0plb09wHenc9AMZlhDxNNjEftmV5mJFuYYJ6i3ItEjQ5TYUi4oQVjnAEc7fgfTD0ChqjiHKP0X62V5ieIOTUrvhJEwsuAaNcAUQBZyME0aW625nWCYCrHfBBUaEK5lRLwF1nDvNbipeB53OtDTWYoRTjEkxiUR6s0M-cUctRm9C2NCGkFyFX4kl2KKQd8T98XaaMqUa3vQATFY7aF0uFhzK0rlidNnaq65t4RGrahrcn3xZ3OLvky-8FGE4V1NV_ugc4WU1RM6QrQ5m5loYTaiMpxSb3BJvpIpuYvyapl4STh5mC0fXdB8i-AAo_3aKiShzVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تنگه‌های راهبردی در دستان مقاومت است
@Farsna</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/461997" target="_blank">📅 14:54 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461996">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faea411181.mp4?token=s63BFmfp2DvRCZomPnrO42KNSAdo3_EaZZPdaHai84AFsKYsi_UwP-RKASko9b8I7O7exozeR8ymb6XFLokSWjkeVm6y_iIR1yS1oEPw8QGRNyZ0DAIKOFnLAzWI2_GNkpOyjxCJQRPU5lgUsfJworOc32XUsMvH5n1DtF34zHA9HaNa3xqdeEPoFAjYKXqc8if3aWBMsYBoT50SLzA-i2FG1HzQfkPls2d883EKca1Je8WYKT4dmdPwMqyZMMLKU2wJwyhtvdxYeumJr_56OkBKxDtrzUbNGedK2Sc27wCgvRt9V1CzmloqSIVuWzM9okMV9ND77evQ_cDtKQMbSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faea411181.mp4?token=s63BFmfp2DvRCZomPnrO42KNSAdo3_EaZZPdaHai84AFsKYsi_UwP-RKASko9b8I7O7exozeR8ymb6XFLokSWjkeVm6y_iIR1yS1oEPw8QGRNyZ0DAIKOFnLAzWI2_GNkpOyjxCJQRPU5lgUsfJworOc32XUsMvH5n1DtF34zHA9HaNa3xqdeEPoFAjYKXqc8if3aWBMsYBoT50SLzA-i2FG1HzQfkPls2d883EKca1Je8WYKT4dmdPwMqyZMMLKU2wJwyhtvdxYeumJr_56OkBKxDtrzUbNGedK2Sc27wCgvRt9V1CzmloqSIVuWzM9okMV9ND77evQ_cDtKQMbSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استاندار خوزستان: در شلمچه و چذابه از جهت تردد مسافر مشکل خاصی نداریم
🔹
تردد کامیونی از امروز صبح در بخش شلمچه آغاز شد. مشکل تردد در چذابه هم به‌زودی برطرف می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/461996" target="_blank">📅 14:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461994">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/450093983c.mp4?token=rWzwseL9-_2aITB9C8fDJMeVXCbP0deccXvuPSt2LA9tYrK0f8t_hAdgZdT06vignVNhULwzvDG2HZQOob02FfrQTGocRFoe1V7ftPpXr0coYvNoJ0wKnMbaDGgrwjEca-YC9nhfNI1vyhdNrtNXz_4QkYdDD5BMcBPCGmH3kULdNOeK910ajK3iSkjE0z5lKanknkcHGpcj6jP5BW7Z14LmIfCFRPU2MGBRMyPD3IJ8HN9xnvIwWQcAHoKXi-2ExISglXP9X9cXyF5sNM8MNoxNU2hUbq47cPC2_dIPqgyBRMb-3VX60ttsFsQrASPpsgGur93O683keB-Nr51PxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/450093983c.mp4?token=rWzwseL9-_2aITB9C8fDJMeVXCbP0deccXvuPSt2LA9tYrK0f8t_hAdgZdT06vignVNhULwzvDG2HZQOob02FfrQTGocRFoe1V7ftPpXr0coYvNoJ0wKnMbaDGgrwjEca-YC9nhfNI1vyhdNrtNXz_4QkYdDD5BMcBPCGmH3kULdNOeK910ajK3iSkjE0z5lKanknkcHGpcj6jP5BW7Z14LmIfCFRPU2MGBRMyPD3IJ8HN9xnvIwWQcAHoKXi-2ExISglXP9X9cXyF5sNM8MNoxNU2hUbq47cPC2_dIPqgyBRMb-3VX60ttsFsQrASPpsgGur93O683keB-Nr51PxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طاهرخانی: به دهک‌های کم‌درآمد تسهیلات قرض‌الحسنهٔ مسکن داده می‌شود
🔹
معاون مسکن وزارت شهرسازی: این تسهیلات در زمان تحویل مسکن با بازپرداخت اقساط ۱۰ تا ۱۵ ساله اخذ می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/461994" target="_blank">📅 14:43 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461993">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWk40S9TAZ9AN00lREzoeat0sO9Yje9hQsKWvJqboQ6cz7E51BRpJtwI7_wVmEK9DIgshvPkk7ZI6lJBYfp1_O_B0zpFaLEVd6MwmPpZf3LBZroU7tOGIYRBjwYv1k4GHhprWlARjoHeyK505CdRqy8AygAfVkUUAcklfSHi5nTH-8Km9wuoi9gS2sg5--CH9pMiLbhzdkpSTlGsV09XgtyR2y_4LlLwFb1-ylTxW4iiWPnyQ0EkvmvAWwoI_8gWDHm791FrnzrzDM9OYfR0MjQwnHhmvukeeI9PBHGDKsmoAqrMwm--xetF3FjAjz5JJMWHOoCh4oORkEWM4IoNVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔞
خارج‌کردن تومور ۲۰ کیلویی از شکم بیمار در بیمارستان ارتش
🔹
تیم جراحی بیمارستان امام‌رضا(ع) ارتش در یک عمل جراحی پیچیده، موفق به خارج‌کردن یک تومور ۲۰ کیلوگرمی از شکم یک بیمار شد.
🔹
سرپرست تیم دراین‌باره گفت: این تومور از نوع «سارکوم بسیار بزرگ شکمی» با منشأ احتمالی پانکراس بود که به‌دلیل ابعاد غیرمعمول و چسبندگی شدید، بخش‌های حساسی از دستگاه گوارش شامل اثنی‌عشر، رودهٔ کوچک و رودهٔ بزرگ را درگیر کرده بود.
🔹
در حال حاضر وضعیت بیمار مساعد گزارش شده و در حال گذران دوران نقاهت پس‌از عمل در بخش مراقبت‌های ویژه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/461993" target="_blank">📅 14:36 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461992">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca39e5c7a5.mp4?token=JSNzbfmS1-Xom47cs_GYmI6SPZ0O4dDndKCo2uJikUeuIHj__zTweeCpSilViI2_idrszrTWTl372XIxinxnqoTNLwjOQWEvZQgH4lbcj29xg679dKpLpSTY8E_j4AFC3MASMNYWUP5wYj01TxYoXDoTe1cyEk9H21FYvB8SyrszzEM0i3-JqHh5rtC-uJ8GvD-YrrT50mDxDSdtmrupGxn7oMc_7_Saaauav6o0EeMVsdtehx_bTNNPqSYThUzh59tbJJiQZI5ECWeihheEmIKczuzCaCKJHyQk62adHZkkZZRLvA7S-VsSjZMLQ9UjOEpMs0Be3GrxXep9JH2aLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca39e5c7a5.mp4?token=JSNzbfmS1-Xom47cs_GYmI6SPZ0O4dDndKCo2uJikUeuIHj__zTweeCpSilViI2_idrszrTWTl372XIxinxnqoTNLwjOQWEvZQgH4lbcj29xg679dKpLpSTY8E_j4AFC3MASMNYWUP5wYj01TxYoXDoTe1cyEk9H21FYvB8SyrszzEM0i3-JqHh5rtC-uJ8GvD-YrrT50mDxDSdtmrupGxn7oMc_7_Saaauav6o0EeMVsdtehx_bTNNPqSYThUzh59tbJJiQZI5ECWeihheEmIKczuzCaCKJHyQk62adHZkkZZRLvA7S-VsSjZMLQ9UjOEpMs0Be3GrxXep9JH2aLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس بانک مرکزی برای شرکت در اجلاس روسای بانک‌های مرکزی کشورهای اسلامی، راهی استانبول ترکیه شد.  @Farsna</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/farsna/461992" target="_blank">📅 14:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461991">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6282f32f2c.mp4?token=OJTYt46Hpx4FDIlq9WcYLvzqRnT7V4npHQMRev3fC_EI6UhTvYFJ2BWxkWdr4jJXsOf0aWeSr8Dmrzdbe6AtJw86JDuWJzsGB-BgQoShFB-2pm1QwuMnCOmw3N95i9YsvN4r2W6e13Kro6W0-fbE5Xci0OjjtLZG_CWH9cnIyxwGZh42G_icIMk58YWc4wU9ijBpXkG8m3S4AHJM7De7734nowsUt1n1-DuunFbO2fS_3TNkGO5C1Ndwhc3Gi1wrtSkaBHrVdnQfWv87mb-7Bn1nn-UwxQRiEM0kwqKAgOaqKEXxh6Rm3MFobV2133L--YLXP05xcB9p_iwbZY5c4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6282f32f2c.mp4?token=OJTYt46Hpx4FDIlq9WcYLvzqRnT7V4npHQMRev3fC_EI6UhTvYFJ2BWxkWdr4jJXsOf0aWeSr8Dmrzdbe6AtJw86JDuWJzsGB-BgQoShFB-2pm1QwuMnCOmw3N95i9YsvN4r2W6e13Kro6W0-fbE5Xci0OjjtLZG_CWH9cnIyxwGZh42G_icIMk58YWc4wU9ijBpXkG8m3S4AHJM7De7734nowsUt1n1-DuunFbO2fS_3TNkGO5C1Ndwhc3Gi1wrtSkaBHrVdnQfWv87mb-7Bn1nn-UwxQRiEM0kwqKAgOaqKEXxh6Rm3MFobV2133L--YLXP05xcB9p_iwbZY5c4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: رقم کالابرگ قطعاً افزایش خواهد یافت
🔹
حتماً در حوزهٔ بهداشت و درمان بازنشستگان و معیشت، تصمیمات سازنده‌ای گرفته خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/461991" target="_blank">📅 14:18 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461990">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f9b1b7b11.mp4?token=IVTDUv8Y8vFuF5TwLZ8NAw3wJyGxBuJuAYfpNvhtMJ409hU_RKe2aRtIzxc3_eNT8iPEtarIpN5_BlAmEUxXOYQogM5hbkcbYnNyOkTSxLhH3jDGdDdDwVnCepVSuEFSl_iFIzLZ7HLO5vLsFSGElO_CuXsqKVtRZS9J91CM3QTC5oHQ8_34T4nJC9_sWEeBTT57MRT1iTQfDhSmO827cUPcJaxCkKpWauJYOPf-e-LjOWnb5ERWin2ryJvjuU4cwub2AkR3Y2kztvC96sFBOg8np1w9pyHhqqi7xEe8eoqPbep-Kr6o9GB8cERYXqZiBCYpHXiDE4RxNFuXLMxgpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f9b1b7b11.mp4?token=IVTDUv8Y8vFuF5TwLZ8NAw3wJyGxBuJuAYfpNvhtMJ409hU_RKe2aRtIzxc3_eNT8iPEtarIpN5_BlAmEUxXOYQogM5hbkcbYnNyOkTSxLhH3jDGdDdDwVnCepVSuEFSl_iFIzLZ7HLO5vLsFSGElO_CuXsqKVtRZS9J91CM3QTC5oHQ8_34T4nJC9_sWEeBTT57MRT1iTQfDhSmO827cUPcJaxCkKpWauJYOPf-e-LjOWnb5ERWin2ryJvjuU4cwub2AkR3Y2kztvC96sFBOg8np1w9pyHhqqi7xEe8eoqPbep-Kr6o9GB8cERYXqZiBCYpHXiDE4RxNFuXLMxgpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر رفاه: بازنشستگان می‌توانند با ثبت‌نام در سامانهٔ «زرین تامین» اقدام به خرید طلا با قیمت ثابت کنند.
@Farsna</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/461990" target="_blank">📅 14:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461989">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
وزارت دفاع امارات از کشته‌شدن ۲ نظامی خود در یک «مأموریت آموزشی» خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/461989" target="_blank">📅 13:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461988">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/350f6d020c.mp4?token=WYw7RAmLQmbF_Sr6E8poeTw7lpms5qKhjBo-7KlJ9Ugua3JseAJKgvEBMEb9Fg2L7qHmXV6pB-m0wJx5iiN0WmBphYIyX41zvjznk5jDPgbqf2AjOvOZrqvWVr12_02yoKwKe9yKAIN4Sk-p2YBMnNQAA4TBPf5vxOr8JTaNa0ckY-Nk6WcQ7q1EpbQQoKwOHAnaW0ogWkZYAhbS-WOgXswF1GrUIuO01FUpp19zSXHFJJWS1zCybiT3ZJc0A0JF5V0hOevNDztPoCXEYP1W3vvfmqxw9dfzAdWk0CLcibdtTLfizonPDs-45kCU895-MI1H74IlMzONW1Hy-n9AlTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/350f6d020c.mp4?token=WYw7RAmLQmbF_Sr6E8poeTw7lpms5qKhjBo-7KlJ9Ugua3JseAJKgvEBMEb9Fg2L7qHmXV6pB-m0wJx5iiN0WmBphYIyX41zvjznk5jDPgbqf2AjOvOZrqvWVr12_02yoKwKe9yKAIN4Sk-p2YBMnNQAA4TBPf5vxOr8JTaNa0ckY-Nk6WcQ7q1EpbQQoKwOHAnaW0ogWkZYAhbS-WOgXswF1GrUIuO01FUpp19zSXHFJJWS1zCybiT3ZJc0A0JF5V0hOevNDztPoCXEYP1W3vvfmqxw9dfzAdWk0CLcibdtTLfizonPDs-45kCU895-MI1H74IlMzONW1Hy-n9AlTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آغاز پویش «برای آینده‌سازان»؛ اهدای یک میلیون بسته لوازم‌التحریر
🔹
همزمان با آغاز سال تحصیلی ۱۴۰۵، پویش «برای آینده‌سازان» با همت سازمان بسیج سازندگی و مشارکت خیرین کشور آغاز شد.
🔹
در این پویش، یک میلیون بسته لوازم‌التحریر به‌صورت رایگان میان دانش‌آموزان مناطق کم‌برخوردار توزیع می‌شود.
🔹
افرادی که تمایل به مشارکت در این اقدام خیرخواهانه دارند، می‌توانند از طریق پیام‌رسان‌های بله، روبیکا و ایتا با شناسه زیر اعلام آمادگی کنند:
@pouyesh8
@Farsna</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/461988" target="_blank">📅 13:58 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461987">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c6ebdf139.mp4?token=UnY6UM3u4l06AQSJOrdNPATF183TAbRVhg_msarMKEm-T5zgAm1UqSlPWrBQ7o9tNTrx1GDnKdNv-ixJkOqATlpcSsXRilfztF7_GxzPQnRRy9HBWsOYaWjjG8WJfvvMqv0o6lDCXZud52ja-Ryd7xqSy3DXKZBy6LSW-_uOfub4Bv4SyymTk-SDw9L52D4cAkoBtzZJ_Wx2s2A_0T4WREoMOkBZppGxtI1LoQeyyRjrdAZzRQhWPknNPq1CtohpEDGvGljFzXIb5Y1ICoC0oMpa1AYIWmRyVXVpuyu-y30ANnAyZBKaWns9qhewSi-UK9MQ7_ntd_Gm8eMKFU8KFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c6ebdf139.mp4?token=UnY6UM3u4l06AQSJOrdNPATF183TAbRVhg_msarMKEm-T5zgAm1UqSlPWrBQ7o9tNTrx1GDnKdNv-ixJkOqATlpcSsXRilfztF7_GxzPQnRRy9HBWsOYaWjjG8WJfvvMqv0o6lDCXZud52ja-Ryd7xqSy3DXKZBy6LSW-_uOfub4Bv4SyymTk-SDw9L52D4cAkoBtzZJ_Wx2s2A_0T4WREoMOkBZppGxtI1LoQeyyRjrdAZzRQhWPknNPq1CtohpEDGvGljFzXIb5Y1ICoC0oMpa1AYIWmRyVXVpuyu-y30ANnAyZBKaWns9qhewSi-UK9MQ7_ntd_Gm8eMKFU8KFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: باید به تولید و اشتغال کمک کنیم اما مبارزه با فساد هم از اولویت ما خارج نشود.
🔹
نباید اجازه بدهیم در پی بروز مشکلاتی برای بنگاه‌های بزرگ و کوچک دولتی، آن‌ها تعطیل شوند. @Farsna</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/461987" target="_blank">📅 13:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461986">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3L66GrvN5-whrlp0tHAmwDo0E7Qn8hZcR2yfYGAFcIE5WZmRpp4zKU4mccfn2laPENrMqLkPuF__zO3Mr6Ea0wTprh3EUZ8-4P51lgUadiS9PeaTP602YUt1b7yic9xIdFFYWikL_iN-b0T9XCRwpIjBvJwIH7dz2V-BnNvaG9Af3XTsV3-ZUreAJPoUtIJYcmssjGYAReSP20E8e6TzD57n44mnQlJsPqYDt0HoNQrlmncPuvduO8JeihaeS_3imXq0Nj4CTEOreecSnnLsPik6B6KkZvzc7PKj9AwI4DgZqOFgzl0jc8-6aqGpwIRK5QFuor60U-99yS0udjIww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عارف: قانون ملی توسعۀ هوش مصنوعی سریعاً اجرایی می‌شود
🔹
کارگروهی برای اجرای سریع این قانون تشکیل می‌شود. راهبرد دولت، دستیابی ایران به جایگاه تک‌رقمی جهان در هوش مصنوعی است.  @Farsna</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/461986" target="_blank">📅 13:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461985">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEhZW88flde9weMGgfw9IKPtv3uiUW3x5SumWMC2veEuH1B7duBaMfwDQWS0ktCODP0eNKVT_hrwFndWDHfM4dPhMNn7DAAX3z2hI3ikErG_C_OSDFulPI62VbZi9SD15N2Vbn016jUim0FEoa8dpeJAMjZv9SSYnRiVTmBtTMaYSmhGW4Je_Ncv5LXkFo-627nU3-I-UYsO1Hg9LvECRuIjP9amccOZnwRFZvSSoHt-umFVWn4BrMAFbhl7OpzN-nPJkiYMKA2yfhS0hbp0WBrwwiJ7bYCRmb57IiU6Y8SFR8uG67lQct0XD-LEiT6Do79jND2SdbKmi9--faA_BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌مجلس قانون ملی توسعۀ هوش مصنوعی را برای اجرا به رئیس‌جمهور ابلاغ کرد.  @Farsna</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/farsna/461985" target="_blank">📅 13:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461983">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e00de65ab7.mp4?token=XxCeZzcyR2cVsW3VOaC9_cSaZ0VkqwEmoJ1kvg1PZgyxmBvKufubKYSEjRaelFJpeZD3YuK71lzqXNmc01e5e17_A8aq6h3F8UsltMQInMMz7-wUXcwYWmetzZGps2rsCp1qZ9pqncNa4V2H_LR0MVfqfvut8p513VSOYveYOHr4tad5IxL-09nIexN_U3HfzmaWt4e9BIPoSqACYsH8TcewDN4JGU7i1NHQkEhy4N4AaDnXTL42FmnR7ih_o2aerXjAktTtkvwkNx4xq2ZixPsr10CBm3rX12Ft7tg0cfd1X0smXV-kBt1U88xNnRKHVqax1F-sECa8itfR4FhUBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e00de65ab7.mp4?token=XxCeZzcyR2cVsW3VOaC9_cSaZ0VkqwEmoJ1kvg1PZgyxmBvKufubKYSEjRaelFJpeZD3YuK71lzqXNmc01e5e17_A8aq6h3F8UsltMQInMMz7-wUXcwYWmetzZGps2rsCp1qZ9pqncNa4V2H_LR0MVfqfvut8p513VSOYveYOHr4tad5IxL-09nIexN_U3HfzmaWt4e9BIPoSqACYsH8TcewDN4JGU7i1NHQkEhy4N4AaDnXTL42FmnR7ih_o2aerXjAktTtkvwkNx4xq2ZixPsr10CBm3rX12Ft7tg0cfd1X0smXV-kBt1U88xNnRKHVqax1F-sECa8itfR4FhUBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: بیش از ۳۰۰ شرکت وابسته به دولت بودجه‌هایی دریافت می‌کنند که مجموع آن بیش از بودجهٔ دولت است.
🔹
برخی از این شرکت‌ها زیان‌ده بوده‌اند اما پاداش می‌گرفتند. حتی یک نفر در چند شرکت عضو هیئت‌مدیره بوده است.
🔹
سازمان بازرسی گزارش کرده که ۱۵۳۵ نفر به صورت…</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/461983" target="_blank">📅 13:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461982">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f4940bbf4.mp4?token=BMgMMta7slG_6pLtjde96BkX9YulZpVT7Ur7I6dKQwa3prWRt9w8-gVLcMmohgCmvJKHu1RAhB8wcardzsO7ToueN_agsZsBNpmtJ7pONfbkqGQHrc61hlrh21NLkuL2qANHEm4i2tzrUGROR4ML4DfcvZAqCab_4xufYRURCEXcGAyDBv2eaptL3Aw12xjg8Sqs1lyrEPuw9-dMWNutX-qXfUf88Wp49qW-rX2Q_glID_5L7XGw_PoC-pH2iHB9RQEQrHPj2Xh9X8ERF3CfzDfMQEuW7uaLlVvv4U8RUyKF064xm7nG-xjPy3v6vrDSJSDoqKODTIIQBNe7_NyKBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f4940bbf4.mp4?token=BMgMMta7slG_6pLtjde96BkX9YulZpVT7Ur7I6dKQwa3prWRt9w8-gVLcMmohgCmvJKHu1RAhB8wcardzsO7ToueN_agsZsBNpmtJ7pONfbkqGQHrc61hlrh21NLkuL2qANHEm4i2tzrUGROR4ML4DfcvZAqCab_4xufYRURCEXcGAyDBv2eaptL3Aw12xjg8Sqs1lyrEPuw9-dMWNutX-qXfUf88Wp49qW-rX2Q_glID_5L7XGw_PoC-pH2iHB9RQEQrHPj2Xh9X8ERF3CfzDfMQEuW7uaLlVvv4U8RUyKF064xm7nG-xjPy3v6vrDSJSDoqKODTIIQBNe7_NyKBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: بیش از ۳۰۰ شرکت وابسته به دولت بودجه‌هایی دریافت می‌کنند که مجموع آن بیش از بودجهٔ دولت است.
🔹
برخی از این شرکت‌ها زیان‌ده بوده‌اند اما پاداش می‌گرفتند. حتی یک نفر در چند شرکت عضو هیئت‌مدیره بوده است.
🔹
سازمان بازرسی گزارش کرده که ۱۵۳۵ نفر به صورت خلاف قانون در هیئت‌مدیره‌ها بوده‌اند، اموال نامشروع باید به بیت‌المال برگردد.
@Farsna</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/461982" target="_blank">📅 13:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461981">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBoGbnoZvUyuSigtNhXHAo4B-y2WMdfUZyQSh933CxTkxOMhq_i5ADM6P3hMP6SEpPxjO-vj6Lgr1zVQkpB1-nN8-7adeHeGCPX5bOkZcGtpSdx6_0lkkJsD06mqfOT1M0HYevgPZ6LVQdc9OmmZygyjCcePcy5Oz_ZSBRgAy1ZUSaZXlW1hB0p7S7tx-1ECcml74XSlhzXnzDDXWhzWM5l5sM2edMvcmLZRCAcbN_SYpdYRSdXyR-41GwImNigNfyF-zW7M4xiKj7zD5UmBPwX14L028PmLijE5lSfKNUr8J7LPY8MjaeVdZlrylTybCKtWREIcWy9b9ufjALHmWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستیار محمد مخبر: انتصاب مخبر به‌عنوان نمایندۀ ویژۀ ایران در امور چین صحت ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/461981" target="_blank">📅 12:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461980">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohT_6BFN6taXI-WG579pOu9jygVrWN1rTbGuaOzcO_z_z3Qu-pHfdfgMz2zlCv9UiomqPGunnQMjDirrobSXh_koOgnqIO_YSE6OKDjUNkULKltCf6yfkA134jT0w59wQgl8f1bMXeNCtiUC1jNwk7nmPlN-tfqfZH18-wSVW-NUEuwVGRHXgNZHaE685cRuXz4SvhOa-_s9we2FKePz0AGZzGwC5qIXQnahEkaAwUknJMZQP6Y2zagy8meCQEZFF9Ef0J3SBLhJiocfpGEqvsbg-HueVTCAIt5im8feapdzSfVvjLaTrr0y-qrz2RV3uOVlOYhey6Gp6NjpyWaeKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیرانوند به لیگ یک سقوط می‌کند؟
🔹
با صحبت‌های فرمانده فراجا بحث‌های زیادی در مورد آینده فوتبالی  دروازه‌بان ملی‌پوش تراکتور مطرح شد.
🔹
برخی معتقدند بیرانوند اگر ابتدای مهرماه دفترچه اعزام به خدمت سربازی بگیرد می‌تواند با تمدید دو یا سه باره تاریخ اعزام خود…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/461980" target="_blank">📅 12:43 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461979">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PjYnqLkLl08xvYM9Fz5AhhGjAGAzGloqP5YGfcYju7__MfXOeDBJ0RdiJulxjFt1zTzmE1wJEiC3DnT4eFQWckajzM9qNVcTCsuxverrRsrc-8eCOUH1TOXapt6hcQrS0Xkr8EPUfecliMjcBj39rbKpbzEaUaNSdf5LpRasXHnylqB8gu0UBfXUq9WSABKCVdC6ICD34AL_Kw7Xj4lLTTesC-hpVhKjkVvoXmcdleoGee10wbakuOSLXEbyyKgZD6-5go2eWW2v32plS_C1E7UWyF1nnXr1qCQ6gwMdD7Ew8Bww1gGY8t0Oo05WQ3pt5jndm9aSXDqItA7Bx5g-AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار نهاد مدیریت آبراه خلیج فارس به مجموعه‌های مرتبط با شناورهای متخلف
🔹
فهرست شناورهای متخلف در آدرس
www.pgsa.ir/non-compliance-list
به‌روزرسانی شد.
🔹
به شرکت‌های بیمه‌گر، کلاب‌های P&I و همچنین موسسات رده‌بندی هشدار داده می‌شود، به‌منظور مصونیت از تبعات ناشی از ارتباط با این شناورها، از ارائه خدمات به آن‌ها خودداری نمایند.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/461979" target="_blank">📅 12:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461978">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDmhBtHcomlT5fovANuPt2tCnNtbsQpHI-zAKO7eTTrA4iaXWDgK7cnoouY4LZa5RI_M_NnvBh1vFiHzfoaRX8Y10EAGnKfWopbfun6hPy2n0lSlz-yPK2ZH2Op0NPVZ5RrqcVHslv-0coQFKylX3KwFDtmJuL2Bx8Cj-yCKhcZygiLiBngtfSGSanyLsQC-3KIN1irx6E6zxDdTGV7Gt9xJHo-DulBpBuMnYkzrB_bOFg_QHqLAGb15Q6LIUG3qIhIwVEteLrHQehGtEKgKAHBt6aVvidm85qVk7uErjjSk3GoH_dxd6VMbrGCPrib_ooawLfxNghxQAEJlyqpQ2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با کاهش ۳۸ هزار واحدی به ۷ میلیون ۳۹۳ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/farsna/461978" target="_blank">📅 12:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461977">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TssqGQxFlg322u7RLge99Pjjfqc1iaKnZucMdm9tLRuLyfZodkDYJkINWS05qYkzpOJAQc3vuORLMWHwJDDNUjDM_nepo7jt6bNLmrdbpLtB-8QTYjPQUV6HDvC3ucNsyOMQLk-dKCFJUlikUM7rSCx_q8q_LDUfNFQKPwyvXcbON6HJ6ztBhy69TL8uEJbXToRyYvJPgY8sLCDVWqtLjVTH9AxI04GRPNQYrMcjOGooC6LYP4jb1ISOgiTMivCra8rL0oklqTyWGomyM6hdndRK3x8MtVlrZsOT6Ej5_n3wNBv9XaDzOykmtPeFp9icqEzqoTMaYnQo6u4Y9UCCEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
📝
سلاح جدید منافقین؛ نفوذ در سایه هوش مصنوعی
🖼
امیر حمزه‌نژاد: گزارش تکان‌دهنده شرکت آمریکایی آنتروپیک، پرده از سلاح جدید منافقین یعنی «هوش مصنوعی» برداشت. این سازمان تروریستی اکنون از AI برای عملیات‌های پیچیده نفوذ، از جمله جعل هویت فعالان سیاسی و بازسازی دقیق لحن آن‌ها استفاده می‌کند تا با فریب دادن کاربران، روایت‌های دروغین خود را به خورد افکار عمومی بدهد. این پروژه نفوذ، فراتر از یک تبلیغات ساده، یک عملیات سیستماتیک برای مدیریت فضای مجازی است.
‌
🔹
در کنار جعل هویت، این سازمان از هوش مصنوعی برای جاسوسی دیجیتال، استخراج اطلاعات افراد داخل ایران و تولید سخنگوهای مجازی استفاده کرده تا یک «حمایت جعلی» و سازمان‌یافته را به نمایش بگذارد. این در حالی است که چنین اقداماتی در کشورهای غربی جرم محسوب می‌شود، اما منافقین همچنان با حمایت‌های خارجی، از تکنولوژی برای پیشبرد اهداف تخریبی خود در برابر جمهوری اسلامی بهره می‌برند.
‌
🔗
برای خواندن جزئیات،
اینجا
را کلیک کنید.
@Fars_plus</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/farsna/461977" target="_blank">📅 12:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461976">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">دستگیری ۸ نفر درپی فساد مالی در آموزش‌وپرورش رباط‌کریم
🔹
دادستان عمومی رباط‌کریم: ۸ نفر از متهمان مرتبط با پرونده‌های تخلفات مالی در آموزش‌وپرورش و برخی مدارس شهرستان بازداشت شده‌اند.
🔹
اتهامات مطرح‌شده در این پرونده عمدتاً مربوط به تخلفات مالی، از جمله اختلاس…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/461976" target="_blank">📅 12:10 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461975">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83658a959d.mp4?token=Q2HHZjyGlwOS5rRTe5ylLhT9lxlpteS8zuG17u8LCLTP5pDVtJ_bzM2Ul1dU8jBO1-LomPJ5GCUSvZnbHdFBjndH9O3gHTYnfG07uLvjrzFsWzwYwvrsxJcRfWq0T9WrsGhzxsmlYi8QqHzqn_W3qkwayqFmPUAm1Rvlae91vSeFZlCiUwsdO3u6SgpR_S8el-EeAJjsdP-d4nvAnVe2FH5uaNGNvndGXBqcsC9lcwgEKk1qTlsKe7woRDjDbaGVLI-Fh7nnTcte2T85dh_hoE-b_mgKDa1RgFs1ZF9r8JBhg0DM6_avlWPJLOrnRK44n50LqpeAQu-Oaki1cJpETw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83658a959d.mp4?token=Q2HHZjyGlwOS5rRTe5ylLhT9lxlpteS8zuG17u8LCLTP5pDVtJ_bzM2Ul1dU8jBO1-LomPJ5GCUSvZnbHdFBjndH9O3gHTYnfG07uLvjrzFsWzwYwvrsxJcRfWq0T9WrsGhzxsmlYi8QqHzqn_W3qkwayqFmPUAm1Rvlae91vSeFZlCiUwsdO3u6SgpR_S8el-EeAJjsdP-d4nvAnVe2FH5uaNGNvndGXBqcsC9lcwgEKk1qTlsKe7woRDjDbaGVLI-Fh7nnTcte2T85dh_hoE-b_mgKDa1RgFs1ZF9r8JBhg0DM6_avlWPJLOrnRK44n50LqpeAQu-Oaki1cJpETw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مسیر فرار نفت عربستان از هرمز در آتش سوخت
🔹
تصاویر ماهواره‌ای جدید یک ایستگاه پمپاژ متعلق به خط لولهٔ راهبردی عربستان سعودی موسوم به «شرق–غرب» را نشان می‌دهد که درپی حملهٔ پنجشنبهٔ گذشتهٔ یمن، به‌شدت آسیب دیده است.
🔸
این خط لوله حدود ۱۲۰۰ کیلومتر طول دارد و نفت را از منطقهٔ ابقیق در نزدیکی خلیج فارس به بندر ینبع در ساحل دریای سرخ منتقل می‌کند؛ اهمیت آن این است که عربستان می‌تواند از طریق این خطر لوله، تنگهٔ هرمز را دور بزند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/461975" target="_blank">📅 11:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461974">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b699798088.mp4?token=HdhBOewiktUy6hhGZ4_v2-CQuHNnIjN2rXtKBihwiMIBvyCicNiQilBGo4XahtYZCqkpX-2FBYhwpeJEm8EN0_oOabGVmrxVEyR7gbzpFaPUIiV4DGceOcKplpgUTReMte-s5agP6NUQky0CxKT5w6TFMoNjzTsX3AN5VGP-uURN1RJlaYre5EAOXxzMiW0hpCGZoRTPHMqU7bfRBsp2HY7bdjTreH7pIsfwPOwfwlm9VY6-Lm0z0Z9lgR53ooG-XXVTqsh7SlYPmZssa8WrTOsLBco0WsiaJNvv2iXYL0a9aa-O1mAfer91GAHtxclcGo5ZJx6VrODZcYkdwYyvVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b699798088.mp4?token=HdhBOewiktUy6hhGZ4_v2-CQuHNnIjN2rXtKBihwiMIBvyCicNiQilBGo4XahtYZCqkpX-2FBYhwpeJEm8EN0_oOabGVmrxVEyR7gbzpFaPUIiV4DGceOcKplpgUTReMte-s5agP6NUQky0CxKT5w6TFMoNjzTsX3AN5VGP-uURN1RJlaYre5EAOXxzMiW0hpCGZoRTPHMqU7bfRBsp2HY7bdjTreH7pIsfwPOwfwlm9VY6-Lm0z0Z9lgR53ooG-XXVTqsh7SlYPmZssa8WrTOsLBco0WsiaJNvv2iXYL0a9aa-O1mAfer91GAHtxclcGo5ZJx6VrODZcYkdwYyvVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
پزشکیان با خالد بن محمد بن زاید آل نهیان، ولیعهد امارات دیدار کرد.  @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/461974" target="_blank">📅 11:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461973">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77b29b6427.mp4?token=miLciB337M1l9o96Hs9atpf37sMD1wYbelUWYyAv8HtfSUnduVXaO8IxmwPlPJPEswvB1f_fd2qiRPDh7Gn_tpocHCrpfAFhblaoGi-RAPVL238JUXrs7BcPON25QharlExhZ1C4I5ZOjDBW5iwbX12IQfaWOjjKdhZG1fW6b2WY-4Y_mscDCmux-YYonoLvc3cqKUXrvxfdpoWHPz_Y3gEcC7sbVt10zSf3c8ZF1_iwVePk19HPfOUH4F_POT_PDmY6LI2T0CCydhGpCFAiCOAES-TeI5vCzeK8hB9bxCFS4uCYSru7Vr0u4ZbrHqz3zqcFwTqU2R-fw8XBGcR7aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b29b6427.mp4?token=miLciB337M1l9o96Hs9atpf37sMD1wYbelUWYyAv8HtfSUnduVXaO8IxmwPlPJPEswvB1f_fd2qiRPDh7Gn_tpocHCrpfAFhblaoGi-RAPVL238JUXrs7BcPON25QharlExhZ1C4I5ZOjDBW5iwbX12IQfaWOjjKdhZG1fW6b2WY-4Y_mscDCmux-YYonoLvc3cqKUXrvxfdpoWHPz_Y3gEcC7sbVt10zSf3c8ZF1_iwVePk19HPfOUH4F_POT_PDmY6LI2T0CCydhGpCFAiCOAES-TeI5vCzeK8hB9bxCFS4uCYSru7Vr0u4ZbrHqz3zqcFwTqU2R-fw8XBGcR7aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: فلسفهٔ وجود ان‌پی‌تی زیر سؤال رفته و همین باعث صحبت دربارهٔ بازدارندگی هسته‌ای شده است.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/461973" target="_blank">📅 11:45 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461972">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Of8vHz8ebQ_M9QAkMF_8hUglAgHEn1O88NSs83SG35iOR9pARRbPdQCRcONBe1w_NCC0J1XPvL_EeAu1vS6Fs-hD41ufCfdbKe_anrqQc078E6E0UJ137jPrFrPm1BDStsY7gInKyhTjdT8DXeFnrsf0i69Mn6DHcQ6_SjQCU503oF9kbOHleWwnWecE7HHQCc-E7gLJmgscFh_ZcGMJKkXaUNd7ynFvAk8e1qktDRXYI0mca3PFXKXJvmPcKWS6DvCGmT7vWV8Smgb1EGW5Zf65S3rmyo5_JT9cETujgvhmUzi2rHF9aE93XiarQay4IQkiyRyJ6Gcpo-yYB_2AHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سخنگوی نیروهای مسلح یمن: با ده‌ها موشک و پهپاد، انبارهای هواپیما، رادارها، باندها و انبارهای مهمات را در پایگاه خمیس‌مشیط هدف قرار دادیم.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/461972" target="_blank">📅 11:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461971">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7280a7022a.mp4?token=W8Xjd45_ztLosiXmOI8KeTOzRU7hCZj5qpXAPVQGj_VuQ0K43R8r2EbY0UbfdT6XAGpSY6B7bix96dqmXeqzSCkPeDLvyIlNFvv-XR42VYzXFwRk_YMeVZTt2oIm5_9sqeprtICMxZtV6C-Z63KIho-GND5wap7DZiOHtJAGTyx6mAZxVMc-IO_Fim0ilWl7W3PSz1WF6_WjTVAg4cRijz9SKE7CjoXwSTn0PZ6ILRglpCfY-Owy3Ll5OoP6lHrsNQ4_4Rf3pnf-BGX2VDdBlS7XAWKyyQVssfD46xokhJjcVEEe9Lol_d_sYBsT3vGIf9FFcAKDLYq_v20WhQDN0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7280a7022a.mp4?token=W8Xjd45_ztLosiXmOI8KeTOzRU7hCZj5qpXAPVQGj_VuQ0K43R8r2EbY0UbfdT6XAGpSY6B7bix96dqmXeqzSCkPeDLvyIlNFvv-XR42VYzXFwRk_YMeVZTt2oIm5_9sqeprtICMxZtV6C-Z63KIho-GND5wap7DZiOHtJAGTyx6mAZxVMc-IO_Fim0ilWl7W3PSz1WF6_WjTVAg4cRijz9SKE7CjoXwSTn0PZ6ILRglpCfY-Owy3Ll5OoP6lHrsNQ4_4Rf3pnf-BGX2VDdBlS7XAWKyyQVssfD46xokhJjcVEEe9Lol_d_sYBsT3vGIf9FFcAKDLYq_v20WhQDN0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ لحظه‌شماری نخبگان ایرانی برای کالبدشکافی زیردریایی به دام‌افتادۀ آمریکایی
🔹
کارشناسان حوزۀ نظامی معتقدند غنیمت واقعی ایران از شکار زیردریایی هوشمند آمریکایی در دانشی است که از دل این سامانه استخراج خواهد شد، و آمریکایی‌ها باید نگران روزی باشند که فناوری…</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/461971" target="_blank">📅 11:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461970">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a955b41d1b.mp4?token=rQ5q_kq_38vSD8KWKc3rdEJFDWfZU-EWAD7i4eWdNZjWMlA4crIrr9LjJwgIDG-q7tBn4w3Hiqq6jJbGGZMhwo2a945DywLNGQu4_exiz7-N1eIvtKLIvnMhZfzn2iHrfCBy1CVjkqZNiaipTg7Q4vHstXru7RfRzxmXcIt3KkMltFAD7X2ArnUAZtFtvXaa22lpqEq_p3MhUWmJU9IIqSBRWjG0UmmYQ7YQe-8dgoiV1ZfIDDHMNhZczXCePQ781lY-lbbgNQWFtFDFAVaFU7pZJ-qDMs5a5m-iYULBIJKClDGJ-2lRBHWyWIuMtleaDxxMwG-Y4YTLWJrDkU4ciA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a955b41d1b.mp4?token=rQ5q_kq_38vSD8KWKc3rdEJFDWfZU-EWAD7i4eWdNZjWMlA4crIrr9LjJwgIDG-q7tBn4w3Hiqq6jJbGGZMhwo2a945DywLNGQu4_exiz7-N1eIvtKLIvnMhZfzn2iHrfCBy1CVjkqZNiaipTg7Q4vHstXru7RfRzxmXcIt3KkMltFAD7X2ArnUAZtFtvXaa22lpqEq_p3MhUWmJU9IIqSBRWjG0UmmYQ7YQe-8dgoiV1ZfIDDHMNhZczXCePQ781lY-lbbgNQWFtFDFAVaFU7pZJ-qDMs5a5m-iYULBIJKClDGJ-2lRBHWyWIuMtleaDxxMwG-Y4YTLWJrDkU4ciA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بلومبرگ: آمریکا مانع شرکت اسلامی در نشست آژانس شد
🔹
به‌گزارش رسانه آمریکایی، دولت ترامپ با اعمال فشار، از سخنرانی رئیس سازمان انرژی اتمی ایران محمد اسلامی در کنفرانس عمومی آژانس که قرار بود امروز انجام شود، جلوگیری کرده است.
🔹
طبق این گزارش، به نقل از یک مقام…</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/461970" target="_blank">📅 11:29 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461969">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f17bf073a.mp4?token=Pn0pRB-qC8LPrUnnf0yHq5zv37IvTECNKhSeqvUxssrEIlK-2Fiil2gbpgHpvcmiQ2KA8QFktznsO8ZSGtAte0Dqm3a2SytLjF_KlPFdUYbguodxZAmbtAlOv_TW_7x4FbvBVdqOOIJFiXlH-n2ll0NxMwDwsaCN9wMfWQnYsILPWG_Ue9wbOL-47MtTsNb8nP8g9hvl5DazdZn-cgGsxEDvpcojoPspMrNorY27qI8R4luLFkcJhTdfEP3Qn7zcoPr6DTn_6yEqiv8HfmlVcj7djFhMqOH1gXpx2y_T-9KUTVYqtuUG5I9OIcajJOOuZgpR33lLN7RfLh2hoLdYZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f17bf073a.mp4?token=Pn0pRB-qC8LPrUnnf0yHq5zv37IvTECNKhSeqvUxssrEIlK-2Fiil2gbpgHpvcmiQ2KA8QFktznsO8ZSGtAte0Dqm3a2SytLjF_KlPFdUYbguodxZAmbtAlOv_TW_7x4FbvBVdqOOIJFiXlH-n2ll0NxMwDwsaCN9wMfWQnYsILPWG_Ue9wbOL-47MtTsNb8nP8g9hvl5DazdZn-cgGsxEDvpcojoPspMrNorY27qI8R4luLFkcJhTdfEP3Qn7zcoPr6DTn_6yEqiv8HfmlVcj7djFhMqOH1gXpx2y_T-9KUTVYqtuUG5I9OIcajJOOuZgpR33lLN7RfLh2hoLdYZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تأثیر قطعی پایهٔ یازدهم در کنکور ۱۴۰۶ پابرجاست
🔹
دبیر ستاد علم‌وفناوری شورای‌عالی انقلاب فرهنگی: درحال‌حاضر، تأثیر پایهٔ یازدهم برای کنکور سال ۱۴۰۶ قطعی است و شورا مصمم است مصوبهٔ موجود را تغییر ندهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/461969" target="_blank">📅 11:29 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461968">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">انفجار کنترل‌شده در جنوب اصفهان
🔹
سپاه اصفهان: احتمال شنیده‌شدن صدای انفجار کنترل‌شده در صفه، بهارستان و اطراف آن تا ساعت ۱۴ امروز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/461968" target="_blank">📅 11:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461967">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dbaa79b50.mp4?token=YgDuylvNMNcBgztZ9KFF5bZELZXTIbqk0nYM74X2EQNiDaDV-tjrarnYEHllhTDVWCKstgawix83UKCHcfrjTMvWc7y6xd8tcmIBPJQSvJC6KLR4VrbSfIdLv7ijBvCEdjbBgNcu2a5D7VdmxgyZ4H6lZ3JIDPhYIFVhi_gQ6LZ46UnAaBC7qQdDGDAwyVIKslSjvN4sfg4jmvwQmgfKTGj68sFfVdDSEprAd3rJDHzsYaR6k73d4GGsESWtamdOtqWMBZPLpXzET3yJn_TtSVdpaIH9e1qtaV10CjfS3BC1fTkm4JLPjMgvJNfETeWvQwYIALHIYux0mM0m7ZpnpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbaa79b50.mp4?token=YgDuylvNMNcBgztZ9KFF5bZELZXTIbqk0nYM74X2EQNiDaDV-tjrarnYEHllhTDVWCKstgawix83UKCHcfrjTMvWc7y6xd8tcmIBPJQSvJC6KLR4VrbSfIdLv7ijBvCEdjbBgNcu2a5D7VdmxgyZ4H6lZ3JIDPhYIFVhi_gQ6LZ46UnAaBC7qQdDGDAwyVIKslSjvN4sfg4jmvwQmgfKTGj68sFfVdDSEprAd3rJDHzsYaR6k73d4GGsESWtamdOtqWMBZPLpXzET3yJn_TtSVdpaIH9e1qtaV10CjfS3BC1fTkm4JLPjMgvJNfETeWvQwYIALHIYux0mM0m7ZpnpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: مذاکرهٔ جدیدی با آژانس نداریم
🔹
صحبت‌هایی که دربارهٔ فعالیت‌های هسته‌ای در محل‌های جدید از جمله کوه کلنگ مطرح می‌شود، تحت‌تأثیر سیاست‌های برخی کشورهای عضو این آژانس است. @Farsna</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/461967" target="_blank">📅 11:21 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461966">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18a153e034.mp4?token=I-ATwQywx0TkkuXKBw9Lq8h82fCepigKAZwfIVqbc33Z06gj_7x2g2Onij7QfANc1tcT70UWgPToUouX74X7yDLBe6gznfZy_o0CKhxdZGbMi6oOKsEyZu6kvHfrrDj-PuUMQACAhJE944PbmTK9SheiwbbgHByyLgrKWK4C63Z7aNSFBK0J7KbXUWC3DeYwm-G-Huu_nBl-3KcVaW_OCM6woOUzMfgRgILJLXyU4Vn4XUor1sP-C5_oIjFiPxvUjLHnJ8mFN4Im0npGg3JrCnj4mS7CpNXSRtXxtrNc1vaKRvUqKjbvV0OfOiGRNypb9omx8YfRO-DZLI7DVML-_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18a153e034.mp4?token=I-ATwQywx0TkkuXKBw9Lq8h82fCepigKAZwfIVqbc33Z06gj_7x2g2Onij7QfANc1tcT70UWgPToUouX74X7yDLBe6gznfZy_o0CKhxdZGbMi6oOKsEyZu6kvHfrrDj-PuUMQACAhJE944PbmTK9SheiwbbgHByyLgrKWK4C63Z7aNSFBK0J7KbXUWC3DeYwm-G-Huu_nBl-3KcVaW_OCM6woOUzMfgRgILJLXyU4Vn4XUor1sP-C5_oIjFiPxvUjLHnJ8mFN4Im0npGg3JrCnj4mS7CpNXSRtXxtrNc1vaKRvUqKjbvV0OfOiGRNypb9omx8YfRO-DZLI7DVML-_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ مدیرکل خلیج‌فارس وزارت خارجه: تعویق نشست تنگۀ هرمز به درخواست برخی کشورهای منطقه و تصمیم مشترک تهران و مسقط صورت گرفت.  @Farsna</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/461966" target="_blank">📅 11:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461964">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/liVNzrNZno55e8P_wcSTmjXxiGAebR7XANkxTXXzZC4w6hzraP_d8mURbe_vMdJXIErmNRBubFWcMSTLExxiAv8Q_WeMY7e8mll5o5J-uihOuazdxyV1aXuOZWZa6QcdrGjeWh0G6ZTpJRfMFP5holhtVCFj7d4vIbryHUrcaSuhiyo5uv643q6-pZ4OjPNJpz6dMgVBRg_D8iwO_pIpjOMXI6XmGuGqgi4N6x46fKFY7MXk-GyuSQvGF8lxTYNOwfaTuhQF6k1PyhK1XEJpZLvf85Gw2XA3-UIASwQPcUJdEcut9siZsBIPbhEIunEXruFMcNSK8xg8_oxZyF-I3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلومبرگ: آمریکا مانع شرکت اسلامی در نشست آژانس شد
🔹
به‌گزارش رسانه آمریکایی، دولت ترامپ با اعمال فشار، از سخنرانی رئیس سازمان انرژی اتمی ایران محمد اسلامی در کنفرانس عمومی آژانس که قرار بود امروز انجام شود، جلوگیری کرده است.
🔹
طبق این گزارش، به نقل از یک مقام آمریکایی، جلوگیری از ورود اسلامی به اتریش پس‌از آن صورت گرفت که درخواست معافیت او از تحریم‌ها که از سوی سازمان ملل مطرح شده بود و امکان ورود این مقام ایرانی به اتریش را فراهم می‌کرد، در پی فشار آمریکا رد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/461964" target="_blank">📅 10:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461963">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i8Ksjyfk3YqP_clD071NoDnzEavHh2ZUFv5DVmxtTeTbyv20fkJJBIBdtJHMSoDtoIuUQlei52J4RF0X9AwtBFblknuAssV2NONWq_2tjY52d99jdotWLGEhdYE9eL75se5-KZMIXOwvRdqywP07YnOAPKviy7HUAVMXTqlM8Zl3l_9Ca8RFbdpR4UsbW7FcvBd49vZ-OEIBY6wXSvAqIRZtMGUmzQjXRR1mlySVKLb_VvLL0WnYHHfVgObnUcm96AuQ5CgcOFuSV9v6Jrg3HtHDqovnuUFNqCrdA2RkJXXzCr7RNc3JN94LMMrUpTa5BDOi75kUwzEhD4RSzGRpJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز ذخیره‌سازی مرغ تولید داخل از امروز
🔹
شرکت پشتیبانی امور دام کشور: درپی تصویب مجوز افزایش ذخایر راهبردی گوشت مرغ در ستاد تنظیم بازار کشور، این مجموعه از امروز فرآیند تأمین و ذخیره‌سازی مرغ تولید داخل را آغاز خواهد کرد.
🔹
براساس ضوابط تعیین‌شده، مرغ‌های با وزن ۱۲۰۰ تا ۱۸۰۰ گرم، به‌صورت منجمد و شیرینگ‌پک‌شده و با نرخ هر کیلوگرم ۳۳۵ هزار تومان، تحویل درِ سردخانه از تولیدکنندگان پذیرفته می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/461963" target="_blank">📅 10:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461962">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwz37Q69-dQUzx0faQFR1PqMqbpOf--m2JV3cP-L2UtTjXX8cG0gWplpFlrLJkcFz079KEgJWos4zOMpZvXhAGS_iC2x6ZnMqXfV-EPJmGMuPKTron16cR7Qdc9v8W2KAeKlKTbcGWMrcgZo-CWEBIZsshl8OkDQNwPY1uiYG787LW5weFhup1Mlf9YfQG3iHFX7X1-r_24BPCrIvruFhWzVyjx2dW7qFHFRck_8mIUcm8MA4ITRn5kDyDTNf0x9dV4s9OMYkOxQDi-NXvOa4noMXnZdnmKWhWpv1pTBg32M-ridbGAJI4NOGbH4Jn1U4kjy90HweRPRbjYg_lZGHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ثبت رسمی افزایش سرمایه بانک پارسیان به ۵۰ هزار میلیارد تومان
براین اساس، سرمایه ثبتی بانک از ۳۱ همت به ۵۰ همت افزایش و شاخص کفایت سرمایه بانک به رقم ۷.۲ ارتقا یافته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/461962" target="_blank">📅 10:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461961">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h65vnLP-L7CakynTv6TfjLqnU0aLatlgQPPYnoJ_Iiqfz1bzPfKI7TN__uwAuezbpVVnjSooINRSh0GVJQoRKjsim-EaSjYiXL5C8d0nXj2RPX5OZwvrv7OakP8ApOkMh_w-5xl6Nidzy00_6_ujX-bLJcjBZ3cfvCaPXq5WejaNDZq8MkkAlAicWisCoxLU8eUkuACeHyAH35p3tFfGYxLbkv9tFDd69v_a-oDJ1aOe74J6E8VxjYF1f6NtB3hNx4H2ETJcvjBekG47i4Rk3tVE7g7o84qxov85SyroIDap4OJ34-1Hne2d7-fINU77D5YoJWBKff-XOYc5FMofgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
مهر تأیید اهالی بهارستان بر عملکرد بانک کشاورزی
🔹
بیش از ۱۰۰ نماینده مجلس بر نقش کلیدی بانک کشاورزی در امنیت غذایی کشور تأکید کردند
🔻
اهالی بهارستان طی یکسال گذشته با تأیید عملکرد بانک کشاورزی، تقویت این بانک را بخشی از سیاست کلان حمایت از تولید ملی و صیانت از امنیت غذایی دانستند؛ سیاستی که تحقق آن نیازمند افزایش منابع مالی، رفع موانع ساختاری و همکاری منسجم دولت، مجلس و سایر نهادهای مسئول است.
🔻
بیش از ۱۰۰ نماینده مجلس، با تأکید بر ضرورت افزایش سرمایه، تقویت منابع و رفع ناترازی بانک کشاورزی، این بانک را بازوی تخصصی تأمین مالی بخش کشاورزی، دام و طیور، صنایع غذایی و زنجیره‌های مرتبط با تولید می‌دانند.
🔗
مشروح خبر
🔸
🔸
🔸
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/461961" target="_blank">📅 10:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461960">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/461960" target="_blank">📅 10:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461957">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6512c993a4.mp4?token=ATd1kRpZRxSRTbSsHcGeh1mjTEjguPT60Y0oTMyrbautkPrHkZSFwqBLt2C8aEX3kBn_ppKl_mzrVribTrGfNge6HYFFSGergk1qYuhiaWVm_rIqPi4QDnugJCp7u9M0Un0fZ3B2A6lEn32aQTBYOMPkqdWbTW4TMig2vM2Itv_62hXDlstx6hOmdc_sbpX1PsmaQupABp7dPE6ZEa54stiHcK38yw1WBwhTAb_z_pUuypXVBVEHXTEgJQD_aCgDt-8OCXSr0etHyVZhksVP-E0szS1raMRJinJS9zo_BgGSlTKO37G5GqOKv9FVIQC7wD9We1wPAmVOhABbxHVpHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6512c993a4.mp4?token=ATd1kRpZRxSRTbSsHcGeh1mjTEjguPT60Y0oTMyrbautkPrHkZSFwqBLt2C8aEX3kBn_ppKl_mzrVribTrGfNge6HYFFSGergk1qYuhiaWVm_rIqPi4QDnugJCp7u9M0Un0fZ3B2A6lEn32aQTBYOMPkqdWbTW4TMig2vM2Itv_62hXDlstx6hOmdc_sbpX1PsmaQupABp7dPE6ZEa54stiHcK38yw1WBwhTAb_z_pUuypXVBVEHXTEgJQD_aCgDt-8OCXSr0etHyVZhksVP-E0szS1raMRJinJS9zo_BgGSlTKO37G5GqOKv9FVIQC7wD9We1wPAmVOhABbxHVpHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پدافند ایران قفل F35 را شکست؛ هواپیمای آمریکایی مجبور به فرار شد
🔹
آمریکا پدافند ایران را هدف گرفت؛ اما با واکنشی غافلگیرکننده روبه‌رو شد.
🔹
تنها چند ساعت پس از حملۀ آمریکا به رادارها و سامانه‌های پدافندی، یک پهپاد ام‌کیو-۹ ریپر سرنگون شد و یک اف-۳۵ نیز پس از قفل تسلیحاتی، مأموریت خود را نیمه‌کاره رها کرد.
🔹
پرسش بزرگ برای آمریکا؛ چگونه شبکه‌ای که تنها چند ساعت پیش هدف حمله قرار گرفته بود، توانست یکی از پیشرفته‌ترین جنگنده‌های این کشور را رهگیری و از ادامه مأموریت بازدارد؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/461957" target="_blank">📅 10:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461955">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjoRk3QzrhG_sPs8vllltx6N-4VqAbUjJtN3UyDuZqHxs9UfYNBom-pQfe1-ihSpRKUh3bDNh3Di84Dk068phayVbVpNR8uLgzMxrjzfdf4mz9L88e-JOGnUL7-M-ne9S4YE0g9qKmjdTi10ntbv7Qad--8odl6sZBn1zPZkw9iWWptXrLo8yqdr5TWDW05HlKEk3oSGUK-9PXFfJG-LAr6ID0ISxrDYtAbDHZckoggvIQBwiQpFFJObhOR75IEtWYg6BzyutMiCkRfIN6fDOJQzorR2igtE2-t4RZCvIOiBrSyF6SINWdjuD4_r32i2v7MuCvSc0gn8SREZ6Ns4CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
فرصت طلایی ورود به دنیای رسانه با ثبت‌نام در دانشکده خبرگزاری فارس
اگر رویای فعالیت حرفه‌ای در رسانه را دارید، اینجا شروع قدرتمند شماست.
✨
چرا دانشکده رسانه فارس؟
✔️
آموزش تخصصی با برترین اساتید رسانه‌ای کشور
✔️
کار عملی از ترم اول در تحریریه و باشگاه خبرنگاران توانا
✔️
رشته‌های جذاب: خبرنگاری، عکاسی خبری، سینما و تدوین، گویندگی، روابط عمومی
✔️
کاهش هزینه های تحصیل با کار وتولید محتوای حرفه‌ای در باشگاه توانا!  (مهارت و درآمد)
✔️
پشتیبانی از اشتغال و همکاری با رسانه‌های معتبر مانند خبرگزاری فارس
📌
شرایط ثبت‌نام:
🔹
ارسال عدد ۱۴ به ۵۰۰۰۱۰۱۴
🔗
یا ثبت‌نام از طریق سایت
futurix.ir/go/rxDxXO
🔹
پذیرش پس از مصاحبه و استعدادسنجی.
🔹
ظرفیت محدود است.
مرکز آموزش علمی کاربردی خبرگزاری فارس</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/461955" target="_blank">📅 09:45 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461950">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7eecd9a2c.mp4?token=iMgESKwkoVHLHwHwxCHVAWPJHKYwwnHVpz3ZMwKx-xYFD9zCCLPPC9IZ5S6zy45UDs8DSWXz2VImnPtQ-3pe2ZpWT1GjACw9Ec9erNNIMfCWtLyvkqABjz_e3vttpV3PGj7d5bJd0BWkbYa-dRtqsT1LYeYLL8DVp02osNfeK-4JNoA8VQOK1AxJ0ry4KwU4o9-W7C_4j5oyc6bLZhGQTkpjJweuLaj_7IvehpF1iEaY1TVGeWm79uE0C40DULOIC44CvHs7DLH16e2ZAtkg9p7sDNe63X2cK6bA2C7Ox0bn1SCKetPvpr_D_0Fw55DSO_7d71IogiWtxX2p4hKpAiSEGkx8aJaByohxPoo4yEsSrcwUA46lC-8xx3r0vUBs63Ptgs6EsYjisxzxl3IwFU64cXjZq_nYQtQVCkIcZBFrp9maW4wc6d5QDBhTPpCxr426elyCmebuae4CSwW2wQ_nhK0wq7A2lAD7GoPPzsXCsX4QZO7oyCuE04uGYS_fetuvr8FuHuUvuqXtEwfqZwe4WOvZdsGOyYMGylJ9qEsQEHn0mWlj2ZOk8ziSvKALLDPxG6e_wR5-V_GM-mppaWln6T9mbPd_zvzH9FMjRwMG8UJUgDlvVo6excBcl1d5kXy_MFOcBnjPqyVGTO3SFyZVVWq_4rI-nM6u746OUjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7eecd9a2c.mp4?token=iMgESKwkoVHLHwHwxCHVAWPJHKYwwnHVpz3ZMwKx-xYFD9zCCLPPC9IZ5S6zy45UDs8DSWXz2VImnPtQ-3pe2ZpWT1GjACw9Ec9erNNIMfCWtLyvkqABjz_e3vttpV3PGj7d5bJd0BWkbYa-dRtqsT1LYeYLL8DVp02osNfeK-4JNoA8VQOK1AxJ0ry4KwU4o9-W7C_4j5oyc6bLZhGQTkpjJweuLaj_7IvehpF1iEaY1TVGeWm79uE0C40DULOIC44CvHs7DLH16e2ZAtkg9p7sDNe63X2cK6bA2C7Ox0bn1SCKetPvpr_D_0Fw55DSO_7d71IogiWtxX2p4hKpAiSEGkx8aJaByohxPoo4yEsSrcwUA46lC-8xx3r0vUBs63Ptgs6EsYjisxzxl3IwFU64cXjZq_nYQtQVCkIcZBFrp9maW4wc6d5QDBhTPpCxr426elyCmebuae4CSwW2wQ_nhK0wq7A2lAD7GoPPzsXCsX4QZO7oyCuE04uGYS_fetuvr8FuHuUvuqXtEwfqZwe4WOvZdsGOyYMGylJ9qEsQEHn0mWlj2ZOk8ziSvKALLDPxG6e_wR5-V_GM-mppaWln6T9mbPd_zvzH9FMjRwMG8UJUgDlvVo6excBcl1d5kXy_MFOcBnjPqyVGTO3SFyZVVWq_4rI-nM6u746OUjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر ماهواره‌ای از خسارت‌های واردشده به عربستان در پی حملات ارتش یمن
🔹
تصاویر ماهواره‌ای جدید منتشرشده از خسارات گسترده به چندین تأسیسات نفتی و نظامی عربستان در پی حملات ارتش یمن حکایت دارد.
🔹
براساس این تصاویر، ایستگاه پمپاژ خط لوله انتقال نفت شرق-غرب عربستان به‌شدت آسیب دیده و آثار گسترده آتش‌سوزی در بخش‌های مختلف این مجموعه قابل مشاهده است.
🔹
تصاویر مربوط به دیروز همچنین دو لکهٔ سوختگی احتمالی را در یک محوطهٔ نظامی در شهر «شروره» در جنوب عربستان نشان می‌دهد؛ منطقه‌ای که به گزارش پایگاه تحلیل تصاویر ماهواره‌ای «سور اطلس»، برای استقرار نفربرهای زرهی و خودروهای نظامی استفاده می‌شود. در فرودگاه شروره نیز آثار اصابت احتمالی به یک انبار مشاهده شده است.
🔹
همچنین تصاویر ماهواره‌ای سنتینل-۲، انهدام کامل دست‌کم ۶ مخزن ذخیره سوخت و آسیب‌دیدن چند مخزن دیگر را نشان می‌دهد.
🔹
تصاویر ماهواره‌ای از پایگاه هوایی ملک فهد در طائف هم از آسیب‌دیدن یک آشیانه هواپیما حکایت دارد.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/461950" target="_blank">📅 09:44 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461949">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e53cc7089d.mp4?token=UVpo-jbmPurzPtyXfd6gXAkOgQNOaAHGcQwmMSfR2ZtXX_enxa2IH-hZL8m0Yo9oFBNx9I3l7tPaCOPyxGPAMtlNN_Jn2ESR6yYk1GdHmEGrm9qfEQzjvGlIUC-ib9Lg6r23Bwx_9040RoZKegUkKdIAiVFDO4ifqkMgjxgESvVPXq-ZTpWT0GmhzSt2O87UolMy0DFvlsNMyAhnGSfrvKfSJwUPOrw3VA6NsGjlG7PIBzzabzLvt5U2SLG2mlb_tm57OGFUOodX22bPKyDpoG3M686HVtawUNbozD6omB3jdKr8CEgWlI321x62S8f8ZM3KIfS7h41bccGI4IQV0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e53cc7089d.mp4?token=UVpo-jbmPurzPtyXfd6gXAkOgQNOaAHGcQwmMSfR2ZtXX_enxa2IH-hZL8m0Yo9oFBNx9I3l7tPaCOPyxGPAMtlNN_Jn2ESR6yYk1GdHmEGrm9qfEQzjvGlIUC-ib9Lg6r23Bwx_9040RoZKegUkKdIAiVFDO4ifqkMgjxgESvVPXq-ZTpWT0GmhzSt2O87UolMy0DFvlsNMyAhnGSfrvKfSJwUPOrw3VA6NsGjlG7PIBzzabzLvt5U2SLG2mlb_tm57OGFUOodX22bPKyDpoG3M686HVtawUNbozD6omB3jdKr8CEgWlI321x62S8f8ZM3KIfS7h41bccGI4IQV0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ مرزهای عراق باز شدند
🔹
براساس اعلام نهاد اطلاع‌رسانی امنیتی عراق، تردد مسافران و تجارت در مرزهای الشیب(چذابه)، شلمچه و مندلی(سومار) از ساعت ۶ امروز از سر گرفته شده است.
🔸
عراق به‌دلیل آنچه «ساماندهی اداری و امنیتی» توصیف شده بود، این مرزها را از روز جمعه…</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/farsna/461949" target="_blank">📅 09:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461948">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLXbvX1z-Dyn3k5MS_LXcVhxksj5_muSq5Klm3EdD1OAcQkMK1tpl5EwxhTUgv1CS2dOIt36_0hO9mbBB0FHLR2vHp_QrjmhNXKl18rkOnYjOEPPGKj8TXa-7RTjUNwRhnAdUPl-WnltUFpbkqybu2rmGrAIU5IehSzQs_hgiL8GxSiAlcONvIhiCK_xQPQ8S2WBQg2iBAjF8Td8VjbS9aH9SSxCVKlOZNV5vyfFJVR2jIGheKapiwoULntLuQTGV9bnCekNYewXwlmrfkMeTMMkvwRVgS0JmekWQGNYfmZizjANtDJ1UZxIpeYZFgpp0LbEN4ZeJ5mepGvc-NKSGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انهدام یک فروند پهپاد پیشرفتۀ MQ۱
🔹
روابط عمومی سپاه: لحظاتی قبل یک فروند پهپاد پیشرفته MQ۱ توسط سامانۀ نوین پدافند پیشرفته هوافضای سپاه و تحت کنترل شبکه یکپارچه پدافند هوایی کشور بر فراز آسمان تنگه هرمز رهگیری و منهدم شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/461948" target="_blank">📅 09:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461947">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‌ چراغ سبز سعودی‌ها به افزایش سهمیۀ حج ایران
🔹
معاون سازمان حج‌وزیارت: برای افزایش سهمیۀ حجاج ایرانی در سال ۱۴۰۶ با سعودی‌ها مذاکره کرده‌ایم که چراغ سبز نشان دادند.
🔸
ایران در حج گذشته سهمیه ۸۵ هزار نفری داشت، اما به‌دلیل جنگ رمضان و مشکلات انتقال ارز، حدود…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/461947" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461946">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🎥
ویدیویی دیگر از انفجار در ارتفاعات علی‌الطاهر لبنان
🔸
شبکۀ ۱۲ رژیم صهیونیستی: بیش از ۱۱۰۰ تُن مواد منفجره برای انفجار تونل‌های ارتفاعات «علی‌الطاهر» استفاده شده است. @Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/461946" target="_blank">📅 08:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461939">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KPNW-WDhfwrgAitcutS-dfbCteBTi3nFDSckyidwfx-pUBTHTUkgb93EYMxOUZbTnD0tkttAZilNkdbRHkRVFvRdOvwIAbAO56bw3wfiXeQVydDV9QMSGXCLSL0AN2vTcPYlIGreQkEJ5MVUWJM9fUYwAcGzEJsJC95mQ67U0ceG1xwMqIMCtr2eYNCAZCUIEoAmP_8nsgKJEo6vz74Y769J7UFocuG0Y84aBA_VUu8OSGUso1KUrRMB6NoVt_LqEAn1m3NQsk-_VeeC8JXm5oTeMKs7a3_N3WxV1S1rBBN7iEHwm0MH0JrX3vyuzPGl-OXotk8SYKc6ohJUVLstKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TnDHpqP_cxJd_Xxwr4rm7D5Vjn5zIzABDiA-dD_S_shBkdExZhT-_6h3OeAR9QjgZIAsc1N9_aG4Y6ALJJqQEErZ7G-Xv7lH85maKHwFvj3gqj9wslNOhB5fmU4W3lgpPZa6b8i5rOCGrSos3Dvjkq-svNA9z1wtnmeqaoybJnBODWt0slcHW1fj5Ee8Tb8Y1ZOlXTtCGdniYhc0w76EqljPniaRUYwsGR33MkGn1zsRSTxIvaj2T-9LTy5UYnjOZyxgSM7Cjfmh0v6iwf7ZXbO6tCiN2rcBTXR49-ykNojJvM7EHV526TEqibD9GxWntY_tEVuAcnX_WRDPbmi77Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GlcvRB5I5RRgQrb9KTCo22esLeb7TPBQhgjhpAPRx8iCVYKp68CG9ryl6pLlrbDpUMLAg4kjHj43bJeQDn-hJxpJVW2kLtimYqo7w-XR7sDLb4QsS7b7NEZulXZtL95byIBKysSMAp6j-SU2xlquHC-Ha2uGMXgMYwCoigwUNIeUMpJE0tUQTzpd6wKXuBjccRKdNSD8I1sSP7ZXazwTjO9cCbdLqdC1Gb_LndhaOkBITgu3l9Vkt3BPpurnsopU__wRasKWCc8V0Wgk0YBM5rJlrCa-_Ue_i1NTZf185SPzxN9EdHC1af_0DBObgyxXwcnG4C0G4YgOOQLc1T0pFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uy6jTxY90PA7dpvMaKv3CSJqYFgvvf1c8bRUhbUUksQTHoRFwaySTwdDHEXQ7Z-BYq8hj_lmG8YKatAxn-FWsy9fJv-8eCwIwhFiuP8H18_pzxEfn2nQ7JcskM_VfyQFnrDNeBt8HbELZTWM3_PXToG6MrVZAPj_89YMiKxWmvsryuhJE4faiZC0xLDZ7HwqbICDXCuvz3_mFEocqeLCypkAA6g1fWsieE_DpauMlB9Eh64NdypqFaJ6hSea3JOReT66bpqVbM2Id2YboiHgIrq2lAHrXdnXnFh8VSRcHTWWyP_LD6iyliz3dV1Xyk4sRfrVovXr-Wg9E_6jiFSFrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fa9c6cLxaRAZin1JqGTPf7KJ0auk0H0yr5J-v-hZfwuYGoPmIXqre4BZDrfgINgxRO5Br-5nd94ucsIKJEi5tujootP4VKOMKe0TOfs_Dhxb-WonT8yv8MTSjDIYBqc6WnRmvdmbnb019U9EKMu1ygYN9ib8QlZoDAIrhYQkdgBZxuR_6iLFUJU46y6ZmR6W4og-SXo9XzSWQ8PGWtbe7tpE8ZoVLBdlkuG1pVLwhqAIQvCDcclgsBUQm-ccItEn31gW9ktvXqYH_rrbQJW_swHmuyVqTL7mslG8kf9RtB6UjNOg53fmosalDH2qgXLjYghrFwoJWLWg_oTbYQOpZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hVB34Zn6yupmDRS69LCwDbjtf5DApV0E_im7014yE9XCs0tgpPAkSSqHnvAPG35-FEwjKIC-QWZPCB-ljVgiS6ZtD3-jnYA4m9fsI6FG0zHTheAbOnxO-unIt3RTnD1el0PoasIrLAPTqPFlC27GyCoaARuPW3ksiYOT6REXBKm5QQ4Zdv0YVDj7rnPWKkIAT5gu87EjqIH1U_QD746MasbPfFn-3s86XZ2ISLP7q3-fAQ7_Y7G0BkTGU2LxdcmalXwopy4XEEA1LTFyYHw2XUchmiCfPtRfLroMYrc_UmyJkR-0LpbVzaAcQEWQMoAndCN63sYlgiTcR9luF2hl6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ptkq4m1-4YLTygap5gP2ZoL4NP31BCojIENYlLFBdWo7Wh65SqBNMNiLjaOK4OXwT586a9SEx6kOGoYPJEPqIftR8aMb06lPzy8ravqiFlZnTr2H6MNtb9Edmf19mshzO1n4Qh4UGuFdsZ7-rI9ZveDO32ynZukIkW6R8Tx0Gh26T4qtW5ejQv2FBbgQjxAJTe_f0DkN266s6Y-URTRpo2PmpVl9S413gmezHNnmxCG_bjrAjjbPDsYWXAIcjANN0LDCZORxIIruPr5OfP17RsW6enJpoTT_kwSxqaeiZy-cWQTvvKJDTTGGEt0CHSe2O0p5AVdg0QjC3M_s2DrkVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جاذبه‌های تاریخی جلفا در منطقۀ ارس
🔹
کلیسای سنت‌استپانوس و کلیسای چوپان، آبشار آسیاب خرابه، رود ارس، پل تاریخی ضیاءالملک ، پل آهنی ارس، مزار شهدای ۱۳۲۰ مجموعه‌ای از جاذبه‌های طبیعی و تاریخی جلفا است.
عکس:
عطا داداشی
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/461939" target="_blank">📅 08:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461938">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">قوۀ قضائیه: توقیف ۲۴۰ مورد از اموال خائنان به وطن به نفع حقوق عامه و مردم
🔹
مرکز رسانۀ قوۀ قضائیه: در ماه‌های گذشته با دستور قضایی اموال تعداد زیادی از خائنین به وطن و مردم که از عناصر وابسته به رژیم صهیونیستی و کشورهای متخاصم هستند، در راستای حفظ حقوق عامه و اجرای قانون تشدید مجازات جاسوسی و همکاری با رژیم صهیونسیتی علیه امنیت و منافع ملی به نفع مردم شناسایی و توقیف شده است.
🔹
این افراد در همکاری با دولت‌های متخاصم موجبات ایجاد خسارات گسترده‌ای به زیرساخت‌ها و مکان‌های عمومی نظیر مدارس، دانشگاه‌ها، مراکز تحقیقاتی، مراکز صنعتی و... را فراهم کرده‌اند.
🔹
قوۀ قضاییه با جدیت به پروندۀ وطن‌فروشان، خائنین و افرادی که به کشور آسیب رسانده‌اند، رسیدگی کرده و طبق گفتۀ سخنگوی قوۀقضاییه در این خصوص پرونده‌های متعددی تشکیل شده و در برخی پرونده‌ها کیفرخواست صادر شده، حکم صادر شده و پرونده‌ها به نتیجه رسیده است. اموالی نیز توقیف شده، تضمین‌هایی اخذ شده و اقدامات دیگری نیز صورت گرفته است.
🔹
به گفتۀ سخنگوی عدلیه برخی پرونده‌ها همچنان در حال رسیدگی هستند و پرونده‌های جدیدی نیز در این زمینه تشکیل می‌شود؛ این اموال متعلق به ملت ایران است و قوۀقضاییه پیگیری خواهد کرد تا این اموال در جهت جبران خسارت بزه‌دیدگان مورد استفاده قرار گیرد.
🔹
بر همین اساس با اقدامات قضایی تا کنون ۱۴۳ مورد از اموال و املاک خائنان به وطن که اقدامات تبلیغی یا عملی علیه کشور وبه نفع دولت‌های متخاصم داشته‌اند در تهران توقیف شده است.
🔹
همچنین ده‌ها مورد از توقیف اموال وطن‌فروشان و مسدودسازی حساب‌های بانکی در کل کشور صورت گرفته که در مجموع با اقدامات قضایی ۲۴۰ مورد از اموال وطن فروشان و خائنین به کشور با دستور قضایی توقیف شده است.
🔹
در بخش دیگری از این اقدامات، ۱۸۲ حساب بانکی متعلق به این افراد در بانک‌های کشور مسدود شده است. همچنین بیش از ۲ هزار استعلام نیز از بانک مرکزی در رابطه حساب‌های متهمان گرفته شده است که در حال پیگیری است.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/461938" target="_blank">📅 08:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461937">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a27685e8.mp4?token=oPPgXgGSsg8Wx1g6r7LnFroJuUfu3lFrXYRdmF1LAKkqVaUUoL2UUHi2w3S6bz3z2-WWTw7PCmMFXHnUetX3UE_JrBW5N8NET7ibBCZUykOsi8puTSVD4OGqv-IMEVUkx6Zh647hctmu6riHwLogkbCPe1D16pN0ilsr8aVdwq13FYqZKN-1bzGMIXeLy4B6HHOFgvwkElXCRcbvIHjZhmuCxyMZmy6nDWeUADEmQre5fnNWeVTtOsv36BHixt2COOhYkAzaJKsyhK-A0C5DQN64eE2Ii9oE-lRRQ-ZrrsnDOdi3dffgB_VEbmdeTlXHL2tnUNNMePA0k-mns1DDpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a27685e8.mp4?token=oPPgXgGSsg8Wx1g6r7LnFroJuUfu3lFrXYRdmF1LAKkqVaUUoL2UUHi2w3S6bz3z2-WWTw7PCmMFXHnUetX3UE_JrBW5N8NET7ibBCZUykOsi8puTSVD4OGqv-IMEVUkx6Zh647hctmu6riHwLogkbCPe1D16pN0ilsr8aVdwq13FYqZKN-1bzGMIXeLy4B6HHOFgvwkElXCRcbvIHjZhmuCxyMZmy6nDWeUADEmQre5fnNWeVTtOsv36BHixt2COOhYkAzaJKsyhK-A0C5DQN64eE2Ii9oE-lRRQ-ZrrsnDOdi3dffgB_VEbmdeTlXHL2tnUNNMePA0k-mns1DDpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ چشم به نفت ایران دوخت؛ «مثل ونزوئلا»!
🔹
رئیس‌جمهور آمریکا در طرح توهمات جدید خود، صراحتاً از تلاش واشنگتن برای تصرف نفت ایران پس از پایان جنگ، آن‌هم به همان شیوه‌ای که در ونزوئلا عمل کرده، سخن گفت.
🔹
ترامپ در جریان سفر به ایرلند و هنگام حضور در مسابقات گلف آزاد ایرلند، در پاسخ به پرسشی درباره اینکه آیا آمریکا پس از جنگ ایران را ترک خواهد کرد، گفت واشنگتن در نهایت ایران را ترک می‌کند، مگر اینکه تصمیم بگیرد در این کشور بماند و «مثل ونزوئلا نفت را نگه دارد».
🔸
اظهارات ترامپ در شرایطی مطرح شده که ادامۀ جنگ با ایران، بازارهای انرژی را با اختلال مواجه کرده است. قیمت نفت از ۱۰۰ دلار در هر بشکه عبور کرده و قیمت گازوئیل در آمریکا نیز به رکورد بیش از ۶.۲۰ دلار در هر گالن رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/461937" target="_blank">📅 07:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461936">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5zRfJ7pG9UlFTK-1plAwW0HlSI-WSJGZ9x5LovCQ-tpQhjtT3l_6GhguRPYeT1D0X2BagBujpX019mrnMHuDBP1HrA40ecPtpi0gWo4wASrl21z0I7xHxhAhoRBush9shvHxyPCrpSX0fxrr2g7Dh-eVAkC1x49CMMmQRPEUQJBI4E1jNhf70kSmVX21Qo3Uoog8pYEtdBqJXcFi1WRIQmUgKeP6_ks-H1aebiJULr-k3P0RThUfLStVRepSono7VC6r9iw3nfMCpiCR6RlLaAfk_o2axXoEOHAIlAJRZ8I8b6A9d4i9Fyn7E5LdX-Wv65Y4uJAfxQvbxG-AGkm0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازنشستگان تأمین اجتماعی چشم‌انتظار معوقات اردیبهشت
🔹
با پایان پرداخت معوقات فروردین‌ماه، حالا مطالبۀ اصلی میلیون‌ها بازنشسته، تعیین‌تکلیف و پرداخت معوقات اردیبهشت است؛ موضوعی که در پویش‌های «فارس من» نیز بازتاب داشته است.
🔸
بازنشستگان خواستار اعلام زمان دقیق واریز و پرداخت مابه‌التفاوت افزایش حقوق و متناسب‌سازی هستند.
🔹
معوقات فروردین پس از چندبار تغییر زمان‌بندی، از ۹ شهریور پرداخت شد و تأمین اجتماعی از تکمیل واریز برای حدود ۵ میلیون و ۳۰۰ هزار نفر خبر داد.
🔹
حالا سؤال بازنشستگان روشن است: معوقات اردیبهشت چه زمانی پرداخت می‌شود؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/461936" target="_blank">📅 07:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461935">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">هوای «قابل‌قبول» در پایتخت
🔸
شاخص امروز کیفیت هوای پایتخت روی عدد ۸۸، و در وضعیت قابل‌قبول قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/461935" target="_blank">📅 07:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461934">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-text">🎥
معنای اصلی مومن چیست و چقدر به آن نزدیک هستیم؟
🎙
آیت‌الله جوادی آملی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/461934" target="_blank">📅 06:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461933">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16b19dfeff.mp4?token=bZjGpFhisj44-u40Kf6OsPK4Y_JYZwC7X8SaXFgHd7imNaeLnCPT50LEljmEruVR9KYj0ZxdI9FiGVdMzH_ZuJji7PQQiywL-gWT1pa8w5RKNRf17k0uzfxppAAVUhBq3UiuvV_j3ZHseJkN_SCg-BvzBuzqtJOLJPmk5xHxwPEMA7ItsRkW5uV2wCwQLrev9ESp880oRJfL6bwm_K3e9VgW1JYnOcsf3UTIRoPF3H5MZAxhDYTvNMvW9UhYxP53h7im6xg2YZoJIgm4rc9zy2m-arnyYUvt0XU70VEzP9B4Y_r0Vmd0d-DdlVsES6K1wwauGu_yiLU8rKD3uuAurw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16b19dfeff.mp4?token=bZjGpFhisj44-u40Kf6OsPK4Y_JYZwC7X8SaXFgHd7imNaeLnCPT50LEljmEruVR9KYj0ZxdI9FiGVdMzH_ZuJji7PQQiywL-gWT1pa8w5RKNRf17k0uzfxppAAVUhBq3UiuvV_j3ZHseJkN_SCg-BvzBuzqtJOLJPmk5xHxwPEMA7ItsRkW5uV2wCwQLrev9ESp880oRJfL6bwm_K3e9VgW1JYnOcsf3UTIRoPF3H5MZAxhDYTvNMvW9UhYxP53h7im6xg2YZoJIgm4rc9zy2m-arnyYUvt0XU70VEzP9B4Y_r0Vmd0d-DdlVsES6K1wwauGu_yiLU8rKD3uuAurw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارهای پیاپی در مقرهای گروه‌های تجزیه‌طلب کُرد در شمال عراق
🔹
شبکه المیادین به نقل از خبرنگار خود در عراق گزارش داد که صدای انفجار در مناطق حلبچه، شهرزور و زرگویزه در جنوب سلیمانیه در اقلیم کردستان عراق شنیده شده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/461933" target="_blank">📅 04:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461932">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">منابع عراقی از وقوع حمله به مقر تجزیه‌طلبان تروریست در سلیمانیۀ عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/461932" target="_blank">📅 04:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461931">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpGTnqspprJci0bAO2Zl9I0Xvdgmsdw6vOyK13nmYXudldTBmQJdvb_zjJFazzvy5BV2F33wK-z7m8L32XcbvBAmENzOEA5XcDPa-4TeQ33WcNiFE5eNyI4yl_uyDrUnPTsf2LYqLMK3QAWY-gmJRQ1RyoVuen2iz3yiuQIZDjhupupOEtCTV2hh-SDydh2suv0UT1QwsDLKsZRBIp8eyrrXzNGe5hQpUCEPiJETiyCX6ktOX3XuY_aHKNd_YXgek-JwThETrGoLBXwrdcpJ9nUfBAaqPl4Gxnayh10GgEgz5fILHYCfwASoC2OrWIuDQ1cauqNnPIzkZOKi_xzhIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزمایش کروز و بالستیک، پاسخ کرۀشمالی به رزمایش آمریکا در منطقه
🔹
خبرگزاری رسمی کرۀشمالی از رزمایش ارتش این کشور با استفاده از موشکهای کروز و بالستیک یک روز بعد از پایان رزمایش مشترک آمریکا با ژاپن و کره جنوبی خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/461931" target="_blank">📅 04:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461930">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">دفاع مدنی عربستان سعودی برای خمیس مشیط، نجران، جزان و ابها هشدارهای اولیۀ خطر صادر کرد.   @Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/461930" target="_blank">📅 03:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461929">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gK4w2zBKlW__FRRio_t5QTShsx-eTwXkP8c278I6iFUxfsWSkgRzLc6NwuyZoiA6RgW_YbsGgvFFXa3n43lU1S2-xwtF6rtZVmev8zvk9FCKllIndah2__nSuIkxRnozeinyjaDS9AF3qHrRDhrhiWZsE1BAVfDmXZo7sfy82D-Gd3dpbKzBegqZ_p0nSH8AfoJSICC_sVvOL-Q9MAupfAkobGCPUcygi9Q9pyOMvpULIAlDGBPm3mIUDkBS4blfngra869PmrPFd6ijAjlXwVafM0q3GM83HgMDpMXBj2FXfKvXT_d-azDaZKcynadxd9tWZYDXt0UpY-XFfxhAbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیل غیبت رضا جباری روی نیمکت پرسپولیس
🔹
رضا جباری، مربی تیم فوتبال پرسپولیس، که با حضور مهدی تارتار به کادرفنی این تیم اضافه شد، با وجود انجام ۶ بازی در لیگ برتر هنوز موفق به نشستن روی نیمکت سرخپوشان نشده و مسابقات پرسپولیس را از روی سکوها تماشا می‌کند.
🔹
موضوعی که تبدیل به یکی از نکات قابل‌توجه در مورد کادر فنی جدید سرخپوشان شده است.
🔹
شنیده می‌شود تارتار در همان ابتدای حضورش در پرسپولیس تأکید داشته که ترکیب کادر فنی و مسئولیت اعضای آن بر اساس برنامه‌ریزی خودش تعیین شود و حضور یا عدم حضور مربیان روی نیمکت نیز در چارچوب تصمیمات فنی او انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/461929" target="_blank">📅 03:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461928">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">دفاع مدنی عربستان سعودی برای خمیس مشیط، نجران، جزان و ابها هشدارهای اولیۀ خطر صادر کرد.
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/461928" target="_blank">📅 03:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461927">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">رویترز: قیمت معاملات آتی نفت خام برنت در پی حملات جدید به کشتی‌ها در تنگۀ هرمز، ۳ دلار افزایش یافت و به ۱۰۷ دلار رسید.
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/461927" target="_blank">📅 02:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461926">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkkFgO3JSGjlXzrpGHdLggUStLwUQLoXf1z_TQvhQ-wv6wIwqnynNhYbVZutlCNQ7YieK4MrR8BRNJU_FMp2OyjW8GqQUQ5l0FxTVlyOo2n3ZCEy4APWutQlBiLtmMLHQHUt3McIkX5QlsHOe1rGm-fiJFdtNhosmqIMohpbhxyQyKhe2WoWQNSc7rWJ_1mMswy2bisa3vKv-ff6t4x4jXnlRRUrbk8Tp_iAznNifjEQcZOQoFR_-9v9-5t-ViHlajt59OoZ4OMIr0e9SUntnj2JCzWcFwNQUsoJZC1Au6mHz2F5nKH7ndbk2LDgf5FcjNdQ3DpL3Eyoj601F0pLWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ ینبع عربستان متروکه شد
🔹
بارگیری نفت از پایانۀ ینبع عربستان واقع در دریای سرخ صفر شد.
🔹
خط لولۀ ینبع یکی از خطوط دورزن تنگۀ هرمز است که مهم‌ترین سهم در عبور نفت حین جنگ ایران و آمریکا را برعهده داشت.
🔸
روز گذشته انصارالله یمن به خط لولۀ تغذیۀ پایانۀ ینبع…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/461926" target="_blank">📅 02:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461925">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4UWzHsl0Q8rZoRFLrt0K9FTAjFOmq1fw06WaYxZvI8satW_gZ1Yiu9Td4YaBxyjoF4kxVYTTsUrmNcou4N8Ieh5ddtkEuPzRPXHRAadtI-VxA4w0EUx1Qdy7xogy6sRoksv0ninLP0ctJ9JXUGmmJ4HQO1IBRl9blTx3luBU8WvEVPLvHtNWa-3e03RACQ5cQ47JShCRjwN6YPwzx7t1c_FJtOkQkjpm6sWPpNHHw9suqNCSNbZSiFAmAX4bQcL6ez2qdAaFjphAf_N6UT8VXIeS86nh2Wp3uCdbO7U8qaL9HNozSI1OZVmwC8URyMue0ZQOKEyHNPR8SLoMcyC2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خودروی آبی‌خاکیِ شکارچی پهپاد
🔹
چین نمونه‌ای از خودروی آبی‌خاکی تیپ ۱۹ را به یک سلاح لیزری، حسگرهای جدید و توپ خودکار مجهز کرده است.
🔹
تصاویر منتشرشده نشان می‌دهند لیزر احتمالاً برای شناسایی و مقابله با پهپادهای کوچک در خط مقدم طراحی شده است.
🔹
این خودرو در صورت حفظ قابلیت آبی‌خاکی خود، می‌تواند هنگام عملیات ساحلی همراه نیروهای مکانیزه حرکت کرده و از آنها در برابر حملات پهپادی محافظت کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/461925" target="_blank">📅 01:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461920">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HG7QEON4UX7Mnb92Ac9i4CGQn5Bs4DIS6JhS6NV657FHM6BlraZy23Cq2FfBsLOF-02KLoXWdG2PWX5GPXXegleC8l5Z6k1a0xB6TI6zRqquZWpEJuJ7aJRlPPotLdhljJhw87j2H8Qg6gGU0jh4KFiOb3FwHS8ZkjITNQn5W-StrOrMnQnyIoOudiwE0lG_xRzkiBbQ2mOugbJHKaYsQ8q1OXc9wewmXuNcdyfUECzrY9Aqgv6rSSIFohFK20j3jDTqF6aSgqxtsb0kN9Wu2lAot_WObYbiJO-3NmrF1VOafNWJAdAwG4Nfsj3Qk_eMjVhK2wKdVY1SSlg7aWSHNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LEuCrKkQempUmZcLpm0HmBnrQf1YTB1Q6jLcCPXK3U0pwzdXpwivC0-1C0e-J1_UhkZpLkUBmNeCL04sRrJY50r7WzvyWVm_eaUxuzPF-jLtkimy3eiYPxth2HrWGJzWVjz1DbRPZkfnYnt_ycxo7m2h94tQEA7qR_-_2jcPq52_Ro-d59FoEQCCXgGXkrqL8lH1k92hZlh8o8JrV3W5S0VveoJYeY2mPPByW4Bqb-AtsCj9eGCycdgMu3pbBsfi3mn5c8Y7LqoRIymadIHG3mqiiU8XomYCvEhCGv9NZt1i0UPHlAamuur5DTPM71s5Q2aTnGh8TuIYi2gi6O34sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pXBjoCHwskTUXkv1rJhcy1xt8-IkqaDz6LSxmrAQTiU1t7W5IOx3c8w2U1hbiR6JV9UnZ6_7mImt6O5xPUga5akW9gJ90YU260hlm8oxcL7RZhZ2EMPS4yKpQ4U_cWHReXaaWuLW3282JO3wfKvvOYPdrz8AMLB5DFmP_UtUiL1PKsAjAWv7efiKUdNT_hE5VHlddWZ6-jQTJ4XcgHMv9XT_E2T8lQTz2aR_hfDXKpt_2c8NGn0AhYLclIZYYQ01quVINWRJ832K4IQfCJmoeU0XBEa-vjdqIAOUDzOi4biCrkmedANMgvVy5pJ0D1JEc7dC3xvRVPw4IuhnZK5YYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hywOQ-A8w-tgGpRBkw9s1LwRoXoAGqhaE-sr_IC4Ay0yZMBs7XthGlYv8ePbclstqXnuzsRpYcMSd-bHpyNVN9rHCrwWawI7QIU9eWt5NqujUDZVuqoMZICfZDNxeU76X0m3rN5CTb_wDo8PxYo_3hk0ByaUjBeoqn6vwa2ij93pQtcd1JDlPcCo9hNnuItOlHfh5GfPF9gc-P5tv9iC_jbbXQDHzBUkjl5FtIWYEUfnM-d181QC5_x1BzlbfQZ3_eUWj4bipOn0jPQYujrE1AyH6_Gp6ZMgny7pfQ1qC8CmgVPbydqJY4XX6zOmTPwcyVImmZUhsaiqblwO9AtE3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E-nvzSEQZmrFCL4dKfKZ-ks6NGZgO2ZBPqPybPg20keF_Si4Y8nge6BUq_SZPSKEp1c-TyruuKv1M_De_z8Vayzm_OTB4_2xSOz0CnpGqZ_u-8AsS8QFByK0mRdcrBUpxAPV9gy6-8tzCqaQE5EOUHHazw4_nTIltpp4oDGWu0Z_3yyfu_bmgMDruhnfJJO63PmrFYeSscOxsNN5Ic5O7LOWLmpTM96YVDoftRVwuVslb6vdd9mXriNbEIVE8aGZsVueoJsTqS8N_FPiLy_8v4S5iNRwCIoHWxC3VQsQ7nt5EesvmwC_mYBpDxJXgO56Fxb8beeu2VVw9VMaTTPOyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | دوشنبه ۲۳ شهریور ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/461920" target="_blank">📅 01:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461910">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ujxrbbNRcNDyaj9mD2-ZDOJ6qrFI0FdXsOZIfqoCDU5m2tO-oP6JTyvDRmZeSWJiyRgV5Hll_5YJkcsitbYyDjgVlj5BMzQTRO98jyeOh8Z6ygWfxH0Q3dtF9Lz72OjnoRyeJuVKDSK6t-Brx-UrvaL4bFzyhjiXsA2JuCKo5Y8gXCB-Z_jucomO0i8NGY3a0CzTBhIv1myX7U216FzwS4rgTuyi2PNMGmDu1-oiDhC2a_FIsui9gXmb5ONV16U1ThVn1ihzESlwAfGeho_M8i1UoVeEFEn3nc2kwF9_jdo5MXMK9jnJt0VA3p3Af8nH_MzOvbGLafOXcdwpqsjWdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/setDM3IIa55JGVvXLOfVLh-YNKwg5CZp_UCdlL0I7Pn7R4ZjxG2pDsSh05aP3rC_mGR7eDgz59Y4M7E0Mr8bAARfg57EHurT1hy8DPZDkuXDJLOC3HRa3hJkkmPz32mS-BxQUYI9cVohikvXyOjDpUfyvGwpfEbkdJOoKTjSqn9Lqv1Q9a9pmwT1Lv_hm7iEh5Pay8nnTrrNfBbQO0riy7TcSrf6l2t9wLQkuFPgMBcNcJ6vbDHMDhuB8UVFNJ96xrRHaRDY3oS5fpXL6BrvKekaj2JduU5Dj5o2TCL3xvm49hdVyGNRXjskGGoa7HrOhiVShG3P1FI74nmS5KuyJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XCNJh5w1e43gV9WK-lCMcZWjQsheF-7amA8b9hG4vWUyTUEAEkQHwvHj87b7jybEb_On1v0VeNKeSQ4dgM8mLy7UjyXsklgvX6lLWRM0-tovmhOKagcD32QNM1xoiJ57nctGWn9ONqdk4sgvTr6Wi9WjuOXF930dnuyMhQnz_yhaZpuSIhR5wpJwNs2xQxbVf-qN0JTcjHKwiGxc8abDqirTMZPwDdbWcv2SPJA7kQfZtp6xD9d3b2g56Irre5ZwokZCvws_VNzeeXceRcJK9k-JfVVuf0cfZTUgoqVSr3ZrfP0eFy5cL0dsuecc-rwV0gj7XvPCBmxcgLoW3bITeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eV0evw1plHVKeKoPtGDYN_7XfxoxgvkseB8rleNN2IBF8NZwnjR6ldC11ZiH5x7lrPVRyEAq7Ym_6nE-YE8yUdeUDFgLY_D_fUnu_-DuBZHoyGJAAXhF8ywct5xZxT1TKJ_jJT9uUXIPLAAr51Zd6bYNZ1NtdecsING9xB_Fc-puFs4ovIgFk2p6UG0_0a3LKaP4-8xivr6SZlGx-YlWg8OKiytCaf7YbCWwt4bf4jRjVf_nNXUGGrSs_kNIG-jjM51NaBW_HisDPcGvMrsGccRnWqBog_MtMmgsgLDpQCzJCpfmRW-Df-piYIQSMV7tfszDf81S4cHt6NOGk75G8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VeZbUlG18M9IoSwehpTvcJBbn1kO7-Stz7f8G89_UE1BBTaGDW6oWJlCj0t-jKZz3sY8ANGOafTipDnhEDX_Boe9RPLGTlRcpkhstj8OScs9zoytxVOtPFHOuXrI9kP_KyjBnhFf-sNlqGUQh41I_kXNcfK0kwZyBhT8Jtx5_JLzuQmMI29-6Rb8B5vNwTijovouOp1FdwKJ9ibRXVQlcBad6K_KjcY5TYia4Z641vxWmn34E8Tl-FIDtVr8Q2hpMBRJQSh988M-GcxLL5Dxi4JUcNjP12_2eyouJ_6c9i5FI4tw0RwIxUPltNuCU6QqkUzkJD5p26SWitAkyTdW4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RaejtZm9uBQTOQcmp-4jPcp4k0onvwP-Kzzbv13xLze-fN9_WPFA6KQEYymoQVjfMYJNbR4AvcXq9PyABdScA5LAEQ5cTMkWSyRUZpaspmrva66h0w1dWGGEXhvph2Pb4pUtXxQ_Yl0MN4v_8mk0SsQt8jmZNu_1iqqrYp-ixG_XJdRfnTLFdndzRbabzysg_EGr1BKJx91CE-MbDrUB_V3UHss2UxqieXelNQAXSeJN-2SNQxWES6AncUSKayO8vBkDHFNNMOm5VeG9btqs2660evgCimVSlWWKWl6OyKk2nUu3_-KvqS_IMgIbl-CvaZBJQCbaXEkxH88osQGr6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WcI9tDI0XChP4cJhxVPDl6hdnXxL_Fv4h4wmEbJ5mxIAwk0W5xnc5Gf7Pn98-ilCH3E7sqGtoAZpkGsDTtZpw28umzAj54m5ohwT0m8CaW6xdPzWPgu5ZsX2mdgLPvfFFnCCV4nFxWBMU2U1iaSyBwooy3slJEHYfKgKuJc0SvST1PuFPF86fLaCEZmZmDbVhWqKUdbj8pSUiR2FP2VmG4pKJllC2uD6UdjmvjqgNDnDgJpKG3J1UQJ2q74zv-tsyI98neRKIzkT1_6EbOU_lTmgcU8DCVJOjXy1GM6Z7D6iwqocznJGbG0HTGd4KyoGQfNpvEQ-gTLpeaegh-TOVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hbtvDQ91v8i_GMmvtCnOloEX9OPoH6A0XFoWlZ2B-hcpGvqPG7NxB47lBf85OpDeWboYespeW-irR8qldtV3DfY4sMGrrHE0RB1xo0zy8bUzvTU0K-6Ky5HLzJigjyv_l3tGrrr3IjM-SDKe7QU-tAhwXcCN2XZoleVhQQjfbRn8qf-loNhcaSAA9c-3i0dGiVjgcj7ZN_QXnAYyHbm_G01qVKcpoLxkC596Q5h3WoH-e2vI0It9YZu1Y-C7E8TZBXyp-e3iVvg8Gce2iPfBYHR6MicH9FA1CzG9pEvJBfjUu3TIlvGS57UdoiLZVzStfsLCtR8rptlPXGincxRtHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AAYNZovxdLcOo0XSyOEe02nShXxncSdQuBIIwAHxIcY0HEIoza67e40Ju5pHK2YqJvKu6VGij0_TJK5kBHWXIErKWr9k95uAOuBmtpjfpfaoNGB5MhvACnkD4KIruK6uNnI8wzdyU-xRuavQjUumjG-Vg8vbaxvh5LJINjpa7McqP6oUIFr0Y5MdKfHG2rlpcctC3TiBcOtmhyndj6VcYUKhjeuMRgT0pfFcCAMLKjexQKx2Ty4UkanzsZFxHF1TrorVYAGHDVChz1NAUNmEdyjOqedR4NhFtA5EWtopB0riZImqJs9dxxTobAkuPhL1OaNHEAGK2awp082vgdH1zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cpadd2IFNN7xLlLylblQKdAk5o4YQe-cIniZHL2nR3dEtIgpgVFvknOk7TLGeEPePOKIjCWoRssUdnYqLFxSS84KA5v7FjIlYLMduQbewx3IcUpm1EyW4v_TdsB4y8ExmN94yjYk01y0UiTC1HzYlR9DyI8k2n2kTlZBLnEHE-85n66y84SNFTfxMrSfCG3b3-yHMdAlt_oBiOwH0gjvAp_v7IQohBOpzXSvwpponymdZy4WnpeZel3R47v8qWmg4fd6kNxdDhjNrMV0YyaLgU2z69vUS493x09MYju7eekiZeLyI50r4EddePgA6FNV3OM_mNH_IizmOR-L6gxtkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/461910" target="_blank">📅 01:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461909">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SvDjCZFYKPhmqjF18RrHX4A6qFJeLEA0wRpiocDzF_qxLEIjIbWFFucA_HNiv97esqJDioUHX5WSxc6q79CKz2TzPsnIHiWtEunHiNxsqlgdEKDvb_HKXVpKJe8zu4clA51CUX5SYkXDuJCkJT6bQUsRNJC1ohQtj5aT8pa9e9eT_v7GqlDIB_CPQW_BxNIIa98CXW6ewWyax8vjNZ6I9CSxSy9JBZyvjTUMeM7vtsg-gseHCRWvD1lie1QCb88rmxpReJN8wxoLQys984kCZf7zo7ggbsiBKgnB2suD22Uslse6v0vnQ1lURnhpPOhOBTo6MDs0xeaahd-eeYCMmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشارکت کانادا در وام ۹۰ میلیاردی به اوکراین از لج ترامپ
🔹
کانادا در حال مذاکره با اتحادیۀ اروپا برای مشارکت در وام ۹۰ میلیارد یورویی این اتحادیه به اوکراین است؛ اقدامی که در چارچوب تلاش‌های نخست‌وزیر کانادا، برای تقویت روابط با اروپا و کاهش وابستگی به آمریکا انجام می‌شود.
🔹
مارک کارنی، نخست‌وزیر کانادا قرار است هفتۀ جاری نیز در راستای تلاش‌های خود برای کاهش وابستگی به آمریکا با رهبران اروپایی دیدار کند.
🔹
این تحولات در حالی رخ می‌دهد که روابط کانادا و آمریکا، به‌ویژه در حوزۀ تجارت، با تنش روبه‌رو شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/461909" target="_blank">📅 01:13 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461908">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjgViBfdcrnCGJF37R0lVXbVtz2WwtpnSBnn5DD5KMxBUHGSWf8W1nHJamn_86ny1eGXgzUTD9tHFmuSV_VjKuueoXEOoPWizcgrbS6BTMSkYv15bOHzYXOK-bPj1cFDTXUx6N5YK1cDFQtN30W4735dddxVWmM-eX7_syR-bPxh3LD2Vfj3pPTH8U13t5BrmnfWmrHe8gNdSRZ84gtj_wIx9ZoRODbI8OzVUweMe3J9hEiP3BW0qw3fNwuBYQ9trCp93_6sN6sbpwTvcwd82Rppz1OiRHHxFVVjwV_ZmiOikamoiW-L6Kn5NeIe-ZIzs4MvwwQLoHpJqgu0a3oZuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
۱۲ خبر خوب از ایران
🔸
از شکستن انحصار خارجی‌ها در نیروگاه‌های برق‌آبی به‌دست متخصصان کشورمان، تا بازگشت ۵۴ هزار دانش‌آموز بازمانده از تحصیل به چرخۀ آموزش @Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/461908" target="_blank">📅 00:58 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461907">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">وزیر آموزش‌وپرورش: مدارس دولتی حق دریافت پول از مردم را ندارند
🔹
هیچ مدرسۀ دولتی حق ندارد از مردم پول دریافت کند و برای ساماندهی این موضوع، اساسنامۀ جدیدی برای ادارۀ مدارس تدوین و در شورای‌عالی آموزش‌وپرورش تصویب شده است. @Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/461907" target="_blank">📅 00:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461906">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e5fa97ae.mp4?token=NS4fcZ35JTLe1Nl9gdJgnVzu6RnPaa66VNNNCd0TipUaq02Kd-iVsPgh1FH7zOUYc29sX2lOVC4otsdqlf2NEf5TqIDpdnzg0m1-ku9lUAxcQYLD4L0zfchBdIP8HrqWZ5xl5NF3pXTXqr4EpJhn_8zFXL5dPkGMv-e0P9_kFW21OErvb5zV1qCbkTN2pKkOaupvq5nThRiYud8UVlp81-q2Y3mXrt-d1xuDzJv5YRQxL-bDDIk6bK8YWI5xIvojZ9p0xK5R9V4fBFtggoXf3LC0bX-1xJfn_i1DPp4scNmbLh5YJLTYPKh1UxbNmkQo1drujizWQtFCJ2ueXyffiYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e5fa97ae.mp4?token=NS4fcZ35JTLe1Nl9gdJgnVzu6RnPaa66VNNNCd0TipUaq02Kd-iVsPgh1FH7zOUYc29sX2lOVC4otsdqlf2NEf5TqIDpdnzg0m1-ku9lUAxcQYLD4L0zfchBdIP8HrqWZ5xl5NF3pXTXqr4EpJhn_8zFXL5dPkGMv-e0P9_kFW21OErvb5zV1qCbkTN2pKkOaupvq5nThRiYud8UVlp81-q2Y3mXrt-d1xuDzJv5YRQxL-bDDIk6bK8YWI5xIvojZ9p0xK5R9V4fBFtggoXf3LC0bX-1xJfn_i1DPp4scNmbLh5YJLTYPKh1UxbNmkQo1drujizWQtFCJ2ueXyffiYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی سپاه: ۱۱ جنگنده و بالگرد آمریکایی را روی زمین منهدم کردیم
🔹
سردار محبی: از ۱۷ تا ۳۱ تیر نیروهای مسلح ایران ۱۱ جنگنده و بالگرد آمریکایی را روی زمین و درحالی‌که در پایگاه‌های آمریکایی در منطقه مستقر بودند منهدم کردند.
🔹
همچنین ۱۷ پهپاد شناسایی و عملیاتی،…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/461906" target="_blank">📅 00:05 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461905">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0da22e4ebd.mp4?token=meaonIS-VAp4SnN6Bp7ZqTUdeXRvE2OLCbupwR8w2pTdQqo86QW7dZRbJIrDsLloNhop5brzcs0ZWUCThOZHHZjpxmYLDwSkVHs5GtEjJ8Qj-HR4AvbTiA1vlsHUvGo3UjkYdZC8cBqbKBNzXOld4Zqk9zmu3yMstmOIeVlz-VoTeZp1nHhMidR-5qpKSdlzwimUVE6V2nvLw0MBw5ePIvMtgZN3AkGSS3R-KAsdRO0TctkVz3E2cH0w6sSB-73NCk85pC67SpSVCuHHMqU9Pb2QmcoZQKD0HO8L_aCh0a5IB8PqLH8WygJjGPHHbdsDMIXvpWe8o-UlfoWE-QLOar6VIu0H3OnOlSt--2GSjImYHRsioGcIWQRR9NoHwWmQ8kXVgzTHEGKrvKxc1zzY1ZvxniLD0wjFWKSo0OIWFD0SJHcmIbjOSxmue1k5tUgrzubMcUWH7dm5XiGeOI5xzowhM6zoke8u-Eu0iRshaaYAgS_nRqw-tWN1eZkQGDEC_61JcQB9rqobl4zngupLrF3GUbtS_QgN438VGOvfUwjOiNYb-mDo2vUb716H08luU7R2xs73hktNDWB73okrDNkeL4JbXnEWImkzI07zGPefGG48pcH8o6ccG9_slWImWeEGzVGNDsUV8_jfidPXsAAFbfQ_mNUKOOYAK1DVad4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0da22e4ebd.mp4?token=meaonIS-VAp4SnN6Bp7ZqTUdeXRvE2OLCbupwR8w2pTdQqo86QW7dZRbJIrDsLloNhop5brzcs0ZWUCThOZHHZjpxmYLDwSkVHs5GtEjJ8Qj-HR4AvbTiA1vlsHUvGo3UjkYdZC8cBqbKBNzXOld4Zqk9zmu3yMstmOIeVlz-VoTeZp1nHhMidR-5qpKSdlzwimUVE6V2nvLw0MBw5ePIvMtgZN3AkGSS3R-KAsdRO0TctkVz3E2cH0w6sSB-73NCk85pC67SpSVCuHHMqU9Pb2QmcoZQKD0HO8L_aCh0a5IB8PqLH8WygJjGPHHbdsDMIXvpWe8o-UlfoWE-QLOar6VIu0H3OnOlSt--2GSjImYHRsioGcIWQRR9NoHwWmQ8kXVgzTHEGKrvKxc1zzY1ZvxniLD0wjFWKSo0OIWFD0SJHcmIbjOSxmue1k5tUgrzubMcUWH7dm5XiGeOI5xzowhM6zoke8u-Eu0iRshaaYAgS_nRqw-tWN1eZkQGDEC_61JcQB9rqobl4zngupLrF3GUbtS_QgN438VGOvfUwjOiNYb-mDo2vUb716H08luU7R2xs73hktNDWB73okrDNkeL4JbXnEWImkzI07zGPefGG48pcH8o6ccG9_slWImWeEGzVGNDsUV8_jfidPXsAAFbfQ_mNUKOOYAK1DVad4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حماسه آفرینی مردم سرخس در شب ۱۹۷ حضور در میدان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/461905" target="_blank">📅 00:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461904">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c57jGqmYcjXV2jVYpZN_ESJn2EMOduzo_Ts2wMazVvLEHvZsCQ_fBe0wk0wY8SbuTkvOHC2aBxHP9wb4jbaEy_7KI7KiAB83FUT1IH5oNq-qyTLsjZmlYiKhzx3mLeoH9kIA4iePlpgSht9E2azhSZcNzsvP-I4F_G2NpgW1h4DppxUT0JthbotEFYL7fS4RrMT3fWZ1DtTBI7Y_-BcFlTFOSSyxu0kYfB9fpXx9ttYE3vo25DB8q2pMuYCykCC6ZZqdv7Yj57qv2UDzpYvQwms33fcVRmW_2OgJt5DBoWP6wnqVPOhIdScGEk-UGMYNNLjJ7ut-biRw4FeamshJjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جایی که حتی ناگفته‌هایتان هم فاش می‌شوند
🔹
دیجیتال‌ترندز:  پژوهشگران هشدار داده‌اند که فعالیت کاربران در شبکه‌های اجتماعی می‌تواند اطلاعات حساس‌تری از آنچه تصور می‌شود آشکار کند.
🔹
پلتفرم‌ها و اشخاص ثالث می‌توانند با تحلیل رفتارهای ظاهراً معمولی کاربران، اطلاعاتی دربارهٔ دیدگاه سیاسی، گرایش مذهبی و عادت‌های خرید آنها به دست آورند. حتی اگر کاربر هیچ‌کدام از این اطلاعات را مستقیماً منتشر نکرده باشد.
🔹
هر تعامل در شبکه‌های اجتماعی می‌تواند بخشی از یک «ردپای دیجیتال» بزرگ‌تر باشد. موقعیت مکانی، فعالیت‌های آنلاین، ارتباط با دیگر کاربران و نوع محتوایی که فرد با آن تعامل دارد، در کنار یکدیگر می‌توانند تصویری گسترده از او ایجاد کنند.
🔹
این داده‌ها ممکن است توسط خود پلتفرم‌ها یا در برخی شرایط توسط اشخاص ثالث مورد جست‌وجو و تحلیل قرار گیرند.
🔹
برای نمونه، کاربر ممکن است هیچ‌گاه به‌طور مستقیم دربارهٔ گرایش سیاسی یا باور مذهبی خود صحبت نکند، اما مجموعه‌ای از رفتارهای عادی او می‌تواند سرنخ‌هایی در اختیار تحلیلگران قرار دهد.
🔹
در نهایت، پیام اصلی برای کاربران ساده است: پروفایل شبکهٔ اجتماعی شما ممکن است بسیار بیشتر از آنچه خودتان منتشر کرده‌اید دربارهٔ شما اطلاعات داشته باشد.
🔹
پسندیدن‌ها، تعاملات، موقعیت‌های مکانی و سایر رفتارهای ظاهراً بی‌اهمیت، زمانی که در کنار یکدیگر تحلیل شوند، می‌توانند تصویری دقیق‌تر از علایق و ویژگی‌های شخصی شما ایجاد کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/461904" target="_blank">📅 23:51 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461903">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeb50b917a.mp4?token=TdW6ZboygMGmfIu1arVoAUZKvmt19gzuUoUaOaSHUVsWnyaArOccCxmuXinWzwZC9JGRS0R0R2ndV7ioNLENWF9hfH_uFaCNY8G-8qFx6LU0cqxLq7RaGLN4rhly_2kjTFpewRYCpea7jRRZyibGWYTDn9gG8NTqGVwFA-zxJOKRlRZQmJe3EE35ODGjMnfkIxhfMd1BM6G5bW-7K8HQBBTRbSsom5BSHuMznOiDwjrrGf84Sxadjww351BX0LhGBfUtEmXWFViQRh47XK0UHbroWGc_AnU6IVsXW_5RM3-KhiyMZUgyH3l3g2yixRaU3V0ZtoDtNnriqjNB3gpOBaT4wgMgjcRKKU0xdG31ioUayJ5lNJhGziPnL5Vi4Lp9Q8i1LDgZ3KqcCzrLqK5Npsr1cDwE9uklvzD5TQTX6oqCx8MHbWNvN2qWo8ft5bCACp3UunMCQ0Tgn-WAkO2NwiGPXldKLnl6gw_cSLu-S_1SBwv608xhRjN0iYb00Lsgz2vABFtdRpWXpNvPtSZkFQGcqA3xM0u8X1RWE5KkFyCvbh-L_3X1m_cZc_7Tw_WNILWys5IGynpqQ03-imlU7YoObeMOubVLyOeVhJuU1ow7f7e7nKeDhwlVQDzVAiy391cRXDC8FoDw_DrIoHBJPVZKrjnxiCLh3Q6juaJsrXo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeb50b917a.mp4?token=TdW6ZboygMGmfIu1arVoAUZKvmt19gzuUoUaOaSHUVsWnyaArOccCxmuXinWzwZC9JGRS0R0R2ndV7ioNLENWF9hfH_uFaCNY8G-8qFx6LU0cqxLq7RaGLN4rhly_2kjTFpewRYCpea7jRRZyibGWYTDn9gG8NTqGVwFA-zxJOKRlRZQmJe3EE35ODGjMnfkIxhfMd1BM6G5bW-7K8HQBBTRbSsom5BSHuMznOiDwjrrGf84Sxadjww351BX0LhGBfUtEmXWFViQRh47XK0UHbroWGc_AnU6IVsXW_5RM3-KhiyMZUgyH3l3g2yixRaU3V0ZtoDtNnriqjNB3gpOBaT4wgMgjcRKKU0xdG31ioUayJ5lNJhGziPnL5Vi4Lp9Q8i1LDgZ3KqcCzrLqK5Npsr1cDwE9uklvzD5TQTX6oqCx8MHbWNvN2qWo8ft5bCACp3UunMCQ0Tgn-WAkO2NwiGPXldKLnl6gw_cSLu-S_1SBwv608xhRjN0iYb00Lsgz2vABFtdRpWXpNvPtSZkFQGcqA3xM0u8X1RWE5KkFyCvbh-L_3X1m_cZc_7Tw_WNILWys5IGynpqQ03-imlU7YoObeMOubVLyOeVhJuU1ow7f7e7nKeDhwlVQDzVAiy391cRXDC8FoDw_DrIoHBJPVZKrjnxiCLh3Q6juaJsrXo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای فرار معتادان از کمپ مشهد چه بود؟
🔹
مدیرکل بهزیستی خراسان رضوی: در یکی از کمپ های ترک اعتیاد در اطراف مشهد، ۷۰ معتاد متجاهر پس از درگیری با نگهبانان در زمان استراحت و هواخوری، از مرکز فرار کردند.
🔹
دستورات لازم برای مدیریت شرایط صادر شد و تا شب گذشته و با همکاری پلیس و مراجع قضایی، ۶ نفر از این افراد متواری، پیدا و به کمپ بازگردانده شدند.
🔹
کمپ‌های مادهٔ ۱۶ در اختیار ستاد مبارزه با مواد مخدر می‌باشد و بهزیستی، نقش نظارتی دارد. به همین منظور و پس از بازگرداندن نفرات یاد شده و تا پیدا شدن دیگر متواریان، کمپ مذکور تخلیه و مددجویان آن به نقطه‌ای امن برده شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/461903" target="_blank">📅 23:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461902">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d93bea865.mp4?token=REAfpitQh0tgsOU1RgzCvslB83Q5s5nYb9VlbKlee7HZRMUVVSXQW1TS9V-2G5bzA-1YRBPPYG6llLhfRQQHpQvjhoa7jOCFaf9-NyrIZZ3d4tp_m2vomyDBV48Pl6MoZZz0ORwCbZLEbk_rVcR8B4JBomstVK23IxqYlTCJ1ih1LFidXMdiKwyjfLcuXbKUZTU3vNQdDf255-tijpJh7V5LKOyVlQ71W2oUIUZeI9dxNdT-_PW0xeTcZSzxJDAV4IM-0IOrTub0L2ZSUYSyeDW1rV2oCLZYLlSUMbHOUBOsXaEAgHDOOGuq9vnBtv-jginBKqnnANMELk-2kZYpQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d93bea865.mp4?token=REAfpitQh0tgsOU1RgzCvslB83Q5s5nYb9VlbKlee7HZRMUVVSXQW1TS9V-2G5bzA-1YRBPPYG6llLhfRQQHpQvjhoa7jOCFaf9-NyrIZZ3d4tp_m2vomyDBV48Pl6MoZZz0ORwCbZLEbk_rVcR8B4JBomstVK23IxqYlTCJ1ih1LFidXMdiKwyjfLcuXbKUZTU3vNQdDf255-tijpJh7V5LKOyVlQ71W2oUIUZeI9dxNdT-_PW0xeTcZSzxJDAV4IM-0IOrTub0L2ZSUYSyeDW1rV2oCLZYLlSUMbHOUBOsXaEAgHDOOGuq9vnBtv-jginBKqnnANMELk-2kZYpQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از کشتی ایرانی که امروز در نزدیکی جزیرۀ هنگام مورد حمله قرار گرفت  @Farsna - Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/461902" target="_blank">📅 23:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461901">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bc2aaa2c3.mp4?token=rartuoRP5zRiPmkWu7-cX0kVytRIw_JsS5FB57wknmpBBdIXCONWrdCRNI43lWUn4PVtvpnd3fqdFZ6hPpcMhMMEthOCWyqGvFUC4t355dKkd-jsZjwKSeGVskO3VKOraKGFhsDG0mlyiUQB5p-fQlQ_Xqe7Rw1srGrOHKZzQGrNdOKm2g0MRHj9kXpvYSk4qWqARDayAnoj_WaSoFg0xMoSFrB0sqNZCAmicrdoB0Asd14ajgSUCUUSNQONk7lV5xiKrYZr9jk_rtkHcOKuDbCp10O_OOQh2RjCbEe9lXroMoeAMB_mFlDoxk8tsIU0AOOdGUKuyXqc0LC2yDn_fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bc2aaa2c3.mp4?token=rartuoRP5zRiPmkWu7-cX0kVytRIw_JsS5FB57wknmpBBdIXCONWrdCRNI43lWUn4PVtvpnd3fqdFZ6hPpcMhMMEthOCWyqGvFUC4t355dKkd-jsZjwKSeGVskO3VKOraKGFhsDG0mlyiUQB5p-fQlQ_Xqe7Rw1srGrOHKZzQGrNdOKm2g0MRHj9kXpvYSk4qWqARDayAnoj_WaSoFg0xMoSFrB0sqNZCAmicrdoB0Asd14ajgSUCUUSNQONk7lV5xiKrYZr9jk_rtkHcOKuDbCp10O_OOQh2RjCbEe9lXroMoeAMB_mFlDoxk8tsIU0AOOdGUKuyXqc0LC2yDn_fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع شبانهٔ مردم ولایتمدار شهرستان زرند به ایستگاه ۱۹۷ رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/461901" target="_blank">📅 23:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461899">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dae0abfabb.mp4?token=P8MkgI1_PMtEnOZBEFN6MKJ-rzJr7fOTqzouV1yy4txCIMRO1ArXER-Axazf_EaXqOP_36IfX_vTTzjHzjXkGTWVKZZ-jPrqdAgoBRB5b9pNOMgkWlWv1dvMi7q3AGTKGTJsLSBabH-AU8t7be8BGayk8Fjn9eibd9bfu8s141DR-x3pAKoJKNi7gbJkeNqSQTEQWnrDkyd9pFOEg3FYESMxrHBxn-XeAQcW9GOI17cplfTHuklvdPoq97a5zt5Y86mLSg-sZPauMsFwoFkB51YfJz_Xy6emPgKyU2RUs979y3O0e5jWkXidfcQ4gb4PvsMTtY1gjmxy3oWR9rtLeG4oobOQoLOaMSuZzF3OKCjlW13If0XDD6N71rkIv_c_ouP6Q1FH1eDR-oxWKmyP5Otsx84A--pQEyIHPe0ooUWZsFteMIbtTA86FtGqzFA5FcCwALGiqMR9Qfj84Pchn8jYmOhL_wGo1sfAw6uYwCn5iNGulS3Cwn-VK_hox661oWzv_Al0tNUMlxwtBozZR_MUii0GxyERJLA1NlEXcpuh5NWvLRxjVkOyllMhKMfWoRzje6xAGU8fMny58uF7qKk2PnMJUTJapqv7Z7T_MQKf4iAvxokisp-2UlgL5SenKVy6xIaz9qxfi5vSgCCft-WWdnXI2CDBQFv9W7N8kto" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dae0abfabb.mp4?token=P8MkgI1_PMtEnOZBEFN6MKJ-rzJr7fOTqzouV1yy4txCIMRO1ArXER-Axazf_EaXqOP_36IfX_vTTzjHzjXkGTWVKZZ-jPrqdAgoBRB5b9pNOMgkWlWv1dvMi7q3AGTKGTJsLSBabH-AU8t7be8BGayk8Fjn9eibd9bfu8s141DR-x3pAKoJKNi7gbJkeNqSQTEQWnrDkyd9pFOEg3FYESMxrHBxn-XeAQcW9GOI17cplfTHuklvdPoq97a5zt5Y86mLSg-sZPauMsFwoFkB51YfJz_Xy6emPgKyU2RUs979y3O0e5jWkXidfcQ4gb4PvsMTtY1gjmxy3oWR9rtLeG4oobOQoLOaMSuZzF3OKCjlW13If0XDD6N71rkIv_c_ouP6Q1FH1eDR-oxWKmyP5Otsx84A--pQEyIHPe0ooUWZsFteMIbtTA86FtGqzFA5FcCwALGiqMR9Qfj84Pchn8jYmOhL_wGo1sfAw6uYwCn5iNGulS3Cwn-VK_hox661oWzv_Al0tNUMlxwtBozZR_MUii0GxyERJLA1NlEXcpuh5NWvLRxjVkOyllMhKMfWoRzje6xAGU8fMny58uF7qKk2PnMJUTJapqv7Z7T_MQKf4iAvxokisp-2UlgL5SenKVy6xIaz9qxfi5vSgCCft-WWdnXI2CDBQFv9W7N8kto" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مینابی‌ها هر شب پای کار تجمعات خیابانی هستند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/461899" target="_blank">📅 23:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461898">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
نشست ایران با کشورهای عربی به تعویق افتاد
🔹
وزیر خارجهٔ عمان: نشست منطقه‌ای که قرار بود فردا در «صلاله» برگزار شود، به تعویق افتاد. @Farsna - Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/461898" target="_blank">📅 23:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461897">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5K9NAprLQL3kYpZTiwcPMlhkja7e4xjOGF7UfVADFN7tD8PZgBqi40EpW8-Cs-kk73Br15nojBPyyjIRR77JJJ-CcAsklEi-HrzxahSAQdYEEPCLwHgye2fuNcHaPgywJA34NjqBxOGL49Wk8y8H0WVxUOwuMN9pMJnXGuAGZnQpbV_hN2JdwQXtqgLwTXyU791b87BJ07v8FLqGhRxJI4uufiR9qOkDRvXAsQ-UitM3XpuHQyf6-Fu5uI7ptkpPFqNe-e9jmQTwu2kl1z_8Q6hAtaQkU1xMeJjO7dGqHYrzguDSyxQ2z1NSlLaFThgMxoMlOO01CEX6_PqKUPugA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نشست ایران با کشورهای عربی به تعویق افتاد
🔹
وزیر خارجهٔ عمان: نشست منطقه‌ای که قرار بود فردا در «صلاله» برگزار شود، به تعویق افتاد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/461897" target="_blank">📅 23:00 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-461896">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c1883a9c3.mp4?token=ELKNvlEBuJY5JIBxGfUgPLFHIfjCfm5vJSPNSY34enVvtYYi9YGggDDp9NksEIFcBuRISiZmjs-gXwl6wo4V3pq43n0xqIXg8jXJchHF9nBXGFxW9Ikt1qwkFWYQvu_tby-la7CZmk7h0kmzViegqiLWFP9KYWVfe-z4MngbIv_DnF_FazXRkWEY-YdZ7WqjOq9_E2FUk7TAjtfwTRxOG0I3EDSrMspGBr0hZhH9uC1tDouzfOytulWcIYTfvcdq-ON1WJXvZvdA-0aXr1q6jLL29cJ4RDzsk_VOzmMszqacFFkZzEcNLhbQW2lnheIBvWttC63AX5E7mrXKIbW2AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c1883a9c3.mp4?token=ELKNvlEBuJY5JIBxGfUgPLFHIfjCfm5vJSPNSY34enVvtYYi9YGggDDp9NksEIFcBuRISiZmjs-gXwl6wo4V3pq43n0xqIXg8jXJchHF9nBXGFxW9Ikt1qwkFWYQvu_tby-la7CZmk7h0kmzViegqiLWFP9KYWVfe-z4MngbIv_DnF_FazXRkWEY-YdZ7WqjOq9_E2FUk7TAjtfwTRxOG0I3EDSrMspGBr0hZhH9uC1tDouzfOytulWcIYTfvcdq-ON1WJXvZvdA-0aXr1q6jLL29cJ4RDzsk_VOzmMszqacFFkZzEcNLhbQW2lnheIBvWttC63AX5E7mrXKIbW2AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت صادق محصولی از تلاش سپاه برای ساخت موشک ضدناوشکن  @Farspolitics - link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/461896" target="_blank">📅 22:57 · 22 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
