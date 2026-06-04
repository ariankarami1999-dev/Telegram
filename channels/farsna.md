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
<img src="https://cdn4.telesco.pe/file/UvZolvtp92K9s7Snp8sAbm3VdXwsHK1X8g861xxNnFrJKO5zB2w1FBOMyaOcuBENmxOck0gX8e-2mMmTyITPd3vhfk6tGDc6a933qq6u6t9PzTysfWHUj6UV3vZuMxC4OIOAhNMvbMU7mEhnDikGgIZEs34JSLiwMRqmklRp9k0ENEdSZD6gjkRQPCuiYStqPaZSc7EiP9W3o6a5vpZFdca_2XrPQokkvYVE51QT5rIEB_pclemtYkfv2YAItY8Hw_wv3Sj4z5sTkoEFTbJ05EoNZ19pctva_UKvVtASovS7hxT-kQUuAXcn5FWU-luEB_MKmKfFnN8jLC1llljrIQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 09:59:18</div>
<hr>

<div class="tg-post" id="msg-439781">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1sGRvxjjoIXHzW_EiYMkssPjSBW61_LxzHA3v2tAv59QHPidwzsW1UF5YTcTwWmsC4OVxJDLvdGnFL9iGi9aEMku_gYN0c0RYYIcT9IgmLSit89dcBqlMgYRuv5O-sA1aYZpLkA8F8i7zUFgOK3oTlZV_0hhh1NQrPATM1H79rumKygMNSRXSaHGErpweyrLgJl4ufAxoFXKx1YeJtHnkDcVONlMkX18lqhrqZpjRRqqop4hUxfNzMiJgEe20KmyZAXyyfKHPBfjPFBbFbo9FK7jMpCeqaYQne3kFmd3sq0xuwM-FzrjCQbhWKRTg1-ZHNJDkJp8eN0ZqDbBia6UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمدی اولین فرنگی‌کار طلایی ایران در مغولستان
شد
🔹
پیام احمدی فرنگی‌کار ۵۵ کیلوگرم کشورمان در رقابت‌های رنکینگ جهانی مغولستان صاحب مدال طلا شد.
🔸
دانیال سهرابی و محمدجواد رضایی نیز در ۷۲ کیلوگرم راهی فینال شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/farsna/439781" target="_blank">📅 09:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439780">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🎥
آخرین
حضور رهبر شهید انقلاب در مراسم سالگرد ارتحال امام خمینی(ره)
@Farsna</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/farsna/439780" target="_blank">📅 09:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439779">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f47cc1de4a.mp4?token=bKil7-lxbs86qwzDi2oxwPnO-d04OZsD0G0opJmxOfecSLb9NV3vFuecvG6s2GAkG1-HjIYIL-OmvE-vQ44Qo4EJ_OF3sTSdW6ogE0pBhI1czt3Znli6F4AW33J4QC3l76sSotITWKQAhOc6xkaM8GMWQf9PqCBgUCsufClQDwAJPXgUeZDmYh4ymB8OCiwnt8OwW8OrJhL3XwtK-nxKO30zcG-mBHRM3f58YjAMTwxYOs9vKNqugnFxDQaU5Xu30wSpyuwkaL8CQCe3gxUZcrzizsRUyas7tzfUkKkHItvWiRiFar6XiMTq7C5buX11iaKpJuGvCiA7yTfcdV98-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f47cc1de4a.mp4?token=bKil7-lxbs86qwzDi2oxwPnO-d04OZsD0G0opJmxOfecSLb9NV3vFuecvG6s2GAkG1-HjIYIL-OmvE-vQ44Qo4EJ_OF3sTSdW6ogE0pBhI1czt3Znli6F4AW33J4QC3l76sSotITWKQAhOc6xkaM8GMWQf9PqCBgUCsufClQDwAJPXgUeZDmYh4ymB8OCiwnt8OwW8OrJhL3XwtK-nxKO30zcG-mBHRM3f58YjAMTwxYOs9vKNqugnFxDQaU5Xu30wSpyuwkaL8CQCe3gxUZcrzizsRUyas7tzfUkKkHItvWiRiFar6XiMTq7C5buX11iaKpJuGvCiA7yTfcdV98-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز مراسم سی‌وهفتمین سالگرد ارتحال امام خمینی(ره)
@Farsna</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/farsna/439779" target="_blank">📅 09:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439774">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ey1XV78akM96460uSMEt5qPWZcfxK89RWd56gp004PpdDvlwTEZOiLzPb4OtRvX48GD2t-EN7VeU0-SjH2Z-ir-74VOvJxba34WkEKgjPnU9hA0tLVnghDQ7hesz0QF215p4ycIW3-MPHgMDkN3u4Dz11zAB7x7Pe7MPyc_BrB-FEhtiXW_n6yofaZQSx2ZyQIUOjHNWj1Qa3DPYRAyCtYREf8e2VBA_XAAJJpRx8JFSn09edBEPMenJvAQwMhvoPawDfT-tpuZ48tEQK0rkGkdDR2ECy-iBG1X4dKED2wv2Tf6W1mHyoAVMmSikPbBmINKEpG5J0znEUlZh1J6kGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X-32MTHlrX9HD1Pp9aSI6EWiM6Ffe58gdZ5iYNTtq7JREAxsrjjIl6BGy16cWOmQq8xuUX_qlFJloQqSjq8H6ffRKV8kIfKXsvjGnn6UJ9rHY0j4JY30EflPbyAdXAHbpcxFcRAcgyUJWawwTvRafQ3sRZSwKgB8szEmHTh3aH37DgmIgupXPSf5EKZs81mMX58L08zbk8axr54AmYJRQbF_DHGZC3my66z3lELTB2_bF6KDV_QQBun77KbCXsn5KNagRoUgcRWUq48Bt_sN8wuj-gMM8fnSYdNEYwOBuq1ij3KLLxObMcB-eFpZgwWV8NwrZsvlXw1v7fJ5xFUPjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r2XE8ZpUHscqM0wHHhyflO0F_g-m4JX5Q-5UsGK_-ko6E2wiABWLwHJUiZPGKkH9NLB2SyADRVWE21NEV_uB_Edfr-ObyRVpYBPyKcxzI7BKu5GGCp6NUmZPgVkMdzuoPQHxt5BBX98zxSRhcM6b8zZzrdm2kQ4BbCSD2B4I1AqNtJR4jECXl3ZQplfI2G7V_Ourrs0G19RMFuaBmOtAVK-sDsGTYXhRbwUEejFnmsDdaNYlsWS47d3MlGNAD7L2EXp5eJ3d0w_at099YOvjUtb8yBL9fC-K_wLS1kFF8b5i0HPB8lkiICYy8z4yHwEm-rsYyfsTFC5WqbdgxkdLBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/egsZwhRWpOhpKQZqw0UbqfTkpvdmVm7tVDYa8RfhoMBKEZqXP6ze8ulbd6zhVqV_QCo55fDnCsFpQ-jx45MnTTgh8mST5nBinzRRYaSeepZwY2ykmklbJBy1qKVX3rEUjHxXZe58rY4vB2USYILUi57CImxi7QzzOkjQDv1ykaVkDLpPC7EE_wV8RS3IOuB2IL-0gpLHWmlc-QHs7o7Sdf1qmm32Mn-sSZ_t2-Bvi1G2Bz0uHE4TlJvwEnMahIYq6ieUq-Fd0Yjk00O15j9eMwqmC0VGaOZ1qIt7U1OA8PUzS4W81gdejJS9V546Na6_jjLCQ9MYnJOoCZeJx0aC_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XsNs3emvq-ka8oZHDDouolF_XjXsDakK5WH2qBVE7I_MznE0SnfuR4Ii1zSXRIDUOjXUnTMRceQulv3zRQZQtgHQAUlsIkwxnSC2sSMsAzYcC7IWuJx-vJM3FugSpJy00f20PUpNddRLHUNkyxug2usUZfC-jj5woj5HFukalZhO7o3xMhAdhL42V5-EHCkmyuChwui3OFoihO6rTnd2StOyY3WTBBr8dt30Xawu4ynfvhOgnbyM6nzOyhoK4Bv-72FzPKttuiiGrCZ1i3Lv-uU_3wRqDLj_pCrDgd84bY3T5p5Eo22AtbeM5AJmmoQ_i3LO13EX3OyJizNkPPUymQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مهمانی خیابانی شب عید غدیر در شهرکرد
عکس:
رضا کمالی دهکردی
@Farsna</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/farsna/439774" target="_blank">📅 08:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439773">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e2c8a0e05.mp4?token=EKIWKmiLBlhefZbhzc4Qk6fN7oGceHLPTCj3vImHXCTMx0kJpDkki-cmZbp2ScRpXlqHQ3yy81qF8eYUE4u-Xnf1ZY4K48mKynPWZKS2uRSLrJxPZmMt3qX92XFWchDPMzyrg_7EnGXd56Pf66WtNKnE0Yk3evC8Kxo_2eXiojTXtv1Ri-6OkYpF_9bIYPlYRQwXPCuN6aCwrQxAGEhGLpIaJG6Y60jWgbsxikGxnE2v2avpuJOc-KzfullFfjbN2sU7KA7i-DQzc0vz-rNg_VMfS93pAIAhgdWXckIZOtmQ5fD05yfM4mspFcID0o-Ht7CWgDbZija1xxv3Bo59vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e2c8a0e05.mp4?token=EKIWKmiLBlhefZbhzc4Qk6fN7oGceHLPTCj3vImHXCTMx0kJpDkki-cmZbp2ScRpXlqHQ3yy81qF8eYUE4u-Xnf1ZY4K48mKynPWZKS2uRSLrJxPZmMt3qX92XFWchDPMzyrg_7EnGXd56Pf66WtNKnE0Yk3evC8Kxo_2eXiojTXtv1Ri-6OkYpF_9bIYPlYRQwXPCuN6aCwrQxAGEhGLpIaJG6Y60jWgbsxikGxnE2v2avpuJOc-KzfullFfjbN2sU7KA7i-DQzc0vz-rNg_VMfS93pAIAhgdWXckIZOtmQ5fD05yfM4mspFcID0o-Ht7CWgDbZija1xxv3Bo59vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر ماهواره‌ای با وضوح بالاتر از خسارات وارده به یکی از پناهگاه‌های پهپاد/هواگرد در پایگاه آمریکایی علی‌السالم کویت در پی حملات موشکی ایران
@Farsna</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/farsna/439773" target="_blank">📅 08:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439772">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">بخشودگی کامل جریمۀ حق بیمه برای وسایل فاقد بیمۀ شخص‌ثالث
🔹
بیمۀ مرکزی: همۀ دارندگان وسایل‌نقلیۀ موتوری زمینی و ریلی فاقد بیمه‌نامۀ شخص ثالث، می‌توانند از روز شنبه ۱۶ خرداد تا پایان ۳۰ خرداد نسبت به خرید بیمه‌نامه اقدام کرده و از بخشودگی ۱۰۰ درصدی جریمۀ حق بیمه بهره‌مند شوند.
@Farsna</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/farsna/439772" target="_blank">📅 08:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439771">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0322159ad.mp4?token=JX0qumBEVKuiNB4Su0ACIQ_y0OqnObpd0nk1bQCv_S4U88Qyz1e4L7GdKrbUuPNdUH-X0ztOPzvQ0jPnpIWcZYzohQ77_RHsZfocZcfKHUHXkQyb7aHRPR4Eh-6q-_sfiEai8wQkZBqg2kuMLNQuxI2rL825Y0zJY5hS1eQYmVumdBaVxWPVBfx-u_8MWore7tHih0wVHiqaHCu2icao7lYXW-WVRyMr9HAKiLYx56qsqX06NkNx21HfpDCn7gQSNE6LtgACMWEM4IUT8F7g2V8WeiV013zma74-uFM4fQkikT6djHSVnwasGscXHoNRwDOKI-YzK9rL0Qr57YsbWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0322159ad.mp4?token=JX0qumBEVKuiNB4Su0ACIQ_y0OqnObpd0nk1bQCv_S4U88Qyz1e4L7GdKrbUuPNdUH-X0ztOPzvQ0jPnpIWcZYzohQ77_RHsZfocZcfKHUHXkQyb7aHRPR4Eh-6q-_sfiEai8wQkZBqg2kuMLNQuxI2rL825Y0zJY5hS1eQYmVumdBaVxWPVBfx-u_8MWore7tHih0wVHiqaHCu2icao7lYXW-WVRyMr9HAKiLYx56qsqX06NkNx21HfpDCn7gQSNE6LtgACMWEM4IUT8F7g2V8WeiV013zma74-uFM4fQkikT6djHSVnwasGscXHoNRwDOKI-YzK9rL0Qr57YsbWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دره‌ای شگفت‌انگیز در قلب زاگرس
🔹
تنگۀ سرسبز شیرز، یکی از چشم‌نوازترین جاذبه‌های طبیعی غرب کشور، در ۵۵ کیلومتری کوهدشت و در محل تلاقی استان‌های لرستان، ایلام و کرمانشاه قرار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/farsna/439771" target="_blank">📅 08:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439770">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/022cea969d.mp4?token=qhfVK0LapYHwcWeLbQFb2V2fFAMBRQ0UTIyAyRHyFF1tbK9p3MC8L5KjzpyyW3xsPbWEvYqZWo-fmPcEia60M4renb_ffiW51HPhRHHeSfJqsAMciwTadCp9GP5a02U0ceT_aXOhM90mRI42h0n_iHJbm1sNwjH8hcxR8U9-2Feyi5Y4jNMeR7ind0IKtDWj1kE7uYxyYF1Cw9JIiEhXviNnYo4oSMd30KBp30HtZ41VExI4VBXRmN5l6iV4ddPVgpl8QerHxjeoOzXlVq6qR2BYDb7RF7f2-9w5nlF529P8dlFtx96EkGu0DEOvVr-2BIpdQIDI7iVKtXrCjv7IDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/022cea969d.mp4?token=qhfVK0LapYHwcWeLbQFb2V2fFAMBRQ0UTIyAyRHyFF1tbK9p3MC8L5KjzpyyW3xsPbWEvYqZWo-fmPcEia60M4renb_ffiW51HPhRHHeSfJqsAMciwTadCp9GP5a02U0ceT_aXOhM90mRI42h0n_iHJbm1sNwjH8hcxR8U9-2Feyi5Y4jNMeR7ind0IKtDWj1kE7uYxyYF1Cw9JIiEhXviNnYo4oSMd30KBp30HtZ41VExI4VBXRmN5l6iV4ddPVgpl8QerHxjeoOzXlVq6qR2BYDb7RF7f2-9w5nlF529P8dlFtx96EkGu0DEOvVr-2BIpdQIDI7iVKtXrCjv7IDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جایگاه خالی امام شهید در سی‌وهفتمین سالگرد ارتحال امام(ره)
🔹
صندلی خالی مزین به عکس قائد شهید امت در جایگاه سخنران حرم امام خمینی(ره) حال و هوای دیگری به شبستان حرم داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/farsna/439770" target="_blank">📅 07:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439769">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🎥
فیلمی دیگر از شنیده شدن صدای انفجار در بوستون و رود آیلند آمریکا
🔹
منابع غیررسمی از احتمال برخورد شهاب سنگ به این منطقه خبر داده‌اند.  @FarsNewsInt</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/farsna/439769" target="_blank">📅 06:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439763">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bGXiM0gbERUpI0lk4akLRWNNrQ-SgcGwIDw9dzG4n0xTUitS3_D6_5xlJLQM_tf6AlQIBx-sGRsPOfpvXXu0PUjyN7tsCTk4AcTyh0Wyi8Orz66ty5UUZH7CHHykKK3k-RT_3ld0u9bM8_rFny-rvv0s5zj8bmGkwXjrHBdfjYdjyCK3xKhMjDhvMwXA49dXI0TRlGStq4rjQQ92wenbc1JmZrbrZ8JDmN4YvIBO-hSR4aF22Pzk_-B5H3w-wNNRXXod1D66pkoxvfWwUGZ3fyzzfEVLygtPRXd4dQ6kbx79ycou34rdP9tkIxIx4QbDAqpVfgUSNeS7Pi_yPutg5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vmFiYoV1OcnXZuokYe81S_d6JSNWfviGatI1UfJ-Mq4xSZ-XTOui3Ue39SMWGSSgmlMIyMqSz1-gfXkvOvfR83XDIa_-ZEW93JFcBjPZgjVBGd-QtvCa5WcXM7bQOtlCNAWOZHznJHrwgHnJg1YPfHIGKomV5BAm-iBdtKKitIEQW7F6D46uPsp6jVkY9ccXlYIiQSILXfMDqauCH3PA5peGshL3S6e6SipZm0LEbpC3rmrnTgJOETX5YnJ0swvfnpWNfrxK8lsCykV1tGl7EtqgneeHi0prOuOWMld2YDtjxNs8QrmCwB_9-4RvpAUWc33JsmPY_UHI6arTqyHFMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LYaxB4tgJ9N7SZqOEx79qOEoIHJWHazFnB8GDFDZomcEaUPrbKjXlmW-SNFBK3Y9RWa-LJMgHzlZkB5Xawx4v_FqfrQE7t3ukRNikpajdgrW7sJa4Bzza5776h3OpkN2ZX-iPJ6XXtQOdfVeq1AVw6oi2-PpBduvu40wlyRDfkAuJU1uqPhcZPht6q5JDBnmPNLNvkXc-9wVKiRgM3nlryV06HaebCJ8J9xGYHhK4kqklxNFRvPqcWsAmJvd-fc-tscEZlpQLYVzVa4HPMkjqM7mmqZW_d1FkITEghfMxK7aLJIzKPJDyPGDvEOHik1zQB7bJj1vm048sSvBxYogcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tOztHA4a1n5sPtH2N-9ESgUXxscd3JqpWLMH5fPsXdyVSpnCty3YGq0P5DJR5QwXDtW0z5kBe_SiBPmonAddn2wISi8TX8N12WzqhGOescJry8Ew74arnVj3Fzpd3HLYMFkW7RruDjFxif9byxUGrOeHUWQPg5ZqmeN1NPQnxRBcriti3qZS1yCf1JZhzdemhTSZXy78tHdngqxQyJluhY2mXp3ATlmtcFqyEuYau22yS7YSHYYfCLb_6aD4a3deQ2oBRAFkqdoTNBzX24HswGDpwfwAxs7YnNJtFODEH0IFSxTK9iMjRY9AqlZlAMA8921zkFgm1P4p18CLoj5M9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XETO1ujY5SmNlzzokzcLb9o4pSYPuYZ6v0_gI7OUjhwJvK6_twYNp4z0qdEeIU1A7bHIYeFL5FfXnSvqi-M489Fcs7UkguR-AyqULx6sBcKGQZB71dmKBLvudtfBBWV11sXd7FepDLqgf7D_aRymZBnHJ4nZ38ZF69SM0iZX4mkBkBLPBxSh2Sv1Y9VKvCPGcRPcAxLhBgi6hLfz6TFm1DZZHmgmdhv2iWLgNKyXZePqmEEQHVoqKnTNQvVjmAdPdCA4HcZ3Yj0AnbJe7vupVryDW46JjqwUdonE9z2vyCaUObVs_tZyTlnq-c6moHHCL5QkOJBqYts2BITVNwc_NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PuuJKGz837Iq5VMIcxSTTlImlLeypRWLzcMcfM-dJUXZhjr9N0xpQHjWdjLOx6hvdrLUKsgU5ai0R5jvt491qj7Ya3ZDAbqrbeS3vK3Q1wO4-j2JDQgdKAmTx7Du-WV8noO57e1-xvK-3CXHb_22-0OjaQAUv8GriUCwKnBTUYBAH3Fnl6lJtWw-aYXQs-zZS5iUNHB-jzH-BGygFULFPW9RDpa4XakOVji0Wqts6WI3_5II8C7DsBiT1c_f2lCCJ10zHCF6SgaDyZjuZm-1bHEDObQyP0OLOxpIJ9EKDM0h2LarxvoSouO2ER3gnYuz-uji6vE5brxh7ORYjlDbWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
زاینده‌رود چشم اصفهان را روشن کرد
عکس:
حمیدرضا نیکومرام
@Farsna</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/farsna/439763" target="_blank">📅 06:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439762">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekM87x-IOPxMhP97jg4HfzzojncW-5BpAEhR-VWsp6Wl_5OLEtuecdGxmiPF79widgcgVNZ4X2vZXIFvDqkWSeIwlVpq7tbNmqduf7JsXyq0qzw_WQ-hdbHATnB6PILByr_nf5opDW-hQMLM-pOSit4IeR726Xf3r4S39TAUvC4Cy1PsuJf1EdBg4TrVj5w0xnMMaOtDl2C5j_qAtKBZRp6dZL-jq3vSSQrEKBkHmQCMGWkIEeaH6JjH7Y_-vghqL372488n_O0vejwaa5izNBogwl_XvdSSrjCD4n5qESHXhS3WstdAxb_8-rs6oWuFmtjAMHbTk8FBVn8WLKH1sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشفی تازه از تسلط ایران بر تنگۀ هرمز در ۲ هزار سال پیش
🔹
یافته‌های جدید باستان‌شناسی در هرمزگان نشان می‌دهد ایرانیان از حدود دو هزار سال پیش به اهمیت راهبردی تنگۀ هرمز آگاه بوده و بر مسیرهای دریایی منطقه نظارت داشته‌اند.
🔹
باستان‌شناسان از شناسایی بقایای یک دژ متعلق به دورۀ اشکانی در میناب خبر داده‌اند؛ دژی که به گفته پژوهشگران، بخشی از شبکۀ دفاعی و دریایی ایران برای کنترل مسیرهای تجاری و حفاظت از تردد کشتی‌ها بوده است.
🔹
در کنار این دژ، یک خور باستانی نیز شناسایی شده که احتمال نقش‌آفرینی این منطقه به‌عنوان یکی از مراکز مهم دریایی و بازرگانی جنوب ایران را تقویت می‌کند.
🔹
پژوهشگران معتقدند این پایگاه برای پشتیبانی و اعزام ناوگان دریایی به محدودۀ تنگۀ هرمز و نظارت بر کشتی‌های فعال در جادۀ ابریشم دریایی مورد استفاده قرار می‌گرفته است.
🔹
این کشف نشان می‌دهد حکومت‌های ایرانی از دورۀ اشکانی، برای حفظ امنیت مسیرهای بازرگانی و کنترل یکی از مهم‌ترین شاهراه‌های تجارت جهانی برنامه‌ریزی و سرمایه‌گذاری کرده بودند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/farsna/439762" target="_blank">📅 05:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439761">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e7aa4433f.mp4?token=aw0i4HWtJIx3yeBfBH6dT88oYHz9pHju-6XUwJloaZc_iRPzP14qlYNp4SLiNLcWH-CN1G_50o8euCK1weVpz09zVf7PIS__JmeJLd__7XLhs2a_RsKSe-Gl5Rky3_WqNXWZhlyETBor2o9G2GiJeh8eWHkTEhecRuPBuWV4NLioK_AG1yyABO5N4byue8cPdxTHD6hPoIbRHMvGEqwxBJR5jfJ8eQBuqAveZDVRz9Q5aa7vyS52Lke6WRZ2Vmrguejgz4sURAC_xPYPCL2WlqvMrYjAmNDVUSEDbqSPLbTS8Y99GYGk4ufVm6fo53bgfy3fnf5AFQ5wVYVY5ckHng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e7aa4433f.mp4?token=aw0i4HWtJIx3yeBfBH6dT88oYHz9pHju-6XUwJloaZc_iRPzP14qlYNp4SLiNLcWH-CN1G_50o8euCK1weVpz09zVf7PIS__JmeJLd__7XLhs2a_RsKSe-Gl5Rky3_WqNXWZhlyETBor2o9G2GiJeh8eWHkTEhecRuPBuWV4NLioK_AG1yyABO5N4byue8cPdxTHD6hPoIbRHMvGEqwxBJR5jfJ8eQBuqAveZDVRz9Q5aa7vyS52Lke6WRZ2Vmrguejgz4sURAC_xPYPCL2WlqvMrYjAmNDVUSEDbqSPLbTS8Y99GYGk4ufVm6fo53bgfy3fnf5AFQ5wVYVY5ckHng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای شنیدنی هدیۀ امیرالمومنین علیه‌السلام به علامۀ امینی!
@Farsna</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/farsna/439761" target="_blank">📅 05:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439760">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca2b00b797.mp4?token=fE4TxE8fSSVF2_cPNV6bLIvZbJ_TpWJnGLSICzAiienAhgGJCHTTThgFDbutUWknLCU6v9yEZHsWPzAGbaXDKO4mwjc0lcJxCy0AopjHHrYmHsx3ChNtk_5PVF3EMA5Ta-iPLqOrSg8MI6vU8dZ_Y2kxSqeHzVL9WQi6DKk_3Ae_2azeqHeDr1I50FbR7InUojPOHBBUCVlSxFhD7ED5u2CLRbUwH22GAN6qHBfztfSZj1v4lbQbAyEtXa7B_x0MZtKrql3QC1D-QHHUI3YezAxmBxGFEc4MNFxywQIkk99SZ-1IAFtSVO_kxJ8zMypq1rJBOzwcS6SDfmc48aiKTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca2b00b797.mp4?token=fE4TxE8fSSVF2_cPNV6bLIvZbJ_TpWJnGLSICzAiienAhgGJCHTTThgFDbutUWknLCU6v9yEZHsWPzAGbaXDKO4mwjc0lcJxCy0AopjHHrYmHsx3ChNtk_5PVF3EMA5Ta-iPLqOrSg8MI6vU8dZ_Y2kxSqeHzVL9WQi6DKk_3Ae_2azeqHeDr1I50FbR7InUojPOHBBUCVlSxFhD7ED5u2CLRbUwH22GAN6qHBfztfSZj1v4lbQbAyEtXa7B_x0MZtKrql3QC1D-QHHUI3YezAxmBxGFEc4MNFxywQIkk99SZ-1IAFtSVO_kxJ8zMypq1rJBOzwcS6SDfmc48aiKTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برپایی بزرگ‌ترین شهربازی دنیا در روز غدیر تهران
🔹
بزرگ‌ترین شهربازی دنیا در مهمانی ۱۰ کیلومتری روز غدیر برپا خواهد شد. برای درک ابعاد این رویداد نگاهی به بزرگ‌ترین شهربازی‌های جهان بیندازیم. مثلاً خیابان اصلی «مجیک کینگدام» در دیزنی‌ورلد حدود ۱.۵ کیلومتر طول…</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/farsna/439760" target="_blank">📅 05:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439759">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqy4xNZqeSRlehtK4aOgB7oPgs1Skyti1Y-bZSAskuOn4Xa3lZkDgMfIvxu9B4ZfbYDID8FKNrmnHdFEQgIivp2W-UHDyTD64A_WhGeMRccS1iQLfkaJkI2y8bMoyx_QJiuhkjjzU5hO_s1Su9FXbMZFJ8E9fEdPPWWoJ5K_d8e4czY-SG7TYTHCkdLX5kfKNWdE716_G42q2xam6eBkZsHtKo77A0PkIFmzD5yggCGHG1aP0ytT3xwjJXrZ9pUsd8ARQmpdb_MNpiJYvP43I44veoF4fuRoFYxuk1dYOaoZgs60Vi_F91Cgfp8TalKWw1hyjHKw7Ar7xSYa2N2uLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیرکل نجباء: سلاح مقاومت خط‌قرمز است
🔹
شیخ اکرم الکعبی: همه بدانند که سلاح مقاومت خط‌قرمز است و این، امانت شهدا است که با آن، اشک چشمان مادران داغ‌دیده را پاک کرده و دل‌های داغدار مومنان را خنک می‌کنیم.
🔹
با این سلاح بود که ما عراق را از وجود داعش و اربابان آمریکایی آن پاک کردیم و تا جان در بدن داریم، آن را تحویل نخواهیم داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/farsna/439759" target="_blank">📅 04:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439758">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j8hE8hgOM15SaqTXpPyrZBxazmQWUz4BaunyKcn0OAfq337oCP96B_ageoEM1afrbIlTDoWolJmonUC5X7L3WGgU4ESWnHGZpzAEE0FFqSwo40-jxhmFokgI3RBLzY01sKB0WIeNkNtCHc_BS5Xm2MJk8xIuTEBY03Co5ND0NJaNbmMO2pWeHQc0zxOaTjeTpwsJKvUzBK5FchbdJVUVrzXngYQ4E0wPM9YHdqvc_R9zD-hynVGiqsrDnHn0WZJdN7gKMHTZBMoNOZNJRqGrTcgSjDwbdHuMA3asKYNxRC1t1xM4q31pb2tGLXBZMEykrOeeZa9JNhIpPz0SLVq9Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات هدف مشروع دیگری برای ایران می‌سازد
🔹
نشریۀ فایننشال تایمز در گزارش اخیر خود تایید کرد که شرکت ملی نفت ابوظبی درحال برنامه‌ریزی برای ساخت خط لولۀ جدیدی با هدف دورزدن تنگۀهرمز است. این خط لوله قرار است صادرات بنزین و گازوئیل را فراهم کند.
🔹
در فراروایت این خبر، نتایج مهمی وجود دارد، ازجمله اینکه کشورهای عربی می‌دانند قرار نیست وضعیت تنگۀهرمز به قبل از ۹ اسفند بازگردد؛ درنتیجه به‌دنبال جایگزین آن هستند.
🔹
اما ایجاد چنین خط لوله‌ای، یک هدف دردسترس و کاملا مشروع دیگری به ایران می‌دهد که می‌تواند در تنش‌های بعدی هدف قرار بگیرد.
🔸
دورزدن تنگۀهرمز، پروژه‌ای است که سال‌ها پیش طرح‌هایی برای آن ارائه می‌شد؛ اما تمام آن‌ها به شکست انجامید. هرگونه دورزدن تنگه، درنهایت انتقال انرژی را به دریای سرخ می‌رساند. جایی که بازهم دست ایران برای کنترل بر کشورهای متخاصم باز است.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/farsna/439758" target="_blank">📅 04:16 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439757">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">مقام حزب‌الله: هیچ طرفی نمی‌تواند مقاومت لبنان را مجبور به خلع سلاح کند
🔹
محمود قماطی، نایب‌رئیس شورای سیاسی حزب‌الله: تمام تلاش‌های آمریکا و اسرائیل با شکست مواجه خواهد شد. رویارویی ادامه دارد و مقاومت در برابر تجاوز اسرائیل همچنان پابرجاست.
🔹
آمریکا و اسرائیل هیچ حقی درمورد سلاح‌های مقاومت ندارند، زیرا این یک موضوع داخلی لبنان است که ما درمورد آن توافق داریم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/farsna/439757" target="_blank">📅 03:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439756">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ادعای آمریکا دربارۀ موافقت لبنان و اسرائیل با آتش‌بس
🔹
وزارت خارجۀ آمریکا بامداد پنجشنبه مدعی شد که رژیم صهیونیستی و لبنان با آتش‌بس تحت نظارت واشنگتن موافقت کرده‌اند.
🔹
رسانه‌های آمریکایی گزارش دادند که چهارمین دور مذاکرات بین نمایندگان دولت لبنان و رژیم…</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/439756" target="_blank">📅 03:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439755">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">ادعای آمریکا دربارۀ موافقت لبنان و اسرائیل با آتش‌بس
🔹
وزارت خارجۀ آمریکا بامداد پنجشنبه مدعی شد که رژیم صهیونیستی و لبنان با آتش‌بس تحت نظارت واشنگتن موافقت کرده‌اند.
🔹
رسانه‌های آمریکایی گزارش دادند که چهارمین دور مذاکرات بین نمایندگان دولت لبنان و رژیم صهیونیستی در واشنگتن به پایان رسید.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/farsna/439755" target="_blank">📅 03:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439753">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🎥
شکر خدا که نام علی در اذان ماست
@Farsna</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/439753" target="_blank">📅 03:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439752">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">حملات موشکی حزب‌الله به مواضع صهیونیست‌ها
🔹
حزب‌الله اعلام کرد مواضع دشمن در جنوب لبنان را با موشک هدف قرار داده است.
🔹
همچنین یک پهپاد اسرائیلی را با موشک زمین به هوا در جنوب لبنان رهگیری، و مجبور به ترک منطقه کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/439752" target="_blank">📅 02:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439751">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d86d1c07d.mp4?token=rzhZa6cYWMx1c8v-GYQ8f3ivTDyz_Xfa1RBPKroTUaAhY1Bun9Bdnxq4dbLzxnlzedWJNL2RyLUiFFpGnChH_5W_-tkqhjmMJwwRZRCkQKYVOWB_2RvBLMMkKAlCETx7-ZUWCb1lNUH1ufJxL_i64J7misIvYPuFJIs3tF2_gLwiWJVNUUrKxhr0bsVQsnxQfRUwj-nwnPy48QrpB2XOMWZEWryUSb-tVX2EXLEj2L5x_fuSOiKqpnuRhDwgQ_jKZq8IkvnxD7nYI-RcF5ajf7nvOfYOPOipXNg7DV091ZagM0pWh46QbReB4z7Fv5yPgIiBV3LnF7I9I5oU-5nR-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d86d1c07d.mp4?token=rzhZa6cYWMx1c8v-GYQ8f3ivTDyz_Xfa1RBPKroTUaAhY1Bun9Bdnxq4dbLzxnlzedWJNL2RyLUiFFpGnChH_5W_-tkqhjmMJwwRZRCkQKYVOWB_2RvBLMMkKAlCETx7-ZUWCb1lNUH1ufJxL_i64J7misIvYPuFJIs3tF2_gLwiWJVNUUrKxhr0bsVQsnxQfRUwj-nwnPy48QrpB2XOMWZEWryUSb-tVX2EXLEj2L5x_fuSOiKqpnuRhDwgQ_jKZq8IkvnxD7nYI-RcF5ajf7nvOfYOPOipXNg7DV091ZagM0pWh46QbReB4z7Fv5yPgIiBV3LnF7I9I5oU-5nR-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دل‌هایی که مبدأ قدرت متصل بود و دل از ما ربودند
@Farsna</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/439751" target="_blank">📅 02:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439750">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R58gEoxqQUr0RXnIsS_wqvkF2B8JHi4k0q9olkgdxBuZUjDeYgQp_FkMnV4u24VP_GUbXmkqY6f-ys9Q_rHIdI0I5M7zQUkyh2PjRbIsAnonmNhwdvTunMA6JqMgDQDGYoQ6-BsBKa09xemw4bDgliYghSl-Y30_4nbrhYMchjQunVetPjwhaMs-npKXSZ-ly_9LAzBQ394tZRxuEAw0-HyNQdEVxOCBpNxXKQJWcs38DLRke8-7hmy_ENAJmHxZyEHzccvSpre0C4grZ1FuPPVgsX4mGBQwVJizKmDT8KOtzIBEhgcHNRGW1ib5pSvPwg-2giLdjduVzNmAkHkYGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آهسته برانید؛ «هلیا» و توله‌هایش از جاده مرگ می‌گذرند
🔹
در حالی که محیط‌بانان حیات‌وحش این روزها چشم به تحرکات هلیا و سه توله‌اش دوخته‌اند، محور عباس‌آباد-میامی بار دیگر به کانون نگرانی دوستداران محیط‌زیست تبدیل شده است.
🔹
این جاده طی سال‌های گذشته بارها به قتلگاه یوزپلنگ آسیایی تبدیل شده و حالا ترس آن می‌رود که یکی دیگر از خانواده‌های ارزشمند این گونۀ در معرض خطر انقراض، در مسیر عبور از آن با تهدیدی جدی روبه‌رو شوند.
🔹
برآوردها حاکی است حدود ۵۰ کیلومتر از این محور ترانزیتی در محدودۀ عبور اصلی یوزپلنگ آسیایی قرار دارد، بنابراین نقش رانندگان در کاهش خطرات و حفظ جان این گونۀ ارزشمند انکارناپذیر است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/439750" target="_blank">📅 01:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439749">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd4aeb0d1.mp4?token=PghnY9aQp2FPZzXfIQSR1K5qz9BhrB_mo28XP1L0NAQrI4IuE55wDehIJ-OoLzLwfxv1yx9X5x0i5RuZ2-UV141nJQiWHdsLlNdHN_ULtuWRMVtNQaCkCJkwha4c2BRPAxzI5HjXsdlwtTpxSMSlbAc3xHctVyPfUaZHP42D8UWSpdykPcfhnV2ZQ0Gzk7CG6SRIHF92R0I7choG5ga4_05VPFKKauSHW5H4qseRQeBRbkE2aUy5AThWR-aRt5gSULyv3DZ0UnLFpk3uJrzt8TDvS9EEfLUCOfhdYiwutIhRjO0_h38KEmo7Z7jlQTnA-GgFniueaFHvFtuqPYu-Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd4aeb0d1.mp4?token=PghnY9aQp2FPZzXfIQSR1K5qz9BhrB_mo28XP1L0NAQrI4IuE55wDehIJ-OoLzLwfxv1yx9X5x0i5RuZ2-UV141nJQiWHdsLlNdHN_ULtuWRMVtNQaCkCJkwha4c2BRPAxzI5HjXsdlwtTpxSMSlbAc3xHctVyPfUaZHP42D8UWSpdykPcfhnV2ZQ0Gzk7CG6SRIHF92R0I7choG5ga4_05VPFKKauSHW5H4qseRQeBRbkE2aUy5AThWR-aRt5gSULyv3DZ0UnLFpk3uJrzt8TDvS9EEfLUCOfhdYiwutIhRjO0_h38KEmo7Z7jlQTnA-GgFniueaFHvFtuqPYu-Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
با فرزندان اپستین صلح نمی‌کنیم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/439749" target="_blank">📅 01:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439748">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4FvcJy0FX7WfpkqwiaAd-vrkiEpVNpc9PsaWwX6KQHFyHDukeu_rytM3Wwui_vfRu0VYYIxYck02FQRvBopdh7B2sMnICQx_GJ1CQKY9GCvzGhNUySnfC1VjYPA4GMAFWw6nd0ZLJvIyWd1259kwVdHTHdj8CQkrorDjIJWqIgFUBjv_XIAqzgx6tFZwdI0wPSJXj2V3n_OvdYBeMxMYgVxSp7dNDrzXhH5KVQVJug-ap_lY4A1WusvWeG0miSt6HHO5Pkn3Xz3GJmjKFSvk5Jd4Pba9kYaLg90TLD_4aSLS5r3OyWxyymVzQ3pztIlFNQ-rbWQHn5XOM81yLZK1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویب قطعنامه‌ای در مجلس نمایندگان آمریکا برای پایان جنگ با ایران
🔹
مجلس نمایندگان آمریکا بامداد پنجشنبه قطعنامه‌ای برای مجبور کردن رئیس‌جمهور این کشور به خارج کردن ارتش آمریکا از جنگ با ایران تصویب کرد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/439748" target="_blank">📅 01:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439747">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15dfcd9da3.mp4?token=GIjAO2bntXNVlW3HM-lPUnF8wk2mBgjY9Z2pIMs3skEN_WzJPS_UQtojxTu9_xN7IgzAheQiFu-RlBsVD2A_OyynsnX4yoatVdfzCkQESeiugC4lsFdatQpaUexR60xc_4k8fDbmZ5vCFARzjbJaxW--XfQrY1vMoTXCMPO8ZwzzUIqD5weSjNaT37GyQi8kRQ-6YUsJ1mFvTge3Oxu783Lcc4LKDWgmz2QudnzBLl6rpe_RVnXxVHNg3ODSqI-2rJO5DcP2e2HV4lGiySzQ_iOcpSEXtbxcnBYZLe1kWdbdNl7poY2V00g_ZYPj9hpvMLouxPoN2SeBRivOAF-U5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15dfcd9da3.mp4?token=GIjAO2bntXNVlW3HM-lPUnF8wk2mBgjY9Z2pIMs3skEN_WzJPS_UQtojxTu9_xN7IgzAheQiFu-RlBsVD2A_OyynsnX4yoatVdfzCkQESeiugC4lsFdatQpaUexR60xc_4k8fDbmZ5vCFARzjbJaxW--XfQrY1vMoTXCMPO8ZwzzUIqD5weSjNaT37GyQi8kRQ-6YUsJ1mFvTge3Oxu783Lcc4LKDWgmz2QudnzBLl6rpe_RVnXxVHNg3ODSqI-2rJO5DcP2e2HV4lGiySzQ_iOcpSEXtbxcnBYZLe1kWdbdNl7poY2V00g_ZYPj9hpvMLouxPoN2SeBRivOAF-U5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از نماز با فضلیت روز غدیر غافل نشوید
🔹
در مفاتیح آمده که اگر می‌خواهید برایتان بنویسند که در روز غدیر حاضر بودید و با پیامبر(ص) برای ولایت بیعت کردید ۲ رکعت نماز را بخوان.
شیوهٔ خواندن این نماز را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/439747" target="_blank">📅 01:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439746">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYNQJZqmVExK38lIP7WMYsK0g9xYvf1ewZSMNOID40QDur9Aoxk1VukwD44eio3daHLWWGnOYJ49VtrHCvvbGtONowVSPHww51d6m51HBS-XnNSNPWCKMF7kEKH2Aw9Jw_Hu8r6UI8neR6uVCM274x1bw5LZsrb_Cm23hiiqgA5xmcaa_9wVX2J8rq-JdN-ChqsU1YbiUmKdkxIm9rLSbGtkAoyI-fs2D49MSwKYL8k-XW2BPbUcAi_YwQv18ImfkVlJc4DzGCGmBIuaf9yH1aEvn2ijrsMzcFAq-NtZo7auhgS7WlIONe373L-Efrm_GevqyJpQsUhbOPhq_3MkCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
برنامه اصلی مهمانی ۱۰ کیلومتری غدیر در میدان انقلاب اعلام شد
@Farsna</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/farsna/439746" target="_blank">📅 00:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439745">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i8CtPsWNRPYUjTBpNR-jHTMBnJTacSfjF9rzxPxRQRfI9kKzlVna8GZSYHHpj_U7HpUTDNao6XrvO_80IX2EkQSwBx73pTHWknHgOJOwD8M6bg9IRO1Qjd8cczUG8OnAwxCKAMJKRjp7o2TPjMSLyREK8wf2U0iYSKrRH6T13h1bttSHBube137W8TRHn6EltunclQ8Y2tt45qHsic8LQ7cAsjj8SFn_rDQ5eI8n5NfTlOWcP1HJpoSlFw8HRzgzDrQP6aYDh8AGuiUeOa2RvMuD5GrjOhy9YQBnypXbrcl5MD_UeVnZUAtuIBszZncIXiR-yuVAXX-_bpMB0cE7hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گل‌محمدی، در یک‌قدمی سرمربی‌گری دهوک عراق
🔹
در شرایطی‌که طی روزهای گذشته اخباری دربارۀ مذاکرات یحیی گل‌محمدی با باشگاه دهوک عراق منتشر شده بود، از دقایقی قبل برخی رسانه‌ها و صفحات خبری نزدیک به فوتبال عراق اعلام کردند گل‌محمدی هدایت این تیم را برای فصل آینده برعهده گرفته است.
🔸
بااین‌حال تا این لحظۀ باشگاه دهوک به‌صورت رسمی از سرمربی جدید خود رونمایی نکرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/439745" target="_blank">📅 00:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439744">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b7a8c1d97.mp4?token=GYivAB5t0e62Q6lXkJLZS7SonDPtE6kLv8R7_o5-zF-ahmL9aJB1tD2fKOo6E1EAOFUwuzhaVWBsQyM2KGryx4RlkaB6wYLSEyzAh2tks_8SsMd_8IKA0gKiTC9cw_2vvyO8M-vlNGHyw52ryrrq0X1RgNrDDZSfjwPR-s3hGe0q3KEgg8fXqb3tnoLuvAgQgFeISNZNQvOarZrRX1KGnFpoFc9QPf0BTUnd2eCmga6wxVKGnoBS-CCIGPLoBtjVgSCnBigrX6F6HvUEUv5CjOoo8F-0i5kwrfMaxownObTUIVoqdJc-0-1yE9DvAgedUdLCooIgcENsGvga-ugOGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b7a8c1d97.mp4?token=GYivAB5t0e62Q6lXkJLZS7SonDPtE6kLv8R7_o5-zF-ahmL9aJB1tD2fKOo6E1EAOFUwuzhaVWBsQyM2KGryx4RlkaB6wYLSEyzAh2tks_8SsMd_8IKA0gKiTC9cw_2vvyO8M-vlNGHyw52ryrrq0X1RgNrDDZSfjwPR-s3hGe0q3KEgg8fXqb3tnoLuvAgQgFeISNZNQvOarZrRX1KGnFpoFc9QPf0BTUnd2eCmga6wxVKGnoBS-CCIGPLoBtjVgSCnBigrX6F6HvUEUv5CjOoo8F-0i5kwrfMaxownObTUIVoqdJc-0-1yE9DvAgedUdLCooIgcENsGvga-ugOGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: آتش‌بس یعنی شلیک ملایم!
🔸
خبرنگار: تعریف شما از آتش‌بس چیست؟
🔹
ترامپ: آن‌جا [ایران] بخش دیگری از دنیاست. متوجه منظورم می‌شوید؟ در آن منطقه از جهان، آتش‌بس یعنی زمانی که با شدتِ ملایم‌تری شلیک می‌کنید! @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/439744" target="_blank">📅 00:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439743">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">یمن: کشورهای عربی دست از مظلوم‌نمایی بردارند
🔹
وزارت خارجۀ یمن با تمجید از پاسخ ایران به تجاوزات آمریکا، تلاش برخی کشورهای عربیِ میزبان پایگاه‌های آمریکایی برای مظلوم‌نمایی و ایفای نقش قربانی را محکوم کرد.
🔹
یمن در این بیانیه تاکید کرده کشورهای مذکور با سیاست‌های احمقانۀ‌شان صدمات زیادی به خود و مردمان‌شان وارد می‌کنند و اولین بازندگان این نبرد هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/439743" target="_blank">📅 00:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439742">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab704aeadb.mp4?token=n3cSPgG6X8S1mZRP0qXp1v2q_EOFjPGfTxOp_AuxPekkgIjZVN82Hq5WLk94V83bFanVJBjO1Y7NOwTDadZy0Oqd404LOyNMYgovA2y0qHVjdch32A_SShB_w3JZJRiODeDPoeHoeaENXEkOkZKpia45myONvlTuUNKdU1FeNaK4za82ndtIU3rWjz1a8j8joX9b_XB2rs80bnkH4wRZhdjMg5NkCCyvwOgmKmXLROkhZPrfNpJwiEdExEnej9gictcyTa70VDE-werUIPxdeQnVLBCDES4n_BWEt1JhxqeTN31M2_kRWOtfoyNIVdmNrfhDotB932-NtXAQsEIpQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab704aeadb.mp4?token=n3cSPgG6X8S1mZRP0qXp1v2q_EOFjPGfTxOp_AuxPekkgIjZVN82Hq5WLk94V83bFanVJBjO1Y7NOwTDadZy0Oqd404LOyNMYgovA2y0qHVjdch32A_SShB_w3JZJRiODeDPoeHoeaENXEkOkZKpia45myONvlTuUNKdU1FeNaK4za82ndtIU3rWjz1a8j8joX9b_XB2rs80bnkH4wRZhdjMg5NkCCyvwOgmKmXLROkhZPrfNpJwiEdExEnej9gictcyTa70VDE-werUIPxdeQnVLBCDES4n_BWEt1JhxqeTN31M2_kRWOtfoyNIVdmNrfhDotB932-NtXAQsEIpQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: آتش‌بس یعنی شلیک ملایم!
🔸
خبرنگار: تعریف شما از آتش‌بس چیست؟
🔹
ترامپ: آن‌جا [ایران] بخش دیگری از دنیاست. متوجه منظورم می‌شوید؟ در آن منطقه از جهان، آتش‌بس یعنی زمانی که با شدتِ ملایم‌تری شلیک می‌کنید!
@Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/439742" target="_blank">📅 00:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439741">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22ad2b4c8f.mp4?token=Zl1kv_ifx8rpNYkbCPDSdQoIe7ij87VNr5uA1MVsFyfI8k66BbXRxErAjC7kpIfLYNkrXTAtt8CxuZIAqDKPNpRvRL-f24OgKH3xferXV3c-_EnS6fsLMZDwugpSXKESjQWcNBUA74wN5LuytPiAeGmvaWZPEzCDnV7EG2J-UJPGz3I2gOaJ67YCPMj5nIL0mjLvKyt9W8T7YZ2guwMvD2wmDV5Zt4xU0bpt_pSZdINzUXPJrsC8rpGRbgxi2Tf9tLH7-fdAbjqUO0iT5ij_3mq9uQTXkU1XbLZoA74fuMuLVDU8s-DGYGKbkZkVyBw_aDtMYh-fDuOJyqgM4KrEpx4Ehr1-UbdybLRNxcch6QfUp_0iQC1amYTlh6LXT0sboZEGJ8bWaiRJpQwR9nc9EwRquH-OYTJuYvG46vaQbsW_USZ8v0JSOi_G5BdC6JMQvaZtWkMHptQDTjRtcIsyOHwOcOogK5QQE02twyvd1_e4xrtpBzeAYwDIdyM7qf8ZfZmSY4MoRu_aSeRhIV2jB4MRZ1uROmeBEGAohFA52IlSRfZTgSrmvyYPN0Jp1q9_OOGoroRtZsxoLUuNTcv3k0umYbDpLyg8pFW6WbWzquPkhyCDeR78pzKyZjs6hMvrJkafVeium_rj2rGsQ2tF03NDIk6c64Rd_LdfddXPaM4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22ad2b4c8f.mp4?token=Zl1kv_ifx8rpNYkbCPDSdQoIe7ij87VNr5uA1MVsFyfI8k66BbXRxErAjC7kpIfLYNkrXTAtt8CxuZIAqDKPNpRvRL-f24OgKH3xferXV3c-_EnS6fsLMZDwugpSXKESjQWcNBUA74wN5LuytPiAeGmvaWZPEzCDnV7EG2J-UJPGz3I2gOaJ67YCPMj5nIL0mjLvKyt9W8T7YZ2guwMvD2wmDV5Zt4xU0bpt_pSZdINzUXPJrsC8rpGRbgxi2Tf9tLH7-fdAbjqUO0iT5ij_3mq9uQTXkU1XbLZoA74fuMuLVDU8s-DGYGKbkZkVyBw_aDtMYh-fDuOJyqgM4KrEpx4Ehr1-UbdybLRNxcch6QfUp_0iQC1amYTlh6LXT0sboZEGJ8bWaiRJpQwR9nc9EwRquH-OYTJuYvG46vaQbsW_USZ8v0JSOi_G5BdC6JMQvaZtWkMHptQDTjRtcIsyOHwOcOogK5QQE02twyvd1_e4xrtpBzeAYwDIdyM7qf8ZfZmSY4MoRu_aSeRhIV2jB4MRZ1uROmeBEGAohFA52IlSRfZTgSrmvyYPN0Jp1q9_OOGoroRtZsxoLUuNTcv3k0umYbDpLyg8pFW6WbWzquPkhyCDeR78pzKyZjs6hMvrJkafVeium_rj2rGsQ2tF03NDIk6c64Rd_LdfddXPaM4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم تهران آمبولانس آسیب‌دیده در حملات آمریکا و اسرائیل را گلباران کردند
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/439741" target="_blank">📅 23:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439740">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d79700139f.mp4?token=q1Z395e3USgUB0UpOkYFHCMF3IvHQQntDypQ6_UZ4-QTp4oMamhCuvS6l_zthuwLM_JE2Nk8wTWOZn-Qu9k9aB2fcoJYKDMGu4H_oDsLZHw2AfgCrLyQvmub5g6vimq3k03HGlDsrvqbF9iOavUxn8_WQ4ZbmPN6iPfACAQ7X3qNkaSi-U5rl1TnIUwkGKvfu9KZ8HjMofo4T8WomsOHMy2Sc15reTI9vXUI35Kf-vComyFfhQRJnx3N4zmyNNTWk5wkUIvF2WuisTGIHQIKGB3B45QNBaAISLPOqttQFEGXswmU84Mwvf6dw_v7aXNaLiyobHnT6pCQW1iRTKNO8Ij7yuhtXgrPO07NGnVMsaXS4DoIUyaVma-_NQBIzhIOBBnk9KfnGx3BTqPdBthN1oIAuUWw-3u6M30A0Z8l9esF5EH4FOo7dYwfZGdvJJCn4K2TU2qUeBf2-3QRUOUdm4jVDLv-2kjVisWVSf9z0kccXkOnEL0khpL6YcV6KBL1YiMtHzP267kLzZKJ1Jo2flwpphhvps0iDCG68zsLvRdwGa2Lvvr3PfjobtTGrxSls89Wckd7e9BymrYD_wHgVWm3r2gEciIkaka8TzXKfjKkAMc3m9xjPlGwXpvLRIN_UjFctJlkA-QBQ6XTfx3RA0G_hmF49hOGkBtKFjJpu2Y" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d79700139f.mp4?token=q1Z395e3USgUB0UpOkYFHCMF3IvHQQntDypQ6_UZ4-QTp4oMamhCuvS6l_zthuwLM_JE2Nk8wTWOZn-Qu9k9aB2fcoJYKDMGu4H_oDsLZHw2AfgCrLyQvmub5g6vimq3k03HGlDsrvqbF9iOavUxn8_WQ4ZbmPN6iPfACAQ7X3qNkaSi-U5rl1TnIUwkGKvfu9KZ8HjMofo4T8WomsOHMy2Sc15reTI9vXUI35Kf-vComyFfhQRJnx3N4zmyNNTWk5wkUIvF2WuisTGIHQIKGB3B45QNBaAISLPOqttQFEGXswmU84Mwvf6dw_v7aXNaLiyobHnT6pCQW1iRTKNO8Ij7yuhtXgrPO07NGnVMsaXS4DoIUyaVma-_NQBIzhIOBBnk9KfnGx3BTqPdBthN1oIAuUWw-3u6M30A0Z8l9esF5EH4FOo7dYwfZGdvJJCn4K2TU2qUeBf2-3QRUOUdm4jVDLv-2kjVisWVSf9z0kccXkOnEL0khpL6YcV6KBL1YiMtHzP267kLzZKJ1Jo2flwpphhvps0iDCG68zsLvRdwGa2Lvvr3PfjobtTGrxSls89Wckd7e9BymrYD_wHgVWm3r2gEciIkaka8TzXKfjKkAMc3m9xjPlGwXpvLRIN_UjFctJlkA-QBQ6XTfx3RA0G_hmF49hOGkBtKFjJpu2Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جشن باشکوه یمنی‌ها به‌مناسبت عید غدیر در صنعا
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/439740" target="_blank">📅 23:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439739">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cfac4c46c.mp4?token=KPOeOYO8lFL3XYt8Nhn4AXeXegJrexpfhrfgyrATnILqoZgub9er93SYVi9pjUeDleAoJwQYI5e9yiNRqkqMjPH54ZjrNGTsuQI5KMytXMEEmU-6O3c68YCTnXf4ed2jlob4nAFLxfPvZEhCuxXi8XnNNtppoiLhbbrgNs5oYAUhutI_0jis_favPtb6dn5bNB9piP71C0KHxeo8YZqOpgLer44f0HrkjQiRqEGfgvCYmpYzCW0PbifPPiBU9TXvlNnynkCjOi_bzqpD8OspCakEPl7zQNhJu--9cpeCeahxKMEKQ5coe5aA2rU7fL1phTKsaV4FpZOTkXeeYd7p4zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cfac4c46c.mp4?token=KPOeOYO8lFL3XYt8Nhn4AXeXegJrexpfhrfgyrATnILqoZgub9er93SYVi9pjUeDleAoJwQYI5e9yiNRqkqMjPH54ZjrNGTsuQI5KMytXMEEmU-6O3c68YCTnXf4ed2jlob4nAFLxfPvZEhCuxXi8XnNNtppoiLhbbrgNs5oYAUhutI_0jis_favPtb6dn5bNB9piP71C0KHxeo8YZqOpgLer44f0HrkjQiRqEGfgvCYmpYzCW0PbifPPiBU9TXvlNnynkCjOi_bzqpD8OspCakEPl7zQNhJu--9cpeCeahxKMEKQ5coe5aA2rU7fL1phTKsaV4FpZOTkXeeYd7p4zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جشن خاطره‌انگیز شب غدیر در پیشوای تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/439739" target="_blank">📅 23:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439738">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f019ceaf5b.mp4?token=Hu3ZtOTJmLtBAaYCRBiiuTocl9BbvHVTlgisJuEjrKYLQyUKgc6MkOQNN5GcpjY9QwfIB4n1CxLad8DkxRKKKzxdivtb97ssjw5oqUyPQ09hovDexFZ7FyLe6psqFl9exn8XSyGDKzpbwQqG5jHc8XmmBlSComg6XBLj5Dv1rene81HmMMOmAeI9egSugXFZ2djPKpEUqZBHJjB4FsgFTlKouGfm-TKE9IkY1bPF0dB-lOQzDs9B-D__CsGIFFnsmNKuzppOAnQncW97gLQmXub8C-rkJKmRsZoxZfdf1J-EPz8CYzNGSYd2zZqMLVYopsyKOhZofLzwmUvuvBt-QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f019ceaf5b.mp4?token=Hu3ZtOTJmLtBAaYCRBiiuTocl9BbvHVTlgisJuEjrKYLQyUKgc6MkOQNN5GcpjY9QwfIB4n1CxLad8DkxRKKKzxdivtb97ssjw5oqUyPQ09hovDexFZ7FyLe6psqFl9exn8XSyGDKzpbwQqG5jHc8XmmBlSComg6XBLj5Dv1rene81HmMMOmAeI9egSugXFZ2djPKpEUqZBHJjB4FsgFTlKouGfm-TKE9IkY1bPF0dB-lOQzDs9B-D__CsGIFFnsmNKuzppOAnQncW97gLQmXub8C-rkJKmRsZoxZfdf1J-EPz8CYzNGSYd2zZqMLVYopsyKOhZofLzwmUvuvBt-QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ما باهم برادریم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/439738" target="_blank">📅 23:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439737">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e8a90399b.mp4?token=ScQro4eiTnmyBINATHuFGNxX4eSFnw8JR27sYR9ckB949vnaUFNsDIe6X1Abh_czNYyoxzzQmhTjhbqsEDPQQkHj3qvL2lepxVsjcdVRvkX1NIK-ur7Q3bEWVHQX8Uw8yEV-kzymp7kU9WcHXTQs8dDCVFOWoql8jHQiOlop8c75u_U-n9_GZTJ8nlUYkLYSpYv8uThnIlU61vpd1j807U847RDVduBXZQNJsjm5iCoVhOTFghtPjTzpokR1kr9UySSDEr_YKfD7zLjJLmU9x877g_b08lil-6eySraObdq-cHt_0daiiq9cpVo4HfxCwOpk-0ZFvTNIFpdRX32_3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e8a90399b.mp4?token=ScQro4eiTnmyBINATHuFGNxX4eSFnw8JR27sYR9ckB949vnaUFNsDIe6X1Abh_czNYyoxzzQmhTjhbqsEDPQQkHj3qvL2lepxVsjcdVRvkX1NIK-ur7Q3bEWVHQX8Uw8yEV-kzymp7kU9WcHXTQs8dDCVFOWoql8jHQiOlop8c75u_U-n9_GZTJ8nlUYkLYSpYv8uThnIlU61vpd1j807U847RDVduBXZQNJsjm5iCoVhOTFghtPjTzpokR1kr9UySSDEr_YKfD7zLjJLmU9x877g_b08lil-6eySraObdq-cHt_0daiiq9cpVo4HfxCwOpk-0ZFvTNIFpdRX32_3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خرم‌‌آبادی‌ها: ما پیرو غدیریم، ذلت نمی‌پذیریم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/439737" target="_blank">📅 23:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439736">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54d945556a.mp4?token=IqBIHeXmiv8nPs0yhFuFvpHwzx-X-SUvwQEZk8exW5qkYSBfyE0PRttNqgzWHMwjqlF0x3_7j32TIHY6ExOplTJPV9bm2THAl0k3sY5pEkXJybDOsbBjh3CVTBXIt4JWUzxG2Wg1KHpwA7Va7Xu44CSMw2N9QtTMw1Y1SqrwKM77mjiKlqy894_yPwyS3s1jBk5TGOcXmq0sV0FFeFWzJ-laFUWgYHFC5bk8NshlVnQovj5-LkPDpsVh8DUdXDNFNo9hatS1j3DoIL6nx-zaMR1vw3TNo6jMvptDQjjFSBeC0ljh727UM40fwKfLrlK50_q2NfE8cvyWgHt6FkIkPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54d945556a.mp4?token=IqBIHeXmiv8nPs0yhFuFvpHwzx-X-SUvwQEZk8exW5qkYSBfyE0PRttNqgzWHMwjqlF0x3_7j32TIHY6ExOplTJPV9bm2THAl0k3sY5pEkXJybDOsbBjh3CVTBXIt4JWUzxG2Wg1KHpwA7Va7Xu44CSMw2N9QtTMw1Y1SqrwKM77mjiKlqy894_yPwyS3s1jBk5TGOcXmq0sV0FFeFWzJ-laFUWgYHFC5bk8NshlVnQovj5-LkPDpsVh8DUdXDNFNo9hatS1j3DoIL6nx-zaMR1vw3TNo6jMvptDQjjFSBeC0ljh727UM40fwKfLrlK50_q2NfE8cvyWgHt6FkIkPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت بغض
‌
آلود دیدار بانوی لبنانی با رهبر شهید پس از شهادت
سید حسن نصرالله
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/439736" target="_blank">📅 23:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439735">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f165fa9c0b.mp4?token=U15JR9_hApTY7McYimvxXwmSHTN19iMmV2euxx7-2kNkWKzB_xqkYYKB7XkxmQON7KKz1k05P93mjcJqbcv0LA1M5ypZZSMi9_7zN0hPfX2GBPmqw98j8nXYF5WNFNgHtGGZhdh1A0o5Sy0SWyX641_SdijRB8MUVuf2PBBSsX7MdvIZPyucoiYoaS10tZ6mj1z8zjJzm01ZLHshkDI1cWZVSjqezo1T_NUMx49flqKRUqKN0YCZKCpx0gGuOdektcZtYoR4W7ZqpFX9ebqKV_n7Uq2BPYqHx5k0eSjXsacLCICkUdG0aeXXD6tVr5TAbNcHGj4rjb3cHh_qowegrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f165fa9c0b.mp4?token=U15JR9_hApTY7McYimvxXwmSHTN19iMmV2euxx7-2kNkWKzB_xqkYYKB7XkxmQON7KKz1k05P93mjcJqbcv0LA1M5ypZZSMi9_7zN0hPfX2GBPmqw98j8nXYF5WNFNgHtGGZhdh1A0o5Sy0SWyX641_SdijRB8MUVuf2PBBSsX7MdvIZPyucoiYoaS10tZ6mj1z8zjJzm01ZLHshkDI1cWZVSjqezo1T_NUMx49flqKRUqKN0YCZKCpx0gGuOdektcZtYoR4W7ZqpFX9ebqKV_n7Uq2BPYqHx5k0eSjXsacLCICkUdG0aeXXD6tVr5TAbNcHGj4rjb3cHh_qowegrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ذوق‌زده‌شدن داوران برنامه محفل از قرآن خواندن بامزه دختربچه شیرین‌زبان
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/439735" target="_blank">📅 23:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439734">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2201a57b07.mp4?token=Jvx1c1sE41Atg0z_XnIg55yX3qj_C4mej43ZZr512MKLSFibcHTWUuwBY3m_SrSnYzS06_X617NDM45x2ISVmJtI4G1L5th161rhn-wgGrQZTWm_hcm6UxDeK7p3EOFDvA_MHxcSu62mvgemHYjFBjLHxt6I9Fexj15g606RdPblN8_CiseOaAtaW0U7KB1hZBNQxGYtVmJzOl6ncFJxOUriQoZtr5CNyaecaYvi8TQ55p2qBjFKckItt3kCDcEywjpMsyxEIM7uk4oTeys-zA0KHU_I7s0uCd5yEYSduEELljqEFOt6cBHpw_wm61AQQbUK5nPcLg98nKhjPffGzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2201a57b07.mp4?token=Jvx1c1sE41Atg0z_XnIg55yX3qj_C4mej43ZZr512MKLSFibcHTWUuwBY3m_SrSnYzS06_X617NDM45x2ISVmJtI4G1L5th161rhn-wgGrQZTWm_hcm6UxDeK7p3EOFDvA_MHxcSu62mvgemHYjFBjLHxt6I9Fexj15g606RdPblN8_CiseOaAtaW0U7KB1hZBNQxGYtVmJzOl6ncFJxOUriQoZtr5CNyaecaYvi8TQ55p2qBjFKckItt3kCDcEywjpMsyxEIM7uk4oTeys-zA0KHU_I7s0uCd5yEYSduEELljqEFOt6cBHpw_wm61AQQbUK5nPcLg98nKhjPffGzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
نیروی دریایی ارتش، مرکز فرماندهی و کنترل شرارت‌های ارتش آمریکا علیه کشورمان را هدف قرار داد
🔹
ساعاتی قبل و درپی اقدامات تجاوزکارانه، نقض مقررات تنگهٔ هرمز و شرارت علیه شناورهای تجاری ایرانی در دریای عمان از سوی ارتش تروریستی و متجاوز آمریکا، نیروی دریایی…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/439734" target="_blank">📅 22:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439732">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
نیروی دریایی ارتش، مرکز فرماندهی و کنترل شرارت‌های ارتش آمریکا علیه کشورمان را هدف قرار داد
🔹
ساعاتی قبل و درپی اقدامات تجاوزکارانه، نقض مقررات تنگهٔ هرمز و شرارت علیه شناورهای تجاری ایرانی در دریای عمان از سوی ارتش تروریستی و متجاوز آمریکا، نیروی دریایی ارتش جمهوری اسلامی ایران، به‌محض کشف و شناسایی، «مرکز فرماندهی و کنترل» این شرارت، مستقر در یک فروند ناوشکن آمریکایی که قصد نزدیک‌شدن به آب‌های جمهوری اسلامی ایران در دریای عمان را داشت، هدف قرار داد.
🔹
نیروی دریایی ارتش، با تمام توان، دشمن جنایتکار و متجاوز آمریکایی-صهیونیستی را رصد کرده و انتقام خون پاک شهدای سرافراز ناوشکن دنا را به شدیدترین وجه خواهد گرفت و با هرگونه شرارت، در کمترین زمان ممکن برخورد خواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/439732" target="_blank">📅 22:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439731">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‌
🔴
عراقچی: هیچ‌کس نمی‌تواند حزب‌الله را حذف کند یا نادیده بگیرد
🔸
تمام جهان می‌دانند که حزب‌الله بخشی از لبنان، جامعه و ساختار سیاسی آن است. مسائل داخلی لبنان باید با مشارکت همه طرف‌ها و در چارچوبی لبنانی-لبنانی حل‌وفصل شود. @Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/439731" target="_blank">📅 22:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439730">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f881ae437b.mp4?token=fS2a4bqaf3k1sMAWcX1no_fYi25dPHGYK_z8_1MsGWV30BR6_zqQvEWSvjCcrisngBFqCOuFJqfZf6EoBrPSJaoOdr-9tMq-MHwjpo8E0g8HfVfML-Jva6jqkGMWH3t2UBJzR7JTc6svEhckwo4OdYTm-lHLM-tHR7KeciWnW9D5WvZgCfKF28TwzCgncFW4bQgo7Ntw5yG0qaEWE_xgt1yUKoKdY6VMLw-3WcWNJsMFyz5lycAMGHiV4Ao1B546ibyYmWXci9gObd-3RIKKJ32NRH6wKwRh5Ps6RXu1I5yXmS1B1CNc_iBtZiIc316k2hM_rRLL5ogRBm49IE3seIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f881ae437b.mp4?token=fS2a4bqaf3k1sMAWcX1no_fYi25dPHGYK_z8_1MsGWV30BR6_zqQvEWSvjCcrisngBFqCOuFJqfZf6EoBrPSJaoOdr-9tMq-MHwjpo8E0g8HfVfML-Jva6jqkGMWH3t2UBJzR7JTc6svEhckwo4OdYTm-lHLM-tHR7KeciWnW9D5WvZgCfKF28TwzCgncFW4bQgo7Ntw5yG0qaEWE_xgt1yUKoKdY6VMLw-3WcWNJsMFyz5lycAMGHiV4Ao1B546ibyYmWXci9gObd-3RIKKJ32NRH6wKwRh5Ps6RXu1I5yXmS1B1CNc_iBtZiIc316k2hM_rRLL5ogRBm49IE3seIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یادگاری‌هایی از رهبر شهید در ارتحال امام  @Farsna - Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/439730" target="_blank">📅 22:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439729">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‌
🔴
عراقچی: وضعیت نظامی ما اکنون بسیار بهتر است؛ چراکه توانمندی‌هایی ایجاد کرده‌ایم که در زمان جنگ در اختیار نداشتیم و صنایع نظامی ما به شکل چشمگیری فعال شده است. @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/439729" target="_blank">📅 22:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439728">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‌
🔴
عراقچی: بازگشت به مذاکرات، مشروط به تأمین حقوق ملت ایران و پایان یافتن جنگ علیه ایران، لبنان و منطقه خواهد بود. @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/439728" target="_blank">📅 22:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439727">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75e6544b6b.mp4?token=JRDfx803wRhMvbVxwUefPwyA07VgkgXDBnFUCcJVEj2XUVisot6Pw8Zxrf2UBXj3yaxtMB6Y1UO0s7P3dIsPl_tceL-RYU_5225-s5Pv9ALnzf96hVyG8P95GEYNPSnaa7eZeP9cdhjqn_JhxP7YVfJbLHRjKHzZCHvSA8HmYDiATg9NrzI0NUS5JEyRirByIX3vzztwI_qFywSdME74_HFfgtw-gGhdvbcbR7BdA8creyV-4oHWbeF2ze1CxJqZD833Gm9yTOsNSg8vYf8iNQFCtKT8RTpMoAOxyBE_h0BFWRuHez73pP6V3xw4mn0JMxKp_5zE1icCKhDqsx2ym2UkdkZRr4e5AtndVqEllcpFS7kYsB1-dZwANMg0rNcbLcIGQv5eYGpAoUCQPIPpl_BYsa4Whi_Es-MvHfhMsHCaaRI75EBtpjF2d3U_nNVCydmKrzqRiYRjHSlEAYKi0moofdErehl9Xq6IswVlZACLPkZ_PM1rJjcEqv2g9iX62dU8KK-p7LIv5d4TOUKdeStB4CXH-Hco6T7sJLMkxxWrwmkpjah9Fqhg4jTwk-9XMtF6oLjsNBVr4orxwkKCYl5-6DANZRZwWC4lRVAk5r8DWLUq0FjRfkz6xp1uNQBXQrtthQQ7xjRRQBvdTuYfBRgOq3_U9QIPBeYSK1e4C6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75e6544b6b.mp4?token=JRDfx803wRhMvbVxwUefPwyA07VgkgXDBnFUCcJVEj2XUVisot6Pw8Zxrf2UBXj3yaxtMB6Y1UO0s7P3dIsPl_tceL-RYU_5225-s5Pv9ALnzf96hVyG8P95GEYNPSnaa7eZeP9cdhjqn_JhxP7YVfJbLHRjKHzZCHvSA8HmYDiATg9NrzI0NUS5JEyRirByIX3vzztwI_qFywSdME74_HFfgtw-gGhdvbcbR7BdA8creyV-4oHWbeF2ze1CxJqZD833Gm9yTOsNSg8vYf8iNQFCtKT8RTpMoAOxyBE_h0BFWRuHez73pP6V3xw4mn0JMxKp_5zE1icCKhDqsx2ym2UkdkZRr4e5AtndVqEllcpFS7kYsB1-dZwANMg0rNcbLcIGQv5eYGpAoUCQPIPpl_BYsa4Whi_Es-MvHfhMsHCaaRI75EBtpjF2d3U_nNVCydmKrzqRiYRjHSlEAYKi0moofdErehl9Xq6IswVlZACLPkZ_PM1rJjcEqv2g9iX62dU8KK-p7LIv5d4TOUKdeStB4CXH-Hco6T7sJLMkxxWrwmkpjah9Fqhg4jTwk-9XMtF6oLjsNBVr4orxwkKCYl5-6DANZRZwWC4lRVAk5r8DWLUq0FjRfkz6xp1uNQBXQrtthQQ7xjRRQBvdTuYfBRgOq3_U9QIPBeYSK1e4C6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع حیدری های مراغه در ۹۵ شب حماسهٔ اقتدار
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/439727" target="_blank">📅 22:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439726">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‌
🔴
عراقچی: ارتباط ما با آمریکایی‌ها قطع نشده، اما پیشرفتی هم در مذاکرات حاصل نشده است. @Farsna</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/farsna/439726" target="_blank">📅 22:06 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439725">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‌
🔴
عراقچی: اگر اسرائیل به بیروت تعدی کند، نیروهای مسلح ما آمادهٔ درهم‌کوبیدن اراضی اشغالی هستند. @Farsna</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/439725" target="_blank">📅 22:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439724">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‌
🔴
عراقچی: نیروهای مسلح ما در هر لحظه آمادهٔ ازسرگیری جنگ و ضربه‌زدن به اسرائیل هستند. @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/439724" target="_blank">📅 22:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439723">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‌
🔴
عراقچی: نتیجهٔ تجاوز به بیروت، بازگشت جنگ خواهد بود
🔹
نقض آتش‌بس در بیروت یک تجاوز است و ما به همه طرف‌ها اعلام کرده‌ایم که اگر به بیروت حمله کنند، این وضع را تحمل نخواهیم کرد.
🔹
به تمام کسانی که با آن‌ها در ارتباط بودم به صراحت گفتم که نتیجه تجاوز به…</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/439723" target="_blank">📅 22:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439722">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‌
🔴
عراقچی: آنچه در ۲ روز گذشته حمله به بیروت را متوقف کرد، در درجه اول قدرت مقاومت لبنان و توان نیروهای مسلح ایران بود
🔹
وقتی کار به جایی رسید که نیروهای رژیم صهیونیستی می‌خواستند به ضاحیه جنوبی بیروت حمله کنند، موضع قاطعی گرفتیم و نیروهای مسلح ما آماده پاسخ…</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farsna/439722" target="_blank">📅 22:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439721">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
عراقچی: یا جنگ در ایران و لبنان باهم متوقف می‌شود، یا در هیچ‌‌جا متوقف نخواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/439721" target="_blank">📅 22:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439720">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNv59N2lq-T_tMyMeVQKsicmq8PmWJJQpchUVxJ-Y4-EEs3hGnbeeg1pNA5WhgryIAmOtEOUM5hrDz0DkQ2Kjac93Z-T9y00U6UFd5vJJ6_mhjZCctte6RdRHpSPI-4tikAo7SRpZ__GdCIGGTpMgo1sOymVzmVI2aQby__S45Vtylfoh56-qniWJtYGblCPYT_U5blB3nKo3DJ1HJhdPsf0EUWNhUp-Pi2heyWw82seR3zBE9rNZXrbTvAISzbotWVDlK2FxlbQYk_FMZNSejw1pjfgWXfgIVK69RuA2MoePbzd0t_DmCJllKMh505ojkU-Jx4mF-Q-UzKpWQwxfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهمانی کیلومتری به پاکستان رسید
🔹
بعد از مسیر میدان آزادی تا امام حسین(ع) تمام شهرها و شهرستان‌های ایران درگیر مهمانی‌های کیلومتری شد.
🔹
حالا دامنه مهمانی‌ها غدیر به تمام کشورهای دنیا رسیده و مهمانی کیلومتری غدیر در پاکستان برگزار می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/439720" target="_blank">📅 22:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439719">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
عراقچی: یا جنگ در ایران و لبنان باهم متوقف می‌شود، یا در هیچ‌‌جا متوقف نخواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/439719" target="_blank">📅 22:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439718">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77d31989df.mp4?token=YX2nJZCAmGFs-4Z1bJPc63SE6I3nM2gQfmB01rySdPDdzYT5ACuWZxHGzQ4PRfOPKgTfhi6dao-X4u9NKJEgDlBevB9HTM4XUhdy2BLr573YjFsUEliF88Gy3ZYwy7pLTXeE7-zB5k0A8wYw-klnLbD51-9iwIUQOG1b8Z5k_uR8zMPitOZTgJawiyM-XXoPVEZEM1OTRy0bHKM1wCTcwzV0Y8I75iSau-T6AVlNBMfNNIopMuFVxHe30fsXIlH4Wsz-njDm-BG7GftkwLNKO1cVE68tLiDtt15CCr-idtzinmteegAE6qcmWdSWVs2JoxmQ3uVJZDwf3z6y-997QyetGzp4_dHOJhC5QrPZt7iRGmoF8cu34R9mVQJDO9Zv9b0dOk5yzMntC70V4eTXisZMjkGrjxnZlV_GneqXE8eSwqlmh7CzbacOytruFOISoOzcxXCySYx41PzbLlCO_5xu21FsTNO2Lkqgag6Ba4ljh1V_zr389uw9KETBw29YLJ3UnOWXHufBn137bX5QG7O3IlXS2csWKaWe8uyzhR-2UJYqEU72_jwXtRTKDSs55Az44skq_WN_wXBFAMxm6ZdRUOmWD7NeLv7gClgLEbUeT23IzR2UXCkf_RoCp8FN7EvPv_GOAtiSXv6v2W5sVhnfS9ziVXOtrGjAPtojEXI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77d31989df.mp4?token=YX2nJZCAmGFs-4Z1bJPc63SE6I3nM2gQfmB01rySdPDdzYT5ACuWZxHGzQ4PRfOPKgTfhi6dao-X4u9NKJEgDlBevB9HTM4XUhdy2BLr573YjFsUEliF88Gy3ZYwy7pLTXeE7-zB5k0A8wYw-klnLbD51-9iwIUQOG1b8Z5k_uR8zMPitOZTgJawiyM-XXoPVEZEM1OTRy0bHKM1wCTcwzV0Y8I75iSau-T6AVlNBMfNNIopMuFVxHe30fsXIlH4Wsz-njDm-BG7GftkwLNKO1cVE68tLiDtt15CCr-idtzinmteegAE6qcmWdSWVs2JoxmQ3uVJZDwf3z6y-997QyetGzp4_dHOJhC5QrPZt7iRGmoF8cu34R9mVQJDO9Zv9b0dOk5yzMntC70V4eTXisZMjkGrjxnZlV_GneqXE8eSwqlmh7CzbacOytruFOISoOzcxXCySYx41PzbLlCO_5xu21FsTNO2Lkqgag6Ba4ljh1V_zr389uw9KETBw29YLJ3UnOWXHufBn137bX5QG7O3IlXS2csWKaWe8uyzhR-2UJYqEU72_jwXtRTKDSs55Az44skq_WN_wXBFAMxm6ZdRUOmWD7NeLv7gClgLEbUeT23IzR2UXCkf_RoCp8FN7EvPv_GOAtiSXv6v2W5sVhnfS9ziVXOtrGjAPtojEXI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یادگاری‌هایی از رهبر شهید در ارتحال امام
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/439718" target="_blank">📅 21:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439717">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nvdh2iJ-W46EszlKCZ4n6vAlshVpQyaX51rB7jdxnQdt3Rj9i5LKjMyAuHRCVHJMVSI7S7wP_P1C510KRHRpNeNHD6dfTq7iHFfPb4BC1SiKR3RwqljmfFh4uBK_i3mM9bTVVIwn51O-3doL7In92fMZ6bqqD3F3tf1JRd6FiymOlD16ORsWZCbwZseEFz_fFHykRqr9TNfdAi-vxc96A4-sTkJEaUa_POa4QJFpBWSuEmiMEyG26OLHuZlv0gtfLSoksNDejtGRC_YILRUChBHuh3IC7IPZeB3-soQEhDH3mcA8tSoi6gMheVa5-1dePbUGk_xtBg-M8-aoVcaD7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
سازمان هواپیمایی کویت: حمله به فرودگاه کویت چند زخمی داشته و خسارات شدیدی به تاسیسات فرودگاه وارد کرده است. @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/439717" target="_blank">📅 21:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439716">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQeJJJds4zDAwUhgJUcR75_DtQhwAxOvrI8IUFtK8oFd5_vwqv7db0ZaCRoBy88HrdV7PWzPzjGL6eqSXI0iMxE-g2R3L32U-ylwXjmxhvm6jZoGeb1S1idtsR2NEShftmCDNrPjDaP5qiv1ZspNKw3CW9unCYFw3eQSvAKhIweCTslJ7-LScUfO0DOA7n5_0g6DSpZ2rnkiQiNEOFrJ5ITJ_Ry7MHedC9Zgv2s8Oxgz5NBDobx6900MU7y2w4vF9Okwy22RLV2Zy_CW33sgElUiveOyilLcKQLqKzdsITDeKzptCTACSc08G9CJ373BZgk737VSFeRgnvnQ-0gb6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری از رهبر معظم انقلاب در کنار قائد شهید امت
@Farsna</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/439716" target="_blank">📅 21:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439715">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6372ae9ffa.mp4?token=sQHdM4yENqMcGRe0dYfdSGnKkR4yejY2TiMKGnBO3tCb-cNApz8ir3g_8FGrk9fdEERm3uSb37DGf9ZJJirXF06SKGjWmlgqPzj7znS9ynkGunOG60w5Z0AIPFX_Wn0eGEp4iTwLvMgr5YRLWWwO1NGGL92-4ipYAMyCzjwV5qa8s_chURk03lLEVGNcSb_0r5D-pBCdco49weSsas7COZ5LRBNuSqRaJtePfUskmnatjbeELmX2UrHcrAadJEIuX0MU-uqff-A_b0Q1L-E-cySBE7g33ZK--RDiVYug16TqsST1D8uHlBH4ERbbND06RsF76Ev5LINmJtpQv5pxkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6372ae9ffa.mp4?token=sQHdM4yENqMcGRe0dYfdSGnKkR4yejY2TiMKGnBO3tCb-cNApz8ir3g_8FGrk9fdEERm3uSb37DGf9ZJJirXF06SKGjWmlgqPzj7znS9ynkGunOG60w5Z0AIPFX_Wn0eGEp4iTwLvMgr5YRLWWwO1NGGL92-4ipYAMyCzjwV5qa8s_chURk03lLEVGNcSb_0r5D-pBCdco49weSsas7COZ5LRBNuSqRaJtePfUskmnatjbeELmX2UrHcrAadJEIuX0MU-uqff-A_b0Q1L-E-cySBE7g33ZK--RDiVYug16TqsST1D8uHlBH4ERbbND06RsF76Ev5LINmJtpQv5pxkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدال بر سر «کفش روبیو» در کنگره؛ وزیر خارجه آمریکا جلسه را «سیرک» خواند
🔹
مارکو روبیو، وزیر امور خارجه آمریکا، پس از آن که سارا جیکوبز، نماینده دموکرات مجلس، او را به خاطر اندازه کفش‌هایش مورد انتقاد عجیب قرار داد، جلسه استماع کمیسیون روابط خارجی مجلس را «سیرک» توصیف کرد.
🔹
بعد از آنکه روبیو مدعی شد که آمریکا در جنگ علیه ایران پیروز شده جیکوبز خطاب به او گفت که «واضح است او معنای پیروزی را نمی‌داند.» و این مانند کفش‌های بزرگی که است ترامپ برای او  خریده است.
🔹
جیکوبز خطاب به روبیو گفت: «درست مثل اینکه نتوانستی بپذیری کفش‌هایی که رئیس‌جمهور برایت خریده خیلی بزرگ هستند، تو واضحاً نمی‌دانی پیروزی یعنی چه.»
🔹
روبیو که ظاهراً از این سوال جا خورده بود، پاسخ داد: «نمی‌دانم درباره چه کفش‌هایی صحبت می‌کند. او از چه چیزی حرف می‌زند؟»
🔹
جیکوبز سپس با لحنی نسبتاً آرام گفت: «کفش‌های شما امروز خیلی قشنگ به نظر می‌رسند، آقای وزیر.»
🔹
روبیو در حالی که از شدت تعجب دستانش را باز کرده بود، خطاب به جیکوبز و سایر اعضای کمیسیون گفت: «چطور می‌توانید آنها را ببینید؟ آنها اینجا پایین هستند. ما داریم درباره کفش حرف می‌زنیم؟ شماها دارید شوخی می‌کنید؟ منظورم این است که آیا این کمیسیون روابط خارجی است یا یک سیرک؟»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/439715" target="_blank">📅 21:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439714">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aA--ZuWC54GG1LCr_dhUn3lsCOmsjoAebOc8rFma_AsuwgspUonPcMpvE3VmS3KuFkpTxYLJ6vK-bQI__oYBe6www6V5_SMlj7EHPwWJWKfamFB0iCYWd8MBYjYT9IL6sWsl6iPRGQW4aqkkx0RA-FBqmPfihUeVh5WSrz3eznoH_wotriRHZDbZUf2BBw4rADIOq-PM4beJUNt88PqGtqox6EYHnioBY342LUTlhvVpRhm45lGRYT-3IydJaUV3Iah2D8xr79NXrDud7P5DDCNIdqpGvzV1CwvwD_E-DyErc5xro4_hWdAvE13uhrvGCXClllCRvB_yjeaws7fOgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب؛ اولین برنامه زنده اینترنتی «خیابان انقلاب»
‌
باحضور:
🔹
حجت‌الاسلام قاسمیان و علی عبدی
‌‌
🔹
میعادگاه شب اول: چهارشنبه ۱۳ خرداد، میدان ولیعصر تهران، در جمع مردم مبعوث از ساعت ۲۲:۳۰
@Farsna</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/439714" target="_blank">📅 21:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439713">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35e616ddf3.mp4?token=jLDFDVoryGNfFkXjq95TQMK2HdhgUySfUIpJh6yagSp4JyJkHDfyIoXh11lPjhn10Lmbs1xz5pFljmxj6eSyhdn0ORWRn_yVFPl9SZZds1yeiZvBBA-GCVX15N9FYUeYwcB4SaxlJ6Z6g6tikzINYWXv9XZaRS6GrF9dlnfiyIH255C1187A3w-j1dZJkHTLGkSO8YbPum7FCDIXlfxfKc7WVOXIK8DytV8tsrbSiGSBQSiO2FAsP1QzDZKxHzS0UUHEx3dmOZHY0i8YQm3k9TYeHMZlilEJvT9iBPhWa9440Qa7wARK9CNw8xFNiZLMDI4ZnbglEvBmx0PCJwh-8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35e616ddf3.mp4?token=jLDFDVoryGNfFkXjq95TQMK2HdhgUySfUIpJh6yagSp4JyJkHDfyIoXh11lPjhn10Lmbs1xz5pFljmxj6eSyhdn0ORWRn_yVFPl9SZZds1yeiZvBBA-GCVX15N9FYUeYwcB4SaxlJ6Z6g6tikzINYWXv9XZaRS6GrF9dlnfiyIH255C1187A3w-j1dZJkHTLGkSO8YbPum7FCDIXlfxfKc7WVOXIK8DytV8tsrbSiGSBQSiO2FAsP1QzDZKxHzS0UUHEx3dmOZHY0i8YQm3k9TYeHMZlilEJvT9iBPhWa9440Qa7wARK9CNw8xFNiZLMDI4ZnbglEvBmx0PCJwh-8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نقاره‌نوازی خادمان امام رضا(ع) در شب عید غدیر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/439713" target="_blank">📅 21:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439712">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‌
🔴
حزب‌الله: یک تانک مرکاوا در حاشیه شهر زوطر شرقی مورد اصابت پهپاد انتحاری قرار گرفت. @Farsna</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/farsna/439712" target="_blank">📅 21:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439707">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q8C0mUr5xKlPikSzg6ejwQQjulnw3x8tNGALHpoheLwe2kNkiNkOGmAOlCzPo6sJniFzWsc1BfGSNAzGi8OssmsIB79hl7E8Dnlli093zHkyEJbZ-1gB-SH-NLV5VSX1wIoxNqTdNh2s3PAr7qMqnOW8q-mS8ictzhhXea3XCAGaP_zPIbNoFAym7_EiYOTqs-uysFE4uR3jUKLmV3B56QvB2JkBz6sgNk58oNY1wM35CAHpquohr_NSd9lyvCxFBrddbm_B2rs5lEB0Lsrv1QpaFHRRzBF2xNTXJwA6MGuUIFy1G2tSacKt7FAREzUbH23IhFbx83y9kFi-cPRYfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qDukZ2tPHjL9bDuMKLwufxt5zSR8aeFpf4ZCWmHl8i6IWdOKkcgu9AZ6UBa_nyntbrs8GV74Cfnh3XlN4_k0w8c6KdlQSojan5R9zBtE_6Sc_P9GqyDBJ5OAmaI0BauJltOdTOBD-RbEBqBDLZinYuHFjfclzlKtDgt5sP7WvOPAY2pjHnmXEilMJHeVd8sMJkzPZhJpR_qJYbvbGRuDPlYS4reYsy7NpdjM88Yzg-dT8_nlg2ZH-Nt33NnrtTcUCLEUl2wDftjn559NdIs6WPtnIARn8aVTHJis0vI3gtI_3bhczHCP5hzYGem1Zj1i_HJ7W0UREi0dKYszeUeO5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D4xa-SvWPYEwkxuZCvvwhBaAxBUCUDVnqM_0_QNrf3mY7jQxVdze_OujPhn8bTzfAA-MyLvCItE85G4e5SkJSFyAbLQCgjJ5EnYaXlmahxaXa7eAu9xu66DCdKmgSs-mJf6QUkNWD129PMKtIOtmnKjCl7gCQhFadcTjdSuf8c5ktzxEByr5DYWKui6xONNz0VS_LG9UVf_uE3MqurUdF3NweyyDXLibDjdDhucOnOfaFFw5ee7bk2MA6sJfSf-bgHC0AdtcpwMGq_yhCvY9nRRVSP71xi7O5yE_8pUZhKabeT-jtDIuUDZ-J8OdQD0IB06V2fck7stHsCy0SRxVuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FKCN4njJB6xCb7ROJL4svhKhZXGinotXqTvgiBXliOpvjFhfGSO3KKJnBfc8zBz0JN_WKlu_9UkqySu8pL3EaGC2k_59XcmbxAfTMwTNfbOOKhRz_Ip5jLjSKrhvpW0aN6Th7RHigMr60uILXEvtVgWzYknuGapzD_BijiaPvLpuqK67WN5piBQdJMVYer3VbnEhh0yXhNxmouvIDkg7xh6RCKDEoX0CugegA9DG62ySIK-ZbNfxorYT4lVhK8C-HfdR0MBgJFA0_w-DhalWZB73QsRBpU0A33cKDD6cytz70Y3dPCTgTQU85d9uZ2_e1T7uQV-KZa9zF3PMF64zmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XURKsfRIZ1Yizyaa6Jfip6f9e99q-EXO8sDZG4tYPUA8Dnm0-QpG7-rOzvvJUpvhIhEmlmMhiR02eUSFcOO4Q_IBvrklw-rM_L7-4MHoop6HZDUNNx-sCP6leL_ZoiGvEyexHGNRPdSg91FP7hrWiz2o4OjkGANTiB5aXFJWOUItc_yyl68Hb-_Z2iAJhtschhfJxiQRVRFw82Dpic47khNc3Dik5l6wIekWmm9heaI4iZjgglEomFqH84ev5RBhrqkL1tLOBY7xGvpSJqsrVIMryBtnO10mCv1VMst6_1Dpzl3GRQ8MB6wNsTZzogClq4XA92S4SNygtZGis6ndcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری که فراموش‌شدنی نیست
🔹
این تصاویر، گوشه‌ای از شکوه «مهمونی ۱۰ کیلومتری» سال‌های گذشته است، جشنی که هر سال با حضور پرشور خانواده‌ها، به یکی از بزرگ‌ترین اجتماعات مردمی کشور تبدیل می‌شود.
🔹
فردا، همزمان با عید سعید غدیر خم، پایتخت و ده‌ها شهر دیگر میزبان بزرگ‌ترین مهمانی خانوادگی مردم خواهند بود.
@Farsna</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/farsna/439707" target="_blank">📅 21:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439706">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۵۵.pdf</div>
  <div class="tg-doc-extra">2.9 MB</div>
