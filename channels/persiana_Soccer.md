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
<img src="https://cdn4.telesco.pe/file/fKMnCr9Q6qCGF6vrgSyQ65ICG454TEJGbfmQT9z9-LFkyDsyxQ3YoHiaEUomy1vOduTewkxiR3eoPwgUv6JuWffdDRPw5BjoyOY1zk76UN9wAHHxkQo4O8p9iAKINl9tnAKMWCT4rZcJxInxY2f-t1epCRYtvk5rZo_LiXeNXkEQRQKIEG2oMWBVEORrh8ORYywZeiah5BcZ9Asu7ORfoyhHzJ2ZQ9ATTZk_A7s_cZzUEbyCzpDbymzAqgYLngMSoLuwApwzFfFkRgYejeeypBGRywRIdeF-SU-l2FU32N9BQuAhyZ7tRmhZ3nUgRyPWPjCl-ZfEIBCdcBbziccfsg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 423K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 08:59:38</div>
<hr>

<div class="tg-post" id="msg-25255">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8869652ba6.mp4?token=sKaXffP6uUWfeo909RQdNy1H2QMxnXPuH61xDbQSiZ3f3TGHFNZNktaFtpM7MWfc4JsM0IP8Ps2cpe48QoIIc_QefTJbXDYJx5g4TFqwwZZKGAjWnDloQ4xSAPJK5yT-B8IU2acTZJPX68V-nBEsme573FyzDl0BcNiOklDQBxNyMZ0dj26GyXyrA3nxZl3F84Pp8FsoinzJNgbZMYg_MtSombVEHgOtqYBVfPC6QYbbI8m_3KV62rc2gfDLdjt5HKl-AvIMiEqMfP903h09pgCfeTyBma14ZE_3jzSzbgZ8UGpW81IOYZQmPNx2ln7OysETvGrg3Z7oHxgdTY44A5FO10GOZ6C6xyChNtRJKxv2si5ypG8d46WiVqRTbNNOcjRsCt0E0gl0UfhtcOrhSkg4U-oOtSYrYDnEyxew4or6eC8qtYLMURYzsWCLV5kGpd08X0QzvL2NJfXkcvGdHSjZdbZsdTL354Anqz0S2-lQkvOlamD53DmKLu5bWZIPJowRV85Te3GeZEtDYQnU7trJcKuzQup0eLYL-D02yTNkdSR3Px7lWKjMpMjMO9j67RxhcwMmlRDneMB2CUUeF_MQMrGB0_wnLD-Bc98y0spQ0FaISZLAEUn_NmDRVXdqDD74-lKVn-FOVqKrq2VX02SHu33bd6-KDk8maIt9Zu4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8869652ba6.mp4?token=sKaXffP6uUWfeo909RQdNy1H2QMxnXPuH61xDbQSiZ3f3TGHFNZNktaFtpM7MWfc4JsM0IP8Ps2cpe48QoIIc_QefTJbXDYJx5g4TFqwwZZKGAjWnDloQ4xSAPJK5yT-B8IU2acTZJPX68V-nBEsme573FyzDl0BcNiOklDQBxNyMZ0dj26GyXyrA3nxZl3F84Pp8FsoinzJNgbZMYg_MtSombVEHgOtqYBVfPC6QYbbI8m_3KV62rc2gfDLdjt5HKl-AvIMiEqMfP903h09pgCfeTyBma14ZE_3jzSzbgZ8UGpW81IOYZQmPNx2ln7OysETvGrg3Z7oHxgdTY44A5FO10GOZ6C6xyChNtRJKxv2si5ypG8d46WiVqRTbNNOcjRsCt0E0gl0UfhtcOrhSkg4U-oOtSYrYDnEyxew4or6eC8qtYLMURYzsWCLV5kGpd08X0QzvL2NJfXkcvGdHSjZdbZsdTL354Anqz0S2-lQkvOlamD53DmKLu5bWZIPJowRV85Te3GeZEtDYQnU7trJcKuzQup0eLYL-D02yTNkdSR3Px7lWKjMpMjMO9j67RxhcwMmlRDneMB2CUUeF_MQMrGB0_wnLD-Bc98y0spQ0FaISZLAEUn_NmDRVXdqDD74-lKVn-FOVqKrq2VX02SHu33bd6-KDk8maIt9Zu4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
علی رضا فغانی:
دوست داشتم هرجا داری کنم نماینده ایران باشم اماخودشون‌گفتن ما نمیخوایمت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/persiana_Soccer/25255" target="_blank">📅 08:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25253">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeC19FpaPaFa9N8mvwKIt7G2Ud5hZ0vZftlamnMYRpAjlq8s-apwBJkEJA1ygLqx5yG-906baqBXex6xGapY4q7opEBQlcAsbrbohq4DSOfE1OMrSXnixSyBsgF2lPu89gWZOVwRWlQfX9_AWn06_UNmkNysIzYuQU_KmwtXJkXfc6u2LK_uGkdZihvBHuf6JtCBJs188kG8W9DXKylIqtgV1EXpEYlWNpz8qN4vJtizlVlYZnPGOY7XjaCigl9zWgJM7Diza29fY3rjEtvw_5VEYwvsZOAvIQSswXhwrjgmmrWBricKYmmnda0OPf1hvvFT08jENKMgekeBDpQYog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امشب؛ آغاز مرحله حساس یک‌ چهارم نهایی بارویارویی‌مجدد فرانسه و مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/persiana_Soccer/25253" target="_blank">📅 08:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25252">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snXLpUzWD8DDfeR6RYyTq107KVsBGkxQpDqvcfgD9WlzGvCc0zoPy1UjnSjSOiXARjf8WZMO9yyuO22NEciepHu2beIUp7GV1tCP52X61fWon_W68-WKjjg0kK8Y_kREwQku8N4kleeS7ZXXVBuoIPLILiO5y-aamUiDFcRKDbqRh-bv3DmbH3Am4B0byd2K33yWZBxSzOtjDAMTEB-eK5Jykst_qEAMJrXXDBkBmRdCr65J13lVKIw6QKPU3q3-JOdO57HqkfHrsBJzskXLRBxUNCXLdh8oWQMeaQZ78yWF3hV5ygvSYtb3O4170ZhzhmCKciHX0OW-vKDTdJlpEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
جرارد رومرو: ممکنه‌ طی‌ روزهای آینده کریم آدیمی ستاره جوان دورتموند با عقد قراردادی 5 ساله به بارسلونا بپیوندد. مذاکرات مثبتی صورت کرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/25252" target="_blank">📅 01:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25251">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVHSLdEEVmLOqwq7pOiBqT4Ot4wRUOhaU1DdcsIDneA9GYS5vRfpHyfM6BthddeE2aNtCk2DyP_DRHNuu9-pN0fNZQg83f1Z_5cnnzXcB2aQPcpDIJJwo0H59foMhhKZDfxYWnxS2tYe5uO1EWGYq8GerW_DOZaK8ZD6gmhs_YVRFYH7cfiZlvwUpZ-LQl4mPkG12sE6JCdjT0GR_Lm1p50mfFvnMo2KJ_UhFEhhV8CKUz2jagVZ55_HJ0tSRpiglEO6jED1DNyqvc0DwfivDHChOpCdUlFQLBA-Y9oCdQzh_tuT3oi_GopXzmCSEix_hPiwV1hmzopLgzgp3OwlRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
نشریه‌بیلد: کریم آدیمی ستاره 23 ساله تیم دورتموند به مدیران این باشگاه اعلام کرده که قصد داره از این تیم جدا بشه. منچستریونایتد و بارسلونا به شدت دنبال این ستاره آلمانی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/25251" target="_blank">📅 01:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25250">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6798637471.mp4?token=qDKfkkrSP5ZadoGiDoYYXWndhq8p-rrBO9n789plne07FGtrWcr44ywEdTEXo73E9Wb8s5IMG8d-24_SXs70ZoKtE5Yfhi9l9hhh0KoWOh41y0yU79dffPinplJqqXp0aAwY6gUlMfHKfi1Qa80SFs5Z_f1jdOmJ2pX9-NZ3Q65p0D1Wk-KrdaWLut_TCLQiQWF4FCqcxFMHoZs3y-v1NJ7QEA2S1RWwX9fUKSAEnQCMvyEcXhDHXJcE7f8NxxsOthX44SfqJq3c1H7acB2zOy9LDAiGI8V6zN_Yb9OcuuCSeLwgVBDPwxCX5PFSTQnWqZMobO6YfcaYDwPlM0T_Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6798637471.mp4?token=qDKfkkrSP5ZadoGiDoYYXWndhq8p-rrBO9n789plne07FGtrWcr44ywEdTEXo73E9Wb8s5IMG8d-24_SXs70ZoKtE5Yfhi9l9hhh0KoWOh41y0yU79dffPinplJqqXp0aAwY6gUlMfHKfi1Qa80SFs5Z_f1jdOmJ2pX9-NZ3Q65p0D1Wk-KrdaWLut_TCLQiQWF4FCqcxFMHoZs3y-v1NJ7QEA2S1RWwX9fUKSAEnQCMvyEcXhDHXJcE7f8NxxsOthX44SfqJq3c1H7acB2zOy9LDAiGI8V6zN_Yb9OcuuCSeLwgVBDPwxCX5PFSTQnWqZMobO6YfcaYDwPlM0T_Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جوادخیابانی‌ تو ویژه‌ برنامه‌امشب جمله معروف
"گشتم نبود نگرد نیست رو گفت" خداداد هنگ کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/25250" target="_blank">📅 01:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25249">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FfyBiF7nLozHl_TTRk_JLYyRs8-jx491wFImXUyoj28SUdwHgwhvQRs71GlAMXoPGE7W6jiPf_ytSE4WRC4tgLbbo-E4iO6RRMA3KHBgeuCBND7_fbjkYt4EVxZb-WmKjSWas8egFU8hjwEMt1HGA-01VQzA4vsGlW0IFrAM75VVJRJVCXtcF2I-DJGz89GTVMArZHs5KshLz3lHe-0wJGXum9atP9TOs3_ZMPo1YpqNdNvl5uQfh-6UWosz7OpNmQQGGlGX1t8RnLIYlTpEY-cGq-_62Qm-kO9UdRfd3_eRhPJddW1BxiwMuMjUY4ESBWKPWDXpCn-q5NkEW7fHzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
خوزه‌فلیکس‌دیاز:باشگاه‌منچستریونایتد برای‌ جذب‌اورلین شوامنی هافبک26 ساله تیم ملی فرانسه به باشگاه‌رئال‌مادرید نامه زد. کهکشانی‌ها برای فروش شوامنی ملی پوش 100 میلیون یورو میخواهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/25249" target="_blank">📅 01:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25248">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aryq-eFvYca65T336GEj8A7sh5trzJVr3NxB7PLdGG94nn8BrF6K06xQ5fjTglVcRz6c1aYK0NdjBqBM9nMiYZmB_rKtl_bX7hwNmBFOrZ5jh0vrfaVPITtzRBzLi74Xj7UJ2gP85gRt7BpBxDGQ6ON1PB6cTzKjWUzmjEpo8_4sSmeOBSBOr9S2tFnhsobpRSXgTZEPgoXYw7Ol_fa7wKrLER1RfQmcH2Af6lp5xzUA7hOmXeNQYWxM_FmJr-9I1vuyoGf_xyDle1SmbnaH-M8a3TdycuEWRyCYtLV3G_Ou7oKDlOOe2hMR1bTFwgxECqk9v018oPI9EnogJ2bprA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امشب؛
آغاز مرحله حساس یک‌ چهارم نهایی بارویارویی‌مجدد فرانسه و مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/25248" target="_blank">📅 00:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25247">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I0fBOOSEWciKGmcB_typ-OUdbTfvKiYrWXBZKPCXtN0qqpkq3T8d_dv7I0qy6zH1gCF_tho---nuef5wfnpJN26St8k9ofvrBYYYY2XcqEOBLZvqfedmSgCCvBbjaCOf6C2HuQm4NAOb6y6oZnDm9lkVmsj-UMsauSbk0y54S9N-Rr1DHLRdR0hjWi76H2Q_hOdakOudG-LWSty1r_Sj663ubQxxOYp9HPkF5Vtr6coU7NVOdeZ0Gj1eLGnWKxiwleeuebAPN2D6gRiUyPkmCYimyXOHuaFHc8RY7GrrFZDMghYVzAIdD_9cgo_t_9dzvEB4Hk_2rrOVOMkaXHJJCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عکس‌هایی‌که از وضعيت امشب بوشهر داره دست به دست میشه: یکی به این ترامپ احمق بگه هنوزجام‌جهانی‌تموم‌نشده دهنت سرویس.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/25247" target="_blank">📅 00:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25246">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltTdaxveywEqDYQ9FoSJosNlgL1Rov0ecmzpwQ5zxXSnZunPgVuyXPmL36YJXWroaUvdsnEEkJUTYk5Ylt539jnBaxYYx_hbURborWR-jc0yhcM4FfnH8Q1Gs13dyQ_4ptdPDhjVtbhI8OXYVww44PT639IEcL4YY0zF2iVnFsWJswEoYPr-nvW9fsnYrtsrR9VMpYIASnuTjM5K0KFhfIkgrZmn_8xSF1Fm8FaS35aqL2C6mK-bjKOkxXD4Myzueu7xX2L1ZDMqZOCOoz4oej7pmvsXsYkQPum5ZH-YuqkHEkqALUkKqYf5hTpOt8h5ak-2OkGLMMM_r09T4g0Dvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه دهوک عراق بعداز جذب سینا اسدبیگی؛ حالا محمدرضا سلیمانی مهاجم فصل گذشته فولاد خوزستان هم با قراردادی دو ساله جذب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/25246" target="_blank">📅 00:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25245">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/giTsCMWGMFEyDbLpDSEgqWcizz7z8pGhsJExIiBkhn68yh-fLPrjDUC50PmOtnS9jawHOsK0ap9wQVFUiI6K-r9NKYuujqUKmOymfmPWi98sJF8EjDlyGjL5Oiq0h_5nuwbCz8nSxiVJZWcYl9Uw6kPnalXyIgLU9MxgxfHcr5l0Kq-J9AKzaES3vZ0Z2TDWjqCA01W5CzYglJcehEBSzHRe1jxDrFpajL8IJdBIPQ1f4D84ir9W2M0rgMOxlSfehb-YogOgrmTCAZ_1KhRloXvktyOQqewdfjv4ShxxGW5hlxml8vATJ2uPy_8QRrsR-IqL6x4cJaRTcIUm_V5Q1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اگه نیمار جونیور روهم به عکس اضافه کنیم؛ چهار نفرازکسایی‌که فوتبال روبشدت برامون قشنگ تر کردن. کسایی که روزای قشنگی واسمون ساختن. کسایی‌که اسطورمون‌بودن رفتند، اونم برای همیشه؛ آقای‌مسی لطفاشما تا ته این مسیرو برو. بارها گفتیم که‌هم‌مسی‌هم رونالدو بشدت برامون…</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/25245" target="_blank">📅 23:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25244">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7YZaaVZeXVkVje5Fhu2eeZpKVy6hGrG_EpdS_aBHunvpp_5uKDOoloi0dB9eWwhwAPwKgqXgQylRnN24nuf-CdcBbeViRUcNpo-iZNm-X52gNYfpxXQbwEw7wBLPbP9nHOr4Xk44Pg_OGeNilMRzsZzde_CUJIhDO4VpZRngHgEYlVA3eb-CJYjJyOqOVBx1joXOLLWqkx0lXwOyCVdqVFgJlPyPczmd-CZhsIT8-z5zw2spwju13KydZkvYb0yapT1rXe4e9SsPUftkowDrWdePUNs-B6xe9kJRb3YUHss5VKBvjCq4n27zs3O2Y7ikfdohYZ6J1KgQ5zBQ_zzQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
#اختصاصی_پرشیانا #فوری؛ مدیریت باشگاه‌سپاهان‌برای‌جذب‌قطعی‌سامان تورانیان مدافع راست آبی‌ها به باشگاه استقلال نامه زده. با توجه به اینکه‌باشگاه‌استقلال‌تمایل به‌جذب امید نورافکن داره و مذاکرات‌مثبتی با او نیزصورت‌گرفته درصورت باز شدن‌پنجره آبی ها این معاوضه…</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/25244" target="_blank">📅 23:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25243">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6DTFwFxhPVKJcBUAwxMA4AGbeBKlAidEVL8oe9O4GuS_jvd8wdwPOawdaDuNzN8yUOtPWq-GSPwMfJUiq--VMc19-puYC2zUEvW3wYCQeDMKIL0cwOEufnGuD46Y03cmkDW23xc7oTWdQeUw6mI7hLJ3Ols1ItFsWBw86yBsAqmi8m-MaDm4-vXP4D2JeydwkaVteteyR-2RoDktiuW0sCPjUOOaW1YxAPSS6Hes2VnAiqB3Uw1KZDMAf2z994FgP4YeL_bJEtby5RJzh_cUx4n_SxrkUZicqnxOeH4zm6N9rxn3IlRExt3HzlKZlwtrucGbXBi1Sif04ECDkobWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
تصویری دیدنی از لئو مسی هنگام زدن کرنر دربازی شب‌گذشته آرژانتین مقابل مصر؛ آلبی سلسته شب گذشته با جادوی اعجوبه آرژانتینی خود سه بر دو از سد یاران محمد صلاح در مصر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/25243" target="_blank">📅 22:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25241">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BJnJDdJilWJwlkMVptV-D7qlSn_MKvHahZq7gB-LrM39rp2Aij_KuiidcznC3CwfzgdaaYXWjNuQL-rUDo7jC4Zli8Z_Logvk5d0PMq7Ou4TKVksJd9A-IrKNhk5yA5ySHw-gOzWPxV7dcQZnfsp2JjhzELql5xccCQ07V1rB1ZhfwDqe3Ouqmy-xTZtrfrr-0Ss-3t6BihQXCZX1rdd60mf-sCzSEpQmfAYC23wjV8kj1-2EJZaYvv-2GKqHyxzbZOPWmkIGe0tnapuU8045lj-6pMhBWTvlHlBf9MsVkmYZKlPY3k5496tQ4BHEYQd07nzWjN-RAy8J0mKacOQew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iLGhTnG8L6nsMjydodK3gbmeuJePR-EgAifHmMnhOzze0hdf4VuIUMYcjCige5aWh66PaZG0J-rjAHQZ_3GAz8OPtGlnplBRV3Gsv1Trcmet9efyjK12dPF211DJFuoS9KBUiU0xLE0Qt8v3r4e5EVkdAVkFBJ0dBbJahUwUIV2XBnlN_2O6_QnMF3MEp1G4pV8WlqAdBhToTow8jXfoSfNxXNLKkRIU-SS-K9Bb5juA6xxciH3tWREFXiLvL8ozK4wYPDJd0GqEgM26dsnr1ySvxBsg_cdQMxqv0HIl-bRCI3z5GazgYjmFvjGqQp2nSoBliTYpAOSi8JYUO7J9xA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🤩
مجری شبکه رسمی باشگاه رئال مادرید که مدعیه‌کار انتقال انزو فرناندز به این‌تیم تموم شده و بلافاصله بعدازاتمام‌جام‌جهانی2026 انزو کهکشانی میشود. گفته با انزو در ارتباطه و انزو گفته به زودی به رئال مادرید خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/25241" target="_blank">📅 22:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25240">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d23ff97317.mp4?token=nVasLUnDnQA_BLFq0hcsG0uHnk70Y1KPsBPrIVwn_Wudpl01R3dSmOyC6JJp1GnMnA9xeRCVLU3zBuFJ2GZUcMmuWrnnmPKjfVatdv39bApIZ3ECYmD1fFA2VzrR8UoavSu6yZs5aFbq2q83dWUoKSiaDk4phJ2-mckPjI95Lq6ta73z0ESnAdziH4s6IpeLeCir3_W-I6i1qLuBcmD2N7b3SwZR_xbEe7-VUqirizbohiUNMAsKiVPbuMsl9CNLbh_tdTe0_GekC8Zt7ZPJttsYRWyqFZa8ttMdE8hLaZ2Dm-fv_FfGo2dD29JxGCDW5CH-zVFW2dU1IGI3BzP8Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d23ff97317.mp4?token=nVasLUnDnQA_BLFq0hcsG0uHnk70Y1KPsBPrIVwn_Wudpl01R3dSmOyC6JJp1GnMnA9xeRCVLU3zBuFJ2GZUcMmuWrnnmPKjfVatdv39bApIZ3ECYmD1fFA2VzrR8UoavSu6yZs5aFbq2q83dWUoKSiaDk4phJ2-mckPjI95Lq6ta73z0ESnAdziH4s6IpeLeCir3_W-I6i1qLuBcmD2N7b3SwZR_xbEe7-VUqirizbohiUNMAsKiVPbuMsl9CNLbh_tdTe0_GekC8Zt7ZPJttsYRWyqFZa8ttMdE8hLaZ2Dm-fv_FfGo2dD29JxGCDW5CH-zVFW2dU1IGI3BzP8Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
امیر قلعه نویی سرمربی تیم ایران: کاش قدرتی داشتم که بعداز گل شجاع زمان رو متوقف میکردم تا شادی واسه همیشه رو صورت مردم ایران بمونه. باور کنید این تیم شایسته به مرحله حذفی صعود بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/25240" target="_blank">📅 22:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25239">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fRwe0_0WHGgZ_9VFWSd6lXfvUcd1832r9XrARtKonx22h7NfMX_8bjLUF8Qj8Q1lASNu_4SJlFx-4Ql48khCBO0Gglbpg4YfeqYOeaQin5TD-wm2bhJDzVS_oOW11roOUEmRTGtr6M4fj-7zBJHGM3xE7Zs6CtovTHPIsSStjVjDcwNajNMPw6a4SUMxlUXpRJEzPxpu4pkrkCBU7d06iIQxA3SBa4Q5gV8Z13hl-3be8dXhwucz2u4g5jaTcqNXIoBrwKmsWn0vpK9oeYTJpUnHmL2gSi08P0Y4qZYlj2RrNNb50M1zjv-oRsmBAM_qkiD9po9mvFgGcfY_sRjLkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/25239" target="_blank">📅 22:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25238">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fb7b4dbfc.mp4?token=Od3OLf0ZTl9ivqinJbXOQfUnc-CpCtBAr1lCXmSYytETjVDb9lyv_dK8Qj6Gl8oW4wzAw5VGJ6ADKq4KsIN_wpgFZJiA2ZBw7zyJjpTjcQBGqbMbguX65CZdKM5a9aHa55DfVIku7Ixx7Zcjd-S6d6Grc1wBcW7ycOi76Mrl6pgD5syrrYeeoNdR-EiM5KfgciVPg6osRcmqJ9Km1pz_pWQfuIDy94-Pb_dMyPyq0cq4yPHL8E9kTsoXx6ycPX1U8_1rDlXpxInH5CiLudRf6mr6oM5nlb5fnmU2AeuDsnycv6ICGuyqJIqXuxMR44USI6cx4koaEePXKuWuL6djMgqwhkrq7UxScuAZrvA98ACPGLOdh-cuqa5Rpad_gA76xNNLZuPKzwhJsDlv1F8TC0VpjcvaCI9FMeu608XZy8U1gPBi7m-3uebgW7a-kfVc3_7-D8zVIVCqF-2nw615mn_c1W8Ovsalgo4ocBMY7AIuSl6uDoHedSoByiCNolAiQJu-cnZRtJ_S-oINj_-sUZQ_vQnH9unlTRXxTu75e4EOq63d1yj3Itrb-bvA6x80sJOjcZ1KIWCUQSSjOTJuLpAuKbDzSUT0WsHRVmrWKqjBYkrEXB5_LRrwzVoLab4L5CyyoVRVmlpWngpQ139acqL7uJMwuZw3XM0kzPcwcAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fb7b4dbfc.mp4?token=Od3OLf0ZTl9ivqinJbXOQfUnc-CpCtBAr1lCXmSYytETjVDb9lyv_dK8Qj6Gl8oW4wzAw5VGJ6ADKq4KsIN_wpgFZJiA2ZBw7zyJjpTjcQBGqbMbguX65CZdKM5a9aHa55DfVIku7Ixx7Zcjd-S6d6Grc1wBcW7ycOi76Mrl6pgD5syrrYeeoNdR-EiM5KfgciVPg6osRcmqJ9Km1pz_pWQfuIDy94-Pb_dMyPyq0cq4yPHL8E9kTsoXx6ycPX1U8_1rDlXpxInH5CiLudRf6mr6oM5nlb5fnmU2AeuDsnycv6ICGuyqJIqXuxMR44USI6cx4koaEePXKuWuL6djMgqwhkrq7UxScuAZrvA98ACPGLOdh-cuqa5Rpad_gA76xNNLZuPKzwhJsDlv1F8TC0VpjcvaCI9FMeu608XZy8U1gPBi7m-3uebgW7a-kfVc3_7-D8zVIVCqF-2nw615mn_c1W8Ovsalgo4ocBMY7AIuSl6uDoHedSoByiCNolAiQJu-cnZRtJ_S-oINj_-sUZQ_vQnH9unlTRXxTu75e4EOq63d1yj3Itrb-bvA6x80sJOjcZ1KIWCUQSSjOTJuLpAuKbDzSUT0WsHRVmrWKqjBYkrEXB5_LRrwzVoLab4L5CyyoVRVmlpWngpQ139acqL7uJMwuZw3XM0kzPcwcAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
۲۰۰ میلیون تومان درآمد در ماه از معرفی دوستان خود امکان پذیره ؟
بله.
شما ميتونيد براساس مراحل آموزش داده شده در ویدیو از معرفی دوستان خود کسب درآمد کنید.
عجله كنيد، ممكنه دوستت زودتر از تو دوست مشتركتون رو دعوت كنه
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/25238" target="_blank">📅 22:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25237">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LA8VH97SsP3pym9eLRs7DHzizsaNynU1UE12mWJJYMQZrN2WeMdvs0helplCVML1K7a-DJ-ZBu8OK4kIeKSB5SVYk1k3Yv6D-G2wktNd8BZFk72QSwB_7v05SqIOGOgB_zkc_ojsB3-IquDeFdQqoovJdseYJ3vCOUeXqMD8NkHybMnzVfPz_bragu1cSJ6i24_Mn3fgkBx0psxgIEeS8IMvRoqRmcQBj4XpEYYsHZNd2HG_pflqzOW9dpEEbJZngbl8EYZYoMObddRSsrxkyf4r0Y7460R0bp5aRa9RBGSaAya2dlJ_AJdAxppM4GvYxdzqnaJWrZc9Z7O5iD0Czg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ورزشکارانیکه درحمایت‌از مردم از تیم ملی کناره‌ گیری کردند: یخچالی‌بسکتبال، محمد امینی بسکتبال، زهرا علی زاده فوتبال، موسی اسماعیل‌پور فیتنس و محمدرضا اورعی هندبال؛ بزودی شاهد خداحافظی جندین ستاره تیم ملی فوتبال نیز خواهیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/25237" target="_blank">📅 21:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25236">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtODz4ZuWiCIREsTaJVb73aGgCjA1EgJujmC4eGC9-C3WgVl4gKl1OJ0C96wwMEr45sWXGvYYLbSiCNohIo6cq3KlucFidKA8pwOLbNYqKrl0qOVIokMErqYGwK7qP4b-xIcuhLkPeIrqz9IMO_A1tezd6IfKjmThKE9CBugBa7RcNAClTxrUeJfNv6ZKMXyVTqyr4xL7vhs7gpMs9sdqrCLgr8WC_Txhw0dz0xjxPMdMkAVlHljJSikl8WFYW1SgypnWf_EAi-lemJtb-Lwdjt7XaY576-nwa0cmC8BylsXgzsC30LjrieyBb_2__cjPezJSYckshaiQYsUHveCYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🟡
بااعلام مدیریت باشگاه سپاهان؛ گابریل پین دستیار ایتالیایی محرم نویدکیو از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/25236" target="_blank">📅 21:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25235">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LI_mTx9ahU6HEAXcF6f0dn0shyaBHmyrzxtwg-x5ENXYnsALH4ynIevsuZkhkvQyeVCJ-JIOB1BddumF7EdKP2MkHRMUnhT6whP3w1OLNQBfMi6-FGgm80wLwb1lSxg3rTg_4q-VXHZUXsdsX9Cro63V-Rfx5h8odc1bIYR3rWS1LiP8repImy43r5Ib0kbeH5AuASSCCRvj4rLpkXCvtbU0BVxCejU5VcHiEssvTtzo3Dtj9KRr0fUf5hbQrxx8SfN4eRXW7bujw2aRvezkvLMIOWzG-wud-taWdSnijG59_i6Uze1CwW8DRgW5MZPPBc5ehyO3aXFeD-RWodF6uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌پرشیانا؛ مدیریت پرسپولیس پیش از انتخاب مهدی تارتار بعنوان سرمربی خود؛ با ایجنت هادی‌حبیبی‌نژاد مذاکرات‌مثبتی داشت و حالا درصورتیکه‌تارتار تاییدکنه هادی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/25235" target="_blank">📅 21:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25234">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BP4q_76sVGT_ZoAZ1maLVECSgDr9_0zTVMdwnFaWpivMyxVuN4swUW055Kz_F5rd4k5R2wy-MbF2rl0T2ysGMlttDHLpPLk7dXxHUkgeZum3N5f5-qZ3DXaEZ1UpA5mlSKTVm_AF12QUnQl_ZE2AGeWfD_gq8P3c4TC0dafj_2y-2VOcusL4UxOZ6mkeOMruf05jUTey2qB07vRqaE4JlnSNRaXsMSX2bk_EKCnaM7mtmAtoMHJRM0f5I9GdKd5e78TwfkY4kVcyOR82ckf7kBrmS7SpOv8jEGnsh5dO-4sf2mhBpIwddJrIlwJxQqCJEWMTTEdeKPtaX2HfptX9dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امیر قلعه نویی سرمربی تیم ایران:
کاش قدرتی داشتم که بعداز گل شجاع زمان رو متوقف میکردم تا شادی واسه همیشه رو صورت مردم ایران بمونه. باور کنید این تیم شایسته به مرحله حذفی صعود بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25234" target="_blank">📅 21:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25233">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlIXDYc-EM-t8KD7BXJ4cAM5FsFCh_LQGsFUE2Ucbbppt6HwthmnxmXGsUMoYFf4WJmpFtZBUrR-3THhoFWOugzFG99ceXq2T2cQFiaqtzbQGJfW-2M2d_mjmd1TEF3k-qBB5QD_B-Zesk9jE6IuXb5-lWo2PkdXmizcP7N6ImvOlDaI1a6tjLTUDBaLV3MDatw8Z8UJl-A1BU6staUF16wNp1xSAGNo8XgNs1edUrOOHlTxcu6VFRrChtgR80rCKbURFfhSFIiTGtoxRRmkL90XewojZLwl6j5CN23w7UqzSb4CyqIdrjruP72_ZxZwjlVnd8dVpmWEoFtiGPF79Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
غلامرضا ثابت ایمانی هافبک‌میانی‌سابق ملوان با عقد قراردادی سه ساله رسما به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/25233" target="_blank">📅 20:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25232">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBowBa3RSqzC2yuGN_NHyNddUcTOyJO4GysYsK_r8QiVjDg-JSxAVGK-RW00-kWLxMHk6vwFHs0z9TaQ1iyn5zdLC4RjYDrD8nzit-VK4_qpnLSge8-r_1GNcCSo4J49iCNlEXRXj01SY2VJo0pCNOSo_ArYsFd7kvSPfUbQjkp-0bNSEUxjnIbvF0B48gXW9aXxalkZcoTGPt2s9kQo0kkfdIns9hK-TelrW43LC-fOKQbFFQn66yMzLtKHcDiL1G9vSMXMVOKbkLIEQLR55F4K9gK6TOYT-oLuTTfdgYRu77MRvHtjfmf2kqUcHLRifPa9VxpoHjWNFbCcio3aHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کنایه‌مربی‌مصربه‌مسی‌ولیگMLS؛ابراهیم حسن: فیفا میخواهد مسی توپ طلا را ببرد، در حالی که او درلیگی بازی میکندکه‌فقط 3 نفر آن را تماشا میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25232" target="_blank">📅 20:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25231">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G85RUkpE4BSsukxBxP_FFSwNXmeRPnHXQluvMDiRFRctDq6W6-kRP3L0ElXqI28L0PFxouqlua7BNEMmc3Mm18VhoqlngC7XPsX2K4q3NSQ_nooQq6Fj0_xJcutfR7_7mRfaEZHsgsxPeG6faxkF0VJ5E8te0Lg4ai3ItA_7XXX9TDUoaMdo_6nXsp5sOACv9US-x8L2TlzK67Erycf1D1w4Mc09zJjbW1i1hXPDw1ph7HEj71WbkgJCmS0-evaqgpRSu6rexxLGj22NKwgz4hHDOni_cVZzzATxAGFCxvCCMo6Jla19imzh95aqFdq-LigU08fRR2cpsNHwPMAczw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇦🇷
یکی‌اینطوری هم‌تیمیاش خوشحالن براش و بهس احترام میزارند. یکی‌بعدبازی از تیم رقیب میاد دلداری‌بده‌بهش. خلاصه که یارخوب تمام ماجراست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25231" target="_blank">📅 20:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25230">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UWTgiNwRx1gQVhiyRAZ67owFh1CRKjk-9Ob7saqYNSU74SqDhajyptExH26HrsdYf4bO3riP2NnSLHenoA8vx2AGVsxyyz0n_BK0qK54kJGh2Pq1zAunhn7nOnNGxg6MdnjPxWmj0x02U0IDU_CyU5B5JxlLXYGLSOKSEa1zy4mM-SPezRN2pMeLA7rAnAmcUUTfByLWIg16cfVZVfKsY5g04NAMC3HAyM79GlBuyevLbO4_Sdbf5RhQHcmPzmiq77lsEW18iH3-5cMuJ1W7KvLl-grMJUsH7fJxJOi1h5a8SZEkuMbPQtVwJV40a39mbO1W3qju9vwu_4bAR0vVMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25230" target="_blank">📅 19:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25229">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qyKrTUK_53pV2zA8S5BgpPxim8vRUSuhVxo5DDSbyDwCB38uDPJeBLTHNJY7ZGMr_QIVsqPcSptmZinE_NpaZVrnyySpbwhPsfy_Uo-OYxjmqxlvEOwdDwCptHspTFZuGJtWzLdnG-9A9VFVW-7WA65p2lueRmXawJJhjyjMMBBXyPsX-HMTJJcP2DdwdtJv-lO0Zg9ZuimX4ZtPjNlWT4_6Kv1yOxdu7rVnNjPovFxCa6ZfYuSgXIV-bWNldeh6aw8IkthhmMlKoYOw6mPfSURcBruy2_45SWPAR9FJY0SrYb59XGhZtfFuCz7ljScR_Iee3NoFDiBaFgeTdAN8FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
#اختصاصی_پرشیانا
#فوری
؛
مدیریت باشگاه‌سپاهان‌برای‌جذب‌قطعی‌سامان تورانیان مدافع راست آبی‌ها به باشگاه استقلال نامه زده. با توجه به اینکه‌باشگاه‌استقلال‌تمایل به‌جذب امید نورافکن داره و مذاکرات‌مثبتی با او نیزصورت‌گرفته درصورت باز شدن‌پنجره آبی ها این معاوضه انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25229" target="_blank">📅 19:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25228">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7acbde92f2.mp4?token=v3__Qb9D1mJjoLS4ezunPyNLTfVGHx6SnqwY4SlCvOIpxUUwhRGii5yLnu_dchUv9FB5d2HEhW8FgWFNM4qyHbG2B1swq8lXdSldC4lhVJj_gchz6sDtF0vctoaAbaUaRisnlmc7-YIt7ych9kpZ9biCaW5bgrwHhUsBwJNTo_qol-6DSanwfp0u15ibTVAyIdykR6LMCSaMJ5GJF_FS-FLH0fBNq7BaJyoxjdFv8aVQ4Ib3eLCpMzzUBrhejcytISFfw_30-6cG5M13pUXtc4WVHgG6a7pizn-X1r4p_qNQ2Q6Uw5f2m0S8IiuyGrkvT0gr07jX2v8zyW2oIrlKjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7acbde92f2.mp4?token=v3__Qb9D1mJjoLS4ezunPyNLTfVGHx6SnqwY4SlCvOIpxUUwhRGii5yLnu_dchUv9FB5d2HEhW8FgWFNM4qyHbG2B1swq8lXdSldC4lhVJj_gchz6sDtF0vctoaAbaUaRisnlmc7-YIt7ych9kpZ9biCaW5bgrwHhUsBwJNTo_qol-6DSanwfp0u15ibTVAyIdykR6LMCSaMJ5GJF_FS-FLH0fBNq7BaJyoxjdFv8aVQ4Ib3eLCpMzzUBrhejcytISFfw_30-6cG5M13pUXtc4WVHgG6a7pizn-X1r4p_qNQ2Q6Uw5f2m0S8IiuyGrkvT0gr07jX2v8zyW2oIrlKjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
👤
طبق پیگیری‌های پرشیانا از ایجنت منیر الحدادی؛ خبری‌که رسانه‌های‌آفریقایی مبنی بر توافق اوبا یک‌تیم‌مراکشی منتشر کردند کذب محض است. این بازیکن اواسط هفته آینده به تهران برمیگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/25228" target="_blank">📅 18:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25227">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KK9tZ7DqwuoaR1GTApISh1Fr_8fzMoYOJTqN4tn4UmZtCfT4kQBy9q0wcX8zClh-rUBcNeahx6wYf6Lv5t8RtiaWQ92Tt9Mz2csEqAAuK7E1l_lPHLjMJGgz6zpRr7X5PLE75-x5TuTy8iGg_QeQZmO7ENobl-c2YM0XQSTaViPuJQWZr7F7ghORamS7FnoTQZdivv2Txih1WTZcCFEy_ZNZyw819omjzu6ZdwwjebCGkqrqnX38NposVPvwwD25tUCIHLlUbMpysigh0ciYWx4qpWflewP2puUF-t_SMS2vsxDF9UCr0P0MDALBbxL_JxjveNQEUNKC8Zv8viXRcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
تو این عکس لیونل مسی با نصفه بالایی صورتش داره گریه میکنه بانصفه‌پایینی داره میخنده، آلپاچینو نسخه عمودی‌این‌عکسوداره؛ لیونل مسی بعد از بازی: من گریه کردم، چون احساس کردم که هم تیمی‌هامو بخاطر پنالتی که خراب کردم ناامید کردم. اما خداوند برام سوپرایز داشت.…</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25227" target="_blank">📅 18:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25226">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-6xlJ3udXlInqXXNavbOp7i0G4_w1K5bgWRdZYaRwm9J6AfM7omGH2hpqFjikliDQm8P9TXKqOQOG655yMKBIB0ZGEsuWmbIIAyCK2NKaB0zFa7KIJTsgZLF82eZaitZhaV61NyPP3Q_VNRr46LIpFka0k_W3Jqwhq9dmByvfpYutsvDpHIuzbmyAI0UG-ugWUFfuglw4TZShUVBdjAwQwlxTHm7udwORVSHPPLl-16pUW0SPsyu_dPZhdNHYrRYs12H2XgDu95CDFymI_SuanCKjs4r2lbSz5e5s6g2k_rKsDZwCVEnlEgOsZ2tkXs32TxVAGfC9ptCN0GPbKY3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بمب اصلی پرسپولیس که امروز رسانه‌ها تازه دارند روش مانور میدهند سه روز پیش به عنوان اولین رسانه ازش‌ رونمایی‌ کردیم؛ بله مهدی ترابی بدنبال‌بازگشت‌به‌پرسپولیسه و صحبت‌هایی با مهدی تارتار سرمربی‌ سرخپوشان نیز انجام‌ داده. تارتار بعدِ اومدن به پرسپولیس‌بلافاصله‌نامه‌جذب…</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/25226" target="_blank">📅 17:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25224">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pI6QDvzj6Hqwkt8fFkGRG_FZ4ec2RbwUqR_5Z04tnJRLSn3rtD5ES_RNGmFAOVZA95Slg9wAZe7h8BgL84vY_eNO5LVhV0dScq63d1Wu_PZzow2MrGOxtoxm217BPVsys1GaraQ-J7bI07TeqO6NQUCaoDPHPKM-VMsQuN8ChpERcAdL8MkYvxAXZQOH7foiUOqmkbxdvq2Fpq_dsQr8TyVWCzeXwKrCG4B3DsziRt187BCGf-dk_3q3nPV9r52qJf7i2OKRIv3t_sktzns7XTl18umBIB0oHunIvvKp3MyhuimAMKwozbolAZO11k_wfVahAwn9Nv6XcgRTQ-1j8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
در‌اقدامی‌عجیب‌ازسوی‌فدراسیون‌فوتبال؛ درحالی که روز گذشته چادر ملو با برتری مقابل گل گهر جواز حضور در سطح دوم آسیا رو بدست آورد اما مدیران فدراسیون پیش‌تر نام گل گهر سیرجان رد بعنوان نماینده ایران در سطح دو آسیا معرفی کرده اند.
‼️
همون موقع‌ای که AFC خودش…</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/25224" target="_blank">📅 17:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25223">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2QE5njG6via_rpdPiAkXNc7UUs9J4UhxdYEgYU30rsQwD2EJUC7F7VTe5aY7wyhzTIzwz_e96XpqN6nzq4KkaJJzGoURV0ZhJW5DV9EgR-6Y2DBHCO0jQDzE15u13TGzCGGOYAs0qQsIEl3k4M11ncKY5jPdBSj1aOFPlcRmUh4p4p2XweDbrajmanxNkdHri4Jto2Bx_YbyfY7Fxy_gL7wtdH8yCamrQ24Ll5E_fY3l9VP8irjBOMkFNyeh_t0RJgc4JTEFcGIInqzjEFHCET19IxrVuTFk4EmVD3zTgrEu8KYnZaBTc3qirbAsBndr-6fqpTBdwSjDeVWkTO9pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی در صدر موثرترین بازیکنان هجومی مرحله ⅛ نهایی جام جهانی 2026 + توصیفات زیبای عباس قانع درباره لئو مسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/25223" target="_blank">📅 17:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25222">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COlNRwyAkXIz7qzha8mkfDk6celGHN0XVMTG5dbrGp23Tt1knnXV-ktytv4rTnOp-UijUAZU_KBS5AKbKeBmUZOyMhZuKu0RGKX3dy9g0mzOJzUKB4Des1Ph0bWbcRx4h82kqq4f-d_p9Wr0GsoNQPyp2NXNicqfd5d3EceHu6WP-Qjauwb_6hoa6lzCZj6nYSKtoSCLn5Kp41AQoc-gWveh6QL1NXmzwjOcgKTGeXdeBk7lJ-29v80wZxv6jcQwpVo17Rma631Rp1gDmEMz62m9mDG3nnjDMD1OrmmTbxpB4kQjSDcoKJt6kxSXZ8LTMLNt3Q--R5b_DzlnvILv8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ مهدی تارتار سرمربی پرسپولیس ساعتی‌قبل‌خواستارجذب مهدی ترابی و برگردون این بازیکن به پرسپولیس شده و از مدیریت باشگاه خواسته  با تراکتوری‌ها مذاکره کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/persiana_Soccer/25222" target="_blank">📅 17:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25221">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3huT0WP4pCg6ZUMb-I7MG2-7BYggBIiKDwbO4bXnxM4KT94nLB-QJCJcvx_PlRuVfV3FAI_w_vGjJqG46WVxZnpBV4mHk0e6-lHPvtSMXye9M0BBwVplJd7jOxZCNtcPKAdYelaJnIkLOWZ6X8rhKREWvHK9eRxxiDP2AiOpjkRjUuaHUrXUFu4thX5Y--iWw4blvRX3EqRKaTOm0Jm9zlyUkpcVn1taw1zAGUSyUpmJo5pLJQvSrNSb2QEJsyDLvGeUM0sp-PrxXoufibb_HH6uS-yjyEv9DJgOp_DBq0RCGNiurz8E9poH6u47Lhu0ydyltrLm8grzDmDzYdk4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ محمد جواد حسین نژاد یکی از بمب‌های نقل‌وانتقالاتی تابستانی امسال فوتبال ایران خواهد بود. حسین نژاد به ایجنتش اعلام کرده قصد داره به لیگ برتر برگرده و راهی تیم محبوبش بشهه. بزودی جزئیات دقیق تری در این باره خواهیم گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/25221" target="_blank">📅 16:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25220">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKEpizaO4JiKCcR211r1S_9MRVoLaM4q8c1gwUQEdR25sbzuHRyYQdxnQJMULXS9cKDsq1NJb4uAeoZJXIJQ7bd5vtjEu8vy6ToOI6oKCJs-CpCuOQjjG-lFmp8WUFKK5lu3OeFQU-BkJv0kMrZ4Nsvt4S85SahEU0B6-C0v-fs7bvi4rAawcV53gkHD9tpTgjCeWdgNI5ob6FeSr_CEZXmjQl0ZpyJ-nvleWbHZyoq5AvJ8NULz9VUOp42cpCUWQbPhgeEXy4Bx5kgovxLYjS-79n8Tq15Ci-oln8c4F9pB4TLpB40RVnr_k7deuHOyENFydOubm0DPWy8lqsjPPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
🇨🇴
#اختصاصی_پرشیانا #فوری؛ یکی از مدیربرنامه‌های‌حرفه‌ای و کار درست فوتبال ایران که رابطه‌خوبی باستاره‌های‌بزرگ خارجی داره بار دیگر با خامس رودریگز ستاره34ساله‌کلمبیا و سابق تیم های رئال مادرید و بایرن مونیخ ارتباط بر قرار کرده تا او روبرای آوردن به لیگ‌برتر…</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/25220" target="_blank">📅 16:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25219">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkvqkPRVcfPcu4jacSI-mEU9yKdmmtHFgWTgZ4I1yvPKUbqUohVOjTiBoLFODZJW1cicm9IIBhfIzYptFf9uHYq_3IouLpdpSCE4ePqytTJFCEx-JevwlELvO1KP7-PFMnuakIvfhHFHYYPqdJkpZlXEkm98fNNLbNwYB2t0xNEUlEjfR4tI-QtO_kbCi39h46celOmRWochYGX_WogiJgav13AmusTlBWBkeR1QhP9upz8_V9b0mceGHAN0ICGNELvi5TE6bGes1KDnYNcHi_d8FJRkzKc7nTWvadpoSrGmfEKgAa-LGPlGve5FW6co_Q_4biQiKbDSN67xbp-abg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
👤
#اختصاصی_پرشیانا #فوری؛ طبق جدیدترین‌اخباردریافتی‌رسانه پرشیانا ساکر؛ محمد قربانی ستاره23ساله‌الوحده امارات ازطریق نزدیکان خود درباشگاه پرسپولیس اعلام‌کرده درصورتیکه این باشگاه بتواند بر سر رقم رضایت نامه با اماراتی‌ها به توافق برسد حاضر است به این تیم…</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/25219" target="_blank">📅 16:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25218">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f158271b54.mp4?token=Llnq7yQecDLWxGHEXOVmvU1yO9AciaGDhccHu0c8bSRF7itGiBz0jlf31Tr1a38QZwDQwvO-Lp1N4nHO-2GzktCCxBrb3mNydxPZGSKmwx9Ung9lWqC2SvmmTBFVsw-YcoXqwDWIJQnpWOLJzgJ74AuK52DW2Lcb5JKRMQWjRAGg4od9bprQ8YnZDyL_CHm9kW-h5LvbdSZ2UzJ76UhQqF1R3PptyLvaoPPgBy_bGzWiU6tW0U7tTftmc9SnSUJfYCHLOMmQ-4-zN_dggEv8jxmBlARWOXVO8JeVQ5ScYmV0feN2mIQxIlMkjo2GsqzDyAX1Rdjnyy6acLM1RdarBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f158271b54.mp4?token=Llnq7yQecDLWxGHEXOVmvU1yO9AciaGDhccHu0c8bSRF7itGiBz0jlf31Tr1a38QZwDQwvO-Lp1N4nHO-2GzktCCxBrb3mNydxPZGSKmwx9Ung9lWqC2SvmmTBFVsw-YcoXqwDWIJQnpWOLJzgJ74AuK52DW2Lcb5JKRMQWjRAGg4od9bprQ8YnZDyL_CHm9kW-h5LvbdSZ2UzJ76UhQqF1R3PptyLvaoPPgBy_bGzWiU6tW0U7tTftmc9SnSUJfYCHLOMmQ-4-zN_dggEv8jxmBlARWOXVO8JeVQ5ScYmV0feN2mIQxIlMkjo2GsqzDyAX1Rdjnyy6acLM1RdarBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تعجب‌مهران‌مدیری‌ازدرآمدفغانی؛
علیرضا فغانی سال ۹۹ وقتی‌ایران‌ بود: به من برای قضاوت هر بازی ۶۵۰ هزار میدادن که ۵۰ تومن هم مالیات می‌گرفتن!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/persiana_Soccer/25218" target="_blank">📅 16:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25217">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lnE3UhxN-G_Y13hoslSzNzrK95u4l4E4E0KY5DsZhpHK7g1xJ7Yi6Jje5wF3u8RlM6k6rGiE4h465OjTogKs_1SpmXqiDr3hit8URUxAEcADkuJzon8hkBthE89-Lw9McWVHB8jk5S9U2_VvfMJ6BEUc28LmLpNy8Q8z_tTDvQNlF2BU0rE73lCiU9gyNrpeaUgsLt5kyM5UcwN8DYMWAsQPrtTU1DHvs9k3_oWCED1JI098vR_2mRQ4N6MHuM5cpqoJ4Ak4PvEg9rQ6tB6_GgBl_fATePcevshs5roS5X6aZ6YOCYoqIR0zFrhpN57hVOk3kxD3hRdWWsrOxO4K7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛طبق‌آخرین‌اخباردریافتی پرشیانا؛ علی رقم پیشنهاد خوبی که از لیگ برتر لهستان برای علیرضا کوشکی ستاره استقلالی‌ها اومده این بازیکن بعد از مشورت بااعضای خانواده‌اش به باشگاه اعلام کرده به توافقش با آبی‌ها متعهده و بزودی با حضور درساختمان باشگاه قراردادش…</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/persiana_Soccer/25217" target="_blank">📅 16:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25216">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sp4ziIX9R3VXW7fEnbb2U2vhUbDYLhwyE9YiI0mNA9IC-9DX0QP2sAdIkaY0Y6vS83n0d6Kch7ui2Cd9qjh4O4nE0FBinaZrzkJVlExQp-nOYjOMmg2UU5gMCS_iH305TSgdqC2VWBh0xz-H-b1HuhuNCtn-n_uwXtcy-TLfyh--dOPRMbTIpxdJtDkhVxr872wPyY10CUUa77r1SsFjHUEPWq0DzCtCr_C5oXVcquc13Da0WIG3TqEqiciRdqNerovWUkTfCA3_Cg7ui4GTlby6glbcma_1DiBol55UOCiOus3I30hq5p02VXbUX9wRRaNHu0ovX4QcOh8D0OiYyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی #اختصاصی_پرشیانا؛پرسپولیسی‌ها به محمد قربانی پیشنهادی سه ساله با رقم‌فوق‌العاده بالا داده اند تا این بازیکن رو به هر شکلی‌ که شده در این پنجره جذب کند: سال‌اول80میلیارد تومان، سال دوم 110 میلیارد تومان، سال سوم 150 میلیارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/persiana_Soccer/25216" target="_blank">📅 16:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25215">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jbGVtoLBcSuvF25s1zHfUM3lylc8lvvJNg9nBUlWCXhhQ6EsrmjGYqx8S22yS7Zdvq8Or_b5hpFuC5eVR7HksCBsJHzeJB_JUwyUht5Z8srYjJH9B-fnvGg0V1ZzVSCnMA5Gqcb925-hBS9P6ELr6kyqFs6opbdjNJdEuDVovBkbqBUF0BzXRf1ISEuuFNkJwDc7_NJmAzxfvEnPHBuNUQ0jUw1Mo5vuWOhmfFKcLB-v8AuUVa7g5vEcHL5sOWhjkcJ7tDWp9et72ZXXvwtWOSAtmvsGRY8mEXlEu1n1SbTooJMZ-n2nwBh6hUxPqoKLjgUWrwnqVvD3uuqRpoTcSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ آرمان اکوان باانتشار این پست در اینستاگرام باهواداران‌گلگهر خداحافظی کرد و رسما ازاین تیم‌جداشد. همانطورکه‌گفتیم اکوان از سپاهان پرسپولیس و فولاد پیشنهاد دریافت کرده و ظرف 48 ساعت آینده از تیم جدید خود رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/persiana_Soccer/25215" target="_blank">📅 15:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25214">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEEQBp0bfuazdNFpfig-Okrte-XNnnrUKxMETKGOgtQTBsCzZq-hG0moJo3cBGqL56wZiOK4JvaVTNfFOwIgHpvmnfCUixMFZMEkT6O4Ugo4ju2LQtmF3ZYqs2H_R8V20-hx5YTsjUvEHzf6qytI8FEMCcAK2lld2DkTQH1rcuDsA_waoDvvym7J2T23fxalra_W4ItKGFkpqAJZtt6Y4tuu_hhwFj0nixAPfdrWqae-td7FYBRAqiuHp15Rs3KdWjwZgSOhgYybQX_2n6rdP0220bzZXBNZa17ilqhvvEZe5rzpzXnMhWne9B3yhzmikDxlJ62nf-wsYIY1snow8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/25214" target="_blank">📅 15:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25213">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e22c0f699.mp4?token=tOFzjQurfg2o0SliVPJLSzoZWW3_hZk7A4dPkWC9thKi4NZTdHvH36-Sy_2sI_o6uCrSOBhVG19wixKvd5ucZ5opiF7DowltRFBxX1RR7pwZLS11G9iI4mduE8jEElaOJ86xD_c7V0iig3FOyieW_E58gR0xAdcpJcgvUZyEo9PemUIDvyghU6-ZEas27_wA2bWvYsR4rTTi_Y2yBrIRmr8gsd6MI9Mw16IkMGtFl4D9MiBlQbGa2hjed_n2Ym4kmAn3QtPWmDUQovkC5LcW3NzLmHaaEGrqHGPBWwhYI8eN_oRthOcUrGVkq09Ii94rXq-WFuJPRMXfAOyE0IoaeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e22c0f699.mp4?token=tOFzjQurfg2o0SliVPJLSzoZWW3_hZk7A4dPkWC9thKi4NZTdHvH36-Sy_2sI_o6uCrSOBhVG19wixKvd5ucZ5opiF7DowltRFBxX1RR7pwZLS11G9iI4mduE8jEElaOJ86xD_c7V0iig3FOyieW_E58gR0xAdcpJcgvUZyEo9PemUIDvyghU6-ZEas27_wA2bWvYsR4rTTi_Y2yBrIRmr8gsd6MI9Mw16IkMGtFl4D9MiBlQbGa2hjed_n2Ym4kmAn3QtPWmDUQovkC5LcW3NzLmHaaEGrqHGPBWwhYI8eN_oRthOcUrGVkq09Ii94rXq-WFuJPRMXfAOyE0IoaeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#اختصاصی_پرشیانا #فوری؛آرمان‌اکوان مدافع میانی گل‌گهر سیرجان علاوه برسپاهان از پرسپولیس نیز پیشنهاد رسمی دریافت کرده است. مهدی تارتار از مدیریت پرسپولیس خواسته‌اگه‌باعلی نعمتی سر مبلغ به توافق نرسیدند با ارمان اکوان قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/25213" target="_blank">📅 15:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25212">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O863jbE0GlPAWR_MQ3n9cpO6Jhu2VDDrZ3KHEPVuhGlc5RxEFyx1ZyGeGQz4C-oqnR2KojSDfmusHjLh8BZ413EQ-4Jj2NDeeX5JNoPl3JTdSJlC0-5Bxhj9140FLJl85pefisJggFAp-sfYoixsQmxxMrhbvMzK12kkdQUOJ2m0Q0unPYL5BekzmzBeehOGb2OsExCM8RtK65yMbkJDsrN0LaoGEegtWutF8lPbOtHOQtZggveW-r5hdW27gxrpEbT8CwJCpyoAVBXniV-QXzJqDxaKDxB9joxk4t8Nko2eUjVFf4Z7j-hSZYEuY4pU6k60S_qSTAkvvW7J9s4nZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
«
وزینا»همبازی مسی میشود؟
براساس گزارش روزنامه مارکا، باشگاه اینترمیامی قصد دارد ووزینا دروازه‌ بان 40 ساله تیم ملی کیپ ورد را به خدمت بگیرد. او پس از پایان قراردادش با تیم چاوس در لیگ دسته دوم پرتغال بازیکن آزاد شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25212" target="_blank">📅 15:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25211">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fS0m5lYcTKY6o_-2FLmFS46nyh-OgBBIqABktdcWSEsJGIeXn3YBGT_Qln0EgiamrtzNYrsFTZx_X8zdDQAkQ5kg2YM9ahrCj3Jxqr0lzmim49o8baojdmVImDuFNeDl2L6MKbcLNZ0yE4e13Dmz9Acz1xLRnl1BONVKBBtqpQP8loXywNaqrVec1vwp8GqVsW1oDlkruqf85rqy2yRZUDlUE5sElH4TWn1TzNEBoGL4H9XiwxqmJhlcOAI3WyK8Kgb2ZaoZ03a79NQCQD8ee25qlg3NbOpzrtkzEUi8ZLyeFlZj9bTPnR372F7TM689Tpw57vlpJJVNHwNoFgM0Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون فوتبال کرواسی رسما جدایی زلاتکو دالیچ از سمت‌سرمربیگری‌این‌تیم رااعلام کرد. دالیچ سال 97 دریکقدمی‌پیوستن به استقلال قرار داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25211" target="_blank">📅 14:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25210">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZfPoeOuxwHQKWXFCYAfYO9ixO4EV9J6_ZqWUdQF4o8I1uUXJ-nhN9yY9LAraJNLpXcNsVW9KZoOzXVS2xFSFgRMUb32n-PgzRheAAs0hw0oKS6qMIwrwolrKueCy3aIwAM65w8ovlnpaGug2ZxZvl-ny9FMed6TKxVDOXSnrWdaWt_mp6wmhfbA-ukbcj7Y74KI_sKhKwjQF4O_lZV-3Umn0mEkQcJPEN0IdYLmbyjv9eE20r4mzpwbufBUhuQeprQz5Hw6JEt414jP1qolLIt8haZr7qOsuZiPDnEHnt7cEKxmSCtCwwBMU0SCJ0ll7tOORKsqObofcoPJN85etA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ابوالفضل‌ جلالی بعداز امضای قرارداد خود با تیم پرسپولیس ساختمان این باشگاه رو ترک کرد؛ یه عده میگفتن تازه الان میخواد بره داخل ساختمان باشگاه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25210" target="_blank">📅 14:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25208">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rxgWumkweBWp0RCf9um48aKc-8mOc4CGMT3qP2-5Kg-ggC0T8jJOAGZHhp-IXEduIFyNINZ16MhiuWxavTr_7icI941-lyYk63Tv4ihwOVsAlpnAkAdV01fc2VZOXYYaor7L4OHreydRci8u53FmJgoXsFdZqG32tD0jV97YdKtF2N_mnA-Z_A07cgQJB3uPK-P6CcwiI-d-M4jjZXvMXpI3JFgpypEeT9DwxV1NsdwNjLLxJPRSUbuFcfpqhQC5yNLe3IeKoPBX4jMyMBThsfveRRdB1snAtJMiBA_5CplU5-ZiRuQ6dTSLvly2pVHU7BfunSXJJDYOZ0pPMj3wNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbd67803a1.mp4?token=TpOk7IBvveFsOIg624k2YD1572pWrY51XqfO-bDoJ7mvQl7zBnp0nCm50XwoLceog_11G0kxJwK_2zfn62L7AdIq2JwjeZoCqa9stymQryfOeWwU1DJPV-MhZSNdy2W8XY_VOuVpyWfzZIzpKQxl3zng0v2qo__xQw5TPpYYaDwdz8oE0PPVVpqERZqZl_IAzfVzJwcgYZqn8jkejvp1sJY70AYk3KI3YIcs6re5RFpxE_M8zi1ZoE1B7xpJNSmgsLAFXU15XIeoYZXC9EwPvlMvssd3Vs3mGuJncKd0RN0KW8e4tKKhk5RNn7lva4k2sUDP-kvEfWvkqcsVFKL3wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbd67803a1.mp4?token=TpOk7IBvveFsOIg624k2YD1572pWrY51XqfO-bDoJ7mvQl7zBnp0nCm50XwoLceog_11G0kxJwK_2zfn62L7AdIq2JwjeZoCqa9stymQryfOeWwU1DJPV-MhZSNdy2W8XY_VOuVpyWfzZIzpKQxl3zng0v2qo__xQw5TPpYYaDwdz8oE0PPVVpqERZqZl_IAzfVzJwcgYZqn8jkejvp1sJY70AYk3KI3YIcs6re5RFpxE_M8zi1ZoE1B7xpJNSmgsLAFXU15XIeoYZXC9EwPvlMvssd3Vs3mGuJncKd0RN0KW8e4tKKhk5RNn7lva4k2sUDP-kvEfWvkqcsVFKL3wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
اسکالونی‌قهرمانِ‌جهان‌شد، شادی نکرد، وقتی قهرمانِ کوپاآمریکاشد خوشحالی نکرد وقتی قهرمانِ دومین‌کوپاآمریکا شد خوشحالی نکرد، وقتی بهترین مربیِ سال شد خوشحالی نکرد، ولی وقتی مسی گلِ دوم رو به مصر زد روح از تنش کامل جدا شد. الحق که تمام لذت و هیجان فوتبال تو…</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/25208" target="_blank">📅 14:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25206">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e403b418.mp4?token=gEQDmsv4CNz4GE6SSG9AaMyD4qDVHEZ-9Z8ljN1X9_s-gkrRW-bI5tZ6QqfOW-p3tO3Wz5WmvxD7eGmW_9PQBWA_uksTerSMzIwZOsEm9ilSJT74GI4rBT11Gyb_5NjaqRHS9haNhCWIiL-up6W5oId3JtsX2D-RdCU_Vfly09qE2s_cEtBEB6VIkW2FubElQ1A-7BTXjgsjVUomyvoAMMdV4Vj6nRCKvO1zinCmGKg8FyJOGoV3FAvjhUsadL4OGJFqBPFKr3H8fUQNzx8SHB6pBIzcSHaoNkKDtoo4OiafmBHpUuV2CYIofeUrkkUtiBKQGl4IdfcNXoPzDrMp3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e403b418.mp4?token=gEQDmsv4CNz4GE6SSG9AaMyD4qDVHEZ-9Z8ljN1X9_s-gkrRW-bI5tZ6QqfOW-p3tO3Wz5WmvxD7eGmW_9PQBWA_uksTerSMzIwZOsEm9ilSJT74GI4rBT11Gyb_5NjaqRHS9haNhCWIiL-up6W5oId3JtsX2D-RdCU_Vfly09qE2s_cEtBEB6VIkW2FubElQ1A-7BTXjgsjVUomyvoAMMdV4Vj6nRCKvO1zinCmGKg8FyJOGoV3FAvjhUsadL4OGJFqBPFKr3H8fUQNzx8SHB6pBIzcSHaoNkKDtoo4OiafmBHpUuV2CYIofeUrkkUtiBKQGl4IdfcNXoPzDrMp3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
#فوری؛ابوالفضل‌جلالی مدافع‌سابق استقلال برای عقدقرارداد با باشگاه پرسپولیس وارد ساختمان این باشگاه شد. قرارداد 2+1 ساله توافق شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25206" target="_blank">📅 14:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25205">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfJrhK_6u_NLuzAyx7BLEf6ZqRoIWaX2mUJGzcp98cwMY9FqRrmj6mOWgupKJ-3QRhd6m8RBHJvEdGSYUodoMvIITr6C-LFbANr9XKfjlT-EbRkJiXc9BNYq48_EDkyIqvr1iZITX35S2ZEfAH56Ud2GjxV4mJyaklUcHVMo_A5IFiefLRHxDGsdwo9SzgHKCB20TikYWouMa7Y694cIQ9pzvl-584igBTOSf2l_8KJO4ECfUKA5HXpgRN_1pxCVruqvIHBtc0KVd5pwH1QDFz4HOlm7OC653krp3pXss1U4fxbEUZfdpj2BWnAQnYXeTBXXRKvdGjWtpuQ-oSy8Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25205" target="_blank">📅 13:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25204">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRKCz8IQ_7BO8HgX28dcJY4M79_dxgBLonS3hpORz6Q3006WM1BliFPyauhAj-fqqMfawAu6P8djjAmFXSSkQE4nZYQwPh7ilkDfUpTAFnqcBrT0aMbpAipmwlaxJZ_IN6RrW6rHj3KHrJuI7WIiO963-AtQ8UtDmFaxB5rjlqGn-l1M6kXLeHNLXY7fMrUcMCd4NYdRaN5EPN2KpQXpr-B1ieaF0Gdc9kCBK5qyauIq6QgkLJb-Kpom0-VOI-olKW4rQ3bFFqSTizEidAD_wHek7kJ8R6U6Y7DVnWpZvw6VwdkDSOI4uD9PzRw4vmiWgXUvVmzpYO5KQ3LHvfe8OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ آنتونیو آدان،عارف‌غلامی،آرمین‌سهرابیان، محمد رضا آزادی چهار بازیکنی هستندکه سهراب بختیاری‌زاده به مدیریت باشگاه استقلال اعلام‌کرده درصورتیکه حتی پنجره نقل و انتقالاتی آبی‌ها باز نشود باز هم نیازی به حضور این‌ها ندارد.…</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25204" target="_blank">📅 13:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25203">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8123ef735.mp4?token=ctyHfq-sgQfdn64xsu5EVAtiLpo8VrELMHid0bCEwO6_1Hb7cD2wT84pNOVkahz7ripgZip7Dy0u-r8RZWWyv-HRAdgykWTdZDKuBeToWecFOgqew67ngxW1ju5oEJFCVlT-_ccOXDYzIjcn1wiJEP_JsbaT0z4UV6Z3tb9gtLrfSHYqK4KYoHNrQ_su5_-XunDQax-e2HO27x0Do-YVnk98qx4V-mWI3hH5S66prR0VwwICXR8aGKS3Xo0I2HhhKgC8q6tWiCZJxsh0Mav4vaPRaPjQgVv9omeIx69n3dZM7RER27upCz6HvfauYyQKDs4jcLiw_7gFsM2qbeQGgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8123ef735.mp4?token=ctyHfq-sgQfdn64xsu5EVAtiLpo8VrELMHid0bCEwO6_1Hb7cD2wT84pNOVkahz7ripgZip7Dy0u-r8RZWWyv-HRAdgykWTdZDKuBeToWecFOgqew67ngxW1ju5oEJFCVlT-_ccOXDYzIjcn1wiJEP_JsbaT0z4UV6Z3tb9gtLrfSHYqK4KYoHNrQ_su5_-XunDQax-e2HO27x0Do-YVnk98qx4V-mWI3hH5S66prR0VwwICXR8aGKS3Xo0I2HhhKgC8q6tWiCZJxsh0Mav4vaPRaPjQgVv9omeIx69n3dZM7RER27upCz6HvfauYyQKDs4jcLiw_7gFsM2qbeQGgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
اسکالونی‌قهرمانِ‌جهان‌شد، شادی نکرد، وقتی قهرمانِ کوپاآمریکاشد خوشحالی نکرد وقتی قهرمانِ دومین‌کوپاآمریکا شد خوشحالی نکرد، وقتی بهترین مربیِ سال شد خوشحالی نکرد، ولی وقتی مسی گلِ دوم رو به مصر زد روح از تنش کامل جدا شد. الحق که تمام لذت و هیجان فوتبال تو ساق پاهای مسیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25203" target="_blank">📅 13:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25202">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/867fd1f608.mp4?token=UY3dch-MpeI0CwVdoZPlRAtGyQpDta5XjY34IQ1_5yIf6_I3J0sggrbhN57VNOasFJSCmB9Ue7MD6PX-q8L0yZnSefhc2OgkQNi5Nbr-eqHaGIfwrChGvy0SmO0uG3MhlP_Kw_SSPMT5I0KdLW66jpT1p_z3a1DZPOYciv3nyz5QMhu-o4AOM-fIVvQhCfJLU_sEDSqoCMnhZ02gcyNKEjB9giyYKBe-lY-QcmR7PEP04UsNjl5jNKkIqaS9s5FcZglXGXtOY8BaWfw7dQNY9Z4gEQ30Lcp3Jz-NRXDu4yZ9yEYD5kd0WU4EnLHLdaSfXn3HJTVOnxicx3oTjAOE2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/867fd1f608.mp4?token=UY3dch-MpeI0CwVdoZPlRAtGyQpDta5XjY34IQ1_5yIf6_I3J0sggrbhN57VNOasFJSCmB9Ue7MD6PX-q8L0yZnSefhc2OgkQNi5Nbr-eqHaGIfwrChGvy0SmO0uG3MhlP_Kw_SSPMT5I0KdLW66jpT1p_z3a1DZPOYciv3nyz5QMhu-o4AOM-fIVvQhCfJLU_sEDSqoCMnhZ02gcyNKEjB9giyYKBe-lY-QcmR7PEP04UsNjl5jNKkIqaS9s5FcZglXGXtOY8BaWfw7dQNY9Z4gEQ30Lcp3Jz-NRXDu4yZ9yEYD5kd0WU4EnLHLdaSfXn3HJTVOnxicx3oTjAOE2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇬
محمد صلاح فوق ستاره 34 ساله مصر در پایان دیدار با آرژانتین از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/25202" target="_blank">📅 13:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25201">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZS-dU3nHas0RW0MOIuHfaFEsMLY0W2p1q4HESuItHg9I7zh2ZMI2H5QPQszWtBh9SyfNRIVgyHrDHWaPkLnTmtC9DYjAKfJd6UJtwEysffZwZzmMBWg_7lThuPsz_YV55nbSN_QV8RuXaA2XQpsjMWvQnCxbgjCPyBcZNwAOXb5Qe8PTg6LF9niFi2C7D-njV8rsnJKnbNw7inxy1dOhuxp_WbRW8u0bHkRzihVc3ceTU48ejfl5W3jAx2QofrQWdi4zJ5l4IdnDcHbpthsgKjwlW8Iya8U3kRb7lcrCDcD3e4b96y4ypM_4H57GuyyT4Ng0IQwD-ejty0ucMlHA6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
فدراسیون فوتبال برزیل ساعاتی پیش قرار داد کارلو آنجلوتی سرمریی ایتالیایی و کهنه کار خود را تا پایان جام جهانی 2030 رسما تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25201" target="_blank">📅 13:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25200">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEwDv0T2aKMSk6TqUnOkbQj9SrGNjOlU5zfJsp1kcWjbmozhx-i6030CBZB-bRdTfEFXueiepyNaDQJNsaoILHn8fQPn4bNNwhSGp-60CwOJo2o8bfMmg8QhiQtw90A_FOTyNcKdJ8dJoCVTl_lh1IaYslYl51MuXZqkDVhjYCalITPA_amgDQMn8vSmH3As-K9IIErrR11WGBb6SxOuY_4sRYTum8kEAo-AqRc441mmciiKTmiF4gNXoB0b11n7it9zc2bjzYUg1-LYbIOK8xwNeWk8w86l_PKm8e108Sh-uRbJGZEm0LLAZyvOQhcFTpAN5bZV_JvaFnC53AJSPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25200" target="_blank">📅 12:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25199">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWvP3WzBxRFB3iVhhRbf6P0QNg6zmn7NudAdYcs4ky1nbbKud4I6382pI-wrnEafRC60AKVepF6g91XBWIXpDQ7A7FGZvOYVnNBrK1AHobyjZijo46sDD5xqD5KN8IjGywC-u_PmGBT4u3WS6coWJ0x5r-aVjQ6kyWOMInS4DeLF1tNyPKYitiyYhsYUHRp0RBKWnAW-fohKpF5J2-GdRipvHOQnqpdRre-qc96Rqk_g0avhxAIYprUMP5GYa_UYI0VgBnzGRFVwG_emI7RP_EaauVM36EM-K_i2Jmp3mQ4r7a71H0oXeGYmHuYDJDkP7r4onwjJROaIjadH36dadg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛سیدابوالفضل‌جلالی شب گذشته به صالح حردانی گفته‌بود وقتی‌باشگاه هیچ تماسی برای تمدید قرار داد من نگرفته و کادر فنی هم هیچ تمایلی برای موندن من در استقلال نداره باشگاه پرسپولیس بشدت تمایل به جذب من دارند و فردا ظهرم قرارداد 2+1 ساله‌ام رو با این باشگاه…</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25199" target="_blank">📅 12:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25197">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32700e30e8.mp4?token=E7qOUbP3geCTebhMGv1uq7mIdkdck4fT0dGRmlTfuOdTA11T8bH175ApWhSqIHMY83DFKhpWtvVn8huq7zF-nFmTpWw95ZVm4rLvf_CfNZjklMCfyTPWUyTYMfXbjEe6rXtr27pnfyxFNhzi2vgSQWUg_3OS_Rpmbrsj3Hp0o8vUkQzZKo2EzagDrLVgqw1bbtPPFxppdAAlUGFml5XU808fxV3ZQX-50P5dd9fNL7PiL-zpPdEkOBvopPqtOy8kiF6qRGH0FO2Q7HpFsMoaWGW3Tc1XbZ-RT-j-_ayGhrF0w8t7Oc1zhdHD-CHDANXoOTA3ii4gh5_uQOK_5NOsdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32700e30e8.mp4?token=E7qOUbP3geCTebhMGv1uq7mIdkdck4fT0dGRmlTfuOdTA11T8bH175ApWhSqIHMY83DFKhpWtvVn8huq7zF-nFmTpWw95ZVm4rLvf_CfNZjklMCfyTPWUyTYMfXbjEe6rXtr27pnfyxFNhzi2vgSQWUg_3OS_Rpmbrsj3Hp0o8vUkQzZKo2EzagDrLVgqw1bbtPPFxppdAAlUGFml5XU808fxV3ZQX-50P5dd9fNL7PiL-zpPdEkOBvopPqtOy8kiF6qRGH0FO2Q7HpFsMoaWGW3Tc1XbZ-RT-j-_ayGhrF0w8t7Oc1zhdHD-CHDANXoOTA3ii4gh5_uQOK_5NOsdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇦🇷
یکی‌اینطوری هم‌تیمیاش خوشحالن براش و بهس احترام میزارند. یکی‌بعدبازی از تیم رقیب میاد دلداری‌بده‌بهش. خلاصه که یارخوب تمام ماجراست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25197" target="_blank">📅 12:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25196">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc9ab7b209.mp4?token=oWP8j_Igdrvpw4QUpFSPFOo2qQI3s-YoPgRSAOoxSdpel0N_fhkm4vwLJ7z3zsXvi-iLlegCVpwow0EEb7GWGZHPx7Q4_NRmzblrLUvfsPBUPxK3aPJlunB2EEKFr0x6VVp95jgnmpf3zHZPZejmnOAImBWWHgun-r81WnQ9PwchSOImss8d49sbzvKGlMdW2B7zIhQzAtTOFEO-G8QiHme46f4OTcDDZWRJ6wNC-Ycp7qgaFzEitPSKI4upX5kUelDGyDjuZ-ZJSqATtBhmS_PqBlaJtxMVUFKkB27-QFXVLqk1DpHdYhjfcr-hTIcjCB-zpNKSsxmk6WnFOrjA1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc9ab7b209.mp4?token=oWP8j_Igdrvpw4QUpFSPFOo2qQI3s-YoPgRSAOoxSdpel0N_fhkm4vwLJ7z3zsXvi-iLlegCVpwow0EEb7GWGZHPx7Q4_NRmzblrLUvfsPBUPxK3aPJlunB2EEKFr0x6VVp95jgnmpf3zHZPZejmnOAImBWWHgun-r81WnQ9PwchSOImss8d49sbzvKGlMdW2B7zIhQzAtTOFEO-G8QiHme46f4OTcDDZWRJ6wNC-Ycp7qgaFzEitPSKI4upX5kUelDGyDjuZ-ZJSqATtBhmS_PqBlaJtxMVUFKkB27-QFXVLqk1DpHdYhjfcr-hTIcjCB-zpNKSsxmk6WnFOrjA1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ادعای آلن شیرر:
یا هر دو این‌صحنه‌ها خطان یا هیچکدوم خطانیستن، نمیشه برای یک صحنه مشابه دوتصمیم‌متفاوت‌گرفت. مارک کلاتنبرگ هم گفته هر دو صحنه خطا بود و پنالتی رو صلاح گم شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25196" target="_blank">📅 12:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25195">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_-ClzNo3HRmxHpkSRrthCPlaC8mC7cTRo1cDp0Uj8FIhkz8wOxYmmo4UTQDAhuNwBL36EoWx-MPNOeNfsTgLKnAGBaANua_q0LCGPMa2VqJ0eya8rPOkRNiqm67P_u8lQtAvw-sgn1OVbnxtCHaJSOvPsiWfwL3EIjDf9R3teIelFWAINgU8iE8Imh1pYhW2kx21ZNJV0yZ8aKjqwlmjWbGs2iSNMadgvUAD74tkjws77HbYc3W8g6WBUsQDduE9ArGBzIzqRPmwElLUF77YGBjnx2c_G5p2l3tFPvEYjCwlSPx7b8DSUwyXzeAhopqzZLWToHpGypatVPR3V6TnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
👤
#تکمیلی #اختصاصی_پرشیانا؛ تابه‌این لحظه استقلال تماسی‌با ابوالفضل جلالی برای تمدید قراردادش نگرفته و به احتمال‌زیاد اگه اتفاق خاصی رخ ندهد جلالی فردا با حضور در ساختمان باشگاه پرسپولیس قرار دادی سه ساله امضا میکنه. آبی‌ها برای جانشینی جلالی بهرام گودرزی…</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25195" target="_blank">📅 12:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25194">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHAJQQyCJl5XqPQMbbOxBfg2MS9YgwInxFiBMmK0yPuIWVuPjonL7HuH3kLX4WRfa0qFM6OJwvFchIp_UC3BhSevUFzAU0iu1nnwAISRfhuw1vEOfEOLQUENUPsChePh-pFjugqg18UKXJj22BiFyrm7eID-qH6RFatUYBbwMuyWujMK2wpPukaB1mv4vXKfXdLJWLoCVybW8bzgnMMKPtUowWXWyawpIygr8eb7Vn_3Wp0Xi9YmRDM5m-t69JavwSG4gy9cmZn8dkv9gy2kbbh10LdQoTRjiAqd2PJcFAiLLziYuMSPU44a5VsoPB3MS9UVr5Q-sB0_u2V8_-20Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری
؛ ترامپ:
دیگر باایران توافق نمیکنیم، آنها فرصت خوبی داشتند ولی آن را هدر دادند. آتش بس بین ایران‌وآمریکا تموم و داستان به پایان رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25194" target="_blank">📅 11:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25193">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LnhyXmKv0e_2fFluDUnSwW2cPFJRfF4SwxOONxga8CixmTiKK3RuVfgb-ViwkW-QJFF2QhbSEzdbpTotLJUGcpruPNCg39rAkWmhDA2X-y82FDeQQJyUxMlKB8FnFrbcaZtqA5QKFhyaheXOUVL2__1eDdpuKEzHZHhvX5r7HS-P4TlUFQd0MqulZgfb9mrkhq80WTca0__XfW0Op9P2-NJ-nvTfloTDj4ykRmeU31h7qqecGs8L0AX_rGteSL-gp0cEXjpgmjPcG5ser_-91ZxAi-XD1YIwfXPUfiClmd3yVG19peDbiKfGwAn8tgn57BA42lgxmlJ2mHmjH9kUhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
👤
#تکمیلی #اختصاصی_پرشیانا؛ تابه‌این لحظه استقلال تماسی‌با ابوالفضل جلالی برای تمدید قراردادش نگرفته و به احتمال‌زیاد اگه اتفاق خاصی رخ ندهد جلالی فردا با حضور در ساختمان باشگاه پرسپولیس قرار دادی سه ساله امضا میکنه. آبی‌ها برای جانشینی جلالی بهرام گودرزی…</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25193" target="_blank">📅 11:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25192">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLvw0fd8cx2usBmMEY8iod9GIWriURFQqdV69lktxxA4T3W42QAniI4nzOBgqTdI78KhG_cytP-LnqSzrIgGgRLO0rYRq2oFzV95GsckJ6s3huhfnxx_NXgUtaL1diHWGs6snwBUap2bnlM-MBZDdFNdpPTKAPXPbXbkJJpyQqP7v9_KcSV_tC6mzvyAHbYGo1f0fSOD_y55_t_FDAsr4hjoW-jXkP8d8QAiMgVi48ndRDQX-mwrayjmhaVV9DgvRbw4c-M85PF8MGUKVczGIotbVQ9yJ7QusrEsG8z4cDusUtCdZEs0p7L6zUxeo2VTBIQR_pEVb5un2cMwlQWraw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇪🇸
#تکمیلی؛نشریه‌گاتزتا:سران‌باشگاه آث میلان به دنبال جذب فران گارسیا مدافع چپ رئال مادریدند که در لیست مازاد ژوزه مورینیو قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25192" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25190">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbOwa4bK37mtXmoJyJOnrHHaqipy2TtlK67pNtn6uOFRIieEy7n8kSLT7PU3tz1NbERqeI2CRQW8OJe2nV2Xk4Opd847p2oZWqRKozouRbR_eVpaeCEQyDWau8IOhf-uU-zBXWpdi2EbchKKq8pumeW-Wkf2B1MG7BN9TyHGfgpRfxVKQ9UV1-MXnZIizmyYZJWsfa-womuq3O5nORg7ACOqwplz9dsJ31sOA503wmN9rCObSerQMmk4wNxpqwQ7OBQs3C3TQ2JKYZSq0yh0Dh5fUYMT9lc6o2dJjxfyFJqOEmD1uogGoRnlE7Q0BFWWoHH2AIrL7hjzgUgLLuRSjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌بازی‌های‌دیروز؛ از حذف‌یاران لوییز دیاز از جام‌جهانی تا کامبک تماشایی آلبی‌سلسته با درخشش مسی در پایان مسابقات مرحله یک‌هشتم نهایی  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25190" target="_blank">📅 11:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25189">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxmLJqweziS8DqCvJFkr92wVq7d0u2gtOGlpbRjaI_d8cz8bXBaGCHg3q9_tJ46Qm3POWSMRLK5E6RXFn9oXnvUSY8GXWQ7Gn2_3CaYxaa9t4QCR8YsyrjmMYHdUDNnqTUDAtFidaMCDNPg2e5FSaDiLmW4cppdQ_9m36lC75YmUEl1B-f6exWLblL0z46iYOUEZ3g2MjyeY8iC9uDgSvZZq908vfF6lEtJWj0BA-nLNOKNR2KXND26fV2iF8TpBcCixigXJ_8DjZeYzwlt-nfguCZ4ywGWxr9BrsWCzCbxr8OB-D7NHmLAhWRKLX77kNKcEGfa5uwSAsMdCQtGk1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی 2026؛ کامبک جنون آمیز و برگ ریزون یاران لئو مسی به جام در تنها 14 دقیقه؛ یاران محمد صلاح بازی دو بر صفر برده رو سه بر دو به یاران لیونل مسی واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/25189" target="_blank">📅 10:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25188">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oeYztL0OJWNkZCRpaM3Bp96CTMKy09N_eTdZhCQrY7L4EroJGIcnEQYBxztX9-NIrSDZ__d_EtPNoJphhtNmGNM9i1YVuEyjVpS1BSVbf9v3i3OJyFS1BfvUvFzgIJowi_TkRBzrpBpVJ7h1tqBX3GrD9V_Qn4autvqkhVygAxPZWmHKIC2YBpWR4vLJsS1-61Ikqa0Ri6E8NgTFid4bxI4KRMVjrqv8HiCy5ADUpQYF4GpKP-Q-fo1vvnx1RhGc1rfi99pKVlYXrC-ELU3f0jJA8gW-wMw_KyqPYmUBdE23tnW7RE-G4HPH1pUuogQwSEpJkaDCfdr-JBj4PCx_Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ مونیر الحدادی ستاره مراکشی استقلال که قرار بود اواخرهفته‌پیش‌به‌تهران برگردد بدلیل شرایط بارداری خانومش و هماهنگی با مدیریت باشگاه استقلال روز دوشنبه هفته‌اینده همراه با همسرش به ایران می‌آید. منیر الحدادی دو فصل دیگر…</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25188" target="_blank">📅 10:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25187">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZBL_zlqXEAZz3NZ20dBAoAgjJnIylQd-hGjr4rB9VaZJSljQdXPycCPjrXKTk03n8R1qfaaBQLmzuQHIhpxcAZ_9vDhJnjMgWbKZaV9gPLop5vunSIzcoCi2eNbTQ6LVtxjM10DbPtSO71J6hsgkX3b2dnyl0Zs-M2AYqt51ST2nhZOTv8v3IKNwNaHuJn1oyQv2IhVoZewHtUeloSHt4tLwE7MjPc6tBPy3CVDdVrN7m1fVaSx30HqPCmSsWgFW10Nq26HDfcWM_sY1_WWLXQvT2819ULpi1AAGojze91yVGudOtVQa1VMEC-kt6RwxVonJwRQI-gm_FQnf1tDXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
غلامرضا ثابت ایمانی هافبک‌میانی‌سابق ملوان با عقد قراردادی سه ساله رسما به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/25187" target="_blank">📅 10:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25186">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9c548a97c.mp4?token=UZWnOrLNXEjuuinjRAGM7WZpTLjw-UDd-b84HuxyBKwSi4aBj33g6a_kEsjjcHciY2BHJ01DLi2Y4ATBuEfFcgzGHMbqLB-pddf0DmOUP0N_FjEU2__Y1z91ni2LcUGwGz3QOwlLv77xachW8f4U59shQH56kuUPuEoTC_ROA_dbKelUMlWvtgs-OgvlXDXXQKZPEWREYuJMjM5GaetxrCFTXjwtE53r0zjeKvx170rLfx1_SzQVTrzYqkf6QRyN60PzI34_BD4KlaTy_VlhFpdJQcELqNtRjCbkX_k0R6yL_ya6_xPaPxNsqlBs3mep8mcOUUN8ii6P9cNqMHGO3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9c548a97c.mp4?token=UZWnOrLNXEjuuinjRAGM7WZpTLjw-UDd-b84HuxyBKwSi4aBj33g6a_kEsjjcHciY2BHJ01DLi2Y4ATBuEfFcgzGHMbqLB-pddf0DmOUP0N_FjEU2__Y1z91ni2LcUGwGz3QOwlLv77xachW8f4U59shQH56kuUPuEoTC_ROA_dbKelUMlWvtgs-OgvlXDXXQKZPEWREYuJMjM5GaetxrCFTXjwtE53r0zjeKvx170rLfx1_SzQVTrzYqkf6QRyN60PzI34_BD4KlaTy_VlhFpdJQcELqNtRjCbkX_k0R6yL_ya6_xPaPxNsqlBs3mep8mcOUUN8ii6P9cNqMHGO3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
هایلایتی‌از دیدارجذاب بامداد امروز دو تیم ملی کلمبیا
🆚
سوئیس در یک هشتم نهایی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25186" target="_blank">📅 07:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25185">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a83c29d01.mp4?token=cRaz5wBsxaq5VfTF45ZYRWIM8Bk8f3F4E6MKM02n97sMGbS0JArz6aL_IRVNPneNPEV_r10niJDzrnWDGVDVCXCa6yJZIZ9rmkEdhPyjiL65sLhSDX_-ITisBHc-rVzN2bPLvTEEWg2l1HsEvnxSfq9XLApErisPF8zs_7-3UXB4aJ0RWxS_pYvMtRH0IsWAMvkY7fCWjYNa-kTwa3XpYbYzqTt97s30ol9FKKWOZ4cCy0AduDQlDnR6e5s95UOooYyqYsOL6-NZ7lbzQVW4jYbmMi3Phium3hKli2_fOzNf5IqmgEQ_Y3CIj1u6hq_UmaDQss0EFp-f16f3KDZmWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a83c29d01.mp4?token=cRaz5wBsxaq5VfTF45ZYRWIM8Bk8f3F4E6MKM02n97sMGbS0JArz6aL_IRVNPneNPEV_r10niJDzrnWDGVDVCXCa6yJZIZ9rmkEdhPyjiL65sLhSDX_-ITisBHc-rVzN2bPLvTEEWg2l1HsEvnxSfq9XLApErisPF8zs_7-3UXB4aJ0RWxS_pYvMtRH0IsWAMvkY7fCWjYNa-kTwa3XpYbYzqTt97s30ol9FKKWOZ4cCy0AduDQlDnR6e5s95UOooYyqYsOL6-NZ7lbzQVW4jYbmMi3Phium3hKli2_fOzNf5IqmgEQ_Y3CIj1u6hq_UmaDQss0EFp-f16f3KDZmWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
هایلایتی از خلاصه بازی فوق العاده جذاب شب گذشته دو تیم آرژانتین
🆚
مصر در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25185" target="_blank">📅 07:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25184">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nuohu_s-QpZGDwjXXE6Y0ta9NXnJMaFICmyeX033ltOwrPmCXnPnrOBeYijDUIhKKwOb6LDR8LAemfbUNf6o_gNjFQn9zhUz3MvWhgVqe0ebtRrv5tr97gPvx0SQgl3_Loc8RiOc8Nh9lTO3DvWaLZYN2LUVJM9Iz-_5pNqI1XlO4kFKHaC4F2CPekvKISoj6xvzkYw2UekwlFjkikzU-i9PUoFpH0Uq-UiOS4ajdQ3586V95_jMMHuw0-Zzf3YZ8YexP2Z5Qdz4LM5EiLySdld9QiECn6dCpU5ThwLXZ_3f9--OHMgVPn8wXMYLDXQCeTYhjTue4yCN8zCaY_Atpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌بازی‌های‌دیروز؛ از حذف‌یاران لوییز دیاز از جام‌جهانی تا کامبک تماشایی آلبی‌سلسته با درخشش مسی در پایان مسابقات مرحله یک‌هشتم نهایی  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25184" target="_blank">📅 07:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25183">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uaCvvxyF3Lwt6IA95ZZ_1SKsQybVsGgLv6BIw38gLiZ2hX7M7nYBY5MH5lzkV-rs8PzKtsdHPwLfaRSNOKgw8IeodZHpPAbJIqn9yYWAbwPW5AZKIH2YpIVjR5lbGNRDaBYYxlESzrNIjEoHk3PCn9zkqJVmltOfu2F6gT8jzxUabvdxYnCOrV52gKJpYby8KWxebZpLJK87HwfELxC5r0IMEu8nhsfPA-msMRQB-Ps0fw_OUqs790JwD_5R1KyXbSZv16HVmY7WDpFx02P6vOPTP1NSZinoBiNH3RWI50OHiA6Wtq4TvllKGij9Ff32FNYRp-57_TaEJxYxoW5TGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌بازی‌های‌دیروز؛
از حذف‌یاران لوییز دیاز از جام‌جهانی تا کامبک تماشایی آلبی‌سلسته با درخشش مسی در پایان مسابقات مرحله یک‌هشتم نهایی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25183" target="_blank">📅 02:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25182">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a56858395.mp4?token=IOCnWEIVfwc_W507CcG9ogIj7OIR_N414I7jLbm2vtSiTibNXALd3l6G6vb4a1HUQF6aGNNloopyqn3MP2npuY_0pPRdLFSFWB8ngmSNS-p25Jm8NPsHe75hsIMD74n6KPILW2ESNhiFD7paTfl4cFeKhMKI4iaElXbdN6tqFhzfs8U4B7V4k7o-2DTvnVmWlB7WjKgUGovUy2b2IE7EdGZiWZyyusHVjtDbIfdf5OzZ1Et5hE1cuGsLvIP1r3Sh7Vu39wwmRDuV4sawcHMqFexfnXUv2BUhRg5EArH1vln1UiQB_WzT1FLsZ06mXX1VKWZI3DtHXXXecm8Wydu-Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a56858395.mp4?token=IOCnWEIVfwc_W507CcG9ogIj7OIR_N414I7jLbm2vtSiTibNXALd3l6G6vb4a1HUQF6aGNNloopyqn3MP2npuY_0pPRdLFSFWB8ngmSNS-p25Jm8NPsHe75hsIMD74n6KPILW2ESNhiFD7paTfl4cFeKhMKI4iaElXbdN6tqFhzfs8U4B7V4k7o-2DTvnVmWlB7WjKgUGovUy2b2IE7EdGZiWZyyusHVjtDbIfdf5OzZ1Et5hE1cuGsLvIP1r3Sh7Vu39wwmRDuV4sawcHMqFexfnXUv2BUhRg5EArH1vln1UiQB_WzT1FLsZ06mXX1VKWZI3DtHXXXecm8Wydu-Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
دو ویدیو متفاوت و تامل برانگیز از کریستیانو رونالدو
🆚
لیونل مسی در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25182" target="_blank">📅 00:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25181">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqLULAavhrUy_H_4V66iU09nGMYPHAl8vKedvXJEnHlUt-SHVwMRmE0BubJp_2FR9DJuwlUjYcpWYHYcdy1IcN1arBFuW1_SsTF68yCLeHXZ2c2aWwkkKK1ZdG6KW9NvKkTC3kNFcZEQlPUrBWmqeAcPiz1951JqrTRo9u0a4bmumGsYepSMCKm_HYLr9Jwm-woTk_OqDWC1sh8bn_Fmr_wl_a0fOp624AMwYuuh7YDqArcnV09JQliy8CRVve9HM3RgCMQrkSUNacpiVSTpF7mv2nIq6taARW0JMEU_3h6Z7UA9_PKYhmsNPdVAL967ZKyZZGN8vMSGZnahEjOzFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی 2026؛ کامبک جنون آمیز و برگ ریزون یاران لئو مسی به جام در تنها 14 دقیقه؛ یاران محمد صلاح بازی دو بر صفر برده رو سه بر دو به یاران لیونل مسی واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25181" target="_blank">📅 00:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25180">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kf9DzDZCRMmyS6_H-9fJDlZqHRI9GBT7VP9hyde9wTqba_BXNshn_QK8oEZi6vS2kmfy6q3QbrsJie_DUYmvrMjNfiaW8wrWhj3i4LuG9lX-9o60sss7sMXFIL8-1piTN06q3YYBWNJvpnjwTouwe7MX2mD0PQpvtoGixSP1jLyAQhVdsuVBq8Gvmm4LMNdDUlOJKB0wx_3Xd8-jxmIZIKcJeNwcnKhZd7FW2fAgL_qn9m-uTgqBB7FcFd6KQ_1DgeqWOYAlWjfPIFlR_bQGVLWbuOq9CgXQTrjeWVD4sE-f5ufF7jLHLLMLQkX0Ctm15ewLYQnIbF-IVzH4inMTGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری #اختصاصی_پرشیانا؛ سیدابوالفضل جلالی دقایقی قبل‌ازطریق مدیربرنامه‌هایش به پیمان‌ حدادی مدیرعامل پرسپولیس خبرداده که فردا صبح برای عقد قرارداد وارد ساختمان باشگاه خواهد شد.
‼️
حالا بایستی‌صبرکرد و دید تاساعات اینده باشگاه استقلال برای تمدید قرارداد جلالی…</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25180" target="_blank">📅 00:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25179">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbSGgv1OisLyaL-c4K50TA6AswsEuAiW2CmJZ5vhYaYm3ykoeJVHLJob3Tf0e_sA9ewpDyaKJmNo7y5BO3qdfHRIcNFiZAXzDCqRMBFG9JMoCNrHJB_aVt40WKS8UavJ6SrJcjdPxfBn_iyxUaRlrP9lz9JWsdOu-OxI-vCpO3w3HGFo23-tZiC2r3orEwBp32P4VTcu4ECLVH3E8DGh8vDNzCPo-YlmVWvu9zdpT-Gtu-owAJED9f1NDNcf7XyP64CpkIdeFC-0gQbxRNR6uUITfaRSexfhdiF9KWywLVhg-Q8Rfjs-DXPsVY_hTKjm0ljvMj5PBrNcTGDk_2IXbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای باور نکردنی باشگاه پرسپولیس: دراگان اسکوچیچ برای یک‌فصل سه میلیون دلار میخواست. حالا این رو داشته باشید بزودی اومد ایران رقمش با سند منتشر میکنیم اگه بیشتر از 1.2 میلیون دلار بود کانال رو پاک میکنیم. فعلا دارن باهم مذاکره میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25179" target="_blank">📅 00:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25178">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNnja2zUgpTwTsqZZIXmBweH0KmbpA29ws2y0B5tWH7-LLfBHmYtseqq4ufhjcRzomZLcqtNsQ-KMW_no16qWbER7RlYo2bK0xnQkLClMdRG-Ulq2rdwCNQBd8x-p5JJjKQx9fJ0esIRGivpnvKwnGq1cymW88oRCc3zUE_JGsuLn3QaDQZuou9ocBmimnbqmSzLjme-Ut6-5IkGRSZm8xAbS8JS1-VO-gm7nO2cW-gfPLLQObDm6ksGPSGiRhXjb_-VWlxE6dkzM4vzWIY6egmxeb8AZD-kD7E3iBzdWKvbopR80of-CuPSEVQnhiRVxKnGarUEgsBuRVizXfed0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده جذاب و دیدنی امشب دو تیم آرژانتین
🆚
مصر در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25178" target="_blank">📅 00:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25176">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vG1O9IHfRqH1m3KYTS8F5wZasx-QJJmSQ83D5w5CLqwkHljK5UYoyjvaaXa4hEcy8SXbsqcMgaQ8pER_vbBMPvrcSVUXUKcUvFkRWsEMfpKIo6BkD37otcL94w9FAvox57R7uNivMumJqt6wtM3TdxMcfT50eLKXB2oR5MoOty-hN493XS1z8FKXmYBJ6fe0ft_wlSDJr4ScSbNbJi19y0fVTnaw9n3w29l-zohuxdso2VQYdj_njjKU2M3UmfiZJIJ9FFWzpFvRr19LsJo2diiL5OOc-SEY5BKoWm987pVL3gIVAbTF0MQ7UGSqCVDYnt2DC2ahs2tXN8LqP3L0yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا
#فوری
؛مدیران باشگاه اتحاد کلبا رقم رضایت نامه احمد نوراللهی هافبک 33 ساله خود را 800 هزار دلار اعلام کرده است. باشگاه پرسپولیس نوراللهی رو در آب نمک قربانی قرار داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25176" target="_blank">📅 23:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25175">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-HoRH8Ymce1kyCSMvu-IW2ULpS0eN182cKcSu9ow2ayN_08Eo8CYy2Daz4Qsb5Xviyvq1wD6eVh5RKgjgEZ5Tiwal2RCtK6ihRKWmLX2qZ4TXXtdqFnCT5byHeCiFad7-uL4-ie7jwsfoYxfsMX51xRzwocvSFXZ1mYJsGJKUrt56GIWh2o3Z1fGaho_wdSnXoci7D2OUYmZNjm8QDW76yvu5RrWcU3TSziA4wd2DsDfmdws5K-Dw4PkdplrN8bqgJwCRLOUgNTk-Yyk6FGKqZsDMj9MKWaMYNof2yOm1A-_kjKtevv_cKcxcB5Tiq8M54Cu9NxQR1EhH7NqmosBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌دهوک‌عراق به درخواست یحیی گل محمدی؛ با سینا اسدبیگی، حامد لک و محمدرضا سلیمانی سه بازیکن فصل گذشته فولاد وارد مذاکره شده‌اند تا درصورت توافقات نهایی این سه بازیکن با تجربه فصل آینده در لیگ برتر عراق به میدان بروند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25175" target="_blank">📅 23:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25174">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRkmNbGWPN9lOBBGosaXDSZmizVD7H6VatuUP353Pmnc6BbCNa78n3LmfQK9F4Rv9TrWzBLW2-FEX-esroiGaiZ2BBxFRUhDU_NX8dVAF-iApZ9XahtgzEsBnhclKlkIgSzfmuQJCjNmBdOPeRmp_DX3pOSsESQMq92DDpkwyGwY6GLNxKTDt9BHQet6llYQ26cD1SNpGtkAzsq67CWVX18VRAgUszkQI796dwH5IwcjVQ-ATzEsBAPNElPQ357H_dwp7JFe5_a_LGYlHvnJxucZ8y4EY0lsOYZZ5jIsrFBjn7B9lT57xPklD-BPUSCZ0ELW37Zk_1kbuNcfIE5p2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال به مدیربرنامه های یاسر آسانی اطلاع داده قصد داره که قبل از شروع فصل جدید لیگ قرارداد ستاره 30 ساله آبی‌ها رو تا سال 2030 تمدید کنه.
❌
آسانی آمادگی خود را برای انجام مذاکرات برای تمدید قرارداد بلند مدت خود به ایجنتش…</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25174" target="_blank">📅 23:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25173">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdTuiaboAa2tDSzxGglehTLvQlriAxgY628DWVHF1GaZBJalQw29eGeQtDj7p9MIHTycPTcWaf5KUNS9x2UtZLE86_Epur4Ahl_cdG17O1f5Flx4fBDrtKXQHeSWDXr3qtkxwppZSP_DxhlWvJ2CRY820uqe1UcG8pDx1dohYgLl9_EV95TlCTVR9vuA7tzVZGRHqid8_QCELR4c4rwgLZizE3i0r9mZ-yBNdEesVXIix7G3MDF739Y2JiOkpq20mtX0ufFRWJAqOTnqCrMq0z-Nfb-bxU6_5FmxL1lOPIhOmcr2gCInzssjOhI9hwpb1HCFVQ5-BQg_logC0Bx97A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده جذاب و دیدنی امشب دو تیم آرژانتین
🆚
مصر در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25173" target="_blank">📅 22:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25172">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNGeUeNHyiK7dBFlcChqdpp3-FtVbZ2CKMP4bjVOvrdjV8Ya2d2FaE58rIIoZN5xlnLZ1j3J_rdLeigxZdCkF6p9cm8kVmxAdDs4ZcVD6BaVrd1_GwoHnQc-epI8nzIm4pO1bw4LNVxOJL92jqgUzDyKpdNRudx-muCA7pHU4BZqKGoCMrHomyhUtwlI1AsUzKckiaAO8wxm_TO2hQBkZD1x32EJZgG0cxby6ukgwHl19xxAKktLC-pa9cY-v68BsJZNX2LTUKGdACLIxf0WkrSunbA-v9o0MLte9-Y9H7TRYNgQZmzIczp_3swJt_BchPFrnS5NTkmK0imeA5RRzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده جذاب و دیدنی امشب دو تیم آرژانتین
🆚
مصر در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25172" target="_blank">📅 22:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25171">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی 2026؛ کامبک جنون آمیز و برگ ریزون یاران لئو مسی به جام در تنها 14 دقیقه؛ یاران محمد صلاح بازی دو بر صفر برده رو سه بر دو به یاران لیونل مسی واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25171" target="_blank">📅 21:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25170">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mF3dV98mvJta8lNrItL98lHu7dgdodX4Ib3nsfAGWsC100VLKnCFmXZy541foSNcjtKRFKadoysg8_gVB0Y7mH1ACfZMbEx7EDqzXkU0gXxxOIsXKiZJ6rMWvzAR6eqvXY5ElPNRp2jCpjf-0K60Hfha3cQRk0KiuCH3r54_6pkyqP_xuzfQ_K4TasNDTnPbrObMaLXaD2Gux45QE9itCusOL-ci4mfO2jzsMS95uq36Y7TJKrJpfdcysaTONeM38_NudH9WfjwPvN1kFl05WhckKLFaDxoSGQSHqeRWPG25aldbWHBGQEf_7XFmwukZTQn_kXQNwng0kWUa22x1nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛ لیونل مسی که نیمه اول یک پنالتی خراب کرده بود در دقیقه 80 با یک سانتر دیدنی برای رومرو گل اول آرژانتین رو وارد دروازه مصر کرد. این دهمین پاس گل لئو مسی در تاریخ جام جهانی بود. لیونل مسی در دقیقه 83 گل دوم آرژانتین رو به ثمر رساند و بازی دو بر دو…</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25170" target="_blank">📅 21:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25169">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXirN6rZ-J3zAP30EaSqOVzUxUCOLl7lmycuKXGUsK57sbF52QxaQoftHd3n1zUtG68F8LpyFwSfmWFM5LvRrQ6R4GiTFWl7QE_7antMWKeL7cVSzB4cCAC8yAImZcBcavP5n73L586QDwhdjSEZ1FMIC4fcihWymE826AaQz9GsQJoE9Cg3kJ3Op3AAWILTlRN90s8e4OLjOtsAkugMbH7jTa4S1925QNcHimkA7jlsPBKRfhYPSjWLyE63Ql4z_RiJfXFWaJroQ_JWnEMOn8leLqSjTkDAGLeuUMlJPuvN4PnX3Hs_yVl45GQ_K-Jg2IUx3dQygu0RFudmLcnlgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
با پاس گلی که در بازی مقابل کیپ ورد داد؛ حالا لیونل مسی با 9 پاس گل عنوان بهترین پاسور تاریخ رقابت‌های جام جهانی رو از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25169" target="_blank">📅 21:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25168">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gup5FP_IDA3HFZ587AgWSBMrDS577B9XGLBLpoCuZKRc5pvGKhhkBc7CS68K974RV9UUexrvLjs363AJeGmUCW5WVQElP1VGbRWFpkL6DzS7_ksfV2__i54-q7UTQl1Gpoi8LMiMDJ-kUAXoaYEJwKS-5RvsrSwodJFyvUYty6m9zpIRA5nkpT8N9LivXyEt8Um_SxgHISQov19SRtB-uPfbm8dEgYfbe2uZfXSoZUacEUEYxrSf7AjyCqJUmR_Xq36giJQ2ubxDGT2_O99x75x-tmblc1C2sV8DXo00lkOO3-vpSvoqGZlR-jQ0-znFBaMo-5NMYKkFQn_K2x61Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ لیونل مسی که درتاریخ جام جهانی 8 پنالتی زده که 4 تاش رو خراب کرده. مسی به اولین بازیکن تاریخ‌تبدیل‌شد که دریک دوره جام جهانی دو ضربه پنالتی در جریان دو مسابقه از دست میدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25168" target="_blank">📅 21:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25167">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IcSWZVR94svTvWHcw8n-n-4hrnXi5IyrlECos_1XYH9Ixii5bZSstWzy3_NhTN2vHvTN6mQD1N2RMdNQVdrkTqCaMSOOTcJMpfH8Giz6bxpwUCPaQZlwpnOouua_95I3nOmT4RlZbl3ul5fJVUe71y8Se0CGSvmJVda_tqfoMQks7T5TBGq-MxiKXXz3sQzFxDDOAgSvphQ_gz5V8R8O3UOAxLP6GGcRh5qzegLmcHvhdEIBTvKpFD3HGi88FX1KlIioqfQnvxTBpI6rOfxdfs8wI9gojcyJgIrWX_I-_IHhq2VP8Bsg943oEFnSot_STJSegvB3LxXkKxv-liV7TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی ستاره‌آلبانیایی‌تیم استقلال: از لیگ‌ستاگان‌قطر دو پیشنهاد مالی بسیار بالا داشتم اما بخاطرعلاقه‌ام به‌استقلال و هواداران این تیم آن‌هارو رد کردم و فصل بعد نیز در استقلال خواهم ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25167" target="_blank">📅 20:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25166">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pUhfbng9xxv9xRHbqM9ratbGW2w-ZvlF8TfMfyWxA8eax_wGB4ZLI_Xcp1RwRRRSiriDANpzG4Xaz3kMiGsd4_rqCxeZNudwbjiKsJHBlT8FIYQi6lwp1AFXF9UcD-Jd_MwNsFNAn4c99WqGqdTMSp5AwkE-D_6bYIY3lO_Le9rl7bSPpE9U3G_wiASesf9RPwZT6KBMX7qEkelmlo8iEJ7XER6ZH0KnHVE1xIyv-BmXRt9LE1-dou3mGG4CqhiEXWsF7TRtuIlXyohZNkw1TEbbPm2v2hKfxvpFqO5cQsMgCf1u8IbwbAi2MIWWDcn1UuwK3aGvd6arC8da0EjkwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیگرسریال‌تاریخی «یوسف پیامبر» درگذشت؛
حمیدرضا دشتی، بازیگر نقش «بینگی کاهن معبد» در سریال «یوسف پیامبر» بر اثر ایست قلبی درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25166" target="_blank">📅 20:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25165">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/au0kbdYFJIlCjN6bPWoO5hMlBP-SAvNPNNzWK7uOCjhFFnubXbp2-k0tL5I1nxScKXln7-AYKVHUBDqoc5H0XFDw7EVmtJOnImc2ZdjclmK2o7S-YFOP11b-CZR3xLNrHVFo5Tdxc6QeAn7hdvCVVdDdRvFNN9bzH8MBD2Ke0tNgmy8J0PA7NvASlNeKGrGY7_VsZodWr7kXEjzAefQ7iLmHIncHi94UGk_s9jJBkWvZPxUC_Paffxcel-OFuKz_3mjOXAIB0VwiGmXO20VxntuX9BL9TXB-kdVjk9ndmIjWSF728KDFkXIyVC8n_RP9rSPSoBOp0UvYZGazJ7uOqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
پنالتی از دست‌رفته لیونل مسی در نیمه اول دیدار امشب دو تیم آرژانتین
🆚
مصر در جام جهانی و واکنش برگ ریزون اسپید یوتیوبر رونالدو فن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25165" target="_blank">📅 20:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25164">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/089d3fa449.mp4?token=ptPfkLacwm7d2GTV_2f43gGNfSGj00mZ-01XiVKoHjvlKwu8IDkDmHIch_FkY2HjxF-KWaPDoa4SrYETLHe2vn7Tj34opuwCMp5om-2DNM6Wp-P0SHMy1NyfFKHh2_be0g5TZ_bFUBQsRGiFuGhdfS0wz6wxNV2q4kag2U5pJsEJTLiR4PwNTbY_vWHz5o7Wbk383X9NVBFMGd4g_6Mrqxgi7Oq_ehqtTlchyVWjwf1W9maBQhYllslOLExB_qYXMOKwXAin7P0cG6L2VsByj2a2OztYroQPMuKvW5iAEqVyxHDjPwTCphwyUnA3uOuv4yveeVw-M9VnxxrWHIfF4BeAdaS7lBJKj14WeMV4Duu-dVpfKPV6Vequtd_61cahNS1MP-_rT2XJx-yCz-Jgvi0Hn5ikehR-l4N1zLnSCYxApUOoeGAnsex7iwiR17wsIwEXyUTh55OeVqKP0XLGyxTwSrQCj-Cvh-doP7jw9-Dh4epFZLPzj66w6CI9-fjeZIcOwrxUc9C8zPh5O09qz_0LHczPnNo-7WF0AbhJYOA0ltD6KysOx8vneska8FHPpMxvfN8D8DkwKRE1s_GIER1TJ9g2EeEtT25zs53OzUZZyk8XS3mzJZDU_OOzK0tl9VG-cmY57yPjoE6QrCAYyMw9ueQi4rvdL5d7WKa5q7s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/089d3fa449.mp4?token=ptPfkLacwm7d2GTV_2f43gGNfSGj00mZ-01XiVKoHjvlKwu8IDkDmHIch_FkY2HjxF-KWaPDoa4SrYETLHe2vn7Tj34opuwCMp5om-2DNM6Wp-P0SHMy1NyfFKHh2_be0g5TZ_bFUBQsRGiFuGhdfS0wz6wxNV2q4kag2U5pJsEJTLiR4PwNTbY_vWHz5o7Wbk383X9NVBFMGd4g_6Mrqxgi7Oq_ehqtTlchyVWjwf1W9maBQhYllslOLExB_qYXMOKwXAin7P0cG6L2VsByj2a2OztYroQPMuKvW5iAEqVyxHDjPwTCphwyUnA3uOuv4yveeVw-M9VnxxrWHIfF4BeAdaS7lBJKj14WeMV4Duu-dVpfKPV6Vequtd_61cahNS1MP-_rT2XJx-yCz-Jgvi0Hn5ikehR-l4N1zLnSCYxApUOoeGAnsex7iwiR17wsIwEXyUTh55OeVqKP0XLGyxTwSrQCj-Cvh-doP7jw9-Dh4epFZLPzj66w6CI9-fjeZIcOwrxUc9C8zPh5O09qz_0LHczPnNo-7WF0AbhJYOA0ltD6KysOx8vneska8FHPpMxvfN8D8DkwKRE1s_GIER1TJ9g2EeEtT25zs53OzUZZyk8XS3mzJZDU_OOzK0tl9VG-cmY57yPjoE6QrCAYyMw9ueQi4rvdL5d7WKa5q7s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
پنالتی از دست‌رفته لیونل مسی در نیمه اول دیدار امشب دو تیم آرژانتین
🆚
مصر در جام جهانی و واکنش برگ ریزون اسپید یوتیوبر رونالدو فن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25164" target="_blank">📅 20:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25163">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQ43dWKJfJfgAeXO09KUxY_JIyBmZNmIRCN7wpGjW0ekrW6MMdQeoQLpfgEP6rB-cLVliN5HRzYAb57gQ1Pub8Pa0wCffJ9LcNg1LpNDwzQGyCdO1H-ykzpKhIQNGFLYE4Moy9PvMlXZLqOiJCJxaJIpRGofhH4I3QEWE7Ulo0eIxg8dujMD_NdocSvmhwHrf_1JHPq1PE0OaL4gX452wdrxh-TfRKqyzPfrawk48N3YXvLewftoz-kLBPt1PLoJhQVuK5eO_xzTqzIij2QGQrh-en4Mdg6FU9AaQZ9uN-gXQqwb0jngh2FOLMLLeR-eal9hA66icuJauChEIzFTKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همان طور که دو ماه پیش نیز خبر دادیم؛ امید عالیشاه، مرتضی‌پورعلی‌گنجی، میلاد سرلک و سروش رفیعی درلیست مازاد مهدی تارتار قرار گرفته اند و به شکل قطعی از جمع سرخپوشان جدا خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25163" target="_blank">📅 19:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25162">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TsTIPjliWSnRF_di3ht6we3naeBxVFxbIy6XOFO7dX0dBOTUHI4hKTJvhzUJrrOoBnoZuZRp4j-tA0uZ6qaENP7M1Ja5dJ7dOWILRRCCaJ1bTchPhcecke5ekwM4w6gL0_lBtkkRuM_cZv1p86BNgtfmd-7efVNsO08v5F91WzoYLuPlWUs91BwFwdguOT3QEuUPlngR9F0uhue6Wh0bQ08cmhtGzUyzdS8Y9lavVmEvyD-j22mcM475nnMDyu3kVELDj7sh3DIy-lAgbPe1qxlPj5ELQ7zeuhoXNXJtdUzxcOtqrRnrl4DV_HN3I2B720RiooH-9xGrG15G5fWE3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مدیرعامل‌‌تیم‌ نساجی: برای‌جذب دانیال ایری از سپاهان، استقلال و پرسپولیس آفر بدستمون‌ رسیده اماتا این لحظه باهیچ باشگاهی به توافق نرسیده‌ایم. رقم دقیق رضایت نامه دانیال ایری رو به باشگاه‌های خواهان این بازیکن گفته‌ایم و هر باشگاهی اون مبلغ رو پرداخت‌ کنه…</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25162" target="_blank">📅 19:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25161">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOUhQo-f9R0m9WlixH_I7WUeKLf2Uz7f4EdtCawPvpL58HfxsbKdUwow3d-8rddmFF7MbyZy8l4pjiplUJfYQs9QA055u1onKuQKrtF1o_bEsdhfujysr-49r1U_saOepNbnlS7ug4RQdWqphbOQR4WVwpDHfs7a0oWXOmQs1Sz_Xa5NVsUjJuMeutbNn9B5J9LUtUI-WpamkMdg-51QvhWw2K-Vzfr5d9d1lCCmWvUikqyIji9SYASr-h9mhbT6YxvXkT8W_Rb8FNuuxpvyAGQqpyVz5cn0IrRLtOL9VCpcyB6VWyV3zB-PoZ-90hX3Y9pAp_E76-QiamzCWl334A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودارکامل‌مرحله حذفی جام جهانی 2026 بعد از صعود اسپانیا و بلژیک به جمع هشت تیم برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25161" target="_blank">📅 19:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25160">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2d97c61ff.mp4?token=NIKuIPzxulKQBu8PN1s7nxKcg1WhJHPKo0NhS5O-vCqZBSnIgFtJby-PbROnolovKY9n0j136hB7QA0osJQNPRxq5zkJSD-fRRFIPyeaOGJyD0-RLMToXC-4kZYG7xQYUd_Djt6VeQ9T7ZxXY259tNRG60HK3C43UkgIANUiWmVgl5JVNR8GHwOpoYMMlh_pav0O8GoXI-Dv-QZzCj_hZc00inqNSpffCaH9h7fDOTkHAqz-Ao6A6509ofRMLDUTtpg4IP3HF2uCanwInmZQQnWZofDW_ozm6eqDPDIDW9_xg64X7YwUSn1c406PsJPn1CjRtFiMHJEx56isHgbQng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2d97c61ff.mp4?token=NIKuIPzxulKQBu8PN1s7nxKcg1WhJHPKo0NhS5O-vCqZBSnIgFtJby-PbROnolovKY9n0j136hB7QA0osJQNPRxq5zkJSD-fRRFIPyeaOGJyD0-RLMToXC-4kZYG7xQYUd_Djt6VeQ9T7ZxXY259tNRG60HK3C43UkgIANUiWmVgl5JVNR8GHwOpoYMMlh_pav0O8GoXI-Dv-QZzCj_hZc00inqNSpffCaH9h7fDOTkHAqz-Ao6A6509ofRMLDUTtpg4IP3HF2uCanwInmZQQnWZofDW_ozm6eqDPDIDW9_xg64X7YwUSn1c406PsJPn1CjRtFiMHJEx56isHgbQng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت‌شب‌گذشته فن‌های کریس رونالدو بعد از شکست تلخ مقابل تیم ملی اسپانیا در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25160" target="_blank">📅 18:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25159">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99da3bbab0.mp4?token=D9N3ey_rKvQ66V1Dg4FB4A_a8RjBOn8H5wxLbgxOSv_wiMFPtF2aUGqKm22hZuh6pR-2a-yZqhcE53vgE_uBeE9eiEVOb_REBD-WXWq2OPZq4M3eRGksFafG2bgHX4SJ-QJLsqPmGzHulciNbJmVn8_NG9nuB6Y3VZk-T4stYM2WY2KWEV4sVW0jf-TCVLjQe7lZF8BFRIjuZu6pEc_hvvn-hlQuXfy3oDcf1u4tHDMi6vXibjGnQYGh0DMtB17KDbq1Il71mtov7wvjT2SIxDHXne7eGI5b2-51sceEFG7fZvzDyAgaa8Ude892QvuaWIc-kKulqfJOrdnl6PjiAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99da3bbab0.mp4?token=D9N3ey_rKvQ66V1Dg4FB4A_a8RjBOn8H5wxLbgxOSv_wiMFPtF2aUGqKm22hZuh6pR-2a-yZqhcE53vgE_uBeE9eiEVOb_REBD-WXWq2OPZq4M3eRGksFafG2bgHX4SJ-QJLsqPmGzHulciNbJmVn8_NG9nuB6Y3VZk-T4stYM2WY2KWEV4sVW0jf-TCVLjQe7lZF8BFRIjuZu6pEc_hvvn-hlQuXfy3oDcf1u4tHDMi6vXibjGnQYGh0DMtB17KDbq1Il71mtov7wvjT2SIxDHXne7eGI5b2-51sceEFG7fZvzDyAgaa8Ude892QvuaWIc-kKulqfJOrdnl6PjiAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت‌شب‌گذشته فن‌های کریس رونالدو بعد از شکست تلخ مقابل تیم ملی اسپانیا در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25159" target="_blank">📅 18:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25157">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iKp8hIYy0x-3N6rQEhsv3z2FRrydi3QHXo6AUMwf4-j-5zPLMw7T6693VUV-f8yWe6k7e9EBLQf_JJ0RfkTE8BRPlQC92XcW62RpRWuh02Z3lMNKMtweX_CiaT_k90wR4Fh8m_YedKup6Tggs1keyR08XgH-XNlkDBqpByfKlXwZLUmWgpkyjay0PjRTkDx0FO73_hiyVjIuiSVZbxd4RzOjTDivguyDjaoMrJXZGK2u87ikVU9emOWPcJ6hGylvWeoK1fBEu9vdCigyj5YBYDJ5nhKqM0eO90Idmm2gXsSuiw376QguouSbJ3S6yVUILSDYTAPk9LPQT-9pqK-ypA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oed_M3nWs_pOQsgi6tlwyZUGvqzjKG01z0VQAnA-s72EOJE9M8algUeMZtIG4-HQ4cw3V4QoVCeJ0whyANSbcjf4vlnWye3ZdwUYIfPrOji-F-cH77PRdLFJlPhMzeM3qm7hQVdeIaUcYJMCdZoMnM8TI_q94jYcaoUTQiJ25N6sNlPSyfMfNh_BUpy5p5cujFBKA0zBaqN7q2eLrT5O234ZtU6xv3DujxnYIU0gqwn0Xvwa8kLtH6w35UhlegSq-1VKO2DnvFsnAOwNc6FuftjuCbULz1ORJZjNztMfWnneNcPrwCoktXF6HMBjQkxMljfFCtL1pQrXtiIz7lvuFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نتایج کامل دیدارهای مرحله ⅛ نهایی+برنامه دو دیدار باقی‌مونده این مرحله از رقابت‌های‌جام‌جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25157" target="_blank">📅 18:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25156">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sv_a2tp6r5nfuJMy0JanJH0LyjCyPLKdcgXbG4pmWUaozdrsC0Z7Y9__0tO3Pt2SFrWnj4KYkQmCqwWpWA7GCGalNpShKKLJdZeW-77gGG_8fDbKDRiPQfVvM4F_9B6Dtr_nZsrc2Biq4O26VxEww9_vO_YFLzY_2K8Y5EZjW-tEW8m2gsJ_bTNNzFzu5HApIJgigqJIX-Ou_XQ6qSp1RG6aXBFwJfiM_ajrO4jM4XHOLcQk0ZKVWwRfulLqyCzxqoa_6EvEc3DCZOL5ugNydgbKNz7C9wb85hplg9cZeFc-qUYlZDoQcyNKlvlHB959Xfzr_WMnv1XavkaMkI0tCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه پرسپولیس باارسال‌ایمیلی به باشگاه ملوان انزالی خواستار جذب فرهان حعفری هافبک تهاجمی 20 ساله این تیم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/25156" target="_blank">📅 18:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25155">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K11_IfTvBWmv_us2tIeQYZdmnMUghHZCAHKqgrXHC4l-CeiDgXH3oEeH3jFVWxUelS4k2_X_vhyXbHXEDKDSWSlfHl3p1sHV5NGrXwhRcoD3PJxiB6dnBFfSecKGphCpooUmH8I-hgqYEcFH_r3xjql02JGVFWG21feEJaU-pmzFOtad9J7fF8sf1ItdHyHy7NOYfr1k6lJovAYs9hjFnEKiceYTdobBf01GwpeTvobvtax9-Yl4gsopNfb4FshNmVJFGwz4b1UkRUjPMQjsCkK-Mof78qeJimEJQda5enFQUqMsCBqO9hwtzRcTtsGJZqIdJd5hUNAlhBf4HLExKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
👤
#اختصاصی_پرشیانا #فوری؛ طبق جدیدترین‌اخباردریافتی‌رسانه پرشیانا ساکر؛ محمد قربانی ستاره23ساله‌الوحده امارات ازطریق نزدیکان خود درباشگاه پرسپولیس اعلام‌کرده درصورتیکه این باشگاه بتواند بر سر رقم رضایت نامه با اماراتی‌ها به توافق برسد حاضر است به این تیم…</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25155" target="_blank">📅 17:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25154">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJ-M_GTnDsWtUkoS8Zww7rGhA5j9qJKdgzKkOwedymgtypZ7HkanoKATISQYSpUgZ87GMGh6uKmModETNPkpp4r6_CAYuo6G2c4Beu5Iq9EyPQVw9JmpxPzxbtdpiq0TXhNfMYDzyyV7af0mRJjdAqCVHVgEQiWSuzsrcB6bIvO21oebqy5NxTIT-jXRgrWOG-8K3dNev2PJO0bj1KZVHP1f0VX4x5JtLy0NoLDeCwKBtoV7etrRXYRvuQUYS8s2Sp4kOnN30asqPCPnIup3dv4DJ7RSsuMH6XBzdmdGI6bBl1sZYfNzUXylhvJZ2UwQi0sVjetekCyhAN3aH4Z62Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/25154" target="_blank">📅 17:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25153">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tz4NRIHN6o2hBPq4vns2mDxjqZcPKbxrFdlRFnqTHLa4wk5moWOcA_ifwn_ZJ2S8Jjnxx3zyNA8NfV_zF-7pQ0ah197jgZB_WjPFmmCzMEiBe1Ovoen95LIZaui3y0orfPgnZCMmHhoEHzrloLDZ2aUGEbLxPYqiWfnfxE1TbNDLKqmljIwe54I5QvexindxQvn3pghDm0BkupEVsDnMO0rxhI3ozgfbJ2xPdoCsG6Q_DdPlho6pfWLC5O7Dtz58siz0DHzS8uPO9m4UTSX12NvX_eCIaLlJZRnaGz4mJcK1sOLG-sNyrY2Aupu3i50Q-Pc0jU9vMaBukP6rYKNJgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛ ازجدال‌شاگردان پوچتینو برابر بلژیک تادوئل‌تماشایی یاران لئو مسی
🆚
صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/25153" target="_blank">📅 17:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25152">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWtFbo1GV6bW-qPLaZ1ra_j8lmhGrx_HQFv5J6m1id0W56Li1VAiFzww3eJ9Xe_ZaI2cHxtESna9usvttVdYGZE1a7c-wkpxwfoyRxv8jyNWR1VFxxQp6mx4XhPjoIXvFfbo3h0QIqSykv6EjzR0KbVR4j1bWj2Bxsge3DlpsYIGyXHiH5vUigaWJ8R87CR_tpbF3-yG2GrpLNlP0t9zq3QtDNBu-OLIolQa-s_lruH8_IxwR7NWKgTVFmJqc4kukBnk-getQuEEcOd1dNZYaZKbBZZQuNzjvvDcPAOY8GDLFaQzXtM-kt4Ty58aeo6vhWrophmvJU0cuP1piWI6VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا
#فوری
؛ امیررضا رفیعی سنگربان24ساله‌پرسپولیس مذاکرات‌خود را با باشگاه تراکتور آغاز کرده تا درصورت توافق‌نهایی بین طرفین با عقد قراردادی سه ساله راهی این تیم شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/persiana_Soccer/25152" target="_blank">📅 17:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25151">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMvuZ7I-yJKNg21oSCRcuJEnZBPgxTsXYG90TpcHfH08-vRGs7lLzHR4PqrFZFKHW2TIidL8LfUQA0jMy7jHD60vSTA3agIgjEmzu5pzUqnpR3Q6CNZ5lQYzI6fftBunaQbI2k7xZlFOQg-K0qPL0SlZBCwkk_lk9gG3hRLSmFXNsKZK7gLIagAasOlTNaSDRahpmr9rgplxmE4ygEz-bBfkdaOjkm5By9KMTEiy9X9UJ8ziQieQcvHIcMHecuPtwESkGkI9X8QcWWp9Jw6JecGmne3VSI3iGjKtj_BzFngb6IGN4ZJdtz8NzJ5zG5mqV6oiFEnvn75cAdl_TV4jRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
👤
#تکمیلی؛باشگاه‌پرسپولیس قصد داره که یه بار دیگه برای‌جذب محمد قربانی یا احمد نوراللهی تلاش خود را بکنه و به زودی با ارسال نامه‌ای رسمی به باشگاه الوحده‌امارات و اتحادکلبا خواستار شرایط جذب این دوستاره ایرانی این دو باشگاه خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/persiana_Soccer/25151" target="_blank">📅 16:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25150">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k40D53IAbrobtHMGGdlDDMs8HncVwo-Wf1d-ohMBnbKR2pZqTv_4B5RUb-tD-2qLsN9atnzz7oBYKgXAqPICK_HmA7V0M6DuSrpQZv3R3wlRO25NF59aiLvJXY1usKLL348kmy3rhw-6tjxWebBcLLbA9Z7tdsZ30DAeCsPJ3q8Kl__fny7A9GUg8mE1RNPxLFJEMEEqwLey21ZPu1ynAnaciozBMsL_iu4TCS4VTewZAWGJdL-drUDLu0-GbfSthIvWhZOl1qLXd3zIrh6Dga8aFfKQVAJn5HW5fLI6_HM0xw2_oGTsZkRpGpc2Dpcdm62Q-vklL73k_owSd1_QZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
همانطور که دقایقی قبل در کانال دوم پرشیانا هم گفتیم؛ مدیربرنامه‌های ابوالفضل جلالی شب گذشته مذاکرات‌مثبتی رو با پیمان حدادی برای انتقال ابوالفضل جلالی به جمع سرخپوشان پایتخت انجام داده اما به عقدقرارداد منجر نشده است.
🔴
نکته‌مهم‌اینجاس؛ حدادی به‌ایجنت…</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/persiana_Soccer/25150" target="_blank">📅 16:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25149">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkwaLKq2lnVIGX4HHjQODDRpsQvp0wKOS8KmE7HiNlwRnojgEFhe6PGA3JhmA_fbitwcq-khba7j1ey4ND2SKPLZJZxyX6_Fqr6cbcBJ7QQ7nalaLfrSE-u1BEGwL5Hh2gA3zh6q7fk-m6s4Ec8e-1bSKiGv8S4ud4cVdw1mWfq-daivs8gub8V2SyDYOzKr1EULuY4ytwfWv_lcHusEgjJfDgsLHrmNis7oZc3lia3h9rFX4UHsbNXMNgY0KjabyD4ZH3u3ztCFfB3OE2-EkXHOYakcRaJEQ1ERC_jroZbQaGvs9Be00XBvQdpjReK2sFet7_-yVsH_c3sd0OHEnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
امیرهوشنگ‌سعادتی ایجنت ابوالفضل جلالی با باشگاه پرسپولیس مذاکرات‌مثبتی داشته و احتمال اینکه ابوالفضل‌جلالی‌مدافع چپ 28 ساله استقلال با عقد قراردادی سه ساله به پرسپولیس بپیونده زیاده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25149" target="_blank">📅 16:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25148">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2fSOkodyn5a59pswIjEA-u0sYx-lxWSffWtfUF8yEeYkUhUnsMdM7fT1afvlKDZ06-GcPlP9msNjutKlpt1eOz-BROa1q2CMi8VHnFMNlieAf9jYQbJJxI9rR7Q6O3cYTfwIMbVEW_ja8x1bhNJjkSV47Mt2MrQ0fUk_AZtYZG3Ky4D7XzpGPVYZA1IbUfhBp4h5Uk1H3FeHmBZaqLO5h3_2VpqCE5KjzBWkP6BTd90q_ecSZmKu-r7dBCVKgRTZ1UaUmQRj3vLdn17N7g_gQr5LA7cEYWG31zI4-a81kUB3kGkZzMhq3uPpCZUe5ccCX9rixaW7tiIsIEIABuKhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
ستاره الجزایری فصل قبل تیم بانوان الاهلی عربستان که بهترین‌بازیکن این تیم شناخته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25148" target="_blank">📅 16:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25147">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UtQDA24GrOVcxvz-sePrsHFHzP15QZGCtj8HuqnUVj1d0p-h00rjGRKqkWxuykjEZd-e48bx8URcJAVwCuVb_hGi1AhiTYcBy8vLJAUWPdB258sUF0fs2IWNugSq215VgGKW3B98r72uNhkqM8oQXb3CVR5CUtVIUky-OcSR_kY5Kc8u_pIDdYUz4YWbBnHtec8k0ojLAqclMgI3wplpQvETxexfDiSyainzkrFbXd1N22jgpbh03kBoeIsy51-nDS8GcHzMzPee1rlKn_h4G8-O8bmrihUJPlURbLUEiQeZQLthW54VKQJgHSdeWWUPb_AqQaTF1mKJUYewTTPVvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25147" target="_blank">📅 16:05 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
