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
<img src="https://cdn5.telesco.pe/file/Uo1KV1i3JQ99jogJx65kuC8P7tIK5U3iCG10r0xX-QB0oaC7QHtPQ6zw6THi-ra7gZIlEKFDK7DsbD1YJGzlcd64BZPVzNqNuzZkO44OdYSyZyKn-cbC0bBjUb4tUIBRiob9r411c-AsYJ_bQpQ5dbEr0ygtLULoAYPAz7EHxCKqCqc-mkQmRLx-h0A9Aa4EoQoTYnZsKnXU71WiygkawXfwTpFF5tZJ6zc9GRk42XJWpuFSkrGrYBnVaLU6w566eGPKZpi3KcFsuWa0XkTJULeAZF55dUU5fcFakpdlU8cgdV-8GvzDy-kxo1JdMadfCduQJgXvGoLvd7CrFPctOA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 681K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 10:19:16</div>
<hr>

<div class="tg-post" id="msg-97075">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ead284c858.mp4?token=H8j4QGDmv-esSfKeHgXF-tpkGP1DRh29tKW83wN77pGsmWz_WjeW5_J3x8XrAfoAD155prZiHh-Vfvpa7itz1Yha1j-0REAIZeWAsh176BMRZQrUr0fYFyxQdNgUYxK4oq5YA27vLN9w1MKmTRcLrBIDpIgQhjQzBiC6ka7SUmhWmwFbQ3juqOjt57pbdPlXo-1fekJ8mVYOjo6k_DhkV2ecAiR_vQdbTcxJNQDl7BIiDleeLvQ-yPDRAE5YgqVoaLsZRovmp_nKi1FT88AMYB2_2pS4mK3rWDea4qTLZeX69rmgXPWaDyHU_rOlHdQfJnrZmxIenqiGQi7XKjb1mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ead284c858.mp4?token=H8j4QGDmv-esSfKeHgXF-tpkGP1DRh29tKW83wN77pGsmWz_WjeW5_J3x8XrAfoAD155prZiHh-Vfvpa7itz1Yha1j-0REAIZeWAsh176BMRZQrUr0fYFyxQdNgUYxK4oq5YA27vLN9w1MKmTRcLrBIDpIgQhjQzBiC6ka7SUmhWmwFbQ3juqOjt57pbdPlXo-1fekJ8mVYOjo6k_DhkV2ecAiR_vQdbTcxJNQDl7BIiDleeLvQ-yPDRAE5YgqVoaLsZRovmp_nKi1FT88AMYB2_2pS4mK3rWDea4qTLZeX69rmgXPWaDyHU_rOlHdQfJnrZmxIenqiGQi7XKjb1mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😁
وقتی میری میوه بخری فروشنده قلعه‌نویی هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/Futball180TV/97075" target="_blank">📅 10:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97074">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‼️
▶️
🇺🇾
روایتی از مارچلو بیلسا سرمربی عجیب و خاص تیم‌ملی فوتبال اروگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/Futball180TV/97074" target="_blank">📅 10:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97073">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77d79899dc.mp4?token=kwuVhgN_TodQR-6y84qX1cYxUaT72GffKdh77kM2GzBeXtH6VpFV9IJS9lxEZv4Stl1-Np0V_442ZrHliSRzWCslZSJHzk5FvOYMmTO-fsJpNCTYfsdzlVknDeHvdU7d52oh09geLunbuQmf7G0Epgk6Kp_HgtH4TeKcy-19zBDsxsvulXsJf9vNnBeodxMjeCzjGY41dhw_PnQ01bvyq7cshzVS7nZkbXz1lO-FD7sI-ynJKyqRMAj9doFg0-isROpG25fbdQRXWs5y4YnVypeZC0-8cQxZHirAOPDdmhpSti6oTgR68LEynFjKPdfhF3b8CZs2mlG7y8SfYaEmoDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77d79899dc.mp4?token=kwuVhgN_TodQR-6y84qX1cYxUaT72GffKdh77kM2GzBeXtH6VpFV9IJS9lxEZv4Stl1-Np0V_442ZrHliSRzWCslZSJHzk5FvOYMmTO-fsJpNCTYfsdzlVknDeHvdU7d52oh09geLunbuQmf7G0Epgk6Kp_HgtH4TeKcy-19zBDsxsvulXsJf9vNnBeodxMjeCzjGY41dhw_PnQ01bvyq7cshzVS7nZkbXz1lO-FD7sI-ynJKyqRMAj9doFg0-isROpG25fbdQRXWs5y4YnVypeZC0-8cQxZHirAOPDdmhpSti6oTgR68LEynFjKPdfhF3b8CZs2mlG7y8SfYaEmoDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
عصبانیت عجیب وحید قلیچ از خداداد عزیزی؛ حسابی کلش کیریه سر صبحی
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/Futball180TV/97073" target="_blank">📅 09:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97072">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80d90dfc72.mp4?token=A86j66xnbJSpNo-drofYXypo9b-EfyykSCTa2o6uKghn4Kk0qng7RuufAt53wKc7jv_QXVMBfNFfaWJmW-W89fa6sn6lv2N1lKG6espuaRZ7ilKWivj80JZ2XlyWdYf0mv_uBDhiyOVr_EnEk4_EOeWH_D5UodEczmEYpKK6lbwTzC12CAUvW_L8_VOiXe9K4i-59BVTYoaZoUfbYKS98mCtYM8KWED0KT0u7s5ySoDN4rfL9v37wGvRrRj24sWYjPL6x-MzOP6QJyTMuct1aEECTPRj-eF5YoKdIxqgOlAZ4czxaYepDV7fzWNAdkDf8Vs0HxmrlUMXkVtftZzbHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80d90dfc72.mp4?token=A86j66xnbJSpNo-drofYXypo9b-EfyykSCTa2o6uKghn4Kk0qng7RuufAt53wKc7jv_QXVMBfNFfaWJmW-W89fa6sn6lv2N1lKG6espuaRZ7ilKWivj80JZ2XlyWdYf0mv_uBDhiyOVr_EnEk4_EOeWH_D5UodEczmEYpKK6lbwTzC12CAUvW_L8_VOiXe9K4i-59BVTYoaZoUfbYKS98mCtYM8KWED0KT0u7s5ySoDN4rfL9v37wGvRrRj24sWYjPL6x-MzOP6QJyTMuct1aEECTPRj-eF5YoKdIxqgOlAZ4czxaYepDV7fzWNAdkDf8Vs0HxmrlUMXkVtftZzbHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
سید حمید حسینی سخنگوی اتحادیه صادرکنندگان نفت، گاز و پتروشیمی:
با توجه به شرایط فعلی، احتمال دارد مدارس و دانشگاه‌ها امسال نیز بخشی از هفته را به‌صورت مجازی برگزار شوند و فقط یک یا دو روز برای رفع اشکال و حضور دانش‌آموزان و دانشجویان به‌صورت حضوری باشد. هدف از این سیاست، کاهش ترافیک، مدیریت مصرف و کنترل شرایط موجود است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/Futball180TV/97072" target="_blank">📅 09:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97071">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b23fa1a74.mp4?token=aUgviIsBdWt2xXMaxgsUNWdfr0bx_Yi_FhT07TuaIvZFlDYYWB0VU3VAQTbqiyeATmIPnia4SyYFJ7DR6vrAI5xpQmrGeRaysWFQAOCl8YnZu8-lZUNitX0OPB0gsjjQRlIx59Sl5oC5hKY1UuLUy2Q8hc61q9rMaoFCsvhC7RBPV8IXBNpi0p1FpuWqnAgxEtQ0NtmPnkL71bq4VmEGgvRm8RwfoPDCgfpqp96x5ON42_URkeI9MxN74N4sFz2x0zveBRorNAi_AFep82UAQsxNHeyVLmHXYBQh95LVod8A7JdJ_1xILhaBJDHEXr1aQj8of3cqwVELaSktSUswFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b23fa1a74.mp4?token=aUgviIsBdWt2xXMaxgsUNWdfr0bx_Yi_FhT07TuaIvZFlDYYWB0VU3VAQTbqiyeATmIPnia4SyYFJ7DR6vrAI5xpQmrGeRaysWFQAOCl8YnZu8-lZUNitX0OPB0gsjjQRlIx59Sl5oC5hKY1UuLUy2Q8hc61q9rMaoFCsvhC7RBPV8IXBNpi0p1FpuWqnAgxEtQ0NtmPnkL71bq4VmEGgvRm8RwfoPDCgfpqp96x5ON42_URkeI9MxN74N4sFz2x0zveBRorNAi_AFep82UAQsxNHeyVLmHXYBQh95LVod8A7JdJ_1xILhaBJDHEXr1aQj8of3cqwVELaSktSUswFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🤣
وقتی زودتر از تلویزیون نوتفیکیشن گل دریافت میکنی ولی کونت میخاره نمیتونی سکوت کنی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/Futball180TV/97071" target="_blank">📅 09:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97070">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUtghhRg19OwztJmTulUyuNchQcuE0NHPE06uGHnQokpaV2nZpLucfrbumvuqHZ-qJqNr7e4rFAFa99nXQoNtakZAFQ8nr9Dn8efiLNewGZLyreCkGwUBBrA21fUwp4V1ZPXlf5ZKhZIR-h02IOzeNl7sM6Hso5P1G4fsGFfLF2cOzQyhuId6IR4lQQFbQ8DnfIRJ9WCprmIWnwuO8MFWAg1_d3-kKfYrqV8pmjFSpYy8f8Wvh0NnO9TehCjpwnqZ80mVnxDf6Z2CYpmpMU8zFLA0L4Z8hCXhlSKFtakqVoO0QnuX6PdojaBdU7d8AUlFhWFXWrOId2Q70eEiPh4ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بوسه‌نیمار و همسرش در بازی دیشب
😘
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/97070" target="_blank">📅 09:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97069">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de3e24176e.mp4?token=TLicEd7Y3rqZugVeeFbgr6iNt1rNX-PFF2bogMAMB-hz3DZD1rWEm11OIjHR3GaDvJVkPWaxjHyl_taNCDESrA9PUcgtelO4aXkTmFEZ5MEvSINjTuzQ5KpeGUHN6TLpAr2ATB3xXjPQK2Y_CjdnXdfYuF1GVe-wsMe1OPYPfBz2Vjc56w1hlR9Zfk3RtE8IPhbyI05jSSNC1hZuh2gBWXxnICe0V3M12hutXQiKocpOBhBw4UlO6xDjV828qzlnDHjUcisvLha_Fhc36upjl2uEDCQ62m5Ksb78SFMDydNXrJ7317_zVsD59NtuCpvXhr_htPW83pU5qwazuUBopQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de3e24176e.mp4?token=TLicEd7Y3rqZugVeeFbgr6iNt1rNX-PFF2bogMAMB-hz3DZD1rWEm11OIjHR3GaDvJVkPWaxjHyl_taNCDESrA9PUcgtelO4aXkTmFEZ5MEvSINjTuzQ5KpeGUHN6TLpAr2ATB3xXjPQK2Y_CjdnXdfYuF1GVe-wsMe1OPYPfBz2Vjc56w1hlR9Zfk3RtE8IPhbyI05jSSNC1hZuh2gBWXxnICe0V3M12hutXQiKocpOBhBw4UlO6xDjV828qzlnDHjUcisvLha_Fhc36upjl2uEDCQ62m5Ksb78SFMDydNXrJ7317_zVsD59NtuCpvXhr_htPW83pU5qwazuUBopQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇳🇴
ماموران امنیتی فرودگاه دالاس این‌شکلی به  استقبال تیم‌ملی نروژ رفتند
😂
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/97069" target="_blank">📅 09:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97068">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8YJ_OQcuFRki2xiPqzyAGC3WF8MOPhhR2rxTUcOhCiJt92nM0AZepqHJQSNiUPAj4gqX6w1iSHmGX3yzCCQBYg6jYECJIUCAs8Kt1gnDxtQOLzSYKqlW8LAmRy4MBE65h65qHOldDFMjIsOgNw1qhMTC_Pcig5Iz5vqGDY242nWpip9zbCWXBI5_uvdv7CmmqiDtpuoWBnSNNNP0OYYbFqmCgffMBx6wsSnc9skJ8GtG6WG4uSUoe25VVdMJzg-BJeUSj2pCK2A39TWRxXzKQdidzP5NZ6tkAMVK9KKCvHvP58njR-h3mbcfEVY3K3EX6Q9RP3cG2R_Ac4DKrYAtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🏆
یواخیم کلمنت، ریاضی‌دانی که سه قهرمان آخر جام جهانی رو درست پیش‌بینی کرده بود، معتقده که هلند قهرمان جام جهانی ۲۰۲۶ می‌شه
⁉️
⏮️
مدل پیش‌بینی اون همه‌چیز رو در نظر می‌گیره؛ از جمعیت و تولید ناخالص داخلی (GDP) گرفته تا رنکینگ فیفا و فرهنگ فوتبالی کشورها.…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/97068" target="_blank">📅 08:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97067">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AG28k-zRurAQdzbmE605Srknusg86CGCpqVggPV39BcpEAEeN4xuKl6XV3lJqqA4EvDPfjpBhFOm27dOC0wc3OSRzzBSXcRcuKMoxHajdUmRJPc3iNJHRwOYyG_SYkpIEPjskq87iNUK0ZSU7fK_qiw1vSmiEFz_CCXPvIJUeSgXy3rtEseXMgaTfNbIDIBR95hVQ9QXOF1hcb64WUI1-WVzMQuIHtpV_-1CEaoe-4hGWP0B_jxpgnJ74F4Cxu4KJuesapGzmL0raxUBxPhEVGyoPz1cRlO8N-xdxt5j_w5CHkHqsgJwT4qEaSZGNcUD3BUnY_o5_e0m_w-M3cwp2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇲🇦
اشرف حکیمی [
🇲🇦
] :" بسیاری فکر می‌کردند که این فقط خوش‌شانس در سال ۲۰۲۲ بود ولی ما نشان دادیم که قدرت جدید  فوتبال جهان هستیم"
🤯
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/97067" target="_blank">📅 08:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97066">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pb5H4lFg6JGr_xRgYSBDvIa0OFHO6Ba8RxgmtJAQgLa8qkx7sRys3TBZVpM-r9gCqeHTzRZrfCjUc9AVASuckBvx5cr2vt8N4rT-K_z27gFdLGcO7MQhULTqhaLCloSt2CwOJOTqT2I_R8ULxLHZYXKutGHjoiRGkz7nYK9CAKcKewE5ANi5m62vUSYeDmaxIZpEVfHnIRDBC8YNfqRL9MdWAO1F6ZxvkBLzlscrGzLg17qfddY5weDx3IzjfPOApRl1vUbHzPiUVaQ-5p5a-zRk17DCEEOufguwksVnXv-CJNwneEEa6YCzvN1mC4BT9b5FWyfXeaB2Ogoes0ZJXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇳🇱
🇲🇦
آمار بازی حذفی هلند و مراکش
🤯
🤯
از 878 تا پاس مراکش 800 تا صحیح بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/97066" target="_blank">📅 07:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97065">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCwSZKGcyMsr-klrfDvflVwZnQeCRZ4mjZaCIaMJIR72eBwjFGUu5wp1SHc3wrukckq2d3t-wdJpz1cKNWHkW92QBpq5bXoCAMcoSvzEPOnEYLp1QhsLPPUd69w-TW8bhyiMQua0pRPwfiS93TmxexUL7Lx6lPUFLytiUH4pTQGqX-4ZxUI8F91fsbzJ-3K6Jcgs5gXrayt_rQX_DBc66QwfOYIJkACn7RhGxwTW1GnAwB_IzsxZccEOGsMY057mkH4Hykx3WBXGi2nx_Oc3z1txWHULLHunExtkhGKDp-s4qlIOs4j1LnQyCX2XWCje2D1DuK4JDvD7cuSMF7GGbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
‼️
🇪🇸
🏆
بازیکنان حذف‌شده رئال‌مادرید از جام بعد نفرین‌کردن توسط ژوزه‌مورینیو
❌
🇹🇷
گولر
❌
🇺🇾
والورده
❌
🇩🇪
رودیگر
❌
🇳🇱
دومفريس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/97065" target="_blank">📅 07:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97064">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jAS1o4rj-h2SMNHn3fTXXJ6UD4049CAD9hHbuNOzGweVfNAdxFe28VhAG_tp_UJEn6S4emYmrRXOHdeuR8BKZgQaFlrZBb3nCBTaBWB_SSfpj0XCFSh-1htRXjIsbPuCqDxWvrqkKwpZNrRJGf5a3XM5EUZIvxore-waXO0Br8d_m5yyn9DyGuPxlYC8xC-ZlyvnkBoguYmpHPdrEWotRvN27SyRl6yP4CSltzD1htNTcEkA4O85lUFcXjRlCaffoCIGR1_jNxG4iuQYYrMBo7zffZ-FHFdjN7_cHlecQ5uylbIZSdPWWcFoVqBsBbaGEbBH0zgnqNQHmLRgUdqbtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
📊
تیم ملی هلند از جام جهانی ۲۰۰۶ تاکنون هیچ مسابقه‌ای را در زمان قانونی (۹۰ دقیقه) نبرده است!
• از آن زمان تاکنون ۲۳ بازی انجام داده و در زمان قانونی هیچ باختی نداشته است و یک رشته ۲۳ بازی بدون شکست را ثبت کرده است.
🇳🇱
🤯
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/97064" target="_blank">📅 07:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97063">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGzxqSm-3MHJORDFGSStvNW-SwWRxBt27WhPSw8q7wFEjU-0jGUHlp-qNzAUH6a3eDl5H98QTF8hZEMIJN7Rg5R79j3rwYTqWBb7MuSXq0HiE6bV1dob7EZNKIUd7OrbDrBXPsLFIG356FFB0xA_qrQPott3g-x3eJUwrGr4LbzoNapruWHGPicXyikPJXAkbzJ-80tF3tmMvmQZ3pjRJFMqXXBQUCBsOUcapvS78U8xMtKBb55ydIEs3iBDZv3VNC76qUv-99EXLJPszqSPlKEcb1hxgow91FYpXudz9oEqBEm0AxIomv3iw8_2Tp8QjTGT31q5AZz3jjM2dB2qqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
مرحله‌ ⅛نهایی جام‌جهانی فوتبال:
🇨🇦
کانادا
🆚
مراکش
🇲🇦
🗓
شنبه ۱۳ تیر ساعت 20:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/97063" target="_blank">📅 07:49 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97062">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ACEJyTq8D2fpI0dTV8BH2FNzZhjDZplNCugr1ZvawoCgiVIwLG2JPZlQnIw5cbR6o5wdidpKKl9_A6DMFt5FRzjeom6hTWB8JFHgivE0ZWWjN7lkBveCkqoKJvKv7OVt-059uldOoRf8dKvPzwu6XsIVgYMOxpW87SxXPFA_r8B5M1fsjPM9P36xLWyKrYrNi0NiEvzSTI4T3pKnykeHQHqGwR3lWa2hMtl2kaqhBlvvZJRDu6UTkW1Xhb-WEfg5akuV9hvTlsWefjim0834QyX3V-OinOHd-R6nf3MhtrpuWcKNfx8sTtgQNJi0NOZRGxdykBH8qvhMrzkND4cxjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
👀
یاسین بونو، دروازه‌بان تاریخی مراکش، اولین دروازه‌بان عرب است که در تاریخ جام جهانی به سه ضربه پنالتی پاسخ داده است
🧤
🇪🇸
در سال ۲۰۲۲ دو ضربه پنالتی مقابل اسپانیا را مهار کرد
✅
.
🧤
🇳🇱
در سال ۲۰۲۶ یک ضربه پنالتی مقابل هلند را مهار کرد
✅
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/97062" target="_blank">📅 07:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97061">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v34jul3QvmwLU86sCNlxJiNSQ21Zg8VC5QjYNASOs2-oKCEoanDbd5Hie0ROVnCJcF_lFktIN1StouHifFoqKsU-Vjcixzs2IFJJp8Af9WB9uip2k-DciNNB_jBIrBEOy_tVDABWXpZQvARf4HlLZ58dwhR4iY7a_tlCbLBbLIpOkEkTZB7zJnjnNmPWdSxjU8l20mjcSZlVmib_8KFarw4jLTSQvKAPAs_wN92jnGMwA8LIkWtrPEDgEUN0b3eHQnhrAgt1zvu5DgLBj2DT4CRrzH94VkfXdMbFU4vhDKEWzv1LBEsKFNIViQEhmKfaAfQQ7ulJbTxk6SYA8TX8qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🇲🇦
تیم ملی مراکش به شکست‌ناپذیری‌های متوالی خود تا ۳۳ بازی ادامه می‌دهد
✅
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/97061" target="_blank">📅 07:46 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97060">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBc-pITwC9kn_i4Q4udHzaSFrlVr6EG_AojUkL9sFTgrD4CEIm74UZv2A4cBJTaiTK_9_83DgFtB3-_7L_le1gPBq5lNNJoJhdSYcyAaGiAU668p3FWT_ddUf6A4GLiKJVpYfI5KiijYXD6R50LejeemJBg9eqsk0Kp6B6eAvgQC0BQec0KjTmIkf1ClcBOSzrvCD0Uz4HStA9sQTqiPfhdNByAYGHZCbDbtkIe8WBQ_mNfD5FvOP2aecXzrzLNTAvJ3EQHaSre2zJ9KSHurFJODE781_patrFUgunNI5d30jMy4DJq4JekAuNS4x9pY5ERZ-tj4bOy-ZCL12CrFKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مراکشی که تو جام جهانی 2018 از ایران شکست خورده بود تو جام‌جهانی 2022 و 2026 تونسته اسپانیا، هلند و پرتغال رو حذف کنه
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/97060" target="_blank">📅 07:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97059">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eP_HWo3bOfglOfOpoDnZfbNN_Id7lXsOmmRfuA278dKFWKrdy15dbuZ-94Ba02FoGMEq5Cx8DdqzsUfgkIIl8g4sprYRzH_csloSM91vL0eRQkRAqBMzB8OohZD2BF0FMZtJgYGjAzHaDadqqgcIR5oYD6xE8zwynoKcJHMiKdRYWVnTcs0dnV72z6PEoT7rUo82onvGxhY3aUs2c-rDBxyRygwoMMjE5mOnd-5w3UuNeJqU6uJpJPcyeaXNxUsU_N6zJUTNc8zQ7acFyqoBQ8p2IO0iHOKqf8Wx86TWMUme5nPHtK5uO_1P6tx4ET6Q4KgHVx760QPEs7lrpmLYTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
آپدیت نمودار حذفی جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/97059" target="_blank">📅 07:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97058">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYRwG88cMMMvZG2czx89k_gDwKueOvzq4I0kpLPbEpArp8KYzUZm1blAdPJptgLxCLO7z0kRKtLhhsrgHmLOqd2iJwxdjRyedhtsknFJ2ZxNfU8_MSDJONA-9kGqPuV1sB9H2Jx_R4JQVICTVgxclhofd2tmKjs7lW5PeiYJ-HPjb6vHAXs8-TaeVj2aNuWeKofD0spYc5CPbO1Tiu3vB2VR3l2BWaD0My-xbTtJD--ZiG46U439LjOF9tF3CdAjn3lzZmAY6ZfUhXz2Bc6Gp74sFtHdK_4TaqSN3VL9x_Kww-DcakX1L9m4C8-IMF36h4PjhSkMBCOVENnkhBUvTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
#رسمیییییی
؛ مراکش با حذف هلند راهی مرحله یک‌هشتم نهایی جام‌جهانی شد
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/97058" target="_blank">📅 07:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97057">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گللللللللللل و تمام</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/97057" target="_blank">📅 07:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97056">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">مراکش بزنه تمومه</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/97056" target="_blank">📅 07:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97055">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">بونو اینم گرفتتتتتتت</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/97055" target="_blank">📅 07:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97054">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">پنالتی پنجم هلند</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/97054" target="_blank">📅 07:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97053">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">چه خبره امروز</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/97053" target="_blank">📅 07:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97052">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اشرف حکیمیم خراب کرد
😐</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/97052" target="_blank">📅 07:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97051">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">آقای کومان ریدی با تعویضات</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/97051" target="_blank">📅 07:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97050">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">تیمبر پنالتی هلندو ریددددد</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/97050" target="_blank">📅 07:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97049">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">همه چیز مساویه</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/97049" target="_blank">📅 07:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97048">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">مراکش هم گل کرد</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/97048" target="_blank">📅 07:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97047">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">شمس الدین پنالتی بعدیو میزنه</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/97047" target="_blank">📅 07:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97046">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">هلند گللللللل</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/97046" target="_blank">📅 07:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97045">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">عجب گل کصشری
😂
😂
😂</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/97045" target="_blank">📅 07:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97044">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">مراکش دومیو رفت که بزنه</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/97044" target="_blank">📅 07:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97043">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">کلایورتم تیرک زد</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/97043" target="_blank">📅 07:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97042">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">پشمامممم هلندم رید بعدیو</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/97042" target="_blank">📅 07:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97041">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">کجا زد
😂</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/97041" target="_blank">📅 07:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97040">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">خرابببببببب کرد</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/97040" target="_blank">📅 07:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97039">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">العیناوی برای مراکش پشت توپ</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/97039" target="_blank">📅 07:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97038">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
زنده از ضربات پنالتی(آپدیت خواهد شد)
◀️
🇳🇱
هلند
✔️
❌
✔️
❌
❌
◀️
🇲🇦
مراکش
❌
✔️
✔️
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/97038" target="_blank">📅 07:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97037">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">گللللللللل</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/97037" target="_blank">📅 07:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97036">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">پنالتی اولو هلند میزنه</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/97036" target="_blank">📅 07:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97035">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">بریم برا پنالتیا</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/97035" target="_blank">📅 07:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97034">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🏆
پایان‌بازی در وقت‌های اضافی؛ ضربات پنالتی تعیین کننده تیم صعود کننده خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/97034" target="_blank">📅 07:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97033">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دقیقه 119</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/97033" target="_blank">📅 07:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97032">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اوه اوه این چی بود گلر هلند در آورد
😐
🔥</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/97032" target="_blank">📅 06:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97030">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56fcfd81e7.mp4?token=lTFAWpIQgU9Vd0foW-0Hdb4xcKUkwkac3W4t01rvGk0ZxLaRVrt9-2JPi-4ueMg2YwO6TsiMN2h9zbKJbjRByZZrke_ADp1C7MtRYOMqQsZoqB2ZCSpCr1qddTBGlZBF2Q8dSjvXcWkpcWyS6ItzLgU4BgUFQSyaZoy6lqoFefRLcHryLhTHdNMzog5V7nY8TQBYJ_VdJ6SW2xeF5g7wP0nuHepXU5QW-bQ4C2AFcYKC36-uUbUCizT2s56F9fVWWb7YTuTA5NGLvw4_y6T7ff_sEV9JxTV9HLoUP13hzTRY4EswWzz4EMD5W9St16ASIAYbFDqKWjrAeJ8YjbOEQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56fcfd81e7.mp4?token=lTFAWpIQgU9Vd0foW-0Hdb4xcKUkwkac3W4t01rvGk0ZxLaRVrt9-2JPi-4ueMg2YwO6TsiMN2h9zbKJbjRByZZrke_ADp1C7MtRYOMqQsZoqB2ZCSpCr1qddTBGlZBF2Q8dSjvXcWkpcWyS6ItzLgU4BgUFQSyaZoy6lqoFefRLcHryLhTHdNMzog5V7nY8TQBYJ_VdJ6SW2xeF5g7wP0nuHepXU5QW-bQ4C2AFcYKC36-uUbUCizT2s56F9fVWWb7YTuTA5NGLvw4_y6T7ff_sEV9JxTV9HLoUP13hzTRY4EswWzz4EMD5W9St16ASIAYbFDqKWjrAeJ8YjbOEQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گللللللللل مساوی مراکش به هلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/97030" target="_blank">📅 06:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97029">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🏆
پایان بازی در وقت قانونی
🇲🇦
مراکش
😃
-
😃
هلند
🇳🇱
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/97029" target="_blank">📅 06:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97028">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcE4WwYJu9HlQ6L5iNHXDM3eIFOQ9b8v6ddQrTStk7h0jBpzFPpbVpCthW7OGR2-h2FOrbfy2-BD9zJyRxic4dR_kawbCW1t-XFJ5Bbe1mqxukz_aghLi-mvZRMoEwKEg8FexMiFdNAqghq4_2k8jVA7gSdJvqAZEc07M7TfTKhhj8vzdLt1PZz4HuSgCmqFn_kJ1pXmojM1zbzFNRVGa03qnN-9FQC51xyWoKjBLrkDT9v8Y8nzH_vPnEuBmgN0wCJdkEKaIgaGQNvigfyzMBL1ZkIsJdMXm5ttiJv_t1DbyMKIW98dmqcC1yNHAbqm5MgRxXtrJuRGmdPAxb5zpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فن‌دایک رو خدا وکیلی
🌟
🌟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/97028" target="_blank">📅 06:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97027">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پشمام چه بازی ای
چه دقیقه ای گل زد مراکش</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/97027" target="_blank">📅 06:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97026">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">دقیقه 90</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/97026" target="_blank">📅 06:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97025">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">گللللللللللللللللل مساویییییی</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/97025" target="_blank">📅 06:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97023">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gQRv1Xsmu6jh12tIyzD0gaVfhww3dui8MKmXYlCK4zdEZKGBx8ad_UZU-kLnI2QGfaSSueOa0fIF2pIgy2NALMBEo7QjcuB5l4BG-onWNW7q6zluGt1SU04W2ku0_a5mXpDYdU9i5jO8Myp_exWWQWEgpd-h4W33l9nTgjEhLGOykOHPHfQxYHqNIFkzPGRB1TmktAuQuv560bS2Si1KJ5Dbs6UeuCPhR9KSgsX0O6QvDQv-yxsjCGaeadq7jYEhHCCV3Hv8Oj4EehrLiSae58GgmiovbPHM2YbrPhNGEQF1-WwedYw1dV185CHDo9bSaXCDPH64M7VDqX2KJS2hfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P07Kj8lVqYTB0Q7ROrzOSU26gQcCU9cCf4pKlXg6GX0HpChqe9_RPUW7dbmhWF9HaGJqDhAPddZAEVNnRvEdH5Oua7iIGPvJBSewZIy3x2RKvbRO9O6AlJTANTyuFIebywbyZEDgZ-o627NXcyuGeKDEA8-JNzirNWJEGyi5vRIra0Cj5d-QkLLIcUdM2JIHhzawAEZv3JPl-NRXjfhQufvkfoE7l0_9QpiGTU54vSqd5tfRmSLp6nRjDYxNCNmzKItZ1koTUSjimukkKJMsySvyjKzeuRnoluJeQo3Qorb3L-jPLyBR9m2M8MX18mzc8YMvIqaHLbd395TnFZ9k0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کودی گاکپو بعد از گلزنی به مراکش به دلیل از دست دادن فرزندش نتونست جلوی اشکاشو بگیره..
♟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/97023" target="_blank">📅 06:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97022">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eec21bdcc.mp4?token=hYvn6_ma23zYUd2J4nzcM3O7GgwXU6Do0DfZX-Z82r1ECppjU8l_gmjZj9ua3zC67Ov0d6UbUkJHBUVUmlMrCVRvqcgQ-gShLimiAAuEdexpPeL0y40kD-BhCUlVSEksuZafsEzATYIKQU6BtVHyrrt2lvEj233e6zRN7zLcqXs9Ou5CDGhixsxLpszJGjzjAeFD8UlUx41xZHQMQRZQoZg0maEDHtDeicTfwwHW9y-EHtb42OSSHVMXHeX_6yCWiaLgZ4rTpSQtmqfg8zGw3vlwxlzIBeFWi1ZG-rRh6PUA5-R_h7F0zftWhL0cOix9OMaCpnF9Rff4wyIf_9znJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eec21bdcc.mp4?token=hYvn6_ma23zYUd2J4nzcM3O7GgwXU6Do0DfZX-Z82r1ECppjU8l_gmjZj9ua3zC67Ov0d6UbUkJHBUVUmlMrCVRvqcgQ-gShLimiAAuEdexpPeL0y40kD-BhCUlVSEksuZafsEzATYIKQU6BtVHyrrt2lvEj233e6zRN7zLcqXs9Ou5CDGhixsxLpszJGjzjAeFD8UlUx41xZHQMQRZQoZg0maEDHtDeicTfwwHW9y-EHtb42OSSHVMXHeX_6yCWiaLgZ4rTpSQtmqfg8zGw3vlwxlzIBeFWi1ZG-rRh6PUA5-R_h7F0zftWhL0cOix9OMaCpnF9Rff4wyIf_9znJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل هلند به مراکش توسط خاکپو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/97022" target="_blank">📅 06:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97020">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">خاکپو
🔥
بر خلاف جریان بازی</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/97020" target="_blank">📅 06:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97019">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">هلند زدددد</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/97019" target="_blank">📅 06:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97018">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گللللللللللللللل</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/97018" target="_blank">📅 06:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97017">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee6fb4d140.mp4?token=Zl30khqLddozIIu0Fw1nOnJ7WfZzQrNdgpmWpC-pe98BL8QdidA5x4ugmlmSnAk4-1sutd0zXSAxsMKP0d_Q62Qjb16MQi0u-y6YxnUrgVercSndoVXd9Me1KYQIw00YixWv7GckOQr4mEWZox3KVEqGQynsSShnaylDjFIIPc7vc5P0kSgG1q85WOz07IoT2LNDdrArQJ42QE-BXP6WzRtU4THLVnCp706drIJubg1I5BkOrf4w6GtFCMc8Z9xN-RShES1dCmCYYQmpWwoEbfc15joCCq1YpYzKmXHrEvU77ygl_Q9GBZ_EALQneJHosTXjEV8qdDEbFrmPkWnwgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee6fb4d140.mp4?token=Zl30khqLddozIIu0Fw1nOnJ7WfZzQrNdgpmWpC-pe98BL8QdidA5x4ugmlmSnAk4-1sutd0zXSAxsMKP0d_Q62Qjb16MQi0u-y6YxnUrgVercSndoVXd9Me1KYQIw00YixWv7GckOQr4mEWZox3KVEqGQynsSShnaylDjFIIPc7vc5P0kSgG1q85WOz07IoT2LNDdrArQJ42QE-BXP6WzRtU4THLVnCp706drIJubg1I5BkOrf4w6GtFCMc8Z9xN-RShES1dCmCYYQmpWwoEbfc15joCCq1YpYzKmXHrEvU77ygl_Q9GBZ_EALQneJHosTXjEV8qdDEbFrmPkWnwgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🔺
ولی پسر عجب اندریتدیه این فن د فن دفاع هلند؛ رسما تو این بازی کون لاله‌های نارنجی رو خریده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/97017" target="_blank">📅 06:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97016">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gg-cN3HINdmugJGxo0n2c4ccKZulcxyKD8gaAEoLpRBO0ct-QafxXR92JTLOpeJ7qVCVPWSQOK2TS-btuDjOnuONfJGkgacDLKzu7QVVLW7ecz-YK5Uj6u16w--ly_xuhLUcQyBXT6AnEr9hcELt5DAHGrJIgfjDhTrCzxFgWc_pV_3D-jrHZG9ecyI5iezFN4WY4uMWS5lLXN5LS_358me18JIs_UaPduilusRruv6LCUjKUD3-VKt1djJGLY34JL4iwBolfaxvQwK0F4xbePXN94GdbSYAZ0z6TyD7XWmSdfglmpIfx7FvAKTH0ElV2hio-vUuKh2ZcKA8IM19tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
‼️
آمار دیدار‌های تیم‌های آمریکای جنوبی در برابر اروپا:
🇵🇾
پاراگوئه ۱-۰ ترکیه
🇹🇷
🇦🇷
آرژانتین ۲-۰ اتریش
🇦🇹
🇧🇷
برزیل ۳-۰ اسکاتلند
🏴󠁧󠁢󠁳󠁣󠁴󠁿
🇪🇨
اکوادور ۲-۱ آلمان
🇩🇪
🇺🇾
اروگوئه ۰-۱ اسپانیا
🇪🇸
🇨🇴
کلمبیا ۰-۰ پرتغال
🇵🇹
🇵🇾
پاراگوئه ۱(۴)-(۳)۱ آلمان
🇩🇪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/97016" target="_blank">📅 05:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97015">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">بریم برا نیمه دوم بازی</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/97015" target="_blank">📅 05:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97014">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پایان نیمه اول بازی</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/97014" target="_blank">📅 05:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97013">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🎙
یورگن کلوپ: «اگر این صحنه خطا باشه پس آرسنال هم نباید قهرمان لیگ برتر می‌شد. اونا ۶۰ درصد از گل‌هاشون رو همینجوری زدن
⁉️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/97013" target="_blank">📅 05:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97012">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hBGRnpoDbtOaYQHck--fJealgQH5TqPYhPhx8d9AsOkkHP7SXf6uqv-FyInSeG6EKXckpx6nFcdnzm6u6IEaxi-EjsMM6rYloJh5L31jJ_Dt93yHWmVqj339zn3Vtuym04RM3dcmfizX_kpV-ztrtF3VaKUuNf4IhVGc9Mwb_OSYUtLGuuyX8-HaCbxkR9TSZgw3v5-GHZXu8ADSQUEgXSPUNokB-y43GuzHW86lRMl_QFdzf86oQSFs2CJANXdZpKOdTDg5s5Xp_Dzg_TFC6dzGfpZtYlxF5AwyeOOxGrTOi7mIGXh1Wd4vxQPw_ygCdzkqW-xPpDFpXl0U4C9WxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوه اوه چه خونریزی ای کرد سر فن هکه</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/97012" target="_blank">📅 05:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97011">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اوه اوه چه خونریزی ای کرد سر فن هکه</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/97011" target="_blank">📅 05:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97010">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqs4_WhAV04fJvZS8hvSNcMash2d4jV64hbs14W1Hoystel5Cdvq3SB7A-sLKPkQhVLvPTby72NCS6ewVEfsvlDRSyjQ7VfVQ9V5QgCv8NC1fblJCstUQaSXyebRzntqpIzU-9izAdTQCPaV-0kdvhUsKwCHo9veax4xs6IW093CoL1zKkZpxmSI5N2wyJjmvfT9qdGE3NnRA0oVUK46wK07IfrWgzjiVLmlyoqSreF-42YZntVuCAI1couS4hXLq2vyxolmkiFJaZ9Jb-W2mvButa8ytmm6mkwpkWwbyHBgrucyFdwURl6Ob8g9DD8X5S_XaWsII-TrSKFiHmoGCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه خوشگل مونتری مکزیک در جریان بازی هلند و مراکش
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/97010" target="_blank">📅 04:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97009">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">تموم شو دیگه مشتی
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/97009" target="_blank">📅 04:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97008">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">کم کم بریم برا شروع بازی فوق‌العاده حساس مراکش - هلند
🔥
🔥</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/97008" target="_blank">📅 04:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97007">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iibSVAnOtxaPoR_V7DVNhiB_AXrGhdwVZL9-TK6lGX_2KcVed5kz0B6fyo696urqO05hTnVgnda95SNxxHiZhNtB6FxMkodxIO4QR7WSYXqBLLvnD1AVV8Md_SeLkrpif3qDhfOdgKJ0yHwqBJmFb4JuTevQdTAyGcXaWNeeAi69W25laRiqxkWhad9jkfP2BVqCfnQUCKzpeckebpEp7FVufaR3qLQ2DjQ6FxvgYAzfi2r2jsRsNSHhTF4Ab22izLXAbgpMnOAhbNqJL8tZ9Bn87Ir_tYJrO1JVGJQmXR2K57-Rj55BxtAL6jygcX1TVn5y6UGKLp_AyiE5Ln382w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
مارك كوكوريا: ترجیح میدم کچل باشم تا اینکه لوگوی بارسلونا رو روی بدنم تتو کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/97007" target="_blank">📅 04:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97006">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7675e39d8c.mp4?token=qH_XZXgU_fEDxhs6_GNJ9_okI3Iez1iWnS4E8Ji4BLwJjCdB9rzJldESTj1C0jK0lzw6r8ipTOv7iD2N1Qc1vR3RUbyC17ZGXHZlZFobtJ0HU082zuhKvhUu3pYa3glhP1aYzs9Jisa5XEi0CSNtbcX05NW31qY4YouOrKK8vLKIs01Lqe5ZcgtP1Rel_N-VtfsEPeHmbVr4dXXOvcHuWSCRqE5cwPgNcYg2DUpLEfGqqhPI-3UQutXfLc1EkZ3-3napkRpvKk2Hsaig8oUg1ne3jsyb-U3c3AwAAxwbIBOXEdJx2RMshHpJvmV_wj6Lu3VtwR3y-fsCd71GFCqXRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7675e39d8c.mp4?token=qH_XZXgU_fEDxhs6_GNJ9_okI3Iez1iWnS4E8Ji4BLwJjCdB9rzJldESTj1C0jK0lzw6r8ipTOv7iD2N1Qc1vR3RUbyC17ZGXHZlZFobtJ0HU082zuhKvhUu3pYa3glhP1aYzs9Jisa5XEi0CSNtbcX05NW31qY4YouOrKK8vLKIs01Lqe5ZcgtP1Rel_N-VtfsEPeHmbVr4dXXOvcHuWSCRqE5cwPgNcYg2DUpLEfGqqhPI-3UQutXfLc1EkZ3-3napkRpvKk2Hsaig8oUg1ne3jsyb-U3c3AwAAxwbIBOXEdJx2RMshHpJvmV_wj6Lu3VtwR3y-fsCd71GFCqXRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک ماه پیش: هاورتز قهرمانی چمپیونز لیگ رو در ضربات پنالتی از دست داد
❌
امشب: هاورتز با پنالتی که از دست داد باعث حذف آلمان از جام جهانی شد
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/97006" target="_blank">📅 04:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97005">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yma5K9xeLmYDkXVlIsXwzxH3zoAmJ3C00EpF2a1EmnQR_UkgXQo0HXSttA1Tk3ND4-qCC1HLKJ0BNgyHe3vEE_Vyrgjc3cfIj-v44isvI-WJK0_6WJC6TPYZrfguVRozFGIdF4iSnT4HTHOg3nJRuajYCKsDUnvZVDkSYE2KQmmYQJ5_DExosu0oTKW6zRorEkl6cIQTS8gpZkBzuEP_eqZmotlsGRS_AycrqHsUM67tuUJZZYlsdSpKMgJG7WH-8DOhcMZPHQFVkD5Zc7AWn57ctZu0NuxFgkP1LrRMuGz1ad3EjRUqUbxxFcjknEzKMLbU8N4PzYTp6qsn9v5Kug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مود ناگلزمن تو بازی امشب:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/97005" target="_blank">📅 04:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97004">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HF010kAOPKfM6GFNQJ1gy_Oe65qFfsDHWUNE4b5A806cQdSQRnXTw6PdtTVzzgG-kEGvg8zXnMbVPbtQYqF3wMhjO8MTCYVnuXSQdKPAYCTan6YhCu1VH-pevZTF0ppf48cxPReJLNohT3LePhgNpmwOW_Pi7Ak-blaghFVccQ4-s9xnhqTVaIN1H2sKwP3xON_3zURd3clE6u4YQhLA-3dsf4z4tuZKGyICHzCeElJFzA3LRpbBVVEAcKCZ6iaJ4eLabxp2E8uG5vzIkRGC0bByldIu1m7hYEhCskABar25frAQDb7Q_KBzfQ8ea6NH8ZvNxqBFm3b-nEGpbs-L8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشاپیش طرفداری خودم رو از لاله‌های نارنجی اعلام میکنم
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/97004" target="_blank">📅 04:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97003">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔥
🇳🇱
ارتش‌هواداران هلندی پیش از آغاز بازی حساس و دیدنی امشب مقابل مراکش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/97003" target="_blank">📅 03:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97002">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5899cc42f3.mp4?token=SJGrw9ECM5tmjQrksmU2WKIlsTz0QP-6FPtZuLQJvtHbQnNWM2TqJLdZ2D_NUOFiMEagFXcGZACHgvf6fDxf5IOXLBZsUor6uVmOUTZLVoVBOI9BgMnXkeBcdiGuOPK0nf995CgP4oe_fowI3R8EE4M-xqM6IOVJsCLn8Z6obKK8KNRataR789iGw6pQB9va7AAC3OD2CDt5G1hHnBZnhfk0WppVbXWcW1GyssGPkEV_MwOZ-XmK0zMdABmb_5rYEvnOcd6XpBJbSG8vmiAfBf93_qr4MiizyC_M9ykBlmbypaLY5UjplTuyVqGUoPx_pasf0kXCHey99eM-uIEMYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5899cc42f3.mp4?token=SJGrw9ECM5tmjQrksmU2WKIlsTz0QP-6FPtZuLQJvtHbQnNWM2TqJLdZ2D_NUOFiMEagFXcGZACHgvf6fDxf5IOXLBZsUor6uVmOUTZLVoVBOI9BgMnXkeBcdiGuOPK0nf995CgP4oe_fowI3R8EE4M-xqM6IOVJsCLn8Z6obKK8KNRataR789iGw6pQB9va7AAC3OD2CDt5G1hHnBZnhfk0WppVbXWcW1GyssGPkEV_MwOZ-XmK0zMdABmb_5rYEvnOcd6XpBJbSG8vmiAfBf93_qr4MiizyC_M9ykBlmbypaLY5UjplTuyVqGUoPx_pasf0kXCHey99eM-uIEMYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇻🇪
👍
در‌پی زلزله وحشتناک ونزوئلا، نیمار مبلغ ۲۵۰ هزار دلار و خانواده لیونل‌مسی مبلغ ۵.۵ میلیون دلار کمک بشر دوستانه به این کشور اهدا کردند
منبع: ال‌ناسیونال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/97002" target="_blank">📅 03:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97001">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHZiv-DPXRerQOG-5ZY_R9RcaIlD0g1PPbL6GTMXanHJ0tsFZytA-f7C9ZN1swPa_iQsaoVj122aoyKOGNOhXd_ztR3YFzcYS7z7YawmWR6ddejcKUZypOyA3wDyA3zvA4Vr5LtWSrwn3txxTbgl-Ag9z8hRSxbq_LO_Ustrt-Fd47fCOX8jfuvl668EIWPOTeDSh6aBGOBfDXKzJpZIoPiD-T4cz7ZUv2QjiIgiP69TVsJ3whghCOgPK7c03vjuQhJCh7p7D3qtnt3fX8EcOcPHA2nl7MpBKTZzM51yhMB3tnARGMJoCeZ_XYRoy7I9GSvl98-pOQbD71cD_-zRQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
#فوووووری
و
#رسمیییییی
؛ مانوئل نویر رسما بازنشستگی خود از بازی‌های ملی‌رو اعلام کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/97001" target="_blank">📅 03:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97000">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">یکی بود میگفت یورو از جام جهانی بهتره
🤣
میدونید کیو میگم دیگه؟
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/97000" target="_blank">📅 03:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96999">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IrCD3-1L9l6iT65VPhbWy2As67C_EDYm38lYPlJoL1KfOBR0iqsHZVRWqU-HyL3RE-Ribs7ZjoKczJ4NLw2dOAFmp1h_ECXi4uWZ2GJSENKGP3wx5SzBBK6x9pEIlSjFijh8Py50Trgao_sPRSOXrTK2Irh5kcdlStADgG6NXGfqmZnyXrESmOgL8YUG-1rUthk8oastV4tdLTjXrqHpzXotX46M2rIGO2_36jRh1tbU3K6zOzy5Puf_QzUjSMeL68vufw4PXcx742-HRwbx0zeKZr5PHiy2k2ke4kpwG3h4H0ag4kkgBsfYH-PsI1RgZrz_0pzntH8b1yzcqaxg3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
برنامه مسابقات مرحله‌یک‌شانزدهم
🇨🇦
کانادا
😃
-
😏
آفریقای جنوبی
🇿🇦
🇧🇷
برزیل
😀
-
😃
ژاپن
🇯🇵
🇩🇪
آلمان
😃
(
😆
)-
😃
(
😀
) پاراگوئه
🇵🇾
🇲🇦
مراکش
😃
(
😆
) -
😃
(
😀
)هلند
🇳🇱
🇳🇴
نروژ
🆚
ساحل‌عاج
🇨🇮
سه‌شنبه ۹ تیر ساعت 20:30
🇫🇷
فرانسه
🆚
سوئد
🇸🇪
چهارشنبه ۱۰ تیر ساعت 00:30
🇲🇽
مکزیک
🆚
اکوادور
🇪🇨
چهارشنبه…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/96999" target="_blank">📅 03:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96998">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/soK370l414y-NB7PT04edxb_-8qUZECunr9fFQy6wSIFgvM639t-ZcTU2vwdvj_D5ikEhgHBAhUAmi01WQEqwdx7vHOLjEBTCPki1x94FCitlLN_OGWP1ZWf3PwTETzte9XTd0u9d3aAsGmzhGJ-pODrnFyp6HUpJUyjsXyag8QMV1gT1vzUO9gctZgtmMd72X0NFyk7eDDABl2ARpaA5xrD0ZoKKBax8oUav6uX5DCmYNQ5KVDv6SEa0j_o64O1nDbNsjkFF8ua5BRNBpoiquIsHgN72Ibwfm9nGMSs3Qd6kBO6J9RH5mRerO7yYDylC2045jgtnROTDDuFL7PptA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤡
🤡
فقط ادایی. ادا ادا ادا.
به یه نگاه به کوچ کردن کارلتو تو بازی امشب تیمش بنداز شاید بفهمی فوتبال اونقدرا هم که توی کودن فکر می‌کنی پیچیده‌ اس پیچیده نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/96998" target="_blank">📅 03:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96997">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FgQB8GLBBBKnMhX0HS1O267RAHWK-8rtmDo_r529iXZFAG6mPjfrQ7M4YQNFO3Lrxb2vWT0PWQs0JX9YpBrxvc-NWjhlZNYjtCsZ1V9VUAXa0PN52VCo7SsRYIHSiBpgqqAs40Eaf_u3fKpgKGKuCXYzkagBuMVN9d9AViLmcjH6KIEVJ16qfiS9ZgAaqwodZQh1TobiM8xR9emVtZPeJLW-uVI6q-un2KdGrjd4Oku-a496Pg6oRkNXZfMcbFuYS8zaMEXktF7ow1xuhyeMOvYS0L4zG5wW8V4knsWCOdLLH6MypGvggsNTe2D4jQsTNLglsWRTkxcpwjx5QeCZDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاراگوئه قطعا حقش برد بود
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/96997" target="_blank">📅 03:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96996">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
‼️
🇩🇪
#فکت؛ تیم‌ملی آلمان در سه‌دوره اخیر جام‌جهانی به مرحله ⅛نهایی صعود نکرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/96996" target="_blank">📅 03:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96995">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KqTNIiuhxLT0-8OgFETHgqmQDPmUmTmgcFPdrQmBLdZ9IAhnuaj5TfhOvbi_3nAgGzbVzPw43IRSZgIH-VUw7iqwPtNRx06_0m89scgVWBXeb5y0ujpj-quAdHI16DmIIyU7_7MVM8ENW7u3S_keBFUdWoF7U6bHlKAvQNhvGa4N23GhDg7RxUThQzNM7rzxqVDDnNaDWEp7_l0MsWQe-E-xzLuEkC6UEZ8aUc2sq5Nr7-e6ndxk7so9RqhgGesg1tVDL1rfyMpgyY9muueuiy_4mlDPRDMveyOpDn9M5zB60rR_puXVR6e8uzSK2Q_BsSdzYjButYdrqxRts3u9mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک ماه پیش: هاورتز قهرمانی چمپیونز لیگ رو در ضربات پنالتی از دست داد
❌
امشب: هاورتز با پنالتی که از دست داد باعث حذف آلمان از جام جهانی شد
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/96995" target="_blank">📅 03:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96994">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtJUBYk1Wf-Kpjng4xvNfcdH7W_Ds2Ms66BxdK4RSq_0m_iVGW5gGEmt7ZlfQkQgfCTe87nj_wTCAungb-_2ypZbELwfG4LN_Wwpk6VpKdGsrEPuWLOW4KMM_SKUmtwt6g_qDX4PdKDbiu5GjxMAhlIMZYjLFJbaf_Gxw0_boJ6TYaNWX2OO4hxV_24j7XUzojr7UG9Jao_aT45nMkXhFRJJWQvUB48fHx7Q5wrPXjt-HMUGK8UM0fZMABxWqzT4jpcS08YeL-8FYA6fJ8JhsPBJifye40tnAtJgvYhls46acgVVdwYqC_xlQ84fzj4n2J-bcpd7CBr5OaSUCyfjLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇲🇦
ترکیب تیم‌ملی مراکش مقابل هلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/96994" target="_blank">📅 03:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96993">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qy8av1O-vR1oe8T_BY1SBxk7L3Z1VZ0TMeiiM_n7sb2FG1zciFULaf3A59261KsImkkbbnx1eBGH-8x3DVwu7bOtNL4vHiFaBFQ1bOuFboVrku4SjTJ1gUpwMbSKX1lwgbfYrGTDelJp71X60kP6BdbIpavysXIkck4F7Rwlyk77nBQGeH5sVf3No03hJW2GPRGPVW-lkiimd8xFOghMjny_9TjDvmQCE3cFrmeGoa0Jx9EDDTL9PguCinE6L_ybjal8A0IbbrwAp0xn6L_-HolGujaZyBKqZT_AkgIgk8JIKQrm0Z1vJYOOHVRFijOcurvy3Q0tkonOQEmyOqoNNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🇵🇾
🏆
🇵🇾
🏆
🇵🇾
🏆
🔥
Respect
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/96993" target="_blank">📅 03:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96992">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-poll">
<h4>📊 فوری و سریع کی میبره؟</h4>
<ul>
<li>✓ مراکش</li>
<li>✓ هلند</li>
</ul>
</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/96992" target="_blank">📅 03:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96991">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZA-JNAP6l1CgSLuKcqtPJ38wE7brBpdDYGs0-mGp-KsjItk3cG2Wgi63pKy1LULbAPGlo9SaigvRskmKhyTt6H9ntWD4R_O4UqJitWfAjh78O7Q88Qmr16JhQwZJcZB4KO5E06s9OZJMC0BgMXq4SAFB7fdywosBpLjXC6s8njP4uFdKCVLhSxt7UJfdGRQUQm-JuHLhOgqv9rZFbQwp8589bqEgT-xLHWalkwK2xVTHXOth8d_AHoI2UrjlBi3ruDXDPRS3W-Q21RE0-KrxNpqXrIrZkJgdTNTa_dyjOMP97RVp1dxk_XgLDxmYnbbOm6bR0V2LOr3De-SPsuAIHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😢
گریه‌های مانوئل‌نویر در آخرین جام‌جهانی‌اش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/96991" target="_blank">📅 03:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96990">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
‼️
🇩🇪
#فکت؛ تیم‌ملی آلمان در سه‌دوره اخیر جام‌جهانی به مرحله ⅛نهایی صعود نکرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/96990" target="_blank">📅 03:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96989">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Du1D77OUodsYr_UNMU3fmINIc9iiJNTqBV3v16hPbMr9qDgoFaN_rSx8OePdDczFL_eioX4ahk7NDhly72GMiZ0mX3RABwhLWwezPyDEotgcRYXUwRM7fwycrHRtBitrvDWF-YdGlKoSu0_hi1cxVkR5jmuWrV3TnEKnThjfchymKOK9yqVE3cp5s_N_jbQD5ezeCN-rwE4klHn-oUqnlSyH8iYuOPWdmAkYdYZ_NB8uPQcMRfP0EfNKLn5cK_RkqGL7q5OFuH6aem7zMFrfiiD3tnMtEUjaDkeu0pF7fjB_8FnyH8VX8uxnm2Cgonffg1OKzO23Ya8Re7QCj2wGRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇩🇪
#فکت
؛ تیم‌ملی آلمان در سه‌دوره اخیر جام‌جهانی به مرحله ⅛نهایی صعود نکرد
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/96989" target="_blank">📅 03:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96988">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/96988" target="_blank">📅 03:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96987">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VxCxaD8hRrpIWN_P8M_jWNAZ4ythpqQ1UBxFX_JF_kc_6UuoS9IYlhcr7MH3QWjoRL5-ltRZUXhjROWxPWp5m_LLl83jCzT1VwByMECsji8nXfB4R9yUbIRhmit2gyzh4zINyQRVBfxfUGW6eUv_J2b0cQuNLMPQKVCXjVNzh9XoqEvChw9QLEMQEFWxX4aP1HYgbMWUFWj_-fF6vcC919rAGTK8P1o8YkNIr4ML3lcOVyRGNZ6BI0i-eqPmkGMiwmtDEbfi3hHWpgvoS3F0hY0yN6D3yiqpCZ_U9L68UadgzA-_2tJG1WGKs0wKzT5F4K1DYEv7K7wOWqS2xctSGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/96987" target="_blank">📅 03:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96985">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CiQFCZEBYUQbdyG0P5m0Kofa2sZOA5COvqtVZXgxY_qegRPZSw118V-5jKzdKCTv2rDCgIRvA2e7pivZZjXEWsoDhZ013RlhG0kgQUePHf9ZeQdr2d3d7d6pfoXNsUmAqKoS9FhDePGPYjhUIizpLGg_MBXcBE2B4zqKgm93cSJyUwtq6rSg7ezWyf1smBMcxE2f-BvkMtGcQSrYMCcO5zd08zJhAUKKZ_yQHZF3myaG1Cj7okXR5CHrR61VCWqNK2rlcQqDh9UBFJCXN5atXttwQLGiGNQEuFKOY3p2QS-gwkdwz9dS8lByDfGxitEmHLx8yi4npRFIzlhSOON1Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇲🇦
ترکیب تیم‌ملی مراکش مقابل هلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/96985" target="_blank">📅 03:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96984">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">همینه میگیم فوتبال پیرمون کرد🫩
منی که هوادار آلمان نبودم اینقد ناراحت شدم خود آلمانی ها چی میکشن الان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/96984" target="_blank">📅 03:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96983">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/js4DVZrqafVnZDuqngEhKF2_otCWKvxpbxoT1ydlA1583CZhGEFE0FDiDP40jvOSMrsAY2sjqcQClD_ukOlHCwmwMcsQBxSJQoqIjbE1INnZyfiaQkBV4PQ-qZlCqR_ZK3erHwErYvftFjFdBICbo0hy6oGVgCAYAIGfcMmTX9vo9QEQ-w_f0iANwqIX1UrKRmeq9tWyUt0SLeVdsssWfCTu89UbvSVaQGiaUwxeSdYBhBoBGFoHEIk8-BJp6QGMmbP91SFldqwfyDqaBEflqgH7C77ATNJqzoRmaXwgAKhwykDkDxdCkhellJaHo7H2woT7s7qo-RpkbN-HUzt2Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
برنده دیدار حساس فرانسه و سوئد به مصاف پاراگوئه در مرحله ⅛نهایی خواهد رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/96983" target="_blank">📅 03:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96982">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">هیتلر آسوده بخواب که فرزندانت سفت تگری زدن.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/96982" target="_blank">📅 03:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96981">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">نویر
💔
💔
💔
💔
💔
💔
💔</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/96981" target="_blank">📅 02:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96980">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIz5Xz8gR6maHG7zzaO3LQSykRIepr9bJN5i-c808svsUPUN37Ttq1Nyxgpw8nUKBj_v98un2Gp4A99NgrYkeKRnfaxufyenk7ilqFelg7Tre7zgKDGan6pvuG4Aa2xjJzhP5UTn_H7-7fEQRDf1YZl5bM5Dem0W4F9Ibd5aAVEDIX4S_shR_0PXCAOpO4zJRT4VuT7J-FaU91O4-SyRZOUYlcV12QIDkKN0YhPlPm_XjcvThQKcyZYejppoh6aCIomlfhU90FNqOLFFYYEzvwjxlUqjVh9VSmoR2h1Q8DbHvI7upCK_q5xT_lAr_ZbXNSg2CvewGBckc85ntUhimg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
#رسمیییییی
؛ پاراگوئه راهی مرحله یک‌هشتم نهایی جام‌جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/96980" target="_blank">📅 02:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96979">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پاراگوئه بزنه رفته مرحله بعد</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/96979" target="_blank">📅 02:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96978">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">◀️
😀
آلمان
❌
✔️
✔️
❌
✔️
❌
◀️
🇵🇾
پاراگوئه
✔️
✔️
✔️
❌
❌
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/96978" target="_blank">📅 02:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96977">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">جاناتان تاه پشت توپ</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/96977" target="_blank">📅 02:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96976">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">جاناتان تاه پشت توپ</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/96976" target="_blank">📅 02:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96975">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">آلمان برگشت</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/96975" target="_blank">📅 02:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96974">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">◀️
😀
آلمان
❌
✔️
✔️
❌
✔️
◀️
🇵🇾
پاراگوئه
✔️
✔️
✔️
❌
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/96974" target="_blank">📅 02:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96973">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">گرفتتتتتت
😂
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/96973" target="_blank">📅 02:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96972">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">پشماممم</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/96972" target="_blank">📅 02:56 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