</div>
<a href="https://t.me/farsna/439706" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">خط-54.pdf</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/farsna/439706" target="_blank">📅 20:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439705">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wA-i7csaV88WwZIw2hRFu60v3-HcDPszmjKu0xDVwoFZXYzSRuUU6xaYpuov4hJ0UmTUiRjepAd7p9nZLPnIYLD1R2de3RNVcK1F_LMW8NVPSMbaCNbiDfnvVxC7DzA36543s9Bmnq0-SqfcLg8xqT4OxDiGJ2dZXf8mTodjgkxciIxRe_jI-jztYP3yEpcftxD8wY35GERkAuxboCq_PPzqudhVz0hVNSFeo0WO5JbgCWwpXWbPABjvO4jFP8bh3nlJG4GHPeb0KM5-OXGYSj3jMCj1SAYAsbK5qcVGth6TITzBuul35_5RYXUacke4u7NHS6BV8anagNihTto9BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان رفیعی با پرسپولیس تمام شد
🔴
با پایان یافتن رقابت‌های فصل جاری لیگ برتر، قرارداد سروش رفیعی هافبک تیم فوتبال پرسپولیس نیز به اتمام رسید.
🔴
پیگیری‌های خبرنگار فارس نشان می‌دهد مسئولان باشگاه پرسپولیس در شرایط فعلی تمایلی برای ادامه همکاری با این بازیکن ندارند و به همین دلیل مذاکراتی برای تمدید قرارداد او در دستور کار قرار نگرفته است.
🔴
در صورتی که اتفاق خاصی رخ ندهد، رفیعی پس از چند فصل حضور در پرسپولیس به همکاری خود با این باشگاه پایان خواهد داد؛ اتفاقی که می‌تواند یکی از جدایی‌های قابل توجه سرخپوشان در نقل‌وانتقالات تابستانی باشد.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/439705" target="_blank">📅 20:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439704">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47bd2679fb.mp4?token=qrwNrKbX-dMCJe31BenhoXIeZE4QUcXroVd0hbb-3wdV7rwZskPHe05UunXFuZUlKcTG7wuR7-xiy5BZMx4_YfjHssmLLy7WOAv5fS75ppP0AcsnCNTV5hIQIn_EYtZC_5sJkVKLP4-nKA5Vuhvj2fN_rNSKhw3YADTwQFH75ynmOg2RgKlF-WcGPQbpJnYMLe9PelHrXbojp9GAYSbJR7Upyv_yEHD6debliO_BvSoH_fljauiCzNnCML-hIi7oHtFbQ7aEl8nw0ckx-PP5ihT7zsXaaIrZ9z5vi_mnTbZwcxdQ0jVSqirv_wc9Okr6El067BwdCLIhWDuyqRVA0CoyKAgHKTEHqOO9AVdHc06fVVQryzRnUAEQV4JGUWck35rjiNkYGyGg4Aa3wCLFoaLaO29fqWXu6fsJYyZYigbfh85PGEKqw3iTc6e_F5n9e5TyL05OGzOof4c52kILOVeEhrxR712tVo81wC7B-aMt3IaGlAmumaGzjiRnY-F7O80g8OXe8ydTWN93xJDTBrUXw6N6s7BhBIPMdwvnbQbJD9_CNp04JRJ1JKuNZz2ABVTJJ0VLeVMGR3CD_lGs844z_SotRGzSCzDRBmNDwfQ2bu4LlFbd0Yb-KQTt3V2aXuWBFCKw7TUv9g3Yd62j1zOrVfwDhLrYTzwKcL4rZtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47bd2679fb.mp4?token=qrwNrKbX-dMCJe31BenhoXIeZE4QUcXroVd0hbb-3wdV7rwZskPHe05UunXFuZUlKcTG7wuR7-xiy5BZMx4_YfjHssmLLy7WOAv5fS75ppP0AcsnCNTV5hIQIn_EYtZC_5sJkVKLP4-nKA5Vuhvj2fN_rNSKhw3YADTwQFH75ynmOg2RgKlF-WcGPQbpJnYMLe9PelHrXbojp9GAYSbJR7Upyv_yEHD6debliO_BvSoH_fljauiCzNnCML-hIi7oHtFbQ7aEl8nw0ckx-PP5ihT7zsXaaIrZ9z5vi_mnTbZwcxdQ0jVSqirv_wc9Okr6El067BwdCLIhWDuyqRVA0CoyKAgHKTEHqOO9AVdHc06fVVQryzRnUAEQV4JGUWck35rjiNkYGyGg4Aa3wCLFoaLaO29fqWXu6fsJYyZYigbfh85PGEKqw3iTc6e_F5n9e5TyL05OGzOof4c52kILOVeEhrxR712tVo81wC7B-aMt3IaGlAmumaGzjiRnY-F7O80g8OXe8ydTWN93xJDTBrUXw6N6s7BhBIPMdwvnbQbJD9_CNp04JRJ1JKuNZz2ABVTJJ0VLeVMGR3CD_lGs844z_SotRGzSCzDRBmNDwfQ2bu4LlFbd0Yb-KQTt3V2aXuWBFCKw7TUv9g3Yd62j1zOrVfwDhLrYTzwKcL4rZtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شور حیدری مردم در شرق  بندرعباس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/farsna/439704" target="_blank">📅 20:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439703">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a467ccdd67.mp4?token=oeFiXuz6iwu9eCOKloG02qjUrkakySBrimtw1lLIFmZfW1x1fgWDbYMbgBnMKqwotT1rD_MlGVltiPmNwaGPWuewz_IwgHqGRyD9DYvuQ153jyx0zlzcRsdwxC9NqDCYOxjpMRH9RZg1K9SL_pvIDJrZF_p885X3GbRI5KXoB7fUFqoLJ8C3FrULOCkwHJXuigIu4Rj-rskl4ooQxTp1IAVncBITFRKaW5nDBSJvNw3MN1rDPfnOs1VFLnHyJ7EfitS9QFvVHRVzAsf2A6LyPDhuFVL8LVhcuOVIFa_l5LIg6yIb78lpX8iaREfhIDW7ehtoLkrkm8Skt9va-w49gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a467ccdd67.mp4?token=oeFiXuz6iwu9eCOKloG02qjUrkakySBrimtw1lLIFmZfW1x1fgWDbYMbgBnMKqwotT1rD_MlGVltiPmNwaGPWuewz_IwgHqGRyD9DYvuQ153jyx0zlzcRsdwxC9NqDCYOxjpMRH9RZg1K9SL_pvIDJrZF_p885X3GbRI5KXoB7fUFqoLJ8C3FrULOCkwHJXuigIu4Rj-rskl4ooQxTp1IAVncBITFRKaW5nDBSJvNw3MN1rDPfnOs1VFLnHyJ7EfitS9QFvVHRVzAsf2A6LyPDhuFVL8LVhcuOVIFa_l5LIg6yIb78lpX8iaREfhIDW7ehtoLkrkm8Skt9va-w49gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خلیج فارس وارد مرحلهٔ جدید شد!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/439703" target="_blank">📅 20:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439702">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🎥
آغاز «خیابان انقلاب» از امشب
🔹
برنامهٔ اینترنتی خیابان انقلاب از امشب، ۱۳ خرداد، به مدت ۱۰ شب ساعت ۲۲:۳۰ روی سکوهای فضای مجازی پخش می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/439702" target="_blank">📅 20:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439701">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zrk7DPG3j5X-LQ3RUmBrP1huHd2vxdt3rtOAhg_9rYW_VIwKbXG4zDVmlw4bBoAIyW1Mj_42E_0MwPnNEeULcWA9RjwYDXAYQ_nM0L4udEaiaRk0OTSbJozz7KNns4P-g8W8urln5bY8RAJknETdPBIvXnLg5xFGvDb6Q6BFdfPV2QU1_-xAt-30CuPQEhXeni7t2--OY9L2n7ALx71DjtM9df74j_NUOMviflJ_78Cn5KRHNpkU10VQsSpfSjeP3jHe0R0R4fiEhg8yyV17JOzYMzszlMXf3GleSYpeQBpD8DhrUwoAW44chi9LdB7xGCrQ761kBbWQJsdFHYrbiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
از اجتماع بزرگ غدیری ها در میدان امام حسین(ع) جا نمونید
📌
اجتماع بزرگ «ایران؛ ذوالفقار علی»
🇮🇷
👥
با اجرای:
مژده خنجری و آرش رضوانی
👤
سخنران:
حجت‌الاسلام مهدی طباخیان
💬
با نوای مداحان اهل‌بیت:
حاج محمد کریمی، حاج عبدالرضا هلالی، کربلایی محمد اسداللهی، کربلایی امین مقدم، کربلایی امیر برومند، کربلایی محمدرضا نوشه‌ور، کربلایی حسین ایزدخواه
📝
با هنرمندی خوانندگان:
زانکو، احسان یاسین، مجال، شروین معینی و سبطین غلامحسین (خواننده پاکستانی)
🔢
وعده دیدار ما:
پنجشنبه ۱۴ خردادماه (روز عید غدیر)
از ساعت ۱۵ لغایت ۲۲
👀
میدان آئینی امام حسین (ع)
@Farsna</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/439701" target="_blank">📅 20:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439700">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GrvN1-7TxlaaxCtpBxhqZkoUPnyW_xj2DjYv_0WMom_IotJwME2P2pX4BMgixpwcN0nGF3p2YpIc-PT9mr8gDhoY1byrDo5dELrQXHPjTt_-dw4fUcW7zAH0rQV4geG85Lgr281IinjdIcdXMT_7Ywnx7GACqKuzOUkR-0yn6aJ49Har3-0wDcOhnJ8m4dUZCYZTNBi1KNRZs2O9hNm0paDV2Znc66CAowKlJXs0Wag38-nR2PckE25nQUlMS5_p7rM0m-MVax8rGZZw2Jo9l-Can_v68OY33vQNJoSulbPWRHIa4sKusmPVwQm88gCXIIObo3-6xOEsJrl7KhixMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
تسهیلات ۱۰۰ میلیون تومانی غیرحضوری در طرح افق۲ بانک رفاه کارگران
🔹
بانک رفاه کارگران با هدف تسهیل دسترسی مشتریان به تسهیلات قرض‌الحسنه و توسعه خدمات غیرحضوری، طرح «افق ۲» را ویژه اشخاص حقیقی از طریق سامانه فرارفاه ارائه کرده است.
🔹
در قالب این طرح، متقاضیان می‌توانند با افتتاح حساب قرض‌الحسنه و ایجاد میانگین حساب، بدون مراجعه به شعبه و به‌صورت کاملاً غیرحضوری، تسهیلاتی بین ۱۰ تا ۱۰۰ میلیون تومان دریافت کنند.
🔹
مبنای پرداخت تسهیلات در این طرح، میانگین حساب مشتریان است و متقاضیان می‌توانند میانگین حساب دوماهه خود را از طریق سامانه فرارفاه مشاهده کنند.
🔹
این تسهیلات با کارمزد ۴ درصد و بازپرداخت ۱۲ ماهه پرداخت می‌شود و تمامی مراحل از افتتاح حساب، ثبت درخواست، پیگیری و پرداخت تسهیلات به‌صورت آنلاین انجام می‌شود.
@Refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/farsna/439700" target="_blank">📅 20:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439699">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/farsna/439699" target="_blank">📅 20:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439698">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e74d018121.mp4?token=Ah_6U8-jMoG6z9DyN27d-uQyUpjYYz9eDKDto9uQOyAoKjJgBR47U5qfPGD_zAhRjMQH5jXYRKmugsHUM2KoeUDolvzCEnO9ioRM_BudH2DLhq7qr8Ap11Gd4_kh2MiWyuaqGcLb_F8ns9jmXCndGU2s3dVY77ur58cs2IgM9N1i746yI2zCneK2JMRz7S1Mn_R1ecGFelSlJWyDVkB7HekMpinaSRr7ayKihEQJJFlk9ECBuIhHZ1GuS4zp83cXG_-vKVUbdHgqmjc4kwAdfhi99hXEXVupQG92hYF4M9GHX6F4JtRWAtSiEkzjfYGUotmw4B3r9DI5Eap0viWRag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e74d018121.mp4?token=Ah_6U8-jMoG6z9DyN27d-uQyUpjYYz9eDKDto9uQOyAoKjJgBR47U5qfPGD_zAhRjMQH5jXYRKmugsHUM2KoeUDolvzCEnO9ioRM_BudH2DLhq7qr8Ap11Gd4_kh2MiWyuaqGcLb_F8ns9jmXCndGU2s3dVY77ur58cs2IgM9N1i746yI2zCneK2JMRz7S1Mn_R1ecGFelSlJWyDVkB7HekMpinaSRr7ayKihEQJJFlk9ECBuIhHZ1GuS4zp83cXG_-vKVUbdHgqmjc4kwAdfhi99hXEXVupQG92hYF4M9GHX6F4JtRWAtSiEkzjfYGUotmw4B3r9DI5Eap0viWRag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توافق واقعاً برای ترامپ مهم است یا نه؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/439698" target="_blank">📅 20:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439695">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QVw6dxC0pbBo6fHEWNFB8jhrB7Qyn4JbExGeyQCuOBN4hrk0Uxytstq95gSiHJnG0_JWysjn_D0f3E0fFmbAJgZvD6YJru9FyPtyEuQGrwFEQh4HboSQktyfDgiAtGgo5WVjw7ZLApIhweIPrylK4TeVxs2dNe_yfHrRe5glZ0muqnUXx86l58A15dJqvDoAsMa2GL5MDCXJOZtTA48GSil0TMvSJySVKvl9As4Mm2ImSPC4nZsHxGp6PrYsQxH6g7WGbMLA5GOOO2lKdfp2KlWboF7p6CRBJKJdiSr7M4hMl-SgcmX-rCf8Whl6sDYcprCWVxUdCkK4Xx2OMVQuaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XFLuV9d3XHTg7D-WJKDgozqBCNZfjfY0ZXU92ZwFu1w2WQaLzWV4u91J1fFOG1lgFq_o6SjFZjd1LJXzCgnmTiXTB8FRglwkqORr6mAKeVHT89a7YKnWsT3HBlFDfFET804crOJ29KNK8F7h3Pre_KWfszlCnr0fY6uNt2MzAgFzE4_RAnNB3v8g9IRSfdZ8VcfzvwZFmqMTC_M17FMDeiOsMakMDnawk2NQRsMxn3h9HEMGl3jGgxRcEb3nexjK_LfaMXDjDck7eBBBNgQjGcYcq1debIqvEcq8gfOhnxMNIpYij9NfXOP_UlithqVl1Xh8p0NXEGECEs_f6pp0dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HG_cHpC9K3jHv7gcppU64SyGxwHBu8nR3jAzpKc6MEvLLaslCOiWD2Ba6z4uWo0c4ZQQBMHCVnem2zP663povJtpMUz49gYkpLnr9gRXHCbz1ihKq3xmuPoc5NmZS2opT9ajUh_OVRXjB5djqULP77aXb73pZLuYNaIQ6Z0WqhZHyC_7S1B3Fye7tn-yCQuuJVge80rt6L8Yc8U3oSH47VlCKuJX3P4-PBvMM43-JOvm-IPNXaRXsgMkXklWF7usQ8JzAptqVtIP2rJovTFgbDvDwa114S4r_YI6o6EVPSbxJkCFjh8lRwcIDgJK0d321xlPBehxINL9SxCseT83_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
نظر رهبر شهید انقلاب در مورد جشن ۱۰ کیلومتری غدیر چه بود
@Farsna</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farsna/439695" target="_blank">📅 20:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439694">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‌  قالیباف: میلیون‌ها سرباز مکتب خمینی در میدان و خیابان پاسدار آرمان‌های انقلاب هستند
🔹
اگرچه امام خمینی(ره) و امام خامنه‌ای شهید در ظاهر در میان ما حضور ندارند، اما راه آنان زنده است و میلیون‌ها سرباز این مکتب، در میدان دفاع از کشور، در خیابان ها، در عرصه…</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/farsna/439694" target="_blank">📅 20:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439693">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">قالیباف: دوران تهدید بی‌هزینۀ ایران به پایان رسیده و هر تجاوزی با پاسخی پشیمان‌کننده مواجه خواهد شد
🔹
رئیس مجلس در پیامی به مناسبت ۱۴ خرداد: امام خمینی(ره) به ملت ایران آموخت که در برابر زورگویی و سلطه‌طلبی عقب‌نشینی نکند و امروز ملت ایران با الهام از همان…</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/439693" target="_blank">📅 20:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439692">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUZwX59FTqOlu2IkN7wC4XgIm80CGgrCCGjXVJREvxo4JlscgR4bCKc3iajb987MXQ-iN9dgnW7_UWVZPu_6x2oV0KChKeH37dQG7wNGcDXCf9khtURb2xRVB2sl6goEAIbzB1DuqG_k4o-jOvOawLG6bU5BqSb6eX40Ok3Dg-PZl4w7g5DyVYnLe_j9KE-eIEjpFAC1Q0nJzhuU1tiNBTTdCHJFbkURxxH9WmDmygt8CCuANO1-QMkwWbRVEmxHiaURBsbNjkNveSbWgkoluVVzHGErx5Zb-4MGXxJbbLk2BPesiU92vO_jS000WdY5oxd9RZsYDfMOEQze9_DzFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برگزاری آزمون ورودی در دبستان‌ها ممنوع است
🔹
آموزش‌وپرورش اعلام کرد برگزاری هرگونه آزمون ورودی و مصاحبه برای پذیرش دانش‌آموزان در دورۀ ابتدایی ممنوع است و این ممنوعیت شامل تمامی مدارس دولتی و غیردولتی می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/439692" target="_blank">📅 20:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439691">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">قالیباف: دوران تهدید بی‌هزینۀ ایران به پایان رسیده و هر تجاوزی با پاسخی پشیمان‌کننده مواجه خواهد شد
🔹
رئیس مجلس در پیامی به مناسبت ۱۴ خرداد: امام خمینی(ره) به ملت ایران آموخت که در برابر زورگویی و سلطه‌طلبی عقب‌نشینی نکند و امروز ملت ایران با الهام از همان مکتب، در نبرد با آمریکا و رژیم صهیونیستی نشان داد که دوران تهدید بی‌هزینه ایران به پایان رسیده و هر تجاوزی با پاسخی قاطع، پشیمان‌کننده و متناسب مواجه خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/439691" target="_blank">📅 20:06 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439690">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-DAFlVtfkxeyxJKF5afBrDPilEcLFROG-256I0BkGhD-FbJD19kX_Z7wUHm_ywXaLpWvHv7l6rRt1NyU0oqa0NmjY6cmppgM4fwmT0s4V_vSRPjJKxxkFHLHWy_Q_HSI5BcZFRcvn-hNyQ9Zx-huU9f4FucjgExJ8BXy77Kn-935IBGETH74_xN92p9iXVBbQnBxX9A5T9wagyuL7f00uCHH5tWBZ413LAmXo4ws7GrGKWrz9xznT0c6-17UAZ48PdAxOuFlCCvFnbOF_xFztquGFaG4mCn2nqF5dX762fMB5akOpHXPB9OnyJzizFG9WrpwcpGe2Cb1_DCr5Ad7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضربه سپاه به شبکهٔ انتقال تجهیزات تروریست‌های تجزیه‌طلب
🔹
قرارگاه حمزه سیدالشهدا(ع) از کشف و ضبط یک محموله بزرگ تجهیزات نظامی و جاسوسی متعلق به شبکه انتقال اقلام گروهک‌های تروریستی تجزیه‌طلب خبر داد.
🔹
در این عملیات اطلاعاتی، تجهیزات دید در شب، دوربین، بی‌سیم، دستگاه‌های فرستنده، لپ‌تاپ و تبلت‌های جاسوسی و دیگر تجهیزات مخابراتی و نظامی در یکی از روستاهای مرزی کشف و ضبط شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/439690" target="_blank">📅 19:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439689">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5rXx96VmWUQid_NmhZ-fDIfFhsqrlBnefYzmJdwWoxmoTi3I28cuCSqP5f7WqlSVMODUcYD89vnp31YQKlanueWYk8lVSWz9ulbKnlrcSXxfKeIbfxA-Wrguc5NJYQiAyvvlU1x5FK4BBHdOcUDiCDbKS44hq-MAMyFunvCPSb3SSORns6RKQrIhI8Ft2IROxulZLLoElxkW_HtGkiK85KRCzPT9lpiVPglBrImFCCPARXQS9l3-FG6SKyjoKHBCop4-lXHQHufYYMJ8WvJD-BG-QeNsq_vHrX9DvgKHPwYO_hlHyeDZP__I4UHzeZWOpi1wzY_lx1Urve-FMZaEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پخش «پاورقی» طبق روال ادامه دارد
🔹
نجفی، تهیه‌کننده و کارگردان برنامه «پاورقی» ضمن تکذیب شایعات خارج‌شدن برنامه از کنداکتور شبکۀ دو، به فارس گفت: طبق روال برنامه «پاورقی» پخش خواهد شد.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/farsna/439689" target="_blank">📅 19:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439688">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_u6IAacDyQR7do3L6BDiJDkbcb_SIoUyvdvt80OnVuN91U_7KapYJw1Grvz452NazvhAeNdVgDhhOHZldSvNNbnvaTw-klang_TJenb_TlHRRv01A4ZCNcLpEksVLjsQ78R8NP2vYYZoSQNlheS-a6IUe8vI_hW63v_2IYpjntZ01gG8qDCvp1ThPoNOm52IdQmQiM3wE8P4A2dAnEh56n9ADsZSGfl4grWUZzCGgW5a7xdZ7jLFd88CFrzH1cmRDKhovbdoqzJaZQyU99TUUpefErHy1IQNVYxDwdbVKRJn0r2NqXhjLWCLKZaDxi4AwJJFfutPHbMToNvYrmDvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: هرگونه اقدام خصمانه با پاسخی فوری و قاطع مواجه خواهد شد
🔹
نیروهای مسلح ما در حال انجام حملات دفاعی در چارچوب حق مشروع دفاع از خود علیه مکان‌هایی هستند که از آنجا به ایالات متحده اجازه داده می‌شود برای حمله به کشتیرانی غیرنظامی و نقض آتش‌بس استفاده کند.
🔹
آنچه با تحریم‌ها و جنگ نتوانستند به آن دست یابند، با جنگ بیشتر نیز به دست نخواهد آمد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/439688" target="_blank">📅 19:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439687">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اطلاعیۀ شماره ۱ ستاد بزرگداشت عروج خونین امام مجاهد شهید حضرت آیت‌الله‌العظمی خامنه‌ای‌ قدّس‌الله‌نفسه‌الزکیه
🔹
برنامه‌ریزی‌های لازم برای برگزاری باشکوه مراسم وداع، تشییع و تدفین امام مجاهد شهیدمان توسط دستگاه‌های مسئول و گروه‌های مردمی، درحال پیگیری است؛ لذا شایعات و برخی گمانه‌زنی‌های رسانه‌ای دربارۀ جزئیات این رویداد فاقد اعتبار است.
🔹
برنامه‌ها، اقدامات رسانه‌ای و جزئیات این رویداد عظیم در اطلاعیه‌های بعدی ستاد بزرگداشت عروج خونین امام مجاهد شهید حضرت آیت‌الله‌العظمی خامنه‌ای‌ قدّس‌الله‌نفسه‌الزکیه اعلام خواهدشد.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/439687" target="_blank">📅 19:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439686">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">دستگیری ۱۲ برهم‌زنندۀ امنیت روانی مردم
🔹
پلیس تهران از شناسایی و دستگیری ۱۲ نفر خبر داد که با فعالیت‌های سازمان‌یافته در فضای مجازی درصدد برهم‌زدن آرامش روانی و امنیت عمومی جامعه بودند.
🔹
مرکز سایبری پلیس اطلاعات فاتب اعلام کرد این افراد در بسترهای مختلف مجازی اقدام به انتشار محتواهایی با هدف جنگ روانی، ایجاد یأس و ناامیدی، تحریک به هنجارشکنی، التهاب‌آفرینی در مراکز اقتصادی و حمایت از اقدامات علیه کشور می‌کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/439686" target="_blank">📅 19:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439685">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cec0d0cf2.mp4?token=HXIQXXE0OKfXSzXnntwbeCpyQ46TCeaWlBFrOP7Ah-2LC-kSELsI0c2gFTiOoRPrPCoe8f59jYl71RVnWQt3r-tYVHXh-IZ9N_NYlGwn0RM0BJTtsjdjNmz-PRemHjIbeqBI148E0hyvUmF0e0Yiyc9rTN-WVjmirFWpRtFLzKrdQygpwyHpEvyPOnXv8QvXK-NT9fs-ZgbnWlkThVjuYiI-as0xD0M0eT85-Np6aiI3n1v-Ij6hWP-jcJsRrw4um9-P6YSWEdXRbbv-MYKEDhBBSOhIMqeOxBAbSr_t7FDWsRERbj5o6CHL5MKMw4MF1Bevgw4AyAJdmypKz2CafQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cec0d0cf2.mp4?token=HXIQXXE0OKfXSzXnntwbeCpyQ46TCeaWlBFrOP7Ah-2LC-kSELsI0c2gFTiOoRPrPCoe8f59jYl71RVnWQt3r-tYVHXh-IZ9N_NYlGwn0RM0BJTtsjdjNmz-PRemHjIbeqBI148E0hyvUmF0e0Yiyc9rTN-WVjmirFWpRtFLzKrdQygpwyHpEvyPOnXv8QvXK-NT9fs-ZgbnWlkThVjuYiI-as0xD0M0eT85-Np6aiI3n1v-Ij6hWP-jcJsRrw4um9-P6YSWEdXRbbv-MYKEDhBBSOhIMqeOxBAbSr_t7FDWsRERbj5o6CHL5MKMw4MF1Bevgw4AyAJdmypKz2CafQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یا علی نام تو بردم نه غمی ماند و نه همّی
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/439685" target="_blank">📅 19:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439684">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMM4L9luaDu6UBWPo_Ghv0vElMWt14qMrr_OvEZnyfHrJV_6ob-nHttxYBwStlUVTZ8uARsKcl6kgQ6rUe02j9Bo23HLb5teC0Af83xPwQUBNulUs4lE5dw0PdZc8AQ5C2PwjJM1uQlEYbAvw-6i4_by6ONsw8rLrWCWef7OcAgZrJ3-_zimgfl-Dh4shL39nhir6esTLlC9u2-9LW5jVFqC1Ac-2EJ_P5ktecnYMzwMUvcJYPpknHjHS8iMquu5c3zWy6qpq96jzv9BgciXfoWd6KeJk6rm7FuGlNO_R4zkHWLP8o4tdsdpIcIKQMRVO9yXkuK0npTMatbnSfjhhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۱۰۰ هزار تخم‌مرغ فاسد در شهرری
🔹
پلیس تهران از کشف بیش از ۱۰۰ هزار تخم‌مرغ فاسد در یک انبار غیرمجاز در یکی از روستاهای شهرری خبر داد.
🔹
این محموله‌ قرار بود با تغییر تاریخ مصرف و استفاده از برچسب‌‌های جعلی، به‌عنوان کالای تازه وارد بازار شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/439684" target="_blank">📅 19:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439682">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa762543f8.mp4?token=tUDttBANCHA088dkE5s2vr_SOi1n-vOh9CHORAetcxP3A3NHgo2kfiFc1iTKT7V1F6HqOK0P7L9y0k_kuLybmd3DA_SlcBLbt-a52VUygAjoDlBBjb_U7I00FRLjzPag34fpNymDbr5fMYZTYluvZ-uveYvegeE148TKFy8A4rLXc9dQ0dPRDohQ_pWcUGpIIkk3f28gPqk-iWPdKo5LBscDm9TSZaSQ-cwUz0EnX3prWZWs38A3TIWbf_bFYqcyJNMyPp8s5NB4Uj1EkU5MqRXyqu6DfDd_BuSf6DPB4tIYfuOEy4rlK3Zd1LVlQlGx0grmMFS_Wv89YmDXzUBuPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa762543f8.mp4?token=tUDttBANCHA088dkE5s2vr_SOi1n-vOh9CHORAetcxP3A3NHgo2kfiFc1iTKT7V1F6HqOK0P7L9y0k_kuLybmd3DA_SlcBLbt-a52VUygAjoDlBBjb_U7I00FRLjzPag34fpNymDbr5fMYZTYluvZ-uveYvegeE148TKFy8A4rLXc9dQ0dPRDohQ_pWcUGpIIkk3f28gPqk-iWPdKo5LBscDm9TSZaSQ-cwUz0EnX3prWZWs38A3TIWbf_bFYqcyJNMyPp8s5NB4Uj1EkU5MqRXyqu6DfDd_BuSf6DPB4tIYfuOEy4rlK3Zd1LVlQlGx0grmMFS_Wv89YmDXzUBuPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲ شکار شبانۀ پهپادهای انتحاری حزب‌الله در شهرهای الشقیف و زوطر در جنوب لبنان
@Farsna</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/farsna/439682" target="_blank">📅 18:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439681">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K32NRaxrG5c3RJRmnAj0zn6Xzv43WOM81xnFebNNnbeNnwRE4hLehCcj_h5rT9quUC3z8wMdT_tdXKk-UfvoBOg91SGhVc0DWp5PbAQ7YmaDoD9hDMfxZ6J2leZ_lYSjgG8KtG3IPuhin9UMZQquYSvr9BW1XdEp1XGkVRFXMtXBZf-QsoxFEyvZxjZIyOjgUiG__De1UykAX16qKuQiaYLuqEWh-nNPSyQAGeGeaF-ey_0nV0Pi5Maz0V2qYjft8xCMsp3iJ2oH6hSNGJgrgMposKMe0eKUoT7b3eUP3wuqaX6aoLygkl-B6rtGWrju-Y0sh2rZdP1tz7Mcsl_8sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمان‌ شارژ کالابرگ خرداد اعلام شد
🔸
رقم پایانی کد ملی ۰، ۱ و ۲:
از ۱۵ خرداد
🔸
رقم پایانی کد ملی ۳، ۴، ۵ و ۶:
از ۲۰ خرداد
🔸
رقم پایانی کد ملی ۷، ۸ و ۹:
از ۲۵ خرداد
@Fsrana
-
Link</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/439681" target="_blank">📅 18:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439680">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7z2-bqSlzht-h2JVYep0jHTt_QzT47EdttB0AKtYEdPDo3LpBg6ZvzdWo9iFFJHvCLaR-TQZCxHh8JhbMw1wYaMurxPj8R9C-jE9dsaYOpgrN5waUVav6BF4OBTcFhbJoA-fPoEIzQ8Ffq2oE4PK418cOPPo_35nWx7yTciVxRG8n1SAgGGSvk_vd37jmClpbbsZwnc-o1ACKUUVdSnjx7ei-RsMXgzrKkCjnQzX4gWwJfPrAhkdSzVzNVeprG5QvnFA9lgi9sMtNy_15de8EwQ1zO-jaRZ5TZwGPqPfnv36Dx18nGJoen7sbhRIS7FeT-xrPUjJAXMdnTKMn9CYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
طرح ملی "کارافن" با حمایت بانک رفاه کارگران به بهره‌برداری رسید
🔹️
پروژه پیشخوان مهارت و طرح ملی «کارافن» با هدف توانمندسازی کسب‌وکارهای خانگی و توسعه مهارت‌آموزی، با حمایت بانک رفاه کارگران افتتاح شد.
🔹️
دکتر اسماعیل للـه‌گانی مدیرعامل بانک رفاه کارگران در مراسم افتتاح این طرح که با حضور وزیر تعاون، کار و رفاه اجتماعی و معاون رئیس‌جمهور در امور زنان و خانواده برگزار شد، اظهار داشت: استانداردسازی آموزش‌های مهارتی در حوزه صنایع‌دستی و مشاغل خانگی و همچنین ایجاد بستر فروش محصولات این حوزه، از مهم‌ترین اهداف طرح ملی «کارافن» است.
🔹️
وی با اشاره به ظرفیت‌های بانک رفاه در تأمین مالی این طرح گفت: ابزارهایی نظیر «اوراق گام»، «برات الکترونیک» و سامانه زنجیره تأمین مالی تولید (SCF) می‌توانند نقش مؤثری در حمایت از فعالان این حوزه ایفا کنند.
🔹️
مدیرعامل بانک رفاه کارگران همچنین به «کارت رفاهی» متصل به اوراق گام اشاره کرد و افزود: این کارت تا سقف ۵۰۰ میلیون تومان با کارمزد ۵.۲۵ درصد برای متقاضیان صادر می‌شود و به‌زودی امکان خرید از فروشگاه‌های زنجیره‌ای کارافن نیز از طریق آن فراهم خواهد شد.
🔹️
دکتر للـه‌گانی با بیان اینکه تاکنون بیش از ۹۲ هزار کارت رفاهی توسط بانک رفاه صادر شده است، از آمادگی این بانک برای توسعه همکاری‌ها در راستای حمایت از کسب‌وکارهای خانگی و مشاغل مهارتی خبر داد.
🔹️
وی همچنین ظرفیت‌های پلتفرم خرید اعتباری «وایب»، سامانه «فرارفاه» برای ارائه تسهیلات غیرحضوری تا سقف ۱۰۰ میلیون تومان و سامانه «رفاه‌کار» برای فروش محصولات کسب‌وکارهای خانگی را از دیگر ابزارهای حمایتی بانک رفاه کارگران برشمرد.
🔹️
در پایان این مراسم، تفاهم‌نامه همکاری طرح مذکور به امضای دکتر اسماعیل للـه‌گانی مدیرعامل بانک رفاه کارگران و مدیران عالی دستگاه‌های مشارکت‌کننده (سازمان آموزش فنی و حرفه‌ای، وزارت آموزش و پرورش، صدا و سیما، بانک توسعه تعاون و...) رسید.
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/439680" target="_blank">📅 18:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439679">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_LCmY69BJrSJP8pMGo4iphNW29tO1K9N9qXFqLazK2sL-wGiBBsfIY_vhiAAKGV3a3w4P-4RIBtrmjSjuHtbu08d34eh7FajqbnzAKEasnu8JDvLoV1y6VtffYG20ARbuJg_0JAz48RxK6zIrkyKSiDXdMdjjCyF22nRf7zpJHdy-kdM-a7dKe-VLYs4DKA-95BNGXAHbpKag3d8YaaAnDJaJb_zJLyVE3LdGPhwtIlf--pZEH3AhEcMe33F0ATNeIJGcaFkYN_SEMNbqTrhA0q4eeTCCTu6NdKz-XDapufPF5gPPeCIVs44jLny060qR1E3lhFSgsjUJPtT8NNvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر فوری: کوچولوها مهمان ویژه پارک آبی اُپارک!
🚨
💦
فقط تا 15 خرداد!
📆
میتونید بلیت هدیه اُپارک مخصوص خردسالان رو دریافت کنید
😍
🎁
برای دریافت بلیت هدیه
روی لینک کلیک
کنید</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/439679" target="_blank">📅 18:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439678">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/farsna/439678" target="_blank">📅 18:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439673">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VW7P_xM6utltARRppqG4lOdfkV7_4DgHmdOL4CAnpcI3og28mRtB5Tsx7YhqPcdI0HMeqeM7E_Utn95qmoWkcLLVEa-DjYBGQA8mCoHzpsP0x0B-gSjeJcTrTh8P2ZT211sbD05pvS-RdNigfRXZoFNbeYmuEY9O4JvTK0xxEINP5P6LumoE1NTZ5c7RT2UXJ3sXcT01TG8Z6ullbjDdAdLDuc8RFFgiq5mfyX78TJN06hzYG13LvxIxE6uKP1YILvDc9NLnx2QT4IHzXSxSM4l9bBKVCEB8u_ZdawmUMEV6PmGNoMgTcRXR9UGQRyO4pjq50P2hJgh3yPHBTZbE4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U8HyTuDSCBEBrmoh_T5XHu6Tj4gqaIE9fOEWhH6i45G6GmpeeW3TpmqyRkKWamu-yJShYlKhQRYULHKbhR6U9sc0oOjI0IiCoCQwvlkHAv1y9GTrtLQSxIM47kIxkxm0AQhxyxsyFSXgQ8OaGeD4NsIcG7Dvvn5oT-ROwOSCoXtz9SJng56Ym-dOB3c0zjWZsGXE92avkg9nkXUMh7TidUfy64hO6hKj7VEsWF3Guo34t1L_dykvy9vcQMRkSQH0--7wxRqesyJTeJ8zSmMqzZScNd6YzNCmRyrlV33uiNtHsUgqex4Xav_OWvkBbmnxz_nbfgYWoX-zFeKrK7SNsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oV7apylLbm_UCvH4FIOrURH5RLU1FVXs4ZXu4r0NBqQ5bnbXQi8klrjILG7nGbb6ANHqqPFtTr-vhY4WMF9MxByo95Owz-mQBCGg73QNEqGZNC_Qzzo4IxaYcdhU1uX5HGAJKw783kW5O-POmOfjOs6cNfEWakhFJQv86rVMVN3bOzwHJ17v1iaeVcdZUU_36dl8-UXrePimY-uxtrRupaQ-pc5jrK-cImu6xVlmMRkR7GdX0j8bsip_csSkXtn9s_xlvPSAYZUuXl3MNOFWnBeklemKfSXWEZXO5wk9V5PkuKyrJ7la_kSFNjJdN79qnqUYAun5J8xN5exV6Dyd1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gbUQvn0cpDQFveLXhCVMPgcVBX7cHxmBtyL5-tFk7Q-YqPba0OPFQxhGuZlUa-32Wx7RsJ_7tnIqMj09intdb_9MTVFKEniXtddjmWfk2i7oCJKYmtAJ4v1kDQNs8koQn03P6Qq5zkmzZsoj7GwmjiXk9JdaFUocWCBtR8sNsETsWUSPZ37QyQ7RDPGO90KjWmpagjoVTseP4Q754DaMZx8uk1aEauGeLjuF6NqSJJ2YvgtPO-YWaRQycRDp2XLA0qIm2e0Oup9Hk-0op3-CxMehwTv82UCq0Wkfa7IHjz_vcI9kPfCiazUR41Ei_R3gNCKGYqcWq2YkqsLrIVp9wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DcL1mqi1zw5uYYJrJtqPK5nP2-3Gw1gEV70k7dwJTet9mv7MPiwlCxzkrjn-LSKYPebW5HyGovVGDHewxjz0PEoQTae0gmU31yFq8fJbohOu_24PHzsu_olvSWL0eOngPR-woQNLLKmUY6ilovELYjHTu_1Sq_DFn_GBYHb3hdKL1_Lsl_a_uwnLYcosZ3Jmzo7kJbymG1A3dEgaDUvnSVMh811_UUCyygTdeRAYvxTgWFrjnA7ky1oPCW_9wE__Mc9BKilZB3Rm16YvRVTx5jaB300FDL3WCVuTU2RaAWFIQJo1u3rY556t6QcvyW-h618ChlOrqrkFHK2Wqo3HTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بازدید سخنگوی شهرداری تهران از خبرگزاری فارس
عکس:
محمدمهدی دهقانی
@Fsrana</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/439673" target="_blank">📅 18:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439672">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgKwc4BxcTNaVXOgKmknqpuT314i-oUmiz2VvNrDYBYuXTx6IfcS1wGR35OjYp0FiE0IPpSTGdJZx3qewhYRWj5JJHl6QKlwAX7pVKw3kThnT0Wb_t0UGDQLNQhnPFWNXBDvLfK7I3Si06aqlaiO8SiObodS3HNwknTitGY22I443qVE-KEFCUlhogsU846hv-9DXvKR-MEwpbYNrJZp5BU8oTG3C-Hl6Y4JtAwvvavj3f_zdDDtQPAUr9b5KyktSUVZOk_RFf_HwiHmd_OMqzFWBB3nBCkTK47RfePClyTehd8sR-hATctj-MGh6Ohz51eh249AtsBiwTDLn1JmgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو: من و ترامپ دربارۀ ایران هم‌نظریم.
@Farsna</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/439672" target="_blank">📅 18:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439671">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8AAL19CabktcUJDwr71Wn7AqDsProCC2Z3ZArweIWvxR6EJWSG1zBnJAHk5h1BiZcBV84F_e3yYU9hqr7nJ_LLxm8i5rc0o2rkEDrSzoEUz-ynJtBFaZzOW29NkPsuoPbqtlEaJQozyXYqKkaMLr3dtkIIaSudQiW-pnzVJOnSI8UMrp-rcLiWfBxXY483fHTwJ5rKYq0-FWu5r6vNtg8kdWo4HaCTcC354W2472PgyWDCJ90PYprJPNPom2uCEGhQH5ntjGU9BetCm65XPMUI_Rg_hq5__WOxhu7r0ueu3h5mHQyfSkDFf3dpyXvA1I5w1tspsu-lY9O0rKAMNDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳ نظامی انگلیسی در اثر سقوط بالگرد کشته شدند
🔹
سخنگوی نیروی دریایی انگلیس: ۳ عضو نیروی دریایی امروز در جریان سقوط بالگرد در یک تمرین آموزشی جان خود را از دست داده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/farsna/439671" target="_blank">📅 17:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439670">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">خبر خوب برای والدین شاغل؛ ثبت‌نام دانش‌آموز نزدیک محل کار هم ممکن شد
🔹
وزارت آموزش‌وپرورش در دستورالعمل جدید ثبت‌نام دانش‌آموزان اعلام کرد فرزندان والدین شاغل می‌توانند در مدرسه‌ای نزدیک محل کار پدر یا مادر ثبت‌نام شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/439670" target="_blank">📅 17:43 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439669">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‌ حزب‌الله ‎۳ تانک ارتش اسرائیل را منهدم کرد
🔹
حزب‌الله: در شبانه‌روز گذشته ۳ تانک مرکاوا در منطقۀ «بالوع» مورد اصابت قرار گرفته و منهدم شدند. @Farsna</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/farsna/439669" target="_blank">📅 17:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439664">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fCaVxXG8Z4C2VE2E4qfCGC1UadqMygYAKMH2dZINWBhQTZDKbvPy5KSNqAQRQcQLWeGfQmiHK927m5BatCI-LZNlXV5798tL6c4YhSgTNZ8Od6n3kikpEJkcYTa1d87QwRfMd5bTW7T8sc7JQ3ybTyv7tNKq1ON2S_ygQzp3eVjbPMMeanylIi5jnEjnFQXZNTY4yhYMSXli8ONtb1Xnr26vt8LSZFGx3uUUT2P2RqWrVl9f7Xlx5o0xVajDTjoxs1EhazF47SXIZbQrbXDSQ-MGcb7Dsv80obG8ws-gMP_KDNWp0sR6oRhAr9GsyshpBkSPO3QDqcuTH3gdchWogw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ePu0AjMyD4Z-4BXBIC4XZHxxFGv-r68x2_4p66ZeeAPvAKhnWqLoHNVzWrJ6K2Mj-tNOgy7lWcRjBZDGaPLj-e4_I_rkxl2qoPIZkksg29OAKIGzl1Cf2xR1A1C1v77dmbh3uItJKDqxnWM-clsWPgoAuOxd5aGoyU1251dRxio6mrwYRbX5Jaz3wQFw3DGKzPNIUgnJdCSXSATyF7Gofn4e-yoV5Ku6At3Np4dE6RNbre8xSiqOIIbxfcCU-MlQgLcVXmcUY_U1XORK_P6M6s5jL733IW8qbqjBp2HbkJp2pJWksOiRWwCWOBxBtHrDDGpETtAmQr_yTtIidvENzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CT6JA7jZ9mYsrL_B23oEhjTEakMqpPfArlaaqo7btfu97js54_phuPlix08U3epttxhubxzRGc8vKjeMlQRplRKnKhV5ZagMvnz5zLWnWWtRfzNgdPeNH7Co8wBE3peh1zffmiPb6IXqZ-fJt0ydpBo9_7-P67S8z41qiROsuIJyBu4WufLO-88u_GYrgK9xyYntm5g3a70iARmLpZk3fp0HLfh_AY4488Z3q14n5tS9NeXlk45Kn-f1RqSQb1HOKFjEkRg_EvotaYOqGPqR072yFOZmZG1IhxchTFMOiIKZwuUCHQS9Z2Ug51SFR94vU5QY9DwMHJTNCohxPfFDfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/icQkJsO8QQqnhnp98mnOYIos4At4OiChLinDfkwl9GtJ6p3Qu9J_2z5zyDxQmHEtMo5d6fxbOEjg3th5Ow70Vfv0HvhzoH3F867j41CIN7-vDN5NG6xM_nOQnScDEt12cJZcvwvMoqCNfSwnG5khwVp51CrvFOFOE87kUkbwKWg2ByPlhtilmXgLqtxLjF-nOTlr2aLOPSTq2wnYM--0bgpbMpoheGEhGbI5Pod2Km0OIhE74l4Kxc5yzYLjQH0ZcMy3IxJD-gswRDg1LTbCccDa-XgHpz9AWp2D4z1vuTKlTvhiAD98FtDsv3J4fGTjJjWuslPkWxUDzGQvf8Zkjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J7lZFKHL-3oc41xuz_sNaz67oglxmN6hVhF2TgsWxDTAvq3FHzth_uizgdcGZFlnnAud0FUs5ib72H80VxyobYz53aSGm8NWp9bEATnqHAfQL-HF7FplUPQk9Gpaqw-CEvqw8y8Oz5ygdXCHTfyNDLxsR7uCrqrYHA67SdldwJGlDqD1-0WV_d9eed1nhePyRSKtX3EpCmQheiZrmenz16VfV3nSd7EEJtZpZvfUGL7Xr8HQC-CdNQF5p7UHUuWgzdLtzpNjBik7lxTe8HCyD0mraB58Y9tiRW9i6bIntSHBexx8CvbXAf1s8WM0pOpWPEsUffiRzIvxs03TY8WUbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قاب‌هایی از مهمانی ۱۰ کیلومتری سال‌های قبل
🔹
فردا عیدغدیر بزرگترین عید شیعه است. برای خلق زیباترین صحنه‌ها در پایتخت شیعه و در جریان بزرگ‌ترین مهمانی خانوادگی مسلمانان آماده بشوید.
🔹
همزمان در تمام شهرستان‌ها مهمانی‌های کیلومتری برگزار می‌شود و حتما دست پر بیایید تا در ثواب میزبانی در مهمونی ده کیلومتری شریک باشید.
@Farsna</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/farsna/439664" target="_blank">📅 17:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439663">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e31c543a50.mp4?token=vQmvq5BcTz1q9WO_JSMJTbE95W55w-GinaEg-YFfZYFiyWBOmieLKBFFbc8dSv1_jRh5sJtMesc8W4Dtp7x0n7G5MRF5HShhyPzhQqH0gOv-BOrLcFNMJd7ljDEUuunJOu1YUzbClmfeStpUv1TErFPR-5YnMg7walXkekOBw__S3i87VufBvRWn4b_toKUUEtdwhIFzhKjCItoAb2-zKrEcgO0m7FIzoX67U1NiDHsa6V3MmPi67lQiPg870AYA6n-mW8ZlO9MF1a7qD24RBzKQK4oKhKSCb4orMZfOtrND48CBNmy_ZF-qpQr49v8a26_4YzPF2I4THyAWlka1BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e31c543a50.mp4?token=vQmvq5BcTz1q9WO_JSMJTbE95W55w-GinaEg-YFfZYFiyWBOmieLKBFFbc8dSv1_jRh5sJtMesc8W4Dtp7x0n7G5MRF5HShhyPzhQqH0gOv-BOrLcFNMJd7ljDEUuunJOu1YUzbClmfeStpUv1TErFPR-5YnMg7walXkekOBw__S3i87VufBvRWn4b_toKUUEtdwhIFzhKjCItoAb2-zKrEcgO0m7FIzoX67U1NiDHsa6V3MmPi67lQiPg870AYA6n-mW8ZlO9MF1a7qD24RBzKQK4oKhKSCb4orMZfOtrND48CBNmy_ZF-qpQr49v8a26_4YzPF2I4THyAWlka1BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سفیر سابق ایران در لبنان: نتانیاهو تلاش کرد با تهدید به حمله به بیروت در صحنۀ جنگ دگرگونی ایجاد کند اما تهدید ایران باعث عقب‌نشینی صهیونیست‌ها شد.
@Farspolitics</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/439663" target="_blank">📅 17:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439662">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCTz9ai0tFwfjbZOFDkBlBFrwNaNzpBdESRSK94ikNsm4bfx7R8Zg76qLpdW4VLOFLDJAbl1_THLIaXBimmjZaj6JBZWPRaeLc35OmWaocH0ffZQ9LqR5Q-g8P9u30FEH3ZsKIf68oO0bLOaTbKLMXt_x6r3fuFkqMKbcHFd4f39yiqx1eG4fbUQah5Vt5Qsw0TpGHsqeXCHX-RotwCEUQbU_J2kpg8QBnjC49Uc11Wgmo-CfSW8UDzIfYDCX9rbNMqDvq0vxp-ECyQ6u8prxuzilZFUGqYqtJBME50GhydvyOVRnJ-iBdZipW4rxDY3fc230yllzv648edRnN1igA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتراف غرب به توان مدیریت محاصرهٔ ایران
🔹
شرکت رهیابی محموله‌های دریایی، تنکرترکرز می‌گوید: وضعیت ذخیره‌سازی نفت ایران بحرانی به نظر نمی‌رسد.
🔹
شبکهٔ خبری بلومبرگ ساعاتی پیش با استناد به تصاویر ماهواره‌ای نوشت که نفتکش‌هایی که در جزیرهٔ خارگ پهلو گرفته‌اند…</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/439662" target="_blank">📅 17:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439661">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">تصاویر آسیب‌های شدید ناشی از حملۀ ایران به پایگاه آمریکایی علی السالم و فرودگاه کویت  @Farsna</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/439661" target="_blank">📅 17:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439660">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5s5CgtYSLmparfn2aUCWPx7_Te3D-274O4R0xzLWEekNsGUvym1rts8Gv6orADjf_1gnzkfRQqVHEPivxRx4XODuxFw8b5-fAUFvc_4sqcaVEWJBsQKiintF-axPxJRg0f5GiSWWIcRV-4KYpVgxbaH5V6AVEsQqzXnSFZNe96-wYACXNi3pFVAmKOcwWr6xgo3VB_wr5vuzgkEOwpqy-0bXqsO-_6UN10nLszyqHu0I9-O5Z-tcRDMn-qydI-eGU9SIWespyponGnzK2CV7FPvXs3QZizgJuGC6NYyxDtFMSNwmL9la3TnnbUGfWcR2SG6M9eKlCMBLN7F8Hc7tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برپایی بزرگ‌ترین شهربازی دنیا در روز غدیر تهران
🔹
بزرگ‌ترین شهربازی دنیا در مهمانی ۱۰ کیلومتری روز غدیر برپا خواهد شد. برای درک ابعاد این رویداد نگاهی به بزرگ‌ترین شهربازی‌های جهان بیندازیم. مثلاً خیابان اصلی «مجیک کینگدام» در دیزنی‌ورلد حدود ۱.۵ کیلومتر طول دارد، درحالی‌که «مهمونی ۱۰ کیلومتری غدیر» بیش از ۶ برابر آن است.
🔹
حتی اگر مساحت پارک‌ «فراری ورلد» در ابوظبی (حدود ۲۰ هکتار) یا «پارک والت دیزنی» در پاریس (۵۶ هکتار) را مبنا قرار دهیم، این شهربازی خیابانی با درنظرگرفتن عرض حدود ۳۰ متر، مساحتی در حدود ۳۰ هکتار را پوشش می‌دهد که رقمی قابل قیاس با ده‌ها پارک معروف جهانی است.
🔹
علاوه بر این، ظرفیت پذیرش مخاطب در این شهربازی خیابانی به مراتب فراتر از استانداردهای جهانی است.
🔹
درحالی‌که پارک‌هایی مانند «لگولند» یا «یونیورسال استودیوز» به طور میانگین روزانه چند ده هزار بازدیدکننده دارند، «مهمانی ۱۰ کیلومتری غدیر» با ده‌ها قلعهٔ بادی بزرگ، استخرهای توپ غول‌پیکر و صدها غرفهٔ متنوع، به طور همزمان میزبان میلیون‌ها خانواده از سراسر تهران و شهرهای اطراف است.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/439660" target="_blank">📅 16:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439656">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vqN8x2uPcT-9Bi6DgJTs01yH7ZqLz_IDUfSyjV3bD60SDMua2UdDdqbNGUwNhSYCQ5AXceCUxHNhgyTnwq4pwSC9oGlZAt1iJaTazsr-WRzx0szKPyFpl12JVDWvN4Ec2zyVx6sbSgGcg9RvxDNj9PpVokFPbMSmYPCbxDGufqwyilmv_g1x6mwtPNwSmFnEHe-gYIEl6W553-5uzDIGxWtmcBoVtRJz026u5Y4bt20LRxG1cSJwjYSGnTsXeiQoH6kaW-a6-2zGzLUXL4F6ZvZDBUIed3H3hXRQ38OrgKMvS2z1e7PkBb11hwm8aCgBQh2aUceS9hQ30SEzHJ8t0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mblQanvtCYHfES9W-quDWIlEZ6_aw1yypEn3-uiV_GfwokKciJdFUvjCmZ0NWg2V3fv71DqAxiw77QBIPLLAjmSd7oKDMDnuK6_IGTmM3jRKA3nCXi1tSHzrzpbSYkBp8BtyxuvjHMoUT00QGEQrrdnzKcrc2QjQyGP1fUjE5VWDHuzzYajahOa7uH7EwtbGuwno7595e2et_32VB1UgLLi5A2dSFxk0U3oU8ot2qupGVYtK_I_NYXmoVvK3feLlBeNmb447I4YiFnwnZZFo4ptWRpchX_ANSrfl2BXRRCLQFGZPBSBkv0Pa0kE3wDaaYU13FGHtcx4ETnpjEaidNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d50b1bddf.mp4?token=RWa3I9xGk53_ILAfHLzRgWOw7khBUs9cM2Xs_eeUXRysr0EsV8LfPjQufZ5tzeQ19KkAEkwWrG5F1NbtfDT7UskxQX-KaGy_vOK3BaBHEIBSHpj6JDQlaSqavxzfevZCpTK9SjHlYzV8Avn97nvVFWYIxudJ2gPZVJjJmrPydB9d-vAN3m2fzfBzSgWtagZxCtvrnizEXdtOPY2kkdXcdYNjJrat9Qw7-RKaJuXCfiyOhmVtp32afnGIH6fpiVMT0meRCazydmcRN_Hgwn-ITJ-wStrqx4-hQa3zntK-PiiiGOw3ixcKOPlBGc-_Q_LV2qJb1yuhjBueosJSZXfArg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d50b1bddf.mp4?token=RWa3I9xGk53_ILAfHLzRgWOw7khBUs9cM2Xs_eeUXRysr0EsV8LfPjQufZ5tzeQ19KkAEkwWrG5F1NbtfDT7UskxQX-KaGy_vOK3BaBHEIBSHpj6JDQlaSqavxzfevZCpTK9SjHlYzV8Avn97nvVFWYIxudJ2gPZVJjJmrPydB9d-vAN3m2fzfBzSgWtagZxCtvrnizEXdtOPY2kkdXcdYNjJrat9Qw7-RKaJuXCfiyOhmVtp32afnGIH6fpiVMT0meRCazydmcRN_Hgwn-ITJ-wStrqx4-hQa3zntK-PiiiGOw3ixcKOPlBGc-_Q_LV2qJb1yuhjBueosJSZXfArg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
وزارت بهداشت کویت: درپی حملهٔ امروز ایران ۶۳ نفر مجروح شده‌اند. @Farsna</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/439656" target="_blank">📅 16:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439655">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c4bedeed2.mp4?token=UWs_lPO2YcHeIhZX8j48Po6JwyRoo1Tz8r9EUcZesM2PgmVlPxfV_oMvxNKBr7qX3o6onB93vF7ZzoZo0_CIadoMmnbEXamj0wzIqdsB2x8MlB_fuVEPItM6-MWtyB7X9Ufo0MFZeUHYUP1zw4wiVWYOglRQF5IMi0v8D1-noiV6xkPaGbhI_JwBeZT0Wnis-g23nnyQcC7Xz1P4XuflmMKk7YHkcNrllQaSHcz5Z_lpOojp6hetWQYZwXFK8SrbzOJoqafRas0moyiZv3dTgcU_43nX98BpvFgUVD2mpNxTej5xhBUNRE1FTkjZWEZXm1Pwj6toE4sdWmiw3VOttA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c4bedeed2.mp4?token=UWs_lPO2YcHeIhZX8j48Po6JwyRoo1Tz8r9EUcZesM2PgmVlPxfV_oMvxNKBr7qX3o6onB93vF7ZzoZo0_CIadoMmnbEXamj0wzIqdsB2x8MlB_fuVEPItM6-MWtyB7X9Ufo0MFZeUHYUP1zw4wiVWYOglRQF5IMi0v8D1-noiV6xkPaGbhI_JwBeZT0Wnis-g23nnyQcC7Xz1P4XuflmMKk7YHkcNrllQaSHcz5Z_lpOojp6hetWQYZwXFK8SrbzOJoqafRas0moyiZv3dTgcU_43nX98BpvFgUVD2mpNxTej5xhBUNRE1FTkjZWEZXm1Pwj6toE4sdWmiw3VOttA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شیعیان اندونزی درحال تدارک برای پیوستن مهمانی کیلومتری غدیر با نام ali day festival هستند
🔹
امسال مهمانی کیلومتری غدیر همزمان با ایران و مهمانی غدیر تهران در ۳۰ نقطه جهان برگزار می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/439655" target="_blank">📅 16:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439654">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4141858b06.mp4?token=Gu23_YJyrpxs0Sy1ip66LAzLzgTEat49mMDkMdsddgvpZORH0tp_9fTstIDc4pFLh0iQLZNdKZtNk8g3mIXT69t6LD2MUVd2QYg3Qm3bShlor_6uBW3ZGHAzSNI-XoR0DT2OgxrRhDgML802I_F6MG8XFIMg6w8VJc5gataaW6K8LYlAJgwS7hpLCeE6fJT6jRwskWaIeufV-4ATTUtsT_eqHDA1xtW954hKwh0Xy4U0GiyWVOXk8tOBhfgwpqIn68KZScCiV7tkILHj0-mny_C7NohmuEjgmx5A1km6AfTJ1Ugzc_dE6pcbK35_0HftGJl2mVy7V68FvztL1cZAVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4141858b06.mp4?token=Gu23_YJyrpxs0Sy1ip66LAzLzgTEat49mMDkMdsddgvpZORH0tp_9fTstIDc4pFLh0iQLZNdKZtNk8g3mIXT69t6LD2MUVd2QYg3Qm3bShlor_6uBW3ZGHAzSNI-XoR0DT2OgxrRhDgML802I_F6MG8XFIMg6w8VJc5gataaW6K8LYlAJgwS7hpLCeE6fJT6jRwskWaIeufV-4ATTUtsT_eqHDA1xtW954hKwh0Xy4U0GiyWVOXk8tOBhfgwpqIn68KZScCiV7tkILHj0-mny_C7NohmuEjgmx5A1km6AfTJ1Ugzc_dE6pcbK35_0HftGJl2mVy7V68FvztL1cZAVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرم امام علی(ع) برای جشن غدیر گل‌آرایی شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/439654" target="_blank">📅 16:43 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439653">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5371cd0bb.mp4?token=H7gi-pNDBLXfvCnfERsWPwKe4Pywaf4h5hvb7kiqM9QXMXH52S5txAdat8CxrlbiA5gPGZL3uZTXneatXi_2z41GMCo3siyWmxqpw9cxWijNBmLtnWDsReCPvLmxTXwbHhjn8VL-k9LyxYkKVbyAVut8TdeQsVtJm45DuN-d-5CK9rO8VMk1ZMPkvYj9zmIK95XOOgAk64m18fvbcFZ4phWFOBGV2hovISZQcvxuq5hyJiZlj71AFL3n0h0gim2zHInR5LlzpA5DiK-AxghnAOkouCciOK3Vd20NZcRkK-TsbcoFjApaHMRn6pCNkXVRtSREvaOQcoftdir1vSUeVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5371cd0bb.mp4?token=H7gi-pNDBLXfvCnfERsWPwKe4Pywaf4h5hvb7kiqM9QXMXH52S5txAdat8CxrlbiA5gPGZL3uZTXneatXi_2z41GMCo3siyWmxqpw9cxWijNBmLtnWDsReCPvLmxTXwbHhjn8VL-k9LyxYkKVbyAVut8TdeQsVtJm45DuN-d-5CK9rO8VMk1ZMPkvYj9zmIK95XOOgAk64m18fvbcFZ4phWFOBGV2hovISZQcvxuq5hyJiZlj71AFL3n0h0gim2zHInR5LlzpA5DiK-AxghnAOkouCciOK3Vd20NZcRkK-TsbcoFjApaHMRn6pCNkXVRtSREvaOQcoftdir1vSUeVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آب زاینده‌رود به اصفهان رسید
@Farsna</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/farsna/439653" target="_blank">📅 16:38 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
