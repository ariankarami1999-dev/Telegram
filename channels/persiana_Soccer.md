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
<img src="https://cdn4.telesco.pe/file/mhddfIF3UZKE9MMdSea_W9XeWiN2X-PfYZhxvkIO5zXSVO0j1dOYskuhDb0HvGT6H_pXNGgNHXup8ueXqzWKJQ1eHL2Krx4VP6bjyjXIsMIuRw9fAjnwGYgQGcRLX81TlsJ75MS84c87V_-_rDfhcC0KLfLg-QSlotV7z8El8LuyXhnxM7QI9_XLHs155cLAD-dwZlKby8bV6DxTAm_cTuuGekOe4f1qbk88rejd-vwh6p4Tv7yZ8_YzbxUrGZ1WY2Wps145AhpkBs2xUr_CQcVQl4g3VCtMMrjMBJ9quHNIzkwzgpF4QjDQBq27NJpqpaYnzBkCCGh0Fxy8MBgrvw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 513K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 09:43:41</div>
<hr>

<div class="tg-post" id="msg-25908">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a632b00c8c.mp4?token=BTKegEayNS-sY-VlkgllDL0j6oqa4BlHxaH_bgMkOwMHkSvyTXL37ucBFwOsveG9x_d5870Jj8vp7f9mLcy-3VbEK1M9eFqZhFtFm6jVwyMQ9szBC5ucUzpn-To0H1JuMOY-7obsSH6f9okh3NA3R2gq6oZa3fun4PL5TC0YM4eCrcf6h1kjilmJucvp9zo3Fl5tXfLuXMaY45IfraUPtFOVGNIR-axOLYdFeCwV-lXPNapzcSaMQJPhjqExD6hSQNkUoqv8fO-kJXF6QaO2oicEgBeW21eHRxxZqJyjQ-lF3HiFjnJklP-OLwfunaNsH_2gv2rMEXnyf-uTdtVKSL5-dEEkBqsa03stfr6lsr5qSAIE232I95-kfR51utB0s4-TNG3V2iSy9iPCPwzZZSBmri3f-W6TArJekP4y3ne6Mj4cyly55UT6kIbjzJWPUnMBfpeZMoXQznN-pAn1N-IQqghQkzgNGdJt9J5IFx79Kxz05hGM7BVCGFGeb1kPK9EwI6XJveLsBGbgfVy16SAbBOd5g_g-5wUYUZSmSG-43r4MvfrpEIHKWbRq0j1v8T9mgCrUJ1GZUSE5WhOZJxvMWdcRtbbxlQsimwOJ62ReON0jHr-t0AOQIJXVCY7TJHdDe3HxyXhDdrlFg9KjbV8AKdZbpZN_MjykGZknRNs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a632b00c8c.mp4?token=BTKegEayNS-sY-VlkgllDL0j6oqa4BlHxaH_bgMkOwMHkSvyTXL37ucBFwOsveG9x_d5870Jj8vp7f9mLcy-3VbEK1M9eFqZhFtFm6jVwyMQ9szBC5ucUzpn-To0H1JuMOY-7obsSH6f9okh3NA3R2gq6oZa3fun4PL5TC0YM4eCrcf6h1kjilmJucvp9zo3Fl5tXfLuXMaY45IfraUPtFOVGNIR-axOLYdFeCwV-lXPNapzcSaMQJPhjqExD6hSQNkUoqv8fO-kJXF6QaO2oicEgBeW21eHRxxZqJyjQ-lF3HiFjnJklP-OLwfunaNsH_2gv2rMEXnyf-uTdtVKSL5-dEEkBqsa03stfr6lsr5qSAIE232I95-kfR51utB0s4-TNG3V2iSy9iPCPwzZZSBmri3f-W6TArJekP4y3ne6Mj4cyly55UT6kIbjzJWPUnMBfpeZMoXQznN-pAn1N-IQqghQkzgNGdJt9J5IFx79Kxz05hGM7BVCGFGeb1kPK9EwI6XJveLsBGbgfVy16SAbBOd5g_g-5wUYUZSmSG-43r4MvfrpEIHKWbRq0j1v8T9mgCrUJ1GZUSE5WhOZJxvMWdcRtbbxlQsimwOJ62ReON0jHr-t0AOQIJXVCY7TJHdDe3HxyXhDdrlFg9KjbV8AKdZbpZN_MjykGZknRNs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه جذاب شب گذشته عادل فردوسی پور با حضور علی آقا دایی و کریم باقری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/persiana_Soccer/25908" target="_blank">📅 09:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25907">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNaPvHacwpkONmEjfN2bRCaVKumIQEdf9e1u83_jpMATT_27AwNhN4xfRrfesUecteKDdSHczIwZv1U3aoKtR_IwG87eotZqVvuVva0yhvCON7mCwK94GwCoOTF3r6eUnG2o51rBvLZDwwftp7AagcMWIcU6mJSOMK92w8J8CwILnZ2vSYqpXwzP_I_hIaWsDxEtjeWvKPhGZASEYQ8qP1NKkNv4BBCqyHf3sStlqDVlFuSAhtNaeJqHy91wqUyMpOjlGhNiWBiD81aOL9TWZOwunFtZ1zvYncAVvrizWtW72j9tuc-iVCPUJM735CXZ2sSbFKRknGXBeCPXfjY-Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هدیه بسیار ویژه فیفا به قهرمان جام جهانی
؛ برای‌نخستین‌بار درتاریخ قهرمان جام‌جهانی «انگشتر قهرمانی» دریافت خواهد کرد. این اقدام با الهام از سنت‌های ورزشی آمریکای شمالی انجام می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/persiana_Soccer/25907" target="_blank">📅 09:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25906">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f9c92951.mp4?token=lbZGUJ1IE9vrXjDzZ4N-cvmW1YMYNG3jDf0GjoEXv9MI6DNhXcHePSTYt9TDnAJDGelM8rAQFWdK2691YBoSY2Cyz58RO2jnOFH0sR8wPsH9w25konzl-D6nrZRpPqoFuwaMrBxZdl2c018Y6pHtA9H30joHV-VzRiQejSI6m2DclFyve6Z1a3-60LpuD4OqY_kEcdZ3jVFJivYNy049a3TcKW_V9EzEATTK3JP5QIGNjSCv1tV1uUCgkbdY1056ObdfBGGr2exj3AAlFOjk3dlSOvZ-pvcHFEJq8oLCOw3_MGO1Vr1CdPZ2KHGAKpR_sToEw6Ak004y8_JKlYeKUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f9c92951.mp4?token=lbZGUJ1IE9vrXjDzZ4N-cvmW1YMYNG3jDf0GjoEXv9MI6DNhXcHePSTYt9TDnAJDGelM8rAQFWdK2691YBoSY2Cyz58RO2jnOFH0sR8wPsH9w25konzl-D6nrZRpPqoFuwaMrBxZdl2c018Y6pHtA9H30joHV-VzRiQejSI6m2DclFyve6Z1a3-60LpuD4OqY_kEcdZ3jVFJivYNy049a3TcKW_V9EzEATTK3JP5QIGNjSCv1tV1uUCgkbdY1056ObdfBGGr2exj3AAlFOjk3dlSOvZ-pvcHFEJq8oLCOw3_MGO1Vr1CdPZ2KHGAKpR_sToEw6Ak004y8_JKlYeKUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های سنگین کریم باقری: مسئولین سرشون شلوغه. علیرضا بیرانوند خودش یه مجسمه از قلعه نویی درست کنه بزاره خونشون لذت ببره. علی آقا دایی هم میگه نگو بیرانوند؛ بگو دکتر بیرانوند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/persiana_Soccer/25906" target="_blank">📅 09:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25905">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edde05bb69.mp4?token=KTZhLVcTAPthEMobUczpJo_QlTnYDs3DgYZkmmZhnCW6r_hoGus_mJ_eNxOVaai8IOJjQoiPi0XKwoslY-eJAu1K-J4Jd0fS77DzeUgcO-ttauFRGDa4eB61IntgpZUr6lV8FarZEsQca8Xjjsspznzx26zgzN0K3GHQE8-MhE-d5XAeeANB51q9-I3dLJF5FAb8W1GgJrvRj30nLolNqT2olt7vKMHS11uS3XIOeFm498Y7J5kxzKQMDA0s1333EzXPVTwYaxs4nszkprLhwWW8afH8fFaoefdFbFaBw6kPBzoKMz1PK_ZNy7l8cH-Stv4uIH7sMDYu3FZ7H8niXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edde05bb69.mp4?token=KTZhLVcTAPthEMobUczpJo_QlTnYDs3DgYZkmmZhnCW6r_hoGus_mJ_eNxOVaai8IOJjQoiPi0XKwoslY-eJAu1K-J4Jd0fS77DzeUgcO-ttauFRGDa4eB61IntgpZUr6lV8FarZEsQca8Xjjsspznzx26zgzN0K3GHQE8-MhE-d5XAeeANB51q9-I3dLJF5FAb8W1GgJrvRj30nLolNqT2olt7vKMHS11uS3XIOeFm498Y7J5kxzKQMDA0s1333EzXPVTwYaxs4nszkprLhwWW8afH8fFaoefdFbFaBw6kPBzoKMz1PK_ZNy7l8cH-Stv4uIH7sMDYu3FZ7H8niXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
روایت‌جالب‌ابوطالب‌از تقابل‌حساس و سرنوشت ساز روز یکشنبه هفته پیش‌ رو آرژانتین
🆚
اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/25905" target="_blank">📅 09:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25903">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pPyQIbhUlMw3va5KLg9T68ftGr3921_SruzpP03dz7S1HACfYA2rAiEbh3LV_0shLs0MCb1GSif61-6KMsfUBFrivuv5OZiJAvTekNwSNE8W_GichLX69lViaViUrUKPmvAAXPhbqmeCSSe3qtxEw1h5uNC9bzRk9V49v4DYQD5_HvR1_yAsVLDeqdC4c3b5LqtGgDCCwja4dwKqAdVUyXI0l8HMu6PPAhc7k-KCh7OPpfC-fjhQdsC4GtHWH3TBq9iEAQyVVqcnmK5uIzs5MIVFWh-P_yc0QKpxwTNnFys0uRfpifGC48u6MsolrMjU5WG4HpseL1NrzBReezzwDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O3_RNVqRgLPGZzdF3adMM_9mBb3EMhKQq99700pW8Ac0G_wibCsoIaDLbMt0OcTCB6APF8CA9f_buyUQ4yr97XatakhQNUFvuTyIEoxh6N431vs-BLBti_LOeGc_zdkqEHgo0bVJSlzlEuLyVT05suvvpAP3ToPCKYb2DDA-_jorBekxKaHpL9xKrHT6f9j6txRSTd3pcZ6kKVVdt9q7kI47wj9aURYu9CpPlonSmto0sl58Jibdsi9dV5O826PMtd_3fqak2b88I6-vWSSjEVFAau0-Myo_3pfYsSLTkL7OpwbUw3RLkQJkGcwHR8219NQnDuJ1OLwEoASniLhIXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
👤
#تکمیلی؛ با توجه به اینکه قضاوت دیدارهای نیمه‌نهایی به علیرضافغانی نرسید؛ شانس ایشان برای قضاوت بازی فینال جام جهانی بسیار بیشتر شده.
🔴
فکرکنم‌دیگه هممون دوست‌داریم که آقای فغانی فینال رو سوت بزنه. انشالله که نخوره تو ذوقمون و فغانی بعنوان داور فینال جام…</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/25903" target="_blank">📅 04:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25902">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCNqxZPG_0Uc8foZxABW9jHZDKdE2nvxaaxGKdpmu2OngD60yua-2fNik_Y0jcDikc2_gfBL28ZxCUqzOtrfh-X1QINeJ0C60rc9Inph4ErbFpvfZxsGYv2P1Axlxl2eU0i918DCNlrIzFo7Sj21ns8asAtumVPwc1Enc3DN3gDNbfMs74bg6cMHPCdk6fuKaA4oti6u35wzT4Tzx3sv-t7IK9FFIh3UUDVIXDXpE61HS-9LBiAr7k_LAuyEW9cvyoSwGsvUuWJM8JqNcw5pdnp_lNe0OY3Zcaw7j_s7xAXamPCYngPg5mx0bgSDABeRDNPZnRt0UZVqc7W61R9x3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق شنیده‌های رسانه پرشیانا از سیرجان؛ مدیریت باشگاه‌ پرسپولیس با علیرضا علیزاده هافبک میانی 33 ساله تیم گل‌گهر سیرجان مذاکرات مفصلی داشته و احتمال عقد قرار داد با علیزاده وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/25902" target="_blank">📅 02:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25901">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1Z6oWxCPqa26FJ7zd_6zGsGlRjIDoP8KeG3EqimPjhPfPR39a103BhbsMtkI84F0i9JfbZbL4WVW5DBlG98aRWKCexOW_hDCuDVs2ERTz53tGFqyHWtzMHwH3oyn6BJEnKvo0iWfFonNJBGDBD8D475znIPZt2mrleG4-vUexnZg265xk0_fNelhjWxJHAci0bcGBDr_SSSPRJJO0AjR5Ri3mc88aTXYWTj_Jw6w4IUpj2Azn7jCEsZC-qRX-Kq9giSRP58noMEEQlCwaJBznUH0EqvaGMXMY9kWv2LFq6SBWY5OHtsmXKD-QEOpDPwyIjZ36yZPTc_B0IrNR0F-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مجموعه‌ای‌از تمرینات حرفه‌ای شکم و پهلو برای ساختن یک‌سیکس‌پک‌شیک و واقعی؛ چون پست‌های قبلی استقبال‌زیادی‌شد سعی میکنیم هر از گاهی پست های مفید این مدلیم بزاریم که انگیزه‌ای هم بشه برای دوستانی که ورزش نمیکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/25901" target="_blank">📅 02:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25900">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/En15T6WFDAADPb09wlyLOPy3hluChgq4efIv8E9oi0JKe2g_HQ-u5tx4L5Mn_fMRm2-j3fXrZyQHlmBW1Jqo9iljk0C7883fvhl2rgSucW-tjLLvZ1gmBAhj2ggHRjXKU8mYvxhiV8kdRZrEJHz-9N70N_9mq3ML8JifOmmEkcnxaQlld4fhha6GQQfF1eOfjanOfqj4jVWayxSmBh-uopd9Ys5p4pc8ORGVql_cH-lk5eonjN4RgQHAHkzLhewFnZM21kedr60xEVbRvIbTGxgGGT4fHwzy_b2xDMmXd4Kw1yZlyKftK7Y2h9DQ1yh3H9hq28PLn1fKGBnWJ-KbaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🟢
#اختصاصی_پرشیانا #فوری؛ مدیریت باشگاه‌سپاهان‌باارسال‌نامه‌ای به‌باشگاه اخمت گروژنی خواستارجذب عثمان اندونگ مدافع‌میانی26ساله این تیم شد. اندونگ دو فصل پیش عملکرد خیره کننده‌ای درگلگهر داشت و با 500k€ به روسی‌ها فروخته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/25900" target="_blank">📅 01:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25899">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TULa37vp4qsL7vTbj15a2hrop8b-4lMX6mLivjo0wCB31gqAbmIAnbkMaQjJIlgO6RK0Gfa1qGAgTkT6SPCnwHdVbm2ggyhLHOnfrRZvfTPo68cy2GQLGU8Awv8DarQIUbcsNuDprxLLTBwBoQAvzcR-REi1kFIpxzycwq7vdVS2am_rmCKf4ZpeSkJnc01ehDr81OHb8swkJ_T_TLujbYC6dLpbapL9326hymtfvKf5ZiS957a_LZZ2Ao4q2wk-RIHTn26qXYcxrrboPfvisPjsJLayvmUQCuSMopY0Ku8hC5por1X3iy_N7msVi6TM5fbJ4qeRqJpI7HGZybGU9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
این‌پست‌برای‌رفقایی‌که علاقه دارند بدنسازی کار کنند یا کارمیکند؛ برنامه‌تمرینی برای ساختن یک بدن خوب و قدرتمند؛ سیوش کن و برای رفقات بفرس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/25899" target="_blank">📅 01:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25898">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bc6affa54.mp4?token=CgYQUhIICDLHn8-VR7274BwlynJWwVsTefj7H05YI_G8E3F5McMwhcasjO_EZ7TkCbYFhfHxKJXr1bI0OQOIuuKpYaAlL0D0XpjUNdjgGg6kwylTq0kTZYHFNYurMnKg1LI5XiJ5v-X8dzVO73hEiJO5ZSUJ50MCDKRi7XzT8lSpYHApaILqCfD3w-dCulhAy4iYhaxm4D0eNScnamgoFD3VB19AirxMIw34sA0Yi2iVnjn40KyXkN3bzutATM1-oF-ThkRFSMnGX-6EFYIXvHMjJGo03WeQnocC-EL8jpg1uYNddoSG5e9nWASBllVvT3UpccF1TT3AouIwahOqSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bc6affa54.mp4?token=CgYQUhIICDLHn8-VR7274BwlynJWwVsTefj7H05YI_G8E3F5McMwhcasjO_EZ7TkCbYFhfHxKJXr1bI0OQOIuuKpYaAlL0D0XpjUNdjgGg6kwylTq0kTZYHFNYurMnKg1LI5XiJ5v-X8dzVO73hEiJO5ZSUJ50MCDKRi7XzT8lSpYHApaILqCfD3w-dCulhAy4iYhaxm4D0eNScnamgoFD3VB19AirxMIw34sA0Yi2iVnjn40KyXkN3bzutATM1-oF-ThkRFSMnGX-6EFYIXvHMjJGo03WeQnocC-EL8jpg1uYNddoSG5e9nWASBllVvT3UpccF1TT3AouIwahOqSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
دو ویدیو جذاب از خوشجالی هواداران تیم ملی آرژانتین بعد از صعود به فینال جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/25898" target="_blank">📅 01:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25896">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LbZTEJOvAve_DeK6MdngYPDoDLCjXNc7a8I6Q5VeXilDKw9jFf7_vvxeeJmDHxGUY-QrRC90btukKsoSMdkp2hYxJiZK_vMgPH99McyBJt8h5Ck-oDHq3xFoWpKuFbksfSZSvSQ0m7IpalAQ6D9QZAPwIs5icZdzrvYp2awmAywz_r8B1G4xm2Czc6Egh0w5QdhhAivDJ2kmzL4dGbMfZTbvCNVV01vD6IxCSTQkBx2Uoat6Duu4GOt2t6P3fL-A1N7-V5MjHgmvSKvkStnluR0ow12-eEM9NkVfvqhgAcSShIqxKEtJnx2hCaCeG4-58u1iykGJZKfTDT-pXYFMTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پرسپولیس ظهر روزگذشته باارسال نامه‌ای رسمی به باشگاه‌اتحادکلباامارات خواستار شرایط جذب سامان قدوس هافبک طراح ایرانی این باشگاه اماراتی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/25896" target="_blank">📅 01:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25895">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZAQd_ESjnt1p9FIv1zkWHX-TB8K9os_vTr-KwD_C2-Aa7Bex6LntjKUO9YC2c2HkC4ZIxEgDiCnC9vm8JsDk1b00JBLye3lC5JLkOb34TNUuNx1QfzzdqjCfq4KUPK54tOeBjpxSUQOUJhbpgMuzBfcxdHA7RCpRY7EZXtgr4iyzKaTo816ctPHzm1Nq7PUCRIK2EkPRVYTbz0jBmspnesBl1sU9GYyFWkbXmbqUXe1RBpUu7EF_JJvreSWRLYFRGRODPutcKmkY5clYxG-u0ErrMqWaRDKqGSIfhGN8WaPvqusou7cB5VQYcVbtPUx5KP0QEBqDFFWxwRr-N5n1ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ سانتی‌آئونا: باشگاه رئال مادرید اماده است هزینه بسیار هنگفتی برای جذب مایکل اولیسه بکنه. بایرنی‌ها به‌احتمال‌فراوان با 220 میلیون یورو موافقت خود را با فروس اولیسه خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25895" target="_blank">📅 00:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25894">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-JQPybbvYNRB8yX6MUEbDK9q3p1I1z9k-Suav1DerDtapY00NqEFadKy2Tm7e_2XwIcuLjDSEFVglMzu3TuxxibJNa7EfX4zmaOViJ27_tBALy4nH2RImgh4ada1X7eJHYirHplKT3kg7vWT1fJZrRqXF4hvG2BCzdiZ0m5EnkOskXpoocB3es1JsG6-5_X3TN9O0jfYnamQcV4JqDckihwUZG6jVJfqMG3d9t_dVexh9JkJlXO8jWJhyQQJnWJESclIH4ohZgmzrq9n8qjrNJTMWgExdM7xXRubJTwYvg9oGTTOY6EvnKm8JW0y31uyL0UznVDCf-_ptP4EzAu6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#نقل‌وانتقالات|سامان قدوس، هافبک ایرانی اتحاد کلبا قراردادش را برای ۲ فصل دیگر تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25894" target="_blank">📅 00:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25893">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anm8LmrokRKhiTGpiTAGvyKplRmfhL9SHipoHT6_0hmfXTfEVdwjdcHCDvotxpb06rfyNETVndDXRcZq52D44bnhY3O-eX_qT4goae90YiORGgUMuSZ2a2qD1V8kZ-u16-43-wOIpj7SJ8ST3ikzwPGs0YYyauUbOhMm2vD3XxYSUHYEXskHbV-Sh7MmRxNXQpI3d-eeQdzQtpJTCYLC3ksGTP-4PQVKi5OOcUxiNf6Op-iITs5UhtLTeHNEGxSz-PtqRRtIPht2rp12vPFYbQOVVLkQMxriBDS9SRxwOQfzdudxjmm1MBjMljK3X3cgouuV7fUdMQZDQJM53cZAxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌‌های پرشیانا از مدیریت پرسپولیس؛ نقل‌وانتقالات تیم‌پرسپولیس با جذب چهار بازیکن در پست‌های‌دفاع‌میانی و هافبک میانی به پایان میرسد. دوسوپرایز هم ممکنه داشته باشند که منتظر پاسخ نهایی بازیکن + حل شدن مشکل سربازی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25893" target="_blank">📅 00:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25892">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgJx4pTwn0hZEPrkjLrFgw8EAq_0puVgnZVknh4LU-Su00gtKd7rj0kXdMqbmJH0w7RWQ_mFz_Fbx5PXAoMs1o9TJNRBt3w45EKhtAwA7hJCQCUmkf_FNREqfpEWnj65CfdK9xLRqqbp2HfqoH89gYjh8I3jYLFHNa6wMaOtHzSOq30DqV_UHRUWk2lTObdLC9vzUyzo-Llmc2Qy0QV2ittrp4IEt3b5WyfCb6fVI0UXsCjID2NTClreBkrJlaMh_PakYst7hXhC_2yaj29pls-qfdD6rJ765GE7-yuQJXdnQwbuVqDKdl-LRiCBvAHTA9VSRElxSkma-OZ5_EV_PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛سهراب‌بختیاری زاده سرمربی‌تیم‌استقلال روی جلال‌الدین ماشاریپوف نظر مثبت‌داره و به مدیریت‌آبی‌ها اعلام کرده قرارداد این ستاره 30 ساله‌ازبکستانی رو دوساله تمدید کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25892" target="_blank">📅 23:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25891">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddb82db733.mp4?token=IXi1rgN4bPOz41qQgIisz7cmBsrB8q25IiA5XfntQKTOaA1kXZo9cXYtTBp_sIWGq1vXQ9B9s35MuSRD0H9sjT5o9s-q_-mbeKImQG5YyKm4cfB9FwgAVotu3vHBkOLYNYHtcy_pKFB6blmLRzceq3E-HR-R1-QrCrdkigdPVj80w8KL1XQeDp2UEpEdzqxgSZ87qFRb9vD6CiwdUeMttBMg4owUZPlPayZctyTYkhAQFEFCHgzEFOCSn1XpSNXcT7kOnls2QBDKN2ts5lE44YfVWtF3WyMq070WbxlZDCmY412CqtLoVwBgxgSVhmQQOmnkcJPvrJ2TPY5aNLrGsG0AewqmIU-uWPIdhv9tvnFMBWAqv0UFT3lTT5oAHU0xOqqD3iAEzVJC4o0fvzPyhi95qY2MEl-ROZRBiSBLjJbYxl53bBG-p4-iY4ykUq7qK3sEED3WSGpYG5rs_d5EYDBi38cHrGz6RN3NjteBeklnddJ6AuuvM-zq8z2A-Kgl2cx8Q8UH0fR52yl0WIGOGyz6GIxjV3TW3ANHUP9dHUFjUr8NIFmSYb3cywznRY1rVcx5WsOqJwxYsrksIw6jR6nMhnZdw72Fsc3lSyCM9C6T-W_Gei3azz30R97Qnv9WeExgSrOkXJjAMT_2wcJLj5tzgfjRaLFYJB9D5AHeYgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddb82db733.mp4?token=IXi1rgN4bPOz41qQgIisz7cmBsrB8q25IiA5XfntQKTOaA1kXZo9cXYtTBp_sIWGq1vXQ9B9s35MuSRD0H9sjT5o9s-q_-mbeKImQG5YyKm4cfB9FwgAVotu3vHBkOLYNYHtcy_pKFB6blmLRzceq3E-HR-R1-QrCrdkigdPVj80w8KL1XQeDp2UEpEdzqxgSZ87qFRb9vD6CiwdUeMttBMg4owUZPlPayZctyTYkhAQFEFCHgzEFOCSn1XpSNXcT7kOnls2QBDKN2ts5lE44YfVWtF3WyMq070WbxlZDCmY412CqtLoVwBgxgSVhmQQOmnkcJPvrJ2TPY5aNLrGsG0AewqmIU-uWPIdhv9tvnFMBWAqv0UFT3lTT5oAHU0xOqqD3iAEzVJC4o0fvzPyhi95qY2MEl-ROZRBiSBLjJbYxl53bBG-p4-iY4ykUq7qK3sEED3WSGpYG5rs_d5EYDBi38cHrGz6RN3NjteBeklnddJ6AuuvM-zq8z2A-Kgl2cx8Q8UH0fR52yl0WIGOGyz6GIxjV3TW3ANHUP9dHUFjUr8NIFmSYb3cywznRY1rVcx5WsOqJwxYsrksIw6jR6nMhnZdw72Fsc3lSyCM9C6T-W_Gei3azz30R97Qnv9WeExgSrOkXJjAMT_2wcJLj5tzgfjRaLFYJB9D5AHeYgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
۷۳۰ سال حقوق یک کارگر، پاداش یک ماه آمریکا گردی و حذف شدن در جام‌جهانی ۴۸ تیمی برای امیر قلعه نویی! ۱۴۰ میلیارد تومان معادل ۷۳۰ سال حقوق یک‌کارگر، پاداش امیر خان قلعه‌ نویی برای حذف در مرحله گروهی‌جام‌جهانی ۴۸ تیمی. ژنرال جان باز بیا بگو خدا با من ناسازگاری…</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25891" target="_blank">📅 23:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25890">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1IULus141wSHgXIgC-tYRosmDCCwIMaXqsvn7V_ii1LxU0IGrxdjCTq-f8-BTBb6fidt3HTz7vyqAhq_8YV3ZPUrVCVnfpWnrAbVLzOArqo-3n_DB8ah8nQTG49fGoRXxV7-AlT41g1exY3lEieItfqu2kMs58MdoUFDBQw4HCNvw8jEjC6I-yYDvvNWXjzErDLV0AU2xTzt0deX0RXjfM9scbyG4YtZSXjRSZ4jDhOlos--jhBPYL_RQcVIKVE3k1w-oJO0b6dnmmDWLmFLIEyHpGQJS528H9xlcHkny0aeNYnLAUXAZW6wDHLY-yNXsa75zjzgjAMU6qtE4vAuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
این پست هم تقدیم به دوستانی که بدنسازی کار میکنن؛ بهترین‌تغذیه‌ها برای قبل و بعدِ تمرین. بفرس برای رفیقت که بدنسازی رو تازه شروع کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/25890" target="_blank">📅 23:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25889">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EF52F6v7MPjLFZEnIFHIyQaYZ47YYdbelVpev4SLClFx-0oMFvnIheMP5F7_ORqmmsu5NbjEyCh6fx-1HKTq7_kuq5_4iMnSJ-LJUnhMmYLHKNDaZ9-VI2F22aeynrM8PTQ8WAm9uYoF2Ais1m3FQvoGfZpA_Aequ0DLTAV6ODQ-_98jceX35uTuRD5JJRW0UscxlbzF49OrbMkfHglF1xtIG6rVBaNtOWCmf3aVe_Qmr1lrMJJXEXHIgddJ1Wu1emZCtepgWj8L6AAZSce3CLADHxgisWFXYjxcBFrlWzuvc_BDpiVAMZc3foe3RISC7xmyQuQGePGaahPDJySIQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه استقلال قصدداره که500هزاردلار به نازون پرداخت کنه و قراردادش رو دو طرفه توافقی فسخ کنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25889" target="_blank">📅 23:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25888">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8342696a5b.mp4?token=ixvamMCjhabYQJe6Te4iGQIO2Xjr3r0nBjLN2ikT6LbDLdco9rm3kbs1eeegElTGiSMS6mzA6Cu5td87776fHdiszI7m_UorPLdKgrN4lNv7p85PXh4qwnTDdLaWS2ncLMiZpCrmqECaJVaVs-fLsiRTyYWX4m30CjKAPGRFEDDWFd3GfAwujDGGUqP4v3gInH5Sd6xv27d5AVy2IERy6ni7kWtXIo8DhB29zNXMSEFMqA78HnYk7OHLi_o3hPr5LenVAl6pcWBpahto1IvwN-H3F-IfjlsXc2Tgpvhahk5w1JK3kyIg86cGeIOfmLcKtnAeFjhuWt0jWMMxjzDFTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8342696a5b.mp4?token=ixvamMCjhabYQJe6Te4iGQIO2Xjr3r0nBjLN2ikT6LbDLdco9rm3kbs1eeegElTGiSMS6mzA6Cu5td87776fHdiszI7m_UorPLdKgrN4lNv7p85PXh4qwnTDdLaWS2ncLMiZpCrmqECaJVaVs-fLsiRTyYWX4m30CjKAPGRFEDDWFd3GfAwujDGGUqP4v3gInH5Sd6xv27d5AVy2IERy6ni7kWtXIo8DhB29zNXMSEFMqA78HnYk7OHLi_o3hPr5LenVAl6pcWBpahto1IvwN-H3F-IfjlsXc2Tgpvhahk5w1JK3kyIg86cGeIOfmLcKtnAeFjhuWt0jWMMxjzDFTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌قانون‌نانوشته در تاریخ فوتبال حرفه‌ای و بین بازیکنان باتجربه‌ای که‌حداقل‌یکبار مقابل لیونل مسی بازی کردند وجوددارد که میگه: هیچ وقت نه در قبل از بازی و در نه در جریان بازی با مسی کَل کَل نکنید و اجازه دهید که در جریان مسابقه حل بشود.
‼️
اشتباه‌مهلکی‌که‌برای‌بلینگهام، شماره ۱۰ انگلیس به قیمت از دست‌دادن‌تجربه‌بازی در فینال جام جهانی و یک شکست دیگر انگلیس در مقابل آرژانتین تمام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/25888" target="_blank">📅 23:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25887">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKWegOwoJ4CXCU_tbjfYoXdjRwIJXC-t5SeEDfXthHvkHDfNgJcbZKVGiPRMLXXs7IEbLdfombzBhC0b4Chig34bpzSlC0sqiuGzr__BFr6r7V0nly_g24-YmX3La_If5qU_zafwIKIqTkW7DC7iv6GFBu5U7hyfr06b7ZsyAO2V1J81gVMGt3uQtVQnhrg91WLjlPa242_kZ2MnK7257bnsQBupTWsUAtCdfj_7CJjOocItVWtApeaOusX52FVKNtPUlUy3Yda-hM1EY7XSVy4Xp8RCITJgmAJfXgG9qrmZp-o-WjFtngu0OyHAb0MP0tl4ALF8mVhphnjwd-Vtjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور برای عقد قرارداد سه ساله به ارزش 150 میلیارد تومان با محمد مهدی محبی به توافق کامل‌رسیده و بادریافت رضایت‌نامه‌از خرید جدید خود برای فصل‌اینده رقابت‌ها رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25887" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25886">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71f007ca6b.mp4?token=kCJEipy3Fx8E8bs5hBa8iq3WdeBuOdpF69HpWUWfPEpO6db_y_d6OxuZDSMihRlOnCs4GVMmqZFC-bB1yIjwe72Y0IDlnAaYmiu6uyy4p4JYtIihc7eRdjeZ7g_p1g_cx8fgjK5cI4YMcUGgaPa9RppcAP7rXzGbqC9irAhuFfYyFN_FNc7O0m2--Tencbvcs6S4L-F3kAS-laD77DjnBoFvQmE_v3Dri3BMYl6FzGy9CbePFaBCqrA4VW040vfnYDv2kCVzqrS2nIJT5Or-pUVY9VofRqrKrjGNSkN59UFHsKvzj-aLCBEUT2FNrDBKFtCZC9V3x91Np47avyE9jm5QHVaSOTIYWsjEINjUwbECpx7cbX1UbtGcS_SXsU18iDb481lXDTBOQsDLdn2uipLh5ZG3D_vGddrmylWuBnKVPo7-h6MIGwCN-4GjnbMictxhNm4CYujn4fqc4jfMC91lw0UgBnSxIHYuL-fwrG30o7EtI9LowewXdWuEuyRbfOSD-LiwK9jid1NoWyVcRFJ5SVKFGKckLPcvJPwn285c0BMZ-cgfZjDQUM4eR0ACj74J7PH8eb1y5azf5mH82FwLsqEupcjqE1HE1x700wSd_uUFZ0tG6Ei0S_wAi6XxDetgOmugxIWTmMsmF13kwEOFcPpFr9TxyP1cFgKXaRI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71f007ca6b.mp4?token=kCJEipy3Fx8E8bs5hBa8iq3WdeBuOdpF69HpWUWfPEpO6db_y_d6OxuZDSMihRlOnCs4GVMmqZFC-bB1yIjwe72Y0IDlnAaYmiu6uyy4p4JYtIihc7eRdjeZ7g_p1g_cx8fgjK5cI4YMcUGgaPa9RppcAP7rXzGbqC9irAhuFfYyFN_FNc7O0m2--Tencbvcs6S4L-F3kAS-laD77DjnBoFvQmE_v3Dri3BMYl6FzGy9CbePFaBCqrA4VW040vfnYDv2kCVzqrS2nIJT5Or-pUVY9VofRqrKrjGNSkN59UFHsKvzj-aLCBEUT2FNrDBKFtCZC9V3x91Np47avyE9jm5QHVaSOTIYWsjEINjUwbECpx7cbX1UbtGcS_SXsU18iDb481lXDTBOQsDLdn2uipLh5ZG3D_vGddrmylWuBnKVPo7-h6MIGwCN-4GjnbMictxhNm4CYujn4fqc4jfMC91lw0UgBnSxIHYuL-fwrG30o7EtI9LowewXdWuEuyRbfOSD-LiwK9jid1NoWyVcRFJ5SVKFGKckLPcvJPwn285c0BMZ-cgfZjDQUM4eR0ACj74J7PH8eb1y5azf5mH82FwLsqEupcjqE1HE1x700wSd_uUFZ0tG6Ei0S_wAi6XxDetgOmugxIWTmMsmF13kwEOFcPpFr9TxyP1cFgKXaRI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه جذاب شب گذشته عادل فردوسی پور با حضور علی آقا دایی و کریم باقری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25886" target="_blank">📅 22:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25885">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTTexaXUwQmActVJe3mYDNVRRlPdDESviz9N9cKZmNmS1_g5Ogdathg4LnwAfyP6RB1JNxiLwpbp5Lj5NWDCnsC5NUKqrIU_lBIIaZdmUlrQBwcS34-UmXqx5PvfjZ_qEbuzJpKHFUA8tAOCuMX8UzxXu1s3tExVnCnJTOS-basUlNwgmRxE5yLpzLxZ7lRA5AUFgL74_Uf4rT9RhGheyvtkPl6ptmyp1a_Hjc18mTHd_Q8CjAKPskqR956XRZlO3qzqeJWwD31t1nNXd9GrAMULldOtqpLwgXdpiaSM_kb1atS-krp0ud5HQ7iBV6q3oE_CjwTP82FZ3KW7xRQyXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
#تکمیلی؛ اگه جدول رده بندی رقابت های لیگ آزادگان همینجوری‌پیش بره؛ نساجی و مس شهر بابک مستقیم راهی لیگ‌برتر خواهند شد و تیم صنعت نفت در یک دیدار پلی‌آف به مصاف مس رفسنجانه میره و برنده اون مسابقه نیز به لیگ برتر راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25885" target="_blank">📅 22:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25884">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pz4jLlajVE0Lm1qwN7bE2AOj_SmETswLgX5OhcycaM6Jdpvz5D-U1XbRrwOyt_uj3wgTZQJ32HhjrSOk0Sr5zdqIGrhRwrMLv4CJCDIfqgolGa-d9GpnaD0WxXuqaAn5g8ce3mUcWzQw94mstrMkVub3ayVXZ6jgovkM90_9Y6e_qSDuHnJooRtze_GoYwxr_-GfeZD7y1tpRaiP9FhhoAEVHInBFrhIfqY3wJFQDBAXl4X-0OXTQ5xJJ_tkt7d1nUfa2M4n_e6GRQ8AiQUerBx-I5RZZge6JHZE4d2K-42RdqlX353ckJQV2tsaTMs32jm2IA7WhZ3ewPWZ40ooYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه پرشیانا؛ شهریار مغانلو به پیشنهاد مالی‌باشگاه‌تراکتور پاسخ مثبت داده و اگه اتفاق خاصی رخ ندهد شهریار مغانلو به زودی بعد از بازگشت به ایران قراردادش رو امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25884" target="_blank">📅 21:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25883">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hlard4F-Xn_E8N2v_8xeaM4F1C5ISlyF-6a8vuXk7iIAF2k3k5K56F46i1sw592pUxBHkNPdBNCG8-FcWCVeHLQdKQGIU0KmS62cD67OW7ed0LiLbToIoAUZ3qHB-91ixY6prBzy-1WaT8wsSprpBJpLljUAt022KVAIR3vpE8XC2BcRSZ9KQxwBm2Dx09OjvnCk5cRUKxdsBPk5oLPUqsX5uz4Ge2m854mdr3kBg_ZaRyeJYNVwBQ88aKkZGIMEHbYEv20SDSlRWuhsFTvDM8t0E695ZujlX3nJX81fAEhDFNXifBnX-c-sGQwqgaogSKr9cuTgwQosl07McUEGTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#فکت؛باحذف انگلیس،ایران، اسپانیا و آرژانتین تنها تیم‌های شکست‌ناپذیرجام‌جهانی هستند! اسپانیا و آرژانتین بدبخت باید تا آخرین نفس برای قهرمانی بجنگند، اما ایران؟! ایران یک مأموریت مهم‌تر دارد؛ حفظ رکورد شکست‌ ناپذیری! دو تیم برای بالا بردن جام‌جهانی میدوند…</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25883" target="_blank">📅 21:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25882">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5c4d2069b.mp4?token=OYR_w3_6rNr9yoK1V268dse5nYhrzq8Ino6tM3tcl4guPjelyD0mBHVT8NLEazpORInYleFdrU1et46Gtk_QcaIPq88K7_6D88dC_-EWhKuLbYSDXj6zgZz_uFtb10hO5QBU0jGiHhiG5g8WmIXwpnPX1ny42b-eZzDUlRy4cb-loWqV_E-H2S_gYM36pHj7a1YPfmSG6afguKzMvwQtzs5r_JqaR0uPdDtQM0T_oO22waUEY-mGruDPE99dhriSFm0ew0zWA_rlMGMCKmI8hq71-_XFS-Kd11t2m9dhP_jqT8QNUPaZPURWmPMjgYs3Kt29vVJvdrreC4UV_v5t9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5c4d2069b.mp4?token=OYR_w3_6rNr9yoK1V268dse5nYhrzq8Ino6tM3tcl4guPjelyD0mBHVT8NLEazpORInYleFdrU1et46Gtk_QcaIPq88K7_6D88dC_-EWhKuLbYSDXj6zgZz_uFtb10hO5QBU0jGiHhiG5g8WmIXwpnPX1ny42b-eZzDUlRy4cb-loWqV_E-H2S_gYM36pHj7a1YPfmSG6afguKzMvwQtzs5r_JqaR0uPdDtQM0T_oO22waUEY-mGruDPE99dhriSFm0ew0zWA_rlMGMCKmI8hq71-_XFS-Kd11t2m9dhP_jqT8QNUPaZPURWmPMjgYs3Kt29vVJvdrreC4UV_v5t9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لئو مسی توفینال‌وقتی لامین یامالو می‌بینه: تو پسر حشمت کی‌مرامی؟ می‌دونی چقدر رو هیکل من خرابکاری کردی؟ امشب دیگه‌کارمون‌رو سخت نکنی. به نایب قهرمانی راضی باش قهرمانی برای منه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25882" target="_blank">📅 21:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25881">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBIUqCn7HQlP-up2dQ5125J3rkwF3b0alICRINxkAeLu0-KbbzNvzV51R_eh67D4F-WRKs4QSz4HVEZ9vy5cRVau18tkw8vChukmZZ4KeDRat7LJ5BMKKFFUeaESAHN2VoqnN-7wycUsOe218hsoKls_8nQOzaKry99SM8js5PE5SfLKLQxs0Pi-QPdEKD5RtLavPwFQbzSKEbXNtx1A1LtRAMU5GPrO6OOa8K7PFggY83eJzy4X1R660PmB2gQDMxM98NR2te9Q455YMAb7FioWjgwVi_mBr9Z8l4Zeqa6Y9FiUNv3Ajg0bLOHrao1MdzOnu0rYfwiqYtUNOlLtDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دولت‌بریتانیاازفیفاخواسته‌بازیکنان‌آرژانتین رو که پس از دیدار باانگلیس بنرهای جزایر فالکلند رو نشون دادن، تحریم‌ومجازات کنه. دولت از فیفا خواسته این بازیکنان رو ازحضور درفینال‌جام‌جهانی محروم کنه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25881" target="_blank">📅 21:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25880">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uw-0wEMO6p44o2rzBJhc0cValDcD-NwO9j6qaC_-sgxEAGfaQGdZMnkJO--o4b7J1d32lTYyiSZ1TssGDm5ukay1gKrQiNFlEcG7F2-PgSFIVGpDVqMtxqzXINgel4naz7f3H7cvTaR9fLmtGnyZzmOLgIsnknyuhvM5YOZQhd-Z6hKb2Nu2rdsBf6LT7q7Kk_dsOsKBFp8X4n2vaSSWiaCzOHe6qaVS0zJ6-NQtVhwC-lFKZDQ1H1BHced9q16ibiPUp3agVM24xCZYvGoxtxk7AOCXh4jdcHh-ljck3cFnEFmHoNMh0gN9O9rtg8iBbwXc_RP5StGD_qLV29bogQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بااعلام رومانو
؛ کریستوس زولیس وینگر 24 ساله کلوب بروژ با عقدقراردادی چهار ساله به آرسنال پیوست. زولیس یونانی فصل‌گذشته‌در36 مسابقه 17 گل و 23 پاس گل به ثبت رساند. همچنین توپچی‌ ها بدنبال عقد قرارداد فوری با مورگان راجرز ستاره تیم ملی انگلیسه که اونم در پست وینگر بازی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/25880" target="_blank">📅 21:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25879">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0qwlQJ4APseUIBTilNAHHYmuM1nVooCsWFvxV7z7X73UOxATSZWjT18DHOhN-NrJwew6fj6h-EoQ2R0KgGH5_AuCDEl13_KPnUsVA8PaY0xa07mp8XPfeRgGC4XT4OWg4PqMyU4uLvgnXfmCgu-OghdYt1Lt2bsLi5jSb72kfTCCRSF4qtPUI22qaxtQ076JGj34cbyYM5TuCXnEH182hFP1X2smXg_VS3aD3LcYsyCiKjnroL5oLULiRl4eTT60QCpJ2xiymxNY2Zw5r99RAvCwp5AxB3Bffp_hRGBokdkIcvyF_dG4mxSb1yfemWO_6K5F8DbOeBk7wgEKOZLvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
عارف غلامی مدافع سابق استقلال: در بهترین فرم بدنی خودم‌هستم‌. میخوام در استقلال بمانم و با هیچ‌باشگاهی‌مذاکره‌ای نکردم و نمیخوام مذاکره کنم‌. ازسهراب‌بختیاری زاده و علی‌تاجرنیا خواهش میکنم که مشکلم رو برطرف کنند تا در استقلال بمانم.
‼️
این درحالیه که بختیار‌ی‌…</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/25879" target="_blank">📅 21:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25878">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsvHhlDdalZDMgfuE_bfRKfS3o1mcELK5xabyI56KuV85hBNELOAYxyofkoYaYmblmNQPbWhUj73O2v3hWKkA3rqPW1WfriFszHYMZdQXxB3rg4oaDL-wUZZhlzbYoAyznLvdQeIfNp-zOzz1cvTYIVv5oNnLdMWlZzy0GOoXVItSyPbZsL7B-MDPeHcCS6wImuGWEaTtkfvSznlTlCIbbuY-8FcXHYeA9xoDG1Qy2tSGoIM6IpcovbQ428WlHeu6NLQiAv6GEG_6_sXCjFiBzTaE2kHRRmMdPWxTWYgExqQK0zmMKenTVwxhAC0oSVCuH63c6oLM3BcxMYHaThvbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">�
جدیدترین پیش‌بینی Polymarket برای قهرمان جام جهانی ۲۰۲۶
بعد از برد ارژانتين در برابر انگلستان
🇪🇸
اسپانیا:
۵۸.۱٪
🇦🇷
آرژانتین:
۴۱.۹٪
حالا نوبت توئه؛ از داده‌های بازار ایده بگیر و پیش‌بینی خودت رو در
Betegram
ثبت کن.
🎁
۱۰۰٪ بونوس رایگان اولین واریز
⚡
واریز و برداشت سریع
🏆
بهترین ضرایب بازار
👇
همین حالا ثبت‌نام کن:
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/25878" target="_blank">📅 21:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25877">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e985eefb30.mp4?token=UsPwBRkN8GVNZn0wMpZnGn7nQdH18cp2V9dyAAX2ZKSsqIf6KC7nFNPurpy4e01Bium2mZxq7szLwDZknLAvlLBqj6VIwo4U7wfLv3w1hlZPmW58CA0_QAfBspwLH74CZyhU0UUd7tWHVcQcFB7ya6Cu9LS6GPpzfp2_z5FpAbRCubJV_qVPLfxDObZMl8r6S6Gn6OIKWfUSXXVkrdWeWUrsQn6xmC1hhy0JEUGkpzvHeUhpMdStKiDB3d2Qm8Q-ElUCC9xdd5jHT5DmBE5lEXScK0kDTFyMFJQXFVm89DL12n0AiTJbi_3441Xo36zljoUWI5mSo8CcC5NsIVIzQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e985eefb30.mp4?token=UsPwBRkN8GVNZn0wMpZnGn7nQdH18cp2V9dyAAX2ZKSsqIf6KC7nFNPurpy4e01Bium2mZxq7szLwDZknLAvlLBqj6VIwo4U7wfLv3w1hlZPmW58CA0_QAfBspwLH74CZyhU0UUd7tWHVcQcFB7ya6Cu9LS6GPpzfp2_z5FpAbRCubJV_qVPLfxDObZMl8r6S6Gn6OIKWfUSXXVkrdWeWUrsQn6xmC1hhy0JEUGkpzvHeUhpMdStKiDB3d2Qm8Q-ElUCC9xdd5jHT5DmBE5lEXScK0kDTFyMFJQXFVm89DL12n0AiTJbi_3441Xo36zljoUWI5mSo8CcC5NsIVIzQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعداز این‌خبری‌که‌این بلاگر آرژانتینی منتشر کرد ممکنه لیونل مسی در فینال گل نزنه و پاس گل بده. پست ریپلای شده رو بخونید. رفقای اخبار +18 رو در کانال دوم میزاریم. دوس داشتین جوین شین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/25877" target="_blank">📅 21:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25876">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5pGA1QTNGWe_P60Eh59RtXzOOQVSlelDrjX-EmAoUiTMoLhRPT7OrA0rUF1x8PhhadoyfKh7DabzR-FS6AjUfJwghboMS0oIFxTva0QtZjRX7W43_WXeqZ3lZeqU23nzTQdMMQ50kuGtd4iT3LutISISThs8QP4Tdy2_4lg5lZXjhsjd5nljmRVmIXa7JFqQVutN-w-1cb32fbJc8ZJXJhnUK1ZzcC5qgOnYfo-r20OTFKjAdighcqP7sPX_9VdeLEWcD059Or3VU2p3ApHiAourVxcQPeqB8AQzls-TVbosW1SMXpueqxp-jNdHhz5SR8eI8YktlkZ7V7S_xvlug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پدرو پورو مدافع لاروخا با گلزنی‌ در بازی دیشب به‌رکورد دو گل‌زده رامین رضاییان در این جام رسید؛ تنها 3 مدافع‌راست‌درجام‌جهانی 2026 موفق به ثبت دو گل شده‌اند: پورو، رامین رضاییان و دنیل مونیوز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/25876" target="_blank">📅 20:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25875">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2kS-OqDCwga4iA2I_evu88QFhdaIgNBBTLV5XnSKWT9OcDU_XryXe7gQCgsBETo4FYQV7Y3GvvP6U6lHoNTa3X6mvbuYH7igz34kWNb5q5GSg-Mr-92AtroKc79u3smVysQUbhCvC-yDXNMlZffhzIUX3FJ9QyJcDHQm9nm9plICOvEL-nZF6hqGU7BXdDFQOenIWcv9GKq8QSVsGIpVn8-lchyO94ohwPkqc_uRWFLNSeSnxWIHCH5bwZYFb5o2pkYBc65PI8sEaxWXhQA9sIXCNEEbiptvkVPh4IsV5kCXmGwanFKmYZyF7RZ85fFSY8DJVHcPMqrZ70OUE8rvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ ملت‌های والیبال؛ استارت شاگردان روبرتو پیاتزا در هفته سوم با شکست مقابل اوکراین!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/25875" target="_blank">📅 20:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25874">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kpg0uvlB4SPhNvcn_FTjx3l6Q2wM9tjdi1DcgaUZ0ouPoS1HKhG5affL0mbqWrIjs4CUTB1fmlnxT5TK3M3mWNgQcwWh3ed14m5nhgYC7Z9mJoqAY3_wcUe5QZHQU_chx2hhDQc_AkvED24oe_T6e49BgQznyHEI4T4pt1gv6rkLKr5GBtjkOgNCVVcI2cZHX55_864Lp67zkEY6vccLpOKVBf8RQUeqc_GjhP-zD4v8_bDOKFURwHdvpxjotDF8HAcm6WdPGxQHueRpsG3Wypqc-Amuf-mz8y767I5cMjVPePm7gMogsDB9d-l6nesvGimtIEzk207cDl_weVfacQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ داستان‌از این‌قراره درسال ۲۰۰۷ در یک برنامه خیریه یونیسف خانواده  نوزادی برنده raffle برای یک‌ویدیو و عکس‌بامسی برای یک تقویم خیریه میشن! این نوزاد ۵ ماهه لامین یامال بود! این جوری میشه‌که مسی ۲۰ ساله لامین یامال ۵ ماهه رو حموم میکنه و باهاش عکس‌میگیره…</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/25874" target="_blank">📅 20:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25873">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArTkZcuUVIDXX-4BWkP7FHLxUD1qIhFrN0Y5mY5xZ2McE2C_EhLiEGaCTHzg7FdXuJlivYX4GtT49CSYYA5Q4COtj2vnhAYsr3r0tGjex5X7XLVnDeXEh8JJR3icqNIzSlUNSnifEW0xEnprf9YJqOu2A5HCweF2ZL9qpUAZmRnrPlWLAB9K7e_6jIsEG7rSPbXrZWeSNQ5cyYLUhYV1dYEnIDo5XMgIO5rJh2nb7thnuwkKDCFd5xDbAIpAljRaBShy_uqYglY2T06IJEsh9lv_8Po5R8UHQW34KWX8_9DE8WQxAAsIWBMbourh9VaHEqkJ7vQgnVtS0JGjUDGzKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیونل‌مسی بخاطر آنتونلا قرارنیست تو فینال گل بزنه؛ این بانوی پاکدامن گفته اگر بازیکنی از آرژانتین درفینال‌جام‌‌‌جهانی‌گل‌بزنه یک شب باهاش میخوابه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/25873" target="_blank">📅 20:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25871">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e_JFtDeThjS6eBLbAF5D4dlklL4Jzug1pj7Cm2Eq3J1j-9HyY7vplR3TZzrfwbSLjJfCii1PMlqZ8XrqCB2xOJfqdJvAl2XOsk4UcBZzkLxK0C9OUtcI7-uaFIqWJUpSViULQlIxWBKvTdBdA5NvvxxUweCuho58B0Y65NUylibtoMNZ3gbXgdCk-6AY-9MX029AnMh0zzwT1PqKaHA8Z6d7rkotHV5BJJyq85HesgbzfUC2NZaB5XD0969hKliLsFwfMAyz93Jw15wkuW6gVe4S76sjeXio7OUW2XCR0bzzuyuc-pJX7V4nK6Me-kxjPHnJHUp_ACTR-SViiVMpnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QjFhuAenKQM89fzTmSfhmwjlFxnnUWDjiy35sgFHrh38DjSdqHRzzM1xmNQ8Y6NE8QJNnQfZ8x9VBViKhOauOdkX7CY0hdSwHf2huvgSzBRUCzjAtWtahyhccsQtzNYdL3thW1hSzG4nEw8Y-UW-PtGNku5L3iTimikbMZVx4oj2oWVjRQJbxeKi_q8AYeElinh6AkxRE832j8rjhOJOGhANfcJ6TPNvV5QD8FexoDVkVxUF6YCk0h0aT8Horz7vwpDh6wdYqk6IYWPaXJIKLiwg3u6T9SSI7BOQzru87yAFg-wz4VAKqNxoW10jy4WNBPJyJkaeDdYykm9yPLidUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
نادیا خمز دختر خانوم پاکو خمز سرمربی سابق تراکتور هم با پارتنرش ازدواج کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/25871" target="_blank">📅 20:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25870">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WIq5hil1S9-otlzSNiTsiTUSLE-C0rX9zkTY_ClxrWMMw-ZyqPrqm075sYaYkcU9dxiAtMV9Dsv3DjbJyuL41epD1gfhjiGdpcvVE4L9QKqjcahr2B3ZvCBHKEzJHophvqZ9xRg3JSrlTLUuniM2NqlTUCExJzQL0DFd6HzkMXxSdfq0IwMQF1rraVowxdkidQ3WS1M3VUhkNNO3cW1AZowrtl0YwGJDSIWLcTKzyNOMfXbs8Q9fb7HjdO6wIzfBEVBs_3YfPvIWl5loU0VklBbLWGsfLdXc4AMuTS4ZK1lha1SEwe9AEqKFY9JOPx1ext5J9bSYR6Lh0io93eNOow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مقایسه‌عملکرد لئو مسی 39 ساله در جام جهانی 2026 با لیونل مسی 35 ساله در جام جهانی 2022
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/25870" target="_blank">📅 20:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25869">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇦🇷
شوروهیجان این زوج مسن آرژانتینی حین بازی دیشب‌ با انگلیس درجام‌جهانی عالی‌بود حتما ببینید. ما هم آرزوی‌ همچین شادی‌جمعی داریم و اینکه فک میکنم اون روززیاددور نیست و نوبت ما هم میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25869" target="_blank">📅 19:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25868">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‼️
دور دور ستاره‌ های حذف شده از جام جهانی؛
فقط‌اونجاش‌که‌دیکتاتورامباپه‌دستور داد که هری کین و جود بلینگهام برن تو صندوق ماشین. عالی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/25868" target="_blank">📅 19:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25867">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed8e8fe52.mp4?token=d9BI8maFX827cKl1kfurJAvaX-kT3AYKferLj8xb_g2pqhZfxKLXZu84bLtS70NndT6DCFruVVrKqw5lYPB4fb45XqS1mJykxfgyoOrYS4nHLJqgTk27bAWuPRHSM8mQ7NRzCXTMHXWYQfoNDgEO1BneKzJEomFW4_6saJK36bMHrNr_AV1kzPHwsfpDSgzCbtL0bdd4QSoDEYOk5oSwVtWVw6muiMAlreHJTNBcoCRHRKyQX3cHVuyaJT_rIWNVQidpi-D4TmHv5puzKK7oyQM-6uKXWdX6SheMvqlJjKUrdxg9OtNXMQknahj2PJGquL2GiGF-f46SzGz9tpt6Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed8e8fe52.mp4?token=d9BI8maFX827cKl1kfurJAvaX-kT3AYKferLj8xb_g2pqhZfxKLXZu84bLtS70NndT6DCFruVVrKqw5lYPB4fb45XqS1mJykxfgyoOrYS4nHLJqgTk27bAWuPRHSM8mQ7NRzCXTMHXWYQfoNDgEO1BneKzJEomFW4_6saJK36bMHrNr_AV1kzPHwsfpDSgzCbtL0bdd4QSoDEYOk5oSwVtWVw6muiMAlreHJTNBcoCRHRKyQX3cHVuyaJT_rIWNVQidpi-D4TmHv5puzKK7oyQM-6uKXWdX6SheMvqlJjKUrdxg9OtNXMQknahj2PJGquL2GiGF-f46SzGz9tpt6Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
#تکمیلی؛دقایقی‌قبل‌بایکی‌از مدیران استقلال تماس گرفتیم و ایشان‌گفت که تا این لحظه هیچ‌گونه نامه و ایمیلی ازسوی‌فیفا و دادگاه عالی ورزش مبنی بررای نهایی پنجره نقل و انتفالات آبی‌ها به ما ارسال نشده. لینک زیر رو داشته باشید فقط نام باشگاه رو سرچ‌کنید اگ تو…</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25867" target="_blank">📅 18:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25866">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WoPlbqhFqECZq8hx09ERitieaXS7pSaNsoL_MLCGFBMfu1wlaI5AmT0DySCZQ1uTztSHpi5GkbOCvph4Xk664JG3Of__2iKd4KD8yQRpSkabOCwaIYu5_3bR2SvZ2i97afu8pweqDxOTtzrg8Bg4uEa3oRaCxViX55GTPH2DLdA1LaTZKDfxZww7L7STI1s7VV79MKa8_pg4qrhegzarw1Ysz_ERWKuF9JaLWOUO6MXelt4K0k4pwteovhfKQ2tI7-hFJ7JUnvVBXXBBFNFXGVD7v2OPzu4fqIZq-NMzwKUIW-OaV0PXK96G5kUtR7p5mlraxLW20uGBIBboNrRL1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#فوری؛ افشاگری‌برگ‌ریزون عادل فردوسی از امیرقلعه‌نویی: ماجرا از این‌قراره که چند روز قبل از دیدار بانیوزیلند؛ امیر قلعه نویی به مهدی تاج زنگ میزنه و میگه‌من تو فشارمالی‌قرارگرفتم و همین الان 140 میلیاردتومان‌میخوام‌اگه‌جورکردی خب دمتگرم اگه نکردی من انصراف…</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25866" target="_blank">📅 18:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25865">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zv2MjEQTHVNucdUo0fM_-vOTYOutnugm0qdmMqdI4GVDylfNcs-MvpkaJwHEM2hVSInKqcX-Ow20mabh7pUK0ZpNT2vNqKnF7JZ-_ozf76kjwW3r6QU43vLqUqcl_J0m8TbSSLOgdkANXC4csKfynTXSGE4w2tkGjWZtHOUlWRdrdQy0EwgIoVmW-vGSLyhHjCE6i-1XdeT5xYZpzC2mAddMqjJI9NvIp_f0czhelpWO2iy2LLF1JPo5PhgGn1JKJ_oMSkmTd9cdPkpd7zBU9vcLq44Le09Beqaf8_WtD2NL3MTk-Ip8i057FOAtrt7htnXt27Qx2hLM9iQTG79i6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌پیگیری‌های‌پرشیانااز مدیریت استقلال: وکیل ایتالیایی باشگاه استقلال به علی تاجرنیا اعلام کرده که دادگاه عالی ورزش CAS تاپایان امشب رای‌ نهایی خود را در باره پرونده آبی‌ها خواهد داد. طبق گفته خودِ وکیل احتمال باز شدن پنجره آبی‌ها زیاده. این صحبتی که خودِ…</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25865" target="_blank">📅 18:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25864">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpZlYrGSPXmzxUemkMHD0mvjBC3J-zlrpBculJ1asBANbNVp4n2qO5ok_8RIITfZC1xrCI4dUPIUwPEwdl72kYWvTwbFZmODO_aa8TUCeKAJyd6Nei0gvcsVI4EMWEUUq2wZEBdUX6f0pLePa31cGezEszEJ3xsvMRLs_2dcMOoAb04JdSsJEC3S-bnZbmghC1BoZoC0a-otYTE5EvhhY6CpBIv892fccaT4yb3SZWsICHL5y0VFxzPqa5dvPp4I8nloJNEmMtlYG006WmjcqZOllfSWaYyvFmnuVmuq5o4pSlBuxn8Mechlqc2q9o43ZrgRJ9TqQWP2SwcUSyBFfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه‌نهایی‌جام‌جهانی؛ صعودتاریخی و دراماتیک یاران لیونل مسی به فینال‌جام‌جهانی بابرتری سخت و نفسگیر مقابل سه شیرها با طعم کامبک.
🇦🇷
آرژانتین
2️⃣
-
1️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25864" target="_blank">📅 17:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25863">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed064d5f2d.mp4?token=OIzd_qy9IT9qzXW7ddyZpTz4GNPxjHtQ2FYUwTTc_vkFfdmNAj79sBZB39UMnRSIFLnK2yws5BkW5jKd3bq4Wpkyfem-qh_6aHI8S_9pybnrYmaoC9eQuCxFUi4Idwj8V0Lhh8yRm5pjq3c0XYc1O8dhRg-LEdgprwP_ZeL3WLwtl5Stg62dObgWWiXZVxnBcy2aOUyVeUbQFWGtaojUdAKHuG_WWoQRU74kBhJSOx_S4cWQ61zbseu0mn9RsATPB8r2JunlhGnwRaDyjvu3-0n3h9aEJhqboNuBtHtXWsqfpuXzIU3PzwqO42YasMhXUnVv0M5CYHbdRdUJV20Uwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed064d5f2d.mp4?token=OIzd_qy9IT9qzXW7ddyZpTz4GNPxjHtQ2FYUwTTc_vkFfdmNAj79sBZB39UMnRSIFLnK2yws5BkW5jKd3bq4Wpkyfem-qh_6aHI8S_9pybnrYmaoC9eQuCxFUi4Idwj8V0Lhh8yRm5pjq3c0XYc1O8dhRg-LEdgprwP_ZeL3WLwtl5Stg62dObgWWiXZVxnBcy2aOUyVeUbQFWGtaojUdAKHuG_WWoQRU74kBhJSOx_S4cWQ61zbseu0mn9RsATPB8r2JunlhGnwRaDyjvu3-0n3h9aEJhqboNuBtHtXWsqfpuXzIU3PzwqO42YasMhXUnVv0M5CYHbdRdUJV20Uwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابواطالب حسینی در برنامه دیشب خود خواننده آهنگ‌معروف "جناب‌سروان ولم‌کن" دعوت کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/25863" target="_blank">📅 17:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25862">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TC329C4PkdJ9QJsIzVxeAkbY3G4bDjkeV4lTQjo8f0garbB5q-NrTIIv3zRtTD517qOZbwQY3TMpSIHfVfwjSmFj0lwxHEnXm4lTlDW6b3-1mWcSxic_sstlp_Opb4qY6MF_BvQeF1R9scfzVmOrKFKX3lcOtDiZoEN88Rk78OniyZxaFBsgkXobsGIp9D6rCTks71NWfGuq1ZcVXZGO_JJ442xCN6UqEkvpFSr4qslGMK0_QT9t9HH9c36LcMztyR8cCazzwj1KcPyxsdt-VIukppWDpM4WmKNwR9RRIcHYdI6yULUeBf-R1femigkjQEYc5brvOeO9wrW47clm3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
#فکت؛ تو ۸۸ سال اخیر هیچ سرمربی نتونسته از عنوان قهرمانی خودش تو جام جهانی دفاع کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/25862" target="_blank">📅 17:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25860">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlQnAIy5QRMl8YdKYdvnfvFfcgoPIDbCW3z7aX_iPC9ubuT43uOzRVmB9SSMNNQomVNfswXysmO65vyS_57tL-uOOWu4A7gj_RFZeMk-2n53vp5CYg-aDDiupGS5RD6E3WReU91S_N7kgpxPcNk0FNdiXP4tzkBBFPCEr440lp8KpKRt3ocouf5gaGuAhir-_DZTZRrJ5ygG-XuSochTYo1oUD3NNKkdMILBeVKR_SVFEVEnew4rShjAxKwVb-gMeSehDd4wD7M-wEX2ZBUSwHvRkWkrt1ObLQO6OLSwtZ-38gkIlOF2thrak6UswXTZbyRwgNcaWaWl33R3f2CYMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
واکنش‌برگ‌ریزون‌اسکالونی‌سرمربی آرژانتین به گل پیروزی‌بخش این‌تیم مقابل انگلیس رو ببینید؛ چقدر تو خوبی مرد؛ مگه میشه تا این حد خونسرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/25860" target="_blank">📅 17:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25859">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/orT5BhV9JypTjcXI7rC_nm83Fp16pv9ugnVK4993wz5vz1MTkywzhDuHH0Gn3fIsUoEDt8Ri0O2tDguSi5iVBY0_tiPyl7lgB5P8jwtHeaHSA5oecBml3TFScN3telQ-ZIrymp6viIJvHUYI2fLc40Wnacq0bEMrvwh4okHy1i7tSP6BnVJzOjLpLHzAPdF4awFEACnlAOTAAQNqQ7NfCtYmY1XQIrMzR5H5tR1zgFHMgAXPMUVB4kV48WlOn8vNJzgcDM-3A4aQ_VrljZC252ltwiRHEo0s448XpNzhiw8uFTQTBc0-hbV0wnTIUvgwr7H3dWNS0omI0zx6v8zGqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
جادوگری و هرنمایی لیونل مسی 39 ساله برابرستارگان‌انگلیس؛ این صحنه از بازی دیشب بود که یه لحظه کرک و پرم ریخت که چجوری نتونست چهار نفری توپ دو از این پیرمرد دوست داشتنی بگیرند. تهش هم مجبور شدن روش خطا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25859" target="_blank">📅 17:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25858">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mLwk_Nx67jgfhr9aPurVZE2HJj_tt9a73xYuy5mp4Q_OzAuoWdd7YTlXlsbfQTpnQKHYmoZxSRY8Xqou08bTRf43weL4kwtB94OEz-v_cjG21pepC8MKy4tLgMZ4bk2kzNYYu2m_2K5Z58EDI45hJL3PkvpcWAFi4TDX_LVU9fPmmnZ2THIII11npRgEcIjJz6HSJmXfEymm4MHCF1EfDCk0-PfqjCUQrFqhEQrnQjsskK-Tgs2ovOeMW0QhWnEnvL_JWwMwa9boc-jFfgwCMMxRnr3Pcd7Fwq96ROtMW_Gi1C_KLb8zulRjbkLrXZ1D8JWruMpY2Z4lx3jHojZdLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
🇪🇸
#فکت؛ مارک کوکوریا مدافع جدید تیم رئال مادرید درمرحله‌حذفی‌جام‌جهانی تا فینال حتی یک‌بار هم دریبل‌ نخورد. یکی از بهترین‌های این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25858" target="_blank">📅 16:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25857">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGuSzgBbrkCMk0u3ht7pDplcuKOWKQH0dERNIVHeFqVzbB54E-KpMlWUwhX0-DBV32jXukhegbMstDf8SaC6lLFMN9KO6Y7bfVuQH-_XSnls6nO8CIheHmWzYwOiYkkUb2mnS6z1mzQEC68vQRVDuWTuqSSsiWpjctBPQ5mwjB4cGlgwuL9lrHNrfU0o2epVsnj-PiBfTeuHOnji9RGPp3d33JMmy1ORNWSufgsfqKYl7xZPax6AocP34JbLCBbGYWErs9U8y-2Bfc6RSzqi6juB5OvrdCv6fJLr4Hx-T0Yr8vpS5nRJvwMh_rznYSALCZWluudYWURoNAy5rTjicg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🟢
#اختصاصی_پرشیانا
#فوری
؛
مدیریت باشگاه‌سپاهان‌باارسال‌نامه‌ای به‌باشگاه اخمت گروژنی خواستارجذب عثمان اندونگ مدافع‌میانی26ساله این تیم شد. اندونگ دو فصل پیش عملکرد خیره کننده‌ای درگلگهر داشت و با 500k€ به روسی‌ها فروخته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25857" target="_blank">📅 16:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25856">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOnxfhVRZODyRfRhUpR2rFKhSVLGTiEmvl63cYh5k0HdmcYBcdelx-XWoEwp-MRKZv3aWhq1-_MMcF40fmCYYrF6Vw_8Ku-azJGz-XpSswe1yKWGuXbD9_QVryiLw-h5Q97RL8ESG0SW7Bvlrl-6aJVnonYZg-7P0hpwc-STtokGAdSjvKYFvMOuhXuUpFDEueDdF9NW9dxKGKW76WoBKbnvyWYVsj83O3OA9A4wAt1AZneNxdAHRRZrUgZp7lTVPEjhVnlDUjjhflPqfoS5YsSSfHROuD1gpg0smMmSABFEMNpqFz2g7NrwyLlq74rqjyaE6vPAUfr7BQbpIJSUgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛بعداز بالا بردن عجیب و غریب رقم رضایت‌نامه دانیال ایری از 100 میلیارد تومان به 190 میلیارد تومان توسط باشگاه نساجی؛ باشگاه پرسپولیس امروز مذاکرات جدی تر روبامدیران باشگاه خیبرخرم‌آباد برای جذب مسعود محبی مدافع میانی 22 ساله این تیم…</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25856" target="_blank">📅 16:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25855">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4hXJ_W-HuuvSMsOCcQ4huBfch6dtOjRy8ZIc0l8V6NKB5pHOWFbkyHBHphe3ioUTI7_HUJwIULrSLtg1Ojul2x0wIyF4q0KdGFLPP4r2QBEk1eOl8kC_FVUPZIF74ryiJAFVwbB8PHch320XLaZFwc-DbMeUw5S8yNTYxPypPD83Bw8QVu460wveY5HqP5lj4_MZUVgXjj6k62QOGiadr4Alxj-jmLRGrPxF_0ishVlL1RJcGFlALhEjq24u0pxzWtPIGw2216-ciDkui6V8O6dC8rWHOxchBkpAS1lru6FSMtSpuTeUlcGv9_lRjG4V0yKFrw27dXh5bEDagbKug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
دریک رپر‌ معروف‌‌آمریکایی‌در دیدار با کریس رونالدو به او اعلام‌کرده‌روی قهرمانی تیم ملی پرتغال درجام جهانی مبلغ 5 میلیون یورو شرط بسته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25855" target="_blank">📅 15:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25854">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38af4244ff.mp4?token=CXQavJ_SzknC4g2R_7U4vh1SoCcftMSocRpKW2CT3drOhDYvGXpSXdT77mb80i8939oG7V0PFAcO7VIxrU_f3WUc-9WERPYFuJVWoQXsg4IiUH58lwd1Q72jl7cRw25pWOvU-Bo3j725Chp6oMPSFnm1FosHZY9hkMrZC08WUJBa8r9YlqSZsOvmQNfSXyVHs1xrHEfWF0S3vu1SwOlF8uMT7iOIpVgxsvz85LcGP7ERGDrCw3wHLr7ATnGn0UM4uD13aDfvvHwLP_wtqkzSxpxgKW6IYJM12a_GwJnSXfgFS3NIeDi1QQzFuJ0wFH7xaYKmUVq9GJuNGpjFhmZIxDbIbChLS4Mx_M2DCgkppf09HnysYWA1TcyMkMteYZucWSxRupYEMyUqoXJ0I7z8rlUNRlyHeK_FMJ0CQ3qkxXeSlMxh7d2-JHHBjri8vcRASOuV9WkSu4rCDhAdZh-cKWOzrPKJHUu0g9Bw-97xy5vNadxcKIacHZkaAjjFy-ZI-l2K2plmMxJ1aN-F8xu-oK6dkx_z589sP84I47mdbakyxyM-q5B1cZXyLnyjmAFkMR24k9KfA7Rs0iTx1SWJburaUuTq80yd4fwq1OI3r2bC6D2XvGnSVFYVIEwagpdJVy1wPzJuWI7xzclrpIIN3NASdq3BjwsB0Phmh3eVkeI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38af4244ff.mp4?token=CXQavJ_SzknC4g2R_7U4vh1SoCcftMSocRpKW2CT3drOhDYvGXpSXdT77mb80i8939oG7V0PFAcO7VIxrU_f3WUc-9WERPYFuJVWoQXsg4IiUH58lwd1Q72jl7cRw25pWOvU-Bo3j725Chp6oMPSFnm1FosHZY9hkMrZC08WUJBa8r9YlqSZsOvmQNfSXyVHs1xrHEfWF0S3vu1SwOlF8uMT7iOIpVgxsvz85LcGP7ERGDrCw3wHLr7ATnGn0UM4uD13aDfvvHwLP_wtqkzSxpxgKW6IYJM12a_GwJnSXfgFS3NIeDi1QQzFuJ0wFH7xaYKmUVq9GJuNGpjFhmZIxDbIbChLS4Mx_M2DCgkppf09HnysYWA1TcyMkMteYZucWSxRupYEMyUqoXJ0I7z8rlUNRlyHeK_FMJ0CQ3qkxXeSlMxh7d2-JHHBjri8vcRASOuV9WkSu4rCDhAdZh-cKWOzrPKJHUu0g9Bw-97xy5vNadxcKIacHZkaAjjFy-ZI-l2K2plmMxJ1aN-F8xu-oK6dkx_z589sP84I47mdbakyxyM-q5B1cZXyLnyjmAFkMR24k9KfA7Rs0iTx1SWJburaUuTq80yd4fwq1OI3r2bC6D2XvGnSVFYVIEwagpdJVy1wPzJuWI7xzclrpIIN3NASdq3BjwsB0Phmh3eVkeI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تاییدخبراختصاصی‌پرشیانابعنوان اولین رسانه
🔴
محمد مهدی زارع مدافع 22 ساله سابق گل گهر با عقدقراردادی چهار ساله به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25854" target="_blank">📅 15:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25853">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7_t8YG7nHgkimNhHNwdHjUWZrUDdsnIZ6W_-jCeJaktN8N5Hbu1wIvnyNyizEtzMEGsrBo2B1TJ6Kd75hMO6954Nuf9PoubPyYRKxl-oQwr_A72TKCbstsrPdqV3JHhAufSItx50GnrIfFo3ezeXsQn2wih8W3qqfJ27MCFB98engGR-mTL0GZGAZFEj6NJ69cNMCMyzhAwSRioHwpNyR6H-Pdkn3ncU6Yqni7kOVSh481lNFv39UleeM60APx3RbwWpUWOY6zZaYQTH85KkfM_HG1ZDO-EV9O5cKpzAYbmyG0MgeOlxHwbzeKGs1oKKgNbjwRQt8jSt7Kv5b0vgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
#فوری؛ اکثر خبر گزاری‌ های معتبر خارجی خبر از قضاوت علیرضا فعانی اسطوره داوری فوتبال ایران دربازی‌فینال‌جام‌جهانی 2026 بین تیم‌های ملی اسپانیا
🆚
آرژانتین میدن. امیدوارم‌نخوره‌تو ذوقمون وفیفا هم به زودی پوستر رسمی اش رو منتشر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25853" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25852">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTxws3QLMQeKMoY2cEldVLlBmTsFiX4przQjcoqTNEQKzYTMk6xguR0GnscwpmtFt5RmBOaFLm5cjqv0DTxqD3dbV_sKX9d9n_g5nss2fyR0mc7soG8dkjMoDIxrcJSt0ucx2seDnpKI-mFX5r8XC-3yoaM4gXLGgBP4QdZ0uxTPrKh-VgdOHVBufklxxfdRxoynrXk1IVS3UwxQc7WZHDuk4SOz9ivBhNNOuuqXg830l-4gNFx3NN5fX_pvtSfCPlSwZHF5jYZmaWu2F6kiwKa2KOFydZzHhNQ2zcyjcPkNdJgzZqrfxCQW9ijpdCUl80PYlOZkO0hojePB-UEZZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
پوریا پور علی هافبک سابق تراکتور و گل‌گهر باعقدقراردادی دوساله رسما به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25852" target="_blank">📅 14:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25851">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYtM0AjHfsqWlE7e1a8x1HWbFWbEcoZDqwgoBKvlFr7iqUjJq0r3iIeA0nPV3gJYeJWobw7lg31yNTZscy9qQ46pslm-dWs0ay7kYZlGldgpv2bwVOaYyqnGF6pNNo7c6Co1IbwbfTZsXvp-ygCuVp5pelOicd8mJNUwRGkuPwEOqOAOHpHQdfqOkWRrDjyqq3VuBGEilI72sgHVzeAq1ew_48KlV1ixWs15nZr4k1LA81WeJ7Bkj11w9PQ_RqNQaBcBgjVXK58bLBUaeCZWc5GhvqZ_h866bZ63_U1dW4G3LLPIMc56G9BShm2I0gfR2JdVI2hy663ey9FTE4xoVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای تقویت خط هافبک خود؛ احمد نوراللهی و محمد قربانی 23 ساله و ملی پوش رو رها کرد و قراردادی 2 ساله با پوریا پورعلی هافبک دفاعی30ساله‌ سابق گل گهر و تراکتور بست. پورعلی درتراکتورِ اسکوچیچ کامل‌نیمکت‌نشین بود.. پوریا پورعلی جانشین میلاد سرلک…</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25851" target="_blank">📅 14:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25850">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTWfz2kcM-zHVtsOgkRbx6RCiARenJj5l_4wrplV_C-JS7ZbifcIpVuXbYHbROF8nSh95VRUVXyFfDYuOZ58HEtIbGHKXAVlvkVXisXL5xAdSeUPo-w5XD-rM3gfaawudFKQs5MASiQADaiYeJpEjNGz8kl7wLazafIFbR63IiINPc6Sps7KllDkkB3vy6nk_ZMiCbxXV5KMlEph3STrFpao_QOHxe7r0BW4pH7Lb3onkWtdUZHtOmf1sof_RJxLdeF9lCgsxepTu3rXBWFrQfPLvnWk0YKS1ZwDC2sS5Or8O4p9HaM17RKbgbmobbFOUtLJgekd4GqROGqQCrYATQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبراختصاصی‌پرشیانابعنوان اولین رسانه
🔴
محمد مهدی زارع مدافع 22 ساله سابق گل گهر با عقدقراردادی چهار ساله به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25850" target="_blank">📅 14:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25849">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txz9Ynn8NcXlKa21Et12mBb70pAMD2DR4xRDt4azFLAecI282_K2Wj5KaS-FxbhJMdIB7aQ43-NeRrL3pCLXYn9Hi4G5nq9SMzC7FNP-D3uRzsyLTAj8xwdiSaqOPxSssu1kkS_PE7TdNA875x8OcTirHo9OmcpvujA9neQ8yfm-BtpGFUBSA97yiH1Y5TvFvzxhmGxbQfflu7hrzF3ZvFlWv11hlFWMRsXAAz101MvfvycuMiZdXx337n4OwqmoNSbF5x2wH8FLCgmX9M55qqf_ETvxFCfm13LTNMbeqU32vPk4r6nNtoWQqrita4qvDXhGVAElM8Xf9-0edjS58w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با مهدی زاری مدافع‌میانی سابق گلگهر به توافق‌شخصی‌رسیده‌است و این بازیکن‌موافقت خود را برای‌پیوستن‌به پرسپولیس اعلام‌کرده و تنها توافق و پرداخت مبلغ‌رضایت‌نامه به باشگاه اخمت گروژنی باقی مونده که انتظار میرود ظرف…</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25849" target="_blank">📅 13:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25848">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfKXy7vXCCDd20FIc-ay6vDfgNY1EpC2OYjHcgKDLgpuO1XqMvKOzU-mcq3QCaNEzD-nWPZI3zAJMfURXfcCsn8LBGv5A76b4diPHk-PTVuKLWmbFgWqpnJ5KBeVFXtXcXKcmI7OPKCAN8k5zPqfjKnd3vA0nbqIJBbFIi-3Ywev2HgS7W1OqdE-YvJTyiQc7jGaIA-55FAENkq0eQ4Cw-4ScWAQdeRKc9PMU8frtGzoUKAmALFECnG1SToz0OAYWXk0qaUtDFnBu2Az_GNEsimoRevI_ng9TM6_7es4sC8oHLXhx4RePGikTysj_xjOCWqtcxNavbSShKnLRztJ7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ مهدی تارتار سرمربی پرسپولیس امروز عصر جلسه‌ای‌سه‌ساعت بصورت ویدیو کال با مهدی زارع داشته و بالاخره او رو مجاب کرده که به آفر باشگاه پرسپولیس پاسخ‌مثبت بدهد. مهدی زارع به‌تارتار اعلام‌کرده رضایت‌نامه‌ام رو بگیرید می‌آیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25848" target="_blank">📅 13:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25847">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oY5bEj-6XX9dSyhVPdDoHkFb020y9SJtR8uX4ZzgCYIS8_LP8VrIL339aMRDeEREEoRqHnwR3E1NyvFxRZDFmHv31tEVxT3wE1XP_LUEwYDAqs1jV5XugAxzwUBRMW-iwh8TRGoTNUxQ2mwG-IPVTnA3PF6vLp9htxFzu9-WBNNCTTW7PIxs4Q4coCCtQHVrqeALmMnUPNDQsury1h0GC8VQalavyrTLEMGaz-EhV3zeuLuIsxGdTfXOXaqBKRcPS88dkT2uMoeAHbvm5V1BEmRZsp2axOlDRQv4ou3VSSTP3aoW_D9cctFxGKd-BMv5fZAu2pWH-K7haC-WO7QJVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با مهدی زاری مدافع‌میانی سابق گلگهر به توافق‌شخصی‌رسیده‌است و این بازیکن‌موافقت خود را برای‌پیوستن‌به پرسپولیس اعلام‌کرده و تنها توافق و پرداخت مبلغ‌رضایت‌نامه به باشگاه اخمت گروژنی باقی مونده که انتظار میرود ظرف…</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25847" target="_blank">📅 13:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25846">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uhm584W51J6op5PhOet63zlB3P8WagwQqTZ1wyEDrxHuxdDoa6q2rZpzT4-t_-HSzd0YSU717EBDzBbvbPheHKB5qCgH4a9iS23TfxccZ2AuW8ydNHIxnlp5Vk24Ycquo-THL2KjmcaQq590Zae4cntJ5BcDertPE6mEtC6KyanBnHb83zJ32cRcD2XtWujPMOzp6cu-PiFEwONM6nTwRSTP5E5YCNLXaHHD4W7Ii30a_eueMpwugW1ah6FmUuoSw5OF5wnAQn3XCaTMXABEdyhlndVYZLnKppym1xDLDwBuR2_pN9YcNmWwIgKQWwHBzP15lGl_2dfPCOsg6pqj1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
‏دلیل موفقیت‌اسپانیا مشخص شد! نهار قبل از هر بازی آنها را یک سرآشپز ایرانی برای بازیکنان تیم ملی اسپانیا کباب کوبیده، جوجه و چنجه درست میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25846" target="_blank">📅 13:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25845">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4018fc48ba.mp4?token=GIdPTYySYNat8_puWK4c3JzbfarPNJRDV2Ux7Kd80IegegeT1l3GXoTK9Xp4DvSs3I9GqazsK2Irrr9tVQ8veyyhU646bL64WWmF2grM5f5hN_sERqdRb61dAv6hCSrPtWpaH8OVt5vDwCY21_Kf4EblT1DaQgKN-5vZ98gXJLxONw3VIgF3y90wIHF9Sy14WHFPto7pvQ4D2USQgZGI1g7pZHT0MIBkCMFqkMkYulu7OUTxIEuelZZVgO0gTfWNlvDWFtGdv7gJZQXc9k-DT6znOFI4e1nDsOaGzAwIklDE9aWc_YEQTzkWDFbRX8WOmyh5qLoVmpEEZsltAvjfFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4018fc48ba.mp4?token=GIdPTYySYNat8_puWK4c3JzbfarPNJRDV2Ux7Kd80IegegeT1l3GXoTK9Xp4DvSs3I9GqazsK2Irrr9tVQ8veyyhU646bL64WWmF2grM5f5hN_sERqdRb61dAv6hCSrPtWpaH8OVt5vDwCY21_Kf4EblT1DaQgKN-5vZ98gXJLxONw3VIgF3y90wIHF9Sy14WHFPto7pvQ4D2USQgZGI1g7pZHT0MIBkCMFqkMkYulu7OUTxIEuelZZVgO0gTfWNlvDWFtGdv7gJZQXc9k-DT6znOFI4e1nDsOaGzAwIklDE9aWc_YEQTzkWDFbRX8WOmyh5qLoVmpEEZsltAvjfFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇪🇸
تصور کنید توی اوج هیجان و استرس فینال جام‌جهانی‌بین‌ تیم‌های آرژانتین و اسپانیا؛ نتیجه بازی دو-دو مساویه و بازیکن ها رفتن برای استراحت بین دو نیمه؛
همون لحظه بیژن مرتضوی وسط زمین:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25845" target="_blank">📅 13:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25844">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRQLz3Wn8UQhfL2PL4KC4dgLpbwoAyCV6yvYV14jL11Drj4cRv4MoQ_JyIURaqhTy0y01v8idPK86-Fh0Yvf8XIn3SQEDAi65A7hULA1tmFess3c45cc90Do21zPZD2FB3kkvoTdnWk_xC7v5xnKELq3Vb0NWIcFpvqpZHssfKK_FhoMwQbg5OvwOiCh9plyRUsEYFj4dTNH5_DRYYOM6-k_VlZzq9fyZCVxWsC-3SFFVU9ml6gLGPcpH_AH-KdfVMtNdwTzhdXGwH2sELZFZW_tHEPFSYwGyhrUw3gzogmSLQdgVQtg6-rjWgBBoCWFWt9mN3PP3V1crnwzS8KoLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
صحبت‌های‌عادل‌فردوسی‌پور درباره‌قاضی دیدار فینال جام جهانی: شانس علیرضا فغانی بیشتر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25844" target="_blank">📅 13:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25843">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c31e28929.mp4?token=SepFvKh-4Iem_hYPRNaKj2qPGnnkme3uwF_iXNMBWkpuI0YA6APSbDOk03MuKXNDqXSvCFL29evtvxc8qqcgr7oLFK1IPIR0HRt2p8OaM0hm6jgp-R2lce5G2tOiRtrhLUcUpXcBVX5mFw-P4x1uT0uw4ZtvVY1iGziixPfA0N180YAaKYDpykWPKkqgXS453ztjfton4U_dJTQBJXHhIeRogtlmku5L82iC87SREEz0RfLxwDsYl-47WV0D5gbL21LNHd5w2FckyuccJceNLUPtJ7ocAeae6o8gWlYMtZ7gE4lOVT9oXrtTFgcWw3xJzaesNllCqNdzGcgUR9J1r3uTjB3lYUE2NnTpXk7W_dmgPNMUofUxxfCYzpXbD6igr1wZ5e7wQRbhcgH5_2KxRYG9fpoTR1-qVatKpyhwVKDLM-OdqjhVhRCfwBi-xidLDCHFflY1GsJ1r2l4siQ57ZwCOjm5Uv6mo2BcsRUsWlPCc-JvlYonSRA6D9mClpCrbKU79aRRMxwudFQub57sWswuemJUkLmKP82qtw2xbP5KH-rbnJsthwAQGQYorZ5Sis2zJWQgN_cbf0e_Is3XDrhJ5o84sHXeZES0ALDTeKnAQiFfbfaEazwTCGyUrgCj0EhnrrfxOhpemmPwKEoOdxIX3aAOpC6_uGKn536LD7I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c31e28929.mp4?token=SepFvKh-4Iem_hYPRNaKj2qPGnnkme3uwF_iXNMBWkpuI0YA6APSbDOk03MuKXNDqXSvCFL29evtvxc8qqcgr7oLFK1IPIR0HRt2p8OaM0hm6jgp-R2lce5G2tOiRtrhLUcUpXcBVX5mFw-P4x1uT0uw4ZtvVY1iGziixPfA0N180YAaKYDpykWPKkqgXS453ztjfton4U_dJTQBJXHhIeRogtlmku5L82iC87SREEz0RfLxwDsYl-47WV0D5gbL21LNHd5w2FckyuccJceNLUPtJ7ocAeae6o8gWlYMtZ7gE4lOVT9oXrtTFgcWw3xJzaesNllCqNdzGcgUR9J1r3uTjB3lYUE2NnTpXk7W_dmgPNMUofUxxfCYzpXbD6igr1wZ5e7wQRbhcgH5_2KxRYG9fpoTR1-qVatKpyhwVKDLM-OdqjhVhRCfwBi-xidLDCHFflY1GsJ1r2l4siQ57ZwCOjm5Uv6mo2BcsRUsWlPCc-JvlYonSRA6D9mClpCrbKU79aRRMxwudFQub57sWswuemJUkLmKP82qtw2xbP5KH-rbnJsthwAQGQYorZ5Sis2zJWQgN_cbf0e_Is3XDrhJ5o84sHXeZES0ALDTeKnAQiFfbfaEazwTCGyUrgCj0EhnrrfxOhpemmPwKEoOdxIX3aAOpC6_uGKn536LD7I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
#تکمیلی؛ بازیکنان آرژانتین بعداز بازی بطری آب جردن پیکفورد پیدا کردند؛ بطری‌ ای که روش نوشته شده هر بازیکن حریف پنالتی‌ به کدوم سمت میزنه.
‼️
خنده‌های‌انزو که‌مقابل اسمش‌نوشته شده بود که “وسط بایست”یعنی پنالتی‌رو به‌وسط دروازه می‌زنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25843" target="_blank">📅 12:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25842">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pX-j8wSEAE6DD6KAIuL_hhmEYqsAVCM8RSv03sjoDFI3QDbqdtChQ4h_d2AfxtKjkOnySYKP1wn2ovX6CMR7sAPNKc2LXuEgRIZrMbwfk5kJ2c_5uMNxI1G54TjnSQP0b1ITe5zPCqzrrFhig1O9LRJIs51ba0H1kfIPbUKv6dIhHP4TwUYdVWxoG73oGDYzp4of_SyugQFgnJAZaP8DjgC92P_kgiMQUIj7-OGgJ11S-MaDsa4P6-A29S5mEKrnepquAl_5dZPnl1qxIfvU3vsFaZNY9ti06uNeD9RnBAQzvPhqOBs459XkEI3z4iT7AEd3JeiWnerKR3Dp8azkXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25842" target="_blank">📅 12:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25841">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Edqs31de8t0n0pJzTFtvuuuJsM_KAUUFysY9U_t1tGSaBhys6QoOi7wK6J6FvJESrUxPem8fP3W57OMn2vcfqcqmRP1QImphki0mrzfbfOT_xhALCJgeXt9yLckyX3lLZ4XIx60I4tkSA4MwW5NuFbrYX6y-cXQ8zVS5oeWSg2Tn56OpPRcppL6E4TeUCXsfYcy5WS9M2rCpWYR9EpcJdvAtaG64vP-RSZJCjGzpnmLomYgXWg7EQXhn9zPSks4ktQtuY8d-9C7QjVSrsCpVXMe4q60RJdztEMoSkfJhcNjPbfohsLoI3A8HV5zsi7xw_UFeGTwVoHg7mIABHswr4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25841" target="_blank">📅 12:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25840">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kbpmGPzAK30v8wdxS6ehZfHGIvZh5bZiU4RSn4pPDd4viPjymBQCDpQmagJMmM3K_ot5UM-BCqLpuRckmgND8u8cWLSirZy_0S3oILz2OHUF0Hd5szqC5Rc_YjaquDF-nx1eRxwHCfpLZ7ky-IKpf92dHgqtRWD8weHscVd-8PLd6cnxfj7lVqb538t5nPEZQ4EIvtSEHEfkAJ98jvLYNjsVAz1xevGKKoh6MT6OzRU_sTD84QLOhVhnYiITdaSXwxCZpnAmgRc8D0IfTjTc9N05D-eDR-PGNQESQpyyZIa0YuJu0V4AG-cLrRVjE6Rd1cdslRtoDi5fC7e37t3zOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با مهدی زاری مدافع‌میانی سابق گلگهر به توافق‌شخصی‌رسیده‌است و این بازیکن‌موافقت خود را برای‌پیوستن‌به پرسپولیس اعلام‌کرده و تنها توافق و پرداخت مبلغ‌رضایت‌نامه به باشگاه اخمت گروژنی باقی مونده که انتظار میرود ظرف…</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25840" target="_blank">📅 12:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25839">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8168388efd.mp4?token=mnRtnsjAsod_y3tYJt3jjZlb6CjYBWYSNl9MygJ2LkdUAeMUFJbt3aXfxb8hAmx-hVBkU0_lFO6X-06rOxGtVW50Qx_NlE5CuoZnk7PIyYxOy-5vv4L01Lj4FLGNQLdxDTINc9qPgEuoixD3RCOzXv_SIO1wvpmsDDhHVAAQ5aUN5v_2L3AiCT47uJKcjZIefXfRGtEWZKwwHqGWmZ9wkjjJ1dOGq4QLjFmeIBp8PJg2BgLiWClweTaQdW5uL5bY7vlSrl9HatLU9jApqYEps6zFanyD3YRzTnYBr1LmH-9nQK7NSoZMD_VItkj8a6IzNSZdb0_SssOk9vrLvLmmu4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8168388efd.mp4?token=mnRtnsjAsod_y3tYJt3jjZlb6CjYBWYSNl9MygJ2LkdUAeMUFJbt3aXfxb8hAmx-hVBkU0_lFO6X-06rOxGtVW50Qx_NlE5CuoZnk7PIyYxOy-5vv4L01Lj4FLGNQLdxDTINc9qPgEuoixD3RCOzXv_SIO1wvpmsDDhHVAAQ5aUN5v_2L3AiCT47uJKcjZIefXfRGtEWZKwwHqGWmZ9wkjjJ1dOGq4QLjFmeIBp8PJg2BgLiWClweTaQdW5uL5bY7vlSrl9HatLU9jApqYEps6zFanyD3YRzTnYBr1LmH-9nQK7NSoZMD_VItkj8a6IzNSZdb0_SssOk9vrLvLmmu4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شش پاس گل تاریخی و حساس لیونل مسی در شش جام جهانی که در ان حضور داشته رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25839" target="_blank">📅 11:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25838">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FfBQdl_GeLz2Z2j0CkEXVY9X6CAfhTMEPUozXfs5AdYG6_rKh1WzO77nH_HjR9VqMli9Y9ZlgNByGVZgBaykX9zRlqmKcO80O9-VeqZ2mSKaVE8GQlpPpCbeS6Y1zvXP_mlCskTdKzUHlBc4T6KL0pbgN9VUOodKxzduvQ5OpHDqCz3tWqLclMVZC_97LHRXJtfLKeLrzCNyLjCXqTAKZ98UH7eaAg9mmn6zOIzNuqiwUk2q1XCqKSSw50746Piv7MbVyw5ABlMnr_qlW-oEM47ztQkHhEHWAQmRC6hxHmQDFqDuGxyrUwxkvbi9QaL5olHN43SY4GfBqhpi0dHuCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ داستان‌از این‌قراره درسال ۲۰۰۷ در یک برنامه خیریه یونیسف خانواده  نوزادی برنده raffle برای یک‌ویدیو و عکس‌بامسی برای یک تقویم خیریه میشن! این نوزاد ۵ ماهه لامین یامال بود! این جوری میشه‌که مسی ۲۰ ساله لامین یامال ۵ ماهه رو حموم میکنه و باهاش عکس‌میگیره…</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25838" target="_blank">📅 11:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25837">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇦🇷
شادی‌کارمندان‌خبرگزاری آرژانتینی در طول بازی با انگلیس؛ دولت آرژانتین گفته اگه قهرمان بشیم یک هفته تعطیلی رسمی در کشور اعلام خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25837" target="_blank">📅 10:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25836">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f89c12ba90.mp4?token=vljoK9OdZdnt8r5fMFwZWdY-beOwaT7uLfqik3CgCRyhgzrlF4meohYbcnav6eyON1B72JwHi2MjwH4fXmZP5w2_nnA5u70xPbFfLY1syy393xqSGt0eIQ6A08zyX6-RjiwAJoptjd4syi0T4hhHuXLclDXKy-UGF22zz5eSvxNKizHB4X25V6ESuFymP6L78mgXixuBZIDuj5syUg_EKVcXYt4-JglL3-RF8AQelAjWv19tTnqvpCGvHu7ALm0Rn_zZ2XCmee-0E_ZtVMSFAJ8Yf2Jrd1JyeltknJ8FcyLRlcnBFrClXmz7GwA2YkYi4gDHLTP6JFtFVbOciRiQEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f89c12ba90.mp4?token=vljoK9OdZdnt8r5fMFwZWdY-beOwaT7uLfqik3CgCRyhgzrlF4meohYbcnav6eyON1B72JwHi2MjwH4fXmZP5w2_nnA5u70xPbFfLY1syy393xqSGt0eIQ6A08zyX6-RjiwAJoptjd4syi0T4hhHuXLclDXKy-UGF22zz5eSvxNKizHB4X25V6ESuFymP6L78mgXixuBZIDuj5syUg_EKVcXYt4-JglL3-RF8AQelAjWv19tTnqvpCGvHu7ALm0Rn_zZ2XCmee-0E_ZtVMSFAJ8Yf2Jrd1JyeltknJ8FcyLRlcnBFrClXmz7GwA2YkYi4gDHLTP6JFtFVbOciRiQEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب‌حسینی‌توویژه‌برنامه دیشب جام جهانی پدر تشریفات‌ایران رواورده میگه تو دیت اول چیکار کنیم طرف خوشش بیاد و مخش طرف رو بزنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25836" target="_blank">📅 10:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25835">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/if2egYQWV-CsqPTvWLqpZW98z6U3b8Y1F0dxknRd4cAN1-q3qaF-Qm9a7yI7vkSBkVRWX5UVFFOz9aqYSkV22ETGbn6AxN2trFwOWlGTpaJgr0zv-1_tTEgWVnpnyKjEFdCkWjxJgcnMqDTXcdaVjcAIt2V7vdoq0lZQSq86byZ69GolNzNoB8ENC7IKd7n48dBASaPxDA-IDzf-whj8vvUD-8jb_MhLEagNCfgjAT124j5S8dg_Uo--QTmpt221u0IX0Jny22KdYDpKphpPgaz-5Jtv4jCvMypA82V0aC2aj_KMfeKywEKXqlZpDbcWoMeDyEPcpTSWO085DSCPwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
درآمد تیم‌های ایرانی از جام جهانی
2026
🔵
استقلال: ۱.۱۶ میلیون دلار
🔴
پرسپولیس: ۱.۰۶ میلیون دلار
🔴
تراکتور تبریز: ۸۸۰ هزار دلار
🟡
سپاهان اصفهان: ۵۲۵ هزار دلار
🟠
فولاد خوزستان: ۱۷۵ هزار دلار
🟢
ذوب‌آهن اصفهان: ۱۷۵ هزار دلار
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25835" target="_blank">📅 10:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25834">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/892cce16f4.mp4?token=nEsMpqLXjg_0YnUwT8G89w6yjHFXWD8Ouvzm35STxMeaX55D0H9EOrlt4qdtvXX69xgS6DfK9CMcVGwkGldivqHYGLc0PfWiC7Co6BOkfWxn9fapx9VPjhIzBTgwrCsnDoLlzGkei5ehN4_bP7elRDmVjiIAh_h8xe0AIVpxcHiTAsE6QJKs7e25_Q7CTscql4ewOkAgs9l9lTalXawro2sMRumEQi2ZBwbE_LfahfDGxZJXlaaauL8IHDmCDSBgzJ4S-5QIaIXeTJD8g4wySznXlkftoQUOTBnngeQ7wSXALvsoJ-hlHCRXiqMMEVH8FmblV9-V9TKmplEK0Cltuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/892cce16f4.mp4?token=nEsMpqLXjg_0YnUwT8G89w6yjHFXWD8Ouvzm35STxMeaX55D0H9EOrlt4qdtvXX69xgS6DfK9CMcVGwkGldivqHYGLc0PfWiC7Co6BOkfWxn9fapx9VPjhIzBTgwrCsnDoLlzGkei5ehN4_bP7elRDmVjiIAh_h8xe0AIVpxcHiTAsE6QJKs7e25_Q7CTscql4ewOkAgs9l9lTalXawro2sMRumEQi2ZBwbE_LfahfDGxZJXlaaauL8IHDmCDSBgzJ4S-5QIaIXeTJD8g4wySznXlkftoQUOTBnngeQ7wSXALvsoJ-hlHCRXiqMMEVH8FmblV9-V9TKmplEK0Cltuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
مقایسه‌عملکرد لئو مسی 39 ساله در جام جهانی 2026 با لیونل مسی 35 ساله در جام جهانی 2022
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25834" target="_blank">📅 10:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25833">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03c6d437ee.mp4?token=cdACjp6l2F1FKDJB1L29Ip0hPzClO2BBle84CI-_GUDae7fU3k-e0jVyJtzLDson9C9LI4MrxItLDGIr0cnCGsFreT3tPKbvhQyOyb-F1-3Yx6Vag_i21N7dirKAEQws1EiD5K0wZM6HYMEOcEbsJo69VVat3PnupKU1G9T4eTgyMvJrXrJTKEZ-L9QhF0IcTSs3VPtXk70bbxHdtGQ7HrQH8w8Ch8hgo98x_uj13irjRsnE5lISqC2_ibutgndv6koK3SjjME4Lh6Li2so95S0D3UijoRLWmuX_lXtkqJeoRU_4dAu4qMXSbn92_KZIajb0YxvDRWw_VHTx7aRzsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03c6d437ee.mp4?token=cdACjp6l2F1FKDJB1L29Ip0hPzClO2BBle84CI-_GUDae7fU3k-e0jVyJtzLDson9C9LI4MrxItLDGIr0cnCGsFreT3tPKbvhQyOyb-F1-3Yx6Vag_i21N7dirKAEQws1EiD5K0wZM6HYMEOcEbsJo69VVat3PnupKU1G9T4eTgyMvJrXrJTKEZ-L9QhF0IcTSs3VPtXk70bbxHdtGQ7HrQH8w8Ch8hgo98x_uj13irjRsnE5lISqC2_ibutgndv6koK3SjjME4Lh6Li2so95S0D3UijoRLWmuX_lXtkqJeoRU_4dAu4qMXSbn92_KZIajb0YxvDRWw_VHTx7aRzsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لئو مسی توفینال‌وقتی لامین یامالو می‌بینه: تو پسر حشمت کی‌مرامی؟ می‌دونی چقدر رو هیکل من خرابکاری کردی؟ امشب دیگه‌کارمون‌رو سخت نکنی. به نایب قهرمانی راضی باش قهرمانی برای منه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25833" target="_blank">📅 10:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25831">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/on2LQfCKczPbwoKGLJRrziY1OWfM6BcDBDbXY1NNFME8PLBa1zHB40nWAzRvCrnlbtQU83PBesSI0ejIVGV0g1Xn7pVxs9hdPaejzfGx4kzidUQ88-wClfgzDDhPSYx7gpASmB1OpXPi2GlrM1zR7MqoYJSgtwZWodgCCTs3rGRb_jxitaqCGTeZ0bTj5IFm11Pb3qm8JHSmZngW7o5GlhS0WiyNdDqYnZOYd5HA6L7bPJR6kavMvBgFp4FV7x0ZzyYvJ_CxirtThA9OFZl9xKVa5NkYYOLfZKAP6aQVtnyhSmIe20Mgu11_hIjJ-si-1X4fbD1ABfNiKGgBd5kL7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
الان‌مسی‌داره باخودش‌فک‌میکنه که کاش همونجا تو تشت خفش میکردم که الان برا خودم آدم نشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25831" target="_blank">📅 10:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25830">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه جذاب شب گذشته عادل فردوسی پور با حضور علی آقا دایی و کریم باقری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25830" target="_blank">📅 09:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25828">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SGUFHiZaTVUUjGw89fc3TJmBbabNwmnCwOo4uFNF73CdoUAb3_eaC6ywCcd2_OKOWiwifQJAcnh1gCOXES2zOwHdgYNa2sIllZ5hKX4ozI5m-hjcq845PzcZDtaxSL8g71iC3TERYFGiwkYpckvLsn4Cla-XxA6TO2WUQShWNFgTAFkN3ZXJ0Ze6eQFfLrpV83aaUK2aAPTR_jo4EKVrt_FWqqzdhbz4st6rsYoRPv7yXFDrwYtSFB1zID3jPJwPxIWmJbtpP4aeszNq573H0jj-CTG5ItpIa2zefqFHG6c_kGhAUSDqjnzM5lbBFQvU22B7bgOn0aR82_yo27CMaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KQxj_NM96OZC4k4-5fzQjNzd6bS3noFGaMBB0e3agOLPeRd4CWrMTaNJamfGsp0z6rcN5eW8jUo2CFDT2SFy7RVFVKGq1E9aeljGtZshC9mcIC7bkr_5xntYBVphtw36n4m5V6wg7kjWNXjCPJGwKB6ik1tyRLWRpBni38vSI1ZvUTsQSphc3ZOJJ_LzS4GiTBF1zvgsucCcRt1LpNptGkUS2yjfWBPwiuEr9RfZSfuJgRyHYSjhXZD4_rsz6dAyVkEsl7G4bM-a9kyD-LkxYLGk17oSbiGgM_pmOtSFRa5hwBUB4dhN5fILLZ57rshi-O8vSn3pOQGf3p-1xPhpHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
رده‌بندی برترین گلزنان و پاسورها رقابت‌ها پس‌از پایان مرحله نیمه‌نهایی‌جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25828" target="_blank">📅 09:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25827">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBO30URFhXjfXRzdpqrQw3x2pNrySC8ujLY3rXUefwsEljf7vBB98ZdWIPQdo5ep0ZP4pyYD6DCxOcqpLfjkn8Re_ajLEFz0ZZfk7gVSnY0XpHIyzh5isyOulHf7H9d-yQ20MFeNQqJSHSrKl-HaurEMeBmNRy4I-wVNHe7BuR6OA5REfZSpfKvTTXJ8p5MsTuXmESeKxlhui6whuaQ0u6t04iX9OA5Nu1I9ZulFIDzrNaimGLZXI_uc5T1Q3ZYh9LnVrIFH6FVKqw0Hm0OVbc66Z9UFAdQvKvKipioKe4NWnZkW1X_jCHcE4hFSsLAlQ1IL8yrSeq5kCSIfaShLpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇷
هری کین:
باحذف‌ما من دوست دارم لیونل مسی برای دومین بار قهرمان جام جهانی بشه. من طرفدارش هستم اون سزاوار قهرمانی دوم هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25827" target="_blank">📅 09:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25826">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa7c3766c7.mp4?token=VIEFMzSqHWnZ42JL0thWVHOaiWvtEUMWV3GC7YoaH7SNBf5nGI58zscc6cjnyYGdhfM2HmuQ3AnaMQh1qGpl7VwfEo0zMgjY2jNxNaWyjtTbK9WmYdNcV_A8tqg1mCWGIobmpIKa1iMU0qtrARRE9lIgLAfn_BWCwoT_3Vp-qCYtXSUsJwprsHvPAtn_YK_XD_MnUy3Z0MIFEpKgbey2qC6LefWVJi9DypaHN72mdngolEYL4RZfRVdKHy2AHsIg6Clu5-56btDaPbDFo7PCjfB-v-Cm6C38eF2a4j0wusAwd2qLRYrqBtVuXZJkkF_7tzZ_Nn9b4ByFNobLRNF_5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa7c3766c7.mp4?token=VIEFMzSqHWnZ42JL0thWVHOaiWvtEUMWV3GC7YoaH7SNBf5nGI58zscc6cjnyYGdhfM2HmuQ3AnaMQh1qGpl7VwfEo0zMgjY2jNxNaWyjtTbK9WmYdNcV_A8tqg1mCWGIobmpIKa1iMU0qtrARRE9lIgLAfn_BWCwoT_3Vp-qCYtXSUsJwprsHvPAtn_YK_XD_MnUy3Z0MIFEpKgbey2qC6LefWVJi9DypaHN72mdngolEYL4RZfRVdKHy2AHsIg6Clu5-56btDaPbDFo7PCjfB-v-Cm6C38eF2a4j0wusAwd2qLRYrqBtVuXZJkkF_7tzZ_Nn9b4ByFNobLRNF_5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های‌عادل‌فردوسی‌پور درباره‌قاضی دیدار فینال جام جهانی: شانس علیرضا فغانی بیشتر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25826" target="_blank">📅 09:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25825">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Um0mCj3v72Z_NFDgFFMD2dA8xRd7HlmgullZ1n9GuVMfF6tJG9fDZ0rskVTI80qEHRuOVRQ8E1b938cK-_CSBxR0J8fgEdo6NnLhBaOmkG-s3sJy83sOgc8dTpPtRSpMZbk5_bntlVpNGEq8hHtak_GpJdLJI9HoIYT1Q-VfyEmIOaC8Mh49lUHQqgGcb2HCEvbCgDOqp9WUObUPEjCVDyS1JTqvtXErkITql8pbgnvOhNWoRxMtGc0JF4vbKXqsmZLcHRV1M3s7kHJGLkHazImnYJOh9FkcAIGYMj1VJe1JQ8Y6MzYcaPdabjxjwog2Axtp5WRtzFCDb6_ObFglgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
#فکت؛ تو تاریخ بنویسین، مسی 39 ساله، پرایم هالند، امباپه، کین و بلینگهام رو گذاشت تو جیبش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/25825" target="_blank">📅 02:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25824">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eq5ALWCEeUf1WhQ64jAYgdAr7-dqzzQImdx3RWNjHN2xMvl-NcBP_KhqDfeMB_Zd_NhLHz7K1W3ERY65k_O0wgnij6RLC8Qi-WPfIeLjhoAMAP1OThmDyAuB3N1NFH3tJQmaogDtdIgjZmzNMfNDs_ezoUXo37jpzpX_QcOuujZc-7z3Eml_fI3mau3WC1KssuretXT2fnyxSt_xtLsdVw2na2jwP_7zGDCYcooXhzJLsGraP7XsJwFN59KBUuIgWi0guD2Ke1pK9TxoVadE_qZgNhTD61l7fda1B0jDoY_fn-RYY7GWjpeRweiZUY_LGHex4cyRy0liz1-jL5DsGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه ‌تنها دیدار‌ دیروز؛
کامبک دیوانه‌ وار آلبی‌ سلسته مقابل انگلیس بادبل‌پاس‌گل لیونل مسی؛ جام جهانی 2026هم به‌آخرش رسید. روز یکشنبه 22:30 فینال و قبلشم بازی رده بندی. بعدش یکم استراحت و آغاز داغ رقابت های باشگاهی در فصل جدید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25824" target="_blank">📅 01:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25823">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29e18a8789.mp4?token=ECZeZDbMC5--R6O-FHfIN_QbVmfoW92r5gLgWqlpKTfuHh4fDpGrv8zmiCz1J1Uqunckh9J7G0_smgsiPM8QDyNuWIc9ef4tbRwsnKHuGtdOhIK_0_G3GccwfzsQE__3CC2Td89X94qr5ZQgSiKUiUxNOoMZic29VJI1GoMdkeE7BBA94fpUuonx3v6J7W_h27lWfKcQvNdNsfIMwI1ZWUY4jcE6KDAX3DmcnokFiL8AYpIZeUqhty2ClscalIEnQh8offbZPYQeHvuKF3Bc_9YEhVrhM1v1d3JO4e7-_ThsmNGSx7V5w_aQW9FDYfG2LIMvhXUH9i66DuQGffl-Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29e18a8789.mp4?token=ECZeZDbMC5--R6O-FHfIN_QbVmfoW92r5gLgWqlpKTfuHh4fDpGrv8zmiCz1J1Uqunckh9J7G0_smgsiPM8QDyNuWIc9ef4tbRwsnKHuGtdOhIK_0_G3GccwfzsQE__3CC2Td89X94qr5ZQgSiKUiUxNOoMZic29VJI1GoMdkeE7BBA94fpUuonx3v6J7W_h27lWfKcQvNdNsfIMwI1ZWUY4jcE6KDAX3DmcnokFiL8AYpIZeUqhty2ClscalIEnQh8offbZPYQeHvuKF3Bc_9YEhVrhM1v1d3JO4e7-_ThsmNGSx7V5w_aQW9FDYfG2LIMvhXUH9i66DuQGffl-Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
واکنش‌برگ‌ریزون‌اسکالونی‌سرمربی آرژانتین به گل پیروزی‌بخش این‌تیم مقابل انگلیس رو ببینید؛ چقدر تو خوبی مرد؛ مگه میشه تا این حد خونسرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/25823" target="_blank">📅 01:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25822">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🏆
تصویرجالبی‌که ESPN با عنوان " لیونل مسی و بادیگاردهایش" از بازی امشب با انگلیس منتشر کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25822" target="_blank">📅 01:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25821">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WW5nwSHi4sYuv9uDl7P-LFNyqtHmvyaqNGXHkpp--H8Pa7Fau1irx9c_7M8YMGxaG2KSyPy1YO5MboP6wpYT7Uo8TgbMcv_oK27H0-lNWpQSQNJ6ASe96uJ2xc3DVXN-BQIQBud-AZcD9EyAlZKS_4DoyZQlZsWkZcqITFRL5jYtXyhaqi-xA0RHYzOgopOHqWmGjJlcRMiH-xc0iH-xezhtsys36g57BFiKWXn_FQv5MsD2HyCVFPjOubo6OJgBOAEPQVYWLeDvDWfIs7jHtJli4m9k4DkvjFu6hIRpGBbyFm4DDs-LslpvVyDnydsYfO334Rmb8sd8fK4uJFdUSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
انزو فرناندز ستاره آینده رئال مادرید با این شلیک دیدنی مانع حذف آرژانتین از جام جهانی شد؛ دقایقی قبل هم گل دوم رو به انگلیسی‌ها زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25821" target="_blank">📅 01:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25820">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efd102a0a9.mp4?token=fXIl77jnzgt0ak9vzOVKmRBr4ixSfRw3T1p-M_aMR-ZsRSE5g7JftBW5eBxAAn2iTUwX9NME4PjnmxUxeHwbgUJubLXeo8m846ektzEYXIrtVlj7LY7j9IptfELeOs3iuKLfcb3a7rtv6afv0evejWLX8bzmVo0YEbdZqB22QRX8uCH7kvPLPusOUxV2bkkBB-HStqun71z44TNp70HAmxaiTGVZQJBgdOXmMdCRM1ki7oZcEn5KVYZR3ZhUJDjwMdFIcsquiipOTNGr3Z0ysaONCzJ-q4HMAh92VFeWddZzzAhpLZ3NEMnpU1x-3CtKeNjF1CQm2aRppY1V8iKwYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efd102a0a9.mp4?token=fXIl77jnzgt0ak9vzOVKmRBr4ixSfRw3T1p-M_aMR-ZsRSE5g7JftBW5eBxAAn2iTUwX9NME4PjnmxUxeHwbgUJubLXeo8m846ektzEYXIrtVlj7LY7j9IptfELeOs3iuKLfcb3a7rtv6afv0evejWLX8bzmVo0YEbdZqB22QRX8uCH7kvPLPusOUxV2bkkBB-HStqun71z44TNp70HAmxaiTGVZQJBgdOXmMdCRM1ki7oZcEn5KVYZR3ZhUJDjwMdFIcsquiipOTNGr3Z0ysaONCzJ-q4HMAh92VFeWddZzzAhpLZ3NEMnpU1x-3CtKeNjF1CQm2aRppY1V8iKwYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
سرخیو اگوئرو که امشب بازی دو از نزدیک دید گفته اگه آرژانتین‌قهرمان‌بشه به هرکدوم از بازیکنان این تیم یه گوسی آیفون 17 پرومکس هدیه میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25820" target="_blank">📅 01:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25818">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0SMQCnuD-hSrdnjNxI95OjY_bb_tXMOFpxkv5MWpF5533cUh8Bt6WhOvHoF-HhegtYwjF4o6lMtdsOCpBbrdp9VLlLMzyzRu6Wq2_e-uIiktumh521_DJr-MrkKdfYS1PBk4p_-wLhDNSxnx8Zt87CsGu1qwCrTyEKhgCCeatDSGKP8CwC7fo7c34W6_T6gMhXAU1SHcfX2IHqK6FCDLWLbHH7fs-2gnWmeTildfAPOFn58-j19hfKLDVnfsfbgVAc1Sh8Jg-OWYmqEot_Xuvw0UkSgHIHXs6zBCnn4BaLLSt5vjmJT9KdWEj8_KWU-75foE505tkIR7vW9QyPhvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انگلیس‌دقیقه۵۵جلو افتاد و توخل درجا تیمشو تا منتها الیه باسن‌جردن‌‌پیکفورد عقب کشید و ۶تا مدافع گذاشت تو زمین‌چون میخواست تاخودسوت پایان تو محوطه خودش دفاع کنه. تمام این باخت گردن خود توخله. حتی اینکه بعد از عقب افتادن هم میخواستن سانتر کنن هم تقصیر خودشه…</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25818" target="_blank">📅 01:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25816">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vEdDQj2qRWg6wUqBe6ks9CKuvtsE8mSac-UKkxw192M8D0ed71juXQln0Zua0SloC_NWWq8CYGfZjyF04wBu5CY7LJwYlNvZhAMllTsuGm43CNItG7lsCYG7xck40QGzP3h1QagGNY2mAIDxS_8Hhq_O2zQ0nP5RVUk83T_YStzB_Zd1oh_MLwAGLOW0xBFA4-U5ipPmDI9OV7Pqzdq99pcWO_GonQOfY5vIi5KqwbArT1UP5RzuYAjN_NHRD8H_hhagnhhXEONdDk8dVqAkaZ0HNI7Gy_NJ6-80zjpEgAeMIfhOUgpvudBbnlhVV4ChbUcRjN4-omsM49P1GGE7_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
بهترین‌بازیکن‌جهان؛ اون‌حتی از جام جهانی ۲۰۲۲ قطر هم‌قویتره. لیونل‌ مسی همچنان به نوشتن تاریخ فوتبال ادامه میده. عملکردش رو ببینبد فقط.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25816" target="_blank">📅 01:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25815">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHXQw4_QYoTNh1Cu930naYs4d31YuCUTkhNYSUkkAJCG8jtdUdFVTnjQy6o3DCVmf_kAktni-HRgI3Jl5ijawFdLbtSx0YEycfG7wph9atk0428NOLzI9zph6MS6Xlo7LmVnU3CxUTjmB-8yiqML6P6K4RQpVXePsfq5ubTTDwuO7IgxKp9vNg-IGmqfh6ilbWflfMk7x8DGZja6frTod7uyp6N8aRhiD1MNJy2tRWYTbkVmIf8ZpQRThKzX727o3TKVLtwdaZAqMYF4GwDdF4sE0_KuKm1ENZE8VhUGb9I11cqypdNY8XTVacBgApnPO1I7q1stuJtvOSrG2mrmMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فینال‌جام‌جهانی2026؛ روز یکشنبه بین دو تیم ملی اسپانیا
🆚
آرژانتین برگزارخواهدشد. امیدوارم قاضی این دیدارحساس علیرضا فغانی عزیز باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25815" target="_blank">📅 01:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25813">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNyYu-lHhHfu0NPP0QanvsNDiGHabvilfKMuXpxil36Ti2JoUYLe6jB3EjhnFDl2T4Z7BtazZZk9DHq5UQBFnmfaQBxMojtKAiM2OaqM3MVXsQ4CXu1Yo2K1dl6uZWaqNE1UM8OSvflcJrszhvDJgK6B6-BvcyRo9eCpw1TtByh_gaHzImkVaa1dfGLUi1GAjd2yYIzbkP_d4dtmNnnuCIXKXAJ0ZI7RBwEdDNyP3zGrilOxvrTjqcLzq-9jz_UvmWiHy0tjSQDs6HjNDiEAkBfsdQwj5-9wvCc34VgjYUm_dQODUhs1yMCob1l0r95NJwG1Tvj7dRov0T5-cxztDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید امباپه هم اومد:) فرداشب یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/25813" target="_blank">📅 00:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25812">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OargswlQl9D4or7ns8IdYHoPI_88bonmIgwZwmZroNhkQAO2I5-f0khgDN7OjoCu9jN3ahu5PH_hg8iB1D_TEculmdV6F3W737iqACBrd8xzxZ7tesEuuX4wFcKAL0qbE5mQY4YikeY_CdDavuP3OAUmcHGDG_Uzt-FgQtGz6Gg2YhRJBhvJ2O3I7lw4CIOyg_w3GqeBGNtKOlnp5iri9sSQg_4b2aH52KQzyM1BNwN8u_YZJwBTuBm-3_1b9Y89dEBVGQcAlMdb1Y5bQjH9oy3oqsqxWLIajd8-G2O9jt0PIb9b-lS9HRvdmcgySPUHTxfEQUlbxtYib98aDyLvuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فینال‌جام‌جهانی2026؛ روز یکشنبه بین دو تیم ملی اسپانیا
🆚
آرژانتین برگزارخواهدشد. امیدوارم قاضی این دیدارحساس علیرضا فغانی عزیز باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/25812" target="_blank">📅 00:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25811">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apg891M7gB_FCv3NnAtX2a-AEfQRNQMXv33W8oRhSEKYd3oyykvFqbhP-znFKERM4AbzOBOplqS1V8JEABtZ-OSpIR5IkpzkHAqu98LUGF5JLVitXqicN7n1vDNajqXArF36PMal83MCp1VkecYpsiz9BqJZEAf0kZi6wUsELEfa6s2LACuDNWU39Tv2ShNaxulKV-UawCKsVrLfDtbt3Jl60rf3h4-PcBHbi8VymKJb_0uTThAsKdcvrPGK-8-TZ8ryqpTdxd8buWyGUdiwcytTXYIP9mgY9gbTD0qXdyA9HAvIeqBDWTI_0E5uBUAfYSvK8tSHbphQ3xXBDpffRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه‌نهایی‌جام‌جهانی؛ صعودتاریخی و دراماتیک یاران لیونل مسی به فینال‌جام‌جهانی بابرتری سخت و نفسگیر مقابل سه شیرها با طعم کامبک.
🇦🇷
آرژانتین
2️⃣
-
1️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/25811" target="_blank">📅 00:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25810">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIsQCFhV-txhK8Nqw4C1sxZ6k-VMxuR41jR0ddxUvi05tbD0erYCOOse2jvkhfl6Kc0rEF65JjzPCONOc_qvY0ph3cG2zLIZRvlqZQXKtdpZMX2bSjaaedUQi7WGBsmCEzngTAR_vuwQn5ID0lu8TtWfvjTDuFGEcAm_1QXG3p2BYeaxj-Z4Gl8iteDRpK3gjz-uUg36uUpKNJd2MsSZtq1FVScHFjzdYWmdIlhOXVt1JwzmS7-o5U8dT-U_lu7PaJxnZJuVMq-NDkCyqGM5YzuGCU9VXmg4GvpLo-ZMWjpsXWiaMPY4X8AxUSwQ8BnyeL61B9ovIzB2-ZUKPRFWfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی 39 ساله با دریافت نمره فوق العاده 8.9 بعنوان بهترین بازیکن زمین انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25810" target="_blank">📅 00:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25809">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ot_5cL6iGLoX4AsculqR5tSjDL3q6cdhFOL-N4OLQuSEmv6P2zfBryOHKo7URMX6VwfpW7ZQ6A_UJGQfjDsIwE0yUPxahPempZwpl5AqVUZJ7uw5ftjEVmqOGQIUVI68RJP63uk1yoPnn7bxDizdviiPth6OUW1NCoOE7lWnrdyvzkTAOSkEmH9-ulzZ48MFqL26ndf3cjOgcDodLlLEIi-3q3D3at-9sbW0ZVP7EG1PAVKwxBJ4GJh6RD_-GfWA963nItZlnZt6f4wiNLE2KPL5YRKdswpRjbhygsF8JAOQeOHEeXodkGSyRmp9RjPt84FQMZuBvrZtQVx5GyjhlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی 39 ساله با دریافت نمره فوق العاده 8.9 بعنوان بهترین بازیکن زمین انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/25809" target="_blank">📅 00:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25808">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSctktXYIl-7xXryH1EE55b70S86kbn1Jsn6A_gjmRVlopkVqFoZyJHA_FjgPDOeyhqMsud0kD6UpBTdTsz8Vuw4BrJs1jMhTAA8DY5A4NxZAKSbqKMPOoDbaHGLjRa4odNR2jjr7Ziz7za8ge9SQEC0JXCpOi9IYH3uJZ9Y2PyeQr2nqUAYAsKYcxD5v1-laPt_jIo4hkAXpKuXNjbDxWRDvnWnEc23zRPKxs7JZytni-NkOL5vPh8ycOUa2P2ussSAGMBfoWpFBGd_HJQw8CqDWDlVwMuPZrjLG2aUll_Gvbtk39u23NeiXgBuoP2UTh-kXCZsnKNtkYsBR1rIAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه‌نهایی‌جام‌جهانی؛ صعودتاریخی و دراماتیک یاران لیونل مسی به فینال‌جام‌جهانی بابرتری سخت و نفسگیر مقابل سه شیرها با طعم کامبک.
🇦🇷
آرژانتین
2️⃣
-
1️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25808" target="_blank">📅 00:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25807">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjN9uceF1UwVRH2ds0R1iTZFkgVI-jEw4b9-9XWnENKMhSgVvyI_9Qjjt8cUyOcGtKpFdxyDG6bwhvGi_3Vn_h7kXL2SvuP2OId-414A02ehUD7klyP5Afme3qYOu_SuxrzlX-53qmuGrGo0UaBhJTqc8YxMj0LD87kuaHWBrkWixrCBWOMIP1ndP3-GWBTGDfA01vA3VP2WVPrHoDkrBchKDfsmxaPDYJn2wy8dIK-pl0utAtMiXOLPFHf3G8GgUeR2E14dSMPPylW1itDQIkCwu18D1sZOughupwON9QH6TSeJbdzOFdb6_vdnnwP1R6QMj1WACoSx0vitzUgTew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
گل دوم آرژانتین به انگلیس توسط لائوتارو مارتینز روی سانتر فوق‌العاده دیدنی لیونل مسی؛ این یازدهمین پاس‌گل لئو مسی در تاریخ جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/25807" target="_blank">📅 00:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25806">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d89d4e5750.mp4?token=J-ERkhbtIqqmyRBBv_9Gyb4s8cBi4z0ZmdepmAtiVars6vHyC6TQF9KCXgb4eMqtd4Fqal3ul2zjGUrPrSwWSNHMvVO5FJP6Lvv81eA4WGQQUmA4NfHCOpcbH90YfpgmRZg5XP-X7OaKv8kzkVSS8tBykzwCOoW6AbkDSE6Ic6ETVT9rQxSk8ZhdVU5i3-7X_l_edL-udxZugo72cdNLNAY_swj5a-soUI0BM-6srfNBtmbc-eQ9o_trj2I7GBD2apZPwyQpkyZk7W67okPDyShwU4H7ICFQy_23JC9s-dlF9eYZ5cxqV3xApFs1tsibomhlqkABSmFhd0ffN8KhNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d89d4e5750.mp4?token=J-ERkhbtIqqmyRBBv_9Gyb4s8cBi4z0ZmdepmAtiVars6vHyC6TQF9KCXgb4eMqtd4Fqal3ul2zjGUrPrSwWSNHMvVO5FJP6Lvv81eA4WGQQUmA4NfHCOpcbH90YfpgmRZg5XP-X7OaKv8kzkVSS8tBykzwCOoW6AbkDSE6Ic6ETVT9rQxSk8ZhdVU5i3-7X_l_edL-udxZugo72cdNLNAY_swj5a-soUI0BM-6srfNBtmbc-eQ9o_trj2I7GBD2apZPwyQpkyZk7W67okPDyShwU4H7ICFQy_23JC9s-dlF9eYZ5cxqV3xApFs1tsibomhlqkABSmFhd0ffN8KhNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
انزو فرناندز ستاره آینده رئال مادرید با این شلیک دیدنی مانع حذف آرژانتین از جام جهانی شد؛ دقایقی قبل هم گل دوم رو به انگلیسی‌ها زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/25806" target="_blank">📅 00:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25805">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c0c717972.mp4?token=gSNeevdWTc9FV_BCnEJIOW8hO_D9p6qRm7NtOfM17YIUjhVqF5YJAIjT5vqRJfFXhbkBCxswpYuEnYq3yGrfKWKQGTE3nJoP5PKk7lVM31rJKSABWC8LEkW8Gb4tt65dbBAYfFWmK2MnfSXfdCZRgCIp0I8DNqRp2e9eoZcblLau_duZuHrRVseXhH_U-BFbE5hHLX7vBgMWw7tAJGwjR18JVITOJ7yJf51P5VuTltan5kBUWsX-i7gr6j-_T8DW-ZSBobrv6vVlju2fk0-IbQhxPpek_4wqURdELFcAoPM0WgL7nuf_2Y8wYw2IFS4VZldfvISxUxJNaH77Du1hGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c0c717972.mp4?token=gSNeevdWTc9FV_BCnEJIOW8hO_D9p6qRm7NtOfM17YIUjhVqF5YJAIjT5vqRJfFXhbkBCxswpYuEnYq3yGrfKWKQGTE3nJoP5PKk7lVM31rJKSABWC8LEkW8Gb4tt65dbBAYfFWmK2MnfSXfdCZRgCIp0I8DNqRp2e9eoZcblLau_duZuHrRVseXhH_U-BFbE5hHLX7vBgMWw7tAJGwjR18JVITOJ7yJf51P5VuTltan5kBUWsX-i7gr6j-_T8DW-ZSBobrv6vVlju2fk0-IbQhxPpek_4wqURdELFcAoPM0WgL7nuf_2Y8wYw2IFS4VZldfvISxUxJNaH77Du1hGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
نیمه نهایی جام‌ جهانی؛ شماتیک ترکیب دو تیم ملی انگلیس
🆚
آرژانتین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/25805" target="_blank">📅 00:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25803">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4db22288ce.mp4?token=ulx6QtZ_WAhbiH5hcVh7et729hFDB6HTZaqm04fFOa_8hX7ZI2X8erZQKAU-Ordji5VwwReLKColz9yEL0Zj25-qVi6HZ4MqDCbVEey1uzANqyxMgwL9zId8NGZvvQpNWBitqJbftCMQXFSCtB_DSCJVto5ktu2vLgLoInzl5YV2XGoL2sbQD_60ln-wbwAAskn0Taz2H8z1Sa9Z6aqpgsnWSHomfpJVMCId6mm3BE9uyYIQLH7E-_7hVhh-ijlHSnC4D57oI96_5CrVa2sXlqHLh4siZgRdzPwslZUsmrTH1_Uu4eEFh-4YvM4UUStLkA3TiaeDPFVKCC6JmZHOJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4db22288ce.mp4?token=ulx6QtZ_WAhbiH5hcVh7et729hFDB6HTZaqm04fFOa_8hX7ZI2X8erZQKAU-Ordji5VwwReLKColz9yEL0Zj25-qVi6HZ4MqDCbVEey1uzANqyxMgwL9zId8NGZvvQpNWBitqJbftCMQXFSCtB_DSCJVto5ktu2vLgLoInzl5YV2XGoL2sbQD_60ln-wbwAAskn0Taz2H8z1Sa9Z6aqpgsnWSHomfpJVMCId6mm3BE9uyYIQLH7E-_7hVhh-ijlHSnC4D57oI96_5CrVa2sXlqHLh4siZgRdzPwslZUsmrTH1_Uu4eEFh-4YvM4UUStLkA3TiaeDPFVKCC6JmZHOJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بیرانوند: چرابعضی‌رسانه‌هااومدن‌گفتن مصاحبه‌ های مورینیو درباره من فیکه؟ اصلا فیک باشه وقتی می‌بینی همون‌مصاحبه فیک داره به من روحیه میده چرا توهم نمیای همون مصاحبه فیک رو پخش کنی؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/25803" target="_blank">📅 00:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25802">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJObJbZ0uRaIlxMBUqSvPNBRIBHtd7scPBGlgXozUMKkRx9uC5KcLen0-tA87EutwNsPiLnzH9tyTv2Zt48LPwkQDrwAhCQV8645bAxrdT47EmrNUy-KH4ZAckQvXEmD8pQVorMzQX-3peCFz2rDZzLQkDz0fINc356RpF3oyzEOd3Ctug_tBbT1kQUKcIwmWBElNWQ102oI_Jl1XbbJ6kGDlj2TiZiGI1C7xQOp5-QhSmLsfgqck0DTGiMd34F9xtdD4GUO7AYzbcsWIVVyJcT-ZemL7tgrJhEEiBkjWnZN3TugQszINrXr93Mg1N6aEkBbKpXSEWQZFHkglNE4GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف اخبار منتشره توسط برخی کانال‌ها؛ درترانسفر مارکت رامین رضاییان همچنان بازیکن تیم استقلال بشمار می‌آید اما همانطور که بالاتر گفتیم دو پیشنهاد داره که درصورت توافق با هرکدوم از باشگاه ها؛ با پرداخت تنها 200 هزار دلار به باشگاه استقلال قراردادش رو فسخ…</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/25802" target="_blank">📅 23:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25801">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K29RtS6lMGdOLHx6IxsLI5KDlo7ODvy7H8kXYUkyZZ2lDuvJ0_UN0F5yRI1HtlRzHwoQDFQEdcHX6z02VmVTBW-paC4a0jcUX5nsNvVpZWxxb0j99Dyu2vzeGaNFdPsoJ499VSjIvQtU8TmXtZ2_WW1g4y6sAOsIXys0pRS6xdLvmOBYs4-ZDkHe13SZ_NX0M7YgYZNhcGemKxhCUmAJi0tN0GRkxVlH5DJ9panQxGaAGGBwFI2uA3vOB7bJgHs7ZirZVXU_OyMiTO2AWiBuRahNUtvtQxVep-YfKz5-TgO5bQd9RrawDRvyES26xn9Ab2FGzCaSkSGeOOVJkswkAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با مهدی زاری مدافع‌میانی سابق گلگهر به توافق‌شخصی‌رسیده‌است و این بازیکن‌موافقت خود را برای‌پیوستن‌به پرسپولیس اعلام‌کرده و تنها توافق و پرداخت مبلغ‌رضایت‌نامه به باشگاه اخمت گروژنی باقی مونده که انتظار میرود ظرف…</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/persiana_Soccer/25801" target="_blank">📅 23:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25800">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tmr9gcC616DLjND9PWWv9e0lDzmAFWkcRu6QXp1tzueiYgNXjrBjaH75cNRB98DQMok_e0AM1E8_BaI8ySJ1Bz6KWesT6f1mDyf3YWGZ07_638h_9DFWcIbYicQPY3tqKrYEKumnqrCUvYstP7TrGif-dvl9LYxy-ZEehMa45jWYwhtP15jL4PvS5J5uHmqr_8yWrcMOPmDylzv99w0J_UIXybfU06jh9g4K6-9_SNtmO803Fo6RBr1_EQzKExZ66JKCGir0PMS0FjAZuKU8KE0bFqeBSiX7tSQcos7CuBjfRzt4XQ_TJkC2zpuvOba9HBuCHeVs8MabZPz_LDbDgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه اخمت گروژنی روسیه رقم‌رضایت‌نامه محمد مهدی زارع مدافع 22 ساله‌خود را 1.5 میلیون دلار تعیین کرده‌است. باشگاه پرسپولیس‌نیم‌نگاهی به جذب او دارد. مهدی‌تارتار شخصا با زارع صحبت‌کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/persiana_Soccer/25800" target="_blank">📅 23:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25799">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30d2d3139d.mp4?token=hyqFVH3rR_g3lOPV_OBImZVulmklRCe-0i0hKfZ9M2X4HyuMv0bF_yzkO6_reBZNZYShrhj8HZO4d1qO85WOeNg-qD-AdWN4I5UgeuFBNL9m2ci9EkIVHT8kv1Nh-F6gQ6ZaZsnaW891vCRHFPn1A9RLwrKaM1WyCEw5HE_rRKOmtQICbw5BGwokXJtGh5BH8wvtQDlwVFMYhUf3vQHDkFhWG4NrQ3mkhQNpcCmitISSircB006Y63RQt1deNywPXGNHoOmcqdgIJxzQpLAxTkfKc9_MukKtWOhyUdmhdYHC0WKJHlZHqyDMfx0hPm9WTzWqc6AcJdILj8MVFhiB8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30d2d3139d.mp4?token=hyqFVH3rR_g3lOPV_OBImZVulmklRCe-0i0hKfZ9M2X4HyuMv0bF_yzkO6_reBZNZYShrhj8HZO4d1qO85WOeNg-qD-AdWN4I5UgeuFBNL9m2ci9EkIVHT8kv1Nh-F6gQ6ZaZsnaW891vCRHFPn1A9RLwrKaM1WyCEw5HE_rRKOmtQICbw5BGwokXJtGh5BH8wvtQDlwVFMYhUf3vQHDkFhWG4NrQ3mkhQNpcCmitISSircB006Y63RQt1deNywPXGNHoOmcqdgIJxzQpLAxTkfKc9_MukKtWOhyUdmhdYHC0WKJHlZHqyDMfx0hPm9WTzWqc6AcJdILj8MVFhiB8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های سنگین کریم باقری: مسئولین سرشون شلوغه. علیرضا بیرانوند خودش یه مجسمه از قلعه نویی درست کنه بزاره خونشون لذت ببره. علی آقا دایی هم میگه نگو بیرانوند؛ بگو دکتر بیرانوند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/persiana_Soccer/25799" target="_blank">📅 22:56 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
