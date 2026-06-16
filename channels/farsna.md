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
<img src="https://cdn4.telesco.pe/file/FqLpROwANUT4gGNE6RiHgWRC9p3V7bjPEjmo_2uaOtdgROh3iEe8TseAh8wE9tngMsjU0yIj4w8aLmf5FlDLw3Xqv5ZjKyh19CSUCxGER5K2GjiUFtiV8dqnm3PkZfN1BGu8EqBDL-4gGGLLO8TL2KcHtuHU0DLzR1c_fcTtzbac4ABRmwSRBdIhJ1BW_w4FkEoz0EbY5gzGivRoW52Q0HXwYJ8dMI8ubaFWP0XLYxiGM-3qtmrag-UxMAxcdPV8ofug3bN9ke0THEFSWAYlkVdKCKn-TC0OakEKCHwOscU7XeQKn_miwdRmrvEiLDYZcaWS0sTeObUQV7GlYh1Q5Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.79M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 02:30:10</div>
<hr>

<div class="tg-post" id="msg-442696">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVNttc2FQIKrWx6K8q-ssdcwh72SrO9jviexOPdCsNTVoVkD94VfK0xlNGTmLtRx1jVaBdJbPJ8V4F6pkOlbutboEqqk4fFmxwfnyxoAr3BPGhLcQXAv8sjLks8PRgwsKBDyjkxjoTqLVcsFi43tSR-FkSu7K6niAlip02CxOeI6Lt6WmPFk4qzqMR1_3HPRunQ9BgOvAUIzWhLJTtvm9_PetUB6biy81d6oMCYGXWf3gzxOuL59T-5GsvpVIzm4jomtfhZLoH-LYwQXIGIEGCXjhMsrtgtluR80yFCM6YP1qwrfLgPZlz0IMvrN5WVuSjXFhOuz77GEcQeD6BIj2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میلیاردها دلار پول عربی در راه صنعت کشتار اسرائیل
🔹
جنگ چند جبهه‌ای رژیم صهیونیستی در غزه، لبنان، سوریه، یمن و ایران در حالی ادامه دارد که جدیدترین داده‌های اقتصادی نشان می‌دهد کشورهای عربیِ امضاکنندۀ پیمان ابراهیم، با خرید میلیاردها دلار تسلیحات از تل‌آویو، عملاً به تأمین مالی غیرمستقیمِ عملیات‌های نظامی علیه همسایگان خود دامن زده‌اند.
🔹
نکتۀ قابل تأمل این‌جاست که بر اساس آمار، کشورهای عربیِ عضو این پیمان در سال ۲۰۲۵ بیش از آمریکا از اسرائیل سلاح خریداری کرده‌اند؛ به‌گونه‌ای که سهم آمریکا ۱۳ درصد و سهم کشورهای عربی ۱۵ درصد بوده است.
🔹
آنچه از بررسی این داده‌های اقتصادی برمی‌آید، این است که روند عادی‌سازی روابط با رژیم صهیونیستی برخلاف شعارهای اولیه، به مسیری برای انتقال سرمایه‌های عربی به صنعت تولید جنگ تبدیل شده‌اند.
🔹
در نهایت این جریان مالی، به‌معنای تبدیل شدن پول‌های عربی به سوخت بحران‌هایی است که دامن‌گیر منطقه شده است.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 779 · <a href="https://t.me/farsna/442696" target="_blank">📅 02:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442695">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e16fc62a5d.mp4?token=ETwn5LkCEoRb8urJfD-Y1CDb9n6zyxLukuQf_EWCu4DXCHlFd9b-qTVRdv4RJ4IhjNZ-4Cf37afCpbasYP_CbHbKu0MNvadgQN3f_i8dchJPUI1y0U8FRwudjRivMfLDIggWK3Yi2kGd6ekPu2bjmGqJpoY8gfN6F21MgW4YR6jQJ2Dzcd3UfvPxQYi3nyWWwnKDsOEz5U1AJkzGjdPzFrJomxlTNsWXRwVnvh2mDO1CKHG1cQGha-PQaIflSA9-E9BUNR4tLuoUs1yBfxcfOOyfaVsrepdzbgtJvyw0O9_YExl8Q49hU6S1zMulUVR3bRgIl9uL3h35SlMse1Uv1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e16fc62a5d.mp4?token=ETwn5LkCEoRb8urJfD-Y1CDb9n6zyxLukuQf_EWCu4DXCHlFd9b-qTVRdv4RJ4IhjNZ-4Cf37afCpbasYP_CbHbKu0MNvadgQN3f_i8dchJPUI1y0U8FRwudjRivMfLDIggWK3Yi2kGd6ekPu2bjmGqJpoY8gfN6F21MgW4YR6jQJ2Dzcd3UfvPxQYi3nyWWwnKDsOEz5U1AJkzGjdPzFrJomxlTNsWXRwVnvh2mDO1CKHG1cQGha-PQaIflSA9-E9BUNR4tLuoUs1yBfxcfOOyfaVsrepdzbgtJvyw0O9_YExl8Q49hU6S1zMulUVR3bRgIl9uL3h35SlMse1Uv1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اشتباه جلال حسن، گل دوم نروژ را رقم زد
⚽️
عراق ۱ - ۲ نروژ
@Farsna</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/farsna/442695" target="_blank">📅 02:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442694">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d39b8b749.mp4?token=bc9W6wCWOw7iJGuvkXA1u1oqk9NZAVIltkbYQvn875AlQoBuUMcUAOra6cSJUaqo0TawHLsnjIsDucSMx_2S93oU7y6xefv_PZOunxPH1teEph4fqqsTHtFqUIjDkbwucz_jJFIi1Ps_GahsqEjn2qzp4zR873HvwVEb5SZJBrAyHfDmQJEIEUNwX3G4JvRn3l1mvh4OM5eyrsxBKF4CqFCtNV8g2FTOIcojcGR7MWeeT38OF64ULGwR4vJUpnPlJj90au_rg4AW3mQUlBN6VHmDF_Xybelnu8aVNpj5xvpLMs7gOiqVlG_7HlTLqU6Bf2PsrNKnQMzDWtdwp5iGtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d39b8b749.mp4?token=bc9W6wCWOw7iJGuvkXA1u1oqk9NZAVIltkbYQvn875AlQoBuUMcUAOra6cSJUaqo0TawHLsnjIsDucSMx_2S93oU7y6xefv_PZOunxPH1teEph4fqqsTHtFqUIjDkbwucz_jJFIi1Ps_GahsqEjn2qzp4zR873HvwVEb5SZJBrAyHfDmQJEIEUNwX3G4JvRn3l1mvh4OM5eyrsxBKF4CqFCtNV8g2FTOIcojcGR7MWeeT38OF64ULGwR4vJUpnPlJj90au_rg4AW3mQUlBN6VHmDF_Xybelnu8aVNpj5xvpLMs7gOiqVlG_7HlTLqU6Bf2PsrNKnQMzDWtdwp5iGtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول عراق با ضربۀ سر دیدنی ایمن حسین
⚽️
عراق ۱ - ۱ نروژ
@Farsna</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/farsna/442694" target="_blank">📅 02:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442693">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aW6_0vEMaYJcv3LHuOa0hDZPU2_jVoyMhClg-LhCJdDRLAMKb-dLp8NhiV4xRnO84Sw2SJBZf5voQRF1hceKzPj1FHkB9pZ5hvWiD3Pngb_IaqyFzMXl0eV9Vdrl1AuryevDPjAOh-MsJ9xcKjz6b-1zZ602lFugAkEG2SLHdCA7Lc2tHf-2sEjfF54HFCI_X085yeLhUGUQkIMuMnXuOiudjeai_zOCs9b2bym9QgeeCCv3W_P92bwaqR4dfbwXgcKcyJDS8oIy-XZBYhYguHDkPPjJuLAaVNGK2kaffjvBkG_LBa3hBvreaCuvKa_RbFicxjaOeuO5QNWEO1wPiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ ویزای مهدی ترابی منقضی شد
🔹
درحالی‌که برای بازیکنان تیم ملی برای سفر به آمریکا روادید «چند بار ورود» صادر شده است اما ویزای مهدی ترابی تنها برای یک بار ورود اعتبار داشت و پس از سفر تیم ملی به لس آنجلس جهت دیدار برابر نیوزیلند، اکنون ویزای این بازیکن منقضی…</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/farsna/442693" target="_blank">📅 02:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442692">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
منابع خبری از حملۀ توپخانه‌ای رژیم صهیونیستی به شهرک کفر تبنیت در جنوب لبنان خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/farsna/442692" target="_blank">📅 01:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442691">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3d1558ca6.mp4?token=lsSXTaHW6Qj6cZiAJL1-vR-75mP9rKjrmyL_dXJHm6df9TuqjAwqHFKTacuHUpcVg0Pl6OzuNhiod5uS2Wjguwvbgg4BECL3g5__0unpLfmV-FuLxC1xme-4l1U1TU0uvDfqMVgB3sme7s8Z3xw_hRwqsjzfOgFxMe6iqQ6isvgK0CTWYITNU3G4zon8PWW4fc21g6Va_VVpFOMfxDFXTxD5VHKhqfWwu3SgyktrJShCk1gqDGoLLqFtGWKuFB9bQtEvP-bVbaf_B1gnY4FQ5v4LLgrGYjqq2NQ94YkNcHA05jhD2QpinKnByj9hfdcqY4VgAqRlzuHiIzLMbSbfeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3d1558ca6.mp4?token=lsSXTaHW6Qj6cZiAJL1-vR-75mP9rKjrmyL_dXJHm6df9TuqjAwqHFKTacuHUpcVg0Pl6OzuNhiod5uS2Wjguwvbgg4BECL3g5__0unpLfmV-FuLxC1xme-4l1U1TU0uvDfqMVgB3sme7s8Z3xw_hRwqsjzfOgFxMe6iqQ6isvgK0CTWYITNU3G4zon8PWW4fc21g6Va_VVpFOMfxDFXTxD5VHKhqfWwu3SgyktrJShCk1gqDGoLLqFtGWKuFB9bQtEvP-bVbaf_B1gnY4FQ5v4LLgrGYjqq2NQ94YkNcHA05jhD2QpinKnByj9hfdcqY4VgAqRlzuHiIzLMbSbfeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون ترامپ: تفاهم‌نامه ایران، شامل لبنان هم می‌شود.  @Farsna- Link</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/farsna/442691" target="_blank">📅 01:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442686">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PZMrHk6Snyaou4YcsfsjmRnbXvWBmkbVXExOQBWF3Jr0W-E0Nvk-rrsOvrE2megCsdASKqQqd73TMzKAkjgz7oMxSS21OaA5xWH7sveKualjucey7xSoOBIprytrdHKSn5u7ET-hdEem8zGzCikrOIgYicHW0NIlXZI_-UvhJrT537nEn2BGdekHbioJQi3KySOJxWGAgSFVKzhqbU-eNwXDP35MJhFWHZDM8_xdlpFr7rmHyxz52Bn7KGQWHdpK6rfCuhKQcjMEeSEqgoU-mBIDUXeSvFE2uKaPQJMMd1NxCZAy9_HFxwMDWE-v79iKewTy6qIehVG7_v4BSeMnKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/exB9ZD0aI4vpdPSySPj7S7qvrLTxuT1L7pIy5KgmaY4ok3iDR9IVqAnyZzBYwKhj9b3R7Vkd20xihQcGMB-EwegFYbHTRjPAB5_W3okmUyszNMGouxiGkxG6fE2HpkqGZx5WdEfwO7Ieebn55B6AoX2lpSCDCmZnJxJxndDq1YdaqwDtoMO0hnZebL9FUC1eBRDQDWs_YxuDeF7Fj9dD1aGRf5OZWEquA4f9VXg6GFCU8hWlS_ovbuFWoq2RuQrb3mkIzRwymWfBIRjb-phpqiXWdIk0kKtqaiq6lgPbwr6MYZlzz1JJVLPI1AfJvxHQhBMvrYjBh2D-XETx4z1qUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z2fihJ5O-CYYeeGEwgbBs8RGDC93YBB-1r9vZ03uDi-2kBQ3s_Lw0ikHwTOMxcyDaj81VRhAw2uJS1hJu1qr0hWod8KDCHb6rW3k0kmv9zIdTte8eTDpwopHdiSxsuWi81bPbQray5OKTmq-zZ45L0Y50cPLrJ2oPSiUQLz7MybwOz6ZN8AUoSQa2FYiFZWD3z-eFFlpjxGB8_5AMe4Q6AO8sSlrgxAzaqg0cXiFKiTgtfg3ialefOOPBZsVcDPfzPaMtQJ83U0R-_TVm6aQU_aM5yaBtzeLXj6Pf6we1skXxMl17ixW4cmB3nGquH2UjpC8xKP5_9orru8FR3Q1Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EKZIyD7lCbPwQxcCBcu90thhjfJv9kyDJKTdiAv8sL_-O2wbtQTT6bf54VwKQrj_4ktEah-75eEpho9xZCe4uQc53xV66l5O0OIK0jmq-9fovliIWKmPaMyLkeIN8QaNYCgzU3zJyEseGk2oRvGnDNeUiX9ChaECzkGF_jsVwC-9jrJLGkX25-r1UMYEmhy0x56qbe-ubcCGqzMWIwgL2RRSUoDW-twCAtbi7dOXOkrBfMbpIFbLlqvDEf_SDDdss3WpRQaejQAAcXo2zsG_ohSqMRRCCplm4CvgGus0CPIDwciA_3T2OL9m_y5j5MttFY1A3nDPcRYp4m12VuCuAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rAYuoXlzpMW1iOUki7tMVG6QrBCQkv3snSC_1HcWx_orWKTxUb6W5xiqCS5oFWr4UxTJnaimPwyjiH1RhKM6yOX_lk3LXb4ZC5_3uhP6LAMNDzyshgo2CkWEwNWpjbRjmlbqDaqCKSaDfKtWndGIS5RK5u_AQqvcBUDUKmvSKJDN85DClxtrmX1jyhJXuDC5hahRDQ3fEm5q7EQI738QNdN9jyBoNAEgVVl3St3OM1OnK5fhN1pG1ohBDClIrUCPzW1STtbWh16E1l79p770vo1bjBaudjdq105gb2Vil3t6XhlopovsNrET2DRC-mEJ8icVGgJAg9Nk6Gg3sNb8kg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | چهارشنبه ۲۷ خرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/farsna/442686" target="_blank">📅 01:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442676">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R6zju-T_Xj_twxZtP_xzoTvZXSJgcZhwHTHBkiPTSh2sIL_7rVfWDVL05Mp9waVqJtu1mHgFMXvLgkmAG95wu7qn7y36mQGccBaCHn2mWpZb_VFOL7eEvWsqQ8DvcoO3Ns0ragz0vpEijRqtUpt4VcwWYpTz145eIV3dgBrvRnBO4pFpJMvZK7lkjLgteqBmCEmLJYCZSqn36lTmRGhY2nonwG7Y7KcwjYcbynVkpQojkKO0Cb4uaUBrKai0zjBsJeM48FlqPPqula0Cdc3jwqg2raUdHyswxX-Uns2g38kfpZmnMZue-aG43Pd5VixKRi3ccorXnNT3VQQWJ_zJfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WjPFeCccdTnydEqwolKO8FdkoBnBkeqc-jyhmtcgMfNgnlvfKPPlC8lUnqwGvQq-H_SDGpv6UAMo_pJUuCYkjnetm6u_vdxi-0bzJb1ejkygA7ST25SXd-ZI2IjQsOrSKwjnbVyoFrow2n5y7-86xw9zdo3Bqsp_hZ83OkD78apOrU2T9iOy_ABiQyeWxa3VGAHqJcOUGgj8I7jWpj7u2He9Sm3mOyXB6tMvTPuuQ3mUKeBnSRRuEltC9IfLaaZKrkPcISt5vMMmQBUq8Hae8WtJwcJPvVZacxKLp53lCODYxx84VqKXG7tALDQRuyIZewc2ubJMBQ0k0OpqEC8_ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KgnINQvFpYr9lwSovXaBgDiLsFmU8GpgXDl-8Eu-64sYKQRCV4Hvpt-vGvwWrq-xbCRR2JLviVBzktIyAQWlMjDsmLkCXRKASfs7VUm_6x3ejCDKpdklpTOrOKWHP8H5h9n7PA0v1CU5OJF9-y4st0pc3O3Jrf9V4I9cL9Xhlp9EGvlIlKmN2DGSS7BpI5H-DRtfrGEhcW9l3qPD2RsOr-RISJRr8wPsOgjx-WsV1bMsKRrmHrxYzgxwehiTrTBFzp1LVASNFhPVjJuQJ4m3pQyQIiiGOVUH3gznJD28-l7gNTWdK0mefa6hxY_lT1_k3Hsg_246npZhIlvqKpehSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fzTc5_2dCZ9IxpiDsDfKxh3neFPpyOhHOp6qHn9Plx-b7hHfrCZPGbvz5H8eHnm3TgDsUkYT3uMd2nhAVBvgqLZOdm44G2ezGb6HpgIigYbSIoFOkluZ1VSZNadlZINLWy0kmPjXoK5UzYVfUb9Nm9P-GVh3hQpbwrCCoy9SRtn31mjpImHjhX5PF3ef1cJwgQ_dJQNA_Ccze9WzjWZJ9EqTyv9qJ-A1qAfpOnQk6Kvm9DZnY4j627olOYdWDmkugFrj1JCIwPQu_iqG1l5J_U5JMaTDztWJ6141zp0XwpJ-fkL3aOwt6rWnK7vtCMKkS0Amw_G7SmgEcsUhzrP2HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pcx9cpkbrhRLbPLEmhXTC2BeDQO1dV3SRyUNWB5qW3LasfwGGEryANCRC1tdS-Dox8qhyvg20sfBnDWvgQCKS7ONS81kGul0fq1-22joNFYRdTpZzm7fGtqKdxxoTQBRgPV9kfWrPz4MQ-UllKhVb8qTHFc6ZcQz8IzQlzza0YQBgp7zQseITeyIrb6UYNCeF0drCewfkyyT6vANS8ysNgxf_eviQkxwpQNJV9TtxtGHIhzuSWv8y4MfXNJrQK8JJjl-PWU6opyIyBdzBeBrk0vWQ2V5mAOEqkjvIeQwK46RpN9QPwLaopAnprMER-sk5mosJtx5H5L0epYm3HQgNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/epaLXXUzx1jHKck_St0EdLKgOeTiHPre3a-L5GRZX2aDbOi5Mqjvbl2NBUe7Tw0D22loNlpxiEfmvJEKHKueFgBYD2EMn3qETOEhSOR470lRtiveCvkB3ocJQhIzQhSfpYQztx48NEx3GwknMCL_WNiAHnOV74WqiRWIh6NgLM9Rqts-PNkwgC6RTLXhbtRzxlaBAjXoVlyX0RtJgrNkby9Km-UNLXLYElBB2oTPOicZixyRfRz2AjCCbb-lTkPcjlETUcHw_WyHlD13QjhLobaj-VYDRVnKdAOHCJcfl8tOkCZTshsBdLLFPG1yzRcVC5bL87mMvqOZyg0aR_v4yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TThrfjAYg2bYBg9ZEviokhK-cEnfubEJFfBShRmQLJHJPLeMNpW_9waSI9P4Ji__gJVTxQYSdsiECYHBXioldTrBoAFv6DdlgWOkSnoUNdeJ8zc7BkvWwfBO5aPV4Ly7qA9JAYX_uf2-RnCYYJVu6NpDDpHH2lbl1OP-u7e0C9WIAjulLfE9yzJaxAkVi6PDR1T9hv9S01B-WKb-ANAPZXpuPgD5L8wdakrl1suHpVgG7Q59tHCysF1qkslhSpqYEAaAEYrDtVEHkTLiz_711NCiMGKIy0RhS0EGMuNxXgmWxg7JCbXENkCTg8rYsE8i5U2znRXQQ3TT9e92ibzTLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VKM-cthDRgGTHYdCi8cyVPrPUrB-TbNDbdXXQIZ-JgIsYo8yRH17DAWO1zbBZriUwmM6fdLsbD2GsG6U0NHXjVkeNZB9wBzpbnQD852cc2_sYQJ4BvGf7mbejO-E1vxLPusF7uIFiuSnnEHgCyDEmqlqGpG8xS41Rss0EqwzyEqEYFmQY0V3cQ7H3VFXqi6BTdYM__nIBiRj3jC2MTmLvLZFPdPiAicGDAnw95D9iiVseXdRmpogrGBcXnGx6Q-uesmCaONbnUQ3X-GO8KD5si_FRG7D-WuEWwLgy-N9yJVXK7jyqpT9mBFasZvTJLBvyFEiBJJkSX3CxCb6lg_YWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FQHBVgjQnBlVqvbeOd3vRt7lW6e4tJFdqpkWGYkhApmfYloXgCtWJvT61C0QaZlHcoa9jEo_BIa6qgCcXnMQvtajzGgfTy-ceG00c_0SURsREmyLmx3ekPB6QoM6Ba5UitWmPH1f4IWpzYzh-bCsHUmZ8orDJliNT4lIvjX99D-MrXZkGix4HKHj_aIRa0V6Xj0WavWApbIPjMtO_fAU3hUx2Er7qMXmKt-6esTusvJnYuJQ3Y-vZQlzxJ02mUaeAfUX8oAgPn2CJVkrRFqDXCxuxTAHuxhCWgms7G9hZYRnybm2jY3PklDQyO580aj0uPaX1T1Jy_Qs_c4PBGTghg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JkRGjZbL9koF4QJ3-1IgWxCZvdC36UUwOu6IHEzf7iHT68gxiMqS0JGDBn-068-Unc6zBrnRP-lYHi7CamPSrI6UQrdgKe-NAFf-3z163Mu04dmWcq6gc13Z4XgIXmo_xIIrneS37rLcB9xnUxm4113CVHedbtlEb2Mng3UlB-3qWEbcCtsOQ50nujpXtIUYM9ZiErAPeEjB6DkDgLC6x-c7RK1Uzya_fCV0il8xdloG_jeXYIsZlNd9RiVn2V4aqIyqXHVq28jaFEe7kEZrRucLsIMa9E8uJ99no7gqzuvTx3zM_3ACknSco_TDbsNbLZq5u61E7-B3v1niEOPRFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/farsna/442676" target="_blank">📅 01:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442675">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb211899e7.mp4?token=JkhnQi_tGnog4cIHZ6fOXINOq9rfV2AQYb1x3hbuiTgV4E47LBVgFqLGNFc9a9PMGN37Elsp4xy87dqSkDO5V2zI_cU3x5akERq7oTDqKA_W-lEW5p-nnPDbNQYz4kXw234ykgNMD_D69xd-Ij-e4g0TmvpIkvItej2R4u6j73Pc_rvKv2hkT1ptGenZs18P8_MGaNwke7hBQ-cik4gXFbym4iA-TY6EAsPHdZiP-kbgqpg9xpc8OeNmERTN0Qa7nk5yJiebsrMwHUGfULkp-45slHOQazDe7aNtApG6UMoC5wdmwKZ8S1DlkFYC1zqYQGjhGGjsftUQ_ZbZSyEEyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb211899e7.mp4?token=JkhnQi_tGnog4cIHZ6fOXINOq9rfV2AQYb1x3hbuiTgV4E47LBVgFqLGNFc9a9PMGN37Elsp4xy87dqSkDO5V2zI_cU3x5akERq7oTDqKA_W-lEW5p-nnPDbNQYz4kXw234ykgNMD_D69xd-Ij-e4g0TmvpIkvItej2R4u6j73Pc_rvKv2hkT1ptGenZs18P8_MGaNwke7hBQ-cik4gXFbym4iA-TY6EAsPHdZiP-kbgqpg9xpc8OeNmERTN0Qa7nk5yJiebsrMwHUGfULkp-45slHOQazDe7aNtApG6UMoC5wdmwKZ8S1DlkFYC1zqYQGjhGGjsftUQ_ZbZSyEEyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون ترامپ: تفاهم‌نامه ایران، شامل لبنان هم می‌شود
.
@Farsna
- Link</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/farsna/442675" target="_blank">📅 01:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442674">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B0GVUJ_8xDQG_RkY_1PJM2ZzNqIWU_a0jNjwCyYG8_ndlmkEcDfZIoldo43xSFWAt8C3aRDLVPv3wIDiIHsnLOdVezMv-P3bmwzkMwgJCgY0-GXGowDWvs-_jthUssCh6IinGExwjLhmEQOpqiNdRsNc5JPmHHhp3s_B6oCg4-wEo5LPHVRZ6_k-JzejQvdcEZS0Y5HP5FVorlwlTrirTssr6VOlLnpqum6LB_PlyL8tlJhEvtuOZDx9Rv_kmcf6nVv_MVZbhrJg_EVISfEPhOJTo7Ygc5u5QN_rGSjK2iWoLE5x-qcyfovy1rPueTNc5hRdtHvYdzlcruuiPcgVLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توپ جام‌جهانی با داوران حرف می‌زند!
🔹
در پشت‌پردۀ این دوره از مسابقات جام‌جهانی، فناوری نقش مهمی دارد؛ نقشی که شاید به اندازۀ عملکرد بازیکنان در زمین، بر سرنوشت بازی‌ها تأثیر بگذارد.
🔹
یکی از مهم‌ترین فناوری‌های به‌کاررفته در جام‌جهانی ۲۰۲۶، نسل جدید سامانۀ آفساید نیمه‌خودکار است؛ سیستمی که فیفا آن‌را برای افزایش دقت و سرعت تصمیم‌گیری در صحنه‌های حساس توسعه داده است.
🔹
توپ رسمی جام‌جهانی ۲۰۲۶ به حسگرهای پیشرفته‌ای مجهز شده که می‌توانند اطلاعات مربوط به حرکت و تماس با توپ را به‌صورت لحظه‌ای ثبت و ارسال کنند.
🔹
یکی دیگر از فناوری‌های کمتر دیده‌شده اما بسیار مهم در جام‌جهانی ۲۰۲۶، استفاده از مدل‌های سه‌بعدی دقیق بازیکنان است.
🔹
در این رقابت‌ها برای نخستین‌بار از سگ‌های رباتیک نیز در برخی ورزشگاه‌ها و مراکز عملیاتی استفاده شده؛ ربات‌های چهارپا که وظیفۀ آن‌ها کمک به تأمین امنیت و نظارت بر زیرساخت‌های حساس مسابقات است.
🔗
جزئیات فناوری‌های دیگر جام‌جهانی ۲۰۲۶ را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/farsna/442674" target="_blank">📅 01:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442673">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vX4U1PBCUxCF_4hd0Ms_er3Z08gbBzA2fvChtX_wg-s1ysW2QWR4tRq2G03vzLiz-j4sz4U0rGo8RmljF9A6y_qBYhuRj-j5y4LjdjEkeHVqa3VVmOAg24MQo9e-n3ftUDvUfH4BKZb2Tp3cBSHGqhmCD6pjojS3qYdXvFVEW_K6qwpimdoj6loM5cP-LHiabsIEmTDyLZHeykZS6tg96callY35ckvnYAGRg99k-0WzKL5VeP9F3uB26xOJcyTt171ku0gcKED_ImgzD3IfMS-HEZ5tzsTPJ3-RoMxc3sn5WpI6hjBMjRShTDWvxgnm50ZFhkddNqKEo7uJyJLWCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه با توپ پر جام را شروع کرد
⚽️
فرانسه ۳ - ۱ سنگال
@Farsna</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/farsna/442673" target="_blank">📅 00:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442672">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">کتاب آه</div>
  <div class="tg-doc-extra">قسمت ۲</div>
