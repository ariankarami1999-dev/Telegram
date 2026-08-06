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
<img src="https://cdn4.telesco.pe/file/pJwSRWTig1jkD3fhs25AyJkqQT5NSo0X86LUe_avbTqs2YZGEV8g4PApj-8rIj06_G960G0iScRxRrCoGfcA9wZ2xKVnfRySzCXAPQ9gVwSxbtlpmnCJUoENM6BkNvGCTNl4QQpX7Cy1WWcK8Iwhbfo5pQyFpc56KQLaXDpDgkLX-8FX2Cv8y30OWyECl-3v5LjvlLCyIcL782aZGZQlOpYpF6UP4qfTrSLcy3KSYMbSCdWGsRAQLkJgJjIgEy6kc2CEc3k-S_eK0qPdktAoQlOKIACafo7T02AvSUANWaS9y5OYcq6BZWSNvfRgibQShgSS3nQeR9F19fVJFQCQ_g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.78M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-15 18:14:03</div>
<hr>

<div class="tg-post" id="msg-454751">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vf8jhW9CRJSweIbuFQOqwkUTBBxAjbDgdhv8Y7Aex5g4YQxVkvIqeABvPJMafvm5ELuctpsDVUsT5AbGXezsKHar2kaXmfQAC-oa6H5D-0dddXY50ouspaChDlu2NZHnwW53TvZqzF1NeW-H4vJtSR7KfYbm-mhvyGdPHhvmWtGNGqUSEfUPlKzw_phuYjf1oChBTFgzF8TLaz1A4dGSsECFbp6QoerDgds1Xe72N3fZsO0u4PnR2zRKor40k4bHLN5CKJ7gGw09JDe3urJOAF3F8Z7sIFuiCKuxFDFBM0geR0XqSweIndLqIJPNUikDXCywQvk-Xp1BjiRc_ge6eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CDcCQ1hgStlLAyKUwrdpiRAtgLaP2LGw5z-tKbF9qeSXdZCmxQU6NXPXXe0jyv8jhc0QL0IGg8lb-E1lKYWJbtvCM391QDn3ESz0KNu8tVzYaQzrfRP8ok0l0YldPPYsIepu22bg3anys2QkN-PPjD-4B9Rpge8QBVJT0-McFy9LjMSYTlH9fD_iEvcGPWWv_tn2s8hctIitpLGoxnnOtiJSSmLJE6s1R9cgs8ajd7gC9InOTtMeEeGx8Z1nY-kTP4f0P59DGdkU6jNQBPwInKmLvnkBuvjrZX4SJ5ZqjzlTcKcQwJVueEDqehc1-5uXcU6VAcTtyqEKHSzIvkglSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mrJKHbA4JcI0-XNvSAnd2zylda3uutEr0IeXWdH_pR_WxH-dN0XgHv4QQElkeypNEsm3MWk-xD9Mpo7F9pXJGDgZ5ackDDwhhHvHTbkaSzMwZXvQpzxKaZW41hEMIQr1Ic57QHdLB4iHAeu5Q8mrNqmFfyTEil7XJyMDXGHGsOD_NZ27RvrUwBuWNdM3CJegeu2xyy8IFhPndpBDpXNifjldszvE5NUwZ-HeIduUl8D5hKIgishqBaIVQC7XS8kd_gxFDYPnd8-fKVu_tUPtELf0v-qO-XXNY_134VtMMLhk0s_rNFf6sk3KoRvDxH-HVwUcvybekKAkOL7qZiEnCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیومانده گران‌ترین خرید تاریخ رئال‌مادرید
⚽️
رئال‌مادرید به‌صورت رسمی از جذب یان دیومانده خبر داد. این وینگر ساحل‌عاجی با انتقالی بزرگ از لایپزیش راهی سانتیاگو برنابئو شد.
⚽️
ارزش این انتقال ۱۲۵ میلیون یورو به‌همراه ۱۵ میلیون یورو بندهای پاداش اعلام شده تا دیومانده به یکی از گران‌ترین خریدهای تاریخ رئال تبدیل شود.
⚽️
انتقال دیومانده به رئال گران‌ترین انتقال تاریخ یک بازیکن آفریقایی است.
@Farsna</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farsna/454751" target="_blank">📅 18:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454750">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/807aa726f1.mp4?token=Zi_hNpNq0ADKmRYTOeiF0_cgXGraCpjKf-VZPIq-4XEU-Xt92r8c8gpSkfpIcyiBFEI1aOsEb9yZqeWgPGm368i3uVvRIfZkVeJ-_zgufKO4RXkdcGP4jxOlah5tNb0Yo7oWkFx0Nzgk3SCshHXsEp86mICQXbhJczY6-GF21LQp1Emj3gI3yk50ndLatjapAclLfhfVN6Kq0Jt_6FqNW8mXCoxYygSt97sxObwb9etnWYq_wwJrB_HcSyTblATwm5R9nZwjE2Lc4MRJ1TlzZEUJfiBY7PWO6Bdnj4Aw1R9RHzb45d8-vj6eZAMxijFajMUvE4LBdq3LlB8xiz9mqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/807aa726f1.mp4?token=Zi_hNpNq0ADKmRYTOeiF0_cgXGraCpjKf-VZPIq-4XEU-Xt92r8c8gpSkfpIcyiBFEI1aOsEb9yZqeWgPGm368i3uVvRIfZkVeJ-_zgufKO4RXkdcGP4jxOlah5tNb0Yo7oWkFx0Nzgk3SCshHXsEp86mICQXbhJczY6-GF21LQp1Emj3gI3yk50ndLatjapAclLfhfVN6Kq0Jt_6FqNW8mXCoxYygSt97sxObwb9etnWYq_wwJrB_HcSyTblATwm5R9nZwjE2Lc4MRJ1TlzZEUJfiBY7PWO6Bdnj4Aw1R9RHzb45d8-vj6eZAMxijFajMUvE4LBdq3LlB8xiz9mqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت یوتیوبر آمریکایی از ۲۲ میلیون زائر امسال اربعین و تعجب او از موج خون‌خواهی رهبر شهید تیران در بین زائران اربعین امسال
@Farsna</div>
<div class="tg-footer">👁️ 246 · <a href="https://t.me/farsna/454750" target="_blank">📅 18:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454749">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ضربۀ کوبنده انصارالله به مزدوران سعودی در یمن
🔹
منابع رسانه‌ای از حملات موشکی و پهپادی انصارالله به مواضع نیروهای وابسته به عربستان در چند استان یمن خبر دادند. براساس گزارش‌ها، دست‌کم ۴۵ نفر کشته شده‌اند. @Farsna - Link</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/farsna/454749" target="_blank">📅 18:03 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454748">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس من</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cfff69d92.mp4?token=McoAHKnJva4LoIoHzNmAwkJ3tUtn188sjDIbqcrM1j43Ol0EpADzLgoWm3KJnCUE-brDxekdWAkRxQyUtYKMtotSqgjlWh1KVk5HTyeXVJrgzd1bs-Qt8Oon1nP9tsOtAk86ccoCuWUJYWNXkS1OpCG85LT3_bHLWcHB75OzrPBivvTGUhcv8bdGUEr52J4fPVXXVUEdiKrXIpeSpbRdcmCFX76GlHQoQZ3KG153FN8ONyFl4h4KSlS-O5tPpTiCmpXomb4tykiBZwUwCo1ycLjP5B31RvSTgkF8Mv5cSY9MgV2lmu7fG1pKAACx1gLHGO53mFpqB063oO03LipFGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cfff69d92.mp4?token=McoAHKnJva4LoIoHzNmAwkJ3tUtn188sjDIbqcrM1j43Ol0EpADzLgoWm3KJnCUE-brDxekdWAkRxQyUtYKMtotSqgjlWh1KVk5HTyeXVJrgzd1bs-Qt8Oon1nP9tsOtAk86ccoCuWUJYWNXkS1OpCG85LT3_bHLWcHB75OzrPBivvTGUhcv8bdGUEr52J4fPVXXVUEdiKrXIpeSpbRdcmCFX76GlHQoQZ3KG153FN8ONyFl4h4KSlS-O5tPpTiCmpXomb4tykiBZwUwCo1ycLjP5B31RvSTgkF8Mv5cSY9MgV2lmu7fG1pKAACx1gLHGO53mFpqB063oO03LipFGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پایان انتظار کلزاکاران شهرستان صحنه کرمانشاه
🔹
در پی پیگیری پویش «
پرداخت مطالبات کلزاکاران صحنه را بیش از این به تأخیر نیندازید
»،
مدیر تعاون روستایی استان کرمانشاه
از تسویه کامل باقی‌مانده مطالبات کلزاکاران شهرستان صحنه تا ۲۵ مردادماه خبر داد.
@Farsnews_My</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/farsna/454748" target="_blank">📅 17:59 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454747">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a24b709c29.mp4?token=sBWBu6ttlYjcCM0w38U_rhypiLj7jpyUedRWXNkG0ZHbsGb_h62c_npIwZ5CC_TjpqiMgh-jqcR-i_tIba_zWkuNkuv6CAFEe0cLcriRB9c9BTAKSvIBJtPS7g93cbMjG4zYikcKJ_bNKR8BiDeNnkr7z9mYSwHi0NiuRm7PD81hsgcPh11QLzEtGbGOtwwRUdJIsJnYXxCSEbvEGQFhCpyId9a_h5lV206pBqJ39UvNuGc53A_yvtdAzCE29b1cVTGJCM3eoIDoYfQW309CbyfUnFWC93L4-jYqUG2_aVLqXyyFva2nL02llILYo3DLva5bsKyVynOoTKz4ohn8gDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a24b709c29.mp4?token=sBWBu6ttlYjcCM0w38U_rhypiLj7jpyUedRWXNkG0ZHbsGb_h62c_npIwZ5CC_TjpqiMgh-jqcR-i_tIba_zWkuNkuv6CAFEe0cLcriRB9c9BTAKSvIBJtPS7g93cbMjG4zYikcKJ_bNKR8BiDeNnkr7z9mYSwHi0NiuRm7PD81hsgcPh11QLzEtGbGOtwwRUdJIsJnYXxCSEbvEGQFhCpyId9a_h5lV206pBqJ39UvNuGc53A_yvtdAzCE29b1cVTGJCM3eoIDoYfQW309CbyfUnFWC93L4-jYqUG2_aVLqXyyFva2nL02llILYo3DLva5bsKyVynOoTKz4ohn8gDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاک‌ترین بانک جهان اینجاست
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/farsna/454747" target="_blank">📅 17:35 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454746">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9758b875b.mp4?token=nXStCVaPI49A3Cx9FgU4pRv6qHio9y5r8VKjwm4tr2ZjSg2_1hNyQ17vQG3Hxz9KIHE9CEBNlIx9WOS8vZJdgdOjv1dUqBV_-GJRXFIKZrTKsZoOE-0UuLq5_H-tPRBldNe2F6hbqq3gPyCl2UupjIS_Kecz4fKk4OUQGvYALvbLa--8K7JDtmB6vmdgO7H64XqBlradnmKHEg02_NT7zLyjaJBJIQLtWJm_jHTyYce0MgX-IUaKHW5LVow-ouf8y6lbrT5PcSk7eaQ4Gyu4M_Fwz56DSBqJfu1g23JVlK0SvD-kbkORjqL2Dq7zaRNiSwYJHUgOvAXvp9G-WEwR9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9758b875b.mp4?token=nXStCVaPI49A3Cx9FgU4pRv6qHio9y5r8VKjwm4tr2ZjSg2_1hNyQ17vQG3Hxz9KIHE9CEBNlIx9WOS8vZJdgdOjv1dUqBV_-GJRXFIKZrTKsZoOE-0UuLq5_H-tPRBldNe2F6hbqq3gPyCl2UupjIS_Kecz4fKk4OUQGvYALvbLa--8K7JDtmB6vmdgO7H64XqBlradnmKHEg02_NT7zLyjaJBJIQLtWJm_jHTyYce0MgX-IUaKHW5LVow-ouf8y6lbrT5PcSk7eaQ4Gyu4M_Fwz56DSBqJfu1g23JVlK0SvD-kbkORjqL2Dq7zaRNiSwYJHUgOvAXvp9G-WEwR9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترس کارشناس کویتی از تسلط ایران بر تنگۀ هرمز: شاه که رابطۀ خوبی با آمریکا داشت و ژاندارم منطقه نامیده می‌شد چنین اختیاراتی در هرمز نداشت اما ایران اکنون می‌تواند کلیددار امنیتی تنگه نام بگیرد.
@Farsna</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/farsna/454746" target="_blank">📅 17:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454745">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‌ وال‌استریت‌ژورنال: بحرین و کویت در حمله به ایران مشارکت مستقیم داشته‌اند
🔹
وال‌استریت‌ژورنال به‌نقل از منابع آگاه نوشت: کشورهای بحرین و کویت در اقدامی مخفیانه، جنگنده‌های خود را برای حمله به اهدافی در داخل خاک ایران اعزام کرده‌اند.
🔹
امارات نیز با ارائه…</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/farsna/454745" target="_blank">📅 17:20 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454744">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fg-LG8QW2Q3JSGBN2Hsw0HFTT-8L1QQT8M_TGFDyDz4AH6yxPPMe0CxkMqk71IrcfndIK-_9yueur00IxsJXaGFOQInJ1eZ1qTF-ceYksLM-heaDnHwwfo6t9-P9SlS9uO32lay-T0jCxtRsqhYIHzK7ZNAEDpSE0ju9kp9nPVcedR57RXtFE7lgT_nqpYzZaL_40HUTBR5IpCw_HpcryjyCvbvHpatl7uJNV5faZpSRtdXdSkLkx-QDwFj27fOmOVNEPLY9tOhO-h299Xv6QMy8LpF1AZmHm557dje45OTK9mOGTj-ZnioTztS5wFvNIiNoEP7KYI4xwicykHyjZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیرکل سازمان ملل در سالگرد جنایت اتمی هیروشیما از آمریکا نام نبرد
🔹
آنتونیو گوترش در پیام خود به مناسبت هشتادویکمین سالگرد بمباران اتمی هیروشیما، بار دیگر بدون اشاره به نام آمریکا، درباره خطر جنگ هسته‌ای، تشدید شکاف‌های ژئوپلیتیکی و لزوم درس‌گرفتن از فاجعه…</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/farsna/454744" target="_blank">📅 17:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454742">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kt_f9pBZiiZ2uQNrWqQnLn0UJktTM-Hr-VwhtaBCUHhJoq21XkOoq0aYA8phn3mtO6R_4KZ05KUIThXeKtExM7tm4BuUaq8m1wwXZE3Q-12FGfJgwOLd8HIRPDlWQY22uFkZ40ivZqYZQDWJsPROtz_8gAlhmFLvJKOjkqx9BSo68rnvZpoiluM-sODey8ZKOMDp_VCk4Dto30rw8lSOKGlRKHRP4p36HDby6aA1aBkI949r6kfLUDs3CBlmUZE2r54apdCUtmvMn2hXEZJTDYIahtiTttmNulLPdkKwwbarWdo8Y9EtOJiThcKfKtui8ZGM34vIeB0swWXVrFqHNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: مشروطه نقطه عطف بیداری و آزادی‌خواهی ملت ایران بود
🔹
یکصدوبیست سال از فرازِ تاریخیِ انقلاب مشروطه می‌گذرد؛ آرمانی ملی که با همبستگی و وفاق اجتماعی به ثمر نشست؛ رویدادی که نقطه‌عطفی شکوهمند در تاریخ معاصر و نشانه‌ای روشن از بیداری، هوشمندی و آزادی‌خواهی ملت بزرگ ایران است.
🔹
این جنبش پیشگام که نخستین تجربه نظام پارلمانی و قانون‌گرایی را در خاورمیانه رقم زد، نشان داد که مردم‌سالاری و شورا، ریشه در اندیشه و معارف دینی این مرزوبوم دارد؛ حقیقت والایی که با تمسک به تعبیر شریف قرآن که می‌فرماید «وَشَاوِرْهُمْ فِي الْأَمْرِ»، زینت‌بخش نهاد قانون‌گذاری در ایران شد و الگویی ماندگار از حکمرانی متکی بر خواست مردم را پیش ‌روی ملت‌های منطقه نهاد.
🔹
مشروطه نه یک حادثه محصور در گذشته، بلکه سرآغازِ فرایندی است که در طول یک قرن اخیر، با فرازونشيب‌های گوناگون تعمیق یافته و با پیروزی انقلاب اسلامی و استقرار نظام جمهوری اسلامی به مرحله‌ای نو و بومی از مردم‌سالاری دینی رسید.
🔹
امروز، ایران اسلامی با اتکا به نهادهای قانونی، حضور آگاهانه مردم در عرصه تصمیم‌گیری و ظرفیت‌های باشکوه علمی و ملی خود، راه دستیابی به پیشرفت و آبادانی را با صلابت ادامه می‌دهد.
@Farsna</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/farsna/454742" target="_blank">📅 16:59 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454741">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5rTwzeQzT7CNz8Q3AHokOBejtc8jzrTSxNKRgPbQPqOw15dFFiAlwYL7FyM_7ur93sUVOdwdYgO93TtcVoXCH5iRh8XZX80qbDW7rfPmoPOgeTutXbPXF_XOTvgBUTnGksoRBGo-W-GcLHhPZt9NIYxEZ_0_obaPhNLSDg9vIZlEDRu_1j0rKtctkOYgdJUvDmNvkjKP4GE1wgwHjJtdV2eswjGoaKVoOaF6_rolB3WlzgDu8EcutpbPmBaGjcLose0FClcg53To51XDH7F5ll5dGAokMmDkcuRZ4W1Pa-cwr7BL-LG1vR-fBT-3MxbgB88BmQL-w7GiBOxEfsTwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنگۀ هرمز را ببخشیم تا صلح شود؟
🔹
ناصر هادیان، استاد دانشگاه تهران، معتقد است ایران می‌تواند در ازای رفع تحریم‌ها از دریافت عوارض تنگۀ هرمز صرف‌نظر کند؛ زیرا به‌گفتۀ او درآمد این آبراه سالانه بیش از ۷ تا ۸ میلیارد دلار نیست و اصرار بر آن می‌تواند به تداوم درگیری‌ها منجر شود. او حتی رقم درآمد ادعایی‌اش را با تخفیف نفتی ایران به چین برابر دانسته است.
این دیدگاه با انتقاد کارشناسان اقتصادی و راهبردی مواجه شده است. منتقدان ۴ ایراد اصلی را مطرح می‌کنند:
🔸
۱. وعدۀ رفع تحریم‌ها تضمین‌شده نیست و تجربه برجام خلاف آن را نشان داده است.
🔸
۲. برآورد تخفیف نفتی ایران به چین بیش از واقعیت اعلام شده و طبق برخی گزارش‌ها حدود ۱.۲ میلیارد دلار در سال است.
🔸
۳. درآمد بالقوۀ تنگه هرمز با دریافت عوارض می‌تواند تا حدود ۴۰ میلیارد دلار در سال برسد.
🔸
۴. کنار گذاشتن اهرم اقتصادی تنگه، به‌جای کاهش تنش، ممکن است هزینه اقدامات نظامی علیه ایران را کاهش و احتمال تکرار آن را افزایش دهد.
🔹
به‌باور منتقدان، در معادلۀ تنگه هرمز، بازدارندگی و منافع ژئوپلیتیکی در کنار منافع اقتصادی باید در محاسبات لحاظ شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/farsna/454741" target="_blank">📅 16:54 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454739">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/370904d528.mp4?token=gAxAJupXdZPlXYvfgR_PBhx_2nfMHX5aecmF9eM8aX5NqXQmvMf0X88SqR6WtdAQGd6aw_yASEOKqqTtlqIkoxjoqahDZa5O9zbfaQPW6iWV_4sVZQIz7XplwceYAYWE_ygdWE190PZHca0mvmEd3QgnT2VoDPD89j13zdWRmQAsg7fhbtZgAzKoZxrzWqi6PLk3npleOP1T4jUpk124FrDd-szRguueZEJX0o8yMg_XkwCWEGTm4OlkvN-sjmaqgNKQkSiryFWTuZf4lvPBtIKlzjhXW1lpOQECcJ8l5nBimz2HVXKSDkHxjqainyaLSKAHa0StZQRUdw9D-x-Zrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/370904d528.mp4?token=gAxAJupXdZPlXYvfgR_PBhx_2nfMHX5aecmF9eM8aX5NqXQmvMf0X88SqR6WtdAQGd6aw_yASEOKqqTtlqIkoxjoqahDZa5O9zbfaQPW6iWV_4sVZQIz7XplwceYAYWE_ygdWE190PZHca0mvmEd3QgnT2VoDPD89j13zdWRmQAsg7fhbtZgAzKoZxrzWqi6PLk3npleOP1T4jUpk124FrDd-szRguueZEJX0o8yMg_XkwCWEGTm4OlkvN-sjmaqgNKQkSiryFWTuZf4lvPBtIKlzjhXW1lpOQECcJ8l5nBimz2HVXKSDkHxjqainyaLSKAHa0StZQRUdw9D-x-Zrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع یمنی اعلام کردند تا دقایقی دیگر، نیروهای مسلح یمن با انتشار بیانیه‌ای از یک عملیات نظامی گسترده و ویژه خبر خواهند داد.  @Farsna</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/farsna/454739" target="_blank">📅 16:52 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454738">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eed2183872.mp4?token=rVJSewuXMB_JMLPX5ttWDMSNMJVAqi7VfvSRE_0OabPlwsrGM49c9mcx6dkD3YpkqqmxjePHUf-yL-fhEtYlo9pOfoLOjiPI8_YGWU9kJ0fqv0OwZWvJQGHOWiCnb1iJQ-BOwGTev8yRh3qYB86QQLwcbAY0Ohtm3gx3pZvNbrhFGaKvICrIicYTsb6la4-74lcZ4acfMDu_n5OUev1fu0wLmEJFRIzXMQ-qJbJSNmvO6WgVpwaZI1XhTD0pjINFjEIKRLOV8dEnAJadjF4Qblbfco0RIodgOqlu11FXGewmMDPnvxm4S1ECLsLMygh8Bw7GY448m1dvD46gXtrRzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eed2183872.mp4?token=rVJSewuXMB_JMLPX5ttWDMSNMJVAqi7VfvSRE_0OabPlwsrGM49c9mcx6dkD3YpkqqmxjePHUf-yL-fhEtYlo9pOfoLOjiPI8_YGWU9kJ0fqv0OwZWvJQGHOWiCnb1iJQ-BOwGTev8yRh3qYB86QQLwcbAY0Ohtm3gx3pZvNbrhFGaKvICrIicYTsb6la4-74lcZ4acfMDu_n5OUev1fu0wLmEJFRIzXMQ-qJbJSNmvO6WgVpwaZI1XhTD0pjINFjEIKRLOV8dEnAJadjF4Qblbfco0RIodgOqlu11FXGewmMDPnvxm4S1ECLsLMygh8Bw7GY448m1dvD46gXtrRzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشکر موشکیِ رزمندگان پای لانچر از مردم عراق
🔹
رزمندگان هوافضای سپاه برای تشکر از مردم عراق، جملات درخواستی‌شان را روی موشک نوشتند.
@Farsna</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/farsna/454738" target="_blank">📅 16:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454737">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-text">افسار غول‌های فناوری در دست ژنرال‌های نظامی
🔹
حضور مدیران ارشد امنیتی و ژنرال‌های سابق پنتاگون در شرکت‌های پیشرو هوش مصنوعی، نشان می‌دهد این فناوری از یک محصول تجاری به ابزاری در حوزه زیرساخت‌های حیاتی و نظامی تغییر ماهیت داده است.
🔹
اما این تغییر ساختاری تنها به یک شرکت محدود نماند؛ انتصاب دریاسالار پاول ناکاسونی، فرمانده سابق سازمان امنیت ملی آمریکا در اوپن‌ای‌آی و پیوستن قائم‌مقام سابق سی‌آی‌ای به آنتروپیک، نشان داد غول‌های فناوری رسماً لباس رزم به تن کرده‌اند.
🔹
ورود این چهره‌های امنیتی به اتاق تصمیم‌گیری سیلیکون‌ولی، ابعاد جدیدی از تسلط نظامی بر آینده الگوریتم‌ها را فاش کرده است.
اینجا
بخوانید
@FarsnaTech</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/farsna/454737" target="_blank">📅 16:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454736">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سرنوشت تلخ تولیدکننده خراسانی؛ ۱۷ ماه انتظار برای ارز استحقاقی
🔹
امین ویسی، بنیان‌گذار و مدیرعامل شرکت سپهر ترخیص راه سبز ضمن انتقاد از بروکراسی‌های اداری و عدم حمایت‌های لازم از صنعت تولید برنج در خراسان رضوی، از بلاتکلیفی ۱۷ ماهه ارزی و تبعات آن برای اشتغال‌زایی در استان خبر داد.
این گفت‌وگو را
اینجا
مطالعه کنید</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/farsna/454736" target="_blank">📅 16:38 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454735">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVRytxxEvMsGyx-fozrpghx4mq79svJwTLr-7Y4ot5zg-kXdYxj3MXNHLEVHmzrB82MqaNFbFGMbkpcRRFg3NKVh3Q5YFVcOPl4bgjM3me8DdpEy0-cUfPCqxzoQRSdfTPTfwXRCKwiIFpsaVgYnhFlcLj-6O_mh1KaSSoOZboc3w78LX0FEBPkOyKlMVC_FiYeUsvSjknPHpxJVUEeKTwkRNSCT88E5PMPADifd3OLsguLjqEtYL1AKsDp479QaKRWzkJH0frigWxdkl6e562afSzPTyivKVNDjeLHng9tf8JyrMamQgEhi0RDZ4ZemMLUn-t2rvxtCbmiydUeBfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرپرست مدیریت عامل بانک سرمایه در نشست منطقه هفت تأکید کرد؛
✅
اجرای برنامه تحول بانک با تمرکز بر منابع پایدار، درآمدهای کارمزدی و بازسازی اعتماد مشتریان
🔹
به گزارش روابط عمومی بانک سرمایه، نشست بررسی و ارزیابی عملکرد شعب منطقه هفت و تبیین برنامه‌های عملیاتی بانک سرمایه با هدف بررسی وضعیت عملکردی شعب، پایش منابع و مصارف، مرور برنامه‌های اجرایی بانک در سال جاری و تبیین اولویت‌های منطقه هفت با مرکزیت ساری برگزار شد.
🔸
دکتر موسی اسلامیان در این نشست، ضمن تسلیت فرارسیدن ایام اربعین حسینی، مباحث خود را در چهار محور وضعیت گذشته بانک، مقایسه آن با شرایط فعلی، اقدامات انجام‌شده و تبیین اهداف کوتاه‌مدت و بلندمدت بانک در سال جاری تشریح کرد و گفت: بانک سرمایه با تدوین برنامه‌های عملیاتی چهارماهه از آذر تا اسفند ۱۴۰۴، پیگیری افزایش سرمایه، برگزاری مزایده املاک و اموال مازاد و تدوین استراتژی بلندمدت پنج‌ساله طرح تحول، احیا و بازآفرینی، مسیر تازه‌ای را برای تقویت ساختار مالی و عملیاتی خود دنبال کرده است.
🔗
[
متن کامل خبر
]</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/farsna/454735" target="_blank">📅 16:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454734">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/farsna/454734" target="_blank">📅 16:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454733">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
منابع یمنی اعلام کردند تا دقایقی دیگر، نیروهای مسلح یمن با انتشار بیانیه‌ای از یک عملیات نظامی گسترده و ویژه خبر خواهند داد.
@Farsna</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/farsna/454733" target="_blank">📅 16:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454732">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7a4bf4c40.mp4?token=fgOY0Ore5INUPoe6Y0LHMJPVtkYeUVAIkrsl2wxSe-zVcrMhkJk3b8R_TPhsHZk2BRHLt7ZfwQNKnEhawbarC91rRgimfsUEG9tRxOZnfZoNPllMJ-ElJNstDbtN3wtu5Zq_7nkz4FYiJUFfaBktnsM2mQv3IXGyLTAr2hrSvHGXrPWroxvQvXzeIxWA5g6BOjuyHOK_cVH_s9mT1-W7TPz0V3rryNhd16jyX_FqQrxJFx5xQXBbpVhLDxu24s25T5EAQPCvGo-vUe8WuPaglAjsqJRqbVXnylhZhGiTJXskvWcFqyFlbZp8eFDdDfSR4lasolnMWUn7h2kdE8vLyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7a4bf4c40.mp4?token=fgOY0Ore5INUPoe6Y0LHMJPVtkYeUVAIkrsl2wxSe-zVcrMhkJk3b8R_TPhsHZk2BRHLt7ZfwQNKnEhawbarC91rRgimfsUEG9tRxOZnfZoNPllMJ-ElJNstDbtN3wtu5Zq_7nkz4FYiJUFfaBktnsM2mQv3IXGyLTAr2hrSvHGXrPWroxvQvXzeIxWA5g6BOjuyHOK_cVH_s9mT1-W7TPz0V3rryNhd16jyX_FqQrxJFx5xQXBbpVhLDxu24s25T5EAQPCvGo-vUe8WuPaglAjsqJRqbVXnylhZhGiTJXskvWcFqyFlbZp8eFDdDfSR4lasolnMWUn7h2kdE8vLyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میدان‌داری یک دهه نودی در بین‌الحرمین
@Farsna</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/farsna/454732" target="_blank">📅 16:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454730">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lh173LhYUUQFZ0GP0hPHRSfa37Cgxxl-IW4NnAMxXzHZwqC3BughU6ttDNK0xWSiUiBdXY-PpMh5GvLgwg1fJoT5uoZxH4D1WkJgNSX0_AR7m2KA4ov1MR-iv6djBml58MeTHMd_UhA_qExIBZzS_n1ceZUaq7TcRenVX5UA5g3Rer_cwQDDUtv8vao2-lsyfdAa_zSVmZwr7oL2Ak6Q6CwfnVAX3Jz0Smxs78E8mU4sy0Gd8m_StjKRPTubd-T_oDicWq33KFxCUZr_bM5iCfyR0fdu-fIjwMXHa_3fomEG1ieXZIBx_2TLmA5FJV9qkbvSVpR9PewQ7a1_5eMsFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعداد حساب‌های بانکی‌تان را اینجا ببینید
🔹
تارنمای بانک‌مرکزی برای نمایش حساب‌های بانکی هر شخص حقیقی فعال شد. افراد می‌توانند با مراجعه به
my.cbi.ir
تعداد حساب‌های بانکی فعالشان را چک کنند.
🔹
طبق اعلام بانک‌مرکزی در آینده امکان غیرفعال‌کردن حساب‌های بانکی از این سامانه مهیا خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/454730" target="_blank">📅 16:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454729">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f383cf50aa.mp4?token=Lrgyk6bt2yNZtSK3PQsCdj1T0HqwB9jQoyzJ4TOosdXZhuQGxxacwp3qt7M9N2K80MJiGasBKkBHeNjdbuxtCY3ikGl8dZ50MJwrjN2Y4CpgDPL_X_dvgjQw0jBma7Siy3lwuLP9I7HMdl0T0Bc5Os_LC9H_JMrBDgs0EnQna2hhe8cCg_YfYUPQ-PJ9d81hnGC6ZWfYjZHw6Vohi2FQx_1gEhIoZrajHDgyT3TmQYHObc3tmmwmjqE_bKBhr5iHeYcTDn_0MRPfuJf-_KGxoqVgC5SXxr6KxBOWkgWGCkHiwHxuLB7K8cnG24C0hMClCyQmSw8TCeSnviinS7NPdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f383cf50aa.mp4?token=Lrgyk6bt2yNZtSK3PQsCdj1T0HqwB9jQoyzJ4TOosdXZhuQGxxacwp3qt7M9N2K80MJiGasBKkBHeNjdbuxtCY3ikGl8dZ50MJwrjN2Y4CpgDPL_X_dvgjQw0jBma7Siy3lwuLP9I7HMdl0T0Bc5Os_LC9H_JMrBDgs0EnQna2hhe8cCg_YfYUPQ-PJ9d81hnGC6ZWfYjZHw6Vohi2FQx_1gEhIoZrajHDgyT3TmQYHObc3tmmwmjqE_bKBhr5iHeYcTDn_0MRPfuJf-_KGxoqVgC5SXxr6KxBOWkgWGCkHiwHxuLB7K8cnG24C0hMClCyQmSw8TCeSnviinS7NPdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هیچ‌کسی در دنیا نمی‌تواند این میهمانی را مدیریت کند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/454729" target="_blank">📅 15:43 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454728">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">هلاکت اعضای تیم تروریستی در سیستان‌وبلوچستان
🔹
روابط‌عمومی قرارگاه قدس نیروی زمینی سپاه: یک تیم تروریستی که قصد داشت در جنوب سیستان‌وبلوچستان اقدام به عملیات تروریستی کند پیش از اجرای عملیات تروریستی متلاشی شد.
🔹
این تیم با داشتن سلاح و مهمات به قصد انجام…</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/454728" target="_blank">📅 15:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454727">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72cdbc7cdf.mp4?token=PdqrOc6N47NR6UUU2mzMBwFS3RW32pAzdsHiuY-5P7FxAmUHoercKbIOl_F-RHmu7KqXc4G1RMhGfIJHUEbUVG3Gto1k9zf9qrObaBaDKaePLqLJGHd6pGPxI9mH7sScxtwBGkILyodf0neaJ7IqW9FWQEXjuRs73XQI_2ppjJgjZed4Fq-WTRUcBxoNOFqR-nlceuv61uT8_xBA27zJgST-O-XXBmQyGRFQDQMtNMx4Wz0C-kER14XE1Rja9lXuFep3Nu0NWLxluhAER7Gqb3U3sYoKDTEFDJ_sOE-Z-_n45ihl7tdKpT7yni6MkMLF-zpnLPdP4MdbcKPoR5EbXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72cdbc7cdf.mp4?token=PdqrOc6N47NR6UUU2mzMBwFS3RW32pAzdsHiuY-5P7FxAmUHoercKbIOl_F-RHmu7KqXc4G1RMhGfIJHUEbUVG3Gto1k9zf9qrObaBaDKaePLqLJGHd6pGPxI9mH7sScxtwBGkILyodf0neaJ7IqW9FWQEXjuRs73XQI_2ppjJgjZed4Fq-WTRUcBxoNOFqR-nlceuv61uT8_xBA27zJgST-O-XXBmQyGRFQDQMtNMx4Wz0C-kER14XE1Rja9lXuFep3Nu0NWLxluhAER7Gqb3U3sYoKDTEFDJ_sOE-Z-_n45ihl7tdKpT7yni6MkMLF-zpnLPdP4MdbcKPoR5EbXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دستگاه الکل‌سنج تنفسی بومی‌سازی شد
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/454727" target="_blank">📅 14:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454726">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">هلاکت اعضای تیم تروریستی در سیستان‌وبلوچستان
🔹
روابط‌عمومی قرارگاه قدس نیروی زمینی سپاه: یک تیم تروریستی که قصد داشت در جنوب سیستان‌وبلوچستان اقدام به عملیات تروریستی کند پیش از اجرای عملیات تروریستی متلاشی شد.
🔹
این تیم با داشتن سلاح و مهمات به قصد انجام عملیات تروریستی از کشورهای همسایه وارد کشور شده که در کمین رزمندگان سپاه قرار گرفته و در درگیری مسلحانه  اعضای این تیم تروریستی به هلاکت رسیدند.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/454726" target="_blank">📅 14:44 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454725">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXiG07veC7KsaVIyMTkC-oJj503BX2u_Jlx_bCLnq4YDouzEs2t8oGtQB4G4e0uJVZ9q4axjqToRMSnXyMA8AKpMWW9cbR9_Pnopf1Um8gmEEYVma_nT_Hoo-w2SGKnH9iGT6zIQYWwyH8LyEkucdvW9EM6DyxBmC_hKN2qv7rlbB8d5kX_s_U6dga1fkDKA-3R_JDHAPbVINor2XAQobPDPew_z79Nhv4F_ZDGAklN2UrREcskT2B5IezepoQZKRDCg6BWMgNCTMZW3WiELDREI0SzsR07cvyUPsN1gboeJU6rcSkLF-7fY_6IuzbouYboK0EAJqCWiqZ76SeRUDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه‌قضائیه: ادعای ردزنی محل استقرار شهید لاریجانی از طریق تماس تلفنی صحت ندارد
🔹
خبرگزاری قوه‌قضائیه: پیگیری‌ها از پروندۀ قضایی مربوط به شهادت علی لاریجانی نشان می‌دهد ادعای یکی از نمایندگان مجلس مبنی بر شناسایی محل استقرار شهید لاریجانی از طریق تماس تلفنی…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/454725" target="_blank">📅 14:38 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454723">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cb4bb875c.mp4?token=KQTNOsIhOBSaddhqjdNqtQThXKAMQby70z2G89GoYaNrP8bUVoR4sJAF-PAyxozKZqESddLDnlqPWcgM8xJDmAMprAD_NEIvwaNsf90K_6Q_QpVVlKvgQLOtAtG-gpI8DtXsITB0Avsqt6hVtct3toO4EbOfmpCoK3V14055aqh8ksaiQHZMvUVf0F-NZBVVeRL3legYEogmE9IzD2j7JwNWtEuXTJB-bw9feLFrUnibAH2y5-x5VstKRV3BxftT5aD2CksJ-L7PrsunsNVziGWvA59keEv-oq-4NbuCWpWMFR9NL1NXgjINf8gt1dRJQHipPEGr8be_4QbY3Vecyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cb4bb875c.mp4?token=KQTNOsIhOBSaddhqjdNqtQThXKAMQby70z2G89GoYaNrP8bUVoR4sJAF-PAyxozKZqESddLDnlqPWcgM8xJDmAMprAD_NEIvwaNsf90K_6Q_QpVVlKvgQLOtAtG-gpI8DtXsITB0Avsqt6hVtct3toO4EbOfmpCoK3V14055aqh8ksaiQHZMvUVf0F-NZBVVeRL3legYEogmE9IzD2j7JwNWtEuXTJB-bw9feLFrUnibAH2y5-x5VstKRV3BxftT5aD2CksJ-L7PrsunsNVziGWvA59keEv-oq-4NbuCWpWMFR9NL1NXgjINf8gt1dRJQHipPEGr8be_4QbY3Vecyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پالایشگاه بزرگ نفت روسیه هدف حمله قرار گرفت
🔹
درپی حملهٔ چندین پهپاد اوکراینی، پالایشگاه نفت یاروسلاول روسیه دچار انفجار و آتش‌سوزی شد.
🔹
این پالایشگاه، یکی از ۵ پالایشگاه بزرگ روسیه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/454723" target="_blank">📅 14:26 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454722">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">شرط جدید برای بازنشستگی اعلام شد
🔹
مدیرکل امور فنی صندوق بازنشستگی کشوری: میزان سابقۀ خدمت الزامی برای بازنشستگی برخی گروه‌ها با توجه به سابقۀ خدمت قابل‌قبول آنان در تاریخ لازم‌الاجرا شدن قانون، سوم مرداد ۱۴۰۳ افزایش یافته؛ با این حال افرادی که در این تاریخ بیش از ۲۸ سال سابقۀ خدمت برای بازنشستگی داشته‌اند، مشمول نخواهند بود.
🔹
میزان افزایش سابقۀ خدمت برای سایر کارکنان نیز متناسب با سابقۀ خدمت آنان تعیین شده:
🔹
۲۵ تا ۲۸ سال سابقه، به ازای هر سال تا بازنشستگی ۲ ماه
🔹
۲۰ تا ۲۵ سال سابقه ۳ ماه
🔹
۱۵ تا ۲۰ سال سابقه ۴ ماه به سنوات الزامی بازنشستگی اضافه می‌شود.
🔹
افزایش سابقۀ خدمت با رسیدن آقایان به ۶۲ سالگی و خانم‌ها به ۵۵ سالگی متوقف می‌شود.
🔹
همچنین ایثارگران، معلولان، شاغلان مشاغل سخت و زیان‌آور و برخی از بانوانی که پیش از لازم‌الاجرا شدن قانون شرایط قانونی بازنشستگی را احراز کرده‌اند، مشمول نخواهند بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/454722" target="_blank">📅 14:12 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454721">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">قوه‌قضائیه: ادعای ردزنی محل استقرار شهید لاریجانی از طریق تماس تلفنی صحت ندارد
🔹
خبرگزاری قوه‌قضائیه: پیگیری‌ها از پروندۀ قضایی مربوط به شهادت علی لاریجانی نشان می‌دهد ادعای یکی از نمایندگان مجلس مبنی بر شناسایی محل استقرار شهید لاریجانی از طریق تماس تلفنی فرزندش با خانواده، صحت ندارد.
🔹
بررسی‌های انجام‌شده و پروندۀ تشکیل‌شده در این باره، این ادعا را تأیید نمی‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/454721" target="_blank">📅 14:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454720">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBEQs0cvhki4Qzx7HjgVntjxHg8j5qQMJpqQUSmAD-JxE1E3kC1FL1qYTYGSu_2SoJ6G925MR6BOII7V2hTZV6HLb9AsxFfp_-XzTriOmTH5PP08GdJx2QeTHR_PHRojfNh2eX7BjhlBBOYOraWwvHfgPR8D5kIb4zFpyJIRWg-9UE8iVtCekfET8MAj0NnbcF3vj2Fd4wodFJQdDqidmjP0JEyvzGsBFv2TF_YMisajuSft8PtOtkIKImZLMpETtPuw5ums_KhqM1GWGYhsdBxp53-qAUXuHGmHay1yZlYlJlcA8mBE3VdruciykuGwlkxomtqNmReDZJY8IEMZ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
تقدیر فرمانده هوا فضای سپاه از بسیجیان دریا دل کاشان
بسیجیان دریا دل کاشان سلام‌علیکم
🔹
افتخار خدمت‌گذاری خالصانه و صادقانه به‌طور قطع و یقین زیبندۀ شما و مصداق تلاش جهادگرانه شما عزیزان است .
🔹
از اینکه در سخت‌ترین شرایط همگامی و همراهی شما را در کنار رزمندگان هوافضا داریم برخود می‌بالیم و به‌وجود شما مباهات می‌کنیم. انشاالله سربلند و پیروز باشید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/454720" target="_blank">📅 13:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454719">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">وزارت اطلاعات: ۲۱ مزدور موساد و ۴ شرور مسلح در کرمان بازداشت شدند
🔹
وزارت اطلاعات اعلام کرد ۲۱ نفر از عوامل مرتبط با سرویس جاسوسی و تروریستی رژیم صهیونیستی (موساد) در عملیات‌های اطلاعاتی در استان کرمان شناسایی و بازداشت شدند.
🔹
این افراد اطلاعات مراکز حساس و طبقه‌بندی‌شدۀ نظامی و پدافندی را جمع‌آوری و برای موساد ارسال می‌کردند.
🔹
همچنین ۴ نفر از اعضای باندهای مسلح شرارت در استان کرمان بازداشت شدند که از آن‌ها سلاح و مهمات جنگی و شکاری کشف و ضبط شده است.
🔹
وزارت اطلاعات همچنین از کشف و ضبط ۴ سلاح جنگی از ۵ نفر از عناصر مسلح بازداشت‌شدۀ مرتبط با کودتای دی‌ماه ۱۴۰۴ و تحویل آن‌ها به دستگاه قضایی خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/454719" target="_blank">📅 13:29 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454718">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">۲۲ متهم پرونده‌های ارزی بازداشت شدند
🔹
دادستان تهران: تاکنون برای مدیران شرکت‌های تراستی ۵۹ پرونده تشکیل شده که در ۴۳ پرونده، قرار جلب دادرسی صادر شده است.
🔹
۲۲ نفر از متهمان این پرونده‌ها به زندان معرفی شده‌اند و برای ۱۵ نفر از آنان اعلان قرمز (اخطار بین‌المللی…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/454718" target="_blank">📅 13:27 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454717">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVh_ABKvP3VWK_rRJzMSuIqSDgsWSGUNedZ0KhY8NUboZ_vvHozeLVmcjOdpXkMJnrInsBavvTaWiLnt1FS8r5fIXGRiZ8nY13u0kYWUrO5CtV8USM5R98_wGfJyxDgrEEAgOat1qyDZCv1o1amTJpW9azMcXeqADPnw9YBsdGie_8MJWJLurPSY2_dsLhH7bcqKcDQx-JQeKrAJ0Xg9PVSBAcvROTzy6yZS3AZe9Oh2IsGOYKCGndRtuvXwrmTRPEqncuLhN0WMsBcuZQmhyMW_aV16sf0r7cR8HHueq_VgjDAkf2-HLM8KQ_2OHFpCXjpbV_QEHmDQAXiozXEILA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان تنظیم مقررات: اعمال ضریب ۲.۷ برای اینترنت بین‌الملل صحت ندارد
🔹
در روزهای اخیر برخی کاربران در فضای مجازی مدعی شده‌اند که مصرف هر یک گیگابایت اینترنت بین‌الملل، معادل ۲.۷ گیگابایت از حجم بسته محاسبه می‌شود و همین موضوع را عامل زودتر تمام‌شدن بسته‌های اینترنتی نامیده‌اند.
🔸
سازمان تنظیم مقررات و ارتباطات رادیویی این ادعا را تکذیب و اعلام کرد هیچ ضریب افزایشی برای اینترنت بین‌الملل اعمال نمی‌شود و حجم بسته‌های اینترنتی نیز تغییری نکرده و یک بسته ۱۰ گیگابایتی همچنان معادل ۱۰ گیگابایت اینترنت بین‌الملل است.
🔸
به‌گفتۀ سازمان تنظیم مقررات، منشأ این برداشت، تعرفه ترجیحی ترافیک داخلی است؛ به این معنا که با همان اعتبار بسته، هنگام استفاده از برخی خدمات داخلی، به‌دلیل تعرفه ارزان‌تر، امکان مصرف حجم بیشتری از اینترنت داخلی وجود دارد و این موضوع ارتباطی با کاهش حجم اینترنت بین‌الملل ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/454717" target="_blank">📅 13:27 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454716">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sccH9AqPxjtnwKzQ6NKE0nrm5Ccspv-F3fj3f6V7_kIJdE_nFzEJuCSAbwBPRd50kyDr05kPLRnQ5RUWqv3wytXnDlS8M2eg_nOJ7fwykqHFjzeQ7c043kUqqrnxKX26fGVwfdke6ofS0Lcm2mHnuJ44s3cQCYQJCBnQoyXf-PjERsD0eRVmmrf8WqtK28lQB0D7RhDITU6h6Cod18ri6siRgCfiS3qed8GRjIkZzad4WTKbrotT8ktawOjetr3-Dv8u2593_FPfAUHIyz7xerO5yGVsGHCb6C4T_zqvxC9nYY8R2Ki4xUDi5Ubo3-rvsOlWL0i-OOnPJUGWZN5iSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیرکل سازمان ملل در سالگرد جنایت اتمی هیروشیما از آمریکا نام نبرد
🔹
آنتونیو گوترش در پیام خود به مناسبت هشتادویکمین سالگرد بمباران اتمی هیروشیما، بار دیگر بدون اشاره به نام آمریکا، درباره خطر جنگ هسته‌ای، تشدید شکاف‌های ژئوپلیتیکی و لزوم درس‌گرفتن از فاجعه هیروشیما سخن گفت.
🔹
گوترش در حالی از نام بردن از عامل این حمله خودداری کرد که در سال‌های گذشته نیز رویکرد مشابهی داشته است. همزمان، نخست‌وزیر ژاپن و شهردار هیروشیما نیز در مراسم یادبود، نامی از آمریکا نبردند.
🔹
آمریکا در سال ۱۹۴۵ با بمباران اتمی هیروشیما و ناگازاکی، تنها حملات هسته‌ای تاریخ جنگ را رقم زد. این حملات صدها هزار قربانی برجای گذاشت. با این حال، واشنگتن تاکنون مسئولیت اخلاقی این جنایت را نپذیرفته و هیچ‌یک از رؤسای‌جمهور آمریکا نیز بابت آن عذرخواهی نکرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/454716" target="_blank">📅 12:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454715">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3229ff6f33.mp4?token=pLGnNmv2PTISnFqimO9G6g2JMY4LNfHNCxUrpi9bGo6BHyWYBgDEQMnBpLddzTAymykb_bSroKJtDIBcXzH0DoGhV30gXQlgAT7FFJVV6UnonL8_B8V180-ubzCZjKQwggqDMIQEuGorR52ZXtf0dAj4HCH7NNRjKlXJ3Z3_aHC7sneXh8mEdcZm0OJa-mTdxvRKd-yRktR2REdDLcGz5htUBjfgPK0Om2lJQ90mW0V0pHeOe8DmXWW9WQEc6twtD-3HzHdad8-1-DeDCyy_1uA4JsvUElNo3OQrXohtTpeDfJRUfbQ-G0U7FH5Ibui-e2FPyT5Fi2Aqr6MEI5tuGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3229ff6f33.mp4?token=pLGnNmv2PTISnFqimO9G6g2JMY4LNfHNCxUrpi9bGo6BHyWYBgDEQMnBpLddzTAymykb_bSroKJtDIBcXzH0DoGhV30gXQlgAT7FFJVV6UnonL8_B8V180-ubzCZjKQwggqDMIQEuGorR52ZXtf0dAj4HCH7NNRjKlXJ3Z3_aHC7sneXh8mEdcZm0OJa-mTdxvRKd-yRktR2REdDLcGz5htUBjfgPK0Om2lJQ90mW0V0pHeOe8DmXWW9WQEc6twtD-3HzHdad8-1-DeDCyy_1uA4JsvUElNo3OQrXohtTpeDfJRUfbQ-G0U7FH5Ibui-e2FPyT5Fi2Aqr6MEI5tuGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
راه جدید انتقال پول را بشناسید
🔹
«کیف پول ایران» یک ابزار پرداخت الکترونیکی است که امکان شارژ کیف پول، انتقال وجه، مشاهده موجودی، برداشت وجه و خرید حضوری و آنلاین را فراهم خواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/454715" target="_blank">📅 12:45 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454714">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار لرستان</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db8b9829e0.mp4?token=fqAOz3sfd-dJLK6wSNMy2c-xUYjy_vyDQ_7kOKTU4nzkhLF_J_ie_IldqXd-MvHKeFT1dUrkwxLC-kGHH27g5zTXkirCasc3ymLIA2MbNF0xuhI80NlgZ3ETTL9KPUn7lCxsYGSEBuKzy65Su_rtQCXTGlXfk6yqrZbhuY1Fm9f0_MbEfaxw9mMF311Ad5fMhrUbPwwYlFeDE0ckzJeACvnuHokTFBWOYHrE57fPUjZNiXTRZGco-o1Oq-aYkSTq3oV5qy_M5frRiE1TvcEK4LHbbR9VQxpddST0W4lf_6k4016yQfP0RKJB9yCOQFzMESsI1NpqMtXkAVlUKRTZHkhKs6da_6i2wk0wxNF3DZTEcSTJAhrjPmsoukNxlcQmUFfly_4xaJGa2PhwuKWxBZ0j9n1X-EJQCYMPu9S2bvXPylID5Gx-KhVFWx5eHCKhB_izn9oV9-wTybP_h2oVQT9NJB3binNsOL3YWjp83rV8_6GuMDMP3dVF0eoIW0CIEOtuvD1AHrIQkkXyMfQz7UG316s-hzSVAK5SY0-lZos6mnaAVVqBIJodFpVNe5HE5clLKog8tAKZUCF7h7dtxkJlkEk1k3Nzo-AeNqtv3P-c-OCwGZiWNCRD3_p2VH_XiEIwEv7a7gHprDHKU_n9_icSZlW3IQzlYmHR1B9opRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db8b9829e0.mp4?token=fqAOz3sfd-dJLK6wSNMy2c-xUYjy_vyDQ_7kOKTU4nzkhLF_J_ie_IldqXd-MvHKeFT1dUrkwxLC-kGHH27g5zTXkirCasc3ymLIA2MbNF0xuhI80NlgZ3ETTL9KPUn7lCxsYGSEBuKzy65Su_rtQCXTGlXfk6yqrZbhuY1Fm9f0_MbEfaxw9mMF311Ad5fMhrUbPwwYlFeDE0ckzJeACvnuHokTFBWOYHrE57fPUjZNiXTRZGco-o1Oq-aYkSTq3oV5qy_M5frRiE1TvcEK4LHbbR9VQxpddST0W4lf_6k4016yQfP0RKJB9yCOQFzMESsI1NpqMtXkAVlUKRTZHkhKs6da_6i2wk0wxNF3DZTEcSTJAhrjPmsoukNxlcQmUFfly_4xaJGa2PhwuKWxBZ0j9n1X-EJQCYMPu9S2bvXPylID5Gx-KhVFWx5eHCKhB_izn9oV9-wTybP_h2oVQT9NJB3binNsOL3YWjp83rV8_6GuMDMP3dVF0eoIW0CIEOtuvD1AHrIQkkXyMfQz7UG316s-hzSVAK5SY0-lZos6mnaAVVqBIJodFpVNe5HE5clLKog8tAKZUCF7h7dtxkJlkEk1k3Nzo-AeNqtv3P-c-OCwGZiWNCRD3_p2VH_XiEIwEv7a7gHprDHKU_n9_icSZlW3IQzlYmHR1B9opRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرعامل توانیر: ۲۷ میلیارد تومان، پاداش گزارش ماینر پرداخت کرده‌ایم
.
@LorestanFars
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/454714" target="_blank">📅 12:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454712">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/626e29a2c6.mp4?token=R_lCuR4xZEYpczyQM14_M9T9Mvsn12PrxF140yrcSrssPMLzlOH3Mnw-UDrjTdDkJeISsmOkCWhrEkJxd2e-_q0CdB7dHXdQt7DfGVVxSCAoE7hrHxqqkDSJx9zEvdWXdhVhP6-__AtdAwM2D47fAsfKHpxFPQZJfEkMSV73JgspcI2OwbL5kDo9eEV2LqtzfuYc4koashnqCWKEdeakVwtQXXf2XjT3JRLkBXz4kGs5a1I_ugNUacMHviv3I6DOcFs8Vk3egjpL-2FC3OGDJZ7k0hiUZS1uCPGfSMMxdGxfOjodJO71wWiGkTodXBx-AIWL1XRi36YERPifGqMl-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/626e29a2c6.mp4?token=R_lCuR4xZEYpczyQM14_M9T9Mvsn12PrxF140yrcSrssPMLzlOH3Mnw-UDrjTdDkJeISsmOkCWhrEkJxd2e-_q0CdB7dHXdQt7DfGVVxSCAoE7hrHxqqkDSJx9zEvdWXdhVhP6-__AtdAwM2D47fAsfKHpxFPQZJfEkMSV73JgspcI2OwbL5kDo9eEV2LqtzfuYc4koashnqCWKEdeakVwtQXXf2XjT3JRLkBXz4kGs5a1I_ugNUacMHviv3I6DOcFs8Vk3egjpL-2FC3OGDJZ7k0hiUZS1uCPGfSMMxdGxfOjodJO71wWiGkTodXBx-AIWL1XRi36YERPifGqMl-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
انفجار در منطقۀ صنعتی «جبل‌علی» در دبی
🔴
منابع محلی از شنیده‌شدن صدای ۳ انفجار در سواحل امارات عربی متحده و آتش گرفتن یک انبار یا مخزن سوخت خبر دادند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/454712" target="_blank">📅 12:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454711">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa4ed34881.mp4?token=XVnlrmkWjM-VbbtJcQjTEyndfxi-0YV0k4yPUFHhJX1bgLpUXO3VOHKqr_fBhtio8IKjgXcyzYCA-2qJxDD6AbNBULNIT00xC1AQn-DFA3Cix5NISc6l3F5c_oSqRlaKlNFBXP9QyL55ly56Wideg73H7iMpGQBIMMIdF9LNeiBH_9mIueY-Devrg8Gfo9MHn3Q6XMHDKy7tF4vjVqGk6CF5Q4ISzeqvuceWk4Y8mqBZ14JmjEKqE-FEqMAsR_OTTIJq_9U4GtBHxxrA9vvrs77TPUfqTzEgAE3y4pdrcMsFKSmjXrKPtDFKIkyEajyaZcnQvQ9ghh4-UutA7nYrDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa4ed34881.mp4?token=XVnlrmkWjM-VbbtJcQjTEyndfxi-0YV0k4yPUFHhJX1bgLpUXO3VOHKqr_fBhtio8IKjgXcyzYCA-2qJxDD6AbNBULNIT00xC1AQn-DFA3Cix5NISc6l3F5c_oSqRlaKlNFBXP9QyL55ly56Wideg73H7iMpGQBIMMIdF9LNeiBH_9mIueY-Devrg8Gfo9MHn3Q6XMHDKy7tF4vjVqGk6CF5Q4ISzeqvuceWk4Y8mqBZ14JmjEKqE-FEqMAsR_OTTIJq_9U4GtBHxxrA9vvrs77TPUfqTzEgAE3y4pdrcMsFKSmjXrKPtDFKIkyEajyaZcnQvQ9ghh4-UutA7nYrDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
داداشم گمشده، شما ندیدینش؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/454711" target="_blank">📅 12:19 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454710">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jw_4ofSekNzEkrqlF7Uda5FohJrc3hNOeBuBYGscDdepRcyGDaQ3d7y6bdgFt8SHz5spGamX8ERKFpbZBFqqdbIHdBgtiF9blLAdfMAIlRHWH_uqL4sQQjRtM0Jzf6ZnY3fmvypE6dkcj6Cq8IhX4KN7gRPUD3HPzAQlV4l5QXIgzWJWn8SaNnXeKTUVka_7Zzq7EHzdv40f2KLqqEpjAnF1Dlt_vMxfhxJpdl4tJjEHkCRdTyICCwq_oCfJI3Btow0Oi3hbDG1DXI5sXYFFduFprS5sbtPhnyR2q2Di904hyCGaen9NlbaL6dTFbTixkLIDGvJfPa70_7fO4udVsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سرپرست وزارت دفاع: دست نیروهای مسلح ما برای پاسخ به هر تهدیدی پُر است.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/454710" target="_blank">📅 12:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454709">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">سخنگوی ارتش: توان رزم ارتش بی‌وقفه درحال ارتقاست
🔹
امیر اكرمی‌نیا: با گذشت ۲ جنگ تحمیل‌شده از سوی دشمن، امروز ارتش در آمادگی کامل قرار دارد و با نوسازی سامانه‌های آسیب‌دیده، ورود تجهیزات جدید و تکیه بر توان داخلی، بی‌وقفه مسیر افزایش آمادگی عملیاتی را دنبال می‌کند.
🔹
ورود تجهیزات جدید به یگان‌ها، موجب شده تا ادوات و تجهیزات رزمی ارتش متناسب با نیازهای روز بازآرایی شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/454709" target="_blank">📅 11:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454708">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ons_9as3foT57pVm7rlJK_30Ev9li_BysGP-QaQzosACyjQPnkc1sdtbkgLlFagG2BvFvFHMO3KAhDmitGYrRdEOpfNaDOhXnvIxDZsSXfsbBbLr2FZnOHh7GwAUg3oZKwtTGBbhkAjVv7DLRGxRhdzMoyTafW6cBOfggUEVd6zQZZsglqYWF-e6jfljizV7IvjBxy-FIVdXUZnuQhLWR_0YAabT87i1CfOjXNvs7mGJRLbbxIFIwmfqHKrbvwjHUU3dnfjxcBN6Alck1Vl-GV6-XsvxU03w4SV7Wv9qeAj_C_z6K9MrYsqT-OZYc-jbdvQR4QUc94uoi7Lj2ThGEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
پزشکیان: شخصیت آیت‌الله سیدمجتبی خامنه‌ای استثنائی است
🔹
این حرف‌هایی که برخی افراد درباره برخورد رهبر انقلاب با ما می‌گویند، هیچ نسبتی با شخصیت ایشان ندارد. @Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/454708" target="_blank">📅 11:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454707">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8jCbVgymNo7ITjwM4wlqA9FbGki03cNb9mp-GRLXtu5KR7TJ4m4ANkpe4Qa_NJGm2lgHlOaWMWSCNKK4NqvdYWiFRgwQxQpfhKRSwRGvzRbvvM-HUJ18qvEizFHwvJrk3tZiY0DcdMWc2Vle0XZjjXJMUlzvYtdP0mUUlvJk7TSyT2h3VaNin6oJg1MmNugL32_DtXLBU8dGM8GU-j0q5QYF-iD0hb1fr90eKvltt8SXNCMb5tgejXx1mh6hme-biYvuZAkVDHFwWjJ_aMO8jjgSwfx_jnJvMrgi90rABV6Y9HbOrzyk7nA9AEo2nY2PN7Sa8HvZiezFM1Y3crGiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاییز پرباران در راه ایران
🔹
سازمان جهانی هواشناسی به‌تازگی اعلام کرده احتمال شکل‌گیری پدیدۀ النینو در تابستان ۲۰۲۶ حدود ۸۰ درصد است و این احتمال تا پاییز و زمستان به بیش از ۹۰ درصد می‌رسد.
🔹
النینو که با گرم شدن غیرعادی آب اقیانوس آرام شناخته می‌شود، معمولاً بارش پاییز و زمستان ایران را افزایش می‌دهد.
🔹
براساس پیش‌بینی‌های موجود، تمام ماه‌های پاییز از بارش بالاتر از نرمال برخوردار خواهند بود، اما اوج این بارش‌ها در ماه اکتبر (۱۰ مهر تا ۱۰ آبان) متمرکز شده است.
🔹
در این بازۀ زمانی، انتظار می‌رود سامانه‌های بارشی متعددی وارد کشور شوند و بخش‌های وسیعی از ایران، به‌ویژه نیمه شمالی، غربی و مناطق زاگرس را تحت تأثیر قرار دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/454707" target="_blank">📅 11:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454706">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJakqV5eQOlPkruAXg9g0T3AxenKgyvSYFVBBu-b04xlYzeoGi9lhWbKKZEJB4DtWFYa9rF-6iRzwM-a4wQ59stK0Lbg7veBIaPUTdNsKe1WYhjoz1phEyyJDwEseqhhQmaAaTWUt9d-6tDsgVDd18OqQ_8zs8vScyqLbVJJZgQcxnr0F35Imi_Kb8P3EGs0LLCCEwbl5djilEWsLQwivg5V6SjmBuOsqIETgXTfS36DiTmc4xKmp6ulcjdBv1HSL_QU_xIPkc6skedL62uF0l0IVv2jI08mmricws1Gqew36IMjTUUoYg5XCrghbzWTaHl7OUr1RquVmfzE-dvLkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده نیروی هوایی ارتش: در دفاع از ملت ایران جان برکف خواهیم بود
🔹
پیام امیر سرتیپ خلبان بهمرد به‌مناسبت سالگرد شهیدان بابایی و لشکری: محال است تاریخ ایران سربلند، سر به زیری و خشوع و تواضع نابغۀ جنگ، سرلشکر خلبان عباس بابایی را از یاد ببرد و چه دور از ذهن است فرزندان این آب و خاک، نام سیدالاسرای ایران، سرلشکر خلبان شهید حسین لشکری را مترادف با واژۀ آزادی ندانند.
🔹
در مسیر اطاعت از ولایت و دفاع از ملت بزرگ ایران در برابر تجاوز دشمنان قسم‌خوردۀ این بوم‌وبر، میراث‌دارانی خلف و رهروانی جان برکف خواهیم بود.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/454706" target="_blank">📅 11:19 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454705">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUvpzmR3aVDWHo7Rsg1TqMNcq3At4-O6wd3i8kFnU55HFC-_Jd4lbIrzY3xY8MSRI2vAT9wCK2t4ubZPn_02vPmLON7__E4KKsWDTh5qRNhMiRvJtwje646Avvb_oUpNIm4t3jfh76IQ_xhqcWDZL6mR_enwgyRzsV4fXI_az6-enyd2621K_VPX5lz6H6ojEracrWt7ODX9WObumfZzATr4Uq4lk_htDlWDFkNyA_smkscT2qoxIo_gZIpSdoOBN2jum6ileEmHzoMoWdfNOjCrhusFEnO5WUCE-PpMOSy9prVSHnAT-2pbocGlljvmO6b4W6frTbd52XElhrn5BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا فاتح جام‌جهانی فوتبال شد
⚽️
اسپانیا ۱ - ۰ آرژانتین  @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/454705" target="_blank">📅 11:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454704">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">تمدید فرصت ثبت درخواست معافیت سربازی برای مشمولان دارای ۳ فرزند و بیشتر
🔹
سازمان وظیفهٔ عمومی اعلام کرد مهلت استفاده از معافیت خدمت سربازی برای مشمولان دارای ۳ و ۴ فرزند تا پایان سال ۱۴۰۷ تمدید شده است.  شرط سنی استفاده از این معافیت چیست؟
🔸
مشمولان دارای ۳…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/454704" target="_blank">📅 10:49 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454703">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48cd5ccefe.mp4?token=qKWzUNUoLYQO7TxYkQ2NMcQK-0lZkI1xxghS8gKKVXdhf7TDm301eHKmA2XRUYk1ESVIpFxLjoL8oIIIU8D-pbWMFFgpXlQUhZzVQ8Edqczci5-QcX3m6nD_-7v4DYiQ0kwZc2NZG5KFfe4aU69jw0InQpEWW49YUE7YuWwXArFqubu6JIk0Kk-dqLXjJzIK5go6rnR_YFbrESfUMl3g687ULeR_X1DVWvRJfXiZ519Mqk4muAdhqjxTh7t_DURabAtXnhtfJghwBw7E_rl9vys47C4QXZnXXiFhW6J4-B2kjrSP-WT54ttE3stl96IrfnmKAWb8q0P6W_61eeAlTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48cd5ccefe.mp4?token=qKWzUNUoLYQO7TxYkQ2NMcQK-0lZkI1xxghS8gKKVXdhf7TDm301eHKmA2XRUYk1ESVIpFxLjoL8oIIIU8D-pbWMFFgpXlQUhZzVQ8Edqczci5-QcX3m6nD_-7v4DYiQ0kwZc2NZG5KFfe4aU69jw0InQpEWW49YUE7YuWwXArFqubu6JIk0Kk-dqLXjJzIK5go6rnR_YFbrESfUMl3g687ULeR_X1DVWvRJfXiZ519Mqk4muAdhqjxTh7t_DURabAtXnhtfJghwBw7E_rl9vys47C4QXZnXXiFhW6J4-B2kjrSP-WT54ttE3stl96IrfnmKAWb8q0P6W_61eeAlTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۸۰۰ سازۀ آمریکایی خاکستر شد
🔹
آتش‌سوزی‌های مهیب هفتۀ گذشته در منطقۀ اسپوکن، واشنگتن، دست‌کم ۸۴۶ سازه را ویران کرده و بیش از ۶۰ هزار نفر را مجبور به ترک خانه‌هایشان کرده است.
🔹
مجموعۀ آتش‌سوزی اسپوکن از ۳ حریق جداگانه تشکیل شده که تا روز سه‌شنبه بیش از ۱۰ هزار هکتار را سوزانده است.
🔹
به گفتۀ مقامات، یکی از این آتش‌سوزی‌ها عمدی بوده و مظنونی در این رابطه دستگیر شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/454703" target="_blank">📅 10:45 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454702">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/128a1a4b69.mp4?token=poBhDMTBYI2bV5UjwX5PPzWkXtibl6gDegpXOrfwkUWe1t62KQA-RawtG8V-3vZg27plvLmLtKJb8Y22tco7oQMjkFyDDP3lQZsamhb8Tr0sP1odwwn2uuFqeu3IwQ8QyrNQMFeqEdLkRgzQ9mQDkX4KaEKWYrwlP4PVGvCyTbElV-rrw6eX0M_2_xNSrZi7DPmsM2xXX0gdof0MYIfR0q1rGUXAtIKGPCGaQt5jNlOdDPJNZpad0emllHr6LV1GvF6ju6EWzeBTaUyn59SUUOr3FElAsyxBr-ZG5UrE8y-6rlFVNS0nkEfPMkYbq9-SynFA7u1a8MuhB2sU6KROfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/128a1a4b69.mp4?token=poBhDMTBYI2bV5UjwX5PPzWkXtibl6gDegpXOrfwkUWe1t62KQA-RawtG8V-3vZg27plvLmLtKJb8Y22tco7oQMjkFyDDP3lQZsamhb8Tr0sP1odwwn2uuFqeu3IwQ8QyrNQMFeqEdLkRgzQ9mQDkX4KaEKWYrwlP4PVGvCyTbElV-rrw6eX0M_2_xNSrZi7DPmsM2xXX0gdof0MYIfR0q1rGUXAtIKGPCGaQt5jNlOdDPJNZpad0emllHr6LV1GvF6ju6EWzeBTaUyn59SUUOr3FElAsyxBr-ZG5UrE8y-6rlFVNS0nkEfPMkYbq9-SynFA7u1a8MuhB2sU6KROfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملۀ خلبانان ایرانی بدون GPS به پایگاه آمریکا
🔹
معاون هماهنگ‌کنندۀ نیروی هوایی ارتش: خلبانان ما آموزش‌دیده بودند که بدون استفاده از GPS و INS، تنها با نقشه و سامانه‌های ابتدایی، هدایت جنگنده‌ها را در ماموریت‌های مختلف تمرین کنند.
🔹
شاید برگ برندۀ ما این بود که هیچ‌گونه سیگنال خروجی، حتی سیگنال رادیویی، از هواپیماهایمان وجود نداشت و احتمالاً در روز نخست، دشمن تصور نمی‌کرد نیروی هوایی جسارت اجرای چنین ماموریتی را داشته باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/454702" target="_blank">📅 10:35 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454700">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u593cs0psuiaPSbMIP_Zdk8Vxnmjr2YRgwep1GS9sqlNZlMAFLNXJ4rV_57ljAg6JXpfOZ1Ai-O9y9paHFS65Mgzky7AHTyCtPXe0YZtYPzn_FLCeZZxnaoaycGNi08MRCIVJCNV3eG15XTX3svAqi7FtXv20jBHN_9C_OC5m_4ISBNrkzFm-VFKNxC4hJstoP1rBEzqFvsSJ_ZPM-qkwCC_RgysV9tJPod1YyKTFiVIHP_9OTd7N3fqEolqXiHGlE4BfTMpbXbSCp0pOecZHCVoy0SnCYu-YkOkwjlSs-L_U_jwCoX71rTTNiaUClcEcKITSUP3ThUFdIJ2D03avA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hnLjz5icCsrrryn1aNMioGFwcEeqO9mJgxAJm0SR4rRR7CiSTz_rKRB1KsGs-qKP3jFLgfb9XykrB4-HcRRXtaCoGbqjP8mGIeL4gUBjEmEyNhl6uhmrKEjBzwKFSkjpHZ46LZJJng-lBphdez7tbDoA4f9an7H-gT8f9eX0oQYpEusHcjW7P5vbcLDDR9FEJqkgach9hBiuIY6X9_ePWM_voNGjKDb_oqd7AHLrJP1YREiLvXD0_UXphEXp3m6qnFCSXpd8f_Buz5sMMywqFyKeKAqEARkanKGLEmgaleqfY3lCzTl6SI76UJ0zhIpYNyUQMSpAcktO-6P-XTA9bg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‌ تلهٔ حزب‌الله ۲ نظامی صهیونیست را به هلاکت رساند و ۷ نفر را مجروح کرد
🔹
رسانه‌های صهیونیستی گزارش کردند که در پی انفجار یک ساختمان تله‌گذاری‌شده در شهر مجدل‌زون در جنوب لبنان، ۲ نظامی اسرائیلی کشته و ۷ نفر دیگر زخمی شدند.
🔹
براساس این گزارش، نیروهای ارتش…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/454700" target="_blank">📅 10:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454699">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFYKjUueQ8M4BIsyi0rftHfdBhtPaBDGnwqeFlXgiq10W-FzrAT4oMejGelARGFdBxzLqQIIgMDEIQQWXeowTwk3WK1OizXLoUzwLEexrWtaJHdv2rT2ufJz5Qd0w0xWhGHExkluvIXpQ-Hmp1CZU-D-3bWGhzfxUGaom4APCc2ma-fz5nFTAsF4oM9oEmW6CLtYrIhNfucfvLhISLgsrnCMOx7jygd9kDF76tqEFqG0a8zovpNKfnL2HQzCMcl5P1io3yXAcwQ9ACkYFYpyRxp7OAwu65ZCk_9Cz042-WIUPzs6J19nYj__-ei59OC1tlP3wTQBu78f7WBfHquFPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این آقا هر وقت دختر موطلایی می‌دید دست‌وپایش می‌لرزید
🔹
اسدالله علم، وزیر دربار می‌نویسد: «در سرخس خانمی را که نسبتاً خوشگل هم بود و از مشهد آمده بود به شاهنشاه معرفی کردند که ایشان نمایندۀ سرخس در انجمن هستند…» محمدرضا پهلوی از لفظی استفاده کرد که صراحتاً از نگاه سخیف و ابزاری او پرده برداشت.
🔹
علاوه‌بر این محمدرضا در مصاحبۀ رسمی‌اش با اوریانا فالاچی، خبرنگار ایتالیایی، در سال ۱۳۵۲، بدون ذره‌ای ابهام اندیشۀ واقعی خود را روی دایره ریخت و گفت: «در زندگی یک فرد، زن به حساب نمی‌آید مگر وقتی که زیبا و دلربا باشد…» این منطق، حقیقت ساختاری رژیمی بود که زن را تهی از عقلانیت، مسئولیت و نقش‌آفرینی تمدنی می‌خواست.
🔹
اردشیر زاهدی، داماد شاه و سفیر وقت ایران در آمریکا نیز در خاطراتش می‌نویسد: اعلی‌حضرت به‌نحوی افراطی و غیرقابل باور به زنان و دختران موطلایی علاقه‌مند بودند و هر وقت دختری موطلایی می‌دیدند به وضوح دست‌وپایشان می‌لرزید!
🔹
خروجی این رفتار، افشاگری‌های متعددی بود که حتی همسران شاه را به ستوه آورد؛ آن‌چنان‌که ماروین زونیس در کتاب «شکست شاهانه» می‌نویسد ملکه فوزیه و ملکه ثریا بارها شاه را تهدید کردند که اگر به زن‌بارگی خود در محافل خصوصی ادامه دهد، از او جدا خواهند شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/454699" target="_blank">📅 10:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454698">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ec7f26e41.mp4?token=up8uHhns8OxnkxqoZqmD4lD-802bUVs0RnNK-kWXy21kqf8RO-gfCM8xrwMQyGag70qv7uTPFLC3N5HWoGs_RpqUIMRJWfr2JhO2MDxS0-V7u5Ecbb6p6IUroMouaz7fNyZKgxRGRMfyIKCzK14Llp43HdpJchpah9fwOyvVlXYacvqqjmCi_k9QeEewl2MzgpNooTGLBNBECUHU5YH35xHLEflgOKEqP5EATNYrYE8IlrhMDd_umwQzFh8sOCj1LlTujAON23AiWMh7Rzx8_X_8uQfHcnMuUgKpTKz5EvXXq2pZ-1aniEXVVdLmRC0W951vWq98EV999pe_CouHGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ec7f26e41.mp4?token=up8uHhns8OxnkxqoZqmD4lD-802bUVs0RnNK-kWXy21kqf8RO-gfCM8xrwMQyGag70qv7uTPFLC3N5HWoGs_RpqUIMRJWfr2JhO2MDxS0-V7u5Ecbb6p6IUroMouaz7fNyZKgxRGRMfyIKCzK14Llp43HdpJchpah9fwOyvVlXYacvqqjmCi_k9QeEewl2MzgpNooTGLBNBECUHU5YH35xHLEflgOKEqP5EATNYrYE8IlrhMDd_umwQzFh8sOCj1LlTujAON23AiWMh7Rzx8_X_8uQfHcnMuUgKpTKz5EvXXq2pZ-1aniEXVVdLmRC0W951vWq98EV999pe_CouHGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مشهدالرضا منتظر میزبانی از دل‌های بی‌قرار است.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/454698" target="_blank">📅 09:59 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454697">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NM3d0m9SZj9Q-V3sEx9geLi4c29hEmtCVe68yymLijdzbvsGH2gqiiwAAEtcLKdlqI1ckoWS8tuAo6Bv5Vr81s6Jm2KtLscg7HYcSLQxUNc0zxrGVHq5YmJCGIjN9sdqkbgj0s2cWdVdsqkHMKSDwy1CJj1E678ErxFjErVNl98KQwVKhxj3D58Mseh_JcYHr1wm2-WM2aOcKxsxJ6n6K-d0Zk_YrX9NOjtQFqV5Uhil3n3Hr0c0rEvuEcOcSEw79wU4JEDXlw6dVWtEL6yYJOR_4Ts9J_cBlLa9nmHPYwiJW5-CzUqD2vtIqnRf-MyVgnhsyBb7d_usZKXZ9epJSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازار ارز به کدام سو می‌رود؟
🔹
بازار ارز در هفته‌های گذشته بیش از آنکه تحت تأثیر عرضه و تقاضای واقعی باشد، از فضای روانی و انتظارات معامله‌گران تأثیر پذیرفت.
🔹
افزایش تنش‌های سیاسی، رشد انتظارات تورمی و تقویت تقاضای احتیاطی، دلار را وارد کانال ۱۹۰ هزار تومانی کرد.
🔹
اما اکنون شرایط تا حدی تغییر کرده. کاهش نگرانی‌های کوتاه‌مدت، افت حجم معاملات و عقب‌نشینی خریداران هیجانی موجب شده بازار وارد فاز استراحت شود. این موضوع باعث شده دامنۀ نوسانات نیز نسبت به هفته‌های قبل کاهش یابد.
🔹
البته کارشناسان تأکید می‌کنند آرام شدن بازار الزاماً به معنای تغییر روند نیست، بلکه می‌تواند نشانه‌ای از انتظار معامله‌گران برای دریافت سیگنال‌های جدید باشد.
🖼
اما کارشناسان تکنیکال چه می‌گوید؟
🔗
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/454697" target="_blank">📅 09:49 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454696">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">انهدام مهمات عمل‌نکرده در پاکدشت
🔹
روابط‌عمومی سپاه سیدالشهدا تهران: انهدام مهمات عمل‌نکردۀ تجاوز آمریکایی‌صهیونی در شهرستان پاکدشت از ساعت ۹ الی ۱۲ صورت می‌گیرد و جای نگرانی نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/454696" target="_blank">📅 09:35 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454695">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
دستگیری ۸ تروریست که مهندسین حوزۀ زیرساخت را گروگان‌ می‌گرفتند
🔹
روابط‌عمومی قرارگاه قدس نیروی زمینی سپاه: ۸ نفر از اشرار و مرتبطین گروهک‌های تروریستی منطقه که با تشکیل تیم‌های مسلح اقدام به ایجاد ناامنی و اجرای اقدامات مختلف ضدامنیتی، گروگان‌گیری نیروها و مهندسین فعال در حوزۀ زیر ساخت‌های سیستان‌وبلوچستان، حمله به گشت‌ها و مقرهای نظامی و انتظامی، سرقت‌های مسلحانه و ایجاد رعب و وحشت در مناطق مرکزی استان می‌نمودند، دستگیر شدند.
🔹
از این اشرار مقادیری مهمات و تعدادی سلاح کشف گردید. اهداف این اشرار شناسایی مقرها و اماکن نظامی و انتظامی و همچنین شرکت‌ها و نیروهای فعال در حوزه توسعه و آبادانی استان بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/454695" target="_blank">📅 09:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454694">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/759e96e986.mp4?token=knoB1WeLObCnzxFAAqv1SIJFIvSONaiircY8kpCpWlDRD8zIdxIXCCurut7qVM_w68zcOpycwdpCyvdpH2wpS96U2QQXWQBoobcVj11gtzbFiQ4yDXdn5J0jt4PJtmmkP6cM_yIohBtOKd4GawsgFfcQhhIXVFKHVqeQsfkV8DHotvh0S8lkWKp0RlvcC3gaRXEAPyA991KmsrN5vUCKS56Jd8oIiJ_1BtEZTXU74Az-U-AfpNFvDxEmJLDAGSbpy2XXNiJFzffQJSUFig4f0ICLg6gD2b2IZG85zHKFcE1TvPGh9hTFbSPIgg1L3MOZI7AReMUd3BZLI190DVIcUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/759e96e986.mp4?token=knoB1WeLObCnzxFAAqv1SIJFIvSONaiircY8kpCpWlDRD8zIdxIXCCurut7qVM_w68zcOpycwdpCyvdpH2wpS96U2QQXWQBoobcVj11gtzbFiQ4yDXdn5J0jt4PJtmmkP6cM_yIohBtOKd4GawsgFfcQhhIXVFKHVqeQsfkV8DHotvh0S8lkWKp0RlvcC3gaRXEAPyA991KmsrN5vUCKS56Jd8oIiJ_1BtEZTXU74Az-U-AfpNFvDxEmJLDAGSbpy2XXNiJFzffQJSUFig4f0ICLg6gD2b2IZG85zHKFcE1TvPGh9hTFbSPIgg1L3MOZI7AReMUd3BZLI190DVIcUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کمدی ترامپ در لاس‌وگاس: کودکی که طعمۀ سیاسی شد!
🔹
دونالد ترامپ این هفته در لاس‌وگاس یک نمایش انتخاباتی دیگر به راه انداخت؛ این‌بار با یک بازیگر خردسال که هنوز درست حرف زدن بلد نیست.
🔹
او هنگامی که کودک ظاهراً قصد خروج از صحنه را داشت، به‌سرعت دستش را دراز کرد و مانع شد و بعد با کنایه‌ای به رئیس‌جمهور سابق، گفت «نمی‌خواهم مثل بایدن از روی سن بیفتد» که با خنده و تشویق حامیانش همراه شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/454694" target="_blank">📅 09:04 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454693">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/116eee5985.mp4?token=NeP40nwa3TMmCVv53SVkql0BfmZ0e-tNe1KyA3Bg86LFp9900mCtMMwsBZzZ5rmL8y6gpr2X-H4RIDnXyQojxiwHgcmNuKEPvczu6Ivp4-6qaFD-bbkmrTo70HmqLs_1TN1P-83QRPvBzN2-ZoR0sL58B2jz7PQMzhvrDje-jGhyEQwe0I_7pdSe9dybQzoJHOFQsUZsEtZhN8AqT_i49ZGJaqAbrX3D5cY6pisbMShEhupaw3zTliNsD4Y2FD0nhzleDxEkZK4_QrNjyK7hpH6Jqrfzjs5P6jFRUjJI2D0LIOA1huF76AOtB_cAo667Kc_BGkPzOhYHfeRoUXwHnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/116eee5985.mp4?token=NeP40nwa3TMmCVv53SVkql0BfmZ0e-tNe1KyA3Bg86LFp9900mCtMMwsBZzZ5rmL8y6gpr2X-H4RIDnXyQojxiwHgcmNuKEPvczu6Ivp4-6qaFD-bbkmrTo70HmqLs_1TN1P-83QRPvBzN2-ZoR0sL58B2jz7PQMzhvrDje-jGhyEQwe0I_7pdSe9dybQzoJHOFQsUZsEtZhN8AqT_i49ZGJaqAbrX3D5cY6pisbMShEhupaw3zTliNsD4Y2FD0nhzleDxEkZK4_QrNjyK7hpH6Jqrfzjs5P6jFRUjJI2D0LIOA1huF76AOtB_cAo667Kc_BGkPzOhYHfeRoUXwHnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حکم ۱۷ سال حبس برای عمران‌خان
🔹
الجزیره: عمران‌خان، نخست‌وزیر سابق پاکستان، به همراه همسرش پس از آن که دادگاهی در پاکستان آن‌ها را به نگهداری غیرقانونی و فروش هدایای دولتی ارزشمند متهم کرد، به ۱۷ سال زندان محکوم شدند. @Farsna - Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/454693" target="_blank">📅 09:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454692">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FwCP0h1CwTYuCetLJ9TeiWANF873eoQHYpwWydByKkVp6FzPtO7Ki_YGxMnU1M4Qexz_w2ddlc35Yx8RRCiBWD3ADAWbGkn_EXmcNrT-g8F2jm47yRv-AYIHsF_8jvXmr4-0uNO6atX19V-YN8OOmjpMsMTfB6yj2SlGMjPVqWE6KQe1M0pXqQkkitkW1QVQdUYBWS_inaVSbcTvOuS90zB-UzxBcb05AVm0UTpD3o4qHpoCtUsiSHvpuT7FHj9Se7EVaIotDI_Z3-rvPFIvTO3MUyanpzfDNg3af_nP8j3udABKcc72B8f4QSDMhtfxifzhdntmxlMWbof7q5F3PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پهپاد بمب‌گذاری‌شده در قلب فرودگاه آلمان
🔹
مقام‌های آلمانی اعلام کردند یک پهپاد حامل مواد منفجره در فرودگاه لایپزیگ/هاله آلمان کشف و خنثی شد و آن را نمایانگر «سطح جدیدی از تهدید» توصیف کردند.
🔹
وزیر کشور ایالت زاکسن گفته مقامات در جست‌وجوی قطعات یک پهپاد احتمالی دوم هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/454692" target="_blank">📅 08:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454691">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a38ed22c5.mp4?token=i20XVJWGE-nKa1iiEnrqoxYt-OEkEzWlQKXHMS_1pEO0ZpvRpbLKvm6HiL6inID2s2apZFdJ0AhS8XOPuGNbhvX0ZEg-ZTr_QfKuwdZTE8kalkXi0-YBbHVGCY9eGgC6PnuYUaRS8UuJbAmQ3V_wzG_mioJdlDDI_itIXkWwzdU07ic85VC2TCdslinr8SDX4fBimlL1xvRjHfqyHJ6iDJ0PXZSrYoxpk2--BWSXam1-ednNNCfJfIl1lHqQZouMkYYN3GE1qU7HNGRvjNUEnkR-5ASKwutWsF3oi1UeAnIT1K4RHnu4BZs2v3wgKpPPprpGSG9Oh9SssKLpau98Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a38ed22c5.mp4?token=i20XVJWGE-nKa1iiEnrqoxYt-OEkEzWlQKXHMS_1pEO0ZpvRpbLKvm6HiL6inID2s2apZFdJ0AhS8XOPuGNbhvX0ZEg-ZTr_QfKuwdZTE8kalkXi0-YBbHVGCY9eGgC6PnuYUaRS8UuJbAmQ3V_wzG_mioJdlDDI_itIXkWwzdU07ic85VC2TCdslinr8SDX4fBimlL1xvRjHfqyHJ6iDJ0PXZSrYoxpk2--BWSXam1-ednNNCfJfIl1lHqQZouMkYYN3GE1qU7HNGRvjNUEnkR-5ASKwutWsF3oi1UeAnIT1K4RHnu4BZs2v3wgKpPPprpGSG9Oh9SssKLpau98Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: به نظر نمی‌رسد تهران دیگر رنگ دمای ۴۰ درجه را به خودش ببیند.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/454691" target="_blank">📅 08:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454690">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6bc792275.mp4?token=cMNg6ShKJQfi6uJX5Ud31TXUbcbW6lGSlctIkhB6ESRRHYKw4tNzyiwQaOk8917Fj5cCwEMvgYvXVOkJ1-cdNEzAtMQQDufrwGwHeo8lOxTu8HGg5zyEB4h819OK-1zF04A4_8wi7a5i2L_R1ZYBFsDa7s9tlUwYqp-ALRXiXP4Y1BHOqdKiag2EuuhvSqN27CA6Z440rmDL7-5sHJV4_bqoR2dVeTap_sdRBOAEPRlcT6K1dsaOB0dhLGcG5eo8tfFzj73rSCpPVyJ3rik1IFEPykEs0Lq9JEaQ1WlfMbhu_iCTnMAwO2RZVlqWV5RsPsr7wL1rwXhzKPlhmofnRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6bc792275.mp4?token=cMNg6ShKJQfi6uJX5Ud31TXUbcbW6lGSlctIkhB6ESRRHYKw4tNzyiwQaOk8917Fj5cCwEMvgYvXVOkJ1-cdNEzAtMQQDufrwGwHeo8lOxTu8HGg5zyEB4h819OK-1zF04A4_8wi7a5i2L_R1ZYBFsDa7s9tlUwYqp-ALRXiXP4Y1BHOqdKiag2EuuhvSqN27CA6Z440rmDL7-5sHJV4_bqoR2dVeTap_sdRBOAEPRlcT6K1dsaOB0dhLGcG5eo8tfFzj73rSCpPVyJ3rik1IFEPykEs0Lq9JEaQ1WlfMbhu_iCTnMAwO2RZVlqWV5RsPsr7wL1rwXhzKPlhmofnRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عطر برنج تازه در شالیزارهای شمال پیچید
🔹
شالیکار گلستانی: امسال خوشحال‌تر از سال‌های گذشته هستم، چون به‌عنوان یک سرباز در جبهۀ جنگ، امنیت غذایی مردم را تامین می‌کنم.
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/454690" target="_blank">📅 08:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454689">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34a86cac7b.mp4?token=VWpMR9b40igNA4lvpN_kN-Unty9FDBIII5p-xi6VgMTSFdqqev0kgwxDWjGSZ3CIrfYNxGgBtQ4vlDKHLKxwfafguBjeMpoD2ONsmty538qnzCCu2s4rh9XfbYW6zqh_byc5ey4vixJH2ZzYCWYbHXZPA1ORbvhB5GgcGh9Ydw7AUMKB1w7LzqA8t9_bTSBRBVvz6V5R58DzeC4a6LAdU7fVQPAQad70afOVukqufLpWfyd5OpNE6o6tuCtkLDvrF1i2nyKHQJkL8D9sAOstwBuQT5d8v2YuCDqr38t_dXYtJwNXF4bXFFTAoBm0qWgV38-4vixhZ_9Ol6PhQALmpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34a86cac7b.mp4?token=VWpMR9b40igNA4lvpN_kN-Unty9FDBIII5p-xi6VgMTSFdqqev0kgwxDWjGSZ3CIrfYNxGgBtQ4vlDKHLKxwfafguBjeMpoD2ONsmty538qnzCCu2s4rh9XfbYW6zqh_byc5ey4vixJH2ZzYCWYbHXZPA1ORbvhB5GgcGh9Ydw7AUMKB1w7LzqA8t9_bTSBRBVvz6V5R58DzeC4a6LAdU7fVQPAQad70afOVukqufLpWfyd5OpNE6o6tuCtkLDvrF1i2nyKHQJkL8D9sAOstwBuQT5d8v2YuCDqr38t_dXYtJwNXF4bXFFTAoBm0qWgV38-4vixhZ_9Ol6PhQALmpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ونس: ایرانی‌ها مذاکره‌کنندگان سرسختی هستند
🔹
معاون رئیس‌جمهور آمریکا در مصاحبه با شبکۀ «فاکس‌نیوز» مدعی شد که از تمام ابزارها شامل نظامی، اقتصادی و دیپلماتیک برای رسیدن به راهکاری برای ایران استفاده می‌کنند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/454689" target="_blank">📅 08:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454688">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">دریای مازندران فعلا مواج و تعطیل است
🔹
هواشناسی استان مازندران با پیش‌بینی وزش‌باد و مواج شدن دریا، تمامی فعالیت‌های تفریحی، صیادی و قایقرانی را تا اواخر وقت جمعه ۱۶ مردادماه ممنوع اعلام کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/454688" target="_blank">📅 07:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454687">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XSzR45UDdl3fumD0hMUt1s5YhBx-zzq4zyMF7-WoZsIW-yoVo-pzXpgoaXrstoTwFUQuKqbthRtsn90ZWPZSX2ZYkpIVbEH7DyYQejMZnJhA3K839tMJ-E0W8htkw0bNpf-DMZ4N7xDJ6ltp1wXYIuNhO-BjexMVl2XynkFRtJfiQIMbKIXNhs6iMa9DOLRsSi9Eq1sN1LTFJ0hMz5s1IKNz28a1uztQ-gRmscHRhTKibvBT-E52FIfcNMVRPm_3IutKX_D8mD-jFUd7A7NnXn1P-pB6O1wpXVF1nCk8NTsasQQI8Htb1DXKDVVCbwOe2R0zN_IolCH2aznJFVuwAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ زمان شارژ اعتبار کالابرگ تغییر کرد
🔹
معاون رفاه وزارت کار: از این پس اعتبار کالابرگ در روزهای ۱۵، ۲۵ و پنجم ماه بعد به حساب سرپرستان خانوار واریز می‌شود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/454687" target="_blank">📅 06:01 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454686">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">آمادگی خراسان‌رضوی برای میزبانی روزانه تا ۲ میلیون زائر
🔹
مدیرکل هماهنگی امور رفاهی زائران استانداری خراسان رضوی: یک میلیون و ۲۰۰ هزار ظرفیت اسکان برای اقامت زائران پیش‌بینی شده و امکان افزایش تا ۲ میلیون ظرفیت اقامت روزانه وجود دارد.
🔹
ناوگان حمل‌ونقل جاده‌ای با بیش از ۱۸۰۰ دستگاه اتوبوس تقویت شده و پروازهای روزانه تا ظرفیت ۲۸۰ پرواز افزایش یافته است. حمل‌ونقل ریلی به مجموع ۱۳۶ رام رسیده و امکان جابه‌جایی مسافر تا ۶۴ هزار نفر در روز فراهم  است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/454686" target="_blank">📅 04:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454685">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4xHawK2Yv4rckR4voWb5XBuidcW9ZK04zAeuKGSFlEypsOIj1qpsR1-hgCZ5qU9M3h7eUhhtNCMxQZo-UnQj3DgUoANGeMUjHV8DnrQConE6bd1oyfRNkgLhlCvGMezl6BzlZA6nj0wMPbm18g3T9LhIVA-BSGGiKIh-p_o2dN5EtmnbXC6QXtQC8k2XZdiGUlMJlv1IPcejYbbgb71w5nLu9zbXMwIkIA_Td6mBAAwPM8tEA682VbeMONTryMy5aXS-sDeis1RJYcJFrims80O_bxrAKlovQhS1nw21REDItof9UeXEAKjgjip7Y5QBx9Z8ZaFXpmxGo_A3ntrgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حادثۀ دریایی در تنگۀ هرمز
🔹
سازمان عملیات دریایی انگلیس از دریافت گزارش‌هایی دربارۀ حادثۀ امنیتی برای یک نفتکش در نزدیکی سواحل عمان خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/454685" target="_blank">📅 04:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454684">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7Eh2eKfXHhjqoE-apXhVbBIoCLZJvTpztae9v8NyND9anxoendYSePPVnernh3bMVmUyOCcxjomT-QGAaRkGDpsDiTCp1E-aQU3Mo4cSpmYqzwFS9KdSvbodQVGMokQyNrpSXDiCtmekDRcYc7NwoV44pDNr95MKwewPRoEka7KsoIi6ma49PysuvvU_njekXFMmnt1HfaxYGkycMySXPAXEmFGGj6AcIuvilRQfiuWsaa-hTqj-RtL-Bxi5J5VdsfZCefL2XuJPTsa7J-qIp_olYj1Ly2T4dYIA3Pe7aSQColUMvkFTaCOIGgJEuCr4em3MjQ_MVYhHtKI8IFj1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا برخی اتوبوس‌های تهران کولر ندارند؟
🔹
«اتوبوس بدون کولر در گرمای تهران زجرآور است و اگر کولر اتوبوس‌ها خراب باشد باید به شرکت واحد اخطار داده شود تا نسبت به تعمیر آن اقدام کند» این را مهدی چمران رئیس شورای شهر تهران می‌گوید.
🔹
طبق اعلام شرکت واحد اتوبوسرانی، تمامی اتوبوس‌های ملکی این شرکت مجهز به سیستم سرمایشی هستند و رانندگان موظف‌اند در زمان فعالیت، کولر را روشن کنند.
🔹
همچنین در صورت بروز هرگونه نقص فنی در سیستم تهویۀ مطبوع، اتوبوس برای انجام تعمیرات تخصصی از چرخۀ خدمت خارج می‌شود تا پس از رفع نقص، در کوتاه‌ترین زمان ممکن به خطوط بازگردد.
🔸
با این حال، مسئلۀ سرمایش در تمام ناوگان اتوبوسرانی یکسان نیست و بخشی از اتوبوس‌های تک‌کابین واگذارشده به بخش خصوصی اساساً فاقد سیستم سرمایشی هستند.
🔸
بر این اساس، در کنار تعمیر سیستم‌های سرمایشی موجود، باید وضعیت اتوبوس‌های فرسوده فاقد کولر نیز تعیین تکلیف، و نوسازی این بخش از ناوگان با جدیت بیشتری دنبال شود تا در فصل گرما، کیفیت خدمات حمل‌ونقل عمومی تحت تأثیر فرسودگی ناوگان قرار نگیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/454684" target="_blank">📅 03:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454683">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91518e29da.mp4?token=LBY68m3kJd9OQDjqu4Gd9Pxm4Wz-Y1Bff0BXN5AZLfCu6H6OuA-pB5K-byxxBlYJ4oyfqT1LqyBtQ2shRzDA5M75NytICVWHR0KoowLLawPAeq-YdeQ5a88mnPcss5FH8fdp3Kq_1lInSbB5GavYxWdStv239_kgiEk-PLnGOvJyrGYxkjdjzDfU1-OQf0KbETUi90OQSiHa5LFYmr6MgggUzRCvTREQRi8Ki0C7t5zPotqXC_KgY77vldK9T8FltE9c9Ck_7o9wJYXz5IUXqWrrSY3vKIwNarQhVkMUXyyvQ5Gy46zsUajp8G5Kmp-3-dbIAqCHX48_MO1wlwEu_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91518e29da.mp4?token=LBY68m3kJd9OQDjqu4Gd9Pxm4Wz-Y1Bff0BXN5AZLfCu6H6OuA-pB5K-byxxBlYJ4oyfqT1LqyBtQ2shRzDA5M75NytICVWHR0KoowLLawPAeq-YdeQ5a88mnPcss5FH8fdp3Kq_1lInSbB5GavYxWdStv239_kgiEk-PLnGOvJyrGYxkjdjzDfU1-OQf0KbETUi90OQSiHa5LFYmr6MgggUzRCvTREQRi8Ki0C7t5zPotqXC_KgY77vldK9T8FltE9c9Ck_7o9wJYXz5IUXqWrrSY3vKIwNarQhVkMUXyyvQ5Gy46zsUajp8G5Kmp-3-dbIAqCHX48_MO1wlwEu_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات رژیم صهیونیستی به جنوب لبنان
🔹
شبکۀ المیادین گزارش داد که چند منطقه در جنوب لبنان هدف حملات نظامیان صهیونیست قرار گرفته و این حملات همچنان ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/454683" target="_blank">📅 02:36 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454682">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHF4YAsHxA4-7BerpQQLYQr-uu66Eu_wr-Xp1UYY2KUYIyG1UW9cr1xqmQ6IiJcptPBMJEW9LwQTZvHMrWaOHFzPjpqu3PpUQ3KJockMQ9jpbbdadH6Lf03vbvQwus6_w8gQQOqO4JuE4yeCfb2F5bCmTMztVBFwm8TmI8zKE4SYocnyMpnPSmE6n4Jynprnq-HXUMOtuHoEIdNFYD1prn9hQcoFBmtHmw0x6wiBvz7fcCLun3EPfecho45nwkI5qO8QYZS601zs8M__pMOjUO_vAh7qi8H6Htyt6PUGth--JOstDeYHefXVOR9SpOL1cauEt_IFb-j7PN5DUZeYZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مربی خارجی از پرسپولیس دور شد
🔹
پیگیری‌های فارس از مسئولان باشگاه پرسپولیس نشان می‌دهد که احتمال منتفی شدن جذب مربی خارجی بیش از هر زمان دیگری مطرح است؛ و در صورت رخ ندادن اتفاقی غیرمنتظره، کادرفنی پرسپولیس در ادامۀ فصل با همین نفرات فعلی به فعالیت خود ادامه خواهد داد.
🔹
به این ترتیب، به نظر می‌رسد درخواست ابتدایی تارتار برای اضافه شدن یک مربی خارجی به کادرفنی، حداقل در مقطع فعلی، عملی نخواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/454682" target="_blank">📅 01:46 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454681">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">یورش شهرک‌نشینان صهیونیست به فلسطینی‌ها در کرانۀ باختری
🔹
منابع محلی از یورش وحشیانۀ شهرک‌نشینان صهیونیست به روستاهای فلسطینیان در کرانۀ باختری خبر دادند. در این حملات حداقل ۸ نفر زخمی شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/454681" target="_blank">📅 01:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454680">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">رویترز: ایران به کشورهای عربی هشدار داد
🔹
خبرگزاری انگلیسی به نقل از منابع بی‌نام ادعا کرد که ایران به کشورهای حاشیۀ خلیج‌فارس هشدار داده، حملات احتمالی آمریکا را با حمله به زیرساخت‌های انرژی آن‌ها تلافی خواهد کرد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/454680" target="_blank">📅 01:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454677">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uyF93s09EM0F7UGKlOe9BNcUtYpwCtCs0hjM9UKeolRcQKqbUiVi7QNyomRWN8n8IM_yJ_hZS9hFNsa_Gk-4_Y_S1pQvPKa6t9tBZw1j-mzUjxsEAT90kuFyU6Np02qER0wAnxfN9JQXbP8UkWuHfzJjFqFytgpAMc-pZhTMAfofUKrELpQMqoMO9LaAx_mAJklwvqawdSq5CI7KzFTRiGAjY1_iWOpHucNVQDK5XZr1pahT5fddTzxhEe_YVukneRPrbhOOOehLAcAAYCQ8qfT-3ssjV5FehVU65i-uoG0lpH9Sqtj7gFG3jcgRo9m9e0FyvPc_Q_bG_GFffQKWRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JXbll2jkcbCk73XHvSv9a45QhSaNhBdT5CndaeDhWGNdWm49xdnsyhNS2XPaP2ogXEBAC5tro98oUMeeTW67MDJ-csTWag1vdZfYu0BYIdLym5_SqwiDORAV94Vd5sydsmXVtrTxVgokA6EisIM9epPj0nxw1VvWud-4QuhWz4ZgBlJpsv29w1y6GmEm6BnxkwKiIjDkMRtOJTRSubf7JbiE4w6Gn5mRGRiWBF-ZfoeaLXPZYc2VkDRWSfz29seem0kN_KAPYzumvo5y7b53I9PA1K3qNC-bqjPuHld7oF08tSKtk9ay9mI-npv9zDQwNMyRux0tp7WmQnI-muphGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sJD7r8-tCN0_ahmPWVMO02EBnGE5mfYBdWK_Oy85hHPmRlvM-ec9xqCuXM3qhheadDya4CHuuoZGPegspNI4BczualZ310ekupABsRPD0JPkcoOtpkIzi3bwRcuLLoCh0bqxlTWfQcGjffj10_02NkZyvs1zWrVEb-qKvfzgxQSxaoRH0tTsG_n_ketdcK4cMOjh-xJ8led6ZomjB885xU_sQ5ZnV0JD0ANJPZ_qltZgzbHmbUsGVCrUXbk2A_P1C7ulEQnTmywDA_w0vcvmJgvCxoWYVRf42ct1R_b7sXNltUbu5pR5nHtnaE7vbEdLFoiCBQk-b3xa9y9pfN184w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | پنج‌شنبه ۱۵ مرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/454677" target="_blank">📅 01:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454667">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q1areJrTpwE6is7MbrKoLXua43zCZiN1Bu1_gbznOfsPLmy1CPoIxY91NuFzkgtniJ7u7qfg61v71GkzQZgl70WE_hMSQ-gC2Yr2HX52DIzs1vigDJAUTir6DpOMhx8xlYBy9vmyrn5kUTmMtlULYaSrTz5t-v6h-j7ol693llX4dzYxd8D1O5hgFhUUCjeksXmu1FIPNoSk-6iD-d2PfXpvAgcfOcGiEIucImNzJLVRGahFnh4Q1UCuVBS3bBtzguo_cHkBFSTq5HGWJEA8GLfQT8HAdN4V0CEcTqMDvEARuzwe3Za7x_kJBgnjJmU5brTQcTIrM8a4eYtUzvKSkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VxTDIyFDQ2NNIKkUJx_jMCPugoxw-NLSxzR45T9yp7DHW_p5Ifq2-dLXNYm1E-b669XB-632YY5yDY0ZtTzpuDwfXKVVbSthwOOu8XVglqtiZ4Tp89ZYBQemtN-6AOVUBTvX8Ig06CATqDprPAdTwUA33dDUJyGlBKhqOkO3TW2Ngl5kNs3UFjznwRxALphXyV1cJvzfCz2pGTbbouI08XW66cbiKWcyIyZSDNCQ8Lelapyi5MIbYliPTWkeRK8pLrh16LXXAfSolZTAIe9sxCkUALCrANQFrnH8rA5DHFoWVhKyWdUltcaWD06UTgbos2LbUD2FPoOhAPZrT5mUTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ck2qBhgJbHH2oi0b4IBDVc0iKoCOaOZsnsdCZFM9OSJoe0BwOjAWWNCSlx60tt6vg9E70ZFClOCadnhjStaUH1tPpohyM2448xFmlUBHRLnwapgqodQ6gRk7wApiufVhcoMlDc9zMIVwwlTpRASAnLvXGNg5cfyRkrKMFoUMeqNWKw9RPaQDwB_T-V7Ze0tFzzQ0JEWXpgJQNT8_hOX8Y_NaKhAPno5xfNdYSetQfZlpzD1m4tahDVOuzQD0mlOpOIPZtPY5GqRYRkcmeyLFPTNOg5a955w_7Ks7sm4-FrEIdr0qel9kXkesE9f878vlviYVzss8V2HKeAc_BTWuQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t2ztaWL3wt_4WOeezLPVRgxSUfjvEDGgnmsUTcewdyrb_Nx_48NQqUFt-GUVoHHDM6vubzSMTIrCKC4DIeljvutNofzymrylezJiYPTYuLp1weSw8nY9LRE7RqBdfJR_tIr_j4eQZbPvzJPZt3dYyM-R-8oDQOMwwBVF6AsnohjT0-A6KtGX_LCLVzdYHiIDaeuQs924wLqEKo0njs2nYG5aSvA1X_VsjWD23abeawY2z3M2ta7VEYHFXNKsYY528Vkz29nnhm400THowulFnnHSGa7_DK1QYDJrTSjQMZAMxRxU1Mb52qPNPko4Fntcqsw5UNRzfOFNUGK2X4z0mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Al3rN4Ds-HTwDxnLQ6U6WPfkMUsQ3x9XhXOlvmJkZumt-t4Ol8gq-sVGOuWZIVwjudUiVQ5Q2uLWsya_pImI_WaPFFNtk9TKlQhRdwoHeYAMhxGoMXVGc31UCpqOSemPElUcJ6pVP5KrJVO5m3YSvb-_vUELpwJSufoZfcamTcpESomqvFmVG4yRvfczyDwXh1d9JJDGVGH8xOjuR5h8p5lSR40YSdVlfNix1TUjXVPuBXdTdSexZmK9cVnBWrg0mlBXtY_8BihBt9BSb5gQT4hh6onFJYuM9gJ35OyEOSVq6IS4mwsAnu-TGzGgPwTRvs460FgWTuEa8jWuWQ38Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T2nVUdS6mnBsDCdV9Pr5AYzj72mhsaPHgJBPyEsyScdvMkOz3mPI4h1YJtmjgV1GN0KscSEIpj1P3moGhH3kClP1wJUOGXlBWtJslF3-plCEV8bDG3Gf29HJ-ouHBBG9-X-CkIJlnglm17V4U-e697tYGXFLWD7oCHSi8aAsDDxk2PbZYa9q5I2T9i5EBcCaoKPI0KU7R4H1HcsD3H_ZhBSIOlZT3ImYaHPhuNkeH42UdKB8LMcBT37_VMyFMfQ8m9UyUBtRxM1e7hux_vm592vb94N0VedmFwqy6Cj1yHdbZsHgnFrSmnDcrz4IWOJuMkCwaCTxIiOi_QWtY2Q37Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ReaHoHmYCtiwFA0h6jTvXLq0t9k9dhQASmVfPwFH-qtYaa-4SpRsIlkku6inStBxbvw6aAbATtoiQSavEjMj5lGWyGDLpYuzsZW1_cRk9jIsXcMgMgdOSfmqLSzicofS4xvg93zoPwLQ-thEufHOOwvo3m60NR9-Rg_SwM5HNzaL-HwR2iW3qYL4roDoN_QEukg7ZIgivdby9NU-PRCDCY4A6TXLqSk68ZHpSbrX9OsQZSb-xyiHHRkRjBHaUeJ2Mv5iTumpSTfM1RuD5WYCl1Gf7tqKSl1rM-LyXgJLnT5EFAwT9Wp8I7kZ4Xa_9xBR6FO7ipu5IRq7IOQg-oElQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CyV5q1ay3b0lh9kUtH9gs4H8-ygCBvrxTGL3C7VeOo3W81fXPy1QRuvTT9JFiTDmCXS_3mGC6aAGT6jknByeNy8DBNCxoCQRrSSkxXLWSNxiY4Te6FVb94yvIAKvzUVKlZ79IbHTvXZfGWpOxYdXMoOQH0-hml_kXdfLVyI6nS71o2NKxY0v6MC-r0O1nSy1iCKddGvlpluKtzDJxBtQHgsXO0eIVWpVs1TWlFtLb9cfYGvSbCIXC7wsj3VT3iD2NVp53VNRNukHH4QChF6cZC94sMRX8Mtnznwe_ALVEowL6ES_9KEOgn5JVMBvbihQ0nURPT0bHsOsi8ovSB6Rgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TZDe8EIOjiCOwRFKjrEbiofW_dmDahnBD6K5W7hXewru89gMyRio6j4QY16X499t3kwvs-fepU6Iwohwv9N-0Yu48QjyhNwZBaXFQ8Az_4QPRSdrfwTrhyDICoiq9VfpxKHDt_mh_3npcNhMvUQXw9zmtPGSDlvVIdVMwaSwWfOjpOni_BnCHsmhG-NVkwvH7PUtdWvo-23DLJ2RN2D8Fm2D709gRi1MGrtGmRygCIRsCZ90po9Fd2DrlAzG7vZh6as5YRT4-cQDk2P2JA2VEkwG_NZRiSIy4YTLAejWKjpag3vF-WZwyuH_LrKyrxv3EBgRxgaimvat74h0fO1Fwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PMi4jvtRocYQmro4CQR-TvNylTCqrNKPV2LVhjTCoLo2g3Y8GLmOB9if5g-ZP61GMaU3XFtXbl31rJUiD8MwO1lIwHw7Yv7bktIRfFyayHOv11aK6xtXE3jZDMZ6PkUcYBCLW7ILOfvfMpsdBp0XYmMSv7AzZ4Cj78nQXMZDiuGgEQQaQdMZlr6gyug2WHqBnHxDejkVNRnQ7PnNMBCFS4Y8bEZP9pGcPEev-qLbJMCYlBsSf1iwrgtSGpxVeBQEgoa4i5Uc8LnidEKRw5kMW8P59C6kG9yODuOvFps1eWnxdp6n5Y2lQL1UxTmqgc3X2O3jq1Ap1v4rxiI4ejtsDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/454667" target="_blank">📅 01:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454666">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">دادگاه سوئیسی استقلال را ناامید کرد
پنجره پلمب شد
🔹
باشگاه استقلال در بیانیه‌ای به‌صورت رسمی اعلام کرد که تلاش‌هایش برای بازکردن پنجرۀ نقل‌وانتقالاتی این تیم موفقیت‌آمیز نبوده. این یعنی استقلال در پنجرۀ تابستانی نمی‌تواند بازیکنی را به خدمت بگیرد و باید با داشته‌هایش از فصل پیش در لیگ برتر و لیگ نخبگان آسیا به میدان برود. آبی‌پوشان در این پنجره دست‌کم ۹ بازیکن از فصل پیش را از دست داده‌اند و نتوانسته‌اند کسی را هم به خدمت بگیرند.
🔹
فسخ یک‌طرفه قرارداد منتظر محمد توسط استقلال، بعداً به شکایت او در فیفا منجر شد و فیفا هم باتوجه‌به این فسخ و سابقه فسخ‌های مشابه، باشگاه را با محرومیت از دو پنجره نقل‌وانتقالاتی روبه‌رو کرد. مدیران باشگاه استقلال با استخدام یک وکیل ایتالیایی تلاش کردند تا پنجرۀ این تیم را از طریق شکایت به دادگاه حکمیت ورزش CAS باز کنند.
🔹
حالا مدیران باشگاه گفته‌اند که در این کار ناکام بوده‌اند. تاجرنیا، سرپرست مدیرعاملی در توییتی عصر چهارشنبه گفته به‌ دلیل «کوتاهی قبلی» چنین اتفاقی رخ‌داده و توپ را به زمین مدیران عامل پیشین انداخته. وی حالا وعده داده که از بازیکنان آکادمی در ترکیب تیم اصلی بیشتر استفاده خواهند کرد.
@Sportfars</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/454666" target="_blank">📅 00:56 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454665">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojoJOsqJo88HDEiLlITVDnT8cgYBNqqQQxoTurS1shLlSJeqILVRkN8Fbruy1gV1bRheVu34R0R7a_aoOI36K_PFP4twAKp2RmQHnlr-E3Ibwf5y0IJbvUe1zNKo1Hd3S04rO1sAXKwNkZB9hYSO3LlwRumXSiV9zqFfxTgtuNdG3ZY7p_pWENTowxDNU65NhAEz53OAq5_N1erfXl2YcuQ18VE_GbOuxhoX-F-4GNfPW14byqe8fy9F8DFA1uzn5m7GYP2pj081HRy8bI_KUNCusvjuDiGfeAA3Tjv5s9gjduKizOhuEXdI8AxLf9SCVy4HBQLt0a_-YYXRFdSffQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمایت تسلیحاتی اسرائیل از امارات، این بار با ارسال پهپاد
🔹
بر اساس اطلاعات افشا شده، در سال ۲۰۲۱ جلسه‌ای بین مدیرعامل شرکت «البیت سیستمز» بزرگترین تولیدکنندهٔ تسلیحات اسرائیل، و رئیس دفتر سیاسی-امنیتی وزارت جنگ اسرائیل برگزار شده و در آن فروش احتمالی سامانه‌های تسلیحاتی مختلف به چندین کشور از جمله قطر، عربستان سعودی، اتیوپی، رواندا و ترکیه مورد گفت‌وگو قرار گرفته است.
🔹
بر اساس این سند، به البیت مجوز فروش پهپاد هرمس ۹۰۰ و همچنین مهمات سرگردان «اسکای‌استرایکر» با بُرد محدود ۶۰ کیلومتری به امارات داده شده بود.
🔹
همچنین در این دیدار در مورد فروش احتمالی بمب‌ها و مهمات یک‌تنی طراحی‌شده برای نفوذ به پناهگاه‌ها و سازه‌های مستحکم  نیز بحث شده است.
🔹
بر اساس این گزارش، شرکت‌های تسلیحاتی صهیونیستی با افتتاح دفاتر محلی، سرمایه‌گذاری‌های مشترکی را با شرکت‌های دفاعی امارات شروع کرده و فروش تسلیحات اسرائیلی به امارات همچنان در حال افزایش است.
🔸
به گفتهٔ هاآرتص، برنامهٔ فروش پهپاد به امارات بخشی از معاملات بزرگ بین تولیدکنندگان تسلیحات اسرائیل و کشورهای امضاکنندهٔ توافقنامهٔ ابراهیم است که به‌ندرت به‌طور رسمی افشا می‌شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/454665" target="_blank">📅 00:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454664">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhrd1xm8EYTUIm-TvQyqW_uC31Jq4WEUF_HL3agBdgIkY0389Os7PVrNl_VES_BXunzcZ4hnmeX27c6O3GL-CVWq1D5gwn2_ovc-_3-uMlerX1UCUafxYblXA-5_doRTv4wzkgZun17JhS7tpTcJqbmgtkHDLGNy4dT7qOuE2khXo7v5mR031SRUyrixDGtQSagW-tUQo5QhHZarIIK2hHei7YEXkYsSf8QUaiNwQIBPwfGEWQeraT-FQB7dO7bBZIlfJyeqN7X5oaTz8UstpUViRSvzDrJdcVX6POuW1cNzpHhiD-09gfjXo13nBdBTlVAmpzsr7PpiXRmH9sdOMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرارگاه حمل‌ونقل اربعین: در این موج از بازگشت زائران اربعین، هر ۴۰ ثانیه یک اتوبوس از پایانۀ شهید رئیسی مرز مهران خارج می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/454664" target="_blank">📅 00:19 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454663">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e352bba80.mp4?token=G8QG-jCVs-KkmvZYsnph5pyCsU7BOtBBBO4x2I6Bp1-yGXzaBBFmmVEj1q1I-wl920sAFAt4HXmOIiFYOd4I9EVoLiY5uTjV-Anx2CpBBfHxgw0osVbZ5LJpnsDW6KJvbNUr3Iw2njn59C5vRU0C7gAc09kkv_zZPkBnQPj9OP53HO2cfF4Dj_ai_PwQwxzBpqQdNuY2fa98nkH545KBSb-HfbdIXCYDIUxVFqEDit3zemlKfkavYTsGn3KjFFr7BOdFayUiFKCIHN78agcRereNZoquuQiKWtXjFLb40lBm-00Ud-hdR2hHiL4MJ6BlikHEBRSlBpXAe14R22hVzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e352bba80.mp4?token=G8QG-jCVs-KkmvZYsnph5pyCsU7BOtBBBO4x2I6Bp1-yGXzaBBFmmVEj1q1I-wl920sAFAt4HXmOIiFYOd4I9EVoLiY5uTjV-Anx2CpBBfHxgw0osVbZ5LJpnsDW6KJvbNUr3Iw2njn59C5vRU0C7gAc09kkv_zZPkBnQPj9OP53HO2cfF4Dj_ai_PwQwxzBpqQdNuY2fa98nkH545KBSb-HfbdIXCYDIUxVFqEDit3zemlKfkavYTsGn3KjFFr7BOdFayUiFKCIHN78agcRereNZoquuQiKWtXjFLb40lBm-00Ud-hdR2hHiL4MJ6BlikHEBRSlBpXAe14R22hVzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوحه‌خوانی مهدی سلحشور در تجمع امشب مردم رودان هرمزگان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/454663" target="_blank">📅 23:52 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454662">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95ffb726b8.mp4?token=QFvYjDarGPtNqhgS0vHqbBIWumObXBE5-R_cYk_uDD-sKGTqxhOkQCLF02nMqUv8aAMGh6nJo_zUOIQWDJ3XMtPRl_UOyRo3ykL-Uc0Ql5PccJad7p0MQceoJD1iRmVD023qOQj0c0qFDH2E038Mh8GmcdKPjmtnW6YyQ0kJRK6L7ujaJmNMkz5xpOqwo-e_I6iqYMw2bQkghxvNb9xiFffTIP1_TZL8vS4ZdGz2Pc24RM_iaBdfmRTRY61CVmWuPM-n4YepUzgcNLbCRRHNHPsQ0-T6rZUOS4LqeEq-lYeYPyJujQtsrnEBU_dKfACHpjrtZRSpIpiBo9WFa-EEIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95ffb726b8.mp4?token=QFvYjDarGPtNqhgS0vHqbBIWumObXBE5-R_cYk_uDD-sKGTqxhOkQCLF02nMqUv8aAMGh6nJo_zUOIQWDJ3XMtPRl_UOyRo3ykL-Uc0Ql5PccJad7p0MQceoJD1iRmVD023qOQj0c0qFDH2E038Mh8GmcdKPjmtnW6YyQ0kJRK6L7ujaJmNMkz5xpOqwo-e_I6iqYMw2bQkghxvNb9xiFffTIP1_TZL8vS4ZdGz2Pc24RM_iaBdfmRTRY61CVmWuPM-n4YepUzgcNLbCRRHNHPsQ0-T6rZUOS4LqeEq-lYeYPyJujQtsrnEBU_dKfACHpjrtZRSpIpiBo9WFa-EEIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مشاهدات بلاگر روس از مهمان‌نوازی و صحنه‌هایی متفاوت اربعین امسال
🔹
جمعیت کثیری امسال با پرچم قرمز آمده‌اند، برای آن‌که نشان بدهند مصمم هستند تا انتقام خون مرجع دینی و رهبر عالی‌قدرشان را بگیرند.
@Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/454662" target="_blank">📅 23:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454661">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aG6L_qbn7lsoyjPuzAB8eu5UJV59G_nXpWmT6YLk3rFl3y1kVbprs4qNAWhnZb-UWZBFPJDs2nT9LTPETwVgwSEOnROrVkTJiwvZf9eyGcgdz-fLIvgc-_U8_AOfEftVxviLz74CQ4AWQpB4mio6TQ8KKchrhC0Vhxcq29TyJtn-C2tmrjPC52zqdXefJhZBVVp_6JiVXAgX9YMVDbrw8vmA1YokCW8kXgSnxTXB5X_NM0zaJYKuTsUAsA1TemynD6VrvyBlt7yQZNEvRI2zHRj1gmvn8dMOg_iF6d0CBV-ZqJKyz2PL563lOtbRPk26LtPq9ABZVPeySUbaa3ztuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
رهبر معظم انقلاب: از اصولی‌ترین امور، اصرار بر اتحاد مقدّس در همه‌ی سطوح است؛ پرهیز از تفرقه و تنازع وظیفۀ همگانی است
🔹
لازم است به شما مردم باوفا و سرافراز ایران عرض شود که از جمله اصولی‌ترین امور در این برهه، اصرار بر وحدت کلمه و اتحاد مقدّس در همه‌ی…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/454661" target="_blank">📅 23:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454660">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqbkPxbiX5BD4SZwKVsn-qsS0r5-T9SOl9KarVk91lMXnLNUy5BGvUokQdtyAdxXRsCGzTVCHsDICsMlr3QoJGKK6_3_Co27IMqrDfgYjUkeTIzaH0c9dran40EQjzskyjSn3FEVh6uHHc9_5M4J8jLD2pTIezj0aTl0qfZe6-UbCK5Ng6p5mdEDAIz1HwisYlR5w8Y6Vg0vpjm057aEijSPtHrf4P6cx_qo_Pt_Nk9MTSHsA61ln0RGrMm7WX-mN6LVywHdYeW_yUhCVsLjUp83M-1v_qZowLeC15WCWZZFoBO1u5uK50w9eLPppk3zlP_6hpHHbjtIt32YgmsU5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
عضو هیئت‌رئیسه فدراسیون در پرسپولیس پست گرفت
🗣
با اعلام باشگاه پرسپولیس، محمدرحمان سالاری، عضو هیئت‌رئیسه فدراسیون به‌عنوان مشاور حدادی، مدیرعامل سرخپوشان منصوب شد.
@Sportfars</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/454660" target="_blank">📅 23:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454658">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egQCZz6VnEKbNknMV3FZW9dPc19wtMXTzf7OclDZqnFn9D1z-DovnY2fO62bFd9neIIsrFI7VpPfB6U5HEy6krujMHYbJPwJncO8XR7cn5zOI2C9eJDH4bdPvDLH4AjZC2ZXk-yC2tUI1Pu29np2vJt2ttfGjjOetVmap08BtQe1C2ETO7Ed3D2rrD4-vPM80_z9rPZQ7pVFjZpGitqrWsjBe_afXxrrXLmMePqKjWBNpY3Y7zUP-wIKUh56KQlJ3UUJTtuoOEedTlloBIvlYzL5tsKiYY7ntxzDIWDLHbtTo02iYSCLUJ2ZneYzPNUYHX9N9H5s11ToCidx6V-sFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام مستعفی دولت ترامپ: آمریکایی‌ها از هر ۲ حزب کشور خسته شده‌اند
🔹
جو کنت، دبیر سابق مرکز مبارزه با تروریسم آمریکا: اکثر آمریکایی‌ها چیزی دربارۀ غزه یا تنگۀ هرمز نمی‌دانند؛ آن‌ها فقط می‌دانند میلیاردها دلار از پول‌هایشان به خارج می‌رود و سربازهایمان کشته می‌شوند.
🔹
یک اجماع روبه‌رشد از افرادی وجود دارد که از هر ۲ حزب جمهوری‌خواه و دموکرات در حاکمیت آمریکا خسته شده‌اند؛ آن‌ها می‌خواهند ما از این جنگ‌های احمقانه‌ خارج شویم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/454658" target="_blank">📅 22:58 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454657">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUw6yCOWOFkvQncAI7mO_remjSsfPnCOnyxRWT41a1KmrWVclsn-pBV7qUD7TsIjADx3H0f2h0BepA3JS9TMHo0Wx1Z0EfIHp0YRNozzfDBATQNUbSSTsf-GwcJacoEGIXQN3Qwisx0HTJQKHwNd-6qEzhQsl9dPwxtis7OAWZURdlPaRWxeWynkVJgRyuqT-CDmfw50eDMDqfb2dGhG0Yev688hJRmQMynUIPlGuW-ZY9lePB9MD4j6otykd_4OOCRJiBB5C9BNhSQHTax1M-w9J0ZbZyKnh4jMm_hmSAsJe00SKr8pWubbDcIKFj9sTRP7HOIQUmFybQvCwuq6KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ایرانی‌ها چقدر از هوش مصنوعی استفاده می‌کنند؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/454657" target="_blank">📅 22:52 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454654">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b22d6fe91f.mp4?token=ixuf01VJY23syjIFg86Msh_OrPTzY3fOykqf7qda_lyJjwmJF_RXG00KTqW8tB1WVBINXpggA_PoYQ-SiaVpZEHFOAS-q76-xt5iFJ6EwsdMO3ATRiqO1wOWKJ-ntoWKh4dGvUNewIGU2Dd8a8ZamV5bBdNK5ix8YhYzVvNrLhf5GJjcsRTDlnSlmB_UYjeFArhxUFmf-lQ24ULx4dFRlDz1DmVq7z5CzogoZc6gI8jGXINzmsCGL4W12IpFdbTD97wmSqHnAwfiAMsBlWGGJNOjo7dPFoJ9VZ-_4rr869tnaZmZVwtOg5Kt6M8uyO3O79dqcL6lZ2SYafSbZAQLBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b22d6fe91f.mp4?token=ixuf01VJY23syjIFg86Msh_OrPTzY3fOykqf7qda_lyJjwmJF_RXG00KTqW8tB1WVBINXpggA_PoYQ-SiaVpZEHFOAS-q76-xt5iFJ6EwsdMO3ATRiqO1wOWKJ-ntoWKh4dGvUNewIGU2Dd8a8ZamV5bBdNK5ix8YhYzVvNrLhf5GJjcsRTDlnSlmB_UYjeFArhxUFmf-lQ24ULx4dFRlDz1DmVq7z5CzogoZc6gI8jGXINzmsCGL4W12IpFdbTD97wmSqHnAwfiAMsBlWGGJNOjo7dPFoJ9VZ-_4rr869tnaZmZVwtOg5Kt6M8uyO3O79dqcL6lZ2SYafSbZAQLBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور مردم بجنورد در موج ۱۵۸ اجتماعات شبانه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/454654" target="_blank">📅 22:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454653">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">تیراندازی مرگبار در آمریکا
🔹
فاکس‌نیوز روز چهارشنبه از تیراندازی در کارولینای شمالی خبر داد.
🔹
چندین نفر در تیراندازی جمعی در پراسپکت هیل کارولینای شمالی کشته شده‌اند و دست‌کم یک نفر نیز مجروح و به بیمارستان منتقل شده است.
🔸
پلیس محلی اعلام کرد که این تیراندازی حوالی ساعت ۸ صبح به وقت محلی رخ داده و تحقیقات درباره آن آغاز شده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/454653" target="_blank">📅 22:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454652">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49c34903d7.mp4?token=Z3z6V5cUA1bKVnVOaQeiMh4T9PSPSg6KQlyZyUi1-J0eGSVs7-BQBnQPjV0y9M3GIfXLDBV1XYunWCdu4k6OobXSSpT73lwb2V14CbMW8WFfUQ0kJDxmjdoxjXwUoi8z0JDwiQYhWdjE3sRadoeT8lDZ5aHKtc9t-uUNZTI3qg0yLERbWUH_bMlPylPzwk4E8q4FdjtYrY2D1YtQPcMWRIHy95iPI6jEClz6Bij4eNR8ye9_kR0sYmjTj5EOe4LVQv3ILNxM6kTqW8MaUGC5kCKz8dPo_OcJi8gBiVkduD6XEg3j6JXqj7waaH9b0Zgl4PBiLa-YBKg_S8YBVf47bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49c34903d7.mp4?token=Z3z6V5cUA1bKVnVOaQeiMh4T9PSPSg6KQlyZyUi1-J0eGSVs7-BQBnQPjV0y9M3GIfXLDBV1XYunWCdu4k6OobXSSpT73lwb2V14CbMW8WFfUQ0kJDxmjdoxjXwUoi8z0JDwiQYhWdjE3sRadoeT8lDZ5aHKtc9t-uUNZTI3qg0yLERbWUH_bMlPylPzwk4E8q4FdjtYrY2D1YtQPcMWRIHy95iPI6jEClz6Bij4eNR8ye9_kR0sYmjTj5EOe4LVQv3ILNxM6kTqW8MaUGC5kCKz8dPo_OcJi8gBiVkduD6XEg3j6JXqj7waaH9b0Zgl4PBiLa-YBKg_S8YBVf47bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: حوادث دی‌ماه پارسال قابل فراموشی نیست؛ کسانی‌که کشته‌شدگان را ۳۰-۴۰ هزار نفر اعلام می‌کنند، نامرد و وطن‌فروش هستند.  @Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/454652" target="_blank">📅 22:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454651">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc659092fa.mp4?token=R_w9Bi0vilROgZK2LQVdUywmfN5ermQHx48uE8QK0IVzgKMjO1g0RkcMRBYZbOFOxD38ZA4u1N0_2pe-EXwY9-Rg0xApW8jEEp1Y45zgynQSr0CKC1NhINgLL6qRu1pWBDb9OvsN3N2lTjV7j-gNZ9lRvjZ7A0D01ljr6Q6UhBIeXxgrU-ruQmHhpbnZypZnaYjzeRPG4QOurJmo1DCRhPLhAn4cSOAYKj5BiOpUCfIFL63KIzjkFe5QcsTrkXKmfOFHH4tpndGjRtt2IkIUnONEFDEsnBlTg-YpCB-ncTP5Tba27HzYkpIW2H5_L1iJ1gWlTp74PIlLmnEH5wdh0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc659092fa.mp4?token=R_w9Bi0vilROgZK2LQVdUywmfN5ermQHx48uE8QK0IVzgKMjO1g0RkcMRBYZbOFOxD38ZA4u1N0_2pe-EXwY9-Rg0xApW8jEEp1Y45zgynQSr0CKC1NhINgLL6qRu1pWBDb9OvsN3N2lTjV7j-gNZ9lRvjZ7A0D01ljr6Q6UhBIeXxgrU-ruQmHhpbnZypZnaYjzeRPG4QOurJmo1DCRhPLhAn4cSOAYKj5BiOpUCfIFL63KIzjkFe5QcsTrkXKmfOFHH4tpndGjRtt2IkIUnONEFDEsnBlTg-YpCB-ncTP5Tba27HzYkpIW2H5_L1iJ1gWlTp74PIlLmnEH5wdh0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: بسیاری از فرماندهان و دانشمندان شهید ما هیچ دارایی و اموال خاصی نداشتند  @Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/454651" target="_blank">📅 22:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454650">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfa5a47592.mp4?token=uMqyhvypHC-9PQqmrpasF6uIQQ-_oXca-mQa7rOFIF6ZRsYTWtmCOauqsuye3UQ56QtpFxTq3g0Znb9bbfDJKCqKDQZ4ZG2DQGnKs18oRTTx-H1_Er4C_5wjKeslRm2i_yhHTb7LfTSUNLHafhLtLR88uMsRifQeXuhEINt_PBtcrntAzIoQ2Jx8COhqMzFmCi5KhDhSxezIkq0FzQufKSd1LbvLLS3ozoKo8vZbFjDxwpVQOU-WfYsqe0n-TDraWZSHPVaawWrGHYcXRa0YCrivWxqhOlQ-mlyMVKjt4Gl5rQAAl5SlxDzJBmeV74g1IkUaDdK3M5KJzZ6pqWxx8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfa5a47592.mp4?token=uMqyhvypHC-9PQqmrpasF6uIQQ-_oXca-mQa7rOFIF6ZRsYTWtmCOauqsuye3UQ56QtpFxTq3g0Znb9bbfDJKCqKDQZ4ZG2DQGnKs18oRTTx-H1_Er4C_5wjKeslRm2i_yhHTb7LfTSUNLHafhLtLR88uMsRifQeXuhEINt_PBtcrntAzIoQ2Jx8COhqMzFmCi5KhDhSxezIkq0FzQufKSd1LbvLLS3ozoKo8vZbFjDxwpVQOU-WfYsqe0n-TDraWZSHPVaawWrGHYcXRa0YCrivWxqhOlQ-mlyMVKjt4Gl5rQAAl5SlxDzJBmeV74g1IkUaDdK3M5KJzZ6pqWxx8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: من در مورد بازگشت ایرانیان خارج از کشور با رهبر شهید صحبت کرده بودم که ایشان دستور بدهند که هر ایرانی خواست وارد کشور شود برای او مشکلی ایجاد نشود و اگر مشکلی وجود داشت از اول بگوییم نیا و اگر آمد به او بگوییم برگرد وگرنه بازداشت می‌شوی.  @Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/454650" target="_blank">📅 22:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454649">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c6223c099.mp4?token=nCEDmXD878HlGEuht05nsuaFb-qqacrA_w7cMDFXyQmUWU2405DWlQpXV9nCNpTU-5Z-Obzavdvxj9vMHYu6LqACkW022ht1Kw7P4N_I3NJ3wNsQNC2vwb2WmaVMKLYfeKUmypzxrEVzOyeM8ALNLXKEnrlukO7nlLGlL92iWjUCBQvGxdWdjA8T7pLRmUd3GNCy9BUJF-kZr6zzC6YqcKkXb392pkg8IQL3Exz5zGKktBgFrPQVx4--fTxU-lxczTKWFGQcy2t5Vctz32EjV36aphMsNzzzhwZbqlQk03VvaHi85FyUbWX99kZRJXlxpmEJwPbaNLs94ydXHsBFXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c6223c099.mp4?token=nCEDmXD878HlGEuht05nsuaFb-qqacrA_w7cMDFXyQmUWU2405DWlQpXV9nCNpTU-5Z-Obzavdvxj9vMHYu6LqACkW022ht1Kw7P4N_I3NJ3wNsQNC2vwb2WmaVMKLYfeKUmypzxrEVzOyeM8ALNLXKEnrlukO7nlLGlL92iWjUCBQvGxdWdjA8T7pLRmUd3GNCy9BUJF-kZr6zzC6YqcKkXb392pkg8IQL3Exz5zGKktBgFrPQVx4--fTxU-lxczTKWFGQcy2t5Vctz32EjV36aphMsNzzzhwZbqlQk03VvaHi85FyUbWX99kZRJXlxpmEJwPbaNLs94ydXHsBFXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: من در مورد بازگشت ایرانیان خارج از کشور با رهبر شهید صحبت کرده بودم که ایشان دستور بدهند که هر ایرانی خواست وارد کشور شود برای او مشکلی ایجاد نشود و اگر مشکلی وجود داشت از اول بگوییم نیا و اگر آمد به او بگوییم برگرد وگرنه بازداشت می‌شوی.  @Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/454649" target="_blank">📅 22:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454648">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b08b848d71.mp4?token=EXe0LwFTSVpFbhV6e4IUSiamYTKVAfO_T28SwFz2gjkuFIVpBiqKzeOjX3UkMwa-rCed4DM5iSW2bwG2uYCb_O77n64DOQUnmW6ado9STzPyV8NlqtB5aKh_f42-mORV_k6-3s7CQ4VP-zrtEhpPAMpsavQDaui-epMTC8kcoT9D9pP2iMZsq973XeG4wbUe4Dw6GYmaXcMXLQUuwZkgQdMhygHKvGgqB3m90c4ZVAmr26OsDjKvOKrbXJzL9PzxVp9Fa8KMXUJVrCvSTAgk_eqGikQnvef7zWmg7FwmhX-MhB_HdEpG1Ss2qbVZZtK9SS5usnWlEEyCQUr6I7vBjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b08b848d71.mp4?token=EXe0LwFTSVpFbhV6e4IUSiamYTKVAfO_T28SwFz2gjkuFIVpBiqKzeOjX3UkMwa-rCed4DM5iSW2bwG2uYCb_O77n64DOQUnmW6ado9STzPyV8NlqtB5aKh_f42-mORV_k6-3s7CQ4VP-zrtEhpPAMpsavQDaui-epMTC8kcoT9D9pP2iMZsq973XeG4wbUe4Dw6GYmaXcMXLQUuwZkgQdMhygHKvGgqB3m90c4ZVAmr26OsDjKvOKrbXJzL9PzxVp9Fa8KMXUJVrCvSTAgk_eqGikQnvef7zWmg7FwmhX-MhB_HdEpG1Ss2qbVZZtK9SS5usnWlEEyCQUr6I7vBjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان: همۀ ذهنیت من دربارۀ حقوق بشر و نهادهای بین‌المللی فروریخته است
🔹
به چه جرمی رهبر و فرماندهان و کودکان ما را شهید کردند؟
🔹
دشمن با هرچه باعث رشد ما شود مشکل دارد. @Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/454648" target="_blank">📅 22:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454647">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11ec7e1eee.mp4?token=uGGvLMeBvaOopvn85eET2GFYY7sOtpv1LOIy-oUitcc8ZEqxZh0H6BnscRy4tjaZnz3KNcFrnplI3Ov3-FfCaX7DYU8JTorN3WtmOamYUo8Q-KIyCcb2ulACkwApzEF4ZHpzFPUDLFuv3KGd6p7yxLBfiRM5ZmJ8O5ybw0a0Xy6YGtoV4nnWqra0xT_DrbuXnkVdbPVB1JEIOWqr8Qa_cAw1UfebjuaYsdO0vDGgZoqae0_FeQRBzITfxcFN-0uTfEHiCCWMlQJ-vJEVY-5-FrVRg4hcM2U1m9UdMSIqo62XZR3IRPRD8nDcVeVLmMTDr5YYEFY9Xv1fYIbO-hxYtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11ec7e1eee.mp4?token=uGGvLMeBvaOopvn85eET2GFYY7sOtpv1LOIy-oUitcc8ZEqxZh0H6BnscRy4tjaZnz3KNcFrnplI3Ov3-FfCaX7DYU8JTorN3WtmOamYUo8Q-KIyCcb2ulACkwApzEF4ZHpzFPUDLFuv3KGd6p7yxLBfiRM5ZmJ8O5ybw0a0Xy6YGtoV4nnWqra0xT_DrbuXnkVdbPVB1JEIOWqr8Qa_cAw1UfebjuaYsdO0vDGgZoqae0_FeQRBzITfxcFN-0uTfEHiCCWMlQJ-vJEVY-5-FrVRg4hcM2U1m9UdMSIqo62XZR3IRPRD8nDcVeVLmMTDr5YYEFY9Xv1fYIbO-hxYtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: رهبر انقلاب در مورد تفاهم، نظر کارشناسی را پذیرفتند؛ ایشان گفته بودند که اگر سه‌چهارم رای بیاورد آن را می‌پذیرند
🔹
امکان ارتباط با ایشان سخت است ولی بودنشان نقطۀ قوت بالایی برای ماست. @Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/454647" target="_blank">📅 22:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454646">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3ef09d2f1.mp4?token=aZvNDfnZKfn50qepSH8oktUOtXQGYvbWeWCKHpJ8IuT2L9aach6A7WfXSRDUVdW-X2Cg2uiQPLRHrk8GGZAcT8iPZu7oUvrVMjglkFwHucVek3f2GfAoohaaEhEQHF_-nh6FXc6g263McGWFueG4EJJXN4i0SydYyT_EiFcWPaGXz741CVUYRQ4SpCAWUCBCh2z0ipf6f-J7hcBBe0_av-2aeUMmMs7I-6ET_tYlHpK0F9uXEjl0WA01UhvmHq_wqnFVyW_x09sHv9-PvpxEvI4Mo6B9AtmSzrRR--Eeyxt_svGRF14kAg-mbsT-PhQiJBVvD-HcC6TmSCLZ2aZtHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3ef09d2f1.mp4?token=aZvNDfnZKfn50qepSH8oktUOtXQGYvbWeWCKHpJ8IuT2L9aach6A7WfXSRDUVdW-X2Cg2uiQPLRHrk8GGZAcT8iPZu7oUvrVMjglkFwHucVek3f2GfAoohaaEhEQHF_-nh6FXc6g263McGWFueG4EJJXN4i0SydYyT_EiFcWPaGXz741CVUYRQ4SpCAWUCBCh2z0ipf6f-J7hcBBe0_av-2aeUMmMs7I-6ET_tYlHpK0F9uXEjl0WA01UhvmHq_wqnFVyW_x09sHv9-PvpxEvI4Mo6B9AtmSzrRR--Eeyxt_svGRF14kAg-mbsT-PhQiJBVvD-HcC6TmSCLZ2aZtHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: نقشه کشیده بودند ایران را ۴۸ ساعته مثل سوریه بگیرند
🔹
شهادت بزرگان ما در جنگ رمضان دردناک بود؛ با همه سختی‌ها و مشکلات امروز از ایران به عنوان یک کشور قدرتمند و با عزت بالا نام برده می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/454646" target="_blank">📅 22:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454645">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cd906c65a.mp4?token=G_i8lzhYfY6FWHluB1XIulXQ23qema-b5zlRZF-UUT_8bMqb18qd3EJ9BKCqsL0yisdnFSd11WBig-pvHtgr4rZr4ktX5fTwT447VEY8cmYxunFtM6GczFKTTSaoL6UyLYzS8y84hCqJKH0ZzhytH4fZOsOiB6MZc203jsFzfrWM2LNoGK9WU7V_EhJrDQSxGuPwgI7LC9T9QUVxfjNJxCfQ5in11fj3_VVpr9oAiQ_L1XdOaEODye7t5HaNVIs95gGCRQlQXvZBhOXQjJ6-QjS3vld06bqUUDQwAYNeA7x2JzpnCASgFHBQccA_xPSK6s3MdUdqMq2gNZ6DwMmbdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cd906c65a.mp4?token=G_i8lzhYfY6FWHluB1XIulXQ23qema-b5zlRZF-UUT_8bMqb18qd3EJ9BKCqsL0yisdnFSd11WBig-pvHtgr4rZr4ktX5fTwT447VEY8cmYxunFtM6GczFKTTSaoL6UyLYzS8y84hCqJKH0ZzhytH4fZOsOiB6MZc203jsFzfrWM2LNoGK9WU7V_EhJrDQSxGuPwgI7LC9T9QUVxfjNJxCfQ5in11fj3_VVpr9oAiQ_L1XdOaEODye7t5HaNVIs95gGCRQlQXvZBhOXQjJ6-QjS3vld06bqUUDQwAYNeA7x2JzpnCASgFHBQccA_xPSK6s3MdUdqMq2gNZ6DwMmbdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: رهبر شهید مثل کوه پشت ما ایستاده بود و از دولت حمایت می‌کرد
🔹
اگر کمک ایشان نبود می‌توانست تنش‌های اجتماعی شکل بگیرد ولی پشتیبانی ایشان اجازه نداد. @Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/454645" target="_blank">📅 22:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454644">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e7bd0df98.mp4?token=UqYhaMsdwED8uJM-svYz9FQaKPLZOfKdElswAodAhYAtVOV43mEZQUuI06_8MH1cMBJqPqTJe8xCdwaF29tyM41zgfwbwlEJv5ko4lXhsReazh-gOYh6bdjz8L8c4xnjPQYTa0ElUtfcstPHONEHSYCi4o57FPqCCZIG0Q2yen31qjYFFpSxeLU9mZE6JWBqyOOukVZ9ak-HpBDarcfWab2MH82GWoLicuCgLze8aepu2zthWFQUc-6zwNZ3NOewbYsK3EWIzQBPn0559rp20pm18DnwJbv3hTB3mzvWcL9_5Iegw8FZ64S9PKJ0IYWTGCFO6Hz03gFuUS9DUbA4yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e7bd0df98.mp4?token=UqYhaMsdwED8uJM-svYz9FQaKPLZOfKdElswAodAhYAtVOV43mEZQUuI06_8MH1cMBJqPqTJe8xCdwaF29tyM41zgfwbwlEJv5ko4lXhsReazh-gOYh6bdjz8L8c4xnjPQYTa0ElUtfcstPHONEHSYCi4o57FPqCCZIG0Q2yen31qjYFFpSxeLU9mZE6JWBqyOOukVZ9ak-HpBDarcfWab2MH82GWoLicuCgLze8aepu2zthWFQUc-6zwNZ3NOewbYsK3EWIzQBPn0559rp20pm18DnwJbv3hTB3mzvWcL9_5Iegw8FZ64S9PKJ0IYWTGCFO6Hz03gFuUS9DUbA4yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: اگر تابه‌حال کشور سرپا مانده مدیون مردم است
🔹
اگر با مردم باشیم هیچ قدرتی نمی‌تواند ما را زمین‌گیر کند.
🔹
دشمن فشار می‌آورد تا مردم را به اعتراض وادار کند.
🔹
اگر به مردم خدمت‌گزاری نکنیم با خدا جنگ کرده‌ایم، از خدا می‌خواهیم کمک کند تا شرمندۀ مردم…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/454644" target="_blank">📅 22:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454643">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0653169395.mp4?token=QyNmmDlx0GKSUg7ve7biZ4RwWuIyQAa90-7e4W8z1I1lp2ElpdXbJM2YTMk1L_f3bh_EuOUw1dHDvuNn8-ZMlcL1ngiCqHBNnBrevIs5Dwp71ZFqMVZmX986SD15wXR-bFYuBoysqev7pzMtghWJjS6RrQ_O-HFmRoFqQodGfXAjo00d5XqJ88sG4Qgf7UVINwaKQjmaXR8a1hAuu95NFDneHCY9Pyi554_VufdSHnRKsOCgIGOkXH2MkPPW7YGOgsqnliMUPB1rOZ1o7IduWV7vKesgvtGy4DzgwH2oTU8axi7QPisC5zTLTMKFPaLLomuVPfMx6oIC46llYjHDNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0653169395.mp4?token=QyNmmDlx0GKSUg7ve7biZ4RwWuIyQAa90-7e4W8z1I1lp2ElpdXbJM2YTMk1L_f3bh_EuOUw1dHDvuNn8-ZMlcL1ngiCqHBNnBrevIs5Dwp71ZFqMVZmX986SD15wXR-bFYuBoysqev7pzMtghWJjS6RrQ_O-HFmRoFqQodGfXAjo00d5XqJ88sG4Qgf7UVINwaKQjmaXR8a1hAuu95NFDneHCY9Pyi554_VufdSHnRKsOCgIGOkXH2MkPPW7YGOgsqnliMUPB1rOZ1o7IduWV7vKesgvtGy4DzgwH2oTU8axi7QPisC5zTLTMKFPaLLomuVPfMx6oIC46llYjHDNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: علی‌رغم مشکلات ۲ سال گذشته، امروز ایران را به عنوان یک کشور قدرتمند و با عزت می‌شناسند.  @Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/454643" target="_blank">📅 22:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454642">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c783b2a39.mp4?token=rHY1iF2SNXclDIuQQgVIvT8oiC7WsHI0O2ZVDwuR2au_45FXtJMHVphE37zOOlLNvzYUmiC_TMIA0EaFyjwet5Z9I0IzFuY9Owz0EeIYr-teoeREtunCLqyjTLD3B7GIf7MXwBUY3FrSv_YgHwxuCrvQOakAn1rS89tcM_WUADzOu1N-yW26bmU9bZedy6xu1Ogm85y4Kf49VFPqUJE-i-aqdN05LlIlVIkYclqjvUK6dylMipSbGultTz8p6gUHlaK14_dFMs-moW3-X5lJ0vJLk-9Xc4vhDkgUKg7EgqTW4DHc_KqKcs-Sl1AxAbwm-IyTjACcF2g8psti2PFdBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c783b2a39.mp4?token=rHY1iF2SNXclDIuQQgVIvT8oiC7WsHI0O2ZVDwuR2au_45FXtJMHVphE37zOOlLNvzYUmiC_TMIA0EaFyjwet5Z9I0IzFuY9Owz0EeIYr-teoeREtunCLqyjTLD3B7GIf7MXwBUY3FrSv_YgHwxuCrvQOakAn1rS89tcM_WUADzOu1N-yW26bmU9bZedy6xu1Ogm85y4Kf49VFPqUJE-i-aqdN05LlIlVIkYclqjvUK6dylMipSbGultTz8p6gUHlaK14_dFMs-moW3-X5lJ0vJLk-9Xc4vhDkgUKg7EgqTW4DHc_KqKcs-Sl1AxAbwm-IyTjACcF2g8psti2PFdBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: علی‌رغم مشکلات ۲ سال گذشته، امروز ایران را به عنوان یک کشور قدرتمند و با عزت می‌شناسند.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/454642" target="_blank">📅 22:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454641">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QX1UHeucfbS4XqZlIaS0y3vLWZOHyCjiLWu0t_dz1G5JYgdJvPodj3vqGJh-9kuOIIvBMh9eJ3cEul1y7GYWgJHWbJTXdg6yu03FWO2LmscKTSGgcUmGgKKJFSmydq5JALz5dnthFCkOIuy9Z2yN2fLyIVtY4gMABxS1UQcH0-pbiL6TuBlosUBKYVlzvtOdiRsvpdGAa3OH5HWMlKtlp2hBPu9Dyyilwn2jnIAHl1TrbMPqP0ZXSxILB0zb0EUzd7dtBviBkrGrnOobd-NBRLpwQ-PZGXiRDDn5H6hqEViAom0sUIZSUJkJLyKgW4xil6HupEGNPx8VboVAeCHY1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استاد بین‌الملل: کنوانسیون دریای خزر در خدمت منافع آمریکا، اروپا و اسرائیل است
🔹
احمد کاظمی استاد حقوق بین‌الملل، تصویب کنوانسیون رژیم حقوقی دریای کاسپین را یک امتیاز مستقیم راهبردی برای رژیم صهیونیستی دانست و گفت این کنوانسیون علاوه بر تأمین منافع راهبردی…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/454641" target="_blank">📅 21:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454640">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
سازمان تجارت دریایی انگلیس از وقوع حادثه برای یک نفتکش در فاصلۀ ۹۵ مایل از شهر عدن در غرب یمن خبر داد.  @Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/454640" target="_blank">📅 21:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454639">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">انهدام باند قاچاق بیش از ۵ میلیون لیتر سوخت در بندرعباس
🔹
فرمانده مرزبانی فراجا: یک باند قاچاق سوخت که در یک سال گذشته در پوشش صیادی بیش از ۵ میلیون لیتر سوخت قاچاق کرده منهدم شد.
🔹
فرار مالیاتی، تقلب و قاچاق سوخت از جمله اتهامات اعضای این باند سازمان‌یافته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/454639" target="_blank">📅 21:46 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454638">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BWo9lHGISoc7TFx-CP-eX9lGmwFXyb-RqdX8DfXyjr_LLt0UGS_lT04F6_oIC0B1bL0HLR3TCRKn-A-593kpOHD_dkNPZkQEfirm_EqXcifbU7_MHWDEwo1jM4cYMmhAEd4Eq7woOsTRsuUxLC8NL1pVAWC36WSx-XIkVD6Kgp5xek3tTxcOSOJ1Jo57BuTkka8Z_JOmInezgyEX1ILtqJ9S_XxPcBaBqO48gsabhgeJj8vmiH0P-s7oSJqLHhrWy1-1KA50NfV65p-4oxE7qma69wFXiagoEuiZG3M0BSQOgBC8i_fppbJ0LRS841jyVmQ4cOocu9kIO_xUa2CGjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سریال‌های تاریخی بزرگ تلویزیون در راه‌اند
🔹
تلویزیون این روزها تولید مجموعه‌های تاریخی را با جدیت دنبال می‌کند. از پروژه‌های عظیمی مانند «سلمان فارسی» و «موسی کلیم‌الله» گرفته تا سریال‌هایی مانند «رئیسعلی»، «حماسه زاگرس»، «دیوار دفاعی»، «کارآگاه علوی»، «شکیب عیار» و «نگین ارباب» که هرکدام به بخشی از تاریخ ایران و جهان اسلام می‌پردازند.
🔹
اگر این آثار بتوانند شخصیت‌های تاریخی را باورپذیر و جذاب روایت کنند، شاید بار دیگر شاهد تکرار موفقیت سریال‌های ماندگاری مانند «مختارنامه»، «امام علی(ع)» و «یوسف پیامبر(ع)» باشیم.
🔗
اگر دوست دارید در مورد این سریال‌ها بیشتر بدانید،
اینجا
را بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/454638" target="_blank">📅 21:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454637">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e6ae32867.mp4?token=CuVe3lc8eBL_2PDfqColy1nVW21wR8IcsboXtDV1obLlANs4yIYLFesq3zLxz6AWau4uj0IW408DBAgZVHbkIt9oWsDnZbGgpROB-4iePKdKpBGM62k--JX_DPNPbB_AQgdpaWqNSz3656Alccwl8Hc8CNn6uwJQUbC--7FHvy49i4FbHDN56C4z0ukRWJlRbdrZsXHKvFafk3mvg72kB06UTqE6WSXRWwGp-R9ds1c_lurJug0EuMFloYqsuyaHLNjYTzyFEGpcoH_etMxX-4UwF4jauT9glNUlZw2HO-y1JsamGs7Wc857mXVpvs0VJoviTD8d9djdkP3gR0iZww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e6ae32867.mp4?token=CuVe3lc8eBL_2PDfqColy1nVW21wR8IcsboXtDV1obLlANs4yIYLFesq3zLxz6AWau4uj0IW408DBAgZVHbkIt9oWsDnZbGgpROB-4iePKdKpBGM62k--JX_DPNPbB_AQgdpaWqNSz3656Alccwl8Hc8CNn6uwJQUbC--7FHvy49i4FbHDN56C4z0ukRWJlRbdrZsXHKvFafk3mvg72kB06UTqE6WSXRWwGp-R9ds1c_lurJug0EuMFloYqsuyaHLNjYTzyFEGpcoH_etMxX-4UwF4jauT9glNUlZw2HO-y1JsamGs7Wc857mXVpvs0VJoviTD8d9djdkP3gR0iZww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بی‌بی‌سی و اینترنشنال چگونه بین خود تقسیم نقش کرده‌اند؟
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/454637" target="_blank">📅 21:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454636">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3f36ea27e.mp4?token=CRLzcOGUDDFf3FVFdrgt6YT7JXYBg5GLhFlPpyKUaqjnfAqwvyOOE5q9kSF4ctAMO6RMq-0vW19E6ojDLCwY8vNhM5M8BzDSnutFkEtekSy5QgVfuY6Zb6zkyPoEIx8kwEOpGLI1_IfcqMtok1O6Naf3T__wi1gejOkUbE62zkaxvRhZKEqXWNuXlQs-tkM6UJGHOUCPmJupbfBP5Pu8oZHlbyrUDcbEoLdrhIpx9p9cEd3FY2tSvnpOnvL6rHww102XzQKzwvKUl82g1ugipzJtext5_V3Q1YJJdUlrH70PjbSfiWHugmb9FITfL1uZ9E0mkJeOI2eflmrw_XkHbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3f36ea27e.mp4?token=CRLzcOGUDDFf3FVFdrgt6YT7JXYBg5GLhFlPpyKUaqjnfAqwvyOOE5q9kSF4ctAMO6RMq-0vW19E6ojDLCwY8vNhM5M8BzDSnutFkEtekSy5QgVfuY6Zb6zkyPoEIx8kwEOpGLI1_IfcqMtok1O6Naf3T__wi1gejOkUbE62zkaxvRhZKEqXWNuXlQs-tkM6UJGHOUCPmJupbfBP5Pu8oZHlbyrUDcbEoLdrhIpx9p9cEd3FY2tSvnpOnvL6rHww102XzQKzwvKUl82g1ugipzJtext5_V3Q1YJJdUlrH70PjbSfiWHugmb9FITfL1uZ9E0mkJeOI2eflmrw_XkHbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پشیمانی پویانفر از برخورد با شهید لاریجانی در اربعین
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/454636" target="_blank">📅 21:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454635">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d32835d80d.mp4?token=n099wcwrqyrAfUbIYiGSGsVc7rZW-D5AH4bROA7hA7aFB_f34fsjnuDWiVnFhVm6TTWMtkSd176t2-AhLOPD1pUDjK4b1PrnUtiNMbMQQe5woPPN900enyeZZkEFVZpuO78hM49uwArELzL5_rYWnVqB_JDgHkx2p6Hv0Nwq_4fRrugyqqJzMRcgVGLz59hMsb0nWFFsp0JliBEQQ5cTE4JkDyCo4wD_xF7eJkGDB4XosU-G166h9_gtvgHiRxmfJh6vedQetCFq83jsl38qsjz6UO2KwUeIvxnlEFNCE3vo6o0opN-FHcC7T7Q89EiurWdPIryxWPRvhX4RiPqMIG7lLywTf3v_bLg28cBs0KsHAJ1j3rYiQd0cMnC-Ibu53B89vdcNydyVlZUffJSrE96UOZUbPYGEnL9zzACBP2oMFxN0KdBmGuuZ-UB50WTtwyaiRLwyo0q7fSYY3EzTDYq7NajVrOl7E5QrF88J8B6M89JpWfKUNoFWL4fiAaEkag7gvF5ZlKG1vDX3eM3yE8hkcyGPu3uie8l6vs3Ny6-yFS1MyeWQYpF1Dki7peAQi5qMBMhMdrdK-KyTlR92yugyFMuWqq_62WN9A9FVl2T8hfxGyE1PwrvLMDlL3oohSu8OchzJ09RMlqb4V2WkaBVbWNU25GXO4U2ha2_BhD0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d32835d80d.mp4?token=n099wcwrqyrAfUbIYiGSGsVc7rZW-D5AH4bROA7hA7aFB_f34fsjnuDWiVnFhVm6TTWMtkSd176t2-AhLOPD1pUDjK4b1PrnUtiNMbMQQe5woPPN900enyeZZkEFVZpuO78hM49uwArELzL5_rYWnVqB_JDgHkx2p6Hv0Nwq_4fRrugyqqJzMRcgVGLz59hMsb0nWFFsp0JliBEQQ5cTE4JkDyCo4wD_xF7eJkGDB4XosU-G166h9_gtvgHiRxmfJh6vedQetCFq83jsl38qsjz6UO2KwUeIvxnlEFNCE3vo6o0opN-FHcC7T7Q89EiurWdPIryxWPRvhX4RiPqMIG7lLywTf3v_bLg28cBs0KsHAJ1j3rYiQd0cMnC-Ibu53B89vdcNydyVlZUffJSrE96UOZUbPYGEnL9zzACBP2oMFxN0KdBmGuuZ-UB50WTtwyaiRLwyo0q7fSYY3EzTDYq7NajVrOl7E5QrF88J8B6M89JpWfKUNoFWL4fiAaEkag7gvF5ZlKG1vDX3eM3yE8hkcyGPu3uie8l6vs3Ny6-yFS1MyeWQYpF1Dki7peAQi5qMBMhMdrdK-KyTlR92yugyFMuWqq_62WN9A9FVl2T8hfxGyE1PwrvLMDlL3oohSu8OchzJ09RMlqb4V2WkaBVbWNU25GXO4U2ha2_BhD0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردمی که با تمام مشغله‌ها همچنان شب‌ها میدان‌داری می‌کنند
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/454635" target="_blank">📅 21:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454634">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">بازداشت عامل ارسال تصاویر پرتاب موشک به رسانه‌های معاند در یزد
🔹
دادستان یزد: شخصی که با تصویربرداری از لحظات پرتاب موشک‌های ایرانی، این تصاویر را برای رسانه‌های معاند ازجمله ‌اینترنشنال و یک کانال معروف معاند ارسال کرده بود، در یزد بازداشت شد.
🔹
با توجه به ارتکاب این اقدام در شرایط جنگی، امکان تشدید مجازات تا ۳ درجه وجود دارد.
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/454634" target="_blank">📅 20:59 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454633">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fi2xW7mK0Bf9HX6gi9zvVIC8cGHzOUlgEHKehM2_Tb7MLk7LOrscqJaRiScvnSAp68sUzLAbMQw-vtJUk6MtjCDXRLQqeMqZ-A2-U6AvpB91c4TUPtmeC5oz9ibW_VRGwZeksb7Nc9TbmFTyPTxGjPAIqtOWQcpB4ttCNjjIGMBuJc1b4floG4DaDuW8ZuwHPxGhIJIhOTRxBCgNAZ2RAZ92f1Wlq7BYqO296ZI4tznMhnutpV6NVH-UjLGBdFjozovadDrlvrG8uKtoJkXURugTd2F6snclcZi7-nU-VZU7M9w6sUN8zotK4RcOSkju-E_VJdu73VC5kGy7Cc0vxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رایزنی وزرای خارجۀ آمریکا و انگلیس درباره ایران
🔹
وزارت خارجۀ آمریکا اعلام کرد که روبیو امروز با میلیبند، وزیر خارجۀ جدید انگلیس درباره مسائل پیرامون ایران گفت‌وگو کرده است.
🔹
طبق گزارش وزارت خارجۀ آمریکا ۲ طرف در این گفتوگو بر تعهد مشترک به عبور ایمن از تنگۀ هرمز و تضمین دستیابی‌نیافتن ایران به سلاح هسته‌ای تاکید کرده‌اند.
@Farsna
-
LinK</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/454633" target="_blank">📅 20:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454632">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‌ غریب‌آبادی: موضوع دریافت هزینه توسط ایران در تنگه هرمز بستگی به تصمیم مقامات عالی نظام و رفتار آمریکا دارد. @Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/454632" target="_blank">📅 20:42 · 14 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
