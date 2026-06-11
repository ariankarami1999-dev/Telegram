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
<img src="https://cdn4.telesco.pe/file/dPqY9QQV9S6tjg_RMDBo9DPYTJrlqg3NYmoPyCE5hS9oQVslh8vk8g3_5JUa_N9b3D7FtlyQyQfQJQWsx1vpNPXGwRy-9C62-5VQMhplOaH53wgLj238jH7In7t1FjIuc8Sdjj_gMGGt-NNTjfCiLI6p6t9aLyjFjiaWGnv04jTAWUDHrKnyZtJ_qnwihftul86ReJ-xejRCCj_6yH1MaJBN8NIg4DRX4OvDoQHTTKPGdunrIcPHNzpKIqZo9v-B5v0q2oyvxwoNb8SCtOcbHP_u3ViRShh6VNqvq3qm4T-zVe5pgXXXKajEt9rZwiVfu7xLp13gyXfMp9wx18a6Cw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 195K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 15:23:01</div>
<hr>

<div class="tg-post" id="msg-23179">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aca2e774e3.mp4?token=fz-Eh-ww_O45P4TN6X8VwMJTgeEBAB5zODoiPH2vFezrNONOUbXfwUbiz9vzORIvjDNfmSjWVkauBLTPwnGav2dWO29ZWXHHiVNd4BL0yJOBFP7Qm22-o8DnBNAaeb1tTb-hSdKqBzX5Kz2o9ehuqBKMgXdyMN-VtlENdTatV6gc1sg1pGysLtVXLUl-a5SbfVh-xRJDdsG6M3CIL4rr6oafc51d-TYgEJzIoIcF6KLtm59L7x2HkfkPB93_eXp8SWAI8MebwXiaSJOtbL_d5WdwwoaVdFlwt3HPtiPitLXGUJBoW-c1Zrmu6ROYbp5EJHxJMLFnOWNTNe2jrK7vgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aca2e774e3.mp4?token=fz-Eh-ww_O45P4TN6X8VwMJTgeEBAB5zODoiPH2vFezrNONOUbXfwUbiz9vzORIvjDNfmSjWVkauBLTPwnGav2dWO29ZWXHHiVNd4BL0yJOBFP7Qm22-o8DnBNAaeb1tTb-hSdKqBzX5Kz2o9ehuqBKMgXdyMN-VtlENdTatV6gc1sg1pGysLtVXLUl-a5SbfVh-xRJDdsG6M3CIL4rr6oafc51d-TYgEJzIoIcF6KLtm59L7x2HkfkPB93_eXp8SWAI8MebwXiaSJOtbL_d5WdwwoaVdFlwt3HPtiPitLXGUJBoW-c1Zrmu6ROYbp5EJHxJMLFnOWNTNe2jrK7vgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
#تقویم
؛
خیلی‌جالب‌شد؛
دقیقا 16 سال پیش در چنین روزی؛ آفریقای‌جنوبی‌میزبان جام جهانی 2010 دربازی افتتاحیه به مصاف مکزیک رفت که با این گل دیدنی اون‌بازی رو برد.حالا بعداز 16 سال امشب این دوتیم دوباره افتتاحیه جام جهانی رو برگزار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/persiana_Soccer/23179" target="_blank">📅 14:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23178">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CqfiTeUz1FAvCwDJC86RfUC08lO9eG6H12aAI7hff0AALPXb2ICuz4yoxlVZ42xV-_9WXDbpjTm7tmZhWYtEVrn9_vREUv8b3v94Tu9TygSDeq_YkCSU3Iu_UwmjTiMwgJQMyq75Tk8xv_C_aTfKx3W5FQ2-Ha1WlffObU0rWVK0NRfQVsBPDzhIXfS11cQaWzbQTw2qCBxlDbpZBd6CsFIxB4hsj6cSyIWU3Z73hFl6fwteUgj6CIk62seM8i04h_R8zVDGOrIf-JfOmF8bWWi-Ii9Tbcf-LypZcRHuYU_9M6I5BLQQi2FPf51ulzLyA2f5MHZl7fjPXhBaa71ZDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ادعای‌‌سانتی‌اونا: باشگاه‌بارسلونا ساعتی قبل پیشنهادی 80 میلیون‌یورویی برای جذب یوشکو گواردیول برای باشگاه منچسترسیتی ارسال کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/23178" target="_blank">📅 14:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23177">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcQke7jTHwkRkNrkuefXrQsX5twN2zEld2vUHWMKz86pEXd50ZBCQMKKAU0GWATexojGCTWa7wCHr2U_QSguImSUpNvT9hRTUWTl5cnVh2MKkwJj2MN5sBZdkyJLpCrujQ9GnV9jfrL1MHjUqHQ-OB5OfxpwKifsJgGawDy8eShiGySJmX70DnLSFOj_ipWG0yxVm4VP_Ax8pOnXt_OTCDh_MR8NjAFpMTb33oCeoWQhk44oW7mo39WF1dR2xU51Z0w6CvEqTYPb6ZVMOICL53WOeiX5rWgwerIuVYaKbtf8JBwZ6-6xFbQ5jIY9ZF7vz7_-Ew817ZmMisGD9m_uZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق شنیده‌های پرشیانا از باشگاه استقلال؛ علی تاجرنیا برای تمدید قرارداد محمدحسین اسلامی بمدت 3فصل‌دیگر با ایجنت او به توافق کامل رسیده و این بازیکن 25 ساله به زودی با حضور در باشگاه استقلال قراردادش رو رسما تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/persiana_Soccer/23177" target="_blank">📅 14:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23176">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18448ed5c3.mp4?token=f9uEN4CJ-3FzBaCAQOHHOOg9LbWUuy_v5oTRt-ytL2ID8kEQVtfdT32oZ8oxKvdEnNWVhqI2M8U_vh1UQ7RzQOP6FpBznJ7g2ysAhHI537WRRFeE-Nu4RRcdxWSG44CLTPQ_xL6_sAmaolUec_z-9SacNHTPNGAUbu9fCyV9MOqwjHIH0pP-qrbBgrApWu-nOF5AWf6s-cmQGDzO2XPFYtzR3R9S6lA4LgG_K3_mTpkvb2c-DWLRRQx-g087E9OBI7xjHmDRNKa5YK-8I9IB-qqPeSwIF9GNG44tOfVxg90sFRghBB27K3cpDV1bI4odBAvhbZnm-WlO0qa7Ud26RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18448ed5c3.mp4?token=f9uEN4CJ-3FzBaCAQOHHOOg9LbWUuy_v5oTRt-ytL2ID8kEQVtfdT32oZ8oxKvdEnNWVhqI2M8U_vh1UQ7RzQOP6FpBznJ7g2ysAhHI537WRRFeE-Nu4RRcdxWSG44CLTPQ_xL6_sAmaolUec_z-9SacNHTPNGAUbu9fCyV9MOqwjHIH0pP-qrbBgrApWu-nOF5AWf6s-cmQGDzO2XPFYtzR3R9S6lA4LgG_K3_mTpkvb2c-DWLRRQx-g087E9OBI7xjHmDRNKa5YK-8I9IB-qqPeSwIF9GNG44tOfVxg90sFRghBB27K3cpDV1bI4odBAvhbZnm-WlO0qa7Ud26RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
5 تااز بهترین‌پاس‌‌گل‌های دیدنی در تاریخ رقابت های باشگاهی؛ کدومشون رو بیشتر دوس داشتی؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/persiana_Soccer/23176" target="_blank">📅 13:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23175">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XE3g_lzEGF1Sh2bcB-3XYxEgYUAJrSXrpIltYGHoT5YPJ6i9ptHR6PzMMFvHHnmpQW8mWdBFlfsfcstWPfDTVoJFlFMjnsy-W7xzJ2ecu2JXcvbLaLpI5TykrwdalhLpGg_yJCAFLgtRIsPUliSVb63AxPdRmZURhVSUpB_myVCdEPAbE2iNiH4VWlmi8TvPa8_izrIcyXNQqY-6vlDZ1IGeT-ra3PazV2DzlkMkJsnLTp3Dz_xe9UMig-MVX1BPBRqB-_qxpq_R7uSgTpPJt78iat1nd7nM5usT-Gu_if2QbzGviYn5_Il9kg2sgYqaZMR2G_d_dopgm05GG7ayvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
🔴
#اختصاصی_پرشیانا #فوری؛برای اولین بار اعلام میکنیم که اگه شرایط کشور برای فصل بعد مساعد شود نظمی گریپشی فوق‌ستاره‌البانبایی روبین کازان به لیگ‌برتر خواهد امد. هر سه باشگاه استقلال، پرسپولیس و تراکتور بدنبال‌جذب این بازیکن هستند. باایجنت ایرانی نزدیک به…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/persiana_Soccer/23175" target="_blank">📅 12:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23174">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jkb0JncBgrNahzIu09Ydxfqr78F_mBspsdHEt4Z1zwLv2l0CFS5pSrVhqy3R8dN24P9eT7G_zHreqgGbElQWD1WoEHQTDATk4jEKhiMh0US5fvTMPXOS8NiGTOtI1b9Q3hyVPsgR__R6zUo66HSrXasEI3AyuKMHEHXYymvoOw3DmQdwH6p6fNhzFFJiy1L_VrzbodyM2O3JesYBVwpVgPgTIgLK3X1VA-LQTgnNcSeGDqEqfljgMBAM-SwsOGCqy4Y2DXpR5ePKtbLXXZ8XdtOoVRsJ6-zNz1MQqID0iHr0bMaYNoW_K1xTYUvMxjVFPxQHiaDwM4KSHZcIRf-kbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
مارکو باکیچ هافبک سرخپوشان و نماینده‌اش این هفته‌حضوری بامدیریت‌باشگاه پرسپولیس جلسه خواهند داشت تا تکلیف نهایی ستاره مونته نگرویی برای‌فصل‌اینده رقابت های لیگ برتر مشخص شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/persiana_Soccer/23174" target="_blank">📅 12:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23173">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfZI7yAFfA5h3QvUgemAfcWC2zho4OgqD7dycJWNelk2idJksz-kYAih9jroxSiosXAtXVOr10mVoJlooI6JmSbUzCi7jQ8B10cuA-gyhVPNDAUfTMJXqVNizJ80UITQfSdS1rR_2WOC1_gn9iq-iTY6xw7zcmB89iQlP9AcV9C9iRkBm43Y1wwpWsvAezaSV9RjnYue0kNdNRAh8cLcM9BY_1XhoMl_rvi8jxCMq6ii2Cea_n17FmCquLrKU6lS6fDQrHDXxIncgLcf8q00pdiSD3JsXN7ms8g89hZ0-7Hu3Z3EuQYReOv70hrcsuF1JOwI_74cHC6f5mLyXoFIqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد فوق العاده شش ستاره فوتبال اروپا در فصلی که گذشت؛ جای ستاره‌گرجی در WC خالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/persiana_Soccer/23173" target="_blank">📅 12:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23172">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e4d302a86.mp4?token=sBrc5MQVxPk1nYcq4bPqsfTJFRfZCpPIjZA-io52tdnXOFdO9RjRFmw79csWjtVlZHQOacf75qy_eLo5eyMadGkS2L9QG7scvyIliSgMuB2aQffq4zHuTBuKDJ_2tkDPBRAZuIucJhgK2fUy8MTPRbetWRB5PFlR1oz2aqIM6GbjzLNOFRbvw8tdgypF2q6dj7D4Emb-zcMcTezFqlnKSpVK-k13tLQ81e6-IXANZhAszDPZqmxZI2UxB9SHKGAIc9YukPaVf8zuZN7pjzjeioUX9PP-Mwg53IqOC5ER10Pd7PuCBZcIOpPz0F7ZoG2V3uSwpPLUfgIuycHXfad5xIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e4d302a86.mp4?token=sBrc5MQVxPk1nYcq4bPqsfTJFRfZCpPIjZA-io52tdnXOFdO9RjRFmw79csWjtVlZHQOacf75qy_eLo5eyMadGkS2L9QG7scvyIliSgMuB2aQffq4zHuTBuKDJ_2tkDPBRAZuIucJhgK2fUy8MTPRbetWRB5PFlR1oz2aqIM6GbjzLNOFRbvw8tdgypF2q6dj7D4Emb-zcMcTezFqlnKSpVK-k13tLQ81e6-IXANZhAszDPZqmxZI2UxB9SHKGAIc9YukPaVf8zuZN7pjzjeioUX9PP-Mwg53IqOC5ER10Pd7PuCBZcIOpPz0F7ZoG2V3uSwpPLUfgIuycHXfad5xIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی‌ نوستالژی‌وخاطره‌انگیز از اوج هماهنگی فوق العاده لیونل مسی و اندرس اینیستا در بارسلونا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/persiana_Soccer/23172" target="_blank">📅 11:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23171">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-UIvMKrpR4C7K0pjz3DbhMiA1YadBFANHfzQYIYgVkxPAd03dHydFrP9UuRPRoCr6xj8pita8cGr4jPBtpwRrUwxZlu68M6tpROQtHz42tkMH51G8ctoia4tXIrItdj_MG08Ky-mTtB3mY_4P4VR9fNos31YPRhcBVgH4VbOUXcry627KM1eTQJSxKb8RrxMWU7IyXA8DIRHPYqC6OxrpJv7M8SLlvXzN2jcNFTIjjW-SIpmIp4-gx-KIbjZWcwf4nSoso7uYpX12MvU_dIcRsAbx5piLtJRWlteHp3Mi_QFjHdcrAHGLBncOMCJRVQlc12MpBKUOVjM-I7uTSpsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ باشگاه استقلال طی‌ساعات‌آینده مطالبات یاسر اسانی ستاره آلبانیایی آبی‌پوشان پایتخت رو پرداخت خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/persiana_Soccer/23171" target="_blank">📅 11:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23169">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cwZZgTN8KtLfZvNfwpYfh709f9-0XtxDf0S1s5Ma2yxwi9y2AoKjSi2XUZDyv0upAC0wXjNSFQfKqo_3uaLAD29JfAybyn_PnFYj0OwicrBZ1WQQv2w2jnKuprL6VZCGqhUx9XG5-xbjaiE_HDSKUnve7VstgxnzxJeP91p2m7DMKAeRPgkHXcOkMB9Vt6rHlK7j9g9TW094R76yMDlCFhGXHx8VJugXAqVogMVvMUj0tqpE95V4lFp_TyvQEivMf1CtWwUZibbQSW3Q6sC30Z7zkYf0WdP5kbN74xdHM_R2e4aqo6G3mHKGleuGmWMIB3bIYeyxBA4KnsnSujbAcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CZCCXE7u7K6ey3-SpetuBxfkLCp0DhM62NlYIs1LH3Tj2RPddRTqtkg2MieygBc_P4Nbmn7SxR-z64WF0qcv8Ah01dAqO6gI-ozZVfxZq8YkKejfVxo0M_wBG1t6spOV1nTmjLKxEiHJw_XZq8sX-fgUgFLTNbOXJmdo7gkplsCwoEh_BmHj4MtdlXboXJWWAp1JqdKIFadGOZwfHp4oPtZW14iW70Rnq95peqIFF-JHQhQMmai24IW_UBOkwwi4L5OesAfaPRiWrsHgmXX-ue4-_oPAnD55aUCDXf1X5hoMzq2vUPb_bT5h4IWYs68uekHYZd0SM5bdgPbU5lRe8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
یادآوری
؛شبکه‌های‌رایگان‌که‌قراره‌ رقابت‌های جام جهانی رو از امشب با کیفیت‌ بالا، با گزارش فارسی و جلو تر از صداوسیما پخش کنند.
📹
شبکه گرند اسپورت هم جدیدا برای جام جهانی افتتاح شده اون هم میتونید فرکانسش رو دستی رو رسیورتون سرچ کنید بالا بیارید.
‼️
خودمونم‌ازامشب‌لینک تموم بازی‌هارو سعی میکنیم پیدا کنیم بزاریم. اپ آپارات اسپرت هم که چندروزپیش تو کانال گذاشتیم دانلود کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/persiana_Soccer/23169" target="_blank">📅 11:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23168">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RURlI03MOKNnZNhB2MJVYRxVNMi4JIB75csk2mGUgnG74ECVP_fvoHoTvf734nLuiYnbbdUHuc8V5oN_bPj2vIAWiTyUhR6sxGGEGC7v2HLAgfz8CTervxFMV02rRcSEAAHupdpZwiLqiQs4lE7MvyPXLcbu13ijEvkArFbo0W4oSqDy7Nksz7jHz-bnr2m2uNxu9F4lLvXL3rbYAoi4_LAuoccIj5gRoMJqhXuFZmip65UFnDo_9cTE9bN_KMmqgqzjR0jlmDFUQzBh_ESsuv3ERYa9q6Iiesm6ICIQ3oDgHCoHwDtd1O2IuqnUacvvTI39thpskVEM2A5UUvXjSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛شهریار مغانلو مهاجم‌ملی‌پوش‌باشگاه اتحاد کلبا نیز از دو باشگاه تراکتور تبریز و پرسپولیس آفر هایی دریافت‌کرده و درپایان رقابت های جام جهانی پاسخ نهایی خود را به پیشنهادات خود خواهد داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/23168" target="_blank">📅 10:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23167">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22d9a8eaf2.mp4?token=VgCc_GXdzj-IjF7kLJx_RTced0-7kztpp6iUuvOZaco4xNjB0E99Z0zu9cld2O3z8yqNZHbaYKjcAc1KXdmpaJLG1VoCQJnu8iz0A4-uucX-jmdPFVXeq10XwryhvqXrYi7TfsSZ7UTpboBpr9i-r7kqdJwl_PF9_0zAfn3YmLbTp5DfsZBprDCAbh_Ll0czkqXtRt-iZuaT-GzJ0L5R6alax_IvSgZM57uUMx559tnoVGs7HRKfFtpcHMlmQpolV-_3d7z1uPstU85LVkhC0P6oYBpgOmCq5ALJZlotv2zRH2gajxSttoHOYiMS2C0WJrW250Es8LN3WcD0aPd-Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22d9a8eaf2.mp4?token=VgCc_GXdzj-IjF7kLJx_RTced0-7kztpp6iUuvOZaco4xNjB0E99Z0zu9cld2O3z8yqNZHbaYKjcAc1KXdmpaJLG1VoCQJnu8iz0A4-uucX-jmdPFVXeq10XwryhvqXrYi7TfsSZ7UTpboBpr9i-r7kqdJwl_PF9_0zAfn3YmLbTp5DfsZBprDCAbh_Ll0czkqXtRt-iZuaT-GzJ0L5R6alax_IvSgZM57uUMx559tnoVGs7HRKfFtpcHMlmQpolV-_3d7z1uPstU85LVkhC0P6oYBpgOmCq5ALJZlotv2zRH2gajxSttoHOYiMS2C0WJrW250Es8LN3WcD0aPd-Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ فیفا امروز صبح به فدراسیون‌ فوتبال اعلام کرده در بازی هفته سوم مقابل تیم ملی مصر؛ شاگردان قلعه نویی باید با بازوبند رنگین کمانی که نشونه حمایت‌از همجنسگراهاست‌واردزمین شوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/23167" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23166">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRpynZMVFmW316VFk9Kd1ZdpJQKR3_g6fd0y2Mby7o8ReyMXEHqSEUMNj0h-fzt8DdOSe3yn13B0FS9TPMcJGvmK6T4W2R94LRGD4C72IzNtVPTGuIZdABvyXf89T8DzsEReIWBaLBx5-ztHEgHKElQiHvLvIOTmdW7yWeJXNN13vpRXuAoGk2Bo3dCHPrUTfZHcfQzCZetAjYHhjUNNg05LIe0BFNWDHr9b3qZkU6xjWs3fsSjqe0Rgi1sSz2q9hUO-TRhLBjjuDGqiXhXY1Hic1tQ7CWJm8VWIlWvzNM8vFlJW7rVJ2wnMKuDMXK_PkXO7zVbyvzZKxbzaaygtKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ آغاز تورنمنت جام جهانی 2026 بادیدارافتتاحیه مکزیک و آفریقای جنوبی
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/23166" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23165">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyYFvDVEFUYq78Oa4wiCkVmSMkGW6P7kFCQZTF5Fi5VRDadhFTxPoUJEwhCR6AD9FrX3-71m5y96MgidnOWBhHcBkzR9cyvd3dYFvFGKM9tK4vaDcL60QhyU80LRtMmD1_WujzOrci-1VNZcXFxw9XAEczBb-iXYiZWrjBl5gngufZr6s9L5jdADtRbqOsFC7kHu-csaHnYarbx_Ud_IInYrUFQdk6WgZDg0bzQRwgQmoClL4AOkehG1GS6fJESH7yNK0RrlzSc9htiGNv1c1SubWxH5UxFRS5qp14Hmww027ihnLYP7Q24mji08Ey_Ij0tHiRvRhHqM--Gy-MWaNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕔
انتظارها به پایان رسید
📃
از سایت وینرو رونمایی شد. معتبرترین سایت ایرانی
🤩
🤩
🤩
🤩
بونوس اضافه به ازای اولین واریز
🔴
فرصت تکرارنشدنی به مناسبت افتتاحیه
🔴
⚡️
هر چقدر شارژ کنی، بیشتر هدیه می‌گیری
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
🎯
📺
تلویزیون لایو برای پوشش بازی ها
🛍
بالاترین ضرایب ممکن
و هزاران امکانات خاص دیگه
💰
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا er21
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/23165" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23164">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e065f47574.mp4?token=YqM7x0yONjxtyEfiOd7bQwxUtOR4gZ1cuQ9JiNQmq9k48jixPl7ExDKZAPknezrcHfBmtflTPHsTZRRdfh2WMLrKiJ5K59O3NUI4f9TSXHuXmBHjnLsh7nZlEZoHxmZRW5ZhJIQOr1aH8nr45qfKmq1SfPLjMZTDezPRTOFCF3lvDgfZq-o9Bu_vZ3cfIJgsC3h2C0Z260bXj8G8OLmb0_APwesayCXpL0G_7pniyvB4AXvFRwFwVW_xLxRkZPQnvEvlCPrZSZ8fb6vblOxEDR96gcRtdA4J1JbenIcdoj2gcwBq2pRZg1x9JgfXJ4JvXyqz4kjHrrlqr2bkYnfGKBt7-45pQc_jrqvGjzoHjgs_YZc_8Pq4gU6tjdy13NWDWChbUFKmIZGISIWR28Jp08GoyHtnTzDnBX-qrQF0gYhc2QA-FYc943y2Jy8xkoTU3K3uweSGFp-bBy3t510H4rqrAW43lsjo29QSDT_FBv65LeAfzxZ_IZbCHRbyB_f1qZOuw-fjuzjq74nR3qVMupMldp12YnEd_6NbLCXbGFUQuZjbvzrIkNvvIkehMybDx12k9apaMVDA9QJBPQOBqmntMMKIzjdrs1q2VUY6nD_VOU2KjVEs3k4lMBgXwpqVAdE0H6hYWrmca-xTnCw9zHueWBagGdrUho4vqg3gDJc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e065f47574.mp4?token=YqM7x0yONjxtyEfiOd7bQwxUtOR4gZ1cuQ9JiNQmq9k48jixPl7ExDKZAPknezrcHfBmtflTPHsTZRRdfh2WMLrKiJ5K59O3NUI4f9TSXHuXmBHjnLsh7nZlEZoHxmZRW5ZhJIQOr1aH8nr45qfKmq1SfPLjMZTDezPRTOFCF3lvDgfZq-o9Bu_vZ3cfIJgsC3h2C0Z260bXj8G8OLmb0_APwesayCXpL0G_7pniyvB4AXvFRwFwVW_xLxRkZPQnvEvlCPrZSZ8fb6vblOxEDR96gcRtdA4J1JbenIcdoj2gcwBq2pRZg1x9JgfXJ4JvXyqz4kjHrrlqr2bkYnfGKBt7-45pQc_jrqvGjzoHjgs_YZc_8Pq4gU6tjdy13NWDWChbUFKmIZGISIWR28Jp08GoyHtnTzDnBX-qrQF0gYhc2QA-FYc943y2Jy8xkoTU3K3uweSGFp-bBy3t510H4rqrAW43lsjo29QSDT_FBv65LeAfzxZ_IZbCHRbyB_f1qZOuw-fjuzjq74nR3qVMupMldp12YnEd_6NbLCXbGFUQuZjbvzrIkNvvIkehMybDx12k9apaMVDA9QJBPQOBqmntMMKIzjdrs1q2VUY6nD_VOU2KjVEs3k4lMBgXwpqVAdE0H6hYWrmca-xTnCw9zHueWBagGdrUho4vqg3gDJc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
مجموعه‌ای از بهترین آهنگ‌های ادوار جام‌ جهانی از سال 1998 تا 2022؛ کدومشو دوست داشتید؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/persiana_Soccer/23164" target="_blank">📅 09:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23163">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJEiBj2yF-RejoDEih52D4SFwnjPdAFEx7qbXMmuPQaqU1uFSYS3BVC7JH2TwcrfzlMSU1dUVAY8ui2BfI6MgBEJoMbygkWtxqn4hc0rW0336IAbMv2AEwsgOsHIt8VKguyky4Q-EFxbsRadlq267j0VLUS6G-m2FeJkWpNrGqQfOIGh1xyWeoRbl1XTAcDnZHSOv6RPsIhK-QY9CxKj2D4YpWeZ7XCXlFBDJPNhcV5-YgOxi5cMfg4bq1-Dhzbbdho6x0dT48g20IUgilCLR9RRzIlXOzcPo3imEWjmHDGxeS82S-lUD2IPtA_gutOsJyG8_DBGg7WDFfvJHt5mug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
مجریان ویژه برنامه مسابقات جام جهانی 2026 از شبکه معروف TRT SPOR؛ فرکانس شبکه رومیتونید ازماهواره ترکست پیدا کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/23163" target="_blank">📅 09:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23162">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VX_FykYT2c7ggN673H-mXYpF_Kq1kfWnA_9FmAkViWAJbhRP1r-ienkA3HZIyJtcYzqJhsq-_7KjMVRhQla2myLSDGwpDOASIAiNy7xDwi6OrKVhd91-qdUh2dnVGHvIAmp_s65PWYe19JJRXNmFU5FXFY3W6LFfBjz-9R-vHQVJVgeQHQFoS7m58xSfqXjS8xBCDyyGfefHw-TjoXnvWRw-3qAvJNnki3k_lRE3KysK0i9kbWV3iAoAMb5qAPe8B003VJlOLoAjGcTaGyqyoDb7bin1NCAPw-8oLYjKX5Se_3CZ6X0kqABmTy2GunjqX-_f1viodksDALEJXv2l6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عادی‌ترین‌مدل‌‌موهای‌بازیکنان‌وقتی قراره تو جام‌ جهانی بازی کنن؛ گل‌سرسبدشونم که برزیلیهاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/persiana_Soccer/23162" target="_blank">📅 09:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23161">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1bdb0ad97.mp4?token=WcigupZMUlvq7GUYh0bLfZiyUkj-mLEKhW5ljkFQRrV7ttuLXhqJbbeTFDt7_40Ttu3zZO5mu1lr2Fwi2O1viFZKxup3dP_Wi9Gp-SVMfaIz3oClNA6laxaIRTgT8tv6j7KRts90jJAa8pcLU96-1WgT_rdS3zDCBDFBCRyqbrmW-VP7kBS4ERGiWgRW9LMIaJ7UdMEBL7-9G0rMUeZEw7JtfJCn7-4zdaxqVWQ3q7rEEDXLfIl-El_GwppFL6zVSyP2zSIUGw7DqE0KvCIPVG35H9BL0YFu_045XTTdxWRxI25kt1f_DtCxELka8o64MayfDQnNADGoOdyPFOft9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1bdb0ad97.mp4?token=WcigupZMUlvq7GUYh0bLfZiyUkj-mLEKhW5ljkFQRrV7ttuLXhqJbbeTFDt7_40Ttu3zZO5mu1lr2Fwi2O1viFZKxup3dP_Wi9Gp-SVMfaIz3oClNA6laxaIRTgT8tv6j7KRts90jJAa8pcLU96-1WgT_rdS3zDCBDFBCRyqbrmW-VP7kBS4ERGiWgRW9LMIaJ7UdMEBL7-9G0rMUeZEw7JtfJCn7-4zdaxqVWQ3q7rEEDXLfIl-El_GwppFL6zVSyP2zSIUGw7DqE0KvCIPVG35H9BL0YFu_045XTTdxWRxI25kt1f_DtCxELka8o64MayfDQnNADGoOdyPFOft9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🇺🇾
جالبه بدونید
؛ مینا بونینو، مجری سرشناس آرژانتینی، تنهااز‌طریق‌چت‌اینستاگرام با فده والورده ستاره رئال مادرید در ارتباط بود و قصد صمیمی‌ تر شدن نداشت؛ اما شنیدن یک پیام صوتی از فده همه‌ چیز را تغییر داد و او در جا عاشق لحن والورده شد.
‼️
درادامه مینا دراقدامی‌جنون‌آمیز و ریسکی شغل موفقش درتلویزیون را رهاکرد و بایک بلیط یک‌طرفه راهی مادریدشد تابرای‌اولین بار او را از نزدیک ببیند؛ تصمیمی بزرگ که‌سرآغاز یکی از وفادارترین و پایدار ترین زوج‌های حال حاضر دنیای فوتبال شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/23161" target="_blank">📅 09:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23160">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea36e1943.mp4?token=Il_PLm0s4EeFfni-8W9-KGhIhddZzkJK-BhQ0E6D8GBaXepK4vmiiGnrlNhI9yn8_9987twmCTeA5VHedGcTjeGzzit1KNn6Lyba6-3ffG-RIifW0b6tzBA7ryXXXf6TxBQLhZbRDt47nJcqFu4u0SC3y2_SZmcky8s6sLs-LKrH99wkmm6fXSAc81Cq274nL8MQtNefbTxhVjfRN8Rxt9TcDX4U3y4gks7dV_Ovb3HYYmH0pa65CjVDrXJGaZcnZhr_lskYQs3HbB7mobXPv2JGuFcFhKQmfCDhFKiRtWPQ1m0zhiP6tS-4WLHOdG7jLvkRNWwGpd4K8YTL71lfYIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea36e1943.mp4?token=Il_PLm0s4EeFfni-8W9-KGhIhddZzkJK-BhQ0E6D8GBaXepK4vmiiGnrlNhI9yn8_9987twmCTeA5VHedGcTjeGzzit1KNn6Lyba6-3ffG-RIifW0b6tzBA7ryXXXf6TxBQLhZbRDt47nJcqFu4u0SC3y2_SZmcky8s6sLs-LKrH99wkmm6fXSAc81Cq274nL8MQtNefbTxhVjfRN8Rxt9TcDX4U3y4gks7dV_Ovb3HYYmH0pa65CjVDrXJGaZcnZhr_lskYQs3HbB7mobXPv2JGuFcFhKQmfCDhFKiRtWPQ1m0zhiP6tS-4WLHOdG7jLvkRNWwGpd4K8YTL71lfYIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاگردان‌جوان‌روبرتوپیاتزا درحالیکه ست اول رو مقابل تیم پرقدرت‌برزیل فوق العاده شروع کردند اما درنهایت 25 بر 21 این ست رو واگذار کردند. پیاتزا درتیم امسال پوست اندازی بسیار زیادی انجام داده و بازیکنان جوان زیادی رو به تیمش اورده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/23160" target="_blank">📅 07:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23159">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfa3df8180.mp4?token=TqB2oHR9AS-QUJproJsVwDB0r37pmCSQdGs9nLXm3HLo8zRGbAtgLyOQpd_SOO0IMLjW1d-a_-Uaki5fDi7W8qPsmPYcp2DD1BJQz67gm202qe80u0vaZGErRLtJouGTQiDGLUwR2Fz81u9zttfcZdheN_vnBu_YpWsyCyTY-Dw86Kal8fc3TAnhKWfwuQekr33EuCx4Fv8MIxI4B2Pbt4GeL6VHNE6aOpBFqAogtK_1Oi20f21TFtrtlO1G96VNEI293vELSUSpRv5y231LCUTWnCwtbAHuyVIKI5XvLyXqRYVGLt-9753CRtamz64q62MczQnjtwvUkVI1xfQJJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfa3df8180.mp4?token=TqB2oHR9AS-QUJproJsVwDB0r37pmCSQdGs9nLXm3HLo8zRGbAtgLyOQpd_SOO0IMLjW1d-a_-Uaki5fDi7W8qPsmPYcp2DD1BJQz67gm202qe80u0vaZGErRLtJouGTQiDGLUwR2Fz81u9zttfcZdheN_vnBu_YpWsyCyTY-Dw86Kal8fc3TAnhKWfwuQekr33EuCx4Fv8MIxI4B2Pbt4GeL6VHNE6aOpBFqAogtK_1Oi20f21TFtrtlO1G96VNEI293vELSUSpRv5y231LCUTWnCwtbAHuyVIKI5XvLyXqRYVGLt-9753CRtamz64q62MczQnjtwvUkVI1xfQJJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🏐
برنامه کامل مسابقات شاگردان روبرتو پیاتزا ایتالیایی در رقابت های لیگ ملت‌های والیبال 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/23159" target="_blank">📅 03:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23157">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1uhPTxIJPwTNXSTjWNLKv7M8XAcNKxMAzWwByMBmoXLq1uEqKC0s4i6AWodHNNfbhAYdyMRAAbUm3UHfUOLTHy7THvcIKJ6-tvgFr9kcvtIX_MGxlSNYRXVFnPdHg0exH7zwYRWT92RExvXRmjKDPswIdCXjCqknnLZ38zgvrjnhku8ksQeFuFJzIogixGSs12fnQLaFyD9ydwZ4bgjlEibdp_e7KPq4kFgNFJzvPYnMkfVx-oHyAIq1boqs9xli9lxBGW7WE7YI5psGRx5PKApkPpCfbyyWYv2tnfG18mTQ00XVtqyaBUvtBXIeUIkx_a7X6iSs67ij1cqS_K1Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
آغاز تورنمنت جام جهانی 2026 بادیدارافتتاحیه مکزیک و آفریقای جنوبی
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23157" target="_blank">📅 01:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23156">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cgu-0i0HwcHnShBGk8o0SgOSl-kzkdDDhQkhVErQqObqVPPQiqvqs9ROzX7IzTUPxPbJVEi9rwEVeHqlaaUS5UEMtpYMj4G0zL9n9JT0SCCHNIP4zHeSf4RvskpscCczACYdoLn-UQTDtNWeCpgEKsDDcs5PvrrDYEodEZAu0r2HGn_HI_NTs1PAl8CYCcIkSUcQ8EI1z6goQ3wXw-kZ9qkOSwPdMeX6AOfkHtgwCaRHE3rmmUyOhMCy8dwD6JKiKumxjHB2t3CBpJyWTfL9rcruB8HF5jraoN8uMIiEfhj3mydMq6RYxsRVDVi94NxK6uhsuVjP_mqoRL0eeZgYJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌دیروز؛
برتری‌آرژانتین‌وپرتغال برابر ایسلند و نیجریه‌پیش‌ازشروع‌جام‌؛ انگلیس هم تاپایان نیمه اول با تک گل رایس از کاستاریکا پیش افتاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23156" target="_blank">📅 01:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23155">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lR0wHBQs1TVcbVkXcYsZ2qx-NcU2fV7q-GGE6RsBwRiJhNzxgoMHUmzmaZvsGAVe4n_YXVCvMT15LI5yomckKYEmwY-PKGFXhZVJbQ9h_ZH14xbeawTvrqvb66vSys75rCJKGbR7Ju2NGmMw3wSBDWtt2ZXzr3HOYWu4z68ZdksKsrh-PyuxEl29OKV7iSxBQlnuvSesNU6-V4uq6paOFZGs29WnOCl6xNjMTuDHvx7CuQIDXVTwvJaLUEMmynmLuezmhb4R3BQi_iTY9QPzypLorNF4rwMdhvJxTXwjLdevhZTXULYKBelNRx39buVx-7xD49PCiomxBFXO7ad4ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
❌
🇮🇷
— سنتکام آغاز حملات علیه ایران را که از ۲۰ دقیقه پیش آغاز شده است، اعلام کرد.</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23155" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23154">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">▶️
هایلایتی‌ جدید و کامل از عملکرد نظمی‌ گریپشی فوق ستاره تیم‌ملی آلبانی که مدنظر سه باشگاه بزرگ پرسپولیس، استقلال و تراکتور قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23154" target="_blank">📅 01:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23153">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5N8jlRmvMm1_lo1IxSjoTVlm3CgmegZZP0seli8anjHiobokiXIe-JVpv7o5_QxoLC7E1IrgqclvPU78YfrTNPpxbjdnoLkJU4DPz-Td-3GW3D2lDcx-nv9-Hx-BW8VtwwSTjrLUawNklaN55Ptb19Mla73p97orMHPM1Ago9f0YWSNHa__zp7zUERVKW4iAc98S6VUl5NK0oDOTbzYBPHmU6I_x4yE4N3qQ-euRyvF7cbJgingfmfARYUIRbkF0gi1EfZeF_k0N6SSrZAJuVpTHIcFSZSlIQIa9lXmJI-SC925zhdo0k8Uj2z4LP3BOk6Djd9pq89ZebxyNVPKZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ادعای‌‌سانتی‌اونا: باشگاه‌بارسلونا ساعتی قبل پیشنهادی 80 میلیون‌یورویی برای جذب یوشکو گواردیول برای باشگاه منچسترسیتی ارسال کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23153" target="_blank">📅 00:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23152">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d36c28277.mp4?token=HN79L9J9uxME7zE_W0TueCDQLJdjlNxV7cPmL-O8YV63q-uUPOcv0hLaRHZjC-BdKKiB4t1xG0HC1km3fnuFItmNZL4UxzZg_HDV_sO5haq_p6onJsQfbr1vSfpWdWmqjH_nX148aPO54emieT28TVacC667wBfOEA-_wPiq67raCa9QvZxLFBX5BkJnLIlXXZfsVZuwH3ycnQf2XXZ5a1Dc649_4VBb-Z6PcmviR0RlLitq9ygTbgdD8TfYbRCPJywlXRFRlDzyXMPErEaSU2DlxAErexCnHGI0uPntzUDpY8WAl2T_IxlHFBxgwcZgVHV2LlpvN4_i1P06o7rxIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d36c28277.mp4?token=HN79L9J9uxME7zE_W0TueCDQLJdjlNxV7cPmL-O8YV63q-uUPOcv0hLaRHZjC-BdKKiB4t1xG0HC1km3fnuFItmNZL4UxzZg_HDV_sO5haq_p6onJsQfbr1vSfpWdWmqjH_nX148aPO54emieT28TVacC667wBfOEA-_wPiq67raCa9QvZxLFBX5BkJnLIlXXZfsVZuwH3ycnQf2XXZ5a1Dc649_4VBb-Z6PcmviR0RlLitq9ygTbgdD8TfYbRCPJywlXRFRlDzyXMPErEaSU2DlxAErexCnHGI0uPntzUDpY8WAl2T_IxlHFBxgwcZgVHV2LlpvN4_i1P06o7rxIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادی‌ترین‌مدل‌‌موهای‌بازیکنان‌وقتی قراره تو جام‌ جهانی بازی کنن؛ گل‌سرسبدشونم که برزیلیهاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/23152" target="_blank">📅 00:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23150">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2567lP3S9qzR2r0NZfAzbxpburnYVTbj9u8wj67wkj-Htz4s9njEGwuNZWo_ozWIeH6YIWI9pmLUL8Vjv4zbj9JjoDjgTlKtkEcBr9ybXd7DV1o4jAnid303RDqjK2gpqUJ626qUaH-Qvhvz7703IMum60zQ6JToQctZhkUXuD9hV67D4_tEdJIzsTuaIYXacXwPJ_1E6cteQdgj5ueTx59VR11rOuvPwogmyZHroncp2BbLAoHJFK-4K0GhjQGEmi4jnYZXYLYY6gFj3TnQ2UvbZq3OhxdSoU6ntIWXFhswoPz7s8DHPQH222dbv24fAge3g1cQ5O0CpezJy92-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ دیمارتزیو: ژوزه مورینیو سرمربی رئال مادرید از پرز خواسته از بین یوشکو گواردیول، ریکاردو کالافیوری و نیکو اشلوتربک‌آلمانی دومدافع رو برای فصل بعد به خدمت بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/23150" target="_blank">📅 00:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23148">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxsxLPmbpPWlPAL-xJPVwqSnzhcc2FWfUX2iywuUcTLPCCtkwZpoRoE62QJi9dVe9KpmfUPgvAON4--Zv1gcV5HHG-FlLOxBBxFocqwib5bji0d1tPHWSFT-9hr8uJotZK_vZCDstlvMZTfjkO1R4mB2mpEetpzCI6dac8WWfWTCDHL-QUFvrxqJJi0CsHsUVwaSGwlOABoEuNuj5PQX1ljqOoFsJNWnqRfswsel7eqdgxYhMkYuIgxTIro6jDAnA4IKuoykCjyyW7hloiVN-NgDfYow0c8Z5N_OpHH2GfKvTBWIUTUHOS1RPovBZZU4I7VxjH_hhasD70vWdX3nPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🔴
#اختصاصی_پرشیانا #فوری؛ رونمایی رسمی از لیست بازیکنان مدنظر اوسمار ویرا برای فصل‌آینده‌پرسپولیس؛ لازم به گفتن است برای هر پست نام دو بازیکن رو به مدیریت باشگاه داده تا اقدام لازگ برای جذب یکیشون انجام شود.
🔴
محمد امین حزباوی و دانیال ایری؛ دفاع وسط.
🔴
آریایوسفی…</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23148" target="_blank">📅 00:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23147">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ace048c41.mp4?token=aYNj4zDvCPcoeRNFJT4LI4nvura8Dj7KvegoPmsCesuukdCEJmKQQoEBwDXi-0yfQ18rj7GPr90hWrjtxWrhUTs4T4lkUX-bvObBIqaSoU26S2RJu54SRTHj1fRZqFJHRoJy72bJoVfcFjMV6jHrD84Y2Q6Tpn78txE6EHrVoETxM-00932HzpJO9XnDAWY_TZLpKuNROhl5-ESG5dRqwjaazl0olB7LZc5Smvs98UakPO4MHZKpAHxOyAGyQOqFYzTm7hGUyc58HII8mSolMHm3zkteiTtiw86Fz7Y3O--WOhsjhLRqwG1EQ4M0k3H7_Ne9GMvStXS-8gnGnXgX2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ace048c41.mp4?token=aYNj4zDvCPcoeRNFJT4LI4nvura8Dj7KvegoPmsCesuukdCEJmKQQoEBwDXi-0yfQ18rj7GPr90hWrjtxWrhUTs4T4lkUX-bvObBIqaSoU26S2RJu54SRTHj1fRZqFJHRoJy72bJoVfcFjMV6jHrD84Y2Q6Tpn78txE6EHrVoETxM-00932HzpJO9XnDAWY_TZLpKuNROhl5-ESG5dRqwjaazl0olB7LZc5Smvs98UakPO4MHZKpAHxOyAGyQOqFYzTm7hGUyc58HII8mSolMHm3zkteiTtiw86Fz7Y3O--WOhsjhLRqwG1EQ4M0k3H7_Ne9GMvStXS-8gnGnXgX2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
#فوری
از پیت‌هگست وزیرجنگ‌آمریکا:
سنتکام امشب درگیره چون پرزیدنت ترامپ گفت ما امشب ایران را بسختی خواهیم زد و این کار را می‌کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23147" target="_blank">📅 00:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23146">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDGNjWOmDlIlRLpFG4bYaBtWODNtajbhPY8Dy3Ul9Os9NboJbRs4u09c4BoiSuo8gaUeTX2kPEpGEvUs5Zb27FM_IxxI0J_70PjIQQZ1x6ARqTNdZ5t7-NQhIWRce6NCoBszhHroOdcNymNxcJ370MQWhJvjdyoYWdYwMOo5GhpccQMKk6o9-Fydo4LFqwQ46l0ZGj7qG-ROY42E6sUaC2vqxfozfw0xpAcKitU_3apIBUgcnqak7qaqzPNmT4Vd3ttShMZbAho7ifthiMjVgXOkq7A15DfErWt9Yj2nhZQZ5EslH--g_z1hGwI3JIJl2hoRNlzVVENKi07iJp7NRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌مارکا: بارسا تصمیم‌گرفته‌که‌بند فسخ قرار داد30میلیون‌یورویی‌مارکوس‌رشفورد رو فعال نکنه. بارسلونا به سران منچستر یونایتد اطلاع داده برای خرید رشفورد نهایتا 15 میلیون یورو هزینه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23146" target="_blank">📅 00:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23145">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IWg1n4LagP-hza9-zxFrmrbr3ZukUlPfKESMIsmTWR0lKQU1Gqo6ofbg8-nzyJQCGjv01wTI4WT7EIH5cEL0_S4pbtbraKgbG7SEL5-aWyJrv_t6ybTBfp01ScSTzX52UZ6i08t85g7FrAXjZMSHFLb_w8w98Ub9s9qC3yV5ghTreYw_fP2qWEJbRsCXl6pHWfLaLUQ8vmbfjg4w_CI9OgoFgB98GPKr46mdvZxuZI9Gymc-1Q8sVElorKAcXZ0VjphOHrqlCZGg0eXKi5Ofjm7aGUgmA38MUMsyBKKOdi0nyknReu_RON1psHtNKXQxOvTQFdQELW96pQ6c8zTWbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛شرط مالی علی علیپور برای ماندن در پرسپولیس مسخص شد.
🔴
طبق شنیده‌ها؛ ایجنت علی علیپور به مدیرعامل باشگاه پرسپولیس اعلام کرده که این بازیکن علاقمند به‌ماندن در این تیم است اما برای تمدید قرارداد خود به مدت دو فصل 250 میلیارد تومان میخواهد.…</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23145" target="_blank">📅 23:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23144">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZfBZS_DNXDYa5AUqKd419zEWGB34wLIGvUQXIk81uOys5FkE70Dx1z7lAy38RepRPfnM7tLrrJjTJaqiCj0jKxZ3BSbU88JvocwWiD3IaNmlijOGCy4VhNiu_QaSWyIGDA0u6EmKNIR0H_I_LQsG1QIXLRA_LZh8mkbc6rLS2-JykysUFWucT0MIkeVUs_eiZ6demu6-Zr7ZIePVTgDRLdPD8kjEii1Q1l2LiTqZ_W5gDZ9RGvUlbAS-FKBcL30tDqUAqT_H0_tTMUWmSqJITiKtREkQW3LV-PLpOr2-SslnfgoJy2uYk-t3r2pwhyT9_YXsnEj5N_pWj-7HIRM4QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛شرط مالی علی علیپور برای ماندن در پرسپولیس مسخص شد.
🔴
طبق شنیده‌ها؛ ایجنت علی علیپور به مدیرعامل باشگاه پرسپولیس اعلام کرده که این بازیکن علاقمند به‌ماندن در این تیم است اما برای تمدید قرارداد خود به مدت دو فصل 250 میلیارد تومان میخواهد.…</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23144" target="_blank">📅 23:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23143">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njX0HXXZkE4JIm9FH3rJcCrHLS3j-ZVui0UfAhZe7xHeDHDIUpyDI21Nn_2ARZwrviSBeY2jXFe2mTfKRE4v6xsoXvp-Zu-eXBi7V3xVwqy1II7E49IEwMVPeXh2_bvwEFtj0--kzCFDC51SbAsSZKLD_TMU-kxEfhHO_jeV6fowdXL0BQ-PCZaf4jtDs6zIIBzsdkW6LAXTyZkUnoNYQtt2OzsuABh8vzV6TL1jNNQYKpTQQ2GNbKfp63H7zGC3SS0RuxN_EJ-QZi9aaFyeXpfog_7dHHP6jr8_Dyq3r6aThUa23EZuzp2xEwQSyBDdsWGR_sKBwsHlaqPjSzmjQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🔴
#اختصاصی_پرشیانا #فوری؛ رونمایی رسمی از لیست بازیکنان مدنظر اوسمار ویرا برای فصل‌آینده‌پرسپولیس؛ لازم به گفتن است برای هر پست نام دو بازیکن رو به مدیریت باشگاه داده تا اقدام لازگ برای جذب یکیشون انجام شود.
🔴
محمد امین حزباوی و دانیال ایری؛ دفاع وسط.
🔴
آریایوسفی…</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23143" target="_blank">📅 23:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23142">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MCvrVfZEZz9clNxTrvstHQ9VVJL_hg82O18--oFYF0EQm5aq4VeJRO65aZn1q5uLsxTrr9ElDcgBg9Cs7lNWHP4wrobpO96lnrX5c0T2S4v3f6ftLRkd8mTdx57Yj0H63QAhxr6Aik5IonY2FxpB4gBltSBUs8W-1GiaMyHiwmJXmxs4MApR2qHf4iayywck_iE-MQDneJKXJSQesTRuL5ZrnsqvkZH6n2W99XcOSqroRAEF8HtvHvJOgRQwM9xkgUU__I3GMdXTwdbLymeSjhGjs2SnnSHYyI7S0uCvDDMc15lllKJSP5apNkciOnDH-vSNVdlFshkiFpyI_ovDUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
از امشب‌اخبار داغ نقل‌وانتقالات باشگاه‌های لیگ برتر مخصوصا چهار باشگاه بزرگ ایران رو هر شب با جزئیات کامل و دقیق برسی خواهیم کرد.
👍
بارسانه‌مردمی‌پرشیاناهمراه‌باشید.قراره بترکونیم. اخبار جام‌جهانی رو هم زودتر از هر رسانه ای دیگر در سریع ترین زمان ممکنه اطلاع…</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23142" target="_blank">📅 23:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23141">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KlmVgknCTCPsh2gpZxkiTnIz4QRvnmzE-pfapUmFm24tlP8FbjSsVGOk_pdH8GaSz01WwGbdbq-fgx_-8QviB9I2MkRcVfcE_nH9FI3B-w_hMM-jtQZ9N0FOiNt9rT3NupSbB16RXBJFWwtpvb8bGPMufa1od8xLOKcBYLaYGw_mQ6ZsTsaQAAjqinliwADWEnoXNwiLrsy3dbN-LZFKIa4JCsBYo6LL8zzG2XHicujBJIkFl55vB_Np3wkwxhX3TrHEJRT7JHHHhi91qPwDnwVj-PC30WNkHF_QM7FhNgUpw_7rQz12vU6Ae8AuSdavCQuM6u5E0sdWGXhcSpqO7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ متاسفانه اموال و حساب‌های بانکی و خط موبایل وریا غفوری توقیف و مصادره گردید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23141" target="_blank">📅 22:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23140">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64161e2ff3.mp4?token=BBS767Mi2eMJ5zPAL8r4XiJMIgKqcz0zPnQZnw-YwSY0vFHDbHOqh7DDMwPbm8R2HOSDsXMZKjvtyNPYYpUUNei0BChVzndv3MRIfxjA-TqtPjnGJfAgQK7XXA40jRghzPtzcwZBABns5ZuxmTz7XyfjtpJpkA4UZG0inFbk1l5YjQHE6Xb4nMgDfBl6SCZDlOAlgqxwDD7ayv4vkh3yuRsAx55CMagwoIFwsLIiPb816x4brFdq73A36-BXmeSIDzgG4u3x8mnQqK05aKgHnm3iacaTdVY_pKkqvC_eCa1aA9oBA1UnG2toetC1UU8_9FsqJ5prLFyMMiXXFfl3g7fNwX7ubBBZTP3pwNsLTXN2bGJJzNBBQTrcdO4tfsR72cMmpmx7c4XsCPh7i9lPDxXce7Aj6OEZr45NuVdDjay6C6H18VKfRU8Acij3q-sQmL0RCLBz3e5KfyTpXcn9Vnwlw3X9jKOD2prWVtHdJ9XVEJb5vIKwxCT7jurTGWPtGK0nsgANaCQTQIYxHgbyGgEHOXv7sxu23BkjWdtr3TQK-WY48i11BKz_YkxvobnVDrW29F3nptYzuKzO1SjACARxkEmaOprYj6keMm3kgIMlBPu8fUjzcLkhYUDIh7jb9M4l7uhCdmpja1EQXKbGtJUYfuiOujHTjO1x2JUw_6U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64161e2ff3.mp4?token=BBS767Mi2eMJ5zPAL8r4XiJMIgKqcz0zPnQZnw-YwSY0vFHDbHOqh7DDMwPbm8R2HOSDsXMZKjvtyNPYYpUUNei0BChVzndv3MRIfxjA-TqtPjnGJfAgQK7XXA40jRghzPtzcwZBABns5ZuxmTz7XyfjtpJpkA4UZG0inFbk1l5YjQHE6Xb4nMgDfBl6SCZDlOAlgqxwDD7ayv4vkh3yuRsAx55CMagwoIFwsLIiPb816x4brFdq73A36-BXmeSIDzgG4u3x8mnQqK05aKgHnm3iacaTdVY_pKkqvC_eCa1aA9oBA1UnG2toetC1UU8_9FsqJ5prLFyMMiXXFfl3g7fNwX7ubBBZTP3pwNsLTXN2bGJJzNBBQTrcdO4tfsR72cMmpmx7c4XsCPh7i9lPDxXce7Aj6OEZr45NuVdDjay6C6H18VKfRU8Acij3q-sQmL0RCLBz3e5KfyTpXcn9Vnwlw3X9jKOD2prWVtHdJ9XVEJb5vIKwxCT7jurTGWPtGK0nsgANaCQTQIYxHgbyGgEHOXv7sxu23BkjWdtr3TQK-WY48i11BKz_YkxvobnVDrW29F3nptYzuKzO1SjACARxkEmaOprYj6keMm3kgIMlBPu8fUjzcLkhYUDIh7jb9M4l7uhCdmpja1EQXKbGtJUYfuiOujHTjO1x2JUw_6U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین رضاییان مدافع راست تیم‌دعوتی امیر قلعه نویی: جرمی‌دوکو؟ من اصلا نمیشناسمش. کی هس؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23140" target="_blank">📅 22:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23139">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eba85793af.mp4?token=Nb7_Ac5DxUhf9EiCYZmPqOO96f2ap3rC4YtfOAlff5aLDYBQbCouhII5TlzbrSm1ku5EbvlZXRAdax0IrfN49wQXaRD-o8dPIJch7M512q0TqOkB1UELd2Wai7sZYicWsd2z40hD1iGpOkoFntQJUfNQ4nhWaEdW8CGTdk2gsznlsY4eeP3FyFe-OQAAdwgSBLodSrm2sEDs7KjHSY7XlOWJtzLkleIn-0IYDQE6PzM3VIIyQhCaevmCesWWgYW4hiAnEf03NuCS-mnDyWEQ7oT4NWTxQzK7wJEGH64Kd3P5NZylGc3OsSIeoPRV87Cg4sKqGJcCJhkIFZItCpj3RH7VI6wcgb3MnEwxoPAKTEed-HMz0p0yWXBPG73Fpuul9L3dZYjei9rbFvri_m_BH0dTZCKIA9HQqeYDqcEHwLKpCilPzVkBtkmG-ughANZ-DdZpvwrOSNQTAvWZJGHT100IjVBqt9DnCev5Ji_HkUJd9a-Ke2XLk6i-hla_khA1IkC7QGkgvGoGSomjYH0fqSGmkYV5tG53MeUQPcEkE82K96IZ94LzNQok5qe2KTk-idDx7L2rgdusYR1AWnA9tgMagln0f0I0C0o_LigTCvYRXnBxtlB0-oVv2cPHegElQhXcUOUgqal4yDXDb0op6m3TAnqOM-pEbbKC-rHO-II" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eba85793af.mp4?token=Nb7_Ac5DxUhf9EiCYZmPqOO96f2ap3rC4YtfOAlff5aLDYBQbCouhII5TlzbrSm1ku5EbvlZXRAdax0IrfN49wQXaRD-o8dPIJch7M512q0TqOkB1UELd2Wai7sZYicWsd2z40hD1iGpOkoFntQJUfNQ4nhWaEdW8CGTdk2gsznlsY4eeP3FyFe-OQAAdwgSBLodSrm2sEDs7KjHSY7XlOWJtzLkleIn-0IYDQE6PzM3VIIyQhCaevmCesWWgYW4hiAnEf03NuCS-mnDyWEQ7oT4NWTxQzK7wJEGH64Kd3P5NZylGc3OsSIeoPRV87Cg4sKqGJcCJhkIFZItCpj3RH7VI6wcgb3MnEwxoPAKTEed-HMz0p0yWXBPG73Fpuul9L3dZYjei9rbFvri_m_BH0dTZCKIA9HQqeYDqcEHwLKpCilPzVkBtkmG-ughANZ-DdZpvwrOSNQTAvWZJGHT100IjVBqt9DnCev5Ji_HkUJd9a-Ke2XLk6i-hla_khA1IkC7QGkgvGoGSomjYH0fqSGmkYV5tG53MeUQPcEkE82K96IZ94LzNQok5qe2KTk-idDx7L2rgdusYR1AWnA9tgMagln0f0I0C0o_LigTCvYRXnBxtlB0-oVv2cPHegElQhXcUOUgqal4yDXDb0op6m3TAnqOM-pEbbKC-rHO-II" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
در آستانه شروع رقابت‌های جام جهانی 2026؛ جواد خیابانی رسما از صداوسیما خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23139" target="_blank">📅 22:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23138">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1ZR43LxHEIJO2RhZyoLQDmyDqWQ4Z1tv-BfV5agTZJEn7mMgGSIlioXOsgovt4gKp-dNgW2jH94BuVfJUo0RUsjZ6i_LPBICM3Hg2en1KX0dSYaa9SB1hzrTbz_wK1JQBU7NIZL0UZJX-HbKr7T9bE0ujp7FNB3g_4XGbhuQKvzM1Q1AvAhRY00zc6QlTytDB8K7OPaLuB74vlPkudhffme3JMoUWcHc4GPkzEm24-7b_oEbx7Y04qDwqhkcBlRJAeUjm8vfteKFf2SeEfQ7JRrrolYHfp6iE5kWQlR2MK4cbU4c2EBsQhWmtJlysfGaVB-wv3tY9oweYnnYFUEkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ دیگر مجری ویژه مسابقات جام جهانی شبکه TRT SPOR؛ از هرجانگاه‌میکنید بکنید فقط از صداوسیما باحضوراون‌دومجری عنتر نبینید. از شبکه های خارجی‌ببینید از هر نظر واقعا فوق العاده هستن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23138" target="_blank">📅 22:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23137">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ho8H080P0JIl7NIFTOtHW4rVtMunaq3Bt11CTYZL2zKRqbZ_ypalFNvCCYI2VuRcxphhYjKTAk_ZjJfiMrpxpTWGkPm08g4rTTkatQuYYkQZ1InkoKnl327dJaO473BiKlzShduQKZWOuHDv-YpdS7P88ny2i-dqAgnwdSqluWGb43CR7tXAa8PiOhGTyzXS0JwpWy7NkSv9WC0o6hckhJ_QWdR_VsVC0-EkbPheC7qpq81RxTu49Ln1HG4odFavs-CpFmGbCL_HElL-PMOQg904hlNLMivW07BdwJhnqT-gvT9UYQybdrEZ2umKwwtsy0bFPt92xFII305lxnbetA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23137" target="_blank">📅 21:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23136">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mq735-oYzhEcKcae38NzA8_dks4xSpmfQZFWbYboqYYEJqP1LZn_rbKcih4K5GAij7d94SF6v5HF1th0mhZowlq1GV7ooduBtHoPXr2cP9UgPpEn6ijVU1MQemNizvHzX7761bHcWA2LeCUSXjqP7P0s0ZJ5eqTOMyNTtXqlvWg3eaUDdCORQNkTMsrPebx6_OHT4ay3y_djnsMxgmRGBUFi0VwYJ2B_uIlAxtLJjgWVE3f6S_DQxq32RuDWVvc6acugMPd_c5QNgI5noDRA9gXlDaIJS50yr44m3d2BQlUGI-O7KeWp0ZWSAPGJrC-grIurWibe-9VyhHOhBI7piQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این‌اشتباه درطراحی نیست؛
پرچم لهستان روی پیراهن هائیتی؛درسال ۱۸۰۲ ناپلئون سربازان لهستانی رابرای سرکوب انقلاب هائیتی فرستاد، اما بسیاری از آن‌ها به جای جنگیدن، به انقلابیون هائیتی پیوستند و در راه‌ استقلال این کشور جنگیدند. پس‌از استقلال هائیتی در ۱۸۰۴ ژان ژاک‌دسالین به لهستانی‌ها تابعیت اعطا کرد. اکنون و بیش‌از ۲۰۰ سال بعد هائیتی با قرار دادن پرچم‌لهستان‌روی‌پیراهنش در جام جهانی ۲۰۲۶، یاد این دوستی تاریخی را زنده نگه می‌دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23136" target="_blank">📅 21:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23135">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ke7AQyJx72Kkkg9u47gygjIKrVSZHLlLpVLAUDI-bx-V0vVfDMT1mVXvUZa88whALD6aoY9ywa8y7yqcmNITSYtfzvUQkIVIzOJz_mS2u_n9NdOPx9yMYX1JGOS0qu3ddDemRKodLjqBsAdHhmtM15eso6A2HgOU9bm44aUqW4FsHTqaP2ECE487leJCH1Wryh1kY2T2dAMqpXepmLNoUmVul3NRKjbx7WTZunUbn8mE_Amervm_BBNz7BW_WCDjdgXzMFeDym1y5hEuoEVPT5xP4WkKguRf2mAj-FM7sypqJOmVLKXgRJjGhLHveaCt6i4X38J_XzqkyMagOBQvMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
از امشب‌اخبار داغ نقل‌وانتقالات باشگاه‌های لیگ برتر مخصوصا چهار باشگاه بزرگ ایران رو هر شب با جزئیات کامل و دقیق برسی خواهیم کرد.
👍
بارسانه‌مردمی‌پرشیاناهمراه‌باشید.قراره بترکونیم. اخبار جام‌جهانی رو هم زودتر از هر رسانه ای دیگر در سریع ترین زمان ممکنه اطلاع…</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23135" target="_blank">📅 20:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23134">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F96kJokKkDle90THEO1JkL7mxWpig7cTSzSvALQkAEH5utNN32LTs8rBa4i1pOjfZCTuY4Ci5djFzszAa7DyepDvOeeKUH8vJ3nro28GD-jO3M1JWcdcwToUVeBZBrzMX_oK7bL22pD50W5TDq3e6AnRJXsWarGIzpkTiOjDacl_XEynXI7NBkzrOqqEv2LD0jDeQ4WIO8I32mHznAGuiAaP721gCcvwK-MgmX0wNigdseAt95DOCz7DFabP1gWNwBBuHXtaC6AB8cBUoCMRha2z3DgvWMOWMXDrHeFPAy8kigOA0d1YlyAIZQrhXLxkC-KkrzmaQnoA8fGjf_HuPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
مجریان ویژه برنامه مسابقات جام جهانی 2026 از شبکه معروف TRT SPOR؛ فرکانس شبکه رومیتونید ازماهواره ترکست پیدا کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23134" target="_blank">📅 20:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23133">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/alhlDYdWXWZlYRKWBWX0QD7eMDHhMwxFxGb--_oNYqaUWC_cWxt0YUItX8gmMOmEnjUr14SyL6d7woMv220qusPjTYv9SPqqTz87Du6M4qar2BbdEgg7R4oYYcTMhlYCyNiscU2yrN4DiaPghV0LrClJLhNDMsXsbXRDN44mGcv5kGrBg_c8BYgWkUKdNXBbEZaTgoLBDHNFRBLxt0Lq1fFlepnYCuDAL6VoEBP3NkK1GrbQ6Y2lwBBRSZprdlB1zDt_6f2uqIOuB64ismWBnX2bqPusGiP_8PHtnOxZ9_3vlGmeHreOKW3SNELdivO2mc4rzZvuOVAIVqyxbIEUOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه‌استقلال بزودی خبر تمدید قرارداد علیرضا کوشکی بمدت سه فصل دیگر رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23133" target="_blank">📅 20:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23131">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/keZqUI1Do89dJ_uJkfvBsPRWLY2qJArgivgt4SHSTai4S3b0-l64GtNVL9OG62usGe2YH7tcU7y9ghhD_i2GW9kpxO7zVdCgkAfxPAFIEvqf5ExgE1preRLNYIF4XTlNLLT107-jy6kUKF4JQhfIgjj_zuUmklqRGDEMirnKIwJB0Pcn1D2-CjG941S19cjsybAmT4Obqo49oddObIHL1Z-nuCZntZLKXE-gw86toL6zRugx1-SlalRlAHcOwaZClBN5Tae1QkpeL0h4nXYAt8hMD2Gdibq62j6E90aPjSocfxQRLb-HC74U7bobtwhzPzj2qhRLkirLvUZ_JuomSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dwK0qARgRqGJv0lLUXqIGWg22bsBjIXMnddiibwQaDbqWKkXBCjEtG4O5yv3VfZi0dVOb7unkuO-XigKvOeqcZy7EgOsuYyRFR1QNUGbm-oyAjR25fSyEEH_zXcKZuACqFUL8unb7YKl1rH7tC_RRsmyETxa2ItiCB6pglrXJaX9FBOVqkP9JyXAVSyWQhDl6vngvEJNHti6rFLD2i2XHOuTce__mcSF8z-gMsjs2e6FaiswFcyFummih5T1WZPdMAwNS0D4towLr8ZywHzN6d7QZetUwxH9P6ydLdsqLnGItjjYc1h0lMe9mgkX0s5YCGhmhQzDq6hqKhgYPz6C8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
خبرخوش: تولد و بقای پنج توله یوزپلنگ در پناهگاه میاندشت‌. ‏«هلیا»، یوزپلنگ ماده‌ای است که در آخرین زایمان خود در پناهگاه حیات‌وحش میاندشت خراسان شمالی، پنج توله به دنیا آورد. طی یک سال گذشته، این مادر و توله‌هایش بارها توسط محیط‌بانان مشاهده شده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23131" target="_blank">📅 20:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23130">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e58078f0d1.mp4?token=ROfJT94M46naxHKH0CqP55Wvq1XcM61aqCPzoE-eqqAezw2-vyMHZR--vu65sEwRCzeEKiS5-UQDPBv1DDs29NUVNusGP5wW60O-EKZrqALWvIVzsncdH8IFuGQhPdXRK4YLLOeVQk1nQFP6iJFS8jkMl_lzlg6TGg5aJsPp1Vl43XGGfXkIcPqnWQFgZFGmSlUiwvoW5ozIJpwVWw5nl2nCtiErID9jQpT-zkHGmbpSrD5-ZQJNnWYtbeI8g-Q4WPfxK1OWCYJVsLizCLslkn97uvWcHhvYecYN3cEDUcpVOuGxclA1Vz3HpDDP0YyUuql7wjFnKugAh5ucxjRZOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e58078f0d1.mp4?token=ROfJT94M46naxHKH0CqP55Wvq1XcM61aqCPzoE-eqqAezw2-vyMHZR--vu65sEwRCzeEKiS5-UQDPBv1DDs29NUVNusGP5wW60O-EKZrqALWvIVzsncdH8IFuGQhPdXRK4YLLOeVQk1nQFP6iJFS8jkMl_lzlg6TGg5aJsPp1Vl43XGGfXkIcPqnWQFgZFGmSlUiwvoW5ozIJpwVWw5nl2nCtiErID9jQpT-zkHGmbpSrD5-ZQJNnWYtbeI8g-Q4WPfxK1OWCYJVsLizCLslkn97uvWcHhvYecYN3cEDUcpVOuGxclA1Vz3HpDDP0YyUuql7wjFnKugAh5ucxjRZOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇦🇷
حس و حالی که از آهنگ‌های تیم قلعه‌نویی و بازیکنان منتبخش و تیم ملی آرژانتین میگیرم:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23130" target="_blank">📅 20:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23128">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6PxRoawkuliR0AXWbRpZd2e5sYpml8MEkne-XTHSWNA120oqkAoojh4BBEtW2T1SXmBAv17S3z5RJBA7BXo2NcNE4fiFdBwaCtpBq2LRo27AC1WpDw9a3OXlTf9vYQQDgFnwzrmnFX34aNobTNyiGr8PzbDxQ-p5ppb8HOTOCHKMuh9f7KMnZnZPS-0VrX4LCrmFE08I7e4y47-l01_cRi1dhJublt4JmUpL3za_ui7GlBDueJUl_FKuNLSTd0NwqAUKn_zEuCw2fKUpKaW8p5iMjOzgpV9k-AA3tXeuBXGmOnUD2EAEoeMeSZyi_JoQJ4WYtOw-vRqOwBEt2-l4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
مارکو باکیچ هافبک سرخپوشان و نماینده‌اش این هفته‌حضوری بامدیریت‌باشگاه پرسپولیس جلسه خواهند داشت تا تکلیف نهایی ستاره مونته نگرویی برای‌فصل‌اینده رقابت های لیگ برتر مشخص شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23128" target="_blank">📅 19:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23127">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RifUdScwJypKmQuEjv6jzPi4UmTGoDMIy5xXuTLPxw0Bnhf97EAWmv7lR-PRAkGCwZdxn514AV1HoPn1d1NtOeC07fMz5D6qfHjdueow1Pq5_4NH1WHzbD8FDgQ1CusFhBilKmXGsY7BtN52fEpX0S61lYrr7oQdlgQCTvvyA8iDx03gRdlukdKqmjuIX75oUSpcR3_A3R7gmPyk22VIXCV65EKUDv0Eb8w01ROG_XWVD05McJap7wqh_RMOyp4Fk3nE30Hu2AvsN1nsjsgatmmLd48q3ZwyOOB9ASDMU-HvBXEXu9by-WXAKJbL9VbGXFtQPTW6Fwc4z4CCUdDU8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
#تکمیلی؛ خبرنگار موندو: داروین نونیز از طریق مدیرام الهلال آمادگی‌خود را برای پیوستن به بارسلونا اعلام کرده‌است. باشگاه الهلال اخیرا ستاره اروگوئه‌ای خود را به آبی‌اناری‌ها پیشنهاد داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23127" target="_blank">📅 18:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23126">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBUZxgpTLTXYLHopONlVr9asJ2QWnNtihNxE-X807WPJdt6anV-P2vr4OO6CqA5it0EO-8ZHN7KZjwPAIbkp3kMnfzi7ngHCzqOyf-mUJKcFdMDLFgYjUGXuVAST4CSP1ElPAyQXSzlEs4UEMuO-cMcWXa6uGFSKtvkNFOOkYe69MpStfffVoAw-7nM2bAiyBIuLnDGs8x5o2An385rCq6Tr2TZz16Hyx4h2b471zWVMlx3xfLBMBCw1aLO22A1Oga0AU_b8f3lkmqhRUtZIJrYtxNid0v8fP_5KCT1rVIT_DwzFXwvOv31RI7cjQnQerJ3O25Kp7QhCgItkGTjSPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
#تکمیلی؛ رئیس‌اتلتیکومادرید: هر باشگاهی خولیان آلوارز رو میخواهد باید 150 میلیون یورو به حساب باشگاه ما واریز کند. نماینده آلوارز به ما گفته که اولویت او پیوستن به باشگاه بارسلوناست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23126" target="_blank">📅 17:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23124">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o2dnoJ83iXhfCaa5Ru4AppknVN2Zn3ekfeaBbq37a6_PCI1LoYjzjuSZCLDR4Q1qVeirCuWZfa7mfPTxk9f8MpnDJ9jg8_3_y0mhwm9Hd7MsVh6sRUjqwXNrLnpeUqOgFQvpJYKddWaiWc1w0r3a3_tqIOhfPE14FRlZPrXpzTKUJS2BwM6KQBDbiDna6Rnp3_KnkN6F_WLyzkZBmq--Dlvq8AX2qNQbhS67_xgUdeCzL4no-jBFN_8ZTLyHfy66w60bsWfxME4LQB7uxDutdirzg5O2x_AmaKvJIg1X6Gw4_uA7VcfgMZAwebtUuALRea6aLMSqNN7Ul3IZlOsP2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pQdax1LcdQW_Eje8k3ljooy8X4TJhfOzsepnXATby7dClGtoIkPXbGswSknkCCmN69TUVmcvvTgEHKkM7PMh-yX8hTeJtsIxKMa8OsPAeAxI_yJqZeQJSrFoT7zhj6oNonkGrJn99V0Z2jRlraRhxesRx9PmcVNVH6hvDvq5BqRMznADNBXwbALqO1-FDm5ngO1TQ2sjyay5bSnAjXhqGDxwGv6xgpNv6qCSW1k7Aj9TTuBV8oxD-J-LyEm51sBtqI7TSFGc69cyhjrbCDoeyaqz8JeuXyfC-HlqVa3sZIZtaXv9CO17pGPA16uwjlfGUXucoOpRMen7WTPP3gyQgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇷
🇦🇷
درشب‌پیروزی 3بر0 آرژانتین برابر ایسلند در دیداری دوستانه؛ لیونل مسی کاپیتان آلبی سلسته به این شکل موفق به گلزنی در این مسابقه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23124" target="_blank">📅 16:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23123">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psVP-e9OyGtj4sL6fqrrd8zu5duF4Uks6E5XayikK1-_ZBfZnPxpv-7P7Z8VEVlHwFrv-UJy9UdIIF_z6ACRs4VeHt6bguFYbO4rEfORFbplOgShGbHvE-lmW9YPCEoJK-jBZUeerOXFLGPmGJvr7bOrpDKQYF-gZx0sl6ZIxZwx26NFjQsDbADjZYdk7qUpz_IBwJ6l4AWz0lcgf6nEPxVsFGb-9G4hNBtMMjFbn9qBQXWja4GjBHoAvQ7WmnCelGmp4fw48UnhBNqBHMl1ZoWZlb3llYkjYp5kK8O0pSbGoodPzH1Dy3oDM53CAoAyxBOt5Fck3L-Ofv_iRtg4Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درخصوص نحو سرچ فرکانس شبکه‌های رایگان ماهواره یاهست‌سوال‌زیاد پرسیدین. روپست ریپلای شده کامل ویدیونحو سرچ فرکانس شبکه مدنظر رو توضیح‌دادیم. الان‌این ماهواره‌خودمه شبکه‌ها سرچ‌ کردم مرتب پشت سر هم قرار دادم که هرکدوم رو خواستم سریع پیدا بشه. تموم این شبکه‌ها…</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23123" target="_blank">📅 16:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23122">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
میراث‌ترسناک‌ضدحمله‌های منچستر که بعد از یه توپ‌گیری آغاز میشه بامربیگری کریک پس از سال‌ها که توسط سر الکس فرگوسن اجرا میشد برگشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23122" target="_blank">📅 16:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23120">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZD1LUry06zSvvFBTa353Y0iHCJqbFLquZdYIQSQZIR9h8vivPb3pqR-8vuKdxpx82aqnUZH76hJ4xGg4wTwAiEuHCUTg4cjbVkbFMY71qgzk_wtxjIKLe4zLMU9Wm4CLTQ2nNF-rGdWieK3m_0INP8A4n5TRSILM1-ODXuwkyewq8I9cMKC_LzUMBtsJGRADnuy-rECCEv4TcOd-A1i5vUO76xV5QmdpLA0fqjpH7dc6-umCKpA_-SE5vzb6BdDIXLOPrH2n_3nqoRSzpqy2t5zaEltaDvYh2qsDkzRPhWcVSW1g_htrk2T9IGF0DR1jEIvMA8M2-gsCEEkCenWXcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s_4tWHO741a1C8k3V8lWnyfwDomaj7E0dOhz1_kFQgls4wG275ROxX4ugSdz1WcG9h4Yc3f6a-hK6qRFrF9v3o7ijK5BG_0e7rv9ae4GaOx7Cq729LnFM0-XxT94MXAgKLrmCSlPK2CvRBvYpQkcyUkHOyS6_jlRV5jg_E0b55Oja1XZab_vCkHNJZdszw1C0MpAPYeGWCtLSl2ruWCFZR2anZcXFgHY0atErItdMeCY18YtBY3GDeB0xtFFUUzptULK3i-trCgoGtvsU_OvGosanjex_Ke2sWhICd3IxOdKABC7iMypTDuRJ9O3fq0Nzbl8f3k0BJhIZC-yjjzp5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
مجریان ویژه برنامه مسابقات جام جهانی 2026 از شبکه معروف TRT SPOR؛ فرکانس شبکه رومیتونید ازماهواره ترکست پیدا کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23120" target="_blank">📅 15:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23119">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYHYFX__p_aRuTAz2_E4GJIPiT5jNSoctzGQxo4u4OcyTHK1xV1bQUxHHPfp8A0h5f-6ZbtqHGwhuy4CeaZLvu3u_5yniyNnl7oTRWlDki0GvdqoE9tHllhVLwxVDFx5JmP7if69T6JBZwm_nvJslNYQS0OL1FsOF-8INFa5F5kYEpvezgnKht64DZtIqDKg5Oqul4OZa9DlRe4TffTDBCgfZ1wkjR7bSppbLgYgPL4MTOWjo-IyUUdBM53PXMyW4jWkyZndiA8RtYuyw5CL2S2aHWff4mtULGnqmrn0l4aAGvJ6QKqqRDKW7V0oJKapxQN8WhSRLJrWXXU4YziOlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام نماینده مجلس؛ یوتیوب و واتساپ تا پایان هفته کامل رفع‌فیلتر خواهند شد. دیگ میمونه اینستاگرام، تلگرام و توییتر؛یعنی یه روزی در آینده نزدیک میرسه این سه تا هم رفع فیلتر بشن؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23119" target="_blank">📅 15:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23118">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BnPr117HKWq1BH1yD51Pv9tfJAPnwkSaaeApF3DSlqgVOdSUBLVAvpESHPH7S4K5nMv-AYOZeA7380bJOshKfkZQLT5ePVktDlHquUu3Brw46_YGgsqKD95fJDMXLpiaBQBDKpRS5AFrG9GG1dyuqqDrJKF076GHyI_bi5dhTQRqHmHZA4xa3fzoCMKROv-q9NGtPNWI8ICXM5K1sWN9aohKisNPPapdB5CBRU7Ou-OdN8yivPUkCSKIdTLNprq_UBzi0isdKyKA5CWphx1sB0lWMoT9oCeeCpaJgcKSX6zaP0aLoKN_9vJ-WEoGMsAtqoZStdWlSnAd5h8uU2nvHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇩🇪
شهربرلین‌آلمان تازگی‌ها یه مکان برای شنا زده که خانوم‌ها در اون مکان حق پوشیدن سوتین ندارند! همونطوری که مردا سینه هاشون پیداست خانوما هم مجبورند بدون سوتین وارد اونجا بشن و شنا کنند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23118" target="_blank">📅 15:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23117">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYObzJAg4na6Eat1UH4grHKNtnFl-Tyil0fUbWb-NVs9ZR6qxv70fzsU5MNLfe3fN2drAEOlg_q86FwIY6xzc2fdUI3outheqUMa6nJsA3wUC-nrRA_cVzRsr5W26Q2C3pBkyKwOLBEH2pIhaIWVEyAlgU0E5Oypr48pNjkjnpNElm_B8ZVyVHWteCYsHo-_Pt073ufQ8UWA4FW-QMZQ6CPoM3TLVJU468iIQ_8wbECCr6wa6hCDX8VxWssBDA2Ype5_3i26gliTfAldQ4xbIJ8sjAUU5MDjdtr48OybBrxrgw3iR3App8oOamlvIitPRQE8yUvl0EDWsJ3pcwCI9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚪️
🤩
#رسمی؛باشگاه‌اتلتیکومادرید در اقدامی عجیب پیشنهاد 150 میلیون‌یورویی رئال مادرید رو برای جذب خولیان آلوارز رو کرد و اعلام کرد مبلغ رضایت نامه این بازیکن 550 میلیون یوروعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23117" target="_blank">📅 15:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23116">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEG8FbE0MuzO5Xd2eOq7YaAJmDJbD5z3RnbOJuGlRcbq9VYLMqP36czBz9kP36TSi0aS3mib2tgjvrN3l28WQks05bhz6z3pj7m70i9rGu9Ix4mwTJT_v6H6CbTHabOOjhmVBvz_ERpQ3lI0UrBIbZCbtF9NmkcjqpYiBAYMMWAlzXGPKTFqRmB1DPDVNzlzyOoLJi_Q8Tcena41y-QwIUWB0hPuyAzmC6tSADN9-K99jynyCe8OeX9MpH6X9Ux2ZNOABIcnwlAckr1-pJ55GXEIYLeElaXRfqEYtKtkYNmkICyO6pzMvtHDIP_r7DmolfsPDAmHdQGDHXTGXfFYVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ دیمارتزیو: ژوزه مورینیو سرمربی رئال مادرید از پرز خواسته از بین یوشکو گواردیول، ریکاردو کالافیوری و نیکو اشلوتربک‌آلمانی دومدافع رو برای فصل بعد به خدمت بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23116" target="_blank">📅 14:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23115">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFl9NDIHWIhct2Wf6hpN-3Rj3NMxh24GHs0oXeCOd3xJRcDjTpQA1DsrW24btEWMXp9ozszb_Futslv7ezr2EV8Wg1PUn5z1v9PhWWxOt3URIkZd2Ou6SAjwqBIUFqZ81-NIkOqfwRxxW6_LljMcubd9nbMRq3V-AYKBBtiG2IA9WOfh9iTmSwXHJvRzjU0orYX1UdJafimFdVqXj0IwP4qLNy1rtei44-v6r8oeaKVn009tFwUKLP37uexUP8oFRchDSAzAvbbFGt28M-VACVHkGhRGh3W5OtPDjJiuoEgJqN_4Tc3fWiKgODTcyfowukAlP4UznFcQihdeLO5BkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌مارکا: بارسا تصمیم‌گرفته‌که‌بند فسخ قرار داد30میلیون‌یورویی‌مارکوس‌رشفورد رو فعال نکنه. بارسلونا به سران منچستر یونایتد اطلاع داده برای خرید رشفورد نهایتا 15 میلیون یورو هزینه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23115" target="_blank">📅 14:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23114">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJbBEzitU0kNFBaKAobTb2LPAc_OCe8M6Fy2wc14CenPnTL0oqPLtfyYa3qyRtQhn8s56V2sl7lzxHi9OIrEsk7X2W9urJRUnZo9wEYHL7HofnsoPietG7DWIpz2QTZ7VlwAe1UIDtrlWE5FTq2azpjmLaSAZF5z5A8qb3m1N4aooeTAXrbJeW55c0YgYCaoAdF3Lx_SnKBOKyPwaX37D8BQMzYmZuf0uViz2e6QWswHoty83_v70Vyj6qHLAYd_qMmL5tiaCumBnI_r16q4nBB_-ijS2-nauxzHcgJIlW7htuTgJyQ-yv0TjhPGGz_rnWMlgHfycepqX_4u1tQPoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ ایجنت محمد جواد حسین نژاد به باشگاه‌استقلال اعلام‌کرده‌مبلغ 1.5 الی 2 میلیون دلار برای رضایت‌نامه حسین‌نژاد کنار بگذارند. خودِ حسین نژاد موافقت خود را با عقد قرار داد سه ساله با آبی پوشان پایتخت در این تابستان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23114" target="_blank">📅 14:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23113">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b4b886447.mp4?token=YR6ac_Aw9on4QcSyQ_U4OWGa9RiVFyRRNi1dFCyti_mJ0YFWnKPMrzqPK0NEwhakoMuGx-yXkI5ApZEH8WwUsJyB3Ee4Y5r0xq-GLDPl2v1awM1k7eyMhmKe1Xc7AHiIvyInPjj6xlaQ0m9--QfqSP4Ftqu1DxqxgaCNYTapCRw_Kv8b4m8-YhhWVCdPmhm4zRJ7YHVb9aOnBeMmfSFBOEyZH2f4HWQjLHHzXRuFB0C_h0IGXVlGLANtbMlyDJKlrayW2Cklu7_H4RhKYe-BX1UVufXsgD7Mqo4ZYM1CeeoqwQQF0wailflXTtGj62yLOqreNXaZ_7WiHMSFU9gPnoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b4b886447.mp4?token=YR6ac_Aw9on4QcSyQ_U4OWGa9RiVFyRRNi1dFCyti_mJ0YFWnKPMrzqPK0NEwhakoMuGx-yXkI5ApZEH8WwUsJyB3Ee4Y5r0xq-GLDPl2v1awM1k7eyMhmKe1Xc7AHiIvyInPjj6xlaQ0m9--QfqSP4Ftqu1DxqxgaCNYTapCRw_Kv8b4m8-YhhWVCdPmhm4zRJ7YHVb9aOnBeMmfSFBOEyZH2f4HWQjLHHzXRuFB0C_h0IGXVlGLANtbMlyDJKlrayW2Cklu7_H4RhKYe-BX1UVufXsgD7Mqo4ZYM1CeeoqwQQF0wailflXTtGj62yLOqreNXaZ_7WiHMSFU9gPnoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اسپید یوتیوبر معروف رفته‌سرتمرین تیم برزیل؛ بهش میگن شوت بزن اگ گلش نکردی باید شنا بری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23113" target="_blank">📅 13:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23112">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQr26gUg-m8NbQyJRNLpOfdkwUuXNI2Wb23o85pHY4D6wa520a91_vq6NOT0jmki32EpUOabXnMiXfbq1WPNgI6_aN8jXWomteZUx3jHQoWC-3McmNdhQS6s7hyrOazD9jdThfjynoSR70-2M6WKbgnlZtyGznkzXD9CbrUNPooX1tzC03IrWx5yQvxe3Gh4dPz-ZpnBOouxupBsXVryfrIQsI6MDhxhnlvAQk1QBSmPLlE_CYQSHeGoSI-hz_Xcsa5yJg6oKeigdCadwQ_uNDvVtxsgwW3ZcklALXR2Rk1xwLDYJfKcioq8VX0hwo_nNkp8G4ca9FWj3oxF4CCyGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌مارکا: بارسا تصمیم‌گرفته‌که‌بند فسخ قرار داد30میلیون‌یورویی‌مارکوس‌رشفورد رو فعال نکنه. بارسلونا به سران منچستر یونایتد اطلاع داده برای خرید رشفورد نهایتا 15 میلیون یورو هزینه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23112" target="_blank">📅 13:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23111">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYEbCSXajTcFR7nzDZ3Ygk04qkxfcgylbOWbtILRZhYuXkkzUy5A8u66FHKxVoGuwnZByArWCSZrhkYjYZK7IKFrEE9Vr4DJfQos28-lNjS3m7dJnnpPaTka9n0tUYbx9NX5-5-sOzfjSRgfS7Rlb_h2TPVy9ENaHTv3thmlPKQMP_J0DWbsasAjj9rN3X5QtP5PqqyUui22Wf2LTifFkZB6NhYtCuOGoQuivXuj8JdcNLs8GxAOblW_r0DQKFe5_zrZCUJ9rsMXRH_YR3gaeCMp86B6eU2xalhBE138cLOLpTKLT9CpK5-gq_8ybnO2Dj9UXTBGNUW3q6sdUXtLqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|بارسا آمادس که ۱۳ میلیون یورو بابت فعال کردن بند فسخ قرار داد رشفورد به منچستریونایتد پرداخت‌کنه اما شیاطین سرخ مبلغ ۲۲ میلیون یورو برای فروش رشفورد میخواهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23111" target="_blank">📅 13:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23110">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc9f0297d3.mp4?token=Kyu7V3LK6wSn_UApc4aqkScMOHiTm0mfMKCwLseWStBPwBb1US6K_JuXk8Z2uOWWJVVCSt2zTQw0UlTPMmLLb0lg8G_OxUBRxcD1rI32MlEi7ZQtrHw6J9uW73sdUD0TqQI2X7zkbC9hwu6hGiqBsfz9p5OMc8uRfKmAtGVoHhiqoHchULvQLNHkRZg2IvyCXxnRx51zPNhxji15zNee-LYcWhwxjcO8Yer6dnFaSQvOQ5HQQ5NSPDquhb-cmwqS7w0x50Gp0TCCPzTU73beFdN5JOVkTGPotigYmRYCFqPs8VN5wx3kJX1QPcVQQv_09_2VWQgQALs-hIQ1kwruaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc9f0297d3.mp4?token=Kyu7V3LK6wSn_UApc4aqkScMOHiTm0mfMKCwLseWStBPwBb1US6K_JuXk8Z2uOWWJVVCSt2zTQw0UlTPMmLLb0lg8G_OxUBRxcD1rI32MlEi7ZQtrHw6J9uW73sdUD0TqQI2X7zkbC9hwu6hGiqBsfz9p5OMc8uRfKmAtGVoHhiqoHchULvQLNHkRZg2IvyCXxnRx51zPNhxji15zNee-LYcWhwxjcO8Yer6dnFaSQvOQ5HQQ5NSPDquhb-cmwqS7w0x50Gp0TCCPzTU73beFdN5JOVkTGPotigYmRYCFqPs8VN5wx3kJX1QPcVQQv_09_2VWQgQALs-hIQ1kwruaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علیرضابیرانوند گلرتیم‌قلعه‌نویی‌وقتی میبینه باید مقابل دوکو،دیبروین،صلاح و مرموش کلین‌شیت کنه:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23110" target="_blank">📅 13:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23109">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHlVIyB7Q7oGvRCeIwzV_JyqeS1OswSxRq66LuAYw8MsuMRef5BBQ3fr204-0UrhYQis1hm0SOv4rA_OpI2OkhynxQ2PLsHcgS3zF3k5G5QnnZE00kvDRCV8B50m1jLhPW1HIMqiWL--mGG64welWjKAWmtbCAp-fuNydZKXTibQvySYJ7ZwtSlnM4OU7Wz--nu6A425U0ULQ_L8dDtwPYcJYUuJx6elzTfjmTS7Y0KltaXoUP937E4yRA51GZQFpdyMSfwJTr5BS_WAIPFDY6Au9P5e7nMRkk_S3285PpNVfZqb0Q8Jcwt9lVvbvd59lP_R9HHngs2OyO7xOmMtLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
دیمارتزیو: باشگاه رئال‌مادریدمذاکرات خود رابا باشگاه آرسنال برای‌جذب ریکاردو کالافیوری آغاز کرده. کالافیوری خودش برای عقد قرار دادی 5 ساله با کهکشانی ها با پرز به توافق نهایی رسیده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/23109" target="_blank">📅 13:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23106">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJ8ff-HnpEn2OFS-NzrX-WJdP4-RVQTr_f5vJkVoad-Vqi5GylgDs7JHKmuYox-eErapKBSLT45YNg3G6966oWdvNbMvN3LTHO8jF8xpL5WxP3PHPSTL0QpiisKEP__kUbWBh-7nWSpL4-arAoaXAJGnAIbB7_iVCLPTwXlhS0fckM8JBrccLEv8TWVoNWQ0tHeEDl6inqBomaN9ZkdEyPI84qi9rZYxxbgW9m8aTpFocigeygMJ7PLV-N92GYABaCvzBWHsy9Ym1ZHKP5wdwVPRAsp9iEZ49cVWp1B5HGJegNH8ydzb8rsaVrPVxQ4IL9G8RWR0VnLdunnLdx9txw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرداشب و پس‌فرداشب‌ازلیست دقیق ورودی و خروجی‌هردوباشگاه‌پرسپولیس و استقلال رونمایی خواهیم کرد. اینکه‌این‌مدت کامل همه چی رو نگفتیم بخاطر این‌بودکه ویو کانال برگرده بروال طبق و همه رفقا آنلاین شن. فرداشب از لیست باشگاه پرسپولیس رونمایی میکنیم. پس‌فرداشب‌هم‌بازیکنانی‌که…</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/23106" target="_blank">📅 12:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23105">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xn37UeC1PtPnsBznLaz5nHnHeRKOHWrRq2BY3CQdp6uLlF0PhfJ6JBuY_aYzs_VruWUy9h3JF1n-XfbnpUTBvDQMnYM6RC2VNC6XAaUn4NpRXaHrssCM_7DD-hd9UNomBqunDHQ6feU1OfsAfpL14_7yMKdK2ax6HN9cDuITR8wDXqib39sMcp8MnJUPrYgqlZhSHqT1nR3BRaqP20DLRYBCsypHplPGuw9It9O46Qh46fgnN4imcXWfxEKn4RuNPzTp_entKySxYIa1Ut5ZZrq_mX2cz1knbnksf8z3UZaBNbTgnKpVPWm9hlDbZCtaFkRSWNz2wTxrf3AYW7Bsew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23105" target="_blank">📅 12:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23103">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cRm6F_pfDXK8LZX_GEGv55F3MawhrhH0TWK3InPrhXSGUwXYgkfalbH10NowKM0GzJbb7vsobPqz90CK3uHQtMy75D3F5O2oiUV7nN_Z-f5xsVgXZPEHWxL0GPVZgbty-a3L0vL-cDEf110IR-beqb32Y52FLagchOLjOFIeExGEWdumjYUsae-YIc1xxSD2dNMiP1bTYKXbF72C6R0nz7BM6CfgjsWz_2ephlIG1eHzz7J8r6MsvETf7Ire5BONfMNBQevsWmOfqCANE8uJ_dD9elwFF78o3Ph-iC67dUfD6sqbzZU7v2BYC-pV3v4WWvftH4pc_jBh1YNupc5_Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ugvWvBNpconc3_AIy_DYjuum_UVmPPhiSq5fXWO1tYgWW7-EcKJg0Fb1-Ng7Pfc6XomQIsxEr44WE53AGHlBoohsoWHctV2GRdGtAiezVaxIUHVjgtCvdGknpLiQaESxIPqToTLaURDn2BWKKnmAxUbUMVLpij3B8fPtNExGwQv2XnguLtbw5Vwg-iV9Dpvb3lxzmkKVLMWkC3SXkf8uDn9j_B5ozC1FuYc7ho-3lNoS_LILEFqsXg9JJRxX0llAzyPwSHhfFM_0-cPKnmEO658ilPGYHlDNaj1mdef5_yX9dyXsHBEfIMwYZsSWp31qBnB9NNUIi5K8FhOP8Lmiyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23103" target="_blank">📅 11:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23102">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FwBGyXgtkqVk85xYCq4x8Xl8XerhURSdeceQ2wdJ_CBD5nUXSdB0Lm49ix4kkjsAkOMg3I1jfhYUOIxh2lepMxoxGWnvzuhnmfD-cE6o9sm-SB3l0RF1h3m7fY8rAnSlC0aIKbqvaumczOrFbXK3bitFps4A0rbazP5Pus71wYq0EdXNx1YBf9AHwC9wmU5NUWsdhQgUVbsLXjA3WJUlQsuWahK0RJiRz0redp2vLXWRBbvMFgVbTU9fVryKOps5tKjghD99UsSeadOrhgu8E0yxDkSGkE4st72ohu6vchIyhBoqaOU98wlTvvB_5bpeESzhn-3h5mbzA-W4vtIW0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
آب پاک ناصر الخلیفی مالک تیم پاری سن ژرمن روی‌دست‌مشتریان‌ویتینیا و ژائو نوس: این‌دو ستاره رو به هیچ باشگاهی با هیچ رقمی نخواهم داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23102" target="_blank">📅 10:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23101">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRqLUUlrG2gNk20tV6ZIQCfIobtJMvJUV1RWcvJDGbPMBibv-fu-sCYvzw7DzLWjHsULwconpw0HpKvvbjSYm3meSf3tVzFaL6jM1m_LrHkNl3-J-oZCkPHZjHVuv-_z-XyaH_fmW1By8TWMOxOQH5QW2pJhI5sFD2c2AWEM84BHN_CACz-CZ4yyxLT1e7jaMyCC3Ima5nhKjBadZQ7rwbZS3xU3-M2Y-_yGdM2pDhQObxXjdRQxVTELVxeQcNmN0HKoPQzsdCTgrrt1voyFDV2yHGukPF_vzXZbC_GBja1YM9OOANC_pMRVnWJu9TfeIEMyBuU0XYCiscJquisdJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دنیل گرا مدافع‌تیم‌پرسپولیس با دریافت چهارمین کارت زرد خود، دیدار مقابل ذوب‌آهن را از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23101" target="_blank">📅 10:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23100">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86dbb1bcb5.mp4?token=p4NS020QJw_OXqpk84ViUny5iGuwH1_y_ASS7ov6eG0UhH4nLOlWVsmO4N4LTLynEeVyw0yeCGmf4Noxsvdl7HgR-DVrvoAc0u8aY9Ri_RkudvimoKkjVcvWAePavNk6tL8FVxew_0ktmzo9urzeiYp3I1AxD7JyImeyWigNCn86A98wu9SVRDxZtggIjYJXPMqNzry6RfHIfdghV8wu-LtGgm34Nb-lCI91yc-TdxPc41Oh2n3S_3r17Ho8n5k4bgU5sikzgpRy0T3GFEHTJWAD4UFCiajoZ4xSRDHdL0LT5KemZCSv2iEyYiRnKfLLnkv1sr0oqRsJ4aQnx2dqaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86dbb1bcb5.mp4?token=p4NS020QJw_OXqpk84ViUny5iGuwH1_y_ASS7ov6eG0UhH4nLOlWVsmO4N4LTLynEeVyw0yeCGmf4Noxsvdl7HgR-DVrvoAc0u8aY9Ri_RkudvimoKkjVcvWAePavNk6tL8FVxew_0ktmzo9urzeiYp3I1AxD7JyImeyWigNCn86A98wu9SVRDxZtggIjYJXPMqNzry6RfHIfdghV8wu-LtGgm34Nb-lCI91yc-TdxPc41Oh2n3S_3r17Ho8n5k4bgU5sikzgpRy0T3GFEHTJWAD4UFCiajoZ4xSRDHdL0LT5KemZCSv2iEyYiRnKfLLnkv1sr0oqRsJ4aQnx2dqaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
درجام‌جهانی 2018، آلمان، مدافع عنوان قهرمانی داشت درآستانه حذف قرارمیگرفت و در حالی که 10 نفره بودن کروس دردقیقه 95 این شاهکارو خلق کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23100" target="_blank">📅 10:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23099">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇧🇷
👤
به‌مناسبت‌بازگشت نیمار به تیم ملی برزیل؛
ویدیویی ببینید از شاهکار‌های دیدنی او در سلسائو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23099" target="_blank">📅 09:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23098">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OuMpPVxMA7nMs7BE9aG1BOWyguKyiDEuKA0waOqNgB2JPyU95v1ir1ja0VJoLFPeVuvjFENmM2UEspa5AMbeZJ30vunfkaUhPp4zy6qHMC7TpbnfFhlSLhQ2WquoUFufij5MK_xnf_RROyAQzrwVf1rmxblPVoBw-wXqWHIx0X0olfB7RQ5_Tuzxh8WsVsWcO4L62ijEpwiE7wYlTxIPSCclO8D1oT0_2V4EpbssylWgmHmHmj_I9Wci97Bc8tBpL0nFmulm7pGKAtC8dsRc_IJ-SM21Gxh2nuKEvw3ya9T04ldyLYxYjhm7e8PgtwSSGNGI8Sd3MzFGj2PaHTTwGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تمامی جوایز تیم‌ های ملی در رقابت‌‌ های جام جهانی 2026؛ قهرمان 50 میلیون دلار میگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23098" target="_blank">📅 09:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23097">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jk8gOp2nx6i8H6fulFkwo3u9kb5lKsM_XkPIdG7SRt0raNSxYZ0TGdC5Jis7tnZJlslV7Ld0rfao5uI9UmM4TepXqDteYbZJ4zfZw7xM-8drTuoNvjsL8QY54hO83dp0BQXKWV0OGwKOsXE2XJ_kPpVrrp0sKNxSvWiOH-6gTGLvQy__pI9cjYNa0ZcM4NRcy2-8tW9cF66OZoMrKvo74DCciO9goEezxezBz6mGoiw9Cum-yhl2PndTOLxh86MQa9qxaQnjeWnrZ420PrdK83WzJz2B7KQWC2KKjoS8hzN6bgnpwU37NhpNdbhk-Py9u3QC7QRNDcn85xA6VVwVtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
فدراسیون‌فوتبال‌ازبکستان:
بعداز MRI مشخص شدمصدومیت ماشاریپوف ازناحیه کمره و این‌بازیکن رباط صلیبی پاره‌نکرده. براساس‌نتایج MRI، مشخص گردید که فتق دیسک بین‌مهره‌ای او عودکرده. بزودی میزان دقیق دوری او از میادین مشخص میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23097" target="_blank">📅 09:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23096">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b8bf04818.mp4?token=FHNZeMqyrkHhlUQzAKb8LQi94xyjudkNdtKBI9kd0ca87jX0yBEO9Ay3o0GsQiSnWyofHnyHX3QfgYs1XEeCXodu20I0w602Lg8NPVThbVzPLX1I_7IQ0lCNsDs9ITjCkZLY_xgHx5BkepmdbRiQUIU-VwM2jifXrXmWJudyzgd8PKN7XySC-PMRCAPCqLqUVL2jK2HvLL5RuH3p4qLLpplQoZZ3qiVyLrwjQE5BS2jACaL0nM2TbcZCfbt6CGraBBSTvIC0XqZB4jHstfGy471n0vGQVUuCJXTylCJGhXR9bKUZzuJ1GE9L4QzYQKe8zfAzGPIMaKCIGUEZ-9vrCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b8bf04818.mp4?token=FHNZeMqyrkHhlUQzAKb8LQi94xyjudkNdtKBI9kd0ca87jX0yBEO9Ay3o0GsQiSnWyofHnyHX3QfgYs1XEeCXodu20I0w602Lg8NPVThbVzPLX1I_7IQ0lCNsDs9ITjCkZLY_xgHx5BkepmdbRiQUIU-VwM2jifXrXmWJudyzgd8PKN7XySC-PMRCAPCqLqUVL2jK2HvLL5RuH3p4qLLpplQoZZ3qiVyLrwjQE5BS2jACaL0nM2TbcZCfbt6CGraBBSTvIC0XqZB4jHstfGy471n0vGQVUuCJXTylCJGhXR9bKUZzuJ1GE9L4QzYQKe8zfAzGPIMaKCIGUEZ-9vrCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇦🇷
درشب‌پیروزی 3بر0 آرژانتین برابر ایسلند در دیداری دوستانه؛ لیونل مسی کاپیتان آلبی سلسته به این شکل موفق به گلزنی در این مسابقه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23096" target="_blank">📅 09:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23095">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85fc2cb234.mp4?token=fP-WGa2layUe3wJoREg4dbe6rBsssgXYwAho2Pqmi7dHU3Xym0AVqCu64rERDpmxS1agasyjWBfrSpOvXYXQeg76bjSNpu9P6tXSTYSLAdAXuoNXOpNbmQFYWo7RmpzHEF89XWIIR_SYIqwqPHzpiAbZwWHEKuCseNdbpJArHEYyOCKAyhGABZopuZqYm5PG1ud-bySRrzuv38Vkc1tZ1NNgWmykoKUzHMk6ejVpB5HjtyeQSm40Pd3-GQfly1JPm8rUGIqn4MqKnly5WhqL9PHCfYuKqs_yWLPROJZhqloDJ---ur080ArbFG6cjpxuw7XGmPzW1cCiQYCRNGyYaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85fc2cb234.mp4?token=fP-WGa2layUe3wJoREg4dbe6rBsssgXYwAho2Pqmi7dHU3Xym0AVqCu64rERDpmxS1agasyjWBfrSpOvXYXQeg76bjSNpu9P6tXSTYSLAdAXuoNXOpNbmQFYWo7RmpzHEF89XWIIR_SYIqwqPHzpiAbZwWHEKuCseNdbpJArHEYyOCKAyhGABZopuZqYm5PG1ud-bySRrzuv38Vkc1tZ1NNgWmykoKUzHMk6ejVpB5HjtyeQSm40Pd3-GQfly1JPm8rUGIqn4MqKnly5WhqL9PHCfYuKqs_yWLPROJZhqloDJ---ur080ArbFG6cjpxuw7XGmPzW1cCiQYCRNGyYaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحنه‌ هایی دیگر از موزیک ویدئو شیدا مقصود لو همسر ایرانی خوزه مورایس برای جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23095" target="_blank">📅 01:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23092">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mLbv55Du7mC6CBOv9M1Np0Cr9yVOXmDW3xSWbdPVYWCH42Qfqq0L_M_jnYJrPT_ZlIWJKYWdisx7av6c9LDvUIjgfn5BXjKBpw6l1pb-qTlKR9KxwrRqxa8kHL9xmo3cGOWQV6EKtJsuyVFZcjtmZl-9N4-tIXxyyrljfCTEsLWVkHz8oiiEvB-bGGJXg6X914wO-TYqr8i1N0AwR0E1gtSF3omGMwG-2QNO6e4oXO0eRMaFdTwdJOLqtStzCHO1LDIGX0pM391RnRm3zaD11UOEzYQB7yNswNJVl3RjRpnXJy6ENT4qSH0qJxUWNetwbux29eyLlgxup5myCJAK3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nd5emP8xRPEV_orQM_s1PM5dy7TnqOkHhsp0_4NRzLEFZfAHRHd0qgpqigdWxIu-ovG2-ITpnpvPtuZiBWl3sbeHh2hdlkUeDZ500RJHydXE6bOpC46eCTrx270UwMRH4-8m9b-6v_RQVJ5jiWkJtMswpwx0TGk7ufAzsiTwcAO36iJCDa0uuX5FZO3dhA5rPq3OJh4SD_ka6p1fNnH7-EiLOUwPOmvfZOAGY9_4XDVm0gLyNZzOsUUUnDH-u5qXpxORffTR43cHcP6JIT9ZsJdB9a9tYMdzTg2No2CYyRR3uaBsqxTW4aJAo7CWstakEn2kw55eBJ_0SoivTq4fxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
نتیجه تک دیدار دوستانه مهم روز گذشته + برنامه مهم ترین دیدار های دوستانه امروز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23092" target="_blank">📅 01:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23091">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7865bde240.mp4?token=Su_B6c7n1_lPIJ6wP1qoiYY_wOMwjww8QQmMVNymJMix2_r6n9R3Y9WT7s0Yelg8fzX_jweiYlMl2MKvhbp5pluHOTYGfG1MKJbzvOiN9dGSKF8oKaoyT12jgaHxOjtOxzZCbiNJNiGWHpJV0F3yDB0-99_xN4qDtwYHqRjA3ZBG1PwSu7xswEwFaD5IoL5WdNPCj3mzS9IlsCaq4nIEf1VbMEQtUS-gMeaenHbUz-5pFLq9Y7RRqYGiRzDPba9Wna8IJ06sFxadUBd8GFQWHfJvkzS_ksUyYOkQZeii_vne-bghTQDlR9dBwD8q0UZleTD6unQSfM-XUvDJSf8Pww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7865bde240.mp4?token=Su_B6c7n1_lPIJ6wP1qoiYY_wOMwjww8QQmMVNymJMix2_r6n9R3Y9WT7s0Yelg8fzX_jweiYlMl2MKvhbp5pluHOTYGfG1MKJbzvOiN9dGSKF8oKaoyT12jgaHxOjtOxzZCbiNJNiGWHpJV0F3yDB0-99_xN4qDtwYHqRjA3ZBG1PwSu7xswEwFaD5IoL5WdNPCj3mzS9IlsCaq4nIEf1VbMEQtUS-gMeaenHbUz-5pFLq9Y7RRqYGiRzDPba9Wna8IJ06sFxadUBd8GFQWHfJvkzS_ksUyYOkQZeii_vne-bghTQDlR9dBwD8q0UZleTD6unQSfM-XUvDJSf8Pww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ فیفا امروز صبح به فدراسیون‌ فوتبال اعلام کرده در بازی هفته سوم مقابل تیم ملی مصر؛ شاگردان قلعه نویی باید با بازوبند رنگین کمانی که نشونه حمایت‌از همجنسگراهاست‌واردزمین شوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23091" target="_blank">📅 00:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23089">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SnpF2xh9bGXZoGQJrlNteh2k5sDgp0WYTeVMd9ueW2ngroUzOYsii7N9H9cjHgiee0XYDNvLAw3wChPzHRRZIiac5xwLwqq6ENvGFbKl0LlL_WoLEzOVy07dlcTYZ66coHrBBZVd4Q1c_J7UFOBSdTFAXRER6cQgNkqX1zPhudjnDLqsnIzaWbxKbPmDFBnsn25gNVuuNU1DQuUfMt63T60ai2Sn8TRpPZZZSxYtwBhPwArFLl3UA8479-QIN5BG4pu5nP2-EyrYwFM6uKQOX2xdiErQChOcV0ar3yfo8pR9Xx466K5ytwpJwTsANZpX5NQO7woPt4oDZl_yq5yuZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bLU83KhiWYySNlOI_YYnsxBTKVG4xAukYT4-KZe_x0AXABOQtXvzOuiEE6GPX2N43jE7A_KWxT-1E1y3ifpq6GfejP4GRiQhTwDWTYfQ2jDC6zLYhFnTTzrH4dX3bA-wr1py_1-ZVrfYvBC0caXZeCBk45wMEmlWQxFIpWERgMO1SwMJ5TJd8x1j3wYzelOk0WvaoDJVs-AsyCXQOh34hTMmO7S0d5p6JGUOQZx2PVVrLRbhjQByu_fNS3G5--a1BtnqSfQGhgMrsQpwOVpxmyVQug4r_nxujYy-pFgKxvBAeElgM8W2-HK5tPbTDQMUqFj6E0uaKhBZ2w3_A7uL6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
جدول‌باشگاه‌های‌برتر لیگ قهرمانان آسیا بر اساس آخرین امتیازات کسب شده در 10 سال اخیر + پر افتخار ترین‌ تیم‌های این رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23089" target="_blank">📅 00:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23088">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPK1JP87GEKrL785_yD1mui17lesT2SyhQKbFYciyxNksk9c-p-kZwRktfpu_vWc1SikP9Esa_yr7uhFrzJ1S2LvtFXmPREIr-9gT_7I1OgAfpBO_Nz9tdobt-yUt6nNV9cdHixdxDZpTF-v58dF-isVoRAiIDE6VFJXJBPwTHKRpUTxN8ggoUcmIDVGieeYa8pq5BRsD8YcMUD7REo1WawDI8BF1OQ5VJuW3tY_Dz7i-38Qc7-4rRD8ASRLy4hbZqgS2-PAb4iAa2luCaVHG9Uo6xXQpf2xMbylEqwJ7gC17xL7Ie173M5k-bmY458TusyBSrAScP4dzDvREnVNkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ترکیب‌تیم‌منتخب مسن‌ترین بازیکنان رقابت های جام جهانی 2026 آمریکا؛ به احتمال‌زیاد این آخرین جام جهانی این یازده فوق ستاره خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23088" target="_blank">📅 00:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23087">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5366993444.mp4?token=IktSa-XxAGxBFVbH5-9km7pWbvG-hPwi22QwNj8MmAODda9onRBeMjNf0gIC6sc9XMIWJ6n_WxZcyx6eHipqhP1DwA50ocNtcyn-vcqBas3Cdi3-VKdc46ch3A_LyXCOAaeyF0nglGKtX8d2_4-ExQRMDIfmsxtR9npRVb91ArvmBizj9-qsMMXRR3ZH9HxS36O5UAqg5O6N6KRm6BDPwkroJAVzCzdCuR01pg8PmQe4xolPSwIJwkNZLpLyYulcILNRKUAXkXnXggfV9Y7LzG-OSht9v9gT3tXSR2QvMmJvUtloDCOlpHI40ZdE9b4J-f5_dKAb38yRc7GYVvUG7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5366993444.mp4?token=IktSa-XxAGxBFVbH5-9km7pWbvG-hPwi22QwNj8MmAODda9onRBeMjNf0gIC6sc9XMIWJ6n_WxZcyx6eHipqhP1DwA50ocNtcyn-vcqBas3Cdi3-VKdc46ch3A_LyXCOAaeyF0nglGKtX8d2_4-ExQRMDIfmsxtR9npRVb91ArvmBizj9-qsMMXRR3ZH9HxS36O5UAqg5O6N6KRm6BDPwkroJAVzCzdCuR01pg8PmQe4xolPSwIJwkNZLpLyYulcILNRKUAXkXnXggfV9Y7LzG-OSht9v9gT3tXSR2QvMmJvUtloDCOlpHI40ZdE9b4J-f5_dKAb38yRc7GYVvUG7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
جام‌جهانی‌داره شروع میشه اما همچنان با بزرگ‌ ترین غایب رقابت‌ ها؛ تیم‌ ایتالیا با شکست در مرحله پلی‌‌آف مقدماتی جام‌جهانی ۲۰۲۶، برای سومین دوره متوالی حذف شد و در این تورنمنت حضور نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23087" target="_blank">📅 00:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23085">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6NUO1hx0eY3q7RghQ8qQHqAGWTH6emUHSEb1NJP2UMSkziicHrt7FELCPDHcu1sY-D52IehuN24NkZ5XIBVzvcvbK_MvK0mNnRhHsW5tvpr8FxKsVE8U8Ir0yIIPdxLeI-aULdg6N0SiXIQwmomGgCgxs9qeO6hq_G0expOGbHKr-h4WAuwb6arIx1BOX4PA7p4Aq8q6LelpedxHdGdZF4_MpN_g_V6BINOR1S0VWKeL299LQz8Wqs1Jm24L_bV8ZFHlEDc54A2HtVX8a8onJB0Wx4HrXdH7nCUCS6OGmfWHrhzfM4tbde0Ocicv-3aLjj6kK3VmshuJWMja1esOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مصطفی پوردهقان، نماینده مجلس: بعد از رفع فیلتر شدن واتساپ و یوتیوب؛ ما سراغ سایر پلتفرم های فضای مجازی خواهیم رفت. رفع فیلتر شدن اینستاگرام و تلگرام نیز جز برنامه های مجلسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23085" target="_blank">📅 00:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23084">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjN9KlOcvdmGLqqO1fHAPgKlqzTmHjb9RAXahShEEtVvAyMNITWXZgXfOplmiD9PeXKKuWhpfIHbxxY2LtqZnqsfrpLgpzuodS4b2RqaBwR1QTW5O1nzjTRq85P7feLqm1uDckpOtStSWEmcHvjMbSPkevDuEQuxkRTh1Wu-SPjBtzjZqZgyrAwwTwCoNEWz6ycv-lN_RMh8PzYXMI6oIPBSgQm2MxRlKPXCIQ470ZiJHwfNiIm6tUuId1vYKUkpwht7lK6h-FZwYDoVYuLcZOTePEfP7DyWBM_Htb3ZcQMoghGE8EM-z1dSkroA2MqxbQ56Z-HAjQlKnnYb9hXNzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇪🇸
🤩
#تکمیلی؛ نشریه کوپه: پرونده پیوستن خولیان الوارز به رئال‌مادرید بعداز رد شدن آفر 150 میلیون‌یورویی کهکشانی‌ها توسط اتلتیکو بسته شد. حالا بارسا مصمم‌تر از همیشه به دنبال جذب آلوارزه. الوارز بارها به مدیران باشگاه اتلتیکو مادرید اعلام کرده علاقه‌ای به ماندن…</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23084" target="_blank">📅 00:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23083">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igjbFnr1lTnKcByMVl1Y4qDMYeq22Z3P2rMIIOKl9_FwoBqLkC45fc0wwpWDbYSqhC2Z5RnoZ9z9-WJgBaTQUokCnpCvIghAIF5WAYzx8FHaW1UONRQvCIa5h_75iKEXLhjvMRtwvy1f1qqkVjTpZw4ZYR56Crq3cFR9QYYvsfVfBPFYgpRO9sh2GP-BzpWSW_vsSde-G9KLPqLFeYtFgT2bh4geAh5jgU5-YVqxBJSBCDNVutCW7Vh0vWtRnPAb-bK9HtMOnFdKdxdK5bw5smtS54jTb3huFNlcBwvXUsNj_0CuB5ekK3rF0jkBQWJn5zB_8Y-nmfV5R9LlBXgVGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ لازم به گفتنه که نماینده و مدیربرنامه های آریا یوسفی و محمد مهدی محبی ستاره سابق سپاهان و فعلی اتحاد کلبا امارات یک نفر است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23083" target="_blank">📅 23:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23081">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8FJh7KfYXNvhh5_LV4ghWf29DW9wHYCwMQkpiGLRWc1AuCdl87ptJtKxR8acXVhH3EhL5-meKp-s41mjx-5Koo37lYneJYzc5N_vAh4xW6HMWfF-JOuXMmMZeB2C-3FrcMbPteihWp8QtG30FS-koyH2RRbIQbpQ2AYYssH7BbxfE8SzBrjhRu3PfDkNzySfYCP9qbAxTLNO7iaD9HGMYMW6QCQyzqxixo7sxUa9pMlYwxqG2LNGBB_AB36nE4NFGVDOgG39QimEen4wPQUfsIOF9AOJJFdfT5iQFczaZpVs2TOm95ICHXL-yLAzBm1NxELLritCeeHVzPRJJ_ScQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚪️
🤩
#رسمی؛باشگاه‌اتلتیکومادرید در اقدامی عجیب پیشنهاد 150 میلیون‌یورویی رئال مادرید رو برای جذب خولیان آلوارز رو کرد و اعلام کرد مبلغ رضایت نامه این بازیکن 550 میلیون یوروعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/23081" target="_blank">📅 22:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23080">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdrB6uoVoJ6ynWhMIXnuiaENF-KlqaD_5fKwbRXuvMR3nOcvIyMeUa4MM7bEu-Ay7Hf7l1qmFfItWkFTTPEheJRcgrfM41QqtwsJqwvb0iDC_o83BY0jqtuchRL35s7lvZZgcY4LB2YSzPOUm4yuhvGo_5SVH--1yOm4_Be1WOl3zNuKKt1CDuRMrgYqCxbd0Q4_gAomap80_-bw_iezHLKJ0Fc424BoKnbJCQbfFWAIZozIXLnktKnoBG7kurDQh1lWTzxsvHuMJ1ihpvTta1CxPe_bIIRXoHVdrVIuZINPJGl99Ck7hJA5JvYPFpQHrV4pfqvyhlrEMbGw4XvV1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق‌اخباردریافتی‌رسانه پرشیانا؛ مدیربرنامه های آریا یوسفی امروز عصر جلسه‌ای دو ساعته با پیمان‌حدادی مدیرعامل باشگاه پرسپولیس داشته تا شرایط جذب این بازیکن رو برسی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23080" target="_blank">📅 22:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23078">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gsVn1cCedPPSPZFFYdSxZDFYmIsWrNbbpsSz86Inwu7ztosY2T5tEHN3LcoGYYk5DQ6O3abQNUzYQUY0ulEyFs1WL6UmpklAevwVub1uDYVROMhOBYYRzQYh-YCHFYKfLE8bNHNeAlMbzkhzNd9G6GsfJY2vZIeLZkYJ3odTdV98kogvHeJKF6XYK5kKKe_nJziCtvUFLgyfykNxRnW2lGPSC2QQZow1JwP77XR-lftsHxtZWTrmv0C-467Od9SgYBXR1PLukaTcvieB8ABt7gmAUNMC7nwsPZXiorLFvBs53pzigzTzIe_6vgjhHFeCAJ2Jy_5wWNg3h8jz-6pHxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pGf_QSnlcyc2dBH6GtZCWjlJm4iuMNomlMM5md5IdrCQY5Om2ImgBiSnB_O-Jz1W-I9zLG2lReSNPMRHJDKvyimy3bzLNFq3FKlA9FTRF3xx-gXciYvf_nNeSArKzUkayb6C22BK5mrIRgWvuyx5DI6u6fGT2xVakq2geFn5TKU0DeIKFXvLBwNcaJE5k4fEBBHB3BQ8s-wjqH4fWOQ5S2Ah1PN3-jo2MT2XU8h6nFY25yfVLpSF0mifP54yLP80XaEbHm7O7xv-LVWIlv_ILFotNZpfkkk0PC6x3xQg2ncghrMWRFp0-p3aHQOrySR25LpxLzrb16Beo4SsMBoh4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
👤
نادیا خمز دختر پاکو خمز اسپانیایی: علی رغم‌علاقه‌ام به تیم‌ملی‌اسپانیا؛ اما بخاطر اینکه کریس رونالدو رو به شدت دوست دارم امیدوارم پرتغال قهرمان جام جهانی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23078" target="_blank">📅 22:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23077">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRFJXFZep54hBDyqLaoJIh1zDG51D1M5P1rEC910Q7nbQS_ajY_H26kkQcosVvY-9I0hmHvkXiB7jpuNK1pmLrfQG_82nDNKmmUfyaONe3inoUWZ2H237QQzYVuTMatezlQbaQ8S5ZCIdC-kvSWLXYgzUt0qZbC0upAKBDDYR35XZTVeBLw5ua2FFeGIRAbe35lpFdOw67eq6Qf5OAjOXj4MyIRCOLPV8Ju7nThd3wiaipJKKIBm79-Dzj4mwc_EDL0_kNpc2A9DtnuFzc3Gh4YOn6WCJuWLssOQPdvT9ZyQ1K3-kTNZbgUcPhk0MPKMn1bK0ocGtO_Abu_YMpA6Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی #اختصاصی_پرشیانا؛ آریا یوسفی مدافع راست سپاهان در بین نزدیکان و بستگان خود گفته که بعداز جام جهانی یا لژیونر خواهم شد یا به پیشنهاد باشگاه پرسپولیس پاسخ مثبت میدهم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23077" target="_blank">📅 21:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23076">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zu21C1XysgY9a9ofZZWaT1MrY2fPRwtJDTf7CUdqra9UpLZXHX1j_rn2gOaT5V5Gg4gI769dZO_H6TCdBNPIIG1VYbqeo7t9h56zgzrGDsVs1a1nQ9gje6bcC8OP-Wagel6jhFJ3AQqDknwVMHTkx7DmiHDuNijR5738Q0iIEV6rSplzlPkCxH406Sv5W-BjKUBPCguT3XlcF0A_d9dsNl-s1rjPPuUHLrsYNZh_A41izFfLc7Z44R84LL9jf7Vu9IVglvTk9WgB-CCc4OPtypJzZOqwcy13BNHpu0IhWDKeu0JKvNyzdYUdzKStYLAxhgpYhpWekK3QhbeGJNmDkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ علی نظری جویباری مسئول‌نقل‌وانتقالات استقلال با مدیربرنامه های محمد جواد حسین نژاد مذاکرات خود را شروع کرده تا بعد از باز شدن پنجره این انتقال رو بالاخره بعددوسال نهایی کنه و حسین نژاد آبی‌پوش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23076" target="_blank">📅 21:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23075">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUrsdUtC2-FA3qiCXFIx9K_045iGCq97PLabumcOgLIZdJo-k-jBC3EpG1BV8quUaTXGPYA65Y6AJLdAdAudjt6SSBYnpMedhF1Fyu2ojCWWBCWNAT4JzXeflLxW3LPczAHgos2mK6iYrI5IIFxa0tYPRNdvlIoskiSqoLI6iV388F0y9_R_mhSn5nHa78t24i9PhBxyRlS61_Nk63izAT43WJe9qp4PcvGjY8yDRMNRVVwWfFOc004NWktcfnJDqpaZLZJW15k8zQt-5wM9-qZmqpcZ1dN7UxKDTdC4hcHfg4Tcfq7g-cSeL46m9wy65w5FV37AJWZNAj_wZ_8BgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باتوجه به اینکه هوا داره روز به روز گرم و گرم تر میشه این جند مورد رو سعی کنید رعایت کنید تا همیشه خوش‌بو و تمیز باشید. در کنار اخبار فوتبالی چیزایی که بدونم مفیده رو براتون مبزارم
😂
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23075" target="_blank">📅 21:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23074">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGY_KtrFxAI8fZ_1UYAjKYN2OMFrW7O-IXut5kCGBa7EpImRf0z350a7uyaHm_om5xMQ5vupGkL4BGEshI2hWqlfDAbwVyMjcKa7uJqz871IcikDWhesVgl3UvI65wPUevE7kyNF8RjmwDhu2tNtsddQj69Kdq0WBu4KN1YBMClzzBFl_vUDFrY8wrH25ZhGl0onor1N_L5TXoNiHtAQ0SPtJyDBvOWyNlITn97xCfdPscyOscbgT1OJQFtHmPQR7k5CmVyOc1mjxq_BBIbICnhdRXK40auoitt3yFNTs7W2AwTfgh91jfIfe6IfWKt0VvKn_VNK-k-NKCAC36gdVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ قطعا یکی از این سه گزینه مدنظر فلورنتینو پرز خواهد بود. پرز گفته پستش هافبک یا مهاجمه. گفته‌بازیکن‌بسیار ارزنده‌ایه که مثل رونالدو، کاکا، فیگو ماندگار خواهد شد... یه درصد تصور کنید که‌ خولیان آلوارز رو هایجک‌کنه و 150 میلیون یورو به اتلتیکو مادرید…</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23074" target="_blank">📅 21:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23073">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCzQPyTnAb-MM-98_gaeEKIeyB3F8GB9RhzfZrRWGSWwQbAQ_kLMtMHSGFHzWn5x4VRqZhAb4nbOScewFNOxivETbsVfX5sPKq5J7rxwK3yVbebWzsXqiCEPUEQAteluRPjNkDMga7nahBx6Vs0Yj7e2tYObswF4t8p5BOCJczQ_n1maL0ANygtDjWuX_W_aTN3rhiv2OUXyhbNDC69ijpjMEm4s7oVLU8D6PK-T4tdpBUQ-JrHNphU0HN4wEEdq2O7byVWp39lfU9diHJx89jm9vbMdy1CbjHZQudmo6-kT41G1Cipd4WT9-TQvzCXVTEF2x0HuNhxi_7O_dZLJ9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فوری؛اسکای‌اسپورت: رئال مادرید امروز شرایط خولیان آلوارز رو از اتلتیکومادرید جویا شد. اتلتیکومادرید اعلام کرده هرباشگاهی 150 میلیون یورو پرداخت‌کنه رضایت‌نامه آلوارز روصادر میکنه.
‼️
فلورنتینو گفته دوتا ستاره 150 میلیون یورویی میخواهدجذب‌کنه.مایکل‌اولیسه…</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23073" target="_blank">📅 20:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23072">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZUnfUlbGNf44VrKc0q63MRdJq7Ei8MauOJsls5zmQRqk_Lakb-JEUqhqQ_P48C6n9m7iYbslNs5PdEmX7WkXe_VuFQmYSJnqUCIjoq9tALw2pGfVdkvdLVZwc9A2vTRK1MAv1Cavy0NI2T2lBkzp_JjWDsCcT-w5fVoflU4Rw9h94f1l7WdPoCsZ3WbIDVW5iS3ishjyb1U1AQ8ycQCNxM4NfYQq-K6mB2WNRpD98nanIQ097x_ge8fAIRpF4q7y0yDuSUBpnVGPq-47OB60WgyyCdDo7b9vKITfRWYACR3T1cMWHsXsR7Y-59A86UCyGY4mpsNEIR6vIP9B0myYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
7 زوج‌برادر درجام‌جهانی2026؛ دراین‌دوره جام جهانی 7 جفت برادر درتیم‌های‌مختلف حضور دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23072" target="_blank">📅 20:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23071">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/993bfd4bf7.mp4?token=AlADOEoxhHwQoXvMVCi1pMfuIIVQwRkrnY2ntbI8-fWuIZO-FwfmVgLomQJFwOoA7yv2NWNa7P0nf2XW5GInwF3yTJXT42OuDrLo6SNK3RpBVOlkNXo_4e4k-vU5ofJ1Gb3H2Dv-4bc8V4z_vE4fewnnO7Ba5pGyN-E01K3eQdvjSlysRUfqyUIiU9IluJgnnuGAwqIruF380faNA_GkAFb7Syrm0KZ0QzOVGqJbd6vbCxxF-0QpQM-lageXWJG7I5PRxpv5inKMz8mrg_boHAjejIo7YZUklWYNj885g7pj6T09M1A3Zyq0fU6DFBGkHgRyqYrU71cF07FjxmOtmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/993bfd4bf7.mp4?token=AlADOEoxhHwQoXvMVCi1pMfuIIVQwRkrnY2ntbI8-fWuIZO-FwfmVgLomQJFwOoA7yv2NWNa7P0nf2XW5GInwF3yTJXT42OuDrLo6SNK3RpBVOlkNXo_4e4k-vU5ofJ1Gb3H2Dv-4bc8V4z_vE4fewnnO7Ba5pGyN-E01K3eQdvjSlysRUfqyUIiU9IluJgnnuGAwqIruF380faNA_GkAFb7Syrm0KZ0QzOVGqJbd6vbCxxF-0QpQM-lageXWJG7I5PRxpv5inKMz8mrg_boHAjejIo7YZUklWYNj885g7pj6T09M1A3Zyq0fU6DFBGkHgRyqYrU71cF07FjxmOtmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
سوپرگل استثنایی کریس رونالدو به الخلیج بعنوان بهترین‌گل‌این‌فصل لیگ‌عربستان انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23071" target="_blank">📅 20:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23070">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSEKEsgy1Ut-EueM8g1a8sHO0pITQby8fr43iDE0SCtOyJsyVqD8ETxQ_mkuPFAxc7E4t6WGux7dlqK2YJIhWqGZ79nDyvF31SFwK8EvrqSThQNnaUhSneoVFeCoNsJ8fh1tEXcX_ovKKmYZu540VszQFbzGoirlhwV8bkSguEA9Z7Q7lNm2eKyi2A9T-_dnpLfUwXg3qCaW47aItWjOFH1VGuFV7gz8ZAThAbtY8Rz1eOangN2mOyBKw4Wt7-fkkstQnzRsrgb_NBRtfXmBe91iBTZiJue7-luF-KBco-OOjbH34He03jz54hL14RG4TZqFPcxsoTmszxIHWV5Pug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فابریزیو رومانو: برناردو سیلوا ستاره‌پرتغالی به یک باره‌نظرش رو تغییر داده و حالا هم میخواد برای انتخاب باشگاه بعدیش تا بعداز جام‌جهانی صبر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23070" target="_blank">📅 19:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23069">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bd17cf6e0.mp4?token=UaATewolDQoYR6MO9bE1xAiWMHJF550SHRw9KwJibAebi9Y4jN3Eo__UB38TeV2MHQLRRJ38rcAB7wWp4c5_Ke0YQ0SEwNclDzYs4tEsJVipjdCZmqW59wWkiD4-DisbUj7RbmzmhTS3PYEOc0yTB9RAShfbd6L5C_CfCgELGOkfT76B-rlpUY6Z0lsomqrEVhlHW7NBx9dUW-QwI1-wl-Vwo_61OWdfadKSWtAjqNAHQKZnXzcm0Okfll0MHGEtpYFKZVxbTnHrpif3ZpEczDf5jSR1ta_AvbGfTB-RPpT5fv_Ghv-yHdN9FvOdgTO_VVKZqJTxTJch5HdPQL-r8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bd17cf6e0.mp4?token=UaATewolDQoYR6MO9bE1xAiWMHJF550SHRw9KwJibAebi9Y4jN3Eo__UB38TeV2MHQLRRJ38rcAB7wWp4c5_Ke0YQ0SEwNclDzYs4tEsJVipjdCZmqW59wWkiD4-DisbUj7RbmzmhTS3PYEOc0yTB9RAShfbd6L5C_CfCgELGOkfT76B-rlpUY6Z0lsomqrEVhlHW7NBx9dUW-QwI1-wl-Vwo_61OWdfadKSWtAjqNAHQKZnXzcm0Okfll0MHGEtpYFKZVxbTnHrpif3ZpEczDf5jSR1ta_AvbGfTB-RPpT5fv_Ghv-yHdN9FvOdgTO_VVKZqJTxTJch5HdPQL-r8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
#فکت‌تلخ؛ مردم‌ایران تنها مردم دنیا هستن که‌موقع جنگ‌بیشتر از اینکه استرس جنگ رو داشته باشن استرس قطع‌شدن اینترنت بین‌الملل رو دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23069" target="_blank">📅 19:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23068">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FvjOHErwMsnvVtZb7nsIB0TOHNb-rHsLqVnqIupvOfbcOUAfqzSn26d0h2tp8dQSHzNL2xWCEUmBp0SvTMh4RZudn0FH0vkHTiMMoaAOx8_-unHC6dlQdqijPVZ0p-xaMYEkQPaKL65QdFYID1anDAGAaWfuQy7qMjxLad64eX7uFC3bGiHIfUd_cRmNLEg8lITZJhandKX_Ubc_naFrFz_kyIWBV9fN_kMqOg6o980VlsEW16TIxdmyVHZMHV_H1-SIYPJubNG4YaBQ_SBbtDh6Pb1ssypBijqB5lq9ZTrZWvtuDTlVulzHKkSIS9EtwxaceCEF3IlJwMcFelvuYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
🇵🇹
برناردو سیلوا: فکر می‌کنم قهرمانی در جام‌جهانی‌پایان‌بی‌نظیری‌ برای دوران حرفه‌ای کریس رونالدو خواهد بود؛ رونالدو همیشه‌سخت‌‌کوش‌‌ترین بازیکنیه که می‌شناسم و لیاقت بردن آن را دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23068" target="_blank">📅 19:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23067">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hj8w4SDzWqBLKY-80qHPGJNbPfqyGmVtZUupwbpLUEiTqVVwkcMamHiOJDW34k3vJsZJQ-QgM0qfXASajpfCxwhblfU_NTfrTveTvo7W1B16xEzBIroN6zxGDupHVwG1EpCwuhF8cdWsUQj4AZla9GUQk3mjGQBseUUQwIYjMXiuokVq2ZrHNPOPnJqsdn4hXcBJy5ykZdNULE2B1_rH0ZjXYoXvZzDU16Uo7PTzKf5ZVxRwo6De2rNcAyRgQkF-nW8FVVNhK9-4nKqU6j3tOfM-rdpJgDSDJ1j-o0_qm2_TZHovptwYko7wpZH4KLMwIy3BgtPwN-iYzjjU588vSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
با اعلام حجت کریمی عضو هیات رئیسه فدراسیون فوتبال: تا آخرخرداد اگه استیناف نتیجه ۳ صفر به سود گلگهر رو تایید کنه گل گهر مستقیم میره سطح دو. اگه تایید نشد، ۵ تیر پرسپولیس با چادرملو بازی میکنه برندشون با گل گهر، ۱۰ تیر بازی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23067" target="_blank">📅 19:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23066">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JswZ_t79Or9kpP6SOPUnfcGSNQJh4Z_rLPPVRWD3wdlci4Mqg_STB06U-qFcX8XTZHcig1CInKRHiy6orgQVCcfpICOupRlLQLQowx2hhGQ107YAVymgz6eL571_QzH7ojNT4GLAHnjatYbNSyMDG2GHk0OB4eBdhEIKoKe90yOIEvC415Trn7QEqdcYNUecDi8ZNT1Vpk23ABDMQU8l0Gp9n5FuHFlFkGaOfH4L9uDkFSN2igKoov_WqapTWjBuivcdYaGm_TeJocgbyTpNzCiP-h2_4j2sQpPdjmD-yP74ZH_tGY162Ob_uYkxNC-qkNuVREtB21I8NoWypsSb_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
لیست‌کامل‌بازیکنان حاضر در جام جهانی 2026 باتجربه‌قهرمانی‌شیرین و ارزشمند در این تورنمتت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23066" target="_blank">📅 18:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23065">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-cV7LxlHq447UMIsSmz7JXPlzj3iXrYS0TNxzIGp_qmxqYiiA323V71HgBl6Qrjs3ZycownuGwbjzgaeZLzEkST4VGf9Yj2q74sDgqNN0Y8xzEnUN1fbussoBVS9MiyBuGVZFBUQr4UpbzBFonTQUfykPAbeGhBG3GCT1ZTOZ6u6F3mkZAlsazyYhBw3qejftepJ2SQ9Juu1KxLtNEC0J6O_9iH9btgixVNYUWXyvLHg7a5YuQxarFpLycMiesix0AtLwgVhBWmPe907jynfgnBmM9bqOm5RSWHtvl-gjiiypAFqEFGxhTmekmuZFk5riG60D6txFQXmWfKaE9JZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همانطور که دو هفته پیش خبر دادیم؛ باشگاه سپاهان مشکلی با فروش محمد امین حزباوی مدافع جوان این‌تیم‌ندارد و رقم 70 میلیارد تومان برای این بازیکن تعیین کرده است. هم آریا یوسفی هم امین حزباوی مدنظر اوسمار ویرا برزیلی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23065" target="_blank">📅 18:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23064">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXgTz7t7Y8m6-fkMdOIHsebSF7mzLHCYkiLr707z684hr71eOdZb-5qbmOhWD2ihhPWrLXfy1G7iCZddfYHhaOkSWkOGOlZAbp42qJ9CnNmEnTEr3X5NJdFcJYAd9-SIEVgLECZ_jgz4Kuk-cWVmjaq6x50z-OURYeVwFBV6Zrnfucstuug9gViDmAgzNm0X_T2MIg_i_TH3cFatp6AQSojDRfVNoANrT7_HslEfo_tD8-tF4yrWFdOPpUcfLvblaua6S_C1mjEbiRksZezGgnEVjKXstsL79GxuLfn0Gi176AFFbiYI9pC4fulpaDFAACwQTQJlYJrUG_obhEA3oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌شنیده‌های‌پرشیاناازتبریز؛مدیران تراکتور با علی نعمتی مدافع‌سابق‌فولاد و پرسپولیس برای عقد قراردادی دو ساله به توافق رسیده اند و بعد از جام جهانی قراردادش رو با پرشورها امضا خواهد کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23064" target="_blank">📅 18:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23062">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEuf5ePFj45ByKYbDCbVlafoZxj2lSQW6v0YAx0ro1yU5cbPdZbn9-b6w5PjB4OjQfR2eS1PlTJjH-bwokca-msNKXKd5tERNx76lbOaAjlMvLyDJ39BP_1iTSm2BmB5koTqR_f0Vba15MfaO0irh2dpKrYz37c3EfGfpaTgntc3EXJW2UAQ49XEqIDC26EnWKXbr9Tb1gdJDqDRIWYGcpnDjKnmT8mAUZaWadwd94uq03_f2HYtjsgQxeKdaMCleSUSVTkkeeC-GYSxjM8BKGMFZBQI5R8hMdDVnNGg0XzZpwkw_NDCzEs_1BcoUd897Ox_BcGxN15Ydc5WWPXtmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ترکیب‌تیم‌منتخب مسن‌ترین بازیکنان رقابت های جام جهانی 2026 آمریکا؛ به احتمال‌زیاد این آخرین جام جهانی این یازده فوق ستاره خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23062" target="_blank">📅 18:06 · 19 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