</div>
<a href="https://t.me/farsna/442672" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قسمت ۱ – کتاب آه</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/farsna/442672" target="_blank">📅 00:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442671">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02a1dc3c57.mp4?token=R9h8fXSrMzIf0KlcmC42Gt4ewuxSLL5zzIDhTS3ZR9iz1VtW4CJFatwdkcZcJcB9oNXnDAuCZhoXygPSixFq9EzCSUB2xDIS72BR8-0ZpONWF6ZamU99z52ZDP0CEuc2G9KaHczPNwM1I6mYAuH7DwKabo2uoXzgINSs3GDBNpQTA14K0qIsd6WammzXuRLjbxHVo542j-IamVxhFQKfiEEfnHV8GNQs2C1OF2Ei8vE4LwNua9DcaSixA9uppMXqAFltz_0c4G6U97RkYOwK9jzhLhgZo0Ra41TbFO4XhJmJidutIB3xfp6BZ9wNIytOS4Jb14Bm4Sku3F5Jdlm6ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02a1dc3c57.mp4?token=R9h8fXSrMzIf0KlcmC42Gt4ewuxSLL5zzIDhTS3ZR9iz1VtW4CJFatwdkcZcJcB9oNXnDAuCZhoXygPSixFq9EzCSUB2xDIS72BR8-0ZpONWF6ZamU99z52ZDP0CEuc2G9KaHczPNwM1I6mYAuH7DwKabo2uoXzgINSs3GDBNpQTA14K0qIsd6WammzXuRLjbxHVo542j-IamVxhFQKfiEEfnHV8GNQs2C1OF2Ei8vE4LwNua9DcaSixA9uppMXqAFltz_0c4G6U97RkYOwK9jzhLhgZo0Ra41TbFO4XhJmJidutIB3xfp6BZ9wNIytOS4Jb14Bm4Sku3F5Jdlm6ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کلینیتون: ترامپ بعد از حمله به ایران گفته که «هیچ‌کس به من نگفته بود که ایرانی‌ها می‌توانند تنگهٔ هرمز را ببندد.»
@Farsna</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/442671" target="_blank">📅 00:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442670">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BqgcMlQFPY9xzds5k34aHKCzEZWZ61HiRUjl98lrfFQIv142I3R7s0-quW_Wx9iLvHDGPeEAEzt22J6aX-5RIH14X0hhxQejkDc-ACrsfZCsNLyti8v4NUsaS6IpqHBuliPw8GlwKA7fqp-KGh_-4YIzj9J0XSNQjvS-zRoVG8Ov-ZL3C1VVyODZMqsOYFGX8BeaeAfySHzVW8v-363TbYzFtBc2bdWKVkXpxXx_wIO0qrBCDjdDOXE09rJEbQ6ZgIiF5dmkHGGr5KUoPr81EwmvkXulPpSatRPJGeOQ-B_ADlDQOsz8OAkswLPNl-wMEJMeOHifOWviYzJq2P2oFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمول خدا برای روزی
🔹
مردی به امام صادق(ع) گفت: «برایم دعا بفرمایید تا خدا روزی‌ام را زیاد کند. من خیلی فقیرم.»
🔸
امام فرمود: «هرگز دعا نمی‌کنم.»
🔹
مرد گفت: «چرا؟»
🔸
امام فرمود: «خداوند امر کرده که برای کسب روزی کار و تلاش کنید اما تو می‌خواهی در خانه‌ات بنشینی و با دعا روزی را به خانهٔ خود بکشانی.»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/442670" target="_blank">📅 00:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442667">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70bdef0fa1.mp4?token=dX77oDSrpKmkUXFfzM9Fu1p17uGOR8Xo7VrQBfQ18OZH_FJ3egAhz-z74nh6L_vhrXV9enDT5c7gE78doef3j8ksPgAhoLE5qSTU85Ckl5T4UKrkAwBh8nCTsOpictdIkfGdfYS4G9rAThaQYTuVzy5wYVUR8Vc_JMhmkjBEWDHOiAKm2CGvA3Y1nC025bFwnjQtMFNQ_HNqM4rwull7fY-LvgLlpTIF3_rfGEDIAQyWmq096MUgo1pplCTEtvuhvCTz0xw4ATUkzv0dGGCEBtg7vH9DdmqZ3I_znV3wwxCG6b5WWWJDtCugN9uWSUwArf0L0LQ7iJzZ1aVCthX1wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70bdef0fa1.mp4?token=dX77oDSrpKmkUXFfzM9Fu1p17uGOR8Xo7VrQBfQ18OZH_FJ3egAhz-z74nh6L_vhrXV9enDT5c7gE78doef3j8ksPgAhoLE5qSTU85Ckl5T4UKrkAwBh8nCTsOpictdIkfGdfYS4G9rAThaQYTuVzy5wYVUR8Vc_JMhmkjBEWDHOiAKm2CGvA3Y1nC025bFwnjQtMFNQ_HNqM4rwull7fY-LvgLlpTIF3_rfGEDIAQyWmq096MUgo1pplCTEtvuhvCTz0xw4ATUkzv0dGGCEBtg7vH9DdmqZ3I_znV3wwxCG6b5WWWJDtCugN9uWSUwArf0L0LQ7iJzZ1aVCthX1wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حمله طرفداران الجولانی به مغازه‌ها و منازل علویان در دمشق
🔹
براساس ویدیوهایی که از دمشق منتشر شده، طرفداران شورشیان سوری با حمله به اموال شهروندان علوی خواهان اخراج آن‌ها  شدند.
@Farsa
- Link</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/farsna/442667" target="_blank">📅 23:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442666">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fccaa2c4c.mp4?token=N55G6IEMVu5jQPdQnxVOQUe4yeDT5q0mANgscp7IU5TYIsb8SriZH_1BVSfJNOwrDY4QttB4KmknXC1VvjFcmgRd1mxBNBhknz1v7JBG0MrawXqSK3vufAaqASxGIUw83KCCoKpq15USucS0HB5pckz_wc89mfApRF1fqNVdOhyrqtjG02yfhWIE6TvXwA9uR8V2IU2ZoDG-SdxNIn3nKuGGsuz-xxvr913z7dKIizrp7oy64KxbEIyURHCAzWhrIbcQUS0DZQh6V-xNIWGnL4ATnaY7sFAwgkm5FzgrYxmlTXAOtmbk5ORu-NMkxkZ0PjR1-d-mF_EOWSqz-7_zCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fccaa2c4c.mp4?token=N55G6IEMVu5jQPdQnxVOQUe4yeDT5q0mANgscp7IU5TYIsb8SriZH_1BVSfJNOwrDY4QttB4KmknXC1VvjFcmgRd1mxBNBhknz1v7JBG0MrawXqSK3vufAaqASxGIUw83KCCoKpq15USucS0HB5pckz_wc89mfApRF1fqNVdOhyrqtjG02yfhWIE6TvXwA9uR8V2IU2ZoDG-SdxNIn3nKuGGsuz-xxvr913z7dKIizrp7oy64KxbEIyURHCAzWhrIbcQUS0DZQh6V-xNIWGnL4ATnaY7sFAwgkm5FzgrYxmlTXAOtmbk5ORu-NMkxkZ0PjR1-d-mF_EOWSqz-7_zCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال
‌
وهوای تجمعات مردمی گرگان در شب دوم محرم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/farsna/442666" target="_blank">📅 23:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442665">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🎥
تجمع پردیسی‌ها در شب دوم محرم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/442665" target="_blank">📅 23:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442664">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4e4206dda.mp4?token=DqAv-1HBtk62eT79ah1BVHsT3tcPQ9kN5aDDH2csiACuN3eBYMNRQfae_0RUMDhdkohZhl4LXO-M2IHCa36_vOuAz2Q4vAXEzUCaRCVGdoOzivrZQv314CBsnH7wduTXGqZDC12dYE_6gKK-ctE0HV3zfB0IcdyGU3pAe2NaHcjqlDtgn5QIxivOo4bYHlNF0NnBtORWorjwzaBdqz1h4586xQqfR_rOMCh2Q4fU9Sm9JdeXXVDUlSng7GdqXZq_T1dpCz8Xs2wLWFSXkBO8PMoI3Mo2Qcg0uf_re2dkWdtDLBAr3T8u4fSwN0o1BAGeGSGE7Xx_RFAyygXvltzDrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4e4206dda.mp4?token=DqAv-1HBtk62eT79ah1BVHsT3tcPQ9kN5aDDH2csiACuN3eBYMNRQfae_0RUMDhdkohZhl4LXO-M2IHCa36_vOuAz2Q4vAXEzUCaRCVGdoOzivrZQv314CBsnH7wduTXGqZDC12dYE_6gKK-ctE0HV3zfB0IcdyGU3pAe2NaHcjqlDtgn5QIxivOo4bYHlNF0NnBtORWorjwzaBdqz1h4586xQqfR_rOMCh2Q4fU9Sm9JdeXXVDUlSng7GdqXZq_T1dpCz8Xs2wLWFSXkBO8PMoI3Mo2Qcg0uf_re2dkWdtDLBAr3T8u4fSwN0o1BAGeGSGE7Xx_RFAyygXvltzDrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار امشب بروجردی‌ها: حسین حسین شعار ماست شهادت افتخار ماست
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/442664" target="_blank">📅 23:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442662">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67dae8cfb2.mp4?token=KIcwKiSR4soqofMTgKndfNrbXFt4YHNsb-QGPjaMMdHLo-yiZhSO_tB6YEx5htFbYXJAbBHX_6g6SAmTqXUDtuFyZ3i2XvLNUpB1B2AOfZqKTURPIy3_AhTPDJ0zBI2L2-DMXQWOCGvys6AHTsszRTxHmt8ruAN1fWpNU2--7FHZuDVeEaqvBL7e2DeaR_tY428G72x0f6T7jWhli1v1xHLZbNRQ0ihEOAEeVTj4hLwm0l2DgahEjNN0LxxMqcCZ32n59pmRo5UabmQfqa9kEgekxr37xi2lL_Lk-ZuMQdn1SlEJSn3pDTsOChGuvIq0HL3I6UxuBaxhSbfC_zEZ0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67dae8cfb2.mp4?token=KIcwKiSR4soqofMTgKndfNrbXFt4YHNsb-QGPjaMMdHLo-yiZhSO_tB6YEx5htFbYXJAbBHX_6g6SAmTqXUDtuFyZ3i2XvLNUpB1B2AOfZqKTURPIy3_AhTPDJ0zBI2L2-DMXQWOCGvys6AHTsszRTxHmt8ruAN1fWpNU2--7FHZuDVeEaqvBL7e2DeaR_tY428G72x0f6T7jWhli1v1xHLZbNRQ0ihEOAEeVTj4hLwm0l2DgahEjNN0LxxMqcCZ32n59pmRo5UabmQfqa9kEgekxr37xi2lL_Lk-ZuMQdn1SlEJSn3pDTsOChGuvIq0HL3I6UxuBaxhSbfC_zEZ0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حمله پهپادی به مقر تروریست
‌
های ضد ایرانی در شمال عراق
🔹
برخی منابع خبری گزارش دادند مقر این تروریست‌ها در اطراف اربیل بوده که هدف حملات پهپادی قرار گرفته است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/442662" target="_blank">📅 23:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442661">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d42c62b2d3.mp4?token=f0vsKLcGpegx95hceqrVGSy7kmsoEJAsIwWJWiuLMre9YkzJZWKdMSNcXDWdz7xRP2I8nYqNMXwU2ObaQBfxZxQiJ131o06gRCIXB5tZhkOFFqyuoBO3KvvxO-Ud8TPuUP-SL5nM9xbTngk2zRzuCkv6ETimTD1_4r7OFnXQvyUEUjg3YQM27EkxoPWhcg7TngV5Zmt3c6CErJpgJMZIB0uCZlhsvYUJ7niQuIUdzvaYz_ZgJf1iVUcPxis-w-vjUtegtuQI1PWNR1ZdfnTmDdwNgXh2r3Oc3acFCgGzoBUlnfLefIDUsZSPa8peZ9n03tpUGt77XZfmPhNVvkJosg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d42c62b2d3.mp4?token=f0vsKLcGpegx95hceqrVGSy7kmsoEJAsIwWJWiuLMre9YkzJZWKdMSNcXDWdz7xRP2I8nYqNMXwU2ObaQBfxZxQiJ131o06gRCIXB5tZhkOFFqyuoBO3KvvxO-Ud8TPuUP-SL5nM9xbTngk2zRzuCkv6ETimTD1_4r7OFnXQvyUEUjg3YQM27EkxoPWhcg7TngV5Zmt3c6CErJpgJMZIB0uCZlhsvYUJ7niQuIUdzvaYz_ZgJf1iVUcPxis-w-vjUtegtuQI1PWNR1ZdfnTmDdwNgXh2r3Oc3acFCgGzoBUlnfLefIDUsZSPa8peZ9n03tpUGt77XZfmPhNVvkJosg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال و هوای مشهدالرضا در دومین شب محرم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/442661" target="_blank">📅 23:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442660">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df266beb6b.mp4?token=slW7p63DlceHQad3ZcpPc70pmxgZWft-olVZVywYamdlMxsjEUrdT2HVvnRpAaMuEKu_uhGeXf5SvVxnBloq2Lf-TQiBMUYBV43pvzNKjZIyEJFqTirWQ2dCtY0rjBpcY7aIrOaOn2pIoTIUF2iOrndAMS1K9YLPMxoyfHWQkEp1IAbRshvOyB4A90whByxvj97MRPzziB3ac5j8aeBJFQ7NK7CrVqQ1IdxV4HQUJSWmiTq_zDTev8m-zsErR1pay5mrPx2tRqTlcsX6K_zYSfuR1fsWOiD2PdXucTUAziqgwNG7se89HrDgZIo_gwbvUJHFDXko5GSRLFUd33FpfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df266beb6b.mp4?token=slW7p63DlceHQad3ZcpPc70pmxgZWft-olVZVywYamdlMxsjEUrdT2HVvnRpAaMuEKu_uhGeXf5SvVxnBloq2Lf-TQiBMUYBV43pvzNKjZIyEJFqTirWQ2dCtY0rjBpcY7aIrOaOn2pIoTIUF2iOrndAMS1K9YLPMxoyfHWQkEp1IAbRshvOyB4A90whByxvj97MRPzziB3ac5j8aeBJFQ7NK7CrVqQ1IdxV4HQUJSWmiTq_zDTev8m-zsErR1pay5mrPx2tRqTlcsX6K_zYSfuR1fsWOiD2PdXucTUAziqgwNG7se89HrDgZIo_gwbvUJHFDXko5GSRLFUd33FpfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوجوان عراقی که در ایام جنگ دوچرخه خود را برای کمک به ایران فروخته بود، از امام رضا(ع) دوچرخه هدیه گرفت
صحبت های شیرین نوجوان عراقی در حسینیه معلی شبکه سه
@Farsna</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/442660" target="_blank">📅 23:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442659">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktI3WQkXPYNhCxkXkBzukw0G8ehP26aUL2D0MI8C2GFbhAdPK1a0AA3rjN82vO_LToxxprGWivudVFcPkVrgLTG8njwHhpofXdiLDEUk7NX8TFSmbnx98y2o0GFTNbFFUIC_mLUPBuoXMJ-S-22ZzB8ol9L3jnEw5YaJPUpOV0MuDqOvnzVkLgGabvzR7118VpLqrh5Bzs0pdh4AogpgHzFmXTg59X8jKj71Qn6krarvt43J8hwdUQ0DwhnQUK-VuvZDXg_8IEjkvjtUFENwQvr2ikebwVlEOxJ0jNPe30IhM5E22bFGJEMjPLxhKG-mEMquUVvc8IW7PpOfvRReQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ترامپ: اگر من نبودم الان اصلاً اسرائیل وجود نداشت
🔹
الان اسرائیل ۱۰۰ درصد از روی زمین محو شده بود و هر آدم باهوشی در اسرائیل این را خوب می‌داند. @Farsna</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/farsna/442659" target="_blank">📅 22:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442658">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41a70598a0.mp4?token=IGTlna3hQ_lNRt3Z39R0CH0oPZfdO9VRVSHCBWchHHsX5yxkDnfWCsmDZAsf7_6g-7OkXDKkZOrx208bsYj-ChKUjEWgNIP1vUMNAsynuCfKYBEXd6aoBrSOHsUOqmDW6dTMzJHk2l5_J-DFfL6TvBP25x4xjDG1FSSqf3KXjUbA9o7_m9ScApl-qcgN24FMYj8dK7WSMLNiuor1PT1G92RDHF5A-7rw-bwEEHvg22HVFq66h1A-vBGZStKGAJyM6BpyKkvb-mK_ynZ2FL0h5sPfybcz4UjvRL7-UOGHDrCSjHvMWF8UVxQXfthuLvnw6GmIQk32qMX8-cuXglUG4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41a70598a0.mp4?token=IGTlna3hQ_lNRt3Z39R0CH0oPZfdO9VRVSHCBWchHHsX5yxkDnfWCsmDZAsf7_6g-7OkXDKkZOrx208bsYj-ChKUjEWgNIP1vUMNAsynuCfKYBEXd6aoBrSOHsUOqmDW6dTMzJHk2l5_J-DFfL6TvBP25x4xjDG1FSSqf3KXjUbA9o7_m9ScApl-qcgN24FMYj8dK7WSMLNiuor1PT1G92RDHF5A-7rw-bwEEHvg22HVFq66h1A-vBGZStKGAJyM6BpyKkvb-mK_ynZ2FL0h5sPfybcz4UjvRL7-UOGHDrCSjHvMWF8UVxQXfthuLvnw6GmIQk32qMX8-cuXglUG4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شب ۱۰۸؛ سینه‌زنی برای امام‌حسین(ع) در خیابان‌های شهرکرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/442658" target="_blank">📅 22:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442657">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f858e5c5e.mp4?token=ljwzofxngo0iY5kj9zrXod1iIUy3NasftjVgdYHLtxnnYLeW2WrgtWHeYeoAs_IwUGmI7vOPEff0T9Cy6wKX5XgFw5ojOs-iHrUcxj1ygU2DRfDazJow9WuTh-AoY7PdnBBwFtM2hfoiIdqW_LBXEY9E9ro2Ie5j692HLjXKuKPBgzuiQ20M2THyqb0Y20z2OfIu9mek5vI8RX-dwRcC0LJthAG3r3EMh5osJQTH5SffyDL86m2tVQ-mtq3jNjUa2uWHZ9ZMv9Nh3rNNo149soGpR3xbUdBjA-tcYfr-Y4fhNOf4Z_5mt_xOKnVMh8waX-6W2gyS3XggAfQ7aJ1xJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f858e5c5e.mp4?token=ljwzofxngo0iY5kj9zrXod1iIUy3NasftjVgdYHLtxnnYLeW2WrgtWHeYeoAs_IwUGmI7vOPEff0T9Cy6wKX5XgFw5ojOs-iHrUcxj1ygU2DRfDazJow9WuTh-AoY7PdnBBwFtM2hfoiIdqW_LBXEY9E9ro2Ie5j692HLjXKuKPBgzuiQ20M2THyqb0Y20z2OfIu9mek5vI8RX-dwRcC0LJthAG3r3EMh5osJQTH5SffyDL86m2tVQ-mtq3jNjUa2uWHZ9ZMv9Nh3rNNo149soGpR3xbUdBjA-tcYfr-Y4fhNOf4Z_5mt_xOKnVMh8waX-6W2gyS3XggAfQ7aJ1xJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شب دوم محرم؛ گناباد در تبِ «صد و هشتمین» قرار
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/farsna/442657" target="_blank">📅 22:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442651">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سخنرانی</div>
  <div class="tg-doc-extra">حجت‌الاسلام کاشانی</div>
