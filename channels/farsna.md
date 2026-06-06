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
<img src="https://cdn4.telesco.pe/file/U9KhteymGvyW_nVzDiVPGBUdcfgvWfKs7G2wkOzH7hHgj6RS9Kxlv6RKVQZRv-r9BP41yHHKrHHXzhht2X5m8PTF1peelGTPPJWIlUmHlqbDnRH6-1YAbeAAFJHS99MCjw9lNwhsoPltZ27gcGE1tob63FvixuIolnvIzWVLZ0-fdrS8a2EeIcygC3UezqH7_H9FCOJNQmc-Q4e3M-tuifzhFC-fYcz9qYGjfEd6IktJ3uHWorFNtfGh9lsd51Uw8TByAuHRIBzQH-uVlI0bQXHXRLmzvE1KVSyjmAvf9yx9QpYhFkmZ20Nahxf3J-B1UnnyBP0JrIFjgNUynFoZJQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 01:05:00</div>
<hr>

<div class="tg-post" id="msg-440301">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a70d2b9884.mp4?token=qDVf784t7Mdcbca9OKcg7F4DEanLb9bf6EvYj0uKnmZUTRpsYENwRJJM1QzrDf9Unq7XkPoLCrHlSTAd4biFHmnrkeufA9hO5YOO9JvggqCcD0wRISWveB0WWkKIMt21qt8laOKLEu9wbBU1MDWYFY1VuTATSYNRjqLRllwQFtDasG0b2xNwp0C2Zsu6Sug787nfakFNUSh5uyRRMCRB1MmvsBF3otp0TuYd9KIV-tIAH9M0WT8wQFjxTaK9zID1zgSDY-KvG8D3PiFcPqf9EkwJnFGjNRCtO6lfns2qeUPP54Y_IQSMqMJG1NDfVRV2F3pMUnRFTzKv05beQsBj-ToO8Pz35b1r1yMyWmeU99kAaQ8qO3jLEuSO-V0ioVyfylj057WbVBi5Ptd9FOmhjHXgonVsPv0beUcnb7UwbAbZqx9qpq9mzFGrD9iAE96ZfkG--Paru5jM0BWle6ViJ7sx90mO9EhXAqQUnKGF9Xe7dAhq-HV-_TA9rm_xbrvnIOnQsj2BHcpfZUgY8bLts3Re2UmA43rgDP7lZFFrAcgsckl1mIASAI9pPoqIaH4Nru4PnrwJtxQrVFTkhyVOAzcYx58-NlTR_otMYmuvDO184i2GaewieElB29CZLk6NeY6zdrZm4SiOX1Gk401Z3SblfbZh1r40o2oAZMjXIBI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a70d2b9884.mp4?token=qDVf784t7Mdcbca9OKcg7F4DEanLb9bf6EvYj0uKnmZUTRpsYENwRJJM1QzrDf9Unq7XkPoLCrHlSTAd4biFHmnrkeufA9hO5YOO9JvggqCcD0wRISWveB0WWkKIMt21qt8laOKLEu9wbBU1MDWYFY1VuTATSYNRjqLRllwQFtDasG0b2xNwp0C2Zsu6Sug787nfakFNUSh5uyRRMCRB1MmvsBF3otp0TuYd9KIV-tIAH9M0WT8wQFjxTaK9zID1zgSDY-KvG8D3PiFcPqf9EkwJnFGjNRCtO6lfns2qeUPP54Y_IQSMqMJG1NDfVRV2F3pMUnRFTzKv05beQsBj-ToO8Pz35b1r1yMyWmeU99kAaQ8qO3jLEuSO-V0ioVyfylj057WbVBi5Ptd9FOmhjHXgonVsPv0beUcnb7UwbAbZqx9qpq9mzFGrD9iAE96ZfkG--Paru5jM0BWle6ViJ7sx90mO9EhXAqQUnKGF9Xe7dAhq-HV-_TA9rm_xbrvnIOnQsj2BHcpfZUgY8bLts3Re2UmA43rgDP7lZFFrAcgsckl1mIASAI9pPoqIaH4Nru4PnrwJtxQrVFTkhyVOAzcYx58-NlTR_otMYmuvDO184i2GaewieElB29CZLk6NeY6zdrZm4SiOX1Gk401Z3SblfbZh1r40o2oAZMjXIBI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
درخواست عجیب پسربچهٔ ۱۲ ساله از آتش‌نشان فداکار
@Farsna</div>
<div class="tg-footer">👁️ 944 · <a href="https://t.me/farsna/440301" target="_blank">📅 01:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440300">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/445c9c889f.mp4?token=spC9lujZCaxAxdBAN6xToFIEI6dqxF0d1A8ak5QtyoBQs9KBU4eyRhFgQSTKLZVzEeGuO0Zgxx8B2m4MmbsNylH54r4tiazxBB_hIkYBV4-K4oYQ7jzVyNHkGpoIoT6JJXc9XeaZWbLSDbzQcIwDPdVgps0AZOqBFtnq0d1IjD015bU-5k-GnfeRDyb5AOKEjELedtlC1CoEpXrAaDC2r2RhQp-hlTEvD4xOcxalFMk3rRdKqO_34FA8mbYkXMRGLwvAXIkI9y5NtXHO9QfcE6jZe_crDBNjSf0vgELc52ljX5rRAX3gCb0CAyM7NNPDvB234SYO6UNSdLjh_Ux_KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/445c9c889f.mp4?token=spC9lujZCaxAxdBAN6xToFIEI6dqxF0d1A8ak5QtyoBQs9KBU4eyRhFgQSTKLZVzEeGuO0Zgxx8B2m4MmbsNylH54r4tiazxBB_hIkYBV4-K4oYQ7jzVyNHkGpoIoT6JJXc9XeaZWbLSDbzQcIwDPdVgps0AZOqBFtnq0d1IjD015bU-5k-GnfeRDyb5AOKEjELedtlC1CoEpXrAaDC2r2RhQp-hlTEvD4xOcxalFMk3rRdKqO_34FA8mbYkXMRGLwvAXIkI9y5NtXHO9QfcE6jZe_crDBNjSf0vgELc52ljX5rRAX3gCb0CAyM7NNPDvB234SYO6UNSdLjh_Ux_KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در بمباران چادرهای آوارگان غزه توسط صهیونیست‌ها تاکنون ۸ نفر شهید شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/farsna/440300" target="_blank">📅 00:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440299">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ede6fa5c47.mp4?token=N9113SjJ6BinNazdAVuALcX2f48mes3jk48EEjQxj20F4aMsbOhWpYE4yde5SBy09A6fAlKOnfNBeUNE1Cyic0M2kyf4RUGdQ5i-9mtRhzRRc-Y9w55rx8tjf5Y0ecsDqO33WluWFbbMF4rp7HUaybHuUE8dZsDxmxEoS6Fjmh5LFsGpdwv6NVXLcFxS6o5vi8a8x4c2r-gon7WYKz2vbQcdQTyaJJS4TAk3v8my8SSmAEZyoi4A-MOD2vGRa1kTHlTp24dIfSV13oUGGsYe2sW_MZsnHUhlsXU-BNEaD7nAKmtyGvKGmtdCMGXS3wLIHRBygWKHVHdAm-eAueVzTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ede6fa5c47.mp4?token=N9113SjJ6BinNazdAVuALcX2f48mes3jk48EEjQxj20F4aMsbOhWpYE4yde5SBy09A6fAlKOnfNBeUNE1Cyic0M2kyf4RUGdQ5i-9mtRhzRRc-Y9w55rx8tjf5Y0ecsDqO33WluWFbbMF4rp7HUaybHuUE8dZsDxmxEoS6Fjmh5LFsGpdwv6NVXLcFxS6o5vi8a8x4c2r-gon7WYKz2vbQcdQTyaJJS4TAk3v8my8SSmAEZyoi4A-MOD2vGRa1kTHlTp24dIfSV13oUGGsYe2sW_MZsnHUhlsXU-BNEaD7nAKmtyGvKGmtdCMGXS3wLIHRBygWKHVHdAm-eAueVzTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
وزیر کشور پاکستان به تهران آمد  @Farsna</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/farsna/440299" target="_blank">📅 00:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440298">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🎥
مردم شاهرود در موج ۹۸: فرمانده بده فرمان، حکم آنچه تو فرمایی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/farsna/440298" target="_blank">📅 00:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440297">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b38eb300b3.mp4?token=OJu55pxBJ0AJuZhYtds6VtmZL6E-PVCIPor94JYRzgPAZsl9wxeOBiQp2ywcRdXQd_f__5ta1ksLxlwNg27gQ4zhLviCA3ta2KFI7qQslmqkBV2uR2_80cLm2bVuW-kkkSk6rc-C3OmXK-ZR00W2Z9M8gVjHzMZIfAtlQLz7oGrA70RKdeAbynTbUE-nBpOmjHA8xh6cwJu7o4gZHVIDTCsycEND8z2CanyIfRDQtlw3oNnTZf7MTvMO6Qe88lATvKpRj6Yfte8QI9yzr3_TMkG5UBGm3Z78nbGCurg2LfA4VS0JXdy6EYh4VVsrNbE8VXrRx0cBzWFywbI41u9jmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b38eb300b3.mp4?token=OJu55pxBJ0AJuZhYtds6VtmZL6E-PVCIPor94JYRzgPAZsl9wxeOBiQp2ywcRdXQd_f__5ta1ksLxlwNg27gQ4zhLviCA3ta2KFI7qQslmqkBV2uR2_80cLm2bVuW-kkkSk6rc-C3OmXK-ZR00W2Z9M8gVjHzMZIfAtlQLz7oGrA70RKdeAbynTbUE-nBpOmjHA8xh6cwJu7o4gZHVIDTCsycEND8z2CanyIfRDQtlw3oNnTZf7MTvMO6Qe88lATvKpRj6Yfte8QI9yzr3_TMkG5UBGm3Z78nbGCurg2LfA4VS0JXdy6EYh4VVsrNbE8VXrRx0cBzWFywbI41u9jmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خون مقاومت همچنان در رگ‌های رفسنجان جاری‌ است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/farsna/440297" target="_blank">📅 23:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440296">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dca6844e6b.mp4?token=IbcYpb2esAhpoeboDnTeaoDfJWutUO_-ZRRCQv1MbAPHevOl7Ai9oMIqq_0ukE40Fx7gFoMXa8OWw53uIlyYn8Iufb6OvOdXu4TEBOAl7FGc9jMrV1FdccjX0KoEB0SrD2j-tIiv_iV3NQggJY9ywifOwwHaeXfOJoR7giBhmYQDcGkJ42C4DGRj6w0gaPM7g_7Uso5xRhQZmOBpLefU4c_Hda7G5AKbdMRvZnEInTYOlR67ta5B1IQVSCsePgMnzMnIpJCjkXnJgo14t4_WNplnIag_jdtD7vVv3yxWqJVANcqVxjwZ8SuBv8foU484dlYcmwQd4TK5qSKv_5x-Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dca6844e6b.mp4?token=IbcYpb2esAhpoeboDnTeaoDfJWutUO_-ZRRCQv1MbAPHevOl7Ai9oMIqq_0ukE40Fx7gFoMXa8OWw53uIlyYn8Iufb6OvOdXu4TEBOAl7FGc9jMrV1FdccjX0KoEB0SrD2j-tIiv_iV3NQggJY9ywifOwwHaeXfOJoR7giBhmYQDcGkJ42C4DGRj6w0gaPM7g_7Uso5xRhQZmOBpLefU4c_Hda7G5AKbdMRvZnEInTYOlR67ta5B1IQVSCsePgMnzMnIpJCjkXnJgo14t4_WNplnIag_jdtD7vVv3yxWqJVANcqVxjwZ8SuBv8foU484dlYcmwQd4TK5qSKv_5x-Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خروش قلعه‌گنجی‌ها در نودوهشتمین اجتماع اقتدار
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/farsna/440296" target="_blank">📅 23:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440295">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCUXAizNkOgVc4KlyaFvBHhbPFODuaw3gV0DftHnmRuW-gmHQFitCREMBuhIPZRfTMS520aRKfDTsPh1ZksYNlo1CqtW7loFmw7EvVCruL_wxqMfH-72GUmWcWoAfqrNoGZ459IRmqvR3VcoUrza575t7zKQTOFzdf1Be1r0gbbXfAE9ZLWyZP8pSDRusHOaWD15RgltvKBbVmnGenGA2WKYjMTdy0qapV14MvlBUMRUOANlDs-ogF_seAulSIoLWk3GgoF8eScbMcqz6q_KDvh1DISWPwxZfxkqFWCWuekU0bplnysz-e38_FSHC7HdJxvHvCA-PNuo5py1b89GRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چاه‌ها آب را از «پریشان» دزدیدند
🔹
تالاب پریشان، یکی از بزرگ‌ترین تالاب‌های آب شیرین ایران، امسال وارد شانزدهمین سال خشکی خود شد.
🔹
لاهیجان‌زاده، معاون سازمان حفاظت محیط‌زیست می‌گوید ۴۹۰ چاه غیرمجاز به‌همراه تعدادی چاه مجاز با برداشت بیش از ظرفیت اکولوژیک منطقه، از مهم‌ترین عوامل خشک‌شدن این تالاب هستند.
🔹
به‌گفته مسئولان، تا زمانی که وضعیت این چاه‌ها تعیین‌تکلیف نشود، احیای تالاب پریشان امکان‌پذیر نخواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/farsna/440295" target="_blank">📅 23:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440293">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PN72QyN40YVMee7tEXO_p_IUHnJnMG_E31PwWku2FZ7dkW4r2yFjMnaTjTZskYAgrP81UKiLxdx1LWsezsbPo8TN6W1XtpKVw1_vrDT5k_5ZZuvrwuNi8Q2h8KOtPYzbw0hoY7FOg3YVmzkdFN3uppYN8SlmchnCDRKEjG42EtMQmzBVqh3xMx2kmiJnEWd6k-AAfEjkRj5Pcqdorg-WJUzPa22I1rMA_DiB0qS7av3U1yu6XwCoEwK-LoXOtJoy7hifOrKq7G8Q35RcqA4uAsyECn2bITcUikgr5RZ7SbjHnpU35HObPPqrv7k3clfJnDxZs3sHjC_oL1Y37TinIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده صهیونیست: جنوب لبنان باید اشغال شود
🔹
فرمانده جبهه شمالی ارتش رژیم صهیونیستی خط بطلانی بر مذاکرات لبنان و رژیم صهیونیستی کشید و خواستار اشغال جنوب این کشور شد.
🔹
او گفته که خلع سلاح حزب‌الله بدون کنترل و اشغال جنوب لبنان امکان‌پذیر نیست.
🔸
در راستای اجرای همین سیاست، ارتش صهیونیستی ساعاتی پیش دستور تخلیه فوری ۵ شهرک و روستا در جنوب لبنان را صادر کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/farsna/440293" target="_blank">📅 23:02 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440292">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cB5EeQLb1ztYx3LaKNZKQdBCjs5wqgLgxn_IAf6uWi0l0a58e9aABRzhuAcY_86v3zM7uXkmWO0d5U1lWq6dK0ZmKykmMjd5g8sHfYXZ2nu8UNjDDF1CmZ1B_YL2Mz-_pw5XgCql_GhPPy5bT2lWeneFjU_KtwP8qyZs2PsW8aRUk92c2m_8r7u-BA3nlOczXHnVVP5IIdDNY1iix4ea-mWnxHq26azCZq2hu05V3QHcgCny9Ht4wL0WDLS9ca_aatC65DuOvMa4VSXzkJNfQ3wMgeoyTuELHvfMX_c4BgpFfMQR0mKaJx43y5A01oHQ9bTD-wj75sxWP3UsVWoSXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا عکاس تیم ملی عراق را دیپورت کرد
🔹
طلال صلاح، عکاس تیم ملی عراق پس از ورود این کاروان به آمریکا برای جام جهانی، ۱۳ ساعت در بازداشت بود و در نهایت به بغداد دیپورت شد.
@Sportfars</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/440292" target="_blank">📅 22:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440291">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‌
🔴
حزب‌الله: یک تانک مرکاوای رژیم صهیونسیتی در منطقهٔ بلاط با پهپاد انتحاری مورد اصابت قرار گرفت.  @Farsna</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/farsna/440291" target="_blank">📅 22:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440290">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42d3cf08d3.mp4?token=hG35wk6c1U3AkHsvF4d9Gk8gxyHqloysvlmougK0EkF3aSecfebwIKuP7cnPF9oScc4n2IfoUrQ2aYkRTeCfdSWlzTx_RTcMWFhqfFGEyLU_AayCohbOu-2vP9QwUEZYauPjkKz7oc0uOaliA0mBmbZGSV3Il6WrzHalY5V8bSMf4-BFlWlAKKxhHsi7UQX7-1bCXSBF3iKJg80H0FrWMVHuiLISjFOJuymq1YN29wr_-EjwJlWBWU04qYGIkJxDhULA_ioRI1TmmnMRk6eroe5ywzapDlC_KLjf3wljBBJcmT_9dNVXzQCuC8hvLvrTNAVOOOAWdjqEz7zXYDbFEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42d3cf08d3.mp4?token=hG35wk6c1U3AkHsvF4d9Gk8gxyHqloysvlmougK0EkF3aSecfebwIKuP7cnPF9oScc4n2IfoUrQ2aYkRTeCfdSWlzTx_RTcMWFhqfFGEyLU_AayCohbOu-2vP9QwUEZYauPjkKz7oc0uOaliA0mBmbZGSV3Il6WrzHalY5V8bSMf4-BFlWlAKKxhHsi7UQX7-1bCXSBF3iKJg80H0FrWMVHuiLISjFOJuymq1YN29wr_-EjwJlWBWU04qYGIkJxDhULA_ioRI1TmmnMRk6eroe5ywzapDlC_KLjf3wljBBJcmT_9dNVXzQCuC8hvLvrTNAVOOOAWdjqEz7zXYDbFEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیرخوارگان ۴۵ کشور برای «نوه رهبر شهید» گردهم می‌آیند
🔹
دبیر مجمع جهانی حضرت علی‌اصغر(ع) استان قم از برگزاری مراسم بین‌المللی بزرگداشت «زهرا کوچولو»، نوه ۱۴ ماهه شهید رهبر شهید انقلاب، با حضور بیش از هزار شیرخوار و نمایندگانی از ۴۵ کشور جهان خبر داد.
🔹
این مراسم پنجشنبه شب ۲۸ خرداد ۱۴۰۵ از ساعت ۲۲ تا ۲۴ در میدان مفید و خیابان شهید صدوقی قم برگزار می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/440290" target="_blank">📅 22:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440289">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در حوالی جزیره خارک
🔹
دقایقی پیش ساکنان جزیره خارک متوجه صدای یک انفجار نسبتا شدید شدند.
🔹
هنوز محل دقیق و منشا این انفجار مشخص نیست اما بررسی‌های خبرنگار فارس نشان می‌دهد این انفجار خارج از جزیره رخ داده است.
🔹
روابط عمومی سپاه بوشهر…</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/farsna/440289" target="_blank">📅 22:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440288">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OS8GEP6z2Cfwuq1YsCLKCepM9UlVOGMVN7ZrAZnaQKMLWxu66qTJQThvNpgk35BfYifxriGLStPY0m3MA7Q76I1pCKxi_wj0tsBgFJBhaCV6DnqTOIELYfEzn1lztkXUlNl_-UrcLMwR0mnm9XAvqGbQNg0q8Z-NQt-E2pUFEO0eNAoQ1daBny9bKW1dA4oEdnjwvcvjHQX-7SEZaGE01HedqGfIYoLfIB-GUgjdD2Ts76BwA_DTSbSvwNUVG7Fd0WnXg2j6WvSKYFt4LmHxaoz9H9jyhFfKhlkf88wOCZIYwccAaFCcwT4EzHn0wyOsSST5ibF35SN6yjbbWb8IIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هلاکت ۲ نظامی صهیونیست در جنوب لبنان
🔹
رسانه‌های عبری گزارش دادند که در نتیجه ضربات مجاهدان حزب‌الله ۲ نظامی صهیونیست در جنوب لبنان به هلاکت رسیده‌اند.
🔹
این رسانه‌ها افزودند یک نظامی صهیونیست دیگر از تیپ گیواتی هم روز گذشته‌ در جنوب لبنان به کشته شده‌ است.
🔸
حزب‌الله از بامداد امروز شنبه تا به الان از انجام ۲۳ عملیات علیه نظامیان صهیونیست در جنوب لبنان خبر داده و طی آن علاوه بر هدف گرفتن محل تجمع نظامیان اشغالگر، چندین خودرو و تانک مرکاوا را مورد اصابت مستقیم قرار داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/440288" target="_blank">📅 22:02 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440285">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
شنیده
‌
شدن صدای انفجار در حوالی جزیره خارک
🔹
دقایقی پیش ساکنان جزیره خارک متوجه صدای یک انفجار نسبتا شدید شدند.
🔹
هنوز محل دقیق و منشا این انفجار مشخص نیست اما بررسی‌های خبرنگار فارس نشان می‌دهد این انفجار خارج از جزیره رخ داده است.
🔹
روابط عمومی سپاه بوشهر روز گذشته از اجرای عملیات خنثی‌سازی و انفجار کنترل‌شده بمب‌های عمل‌نکرده باقی‌مانده از حملات اخیر در این استان طی امروز شنبه خبر داده بود.
🔹
از سوی دیگر در روزهای گذشته چندین درگیری میان نیروهای مسلح ایران و نیروهای متخاصم رخ داده است.
🔹
بامداد امروز سپاه پاسداران در پاسخ به تعرض دشمن در جزیره قشم و سیریک، پایگاه‌های آمریکا در بحرین و کویت را هدف حملات خود قرار داد. در این عملیات دو پایگاه هوایی آمریکا به نام‌های علی‌السالم کویت و تأسیسات مهم باقی‌مانده در ناوگان پنجم نیروی دریایی آمریکا در بحرین هدف آتش موشک‌های بالستیک نیروی هوافضای سپاه واقع شدند.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/440285" target="_blank">📅 21:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440284">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d84ba5090b.mp4?token=b-LXN3S_v-i1ijOo89TIs2s_-Au8pf16ZCRnPapHQJWouKC7OQ8hJd5kS5Pxn1buoN9Lo0nKGwEzOXFldAd2-EhyZKAX45XmkAthzl_nXFhdD1bVJzViMB4FBpo1BE3Uo_7_HYpk0yDDA-6hChBr2elD4ytiNf-RsAPUT5G4DLVrl2i1nZ_IU-aAtJF4moNwEeJYvtYti0SCM_q8hasy75BL9i7rsWxHdM1adlNNE4V7JgvkjCCM-EfNzuiKD8VrQm_mbMRRIdrLGGgZOsF7SvI_iAw8qCcdTp2dhdeURCG52VhLhr4In2DYYGcKl5rx5RXY0dgIazgtcDeTZSj98w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d84ba5090b.mp4?token=b-LXN3S_v-i1ijOo89TIs2s_-Au8pf16ZCRnPapHQJWouKC7OQ8hJd5kS5Pxn1buoN9Lo0nKGwEzOXFldAd2-EhyZKAX45XmkAthzl_nXFhdD1bVJzViMB4FBpo1BE3Uo_7_HYpk0yDDA-6hChBr2elD4ytiNf-RsAPUT5G4DLVrl2i1nZ_IU-aAtJF4moNwEeJYvtYti0SCM_q8hasy75BL9i7rsWxHdM1adlNNE4V7JgvkjCCM-EfNzuiKD8VrQm_mbMRRIdrLGGgZOsF7SvI_iAw8qCcdTp2dhdeURCG52VhLhr4In2DYYGcKl5rx5RXY0dgIazgtcDeTZSj98w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موکب حزب‌الله لبنان در قلب تهران؛ تا آخر با شما هستیم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/440284" target="_blank">📅 21:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440283">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/081d11a12f.mp4?token=blQ141RkfJ59PLV6kohi0qL2V0sAqEwJhwZpywmwqFFP9TdbCDHT6gCutmUrRWqYyPtSE-nQx42ODYQoqT8ZcyeIBCgfhnnZ_ITI_w0DOfiuwEri00otzokqONJ_mMe0UeKZQEH9el8nBbprgkAUSbfAmsR4PHHSIESm12FlfGgbrre01_3oSe3xeybqyWZYQ9I0M5baXwTRFkdDKEDu_1AGdyYwyS3CsIaUo_NL7vnzkEWTTazphon_krAqe4CjoFX2PHlJJ8Hl6oJMMPszDXeAc4RNksympNrJZbjqfAixXtgGBUZUhtyFw0Sx10fc2gY1JRI4CpHdItSNWhhUnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/081d11a12f.mp4?token=blQ141RkfJ59PLV6kohi0qL2V0sAqEwJhwZpywmwqFFP9TdbCDHT6gCutmUrRWqYyPtSE-nQx42ODYQoqT8ZcyeIBCgfhnnZ_ITI_w0DOfiuwEri00otzokqONJ_mMe0UeKZQEH9el8nBbprgkAUSbfAmsR4PHHSIESm12FlfGgbrre01_3oSe3xeybqyWZYQ9I0M5baXwTRFkdDKEDu_1AGdyYwyS3CsIaUo_NL7vnzkEWTTazphon_krAqe4CjoFX2PHlJJ8Hl6oJMMPszDXeAc4RNksympNrJZbjqfAixXtgGBUZUhtyFw0Sx10fc2gY1JRI4CpHdItSNWhhUnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر آموزش‌و‌پرورش: هیچ مدیری حق ندارد هنگام ثبت‌نام از والدین دانش‌آموزان پول بگیرد.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/440283" target="_blank">📅 21:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440278">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NogxlaKsQR6kjgAep0rQ5fHw5bj2-3NANnNiAu-uPGuK2cxGEfvVPcN0qtgCdfUd0kqA4otYiXDkNBUZO-sih2HCVZSKjaACYlh9B1d2azVFolPudXGQ8Nnkaug1ScwXiN-voVr8iFmEsFqL9gf2miUo_GE19qk9gW61-D_eADSCpklwy4GqT2v5nKQ6PY79aYjnBgUaoLxIG7zd00ZaVdo0HfL_NbgffTA-9QPbP2PeUmcGB6SGYSAFHdxAwqngM-CtOjwBrxAJX4O8m4p-zbm6LDndjiWFov6BULe1fCyd4EDh53VBt3ElkUimSXMGazQF02OENlbBXosPGJZInA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PbTSxtREjTUEMUJWNUD5Bml9mGx1qI1j2xhPpYh7SJ1740sQAJnrLDUvsKItfC5Rm-4WtOK5b3k7e9hZt_zbq3NfOJCWxLUw9IneB_zUDvNpUJB5-fkBqAqOn67g3a19o3Ry9haTirJGGzUBCy5szlv-diV4Vgg19_OKxpQEZ8W9tIY5T7wXDRJLFNuO15OVOsKbWYAIRYJygUsjc7aXJQJ3yZ9fTkWDttpV2WehYu0useKHxdmm4iOZLcIZUU4ueCZ8PMKyNV8E5fgNpKtrI0rivOTKOMAPgaXceXJYeCTLh1zmgWPaUM3vqpLNtCWq9f77nD3RuxM1UEYQvYUI3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/amhd5d75SX9_5Q5oFUgqLbpWLX2fNtM_fcnDE0kKUdVPJSD7a-F_DZz-QTMYSoTm7U8txI9-kSH89ylfVr68tXQK6xxWDmpyCXSgfudkJxL4HBXOucX20_h8yr5aWk2Oi5k51AGx_ooTvQBKp4cHZtYLtjrdYUat9IDigc12uaMiF0u0MWuRGvr-LGeRDb-24Gg7rgBjTy1T72rs0G2REIS9XwxrGviYwpQVQipStHVM6FFsn5jEjU4IEcNgQ5uRQ1Mf0IarhAzhnd9yPi1aUhTGu2-G-aiYX7QAF3Z21dzMlOODjCnJyVi2zSMyL-r9FcEmG5qihZ7HXeku5we2tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JrIY_xGgP_UDcFgfDiKAOIhEGUizMIPci-UPBYwZDY6MQAmBhCh7hXb0_-EM3Ujk3NAA8ZozTgST-6ntDxS-JaGNJnw7S40qLyYCe7AbNTdYdaZ0l_je2hV74WnJHYPUT_1zWe5nHsODFg71_vfex-XZ4X9x-cJJZ1sU2XC-1B3fWKRQCEct1p7MapMNXMo8eiNI0f3i9UoH2YT_9gvgRetSAP7aCIMdx4ORiKCnXtnFVamzWEbF89Js9iGFW5Wo8fhI47vstcQrFNRfdC6c-chuQE0RNI600e9JMv_CYF3LcjZI0PSrmKaZNIbJ7_oqV6RhFuCljgJmGPf8eGVAlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rAh-GWTpfsIR3DN1XI8X_yCOoREaXe-i_jtymVdzPZZ0KQd5tUEUN_E0DFxTZUL-HrNUCMqkyog3HNs0uYk7HmpnpfLlMlNNP5kffveTVqV1KGDCew98z03cBwUXRSVyo9hITzjPBOCvQ_tjbmgygnwBTTd_l-QkPU27_uuEl5tBTu1ypV0qPiYXph2nhfugU-DVP8nFfosgnQDAEBu4hJ3-V9glYpyZm6hdaVyHr-Ceh_QUJ1I6H57NMLhtn5LRkCjbmjv9DzS-lE2B0OUcvMPkGE_BZFBcA-eIqtpOwvixIHAD9lVSxrKzI6qeVN974kXoen7C4o1hV9S350UTgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
وزیر کشور پاکستان به تهران آمد
@Farsna</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/440278" target="_blank">📅 21:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440277">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس من</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QpNyAM7H17xKXVwQ53qr8TCMyM8u0mjKMTOnrDiuUWsazrVWtALGMCQJ_MCyVADRDyGFv26IjAvvleBLOgWxuhPBF-S7DvB-F57FJTNhTkj_k5KL9kqpb0dc5p8zJGbLkVla_XEQvdWv6GCyJXj9k11kEqspvWP4Dr_g55uzj0lOPne9xC1qco-yYSSq63BVYKIFJK39ZVPm00d6yZBJF1auZrd_YfFE7s25HdD7HLTjs7FGlpefOOp6wo_bSgSUpPnNKZS1ObyVYmoAKfg3IOO7l17DIUv1D93KdHLS9LuFqVnuI343Dz3r6SqRQSLL6qT8CcrbV4jRuWj-nHwiVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس‌من| صدای ۹۰ هزار دانش‌آموز به شورای عالی انقلاب فرهنگی رسید
🔹
بیش از ۹۰ هزار دانش‌آموز، داوطلب کنکور و والدین آن‌ها با ثبت چندین پویش در سامانه فارس‌من، خواستار مثبت شدن تأثیر سوابق تحصیلی پایه یازدهم در کنکور شده‌اند. حامیان این مطالبه معتقدند تأثیر قطعی معدل یازدهم باعث افزایش استرس، هزینه‌های آموزشی و تشدید نابرابری آموزشی شده است.
🔹
در حالی که وزارت آموزش‌وپرورش نیز از اصلاح این مصوبه حمایت کرده، عبدالحسین خسروپناه، دبیر شورای عالی انقلاب فرهنگی، اعلام کرده پیشنهاد اصلاح مصوبه در دستور کار شورای معین قرار گرفته و باتوجه به عضویت وزیر آموزش‌وپرورش در این شورا و برگزاری جلسات هفتگی آن در روزهای سه‌شنبه، وزیر باید زمان حضور خود را اعلام کند تا در خصوص این موضوع تصمیم‌گیری نهایی انجام شود.
🔸
اکنون چشم ده‌ها هزار دانش‌آموز و خانواده‌هایشان به تصمیم نهایی شورای عالی انقلاب فرهنگی دوخته شده است.
🔗
جزئیات کامل این مطالبه و آخرین تحولات پرونده را
اینجا
بخوانید.
@Farsnews_My</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/farsna/440277" target="_blank">📅 21:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440276">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3e87b46ae.mp4?token=AA64pHsNGf14WV7fjmLAestKDjA6oytKZ3NqHon-GWg4Fm2Be-ZoLhIibvM4WaI-czYUkGMuaYOHGVXSc167WoqQb2Y2nq0o0kN75QImXrD5J6E1n0HzYz8GKzOSDCB9DlX1db19PvGC7L9wx6zMBkyK8AVAvrcPV4w5QKTCJ-5wv5uWBJEjOesdT_PscNFtxZoZPMatk55F4CeM3LFiKiCnjai4gYG2M5fArCmVSff-ByV41ruWjeHsA_S7CoLAQYBIS52ezU4BtT-gBtek6t8qi9F1R5oskaWqLjlWg37uX3X5pDt4BCyxIhX_0rqWddrE10GW5WyKbq8d_NG-oIRTsjGHFxeaMlCIDljHnSd9SJk30lhpfWzJAY7t91-0dkZdqDI2iZK-jYpVSfl4Wssdbx6_uLCjxHDgwVn9E3tORGE7ShgNb5YafIIJh5cTvMDwmGMdFq63ONbpDC6IvkuFhCFc86U11vS4wMCKJVnZEW3AbhcOxkA0ETd6xeDTPb66xFYnRMIOQFjWvZYMh0jfgqEn3vrsBNwIg6IbMJP57MdGDyQBogvQ55pPo2PGMjuEGmowDTiWfYMdzMjs-GoVwnrCbbMxofSqno6_1DcuciGdtVxKRCoiktqIu3kHyKSA5WLjrUGqv1YNYZVHtRK7fC0hizHjMzLaMCJIA94" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3e87b46ae.mp4?token=AA64pHsNGf14WV7fjmLAestKDjA6oytKZ3NqHon-GWg4Fm2Be-ZoLhIibvM4WaI-czYUkGMuaYOHGVXSc167WoqQb2Y2nq0o0kN75QImXrD5J6E1n0HzYz8GKzOSDCB9DlX1db19PvGC7L9wx6zMBkyK8AVAvrcPV4w5QKTCJ-5wv5uWBJEjOesdT_PscNFtxZoZPMatk55F4CeM3LFiKiCnjai4gYG2M5fArCmVSff-ByV41ruWjeHsA_S7CoLAQYBIS52ezU4BtT-gBtek6t8qi9F1R5oskaWqLjlWg37uX3X5pDt4BCyxIhX_0rqWddrE10GW5WyKbq8d_NG-oIRTsjGHFxeaMlCIDljHnSd9SJk30lhpfWzJAY7t91-0dkZdqDI2iZK-jYpVSfl4Wssdbx6_uLCjxHDgwVn9E3tORGE7ShgNb5YafIIJh5cTvMDwmGMdFq63ONbpDC6IvkuFhCFc86U11vS4wMCKJVnZEW3AbhcOxkA0ETd6xeDTPb66xFYnRMIOQFjWvZYMh0jfgqEn3vrsBNwIg6IbMJP57MdGDyQBogvQ55pPo2PGMjuEGmowDTiWfYMdzMjs-GoVwnrCbbMxofSqno6_1DcuciGdtVxKRCoiktqIu3kHyKSA5WLjrUGqv1YNYZVHtRK7fC0hizHjMzLaMCJIA94" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشییع بسیجی شهید غلامحسین کریمی
در دلوار
🔸
غلامحسین کریمی در حین انجام مأموریت در جزیره خارک به فیض شهادت نائل آمد و امرزو در گلزار شهدای جائینک بخش دلوار استان بوشهر پیکرش به خاک سپرده شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/farsna/440276" target="_blank">📅 21:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440274">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOTpyyn6M1vbraoAkwanZqjIMjhjo7LInlX8IJIrkVDfHOhXHhjgtwAS_dqN5lM_H1e3LNmCSL7KH9ezzJVN-GYL0Ll3n3DvjWgSLugROFbkMrFPjzjhbEm5TUv-RuqYW-64X5r3XdIY8KEs3PaYAIiZunREOVju5jwxfRcvFsaKVo2qzpG3_Kev84uENRATgdUzd23fX-uskRw7vGb_gZx5FhA33Nop5y4r6ywJucOTLwUdogT4xY_3h_gexLJxZEkcnP9dmsoxoDeFcQl31VD21TcHnz6xuSc0VqkKBiL8EtHEhdK6Mwd7Prt-TRXbrB_lTa5_HTKymhp7GLW1gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هک گروهک تروریستی پژاک توسط حنظله
🔹
گروه هکری حنظله: در یک عملیات سایبری پیچیده و طولانی‌مدت، کل زیرساخت‌های ارتباطی گروه تروریستی پژاک هک شد و تمام مکاتبات، ایمیل‌ها و اسناد امن اکنون در اختیار ماست.
🔹
در چندین عملیات ترکیبی هدفمند و مشترک، مختصات تمام انبارهای سلاح و مراکز فرماندهی پژاک که به دنبال ایجاد درگیری در شمال غربی ایران بودند، توسط حنظله به واحدهای موشکی سپاه منتقل شد و این مراکز در روزهای اخیر منهدم شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/440274" target="_blank">📅 20:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440273">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzXDABY1fX9Okv7xBaElDn0AOMrvznaSI_ASQGDypA6KSV4RMLMuIxlr_J6n8AOu2MOdGE__OLGY-x2Y1bkF_cDdmvJ-T8odElIzd8OldCDb7wXgvSAtVijvTahA1qAIWEoDIHLy-p9k3zNzCd9A4inZaUg_QpNqQevGsvfsAoeMpzrlQ1mP9Y1Q-7kg4S880uTwvDFSOs5ejJqWT4CaHf1Xshg1uOEN7u-Fw_U_pUyjRasvyQ-HZAJZDR0tRNzI6P1OaY1pbS1wh8a-XtBaTrYE9o4gAXz_VrlWHnTKnuSu_mtpN6csZFCd0vvZ466z1vBErjRvwp3x7p1thD5Jvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام پرسپولیس به اوسمار ویرا
🔹
مسئولان باشگاه پرسپولیس با ارسال نامه‌ای به اوسمار ویرا سرمربی این تیم، اعضای خارجی کادر فنی و همچنین بازیکنان خارجی سرخپوشان، از آن‌ها خواسته‌اند هرچه سریع‌تر برنامهٔ بازگشت خود به ایران را اعلام کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/440273" target="_blank">📅 20:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440272">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDQackfzfjfCB5cBgiL5Ma95qkL0swYDmJz9MAHkK_NM17jKqbHPucrFm7N655z5CsC6ECaBv1bsU905R68_oHtvhITI6YVmNE79wxZhq8VIB-OYPUPH1BHCzxQcfsFGtNvJEOaz2RPOCs2EBbSoPEhpfKv0LSMz41ZAwSOdybfRNv6s8QdkYVCJ4-8qBl_N4C3HFMhVdVH6LYuLFdOyu7jvQuLbOcSUVMqf6KskNB54BizFMELv_RuSknt1shN5aKvgIGwsoiGuMjJxaOYx8jKXc598beCKyqtMX2RDuxoYg5WGq1bnlwf9A4kFlNxsUYl8iSMVX-GyQTsNwTeKzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی برای اولین بار واکسن جهانی کرونا ساخت
🔹
پژوهشگران دانشگاه کمبریج و شرکت دی‌آی‌او‌سین‌وکس موفق شده‌اند نخستین واکسن «جهانی» کرونا را در فاز نخست آزمایش انسانی با موفقیت آزمایش کنند.
🔹
این واکسن روی ۳۹ داوطلب سالم بررسی شد و هیچ عارضهٔ جانبی مهمی نداشت. تفاوت اصلی آن با واکسن‌های فعلی این است که به جای هدف قرار دادن یک سویه خاص، برای مقابله با کل خانوادهٔ «ساربکو کروناویروس‌ها» طراحی شده است.
🔹
مهم‌ترین بخش این پروژه آن است که مادهٔ اصلی واکسن به طور کامل توسط هوش مصنوعی طراحی شده است.
🔹
پژوهشگران با استفاده از داده‌های ژنتیکی کروناویروس‌های مختلف از سراسر جهان، ویژگی‌های مشترک میان همه این ویروس‌ها را شناسایی و آن‌ها را در قالب یک «سوپرآنتی‌ژن» ترکیب کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/farsna/440272" target="_blank">📅 20:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440271">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9fd8574e4.mp4?token=VTOvtRs4lqcwiFbMMM7j6Xf8At-L0-ExXPcqiVYvStcx2Xzly15v0j6n3qLvDCEJrHNeN0BAoD4aFCTjQd5n3izKOFVjHtcTyiubHr8lXUfpg_0XXTv6UM_MN7if2yex22woHjVv0CpZcx7YwcILnle55Z57PBAdxiOGdHjIKOYrqfqav3fRRO3WZOvMWWpgg9CtqP714QnsS1AVYsLSoEkPXfKoCqFUUJaapxgWjWx4UGDbPjZCUm3VZcQJ0sLZnUM96aBfgPy8Bas1X85sNKVtp1mu278MMObpX8fLftgVPzkI9XkWGQEpBsRY9RUI8JvsNWdf2VJlNhFyort8ybOZlKNrPsEelNRkeLQ5G14UsBlCo8efs6JccAspJpcu6t17Z0oJ_UHaHEGWQ0ezPX7QNXA0R5bz5N5j0H7C4YUAurAMqPOrEgQKpR3youw-175TxKcyQ7MKz2kIwTRTYM6AHNtanEGkap317IgJlexHczaIFVgGZ-mKtK1YOA02DCgrJ1RijUdFTOcaoTwfbwBLch7QNpDOmP-O5HTIeBTYB2QT3fBJoKUHGRkrnNjStHmmbhmTMDbBdcQ2epCZMc2x3bnsZyNW7zOlspVI7onHjbn5Hy4EIueEr_RNIUfzuuAdrrNchRpmGPYBiJ6va24U-_uNtn-_qZVIFOFs1ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9fd8574e4.mp4?token=VTOvtRs4lqcwiFbMMM7j6Xf8At-L0-ExXPcqiVYvStcx2Xzly15v0j6n3qLvDCEJrHNeN0BAoD4aFCTjQd5n3izKOFVjHtcTyiubHr8lXUfpg_0XXTv6UM_MN7if2yex22woHjVv0CpZcx7YwcILnle55Z57PBAdxiOGdHjIKOYrqfqav3fRRO3WZOvMWWpgg9CtqP714QnsS1AVYsLSoEkPXfKoCqFUUJaapxgWjWx4UGDbPjZCUm3VZcQJ0sLZnUM96aBfgPy8Bas1X85sNKVtp1mu278MMObpX8fLftgVPzkI9XkWGQEpBsRY9RUI8JvsNWdf2VJlNhFyort8ybOZlKNrPsEelNRkeLQ5G14UsBlCo8efs6JccAspJpcu6t17Z0oJ_UHaHEGWQ0ezPX7QNXA0R5bz5N5j0H7C4YUAurAMqPOrEgQKpR3youw-175TxKcyQ7MKz2kIwTRTYM6AHNtanEGkap317IgJlexHczaIFVgGZ-mKtK1YOA02DCgrJ1RijUdFTOcaoTwfbwBLch7QNpDOmP-O5HTIeBTYB2QT3fBJoKUHGRkrnNjStHmmbhmTMDbBdcQ2epCZMc2x3bnsZyNW7zOlspVI7onHjbn5Hy4EIueEr_RNIUfzuuAdrrNchRpmGPYBiJ6va24U-_uNtn-_qZVIFOFs1ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عطر ۱۰۰۰ساله در دیگ‌های مسی
اردبیل
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/440271" target="_blank">📅 19:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440270">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">در حملۀ رژیم صهیونیستی به شهرک‌های جویا و معرکه ۲ لبنانی به شهادت رسیدند.
@Farsna</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/440270" target="_blank">📅 19:41 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440269">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d44490100.mp4?token=IWJ-M5E-QuBF7mbyCxdWSVtkA2Scg6WLesjClmwsBpXBzsw1paKxNmiUDrSS65KJZyEgi3jI1z47dg0MWAeOJEyfspF-cZrdQp1SsQZhBEs5FvIxLVcgZJtxgdxglPlHBgSREs826aUsF_VB7_-2WYLs6ktbeg3XU7XfF4DnXqTEGRR9HCrLtcyexGqstBwR9I1sFBFvLqOa_eUjqUMlsVLzDvAvdxYGfOaMp2uJoVAPA66rIEg2FVJ1ZoADHziDE4Q-EiZI4W2WjezVkvE5Njf2RQuDCBzB9eUCwL49XcXzsvPDHBMkMXrmcZ-jSlMluIH8-kfbu-RkoYgxriwm6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d44490100.mp4?token=IWJ-M5E-QuBF7mbyCxdWSVtkA2Scg6WLesjClmwsBpXBzsw1paKxNmiUDrSS65KJZyEgi3jI1z47dg0MWAeOJEyfspF-cZrdQp1SsQZhBEs5FvIxLVcgZJtxgdxglPlHBgSREs826aUsF_VB7_-2WYLs6ktbeg3XU7XfF4DnXqTEGRR9HCrLtcyexGqstBwR9I1sFBFvLqOa_eUjqUMlsVLzDvAvdxYGfOaMp2uJoVAPA66rIEg2FVJ1ZoADHziDE4Q-EiZI4W2WjezVkvE5Njf2RQuDCBzB9eUCwL49XcXzsvPDHBMkMXrmcZ-jSlMluIH8-kfbu-RkoYgxriwm6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از مهمانی کیلومتری در زاهدان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/farsna/440269" target="_blank">📅 19:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440268">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🎥
شکستن بغض فرزند شهید صاحبدل از دیدن عکس منتشرنشدهٔ پدرش با رهبر شهید انقلاب  @Farsna</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/farsna/440268" target="_blank">📅 19:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440267">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s37kCPB9i6ivChjhSYF5vtzn5FCmmGYj0I6cYd17Dz8mbzpeLpFhvIzYf3JnAhtZ0xzKD252PUV0SfTn85oF7wqE9REHA1Z-0Zy7Jsu38hf3rmXDbfjZ8LGIOGynUmbhpkJd5g1aFNXc8LR6JsXtvI9HTSSFfo74-a62kL-bzbEf8sW73FZf7ER68skU5DeKLnNlGPBvwDIhHijkckFMWs1IgX5Tdmp_tRmfJ621EKBLTMgfmj9hPwyElM859IeaiG77Pfe6Zo8rOjjAVRErUWnnes7eOLPb2A82vyBfFHUFgcoBWF2v11s5WrfTWjViXFiZC8xjPQu9q6OY-_pSQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۱۷ ماینر غیرمجاز در داراب
🔹
فرمانده انتظامی داراب: ۱۷ دستگاه غیرمجاز استخراج ارز دیجیتال در بازرسی از ۳ منزل به کشف شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/farsna/440267" target="_blank">📅 19:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440266">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62dc4dee5d.mp4?token=k5wQ-k2MrEUtndGwhmj8gwkLFB98IvX052QGRVqRmDmYcfCIT2t2wlexdax8gSm8pFHAbEaLVAcYqkDpxlgFvK2akuPNH5-xPmJZHztGAHrsuRAaO8-E0PLWgfamPT8hccmx7Bca32xg847EtFGYjzpZ2npbJqPYtcEc_ivmkb328L1o4IUHq-qlrLC58eaEHYG0cxpimJUYF_NTuI80vxb7SjdUmWhf2Q4iIHkh2ScVEaxuFGv3t0Zz74lzL_Zpm__bb7-XVIfhMktWsifMmIlnIRHfGSE5SRfNWDbn9x1OptCgqb4MNBfbNAkDMDyhMnbR5EP02UfMhmVfV_Fnig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62dc4dee5d.mp4?token=k5wQ-k2MrEUtndGwhmj8gwkLFB98IvX052QGRVqRmDmYcfCIT2t2wlexdax8gSm8pFHAbEaLVAcYqkDpxlgFvK2akuPNH5-xPmJZHztGAHrsuRAaO8-E0PLWgfamPT8hccmx7Bca32xg847EtFGYjzpZ2npbJqPYtcEc_ivmkb328L1o4IUHq-qlrLC58eaEHYG0cxpimJUYF_NTuI80vxb7SjdUmWhf2Q4iIHkh2ScVEaxuFGv3t0Zz74lzL_Zpm__bb7-XVIfhMktWsifMmIlnIRHfGSE5SRfNWDbn9x1OptCgqb4MNBfbNAkDMDyhMnbR5EP02UfMhmVfV_Fnig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت حدادعادل از برنامهٔ‌ دیدارهای رهبر شهید انقلاب با خانوادهٔ معظّم شهدا و اشاره به نقش سعید صاحبدل در کنار رهبر شهید انقلاب  @Farsna</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/440266" target="_blank">📅 19:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440265">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fdd40e9bf.mp4?token=lA2I36K9KuEHJ3Za-_CV8EYRFtsiuNbVso4LfPUYPcGgntqumASeJ5aIsTXugmTsBatMXJq3qt4TLXx2nBxJ7Zc-nAu7kh7HVvV5DihBhvn3EG4abZxa1X8wPzIHnNLzhj4AVtGBBkI-HFLIFNPG60HyrErctwGfSGIQVDFHNWznq1OGLWG8rrY1f_I49-FNNhEzVHpje2sseTqMOXxw3E49KfeZmA0ht3ZNUGRXsQVqHZaBPiiHZLEvVXqOKbtBBaKHmbtN46kZPxXTlnR-jcFi-Nmh-en6Dp5t7mVXnogexEUETX9GAJgfJ-vLrJdzIp5QSJvc75rPb_ouwrHwlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fdd40e9bf.mp4?token=lA2I36K9KuEHJ3Za-_CV8EYRFtsiuNbVso4LfPUYPcGgntqumASeJ5aIsTXugmTsBatMXJq3qt4TLXx2nBxJ7Zc-nAu7kh7HVvV5DihBhvn3EG4abZxa1X8wPzIHnNLzhj4AVtGBBkI-HFLIFNPG60HyrErctwGfSGIQVDFHNWznq1OGLWG8rrY1f_I49-FNNhEzVHpje2sseTqMOXxw3E49KfeZmA0ht3ZNUGRXsQVqHZaBPiiHZLEvVXqOKbtBBaKHmbtN46kZPxXTlnR-jcFi-Nmh-en6Dp5t7mVXnogexEUETX9GAJgfJ-vLrJdzIp5QSJvc75rPb_ouwrHwlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت حدادعادل از برنامهٔ‌ دیدارهای رهبر شهید انقلاب با خانوادهٔ معظّم شهدا و اشاره به نقش سعید صاحبدل در کنار رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/440265" target="_blank">📅 19:16 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440264">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/slvQUJuop3FFJ3NIxzt7cnr51Ife4gVtQKiCKL2vsnXfsO6DWr3a6JklnJOz-a4p54tcUwnzWrfoi9gl3BN6Owd1buKCCf7Dwx0h77kxU0iI2aK2UrSkmNWSOkFurWS7FaHnfR593_EyCyiQWW315q-IwazGNfonT_8o6kybtfpBSGTxR2Aw2fSRnPO0WF2fLx97Xd2UICQxmOpZjrz7c5RIRns7U2joFiWID31GAQUQIyw_n1O_nj9LaSfeWrmv8rnApBTwyTYl3fITuhO9IaszJeZq5dfctHc91-BcEmMIM6bIvMElT5GASOYBl6iHgrYY09QEnAce_l158yrhcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر نیامد، بررسی اصلاح مصوبۀ کنکور عقب افتاد
🔹
دبیر شورای‌عالی انقلاب فرهنگی: پیشنهاد وزارت آموزش‌وپرورش برای اصلاح نحوۀ تأثیر سوابق تحصیلی پایه‌های یازدهم و دوازدهم در کنکور، در دستورکار جلسات شورای معین قرار گرفته بود، اما به‌دلیل غیبت وزیر آموزش‌وپرورش…</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/farsna/440264" target="_blank">📅 19:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440263">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/602cc49cc9.mp4?token=R2n225Cz3eSdCcSoYaFSv6gSBJs7NnuIjeEKZIqGFRu8rjLRTrMup_-BSZLB6f_INE8MWrbl8UjZUqW8UeYLyesfk5FLmujSud0ZemQK_h7p6GBSPiTHYlPbHfeml2AKT_XSz1z5qazFXio0r9aDvpbi7gLH1H8mum5zXasmdDXYR3BD9yOREbFa1xKq3eMHby18rKjxyUL76ySAjP0os2BZjQkJvzJZag25QX13z_vICMAJOwuh3E6FbMXJuVCqZSGKc49-V2-jFqrmhN8JTV4yj2SHP1sY7CB43xY1sVzpniBZ6CXM7rM5ZYhegdbS5CRTdyWN7dQFwZZk3V_SBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/602cc49cc9.mp4?token=R2n225Cz3eSdCcSoYaFSv6gSBJs7NnuIjeEKZIqGFRu8rjLRTrMup_-BSZLB6f_INE8MWrbl8UjZUqW8UeYLyesfk5FLmujSud0ZemQK_h7p6GBSPiTHYlPbHfeml2AKT_XSz1z5qazFXio0r9aDvpbi7gLH1H8mum5zXasmdDXYR3BD9yOREbFa1xKq3eMHby18rKjxyUL76ySAjP0os2BZjQkJvzJZag25QX13z_vICMAJOwuh3E6FbMXJuVCqZSGKc49-V2-jFqrmhN8JTV4yj2SHP1sY7CB43xY1sVzpniBZ6CXM7rM5ZYhegdbS5CRTdyWN7dQFwZZk3V_SBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حزب‌الله: یک تانک مرکاوا را در جنوب لبنان با پهپاد هدف قرار دادیم
@Farsna</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/farsna/440263" target="_blank">📅 19:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440262">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IeGo3X51-s-ffXcWOcYosIcdrE2NlEmQtJFc1z_mSMPl5YjOp-46JMduGs5G2YVqY_8cWCXhxXvZtfYpPxExFt2KmKo6otAoQAyleNBy4zrjZYSvnSmlZQb1rq-FZFoogrS-V2nIryuYBQ7P3ef-Jzp5XyvM7EAxG-ehMWEUB2_J3rGRArNW1oc9KS90DNNAp4YmNAGiMYAuboWjPwJ33AikZybMI0kT_tGW_v94ren0AU01KxpRS5LMVpbM9Crn66KAKfNGovVUNtVy2ynFI-70o85HRcxKyo_t9Iz9pHhPURzpUQSTRithBcztqPabrl61oqKSav_TcesYHy72dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی فوتبال راهی مکزیک شد
🔹
کاروان تیم ملی فوتبال ایران ساعت ۱۸:۳۰ امروز شنبه، اردوی خود در ترکیه را ترک کرد و برای حضور در کمپ خود در جام جهانی ۲۰۲۶ راهی مکزیک شد.
@Sportfars</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/farsna/440262" target="_blank">📅 19:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440261">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zg2xyOTv1O3oSChZEMyZgMDVo2_FQMj9gHIPxupflYzY7Ol9BR7dJpwKLVxUm04nSjr0Ck0h15LUkucDaHhUSpn5hs7E4VoIzJKfCq9EOWbPEVxbjRnzzoaRTyXfjiZEIawaySsouhfpVGCoZi3BvG7WYQcvW2JbFCflgDGdvJYp_J2zQ2N5NsPTMNjggfXXpKHMCYaCRXr77q2_9-4uEsUmNaeYc6FFgIgJgBntIR9TR0ks8kqdaRALetFohYtL1KjAlT-69NPjSazQLcegL3-8jQi2faZ7y5KK_PoedjNrPU6IM1mZTY95NrG-x8V5g1MS-wEIBhHYYrwpvHuAwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متن_کامل_پیام_حضرت_آیت‌الله_سیدمجتبی_خامنه‌ای_رهبر_انقلاب_اسلامی.pdf</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/farsna/440261" target="_blank">📅 18:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440259">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/038ba91241.mp4?token=QO7c_eowfrmqT5T6_iXR2M3FoLwF8ZbR50zxBACwcLfft1bZK5NBmoJH8kFsCIf1XdrTmv9ghuyb4_3sDGltv32gz0AMlHm89z8ndBo82plMeDr4MHrlLjFxxr_wQ3DAQqpFjinUJ0Z69soShESEVowBGdMDu7Hb3VvqF1FEOhGyOH9_t9ikYk2x4eLef19WvXVfadvcf3rCnMeHDrrNShUcItrNs6ak6V0eo5jCJAIcpAY3xikLC081yHwsYDmQVoYrd_xgKd9C7NoSx3gkSeIhgjvlmyEmMfQPshaI3_5Vamp3QP1itkHTvGME_E6WNz9aNMjCf1NCXLBl3pZOcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/038ba91241.mp4?token=QO7c_eowfrmqT5T6_iXR2M3FoLwF8ZbR50zxBACwcLfft1bZK5NBmoJH8kFsCIf1XdrTmv9ghuyb4_3sDGltv32gz0AMlHm89z8ndBo82plMeDr4MHrlLjFxxr_wQ3DAQqpFjinUJ0Z69soShESEVowBGdMDu7Hb3VvqF1FEOhGyOH9_t9ikYk2x4eLef19WvXVfadvcf3rCnMeHDrrNShUcItrNs6ak6V0eo5jCJAIcpAY3xikLC081yHwsYDmQVoYrd_xgKd9C7NoSx3gkSeIhgjvlmyEmMfQPshaI3_5Vamp3QP1itkHTvGME_E6WNz9aNMjCf1NCXLBl3pZOcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جنایت جدید اسرائیل با حمله به یک اردوگاه در غزه
🔹
رژیم اسرائیل در این حمله، اردوگاه آوارگان را در محلهٔ «الرمال» واقع در غرب غزه را هدف قرار داد که در این حمله  ۶ نفر شهید و ‍۱۵ نفر هم زخمی شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/farsna/440259" target="_blank">📅 18:55 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440258">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKRuk_uopYV2Gs1rjQ6mX702EGE1p-nZRy4Tc7GoJAKQfPKs6fuXTSkWBiLo1oDUhY5A3N4bMtgIErks1HdpQKgK5Zd-10jloWkGT2p3UPdfH380n1jrg7ZdBFVKDta1wgWqMccz0SlpeGAnnVwAfZlF7A96YzFHLq_N0Odv3FDoQ9dG8xK-oHO6Tl9k7Kid_ixkWfxqvc9_5skldYT9nq-Kr_-lg54vuFn2IizpCE6hhARHLXz3B9O_2xLUOXkMsnkxJaP4mMa-mgFEgz9A1QbqJt2LWTmuNled6ii5cjG7SSlgbPg6i3dFDLwi5xJ3m68qvZZP8QRo6MCPnm5s8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: امروز بیش از هر زمان به مدارا، گفت‌وگو، تحمل تفاوت‌ها، همبستگی و همکاری نیاز داریم.
@Farsna</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/farsna/440258" target="_blank">📅 18:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440254">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FneVegR5zpyky183mmlzEnsARr5pYUnWAMek_EhbnT_D4R7hfUkmVn7Xx3diWsiBHFZSUkych_cXSLa2J2UXwSB6eYDcaNBHY2bIofdySZEaGxsFMRpNOqbf2m7OU_Yh1D9vm2jUNZC_VEjI0tny-QU0u_LORiPZHzcUyCdyiqwi98JISYXiaYahDJDxTHnYG73mqzoBxN01i6g641bgsMlIgNlqGMJJLtyuiHJZeJ00CECiF8m6Bab2WtK1GoTwwnwZcQJT6CcDznMZ30F050fKBAmzzaHfW9JQZOJMUx0orGuPuRRWZTYfwC_3aOQVQaJPSxXVHV0oAAqU2ZZlbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dPXju1hSNLnEO_uze1Q4XIW0VQZKcs72RbU3Kcz6G55A8GWGoeFCzoKRP-rFqO5-0_rnuVhhJXAUlFQTyd0bS4DEfV8Ut_-1HkN6PhG0LitTnjSMLUVkBTat7EEHxMqBicO7VEed9t31sqMSswW-27-qjoLo0H4oJ18sjRl971GQWYV8k-vnRQSufeBt9USl5WFKH66OSjhXnlraWFY3ROj62hQ3roaxs4Tq32StWMGMZ1nxMZvdUpBA5lDEgqb5nPzr13kGLEYtfhjTkscgdp-a4FG2PSgY3OyTPJpp7fwetUmRrA_XprT_uwbhRKqmkhFZ1bLpffIjEr_tL6w5gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dgP0-gYw7Orye9iWNm6ztYv_PuocIbT2DHWZuFSyCprzYtORD3GhncqWbsHrSNDP7omqLSsj_evzanDOjODNthkM6KPv8eru0d225OvDuZjCwEEYlD-Q082hSzvvHTb_dIGbzB9TCcDzE_J-j2WwhzZvfMX7Yhi_GgY-IYpi-DwDDW2Xq3jA2hzc_NrYTlSnEsFX8NGDCCaqkaNsRdxi0daPE4VeHbidIquAM2zwyOq_ZRpLLf_YlL3ji3xuCEtxJI6BwMSoCe-8efQruTBYhJFp_YraPxi6WsxgjCY_t_CuwRJ37J0_U87BqHQXQVyTArEFAcoSu89ZD0KqYMjBKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kEkGesR9pfUDEKNt82nTI5H8R7UxpSe7LV2WxeRpY71xUr0KxJXYGM4xZZjDMJW4-0CUiMToE1A2fmT5ratdGJ3EVuYTlhgHc67-zlsIdgl-LyXAeOe2QnLwXMNjd7rfHba3wzqws22OVjyyxhe--qX9JjB8ixbfuMNtEMv6cIluPZPhLPFdq7bxZVET6gKXftyeS2pnrnkk7dKY5iq6xRaepfRF4119Te0ycyf7gvAMCiaEHjfDrv6H1plFb14hZ7Q0k7s6SsT63Q2vLAQAiwrExXAocIb9vAZymZi-h3YLmWRzabpEBYW-wW8kbF1Intr3HoZLtypLgGfddMqwCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از اعضای تیم ملی فوتبال ایران پیش از عزیمت به مکزیک برای حضور در جام جهانی  @Sportfars</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/farsna/440254" target="_blank">📅 18:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440253">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b08cLkHp87kX0ueh8NO7T4RwGwBxI0DKfk8nJjxkCUSlUcU-NxkEJVxzs5r09Uh6kbah_8eIz8L0VQgBRZQcnEZhIauQsoqo9QiqxGKO-p6uaZyfHSvmIyasUcGhDRkT_D-yWx36HbHjo2d7dclhH1AHYS5ZSHB71kiPuEickAk50TXHgRM5IpP9IdKjE1_b5r1PhY3qIK65LxcJ2K7UtpQD0OkNt1F9Ub8gzh6J5tMhJkpvTzOEFEc_csFb4TZNZflMdeIJVzl-NxlpRyR29ojfWIMA73-bmAl7PNK7C9VPCJtxKmTKaeELxigYsdmGkdLmKxZid-RT7ze0uXtwGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر ماهواره‌ای از اثرات آخرین حملهٔ ایران به پایگاه کویت
🔹
پس از حملهٔ تجاوزکارانه آمریکا به جنوب ایران و نقض آتش‌بس، تهران به پایگاه‌های مبدا حمله کرد.
🔹
درپی این حملات، منابع آمریکایی تایید کردند که پهپادهای ارتش ایالات‌متحده آسیب دیدند.
🔹
براساس آخرین به‌روزرسانی از تصاویر ماهواره‌ای، مشخص شد که آشیانهٔ پهپادهای آمریکا در پایگاه علی‌السالم کویت، کاملا منهدم شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/440253" target="_blank">📅 18:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440252">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IiDg5X2eOblRvQOh-XRveGw7nmxF9GWPOwzRaj7s0rWQpTY7kegyiZtrPzXd3yThKmWazTwwvkgUp_Rsp5Xv7vmzNUWOUG3maqeMTsIUgpl_Ze7StY72ontFT6usqQ9oruyPRr-ClyFJMnRdt7V8DAOi-DD-5H8L8xecXYIceHn2MaTZiv-g-dy2oi5CgX3B_NoZ9kqo2BOpj66G-Ta08SBfFGYvrUmpzXC8Ro6BUca4Bav9SLCnwPEGusmtyD_Ce5zLZb6dfa0sRqCA-bBEf2zKk24hOsl9leDAZs-VusHq26agSGKCrir8CNzQMaKwFyw-MUngBEsFGdF3AVXITA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تروریست‌های ضد ایرانی از کردستان عراق اخراج می‌شوند
🔹
شبکهٔ العربیه: دولت بغداد قصد دارد با هماهنگی مسئولان کردستان عراق، تروریست‌های تجزیه‌طلب ضد ایران را به صورت کامل اخراج کند.
🔹
پیش از این بارها عراق تأکید کرده به هیچ عنوان اجازه نخواهد داد از خاک این کشور، حمله و تعرضی به خاک جمهوری اسلامی ایران صورت گیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/440252" target="_blank">📅 18:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440251">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">بیمهٔ تکمیلی برای قهرمانان و پیشکسوتان ورزش کشور رایگان شد
🔹
صندوق حمایت از قهرمانان و پیشکسوتان ورزش: خدمات بیمهٔ تکمیلی در سال جاری در قالب ۲ طرح عادی و ویژه ارائه می‌شود که بر اساس آن، طرح ویژه برای قهرمانان و مدال‌آوران رقابت‌های معتبر بین‌المللی و همسران آنان بدون دریافت حق بیمه و به‌صورت رایگان اجرا خواهد شد.
🔹
ثبت‌نام متقاضیان از ۱۶ خرداد آغاز شده و تا ۲۷ خرداد از طریق روش‌های اینترنتی و حضوری ادامه خواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/440251" target="_blank">📅 18:07 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440250">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9c37677af.mp4?token=SQhfan69uVcrwsyhC1pYA6Oc0-RJsL2DD9L8pLYh4l_uxAgsgmlCzvU5qk6LXxkCBvcOXg7E3tsKBYRhKM6SFAjOeojtW1HV5ctRoNX7BN5R6joock34FskCHruqF7k4_5ORIZQau6M1VtxmyVOmiCYnjmmuFY0S6eoAIjoNOjV_dUk_ISNFHEKdhChtYVtupNjwXABGY0pEu4W9YHsnFxfMjo4mK_3_eIeeqGu5bSSwWssqW23BrKjg9TZ9q3ZSzSK0MvuxOP1m055K0deyr6X4__M1oWQRwpT-ctIury9EHl8fYlvcBTB22z1JTqq45okpymXlDSqcRenAwBuatQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9c37677af.mp4?token=SQhfan69uVcrwsyhC1pYA6Oc0-RJsL2DD9L8pLYh4l_uxAgsgmlCzvU5qk6LXxkCBvcOXg7E3tsKBYRhKM6SFAjOeojtW1HV5ctRoNX7BN5R6joock34FskCHruqF7k4_5ORIZQau6M1VtxmyVOmiCYnjmmuFY0S6eoAIjoNOjV_dUk_ISNFHEKdhChtYVtupNjwXABGY0pEu4W9YHsnFxfMjo4mK_3_eIeeqGu5bSSwWssqW23BrKjg9TZ9q3ZSzSK0MvuxOP1m055K0deyr6X4__M1oWQRwpT-ctIury9EHl8fYlvcBTB22z1JTqq45okpymXlDSqcRenAwBuatQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قوانین جدید فیفا برای جام‌جهانی ۲۰۲۶
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/440250" target="_blank">📅 17:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440249">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1jHnpaV4mjgt7vQHbT6K0vA4ecJ0S8NFqf0U3OzMjOmRNQHq5x8o7jLQ7j4h1DJUoNFU67k4UR_OF0gOqIdmtCpclEKqGJGSZzQcwLae_3_7iXh_QTbgGiywoSYjS7FMEDQP8BK6KqKGOFug8GzqcPRXk_EBXFPUAomyEIKazyK7R8MTwHCkLfHpgMIyy-IUzOMO6JWohpbrcpS7_79heTtk8drBQT5u7DG81F7oBhVR8rAtPGBRDojGYPk0TxNzQI10D0XcKC8gzFAHe7I3WFWlGrOZdDDMKe83PDjuI6G-PTFgL8-SAnk7ep-V6d8aMI01ZxtFtYBRLaKsFGRyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان ثبت‌نام‌های مشکوک در قرعه‌کشی خودرو، با ورود دادستانی
🔹
پس از تکرار گلایه‌های مردمی مبنی بر اختلال‌های مکرر و تکمیل‌ظرفیت برق‌آسای سامانۀ ثبت‌نام خودرو، دادستانی تهران ضمن صدور دستور قضایی برای رفع این مشکلات، خودروسازان را مکلف به برقراری عدالت در عرضه…</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/farsna/440249" target="_blank">📅 17:30 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440247">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUhhK0WzfJ0TcP-ljPQfjvfKD8rZehj6UUulHxH98v0cHfujKZONZBg3HZO3V6ZQhOWiO2do4ivlf1JvWnZcSC7GjZxkyQ09kf-xT58shZxGaBL6BNc1lFD9mM3OBjxTbrGIKPcLeBUNDF8bSu7V3ufR04Dv5uyWpBP7K22iSFhNn1tTPO6IATeJlOVC1ReBNRszqFPRPpf7eARPdvyc9BUlInsF5ikUfQV-YT9SyvhVz7Wrz6TGBxM0TLZGu5SGXXtmsw47KOGJ3nx2uqHKIffiaeJnMEXwrraIl1wxgPfkH7fGMsERxQVfLOFU9NP6Mu5fJWkWGudo__Zl0WjW3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر کشور پاکستان در راه تهران است
🔹
وزیر کشور پاکستان که گفته شده بود قرار است به ایران سفر کند، دقایقی پیش لاهور را به مقصد تهران ترک کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/farsna/440247" target="_blank">📅 17:16 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440246">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/165a80e851.mp4?token=J3wY3tCPTb9ergg4J5GcHbcKTMCK6SDzgnUJbiVR2PtAhlRZ9LZhrwPCttSzBe0yRkfZaEBY_OonDcUzkMObMTttd1o8i1f3baTOlPqvzn8ES213GxpCAN6Dml-YhvxXkr2H-k8HToDReHpI4wIm5thNA8mSQs0SZpdA3SEtX1E4kssiQ2ePKSDTdJXJVGT3dp9k8XXn0GAOCoqQyQtVNbGMWE8oobJZmYqGdNDa_pl5ZhNge3V4jMEHktX_6Seq8i6KAYJfmEfoLGcOtj69lQtYOLIwXzt8l37xhC8HpZjXoRX0J7gtljeXhLECVRW5BtcT-a4LqNARksGyQ9JPsDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/165a80e851.mp4?token=J3wY3tCPTb9ergg4J5GcHbcKTMCK6SDzgnUJbiVR2PtAhlRZ9LZhrwPCttSzBe0yRkfZaEBY_OonDcUzkMObMTttd1o8i1f3baTOlPqvzn8ES213GxpCAN6Dml-YhvxXkr2H-k8HToDReHpI4wIm5thNA8mSQs0SZpdA3SEtX1E4kssiQ2ePKSDTdJXJVGT3dp9k8XXn0GAOCoqQyQtVNbGMWE8oobJZmYqGdNDa_pl5ZhNge3V4jMEHktX_6Seq8i6KAYJfmEfoLGcOtj69lQtYOLIwXzt8l37xhC8HpZjXoRX0J7gtljeXhLECVRW5BtcT-a4LqNARksGyQ9JPsDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موساد چطور از اینترنشنال استفاده کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/farsna/440246" target="_blank">📅 17:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440245">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf8d367916.mp4?token=aivbAGPeTfVBcrGualwotI61-C1CSoplT1yGVh3oAxlZHUIDelhRSWOtvO5grKbAQJPOA16qN8ZZeXuP0o5XLe1UznR0E_XLItgiTu0ygDxx89NvOOm8K4OUsnyA47juFb6DHbjw1cvoVgvdU_AoOHsqiQjrLir5WDwjtz52anmeNyS_en1HrMUKyA9LtCXa2A8i4rqtlG7wEAmVUuws5vCTSW0vzW5ddqEmen8PzgAnoL-Ngn31yALIC-zyo2NSDzJqLxR8rhB1ThrxKx4DiB-_NMxWrQ4fAc1nEvSOxHvfv2KzoqQDRiGQI51mKg_daAWRI7wVwS61fuNIa2Fjvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf8d367916.mp4?token=aivbAGPeTfVBcrGualwotI61-C1CSoplT1yGVh3oAxlZHUIDelhRSWOtvO5grKbAQJPOA16qN8ZZeXuP0o5XLe1UznR0E_XLItgiTu0ygDxx89NvOOm8K4OUsnyA47juFb6DHbjw1cvoVgvdU_AoOHsqiQjrLir5WDwjtz52anmeNyS_en1HrMUKyA9LtCXa2A8i4rqtlG7wEAmVUuws5vCTSW0vzW5ddqEmen8PzgAnoL-Ngn31yALIC-zyo2NSDzJqLxR8rhB1ThrxKx4DiB-_NMxWrQ4fAc1nEvSOxHvfv2KzoqQDRiGQI51mKg_daAWRI7wVwS61fuNIa2Fjvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پایان آزادی عمل اسرائیل در عملیات‌های شبانه در لبنان
🔹
حزب‌الله لبنان با به‌کارگیری پهپادهای مجهز به دوربین‌های حرارتی، توانایی اجرای عملیات‌های شناسایی و رزمی در تاریکی شب را به‌طور چشمگیری افزایش داده است.
🔹
این پهپادها قادرند در تاریکی مطلق، ردپای حرارتی نیروها و تجهیزات را شناسایی کنند و محدودیت‌های روش‌های سنتی شناسایی را پشت سر بگذارند.
🔹
عملیات‌های شبانه سال‌ها یکی از مزیت‌های مهم ارتش اسرائیل محسوب می‌شد، اما فناوری جدید حزب‌الله می‌تواند معادلات نبرد در شب را تغییر دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/farsna/440245" target="_blank">📅 17:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440244">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4rskXgv-hMXw5aWW0--wKZ_2bYvCERTp9644sHSbgiatAA-s8n7RCyZLI39ddKvZYu9XB7HXpDbyVC2hg8RC5Ie9Q0o0q-r4yNK6dg_hoZlxSqZs33dEycQRkKOQWHQyjdpgz2kq4dNp_Cyf3V9iWn4kNTgd-Kq7veMaXqinrtd1qoVeuvAeqlyWMcI21m9rF5C1JHvSqPvfmV93nbT0TjBMlB-d-Msjx0nc22uAPmzWatMlcYShAMqe7vITbwQYRtbcMo9LxEuDf8k-WObiPLUN4Vv0qVeIajN2gdPWxv74IbEZgxKyDRUZl4wWqv7WU9lq8bi0ZeuFSEhFAkrGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف نیم تُن شیشه و تریاک در سیستان‌و بلوچستان
🔹
فرمانده انتظامی سیستان‌وبلوچستان: ۳۵۸ کیلو تریاک و ۱۴۹ کیلو شیشه در استان کشف و در این راستا ۸ خودرو توقیف و ۱۱ نفر از سوداگران دستگیر شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/farsna/440244" target="_blank">📅 17:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440243">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAod2PBjkGK2duThSvGTTtuWCbiysFky3Vyrqvt29WIDoZ7D-_B-A9EEm2xDsHKEMZllUoUMVeUp-HcuTIANqEq4_rhuccLxzmgj0im2xoP7QleUvxQx1AeZN87ZK3MLTuVQY_6cQFzDL8XXwuvuX2uZsWfW8EOtvdejmhi-TpF1z74VmnyTIwmSUSbZDKpEgCfVsR8iOfqxXtKUSK4pG2tdKPN1lR7EuPByO3rJca2gvtnNKC_GpA2O2yJLyOcX98YslN2tqBiJ9JYwnaRstqpzYJkmqXHusuVXqYgdZK6TNpozhndmD8HXrqypbivz660PwVU0QXuvrnuwoStSRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سهم فرهنگ از بودجۀ کشور؛ فقط ۱.۷۴ درصد
🔹
تنها ۱.۷۴ درصد از مصارف بودجۀ عمومی کشور به بخش فرهنگ اختصاص دارد؛ رقمی که معادل ۱۰۴ سال فروش سینمای پررونق ایران برآورد شده است.
🔹
درحالی‌که کشورهایی مانند عربستان، ترکیه و امارات سالانه میلیاردها دلار برای توسعه قدرت نرم، تولید محتوا و زیرساخت‌های فرهنگی هزینه می‌کنند، سهم فرهنگ در بودجۀ ایران همچنان محدود است.
🔹
کارشناسان هشدار می‌دهند تداوم این روند می‌تواند فاصله ایران با رقبای منطقه‌ای در عرصۀ فرهنگی و رسانه‌ای را افزایش دهد.
🔹
مرکز پژوهش‌های مجلس پیشنهاد کرده است بودجه‌های فرهنگی به‌جای پراکندگی میان دستگاه‌ها، در قالب برنامه‌های ملی و پروژه‌های کلان تجمیع و براساس اهداف و خروجی‌های مشخص تخصیص یابد.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/farsna/440243" target="_blank">📅 17:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440242">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a67006c458.mp4?token=Jrg7yG8fYtytZRJN1huqMJcxPPd7Y_VK72vVbgm8mj7gicpAPpz4WOrfuo6zBr5qi4Aw8ZTf6bRUiws8d4b5tnTgfpjzzRDH5lC5z5T3WPaO_zdYIc1V_jR9kvZs9jzuW02tpC185O3vevG1xWp48PvVxTqvNOV9bUWJL_SVcGWn8uBRK2GgnW3nmKa5U8fqZEA85K-KqyBjZMk0FSRd-_QNLwaTBDnKRo92XuerbjrTwpbKlS2knyAFnKDkoeSpeuh4lJOhezZM-Rw93Oaoco-ID4Kb9Z5MWx-KjkyJmc2MllNLKvOk0cQuLhF3mdobYbdp2YZq6bwA_eZxteGUOoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a67006c458.mp4?token=Jrg7yG8fYtytZRJN1huqMJcxPPd7Y_VK72vVbgm8mj7gicpAPpz4WOrfuo6zBr5qi4Aw8ZTf6bRUiws8d4b5tnTgfpjzzRDH5lC5z5T3WPaO_zdYIc1V_jR9kvZs9jzuW02tpC185O3vevG1xWp48PvVxTqvNOV9bUWJL_SVcGWn8uBRK2GgnW3nmKa5U8fqZEA85K-KqyBjZMk0FSRd-_QNLwaTBDnKRo92XuerbjrTwpbKlS2knyAFnKDkoeSpeuh4lJOhezZM-Rw93Oaoco-ID4Kb9Z5MWx-KjkyJmc2MllNLKvOk0cQuLhF3mdobYbdp2YZq6bwA_eZxteGUOoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی دولت: کارت امید مادر در بستر کالابرگ الکترونیک فعال است
🔸
۲ میلیون تومان به ازای هر نوزاد به حساب مادران واریز شد.
@Farsna</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/farsna/440242" target="_blank">📅 16:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440241">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxyrovffTH0kdENQsoupdPOr8t_rNtKDAvt4qrZAwbS3AXtstVtIw4kY_UZYk1f96WWT8KxXYBCUcqTiM2Suq24bAsH3dz40dfn9QTGkcMyPt0eqUtQKvwgB1MNMdOpCuW4gXtA1sgwC8OvX_rvF2vGgJgIqSXVI_P1-rszot7B47AR8PkRMdBot-7GwWD9Q2CC7i3lVlAzXI_CVzQhEB4r1G54B2QUOe--WVrt9RvrWWSlW5iIQqYvdTSxXj87YisWShewUrzTccw_RFuNFnTbJPqgJ3IrMvO_ru2mjmPBUgc62qseLsjkMJIVPFwU7xEKjpxyQ_MmJoIno3HwOeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توسعه پایدار شبکه ایرانسل با رویکرد حفاظت از محیط‌زیست
🔸
همزمان با روز جهانی محیط‌زیست (۵ ژوئن)، بررسی شاخص‌های پایداری نشان می‌دهد، ایرانسل توانسته همزمان با توسعه زیرساخت‌های ارتباطی، افزایش مصرف خدمات دیجیتال و رشد تعداد مشترکان، آثار زیست‌محیطی فعالیت‌های خود را مدیریت کرده و شدت انتشار کربن را در شاخص‌های مختلف کاهش دهد.
🔸
بر اساس گزارش پایداری ایرانسل مربوط به سال ۱۴۰۳، در حالی که تعداد سایت‌های ایرانسل هفت درصد، مصرف دیتا ۲۱ درصد و تعداد مشترکان چهار درصد افزایش یافته، خالص انتشار کربن تنها دو درصد رشد داشته است که نشان‌دهنده نقش مؤثر اقدامات بهینه‌سازی مصرف انرژی، ارتقای بهره‌وری شبکه و استفاده از فناوری‌های نوین در کاهش آثار زیست‌محیطی توسعه شبکه است.
🔸
علاوه بر این، با وجود رشد مستمر تعداد سایت‌های شبکه، نرخ رشد انتشار کربن در سال ۱۴۰۳ نسبت به سال قبل کاهش داشته که بیانگر اثربخشی رویکردهای مبتنی بر
#پایداری
و ESG در توسعه زیرساخت‌های ارتباطی ایرانسل است.
👈
جزئیات بیشتر
@irancellnews1</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/farsna/440241" target="_blank">📅 16:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440240">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-27L6yhpsaNsz-6cuynA-Y65wcmLePGwFGSt7skSONrq1avBmyl-ks48vWMMpjaEhJEbijXZqX6CFuzZL9-5z7yPoWEUD6vNqoZYzDmvuR0jj8bT85U19JetfUYiUWZtZA21bniUmhOqFEesxDYC5U9OUtNGnq5NQG17fLzIcdYMjmwk-SxmnhvOy3qyIl9VuNXyxnuktTN3KbcTnwnyjeJaai7F82LaJhDMTM88a0YHs5cfcHnmx_fYfW4f1zbEZRbBGiy5_0wdRST8OUCEUwfTw9SXxeMgQB5ZZHCl_jaSOVYv77ze4bVjznpqM8z911aQf88rrgbLIznG0P7oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای همراهی و شرکت در پویش هنر برای زندگی
لازم نیست هنرمند باشید.
هرچی دلت می‌خواد بفرست:
نقاشی، دل‌نوشته، عکس… حتی یه خط ساده.
چون هنر راهی برای آروم شدن دل
و کم کردن اضطراب و
خستگی‌هاست.
آثارت رو به پویش هنر برای زندگی بفرست
تا با هم، با هنر،
از سختی‌های زندگی عبور کنیم
شما می‌توانید آثار خود را
اینجا
ارسال کنید</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/farsna/440240" target="_blank">📅 16:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440239">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/farsna/440239" target="_blank">📅 16:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440233">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0eb4b0122.mp4?token=X98esLK553qDpsRNyWiVoPY0iuuy_3SC0R-26Q4lgF6OU4qod_o8ZED-OrnjeJvll3c9WBybpTiyfgqp1OnBviW6eHh9H28VlHtD-LPl3dFpHWDtsnhYTq0sSetPoJ1EoaF4SKGiX85o8zfwFOEvgWWj8SBdKOtOQCT8Jxmn2u2ZAr2pshkul_UR8g5ZTRvIX2YanD-s_RmYCE1CmMyhYgxwPIcdpFZllFSoM9asMuuUK0ArfHnUSgDxjSdBvdm_EVPhc_1sGPQKviLt5DuHskQ6BlaZsWQgtJie9gN8ZncRkwmZeq7ToIANFVKdIbZU7JTW_cTIHywVN_XUjqBiTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0eb4b0122.mp4?token=X98esLK553qDpsRNyWiVoPY0iuuy_3SC0R-26Q4lgF6OU4qod_o8ZED-OrnjeJvll3c9WBybpTiyfgqp1OnBviW6eHh9H28VlHtD-LPl3dFpHWDtsnhYTq0sSetPoJ1EoaF4SKGiX85o8zfwFOEvgWWj8SBdKOtOQCT8Jxmn2u2ZAr2pshkul_UR8g5ZTRvIX2YanD-s_RmYCE1CmMyhYgxwPIcdpFZllFSoM9asMuuUK0ArfHnUSgDxjSdBvdm_EVPhc_1sGPQKviLt5DuHskQ6BlaZsWQgtJie9gN8ZncRkwmZeq7ToIANFVKdIbZU7JTW_cTIHywVN_XUjqBiTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بمبی که در آشپزخانه منفجر نشد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/farsna/440233" target="_blank">📅 16:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440224">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eslRpus1zegWbiLaKzHXAuWyXQvyOciII0iE-cPTYNnQbSw5gyfrWqn1YTiZgmLUI_4hDSLQRvXS0HoV3ssakkoaCv9Qy0tFR-5xFq0xnZwSS3EWM-PpGor3ZGI1zcKyd1S_L6O_Iyps2SEhRB7KSf7DlwMZHyLZffSyZhao3dvM0Q0gMmRpNYzphD1FBdjNVHdW8Z4NlgUVHZKu0o5BlInjMnGCtBfCVaAm7tYfJwkloX9vpxyZq4v2786kUrvgtnnqNhK6dhFpGzo1yPlQZH0zEaSjpdetTWCs8KfaLPWqY16Uu8QhAfUybtBLpWKakSunuWnxUneAcGNun4FMmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cRD0FgwREs-HCO1V6HWvbEb7eE72SDYbxjaVAiN7jZwO0153oMh-9xhIQgsJI2HOS8hbddwidMEQva1YQre5IkACw1XJZoSRmcuAdiq5st-ok8VEalmbVB9w8e-RxWcSvVIjnI_cbvqbaiArSNu4s1JtVPq90qMoT-1KMWVibvao-be1gMMPKg6qPwK4V7N3D9NtcKqkAd6vh2Ck0yOiEGoclLnrwiBzz67IE_yLFwD_WrcyRb-GZDx1aji5_ABf19eATXHhGP6vzxC4BeHaE_8V0qnj8-vPKCKnYJ_PybjaeVS9IQHaSTQg7xzo_Lp7QKzvZjk2I07PpAIV5mYCNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MNZSRbOodtPsQdcgRXXhNF5CTwRCrFbCTLd3_riGEdg4WD_wJCk8b6PeA9iqUD8EqDjlieiUSYjUuhTkms6-MoPKGzvhryLJaxwljkUBmsQDWSq2vy4t9mKH-PYlLAQdgBaGRCRZ0o19u9DvXch0yUFpXgPbWN3prvwRndFF-MBP0mczf8P-pPiMKW3Sg3t4xxJ9lc2V5Z30ba8OgG4mMTDlNLewnHcwCBwWmpC_y8jksjX3AZxCtqFRwsBBxGt3VkY0fl3-Kjvf4zIhOCGXOko_Vl1bCdDULLd1oXsOybxVO1W3kxSAxqfNVOmgZ3zb6wx9kx2WWnAYzqKqL0JJ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GuZFBNaz9C2meps3kFPCq3W2YGJ7WfkKUq-oQnd0inuu2T68zox9oNZ5y9z6syDE7fslDx8elzljg7ZN-Ztjt1djEAGPooc5xPEFPrPrA4c-tBsPB6Fjx9N_sVUCg3PpNwQ7QTaD1g0ZnkXNJ2yBDFNwOS2qGIh8VFW0phMKZKuGryJZbUsNTTaY_EHsx3RpPwQerODcSADyj8DMEPKSiZIQnS0bARMNnqV2Q-9_hbp-8-VSx5Q-sUzyMiBvDbpAp_bRkINMBpTae5J0ldGR_NdiskFv96bAwKZusSGU_mXYiIW3I392mnfai5VQzvknKiLlz8D-I0qYe9hkut1twg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R7Ug3ab4prWIm83Z0-sMSORTcFCqL5RNsPtxXoAwjrESTDfXK8CSkOP9iG-Z1Pdxc3WaZdeN5efKMKnsTqdQXDJK_ftDz5Quau6q-y1HUDoz221-owdK_AtoFrcEsG_y1fIOJqAhs8C0jFBrjU_wLcoFlEx8OSfHLYBPgzoiBPpnHzMJDinCqpdZiNJo4A4ttNO7QON1RuDCCbSdOcf13qVJ0av0gzujqGdoUJnEP1MWtINdObMvq-1cRB9BIgGm1j4pMHFPlF9e2RzRuZKtZeDsHHKs0gXlALousSfQyKIOET8jv68fVc-hQVr77GKAvygjjEP0U6QBNVKvWeBLog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MVp_YtRuKMv1cMTHGDyiHVWHyhiFIrmaH3TJpZQDG_48UtMUwYaMJq_SlRSCUtbs6VsHv53zcdn6r8r_jE1oZG0C2iWLrM9eUIcPWOwPRvUi5d9nIF6l7AEl2oLieG7wK5Fhrk1qx5_9y1VfOhDAnYaz3AnKLzZUDwFoDPDiIok5wFr9RSvwL322LhBkZsLjJNDDuAIpQC9BH3J-Gt9Ntb6qVBLJn85Fv3PxVOQuvzBof3vAKYoBla7hEmoDoUsCJg5Gc3PFLRzJdiBk-H2VbyrZhMPNHmXSGsnVoWwyDXI9mdnov3qWttjyZCVWlXLv9-sr3dKoesQtJOy1wG-v1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bKKtXZSEEhdASi6FB4j8KuA9dws-I7wA1tZ40wHYxRon-_CoDOMlGmaqdp7hkkx4MCYAPqOaAtCTZMoRbK_AsASQSAm2hPq3asP5Qzk8gfiBCV4ttniByfGjJ7rFH_HMytRIjXB1iYZcZjgqi_UKRkq_UeNYqyRWZ4SbeW6QoFfWUnqO9sFVsW8wFJvWuDkvzygZC4ImzBETl46lcWYOIjqYZ8JlLtHbqCSRuDx5-PnQ00YFQHy6ESJHMf8wrSGljaYBF1otjxthrmfOAYmo_pBt5IbmgNZBlck90Z0z8kYRsiQYUsY5Qv00FMRFheGdtpmSVCe53dETGuIqb6tBxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kF0ubiLtEVXDCvC2y9gSSm86yX6QR_dGqBCyy9-ghPQCyDn-85DSQvHTcNIlI65eMnwZqo4JtJ-qTJ1PzSIDzie9hS_Gumtu8x1mltaP7uXJj5gip0mBR8CbqtFpxUisXO6A2b3cXgAGh5ATtijCFNCejRZV99TB0_GyKK2uTiNE2ZOZ1HS_7TX7shdztNO8HOFJGCjeRoS2xrFdBl9qPTTu5FOkSdmpSAHpOzrry0K-Jl9p3UrNJLJR0CCSsj0DzebK2UP6o3LW_RxpoXiCIrem6zq2_fgANYK26SZh9VABfbUCPYgKyxsVMOyQK0t4uUyZtNvSBNkmmTQisMhCFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DATJ6gSCORQSyKKV2yAGrHZzYL1Ak5gfF-hNZ4Nzyw-7ISKrpx-N7dj8V0ZXuuNcW19MBukp5aZtdYQYtGl2ULWH_-GvOFThglhDL8BkfSHhr12vs0hJU7q8Z7oiWIyKf3WNylaXpSZOSwiLGWd-oPFmTHJ372Momrelki1r4Y0EFGNvo6jaG6zZCqFQHxnHHJtwCJfrCNtk2sM9-wws3-6GcJfxa_chEOg9QyLKBwRoraqi_O2eF9HUPkob-PkN3UIdbkWBeXsUsC8WhAXoJDZHtnbjoivI0uRo6CthGO1FZWMWqM2qscHbj94iarZDii2TrKNwMcr1T5FJvHUQ8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از اعضای تیم ملی فوتبال ایران پیش از عزیمت به مکزیک برای حضور در جام جهانی
@Sportfars</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/farsna/440224" target="_blank">📅 16:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440223">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98d6f7a76c.mp4?token=EieFoVE1aoljvWDCpSbKd4hiZkMWqc4W19FK0vqwc8mgX0FH0HT96oI8bi2mNzSvVI-BVVZFeQ71yhiBiPZnxqOg5rB7ox60vr6VAuWMpaMIPCN9u6uyWKo0uVbBxwKm1wPxyxF-3xbAKiJvZevVCyfYdJ9fp3QUl4CxWXBbu8cJusJrJS6NlxGr_8nrCkNT4hp0wNhvbiX4kwjOc98QMm5pifuEEhX6LsozQLv4q6IbtDcu-fwqQwEFa8cHEzose_SzSu6xH4oEKaCEKBsFwLTnhRw4nFQ3vvHvzbJvrNWjd9KEamCcbjWaTsz2sivApzkBmeBU7uI5nHE2A6puTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98d6f7a76c.mp4?token=EieFoVE1aoljvWDCpSbKd4hiZkMWqc4W19FK0vqwc8mgX0FH0HT96oI8bi2mNzSvVI-BVVZFeQ71yhiBiPZnxqOg5rB7ox60vr6VAuWMpaMIPCN9u6uyWKo0uVbBxwKm1wPxyxF-3xbAKiJvZevVCyfYdJ9fp3QUl4CxWXBbu8cJusJrJS6NlxGr_8nrCkNT4hp0wNhvbiX4kwjOc98QMm5pifuEEhX6LsozQLv4q6IbtDcu-fwqQwEFa8cHEzose_SzSu6xH4oEKaCEKBsFwLTnhRw4nFQ3vvHvzbJvrNWjd9KEamCcbjWaTsz2sivApzkBmeBU7uI5nHE2A6puTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازسازی همه مدارس آسیب‌دیده در جنگ درحال انجام است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/farsna/440223" target="_blank">📅 16:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440222">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‌
🔴
وزارت خارجه: نقض مکرر آتش‌بس از سوی آمریکا ثابت می‌کند واشنگتن اراده‌ای برای کاهش تنش و بازگشت به ثبات ندارد و مسئولیت تمامی پیامدها و هرگونه تشدید تنش احتمالی بر عهدۀ دولت آمریکاست. @Farsna</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/farsna/440222" target="_blank">📅 16:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440221">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‌
🔴
وزارت خارجه: حملۀ آمریکا نشان‌دهندۀ بی‌اعتنایی کامل این کشور به اصول حقوق بین‌الملل و منشور ملل متحد است و نیروهای مسلح جمهوری اسلامی ایران با هوشیاری و اقتدار، پاسخ متناسب و مؤثری به این تجاوز داده‌اند. @Farsna</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/farsna/440221" target="_blank">📅 16:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440220">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
وزارت خارجه: تعرض نظامی آمریکا به تأسیسات راداری و نظارت ساحلی در سیریک و جزیرۀ قشم، نقض آشکار آتش‌بس ۱۹ فروردین و تجاوز به حاکمیت ملی و تمامیت ارضی جمهوری اسلامی ایران است.  @Farsna</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/farsna/440220" target="_blank">📅 16:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440219">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
وزارت خارجه: تعرض نظامی آمریکا به تأسیسات راداری و نظارت ساحلی در سیریک و جزیرۀ قشم، نقض آشکار آتش‌بس ۱۹ فروردین و تجاوز به حاکمیت ملی و تمامیت ارضی جمهوری اسلامی ایران است.
@Farsna</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/farsna/440219" target="_blank">📅 16:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440218">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02f48f72d3.mp4?token=v1Rq0Cc_3mTPO2woOPMAhiz9y0x_MktFPVlvKolBLbBZvK1QswH6DYZXIRvvHgXFh5Bi5q89CuEit01BKt7GhM7PH3hOQqs5W2gzRBzytS8aTrjlgF-cENheuTNHmzSiabsZGdtC4YyeyCSkI7SHY__uFh_dOdzI_AjyKx4RSwsjqNaZHOCOD9QtytdKXkIQVsf4ITFnZKFpLq-HFXA_14z3UZzyZ13QcJa_Cim8ODTMTGDxM4hctJGzBifE7EbGBLRWeWq-V9yhsHaxx3l_bsNKGaPqH16C5PfYhh4KoXbijZ5ZOsPk9lMMCKtdIRNpOs-i1TIedNVbSZIa3euNqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02f48f72d3.mp4?token=v1Rq0Cc_3mTPO2woOPMAhiz9y0x_MktFPVlvKolBLbBZvK1QswH6DYZXIRvvHgXFh5Bi5q89CuEit01BKt7GhM7PH3hOQqs5W2gzRBzytS8aTrjlgF-cENheuTNHmzSiabsZGdtC4YyeyCSkI7SHY__uFh_dOdzI_AjyKx4RSwsjqNaZHOCOD9QtytdKXkIQVsf4ITFnZKFpLq-HFXA_14z3UZzyZ13QcJa_Cim8ODTMTGDxM4hctJGzBifE7EbGBLRWeWq-V9yhsHaxx3l_bsNKGaPqH16C5PfYhh4KoXbijZ5ZOsPk9lMMCKtdIRNpOs-i1TIedNVbSZIa3euNqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی شهرداری تهران: مردم کمتر از ۱۰ درصد هزینۀ مترو را می‌پردازند
🔹
شهرداری تهران هر سال مبالغ قابل‌توجهی برای توسعۀ خطوط، خرید تجهیزات و نگهداشت شبکۀ مترو هزینه می‌کند.
🔹
بخش بسیار کمی از هزینه‌های مترو از محل فروش بلیت تأمین می‌شود و سهم پرداختی شهروندان کمتر از ۱۰ درصد است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/farsna/440218" target="_blank">📅 16:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440211">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KWw4S5IhPA9HtrL_O2TWP9NzhPiySzoC9B950yu3d6wwczeYAULDcY_Y-m57aUo-Be6JHHDZYPaP4EFtL1jfo2bmzNymajfTIioA-crKPSpm-rblQ5vDf4v1gJy-onkj9-783j5VihsaQjn_oGgpW7S6DGf9Kgod_59W43onkrl8zqPltKhqBt2Uu1WuIYq7SzPb0pJCOgsRoFnGK4TxIgbbW-dcYDSMv-1uvDb2Zg167RylNoN99IL_R47Kf5q_IWDGG-jxKYOMuA0-VYL0ZkL1ryABYOAIr_6sI7ZqeGLpzfc3kL1VzZw3AOW_o21KMwGCXT9NzpoOUJ2k6QSiSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rrUBIZf2i8nz7HcwN_BbzxZOe-50_ntlO5TaugMODHefRFjs5licuTVXCb9rNVOTcvNgipTDNWgFyj7UQqzL8LbSDGgqJ9LKi2fPN94xSLABRvmBTje72Q7t5Av4T1rYM-PBu9YmUzyqwVq-7yjrJdT9BrW8Aob2v3o4qHtB6kjeErc3Qv66yDF0FAbLRAOGtXtbwKiFEk8mHd2Yz2AzBB0CBcM-Ho9WjW1P_qKXv7p024cl0JXrpAYcVOqaNlsShKWQvYm-ryy8Z45TVet03lJqSFiuTRxRhxbwotLCk7dkemXOMaekf3H3v0vEzY4tpwSBL5ogHzDamoKE1T6JPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r7AVcJCaIjnw8hAlpXy-Nwl9aOTsdd_t-owrKpfvjC1p8rYYVaC1QJ1wkrsklT9TClFy6hkqwT8CRYrSMc_2T5e7GQavE7NLXPIBpY2kekR8XORUOezU6paFFWsUKtVamVzHt7iXzQoHMZgNuChWTSHizyZpQVBhSxvDpasXiXMIXKSa-6CFzvA2jLiFzEjw0KjrcvOQvGbKfFn23tGjAmrCw4oxOt4goQc5czb_pFgef8idJHgGE5QMMFNgpzOZ6_GfDv9148mQZfUSi8dG8dpWA4CFjUy3FJmSiuxbXA-HjwrX7RjPjq4wJJrmUhcLLD5Z47bDNs1IDt067oOdTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VGnNClAQUMvOGPGaLSiI3IdoSDL4LO4ZEQEnw5WrGWw6SfQB769LPohNnIGa8Y0mV6BlaT1EPHRxenWhm8A2qD2UZiK3zurjMX04XJNscDTCFdGcoGSc2VKi5wjvzypLLnJnaQNRVYN-2zlcC8mM-6xc4fRTn3sEBM_VSpPw-0cNXmao7wly-xZdQ_kGDYrIE2kVlLxgFojUC2puGOYh1INQk0MSKH3-h52GY8uqezAnCx5twsNVraQ_jXhYb9LmQnhpP-69bcVxWpDuhWfdx7NwLMB4-RRLVuFLorVQE1jXjqvR3UEyi2Hf81z0tdwuJkURzL9IKK9iD0K2FnphOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SKPh32yICVPFyWti171DdtXlT1BLZLNQZbWjXfu5QTRIxvaH2wke7qPD1in69pDYcxP_tv5GPJBOFw5co0-DswXxgO19XmEgZ6aA6dtXWcfiIQVCPsNVV1ZH0GNvHQjgnrlJfLJjSjpRrDGuUeq56KcAm6OkvCOWNSNgcmZBdxn1xSr9yoHxuT1KpXRCOI_ovvlC1bpJTkBX5rTbiFmjpb7v5ffMwPel-H5Ki1Z5ZH4rmryl6MWd0vgWpW4LsR9hM_wOIw1j4GkkXnoKrPoTmbHM3EqgIWN3VopI7knrObA0CwVrMuR3t1H7F3oRQhOXXDisiorHyqkkTYKGYVbbvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iT5WqgGQN-QZO7Y7cY_e5JzILWfQvx79uPzc0is205wSOt6gNzUGgumATKBb8djbmtHgqDgyMK8RYDFnOMPN94ZDDpP0tPsyF17smVCkTphzkYcAh0vh7QUKd3on7t6f3eS5E0AfL5pbfR9ZYHsDVVIK0VfpRVowvMxIo9cu5hTRWMrdtg67AU83Io_nc4pEPPH0hk2KKCHTLduVQz47GCWMJxbIvrKpzu5ufQikq6jwDVp9iPM2GaDQcZQOYHLcYnJ9B-HYQv-6eHoIjxEdF2XzAkuDo9DO2zJNVc2TvkJ_0TRaQDKWOfE4qIBQ9CVPPPcqfwHD8bMw0PtXJr5i2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/afRgyfH4hhtoqfSVgARN6GPj3oAqCHJ4UwvYFgEspzy6yW8-0qAO84PkrmXmg8Y_LxxcTKttAQ10zp5DdiHsTl3bh_H5jmwyDArjOYtF-UQd2cmE6Uj8EjJ92xAVVlKkOb0ODtWENz009NzdXNkp8GEm7qQql8bb-eU9bDB7LtW1QpgMuKrnPJw-Lsnpsh0MRzuCmxkFteQBGhWxJRmdAcz1LbEFpoymp-ejxphsGj_OmufIaW6amX560DG5ywb9wGdjPBWNUidLvKy-7YlioD_aXCxmVO_uwszYfXAfZLKyPxFbZhos-i-I0SZqbTD0-EWxAQXLlpp5jLnpsAoMHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
گنجینه‌ای از زیست‌بوم‌ها در فارس
عکس:
احمدرضا مداح
@Farsna</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/440211" target="_blank">📅 16:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440210">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">حزب‌الله از رهگیری و فراری‌دادن جنگنده و پهپاد اسرائیلی خبر داد
🔹
حزب‌الله اعلام کرد یک پهپاد هرمس و یک جنگندۀ اسرائیلی را رهگیری، و آن‌ها را مجبور به عقب‌نشینی کرده است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/440210" target="_blank">📅 15:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440209">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4FxlRurQLln5E6BYJApHU2YQ3fs1zFmu8DRiwcyT6JK8r9eVm7irprG_JORotmXkStu630n2rD2tU2v6iBxR1LqWLcTdWc78tW9y-mcm8eNooKYqFdW5p9Dtc4haOH_is0UmvLrdry08aWaGgWOzdmwxUhNdwrqrbb_QAZWEigtgUk5axclBtE8f0I3cX1Ji9jWeyh3xf_parAjCY4ufMxTQlPIqC-xTye0lA42mtTicxrjzCncfInpCZ8y0sbSuyM9NJrQxEA5y-aP4uazS9LT_FsJXZujm6VknaLAZvDbqTCHcXHlE1jKTfBaxWi6tPuJn2KyDzaOxP0GVyYmLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی فوتبال عراق به‌دنبال پوشیدن پيراهن سیاه در شب عاشورا
🔹
فدراسیون فوتبال عراق به دلیل همزمانی بازی‌اش با سنگال در جام جهانی با شب شهادت امام حسین (ع)، از فیفا درخواست کرد مجوز پوشیدن پیراهن مشکی را برای این مسابقه صادر کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/440209" target="_blank">📅 15:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440208">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/103ca78e83.mp4?token=blkreUMfx6AM4eUzRebFLIwfeI9G2XF9Ms7UgqAcu-xfflYDJcBhcgj_YQ5aqPZf8avo0xUztw3R0H-UH3R6Gdt_qnhxIWc2QHcRpLBLTHLs9wxQRZm3FQMIn0LuNPay52nUt8SN7xBqbYUyM0OwKEj8yA5fq1vzVEWDKsk2gmy8eK77iXjWCghquu9_13qEH26sCEFlmuup-6-w3zgMmPfAlZFjrRLgL8W7fJ5ZhP8vvW9dUpJTmurfc6y5dwNWiqu2WUMeKXaOu4uZecX6n3n7Yni3sNq3wKdaZOuxf9x1beqP3p-EBSUaXS4cJBi5KkYqp67u1HT0roma5LgbqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/103ca78e83.mp4?token=blkreUMfx6AM4eUzRebFLIwfeI9G2XF9Ms7UgqAcu-xfflYDJcBhcgj_YQ5aqPZf8avo0xUztw3R0H-UH3R6Gdt_qnhxIWc2QHcRpLBLTHLs9wxQRZm3FQMIn0LuNPay52nUt8SN7xBqbYUyM0OwKEj8yA5fq1vzVEWDKsk2gmy8eK77iXjWCghquu9_13qEH26sCEFlmuup-6-w3zgMmPfAlZFjrRLgL8W7fJ5ZhP8vvW9dUpJTmurfc6y5dwNWiqu2WUMeKXaOu4uZecX6n3n7Yni3sNq3wKdaZOuxf9x1beqP3p-EBSUaXS4cJBi5KkYqp67u1HT0roma5LgbqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چتری از غبار بر سر کرمان
🔹
شاخص آلاینده‌های بالاتر از ۱۰ میکرون کرمان به ۴۵۰ رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/440208" target="_blank">📅 15:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440207">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNnS-3PgDMqbVpoLHRgnoZ7Yzg-iJbU675SF6IIiJMGKm1WgphovK-UnLCg8TYEvjHg-buBUkE_UBgFm6oX2fCn3MU4R-KJZo6sTx-7eVfPlZGUG-euAcTHZe7s58HY08sGOgB3EGBb279Q9Az-jBQP_O0b_hrl99Jr9LPBhDU5vFnsrff7q3jjvHvwY71INpef_uK-JboA1rtCQyJMkrVyaaAotl0vszYa3laXDhykV9_kH9V2sO0TAwxps0Z8owlr2mh6u7A-L5Cn5rIVfbBk9NUWVHkE2QZkcV6ttHVh9E7t-oCzyEx2XYJJzvA7-zl_i8UMDKTDy0hHoCG8plg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه‌های بزرگ بدون تأیید محیط‌زیست کلید نمی‌خورند
🔹
با تصویب آیین‌نامۀ اجرایی بند «الف» مادۀ ۲۲ قانون برنامۀ هفتم پیشرفت، نظارت محیط‌زیستی بر پروژه‌های بزرگ عمرانی و توسعه‌ای کشور اجباری شد.
از این پس:
🔸
دریافت مجوز محیط‌زیستی و ارائه گزارش‌های دوره‌ای در تمام مراحل اجرای پروژه الزامی است.
🔸
سازمان محیط‌زیست می‌تواند فعالیت طرح‌های فاقد مجوز را متوقف کند.
🔸
در صورت تخلف از تعهدات محیط‌زیستی، ابتدا اخطار و سپس دستور توقف پروژه صادر خواهد شد.
🔸
تمام فرآیندهای ارزیابی، از ثبت درخواست تا صدور مجوز، به‌صورت الکترونیکی و از طریق «پنجرۀ واحد مدیریت زمین» انجام می‌شود.
🔹
سازمان محیط‌زیست موظف شده ظرف ۶ ماه دستورالعمل‌های اجرایی جدید را تدوین و ابلاغ کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/farsna/440207" target="_blank">📅 15:17 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440200">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rYSMZfvDhS9zsdwxjeLocvwE-JaG411ICLj6u_56rb-Rcbmdu1ozcHV0KIbLawBUYySLc6lqB3jmIeObUX8G-zdazfG0ywUOklCpV3wDrklbYmR3pNB9G5NdQkejtRdMJeI9nKRiYf6YCsauU1kjyMGJLLO8Bzu8cejUwJy-0wKlbr9zWbuJhJDN6NnrZRtkHPMiMBTVPlpcUOGINe_tnLpxY6ZmR1JoJSL8bXFzY_93T7xfcMZbOjRPJw1BztHdxpKNweLlG0tiE9PE0dSOk13jfTGeuhFDsPXxQ6ER5jRk5GHa4_zBAZvclIHBJjlenwPOQigeznheqTIrcNuSOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r5Ej55CQMglG4vJANh-MtVI4tdGA2de6P1wk6SWAJ2PWYhnmXVqb6EqJgQrI-uref7L-R5etazXFrpRjFl0Kq77JUqho8V9pXXXE4eTnKXI9dfefqN1uLNLPT0K09qNFDE8lqfFycjPp-4mgR4X5kzxZUlJp0LQK-I79xO9zhY648GOcPY_-w50SNDEcBL0dUr6ZJkKrKV3_DnFWH3NnLXXWfM4Xi9lssQwpEIbnluR0pfRZAfg5OnSP-AkOQrm5a0y73G6CL5mwof9O2gXQQ2zUCVeK5F2ALWgxv56I83TihX6ty5Rc2kbYCzzCXogDaVexrtPGPmM6V6v07TISLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LKz6uNMVAdgUJIBGYzVmKDh2k-SOR2zbraN2wbxsAG8lpxoHdLX4_YfVKyx7rJ8abzk4w_2cAOrvx3gpFJPpkn4KueR95reUKAjsCWyn0J4gtCavGqDaS_ESEp0fVFhzSpPQbNbe3TVmKq-OLmelWPxyabG5Vg61HrfIBFHFgtYsOLceGc15cCRupp6yEQet_-4u9NWL3tCOifMreOevqte0AqZyN-gsvbpz4Og0KJcG5-0DuCdyE-oJWhjbGZJmUSlMhoB-oHo3Vtkogp6jOoyLYScSZxAlpoWU6oWUX72Cdq6kV2feJ3jT74yBWqA6z1Fknq7wXsXK7lA6dWcueQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LOs-Mea8GG0OuFWOVG_iJzFWz2meN25ez85Ibe1zLwiB7jV8RsSVk5DbJproldDCJ610HnUnhh2UmY6x7QY_EtPChY4uMAOHL8DAfHXf6uc8Y-sixByNV7mrBuY1UFHQ_lwyRBWRF6zkh9ydBE-yXrEMJiwR-gJC7ZC4IEC8vC0oGf8yryoCEx6H2rU1Bniva2PvKK62aNMTw2lYLKmHSny0Wb45CmEHa5COogvLxp1mWfQtzvHSXB0srDG5W0i-6ESMFsNcQDJQngxycAHdWY9uWsNapjO0v0rSzCXbMJC4abB1hYucRvtVoKh_iMjXAhYvJP_T--8VsGhlIZLbsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L-b3HWWtNG17ab7sLGe_m-ZSZjhFE_w3ohVgwx8G5l63VKYau9Bofjc5CiOY19BLSXcnFenLrer_D-5NvZtn30KcKKki7scFCVBOEcA2gMExV2uiSuH2J-i-4dYkZnLdzGTr64Y-8Y1nGwm4DHU7LQMti_m5aNQFa__7MdJ73vjzcDccW3xwn6pYoWOLiQpn7svcx8rgNxPOJFaeMlRqjUZRwzep-kGpTi1w2ZcHdM69yGfI5MzeY3rUrL4Wzaz8aQYQqxf06XGEbCHOfF6ZWxPmdqt5toVwtYJy3qygP2kVM5k8xEIm0Pnt4fSLWnIDC1_jjxyqQfZKBOhjTgeY3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hWTUE2PCS2bkSPWaNEgJOCqbGAJb3Ub7g6FFj4Qo4ATf-0-ZXX0mx5HeuWWhzQXVK7BRrVphDKQYlbSpA9TaaMotj0Qzn88iG703g9AZwqqDuzRjocIQnHNCdYsxCEoLo-FZYcunEtYJT2D4l_D56-OQTRHEfeyKMr03iY64YuBuYBWUsV6w6V2R16upZrUdUcjWVHhGRYLPn_LdJbQbPDuBNYP-Ts-DSO3cWUeLr8RD6f-ZLHX0VhczX3MDJruAEzEqjv6_27iHufrGICNAimd82Fl_o6-mK91YThGTeb8dzheudKoRlxHtlZDc3DB2H8Cvj3CReRRFhruaKJRJ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rESQAijo3AQ0LZ5UYjHqkx0BTdAJ4OFCruX9LU5DCIiEZvvgHGFFjkC74m3fdopNquYm4yfBeDaeT1l4kDMGNirfecqGWZp5fzzcarcfLSPeNI-OIXYPZ7CaxSDFOYt2K9umZCarF338TQOrJkhf3mvcbob5PTk6dXFJH2LotUflGVr2TxC1ptGa3-2it6VFrmwKT45JZBq8kHpCCJ6XbQYJi5FoctJpumVUy07Mwtzv_WZYvOat31EIBvm8SJdqTa8OZvlt5f6dF-BkmkCT_8q3HM1gPBWNSK8H6M0NfCqycZXDuGg9llyfZKU-DUbgPEpUqLrC-zbzmB1MajaGiw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
برداشت سیر در همدان
عکس:
امیرحسین ترکمن
@Farsna</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/440200" target="_blank">📅 14:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440199">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sd3p1tun8i4Ix6_P1xlsdKg0IizUGJD2JtFgMw2SCptzLX_B0LV3bRm6BPeR1UiYLZs5zMh8niXdzcSMjlgAg0SEAnMurXb9URX31PWGwvMyGpRL69fEe1UVR_c6QxadNk-szEGyK4Jj9kZte0QwxwiW8Fre0e42Eo5ueK16LKAC2MFalUk-o9yyEjqOVFCm8sN5jdBxb7W6Ay0Xez-rVQJfQzEFiOkI51G-Ym7s2jAoUFDNALTx75NMRv_c6Cb9BV2PGcdrnkiebQ4svjWdnLDG5XMLxgt1fO-l-u8Q6WQMadNoag1gN0iIjEiymq2_TH0b-OsFpdsmkhgAYDB_QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
برنامۀ آموزش‌وپرورش برای برگزاری امتحانات نهایی
🔹
وزیر آموزش‌وپرورش: برنامۀ ما این است که اگر بتوانیم مجوز بگیریم امتحانات نهایی را از ۱۳ تیر حضوری برگزار کنیم.
🔹
پایان امتحانات را به گونه‌ای طراحی کرده‌ایم که دانش‌آموزان برای کنکور یک ماه فرصت داشته باشند.…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/440199" target="_blank">📅 14:41 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440198">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f07cc3ad1.mp4?token=nzJDQ0v6fPs2OJmTHoiOJd2pOjSMbbp7va_hVv7rj18k2ufZs-jZ2R3jkk9btTBpzIgNYpmhSz1x9hKYhxF9KHtamzlWVoncHt5TusS1XNepbQMUV41f1neucH0ld09Ik_uIbBUC-TTIOTmMhwGaYwcWKFUj4Nxv_71xrWzjV0XhMPYZ2EXpzlVoxKg5cF7SKgpxfRuNkKg1VQYxc1_kvzn1jINhb0EI0Z8aeXxXHWdkwu0C40JjoJua9V8cVG6iceksiQLjBj1UNtvuvh66OasFkXVgq1F6tX0J2fFDnk7-7SKRHMhbwEKAz9rvSlNPEsGB-OAdrtNoZp_OIuueew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f07cc3ad1.mp4?token=nzJDQ0v6fPs2OJmTHoiOJd2pOjSMbbp7va_hVv7rj18k2ufZs-jZ2R3jkk9btTBpzIgNYpmhSz1x9hKYhxF9KHtamzlWVoncHt5TusS1XNepbQMUV41f1neucH0ld09Ik_uIbBUC-TTIOTmMhwGaYwcWKFUj4Nxv_71xrWzjV0XhMPYZ2EXpzlVoxKg5cF7SKgpxfRuNkKg1VQYxc1_kvzn1jINhb0EI0Z8aeXxXHWdkwu0C40JjoJua9V8cVG6iceksiQLjBj1UNtvuvh66OasFkXVgq1F6tX0J2fFDnk7-7SKRHMhbwEKAz9rvSlNPEsGB-OAdrtNoZp_OIuueew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همراه همیشگی رهبر شهید را بشناسیم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/farsna/440198" target="_blank">📅 14:28 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440197">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23456d3ce6.mp4?token=FLwJQzLB7hFXAgbbOaYprr9MO1PWZz4nIROL-JcXYYkm3tWPfxOroMVjlb6drbBE5cvyyBOIRB-N2TIYrvuD6542atjCnLVvo9Hy469XYkpCNCxU3eYDHPyEw_NiXL5JYfMU2qhQD8urnw1o9PRMZxFUK2PF6znGybPMolKtNZSUpSGKAyBKBCV5mts31nD_PSKLdOWmUZgjxnvASTiiJquFMRuXCVDiNymu_vlhqlENQ8RzswnjzZmpCEbys2BjPLv4UQ7XWOh6mHYw2aYeuvV6f_76o6FsBCvinQQOnj23SPx0XSV1W7grhMVdQMBEmGeWjlq7O7nTk3ArelkV-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23456d3ce6.mp4?token=FLwJQzLB7hFXAgbbOaYprr9MO1PWZz4nIROL-JcXYYkm3tWPfxOroMVjlb6drbBE5cvyyBOIRB-N2TIYrvuD6542atjCnLVvo9Hy469XYkpCNCxU3eYDHPyEw_NiXL5JYfMU2qhQD8urnw1o9PRMZxFUK2PF6znGybPMolKtNZSUpSGKAyBKBCV5mts31nD_PSKLdOWmUZgjxnvASTiiJquFMRuXCVDiNymu_vlhqlENQ8RzswnjzZmpCEbys2BjPLv4UQ7XWOh6mHYw2aYeuvV6f_76o6FsBCvinQQOnj23SPx0XSV1W7grhMVdQMBEmGeWjlq7O7nTk3ArelkV-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیا رقم کالابرگ تغییر می‌کند؟  @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/440197" target="_blank">📅 14:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440196">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در بندرعباس به‌مدت ۴ روز
🔹
استانداری هرمزگان: به‌دلیل خنثی‌سازی پرتابه‌های عمل‌نکردهٔ دشمن در حملات آمریکایی‌-صهیونی تا روز چهارشنبه در بندرعباس، احتمال شنیدن صدای انفجار در این ۴ روز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/440196" target="_blank">📅 14:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440195">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🎥
شهادت سرتیپ ارتش لبنان در حمله پهپادی اسرائیل
🔹
ارتش لبنان از شهادت یک افسر عالی‌رتبه به‌همراه چند نظامی دیگر در حملهٔ پهپادی ارتش اسرائیل در جادهٔ الخردلی به النبطیه در جنوب لبنان خبر داد.
🔹
منابع لبنانی اعلام کردند که این افسر ارشد، درجهٔ سرتیپی داشته…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/440195" target="_blank">📅 13:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440194">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‌ فهرست اعضای تیم ملی ایران که آمریکا تاکنون به آن‌ها ویزا نداده است
🔹
مهدی محمدنبی(مدیر تیم)، هدایت ممبینی(دبیرکل فدراسیون)، مهدی ملک‌آباد و مسعود اردشیر(نمایندگان حراست فدراسیون)، مهرپویا اسدی و سروش سلماسی(آنالیزورهای تیم)، محمود اسلامیان(مشاور رئیس فدراسیون)،…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/440194" target="_blank">📅 13:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440193">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abxjk47SKOQFfvZ1q6jr4Tu1JuwvmRlRLxcEF70IRvmocLBVzHfxJOmdGf8URDDByyz1chqZ1CWJZgnoZfbMqksbotGzU4DrzRVb5-ZFbDJI62d2adBCiSMXICP4E42uhCUxKEq8KK3szlcx-KCrMxigN-O2VaMV76aPnbkSn5jqeGvhWxv4WfdNwMCyyEPgq0Cm672gYDL-KBbe4OFPydAnwCvbJPGEHK26BCPvjsypmY3Ez1LYBSAhhmifpzBM-Oiks-MDtf5UAD-Y4PhrpBaA7GsYWBhdZOBOp4p07xykvfha-B5XXeqWwO7fVmpHSo5aI9aA46wcGXJXhuSqaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این چه وقت وسط‌بازی است آقای فردوسی‌پور
🔹
«گزارش این بازی را به همۀ مردمی که مظلومانه از میان ما رفتند و می‌توانستند تماشاگر این بازی باشند تقدیم می‌کنم». این را عادل فردوسی‌پور پس از ۶ ماه سکوت در آغاز گزارش فینال لیگ قهرمانان اروپا در آپارات اسپرت گفت. حرف‌هایی که جمعه با انتشار کلیپی در رسانه‌اش هم منتشر شده.
🔹
در سال‌های اخیر رسانه‌های غربی در مواجهۀ با جنایات اسرائیل از یک تکنیک استفاده می‌کنند. نوشتن اخبار در مبهم‌ترین شکل ممکن. بی‌بی‌سی انگلیسی در تیتر خبری در مورد حملۀ هوایی اسرائیل به لبنان اسمی از عامل نمی‌آورد. در مورد پاسخ موشکی ایران به تجاوز اسرائیل اما تیتر جور دیگری است. «پرتاب بیش از ۱۸۰ موشک بالستیک به اسرائیل توسط ایران».
🔹
سایت شبکۀ چهار انگلیس نیز رویۀ مشابهی دارد. آن‌ها که حمله روسیه به اوکراین را «تهاجم» تیتر می‌کنند. در مورد مشابه تجاوز اسرائیل به لبنان را «عبور نیروهای اسرائیلی از مرز» عنوان می‌کنند.
🔹
این تکنیک مبهم‌گویی حالا به ایران هم رسیده. این‌بار پشت میکروفون یک گزارشگر فوتبال. عادل فردوسی‌پور که بابت ریزش پلاسکو در ۹۰ بیانیۀ سیاسی می‌خواند، در گزارش آخرش چنین رویکردی را اتخاذ کرد.
🔹
صحبت از «کسانی که بین ما نیستند» درحالی‌که مشخص نیست این افراد چرا بین ما نیستند؟ در ۱۸-۱۹ دی شهید شدند؟ در جنگ آمریکا و اسرائیل علیه ایران بمباران شدند؟ در تصادف فوت کردند یا در بلایای طبیعی؟ در بمباران دانشگاه شریف، محلی که او در آن درس‌خوانده و استاد است، زیر آوار ماندند یا در مدرسۀ میناب؟ او که از سانسور گله داشت، حالا سانسورچی شده.
🔹
در سالیان گذشته اصطلاحی در شبکه‌های اجتماعی و میان مردم باب شد. «وسط‌باز». روزگاری شاید می‌شد از آن دفاع کرد اما اکنون پس از دیدن شدیدترین بمباران ایران توسط دو ارتش متجاوز به مدت ۴۰ روز، زدن پل افتتاح نشده در روز سیزده‌بدر، حمله به مدرسۀ ابتدایی و سالن‌های ورزشی دیگر جایی برای «وسط‌بازی» نمانده.
🔹
این دو لب جوی آنقدر از هم فاصله گرفته که کسی نمی‌تواند یک‌پایش را آن طرف بگذارد و یک پایش را این‌طرف. حالا آن جوی، دریای خون شده.
🔹
او یک‌بار خطاب به یحیی گل محمدی که در نیمه‌نهایی جام ملت‌ها با پنالتی چیپ شانس قهرمانی را از ایران گرفت گفت: «این چه وقت چیپ‌زدن بود آقای گل‌محمدی». حالا این چه وقت
وسط‌بازی
است آقای فردوسی‌پور؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/440193" target="_blank">📅 13:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440192">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">📹
«مدرسه همدلی» روایتی از معلم‌های دلسوزی که نگذاشتند زنجیره آموزش قطع شود
@Farsna</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/farsna/440192" target="_blank">📅 13:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440191">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-text">💚
لبخند رضایت شهروندان، بهترین پاداش خدمت است.
💢
همکاران بانک شهر در جشن بزرگ غدیر با عشق و افتخار، در پذیرایی و خدمت‌رسانی به مردم عزیز مشارکت کردند تا سهمی در برگزاری باشکوه این عید فرخنده داشته باشند</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/440191" target="_blank">📅 13:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440190">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/440190" target="_blank">📅 13:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440189">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAyvZHV1XNVba3VnB49UgUtZ4PoArCYu4nA7iSWpGzSA5hF92X1O4eMNRTo5ZYTbBXftxnecDb-9fMsuyj2fnvQVQ3_mSg72OPPG65LAzImXBZrlUQfQsgoSfwLcj99PqorNU9huuMlyyItxffMtWdT8Ncas4iXbmsbzG8y0csVI5FUaJuge5D7ADa9Uoo-OVYEBk1Wwx0Yv5xOGcjKz4xL_En-jHS8cxOpWMUx5cJO66AOmbUpeU7sKchmSzylZkmeDcPfi-nMssxw45NpEHcaNFRszXBgXsvBWE8XmmlU72c-TiRAXVswDPb7hI5FJib0U3vvUncG1rNHb4QQRJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نصف حقابهٔ ایران از افغانستان نقد شد
🔹
۴۱۷ میلیون متر مکعب آب از افغانستان راهی چاه‌نیمه‌های ایران در شمال سیستان‌وبلوچستان شد؛ این میزان کمتر از نصف حقابهٔ ایران است که در سال‌های نرمال آبی پرداخت می‌شود.
🔸
طبق معاهدهٔ ایران و افغانستان موسوم به هیرمند که سال ۱۳۵۳ نوشته شده، در سال نرمال آبی باید ۸۵۰ میلیون متر مکعب آب به ایران داده شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/440189" target="_blank">📅 13:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440188">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/705961b41b.mp4?token=u5QK-B38EUvHo-_HuYxR83wVlWJoQ84C-vVksySPd1YvmKk5_WNorq_I9mlc6RPtjs50Fdv79v4kn0Ti6rAErul8Dkvhallanad3-QvyfYiOzKEiDx_qKP0uAQ2EYL402kDe37WU2N4ERnnIGEe3AoJUmneJJr9W18Ui128j860vXg7fGDeeaM0GY6E5EZqqDfOu5e345sShHtb3o7pa3rnapLZg7NiQnp2IWIS9xC1b90TBdr6FWh8RhNbosvWeYMtaph47NrAYO_dx2FUXj1P5VGDuVAhQ9eY1vWAGGmoigbz7MNoTu4cFgEiDfhQgqq4toksfLvO0TzTdJVJahA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/705961b41b.mp4?token=u5QK-B38EUvHo-_HuYxR83wVlWJoQ84C-vVksySPd1YvmKk5_WNorq_I9mlc6RPtjs50Fdv79v4kn0Ti6rAErul8Dkvhallanad3-QvyfYiOzKEiDx_qKP0uAQ2EYL402kDe37WU2N4ERnnIGEe3AoJUmneJJr9W18Ui128j860vXg7fGDeeaM0GY6E5EZqqDfOu5e345sShHtb3o7pa3rnapLZg7NiQnp2IWIS9xC1b90TBdr6FWh8RhNbosvWeYMtaph47NrAYO_dx2FUXj1P5VGDuVAhQ9eY1vWAGGmoigbz7MNoTu4cFgEiDfhQgqq4toksfLvO0TzTdJVJahA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پلیس اراذل زمین‌خوار را در اقدسیه زمین‌گیر کرد
🔹
۸ نفر از اوباش زمین‌خوار که با شگردهای ارعاب با فراری‌دادن مالک یا ساکنان قانونی، یک ساختمان چندطبقه در اقدسیه را به پایگاه غیرقانونی خود تبدیل کرده بودند توسط پلیس اطلاعات تهران دستگیر شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/440188" target="_blank">📅 13:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440187">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5R7rtausbRMGR9Gis3rZr5vL9IwwVtrkMOjuB41CqiJInQ6iAJt8p2KGdW4DLPw1s2sItyj7KchpeF0imBqYsaF8_3ImGoTmeMKYyQ_fP4v8FdrF0zif0VVLdyNG3o29ezdbZBW5NHaTorfMvvd81vMiQlyLScUBbdIYUJFT3sBw8GPYRNISHH1FHdRQrrv_rce7pIAxt3Ca_1UUZ4zG8LL5Uk--OKPyuA215-YO3xXnTXSlCXX1ojp6eREPH8P-jwjSHvP-dZXF4GUGIZ5UF8JuF-nIaSsJshBvlP7AUTJsHtFDcStvvnUI41S79a4OAFXMe6Npt88SKsT8YHKzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هفتهٔ جدید بورس هم سبز آغاز شد
🔹
شاخص کل بورس در پایان معاملات امروز با رشد ۳۳ هزار واحدی به ۴ میلیون و ۳۹۲ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/440187" target="_blank">📅 12:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440186">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/802472a828.mp4?token=r3nLSrCFhrdg7tKg44fECf5H6gvn-ShGjtGy-gTA8UUN4upo3JVylxi2Y9ehbqUI7eY5jYrNRJzMVlSAZ-iSemmDyGIKDjJ5Kp5fklr_4LvCUggCwOEsrSwwyXtKVva1sUWaYGMVXIMiuNy_a-bBLOR8bF5QbF9ZZw5J8W9VHhqK1K6-b3Q6nTDUsaR_YGXkJx4hzgnkorpeD-lG5t5mKmz7m9r08OxEYzboq4u_16p87nlJMrWzflOgC_iLaFo3nQeZDfumAKm5d-dq-2B1brHN5AO7y2vpVOkA1X7alHFjegMohkmPr_1iy2GU75EM2dkdOMu4x17ESkEvn2wQGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/802472a828.mp4?token=r3nLSrCFhrdg7tKg44fECf5H6gvn-ShGjtGy-gTA8UUN4upo3JVylxi2Y9ehbqUI7eY5jYrNRJzMVlSAZ-iSemmDyGIKDjJ5Kp5fklr_4LvCUggCwOEsrSwwyXtKVva1sUWaYGMVXIMiuNy_a-bBLOR8bF5QbF9ZZw5J8W9VHhqK1K6-b3Q6nTDUsaR_YGXkJx4hzgnkorpeD-lG5t5mKmz7m9r08OxEYzboq4u_16p87nlJMrWzflOgC_iLaFo3nQeZDfumAKm5d-dq-2B1brHN5AO7y2vpVOkA1X7alHFjegMohkmPr_1iy2GU75EM2dkdOMu4x17ESkEvn2wQGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شهادت سرتیپ ارتش لبنان در حمله پهپادی اسرائیل
🔹
ارتش لبنان از شهادت یک افسر عالی‌رتبه به‌همراه چند نظامی دیگر در حملهٔ پهپادی ارتش اسرائیل در جادهٔ الخردلی به النبطیه در جنوب لبنان خبر داد.
🔹
منابع لبنانی اعلام کردند که این افسر ارشد، درجهٔ سرتیپی داشته و به‌جز او ۲ نظامی دیگر به شهادت رسیده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/440186" target="_blank">📅 12:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440185">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59639d9290.mp4?token=SafRMd0uHl4OCslvpb0072WspwyZZGagYPfXYj4Dff_2gyGiWIWVPHcc7B_vYI9LaFjBxb4hx0asGRDY3StjWBwy48zv6Av5wVk9eG76McYRVPQ_H0vH1XeSVhIMJXZkTrrxIrKJ2C9iOLY90NbtdlpnWoBpIm9Z_er4faMJihrw9Pk1ObjUKZu1zDE8K6iSOmU-mx8EWJtLijk7mT2hAZAC7HBqjya7o5rWgaxGdckkDxDAB4e9UsLZgcrypf76FY926Wl7vABC6e1UVEP3hajCdywYu0zISwlbvPvgbTvNmlRi3qeGS_3dwu3G_31Mp0YAtRpRvVaU4-CuW0ZHSYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59639d9290.mp4?token=SafRMd0uHl4OCslvpb0072WspwyZZGagYPfXYj4Dff_2gyGiWIWVPHcc7B_vYI9LaFjBxb4hx0asGRDY3StjWBwy48zv6Av5wVk9eG76McYRVPQ_H0vH1XeSVhIMJXZkTrrxIrKJ2C9iOLY90NbtdlpnWoBpIm9Z_er4faMJihrw9Pk1ObjUKZu1zDE8K6iSOmU-mx8EWJtLijk7mT2hAZAC7HBqjya7o5rWgaxGdckkDxDAB4e9UsLZgcrypf76FY926Wl7vABC6e1UVEP3hajCdywYu0zISwlbvPvgbTvNmlRi3qeGS_3dwu3G_31Mp0YAtRpRvVaU4-CuW0ZHSYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیت‌الله مصباح: ذکری از این بهتر پیدا نمی‌کنید
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/440185" target="_blank">📅 12:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440184">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ابلاغ وام مسکن ۱۴۰۵ برای خانوارهای فاقد مسکن
🔹
براساس دستورالعمل بانک‌مرکزی، تسهيلات قرض‌الحسنۀ وديعه يا خريد يا ساخت مسکن با بازپرداخت حداکثر ۱۰ ساله برای خانواده‌های فاقد مسکن، خانواده‌هایی که از سال ۱۳۹۹ به بعد صاحب ۲ فرزند يا يک فرزند می‌باشند و خانواده‌های ۲ نفر (زوج و زوجه) که تاريخ عقدشان از سال ۱۳۹۹ به بعد می‌باشد، پرداخت می‌شود.
🔹
دستورالعمل اجرایی تسهیلات به ۴ بانک عامل صادرات، تجارت، ملت و پست بانك ابلاغ شد. بانک‌ها باید فهرست شعب را در تارنمای خود برای اطلاع متقاضیان منتشر کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/440184" target="_blank">📅 11:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440183">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🎥
آغاز بازسازی پل B1 کرج
🔹
مدیرعامل شرکت ساخت و توسعه حمل‌ونقل: در مرحلۀ اول بازسازی پلB1 کرج که در حملۀ دشمن آمریکایی‌صهیونی تخریب شده بود، عملیات آواربردای شروع شده و پیش‌بینی می‌شود یک هفته زمان ببرد.
🔹
بازسازی پل B1 کمتر از یک سال زمان خواهد برد و تلاش…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/440183" target="_blank">📅 11:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440182">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">انفجارهای کنترل‌شده در جنوب اصفهان و بهارستان
🔹
سپاه اصفهان: به‌دلیل امحای مهمات عمل‌نکرده در جنوب اصفهان و بهارستان تا ساعت ۱۳ امروز، احتمال شنیدن صدای ناشی از این انفجارها وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/440182" target="_blank">📅 10:55 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440181">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e708d74fa6.mp4?token=fZ9df_yoNM25FNnJ9GcP4Q5TcE6u78eUzHl05ZVXiujXwyTsDvsxnXjPCapIGT_iWcqTw7nb-uvRpiE4qPMml4Yqw5YqI6iwjNsjTDolQ3e6zru7FtpVLu0cog7cLN1v1zCrRnfEV6Hf8k_0f0_4rZIy8DDmzQuqhg0MODmz-5UgAs4DTXYmJvJRY8Kb-hTs1Z7J0GTL6D7PkTuzl5Z-3my-TPNoam8vmjBX6A1ne1omacJUg4reu0YB-RMNLtJYTmk-jPk03Sgw5vXr1X-ptEFnk6Oy3UZTnnAPjCclMtJuKLzsDrbulfjWyT2lpxoTdkixhtTWzDO7sTbnGQuWBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e708d74fa6.mp4?token=fZ9df_yoNM25FNnJ9GcP4Q5TcE6u78eUzHl05ZVXiujXwyTsDvsxnXjPCapIGT_iWcqTw7nb-uvRpiE4qPMml4Yqw5YqI6iwjNsjTDolQ3e6zru7FtpVLu0cog7cLN1v1zCrRnfEV6Hf8k_0f0_4rZIy8DDmzQuqhg0MODmz-5UgAs4DTXYmJvJRY8Kb-hTs1Z7J0GTL6D7PkTuzl5Z-3my-TPNoam8vmjBX6A1ne1omacJUg4reu0YB-RMNLtJYTmk-jPk03Sgw5vXr1X-ptEFnk6Oy3UZTnnAPjCclMtJuKLzsDrbulfjWyT2lpxoTdkixhtTWzDO7sTbnGQuWBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سپاه پاسداران: پایگاه هوایی و تاسیسات مهم باقی‌مانده در ناوگان پنجم نیروی دریایی آمریکا هدف قرار گرفتند
🔹
ساعت ۱:۳۰ بامداد امروز چهار فروند نفتکش متخلف با تحریک و هدایت ارتش متجاوز آمریکا بدون هماهنگی و بدون‌توجه به اخطارهای مکرر نیروی دریایی سپاه، قصد…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/440181" target="_blank">📅 10:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440180">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">هلاکت ۶ تروریست در درگيری مسلحانه در هنگ مرزی
🔹
فرمانده مرزبانی: تیمی از گروهک تروریستی که قصد ورود به خاک ایران و حمله به مقرهای مرزبانی را داشت، با مرزبانان درگیر و پس از تبادل آتش سنگین و درگيری شديد با برتری قاطع آتش رزمندگان مرزبانی، مرزبانان موفق شدند خسارات سنگینی به گروهک تروریستی وارد کنند‌.
🔹
۶ نفر از اعضای مسلح گروهک تروریستی در این درگیری به هلاکت رسیدند و  مرزبانان در پاکسازی محل درگيری، ۲ قبضه کلت کمری و مقادیر زیادی مهمات مربوطه را کشف کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/440180" target="_blank">📅 10:41 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440179">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPbJS176YGsvpK6NrRJfxhcemqO_b82-VOoJKfKSunfXcl3u0Tz-cHZOnQHBdOzE64WgtbJTNsKjVKhI54kbE7pLaaMnW_e43tN6dEy_5i5z3cfiqZL1QcSlgRcfU-D5eVr3etTVE2WLY9y8syNQtJar6tTHUAtPlXQOrjWwNeUMiYUB2AxQmLcU1x0JZa4g0zAXR3LE1htS8fFc9aM6djezlk6pqxRFawAgx7vz_fl38miTyV8ZprI07KR_75R2kht4KSR6IBqQQO4cBJIGhQ-HTNQ9NxlyGVr1kkr0AnH6bryD7wRXUq0zJWftc4K3tudbStwn6Xw1uW-YFU4yfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ولایتی: صلح پایدار از درون موازنه قدرت می‌روید نه از دل سراب تعهدات بی‌پشتوانه
🔹
مشاور رهبر انقلاب در امور بین‌الملل: کابوس دیرینه و ترس تاریخی نظریه‌پردازان غربی از قدرت گرفتن ایران به واقعیت مبدل شد و هندسۀ جدید شکل گرفت.
🔹
اعتراف رسانه‌های غربی به نیاز ترامپ به توافق موقت برای بازگشایی تنگه هرمز، گویای شکست دکترین تهدید ایران و پیروزی اقتدار مقاومت است.
🔹
اما خطای استراتژیک بزرگ‌تر را آن‌هایی مرتکب می‌شوند که در منطقه، به سراب سازش دل‌خوش کرده‌اند.
🔹
معماری جدید هندسۀ قدرت برپایه تضعیف مقاومت قهرمان شکل نخواهد گرفت.
🔹
خوش‌خیالی دیپلماتیک، هزینۀ سنگینی دارد و صلح پایدار از درون موازنه قدرت می‌روید نه از دل سراب تعهدات بی‌پشتوانه.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/440179" target="_blank">📅 10:02 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440178">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‌
🔴
آمریکا هنوز به برخی از اعضای فنی و اجرایی تیم ملی ایران ویزا نداده است
🔹
ویزای برخی اعضای کادر فنی و اجرایی تیم ملی هنوز صادر نشده و سفارت آمریکا تاکنون از صدور آن خودداری کرده است. @Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/440178" target="_blank">📅 09:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440177">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQ0_PFCDbTPfYUN3f4PgxW85PcBtwu9sWiPFBWjblNArRqdBUxZIVzgiP9QhL1f6a5g1ln77oRtbUBhRF8CAmZpHWDABcagC1xdMCt7Rjv5wIx-lBm1PPJ3ZvuO3nnGLkcG5S29yVD7d0UZJFUqvz7t09t66EQbSR8N25LzRqJeeqjPks5n7KYFgepOdLf7nRVkUdhgr1UoPBC1xC3VrvPD94qlXgLHVWR-Fn4WFbu6kmBsVmmdUVewkeRe8Rz8UVyuGwFhlb9rK0mY-WvNL-obwbDd7GOswNOeRdYs28V0RB_8wxfNt_RJ2mD4b82TqL328km6hLPnHWqZeB7mXsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
صبح تعطیل ساکنان شمال فلسطین اشغالی با هشدار حملهٔ حزب‌الله آغاز شد
🔹
هشدارهای حملهٔ پهپادی در زرعیت واقع در شمال سرزمین‌های اشغالی فعال شد.
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/440177" target="_blank">📅 09:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440176">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z985qARFWFofVabClvJVqTnGMoYKOLQpglejR_Y4wz0C5bgbhHg03I5zqV9LMgEWN0qSEz4sW_1bYCn4rv20aS7RzEAoSMWGFgf-UULrIxMu-ykoyTr9Ky_OmjOKsF9q849EVrikAJNcekuPLzDfz2AWh8YxktS2ooYnoXRrsEUx0iAq9-U0eIUJwXXdYtcEVhsuPlEH3snVJylXYewknB5V0LldxevaSjQ2OjPuUw5THpboZ8CvK0AyRO6gAV8aNC9uO2e4Kt5DaUX3xqr75ebPnabeUzCX4xxC1gavGb7huJ-IX6nqMjXS5zX4rd15oiHDZjpiWtaTrtoS6GgNiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عراقچی خطاب به رئیس‌جمهور لبنان: لبنان را از دست دشمن واقعی خود نجات دهید
🔹
براساس اظهارات آقای عون، ظاهرا این ایران است که یک پنجم خاک لبنان را اشغال کرده، یک چهارم لبنانی‌ها را آواره کرده و کشور او را روزانه بمباران می‌کند.
🔹
اگر لبنان برای ایران ابزار چانه‌زنی بود، ما مدت‌ها پیش به توافق رسیده بودیم.
🔹
لبنان را از دست دشمن واقعی خود نجات دهید، آقای رئیس‌جمهور!
@Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/440176" target="_blank">📅 07:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440166">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IWhaF_DkMnH_Dz7m7tTNTxrnQbNqufSQrveFWrW8U_a5wHO4X8_VlgGCVktd0xAHD7SUnhBFJnlblRP2EyGrNjBaYznodPY05WsFnS810-Ywr7tyIaqmNm_WyplXsnQ8WpcSGlsZuTj2jK52pzKiSfYUkk_Gdd3X3GvdZb7S18G_j57rkIq7Pzfem4-oEeOMTjQ4VzzmFzJrM5hAyeVCPsyRL2WD3f86JWKG2kaUFRlszwR-nPRdwoYvCDuvTLcFFlaA69X3z30Xr8tYp029FIkGgAP_R1fxOURQfFt60M9-XhfLdwovx1_7cWw9ifOIMn2hi0UbXABjhiNkTFekYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bq_w0UHfGrk5RxUe0i-nFSvPrgpShcLO5vUomYEWt527cdfNftG71VwLTMrNaUpGUDQuCyKtDaJDrAfFGwCkkwL1Gpm4T0e8ib084OdVyKuwwuFJchWO5xaXbzvModzt1wz58hDspMToK3iY-CJvVqNb0KV0FJHX-GAOkHD4sC1eNmUQ2_uIW1SfDAQVOGXabDUI6DezyyJ2r4KJo8A4bl8pM1hxtLQe50uZ1lKHPhBcOeWbOc9qlbftAGssP5BVkCg11tdrvJQ-yW1QOQG68X5OK-phA4C3eayHpPwtxuLpyi7JfzymBMyFzoEuNDWHk4OGl2kr0l8cnqv7pNM-EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SXfnMGaDuIqN8pqZoUjTmdZ_hh4IxUHtuIC99v0niMV4q7B5wSL9vMnCsKFNeyczwAY9k4RuuNMHrplR9pRauTeZvHEmUXaAqF8UcS_dBbcNbkvTucYdMV_vwUhyiMHKyNRnVfq_ExOMuzEwlFQ_LaROyNms84GRIju4V5Ae_a4RyNGBJWHIq6Nkp8_CXnjRW1-PX-_2eXIi65l6ZtJsIJJy3Grw-Gw5F3VmFQpv82q7zxfXvi7yyKjJgc_4UasPY9O7kCkUFBg_5OqNwnhit_DWdKE9mxQT3cFplj_ar8bBfqhVhVPK2YVQwcOcsFbU9PnJruxXrfjyvO6Bg99fPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NvRgtC1WRGzlVEufw79mAlQFw-kHuxzKDUVS6Zg0wmIk2JKMZHQ4F3jSHzNYBa1szN5_jUWzRGTZTAGeL4KIqdxLV4OVtuAF9MDS18s8oyYrbpnST9l0jV3tefEWerKHa1-5yP__nbaPnstsEWYKYyYEw1e6GVGW57rklVYyK1waQX9GqqkBwAxCzQqy92qRcinrnso7HAn7brvY7iJPsH49YGOiNGm--iC_DA2fK7BnWxFn2cFk92pcOAkAup9dAWcIf2rK4t7CulzC3ZlKYF87U0jq4FgRPK9qRW3EzxSKTR8mZ5hwrLmTupnn7hwSvissrxWnQBmeeYFllrfrpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uDtjt3beIV18m4NqBknKOmYJynFscucLb9ybtzOpdLWphtut2Tcrenci9uflNwnxlvgb3V7GCJlJqBKdXAmtS8l9rh6RFbwjx1wV5urwn7eTith3q1kNTvX0pQK0CQ-GnJ8L2B4KTp5FeeUWLpe6H1pVlY2lv2TmeTdXpEcEJ-RXb20b5S3cztkuHp3lA7zvrbE4yAP--eJqJz_wJLpq7XCTIF6z1MSyjXkVipa24CNcF35jje1GrAOqmtn2DeYz94w7Qb3bMnAceRbNnP6F04I8IETUZczXI9lrq-a04NvzM3HdqKCdfLvxXkgnwxm7Ryeqb09on1SItzp0iIgyig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BiB9IQKCLvHlNs5yD8MDCRUSIb61rgtpuNfDRWMxPOfAKAJ8MnW-JPOrORN_F4Z_F1j43-9c8ifngwkDEel0IsBEBdL5Tn_xiQFUetRGcrmm8RovA5q1Iu_PjloBeocc00KdBAGWfu65tiA2Mtqh42bX5pnpNImRdUBIJcc-XtWsEbCaSO-8MqNVBaqObH-Z3XNlz93ZBjXqdeUZzGol7GL7lUgz49M9HJLkLJ7UGr_2kUDkHwOEsS5pqWMljERF3gRTd2TLkzjkL5-6qoCi6kkkM93ZHF2r57x2MbyQfEghm6a3ZPgL9k5-ukEalTrguuJ5gD8OJc8QIYGg66dXLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZM0eIhDtelpizDQhhLBKcx21Zt9P26wPc4YaU402G8k0Xx4_jiXYBxEjPDqkOM7mOIjvAhLnLXrlj0b63cfye4nCniBmb4QzgXFDq3ZQSdiFsb6_xJef5tgUrquhbrsmvcTVA8ddr_lI-9a_8lxSTbh6QiJ-z4ApzodnEJ_xhuhA-OO7_Kt4dJ0W49nyHJ7yFgoapXUQlEtjLIUSgCJB4APJxl_lHAy43YILXWew_I2YlRFZzoxQmPBiRQ_wLtKTy2P8QsMblbf9wc43WZ5cUM7owje99GZSNyfnXNQv1xI8i16X8LW91uJEWB9iTQOw3ODkfjk2XwbgZ8rU4DP7dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D7-dxNN488kJCtVvGmTGcbAFG8m1cyxoOxAsFiH9uBKxqgR_qX7tPl5XPlTLONfeDz1ggRewf-LY77JPvQ83wWecIEHehOydTK3VnkSVfV4Ns2KzSaB6s7Faot1FuSrsUE7OXynMmEVI8FLc1nPsiMfrStOWMTQIs4QQjF7TajivmXZ7AtAVx0JHePJIVSRdldKQepLlY8g7uXkMdjld9cC6wKcRicQFzKfXWKiHcI29juEsQTyXMM5H8YlHSaZ_sHy94dqKBeSESu52Wfeas0-EpeTfCcj-NeaCmz5wL0g83zMgKwyNYaBsINGapAhsiuKq7WtfLms7XlvWDdxk3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b-xziwBjcMoWKKVDZzqyNtje1YVrSmeegg4TVd-jmOpzieIDf9-ZIVj4egcIjhJcuCNUBTDE9t7DN84BJfBfB44vMThbJhcsSTxDPw2O9f_n3I9b0AtLeu8z1Cc3YPjeEgbzwkbFOAHZdFSzL0MrgqOrb9Mn57J8FnVt4Kl7Dgl1i5Yoj_GQUe03DSkdZgd6AwWZb7Ibn0ok4orH1Bgm9LXPCHWWb-gt7gIbPWTJRslB1d_xri4lXLPFzUDeQ_T762_a8t-1NRJREnDwF7SbQFVW23r9B3r8pXack55pm9MtTFgUHFRhDgTZ_AaQJ6yavgsvGoXIfruiCGfvkNRjHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FSQpwoFRjTFmeuopyQmzQ4dFksQBa1hOrbb6uB_Rwl-h9WXJ-NYcNKTwJ6WkC9CO3eXlxkvmepJMk74CvZsQEp-uSZbhVayrQdDOhP6gmo2PEPFPq-jFy1pnZRADFza2B61975Tpv3Bxsv1PCsKwrBIkoVt-j1TDRcVqmzJjS9iCcTiC-LEBvG1v0HfhR_RlBswZpzaLqHdA6tSgBJNQetkjG56-eqGMXjIGs_uuy06QHNhMBGGpNQK1vIePK32377iiAdg5z8GKrM78R8VeigMRevejTLDHvuWcB9MvwXDHWiZSBaMZixj9_PyjtSEkesk-GaArBS9GP_aPtSDF9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جشنوارۀ «آدم برفی»، در آخرین برف‌های بهاری توچال برگزار شد.
عکاس:
احمد بلباسی
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/440166" target="_blank">📅 07:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440159">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BJPruParF8xU6pFN2XuiNQqKh-0fpPj8rHzE_4OdCz0u-UY_sGlwSY3F5qXHrfhduPseimZlVo4vtVDC6XDyPu8asi5mokJZmm5k3ZuT-4zpCLtlnjDE3JhKpYBz6dMUHL8QEfvMyuO2R-sU8ndbRn9yFyC8x0gaQZltRxHaSV5NTzJoCdd0gfiyK7-XiHB1R5jfP-2v6l9JQvlMfkMIRc-RlAT0qJTIjWB18osBHINaX3y4nONCNeu1WWenJVOpHwt5K1yAzH7eBe0CQJHzHEgDdggMFIziure_XpxgzLSKS9wyI-XRFJF0bXg7M94qNjqkUoVgdFuftTIJsq_Hrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EGtBxBWkw8tVGD4AYX9BS21bYRuOyDgFRsXZ1fRVcePjE9jWJZVuYe7TmjwLczdZGnHdyGU65C-oMDnIKa5hj7NNlxyTpoHMFWIwmTy6ertKoxurUkoTCMEt7zK3G48qXYu-16hH19ZAk1t-CPI7CGtCabkAUN3mDUX5gwyOT7DgdbKkHuy-83X0S7SqAYZeV01_yUwlIGC9k0diMsYPKL5IuMUifBnnQFuWtzNES1O_TS7z0ticayqQThkaDyZY0ydh6gVwzr11w_pYaeqvyPAGfoJ-KfZeXPS7kPbpnCE0WXJAwTgmjCPfbWVLrD07c1U1LSJ2vYM_bw_jWtPAnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vbMkSXw2PrLoFbnRMF3N3lqhf_HpDL5Mhb6T7eVKQB02D7rZhGk4UAbBA_apFPE7L3Qx5cbCBQLsqLH6SE6_fgCkVopciZ5TDukq834B4xWtSD21zkglUh5i4kGuIkytVHXdNNk__Sw0t_3R9BUN1KQ0iqqSbUAmIcLJX-fyxajFr8RE02Rld_WyeEhXfECKiELcEW-rC0-8rVE4nGrNFNo2sh7oyNKJB8NqCe1pjZgkhvBDq6zBRKF7icI6OjkSddynDPl1xEv15l3bEIloJ9FdRz8f3EDDcjUfeTOW2oWVkU6XALLOmtIVmTNDjB-SaXfyhTHvjtp7w7zFi6yLHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I7eUEnU6j0M3NR_b4duulM65b79mTMipamslJuWd3tuVAq8GyWAbG0R20Fid80ntvVHQpzFfx7MK3pSnDIuXbYiOG0jbMzxmqHOssOfjcsPVS_HiUEMCzlWk4CE8xsI5t6_HjAcpU6C5NPMn3KzdvAOMCCOa4LXcWwu33okrnr0SiNhlWZi_TslD7HZELXcNbtm0NUX5LCebQefgBzHOMG7I2XDqpkxkw9sqdDUWo4wj_LubwhVCFh1-dw4d02s0EfcwjdjEKEqYe_lH40YaslFR4qAX4cYVKPGc3IPByJXnTn80kDNToVPHfy5ns3Axj7r_XI1-mqsOS1HLsDxA2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bB9wSzPqbcOJbTpqveZauGEp9HSVYDypuTsQgw0zI76pEoqcHooxQTANCWlwcqFTp-T3Xb99cPJK6JFTzdjnn0I8iMuzYg4DLdQZFAW0qXrMA2eca4MVENIayI5PyFLLmy4bRhF_l553PQ3W0zR_On93R6_UP17wlqdJniK5P35ld8Jo4HtvpYOqavnlE2HSQfaJUbFQ66CfFPDEx16HukaegTCUPWW6yoCEkI4SE3iwGUAB8a_4EfRmqVf7VydOwKTJlLphbfzOxObtAdwkTAmixdebsjfUjO4KMETahqfJMcvpyD-ZygRTIKdmtVwLD6ESDu2KNkvyN1NU3rt4dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nVd-vasemJvFoUwKjCh8P9alHkarQA7kuo6VfAlVuMI8P3nYkCFV0cFrZEOdesrT4n6FLCREDj8juJ7JR9Wy-uUMZJ4Y6Y3bVLImv3tOjRpKDNe8knsiUyd_9GDMuHLwu_Gprj5DIJ6nf6RVOP0yJjlby727d40y4LKZNwhdLttiVzKMad0oFe_QJisBAwZGU_Xs-fUbXfFhU3DInmIv5y7UrGeIZBgj4eKfkb1dNJRy6n1Qn7iqmWYX-Pa3eOYSO5ne9f3cYFA4A_L9TkmkddB6v9xgTVgJ5FYRAEXAZ_U8-0TKK96O6U49XoA86k3sX61PcSCoDzyVouLepVGLIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
نصب کتیبه‌های ولادت امام موسی‌بن‌جعفر(ع) در حرم رضوی  @Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/440159" target="_blank">📅 06:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440158">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">سپاه پاسداران: به دنبال تجاوز ارتش کودک‌کش و تروریستی آمریکا به سیریک و جزیرۀ قشم پایگاه‌های دشمن در منطقه مورد اصابت موشک‌های هوافضا قرار گرفتند.  @Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/440158" target="_blank">📅 05:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440157">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سپاه پاسداران: به دنبال تجاوز ارتش کودک‌کش و تروریستی آمریکا به سیریک و جزیرۀ قشم پایگاه‌های دشمن در منطقه مورد اصابت موشک‌های هوافضا قرار گرفتند.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/440157" target="_blank">📅 05:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440155">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b87e64f79.mp4?token=bqrfgQn7CFg1hJemrAd_XcnU7LAS6fCod1iJ4q5kXH7NtAgxyQoRgDRfwhUe77cgWHJUaEY0ygJw1Z3xxf8oxCz_wPWfUPyfh883uL4u5Sx9PSVFzmCl3czOlQO0gBAOm7AY3ctk-D5gg0Dx8V44B4-WN5ood4XB1Scu41zHjdzapD7RZqopoCID0HGRxv0IG9BZtC25QU3r0VBRJEgzmg5sPlpQMTmxRJV2YYF6nkr_SHMBL9CTKtlnITg9v1GqGPOBhdlrFwH_6tS6dYP2UiY7Sv2H4mKUGm26NBNdbmUwQNBxeGE2q_FGz_wZMwhH29BipbUJCMh5RROhYIlk8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b87e64f79.mp4?token=bqrfgQn7CFg1hJemrAd_XcnU7LAS6fCod1iJ4q5kXH7NtAgxyQoRgDRfwhUe77cgWHJUaEY0ygJw1Z3xxf8oxCz_wPWfUPyfh883uL4u5Sx9PSVFzmCl3czOlQO0gBAOm7AY3ctk-D5gg0Dx8V44B4-WN5ood4XB1Scu41zHjdzapD7RZqopoCID0HGRxv0IG9BZtC25QU3r0VBRJEgzmg5sPlpQMTmxRJV2YYF6nkr_SHMBL9CTKtlnITg9v1GqGPOBhdlrFwH_6tS6dYP2UiY7Sv2H4mKUGm26NBNdbmUwQNBxeGE2q_FGz_wZMwhH29BipbUJCMh5RROhYIlk8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ویدئوهای منتشر شده از فعالیت سامانه‌های دفاع هوایی بحرین و کویت
@FarsNewsInt</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/440155" target="_blank">📅 05:02 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440154">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
آژیر خطر در کویت به‌صدا درآمد
🔹
رسانه‌های عربی از فعال‌شدن آژیرهای هشدار ‌و پدافند کویت برای مقابله با حملات موشکی و پهپادی خبر دادند.  @Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/440154" target="_blank">📅 04:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440153">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
آژیر خطر در کویت به‌صدا درآمد
🔹
رسانه‌های عربی از فعال‌شدن آژیرهای هشدار ‌و پدافند کویت برای مقابله با حملات موشکی و پهپادی خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/440153" target="_blank">📅 04:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440152">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rsxRhPVDYcGLtVu9tB0re1w9szcG033fustVrh96qghIZO01LnnYAgyNvzm6wlu-unbhv_RDtfA0K_tqkvlfRUnipQbsZ3KOJeqfCiak0RL2cx09S4CVT7xiIEQ1zpFFCUGESPi5Rc2HOsU7tblh5l7hilTH6QNAzjlparSnB7qEX6Zj-qoP0b375GYiGcEawL_ILHrF8eL48aDYPBJ8IYa0vcs0JucjIG-JVu8ZHs0mN9TSMYA3NXei_IjximVLo3B_ooQ28bJ6Y-ufaOO4mSIEacTOIHsK5ILNbh3VJrCCSDOAkR1NHpw7eyF8Kd-nGVIHkHl5byINFGYXz9srDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پهپادهای حزب‌الله بلای‌جان نظامیان صهیونیست شد
🔹
رسانه‌های صهیونیستی اذعان کردند ۶۸ درصد از نظامیان اسرائیل که در جنوب لبنان به هلاکت رسیده‌اند، ناشی از حملات پهپادی حزب‌الله بوده است.
@Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/440152" target="_blank">📅 04:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440151">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e51a15280.mp4?token=HGCKBGGwTBYS4wGOFg_nJN3hrzB9Rs5gwMpKLHLOEjgwlX_FjQBi3F49-l5_FqKRSmEWbWSrTWVgYmDoe22FDm7AMMgUvNEvXrYDl6s66Alfq3VWbs9RmLrRYi_d5Y1MxRzilAqQ6MIU0kkjxfVDnhF_z9HjroLE8734FBflhdW8goO6HiRL5uE86b2LPAXDQTjHi72_VPC46AhxuStxh6AXrM1VXEhI-S0RSh1T45szQLn2kuLX24hRurO_VFSPaJEmBCMf4IpaSn1fy6fQLk3fXWPgKSneuTMUL74P2C_zX0U5dc7PerAhUz_nvqpdfa-S_iJfY10Yl3CKmdy22b6dsGKygmwHPn-KDPN-GZtPVtd9M4Cq36St8SO_bhWtZ7tlTl9y4DF_QnwRbz2PxE0gWKzQojJUJeCX1hLTt3nwFuucfR_2iKExJr5XyBUOEcuSSDME-kb2E9nMHRNsfXqdzXSKNHwjA-_VMqT2cDcWltwLy2Et9tOzWe9ZO57jvUl4oMLeMTA486uJYtsF-C9wcbkPw9bRXZMP3FqWr6JLiZYOwoIHIG_D6NQ0mdjexjihzSHtT9MX5x8fKPyZUqSZ84MNahCaLEYBtylHLNJeDCEqfz_3S2pA2H1qWaVXow_VlfhHlneFAKbDoFS_9fpdkMnqurKl13DTo9GBIwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e51a15280.mp4?token=HGCKBGGwTBYS4wGOFg_nJN3hrzB9Rs5gwMpKLHLOEjgwlX_FjQBi3F49-l5_FqKRSmEWbWSrTWVgYmDoe22FDm7AMMgUvNEvXrYDl6s66Alfq3VWbs9RmLrRYi_d5Y1MxRzilAqQ6MIU0kkjxfVDnhF_z9HjroLE8734FBflhdW8goO6HiRL5uE86b2LPAXDQTjHi72_VPC46AhxuStxh6AXrM1VXEhI-S0RSh1T45szQLn2kuLX24hRurO_VFSPaJEmBCMf4IpaSn1fy6fQLk3fXWPgKSneuTMUL74P2C_zX0U5dc7PerAhUz_nvqpdfa-S_iJfY10Yl3CKmdy22b6dsGKygmwHPn-KDPN-GZtPVtd9M4Cq36St8SO_bhWtZ7tlTl9y4DF_QnwRbz2PxE0gWKzQojJUJeCX1hLTt3nwFuucfR_2iKExJr5XyBUOEcuSSDME-kb2E9nMHRNsfXqdzXSKNHwjA-_VMqT2cDcWltwLy2Et9tOzWe9ZO57jvUl4oMLeMTA486uJYtsF-C9wcbkPw9bRXZMP3FqWr6JLiZYOwoIHIG_D6NQ0mdjexjihzSHtT9MX5x8fKPyZUqSZ84MNahCaLEYBtylHLNJeDCEqfz_3S2pA2H1qWaVXow_VlfhHlneFAKbDoFS_9fpdkMnqurKl13DTo9GBIwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هیچکس غیر خدا زور ندارد؛ خیالت راحت
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/440151" target="_blank">📅 03:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440150">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sq090s26rF2hh4JgLivr055TqIDxVKbCe2nTieDzL-on-Mofu7LSWrK9lyfLyoWXb-VIWG0X8zrECuM7n_Sk3Id1zJLTxITj8z63SDj-iL-IOlb4tIq1T_zvner4J6r8lwexjYkFb8Z2OneTTvzf5kFE_qKixAvHGmoB65i2mE6Yberz8IAH-4cQ9NZ9dfthp4yPEcmvw5KWdevk15sn2UOqVwTXQzverTNeZdTCyGmX4sJ-GGRC79LqjJO2aSGtPGSbA5ZMUEDMUT00vdQV3URj8gsyLBaHxudPb98JNx-8X4FbrKmLIC_R2RpMTiR9L3lVPdwGUgw3xGapw0oQpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویژگی‌‌های محبوب اینستاگرام رسماً پولی شد
🔹
شرکت متا به‌طور رسمی اشتراک پولی «اینستاگرام پلاس» را در سطح جهانی عرضه کرده است. یکی از مهم‌ترین قابلیت‌های این اشتراک، ویژگی «استوری اسپات‌لایت» است که پروفایل کاربر را در استوری‌ها برای دوستانش در اولویت نمایش قرار می‌دهد.
🔹
قابلیت «استوری اکستند» نیز مدت نمایش استوری‌ها را از ۲۴ ساعت به ۴۸ ساعت افزایش می‌دهد. کاربران اشتراکی همچنین می‌توانند چند فهرست مخاطب مختلف ایجاد کنند و برای هر استوری مشخص کنند کدام گروه آن را مشاهده کند.
🔹
کاربران می‌توانند پیش از انتشار، استوری خود را پیش‌نمایش کنند، آمار دفعات بازدید مجدد استوری‌ها را ببینند و حتی در میان افرادی که استوری را مشاهده کرده‌اند جست‌وجو کنند. همچنین اگر کاربری نخواهد یک پست در فید اصلی نمایش داده شود، می‌تواند آن را فقط در پروفایل یا بخش هایلایت‌ها منتشر کند. در بخش شخصی‌سازی نیز امکانات تازه‌ای اضافه شده است.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/440150" target="_blank">📅 02:58 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440149">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ادعای سنتکام: اهدافی را در جزایر گروگ و قشم بمباران کردیم
🔹
ارتش آمریکا ادعا کرد: لحظاتی پیش، چهار پهپاد تهاجمی یک‌طرفۀ ایرانی را که به‌سمت تنگۀ هرمز پرتاب شده بودند، سرنگون کرده است. این پهپادهای تهاجمی تهدیدی فوری برای ترافیک دریایی منطقه ایجاد می‌کردند.
🔹
متعاقباً، نیروهای آمریکایی برای دفاع در برابر حملات بیشتر، به سایت‌های رادار نظارت ساحلی ایران در گروگ و جزیره قشم حمله کرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/440149" target="_blank">📅 02:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440148">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8f6a2ce16.mp4?token=T2lOMmdn6GnGc_0Nx1DbQ_UGQI3Fpp3TBiChA4CIteOlbp5XGH2eAC0JmSSfJNK8Ri8L109Gth60xIu4pl-T6y4o9TvvJrqThwEu9CpSmyrgZu5qY9DmZT8thenAlMsdg-hkxrC5e19Fc2Z6Or4vlAO_yR9B6RD9ZoK1NcR7QyNFJLcb-fBuzHFT-hh1tvJcJhr74xa9TNJQ5WOKeJ1BYP_VpYntFxhgPvBVJOfdgU8reZB3FJN_15XDrNasm9dgs-ccfOXpQ1cqOC67eY_Z-fhuD9JWl7j2oZWnCw_CpRyvsv423HnAld6WIfAcjswxx6MbcNS54yCcjrfp54-vSabxUIfe40jYNVp6fkiukQYFGWyr7ZNSLSyusDsP54lW4A_LMWFiOwsK6dX9U4LvrZ6ZjXCgOjugq18Z_f0cVd-FwlXRJVkGNtb1LhASLz3v0nGXknxMnY3rwcfXSs9cidk6DvW1NAbo5Lyqu5qVOFTh85ZtcxCj3KOeTE5BmYKlBn7ESVI0giwlJNWU3LjAEJndI_9V9M8JTEbzcorrfTIObngdlilLhYzzLVlymbGatT_5eMFj5uWUiXef_VBfYmeXAmJBb0P5GEaeTMxP5ZYHrLLL4eQdpae_x1VQKfJRrOV5W9cwWV6Fapaq99ND73i1HR6qXylqd9nngsoFXX4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8f6a2ce16.mp4?token=T2lOMmdn6GnGc_0Nx1DbQ_UGQI3Fpp3TBiChA4CIteOlbp5XGH2eAC0JmSSfJNK8Ri8L109Gth60xIu4pl-T6y4o9TvvJrqThwEu9CpSmyrgZu5qY9DmZT8thenAlMsdg-hkxrC5e19Fc2Z6Or4vlAO_yR9B6RD9ZoK1NcR7QyNFJLcb-fBuzHFT-hh1tvJcJhr74xa9TNJQ5WOKeJ1BYP_VpYntFxhgPvBVJOfdgU8reZB3FJN_15XDrNasm9dgs-ccfOXpQ1cqOC67eY_Z-fhuD9JWl7j2oZWnCw_CpRyvsv423HnAld6WIfAcjswxx6MbcNS54yCcjrfp54-vSabxUIfe40jYNVp6fkiukQYFGWyr7ZNSLSyusDsP54lW4A_LMWFiOwsK6dX9U4LvrZ6ZjXCgOjugq18Z_f0cVd-FwlXRJVkGNtb1LhASLz3v0nGXknxMnY3rwcfXSs9cidk6DvW1NAbo5Lyqu5qVOFTh85ZtcxCj3KOeTE5BmYKlBn7ESVI0giwlJNWU3LjAEJndI_9V9M8JTEbzcorrfTIObngdlilLhYzzLVlymbGatT_5eMFj5uWUiXef_VBfYmeXAmJBb0P5GEaeTMxP5ZYHrLLL4eQdpae_x1VQKfJRrOV5W9cwWV6Fapaq99ND73i1HR6qXylqd9nngsoFXX4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرگرمی جدید لبنانی‌ها
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/440148" target="_blank">📅 02:19 · 16 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
