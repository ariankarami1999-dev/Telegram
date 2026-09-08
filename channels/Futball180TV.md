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
<img src="https://cdn5.telesco.pe/file/Yaaioy3-UDqBCk7s4tO3E9ewiMdgWfCc9iQxWU9z7MHKIUiN-AVimL0JU4zJQqxw2yzYACJUeucjostgr_PkYt-zmzoJxbP9pIDFtVtNp7Dotzl4TiCCbaxpY_HSEKfbeB7zu0WO5u0DKTZGc9tD65EWBXepATbPcvtMmIjAsYPolVHa0eCn7XH_DyxPkl_UAgwEHRU1JlKD9GGOLqUTYYF3qgUBoSKIHGVUEVkv0cbX_Db6TF7UanQEN46O6haNaAbteKs5AOjA9sU7deAehfR4LJNvZSehtvGRfXo8QMKXEbRQoA6DxkjCrJWhPuPbSZVlVR0VBQT-lEaUlZqxXw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 423K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-17 08:58:33</div>
<hr>

<div class="tg-post" id="msg-105847">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12456da477.mp4?token=kb2EC5JJtuTw88X7Q0jD7FnSTogxDN_EGXSGXIkE-1Ltjo594KJPb2WG59Ep2gx8Dfz_XB_jD9on_kOmQfzltI8-oAVrfpcD24Tl6S3gq_y94qDzmRZtjrIu7w61dsJUHfVsLm_eoSfRdT1EhZAontjBVD2ZUh6-c2vhw7iOLvn-2LT3IlY13qBAxlZXiW_6gsl5-RqitymuJWVSyjH9FUYGztzaVqK_W32xxQzZwL3mOEZJjG64RzD90ijnnyEtgkz-9cZr7DBi7nJjEifgfhwl329VRWCYWvDgDFzDO_ZZbmglGNPxU0F2Fw0eHK7T35ZH_YB3BXqypUiOhkdjIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12456da477.mp4?token=kb2EC5JJtuTw88X7Q0jD7FnSTogxDN_EGXSGXIkE-1Ltjo594KJPb2WG59Ep2gx8Dfz_XB_jD9on_kOmQfzltI8-oAVrfpcD24Tl6S3gq_y94qDzmRZtjrIu7w61dsJUHfVsLm_eoSfRdT1EhZAontjBVD2ZUh6-c2vhw7iOLvn-2LT3IlY13qBAxlZXiW_6gsl5-RqitymuJWVSyjH9FUYGztzaVqK_W32xxQzZwL3mOEZJjG64RzD90ijnnyEtgkz-9cZr7DBi7nJjEifgfhwl329VRWCYWvDgDFzDO_ZZbmglGNPxU0F2Fw0eHK7T35ZH_YB3BXqypUiOhkdjIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
پیام جدید وحید قلیچ به خداداد عزیزی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/Futball180TV/105847" target="_blank">📅 08:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105846">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105846" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/Futball180TV/105846" target="_blank">📅 01:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105845">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BBRkW8NH3gEwvPPnN-y0oifw07R2GMwa0rWLEX2HcNFletbrxtFP_q_DaZ9vh0hXaptSNN2dDiD18qfxofLrhNbpkGiPd7TKiejIHB0O2g3XfLgUF_3tmG5pCl87JrvIu7qo0-je7wCC2SOSng6fqlS3oSuf5d_K597KvNdqKyiRHC4SMnRokOLoco762M7nTVDAvIakys_VahocAmGWKCZwz45iNcFj8sksJeMMGoutouEiti-73QkjpMOOoYz3c7XTwrMmC8V1lMQ6X765RS6hPGrv-VGealY1zJWzQRt1bC-6nsy_7npUQkR7Ts7W3rbW5mI6m86vYMmvxDaiyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیرکس‌ بت می‌بردت وسط هیجان
US Open!
🎾
🔥
🦖
رقابت‌های نفس‌گیر، امتیازهای سرنوشت‌ساز و هیجانی که تا آخرین ضربه ادامه داره!
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/Futball180TV/105845" target="_blank">📅 01:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105844">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/Futball180TV/105844" target="_blank">📅 01:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105843">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94a89c6058.mp4?token=h7XnrwFM5AVDbHF1-KDJpeeuIyVt_rJNez7hzsVWZPwXq-piBap6BJNjxQFH1EYZG_eU-0vhgX1_ZpkEjUtdhVy2CM7gsA1TiY5o-mX7n_m9vHeDGYjFcANZXwqvI-Y6lGZOMyNiXfOtb6V9BekfLFxZRL1ohNLDkvstcPZ7KDcm7JJG4q4Ga4C27xaevOqPIURP6D0C9FgJj5mynzwvDyxqua-qopf4rubCPXTUbUBw_qepx9ejsD-LtQ7VEh0v-xW_hv5nAdaGwdAHyc3r14DahLlF7_y1rmbpWabuJEKvghQr4NBpdSStKdHFJn0f-OGJnG-OOfSglpx62ElNzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94a89c6058.mp4?token=h7XnrwFM5AVDbHF1-KDJpeeuIyVt_rJNez7hzsVWZPwXq-piBap6BJNjxQFH1EYZG_eU-0vhgX1_ZpkEjUtdhVy2CM7gsA1TiY5o-mX7n_m9vHeDGYjFcANZXwqvI-Y6lGZOMyNiXfOtb6V9BekfLFxZRL1ohNLDkvstcPZ7KDcm7JJG4q4Ga4C27xaevOqPIURP6D0C9FgJj5mynzwvDyxqua-qopf4rubCPXTUbUBw_qepx9ejsD-LtQ7VEh0v-xW_hv5nAdaGwdAHyc3r14DahLlF7_y1rmbpWabuJEKvghQr4NBpdSStKdHFJn0f-OGJnG-OOfSglpx62ElNzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
💙
میثاقی: با صالح حردانی صحبت کردم او توضیح داد که اصلا قصد حاشیه سازی نداشتم و هیچ قصدی هم برای حاشیه سازی ندارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/105843" target="_blank">📅 01:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105842">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83ee6a8989.mp4?token=tLz-u9q4hGUcG2XtbRA0Mel2c19nhw0XYRydJyjsIUGAujwVscAYrp__Zf18nNqcOyP4dLFwmuRPA73o2_AuTESCKF4AWqg_QNEGsCZOgt-CfGNesiUMXrOEwBcILX8cKq2PVnmDbVKe-l3xYSIHq5KVTdMBvxzwaRUkRccJB5MPI8Z1YgXQKv_NiQ9aYXVGwt-dV4-LesQ0o-6sDxwnfjEiRkB3CgNNnjm31ncELuZqdVvhVXgWRGmRdCr5-H5-0m1M7dItaI90PStCU3ASezZF_ClcZRdJzte8o9D6BP3Kp2lgF6LrFY6CLAugvRXgPKfQvgiBjCt4QNr73H803A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ee6a8989.mp4?token=tLz-u9q4hGUcG2XtbRA0Mel2c19nhw0XYRydJyjsIUGAujwVscAYrp__Zf18nNqcOyP4dLFwmuRPA73o2_AuTESCKF4AWqg_QNEGsCZOgt-CfGNesiUMXrOEwBcILX8cKq2PVnmDbVKe-l3xYSIHq5KVTdMBvxzwaRUkRccJB5MPI8Z1YgXQKv_NiQ9aYXVGwt-dV4-LesQ0o-6sDxwnfjEiRkB3CgNNnjm31ncELuZqdVvhVXgWRGmRdCr5-H5-0m1M7dItaI90PStCU3ASezZF_ClcZRdJzte8o9D6BP3Kp2lgF6LrFY6CLAugvRXgPKfQvgiBjCt4QNr73H803A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
💙
اسفندیارپور مدیرعامل گل‌گهر: سندی بیرون آمده که یک نفر از آن طرف فحش داده ولی از طرف ما اتفاقی نیفتاده است!
💙
میثاقی: پس چطور عالیشاه 4 جلسه محروم شده است؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/105842" target="_blank">📅 00:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105841">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1e01e106d.mp4?token=eVFXHbDBYexT-LLu9Lp_dWODt0qhAB1vrfMd8Lg-PSjZhfCJLHEUpi2s7M7icl6hBvRGrhXquP27_b0NlU9T-XXFhmgaYxvkvW06ocLDVbnd1iwGPm7MyLj7mA4YXE_RpaG9Me2VHloRzHDykRgGyW_Ct1YR0mIBO49U-HsdF-LCkj_QkkJKVzGAOo0IhVQ5HzeXdxNLhB_PuLpVSKM1AvUEFzDf-_0igyQW40mBqLxNl8oFa5eufYNsRtLE0rpLrdsyZPr3rCH45dYltj4NoCkwPhMRbCDXy1VzWgW3jZydYqNtcegSea600bxToLefsjrki55DTVIJfHbWJPao8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1e01e106d.mp4?token=eVFXHbDBYexT-LLu9Lp_dWODt0qhAB1vrfMd8Lg-PSjZhfCJLHEUpi2s7M7icl6hBvRGrhXquP27_b0NlU9T-XXFhmgaYxvkvW06ocLDVbnd1iwGPm7MyLj7mA4YXE_RpaG9Me2VHloRzHDykRgGyW_Ct1YR0mIBO49U-HsdF-LCkj_QkkJKVzGAOo0IhVQ5HzeXdxNLhB_PuLpVSKM1AvUEFzDf-_0igyQW40mBqLxNl8oFa5eufYNsRtLE0rpLrdsyZPr3rCH45dYltj4NoCkwPhMRbCDXy1VzWgW3jZydYqNtcegSea600bxToLefsjrki55DTVIJfHbWJPao8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
❤️
حجت کریمی مدیرعامل تراکتور: حالا حکم کمیته انضباطی آمده است آیا واقعا باید خداداد عزیزی را در استادیوم‌ها راه ندهیم؟ آیا این درست است؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/105841" target="_blank">📅 00:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105840">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fca1acab48.mp4?token=AH997B_BMIDYc7vbfa_VCVxphXiJbRuq6cknSXY1Gne5W7oTdZVyk5RxW3rZs2rUB9YcwWErQnHP8IJAgVRkcCj2lNT1h4qKrO4g_EkGTUCF77nBGI453aT_4sU6UUT4Q-KVW2W25CK-cdGIOMMs8gP1yy4dMR97JIFointerJaOYK-PTyP8GWCIAeECTNIF07evO7N-spKfC_V1TCfsY_N35Z-kIDGtRZjvNaL11-T_O9VK5xLbm7k3PSQHigCcxDuvH_JiuvFRpjlWesF3HWLjC7uIbqoyzBBg1-ScEk0Y6mjFAxq-L3vmbJVGEGhM2t8OrGtqCSL9h1S8TXLKsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fca1acab48.mp4?token=AH997B_BMIDYc7vbfa_VCVxphXiJbRuq6cknSXY1Gne5W7oTdZVyk5RxW3rZs2rUB9YcwWErQnHP8IJAgVRkcCj2lNT1h4qKrO4g_EkGTUCF77nBGI453aT_4sU6UUT4Q-KVW2W25CK-cdGIOMMs8gP1yy4dMR97JIFointerJaOYK-PTyP8GWCIAeECTNIF07evO7N-spKfC_V1TCfsY_N35Z-kIDGtRZjvNaL11-T_O9VK5xLbm7k3PSQHigCcxDuvH_JiuvFRpjlWesF3HWLjC7uIbqoyzBBg1-ScEk0Y6mjFAxq-L3vmbJVGEGhM2t8OrGtqCSL9h1S8TXLKsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😳
😳
😳
گلایه عجیب خلیل‌زاده از حجت کریمی؛
🚨
‼️
چرا به تماشاگرانمان گفتی فحش ندهند!
؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/105840" target="_blank">📅 00:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105839">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d780e6da8.mp4?token=b4X2GyS0ZN_al94AlQYHCHMpkbHcFiMukKmhwMnJvWSEAsSRH8iRhCv2RHzS3LxHrzawp_BeUNKNPkR64sd3fFauBeHdxfzoUI8rk3QzcDapkeR8CBMDFmSR-3sVcZeCpteD_FZNyvra5B4QB4ae8Nk3C-oAl7UxxxzCOfa2mj5aUOFSIbv8bYis4Rm8LW02QlqxALTVmkGZNoqqFyfmUzbKfpfWP1QCU7Ywm3IkCFWtNyN8YeGDjRXIkNJxIcFAr8kt1Kc31rSL-y4LYpag7sZ3cYayH01ZglHhVKZzdFofMlyxMXsM4Fk7aDG6qrn7x8Sz9_LJbrwflT9XTuCq3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d780e6da8.mp4?token=b4X2GyS0ZN_al94AlQYHCHMpkbHcFiMukKmhwMnJvWSEAsSRH8iRhCv2RHzS3LxHrzawp_BeUNKNPkR64sd3fFauBeHdxfzoUI8rk3QzcDapkeR8CBMDFmSR-3sVcZeCpteD_FZNyvra5B4QB4ae8Nk3C-oAl7UxxxzCOfa2mj5aUOFSIbv8bYis4Rm8LW02QlqxALTVmkGZNoqqFyfmUzbKfpfWP1QCU7Ywm3IkCFWtNyN8YeGDjRXIkNJxIcFAr8kt1Kc31rSL-y4LYpag7sZ3cYayH01ZglHhVKZzdFofMlyxMXsM4Fk7aDG6qrn7x8Sz9_LJbrwflT9XTuCq3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
به‌به آقا مبارک باشه. اولین لحظات بنزین ۱۰ هزار تومانی در ساحت مقدس جمهوری اسلامی
🙏🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/105839" target="_blank">📅 00:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105838">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cab995b804.mp4?token=GmqKDmuxGmoV6J_CQXESn9B-pwjMxJM3nYQvZPS045bfcOELMn4XPZiHehGbrku5H-z_UO0FPfwDhwirvRKZwBIicRDOU6Zq6Zcywp_HacLelIAwoHf_SfjPAOxaEJXx-oMbOijtrdu_mY7kGpaqsBxYiatBwNuOzvFazURmoP9y8tXhosOmKffNOUsYSRtHU6dB36kwW0Bw7ZsyNNTOpZksy3QSzlgKo-ujYlf9YRX9nMe0y1fcgSRGpY3MgNByd4weuQIvgXZIwPbDr38TXaFvntfYGIGSJLHfpTAyZdIvrXXNH6cAKgB6KGXL0SxFOrzSJ8kWmpIGtHXO9BZ99A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cab995b804.mp4?token=GmqKDmuxGmoV6J_CQXESn9B-pwjMxJM3nYQvZPS045bfcOELMn4XPZiHehGbrku5H-z_UO0FPfwDhwirvRKZwBIicRDOU6Zq6Zcywp_HacLelIAwoHf_SfjPAOxaEJXx-oMbOijtrdu_mY7kGpaqsBxYiatBwNuOzvFazURmoP9y8tXhosOmKffNOUsYSRtHU6dB36kwW0Bw7ZsyNNTOpZksy3QSzlgKo-ujYlf9YRX9nMe0y1fcgSRGpY3MgNByd4weuQIvgXZIwPbDr38TXaFvntfYGIGSJLHfpTAyZdIvrXXNH6cAKgB6KGXL0SxFOrzSJ8kWmpIGtHXO9BZ99A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
❤️
حجت کریمی مدیرعامل تراکتور: آن کسی که ویس را ضبط کرده است چرا به آبروی طرف مقابل( خداداد) فکر نکرده است؟!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/105838" target="_blank">📅 00:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105837">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac4ad57568.mp4?token=CLelqLTzDvWNK31M4bvD4KRKuvgz9lVxohasxSShEz-PcJtNK2PI3pp3y8NRv8d7kh1HNqr7GwaWlQJ_-YBFs3YnYPOcb6iAjQj0BrY8FIqjAXgzIxKdt-vWSxluNl1k1hGxdHOY-JtyOP2JXX0sUk6oGFEjuWR2lzsfmNT6VusjjdrWhbhTfedp1Pa7mtrKfSDG3TOeck_YVmo0STqfm6IwrfXyhgfZytjJrtZgIRBSmo5omnS2RyHGF7SpN186EfAo1PB_9OIBWS6cpvHlZ3KRvgrNPI80M9LtMyBNc2-E5I4ocTlR654XiI-ELmrcY_lzGyaiSJjXdzLDRsoogQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac4ad57568.mp4?token=CLelqLTzDvWNK31M4bvD4KRKuvgz9lVxohasxSShEz-PcJtNK2PI3pp3y8NRv8d7kh1HNqr7GwaWlQJ_-YBFs3YnYPOcb6iAjQj0BrY8FIqjAXgzIxKdt-vWSxluNl1k1hGxdHOY-JtyOP2JXX0sUk6oGFEjuWR2lzsfmNT6VusjjdrWhbhTfedp1Pa7mtrKfSDG3TOeck_YVmo0STqfm6IwrfXyhgfZytjJrtZgIRBSmo5omnS2RyHGF7SpN186EfAo1PB_9OIBWS6cpvHlZ3KRvgrNPI80M9LtMyBNc2-E5I4ocTlR654XiI-ELmrcY_lzGyaiSJjXdzLDRsoogQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
❌
حجت کریمی مدیرعامل تراکتور:  دیشب بچه ام از من می پرسید بابا قضیه خداداد چیه؟ من نتوانستم جوابش را بدهم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/105837" target="_blank">📅 00:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105836">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd890b34ee.mp4?token=vbd9LVWagl6N-BXKMrY6MW9zYo_z99haac_TBhNNiM0aWsk1UjEpGTGBlD3eHy4dnR63MYlWAhrfFMOUL57YX2CFYs6kbZ2fE8kxkNCoS2Tx6s20_CLYdCN5ugXeqDyuqDPfBWJ83PRJtn9Dlf5qFD57LWUU49sXp0GD7tt6N0k5ngW5W6sSwBculh9aoKr8lkb9rtxS24nbKyDwOFO0NkeTmqE9Xgdis_FOYnobL4Oy6DCvHCtehLyDcLF3kEnAaNA4-KPJ4sjDeYwnU24EXXIjKAurK2EiEBfuVvSAap6REecyWGox2pQZ-E9GUPZArUlMQWFxoY0XAlD62WzRrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd890b34ee.mp4?token=vbd9LVWagl6N-BXKMrY6MW9zYo_z99haac_TBhNNiM0aWsk1UjEpGTGBlD3eHy4dnR63MYlWAhrfFMOUL57YX2CFYs6kbZ2fE8kxkNCoS2Tx6s20_CLYdCN5ugXeqDyuqDPfBWJ83PRJtn9Dlf5qFD57LWUU49sXp0GD7tt6N0k5ngW5W6sSwBculh9aoKr8lkb9rtxS24nbKyDwOFO0NkeTmqE9Xgdis_FOYnobL4Oy6DCvHCtehLyDcLF3kEnAaNA4-KPJ4sjDeYwnU24EXXIjKAurK2EiEBfuVvSAap6REecyWGox2pQZ-E9GUPZArUlMQWFxoY0XAlD62WzRrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
❤️
حجت کریمی مدیرعامل تراکتور: حق نداشتند که آن ویس (فحش های خداداد عزیزی) را پخش و جامعه را ناراحت کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/105836" target="_blank">📅 00:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105835">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a288bb9015.mp4?token=cTp1T_7qbKpFCX11F9DSSe8UVb1qGz8QGqrGrlZAiZ-YLbE-QA9z8nIAYrqN0_nWsdBQ6KCd3m_9JHDbont5ZEjxeiv1lsV_BzwExM9qqn8nJT3sCDqbXHf12UG3UEVfuzW7uIDgTuHPihYiq8KcGO52SirjvPI6dLVArB7UcIHeQ-fd9fN3Ii3tn7nwzYD_uqN3uHninq25XiurfDkFJCGXdmzfKepkoP92U_hkVVkQB-XqwxXtZHT4CyxL-rJX1ZlezNERHzxLNmONnF4TH36MxsXSfb4GcUxZsAsiFgDx0vOvqBM7mJIjA-z8wz9vYhRDhZvyVU8JTSLh3dUCXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a288bb9015.mp4?token=cTp1T_7qbKpFCX11F9DSSe8UVb1qGz8QGqrGrlZAiZ-YLbE-QA9z8nIAYrqN0_nWsdBQ6KCd3m_9JHDbont5ZEjxeiv1lsV_BzwExM9qqn8nJT3sCDqbXHf12UG3UEVfuzW7uIDgTuHPihYiq8KcGO52SirjvPI6dLVArB7UcIHeQ-fd9fN3Ii3tn7nwzYD_uqN3uHninq25XiurfDkFJCGXdmzfKepkoP92U_hkVVkQB-XqwxXtZHT4CyxL-rJX1ZlezNERHzxLNmONnF4TH36MxsXSfb4GcUxZsAsiFgDx0vOvqBM7mJIjA-z8wz9vYhRDhZvyVU8JTSLh3dUCXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😆
😆
😆
😆
عادل خودشو جر که فحاشی خداداد رو تکرار نکنه بعد همون لحظه واکنش سخنگوی گلگهر:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/105835" target="_blank">📅 00:06 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105834">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/670edf11a2.mp4?token=fLtyj0-A6qLMNE_bqt-_BdUayH8Az49hrztSjuX6gRTc0eEArcvXTp9RtjJHhRbRLlNzFXvEKqyyLTfIpoiM4pfP0CIcmMomNt5Q2NCllN90ifiUhAgGxzCG-aj3XbxNkVXgxL2yjQWgmDALdZR-TbzCeXJT_NeBPTVkBHxTFtTq18TcGiDal0OwI278H_tw4RIsRg8B6vfbd7zG6htx2J5noWmMiNdM50ultSBM1Ed8y3ZqVQfDIK0yjzcch8S1peHADFArdqa1NsqzG1Yg9lWnSHWZP9OPkOyyjALWKJuAfFHBGQ-vue668FnQjqvV2NcwtY-Gf1e2eFDhu5WBfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/670edf11a2.mp4?token=fLtyj0-A6qLMNE_bqt-_BdUayH8Az49hrztSjuX6gRTc0eEArcvXTp9RtjJHhRbRLlNzFXvEKqyyLTfIpoiM4pfP0CIcmMomNt5Q2NCllN90ifiUhAgGxzCG-aj3XbxNkVXgxL2yjQWgmDALdZR-TbzCeXJT_NeBPTVkBHxTFtTq18TcGiDal0OwI278H_tw4RIsRg8B6vfbd7zG6htx2J5noWmMiNdM50ultSBM1Ed8y3ZqVQfDIK0yjzcch8S1peHADFArdqa1NsqzG1Yg9lWnSHWZP9OPkOyyjALWKJuAfFHBGQ-vue668FnQjqvV2NcwtY-Gf1e2eFDhu5WBfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
‼️
❤️
حجت کریمی: اگر خداداد عزیزی فحش داده است حتما یک نفر یک کاری کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/105834" target="_blank">📅 00:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105833">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9428c43ae.mp4?token=mJZ5qnUu4pCqXQOOUAQVpVNvRiF4KQMsYBH59et2RZK7NQvApOGjMkx5lh-YqKgjvy_4VIIGSN8f-W-TluLqKDCI62-nRO7opQmqMdb2arcYifeHI6gT5ud5vQflXR0Yvyslbsshj-2iRicgtWbiF9aOQg0jrO8_DYUjK456PITdfZ_nYivr9zXdTvK6Fkhz6NgNub4AOiGmMcP5WqYFD-hHgAbGgXL-Zuvb_kYllkmLCVCAywgPJijvH9warMTaY_Qp8S49WfI73eiS8K5cAp7e54WjkBTehhVGhg6orREHZ93uXcRs9GZTGh2D7-Nlxodq7DGi_eCJXt_Zg5EcoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9428c43ae.mp4?token=mJZ5qnUu4pCqXQOOUAQVpVNvRiF4KQMsYBH59et2RZK7NQvApOGjMkx5lh-YqKgjvy_4VIIGSN8f-W-TluLqKDCI62-nRO7opQmqMdb2arcYifeHI6gT5ud5vQflXR0Yvyslbsshj-2iRicgtWbiF9aOQg0jrO8_DYUjK456PITdfZ_nYivr9zXdTvK6Fkhz6NgNub4AOiGmMcP5WqYFD-hHgAbGgXL-Zuvb_kYllkmLCVCAywgPJijvH9warMTaY_Qp8S49WfI73eiS8K5cAp7e54WjkBTehhVGhg6orREHZ93uXcRs9GZTGh2D7-Nlxodq7DGi_eCJXt_Zg5EcoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
❤️
حجت کریمی مدیرعامل تراکتور: به دلیل اتفاقاتی که در تبریز و در بازی با گل گهر افتاد از تمام مردم ایران عذرخواهی می کنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/105833" target="_blank">📅 00:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105832">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8340864e3b.mp4?token=VN1b836N35o-qINQL0_tQulGSPD6ksuCd92D_x5YzBW8ziF4gGu9_1NDB00uOTFsQKpOLMh4EW4REzYVjr2Ow7t27_NSPqX55RDuE205k1ECTO8LuK2c-cqq4a9Kq3LoDpIveYUXYr8o7fYxEskN2ZolavKn5YqCVWxUirXbdqVUWkRBD3qp5ApN5aY9RTXdV1Tg9zSc5XavpP9bZuClc--5SsKcB1coyTb2Kl4duwSXANy6Gr9yD_AXM2UHT7b9ojjD-csWiRUCH2OBlFbbdQyEQkpX3GVKbiQliRhBLVVTWTfBK3bFrIQP7CcWxp0TjLNQeymo2hcL83v_Z9oiRDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8340864e3b.mp4?token=VN1b836N35o-qINQL0_tQulGSPD6ksuCd92D_x5YzBW8ziF4gGu9_1NDB00uOTFsQKpOLMh4EW4REzYVjr2Ow7t27_NSPqX55RDuE205k1ECTO8LuK2c-cqq4a9Kq3LoDpIveYUXYr8o7fYxEskN2ZolavKn5YqCVWxUirXbdqVUWkRBD3qp5ApN5aY9RTXdV1Tg9zSc5XavpP9bZuClc--5SsKcB1coyTb2Kl4duwSXANy6Gr9yD_AXM2UHT7b9ojjD-csWiRUCH2OBlFbbdQyEQkpX3GVKbiQliRhBLVVTWTfBK3bFrIQP7CcWxp0TjLNQeymo2hcL83v_Z9oiRDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
با استقلال تفاهم‌نامه امضا کرده‌ایم
🇮🇷
چیزی ۱۰۰ درصدی نیست!/ توضیح محمد خلیفه درباره جزئیات تفاهم آلومینیوم با استقلال؛ که حتی خود از بندهایش خبر ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105832" target="_blank">📅 23:52 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105831">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
‼️
🇮🇷
صحبت‌های سخنگوی باشگاه گل‌گهر در خصوص فایل صوتی جنجالی خداداد عزیزی؛ با صدای بلند فحش می‌داد اما کسی از رختکن گل‌گهر بیرون نیامد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105831" target="_blank">📅 23:23 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105830">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
‼️
آدم عارش میاد بگه به فوتبال علاقه‌منده!
مقدمه عادل فردوسی‌پور قبل از مرور پرونده بازی جنجالی ترا‌کتور - گل‌گهر؛ این‌قدر از ترسشان برخورد نکردند که کار به این‌جا کشیده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/105830" target="_blank">📅 23:06 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105829">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08a84e3855.mp4?token=YKKdjzHZEWsl_3ItqsuLB7ZpoPFNV0M2ESzYJWH3wc_a8LhP-rYZ2rQKa_8mZNEO98oxeN_W-g_oaPsU2gWzv4_9lJGOAFwKlj_MzOqaTwi3TyFCsXUB8sgL-DGEIf1AHTqCkpPei28DKsO9J3tN8mnLJPtAjawV3tioX_zffGe3F6gcg1NbgPB95z1y9zj-zjpJfBZrIay8NlYypZYvKOiriCLPKnL7LkGMT1W4-6G407tRpAGlihAiuf67iL2VXjrEs48zbJQLw1FTHzTO_NuxT2w0orIid9DLrdyyo13djykBmz1U9eU86FnDEsuAd_6yzqRWwtUmXGd5LCiCAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08a84e3855.mp4?token=YKKdjzHZEWsl_3ItqsuLB7ZpoPFNV0M2ESzYJWH3wc_a8LhP-rYZ2rQKa_8mZNEO98oxeN_W-g_oaPsU2gWzv4_9lJGOAFwKlj_MzOqaTwi3TyFCsXUB8sgL-DGEIf1AHTqCkpPei28DKsO9J3tN8mnLJPtAjawV3tioX_zffGe3F6gcg1NbgPB95z1y9zj-zjpJfBZrIay8NlYypZYvKOiriCLPKnL7LkGMT1W4-6G407tRpAGlihAiuf67iL2VXjrEs48zbJQLw1FTHzTO_NuxT2w0orIid9DLrdyyo13djykBmz1U9eU86FnDEsuAd_6yzqRWwtUmXGd5LCiCAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇮🇷
فولاد خوزستان با گل دقیقه ۹۲ احسان محروقی مقابل فجرسپاسی به برتری رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/105829" target="_blank">📅 22:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105828">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc6f987e3d.mp4?token=DP4wT7EJYB_H_SuRQhA2DHPakoqFKMJCYXEDAlEvjv6Wbemr-xIlw5D8PUwLLL2YuVxfLi39xH_xZiQmQGJwk69Caj82R3K4O8D6jk8tnHPDg6Mv3dBvPfy82a7ReS9cUMs18QBuR7ITXjJnDiaivvi6NCUbLFDcESGHef3PUMgpKM6sITID7t8X54eT1ZWw_ItwcWhrlop-ASxOoHifLa_h7yk5NKZIMw4bntGlIlzc7slIMCUTFqpzo8JrbWZcq58dVKJ3ZTf4-NGQ3VbVOF1gU5XAGVfIRc8-VOpW6Pyibsmx8XmhzorAencBZt0P3x3fA-3ZRGC2IVdgH5YWEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc6f987e3d.mp4?token=DP4wT7EJYB_H_SuRQhA2DHPakoqFKMJCYXEDAlEvjv6Wbemr-xIlw5D8PUwLLL2YuVxfLi39xH_xZiQmQGJwk69Caj82R3K4O8D6jk8tnHPDg6Mv3dBvPfy82a7ReS9cUMs18QBuR7ITXjJnDiaivvi6NCUbLFDcESGHef3PUMgpKM6sITID7t8X54eT1ZWw_ItwcWhrlop-ASxOoHifLa_h7yk5NKZIMw4bntGlIlzc7slIMCUTFqpzo8JrbWZcq58dVKJ3ZTf4-NGQ3VbVOF1gU5XAGVfIRc8-VOpW6Pyibsmx8XmhzorAencBZt0P3x3fA-3ZRGC2IVdgH5YWEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
واکنش کنعانی زادگان، بازیکن پرسپولیس در مورد حواشی دربی و ضربه اش به عارف آقاسی:
در فوتبال اتفاقات زیاد می افتد/ نمی خواهم به کسی توهین کنم و یا ضربه بزنم/ شما دنبال این هستید که حرفی زده شود/ هیچ کسی مشکلی ندارد و همه را دوست داریم و به همه احترام می گذاریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/105828" target="_blank">📅 21:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105827">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d82451c129.mp4?token=vEZTjiaEMMEZA4oXWIO3xxrC0ivTvo0cyzLsWclPmJAFCIc_qF1H-aMNQBO2nNpCUDEDLbR_P1CJroMRHjYwGdHsBqgCqphwEHOt6FGAkDBtZxFgu-s8V3-9tMOBK_e33B0XTT2Nr7ILWHc4eFpXhnZQkh5HCl2Q0h6f3a9zA7xJeaC2dvov5bCE5eBognxehyipg7bfjJJCY05Kxd5GVcSOGZQ5e1SHL7JJjZvyQnxD6YBtb4gqKffxAtJMP0zN4Zavoyu_51bvOb1ACayt-VPBxrbqSCxrnvWW5FtEeYYWOu_JX40rW3Dwr-5vFjBHttooqBT1Xoy7VQQXPlCf1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d82451c129.mp4?token=vEZTjiaEMMEZA4oXWIO3xxrC0ivTvo0cyzLsWclPmJAFCIc_qF1H-aMNQBO2nNpCUDEDLbR_P1CJroMRHjYwGdHsBqgCqphwEHOt6FGAkDBtZxFgu-s8V3-9tMOBK_e33B0XTT2Nr7ILWHc4eFpXhnZQkh5HCl2Q0h6f3a9zA7xJeaC2dvov5bCE5eBognxehyipg7bfjJJCY05Kxd5GVcSOGZQ5e1SHL7JJjZvyQnxD6YBtb4gqKffxAtJMP0zN4Zavoyu_51bvOb1ACayt-VPBxrbqSCxrnvWW5FtEeYYWOu_JX40rW3Dwr-5vFjBHttooqBT1Xoy7VQQXPlCf1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
❤️
کنعانی زادگان: بازی امروز خیلی سخت تر از بازی با استقلال بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/105827" target="_blank">📅 21:52 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105826">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7963e99b5d.mp4?token=rTBouJKM9dn2B6hie7bmJKo4B_gw7MZ8i0Ylx4OM5aGIJYvUz1LW6fp2mYvyzUIqVYX66-Toq26r7Ur4R8fu0LIfbWZg-bDUNexFhLMUz2BapoQL8uVnxlO5MXrmrK62vMhYfzpVg8QYZQWHvGtBf3WGH57ruywIgLTIQacUeuZqzQRUG6XjqlMpS1lQffy3E9znOJ1JwUsGqoNrzwwd4ZssdXpBU_zcIc71l_wtWo0hYuluSMSo_p0LZD_6yHW93mEOF1r7E5PbCeHi5htNXyei90MaVAOIek3pybSGsTL3JPQq34bo3cZecCqzWM_wdbnV94g-le1aFgc4YzUisw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7963e99b5d.mp4?token=rTBouJKM9dn2B6hie7bmJKo4B_gw7MZ8i0Ylx4OM5aGIJYvUz1LW6fp2mYvyzUIqVYX66-Toq26r7Ur4R8fu0LIfbWZg-bDUNexFhLMUz2BapoQL8uVnxlO5MXrmrK62vMhYfzpVg8QYZQWHvGtBf3WGH57ruywIgLTIQacUeuZqzQRUG6XjqlMpS1lQffy3E9znOJ1JwUsGqoNrzwwd4ZssdXpBU_zcIc71l_wtWo0hYuluSMSo_p0LZD_6yHW93mEOF1r7E5PbCeHi5htNXyei90MaVAOIek3pybSGsTL3JPQq34bo3cZecCqzWM_wdbnV94g-le1aFgc4YzUisw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
😢
🇮🇷
واکنش جالب هوادار پرسپولیس به عملکرد تیم
:
بارسلونا هم بیاید در این زمین شکستش می دهیم؛ 2 تا به بارسا گل می زنیم 3 تا به رئال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/105826" target="_blank">📅 21:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105825">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
پیمان حدادی، مدیرعامل پرسپولیس:
🔴
با توجه به مستنداتی که در اختیار داریم، درخصوص پرونده آسانی از باشگاه استقلال شکایت کرده‌ایم و در صورت حاصل نشدن نتیجه، حتما پیگیری‌های خود برای احقاق حق باشگاه را از طریق دادگاه CAS ادامه خواهیم داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/105825" target="_blank">📅 21:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105824">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQYGPyAiIHUojxRgAi-_U5JKltmlt79ikgmW3z_eVTkYuI5DNSoJTjYO--a9ZIV562P1QCcxUJdwS42nVTsYIKLFDLdA5d557KvN8tqsagJ4RSBP8RtgWsLUQhNJs5hr_DKN9SqvN8YQP7RJKoKnKIHU2LPN9mL1kvIu73t3E0-3wwWD0Sq29y1Tl9e8yiU9XueeY0ewoDmxbcZD3A2dD7QsLshQoczu4okNo0WRl4bztSBaG2N-HtneZ-7wiP9JocNYkFMvYaTO4DZAKwtxwQT1ek2f4kB8o3goZpCpOlycdYcZouQhaCHh2XJYzLP__4NoDefRbtBjmVxfelRSCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
عبدالله ویسی، سرمربی ذوب‌آهن پس از دیدار امروز مقابل پرسپولیس از سمت خود استعفا کرد. ذوب‌آهن با کسب ۶ امتیاز از ۶ بازی در رده سیزدهم جدول لیگ برتر قرار دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105824" target="_blank">📅 21:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105823">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IRS_D6YPhEiOYZN_Vc2NwDUaAYq8gQW5-cGIQffjN2Iil9UDXK-EBBqdEVnKTznk2GqTCJgrlQCkwYdT2LkXFeBW079LAHg6VGz_FxIgmymS9n4Kn8rYEaUVS64cvdwYhO1nAMcmYQlagTDN-Q9s1APXRqYeLAmriMhCiO4IZCYMa9G2AoZCEIeneYg0jB3ae1zHTI5O0tW02Dhq3Eg9kmf7Ju0M7c0JhLlyefGQHDXujKRppA1HGfmUdQm7gN9jvEcDlhQrA8UJbCSWKpaka0OGQva3VfBKCv2tesDvPilS18bvEltf1wgwWZwdhRhLtZGni_GsZdKKgsAhGX47bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
هفته‌ششم لیگ‌برتر؛ شهرقدس قتل‌گاه رقبای تارتار و تیمش؛ پرسپولیس با یک نمایش زیبای دیگر دوباره از استقلال پیشی گرفت
🇮🇷
پرسپولیس
😀
😏
ذوب‌آهن
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/105823" target="_blank">📅 21:13 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105822">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjLZmDXrDd8Sn8vPVCtvGeZUO-RdIzDUzcdAF78UFVvExbm_JgKMx5OyEjIn8OuQ1gMO0HUkpp_wsIy1ynx6Uu9ePaLuGpogK7w0XS_2l35qY5VEbktzt9nDB85hyg_hqd4HzsgFMYeSn8DZeEpvgGLLyzuNZ1ilJF9ZtOO0xe_jfLI5qIGm_BpP0DRGz6E5J4w_iPYr0jRxQipfGpIh7tVelcNphThEySqeFTefg8SfsitEDHZUTxJzUTyM1z185Gh2yxU79GLuvcdPKiMwGG-9CL-oZM_X121vPRVmIvrx-jl3kk_wXquRGqehSDPTcD9RoELZb6Qb6Wl59-_7bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
هفته‌ششم لیگ‌برتر؛ شهرقدس قتل‌گاه رقبای تارتار و تیمش؛ پرسپولیس با یک نمایش زیبای دیگر دوباره از استقلال پیشی گرفت
🇮🇷
پرسپولیس
😀
😏
ذوب‌آهن
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/105822" target="_blank">📅 20:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105821">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca306a134d.mp4?token=R1zYEWhTW68J0QjJHx2ehVZZaoA9oCtVp5yW5FXAHWoPJliIHO7D36s6jatxqznUambO9ZFNwnQsuSOfHDh8TMpbFxeyHQZ8n2fQTDmpPfeLayNwmFEnmcVqSq9YuMXrK7In3NagnLOKszp0DVOTwf76WttVh9ZdRlyLIVPm4XeDxUIHWazYrp0td5RvJ3pnS1pZ3GVIWHnDeqY-ZJc_oonTl-PFEIoWGO9AQvd9ek-nwXCLhP4P6qxUx-iNNAO9d9TJal6xymPFH552V24yDemE1re7ALsmCCjz1HzeCfJts2K3_qYLYcQ8wmLr1WgF7Cl-ZRuQuuY9U_-qNFxisw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca306a134d.mp4?token=R1zYEWhTW68J0QjJHx2ehVZZaoA9oCtVp5yW5FXAHWoPJliIHO7D36s6jatxqznUambO9ZFNwnQsuSOfHDh8TMpbFxeyHQZ8n2fQTDmpPfeLayNwmFEnmcVqSq9YuMXrK7In3NagnLOKszp0DVOTwf76WttVh9ZdRlyLIVPm4XeDxUIHWazYrp0td5RvJ3pnS1pZ3GVIWHnDeqY-ZJc_oonTl-PFEIoWGO9AQvd9ek-nwXCLhP4P6qxUx-iNNAO9d9TJal6xymPFH552V24yDemE1re7ALsmCCjz1HzeCfJts2K3_qYLYcQ8wmLr1WgF7Cl-ZRuQuuY9U_-qNFxisw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد از مشخص شدن محرومیت 4 ماهه خداداد عزیزی، پرسپولیسیا این شکلی عالیشاه رو تشویق کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/105821" target="_blank">📅 20:46 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105820">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/656ef71eba.mp4?token=KkJUG9G2HRJgVbeSizc24nBRWF-UvvqV0UdjAVLEcXzaYvH3dEcscDKXxReH2xKeTyvx0RcosNKj-wpABCu2j0plS73rfeh8bXRY01soi9uIYtoQVgWf8uLTZGIsX-Acly4WK4KlDHIhIhe__fSfuPKMCglHKv7a3H6ZTO_Nc2sjSG_Tyz6H1Y1rnJpiAO7KiBbp1mFBowaHqt5_0bkThdAZft4Oi7TN7GLdHUNkZCH4_7V9Jne_GWEwIfAOLyakx6tnkAApjhfPJShi-R9DzEdMG1h1F9gRYd5AdkasQjQCSf3glv_rneDsIJrdOcYkeWG4uXpUrzphy3XKVK0I7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/656ef71eba.mp4?token=KkJUG9G2HRJgVbeSizc24nBRWF-UvvqV0UdjAVLEcXzaYvH3dEcscDKXxReH2xKeTyvx0RcosNKj-wpABCu2j0plS73rfeh8bXRY01soi9uIYtoQVgWf8uLTZGIsX-Acly4WK4KlDHIhIhe__fSfuPKMCglHKv7a3H6ZTO_Nc2sjSG_Tyz6H1Y1rnJpiAO7KiBbp1mFBowaHqt5_0bkThdAZft4Oi7TN7GLdHUNkZCH4_7V9Jne_GWEwIfAOLyakx6tnkAApjhfPJShi-R9DzEdMG1h1F9gRYd5AdkasQjQCSf3glv_rneDsIJrdOcYkeWG4uXpUrzphy3XKVK0I7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
گل دوم پرسپولیس به ذوب آهن توسط پوریا شهرآبادی
64
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/105820" target="_blank">📅 20:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105819">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔞
⭕️
⭕️
⭕️
⭕️
‼️
‼️
‼️
‼️
🇮🇷
🇮🇷
صدای منتسب به فحاشی زشت و زننده و ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/105819" target="_blank">📅 20:16 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105818">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lbll0s23YWJGK0bh0waaToW5xaxgSgNDLwiXKuA3m4CS8I-4okLLUY16mKueTfHecnaRm79NV-Elz1-5WcblOP5BKw2XDEFe_tMfoOKFBuhZP_zHrmlCtwXLNhuROSzotJSVPj7S7wBIecLEuktLh2A6mZaARF5ABzJBxEL7iWcgH1H7GXYZuQy3wmgVProQNlJ-mSHLI3EcZwosGaFoqHsY4KpXtH_h4Hx4rsmj97u5DBOlIw8WYynDzk9Sh_E2ZlkpdPSxLLdzX8iYTeHBQgoIlsUSWEYM1rRl7M51hQexrpeUhW475afWe9szcAjjzisZ5DMxbKhNZadoHAm7xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔞
⭕️
⭕️
⭕️
⭕️
‼️
‼️
‼️
‼️
🇮🇷
🇮🇷
صدای منتسب به فحاشی زشت و زننده و ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/105818" target="_blank">📅 20:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105817">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b10d894fc.mp4?token=KlNw6YP9RXnuQUWFz_arBzJNCdY_9u9cRaY1yaLYX0n6svjb1ERIorYY9DLwoxO447YP-aLy92Cv3rUOfxuJk4QE6D5NT50RLEEfe8CKafNr1y_4v60xi5JlPjdjhSYtGL74Pdkca0yZ8QWyFMY4602V3hRwbTcHBtwtVkwa-bXc03vzr3wh6a2uJk6A_idYoXgSuZDIsojSpKQi2_IdL7SGnzGeV9UCG8nsq-7TLii9Oio0FLKFQe2iKQYQbphmLsVUopFvkY0Uq4pMGN2qtt6qfRYAZzDh6o8hjWbUw8887gNWea8omx5vRKrpXyOw5W0CdFpjdhWpEoVyZ9g1XwWaRVyLVmKKca5XVkxt0aRX1-KI8pQ6y3_TpVqP4DNPG_WneKY9SO1EKWn8cDfDqBzr4PkmHyS23AyV4oROPq3TRfAIetjyr75ZquyUmtu958lIrYB57jwL53OSYhacICrpmrjQnsYBVzFq66xhgTxsXttako99FM6BSajByPcVQJonm8jtlEqtg4q6bg5I0kKYL_PXpO4Zd03bvWE8xr6Ky0ix9D14yUqdY2YaIZDdEZ0G8JzkWZ3Wvy9OcmxbIXYOrdjOz14L1Gc4KD99XE6YzjNSwx_Ns1FSMxIyfZ3YjKBfn3Rwq2So9Nl4p_lmEr5d1QzVx88D5kpY_HX2k-E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b10d894fc.mp4?token=KlNw6YP9RXnuQUWFz_arBzJNCdY_9u9cRaY1yaLYX0n6svjb1ERIorYY9DLwoxO447YP-aLy92Cv3rUOfxuJk4QE6D5NT50RLEEfe8CKafNr1y_4v60xi5JlPjdjhSYtGL74Pdkca0yZ8QWyFMY4602V3hRwbTcHBtwtVkwa-bXc03vzr3wh6a2uJk6A_idYoXgSuZDIsojSpKQi2_IdL7SGnzGeV9UCG8nsq-7TLii9Oio0FLKFQe2iKQYQbphmLsVUopFvkY0Uq4pMGN2qtt6qfRYAZzDh6o8hjWbUw8887gNWea8omx5vRKrpXyOw5W0CdFpjdhWpEoVyZ9g1XwWaRVyLVmKKca5XVkxt0aRX1-KI8pQ6y3_TpVqP4DNPG_WneKY9SO1EKWn8cDfDqBzr4PkmHyS23AyV4oROPq3TRfAIetjyr75ZquyUmtu958lIrYB57jwL53OSYhacICrpmrjQnsYBVzFq66xhgTxsXttako99FM6BSajByPcVQJonm8jtlEqtg4q6bg5I0kKYL_PXpO4Zd03bvWE8xr6Ky0ix9D14yUqdY2YaIZDdEZ0G8JzkWZ3Wvy9OcmxbIXYOrdjOz14L1Gc4KD99XE6YzjNSwx_Ns1FSMxIyfZ3YjKBfn3Rwq2So9Nl4p_lmEr5d1QzVx88D5kpY_HX2k-E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
گل اول پرسپولیس به ذوب آهن توسط علیپور(43)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/105817" target="_blank">📅 19:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105816">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">بالاخره پرسپولیس زدددددددد</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/105816" target="_blank">📅 19:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105815">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">علیپووووووووور</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/105815" target="_blank">📅 19:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105814">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">گلگلگگلگلگلگلگگلگل</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/105814" target="_blank">📅 19:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105813">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd555c5d54.mp4?token=Ic4rU9CKooaXU1yW19uIrfTz39rsr6Phj813DuLnwgLJb-Joz07GU2md9TIqYDgS8qsPidDaHFsBaniIizKH3dRBjB_moex0bVLGnG19YbmEZh4v1OedHB6MxwYAl4GCj7-Rkieoy2PicQdYl2F4KWukluxgHJEc7zCAr_KXEizDbAOlu0udpko1gRR99VnNSkGpS1RUcwYDNSpxtoLbLHkDtgPymrO0rHfm7i04OdLI6QXaX96U-mKd7D0Ox6IyDOhm0JTJJlyC4BtQum18Wq2kxkH33yMR9z6SWatsaRGPSS1-oC82kqwtcenoVwyrIXVIHqAohm34kTpeHMoyFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd555c5d54.mp4?token=Ic4rU9CKooaXU1yW19uIrfTz39rsr6Phj813DuLnwgLJb-Joz07GU2md9TIqYDgS8qsPidDaHFsBaniIizKH3dRBjB_moex0bVLGnG19YbmEZh4v1OedHB6MxwYAl4GCj7-Rkieoy2PicQdYl2F4KWukluxgHJEc7zCAr_KXEizDbAOlu0udpko1gRR99VnNSkGpS1RUcwYDNSpxtoLbLHkDtgPymrO0rHfm7i04OdLI6QXaX96U-mKd7D0Ox6IyDOhm0JTJJlyC4BtQum18Wq2kxkH33yMR9z6SWatsaRGPSS1-oC82kqwtcenoVwyrIXVIHqAohm34kTpeHMoyFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
واکنش جالب عبدالله ویسی به خراب شدن موقعیت گلزنی تیمش مقابل پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/105813" target="_blank">📅 19:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105812">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a21d11818e.mp4?token=O-kzBmCV8Asm1ZJcmmeXOyPsPNl-YQokiKK03x8M2L3VKbgtqcMZ9KxGT9AeSWJgbDZh9SfFCwZak1S6uCixW6EvjG26HTHF66esDx5SU-F6qiq5wjTUMrXb0vZ4uKpyWHzsN0OJ6ik3TNp5B9QERHgmUotLAluiLgpXAaS1owcIsqtmR1oUwg54iQYX33pLS5Oe6HuJtV91_Jgw0ZMD1De3SrwyN3ILy7yL9oC8ZGfjj6klWZFyH3FVVV44m8loQB0ce_r45Z7xh8ozyLhII0sx1X0S7UdjxrZOB40t_MGD3Bhki-HiuiGmOIw3Z1E-N9PVbjjJIbpuZZKwdu7XiBBy3I2bacNzHTdaekQD00iXyVxu4RtXmQOs0qeiOD3Mz2uyzD-INzp7IaCxsaHQh_GlaxIvr9jD3CPCYQI416IS0zhSkkhn_JxrjDayQ2G8tTysb1r2yZFu_HqwYChAM_Krx6H-b4t2d-LImL60VD-VbiMKeWvHrDjtGcKAz43Oh81SmeIa4aqAZXcXqp9jeA8gANbGPJVJmbIJu1vipZaCpEk219XCa_oP9S71qkB5CDZRpNU0ReQCMnSIaD334BClSvjigVPc5Eb6xiP_4Xma-qL16B5N92MRLzVrHplqIMBA5gAzdf6LPUJnxQKGwgEAFiUnP2ZMAIYXWBTzCO4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a21d11818e.mp4?token=O-kzBmCV8Asm1ZJcmmeXOyPsPNl-YQokiKK03x8M2L3VKbgtqcMZ9KxGT9AeSWJgbDZh9SfFCwZak1S6uCixW6EvjG26HTHF66esDx5SU-F6qiq5wjTUMrXb0vZ4uKpyWHzsN0OJ6ik3TNp5B9QERHgmUotLAluiLgpXAaS1owcIsqtmR1oUwg54iQYX33pLS5Oe6HuJtV91_Jgw0ZMD1De3SrwyN3ILy7yL9oC8ZGfjj6klWZFyH3FVVV44m8loQB0ce_r45Z7xh8ozyLhII0sx1X0S7UdjxrZOB40t_MGD3Bhki-HiuiGmOIw3Z1E-N9PVbjjJIbpuZZKwdu7XiBBy3I2bacNzHTdaekQD00iXyVxu4RtXmQOs0qeiOD3Mz2uyzD-INzp7IaCxsaHQh_GlaxIvr9jD3CPCYQI416IS0zhSkkhn_JxrjDayQ2G8tTysb1r2yZFu_HqwYChAM_Krx6H-b4t2d-LImL60VD-VbiMKeWvHrDjtGcKAz43Oh81SmeIa4aqAZXcXqp9jeA8gANbGPJVJmbIJu1vipZaCpEk219XCa_oP9S71qkB5CDZRpNU0ReQCMnSIaD334BClSvjigVPc5Eb6xiP_4Xma-qL16B5N92MRLzVrHplqIMBA5gAzdf6LPUJnxQKGwgEAFiUnP2ZMAIYXWBTzCO4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرصت سوزی عجیب رحمان جعفری مقابل دروازه پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/105812" target="_blank">📅 19:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105811">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8676bf1957.mp4?token=HW_JumWO6gcAW7rVCqWsgw_adCOcwW5lZ3cyiduP0d5dAYQHObwG2hHsgKo-AJ_xQ1jnWooSorstEvM8qOKvZ_PGEH6dslBp0J7-_9zIklvBETWMztmtzEhnT5r7ATOqHudBYJ8z_NO11VB7Cdu8fHXUij1Lcv2TRtBPZvdZwuQaTZ2gLLwj7e9fN8I3t55h79LV-kk5zvcuQRFkZtPw1SMQWrPX1fAK70deyCauPeLMfRxLeKhu_L2JiwbXpXVQefRinYX4Dhuo_YE8GsGyo4r3tKIX4-tTUSFnmRAY_0xcUA6shyGmZLM7dLTyjg3hdjXG5WAGGZq79WSaLz18dZNtCPRxk1bgmr0_mPevP7Kul0DO4g2a_uaX9MAl5d4T-kOfwa9TmUHqQqOwe7-l_-uhNFUKpMyLx_sb5nv7BW8lbV7j-U6LxyHhMWPic2tKhl7O1aPFaCt4BtNrOZl8zzJDnA68SpiEHBvBdVtj6xtiUItcnzhuTQRq-Xrf-uMNMju0EHhqqy3gPo5WII0gdFnfoHl-HekSL251P4ehFYr7Al0IvyNxIXb0yB8IPFXgz1c3-d2t6gWFxN7zfGqdgRDV2ik-1A8ERqhAXuiezjjnrFwF3lsKbrTOU6jYFUfPzKoj5ngllnivj0aYZECalHZF1GjFTJIwBaqeH5sjHT0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8676bf1957.mp4?token=HW_JumWO6gcAW7rVCqWsgw_adCOcwW5lZ3cyiduP0d5dAYQHObwG2hHsgKo-AJ_xQ1jnWooSorstEvM8qOKvZ_PGEH6dslBp0J7-_9zIklvBETWMztmtzEhnT5r7ATOqHudBYJ8z_NO11VB7Cdu8fHXUij1Lcv2TRtBPZvdZwuQaTZ2gLLwj7e9fN8I3t55h79LV-kk5zvcuQRFkZtPw1SMQWrPX1fAK70deyCauPeLMfRxLeKhu_L2JiwbXpXVQefRinYX4Dhuo_YE8GsGyo4r3tKIX4-tTUSFnmRAY_0xcUA6shyGmZLM7dLTyjg3hdjXG5WAGGZq79WSaLz18dZNtCPRxk1bgmr0_mPevP7Kul0DO4g2a_uaX9MAl5d4T-kOfwa9TmUHqQqOwe7-l_-uhNFUKpMyLx_sb5nv7BW8lbV7j-U6LxyHhMWPic2tKhl7O1aPFaCt4BtNrOZl8zzJDnA68SpiEHBvBdVtj6xtiUItcnzhuTQRq-Xrf-uMNMju0EHhqqy3gPo5WII0gdFnfoHl-HekSL251P4ehFYr7Al0IvyNxIXb0yB8IPFXgz1c3-d2t6gWFxN7zfGqdgRDV2ik-1A8ERqhAXuiezjjnrFwF3lsKbrTOU6jYFUfPzKoj5ngllnivj0aYZECalHZF1GjFTJIwBaqeH5sjHT0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🎙
عایشه‌گل جوشکن، بازیگر و خواننده ترک، در گفت‌وگو با مجید واشقانی در برنامه «رُک» از ماجرای آشنایی و ازدواجش با همسر ایرانی‌اش گفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/105811" target="_blank">📅 19:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105810">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZ0Gh6rzJWFxxT5u5qYT-JsFEsesnjqmWlVypnGSr1UjoG5Kb-eKm50TwnwVeC6h1XMADROBtvpwl39TDB_Z2JR-OBl_YMm4NgkUxN73BxuozC2enz0Z34T43KmWLHD2xur2ttZGveB7qy6btvcDqttrBoObDXAtwfR3ywmDzlLeVKeVh75EoX5C77_YFsH0EaX-ZaLl3AtbKx_jI3p87lgmjV3eXZwlXJ_tpBvTn26FASiyySQrxV1cO3QUZSVcPiPyy597y_lw3g626RgnS3T9o8RDJKBYyLBeMSOyIom53brLQBuWkBmKEox8bJ2EN9PMZh6GERbRUjdL4m02rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه موضوعی هست که فکر می‌کنم تقریباً همه ما به‌نوعی باهاش درگیریم؛ هزینه و شرایط بنزین.
شاید خیلی‌هامون هر روز درباره‌ش صحبت کنیم، غر بزنیم یا فقط سعی کنیم با شرایط جدید کنار بیایم، ولی در نهایت چیزی تغییر نمی‌کنه مگر اینکه صدای تعداد زیادی از مردم شنیده بشه.
برای همین این کارزار راه افتاده تا نظر و درخواست مردم درباره این موضوع جمع‌آوری بشه.
من خودم اینو امضا کردم و فکر می‌کنم اگر شما هم با موضوعش موافقید، چند دقیقه وقت بذارید و امضاش کنید. حتی اگر فکر می‌کنید یک امضا تأثیری نداره، همین امضاها وقتی تعدادشون زیاد بشه می‌تونن نشون بدن که این موضوع برای تعداد زیادی از مردم مهمه.
اگر دوست داشتید، لینک کارزار رو برای چند نفر دیگه هم بفرستید. شاید همین کار ساده باعث بشه افراد بیشتری از وجودش باخبر بشن.
🔗
https://www.karzar.net/346254</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/105810" target="_blank">📅 19:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105809">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sZ7sDUS6sKJuCjo_harl7wGl-eVae0kvM0RizmpbhhQ2NC34ou_ZeStF6p-1LbS8h_4rQjMpLflqGv9raD5rl8vP8q9uYZkXFLuM2D0X6YEacEeX-ODo6gCte5J-ENnePNRmdxXv2BCSa1NQ-DbQkMx9pne-gpO0YCnoxwE9rxCuKz7iYT2pj5mecDldPunEEe3OCFQZDe9Pq5VO9M4tHNxiiTtUuxL6m6kf4QzmIGBUTUhyqNO54NEUEOzxiy8zqlm0AXAk_ojEqbJai-n_oH82Bxggd1QZLKMTeMb6E2I7eOmGeTyS0cONreb1fnxvA4jvvAiD-EEIWqX77j49lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🏆
اگر حق رای دادن را داشتید، به چه کسی برای جایزه توپ طلایی رای می‌دادید؟
🎙
کیلیان امباپه:
🔴
من برای خودم برای جایزه توپ طلایی رای می‌دهم. این یک جایزه فردی است و باید دید که بازیکن در سطح فردی چه دستاوردهایی داشته است.
🔴
برخی می‌گویند که من یک فصل بی‌نتیجه داشتم، اما من هرگز برنده توپ طلایی را ندیده‌ام که تمام معیارها را داشته باشد. آیا بازیکنی وجود داشته که به طور یکپارچه توپ طلایی را برنده شده باشد؟ نه. این بدان معناست که همیشه کسانی هستند که فکر می‌کنند بازیکن شایسته آن نیست.
🔴
اینکه من بهترین گلزن تاریخ جام جهانی هستم، چیزی است که در ذهن مردم باقی می‌ماند. اینکه من بهترین گلزن تمام تورنمنت‌های بزرگ هستم، جایی که بهترین بازیکنان بازی می‌کنند، لیگ قهرمانان اروپا، جام جهانی، نمی‌دانم آیا کسی قبلاً این کار را انجام داده است یا خیر.
🔴
من کسانی را که با من مخالف هستند درک می‌کنم، زیرا این یک دیکتاتوری نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/105809" target="_blank">📅 19:16 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105808">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32837e6be8.mp4?token=cI2rgbKxTonIdp22QEAUcpo9-QriJ7InDVMNWe--SMlLnED4COeCeC5pNTLQyJQJ-QZkBIQCixHmUVzha1HFJ_y1Y2Xq1HMG0J8en1fuxAQ0Yc1wB4Wk8seR1vSktiPmH_4EXLnaR9ff6Ja1WWB2vASu7pRRJ0wYtU65WZrPqcGK041l5oYAKItD6JwxOyzpxpqBcYWb-pFtx9VBMPhpC44FVyw1Wa4eUn0OQROgqjcZTBax53wy6RkjLaYrmOfjAJa9NzswfY-I8pcDqgSYR9upwm2-CSopHvZniJqvH_IA7_1ORYkXAD70J-FgfkXgH4fhvQYMQiuTKn28Hb2-zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32837e6be8.mp4?token=cI2rgbKxTonIdp22QEAUcpo9-QriJ7InDVMNWe--SMlLnED4COeCeC5pNTLQyJQJ-QZkBIQCixHmUVzha1HFJ_y1Y2Xq1HMG0J8en1fuxAQ0Yc1wB4Wk8seR1vSktiPmH_4EXLnaR9ff6Ja1WWB2vASu7pRRJ0wYtU65WZrPqcGK041l5oYAKItD6JwxOyzpxpqBcYWb-pFtx9VBMPhpC44FVyw1Wa4eUn0OQROgqjcZTBax53wy6RkjLaYrmOfjAJa9NzswfY-I8pcDqgSYR9upwm2-CSopHvZniJqvH_IA7_1ORYkXAD70J-FgfkXgH4fhvQYMQiuTKn28Hb2-zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❤️
بازشدن پرچم 6 از سوی هواداران پرسپولیس و کری برای استقلالی ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/105808" target="_blank">📅 19:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105807">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3392d48f0.mp4?token=OBLXf3P-jrh5pADKrlXbBuhNqSfuptC9Al8Ko_7DZ3KqQw2fUZ0FjqbR9n5H_YunQ93tk8z2yLOd5l6JVHZZ5b5EoBC3JTBGo5uyMTfXg6fxYZ8bscWXM8XNCnLWk24v5hzrst7ExCTqzHOqgVCBYu58tkCml86_0Da1NLWnsc83oul0rXgjAsULqJBnBSkrIZSrHvxUx8pd9cYjqJK15KlY7tj3TXpuoEENo-v-DOxLybo62LPzxozE0mV4m2rPg95j-uezlTpUHjtoBfOdF6EO5cbhWVa0VZ16e6WMDuSFeIoaTKJXVPqGmta-QOKElWjQNADNtfgz0SJwAph5ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3392d48f0.mp4?token=OBLXf3P-jrh5pADKrlXbBuhNqSfuptC9Al8Ko_7DZ3KqQw2fUZ0FjqbR9n5H_YunQ93tk8z2yLOd5l6JVHZZ5b5EoBC3JTBGo5uyMTfXg6fxYZ8bscWXM8XNCnLWk24v5hzrst7ExCTqzHOqgVCBYu58tkCml86_0Da1NLWnsc83oul0rXgjAsULqJBnBSkrIZSrHvxUx8pd9cYjqJK15KlY7tj3TXpuoEENo-v-DOxLybo62LPzxozE0mV4m2rPg95j-uezlTpUHjtoBfOdF6EO5cbhWVa0VZ16e6WMDuSFeIoaTKJXVPqGmta-QOKElWjQNADNtfgz0SJwAph5ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
هواداران پرسپولیس در پاسخ به فحاشی خداداد عزیزی به امید عالیشاه، کاپیتان سابق خود را تشویق کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/105807" target="_blank">📅 18:48 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105806">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105806" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/105806" target="_blank">📅 18:48 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105805">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4au16FRUIpVzLDDVRZRo9WrPuJnRDq2OGDzUD_54dWENce3dYgjtQaVY5L85g-yYgqwtA8a6iMWkt3C5otJNdD6Hrijs7jcl8BsDXrYCWq7h9B8SNYUyUtUlhZYmtHQKg4M7JSkAG6ULWZ9B8dwf6yDLatEgpHAc7FlL1w_zIXQcjYhHIsSWZukajQlEOd16JFJYMlZvsjAe-rm2uzjHdrifxjISd4jk6iMGyGT1xEDv9cm2BEaY0tq0J54bakdhLeX1LefCoCgrq6infbdkWfYTb8XCYMghvfRqjNaEn2iFh2T4r8eMifJ3zWOlausina6VUWCsDsukeT-A-qxpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105805" target="_blank">📅 18:48 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105804">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TeAIjcaPSDb4z7Sx1d_0bdEl3GazV1_yWbWT2qkUxsdYdXyspSXrQ2A-gORq6B3IQj4kO07aD8eQ_dSFJ4mYtRFphGUiZ33f8cu9o1v6YqcZDL4yYDZjtjKmiOHibTl2l1TH6UVv647Ja5-0Oj1mSah68R93NNr6WYPusqPeidGCl8WO-5k-LsvymeFnyFyMnY9ziZQJDb6wa9qK96E5FWK8hu3rexXTtnpMKBJcmTEoJ1NoQFXEAmENUczBiPEzanoy-v2KeuEiMyuCTl5AXZVPUhXfafP5c197cTlezPmfmjkk4Ick9C78hNQu5PPbz6sx1wAeE3o6jnwuA0QCgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔴
شماتیک ترکیب پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/105804" target="_blank">📅 18:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105803">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b66914acac.mp4?token=aRFmDZmb2lXdExf1uH7W4xncv_eALs7ugalpoZ4Yt3Uo11GhEIQoe-EPpvNIaSFNVz6AyWdJ8la-4T0kne4u-16vfLEIum39CmROdvNnuR4_oxfTcR6P4xFl4V7c4qXQTqNfW_evcYKJ4ldBw10t7gWlzqKLD4sZlJqW_EX8golY_itN_b1dCy1S0VPsY4e53OTtRmDdooVXQizwX45dnquZAxHnYKzgy7AHjba5cbYmMTwxPawxsDfnFz7DSam9IPdDgtOQ3Zxexds-sdDTi9XPjMSuEVDbw7EnDoqXKVKf7N135Ucd558m3MsPuGyXLOfUYNfYqZe968IhbIja6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b66914acac.mp4?token=aRFmDZmb2lXdExf1uH7W4xncv_eALs7ugalpoZ4Yt3Uo11GhEIQoe-EPpvNIaSFNVz6AyWdJ8la-4T0kne4u-16vfLEIum39CmROdvNnuR4_oxfTcR6P4xFl4V7c4qXQTqNfW_evcYKJ4ldBw10t7gWlzqKLD4sZlJqW_EX8golY_itN_b1dCy1S0VPsY4e53OTtRmDdooVXQizwX45dnquZAxHnYKzgy7AHjba5cbYmMTwxPawxsDfnFz7DSam9IPdDgtOQ3Zxexds-sdDTi9XPjMSuEVDbw7EnDoqXKVKf7N135Ucd558m3MsPuGyXLOfUYNfYqZe968IhbIja6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇺
🇪🇸
خولیان آلوارز در مراسم عکاسی UCL
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/105803" target="_blank">📅 17:39 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105802">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdea9220e8.mp4?token=CsisuHAoNrZyEirsKQdYno_40xdYTPAqnFYSRDHt-8zC2YpU65sPGgA5XUXZrVesBeD9iSXxuh4r_aKxBcPny8uzQBI-I7353ktwfWKb7V97p7POYW4eZj5Psf_ACpOMXeb1Kx4B4N6IYP41TU4et36YqdHElMJGsBBNlUjz-4ER5w5bwZOTfT_cuZWvTPiLVKlIgEvGqtHhETV6Yr_glZWGCRkyfgD3GEeEyhKv2IEBcNv7qP3q45dZL7Kyc3Rq5unugs-cO72-cqWXdeowa5lFyy1inpliiXzUTXPYqJ0F6MtMRCIaJk7ksz1ZDjDP0la7IgTV_zRNAe9_Yyjc4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdea9220e8.mp4?token=CsisuHAoNrZyEirsKQdYno_40xdYTPAqnFYSRDHt-8zC2YpU65sPGgA5XUXZrVesBeD9iSXxuh4r_aKxBcPny8uzQBI-I7353ktwfWKb7V97p7POYW4eZj5Psf_ACpOMXeb1Kx4B4N6IYP41TU4et36YqdHElMJGsBBNlUjz-4ER5w5bwZOTfT_cuZWvTPiLVKlIgEvGqtHhETV6Yr_glZWGCRkyfgD3GEeEyhKv2IEBcNv7qP3q45dZL7Kyc3Rq5unugs-cO72-cqWXdeowa5lFyy1inpliiXzUTXPYqJ0F6MtMRCIaJk7ksz1ZDjDP0la7IgTV_zRNAe9_Yyjc4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
💙
پژمان ماندگاری مدیر رسانه ای استقلال: با صالح حردانی در ارتباط هستیم هم من هم باشگاه، ولی باید زمان بگذرد تا اتفاقی که بین باشگاه و حردانی افتاده است حل شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/105802" target="_blank">📅 17:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105801">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e983fd5a.mp4?token=EM4TLBeEMQn-1E0panmcW4eZ-IYx1Mabukbj6Okng5H_u431QCyVuHnaMWT1UypJeUijZpfwEZe3MUc_4bD5VxA2lQxVr72KFGFxC9DdVAcjUfphQib8zqXPd1YVnWDes04e9IE_5hOtO1aIg2bViTTsKX07EbxdjyssDir6-xKP1JIMKpgRmKMD-3ivb739XdJi9EEARbHjSgeQU0oqlAYYn2LAzCehN3-KC5Nxx_QCa6AOetsDZW_o2SRS9pzHfNWlaAjRIniKrQKrHWi4m9TDypem39mChSKv19Iqxj_yngcSciRX1oWGB3N91kGBcDweJzoGGDZsLINbK3MkGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e983fd5a.mp4?token=EM4TLBeEMQn-1E0panmcW4eZ-IYx1Mabukbj6Okng5H_u431QCyVuHnaMWT1UypJeUijZpfwEZe3MUc_4bD5VxA2lQxVr72KFGFxC9DdVAcjUfphQib8zqXPd1YVnWDes04e9IE_5hOtO1aIg2bViTTsKX07EbxdjyssDir6-xKP1JIMKpgRmKMD-3ivb739XdJi9EEARbHjSgeQU0oqlAYYn2LAzCehN3-KC5Nxx_QCa6AOetsDZW_o2SRS9pzHfNWlaAjRIniKrQKrHWi4m9TDypem39mChSKv19Iqxj_yngcSciRX1oWGB3N91kGBcDweJzoGGDZsLINbK3MkGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
💙
پژمان ماندگاری مدیر رسانه ای استقلال: در خصوص ماندن یا بازگشت صالح حردانی جلساتی در حال برگزاری است اجازه دهید خود سهراب بختیاری زاده در این خصوص تصمیم نهایی را بگیرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/105801" target="_blank">📅 17:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105800">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/533e25adb5.mp4?token=P2-HON9MhJ32qGhMRMffskdayOqNuIZPTzogvmIKgee6qD7k7MwWNUGH1VamMxXY4x8xW-zHmcPsLiuDbCBNteBsrjCXyAV4RfG9YCaLhmXoLl6zSEVHyZ3GHuTf3aB5u3Dr19kCKHJZVE1QqcFrG7CnTL5k4oDElXKBVi4AQrb9razmc7QGM15p-cKCnRMAfcjpQXQR8yNuSb3uECv3ueSudBLHYicN9ElpjRXe4RaV7nxlHIqLubhY61oPS-F3OPXK-8VZ0tbSsnhLzh6dkhguzpSSwphDh8q_cDfbpL8gaELVCroZUYttUPWREi09m6eonkzoXDWRgeOLFsd7Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/533e25adb5.mp4?token=P2-HON9MhJ32qGhMRMffskdayOqNuIZPTzogvmIKgee6qD7k7MwWNUGH1VamMxXY4x8xW-zHmcPsLiuDbCBNteBsrjCXyAV4RfG9YCaLhmXoLl6zSEVHyZ3GHuTf3aB5u3Dr19kCKHJZVE1QqcFrG7CnTL5k4oDElXKBVi4AQrb9razmc7QGM15p-cKCnRMAfcjpQXQR8yNuSb3uECv3ueSudBLHYicN9ElpjRXe4RaV7nxlHIqLubhY61oPS-F3OPXK-8VZ0tbSsnhLzh6dkhguzpSSwphDh8q_cDfbpL8gaELVCroZUYttUPWREi09m6eonkzoXDWRgeOLFsd7Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
پژمان ماندگاری مدیر رسانه ای استقلال:
🔺
مصاحبه پخش شده از بهاروند در خصوص قهرمان لیگ تقطیع شده بود/ آخر مصاحبه می گوید که هیئت رئیسه فدراسیون فوتبال می تواند دوباره در خصوص موضوع قهرمانی لیگ بررسی های لازم را به عمل آورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105800" target="_blank">📅 17:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105799">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b75db3430f.mp4?token=CCBPyMk66kYdDQK_IJ9tAALuKWMyAC-jWb3w6-1nQm5t9Bv8lOGLJpv8X5GOYf7fXc0E1d_p6jON7bmeFix67Ee42shv_wQlEa_vw_h5dPoSGTk1oo9EJovy4cYF5t8qwNuMwo4SY6e0ZK0Mt6ChTqWQ89N5EOIdCdPpfxy_6N1rFk7aJG5NbEGVv0rbc_T__gSsFlx4ZzRrbBYPKpFgeS_W7GHIWGldNIFhsXrjWxCP21UBtOWlJAMozJcN8ccKohPihthsavhdvBnDnUkQALgNS95f8BxL-gJcTrUl4T13G1USKNQuA7OrST-4x1iqsSqQgigbFJ6wbuPEgcedsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b75db3430f.mp4?token=CCBPyMk66kYdDQK_IJ9tAALuKWMyAC-jWb3w6-1nQm5t9Bv8lOGLJpv8X5GOYf7fXc0E1d_p6jON7bmeFix67Ee42shv_wQlEa_vw_h5dPoSGTk1oo9EJovy4cYF5t8qwNuMwo4SY6e0ZK0Mt6ChTqWQ89N5EOIdCdPpfxy_6N1rFk7aJG5NbEGVv0rbc_T__gSsFlx4ZzRrbBYPKpFgeS_W7GHIWGldNIFhsXrjWxCP21UBtOWlJAMozJcN8ccKohPihthsavhdvBnDnUkQALgNS95f8BxL-gJcTrUl4T13G1USKNQuA7OrST-4x1iqsSqQgigbFJ6wbuPEgcedsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
هوادار پرسپولیس
: ای کاش خداداد عزیزی سُر می‌خورد و آن گل را نمی‌زد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/105799" target="_blank">📅 17:26 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105798">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a65105bf5a.mp4?token=RIz0g9GR5U6fs0JmXAgRLUhGhp78iMeDSjQ56FgBUBllXspoMM129D9Ifgaz7W2vu2AA9gQ9eIYmFRHRYlVcavp8agoAkxgCiqVJZLhhz08z7NP9NP6A-gJouxElrJBZ9o0L3NIIFv0bZ8r2jC8SPq9lnkPFZwvcRjaqzDAgrY0fYpqLoIss0tQOy-lszsvnZ9OX1LDdSr2bL-HxJde6yiBBy2fI0KV-o6nDBQ4bpKZk4Zh8CAmIi6Hp2qqus4q86Th3D_SGbl7hXu4Ejo1rnsereQNeqGGTuKWtBdtYjiwZwh28GE0_nPCgPspwYtCnyXhzC-jbHyvyLgtZLSjvOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a65105bf5a.mp4?token=RIz0g9GR5U6fs0JmXAgRLUhGhp78iMeDSjQ56FgBUBllXspoMM129D9Ifgaz7W2vu2AA9gQ9eIYmFRHRYlVcavp8agoAkxgCiqVJZLhhz08z7NP9NP6A-gJouxElrJBZ9o0L3NIIFv0bZ8r2jC8SPq9lnkPFZwvcRjaqzDAgrY0fYpqLoIss0tQOy-lszsvnZ9OX1LDdSr2bL-HxJde6yiBBy2fI0KV-o6nDBQ4bpKZk4Zh8CAmIi6Hp2qqus4q86Th3D_SGbl7hXu4Ejo1rnsereQNeqGGTuKWtBdtYjiwZwh28GE0_nPCgPspwYtCnyXhzC-jbHyvyLgtZLSjvOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدون‌شرح :)))))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105798" target="_blank">📅 17:20 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105797">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ce531ef9e.mp4?token=WC70BD_FUEeQyMf_yk8rzbA510to-y1aAImnqAH-BjnnihBpN0m-qgxt9I6TqZUuPDKEV7KF20JrTOLiZvSK0iEQrch2b-nRUgNjVoJM7BZRGAgXBAsNDZnGQL69xds0fiywycs-ViC8X0o6pp_iwK5kRc68cxgQk1OsDP3yJT4gygPSxvJVeHaYQSoQcLKXNPz_92y8lm2FIVMnrZt_kQN_tl8h9ahv2xniHEq3-2L4abXsiYsng24unVUS9azgSSN4miqnmRJMrMJdQCs9yKSyXBPPg4kauqeoMgaSrPikabsVfUURJn6RBmkZuOP1exlo6JaX2QJ78qGXLbbryw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ce531ef9e.mp4?token=WC70BD_FUEeQyMf_yk8rzbA510to-y1aAImnqAH-BjnnihBpN0m-qgxt9I6TqZUuPDKEV7KF20JrTOLiZvSK0iEQrch2b-nRUgNjVoJM7BZRGAgXBAsNDZnGQL69xds0fiywycs-ViC8X0o6pp_iwK5kRc68cxgQk1OsDP3yJT4gygPSxvJVeHaYQSoQcLKXNPz_92y8lm2FIVMnrZt_kQN_tl8h9ahv2xniHEq3-2L4abXsiYsng24unVUS9azgSSN4miqnmRJMrMJdQCs9yKSyXBPPg4kauqeoMgaSrPikabsVfUURJn6RBmkZuOP1exlo6JaX2QJ78qGXLbbryw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
بعد از دعوای خداداد عزیزی و عالیشاه آدم ناخودآگاه یاد این صحبت‌های اسطوره علی‌دایی میفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/105797" target="_blank">📅 16:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105796">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc7d165fd0.mp4?token=idxTSOrbrC-9ugVWC2k7Cb01-a-iKYh8CjiNuy2RFjLWbnyz5XN3qmjuBHVYcqyvnxCOkVxMJzbDUDjNBHoR2nWsPmKCvpQBmq4jISREmjtXp3B6Ao3Lxm-xar2Lxid4MbiarwpHonwiiqmOeVWx7K0QUGNN94KZFAM6KAKUrUdEV9rXFFyRAgZU3oc1mDXdrUzH5ohn_EKgeSuHdP2GostTzJl_C4LdiTDmcuurOd0Rt-DBXCjRL98JdfiyYm-Q0Gyat8bRiYRVdTho64hgU5Q1i219a8z_jBs9YXD7j1qQTH9wJu9pO6e0ljWH55wq0tLDAMIWO9XbbBZwJ4Qlwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc7d165fd0.mp4?token=idxTSOrbrC-9ugVWC2k7Cb01-a-iKYh8CjiNuy2RFjLWbnyz5XN3qmjuBHVYcqyvnxCOkVxMJzbDUDjNBHoR2nWsPmKCvpQBmq4jISREmjtXp3B6Ao3Lxm-xar2Lxid4MbiarwpHonwiiqmOeVWx7K0QUGNN94KZFAM6KAKUrUdEV9rXFFyRAgZU3oc1mDXdrUzH5ohn_EKgeSuHdP2GostTzJl_C4LdiTDmcuurOd0Rt-DBXCjRL98JdfiyYm-Q0Gyat8bRiYRVdTho64hgU5Q1i219a8z_jBs9YXD7j1qQTH9wJu9pO6e0ljWH55wq0tLDAMIWO9XbbBZwJ4Qlwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
بزرگی و مردانگی یک بزرگ‌مرد، با حرف‌های پوچ و توهین‌آمیز یک آدم بی‌سواد زیر سؤال نمی‌رود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/105796" target="_blank">📅 16:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105795">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/608b5b0627.mp4?token=TS21B9WSvZHOKWuOSKZ5RpOtJy1sXCNiNxbLCzD76EMEj6cp0uAvfclnB8ZFRv-WlAX9wFnaak7gNVvfIYsXiELZqQ5f7t-G5ixNaVEtJ9AzzVqzk4PYFiam7NwSghMKFiFjxlBTKjeYv3JNFKSUZy51C8vJ6WeMRGrt7Yl0oyH5raB4gZrv3NqmyL1AdFOJDYzC71g-lyGaiVBXIZVjGY3AaR896sEE1ABO920qvFcTA_gys3OvDVGQoIaXwUYke1Q0hMEM41c9afI6KRyyH14H09FJXDEPrnnfXCgAnvksA9-L9v1NiNCkOaNeyUBjU8snlc8Ne3cyCXi8Z__bcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/608b5b0627.mp4?token=TS21B9WSvZHOKWuOSKZ5RpOtJy1sXCNiNxbLCzD76EMEj6cp0uAvfclnB8ZFRv-WlAX9wFnaak7gNVvfIYsXiELZqQ5f7t-G5ixNaVEtJ9AzzVqzk4PYFiam7NwSghMKFiFjxlBTKjeYv3JNFKSUZy51C8vJ6WeMRGrt7Yl0oyH5raB4gZrv3NqmyL1AdFOJDYzC71g-lyGaiVBXIZVjGY3AaR896sEE1ABO920qvFcTA_gys3OvDVGQoIaXwUYke1Q0hMEM41c9afI6KRyyH14H09FJXDEPrnnfXCgAnvksA9-L9v1NiNCkOaNeyUBjU8snlc8Ne3cyCXi8Z__bcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دعوای خداداد عزیزی و امید عالیشاه از این زاویه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/105795" target="_blank">📅 16:05 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105794">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQZx0rB_GiOVv7QTerBdYRFekvD8exGvxg1KQPkXrqj7d2PIHlEK5sqjB1A9hL9f7PBBKedHIZZxiTD-KFreTtAAkPAQpZaLqlnzAk4fhRlbcN9XURnKhopxN8ZvUURcLU2qnSunaweAVaIzK5qp6bfur-A0LRoKuEx8PdXuKiJdtT5r_wss0SzghvOTBTVRIYtGIK6SfXSoG8012F_mg3yKcKEchY_3Nzd4DILkOY8KX6eV2lxCZLyY-oznsiRwimD9HMMikisPIJksEIna9My5ph8HjutivKLP5wg7Z7nGs07F0tEYpbb2as1q2jhksCSimxc1SD9DbzbQeQ2sAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔵
هوادار جذاب و شیک تیم‌الهلال عربستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/105794" target="_blank">📅 15:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105793">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72559f2230.mp4?token=hqPwtHSwuzqUUsf3TSOi_hkwltRBvkpEdCemLVwvzPWu-Fi27k1wWy4OxfABSZkCgHqEwqIJkrtQsQQ2YwLXAxq2RLQHjcE67QPMrWhbIOpJRnXP9uT_mB_0Xa6jhpXTlYl4bmr1UItAesMRLATjwVDzLotYXB6b0CVPJzvA7F9c8nX_RK8UyiO4ZMZeCseaR5tndqiUEz-7mBiI2SlsfNxT34SzMNwsenwvP_7coydSKogrFfkGcNMAHKrYFE-dWcRV6fdV9sNfswVKX8BI_YOYUt-lYMrJDzBgvCR3NIqxwFzeVsA7-BF5xA7ZSrMaYaBlO8FrXjaBTiO7T6Gpcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72559f2230.mp4?token=hqPwtHSwuzqUUsf3TSOi_hkwltRBvkpEdCemLVwvzPWu-Fi27k1wWy4OxfABSZkCgHqEwqIJkrtQsQQ2YwLXAxq2RLQHjcE67QPMrWhbIOpJRnXP9uT_mB_0Xa6jhpXTlYl4bmr1UItAesMRLATjwVDzLotYXB6b0CVPJzvA7F9c8nX_RK8UyiO4ZMZeCseaR5tndqiUEz-7mBiI2SlsfNxT34SzMNwsenwvP_7coydSKogrFfkGcNMAHKrYFE-dWcRV6fdV9sNfswVKX8BI_YOYUt-lYMrJDzBgvCR3NIqxwFzeVsA7-BF5xA7ZSrMaYaBlO8FrXjaBTiO7T6Gpcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
جوری که دیشب هواداران والنسیا هنگام تعویض شدن پدری ستاره بارسلونا تشویقش کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/105793" target="_blank">📅 15:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105792">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2073e1633f.mp4?token=ApgOskQhJ73cndw7DOeAsGOanB4kU4SmvPte4EjiMJsnVWEtTO2teKdy8aMo1U_5iIHd1IWu9XWFfkOFwGiVV2Yrn_ZF5OG72TCF1iKNkHkiEo6a6mYkTCoSIG6KhC8QEeQTSQvkM5W8_L9XXZwNMP0YqIPMblkMVEsocXebFik5cW4mFnDWuHKwEWcNdZvPMdnVhZQNlCeeROL1F_9G9pjxCCgLWEljgpjmVgdA_TJmEGal42SuJ6VuMynNsSVw56EctyTdaBunNbMnNEVlA-E3J5Fqi9BdI-7RqQmSeOnktlW_kGFojZpaapWJ-6EPv0qZfuhZs0OjmOwDJuUmOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2073e1633f.mp4?token=ApgOskQhJ73cndw7DOeAsGOanB4kU4SmvPte4EjiMJsnVWEtTO2teKdy8aMo1U_5iIHd1IWu9XWFfkOFwGiVV2Yrn_ZF5OG72TCF1iKNkHkiEo6a6mYkTCoSIG6KhC8QEeQTSQvkM5W8_L9XXZwNMP0YqIPMblkMVEsocXebFik5cW4mFnDWuHKwEWcNdZvPMdnVhZQNlCeeROL1F_9G9pjxCCgLWEljgpjmVgdA_TJmEGal42SuJ6VuMynNsSVw56EctyTdaBunNbMnNEVlA-E3J5Fqi9BdI-7RqQmSeOnktlW_kGFojZpaapWJ-6EPv0qZfuhZs0OjmOwDJuUmOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🇪🇸
وضعیت شاهکار این‌هفته بارساییا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/105792" target="_blank">📅 14:50 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105791">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEeP5VKMc2hPVC6IabNwvAlYVQlivA7SmmQWPunl8EvHE5hjAWkjPQ8rrSc0jYDNg39oYm8lrKKRc2tuDuL1yO0iKCZt4vzhR2EChVjgn02VxFnj3tve3_Q_WMZI869kUzgEmLSWBifmOdTrAhQKDKS-0KYpHwu1e9vPfXk_Nj-gah4KUniFAPrRqnLSm42qK0r7uIcxlUPp0VDvY1fwi2Nocp2qP5O-GWSCKRoDIV2BdcJARUSZNm0Cx4OH2LSNCki1bToy6jO67WdQS2gdmXFkEcCTBuDTNKzqXR_lGxzwCtU5PiDieNMWladgC089AB-qb-HD1aqoqMNjT_t_Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تعداد بازی‌های لازم برای رسیدن به 300 گل
:
🇦🇷
مسی: 365 بازی، 300 گل
🇳🇴
هالاند: 384 بازی، 300 گل
🇫🇷
امباپه: 398 بازی، 300 گل
🇵🇹
رونالدو: 499 بازی، 300 گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/105791" target="_blank">📅 14:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105790">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7j1rB590KW0zz2ODRRTCdLfEjrpL1un8u_d7NcHsX0Fm5HrANGHqBQz13vZaLK0tGwY5YVNKpJLAYC0ct_e3vo2RXw5MbRHOtdV5ZT71-XaYVEnc6k-kxjKNENtyMiQ2sawZ46BTEvuLnB00wkoF5Qs6dnr-7t5iYuSLVpud5YqLMUkpUD122Mx57e6ZxPQnqNU2DIfO2Uf36T-BQRakhZOseHeUyz6g3ZtXH3zLqBLrk38sZjQaWHHYoZddS0gP6ayxE479QwHSZmFWrt-mRrQGixOScLPWi0vCgbJBfeB9nm-Jn9wDIqbWVOlLvhQnwS7-MHR2-yK-NFdHqJk0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇭🇷
🎼
لیست تیم‌ملی کرواسی برای فیفادی با حضور لوکا مودریچ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105790" target="_blank">📅 14:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105789">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iY4WNgi4sIDFAE9O4OEJLneMFN7s0UIie-FHjcXa5nAngaZc3twKDM4H7aYvKvJC-2rrcC6m1SsAFNHlCi6nPAhSsvWe22PwautemaeRH-QVdbqiqVEAPWVwXIYpS3whtdJOsTBtz8XwamJ-vJ6LHt9hWGYupITe24fqzfk_pWi9kFj8PLx1g85L_Ix4w2XFljv2FpN2kS3y4YZT505Mbx0Ay0hH9ecS_3fz516GwamHTjEEjCXCpqeG1xmzC3jDdpcYe7ox2z1yzE2EGS3FuTKQHd_WUl2l3H8fzcXAz9jD_02dQbKQmhtr7A328I3F8srCfLlni31S25GjFVUlpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🇪🇸
این تنها سومین بار در دوران حرفه‌ای امباپه است که این بازیکن هم موفق‌به گلزنی نمی‌شود  و هم چهار موقعیت گلزنی بزرگ را در یک بازی از دست می‌دهد.
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/105789" target="_blank">📅 13:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105788">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51d2063588.mp4?token=DAPl5WeuE6O5TlXkOQAgopDsSgyBzpPonUecw12TqYt5eAjnTZn40coDi304q_6kCJl8HpwGueJjbSHZQLYv0CnqP8bCFg9ieKN8rq-3YxZc-lKvBCApt3BXHJ8UqEWOdULKfHa3xCUI4vdq3mwONMwtELY2vre7XNAehDPGdyr8kW7sBSF4TztgY_-v_dHGACVM--QxTLOKevQl478ruJcpp_o3GC2PgH2oikP2_-4G8FlO6jkXlJx0BxK55LvM9zuTTog6-sa_SaNATc2MrzlitirvfLa9sULBWe9ko6YmBQPCboED_fx5EjMhR5ZWzfdCBsQkv2ao7GppfpM6TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51d2063588.mp4?token=DAPl5WeuE6O5TlXkOQAgopDsSgyBzpPonUecw12TqYt5eAjnTZn40coDi304q_6kCJl8HpwGueJjbSHZQLYv0CnqP8bCFg9ieKN8rq-3YxZc-lKvBCApt3BXHJ8UqEWOdULKfHa3xCUI4vdq3mwONMwtELY2vre7XNAehDPGdyr8kW7sBSF4TztgY_-v_dHGACVM--QxTLOKevQl478ruJcpp_o3GC2PgH2oikP2_-4G8FlO6jkXlJx0BxK55LvM9zuTTog6-sa_SaNATc2MrzlitirvfLa9sULBWe9ko6YmBQPCboED_fx5EjMhR5ZWzfdCBsQkv2ao7GppfpM6TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
😂
امین‌رضایی یکی از اساطیر سندروم‌داون در دیدار با علیرضا منصوریان در بغداد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/105788" target="_blank">📅 13:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105787">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/737dc646bf.mp4?token=PLnzUcmKhMWBMwMiAXYrtckTzJp-Qr1kgOL3uJCXbzPKZshE58_qty4MLxONLgRFGaR2sWgHABa2L3VZmElfBVj8surjMrBzOoXCnbjYJ5L2ee0iF_3V79bu2nCZDo8wQ28Ga3pZ99U_Vhn5klvEn6YJZTq5VJxG-2T-ll5ZTSl0lSftkIw50290EHHzJSS4UDqpN29UWTBOn50C_yNbnhuE5NXnNAmV1euwDD_4uSRDOcz8ab6XFAjoHvVUFCpMHn-EDqV4bch6WVMvzuePj_njpwJkrGiLlyTDeTysVaLA9dGjGthao8qsN9xYChROVyvv0-omwWyl15fdggmUQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/737dc646bf.mp4?token=PLnzUcmKhMWBMwMiAXYrtckTzJp-Qr1kgOL3uJCXbzPKZshE58_qty4MLxONLgRFGaR2sWgHABa2L3VZmElfBVj8surjMrBzOoXCnbjYJ5L2ee0iF_3V79bu2nCZDo8wQ28Ga3pZ99U_Vhn5klvEn6YJZTq5VJxG-2T-ll5ZTSl0lSftkIw50290EHHzJSS4UDqpN29UWTBOn50C_yNbnhuE5NXnNAmV1euwDD_4uSRDOcz8ab6XFAjoHvVUFCpMHn-EDqV4bch6WVMvzuePj_njpwJkrGiLlyTDeTysVaLA9dGjGthao8qsN9xYChROVyvv0-omwWyl15fdggmUQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🇮🇷
حمایت جالب هوادار استقلال از امید عالیشاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/105787" target="_blank">📅 13:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105786">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ca5c3fb8.mp4?token=gbekEcge7Dk7k3WkhaA7srWnjM9Iyg3HI4V4PSxAAAi-6a0b0OgjIS8rKEtyH47ANQG9yxsUO2Da6XDDjv1qWpezXtqOO5Oc1UXNxln6-RhhFGqWdZ3OEBxkUbu6VVYdrjaYZz8mPXa-P6yvm4nKtDkOdrSUFOAXWAB9-D91qtm5067E6ZWXek_BWPyHyjxmL3VkKShOvHHxQjToIB-DQs0ZATCcD1P28OdbjHFzVEtFPXrtE73HOpsnClYGmkx9MzHlgycX_B_B_H3ZRDPNyBe8VOOh-Jt7HyaeWn689-AlXOPIAQmdmwLobk7BXPeG68CJtaM7QYs5y2VwpD5goA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ca5c3fb8.mp4?token=gbekEcge7Dk7k3WkhaA7srWnjM9Iyg3HI4V4PSxAAAi-6a0b0OgjIS8rKEtyH47ANQG9yxsUO2Da6XDDjv1qWpezXtqOO5Oc1UXNxln6-RhhFGqWdZ3OEBxkUbu6VVYdrjaYZz8mPXa-P6yvm4nKtDkOdrSUFOAXWAB9-D91qtm5067E6ZWXek_BWPyHyjxmL3VkKShOvHHxQjToIB-DQs0ZATCcD1P28OdbjHFzVEtFPXrtE73HOpsnClYGmkx9MzHlgycX_B_B_H3ZRDPNyBe8VOOh-Jt7HyaeWn689-AlXOPIAQmdmwLobk7BXPeG68CJtaM7QYs5y2VwpD5goA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شوخی سمی همسر دیوید بکام با ظاهر عجیب محصول کشاورزی شوهرش
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/105786" target="_blank">📅 13:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105785">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4072bbde8.mp4?token=vUf93SBCNoh5c4MkDWPI8skDLwwsPcOChsY-lAbSlZvNzdnGt2fCtVGyRo1mUdhhCN4pC8bWCb79a6Iqkuf8Ubj_TzWl6V9A5eGq1bw_jPm7y4PN_bjk69XfRXknv8U6ET6MGsk-E2ad3UBK-iDgFlm5wn5_s24X0JdFhRgZZfLHDSoMXM1hfaorNVJw6DKggk-NtXLkZMKbHm8ADjSUfbPiqJpGdFvg55yPIieY9HIB-NH5V-4S3NTRCOid9Kh6Kq_Spa8M0oOlUQeWMH3G-tw6f9v38HY2tanXNPyzh1B58-1K-a_tC-QidEtdGiCvN29TsBOG5FdAAiAL8UeKeYUhOH3D2BQ2VH3hOb2PdzzkKbGrfFLrGb5AVjrEDB3tUDDGlz5YYTBXfH_-XYSDnKK9CsMXUBrA4wk7Z12fgK5U2Ph_kMxvlJ11d_pxvz5vpLHhdG3tsINo1e0M8mVJEZxpmw2juldHKghXhwhVl5vMPSPv9KLX9IHa-Ify8pJm8m47f5ijEU0wOSYxgEZqiMwhl2goKLuxwe3vg1ndNTD1Yn8sc2YMGcdADL3aRa1ppQ9nKAfO1S3CYPXrgS2Mc7WTfqonXOt6GrK1h03lBeGNaTKGaED8GDLf5R5isM2HOys47YvH9-B7qxvgrTgMeotPt5V9G3p6KXSUIM9yAdI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4072bbde8.mp4?token=vUf93SBCNoh5c4MkDWPI8skDLwwsPcOChsY-lAbSlZvNzdnGt2fCtVGyRo1mUdhhCN4pC8bWCb79a6Iqkuf8Ubj_TzWl6V9A5eGq1bw_jPm7y4PN_bjk69XfRXknv8U6ET6MGsk-E2ad3UBK-iDgFlm5wn5_s24X0JdFhRgZZfLHDSoMXM1hfaorNVJw6DKggk-NtXLkZMKbHm8ADjSUfbPiqJpGdFvg55yPIieY9HIB-NH5V-4S3NTRCOid9Kh6Kq_Spa8M0oOlUQeWMH3G-tw6f9v38HY2tanXNPyzh1B58-1K-a_tC-QidEtdGiCvN29TsBOG5FdAAiAL8UeKeYUhOH3D2BQ2VH3hOb2PdzzkKbGrfFLrGb5AVjrEDB3tUDDGlz5YYTBXfH_-XYSDnKK9CsMXUBrA4wk7Z12fgK5U2Ph_kMxvlJ11d_pxvz5vpLHhdG3tsINo1e0M8mVJEZxpmw2juldHKghXhwhVl5vMPSPv9KLX9IHa-Ify8pJm8m47f5ijEU0wOSYxgEZqiMwhl2goKLuxwe3vg1ndNTD1Yn8sc2YMGcdADL3aRa1ppQ9nKAfO1S3CYPXrgS2Mc7WTfqonXOt6GrK1h03lBeGNaTKGaED8GDLf5R5isM2HOys47YvH9-B7qxvgrTgMeotPt5V9G3p6KXSUIM9yAdI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
فرشید باقری، بازیکن پیکان: خوشحالم در پرسپولیس شاگرد گل‌محمدی و مطهری نشدم. اینکه بعد از جدایی به همه جا زنگ بزنند و من را خراب کنند، حرکت درستی نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105785" target="_blank">📅 12:45 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105784">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZataCB-NXxPzs080VhekdxbfOFkR1aT6vQcGGjMSza2KdeB8eeUrMB7FbNdMmZXMhqfWSGKajRGIYiHYWdKdss4xs-8pw1RdHKYzFrMs2hOfuv5WaI7brt688MASbjCpOnz1XPGZUOYiw8pr-hapXCKYCCdx1wKXQ0xdO8YkTFUoiXaVbyBaxMeBnAjYmG1ZoaYOqz3VTaAMB2RcwotU7s5WsPLj9ci5_hoA3iJUJnLCGoT8ihpL8JTqU8j62Qn2de4duQlR69-8egonQQctEYxePXuE6-3SxAywWpGY-R7mW5l1RpYcBbXHeQEJm1dakM04jknS76WQNRkMenHcbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
👩‍💻
💡
یه راهنمای فوق‌العاده کاربردی برای دوستانی که با برنامه‌های آفیس سروکار دارن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105784" target="_blank">📅 12:20 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105783">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4331728b0.mp4?token=YPpHwET6bWo0ElEAEsI7Hh2b4XoyEFUbvgcnSEX9cSByQLJSsWZqAB27uqEvMNmlBD9qkKG_NG-MhwWFjnv9_wwMaB1beCN1Z7cW6zuZi5kZvq1X3iGX3oHMrjcfQ6eoq-llmRxkSiSEfaT8LCQzRP8Mx-au8KJPJlXaAZP_T1MLYofb2cF1K4UfotQG-7NItlhBDiHYdSIIrKBTGDt3CqWBYglI-M4oQg3G7g0xm1lFUfPX2o7evzUohGxKEH6-oC89tJEUSJ0yzxJHOS0-a1rF5O-dWdbiSwxa5MfVsY3JjT8P7jvBlGxcnwlEPjmoZubGDitOEWHuycBtPqcLRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4331728b0.mp4?token=YPpHwET6bWo0ElEAEsI7Hh2b4XoyEFUbvgcnSEX9cSByQLJSsWZqAB27uqEvMNmlBD9qkKG_NG-MhwWFjnv9_wwMaB1beCN1Z7cW6zuZi5kZvq1X3iGX3oHMrjcfQ6eoq-llmRxkSiSEfaT8LCQzRP8Mx-au8KJPJlXaAZP_T1MLYofb2cF1K4UfotQG-7NItlhBDiHYdSIIrKBTGDt3CqWBYglI-M4oQg3G7g0xm1lFUfPX2o7evzUohGxKEH6-oC89tJEUSJ0yzxJHOS0-a1rF5O-dWdbiSwxa5MfVsY3JjT8P7jvBlGxcnwlEPjmoZubGDitOEWHuycBtPqcLRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرد آلمانی بعد از شروع فوق‌العاده در لالیگا و ۴ برد متوالی و ۱۷ گل زده: تقرببا بی‌نقص بود، چون هیچی بی‌نقص نیست و همیشه جا برای بهبود هست!
بارسای تقریبا بی‌نقص هانسی فلیک در صدر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/105783" target="_blank">📅 12:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105782">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105782" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/105782" target="_blank">📅 12:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105781">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ncLzYKXSELUGDffKfePQ7uS-9gglwHsr6K27_SGmIAihJLpwwzrLLjhQfvQUU8cHZyMAn-GF3zNz8OEepQbzfxG3zedK2zB8TygRFXSO6JXZL4KLfMD-j8cs887RTFNKPEIQnhr7Uzq05zhjNCD6CX9VaYYoPzuFQx0owDOiidsgPc0c2Ni2lvcOIe30yzYVRRhrZm-9gVdIb4uR6Wm8z-G2PPJLBj0sDdv5AplC7_WnXbT6joLXgzefc7qlppK2VYkDl0dO_kIzIlpekPkmnOaQH8MwyqqbLMa6qPXJQcXqdc1K_XW4kr0L0lXs_0bPdB8X24lh-aTgdQDa_AxhYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب
⚽️
ذوب‌آهن
🆚
پرسپولیس
⚽️
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
📊
نگاهی
به آمار ۲ تیم در در این فصل
ذوب‌آهن: ۵ بازی ۱ برد, ۳ تساوی، ۱ شکست
پرسپولیس: ۵ بازی ۳ برد، ۱ تساوی، ۱ شکست
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
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105781" target="_blank">📅 12:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105780">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1732fa7bfa.mp4?token=jH22a_UhXhBYICG4mzaS3WNiFAsXM_H4pITRyQ8mcXlDrvvw4A5RK5xpm6ZtFosTt7_fwFOQv0cG-oZJGnMdp8COV9mFT_bInMw0xgGvwqm-ekHrPqwwUVGpAO9ThCksY-Oob4jIDP3jMcSCNX98fuh3OhP73gHCOg0L7Fok1tXRlONKzLMRIkIunEGR3NTi2MboHFqCLD6KYpJqqEzdW1h0ZCDraGyPbqb8DpFiHUE6eXzTxHSXa136p3fCOIGgTgve3B-K93du9jYvvxtvlyMdl-ugqSsJXPoOrelxKDrJKvGKZF_QbmxnpGZ3S5Gg6WczMrvRTXYMpKOxMnSE2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1732fa7bfa.mp4?token=jH22a_UhXhBYICG4mzaS3WNiFAsXM_H4pITRyQ8mcXlDrvvw4A5RK5xpm6ZtFosTt7_fwFOQv0cG-oZJGnMdp8COV9mFT_bInMw0xgGvwqm-ekHrPqwwUVGpAO9ThCksY-Oob4jIDP3jMcSCNX98fuh3OhP73gHCOg0L7Fok1tXRlONKzLMRIkIunEGR3NTi2MboHFqCLD6KYpJqqEzdW1h0ZCDraGyPbqb8DpFiHUE6eXzTxHSXa136p3fCOIGgTgve3B-K93du9jYvvxtvlyMdl-ugqSsJXPoOrelxKDrJKvGKZF_QbmxnpGZ3S5Gg6WczMrvRTXYMpKOxMnSE2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لندن مطابق سالیان اخیر قرمزه
😂
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/105780" target="_blank">📅 11:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105779">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be20a40432.mp4?token=VUhdI5ds0ShRbl21JPSRahTtjQqW_y8u6_IYHani-7Q947oYHsUXIdQDuONjLuoZMzC4hfZc1Lq1koYUjB2npoL2BypLJzB1mTljfOIUo2fLynn23N1IjcIg3eevfx40k7vytNkLlw8Pd-J_0L_aWUROk5ED3Xw4Q83Te8ebA3JH4nTorUOjU-ox8oTEkaTT4AozgUlZ82M6EBwafmtuN6yqZ1FN3j15pjFCkRaAKlYaJocHxeWQCWyEjIlsYjH_39xE6oqoaFCWcjPoRxO02HVyov2-JSXUonF0zMaWz-AF3WasepUUOW2fDsKYgcea_4myEbp42is69CV0cTt4mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be20a40432.mp4?token=VUhdI5ds0ShRbl21JPSRahTtjQqW_y8u6_IYHani-7Q947oYHsUXIdQDuONjLuoZMzC4hfZc1Lq1koYUjB2npoL2BypLJzB1mTljfOIUo2fLynn23N1IjcIg3eevfx40k7vytNkLlw8Pd-J_0L_aWUROk5ED3Xw4Q83Te8ebA3JH4nTorUOjU-ox8oTEkaTT4AozgUlZ82M6EBwafmtuN6yqZ1FN3j15pjFCkRaAKlYaJocHxeWQCWyEjIlsYjH_39xE6oqoaFCWcjPoRxO02HVyov2-JSXUonF0zMaWz-AF3WasepUUOW2fDsKYgcea_4myEbp42is69CV0cTt4mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
⚡️
ویدیو بسیار‌کاربردی از بات‌های جذاب تلگرام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/105779" target="_blank">📅 11:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105778">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/872be66f89.mp4?token=Ygk8AtFl5mEZT1F2TwB9IP31dQlIATQQ7iB0fv9njX_KFkHr9Tr7A0VWPKr0HitpSLOSXoMzNZmoNLyoOJycPQurjzsVy-HjDUd_DuumMS4RyhcqnfWNYzVlqgGMltdP2n7PxHLkjNQANnv8h2fZ-wgixhCe5tLJlkC6C5VIjy4WKXIoJquEo8zUHYmaTkm6DpBPojHPVlNwIR2aYLQ98fWGakdZx0gjiNJng4HVGx18nXdl0-bUivLk8Y1Nbwf0j4DkvcmTETs7QHgoQQeo7cMIML2TuP5Z6x7L553KLCWIXu7jtsOBvQAp3tnKxSwRd1amOqhvZtUUwhaQo7XzNoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/872be66f89.mp4?token=Ygk8AtFl5mEZT1F2TwB9IP31dQlIATQQ7iB0fv9njX_KFkHr9Tr7A0VWPKr0HitpSLOSXoMzNZmoNLyoOJycPQurjzsVy-HjDUd_DuumMS4RyhcqnfWNYzVlqgGMltdP2n7PxHLkjNQANnv8h2fZ-wgixhCe5tLJlkC6C5VIjy4WKXIoJquEo8zUHYmaTkm6DpBPojHPVlNwIR2aYLQ98fWGakdZx0gjiNJng4HVGx18nXdl0-bUivLk8Y1Nbwf0j4DkvcmTETs7QHgoQQeo7cMIML2TuP5Z6x7L553KLCWIXu7jtsOBvQAp3tnKxSwRd1amOqhvZtUUwhaQo7XzNoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
هایلایت‌درخشش دیشب لامین‌یامال برای بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105778" target="_blank">📅 11:05 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105777">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUvqN_8KKcbEMAKy1GSQNr4q7wONfguLHWujRlABxDivceE6lbsTlWjscHsXczGvy_Ko1wXNqzHxCnVrJIi2VBM-TRWAVIZGFj2vbCgy5rGNdq2w9FeAF-9-HHaPEX61O5Hk2oDDguFd6HFsloGVvSctl_6zIKrbVxQCAm6OnSpRrfZuxu-fkSrBPQ6VwfcI5HvgEoLV4xG_jOILECjCwwWZeuCS2NJnQ_qk3r1xo1kFcJgS-DqyfFVr5oiKGyZ0ZaRwU4rW7aOqXEAFb8fI3Bu9XxEN3nH3JwR_ThxGXR65weSCLSb0xgeac_LLpLJGc0208MxdxIdFA7i77WYLow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
💸
بالاترین میزان حقوق در بین سرمربیان جهان؛ هانسی‌فلیک بهترین سرمربی فعلی جهان در بین ۱۵ مربی اول لیست قرار نداره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105777" target="_blank">📅 10:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105776">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
⭕️
با اعلام سازمان‌لیگ ایران، فصل‌گذشته لیگ‌برتر بدون معرفی قهرمان به پایان رسیده و جامی به استقلال تعلق نمی‌گیرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/105776" target="_blank">📅 10:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105775">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e60f25ffc.mp4?token=Mnjg5ptb01Zbgqo_cLW62EjHkEaG-_QdHCE2cv2ES7oE6kCcm9RO042stD-JRYFw2dMX6mpWQ3j13zgIo6HRtnhgQh52CMhrhwJb2w4TlY1-6g4PjXm68AnckmczM6pwpGxFl-EbkGT8N1P7mlgHQXF93TPeqdEWhMc0I_YLr1jRFkYTtj25WO3w61YgggHKAKXtKwzmy8_2dvlaxO_aEm4luoz1mcpKepyvLYS4uELiUPq59yfkunHMdv0C-Xmn00yoy1k_jA7vB3B0ZB_LA5gsaCACO868XhjuKRLOol2_-7W4iycPhRwO9eGbRWvQxtEHI7CtT9uK1DESpLvZRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e60f25ffc.mp4?token=Mnjg5ptb01Zbgqo_cLW62EjHkEaG-_QdHCE2cv2ES7oE6kCcm9RO042stD-JRYFw2dMX6mpWQ3j13zgIo6HRtnhgQh52CMhrhwJb2w4TlY1-6g4PjXm68AnckmczM6pwpGxFl-EbkGT8N1P7mlgHQXF93TPeqdEWhMc0I_YLr1jRFkYTtj25WO3w61YgggHKAKXtKwzmy8_2dvlaxO_aEm4luoz1mcpKepyvLYS4uELiUPq59yfkunHMdv0C-Xmn00yoy1k_jA7vB3B0ZB_LA5gsaCACO868XhjuKRLOol2_-7W4iycPhRwO9eGbRWvQxtEHI7CtT9uK1DESpLvZRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😢
🇮🇷
هوادار روشن‌دل تراکتور خطاب به شجاع خلیل‌زاده: به قرآن خیلی جدی میگم راموس ناخن پاته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/105775" target="_blank">📅 10:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105774">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ab9d20b35.mp4?token=RcVVOHnscLNRf9u3x83n_qYaX04DNGyCwZHpDisqLLW9F6FQuYVRhYVy287Pz4-mA6X7obHllvInXq29SFrp4-HMlS0xUux_Y36dXRh6XaLx40FofJZps07lNHyzd1-GGpfk9AmNDhS4smgMnWvE8PHQRYDCOX0KpLRzYu1sRvguUmf62TdsEaFYlrTL2q_XGfNZUtwLsZ5NNMht7mZZEuzbkBgmOYl8pc-THLlr50TFNuOV-YToifX_zQpkL5gCeq_20uXTgySwaVZEh5JuqUO2WTDrOHOUf49pFVO8fpi6ZTFQQk9-xFHVakqlfwcLT8pS6tv6d0-DGCO9mbUWjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ab9d20b35.mp4?token=RcVVOHnscLNRf9u3x83n_qYaX04DNGyCwZHpDisqLLW9F6FQuYVRhYVy287Pz4-mA6X7obHllvInXq29SFrp4-HMlS0xUux_Y36dXRh6XaLx40FofJZps07lNHyzd1-GGpfk9AmNDhS4smgMnWvE8PHQRYDCOX0KpLRzYu1sRvguUmf62TdsEaFYlrTL2q_XGfNZUtwLsZ5NNMht7mZZEuzbkBgmOYl8pc-THLlr50TFNuOV-YToifX_zQpkL5gCeq_20uXTgySwaVZEh5JuqUO2WTDrOHOUf49pFVO8fpi6ZTFQQk9-xFHVakqlfwcLT8pS6tv6d0-DGCO9mbUWjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
کنایه تند رسول مجیدی به فحاشی خداداد عزیزی: والله اینطوریا هم نیست که همه جامعه فحاشی کنن
…
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/105774" target="_blank">📅 09:50 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105773">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfbdf6e4f5.mp4?token=MBJ_bi9NZmk49FZ-0ZzhUBrrOFxLRV57Yh_XesufWZvNsYiwcszRtvKDSQRQdsl8Ruas_R2a_H-imsdDz0HoUPid5HOrSlTzz73bzj4TJrer9-7km5oF9NXGUq1ntdxap1UuOXH4BGbI2f_sTDsvJncktkPMkaFsF-ihikEMtU4TGM83Ld3_OmQddE267gazNFLcPgZI3l8wM3PLzGSp4JrZJI5hvJKp5eNpCqQcyTYuFmU_ZeN1b1k4O_DtQiNeMd7h7D9Up7L_HS3GbJ-SBim_o3gH3FPkUjOMFEpNklFOP9CmOJKAvzsxFj1DPngdHBfOmf5iMOUHOuIuKEajzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfbdf6e4f5.mp4?token=MBJ_bi9NZmk49FZ-0ZzhUBrrOFxLRV57Yh_XesufWZvNsYiwcszRtvKDSQRQdsl8Ruas_R2a_H-imsdDz0HoUPid5HOrSlTzz73bzj4TJrer9-7km5oF9NXGUq1ntdxap1UuOXH4BGbI2f_sTDsvJncktkPMkaFsF-ihikEMtU4TGM83Ld3_OmQddE267gazNFLcPgZI3l8wM3PLzGSp4JrZJI5hvJKp5eNpCqQcyTYuFmU_ZeN1b1k4O_DtQiNeMd7h7D9Up7L_HS3GbJ-SBim_o3gH3FPkUjOMFEpNklFOP9CmOJKAvzsxFj1DPngdHBfOmf5iMOUHOuIuKEajzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرکت تماشایی دیشب رودری در بازی بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/105773" target="_blank">📅 09:23 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105772">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXDhxDVNy_9wpcI8cH1-S5UWaIIaq3PU-kHBln9XyjAWYneQILZzzdzv7xm8urPJXq6rre0Uf4kadXqYJLd8pJPBxTN1Y5Nx_bKbalfBCvytz4kC8_Cwpyg7HgHDY9jwgLHB96z7xC6IBRwoqnueLMX4EMveMAdCNQGYW88ViBnPC8cmqxiHuaWqSMuDPqkzgzhGyODtE8ywzzLKuy3Jqtnhyt8iY5Hdtsfch7W60JjYZPq6I3xh6iyXoNwQrIrCovg1KDNtggSV8POY9nbWXgZaPWgARPKa_1LT14tCpp5ZcjIJyV-bHQineFZc_mZjH8YgFlNsD5KjfYcskV_uug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/105772" target="_blank">📅 09:23 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105771">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf5650c1b3.mp4?token=BwV7vEPcqC8G_ZJ9soQEJIWRzkGpMNAWOvJ4ezrFJ70HpY13LQUpVscj7glj5gTr6H56NtZr5IhgeW5vVBRzRUsokPW6V2Xg-0-NtworDSnW4TgxppY_Q1RwDMPNYbtzKTg2njP0Ut635ldGBq5DLRYiWk4F0M-vR2USBOWJUw0eTNNZbyMW7VFrs5qGSH59AI8CN2COpBQzJWz8yF5vSbbKhy5o9SEzisYCgcFDh5f6Vb56H8AEuwkl-O84nr-dov5ekCdyYzf86S1WJn4PcYYkCbJhFWm1SUrTa2CoQL2w_PH2DnA5zZtpTiWvoMU37UwwQE36dhh70atAhmu89g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf5650c1b3.mp4?token=BwV7vEPcqC8G_ZJ9soQEJIWRzkGpMNAWOvJ4ezrFJ70HpY13LQUpVscj7glj5gTr6H56NtZr5IhgeW5vVBRzRUsokPW6V2Xg-0-NtworDSnW4TgxppY_Q1RwDMPNYbtzKTg2njP0Ut635ldGBq5DLRYiWk4F0M-vR2USBOWJUw0eTNNZbyMW7VFrs5qGSH59AI8CN2COpBQzJWz8yF5vSbbKhy5o9SEzisYCgcFDh5f6Vb56H8AEuwkl-O84nr-dov5ekCdyYzf86S1WJn4PcYYkCbJhFWm1SUrTa2CoQL2w_PH2DnA5zZtpTiWvoMU37UwwQE36dhh70atAhmu89g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هواداران آرسنال دیشب حسابی از خجالت مورگان راجرز بابت عقد قرارداد با چلسی بجای آرسنال دراومدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/105771" target="_blank">📅 09:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105770">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99e6028a7c.mp4?token=vNUdKWzf2R0-gupIX4ItfqESDfmkNDaGKQz4VmIaNnxI7OPW4wgafaM2yH_E2LzvGHj56yi3DRXDoTg1JkL2r-XHMpYFtY9B9U-tDk5UOB0s9opaGp-ZKUEyTXeuHOEcxO1p90zTu_-d2TOtnvQwZTSGkuK6hHrhQy5e121B6UU3O6ys1_ctN6NMH5IpQi7-LGKDbJdbx9hbKYkuDceAh9AT4Gc9fCH9tOa83lTLKUyLMHR71L3PxeY_odbO9bUigENa23ZaOv0_wvBhX5xFTnRZcKWjQAPMXUlHF9t5qLe90i-0qZ5lLkh_-sTIVN8T17zI6ZPuGaTym89HAz9ilQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99e6028a7c.mp4?token=vNUdKWzf2R0-gupIX4ItfqESDfmkNDaGKQz4VmIaNnxI7OPW4wgafaM2yH_E2LzvGHj56yi3DRXDoTg1JkL2r-XHMpYFtY9B9U-tDk5UOB0s9opaGp-ZKUEyTXeuHOEcxO1p90zTu_-d2TOtnvQwZTSGkuK6hHrhQy5e121B6UU3O6ys1_ctN6NMH5IpQi7-LGKDbJdbx9hbKYkuDceAh9AT4Gc9fCH9tOa83lTLKUyLMHR71L3PxeY_odbO9bUigENa23ZaOv0_wvBhX5xFTnRZcKWjQAPMXUlHF9t5qLe90i-0qZ5lLkh_-sTIVN8T17zI6ZPuGaTym89HAz9ilQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
حمله شدید وحید قلیچ به خداداد عزیزی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/105770" target="_blank">📅 08:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105767">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/105767" target="_blank">📅 00:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105766">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e26f7c6c2.mp4?token=RneZP1SUW5tITRIVVK36BkK-v2MaCyPn4XVRNHT3uvX_dnf7tycNrsCZLnRpAxFxQXnka3dQggEIGSglclFVxUVBVo07XBMAMvp1uKKm5G8UR2X6TPabwHiWlLmlFu4xPOIDSDXulh6z1ZGjSUx-zKzMcI9P5i7VU1ioZ1Fo-npy8L-aeecuiGvLflK2WYycSmWAROigUY_xtOAmA2uKwqkANOwtzqOCmOiyw8V7PKsQpqF1YW4y3ilLoNX2TXMM6g3inbmO2yC1cwlbWyYlIOuNFjtM5gbf7VGMX1608Qacrdbu1ncXGGfeGDE36w7wNnZNBRl-ZDntFecrttuETA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e26f7c6c2.mp4?token=RneZP1SUW5tITRIVVK36BkK-v2MaCyPn4XVRNHT3uvX_dnf7tycNrsCZLnRpAxFxQXnka3dQggEIGSglclFVxUVBVo07XBMAMvp1uKKm5G8UR2X6TPabwHiWlLmlFu4xPOIDSDXulh6z1ZGjSUx-zKzMcI9P5i7VU1ioZ1Fo-npy8L-aeecuiGvLflK2WYycSmWAROigUY_xtOAmA2uKwqkANOwtzqOCmOiyw8V7PKsQpqF1YW4y3ilLoNX2TXMM6g3inbmO2yC1cwlbWyYlIOuNFjtM5gbf7VGMX1608Qacrdbu1ncXGGfeGDE36w7wNnZNBRl-ZDntFecrttuETA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
🇮🇷
🇮🇷
سجده جیمی‌جامپ امشب نقش‌جهان با پرچم استقلال مقابل سیدحسین‌حسینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/105766" target="_blank">📅 00:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105765">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lroZVgwgFFmYB4v4ykz1bD7BmaUFxskgCSQv3r5bzz_H3A5y-y93ZCFCyBsbzFpTcmevEzi48sipJuVF5TnmbKt86vaZkO9rGVGNu6aclyITAL9Jx6dlYoE8NU6weO4OI8w_OyAlBL4xbueKcMxhBhFuLpqoeBBT3W_LXNzLEm7SYrQzpv4H9tD1JNvyNxCdABafOKDQNXH5T5q0arsiBvxls5Vt5iOJLWtXkcPVDMVNFowkxRizkaG1w8nyMdgKrNLIIRs5asbz9mv16F9sZKM8edPpY8is_nUGLmVifZCXpSzb24I2GjXL_aXWZ10OVkefuVuRiOvUBVu4VuidaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇮🇹
پایان‌بازی|
🇮🇹
میلان
😃
-
😃
یوونتوس
🇮🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/105765" target="_blank">📅 00:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105762">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
🇮🇷
🇮🇷
پیروز قربانی: من به توافقات قبلی کاری ندارم، خلیفه و گودرزی رو نیم فصل به استقلال نمی‌دم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/105762" target="_blank">📅 23:45 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105761">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02ce7af3d1.mp4?token=OL19vg19ETj1yMSe8az6SlNNpqQWlOY63cq-z5__8bX81OCBRhpmztAHFb-P2F6lwQSNKcuD4Gwq4vrQjE7roO1Q8JTtU3C7JwcSPHlYhUeRhjV4Yi9ARAIgtHFgnnhUKR1_C5PW_fWWlfLzNlkaWcZ38AWBGqERb4IrOVz3UVGu_Pr6U4Te5CcdLR8u3vDOngRQuw3UXJ_GZElZLL1LhfbhUK5DTcMXs971ZfSC8u5A-_2rJEVExKEZCTDTSAHE7wD6-oh4FGTSztbL7JVwyuW_CnbyKRiULlWNCFU2ik_PqCLirliGiUX6RCflanQE3iTMcfsmL1yz1lsD5uA4KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02ce7af3d1.mp4?token=OL19vg19ETj1yMSe8az6SlNNpqQWlOY63cq-z5__8bX81OCBRhpmztAHFb-P2F6lwQSNKcuD4Gwq4vrQjE7roO1Q8JTtU3C7JwcSPHlYhUeRhjV4Yi9ARAIgtHFgnnhUKR1_C5PW_fWWlfLzNlkaWcZ38AWBGqERb4IrOVz3UVGu_Pr6U4Te5CcdLR8u3vDOngRQuw3UXJ_GZElZLL1LhfbhUK5DTcMXs971ZfSC8u5A-_2rJEVExKEZCTDTSAHE7wD6-oh4FGTSztbL7JVwyuW_CnbyKRiULlWNCFU2ik_PqCLirliGiUX6RCflanQE3iTMcfsmL1yz1lsD5uA4KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
واکنش عارف حاجی‌عیدی به جنجال در بازی با استقلال: والا یه ۱۰ نفر بهم فوش ناموسی دادن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/105761" target="_blank">📅 23:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105760">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1098753ac8.mp4?token=u8YjFOFFPOaRV_i6nF6-DxzGg_R57jljjv9ckPWobVk6CyukBmu29GELscg4dE-0_Yh2HbKP7VGR2lntk2439gM2tAvUEIV5k7hIFElxyWXtvRO_IQIGzGChjwF7urmIw0YH_50ROKarAgtOpGkdS-02t9BJgb4zTm6n_4iD-CIgJ0jN0hjRarQXf4MigmTho8Pey8jJ2PAei5NrI7VpGAY3-i9OVEr1TAEmozx4BbKGTk5IbKOsZ2ajEYCEpsTvAuZwu-LFRltzFSMhTzzrEmcF0TQzMglL60uhj6wjO8gI6PbAwT3Imylfw2ZrcFfxBe2QGRDTKgNZRvfT0ClXwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1098753ac8.mp4?token=u8YjFOFFPOaRV_i6nF6-DxzGg_R57jljjv9ckPWobVk6CyukBmu29GELscg4dE-0_Yh2HbKP7VGR2lntk2439gM2tAvUEIV5k7hIFElxyWXtvRO_IQIGzGChjwF7urmIw0YH_50ROKarAgtOpGkdS-02t9BJgb4zTm6n_4iD-CIgJ0jN0hjRarQXf4MigmTho8Pey8jJ2PAei5NrI7VpGAY3-i9OVEr1TAEmozx4BbKGTk5IbKOsZ2ajEYCEpsTvAuZwu-LFRltzFSMhTzzrEmcF0TQzMglL60uhj6wjO8gI6PbAwT3Imylfw2ZrcFfxBe2QGRDTKgNZRvfT0ClXwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
واکنش پیروز قربانی به پخش آهنگ "نصرالله معین" در نشست خبری بعد از بازی با استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/105760" target="_blank">📅 23:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105759">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‼️
🚨
🇮🇷
🇮🇷
محمد خلیفه: تفاهم‌نامه بین استقلال و آلومینیوم خیلی صددرصد نیست چون ممکن است استقلال مرا نخواهد یا یکسری اتفاقات بیفتد. حتی اگر قرار شد بیرانوند به استقلال بیاید، با او رقابت می‌کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/105759" target="_blank">📅 22:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105758">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1b9ee8002.mp4?token=a3btKHILVjzk1T3teXufjE7paTyFSxPl5gBux0y67iRl9w4lMtow7Wchve0ENb9YbkSU_DA9_FMXpL5pmrtMgD_Hfb3DRGIbkAWVIZwzc3fp4_zSxA9hIMHN5T1F1y1bZCxvBt2egSskuKpQaz-Pmo6aB97nhruxrPmq72dJ0fGbXL5krC61uCwerGXEFyVPH34vsf_miNt4q36WZxoSQzEx0XKutLuAWQrSR-4-FmQdFvAo8LfqfOOZI3r4hRsOxITROJGNQesTKaV2LbzPFd7ZktTW0hg5JFag1KZBZELPRolqQIF00tTXHU8JlNDznTUFYdci1-10CpQc56DTwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1b9ee8002.mp4?token=a3btKHILVjzk1T3teXufjE7paTyFSxPl5gBux0y67iRl9w4lMtow7Wchve0ENb9YbkSU_DA9_FMXpL5pmrtMgD_Hfb3DRGIbkAWVIZwzc3fp4_zSxA9hIMHN5T1F1y1bZCxvBt2egSskuKpQaz-Pmo6aB97nhruxrPmq72dJ0fGbXL5krC61uCwerGXEFyVPH34vsf_miNt4q36WZxoSQzEx0XKutLuAWQrSR-4-FmQdFvAo8LfqfOOZI3r4hRsOxITROJGNQesTKaV2LbzPFd7ZktTW0hg5JFag1KZBZELPRolqQIF00tTXHU8JlNDznTUFYdci1-10CpQc56DTwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
🇮🇷
🇮🇷
پیروز قربانی: من به توافقات قبلی کاری ندارم، خلیفه و گودرزی رو نیم فصل به استقلال نمی‌دم
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/105758" target="_blank">📅 21:57 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105757">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k1Gcn5AOrVdBaDU6OuEmHkUu0oAwtOzjqntUS7281xi6JlJiScEOfXKMMt38uxXOgghOlZgY_-jK4MtlUnYVfrEYjcEj2fsMWCdJ1zIyfTuTOlRnBIPuKdBMLbjk24FwgSwQIqmkyPJYJArQ-Y0657BInKndojJheDnQh2emhNhwT1u2mjXmew-muDZraCt-eg9DKaKaPlzZltsNZRTbjecQf5Sv0B8cdFmYLh2u7SjyzuYRCtVq5O5LyhkylP-7U62rzZuzCHkGfHGCEMXNSKenRoLmofpsUCvvfOxYjtx3EcKhtjcHKvtTev83O_l8Xfwc5qXNw2q5Uq-l3V_jkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فکت
؛ آرسنال در ده بازی متوالی لیگ‌برتر مقابل چلسی شکست‌ناپذیر بوده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/105757" target="_blank">📅 21:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105756">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">‼️
🚨
💙
بیزاتی مربی استقلال: ما هم از نتیجه خوشحال نیستیم. قطعا مشکل گلزنی را حل می‌کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/105756" target="_blank">📅 21:26 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105754">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09d4a38935.mp4?token=VuEwBZg0oVgnPf1XazJfvdbPJeYE2UmRzp1VIt0zBmWghGk8vCrkowOfc0x0QvApar5OVVLw5ocl-Ec1DfJ2zI5a24LlsCajnEcJbEQ62h3Xv386tBcHor4YvX1B8jiSgPfE1sNKR8W8jaxCWs_SSLjLur2MhC_K1O44SoN6moIZ8PsD_M683CzGGXGVmo9nhim3LFIQJ3ldR2FMGgI3YkaDWKf-AbPkKBl-Lm31O_fFMUt70XhQ5ds1UizZoXm9bkwzKcrTFJcCoTwVuT-onDoCNYmNmkgUxQ4yZ1Nylfpf2ORKUsK0Y3JUQMs9MAOCR4Ggf_uGEalmMyL6ShCPdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09d4a38935.mp4?token=VuEwBZg0oVgnPf1XazJfvdbPJeYE2UmRzp1VIt0zBmWghGk8vCrkowOfc0x0QvApar5OVVLw5ocl-Ec1DfJ2zI5a24LlsCajnEcJbEQ62h3Xv386tBcHor4YvX1B8jiSgPfE1sNKR8W8jaxCWs_SSLjLur2MhC_K1O44SoN6moIZ8PsD_M683CzGGXGVmo9nhim3LFIQJ3ldR2FMGgI3YkaDWKf-AbPkKBl-Lm31O_fFMUt70XhQ5ds1UizZoXm9bkwzKcrTFJcCoTwVuT-onDoCNYmNmkgUxQ4yZ1Nylfpf2ORKUsK0Y3JUQMs9MAOCR4Ggf_uGEalmMyL6ShCPdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
⭕️
نرخ سوم بنزین به مبلغ 10 هزار تومان تغییر کرد؛ سهمیه اول و دوم بدون تغییر
سخنگوی دولت جمهوری اسلامی: نرخ کارت جایگاه سوخت از بامداد ۱۷ شهریور به ۱۰ هزار تومان افزایش خواهد یافت.
در جلسات کارشناسی اعداد متفاوتی گفته می‌شد اما چون رئیس‌جمهور به مردم قول داده بود همان ۱۰ هزار تومان تعیین شد.
۶۰ لیتر بنزین ۱۵۰۰ تومان و ۵۰ لیتر بنزین ۳۰۰۰ تومان همچنان بدون تغییر ماند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/105754" target="_blank">📅 21:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105753">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPlVy_m2ccHFA6x7h2r18Wa1JfpTeBIwyhHlkBqdMNAhoLx9KRot4Oxpmz4bTqGAa9YpcOhRISoqGnup0lgivHo55EbRfOL-dLlpFVwwi_jIxIBR4Ff7yY-f9x9ahtvS8zOqGskCUkg_aU3_a6_dfEROpzvKg0R9Q7HsLOESoLlmiUl55wREjpeGW_Mx7oXT7wcFhFKvgzWw4JpeNpkijtvTHok0e7gvu7HvZfevPDGCDSWTk8YjhKwbJCJ6JFH3hOr5Iux579xexvroMxF5n6ogsmP9yMhez1okw8c_rmeWgNHPnsg_U9fc_bHeT3U4je4H5rOuVI7kTQQORuBfZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
هفته‌ششم‌لیگ‌برتر فوتبال؛ به یاد دوران مساوی‌های متوالی با فرهاد مجیدی؛ استقلال و سهراب در آستانه به صدا در آمدن زنگ خطر قرار گرفتند!
🇮🇷
استقلال
😏
-
😏
آلومینیوم
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/105753" target="_blank">📅 20:57 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105752">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AuETsWoO2aWsMAAGY_UkIFdqJ6U2UQf5bXhfqdVr1MlFdspiEndL6PmloWDpd0geMUlOPbGkoP1JkvTQ8Q1sysK4avwpfXYg6YhIXM8GtBhZzadFjr_DRmgR1qerNY00ukC5Gi9gRg_d0uoSLaWZ3Bm9uE25l0D-A__wAqUaAPS7VmSnRKS3qRYQS2yfF0I9RaDyucT3QW4cv3TymfoSJSwhkA8HvwV0jp7qg6tPMMoU_hl6pg5vzYItI0-uqmJwE0tgbOkhlRvh-UuEDWEvN29hKJbbB6JXzyX7FZscuUsJdqsqMMDuZiHVqyenwMlyd_nb5DHqOJClDPVEJYuPHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
هفته‌ششم‌لیگ‌برتر فوتبال؛ به یاد دوران مساوی‌های متوالی با فرهاد مجیدی؛ استقلال و سهراب در آستانه به صدا در آمدن زنگ خطر قرار گرفتند!
🇮🇷
استقلال
😏
-
😏
آلومینیوم
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/105752" target="_blank">📅 20:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105751">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">مرحوم ماشاریپوف برای استقلال به زمین اومد</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/105751" target="_blank">📅 20:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105750">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">مرحوم ماشاریپوف برای استقلال به زمین اومد</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/105750" target="_blank">📅 20:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105749">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c5e1fcdc1.mp4?token=C7K7r3Lkx41MEc27_WgaeEuOkoEFZCtpd1Yiq9tN6wq4VlJdX0bX-S0CVDa36vRZRu9Ttad3RzmngCD6sceg_ZqA7w10Cf439jU05Vobp83q1H-jVU9tQZvT1L1C2N4w1UPrlEdan8elUBu4zAuNtSlwC6R03Q76uVI3dVVvFn2OU3DbEkQOgqOUzzMfJ7CjwXHhzqBWf2XiPGoBLD21aOmPVMbzRkmVgh5Uoxp4mQTzDGLe7q_dFwjO635ZpUKWrxXX8-S1ZdfjWHguVRK0MKIKPo-pfFIM57FPLrkuBZFL6Zr5qakgqk6sASJJ84Tco1XTv9Axe1JKjVyrlkGikA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c5e1fcdc1.mp4?token=C7K7r3Lkx41MEc27_WgaeEuOkoEFZCtpd1Yiq9tN6wq4VlJdX0bX-S0CVDa36vRZRu9Ttad3RzmngCD6sceg_ZqA7w10Cf439jU05Vobp83q1H-jVU9tQZvT1L1C2N4w1UPrlEdan8elUBu4zAuNtSlwC6R03Q76uVI3dVVvFn2OU3DbEkQOgqOUzzMfJ7CjwXHhzqBWf2XiPGoBLD21aOmPVMbzRkmVgh5Uoxp4mQTzDGLe7q_dFwjO635ZpUKWrxXX8-S1ZdfjWHguVRK0MKIKPo-pfFIM57FPLrkuBZFL6Zr5qakgqk6sASJJ84Tco1XTv9Axe1JKjVyrlkGikA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😆
😆
گزارشگر اراک: محمد خلیفه ما رو یاد جوانی‌های مانوئل نویر میندازه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/105749" target="_blank">📅 20:27 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105748">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d287258445.mp4?token=l2vxhMUyxwI04dAkRnGbwQPPvVST-BemhWmwZb2tRqDYtQ0-zz8mj7IJy6XfKg59mMkY8fOZfLz8_fBBKTptl0xkvQrCtKiQlmR_7w_tObLzYhglJ_myi1G0TOtwfELeLSgYhk0YWxcuhDXjfeSAoQKZ12pySZjfBMQIDwjmtZPE6bw2K5yeZc2ruICWbtJ2Ida8U7u7zISGbb4kV16lolBr9VkT0YNt3G5fLRVioeHPQ3kqaAOuhRUoppICMdev7841BRyBqhFbyM-g6bCA8YHZ51ZasnlVRdIgSp1ihpg6iKKnz5Q-OjaEdIvLmPq2bG8mN5EmdGWR12HIw-Liqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d287258445.mp4?token=l2vxhMUyxwI04dAkRnGbwQPPvVST-BemhWmwZb2tRqDYtQ0-zz8mj7IJy6XfKg59mMkY8fOZfLz8_fBBKTptl0xkvQrCtKiQlmR_7w_tObLzYhglJ_myi1G0TOtwfELeLSgYhk0YWxcuhDXjfeSAoQKZ12pySZjfBMQIDwjmtZPE6bw2K5yeZc2ruICWbtJ2Ida8U7u7zISGbb4kV16lolBr9VkT0YNt3G5fLRVioeHPQ3kqaAOuhRUoppICMdev7841BRyBqhFbyM-g6bCA8YHZ51ZasnlVRdIgSp1ihpg6iKKnz5Q-OjaEdIvLmPq2bG8mN5EmdGWR12HIw-Liqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
استقلال از کوووووون آورد
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/105748" target="_blank">📅 20:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105747">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">استقلال داشت سوپرگل میخورد
😐
😐
😐</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/105747" target="_blank">📅 20:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105746">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/105746" target="_blank">📅 20:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105745">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da0209e41e.mp4?token=UUXoosRcO6n5DIe38A4EqlzFPPzZ430yNwVDswNR00FefcXHtK4RzAjyUvSQU4J3eRcOXpZQpodoZ3f1-w5BDmL9HN0IThS6_GyIc75JMDwu9uVsmcetRm5nY3nM-vi8HkkwH3f40NoGrFVuFNpwaOOdbQxHdI5LewY4ppMbIBYtXpTKFCpp8Z35EYfc2jCaMfDOno10yxCHpyLRbVe2ud1MvgC-5Fnj5qlYdYdlPTFSo6pYrYlEGd4bDWxJyqf6r015mOSWBS877L0PWxLYs56UbwQi8SZIXs_vympoGhyQZnMd_JUUHpffZa5fxHD7l8B75ydkFwWX_lUkJds0Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da0209e41e.mp4?token=UUXoosRcO6n5DIe38A4EqlzFPPzZ430yNwVDswNR00FefcXHtK4RzAjyUvSQU4J3eRcOXpZQpodoZ3f1-w5BDmL9HN0IThS6_GyIc75JMDwu9uVsmcetRm5nY3nM-vi8HkkwH3f40NoGrFVuFNpwaOOdbQxHdI5LewY4ppMbIBYtXpTKFCpp8Z35EYfc2jCaMfDOno10yxCHpyLRbVe2ud1MvgC-5Fnj5qlYdYdlPTFSo6pYrYlEGd4bDWxJyqf6r015mOSWBS877L0PWxLYs56UbwQi8SZIXs_vympoGhyQZnMd_JUUHpffZa5fxHD7l8B75ydkFwWX_lUkJds0Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
گل‌اول سپاهان به استقلال خوزستان توسط لیموچی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/105745" target="_blank">📅 20:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105743">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اودگارد گل دوم آرسنال رو زدددددد</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/105743" target="_blank">📅 20:14 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105742">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WB2MhIsIJlPg5aFRoKZ2KOF3u6gw6XgxjhWo8gUufgdHOwFUUSg1ilp_pwS6wvIfTRoChh5EuToXH7HNg5yXkylxKFwVGmW7zXY0RI0KoxO5-USUXUXBsupD921ksjd81u9m7ZscvS182Zbfb6gq74atnqjATpc3dA1usRqMRxz_UQNeg1AIJ8Pu_Wv9EYNF2eCBOVQnfsUDf9ApeZSn7a4TQfONTXcEUmpNHVIUmxk3gkH_YpuZXu8K4aRLJBwhxJfsxwnNhA-ekdhhD-Ck-vPmukZ9lbtDaIj5uiUvEEmOkk92NRzpYqK4ne4SLqUwjDCiusWiksoFMrymmIBIZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📊
🌟
مربیانی که بیشترین تعداد پیروزی را در بارسلونا کسب کرده‌اند، پس از انجام 80 بازی در لیگ:
🥇
1- فلیک (63)
🥈
2- انریکه (62)
🥉
3- گواردیولا (61)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/105742" target="_blank">📅 20:02 · 15 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
