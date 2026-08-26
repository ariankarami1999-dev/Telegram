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
<img src="https://cdn4.telesco.pe/file/XjeLtBYYcbukWyZxQEsOZrPo92up8E-43-Y4Ed_F5q82qrJ4E7vmMjm7oBKaFmr8uj5Cd0f9f96N5vnVy7GrRV8mt1-gryKsEJ7GY_-uX4n54NV5rlN1xGO6Yxjcz5JcXPJPIhchfsjMjGqv6jdPhDv-Fgk198m3IqV5QjpWqdWTViIpqt5PC6CxKBauPuCCLi4CIC8i0214k-jv82m4ZcDxhNBPFegq3r3cDDqNImvS7zfO4HesJ9KoTHmiMohJN2fdCMztfmQAvreKB3XZlOmzuZAz95AEdALqFXtna_oMl0Nck-YtMxH2Yv2Zp9nOdlOiJJXzar7LFeZvGMAMsA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 624K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-04 15:00:30</div>
<hr>

<div class="tg-post" id="msg-28521">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOzANpcasWpaDtG07eMpwY0QQbiXkczGsNXXCEY2aHAK5rwYWyQr_BsuQYo0SGqCXS6onmPSkK-dYdktXSr_NXUSAGOaO5x8oAd9Td-Vc_mlDQ3DffjOqBUXU0WYfWz27gp8LlZuxkxcEY5FVkFkEfz8ayyqTLwATEAuVIdxAwXQEevXlgxfuknFc9QdqMMe24KoV9NdvbyjcT_if_pLA1e9DrxSYW7XBDkrhINM68yNRDVADflos6KdRAgmpRSOdLvu8H5VnK95GIX4xDzXUjh7roo6jReBzY0Lqn1punff7sw7j0_vdqktt6DV2Dj4LPFWAnWbFBsSupoq5bRfNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درحاشیه‌دیدارهای‌این‌هفته لیگ‌عراق؛
یه بازیکن عراقی بعدگلزنی‌واسه‌تیمش لباسشو در آورد و دویید سمت جایگاه تماشاگرا تاباهاشون خوشحالی کنه ولی هیچ تماشاگری تو جایگاه نبود، بعدشم که برگشت به زمین‌گلش ردشد و بخاطر درآوردن لباسش کارت زرد دوم هم گرفت و از زمین مسابقه هم اخراج شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/persiana_Soccer/28521" target="_blank">📅 14:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28520">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8oTVhY6uLsn-HVeLuHRZA61VbUTC_4I02wYP4LE8S2TqXZ-o0rNeGBDED_cI6MfIzQn7xgBmSVVDFppze2WxYI_m_bGM6WPAhEVavnBZSEK6EZIghHwN8MxlXbCsCfT6MV2Q59ir1Hw2uL-0DkcWVgnKYbcdT01IBQ37j_THUrbEHCxIyc3QNIXR5L5UxKvrNJAzOvkgB6h_gZJKOnIbdBCTvfZbFYxzHAWLQ1OKN83Kz_MJdK7OiG2kOY6wyVmvZyov8FwCfSYpc2GQyUvnsvPfLU3tuw10QxiT7fALM4JP7qAkvvFdGtwvdYmTwbn9o8u0Z1YoGIA2Y2uajkqQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رامین رضاییان ستاره 36 ساله‌فولاد از هواداران این تیم خواست که دربازی روز جمعه مقابل استقلال کل ورزشگاه فولادآرنا روپر کنند و از مدیریت باشگاه فولاد نیز خواست که بلیط فروشی رو رایگان کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/28520" target="_blank">📅 14:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28519">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTqvw8m0_mpT1dSX8YNQM2lTFAy6GEHHI_f3qmyB1oJxPFpyygW0-LS_QfvmmRYeDKjCxvuYuIwrETtR71gsqMERgeoTKb-UndQVUgxAu8iQBw4U3TJn45_zmxkNaSMeHeGRijCYHjB1DZFvnOW55MKmE9GitdmUoC-FHxNsFLbNjSKbOUqLd50-WKCd7JE4Ti2WR2Xss64IW_4OeA6fKw1zmBIYbu2eUcE3aAox6pfusyDvWLdQLZ8FCkh2UC9rmk_LF1pFqcJbAx5PokLFuK5WLrK44wWeBuAaiGYBHzOAXZfQrUIftAkMqWCKGhDDFrTQJQjH0kN2XDoXfr20Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دولت دو کشور آمریکا و امارات براش ویزا صادر نکردند و مسابقات‌جهانی‌مستر المپیا رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/persiana_Soccer/28519" target="_blank">📅 14:14 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28518">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bU3y_jKePIQ3xA2X7xzzx81zeAgRL1pBXztBgEOyS25oaIlQUp8jpHS74CZ0d80-wTMn1zO-WtiO3eD_5cf0GynKbB9WiXSxZno89a8RMzJTGXLBx7LsBcOFT9bmsLbvk5AkSG-hhtIt7fwNIA_WcPjjS8PnA6UvOkfPGXyhe-waO9YQMDNGqqn_pnHyymVkBnvvVD9w0mFDymude0DyBtXe4C27GZeYQQFUbYVuBn_SL8yaWvAmvWFqXAwl9xDm3scOhVFug95gbT8oBJkUIh_3q2XkdoEOdQyELGcXXsGqvTnpOi_5olxq23x6h4yqBqzf3RYdl7p6KQ-hGp0NKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇲🇦
سانتی‌آئونا: ایوب بوعدی ستاره‌مراکشی لیل درآستانه‌عقدقرارداد پنج ساله با منچستر سیتی قرار دارد. توافقات بین دو باشگاه در حال نهایی شدنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/28518" target="_blank">📅 14:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28516">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a17541dbb.mp4?token=j071qAeLj9wTbIylzb17uaiZsWTENLZmEoJGWQzPS0TbEzRCa-TgxRt3Oz6sg_B9AdhOLH-NDsTm329uCb4VrM6sbWolxkCTY16MsipTYsjE1urmuhKnDeisVSAKGTzWfUw0bTe9rOxW23snHZQ7MjL_07NgGwzcDK_Wjm21rgtPJjNQY2MHfvQ4wB2NugZfzqT6xYPBFwHnhcddLCFwPRDU5_Gc69KdzwqQCWC3Byx7GbIizGeQCaYcW60pPmRZc_xpPmVTU29vOJKYEVpx0izzoED6QoPf7qfe8z-1rxGib-qMQq02OOZgifKROSV6wbGlirFOIDl4A6RUY0vijDWqwqI3gj2yc0IfEJRq0sL12BYwx0iwtRkwmCYoEvjLvvAW-b7JqeU6PzyFBlA6igqL5nOJznKQr22L3uaE3NSTa5tX6x--Fwf0H2pUeCV4epw2gMnGEi6e8hjeDlTOG6UCFTdP171CSSjgvLYG03TPyrF4BFk902Ta96DET5gOuth3GOXVXdY8Hkqy0aXNZD8GGn1v5_0tyCnWPw_cYi-p5FKNQNtrjxaYwuWf_ddA7lkezxHEUdr3rOCkppfd1fsVxhCs4ZkpKjw_o7x4W_T0-4dU48vkCy7-glmTxlbj7sdgb9f58VL0EFsYJH1b_3idwHHbbBB9guCfdqf0WRo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a17541dbb.mp4?token=j071qAeLj9wTbIylzb17uaiZsWTENLZmEoJGWQzPS0TbEzRCa-TgxRt3Oz6sg_B9AdhOLH-NDsTm329uCb4VrM6sbWolxkCTY16MsipTYsjE1urmuhKnDeisVSAKGTzWfUw0bTe9rOxW23snHZQ7MjL_07NgGwzcDK_Wjm21rgtPJjNQY2MHfvQ4wB2NugZfzqT6xYPBFwHnhcddLCFwPRDU5_Gc69KdzwqQCWC3Byx7GbIizGeQCaYcW60pPmRZc_xpPmVTU29vOJKYEVpx0izzoED6QoPf7qfe8z-1rxGib-qMQq02OOZgifKROSV6wbGlirFOIDl4A6RUY0vijDWqwqI3gj2yc0IfEJRq0sL12BYwx0iwtRkwmCYoEvjLvvAW-b7JqeU6PzyFBlA6igqL5nOJznKQr22L3uaE3NSTa5tX6x--Fwf0H2pUeCV4epw2gMnGEi6e8hjeDlTOG6UCFTdP171CSSjgvLYG03TPyrF4BFk902Ta96DET5gOuth3GOXVXdY8Hkqy0aXNZD8GGn1v5_0tyCnWPw_cYi-p5FKNQNtrjxaYwuWf_ddA7lkezxHEUdr3rOCkppfd1fsVxhCs4ZkpKjw_o7x4W_T0-4dU48vkCy7-glmTxlbj7sdgb9f58VL0EFsYJH1b_3idwHHbbBB9guCfdqf0WRo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تقلید فوق العاده صدای گزارشگرهای فوتبال ایران همراه با نظر خود گزارشگرها درباره تقلید صداشون. جفت ویدیوها عالین حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/persiana_Soccer/28516" target="_blank">📅 13:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28515">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tT__dp-f914Wj0epxOkxe7tFTQxtSaJ_KuFrIeREHxF2GmpJ39YFnLjfPEXZm4IcJFH7DLR4vooT6V1JLOsHCJq6gNS9axZhKH5sGcwc8FNli4hmN-gPFPsPKS3IymPGReEgxzQqyPxTRYK-0TEjse9JwaTf9turxC5B7xoKDuib1GBw6RIqdgZHNUIAOoB9N2iv3IftM4aKhmUO-_NDqzTBbmunRxeUGlbjFkFdFxSVs2_RfrXcPH3RMgOJ74COXzM4NKtrj2qPpMqxFnf7ZBh2-mpgsK74KVIHDIJ2Ty6M2J2IhCa2fQF_UelRTTsFZRS8AxTnuWVS8Nq2qzk2ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
النصر دیروز درهفته‌سوم لیگ عربستان درحالی تونست سه امتیاز شییرین این دیدار رو بگیره که از دقیقه 12 بازی10 نفره‌شد و دو هیچ‌از حریف عقب بود اما در نهایت با درخشش مانع سه بر دو برد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/persiana_Soccer/28515" target="_blank">📅 13:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28514">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bpPihQYC4vZxbtRnfLHeoYUEmV94zZchBiyhaLSWVYiITrLv5qqY-ayAleXPX8Av1RyoJNZE4QtW_pDX58-EjhpatiDE7XVtXVPSZ4mW-chUelp6lxQEtOv8G1Z-ESXQ7AJQzySHhqz44UsHaL2BkyZbcfHj_N2bWP4IT2V0aRadzEZBMsLmEWDQhVg-xZCq4f8hT6YMssKjDXF5fwg6tYE-FsUOk6KmoMw803mx6FJUB89KbWHNiLDYz-KZTXRO-EEroTxLA16I0eY0AwRONILeFrj5xX19kaDXAs_zwdcjwvFND0bUY4Yt5F2_4z1M5LPMIsyetIiurI4fPIdBwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/persiana_Soccer/28514" target="_blank">📅 13:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28511">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o29H2HI29GgM0P7rfBiOaSCSZ4_eu59mklRMzmV7VZUSuO-a9fzeRXxe65rKM6GHGXu_adx-8sjeoHe5MhVMTNgeRBdtx3ue4AEcnIBquktDbwt_ytu76x-uwbZuXar7MwL2xgMwAbunrH-CYRFBbWYloRjGInZoYAPq4921QVUH0dGelkXkj5Ii7xlNkB3D85fHjVOdobCLGPIrdKwIxyrtCQxIlsfynCiCzwkBfh50o2v-0IGFDSfIW-NjzOHbQ46e9Useo_KZyOQFh9uAMiboLfQQus_JeMi9YPrD-8upjMZSa4xsMX-s7jSjQG40FnO_CtDuyRcLiPuqBsGe-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قلعه‌نویی‌قبل‌از دریافت‌پول‌های هنگفت
🆚
قلعه نویی بعد از دریافت پول‌های هنگفت از دولت! شاید شما فراموش‌کرده‌باشین ولی‌تاریخ که الزایمر نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/28511" target="_blank">📅 12:58 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28510">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ua5uGqLxich7OHRgQxA3-S_S9PUNCPwPxqrTcNusE9V2-7zFCVtZHQ-MaITmGsz5WA0w68XhSIBlCYfzAAjtsujsjcTaxSrG1shImyekMN5A_a5vsFXZedgntqbQkW7lqQyIEfpWM02bjnQomg4_sHInnpF5vePYmqKvNc8EzMpexzbpCdNH1x_zU039AQpkJN5AOWBdU53drjd16QFF-Umrlgmc0zGIXjT4NPeqhwD8gyqKzBmSxfh_qNqYHReli5pByQ5va79ajFePh8iwaUWvbvRCjYtzs8dD_c6CSG7AlgsKTsc5AJ-52TRbVrsTALP5QfD0fEeC2QF-QikOkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نشریه اسپورت: باشگاه اتلتیکو مادرید آمادست که خولیان آلوارز رو با دریافت 150 میلیون یورو به تیم‌آرسنال‌بده و توپچی‌هاهم برای پرداخت این رقم اعلام آمادگی کرده‌اند و حالافقط‌رضایت الوارز باقی مونده. سران اتلتیکومادرید به آلوارز گفته اند تو رو به هر تیمی که…</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/28510" target="_blank">📅 12:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28509">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5DkAHsLrPWhzu3359zuaHS55clGAXj775FhcCSYLtf5GdYwsSBvx9eg2TZa_32dYww6GEgxQMfhonBbRGMU-RasjEUqtaXmX-eOVQnS4ZI5B8VTZPargESzIEIhGHFr1AYIaqqTIvkYFOEZntpNVrRPVZUOTW6Xky39UzGdf9oCZfEEO5m3egjV9Vkmceezuhwk7pN-9E-piQ8yqsYHBBzN06Q3hjPzTvLYlukH531TKq0WUXXf8Dezb1evckZcHbeosi0wzZshY6inXc83vIX2JV1kPjPDInDwYYZTk-gJObFY6lCei4hhPwGOzvkc1EhLv64YSxO9yUjXe74NIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌پزشکان پرسپولیس؛ ابوالفضل جلالی مدافع چپ پرسپولیس به دلیل مصدومیت از ناحیه کشاله ران 4 الی 6 هفته دوراز میادین خواهدبود و دیدار با دوتیم تراکتور و استقلال رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/28509" target="_blank">📅 12:12 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28508">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okoLGpYMU_gRhVfnDQWzirYfAwl7FZJpgi2D47OEnDrDoJia_DYx0PzT3Ad9mB7pBxcociGiU6wEKnOGL1YzF78fe4SNcTrYNAqrmqnQKGCg0vUu1raCm551FzfIzt4ZygG1XJf1xLYeWDQq1vKeFBesJTxfiYeaeYze7MkjZ0yE2Nn0L_uZrpUHNQKKcj4uze2gtwU3imy8nG53N4gWioTvGbsn__-ZSVHd_Qf6QWdBvODzRyzMyALXloWCP66E-8WnDQ0GaTZL7CjK02b8s2LpTKraGVJaCd52ieTEsLLQqyA_fTS-kADpHqFJCfUW0ZMGR347_IeFrSGNB3dfaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگار کوپه:
آدمای داخل باشگاه میگن که تو خیلی ریلکس و آروم هستی. مورینیو: عه؟ پس تو یه منبع داخل باشگاه داری. خوب شد که بهم گفتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/28508" target="_blank">📅 11:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28507">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/099bc5af8b.mp4?token=BSe6eIW-qYb5RPxXdz7O7M6XJV_VUu68Aj8aXdVuMcWGBVXzGzRA3ZJiZNtPXtkpD3bNr-gKCa6hB_WRnrWmci6xBt-xMruqp7KRcdpOIRxAhPhNv6VCDUMYzXIBMqv8WofFTUKSb0zaHOiLCbO-04p7XpsUOjBEEaU2A7XMTCmE9qOf6FnH6B1YbbOhQy7PK8ytwvNvi8YmjQowyktvMTFi5CDwo0Bng_0JCC8mGXnX2iJ2KBFnvBYzhEFMMcAWUZvRuqzbHnCvaDGTBr99XjdA6QTuILqrTK57WLKtsvc8nUOPEcIVz5QjuDtZV4ktkUq6IWejTdKdL7kx7aak_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/099bc5af8b.mp4?token=BSe6eIW-qYb5RPxXdz7O7M6XJV_VUu68Aj8aXdVuMcWGBVXzGzRA3ZJiZNtPXtkpD3bNr-gKCa6hB_WRnrWmci6xBt-xMruqp7KRcdpOIRxAhPhNv6VCDUMYzXIBMqv8WofFTUKSb0zaHOiLCbO-04p7XpsUOjBEEaU2A7XMTCmE9qOf6FnH6B1YbbOhQy7PK8ytwvNvi8YmjQowyktvMTFi5CDwo0Bng_0JCC8mGXnX2iJ2KBFnvBYzhEFMMcAWUZvRuqzbHnCvaDGTBr99XjdA6QTuILqrTK57WLKtsvc8nUOPEcIVz5QjuDtZV4ktkUq6IWejTdKdL7kx7aak_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
گل‌های دیدار فوق‌العاده تماشایی و مهیج امشب دو‌تیم چلسی
🆚
فولام درهفته‌اول لیگ برتر انگلیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/28507" target="_blank">📅 11:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28506">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-mMkNxyse1oouyD1PaOxJUJd24-ZBtlrE9WsQZ9dqpxehn7fVjq3ccDhkpos0LIQhHxS5NttOSFPfN5VehmxycDPJrry95dlyLCWD9-vrPvdDgOXO1YRQsWvp-M2M4ErCV77HeU6BedSElSLVD82-GAeUlokNe_HjEc_Uwf7nrcU_9VRcPRW85zsigOfEyIRkobW9MjSrXoxbJnTbBgEwTExjpKFo1jgYOO-x_9wCcilb_wTsD9_3IrzON-BTbIb8zFSuSFd_MRmSyQXDxZhr5jpT65R32nR94BjE-npNrd75MksGX30lLxurqEVFKItNJYdvJSrd2AbVfovPKYmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باتوجه به‌ سوالات‌زیادی‌که پرسیدین؛ بعداز پیگیری‌های دقیق از مدیربرنامه یاسر آسانی بااطمینان‌ کامل اعلام میکنیم که‌فسخ‌ قرارداد یاسر آسانی درسامانه فیفا ثبت نشده و تنها یک نوتیس برای باشگاه‌استقلال فرستاده بود و هیچ‌مشکلی برای همراهی…</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/28506" target="_blank">📅 10:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28505">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lnNvUXcXlGngtl5stqo-CtBvAQ7NlJmIQ_1jALJduoSaSQ20TsPCNNW6cJdlF1xCNN4FS6srwDqVFXlJGA26kUZMCxS01TQCFoXDLm471rwalnA5Gii_iPQojrmtAyTyXDXMHU6JxUYv6BtBZBbbVN5wQ0Amf1a4v9FolMV5eLJIQfOIF8bRC2I0G5vxvXhSVhKDp3oi0ts07TP0FSV2pIQGhHb9yhEHzTNX-WZRCwq_4rcuWnG8a6hGesmGM-onE7uFYsrt6JmfEqYkAxu2ftcF_VOa8Ml2Z5qRsLcR728_O5k1mqjPJqHspkLDIWVjEY_U93fuzt0vgBKTkiSQSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#فکت؛درصورت‌پیروزی‌استقلال دربازی روز جمعه مقابل فولاد در اهواز؛ سهراب بختیاری زاده به تنهاسرمربی‌تاریخ‌استقلال تبدیل خواهد شد که فصل جدید لیگ برتر رو با چهار پیروزی پیاپی آغاز کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/28505" target="_blank">📅 10:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28504">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Motxfw7cuNvCwZKmmH1zK5PSWJwBXb5ZIcDQWXA1Tn2JEmn6o2JymhCJgZGdoI_FKyPGf_zA1tjv7onoQG-cPe_stfl8xpUFKSivJEPF6VkIhZhOwIIzwcV6aF6J1nL_7tgQ_dmCxsAkFH01ZC6m_F6ygV5zy8PFemuEVK-NzpgtMXm9tkZIrd4-QZbFcdbBKwb6b8DU13ZVG-DEqIVf-Tc34uBYyzjAfHHK82dOXQvkNFJU4lz5aOo1pNoWbMHIDcd0MLCKMScXse61pvSD8Ra6lyIopxYlr6OzM9W2wEj1-awIQ_1PlNbzt5pfkEaF9X_xGQXukaZ6jD-bMMFPZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای هفته‌چهارم رقابت‌های لیگ برتر که روزهای جمعه و شنبه پیش برگزار میشوند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/28504" target="_blank">📅 09:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28503">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6eUwBpfw1-uDuZcxUdWdW0qKaYwjcKXSljp2gHi-Dygq8119JTaudS6ajme4QLqpRgM80JedRLgXFyFH7XPW-y_mY82qdWhCpyHoiQeuzImDCuiSFs7yd-fINz-N0Q1uDqne40GHkJ3eKlzuChhTKlN1qDhcAx786cv9CgdSX8VL1dueISc1IdJ3nOsLsOtBp-RKxZI4JexBjCh2r39rmSGCrkEg0BmXR-C7InfCjU-sF8nL_ksTrCYoyLWxrT8u4Zp-DnT--iiX8SesO4w-O2vEfLhCRfbBbIlOqar8H6SgNb9x4eAJ8Qvag-HZEqOxQwS4AsMvKohm-G3jRKqTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیوانگی‌مطلق‌درسوپرلیگ‌بلژیک؛
رویال آنتورپ با نتیجه ۴-۱ مقابل خنک شکست خورده بود و تنها ۱۰ دقیقه تا پایان بازی باقی مانده بود، اما در اتفاقی باورنکردنی‌توانست‌بازی را برگرداند و به تساوی ۴-۴ برسد. سه گل در تنها هشت دقیقه برای‌رقم‌زدن یکی از باورنکردنی‌ترین بازگشت‌های‌فوتبال درفصل جدید
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/28503" target="_blank">📅 09:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28502">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MrMDWBI61gx_WTktSiVYtYm1QeC3bCXnU3_loy0mXb1yaxNCMC3OgSdv9bEJWq01E_bdQrvPVYUyH753v8O9wxGgRgw2Hl2RfVYQwqj8PPNq0Hv0Z58fJKtyjVNiXaPmtyoz5QrR3kcBONTY4_FZzkwge3riVXDbhH069CCrd3lwYJ3fCo_8EmuZgTbjoEFhQVK33tUDLOBmvpqcI6odc0GlNbEqZAQF1IaUZcTjBcsRAuw7WXkT7HPUOT9sENiHr4u3gNWxXyc7_Y8aqjrIDpnc8_dQLU9PUrMSeOzNbhL1N7x-B7wjNf72O-u_BHD4162baYA2sKhzp6ryEjIF_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قدمت‌تیم‌های‌حاضر درلیگ‌برتر فصل 1405/06
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/28502" target="_blank">📅 09:03 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28501">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKtXz-E7OO4jmIpxw8wdk8-IbAyRDUYe5yEn2bk_QrII-X-HFZbGwFGiyNaz8wavQ1wVKrQipjvmx0ay3WvgfoXiHxuZJoK8L7il-e1HRaFDxNu8hWYZDNG0RMKqZPlM78zdFhY2b0BfCgdVGRVjg-1ZouQdwncyVNyT8CWyY1rMlMcUW9PKNv-7Jdsed0u3psYuHk95XB0NSyYVVG-7Eb7Oqycl_AjKZUygLdKVRIXVfbHRuT-0I2h4KK3RK8nDLZHkCvjVKK2TsNX-67FuObWIaJZ-UOpyQetpZsiukaNqap82H-Hy2391_xaP4x-2zM-t_CbJun5SkxalV9G45Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇩🇪
مارکو رویس در گفتگو با رسانه‌های آمریکایی اعلام کرده به احتمال زیاد در پایان قراردادش "خرداد ماه" از باشگاه لس‌آنجلس‌گلگسی جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/28501" target="_blank">📅 01:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28500">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMisVKv_4w9X3Xt9Hh0hwEd366lZHZ1G8jHGEyKD_g9wMJTgexlilFX8t7XWDYpXDIlqMK0Q_VVZyU1-hVhnEhZGKzXKJVWl1tzupanTew_CKiqYN8ixll1FGTOZdnQvCrBslPMR6hGEdj4QWp_Xu9NPlvZWtjGavlm-CEVbko_ti0fHDAJWQuqpNlVERcnfENTMQObzINS8KkqOMCC6W0LfEp_xq5kvp1D_iSgbJ937jBy46zZH4Gt_VO0ZwkARHt_dCbX7ekkIBYah4zNEnfiVrePIHSCTogZ4XMxsi-zFIiZMuCwyVnaEqsOsTv6hVk6V7rpBRemjF1YqNAJmIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌‌ امروز؛
دومین آزمون مورینیو با نبرد کهکشانی‌ها برابر سوسیداد در ورزشگاه برنابئو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/28500" target="_blank">📅 01:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28499">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibgdhKmwveuv3E31Za5MjmJtJ792hObZ2n11mgiSpXx0PBY9thjiRD3fcoUES-WVE79ZM28dM1HgSxy09pcq_tsx5-hQzkm2TlNX2L5_0wV0wUy3tZ_UFjPa6P_m1ghBhi0FRHoHV6N2c4XR9IwufNM6LZGNpIfMbVCFCi747UqavnjS2RR2DdcFC5hUPjFPrSAcnFI6EyMfeCj8Aqg17EYX0DzZ_XxYDd3W_J_aoAPG8OOWDIMCiYIgMBml1uzlGyVy72-mmNKutz-tinjJ9-rfjlHIOgqROCAQx5PfRPDjNyHJh1MvxqlsVmO1cxxax1Hwni-MTaeBzp4Z643iTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌دیروز؛
بازگشت‌دراماتیک شاگردان پوستکوگلو با درخشش ژائو فلیکس و سادیو مانه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/28499" target="_blank">📅 01:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28497">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DaTNy5N2yow_1J1mA46XluLJjGQP544eZ_NBvIqi7rECJbVDppbv77Kj_b4d4pelZ0qfBsMWd8xTJA_08wOk8_I4IwXFZy09KJVx2CCMYPG8AD2WciPQMPCc7ZFs5f4mNUr3v3HaBGMGsLrLjf64pH4qz-jE4T5O283WLvsFDACm1lRrZCVMadB5LzZvd-dZLPqGNUT1NU2d7WsCaLOYfW7HvLaRUrlsZX2_dkKDUDluNB9340EjgxN2hxNzwu1y9esJMiTowIt4avYSEmCpIjM2F_BcYg0fgh5wNguRWHC8gNvSO2zuNerzuQjHrtLTipy_VSaI2u6LHrp2dZvFyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
#تکمیلی؛ باشگاه آستون ویلان پیشنهاد 45 میلیون یورویی الهلال برای‌جذب اولی واتکینز ستاره خط حمله این تیم روکرده و قصد داره با 70 میلیون یورو این بازیکن رو به عربستانی‌ها بفروشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/28497" target="_blank">📅 01:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28496">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/122f8acbbd.mp4?token=LlVyYQN8MrbbUyue9_tuTtOTESS8TfmekWudma9eSu3w84vHCVBWT_3IWFfubCSBXm274p_VFbgPLNymWUZEIxz8MVWjB3WDjHzzDJ4mwlK35VeI0oRe3Gf51UxIRtnRQHY4LrxSHE25hRlcX5B1EUNU8vHXdj7voYGdr5Fm_ZlXsx6mioHZyrDoHAghqJaHxsMDEZ5qWBxj7Bw8gwFI20viB5vI-4engDi6XDscdnTmeIsPxuPw_ppeaDfniaU6uFekN9OCPx5VUQrs2w9sKXPZhdxka223-BzcFPCKttUVpxxo2AoiBoFpQ-aLNCE7gWIpyj8kzNZK9YtDEt3jJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/122f8acbbd.mp4?token=LlVyYQN8MrbbUyue9_tuTtOTESS8TfmekWudma9eSu3w84vHCVBWT_3IWFfubCSBXm274p_VFbgPLNymWUZEIxz8MVWjB3WDjHzzDJ4mwlK35VeI0oRe3Gf51UxIRtnRQHY4LrxSHE25hRlcX5B1EUNU8vHXdj7voYGdr5Fm_ZlXsx6mioHZyrDoHAghqJaHxsMDEZ5qWBxj7Bw8gwFI20viB5vI-4engDi6XDscdnTmeIsPxuPw_ppeaDfniaU6uFekN9OCPx5VUQrs2w9sKXPZhdxka223-BzcFPCKttUVpxxo2AoiBoFpQ-aLNCE7gWIpyj8kzNZK9YtDEt3jJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نادر محمدی هم یه تنه تمامی قوانین فیزیک رو داره نقض می‌کنه؛ در جدیدترین اقدام این پرتاب 45 متری رو در لیگ یک روسیه انجام داده که کرک و پر تموم رسانه‌های دنیا از این پرتاباش ریخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/28496" target="_blank">📅 00:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28495">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61cd0ed9f9.mp4?token=XQ0FCQyHtnoNsFaYSZ3oDv2drd8WAEr5NN6kxQrFnin5kjyYuqg0J12c1B-e7fNlXVkLwAxH99XAbLs5tRxJVpokozXcpSVAxADkEnBVeckHFDdNm5hhR4bqi3JY2XFEejSPbInNCFEwoGDTMHX-ORE7hvsDE3cuQT04Y7y26NFo9RDZRh9AVIpYoV7WboND0vX5mFHqqXqs2Uo_pquF6tTXmvDPTpL1bu7Ijk2GK_DMR-G7u78pBcmC8dYhBR4Y-S7tWOC5xt8nAYiJiYjo4IXQDF6l3otS-IW4m4pjtGu4gvQQy8b8M9dMHm9By1K6JvFrxmZGrqUgeF5nSZX1qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61cd0ed9f9.mp4?token=XQ0FCQyHtnoNsFaYSZ3oDv2drd8WAEr5NN6kxQrFnin5kjyYuqg0J12c1B-e7fNlXVkLwAxH99XAbLs5tRxJVpokozXcpSVAxADkEnBVeckHFDdNm5hhR4bqi3JY2XFEejSPbInNCFEwoGDTMHX-ORE7hvsDE3cuQT04Y7y26NFo9RDZRh9AVIpYoV7WboND0vX5mFHqqXqs2Uo_pquF6tTXmvDPTpL1bu7Ijk2GK_DMR-G7u78pBcmC8dYhBR4Y-S7tWOC5xt8nAYiJiYjo4IXQDF6l3otS-IW4m4pjtGu4gvQQy8b8M9dMHm9By1K6JvFrxmZGrqUgeF5nSZX1qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز اولین‌تیزر سریال «مرد سه‌هزار چهره» به کارگردانی و بازی مهران مدیری منتشر شد؛ مجموعه‌ ای که ادامه‌ماجراهای «مسعودشصت‌چی» را روایت می‌کند و قرار است از اوایل شهریور ۱۴۰۵، به‌صورت هفتگی از شبکه سه سیما روی آنتن برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/28495" target="_blank">📅 00:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28494">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQUpB5ed7j5r-TKWcdTppiX1AM-Q67x3h3N2fsh4UD-0b8GCC808DA_aGhd5Egicwv313BW-7JXu8gGTj_69ACnvb3MAXQHPaxltkcCUP6dFLgChb4dwnHbcvy3kKJgOpfls4QBwl2_xD-falPiVhu2b_vpMIaj0tcMQ0tMXeuy9odU7NRgVIek49ZKJdALvSjTUxQm0sE7PUZQPGNL_mmDARTs0HBM0QTR6GXXIrQ3MHcl3iIjSVvJN0pLlioqEOV-OCmJ2qNy-7daJUpIwCXr_egpC4sHGm47sscfUJnHTG04MJ5KLuUK_KWxDASLZmrTHjwAOfL-wMUNb7OLIMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری اوستون اورونوف که گفته مصدومیت جدی نیست و مشکلی برای همراهی سرخ‌ها ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/28494" target="_blank">📅 00:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28492">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ig9FGP_uulgRNUe5GbDtu1uUJLqb-TV1ohwXyi0p0KUaHRB3Rkzb_U4BZlO1ePO5D1MoU9PMM6v_AaVFitQyR1JxYIBxh1G15eHYG8DYq0kYtKbGE5ayVvR4Rjm8BrVZHuAsGJ5_vmsIJVeJ5V-xDTTyZ3VIXwcvJWwifbzjnPYom2kQbgQcvTaNIWwCse-EdPlsyEA0E6pIkI1JCvAHMs-fheRxYWvOgUTUIx3H4rZ9dYqZT91AKQ9BlvOFbenMBb__7WBt5wEV-HJ-I1TtFZzgQN0C538Q4tGpMoJcE7_-L14WyohVqboXJ_TYbssbcjRB6Mfgy9-fk0jXRsHFiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d1xkUmXMgVDCPzZhcUxl5_ZfMlExxNkxtZjJwZndWarCkZ5oozALgeocA6AJJ7djDaD8XVT5uv__cwuo-jk8lAEYk7gDgSIw4ziKhA8PGFUT7xByUYNBb-5JIXaNRUu7v2Hl2F51HDpqX1d7VhUCG0k4i2HVO6yjZ9rWDS9oCQzSsrBM5PkvLyIyUSU4NhGtflb3yzkZVeWMWbhCcq3yKfgBAHOqT-lCmabP0tK1k13wHVUQkbeZSw9kP9SCUPoqArYuhvRwhCmMAeee-48s-V4fK89RwXm1qYWVdubBc8PIga5G-qMeqvaZDf8ICSu5vagY0hH0HoFh8YeVjikNFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
#فکت؛ عملکرد حسین‌ حسینی دروازه‌بان سپاهان در تقابل‌های‌ خود با استقلال: چهار بازی، سه شکست، یک‌ مساوی، 5 گل خورده. 0 پیروزی و 0 کلین شیت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/28492" target="_blank">📅 23:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28491">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tN-RNdENhNNThLc1wLkdl-VZ44uA_z2MdkB1sNa9PmM3qh5_ur3RGLSDsEghnfigMCJai2698iLPYVeP8H9--TMkbsNPV07QFxSUI0yAerMEIBApTsjezXdSSJWqEJlN7lTwcC8pW7gX216kTcy_rnzNFVBD0ePfYPkOg8gf_xnzzGBZVXrXFFon64ZSo5kPxDKho20AwCRrz4Mbjbi30rXDeda90qUo2oow50xatTcsTEgUUVjBMHY_kQZaYgh1ceAvs6GZ4v4vnKrL2YFKq53YeyEIZwiF-ii1tEClHXlHxtMC8NcJFzYbMzvlKeH5Ky1ii-6AMZ-U2pgPILjSPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ مصدومیت اوستون اورونوف از ناحیه‌قدیمی همسترینگ بوده که بارها در این ناحیه مصدوم شده. فردا از او MRI گرفته خواهد شد و میزان دوری از او از میادین مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/28491" target="_blank">📅 23:33 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28490">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d926debd47.mp4?token=UtL7WNNWGDWuNfvuVFoYMdEx5YRVRxbnA5ZP2AyU-Pk6Axncp0Kyt4QfBeoVT-FkwKhAL4YmffVeRdFAhPF9ZjLsaocoKw1d9Yc7yY-Wb94dW4SOvAcA5FExfHnCmg4V7yLJQHcQgzOQQkpoedLZ-5U-1D1TwMoCFpGcwkLs1GLe1TqkKKeCBC6Kx43tu3Ay7NQKkGXr6vSkAIX788f_M4O-mia9kfAxJgyTmViX0Sro-Y4wQLd5QoLyFZvUWGJFrA8BSssxjXCVTYs5o7JYT8rCwpfTt9lSNgUrQ42ke_-C4fBC_DpJqh8bVHeErXZ9nCR9m7eJfc591oPWeEkvYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d926debd47.mp4?token=UtL7WNNWGDWuNfvuVFoYMdEx5YRVRxbnA5ZP2AyU-Pk6Axncp0Kyt4QfBeoVT-FkwKhAL4YmffVeRdFAhPF9ZjLsaocoKw1d9Yc7yY-Wb94dW4SOvAcA5FExfHnCmg4V7yLJQHcQgzOQQkpoedLZ-5U-1D1TwMoCFpGcwkLs1GLe1TqkKKeCBC6Kx43tu3Ay7NQKkGXr6vSkAIX788f_M4O-mia9kfAxJgyTmViX0Sro-Y4wQLd5QoLyFZvUWGJFrA8BSssxjXCVTYs5o7JYT8rCwpfTt9lSNgUrQ42ke_-C4fBC_DpJqh8bVHeErXZ9nCR9m7eJfc591oPWeEkvYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
ژاوی هرناندز سرمربی‌سابق بارسلونا با عقد قرار دادی تا پایان جام جهانی 2030 سرمربی هلند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/28490" target="_blank">📅 23:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28489">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‼️
🔴
👤
در فاصله 8 روز تا شهراورد پایتخت؛ با اعلام باشگاه پرسپولیس اوستون اورونوف ستاره ازبکی‌سرخپوشان درحاشیه دیداردوستانه امروز این‌ تیم‌ دچار مصدومیت شد و تعویض‌شد. هنوز قسمت آسیب دیده و میزان‌دوری‌او ازمیادین‌مشخص نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/28489" target="_blank">📅 23:14 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28488">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FmOXA7URvTn-y_3mIYQwGfCe-J-jB8Ie7BCYB628XAAzwoLG_QzJn5aLf4sQ3wwmGOwqDOhrb-bow9xLWwcDrv-Twi19NVhPvXX9CSeqIHRW0OsRxxUnOS5SRs7tBzV2uEd5VNjI-6rV6yQpdbyPpq8nqxi31v1EbHvmy0uIqGBKYjnzPIWVJQN8Vc0tn3e59p52PfTOpJofi2tmqUk2JnTl_9ItK0ePCdXaqynKQz7HY5v49QSIwmWGsu-aegtNpIHylt0r66kNlOIvbYNFOQNUgNS8oQj-A14QESHQXlQQ-HuNMBEBojMOvdRDk29Ma5O5RyGd2_l8zIFQBGDAuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇵🇹
برونو فرناندز ستاره پرتغالی منچستریونایتد بعنوان‌بهترین‌بازیکن‌فصل گذشته لیگ جزیره انتخاب شد و جایزه ارزشمند خود را نیز دریافت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/28488" target="_blank">📅 23:07 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28487">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tlhHJjHBJy2OYJGjdbUKLBWID44Prxh34dt6HhxhmRysqJoTXgOR-M1MAXV4ax7X8e6vKTz4vfuF0GAbUUhwWkeb2rem08Nd5vlQUTX7E90FjVeEPQA7nu_zmc8zd2U1lf_MlG8GlsZ220Lzl3-59f4Dt_G3zmdMQFc_x4pgQepfdWk7hgoZxSwn2j6xvxfnPg1Vsk91k0EOvldbTik57xYPZlx4VRkNJ7CUxbJqcrUSwJOhiGkHFSddGLU2T3-Jg5aQoDsTY_DmDBWqq4wuGNuOzrYBYGgldGwfiYsy5dybNteEzqB_hqF2U12MuWz2qRZjVjVYzFbug63rgsuM6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
ترکیب‌تیم‌منتخب فوق‌ستاره‌هایی که فوتبالشون رو ازباشگاه‌پرتغالی‌اسپورتینگ لیسبون آغاز کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/28487" target="_blank">📅 22:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28486">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f05b52e15.mp4?token=lBRKWWXY3dzUq0pDE166vFThlqqA6FSYMT8jsHD1YFsxA1Uk6NfiFtPEs9As2TWxJg1--BZ3oxlWl2aEI6PixHoaJN05YO9YFj10dtAj2Ve9TZ88XSpM-7cgOyq4FTTb5fOal52Z4F0alMPAdOAyI0q0yqovoEab27kV8SqeMVahbq5pAyPLd9_IqKpYsxvAXm0PozsuV9dGoEmkKBOUHQCAmISONR_tqZm7Xq8E_JkusU9_v_tyDmbCEJcqvuj2NkkiVGyWfYMjLLh9NepM13o5E5dQG-0Sp-n5IGP-tFtOVvE01N9PZNMbmSLUuyD32W2Hna5-QdlJKN6dpLwsfKKyTEPGrPFT2fxFONk4mnMxLDqYi2DGo0ROnSL8eTzXCIgxY-c3sYOxu0dVhYF7UETxEm_pPK8JZ2KOATeQsrTe4_mOZjHuV2oq4lgb0cOXeA2VV8rN3tl7uErqhJolR1oPUzAjSFJNG_8X9wEhwptZz66E6VmtHt3Z8z6uJ7LEXNl-pDTTo2kSpnDdqPPSwrsXM5JOhJm2vZgr8pBEfaQvh1fEVPvJjiXGCjYdxsweG4Cx3rQA1Yi15_5TCZbLQ2hewj1xT8TDh0sZAsAkZMkqTgqVqr0R0tAOzsTItakxRCQ1e_XwL3BgIP3MJIZ_Sfd0PNEk4uv7rj0u7mI4Rf0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f05b52e15.mp4?token=lBRKWWXY3dzUq0pDE166vFThlqqA6FSYMT8jsHD1YFsxA1Uk6NfiFtPEs9As2TWxJg1--BZ3oxlWl2aEI6PixHoaJN05YO9YFj10dtAj2Ve9TZ88XSpM-7cgOyq4FTTb5fOal52Z4F0alMPAdOAyI0q0yqovoEab27kV8SqeMVahbq5pAyPLd9_IqKpYsxvAXm0PozsuV9dGoEmkKBOUHQCAmISONR_tqZm7Xq8E_JkusU9_v_tyDmbCEJcqvuj2NkkiVGyWfYMjLLh9NepM13o5E5dQG-0Sp-n5IGP-tFtOVvE01N9PZNMbmSLUuyD32W2Hna5-QdlJKN6dpLwsfKKyTEPGrPFT2fxFONk4mnMxLDqYi2DGo0ROnSL8eTzXCIgxY-c3sYOxu0dVhYF7UETxEm_pPK8JZ2KOATeQsrTe4_mOZjHuV2oq4lgb0cOXeA2VV8rN3tl7uErqhJolR1oPUzAjSFJNG_8X9wEhwptZz66E6VmtHt3Z8z6uJ7LEXNl-pDTTo2kSpnDdqPPSwrsXM5JOhJm2vZgr8pBEfaQvh1fEVPvJjiXGCjYdxsweG4Cx3rQA1Yi15_5TCZbLQ2hewj1xT8TDh0sZAsAkZMkqTgqVqr0R0tAOzsTItakxRCQ1e_XwL3BgIP3MJIZ_Sfd0PNEk4uv7rj0u7mI4Rf0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تومیسلاواشترکالی
؛مردبازی‌های‌بزرگ؛ اشترکالی مهاجم 30 ساله‌تراکتور که شب گذشته در دقیقه 80 بعنوان‌یارتعویضی‌به‌زمین بازی اومده و در دقیقه 90 گل‌برتری‌تراکتور روبه‌پرسپولیس زد. سال گذشته نیز دردقایق پایانی‌بازی‌برای‌تراکتور به میدان اومد و در دقیقه 90 گل‌پیروزی‌بخش‌پرشورها رو بثمر رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/28486" target="_blank">📅 22:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28485">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oalY2yiZ_T28g1V5NkUbM4xX7tpo6ZMqMsoaZ1bNJNv1Z8RD6C1zI84W4E9fzaNoi-XLQvu8Zn4sKfO31NtPMvvcGwwv3Wyy8Z8k_LeAaOF6BVlI8bXOsLr-FCcbxKtxrvS_8Fd3xqz1-Mx9XZ6UYA86cHh5kavusMaOFV3ETIl41feOsTPBdzKqHpJdkAAbwKbuwasXZcTYWMOnXVTfNSGHWoslZW7_J6dOhJcfzjz0Ezz9bXwvBNhHLIPKsu3sqFTL6GSSqhtm5IdOLFgHPVkBjjTFBa_wo8T5tfZ0tCjVfWd5orO1ciJmtRn8QV8BYsZV2ONlQM4lEDw-BTEP4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#تکمیلی؛ انزو فرناندز ستاره25ساله باشگاه چلسی در یکقدمی پیوستن به منچسترسیتی فاصله داره. آلونسو گفته دل انزو باموندن درچلسی نیست پس بفروشید و 140 میلیون‌یورو درآمدزایی کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/28485" target="_blank">📅 21:55 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28484">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4bE4ynxWLdahbq6VKG28aXeve_8HpJqNl02ZYybEEQPwxTqz1IzIkDb_xkq87JAXdIvfZXJ-VSrYIHb0tdbOikKW1vEgVXLJBi9-Issq6sm7MO1yXK8aSovCjpCBcqsqhZPSrVSA65ljNurLZeC--6KFe05oKt0fyr0PyZH1K5hqt9mWocQ_TAm-1qciFA80cJU04A9Cg75PTUYyWO9YquJA3ag1HX5Y2OU4fTZ1VTW219z4lvHR8tVw8c5GULnspeChvODuA_VNVxEJ3IV0-1GGRWxfGTYn9XSKH9yY8ptlVLzcrkLU4BgeQT6VyPia7Pc0_zXUHWn5qjb3WwghA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌میلان باموافقت‌روبن‌آموریم؛
کریستوفر انکونکو ستاره‌فرانسوی‌خود رو با قراردادی قرضی تا پایان‌فصل به لایپزیگ‌آلمان داد. انکونکو از ستاره‌های فصل‌گذشته روسونری بود که روبن‌آموریم نخواست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/28484" target="_blank">📅 21:34 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28483">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rPzFg1Ty2bOGJvH5zotmPhyyOmg-QcbJjgimZxeM9lt6aoSevGHR-1Tj8yIUbXdosbfXGK2BwAsNcxRqcFaGrcnyfpnKsN7VpAUzm5C0fOrI8JH-1ixLvz8gPN6cGOAien94puOTyNluVYnB6UuC2KsMiDXTyJcoKqHNCJw4Rp33f1wajLsz3Xp4puBCVWia_C2O_BO8Nu4wS_LpVbsalcW_L0-DmUOtsozpDDZ7qBP3nI68tA0t89SvlqSmmAf_CTmOQeGy47Sm925_WBBlPQdQBOnbR61y3vCV0nkA7dFj0dMqGlOYmSCu5Avw8z6M_5mbXU_rQw3mrbXtCPhI3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
در فاصله 8 روز تا شهراورد پایتخت؛ با اعلام باشگاه پرسپولیس اوستون اورونوف ستاره ازبکی‌سرخپوشان درحاشیه دیداردوستانه امروز این‌ تیم‌ دچار مصدومیت شد و تعویض‌شد. هنوز قسمت آسیب دیده و میزان‌دوری‌او ازمیادین‌مشخص نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/28483" target="_blank">📅 21:15 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28482">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-bowVKWIPBnIl1qla4AiWN8fDtfoS8CYNg2aWA4WlUakHUwQMQOMI8ez20kQsdRPK07l-PmA0hypKUwgoJENeg5P7QCg8YAJAuqvHWekl1oxDhk2wC-uAsI6QYMzhYLgK6vHKiXK3luLTwhZLJVmjPPzjmxY-VOwMzfYveAilEq9-ljW0IPsQlbCKKtT0i8C-Dh_SnzzzejzDM_yy4zTGPzdAi-gxYFMKCJHhKwPLO1j0ETl_ZB79bFnFvh6IkgdviFkVjSq4RQACYFpcnGKacxkL_GZ8K9hU1RWrsiCxXbSHTA_NSJqGohLyXXCK3GEfsSwDIv4Wej8_3pen8DaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
در فاصله 8 روز تا شهراورد پایتخت؛
با اعلام باشگاه پرسپولیس اوستون اورونوف ستاره ازبکی‌سرخپوشان درحاشیه دیداردوستانه امروز این‌ تیم‌ دچار مصدومیت شد و تعویض‌شد. هنوز قسمت آسیب دیده و میزان‌دوری‌او ازمیادین‌مشخص نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/28482" target="_blank">📅 20:43 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28481">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RXESDcOudHuE9pooAbbHip66A5GIA_7Na3x-RVNXqp86cpT8cYrMxh10i48ds6whiFy7lzPK8F1lmE8lewrSx5VzCnEFVnePytkZMbGLP0twKCOLfVCvp5VnGXnb-o8JY9rUgyP3idSdes91V-DJBXVhFfPrk2lxR3ZNUCUd6e3B_Xjg_5Evot2ckMwhItlHxCJ78PktlcZjm930I-CzwscDYZNqaEgItRbezSavrwALipGOQM2PWlaFcrpnA78_gaO7_J3ctBNg7QovveVQOUu_-Mwiji7Vpz2ml-1z28cgf7-E2oPsPrKpE2vTWdKrwBHhG2585TsGgdzKNw5IlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇫🇷
رسانه‌های عربستانی: کریم بنزما در لیست فروش الهلال قرار گرفته است و کادرفنی این تیم به مدیریت باشگاه خبر داده ستاره فرانسوی 38 ساله سابق رئال مادرید رو برای فصل جدید نمیخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/28481" target="_blank">📅 20:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28479">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EROs0A8UwPJlnb2ya27NoMjzRsJOCuvl41g-8e_d6loX8ZCRGW1QWMXbo2ZKMUrQnUItL76Fio7_oFPE6j-8ShWjtb94cmRRWjXu_wRvgl8JbQ9I7ABff7hD_a5ALrtfsgvyGPRal18K_DKsEPaCVe7PwKKOgugA1RasbQ5LidZ4OSxTYwMcKE7JZfH4u8fj8l4b_5oRCJ21R-CwF_5xq7xyV6ZUm3WxawmwAfJ33C9JAffvsgtzENJk2x7Aji0qhvB1gNcy9ADLhdSKRBU26Ah3_w5ocfm-WulAEE7XNlisnsjuUkVwfxYq6P0d--SDt6L1hc731zHlnU5y9W4CCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SIh0GzWuNMcNOsvYuQ8_DKdDH9vEPnSzXJz4n09_EKNkOiPcmIbkJqNcZshemPNsHXtMTO0glepl59ao35KLdHRBN27-VAMDm4Xrhrc2wjH4OEEg0CE3rXkwQKdWXszkd1uLz0ABOmMdxdvmtPl4RS0aICxIIT9E3AHfZOMvg9mBiDyu1Ah41K5ty9sXzqtUAJ5wsuijBN_xSvYye_Ej62s8BMnn3JPeo4dvwDet1I5x_BHtv234hRSziP-ocHDFdYUKdPxuKpBl2JaTj7pYwNgjhU1L1raqEwyXEUy9ly0Nk-muoSQ9KWUWwFQjsBvoq9qBNfy6tWCh606Rq7SjMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇦
خبرنگار معروف و محبوب شاختار دونتسک در کنار خانواده اش؛ جالبه شوهرش بازیکن تیم شاختاره اما اندازه خانومش محبوب نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/28479" target="_blank">📅 19:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28478">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMoeBotTtzolcxW4c--lMONVjGkL1h_At9yJQEYn5rma6UAHu6TAlGuOqSInQQmGcxjA3pjoz5kdZM20gQQUwh4UfIdPly42AimEnkW64hFE83XTCCN0pufecVm2eC57H6AMrpILNHKcT04pIoHerB2IXTS-ccGIl5U9WmYujozl2ztYpSsYrm8Y2kD5cIrgcZh3bLfV9cIMhv1MTIlAImi8pSfcl3iqEbQAtuc-n-uyN7ajDLFQeP73LqhppfQhX7wQ2YdK0MRoGQ-TX75qChxocsSZeWhODdfbbYKxLEqxf35NBsJyhERkSZ2Wt5KrXHEGZ5k3UwQYwbkWldt3sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم؛ هفت روز تا پایان نقل و انتقالات باقی مانده و هنوزسرنوشت بازیکنانی مثل بارکولا، آلوارز، انزو، مینته، امبایه، گاکپو و پست مهاجم نوک برای بارسلونا و وینگر برای لیورپول مشخص نشده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/28478" target="_blank">📅 19:53 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28477">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxetivueDNaQbFRbSJR113pOhzmEq2nwB7qU5ME9LpTM33JZ9879mRKCfd3I-TIo9s5q2Bzb6jQtP_ELaMpJCztUTWr0iL4RH6tisZ65NB5Sb_3wxOgIW_iNUQMDQ4ZhaVBoSxiRuNQg7eb9eRC5I2wauXo9nw9LlcyGbUzCoRYVjhXSLknb06hKdk1wPypfiOhJqj89pgf3_Ny6slRhnMLT8PJ2ksy6hWGCiu56rhw58tLXa8yxofOMAfs3TOF9e03gBFIQUl0hSv9scVSYCvgrXce9gW4qdv4k8gu8FHfMZtLNAx-I0tD_Dlc4i992gOT56fzE5L-De9INVYDz_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نهایی‌دیدار روزگذشته تراکتور و پرسپولیس از نگاه‌نشریه‌متریکا؛ محمد نادری مدافع چپ تراکتور بهترین بازیکن این دیدار حساس انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/28477" target="_blank">📅 19:13 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28476">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZ5Rd0uQAV4rN5caG86jqR_dbj2vb9YR_3cY1BBQZN8BrPxrPJ9b8SCTXCUotBYg0a8osyN-dJ7KlEWXPP4uEuSw2SUuIqZAEx05RSom2VlE20X6uy5YNdgaa3e8DhxqzTOdPiGHDnz_tT-Xf7A645jRRAXTP_Gcnr9GYhmTmTRSQgp6oMUvoznqGp69ZjOFk1EsF31ZZqXhenDHIg5o4O5PBuo58PuR1KnMnsHf2NcAIMUGBgA-HdGohokjMnDnQpLyKIkoirgbguv_6_2UDBb9BoIbme3eVDRodbI6KVrXSPOdIm162PMc2pM-v_2oJoSUuKpU_jAjOXjIraiLig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حرکت دور از انتظار عارف حاجی عیدی هافبک سپاهان خطاب به هواداران باشگاه استقلال در پایان بازی امشب؛ حاجی‌عیدی در دوران حضور نکونام در استقلال تلاش کرد به این تیم بیاد که نخواستنش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/28476" target="_blank">📅 18:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28475">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‼️
قیمت‌موادخوراکی‌درتنها 5 سال‌اخیر رو مقایسه میکنی آدم‌کرک‌وپرش‌میریزه. کسی ندونه فکر میکنه 50 سال‌گذشته و این‌قیمتا تغییرکرده. قیمت خودرو هم که بماند همین امروز روهرماشینی 50 رفت بالا.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/28475" target="_blank">📅 18:18 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28474">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pnk3B3JYyWlrfrG6V3nBHO5MZ7i0TNC0K817PpQ_VmB1nJI3MbYsJdr1ZZvT9zPfDMXiHrMHc8j_oYQSv17ln8ry2nr2RHTB56WLQF8g2vTRRR0OK2g7n8D0veFGwARWcqy1nWf1-nC8ln_SqgEuVa9yTEDPahxlWsh4W7dK1ICq9TVzkVDthDT8e6wV58W54tD6hV7gQWK3oLtNWNoqzX5wmf8-nLq_diGP5K7PzV89VIKRWp97Ivn_8cRJz8UIVB7tS0uW9BoXOuICzokGTdOFdOyoPiYau9gi7tBFa_YkhBCiZfd7kTqOHHvL-OKmlFY2fm_J8GYUd8FmnlH6yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
🇪🇸
#تقویم
؛ سال 2017 در چنین روزی؛
بارسا باپرداخت 145M€ به بورسیا دورتموند عثمان دمبله ستاره جوان‌فرانسوی این‌باشگاه رو به خدمت گرفت.
عملکرد دمبله دربارسا
: 185 بازی، 40 گلزده، 6 پاس گل، 141 بازی رو به دلیل مصدومیت از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/28474" target="_blank">📅 17:37 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28473">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORzI6ODo7zsBOI1LWi_43hp29CQBbrN5V7f-Z3Ls1ehA_lc41sa8ZyhquACEFtnZvGOFJW9AjroBR0cNXsh3SBQ3LmVxa9OCv5tpNWd1tl-LaFGsyGesb90U8fYS36qKtZdCMrwSdp88WF3EbVt_QUEbOIFREP_rAKvWGsfM4t4lBNteyAB9qMvh-yjLH5B0G6OzOjQbhIfDHL6bSRGy3i2mnohSZ05Apa551hc_9UclEqdAWi0KA0hHaet2PRc3ZOYU_VEk8kmsVEcvegGVyZKbMDwfw9ed6N_5VYZPp8aDAXlbNWjDy9dDANGIyC_-CbysXSg32lL9hvCx3z0hVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌تاتنهام‌امروز100 میلیون یورو به باشگاه‌منچسترسیتی‌پرداخت‌کرد و از ساوینیو ستاره 26 ساله برزیلی جدید خود رونمایی کرد؛ سیتیزن ها دراین پنجره 12 بازیکن خود رو فروختند که بیش از 400 میلیون‌یورو سودخالص کردند. الان هم میخواد حدود 140 میلیون به…</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/28473" target="_blank">📅 17:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28472">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hdo300fC2Ds3zh3P6s_a6KfT6X3pqInc-ULELC_eT3Sv2mXbpflgovez2K4SnVOPlqUcyOeEglbZaEOm_9rp7R-AwFYJvdMPNx0ELfF3UxIlz_ufuOPYkyEA6s81BEph3RDlXFbB3gK5o9IFMKLUmohcYC0wkNpIvqX3DYDX6VczAT7MiaE72twI3vuIMR9a2URqK-HWAVvx5XzKDE7qU6Qj8nNFF7C4147NMxwWGIAfsbded0__FBzmtcDDke7VZ7xRsHUjSRfmQqo_ZHcceLzvqQYheb3CXIWKWhH9x9kHfc4q9A7-j311T2j8vWlKBuGK3p3BR6SebWbqmofFoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
ترکیب‌احتمالی تیم‌اینترمیامی درفصل جاری درصورت پیوستن‌پل‌پوگبا و آنخل دیماریا به‌این تیم؛ دیویدبکهام‌مذاکرات‌خودرا بااین دوستاره‌فرانسوی و آرژانتینی‌آغازکرده تا درصورت توافق‌نهایی باهاشون قراردادی دو ساله تا سال 2028 امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/28472" target="_blank">📅 17:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28470">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aRMWX9QZZs6fMBfdKWdIZLZ4U_tbP-iYqI4jcAvcGll9CWQC7tLjF4raHAYrThGrUbhiS_F0Gx2RIBbyy52nXHr4PA7IB_RGZNX8HaYGT9A5z5I1-mWzg9lzQ54yIiHMbXWObldY2-QXnFzMwwB4zl3ALRwRm4FKVI3AEjwtYtaFCSeWLYEQz7iuR5z97tRE0PVHb96uqvGs0JWZGeCsz_OCdqo7A5Mb-LZtNuGCsYG1KA6gcwOqMEYCfyXao3kKzBVw7NBQ-eixQKYE5AyBfSqEk2xKAvlR7bWFzOG-RPVeRwuxmUpMD3pIw52KL3kddhL_xjehoIRa3GBJbd-DZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری دردناک محمد فرهنگ یکی از عکاسان زحمت‌کش فوتبال‌ایران: دلار شده 204 هزار تومان! الان من‌چطوری اعتراض‌کنم که بهم انگ وطن فروش نزنن و از کار هم بیکارم نکنن. خداوکیلی دیگه خسته شدیم از بس دویدیم و تهش هم هیچی نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/28470" target="_blank">📅 16:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28468">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f00e5c331a.mp4?token=dB-m3g_Qay3tbyPlgaD9XaAMLv0wYmkEZ7LwH_pNJX7BYf6jQx8fyvA1KihqZndm53iJsuYIzTLtSPnn5-bx0ZBiDAJJMFlJ-Nu8Zzf5Zdva_VXzJxtUTlrZ4mEL9INizJ2yAkKQ9w0Ap_EQxFvQkRj_EGB1mqzBi2e5-GtCBRZNEUt4RDE0QSJcNfL5lCwi8CO1ngNJRVpyWjqcBNb_XNFkxEFTYmEBX6CnVN2hLL6tRwg9TAfHq87KBLk6oLuMXdMlnZ7bLtpmOLaA1t5HDNkCSrX2i8EsmbQx8ZNi7krsWvSKqxMGwaHPTwkIhl62oeWg6NEo301Dc8ljPPp22Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f00e5c331a.mp4?token=dB-m3g_Qay3tbyPlgaD9XaAMLv0wYmkEZ7LwH_pNJX7BYf6jQx8fyvA1KihqZndm53iJsuYIzTLtSPnn5-bx0ZBiDAJJMFlJ-Nu8Zzf5Zdva_VXzJxtUTlrZ4mEL9INizJ2yAkKQ9w0Ap_EQxFvQkRj_EGB1mqzBi2e5-GtCBRZNEUt4RDE0QSJcNfL5lCwi8CO1ngNJRVpyWjqcBNb_XNFkxEFTYmEBX6CnVN2hLL6tRwg9TAfHq87KBLk6oLuMXdMlnZ7bLtpmOLaA1t5HDNkCSrX2i8EsmbQx8ZNi7krsWvSKqxMGwaHPTwkIhl62oeWg6NEo301Dc8ljPPp22Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هوش مصنوعی دیگه داره کار رو به جاهای باریک میکشونه؛ یه چیزایی داره درست میکنه که با واقعیت مو نمیزنه لامصب. اینو ببینید‌!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28468" target="_blank">📅 16:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28467">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CI50NP7sMVrF-bzrAsPk2D02kpd--gcw1In6IBoIMp_ybszL2ld93IU7lwTCHjSsTJQkVvG_kLcWYjz-opE-UGL3sLXgc86-9Yo-2n7PCOOec2x1hSjahZJ_bjRS_8jaPBWdspxBeIsKmlBGZ-Ixc0gRP7egvVcFHWg9fNWrOlgTNAmvQnuebkZyxgZ2qFlX5KZLP82b_YL2f83R55CS4BnPOCgSO4evbqgkYR4tlz8GkFu99x6OPGx6CwfW7w7437dzIagpchbGdp2JlBFKWBkiW-lPUL5KNJRR6c8Qm0k6VnAuEvOLJWcIGCjHTqtlmeOyFr6i9oSfTorWIoeNlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قانون 90 به 10 در دربی بالاخره اجرا خواهد شد؟! بااعلام‌رسمی‌سخنگوی‌سازمان لیگ، طبق قانون باتوجه به میزبانی‌استقلال در دربی 107ام 90 درصد ظرفیت ورزشگاه در اختیار هواداران این باشگاهه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/28467" target="_blank">📅 16:04 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28466">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njDBrIlcaMXdhiag_iERLiRkykm__lTgEIc_vY8EVZyXSBpSYsDBy2oJwbne-y9NqE77K4QSl_DSGHxdmW-Eq1mm2tJesliMrrDQSYH_iZeO5zorhQ4Rm0C8qNL3Dq-MgKJvfSi60CFt_9ya3BZEXuvfDNBhD6rV8v0QwkQwRnMNT7O7ldcssQiBIWJ6I9S7vR6O6nZ90Xv7AKk0oyesZRT_T5wwuDLh6U9P3cppSIMrSTKZEI1s0SneCRwEboLw-Z4s1pKCuvvbBi4c92QaQfyCr2dhT5Rkr5TeryMAL0IDZO2jF2JlYhQvAOeR7-bOByZKBDsUv419fB1Zm8HyfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عارف‌غلامی مدافع‌میانی‌استقلال با قراردادی یه ساله به ارزش 8 میلیارد تومان به چادرملو پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/28466" target="_blank">📅 14:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28465">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7KpSX8cDhXkSv910LBXxISHHVUbzK8pCUA4G2feKclRQifedwVHNzZZHLRlFVALPQvIOiF7g7AnFW6of6c9ApbWXFkUHV01L_fWWI9A29_R6LYxOjSKRtRff1L78fFMNRMHUC69CQpXWhdpUkkHuq0ZINqVH4z8zId5WfhvKmFj1l6uXqX9nVf3VJ3CCxyE3O9r5Cef9z9OtwYVVCUzNaptPQre2ExyLnszvoMe85DTp7LGlBEwcd7A86rZr0QY-VnL1jZ5Rikdl96GZ1WIMvTf4WXz_ajrz8cHs3Vz3BXxNAI2QLmj_nFNON5nNclQLiaK0-rA76_DhwxE4eKr-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
خبرنگارباشگاه‌الوصل:ازپیوستن‌مهدی طارمی به الوصل خوشحالم. او میتونه به خط حمله تیممون در این فصل کمک کنه. بزودی با او مصاحبه میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/28465" target="_blank">📅 14:13 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28464">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rmwqpMzc32aYVcxGYynLpFEwjDeGO7IpQHt_9xU2O9ybJmb90Tg4waGKqaFI1Umb5NNMJj4sUzkgtycYAIqgiDZPZ8w5zYbtw3W-EcZa1dYmYYVSImpGk4jAX-wqYoPy31WB5HQGIa4iD3o9apHzHuYJjWmnYPNqlrtExqUD3sKUaYCG6XuboXLM-HgUHWwaytvW_SmbrNZuEgUv1R4CmoU9tF3cnUPELVGnWIEe867QX-rAZ2JhFyCg4jqLGRsNSXbW2Y4jOe-tEjvBz3-wAKc6fXgRftbatKpeu_6G6saKLjjZ5RmUm5E-s3oOL1_OVWgZAkghEHP_lC28lhT8jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
هایلایتی‌ازعملکردفوق‌العاده دومینیک لیواکویچ دروازه‌بان تیم ملی کرواسی و جدید تیم بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/28464" target="_blank">📅 13:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28463">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uudu4SkOte0DKMaBlXzVbkaz4QJ_Gj4ezw3BKq2ZpfdIJBTFaVGT-7SLFf11R-uiYP6EON8rVPmQkATgcvIu4EVoMWMUwaSbTPLx_Kdvegsq4fiUUicTVLHjbdWiJHm-qLa_t_FWDm4zesWMhyApIFmehRP3UlCHP3d5g5-kisouU0M9XQ8w6-Z6hgZgs0drDI-YhPWcJfOAnU0HREu1lEYf7ExSS-FAv7zfM5lW1M3sh9qtphTRSQhfakI_wDZYWqKojfAYl3AhFcj3G5rSJJMOUnZEzeEwe6qcUZpbWe0ACZNIRXClkfmcAaHK5WiWpjJB8MIrtIaH9hvCfkG5zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توورژن‌آمریکایی‌فصل‌جدید عشق ابدی یک دختر ایرانی رو دعوت کردن که همه پسرها عاشقش شدن؛ اینم رفت همشون رو به ترتیب بغل و بوس کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/28463" target="_blank">📅 13:43 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28462">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cf16d76a5.mp4?token=fmPYBmwVbGduoKaJvXhbqWZzl555gOUZRroWPGxp6u6b5PMWKI7Q2Z6bRRJMsd235dq3Hn6UkBycHdFvlElmHjiAlaeV7RybyUmKSSqb-6yvLsyJC7T810vAS-fbx_XyrgHJuScSj8v1myfhNyj1u2a-X9eUua5G1bFgWsYgLnSZkOl359hopD1Sd3jQJsknfmhWgqU0LLZyhzmB8hbm15xlCdN-qiN7EuVixTHuNsxwK96Ly6-KOZfIGHcHfg--F364mhu1Pxf4uuOty9mQ2AnvEOPVTyJrTojD-j6BJRaohVFP_Xt_0QEmoJkAMJUQYbtZcYl43e7cD1QCjOYzsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cf16d76a5.mp4?token=fmPYBmwVbGduoKaJvXhbqWZzl555gOUZRroWPGxp6u6b5PMWKI7Q2Z6bRRJMsd235dq3Hn6UkBycHdFvlElmHjiAlaeV7RybyUmKSSqb-6yvLsyJC7T810vAS-fbx_XyrgHJuScSj8v1myfhNyj1u2a-X9eUua5G1bFgWsYgLnSZkOl359hopD1Sd3jQJsknfmhWgqU0LLZyhzmB8hbm15xlCdN-qiN7EuVixTHuNsxwK96Ly6-KOZfIGHcHfg--F364mhu1Pxf4uuOty9mQ2AnvEOPVTyJrTojD-j6BJRaohVFP_Xt_0QEmoJkAMJUQYbtZcYl43e7cD1QCjOYzsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فکت؛ عملکرد حسین‌ حسینی دروازه‌بان سپاهان در تقابل‌های‌ خود با استقلال: چهار بازی، سه شکست، یک‌ مساوی، 5 گل خورده. 0 پیروزی و 0 کلین شیت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/28462" target="_blank">📅 13:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28461">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LD4f2_swCuOaxNgmSbfiEgJSlos5qGrkpii-pIu_3n3_jSM-1ttKui4-YX2z-HKSc1O9IOrJlcGfQhiDpI-DWqPkfpvH25M14piNxAEjCU2YAAfmkUo_o8cbocz4VusHoRp_Z8gBL8Fudcyfq89iWRNxb9XAos2_YU9ADJGiKOIXzU_byAYMnPUwNO8o-u5bBcguQnWQ2G3ud7wK4UjQe7XKhMIwo7NmLGDG0Em9dBTSthZeXFQCrZfLNPMOpq5bZ_fRec-drJ92MWdPtxZtV4O8R62UVShHZ7rN3IU7WAS76IA4UqrlnqJHCctUjriKWf_-04v4lrtgYVBuqHQ6kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💵
🔵
درامد باشگاه منچسترسیتی در این پنجره با فروش ستاره‌های این تیم: بیش از ۴۰۰ میلیون یورو!
‼️
ساوینیو ۹۵میلیون‌یورو؛تیجانی ریندرز ۶۱ میلیون یورو؛ رودری ۶۰میلیون‌یورو؛ عمر مرموش: ۵۸ میلیون یورو؛نیکوگونزالس۵۵ میلیون‌یورو؛ جیمز ترفورد ۴۶.۷ میلیون یورو؛ آکانجی…</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/28461" target="_blank">📅 13:02 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28459">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XjqS3h3Wy78PEg98njPdr047VIq5Gkx_gvhb2HKM7kT7Qg5yCsPpFN2WpALTBVplVwnDakarn-fQym71JSThRXvv-QvARrLzFY2PfxZlqSuteZE8hryiVuFx51CJsYGWsexIvdN9GtSfRKjnd_vxr0K-n8h6Nr4m3PMEAGbTYALcUfKouFQUv1yR2YtRnwA0WtxZ5QSS5oDabRg3M46H6lnJV_HEZWWVI4EYQg_rvkBUJP-tpEnwP0gnZQaWxTSt_j3oW216fZE3OoYXr6W0RGq7iZX-tVo4pzuDzOGlm99GXf1wcT5Ca42e-NjE289A-qcneQQUimXIsPKi-Lg5Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dFoknxKhDJYO8xZDE_0pIIGXojGhPh6QmlhZL6ESOR0TgQZ_qhz-ld3iDre14lyxlp4BtqCGbahatZ-7N1lOWwNGuOM93gdsKkOKB7VL7IdTtKHMdY0mKQmnceGZbmGrBoLVKkk7oV-sUSUVkfzUrYFiNPSc5cwT2E_0Pr6JiDP_IedNzSxqEfNRhBkdScqwKAmrDHwQdsbPiE-eMOx-6pyioxSVhESqDBU09OGfKdR0CASGhCUMToJOPQIFgzWox2EH3_76nr8Av-nbHSK3XnDAyaW0V8Gsi0QEZeX-6ZS2ePz-IYwgwOI4usQWkcFtni8nviuDU6BvJZzSQK1s8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
از مربیان آکادمی لاماسیا؛
که حسابی به بازیکنان این آکادمی رسیدگی میکنند تا ستاره هایی بزرگ به تیم بزرگسالان تحویل بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/28459" target="_blank">📅 12:43 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28458">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b364f5abb.mp4?token=Qj438S8tJJ47AQ2MjbrOpyMirPxzTvTPK6f_nsIfA2l0hFl2HuM71njlvNmIOGzRaYBDkrZu7qsZ7xXhbuDVx2wcQ6T_fSQRoaXYq77gqgpnwG4QCTlctyrapllzon8ineFDD5oObpT0Is4BaRLIpa-9z5JMg44X4rxy2-6F76qmgK9-Fcevp8jzVybwXop-V7K-egK1-3Nj2LL9rQ1ysvuCCELPcmb5hRUfsKanHEbYoVZWGN8CP01AZma9x6aenuh34nOXTn4P-xEdBAtdqimqAtxS5Mj4fjZgcxYYC7y9jc2VmmkHhCKlpei7whL6qXDsPRwhMXsHk53pL_CAjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b364f5abb.mp4?token=Qj438S8tJJ47AQ2MjbrOpyMirPxzTvTPK6f_nsIfA2l0hFl2HuM71njlvNmIOGzRaYBDkrZu7qsZ7xXhbuDVx2wcQ6T_fSQRoaXYq77gqgpnwG4QCTlctyrapllzon8ineFDD5oObpT0Is4BaRLIpa-9z5JMg44X4rxy2-6F76qmgK9-Fcevp8jzVybwXop-V7K-egK1-3Nj2LL9rQ1ysvuCCELPcmb5hRUfsKanHEbYoVZWGN8CP01AZma9x6aenuh34nOXTn4P-xEdBAtdqimqAtxS5Mj4fjZgcxYYC7y9jc2VmmkHhCKlpei7whL6qXDsPRwhMXsHk53pL_CAjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
اسماعیل‌قلی‌زاده ستاره 19 ساله استقلال:
باشگاه سپاهان به من گفت یا قراردادت رو پنج ساله امضا کن که دیگه حق تمرین با تیم رو نداری و حتی اجازه حضور تو تیم آکادمی سپاهان هم نداشتم|قلی زاده در دو تقابل اخیر شش‌امتیاز از سپاهان گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/28458" target="_blank">📅 12:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28457">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYoJsQgLvLnisGiD_BgFs3SJr5KGtcsNXUq7MkVAtLTDDsOFbA-S5xZC-t4I2V7YnutHL7aSMUVCzcvGRx7H7avq3tc1EIyUL-nH8bueaZWvcdVo1b5f-HAby0e9r8O7DIg8x59xgjbQ896b0sgmAaEiaZjW65l6VcWeZs1HlSWsS_U1FV4ANRv3QMvwvG3jBDUH_0ItapXzCeuh_bddNIKruCuSh5StteDqO7m66i7yTNWSB9VUnXw_DqBGDiuOyysHXkp3rMR-LvmYe-qMYnc6k7VwjDwnLSqTYreQzOE5nlxiGrAzATxjTauFo9FHAGiePSEpXjeb_CtaJEs_cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
با اعلام خوزه فلیکس دیاز خبرنگار نزدیک به پرز؛
اوسکار ناسی مدافع میانی 21 ساله گرانادا با عقد قراردادی پنج ساله به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/28457" target="_blank">📅 12:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28456">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wmk9f3JZ-GU6MtfEqPpSn4pHFW24PkwRoDuMsuV2KLYqO5M4k_bkZUxs9BuD9IjhD5I5sqwbNIyZ3BiQ9CYEdFHHd5OYO8dN_RTBMfx0auE1es1ZT3VxKwFifthhTGUIhM3Xd30GQ5a8vmycj2cm0fYKEsYfKr8Bm80qsifhCZzH6cNJiUUJd2TkcD-ru3DLmUaxhR_Br7FIX_bVJPaWkKqzYXMK-Zxp1Xp4qiszcJdufUfr7ZSyCoxVPrBOB8B78p1EnUmREM8Uy7k8ctj4nkr8S0D6zdVf1ycXTv2TTsm9M5JfCc6MRE9i2MK_GDyOtSTdufL5g6CVjYYuWXq4uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تعدادی‌از حرکات‌خفن‌و‌فوق‌العاده برای در آوردن سیکس پک‌های شکم درکناریک‌رژیم درست؛ تو‌ کانال دوم تمرینات‌بیشتری گذاشتیم اونجا هم جوین شید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/28456" target="_blank">📅 11:50 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28455">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JD_epd6uhVxKtsT141u-26Q8a43G8RiXoR2yNh6eyZD0VLR_zRHI-IzlCI-8oZC-FT_IWe7EAeHZfi1vkuhYAVj7rmLB6WkFGExjH0LYICxOW2ZGmugYsaOLPow_yfnLcqsZWvvkCtxgHOFmtKZlDmjBI22aHb6qU90qqGqekjxzORpvtv71C-TK_LhBBOeEhwDJIiHjdkKBWHupxghWFU3_GrRsbZMO_ECvB7c2QX4ULWQiVavCY5kgOclfF9yo8qVnMxdCW9yT1ctsIPPG5nKbsEAUdWphk2nbum4WUEODTFS0YzqonAM7yy2rLMsBLEzW9g6P_DtNiLwNF8qh5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حمیدرضاگرشاسبی‌مدیرعامل تیم فولاد: باشگاه استقلال یوسف مزرعه رو میخواست و مذاکراتی هم بین دو باشگاه انجام‌شد اما کوتاهی باشگاه تهرانی در پرداخت رضایت‌نامه و تاکید آقای حمید مطهری برای ماندن مزرعه باعث شد که این انتقال انجام نشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/28455" target="_blank">📅 11:38 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28454">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYSJdOZnDI4G_MDWz_fc4HgtycnsYCRr_-cqQnWx853owMGO-KL2MGXmrRZt8Fjs4csHMTZ5V0aFExNpyUTKPOU7czUwDyjVbI_f_Zv-rzRC_ic6orOpOcl4VqyTqQufOAmPs72ervGpFd1m1K95msvX9S6FECqu-gQIJxGOy96J_Ak8OXe2_xYBKY49F2ImeUknW68AQkF4R1SzcIx2WVtXCZt3HXkB2mVVkp8fHnIsedzOQfJf6nbWTJBQx1QmOZr2AjbDJR7cG-zhEkFAw2stbHa-PdR9ealZXpmHzghIegYXtghSWCjdNpMaReWVEIgbGyEoPfo3cuu4CourAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔵
#تکمیلی؛انتقال‌ ماهان‌بهشتی ستاره 17 ساله ملوان به استقلال اوایل‌هفته‌آینده بعداز پرداخت رقم رضایت‌نامه‌توسط‌مدیریت استقلال نهایی خواهد شد. بعد از بهشتی آبی‌ها در تلاش هستند که انتقال فرهان جعفری رو نیز نهایی کنند. جعفری مدنظر پرسپولیس نیزبود که بدلیل باقی…</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/28454" target="_blank">📅 11:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28453">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVkGCadP0m24TY4dRhZwB3pXKmwUIMnJ9XqcKDW_kPFegzCdZVwuzgSc9BBp2XzOm5aJwnE8msIdmQJB_R1cwDehpvKeDCSWCpyO9x6y1xCHxwigH4HCJ8Ij1M3NxLseOQxwDAZUnqx_P_A6GBo3OISj2b47Anfk1PbxmxA9iQtKNkUKYRGbUV68-4f7EUeJtXEvSowPrd7cgS7zx8BEGtbL6xKmxVZZScuBgakwZfc1fZf5BSUCbXQlRZz791wLpBsgETS9qGcOn7FUy8ji-mHsgDn2PSOScXsHvVUixpi6PcZoEWbILTUrkNFmZPIfFi4e_8JTfTYyHahpBt4Krg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛‌سران‌منچسترسیتی‌بیخیال انزو فرناندز ستاره آرژانتینی چلسی نشده‌اند و مقصد دارند به هر شکلی که شده او رو به خدمت بگیرند. انزو در بازی اخیر چلسی از سوی هواداران بشدت هو شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/28453" target="_blank">📅 11:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28452">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGP-fVo6PmKsMwe7F4DWYcuoNwKzwTBFTtP5H1fbZATpcv7zY47svH9C2rZH6AiDEWBlnuytA7Xv9Dm78yItbEa1Df1quIfv2K8KqpbT4LWAxCqoNF49pNnbXZBGnLhs7QNwIqzewgNqZQ9AWfQwgpGwYKq2Ovk0zahr2i7CQGWTbKO66idMdvUi3ZPHoIjysdYei-R7N3kOqFLjv4Tr3mDbpdg0OtwmF3K5Ld-q2G1FT8fmeGPwMRzBwbgRIPeJH9XMS1mVGshVMXbwGzc-5X9appOWfC75GT4RrsRvAgKYPy9FFj6u3tUByI8kXU0utszkKA-9aGps0l78Je-RDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی‌تارتار سرمربی‌پرسپولیس گفته ترکیب تیم‌من تشکیل‌شده از بازیکنان 22 23 ساله. براساس امار رسانه‌ها میانگین سنی تیم پرسپولیس در بازی امروز مقابل تراکتورِ نکونام 28.5 بوده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/28452" target="_blank">📅 11:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28450">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJdWE9PT2qQdIp5FZlnVy47gOxCK-jXvI2O7SG1LJ7pS3g61xDJwSJH0_vkwL4G6D5VnRl3XX76wMr_9ikyj5J85Whf6ijavKSvCCsSLBJfCRQmGM6h1tN5vf1CKuVtzQP1K9kkZ8cfEfJygRGyL1CVhkIilPun3Z2_brIl32KF3gCom6gQSyLsOXlNQKJhZrsIjdQE01DmhO66ZTFTEipOPDaKT1G9NJ0SKZhcO1wjvSLfQVctMW5VlSi4FVtq637q_IanxnodVnBLb66gGFn2C7nQudFDxe3WS2M56-3X--eNq9lB2s5Yaw08VoICPpO9abWW-ONDi9rYcenlgtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نهایی‌دیدار روزگذشته تراکتور و پرسپولیس از نگاه‌نشریه‌متریکا؛ محمد نادری مدافع چپ تراکتور بهترین بازیکن این دیدار حساس انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/28450" target="_blank">📅 10:42 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28449">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/039b0e1735.mp4?token=lei7Tg08P-xyo9eEnD5MSIEHavkEqzRv8aTs74lz8r_wtXTKSQDHheuDAa_mIjbV197tVvv80UA97KsQwRLhqeUUxQzZRT38upOcEfj8bC2ZQ9mJlrPYigJYkV-wEkPJYss28Pznnd9aTErNks1NylhbXLcLi5JZ78MR3d4nrUxIBkLRYkcSGTgUkcZr266pb8vxTaLr-tEH_mr0pbrS6DDBoSsHRWmqWR81WUQ1Mn8rhjFoolo4wkLLXyikfICwj8Gr955R5I7WJ8yDwuZIlpMkfXxu7kkja9PLh2C03T-E_vcMcMllKnLsal8917LBb6K81Idp_hS8PKTahc9mug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/039b0e1735.mp4?token=lei7Tg08P-xyo9eEnD5MSIEHavkEqzRv8aTs74lz8r_wtXTKSQDHheuDAa_mIjbV197tVvv80UA97KsQwRLhqeUUxQzZRT38upOcEfj8bC2ZQ9mJlrPYigJYkV-wEkPJYss28Pznnd9aTErNks1NylhbXLcLi5JZ78MR3d4nrUxIBkLRYkcSGTgUkcZr266pb8vxTaLr-tEH_mr0pbrS6DDBoSsHRWmqWR81WUQ1Mn8rhjFoolo4wkLLXyikfICwj8Gr955R5I7WJ8yDwuZIlpMkfXxu7kkja9PLh2C03T-E_vcMcMllKnLsal8917LBb6K81Idp_hS8PKTahc9mug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
مجری‌شبکه پرشیانااسپورت:
جدا از شوخی سبک‌فوتبال استقلالِ سهراب‌بختیاری زاده یه شباهت هایی به‌سبک‌بازی منچسترسیتیِ پپ گواردیولا داره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/28449" target="_blank">📅 10:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28448">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3h4KiTdCv3B9VCxNlHnkZODX-iosCHX-wepMLKnuAgm0IskWfy73xYUHd4gIQ3zP2R1bvAluawYa5tDNjIibtApmwdN6WOr8K7YoKjtdk94D4eHflnorP7dAjJDzvDoDXxJoIMOf26GjtYne2ZSHTC18U3tYT8r_Zs2Ai7uHIQGvxb4lbEnkSUlOh0oZ1tMvCk4pE1DJM8OML3uOqhiebpeL2pU9egXNZoZy_YKsWEfNXWIL_e1WzXRlJi-4z3lZlz3VVTpSI8qWsmY-3FrTIynIgsadmE_LxoHq4TTQNYjcR43omZe6eqpPhcEdszF4tsm3ITkBd7EzBgApLfVvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
👤
#تکمیلی؛طبق‌شنیده‌های‌رسانه پرشیانا؛ باشگاه سپاهان به‌نماینده محمد حسین صادقی وینگر جوان تیم پرسپولیس اعلام‌کرده درصورتی که بتواند رضایت‌نامه‌اش رو از باشگاه پرسمولیس دریافت کند حاضرند که قراردادی‌چهارساله با صادقی امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/28448" target="_blank">📅 10:10 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28446">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T-tXNV5Xu8oukvD4KAiNTuVmHBNPTMueE6vV15EQy2PZ5jPO5Cp71hdr2GqmRrD828fRpHvylZiHVg7_vV4sV1YqbZLXWIYj7V6xXniHtDGC3_3nGmBNwuLvD-cZ9A1pqNhI4AEsZIfW_RZfIlHB8Zer3XUZ2bwtyhXI9wkORCuaQdkE2S02UG_q8YTiVyAf6QE7k3n5CNyBY9BEmm7dM5y8T683X9k7CeNoXFCFSUhU7-RLxy1SGSF4JrdyYgJ-KU2bdGm7OTTk4uGr16RsnHxqoSO7MmIIBP7k9jdxpl4caQZVPKC4EzTG9iOelKSNRF2RqeBzLXSv_Th1Bhln2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iU536i3rO5oz1uMz4VngBXYmq0shaF3RFONyd5zkshDg872a6Rs8yEAC_2zVLvAN0oIMKtt1zm4hSoHt9YhFus1jdO-8Xpv0y26empS85ypidOi_MRl15Sncv3rlFNifhmXt70Xl3XYR0lwnCi1NI2L54wx9TWm-6moYLdaVjMsF_75zUPecnxFbF2tm-6zU0BDvQBeaJwa9KOc_wmEd2JFqgXzm57nrKson-pPRkDQzETOaK2yOYeVby0NFY8LFFw7Qk7dqDs9fi8oXb7inNNIQyyNQyFwWke8hiB3oxOE6qfw1mtdYus6LHYvpPi40U8VUP4MWzIOz5P0m6wzU-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🗓
برنامه‌وزمان‌دقیق برگزاری دیدارهای تراکتور و استقلال در لیگ‌ نخبگان‌ آسیا؛ این پست رو یه جایی سیو کنید و برای دوستانتونم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/28446" target="_blank">📅 09:40 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28445">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f23b0b1a8.mp4?token=SPwNHooRC_5Q_DuaLyg3tGS-GhkANPS2tl99UPVNvcR0EgMn7w7apq7mC56NgqtvyVo--2ZJF23VESmocB_C8R8pe6wRJISYyzCIYwPgHM8HRhLd10Hmn6pRmQSiGXDl7ePi7Xh1EJ6KReyTyXjxJkU_Mt0ni5Ko0dOokmSK1O8IFS2SLd53m0yfdTMsaWmfa_AdXr79prOKxZIL-4o3XLpi44h1YJr6ogBfMVp3MufY-E-KBjYZ2MYDYPedqMAqVBOgpDNZrQjy2vksDw6tq4YO7zYTf7OkJQ7sSvzHj8uugf203L6lH0XD7FrZj6Tj7X9uoJyvky0_0Mm77aFrKwNTVGCbUsLLcy0EzacG4vOCLCd6Y5C7iA5XSOoit97DNRw-cqIh00dpSByij1WLWGplm_T8ijp9E6nxtnSxxsZrrZeU7fQvgspcqtXUH85updr7bf5vewAwmo-2E0vm-IImuPk8yu1TlokfvXSXkuPmXreOT2M6QEYCEK35ubb5_YcMpzMmbSvFDx9PH95tNn8ofTEVOoiaZdY25EKdkmaUjWAc8ZVkoXOxA3tgBB3Tsn2FOOw3oNyJI7Ebt1O_pt-2xl8AhsztUrAzGvqg9cc3SmdTfb8j54qFwOA2zSrEURjldtmhw5D0qS4EW0F4y1RZw_jlOA0VNwc68sbRbj8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f23b0b1a8.mp4?token=SPwNHooRC_5Q_DuaLyg3tGS-GhkANPS2tl99UPVNvcR0EgMn7w7apq7mC56NgqtvyVo--2ZJF23VESmocB_C8R8pe6wRJISYyzCIYwPgHM8HRhLd10Hmn6pRmQSiGXDl7ePi7Xh1EJ6KReyTyXjxJkU_Mt0ni5Ko0dOokmSK1O8IFS2SLd53m0yfdTMsaWmfa_AdXr79prOKxZIL-4o3XLpi44h1YJr6ogBfMVp3MufY-E-KBjYZ2MYDYPedqMAqVBOgpDNZrQjy2vksDw6tq4YO7zYTf7OkJQ7sSvzHj8uugf203L6lH0XD7FrZj6Tj7X9uoJyvky0_0Mm77aFrKwNTVGCbUsLLcy0EzacG4vOCLCd6Y5C7iA5XSOoit97DNRw-cqIh00dpSByij1WLWGplm_T8ijp9E6nxtnSxxsZrrZeU7fQvgspcqtXUH85updr7bf5vewAwmo-2E0vm-IImuPk8yu1TlokfvXSXkuPmXreOT2M6QEYCEK35ubb5_YcMpzMmbSvFDx9PH95tNn8ofTEVOoiaZdY25EKdkmaUjWAc8ZVkoXOxA3tgBB3Tsn2FOOw3oNyJI7Ebt1O_pt-2xl8AhsztUrAzGvqg9cc3SmdTfb8j54qFwOA2zSrEURjldtmhw5D0qS4EW0F4y1RZw_jlOA0VNwc68sbRbj8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
موقعیت صدرصدی که دیروز شهرآبادی در دقیقه 90+6 برابر تیم‌تراکتور خراب کرد اوستون اورونوف فصل‌گذشته دقیقا اون موقعیت رو تبدبل به گل کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/28445" target="_blank">📅 09:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28444">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WeTReWjkc74V_5moqrI0pKnRtG81W7Dhn9Ej49B4DFt9tMgLp-4MEV_qb6us9qlAIodnxkhBNxcfW7xJwklosplbyThGScV9AngxA8XevQzsO6x9Bo6w9XBY1rlym147VD-oSE4KclwYx3EYjA1PNXWoesXvZV_D7ewPQ617yXwhoEW-cOB2cwcXe7UqZiRRJBWHZXYvkdbNVeLSJmKTpJQF42fJODlxazaMN5UEw3TpzaEcQGLEJ-zAfY2TT2N7uQdoclTlI8cUv2W4jiptTSY8X2z3P576IgFg56CSxuVneWRO02nT9xSPcT38f5zK5Q-52NwXb0KgCwjW7qxJYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇫🇷
رسانه‌های عربستانی:
کریم بنزما در لیست فروش الهلال قرار گرفته است و کادرفنی این تیم به مدیریت باشگاه خبر داده ستاره فرانسوی 38 ساله سابق رئال مادرید رو برای فصل جدید نمیخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/28444" target="_blank">📅 09:18 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28443">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RipannZaAjtIbmjWbR1I6GTaU603g2j6DJfh22CVMK4ALcwFlbivD6vY3LY6fiGr0UzvLzHBP3F5x40NtaB9b4rz0Ka1q34NJNgX-eUvLTRJmaMQvazZy05WmQvyDyMJqXVm8uZ8Wn9OgzReo2vpcJzte9CV77OlgR6pv7sgMslIKoOCCnL3zfuV79SKo5HLe5_OJfm9UQqDL05rTRlLXaNxekNEI4vbzUawjxVRkr3ytdcmLsQXddRPPpOjOlzyKreP3h5IDnzzl26Q-a9mqQYR8kDLj8WeBrJvMWZTU6HpWvKqtTdnKNBYN6pI4of90d35ys6YIyd0TB9aJthbWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
راس ساعت 24:00 روزچهارشنبه پنجره نقل و انتقالات تابستونی لیگ‌برتر فوتبال‌ایران بسته خواهد شد. بعدش باشگاه‌ها درصورت جالی خالی در لیست خود میتونند که سه تا بازیکن آزاد رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/28443" target="_blank">📅 01:14 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28442">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e1b5debf9.mp4?token=A3_W8PGQ5re2UG-ElQ7HvbriB4P4WTzsuwshkUAv2DJ51pb26n1f2BCruQCnHFOkkR5w0r-Ke9yGVHOdPlEgkDtDvlhwpXqG2UCtR8ugkrNm7jCW682cAd_KsjA-U9vo9Q2JJv3O0xJOzWriL4uXyTf4gcL0tPiCBQf-qmyc4U27U12Bg7VRi9HgjBJZX90PYlSZt6qMK2Sw1ScYuVtOd2D9-kmMu7mqK6vsuxLZkXjw0i7H4JxKnOZacvOgrw1aJBpo3G4HT8yfO4fVjajDFyD9z6DJ1cLxRPhJm3BhHjkyjnbtHhm_gCMbksTdHpjud_dJLfSS_bQjGEmZE5gmeBr1pvhx4zLDrTP5cAOSwmA-kekg1xQljxCOw46cQPtEN4olMHpV8nbeRDi0QHgf-TdFyeQUrn9r5EnfTcYIlV0RIMJsaUxI_vPp728ysStak-OpS0XU5JwQqGcP-wWgN0fRGHkEiKLn1rWzbpZ_eWeZ39RIC5OgR2hpof_wA8Hho0Xe0gIYyf3dIhRjZPpyUL4_eErzD_GJ8Ljpbjd6wh3jZVb4SywgrXXCN1GayGacY6udL0zqw222NIQerbasTsdaOfCDQizjvA5Z4AcvAaKl83EIPpzzMQxv_vG6ol1MXISta8_ouX6SkK_7MQ0x7Op0HkYuKmdkXIwzFG66eyM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e1b5debf9.mp4?token=A3_W8PGQ5re2UG-ElQ7HvbriB4P4WTzsuwshkUAv2DJ51pb26n1f2BCruQCnHFOkkR5w0r-Ke9yGVHOdPlEgkDtDvlhwpXqG2UCtR8ugkrNm7jCW682cAd_KsjA-U9vo9Q2JJv3O0xJOzWriL4uXyTf4gcL0tPiCBQf-qmyc4U27U12Bg7VRi9HgjBJZX90PYlSZt6qMK2Sw1ScYuVtOd2D9-kmMu7mqK6vsuxLZkXjw0i7H4JxKnOZacvOgrw1aJBpo3G4HT8yfO4fVjajDFyD9z6DJ1cLxRPhJm3BhHjkyjnbtHhm_gCMbksTdHpjud_dJLfSS_bQjGEmZE5gmeBr1pvhx4zLDrTP5cAOSwmA-kekg1xQljxCOw46cQPtEN4olMHpV8nbeRDi0QHgf-TdFyeQUrn9r5EnfTcYIlV0RIMJsaUxI_vPp728ysStak-OpS0XU5JwQqGcP-wWgN0fRGHkEiKLn1rWzbpZ_eWeZ39RIC5OgR2hpof_wA8Hho0Xe0gIYyf3dIhRjZPpyUL4_eErzD_GJ8Ljpbjd6wh3jZVb4SywgrXXCN1GayGacY6udL0zqw222NIQerbasTsdaOfCDQizjvA5Z4AcvAaKl83EIPpzzMQxv_vG6ol1MXISta8_ouX6SkK_7MQ0x7Op0HkYuKmdkXIwzFG66eyM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
نتیجه‌دو دیدار امشب؛ پیروزی پرگل گرگ‌ها در هفته اول سری‌آ و دشت سه امتیازی و شیرین آبی های لندن با هدایت ژابی آلونسو مقابل یاران آلوارو آربلوا در فولام در گام اول لیگ جزیزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/28442" target="_blank">📅 01:06 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28440">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YB746rqL_1gBtfuuKBAHAp3rUYYM9GyfUKv8VW4Ahw3JnrLRlx2XG-f8Y_he5h0Q4yHwl0gYSyavQonLCvmc853HNj1V_As7A4fKQ8xzs8sPwclhJrZmbyyM00Qgna3lRZxMTp0Q2Um45EAMNUoBwdnoJ8x8sFIO_MsZxR2M02Dj2T5mOizzLal9pr5tjbCCpDVwaL613RBaEmCF4NbHG6IAS1Xk7BpAcLsFS8qGJVdtMfJ9rxtSbARVpjiCiKqHDqCyWRHxSILGjvKlMwHw4G0RNn_hyttmzWvVIPEv_9eilgTVTJ6bb_yvlnq_rJb6RTQvNU76toXtPrul3VTTcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌‌ امروز؛
فرصت صدرنشینی یاران کریس رونالدو با جدال مقابل الاتفاق در هفته سوم
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/28440" target="_blank">📅 01:01 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28439">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpqHPbyJsmQCqoQAX8FzR9qb-Q-4c5s-AM2T_Wti_TDXP0x9OxaKeG7aFgCcJLFTo1BpD7gMGBaPkJkR1lQzSohatfTtbsyrmP8ByyZHU_zRRGHgJRZGBCW7ZIgPWlNhKUB_HPjqQRn9LvPxzCymGDxelvDBj9PGm6xE2qo5OUpOqKhfm8-LKfTZPDrp1t6e2T2cUtyvHp5zhS35xN3UipTou4JpfYzKJsYXnAjKl-qAn6_Z4Y94-cdRCxA-B6MOyx5xP-Xbuw7UxkWWb2KlR96k4cTLuRnxW2Z9CAmvtog4bqQVnGrRJjyOUKAs4xuR2UiBAWoTAx_Gl21qBjIOrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدارهای‌‌دیروز؛
شکست پرسپولیس مقابل تراکتوروبرد ژابی‌دراولین‌تجربه‌مربیگری درپریمیرلیگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/28439" target="_blank">📅 01:01 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28436">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5d9ec1535.mp4?token=dMTTn5ga9bCdvWAeqLl-AFit50GMwpEFQEieAXBxgkfPZYaVB06id6YfPm6buQqF9SBnSMXRCDx4TfTTdKb3rKm_aOA-DXGhDm3xUv2W-R9oQv4twIERwrAl2wKEE8u0gfWNlFT3JR7rwKKy1Ka-rTMdYydM11X02vlIdZkHp35U0oORxcCsKiNGCdnlTb3-eG-ZgC64rZsP8j3RFnpq0Na261QJnO-62d6ikS9AT1mSl_8WI3szBWS8RGZP6zYAAwYmW281gg_gN4m7RKeGuU57_9PTQKaL05x0vq6yVCsVJ5atHvuFCeXzFLA3Exn6V4LG1Nj3TSpA75jGShhzwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5d9ec1535.mp4?token=dMTTn5ga9bCdvWAeqLl-AFit50GMwpEFQEieAXBxgkfPZYaVB06id6YfPm6buQqF9SBnSMXRCDx4TfTTdKb3rKm_aOA-DXGhDm3xUv2W-R9oQv4twIERwrAl2wKEE8u0gfWNlFT3JR7rwKKy1Ka-rTMdYydM11X02vlIdZkHp35U0oORxcCsKiNGCdnlTb3-eG-ZgC64rZsP8j3RFnpq0Na261QJnO-62d6ikS9AT1mSl_8WI3szBWS8RGZP6zYAAwYmW281gg_gN4m7RKeGuU57_9PTQKaL05x0vq6yVCsVJ5atHvuFCeXzFLA3Exn6V4LG1Nj3TSpA75jGShhzwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟠
🇮🇷
رامین رضاییان در اولین بازی‌اش برای فولاد به این شکل پاس گل داد و فولاد به گل دوم رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/28436" target="_blank">📅 00:42 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28434">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cATBTAUI3sMtMVTIT0vBPjBkTTnB444eJB8DginZvg00fP_whz-yeDC3JpuAQcUiOqY6rbMFLHpe-3F4r_yXpUzM4KLEAFpxxVA-Kc_afna9a8gFNvOwuzrFZd3fyKlDkrmV0-XFgVYAUUTWZ_aV1VceYdPv3XEu63JXvPlhiqDNE1ASyOPs0eEJaU3VnrmAEqYt_gko_umv-NGNgGrQv2hvLi1ID0CUNkAJItFtzOoq8m24zwdEmoIANZdr5GXwSQDYWkSwO9pZud_aghWsBkjfF6CbzmRhOBzVS1skndOxrG5HF-qv-hG1F6xhSBGzvFr76XiOdOWqYg0vBG3EUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YHgctHBaIwUgBdk37pi2Mhb8yWB6J5pnwEl_wNJSdjnj-6nVG6bjxTUV1yVqFLMfrMmmN2UMkNVFXhNY6BLlIwwmMf2TYz-ftTG5a3AhKBQywPgcgLzaoRvk5aQC5gSCXh0bdOfXMKmCEyEgk0e_hIZo8ifQS6soY8d2yp1KrvNOdmHQ4oqDZNm0df3ia_Qq6LBkHvlzhGiTa5hYJKabDh-tnSmQV_e4_iqjjvL0XK6f4PDeAl9CjwwYF2TnJkDbKt-b_Pv-Afnbt6PiH0QLno38UDKo_weqNEkb_rK3ZZ3kcgWQ49qGnkID7wMXq8AphAJ8FtStk_Hly61dcTqEow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
نتیجه‌دو دیدار امشب؛
پیروزی پرگل گرگ‌ها در هفته اول سری‌آ و دشت سه امتیازی و شیرین آبی های لندن با هدایت ژابی آلونسو مقابل یاران آلوارو آربلوا در فولام در گام اول لیگ جزیزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/28434" target="_blank">📅 00:34 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28433">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIBsWPRzAGF4RjKr5YvPnsXOSUmICdHxRUWgXTa8N2IrgvZZvihXoAatYAf7QRNf2Yv1znajOOeE4nWkSYG7SuDdCe-NYAhzbk-_EQbWSA1gY8VKl4x67anLBOmXa33gKC5VzgCG68EW2T5lp1ZDd1Wd81XdsY-qYEMaHl-Od910QaETmWQK6snIoOtM5WadY9wTi1E4x73IDU4r7wSmgPSoaLie0dD-tDD833qMLNgjcUgkSc4RuIFootrbtUKQBoTbHRxsl8ggp4UOIIYmRzwWWxQ8TCustutdY0Xgs8gi58xq1KdN3EpY8jBmpOkr2nVgQZ3fwUTioCjsUagD9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی‌پرشیانا #فوری؛درجلسه دیروز هئیت رئیسه فدراسیون فوتبال سه نفر موافق اهدای جام قهرمانی به استقلال بودند و دو نفر نیز مخالف. مهدی تاج تا پایان هفته تصمیم نهایی خود را در این باره خواهد گرفت. احتمال‌قهرمان اعلام‌کردن باشگاه استقلال توسط فدراسیون فوتبال…</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/28433" target="_blank">📅 00:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28432">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPT1WLTrN1HaAIt-rt5Eh2l7olx2qrnNSnZeWBLh7jRNV8AzxqWTinGta2yQPqqRzKqG1648Y585J5K7YaCuBjlnOsbtt5SSdYffUsRg1PlpbJfrEjDipJyaZ0PWRgVATVsVyPSkGZbMAYTcA722TE-DwFy_36NgNrc7xSkiSF45HhN_G6wp_fEngL6ZWid8uMY92DkSmNejlsWjpcUDHk3anRWcSQnEzXCo_J6fXSnoQ4PUYqZ3NCA2MgO_Cr-wuwToXNRmuVZtJartTFmjLM23gI4lTEQGqOBlp1xASCHcZjTZtNcpquf6VbcapKlqVuA04JdK5ELfgl7ddzHCJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مدیریت‌باشگاه‌پرسپولیس حمایت‌کامل خود را از مهدی‌تارتار سرمربی‌سرخ‌ها بعداز شگست مقابل تراکتور اعلام‌کرد؛ حدادی مدیرعامل تیم پرسپولیس اعلام کرد که کادرفنی تحت حمایت کامل اوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/28432" target="_blank">📅 00:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28431">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVUkqS1OCkTY--2sNBaHt-jpP6gOR1ICJ3TuqEPS__ub8oeqfRZAOuW-U9MqCr_uzGLpxHcmYjeyXzh-90hXeTuDrceivR90KTLNer1WN1lrQYxNkNT0dRV5T9xp126c6asmGQat78w_CPesf7Yvl5xAQSVk2YMpIKC4_ZbIqA265r98pPKbMCec1KUACwtNrL_x-yjq4Hj6V0zCptgxzpdmwXfJDJZyZcjlg4APcgemNmqys7_xGhBGJhEDprTPZjyHARTLYGv3WL2jPqTLjoCGw3CpQzZvNtbndfJUz99ue5fY-RAQu0qvJCqnyF5GC9p4AGQ8UsyTwGsQiuh-GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی‌پرشیانا #فوری؛درجلسه دیروز هئیت رئیسه فدراسیون فوتبال سه نفر موافق اهدای جام قهرمانی به استقلال بودند و دو نفر نیز مخالف. مهدی تاج تا پایان هفته تصمیم نهایی خود را در این باره خواهد گرفت. احتمال‌قهرمان اعلام‌کردن باشگاه استقلال توسط فدراسیون فوتبال…</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/28431" target="_blank">📅 23:53 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28430">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/206c65214b.mp4?token=OoaDhd54GesUnALItWsdvTeZ0xcjrpfpUE3yuiBH8hsTIu4yRBgLJ6t9SB3Et9hjmvIMShcZeZkMr2-t4Xr0ALhRPz5_eDHcX0HpMhTrdl1j-WbEwCxD6H2pyVULVRSVh_hp3AZRlue9UYX62wFpgeJMjOhea3LCop9BR9leTAUw9S2-d4lvDihCQdY3MPFmNQnVI9h0Ax8gLDxk3DS94BKCdGQ80nsf0DpapbL0P4uSPxnYBgUzqo6CndyvGkgnv67ia8DwHgZUhN-drPrrnjf3NX96AcdXzcS9V3gwIH122Fcdvv3ikN2wn4YP70IQONCTuPsmD6RcdzwveD7yuTEghxBamC_-T_h6pB8J1c3DxyzfRt67dacY2yD1rqHn3QryJMFLcQDVeZzm_AMhcl1TR27OP875iggFMxO3ydziZurlXSuIrH63d_wqs495bzHbnFgFaQQHCRhF1kIZYMBt4QoXGwSnaem8I7CH0AuAsllQX2Ms9IyBZnJnH643kKNM2QCj74qMhT0NAe4CH-XRvOSP2cJQUm2q5bByCvbA0jrktWJItLRFGa-Ti5iT7V7htzqGhs_wfjhvEBybPjuVjUzhYE7aKstBKC57lF5Tq3Q2013GG4vSdSJJzJ7qMD5Jac0SFiO73hxqkoMFxi5d7Rm2UE_GL_QML-VT38I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/206c65214b.mp4?token=OoaDhd54GesUnALItWsdvTeZ0xcjrpfpUE3yuiBH8hsTIu4yRBgLJ6t9SB3Et9hjmvIMShcZeZkMr2-t4Xr0ALhRPz5_eDHcX0HpMhTrdl1j-WbEwCxD6H2pyVULVRSVh_hp3AZRlue9UYX62wFpgeJMjOhea3LCop9BR9leTAUw9S2-d4lvDihCQdY3MPFmNQnVI9h0Ax8gLDxk3DS94BKCdGQ80nsf0DpapbL0P4uSPxnYBgUzqo6CndyvGkgnv67ia8DwHgZUhN-drPrrnjf3NX96AcdXzcS9V3gwIH122Fcdvv3ikN2wn4YP70IQONCTuPsmD6RcdzwveD7yuTEghxBamC_-T_h6pB8J1c3DxyzfRt67dacY2yD1rqHn3QryJMFLcQDVeZzm_AMhcl1TR27OP875iggFMxO3ydziZurlXSuIrH63d_wqs495bzHbnFgFaQQHCRhF1kIZYMBt4QoXGwSnaem8I7CH0AuAsllQX2Ms9IyBZnJnH643kKNM2QCj74qMhT0NAe4CH-XRvOSP2cJQUm2q5bByCvbA0jrktWJItLRFGa-Ti5iT7V7htzqGhs_wfjhvEBybPjuVjUzhYE7aKstBKC57lF5Tq3Q2013GG4vSdSJJzJ7qMD5Jac0SFiO73hxqkoMFxi5d7Rm2UE_GL_QML-VT38I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
#تکمیلی؛ سردار زاهدی معاون‌نظام وظیفه عمومی: علیرضا بیرانوند ازمهرماه سال 1405 سرباز خواهد بود، و باید ازیک‌مهرماه‌به خدمت سربازی بره؛ زیرا مهلت معافیت تحصیلی این بازیکن هم آخراشهه و بزودی به پایان میرسه./ حالا اگه یهو زدند معافیت تحصیلی بیرانوند دو ساله…</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/28430" target="_blank">📅 23:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28429">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9CUzLSmwRlEo_E2BsrVP22PcriTbknPVwS63YiDH2eJBJli1z52llZyVHd_WFNnM-ofrlMIX0uTHu0xrv3Z5KdAk-rt3qRFERTe54iktAeV0fuyp45Lm0_ouCHv1vEFjo7B9B1omRUm_sC7YlFZ8wi0YnwNLXJNAFdZ3cyfQbOJj1p-3H27NuEoIE4FUhkFleqEuj6XVEA98Itwell_uNzscdLPX28c3Go7xi1F5Cnc9mj2WmV6c8pjllMe4pSGzmmN2VhDOdlW_05g3ipU8GP-LeVnTljkVkTOEsywl5iSBVf-Z6YWaRvayj7Od5MEkkcx4WkL45wM3JH1B_PGjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
برخی‌ازرسانه‌های پرسپولیسی خواستار استعفای مهدی تارتار ازهدایت‌پرسپولیس شده‌اند و مقصر این شکست در حساس‌ترین بازی فصل رو او میدانند.
‼️
ترکیب‌پرسپولیس‌بعداز اومدن مهدی تارتار در این سه هفته هیچگاه لو نرفته که گویا به بعضیا برخورده و منتظر اولین شکست بودند…</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/28429" target="_blank">📅 23:26 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28428">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbf8bXBFPp098vBTDqnVexWUCxowbPP3G6uXbjHUpef0scN0bsrTc_lJ8JGCb_9AQ2O2n5eL29aeoClMzDzowTtH_lZbtfla-dYoI4f-XcVz1jbv6ntQYp7PwXCxOMJJNPN2khTuROlX9jIGr1Sjxk4YpWdPKnjBrb_A_SFFKzbpeBmv9kIV5eWe5Emhsjp29nLdqX7o9Mygbv2Q-Jp0Ki98jCqdgGgkRzxYEIDIbgOtO6DUuqff7MD_hWY2KnmT19th19b1u-F9_a0KORwAdd1Ou94AY3cWLIUt55Xjaa8qFl7Ccfr_oK7AnN-DqrZyrl_pVZ07dJqk6SWvna2k9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گابریل مارتینلی ستاره‌برزیلی‌آرسنال که همسرش گفته بود رویایش‌پیوستن‌گابریل به رئال مادریده حالا درآستانه‌عقدقرارداد 3 ساله با رقمی نجومی با الهلال قرار گرفته است و موافقت خود را برای پیوستن به الهلال نیز اعلام کرده و تنها توافق بین دو باشگاه بر سر رقم فروش…</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/28428" target="_blank">📅 23:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28427">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGOMXczx8-8H2SFdBvaZY9juU3j__Z28OCVyLnjnwQATJyW5FDAfuHRp7DdLQP8RluACSTgjaIMovu6tgFqk8YXRStiR1mGF6J2RhicxRcSAJDUA9kXn_8WU8e4iDiIhHkY5mKLYKn192nTXpE8W46x8NEycdmjiHEIYCIJgblJJ7CsQXfSD-9sy1QnsTom_Ma1pYvxjJ3Fi-MHmSbXSwO56X8LOMSolTBg-W5TzqbPko_xm84zA4UB8zvRW_9rfsFfXsj1xog64htxtmd_B7nKeA4U7aqqRm6ogw4a7kiGQbQO8cemqza3ubSzfNDRPsqReOG5abSCYVOourkWX4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌رده‌بندی و نتایج‌کامل دیدارهای هفته سوم رقابت‌های لیگ‌برتر؛ آبی‌ها درصدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/28427" target="_blank">📅 22:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28425">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jxsscrs9ve490SOSBp1OCaQHSvZ3xMc59Sit9zPz6U_eWOE4HqZ_CwQSTEUOZO5Zg4ecgxCKdd-SK3FDMgei8bRmbCznz6JwKnXoc3BjQBRhp41jpIgdkZTzQnIMQrah6kYETRLzPHKnvs9DGYPrGVBMw49xg5Baauh4Bz6Q118wPQRO-bQsF1PAA9TuMuuToBxthSqK4Kua2Gfi8-fCFBuAgwmOq5xy2aYfTKCErhggoVPFOeUxOWFIVt9j-84RRDe0Kgd1hFiRJ46kvJlz_2pZHDnQ3LxkoIKpKsQQZpCcokQioByBCAUVKxynlurQIcCMNr2MwJ8xXWj46PaTcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GsJa54g-mwo9ljAKyeazwP2bNDsLmbs4ocGQh0ac5Be50j5YSaTNxUE2LaP9Vz4nmPdXSkC2mXIxmf67ibmdZOzh-e4xCA7gINykmy1EMFlAKj9CSKdqbJ8GliojZyEMf2R41noRdVhAVUlnL_KUdhppJlQ0wxqCLU14UmuyYXaDMI5YFkSlM_wziU0uwReAz10GlED0dynqyK6vgKODhj35tWj6Jp0TBHKXh1hFnEtEsFVONgTnlIWRc--dOFb9TRKanjw0HY5TqnfrxIMfCwG671764NLSV2EiHYp5H3ZmbX9jSlX7NozEoYtqXlQxHPh3OnFcEOH93s9s0NpPjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
جدول‌رده‌بندی و نتایج‌کامل دیدارهای هفته سوم رقابت‌های لیگ‌برتر؛ آبی‌ها درصدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/28425" target="_blank">📅 22:37 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28424">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7lErCq3fFp1lswAaCVyjS_WiElNDNHcFXxIO3T5HdlkKrFB-hs4JqxoCSyCiOvsZSv4BappS_-824M9lfwZ3pFZRcfZjVzJ_YexJSocJZPI0js9CXhzKft3WLR8VyIxteQ5IaJNN7WFwbYcQdJTGzUug8EfO05uxc-dv7K2NwloZlQSgtnYrxJ2_SiF5Iaj_bErVwKQpmWt91IluZwyOqePhRbxNmZVlV4zUlOMINlFWDGf5Bqbhpjb8NuO6AfpS4pe3cpqRJxIWuLH8nSnMhmcqtRM-Hv-wThhDisyYYVBjvvASoX2ovqRfBhRIo6rP2TYAR0ILcdafUIiWsLPXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛اطلاعیه‌سازمان‌نظام‌وظیفه: بازیکنانی که مشمول خدمت سربازی هستند تنها میتونن در دو تیم لیگ‌برتری‌فجرسپاسی و ملوان بازی کنند و امکان گذروندم خدمت سربازی در تیم نظامی وجود نداره. علی رضا بیرانوند هم اگه معافیتش رو به هر شکلی تمدید نکنه تنها تا 4 شهریور…</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/28424" target="_blank">📅 22:07 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28423">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFOXXWAPdDnsKm6xJEeTeDnPOo2-r2jMjqFwYsFTgfgHmpMweRXz-SCA3o6Y-aYfKV9mvTa7BJ0CWtFaAMzNnC3YiRizCRsxTN-EQFNogD10N7DqKhgxVsm1ry9AeKJ8JpB8pLgbmzHZEaIIRHZDDkH-c_MQhl8a6AqHsd7jG2OZB9-P-9vExnweMWVGR_w1wJg0oS5zUrRgPJiZDqiATRsytAVxzddbuoZyD1GeHXLpnJGEcvKWjfnyfthb_aEeWohIZ50eP65X7qxX9c4sDL2hbz5rhszkEBSDfaG5TVdzzGjzoXCQMvLjb6ZP3UDgDbGHDMEK7DgLToZP0Rrw0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لیگ‌برتر|پیروزی خانگی شاگردان جواد نکونام در یادگار تبریز و دشت سومین پیروزی پیاپی و ثبت اولین شکست فصل پرسپولیسِ تارتار!
🔴
تراکتور
1️⃣
-
0️⃣
پرسپولیس
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/28423" target="_blank">📅 22:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28422">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9gxmaR__9jrETN8uPPeSYSTg3V60n1p8Nx4qsNExSvObz1MR455bhMExgnj7R4XImqM3a0Z88TgbLTJjrqB-i3CbPhWN5Tg_o876TAK4-RaDiPdfcm13hJCc8GaqzdfKfQYsS9H73fb5jucmYs55yadIQ-YbK-6J9CUAspS_VYULK7AsgbeRBLMDyqYXAwQ4b7SFpSMfoGOmNoi2NCy1VBherfwHpb0Zn8J2XoU0UafsPKPWMZtWS2cQC6vSB5IQo_MH1rIFnCJCHg4R_IYmtcSsNzyEeOPu8WQGoVV617cQ6cs6KT5kgXnUmOOy7BO_w3a185B_7nQErdGShep5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگاره از تارتار پرسید و گفت چرا اورونوف و سرگیف بازی‌نکردند؟ تارتار برگشت‌گفت به دلایل فنی بوده و حتما یچیزی‌ میدونستم‌که بهشون بازی ندادم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/28422" target="_blank">📅 22:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28420">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9248dbd6b.mp4?token=fjo2UUTBa18MT39gYg_P9svemHg1Fr19t_vRqt2NzsbzIjT4I6bSciHecqh8T8dNeHeAe6eeAvc1rxdc7Ev7V_fUvl6QO7YJuqqX_7RT6lfRH1pw7HE79kRP6bi5i1zyC0aDfEWL0RcQbGS33JIHsjmdywccH2Xa2Hiv5Gb356-7jhRXui-IAQNl5lQNwIEm_dPSeqNihsExE2Nb4-fjP6ATcoj7ARli30gcRCvVKFQTCTTveuhQ914cbaXRasNnWHXmfgy2aGZc0FPvuTE40q_FAq9km7zMst2GoRZ93GfTrhw9k_EDlZmJxEyAhSk0q3L8AfE3PYLfaL3H7JJZmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9248dbd6b.mp4?token=fjo2UUTBa18MT39gYg_P9svemHg1Fr19t_vRqt2NzsbzIjT4I6bSciHecqh8T8dNeHeAe6eeAvc1rxdc7Ev7V_fUvl6QO7YJuqqX_7RT6lfRH1pw7HE79kRP6bi5i1zyC0aDfEWL0RcQbGS33JIHsjmdywccH2Xa2Hiv5Gb356-7jhRXui-IAQNl5lQNwIEm_dPSeqNihsExE2Nb4-fjP6ATcoj7ARli30gcRCvVKFQTCTTveuhQ914cbaXRasNnWHXmfgy2aGZc0FPvuTE40q_FAq9km7zMst2GoRZ93GfTrhw9k_EDlZmJxEyAhSk0q3L8AfE3PYLfaL3H7JJZmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟠
🟢
گل‌های‌دیدارامشب‌خیبر خرم‌آباد - مس؛ بازی یک یک شد؛ مسعود محبی بایک‌ضربه سر دیدنی برای خیبر گلزنی کرد و نیک نفس هم با شوت دیدنی اش روی حرکت انفرادی‌اش گل مساوی رو به خیبر زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/28420" target="_blank">📅 21:39 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28419">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bb30f0066.mp4?token=ESxXY76zWvgHMtyHfMFt8aoKTYrLWGQJT32miTFG3mvWxeCwQgWRqAuQsqR7krl0va4qTaFLvBmQ7XuSeDCXpE8og3lViZvsVDruNazpaI19niEpLA6XH6TnYmooHPykp-YlCB9EE4pA-V_wmxM4Tosurh61dP-ZreBOkkxoK-2fjAjOulNBHV1EGekA3F5uLYyumqbBliOeYSDCvDsYIaS5VSBLZLTlywcn5MDd-hxeBLFjxkZHVdOl2gZJJuoTgQ6K8c3vdMqoo3ZzZs4GyhVID4PG81_TWXKhtOZub5QaVPw1_Jx_prPyRe8V2ZaOodE3jhIW9WjsP9ZdDPijWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bb30f0066.mp4?token=ESxXY76zWvgHMtyHfMFt8aoKTYrLWGQJT32miTFG3mvWxeCwQgWRqAuQsqR7krl0va4qTaFLvBmQ7XuSeDCXpE8og3lViZvsVDruNazpaI19niEpLA6XH6TnYmooHPykp-YlCB9EE4pA-V_wmxM4Tosurh61dP-ZreBOkkxoK-2fjAjOulNBHV1EGekA3F5uLYyumqbBliOeYSDCvDsYIaS5VSBLZLTlywcn5MDd-hxeBLFjxkZHVdOl2gZJJuoTgQ6K8c3vdMqoo3ZzZs4GyhVID4PG81_TWXKhtOZub5QaVPw1_Jx_prPyRe8V2ZaOodE3jhIW9WjsP9ZdDPijWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
مهدی گودرزی ستاره جدید گل‌گهر: مذاکراتی با باشگاه استقلال داشتم اما به دلیل بسته بودن پنجره باشگاه استقلال نمیتونستم با این تیم قرارداد ببندم. آقا سید همیشه به من لطف دارند بله با من تماس گرفتند و درخواست کردن که به گل گهر بروم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/28419" target="_blank">📅 21:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28418">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e283ffe059.mp4?token=jsVvvC3eWtJLk_00KZ-G1nhdje14bfSfwgcGz57s2C3Os6aS9RjAv4FOeRtOUc8aYNP6VK571iFIVKtyJnMawr3ohR2gSf4XjTs5gGPAZOpM38xQ3I111-aMHk2WyL7TK5vhypN-cry5p_s2wSY339SJjCuR7H5SSSOPuIhrbbFd7RGA05m5wOLfHjLcvaqE1Y_K8vucDfzcL6Ch8dE98phAUCs-IEaCS27UtT1Ge29caaH9mrnkiNk7Y0FKtHPmH5uxsNtonY8_dcBDEwe30h-dIUpAzeB8dQBJHiGtnhUXPF6zJZDCr00oib-_o6A-mFlDhkSYOKL7T6372yH2vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e283ffe059.mp4?token=jsVvvC3eWtJLk_00KZ-G1nhdje14bfSfwgcGz57s2C3Os6aS9RjAv4FOeRtOUc8aYNP6VK571iFIVKtyJnMawr3ohR2gSf4XjTs5gGPAZOpM38xQ3I111-aMHk2WyL7TK5vhypN-cry5p_s2wSY339SJjCuR7H5SSSOPuIhrbbFd7RGA05m5wOLfHjLcvaqE1Y_K8vucDfzcL6Ch8dE98phAUCs-IEaCS27UtT1Ge29caaH9mrnkiNk7Y0FKtHPmH5uxsNtonY8_dcBDEwe30h-dIUpAzeB8dQBJHiGtnhUXPF6zJZDCr00oib-_o6A-mFlDhkSYOKL7T6372yH2vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حسینی فر مدافع ذوب آهن در بازی امشب مقابل مس شهر بابک به این شکل تماشایی دروازه خودی رو باز کرد؛ جدول آنلاین هم پست ریپلای شده ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/28418" target="_blank">📅 21:24 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28417">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AuSXxM9uaLjLHynNnW5yxyN61wZ4O58cLe8aTmdbib_PTcSpk5Damk01G8iDduGvE1_flu20DShoZ1jo39F_27orS9O8iFLb26IOaFL4A2PmJNMoglJsUWsq-ivjG7sFejI-ylh8MuFYO5zQbRB5Hs6Se8p1Jlful97lwVzq1QHSrLRnnid4JUOVz-vM14AkXHv4ctmc6UGcI_KvhcOZPTEBVuIqnDx33x7YoeTCxQNF-5Qn4ZpQSQ7XYn8Te32NLpygMLgJI0rgkDoNyx4BtRml7pJncgm0ZhUqWiO-nIgl6G-wcA3gCWN5rC_mLsQjtNp4R-QkdnEqDj6VUaQa2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
برخی‌ازرسانه‌های پرسپولیسی خواستار استعفای مهدی تارتار ازهدایت‌پرسپولیس شده‌اند و مقصر این شکست در حساس‌ترین بازی فصل رو او میدانند.
‼️
ترکیب‌پرسپولیس‌بعداز اومدن مهدی تارتار در این سه هفته هیچگاه لو نرفته که گویا به بعضیا برخورده و منتظر اولین شکست بودند…</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/28417" target="_blank">📅 21:08 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28416">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87affc8d0d.mp4?token=uPiYzcbEN0SOdxuahE1699e5yTWOxR4PoVDZtFQqM45qyAZtzJB9--Btt_HIdeHCr43p6Zih3V1RIZBRWLtvzJhMb2gsrYitfD-8vHXihan3n1Y8q_QS6dpbEKm1pGcz6lwwgqirS0TImDf2WI3BBWEXeIWQdW6cCT6MNXaBZ7VcxfnwSihbttvpJz6bQ76X_pwqV8gAig4e9O7ubADY-vKCZ0B05Fiwk-N1W9J4wbCUOtFMsbUag0J3veTJlINQUILF_mC_43RTnE8h6Y1vjudpj9-T7TZ0mdxalRppKohuIlaOXqL1bCvdhinWsDC4yAB-pFJiwbQtp6Gf8kCrog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87affc8d0d.mp4?token=uPiYzcbEN0SOdxuahE1699e5yTWOxR4PoVDZtFQqM45qyAZtzJB9--Btt_HIdeHCr43p6Zih3V1RIZBRWLtvzJhMb2gsrYitfD-8vHXihan3n1Y8q_QS6dpbEKm1pGcz6lwwgqirS0TImDf2WI3BBWEXeIWQdW6cCT6MNXaBZ7VcxfnwSihbttvpJz6bQ76X_pwqV8gAig4e9O7ubADY-vKCZ0B05Fiwk-N1W9J4wbCUOtFMsbUag0J3veTJlINQUILF_mC_43RTnE8h6Y1vjudpj9-T7TZ0mdxalRppKohuIlaOXqL1bCvdhinWsDC4yAB-pFJiwbQtp6Gf8kCrog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
جدول آنلاین رقابت‌های لیگ برتر بعد از پیروزی تراکتور مقابل پرسپولیس در هفته سوم لیگ برتر.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/28416" target="_blank">📅 21:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28415">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2UU-DAeywqv2pUvSFJZTNLQm5Y4ZkXV6EthYJsqDPPapP_ncXH1vm5tN16zwxNoIxcx4UeXTb2VHuFjwv5VlopKw4S0SqiNooiKPtzN2c_ZvjCNtENSDsQq1QHibYIMq1ahVUnggciszTXJPMeYzutqlnvQz_bJPxPZEgP6E3qGp1RTeB4LDoFooJ1NhOTu0phjwse8YkvCSa9N8RpaNBsPtUM_4CWkmZ6XxXopMq-pUBEvNN5nhYAmo7JDZFHXBWlZ63cXMH7DiMFZr_T9cWWTP_6yA1xY8pqv3Fo-EFf7FwDm1S7_G7NTrWbbf_yTJBnZZcqq0zgttRH7ZCfCQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لیگ‌برتر|پیروزی خانگی شاگردان جواد نکونام در یادگار تبریز و دشت سومین پیروزی پیاپی و ثبت اولین شکست فصل پرسپولیسِ تارتار!
🔴
تراکتور
1️⃣
-
0️⃣
پرسپولیس
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/28415" target="_blank">📅 20:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28414">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgyPPPJZywqFs406RRU2geptC3KjQqAt75drCHvZ1h3OUuTGlKGL5y6GeYnWUhOLzvN48kyXEuFrdvjd4tGDOEfKXhcUh1RYweNmcjOUQT115LgVo0jhVr8JOHl4bam-g_zzegw42lXLk1knMj9SISLRw_9K7wiUeb7XxqmwEJRkJD-_xBo4hPFQFPqhutkAPiqvZeAk3fWlpvUfuyXl5fdcftfq1S2OBADqR-0bNAzQC9NaaK3ZvwGrF9oz6bw6VHomvSUtPw8DEtEh-JoM5HVAm-gfFkzkY_TFP6KgX70blVmYEdHQSbzcZHWQBg-bPulFwvnI7sgffV87jgLXVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لیگ‌برتر|پیروزی خانگی شاگردان جواد نکونام در یادگار تبریز و دشت سومین پیروزی پیاپی و ثبت اولین شکست فصل پرسپولیسِ تارتار!
🔴
تراکتور
1️⃣
-
0️⃣
پرسپولیس
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/28414" target="_blank">📅 20:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28413">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U67Q_42TRipINzcC0aP78O8RhJf9kAyE6AVcmw9cbgMAuWeNDzCvZ70mw3OrdCCmJym0gMF-qNYwwn6nU2zEdu3DEMdRsVWsw1gq3XlO6gO0tolf2NXs0pNs6xOQF1wFH0bIVUB93nslemKl0o8UqE1hS1HxmxXJichWHAMja-8xPtrPKwwcjnYijtlCpEPWfBRGUoOD2oNLACdMD9P2N03fzfkZXEIK3WIX32ICO-HYh_O-HIPS1ivEZhFrB0sEB8lq7ivsrw_wE6x5RjNJpLpdyMmMvjteDAGW1A_2M4x6BJw_V05RVIhbjsscdmHLFTQ5dz9FjeYVbZDcVKa1qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لیگ‌برتر|پیروزی خانگی شاگردان جواد نکونام در یادگار تبریز و دشت سومین پیروزی پیاپی و ثبت اولین شکست فصل پرسپولیسِ تارتار!
🔴
تراکتور
1️⃣
-
0️⃣
پرسپولیس
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/28413" target="_blank">📅 20:37 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28412">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SGAMCo5wsh9AFpWO-JpSk4skTqS1Vu_YRtvctPSp37dmm23Eyj10zvrb5oyOdOK_bSBlbhJi466A5HZTlB9G7jm2_Hy_4mHub1wxtUoyv_w7tD2NqMloO9r47PweDy8dbXwD6vzgzJaNSdAteEWimDGU_JDL_C_PncwGEkWd55ctI3YaeKhG1h9fVEzPDEXzSVkMId2Pbd1B_5GCnuMBzgONPoJ5m1G7ojLnFROqSl5jaPfJHWtJygE_R1FK_GXpSU8-mCn0eBHhcLF4PdLj9-3DtxqsyABASsxPLAhMWQqKsVPSI149sBx1DgIY_7eSGPAMx2VRkkmbwDKd2Y_M7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمارنیمه‌اول‌دیدار دو تیم تراکتور
🆚
پرسپولیس؛ نمایشی کسل کننده از شاگردان جواد نکونام و تارتار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/28412" target="_blank">📅 20:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28411">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8596f7941.mp4?token=nmibJtm7vUq-m3Nq1qzyrZM1JJw5iYUMf1pv8fferYcBMyYa49z5ZiNBxRo1vyVm9d25d1ELVLl0Zm90lakf6rZgPb4CmZSioy6oEgDh3nDeijK_JWx_cp6sC-CMF-RnGltQMIDxVm3fFsBEQpDhoCCeZc-SVABJOH70haLQth5Su_20CwjmdMEb6sASweb-wpbHW4BglCEHatDrVHLK7Dfcj8CfDlxLCb3YVcgXmi19qFz_thCyDnrzx_l85qZxq4lzH8aonZ-fAO8zFyIfTZpAuqpE3OmmZtfipW6FnNhlxwp1IQ8IKTaWjXySuOJ-7eipUtZ0aFVOpuwwCmvWow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8596f7941.mp4?token=nmibJtm7vUq-m3Nq1qzyrZM1JJw5iYUMf1pv8fferYcBMyYa49z5ZiNBxRo1vyVm9d25d1ELVLl0Zm90lakf6rZgPb4CmZSioy6oEgDh3nDeijK_JWx_cp6sC-CMF-RnGltQMIDxVm3fFsBEQpDhoCCeZc-SVABJOH70haLQth5Su_20CwjmdMEb6sASweb-wpbHW4BglCEHatDrVHLK7Dfcj8CfDlxLCb3YVcgXmi19qFz_thCyDnrzx_l85qZxq4lzH8aonZ-fAO8zFyIfTZpAuqpE3OmmZtfipW6FnNhlxwp1IQ8IKTaWjXySuOJ-7eipUtZ0aFVOpuwwCmvWow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
آمارنیمه‌اول‌دیدار دو تیم تراکتور
🆚
پرسپولیس؛ نمایشی کسل کننده از شاگردان جواد نکونام و تارتار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/28411" target="_blank">📅 20:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28410">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/130f6f7f0d.mp4?token=RruOgiadTFKWr1UNl988_HPGzf1JM5jhJazEntVWcNepRSyE5enaC6ZIidBLFWGJO3VotIngVq26jT5rJhGzOZS-Av6CrJBKc2n34cu8xjgfYQOkk1NOFrGnIFLZuQuZ-RX62zTtyv-_t30nr7jDSoNU2zdeouApxHmg50e2PyB9QCwlskSlS_87x8JDKzT5whyDBXGoREiYowUehuSAouloKarm2sAw2I5MjQHZBdDKrwk8yZmCGvHWhtAo-D-bCUl7G3mBvj1Dl3O3J1FXrXvHi4TZSrmwn3GN1tgKlPll2UB8NLzVA8klvE8L0oZOT8rwGo7hQsyHxo9JV47BGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/130f6f7f0d.mp4?token=RruOgiadTFKWr1UNl988_HPGzf1JM5jhJazEntVWcNepRSyE5enaC6ZIidBLFWGJO3VotIngVq26jT5rJhGzOZS-Av6CrJBKc2n34cu8xjgfYQOkk1NOFrGnIFLZuQuZ-RX62zTtyv-_t30nr7jDSoNU2zdeouApxHmg50e2PyB9QCwlskSlS_87x8JDKzT5whyDBXGoREiYowUehuSAouloKarm2sAw2I5MjQHZBdDKrwk8yZmCGvHWhtAo-D-bCUl7G3mBvj1Dl3O3J1FXrXvHi4TZSrmwn3GN1tgKlPll2UB8NLzVA8klvE8L0oZOT8rwGo7hQsyHxo9JV47BGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی کنیم از این صحبت های جواد خیابانی روی انتن زنده صداوسیما که سال گذشته به زبان آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/28410" target="_blank">📅 20:21 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28409">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56bd5f94c2.mp4?token=i8VijJGOOdBKQNYfuaX2JKoPO0bNhIZ7cEaiCXKVYGfV5XrTnkJGD7gR-e7I-UkFSN0Mu575UZPqX0_Mg6fl1v0vrm1o1l7KaweJccBBGA8MaaIRDFdcfmP9FejEVR7JtpU2GfVShcWpiCNyaubjetBf--icHIl6XV86dKfDSJhvXkRy7q5Lnpcx49s88hWgjZPZ85DhjVw4Cf2ZM2K81TOsljhtbz_SKEnAqBwtADUPgnWoL_Cb0VfC1NddTje2QrPxmqisbLAB9iOqOg4Wp4aVGGuRGxOgrMHj6s5rLMlf00eSoiw8imI7QWvTc04DvCWMPYSm02DB2BlCrukYRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56bd5f94c2.mp4?token=i8VijJGOOdBKQNYfuaX2JKoPO0bNhIZ7cEaiCXKVYGfV5XrTnkJGD7gR-e7I-UkFSN0Mu575UZPqX0_Mg6fl1v0vrm1o1l7KaweJccBBGA8MaaIRDFdcfmP9FejEVR7JtpU2GfVShcWpiCNyaubjetBf--icHIl6XV86dKfDSJhvXkRy7q5Lnpcx49s88hWgjZPZ85DhjVw4Cf2ZM2K81TOsljhtbz_SKEnAqBwtADUPgnWoL_Cb0VfC1NddTje2QrPxmqisbLAB9iOqOg4Wp4aVGGuRGxOgrMHj6s5rLMlf00eSoiw8imI7QWvTc04DvCWMPYSm02DB2BlCrukYRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
آمارنیمه‌اول‌دیدار دو تیم تراکتور
🆚
پرسپولیس؛ نمایشی کسل کننده از شاگردان جواد نکونام و تارتار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/28409" target="_blank">📅 19:49 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28408">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7JSeH3fJ-1oU8_UGj1PCCmxvqiog_snftRNtRXHibZulcXSkl0bECEB-ck-jroYqWMz1mNiBTY_xMZc-K8dpP3SvWo34oNs9TuT0-0tu46NywhjmKGKm1C3zlR2eZwaI-G6V07Rg9kMaUDibeOoHvG6LF0xi7S0_BuF8Kxf-ToKNVwVgEDRKPC3lqtWqryBbj-X9GhZWIPMlu5XxrrTN7Xs6WHSA4T19C_AFjztMUANqHWL_9mJ7oF6gq-tDeTKqBcWkySzqGwzjafyqxtzV6WVVHyPWueNis3ND5bZLRvmBLi-aYQn7jKtUXzonEhubC5WBYk-ac-AwLRqiLYDEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💵
🔵
درامد باشگاه منچسترسیتی در این پنجره با فروش ستاره‌های این تیم: بیش از ۴۰۰ میلیون یورو!
‼️
ساوینیو ۹۵میلیون‌یورو؛تیجانی ریندرز ۶۱ میلیون یورو؛ رودری ۶۰میلیون‌یورو؛ عمر مرموش: ۵۸ میلیون یورو؛نیکوگونزالس۵۵ میلیون‌یورو؛ جیمز ترفورد ۴۶.۷ میلیون یورو؛ آکانجی ۱۵ میلیون یورو؛ آکه ۸ میلیون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/28408" target="_blank">📅 19:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28407">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cfErJMAmDTYKoFWaOgTqr8UJRl7DizriKcbsFdspIPW5dD71OPcFbsJ_FttddvL1S9bZblgxSC-MJea5y-wnkFVI-bYVG2J_TOWkS8mKt7CkE9wo4FmZeoPf5ITx7_jPzWI3E1OW5JdXoPhF0VF4KsEL-bN8VRQyowiQ6g5d4STKUxN_oC_YTBEYCQ8uj7YRc9gs2ptnxr-wets_cIf4PFaa9BtKmVN5yWcfpzLD_1HsJtrw0yAIqpxXS-3Hp3R3lA9uDax01gAxbouBS-j8jBVNK-no4EC1o1MTL5FAZc9MJUKeHqJJ1jhpoP3y0GAtT8LU3plH_RRGfHWmwHdwWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
🔴
🔴
شماتیک‌ ترکیب دو تیم پرسپولیس و تراکتور برای دیدار حساس امروز؛ ساعت 18:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/28407" target="_blank">📅 19:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28406">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HtYRBrB5T6pf8zEL659FkIEaObNOLz0IkWUn-G5oUmD5q2lO5llF4ITid_GV3asnb3BQcyvnliDWuNNuVn9kiJSMtwSyjtTHcEF7g_U2EURrTtyAX9KXYulOEd5-LK-JxG59Ldwmq8L4O5XjtOFJvajxtEJ6BUiPkS4lLIWxixMwowa5UfYaw4fLRhVMpbtkBBHIix5rtZgCUIoAV329YSB2li1WwdS-O1RsbI6zGeJxNQ9f5oRSfvn5bL2X0YHuGKlOF-xUReRN3-A8Xcz-695EPYDefu5sd9FUaYbln3GdwR_IdzyF-YQldEADrtXRcSfnYk46bF8WG62EIY9ajg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه استقلال طی روزهای آینده 70 میلیارد تومان به باشگاه ملوان انزلی پرداخت خواهد کرد و مدیریت این باشگاه هم رضایت نامه بهشتی رو برای آبی‌ها صادر خواهد کرد. تمام توافقات لازم بین طرفین انجام شده. بهشتی تا نیم فصد قرضی در باشگاه…</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/28406" target="_blank">📅 18:49 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28405">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7DMy1edn5B1_Tyu2WlC200nFNBhHRI2a1z9boatLktGmrjS-x_ScHw5ac0nfLHPJkK_FUlMrw_sjxrsab-y9kH9NQJRv1ajhEwFORQcYvSjqBQXyH8-lpyAsIgubOBn1bJW69T8BIASeWygqJaZyBw-S5zv1JlZagEIOpSY5Y7XKBmeZZ-SNn_xCACF7cpLUdWLXKYsKmX1_LXxqkDn_9grYVdpGgwMBUts5OrSvC7UXKsi9x9r2Lyxw1Tl-MqFa-IsLqEZONMAP2glGZCRUWca2q6Oi2hy3LyNJ0KCH6it0ZJ7_5lP197IeqJsDnM8BXMocFTQOqFH1ow4-EGjmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌پرشیاناتوسط سازمان لیگ
🔵
بااعلام‌رسمی‌سخنگوی سازمان لیگ؛ یاسر آسانی یک قرارداد دوساله تو سازمان لیگ داره و الانم داره سال دومش روسپری‌میکنه و قرارداد جدیدی منعقد نشده بنابراین هیچ مشکلی در این باره وجود نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/28405" target="_blank">📅 18:30 · 02 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
