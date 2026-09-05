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
<img src="https://cdn5.telesco.pe/file/Yk_aN2BNTEALTKKu37m1Dux5Gr5Ra3gqdJEQykIzYOz144QoJ2mgzOpSz_fAWDYG83CgDl2FX4JoMlG04Em4uWZGS_Up70pBlqmgTDZzROhnSmqjQ4wRdxjA0C916tKckkdQNes02XAoDy_WmQ0PgDYX0DpoBsSxNc5TZZXdc1Cc4XEGNXZ6F2NpZ5W2BejUkGf1NRG1siFnrkq74Ecz7GYCtldYMqnWEcHC3ZsGLkomT234wkjo7OOarFvMVxb5R-yPoLtx4JNwHlOsUYhYJEj9pPq5Bo2c7R27up7sTzPVVpI2tQoAVm7lorlbGPe3qsHexM1QGe866DPeliOUJA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 426K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-15 00:05:49</div>
<hr>

<div class="tg-post" id="msg-105646">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ed90248c0.mp4?token=txVB9sAZFZGZiMDswJVd0DWVHKoLRoUSNR-bu89yLRbpLxPh6icz0EQHDuc7hI9AiW57JgOGwh44ZyBFqe6N5hWotlXxTY0OplLA2F9aquPqZUoJ3tFuhtmQ4-bKKTzdVLl9Zt1zHP8K95SKqXg3n0ki7ZNDBnvNBIitWpUq4CgcfQUTz6SilA2Xkie6hd6feZILoI9swz4FsoZKOaPLiY7tAeho9_Xjvk53vTt35Dvx5MoVeiCxmHY55xhE0DlwcpVmXV9jcCKWi3DvjwzA7wj_4SfPxvb8CFDACKyToP_IFCAQUodZUyXn4JyEJC8G74XHWKuxL8zU90XYJQ1CWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ed90248c0.mp4?token=txVB9sAZFZGZiMDswJVd0DWVHKoLRoUSNR-bu89yLRbpLxPh6icz0EQHDuc7hI9AiW57JgOGwh44ZyBFqe6N5hWotlXxTY0OplLA2F9aquPqZUoJ3tFuhtmQ4-bKKTzdVLl9Zt1zHP8K95SKqXg3n0ki7ZNDBnvNBIitWpUq4CgcfQUTz6SilA2Xkie6hd6feZILoI9swz4FsoZKOaPLiY7tAeho9_Xjvk53vTt35Dvx5MoVeiCxmHY55xhE0DlwcpVmXV9jcCKWi3DvjwzA7wj_4SfPxvb8CFDACKyToP_IFCAQUodZUyXn4JyEJC8G74XHWKuxL8zU90XYJQ1CWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رونالدو از پشت چسبیده به دفاع حریف تا تاکتیکی که مربیشون داده رو ببینه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/Futball180TV/105646" target="_blank">📅 23:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105645">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/deea5a0900.mp4?token=JhG3o9yQgoG6h9lKuMdQfrL7JtlFd0z4dLgspCz9vA8ShMsC-hOpfvERmdJi4eikw65pI5XG-xl0350Wbqcrk_Wg3JHvYKtSrd0Ds5yU6A3mPKYCHCPpb7yrBrEY4kLZt0xTZRjTYZZnUHvxnU93YIYR_K_-iuXgWGzdVorgvMO8u38W6SC02nI3umQL337Lb9NYPCFK3r-Lk4r44UXHQwFJxRObaY0eb3_EwXhjhAvTQWq0Vs8udRSVBVzmlXcZwFwinW-qT8Y8OzOcvrNr5skEeWctmUp8j-YbHcPtTSJDdqYJuaC1_CgD-6ufnB89Zm8Rk3vezUxepPpxedCEeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/deea5a0900.mp4?token=JhG3o9yQgoG6h9lKuMdQfrL7JtlFd0z4dLgspCz9vA8ShMsC-hOpfvERmdJi4eikw65pI5XG-xl0350Wbqcrk_Wg3JHvYKtSrd0Ds5yU6A3mPKYCHCPpb7yrBrEY4kLZt0xTZRjTYZZnUHvxnU93YIYR_K_-iuXgWGzdVorgvMO8u38W6SC02nI3umQL337Lb9NYPCFK3r-Lk4r44UXHQwFJxRObaY0eb3_EwXhjhAvTQWq0Vs8udRSVBVzmlXcZwFwinW-qT8Y8OzOcvrNr5skEeWctmUp8j-YbHcPtTSJDdqYJuaC1_CgD-6ufnB89Zm8Rk3vezUxepPpxedCEeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
باشگاه گل گهر با انتشار‌ این ویدیو نوشت: دو صحنه مشابه با دو برخورد متفاوت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/Futball180TV/105645" target="_blank">📅 23:31 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105644">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a5829c411.mp4?token=Xs0dJDYbiUvwGzza1ts1WrAKsOWsAjvl2B9rKeNepzQzxIfAvcHdFzNI5b_fbytVlf0Lb2hzpRh7xenEpTsUoB3U9oM8cxLGU277wf-eqIwpi7qFJ9IuCzDe8OXNVqHgG2azW6H_VXrGCzsqZ4bgP-4_GS7n3f_7V_Z4pMiGBXwY1kb-N0UtdPnEaQe2Z4t8AOlSEEiKGu705wiAmRDVdQcfZ4dQRoUNUSmHICZytFsjUukHfZ5ASIJ73pgO89inp7wzN-fl8VZZ4bu74iaYlJB4P59LZigPEJ40lBFCOmVaRcpImgnHOX41LJkK2fHAC3VP_mZIzraCod3dllkIaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a5829c411.mp4?token=Xs0dJDYbiUvwGzza1ts1WrAKsOWsAjvl2B9rKeNepzQzxIfAvcHdFzNI5b_fbytVlf0Lb2hzpRh7xenEpTsUoB3U9oM8cxLGU277wf-eqIwpi7qFJ9IuCzDe8OXNVqHgG2azW6H_VXrGCzsqZ4bgP-4_GS7n3f_7V_Z4pMiGBXwY1kb-N0UtdPnEaQe2Z4t8AOlSEEiKGu705wiAmRDVdQcfZ4dQRoUNUSmHICZytFsjUukHfZ5ASIJ73pgO89inp7wzN-fl8VZZ4bu74iaYlJB4P59LZigPEJ40lBFCOmVaRcpImgnHOX41LJkK2fHAC3VP_mZIzraCod3dllkIaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
باشگاه تراکتور با انتشار این ویدیو نوشت:
خطای شدید امید عالیشاه روی پای امیرحسین حسین‌زاده در شرایطی رخ داد که بازیکن گل‌گهر پیش از این یک کارت زرد دریافت کرده بود و با توجه به شدت خطا، می‌بایست با دریافت کارت زرد دوم از زمین مسابقه اخراج می‌شد؛ اما متأسفانه داور از این صحنه نیز به‌سادگی عبور کرد.
در ادامه، خداداد عزیزی، مدیر تیم تراکتور، که نسبت به این تصمیم داوری معترض بود، با تصمیم داور از کنار زمین اخراج شد؛ اتفاقی که در نوع خود قابل تأمل است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/Futball180TV/105644" target="_blank">📅 23:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105643">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2fedf27ce.mp4?token=FOwwa3_xkHFW3gMI50CakMQjbl06Pa44J6sLt5UhJaOVuQCReTmPrn2wFq4DojKY9Hr4tSusyVF_44kwgvktK1U_b793F24AQrwwRIWTaXyUy7-KZOr28lQsgBXobpdeNwg6Fm8fmIk4WFCNz9_ZNcEa5v7r2SbjkmNKrS7ILqnd9g0Qqgh4ODS8p7QXzASHrMi0EH-C-lYyOQX0wT_mjHpRC4GfGYLBWLjI_11N6fYUhAItac6LitQOgIJoMsnaiAuWGn1KhKSdvEKHo49vY74LSpG4MlxSzC6tYUEQB4XRWAKQZ1oN7dPKL9R_ouw7SZb8kdAjvZySHJkAPlGJOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2fedf27ce.mp4?token=FOwwa3_xkHFW3gMI50CakMQjbl06Pa44J6sLt5UhJaOVuQCReTmPrn2wFq4DojKY9Hr4tSusyVF_44kwgvktK1U_b793F24AQrwwRIWTaXyUy7-KZOr28lQsgBXobpdeNwg6Fm8fmIk4WFCNz9_ZNcEa5v7r2SbjkmNKrS7ILqnd9g0Qqgh4ODS8p7QXzASHrMi0EH-C-lYyOQX0wT_mjHpRC4GfGYLBWLjI_11N6fYUhAItac6LitQOgIJoMsnaiAuWGn1KhKSdvEKHo49vY74LSpG4MlxSzC6tYUEQB4XRWAKQZ1oN7dPKL9R_ouw7SZb8kdAjvZySHJkAPlGJOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
مهار شوت سنگین رونالدو توسط رایکوویچ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/Futball180TV/105643" target="_blank">📅 22:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105642">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/267551e507.mp4?token=Z5w_psgeo2Y06nuyFXU-Osz3MCugmvT2Hy1STBvXNeLqZnShdQIw7nMRo-DzflTwMfkR50Crx2HMICujCTRBjSWN8MKKC1D4jDNiLWRkK06f979IQWaK4zwS2Dtu_ffP5X7_kYpd8jV4hpF8QcM2qUBxgO764cG4dBqe5mszGEpZj6IpYdiNVVDqHSeOM_MqRSQvpRfr3yMHHfUES00EwLcHphs6I-BIClA0Rx_XGN2cfbr3aK74FcsxqTO89se82KsVJYMqxecHviXZ_OSbD2_Rm6yflBfafYxMfo8EamVRncA8w_-Ifx13RbmFLB2DIwBqC2SSgJZY_ZJBnq3iYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/267551e507.mp4?token=Z5w_psgeo2Y06nuyFXU-Osz3MCugmvT2Hy1STBvXNeLqZnShdQIw7nMRo-DzflTwMfkR50Crx2HMICujCTRBjSWN8MKKC1D4jDNiLWRkK06f979IQWaK4zwS2Dtu_ffP5X7_kYpd8jV4hpF8QcM2qUBxgO764cG4dBqe5mszGEpZj6IpYdiNVVDqHSeOM_MqRSQvpRfr3yMHHfUES00EwLcHphs6I-BIClA0Rx_XGN2cfbr3aK74FcsxqTO89se82KsVJYMqxecHviXZ_OSbD2_Rm6yflBfafYxMfo8EamVRncA8w_-Ifx13RbmFLB2DIwBqC2SSgJZY_ZJBnq3iYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐐
🐐
به پرواز درآمدن کریستیانو رونالدو برای انجام حرکت آکروباتیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/Futball180TV/105642" target="_blank">📅 22:47 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105641">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62cb090160.mp4?token=NmmRaz5IJT3f_CcvieqGDqlHmQwT98II1HQINfHesgHVr91YItCTuszf4VSQKjpkbSXQyMhiGOrdard5krJClVNjp1eMJ7Cwoa_yqAUjdieWJdMM59oACYc0-7Q0u4FTTUg7u4vnVFlqnEY7XVO6Uiez-ngoqEBuRGIW52JlUygKyEonLl8ddcjojNqtpnm00WHbW5cIEp6ZwHW9slxJQDIwqjfxXy_e1rkVc79yr4lW-3MMP4gX6j9K-RZQYbSiAnahyLq9Wt4NsRZkJ0u1ykTIoHtmtm8p_2zsnwyK_lJMjfuLsxXGQ1ej2e9jy5sty56ykyn0hOFCJL7Q5QG_CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62cb090160.mp4?token=NmmRaz5IJT3f_CcvieqGDqlHmQwT98II1HQINfHesgHVr91YItCTuszf4VSQKjpkbSXQyMhiGOrdard5krJClVNjp1eMJ7Cwoa_yqAUjdieWJdMM59oACYc0-7Q0u4FTTUg7u4vnVFlqnEY7XVO6Uiez-ngoqEBuRGIW52JlUygKyEonLl8ddcjojNqtpnm00WHbW5cIEp6ZwHW9slxJQDIwqjfxXy_e1rkVc79yr4lW-3MMP4gX6j9K-RZQYbSiAnahyLq9Wt4NsRZkJ0u1ykTIoHtmtm8p_2zsnwyK_lJMjfuLsxXGQ1ej2e9jy5sty56ykyn0hOFCJL7Q5QG_CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
حمله شدید امید عالیشاه به خداداد عزیزی: خدا را شکر سابقه ملی ندارم. من نون بازومو می‌خورم
🔵
بزرگتر از شما هم نمی‌تونه اونجوری صحبت کنه. داور سر تیم را برید، گل تراکتور قطعا خطا بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/105641" target="_blank">📅 22:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105640">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fes7krtB-XoqFR7HVJaeSGqYmgqumnHDDLqfrsGDcBFVXApxOQlxtmqjk9Emg09VyJCrfr-aly4_tqvm7ntpLA0wQ9P787grF3OhFTRt0a9qKpuEwyGB6zyvyufmA6WnVpLfCXL_jsEkcByjCiB-xPS60pJRWEzgQNFBq09_6hGqmrjlX5TE16TTKtLN4KvUinjr_yPY5-pxtjwxltVzAkLUUsa1yh8eBwh9BA4-tARr846TKFxlkgmTEmPC0gn3C-C0T_4Nk8ZUbO5G89IjpJ0GlNyQIHm8aTGw9A3V6M7aBMeASEriCmgXPYk2BmnUCDuR3Tl3ifDsUJxDY5T6uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🚑
محمد عمری بازیکن پرسپولیس بدلیل کشیدگی رباط زانو حداقل یکماه غایب است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/105640" target="_blank">📅 21:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105639">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff5384812d.mp4?token=AsWSuOb5N-5wGZ1CKiBvvI21wd3klBWxQgoL5jOZ_gTS1l78DC0Ca71HK0cjC6DoFHmD1pORtS-GEmLgjcjvQScJ0nM1tUe3N_rV6oJpdxKbSA0FAjtyVgiM9kA6lgSuk6l4-TJr2-bX1GDbqEy5IOApOLRifImEgDo2ULqrRehrQIQ3Hf-FFHziXtpL0XI0Mt0bfjGJS9mG4zg0aeQQUT0dJt9pL91MU0FaNkiWA8pHZ11wlLbCIFeTVMxLgZH_y7CesJROwbWc2snXOY7Fv4YDXrxrbm3celrI3TuM4-d-rWC6-ytQUHYRJfwZUafmiMWtP8haQ7PcSz41LIbKEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff5384812d.mp4?token=AsWSuOb5N-5wGZ1CKiBvvI21wd3klBWxQgoL5jOZ_gTS1l78DC0Ca71HK0cjC6DoFHmD1pORtS-GEmLgjcjvQScJ0nM1tUe3N_rV6oJpdxKbSA0FAjtyVgiM9kA6lgSuk6l4-TJr2-bX1GDbqEy5IOApOLRifImEgDo2ULqrRehrQIQ3Hf-FFHziXtpL0XI0Mt0bfjGJS9mG4zg0aeQQUT0dJt9pL91MU0FaNkiWA8pHZ11wlLbCIFeTVMxLgZH_y7CesJROwbWc2snXOY7Fv4YDXrxrbm3celrI3TuM4-d-rWC6-ytQUHYRJfwZUafmiMWtP8haQ7PcSz41LIbKEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
حجت‌کریمی، مدیر عامل تراکتور: از آقای تاج درخواست داریم ستادی که علیه داوری بازی‌های تراکتور تشکیل شده است را پیگیری کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/105639" target="_blank">📅 21:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105638">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkWFOPnxA2EC4r2PupsxxqySXxLLJsWYC-2kY0YEKxzih3c4yeAocwKsOFCAbmSjd04vGLZBA_MXRx-EN5Lz_zUVLae3NpNo5DXWKaURIz27mTeBBHqitfWzUIsGiCVPCDdL-Y38vnE_nD2zt98v8VF8fkXnbIwil7Dpm8YOY-b16AU8-osoGfYgeToyav82f8IE1OzYBtg9QIkuPjaOs0rWVd90AUDVGNsyg1ZJnKLM3udcCc75ZDoyYBtjm3JjrByuQ_u_yJ95NWswZQMBAEhgZ-OCyx5fSX0ZMlSVyT_trqmtSWK9LhIFvk3l00uRK5r2iWTLU942zUMHsmMyDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
🇮🇹
گل‌سوم اینتر به ناپولی توسط لائوتارو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/105638" target="_blank">📅 21:34 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105637">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3f75618ba1.mp4?token=OdwD3UxE6j1N8IMeRFCiZOORAvB63AyG8QUzYrDllYYSAeMZFNbbB2ogx28cKNZKvhUwA38CYNis5uiTKrUvmoQfeiuv0ZRGbTrZ3l7a5oXtQwFpYGm1cqw7T_1Nffuk5COUYcgLfJP0ltWDybfc7O2Xdr0pEd1PkGwc5u_mptbPJ24cE_K5ozOvQs-7-_6NOFLxNQ3_eDgaxTfQ4eLiDAhFKzVFUw0PmaMz0VdwQaR_iR1puIDVmtwQaOwGIXh8tecX3cO0rBRzYOZhx3O7eaY3zBqJEh6tnlF4psSND_YlFstAyNgR5JI7MiPeL2ckCfNT176cIqbD0cywegzB-HGRIRf-GXYbejhsXElhBiH_UnkMYcidryV4-j-p4PB8WJwDEqLmaeM5sJzoZnztt4KaeMpstIfGt77W9xqVv86TTfVfZhtjB4zlWhQxqX5Onx6UfBql_zTDUA8pASyNHHT_KGzi6JYMbaTbmySWlxP0pWbk0uFm9s684CXqlD1y2M4Y1y2Ei_d2vHRq1Mmz19Oh8DkGV-1lVNSYpM9sGNApnEneq1rKgNkPqcaSX9ZJZQMrQ5BE5Gj_rq5bVYxMJBXdab3gPN2M8WG6hIJVB71GHX5uSs8HYAMTMl099V8xEFL7ZTp4OCsy_xPR4hsN5lFtPB2-biT5ZcJh0JSB59Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3f75618ba1.mp4?token=OdwD3UxE6j1N8IMeRFCiZOORAvB63AyG8QUzYrDllYYSAeMZFNbbB2ogx28cKNZKvhUwA38CYNis5uiTKrUvmoQfeiuv0ZRGbTrZ3l7a5oXtQwFpYGm1cqw7T_1Nffuk5COUYcgLfJP0ltWDybfc7O2Xdr0pEd1PkGwc5u_mptbPJ24cE_K5ozOvQs-7-_6NOFLxNQ3_eDgaxTfQ4eLiDAhFKzVFUw0PmaMz0VdwQaR_iR1puIDVmtwQaOwGIXh8tecX3cO0rBRzYOZhx3O7eaY3zBqJEh6tnlF4psSND_YlFstAyNgR5JI7MiPeL2ckCfNT176cIqbD0cywegzB-HGRIRf-GXYbejhsXElhBiH_UnkMYcidryV4-j-p4PB8WJwDEqLmaeM5sJzoZnztt4KaeMpstIfGt77W9xqVv86TTfVfZhtjB4zlWhQxqX5Onx6UfBql_zTDUA8pASyNHHT_KGzi6JYMbaTbmySWlxP0pWbk0uFm9s684CXqlD1y2M4Y1y2Ei_d2vHRq1Mmz19Oh8DkGV-1lVNSYpM9sGNApnEneq1rKgNkPqcaSX9ZJZQMrQ5BE5Gj_rq5bVYxMJBXdab3gPN2M8WG6hIJVB71GHX5uSs8HYAMTMl099V8xEFL7ZTp4OCsy_xPR4hsN5lFtPB2-biT5ZcJh0JSB59Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🇮🇹
گل‌سوم اینتر به ناپولی توسط لائوتارو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/105637" target="_blank">📅 21:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105636">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8ffHm8eDwE6KH3blBsKX6sXDpea1fdp3EaTVLyxvXWso2n3O26mZC6LzpxwJRuxhsiYAfPC_fpOYC4rgL_pfa8QPz6RNu4D3oUQeB8XfrEm7aqhUDnGJy5DoJNaKXtJES2BVu89nK6oEFusCOKTCB9kJA8yOzgmh1AHqOy6ahUn5mSZubyywKJaXLfT3tp2ryFqrYOkgtJkh8MYi7m_WEfuj5dgNHe3AiR30BwvWxLshg8qljsG4gCybD0s2km1LgIKqpJyJOKIomYz_O9rJ6ToTaEOmQwmlfNyCF4deewDv7rtVvE1Nnqx5fNCkRaf8PkYVe9_OZdjlicGn_vSeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلگلگلگگلگاگ سوم اینتر به ناپولی
😐
😐
🔥</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/105636" target="_blank">📅 21:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105635">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3686a0d49d.mp4?token=CJZkTe1TSuJ91GVq5DWKe9v6QLpIokW7x1HX0e7itQj0KpKWq-i33jJHX6DGe8zd0JAZWA022h6gWiTu1zeo-2LDES3bbYiAFv-y6ZM0Tdg1m_vI-EDkXoUPnTsTarhPN8uwsGOLF6AsGiLEi7K5Dv4R_Nh8XwXEc31_bR_mBbfjmLTKjZ9ud-YqsJu1KCUBGL1nmVbGw1NkDa8Xra_4r6WhuSrMCneelQNxm7mksPCRQm9QKcU8cOFtNUpwbDCI9fGj01wJsQI_D9IBdPCxY9i76p6L2XZpBrJp0iq3CuDQEpxZAPsdvZqVAKqRNJ-IE8xuD7jydZq_-XelvcpUXw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3686a0d49d.mp4?token=CJZkTe1TSuJ91GVq5DWKe9v6QLpIokW7x1HX0e7itQj0KpKWq-i33jJHX6DGe8zd0JAZWA022h6gWiTu1zeo-2LDES3bbYiAFv-y6ZM0Tdg1m_vI-EDkXoUPnTsTarhPN8uwsGOLF6AsGiLEi7K5Dv4R_Nh8XwXEc31_bR_mBbfjmLTKjZ9ud-YqsJu1KCUBGL1nmVbGw1NkDa8Xra_4r6WhuSrMCneelQNxm7mksPCRQm9QKcU8cOFtNUpwbDCI9fGj01wJsQI_D9IBdPCxY9i76p6L2XZpBrJp0iq3CuDQEpxZAPsdvZqVAKqRNJ-IE8xuD7jydZq_-XelvcpUXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇮🇹
گل‌تساوی اینتر به ناپولی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/105635" target="_blank">📅 21:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105634">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">گلگلگلگگلگاگ سوم اینتر به ناپولی
😐
😐
🔥</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/105634" target="_blank">📅 21:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105633">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56515cdfb8.mp4?token=TgzuauekKI3PsKUTFH_hQJbMoUpJn-ad4B3KXPKEDsnaee5ofUGZbl20-C9JVxI8LNREe6MI506-cOy3x86Wz-88AROXeJTkq-Uha2spiBbXqLCl2gJdJbiTJxxQ4DdBmqn5GK_h87UF2c_K3dyfEPMCXmbFkgRiCRO8aVBrPVQ54lluxde0TTtld7HNe18uymvUHxQYWtNH__EzUJWd8SqJlg8ccnDVkm7eStFK7KijtstGYdVRDbfNSr1vnYH_-N_Zr12H4uMVeDbQlp10I5DF8Kv9gsWw9e7peP8zKnOanPYbPchYi8-MKKYwMeBZvEK1A8T_eKN0kzOh6J6MBREKpa4UKtfCrTR1qUoTEEgV9wm3N3D7_3MLHtXNl9ck5vYLZkjpMeSQpplZ4IVOSg8jbfvIrA5n07J7DJMtZuggo_xvN0IpTM7xW09pJhegAFm9QZfoxlcj1PUtpHpg8DIZXxUA4mDDsOxvVjwSQpVS9-y8pVMAB7J2HTGSR0fnLz9I1435FxD60wPugW1Ru8Nn2I3OZivM2Mq6Nb69Iglr4OCh_TFIdYrgKI6DXkYUzHDS9NuNOIvxb2ypFnm98vn1nvP1Mh0dsVOXDU4eIp5Vu5ujcx4-mZq2anwXVoNjM7o-MUrEE8uYEAgHg2ZjAkjSFh4BladG4Top7mOmVLE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56515cdfb8.mp4?token=TgzuauekKI3PsKUTFH_hQJbMoUpJn-ad4B3KXPKEDsnaee5ofUGZbl20-C9JVxI8LNREe6MI506-cOy3x86Wz-88AROXeJTkq-Uha2spiBbXqLCl2gJdJbiTJxxQ4DdBmqn5GK_h87UF2c_K3dyfEPMCXmbFkgRiCRO8aVBrPVQ54lluxde0TTtld7HNe18uymvUHxQYWtNH__EzUJWd8SqJlg8ccnDVkm7eStFK7KijtstGYdVRDbfNSr1vnYH_-N_Zr12H4uMVeDbQlp10I5DF8Kv9gsWw9e7peP8zKnOanPYbPchYi8-MKKYwMeBZvEK1A8T_eKN0kzOh6J6MBREKpa4UKtfCrTR1qUoTEEgV9wm3N3D7_3MLHtXNl9ck5vYLZkjpMeSQpplZ4IVOSg8jbfvIrA5n07J7DJMtZuggo_xvN0IpTM7xW09pJhegAFm9QZfoxlcj1PUtpHpg8DIZXxUA4mDDsOxvVjwSQpVS9-y8pVMAB7J2HTGSR0fnLz9I1435FxD60wPugW1Ru8Nn2I3OZivM2Mq6Nb69Iglr4OCh_TFIdYrgKI6DXkYUzHDS9NuNOIvxb2ypFnm98vn1nvP1Mh0dsVOXDU4eIp5Vu5ujcx4-mZq2anwXVoNjM7o-MUrEE8uYEAgHg2ZjAkjSFh4BladG4Top7mOmVLE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
صحبت‌های جنجالی علیه عالیشاه؛
خداداد عزیزی: او اصلا در حد من نیست
🔴
بیاید بگوید کجا بازی کرده است؟!
🔴
اگر یک بازی ملی داشت بیاد صحبت کنیم
🔴
این همه مربی آمدند رفتند هیچکس تو را نخواست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/105633" target="_blank">📅 21:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105632">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b8b13cd017.mp4?token=ZkkWZO6RDaGIW4nE6eDFWyTMScz-I4VqkkpFu1egxw7I9mku4yIx1EGXhPs00K-O9RJU0jfkLAonSq-_185BVDa4twedgNpbImJz62EifBwy5-dYn2shz8KN3JH3hR-Ugow7AEflOj6iDUyGKNafhQG9uXHVFSeLs2H4RRrIcW5nVt5rbeJX11NHbEvQUYC5IO09XHUwufG7E1TapW5AJdbaRFhkwmbmd76YWp1K0cFvj2HUdebdale7UychUzztKVVllH-GUSnRSDSwfhijTMe2_TaiXhalkCtc4t-LPphkXX0TNFLsy8emnVFHNNGauYVROuwOA0thhlUHet2TFA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b8b13cd017.mp4?token=ZkkWZO6RDaGIW4nE6eDFWyTMScz-I4VqkkpFu1egxw7I9mku4yIx1EGXhPs00K-O9RJU0jfkLAonSq-_185BVDa4twedgNpbImJz62EifBwy5-dYn2shz8KN3JH3hR-Ugow7AEflOj6iDUyGKNafhQG9uXHVFSeLs2H4RRrIcW5nVt5rbeJX11NHbEvQUYC5IO09XHUwufG7E1TapW5AJdbaRFhkwmbmd76YWp1K0cFvj2HUdebdale7UychUzztKVVllH-GUSnRSDSwfhijTMe2_TaiXhalkCtc4t-LPphkXX0TNFLsy8emnVFHNNGauYVROuwOA0thhlUHet2TFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
گل‌اول اینتر به میلان توسط لائوتارو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/105632" target="_blank">📅 20:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105631">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2f3a740412.mp4?token=D4NbPjUW6PZfk3H2ZIfcvDvMgN-W_x2piRAkiqXyuHHUiRLsL-Z7sWMr4qTYFxCb2zTaQzaW8bA3I6RPOVEPe7egEuKZCP2ux7ASSim2yoH-DgAxEoSW5y8w2NGtEJFR-ScWgCa8Mj_J9kuKq54goaUq-FqEhDBWXUMHxcKCKUv0BU2fzYiCNFgFix2defuz5BM9F9GiBHa2tldkMw26fnU8lvjJ3WrGCZCpYhyM18otgVfpYVy9wQhXyx6ne9AzvPbngIyLWBmVA_xFPfHsaq4qMaOYQvKyLNb2zcIR7_jtb4M4u0_Uer80a4MYY9WxBlQpZBWYVRsEEgpxQRjyOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2f3a740412.mp4?token=D4NbPjUW6PZfk3H2ZIfcvDvMgN-W_x2piRAkiqXyuHHUiRLsL-Z7sWMr4qTYFxCb2zTaQzaW8bA3I6RPOVEPe7egEuKZCP2ux7ASSim2yoH-DgAxEoSW5y8w2NGtEJFR-ScWgCa8Mj_J9kuKq54goaUq-FqEhDBWXUMHxcKCKUv0BU2fzYiCNFgFix2defuz5BM9F9GiBHa2tldkMw26fnU8lvjJ3WrGCZCpYhyM18otgVfpYVy9wQhXyx6ne9AzvPbngIyLWBmVA_xFPfHsaq4qMaOYQvKyLNb2zcIR7_jtb4M4u0_Uer80a4MYY9WxBlQpZBWYVRsEEgpxQRjyOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
گل‌دوم ناپولی به اینتر توسط هویلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/105631" target="_blank">📅 20:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105630">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d3255aa137.mp4?token=nljlfyfE_QE_lI9k-UH4JssAXt_47x-hEIi5Av39pKtbsk4sld5dIqEyjVywwMZi9hGhfwhFrnmbxjygxrbVF5KxaMIMhcQ-jWgpDSN31DuQcAVEHUantr5Qxy9JcGhIt9K9XVnA5Y8wv8-Mg6R3Q0WGcJ8npJYrWAKvsuDx1wv49pDP9WZuQ7idj9GOamKskcdt8RXgs39FZji9-cwZwVl4_0r3yGfekpddNxOSQO9Dms430wut7QWAc06vBybVupUDnZwd_kXBjaupoPqdXGxIQ8h1g4caa14eTrbZscq3VPF_nr1Jf2Fxromq05WOe7gBd7H2d8TzSgh-iI-6oA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d3255aa137.mp4?token=nljlfyfE_QE_lI9k-UH4JssAXt_47x-hEIi5Av39pKtbsk4sld5dIqEyjVywwMZi9hGhfwhFrnmbxjygxrbVF5KxaMIMhcQ-jWgpDSN31DuQcAVEHUantr5Qxy9JcGhIt9K9XVnA5Y8wv8-Mg6R3Q0WGcJ8npJYrWAKvsuDx1wv49pDP9WZuQ7idj9GOamKskcdt8RXgs39FZji9-cwZwVl4_0r3yGfekpddNxOSQO9Dms430wut7QWAc06vBybVupUDnZwd_kXBjaupoPqdXGxIQ8h1g4caa14eTrbZscq3VPF_nr1Jf2Fxromq05WOe7gBd7H2d8TzSgh-iI-6oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
گل‌اول ناپولی به اینتر توسط متئو پولیتانو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/105630" target="_blank">📅 20:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105629">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbX4gQce3Ygf9gSnZkOcQfrmQF3Pb_n9EywhZYDfcPcM96zf2-TFdVFYHvAPHc4HlLacal-kOhNEnILR5sWi3UEKFXaodHCmoZyYxII54kY_DpI2MZsjVZGlJZlv3_gsDOci_VtiqSZSwciKhjfjpApCosi54IBxH6O9Hyax4YgDAouY3tYf3JEpKR__eXjnCBejkOjX4zi05XHDvRCH8r8qFCJaN-szMfz2EjSCpBPjCLWH8PZXxKU6GoRju9-Q3EXXQ-LUhDctzR6ddclhGe8vNwko_EVWgkJBPU7n8bhdOj75yVQCGdXN-S-EPxN77InFoJkMILdI8rnWFvg-ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
⭕️
🇮🇷
سهراب بختیاری‌زاده: تا زمان حضورم در باشگاه استقلال، صالح‌حردانی جایی در تیم و تمرینات ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/105629" target="_blank">📅 20:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105628">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63eaffb64a.mp4?token=qCGEhisukerYOVmqFr9HIwu-nBBJj0FUI7xnG6tk-Ii0gBv13Fi6vpjGF86aeswMGUt_ociRIFNmvAJmq_rzbPX6W2SzC6qwXwifpLGQdVoaBfIewoY-67IsnqAoTSmXk1bK-FGRLj65pdVuAI8wsntQnp0p9X9WVm6coOLuB1wzRJPflh_AgaKp0_BroMclAd2Mhz5sp7CMlwxDA0KQ2wFbXTASdbJHq8OublvUL38OzV9yTleOyC-Dms1thngVq5lV_Zz0iBS7X0aAz7Urdk3whk262hreqbUGuXKiqAMPNULZyETs8OP15lJVhvlxbRVHP9v-IQe4vURyi-pF60bsFCc3sZPRMTXs-ySgdA9xRoumea5mPTCTBukQ7MwWgrRhveDl6vTuRB38kpMDl3HBGiXulFMBGIHowQzz4lbnnHJ31pfgNJyzbxVjkfk7L-6hrdljtb8DqhGYc0hDUlLIVlpxXI5Oenthy3EpMsriyyqnlHCuejBGrvZYKFKKZ-GX9zglB_xv1Y3v7UrPva2KGYOqkSEB_0WPPN-nMuqMt-X59Del8fhI178dzBHXhytjUyE4QkgLK9xAC4ZdhljaTcQ9ZNo5oNtUBl37C3g2mNcbZ7RKNdpWx2Gvkd4xNWqShOiznPKEGvYe0SYATJctoNxHVl4boVo6mcGVTKk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63eaffb64a.mp4?token=qCGEhisukerYOVmqFr9HIwu-nBBJj0FUI7xnG6tk-Ii0gBv13Fi6vpjGF86aeswMGUt_ociRIFNmvAJmq_rzbPX6W2SzC6qwXwifpLGQdVoaBfIewoY-67IsnqAoTSmXk1bK-FGRLj65pdVuAI8wsntQnp0p9X9WVm6coOLuB1wzRJPflh_AgaKp0_BroMclAd2Mhz5sp7CMlwxDA0KQ2wFbXTASdbJHq8OublvUL38OzV9yTleOyC-Dms1thngVq5lV_Zz0iBS7X0aAz7Urdk3whk262hreqbUGuXKiqAMPNULZyETs8OP15lJVhvlxbRVHP9v-IQe4vURyi-pF60bsFCc3sZPRMTXs-ySgdA9xRoumea5mPTCTBukQ7MwWgrRhveDl6vTuRB38kpMDl3HBGiXulFMBGIHowQzz4lbnnHJ31pfgNJyzbxVjkfk7L-6hrdljtb8DqhGYc0hDUlLIVlpxXI5Oenthy3EpMsriyyqnlHCuejBGrvZYKFKKZ-GX9zglB_xv1Y3v7UrPva2KGYOqkSEB_0WPPN-nMuqMt-X59Del8fhI178dzBHXhytjUyE4QkgLK9xAC4ZdhljaTcQ9ZNo5oNtUBl37C3g2mNcbZ7RKNdpWx2Gvkd4xNWqShOiznPKEGvYe0SYATJctoNxHVl4boVo6mcGVTKk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
❌
🇮🇷
سهراب
بختیاری‌زاده با کنایه به صالح حردانی: کاپیتان دوم ما باید یادش باشد که زمانی ناصر حجازی، پورحیدری، شاهین بیانی و زرینچه کاپیتان استقلال بوده‌اند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/105628" target="_blank">📅 20:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105627">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
⭕️
⭕️
🇮🇷
سهراب بختیاری‌زاده: تا زمان حضورم در باشگاه استقلال، صالح‌حردانی جایی در تیم و تمرینات ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/105627" target="_blank">📅 20:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105626">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
⭕️
⭕️
🇮🇷
سهراب بختیاری‌زاده: تا زمان حضورم در باشگاه استقلال، صالح‌حردانی جایی در تیم و تمرینات ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/105626" target="_blank">📅 20:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105625">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEfWKDZtZfw3ZlDM9zwIAOr51YNLDYvyD1b4WBvCoD_m4pA5_R_05XNJ4RcLh6pQoRIbvraOifzWZjw6oRtH8zhCJBwchMg8EHEWcXLEQBD76dD8RCUxEMBpRjQyyG8_VijR7SfqAfwilI4CNQWCDmurc5R4E6_pABWL9Fjmy7cLmcjuU3Kracuf0Qj89yw1hQukWk5aBedpXso_9WtMVyOLRT3fz0S3t8xiRYyD0SpTje-hEgxbjwwUYm5spcVYyWd-3BhpIUA3OyhVky1o2Q965mIzuO9FZ70r7pvXt7KS5t9ezkp5gSVnGqV1PJPSDkL63oQpCvM5v6a1UzrrOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🟡
ترکیب النصر مقابل الاتحاد با حضور رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/105625" target="_blank">📅 20:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105624">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QoW86EBi1OjI2oq8P3Gi5aHU7zaBiCeNhn5-2Ks0A79JVidnz0O-dFEhLihHg2mv09-trur3FG6eGIKx_jjnLI5b-g-lfKhDdiY3X8yQ1XuSCj-ciZVKWwkPGzZSGj3oeWpD4WKyWgllDLAm2ahI-aXnBP-RRoNDQiHdg4msgDRlPc5rwFyfO_fTwqUx0G0IcII4wJKotv8EGMwCkMhd3qMFRDE9AUw7DeFCtS3EWX8eMJSVJOAOONWYoHB_tYBwry-S1h9f1QTTTFTVf438G2DSplQNf75_UiAm-djNaCJaez4UBO129HkKqvvLnbQvTmTh8zVABB4QVqrGd1l_Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
هفته‌ششم لیگ‌برتر؛ پنجمین برد نکونام اینبار مقابل همبازی سابقش رحمتی؛ تراکتور با تک‌گل جنجالی امیرحسین حسین‌زاده در اوج باقی‌ماند!
🇮🇷
تراکتور
😃
-
😏
گل‌گهر سیرجان
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/105624" target="_blank">📅 20:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105623">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYet1nlpnfQDAPZHM5ciMCFs0crLSqnpSS31lozMjIrw9O7Bl5UL5ekTiRK7ZGLz5U7soquM8xR4US5hyvJiBavZdUj5BAfBLwQbnBA0k8j_Tr8pAciRlgFCTarxtAVaf4Jy5oqrwFfU6c9MUJWo0ir22b3WqY7z-Y3STRQeMnouADuaz86dK7A8WkIEbf8zO2cwUdALPWmkOrEp18p9aq92qLplnybP7ECNEQ0hu3BEXb4DQwdeIKlJYvyrltDxzJUG9wM71_m9xFgQ_teSLfFHX8JZvPGHuE3XLQNkQM_sW4S515O8KE9CnZm7R6cuNV6lupPyf955iXit9Z44ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❤️
گل اول تراکتور به گل گهر توسط امیرحسین حسین زاده روی پاس‌گل بیرانوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/105623" target="_blank">📅 20:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105622">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgECjQm_s5crvmw2WJwTITd4cuCv0DzKrXRxihGYbr81zI8Nu5P6V-hrwlzF9cHHA0c7lKAYeey94zBWkpBX6OAMDWyeSeTTZ9TymArD6deCB_7Xj-5VXjPNZQE2YhwBK_CflOfS-D5xtaZgWPTw3yt0ce2xrA_G8NMWNIiIyWBJzmSrNNm50rAMh6eelq5gPNa6dVKaKMcuAfdG4ZMSD7IbZzGFCgnTlb6-qmYQNw1d-2_ce2RUsIRy_f7t-llo59bJzVa3HeKH4smqe6jGEaHeR7eCiUvxVTofmUnNxnJCJTH02tZWxchB71hM9iVGRv1yowPcvjYm-DrH8GxOWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پایان بازی؛
🇪🇸
بیلبائو
😆
-
😏
اتلتیکو مادرید
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/105622" target="_blank">📅 19:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105621">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKZfJVbEcBtnjtDoWQhlbPv0Gn1KjDXkt1zFZ8aHBixia9fmf1VZYfVHAD4iH0f1DxWTM7Yjbk0DBXBvlSVq0qtIRTRWwPQeAQHTl1kYhqztRi9i1BfCyxT9wJmskz6HDbw8LoED4RDUKDVPwhkeyoLLeBg4h9AVv4EsiOp21MpBkGAb8lqqDX3dUiW9fkAmIQUsCiJakJ_9XKfROcWenU3-ifrnbYUtlwbvPz9VubK8FcpD3XrYJouO3aTiIH5soMTksnAZfkfgxhPk_nM37aRvO9KRoZRDcZBxAWCS5xXa5Bd8u60_2HC15yS2pbLxqa0D9dW97L-9vksgHZADnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
🇪🇸
🇪🇸
🇪🇸
گلگلگلگگلگلگلگل سوم بیلبائو به اتلتیکومادرید حقیرزاده</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/105621" target="_blank">📅 19:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105620">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
🇪🇸
🇪🇸
🇪🇸
گلگلگلگگلگلگلگل سوم بیلبائو به اتلتیکومادرید حقیرزاده</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/105620" target="_blank">📅 19:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105619">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d35a3e6c77.mp4?token=JIFhASOmQR0UDu0wwXZEZ33UpfWc5It4vZZt41grb8I32wIZHgaT8RoK-Vu3Iu_yMXizTT8-fHmLGu0Cd2FPbEHtNyA6eIvqxdYUeJr5zFpwpZJ4GMJjPZg4OwVDskBBR6Te0FqWMCRbkjdzdK__UhVKkeUj6RevsIhyocHos9YRxEygBXeqjkK-DFHLrxKsvDKViFfHj8QCvB6oipgqsEgNxrP4beun-ItsxoN_VPPCkbkauh6s2FqpL0WHg4wt0AVUcmTYdLK8bFXeJwNHItsKypHOrTdoU6RhXMyz46J6Z5s-TelUJDQGqilJl-fqmZ5M-bV3s_F_24ZjDihBCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d35a3e6c77.mp4?token=JIFhASOmQR0UDu0wwXZEZ33UpfWc5It4vZZt41grb8I32wIZHgaT8RoK-Vu3Iu_yMXizTT8-fHmLGu0Cd2FPbEHtNyA6eIvqxdYUeJr5zFpwpZJ4GMJjPZg4OwVDskBBR6Te0FqWMCRbkjdzdK__UhVKkeUj6RevsIhyocHos9YRxEygBXeqjkK-DFHLrxKsvDKViFfHj8QCvB6oipgqsEgNxrP4beun-ItsxoN_VPPCkbkauh6s2FqpL0WHg4wt0AVUcmTYdLK8bFXeJwNHItsKypHOrTdoU6RhXMyz46J6Z5s-TelUJDQGqilJl-fqmZ5M-bV3s_F_24ZjDihBCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
اعتراضات شدید خداداد عزیزی به داور بازی؛ واقعا بعضی وقتا کسخل میشه الکی کارت میگیره
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/105619" target="_blank">📅 19:38 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105618">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🟥
خبر کوتاه بود و تکراری؛ خداداد عزیزی در بازی امشب تراکتور هم کارت قرمز گرفت و اخراج شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/105618" target="_blank">📅 19:34 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105617">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQsM-d_Q5P0cd0ihPl_Xl-JuEoO8Do-8irmOwnaVLGyl91kMbjfWOFvD8B4fyrDN3wd3upOO7PngEaJTfzPBDayJPJ4dwhwfuLV2iVWdKtqX3Ejw0fh8T_thoWhA8HpZDuyorSw0Q4YR-5E0TPRO0FaLbXP0N_o9QnoaoJ2CtO5tTvlYV4HRiAiImdNL36PeLTv1vtN1AtwM5xekhOXsNNHuAR4dMh8HB-RMS8NBFcydgnTrTvwwNk6cvhNhlWd8xe2ZP9mNqMaq1DPcc2wJV8BB8AWBUGli3s8Bch6RXeJUr9jznHMeFVXl5NgmHNzj7mx1he-HrL4__KW-P7hicw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
تاتنهام برای سومین هفته متوالی در لیگ برتر، بدون پیروزی و بدون گل باقی ماند!
😵‍💫
🏴󠁧󠁢󠁥󠁮󠁧󠁿
شکست 3-0 مقابل برنتفورد.
❌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
شکست 2-0 مقابل نیوکاسل.
❌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
تساوی 0-0 مقابل ناتینگهام.
💸
باشگاه بیش از 300 میلیون پوند هزینه کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/105617" target="_blank">📅 19:31 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105616">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
‼️
🇮🇷
🎙
صالح‌حردانی: مشکل خاصی میان من و آقا سهراب وجود نداره و‌ بزودی شرایط به روال قبل برمیگرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/105616" target="_blank">📅 19:29 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105615">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
⭕️
⭕️
🇮🇷
براساس گزارش برخی منابع خبری، سهراب بختیاری‌زاده به تاجرنیا اعلام کرده که زمینه فسخ قرارداد با صالح‌حردانی را فراهم کند و دیگر قصدی برای استفاده از این بازیکن در تیمش ندارد! به عبارتی از این لحظه استقلالی‌ها باید از بین سهراب و حردانی یکی را انتخاب…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/105615" target="_blank">📅 19:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105614">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhvY6r3v6B-OcfC3h3YfJvFSiK8yet22CYBABCpG5jwbysBf8XZ6oGglCrmypRihQY6PjJN3MRmJT1n_FmoPB0bHw6_TlXlGDKZIb9hP8XEHT04hEP903hj14-qfHNQ18ozEF8_P3HRJRnl7TcX3A7ssaJJTYaTExSWy5pcsEIaKjzPIpys_Tc7JW6piJ74h6S7_7RpN8X_51iTEVv3X6MS981XG3BGW8tzL_HMQ8Lkh4dXFSO495XSTEpL9bGPhsihVPnzTmC4P0SMb7rBc2H1uthaGSRXmaXRUnr_4KnBxPIy-drHVw18466bH0AKuT-CtKfLXwlp57Z2u4TjgxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول سیتیزن‌ها به کاونتری‌سیتی توسط هالند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/105614" target="_blank">📅 19:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105613">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8baa9605b.mp4?token=FxENXGmuD50N_ogIT5ZbqhSMIr83Y7ii6dt-rD1OlWFUr3e6bOxELE2vD0X34K6rAJJUelE2WBF_PJ2hgtSGpFCJiWLnJUj5lwdIt0rUByeix3FLxMUY2BUcF_BhuaKSuTyJkeECyOJ_fuh-A9MuuX1-T8swl35A1wQtBMp3l86xFRU-kC4InvHWV07C_ywkHsGP6O-ZfXQ2k0e6GbRaqRhYCA5yqFZqV-J7F0Lk3OpsInzRUzHbxghm3YslWPw-vR34k96PVTKaEITWFm9gDtMmbe8kbeZDoAdaXpsBkhnP9EEwycPXF44dPDk-D0elg-2HnO9UPMjV2M1MW-05Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8baa9605b.mp4?token=FxENXGmuD50N_ogIT5ZbqhSMIr83Y7ii6dt-rD1OlWFUr3e6bOxELE2vD0X34K6rAJJUelE2WBF_PJ2hgtSGpFCJiWLnJUj5lwdIt0rUByeix3FLxMUY2BUcF_BhuaKSuTyJkeECyOJ_fuh-A9MuuX1-T8swl35A1wQtBMp3l86xFRU-kC4InvHWV07C_ywkHsGP6O-ZfXQ2k0e6GbRaqRhYCA5yqFZqV-J7F0Lk3OpsInzRUzHbxghm3YslWPw-vR34k96PVTKaEITWFm9gDtMmbe8kbeZDoAdaXpsBkhnP9EEwycPXF44dPDk-D0elg-2HnO9UPMjV2M1MW-05Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
عصبانیت فوق‌العاده شدید مهدی‌رحمتی از داوری بازی تیمش مقابل گل‌گهر سیرجان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/105613" target="_blank">📅 19:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105612">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Im0APaUhlFgjwTWL9l7UjhZ8CfYrHTBEhFZZa1gJF1FuegPz0M_rI9sPnujvl0BiAXery7hFMO-9Q3jVYrktn798bKOo_rfw3NhENK-44_njXgBriKs37Snz_O4SLQD3aWTwc707UpPrudbfNZhVu4rR4nw7hZs3Rcv1rrMvC1kDI2IZuhedFNwiVDymgkbJySCOb_ozcJ5hcCrnfraJbVt5WAvVo6CqA8rqYA1PbneIuK9I3bbKfSvIISCb99g6F0JwSe6MElvMLFivTar7U59UWO_AT9j_J9QKhlWxGtO7oIpQMYhI4n1vF6ZVXksH_q5qR6TgnUjcY5iQ5UZicA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
ترکیب بایرن‌مونیخ مقابل شالکه؛ ساعت ۲۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/105612" target="_blank">📅 19:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105611">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5cf5064174.mp4?token=Y2PoLTojF5T6yx-ec33f-yyis_MU6PK4pD8vmbDwFJVgQoObqlVXgF_ueaSdhuOWVEANsSOwkZQcG4bvjPP6v1NrIuY80HswEtieOeHt713bXVQ07Uwf8GxbwNFuwMdWrMF5GwNwM4PAZVhvG1nozKwjL1l3gVPr9ZtO_zuzU46f0SBG0vGoX2aIOTLKskAuB_miIBFcRCHwLmTSfFgEMhikDp_xii1RuSIlpiMqikQmTlfMbyAf5Eh5ek7ktu3MF2-LJ5aW97_xKxzP2LWNTvqWsH-SXVmlWzGXa41qnchDGxFvwW6o3jr2S0rppPIPQORmu8KKyHdx5S6bbVMk07mUlQOlkicSYYZ1fiQXuxfMxB8X7YBYYMG0WENOEnomkMd7rw4aEI5WHJ2t4W7pfo6kqzgXy0KS4uQGIG5d0iPDnBoOKxTowm3PSd0v4DRyQAFWk3S9JS9wZNTWm2nQDWeoGXwDzgjg1u8NA2_HjRDOroXIL_e_9JxApmEanOLXLCxNaPrNBYrPkh869nXQOKIZIOnM4BzC3FtozHEThiKQFIbdVl32eKBKs1cW-gqoHzugpHJi3EgnhLDg3jcDYx1w2FDndo3rb3KEayaGkVYnkkjxqrDfC7h06n15mvtj-12lVmY089i0W0tNqTd2jqMuo1KJGZpkItxC5qDm1rI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5cf5064174.mp4?token=Y2PoLTojF5T6yx-ec33f-yyis_MU6PK4pD8vmbDwFJVgQoObqlVXgF_ueaSdhuOWVEANsSOwkZQcG4bvjPP6v1NrIuY80HswEtieOeHt713bXVQ07Uwf8GxbwNFuwMdWrMF5GwNwM4PAZVhvG1nozKwjL1l3gVPr9ZtO_zuzU46f0SBG0vGoX2aIOTLKskAuB_miIBFcRCHwLmTSfFgEMhikDp_xii1RuSIlpiMqikQmTlfMbyAf5Eh5ek7ktu3MF2-LJ5aW97_xKxzP2LWNTvqWsH-SXVmlWzGXa41qnchDGxFvwW6o3jr2S0rppPIPQORmu8KKyHdx5S6bbVMk07mUlQOlkicSYYZ1fiQXuxfMxB8X7YBYYMG0WENOEnomkMd7rw4aEI5WHJ2t4W7pfo6kqzgXy0KS4uQGIG5d0iPDnBoOKxTowm3PSd0v4DRyQAFWk3S9JS9wZNTWm2nQDWeoGXwDzgjg1u8NA2_HjRDOroXIL_e_9JxApmEanOLXLCxNaPrNBYrPkh869nXQOKIZIOnM4BzC3FtozHEThiKQFIbdVl32eKBKs1cW-gqoHzugpHJi3EgnhLDg3jcDYx1w2FDndo3rb3KEayaGkVYnkkjxqrDfC7h06n15mvtj-12lVmY089i0W0tNqTd2jqMuo1KJGZpkItxC5qDm1rI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌دوم بیلبائو به اتلتیکومادرید توسط ناوارو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/105611" target="_blank">📅 19:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105610">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d7c282d728.mp4?token=UQuD5rQedljy2-qJj_imBZPCQhY96T31Pjc_KK7_IB9XnTwvvR73M3aZhfwRuS-fGzGFej5Hyq1BYyd_QZ1DuqIPP6yV3zjjLWA9S_CtSH0I85MUTqInw3fPjX_AME08ZKdUYxyyzOFdMDXTaEKiZEXGHUJ4VggQ7TTeDxe8-ANLMDjNbMakgTiYNlNiZUenHlXIM9wvbfY-9lwu1XI0jIt-N2R1297lnIrEudG8L-t0zxkpFHdon9S8TG4csoU5mQXB2FV593WQT2ctpPV3Is6WDvauN6-K-Dt2dIduM2YXhau9D5i0k2FuNKXBtJFwXCnqRfthvRHFZ-ewP3D7szVljGH_wNgWonv09z9ZIpeLbXPIihYZHF-Ku5adWmWvdIb4ykfKk6bBvjn5OJQnuN4T_3lKsC980CehuR_Bx9oDjBxS6I395bvmIjuLzEKrvwb3lvaF3ohbHhn6h_DExERV2F7XKqXh4yOSrls5L0lBvRrLmOpJiLxczH8Ivfd5OHZwE3fdI1cWPsKTHml8oDME3hu-N2xBhq7PnHxfl1zNysvwHlPqRPD0WI0J6JysbcmuZv5BIJFnQafhzNqpNms7vLatzqTBgPVOY9hVVcjMsPA7slLxkQKmUX4Wkd6KX8aIbz3yoAn6egVNH7KdwMSmoLJCltdR3JfvtcNRBbk" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d7c282d728.mp4?token=UQuD5rQedljy2-qJj_imBZPCQhY96T31Pjc_KK7_IB9XnTwvvR73M3aZhfwRuS-fGzGFej5Hyq1BYyd_QZ1DuqIPP6yV3zjjLWA9S_CtSH0I85MUTqInw3fPjX_AME08ZKdUYxyyzOFdMDXTaEKiZEXGHUJ4VggQ7TTeDxe8-ANLMDjNbMakgTiYNlNiZUenHlXIM9wvbfY-9lwu1XI0jIt-N2R1297lnIrEudG8L-t0zxkpFHdon9S8TG4csoU5mQXB2FV593WQT2ctpPV3Is6WDvauN6-K-Dt2dIduM2YXhau9D5i0k2FuNKXBtJFwXCnqRfthvRHFZ-ewP3D7szVljGH_wNgWonv09z9ZIpeLbXPIihYZHF-Ku5adWmWvdIb4ykfKk6bBvjn5OJQnuN4T_3lKsC980CehuR_Bx9oDjBxS6I395bvmIjuLzEKrvwb3lvaF3ohbHhn6h_DExERV2F7XKqXh4yOSrls5L0lBvRrLmOpJiLxczH8Ivfd5OHZwE3fdI1cWPsKTHml8oDME3hu-N2xBhq7PnHxfl1zNysvwHlPqRPD0WI0J6JysbcmuZv5BIJFnQafhzNqpNms7vLatzqTBgPVOY9hVVcjMsPA7slLxkQKmUX4Wkd6KX8aIbz3yoAn6egVNH7KdwMSmoLJCltdR3JfvtcNRBbk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌اول بیلبائو به اتلتیکومادرید توسط ویلیامز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/105610" target="_blank">📅 19:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105609">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">گلگلگگلگلگلگلگلگ بالاخره اتلتیکومادرید خورددددد</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/105609" target="_blank">📅 19:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105608">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9c8ab04f1.mp4?token=XxD3yu5H4ieLGPJECP2rZPAASvMovCAFnIrogF-UvInoLQumKEo9VEQwNfVNOJ1uXgSH-i7nmZWaMGn1BMlz-0ug-1Egbv2PKDRP83RDYTR1bAllQO-Dpl125q5GaH8fjqVrSsuhAxpkQenrkP5vJux9rB9JgLY1ehAP7u2vjfgyEGoKQJWC3wHT_R97X9c99qZtEptFuBnjNFWFVJ6c6Z1z6hMJbRSW4tr8vHPvkOGlRwQqNoJeocAYYZx9Jw0u7IOP2bSJbJImGIpchPJB6Orb8vNUo8H6oOM5e2FybK_drkVuPpj2diJ4GjGsMs8GA6tEbbR0MUtgJ0w6riQleg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9c8ab04f1.mp4?token=XxD3yu5H4ieLGPJECP2rZPAASvMovCAFnIrogF-UvInoLQumKEo9VEQwNfVNOJ1uXgSH-i7nmZWaMGn1BMlz-0ug-1Egbv2PKDRP83RDYTR1bAllQO-Dpl125q5GaH8fjqVrSsuhAxpkQenrkP5vJux9rB9JgLY1ehAP7u2vjfgyEGoKQJWC3wHT_R97X9c99qZtEptFuBnjNFWFVJ6c6Z1z6hMJbRSW4tr8vHPvkOGlRwQqNoJeocAYYZx9Jw0u7IOP2bSJbJImGIpchPJB6Orb8vNUo8H6oOM5e2FybK_drkVuPpj2diJ4GjGsMs8GA6tEbbR0MUtgJ0w6riQleg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❤️
گل اول تراکتور به گل گهر توسط امیرحسین حسین زاده
روی پاس‌گل بیرانوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/105608" target="_blank">📅 19:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105607">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">تراکتور زدددددددد</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/105607" target="_blank">📅 18:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105606">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">گلگلگلگلگگلگلگلگ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/105606" target="_blank">📅 18:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105605">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">گلگلگگلگلگلگلگلگ بالاخره اتلتیکومادرید خورددددد</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/105605" target="_blank">📅 18:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105604">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d91e2fe36a.mp4?token=e7WTuTvqN2UkWm1ThPIlwZ0Xlm7dDQZlWwoYnatFC5vajrQ0JeZ0QmgZZneqz9XSrt9iE9DdaKrkChioQewJte8lsm08o5T3jT1f2-xh0T9v2BUqRMbXu8-teXbRzz-Yg8DZVyiLF6WZUOv_t27xIwNPZfMnUZi-bUj_Ie0-zw8jgonbu3myG8-yiwD2x1GatATQhZ3G78PJipIacxUYEU8JaZQz-c7xEhjZqBbH-9HnjhibaV8HoPIyvcwa7t8UVoRe7F8oLrS6NsxGpl7bSZ_vW22WjPCIvxcTIkS4oXRevj7J_k-P33MgxPVEvSHPTbqmlW893rEp0qYaEp5vtEFC1K_oSik-LYZKUWZUJ2rOKEJrh1JIHdKhJtSUlHQWeCYBcgvlFz6_wO9iFX1mLHP9hZM1qfgWoYNFNUUJDkbrcv2uHUpkxebk6qrKTjFH62yEBF2NAyCnnf_XuBrT44SRCyRjk-A-k6mQ02wQfN1pJfIB0ykiW6GLuxYPa4KT9KjM5WTH8vZL_i6NCVURjqE0nt82yJqk0G8HNXeRfNk9X4QZ-Up0y_L7N4FfXB0aGFv2VeMJc8kKWOsGf2yARihWqt6YRSY4vc_l47IzDcF0sbBcl6bHHB2ptKhtifRQ5tmID33pzNAg_AdueXF4ZYjVF4uoL77Q0jhJzE04kBM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d91e2fe36a.mp4?token=e7WTuTvqN2UkWm1ThPIlwZ0Xlm7dDQZlWwoYnatFC5vajrQ0JeZ0QmgZZneqz9XSrt9iE9DdaKrkChioQewJte8lsm08o5T3jT1f2-xh0T9v2BUqRMbXu8-teXbRzz-Yg8DZVyiLF6WZUOv_t27xIwNPZfMnUZi-bUj_Ie0-zw8jgonbu3myG8-yiwD2x1GatATQhZ3G78PJipIacxUYEU8JaZQz-c7xEhjZqBbH-9HnjhibaV8HoPIyvcwa7t8UVoRe7F8oLrS6NsxGpl7bSZ_vW22WjPCIvxcTIkS4oXRevj7J_k-P33MgxPVEvSHPTbqmlW893rEp0qYaEp5vtEFC1K_oSik-LYZKUWZUJ2rOKEJrh1JIHdKhJtSUlHQWeCYBcgvlFz6_wO9iFX1mLHP9hZM1qfgWoYNFNUUJDkbrcv2uHUpkxebk6qrKTjFH62yEBF2NAyCnnf_XuBrT44SRCyRjk-A-k6mQ02wQfN1pJfIB0ykiW6GLuxYPa4KT9KjM5WTH8vZL_i6NCVURjqE0nt82yJqk0G8HNXeRfNk9X4QZ-Up0y_L7N4FfXB0aGFv2VeMJc8kKWOsGf2yARihWqt6YRSY4vc_l47IzDcF0sbBcl6bHHB2ptKhtifRQ5tmID33pzNAg_AdueXF4ZYjVF4uoL77Q0jhJzE04kBM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
تمجید لوکا مودریچ از کریستیانو رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/105604" target="_blank">📅 18:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105603">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105603" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/105603" target="_blank">📅 18:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105602">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUilMYaeh-pu55GzFoOeduLSsnKIrtaPWdP18BGOzUAsquv3Nzl26Z0urNmcCwE7Eu5mcljcSnQVpHOB5oDDQrj0xTJw8NuKACVN_lRlwYXg9YPacFJ-4nBD6U15TpljPI-VFO2ZP112eY5Rx58M328MBXGBwPLddW3n66tibM2TX1ae-kYbKpKu12CMvFHdge7NWQcYK2ObMIx9xZ3YuW54Vsq4AVz5hTrF7gxBL9ON1lCQ5wZxiwsyqyL4S7IvIYWmXZPgcHmjbm__nQ0v4prFFUaGnfafUKcMzzVSfeeEavLSrbF501rGhwFW4dLseemz5eF-qq9PfTz1WK3IvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب اینتر
🆚
ناپولی را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
📊
نگاهی به آمار دو تیم:
اینتر: ۲ بازی ۲ برد و کسب و ۵ گل زده
ناپولی: ۲ بازی ۱ برد و ۱ شکست و ۳ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/105602" target="_blank">📅 18:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105601">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcfbb8df7d.mp4?token=KZwHtDDLADV_bdC76V65W1HHJsOvsIpv7sBbUyNUA3Ds0Q5M7kbKcpFh2u2onJ0ZNLstefM2HUVcDeBP7d9nmUcqIsRWa2m30MQFFxA9BugBVgjNKclcjusYDBtuX3vDEXHKhrI99SHmfFC7XreWS-pqewrCf59i8MY4o2cuIBep3tQbln9xgZRmu-iFQ9M78qCXv4ydmBCD7MzZf04vw_6dzPXvISf0YJJvyq34crrdoW7rI86GGsdm-DTD8rLVZNS2kW6qGkRQAJqfC6WWhFMHW3-cosWBo7GwWpG-ALg1fFdrPIsKQRf9v-qk9EO4E10gErocINr4n99PMYwRrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcfbb8df7d.mp4?token=KZwHtDDLADV_bdC76V65W1HHJsOvsIpv7sBbUyNUA3Ds0Q5M7kbKcpFh2u2onJ0ZNLstefM2HUVcDeBP7d9nmUcqIsRWa2m30MQFFxA9BugBVgjNKclcjusYDBtuX3vDEXHKhrI99SHmfFC7XreWS-pqewrCf59i8MY4o2cuIBep3tQbln9xgZRmu-iFQ9M78qCXv4ydmBCD7MzZf04vw_6dzPXvISf0YJJvyq34crrdoW7rI86GGsdm-DTD8rLVZNS2kW6qGkRQAJqfC6WWhFMHW3-cosWBo7GwWpG-ALg1fFdrPIsKQRf9v-qk9EO4E10gErocINr4n99PMYwRrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
فحاشی هواداران تراکتور به امید عالیشاه در بازی مقابل گل‌گهر سیرجان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/105601" target="_blank">📅 18:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105600">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOuhUrCj9iZ2gjmo7rrZxxdVMm5nGlQIyva5k2fOzrivb6RaOgg1uFYocAjc_Hg97wU4LzCxqI3ZruQnVV6jkQXmXJ2ZGDR1HZ4d-KvrZrC0Y5dNirdXmodacHX1NtdJHi9ICojAToiuUelIeTf2klz7iHRAM73UXZgcN7G5VsTuKB-WmiXocyvXEvQQ9-Osi9xF5VtrARu8NABEYcDetHH2ba8HCI7QUEFLmMdYudblxiD94mrsJweAl3lnoK_oDTbuVljMakvKwMyEfJy0iT5gFzxn2fzH9JwI7izF153uubKVxGuK-E7Gs_4TKDw5IzqVcLGqSdmzSqViIADZaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🤯
🔵
هالند مقابل تمام تیم‌هایی که در لیگ انگلیس با آن‌ها بازی کرده، گلزنی کرده است، به جز یک تیم، یعنی ساندرلند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/105600" target="_blank">📅 18:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105599">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BeDjBKTaLxH9AwOf2aEHgPFiAF3JTSwdheAyJWd2KTcmMknOaQCRJSgOOoBJuvb1A1bcOLlJzeDXXWbM1z729rg5j8W_ix1_xdhM_64jZdKg8N51A7-gWGEJnFc3V4KcY-TG_0TKU3OcEhaPykAHFuU-y0YenEZyPWAU8ysRGGD4eu0cDY8pjQ23R-jEBnv6DlzeF2A4vG7tPVqxqiJnVGu9FiDMVUDQTVOo3ri-ROiKtbcBBlhAb_V5cVJMpI18X2ECYKfujFypfEpeeVfouL6q7fGieUG95RMcQcL_7eHkDjY0-hcWJH54lcj0ZQuTSfgqGsFH7BH5OjhWUkS3Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
ترکیب اصلی اینتر مقابل ناپولی؛ ۱۹:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/105599" target="_blank">📅 18:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105598">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvNfsFGk1VeOsneTnnA8O3lQdTLY0pDEy17K4LSl9JjBBAMyccMSfd7c_daBKfXQuYO_VXV6caC9hpYTK5Yxfh109dvQMKUDRm3ybV60dxvBWncjnqPxk57AnrpCCpydJY5kuv-i6pu4HySDSTSLmD_84_l-Ikb8Z19a4oBzDdysGnCkOFUth0EMdEGdoNs8Zp2bkogMbCWSIRl1O7KG9ltHjN5j7cMh1kRE-KM7hBxu3mUnqJeimk4HTXmtnoUWw9svklhbNRGP0cZS3kSPfy2mcItTc32TRy9bj_vS1cZHBJlOZXjcWBGFKjlQPQBidaF0UlHsXPgKwowZ0JoiEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خولیان آلوارز امروز هم نیمکت‌نشین اتلتیکو هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/105598" target="_blank">📅 18:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105597">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0ffcdccef6.mp4?token=ArQaYGNacq8qBA7KYW6e-NR4q7xeqTdNPz_y1kN1PI1a4NQY2oJHE-YL41z54MNZZzt6BnnVmBWqcKCB_xIAb6bxYokpqMo40dzZ_6vA7Cq8Gvu7HwuEbMzjsJUVyDB5Mbw-S00BcJ94-nSz7gFljCGDhhMrxvQTaHdeYIp1S7AMeP-dJgUWV_p3i08EM660wnoOYuMgX5L_hhikQJZCZ_klO36nYlcrV7r_OzPf5F-nZkqhw2JJD5aI3AlPvOwLh_iAjG9LZ-naR2yfZXkk3ca32Z9GRGt6aOZ2lulWUkCpCMMMgGyIoh3B9gKiYTaqGdfvQIjO8cDJ7to_f0sxww" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0ffcdccef6.mp4?token=ArQaYGNacq8qBA7KYW6e-NR4q7xeqTdNPz_y1kN1PI1a4NQY2oJHE-YL41z54MNZZzt6BnnVmBWqcKCB_xIAb6bxYokpqMo40dzZ_6vA7Cq8Gvu7HwuEbMzjsJUVyDB5Mbw-S00BcJ94-nSz7gFljCGDhhMrxvQTaHdeYIp1S7AMeP-dJgUWV_p3i08EM660wnoOYuMgX5L_hhikQJZCZ_klO36nYlcrV7r_OzPf5F-nZkqhw2JJD5aI3AlPvOwLh_iAjG9LZ-naR2yfZXkk3ca32Z9GRGt6aOZ2lulWUkCpCMMMgGyIoh3B9gKiYTaqGdfvQIjO8cDJ7to_f0sxww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول سیتیزن‌ها به کاونتری‌سیتی توسط هالند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/105597" target="_blank">📅 18:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105596">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‼️
🎙
🇮🇷
حمله رسول‌خطیبی به هواداران شیرازی: لابد پارسال فجرسپاسی قهرمان شده و من بی‌خبرم‌. یا من فوتبال نمی‌فهمم یا این چند نفر هوادار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/105596" target="_blank">📅 17:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105595">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🇺🇸
سنتکام این ویدیو رو‌ منتشر کرد و گفت امروز سه نفتکش ایرانی رو با موشک‌‌ هدف قرار دادیم
نفتکش "دانی" را در نزدیکی جزیره خارک و نفتکش "استارک 1" را در نزدیکی جاسک به طور دائم از کار انداخت و نفتکش "کایلو" را در خلیج عمان به طور کامل نابود کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/105595" target="_blank">📅 17:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105594">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇨🇳
🏀
ژانگ زییو، ستاره‌ی 19 ساله و قدبلند (2.23 متر) از چین
🥶
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/105594" target="_blank">📅 17:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105593">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🔵
مصطفی‌متدین از مدیران صنعتی هلدینگ پتروشیمی خلیج‌فارس در آستانه مدیرعاملی استقلال قرار دارد. این شخص پیش از این مدیریت سازمان توسعه هلدینگ‌خلیج‌فارس یا به اصطلاح شرکت "پیدمکو" را برعهده داشته است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/105593" target="_blank">📅 17:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105592">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OWfCwkiNddk1zXLlRtZY6MzltLofp6HQAAA74a2p_XklPCpQzU5rXWrIX4CGkN3L6aH0vZUoEwqMgnkuEqDhLumGpA6uoTUSQX97AseQPOe9TOQYlnzvErSZ3BLd3prdObfWQHbPrrfXfawaZPJQRqKu7jRIo8aRp0ZIhoE4dTX85ou1C5bWciiSfiKRIkGw9IbJrrUbePSfdJkzuViziY8c0qtz6UwFHgNsCG_TG3beUJ3uWJ0amIMS1LGFwhsyIYvhaL9UtxsEEPNJ-oTeA0phL_5NMj6HuVeRuoe0iv1cYBIjRnwDJBG4hvvkbh2SHH3wEQwzvZG_7KDW7oAcig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
لیگ برتر ایران؛ ترکیب تراکتور مقابل گل‌گهر
تراکتور- گل‌گهر (١٨:١۵)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/105592" target="_blank">📅 17:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105591">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce3805b0d1.mp4?token=BfsosQeY-dBl6OICbysP4dTAWDSjPCzAO9_IjgdETA3EEKJgF3pBQw7R299uZhU-OZt-Qm6UPMpV6USJwTuYsmxlOXRnwQ-KZ1xQDQHERqGf1t0x_hVTeZI3UOBXgiyTD8vGgkpXPO2cGL-rxDCmeANyzA0eTo7gnYajHmQSw7aa2dJLwwH_FmamluEFck6FMAEPCXRSgs-T5vO8W2GwmT-99XMdwe0jc0t5E7OyreYSArL-cUD8JEL437EIaUTRi-aD-MFjNRlJXLQITjhD3TsjLxT1wT5Sf8I2mshVsR0IDujfqmYVQE9CirrLRdj7UHDYifvy5u9u43X7lynrLoc72Lp4v0lS6kRIq0toWTIafrmMihKSujkXb6UQ081wfNv26OIvZhy_Go6X1wHojnB7jT-j6vEmieE9ML4ysp0lJLZEQoExCL48zvxBF9Igd8EzqSWWlqFh16wIMYRc9E0PL_wsVXZ4JY5iqTEsozsCwXfbE96_IVnd66FB8pM7YCgge0GC1FJkhqmGfg5PDUgYoaKUD2Gc1VBQiylCCxBGgxPxVhIs-eOOPn6OMklnhhg9ty4cnZPePh8g1rp5GRtRuK9yxTElVOTaaT-6Jqt_TWs7eTT-53YSCcQYuqut6bYyMmVXnbjsyztjGCgjDmfRzJm9YXN3432apg8w08U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce3805b0d1.mp4?token=BfsosQeY-dBl6OICbysP4dTAWDSjPCzAO9_IjgdETA3EEKJgF3pBQw7R299uZhU-OZt-Qm6UPMpV6USJwTuYsmxlOXRnwQ-KZ1xQDQHERqGf1t0x_hVTeZI3UOBXgiyTD8vGgkpXPO2cGL-rxDCmeANyzA0eTo7gnYajHmQSw7aa2dJLwwH_FmamluEFck6FMAEPCXRSgs-T5vO8W2GwmT-99XMdwe0jc0t5E7OyreYSArL-cUD8JEL437EIaUTRi-aD-MFjNRlJXLQITjhD3TsjLxT1wT5Sf8I2mshVsR0IDujfqmYVQE9CirrLRdj7UHDYifvy5u9u43X7lynrLoc72Lp4v0lS6kRIq0toWTIafrmMihKSujkXb6UQ081wfNv26OIvZhy_Go6X1wHojnB7jT-j6vEmieE9ML4ysp0lJLZEQoExCL48zvxBF9Igd8EzqSWWlqFh16wIMYRc9E0PL_wsVXZ4JY5iqTEsozsCwXfbE96_IVnd66FB8pM7YCgge0GC1FJkhqmGfg5PDUgYoaKUD2Gc1VBQiylCCxBGgxPxVhIs-eOOPn6OMklnhhg9ty4cnZPePh8g1rp5GRtRuK9yxTElVOTaaT-6Jqt_TWs7eTT-53YSCcQYuqut6bYyMmVXnbjsyztjGCgjDmfRzJm9YXN3432apg8w08U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
لحظاتی از مسابقه طناب‌کشی تیم ایران در بازی‌های جهانی عشایری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/105591" target="_blank">📅 16:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105590">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20fca94904.mp4?token=F8heJyvld863DHh9qEad2PIG1NpXp3_yTSkE1qx6iCn6cHhhSu5vrf3oHRiLGQ2hEDcdnCFMKDjfy8h2A1IGB2pecO72WQucp7KbClamb9OjtuQ0wVIwLN7fvitiTVWJgHDPZOVXG7Bta-7cHN6dPZldTdtluNEkysJYwlL5lyUzXxeSDU7xZZrYIa8yN-WwQeW3OroIV3tXjXfqNfRkOrGvKHlB1k9qntr65V0mfEvov3njXRhZiNo0PB-N0CdJws4u5R-MyOM78e2UWRY60366DZbA_DUODhn6PC2QS0r84pfYeb2vcrHn3KM3VBD5uTJ7D9H9yeeONo5VJe6mFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20fca94904.mp4?token=F8heJyvld863DHh9qEad2PIG1NpXp3_yTSkE1qx6iCn6cHhhSu5vrf3oHRiLGQ2hEDcdnCFMKDjfy8h2A1IGB2pecO72WQucp7KbClamb9OjtuQ0wVIwLN7fvitiTVWJgHDPZOVXG7Bta-7cHN6dPZldTdtluNEkysJYwlL5lyUzXxeSDU7xZZrYIa8yN-WwQeW3OroIV3tXjXfqNfRkOrGvKHlB1k9qntr65V0mfEvov3njXRhZiNo0PB-N0CdJws4u5R-MyOM78e2UWRY60366DZbA_DUODhn6PC2QS0r84pfYeb2vcrHn3KM3VBD5uTJ7D9H9yeeONo5VJe6mFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
😆
هوادارای بارسا جلو کمپ تمرینی این تیم منتظر حضور رافینیا بودن. حالا رافینیایی که جلوشون دراومد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/105590" target="_blank">📅 16:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105589">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmDgMiU9jDNvo1pCTQQIxw6-dwI6Xjo3e30ePY9GzfP5Ugy8LbBcohDvHM2LG83AWzmqv1tUcdTosxQZ0dnOHhEfUKTHb2jhq-J90Trjkawh02Ku0FS8NWS8CZhn1MWdG4AfzjoPMZqybg1N3GtQGePTla6ZF-WONaDHINY2DtcsdpI63wzaKOHxsfup4fPJo0RUu0XC0HcQauRPbqDcvKf29MzwZ_nQgG59dFSUsKuKyQRqPwcG7pQNSpi-DcHkpNEcRbtE6XdYMfetT6dNyGeGPjOu62GOfozcErC8xM8Z6Py4jZPYY79xad6Pzt3nxAxwY29xmeIAJWoUNTh9pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شانس برنده شدن باهاته!
🎁
تا ۲۰ شهریور
با خرید هر بیمه‌ای از اسنپ‌بیمه در
قرعه‌کشی موتور یاماها، آیفون 17 و PS5
شرکت می‌کنی
🤩
چرا با اسنپ‌بیمه بیمه بگیرم؟
✅
با پرداخت قسطی هم می‌تونی تخفیف بگیری
✅
برای هر سوال یا مشکلی، پشتیبانی ۲۴ساعته داری
✅
و در قرعه‌کشی
موتور یاماها، iphone 17 و PS5
شرکت می‌کنی
این فرصت رو از دست نده؛ چون با اسنپ‌بیمه شانس باهاته
💙
وارد لینک زیر شو و جایزه ببر:
👇
👇
👇
https://l.snpy.ir/ixsth
https://l.snpy.ir/ixsth
https://l.snpy.ir/ixsth</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/105589" target="_blank">📅 16:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105588">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
‼️
🎙
مُچ گیری عادل فردوسی‌پور از محمود فکری: کُل دنیا دیدند دارم به صورتم گِل می‌مالم
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/105588" target="_blank">📅 16:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105587">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29285b8410.mp4?token=IZGXPQ1KF3hBGTmGPpU5oo143t6kVMT4cgel7gt-saTlzVn0bBR1D7cn8RPqQY4XP5n6d87cByXIqFchhmNE95mEkQJN2TstkqMuCLGlSlLcbJI-jZW2pMcPtoPs3AipHARYIPjunH-UN_JISXNpsYrTRoDJN_pw5OpyWPZ1a66udJ12_zj9wKkGh5oKqx9nYeoFeUsrlWHqyBYEaRK0Dhb3xRD-G3nkTV2SQTSsBxCwBIQhQlKxscAscTlxyavbK-RCN3D5_UyMk7GB0UUpDoaWu_4tlobnTvB4MTDKVVdXZomODSiRWGuaIpzlKCcrWCwM39bn_1Rv2UTex9qGkRHgwuT_y8JkuLIN6mVY4DyAtFjHmSIqou0DLuCJV4f6CqfbtM-fmWWBsQ8qi6fjk3wdhbgU-vEfA--ff8Oc_t2UBqLr2JjjeOS1-41yCuTvaHK9L1d6ytEnIeOl2RqTmb2u1h5OHUTCdH3u9G1uIrE-Mf6xcg0MUfUsR0zCEj_uB00q-f_7srKZUvCYy-C5gz6u2aWDYgZ8Wm8gehp5_h7InPdeV8CQdtmTdTQm-trx9u_psXDUCKUM_pK86OlTJYvK84I4_f08IWgWX9kL8z2QvuANRplEJzPWNBwIdiLGYziMy6PEV9GqskrXmHvuxLEgUzTFF-VHjZMO38Mp3Tk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29285b8410.mp4?token=IZGXPQ1KF3hBGTmGPpU5oo143t6kVMT4cgel7gt-saTlzVn0bBR1D7cn8RPqQY4XP5n6d87cByXIqFchhmNE95mEkQJN2TstkqMuCLGlSlLcbJI-jZW2pMcPtoPs3AipHARYIPjunH-UN_JISXNpsYrTRoDJN_pw5OpyWPZ1a66udJ12_zj9wKkGh5oKqx9nYeoFeUsrlWHqyBYEaRK0Dhb3xRD-G3nkTV2SQTSsBxCwBIQhQlKxscAscTlxyavbK-RCN3D5_UyMk7GB0UUpDoaWu_4tlobnTvB4MTDKVVdXZomODSiRWGuaIpzlKCcrWCwM39bn_1Rv2UTex9qGkRHgwuT_y8JkuLIN6mVY4DyAtFjHmSIqou0DLuCJV4f6CqfbtM-fmWWBsQ8qi6fjk3wdhbgU-vEfA--ff8Oc_t2UBqLr2JjjeOS1-41yCuTvaHK9L1d6ytEnIeOl2RqTmb2u1h5OHUTCdH3u9G1uIrE-Mf6xcg0MUfUsR0zCEj_uB00q-f_7srKZUvCYy-C5gz6u2aWDYgZ8Wm8gehp5_h7InPdeV8CQdtmTdTQm-trx9u_psXDUCKUM_pK86OlTJYvK84I4_f08IWgWX9kL8z2QvuANRplEJzPWNBwIdiLGYziMy6PEV9GqskrXmHvuxLEgUzTFF-VHjZMO38Mp3Tk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
خاطرات شنیدنی ستاره سابق آبی‌ها از دربی شش هیچ؛ قراب: همایون بهزادی زبیاترین گلهای تاریخ را به تاج زد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105587" target="_blank">📅 15:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105586">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f59ae44943.mp4?token=pAyGvWXfy5IKIAkrifEk78NCKbx6oBmNixE0rJSGlBdhdEK9EVx0IJBH1Dp7PW-4auD6iPcW9KOsB9dKgPxR4gSMzeSBVXJ_iCrSzv7UFo1SBZDq4vv3i4kbH76AohtFLUCdRDrv3tEDLZKtvICfNZWNfLiwkKqO-DBTH_H2_M7RNhIpDTFEOpsm5Y1ww6rZLMYqc4ucehy0ex-rlHpDaD3gXP8aCyeJ6vUZmT4m2gIzOHPn-wIJf7YfcpgRT2iSCD5FfEKXxHuIkNKWSUhr2KlBtPDyd8B8M8l26d-jrM1cPGE9SzCsMliWgtK16x53a5oh1sh9GAPJh-3cWcv_1nJBF4qDOhtgyADuq4oIvNjgX9jm2l7O-_69C_ETUpaOsUbdyNx1hxHzoZazHl_wsIzNxzRqv-JvRhtitixNGF8lgxqAmqXMv7jnTVR-xVxiJMFxjIffMO3a5pncIVkkIl73mYJhYZsz3nUzCuBf82O6asee-I32Qa9vn7whOjBOgf9NAMvv3rDDmE-QPL99zOLmzi9tfKq0Y35lacevhxZ50U1QNOlJEDWE7IVk5CuynSVswNUHcMPQdkk_fJAGwN58XNiHR90jF9Xt7xNK451UN65gD0rLvmHcIwSq0VRwmJ7A9sREENA9CF56b5tl8Y6bPGXefClu0bLk6WEqonI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f59ae44943.mp4?token=pAyGvWXfy5IKIAkrifEk78NCKbx6oBmNixE0rJSGlBdhdEK9EVx0IJBH1Dp7PW-4auD6iPcW9KOsB9dKgPxR4gSMzeSBVXJ_iCrSzv7UFo1SBZDq4vv3i4kbH76AohtFLUCdRDrv3tEDLZKtvICfNZWNfLiwkKqO-DBTH_H2_M7RNhIpDTFEOpsm5Y1ww6rZLMYqc4ucehy0ex-rlHpDaD3gXP8aCyeJ6vUZmT4m2gIzOHPn-wIJf7YfcpgRT2iSCD5FfEKXxHuIkNKWSUhr2KlBtPDyd8B8M8l26d-jrM1cPGE9SzCsMliWgtK16x53a5oh1sh9GAPJh-3cWcv_1nJBF4qDOhtgyADuq4oIvNjgX9jm2l7O-_69C_ETUpaOsUbdyNx1hxHzoZazHl_wsIzNxzRqv-JvRhtitixNGF8lgxqAmqXMv7jnTVR-xVxiJMFxjIffMO3a5pncIVkkIl73mYJhYZsz3nUzCuBf82O6asee-I32Qa9vn7whOjBOgf9NAMvv3rDDmE-QPL99zOLmzi9tfKq0Y35lacevhxZ50U1QNOlJEDWE7IVk5CuynSVswNUHcMPQdkk_fJAGwN58XNiHR90jF9Xt7xNK451UN65gD0rLvmHcIwSq0VRwmJ7A9sREENA9CF56b5tl8Y6bPGXefClu0bLk6WEqonI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
پریمیرلیگ هنوز شروع نشده، جنجال‌های داوریش شروع شده!
⁣
🎙
📹
مایک دین، داور بازنشسته پریمیرلیگ، توی مصاحبه با پادکست جیمی واردی اعتراف کرده که زمان داوریش بعضی وقت‌ها برای خودش چالش می‌ذاشته؛ مثلاً ببینه چقدر می‌تونه بدون سوت زدن بازی رو ادامه بده یا چقدر می‌تونه توی دایره وسط زمین بمونه و ازش خارج نشه!⁣
⁣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/105586" target="_blank">📅 15:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105585">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b748609641.mp4?token=ZQjuDoRmbD5zTIG4MC3M9NjVj0xsZnN7G7_l8DWAIz1bs2SKjtHNIfKqNrXWaEA5pK4fgPItx4wcQB3iZWzX3xxFGU8h6vcuBkpOPMonnECSe2ZoC8XU8oL7Ejv8FwDBihhny0ZJ7MiaomZSfwlMzkDgda-bTSyPlk7IiDN6qXN51Y5PUceHHQHb7M5S09jWFJw4TWozrHKBwvTc2JUMWbvHInbBHw_MpxCvV-BAs2zixWiy_SYqMhmoSWTd8FdRyY3ZpVP2ZptvaOFFkH3jjeZXxQF180jEj1JIjGbHTrcrPWxI5Jfja4Kd1VEAEH7TH8GPeJeQ2zLQGZdA_CyhgUUYpQ23cBf0Pk0RVtYZxV9PUr_L3l8nd4Dnsk5tWA17hZiPlqiLikVCSSbpisfa6FodmL6io58lr2NGylQpHst2nz-opLtwhjrV1e1yRUo5zxNJef7qbhMbEcRzszd3MldcCs5qn2TxkMTsppVLDbHLfTdbQUQInBJAEIzd5tvKe1AZ1y2MFS1j1vBX2UJnwK8F02oUMQaR0vkY6FJKmd6Q0d8Xmd7Vrum7rOZz2KwQCx8sH8vAEyJglCPsEvwf2R6LdvyiTfJKW-iDre1s1cmS6sgTHjMAfWP639ZUsRMBjERkaPlad3ssyMQVJ-GLJ9_3XetgwFlVCjEKmhzWZXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b748609641.mp4?token=ZQjuDoRmbD5zTIG4MC3M9NjVj0xsZnN7G7_l8DWAIz1bs2SKjtHNIfKqNrXWaEA5pK4fgPItx4wcQB3iZWzX3xxFGU8h6vcuBkpOPMonnECSe2ZoC8XU8oL7Ejv8FwDBihhny0ZJ7MiaomZSfwlMzkDgda-bTSyPlk7IiDN6qXN51Y5PUceHHQHb7M5S09jWFJw4TWozrHKBwvTc2JUMWbvHInbBHw_MpxCvV-BAs2zixWiy_SYqMhmoSWTd8FdRyY3ZpVP2ZptvaOFFkH3jjeZXxQF180jEj1JIjGbHTrcrPWxI5Jfja4Kd1VEAEH7TH8GPeJeQ2zLQGZdA_CyhgUUYpQ23cBf0Pk0RVtYZxV9PUr_L3l8nd4Dnsk5tWA17hZiPlqiLikVCSSbpisfa6FodmL6io58lr2NGylQpHst2nz-opLtwhjrV1e1yRUo5zxNJef7qbhMbEcRzszd3MldcCs5qn2TxkMTsppVLDbHLfTdbQUQInBJAEIzd5tvKe1AZ1y2MFS1j1vBX2UJnwK8F02oUMQaR0vkY6FJKmd6Q0d8Xmd7Vrum7rOZz2KwQCx8sH8vAEyJglCPsEvwf2R6LdvyiTfJKW-iDre1s1cmS6sgTHjMAfWP639ZUsRMBjERkaPlad3ssyMQVJ-GLJ9_3XetgwFlVCjEKmhzWZXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⛔️
🇮🇷
🇮🇷
لب‌خوانی صحبت‌ها در صحنه جنجالی داربی؛ کنعانی‌زادگان درخواست احترام گذاشتن داشت
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105585" target="_blank">📅 14:50 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105584">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t9EOsW3idmBknGM_D8C6plIZEtVKSpHPqkHwrUk1lYwsQT76RW5ADhzbFGBkq0iMQzX-2jdyom5Gjbc4NihEPfU5Tao31X2VbzZdsuNz3NSbPulf2oHbd6gIGhvLtz5Q-FJmzyVpX-3bXWzs8HeJnq8DGUWoSPZoEPGuChNObsiUm8e1NR88_LXTnvYZtBLb9pxy38tuRMbASOtTCUWzN4gGBTY6J6fyzNFOSzecUgC298mElzGNi4tKgGAIwVQICkOVrbp-YpxfdtEJhv1v4XO_3tCCcP6whmsFf1M08WqqRLe17qMw4lLiraLKrXwumnkJLPvmpBiXOjp9VqcFFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
🇮🇷
💸
هلدینگ‌خلیج‌فارس مالک باشگاه استقلال اعلام کرد که در ۱۲ ماهه منتهی به ۳۱ خرداد ۱۴۰۵ موفق به کسب سود خالص بیش 187 هزار میلیارد تومانی شده است که در مقایسه با مدت مشابه سال گذشته حدود پنجاه درصد افزایش داشته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/105584" target="_blank">📅 14:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105583">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf4edadd1d.mp4?token=fVIr5U7-0dUbArKO6qWZsve93OiFC4G9z1DpKVlwLTWuCjO3CLp7TP4AzQcnq1L7qmttEvRQq2NtZurbTe0HS5LWzyALcT9zrdQobmi_Pmcmn8n3b6VACC2Pcd9--QHZiPRyIucmZzeMCdwZOdEC2cERXrvgBeTDs34_V3nS--087tMmclnxzGXrKHmjPJ7sXN1SQJPwYih6mlkK0GOtOx62iEV1j-bku0--hM9rFePmc0SasVyS-B2JUAi-H7ZwXBW1Ny0o91QY8VhZXAbLkVCElpdA-lxOpDe1qQC24xgjcDw-Nc3kLc5JDbApPqCKjA5kEvQn0NoZrcFiWeKBLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf4edadd1d.mp4?token=fVIr5U7-0dUbArKO6qWZsve93OiFC4G9z1DpKVlwLTWuCjO3CLp7TP4AzQcnq1L7qmttEvRQq2NtZurbTe0HS5LWzyALcT9zrdQobmi_Pmcmn8n3b6VACC2Pcd9--QHZiPRyIucmZzeMCdwZOdEC2cERXrvgBeTDs34_V3nS--087tMmclnxzGXrKHmjPJ7sXN1SQJPwYih6mlkK0GOtOx62iEV1j-bku0--hM9rFePmc0SasVyS-B2JUAi-H7ZwXBW1Ny0o91QY8VhZXAbLkVCElpdA-lxOpDe1qQC24xgjcDw-Nc3kLc5JDbApPqCKjA5kEvQn0NoZrcFiWeKBLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇪🇸
🇪🇸
آیا پنالتی امباپه باید تکرار میشد؟⁣
📹
تحلیل صحنه پنالتی توسط روزنامه مارکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/105583" target="_blank">📅 14:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105582">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b71a26a715.mp4?token=U39jR6Zaq0ClX2XpBUUoMC9mzMgkc46MgiB65mta96iNokhCwE7bIMKfUioOTFWnfZLrPKvg3Rr8pITh6dGtOCQvjD3CnRzf5y3VNVt154ALyqwxnh2gPmR9MVeAqdPWLSjXHZyQz36BdVxJ5ubm7gKwBuVnVWoXwbyl0vC2VbLGZ4E2FdAYh0zOZ5uWnwhYaZd8UMPjY3znT1rz7Nxx2BsW5-CvYtQ3GsR-Z_nHdAhKd1RBs-1R-5RBKVUuHpPrt5pr0frpcBDT94gc7EHAgOQ32N-y-miZPLxOyshO9ulWijb3vTZSasfDQNbpi2V83fwCsVFfEEOkaNf5UDTIGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b71a26a715.mp4?token=U39jR6Zaq0ClX2XpBUUoMC9mzMgkc46MgiB65mta96iNokhCwE7bIMKfUioOTFWnfZLrPKvg3Rr8pITh6dGtOCQvjD3CnRzf5y3VNVt154ALyqwxnh2gPmR9MVeAqdPWLSjXHZyQz36BdVxJ5ubm7gKwBuVnVWoXwbyl0vC2VbLGZ4E2FdAYh0zOZ5uWnwhYaZd8UMPjY3znT1rz7Nxx2BsW5-CvYtQ3GsR-Z_nHdAhKd1RBs-1R-5RBKVUuHpPrt5pr0frpcBDT94gc7EHAgOQ32N-y-miZPLxOyshO9ulWijb3vTZSasfDQNbpi2V83fwCsVFfEEOkaNf5UDTIGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😁
😁
😁
😁
وضعیت دیشب فوتبالیا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/105582" target="_blank">📅 13:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105581">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFe6uqEd4DT_H4hwibxzPHd6U0KdY7QRzlJp0eq8zO7EDBfLGcnZXCrIiA-gV0o-y8IBOXNEI_XpyY1dkVFUMGtaZgT9nhG0fnjdqEJCClWMoMrUcBxO5ulG60uq_rdtfycnj9TxD7ShlhI3H0rSDSwwhc0RRFCFncqpmk5ZJmnP9xE67WlEHhf-eq8RqaEJnurKGqqMU_MIWAb2YzAyBWptjp-wCTBdQfkMAEfDw3bwFds9Z7UaseTUxPMqzHczqGGlcZMQbPZGFzT-5D4s_cPQbTbIJiPntNKv-1AZxj2upNRkq4Iae0F7NXn2x7b5FJk7g4lRLyZizw66o3Pmaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
20 تیم برتر جهان، رتبه‌بندی شده بر اساس ارزش‌های بازار، طبق داده‌های سایت ترانسفرمارکت
💸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/105581" target="_blank">📅 13:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105580">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
⭕️
⭕️
🇮🇷
براساس گزارش برخی منابع خبری، سهراب بختیاری‌زاده به تاجرنیا اعلام کرده که زمینه فسخ قرارداد با صالح‌حردانی را فراهم کند و دیگر قصدی برای استفاده از این بازیکن در تیمش ندارد! به عبارتی از این لحظه استقلالی‌ها باید از بین سهراب و حردانی یکی را انتخاب…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/105580" target="_blank">📅 13:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105579">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
⭕️
⭕️
🇮🇷
براساس گزارش برخی منابع خبری، سهراب بختیاری‌زاده به تاجرنیا اعلام کرده که زمینه فسخ قرارداد با صالح‌حردانی را فراهم کند و دیگر قصدی برای استفاده از این بازیکن در تیمش ندارد! به عبارتی از این لحظه استقلالی‌ها باید از بین سهراب و حردانی یکی را انتخاب…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/105579" target="_blank">📅 12:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105578">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
‼️
🇮🇷
سهراب بختیاری‌زاده درخواست برخی از پیشکسوتان و بازیکنان استقلال برای بخشیدن صالح‌حردانی را رد کرد و نام این بازیکن را برای بازی فردا مقابل آلومینیوم اراک خط زد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/105578" target="_blank">📅 12:47 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105577">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb7600cfd5.mp4?token=iomDK0C62Bied5CjaZXz-6ucYN_cxmVlVkuj_O-t3t4mjL4brCKh2USwQeTMBLYifxKAiycp0mEInDGM4lAExEZA33BNPzkpS6Cfdaaai5mEOcm78lCIrk2EiOBCYOLOR1X84BWfdBnwp5388tmPalbjqJxDKpzw18DEpcC2GzFdSR63rlyXHxzSJTZAGTnrdR87fL3FK0r6kjYB-mePLKoy88HH77vPwtunm1AfLJiNgwXB_T_oS5TOARRN6KLHshLWp6n06ZmF3oWDmsnUCaMIxSGC-pKWYym86G3o289rBFt_u9_ksL0TkqIB65L5kusVdYPSW5xMCU7t21pBEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb7600cfd5.mp4?token=iomDK0C62Bied5CjaZXz-6ucYN_cxmVlVkuj_O-t3t4mjL4brCKh2USwQeTMBLYifxKAiycp0mEInDGM4lAExEZA33BNPzkpS6Cfdaaai5mEOcm78lCIrk2EiOBCYOLOR1X84BWfdBnwp5388tmPalbjqJxDKpzw18DEpcC2GzFdSR63rlyXHxzSJTZAGTnrdR87fL3FK0r6kjYB-mePLKoy88HH77vPwtunm1AfLJiNgwXB_T_oS5TOARRN6KLHshLWp6n06ZmF3oWDmsnUCaMIxSGC-pKWYym86G3o289rBFt_u9_ksL0TkqIB65L5kusVdYPSW5xMCU7t21pBEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
وضعیت دخترای حشری تایلندی بعد دیدن پرسنل ناو هواپیمابر آبراهام لینکلن در پاتایا برای تعطیلات!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/105577" target="_blank">📅 12:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105576">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🇪🇸
لامین‌یامال در آخرین تمرین بارسا پیش از بازی با والنسیا بدلایل نامشخص غایبه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/105576" target="_blank">📅 11:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105575">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8Schs_ZW7GEfVpdRoTw468X5ZPDrXQxFvqs8Uc3ElzS0KkkEkFA7xiH0N1IZwLq7Bl8npAC0dq7lWNgfJO30NmaeD3xNORIjqzLUenrrire4IvO24WASLpXk1Wv1bo_lvjxVWM4F1qMrgL0U9SsMR0eQ4G3H5JlN305wCU9oHgFP43DTfhDSjqwqYVkeFeAhO4kr9E0TTMfgiGBe2_2vD8Egqb-N-qwp8FfTpH3tGUzGa3wmk1bQGt7_L0r5OTk1GwJBCtvFINR7EsDRHY2ITrVeEo95PnsidWuhCXZ3B3D_x1eVdcRbD1qM1BLYw_CnHI6Z--Jd2D_mfchyTSY6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج رئال‌مادرید در ورزشگاه بتیس از سال ۲۰۲۱
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/105575" target="_blank">📅 11:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105574">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c140b1799.mp4?token=SfVHXH0YDFrYQul9w6avorAO3PLiW7saWU69LefzDSZWEzgzoaUD7oWeg1vuu7fhB_fHTUSVFO-E-WK2pT4DXQfgS91OU5J3w9JnyQdAOJb11_OlbQ9qWiCxAtD0eYKAF9yo6yVz1a0CIVvSxM1AfZJ---QglyBqIBH_s-qifdVQCJv3SfokK9deN9ixOEGWI3n7NmYAyX2dIv58vIbFMB_57renhHfpCle63s7CGd7gbbh3AlSJ247Gp6TlJ4cO30d1tduBycFkmAWO9Vow371w_V6EpijMv1JmuuloJz9SjWrGJ7ISg6LUXpdI23HQ8kEDOzYri_gMvbI8FwGAWZ4awUdGoDM_9m3-ay-b4uxOAy7v0dNDumt_rCsUJSwyuxTPOd0u1FPKak3b69GZaxtxTxTx0qMdXFhaEEEpShzureR5jo6Ma45rs4nHRoSq1go5bgV-LbOZlXOTi1VUo2sbAZSYWcTlqlQbLNH8oz5Xl3oovL2Y3S3032UKbdobb_qZZUdHzNmqP_2La1X1Y9-_J90D4hLr1DqN7hAoVxrvkwJMkezm5Lu_vV2o2uYetS8YhlR4rn4_bTc4ZMdOGXcAJ_9sJe4aBT9BZsKISlcUe0e4KYNinuB219sHZZAJ1C1GmJ0to5E1ZM7VkD8kjHjpxy7kBI7hqIFYACr-Dm8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c140b1799.mp4?token=SfVHXH0YDFrYQul9w6avorAO3PLiW7saWU69LefzDSZWEzgzoaUD7oWeg1vuu7fhB_fHTUSVFO-E-WK2pT4DXQfgS91OU5J3w9JnyQdAOJb11_OlbQ9qWiCxAtD0eYKAF9yo6yVz1a0CIVvSxM1AfZJ---QglyBqIBH_s-qifdVQCJv3SfokK9deN9ixOEGWI3n7NmYAyX2dIv58vIbFMB_57renhHfpCle63s7CGd7gbbh3AlSJ247Gp6TlJ4cO30d1tduBycFkmAWO9Vow371w_V6EpijMv1JmuuloJz9SjWrGJ7ISg6LUXpdI23HQ8kEDOzYri_gMvbI8FwGAWZ4awUdGoDM_9m3-ay-b4uxOAy7v0dNDumt_rCsUJSwyuxTPOd0u1FPKak3b69GZaxtxTxTx0qMdXFhaEEEpShzureR5jo6Ma45rs4nHRoSq1go5bgV-LbOZlXOTi1VUo2sbAZSYWcTlqlQbLNH8oz5Xl3oovL2Y3S3032UKbdobb_qZZUdHzNmqP_2La1X1Y9-_J90D4hLr1DqN7hAoVxrvkwJMkezm5Lu_vV2o2uYetS8YhlR4rn4_bTc4ZMdOGXcAJ_9sJe4aBT9BZsKISlcUe0e4KYNinuB219sHZZAJ1C1GmJ0to5E1ZM7VkD8kjHjpxy7kBI7hqIFYACr-Dm8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
زوج فوق‌العاده پشم‌ریزون ازه و اولیسه در تیم کریستال‌پالاس دو سال پیش رو ببینید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/105574" target="_blank">📅 11:29 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105573">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105573" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/105573" target="_blank">📅 11:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105572">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CS6dQucc_JwCkdQ850nox8pEKGRIKu8ZO9RuOCa2obhNCNuEoFWVahH3sDyDYIHiVhyqQnjffw8_G5FPDA2rKFYSxAywffMhwh_iExbnuQVIxa8m0kw5WIfmYfHF-4onEjKvHm4n_y50vBX-ViShnmSywVY6HE3gdIEdZjfHVxC8KkDdgTEHNI4VDw8cdhts6-phP5ZgT38JcsO2JFPgcHoOu0eUbHW7y50-nUcolBJI--TAJQfXlvuYdsakIt3QhOQBCPEMfDD_cSv8sAw5Zw4g1jt5ELvPhrTN71B3z3yXLjOMwNR38PcKaQW3ghMMS3z95Fn40s8tpfBP5FNM4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
بورنموث
🆚
نیوکاسل
کاونتری
🆚
منچستر سیتی
تاتنهام
🆚
ناتینگهام فارست
اتلتیکو مادرید
🆚
اتلتیکو بیلبائو
ناپولی
🆚
اینتر
آتالانتا
🆚
رم
دورتموند
🆚
هوفنهایم
بایرن مونیخ
🆚
شالکه
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/105572" target="_blank">📅 11:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105571">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72c6aac1de.mp4?token=e2sz2yq-6BCgKjx12A9Ftu_Mgr3saV5m9G2Hhf1waXyaIWBCJFbPo9dYQMA6z5s1X1pzQHsYHCoue9YyRuBBgFD6KeihmEEGCEmYnjkLlcoycCNM0Hmx16fJJWpYJXalqYQw7JS9nVU7kGgXU_-3tkmrcaQff-DmPRPVOvAHLB-ZORG6GppTanqNe_7AjTYbjq-tc2uMLLjwz1UjsfmZ5zBvjcKta1rlsFhOH0KHPXQ6ZNI6prxPkHg99zVOinDF-uYU5WxH6R41AIsFlFQwc9_L8gOXJ9XI4KcrUZ7YgYVqOrWo7ujSk9Y2jgyJ_hkkXBnmN-a8G7nEq2M_eVB1b1wkFSLen2ZG6z9AwlRgudJjjiJ97jFSOnPQiq4KCKWhtML67pRS9cBMGBNbz1pjRmQ6abx7WmQiX1c2_354nHUmJe4IEMrbtQCIxq--7bBD1sIPZ6tK7xOPyYx9E7JBSqW9IUw2jmwPee52SNejNi99m8XYXSe3mt6GKpCJsWb7bMLovSbe3W78Un-pL80B74-DdMCClwY6XDWyH_bD4Knnne_fj_oBUuHfBRAcVvc93jNN29JwZYsa02ywWWAa3ov6sWx3DVO0O_OBPEmLm80BhaI73gKcCRXVSvik6AKDDx0wqBPmqiKNn9XF9TvJzuXZHaL6o6PnGS2MgdLQu_c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72c6aac1de.mp4?token=e2sz2yq-6BCgKjx12A9Ftu_Mgr3saV5m9G2Hhf1waXyaIWBCJFbPo9dYQMA6z5s1X1pzQHsYHCoue9YyRuBBgFD6KeihmEEGCEmYnjkLlcoycCNM0Hmx16fJJWpYJXalqYQw7JS9nVU7kGgXU_-3tkmrcaQff-DmPRPVOvAHLB-ZORG6GppTanqNe_7AjTYbjq-tc2uMLLjwz1UjsfmZ5zBvjcKta1rlsFhOH0KHPXQ6ZNI6prxPkHg99zVOinDF-uYU5WxH6R41AIsFlFQwc9_L8gOXJ9XI4KcrUZ7YgYVqOrWo7ujSk9Y2jgyJ_hkkXBnmN-a8G7nEq2M_eVB1b1wkFSLen2ZG6z9AwlRgudJjjiJ97jFSOnPQiq4KCKWhtML67pRS9cBMGBNbz1pjRmQ6abx7WmQiX1c2_354nHUmJe4IEMrbtQCIxq--7bBD1sIPZ6tK7xOPyYx9E7JBSqW9IUw2jmwPee52SNejNi99m8XYXSe3mt6GKpCJsWb7bMLovSbe3W78Un-pL80B74-DdMCClwY6XDWyH_bD4Knnne_fj_oBUuHfBRAcVvc93jNN29JwZYsa02ywWWAa3ov6sWx3DVO0O_OBPEmLm80BhaI73gKcCRXVSvik6AKDDx0wqBPmqiKNn9XF9TvJzuXZHaL6o6PnGS2MgdLQu_c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
واکنش مورینیو‌‌ و نیمکت‌نشینان رئال‌مادرید به پنالتی که امباپه از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/105571" target="_blank">📅 11:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105570">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
✅
🇮🇷
صالح‌حردانی که دیشب یک استوری در حمایت از سهراب بختیاری‌زاده گذاشته بود، استوری خود را حذف کرده! با این حال سرپرست آبی‌ها به حردانی اطمینان داده که تنها با یک عذرخواهی ساده می‌تواند به تمرینات تیمش برگردد که تا این لحظه این اتفاقی از سوی حردانی رخ نداده…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/105570" target="_blank">📅 10:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105569">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccf1cf6a70.mp4?token=nlMBg9BPc2QDcLWqr40KGe4C2FApXsdxHUvCgSN-Vm2kQGur_kspkvJa64R8btmbauG3772ScPRMnuUiO7baMFyfyHy-AM-QvteWuaEA15rrqN6Xm_CWJ0mocDcCCiudkYJM5aj2_glCY5jrSmhMwTaQdv-lxIZ_ar65ONhUWKtfcxhQGmwwecry4xr3x0wHDpIWYiQ15XwiZ-sBUz3WugO8qDvxQgFvjb7hfMSHWC4kTnI38WjdGld3sgVeyE8890XE9QZfu8KRFbFlEYKwlk7URrw5tEpvefMbRn-OlcofWI9U5uEsaX7GDyIdYnTp0UCMvT74fIGYRajGJ7hOZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccf1cf6a70.mp4?token=nlMBg9BPc2QDcLWqr40KGe4C2FApXsdxHUvCgSN-Vm2kQGur_kspkvJa64R8btmbauG3772ScPRMnuUiO7baMFyfyHy-AM-QvteWuaEA15rrqN6Xm_CWJ0mocDcCCiudkYJM5aj2_glCY5jrSmhMwTaQdv-lxIZ_ar65ONhUWKtfcxhQGmwwecry4xr3x0wHDpIWYiQ15XwiZ-sBUz3WugO8qDvxQgFvjb7hfMSHWC4kTnI38WjdGld3sgVeyE8890XE9QZfu8KRFbFlEYKwlk7URrw5tEpvefMbRn-OlcofWI9U5uEsaX7GDyIdYnTp0UCMvT74fIGYRajGJ7hOZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇪🇸
اولین شکست فصل رئال در خانه بتیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/105569" target="_blank">📅 10:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105568">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQXZLKOozhID2sbLhADObvbb9RbgrZD2abGubfLPichqQUVvE6jWCKiuTzbIMkEC0EaTxXujMHA5m4NugSEZc8VKFEyF1nwnpLkJNqg0KAnx82Ne_nAUOn5YP-i7daV0InKvbyKlZLO0n-ON7a_H9T4mzrQI3gVtWdSpj2uQOLgnfHGnrNI8nhyKFu564btBDI-kL4YXsXXRf593EntdK_Qqv4ykyg-6QZRzGTMGTQkWL08iSctJKZlokB6A55jYWZ03Na7xKUhvU0PXYckUe_MsiXi1kcYK1z8vihqNcgmiR6ql6-v1_hbfX_HkefRDf0M8B-9nHRMC8vhU5tHYAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🇫🇷
لوئیز انریکه درباره نتایج ضعیف تیمش: اگر دوست‌داشتید میتونیم روی قهرمان این‌فصل فرانسه شرط‌ ببندیم هرچند که من شرطی که خواهم بست رو لو نمیدم
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/105568" target="_blank">📅 10:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105567">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0094c6fe9.mp4?token=Qnb289lJilqNXfxTHv0TyiBQyo6PGfdgYSEk7a5MlTtfZRw-EdLgyFtk4YzKfUPZixzhVAujWWURv5PNLknwpRCFgpfdfxo5VO-g99fqeiCrh3axN68wXzOJVjK_NOY6Rg63uenmo8Iwctg6x261aobAMPlXuUi9UFaspPONj-cstE8rRBYCEpRzXS0LP9HnipmbPgzXxQ9no4yb_W_q_bTy3_PsoXXLAp1TkzFg2f30CqV60TGh0pE9YF4KklsBoisiqGTZNIduAFSo0F4P-nIIF_9oVGn9cKpSwmLoskL4cT-YkAZnqXfJx5t3yaULEoc63VaWLG_DyDV4DWDTrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0094c6fe9.mp4?token=Qnb289lJilqNXfxTHv0TyiBQyo6PGfdgYSEk7a5MlTtfZRw-EdLgyFtk4YzKfUPZixzhVAujWWURv5PNLknwpRCFgpfdfxo5VO-g99fqeiCrh3axN68wXzOJVjK_NOY6Rg63uenmo8Iwctg6x261aobAMPlXuUi9UFaspPONj-cstE8rRBYCEpRzXS0LP9HnipmbPgzXxQ9no4yb_W_q_bTy3_PsoXXLAp1TkzFg2f30CqV60TGh0pE9YF4KklsBoisiqGTZNIduAFSo0F4P-nIIF_9oVGn9cKpSwmLoskL4cT-YkAZnqXfJx5t3yaULEoc63VaWLG_DyDV4DWDTrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
به‌نظر شما دلیل فحاشی به شجاع خلیل‌زاده در ورزشگاه عادل فردوسی‌پور است یا رفتارهای او در داخل زمین؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/105567" target="_blank">📅 10:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105566">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ffae934b6.mp4?token=vyv--LwPqODHK5OCV6bg2GqwxR-eanD6FlTnbDe98NsQmx9L7CBuB3opJ5vKxi41YiyO88gcIj3XEwjwABkey__SGsXJFH6_0VdAob4LXd6bH8H2WkG28BR7o3wU2Rl8bUinnNTnMhbodVL2dwJ1coNPW_sebxmsSbC6GSOu2Fm0_jMQ3pkTY7qf6u9zb2Q5_XwN1kAB57ULTB0UQfb4ZGTQrOqSvJ_2l9fLilyTEuLcRKLq6HnvKRcj9XT7NIWfkwg506F-kX6J3Lsl7XNizeKjkBEM5UsXgjwer9qOZOI4KAuHZh9hVdtZ7W0O-EUnFY5pahDS5szC1SNmPl_dbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ffae934b6.mp4?token=vyv--LwPqODHK5OCV6bg2GqwxR-eanD6FlTnbDe98NsQmx9L7CBuB3opJ5vKxi41YiyO88gcIj3XEwjwABkey__SGsXJFH6_0VdAob4LXd6bH8H2WkG28BR7o3wU2Rl8bUinnNTnMhbodVL2dwJ1coNPW_sebxmsSbC6GSOu2Fm0_jMQ3pkTY7qf6u9zb2Q5_XwN1kAB57ULTB0UQfb4ZGTQrOqSvJ_2l9fLilyTEuLcRKLq6HnvKRcj9XT7NIWfkwg506F-kX6J3Lsl7XNizeKjkBEM5UsXgjwer9qOZOI4KAuHZh9hVdtZ7W0O-EUnFY5pahDS5szC1SNmPl_dbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
‌مخ زنی به سبک مهران مدیری در سریال جدید مرد سه‌هزار چهره: فقط اونجاش که میگه برای من منگنه بشید
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/105566" target="_blank">📅 09:50 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105565">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fe613df04.mp4?token=t1WkpF4JP6pJquU6GRk3C4yv-70mt6gx5D1YeDXJB1EpcpRd3BD5MLxeR7EXq7MNVqAIbXuD6TUNMTVKtH9R9qOvVc0hLiQscxdRsH99OMSXeDWm6iJxm1X671boZRVeutDeZtgU8iwwHq8q1FdiD528QqM2rpZkbQ_PcVPjtnObN70rGdHu0MUkeqrOua5pBRdANYaEzX-Qc82cBqG_WToaR8mzb5htetP9r607cd0zbaAUPLMVYEwhv6SYhprcopHVtk426M7_9eSzm_WoFZ-uMdJsM4MiRm2XuXHT1w_kOvEZWOAqzlk3WhIK0UZLweULRT3tT1kjAE1E28Di3pCL5GXElOFma1eL7zyrB03verJ5KyIGdY12J4symibQFZ6dEh7JQjOQKQo0km-UIjidGdvLDdQywydHld-Wz7I9z7wqZw2G8Vgp5vgPrqM7upmB3B8vuMy8Qiw-MMkTmIESAtSHTEfL_Kn2rGqATJH-JywzV0eV8bJ2d1x5A09FWZDLipYZw9B7GmEfHDIZ50Ub8dn94vtdyNsLnmHpJuP1T16tYUzadZF37V0qy1oR7D5_lmc76XHahm76R7wpx1lgVolkccReH3BxEqP1UsNIXhWC6d4MbJt5C3rLUJegSO9ZS_dkox4f5bF6ttwMEmH6hjFAk2vl4JUaZUE_aZE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fe613df04.mp4?token=t1WkpF4JP6pJquU6GRk3C4yv-70mt6gx5D1YeDXJB1EpcpRd3BD5MLxeR7EXq7MNVqAIbXuD6TUNMTVKtH9R9qOvVc0hLiQscxdRsH99OMSXeDWm6iJxm1X671boZRVeutDeZtgU8iwwHq8q1FdiD528QqM2rpZkbQ_PcVPjtnObN70rGdHu0MUkeqrOua5pBRdANYaEzX-Qc82cBqG_WToaR8mzb5htetP9r607cd0zbaAUPLMVYEwhv6SYhprcopHVtk426M7_9eSzm_WoFZ-uMdJsM4MiRm2XuXHT1w_kOvEZWOAqzlk3WhIK0UZLweULRT3tT1kjAE1E28Di3pCL5GXElOFma1eL7zyrB03verJ5KyIGdY12J4symibQFZ6dEh7JQjOQKQo0km-UIjidGdvLDdQywydHld-Wz7I9z7wqZw2G8Vgp5vgPrqM7upmB3B8vuMy8Qiw-MMkTmIESAtSHTEfL_Kn2rGqATJH-JywzV0eV8bJ2d1x5A09FWZDLipYZw9B7GmEfHDIZ50Ub8dn94vtdyNsLnmHpJuP1T16tYUzadZF37V0qy1oR7D5_lmc76XHahm76R7wpx1lgVolkccReH3BxEqP1UsNIXhWC6d4MbJt5C3rLUJegSO9ZS_dkox4f5bF6ttwMEmH6hjFAk2vl4JUaZUE_aZE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
باشگاه نوریچ سیتی هر سال نشست خبری ویژه‌ای با عنوان "نشست خبری با قناری‌های نوجوان" برای هوادارای نوجوانش برگزار می‌کنه تا بتونن مستقیماً سؤالاتشون رو از سرمربی تیم بپرسن. امسال هم این برنامه برگزار شد و البته با یه اتفاق ویژه همراه بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/105565" target="_blank">📅 09:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105564">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e01f66133f.mp4?token=LELrQKSU9iAzoV5kr0ThNsFD4MlG2ywJtEa9wuL27NqNhlLTBf7w0Q3T8t7GTuOVYJFC3nVTY0xC_40kwC6tjhTFZEjdYyZ9CQTZfYKicvPZaooBPCOljqY91iSEaSb-6AJceH_wFltf2FaiY0kBQOGLAgF8E5ZL11QDoDmQ6rDp5ZxbdARiEVpdNbRypX9dcRre7IsLJxXyx1N5Sxn4f8cK30pvtJdBvXNrfZKHMXD-Mjm7NKXPAftE01hTlylQgb7gb7haYUWtGmAv8h1i2KbAyABf5JpbovlOuaPKj777icAkVCscS4iHvHAPSHZ4fQi3_R9AX7tb-ukfvDRWuXzt13e2ounxK9aAtt9nttfauJj7n_2AW56icTgjZR3i7G1IRRKNYUB19CEixrXFpDz8pfE1jrBnV8YSca7AGyvz91eB4c2DehaycNtixHLCwFkLyqcEIAIfktTfT-6nI_aSmQFqRpyvEsAQHRX2zXQGP2sIVBTAoz-iOohJUM3ljjF4cnjXmcIoGaRRXOY3CRPwGbNPAK13VTD1Fda_it9HTpJAR0mVMvHS_UwkRxyxpu77PIcUGUwjqwb2IKvFJsjg60XpHtXmL4Tiuks3a2ZIOKFYBEpgKpY3QcvZxGUx5k9bN9mtOIoNcZfxSQDmec7HoHTOa3079IgTdqItM4U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e01f66133f.mp4?token=LELrQKSU9iAzoV5kr0ThNsFD4MlG2ywJtEa9wuL27NqNhlLTBf7w0Q3T8t7GTuOVYJFC3nVTY0xC_40kwC6tjhTFZEjdYyZ9CQTZfYKicvPZaooBPCOljqY91iSEaSb-6AJceH_wFltf2FaiY0kBQOGLAgF8E5ZL11QDoDmQ6rDp5ZxbdARiEVpdNbRypX9dcRre7IsLJxXyx1N5Sxn4f8cK30pvtJdBvXNrfZKHMXD-Mjm7NKXPAftE01hTlylQgb7gb7haYUWtGmAv8h1i2KbAyABf5JpbovlOuaPKj777icAkVCscS4iHvHAPSHZ4fQi3_R9AX7tb-ukfvDRWuXzt13e2ounxK9aAtt9nttfauJj7n_2AW56icTgjZR3i7G1IRRKNYUB19CEixrXFpDz8pfE1jrBnV8YSca7AGyvz91eB4c2DehaycNtixHLCwFkLyqcEIAIfktTfT-6nI_aSmQFqRpyvEsAQHRX2zXQGP2sIVBTAoz-iOohJUM3ljjF4cnjXmcIoGaRRXOY3CRPwGbNPAK13VTD1Fda_it9HTpJAR0mVMvHS_UwkRxyxpu77PIcUGUwjqwb2IKvFJsjg60XpHtXmL4Tiuks3a2ZIOKFYBEpgKpY3QcvZxGUx5k9bN9mtOIoNcZfxSQDmec7HoHTOa3079IgTdqItM4U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
بیرانوند: مردم فکر می‌کردند این آخرین جام‌جهانی ما باشد. میخواهیم در جام‌جهانی بعدی هم باشم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/105564" target="_blank">📅 09:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105563">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edf296c20c.mp4?token=HyPkFoOLkS1Xco2EJ7HAJ21JLaxmnXi2_UAEOqN3zLtQeu-Oz3W7uh5dsfGdTzfDMPot4Ar3vDZ2jlTlYC-MnaUvlOuGiI8rVUcw6QPAA_MC36pP8ugY1c6J4qxogY-XCkxSq2isk90kN2dPHq2f2K3TBGsuO6ubdZLpNCEmvu7Ksbryrb_KYlCzFgGPnxnlAxWshhOW3shGLlFl-nnCB509eh62vSD1KSOLo3tpEgmHXHEWYageMLC_Y8ShgtOcVpDNVW0xt7cYZ3zvFgEcudsbPEw09sfSkVGpQeGAZ9Fq9IFNMfoY65H24Wgbfu_IkRgRH0Vc-c8RyBMBsJiRdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edf296c20c.mp4?token=HyPkFoOLkS1Xco2EJ7HAJ21JLaxmnXi2_UAEOqN3zLtQeu-Oz3W7uh5dsfGdTzfDMPot4Ar3vDZ2jlTlYC-MnaUvlOuGiI8rVUcw6QPAA_MC36pP8ugY1c6J4qxogY-XCkxSq2isk90kN2dPHq2f2K3TBGsuO6ubdZLpNCEmvu7Ksbryrb_KYlCzFgGPnxnlAxWshhOW3shGLlFl-nnCB509eh62vSD1KSOLo3tpEgmHXHEWYageMLC_Y8ShgtOcVpDNVW0xt7cYZ3zvFgEcudsbPEw09sfSkVGpQeGAZ9Fq9IFNMfoY65H24Wgbfu_IkRgRH0Vc-c8RyBMBsJiRdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
🔥
جورجینا همسر CR7 با لباسی از برند گوچی در هشتاد و سومین دوره جشنواره فیلم ونیز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/105563" target="_blank">📅 08:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105562">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105562" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/105562" target="_blank">📅 01:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105561">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TbQ1TIsCRNUwMRFZmTriSIsl6PKelSrQ6vmPk1N1hINrkB99Tr6H_E7CDEXgedW7JwE4vpMLoMtpZvCYC5yXes5u1iN9XFxRCk7ymWyHrSloP0KJssh78c_k333BT4Bay6-xsmd3_p4yC4Akw8Ze7t7hAzxQXYGK4q6TjvdsOVxCOVD6nPYlSbEgqmglTWiESduFYBp4TZFfyG_dYVMCEM_8wpE-cC3j3__M3xpAlnBVn7MhG4Z9KkQXDDYuC7mT60bS9fwcJiiZtBi8mA6qgf1oo1CT0gCKGK4HUbsvZFZKWxQqlOVVh2dwyCfZ_27rnkE12dFgs0KS9vTIpORyMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/105561" target="_blank">📅 01:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105560">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/105560" target="_blank">📅 01:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105559">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b6612a039.mp4?token=MHONacyN4a-t60yS5mjODdiWjjMijKzX7NQgcLCOJ3YFOjz8KaS5za1xCeDUPIWGNzrXNndt1S0i804ShmzYXEPGuZ2LM7Lqu3pXqH2Q1u_IxRCkkjQEpuoR45z0PHTuyokzRYNwoQwEltWeISwelSroNx6ochv4Qmq3RdKj6q20hVuYs8-WDY7oO-2Aey8AWOyoYv7gq7Zs5ft_9pruLQlI0ExpoD5alXJ-ftiM6vSqjgKy-rkmLcQHINmUuAfNy4BgDO0kn82fDNl1PV2wV_-y-qwt4fxalB8Y-IoCUbX6NE-xp_Yat_Gs56uy66slzzy_0rlZyfAHqRTpH2VR9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b6612a039.mp4?token=MHONacyN4a-t60yS5mjODdiWjjMijKzX7NQgcLCOJ3YFOjz8KaS5za1xCeDUPIWGNzrXNndt1S0i804ShmzYXEPGuZ2LM7Lqu3pXqH2Q1u_IxRCkkjQEpuoR45z0PHTuyokzRYNwoQwEltWeISwelSroNx6ochv4Qmq3RdKj6q20hVuYs8-WDY7oO-2Aey8AWOyoYv7gq7Zs5ft_9pruLQlI0ExpoD5alXJ-ftiM6vSqjgKy-rkmLcQHINmUuAfNy4BgDO0kn82fDNl1PV2wV_-y-qwt4fxalB8Y-IoCUbX6NE-xp_Yat_Gs56uy66slzzy_0rlZyfAHqRTpH2VR9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
رفتار سرد مورینیو و وینیسیوس بعد بازی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/105559" target="_blank">📅 01:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105558">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iENV3Y-hn3ebRodgNaIDwvAmaMlJA-Mjs3TZZZcOx4Hpec8Z9gXWB0H28880NnfpyjdsAYK--emJSUPgpRMmhvP9lJfwOy091L70E2UA3yRhXEdm8-Aszp-50w6Sg_2GQDDK_P_Z3aUzaULG0JxwW-IOFLyq_qltVj6EXAirnoytGe1eWuE3FOigzzNvorHaexz-t6aZhQD6KtENtX3aUKPEzMtPRmrmcnn0fJkKAGO0VDwcNIUqnm4FwbXOvzeGJATS966rV93GUAEw4H6eQwMHCIwQk6hVnmxGvHgH_LgNCr9dDFnbM4vONRHjde0Fon9qSQ4jTCySHiYaXmk9ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🇪🇸
#فکت
؛ در آخرین‌فصلی که رئال‌مادرید مورینیو مقابل بتیس در خارج از خانه باخت، آخر فصل بارسلونا با کسب ۱۰۰ امتیاز قهرمان لالیگا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/105558" target="_blank">📅 01:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105557">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPXak7p80vNpj_fWZZltiaZxm-EmQQdZRMHnJ1SoPYmLZfp4TwhGUoCeo6AeAkNBfl-NfeZGdPHWHj1iBvafIRjih4h1fps9x1f5PyCQE2R-hMZGRRVupohpV9D4NufbfbgWEymdLZzFnV7PRe7cGOgkOC966i6tZ9qjxT2cUxXKR-VF5PRSNV3_MzLrtdCQTg4wDxXkJJd2Z6_35Q6JqBX14SuelrXLWSPIzRTureUXfzUUp6MHWOERktau0ZbGJKVyNd7g-cnedw030tHGg2903k485mxqAVOR5RFgGEMi-OK0hkor6wwCnaFmt99mBwoaAoYQvQJP_yq6zndgoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
ژوزه مورینیو: عملکرد داور بنظرم مشکوک بود هرچند باید برم بررسی کنم. تعجب می‌کنم چرا نیمه‌اول به تیم بتیس حتی یه کارت زرد نداد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/105557" target="_blank">📅 01:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105556">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bv3tIYixe35QemoiI0VrVmDWZCvFsFSuEJ7beeFamNCqg6oz-Bqv302QPzPg8C3iNCFFBTIlJkwnC4VzlfDpWBwVvaAth3AAwZrQPmdRm1GzdrtVZHBoXwQ2inqnTBhyjBJSZGh02tS4Cigs5rKuwCi-594IgiTcCfIn48QBUoYSt6GKuAO-shBRnSkobF7KNmxi51U8RIoKtkBiwHZB6qU6Hp0CCKw4YTOKIJH9dShqXvpUkJoGOyGTQ1mE-4uUPjPyU4TGMI65rrv8TlHAAHK6PxWso1rCGQPzQtFqlh5i1D3idgTKCaSzuYHEhNfFB9r9vk6IRMztLbDOxvYFmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وسط ریدمان رئال‌مادرید گویا باید از اونور یه فکری به حال پاری‌سن‌ژرمن فلک زده بشه. سه تا بازی کردن دوتاشو مساوی گرفتن امشبم باختن! گویا اثرات جذب فران تورس داره خودش نشون میده
🤣
🤣
🤣
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/105556" target="_blank">📅 01:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105555">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9tvMt0y9AyHoI96QIQ5sUrX-QGzGIlUNlD-nCSz8zqYbaXxv9rbIKkr-jRgv1TMifs-cJ5WCqej0YQSGYFWeiyQ69n_K7HQNNrBUiaUgg9-fxB7RdO-4sk2ZzLN8nxo2Pq6TfFb1p6C92CAeAAXxZuSmPVl8QCqF7sw2AiklY9olFgw6slTqoVkWKAo348bVAYHg4EK4dTiR1XPy8IZvubuZP-_lmXLSK4UZ9OOnf5ysK2QEakUa820vaV3ONjhZpwCTOu_iXJV3nRJgeOJIooQkUwDsVzCZF8jVMDBxiU0tZvtPxB98myLFekHitE7hv33ZjQmqKCq3fJdR03FCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
ژوزه مورینیو: عملکرد داور بنظرم مشکوک بود هرچند باید برم بررسی کنم. تعجب می‌کنم چرا نیمه‌اول به تیم بتیس حتی یه کارت زرد نداد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/105555" target="_blank">📅 01:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105554">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🧕
البته گویا این صحنه هم آفساید شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/105554" target="_blank">📅 00:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105553">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAyrFQn0_AO01fsovyd5us5F_ElMGbFX5QTmhvkOB5jFHU0prH9z8GLVk49ATiGzOHgl_BCwfPkjvin2xU9ka5Yf2JdpDUOv4TFN-Ku3tbaMqABR50g0HBYoLMheQaXRmDhgLS862QlRjJOItBbzC1M-qn1MgryiouG54PIW2-VeP6CU7lWLk2tAz72ZRmvXVC5xR1UbL-Y1bNF7dFvBtcEkRhooNPK3GQqD8iAhwv02IFuG3lLwkZHdSLxANqvVRXft3JzpViIvM52yUv7Fssy67tlYGKgYxHJZc0YfvMzivqmgJs0F52l44F9uP70siLhtBU7weecn3kklxktW_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📊
🇪🇸
رئال مادرید در پنج فصل متوالی در لیگ، نتوانسته مقابل بتیس به پیروزی برسد [سه تساوی و دو باخت].
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/105553" target="_blank">📅 00:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105552">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPCK6AD4kXJxQPyLELQY4SGXd8dbcpcTyzxkpgHuzP2JKJst3aAYFWdhqH0xcY3uA_JkiLA4uTR9PFv1iwHHhC1qzwhhYZt2Ao4avkB6kG4xKx4aIxVfyAzxthU7Xhmfsdxch_KjLaHRI583X02j1yyKHJE0EddCUKo9iAnz_u67pc2lVZGQUHkq4U1dMRq1EF_FPQgn8_fa8-lJVQPdps7XX6dABLGNcz71ciNT9u7tHWImVIm8SdAQfQVgQJRgDG1NG15eu00YmlCGPQs6ritEK68B339V0Esjs0GxHZl42WPnk9PaPBOLxCQ-WATOzQx6KIuH26wxNq12DX6Bhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هفته‌چهارم لالیگا؛ نود دقیقه نفس‌گیر در خانه بتیس؛ رئال‌مادرید با زور پنالتی هم به امتیاز نرسید؛ پلگرینی مچ مورینیو را خواباند!
🇪🇸
رئال‌مادرید
😏
-
😃
رئال‌بتیس
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/105552" target="_blank">📅 00:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105551">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJLeHzL1x2GNrJuZALo5-y6dBbw4KiWnl6lJ8gmAXEt__XmDg3q9lulC_lpNbzw3z6C56OMLMYFJ7nSDqAcQTzSQD-FYKzZCbmk6cUvcud8qAS3PvRwkg0Geh8ITpeZywna1uzEnZHXrqQ07ETd3X2cOBavDJ4MiYT1njgZ7wgzn7EbvI_gpqZanRifYraOebW_uGmFdT8i9dnCu0EPNJjRK2O_DdesQt1XGR6GYnboTRJE3mm4RAsuyT47MLM4eZT7QccEi_Jx0hxETid12TXafBCWLcFyiD0VAdSy1KDaS7LfcS0j5aGq1OK6Pw_rpUwyXm-pMOpnIrdhpu_QJJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هفته‌چهارم لالیگا؛ نود دقیقه نفس‌گیر در خانه بتیس؛ رئال‌مادرید با زور پنالتی هم به امتیاز نرسید؛ پلگرینی مچ مورینیو را خواباند!
🇪🇸
رئال‌مادرید
😏
-
😃
رئال‌بتیس
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/105551" target="_blank">📅 00:36 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105550">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
داور میخواد پنالتی رو تکرار بده
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/105550" target="_blank">📅 00:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105549">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AE6jfLixIJt-yaneNJOWSXNSiZgDjKiOTCkrN80xcavxW7RjBjdRR8wEVz7YWLatU9DC-nldIFcbMx7ovJzENK153dzNq9ihWgjPsdOFkZC5yJwNshgGnbDwPVXvbegT46DJljEjmWga1vJ_-_fV0IkkRPEmTQxzDDLiaEKoHLP1eN-EEVOCh5s09gVTSa0v3OPkzmkN-EjDuvzmjHC5li5B7FNPjzFP-tNZsdaQCN_Z_m9Llf8hvAy0bUf2FjIGls1spB4DBChlgm8gvEhFWeRpJq7VK9fHUpy8e0s3qpxgi0MxLuR44lyJYwYG2K1gp671RMVUGzwkmKLcskTc3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
داور میخواد پنالتی رو تکرار بده
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/105549" target="_blank">📅 00:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105548">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">رئال‌مادرید بدشانسسسسسسس
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/105548" target="_blank">📅 00:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105547">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">وای خداااااااا چه شبی شده
😂
😂
😂
😭
🔥</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/105547" target="_blank">📅 00:32 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
