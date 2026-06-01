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
<img src="https://cdn4.telesco.pe/file/TRY9RHoJQAFMjUCquG87f7OgyzPJych4yt9PkOTgRGcT42Pm_wIQMjbADhv3Ss6NJUKqeAjj-DunTMRarIs0u9oyUtfV-Rklj4268g2Wjk1kLtHlbJGYV4Y9QbTP9Bi1LIFHtlU2xNa-i8d1bM_cFiFhwBogpWQIzeGMfVBUtzj5Ie_rwyzaAyKoQHZvKt0at9N5-gdMeTnlijbVX8ccJvzV_JezUjgmjFOLaNrKX21SV4rkwon30CJrsrrJqFJXR19EXTUI1MeufL_qWJEFQCYAmHWHsGj_32y7vRwOdilnd_A_aN-lvDIdXrJypX25nsz79XuBL4_-qggwB3LPYQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-11 13:09:42</div>
<hr>

<div class="tg-post" id="msg-439193">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwZ_HPquS1XMGkrS9ZWnry97aKAD3FK-qm-pbLpuS_QKtPHG2E3baWdUfio-XEQzrmlCfaRiIB_3k_tKRg_nivFeK3so5bOykdcdVyGUU8SjVCh1wB-5CPzbS8xVFkX18r1k735p5wYWAO_ocHmNOBvdCQsPb21lCmECAygBMLayW7YGQSKTnLsmpTHiOiEPTEyKM_3g1YAD7G_-PLh8Lh_boxtTn7JZ5HPPrAeBR3fR9uKT-5wtIoedml9XlFbwlpxbJedj3MDW6YQK5MwhKKGyLDH1pmzdNDdj6UQBCs7ad7Z9NS0cX_dXLd4gszS232hyhgTSzSveO3jK5LDOCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
آیا رقم کالابرگ تغییر می‌کند؟  @Farsna</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/farsna/439193" target="_blank">📅 13:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439192">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jelqknFEvtpUJw0Caco-VfyNgmL0jRZQHt25SvsaysL3bxbeeIc82BPvKcUs4BEssOIh8ODvBo2eHXxZ0lmGd4n1XW7NuSp_OjXWR2oH_gX7pU-bqFUpBEtt8YaumBAMFriteTmg9niIeyPmGzm4lSxuUoQsPgi2JZEHpZsKcwi3-ufdtOIevZcYE1UZtW8-tAu_-xf892F8qQUQqBYVqcWA2Jt46dUdrZ7TQeWs52iZAeKZGnE4JGVN6p6LHmWqMHCcrB8BC6ylQQYbdPWgVwSzDljtkQ-lCsN7NIEq3z3PUB1rEH6iCBWMihFA-cKm-vDDW7uxInOZkgTbLuCgXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف به آمریکا: باید هزینهٔ جنایات رژیم صهیونیستی در لبنان را پرداخت کنید
🔹
رئیس مجلس در واکنش به تشدید حملات جنایتکارانهٔ رژیم صهیونیستی در لبنان نوشت: اعمال محاصرهٔ دریایی و تشدید جنایات جنگی در لبنان توسط رژیم نسل‌کش صهیونیستی، شواهد روشن عدم پایبندی آمریکا به آتش‌بس است.
🔹
هر انتخابی، هزینه‌ای دارد و صورتحساب آن هم از راه می‌رسد؛ همه‌چیز در نهایت سرجای خودش قرار خواهد گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/farsna/439192" target="_blank">📅 12:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439191">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3c3dc9b9e.mp4?token=V3xZOQGfHMo5cZ7w55pybKnm3XY6vGEdhHEvv9dc3qE2GOC-vImNMlpt0flMTXERJz7EgTXN50ipdSro37_RiQ7ST6bSz2S1LkH4bOi3w80n8H1nK6Fd0rOAuiiiFR9mHU9oXD2aZU0wONR6ar5F2zMsw_sAJ9ibAtgBj1eH9JQubPYRNQwJp51JQ-PzM5bBEfeQeTDUUHx3Vl7QNhW9lqKHwgpNp1JcfulHweRME0caLg5FtJZdGgZLulODlONTKXqN2Pj5f-UX1COrPP5m5gx2aPj4rH_luZZ6K1wf7g6l3oXmpxjQ08XAUV2B--M3QTIEWQnWKc4ID39mpOBqQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3c3dc9b9e.mp4?token=V3xZOQGfHMo5cZ7w55pybKnm3XY6vGEdhHEvv9dc3qE2GOC-vImNMlpt0flMTXERJz7EgTXN50ipdSro37_RiQ7ST6bSz2S1LkH4bOi3w80n8H1nK6Fd0rOAuiiiFR9mHU9oXD2aZU0wONR6ar5F2zMsw_sAJ9ibAtgBj1eH9JQubPYRNQwJp51JQ-PzM5bBEfeQeTDUUHx3Vl7QNhW9lqKHwgpNp1JcfulHweRME0caLg5FtJZdGgZLulODlONTKXqN2Pj5f-UX1COrPP5m5gx2aPj4rH_luZZ6K1wf7g6l3oXmpxjQ08XAUV2B--M3QTIEWQnWKc4ID39mpOBqQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس قوه‌قضائیه: اختلاف نظرها در کشور نباید به تنازع  تبدیل شود؛ در زمین دشمن بازی نکنیم.  @Farsna</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/farsna/439191" target="_blank">📅 12:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439190">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f695ea1873.mp4?token=AwZ8WsaXMfw-LkSo6HtlxjGvC4jY_Es35DNb985nqRx3iyKvdkQA3fOmrqqbGI5wsXbsLlw75N0E4o_Sy73bUADd4biadjuYE1jmOI5UD3h4TBqatwfTMKkQRh8ATkm5JJjOerh5ULj9K48SdMxsbhV5a7_KU_GYo3yp64OO_FYBVUV-HqwQV105pjaznZ7UWnq9GHwz8ZDv4cnZocKXpriU2kYvClwicStutpvrLoT_BKFi0kD2tpM1LZTUH-Rag-C3WIzv8PkaQmxNP_MjgZL97WJNbs3tm1EvQzNMPV7GfU9q3Wbf5hZ1DVHQrhYqcm1h_sfU_Yc8jBusd8cwnTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f695ea1873.mp4?token=AwZ8WsaXMfw-LkSo6HtlxjGvC4jY_Es35DNb985nqRx3iyKvdkQA3fOmrqqbGI5wsXbsLlw75N0E4o_Sy73bUADd4biadjuYE1jmOI5UD3h4TBqatwfTMKkQRh8ATkm5JJjOerh5ULj9K48SdMxsbhV5a7_KU_GYo3yp64OO_FYBVUV-HqwQV105pjaznZ7UWnq9GHwz8ZDv4cnZocKXpriU2kYvClwicStutpvrLoT_BKFi0kD2tpM1LZTUH-Rag-C3WIzv8PkaQmxNP_MjgZL97WJNbs3tm1EvQzNMPV7GfU9q3Wbf5hZ1DVHQrhYqcm1h_sfU_Yc8jBusd8cwnTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس قوه‌قضائیه: اختلاف نظرها در کشور نباید به تنازع  تبدیل شود؛ در زمین دشمن بازی نکنیم.
@Farsna</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/farsna/439190" target="_blank">📅 12:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439189">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0543b35b60.mp4?token=nghnkCY4Wvggdrp8mLD1X_rFK_a7XP61Ojk7o5CjLShklVuFzq-OS9jihtCtQ8uJFIbIFzDGwJeENT7NbUsZDsU50rtv7sPMpcBjXO-L71N3TlEP8fnK-zghq0GVqqzZiar7EUoEQ0sjWw68AWtqlatHKLQMAWIMvLTSbix-Hzck4SB1wKBwWLELfkE0RoLNlCC6Qj0NeSBIAHte7MEc2T-4wJov9tEAhLBaMZVGue9sw6Z48NDh6-liOsZsepl9ihF5mrhq_cvo0BPFz_uJqsb4h7oytziC7Ngvl1kzws8e-l_iZkHpxZO59KZUOMguzaexC4VB8jyNIYP1jKzhwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0543b35b60.mp4?token=nghnkCY4Wvggdrp8mLD1X_rFK_a7XP61Ojk7o5CjLShklVuFzq-OS9jihtCtQ8uJFIbIFzDGwJeENT7NbUsZDsU50rtv7sPMpcBjXO-L71N3TlEP8fnK-zghq0GVqqzZiar7EUoEQ0sjWw68AWtqlatHKLQMAWIMvLTSbix-Hzck4SB1wKBwWLELfkE0RoLNlCC6Qj0NeSBIAHte7MEc2T-4wJov9tEAhLBaMZVGue9sw6Z48NDh6-liOsZsepl9ihF5mrhq_cvo0BPFz_uJqsb4h7oytziC7Ngvl1kzws8e-l_iZkHpxZO59KZUOMguzaexC4VB8jyNIYP1jKzhwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ رئیس بنیاد ملی گندم‌کاران: ۵۰ درصد پول گندم‌کاران این هفته پرداخت می‌شود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/farsna/439189" target="_blank">📅 12:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439188">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5653b7d9c4.mp4?token=Fj-HZ1w40ZJv853_7zpbWMzE97lEbmkG_rtaCioPdPIMdTg5Dhr4nrgzByQkmYrVQtskp2DXWSr1qr8WgMykGw5q0l9fR6g8dW36jEHDVvDMWd-nejaIhPDsIZruiTGekx_TlURnTO4w8BOmDFXwA04pn9KQu-NiNCAJP2dU0Vu_70ij8Vw47S9Myast4EeA5AWE-ACugiF5LLgn6TfDpvwmUnaLcgYZd7p5arhtv40rBmlP3FtwTPqm4vATujJPVhG-XWyfizbnnK_BUJWpabSvvLArmfXnMyolFjO0q38iYTHeVBvUrqhpn7GvIw2VDLTZql8yULycudONH99gznFdsYrR6vzZh2U35zHPgWZKKfQB5a35B2kU_eDGyLpr8hMsAfZyAFsFsVJ1yN5ACe8g35itz2haS9ZzhN-qyypmm8374Y4E9ni_-mHO_ERTRXYbut_lUkP3W6fgKD5qhcIW6d9Elmsp05va03nKPr-LQCrSVgUQbBGd7ZbXnrtOmJ9WRBXG4VOzLKsZA3j8_3eSAlsfXxGRDruqmjQLKZsr-dsb61sfMGIhBxt-4et3tpIsaj1XJ_q37IxpO3gJq68F9MbnNDmGAnG7PhdjC7-itYUTHbxbH9zk_MvihY3vvFromFHCFOqfuWUq6ec9UMP2EHI7QkZTMlFPMIWM4mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5653b7d9c4.mp4?token=Fj-HZ1w40ZJv853_7zpbWMzE97lEbmkG_rtaCioPdPIMdTg5Dhr4nrgzByQkmYrVQtskp2DXWSr1qr8WgMykGw5q0l9fR6g8dW36jEHDVvDMWd-nejaIhPDsIZruiTGekx_TlURnTO4w8BOmDFXwA04pn9KQu-NiNCAJP2dU0Vu_70ij8Vw47S9Myast4EeA5AWE-ACugiF5LLgn6TfDpvwmUnaLcgYZd7p5arhtv40rBmlP3FtwTPqm4vATujJPVhG-XWyfizbnnK_BUJWpabSvvLArmfXnMyolFjO0q38iYTHeVBvUrqhpn7GvIw2VDLTZql8yULycudONH99gznFdsYrR6vzZh2U35zHPgWZKKfQB5a35B2kU_eDGyLpr8hMsAfZyAFsFsVJ1yN5ACe8g35itz2haS9ZzhN-qyypmm8374Y4E9ni_-mHO_ERTRXYbut_lUkP3W6fgKD5qhcIW6d9Elmsp05va03nKPr-LQCrSVgUQbBGd7ZbXnrtOmJ9WRBXG4VOzLKsZA3j8_3eSAlsfXxGRDruqmjQLKZsr-dsb61sfMGIhBxt-4et3tpIsaj1XJ_q37IxpO3gJq68F9MbnNDmGAnG7PhdjC7-itYUTHbxbH9zk_MvihY3vvFromFHCFOqfuWUq6ec9UMP2EHI7QkZTMlFPMIWM4mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر یکی از عملیات‌های گشت و کنترل تنگۀ هرمز توسط شناورهای تندوری نیروی دریایی سپاه طی روزهای گذشته
@Farsna</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/farsna/439188" target="_blank">📅 12:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439187">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac59e86c7d.mp4?token=hNNcgkltGJJL__o31en0BZCaR4EFdrdtDNzawFwoNW3_QwSd-u3zz4unjbK7Ro6cn9VRjL8GbQbTnNL0KWB4emfIWSX59NK41XtWNksRbVfLSRTADp0c_Yz-gb066O2g6R0PxgYNuzImOnLrIpD5YygNSOOfwX_0H6KIR7TvsuAbX38WbzMkA9a2ulJuWZMzTpez-9GvwkjCp-P_VdbNuexZ0KNJpGG72tykrwBBQri8f6SYr8hvVm1M98Pkf6MlpZbSwWnyR3OfcinIG89L3jBi6Antu4cPr9i-Odgl226P_kLKPNRWRmmUe_EMSY2r3L-qPHJVyERscrsZLGt_Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac59e86c7d.mp4?token=hNNcgkltGJJL__o31en0BZCaR4EFdrdtDNzawFwoNW3_QwSd-u3zz4unjbK7Ro6cn9VRjL8GbQbTnNL0KWB4emfIWSX59NK41XtWNksRbVfLSRTADp0c_Yz-gb066O2g6R0PxgYNuzImOnLrIpD5YygNSOOfwX_0H6KIR7TvsuAbX38WbzMkA9a2ulJuWZMzTpez-9GvwkjCp-P_VdbNuexZ0KNJpGG72tykrwBBQri8f6SYr8hvVm1M98Pkf6MlpZbSwWnyR3OfcinIG89L3jBi6Antu4cPr9i-Odgl226P_kLKPNRWRmmUe_EMSY2r3L-qPHJVyERscrsZLGt_Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: با عمانی‌ها صحبت کردیم و آن‌ها هم دربارهٔ تنگهٔ هرمز نگرانی‌های مشترکی با ما دارند.  @Farsna</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/farsna/439187" target="_blank">📅 11:53 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439186">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W67QbgS5L088evCdFOaY4nCE0s997nNSWZq2pOGcXvRpctKCXIbIXgWZ1IxTWJ2NxJC6sGCMNesVK6FexvixPUMfZKLVFlJvknjvFn24yPDm10wB_Gb6lZJY5cKdBGAufSSb6FkMBkUEXzhm3B9ghkROh4q65-eE-pFVscMkFKY3RScmtwpvBK75QnynMCSrk8csgADe6muvbzjXE_0mf2RizI5LktKgGKRhsV6M7Ei6TdAfEryTqAU_M_wpUImfMbbfevGF7WF2ZObirDefBZh8yyS-auVkxUrAuwJKzN6XVC7HQxFyKnu9VZ92WjL9fW45xXFMdFSj3YS7jAoUcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آزادراه هوشمند تهران در آستانهٔ بهره‌برداری
🔹
ساخت فاز اول آزاد‌راه شهید شوشتری که مجهز به سامانه‌های هوشمند است با طول ۹ کیلومتر به ‌اتمام رسید.
🔹
این فاز محدودهٔ بزرگراه امام رضا(ع) در جنوب شرق تهران را به شمال استادیوم تختی، بلوار هجرت و بزرگراه بسیج وصل می‌کند و ضمن کوتاه‌تر کردن مسیرهای تردد، بخشی از بار ترافیکی بزرگراه بسیج را هم کاهش می‌دهد.
@Farsns
-
Link</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/farsna/439186" target="_blank">📅 11:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439185">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cff7c45be.mp4?token=OA2w3AtKZ4px2RvWVq5TG-FiKt67v48NwUnTaGdxByG2KAI0kLIO96JDGB2Fv9F85FK_CvKZ2ECY-jLldn38slDZCeAXUrXZNhuPpvF0pSaZ2zf_g5uqz-CpluXD6b_0BNPgrQQKB1HDqg8RSa7lBwvDEfAjq0aexsGQKxjvfhHfja-8Bz5wvrmjQ7c049Fc7izrrW06USyNn1j-hAYJMSA7F2YeIygl91Cva1UbFGV9dRh5RlHEBr8vT62-WoCP7YjorgnNPSTo79X1OtTHAGBmTdmRjCRznuH9meBToTlXDwa3U2MkfC11hJW1ln28OY0fv4QtIcZAJBoxGksIuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cff7c45be.mp4?token=OA2w3AtKZ4px2RvWVq5TG-FiKt67v48NwUnTaGdxByG2KAI0kLIO96JDGB2Fv9F85FK_CvKZ2ECY-jLldn38slDZCeAXUrXZNhuPpvF0pSaZ2zf_g5uqz-CpluXD6b_0BNPgrQQKB1HDqg8RSa7lBwvDEfAjq0aexsGQKxjvfhHfja-8Bz5wvrmjQ7c049Fc7izrrW06USyNn1j-hAYJMSA7F2YeIygl91Cva1UbFGV9dRh5RlHEBr8vT62-WoCP7YjorgnNPSTo79X1OtTHAGBmTdmRjCRznuH9meBToTlXDwa3U2MkfC11hJW1ln28OY0fv4QtIcZAJBoxGksIuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر رفاه: کالابرگ خردادماه به روال ماه‌های قبل پرداخت می‌شود
🔹
بخش‌های مختلف دولت مانند سازمان برنامه به‌دنبال منابع جدید برای کالابرگ هستند، اما هنوز منابع جدیدی نداریم.
🔹
در مذاکراتی که با صنایع لبنی داشتیم، قرار است مواد لبنیاتی کالابرگ با ۱۰ درصد تخفیف…</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/farsna/439185" target="_blank">📅 11:46 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439184">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b145f3b466.mp4?token=kJJmup7p024ZCuZchBVHzXmW8lvwrsjsAA0pFgzKZgMZ5UqIaFR81AFMh6ABeZLRf-IJBzC2Qsl5RrrcAJg0vqQzOGXaUIOHuXWKIjY-b3w4NkcV4F_-CcO3kvn2_FA_LZJGeJYjKdQjzq6tD3NqsQQ7dWBgHfkEgL-yeAXPgSnI2a2Qb6PUdNthlxwCH4UEuSQQv92n-4BTQ22KcC20VHBPMHR4duftFoLzTLt7JO1LytJZFA6fAIAAwncRjjpCwQuwKLsaLrv3AEV2qDTRL32eP6NtprRCMXLj5DRvM5r4QwTkmYNJoXASqYVX4JmEOKj_6jyfjoyOrxKAy33G-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b145f3b466.mp4?token=kJJmup7p024ZCuZchBVHzXmW8lvwrsjsAA0pFgzKZgMZ5UqIaFR81AFMh6ABeZLRf-IJBzC2Qsl5RrrcAJg0vqQzOGXaUIOHuXWKIjY-b3w4NkcV4F_-CcO3kvn2_FA_LZJGeJYjKdQjzq6tD3NqsQQ7dWBgHfkEgL-yeAXPgSnI2a2Qb6PUdNthlxwCH4UEuSQQv92n-4BTQ22KcC20VHBPMHR4duftFoLzTLt7JO1LytJZFA6fAIAAwncRjjpCwQuwKLsaLrv3AEV2qDTRL32eP6NtprRCMXLj5DRvM5r4QwTkmYNJoXASqYVX4JmEOKj_6jyfjoyOrxKAy33G-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: حمایت از محیط‌زیست در تنگهٔ هرمز بسیار مهم است و هزینه‌هایی دارد که دریافت می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/farsna/439184" target="_blank">📅 11:44 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439183">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb5ddf5a05.mp4?token=c5Rto-fnkNpMrCGpQKUBOjXd_7_2EqRk_bUnsuCrP-w2nh1iLMtVhQZiR9v-ijsL7EQ-3AJKEB0RxZZS7xgxSr88aq_wIrzmSX_nCAwcMgSU0V2bsyZONPAOujgA-VyzyqdGVcvz8zkwrZIDJdUTn49lhmd6oyohgClo7Pir3ngVCyHmfvPjMyWO1l8KqkhUVfBpVAhi-0ONt86B1alasNlm1cL9Dx2o6F56FhiIcN9rNxDq6BjykW4ThINK-6hPLQ-8Iw4yEvgfCoJjbQW0OTrdRNOHYtFN-TkydnxrQ1dhAaztrHEOhLaCWBrDI9wvCwH22yIInLM9HkkyQYn6Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb5ddf5a05.mp4?token=c5Rto-fnkNpMrCGpQKUBOjXd_7_2EqRk_bUnsuCrP-w2nh1iLMtVhQZiR9v-ijsL7EQ-3AJKEB0RxZZS7xgxSr88aq_wIrzmSX_nCAwcMgSU0V2bsyZONPAOujgA-VyzyqdGVcvz8zkwrZIDJdUTn49lhmd6oyohgClo7Pir3ngVCyHmfvPjMyWO1l8KqkhUVfBpVAhi-0ONt86B1alasNlm1cL9Dx2o6F56FhiIcN9rNxDq6BjykW4ThINK-6hPLQ-8Iw4yEvgfCoJjbQW0OTrdRNOHYtFN-TkydnxrQ1dhAaztrHEOhLaCWBrDI9wvCwH22yIInLM9HkkyQYn6Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: قطعنامه شورای امنیت برای ما تضمین نیست
🔹
در تفاهم اولیه یک بند دربارهٔ صدور قطعنامهٔ شورای امنیت در صورت توافق وجود دارد اما معنایش این نیست که ما قطعنامهٔ شورای امنیت را تضمین می‌بینیم.
🔹
صدور این قطعنامه صرفاً برای پوشش حقوقی توافق…</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/farsna/439183" target="_blank">📅 11:43 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439182">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b04cce048.mp4?token=eApm3QgPlEyC9zbDx4sopujQt7F5XE--O8JXsKtYfDwGk-AiBjDpbHyTMEad6NuZknjs44xZkfJ5LAfSlgA9Xh6igvsA3mgvPKFeXHa-DoRxKB38F0bd5cGqkuZvYL0uJgrGzUJJ3LzvSbH-JAhJWJlNNRxARYmtxMB3Gwae8g7zLv-iNJ6C6aHvTl5rnvWrTdDwNSu0Kn6Xk1JaN3qgCt5DS5GoYdCPfCmW7CD1oTXYB4BTU-rncEv_39CVSDEcIKJzy-m56M_ut5vnVJQIE2mEHS5PMl7K0_hq30vGCJTzWmQZF441UIBZzki1YRj230GGtMtRMpG6d5SGbZkWkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b04cce048.mp4?token=eApm3QgPlEyC9zbDx4sopujQt7F5XE--O8JXsKtYfDwGk-AiBjDpbHyTMEad6NuZknjs44xZkfJ5LAfSlgA9Xh6igvsA3mgvPKFeXHa-DoRxKB38F0bd5cGqkuZvYL0uJgrGzUJJ3LzvSbH-JAhJWJlNNRxARYmtxMB3Gwae8g7zLv-iNJ6C6aHvTl5rnvWrTdDwNSu0Kn6Xk1JaN3qgCt5DS5GoYdCPfCmW7CD1oTXYB4BTU-rncEv_39CVSDEcIKJzy-m56M_ut5vnVJQIE2mEHS5PMl7K0_hq30vGCJTzWmQZF441UIBZzki1YRj230GGtMtRMpG6d5SGbZkWkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: سفر هیئت مذاکره‌کننده به قطر مثبت بود
🔹
میانجی مذاکرات همچنان پاکستان است. در سفر هیئت مذاکره‌کننده به قطر برخی از جنبه‌های مالی توافق خاتمهٔ جنگ بررسی شد. @Farsna</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/farsna/439182" target="_blank">📅 11:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439181">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c2535b069.mp4?token=fqGFGy4cLzrzezYDl1t_7kKiMv0AH1LN-begrqzjpxm0J0WU95ElM5mFrl6Fb8lnab67av_i-sVnTMoCKy8Mla1t4H5hzw6M8dpcBS9L3sJjuusBkP7VmcXtK1qATW1A_GcBlcjTuFoKVc4P_5bADt2xwL_89F-5sEcZ3kq14Sggf3FOzlod2zymiNdl44tm-B3uzCKSKdSmfzatoz0SEQwy9YYHjyhLMtAbI72OOq0l24tWkwg0WaQ5XNa8acrh3hvs-vL4z_DIMbZRu-bAFkxTeJt4UNWQlyzIKhtuENuZAPu86vDN1Of_pvopnNpS25ZTk299iv7KEk5X5S9XrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c2535b069.mp4?token=fqGFGy4cLzrzezYDl1t_7kKiMv0AH1LN-begrqzjpxm0J0WU95ElM5mFrl6Fb8lnab67av_i-sVnTMoCKy8Mla1t4H5hzw6M8dpcBS9L3sJjuusBkP7VmcXtK1qATW1A_GcBlcjTuFoKVc4P_5bADt2xwL_89F-5sEcZ3kq14Sggf3FOzlod2zymiNdl44tm-B3uzCKSKdSmfzatoz0SEQwy9YYHjyhLMtAbI72OOq0l24tWkwg0WaQ5XNa8acrh3hvs-vL4z_DIMbZRu-bAFkxTeJt4UNWQlyzIKhtuENuZAPu86vDN1Of_pvopnNpS25ZTk299iv7KEk5X5S9XrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: ما حق دفاع مشروع در برابر نقض آتش‌بس توسط آمریکا را داریم و امروز هم مبدأ تجاوز به خاک کشور را هدف قرار دادیم.  @Farsna</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/farsna/439181" target="_blank">📅 11:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439180">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9tAxesljl5lexQz-fD8ur45LntaB1Sz54R8x37GWnERKxP0bJD-JLN4-P2-IMaUqcHVU8PJE1F7aZN5aaQgdQ6AfAF7gJpsXgRbWabBGbD03v6YNn0hFEY_2QPICXbO1G1WC0y80hLtualDrRkhUIPsyRfoD1rLOm9_S11KN1R7M18xqNhGF6JfSiN8GO7jAhzonNbuoLcaIcIYfb6-QzM5fEbHIUmoWtiM7Ob-Fo23POpGc9bCs_awP6cDIl6_zm3uarq9pPZ7f5U9dHpDsmrhoUDs8fl3113oTIQcG7XvevtUXQ5FQdCBheIiw_lwSxMPhxfsRXiC8jctdkmwiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان حمایت: افزایش قیمت مدیران خودرو غیرقانونی است
🔹
در‌پی اعلام شرکت مدیران خودرو مبنی‌بر افزایش حدود ۸۰ درصدی قیمت محصولات خود، سازمان حمایت از حقوق مصرف‌کنندگان اعلام کرد این افزایش قیمت قانونی نیست و فاقد اعتبار است.
🔹
براساس دستورالعمل مورخ ۱۴۰۴/۶/۱۱ شورای رقابت، تمامی عرضه‌کنندگان خودرو موظف‌اند مدارک خود را جهت تعدیل قیمت به سازمان حمایت ارائه کنند تا پس از بررسی‌های لازم، قیمت‌های جدید محاسبه و ابلاغ شود.
🔹
با این حال، این شرکت بدون هماهنگی و به‌صورت خودسرانه اقدام به افزایش قیمت کرده؛ درحالی که استعلامات و بررسی‌های قانونی این شرکت هنوز تکمیل نشده.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/farsna/439180" target="_blank">📅 11:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439179">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a4848aa7a.mp4?token=dQj2pHBNuubCCg7-lpf8p7qqGSCFfVnu6QgdjFTJZnR9B678AXKYMwCb5SqbBa2or1L2ibZOqL9xwLQ4KQfwHbtIOVvlJmMDj2NZyYNuDfeOHOIM8bHPC276Eaiy_iSFbtOERtzgcETkOryf1m3tSLKA6PYvfHfGK6w_I6tX5aDZStL_SsD142eSWGlG9eberScnpJZDT-_JWVULe2KSns-BVr8JDStQOKz5MPAlcxGsZ0XCbiYVOFpAxpt4ZUI6Xt9aUoEuz9weitmWdKu2-JBRKdoW12gVs5gdK4Nw5qrk4Z7K5V1YXs4LYfaGqNU9_EsDpf6MJvt3qzCsKeVKHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a4848aa7a.mp4?token=dQj2pHBNuubCCg7-lpf8p7qqGSCFfVnu6QgdjFTJZnR9B678AXKYMwCb5SqbBa2or1L2ibZOqL9xwLQ4KQfwHbtIOVvlJmMDj2NZyYNuDfeOHOIM8bHPC276Eaiy_iSFbtOERtzgcETkOryf1m3tSLKA6PYvfHfGK6w_I6tX5aDZStL_SsD142eSWGlG9eberScnpJZDT-_JWVULe2KSns-BVr8JDStQOKz5MPAlcxGsZ0XCbiYVOFpAxpt4ZUI6Xt9aUoEuz9weitmWdKu2-JBRKdoW12gVs5gdK4Nw5qrk4Z7K5V1YXs4LYfaGqNU9_EsDpf6MJvt3qzCsKeVKHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: پول‌هایی که ایران در برجام دریافت کرد، اموال مسدودشده و حق مردم ایران بود
🔹
حالا هم به‌دنبال احقاق حقوق مردم ایران هستیم و هنوز دربارهٔ سازوکار یا نحوهٔ دریافت اموالِ به‌ناحق مسدودشدهٔ ایران تفاهمی انجام نشده است. @Farsna</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/farsna/439179" target="_blank">📅 11:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439178">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50678b3be7.mp4?token=WXA93DN5HXCnc72eWU1xTwatuY0-bgoDa99_szsGdEhiQIxk4Wpa2kluD4kIGF8kMjJ76FNlvmpwyiSw8cqcIp3Ig57Uf-VuCxqT7hqVOZGdr0xm2rUVtvsbHolyGRt5-362A7NT12l76rRQCKxoG9twWXpfXASNnhBDgwtiKBHXwxlRECe1e9Z6XdqDoOn_wsYuTiKJLXeVZfIZ6s8rovQlmDM4Hw_bYIflKaCcNTb7ihisJdToYRK0CJcuIHMol7VbXGHhFjnulLBVTZh8NvGNFmArB5q1UdvyLmIrU2_Os63H__OtfYM8LjgdQTL-KJxrxKS0NI34MAyj23chwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50678b3be7.mp4?token=WXA93DN5HXCnc72eWU1xTwatuY0-bgoDa99_szsGdEhiQIxk4Wpa2kluD4kIGF8kMjJ76FNlvmpwyiSw8cqcIp3Ig57Uf-VuCxqT7hqVOZGdr0xm2rUVtvsbHolyGRt5-362A7NT12l76rRQCKxoG9twWXpfXASNnhBDgwtiKBHXwxlRECe1e9Z6XdqDoOn_wsYuTiKJLXeVZfIZ6s8rovQlmDM4Hw_bYIflKaCcNTb7ihisJdToYRK0CJcuIHMol7VbXGHhFjnulLBVTZh8NvGNFmArB5q1UdvyLmIrU2_Os63H__OtfYM8LjgdQTL-KJxrxKS0NI34MAyj23chwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عقاب آسمان ایران که هیچ مأموریتی را نیمه‌کاره نگذاشت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/farsna/439178" target="_blank">📅 11:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439177">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d4b61af2e.mp4?token=eb642rFtcygBPdPVwLq-T8W4633kaDljETk5qvStjduFVK_FSg2oqhr8zsCTSaMIRJYHd41WL4bGusZ8NQ4noTmvnbH-NXH79UxMDgUPzy1-gZCVi8QIDGveaGAWgLr9dDdHmeo6ZJ1380VxGeCDJrMSDt50BkCRERBUXgcNU86XofpC_fyUtDrxhkm7XYaebFzRYBry3pwnlmjg1LWjEdD71VpYNHF4GPIbe7IWgx9uvv1kC9jTOWqrbTMR4Uzd7slEJFS83bzrQezwk0pQEtcvaFZJep_MTleaWjEo5xVdmJUp-1HiM3DgI8eIa6_eMDp9lIwV0AZQtob0egM31g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d4b61af2e.mp4?token=eb642rFtcygBPdPVwLq-T8W4633kaDljETk5qvStjduFVK_FSg2oqhr8zsCTSaMIRJYHd41WL4bGusZ8NQ4noTmvnbH-NXH79UxMDgUPzy1-gZCVi8QIDGveaGAWgLr9dDdHmeo6ZJ1380VxGeCDJrMSDt50BkCRERBUXgcNU86XofpC_fyUtDrxhkm7XYaebFzRYBry3pwnlmjg1LWjEdD71VpYNHF4GPIbe7IWgx9uvv1kC9jTOWqrbTMR4Uzd7slEJFS83bzrQezwk0pQEtcvaFZJep_MTleaWjEo5xVdmJUp-1HiM3DgI8eIa6_eMDp9lIwV0AZQtob0egM31g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: ما با مردم کویت و سایر مردم منطقه که خاکشان مبدأ حمله به ایران است، ابراز هم‌بستگی می‌کنیم
🔹
بیانیهٔ اتحادیهٔ اروپا در حمایت از کویت، مصداق ریاکاری است؛ نمی‌شود حملهٔ غیرقانونی آمریکا و اسرائیل به ایران را نادیده گرفت اما پاسخ ایران را…</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/farsna/439177" target="_blank">📅 11:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439176">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4g8QmxsZPqD5_D8z9VIj5Hrj0CgsEuudPKBGFaGlperWmxkXnYQxNOqMeXMyRycdDRaCZqGRtfk84Ww9nxsyretCsX-mjn1pkuAVLrT70ImK_6cHM7asEgBHjW4itjrsMzZ-pw8bzC_w2KtEqE_gWOJor-um1r454p2pLSjd7e2z5rpIUfNvSM3YXLrzWgZ7igVoYBfXqFfMYzJy4eRy51pV2q4pDqU41kc4Y0qcWIV1eejoImU_2_nhhvjW7WKwdSeZ9l6V1jI59upehut1T5XKOUat-1T_oSYxjfGE5OHSUC2Xu1hpWsZfGEj6l07GkuvDpCMjcjtMrXuuTCocw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
افزایش اجاره دادِ مستاجران را  درآورد  @Farsna</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/farsna/439176" target="_blank">📅 11:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439175">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ab32b38bd.mp4?token=peUSz9hcBV45crlr8ITln8gul0x8nIDiJT22j03EEM_1jso9oXcZDfKqX-Q0fOm9X4FmdMe-oUTjcUxeaXZ4D0W94JnEIh_bWn3RM576xJYAZGn2S_ukrVHMcbI1vJ9yMZmKFNqr8v_p_myx4r1SKEuQ3_V_fF4H3EcEtUXy0z_D-91Pk5ZVB8sArYovacUFJ09hLxSdamR_SCEw50S9niHm-0uqUdhGpOI8KQEMMoeikPMIKc5GG3mbBZFMEdvTn1h4-CbF0hHcQwdmKMlvyrkTAs1k2uNzxTPts3jOkl_oo-MOXkhJ1044yL0nnTUhl7DN1DxFKTeiWrez4hojzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ab32b38bd.mp4?token=peUSz9hcBV45crlr8ITln8gul0x8nIDiJT22j03EEM_1jso9oXcZDfKqX-Q0fOm9X4FmdMe-oUTjcUxeaXZ4D0W94JnEIh_bWn3RM576xJYAZGn2S_ukrVHMcbI1vJ9yMZmKFNqr8v_p_myx4r1SKEuQ3_V_fF4H3EcEtUXy0z_D-91Pk5ZVB8sArYovacUFJ09hLxSdamR_SCEw50S9niHm-0uqUdhGpOI8KQEMMoeikPMIKc5GG3mbBZFMEdvTn1h4-CbF0hHcQwdmKMlvyrkTAs1k2uNzxTPts3jOkl_oo-MOXkhJ1044yL0nnTUhl7DN1DxFKTeiWrez4hojzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: یکی از بخش‌های تفاهم، ایجاد شرایطی برای بازسازی خسارت‌های جنگ است
🔹
یکی از راه‌هایی که در این مرحله دربارهٔ آن صحبت شده، اختصاص یک مبلغ برای بازسازی خسارت‌هاست. @Farsna</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/farsna/439175" target="_blank">📅 11:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439174">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">رئیس دادگستری سمنان:  اموال ۱۸ تن از عناصر مرتبط با سرویس‌های جاسوسی در خارج از کشور توقیف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/farsna/439174" target="_blank">📅 11:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439173">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e85453ef3.mp4?token=nxvnI5SmqdH9NE65QOrc1Y8jo8D_ODV9eJvQEjzVVpL6Seqc_SzD0fDrr_gDDVpaiN0pvToKrVjk5bqHJhnd53GFJUz6D2gq-9DtQdmXeJxeLIjsg6i_jbj_ymHI8pQ8jeApXP2ImeTFv5tPC1JZ2v8FMYyQZr2WFeiA5pJ7-HLGEvLUn1NX7fWOnZwVStM50WKOHqLz-rKXC2lNo6T3M0mLpkYD4LmCjI9CihvLpM0gP6SksHpBRay_69414Fg0lDPr2WfMNLRgNsRJCCpG9BKGq_70dqcKGmm79iBJsEKCXMbopuu_g69tX_hw79fiEL-faoBxLrX8eydyn994_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e85453ef3.mp4?token=nxvnI5SmqdH9NE65QOrc1Y8jo8D_ODV9eJvQEjzVVpL6Seqc_SzD0fDrr_gDDVpaiN0pvToKrVjk5bqHJhnd53GFJUz6D2gq-9DtQdmXeJxeLIjsg6i_jbj_ymHI8pQ8jeApXP2ImeTFv5tPC1JZ2v8FMYyQZr2WFeiA5pJ7-HLGEvLUn1NX7fWOnZwVStM50WKOHqLz-rKXC2lNo6T3M0mLpkYD4LmCjI9CihvLpM0gP6SksHpBRay_69414Fg0lDPr2WfMNLRgNsRJCCpG9BKGq_70dqcKGmm79iBJsEKCXMbopuu_g69tX_hw79fiEL-faoBxLrX8eydyn994_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بقایی در واکنش به ادعای ترامپ دربارهٔ خارج‌کردن اورانیوم از ایران: ما دربارهٔ جزئیات موضوع هسته‌ای هیچ مذاکره‌ای نکرده‌ایم.  @Farsna</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/farsna/439173" target="_blank">📅 11:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439172">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3b8296f4a.mp4?token=O2xNVSqbWj3su_qTENpdHKwf9L8A3DsPtAkKrPdeNSV1uO2smdp0Tn5SLilOsOTtmWCtoyrx30XLktlgojUsOebTxP3DWq8T5TPQg2y-VcodxIJZhBA6_8X5uuS0RE-gYFtul7YoGRv6LuPXyUePD75ri-0nrPgpngZtYKcbz95uHKg0U_j8kkXClBpCRk9mH14sioYu5lL8r183KrR_BC-TIfsy3Dn2ephQlMcztoX0yVM9yIobPcKmdaU0wktpkDQ7WWPsIfq8Q84iDkCwmlQ60pB1JGnL4qUAQSR3-U8wSEvhJ6UkAyfe5Kn3pBnhV1endQ1a7uide27S8PpYhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3b8296f4a.mp4?token=O2xNVSqbWj3su_qTENpdHKwf9L8A3DsPtAkKrPdeNSV1uO2smdp0Tn5SLilOsOTtmWCtoyrx30XLktlgojUsOebTxP3DWq8T5TPQg2y-VcodxIJZhBA6_8X5uuS0RE-gYFtul7YoGRv6LuPXyUePD75ri-0nrPgpngZtYKcbz95uHKg0U_j8kkXClBpCRk9mH14sioYu5lL8r183KrR_BC-TIfsy3Dn2ephQlMcztoX0yVM9yIobPcKmdaU0wktpkDQ7WWPsIfq8Q84iDkCwmlQ60pB1JGnL4qUAQSR3-U8wSEvhJ6UkAyfe5Kn3pBnhV1endQ1a7uide27S8PpYhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: کویت هنوز امکان دسترسی کنسولی سفارت به ۴ شهروند دستگیرشدهٔ ایرانی را ایجاد نکرده است
🔹
اجازه‌دادن به طرف‌های متجاوز برای اقدام علیه ایران از سوی دولت‌های منطقه، آن‌ها را کنار طرف‌های متجاوز خواهد نشاند. @Farsna</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/farsna/439172" target="_blank">📅 11:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439171">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19d2e52790.mp4?token=bfzW_f3mmeRa23CQGs6tCsVCz0W_kRCY6oGTElvv2XRIg-kHov8WdoebpjZCvbtwIt7BuX13sjpV3skVAeV5dgNaioG4U0SFhOndwJBnT_caEwF8n9XGb3wE3PPOM2kxOtMfw7nZz1Dsf1YJw2GZqWKBVJxKyYhz7D1eY-9PA1EaIFUrczeL0NopB8IyfrFeb9b8V-S8mvZvaO2vp5N2n6AUfxav3CsCwIbROIi-lKwlBmty7m52ROM8VOqo0uhMR_uqa0HbQ9kTrfi9riNjhnj26OBfgp3UNw4voJxsU99B19bsA3oT20OuV8pntxsckQ_t4rf7ItB4dU7udc2L0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19d2e52790.mp4?token=bfzW_f3mmeRa23CQGs6tCsVCz0W_kRCY6oGTElvv2XRIg-kHov8WdoebpjZCvbtwIt7BuX13sjpV3skVAeV5dgNaioG4U0SFhOndwJBnT_caEwF8n9XGb3wE3PPOM2kxOtMfw7nZz1Dsf1YJw2GZqWKBVJxKyYhz7D1eY-9PA1EaIFUrczeL0NopB8IyfrFeb9b8V-S8mvZvaO2vp5N2n6AUfxav3CsCwIbROIi-lKwlBmty7m52ROM8VOqo0uhMR_uqa0HbQ9kTrfi9riNjhnj26OBfgp3UNw4voJxsU99B19bsA3oT20OuV8pntxsckQ_t4rf7ItB4dU7udc2L0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: مواضع متناقض آمریکایی‌ها دلیل طولانی‌شدن روند دستیابی به تفاهم است
🔹
آمریکا مسئول جنایات رژیم صهیونیستی در لبنان است. @Farsna</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/farsna/439171" target="_blank">📅 10:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439170">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bc3f7ae84.mp4?token=rOr_0Tj4RhthrHZGTx7-phwC0RbIzmyr5MsVJcD6F7Fq3Bp52kacTQQA2xWGtErEuVvxDkTfZiWNu99MLA-e-uyqgDGZeu8OMtobCymv753b42vET896LPfL8PlmKkS-GHDAcFrxadzbvEP6Of0gnRZ_OTtc0-OiygaeVwvBBVKpL0EKsX5kEkduDFxiqdH8Kk1F-n6j-iigTfXSCmZM0SzLN7uo8vhmPGnehm4StMBt1-j8cbMZmIjehPmqghGaHyR5iRYY8_wUR0sb12dzxnY07xq0Ft1x6cijVFizo6OB1Ia-8cWHnrRHTQLIAVjkerSGP-K2XMeW6iNx6XCCtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bc3f7ae84.mp4?token=rOr_0Tj4RhthrHZGTx7-phwC0RbIzmyr5MsVJcD6F7Fq3Bp52kacTQQA2xWGtErEuVvxDkTfZiWNu99MLA-e-uyqgDGZeu8OMtobCymv753b42vET896LPfL8PlmKkS-GHDAcFrxadzbvEP6Of0gnRZ_OTtc0-OiygaeVwvBBVKpL0EKsX5kEkduDFxiqdH8Kk1F-n6j-iigTfXSCmZM0SzLN7uo8vhmPGnehm4StMBt1-j8cbMZmIjehPmqghGaHyR5iRYY8_wUR0sb12dzxnY07xq0Ft1x6cijVFizo6OB1Ia-8cWHnrRHTQLIAVjkerSGP-K2XMeW6iNx6XCCtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: مواضع متناقض آمریکایی‌ها دلیل طولانی‌شدن روند دستیابی به تفاهم است
🔹
آمریکا مسئول جنایات رژیم صهیونیستی در لبنان است.
@Farsna</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/farsna/439170" target="_blank">📅 10:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439169">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aso7RHtaLs5vJZ5Vi2-pbnRQF3IawlepiD3gpFCaztj2RBhL2_gsmWpUg-4xKDlUPEq7QAv87cqM20cAuPXSCkBYPZB5PK8ZMYW-ezqK3LI41JkbAbOIkyMpjFeRYZjpZovsbEU5lglZxO9mKiPVfwHx6ILnFynQi4rKrZn4ReiM-IM9T_aHduJyjmkmYjrTEJOqZ8P1ffZ0mK04bdJHOaXe8D_RgyKOP3ATGME3sD3T2eaRk-UsHtA7PBCe1SmsOb74T0uWjCVEQ3kYQDAI6rsiK1rotl-SrqaV8GnGNRRwo4zTer9Aw13i-ivexhn3O_G8B1k2Cp_cKtNwRJRSLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ بخشنامهٔ افزایش حداقل دستمزد کارگران منتظر ابلاغ است
🔹
با وجود اینکه عضو شورای‌عالی کار گفته بود احتمالاً بخشنامه افزایش حداقل حقوق کارگران در سال جاری روز چهارشنبه ابلاغ می‌شود، اما بعد از برگزاری جلسه شورای‌عالی کار در سال جاری این بخشنامه هنوز برای اجرا…</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/farsna/439169" target="_blank">📅 10:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439168">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e9ea95ff4.mp4?token=vvN0eixjbEnSWP-LAZpAvM7F34JWuudgGzVG9MghFktsINoZHFq3IYrI3G1Y2-UGxa1WRDH_k67hBeKejW1g9Sw86IYAN2wtAfnU8-mBHx12kjJZX4vBD1jZwiGyi53B4ys1dVoRJ6hWnwQD7u4VZKqlnPhodziIWWPfgT1MsUpaZhIVuWf8hUeq9KsPlL_cL9Y_rXcihAUgIeylKRxxotVVIyFAHga5CN13ZepMlM65uNv8nv69yaPOYLpwOurvplUl6WzSIb-V4TdmsNhwfmYacEvGSj-89WR4zlB0Gf_4HWjoURnf1w0Zk70ezB0E7-OhU8ia0vD97WooWEWKBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e9ea95ff4.mp4?token=vvN0eixjbEnSWP-LAZpAvM7F34JWuudgGzVG9MghFktsINoZHFq3IYrI3G1Y2-UGxa1WRDH_k67hBeKejW1g9Sw86IYAN2wtAfnU8-mBHx12kjJZX4vBD1jZwiGyi53B4ys1dVoRJ6hWnwQD7u4VZKqlnPhodziIWWPfgT1MsUpaZhIVuWf8hUeq9KsPlL_cL9Y_rXcihAUgIeylKRxxotVVIyFAHga5CN13ZepMlM65uNv8nv69yaPOYLpwOurvplUl6WzSIb-V4TdmsNhwfmYacEvGSj-89WR4zlB0Gf_4HWjoURnf1w0Zk70ezB0E7-OhU8ia0vD97WooWEWKBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توقیف نفتکش روسیه توسط فرانسه
🔹
رئیس‌جمهور فرانسه اعلام کرد که با حمایت انگلیس و چند شریک دیگر خود، تانکر «تاگور» روسیه را در اقیانوس اطلس توقیف کرده است.
🔹
مکرون در توجیه این اقدام گفت: «دورزدن تحریم‌های بین‌المللی، نقض قانون دریا و تأمین مالی جنگی که روسیه بیش از ۴ سال است علیه اوکراین به‌راه انداخته، برای کشتی‌ها غیرقابل قبول است. این کشتی‌ها که از رعایت اساسی‌ترین قوانین ناوبری دریایی سر باز می‌زنند، تهدیدی برای محیط زیست و امنیت همه نیز محسوب می‌شوند.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/farsna/439168" target="_blank">📅 10:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439167">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2ed333f21.mp4?token=LOwi4fvVXATS62iHA9DtyR43iXq3CgZb0X_i3ReJvO0QS2ezm5wM-0TmoF-icS4Qj4CJuDzZ5SloiftByiYOXys_0zWRPgvp0QfAY2gJPzEvtLDPmG5ozqhLQ2uC-yUXu6S3tCV7D_ISG5tbctwD1Xtaaa894e4ghm48RljbnUFFhcJHTlMTSu4CgF52Rma3RQGE4AI6bWaeDWCpU9shyPNE0vGjulCoTn_TZIIDEI_muQwosC6VNXWd64CKXCOwW-08mqgXiLuNbEiSf1gUYFAGP1YvxM2Oz5Oa1ydS7aMKaMbbjhBXBmOty0UbNVy_PPl8_b4edqVb_A9QMy7s0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2ed333f21.mp4?token=LOwi4fvVXATS62iHA9DtyR43iXq3CgZb0X_i3ReJvO0QS2ezm5wM-0TmoF-icS4Qj4CJuDzZ5SloiftByiYOXys_0zWRPgvp0QfAY2gJPzEvtLDPmG5ozqhLQ2uC-yUXu6S3tCV7D_ISG5tbctwD1Xtaaa894e4ghm48RljbnUFFhcJHTlMTSu4CgF52Rma3RQGE4AI6bWaeDWCpU9shyPNE0vGjulCoTn_TZIIDEI_muQwosC6VNXWd64CKXCOwW-08mqgXiLuNbEiSf1gUYFAGP1YvxM2Oz5Oa1ydS7aMKaMbbjhBXBmOty0UbNVy_PPl8_b4edqVb_A9QMy7s0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ سخنگوی دولت: فعلا خبری از افزایش مبلغ کالابرگ نیست
🔹
افزایش مبلغ کالابرگ جزو مطلوبات دولت است اما واقعیت این است که باید خواسته‌ها را با داشته‌ها هماهنگ کنیم.
🔹
باید در این زمینه، مطلوب را با مقدور هماهنگ کنیم. باید بررسی‌ها انجام شود و امیدوار هستیم که…</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/farsna/439167" target="_blank">📅 10:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439166">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qriT6tYvg9DwZaRiKXGi0ykKqK0kAQqVRRXIAnbk4leLx7fifK3_3NlP2MvZMkcHLNEK21Ku6cVLfwGDdZtMDp06oHzAN_nEmvRUargtLWN38wUXQfufAIuRVRRZZSxdrvwkt6cv0aoWGwgvRQesv8qIcH4GydS668hSBcSw4pUWuZIEHisF6jLyuT4v5bQlYGXyY23iqTJaujcv0RxFJ3nI1be5VYSpdLU0IIRZiPQfVKDVJ8wjPqVvZst__AkW5K01-Dm3pudqn8r-lwjejYH4NC3FIWNszoE0leMI9hpDqBbCmVcUmD41kWvxv-BtHZNXuSZs40VmB6OrIj91Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تالاب سولدوز پس از ۱۵ سال سرریز شد
🔹
در سال‌های گذشته تأمین آب تالاب سولدوز نقده در آذربایجان‌غربی در طول سال از طریق کانال سد حسنلو انجام می‌گرفت اما امسال برای نخستین‌بار این تالاب به مرحلۀ سرریز رسیده است.
🔹
امسال حدود ۵ میلیون مترمکعب آب وارد این تالاب شده که همین اتفاق نقش مهمی در جذب و میزبانی پرندگان مهاجر و بومی منطقه دارد.
🔹
به‌دلیل شرایط مناسب آبی، تالاب سولدوز به یکی از زیستگاه‌های مهم برای تغذیه فلامینگوها تبدیل شده و هر سال در فصل پاییز هزاران قطعه از این پرندگان، اعم از جوان و بالغ به آن مهاجرت می‌کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/farsna/439166" target="_blank">📅 10:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439165">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
سپاه امام سجاد(ع) هرمزگان: صدای انفجار در بندرعباس ناشی از امحای مهمات عمل‌نکرده در جنگ رمضان است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/farsna/439165" target="_blank">📅 09:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439164">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/juh2BZW_uV8eDQ7v1SW5FcQgrE9KaskkSgJETFsSvcyEeKdqlM6UmxhZHR-U81X4Fb3P7FCaJ-WavnoCTx9EPeEJPQzhLFUpD0IJQLzuA1Hxv1GLqwg0xrS0Lp-pbdMSokoLtBTT5gQnjxsLgUIVZrQdh4PYgrTkT1GFp98N4HVrAl8sjmeKK5ohDDw2DPbUIW3_JQCnVYWup4lZS_Lcw8Vadf5URVhtD2OkYNyrsMw3fhW0Wjd3XtC0WfpVMAARFXxXU1Qk4ckhA9Osgti6vsedRXxrIxJUxyFsboYFPrur4dRUPROsMIP1b_IS25bWAyYK0HYsGtIIIlfJHuGsDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
سوگند اعضای هیئت‌رئیسۀ جدید مجلس با حضور ۲۰۱ نماینده به‌صورت مجازی و حضوری  @Farsna</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/farsna/439164" target="_blank">📅 09:56 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439160">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zyyh6HQQI6tIAnoLkSeuGaBvRej850sSiwhO6gp5zRT7QvIde7ronFaD6DjGQBYAMiXjptpjLzhRrwZoa205cQZttSsHey7oM_GKSZJjMkfP5RhNi45x3vIwR-OXf_QvFXEMwRW2KzW1qtDqs0WyubYrEiIxjYg5xufiU7CCKud09myyfWhE53Azd16ZrQ5kbRfIADZzK55lQph1B7Knxm0d9eDl8zpy189mijM7QBaRHHKjZpsRSDV0yaKARynsQcaTUm7rSFGncQt-BD1Z-xwZxyCZvA0LH7-DJtDkOmol8N6CE6e7lsIryPkidKkAbt1D_25ULb_ldLOSeOvZ6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qyVT2T6cKGq9O62qnL7z7h7N0g69vit3caj4ElFD2y_U_O1H19hoPPY7U9WGn4YljEvyzag7eoGcnxkQn29dkTuk4NtDCThMH9z91jfnf3lb1WYigz8byeDtaZi5CDDMQYpf9mRMS92r-1Zfw-RZNM6MjVuP0HTp8fZKxwodVvkYmMWd-VbemxIDx4n_hy6TaD8jgWkmo_8SKCf6UyE_WxQwnzCxeeJMguZ2TISkpAsx5CdsqN6Im5B6m_dmIeTfGYEdyb9A0isl1L87r9enKua95I5K2LHERBqidgFZlFP5xO1i_uNpqyrR6SjXdsKcISMig0XfCaBp91CljNlOkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J2p_yVqITtOuv9eDDFoA21tiPVaWcpiwTabdIddUFI9cArsCOTVT4RW6PZD-P5BjovjYNZrghi5tfpaVL4OYQjmafL_FfaFIhXpEHOS7GgTVRK1GN0isg003VJUHdDKbWWdnwmPGPqJRdceJhS_ykNTGZklvPpEkcMToD72byyEiEVfAoyvXnv3Ga6YISpXh5WAtf86R9ygVJaax3aAskyiXTiKVfH66fBl-AtPHlgafsZRulkOVVEqtlYHARs0zxHhFqij-j9MOWr1iQeJnIpih5su7gKvjXvIWRpY8SSUxF12MVXVntZPtnvIpn62DUmfNDrptG-zUHkGzQY5F3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SQBqcInCkqd_J6H-5BkunRc96FYA5VmkKXhEs31Ke2_9TNZWuh3orSd96lPPQ9XZWWHCUK9Sb9nPqTUSEGWm34tz8t3oLRMoRGhEkJmqTg42U3eyGEDF6skGwLgy94szrVUeXm07gH42GMrmgjN1dZyw1rQ8Hz7hQHuxAKZ_5S1ovSfqjz65E78nwTIK9IY7ABjvhV3wnRDtLheTcVtAMGqkFV6x6AeiMEkt-ckKa-uBfseNOlDY_2IEVZIvHFak-Yx_FrhIRNkhpAQVewjNPWdpj0Dm7jZYOPkYGLtC6NPSmBhzLjvkncdQqUPtJP-hPJSP5xhy3FaczR-AFEkV9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پزشکیان: حاکمیت و جامعه در قبال کودکان بی‌سرپرست مسئول است
🔹
رئیس‌جمهور در بازدید از مرکز نگهداری از کودکان بی‌سرپرست روشنای امید: حمایت از این کودکان صرفاً یک وظیفۀ حمایتی یا رفاهی نیست، بلکه بخشی از مسئولیت‌های بنیادین نظام حکمرانی در حوزۀ عدالت اجتماعی، حمایت از اقشار آسیب‌پذیر و تضمین فرصت‌های برابر برای همۀ شهروندان است.
🔹
همۀ ما در قبال این فرزندان مسئول هستیم و باید شرایطی فراهم شود که آنان بتوانند با برخورداری از فرصت‌های برابر آموزشی، فرهنگی و اجتماعی، آینده‌ای شایسته و امیدوارکننده برای خود رقم بزنند.
🔹
یکی از مهم‌ترین موضوعات در نظام حمایت اجتماعی، برنامه‌ریزی برای دوران پس از ۱۸ سالگی است. باید سازوکارهایی طراحی شود که این نوجوانان پس از خروج از مراکز نگهداری بتوانند به‌صورت پایدار وارد بازار کار، نظام آموزشی، نهادهای اجتماعی و ساختارهای رسمی جامعه شوند و مسیر زندگی مستقل خود را با اطمینان بیشتری ادامه دهند.
🔹
حمایت واقعی زمانی محقق می‌شود که افراد بتوانند با تکیه بر توانایی‌ها و مهارت‌های خود در جامعه نقش‌آفرینی کنند و به جای وابستگی، به شهروندانی توانمند، مولد و مؤثر تبدیل شوند.
@Farsna</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/farsna/439160" target="_blank">📅 09:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439159">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjMIxf5Hsfwx2ldnh-goIVPleSbLMYg9ms3vZYFMf58i4Z96U7_lqtktiblPs26QqSVPiLL-Yr-0wb6oKVQ8tsgqMLHsKVTK44fqShCtjIAZnWzZ1JFrD02GTAaoZhV3K__H12p5x-jgb413m6Ip99r3xI8RL7aEBV43EnZZ2lhL_oiQvydqpcxXRvcItmXA6aVxRu-xHSX-mHwN-Q_76jsnukL43pbZJ-eZWZs59gzPgErPSf8XXFBuztQ7kbBrceV_fremvylUTbRTZs5U4JclNPyTGDWNrwuNNZBlsqeV_trUMgNyDniqpRh5fvb7WCsQSqybsLabH-S3Ka0y9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ارتش اسرائیل به هلاکت یک نظامی دیگرش در درگیری با حزب‌الله اذعان کرد
🔹
ارتش رژیم صهیونیستی اعلام کرد در حملهٔ پهپادی حزب‌الله، یک نظامی از واحد کماندوی «ماگلان» به کشته شده و همچنین ۳ نظامی دیگر زخمی شده‌اند که وضعیت یکی از آن‌ها وخیم گزارش شده است.
@Farsna</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/farsna/439159" target="_blank">📅 09:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439158">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48844af690.mp4?token=doXK6_WU6Jg3JtNHlC3D6N2R6vPcUGzByN8Y4NQFPHHhoBhJLJb7XqGFS9_BZs0LyDyg3zRHQlA8aKFkZVSqLujPNcv1U2-W3X4eyOp9MOQ6GodOU3xABFeB7N2YKoxnxVJ3RzZeFkNO5ax6Hy2ZlJys4FyqX1zpGXHaoqQAj23VK-88ydxeXiW0RJcmDJdafmSsayiUld-tvYU9xhHpDhGSfx765HEhB9eH_fcpMS-uejPSXnY4U9OnLi2f95McP9fJv7EjXPl0k1NjDEzhDfkvG0KIJARRRWbceoKQFgDWy100vR7MrLTeFFT6TrkzZaznMIxsS1LUq_mrU-RTRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48844af690.mp4?token=doXK6_WU6Jg3JtNHlC3D6N2R6vPcUGzByN8Y4NQFPHHhoBhJLJb7XqGFS9_BZs0LyDyg3zRHQlA8aKFkZVSqLujPNcv1U2-W3X4eyOp9MOQ6GodOU3xABFeB7N2YKoxnxVJ3RzZeFkNO5ax6Hy2ZlJys4FyqX1zpGXHaoqQAj23VK-88ydxeXiW0RJcmDJdafmSsayiUld-tvYU9xhHpDhGSfx765HEhB9eH_fcpMS-uejPSXnY4U9OnLi2f95McP9fJv7EjXPl0k1NjDEzhDfkvG0KIJARRRWbceoKQFgDWy100vR7MrLTeFFT6TrkzZaznMIxsS1LUq_mrU-RTRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گنجی: حاکم‌شدن نگاه عیسی ‌کلانتری در حاکمیت «سم» است
🔹
کارشناس ارشد مسائل سیاسی: کوچک کردن نگاه به آمریکا در شخص ترامپ، یک کج‌فهمی سیاسی آشکار است. مسئله ما با آمریکا مادیات  نیست، بلکه مسئله بر سر «وجود» است.
🔹
کسی که می‌گوید «در حلقوم ترامپ پول بریزیم…</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/farsna/439158" target="_blank">📅 09:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439157">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">پول دولت به گندم‌کاران نرسید
🔹
رئیس بنیاد ملی گندم‌کاران:‌ دولت هنوز پول گندم‌کاران را که هفتۀ گذشته قول داده بود پرداخت نکرده. این در حالی است که آنها برای کشت بعدی نیاز به نقدینگی دارند.
🔹
سه‌شنبۀ هفتۀ گذشته جلسۀ تعیین‌تکلیف مطالبات گندم‌کاران به ریاست معاون…</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/439157" target="_blank">📅 08:54 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439156">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
سازمان پخش اسرائیل: حزب‌الله از بامداد به شلیک موشک‌ها و پهپادها به‌سمت شمال اراضی اشغالی ادامه می‌دهد.
@Farsna</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/farsna/439156" target="_blank">📅 08:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439155">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kbZ-cGubT24TCEzu9YYPumX0xeU2MzGqA_FjHq4WJCKGXwk_jGGDSM5TY9HbUSlZSbcLjiQvsp4264rP1HU7ggb6ndURcg7c-kD2DmSsSjqTnpC39VZAg_3MOzWNcg5uVNvqpk2vF8VnFmvXyiU1VFusvs3ZZ7FH3yWeXH4XhhJqM9OktrqkVX5fHNbLQJvsB9i9CAOPZhg18wG8L8DIapVLz0nQXIFte0BqN-z87MjzBrSpkvN4-GoApuSLgRgXimjiQOAfBtmmOk1M06IAJ1K5iUy3zUMw5YA8bPL4npfWXH9H7hRqpcAoguk_sli-z5fRQp0Q-tDlzcP290BL1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیفرخواست قاتل ایلیا صادر شد
🔹
دادستان استان گیلان: پس از تلاش برای شناسایی و دستگیری متهم حادثۀ قتل پسربچۀ گیلانی، دادسرای مرکز استان رسیدگی خارج از نوبت با هدف ایجاد آرامش در جامعه، رعایت حقوق متهم و تعیین وکیل تسخیری در دستور کار قرار داد.
🔹
با رعایت تمام…</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farsna/439155" target="_blank">📅 08:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439153">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adfa5f3571.mp4?token=vt0mAxHzrrXQF2Qr9bU5y5CvzSG2qw8NLthEqmoT9fbShkJ94vJ9TxWSTbgDfMRj1O7wo3WTg8gouQo3XLE0NbFLbNzpMivcLAJGhWZiPR5YNoF0ho8W8B8JrIVv34lYoJ3gvVLudYSQ2OHIABnkRN462rDyXp8SJnzUbeED8ivNiRHVi2Nv6gbA5rmgZsfcL0Fo2TGmhD_W7jiB9lXb-EkwlS5wxk-WCtll7esqYrvs20y8_yc26fap3qxGgtV71STTb0pnX1k_8IeIrv5JFEMu6ZNfS9fSRc7srwrAFrS_T44bfLIUTd_p_HUfcmT-Fx-IwWEVeBaXd3NYviP2-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adfa5f3571.mp4?token=vt0mAxHzrrXQF2Qr9bU5y5CvzSG2qw8NLthEqmoT9fbShkJ94vJ9TxWSTbgDfMRj1O7wo3WTg8gouQo3XLE0NbFLbNzpMivcLAJGhWZiPR5YNoF0ho8W8B8JrIVv34lYoJ3gvVLudYSQ2OHIABnkRN462rDyXp8SJnzUbeED8ivNiRHVi2Nv6gbA5rmgZsfcL0Fo2TGmhD_W7jiB9lXb-EkwlS5wxk-WCtll7esqYrvs20y8_yc26fap3qxGgtV71STTb0pnX1k_8IeIrv5JFEMu6ZNfS9fSRc7srwrAFrS_T44bfLIUTd_p_HUfcmT-Fx-IwWEVeBaXd3NYviP2-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سپاه پاسداران: مبدأ تجاوز به دکل مخابراتی سیریک هدف قرار گرفت
🔹
به‌دنبال تجاوز ساعتی پیش ارتش متجاوز آمریکا به یک دکل مخابراتی در سیریک واقع در استان هرمزگان، رزمندگان نیروی هوافضای سپاه پایگاه هوایی مبدأ تجاوز را مورد هدف قرار دادند و اهداف پیش‌بینی شده…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/439153" target="_blank">📅 08:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439152">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb82734318.mp4?token=G4KDt0dCTfAh_0tXEM-T-Ij3BOxO_pLCgpV85GFyqLobEowHgDhqjYF3Ejh25yG1mviW2949Mi8VpSoDXGEgtCd_okxsyZ6GkPE2D8r6lGwQD4lpnoW90PoYS8CiSqZ1DfAac79eRu3V6t8SfJ0H7nfDAZSgeUQZaw4ff7qwabvFIsSud-vB7xTVjLP3kIOqr3Ir_W45y1EGz5FmEyB-7YIoVpFVsT80wMHs0dXaly6IoKhTsJR6b7RxEgD4E-TJ7BxD_jiUPIDjIjBXp-C_1AjndmC3rk0NQCUj-JVBgKKhGPZPG2by2-a9_I-l48A5DqohQunAwZpCvfHJsF5BbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb82734318.mp4?token=G4KDt0dCTfAh_0tXEM-T-Ij3BOxO_pLCgpV85GFyqLobEowHgDhqjYF3Ejh25yG1mviW2949Mi8VpSoDXGEgtCd_okxsyZ6GkPE2D8r6lGwQD4lpnoW90PoYS8CiSqZ1DfAac79eRu3V6t8SfJ0H7nfDAZSgeUQZaw4ff7qwabvFIsSud-vB7xTVjLP3kIOqr3Ir_W45y1EGz5FmEyB-7YIoVpFVsT80wMHs0dXaly6IoKhTsJR6b7RxEgD4E-TJ7BxD_jiUPIDjIjBXp-C_1AjndmC3rk0NQCUj-JVBgKKhGPZPG2by2-a9_I-l48A5DqohQunAwZpCvfHJsF5BbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صاحب‌خانه‌هایی که هوای مستاجران را دارند
🔹
وزیر شهرسازی: تعیین سقف افزایش اجاره‌بها به میزان ۲۵ درصد و تمدید خودکار قراردادهای اجاره به سران ۳ قوه پیشنهاد شده و پس از تصویب ابلاغ می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/farsna/439152" target="_blank">📅 08:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439150">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/joHPLVG7FUvuGcSjo0yuOdNGEt7Tz2v4rcZgktEHzGZUKvcNAws6Pg4nqkVlD9f_EhuQXR9GzI_577Kth8Yd54LYqibPglBs9ycHcqtY1xb_0Ul895F5YtmOsjnwnjTE081IO-iTnjIKFsydvkCruWRq3rj_HfEiUphlOGDnyX5G6tZBJd2iAXewzBo1ulJ2IFQQ-NH-vlEQs82M99xQn7NDJEpPYNWymb2sxiieryDy7bzP7-B2pLJIf-xRGqQgqZqG4y-NcJtDBZe2o2Fm8WTAPChDBaCJ3Osu4boRvvTHOsL194YE0k3tPifm7EtlQMj6vw4HCwzPzs0nFE0tGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fJuxvb5kV3bdZHs0DL5-MI4brJ1Oinq_YaXRdWruTxzJgxN2YIpUnTLZGvGG2OwYCKTR7GYi62EAGrYi_d1fApKunNF2K5HGWSdcWepdtRDTa1gOYzDt68y-uYwwEYY42i6KDfbrx8uE_aa59KuJw4_A5VMvgpMj6-UhDsG9i9OdotpXe5YH40FagyeAaOF4Tt1pIFNrs2VXP2jSZG9w8B3azbxZOjXKzBu_mfr1msu1XrTeludcM7bI1PYQefBOP-0shgnILGG0IVLeH9jXvchXIA4bYTU4iIdBfMCpsSUo1R0vH0LA7WZ_bDKOFb1Ve-_MTwLaUcSvan41pEy79g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
عوامل آتش‌زدن مسجد جعفری و حوزهٔ علمیهٔ امام هادی در کوی نصر تهران پای میز محاکمه آمدند.  @Farsna</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/farsna/439150" target="_blank">📅 08:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439149">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اذعان اندیشکده‌های غربی به غیرقابل اعتماد بودن ترامپ در فرایند مذاکرات با ایران
🔹
موسسۀ ران پال: ترامپ در ۱۱ نوبت ادعای پایان جنگ یا حصول توافق نزدیک با ایران را مطرح کرد که همگی فریب آمیز بود و دیگر کسی سخن دروغگو را باور نمی کند.
🔹
فارین افرز: تضمین‌های آمریکا قابل قبول نیست زیرا ترامپ به علت حمله به ایران نمی‌تواند اعتماد تهران را جلب کند و تعهدات مورد نیاز را ارائه دهد.
🔹
کریتورز سندیکیت: اعتماد سکۀ رایج دیپلماسی است، اما دولت ترامپ نه فقط غیرقابل اعتماد، بلکه قابل باور شدن نیست.
@Farsna</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/439149" target="_blank">📅 08:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439148">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e9fc39208.mp4?token=FY7HJQPv5E-haEE3g2g1Nqpwrl18kKO_1kQTjOYHUusabUlr0Uaep6iCmxHsITzqUJ6skwGz4LMfU3nix-zASjS-eN6IyQJofKW6N_fTaHCr2Ap4ByT6j4xLQ6sInnA3Mi7kkvQpYZ-pJ7Yw5BfHx1N6Fiuh08ElZjPv7iTdhaAzzfVN_hAdeNfKwMMEoL0GrbqcgO3gkAhl_BX_A4x2a93l8gmZGHZziU4wkaPxEDShUjBCOV4ylMpwYlS2NH3r_fcCahLOXhaMDMXewHdWumXMZTNmZX7Umc_ZUFijHym7Oirk_Y42TA7umTdBAyB_AXT_DQtqf6G2mCImO7BCSZkPGP20skyVEFIRH3Mxj8EEd_8wydIb1Ur54iyYsLdQbL3r1bEbmzgfK9GuK_Uiw5q2THIBg-5VQqfVQqIudqnvEq_KeJce_uTg4B2wJyFZdh6hK3j9Mg0td1mNnpsDuXeS6AdHabb2FNn7LBuakqF0tKtnWNg-dTf7Ndl_FelrG-kl1LQzQG3uzZAIyewNUIbv5WUHHXBEO-cbWBI0RnvUuEDqtYdw8HMC2-25ZWk-wJSOkIs6iyuC3bdqV_pW1uIUhxPpUZ8-b55bYm4X_DLyJAniRd7BjBzhol1hgPkAoOB88qCbxXd0l5VPhb4abIMclgVYH5fPfR-p2xWT15g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e9fc39208.mp4?token=FY7HJQPv5E-haEE3g2g1Nqpwrl18kKO_1kQTjOYHUusabUlr0Uaep6iCmxHsITzqUJ6skwGz4LMfU3nix-zASjS-eN6IyQJofKW6N_fTaHCr2Ap4ByT6j4xLQ6sInnA3Mi7kkvQpYZ-pJ7Yw5BfHx1N6Fiuh08ElZjPv7iTdhaAzzfVN_hAdeNfKwMMEoL0GrbqcgO3gkAhl_BX_A4x2a93l8gmZGHZziU4wkaPxEDShUjBCOV4ylMpwYlS2NH3r_fcCahLOXhaMDMXewHdWumXMZTNmZX7Umc_ZUFijHym7Oirk_Y42TA7umTdBAyB_AXT_DQtqf6G2mCImO7BCSZkPGP20skyVEFIRH3Mxj8EEd_8wydIb1Ur54iyYsLdQbL3r1bEbmzgfK9GuK_Uiw5q2THIBg-5VQqfVQqIudqnvEq_KeJce_uTg4B2wJyFZdh6hK3j9Mg0td1mNnpsDuXeS6AdHabb2FNn7LBuakqF0tKtnWNg-dTf7Ndl_FelrG-kl1LQzQG3uzZAIyewNUIbv5WUHHXBEO-cbWBI0RnvUuEDqtYdw8HMC2-25ZWk-wJSOkIs6iyuC3bdqV_pW1uIUhxPpUZ8-b55bYm4X_DLyJAniRd7BjBzhol1hgPkAoOB88qCbxXd0l5VPhb4abIMclgVYH5fPfR-p2xWT15g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نصب کتیبه‌های ولادت امام هادی(ع) در حرم مطهر رضوی
@Farsna</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/439148" target="_blank">📅 07:19 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439147">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
سپاه پاسداران: مبدأ تجاوز به دکل مخابراتی سیریک هدف قرار گرفت
🔹
به‌دنبال تجاوز ساعتی پیش ارتش متجاوز آمریکا به یک دکل مخابراتی در سیریک واقع در استان هرمزگان، رزمندگان نیروی هوافضای سپاه پایگاه هوایی مبدأ تجاوز را مورد هدف قرار دادند و اهداف پیش‌بینی شده منهدم گردید.
🔹
نیروی هوافضای سپاه اخطار داد در صورت تکرار تجاوز، پاسخ کاملاً متفاوت خواهد بود و مسئولیت آن به عهدۀ رژیم متجاوز و کودک‌کش امریکا است.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/439147" target="_blank">📅 06:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439146">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
فعال‌شدن آژیر خطر در کویت
🔹
برخی منابع از فعال‌شدن صدای آژير هشدار در کویت خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/439146" target="_blank">📅 06:53 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439145">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j38IyDP2ppDw0yorwN2mRSNr1Xniun3K9eFpTAAiLNW3sSrzzztMZ50QLWFJjWp8hZFqN51HLIGRzQbXN2zqXxWMgyk5V0gfCA1rg8goqWoxKUnHlCykpQQ78O_BKab2OFHkfb7SOPQVVbvYja8KBZDbNGXNRq9nYHIH-isun0i7yOpPq1mRChoj2KtlSNUnDJAul011GzLCFQObEPe1BaaNiltVcquQMvtKvL4JXJzvVWB8pGH05iOSohcpVRI8sVE8iUV_Xw3Ne-h0ouT6QASokhX8IdMQGAGlNyG5XK3nRBZZJnsM_DN5VDrwHrt87P3lUp2HGwTRcn7oI3sg4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اورژانس تهران سرعت گرفت؛ ۱۰۰ موتورلانس جدید وارد میدان شد
🔹
قائم مقام اورژانس استان تهران: با بهره‌برداری از ۱۰۰ دستگاه موتورلانس جدید، ناوگان موتورلانس اورژانس تهران به ۴۳۰ دستگاه رسید.
🔹
ارتقای این ناوگان، زمان رسیدن خدمات امدادی به مددجویان را به زمان استاندارد ۱۲ دقیقه کاهش داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/439145" target="_blank">📅 06:29 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439144">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2SlvtVLFyzo0fCIdI6sAJ-TCWAQr6AlVifsH0d9gymNE2551zOrVMK4OPP9AXXkQINqHJQUdL9EAwPo5enwJzR1aqoCfVwsnce5j4j-heRi8LnDyQMOB602XnrhffYU_xB00bjg8FtpCtUrtMmDBGGysbZc-Lvir3pLKjTIv-rdfChqD8ftskNxnZl0xgF9QJj14ffWU5FWcOr9WlPhgWjluMGZqOlZUpGrHostxYH1iIq8hfGDiPhqT6EI9KXJwCNr0Ouqu7s5S2vQPCuGINywytCsTViYMgHo9rJX880hnHBLh7KguTCuf4Uzjigmjp8cY1NI_2QWKS5yUPPKLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار مرگبار مواد شیمیایی در آمریکا
🔹
وقوع انفجار در یک کارخانۀ بسته‌بندی در ایالت واشینگتن آمریکا، منجر به کشته‌شدن، و مصدومیت تعدادی نامعلوم با سوختگی شیمیایی شده است.
🔹
به گزارش گاردین، آتش‌نشانی لانگ‌ویو اعلام کرد که این حادثه پس از ترکیدن مخزن محلول…</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/439144" target="_blank">📅 05:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439143">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_UOOAJTeHNG3WFLVQa8Zu39eFKu3r5q9IobPMGAF-CWe-xR_tCJEybk-AdG5LFAlrjAA_oSsLKkMTxVQoS9JWjGFZe86xvuFDkzUEsqywstqjv21_CWGhbEHbJ5gyc76mz8yOhfRJLSCKErPmIHm14Tk7ePYGiVq6nhYBCG_Pe5xQKrfThz9vXP4EYlMrTz9oaYxvd-JybixKro3M31dtWhUEs_bIBMEG8JLSzI3o-6hB96_mIrC6cDrNvEZgn3bpLlvmpA9OT1Uuhe6i5ayvAao-VZWyLp_Z4E_Fr_qTxZdj5ErhBSrDoCGzqrSqxsjLYT-nLxpL7JWGt646K-kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزشگاه‌های آزاد حضوری شدند
🔹
رئیس سازمان مدارس و مراکز غیردولتی اعلام کرد مراکز غیردولتی اجازه دارند کلاس‌های خود را به صورت حضوری برگزار کنند.
🔹
مدارسی که مجوز رسمی فعالیت آموزشگاهی دارند، و همچنین آموزشگاه‌هایی که فضای مدارس دولتی را اجاره کرده‌اند مشمول حضوری شدن هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/439143" target="_blank">📅 05:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439142">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZHCtovzSpUn-_VGp9dDHQxvqUOfHpfJIHsu6SCPOIUuLHgnGz_TQU1C28UH5B2Xh9wOZoxX3Fw_dUEprtNqjAH85Ox26aOyEOaM8TQZoWT75DcxyAW3KXCoc4UFwhdnHjPoBvKIyhI1NToZ6flScDj-6KBxcUFrbUKjlOjrHTgLHCffKTyysK6BfKTHj8cAh_jPhMexT-nnpkOozvO-EmSASnw9Q3WgHdp0hynGezq-Ruq9xgTiO6LtIKp915qgtobxecbdaaJk9I67qlcOroJKRh8l1XAdYqbX5N9o_Y4WZsPl8ukT4mTPbXjU9dlB_91vg03QBLqCL1YOw--UXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات آزمون صلاحیت‌حرفه‌ای وزارت بهداشت اعلام شد
🔹
آزمون صلاحیت‌حرفه‌ای گروه پرستاری، هوش‌بری و اتاق عمل ۱۸ تیرماه ۱۴۰۵ به‌صورت حضوری-الکترونیکی برگزار می‌شود.
🔹
داوطلبان، صرف‌نظر از دانشگاه محل فراغت از تحصیل یا دانشگاه محل خدمت، می‌توانند هر یک از حوزه‌های اعلام‌شده را به‌عنوان محل آزمون انتخاب کنند.
🔗
جزئیات کامل را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/439142" target="_blank">📅 04:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439141">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPIgAvhOThZq0fBuO1feMaqpDalF_SlNFuyLeImxpG-z4KF3MoZF_0lp-R5Frv4oXEHKWOoW0I2GC2GCb1paCq0n5cEJZEkSYpPGoVuj71WkGvY7lXYkTuWPIjvHvgxZ_0xqKd39E3wQOkjH477wP0sHCPgovgcxtBx0OeAJHGr_lgBGHrS-Jrywu60B5MMX2btz4UTZKesaCl-eS1DuIi3itQuehrdGPfA2tUfPyJUrr3LmLkVJUgxl0EhZOLo5qBQTtxY8cv9m8IIRwJRT3JlmkAkob8GaOtOOHA5rnERC4GeyC8hMkx1_UGhksYuBSN8OM6Q0_fK1wbSK7w9lhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۶ درصد چک‌های صادره در ماه‌گذشته الکترونیکی بودند
🔹
بررسی نسبت صدور چک الکترونیک به کل چک‌های صادر شده در اردیبهشت‌ماه نشان می‌دهد که حدود ۶ درصد کل چک‌ها به‌صورت الکترونیکی بوده است.
🔹
شبکۀ بانکی در اردیبهشت‌ماه ۸۸۸ هزار و ۲۱۶ فقره چک الکترونیک صادر کرده، که نشان دهندۀ بیشترین میزان چک الکترونیک صادر شده در یک‌ماه، از ابتدای شکل‌گیری این ابزار است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/439141" target="_blank">📅 04:19 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439140">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
حزب‌الله: یک تجمع نیروهای اسرائیلی در شرق شهر یحمورالشقیف با موشک و گلوله‌های توپخانه هدف قرار گرفت، و تلفات قطعی به آن‌ها وارد شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/439140" target="_blank">📅 03:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439139">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
برخی منابع از حملۀ هوایی رژیم‌صهیونیستی به شهرک القطرانیه در جنوب لبنان خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/439139" target="_blank">📅 03:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439138">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">نتایج بازی‌های دوستانه ۸ تیم جام جهانی در روز و شب گذشته چه شد؟
🔹
در ادامۀ دیدارهای دوستانۀ تیم‌های حاضر در جام‌جهانی ۲۰۲۶، روز و شب گذشته ۸ تیم حاضر در جام بیست‌وسوم به زمین رفتند.
🔸
ژاپن ۱ بر صفر ایسلند، و سوئیس ۴ بر ۱ اردن را شکست داد.
🔹
جمهوری چک ۲ بر ۱ مقابل کوزوو به پیروزی رسید، و کیپ‌ورد ۳ بر صفر صربستان را برد.
🔸
آلمان ۴ بر صفر فنلاند را شکست داد، و آمریکا ۳ بر ۲ مقابل سنگال به پیروزی رسید.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/439138" target="_blank">📅 03:11 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439137">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZiv11GVPRg2aIG7qoF2GnwuBqEEy1cPxwt5O8sDFx18nfwEJOCRIYG5qTq5K4ZR43TAN4quw_gQjz0tD-p6n7dbJeCg-qqK8KY4o6ITPf6M1Gd1BNAi27aUYE64E5ToN02ambn6wmcQBsIuCzr3Wa3sKVx8zqNetykDmkZHGSDBHN_mdT6V4VW87wLb_rD7xU4gsG9rxBS3q-4hl4hdPqdyg1NQRUEkTfkx5_gHC3T57IOWVQeNWRNcatrwfAbECR4hDcxtwp2EL1mRONBwX3YDk-X-_dGcpvRP9uGqmfc-gFl4flERpxnWE_7N8gZHw3Unyw4sxXKc1Wjho-PZJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحۀ اینستاگرام کاخ‌سفید در دورۀ اوباما هک شد
🔹
به‌گزارش راشا تودی، در جریان این حملۀ سایبری، علاوه بر انتشار تصاویری از حاج‌قاسم سلیمانی، پیامی با مضمون «کاخ‌سفید تحت کنترل شیعیان است» در این صفحه منتشر شده است.
🔹
هنوز مقام‌های آمریکایی دربارۀ جزئیات این هک و عاملان احتمالی این حملۀ سایبری اظهار نظر رسمی نکرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/farsna/439137" target="_blank">📅 02:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439136">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMabA1JW-UZh0QRL1fWyNodlsQi8YswufYd5tK7Bn1a9DYpln68iytLwHR0nGHioQXeaPBTIsOV_htqJASj9K4X0UPXeyLdCW8J8aTs0dY4szn6UGnTRlf__G5o_Jik5NQK7rrzzL6Mqh8iYnltgSVgZ7v0CzgFfs3iBq2Gejg6VbIrz7ffMNYSWEq7cozc20ulJJqRQwvnwQWNgVYM4uu24Mck9247ibwHExtsv4ire-ZJd9OaPhxtj0_A2kKpcMpCLWG_JmMqMbxY78I__aLFtTmlwrQCFf7MK1K7qSV8otH0GD9oDygDS33jP2eSg0zJ7EfCcOw3JJODsh0beOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیرعامل سپاهان استعفا کرد؟
🔹
سکوت مدیران و مسئولان باشگاه سپاهان دربارۀ خبرهای صادرنشدن مجوز حرفه‌ای باشگاه سپاهان، شایعۀ استعفای مدیرعامل این باشگاه را پررنگ کرد.
🔹
علاوه‌برآن، منوچهر نیکفر مدیرعامل سپاهان نیز نسبت به شایعۀ استعفایش از مدیریت باشگاه واکنشی نشان نداد، تا باز هم شایعۀ استعفای او تقویت شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/farsna/439136" target="_blank">📅 02:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439135">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e6e4d90c2.mp4?token=GQmPUIQnqdQaa59tKEcAmARx9TXflHC8lPWLi9kyADM3cMmjFD-czPZUWbS3sarNnFi2cuyisebYaY4lt01RmB38qCV26pB-8jexwZw4Wbdq9bXj70__iK1g7QBSnw5w82TPDxGrIuORRIXgh1hiK6EUoR2g_XZWi0SNl3H9ytvW5OUPuEEi3nlshhishj9BRJkIrB8s8vyMVB3A3z9irfDgKDSG0YfeouibKOhOMCIg3gT3QngVI6I8vKNJ19Eu_YZtDohpjaFtZjFPoDffQmdDpcu_YPksOg6GDqLB46_XJzkWaJo3GzSQ2UCthPRwW0x_5j_vXAP4ev3oDLZegw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e6e4d90c2.mp4?token=GQmPUIQnqdQaa59tKEcAmARx9TXflHC8lPWLi9kyADM3cMmjFD-czPZUWbS3sarNnFi2cuyisebYaY4lt01RmB38qCV26pB-8jexwZw4Wbdq9bXj70__iK1g7QBSnw5w82TPDxGrIuORRIXgh1hiK6EUoR2g_XZWi0SNl3H9ytvW5OUPuEEi3nlshhishj9BRJkIrB8s8vyMVB3A3z9irfDgKDSG0YfeouibKOhOMCIg3gT3QngVI6I8vKNJ19Eu_YZtDohpjaFtZjFPoDffQmdDpcu_YPksOg6GDqLB46_XJzkWaJo3GzSQ2UCthPRwW0x_5j_vXAP4ev3oDLZegw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هم‌خوانی مردم تهران در میدان انقلاب
🔸
تو این روزا که جنگ اقتصاده
🔸
کمک به هموطن خودش جهاده
@Farsna</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/439135" target="_blank">📅 02:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439128">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O8EAQvXewNUoK74PxQaBfoNsLdIbREQsQ6EFkk_FXzdxHv9WjAv72Sp-QSNcfg_8gYh86kMWD7lNhJNNx6lPvVF-aidXWJd4UEspigkXSTJhwoF6MIVKec27w_NO_16sFpszaesZtkbPwfao3AM75hWa2VtxGL_lgSwQGiF81tWCtwfu2o2N2itad2YplMqejnov6ZZBrDdzzAgyXJ4JIpEL3Ob6iQT3c2PL8tHtWSruoLjRDNKWUkrNalmho32rbHNCgI7UhVtPoM_GNAFNX7Zm0A3Ms29KEm7jv2x-i02ba4ak7s_JjffKtZ1Vs37Z5dEWtqhCgGB6fAYUGtqBGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LJy8O13KNrtJMhFyuXWTgZQ9hWWjUQjCEKTf7QYWOh_IN4tlhQ752p4BwbHieUBVkxghmxmGj1Hy2Ax3-Md8JEuRbH7APU2PQ-5b06KXvd5Xbhmmr3C6YVcm5GiSNBNPQzSHNpyDAnjAz1VJk_QmKtrCDD8vE-gwVinXIUgLZ5EdTTUIH4XRC2Lj_IFv4eFR_3pohvm1KGHDbbpZUbOHk9ts6jeXV4A5q4mHlPGJZ6PSuYJZXa4U9KxL1fRM3c98bh-MeZAr7ven6NQ_6FlWtJnMrG9i4j5jYUtc6t5zHd3CdpVosqh-2euhkSEsYNJ2NWw0FSJhrbwPKDDipbrXYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oKywJq373xNS5lt0wzyjEPjInIs-3x7Y6k92yeleDRvi7Z7nVyB9vK4wVpArQviowDcL7V62wi-7f-D67ax0sl4cxtp1h5OReMys1wqWv87hSKftlCIlmAbQGDU4_A5H_tXE19e6XQ_5tbmJID9TEmx9PqQhT6AoIj2dux18zP01OHIvFv1xzjNQkbfwb9MFaajkIgPy6OdlWEIs85_qQmiXdL594SJol9lTc7HsHJURApxuXnIzBaZhL0YKHG6gJN5XVCJNqqs3InsBb2AcCaf2paBYVV2opQSy5MAZSRZ5vAlUhSDngNejRa8y9WIrUAUg9NCkryQ-KW660Bl5HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RhK75Q5Y2jaoHWJmdjfgW8-tP5t0rcSUWHHPhnKhxhPUdxXFmXLBUMrZMHDXcgSGnaRCiQDSbiDMkyDNfMmWgm3J-YGBa9_vDvruuYG4XeMPZNsRxXaa4tMMf3hLl9NqyP4apkTtuZG7P06aIhTujZzH1nugGJ2B948JIW9-2JK2qLDjs1KUs3OaowVEKIFyDWEb6g71Vv1MWhIUl60EMGbLCdEwPffT97ONdSRResEqhzRoImiglBpNgRcHTamrR-CJAhvpa7CoFyCvDwQXYPSpb7ggeN9EEj3YRsVudA2J-cH1Z_kdPbhAiiEN0wXJdLudB5Md02SgtyNoGnz3Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bcuy5eBTZRbh6vUw_WmkKkLZaG92Vv0zlnAhUq9fa1-_xT_Rtj7AxBJenh-RBfiG2rf3v-KNUTRCN4lAW1TXRE5JSCS8t_yQR7XLQb_DZvc5moNOZyuOJyBN5KbjLcHWUe62CSM-01hc540j3ix_ONXwPGXIQ9RHFkUfiMCZnkhpD-IjJrXiV3fV13F24yzME-LfDdcRt0MYiY2UJgRdS4WSgQuCPM56RcE15kLmpkvZGqEeJDwKUAsMnMI5TC2Knu43Ano3Y05ULsVkBDSeaBk2A5GwIEUO6gEYgnDT9z8f_1-j6iIb-iHow1y7KPd5mGIDvARV1VTvLbL4Fwb4qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LsHjNXAHvJ8vZxI49NHLbaop0zUgRWvq4BlP_R9njumKjhKoYoTFw5OS4OkbB9KoWhGAajuZN9i45pGqOp0ASW47eyTEhjaVkfNW7s4-3Pel-gusmblOgr9_VLssezTuxSOEd1s55_D4IgaS7ebdS5WPR28GgOaydl_SwNW3nvcQMzpFltXgJOKJ0NlXPQBY2idj_tbwwQIwozXqNtfTwohJ0jb8WSpmG35uFztVdi8GjNH6J8mOFbkd8e8w7GZujqgi77JL5kc1JrjOgCSqpk3tCJltdKx88xCV9fyYpCXcJYJW2_OMDMyHsDG0XZBeX0Ou78-gYpOUoFUUoZGCgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P_a1Ky3O03GU77ViIsylNZlUXLOASzbcbBch0Xsqcr0UST1MD2wQWKNDnjpUgDfQqfaW4Bpgv9hUSsk2fpwF36XZY93xdu4mo9LeXH9UuW1SAz5S1K3RXTOz-Ny48qdUVthgsd2CNCqa8qhGd-zu6QMgcEaxqdkf8m2Rn5_tyOs0JHkwdRLq_KMzq10TJ8zzEDaHO9-9nSI2cFdaJc890_QvAXIV_DUYLovH0iqglYlsLEm7HmqIbuBIuMXrmr9UzJnSsgKGPsjoKxOG_1NuT4S7MORquPXQIEajBgfVSOktNez5ZETEG8tAgM6aD7OBXJ6hqcDOp66nKa5VgTcFgg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اختتامیه جشنواره «قهرمان ایران»
عکس:
صادق نیک گستر
@farsimages</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/farsna/439128" target="_blank">📅 01:54 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439122">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bOXCfk7tZYo1zNCzAeYEc5sCDR_UUElqB4wzU4-5zxo9kMOX0aMOG0tWTSP2Qc43lqxi_i5342mpiG1Ba5eLWivIbZHXB2M4gd3oDqlQowgQ-wtxLCHtnone1PsyQDE0VL_6NNxVTahVh9suOFot0fMEPh9iUvh46ABLiIsJdhBHWNkM1EdBd2e2yPcZ9UwsCNaCAulYTekY8VzpIzuEgH0sTCojf6oQz1EpoBWHvzlW3Bt7XdIpcza8L5r2PMSaN5rEd9lgRaWym3yVylwfT13hu3gZsKAA9d6Vn5lmhb5J9I01kLRLdQkmfRKj2-iA9ikdXg829R3FTmVgSVaHgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iMTU56kzgi-sp39MXECUSVpYtGrYl3-sHO-DydksMjj25DIYZ8-Slf07IFjb41t-6x0G5HgJym8V7f7Xlq8Y1pQ2KVdU43GMgfz2qN4ex3UsYGM5KWRFLeRfP7hMRRmhr9yYHBXWGzPqCLUf1QVGFtgs7ef35ZWOH0kGPt_qLvXo6XYSH6z30G66WVU1qRiECQaXtSK4RXltLwltVGxZ6bGZi_xpxIMRgSOOVYp1mxyc7pvuMPLTggHGmSwhhQrDmueDXMDwsclUh-lcu_84yo3uzpmn4DcCU_C1vSMxkfo2_lCyue21ZnDmZSQeP8ILz89U2_PkrjIh7mwDlGbQ0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eP_KGLiNFoaA1QlvfsXButNDLHHbuuNBlRMTdSD-0PBAVfrtxsHDM56739IdRxrDhmU9YKPFtiqOqh5NKuoSm08cSvwFKTitBOzocRjewnmVly4EEtZWFwXzGF1GKCe0filBbERSVig6ueVc20rU9kq-6NPj583BCgu_ta9edYjad3Xsc3jAwkPMLC_ksT5ZNMcs99Ks6xXj37dDPAD5PqakCm02rHj74Ug6nYzwmgg8T0iyFQi86vZH2nNpCaRSyH7AW_GomsIOvD-HDwDQ1GYHm2tY6XETlwluir9f9cxSHVHNFfsnlwDsFgJSC2oFtW71HbdQuRPhQPjvrIEPfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jTIMHZm3pp0ppOg8pSTYWvFHUAdACsUxMNobBsfNRu_GTWNETqdmqwACx821P-4t6bx4Kq5-vyGoXEBtSAWQpoAwJYG__UIqKXehv61L30JraD9cu9bRlrZQDZvlmvScdEdwo-83hQOgl52XUl7638OLd8_s6XydnNrhAlCLepFQ69nJyfYPOBp4n67kol8U0R-CSPqbLF-PutORUE-kKEaAELti-q2SQiYjEX9n-DPeoLiypRF8mTPMZ_ROKTlCxxud1EepxiahK1WMGHTYjq5qgtMMPLKngyrDceNAI7hhBuv3dKBmL2stDcFcpknePnEQXvKaLaEABBQOqCn7pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SdNUbq3WO_q-hQ-6OGDmJdQcYWG8VXGBBXciW92fnRYfCQYxdVd9V3wkBTh6UaM1L0KazFCGq8Q7sORmE7bRbzgGkxsnLMbUZraDV3mXLwNc-kXXtR8wHR4BHdgozRH-8FoxC4CSEsGvkgNH5bQBWO6Pi9XMRJW1Tqb8rvYHUMtMTAyWP8wRWLKFKfrgheWdIKDbCd_gcpiTi7P3YypfHkglyiyQvHCuQWjkyuiIMd0SZwMxoDeKFETHc2Q7kme2vPFjP7coEBF5Gu3DOlkCfxHH0Wrf1y9dQMrfFZfm7AXEALhgW_ye3J2LhVM0-MTAjSRE5RohNAFc0X0aq4_yMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hxgfQAAyFU7kP7-8pF02FJc1phpmhz-xTLLTofv2-8WLMh0STMXXq2gtoiz9OJH7dGH_qmXdvSlXlkOEMW0iupQTldHGVGA9fLRuM9wbAYyyzdnLyrQ39aNM7-DCEHOtgTUBG_8Xhm1Qijep5CD851ngTLzXgQF7HEM6IYszCi4j1gViwV80o4NMxt7QujM625v7TbPxRPrzZuMzvV9Sx8u1Xu4sAb0eXQ_erYOwPvYWbuwMOxCnWMupsKItbJYJ4tCpKm9mu8DPnLvGDBCsCP4FszETYH5XLNFzVVsBo_GZRUoxW1giTldRVGwYqJ7cBzbjViH5IOCqeRtJx2f-dg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | دوشنبه ۱۱ خرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/439122" target="_blank">📅 01:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439112">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ad5z34Z1pTxpOQwaoc5gdlLy3QxTl2wlvT9QksSLezUV6JjWy_MzwVMOL1DbAQiGRUYUIKSBqSI1reZ-NUH7IhfggyEnax1x4gH0QBW7RcHCtDpkAxDUfM32VNNfu2UspdT_q8rjUU4i-kXuaE1sezyX2Pt6aZcH_aSgUMSg5YxAvKYenQXffGNdaCKBLISTE5JQ8HzTqXET_ynBbYB9Qn2ydvMzlrNV9jFxwsMM-p_j4SlYu-5_-n2NBErCJCtKD09e2Prw_D98gBM_rr56LzfxIq9LYniLxtEIPZo1Xx7VlfoVWKeiGB3TXNgFWf04yY9MjW9pH_l1L3es32sC1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h3mf3eHD66y060AlU-uLD1G-3T1Ir97kBRBgD4KTg-8bl7KCE-_sb1A2CSWat9hA1TKpRi1pAgnPV_GFSeVw6s6mLfqRH2MqL-e2fg0VICMQp_a16HkskpVyNmeFiwZN00UOwu1otWRgaJwEMHXP1kdQMv3Jku-LDxy-y9Y4PzHOCe9lCt9pAoyPaELZ1UOLCaUo6FXcXD1J-fNuqQ09Rv5nXZXP14EKj96vgC6FvbM3mrN3j_Fj88FouyRgQ1YFdHTPgfhil_dhXLT0C9Ir7HY0s7oLOv2o-QHuN2PSsWdRNPIFyFuDjG0qJLO3AT1k8DrqD3S-DvfdJ7tGTVuO-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kjn9PBYwU2SE2i6Mv77pXp6aUZ58MYRMtFViMVikDDktK_Q_5D6YNAIjOlB0EK0UL0YqQk-vuAFnJNSfR3G0bloeCawnc7komEBbZH6M2DnzRhFPNEMvms6tfmv2ygoS5F_fhF3KmjFJVvTwo-_Jbr2wAsgztkDv-OHtYnTxqH81R6Y-V86SU6hg7jcS4l-ocutMEpTMtU_rK1h_AtrZBLft2_LgYeH7vPwVRXta6hVUg5Dp6Gk-VFJbNnpGLHYycHPk73AaWegJygYTjQ2w8MEa3MhJ0nRyB2Ywyz-sNsRE9PXsg_S1tLK1F1EquOm7AkXJjAuB_le9G1iIHJ9wfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jrpqI8RJF3keW90XbTaL1k1LIrNaBGEDARFWH22U7s5LTffFP4SecHHHmnKZESV9FQyGx7xAEvuVkGFKaQQWU5gAv93cMNDqAj2bV2ZGyn1lQJq1oLT6MYnmwxU23aKxC5fdTH6zaMlNl5iUaRWTYrzRuJN__Z0YMTNd09k7sl3k_QqOsWB1T1JX_uQ02z6nAP_xbBJZTEecIx-ImVapWBywuVqXwe4shYNzdJT4UiHs7XDSYbZie26pwJD7Xlg5oLbnVt8vqcO8g5WbGijuuOv1RqZ8Vj7C6SLQkKN12Vsj7mpstvPTVDrhpRRy-qN4ZhbC2f3Yb9R2RCapvWDu-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZbDTAExNTNdq2Zt9rJCaL7mmI_QOp_Y3ETjZ3UkwPQ51_ELw-Egx4yNVBM3DIRrnbpOnmIuu7NSCjZZV1E6_NkrZwF-yAkHN0hVUYb-l69ord443oz0Mf5R3GgUA1aIYQ3oIG_eFA1Wx3equbvrdIQgjd-C5FPQVHpIHAXXjhPKGqPHSBJs0Db66EeorVTAqZZ2Ty_d9y-9ZLSWDxTROSp82PLfMRxr7BxP14EJd1xxyibDsHU_wjcXzgWee783Xo-sCK1jrpamzfNuuzr_nhXRe7AYv8HMOjKRBaeBAt6KbDpExlb_B-QOru_UNj-Btb6s9p0iKxvyud07KT44kkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TB_KLhf-RpN6YxZPgT_6FjOfSIN89-IjLQypPtsoVV-tl9q7-Jpgv_C3swmHesoWd2ReYvLpd8PPOt_ahejCresEyE8jp_38Z6hidyiz80XjxZ990FYrWduVYT3otns6SOmmH0o3KOTi5JDNUOmZwpNoPUjnLXlVWjq6HDDQcYjgySQDhpLt2tgV-Ht3vW8fkB6T0d7YICne0QzZ6WOP9e5ZEWdsqdbXR5KbrRcQAPGWYFGY0UGXoYAmLsjl826mKlrmxDm0jCxSs7fbLsnbvX5qQ54Eyx0I8yzUeH0Rq453IAlCyd4K7m1tyrB_fqcDe9Jp1EZMgEOG43QnPdCxTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pIODA63B6unorVKJ-LeaEYh01dqU2Yo-D5uWb8QUYWz68RUsScvaxfCx6dCYZPa4Yac-RCGLNUgwUO70C4M598kJrn2aLV9NywcC-wMVzk_nF4H9OaqtLJUpQSjf7xgN30h4NKYUYzUYvSwEoSJ2m4r72EBXPHTnKAnU-RfjyMtj7tAdz_ZF3MAMe7VRZQdqDUBv_CbbD_w77W3uDClZ1gaj_ByHK2wKJufB8awR-86Nd5wnDaHhhAMTz2eu4EDNYs7OsUtGyoOCZQXyRbczJBITfHmasrRNXu0-IgSd67qci-wDfawGXfzZeilsbEPuYLQTHNhVp6BWqysY-uRhxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rYesyr0F-igKGVnEW7GoKXollmJQB0Kod9n4BJUZtyLgfj1Md2xe9yjqzGnPN3eCs3iitKFt6FWrvTWYgcIp4XcCB12Pjq4OqY-HBpUSCVC42pRTK4zvoXzwQVIoxsHy6nFXFPD6Rtmbj0KoDzjljtlp9l5u3pHeyujoOvUEknk7RJI_1CZYECh9wPvRFyVO1tZsTUyUsAAZE6-VUFDLordPz89uJGUhGGc5zDdwJiZCq_TlGl5eL-wx5urYHThHC8E9o7zzLzAdQ4baxZpkvRbJLrdCBnxyMzXqdzQNrD-YpbUIWXxCMpbsBXWy_-JC_yiWGOHv3q7Ya9rdTRmfNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wq6zoMqg8n5hbGKn5ZMfOyB4T4VPlUbKmrqtCmZGTp2gCtw13TECiG0_55y_KtVmoK4i57HDJoxJC4A12NLGpfVeRpxLYKd970pk1-s9UxdyDYCGnVyP7PRuEP3J5BGKHaJDeZjvPC9nFQfrjZsLsVs_NJhRZ8J98V_wABXW6bEoyVe9hs7O7kWTSzmT3CM6OhAN9qNfuJUjJW8--7JC-dxV-ra8i5IVV-Pg16IpeG-zGYr7NJNjXT81KRKvPqC31VNtEaAW15sIht4d4EVCOi1mOU2xnipA6pewQeSMXGK-GENauntnujfsxcj-g3hZ909zqS-sGygJUxiKjhjgqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lWBGsiR_Ee10SvJWqdUCsDJP6iCACpFCB9JNfa_JlrJyCZXxdxwcIZQpAyW1UVJ0QAckiDAKIif1KD02EAqKeHPESuXEEpdyWiFZwoPYaj2Ife0PY_rWGmX3Mx0tV80_fJPJGJGkNndio9pc95T_oSjLwtvKUnfj0C2PDlBqkdddz391r0z1hdXqzdQRL0VSnXo7jXfm2xgb9MhNiFK29aL6aKca5J5sZgDzsR5Hq0-dlAX--k0p4NyoRXRmPdp_MHEqskl7EVZfXkcTIXoVPjPZoR_kNtCxo3_itRzqzH4ftAGRrKJvTmXcivqEc-iNN1NmI1RiiDWZVNbDs6T0Lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/439112" target="_blank">📅 01:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439111">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qj2r0u6mukWCmpBU0H6d7akrKk5FPo4gNFQUveuPocJEHI3NfsV8q0PFaOYOtdOCJf00qLIvz1W2lpOwQEno_Nl5IsVt0IUFycHocw8Ek1o6dQjBqaFENAnjUu3EnbB-768hCievuCi9AF4CwaJxN6dSUozd1Lqy0XD_1WCGeHgeqxKt_gF2-l8obYatamKE30HBWTDPpM8_ew9g5RY_wEjhYHb2DiLe9E1czAAQQtdXE0Qa7AECXD7CpVmOFMX2u9bVGGOoLh3Rwwha95AMvTL7ImP01H7V0Qd3rUEkVi6zF-AD_QcF_qoh5RenYhR1BmT3a9dwsUI4wJU_5_O-ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«آزمون‌ساز شاد» پولی از کار درآمد
🔹
در حالی آموزش‌وپرورش اولویت برگزاری امتحانات را سامانۀ شاد اعلام کرده، که آزمون‌ساز شاد بسته‌هایی با نرخ‌های متفاوت ارائه می‌دهد.
🔹
از بستۀ ۵۰۰ آزمون ۷۴۹ هزار تومانی، تا بستۀ ۳ هزار آزمون ۳ میلیون تومانی در آزمون‌ساز شاد به فروش می‌رسد.
🔸
در صفحۀ اصلی، آزمون‌ساز شاد به‌عنوان «مرجع رسمی آموزش‌وپرورش برای آزمون آنلاین مدارس» معرفی شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/439111" target="_blank">📅 01:22 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439110">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdRKXo_Y5f7iVemsMyONKWZykB8sxaycGnYDeUnHZITqeFmrTvFf5jtSGMU9ZRm2gGhg_sxM7hJbOBzBLuu7kNvlpJ63pHoCSnaK8oT5t4OVkcAMrFpNu7zYimWeNnUSiJMb8fGD7rRV8mqMw3uXk3J_OXkOsCPWU4XyGhiTHBDXJPG7W0WgtEa1Da0qKyIWL8PuYbrqyj-WUN9x9HeoiT6HboPO2TEeOn5ab3StRQa4MCXMosP_GxLANV6lEPbAKCj9utaTlieTJ1fjA2juafysNvJqBG3yc5nbMCUOzG0KM2Jp8DeLx6BY7Qr0xOGUIx4vHfy4jyNlxCPUPDSYBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست باز ایران برای دریافت عوارض محیط‌زیستی در تنگهٔ هرمز
🔹
رئیس مرکز بین‌الملل سازمان حفاظت محیط‌زیست: دریافت عوارض محیط‌زیستی از کشتی‌های عبوری تنگه هرمز دارای مبنای حقوقی در حقوق بین‌الملل دریاهاست و می‌تواند برای جبران خسارت‌های واردشده به محیط‌زیست خلیج فارس هزینه شود.
🔹
آلودگی‌های نفتی، فعالیت ناوگان نظامی خارجی و خسارت به زیست‌بوم‌های حساس خلیج فارس و جزایر منطقه، ضرورت تأمین منابع برای احیای محیط‌زیست را دوچندان کرده است.
🔹
در نظام «عبور بی‌ضرر» کشور‌های مجاور تنگه می‌توانند برای خدمات دریانوردی و جبران خسارت‌های ناشی از نقض مقررات، هزینه و عوارض دریافت کنند و این موضوع در حقوق بین‌الملل سابقه دارد.
🔹
ادعای غیرقانونی بودن دریافت عوارض محیط‌زیستی از کشتی‌های عبوری، مبنای حقوقی ندارد و این اقدام می‌تواند در چارچوب قواعد شناخته‌شده بین‌المللی انجام شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farsna/439110" target="_blank">📅 01:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439109">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">۸ شهید و ۱۹ زخمی در حملات هوایی اسرائیل به جنوب لبنان
🔹
وزارت بهداشت لبنان اعلام کرد، در پی حملۀ هوایی اسرائیل به شهر دیر زهرانی در جنوب این کشور، دست‌کم ۸ نفر شهید و ۱۹ نفر زخمی شدند.
🔸
منابع خبری شامگاه یک‌شنبه از حملات هوایی جنگنده‌های اسرائیلی به جنوب لبنان خبر داده بودند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/439109" target="_blank">📅 00:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439108">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AePzS7f4Vj3xERiIuxnWrFOK6c0c1EltS7My4UZjCsbuwWDYzwRtj6VtmTkNWYhlLeVivzEvzmfK-y4LAH3MlX39ruZU2lnqi2kzrclNq9Slp05kdX2BmtmkNkD85YBR2R_piqtvgZwh3gwsfFZgF06wRj-xArqALSYVCGCXvaRylP5xGKJ1aaarvNvDTY3pB3sK0-V7svfnMgYsB6G6Ehc02SbgHhZEmedvlvL_CctoglVS4Wsb9FeKsNz0Gq04yxzlUkhGdKVOkGktTOVjanY1ST7cKKdkWmCq3RrfAQYBGOR4HwGUg_jNrK4NknXBziErAM8mwut1rGoSQbJfoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔞
رفتار وحشیانهٔ پلیس هلند با یک پناهجوی باردار
🔹
انتشار تصاویر برخورد خشن پلیس هلند با یک زن باردار در مرکز پناهجویان شهر «زایست» موجی از خشم و انتقاد را در این کشور برانگیخته است.
🔹
در تصاویر منتشرشده، یک مأمور پلیس این زن باردار را با خشونت به زمین می‌اندازد…</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/439108" target="_blank">📅 00:48 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439107">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qFz4DBNd6MEtL05XmSIhaRtDfCH8XsFQvtWAgQlLho6uwfMHEWtCYhT2tqvBLWCbnWwSdJulb-sHfLnGBDkpjRTXgZLnma8362Jbmasi5t-NeO062_3L15zdNRiJF6J7U9MGFA2bLh17ZDht6M3F1smlJlLEO2a9mrju7xXi-Wfto2UTXc-VfT1yWYyUGtQpRVKJY-mBd7yK2PcJGazbSfXsFsg81t-knIA7wjE2vjtut_YMQHEgfcf4EPZ96wvpDFIG5tB3e5D0Fws7xWZ6rBb7JdgtTbE_gj2izWMZseGQHE3hvMapwv9z2TWYJGG70icZ5lQUYh9806agjHmISQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معمای سهمیۀ آسیایی ایران؛ پرسپولیس جایگزین سپاهان می‌شود؟
🔹
در شرایطی که سپاهان تا این لحظه نتوانسته مجوز آسیایی را بگیرد، باشگاه‌هایی مانند پرسپولیس، گل‌گهر سیرجان و چادرملو امیدوار هستند به رقابت‌های آسیایی فصل آینده راه پیدا کنند.
🔹
مسئولان باشگاه پرسپولیس در روزهای اخیر رایزنی‌ها و مکاتبات مختلفی را برای بررسی این موضوع انجام داده و امیدوارند در صورت حذف سپاهان، شانس حضور در آسیا را به‌دست بیاورند.
🔹
اما قوانین موجود دربارۀ نحوۀ جایگزینی تیم محروم شده در چنین شرایطی شفافیت کاملی ندارد و همین موضوع باعث ایجاد تفسیرهای مختلف شده است.
🔸
برخی معتقدند تیم بعدی جدول باید جایگزین شود، و برخی دیگر بر این باورند که باتوجه به عدم برگزاری جام‌حذفی، تصمیم‌گیری نهایی دراین‌خصوص برعهدۀ فدراسیون فوتبال خواهد بود.
🔹
باتوجه‌به سکوت مقررات در این زمینه، به نظر می‌رسد نقش فدراسیون در تعیین نمایندۀ سوم ایران برای حضور در مسابقات آسیایی بسیار تعیین‌کننده خواهد بود.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/439107" target="_blank">📅 00:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439106">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">فعال‌شدن آژیر خطر در اراضی اشغالی
🔹
فرماندهی جبهۀ داخلی اسرائیل: آژیر هشدار در جلیله‌علیا پس‌از پرتاب موشک از لبنان به صدا درآمد.
@Farsna</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/farsna/439106" target="_blank">📅 00:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439105">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14c385a45a.mp4?token=RgKZ7bum21SrnYq62WxCfX-lqTNAvB8uZM9oeZf9r1cn5a_pKpoM9nQaIdht5RP22cbUMY2gxgDhjlcHXThmYcKXoDLYrh4I8sj2Jyx9pilLNKfojIuYV0BoG7I5qpf7uzPf9W_qki5vTzDKhLsR2oPJTnbuwJUQir8NQIPEUcNBYsJjdUttSanlzA7CYNHvaqmK_wFxq2wPYuNQJeXhE6v8pfLysa8uJhxZwmbzrVCHpp1eXSoimAhPrPywaDkuvn1WnOWYr14-f2Kb09pXdTjx3nuKbWawYjsQPOCc_piGn6obrLMkWd3Hhpa9KKuqLrSx78-az1ATMrDUq6f8HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14c385a45a.mp4?token=RgKZ7bum21SrnYq62WxCfX-lqTNAvB8uZM9oeZf9r1cn5a_pKpoM9nQaIdht5RP22cbUMY2gxgDhjlcHXThmYcKXoDLYrh4I8sj2Jyx9pilLNKfojIuYV0BoG7I5qpf7uzPf9W_qki5vTzDKhLsR2oPJTnbuwJUQir8NQIPEUcNBYsJjdUttSanlzA7CYNHvaqmK_wFxq2wPYuNQJeXhE6v8pfLysa8uJhxZwmbzrVCHpp1eXSoimAhPrPywaDkuvn1WnOWYr14-f2Kb09pXdTjx3nuKbWawYjsQPOCc_piGn6obrLMkWd3Hhpa9KKuqLrSx78-az1ATMrDUq6f8HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تاج: مسئول میزبانی ما فیفا است، نه آمریکا. با صحبت‌هایی که با مسئولان فیفا انجام دادیم صدور ویزای آمریکا برای ملی‌پوشان ایران مشکلی ندارد. میزبان مسابقات برای صدور ویزا به ملی‌پوشان تعهد داده است. امیدوارم فیفا مسئولیتش را انجام دهد.
@Sportfars</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/439105" target="_blank">📅 00:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439104">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qleJuGusO-7Q5qjXXGoQDxu3cTZVKw2IvSLQ1PSiFNzUdSr9-ADHLRHMn_xFl5pdV5HxY1k6OsOglvA-V6o1jNdiSRYgW1ROnL7lbnE3IRApv8Vdw1cioeh6llTej3yNJrFGwAuISTM1SZdDnXKQXDbJcbxnMYbKOv7COjN_v4_Ic3KgqdOLNhZcnMGT52Idt0zvMtNwVx89HIogb4cdLRMwPNJdmgLYun58RZ3IeWSsHfEysoKZ7q_PqfOPBrTtigU3i60Bj87cYeg7vxAgTyoDudO1tGr2RKU2jEQO6HEq6m7ldBT092zcQowpy33LaFutc63RK92RTAGd_4i8Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرد شکسته‌پا و کاغذ
🔹
پای مردی شکسته بود و در خانه استراحت می‌کرد. هرکس به عیادتش می‌آمد، از علت حادثه، چگونگی اتفاق و روند درمان می‌پرسید و او مجبور بود بارها و بارها یک داستان تکراری را برای همگان بازگو کند.
🔹
سرانجام مرد از پاسخ به این سوالات تکراری و بی‌شمار خسته و کلافه شد. پس کاغذ و قلمی برداشت، شرح کامل ماجرای شکستن پایش را روی آن نوشت و بالای سرش روی دیوار چسباند.
🔹
از آن پس، هرگاه عیادت‌کننده‌ای وارد می‌شد و می‌پرسید: «پایت چگونه شکست؟»، مرد با دست به دیوار اشاره می‌کرد و می‌گفت: «شرح قصه بر دیوار مکتوب است؛ همان‌جا را بخوانید!»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/439104" target="_blank">📅 00:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439097">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DpQKJ_yJT8ye4Q-GIWi7vfdmLhNB9kG-77PA-pv2CThXSbEZtAnswxCtHCpW_w7cYfshHI6gBg4F3gZsXq5XfQesD2k2BnMhVBiJSO-jhVupHPPVLxM9YYAcZGqcTEV5PRcFhtoYkvu3Iom-3qRFSJ5FkMyZDwY8JfWKr41IHpwmHzsZRMO6UpwpkmjcDxxfsYbqPjt8KjX5xv_AWq6rQ3Mye7LZf9at86Qq6hIGKgqBXily04bRWkKVgwmXrsxqVhh1sHNH9dWZokkebBhbZmWXx0KoaWZhWCC7UYNUXXEi3-2CnBUcpaf_DbRW9jbL3WEuSoQXn48fPENywrLsxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UWFMhQF_xecPcBSm-tb4NRAwj9hGWHO4blSgcWbOQEn_-5sciLsVIcMvUwf-DhFh7TO10cCinrr7xWDSb9aHbajSd8eXxOvM8z8mIvqZdgZkTVCX3RmiUzVLG42x9YoNKNZome-C-0UGNgHSB7_P8oflBzso51_7NGXN4JNS6_BUTZVoLZZZwxW0Yfp19vZmlQeqHDg2OJawQEwvEJmBZfpLMOkOzAL4iqcbNlg6KyWMiujfFdaPQE-RTM79ARazSjZnca-nJ2pna8deRZbMlFS3DlwDhr0Jcj2OrSLGIDkIqQNL9ibJJ_B27WaHdoD_toAcSfCw66FzalLY22TRqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZqiKsGfSMNforDVkyFJNnoaPsJ4txBh40Ykr9bUMtlgs94JfiKmWg4Prb5QrTinEIKRNKyNq7RMvrSDN7nVowLNplRzlO-jQboo0f8dQcZmSadfSlWpJcbeq7V7ZdyNuBhvcD5FLK5K8dr7KEDof3TeQHSC5C1klhFm_dO2WurFG2mLK6VCT7S1xv8RuGUDELbIRvcy8spikMFIFtJigbxAsYerqVApNQ7dtS8dyrMZboYtY6HJY830WoFmBIEy7lCNA9PugwpkoARZSKaXpnPLAQjaygrTxg9_oobj-plsCjlvSqWFO5y5mOnZABqKs-H5dPVG_bKpw9ankq78dYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SCINTFo5c0rg-q8cA6ljJSZAIekj01lOv4KuRIZHYppgY-31Xg1TZynBybBIHWMY7xTeBmqj8RgTC9x59kSrFEO24q4L04Kw32z5P1Hvb_9k2rA7QBFYPDKTuONTKwdPFG8kWnpMbc2ls-v6E7WX3ixnq-u1HyHqkf5vmIvLkldMLTtnIKp8d6mXGM8Sq5nrOnK1GGjpRcB75Kq2jd48Pxa3pv0DfeeCjpCpUsauBrmDyjKiMKJz_AO12IZXjlohFbOWQPaNBl_HV1Zo87bi3jeCriD9uUkC_hLTZV0dmu4Mke63pygzwp0SYcqk9vdHNRrfgvy57zpxUivmabMaBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fEtCfDlyGNJoZ1YIetHLEggWafm3OMrWC3zgSL-1wN1OYdcT2beXPHU4KPHnbUKOsZjhacbJtReW598jaKc64STVVnWveb513DTNZqtB5qXQcWl6G4hiI72FsYOLC25wSAfdJFN7J8HdtOmhLUUDQIW7GECFIed7HMSsVSLWFvdSZXMjquS2mYli13R_HGORTbcWlJ09xlQQVTMrd95DvS2KnRMi7JJTdyAoYksoXqfn8ra0Z90TGANDUIUDGPmbacvRtZOZ8phVxsa8FyaKwaZMYqP0O9S3_GLeVAkoQZCwTFJO6jL_xpLl_BfH9br0uMBFTGp0yq-fWy9jRO5okw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sYkGlMm3bVd6AWcvwd93nU9mJDnUUa5vtqxT_7Ah0vddaJxy3z-bA-rdZC8SABzZb6AIGcg_Cws7x5Cot_f2FjS52jCLLdjKd3rLuV9Ns3uHmvQV88d8u91APu8x3mqWEE13yiYboEY24zUIcmRitbjOwGfmqj0_2yHPUbViwMVzGLCqD5MBOEc_XxwHiJsrQUNsv4uVGQrX0YebrZrv2BgvsG8TYM-CDw7Tz8u_3YUpoFc6PF6oes1Ev2UPsWr0PNSUTZgVLBjBoHiFvzo-zm5QQOSOT3W8Zow-9Gq-DyFCuplj-0PuEGlNR0gFTwdJ2oKVaRz-RIzeImKC7KUxFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q192qZnlX2_x6jqVzTkd8-VZNOa9C6ImZv1_-vYDZvVcc0rCXOsei-1m6WfmzsuJJJwwUXODivS2SEJ91dcBb9jJMIQ11YRYEe3Qd4iiHUASshMuvdVcy9KhDiHiz-BIORxLTf7pce8ytIMfOj4riRwAdKBfGNmCsOtgaDMLbrZoOEHiFCbuQ1kX250Kb7sKPVvmvvlObHi4Z3WzTpEsL5CEmkBI4WcjTXQv_frsForBmm5egjmlmUc-xKsIeXkCUTVP6-llPrS2SOExHvn0ODrnt6KcQwMOpODplwbVfC6NI4bTYR6lqRKDHGdVepkkrO_Ru7mCwcpKXhlrbN1mfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
گرامیداشت فرماندهان شهید سپاه در بندرعباس
عکس:
رهبر امامدادی
@Farsna</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/439097" target="_blank">📅 23:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439095">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ada0223afb.mp4?token=JLGu-QfnQiTY04P1AeKvaV6p0VjrkmGB2iqsh5KTqF9wL4ax2yl-bfqAWvESexw4Ut82aJQNk6SMCRw7nVHnus4GpjlznWm0KvVuZa56XGUtDW09Wy4N0XK7su1t4RsUaPCdK9oDfJAawV0xnLw2TPVoEODtIxibNtjxs64V2HtMW85eWK93UGlgkoVac2Uj1tKOCrP_1mxduj3kto826Ot-_WkDt0eNpmfOIgyN3xELZs11tXVXgsk8rWqaeSx5OiCDfiVGIB4DbTWjcXXroAoO0A7eG3_CAFYQXwO46AznETvx41JkmgZzIYZ_prBPGzGkZJJVgxQ-PtgcO9Bj1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ada0223afb.mp4?token=JLGu-QfnQiTY04P1AeKvaV6p0VjrkmGB2iqsh5KTqF9wL4ax2yl-bfqAWvESexw4Ut82aJQNk6SMCRw7nVHnus4GpjlznWm0KvVuZa56XGUtDW09Wy4N0XK7su1t4RsUaPCdK9oDfJAawV0xnLw2TPVoEODtIxibNtjxs64V2HtMW85eWK93UGlgkoVac2Uj1tKOCrP_1mxduj3kto826Ot-_WkDt0eNpmfOIgyN3xELZs11tXVXgsk8rWqaeSx5OiCDfiVGIB4DbTWjcXXroAoO0A7eG3_CAFYQXwO46AznETvx41JkmgZzIYZ_prBPGzGkZJJVgxQ-PtgcO9Bj1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرار شبانهٔ بجنوردی‌ها به ایستگاه ۹۲ رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/farsna/439095" target="_blank">📅 23:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439094">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a31e292e4.mp4?token=PUCRirAM5da2KIPAfRBOtJ4DJ9y1TE4g_AtGFQjq2GQVGhUI6MFYlvjDbUJjNG9UeCM4X5PxwZ2E_T5mHKH-mRkBWIlXbmjppB9nJFMj3t4ai_I29UsIz6gofJudrMobdYG4g5lOR-veSjZOCGu54MB3dzmo8Z79hdnS6h-Yz2it0KeV3neKliQqkq9HXclydhtIqMbKFQSTd4c-NpVoy6LP27KL3f6Id-vS_3KpgNcmLkl2ajBivVjDRQIsCiIwRduzNRD3msw98EF4CBrOn-vFo-DL0vTx9vlExYzuOLCQyvNPI-_tX_PBN6rlm57wL0zFHsSFTqcBEf_kK56q4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a31e292e4.mp4?token=PUCRirAM5da2KIPAfRBOtJ4DJ9y1TE4g_AtGFQjq2GQVGhUI6MFYlvjDbUJjNG9UeCM4X5PxwZ2E_T5mHKH-mRkBWIlXbmjppB9nJFMj3t4ai_I29UsIz6gofJudrMobdYG4g5lOR-veSjZOCGu54MB3dzmo8Z79hdnS6h-Yz2it0KeV3neKliQqkq9HXclydhtIqMbKFQSTd4c-NpVoy6LP27KL3f6Id-vS_3KpgNcmLkl2ajBivVjDRQIsCiIwRduzNRD3msw98EF4CBrOn-vFo-DL0vTx9vlExYzuOLCQyvNPI-_tX_PBN6rlm57wL0zFHsSFTqcBEf_kK56q4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این عاقبت بی‌وطن‌هاست
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/439094" target="_blank">📅 23:24 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439092">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🎥
نوجوانان مشهدی سنگربانان خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/439092" target="_blank">📅 23:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439091">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🎥
بروجردی‌ها: مسئولان بسم‌الله حمایت از حزب‌الله
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/439091" target="_blank">📅 22:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439090">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">خلاصه جلسه 1</div>
  <div class="tg-doc-extra">Ostad Khamenei - استاد خامنه ای</div>