</div>
<a href="https://t.me/farsna/442651" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
#حسینیه_فارس
| شب دوم محرم
سایر مداحی‌های امشب را
اینجا
گوش کنید.
@Farsna</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/442651" target="_blank">📅 22:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442650">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/442650" target="_blank">📅 22:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442648">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EW5gYzvR5sB-ofrKu-w0n69-0yZr7DLMYAk7q2DST8BupevgX62N-6oiTcc6ilPeoehDhvyGmFi2lqElSNZwCxWSCMKYXBMFVoc-kuVeAEagho5qIA9huewSKTnlYsL4EEeBeIMppkKv-vJ0L4r4qo428_ByckGIg1Z3IEEcTspRPyv49yWb9lyBvJXgT_C2Mqa4xMAD7U-by79_OU4Py77-G-toVrFrda3xsUCrOdIHI7UNSLayFGpRl0OPuROVhAgUb_vbr8F-nfDL0I3N7dpo2GY6W5tyrvX401KYsGWnbfAua0bK7UnOMfJZnzwniQ4QtsreYF2DRuEAmADl-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری از گفت‌وگوی شهید سپهبد سلامی با فرماندهٔ شهید کل قوا
@Farsna</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/farsna/442648" target="_blank">📅 22:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442647">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
هشدار قرارگاه خاتم‌الانبیا به رژیم صهیونیستی
🔹
قرارگاه مرکزی خاتم‌الانبیا: ارتش تروریستی رژیم صهیونیستی طی ۲ روز گذشته پس از اعلام پایان جنگ توسط رئیس‌جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض کرده و همچنان به جنایات و کشتار مردم مظلوم لبنان ادامه می‌دهد.
🔸
هشدار داده می‌شود چنانچه ارتش کودک‌کش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ سخت نیروهای مسلح مقتدر جمهوری اسلامی ایران باشد.
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/442647" target="_blank">📅 22:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442646">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4e5033ec2.mp4?token=V6EpvYM0RmyQzKSwR8euGXyDr6jZay44HTKiR0_KIXEXMUjByjUIMcXb3eJxZUAp7DXeOaoQGtV-B2T_-3U_BY-CYdDY8KAwU6ioyxU5d3o4gLUXMzCrG9sBeTJ1VaZeeskt-fTzdqVqI9MAInuTX1UTPAsDRk8mxAVs_VOTPZdZzHt-ylnbyOBqrtCkZkJJKZ5rAOHIa83ymGU-4FdILjidOu-JsFCV55lQcNV4upHeji6ozJ5IQneDRiVnpjLxVp1TGsXjvt0UP83LLBUlwqCPS65UVawtXieS-kMYvXz01MXfg_fuGa1rTfKGh-Sc5Urm_a6dOxP5no2gHLSDsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4e5033ec2.mp4?token=V6EpvYM0RmyQzKSwR8euGXyDr6jZay44HTKiR0_KIXEXMUjByjUIMcXb3eJxZUAp7DXeOaoQGtV-B2T_-3U_BY-CYdDY8KAwU6ioyxU5d3o4gLUXMzCrG9sBeTJ1VaZeeskt-fTzdqVqI9MAInuTX1UTPAsDRk8mxAVs_VOTPZdZzHt-ylnbyOBqrtCkZkJJKZ5rAOHIa83ymGU-4FdILjidOu-JsFCV55lQcNV4upHeji6ozJ5IQneDRiVnpjLxVp1TGsXjvt0UP83LLBUlwqCPS65UVawtXieS-kMYvXz01MXfg_fuGa1rTfKGh-Sc5Urm_a6dOxP5no2gHLSDsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
رامین رضاییان به‌عنوان بهترین بازیکن زمین انتخاب شد. @Farsna</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/442646" target="_blank">📅 22:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442645">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">🔹
برخی منابع نزدیک به تیم مذاکره‌کننده ایران، ادعاهای شبکه خبری العربیه در خصوص متن یادداشت تفاهم ایران و آمریکا را تکذیب کردند.
🔹
العربیه پیش از این نیز گزارش‌های نادرستی در خصوص مسائل مرتبط با ایران منتشر کرده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/442645" target="_blank">📅 22:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442641">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XaXER0Gky3saaipIKZBNrOhzV10ptA14BAYQGTyV-QW_PnuTp0pnkpogUjsBjRf_BphoaITJYeSn1etxX5PjHLo6p4xUSb9p4DRuFfy9ss84QUYnQq_9zM9ATS31PHl-w1GczSCSldRTQelPK5QTAvsdRLXAT1rp2_Ifeemlgq9GHkytrqEtB4_8qu_hdnsp9U8q2cRUrs1okkHhpqnBmwY8BoZ9IUP1mxQZ9S70-shiukR08qSk4WzqKhGqhN4xx7JXWpTJYRmQ9_FVJWciAXStSG_FRMXScRYStTawtMrqFI1R2RnuOCVPcCriyyI_LY5W5THr5PWFQUE5Le4M2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vb_3r6FXH4Cc2UySWD7Y-yAkYSYxdikj91iRE04GG-hXDF3ltZ_fhqLIy-HVT_-BJPhI2o5KEZzY5bfn49k91RXi0_R-s0nw_fLOHNycBqXh0stYlNg4kcoowLYXCwr-aXWjoTV4yd0bgBp3U4ezMjdW-IyDCIIv3AEaCFkkrAUjPe97CbU0UZGSG0WCuC_GWV5Ui5INiWzWOv_3DXTrDFYy3qw7oJ4tBpLMiuuM4DAmVZV-IDV7jJePxD9YANMI4s1EACGxvy5VWN0h9G_jToy-1sDcYoLtrE-iQWmAurnM6Gn3SHY6dTQkuF8QtTnkAmSlYT8URe9qUcrJJuKjMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MngyIi4eOaOWoqV5wASzWat6AwQhxQkcWsJC-TQxgFDlRQIILCzJTCofuYv50fRyCi7-Eh9bNRMCp5jH6jyh9U91NjMG0kt7uWx_qTp0rVPqaHGq-k8PeXze04r8waA6wgP4JSg_bw7q9xJ0YttukdF4ACimKI6l-YvtIZ-g-0iBN-RPwVOFiG8sB5aywqVCDn6ePazRYdAklQsNtEa16lRj0fla-Nx-i3VwayZpj81dNWai7mScMSoccE0WvsvDb9O_xLs6FzpI--l1gvwNCV6EAbjcv4liGiABJ_YN4K1ALWpXsSPEurUnbWDXqqm6Y17aoSJcdPHGUedu0DPD7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OQzkmIrP1uVsSlIDHlq3gqdzqNIpvYtvmLoT7zk-8_Z-z8RkpA6hJ2T2lPVANG7PBLIqTN-F3yz_xVm7NF-wW8raigHy6NA5tpSxSrPXdeRwK8dq9Uee2_RfkqJFTHUhzSGOlSrTlNh6YO_pYlqTunlBDltNhmUNJFupuQT9DGNbyc_bgKhbBSAV1cMEwwIDwc4WyHGWtYmBK-VpjxhItmfxtPGhpv3KWpAtwjVXzNNHmC1bggtVizCPYSNDRn_3RnbHOPhY0Doex8dQaRgfRztwY-vaIjFVAZpxxxQIwY8QszcXMQpUvnZtTotSlgEM092WYV-_U8lKQF-P2AYNCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از بین‌الحرمین در شب نخست ماه محرم
@Farsna</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/442641" target="_blank">📅 21:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442640">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f88826f8d.mp4?token=Bp6AYSddzuXWo1rXjGvh1BYaWkTP8aPvES_zPDaxcjqYO1vgiosd1oCWfxzJSotwtB7wemh7mamklG6en8ygrozC7ubR_fcLVauciNpkb0v9ceBRMBBGVfgQkClgp4HaCdU_nmS7uK2nHRMy3bvedf6Rz__58CSH62mSKrwkM87oC7w-rqJbTWJFPHEPDy-O8RyzfbNLmVCHtK-Ay8tW6nZ6lW_ouNmyCKyP1JVxFkMuvNIL2EaT8TtkNuLQZUwDu4XxA4sN6viMVWS1snIn4obgltYNL5wBZKhn8qScDcz_eEcY8EhsbeYsU2CnPka3qLAHOHzHGN7HICQrXzqcYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f88826f8d.mp4?token=Bp6AYSddzuXWo1rXjGvh1BYaWkTP8aPvES_zPDaxcjqYO1vgiosd1oCWfxzJSotwtB7wemh7mamklG6en8ygrozC7ubR_fcLVauciNpkb0v9ceBRMBBGVfgQkClgp4HaCdU_nmS7uK2nHRMy3bvedf6Rz__58CSH62mSKrwkM87oC7w-rqJbTWJFPHEPDy-O8RyzfbNLmVCHtK-Ay8tW6nZ6lW_ouNmyCKyP1JVxFkMuvNIL2EaT8TtkNuLQZUwDu4XxA4sN6viMVWS1snIn4obgltYNL5wBZKhn8qScDcz_eEcY8EhsbeYsU2CnPka3qLAHOHzHGN7HICQrXzqcYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مهم‌ترین درس کربلا برای امروز ایران چیست؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/442640" target="_blank">📅 21:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442639">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b0a521673.mp4?token=WCoHP40ZZBKSHs08qJPAWutr-3iu6j4VjG07gdWkTz6TbZNE0AiTrbuAAyMGtnTH97nKBNtuKDFSj-m4CbWZ4QYK6Qvb0kOifRzDURUqupLcR1ddK_-5o_agtte5KHZQTfsRNxcvCwD8OoGS5NsDaeRV-XY3_vd19ZnqeNKHx2wD28M41FoUX3JSh2Wwpdz19jQ5fQ0rRWyM5vawouUuMLW4MBABD8qzLwxSGVlnTwZ5v18r64ZR70wSO49Ej4GCBv0DrgJ1HpIH3wr4M7NTaATnzgoz9QSRi5ketXqpYVjji33uWVKEHOlW5M6HfJ3QI6bLTe3IrZrcQYU-EKgWdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b0a521673.mp4?token=WCoHP40ZZBKSHs08qJPAWutr-3iu6j4VjG07gdWkTz6TbZNE0AiTrbuAAyMGtnTH97nKBNtuKDFSj-m4CbWZ4QYK6Qvb0kOifRzDURUqupLcR1ddK_-5o_agtte5KHZQTfsRNxcvCwD8OoGS5NsDaeRV-XY3_vd19ZnqeNKHx2wD28M41FoUX3JSh2Wwpdz19jQ5fQ0rRWyM5vawouUuMLW4MBABD8qzLwxSGVlnTwZ5v18r64ZR70wSO49Ej4GCBv0DrgJ1HpIH3wr4M7NTaATnzgoz9QSRi5ketXqpYVjji33uWVKEHOlW5M6HfJ3QI6bLTe3IrZrcQYU-EKgWdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر آموزش‌‌وپرورش: از امسال لباس فرم مدارس ۳ ساله است
🔹
حتما چارچوب لباس فرم مدارس را تغییر می‌دهیم. نباید خانواده‌ها را مجبور کنند که هرسال یک لباس فرم از یک مغازه خاص بگیرند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/442639" target="_blank">📅 21:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442638">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fd0a85716.mp4?token=dIxLF9QPNIayvRthMb2VwUfsGnU4BDq10OuAkWQVJHBGGUHgMAe7T4h6H3xcHhG5_qtbeZlPjmzlj9W0cqqEfU79aTj0eKQbMuW14z8NRq10t6GqyTMvRQpRnSq0s0wGqi8WYH60yGb926hd40BwC9bFBeVHFZyOAX-1YDCVt7ARVzP4VselHr2ajbk-PL77kQjU2vc7-foHgtJj3HIHaZaZAZEDJyDpDSW6rJJ1EvDS5Fx1y9rpPy4fILG2uwrVpdr-ASVDfLSphOBKbc-lYs_RFIr61hq2K6lEA_yiCBpFfvnRCNeFLu4QyFDNHAQV_XMtt6gKq7gMz01Vyg1W-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fd0a85716.mp4?token=dIxLF9QPNIayvRthMb2VwUfsGnU4BDq10OuAkWQVJHBGGUHgMAe7T4h6H3xcHhG5_qtbeZlPjmzlj9W0cqqEfU79aTj0eKQbMuW14z8NRq10t6GqyTMvRQpRnSq0s0wGqi8WYH60yGb926hd40BwC9bFBeVHFZyOAX-1YDCVt7ARVzP4VselHr2ajbk-PL77kQjU2vc7-foHgtJj3HIHaZaZAZEDJyDpDSW6rJJ1EvDS5Fx1y9rpPy4fILG2uwrVpdr-ASVDfLSphOBKbc-lYs_RFIr61hq2K6lEA_yiCBpFfvnRCNeFLu4QyFDNHAQV_XMtt6gKq7gMz01Vyg1W-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توافق ایران و آمریکا به روایت کنشگران خارجی
🔹
اعتراف به شکست آمریکا در میدان نظامی و دیپلماسی
@Farsna</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/farsna/442638" target="_blank">📅 21:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442637">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtCOuRetcizoHrUiwGPdfBzSwOWr5a8MHrHzln3L6UFEfsIvtfuI_prOt0buWWUF4w0qzx26k4e-WX0SEPUyj8ZPA82Rie-fKqwJA5bJke7dASuymRS0zwggnjXHBf582INLCUgBWH4AQtzzbCKGJe8e17cBUNrRv9NGseuFMJaeRyIVrgyJorD6_U7YhODMjCO_S0-_Nyk7z5KxUVezEL0y32EYuEs0vGcMgKBwEZ6YKdP5VK464eELTTb1Ws19I8jzhUE43aou75I5XP6IEopmrIVWz3FFuEz8o9uydFhBkGSlN5IuR-VMxBx859A80mAmhnUayFPapv5jpwmT-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد بخش خصوصی: نان مردم را به ما واگذار کنید
🔹
رئیس بنیاد ملی گندم‌کاران به دولت پیشنهاد کرده موضوع خرید تضمینی گندم را به بخش خصوصی واگذار کند تا از هزینه ۵۰۰ هزار میلیاردی هرسال خلاص شود.
🔹
امسال با گذشت ۳ ماه از آغاز خرید گندم، دولت ۱۲۵ هزار میلیارد تومان به گندم‌کاران بدهکار است. در حالی که کشاورز برای کشت بعدی نیاز به پول دارد.
🔹
دراین‌باره برخی کارشناسان معتقدند خرید گندم باید همچنان توسط دولت ادامه پیدا کند؛ مرادزاده، کارشناس بازرگانی می‌گوید ورود بخش خصوصی تضمین تامین نان را کمرنگ خواهد کرد.
🔹
در مقابل لطفی، کارشناس دیگری در این حوزه می‌گوید: وقتی دولت به تعهدات مالی عمل نمی‌کند، انگیزه کشاورزان برای کشت سال بعد کاهش می‌یابد و محصول به جای سیلوی دولتی به بازارهای دلالی هدایت می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/442637" target="_blank">📅 21:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442636">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">سی‌ان‌ان: ایران درصورت شکست مذاکرات با بستن هم‌زمان تنگه هرمز و باب‌المندب اقتصاد جهان را منفجر می‌کند
🔹
این رسانۀ آمریکایی نوشته: ایران از این پس می‌تواند تنگه هرمز را به دلخواه خود ببندد؛ این یعنی رژیم ایران پس‌از این جنگ توانایی همیشگی برای آسیب‌رساندن به اقتصاد جهانی به‌دست آورده است.
یک منبع آگاه به سی‌ان‌ان گفته ما اکنون تنگه هرمز را عملا به ایران واگذار کرده‌ایم و این سلاحی قدرتمندتر از هر سلاح هسته‌ای است.
🔹
منابع متعددی به سی‌ان‌ان گفته‌اند که درصورت شکست مذاکرات، ایران از طریق حوثی‌ها اقدام به بستن تنگه باب‌المندب می کند؛ بستن باب‌المندب، همراه با تنگه هرمز، اقتصاد جهانی را کاملاً منفجر خواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/442636" target="_blank">📅 21:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442635">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🎥
آغاز مراسم تعویض پرچم حرم‌های مطهر امام حسین و حضرت ابوالفضل علیهما السلام به مناسبت آغاز ماه محرم الحرام  @FarsNewsInt</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/442635" target="_blank">📅 21:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442634">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58693fe30f.mp4?token=nGJVwR4Erpc5DLoIqa3_KfEXW7n1bWxSYlPwQXggAon8QOx_vANaAimoBWRH5p9nTedoQPxxs78LE2CN_W4KuCTU7kAYW5ByLX4aPE5AjgCwQEbOsKDfYULiYltpDkqBLyOl-7sPA1R9xxGMCPpDad19DTVFWLK9PyiyDGqZkYh-lA9ufeLnQx9L4BSqQPT-96UaHq9FqkcQZVyBSZMjvKLNPIChknJrxPnB5VJio8BLI6kvYt1l5jZhvU9qPmh13OraV2azPDpJzsEHyClQX-gljFgCTQZUaUyc118k2RwxyeW_1Ne7JIAJSMSNj_Sy-haaXrJCuS3XwRPzayLwHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58693fe30f.mp4?token=nGJVwR4Erpc5DLoIqa3_KfEXW7n1bWxSYlPwQXggAon8QOx_vANaAimoBWRH5p9nTedoQPxxs78LE2CN_W4KuCTU7kAYW5ByLX4aPE5AjgCwQEbOsKDfYULiYltpDkqBLyOl-7sPA1R9xxGMCPpDad19DTVFWLK9PyiyDGqZkYh-lA9ufeLnQx9L4BSqQPT-96UaHq9FqkcQZVyBSZMjvKLNPIChknJrxPnB5VJio8BLI6kvYt1l5jZhvU9qPmh13OraV2azPDpJzsEHyClQX-gljFgCTQZUaUyc118k2RwxyeW_1Ne7JIAJSMSNj_Sy-haaXrJCuS3XwRPzayLwHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
راه‌حل وزیر بهداشت برای گرانی داروها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farsna/442634" target="_blank">📅 21:21 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442632">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efd206c8ee.mp4?token=j6uoVv857FfG43J_aM_yFYiXO77-98xhZGPN4RIr0VGWz9JsaCUnl6LyL1Dos1VD3qIn4OGMegGcHdsZxOKJMx1sWDVfYlYqHwywQzsMga9YKCrE1aLa63UuH5mZOEYVxn66nzMR_skftLSTLuUi1sBkoxkQNreY583US36QH0Dl4grqinU7uPUSSUiWwG-HeJWE9MTXIe396L9ADKrTSMeG2p1GApYEFAiji0EqMRucAUz7koCHP-O6P3L6dvq10ILev3U-R_UKD5ZZ6ejBZIMcrRkiVWHdqLAHdJpSfmEaPhS9Ovn0hQq6Aj02kCOEY02jgnADCR0G7_t93TFgGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efd206c8ee.mp4?token=j6uoVv857FfG43J_aM_yFYiXO77-98xhZGPN4RIr0VGWz9JsaCUnl6LyL1Dos1VD3qIn4OGMegGcHdsZxOKJMx1sWDVfYlYqHwywQzsMga9YKCrE1aLa63UuH5mZOEYVxn66nzMR_skftLSTLuUi1sBkoxkQNreY583US36QH0Dl4grqinU7uPUSSUiWwG-HeJWE9MTXIe396L9ADKrTSMeG2p1GApYEFAiji0EqMRucAUz7koCHP-O6P3L6dvq10ILev3U-R_UKD5ZZ6ejBZIMcrRkiVWHdqLAHdJpSfmEaPhS9Ovn0hQq6Aj02kCOEY02jgnADCR0G7_t93TFgGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز مراسم تعویض پرچم حرم‌های مطهر امام حسین و حضرت ابوالفضل علیهما السلام به مناسبت آغاز ماه محرم الحرام
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/442632" target="_blank">📅 21:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442631">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dp8y_1TDVvpluHMcE1yPaCEB61gRcY4QVzqHtM1HK4Vq7St-_gX9Sbsa224_RiprIUngYrbbMzWJmLHPVeYQzK-VGZDjLiW-QCxWkOoJp-tADa8Txp49sLFbR5j4RUbQQOrgcovxj67oFunGU6BoJG3jTldt-X8mnqTUUAvKs9wr8anLIieRgT5d4KN82ESq0pUJ2v8_6mUbd821WVJ-4YdjLyqNUSsCI01Rgx8RYMsEuCoLDIQ3-cDMnCkAEld12wWRkiBswX-oEBEuuUQLA0L32fZT6TAaUyWSh2bKrK7HIAJN2tMQhjVFzUOp23JqPpdksy9evh0sAWKle23DyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه شماره ۴ ستاد بزرگداشت عروج خونین امام مجاهد شهید حضرت آیت‌الله‌العظمی خامنه‌ای‌ قدّس‌الله‌نفسه‌الزکیه
بسم الله الرّحمن الرّحیم
السلام علیک یا ثارالله وابن ثاره
◾️
همزمان با حلول ماه محرم، ماه پیروزی خون بر شمشیر و ایام عزای سرور و سالار آزادگان عالم حضرت سیدالشهدا علیه‌السلام و اصحاب باوفای ایشان و در آستانه برگزاری مراسم وداع، تشییع و تدفین امام مجاهد شهید حضرت آیت‌الله‌العظمی سیّدعلی حسینی خامنه‌ای (قدّس‌الله‌نفسه‌الزکیه) و شهدای خانواده رهبر انقلاب اسلامی، جهت‌گیری محتوایی و رویکردهای تبلیغی و ترویجی این رویداد را به‌ استحضار ملت شریف ایران و دوستداران آن یگانه‌ی دوران در داخل و خارج از کشور می‌رساند.
◾️
حضرت آیت‌الله سیدمجتبی خامنه‌ای رهبر معظم‌ انقلاب اسلامی(مدظله‌العالی) در اولین پیام، درباره‌ی رهبر شهیدمان فرمودند: «من این توفیق را داشتم که پیکر ایشان را بعد از شهادت زیارت کنم؛ آنچه دیدم کوهی از صلابت بود؛ و شنیدم که مشت دست سالمش را گره کرده بود...»
◾️
این
«مشت گره‌کرده»
که نشان رسمی بدرقه‌ی آن یگانه می‌باشد، فقط یک نماد نیست؛ تبلور همان دست مهربان پدر امت است که بارها در برابر استکبار جهانی ایستاد و هرگز نلرزید و جز برای خدا گشوده نشد.
◾️
از دل همین مشت گره‌‌کرده و از جوشش خون مقتدر مظلومی چون اوست که دل‌های آزادگان جهان به تلاطم درآمده و ملت ایران بعثتی دوباره یافته ‌است. بعثتی که باید تداوم آن را در اعتلای پرچم جبهه‌ی حق در جهان، انتقام خون پاک امام مجاهد شهیدمان و ساختن فردایی قوی‌تر برای ایران اسلامی دنبال کرد. حضرت آقا اعلی‌الله‌مقامه‌الشریف در یک جنگ خونین به شهادت رسیدند. شهادتی که در میان علمای امامیه رضوان‌الله‌علیهم برای شخصیتی در حد و شأن ایشان در جنگ اتفاق نیافتاده است.
◾️
در امتداد جوشش این خون مقدس که زمین و زمان را به تلاطم درآورد، شعار محوری این مراسم این خواهد بود:
«باید برخاست»
◾️
این شعار، امتداد همان «قیام لله» است که در طلیعه چهاردهم خرداد امسال از سوی رهبر عزیزمان (ادام‌الله‌ظله)، زیربنای مکتب خمینی کبیر و خامنه‌ای عزیز خوانده شد؛ قیامی که از نیمه‌خرداد ۴۲ آغاز شد، در بهمن ۵۷ به ثمر نشست، در عصر مقاومت استمرار یافت و اینک با شهادت مظلومانه آن عبد صالح خدا، نصابی تازه یافته است.
◾️
«باید برخاست» یعنی این خون چنان جوشان است که دیگر اجازه‌ی سکون به هیچ دلداده‌ای نخواهد داد.
◾️
«باید برخاست» یعنی عهدی که ملت بعثت‌یافته با خون او بسته است، تا پای جان ادامه خواهد یافت.
◾️
برای این مراسم که
«بدرقه آقای شهید ایران»
نام گرفته است، بسته هویت بصری درنظرگرفته شده تا مبنای تولید و انتشار تمامی آثار رسانه‌ای، اقلام تبلیغی، فضاسازی شهری و مردمی، محصولات فرهنگی و برنامه‌های مرتبط باشد.
◾️
اما این عزا، تنها مختص مردم ایران نیست. از کشورهای جبهه مقاومت تا اقصی‌نقاط دنیا، آزادگان و آزادی‌خواهان جهان داغدار این شهادت عظیم شده‌اند. امت اسلامی با الهام از همان مکتب، کلام الهی
«قوموا لله»
را سر می‌دهد. این شعار، عصاره آخرین رهنمودها و پیام‌های حکیمانه امام شهیدمان است؛
«قوموا لله»
نه فقط توصیه او، که تجدید بیعتی است با مکتبش. اعلامی به جهانیان که آن عظمت، آن ایمان و آن شجاعت بی‌بدیل با قدرت و صلابت بیشتر ادامه خواهد یافت.
◾️
به توفیق الهی و عنایت خاصه حضرت ولی‌عصر (عجل‌الله‌تعالی‌فرجه‌الشریف) این بدرقه، طلیعه فتح مبین و نقطه عطف بعثت ملت ایران و امت اسلامی برای افق‌های روشن پیش‌رو به پرچمداری رهبر عالی‌قدر انقلاب (مدظله‌العالی) خواهد بود ان شاءالله.
دفتر حفظ و نشر آثار رهبر شهید انقلاب اسلامی
۲۶ خرداد ۱۴۰۵ مصادف با اول محرم‌الحرام ۱۴۴۸
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/442631" target="_blank">📅 21:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442630">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">رهبر انصارالله: به رهبری و ملت جمهوری اسلامی ایران، برای پیروزی بزرگشان در برابر طاغوت مستکبر زمان یعنی آمریکا و اسرائیل، تبریک و تهنیت می‌گوییم
🔹
ما همیشه آمادهٔ مقابله با هرگونه تنش‌آفرینی یا تغییر اوضاع از سوی دشمن آمریکایی و اسرائیلی هستیم.
🔹
این آمادگی شامل هر سناریویی است؛ چه زمانی که کل منطقه را هدف قرار دهند، چه وقتی که بخواهند غزه را دوباره هدف بگیرند، و چه زمانی که به هر بخش دیگری از محور مقاومت و کشورها و ملت‌های اسلامی دست‌اندازی کنند.
@Farsna</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/442630" target="_blank">📅 21:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442629">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ef5de62c7.mp4?token=v2pkv4SSVFVmUOpRXnd12VRIpnycmRBhU6J3GEIDilWTVQGdSbXiypcNGZ4d1Lxq86_HZg6WDUC9-P6qnCFsym-Ao595S3EJsQZWWl5DOJx_OFfNX8zplBuC8VgkzEuIEaN1GWzstj1C-nCQYzv1Mzchye3X0GEq4Y7lOlqGx2EoVlN2KaJBr3nreTcGhHovsyHA2LOdbVE_0hwsv1dT2hH2iPK9PMaTSDTbHs_9AHVizld-qQ9Dfs5aUIsjIADKgGSozjqNNsuTLx4eWT9wLM8Yt7e-FZDAUp_LZbwgtANN5BypKIkV3LkClgObchTmvy5VtQ4_3OF_72uV2jRqSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ef5de62c7.mp4?token=v2pkv4SSVFVmUOpRXnd12VRIpnycmRBhU6J3GEIDilWTVQGdSbXiypcNGZ4d1Lxq86_HZg6WDUC9-P6qnCFsym-Ao595S3EJsQZWWl5DOJx_OFfNX8zplBuC8VgkzEuIEaN1GWzstj1C-nCQYzv1Mzchye3X0GEq4Y7lOlqGx2EoVlN2KaJBr3nreTcGhHovsyHA2LOdbVE_0hwsv1dT2hH2iPK9PMaTSDTbHs_9AHVizld-qQ9Dfs5aUIsjIADKgGSozjqNNsuTLx4eWT9wLM8Yt7e-FZDAUp_LZbwgtANN5BypKIkV3LkClgObchTmvy5VtQ4_3OF_72uV2jRqSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرکل خودرویی وزارت صمت: از امسال به خودروهای مونتاژی با ارزبری بالا و ساخت داخل پایین، مجوز تولید نمی‌دهیم.
@Farsna</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/farsna/442629" target="_blank">📅 20:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442627">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60722f8d84.mp4?token=CcpycI6vZghO5jq4MmZE4Gg6aN2s2Sy-seq4VJ209qlKl8wssCY-OmVEbAWg3njzRznHZr3538FLCkFl_FezyWBddDkuzOBlYnp04R1RM4VnIMdtKoWmbPVOZIRR15muAkT2atJ82GzltXXmBEWNMVhqxC-4JdBcJYI8Gs02PBNhpw9-0QyZGcahgxtMx8p699tDFgK0KpczkgPv0tXF-64OggzDDcqyMGChk9wIxkdks43neYMdsf9PGKhkvLu9ZZsmIBlihy7VAntlA58ouI7TiM2BEFeoCP3SEfXD7qgVT14r6LYORpqLBD37I82gTpMbMRTzKQU1Py549CJ8mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60722f8d84.mp4?token=CcpycI6vZghO5jq4MmZE4Gg6aN2s2Sy-seq4VJ209qlKl8wssCY-OmVEbAWg3njzRznHZr3538FLCkFl_FezyWBddDkuzOBlYnp04R1RM4VnIMdtKoWmbPVOZIRR15muAkT2atJ82GzltXXmBEWNMVhqxC-4JdBcJYI8Gs02PBNhpw9-0QyZGcahgxtMx8p699tDFgK0KpczkgPv0tXF-64OggzDDcqyMGChk9wIxkdks43neYMdsf9PGKhkvLu9ZZsmIBlihy7VAntlA58ouI7TiM2BEFeoCP3SEfXD7qgVT14r6LYORpqLBD37I82gTpMbMRTzKQU1Py549CJ8mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شکار یک خودروی نظامی رژیم‌ صهیونسیتی توسط حزب‌الله در جنوب لبنان
@Farsna</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farsna/442627" target="_blank">📅 20:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442626">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TaJ45AfaYTobmVOWggcO2P9Nk1FrFAk9kpGGoF6bYbpKQzrEuAcXWEzcr5_LAPBRAm8zwcKRSkenoFLTYdtO1L4nlRmThC5k80agoKnZuOlVxvI2J1eYMiKqnEXf7GSV8SwG9rSh9DNTdvk2ZPYLEMQWbCTfIcGxSR2f8QM7G2Lcgl_NuSLpRH_q-JjtfnQCC22EeHGXxCCNOx2IStSKxCHuKPUEngyDGRYhm_5CWfA2BfbZv51LmWZkCqv2lXG-bSYDkljEoCrbXhGkUdWWWNyub250kSxWF05U-u1YJ0ZYIXaqXodgyCSGwwiREk2cgOISjUymyNNO8Swk8fUPkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین دیدگاه‌های موافقان و مخالفان مفاد تفاهم‌نامه و مذاکرات با آمریکا را در فارس تعاملی بخوانید
تازه‌ترین مطالب و یادداشت‌های:
🔸
محمدجواد لاریجانی
🔸
آیت‌الله میرباقری
🔸
سعیدرضا عاملی
🔸
یدالله جوانی
🔸
حسین شریعتمداری
و...
را می‌توانید در صفحۀ اختصاصی هر یک از این افراد در فارس مطالعه کنید.
@Farsna</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/442626" target="_blank">📅 20:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442624">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">📌
مهارت‌آموزی هیجان‌انگیز/ چرا اتوبوس‌های خلاقیت، میهمان مدارس پایتخت می‌شوند؟
معاون شهردار تهران:
🔺
دانش‌آموزان در کنار آموزش‌های تئوری، با لابراتورهای سیار شهرداری، مهارت‌های ساخت محصول را یاد می‌گیرند.
@Farsna</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/farsna/442624" target="_blank">📅 20:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442623">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CoBFqLdQv-kvxcDLUiVeqa5hZPCAdAbs6GNL_BEOvqZLeNoc5Pz07csERZX3pO8n8WW2F8JaD9hrnDPxuNbCJcpsO-ybdPig3MmSjHrkEm1QnkqjUFIPMJ6HIxWxZEpv0jcmja5qny01tca6jHkRBYT5U1vcVfA9fPyHYY5agj5ikKoRNHgAHNvOO2eS-5AQzDr90ZmMVRoPALUMtpjMMNt39hPIpr6BeMUx1OYuc40W_VlNebdxeaBTbl1Fxx3pjtiti0XqmblB-seARc7ueieIF5pUnEPOMnOdaFMv6_miqAN5p3L4juvj4U0wMgBsJkrh5BdPwkt3X-Bzi2harg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
فهرست برندگان ۲۵ خرداد ماه طرح «فرالیگ» بانک رفاه کارگران اعلام شد
🔹️
همزمان با برگزاری رقابت‌های جام جهانی فوتبال ۲۰۲۶، فهرست برندگان روز دوشنبه ۲۵ خردادماه طرح «فرالیگ» بانک رفاه کارگران اعلام شد.
🔹️
در چارچوب طرح «فرالیگ» و همزمان با مسابقات جام جهانی فوتبال ۲۰۲۶، در پایان هر روز ۶۶ نفر از شرکت‌کنندگان بر اساس امتیازات کسب‌شده و از طریق قرعه‌کشی، به عنوان برندگان جوایز روزانه معرفی می‌شوند.
🔹️
طرح «فرالیگ» همچنان ادامه دارد و مشتریان بانک رفاه کارگران می‌توانند با مراجعه به سامانه «فرارفاه»، تا پایان رقابت‌های جام جهانی ۲۰۲۶، نتایج مسابقات را پیش از آغاز هر بازی پیش‌بینی و ثبت کنند و شانس خود را برای کسب جوایز روزانه و همچنین جوایز ویژه پایان دوره افزایش دهند.
🔗
فهرست برندگان
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/442623" target="_blank">📅 20:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442622">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/farsna/442622" target="_blank">📅 20:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442615">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q2T1gYI1qhRM54VC-Yb0p-fWFI3nICaFvirhaVzw8xY0MRVMBURc9liDz2mLh-eHWVg_GVdvftIOhvQJYQhJB9ARaWZMaZk5k2x04HqfKrqGC-Eoa-_La__ZsBOGdwewmjk3Op9rE-_5K35Ad7yuWvffV2BFmJ6sUnjVJVt6B41RA46K-tw19P7Lh5pBzu8rhHPSEub0yeKuwwflTr8Cri4I4B5yI9RheJvfZGnor5Lg48ZRz9PEBtpRsJJRhgjqfYfhygPeLryi8Z_wVLw00cKPoqcP2PhgSUm2gC2YRrmmmO14OMRKdUvUFNcxEYSKPEaE_akjVQ0hAF6qyfg61Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kv4EMwJ1dE_swzAxZU5_DTiUr-ZyBvIpMaT59ST3oITp5qYapkDjGjG27SNgtL2e0d7wvumafdTYVtQ3HtZghHbFfhojY-lAWiZZefXUuHCsCYSj173QzP_1_8Vb6kuv7yl1_jwk_apYinw9t-Xl8mirMnmIw3PqftmK7sf0qX_qKCVwCO9XWusiWcnt454L3NE-r1D2HGotJfmuAUEmhKSF9W2KrQR-ggnT9epIU8s-C4qnOdwwy5HEo87OLu9FeMwRNO5Zr8pDhls62NMyxBewRiPygwfU2xkkwkObuMUPQyGP-8fcViH7mzkobCIYuQ4nZLXSU01hTx0SNTAcTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gZgQOfw4YQ2UXe7FcHah8mXiK7KOLJ1wWMbH7W3UZiT7JlOppSA2zdCWcMapWFv6QHZcenrWi64oDyD5KTG50iTMADC8NEsV6Ny0GSP9hKYQlHxuWA2a2aqMstQYbGXVhgfL4h0GeSC-FDuT3L8sidOKIauGs3b77gvdUHhkcEwZr335dSRYYrnP3fWoUkWQ7_4ULk4JoZzTJkkg26yLxq0o-LnZXOOmGlpHnKGWdqG0alE2G03yx1A7e5jbXVzUDo80gvvgkoa_v4uYnmWGFJUrQFvCPgBIAn_Mei_iL1DdJe9Z9zQG1QTpY4LhLnMzBqr-_mFolCl-HJrx8V4b_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s3GqiyfYZkb-QWmhyeUiV8dzdLVBqnALG5WW_PlUcYHsjRPySrp7J4tgM7ogswAp8QvCPy97LrV-3wx1nio1PEOXctsfsc4Gr6Ma_6wfAi7v083t7DtoEtaTuP3XpSG2jrBVmO3IL-8ArDziXTExsaGzT4OoFgMV8TQZKNlL0K3C8A8yomfb3sB_0NB1iN8m-ZB2dch7LnUBVLgBMk3kWEjUi_iYtsIGDPhqu1QKl54V6umEG-VHe4feZ9tNaIO-VVnCXACMgXsxsX985f5P5Mt42gasetM2xxE7HkpZY2q6fdPdAL-jInr76BVqJ6n72wuG6y9vG3g-IaHCHG9lWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n-x4H5IfPhXZWNX4z6ti-6IKiNka6neCCTQo9q23_iTBdtYXgXJn2M9DaSJ8mBzb4gHtytPX34WV5gt0eFGzdYjN-YfYx8d35Pd5UGryU0K-9o2kYLsdBP4FaynsQ38CBOpvjFqnHiX5KxuT9GmdK0n-8Idq76hwXDn8ObDLQvu6anpSAVxJ87t1-stYlzWesguwppRPQOapl0iIVsVHbZjnkP2HXe6DdkvzXOZuvKe5xNp4dc624qUfwmfk1Pd-cSOXNpPVMnOhutnhvNlXn490nceZwUY4d4WGb0o8VTGZxiH1r6IGD0d0x4TG6voxhan8DHFhYvs-80LyqgTwDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RHeFlJ4NyiggXCrBkhTIVwVS2JBKlaAbYVNcCVWL1n7kcn2ZGNqpbwWs4oSiZadYc2zNdiX2uheSpR6MlNVNf6PHZpE1w9ONL2khiUy1-Vi9Ut9JXHK_c_5EFkx8VIyuClBeLnUhHOlFwc_gXvvVoi466daBcmewNJqozmVzKkHNJPyGS24SIPGVudXThF_gdyzsfdoLD28xy1TN_IaQDLo2KN91nuWUyq1xLASqff3cXf-jpKbzZPTm4sjyQTMvMOWJpk6WX1vaLx2jwMDBp9y4yNP6Fa2fwvPdh5eqTPTB_S2Yw36_-m4cvBXIaZDV5IaxNUlf2i_t2JWT8cmTeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hlzhS0JQTOJwoVmKXf4Cdxaj2LUXEOpjxmeGW445xbGLKKhangeyFDzVNvE9i18ffKM4_B4-fnU_qgE8RL2mzfn2fF4r-TemFkaKhHwgbBLrIHtiqKOKhO2gfuYgiYYVh7ibkiQThs_0Iea4FE_wIgU8BqxQgwPb1DffcHfC9PH9alsw6qYSu_8zud3TdWQUp5kCCTeQEgyIqpuUgOTVwCpqXVl0Vzu1S7P5iISX8NvTb-z5qFLedB4r9pKoKjS2ha2KA8Wy_wpaXxSfXOI0qT13uPDbHNFGU1SAOMNm-CScDV_a3s3u-G4rEMjRhaz1-KDQYXJyiSNDrmhFBEBhBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تمرین پرسپولیس زیر نظر اوسمار ویرا
عکس:
صادق نیک گستر
@Farsna</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/442615" target="_blank">📅 20:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442614">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZyS0prJ8_Q3bcuYzN1Lm0gj3fUUVZl-sJTJP4cTbmr31hiwUe5B4NmySILVBpJ16Z5-5m4Exng7o_ceTQu0MMUCvLcMgxPMsq_YlxnuAKMc6RGr4uhIStJUASiJgXVwxnRNzeDKoS8TcGPmHVIyZSqxXiNEw9qGFAZk6fGQYwl1RyXCfpJPAPsipEZH54cXvDBklmWRZm0yDYJFng_ZVA3gPccHq-DRAUXhSkR2g3FzlXSEN8m2NYCl2kFnIiDnC4rtRe9CoxLjkp5Dshk7tPOnw9g9ToTC4XR9WxxkF01lkAqE_XrsirocnjsWZ4sFUbLRDHoJ_do85Y7IvPaFCAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هریس: ترامپ دوباره ما را به نقطۀ پسابرجام برمی‌گرداند
🔹
رقیب ترامپ در انتخابات ۲۰۲۴: ترامپ هر مذاکره‌ای را یک پیروزی جلوه می‌دهد، اما در نهایت آمریکا به همان شرایطی بازمی‌گردد که پس از برجام وجود داشت؛ توافقی که خود ترامپ از آن خارج شد.
🔹
تفاهم حاصل‌شده صرفاً «مفهومی از یک توافق» است و هنوز مشخص نیست در روزهای آینده روند مذاکرات به چه سمتی پیش خواهد رفت.
🔹
اگر رئیس‌جمهور بودم، هرگز وارد جنگ با ایران نمی‌شدم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/farsna/442614" target="_blank">📅 20:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442613">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e815bcdbf7.mp4?token=QHy76N0Qqg7zJBNiJery96NTIcRDjAjvUFT4Sw5tc96gILtK1STeDz2fy-og-QIgJyy0n5BWBmfaJqWYsC54FRzDPpXXWE1WCqThcabFPz0DPZqUhA1kka1_-5Ic9XVcjdt-UmO_LHrk5cjDC23ViEel9xLUxp0A8R33pUqeMb7R4HYusq25YiaDpPrW7Vfm69o4Aot86D4-F-99Bl6bivSV3qyxXHEWIot96Tr3g5oj_ttxssOqWo4fobvh3QJGVwwOiCCda8RfrwvSrJM18PAGIF27palFQoVMpDK8C_1d4trZaH53BR3h-MD0l6xr9O2eLhlTtJlKQBgt6feSBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e815bcdbf7.mp4?token=QHy76N0Qqg7zJBNiJery96NTIcRDjAjvUFT4Sw5tc96gILtK1STeDz2fy-og-QIgJyy0n5BWBmfaJqWYsC54FRzDPpXXWE1WCqThcabFPz0DPZqUhA1kka1_-5Ic9XVcjdt-UmO_LHrk5cjDC23ViEel9xLUxp0A8R33pUqeMb7R4HYusq25YiaDpPrW7Vfm69o4Aot86D4-F-99Bl6bivSV3qyxXHEWIot96Tr3g5oj_ttxssOqWo4fobvh3QJGVwwOiCCda8RfrwvSrJM18PAGIF27palFQoVMpDK8C_1d4trZaH53BR3h-MD0l6xr9O2eLhlTtJlKQBgt6feSBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رامین رضائیان به خبرنگار خارجی: مسائل داخلی ما به شما ربطی ندارد.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/442613" target="_blank">📅 20:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442612">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ادعای وال‌استریت‌ژورنال دربارۀ معافیت‌های تحریمی نفت ایران
🔹
روزنامۀ وال‌استریت‌ژورنال مدعی شد تفاهم میان ایران و آمریکا این امکان را فراهم می‌کند که تهران بلافاصله پس از امضای توافق، صادرات نفت خود را از سر بگیرد.
🔹
به‌نوشتۀ این روزنامه، معافیت‌های تحریمی تنها به فروش نفت محدود نمی‌شود و حوزه‌هایی مانند خدمات بانکی، حمل‌ونقل و بیمه مرتبط با صادرات نفت ایران را نیز در بر می‌گیرد.
🔹
این گزارش درحالی منتشر شده که برخی تحلیلگران معتقدند دولت آمریکا ممکن است همانند تجربۀ اجرای برجام، با وجود اعلام کاهش تحریم‌ها، موانعی برای بهره‌مندی عملی ایران از مزایای توافق ایجاد کند.
@Farsna</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/farsna/442612" target="_blank">📅 19:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442610">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1db2a80a8a.mp4?token=hqy4VYyYBdtbzWpbpffEGca0Hxgi5mdFNacRmdVMbhbU8AscBJWgfKdHfcwhUjVueaTfeZOfPmz0MtaohXTq6NxdrVROItz6MQnC0hZnkJAh3cigWAky9odsaoERgXqXiSc9Vi7jhLQ_YJt3oNLZZ_SYlrnkaMtZSHBHlahzyAbySjUql4YIklos8bjBM1PRGONOZM7eeWTNrp2Fis8MtDrkdvp3k7DmQPMsJxwurQY58muSHZiU-TxdZ7r4ku8Q24XXhObZLhzInC4NW5QMG9Vw9jB-Mc_nwJyRjMswd9QPT4pXgT18pk2juAYsVsiHCV0PJJNzoyGoNGjgtiIyGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1db2a80a8a.mp4?token=hqy4VYyYBdtbzWpbpffEGca0Hxgi5mdFNacRmdVMbhbU8AscBJWgfKdHfcwhUjVueaTfeZOfPmz0MtaohXTq6NxdrVROItz6MQnC0hZnkJAh3cigWAky9odsaoERgXqXiSc9Vi7jhLQ_YJt3oNLZZ_SYlrnkaMtZSHBHlahzyAbySjUql4YIklos8bjBM1PRGONOZM7eeWTNrp2Fis8MtDrkdvp3k7DmQPMsJxwurQY58muSHZiU-TxdZ7r4ku8Q24XXhObZLhzInC4NW5QMG9Vw9jB-Mc_nwJyRjMswd9QPT4pXgT18pk2juAYsVsiHCV0PJJNzoyGoNGjgtiIyGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ابتکار شعام برای خنثی‌کردن بدعهدی آمریکا
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/442610" target="_blank">📅 19:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442609">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-xGUV5AEzZFFenbeJWCHVAbAs6iq9TbcmvZIv-EMW9bf17G2N7eKxLbNo7ZCBPCiWZSJ3FJQOjl7OshtOgw3ETlSNjFS5as-nM0OrzfdYanrymzO6PWXx7sNpGjhnJ-pX7mdZo37-KHc7s-mxs96IUoWzUEJ2wSi-M5FGSxScbTtu-CsREVL303dGvCkFyXv1XioOZ-AMNaWcdwVTTnsa1V6DfKPoNZjoet_kuN8ZjA_-dqYRZ6RjhCfD8NphaDF9LqwD_qubPrrFf2FW625TzcWjaZegDXCFm1cUiM1THZXyFlCXvD5ph3W36upYALw-hLiBUudTpMVpXysf8p_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای اف‌بی‌آی دربارۀ خنثی‌سازی طرح سوءقصد به ترامپ
🔹
اف‌بی‌آی مدعی شده طرحی برای حمله به رویداد یواف‌سی در کاخ سفید که ترامپ نیز در آن حضور داشت، خنثی شده است.
🔹
به ادعای مقام‌های آمریکایی، طراحان قصد داشتند با استفاده از پهپادهای حامل مواد منفجره به ساختمان‌های اطراف محل برگزاری حمله کنند و سپس افراد حاضر را به سمت محل استقرار یک تیم تک‌تیرانداز هدایت کنند. همچنین برای مرحلۀ بعدی، یورش به دروازۀ کاخ سفید نیز پیش‌بینی شده بود.
🔹
براساس گزارش‌ها، تاکنون ۵ نفر در ارتباط با این پرونده بازداشت شده‌اند و ۲۳ نفر دیگر نیز به‌عنوان اعضای احتمالی این شبکه تحت بررسی هستند.
@Farsna</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/442609" target="_blank">📅 19:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442608">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🎥
چرا مدل موی فوتبالیست‌ها عجیب‌وغریب شده است؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/farsna/442608" target="_blank">📅 19:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442606">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">خط-68.pdf</div>
  <div class="tg-doc-extra">2.7 MB</div>
