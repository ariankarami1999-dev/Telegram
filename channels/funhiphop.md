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
<img src="https://cdn4.telesco.pe/file/QaU_bwC5qe2Q7DJOOtTRJprULajRByrNjcDuYjcslxU0Avwxm7e0WzROP-wy5vF6YCuIMpV6xr9gNk530TpFORD7nNATw003DrNAx-hMqbmqr0krzXYPz3COY8bJva9K_G8AwKoAAAUo9r8_tQitt5pyqnlw_kdVXIX5yibyVYhJTqqiE4e9vH6xng5x-BobcE8Xg9JLs3WR1PqSdCUrp1BDJ252XZSPT5MT_YiZ74efmRVNxdZ5PTliMOdWtvE6VH84271AQev5Y13-TlOB806XZlm5rkD9czxo6fZJiucaifE4yBxhdgPYUQ4NhnZ_m9_JLOlNozCz5o68L7w37A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 226K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-14 17:26:02</div>
<hr>

<div class="tg-post" id="msg-83028">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترک جدید حسین تی‌ام به نام "ترور"منتشر شد.  Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/funhiphop/83028" target="_blank">📅 17:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83027">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdBhi9Fk_4tKpyRkNR4LFS4hha4RJFKYzjc3ztXj4maAXYMiQ2ebGfiKRU_qqiv3awuAmkKtqygPMvuwobEI-lbnKLktohHNXdOVAB3C35LXnoPlgQPJuPKeFs3LrAGv3jaOn1nTFlKURRziFW_nS8c-qyrVYJXfZFTysBFdFhTvvPRvfps0ReAlhj2t-Fsc3tNgLuD-Rnk8fcOZAul5tXy1ZwcasXcj82IjJMbVIbNPgT23c9cHxAzhSazWE9tzw-JqaDnN8UnKg1yOYMXuzw9aXnLDPM7s0ib5FKoLi7TVrHdWfsCe9v_1iIdtCi0fnRXGp3KY7k2sdcc1kJh7OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید حسین تی‌ام به نام "ترور"منتشر شد.
Youtub
e
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/funhiphop/83027" target="_blank">📅 17:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83026">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">پسر میدونی چیه مملکت از همش عجیب تره، خبرگذاری های یه کشور با فاصله هزاران کیلومتری از ایران بیشتر از آینده اقتصادیمون خبر دارن تا خبرگذاری های داخل کشور خودمون
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/funhiphop/83026" target="_blank">📅 16:50 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83025">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEQYyYV-7JeErrCmpmp4HU_91Y3aCtrhai4t1KnDsdA24G75oXtiK56c-g985uxq0DetCPvEbCoxDpzJdrk0p0O99fsMvPEcF8yLWKH1lPAczlmouesK5q0u0A9XoSWO4U6DbBYgTes_gkJCar98cMHCAzdbDB2yL8YMFWu-AIOEs7qtKPFb7ozabBwGd85IqqRX-tZMzOIcSWsQ2CinSAncOvX7quGwFc3IVxW1bWWRyxT34EZ4o0dGHIQZ5UwOQZ-QhGfFsECH0ylesx1sCMG3-EdKt3uNd3IXnJ9r6ouUHSpN3kmPAkYu6d448vYg0o42NKw2O5MmHaSZsMdzKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محکومیت دیدی بازهم کاهش یافته و حالا ۱۵روز زودتر و در تاریخ ۵ فوریه ۲۰۲۸ آزاد می‌شه
دیدی پارسال از حبس ابد تبرئه شده بود و به جای ۲۰ سال، به ۴ سال و ۲ ماه زندان محکوم شده بود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/funhiphop/83025" target="_blank">📅 16:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83024">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxK0blrD7dGAY1ONJIkIZYfayJKho6cTLUwRbZrXXbhyTxVC90CvEkTfxISypiuz2B0zuI12QNZB1-3BcPpTp_i7xhupgiAIkjjmzqUtgYcD4EdwXCnK3nCFVZxcM94q0LEcs-ncczRqTsxgYj0nfbsxdaymh5-8myn0CZDaq7l_2fCeZoK3IXakkUPW3BOc27FWDmxK1X--fYDgwXcjlDzdYUksBI0Pau9BbFZVyDJgDkjPi7GE99GzFP6t8imio_u0OzMz9U_8PZzAPELN2NWOCvw8hSV7BCbcfcrOTZf__H5O7BBh7eozDMatF01hJLk_aTMGd2cdgl-X8Ej2lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
😂
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/funhiphop/83024" target="_blank">📅 15:47 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83023">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">به مناسبت 200k شدن دلار بهش لوح طلایی ندادن؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/funhiphop/83023" target="_blank">📅 15:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83022">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxIvRz5cbdlVrhtdCahz_lNqy-NPklpiVTSkQZI9Ibk14u3qOYrBQ-xjI8ujGXUZpcaAf9bwA0C_zpvoqfAyVrFvHGbpIkBwg1cO9HPFAmcKPyU2Z5Ukp29HhX-5Eo5Iy1gy-3GaONoHvvsvWakCC5SgynZlA8AmRtg-7_DF5fC9mWSYxs5HE5FeoTOFBtF31BrPtxdgwiX4_nwmriopekWXZtdwpX46VTa5Ik1v8PtlJPOB8WkTWTgHCvc_VWVnZBik-_vxOAe975xeG0t5v4yvDSjrUi58bRZ58alc9Zp9OUVeTciVIWvfupPYEs-toQwLUTciZTg6JQ9L2nsruw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دالی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/funhiphop/83022" target="_blank">📅 15:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83021">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">البته در نهایت این دختره کفشه رو خرید و به آرزوش رسید.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/funhiphop/83021" target="_blank">📅 15:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83020">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-27lUIVDYlZNnPmvuTqwGh2uQ9322Hcu12C2k0WF2NyLq608jsRgHGDQkfgmiBHZNABG6kihreVni_VNZvaeIwG5nLi8xei69u1NYQF6Woma0EfKqyvP7OH-Gu7qwOJyv0VT4-F9CV1_hxcUvAeP8t_x1Y340QuIM_85M4VlWPZd0dU_TvmhDfKwq6fIrSfThWyItEb4yZrJ4trYNk1eA_XpWxfrAbyYJJbkwzd9dQboO5Li-rfBd3TGNYPZmQyAl17Rw08sVgPl-aiWphxxo1dTtA0ZPQh_giG2sdLWGnNjz51k0evHOsBfM-8zfEScWbfNsuhvWBoUmVsyEVX9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئو این خانم از دیروزه حسابی وایرال شده؛ داستان از این قراره که ایشون واسه خرید یه کفش به قیمت 14 میلیون حسابی برنامه‌ریزی مالی کرده بود ولی بعد افزایش قیمت‌ها، کفشه به 19 میلیون تومن رسیده!  اینم دیگه طاقت نیاورد و پشت فرمون زد زیر گریه  @FunHipHop | چمن…</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/funhiphop/83020" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83019">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbd895d17e.mp4?token=V02U5xDHvh4EErMjLSwTI-wuln4AQWBDmS9G5ozqITI7Qwy5TlMhog-gPt1mI3y3eh-e6289tN2gJgpqLtmRVHPzlMO54sNYPONFqtseE_BrLIFRQiqrz-lEYMknVezUroHuhYKGfremQnqGCbK6ozLqOUtrTVWh0FJFyTRzQN-_11rD2Cgu6TO76pl9Y1VW7INWVfJdUHPSpfrtXGp2Ylhc1NExDPDNVpSaJ6CDuxRXSXghh3GsW3VNehhkDOQZZ8eaY4zegtX6FEZKDRbObe2KKYM_wKNnKH0J57i4KbULQhniLblcmY0bTPKEIU6V7LjBYDjx5Rk7dAr_eUkbdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbd895d17e.mp4?token=V02U5xDHvh4EErMjLSwTI-wuln4AQWBDmS9G5ozqITI7Qwy5TlMhog-gPt1mI3y3eh-e6289tN2gJgpqLtmRVHPzlMO54sNYPONFqtseE_BrLIFRQiqrz-lEYMknVezUroHuhYKGfremQnqGCbK6ozLqOUtrTVWh0FJFyTRzQN-_11rD2Cgu6TO76pl9Y1VW7INWVfJdUHPSpfrtXGp2Ylhc1NExDPDNVpSaJ6CDuxRXSXghh3GsW3VNehhkDOQZZ8eaY4zegtX6FEZKDRbObe2KKYM_wKNnKH0J57i4KbULQhniLblcmY0bTPKEIU6V7LjBYDjx5Rk7dAr_eUkbdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو این خانم از دیروزه حسابی وایرال شده؛
داستان از این قراره که ایشون واسه خرید یه کفش به قیمت 14 میلیون حسابی برنامه‌ریزی مالی کرده بود ولی بعد افزایش قیمت‌ها، کفشه به 19 میلیون تومن رسیده!
اینم دیگه طاقت نیاورد و پشت فرمون زد زیر گریه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/funhiphop/83019" target="_blank">📅 14:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83018">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7770ac79f.mp4?token=vW61gfWY_u45_m_pXmRGA1v-ctM6qwkbUZEtoWdkVjUkYPmB2GJIdSStXLuo-6Ujd7rjOATBzhORWD59pXlEcMPwWpEds_lJCl7KCxRp9n2G_aglw6PlFXJ6SaolnjjOG7utX8BwVDDz87lwvkdb8nnYGYt-lAwTmxqNj4oXaUlAbQf6mxFoZf6Br_pVK7nwirABj8bZHNKWGxA8ZNoUhs7_ewUHdnOBQVxe1IMAbffmoi7jLQbu0_ff4PUtw2ETJqrJpxzHzBvmJxBNxgNcD0kwNiUzAqPIaLxPrQPvUdeI6ESSo5KFNL5dg29Jev-zEv_tlkg4QFZtAGWQ2dxvOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7770ac79f.mp4?token=vW61gfWY_u45_m_pXmRGA1v-ctM6qwkbUZEtoWdkVjUkYPmB2GJIdSStXLuo-6Ujd7rjOATBzhORWD59pXlEcMPwWpEds_lJCl7KCxRp9n2G_aglw6PlFXJ6SaolnjjOG7utX8BwVDDz87lwvkdb8nnYGYt-lAwTmxqNj4oXaUlAbQf6mxFoZf6Br_pVK7nwirABj8bZHNKWGxA8ZNoUhs7_ewUHdnOBQVxe1IMAbffmoi7jLQbu0_ff4PUtw2ETJqrJpxzHzBvmJxBNxgNcD0kwNiUzAqPIaLxPrQPvUdeI6ESSo5KFNL5dg29Jev-zEv_tlkg4QFZtAGWQ2dxvOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوزجان بیلان یکی از میلیاردهای ترکیه‌ای و مدیرعامل شرکت موسیقی «Muzikonair» امروز وارد ارومیه شد و قرارداد همکاری خودش رو با امیرمحمد امضا کرد.
طبق قرارداد، این پسر به همراه این شرکت مسیر جدیدی از زندگیش رو شروع کرده و قراره برنامه‌های زیادی خارج از ایران انجام بده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/83018" target="_blank">📅 13:47 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83017">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewuFFb3PuRrQb0W6oJGvKPI4tNKFLK03-R1gzrHJaTz6voHVfM-ExxfZexfS7G2qozsQda7EX4FJKM8Eqod9hBwcWbDdlb9x9ZMn71oAWE6Xsm2VR9OQZtHDxsYb24qjNidPmUyRSy9wj10CcXJ0K5PkR_0ZLcy-bKfgUcyKeapI9yIf7gaJn9lHGbR0wiAQn4GPzKYrNan_WzN_ceL6AipW0Cq1pT-92lQ7Ap2hFhQPJVNUnFUcMxVzyvT-ZHDR3-JbJ-4mCVk2E-baeEK5Wp5muJO_rFZ-yn3KaWrXc886IqA6g23BBRwmpabdMGm5QmPiMLuHk28LcJZr1rBucA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
صد درصد بیمه ویژه پیش‌بینی لیگ برتر خلیج فارس
🇮🇷
⚽️
با ثبت حداقل ۵ میلیون ریال پیش‌بینی میکس بر روی رقابت‌‌های جذاب و تماشایی لیگ برتر خلیج فارس ایران، در صورت ناموفق شدن نتیجه، بت‌‌فوروارد در هر روز از رقابت‌های لیگ، ۱۰۰ درصد مبلغ پیش‌بینی را به عنوان اعتبار پیش‌بینی رایگان ورزشی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/PERG100
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r14
💻
@BetForward</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/funhiphop/83017" target="_blank">📅 13:47 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83016">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">دلار نزدیک 230.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/funhiphop/83016" target="_blank">📅 13:34 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83015">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8BinZMInauunIm0h1pUkpXxpeXf0uzwv_qyflb4o0JNDSMUAiXc9ePfdxf96KLFR0tIvCbt0qTdnMNLQpqSRvvWiEe3MnTDeHnQ0v23DUs2Jcciry2K62PVWxDKb9tfJkhsBpDQDvCANSp8sbwPPxT6UdnpIKCaR7MQggYVtxckdxXjyRYGj3o9FtVG78DMTdtxm04shSNg4Ub9lQI3G8HP5cWVVe2J8fIWffrNcv19HquUy7UXyNANW0vaDLLXmn2vHod_EDzxuznTbDDJeTuXAy9OYSynS_y8CW4CpkgiL10LuvLs-VeSP1KRbJlPD9wCoOwdWDeRc-hHc8YiDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جیبارو سفت بچسبید شاه‌دزدای اصلی دارن میان
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/83015" target="_blank">📅 09:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83014">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">چرا هر شهر کوچیکی میری اسمش پاریس کوچولو عه، بخدا دنیا شهر های دیگه ای هم داره، یکم تنوع بدید مثلا یجارو بزارید لندن کوچولو.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/83014" target="_blank">📅 08:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83013">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ادمین نظرت چیه هیپ هاپو برداری فقد فان رو بزاری بمونه؟</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/83013" target="_blank">📅 02:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83012">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16cac9fdec.mp4?token=f-sDqvIbkzFNHQOUMU4Ro3nwj-ZNDo2G-xyrLwtUiE5dF25fy4279jW_pNrhcpLU1IM0Ll25VCHUwlk6G2ACe_1St3Z8VbbCWW4A1TqyVhQMp1Qm9cuMXrk6l7cUh4DaxuMci9Vm5pwRF-vEtsApwwukE_rFM7JxLaRRsY5jecFTOtybWKzZXpwlETAMSJlB0vosYvzNMCs6Wk-On7hdPNRuT82N0gL1SHQGj0tCwi2DIenp1f__W3LSwYMvuni4gHGcQUVcxFnixVNdQ6eaWK2z_gtQ8TsoCUQ0LMjNBHTtEGVXmFdXtQgVhcC_SlATsx-Q9OqOAAORKEcd15b_3GY_6yI2xfvIMb2w0WfxVhK6gafqB3TDOhyMQWwtA0n6-Ry2708OBWG-UYMc6yDZ6zYQqO97JGctpUj5cl6mg-E_jTgjtPPYWyvoek0aemeGJteU7XmZCrJcz43Ytc8GAfjb7EukOzP1igI2Xxsl8ACXt8XsTOR-m6Jn8X_t9IrZGdynoQbWg0ilm927RnGvKjI-ivp10uJ2BiAMRZmC3Q4VEwdgxw2PuCFXjg3a-UoQU3tR52Whx5MnBH6PW-7hrLvaA9mF858B3aJIORliCHk5xia-qj9Zsv2ao7vJE3-Q-mzj-_AX8giivSTTuxguohZBOAau2mam0lj-xfSGTIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16cac9fdec.mp4?token=f-sDqvIbkzFNHQOUMU4Ro3nwj-ZNDo2G-xyrLwtUiE5dF25fy4279jW_pNrhcpLU1IM0Ll25VCHUwlk6G2ACe_1St3Z8VbbCWW4A1TqyVhQMp1Qm9cuMXrk6l7cUh4DaxuMci9Vm5pwRF-vEtsApwwukE_rFM7JxLaRRsY5jecFTOtybWKzZXpwlETAMSJlB0vosYvzNMCs6Wk-On7hdPNRuT82N0gL1SHQGj0tCwi2DIenp1f__W3LSwYMvuni4gHGcQUVcxFnixVNdQ6eaWK2z_gtQ8TsoCUQ0LMjNBHTtEGVXmFdXtQgVhcC_SlATsx-Q9OqOAAORKEcd15b_3GY_6yI2xfvIMb2w0WfxVhK6gafqB3TDOhyMQWwtA0n6-Ry2708OBWG-UYMc6yDZ6zYQqO97JGctpUj5cl6mg-E_jTgjtPPYWyvoek0aemeGJteU7XmZCrJcz43Ytc8GAfjb7EukOzP1igI2Xxsl8ACXt8XsTOR-m6Jn8X_t9IrZGdynoQbWg0ilm927RnGvKjI-ivp10uJ2BiAMRZmC3Q4VEwdgxw2PuCFXjg3a-UoQU3tR52Whx5MnBH6PW-7hrLvaA9mF858B3aJIORliCHk5xia-qj9Zsv2ao7vJE3-Q-mzj-_AX8giivSTTuxguohZBOAau2mam0lj-xfSGTIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این یارو زیر یک ثانیه از ناله های پورن استارا تشخیص میده که کی ان، زن و مردم نداره همرو میشناسه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/83012" target="_blank">📅 02:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83010">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d117c4a49.mp4?token=YZP3v2pDDOT91o3E3Vri1coti0M16ZhPKKOMbkU51dXOCTHfyPIy4OW2pkSoBf-Tt7LUPsU4vltRjDeHWaFU-4RrM71CsUHwdIk_h4qUm3aOso5OXilxzz-LGXHQX64stz1WIjgHJbnuZLKHwI4zKaz7Sz57pQTc98IHJBHRgSbPm_ykAB1WmRYXw91nc_kviq4kwgikKOuIdQjO3JHsF01YblQukSZGzzjdgWVDuvWbMnQsdLSsdWSohyWlNnDiE3Kuk_68d_dhewMwMr5_hVYJ-kzSEcCHv-EpD_wPjCa-lISAdiq8UpL29w5I16FHKCtve_lQN49NW4CGkuYWqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d117c4a49.mp4?token=YZP3v2pDDOT91o3E3Vri1coti0M16ZhPKKOMbkU51dXOCTHfyPIy4OW2pkSoBf-Tt7LUPsU4vltRjDeHWaFU-4RrM71CsUHwdIk_h4qUm3aOso5OXilxzz-LGXHQX64stz1WIjgHJbnuZLKHwI4zKaz7Sz57pQTc98IHJBHRgSbPm_ykAB1WmRYXw91nc_kviq4kwgikKOuIdQjO3JHsF01YblQukSZGzzjdgWVDuvWbMnQsdLSsdWSohyWlNnDiE3Kuk_68d_dhewMwMr5_hVYJ-kzSEcCHv-EpD_wPjCa-lISAdiq8UpL29w5I16FHKCtve_lQN49NW4CGkuYWqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نگریرا وقتی میبینه ده ساله از فوتبال خداحافظی کرده ولی هربار که رئال میبازه اون مقصر میشه:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/83010" target="_blank">📅 00:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83009">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دوستان رئالی نگران نباشید
از هفته دیگه که رودری به تیم اضافه شه اون موقع رئال واقعی رو میبینید
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83009" target="_blank">📅 00:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83008">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FM0WeBMEBF1_AnxXZa3MhcFh6LIykM2znLgOLR-HCT31VQpKwX7L6LWr7IgD2EWe9E-leAMnoCXZJhmLaK7AzNR9ct4fEjWqbDzlwniqPPko9N4HUNWigLjkEc5-vHXg5-pxafZkqBxF4_J7423MnIv4ZPCOFE6NbCWPaJ7OAGm03lz02ISZC9Tc0W1s538a3ro_CDHJ8w6vxFaUfSwBCmh5L5ipzCD7_sLXDngztk8wo3oYy_5y3MskQ33PKanoGpAUnlccPOMMUFyShO_QiVN_haijzzrx5ErAImt_1o-SdLAVy5xFnyULImbt5TsViKb3s-81reJ9UoVTdSaMsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چنلای عقب مونده ای که این شات هارو میزارید چنلتون و میگید ترب فلان شد بهمان شد، کصخلا ترب یه فروشگاه نیست صرفا یه واسطه اس که مغازه ها جنس هاشون رو میزارن توش و میفروشن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83008" target="_blank">📅 00:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83007">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ولی لاشی با اون صدای بگا رفته هم بهتر خیلیاس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/83007" target="_blank">📅 23:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83006">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">امیر تتلو از زندان بیاد بیرون ببینه حسن بابا چه کسشرایی ازش داده بیرون مادرشو میگاد بخدا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/83006" target="_blank">📅 23:32 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83005">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0641a73955.mp4?token=AH2CzM7fCrS2llWQ6KzhAMAPHsBIopOq2FCcNk6UkXTlj1lAaaWxV4OVtWhxI7aaJ9WUuXrlpnLdF1792sv0dOQTUrWOO8cQWWlU6LTgX6aiZ7qJklpThnry-4YLFptTcSU20wrbQ4etKqJJWRaxhuVq1zdFJAq_sAh7uMHxi81vMNnx9UWudkB1WSPcBdU1yV_oLX4Nl5yNgQJaCrJ7eWzYq_rfrqgr9SrB5rObztFV9PcdFQRgibkcc-vQe4ZSxY4Fkoy5nMWZuZzt4n5HcvI85JQh7FPErTix_zQLOcGTi1KgKFgkPufVXqRurG12AwIwcaXAvpRxhZXNbXj_Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0641a73955.mp4?token=AH2CzM7fCrS2llWQ6KzhAMAPHsBIopOq2FCcNk6UkXTlj1lAaaWxV4OVtWhxI7aaJ9WUuXrlpnLdF1792sv0dOQTUrWOO8cQWWlU6LTgX6aiZ7qJklpThnry-4YLFptTcSU20wrbQ4etKqJJWRaxhuVq1zdFJAq_sAh7uMHxi81vMNnx9UWudkB1WSPcBdU1yV_oLX4Nl5yNgQJaCrJ7eWzYq_rfrqgr9SrB5rObztFV9PcdFQRgibkcc-vQe4ZSxY4Fkoy5nMWZuZzt4n5HcvI85JQh7FPErTix_zQLOcGTi1KgKFgkPufVXqRurG12AwIwcaXAvpRxhZXNbXj_Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترند جدید فضای مجازی دنیا چی باشه خوبه؟
شکستن گوشی و تلویزیون هایی که عکس و فیلم نتانیاهو توشه.
حالا پول اون گوشی و تلویزیونا رو کی داده؟ خودشون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/83005" target="_blank">📅 23:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83004">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tp31W1wUCeV1pt_jKpYtvpe3GM8VYjQIXlkljdkkeC3oGp3WZrg6z3vlKllIxbHBxe7oEXxQOUlfZAu9VSNCuvx65P9-RGw8B54zO-HZR1Z_KpVnb6uMWdgbh5_iQ51tO_droloECqoZD9wL4lhY6Bz-Ud5fYm5GjlwanSn_9dGCYg6EmJo4eHPGJO6c3T2K2yZ7mdpdlSbpB4JCDN_tlwdgnWjgAnoUnDPHGovmYfJ8eNebryn9tyisU92Vf90CRO2VbX27YKcgXD5o5P_B-kyoZfbVOOWdEnNDCg3Fsr8Za9xW9yqtSd7UoqbTRl7YUVMXOry4I92Hun9XzYONGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا امباپه یک ماشین گلزنی ها اینو گل نکرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/83004" target="_blank">📅 23:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83003">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbCTkYHDKmSqXaTzdCz6XIyH-VLMZwSQ-zX9n9ygGQWRsn_yDneIaJVxyeSSB8Iil3tiMxOl8l6HHXrxbEsHICkgEDFKGvy8zTuxbdvOHRuTS2TkrVjqbY0uamMwWU1-a3SaJaIlpo4eOtM72GJp7t4VIkjyRfwljWU2qmkRmVKZacIe2itNqH1-RNWBRJo2yOuNUBoobD_JvfDZUwuue3CQrUDuywvK0vjZi8jE74PJnPFH8wrYVa5uMUNsotHZoFgBaQI-SezfldpJ8HMnQsJCOWlLAO_rkg_T7Irz1R1zpBwCt2T0ES_inslxYYiHr-tsOmDfAoj4YcYvQhgxdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خستم کردید ناموسا، کیرم تو این زندگی که شما میکنید و ازش راضی اید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/83003" target="_blank">📅 23:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83000">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8WvkxZ2aWRbHB-SPziLe_jG7x-xtnuS6B_VyiIe0-oTfUo2yEQiqvc3QE6-2ud83asHJvdnl1TSYuaCpjR-iiAV7sfj_a1OTjhDVHRxXawYYdMPJNeG3mnzOzGsVTl69bjlNo1ts7KzwoKe64IKZQgoLc810tL9kA062dGiIPaRYI4D8DxG2GAtYyJhiBdEI8Fr7x5q2c0FvnV7rsIw3BP_uISL_yubTQmiZZ3eWx3lpmRw9gzyLR63Zu4TaVHz9gB1atXSaHCPAaQqK9fqui0cEaGWx4YHxC08rxL3T-XySlGA2yCEgYbvj6T-cjFGujPpG6nNSyPCRqqVd4ccAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گاس فرینگ تو مراسم اکران فصل دوم سریال جنتلمن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/83000" target="_blank">📅 21:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82998">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">یا علی اوتیسم  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82998" target="_blank">📅 21:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82997">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cfb0d4b2c.mp4?token=eH05LH8zWnGK0aDS2eYBcXskXtr2cn0ChtML-tIJGLENyIdXnS_wIcy3B_y3ZB1M_wA_wztXM1IPfazw1h3aHoofIIlcPt1j1NwiVdYD0yFqObYrA0MOvjZpevZeLBhwC-c7zOGkhWDHFJcIQmRV5SaSiFRb6sTBc0YFd8-vDm9F5XXFNwhlV_l5CnTmmtjKgaiD7B2lHDzaEXrz_SYBgY5vNzVSD12FBykJnasNRFzfYT1OxuJgAdxO_HIDqfIcdL_XYARmNWB6DSE8EduBOyucsP0XkIoi-WfuxRRuqML4ttIOCMfb-2LVa8HB_nf_65CVvMXmNNMukM8Mr_xJSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cfb0d4b2c.mp4?token=eH05LH8zWnGK0aDS2eYBcXskXtr2cn0ChtML-tIJGLENyIdXnS_wIcy3B_y3ZB1M_wA_wztXM1IPfazw1h3aHoofIIlcPt1j1NwiVdYD0yFqObYrA0MOvjZpevZeLBhwC-c7zOGkhWDHFJcIQmRV5SaSiFRb6sTBc0YFd8-vDm9F5XXFNwhlV_l5CnTmmtjKgaiD7B2lHDzaEXrz_SYBgY5vNzVSD12FBykJnasNRFzfYT1OxuJgAdxO_HIDqfIcdL_XYARmNWB6DSE8EduBOyucsP0XkIoi-WfuxRRuqML4ttIOCMfb-2LVa8HB_nf_65CVvMXmNNMukM8Mr_xJSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یا علی اوتیسم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82997" target="_blank">📅 21:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82995">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mQRovtx6ojBDxZx-J5l0jLbp2QWW0JCwXgP8j8AY6h1NNkWwLSoNqeRfmhsL80Lg2kn3rRDV0Cl5F12Iku561K6YO3rDO6d0Sm9PnONxS_zzDZ7u2Po7B7IS_CEulBd7CPUTMsNlnP6l_teKFcFSk0S-ho3oRzHl7De1IqpOeyP7LuAsprZhuhuu6EigzRKisO6tSubS_0njku-ZDK_3Ynh6O35tYcouutzM5ysGDjRrbhQO80owHVqYbXh1zvslF-2SdkHMLVccEdLoYXY-ayehui6y_Kon0YCfg8hFvsrmQ_RQkl981rMT9enntdtNhNt3pLVOv0AZSDXsdzbCdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d_A9Dd2pZXW-O8cdZCI4N8RHcIu-ksBkIU6m0LrTbqD94yrh0ILHQe3QpbBUQhWTQx8jp5DZFPoP0iRrbxqbXW69KtU-l4gYy5vs3YM01yuenXfZXZjG8iXLAFfzI6hmFGyl_bssCAfQuhgJBN3VZav7er6UfQqMnoUwHeIKky4SuCsx9IaIbbji2wn_UHRxKknO0AIHrIn7H8ZNsqtWP7Qk4TihTVg2d_fkxYg1rFNwapsqofFZCZSjiXzhdhaAW0kvWMRMFo6rt1uIfXmIog7NP29VovPgFEWWYJKYNTdihNyC60Jy0nIrzytWtkwt6m06w5ZKfUhtlqSs9aeksA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کاگان این گیفه رو گردن گرفت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/82995" target="_blank">📅 21:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82994">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce693d467f.mp4?token=H9i6rJySzrMK1TZ3BEIakm71wZ5cZFYVxjYNyKhn9A6Wbzi9Ec3CujnCCX4SjOb1uPS_Rly7zJ9_SpfCzoki3zabG1l92Wrn-s_gJnxgmExO1Ym0uDQRxOMhx1K_qySmfwwTQisD4PnkRdEYBeGyaYx_2tmYR6mVqDLNi8Xi6WMRbljvO4KwRzwl1Iz4c-Lxax1gy53FjmnyTERdJvBWpDW7AoTEcNV4YMTWO8NkvzseZRh3-49nwfJ9JwmVZZzKMKZXhiu6aFCnclzuK2_iGLKu1NBsthBHJzeiWNnPlzk1TZG85PQ9ELZrrmWb_1yP-s-cruR_OjBXTXAaEG4vgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce693d467f.mp4?token=H9i6rJySzrMK1TZ3BEIakm71wZ5cZFYVxjYNyKhn9A6Wbzi9Ec3CujnCCX4SjOb1uPS_Rly7zJ9_SpfCzoki3zabG1l92Wrn-s_gJnxgmExO1Ym0uDQRxOMhx1K_qySmfwwTQisD4PnkRdEYBeGyaYx_2tmYR6mVqDLNi8Xi6WMRbljvO4KwRzwl1Iz4c-Lxax1gy53FjmnyTERdJvBWpDW7AoTEcNV4YMTWO8NkvzseZRh3-49nwfJ9JwmVZZzKMKZXhiu6aFCnclzuK2_iGLKu1NBsthBHJzeiWNnPlzk1TZG85PQ9ELZrrmWb_1yP-s-cruR_OjBXTXAaEG4vgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به لطف هموطنای عاقلی که سطح IQ مثبت هزار دارن، لبوبو ایرانیزه شده و وطنی هم وارد بازار شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82994" target="_blank">📅 20:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82993">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">از اصفهان موشک زدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82993" target="_blank">📅 20:30 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82992">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">از اصفهان موشک زدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82992" target="_blank">📅 19:32 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82991">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">از اصفهان موشک زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82991" target="_blank">📅 19:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82990">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWymvoQ6DFNxWbfiWnQx2hYaO1iPgKlX3WggjGV0mGBnKhKZWlziCfQ3zR7nJWlmZ8p4DloYP_4G92vUeEk3Aj2_4wKAAHhT1_iePJQZjfSbtMxdOdduSqNgxEKCzTLKWQrv_WmqWdrZNHSbgfGbaC9Vs0W2UttSZ98ehSDywoZcjszf3hgsuFVIHuVgYk5SmbkdvtEIVZZNFNdAhBhv2oBKfd1zVLMHMuaLYejMLJbnbDeZugsEPFdBjNcsI4DwMd8YXamlIFs0jrZw8vHxCGgKP6y_U0Hkt2obS2lfty6WSDmZrDczMU4M9xJe7Rifo02ftBKWUW3YPdJdFo5Tnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوید محمدزاده از تئاتر "آرش" به دلیل استقبال کم مردم اخراج شد  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82990" target="_blank">📅 19:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82989">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">برو مارکت ترکیه خب مشتی، یکی از رپرای خوبمون رفت الان یک اونجاس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/82989" target="_blank">📅 19:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82988">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hg30NzHGrxFYBr2aL5jdqcSdXKblwOs5bIkPfyHbami4jB9KpM4YZo3j45EFLjbo-AIJG4Xlk4japWM1s8Z9rE1YkrWIsKvGXY4GjMUst-HHTZ7OO4-TdSe28DL_oGGgrVyF3F8pJP8Y1pKPfS6aAYZpuJAqMH4rmQnTlE2hMbtVi3dcyOP3nuduYNCHYlQRCsInkXjJq1Bat2HjneawkP9ZNmNM1gh4vyh_UeLaV4L2HR2O8DPq6rMc3IppGkIqJpsnztbkAM26CBIAbYAtJ2ZaFx8Sagi2m-RrPQ6ZL2TbPX6HatSvkLhmLsNMVdb7D00cCwJxbpTJaen_SpzmGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادمینای چنل کوروش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/82988" target="_blank">📅 19:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82987">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6ed68f76d.mp4?token=m1CxGqyDMY1klQx_FXQ3gKhM1ov9qdjXhvxdwJRCJWa3r_Tu4e6kvy3ifJUrRTw5S4X05og0JHXkel-d7ETm9hvbwPGGOj_dBqmaYmQvTV82Vfj_pXlUkSg8HFWD1DvLECTE63AviWpsZnxhKsotPHgQX2C89nbISNIbP5ggL_MwNuTFWzOsg5sxohTMh_kwb40i2gd4B-ICYjHBO0atjX8qoabfoU90TfS_ZZKfVadkxqR5E1vQlkd3Eua8CIQe-wMTQ324r3JMklTOyTJANdVLctNIl4mpqijhvrT9ciVnAHOJCiH_TFveBmcr90yXY35QcxN_LFqcwpJ5_dm9Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6ed68f76d.mp4?token=m1CxGqyDMY1klQx_FXQ3gKhM1ov9qdjXhvxdwJRCJWa3r_Tu4e6kvy3ifJUrRTw5S4X05og0JHXkel-d7ETm9hvbwPGGOj_dBqmaYmQvTV82Vfj_pXlUkSg8HFWD1DvLECTE63AviWpsZnxhKsotPHgQX2C89nbISNIbP5ggL_MwNuTFWzOsg5sxohTMh_kwb40i2gd4B-ICYjHBO0atjX8qoabfoU90TfS_ZZKfVadkxqR5E1vQlkd3Eua8CIQe-wMTQ324r3JMklTOyTJANdVLctNIl4mpqijhvrT9ciVnAHOJCiH_TFveBmcr90yXY35QcxN_LFqcwpJ5_dm9Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست پاشینیان نخست وزیر ارمنستان تو اینستاش:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/82987" target="_blank">📅 18:50 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82986">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf87a5e3b1.mp4?token=XJI1ZEZhqeTrtDJX1DFkmrLaGllImuAfLeab6-SHS3zfarE2IxO3LrjtgRv0KSsHXoFNzBM4U5zFmml_7eDJN4hgfWd2s-lE4Hhyz45cz2-u_8hjqADB6gfytXkD5ZOGoT4h7WoFNOOgUnz82c71IK3UCcTxTpMadw_doCTswzP3j76BFra6ihGUUtM4_E1Im1GKcQsSAUD8T-NkRuqIwBES1K6Y1ICsoNyjCoJ-2x8GXmMcY9CnInLrIw-i5qRxA7wQRAaYX4MwqlZfsEKnadlK3UKTTNOkMaFjw-nMxxU_AyKfNaA_u5m1KLZ8wA_u6Zr_u3Vh_bEmznbr77mqrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf87a5e3b1.mp4?token=XJI1ZEZhqeTrtDJX1DFkmrLaGllImuAfLeab6-SHS3zfarE2IxO3LrjtgRv0KSsHXoFNzBM4U5zFmml_7eDJN4hgfWd2s-lE4Hhyz45cz2-u_8hjqADB6gfytXkD5ZOGoT4h7WoFNOOgUnz82c71IK3UCcTxTpMadw_doCTswzP3j76BFra6ihGUUtM4_E1Im1GKcQsSAUD8T-NkRuqIwBES1K6Y1ICsoNyjCoJ-2x8GXmMcY9CnInLrIw-i5qRxA7wQRAaYX4MwqlZfsEKnadlK3UKTTNOkMaFjw-nMxxU_AyKfNaA_u5m1KLZ8wA_u6Zr_u3Vh_bEmznbr77mqrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آزش آنالیز ببین کاراتو تروخدا
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/82986" target="_blank">📅 18:35 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82985">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ویدیو جدید پخش شده از نازنین بیاتی کف تهران.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/82985" target="_blank">📅 18:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82983">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5EaojwLlNM0_M7TD5ZcUCxu3Zq0by_1KoS4w_FpDD9q9UCilLH05jC4QZJ922IW5A8uEZ7vr7hKy_l3_4XSPEyAWk67XUwxXCo44HZApELkq_pLf052IDX-GxLoACkNc6eDos9a-sSfEFVVCTCL5ghZhcJDsW6g0u0rsGd4QKGGb8r--ipXya_GMYup0MQjGKceWu5Qeqx-pOBMupfjtV6jQ5M-JVz6QBZuKL3wzdh64GUb7vwcT5EjnYceXfj4gkLWZqWB_nJwgiQozRafriA7lnMAApOHiGHLiX1hv-2lfgn1P11-jv-CH0p7KRdyx19VPQYv9eOLIUUu8dScvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c34b684e1d.mp4?token=chwV5RGSP3iHz5v2O-Awohb7DhcME5zkdJukJZ2kZBaODHhYoaY7S9f32dqxRG2fhr-fDKKMDxfOnxbJ6Htdt0uDdCANq4dJZPP8_Kp1sp-VV1sqCtH7bS4ugsqce2_uglMdQRx4VWm9sJQZzbUXSrkYyEUy9lWoNxuSzrzvJPfoEUcrcxSXpHEfZed5c2Rl6Y48_yIWGnYVfKkt6G5s4kWHRINXQQ99HvpZyClcGa6TsYrrZzhjGQYI0UwTqKRbvdnpi5DszXn5iT9qNUNVaJ4IRjlC6Vb9mMrALYKNEhtrR_wwIHccWslifMasvNozaSgydrKasXRs7Z3qRlqu1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c34b684e1d.mp4?token=chwV5RGSP3iHz5v2O-Awohb7DhcME5zkdJukJZ2kZBaODHhYoaY7S9f32dqxRG2fhr-fDKKMDxfOnxbJ6Htdt0uDdCANq4dJZPP8_Kp1sp-VV1sqCtH7bS4ugsqce2_uglMdQRx4VWm9sJQZzbUXSrkYyEUy9lWoNxuSzrzvJPfoEUcrcxSXpHEfZed5c2Rl6Y48_yIWGnYVfKkt6G5s4kWHRINXQQ99HvpZyClcGa6TsYrrZzhjGQYI0UwTqKRbvdnpi5DszXn5iT9qNUNVaJ4IRjlC6Vb9mMrALYKNEhtrR_wwIHccWslifMasvNozaSgydrKasXRs7Z3qRlqu1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو جدید پخش شده از نازنین بیاتی کف تهران.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/82983" target="_blank">📅 17:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82982">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpIiqxZabexwq-b5Io9BK4alLECEFrTnDpZtQII0qvGAJbhEYX14jJjFGm4p1GsrAs0atO5-p0fYQqJff4rdVIclfZrUODgtGJy3UW6rm2RxHbZtJ1mEIMG1GOR7io3B33w6hPIoKhKqj8ceXAo--u1NismgGzsoq68oMtE4qYw_iZ4MX3-MsKpupBP4MYbZCLjch50eb5ECL9M30U6PqT9tGOkwI1fax0DVLsTk-CtNkS-P0QEqE8tmRAwLQqMwCXQ6dmngHfvhkKtEUj7bz_n-6KC7XXnghdLmJRsOp8bCRhfJJfdQ939szUDrl8hERB87oZNLkcRgZ-2f459cSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بیمه صد درصدی هفته سوم لیگ برتر انگلیس
💯
⏩
با ثبت حداقل ۳ میلیون ریال پیش‌بینی میکس بر روی رقابت‌های نفس‌گیر هفته سوم لیگ برتر انگلیس، در صورت ناموفق شدن نتیجه پیش‌بینی، بت‌فوروارد ۱۰۰ درصد مبلغ پیش‌بینی را به عنوان اعتبار پیش‌بینی رایگان ورزشی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bwrd.link/PL3
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g13
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/82982" target="_blank">📅 17:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82981">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qs4Up5Lkyux7UHFJjwnk1lqCxeZ_03gSeiqhRpI6UNFtAhn_3CwQx96gBq4qR4-IolUFLcRC9fDjAJKJGX6ZKWo4Erj9AkPiodk8Et4Ag1PeVqUq0zLibuVx5hqQWFSBYG4UA7-_nNI24mYPA4uWAtAXHrR5Py7oibTo57L9NUartb2_tMb6Pib_ahCcCZ7uPhQj6a0f-PMsR8i8iZBTJXfiSIdJxFN00I_5cJ4OI-mP3zF6yJ2vD5py_w8gtAgJ6K_SY6xmOxGIKlyWhNAVRE4qtZJwBGzhOlrkb94nPKE0QjsKVrN_4Zs6GChFvUMeWnD-RRTA1vRD4P_zerajtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید کوروش و سیا به نام “چندتا؟” ریلیز شد.
Spotify
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/82981" target="_blank">📅 16:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82980">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/575bec5ffb.mp4?token=IMlqHanLE90WDfoKkRUM2bCo4rYbXJrMVPujlXO9iEUeeQ1zVmecC7qKJHAdRjuteWAnHjfHeGMCxpDCFWphHJzsfwfCklyWMBN-lQhacIY1Ky9vQvQ4qroq4UN4mhtMln3tq7stel_L8oTX7jkZeatsXa601bfHnRZRY0uN18olqF988XQzCffS6x1e1jmvCxUt8mn88QMVjAfKD1wrSYzUniQltOc0FRTA70WZxXn0V-h5Q_A_VS7FKgI-YQ-CYDo5X4zhSEkA9lWDxQrNlm9oVRSabx4FuXlG3WvZkgaKtE4GLKre8IjBa4Mip7a1DHHX-YDoWmiSquXv89ApIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/575bec5ffb.mp4?token=IMlqHanLE90WDfoKkRUM2bCo4rYbXJrMVPujlXO9iEUeeQ1zVmecC7qKJHAdRjuteWAnHjfHeGMCxpDCFWphHJzsfwfCklyWMBN-lQhacIY1Ky9vQvQ4qroq4UN4mhtMln3tq7stel_L8oTX7jkZeatsXa601bfHnRZRY0uN18olqF988XQzCffS6x1e1jmvCxUt8mn88QMVjAfKD1wrSYzUniQltOc0FRTA70WZxXn0V-h5Q_A_VS7FKgI-YQ-CYDo5X4zhSEkA9lWDxQrNlm9oVRSabx4FuXlG3WvZkgaKtE4GLKre8IjBa4Mip7a1DHHX-YDoWmiSquXv89ApIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقال تانک‌ها از ایرانشهر به سمت چابهار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/82980" target="_blank">📅 16:24 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82979">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترک جدید بهزاد داورپناه و آیسم به نام "تا بتونم" ریلیز شد. SoundCloud Spotify  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/82979" target="_blank">📅 16:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82977">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUi3G_TEkdAWDd2BMgId8KdCsDkt75jjpP4Z9xxuuBOyy56Cy3WYH39KC-4QK1f0n7-uiQvYl6jQJAA8xMhjATDDqUKGDt9plcEV156149lRGAFIV3GiNrQd0s5XsPIV7E0itglr3hVgH0rpce8IHd9E9wJSTtTY5bLQCZ4NRR4_r4dRDf7lcG3TsPcNXqzijC94qLGpAO9-aCtbb6u6LigZJZ17EgoQ-EYYSA430bftrNNaDJcZWiCfsapLjS9iOe25Hj9jQ_kwuClu6z9SxgsMZC-2iSWOXDvFoN3LFuaqsIFCkZXgv3kHxuJ2y6DMK7vw_RbB371RRgMx3WCkyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید بهزاد داورپناه و آیسم به نام "تا بتونم" ریلیز شد.
SoundCloud
Spotify
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/82977" target="_blank">📅 16:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82976">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCdnQQeO62qdWM4iQ_xyYsH5kMGUysVBI8axmrwqC7deXYdH0_T0pZsueDWA5vLyS8hAFpuBKa9HNdJJxVP9E5AtbAvqfiLA05JK4R2oatfuW90OpanJiBmLYqworakPlyU-v8D9S8VwE9bVcBo1JV3DS9gshFLHL5JISvNPuSxlj_5SLMD_WNez-hPs37QZgNDzLY7fTxCwtWhiovpNgBAjTYgNrRVMh3aQYiqiRQlMaTHKMdyfiFdeZWtDEC-9kmaNHE4NEHPEwS2IALwv6palH7-97UQ3tLgxfahf_PHVFeXG7SsUQYJ9cEDVNYV2f335RWngVPo1YVfY3xKqFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهیار و خار مادرش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/82976" target="_blank">📅 15:49 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82975">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9q8mmaajfD2mmCSzqCBdw_-ZiRRRRUyTrwUTTVVld83mvnpeaf8yhhYqxscrf3EmPHX5wG4W3OnapjIJmxR8h-rn18S8SP1kHk3-Fc0izkFagrhm4oPyarUxSOQOvAEdjpZ2xC08chlOjV2oTghgTg8t3jcwXQGXoZfWYS9cDh9HZ0XwyGQECWLk-LG49jMbB6A56dqNAkW0Q-QI4TS893BkEfPp3-rL3AehgxBeskpJZKp4VdgP0CpC_MRYolERPd0PKBos2ScWLrMwGX9hak60CC_1YpYP7hw4I3rWBxCRl7QYud3GGgAutD3SOImumGaDrkY-6wd8xzS8OHWTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برا دکتر حسام خوشبختی تو کیر خلاصه میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/82975" target="_blank">📅 14:37 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82974">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/McfpcB8v6OmjS-JyTJOdFWHE95oqoUCEH2GJQEuBReu5MAzjzoeojy7AvjOtIr17J3kUeAd10HsDkXxGKQIzt30L_Qjqz2b4K49eBFMH_F8_o7MZ6_f5TAZXdyYSM_9QGR7OPnPQjueEfhZNSzIzmtVWgGR1lzyE_il1OyWoCgZyF8142Aj2G79fnzOslk5UFKTuU3G9KJ2mDzra50Ntudtnq9D1zMa4ALptu-wXwUMq53veGi99fseWIdGdcBSjtq9DqiYQFvPxzbC3srH9fIFSKeKw9IWRjyPIdJ-GdKZepjsgzEanjx-PPZre-X4nt96F3n81jx1KqybvAHSwNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ببخشید عزیزان، کمبود محتوا تو سطح فضای مجازی و رپفارسی واقعا بی‌داد می‌کنه و ما چون دوست نداریم پرامپت و کصشعرای سه سال پیش رو پست کنیم، مجبوریم هر روز به پیج این اسطوره یه سر بزنیم، ممنون از صبوریتون.
🙏
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82974" target="_blank">📅 13:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82973">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">خبرگزاری مهر: موج یکی از انفجارهای ناشی از حملات آمریکا به یه مراسم عروسی تو هرمزگان رسیده و باعث ۵۰ مجروح و ۴ کشته شده.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/82973" target="_blank">📅 12:50 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82971">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYBLd0xlTUsDtN8cAPXTWYW3l2DMDXBbRmG8jtsMq-JiMOih_HlrKxRkw7xpXz8R5LsV4oUlj1_v-7sT-G_5H8e-k3olJ4bXkrBaDKKWClcJgq0Q-T3B4biWwdHTml_ljucENvlxX_QBInun9wTRtYy9AMAUtuH1Xa8WZJd4TWIavzMI_kgoTncj99BWkTaKNeCn8fpN6qzaSwZKCdP25h5IyzyK5K2TTiOcdea2iz2kpsfQgfV5Zfn4tleYDkvaliQuCDq1hw1TN4xiJsUJnuUDe5go_tm1T26tNQK07HxiLBdNMSy0_Mx0JcUVLJ9HFhjz9Xj90N-poQ53rQhuuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ad8899803.mp4?token=fNJi0ZIy4y1NsiJPWirstk4tVX-nMdziPk3Nydcb84uCeLO4JYCJ2ZF7pxUza5CONvaffXegM2SoAp3k51BJiuM1yl666sNSOJx_LT2A8w6SYSFyeGeOVUUIyAzL2ioIopfaYUZ80ysNt-xjx0DCsCaQuoTpAg1StVmym2v0hBnmowT67f84H2tTD_-1rW4cA_6hYkuPXoxNlPLE6Vf8WCBnfKPFxuPABB952HyrrUpkkt0mposB_G2LAuRADnNRk6-yDHNj3yU1cfA6t25Thl0UIZfptrD3kTUa4JFCgFM6n-7ARRooPqRSa9X1iQeEIjqHwAc7z_qtYrLuiEH0SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ad8899803.mp4?token=fNJi0ZIy4y1NsiJPWirstk4tVX-nMdziPk3Nydcb84uCeLO4JYCJ2ZF7pxUza5CONvaffXegM2SoAp3k51BJiuM1yl666sNSOJx_LT2A8w6SYSFyeGeOVUUIyAzL2ioIopfaYUZ80ysNt-xjx0DCsCaQuoTpAg1StVmym2v0hBnmowT67f84H2tTD_-1rW4cA_6hYkuPXoxNlPLE6Vf8WCBnfKPFxuPABB952HyrrUpkkt0mposB_G2LAuRADnNRk6-yDHNj3yU1cfA6t25Thl0UIZfptrD3kTUa4JFCgFM6n-7ARRooPqRSa9X1iQeEIjqHwAc7z_qtYrLuiEH0SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بالاخره رسمی شد بچه‌ها، آه از دل‌های شکسته و حسرت‌های ما
💔
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82971" target="_blank">📅 12:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82970">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WAxEnuHj_yhWgjRBxmv2UzNc6gUaf9OKaJQFLF7Xbh5QPuehCelKBGiOHw1fAdOLj263Sq8k2FAlvixfhWefC8wZe3O48GkVWRjppf7dlkL3uBXyf3fHbczapxAFP46zpBZmPBTSFmqV9PsC1kOeAWgd5XPIkNuXyuy3cQfFc2JeVXRHMss9QxzxjU7zYiJhkmU_yA95Hb_mMueXnDmyDCSYsOh7D2_BhqtFL-ZsmmV1Lpf15AVgiiLkKmICDHJM17Rxr9nMF6lIq8G5nChFP2rCqavjah18ysCHUheGBtozMx1a64Ldp-JYaepuBIGc18Y56mQltYTuzYGOkbMb0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بیمه صد درصدی هفته سوم لیگ برتر انگلیس
💯
⏩
با ثبت حداقل ۳ میلیون ریال پیش‌بینی میکس بر روی رقابت‌های نفس‌گیر هفته سوم لیگ برتر انگلیس، در صورت ناموفق شدن نتیجه پیش‌بینی، بت‌فوروارد ۱۰۰ درصد مبلغ پیش‌بینی را به عنوان اعتبار پیش‌بینی رایگان ورزشی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bwrd.link/PL3
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r13
💻
@BetForward</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82970" target="_blank">📅 12:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82967">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ای یو علی هستم، ۲۸ ساله از کرج  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/82967" target="_blank">📅 00:56 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82966">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b02f59615.mp4?token=dvvUYYur1Ec9NJHuylg2U0AtoZjnVnRJiwYk-RuiZG0HOXPTN8nS_bougJ4tMdVnfY83HrpUjm2r8JsPpi1GpbMVhE33NvizeqkrG0au20bixke1MGo6YgfTg_4OQe2cM2eNwWOLh6Vq1xb1GjUsSCFXeGJY7mrUQfNf7dVSD_zWMPThVw2FhMUDbCkKwUP8bPN49xst2uRUx_lKFQcWLE8XCDw1jufPrS8jd-7KDJloUN6nhgBd54O78yC9naqmdPQS_ZlhzdVXI6fRtuJK1QtA4jmu1tDoAfs6KwLS30Mv59-WbbpBO-uBNnRPA6iZ7wRpBD-P10wC5ArWo2Gorg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b02f59615.mp4?token=dvvUYYur1Ec9NJHuylg2U0AtoZjnVnRJiwYk-RuiZG0HOXPTN8nS_bougJ4tMdVnfY83HrpUjm2r8JsPpi1GpbMVhE33NvizeqkrG0au20bixke1MGo6YgfTg_4OQe2cM2eNwWOLh6Vq1xb1GjUsSCFXeGJY7mrUQfNf7dVSD_zWMPThVw2FhMUDbCkKwUP8bPN49xst2uRUx_lKFQcWLE8XCDw1jufPrS8jd-7KDJloUN6nhgBd54O78yC9naqmdPQS_ZlhzdVXI6fRtuJK1QtA4jmu1tDoAfs6KwLS30Mv59-WbbpBO-uBNnRPA6iZ7wRpBD-P10wC5ArWo2Gorg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ای یو علی هستم، ۲۸ ساله از کرج
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/82966" target="_blank">📅 00:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82965">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c3f3bba65.mp4?token=iGcBIMqY51VdvMScnIWgtgVIfFCMm47zIDeQHxvu2AcoLOQFDlsfj0VH-mmcsDs43DtqAAbHdLTr89g108IqddpUmR25xH8zT47iVJk_2ygTpSN9KQF7lEkuDhqfMGPOlKcUQBWgWiegU0h8w-DM0Ukayu8SGzPn-F8lvot0Ov9-GNnKi5_BrgmVI0n7g74RdN5KXNKWo7gG_kECfMIYEtGOaFUwaXMm2R4oRs2UBlwhCfEvVg_dM0GKj91Dshccz7Yci3Mg478ZmtaQXGhs7bi24jz0CvB6iT84q2FD-N3McYtpYOkkBBK_bjpeQiuyArxFIvsA__zqNuSBgV1e3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c3f3bba65.mp4?token=iGcBIMqY51VdvMScnIWgtgVIfFCMm47zIDeQHxvu2AcoLOQFDlsfj0VH-mmcsDs43DtqAAbHdLTr89g108IqddpUmR25xH8zT47iVJk_2ygTpSN9KQF7lEkuDhqfMGPOlKcUQBWgWiegU0h8w-DM0Ukayu8SGzPn-F8lvot0Ov9-GNnKi5_BrgmVI0n7g74RdN5KXNKWo7gG_kECfMIYEtGOaFUwaXMm2R4oRs2UBlwhCfEvVg_dM0GKj91Dshccz7Yci3Mg478ZmtaQXGhs7bi24jz0CvB6iT84q2FD-N3McYtpYOkkBBK_bjpeQiuyArxFIvsA__zqNuSBgV1e3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدیو از صفحه رسمی فدراسیون تکواندو ایران منتشر شده به مناسبت گرندپری کره جنوبی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82965" target="_blank">📅 23:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82961">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اون قسمت از جنوب لبنان که میگفتن اسرائیل حمله کنه میزنیمش
کنترلش دست اسرائیله دیگه</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82961" target="_blank">📅 22:59 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82959">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCkYU8BNMFZeodKwaaj5xXz_9GGor1f6O1y4j2oBXG_NMzw368tU6NFfk4jIFlbEOk-xSuczMo2E16MyLXJnXBJMUT4ZiUoWst48Fb-VUHtuoMNLFIlRYizGAqGK4wKuVgyCcOxzOpwSeyvoSekAAX8E1QJ5UJGhQpGRlPz8FptkT0xcGCkKd87H1TrFpPafaa_eJREg-ytA7X0uv2qDCx-Q4PQr4IN1naXuInzX013n4P-_gcR2teJ5XJyUWDR5MJHdttTv_TKVLcjJK7h7MBL4Jzarj_i9MZLGqGZbeG6mVX8Amz1bESTTMhpU5IBopvYoFp5zMia9OTeGpm9-PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکوندی شاه عالی بودی شاه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82959" target="_blank">📅 22:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82958">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7a86445b0.mp4?token=s_CSRhlvLHjwa5dDTfyIXsxDSQJk1qPrqKwV3or9IIaQK5hBA9Wcw0cYoL9tg8vI__iYKrvzrJCyaDKtwPhXmxbSfLHx9lbRWgQrc9iLE5NY6Kj6g_DQg1R6-c2fvZV5b1k-oRj1WSyv-3XPaM96TsHJRsWi7PZ8Tjv8EkRpcMxkd1SgTR7prV_0bRRrqQxAyicGt4kvXI-ZSGQGHGj8d5OkTswNoy3O2cOIX_Tq831uvO26gE2foH9oYqHPSBwyRRAAuTfP--JRcclXEH4nyrIq66zGrd450u9QeGfS1_dzjFlX7AsBcoc1rD7nwlrKksA9jpdCAmYkiglz7GehBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7a86445b0.mp4?token=s_CSRhlvLHjwa5dDTfyIXsxDSQJk1qPrqKwV3or9IIaQK5hBA9Wcw0cYoL9tg8vI__iYKrvzrJCyaDKtwPhXmxbSfLHx9lbRWgQrc9iLE5NY6Kj6g_DQg1R6-c2fvZV5b1k-oRj1WSyv-3XPaM96TsHJRsWi7PZ8Tjv8EkRpcMxkd1SgTR7prV_0bRRrqQxAyicGt4kvXI-ZSGQGHGj8d5OkTswNoy3O2cOIX_Tq831uvO26gE2foH9oYqHPSBwyRRAAuTfP--JRcclXEH4nyrIq66zGrd450u9QeGfS1_dzjFlX7AsBcoc1rD7nwlrKksA9jpdCAmYkiglz7GehBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کافه ها هم مثل طلافروشی ها و صرافی ها جای منو مانیتور گذاشتن که هی بتونن قیمتو عوض کنن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/82958" target="_blank">📅 21:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82956">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZbNC_G3Y4cWXZDAQgsz8RTmMBUeQdsWf-FvBncGgvB26hMAqPqrZFy_FZoRcSHkRNrfDwVBKcNniCPr_8kOuYzKJR1zPob_SCFolNwmMcCgGPxKIQwnmTRkuWM20pYo3aV3nWLdEsbdU0ZkXM1pvNJ7slH_bIigUndKQyqlKFC6BwStaBj-G1tUmrjk-wwPTTv1_v2EfT67Xg0581edOCXWDaTJSX-kqGcjWXTaVtF3FD2X8H5PzFCHIlz0ffxtQSiDSygZwkFVH-kKofddnEzmRi6Vud5NHgsckkKTMeMB2kmynwNX_TU75lnkbOYX9B_Z959FDmy1a3po3d70OfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید دانیال و پیدار به نام "Bipolar" منتشر شد
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82956" target="_blank">📅 20:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82955">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LpbH7pbW6ADhPZI4bOgrovQDhgPYG934tRen5ejAwVdBO-W-9F7V3PyfQNenEAB2QernIC4KAM0bXi0ltVN7-h-WFmaYrOcxdSLFp074eh0tCuZTsRDuH0_TqjPxx5hXMBhWQK5_AumCiE1U9Fw4ypT7KNRDK2S_xBcxU9aTWPeRGDUiQO1Y7dqM2vNwWg6We0vdtJphyqanOHrb4SmZpMiSC7SBXD_hNWThzhp5aqQ5mR1GV5X5DoeOSqnIH1GdcZ7RpVYQuWeLwZdiSb09__BI2-UGgEv4TAaJeUM3ZFSmr8kzuj_ZX21ZR3KeL9lv5HKa4_37pInSMzkhgCcGIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا رامین بد سلیقه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/82955" target="_blank">📅 19:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82954">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZIjHQ0zrGpY7h8iM2awTImGYqah2hk7Bje8JRpLfZWQ5kJhB_kCA8G33XDeDPeW4vmVamDEtmaSumBWyeQL3wOnkBOm3g8J826N8cRYZWla-bLiPgVzoZURpeqYrA55WhC5DIb3UZvNqfQmAcIJc70BHxTmE8wq8XQQnbXoZSCtZ0n6EclOdkT-GVzcBqnDzGC5p8ao_Jmy_lfGaYkXTRkIX0Z6Wul6unF95_k644UPM6VPSK85akXru4zjtPnhfJ2rDzXDWbt0aFzEebwQawT-cGjL4bBqIxy8J5oFVld9augHXxMEJyak8VJIEwWU1jDjs76Cf7Ar-Jz8A0OQYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینی و پسرش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82954" target="_blank">📅 19:12 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82951">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzZDkOV7m-bwXO_kqj2xium03rNeRrgbbZsxctjmj4T3tMhH_zrEzC55nwC7mJSMZI69ZI1fSKWQzJsYw11lnQgMNu3bY3TrWfbZ1CiUwVTZC27JbWw1BKI2ydPT5ZRixWG0P3kgNjGPMNutDRsgipAjlMehQqLsUm-dBtnwyFRpQz5zt8EcgZVpk5E5GIycGo7zXUmWp6dBstOO0tn3SKv0bCp1_Ds-LojGQMkFv1GtpcRGQy_bU6P-fE_Q0pMiJCGL64ekyI3R4RP-4pdpxDySf6Bo8BW5T_mljrv9xGtSd7r15dbP7ONAEv5jykcRH0Qxhvvv90rGRKInkgJvTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4876dd24fb.mp4?token=QK2gZ5OTuOZjA1Cn-Q4WZb6_BGkd-ZVDLFdqmrL8n787YqtbIQ_Ngd7qtp8dPCeNs3obYWfz_AtdKoLinGoBE0zCr80H94nVuJK16epLqb2REfNLVleJZTCiTB08HtS4FAsmbYsX4FIyYFvtSNPecKT0mG2xDEYINJuvWzvHnHj_RJ7kkaZQm5WN3l4r7sGG2GEipOYgas7uKgEqTC4tSUO6caGOVFageEFU3QCEfNyHyYTtRpNkpV12im8ggmcBgR9bUPjHJqsnhSFIQTtxk56S40ogXKSzo6jNp4SUXxBeHc50bkOMpVXvL9SNdZxBmJmbqmEgkfT1IOr7mgEg5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4876dd24fb.mp4?token=QK2gZ5OTuOZjA1Cn-Q4WZb6_BGkd-ZVDLFdqmrL8n787YqtbIQ_Ngd7qtp8dPCeNs3obYWfz_AtdKoLinGoBE0zCr80H94nVuJK16epLqb2REfNLVleJZTCiTB08HtS4FAsmbYsX4FIyYFvtSNPecKT0mG2xDEYINJuvWzvHnHj_RJ7kkaZQm5WN3l4r7sGG2GEipOYgas7uKgEqTC4tSUO6caGOVFageEFU3QCEfNyHyYTtRpNkpV12im8ggmcBgR9bUPjHJqsnhSFIQTtxk56S40ogXKSzo6jNp4SUXxBeHc50bkOMpVXvL9SNdZxBmJmbqmEgkfT1IOr7mgEg5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شات های جدید سیدنی سوئینی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82951" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82949">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/shYyywnPVRTNWCI0AGbY26d448Y4Vx4fiysNqyRoLYq0-OY_5CibXRe99lTIHUCuZLnGd96tqVAgumlXfudWfCVAhofmgXZh6RgEdgN5-bNFnWGOCWUfW-T-4x8gr36V9UCCOVobB_WSyojyaoYzSHSjgJng8rhAF_ROMCiq424LgNKFiA_zGamG8U--spCOzcyX1FnNPMCg_wXinUk3ZKdLWY99edsAr4jsA4IsWe6HQkG5tBa0v166rzW8jjmr4h1xvTvbCqajdlPzDQnFYxp9az0WWL-8wxV9xPIxes74wN6ujHW97odJ4CpCUTokOV6ru5Kyg9MqdumfSmdnLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید دلو به نام “منو میشناسی” ریلیز شد.
Soundcloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82949" target="_blank">📅 17:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82948">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">خلاصه بگم کونمون پارس
ترامپ میخواد پایان جنگ رو اعلام کنه و بزاره بره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82948" target="_blank">📅 16:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82947">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bspt81a-XxjyKyh58ipokn0eeTdnKA-0LCM0EkBrMKG-nhIsfXN9IbbTHziYO7iMUTMJeNNE72Wh8H0FWM2n8OQG8qR78sT3fdKuXN9fHFXEk_yTGAESGVAsAhqkhNliwBOhFq9wO0ZcorgL1NApPXDg1dIz7x6sNU4qmFjZ8_9Q6KZRH8xoiqm9GDjlG2KEKL0P_EIuygm8073xskt2T4F3eJemfSxOesJBPSNXjLu-TxoLiq58uipFEaSiOVDUzQii3HXmMrzauQEJCvvH_hVch30nxPw89-njHOr5-clGbSpurBjWsmUgqUinxCvSqu_9DY_L_jFwGzHIxOoFaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فصل دوم این شاهکار اومد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/82947" target="_blank">📅 15:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82946">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c808b4326f.mp4?token=I31U-WbJGxYawMtTEQU77R0DuW28Tkqrd6zj571irzgZu4vyUctp3hBQVjFvNPzpweoepGz4V60GD6DES6G50PJH2YvKYEgcmN_Sjw7FKvivaZGBUjgUw-cxwmy-ejdAMkyTrDgvD1LyGma6gpeULapAyiix50y6eUYTxTP9KCdMaQ9sicVcUH_Titw8LbuZ0jQKlLec2qqiT7eshxE8qE2OK98UA7ixP7WnHz78W60CsxuClh8VTwvMcjuxko_Z7XBrt2g9Lv0dlaCeFbOB8eA_lWZGiIAr7s8JgwHR70bX2RntJicuMzVc5sIwirM5mliu7Qf6v7r_PWSRJGsG1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c808b4326f.mp4?token=I31U-WbJGxYawMtTEQU77R0DuW28Tkqrd6zj571irzgZu4vyUctp3hBQVjFvNPzpweoepGz4V60GD6DES6G50PJH2YvKYEgcmN_Sjw7FKvivaZGBUjgUw-cxwmy-ejdAMkyTrDgvD1LyGma6gpeULapAyiix50y6eUYTxTP9KCdMaQ9sicVcUH_Titw8LbuZ0jQKlLec2qqiT7eshxE8qE2OK98UA7ixP7WnHz78W60CsxuClh8VTwvMcjuxko_Z7XBrt2g9Lv0dlaCeFbOB8eA_lWZGiIAr7s8JgwHR70bX2RntJicuMzVc5sIwirM5mliu7Qf6v7r_PWSRJGsG1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82946" target="_blank">📅 15:23 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82945">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mU1dWZ04tv2LueW_K3kiiNIqZeolZWftUX0vi6n7gpnY3-Mp4Jry9Mw7IX7hKtRv0NuhJgMK7YUKnzsyNd1onJN4YH1ICa_6spEu2sejqgTQB10UUV8QtOKXiQmyRIiYUIU-dj8jz1qIZlhWBrg7_gZ2kCfW2DHSnSlzJXtd_zLYc-HYxqAtPs20of54Sa83rM4aW9JHPH4un_1yxImwH65iUbHe3co1J5YAdPXd-wTq5pqQwGMtd3tRWVhEbmwRZZ8I_rDih4OL7P9xmUe90NC7vq3cTl5BdCssjH4V4hzBDs6MsDih8quQ6YrseIyPcGq5nDi-NgPLGkIRUX98Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست اکانت تلگرام تو توییتر: امروز احساس میکنم خیلی کیوت شدم، شاید بعداً عکسای نودمو براتون بزارم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82945" target="_blank">📅 15:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82944">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WW9rtc2b7g2N6pCE107BY-U6Uevw3qGPyIx4Tc2luTjeGPdGWNkvthoqMlRNd5V6V715X7Jf6ZaceRMoAU1rpDskMukY9Ko3VA69R_qpA-YW_JDc_R13eU4bTDpQU-u0mm2t7RD7qKr_ufNCluVsf80rAcBwzJoB4eQz7LoyVA5PtS7qU_S1oKh7Mv6hSj2uq4li2a8Dp1i2btRog5OmmlDf0CFLPUjdk_4zylvtEdqIv8FdAMaTdDjJbc_LEdWqp12dmDZuc7A7AJiMrj_g2xcxgsUAnuH1hoQIhpHhhqILbFTHJMAbFzc5yw0r2bkmu_xRcTjwojywGedsifDNpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد توافق ونس رو دعوت کنید برا تحصیل بیاد حوزه علمیه قم حاجی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/82944" target="_blank">📅 14:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82943">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70a5ddace4.mp4?token=f54srDdUAcC0sUjfBaKxLK85yhTswHZuAa662WRSu0_Y7Jz3G_P27IFW873qNvVoE-3yf9dAnzWQbROWUdTWm2WqL90zz6XtHtZq2fw_NoOzU_bGMWhFx7XQvwF3214k2_a_AFVHzajgJZ9QgcHBHAkkOP_JSfkHjnAKtV1gSlLXCL6UK9spHLBF7pFtp75a8gQEKUuI1Ipun7Oko6cJp5lSRQhMQ9ONPwh8kf1-x9Qk6bqNQ_OulM174xZwBnryrT8DzL1yPYzfOKtKz8u57CIiZrJ1J5wAl3BqEOEeobr21umrVaj4q8u0DfasEh_Wj_5fFIvjef7Gai2Z8JwQ5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70a5ddace4.mp4?token=f54srDdUAcC0sUjfBaKxLK85yhTswHZuAa662WRSu0_Y7Jz3G_P27IFW873qNvVoE-3yf9dAnzWQbROWUdTWm2WqL90zz6XtHtZq2fw_NoOzU_bGMWhFx7XQvwF3214k2_a_AFVHzajgJZ9QgcHBHAkkOP_JSfkHjnAKtV1gSlLXCL6UK9spHLBF7pFtp75a8gQEKUuI1Ipun7Oko6cJp5lSRQhMQ9ONPwh8kf1-x9Qk6bqNQ_OulM174xZwBnryrT8DzL1yPYzfOKtKz8u57CIiZrJ1J5wAl3BqEOEeobr21umrVaj4q8u0DfasEh_Wj_5fFIvjef7Gai2Z8JwQ5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی بهت میگن اگه ناراحت باشی عامل خود فروخته دشمنی:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82943" target="_blank">📅 14:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82941">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">حاجی دوران شهید رئیسی، یادش بخیر</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82941" target="_blank">📅 14:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82940">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpyi-8oVuP8sq5_w_OrKqeVy3nS5aXnB_hDO42GidpatEknWtB3q7-ITQ00SV1_DgDYfi_aCl0x_Gqg3YP-B5PE_m3KmKQdrmEiSOXgR9qIF9L225zxSrGjVHw9jVVDaPMd4gj9Iz7PGJe1PbjqSNhP-SWJbfrrahoCwfvqBoDUHgwEpQ59-U0rECZy3Ax3LWGuZDLowHJJtKEBVa6hT6sZ9T_2M-azI8Z_oKy93VZz9b_7r8T2EIDQHkuVKYe0Z8Mzs0T-4ves-lUSS9reDlA3M9FsO0PZxyEtZIhPqvN6Jtv1jzhiff7rasfqUnZkx1mdll3LIfmz_RRiDXbKR5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشتی از سنت خجالت بکش این ایموجیا چیه
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/82940" target="_blank">📅 13:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82939">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">یه گدای ایرانی تو ترکیه با  ۵۸ هزار لیر (۲۷۰ میلیون تومن)  پول نقد گرفتن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82939" target="_blank">📅 13:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82937">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzUaFccbvdAZK9U1Kgfnbe34q2a5Q3WoloFq07bLJV5LK6rhwhTHDcHIkzgA1p2m8_QYx2CcRkz0fBK2mlAEcDz2W4W5cARBsR2PgDfuCUuFXaSmfKQPxeJPjLRxtjCimQZCMxT5LV0hGy3XlSaqUV6hwBvBw51UpigezYNBSwQedL86hc5tXteZvfBeoCe8-mpL3p_NcDDHL2Fm6Qk_Bfxf-T7wWNv4KlYvRZUFXnUwxRkfK6jeZ_7X5-wf-o5DaszK0WCdwAY4guakXmfI6vWSatYQCLrpPb_Lh4tededeQAAp40wK5wKXxgx1Iq1AooE_CAGAQBsyi2XvbBAA_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa3cc88bd3.mp4?token=ZPuThkL9rkhWZPP9ySC4S9r4FVcFax0cOVwxZs_sqtzTZfcyq28olOFtrscOaIi-65TPZbdnmof6xKDWQKUxXS3ZG2NQzO9c5kx-iyhbCGx-WX130Sr1Jl2smYxrCu4fslHWubARxoUJ_BzcazgVN5AQToVtdFrmUbueVLL4XadKDmIy-S2j6xFTgkXuqMgxk5g4dEzCMzjNHq6Tg_pleq3mU3pVJJXT6c2MNYQvK6K4G8Fv05uQRaVXArpufT9ynv69hZDCSh0jvsMHMDIJUKLwrqE-aSqQGRIKODXWW6bDWR3WinPWzzSaeTQqgwfuAcghBDVFTgzjDEW9kyHOCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa3cc88bd3.mp4?token=ZPuThkL9rkhWZPP9ySC4S9r4FVcFax0cOVwxZs_sqtzTZfcyq28olOFtrscOaIi-65TPZbdnmof6xKDWQKUxXS3ZG2NQzO9c5kx-iyhbCGx-WX130Sr1Jl2smYxrCu4fslHWubARxoUJ_BzcazgVN5AQToVtdFrmUbueVLL4XadKDmIy-S2j6xFTgkXuqMgxk5g4dEzCMzjNHq6Tg_pleq3mU3pVJJXT6c2MNYQvK6K4G8Fv05uQRaVXArpufT9ynv69hZDCSh0jvsMHMDIJUKLwrqE-aSqQGRIKODXWW6bDWR3WinPWzzSaeTQqgwfuAcghBDVFTgzjDEW9kyHOCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید مسی که قبول کرده GOAT خودشه.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/82937" target="_blank">📅 11:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82936">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gofQuTlIrEFhkafQVszLjtxatl-lKrqnBO0onVB9ys5oXSxPX8bBxIzkSZ-dnqa2549JInbzmL03LcOAxN5MD1ltvQdn7v0TVFo2H2vX_nm58nACeQ0kkEyd6OQxkIf59RTc1fNr_2xJ0w64n8QUvPugB4mhZKHF3Quu8C_vJhh2lyX1fU3P2AIogWLVp4Uhmindq_OU4qfZuaRR3IKDgT6rnpiH8w2f4vQMSB0CxBPm08ZxwFZ6NKxML6PlUz-Wz8LrNYw93NX8FzsFrTIlP4gD8U3qLFh0MbxUQYGOS5oXDODb37j7n_QGsUQQFYIYqRpvG6l4LLM4rrMRHZJySA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیوید بکهام اینو توی باغچه خودش پرورش داده و به زنش کادوش داد، ایشالا که خیره
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82936" target="_blank">📅 11:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82934">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCRQ8__2m55X8c4P0hE9pCy3Zt8tm0qPoht3BgCd5SKnsz-My38MPz-MyeoZJ40zw18Mz-oJ3tsF0s3S0sA0B8V6rfZ-YU-eQxDV3olQoYIvwmlR8YWnbhutRld4dR6ZrOMOvVZiyLQhi4y1dZPwMSlr3YqDUWe2PHCZCEGTH6EzdJINexm8otXHSbT1ES6Rf0q8P3lAu_uKeb79HTHkIUr8tbdOtimglHbkFHmvH4ZE5PgJfTB8US2QHZxohaprOs9I_kNHALEBS3xfkIt_56SRDK3F8cokvC3I65_MMZIlYtUFg3uBYPCRN4bd7EFgRWjMuNv43lFTlsTmrRRY_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرسی نکن پسر تو تازه ازدواج کردی
😐
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/82934" target="_blank">📅 06:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82933">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c96481e00.mp4?token=v8TKQRUUhkxq9jEil7lo8Px_Sfuz0jRJMGXz4nOiI75UudQvFeCFnlMdRQ3Kma9SDecLhsRL_NCwf3Vl0dOtWgT3PFDzHPubpTHixGPDUYiF_wS336m9aXEfLgXEwEIUl7WPS3q1ITeLz-YwPzZEpz_z0leT0xb4zEgUDo-1sYzXt_8X8pZ8gudGYdTFVmjo4fQx_G9MAH8VUJwruGGS0Ga7y5ckdFtA34jXCEXx5K95Fdel1IChAF53Ova4BmZJbQGLqjrmmhOnslAKZpFFHs_1CODPIBaoOMryN_63WVYO35VYz-mFSaOAb0F89_8-2mLGfQVighyr20fJDTPW7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c96481e00.mp4?token=v8TKQRUUhkxq9jEil7lo8Px_Sfuz0jRJMGXz4nOiI75UudQvFeCFnlMdRQ3Kma9SDecLhsRL_NCwf3Vl0dOtWgT3PFDzHPubpTHixGPDUYiF_wS336m9aXEfLgXEwEIUl7WPS3q1ITeLz-YwPzZEpz_z0leT0xb4zEgUDo-1sYzXt_8X8pZ8gudGYdTFVmjo4fQx_G9MAH8VUJwruGGS0Ga7y5ckdFtA34jXCEXx5K95Fdel1IChAF53Ova4BmZJbQGLqjrmmhOnslAKZpFFHs_1CODPIBaoOMryN_63WVYO35VYz-mFSaOAb0F89_8-2mLGfQVighyr20fJDTPW7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداش میخوای کلیپ غمگین درست کنی درست، ولی خب مشتی از وقتی یادمونه این بازی مساوی میشه خب.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/82933" target="_blank">📅 01:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82932">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DDc4Qip7Rfi7F0ayKnUeeNjbK8CfeU6dh_aX6YusGm4zKRIWYsfS63EzHXjPlbU3mriJ_iltIdKpTOFedfMU8L_AidSZj-yrs3Y7pyvQrXQTdAyD_jysMEp9p8QcFcwdvNx_fsk5_yEMzWzn56KzwN3wJPmQZrwOX_9C-0on6XFe8bc1nURC_wgX4rfwDCxP11lzdhnutsD8caTa5qnft9qic8je8EASZdK8fxjzZ2KIs1h_8SbVKcoznRCQ2kDvXmiVdhsTIWkx5BdTOj_wqGSufxZEo4QY8jEDjRW-qU1YkhEbugcnyP3rvo852E2swGyCbuAPRcCx2ctLjkxCCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داداش بی‌خیالش شو نصف شبی بگیر بخواب، اون بی‌لیاقت بود تقصیر تو نیست که، لیاقت تو خیلی بیشتر از بودن با اون بود.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/82932" target="_blank">📅 00:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82931">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDaLnixOZCaIf9eYU-LWeV-MXb3gAYYvGjjqrHYO92grw2jZaU4UXOqppB72Q2KbFvkazVcl9X6w-i33QmjtLyPAhqjzyRpHZ6Zd8oVrC6URRAcSV2_QJZcaQ0GFguSdMpEzyaT1M8IXUjoX5w35AiJT7x4QjEr6LjwY-pawYzvMl27qhYKyMpf5uhwrXU0ZYhssSMLZ1m6kX4ApYTiYRyvgz1ptgop9wykLI1BiH5lPSFSz-gDisZVlB8h15sLdARUuTtXBkM04oDzzDHU1bGri9A4bUBxY9aHIhFx34PkKsUED3jd4f24XrHX-uYO2iM-KqDSC0Qc22VUfFSMF_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۰۳ سپتامبر ۲۶
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/82931" target="_blank">📅 00:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82930">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/azGMX3Z6lI4WluGap-7aSEw2CEXGrQtbXhFfndbqlIb-DI2df5v93nKpcWZvU4z31XMoTVeckKeCoPuMfoNK7aD1PAgC6CypdbTsHt8CTqN81z0_fA8T7E9L4NecJHND_pVsgAl5OMWpKdIQtVoqKUVT_Ym0hfHFFkMKbLpkt43xbqiaWkKydbMfwX1sV0LLhBGw5O-nLpjLlafUQQEHS_GMMok7lHReufjOXopUW-aw7agPpJwggKgJXNn6DXa21DfzSUGaKXOhumfcMSiNkYZTlt-Gk7F0cIGzRrFhC2CnsPmq7yqSrqjNM4_pBi8Fcg8vEgHFgg2yO70_SV8gHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راننده جنسیس که توی مشهد یه تجمع رو زیر گرفته بود: عمدی نبود، از تعادل خارج شدم و وقتی به یه نفر برخورد کردم دچار تشنج شدم و جا اینکه ترمز بگیرم، گاز دادم و یه دفعه همه رو زیر گرفتم.  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/82930" target="_blank">📅 23:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82929">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">راننده جنسیس که توی مشهد یه تجمع رو زیر گرفته بود:
عمدی نبود، از تعادل خارج شدم و وقتی به یه نفر برخورد کردم دچار تشنج شدم و جا اینکه ترمز بگیرم، گاز دادم و یه دفعه همه رو زیر گرفتم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/82929" target="_blank">📅 23:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82928">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSMAGJl5DtOb3FTtOushKpIeICPi4QXO-wkMM95pBogfWZMpY4WKjySBc8_Jw20P_GkIF0xjutcUIHZUSXyd0C5h4V87NZqLaK5FeeBQVAEByH4kQrrULu0bLRA4jCOYA90OuAE94JqsRRHlxnyeqGMoTVXZ_3HVp_48P89PtkpeVIgTQWJRbzbbz4Q_STf0IEmMSq8QY6HL0wTkCv62VbU8edvfh-i69BL2DjpvvXVoYyJ21fRY09fdAHmYi6Z-0pKTtYqNjbwb5RqdLdOsW0wRRKxyLvAoxjYoMeUfaFliKRj6eOxaQ-BJ0h8Ob4EzNGqSsFi61DarhMkjUCQVxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی به این پزشکیان بگه یه زمانی همین روسیه نقش آمریکای الان رو داشت اندازه دو تا اصفهان از ایران خاک غصب کرد</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/82928" target="_blank">📅 23:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82926">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">پزشکیان خطاب به پوتین :  قدرت‌های بزرگ صرفاً چون زور و قدرت دارن، حق ندارن بدون توجه به چارچوب‌ها و قوانین بین‌المللی به بقیه کشورها حمله کنن. حمله‌ای که آمریکا علیه ایران انجام داد، نه مبنای قانونی داشت، نه مبنای علمی و نه حتی توجیه منطقی.  @FunHipHop | چمن…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/82926" target="_blank">📅 23:08 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82925">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">پزشکیان خطاب به پوتین :
قدرت‌های بزرگ صرفاً چون زور و قدرت دارن، حق ندارن بدون توجه به چارچوب‌ها و قوانین بین‌المللی به بقیه کشورها حمله کنن.
حمله‌ای که آمریکا علیه ایران انجام داد، نه مبنای قانونی داشت، نه مبنای علمی و نه حتی توجیه منطقی.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/82925" target="_blank">📅 23:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82924">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">لطفا موقع بازی های حساس دنیای فوتبال، شو های مهم و حاشیه های بولد قیمت دلار رو ۵۰هزار تومن تصور کنید، تا کیر نکنید تو مغز جوون ایرانی ای که تنها دلخوشی هاش همین کصشراس اونم چون دلار گرونه نبینه، نکنه، نگه و...
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/82924" target="_blank">📅 22:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82923">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سیگارا وینستون جدیدا بوی پهن گوسفند میدن</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/82923" target="_blank">📅 22:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82921">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RnOrXc1g7UaF5B3Ak8XvuJ1iU2PC9r7cSf5zHoyJupoS3htfW9Re4dsfq1zss1FgVwBumdy7rFYAViSMFrvdrkL8MuOTZDFK5z6Gy3qgMMffnOZTY-qkBxQwW7ddrAD7I0KtwDGeHNrWvlN1Ho8L24IW4oZmX9B2Keq2e491S9FlnYN-XjbOAi8nNYVmY8vMuww3bpuIH-5AN4cERvQwyalDdJgaOmOVevBuRsNn865QrPOPE6vlYQsHj4wyqoLCair5YkTUDOeTB407LoWMvzM_3X_HI5wc1b1jSqGMdYWimR_UrSic_TpkFqiwGM2mjWiisePpwflMuYROwuD-8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/krlg65Qk7sMKC_7AhFnAygTKfp9k_dsZm_Y84fPHMoi7ZxqrGLoPuv42IY7p4D9zQc8ysVq3usDAinM38tbBs7GtBt1cgShLZQoKhdIuoOy5TA3KTX_mLdbtZ0XFvbiLacqQ-z92V0Te84GW_0qkuDxJdoUpeEVPsOl5Sc-VUDr1cZq6sCFOhzXhFOPwMJ_m1AKgkoA4aaFn3YFzPtMx8TDLRvU4saiIjr_RU866pkMKJ4DpsLvN98630e-1s7E76FpcpPCuarbQ3rO_XFYja9A7FyBUvF1R8z8Olsee_eS40c6Q9ze3mNXZryMs3LStx66XS7RV0gHTDC8RrKuVbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شاتای جدید لنا.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/82921" target="_blank">📅 22:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82920">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">خلاصه‌ی صحبت‌های امشب دونالد ترامپ، رئیس جمهور آمریکا درمورد ایران:
تقریباً سه ماه پیش، گزارش‌هایی وجود داشت مبنی بر اینکه ۵۲۰۰۰ معترض کشته شده‌اند. و اکنون می‌شنوم که احتمالاً ۲۰ تا ۲۵ هزار نفر دیگر نیز به این تعداد اضافه شده‌اند.
به نظر می‌رسد نزدیک به ۶۵۰۰۰ معترض کشته شده‌اند. تنها توضیح این است که آن‌ها مورد اصابت گلوله قرار گرفته‌اند.
این رژیم روز به روز ضعیف‌تر می‌شود و به زودی به مرحله‌ای خواهیم رسید که دیگر نتوانند به راحتی مردم را به قتل برسانند، زیرا فکر می‌کنم مردم دیگر این وضعیت را تحمل نخواهند کرد.
اکثر حکومت‌ها نمی‌توانند این‌گونه با مردم خود رفتار کنند.
در اکثر حکومت‌ها، مردم تلاش می‌کنند، استدلال می‌کنند، صحبت می‌کنند و سپس ممکن است یک تغییر سیاسی و انقلاب و کودتا رخ دهد.
اما در ایران، آن‌ها مردم را می‌کشند. وقتی مردم برای اعتراض به خیابان‌ها می‌روند، آن‌ها را می‌کشند. آن‌ها با مسلسل و سلاح جنگی، درست به چشمان و سر مردم خودشان شلیک می‌کنند.
خبرنگار: اگر می‌خواهید مردم ایران قیام کنند، آیا سازمان سیا را برای مسلح کردن ایرانی‌ها اعزام خواهید کرد؟
ترامپ: من نمی‌خواهم در این مورد حرف بزنم. دلیلی ندارد چیزی را افشا کنم.
یه سری کصشعرم درمورد حملات محدود و تنگه هرمز گفت که اونا ارزشش پوشش ندارن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82920" target="_blank">📅 22:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82919">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">چقد غیرقابل پیش‌بینی</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82919" target="_blank">📅 21:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82918">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">0.000000000001 ثانیه فرض کن لیگ ایران ببینی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82918" target="_blank">📅 21:08 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82917">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">این دربی با اختلاف بهترین دربی ۴ سال اخیره
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82917" target="_blank">📅 20:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82916">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">چه موشکی ول داد یاسر آسانی</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/82916" target="_blank">📅 20:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82915">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترک جدید تهی و بیگ‌شگی به نام “رقص اندام ۳” ریلیز شد.   Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/82915" target="_blank">📅 20:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82914">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMbhtoIeWPr6k_D9wRsXkOFJHQ5c2vbax1tdB9Y5hgrBWeq-eQwQyhvhtvDKGaRYpK1wkNW_nwcAiop8PwIq_dwlUfKQ91gOpZKkXm1NXA7BR4HIY6gLDzLn01ywqZLvOqrynySE9JriB3qd2HQzHTpQVPch9OKrqVaMdBdM1Z3HXdE9g3MZiGEd5aAEmh_S1TFKLl_YYdopHG0gKg0hyZ6S4DbukiIFGQedUbFi9GBgh2cLT5SdtcGQrdo7aOctbZGeE8V6_Nv0ud-2YiH0eCemMtC--Q8UC1E53dfQZR0MT8VtXmGhE-4uIagszkmKZcUfBIzIH46XiMN_ZiR5ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید تهی و بیگ‌شگی به نام “رقص اندام ۳” ریلیز شد.
Youtube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/82914" target="_blank">📅 20:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82913">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cHI2BZ2IB-t2YnwngJsfn5G2vLSN7K5QLJmDsQfiS1vy7xU_vqj1xmlf_lQ7PAoyXzVvFx85gLpmYrdWu5sFTn9LlqEDd7gTQMQWBij-NcjzAvr23SxL4qSRsZpsqY7lqx52fO2KotcMTzViSaNjQmCUvqeV-Et8D6YG6OHI06fegrYsNzAgZ0EmusjC2PEdnSly8NPFH4tvJENsUxpAAkOYffI3wPpjzhILnlGus3iuWC8fcty-X1aBnkRjEYmL8t8R44SKcIJaaRjSsWFrRlfYcSl0QwRq-jX26T22Dinf7HYtbKxNhIXrIcVWsp3dWDqWrHGU6tHKomk3hAzPOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سکو ها جذاب تره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82913" target="_blank">📅 20:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82912">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1R8k7jgBe5gl2Ut2yaYzxhWrlhWVduXQ82CcH6JJQJPa5WzzDl2SIe8YWhBlwjfNch3luXTcQ-bc1GqdB8DHSxirfzId7vOSsTuUIh9QwxbsRCl7E2Vvlg2ins9_bj3SfPdTK4pV32KXjTjPkJR13DuQ6DY1zdBlvBvUIzuQudqb29YjmW6HZ7o09hGb7nOvI2yEEQqn_kpzeJuACakG_IH4QMmXqWD3Kwp9rAhXwxCXo4gpt8Axlmf2AZtv9wrEwlOfd6WOxdvJIoKw05d2PV75jjcDCmPnUTUlq9oGRySGq12y9q_rJFCgBwy13dg2-LfTOhuhkx9x6j5VaCcAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمایت استقلالیا از دکی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82912" target="_blank">📅 20:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82911">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پرسپولیس از کون آورد که نیمه اول مساوی تموم شد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82911" target="_blank">📅 20:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82910">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">بیرانوند کص ننت</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82910" target="_blank">📅 20:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82909">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">خلاصه دربی تا الان: آقاسی به علیپور میگه بیا گل بزن علیپور میگه گوه نخور
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82909" target="_blank">📅 19:56 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82908">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">علی پور
😂
😂
😂</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82908" target="_blank">📅 19:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82907">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">موقعی که پزشکیان زنگ زده گفته دربی باید مساوی شه صالح و آسانی دستشویی بودن فک کنم</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82907" target="_blank">📅 19:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82906">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIf9dGRLBPHi7TBFyu5P9cE3VfXETK69zpfqVIz9zR7a0FgvwEQvCTroLKKWZOK4lkwt1DuZ0y5Ha5B9ZyTUOiMgZHRP303X0doAvpI8p9926mu3hMLPSoCy-nATZiVpIeJ62U_UDxpFU1jwEsVkXf8W36HnfKn_XEvh_5UF_QtqIzh6Qel55UeemWqvBMhoY--C1o0wHKXaNrfjeM0n3wXdGZ6WDFqwsIgFCVAy_C45jRr_vNIUWdvg6W_31hm3_WQaGs9y6fWIbCBcFsiLnkn1u6Dn5e6siSAS2p6EXnXNxmBaCRnCr6LVhvkhV41KHUfstCkWnxLpk6Je8Icx5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رافینیا مناطق خاورمیانه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82906" target="_blank">📅 19:16 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