</div>
<a href="https://t.me/farsna/439090" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
جلسهٔ اول اندیشه اسلام از زبان رهبر شهید
🔹
این صوت، خلاصه‌ای از اولین جلسهٔ سخنرانی رهبر شهید انقلاب در سال ۱۳۵۳ دربارهٔ طرح کلی اندیشهٔ اسلام در قرآن است.
🔹
هر روز یک قسمت از این جلسات به همراه متن خلاصه در فارس معارف منتشر خواهد شد.
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/439090" target="_blank">📅 22:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439089">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">برترین‌های ورزش ایران در سال ۱۴۰۴ معرفی شدند
🔹
بانوی ورزش ایران: زهرا کیانی
🔸
آقای ورزش ایران: امیرحسین زارع
🔹
بهترین فدراسیون ورزشی: فدراسیون کشتی
🔸
بهترین تیم سال: تیم ملی فوتسال
🔹
سرمربی سال ورزش: پژمان درستکار، سرمربی تیم ملی کشتی آزاد
🔸
زننده گل سال: مهدی طارمی
🔹
قهرمان فردای ایران: مبینا نعمت‌زاده
🔸
بانوی پارالمپیک ایران: هاجر صفرزاده
🔹
آقای پارالمپیک ایران: علی‌اکبر غریب‌شاهی
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/439089" target="_blank">📅 22:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439086">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sFGORqXHaGDaVy37VkAeLKUKVH8GKnIPxpSB4IfcuenLnK-yKuh5ymjWAtChmop6nDAFfLK0FguTlsKsJGCmEf9vPaS6z8FaLgNgH7UlUqF9yprMnPIaVVW6emL_3ugEVdUUUWNCi8zXYCcOBjPtOBrd_AyEhnMtI5zSG5IVHeBfiz5-gX0ZFeV4Rev6AaJaMBl0yFwAXxiPf4Sg1LSck1iZYVTCURohcB6idv4scp0alve528bVbqs2kLlkUdZ_eS1UPCVmlZNMEA91l4ogfNWC7ZWP5O88JCkTuMgHO72lJEH1R3okHMY77bd8gIi4o_GUEaQ2SPY3Rt0jn7wBCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XGwPdARTuOSaaZlW6ZflZSdpo0tocwXQpSbpHsaCqx4aFOB0VYOIDihK-8U1-D3HLkDEWzkI97_9lxonS-CAK5w_CrNe_lc_S0nNlbo1l3sLJjSMVE3NT6EmWM2VF7uw55ujDsI_u1xuuHJEkGuK0sZ37Z7aaVCboVruWFZKvX3pFwfE-0ZgGVgcwhS2HmdtZE7t3zId8z6hCeCierksQNaXdsbG3e8kKaaIVtCbEmJIpncAg0iTYSlGVeKcdhSoaPlZwuJU1v82s8NE1ah3izHfGkxBo5oePUpG_kgZ5_167FXFZeqKjE8A9IJGRph3iMk76-BgwUY3ZIHsF6GcoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JWpuKHB6Khj7CtY9k6yGLbv-h7QYnnbpxGBV1SRJ93f1sGV3lssDXwATVBVajtHN66Og6nkyedFH1rIAzeDQAte7YYb4dMlSfQEBdySpZ2VhVDX-9xggBX764BGsJGRoU_JyiCusj-6lyzcZs2SdIcpMqztueWkxPQGrpSylsh6gEJPrpTUZ7T49d4O2y8IKnIRaYMX2x_Xvgt710Uq_ZbrdVUyBgJ6GPQiT3auKykRwxrrcmETL__FLjjC5gUe_ke10JDpW7IVY8CBlOeQ-PFgsfpSLOdXOLjmych3t7hFPQqq9ZwG8-LrGNwDXqrbeJybOJHiR4ky_hZd2w5W-Xg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
پزشکیان: روند را با قدرت و با صلابت تا جایی که جان در بدن داریم ادامه خواهیم داد
🔹
یا با قدرت مدیریت را ادامه می‌دهیم یا شهید می‌شویم؛ جان ما که از رهبر شهیدمان بالاتر نیست. @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/439086" target="_blank">📅 22:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439085">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0142c54c85.mp4?token=v_rBo0jDF09_TWzgvvQ24KDIxkpXXiTcZZFvg_rDxFNM_KkJOx-QS9Dfgu78aY0VIbXKSzHoVm0y3XwbK17VqcceNsaOn1nBIbUo7C2OgKYETXwlQLle1-mb5MirPPKxLH43yX65GMuA_5pVmsIM-YgqYjmStyiJTDWXUIhBcd3Sg6MV3pyvUYp6vNKMlAdEArbTKu_oOgI0h-2ErzKnf4RYKajyIut5czBQMwo7wgoBVzSa_zoK6tW8_-ssuN01U_uakDiZODsxj1LxVMH5m5GrGcdpdY5KI1iW9LAIujS7H6UVLipb4ezN0Sc5epP2vU65eFISrks5c1ywaVllQlUAvZg6NEtThA_jmxnkY4vgoN_-JCKcwfjAGCGme5lfi2UZg6Z3RLkmDMVR1LnvXLk94b0j31-GjEAtZP70S7ct4kq5MAH-b66Rey3N7zeMNasItlYy6iWVFGVPLWwEDGD4XK6q78mBR860mosQNgLz7nhxhYuJ5R_FlrzZLTAoQ3Oas72L_uEdJWRYLqJG8DKppOP-XvuCCOZa2u3e1dSzq66m7npPPyXrRz_2v05GHV2f59Rgp3RyKedd5cLy08iSwEsTXBdV8CHdU4nRDIPX1Kl20e-IPLWI1SmisHHJsZLFpn65yeP_tcHEYqVAOrmPcacd73YYDIRVIoFMaJE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0142c54c85.mp4?token=v_rBo0jDF09_TWzgvvQ24KDIxkpXXiTcZZFvg_rDxFNM_KkJOx-QS9Dfgu78aY0VIbXKSzHoVm0y3XwbK17VqcceNsaOn1nBIbUo7C2OgKYETXwlQLle1-mb5MirPPKxLH43yX65GMuA_5pVmsIM-YgqYjmStyiJTDWXUIhBcd3Sg6MV3pyvUYp6vNKMlAdEArbTKu_oOgI0h-2ErzKnf4RYKajyIut5czBQMwo7wgoBVzSa_zoK6tW8_-ssuN01U_uakDiZODsxj1LxVMH5m5GrGcdpdY5KI1iW9LAIujS7H6UVLipb4ezN0Sc5epP2vU65eFISrks5c1ywaVllQlUAvZg6NEtThA_jmxnkY4vgoN_-JCKcwfjAGCGme5lfi2UZg6Z3RLkmDMVR1LnvXLk94b0j31-GjEAtZP70S7ct4kq5MAH-b66Rey3N7zeMNasItlYy6iWVFGVPLWwEDGD4XK6q78mBR860mosQNgLz7nhxhYuJ5R_FlrzZLTAoQ3Oas72L_uEdJWRYLqJG8DKppOP-XvuCCOZa2u3e1dSzq66m7npPPyXrRz_2v05GHV2f59Rgp3RyKedd5cLy08iSwEsTXBdV8CHdU4nRDIPX1Kl20e-IPLWI1SmisHHJsZLFpn65yeP_tcHEYqVAOrmPcacd73YYDIRVIoFMaJE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گرگانی‌ها ۹۲ شب در خط مقدم خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/farsna/439085" target="_blank">📅 22:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439084">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‌
🔴
حزب‌الله: ‌۲ خودروی هامر ارتش دشمن اسرائیلی در اطراف قلعۀ تاریخی الشقیف در جنوب لبنان با پهپادهای ابابیل مورد اصابت قرار گرفت. @Farsna</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/439084" target="_blank">📅 22:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439083">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9f63808e3.mp4?token=su3Ks2vtXL5NZiWOi-AOwQJ3WSrs5C5iFbb8m--8zFb5LzVIWDB5MfyJwz4lIYXMTLYBTMnL7TAu9khfJSTRkEAtT53RQOauE1iPVoeFapW8ZM_T2HdcenvHL-H_RHCnGKR2ILm83-_HfHAnogdfitxFoxaa1EvnehysLPiYw3luU0pDFKwK-Xu8TprZZB6Pzzj9fI4vEN41_GTGojFlflAvV3j7Sy9zZEtfZhe7f_ROB9HAK9Wg3TlpBkXsKnxSqVnsAJwVzMjPJzXdxcO1bLG-LH0S6ywPo60fl-3dhnuGgLQxWoMoM1_M-EexhYXp4a1PHHRLEeiT3Q6uzs4EHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9f63808e3.mp4?token=su3Ks2vtXL5NZiWOi-AOwQJ3WSrs5C5iFbb8m--8zFb5LzVIWDB5MfyJwz4lIYXMTLYBTMnL7TAu9khfJSTRkEAtT53RQOauE1iPVoeFapW8ZM_T2HdcenvHL-H_RHCnGKR2ILm83-_HfHAnogdfitxFoxaa1EvnehysLPiYw3luU0pDFKwK-Xu8TprZZB6Pzzj9fI4vEN41_GTGojFlflAvV3j7Sy9zZEtfZhe7f_ROB9HAK9Wg3TlpBkXsKnxSqVnsAJwVzMjPJzXdxcO1bLG-LH0S6ywPo60fl-3dhnuGgLQxWoMoM1_M-EexhYXp4a1PHHRLEeiT3Q6uzs4EHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«امیرحسین زارع» آقای ورزش ایران شد
@Farsna</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/439083" target="_blank">📅 22:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439082">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec99175aab.mp4?token=J34RxgGsUNQA-SaWVIOnGUQSEjzfR8v3HEH5FX5PNf6Ue7FLeINUAL2gKo_mxkFUctn4J2Jv_fVX8ti2n2YkXLQ9lmbnyxDj4fsFE-iEL3t9l2WjbDY5_zIHsLMakdlnz-_Kt5SPrXN8fWqVACR-S04nXDwHHBD3AZL1D4jzcHSv5Zj7TkdKtLyZkWS5FROEOsUtg2rkbn2uEvBS_tkcCA2fw6zRyOUDwoo4xV3F0wrDAO8yTySuHu6f1zEUEDzZu19Dm0fLQye1OqdqoR7hgHQx1He-Zf_Eer3201AAr-THfZY9cE7C70ZpC-ZyuwrIQ2pTnVQmNdigxsi6tEGZfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec99175aab.mp4?token=J34RxgGsUNQA-SaWVIOnGUQSEjzfR8v3HEH5FX5PNf6Ue7FLeINUAL2gKo_mxkFUctn4J2Jv_fVX8ti2n2YkXLQ9lmbnyxDj4fsFE-iEL3t9l2WjbDY5_zIHsLMakdlnz-_Kt5SPrXN8fWqVACR-S04nXDwHHBD3AZL1D4jzcHSv5Zj7TkdKtLyZkWS5FROEOsUtg2rkbn2uEvBS_tkcCA2fw6zRyOUDwoo4xV3F0wrDAO8yTySuHu6f1zEUEDzZu19Dm0fLQye1OqdqoR7hgHQx1He-Zf_Eer3201AAr-THfZY9cE7C70ZpC-ZyuwrIQ2pTnVQmNdigxsi6tEGZfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بهروز رهبری‌فر، بازیکن سابق پرسپولیس: من خودم را فرزند شهید می‌دانم؛ چون پدرمان امام خامنه‌ای را از دست دادیم
🔹
۳ ماه است مردم هرشب به خیابان می‌آیند و نشان داده‌اند که همه‌شان تختی و پوریای ولی هستند.
@Farsna</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/farsna/439082" target="_blank">📅 22:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439081">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f74332a29.mp4?token=lYXIoAeqMv84Zs69fs0g4ZyA33blkfaTKPL_S0PeUM0EFwRIzYDA9EmAsO0X5aIzRDw_aJA6DAa5SgW9oZL0ZTmLs4iLkQ6kq1wifSVcgDFxrZKgZqPaT2n57ZhAgccZUaFA5obviE6KAmgL_Ok5_UvSVGrOPczDkUPQeYdltsgv2E6-eBXnz2Ok2HoVbz42NCenq5SOlbGv1R2kEQIpBGKHXDtzq1eE5hn4jtq9NU7VkxpUo0q_kQ1Ks6nPiCbc4_CxmQq2kIK-bTkbwOVQJaGxDzA0HbfOkRX-0Yh_Q79MX19V8sOLsXrN2xTZQwhyqlHY_Fdkz4qobuozosEjqyNb2n-If6FTOFRMdk8-UfJQiIcWwHXoFw2x_a-NnykeO30KBn5sm3js_CSYjo9r8Di8ZRpEGCiEfQaxGpf83wL9Dywjvz3UWDdyo9ZeV24Zm8yRaTNdyG5rbavHIilv3LeJi-j6twfWczWxRXMyIp_Yar279MPz0vTgbKOSQIFiltYV00GlLfM7T_Sr5itUwkHWzqbQ7gG8jKynGQB9m8Jdfe4EXJk4zAoA2SPqAkyvyHiol7Sanlu54maIV5kFKK367-ngm2i8izmXUg8IoyVMxk0YX3VxmIc0-1-oAnvimjItkU_XY2EMXI9_stJS7Md144sx2GctgkKAQJaZ2jI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f74332a29.mp4?token=lYXIoAeqMv84Zs69fs0g4ZyA33blkfaTKPL_S0PeUM0EFwRIzYDA9EmAsO0X5aIzRDw_aJA6DAa5SgW9oZL0ZTmLs4iLkQ6kq1wifSVcgDFxrZKgZqPaT2n57ZhAgccZUaFA5obviE6KAmgL_Ok5_UvSVGrOPczDkUPQeYdltsgv2E6-eBXnz2Ok2HoVbz42NCenq5SOlbGv1R2kEQIpBGKHXDtzq1eE5hn4jtq9NU7VkxpUo0q_kQ1Ks6nPiCbc4_CxmQq2kIK-bTkbwOVQJaGxDzA0HbfOkRX-0Yh_Q79MX19V8sOLsXrN2xTZQwhyqlHY_Fdkz4qobuozosEjqyNb2n-If6FTOFRMdk8-UfJQiIcWwHXoFw2x_a-NnykeO30KBn5sm3js_CSYjo9r8Di8ZRpEGCiEfQaxGpf83wL9Dywjvz3UWDdyo9ZeV24Zm8yRaTNdyG5rbavHIilv3LeJi-j6twfWczWxRXMyIp_Yar279MPz0vTgbKOSQIFiltYV00GlLfM7T_Sr5itUwkHWzqbQ7gG8jKynGQB9m8Jdfe4EXJk4zAoA2SPqAkyvyHiol7Sanlu54maIV5kFKK367-ngm2i8izmXUg8IoyVMxk0YX3VxmIc0-1-oAnvimjItkU_XY2EMXI9_stJS7Md144sx2GctgkKAQJaZ2jI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت فرمانده‌ای که‌‌ از جنگ ۳۳ روزه کابوس اسرائیل شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/439081" target="_blank">📅 21:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439080">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09b5b05076.mp4?token=OEIlAZGLKaE8evPMN0wybwtRmKSwYYyphRYh5aFfp_zZGp_c-CEwGG1DtVSRl_i7fnUvzGRZEjoqjRReu-mqeFWMZ2mIQKMv4RXPf-GpcF-8zeMfK3hh5z3uCY3JKK33fQazN5BhmxOg7K8hycJB75Css8dGfJ_QX3bsszgttJ9fM0lLEozYDmVXBqhVz0zn-tZTN9BfflQ12MMHX95dfb4gTLDpjGWSWtBPtZ0nhfjGEF9O9ofxvTsBiCxjfn-8sLF7GDzskdsUXZypaLvi8cAVvM5KGjIplRGUW-MIq-qQx9c-Vzz6aEfl8WencZH-Qp0k_TmU4xp6m5E3hF3mPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09b5b05076.mp4?token=OEIlAZGLKaE8evPMN0wybwtRmKSwYYyphRYh5aFfp_zZGp_c-CEwGG1DtVSRl_i7fnUvzGRZEjoqjRReu-mqeFWMZ2mIQKMv4RXPf-GpcF-8zeMfK3hh5z3uCY3JKK33fQazN5BhmxOg7K8hycJB75Css8dGfJ_QX3bsszgttJ9fM0lLEozYDmVXBqhVz0zn-tZTN9BfflQ12MMHX95dfb4gTLDpjGWSWtBPtZ0nhfjGEF9O9ofxvTsBiCxjfn-8sLF7GDzskdsUXZypaLvi8cAVvM5KGjIplRGUW-MIq-qQx9c-Vzz6aEfl8WencZH-Qp0k_TmU4xp6m5E3hF3mPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زهرا کیانی، بانوی ورزش ایران در سال ۱۴۰۴: عنوان خودم را تقدیم می‌کنم به دختران شهید مدرسهٔ میناب و خانواده‌های داغدارشان.
@Farsna</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/439080" target="_blank">📅 21:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439079">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebEo7XCvdoZEgrK_juh3JspjU0im10_lFXGNEMgGnjbPcEtkfJ5R_iI8JCY88RnY9odBlnfEwTD3q7kdJoNqjBhBzQ-x2qTKq8Nny4Cmq7kiouZOhZrO-xkdtYUhjYlcvJqqOIt4Lwq6fd7gV7SWAiV4SgNl3lTOKhBF9gQBAIKJxnK28Qy48egYkMe-zGPM2fiy32fs_cX5DmfZXw4Wf83zLIE_JaTXN2nv8EIOx-6h4gI7QzschD_kCbrhduNEkNgfCV2pbx4pLpsQcVFRuGyekMM7dklO6Vi6rmn6Ti-E5RF1JO-p5f-KO6wmDsONhMFNmVi9IcsaRcjQHtaBXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
سرپرست وزارت دفاع: در جنگ رمضان به فناوری‌ای دست‌پیداکردیم که حدود ۲۱۰ پرندۀ دشمن را هدف قرار دادیم.   @Farsna</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/439079" target="_blank">📅 21:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439078">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29a71937ed.mp4?token=BiMuAbwlW7Lxm4LZanWc0OwTr7tc6QppzOMZQJEyxWJn5gZA5eucgwjhDn_aGSeNSSsQnt-f2HklxarInOwWgD7oGjPImm-ehAZ5askyna858qtFkC4ZnM2dG2ekQFlTJqtYJt1M0o2CczUAUDez60ryPCqNrBx_0wpj0fIymGbLuECqkSc4kMti63Ug6uS4Vv7yoqUlgMFZJasoMxJjdeODLKN4_lAkNyJ1qGbxpbldfgKZy1GDje2AB2TfUGL8Ivacc8g0XF9_xXfT5sP1pTSfsoM3K6j5MdfS-sf1duKzk6Z2TIJ1yFiHeS6W7bmnD26O59Ro9VXiyX_lz7vW3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29a71937ed.mp4?token=BiMuAbwlW7Lxm4LZanWc0OwTr7tc6QppzOMZQJEyxWJn5gZA5eucgwjhDn_aGSeNSSsQnt-f2HklxarInOwWgD7oGjPImm-ehAZ5askyna858qtFkC4ZnM2dG2ekQFlTJqtYJt1M0o2CczUAUDez60ryPCqNrBx_0wpj0fIymGbLuECqkSc4kMti63Ug6uS4Vv7yoqUlgMFZJasoMxJjdeODLKN4_lAkNyJ1qGbxpbldfgKZy1GDje2AB2TfUGL8Ivacc8g0XF9_xXfT5sP1pTSfsoM3K6j5MdfS-sf1duKzk6Z2TIJ1yFiHeS6W7bmnD26O59Ro9VXiyX_lz7vW3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پژمان درستکار، سرمربی تیم ملی کشتی آزاد: اگر ما اینجا ایستاده‌ایم و پرچم و خاک ایران استوار است دلیلش رشادت‌های شهدا و مدافعان میهن است.
@Farsna</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/439078" target="_blank">📅 21:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439077">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1df801dd95.mp4?token=FJr2qHeeQi2kBW1k4tqpVb3PUJElDvbpjfJNxizAtTAjcQ6JCxsyrhD0_tiFWuf-dLnxO9Wlm77DBBTmx77EX2viqInCNNe4F_nRA_1BTuXCI5-4c5uQiVAUJUHZdPhjpa9eh4j_e7Q50ff_BIx3K5JgXeX_07r5h_8KBrTWoZMkAL2pIY_-IOg4TyE5JMrwtCaxYNlVxG7hKJN7QjevWCp9fq9OWwRkhyYhKQs4BB8Rj2kexyARaKYrCxicXTkrQrcTR1gJilFiHDvs2mFeMzp-b8gsAmnaWuPSm3lyKpM4_Gn8u8EubKY6rEFAmU-Z7ysmzT9cvjvauc1ZJYg7Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1df801dd95.mp4?token=FJr2qHeeQi2kBW1k4tqpVb3PUJElDvbpjfJNxizAtTAjcQ6JCxsyrhD0_tiFWuf-dLnxO9Wlm77DBBTmx77EX2viqInCNNe4F_nRA_1BTuXCI5-4c5uQiVAUJUHZdPhjpa9eh4j_e7Q50ff_BIx3K5JgXeX_07r5h_8KBrTWoZMkAL2pIY_-IOg4TyE5JMrwtCaxYNlVxG7hKJN7QjevWCp9fq9OWwRkhyYhKQs4BB8Rj2kexyARaKYrCxicXTkrQrcTR1gJilFiHDvs2mFeMzp-b8gsAmnaWuPSm3lyKpM4_Gn8u8EubKY6rEFAmU-Z7ysmzT9cvjvauc1ZJYg7Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هاشمی‌طبا: تمام سال‌های خدمتم در برابر یک لحظه فداکاری رزمندگان ما بسیار ناچیز است.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/439077" target="_blank">📅 21:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439076">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6AxmUycal2TBhvn1KnFcrFqbMw66m57Jvk8WmpwAnRAPoXRvAwJ5SZ3BqqY2gmj4cHciTK4xCxcgiTTfQlkEK5VIyyW-qp16YBGBPuSkEzl6Kk-ZtfOQN88axNPu_GMdcXeqSGIK5ypGGGr_Yz1HJSuIh_6yhQiYekYUSKWMYbfQpFZq3cuTn0h2ocRge-kYASnXfz7XoI6m6l0uFApkYBwJl4-_uLao4UlfIpS5_tmzggsgdrId0bH02cNobUHhdgE7lNEGxhhmhOexdZwkWhIZfsRvQlc50Xs5dBQD0hJvvX8P8utkeYLjn4V_qKzjWN-aiYTRwsmYANbBl0D1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر نیرو: مصرف برق ۱۰ تا ۱۵ درصد کاهش یافته است
🔹
با وجود اینکه با توجه به شرایط موجود باید انتظار افزایش مصرف را داشته باشیم، در حال حاضر کاهش ۱۰ تا ۱۵ درصدی مصرف را مشاهده می‌کنیم.
🔹
مردم در مدیریت مصرف همراهی خوبی داشته‌اند و این همکاری در کاهش میزان مصرف کاملاً مشهود است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/439076" target="_blank">📅 21:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439075">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3fc237f0e.mp4?token=ORIX-YZrScqfBXhb8llx6V22jCVYUHHEeFgi_xCfJwyFe8HsQdl2RZwOo-N_wzSjwv7bdgTW5rXSMc3LeCWz3Qc_aZDFM7Ju4s3cGQ1VaY4AQ637s0Ii4EwKOY23X6mZ-Z_rEhDmnbJQ4pedGsCx1JmJfpLKR6J_YL3iyGdi2g4aE9EwzM-HqWzD-7N6xY-abCQOsZTaRLnAX-S3jP7YB6UEveND6uWNJAlH-qFRQ1onzQl8HO5TnQgIgsiYKD_yJ3gx2o5cnktoB_gX2DUMTNk4i1Ebm2OXKTpTFbou_pF795-kfCJ9ER_cFKmtOsr3rkRCTY2z7tUHfQRZjw57AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3fc237f0e.mp4?token=ORIX-YZrScqfBXhb8llx6V22jCVYUHHEeFgi_xCfJwyFe8HsQdl2RZwOo-N_wzSjwv7bdgTW5rXSMc3LeCWz3Qc_aZDFM7Ju4s3cGQ1VaY4AQ637s0Ii4EwKOY23X6mZ-Z_rEhDmnbJQ4pedGsCx1JmJfpLKR6J_YL3iyGdi2g4aE9EwzM-HqWzD-7N6xY-abCQOsZTaRLnAX-S3jP7YB6UEveND6uWNJAlH-qFRQ1onzQl8HO5TnQgIgsiYKD_yJ3gx2o5cnktoB_gX2DUMTNk4i1Ebm2OXKTpTFbou_pF795-kfCJ9ER_cFKmtOsr3rkRCTY2z7tUHfQRZjw57AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر: به آقای پزشکیان می‌گویم از وقتی شما رئیس‌جمهور شدید دیگر کسی به ما گیر نمی‌دهد که چرا کت‌وشلوار نمی‌پوشید
🔹
دیروز هم که رئیس‌جمهور کت را درآورد و آستین کوتاه پوشید و ما راحت‌تر شدیم.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/439075" target="_blank">📅 21:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439074">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fed3a553bf.mp4?token=m1FntmxFFeaVHkZWTZMpgyP-4eko5x9uTaZUyQCTZXLWyC2rvpPLra4zqKSCAtCOi9vQq0bUZfCE0ONV1Iw5C1UD44ROJhWPJ0IPmrgQjp7-zbTzCJvW14AZPTkMZBHOSS9eKqkcsWErFB1nRLkYJgww4-fcokn81N0k8kYRVO4bTTBqoyGgFlN0muovCg0hdZ3A7-JEmqqUdnuuzM5WnZPkTHB-3xN9ZG3jDUvnO8gXVzeADS3qqa9z-CAwclKS6jykx3-IQ3YvEHaRwGs28G2lJ8KJvX3tUF8FXvDo4y0vhYinCJOUVMCSFW3-2eVqcQ8apxm6LsiJPN9mPc4PAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fed3a553bf.mp4?token=m1FntmxFFeaVHkZWTZMpgyP-4eko5x9uTaZUyQCTZXLWyC2rvpPLra4zqKSCAtCOi9vQq0bUZfCE0ONV1Iw5C1UD44ROJhWPJ0IPmrgQjp7-zbTzCJvW14AZPTkMZBHOSS9eKqkcsWErFB1nRLkYJgww4-fcokn81N0k8kYRVO4bTTBqoyGgFlN0muovCg0hdZ3A7-JEmqqUdnuuzM5WnZPkTHB-3xN9ZG3jDUvnO8gXVzeADS3qqa9z-CAwclKS6jykx3-IQ3YvEHaRwGs28G2lJ8KJvX3tUF8FXvDo4y0vhYinCJOUVMCSFW3-2eVqcQ8apxm6LsiJPN9mPc4PAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
واکنش معاون اطلاع‌رسانی دفتر رئیس‌جمهور به دروغ‌پردازی شبکه ضدایرانی اینترنشنال در مورد استعفای پزشکیان
🔸
رئیس‌جمهور ‎از خدمت به مردم عقب نخواهد نشست. @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/439074" target="_blank">📅 21:24 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439073">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‌  فدراسیون فوتبال: شایعۀ رد درخواست ویزای بازیکنان تیم ملی برای جام جهانی ۲۰۲۶ کذب است
🔹
فرایند اداری مربوط به دریافت ویزا طبق روال انجام گرفته. @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/439073" target="_blank">📅 21:23 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439072">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qV_8fBmIF1ZosPLPbS-zvjwIk4kyQqgxtpT4drb6byArdW9AMus8oPCu4yLDsfm_kmKpzP1mEHjAXV_4Ax2IUUnaFJgg2vY4BqBdk2-Dm6LG6gJ7KzS1RMDI1T_qbz4FhI6T-sdedxrs3rdplAzLnXC_2o0GyhU28uDyNBHyl1FYaL6URclK7kQQLmXuugB5bnMsAwS9ZxfBe6qDyirSx6c4p1qDNQhLNbkd8VzLJsE84VuRC8N5NTgg34xGrQ4b6C9cDwn-BlkscQh8P0UvRRMPL_gqsXbTAt_DCskiSy0EF40eRtCdz9RODqvvbTRPwuKhKeYPcxhQLTc97S-Vyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
واکنش معاون اطلاع‌رسانی دفتر رئیس‌جمهور به دروغ‌پردازی شبکه ضدایرانی اینترنشنال در مورد استعفای پزشکیان
🔸
رئیس‌جمهور ‎از خدمت به مردم عقب نخواهد نشست.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/439072" target="_blank">📅 21:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439070">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd63434b5a.mp4?token=HPa0NVQWbjJuC7YDGirv4gMLJh1jVAjeFKz3FBiJGmemrSgEtJounqprPueIyzLWvngehW18UBClTh8oKxObCnbrz7z_jATlmypcCKsR0Ge3TjSsUGPqtTyXpPAi8ze1bX2NeAdscl89a2rzYPAyJC2_mu3zCLcOeuz2ZJY4AJD95uMTHVYrsabyjLmcSJmSSJu1szKfgQkCwX6qFrOzR0QIsOFRbq4ZsxmFSljbr7Pxm4w0SpEXpHS24NhfPbL2Qb90dGQlbxF5I1NhrruD-dwlVM7qwVUG_CuqSZMuxm2gXrH7U7i2stlIt3t-2dDzyqV0qKkZFgQ1ox4xPmQf0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd63434b5a.mp4?token=HPa0NVQWbjJuC7YDGirv4gMLJh1jVAjeFKz3FBiJGmemrSgEtJounqprPueIyzLWvngehW18UBClTh8oKxObCnbrz7z_jATlmypcCKsR0Ge3TjSsUGPqtTyXpPAi8ze1bX2NeAdscl89a2rzYPAyJC2_mu3zCLcOeuz2ZJY4AJD95uMTHVYrsabyjLmcSJmSSJu1szKfgQkCwX6qFrOzR0QIsOFRbq4ZsxmFSljbr7Pxm4w0SpEXpHS24NhfPbL2Qb90dGQlbxF5I1NhrruD-dwlVM7qwVUG_CuqSZMuxm2gXrH7U7i2stlIt3t-2dDzyqV0qKkZFgQ1ox4xPmQf0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زخمی شدن چند صهیونیست در عملیات ضد اسرائیلی در کرانهٔ باختری
🔹
روزنامه معاریو: در این عملیات ۴ صهیونیست زخمی شده و وضعیت دو نفر از آنان وخیم است.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/439070" target="_blank">📅 21:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439069">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🎥
اصابت پهپاد حزب‌الله به یک مقر نظامی ارتش اسرائیل
🔹
وبسایت عبری حدشوت بزمان: در حمله به یک پایگاه ارتش اسرائیل در شهرک «بیت هلیل» ۵ نظامی اسرائیلی زخمی شدند.  @Farsna</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/farsna/439069" target="_blank">📅 21:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439068">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e82e87bc58.mp4?token=fDSTaCGrZEz24nlWXhe6rn_PP_qpXJ9t-FTApruy22mtkW6zYEEQvM9h66EOdMJxDzdg6AxdHnN2Z2zKHW9vS_BK_GeTHdW1OU2_tpk457uYUjH1A_8ClIViYBx9Bu5Hvr5kB6by3ZdBwWZAu65lOWIwfS7LEORs2zg1WRn8CWWtJAi_jmYHJT2LrudVHHRxRCiUz7Xsibq04DTxoiWN7rhNMwyOCfs1U4ulF17h0rbzGxiuZ6V2eUv8Z5xskK2m6kFPCljaVTwdxIiLlQSiH0uCbxN8KyNn7ohUO3zShfZFvNFFjH0BgKhEhpfLwYRutZhRf-Ka7IYM3UCmNdW7iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e82e87bc58.mp4?token=fDSTaCGrZEz24nlWXhe6rn_PP_qpXJ9t-FTApruy22mtkW6zYEEQvM9h66EOdMJxDzdg6AxdHnN2Z2zKHW9vS_BK_GeTHdW1OU2_tpk457uYUjH1A_8ClIViYBx9Bu5Hvr5kB6by3ZdBwWZAu65lOWIwfS7LEORs2zg1WRn8CWWtJAi_jmYHJT2LrudVHHRxRCiUz7Xsibq04DTxoiWN7rhNMwyOCfs1U4ulF17h0rbzGxiuZ6V2eUv8Z5xskK2m6kFPCljaVTwdxIiLlQSiH0uCbxN8KyNn7ohUO3zShfZFvNFFjH0BgKhEhpfLwYRutZhRf-Ka7IYM3UCmNdW7iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور رئیس‌جمهور در مراسم قهرمان ایران
@Sportfars</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/439068" target="_blank">📅 21:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439067">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">عراقچی: تبادل پیام‌ها در جریان است اما تا زمانی که به نتیجهٔ مشخصی نرسد نمی‌توان در مورد آن قضاوت کرد
🔹
به گمانه‌زنی‌هایی که صورت می‌گیرد تا زمانی که به قطعیت برسد نباید اهمیت داد.
@Farsna</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/439067" target="_blank">📅 20:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439065">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QjmA0WmNFlA4Wx5ivon7AO0bq_DgWJR0_UL058yI52meUOE95brEUIcO4QA2boRtgTlfC931MqguXwkAJrFMU1U7f1lgV1ms4meaqkVyHdQJPaVGEWdEsr1aODXh1IPs1jfy2Y4dCJM7fYhTc9AP6jbGf8_k41w9GpHemuvXnhzYW7eX2dpgp-TdJHW2rv_-VramFvOh631fP2pBreie-yJ0TkNZMZ68zJR9vPkRDaunWV77KItPctX7xRERKid_WL2hxHDWKGnNXSyrtqF5K_f_896cEBUkZBs7yFRh56tmPchnZ3xkSEKZWIO_ArGFdo6EruMRrhjbfwIy4hKYHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۶ فرودگاه کشور میزبان حاجیان می‌شوند
🔹
در عملیات بازگشت حجاج بیت‌الله‌الحرام به کشور، نزدیک به ۳۱ هزار زائر ایرانی طی ۱۱ روز و با بهره‌گیری از ۹ فروند هواپیما به کشور بازگردانده می‌شوند.
🔹
براساس برنامه‌ریزی‌های انجام‌شده، حجاج ایرانی از فرودگاه جده به شش…</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/439065" target="_blank">📅 20:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439064">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">آمریکا به زخمی شدن نظامیانش در پاسخ ایران به نقض آتش‌بس اعتراف کرد
🔹
سی‌بی‌اس به نقل از مقامات آمریکایی گزارش داد که در حملات موشکی ایران در واکنش به نقض آتش‌بس توسط آمریکا، چهار نظامی آمریکایی و سه پیمانکار زخمی‌ شده‌اند؛ درحالی‌که ارتش آمریکا مدعی شده بود که موشک بالستیک ایران را رهگیری کرده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/439064" target="_blank">📅 20:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439063">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/224f2690cc.mp4?token=gfT8TpfV6OZZSEbg5EgmUo0JUCTbS4DgNEgZspI4beUtzRTtFQBqlQQ4esjAjvQ1Ibtkm23N4CI5yfp-BqfdSLCSEMWE0bo0zmXrf4_sYqqH5_GaO6nZEb80W92JpV9pi-lMdbMjlf9RmNBrgG4FpFa8r7OBCu9HWQww9rfWlvCHUXcVUpvoPM7W6p8kxTfStCMri7GM3eUj8t77xdrQSeI1kknJ1bJKPgE-xDQgnLUG4GWWdy-a3jlyIzAjs2pzOLMbuQvLCmnLqAQAWSsYbJ5nBxC37WJtAnPs6v1RUUolQLQpM_r8wRNm5j9W0ZlmgTcdJ6Cnm2kAqZJT5KicIanwfDGg1inxDZePnv2cz-a0wLOX6OBYpj6aYVjgWGEykUI8YocE8v1ocXABp_rXumA8v0iUWjrQluHlnvM73kNzobwAWAmyG9GF7ZwNKzdTKPk0PR71XqKbbK_XxErHWePFIyE3AaDcZhhkFYisMtS5RqoSfzNZ7M5aBWUQuktfFA7tcwXJMy72ITnMV0CVbDhfOgqYZiReg30s2by-N4k4G-RfaIgO-8MI0JYLIrT2lRfyiRd_fsaZCagotsXG1j_cJlC8e2eVmXE1wZV9i5n3ZRcdCwSFZ3jAXZz61QVbwnmmLX5MrCgyIo8Q2XlVktklrqlNZuC9-QsBpXn7fms" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/224f2690cc.mp4?token=gfT8TpfV6OZZSEbg5EgmUo0JUCTbS4DgNEgZspI4beUtzRTtFQBqlQQ4esjAjvQ1Ibtkm23N4CI5yfp-BqfdSLCSEMWE0bo0zmXrf4_sYqqH5_GaO6nZEb80W92JpV9pi-lMdbMjlf9RmNBrgG4FpFa8r7OBCu9HWQww9rfWlvCHUXcVUpvoPM7W6p8kxTfStCMri7GM3eUj8t77xdrQSeI1kknJ1bJKPgE-xDQgnLUG4GWWdy-a3jlyIzAjs2pzOLMbuQvLCmnLqAQAWSsYbJ5nBxC37WJtAnPs6v1RUUolQLQpM_r8wRNm5j9W0ZlmgTcdJ6Cnm2kAqZJT5KicIanwfDGg1inxDZePnv2cz-a0wLOX6OBYpj6aYVjgWGEykUI8YocE8v1ocXABp_rXumA8v0iUWjrQluHlnvM73kNzobwAWAmyG9GF7ZwNKzdTKPk0PR71XqKbbK_XxErHWePFIyE3AaDcZhhkFYisMtS5RqoSfzNZ7M5aBWUQuktfFA7tcwXJMy72ITnMV0CVbDhfOgqYZiReg30s2by-N4k4G-RfaIgO-8MI0JYLIrT2lRfyiRd_fsaZCagotsXG1j_cJlC8e2eVmXE1wZV9i5n3ZRcdCwSFZ3jAXZz61QVbwnmmLX5MrCgyIo8Q2XlVktklrqlNZuC9-QsBpXn7fms" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم خطاب به دیپلمات‌ها: صدای رسای اقتدار ایران در جهان باشید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/439063" target="_blank">📅 20:44 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439062">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMyZ9xn4UyYFKMilIfvJwaMxBTkA-C0pkfiSzO-eRWHFx6Dm928nM51SM0K5hhuLuytpra8cVTkjvcQYOhh7hc-ngHRSCURUt3hhNkj-Bo21_NUf5bj-7oolXTC2Gj8bDycMSxSpZHOrP8jx2FQO8zEFWmZyCKsZC2YAdp_3Bvt09cMXDm6QhXLdtuk4_oh8SssIYyOB7yEXd6okS7SbLzcuq48Pwx2uYf-GHjFWG4OtrQooQXuHN1Q8eJF3DsM6gfSKKlcduaj_xTmmQguwNxTzg5jPG43Qc1ATlTl7fyd7Xd3rOtcfMgiOgAuu2pvLsmypUCtkDhHCVS2fbDRDWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سکوت دولت الجولانی در برابر پیشروی‌های اسرائیل در سوریه
🔹
شبکهٔ روسی آرتی: یک گشت نظامی متشکل از ۴ خودرو در میانه نگرانی و اضطراب شهروندان سوری و بدون هیچ گونه دستگیری به سمت حوض یرموک در حومه غربی درعا حرکت کرد.
🔹
روز گذشته هم گروهی از نظامیان صهیونیست متشکل از ۳ خودروی نظامی به عمق حومهٔ جنوبی استان قنیطره در نزدیکی نوار مرزی با جولان اشغالی سوریه پیشروی کردند
🔹
تجاوزات ارتش رژیم صهیونیستی در جنوب سوریه در حالی انجام می‌شود که دولت الجولانی در قبال این اقدامات سکوت کرده و در حال انجام مذاکرات مستقیم با صهیونیست‌ها است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/439062" target="_blank">📅 20:39 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439060">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WkfnZ7mk9lNF7IJxretAMo6t9fV7zhv_e6ojGM15F-yDOgcMgWdfjOEELZRpcRcxVmQ9JVATkYqGTjeWRW6DQ2ojwKEjpR95XFgj2OiRPPwRMfcH6fq66U1OsYyHMXYyFLLZ5uToC5ToJwiiVwtZ273GcXritWuECWaGUEgjHpzzggAjQ3O2KeXXA_Z_WcGw2l8HrdWmCb6NQ2qkZpcnr74AXP8kaBBJxdIkPN3s6GQa3Su6JPmz28NFQVTFWj46-ppVxobeW8GyvK8gkDE-q0XFpztlyHYRfjQNRx0z83xUFpeb8jSs6CIn67UnT-C-uTGKeIwn4dd5rMm5F7QDiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامۀ تلویزیونی «ثریا» فعلا پخش نمی‌شود
🔹
برنامۀ تلویزیونی «ثریا» که با اجرای محسن مقصودی تا امروز به صورت زنده پخش می‌شد،‌ در صفحه مجازی خود اعلام کرد که امشب روی آنتن نخواهد رفت. و تا اطلاع ثانوی پخش زنده نخواهد داشت.
🔹
صفحۀ مجازی این برنامه نوشت: «امیدواریم با تغییر شرایط و بهبود فضای رسانه‌ای، امکان پخش زنده این برنامه به‌ویژه در این روزها و شب‌های حساس و تاریخی ملت ایران فراهم گردد».
🔸
بنابر اطلاع خبرنگار فارس گرچه این برنامه فعلا روی آنتن نمی‌رود اما مستندهای تولیدی این تیم همچنان به پخش ادامه خواهد داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/farsna/439060" target="_blank">📅 20:32 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439058">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVb_eigUIy8Xtgj0VDDgSXVjBrKs-PQ5Z4mPsXV7RPEIpbJ_nuNIcrbkZITjD_zIjrauTXmMK1bENLSGkNGzIqz75HXJmOtIKJ8zTGrqmzDvaL9yXgQgTdESR4lz53KDbzLfqNgOH5wmeLS-EYZNWRsXWBC2SudcjkZbxG41SO7Th72Ts4P59IUK4NtmYl8ykbhyt5sINabfwclcU5xOdQa07NSX8R2ddPFo1ct0xk8mlH2Vf8JYqcmQobCxDgAyjR7emaL7rNUpgWgblPqoYOIHGwYDktGQ2iqzRimOPNDsAfGx1hgMbnrGS4gKvLgheId91wK2EEMnmllJfQhK_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سکوت سپاهان در قبال حذف از آسیا
🔹
مدیران باشگاه سپاهان در مورد انتشار خبری غیر رسمی مبنی بر حذف این تیم در آسیا فقط سکوت کرده‌اند.
🔹
این باشگاه به‌دلیل نقص مدرک از کمیتهٔ بدوی مجوز حرفه‌ای را نگرفته بود.
🔹
با حذف سپاهان، گل‌گهر، چادرملو و پرسپولیس در صف آسیایی‌شدن…</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/439058" target="_blank">📅 20:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439057">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sskH-2TVxmD-itMxamvPxHoeqBDVW-Vfg57r6gZ_iR5MUcW4YnRW3h8sKgiji2JtVDnhNWbUaTBTa1kW0lnzaw4w_q-Z7SqwyUqyO8bctStEkXSRXBQl-gJJFvV5yLp4MXx2Qed4P3daCjM-HlCaf8v9iaCtLncgP0GLYbBxq_WaTs-qO8QTUT3UvWqUYxFQ0JA37nJ3jiLGj3DR1Ed_aYyG_HLQcBLxaxFQo0okfpLnvXLTEl1_V9LoUsMC3AOAIlFR3qS3vOfM-jmIzigh5eN9R0qFCe9BLczVksR1oMBmi_kGZ8WiTEATCA3wwBgUtl3KkH2ENirezTpTR_E3bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تصاویری از حملهٔ هوایی اسرائیل به یک بیمارستان در جنوب لبنان  @Farsna</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/439057" target="_blank">📅 20:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439056">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7ae5815fc.mp4?token=K9gJWMvI4hJmqoJAgVzIJMOKxuzfpkn9Yb18G4O6iYxIl5y8xUPtSnqnF1TpnNnQd4YUwsUhKV1rR2Fr92LVATFQoksvZuusyZQSHyswYrJHKDD3MQTCBAkdkAptQpesrntmh7x1feqmW8lxJMSQpGwyITotmx2HlqhJF6to6VCYL01yoxN53jHa8rgMl-KUhr-PlGF7ulYdgFi9PAfQ9yt8HeIV91ZmRQCq89DqblfF2cyDqDEpftPU9Tplh38IpnwhXb9KKFFf89mezKiDsUWNcur331kN2RjME8gtRDOtdNb3mCRnP3MLNbJU2zEhPnrPZiIn3E4JSTjN-yB8Coi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7ae5815fc.mp4?token=K9gJWMvI4hJmqoJAgVzIJMOKxuzfpkn9Yb18G4O6iYxIl5y8xUPtSnqnF1TpnNnQd4YUwsUhKV1rR2Fr92LVATFQoksvZuusyZQSHyswYrJHKDD3MQTCBAkdkAptQpesrntmh7x1feqmW8lxJMSQpGwyITotmx2HlqhJF6to6VCYL01yoxN53jHa8rgMl-KUhr-PlGF7ulYdgFi9PAfQ9yt8HeIV91ZmRQCq89DqblfF2cyDqDEpftPU9Tplh38IpnwhXb9KKFFf89mezKiDsUWNcur331kN2RjME8gtRDOtdNb3mCRnP3MLNbJU2zEhPnrPZiIn3E4JSTjN-yB8Coi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: جنگ امروز اقتصادی، اجتماعی و فرهنگی است
🔹
اگر به داخل کشور برسیم، نقشهٔ دشمن نقش‌برآب می‌شود. نباید اجازه دهیم که جوان ایرانی بیکار و بی‌هدف بماند.
🔹
همان‌طور که می‌گوییم «بزن که خوب می‌زنی» باید بگوییم «بساز که خوب می‌سازی».
@Farsna</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/439056" target="_blank">📅 20:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439055">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
معاون نیروی دریایی سپاه: در برابر زیاده‌خواهی‌های دشمن خواهیم جنگید
🔹
ما تا آخرین لحظه در برابر هرگونه زیاده‌خواهی، پنجه‌درپنجهٔ دشمن خواهیم جنگید و خیال ملت شریف ایران راحت باشد که فرزندان شما در نیروهای مسلح، با سلاح‌های آماده و انگشتانی روی ماشه، حافظ امنیت و عزت این مرز و بوم هستند.
@Farsna</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farsna/439055" target="_blank">📅 19:59 · 10 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