</div>
<a href="https://t.me/farsna/442606" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۶۶.pdf</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/442606" target="_blank">📅 19:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442605">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KtFyL6DtdpEXRGjLIbwYoMitXW5iCM3r2L587FEpegQalJibWSjOdMHSLhvlRQRN_e78OVzkV6dnb6bzwmnHNkhdfPpGCO83tUkDO3us1oE5-v621psCK4ALLufnDl5t4bULcRK20_-LtMW2Xas1JAHSM8zfGXMI6ALgeSsGXdUOfFuIjiOhH0a652XJo9SGTs3CFeFlR6PCT26B3BfibrVpmSanytBxAV0DfidRDYOXyItfCgPnzMBUg_AclbZMTf13A3Y65ePesD-GKAbZdvo23e6ssTIOHJkg_nEbuvdVn-eyk0xKc6fy8UkAbwvIxff_A6__0VuQyH47XS2UcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابلاغ حذف تدریجی چک کاغذی به شبکه بانکی
کشور
🔹
با ابلاغ بانک مرکزی، بانک‌ها مکلف شدند نسبت به کاهش تعداد برگ دسته چک مشتریان حقیقی در ۴ مرحله و مشتریان حقوقی در ۲ مرحله با فاصله زمانی حداقل ۲ ماهه بین مراحل اقدام کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/442605" target="_blank">📅 19:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442604">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5adbba6886.mp4?token=CjiFp-cRerIMPy2cLcJRhWVDsvFd9OPLPI3h6rVbrkB-ZBqj1k4JUgCn7qfwX-CrFqKpgR0hXrxG2HOnSWNFfvH_61uqubbSF_DHSOVCpo4vTmNkgy4i3vfA1opalpJOXXElTF7oeGhiDh4DE0dFmG_vvkjeumX2E2dFmorrCT8t4rfHukQ1UDSmk7huubhOsAAvG9oEVWhs1_ytAXQ_1RQPDn_MAIRGhvA1KiULerctyCJ88_IET9O18AqB5bliYOFcACLdcCy2sob7AOmlr9x8ZlSpndLiNF2QS7jj1sP39flXt1DP3SCTurjFV1P1zylBSKOHF6_rXEBF30kF1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5adbba6886.mp4?token=CjiFp-cRerIMPy2cLcJRhWVDsvFd9OPLPI3h6rVbrkB-ZBqj1k4JUgCn7qfwX-CrFqKpgR0hXrxG2HOnSWNFfvH_61uqubbSF_DHSOVCpo4vTmNkgy4i3vfA1opalpJOXXElTF7oeGhiDh4DE0dFmG_vvkjeumX2E2dFmorrCT8t4rfHukQ1UDSmk7huubhOsAAvG9oEVWhs1_ytAXQ_1RQPDn_MAIRGhvA1KiULerctyCJ88_IET9O18AqB5bliYOFcACLdcCy2sob7AOmlr9x8ZlSpndLiNF2QS7jj1sP39flXt1DP3SCTurjFV1P1zylBSKOHF6_rXEBF30kF1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اگه برای چالش‌های تهران تو شرایط جنگی یه ایده یا راه‌حل فناورانه داری، این فرصت برای شماست
سازمان فناوری‌های نوین شهرداری تهران دنبال ایده‌ها و طرح‌های خلاقانه از سمت شرکت‌های فناور و دانش‌بنیانه تا بتونه تو شرایط جنگی، چالش‌های شهری رو بهتر و هوشمندانه‌تر مدیریت کنه.
اگه شما هم تو این حوزه فعالیت می‌کنین، می‌تونین طرحتون رو ثبت کنین و هم تو حل مسائل شهر نقش داشته باشین، هم فرصت همکاری با شهرداری تهران رو به دست بیارین.
📲
برای اطلاعات بیشتر، عدد
۱
رو به
۳۰۰۰۱۹۱۵
بفرست
🔗
ثبت ایده و طرح:
https://deftech.citex.city</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/442604" target="_blank">📅 19:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442603">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس پرس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdVe8OkIbFDSjsHOuq3c8-jOjyo4evXC2djE_GvctUQg0l8lTug5m7sEY8GF7-u0_KrMtPd7j7lZqVwewHe3prg_cms1qspyd2KEdeaYHXkpEDgN0fixJ6qOFOWCavDN8keddZHVKXVsx7_FS7p05dQDkn794Z2lIaq-zWK-EwnPAxVz2CcV4rHRvkedj1Q_3rMMfi-bf7VIqokLO0npGfvzUunxkxMEku6cxBOe5EPyfJgAMyBhkZ2XLEfbzOgbgWJqKp2n9Z1hstgddQeQDuZExMVdoJ3fIkWweyw7p--bkNqs-4JAM26Na3LXnPoKsJ7rRc_yhLSeQdBBMaeOhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔰
آفریقای جنوبی «مس» را مشمول مشوق‌های صنعت خودرو کرد
🔻
دولت آفریقای جنوبی با افزودن «مس» به فهرست مواد معدنی مشمول مشوق‌های صنعت خودرو، بر نقش راهبردی این فلز در زنجیره تأمین خودروهای برقی و توسعه فناوری‌های انرژی پاک تأکید کرد.
🔹
کمیسیون مدیریت تجارت بین‌الملل آفریقای جنوبی (ITAC) اعلام کرد فهرست مواد تحت پوشش این مشوق‌ها با افزودن عناصر نادر خاکی، آهن، لیتیوم، گرافیت، مس و کبالت گسترش می‌یابد. پیش از این نیز موادی مانند آلومینیوم، فولاد و فلزات گروه پلاتین در این فهرست قرار داشتند.
🔹
قرار گرفتن مس در میان مواد مشمول این مشوق‌ها، بازتابی از اهمیت روزافزون این فلز در صنعت خودروهای برقی است؛ به‌گونه‌ای که میزان مصرف مس در خودروهای برقی به‌مراتب بیشتر از خودروهای متعارف برآورد می‌شود.
ادامه خبر در مس‌پرس
👇
https://mespress.ir/x6R5
@mespress_ir</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/442603" target="_blank">📅 19:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442602">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/farsna/442602" target="_blank">📅 19:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442599">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CbuG2CoVco0a0RhUQbuVD3FBxGX6eGdX_LhpCgzEcTkzet1pIPkX6rZP1RiRipWesOzTA-rZNs6kIAy9Y-EPytkIferHpSQm8rXSpLSvlGD4VLTb70tWMGZ0Tz3GK6KkN2Tdd3uZzMFfJsKhym3Me7cKHkD_KUUxGcdMTgwaAHyAdtElIAv4slHJ_0mQP-D7dylrTMe7fGFMUdr1bDHi2o6xH9ryRRQirntmWpWR1citWZgrSCYbKZYOX6nHYFlgl9UzMXH0j_MPHBuefg597SEohUZRM30d1jIor7Av6fPY-0EZBmILqsLzUsyuu_H-_V22OhJVyfCCm4WQ79vcZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه صهیونسیتی: احتمال پاکسازی کابینه ترامپ از مخالفان توافق با ایران وجود دارد
🔹
اسرائیل هیوم گزارش می‌دهد که ترامپ در حال بررسی «پاکسازی مخالفان توافق ایران» در دولت خود است.
🔹
منابع آمریکایی در این‌باره می‌گویند این مقامات شامل «وزیر جنگ آمریکا پیت هگزث و رئیس سازمان سیا جان راتکلیف» می‌شود.
🔸
پیش از این، رسانه عبری از مشاجرهٔ شدید میان برخی از اعضای کابینه، از جمله معاون رئیس‌جمهور جی‌دی ونس و ترامپ خبر داده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/442599" target="_blank">📅 18:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442598">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQityupOJVWe1Wcg2Uaq66ayxdpqd08t1OAGuOyN_eQaLpypgnlMp2uVejaTtkzjGCm5BRaHj7SlxmZPu7yyXQeH4Bkl06LsMCpoii-q_wuSs8ho4e0pTCeN912UfI1dwXVhoMxMvIR5C_4PCd_q_i5XRIkRjUxLylVLgqPgHZswUIaPehvHQ74TKvgkqhA_7X3vDMzTPDWCoY84ci2_nooKnyS7NJsm9ZjzscNTi-jV3cfTX8p1BuU8i1mmH6uCbBqpYN0xdxceUzgG6OZSv_QU2D0haWDsZvCSPc8QPuSYsrX2iscRhYNhYXg0JhWYom-iVxt5Ye4C2Bx6A6N8rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
اگر بخواهید فقط یک جمله به رهبر شهید بگویید،  آن جمله چیست؟
🙍‍♂️
جمله‌تان را در یک صوت حداکثر ۲۰ ثانیه‌ای به
@Fars_ma
ارسال کنید.
@Farsna</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/442598" target="_blank">📅 18:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442597">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3e5d3bb29.mp4?token=cmCufbtN2-xa-n5F1XqxPrZ_SJ7fiLDm5Kll9DUKmXVXhCeG7OjzQKjsSlUgsJ_B_tf4ns-daMc29HmInecUE7tQI0QuXl5isa9_FdMtlqqFVnT0qWlOMp_a3c9MtZyyn-eEO_aZi8_TzjAKmKxXzIL_PnepsEt7HiVI2qxxKO5cCJVhc5B4k38XlyCW3H1-yspTuGnSQbMBKPcGx_Jb2AO4XtL6jsW8uhjMYuwBKtfXcvdCiIuq5pO9GvmEfs6_UnU_FxMjHvkynaCGXWVp3sVzWw2qWXL7n0-Bn1EhXDGuCilFhniZAWGplL6MNtBgbnmZWOa6yg39QgFqO3yN-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3e5d3bb29.mp4?token=cmCufbtN2-xa-n5F1XqxPrZ_SJ7fiLDm5Kll9DUKmXVXhCeG7OjzQKjsSlUgsJ_B_tf4ns-daMc29HmInecUE7tQI0QuXl5isa9_FdMtlqqFVnT0qWlOMp_a3c9MtZyyn-eEO_aZi8_TzjAKmKxXzIL_PnepsEt7HiVI2qxxKO5cCJVhc5B4k38XlyCW3H1-yspTuGnSQbMBKPcGx_Jb2AO4XtL6jsW8uhjMYuwBKtfXcvdCiIuq5pO9GvmEfs6_UnU_FxMjHvkynaCGXWVp3sVzWw2qWXL7n0-Bn1EhXDGuCilFhniZAWGplL6MNtBgbnmZWOa6yg39QgFqO3yN-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میثاقی: عدد ۱۶۸ در حافظۀ تاریخی همۀ ایرانی‌ها ثبت شده و فراموش‌نشدنی است
🔹
فراموش نکنیم در یک سال گذشته چه اتفاقاتی افتاد و چه هزینه‌هایی کشور داد و چه کسانی را دیگر نداریم تا امروز بتوانیم در مورد فوتبال صحبت کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/farsna/442597" target="_blank">📅 18:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442591">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mDO0H4e5b31tkGLXU7yywe7H3uC4pxYbfxxmavsd6XOyOkYNCg2ixwv5zj--RLZtWwtknmg1A3iM_rcRWfZQaCyKEUJbNFM8jYsNGikkbwv-ZeGWfjReSy1bvKT3TRVRJhT_HWCtt1ID-KGg778ffaw06fA6-giED5nff3R1Djg8Z_4xovFdUbWncRECYzTwkHowHrj-4sFCcNEsK2SgrVDylGHdyyRNc1imepUf2WJ6WBrIvUxazbVzsXX8uuQNdfNVk39jX7j9JdtLV7SW8Pz63RBA962dWNzgaXAsY-_yekw8TiAU5jgoZpJDO1ifUxNX79QBa4Umc6ALZ2F6gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D79lXwKaUsR64BjAM7VgYJEIwOEhD_ZM8kccTaCBUY2afAcbEkMyTLKiJk1vDHcwvdaJLqm6jH3tX320YACGeaSRjXjTsAlvna2J8seMtfGwsawwZfZ8UIwKK_21RK3w8xUksAGaBxglmUb-INm--FskqCDoavboqUe3P2KGwfL6SSU6EAUoZrUTodfMIwmDa_hx4xWKiH8oeQD-aobEGIj7i7O0W2UaJjPyYcC5QR4KsFittl2lWufJjuaMESi6JeahsHqQwmg64HXk5EuCOxovAX-nZQnZPuiwZhtCQ1sGbj1X-2IcFO_mjMIDO_gXAPZq5h-Oy_vwHOJUG929Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Grt9UR8tIRbppGJWVPzfKWNSGF15HlPE6La7r0nbVUCY9QLeMjfYPEytQB_G7cOUWzGYokBXwZlsMzEqNqq8J8bGTFJ0F6Vvo31bHRtqAJlLhbRBUKG_mtFk5HJNXnI9C75ssC9BOmSDAwC1dvehLmFAJEysOcjn5e2_gDBnoQFRMXv2x4BRhI2AJtR75LNe5PUQxVA04hoMd_e27-k0WTWEWzpaA4H3KqJcTSxzCt_DNSy29NnRyjdTfLOR3hqhw1U4UcByWBTO-sikSY2s-16__ZUA-VnWjW5Fyq-XAkGaKjB3lO-pj4gDgD6aauacDnSZ519WRqofJjEVmqkDsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E_73A9vrxp_k3iTrS5sLrlLjCMP7XTaGGR6TGp7G6ivnasI_GRmMyvx9sce4DlIYv6ItnPYlNAu0MaPdFpZkfbEugjWT2CI4UnGOFb_Oqc17NG30ubvlG4U3huDZEf32-8s31qwP93iEAM58rJOiB4wC08jSqFj3c7-uw54_s7EuYQ-xJV383HE3p8QOaRJbqhRW7aDLRenGs_JoiC-qywM3RNME_abNEMch9lb15yvApKbk82LqgN0MRuozf66Jy_l30lbDd43qXloeJNB7nro-mYfsBN-Erf0nzwJwOi8Po1ruzqV-slsPP6K2p8oeDhy-ymLW84QOgzj_FhFBVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qDP6HUtic0vezCJTscZqYaoh_2nR4pcB3Oy4Fe6ry43BjPm8guGAtVM8i5U6HAIy5EJrEmEsITwK5fgd4fE4vLIM1bXpFfOiU4Gs-zVHRW3pR3qf4hSyTiZ2dZz4al0joGPPI9KSmu0doLMrwkgTKa5ZGLeXnreWcmFgqyVLKbAjccF_Nqf3BDAlUJezQA6ZpJuyqKXs266P1_Zi8L6EIEsOtdHwWbsWVrmO8-DJP389d9M-QNzYfh1nvMB6VqhsgNhkHguG-0WnTT0XEwTuZ9LJGO0S7J-L4C0YlTNwMP9nZBialHQoU6Fqnnmv3Rur8eHiw8THOAMQr_Wkb92Y8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J013RZoP48kabpz3sYyO86e3TUBV08Eeb2tq8W5OgXjw7KfeaND53-U2BE83153YyZ28s8YBzFVDFGx4Ch64Gzu7b8GhJvKFGtTgvYAGGVYOjZ8A_tLbYvqFXLSajjwqYPt0gnKoNlKm9GM3sIBu-iGmmqEckAijjUx7jIT5O1Ul076_Rwp7mncy90jTPzC1Yo7_VRbRBHS-8tUj8BoMdeaF_n4aP-9q9f3xz4G1aERdTuGHUD4oJJtMc_FRGsl1yCCMOOJWZycrA0b3t6PJCAvnpn_GUnBa1QpTuZIV8lTZugsLMG-VEUlmFoZkjDuUB9BjGWiRqZj5gg7NlZ2Kew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دیدار با خانوادۀ سرلشکر شهید شیرازی
🔹
غلامعلی حدادعادل، اعضای دفتر حفظ‌ونشر آثار رهبر شهید انقلاب و جمعی از اصحاب رسانه با حضور در منزل سرلشکر شهید شیرازی، با خانوادۀ این شهید دیدار و به مقام والای او ادای احترام کردند.
🔹
سرلشکر شهید شیرازی، رئیس دفتر نظامی رهبر شهید انقلاب، در نخستین روز جنگ رمضان و در حملۀ آمریکا و رژیم صهیونیستی، همراه با رهبر شهید انقلاب به شهادت رسید.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/442591" target="_blank">📅 18:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442590">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/926e5026ed.mp4?token=OLmRwNzA7HkJaDnBZzMkbM6ljcq7--Cc9ogw4srvsp2d30czSTL_ondvVuwhLK-In5FxlGaXHzsI7ifq2V5ib4Q6M74AItb4Qka-og8OPengcAKYYUrcyge8UwJO2483fHO6ijtf_wcaOOicaWYbskhvztwy6-BBCq2XMMJ_mpcqt8Jx09e9xBZQgw4BhaAd6nhIyYWWKk74G-JkgZx_NBCRU17zEkLDBMHbq4xruFU4dtW9MNeHCvt7zrCysWTCPTCmUvjaXYO2EASIatIq7HfjdT3vFr5lh-KvYJkuLg7m9yep-4cYy2MhYaGMw0-HsLcO35-r00wSOQxQz2ebxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/926e5026ed.mp4?token=OLmRwNzA7HkJaDnBZzMkbM6ljcq7--Cc9ogw4srvsp2d30czSTL_ondvVuwhLK-In5FxlGaXHzsI7ifq2V5ib4Q6M74AItb4Qka-og8OPengcAKYYUrcyge8UwJO2483fHO6ijtf_wcaOOicaWYbskhvztwy6-BBCq2XMMJ_mpcqt8Jx09e9xBZQgw4BhaAd6nhIyYWWKk74G-JkgZx_NBCRU17zEkLDBMHbq4xruFU4dtW9MNeHCvt7zrCysWTCPTCmUvjaXYO2EASIatIq7HfjdT3vFr5lh-KvYJkuLg7m9yep-4cYy2MhYaGMw0-HsLcO35-r00wSOQxQz2ebxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
باران در اولین روز محرم مهمان حرم امام رضا(ع) شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/442590" target="_blank">📅 18:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442589">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbd1093a5f.mp4?token=YALFLB3fzCrRJbeUdSecUHFeXdn56jTgXhW_Q7kK_pGHeiKd6Fxmn0yMWD1NA58aB53cm7QljHwJ2t71Sz4tlGqHhUO-fqZLOLbirbcbkqo3R4XYRsbqG7wwikXox7LmKtRmk8zGMTIGOsq5189pMixl5KyjBRfhdiro4-kKYI1kqJDwlwhXqelJtz0e_NTLx3VAd-d9f5-1KIQE3rnM5GJpkA8u48od_latBUe7DLx8JqNt61UJAleUgvQOMZgEohck37LH6wH9WbPyP63O51clsBblgwaWhj-zxoIPPaf-x52xdmhxKS-dpasg9B_3X-Rt9Z11QPS0oNpaeFPV6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbd1093a5f.mp4?token=YALFLB3fzCrRJbeUdSecUHFeXdn56jTgXhW_Q7kK_pGHeiKd6Fxmn0yMWD1NA58aB53cm7QljHwJ2t71Sz4tlGqHhUO-fqZLOLbirbcbkqo3R4XYRsbqG7wwikXox7LmKtRmk8zGMTIGOsq5189pMixl5KyjBRfhdiro4-kKYI1kqJDwlwhXqelJtz0e_NTLx3VAd-d9f5-1KIQE3rnM5GJpkA8u48od_latBUe7DLx8JqNt61UJAleUgvQOMZgEohck37LH6wH9WbPyP63O51clsBblgwaWhj-zxoIPPaf-x52xdmhxKS-dpasg9B_3X-Rt9Z11QPS0oNpaeFPV6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظۀ احساسی بازشدن پرچم سه رنگ ایران در کف لس‌آنجلس
@Farsna</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/442589" target="_blank">📅 18:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442588">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">شهردار بوشهر برکنار شد
🔹
اعضای شورای شهر بوشهر با رأی به استیضاح شهردار، به فعالیت حسین حیدری در شهرداری پایان دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/442588" target="_blank">📅 18:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442587">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2746eb9dc.mp4?token=ldRGKtZaGlHt-QBVSVzpnXYK-NuIKMXnFwZB-AXIo4B1cmJz_WfHL7d9FbUMsHbrTA54tMh3JYsN5vsOsC4pj6AZUcxvnSRzs-sVohYvTxirdH-d5293zMQ2RqQGleDqlnp8gs6fVBIyV5YmTF8SjNpnv8GM91lnldFdv9pNcD7YdrqDokMUOadFtDakUQL03JRQ7J-t6rkZqF2cHTWnxt5aTvDu_W6o5fGL85gw51aOgi6gmEMs8gOMExiWoSatboOmPalnaKxebhnA9xWFUPs1J9zgEF7N1bxI9ZsDZmlemnZmjkFYn7EWmHNFvwu0Q3q_s6JkMitFcSaqvT5ggQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2746eb9dc.mp4?token=ldRGKtZaGlHt-QBVSVzpnXYK-NuIKMXnFwZB-AXIo4B1cmJz_WfHL7d9FbUMsHbrTA54tMh3JYsN5vsOsC4pj6AZUcxvnSRzs-sVohYvTxirdH-d5293zMQ2RqQGleDqlnp8gs6fVBIyV5YmTF8SjNpnv8GM91lnldFdv9pNcD7YdrqDokMUOadFtDakUQL03JRQ7J-t6rkZqF2cHTWnxt5aTvDu_W6o5fGL85gw51aOgi6gmEMs8gOMExiWoSatboOmPalnaKxebhnA9xWFUPs1J9zgEF7N1bxI9ZsDZmlemnZmjkFYn7EWmHNFvwu0Q3q_s6JkMitFcSaqvT5ggQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از فروپاشی روایت تا تصویرسازی دروغین اینترنشنال
روایت‌سازی دروغین اینترنشنال برای سفیدشویی سلطنت‌طلبان، نقش بر آب شد و رسوایی‌شان را دوچندان کرد. این جریان فحاش، با همان رفتار زشت همیشگی، ثابت کرد که هیچ نسبتی با ایران و ایرانی ندارد.
@Fars_plus</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/442587" target="_blank">📅 17:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442586">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14addb21c3.mp4?token=Ib-xL_lCdjwxV5-IpHiKDLO5nN8UuHmtYJ667fyz6hCAxj-_S1-zAgu6m2WJ9ZdCXmS_xmerN_LLuKQSsclHkTQLaNFzv8ALJb86yHSBvD-A4dJy3gUuRFqWcZoDrMdcUY0c1c4BQdZhTtZTu_aWNsGi98mzV02EwUYpDxug5lVCwIyCFEWnntFxJwv3j2a-z9voX5umxSnm6uGYADsD2I4AIuAp_DmGWtjTQJe5NxyU68bX4tFOe4WZSPR_HnLOs5Y_omruT4HKy1sOJlS413_JFbYn5ZmAuIzcZIMvk_V_nHW87blFoP5CPZL8S18Lmw1zUW7ABM-ZxYmppBftyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14addb21c3.mp4?token=Ib-xL_lCdjwxV5-IpHiKDLO5nN8UuHmtYJ667fyz6hCAxj-_S1-zAgu6m2WJ9ZdCXmS_xmerN_LLuKQSsclHkTQLaNFzv8ALJb86yHSBvD-A4dJy3gUuRFqWcZoDrMdcUY0c1c4BQdZhTtZTu_aWNsGi98mzV02EwUYpDxug5lVCwIyCFEWnntFxJwv3j2a-z9voX5umxSnm6uGYADsD2I4AIuAp_DmGWtjTQJe5NxyU68bX4tFOe4WZSPR_HnLOs5Y_omruT4HKy1sOJlS413_JFbYn5ZmAuIzcZIMvk_V_nHW87blFoP5CPZL8S18Lmw1zUW7ABM-ZxYmppBftyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملهٔ پهپادی اسرائیل به جنوب لبنان
🔹
در جریان این حملهٔ صهیونیست‌ها، شهرک «میفدون» هدف قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/442586" target="_blank">📅 17:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442585">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d999b963b.mp4?token=rBGT4MlvoBEEasfZDEwpE8KannqgnDiIMh85BQudhudHGfAJPJj3vShxRqdehPqIbsK-bo493W-alquDMDUFKlBmu-Nsv0tOKN1tsKGzEfRjIH7hOhKtsFnAQc2gi4FCAWNoFnmmTBnmP2NrPCVTaqZrgNoJnSM0e09VvYHKJmqgs8p9JFzK5dBKK4NmL31vWVYvY_R4wwkd4PvqyOz-RUtMFdjOSHfJ-7WhBSz-DZiOl2mFN3eQNMRiJurJa01eg16l3JGyGb04-lxzwXIOj5ThcRoWUhSHibyQQYTWctIO1DqgjUxL_e63ZQyXBAJyShtQnjM7ZZxskBZ-3TmeFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d999b963b.mp4?token=rBGT4MlvoBEEasfZDEwpE8KannqgnDiIMh85BQudhudHGfAJPJj3vShxRqdehPqIbsK-bo493W-alquDMDUFKlBmu-Nsv0tOKN1tsKGzEfRjIH7hOhKtsFnAQc2gi4FCAWNoFnmmTBnmP2NrPCVTaqZrgNoJnSM0e09VvYHKJmqgs8p9JFzK5dBKK4NmL31vWVYvY_R4wwkd4PvqyOz-RUtMFdjOSHfJ-7WhBSz-DZiOl2mFN3eQNMRiJurJa01eg16l3JGyGb04-lxzwXIOj5ThcRoWUhSHibyQQYTWctIO1DqgjUxL_e63ZQyXBAJyShtQnjM7ZZxskBZ-3TmeFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معجزه‌ای که امام حسین(ع) برای طراح ضریح خود داشت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/farsna/442585" target="_blank">📅 17:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442584">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ie-QjmmLe3dg4w07WlKclCHIfxEHWjpRT1jLbOaELuruJ1MwXv_ZAruBBDOrnedu6PpQt5BOi0vVJnQAaE1t2svpNM4XqPnGQJx_RVb2DQXMc-HaT-FBQdc1u6qBr7RtLfIWlai6iyJoPDL4jXGu1vzDNhfuBbgBcWB-c8y8vBW9y9MoRn4l6SjDEU53n-WPLuG5Fq6-Lat5xNTdXohQ7DhfHC1o1wz5kifPKRqA-G-drVyv9iJuDO5Csz0tj0lFSynJl3GaNfUziDiPmPvocEOIy8JQYseYr8SEZsNPJLMzxmcEfMnN4AfP6MOIJSpfk_4kITnxq-5Ygda6hh68jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکونومیست: پایان جنگ ایران، یک شکست بزرگ برای اسرائیل بود
🔹
اسرائیل به امید «نابودی ایران»، تجاوز دوباره علیه این کشور را کلید زد، اما اکنون حتی رسانه‌های غربی هم اذعان می‌کنند که این جنگ «ضربه‌ای» سنگین به اعتبار نخست‌وزیر اسرائیل بنیامین نتانیاهو وارد کرده است.
🔹
نشریه آمریکایی اکونومیست با اشاره به تفاهم بین واشنگتن و تهران تاکید کرده که بنیامین نتانیاهو همه سرمایه سیاسی خود را به کار بست تا رئیس‌جمهور آمریکا را به جنگ با ایران قانع کند و «حکومت حاکم بر ایران را سرنگون کند.» اما در نهایت به هیچ یک از اهداف اصلی خود در جنگ ایران دست پیدا نکرد.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/442584" target="_blank">📅 17:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442583">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bddd12045.mp4?token=mnj0hVf-Q86jt355aGBK_d0dJpb1v_fphUzpvLLscLG2gHuhRrF7oP70yiPn0ePjo0O7-YEkbRUnfaH3gL8mv24bH1gfuB5xWQSvpM_m1-UfXI8QINv6o7rOm4UAljC598E0lTBzb31M9fS_cgKGJKBcnciavZOeq2MWsArktMj8O8QJ2XOQ70Lq5wh1JUlbeh37UASD5CXYi156kiOyDNxwffhDv3EtEt02yf1G-T5RkynKuJ6oBqBzkucQDpv9vU4UOI_3KLK2kHou2LOO0JcOi_m6LdSmySDA1GFx5Taxg6jgXhMwMavyZvxZpjGa7s94w2tPevItyyEkZi6iHDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bddd12045.mp4?token=mnj0hVf-Q86jt355aGBK_d0dJpb1v_fphUzpvLLscLG2gHuhRrF7oP70yiPn0ePjo0O7-YEkbRUnfaH3gL8mv24bH1gfuB5xWQSvpM_m1-UfXI8QINv6o7rOm4UAljC598E0lTBzb31M9fS_cgKGJKBcnciavZOeq2MWsArktMj8O8QJ2XOQ70Lq5wh1JUlbeh37UASD5CXYi156kiOyDNxwffhDv3EtEt02yf1G-T5RkynKuJ6oBqBzkucQDpv9vU4UOI_3KLK2kHou2LOO0JcOi_m6LdSmySDA1GFx5Taxg6jgXhMwMavyZvxZpjGa7s94w2tPevItyyEkZi6iHDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هرمزِ بسته؛ ۱۰۰ روزی که بازارهای جهانی را به زانو درآورد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/442583" target="_blank">📅 17:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442582">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZtVaukPR05jkFy7e-jdwGa6fyLyfgGI2T8wXiYBqBSVq5Dq004X0fJ5gbjRmVpnzdSN8SWhPI7k3ieghyInLybCsCpl3tBoDYX0qbQ3Eee-uDvmw-wxJhWsiDhWw9rX5GQXKdutlJDxMZDEx8hw4rPimH7xZfYktlovDJx3SMgcGq1kTtHWTNxr2DDszPlYh7UG0RV6N8Gkd6e8JFVLFbQFoJSpH5ss_DgjwNKYC-l0Ite0PSd4DepLJV5nVtKlk9JEydJb4RjUnzKwvYWVvEjdHQyvueoJL3TLYGxBCCWiFhb8HJ5ccyjX4aFEEd-8K0l1DRAeqmeMGxxPR50GQTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: توافق با ایران را به کنگره خواهم فرستاد
🔹
نه‌تنها متن تفاهم را منتشر خواهم کرد، بلکه احتمالاً یک کنفرانس خبری خواهم داشت و آن را کلمه‌به‌کلمه خواهم خواند تا رسانه‌ها آن را به‌درستی پوشش بدهند. برای این که این توافق بسیار مهمی است.
🔹
تفاهمنامه درباره یک موضوع است، این که ایران هیچگاه سلاح هسته‌ای نخواهد داشت. باقی مسائل، رک بگویم، بی‌ربط است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/442582" target="_blank">📅 17:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442581">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b257fc1a8.mp4?token=lMBN4LVKCTklrMXtSJOlUT1SsdF0NfrlMC3CJU2oxBHn2M1pI3nSHjK-QZUcrfdULdGxGhHlWe3yVQfML4ojJHVwF_gI_xlqQN9C2N9bG2mKxwM9SFA_4IfFNf4n9Xq2jKGTNK796JNpZ3q4i0gVWme170cucw5dOg-txafNWQMOduVEZyt-m6b0g2QypHV_v1UfdmXUh3J0dKp4GpYPi85Tsp45TX_nalM285xk5V4E48LYnWkY-YQIy1yp__Va1tQT8cht-sOue5cRaaozT1U8NjkqKQ8T-u5qBpdZCzd4BCIuRCRStgWxKj1kGCWQXGicH3gVdcIZwR_KioyWpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b257fc1a8.mp4?token=lMBN4LVKCTklrMXtSJOlUT1SsdF0NfrlMC3CJU2oxBHn2M1pI3nSHjK-QZUcrfdULdGxGhHlWe3yVQfML4ojJHVwF_gI_xlqQN9C2N9bG2mKxwM9SFA_4IfFNf4n9Xq2jKGTNK796JNpZ3q4i0gVWme170cucw5dOg-txafNWQMOduVEZyt-m6b0g2QypHV_v1UfdmXUh3J0dKp4GpYPi85Tsp45TX_nalM285xk5V4E48LYnWkY-YQIy1yp__Va1tQT8cht-sOue5cRaaozT1U8NjkqKQ8T-u5qBpdZCzd4BCIuRCRStgWxKj1kGCWQXGicH3gVdcIZwR_KioyWpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تونل‌های برفی در ارتفاعات اشنویه
🔹
با گذشت ۳ ماه از زمستان راهداران آذربایجان‌غربی همچنان مشغول برف‌روبی در ارتفاعات شهرستان اشنویه هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/442581" target="_blank">📅 17:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442580">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mE43w2o1F19YsT5sy4PBMVJyNI8GRE1m95400M7f2X-4bmDDyRWG6wK2YIyQJbw5vPZS1dFxLfPIY9BzKIz7wlRJeDVRo27ySA1uQELJrZFQjVO8iJdQDET9Gf_NfRZPjvAewa0QND6pmic8bIHHIl8HrwxbvuuTmFX6roSxlIltOcVTgFnM_I8zCJwTu7lGQrk2zhDutJZNDjKLgGGmQBp1pJCYeWIFp9A3COGlK0wRGoBsxyv4HVE1n7jmCcJe0A4zbjv1lWgnT8HU8c5XmAV1eSUgZPpzvos7RQcQVNJh6sr5gX8kc3I7uZG0iO63_Ad6idY1BOqGHwy_D6qyhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چمران: ایجاد منطقه آزاد در تهران به تسهیل ترخیص کالا کمک می‌کند
🔹
رئیس شورای شهر تهران در واکنش به مطرح شدن ایدهٔ ایجاد منطقهٔ آزاد در تهران گفت: چنین اقدامی می‌تواند در تسهیل ترخیص کالا مؤثر باشد. برای نمونه، در صورت ایجاد این منطقه اتوبوس‌هایی که در گمرک…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/442580" target="_blank">📅 17:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442578">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0c4fe8180.mp4?token=dtZeSTJO-UbingZUpby1JUBT0N64w7JQ21wdrqdUeE4gdrEL8PfQD8Xtppt0jRTfFqJG5FFGQcKVlYnHYA7O7riG1juytDnGltQkxuCGC8-M0aOmCIkD1Yp7eOePYrUUsPD4swYiylgemmP1cYB3MNcZFg-_27aiAjMLMoJuHCqHuGhfOhOFigRWn_CjccrYWSGaPLPs_VUBmT6D1MgMK4Xdls8RGbN8u7r8cDxeSRmn_WCFsKY9V6_agCdDy_OhBTVMM3CDjPrJXpCBhu4dX4pzXsAhCQlIhnZ14n_UVjJ0JZ_uZ9lZ-aZ75lImypXmTUqz9EsjAuMsDu3tyWBXBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0c4fe8180.mp4?token=dtZeSTJO-UbingZUpby1JUBT0N64w7JQ21wdrqdUeE4gdrEL8PfQD8Xtppt0jRTfFqJG5FFGQcKVlYnHYA7O7riG1juytDnGltQkxuCGC8-M0aOmCIkD1Yp7eOePYrUUsPD4swYiylgemmP1cYB3MNcZFg-_27aiAjMLMoJuHCqHuGhfOhOFigRWn_CjccrYWSGaPLPs_VUBmT6D1MgMK4Xdls8RGbN8u7r8cDxeSRmn_WCFsKY9V6_agCdDy_OhBTVMM3CDjPrJXpCBhu4dX4pzXsAhCQlIhnZ14n_UVjJ0JZ_uZ9lZ-aZ75lImypXmTUqz9EsjAuMsDu3tyWBXBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مداحی محمود کریمی برای فرماندهان شهید و ماکان نصیری
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/442578" target="_blank">📅 16:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442577">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b67a9666a7.mp4?token=rkfjuTHtdo2tOUoemz_WyS7U5tVkMXJypfHXe3EDhM7aFN3T26wGR14qLP1Cu-ersY_ZNVTxF0T48lSxJhQBdHKO5yfx3k_OxXF7fW_cJTUiL_a8xJ4MrR9Cf7AKQPeBKqnBiLujKylxrbi8U9hd_7eF0XbJ_5x6ZtcjHsPjjeBXu2Dmys1gWwOitr6F3EAPd8Lr4gzYTffDt9ChMU1CIe6ZcFMEjtBQ_uuv9kCEgkNXo7lsbrZRDgdqdAFUWPLpcrp8B2plsKd1tkjO2jFz4S6TlFPixUGBy9TK5TI27HNRqY4z5EWg-ESFaZiuLmSPUAHvi3y2Fd65YKf5LfPetA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b67a9666a7.mp4?token=rkfjuTHtdo2tOUoemz_WyS7U5tVkMXJypfHXe3EDhM7aFN3T26wGR14qLP1Cu-ersY_ZNVTxF0T48lSxJhQBdHKO5yfx3k_OxXF7fW_cJTUiL_a8xJ4MrR9Cf7AKQPeBKqnBiLujKylxrbi8U9hd_7eF0XbJ_5x6ZtcjHsPjjeBXu2Dmys1gWwOitr6F3EAPd8Lr4gzYTffDt9ChMU1CIe6ZcFMEjtBQ_uuv9kCEgkNXo7lsbrZRDgdqdAFUWPLpcrp8B2plsKd1tkjO2jFz4S6TlFPixUGBy9TK5TI27HNRqY4z5EWg-ESFaZiuLmSPUAHvi3y2Fd65YKf5LfPetA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صحنه‌ای از ۴ دفاع پیاپی ملی‌پوشان والیبال مقابل بلژیک
🔹
با وجود ضعف‌های زیادی که تیم ملی والیبال در هفتهٔ اول لیگ ملت‌ها داشت، اما ملی‌پوشان ایران مقابل بلژیک در صحنه‌ای دفاع جانانه‌ای را به‌نمایش گذاشتند و نشان دادند می‌توانند با تمرکز بالا، نقطه ضعف را به قوت تبدیل کنند.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/442577" target="_blank">📅 16:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442575">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‌
🔴
شیخ نعیم قاسم: از طرف حزب‌الله و مقاومت اسلامی، و به نمایندگی از مردم وفادار لبنان که مشتاق ابلاغ مراتب قدردانی خود به شما هستند، و همچنین ازطرف شهدا، در رأس آن‌ها سید شهیدان امت، سید حسن نصرالله و جانبازان و آزادگان، از شما در مقام ارشدِ مذاکره‌کنندگان…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/442575" target="_blank">📅 16:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442574">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: ما همیشه گفته‌ایم که ایران به حزب‌الله و مقاومت و مردم لبنان همه‌چیز داده و چیزی از آنها نگرفته است
🔹
ایران به ما امکانات، قدرت برای آزادسازی سرزمین‌مان، برای التیام زخم‌های جامعه‌مان و کمک به آن داده است و اکنون ایران خون می‌دهد، با حمله…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/442574" target="_blank">📅 16:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442573">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
نامهٔ شیخ نعیم قاسم به قالیباف: کلمات از بیان سپاس عمیق ما نسبت به مواضع قوی و حمایتگرانه از لبنان و مقاومت و الزام رژیم اسرائیل به توقف عملیات نظامی در تمام جبهه‌ها از جمله لبنان به‌عنوان بند اول و اساس توافق بین ایران و آمریکا ناتوان است.
🔹
شما تنها و…</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/442573" target="_blank">📅 16:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442572">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
نامهٔ شیخ نعیم قاسم به قالیباف: کلمات از بیان سپاس عمیق ما نسبت به مواضع قوی و حمایتگرانه از لبنان و مقاومت و الزام رژیم اسرائیل به توقف عملیات نظامی در تمام جبهه‌ها از جمله لبنان به‌عنوان بند اول و اساس توافق بین ایران و آمریکا ناتوان است.
🔹
شما تنها و مؤثرترین شعله امید را در بازداشتن تجاوز اسرائیلی-آمریکایی از لبنان به حقیقتی تبدیل کردید که به جهان ثابت کرد ایران حامی حق، مقاومت و مستضعفان است، و اگر دیگران راه آن را دنبال می‌کردند، آمریکا و اسرائیل این‌گونه گستاخ نمی‌شدند و اشغال صهیونیستی بر زمین فلسطین و قدس باقی نمی‌ماند.
@Farsna</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/farsna/442572" target="_blank">📅 16:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442571">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0426334c5.mp4?token=lvd68_MC6ISsMXBo-q4-h3GGVR9z5tXGQhr0OTq0EJxpr2KWvdALgkQo-iA4MKrTa5kAMQ0mn4z3IBaRae3wQNAxtB30-M1KfbEuoCkmpwwp9hC4W3BToGz-p8lkBRLnm3EytGFAAxcbwGbzARGe3aUjq9mnyoV6GZXx2hF_pRreHczv8Z81if1ddrL7iqHNfH7SJjPSN2lrncAGHqoEUcqZvTW9fkc2PP7z5TUeopgaA5K-QkMnhydEtHaADYI5fjldDpwZax_0H-m1Nb0079XtkNBA99U8M-Oah5Mu2BT-GFdh0CQVTaFRKiJm0yJGPpjg9eqZhZcEh9J8ztVdPDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0426334c5.mp4?token=lvd68_MC6ISsMXBo-q4-h3GGVR9z5tXGQhr0OTq0EJxpr2KWvdALgkQo-iA4MKrTa5kAMQ0mn4z3IBaRae3wQNAxtB30-M1KfbEuoCkmpwwp9hC4W3BToGz-p8lkBRLnm3EytGFAAxcbwGbzARGe3aUjq9mnyoV6GZXx2hF_pRreHczv8Z81if1ddrL7iqHNfH7SJjPSN2lrncAGHqoEUcqZvTW9fkc2PP7z5TUeopgaA5K-QkMnhydEtHaADYI5fjldDpwZax_0H-m1Nb0079XtkNBA99U8M-Oah5Mu2BT-GFdh0CQVTaFRKiJm0yJGPpjg9eqZhZcEh9J8ztVdPDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قطعۀ دوم آزادراه شهید شوشتری بدون قطع درخت ساخته می‌شود
🔹
رئیس شورای شهر تهران: قطعۀ دوم آزادراه شهید شوشتری طی ۳ تا ۴ سال ساخته می‌شود. بخشی از پروژه به‌صورت تونل زیر جنگل و کوه اجرا می‌شود و به جنگل آسیبی نخواهد رسید.
🔹
یک کارشناس شهری هم دراین‌باره گفت:…</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/farsna/442571" target="_blank">📅 16:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442570">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/610aa9973e.mp4?token=Sk6kzK8iMQinL6t0Aonn36SQ4YFmgYBRhsB5egIkXqUrmTbKPn-1ngd6Whmvo9bbTnCtz6xscrW1JdKLX0MqYZeqo0ulgssbQWeVOUINykeLWVEZjDZvWCEubbAYXTEtImadHE5hnE6HGvG3_2AGwdASolGdfwV5EiLLCZatbM4ECa2FuPTqBooZwSOM9hCRfpJsiJROqenFO-iIZVyASf46P9EGs24ToM0sCAgXrXItwlqqo48ct_pCDHSE31ANK2lH1mA2zwJkqbSZbWxBc-fccqOGSA2evAuU7lhLO2A86sA_zzxYgFDJjTFI__QTk-D5zN_6UD32B3wM59RcSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/610aa9973e.mp4?token=Sk6kzK8iMQinL6t0Aonn36SQ4YFmgYBRhsB5egIkXqUrmTbKPn-1ngd6Whmvo9bbTnCtz6xscrW1JdKLX0MqYZeqo0ulgssbQWeVOUINykeLWVEZjDZvWCEubbAYXTEtImadHE5hnE6HGvG3_2AGwdASolGdfwV5EiLLCZatbM4ECa2FuPTqBooZwSOM9hCRfpJsiJROqenFO-iIZVyASf46P9EGs24ToM0sCAgXrXItwlqqo48ct_pCDHSE31ANK2lH1mA2zwJkqbSZbWxBc-fccqOGSA2evAuU7lhLO2A86sA_zzxYgFDJjTFI__QTk-D5zN_6UD32B3wM59RcSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جزئیات جدید از ثبت معاملات ملکی در سامانۀ کاتب
🔹
سازمان ثبت اسناد و املاک کشور: مالکان املاکی که دارای سند مالکیت حدنگار سبزرنگ هستند، می‌توانند به‌صورت خودکاربری یا از طریق مشاوران املاک، نسبت به ثبت معاملۀ خود در سامانۀ کاتب اقدام کنند.
🔹
این قراردادها دارای…</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/farsna/442570" target="_blank">📅 16:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442569">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9767cf1552.mp4?token=kEbrHY0-P7F8M088dSuFJd4wh6KVzOsMbbTVj01-VyqmfIjYugd-wr2iSBuIFmT_dCpn0ghHO0UL_BGjXE3WgeK2tbj9mukkW-HMmmE4rD9E_R-8f3OydOGbdkOtJyQh911QJ9G0TdA2C3mSVDF4z1NKZBHiSkZRGJSN6SWWeaEOpKl7xKZtRGTe5oMklIrMjb3pY8r457DuLc4G9HMZCttZ7l36J6VI8sHQWHqgAMEDh7OW6bu3iTSzIsk6i4IzYYagyFaJFf3dgtZfnW7EZa2OetJyACWEE-qMWep9Or8IlgKQOgmnTEjBZp-dopMeP5TtQLfcrTjJ6FvjxqiQRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9767cf1552.mp4?token=kEbrHY0-P7F8M088dSuFJd4wh6KVzOsMbbTVj01-VyqmfIjYugd-wr2iSBuIFmT_dCpn0ghHO0UL_BGjXE3WgeK2tbj9mukkW-HMmmE4rD9E_R-8f3OydOGbdkOtJyQh911QJ9G0TdA2C3mSVDF4z1NKZBHiSkZRGJSN6SWWeaEOpKl7xKZtRGTe5oMklIrMjb3pY8r457DuLc4G9HMZCttZ7l36J6VI8sHQWHqgAMEDh7OW6bu3iTSzIsk6i4IzYYagyFaJFf3dgtZfnW7EZa2OetJyACWEE-qMWep9Or8IlgKQOgmnTEjBZp-dopMeP5TtQLfcrTjJ6FvjxqiQRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور شهید لاریجانی در منزل شهید محمود باقری، فرمانده مقتدر موشکی ایران
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/442569" target="_blank">📅 15:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442567">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-KoUGN-bc3JsVmkDCIm3apR7xa-pYhn37KzVIQmICx1xo8Qjb7Z_vB8zdBN0qWTcQiEjloRbt1J0dc2eXSABMMjBdd3q8BauszBmsKJJBnrTY8GEr3SFaFUcEnM17k8GV8cqPXUhpZzYTqMgxWhKeg7b7_tE4herNwmmML7za9LUtozZ-7mJ1V2zU0C1H_3NpWSORXNTG5WmlM5gdgyhG8bDUyw8mEejmZWGxEBJ_OYeQhnh7C8GSVqyMUk_fi6avVC9tnKCqv8X_kJAgzhBVgnjCLQaRgv53VreW680MWLITO0Yh07hu_e0lnOgarG9cTtZ3PhnqLuF2vLg3woMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cd87c0908.mp4?token=unM8t6-VhCrg9-CLjDivZX1LUkUja5SYht3P2915KC-41lmrx6wNR-UhxWFG1If2yvWyBMYZ1nBackr8TDSxJMp-81P4zEBL3NHgyd1LjE7vRULno-OmjZW8ygT2SDJYy8etMNRMOTkQlh6F7cretj7T8K-KfY0rb2ZWA3t8rtYCkRF8CvlRntxTdgdXYBSquTQRsPkMGgNqxs7RDjlS1op68LSMOcjdkpj_oyOtko9kUDvQDdqlVsISHmyUKMdSHO7bIDm7Ob_w380_9itIvvR9qF5gb7fAKkfLULBgSWQil3-wkeCxzAcbiYTwcSjAh3mLAKa8J1OFpmPWdF9pcpDRa8aDDXbbovd0N4YHwRj_UqTITiHS1mCl_h2T-iGXlGsPxrWs1sg3mVZ9tgfg5ZYSrdCkRBH8YeTOwmgrzo0tMzlkheCil0rIhyQJqYs7SMQtirNQSvV-0iinn1KeCcZU6twNixPxMK4WKVVc9vLHFhsfQfx8RkzpL36F0AkNZsbQty0X3odU1xb3UsHp4fviTjXpzklSjgqFuQWHBE-Vgzpxoqd-O8svWopQOiOshEMzOu8OY15Q4946WopMWQIn7KaasBjGZy1WSrFNzD_Sansj1Kfcv1CsIGz3JXPJrLC_zEozDfXvpq7J6w7THA-F00aqMth30lSr0zizmaE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cd87c0908.mp4?token=unM8t6-VhCrg9-CLjDivZX1LUkUja5SYht3P2915KC-41lmrx6wNR-UhxWFG1If2yvWyBMYZ1nBackr8TDSxJMp-81P4zEBL3NHgyd1LjE7vRULno-OmjZW8ygT2SDJYy8etMNRMOTkQlh6F7cretj7T8K-KfY0rb2ZWA3t8rtYCkRF8CvlRntxTdgdXYBSquTQRsPkMGgNqxs7RDjlS1op68LSMOcjdkpj_oyOtko9kUDvQDdqlVsISHmyUKMdSHO7bIDm7Ob_w380_9itIvvR9qF5gb7fAKkfLULBgSWQil3-wkeCxzAcbiYTwcSjAh3mLAKa8J1OFpmPWdF9pcpDRa8aDDXbbovd0N4YHwRj_UqTITiHS1mCl_h2T-iGXlGsPxrWs1sg3mVZ9tgfg5ZYSrdCkRBH8YeTOwmgrzo0tMzlkheCil0rIhyQJqYs7SMQtirNQSvV-0iinn1KeCcZU6twNixPxMK4WKVVc9vLHFhsfQfx8RkzpL36F0AkNZsbQty0X3odU1xb3UsHp4fviTjXpzklSjgqFuQWHBE-Vgzpxoqd-O8svWopQOiOshEMzOu8OY15Q4946WopMWQIn7KaasBjGZy1WSrFNzD_Sansj1Kfcv1CsIGz3JXPJrLC_zEozDfXvpq7J6w7THA-F00aqMth30lSr0zizmaE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
میناب ۱۶۸ روی سکوهای ورزشگاه  @Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/442567" target="_blank">📅 15:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442566">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XjKataFc-1PwceMDnQS6qB4bQMNV4Twy7fUv0dcaIkVhQoZrY5qFlPyglOboLhBAXXZEQbZLsesNCri04QAhTr1G7ssPMDQ0YUXuUqcLyuR0aa8NAgzxnX2EhuGzRHzjXkKKalQOXL08NUerWaqnG8EPf8WwJ-X4Pya9K1c8hkIx86eNwHhM2HPbUwZJuni2cNVv_va3RRQ63s0Hv913HfHQpd4G312O6YxzGeOucd1tjjLw8oGVCeqfBL16iXgZrZjtHB1yILS3EmtDTCXV1W8OQQuGIgiTJ-IY0LRmKvPOYwnCJWby2N8xSsBgYPMazjS7j2kfoAU0KmvZ6LCfjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمال وقوع سیلاب‌ در ۸ استان کشور
🔹
سازمان مدیریت بحران کشور: از امروز به‌دلیل فعالیت سامانهٔ بارشی شدید، احتمال وقوع سیلاب ناگهانی، طغیان رودخانه‌ها، آب‌گرفتگی و رعدوبرق در استان‌های آذربایجان‌غربی، آذربایجان‌شرقی، خراسان‌رضوی، اردبیل، گیلان، مازندران، خراسان‌شمالی و گلستان وجود دارد.
🔹
همچنین در مناطق جنوبی کشور، به‌ویژه سواحل هرمزگان و بوشهر، خلیج فارس و تنگهٔ هرمز، وزش باد شدید و تلاطم دریا تا ظهر فردا پیش‌بینی شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/442566" target="_blank">📅 15:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442565">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lR4ZrygWsHcTCrG9IlJx5_Qm-W7w3TWfy06CokkkvOWYGgN1S16Jx_h6upp2TCaKU6RywrnIM6FeqPScKCiG8drB6om6gQCyar3WnCJfGkifv7arLt0dT3Fr-jojjqG9rjg8wFQf5xjRRh-U-I1vZN_Q9OKLqr8BaGJ0jy5DPNOw-rCS8RhVklKGu3lweiQJj6BdyYa9XN9uc8c9FBaPlh-Vi7k1a1USCIyWiVVuuOHBFgOeGXAF3Toyiq55In5dI_YqJNxvMIxvC58Cf5d7OqFpk52U-Ig5t09AmL_feF4mSJgtKMHWu2RYzSJXB-60HGeOoyQxG7ayohhI0k5frQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزش باد شدید در تهران ادامه دارد
🔹
براساس داده‌های هواشناسی تهران، در ۵ روز آینده آسمان پایتخت صاف تا کمی ابری در بعضی ساعت‌ها همراه با افزایش ابر و افزایش وزش باد پیش‌بینی می‌شود.
🔹
همچنین از امروز تا پنجشنبه در دامنه‌ها و ارتفاعات در ساعات بعدازظهر رشد ابر گاهی بارش پراکنده با احتمال رگبار و رعدوبرق مورد انتظار است.
عکس: حمید عابدی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/442565" target="_blank">📅 15:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442564">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSnCKaeW2TqM_1lCsfaJrFAtLZUFM2J-0x6EzqHYFQWsryIeqK62_N1bOUUUjm9XNHS5QS5E9etEgerSePuMN-nFw7linf2su2oj-OlnTpk3A4-9SYDIUZNaDHZXSmd3SqgyY0nb7m_4fBqplsjw5MIkgUyKCwWc8ZVyOPO9HDidS8H-mDkbIbLnxwQLpb20Uhp5OMMovybyTN4c3XbgIY0vqaFe5B3xtTFlt0CJvhMWujYIaInloVkhpII_3u14pQ3UqSmRBL5cFZUBh5pOGcgpzdipSscoBLtCUT1ph1HgiVBw_VZSUajwgcNtdUcpP4fW-W3R0fWvvpwKosaq-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی ایران در رتبۀ چهارم
🏟
پرتماشاگرترین بازی‌های جام جهانی تا اینجا
@Sportfars</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/442564" target="_blank">📅 15:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442563">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🎥
یادش بخیر آن رهبر جاویدان در بزم ماتم
🔹
مداحی محمود کریمی در شب اول محرم به یاد رهبر شهید انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/442563" target="_blank">📅 14:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442562">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vM7r1Z5Zp5VCODbGPZXcehGVK-6OVx9Wn-CKH4u1i8m4EL0Ds5sdM2y12yygaGs5jeI8t3rVTgrdQhseLEMb8IUpE4ustSaQNRoM7SaJ04m8siTuX1T4a0Yg9VM-K6R8zCB59zuzZPF_LYQ_tDVt3W9-LpRgWvSiW39PAKRFZEfIFwBcXrVKVhI3HG3GJyh_ZQ60AZ2VOsm1xCl3KxQZKsS31Gf73roiU4C_Ue_ksWQL6O9dokojI8lkoXuvQEIbQH-GjDsPl02biXnbIKuBdc7KjiiIqn2GjCs3QmH3z-6Aba8s6L0jIAOTyG1A8KwxTEtBVPZGaKI_4UUdlCMXFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر سرباز طبیعت به‌جای ۱۲ نیرو کار می‌کند
🔹
فرماندهٔ یگان حفاظت محیط زیست: یگان حفاظت محیط زیست به حدود ۷ هزار محیط‌بان نیاز دارد، اما در حال حاضر کمتر از ۶۰ درصد این ظرفیت تأمین شده است.
🔹
بیش از ۲۰ میلیون هکتار مناطق تحت حفاظت در کشور داریم و بر اساس استاندارد جهانی، برای هر هزار هکتار باید یک محیط‌بان حضور داشته باشد اما اکنون برای هر ۱۲ هزار هکتار یک محیط‌بان داریم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/442562" target="_blank">📅 14:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442561">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f14d10416a.mp4?token=AmSiNNB8jmc8HDNJM-HdLuKie_bErLWcQ9P3M0FBHltPaoiJnUyEzYtiPCwOuQDteDZTvOb94M2QvlVMSwyLMJO-Frqp7S6_w9NTL-X3A7PRsySjxY1vtzzK2YncK7oNANQ50dGbXAm2dZ6hcFGiwSMvLD-el7egOt0Ca4fblSvkRnCC0wj9JbKTuBKQmlWVtejaaNZTxRkAk3Z-HoUaZHbzgI5OgXwgoozD9zSjR795pCqtYknPWs32H1oNAeGi5FlEQx59KJv7_axXEsz4qB2IgKwZhr5s9CYIRKD4Gz7V7jzhA3ruFWa-zJ5g85Bx12Earqjn-TOquTPsU2tPmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f14d10416a.mp4?token=AmSiNNB8jmc8HDNJM-HdLuKie_bErLWcQ9P3M0FBHltPaoiJnUyEzYtiPCwOuQDteDZTvOb94M2QvlVMSwyLMJO-Frqp7S6_w9NTL-X3A7PRsySjxY1vtzzK2YncK7oNANQ50dGbXAm2dZ6hcFGiwSMvLD-el7egOt0Ca4fblSvkRnCC0wj9JbKTuBKQmlWVtejaaNZTxRkAk3Z-HoUaZHbzgI5OgXwgoozD9zSjR795pCqtYknPWs32H1oNAeGi5FlEQx59KJv7_axXEsz4qB2IgKwZhr5s9CYIRKD4Gz7V7jzhA3ruFWa-zJ5g85Bx12Earqjn-TOquTPsU2tPmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایان محاصرۀ دریایی آمریکا، با عبور کشتی‌های ایرانی
🔹
دقایقی پیش چند کشتی ایرانی نسبت به تردد بدون مشکل از خط محاصره اقدام کردند.
🔹
طبق اطلاعات ناوبری کشتی، یک نفتکش ایرانی VLCC از آب‌های آزاد به‌سمت بنادر ایران در حرکت است و از منطقۀ محاصره گذشته، همچنین…</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/farsna/442561" target="_blank">📅 14:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442560">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39152c14ac.mp4?token=idZGmkFDytUOFvLRkh8_9IEAGOipAGovreR2SLq_2gNzZgwlNQ4H31sIt1LM_CZh9Mw5l6mU0ZO58nTkw7iZBKi3qwfMrm7fBg2ylG5jhvI66FT5a5SYE87UzdrOo61A53S9AosydfzU3Gf-cwdWv1woZS1qMSw_xrOhdRg77s4u0PQDqzJ-UONqWaWD-vgxNmll1wtEjtAGaDKtu9hnfGCTiWU3eyJ3BXEUCg-On055BDqUYgoGryj95yDW0qhhFpNNI_UkZ7lg4jHYd9CIa4BwJ1t18SfNegxqEsd7L0LjU7JK-Vi28jGWNA03yAnAtGrib244qsIDnDGOj4AjBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39152c14ac.mp4?token=idZGmkFDytUOFvLRkh8_9IEAGOipAGovreR2SLq_2gNzZgwlNQ4H31sIt1LM_CZh9Mw5l6mU0ZO58nTkw7iZBKi3qwfMrm7fBg2ylG5jhvI66FT5a5SYE87UzdrOo61A53S9AosydfzU3Gf-cwdWv1woZS1qMSw_xrOhdRg77s4u0PQDqzJ-UONqWaWD-vgxNmll1wtEjtAGaDKtu9hnfGCTiWU3eyJ3BXEUCg-On055BDqUYgoGryj95yDW0qhhFpNNI_UkZ7lg4jHYd9CIa4BwJ1t18SfNegxqEsd7L0LjU7JK-Vi28jGWNA03yAnAtGrib244qsIDnDGOj4AjBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
اژه‌ای: ما برای گرفتن حق‌مان مذاکره می‌کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/farsna/442560" target="_blank">📅 14:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442558">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HETSNvde76GD0iE0GufyPIezTogA2_Fvw1wIEYvjN7jRuF4QsSHFZ6gJWS4mIU0YzfqAZCm6kVCtbPGohln-pdw_-V5IWLM6KJBJx9uoi4XZEbqUBmKQ3IeqvkPuE2Cbnp6wjGeX5gMinqW-KkJh5fmhYvcUW1uQK7NOPXKpj0tOrgq-0AKMm7ls_ndcWtRaGNm_P72JAjKaK1T3NGXSlLJxCsCucNsgTyIW54xuD1qvVi9i5g_FK6dLPZ4korKkdwO7KrVNUcWRuiucFn-BRKPZd54Qu0DKxaR0ULzYR3T44qvRjITf1-8EcL08mDL-0lPRFzjaaQJL9IZ9yvxZ5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YhHPKW46XhwSfxPzpULV-vLk_80c8crMMSdu3RQoN4cjsErTA5maXDakgLGIubqcgHznXuORmeVEewH7dG9skFhavJmN69-bkEbn2AnV6keKB-rqpVregLlUUzVCK_6UJGz_cp0ZW7eZEJf2rUZU_zBxx81ffqEAA5DnHsaCNDAbs2_yZisYRiR2IFmdPaGeYhRpJnSVXGg417z3yzZ_pNB2SA8VrxDIVimbHupzGztrWqDUPe-LrITVAesFJckZQWjMyz2ny9xlD9MGXK2NI5WKVKv2taGQloZN-Wg18rAHgKagrrLEoKWD5jXtJgnpBcZh1PGemWuoK-1Be8sKlQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تفنگ محبی مجوز دارد
🔹
شادی گل محمد محبی در بازی با نیوزیلند باعث شده تا رسانه‌های ضدانقلاب و برخی از کاربران ایکس با حاشیه‌سازی این شادی گل را خشونت‌آمیز تعبیر کنند و موضوع محرومیت این ستاره تیم ملی ایران پیش بکشند.
🔹
نکته جالب این بود که محبی به چندین شکل شادی گل کرد و تنها در بخش کوچکی به شکل شلیک تفنگ آن هم به صورت ضمنی شادی کرد.
🔹
اما با نگاه به شادی گل‌های ستاره‌های بزرگ دنیای فوتبال این نوع شادی در مستطیل سبز عادی بوده چون بهترین فوتبالیست‌های جهان به این شکل شادی کردند و محرومیتی برایشان درنظر گرفته نشده است.
🔗
شادی گل‌های مشابه بازیکنان بزرگ را در
فارس
ببینید
@Sportfars</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/442558" target="_blank">📅 14:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442557">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b69d86769.mp4?token=HjjxZC6a6BhJOX7XCVzB4gUG0FEuI4wGCzuRnf1SvCbgByr71bgoK2pztTNlSvVpnLBwQWKR_Pp0-kZ7ti--dcsojeZSRWdrGLy0deSh_sIElj0RC5hjxO-pV7-UBxp3aVuIZfB3mTqwL11wDLggRA04of6UpvSnZLEE0uMTXx8SstOFBuCxo2dDcGqFQilDeoyq7cP8iDQ9_gxMcIq6IxvrLmESqAyWrfGoSG3JgLSSTJ7sjAYs3I_Y9pgSrN5lFbKJJ1YwHT5EAUsMH3gsZhQi5UiXnGbMZxJ78ng1h3xGj8klTM6hgKxieHq3o4IYCE4EIaV4odzA8xlQTnrT3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b69d86769.mp4?token=HjjxZC6a6BhJOX7XCVzB4gUG0FEuI4wGCzuRnf1SvCbgByr71bgoK2pztTNlSvVpnLBwQWKR_Pp0-kZ7ti--dcsojeZSRWdrGLy0deSh_sIElj0RC5hjxO-pV7-UBxp3aVuIZfB3mTqwL11wDLggRA04of6UpvSnZLEE0uMTXx8SstOFBuCxo2dDcGqFQilDeoyq7cP8iDQ9_gxMcIq6IxvrLmESqAyWrfGoSG3JgLSSTJ7sjAYs3I_Y9pgSrN5lFbKJJ1YwHT5EAUsMH3gsZhQi5UiXnGbMZxJ78ng1h3xGj8klTM6hgKxieHq3o4IYCE4EIaV4odzA8xlQTnrT3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: در مقابل بدعهدی دشمن می‌ایستیم.  @Farsna</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/farsna/442557" target="_blank">📅 14:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442556">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkYQwSL2CrZDFEJpFSZNhztjQBa-9GysOxp7Vl79Un1BvFNZcGNxYf6ZhgqcFcMGaXsptJUN3MoE_ugd9OpFjsWYVw5qdNWpCVhr0yXPonABU3S3AF3xlNIffBPbqiUZmQhZy2u-a9IwwNmpD7NPXJ68sJhlGmkJBxkKt6nX_pKH7GJ1ukD1HNfPHBsGgua_9EI_R0CsZpKGgLo2J5WsXKzv2v-Opd4dCAHISeMIH347aF0euHF1nt3gYbxqHGYg_Jy3KMYp-msEddgQ1Z-6mdnbu--H3tIu2FkBfEJ33gXiHY9XWZHHmrhVWguMGHJx_nBx99tKeSZ1FWBI0T83oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
عراقچی: جمعه پس‌از امضای تفاهم، مذاکرات آغاز خواهد شد
🔹
در مرحلهٔ اول مذاکرات دربارهٔ خاتمهٔ جنگ، محاصرهٔ دریایی، تنگهٔ هرمز و آزادسازی وجوه مسدودشدهٔ ایران تفاهم شد و در توافق نهایی دربارهٔ موضوع هسته‌ای و لغو تحریم‌ها تصمیم‌گیری خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farsna/442556" target="_blank">📅 14:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442555">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb7cce6c6e.mp4?token=Z10wGLrxp13LyOfF2I5CPbNu5s3Be4w0RWpomuvanaYEPgp8EVaawcA8UVwU5wtDbVtKZ8-nxp9Ugx3-4hmKbYeTT8J0qVMmtibeokyqi7cSWdU_1XGCEdU8gfNbN8O3hrvVv7AQ7qV1QPqK9MvYg7tOqB39xsfrtDlirw1Ww9uGgkWB72N_zV9Qwv_EkHGKiUPgG92_IEY87liMAnurJs82PdotyYnnMsnNZW2J6CCetuIJU6nWmfY447T3p74G0OOpPdB_qAi5i-boj_k2FXYpHU3D_Uj1xFsPQ2V6mGaQP5k-9mOjjOUo0pKX9RKBKgdy8HJJXpUsB5rzJ9Wezg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb7cce6c6e.mp4?token=Z10wGLrxp13LyOfF2I5CPbNu5s3Be4w0RWpomuvanaYEPgp8EVaawcA8UVwU5wtDbVtKZ8-nxp9Ugx3-4hmKbYeTT8J0qVMmtibeokyqi7cSWdU_1XGCEdU8gfNbN8O3hrvVv7AQ7qV1QPqK9MvYg7tOqB39xsfrtDlirw1Ww9uGgkWB72N_zV9Qwv_EkHGKiUPgG92_IEY87liMAnurJs82PdotyYnnMsnNZW2J6CCetuIJU6nWmfY447T3p74G0OOpPdB_qAi5i-boj_k2FXYpHU3D_Uj1xFsPQ2V6mGaQP5k-9mOjjOUo0pKX9RKBKgdy8HJJXpUsB5rzJ9Wezg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: اگر من نبودم الان اصلاً اسرائیل وجود نداشت
🔹
الان اسرائیل ۱۰۰ درصد از روی زمین محو شده بود و هر آدم باهوشی در اسرائیل این را خوب می‌داند. @Farsna</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/442555" target="_blank">📅 14:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442554">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e9149ef45.mp4?token=DunOnneTphUS5UoA7Id5_U3iozxkfzbDJ-ZC-RQx0XRpBYi0tb-qyGEm_jgmUHWadLQ3cY3pMEcbyRorSzPO9GI4j2nuhu0A4UQxXMbV8iw9Ni5rCAc_xRPijyrzGYfAiyiea1bqxHtbmvsXuM7dV5NKg4mX89iNDR5Zw_1c65BEIzhPFsiKNQ6i0wCalDRjuzmri9rUigsCZ2rfEDkyr1OOZj0MiEoeRT--IpFzgjtfMuVqgBl1REv0Tw4ooBbz7ssT4WGg_HjG8U7yJ_71R-IYmJhHSIBFA2mLG5_51PhGq-ST2DHSbZAOqhc_X3dTx1WF4S3_2Ce6OiVdF_m7hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e9149ef45.mp4?token=DunOnneTphUS5UoA7Id5_U3iozxkfzbDJ-ZC-RQx0XRpBYi0tb-qyGEm_jgmUHWadLQ3cY3pMEcbyRorSzPO9GI4j2nuhu0A4UQxXMbV8iw9Ni5rCAc_xRPijyrzGYfAiyiea1bqxHtbmvsXuM7dV5NKg4mX89iNDR5Zw_1c65BEIzhPFsiKNQ6i0wCalDRjuzmri9rUigsCZ2rfEDkyr1OOZj0MiEoeRT--IpFzgjtfMuVqgBl1REv0Tw4ooBbz7ssT4WGg_HjG8U7yJ_71R-IYmJhHSIBFA2mLG5_51PhGq-ST2DHSbZAOqhc_X3dTx1WF4S3_2Ce6OiVdF_m7hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: در مقابل بدعهدی دشمن می‌ایستیم.
@Farsna</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/442554" target="_blank">📅 14:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442553">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6800f9e7b.mp4?token=CltjZ5dlB8-CSl1QJ9iZFvGoWtPn6tQkvIqjWYilKNS5tqkIZjlrXwOJM-8yKtvUxpng6Ql3i_t-vX60YwKFpP-isWmGsU1Z7iSN8EDJKQA9dEZ4e5FT1yimMxCH084daS2rqSqyJ7eFVQwUvSU0RdVxPrEf4oYTIa78Swxw6giwIwizTG5PcI40W2ybixFOCLC9opDWljM1oqUCtrKFkk0_PBoeDvV6CEQaryfRqBVAY9SMs1J-d03Bi7aR1RfCFtpqXTeN8mBu5hsk3U-w4BNEfEAZVv9-YRDwSgHHSX-dC1YHG1clRXAJaqpwkoP3o-Cjgt7xBUJflc9f0vTjXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6800f9e7b.mp4?token=CltjZ5dlB8-CSl1QJ9iZFvGoWtPn6tQkvIqjWYilKNS5tqkIZjlrXwOJM-8yKtvUxpng6Ql3i_t-vX60YwKFpP-isWmGsU1Z7iSN8EDJKQA9dEZ4e5FT1yimMxCH084daS2rqSqyJ7eFVQwUvSU0RdVxPrEf4oYTIa78Swxw6giwIwizTG5PcI40W2ybixFOCLC9opDWljM1oqUCtrKFkk0_PBoeDvV6CEQaryfRqBVAY9SMs1J-d03Bi7aR1RfCFtpqXTeN8mBu5hsk3U-w4BNEfEAZVv9-YRDwSgHHSX-dC1YHG1clRXAJaqpwkoP3o-Cjgt7xBUJflc9f0vTjXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: جنگ اوکراین هیچ تأثیری روی ما ندارد، جز اینکه ما سلاح می‌فروشیم؛ ما هزاران مایل آن‌طرف‌تر هستیم
🔹
اتحادیهٔ اروپا هزینه تسلیحات را تمام و کمال به ما پرداخت می‌کند. @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/442553" target="_blank">📅 14:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442551">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4afed014df.mp4?token=VHI4xvai5-mn3ehOtoR1BIX8HLDGIexCmtbcTqofxVrzMmjQxwFq-rgFmept7g8AzM_ZUTSMaFVBN5VSJXgRzDXnDobZcq6iSEcWzihqO8atFD1WDrzsoRWobcY0Q9oizRQ5jq3T2PQiw6_tHknWHQahec3Ee_HY1qz-WzcjwPk0Y2lLwqO_stIfxhFCC_Dq_yLmIjhpo-58aALodVrds2hS99uCphyQkv5sykwGytLpesoxHvgc9yXGot8r09mwWnCEk9mfIFf-dgO0r-IDcRET0uvC4PcUaPe29Va8xPui_T4hr0jOe9VeGCNLqIEmW5WnaGGEUhLttiUBeT21Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4afed014df.mp4?token=VHI4xvai5-mn3ehOtoR1BIX8HLDGIexCmtbcTqofxVrzMmjQxwFq-rgFmept7g8AzM_ZUTSMaFVBN5VSJXgRzDXnDobZcq6iSEcWzihqO8atFD1WDrzsoRWobcY0Q9oizRQ5jq3T2PQiw6_tHknWHQahec3Ee_HY1qz-WzcjwPk0Y2lLwqO_stIfxhFCC_Dq_yLmIjhpo-58aALodVrds2hS99uCphyQkv5sykwGytLpesoxHvgc9yXGot8r09mwWnCEk9mfIFf-dgO0r-IDcRET0uvC4PcUaPe29Va8xPui_T4hr0jOe9VeGCNLqIEmW5WnaGGEUhLttiUBeT21Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: به اسرائیل گفتم «بگذارید سوریه حزب‌الله را کنترل کند».
🔹
من فکر می‌کنم آن‌ها بهتر این کار را انجام می‌دهند. @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/442551" target="_blank">📅 14:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442550">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54dbe2cab4.mp4?token=lzIGmUKxItPq8TouqsAlnj6X-6UMXYyDKcuz3-nUHb3Od27lZz7G6OUP0NBw-6eKD1FZ2_5BAMRpZHaGr32clyeuhhij9ByOveG0aGAyEYtwTiH_uJDQaK0scoMFJcZeKqaT48hUC3udq2qp-AilynfALoYy6qH8Ch5FSndsizSp5YxdnViIVnGzWLd08AbwTQhGWsYVJZFJmILN5w5ZDQzHh0CK-f4xXS4nsTtgXO9n1iZr_Rri0vyrX2DD5_M-9RUAol3Eyy-v9L83sNx0sOTVrwW-kY8vodsN698lrym0lupnc0dxKQvqbaQ1-nshnbM2FmCWNdEh5DHgtAI3Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54dbe2cab4.mp4?token=lzIGmUKxItPq8TouqsAlnj6X-6UMXYyDKcuz3-nUHb3Od27lZz7G6OUP0NBw-6eKD1FZ2_5BAMRpZHaGr32clyeuhhij9ByOveG0aGAyEYtwTiH_uJDQaK0scoMFJcZeKqaT48hUC3udq2qp-AilynfALoYy6qH8Ch5FSndsizSp5YxdnViIVnGzWLd08AbwTQhGWsYVJZFJmILN5w5ZDQzHh0CK-f4xXS4nsTtgXO9n1iZr_Rri0vyrX2DD5_M-9RUAol3Eyy-v9L83sNx0sOTVrwW-kY8vodsN698lrym0lupnc0dxKQvqbaQ1-nshnbM2FmCWNdEh5DHgtAI3Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خانوادهٔ شهدای میناب مهمان حرم امیرالمومنین(ع) شدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/442550" target="_blank">📅 13:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442549">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57b48cc3d0.mp4?token=anS-AkSw9V8OOxLyHGpdBZUccMSHsq2VWASw0g-1oIPFWw9GyUKQqdNTOH4uIRdbr4Xaft6jJ2jkrvFF9NcaU5HyMV0hHkTeWtJElA30vZRP_-GTzsRH8VV_VZOxVEsDnJ29nmphfsz8Szu3-PiH6dnK0tzcsUvyNOCETXJPsh0Qi29unhrnH81_ajwxWlNGn5awuqUO_8apTsJxn7MXhNldFCKTEBMQAJPC2kpltDAkRBBGzod5rFCO_qTrdoTQ4uqJRRCriiaccbGkYUXYjhEtzBdV9hq7ts-Bwe6nidtEX1OYLm03G18gKhJs8oS0l2pODCcBn3cv2qrdeE_oNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57b48cc3d0.mp4?token=anS-AkSw9V8OOxLyHGpdBZUccMSHsq2VWASw0g-1oIPFWw9GyUKQqdNTOH4uIRdbr4Xaft6jJ2jkrvFF9NcaU5HyMV0hHkTeWtJElA30vZRP_-GTzsRH8VV_VZOxVEsDnJ29nmphfsz8Szu3-PiH6dnK0tzcsUvyNOCETXJPsh0Qi29unhrnH81_ajwxWlNGn5awuqUO_8apTsJxn7MXhNldFCKTEBMQAJPC2kpltDAkRBBGzod5rFCO_qTrdoTQ4uqJRRCriiaccbGkYUXYjhEtzBdV9hq7ts-Bwe6nidtEX1OYLm03G18gKhJs8oS0l2pODCcBn3cv2qrdeE_oNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الاخبار: الجولانی ‌دنبال آتش‌افروزی علیه حزب‌الله است
🔹
روزنامۀ لبنانی الاخبار در گزارشی هشدار داد دولت الجولانی با سوءاستفاده از تحولات منطقه‌ای، به‌دنبال فراهم‌کردن زمینه یک درگیری جدید علیه لبنان و انتقام‌گیری از حزب‌الله است.
🔹
طبق اطلاعات مقامات لبنانی،…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/442549" target="_blank">📅 13:45 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
