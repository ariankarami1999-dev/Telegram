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
<img src="https://cdn5.telesco.pe/file/tRDeUf4nd-Hd2dQli_4ieI5g3K2y7QIDthao4l0wpJEiRhAPgQmfqD0tQpclN2B8KMteoXTmcIFCWwQ3rYFWJX7kBPaSpOyUIuWt1xLsSkYi6DTpx1W6gLgcJbY5Y314h_tjhRgvrwLW8mdkmYD2gChVXAN0XDwEWnH7NgMQ9HeNCnwwsAw3xWG6f1jBCyCtu37CDRltWicqak5h0aLXisJdgJ-C8jLcOAaOUyd0kYAONl5x354HcM6ejViEfo-jH3w9Wz4Xi8IGvmySLS-aZobiSoomXW_wlsTVkTK8pIvarPN2p7so0LG1kkgZrnAJamWvjI8gTaRJUvlreJ7mXQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 526K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 19:05:58</div>
<hr>

<div class="tg-post" id="msg-102010">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/746abba13b.mp4?token=mqYdcIYIzVyM9bDqsdKHcKy_xjiGNA7B_L5y_PpEEshQsO6F2aB_Gy7aLImwU0QDoXJy00e8DPqtXuLIF9ZgLcjWojmAMebyEWKrp4lN3UdNP33b3i1Ky-tEFBP0tl5DSVJZKdrl5nXxrIIm-Yr6JrTX_oal_YOji5Bn3m1b_U3Ov8iJ9oj0hY40NiS3nL7ZY8922BnY4k2HRnKlZz1eJbx2koxerZ9hYF2w7YGakhhk6MKWvH7bSTt6fwrldsVnfao0lDmARpmLRLvOJqOa8RhXKrrNdBWEJq1NWalGar5YsSeYTCnJ7OfbRcSUhsnWFtsroakwfH1f-TeAlGXY0kGiVdNHGYr_uHyUkfN0VmJtZSa-3ZdZ2bcvNilky1kx-pWIPxMjkan_Zd_KI3A58bBcwZxWZ9P8oK7QjcDp82-s5b_j1mnd4MOrGtnaXbzYV6FCZOj-E3eavlnkovqOV0apEquP-2t5XAmBErCB2VzeV2eH8lGCeWym3oGjVpb2d0X02sspiA_1xwaypu50f_s66BAb2cuEHWqcI-1v9ra1qqv310j8DJfwdfDdMGS0IEXX0S5KrXjGCzJve3xa31LPKajVab5wNtFXdYJ0sCJL9zzEAcnyETcWMrxw6LyMs6X5OHhhnWJmJ-OisZy1M73sWzMMO78T7FLdFA50Z5Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/746abba13b.mp4?token=mqYdcIYIzVyM9bDqsdKHcKy_xjiGNA7B_L5y_PpEEshQsO6F2aB_Gy7aLImwU0QDoXJy00e8DPqtXuLIF9ZgLcjWojmAMebyEWKrp4lN3UdNP33b3i1Ky-tEFBP0tl5DSVJZKdrl5nXxrIIm-Yr6JrTX_oal_YOji5Bn3m1b_U3Ov8iJ9oj0hY40NiS3nL7ZY8922BnY4k2HRnKlZz1eJbx2koxerZ9hYF2w7YGakhhk6MKWvH7bSTt6fwrldsVnfao0lDmARpmLRLvOJqOa8RhXKrrNdBWEJq1NWalGar5YsSeYTCnJ7OfbRcSUhsnWFtsroakwfH1f-TeAlGXY0kGiVdNHGYr_uHyUkfN0VmJtZSa-3ZdZ2bcvNilky1kx-pWIPxMjkan_Zd_KI3A58bBcwZxWZ9P8oK7QjcDp82-s5b_j1mnd4MOrGtnaXbzYV6FCZOj-E3eavlnkovqOV0apEquP-2t5XAmBErCB2VzeV2eH8lGCeWym3oGjVpb2d0X02sspiA_1xwaypu50f_s66BAb2cuEHWqcI-1v9ra1qqv310j8DJfwdfDdMGS0IEXX0S5KrXjGCzJve3xa31LPKajVab5wNtFXdYJ0sCJL9zzEAcnyETcWMrxw6LyMs6X5OHhhnWJmJ-OisZy1M73sWzMMO78T7FLdFA50Z5Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی فوتبال تبدیل به یک فیلم و اثر هنری میشه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 537 · <a href="https://t.me/Futball180TV/102010" target="_blank">📅 19:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102009">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIJgcZvLa0gMwKEiZAkvr1tMRnw1Ltcr_u4hwmDGtYL65hCHatdAshi1vS5X4ttHwW4I7nkuPZ2wMR6VDipfn3x-S4F-Ynv3Sp4O3WJbHCclm_7_VFXuCa8AQENUmSOSHqH8IILfBh5bGveaa1E6ItjE1iNhRQo-9M-9k-fKjsqEC7qO0UlPEKn1gihBHdOq7X91s-LJ77QEw68WvWfdjTui3aZw3XVMcz0YIdoIgDC7bKddCXUX_OAxvGoOBdNLlupsQD2Ervj9FScK4eBO2UDJZJId9lxTB1xndfXX5sOvS0gr0L0QGFKbMn-HGV_YDcEu1F83iZPXCTaMvRhCyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
اشرف بن عیاد:
کار تمامه، مدیرای بارسا متوجه شدن که موضع اتلتیکو برای فروش آلوارز تغییر نمیکنه و نمیفروشنش، حالا بارسا منتظر واکنش آلوارزه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/Futball180TV/102009" target="_blank">📅 18:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102007">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UIHnPOoptWCncUchqpThs5Th1LLaMpp_xeIySa6rIc4R9r3CzKHiINeANATFJtvioauaLJo92eIDyIJ39x5d4YPIXON2EnMFtqkrnkvL-oD2bKpmRGabgbu8KE1qq-Al2J-j-w4aJj8kgP6pVvVwkImfu9OzxEi4kYoPZh7YvlXsa3wCgybqQX4k9INCe6OhqfGcpfkUCQ_HQ2GY1miLCmqyxxZ0RCSjQ5-V2TWQZ0RxuLNrVt2z4iQa70HK9yV_OPf7wKI2Mn7TCRowmPzmL4tyvo0ezHet_f8Tri2nanPWR4eW8Pe_PatZAmFcY483CgDV7svySWzlOTKDPxB1Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jsKEf_NYZme9rf_0-dsh36F5Slz5nMVo8VSz4uInH-0-8Rv-4OAS0wTyZqVPNCgChR0cxuTUqIrK-D4DcbTm3nbkOLwgevj7ZyjG3CB-EnA7lCXgAwOLXcF0UO9hea2YkAwy-paOq0MwUNZu3R9rdqSqfSNxDCBo8G46Rtdrbk9cG0EHQ7EtnpNGHDu5VkatNDsSOOhH3mP_EmZkfOEVATP3q5w46Ib1IlD3n1koR2Uhkuf4_z0vyEaecVfR61kym1voUBG-6iQr16bJ832AJAv895UntqEtPNerWfYWcvA8CF9gca1S0zs8WjFfn-4m4tSl5eyKP8G2K5m4z6G4Pg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
تاریخچه رابطه‌‌های وینیسیوس جونیور:
• 2021 —
🇧🇷
ماریا جولیا مازالی
• 2022 —
🇪🇸
اِستر اکسپوزیتو
• 2023 —
🇧🇷
لورنا ماریا
• 2024 —
🇧🇷
جولیا رودریگز
• 2025 —
🇧🇷
ویرجینیا فونسکا
• 2026 —
🇧🇷
ویرجینیا فونسکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/Futball180TV/102007" target="_blank">📅 18:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102006">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac77f90860.mp4?token=TbismWjMyqEiiJN8Yu29KIYBGDT8iLFKBBHlJBiIJpCKEmLfHAWW2fzsXGCdkfxQe4FInrAl_MusLkeT7fkNwEkolMZytqcAioAD3A8RkuT_eHdxiaxP6C8LcHrv4MWIECFvH9Jf6RjOdVqYrGNH7E9tFQlLKswnHoEin6q8AmJudF7zhfv2phfhS8IM5NLO27jpfC1VWU42VXP0yutIkeMegdFPRmusONEQS-IJ8IkJiadMKVgoZ0ZwygEsZ3T6Gk-QA_xJJYKh0yEJ9oXbifkzCmhvL6jrOoUUix_9ccdfIzFT5O9c18SzEw0PmtmWWX1wkLp7DFzypBQjcF2I1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac77f90860.mp4?token=TbismWjMyqEiiJN8Yu29KIYBGDT8iLFKBBHlJBiIJpCKEmLfHAWW2fzsXGCdkfxQe4FInrAl_MusLkeT7fkNwEkolMZytqcAioAD3A8RkuT_eHdxiaxP6C8LcHrv4MWIECFvH9Jf6RjOdVqYrGNH7E9tFQlLKswnHoEin6q8AmJudF7zhfv2phfhS8IM5NLO27jpfC1VWU42VXP0yutIkeMegdFPRmusONEQS-IJ8IkJiadMKVgoZ0ZwygEsZ3T6Gk-QA_xJJYKh0yEJ9oXbifkzCmhvL6jrOoUUix_9ccdfIzFT5O9c18SzEw0PmtmWWX1wkLp7DFzypBQjcF2I1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خشونت بی‌سابقه در لیگ‌فوتسال بانوان برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/Futball180TV/102006" target="_blank">📅 18:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102005">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8T0-m3-l_47fWziFMWHtMvtcAR6O7hoOSBXkZqsUJfEjHipSMULu-hRUMdy19PgiiqPxKlPwNk_uUsOnrV7sXbdoZwWbv7jimu2BP7D4_SVEhZWZA3hlk5sSx29udpBVfZX9xvCXrt3cxCxS0p9f1dCRLIl5X-MoV5OjcmN3XwOqdLZ1-TULp9oHgVN9jZD3ZFLDTMGoVvzzHigzVoEP6wGHh7x0HOnUqQ4PYNYPjpj3l-5D6iBq7DlQ2E00IBLTGrDvQTspHCjkL7urO1-yON78CyJwPrYlNrqLKoLZOYGUMV1JJgzQB5TrrsawBSigDzvbKhNTQPcfTgo5YYCLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
🇪🇸
رقبای احتمالی رئال‌مادرید در سید یک UCL که با دو تیم از این تیم‌های در تصویر بازی میکنه
🇮🇹
اینتر
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچسترسیتی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیورپول
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
🇩🇪
بایرن‌مونیخ
🇫🇷
پاری‌سن‌ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/Futball180TV/102005" target="_blank">📅 17:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102004">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aeu3x3LqecIwWT5CJHUg1J-s-O0Z_08mobO6ZZM7BhAj0zefduRprtXOccwn-plaR8zEw8ubMX8VH61-_8MJm_vyAWCnC2QBpTNxPkbKGmTa8UIzoD4_bwPKRM7NLMeZfZ4EbKK9T5C75dNvwzYkKEtf5F1Wv9n64YFZ0Eh3bzX83VqR6dtmtJ7UshprpkyFuXGEuuCXvITRQbIO-GD6SbRpGEOwYDo9WhymSxvM8lrk_PSTB3jhFXAztOS7VY3kmOfDTRDJ7TiovZ6aU1caShm76FWXmfvMV8YEQKjEmM94DHt54nuZN4oNcs2nrbMON9UhW05ZJYmKAppLUPRITQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
متئو مورتو:
فولام قصد دارد یک پیشنهاد بزرگ به رئال مادرید برای جذب گونزالو گارسیا ارائه دهد. آربلوا می‌خواهد او را به تیم خود بیاورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/Futball180TV/102004" target="_blank">📅 17:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102003">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYTjPaOmIPquHLUJGz5qNnMC5n-y5mUOjOzdUBNFSc8arN9gmBi2mfoFgnh84ocRgUoW16D3LCyBkDIcX-ox-bGNcyjZnaTBYIrZlaagEmdMAIxXKPS7boHiZKYzemVyFU6tDtVieARS2v-uB_TZ2JXOsG9NQjQqIWwu41t1IMXbaxpnC_8bqsU4kdLd5hix8Ham7vVqD3-D7NCrPguaPhUU4SwfUzGHZPT45geQR59vge3YuISUsY2PYhEErYg1rllHNV2YrfwmYl7_4RBJgDfQIJqsLh0QG4Mpc0-2nylt679yiRGNdCEG7emy6L7dVPVNcTLnEEAq5ezEOz_ulg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سانتی اونا:
باشگاه الریان قطر پیشنهاد خود برای جذب جیدون سانچو ارائه کرد
باشگاه قطری در تلاش است تا وینگر انگلیسی را متقاعد کند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/102003" target="_blank">📅 17:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102001">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🏅
فوری؛ لینک پخش زنده بازی پرسپولیس و پیرامیدز مصر گذاشته شد
💬
@squadify_ir</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/102001" target="_blank">📅 17:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102000">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9608d1c2fe.mp4?token=rcAVThDAyXT1yIy4rjoackv0hfVqOAWKpDbDEdg4dgqsh1sOWrZxcStyBUPH3O7ODSuq20-k_Z0h9qhtwujZwtWOcRhc8zIAyTcuL4lrt0BEUvEzA64SHTl0nu6DQDoicTSE5Pfat-px_iJIcIzwsTyY2Jb7l3GAJwv7ANXub2ionw0YpdhwEa3SyY6TKaJI1VjgcHYeFdZayL_3fhHI0V68GYnqXdkerlm-bI4YBs50Zm5V1alAqnXXGlScNOa38ZA2p5bXoQ1k8BN9ghe4PmmCMRQjAi17g07u8jOfvDqTN6ghOzbZRloGjiPP0Fr3T3BKdH1aj2LEB5Tvecz5eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9608d1c2fe.mp4?token=rcAVThDAyXT1yIy4rjoackv0hfVqOAWKpDbDEdg4dgqsh1sOWrZxcStyBUPH3O7ODSuq20-k_Z0h9qhtwujZwtWOcRhc8zIAyTcuL4lrt0BEUvEzA64SHTl0nu6DQDoicTSE5Pfat-px_iJIcIzwsTyY2Jb7l3GAJwv7ANXub2ionw0YpdhwEa3SyY6TKaJI1VjgcHYeFdZayL_3fhHI0V68GYnqXdkerlm-bI4YBs50Zm5V1alAqnXXGlScNOa38ZA2p5bXoQ1k8BN9ghe4PmmCMRQjAi17g07u8jOfvDqTN6ghOzbZRloGjiPP0Fr3T3BKdH1aj2LEB5Tvecz5eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
آنتونی جاشوا، قهرمان سابق بوکس سنگین وزن جهان، از آهنگ سیاوش قمیشی برای آهنگ ورود خودش استفاده کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/102000" target="_blank">📅 17:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101999">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57f6f418b4.mp4?token=Ha5UTnkC93OXRQ-DqbtW1aMn3qvpwxXAo1NY1sNg8sqZg3Pz4yW4UsTpFtEC8AwmpH0yEy6G9ZFvhOeVYIjcDK6bxBhwzVor0qzco8CWLWRhBEyDOIo185Kb4dKxQpH2GT0xUF-f6zXGZKb1M5iUvf6v3YCC66oltJdDk6eVof1dP6g869gxdM_5koSVwuR36zI6MGJkYZ8L4Oaj7XpgXJgTwHYi2Jxb5wwnOMY633_jWbUeBP7JBE7gmDk9o1G0eVn7aenlNMQaniD5aUYzbyYJBDD_y3lawC29JveOlU3DVGYyb0a0vrRvdICHBaNNNtsgcUt5Iaj-6T-1EIcsAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57f6f418b4.mp4?token=Ha5UTnkC93OXRQ-DqbtW1aMn3qvpwxXAo1NY1sNg8sqZg3Pz4yW4UsTpFtEC8AwmpH0yEy6G9ZFvhOeVYIjcDK6bxBhwzVor0qzco8CWLWRhBEyDOIo185Kb4dKxQpH2GT0xUF-f6zXGZKb1M5iUvf6v3YCC66oltJdDk6eVof1dP6g869gxdM_5koSVwuR36zI6MGJkYZ8L4Oaj7XpgXJgTwHYi2Jxb5wwnOMY633_jWbUeBP7JBE7gmDk9o1G0eVn7aenlNMQaniD5aUYzbyYJBDD_y3lawC29JveOlU3DVGYyb0a0vrRvdICHBaNNNtsgcUt5Iaj-6T-1EIcsAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
قلنج‌گیر معروف ایرانی که با درودافای مملکت ویدیو میگرفت توسط پلیس بازداشت شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/101999" target="_blank">📅 16:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101998">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a860d22dd.mp4?token=YTFs1ga8mOOWX2hR-qtbHiQaoL2m-MoNb97gR4e5aXRoHpq1UyvTxV8N9Mx_WGSb2OuQPd_7DzQ_Eks3LrjoGD_QHBN3fRIbU-RN9pMtYS7yTLjV2YGKblqqhAZmm01PCvl5vQARYSg0OBpwNCbjCcsKHzb4Ot-ai8Jl-kBFhgTImNZKqDQPYPlyay7NSZ7OSeYMNxZ757b_jrt3LTjB_CWRxzmqEhf13ucue-S4im8o68XVDxIu0IOyyQ3wTaTbi3wtaSVxVhxp7Sv7z9cGsaknL7FQ6hNStdJm5LpeiKP34X0KwDCyF9bofZ-WSlskXwWctPl2E4ufaaEVrZIUaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a860d22dd.mp4?token=YTFs1ga8mOOWX2hR-qtbHiQaoL2m-MoNb97gR4e5aXRoHpq1UyvTxV8N9Mx_WGSb2OuQPd_7DzQ_Eks3LrjoGD_QHBN3fRIbU-RN9pMtYS7yTLjV2YGKblqqhAZmm01PCvl5vQARYSg0OBpwNCbjCcsKHzb4Ot-ai8Jl-kBFhgTImNZKqDQPYPlyay7NSZ7OSeYMNxZ757b_jrt3LTjB_CWRxzmqEhf13ucue-S4im8o68XVDxIu0IOyyQ3wTaTbi3wtaSVxVhxp7Sv7z9cGsaknL7FQ6hNStdJm5LpeiKP34X0KwDCyF9bofZ-WSlskXwWctPl2E4ufaaEVrZIUaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
اسلحه به دست منتظر آمریکایی‌ها
صداوسیما: مردم بندر جاسک به صورت خودش با اسلحه در ساحل قدم میزنند و در انتظار ورود نیروهای آمریکایی هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/101998" target="_blank">📅 16:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101997">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABp-pRvAxC9MfXrpuRZ_Yoo3p3FXoRok4mP0oGP7kKFdT7CrmRNqdzyVwZongLv95toTghQWfAPXPUW8uIVdenzZR1WeU0fI64THI-zA-rvyh9L_sexaqKKQ0fNS0SR8TgDVtb7CWLvEESFP4bstqnDz3KAwNUNRK60lcfYq6xzATUOq53CClkwXn4wYOVRdy0dZ1lDrC03HF1VH4ro-2o-PPf4VPAIF8rGnC43hBwSw8DsbU8E4HsAc9dKbSxi8MzSZDRD0JdR4WpkbsLo2fZ_dUw5bVfeVBXRCnDI8Spu0qpVPGQ7G-bahO4n2AHyqzSChBvzhIJNzG3uhxbtUQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنانی که با همسر یا پارتنر هم‌تیمی‌هاشون وارد رابطه شدن:
🇦🇷
مائورو ایکاردی و همسر مکسی لوپز
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان تری و دوست‌دختر وین بریج
🇩🇪
مسوت اوزیل و دوست‌دختر کریستیان لِل
😀
تیبو کورتوا و دوست‌دختر کوین دی‌بروینه
👀
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/101997" target="_blank">📅 16:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101996">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58250e2a71.mp4?token=GBshSmjeV4PYubMCaplOfvWid7iNU-N_B9iFMqXKVGb8dPDA43Ks5CSF6PlMc4g7909P4tMA3CGAbwF6x4QP-PKM3S4hJKMEfsA3YXgjqRQnxUf4hjWHh0_rwfHmQm-8eSRszH0LfB1RU-imSWwoEjmTdt0Q70jabG482CSCUryQOfgACFUd5v1Z6ppF4BHhBGQCrJ1xQ_Vti4CYxvua8kLf9rRvtKwwnUpkRukGFmyqB1qhkGjOeYozBcbFahW_NHa0GvFuBalZcKKp6Blm8TnD3xc8zpRyfi6dagOL5LDvVdY-n6eUe6-QXdhsZfL6gKno-hCgkvKgQWmW14o0jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58250e2a71.mp4?token=GBshSmjeV4PYubMCaplOfvWid7iNU-N_B9iFMqXKVGb8dPDA43Ks5CSF6PlMc4g7909P4tMA3CGAbwF6x4QP-PKM3S4hJKMEfsA3YXgjqRQnxUf4hjWHh0_rwfHmQm-8eSRszH0LfB1RU-imSWwoEjmTdt0Q70jabG482CSCUryQOfgACFUd5v1Z6ppF4BHhBGQCrJ1xQ_Vti4CYxvua8kLf9rRvtKwwnUpkRukGFmyqB1qhkGjOeYozBcbFahW_NHa0GvFuBalZcKKp6Blm8TnD3xc8zpRyfi6dagOL5LDvVdY-n6eUe6-QXdhsZfL6gKno-hCgkvKgQWmW14o0jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🎙
علی علیپور: حتی خود پرتغالی‌ها هم کیروش رو گردن نمی‌گرفتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/101996" target="_blank">📅 15:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101995">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4Qi7qBDCosFh9mQDSgLEVG46ZPfLyniBSxV65GvYdqKrYVlZodmwuGgBeTPXiJVCn0ri9EOoi5K-k--esPw92VlU9sc2CiuV_3GDSW5AkPhapy6lUHDnjiASwz54vi72m3gfyjQmt90JLF11ZCpcFBjjkiUtIIJo-VpqohctZjzUzq-apegTfuZ-9YuDYDfscbX4BFPx0b5-6kXtQuKx8y4oJiCyrP0eG7svtAHx1ffWXJ3iXDOZPm60_zlHElIj-n8PlnP3XW6jdjSj2DKzOcojZ3wMN0tUfwPa5RvoMg_kU4jGiPNHlYdE_6goDRFC994heCZnff43_0wB6ItGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📉
می‌دونستید؟ فقط چند هفته قبل از جام جهانی، اینس گارسیا، دوست‌دختر لامین یامال، حدود
۲۵ هزار
فالوور در اینستاگرام داشت. از زمانی که با لامین وارد رابطه شده، تعداد دنبال‌کننده‌هایش به
۴ میلیون نفر
رسیده است. فقط در روز فینال جام جهانی هم حدود
۱.۵ میلیون
فالوور به دست آورد. همین رشد انفجاری باعث شده چندین برند بزرگ برای همکاری تبلیغاتی سراغش بروند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/101995" target="_blank">📅 15:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101994">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🔴
فوری از رومانو: لیورپول در حال تلاش برای تکمیل انتقال بارکولا است. این بازیکن تمایل به انتقال دارد و اولویت خود را به لیورپول داده است. لیورپول منتظر اعلام قیمت مورد نظر از سوی پاریس است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/101994" target="_blank">📅 15:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101993">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZnE2pk8xWfK8kaX1EUhJxXjaFdzzCvaXZhWlo7UrULxUEoPd3XMxlMYXw7DPjqH0yryv1HPIsJY8DTbzJ4eH4VLz8tSZVjIbcFFswFIEW5ngY_44KuS45pz9qkPCPjfiU-V292VaxQL_qqT5yP7WnjONzyJWtqlaH0o_Emtf5Hk-wXGYj__oTVbdq3ufOzBm8r_mFsOvEtSvgsexVmoRFEBi2EW-f-NNIzQqRSwRkV751EQsDG_cZK9aIWD2sY-jI_BQNmxzqxmmEMmV4qoFnRK_Mo8IOiLS-TaHV9-BnqlGWa2PmShTBULP-ruFNiGkBE-dSesgKnLQ3I6k7jLqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
فوری از رومانو:
لیورپول در حال تلاش برای تکمیل انتقال بارکولا است. این بازیکن تمایل به انتقال دارد و اولویت خود را به لیورپول داده است. لیورپول منتظر اعلام قیمت مورد نظر از سوی پاریس است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/101993" target="_blank">📅 15:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101992">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45e9d378eb.mp4?token=Zx4z_I_QaQRpEqemvT-zEO7CIpyT6oHuQk3i3105fRggopLN6tXN_D0LNdRCAJsTPLaFjVbLPEr3u3n7uVlCjl9KxC0dUlVTsg0ZS-zB3CHMEvKL65Wxl-7p6Ne6D2sYOWSM3muW_onSZwOXEvsNv4m-FA0HZuJgCA9_VorQOwV_r6k1qIsRs2qNPKhif2JnUsLWptvf2v5ygXyx7wpMv5Q0wLDwF-TKUPX_aP8IjgJ-9QASPpmjd-RWN1lGtvijpmbq_tCFjkjMuj3vVrmV1zlkTWTAHx61EF49hoDL0rzwM9DsEfjkGhfkrN2L8xyjEteb3k7YBOZU1OiNTzV1YC4r8kea-dzDDUtMe3GhVg4ANqxlZBh9qLsBetfNkuapLiQkVh7q2_RnKprPDEbxZeFSMomceF8kwlBOT6lIVfVzAL0R5ES7yM8Y6sR4DLxe3XIA2lx7byqW0IoWSHpMVYfjwVbZY_pS3Fy-6WuQ5Xqm0nfQrytqgf9lDHNwMwgcy50oJSCSZtwDxNT5wVc-XmfhIS2y7FQOjmk59tNMsREkU5m6EUP-K5gQMuAv83gGa1_psYdtr8kv4EeIlNmzHNDM6tR_LczZOfjQysQ5DcnnSpltjZKQvfMgX70JahX_PE5DrIjaTdGvibbSt7alL5m6xnXA2SFSbR1Z_awDX-U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45e9d378eb.mp4?token=Zx4z_I_QaQRpEqemvT-zEO7CIpyT6oHuQk3i3105fRggopLN6tXN_D0LNdRCAJsTPLaFjVbLPEr3u3n7uVlCjl9KxC0dUlVTsg0ZS-zB3CHMEvKL65Wxl-7p6Ne6D2sYOWSM3muW_onSZwOXEvsNv4m-FA0HZuJgCA9_VorQOwV_r6k1qIsRs2qNPKhif2JnUsLWptvf2v5ygXyx7wpMv5Q0wLDwF-TKUPX_aP8IjgJ-9QASPpmjd-RWN1lGtvijpmbq_tCFjkjMuj3vVrmV1zlkTWTAHx61EF49hoDL0rzwM9DsEfjkGhfkrN2L8xyjEteb3k7YBOZU1OiNTzV1YC4r8kea-dzDDUtMe3GhVg4ANqxlZBh9qLsBetfNkuapLiQkVh7q2_RnKprPDEbxZeFSMomceF8kwlBOT6lIVfVzAL0R5ES7yM8Y6sR4DLxe3XIA2lx7byqW0IoWSHpMVYfjwVbZY_pS3Fy-6WuQ5Xqm0nfQrytqgf9lDHNwMwgcy50oJSCSZtwDxNT5wVc-XmfhIS2y7FQOjmk59tNMsREkU5m6EUP-K5gQMuAv83gGa1_psYdtr8kv4EeIlNmzHNDM6tR_LczZOfjQysQ5DcnnSpltjZKQvfMgX70JahX_PE5DrIjaTdGvibbSt7alL5m6xnXA2SFSbR1Z_awDX-U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
لحظات خنده‌دار از زنده‌یاد اکبر عبدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/101992" target="_blank">📅 15:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101991">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d63baf35c4.mp4?token=fqowHwKHJzDdSFMuW2DST2-RWwL-lbAhOicYnBiwYML6fJnEn-aDLi_JkmPiu5N2eATO3-1nQ_5dyHwq7V8F0y2SaeXvL_7w9oCTnMtjxObF_UX7YkyirmZZ38moMS-8OsrfYxPnwqMjumAKyFaRDXME2evT_eSQK3IZ2yPl1UiY4H3i7p3N4LJ_wP8FN0WeOZi8cv2E2-QibXVFCcMMXES9_JDgDdskPjyLU3--HJFqU7gFgZyMR4Feuoi7oFeAhP8jJN8BL1HXXw3xhj3OxBMhIPCoKlGAH88oRVF-F0WU2qFprhDW58hx-8pEXYGAOXAEXJ7Fx26S9vOfugjJTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d63baf35c4.mp4?token=fqowHwKHJzDdSFMuW2DST2-RWwL-lbAhOicYnBiwYML6fJnEn-aDLi_JkmPiu5N2eATO3-1nQ_5dyHwq7V8F0y2SaeXvL_7w9oCTnMtjxObF_UX7YkyirmZZ38moMS-8OsrfYxPnwqMjumAKyFaRDXME2evT_eSQK3IZ2yPl1UiY4H3i7p3N4LJ_wP8FN0WeOZi8cv2E2-QibXVFCcMMXES9_JDgDdskPjyLU3--HJFqU7gFgZyMR4Feuoi7oFeAhP8jJN8BL1HXXw3xhj3OxBMhIPCoKlGAH88oRVF-F0WU2qFprhDW58hx-8pEXYGAOXAEXJ7Fx26S9vOfugjJTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
دستاورد دیگه تیم‌ملی در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/101991" target="_blank">📅 14:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101989">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fmD6Qk8V2gG-pD0ClVilVwV04PY7XZ7wE1iV5aOOckLY_MPwOa3tvyNbYYGlGZrHkHaPiJ7Bn8PF3w2bcKYyaf-zdYMd03mANFJStqY2Di_kmvBSV34H46274NXbPSq3-twu4c5vdGHF-8geU3dyyNNdJrLInKup05srcL8T3jGdTRHZUqjy2_ip94u_EnzdjmRtdBA86ydOe35B56STmwZQJdFPJBPJpPOAjYba8oVJkOiEtkUBFV6vrL8Tgn2y4FsMSVLSqO77P_b0iSg4Kz7G3s73nidvA2hjbFY_FmOzwMv9vobgN_OsVjjFNGNzp12s4UDb5cYYUn1YPyHYEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GGA_jezv4vipmckUzCKPoZPRMIlaggerESym9tsewcirkp-pxL4-YIkkcD2aFl2vNDFniF_owAa9IjRMXSr6NTQlDc5T2tXc7-9tDTcn6cmoy3QRnWBUmsVJ1fKnCjUsm7xUIY5rBboN6UFhoLrRT5FUD3QjnGb7rvBRHwU2zg5A6_njwO0vWdX7QQ-ut9-TMMKGNOmWvIW5hyRXF_pxRpmNz6PWaV5k-j94i382AKiHq4N8Le9JdHPe728ZC4MgGISEMSJKYlN46-nxXTy_oka208JhUzitHbGoiJAJY1nukIcEAOn1h6j8SMWp7ne8-KUdW61kfc2wixO_VfpUBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
اینس گارسیا، دوست‌دختر جدید لامین یامال به این موضوع که گفته میشد باعث جدایی او و نیکی نیکول شده، واکنش نشون داد:
من به کسی آسیب نمیزنم، چیزی رو از دست کسی نگرفته‌ام؛ فقط دارم زندگی خودمو میکنم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/101989" target="_blank">📅 14:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101988">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/310ebc00ec.mp4?token=H_HMFxGVqIXEFlNoye9rX7UIW2rSD4pNtvkjXqBjzpHLKqf23VMBhvTdXtnnItdy3VMIEeeokNaEx0VS3Abc_fFPF3PuTZ7ri2-j9LIhMtAxGpmfxwiSBCneFxO9XK-jnSh3gKfHveN69jhPUoRaeXGmut1lc5H0JZgCko_cW-LNy2kpf4Wop5cNvxRAHC7rShKexIemSpDxnGye0LkzZYFT4naxiZQgFj0cH1chTa4vnyl-Y2pQL2ftDK1yGpfVAEYVxrQl7lTxzPssUNfq9_F6k6aNhR42p1nU-gnbeeRShbE9vJpLCrlXF6C6LMB2UhCPYNJAsIJVJITLe8Dt3SI1EdBlPVRXrARGrxKNzgeZ3LmJipO04veYfjavJONFCW4sztI-JGUPCfhOpEm1tAr7duOfpNRWG3dbKibQaCydebLU0SF6smoD6z9VVBIEiLWHqj_i2PtHxnQDCV7f2YBvG_LM-hz686xITJnaAysJnrKZnCiCogcN7sRbKSN4oUuemaiTs0KZiQ-nwIPcydkZqI6cBPFAP3jxH60Dt0YkESggoviU7hUcrewHcIqsSM9iBXrR-0W0jvb_7V72c9J-DUMhTeL8SCPniJnTTNx5m8V8Cpr0vPUyKqlWTCaMANn2QGI56dG3wNgutLAC3Bug9MHTqp3oMPKW3MgFR38" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/310ebc00ec.mp4?token=H_HMFxGVqIXEFlNoye9rX7UIW2rSD4pNtvkjXqBjzpHLKqf23VMBhvTdXtnnItdy3VMIEeeokNaEx0VS3Abc_fFPF3PuTZ7ri2-j9LIhMtAxGpmfxwiSBCneFxO9XK-jnSh3gKfHveN69jhPUoRaeXGmut1lc5H0JZgCko_cW-LNy2kpf4Wop5cNvxRAHC7rShKexIemSpDxnGye0LkzZYFT4naxiZQgFj0cH1chTa4vnyl-Y2pQL2ftDK1yGpfVAEYVxrQl7lTxzPssUNfq9_F6k6aNhR42p1nU-gnbeeRShbE9vJpLCrlXF6C6LMB2UhCPYNJAsIJVJITLe8Dt3SI1EdBlPVRXrARGrxKNzgeZ3LmJipO04veYfjavJONFCW4sztI-JGUPCfhOpEm1tAr7duOfpNRWG3dbKibQaCydebLU0SF6smoD6z9VVBIEiLWHqj_i2PtHxnQDCV7f2YBvG_LM-hz686xITJnaAysJnrKZnCiCogcN7sRbKSN4oUuemaiTs0KZiQ-nwIPcydkZqI6cBPFAP3jxH60Dt0YkESggoviU7hUcrewHcIqsSM9iBXrR-0W0jvb_7V72c9J-DUMhTeL8SCPniJnTTNx5m8V8Cpr0vPUyKqlWTCaMANn2QGI56dG3wNgutLAC3Bug9MHTqp3oMPKW3MgFR38" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
چنتا سوپرگل نامزد پوشکاش ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/101988" target="_blank">📅 14:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101986">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KrHqV0Tg68Un3shsf_WJkWdaM9zgKeJrcGgWQggleuV6pSWHZc4yFHBnSSEIlVAuNawgRCXCRxjb89MkcJhf0qdqdQxDtJ-gLZLNK4E0GISkD-yMmwYgYRxQiwabAPAEOc3kO99VFfa-A76XenDHTfIUGHBf5ZjOtJWAYUXvNrFaSi8ToPOwHMq3uz9fBkprwoGGeM4SQZluWMe03pLWfmsEgJCwsiggBnjYV1gG11W5GznhRnmRJ6JmBEgVu5HgtHHUvaxoUg2F27TpdI8BIZNSbp13Lm_Y1p6MSwUm67urw9ddU5hGJpMkekm466aNl_GFzv1Ytv3F5mgaCfH5yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uialL1mv6dUXR2_hWVGJEUci8y2wRm-b78GTXyUKSn6MFmNsJQ_asxsqkIFPYmGIJeb5eY5wqznPf-ZXrOYhzlpi9dDxGp3xNoCNyXFFHLydeb7PdPwQegxVOmdUkALgvnX4icJDQnR1r91loefS6qfk0C9_cnhzTrGDWhgxhfxEYJsrsN08lKSGUFU7iypbZRmKJaaUzPFWXOmZF1hn7wq6bBO0HbO-samXmMyGUcbNQz3vw9ZC4MocIq-EDftk-RRhabKCCsRLqkjTna2R6BU7LuwIOEW-YdeY4lRmKupTach-lhoZ5OhevkCXtVdqpExCjorTL6VO3TwhaMA01w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
تاریخچه رابطه‌‌های لامین یامال:
• 2022 — سینگل
• 2023 — آلیسا
🇷🇺
• 2024 — الکس پادیلا
🇪🇸
• 2025 — فاطی واسکز
🇪🇸
• 2025 — کلاودیا باول
🇪🇸
• 2025 — نیکی نیکول
🇦🇷
• 2026 — اینس گارسیا
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101986" target="_blank">📅 13:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101984">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CjzplorUJdOOeL3o-seugnWW1WsTP83233W5YuDO2P43MSRE_n1r_r-0tAou42RE2m0KRLtX4N1HPeGF-vMls6RBP_qETS_nrpJ0lTqbtTdQOlEjYNE086Gbsfs5zzmd_ylaG3MqPIvSR9hXC6xoD7XDf9a4d6QgvRYNb5vqIENEJV3BQzg9gx2QoO5GyoeRgr2CXyToIWy5kWZqG5wFyyiVgCv_qrEUbrBwFQdPPhLqBJRFgfl0eZ6YLhybA5PM8hh2eR0D1a6VnDTRcyPKqkta7wniK1zx-dhqIyzSKZmtWrs3xN8daN_YARHyq7JQYk5M4eTNnKKfjBZTkgGFGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QEo4Q1luxdVPcb1LBbhh2AJPmDr5DYt_M_kGELCvhnff8dKPlPXA42bXw31WRwT175gGLBiGEyXYzVvU1ymW7V5RdHPrum32Va6B5RrKZa-j_65vntPhPL3lfC8w-XN3RUd7hX0vNJ8uhsLRaUzx2q5WzS1DgR6I-JoKPwoHgqNa-DnN_3bRPJO2uqHvrKP2uYt6MVtddCiIj7NONfgA44gWjAXV7ZDS1LwGpWP7V6KC7zKm_eNqzd469bP4lWtJyvI8tnZVg8a0XizHcdKCkwBwBiWGm_0sGLTrwXcufAaui85ok62CKAHimfdpYQ5LpbqCrGbGy1TN9ioDYo9TPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
جسیکا توگا دوست‌دختر سابق وینیسیوس جونیور:
این فوتبالیست‌های سیاه‌پوست فقط از نژادپرستی شکایت میکنن ولی همیشه با زنان سفیدپوست و بلوند وارد رابطه میشن. اونا هیچ‌وقت با یک زن سیاه‌پوست وارد رابطه نمیشن یا چنین رابطه‌ای رو علنی نمیکنن دلیلش چیه؟ جوابش واضح و مشخصه! خواهشا این سیاه‌پوستا فاز آدمای اخلاق‌مدار رو برندارن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101984" target="_blank">📅 13:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101983">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
په‌په‌آلوارز: دیومانده به رئال‌مادرید تا 2031
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/101983" target="_blank">📅 13:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101982">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgAGmWD0E5qLy7cmqgUfVKo3ukMbsBO1PWvpyI-0xTSQSPqho_J2GGdJ1DAvFTXUGGVurpFrpMbyHFsbR922xugLrZH1Q9U7EdOIsPaKtEFSw9BluxOl2TCnhIRR4NQ7mn4s0I9LAB-tlWxix1ZJ7qNcGw5VBOG3KU9PZX4_sOPLcJl3Lvolvd5o7Df2GXsNLxh35XmLBJIX_vaHBX9_bUuCVdwpPKs4Zw98WxSahd0V8gvTp0e0GNtp3uvJFweLYHrP3P5ZIti1oReliKRfnSUwJMF6cnZjCyTTQ-_-ZcDvHP9zkU4hWPS5rz4-P9cbeZ914xEvSIObipNkagBQvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
په‌په‌آلوارز: دیومانده به رئال‌مادرید تا 2031
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/101982" target="_blank">📅 13:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101980">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bBfnNlwfE45wA3FmY5xxLhY4kJuAGMsg5niM6c6cFbLZRMKxhQuBr_JGi0OVB4J4urfwLsH7GodsGZqIwgJflBl8q86VjCVvkoDIKMZ1Zq3VD9TW67Do6f15VT1ZpEDRrUCeLzrFm6IwADQ1FwxcMebfjIdP8J6VEULadY3UlLRcT8t7okyBPu9vVFpAyPoLjr_8TllnR6Ow4tD_JUhDtRHAs61vvv04U8DQzienVnVZGBK5WB2JWIGlhS2sOudtfD2qjET19p9U7_rdHGAICJETFxwaaHsPILOhLmVmfgp2XIdylDi6ShRbnyo4tWRv4JTlw2_pBm1hM6UO6oIl9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/huL3Q6923qsMMBJ8BicWid2P_O1AtKEFPzf_B_K3VYYMhM0qJPa4hg7BCf9zm-BNON2pywNQcsp1OH6n-i7Jqbxe_HPWa4TyjKBjsFF0pnL_BWVZS8lqiBvVJY0cZTzb8Xr63ryOyLXKNgUVpd5kXvOujvJmyf4MINUSDUNDi46Uk3QQXa05j_I67toVzZONEwd8P6L6_MxyT_4N_WfGVSkp8BRpYKG2juaqO73JwUbfW7pDaKSRyVjH8itkxG2l-BNbXl1PiQEPavPP6jyi_fNxUQsxmKSm51is0yx73nlpgtrZlomDYnjLyKTryldHX9tBeK5dg7oHLMIVtKIFoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📅
🔵
17 سال پیش توی همچین روزی بارسلونا 46 میلیون یورو + اتوئو رو به اینتر داد تا زلاتان رو از اینتر جذب کنه.
🔵
🔺
فصل بعد اینتر تونست با حضور اتوئو یکی از موفق ترین فصلای فوتبالی تاریخشو رقم بزنه:
🏆
سری‌آ
🏆
لیگ قهرمانان اروپا
🏆
کوپا ایتالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101980" target="_blank">📅 13:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101978">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L5VImra185rPqPT8zjEXlew8NlKZQVtG79R_gbWqyXDwggSRlLl7IeyB4WNRtcrmd25pSjwrJJMnteWTqQwplkIprxmlv2pJeU056w6ftma254Q8foBAnYJMI82scJnqT-jlZHZv1mGLZZcSmnkHRxcRZgmmrfem8Plo6kbw2fNaXP7Y3jdJFvnmSBdLd6nApznu9X6bnV10_Ty4DUqb3bnK2TtmGu4vsHMFwdty3JF4wWQiUZQkfVtLYZXoq6H2VVuqMap0n7YHuObrIMdSzT-S-cDjVu3jBiR6VNIMXpAFGaRIjjS-NUYw8E4Sv4A44gTftVWVSahLwAirJCQsgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OgHMHm5LcXif8AyQaL9reNii9RvURDneJB4xKdkJqsGdjkcuC5Y3FTydkDs89_i-sJW_SR8VOMBLzEHnQhRY0W8JP1RM5l5ap6xPxDGoKpgbKJfukRJAxUAGGmHuDOf60euRoRK0-nPrqu8T5PWIJjmg3_U0P91MFR-Oa7B7VaTmyeeV7wDdwzHEeEK12iFNp6ltAU7wFScEy_agQoCI6PdiPzdOrR7ZEg-dnx56-NvSf9mTpH1qvFujF0P_K4aHHE3-dEXIvUaf-P70SdZMtauwxhTiys4-S5P_BKCOT59ZN3m-_9m5Q2hvTNSzglNuJJyB0thzDEHnCari_aJHVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
الساندرو نستا درباره غیبت ایتالیا در سه جام جهانی متوالی:
باورنکردنیه! پسرم تقریبا ۱۸ سالشه و هیچ‌وقت ندیده ایتالیا توی جام جهانی بازی کنه. وقتی بهش میگم ما واقعا جام جهانی رو بردیم، تقریبا باورش نمیشه. میگه: واقعا؟ برای نسل بچه‌های امروز، دیدن ایتالیا در جام جهانی انگار داستانی از یک دوران خیلی دور و گذشته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/101978" target="_blank">📅 12:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101977">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LONdZmcpaEUPLsyGAY0wJOAzDwnlcYauBuTo8_4JQlCFr9pAt1SLCkTTuXV5Z5kxB7OPobTtJmHVsbE8kwE2MCROY1EciC_gG-hkMU9J8bKG7uCqjcBN3SI-ngmt4q8nUzGPg1vDJ2VKgbKMamUlyepms0QVjWBwD0wxov4gbxQwktiA9YEcShBt0oRILzfxXT1qVcoZqK6MkIYMTBZFqLkApgVwHp5q6K-xSnD0JxRyKjriPSJmt5aEwfqVYWqRwkxOwaKMGcGvhsOgQwgVnPQH1TfHZ9FVb1-ka-JYHWkzQmrZvNsyGBCk2No96n4mL2eAntRMPG4Yek5OiCky6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔴
ترکیب آرسنال اگه همه شایعات نقل و انتقالاتی به واقعیت تبدیل بشن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/101977" target="_blank">📅 12:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101976">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKgkDaKvEYeRHrCTmvFXpUUakjUge5VkcxevSTvVoZmvYJTgCb9Bu7Hs2XpN3UKldu5TTYfHRuhM4bjpmVl4hZ_zwpHKmGMm6JHNw8pjmb60iMdQU2WrNkFFgvOuNFHNLmlUceuPxiiOJ6S8bc-8yNDqCGbS_qD51uFRvRPWRLIEIJkVv_qFSw9JbksFDCg5jIgz8h6viISWVgoW-vkt8rz1kbBidI1vY3VE1SAWXwPMaoStR9NnI6yOz68ulG8xTQbJT4s-Q4kQ0UJXHg9G49HVLEGQdK2R6WI4vs92pMaR4smSpwsnqk1Rn0c-fAki2m0M8AQf_g6S8WlxsGKp7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
طبق گزارش‌ها، بدهی‌های النصر عربستان به حدود ۱ میلیارد دلار نزدیک شده و همین موضوع توانایی این باشگاه برای جذب بازیکنان جدید را محدود کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101976" target="_blank">📅 12:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101975">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ddfc2f853.mp4?token=SibjIRTN1zTqTxZOlZBe_jiSUUmjfO3dKbh5F8PZLlSiGNbEJqUkpPcPj3Y_zIh4nbjknVXMYof3aTuUvfUCfyR1X9PSaQPXyiNav4m8_eOhSdXdRXu452bWc1SuaQl9g3ETGJHh1p3FrGJk1ce8PbQhmnNaEglM0x3N8CvP3iaAPK9q_LxMYBgM7nxg8kieeRzRSVjQTDrPW7bxDYiAhlLjom__GPA172x0VExJFhZF-SjfMj4hJdlM5bskravgB1HFHOoCkrwSbAM9sy2PgrC2HoIo-exncuuooyPqxDLuDt06f8Wu9FL0Ag2qiK8839pVvYjRjh9Rx9VzKGJdEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ddfc2f853.mp4?token=SibjIRTN1zTqTxZOlZBe_jiSUUmjfO3dKbh5F8PZLlSiGNbEJqUkpPcPj3Y_zIh4nbjknVXMYof3aTuUvfUCfyR1X9PSaQPXyiNav4m8_eOhSdXdRXu452bWc1SuaQl9g3ETGJHh1p3FrGJk1ce8PbQhmnNaEglM0x3N8CvP3iaAPK9q_LxMYBgM7nxg8kieeRzRSVjQTDrPW7bxDYiAhlLjom__GPA172x0VExJFhZF-SjfMj4hJdlM5bskravgB1HFHOoCkrwSbAM9sy2PgrC2HoIo-exncuuooyPqxDLuDt06f8Wu9FL0Ag2qiK8839pVvYjRjh9Rx9VzKGJdEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
خارکسده جزیره برا ایرانه
✔️
خارک و سه‌جزیره برا ایرانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/101975" target="_blank">📅 11:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101974">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQKOf5FU7lefFbkO7zNLX9gLwl5kSLymyloe1D8ic-URvtjmtM_0eygfjLcQZ2ZHF_J-0X4FTTAFjtFYrynUzEkvVpLP8A41y3m04QtQESC6atQN6uFDmaZAEotyjWfj7tD5DUFmzX-cM_VwiVL9lDN5pndxolmxBCMRnpMNQuZ4ZzVnpBGpoGvQrv6Kn1WUHlM6BkIG6208qT84owZOZ4w3t6_P3EDq0I2tQi4xwGEQDfyTd50TSj6mfTsF0xmti0tBiUuUVvZGA3PkCbimBt-S6zxEuMwuJ98RG7HZtu2crMSelw_h3LVnD_hTInxHItaY9gO2eW_9wPh76hkSTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انزو و خانواده تو تعطیلات
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101974" target="_blank">📅 11:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101973">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjTmAyITjBqGQ50_WlM1hmLZMDU0oluGOGn4Nva7nJetVUCkZmCQe-ZNUF3lKLSNsWs3J0B6X5GIVU-Qj9kD0s4uoUBPHOYP2ZXg5pm_t4oKMi3Sf1Umuzk4wwrL_9XiFXrJoPOAS1dLZZkDXcPojRJVJzhS1p2uEzrQozQYufgsEGPAjm0g9XYZYrxOyyoAuLZwZ0PlR6uomVMY0NyNd6hLdrr3Bj1onJsHKgTzhY-xXugz7zqxAiaMJYnnaIsOaOxGdkyH6ZbGhxRIj2puXmfbS_pUVSbi04_I8xHyMp5yVmkM3RsCiNGr4SuMWtO2MUXAbpTEHcNOHCsxCF9x6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
‼️
مانوئل نویر:
🔺
هرگز آن لحظه را فراموش نمی‌کنم. مسی بواتنگ رو رد کرد و درست جلوی من گل زد.
🔺
بعد از مسابقه، بواتنگ شوکه شده بود و گواردیولا به او گفت: «احساس گناه نکن، این کاری است که مسی با همه می‌کند.» سپس به ما گفت: «حتی اگر صد سال هم مربیگری کنم، دیگر هرگز مربی بازیکنی مثل او نخواهم شد.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/101973" target="_blank">📅 11:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101972">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c941f7e49.mp4?token=Las1kMFL2aWkWml6xKSP2Z70HFhJtYmJN9OpMCBjCPrvnS_h1qQHLX78gZvaWCUeB7zoN-5ddTFYH6MXRfOt6geJWZVc7wk0PzlXscQVPRKApgTHZjos5r7waD_4Ba38sial1pIy5LgZoCsJ7mcDHICFRuzGfX0FNqojQ9WHy6nAAD8WctCOPVX0IDlkvEYeqfq-A8V3t0iKoPUUsxJ3AYT0lp6lhEULonKjbW7ORFDlU-G1N9ERRchFJgqXIqP18QkfQqzpeTatrpy1dko_Ux7Z20P4FwrOJsMNDb1VQ0z1hygs1TQbNGBVSBTI4QOiKe6RlzcYtaysotn4BZPgIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c941f7e49.mp4?token=Las1kMFL2aWkWml6xKSP2Z70HFhJtYmJN9OpMCBjCPrvnS_h1qQHLX78gZvaWCUeB7zoN-5ddTFYH6MXRfOt6geJWZVc7wk0PzlXscQVPRKApgTHZjos5r7waD_4Ba38sial1pIy5LgZoCsJ7mcDHICFRuzGfX0FNqojQ9WHy6nAAD8WctCOPVX0IDlkvEYeqfq-A8V3t0iKoPUUsxJ3AYT0lp6lhEULonKjbW7ORFDlU-G1N9ERRchFJgqXIqP18QkfQqzpeTatrpy1dko_Ux7Z20P4FwrOJsMNDb1VQ0z1hygs1TQbNGBVSBTI4QOiKe6RlzcYtaysotn4BZPgIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیوزلندیا اینطوری از بازیکنای تاتنهام استقبال کردن
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101972" target="_blank">📅 10:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101970">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dk3ZjxUHvNjavd6GhPggt80-vtwP5gX6by-zs-LkGteoKDcm7LDhVtTgE2SGj-Zg7etqKeRVjXMSV7FDgeNabXK0gucnFUzU6cEn9mGSgb25ziiDK_gTiidh-YuZJC9Bbmxwf2yx6u3gK0mBOSXFMJYTuM0Bgtc1qVawEJZz9N-T3M-3BqHZUycWHypLCWUYKEyW04UjeZpOMISTU1edGoriFlsh5qs22F6L5CUmKgIRpbKTfYjPI7Ek9DNaGT7WkthdsNUj3fNDn9cPsgjaZwLCn8e4dIwyagKDq1uIRqgM44ywdfobOu5HJi7bHE-DoZtEv6Um7P8fFv5V_uTkwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/viXOTRu5jdHJnqiGEJQPt9gBFcH1u4d7t1AEIF-C1VIJvfln3x9gUn2_oIaI1frnc8XovIX7GzOQvTr4Pn6e1W6LiutNwt2_7DZrqMnVx1WX0LSRu_omEA7mKDhjGkw1wz8hdnmVZb2T5uMZiRfD5iFDm6qn7re5pcn2w1kIsst8pXcXcyVTqQcaE5kDpUHzVM-2PZ0KCdnIwu536guCApgtZY8-3mnqjwIspPLD1CVR5V_tB_o2u5VwNWYlzO9fkSSSdx8V8XC5mW8JFTqTObtEHCOJRThrh11yS9HjZn3btP90vuOP4Eg_fV2uxCtxQ3qnvloFf1a0uJD6jrxXoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پدری داره تعطیلاتش رو اینجوری تو اسنپ چت میگذرونه
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101970" target="_blank">📅 10:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101968">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ifSpFeQDi6vyX_7SDenGFukBXcZCUbD7lI5PyXhFPUI9_I1b13ZQxEKAlLgzmTDatqXnn9fTCX3iTQHWCdWzSttreO_gQJhsvqMgRGp_PbxGHEAJU5WMEsXG5LoTyWcTFRFxOCdYTKsqAfINqFsDqZrB4i5MYwZOPbtF0fVwH_UloIrlwIXgIAcz6BCk6YRyNMnYgY9F2qq8-wmgw_g5PYXqkzVDd5Enfuwgme6XEj3MOhb5HJDVRYUCOIWCdm8Wr4N-IP8nyQmB7yECYqKnPed3pONWnHgMRfJcXGgDzp1_kBDFJDJ9KcE44CzL5Gok30RuNigDCqs4V3SoCW_1bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KTPi-38ol_8TAoVc8BKQQf6Mk7VL-C3Rj33Mbzg3YcIv9lbrbHaIBtUuwInSSIndpPBPmDrd6TjZUM6EFmTxphqSll7gDqnZ6z367wW83adDtXx739JwDRa-4PXZ1v_1esOs919SezwyiNFhqDwzREGgylV24Liopstdg1Kr2J2flBSBgA2cmPvM7-tS9GgYH4sXJpGv2Zhn0n88yfOJc1cxHyd-hHhKccip-v9l7kzKKnF7Zgmexc6mQfDsS_MjcbM6ln89rSbsiwAULlinepYoiV3nAs8qxJHE1XETJCxxHrhAxLJ6-3tsf-eTS40wf64BN0eqsjpJUKLvqgpy7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
😞
میگن نیکولاس پپه بعد کات کردن با اکسش تیانا ترامپ ( پ.ورن استار ) الانم داره با لانا رودز وارد رابطه میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101968" target="_blank">📅 10:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101967">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMiCH2TCtkoApRf6gQSDvwbjBO9sIuUa__wLqOZtjPbtW2RnhDFTcpY6bHBk61bo7pShdNMldmKWyjkk_9fp_KDDBqOGC9kYKt4twI1ypZUX2SWTsN3ZgPG_QLLerVHmtgL65USiWnaEGhvYU6srCK8qaCpTYl6SETuYwzXauCCSvuXgedSrEtRdrMFuaJ-LbMfXuf294Nav20pI_ZopvK0peTfYJoM5uOwZivCZrs0hnPj19DWGwebTk9DF7B3n_GRtV6bRkHjr1FvrSd8Y4MuqEYcRI_f9WwmXq4u4z39t3j5Rbk4ekYjHv0mgoZByNcIFSqUm5QCfsoBBmOo9fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
موندودپورتیوو:
اگر بارسلونا نتواند خولیان آلوارز را جذب کند، دیگر هیچ مهاجم نوکی هم نخواهد خرید. بعد از جذب آنتونی گوردون و کریم آدیمی، مدیران باشگاه احساس نمیکنند نیازی فوری به خرید مهاجم داشته باشند و معتقدند فصل آینده فران تورس، دنی اولمو و رافینیا هم می‌توانند در نوک خط حمله بازی کنند.
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101967" target="_blank">📅 10:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101966">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MaauBu-VB59IrA-yODnrgRgj6hWtTvJF8TEGwSNBwcblLHlI1h65pjD147liXmVumIf6ViLyEE2xYj9GArwFZRcaQ1ATUC8SxtjEq802zOJiWX5LkE9JDDqcT1FO5opsLO4t42-cSH2-tMWkVOKTwOdo4uuM7o_kmg_ICavHpDbhMx3tVTpL3o7t7bq4GXrcdR31Y4eq3ueBN6WdYgxawXphwrB82p6eYFEH2wokcYKhkBIm1WWmarnc4zqQrTzW0aLyfnZpDEx-6KtQoRJk-g83wkeCoau9BKqQMiXrisRvZ36hoA-WbIFRP3KFSXfqYaEeIHTJNVyHrDFia0K62g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇹
–
فابریزو رومانو:
⚪️
در ساعات آینده، باشگاه رئال مادرید یک پیشنهاد جدید به باشگاه لایپزیگ برای جذب دیومانده ارسال خواهد کرد.
🔻
این پیشنهاد از 100 میلیون یورو بیشتر خواهد بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101966" target="_blank">📅 09:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101964">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RBapGYXbH3I-dsqEOi_9zGQZk_AIgjOeJB_Q9nTqE27BEwbUinwigQixw6dJPdEpmS46jFTrVPa5RSzovmX3pxZxUiO5R6MeBNC-WGmmFxBMAZjccF9n6fnLP66GanDJgdnF7H5Sqw8x0TG69_TUr_2cv03v6NjOrM_CzUWWpb6ly1lWQXrdwIpExv-QuvNc6uMK6KutyZIHXDNcA2WYpebJhwb8WCKUpqQA92R1oAmUSFnBwfHAOfQoijiUML-dUdCB5T2kuLtBWKK5bydB_EmP_zlqJAbNrFCYC3TL-0oMyzkLiA0Hj8_kslb-D8oqUVGtIrTv5VS0bVNHWFWeIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DZq5ss6RAvY8I878NDcSzXh4prlVzZRQw_Yf4nWqomCobrSoGqY_CxsrpE9QOs0hjci50XMp5zyVJ9-iWHrPQXKrUywrL8V70YKDEmCo-vaaNAxP1DuJQk9_OZBand6HxiMT474TD7Y8J1A1QN7CijJAR-civhKtugene-VxUC1Tj7RjK4xoYZtzZN-1aNa4fO8zivDGs5ERhJ85NeGmh3p6vak45ewUcscfauR6MqbhrRivIO0VkM8uwRr10yN4eEjYPvRUSBYhP_s0mNn11PxhLoOMzVHBe1kXTG4aEcLNAgaJzcAvI9tgaa3iRGFpty0LYQ0SQ5BLl0qc9pPclA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
سوفیا رین شایعه‌ای مبنی بر اینکه حاضره شبی رو با کیلیان امباپه، آقای گل جام جهانی، بگذرونه رد کرد: من هیچ‌وقت با امباپه شب رو نمی‌گذرونم. هنوز باکره‌ام و خودم رو برای همسر آینده‌ام نگه داشته‌ام!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101964" target="_blank">📅 09:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101963">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7DDqU2xJxNjGS0c2jA80ItM7_CuJ84JDM98rwwhMRkZA_MKjzqtxLI9WLyoQYb78lEtUP7VhvLxHSNV12mwVNU2m1ggs-hjoR9rmFNZNMp56gK_AIt7vbG-r8WrRvmnIwXSQr1PJ2GNOIV5d_8ji-0pJVciqzcdGqKb7jEqKU99bJuEC7WZUP6MXGTzSRrt9Pmzgg8LbSbvk5svlbwMO_jTJFp5bXCQfrVAMLbbHBERPTJa8QyyZNnuxTv1reXJ6vd7tUxBVlOye_jy-6a6i3udDKDbEXIdKQiOnyFLrNrQEDhlUQsf5lvoyQJmrOjOWtiuXDo0kB-6ZXJ0JZjKSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
رونالدوی برزیلی درباره کریستیانو رونالدو:
فکر میکنم بازیکن‌های خیلی کمی مثل او از بدنشان مراقبت می‌کنند و این‌قدر اشتیاق پیشرفت دارند. من تمرین میکردم چون مجبور بودم، اما او تمرین میکند چون عاشقش است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101963" target="_blank">📅 09:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101962">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f0d0985c7.mp4?token=oH2kDm212imOZF9d5dz6ZyssFTHAkHdSmmcK306XCnudY8DIy7zupr-yXn9RJZvAX8-JsHx2fAOVwj_dqoTYxUyIAlLgzAX49aJUpF_ZcWnw9azTi-JPG_BNrL-Z-z6QgF1_zNs2mal99KjnXN3DMXJZ_Msl6LfmcRXHqMcxaG7y2-hpTra_mJjzCIM7N0RW2tdd94m_DToKOvR_fHTG3DRsMIdog00qXBZsikW1vG6XzlX7aWBlSI-MOx8FTX9OFEz_bbkgn-kVk5GS4ikPpqRM27eG3OIm6xCXUddlrlVUykL2zrYy9dykeAO_eWBaElKGgBofOp9hraPXVkSDPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f0d0985c7.mp4?token=oH2kDm212imOZF9d5dz6ZyssFTHAkHdSmmcK306XCnudY8DIy7zupr-yXn9RJZvAX8-JsHx2fAOVwj_dqoTYxUyIAlLgzAX49aJUpF_ZcWnw9azTi-JPG_BNrL-Z-z6QgF1_zNs2mal99KjnXN3DMXJZ_Msl6LfmcRXHqMcxaG7y2-hpTra_mJjzCIM7N0RW2tdd94m_DToKOvR_fHTG3DRsMIdog00qXBZsikW1vG6XzlX7aWBlSI-MOx8FTX9OFEz_bbkgn-kVk5GS4ikPpqRM27eG3OIm6xCXUddlrlVUykL2zrYy9dykeAO_eWBaElKGgBofOp9hraPXVkSDPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
⚡️
بخشی از گفتگوی جذاب بکهام، زیدان و زلاتان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101962" target="_blank">📅 09:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101960">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tyU3KIie7xPDL-jrw5kb5oDplwi2TpRgnJNJ9WUIckTsgsTz0Il07L6vMB6VpzRsVYbpZh069iCtc9v_u6Zu-c5vvH9Ij3vqfLnLMDEBdgqr67-MwsaW9c1gpyDbgc1GnrTcQ4b2XE3zJ9NiectDZdQHk2AV-I8TYQE6vejgB8B9_vQjNLiR_E9ebZWwECAIY9FoNJE83o08XPZC0tDo3q9kaJcBRvjkwVWbsubWcus362wm9C4Qas5WOD_0h-0lsVrGOQXSKeJNCXEH-VlSmKPW58IKRkBl75FT7QLyvLv-R_PP5jFihlRaz3Ra32hbOvPaU2EDE7PTmlzR6ub83w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WzCp1Ch7sRMiuvGlPj32fUL75U5uD8t9UW_1ZPRNI40SFYJGBONhiKvsyFABe0RslF_zGW4WDHrrhdBHwzrDtXaYEL9r3KNpHFZEMtI6iTI0yktjFylmMMGxaVatf0NonY61zwkK6XfZk0iZpg8XUd_lq_yo17WUwhclKWGTDBHq-4XkIcxPe2ZkRnea51FAj5mdk-jB63eELXKEUGn0kT3Ax3-ruGK87ZwWMBdZTc7WlBYhl-5eSE0EvzM9xDM-wgZFXxmJc-M81cK16VJJG2n_5XJNPzHIMgFClcyRDumCuC754DDEo_cThi_KwEer1U4n_2EzVB-qLrkJgG_rjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کریستیانو و جورجینا قراره ۱ آگوست با هم ازدواج کنن بالاخره. تبریک به این دو نوگل دیرشکفته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/101960" target="_blank">📅 07:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101959">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YETGVfDKMHUbLeD6v14pkrLVol1ZwRM6s53daTHLdyv8hZkkxdx3ZFQ3UaLU9ERDTlkOuO4Qzd6keQ9iuOJ_9M-EYADdyOmAOde7H2glE3ITsYGUYPGAyAoEoWNSgzLyVI12vINl54L1qfaXuEgrD2tsOpsSzajl0eZgFLl4y-Ts-bF0-bOfsmOjQyXLLSGZSNcPdTWv07Pg38xmgq6zbGOhhuoLLHjGw8trKZ0TggTSfUXdaBCzqBw8yyNlLZla2ZR1B7pMnPShNnapljJggopPRZ8tlX3xxT8QFRx__xsXn9sPLaejW4wb_ZyPUHAHxxSzEO-EojxT8O52dCMWCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👑
موندو:
تعجب نکنید ولی احتمالش زیاده که لاپورتا پرونده نقل و انتقالات بارسلونا رو بدون جذب مهاجم ببنده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/101959" target="_blank">📅 06:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101958">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85d2fa751b.mp4?token=hvHeS5-YhcZXmGeUtSoTOq_54kv4S0hW7DfKURIrSIIRgH0OJTwvRisewzjeQ7nyYs_E8ZOgjWskYSZ_P9ZMdXPzh-W_1-BeZYde4pUPLkdaH-9hI3Z_kJ_Oo7P8-6j4UkemzHVsychLVogV2mvBklwrPjhOx7ezOlXVEKfroj28xjBNJR9ObFozsHx-SCUaTGEZ7tffKy3oLKOF9hJhH3-IeRZZ_gySa0ZYcRgjyNdVWSc80dwgqU-7pTrd-1E--32j_sEPuYUKvdDkLfBvIASOlZx9vt-Tm55MHLFq7-X0m58n6Fwh6lum8iG7C9mq7ltC7oy-trHiq8eCMS9BuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85d2fa751b.mp4?token=hvHeS5-YhcZXmGeUtSoTOq_54kv4S0hW7DfKURIrSIIRgH0OJTwvRisewzjeQ7nyYs_E8ZOgjWskYSZ_P9ZMdXPzh-W_1-BeZYde4pUPLkdaH-9hI3Z_kJ_Oo7P8-6j4UkemzHVsychLVogV2mvBklwrPjhOx7ezOlXVEKfroj28xjBNJR9ObFozsHx-SCUaTGEZ7tffKy3oLKOF9hJhH3-IeRZZ_gySa0ZYcRgjyNdVWSc80dwgqU-7pTrd-1E--32j_sEPuYUKvdDkLfBvIASOlZx9vt-Tm55MHLFq7-X0m58n6Fwh6lum8iG7C9mq7ltC7oy-trHiq8eCMS9BuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🔥
نیمار تو اولین بازیش بعد از جام‌جهانی با دبلش کون سانتوس رو مجددا نجات داد و با نمره 9.4 بهترین بازیکن زمین شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/101958" target="_blank">📅 06:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101955">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sXWVcXEb78TGA7H7S_jc5_A6l1yM0gLFGLQC3qz89WbaQE0AqjZ7pxR_F8iU6mCOB-0QE4h-_Tw4D0_GXVp04LohVHTCG3BwTXmA0AFXmZ5ujUSAeXZtfDME87sANrAYl0MwMjGZaaVLLVj9MCctdEBo82pVgWO-xF-B4eyaYbPGEz58keZg3uhW2otqzh1yDQJfhsyn_3eBD2_hfbIF8U68KLcg7cy3q1mPV9eokvejZN9OHk6EWALfE8Ian2NYQSqTuYe0UGZr3EukwNofU1kAjdGyFcNSbpLB36k0rxp-FtfV0yNXt8uZ1RxlDGJZUJJBapcusS2EC3zdmmGXkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gx_oDIsBQt9_u8qwqTSITnGqCctAlQ8-nI-YnlRPaahp6cHRLOddhOZKmerM7MFcf7uFZ_QixPK0xEpQ9ZdfRnYjnk-Yan_huy0Aod1HN4y1AJOb7Qrv7_YZ3OHJmxhBydMyugm5nwiLNMoEyPVqXyF7pbAwEbDwqX9SugmLoAdNP3nORvo_quD783vwLMZeN4HDJ0FKfIdRBOK1JQlW0qnU4LaupkcvbB4bVPY94e4N9QF3HFyyTMyq8NTnunk49Y7yPodyNnd0stnrzdOlU17HIJU97uqOceVxsI_YBWCZ44wUZtFQm9kfBNaQ8wyHCFH-tHnEhFXTSauFpZcMXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/953a60dfac.mp4?token=Q-leYCd1fSawmTRGJRKoWlwtIgxy8A3KdxMf557yFRVly_He8y4rrQkTSatxUXMr9lBxrtmciPI_uloAhbl3h-euo7N_oiHJKaBpGs-v4TtfMs4G1P__q1quJX5gzm-LiEHFnrdHRna_KRaoY9ZSJLRNj2j1AwXis31np5xSIVFpDehwjOHPXt3_qa_r8dgO2HZoIxA1R1ptLe7QlatcApwlvKl_0xsrDi_1KuWiJ9n_brFZInKkOAL3xC7FQ8zDt1LkGFo9vg9i4S-dR6tdKhKbACZhcsPhQ31i_5HRckRphCBeUy0Se4rQbOkNdRv7v1ejwiLtgtGvvdH9yABuqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/953a60dfac.mp4?token=Q-leYCd1fSawmTRGJRKoWlwtIgxy8A3KdxMf557yFRVly_He8y4rrQkTSatxUXMr9lBxrtmciPI_uloAhbl3h-euo7N_oiHJKaBpGs-v4TtfMs4G1P__q1quJX5gzm-LiEHFnrdHRna_KRaoY9ZSJLRNj2j1AwXis31np5xSIVFpDehwjOHPXt3_qa_r8dgO2HZoIxA1R1ptLe7QlatcApwlvKl_0xsrDi_1KuWiJ9n_brFZInKkOAL3xC7FQ8zDt1LkGFo9vg9i4S-dR6tdKhKbACZhcsPhQ31i_5HRckRphCBeUy0Se4rQbOkNdRv7v1ejwiLtgtGvvdH9yABuqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🔥
نیمار تو اولین بازیش بعد از جام‌جهانی با دبلش کون سانتوس رو مجددا نجات داد و با نمره 9.4 بهترین بازیکن زمین شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/101955" target="_blank">📅 06:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101954">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMhu3IvJZ6TL2vLgS6xdQGJVR-o5qYkrtYPsCz9K-Qwqkk7CNQloQpuY_7c68xYMZLuGVgFAFmhyppp_D8lNvYWrU_xY0B2DZA3jgVWHAIAw8yVoQXgdnd7bvfJKSZ-fsyeQdyzdNYuG0VCzNxYUvQ8KX-Tf223amYE9gf0t3dmm1IzCjuM_2-TZEbkSmQbQwPrXnXFi2v3qlbPEDYlDPdYCXfSNu_A5skOTPgec-gfTwrlhnjuXVB9WfJjZTx7xuB8QRDkUE34RJ1E5bmuQMHvoAbg2TiHJjFCvlFs_T1wqj6yquZtv5rQk-OAh2ffj8g6jzMAMT1FwAsf-AAAwyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
مسی امروز اینجوری تو روزاریو شکار شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/101954" target="_blank">📅 01:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101953">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44643cb150.mp4?token=SpQoi2w9TpKb-pSuqkyb9CEJ-3LpC2dZg6-sH11m6vwW6IvXKp2YmC3jo_2RmioeMyndh9dLxJleaGj2Sn90KRF8UTDbjmicXRuinFDl6xtyRh9ydpo9r8uc2TpH04H5unqBzGbfkI5TWO_LdJaCoyw_M-wGYP39cun4sfq_KHnQjmF3lnqrwdV86B-diC9BsBAe_Iwjf6M7Wj54Lwm-e1hmoKBDI2gYaADtJaI1qy1xWws6OIeTF4wmt7o18bRzz0BsPU_QlES9rNbSSvK8Nw9QG67RBxLVc1HdwwdLsOmW_GVwySv9UV_AbGS8tCeibe_eyXT7VUARGse78zyu31rwu6K38vJ3loaDD8eyK2QWerOnDdmWPVSvc6w7tCihVOtzOGmh-8dskW1Qevw3lCXGbAITTO28hS1VncLYwDabyIlDcBp5lvrrvUMw0w-_D7MFboSQfjvqKT9uxzH0BGDbzQ5G-rNaFtV85ds68tiKOQdGVazm5yhD_8shp6HyrJLeWpPn-7UYP7mbARKKlniQIipjJsYCAjpDnk37_9K_srbMxJlKsD__RU7ahNI1bfsdlgRcYf-aPZReq3j61IujOvwO90vhvRFFX62_z1b_VauIBUbOtjjopH_jZOW7L9qt46rj-YPbNK_5lYgKZqM-l_IAk_f62zM2B8JcmF0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44643cb150.mp4?token=SpQoi2w9TpKb-pSuqkyb9CEJ-3LpC2dZg6-sH11m6vwW6IvXKp2YmC3jo_2RmioeMyndh9dLxJleaGj2Sn90KRF8UTDbjmicXRuinFDl6xtyRh9ydpo9r8uc2TpH04H5unqBzGbfkI5TWO_LdJaCoyw_M-wGYP39cun4sfq_KHnQjmF3lnqrwdV86B-diC9BsBAe_Iwjf6M7Wj54Lwm-e1hmoKBDI2gYaADtJaI1qy1xWws6OIeTF4wmt7o18bRzz0BsPU_QlES9rNbSSvK8Nw9QG67RBxLVc1HdwwdLsOmW_GVwySv9UV_AbGS8tCeibe_eyXT7VUARGse78zyu31rwu6K38vJ3loaDD8eyK2QWerOnDdmWPVSvc6w7tCihVOtzOGmh-8dskW1Qevw3lCXGbAITTO28hS1VncLYwDabyIlDcBp5lvrrvUMw0w-_D7MFboSQfjvqKT9uxzH0BGDbzQ5G-rNaFtV85ds68tiKOQdGVazm5yhD_8shp6HyrJLeWpPn-7UYP7mbARKKlniQIipjJsYCAjpDnk37_9K_srbMxJlKsD__RU7ahNI1bfsdlgRcYf-aPZReq3j61IujOvwO90vhvRFFX62_z1b_VauIBUbOtjjopH_jZOW7L9qt46rj-YPbNK_5lYgKZqM-l_IAk_f62zM2B8JcmF0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
لوکاس هرناندز: «کیلیان، اگه قرار بود یه تتو بزنی، چی انتخاب می‌کردی؟
🔺
کیلیان امباپه:
فکر نمیکنم هیچ‌وقت تتو بزنم. دوست دارم مردم من رو به خاطر کاری که توی زمین انجام دادم به یاد بیارن، نه به خاطر تتوهایی که روی بدنم دارم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/101953" target="_blank">📅 01:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101952">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRXZmpqtEDS3ZloMdGXANJh29Yvtuvu2Nb6Tybr_sDS-MFRqLfcs_Lqhb4EcGxaZLcnxZrkI8kVeaCFsLCaMTdep8FX4UckN3bmDMznDOlYw2WD-U1paK_JT5qVLkYHSj9YOq7PUkbrGtRB5oELO62hVm3YwNLjkCn-AtBrE_M_e1Tyx6kXng26USr9AaZlIymKOWam2Br0IOsUOAyjZmomerKfX3mEIYGp67oXsNFZi2bd_ks8Se--6Avt5spbHqyjglWoFJ7gYTFE6xa4FVQ-A0ly5FlTl2wsksBcZ--yg5bRRpnw75lfdi8ctthPP5L2zcIejY3rHKkGVMnpwPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
امباپه و پارتنرش بانو اکسپوزیتو‌.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/101952" target="_blank">📅 00:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101951">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KmyADtsAfEsQvxnbT0eEj5LxhHoLzslbggAPq-3fecjNEeQaXKdzQLSgZiGLBSO744z8f7edyu9KcKa6wGtyAvCpPjX8JP8XlK8_YpRqFK56ac5oKQLRPxS33r8EBvRDY53hYeSYMTI45z0pBe7toLs8etXCoYmoTcz5Otruw0pelNIrWvGKpEqdyE57NzdcPp7EBq7SVx9YETX1LqBiigMINLGhdvweJW_MYHagOye7c3c897pdNZtgODPSnX-qFP2Tt2HiFc1ADI-dw9h103BL6dg5g78P56Qc7vxSsgUmTV-MAnMoznuvQJewNutWNfAW9ti4vN1xIFOdGtqQKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینی خوشتیپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/101951" target="_blank">📅 00:51 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101950">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63dd42dc4d.mp4?token=Z4p0SpqqzCIxtsyXxypOVel9BjDLJ5u3PlIWD7JhNGEtUo-3q-6FIUAmqheGyS3GLBrYo6ehYovPntsTwW6oIYqKjnZVVaMK5KdMQ-YphE669SdgAFNEpw2zo6LuNbWc2fjXVjdO_NLndM_s_Lj8WAoGNjKk_vEYeesIzcPvHkI1vgZKUjD8u6F7vWCo7W8yEZM0XUWcjstGwGqwnFdypgoHhCl6HnBJIjN1NpDyCbGDyRI8l-8G8ANTVQ1D4SnTEsfngB2sW_8kkrYjNXQufL0y5IgR9_yyo_v9GU5WTvsjhx40HkB3DVwr17Hxyg9hZ_NLFnZx8VwkQoBjFACGiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63dd42dc4d.mp4?token=Z4p0SpqqzCIxtsyXxypOVel9BjDLJ5u3PlIWD7JhNGEtUo-3q-6FIUAmqheGyS3GLBrYo6ehYovPntsTwW6oIYqKjnZVVaMK5KdMQ-YphE669SdgAFNEpw2zo6LuNbWc2fjXVjdO_NLndM_s_Lj8WAoGNjKk_vEYeesIzcPvHkI1vgZKUjD8u6F7vWCo7W8yEZM0XUWcjstGwGqwnFdypgoHhCl6HnBJIjN1NpDyCbGDyRI8l-8G8ANTVQ1D4SnTEsfngB2sW_8kkrYjNXQufL0y5IgR9_yyo_v9GU5WTvsjhx40HkB3DVwr17Hxyg9hZ_NLFnZx8VwkQoBjFACGiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ری‌اکشن هالند به میم هایی که ازش ساختن.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/101950" target="_blank">📅 00:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101949">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8PqW72NY3VBer5XpgINkS0OGIqKSIoVrUYgAECOsGaofGMaSctMjYjadGlgLHaZJ-azmk7zigGzX9seVN0eUodJwhBd_SjyXUr2Ldr890VEK4JtquI8KFedTlj0onWTph8IkGHmSNor_iF_FPSoQ-HyminnVbGrHB_LhGXJaQBxUci7A5UZuO6ts2MBstCLGuZLavJJngHDkNbQyGSh8nPfU99pfACBonz3Ej33K8uzOjMgHo4qXDgzE5HsGtCoEVnSXtixVNwSAYuRNI8aoZpF8tQehl4AUz4-51DopWVIS8MUghsq12KtBpiY_FEtjzhVAq6kE-J8zqL3SR_n9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو: رئال مادرید و دیومانده بر سر قرارداد 5 ساله تا سال 2031 به توافق رسیدن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/101949" target="_blank">📅 23:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101948">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iase3SUsnKF9pZK9CAR4mKw_WjXGXUqZfqs4NgEtpIga0eNdR-E7hRC2icmNbIhijB0sOZ6owOb1J9tkdSse_fQeIpIMIhAxCnS-nAAvVUSVAJCPoUmUtFmC-hVP78U9TanAMoFFzRHL5STJH5KzQX-QiWJeNww-M8yTyaJUP84DcFbR7bbwu9-KPfCx1OmQhu2KJK1oMtdjahrBRmLf5iuVfIiSVBRjTxlnjMngd73Ly89VTkQWdRhhy52Q8o1m1sHANTUK-Muf4Av9ONVtRNaVmwz7LkHsmPi-exwU5QeQGACMyuLUBrmKd9lXp7HrrOqRD_PZUI4_7Au03taVWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔹
ساشا تاوليری: باشگاه الهلال میخواد مبلغی در حدود 120 الی 150 میلیون دلار برای جذب لوئیز دیاز هزینه کنه! اونا بودجه 350 میلیون دلاری برای نقل و انتقالات کنار گذاشتن و این تازه آغاز کار اوناست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/101948" target="_blank">📅 23:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101946">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fj2jLjQTB8BAbMknf3BnvQ1HwnN4wFmcVTz7FQHvfszlArE0fE0O4MyETzoRCRbFoyV7lS4ScDv2XezmAXNYkByTmjo_OxCmpN6R8WxWV1VnCwG8IW9m_A8B0Zp3wvVld_btEpE8ovtbznRErSvLXZUzCoor0BQJvec1ytAs1_pH71ZMGakOnydz7YPNtpsjuyqkpp_9PDclBYiTRp_yiG_LEcgAiXfGXuMCm0M_MyHmVEQacrKheFD3VW3LKp9TQfEJmNMaRifISpZxcdA2HtbL13W2U-Cq72pVERMVqd2-jemfx3Q_xtj1j-WWxSaRrVusNBTE5GKEAuLvvjnBjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GIKUiVkg-nBAtrOrl-xkkim1iYVli_jEg1CDqO4P2cFe8ion9jZJPGK0xCUYE_q94EgWMvlsBY6TBVv1mefWDVetYhK2OI8EnflmyrM2bAlSPZBzeCWI6uirS5xSD64vefwA68u-SIApCg_FBcc6oxA2skDAwJuWCnCZ8N6hfEP53Ewp0WHz61MioOE6gRA3puQ9hTWt-gD3rlMOHoe7z9sPJiL18uPjIYoMFEriaxPLsmW9lZc4TuUen9RnnMfQEx4RPWdoSOr9-98uGBLiuu_M2m6PPfDfiLByLz9o73AbToGAC4djfrlWsi77K4FEcStz0UYL2UF2GgE5jfXsHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
سرخیو راموس درباره اینکه بین کریستیانو رونالدو و لیونل مسی کدام را انتخاب میکند:
برای من جواب این بحث خیلی ساده است؛ اگر فردا فینال داشته باشم و فقط بتوانم یکی را انتخاب کنم، کریستیانو رونالدو را برمی‌دارم. مسی لحظات جادویی خلق میکند که کمتر کسی قادر به انجامش است، اما کریستیانو این حس را به تو می‌دهد که فرقی نمیکند بازی چطور پیش برود، بالاخره راهی برای بردن پیدا میکند. چیزی که بیشتر از همه تحسینش می‌کنم همین است. استعداد یک چیز است، اما در اوج فشار درخشیدن چیز دیگری. وقتی کریستیانو در تیم تو باشد، همه تا سوت آخر به برد ایمان دارند، چون او بارها این را ثابت کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/101946" target="_blank">📅 23:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101945">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdSRXUeHFLHfSm42UAeEfXi_pixIRQz_HiVBja2x4g5QIpCTZsGNKPTQteS92dn3M8-ijQVKOS5GUj3Ov--X6lmzxCaInOmQzyVqMvcgoG1KjN75iXjyP556qlIVZl-p8IHKionGTX4mr-V2wu-IvOPtZSyCWwu0-NXnhW4Wf1Cjaejb4aTfeO-IXoaAy8iWUKJNg-mmn93hspcb-8RSGl_gBFMc0s-u8Nj5xLwvXYoHJA9uRgdcrVRav2R9VZBIaRlC5_IaHUE1eEMrmytSnU9sqPyMg9PMZjk4UrZAJb7WpzMKrqyhGlN49maj0vY9gin2fQqjy77oQMmK0C3I7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
به نقل از فابریس هاوکینز:
مایکل اولیسه تمایل دارد به رئال مادرید بپیوندد، اما بایرن مونیخ درخواست او را رد کرده است. رئال مادرید تمایلی به درگیری با بایرن ندارد، زیرا رابطه بسیار خوبی بین این دو باشگاه وجود دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/101945" target="_blank">📅 23:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101944">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMEzxtJKITcaoaUwMjtBOl91qyEV_w_RPAnZacKMQcpQa0pyq2-021JnB9iu3c0p8HWLp_nZ0hzwleGY2GsfEF8gU91BufcG2MOT6PiwEElVLFrQ0Ta5OrFWD6Iol2w7fa5l0sMRS0OFqlIOsOh2qHCHtsxSB2FV8A8_6X_wwX8wbhyYlbnztcH5rbKghDJfIn_R5B4BvjN_hyo3MH29MncWYSae8cBLExORG2tgs6axQIaYxpQih12x8FAUBSMQUgMLwyxUiG7xFHviQF92g16Z3GLwdFBlSB5tU3gohpyL4k9GZXLYTJ9I0bMo7R9-EVKmeOdXfXxV6NQIL0b8QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو: رئال مادرید و دیومانده بر سر قرارداد 5 ساله تا سال 2031 به توافق رسیدن
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/101944" target="_blank">📅 22:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101943">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFLvfnMp_ZzSb-ksco28JdTzobhN1Qm_Uw2qBUCO1u9LqwvTYMRjRGClGHZW1hw4LrxJFZcoE_pv0TV7D9y3vuI6ZAQIGt9yjmt3qBWVWrEy1TeOPF_IoGk2-vQk2bqmVnYdya1PWTVo10EaBTjVKgKN1ObpZvEfzFHBPmVAtnFqCD5PM8_GswFfkColsx56ZWtqs8QvurnHF7XoqydNcPk4MiRGtltFFLFGNXOoW8_zyJwpLBDMKyDS2j_ti1pB2V9giVlV713Le7KmYKM60lVhnEyIdJILSAJ1qOTjXLtusMF5hPiTE4O3p1qPFY_pGwB3UtSvpleJVswW18dcbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فابریزیو رومانو:
رئال مادرید و یان دیومانده به‌ صورت رسمی بر سر شرایط شخصی قرارداد به توافق رسیدند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/101943" target="_blank">📅 22:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101942">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qxl-Nd2vb8Ya9fphejAUbJIRRWnlcyemCHtQ1mvAsvvo55Mj_gIMvouIortVMLuDh5V8Ui4aOVjeD7YAOJEJYvBRU7TJe1UdKQW6LPxmOBZ0MsMjw3oCJhcf-DujOaxWO7MZ1NT6VbJyuW-GWpzSMuyUqpDVFgC7-iy2TUqN2aeQhwZzCJuAG57wnvy-E46oB2cDN270z-OPQ2it3AoY7Tuorbp17nAvJZ4OdOdZSbFvLv9CqNFAHtTuqfLtHR_SnFC6fgBtWjCTJmoGyKTi11G2P5Gfh6KXWjpW46173K6hegdyeCCWnFNaTyDnjL4coNwM6XObjT2Zq74Q5-_clw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
👀
ترکیب احتمالی رئال مادرید برای فصل بعد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/101942" target="_blank">📅 22:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101941">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4yuQOzYB1FBjmmQefGTMVCMrYwxkDKHqMf1nKJXMsXyvyV1o7F6fDHzeR1RN_t3xG_wGeaYEXTVgCtboxJ2Qk5-OJpl9Nqw5_sOhJSr8V27RExP7zDsQBH3mBGdDG0Dy3AXF8dbSxHpZVdWbSn-77JSDxwlBGbKXg7zyI-0uuhIbx3aET_d-3QD7HH3JfwQ67jnLJvv4ixpkqXSzWvb1W1BezD9LA5W9VAtZPKnr9zX7ZekCHc7frECRccnyHvnsL8ly7swWvJCWY3b3j3x9LIk5HQIfI64HQN11KOmx-fagtT-AWYmr6px7Rn4yuonkztl9KUK3R8ubsLfBJPd3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از قشنگترین تصاویر جام جهانی؛ مارک کوکوریا قهرمانی رو در کنار پسرش متئو که مبتلا به اوتیسمه جشن میگیره.
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/101941" target="_blank">📅 22:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101938">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dcjt12D0z2OvBfrQRSRPXfyVrMCYfaJFrBeNMHezs1EG3zo-3ItD1pXCENZNTuVTU2DkdqUzRhNC_DVGqFpAxwzZjQGZxFswkPPGP5yy4-B3s-ykt1ZAyarkuvCkUCwx46kQJZO-ILmwxaEejxG4AnHyHU-fG0Smwlmujv2AixXIZlnO6IfANE58ufHtfmc9P9_tGuRH710W_BtIj1MO-53xJ6Iq6k8-8XQ8-B6sJYHNDnPx8EUSXWYMmOl2x5x7_drjkyxUxK1CFMxRCiH7fFmbkyEe3oOWKZhVQ8_MmFUOfUAHZ4bgnuCKhUAZS2M0DMPFHf9fhuFXc_Bv3xBiNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SRxHS_2FS3XLL9Ko5Tayq8Ggy8_1tiHlV0B_uXVKFrWXFfypv9SS5MrBJQAEwjI_cnIIRodfySSBx31F35x_zqTg4bW6BgXTru2MPmjRMj5hhB5fwQ3NpAZFimEONrrvzFYDOF5dUudrKyAsyCCZJSIyERUxFGFCyjQNRqJ9QiIyvA228S_w3NMCTH0Hua-d_zUtViTqwxxIir_yRQ3cnkSparDOR7BNrSZFHXkULkInZRTl9GZPRk6HgH4LOcwB4ZJhsTK3knh_T7K1e6HKdt2krzAX6a9Wq3DVVmTw0RH5w0XzdXeFmOa5O2MmHvvyCAJq6ir5ztxae0T1P7BJkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tW_XV_En-IG7w7ul_Vj3P6dfsToWS7KwYo29HP23eAHInRGqdHm2edN8d8ugD-308JrdPkn8GWxXAMWSQG8FF-E5pZccPbp3H6cL6tvTTX9YeAyQQBX5z4uTkIeNGilyg_8s7a7th02_e3KSILNFA6qpl6Poprnqs9mx7zcXBIkFxRqJzFX9CDxbSBSQ6P85ru-H6MlN4cBQlarDiQ6WrddMBWS-4D4-8jPSOCfiwI2GIZpPPsrnzD-YzKFgKU7u2uqU0fJiYSdm9iqAX7sBFUbQjePYw9fl296brVg0C4gPAYgvK01lo2WllVg5N_A_u1jgvV49Gs0p-aOYomB1Zg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇳
😆
امروز تو یه حرکت پشم‌ریزون دانشجوهای هندی تو اعتراضاتشون ضد نخست‌وزیر هند، عکس امباپه رو هم آوردن و محتوای بنراشون هم اینا بوده:
«دیکتاتور امباپه شکستِ سیستماتیک را تحمل نمی‌کند. همین حالا استعفا بده!»
«۱۲ سال در قدرت، و تمام چیزی که از مودی(نخست‌وزیر هند) نصیبمان شد، نسخهٔ پرمیوم امباپه بود.»
«دیکتاتور را پیدا کن.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/101938" target="_blank">📅 21:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101937">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pb32gecxljPLvJzLtMsclsZzTcLfgFQBUdvmeUD7qeIHureDAHUi2wBl9SwJdT-qgGZ-7gM7f5r-VYES1SCEo5dZadodCE-AF7A2_iuOWbnJll4vxXgVNhmIJkS1U1vKTvQOwFnaJFhnXBpbI6yWnhU-OtOjzIvgBiemPv_l5j4vqNUGVHsai3RD43j1mws91sePG24gSb_-9fHL5nhi7FOH9gvsgGmaHkq3s51KIBejQoLEMsKCKZjePA36hcqm7zwBKsa1F3YT_I2pKmW3fTONPZpWozUoUkRuGHJ09FSPlfSShBSBCexQff_deUhNmTK51c5OVF9ZeXU3HKO8Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلاتان ابراهیموویچ: "بین این دو باشگاه، این سوال پیش میاد که کدوم یکی احمق‌تره؟ لایپزیگ که پیشنهاد 100 میلیون پوندی رو رد کرد، یا رئال مادرید که 100 میلیون پوند برای این بازیکن معمولی پیشنهاد داد؟"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/101937" target="_blank">📅 21:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101936">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEYtJeNl9T56DdCwzO7av8gKq1E-Gqj1x0f0NrrY8479wNndrFVuy3hsi0WUBRm7V07sychyPTkRD3qe3VTZgUHZ7JvoLAbX2lutpBUZ6EVvIpg0s3hNadQXreXWPJQjfk54mDm0XxcUrk9prCGQlSRGoO0alISUyMXT2j_ktF1VRrtoTikXBACnu9zqam_FayUQ9cxfAXrspYsREgl971zJuqqQdKqTWO3NUpc6RZoJUIdx-eZVhbDH2bY112Dcm1wzIV5iYpDAFwDANhf7wS4RR2QZjunKW9dS4g6CHcJqFvXib8pBb6NNPf-fKIIABNJOi2l7RM482VjN5NM5jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
محمد خلیفه، گلر جوان و ملی‌پوش آلومینیوم به استقلال
پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101936" target="_blank">📅 21:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101935">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IsBWmPwg0PdTMjWLkBpSMme4xi4v1Jo0VzFJ8XNaxieYKF6lPpdFGIx12_lI4TUqE83C2XV2mc_Ceg00hWXJgca31Hln6qc4E1SG-ajJKRNGkwNs8Osxh1zDQGVSRlYFzp8txHjwYYuDYLOeZ0wVx2-FfE7bfuyqOM-ZcwvJHiYYT2L9a1mEvu0h40yLYdGRWDHsrIafj-7MARKX8rRllZ-jzTOtzomDrZv4kqZVq9nfhuhTssgYkJWzKJ9Y8KeijwFvZnsBhLzQZBKnG6EmeLOjkIqJJaCqsoQCinxrZvhCmEwN8Ii3ugjHS-vh5sMaNS-dFralg5u3qasjXrS6HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ماریو بالوتلی:
یه بار زلاتان ابراهیموویچ منو با رافائل لیائو مقایسه کرد، ولی جوری حرف زد که انگار می‌خواست بگه بالوتلی بازیکن خوبی نیست.! منم فقط یه عکس از جام قهرمانی لیگ قهرمانان اروپا استوری کردم و زلاتان رو تگ کردم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101935" target="_blank">📅 21:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101934">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5BdOWd8H-zyUgrGt_Rhw58D3l1Ki46xOTB0lSvxs4YSqUVpgJd_d4KnjCZGkABnatdr8LGXqI3I4_GNrZWaFbRdyWi6oMYyYrCwU-OZKL1duEPMmTrDsA2K3QJuqOW2PC2ROhoNlqukpHcTED4vs_ZQFegrxozr8DMyIbyuL4ErUf2o3uButQe2gDlyBVFKs5rPD1wIt1X0KEvSiGTipcbfWpa_xmngFSXZoTmx-2cbt4qvusDRjY1zSqekvhu4AKcanmCZ4wH4g24YVangk9EcHze2lTlrVpjF0jC7FyFLx3DEo1fcK6DQpdatN6kOS-plICQInbXHGt-5Ke8T_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
کریستوف فرویند مدیر ورزشی بایرن مونیخ:
اولیسه به رئال مادرید؟ این موضوع اصلا برای ما مطرح نیست. او این فصل هم نقش مهمی در بایرن مونیخ ایفا خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101934" target="_blank">📅 21:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101932">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gA5fis5mbjI-M5C0_PwtF1BSVgOKvEQ06sek1f2bQtXCx9Cgq9sO9xM2OWoyubdI5j0_tN1CUGEqIn5W-kmwL5gv-aCMsucrpkBSYoxF5JleGAk46xDZ0stqD09QHLupB6CzGF7xeglLfFGB6vIFP6sl1STRIM1orRdnlX8CxclI-S3h6gn3e9z-PEWLHzL5JQ1h5HvAF0ybeB0iBfz9EfMJr4uwh3Ae30SujuLtDpsgx40D0XnxWRMCVDcePR0Qx_rvcijkKe6ssU3zSWoo1OS1NkkYwY4Frva_ihup6lwl873rKuBIUetH0hveaEYBZp4_R6G_Zsa9TdriPfFiCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Onj9qPnvHKUaNZZyK7JiTXa53kvSCxaNmtmAVv3WMq12p8Tf5CkdzbIGW6TcnT5ovIiyj7OxB2UBwYGTENmDf3OHkx_HqJvG3G1M9eDASXlsiJlwSvF--_MV7ZNc669MnPRePxjOlp0RcHQkTtA7W0i1IKZxeF89mPZCdK5XhDWtYYUe5jcVqac7fnP-6SbKgDGVvWprxy_g0KILGt3hVhynxclNOnL4RkaC_ATH7nqvUsg-ALWdTx5kJoHM4gtIYYE3TBG8FTNHNgvguZQqusCapAA62PhB4t0vyr1ijL1SR4S13LsZaIz6j8so6auhRCYGrOY6wD-8r-S57NHP4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
براهیم دیاز هم از پارتنرش لوز مندز خواستگاری کرد و رفت قاطی مرغا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101932" target="_blank">📅 21:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101930">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JEDulB_7pzaDW39DpyHIV22uqbI52LSgqkhtYG78rxaHJr_bMC_jDqGK7Tr8rsvGf1zMNjDnZtiGdXlApU3DT84tG8VbYXzKpO-DPWd76yPwj-V5QC23JVDS70oHLvBbTmwBWLrG4hDzf9kUOKjH_bsEnHk0NLwljtWH5XEK0Gil-hFiiyGHW4qFbCVxTjMpkxHd8hLSb0KofmFyxyWB88KuW4C1bY0RuyK61dxel1-CurEG0lq4ItjTt8BlkeptIKp4XaBbdOJ3Gl14T2JSlINPxjekBJCQpcIDO59ofDSpxFrRI3BqYZ-U-ca1ElKxkMfiyhIvBeGJ_Ux_t_dLyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2c2dac8e5.mp4?token=gVJeFImaHyR3orXOMRD9j6vpr_PmJxeuesiDvd8Xeqa2hGWPIeKE9dIWR2KnzSqVnwI2RQ1wfm6Ned0MShka3SrF11j8AH5V0WmTrmTkpiyH-kpN2Mckqlylmoquv5kaDvZandrHK2-bpWQHju0Bhv_BuzFBnmzzWn-j_MG03L5Sh0MRNJXwoj32Xxv1Nui4vAJAuO-yHi9vFstk8NtevYWHlPxI80kvdvZSRgGM28kOPyn1FwrE9JGAvF16oDg7RM92V0oF_8rSnf3ZfKug_VGMQvk6MpxWaUplwShHRmgFjgT8HNoB5CmFZHmRB9nakSpLrIfiyhuO0Z98wzitoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2c2dac8e5.mp4?token=gVJeFImaHyR3orXOMRD9j6vpr_PmJxeuesiDvd8Xeqa2hGWPIeKE9dIWR2KnzSqVnwI2RQ1wfm6Ned0MShka3SrF11j8AH5V0WmTrmTkpiyH-kpN2Mckqlylmoquv5kaDvZandrHK2-bpWQHju0Bhv_BuzFBnmzzWn-j_MG03L5Sh0MRNJXwoj32Xxv1Nui4vAJAuO-yHi9vFstk8NtevYWHlPxI80kvdvZSRgGM28kOPyn1FwrE9JGAvF16oDg7RM92V0oF_8rSnf3ZfKug_VGMQvk6MpxWaUplwShHRmgFjgT8HNoB5CmFZHmRB9nakSpLrIfiyhuO0Z98wzitoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
برگام عجب سلیطه‌ایه این! اینس گارسیا دوست‌دختر یامال، بعد از موج انتقادهایی که به خاطر جدایی از دوست‌پسر سابقش گرفت، یه ویدیو منتشر کرد و گفت:
من به خاطر پول یا شهرت لامین باهاش وارد رابطه نشدم. خودم درآمد دارم. از وقتی با لامین وارد رابطه شدم، بیشتر از چیزی که اون برای من خریده، براش هدیه گرفتم. کلی وسیله گرون‌قیمت براش خریدم، ولی اون فقط یه جفت دمپایی برام گرفته که حتی ۷۵ دلار هم ارزش نداره! بعد هم برای اثبات حرفش، کتونی‌های گرونی که برای لامین خریده بود رو نشون داد و در کنارش دمپایی‌ای که لامین براش خریده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/101930" target="_blank">📅 20:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101929">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CjzcXpm_AVSWtBKNdRgeFjCdZbP5hRXDTdxnEFsZxloM-T-r7NEAtiX1flUwHjgxAiOoNJtv5NAXSN-2rGH7_gTSfO3H5k6R1VPs1f9M2y1yaiUW6NBgNtKL-f-gHKCWLB7QCrdqqxmkXY60YRW2Z7hAAdJHauccRgBkGMaHez6_QR3sXQ_sdwq-VgLEkZfvrTZCL2RqGYyll6dD40PJSsuVaatNaNqS3BckKJWUSc9dQFD6JxPzebT8LxeUu2RvXEwfjLJaRoy0m7N-VMj4a2kc6RUKtDsA3nZ4iV8zFMQSi1G7PNHgQ0PGiDNv7zuK9scpgEO6lQ-OADH5D255tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
پوریا لطیفی‌فر هافبک گل‌گهر با قراردادی ۴ ساله به پرسپولیس پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101929" target="_blank">📅 20:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101928">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62941770b7.mp4?token=lE9MOw-_xBxM0Cu_4HPQyRdY-To2bGhmC2IP-0siQmon7FQYrHZWtdm2CCP4o0_latGlt1CFiv-0BQb9sGGDm87OYQQr05gI0uHMKAVhGtBYS4cYD9MBry--uOjRCEMfkCRCEr5mk3H_rxcZNmcmmzZwgx6ho36RvRGg2hqWnur6LolkYwuJ30k84Xgp7lUGkUMfiuA2NKILmYxWwc0JbualfaxH5R-GI9yj8JVg5KIDxbpp25bEiMp5t8meWw6SV-R8RIZpaYZ0xMt19BLLtkySeiSn1FjyOpT720ZTPKlEzy4tx8zEoxI8MTA42NT1GyX3huDgEeElHAxBK5XAKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62941770b7.mp4?token=lE9MOw-_xBxM0Cu_4HPQyRdY-To2bGhmC2IP-0siQmon7FQYrHZWtdm2CCP4o0_latGlt1CFiv-0BQb9sGGDm87OYQQr05gI0uHMKAVhGtBYS4cYD9MBry--uOjRCEMfkCRCEr5mk3H_rxcZNmcmmzZwgx6ho36RvRGg2hqWnur6LolkYwuJ30k84Xgp7lUGkUMfiuA2NKILmYxWwc0JbualfaxH5R-GI9yj8JVg5KIDxbpp25bEiMp5t8meWw6SV-R8RIZpaYZ0xMt19BLLtkySeiSn1FjyOpT720ZTPKlEzy4tx8zEoxI8MTA42NT1GyX3huDgEeElHAxBK5XAKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💎
استمرار، استمرار، استمرار تا رسیدن به هدف
این ذهنیت منحصربفرد ترین بازیکنیه که دنیای فوتبال به خودش دیده.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101928" target="_blank">📅 20:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101923">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o3EVh-RxG3LA5Ogzze8eMAxwuSETzpeH-wBr7cvPePJmsH8p-ZiM4BBBdMtYQUbyKmM-5dXOcRC2mZkjn-O0RfqQ0ADruS7hjmj6P-_KySZAu9sduP7tBo_Hz13gjepwONx_9PdOWCQSUxP750msBW3p4FeBK2kwoW6SmUGrbdTr_8IPATT7JBkPaYbTRE0PvFN6zCq2SqeEBRsOo62jqLkrF_b_qHT7diAS-W8P9tVcXwoEOa0h3PSuMXjTOEMvzuoyDJHX5egnS7w-SSLXSFj22ZWup8wnogX9ZfcsHBpkBeEbmPQJqI9mUEUptvfF6JZhF-KjDNePcQSLK6YFQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IlMs0TEhhumhLNkNb3-MwAdQc07DyssclFFulcABaqu78CWxOID-8QITsvOlTJdbwCw4tbrC2_BJgUcFe6iNiDaMNlT-woNnguCGXfyXaKoxxuYajJfy3vnV-a6xSDBWQ5iEOgbvnFAQGqisITvXgSwLIKpadnKi_YQHpmoXGPWwdsJBmeKR53eLIf1R9Au_JqbJ8ez2hiwv2Mr55HMf_GNo23KJzjGPryYCd2IfnpRd9EJG-aUCwfAKB3pnnryptZePMJdefkwyfghqA0Iz8Qb_-hmtHGZ6GcjeNl4gZN-JKYr1X9TlSC0-HCsgo7VsTANevEnoJM3tQ6pAfbYssQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hC-vo_narq6s6O77LF9BFtVwyL8jV3c9nkZ4h45allrBI8s8Ipngh6S39nlc5XGwo3D4B_gclBKoksOBpEOEerxBrxVQJbayPzSscihb9F6kpGuwy4mGbnD3u5VkZYkg7KXcIjOwXwA3_CvnGCiaTGsgRIMxM76XOiv10-VzjZQv_WW3MtYoSRDwg7z654fT4cOvxJCR5hBN2j-cqYKmEV1aE6-j_8_GCdBPu7igOVnRaQaSvdKhP8g1qV3gj1rsASgS_RXDbOkbfYvZ9c32YoM2dHb7LkRqK317KolL3hC4dBGUkGP0VgvoC3NNJoWIVEb_P7dvCVkPKxZQDjRqMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91c7199c9e.mp4?token=NZ-PQ5uFlfFFUT_SSHNV7BQnMgcaLde4x1g26zIdCMh_KJkhSwFoTkmJe_awibS5tAepcnMJWtdON3wQuQrrw3nOcMMqocrVi-ce0yWMEUAYjWviHSz74NcdK9VTpmfnJFvr-s_rg8JKc3eE7G3ObShXbWTWWiYq40DQQFQhX-jI3ctbYHWzoL7IftJ1uQmDcrjIuVCgZgKiCyJPe_hwpNdKQy4WVMXUCtiWUhoNUIGXrdk9CkGHrgGjIkHLtrcA0E6Ed6i1tU-mfITogOH-OzW0q3pEYQzbLbFBG-bn7ulvgTKh1fPdrdu7zkxdG-v1XAAHWWMNj9bQHNE-yaeD9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91c7199c9e.mp4?token=NZ-PQ5uFlfFFUT_SSHNV7BQnMgcaLde4x1g26zIdCMh_KJkhSwFoTkmJe_awibS5tAepcnMJWtdON3wQuQrrw3nOcMMqocrVi-ce0yWMEUAYjWviHSz74NcdK9VTpmfnJFvr-s_rg8JKc3eE7G3ObShXbWTWWiYq40DQQFQhX-jI3ctbYHWzoL7IftJ1uQmDcrjIuVCgZgKiCyJPe_hwpNdKQy4WVMXUCtiWUhoNUIGXrdk9CkGHrgGjIkHLtrcA0E6Ed6i1tU-mfITogOH-OzW0q3pEYQzbLbFBG-bn7ulvgTKh1fPdrdu7zkxdG-v1XAAHWWMNj9bQHNE-yaeD9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پدری تو تعطیلات در چین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/101923" target="_blank">📅 20:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101922">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1toO-5ydHWngHTfaxmoF2vAUF22Ytwh44wJOIil52_LVsktrgejipbAsOIBfTeKQbO10t11wWSQcy1IdII4KyDEJoLz9IhCYnCIr1T214L1X6fAn567WEEdHMPUsiSQ1-br73bRLL92_rSFwx0IYY0ET4Z_rpKDOvJXP3rgfSSDAGTCysvilMtryS033Pv4LnzSBOpkyy_9mCSISFPH0rpCagQTWPsPCDVpnJosCNVm7MUfuwemduaHF2lb7UmTJ4FJH_BMBWFdXl7DRAm308SauVGJy5Dyy6d50cGQBWm8NWdW4udD0dLQgOXkIc4e7ksCWJ8yHexMQa1QWfnRJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🔥
همه مدل کیت فوتبالی فقط 570 تومن!
🔥
⚽️
از کلاسیک‌ترین کیت‌های نوستالژی تا جدیدترین کیت‌های باشگاهی و ملی دنیا با قیمتی که هیچ جا پیدا نمی‌کنی!
😮‍💨
❤️‍🔥
👕
کیفیت بالا
💰
قیمت مستقیم از تولیدکننده
🔥
تنوع فوق‌العاده از تیم‌های محبوب دنیا
✅
دارای نماد الکترونیک
✅
امکان خرید حضوری
🚚
ارسال سریع به سراسر کشور با کمترین هزینه
اگر عاشق فوتبال و استایل فوتبالی هستی، این فرصت رو از دست نده
👊
⚽️
💚
کانال تلگرام برای دیدن مدل‌ها و سفارش:
تخفیف  ویژه  برای سفارش از طرف ما
👇
👇
👇
عضورت در کانال
https://t.me/esportsofficiall</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101922" target="_blank">📅 20:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101921">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fac07199b.mp4?token=p5F35hWWExs9ik-0Lr-zXuGhkMwiKWHGr_3yAyxSOEGVlgUioSmtVpGceQ4gvAPhIjCVl0Vij_K8gBi3DzIQ2hHlKeuXzpJW3BwO_Ta02-GTbxWTsg4zNTudUf6vbQee5KdFFe446B95DY9-YEFRBUMCiaOVQPaau5IXTHBGgfFcyz-p379px5COEOIllqiCGo_Pdt_7gUNDHuQTGx652wG8xzVYvyFr7rjYAIn3oCMtHl5HKDaydumgcmr3CWBjZ3Xz4jjVHgiv1240qZmfz4ZdQxWHr3I8bVQvSBexbyrLQu0TjKwk1e-2umaLLWWrp0iuL4E3rcmqWgiWjSAQdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fac07199b.mp4?token=p5F35hWWExs9ik-0Lr-zXuGhkMwiKWHGr_3yAyxSOEGVlgUioSmtVpGceQ4gvAPhIjCVl0Vij_K8gBi3DzIQ2hHlKeuXzpJW3BwO_Ta02-GTbxWTsg4zNTudUf6vbQee5KdFFe446B95DY9-YEFRBUMCiaOVQPaau5IXTHBGgfFcyz-p379px5COEOIllqiCGo_Pdt_7gUNDHuQTGx652wG8xzVYvyFr7rjYAIn3oCMtHl5HKDaydumgcmr3CWBjZ3Xz4jjVHgiv1240qZmfz4ZdQxWHr3I8bVQvSBexbyrLQu0TjKwk1e-2umaLLWWrp0iuL4E3rcmqWgiWjSAQdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😐
تو شیراز یه ایونت ورزشی برگزار کرده بودن که چهارتا کم عقل سر دختر دعواشون میشه و طوری همو میزننن که کم مونده بود بمیرن‌.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/101921" target="_blank">📅 20:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101919">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DhfxCHOIX8TlsWTpaX_G3pWpKdMo4N1ClVUNYcTSJofMRCcD-f_lCnBj97EslhDgF20sJ7d1APn0M-4X87Ge4nriB-HNYQMOZeSl6PMfcIXr-83aHs_XFDY7PYEr7VK63iLmykpBSYaQuX3AnrDjalCeKFm294elUzIItmNgbvTwEY2V9PP3Mk1mUD4FLaGnbQ8EAvL_nzhSChIh_rFCcZcTudS3M0GK8kuvObrhyjCp05Izcn-C7NgTpBe4RuL6eOw4FfPFnOSuxUsOHKQgIvkQSNTTq1hvM0FZ7fogm8wZ3gC71IZ-YsOt0VEypOA96wI3qM0AsmELXxWzCxQaOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vLxbpPeTiSv5psgOt5iQxTyCniqa49n6hRDCZx3JD0sSKMMa_OMgnc7G8A_RR25HCYLkvEA2A-G3mBPN7q9F4Mml-A8oKB04tenoT46Emj8XfGdXQ7jlBz4ZbsDsuYP-gAjJzIW0GoWt38ijG6gq0GcF6O-m2nmiRxtSQ49jMwara-gLfEjYL5YgwvdHBbfnMZtPVhwkUDWuG4EhyG1alqla3PjRB-sTcZjbBmgUQTsPVLArhsWGuZRxvTX9agabFc5ml276rHDtFP4NbY5ni_DhczgjJ-q7GkviL_DQC_WZBX0Di0uf2rtHjuLFbJ213ozl7fd7DLyLCTEfuWsmxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🇪🇸
فرناندو تورس یکی از آندرریتدترین فوتبالیست‌های تاریخه.
افتخاراتش شامل:
🏆
جام جهانی ۲۰۱۰
🇪🇺
یورو ۲۰۰۸
🇪🇺
یورو ۲۰۱۲
🇪🇺
لیگ قهرمانان اروپا ۲۰۱۲
🇪🇺
لیگ اروپا ۲۰۱۳
🇪🇺
لیگ اروپا ۲۰۱۸
🇬🇧
جام حذفی انگلیس ۲۰۱۲
خیلی‌ها دوران سخت اواخر دوران حرفه‌ای تورس رو به یاد میارن و تمام چیزهایی که به دست آورده بود رو فراموش می‌کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/101919" target="_blank">📅 20:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101918">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OucxWF_vFhd3jZMNwZqEaD3EgfU3wvSLVylajSEWTxyRQTb5_RNfUA9Epw4YxL94GU1cP90xEFLW_6ABu14rxOSmhEpNMfJFOnCAB689SDGko_749K7G8_qSYp7F7xEMDp9Y2uz9T8BcotnOov9XGsmzx_riklTmVGgBDOwfj_hpgjdf0Yj924Lqd3nSQzQ9pcvXGEu4G8sBcKRqiXRXclKjFtGkrM9SmfYS0YU3DozlRsLX_Q1JNfGh8GJC9cba8DXWkn82BKq2OX1dY6dY7aaOOsmx0c1oCxyOebfqI6zR-isUX44JOR3EC9H4UgDFPifYD_nlMnLOAPFpULJf4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
اسکای اسپورت:
هری کین بلافاصله پس از پایان تعطیلات تابستانی خود مذاکرات را برای تمدید قرارداد با بایرن مونیخ آغاز خواهد کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/101918" target="_blank">📅 19:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101917">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/779a683584.mp4?token=hEQARU_7TuvcKJYzRheCwB2QToxEUg7FhzNloFWX660uP6cXX3rYtjH3QisGuMO7hm8--i3DzsXMa6QOBsdhWNu0at0KOLmfdFvqhqmc6yf5xp9Qrpb-6mqCviQiP5rHy0mH-sc_2dKGNMW0fOtq878FuWvm7ErTmIvIwTrp6-wqh_92ojt9YRBNht0ekudCrCbprgz11bVIY1DWtvHNgCc0kqxtJ6kF2gfGBue5Ufrx5H7RA-RX-kT1UgUsxYhONX0j-RkgjiXvrL4scXosgKsSRQV31myLff4H38VRqw5-EgTwciVZH-TUEFk29GZn8tkFIfITW9fE3DqYL5htDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/779a683584.mp4?token=hEQARU_7TuvcKJYzRheCwB2QToxEUg7FhzNloFWX660uP6cXX3rYtjH3QisGuMO7hm8--i3DzsXMa6QOBsdhWNu0at0KOLmfdFvqhqmc6yf5xp9Qrpb-6mqCviQiP5rHy0mH-sc_2dKGNMW0fOtq878FuWvm7ErTmIvIwTrp6-wqh_92ojt9YRBNht0ekudCrCbprgz11bVIY1DWtvHNgCc0kqxtJ6kF2gfGBue5Ufrx5H7RA-RX-kT1UgUsxYhONX0j-RkgjiXvrL4scXosgKsSRQV31myLff4H38VRqw5-EgTwciVZH-TUEFk29GZn8tkFIfITW9fE3DqYL5htDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
رونالدوی برزیلی سرعت یک وینگر، قدرت یک شماره ۹ و تکنیک یک بازی‌ساز رو همزمان داشت.
🇧🇷
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/101917" target="_blank">📅 19:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101916">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa3ffe3c02.mp4?token=GhVTpfgGzb42lixBphMjgOOpJdb5ep-YeVE-QwRt6cKfE-3DdO7Eh_gkF0rDgUaYovVkJRk2aI75YON7OVM2K4I8c97iSgAaKowS5YbpwCQ40zjEk2QQgCI5hFuKhMWPGWckWqqED_XVHL4QnxCcjBDtiPxBesADRvAls3AdwHq-Fn9PZWVWf_BMAt2PB-QtywC77EVBK5nGowSIZVXUHjG0RusylZO3Q16XAdDhqaqczn5NrYN3JnAxr6zQiiQgIcXrm5JCEy67gNaCvjIYXi1mD9UC_oIIwMHj_oWdT-MFzq8B5y4U3YxWMIB4pB5YF_8wNDBjKHa-tFHraVKI8FUZTSmurAilEUnYpQ0uhL_PAE8j5sCATBteLdbtgRD5XrF0tyaRuUIE-GvvUJWbsvHpUtGyTCm547JCcvldYKOIjCop5itBpDge3lggvQRX2Y1saFzQsjgKef3TmXSCNAHV76-LeEVKx4MCGnLevF6MFHucNKKlP8zjgv1tILMu4zqcR6ajr28xsc5PRnMRAmR7nmebvZGl5U6IBq71m-pmFO4K1m9slpWYEmDBos8j0l_HBMsWnox63Y4eixCQbEKGTvfnAry2Jss4U8C1xIfsrH9COaQa52SCBiLI6Etzd3hvgb4d4acTte83Uz-xFU6pmuyHJ-8HJU2sVvxFoHI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa3ffe3c02.mp4?token=GhVTpfgGzb42lixBphMjgOOpJdb5ep-YeVE-QwRt6cKfE-3DdO7Eh_gkF0rDgUaYovVkJRk2aI75YON7OVM2K4I8c97iSgAaKowS5YbpwCQ40zjEk2QQgCI5hFuKhMWPGWckWqqED_XVHL4QnxCcjBDtiPxBesADRvAls3AdwHq-Fn9PZWVWf_BMAt2PB-QtywC77EVBK5nGowSIZVXUHjG0RusylZO3Q16XAdDhqaqczn5NrYN3JnAxr6zQiiQgIcXrm5JCEy67gNaCvjIYXi1mD9UC_oIIwMHj_oWdT-MFzq8B5y4U3YxWMIB4pB5YF_8wNDBjKHa-tFHraVKI8FUZTSmurAilEUnYpQ0uhL_PAE8j5sCATBteLdbtgRD5XrF0tyaRuUIE-GvvUJWbsvHpUtGyTCm547JCcvldYKOIjCop5itBpDge3lggvQRX2Y1saFzQsjgKef3TmXSCNAHV76-LeEVKx4MCGnLevF6MFHucNKKlP8zjgv1tILMu4zqcR6ajr28xsc5PRnMRAmR7nmebvZGl5U6IBq71m-pmFO4K1m9slpWYEmDBos8j0l_HBMsWnox63Y4eixCQbEKGTvfnAry2Jss4U8C1xIfsrH9COaQa52SCBiLI6Etzd3hvgb4d4acTte83Uz-xFU6pmuyHJ-8HJU2sVvxFoHI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یکی از مصاحبه‌های چندوقت پیش کریستیانو رونالدو که اون گفت او قصد نداره یک‌ روزی مربی بشه و بیشتر به مالکیت یک باشگاه فکر میکنه. او همچنین درباره اهمیت مراقبت از ستاره‌های جوانی مثل جود بلینگام و لامین یامال صحبت کرد و گفت باشگاه‌ها باید به رشد و آینده این بازیکنان توجه ویژه‌ای داشته باشن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101916" target="_blank">📅 19:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101914">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrar2rbAcXksX8wcSx5ARODDDAOoCbWZAks4oHJI7Wfikkf77KYd9rogDsO0uf3zyddUcXQxIJX8EwcoseJZR8wdKJ7Rp44VmKXqIKrBwELg8jsAjlVWBUl3oET7eSy6NEjBafbHrIiQSyip5Ui_12yLxmwl5LMS_eugyqJngcd4f_tA11BGmi_mk3PYKkfsFBsKZ5LaORj60hp2fSsyOOTB-unHEI4Qli15gGgElqn4m34wDbXjL1fJN5cBF8X8_cLhnqcerkohl0ut1OxrbZFz9XPG861JQ4ugmaCY2GHYIYjUygs_dIluFrqHjDxUiD1YUCjcr2TBGbmj8UlXww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9c742e9e0.mp4?token=VnXysFx8CAe4YjUNqdAjTkmOztkIzHFJ-E-F6EnkuxAc_kLvRKFoNbzpd-DUPIpRDVm-SylBQ6Bc0uvVxO5z5cjXEbtsRaXkSt8VKRS7at9DHmTXPio9u1USrXjzHHhL0TRm8omHBYnDSMGu1H21Cl6PP7MOVulz4pMXscDf4W1B2_s6bM2wCaGjDiLO9mURLIzK8VhnUSmqtKyQ0-tYIuAxNc8eF0RM-u3MLS7ExAKeAM7mvh7aAoV8DHpX-Fm0H6CBXXHs00NULlV1yKRdP3Y2ucL_jBCNXTZrfItvYsl0LRhATlyKJWs-TYRum4qlMM_qdQ72rrGscNQF3Ng5FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9c742e9e0.mp4?token=VnXysFx8CAe4YjUNqdAjTkmOztkIzHFJ-E-F6EnkuxAc_kLvRKFoNbzpd-DUPIpRDVm-SylBQ6Bc0uvVxO5z5cjXEbtsRaXkSt8VKRS7at9DHmTXPio9u1USrXjzHHhL0TRm8omHBYnDSMGu1H21Cl6PP7MOVulz4pMXscDf4W1B2_s6bM2wCaGjDiLO9mURLIzK8VhnUSmqtKyQ0-tYIuAxNc8eF0RM-u3MLS7ExAKeAM7mvh7aAoV8DHpX-Fm0H6CBXXHs00NULlV1yKRdP3Y2ucL_jBCNXTZrfItvYsl0LRhATlyKJWs-TYRum4qlMM_qdQ72rrGscNQF3Ng5FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
طبق گزارش‌ها، لائورا ایگلسیاس، دوست‌دختر رودریگو دی‌پائول، گفته او حتی ۱۰ درصد توجهی که به لیونل مسی دارد را به او نمیدهد. او مدعی شده بعد از شکست در فینال جام جهانی، دی‌پائول دیگر حتی کنار او نخوابیده و رابطه‌شان به جایی رسیده که به فکر پایان دادن به آن است. گفته می‌شود او معتقد است دیگر بازگشتی در کار نخواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/101914" target="_blank">📅 19:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101913">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_FqCJPYhvaqM7TmFH-jLt61omuYbOO1S1JU_ls64Hv02otT4m5HvTE_DR4wm0WCM-cobF-rQvHEgpvG_ob9muF7OuH4QP1o82bnLj3fRY-xQJFbE4e-JkQ-RdOpKIANx8IPUcFpopRN37Bo55v9zwEUDSX_wFemrD12HrUtfXPCRajq6E8g9o5n1MjylngGJ1ncoND1XUA0CupNMzCxDmSA9zZ0AaN08cuCsa6U79ZEhYanlCmwb0GjaHvMEEc8XRExVscv_C4Mq2HtG6oGtlWTCqxm-jCgUE8KUbRb8kgEnuDaK6hwU1O01IWQ286RRHLwSDNKAN-woOdrwxhKSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
تلگراف: ژوزه مورینیو با انتقال وینیسیوس جونیور به آرسنال در این تابستون مخالفه.
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/101913" target="_blank">📅 18:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101911">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eXkz3tTpmuwGGT6bGiB-5ICTijXWfhZcrSmEuB0Nw4cAepBgvKFp_Iku-b1q72untSdclrcCy6yix_l52_5F7ka6am8ojOKMTb9mFGEWupDWlEZ4KBYXa5X8jFoNyIM-eosCW3gdzkdHefAMiANGPNcyVFQxQGQ4xXxEb5lmrabUVdGkB9_FzchJOur6ilnkMr2jrx6uReMaxRz3ohXJppFV74o7ozQWT08nTzmShubNmBAC4FCLE6XtVx8ycFZD77lSVHuQNNc2UvdbKgWazMyY3TkvMJNSGczcOWPCfpNpcIWbenEWDjJAEcXo24rWET903zEl0LDJnaqHFYjAfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AjQRfO30rs8ysNHD8u-KUwR5mgdAq-N4AArnemFHYHMxSO6j4tt9EpSOvuUgQ769Cimbz8mB0Z8FMJVh1wGC7zRkeAEVt2w49k-vDhZ3vYeJ-CIr1oYVkQKjfbqBVVp9bE5cDdt71kHqI7UXH5LIdwJPP6OqLPuG1i9XBGOAu74fB4l79eWCt32E0mkn3eGVHrdLA9nCqkI7UBknT5LkQHt3I86E0yfYz9zDEXKACB6QeGj4QRQS3P0iuwS_q4JQfU-T1AgFUMT5zd-BC5kYC1UCPi6YqLwjsUgtea8AVfrgCq6JAD7jTbadbUkh9HVBnNzLK9lqJl13lxgYFXVWYA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚽️
رامون آلوارز:
اگر انتقال رودری و دیومانده نهایی شود، رئال مادرید ۲۶ بازیکن در فهرست خود خواهد داشت. در این صورت، باشگاه مجبور خواهد شد حداقل یک بازیکن را از فهرست خود حذف کند تا با محدودیت تعداد بازیکنان مطابقت داشته باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/101911" target="_blank">📅 18:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101910">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrbnbPFNV6w5CFaGezOjHhUxOSIbueWl4wByfGIFZdLfjdekibvE5BgRJyJ3sSrFj7lVlykB3H28k4dZMj1ZbxniFih1VQQZ7D07UCa6myj60DP6d69PZAXrKD1BahW4NGDYiEgUyU1nxPPZo41k9HgwZiOZNHLYzjbJhdYwBiwLpPXEtYPE9U7hlQUhj8rnzjk66e8iaJYhvPawdf7PccZbtk1hPRgZIkEiWKvjLWgoFrQu78NmOyOJR4TjaznbTbD7pMcRExQw3JUrmFH4rBxSA0RooPsQScOzkfPdWvg7CIhBxBsd3neFTSf9TroSNEL8kD3MS3H4s0TZrKBW5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با ربات هوشمند تهران پی تو ۳۰ ثانیه خرید کن
😍
فروش یووچر، استارز و تلگرام پریمیوم بدون احراز هویت و ثبت نام.
تحویل فوری زیر ۳۰ ثانیه.
درگاه رسمی بانکی و مجوز فعالیت
✅
@Tehranpay_bot
@Tehranpay_bot
همین الان استارت بزن و راحت خرید کن
تلگرام استارز با ۴۰ درصد تخفیف
😍
یا داخل سایت رسمی بخر
🔽
https://tehranpay.net/utopia/</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/101910" target="_blank">📅 18:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101907">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p7dTCsq929Jd0UvSrrWtQZB0nbHzn-ZmJOhLNT9FOwdElkqvI0nA0TIxLELLdmHCg3SdfJtNsuHpkNqX8ugChozvmmMZU4fvGmmwoOX2HukzbD6rp7dKaZjgrs5HgJvWZgJR_uiYyxgtX1Q5PFmpx4iCF0L1TnzcYaPmgU5n67yUhOj_be6YNstS5x-UwFUtqi0BwFRczs3_UHwm4J3suX9ZbOWoKvT1j0EEuH2IJSOD0VeGu4lYgxv_iUxeANSXZDiJ0SlNq7ANA_qPaTGbDN9I_spEPu5PvhbGPNGApcYpTR3YXRE07j3aXHNo-ILlQkiH46XhW68MRS_Ghznqzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iwwx_9x1tdDC3b0HS36s0ZWgUPZZ7yDF3FxpW9PIIOAsH6iCz_P0tcdA3rWRVdJGY3JKSsvDSw436eRbMzXl8px8dbjs9BCutqOFhHaM5t0FX7zHPBVmD100EuZZNHURPD7VKYLwBdWFQJK5u1SFboiDs1B8v_q3GUeuI8Gz-i7_ULwAD-W20aPZ0-fkdnra0WKWF65JqvwbBZjUDdMxt1SGhJMDGY5XMilDXkDBy_F0xRQ_9KOqjMuLyWXSZP30oao-IMQUOHTBDWantufb1puwEFVR2oDPvTJzCRiV-RH5gdhEm1MdYKafe9wxCPIzoc2ZprlQxV9CQ5_06rIh6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d05827d11.mp4?token=h0NMpj4cxsZFPa2fcZ5Ypr9H_EFXrI_ZCPsJAeg3yPeDiF_TEQlwooVYtvXV-BE_2JrsJwskK-fWTq3SXh8okK36hkIppFGyiqGVJ1gIv4nwAf3JTg1_LLyF04XwYjQ7UG4YtqKhtnA3dU06gWUMfF72JavYpx5gRb8KXOQShwj8CSlGLB-d9OKbPWa5iuSCaDJpQCUY5rRRYUrfcb5RnVj5-FWV6eWSr4JEX3Ih_lsG1I5EOmg7kazBgNFJVKzUyk0SwBfPZuHWIfQzEAcMSQX6D2PKXaXRukhqeTzCbKOYno6Ml4kIdpX9ToOru06G0g-VgjkJcy2SSrXny7Q9dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d05827d11.mp4?token=h0NMpj4cxsZFPa2fcZ5Ypr9H_EFXrI_ZCPsJAeg3yPeDiF_TEQlwooVYtvXV-BE_2JrsJwskK-fWTq3SXh8okK36hkIppFGyiqGVJ1gIv4nwAf3JTg1_LLyF04XwYjQ7UG4YtqKhtnA3dU06gWUMfF72JavYpx5gRb8KXOQShwj8CSlGLB-d9OKbPWa5iuSCaDJpQCUY5rRRYUrfcb5RnVj5-FWV6eWSr4JEX3Ih_lsG1I5EOmg7kazBgNFJVKzUyk0SwBfPZuHWIfQzEAcMSQX6D2PKXaXRukhqeTzCbKOYno6Ml4kIdpX9ToOru06G0g-VgjkJcy2SSrXny7Q9dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
رودری درباره جنجال‌های جوایز فردی‌اش:
فهمیدم مهم نیست چه چیزی به دست بیارم، همیشه یه عده هستن که میگن بازیکن دیگه‌ای شایسته‌تر بوده. وقتی توپ طلا رو بردم گفتن وینیسیوس باید می‌برد، حالا که توپ طلای جام جهانی رو گرفتم میگن باید به مسی می‌رسید. این بخشی از فوتباله. به نظرات مردم احترام میذارم؛ مسی و وینیسیوس بازیکنان بزرگی هستن و مقایسه شدن با اون‌ها خودش افتخاره. اما بابت جوایزی که با سال‌ها تلاش، فداکاری و ثبات به دست آوردم عذرخواهی نمیکنم. هیچ‌کس نمیتونه ارزش زحماتی که کشیدم رو زیر سوال ببره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/101907" target="_blank">📅 18:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101906">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cbd3d9241.mp4?token=eiWALpCdtFgChnX7RBgpqjpHcG71lBaa3zts8OcZLxTKpazVWANuqNwnJUhvlxgTEz5TJwJylJ_MEwW2Rg3ejlQYyBcyHh4sWN4KIrJF1S_S2YkzRUnLE_J95QhO_it2t69eBr3Z5Gv-8h3gN6-fmZ06sIW2ATPsnQS3eGRepzqo5on3mVMCdf5ExPZlQRZuPqetxLhZjcAIRtfohq3WSThOtYo6LXAhrePSrd8FvVFjZQNdIdfhsZGnT_pdJvAu9NrctgvioNLlyzRetmrYiLpOVTQIHzmC74w60o_QAMQ1I55oKF8LogXHtCSeu_x65kxv_nwQugHtGHhMhUa0Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cbd3d9241.mp4?token=eiWALpCdtFgChnX7RBgpqjpHcG71lBaa3zts8OcZLxTKpazVWANuqNwnJUhvlxgTEz5TJwJylJ_MEwW2Rg3ejlQYyBcyHh4sWN4KIrJF1S_S2YkzRUnLE_J95QhO_it2t69eBr3Z5Gv-8h3gN6-fmZ06sIW2ATPsnQS3eGRepzqo5on3mVMCdf5ExPZlQRZuPqetxLhZjcAIRtfohq3WSThOtYo6LXAhrePSrd8FvVFjZQNdIdfhsZGnT_pdJvAu9NrctgvioNLlyzRetmrYiLpOVTQIHzmC74w60o_QAMQ1I55oKF8LogXHtCSeu_x65kxv_nwQugHtGHhMhUa0Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
حالا که اینقدر امروز دربارش صحبت شده یه کم یان دیومانده ببینیم.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101906" target="_blank">📅 18:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101905">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff6a2da2fb.mp4?token=NyTMr-i2GGegTAHPq14bjfltURQwnD3i3dyVm_fQB3I7UiAxFx4bJGNxnDSscf0giypBIbc7iUApgisj34643b0Aqtd1v3vT-zb1uC0j9rJzdDWg9dXGPdX2ekYhsCTHuw18G075tOBXCEmaWfkDpPFpuZCd8b8fYzGtpFD_NXWszhKqr4pQIwfkNqCp5UtYVNPAvGYDQjCgYCwbotK_ly7iOgtdtcpmedxukhBPRLMlJcBguO6ls8XxONAoSRiKKJroJqkRR2ylCez_63OGCo9mudb38YITbWjw24iGVbWaAXrTDcNk85mc2Zl2xXrUuVEEp0mKKYqNZq9fbKy21JJFhJDjEOOTBevb6pQtyb46co_ISml3Lu-V9W6Bn0GxiVK1C6y_ZGtZEJ70_DTgR02nPkOjdPqgVqesgjX8Vbaa5VEaLNTEHzANZStgjYw0NM2XzUatcwp7bPC5qghOgkfA0yfLPUXapNQFL_zQLyu5-DsUcajIM52dwJ_ohXhi-zdsAzbxCSH8d28i6uNyAVZAesy1Y_0ofyntHd5N5RDGoV93eM9ZmqHYRChActZEVeh41rmpqVQyiL6cu2kIE2QH4-Jo4l-VJvYIlQcI3SFgNm3JxDGrc5K2640bviqCJJO0hqQr8moYSPlJDIboWDE2kbGlNd3WvargmCLyMNs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff6a2da2fb.mp4?token=NyTMr-i2GGegTAHPq14bjfltURQwnD3i3dyVm_fQB3I7UiAxFx4bJGNxnDSscf0giypBIbc7iUApgisj34643b0Aqtd1v3vT-zb1uC0j9rJzdDWg9dXGPdX2ekYhsCTHuw18G075tOBXCEmaWfkDpPFpuZCd8b8fYzGtpFD_NXWszhKqr4pQIwfkNqCp5UtYVNPAvGYDQjCgYCwbotK_ly7iOgtdtcpmedxukhBPRLMlJcBguO6ls8XxONAoSRiKKJroJqkRR2ylCez_63OGCo9mudb38YITbWjw24iGVbWaAXrTDcNk85mc2Zl2xXrUuVEEp0mKKYqNZq9fbKy21JJFhJDjEOOTBevb6pQtyb46co_ISml3Lu-V9W6Bn0GxiVK1C6y_ZGtZEJ70_DTgR02nPkOjdPqgVqesgjX8Vbaa5VEaLNTEHzANZStgjYw0NM2XzUatcwp7bPC5qghOgkfA0yfLPUXapNQFL_zQLyu5-DsUcajIM52dwJ_ohXhi-zdsAzbxCSH8d28i6uNyAVZAesy1Y_0ofyntHd5N5RDGoV93eM9ZmqHYRChActZEVeh41rmpqVQyiL6cu2kIE2QH4-Jo4l-VJvYIlQcI3SFgNm3JxDGrc5K2640bviqCJJO0hqQr8moYSPlJDIboWDE2kbGlNd3WvargmCLyMNs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
تیم رئال مادرید در دوران پرایم خودش یه شاهکار واقعی بود؛ به طوری که تقریبا هر بازیکنی، کاپیتان تیم ملی خود بود.
💀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/101905" target="_blank">📅 18:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101903">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/virCfL5coZz3MGNB6eZSpszrjsvuU2pxswnyATfscf3sRlvBEEDNbKJaWWIecc7jMXye6iigsowu0rdVWgS93_v6ql4k6Z9IPu2kCstxSlE8bE9DSW4Hj2p_2JtxL-T6EPPL8pfNWNQwe8Kg7hvFMu_f2b-sFLdknM9_Daf3U21dmVbnAYmlhRgfGVOjn94Emi_J-L-SlMqBrbI1zkL3qzTgBEAIVNXyI5odLvGBOEmx2l9H0kA18oFR_Rzeyu8GWDYMKVq2XLeuRiqVXbXcItnXB7tOMiyNchQaSXP4BZKlE4oNjKYiFwdIFY-WKuTITpIvXX8FpuYRdTpQByYRig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
کاکا درباره دوران سختش در رئال مادرید:
من از میلان آمدم تا بهترین بازیکن جهان شوم، اما مصدومیت‌ها و رقابت با بازیکنانی مثل کریستیانو، بنزما، اوزیل و دی‌ماریا باعث شد کمتر بازی کنم. حتی امروز بعضی‌ها من را یکی از بدترین خریدهای رئال می‌دانند. اما آن دوران باعث شد خود واقعی‌ام را بشناسم. کاکا می‌گوید نه بهترین بازیکن جهان است و نه بدترین خرید؛ بلکه همان سختی‌ها او را به انسانی که امروز هست تبدیل کرد. فلورنتینو پرز هم هنگام جدایی از حرفه‌ای‌گری و شخصیت او تمجید کرد.
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/101903" target="_blank">📅 18:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101901">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nAHy9SswW0Xfj_Wv79lCcxr9aB_eflSE9VAsdwbRT2f7R1SwAysDzVfr6S37pqcjqV6QD1Aoor_huRlM_2Dn1336IM7da9zMgzkmly0YsvcgukIGxDMgv46xN6kaNBOhWGrq6y_ldOX2WB4hzi3PmQyUjkiQfS2ttfVmXjVxsdUi5cw_wDTGSQo2cQ6vu986inp4u9d2mJ2DxVfDHScYw8_MDlLwThOSP81MqEa8HsTn1k7fc7htrv4nk0chTLw8lifEDro8jL7dPlOMynCzebepomuCvpqR3omAD014g7qcpgNKmgxRYond0FwNjcRmmwH_ImdwxyeIGYzXYidrmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X8b4zRd_xRLiDSg1XLVfPcbwdJOpETb4NPNMNa7cd95jzCSjEVMNu0IVF-basXScOc22L26G-L2FkIJtaKXiUpM-CbgHxtL5SZ-kGXONFfocc_AuKYofmGAVM73EKbCf8ofvfZTzRh7wCtCBDXBEX-Scnx6waU-SOhyvHR2AaNAu3Q5f5Thyr1sxYhdS1ooBiJIvpmeO3kj-bWzKJZXLY3JREbC-R74tdKtt5lJX7GkFzcRHv_vxqWsDXc_1Pc8yqTVSZEhmI48-r94aJADXLqys7C7Jn-UREygpSghcHAyWGDZqTakX9SUoM75IkhZivjdJo3HD5WiggjV2l0HBnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
یان دیومانده درباره گرفتن یک پیراهن تقلبی کریستیانو رونالدو در منچستریونایتد به عنوان اولین هدیه تولدش:
اولین هدیه تولدم یک پیراهن منچستریونایتد بود. توان خرید پیراهنی با اسم بازیکن را نداشتیم، برای همین کاملا ساده بود. خودم با ماژیک مشکی پشتش نوشتم "کریستیانو رونالدو" و شماره ۷ را هم اضافه کردم، چون می‌خواستم به خودم انگیزه بدهم. هر بار آن پیراهن را می‌پوشیدم، تصور می‌کردم خود رونالدو هستم. فقط می‌خواستم از همه بازیکنان دریبل بزنم و تا جای ممکن گل بزنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/101901" target="_blank">📅 17:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101900">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b492c31a81.mp4?token=XAR8TdCMy8ak5fsgzkBdAjZGiQduG2KHMnTt50a7T1DVi9izYTzw2VhIkRe4JtnT0N7ZuOSAGFoJRWqnKLQUJ734Hd2x49oW63-ld5nkgGz0i73w5w9N44hm8NtNH-qvY2ZxaGU5wrSTsqLREvqlf-ZmExapUXAFd4OJrGMqkYWIogwS4fHMh58_gYxLw-UJw-iUWlCUMYgeV5swMyeAm_Ni1_spBNiP3XkgVDCJdzhBIzKfMZFwX8gCMQsj3YDTN32YKX8WkcJW1tydpLTM3mqotffTL-aHd1WoaYYD0vB356uQHScIN1-2hNACbiNjtNfL112689y_F_fxssFYoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b492c31a81.mp4?token=XAR8TdCMy8ak5fsgzkBdAjZGiQduG2KHMnTt50a7T1DVi9izYTzw2VhIkRe4JtnT0N7ZuOSAGFoJRWqnKLQUJ734Hd2x49oW63-ld5nkgGz0i73w5w9N44hm8NtNH-qvY2ZxaGU5wrSTsqLREvqlf-ZmExapUXAFd4OJrGMqkYWIogwS4fHMh58_gYxLw-UJw-iUWlCUMYgeV5swMyeAm_Ni1_spBNiP3XkgVDCJdzhBIzKfMZFwX8gCMQsj3YDTN32YKX8WkcJW1tydpLTM3mqotffTL-aHd1WoaYYD0vB356uQHScIN1-2hNACbiNjtNfL112689y_F_fxssFYoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فران تورس تو تعطیلات در کنار بکهام و مایکل جردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/101900" target="_blank">📅 17:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101899">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51f2886d75.mp4?token=bEoTc-ou1hz4cnbnLOzVNntdTAkHoQsDYIdBakJOJdCkPF1i5hNKSSjSeeFcfVDVg-gQrxCO70i7gqQGTZMZA2WXL9Ca7orQvOaYFC8aIZUcg1SF6iYjN00bB8tEWQAN7Kxka7gAxCWcpN3zXQ66jt8nqea2Ju17aFPSSmsex_rB1rpEjF46bylewspg7L39B3wtkIFk6TNJ9ZI7kqvdDJ6pz46T4fHaW_hDT_CVk4VIZiJXo0eTgsu6JYq-OVFh1XjxDSWq_s7ikVcFcJzFzpg2EYS-OvrttwLDdepg3OGz7FLhlxKcGD8c_amDC2HkT1HetQC-_fzBlzk_wH0MdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51f2886d75.mp4?token=bEoTc-ou1hz4cnbnLOzVNntdTAkHoQsDYIdBakJOJdCkPF1i5hNKSSjSeeFcfVDVg-gQrxCO70i7gqQGTZMZA2WXL9Ca7orQvOaYFC8aIZUcg1SF6iYjN00bB8tEWQAN7Kxka7gAxCWcpN3zXQ66jt8nqea2Ju17aFPSSmsex_rB1rpEjF46bylewspg7L39B3wtkIFk6TNJ9ZI7kqvdDJ6pz46T4fHaW_hDT_CVk4VIZiJXo0eTgsu6JYq-OVFh1XjxDSWq_s7ikVcFcJzFzpg2EYS-OvrttwLDdepg3OGz7FLhlxKcGD8c_amDC2HkT1HetQC-_fzBlzk_wH0MdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر شاهکاری یه کپی بی ارزش داره
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/101899" target="_blank">📅 17:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101898">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fe82274ba.mp4?token=ABaWCVO7uM7ry8hQ_GS9mHkERoywfnXWZosesPt3wj2IM47vee7KbmYSHTVZeFkW36LLWC5H681gjoqH7hVqqJuVv1DsXRdSyFbiwyWkuBPbRPw8WQGhp-T2EIF2TGUATIp5DsPsAe6Y5TQf52I86P9GCjdW9rDTd7IXeKuHbZilKTsn3-qXz7vxZZoA40EXaMIF9_nE69CYcCPKH7qmG3dOKsm8BPSmVwhmKKHVZZLOS1L7OQs8W1Wxk6I1mSa1cyh_hQnrj8jc9JbogKgOhIAt_7ahN7jJ8dUJ8JdfWsuEedQRZOaOzK48bDKY8_FXbDIegWB7wpF5zPh2TtID3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fe82274ba.mp4?token=ABaWCVO7uM7ry8hQ_GS9mHkERoywfnXWZosesPt3wj2IM47vee7KbmYSHTVZeFkW36LLWC5H681gjoqH7hVqqJuVv1DsXRdSyFbiwyWkuBPbRPw8WQGhp-T2EIF2TGUATIp5DsPsAe6Y5TQf52I86P9GCjdW9rDTd7IXeKuHbZilKTsn3-qXz7vxZZoA40EXaMIF9_nE69CYcCPKH7qmG3dOKsm8BPSmVwhmKKHVZZLOS1L7OQs8W1Wxk6I1mSa1cyh_hQnrj8jc9JbogKgOhIAt_7ahN7jJ8dUJ8JdfWsuEedQRZOaOzK48bDKY8_FXbDIegWB7wpF5zPh2TtID3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زیر ۲۹۹ هزار تومان با ارسال رایگان!
🥳
با سرویس سفارش
یک نفره اسنپ‌فود
غذای مورد علاقه‌ات رو با
همون کیفیت
ولی ارزون و به
صرفه‌تر
نوش جان کن.
😋
🔥
از اینجا سفارش بده
👇
👇
https://i.snpf.ir/wopv1
https://i.snpf.ir/wopv1
https://i.snpf.ir/wopv1</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/101898" target="_blank">📅 17:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101897">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e5e82a980.mp4?token=iJQ7tB_6YVj0yKqBu7VaKnXXzmo2qbjPBRYL6CAb_enGnE2bMl5WK8IBPXekjM903eybPwZhIPxmhxytWgj8-nWZDwrlhomN6PnSWaUudX6WQL359NTf2Xv_uH0J0Ko2rzp2BQFjIhvJximQlSAzioZCZ6F3UXlYV3gHbDFEBSGRrhOOgxyRTaIWSX_C6m6NFI_zZXHzSDV9vwd6dwSdDxyXkRuB3eOcPEe3kBbfMqear0kJkSq6faE6ZdFsM7aU5qKfjzEF2dSAfyuLR1zXV-cuZFM10UPUGe30_ciT8m0cFrdTt5qjApeprkaohjFvqBc2cBgZHUm7uZ2VpQjr8IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e5e82a980.mp4?token=iJQ7tB_6YVj0yKqBu7VaKnXXzmo2qbjPBRYL6CAb_enGnE2bMl5WK8IBPXekjM903eybPwZhIPxmhxytWgj8-nWZDwrlhomN6PnSWaUudX6WQL359NTf2Xv_uH0J0Ko2rzp2BQFjIhvJximQlSAzioZCZ6F3UXlYV3gHbDFEBSGRrhOOgxyRTaIWSX_C6m6NFI_zZXHzSDV9vwd6dwSdDxyXkRuB3eOcPEe3kBbfMqear0kJkSq6faE6ZdFsM7aU5qKfjzEF2dSAfyuLR1zXV-cuZFM10UPUGe30_ciT8m0cFrdTt5qjApeprkaohjFvqBc2cBgZHUm7uZ2VpQjr8IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارلینگ هالند از مزرعه یه پیرزن استیک، عسل و شیر تازه خرید و بعد رفت خونه تا خودش دست‌به‌کار بشه و غذاشو درست کنه. فک کنم هالند بعضی وقتا یادش میره که یه فوتبالیسته با میلیون‌ها دلار ثروت.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/101897" target="_blank">📅 17:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101896">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjEw2MLhZUNFs_rz_pUwEMEFGelDmlki7sevCM4fCkkGiiM0lxDVNRiBH6UaDWC20k7AQjNu9kj3NitGwptkB-SyeORhDwn439XojzikDRkpYjVPyfcvVle-XZkJGRf1rY-M2B2lJN_ydQJ5NA9sE6ji0bK6V0gk96HKG-XYKeand31jPn677m_SnW1EXHZJnOThgR8XYzOPqwU6UBdPvhO0vRNQaQDeZczPlK25qzO63Z6NTEgVfV0O_eeGxaP-kwWGDcTQ6K2uaiWvw5DjX8QKKG88VueYz5NPF5Pfd99GBMtJEmfqkt9HUSFow2m15XnQ_fA6VY6RRQYkTBDpzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دیوید اورنشتاین: آرسنال در حال بررسی احتمال جذب وینیسیوس جونیور است!‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/101896" target="_blank">📅 17:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101895">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKmpMSPw-M-ibvikuj9V0-ulWTmvC4b_PdnbkiBRZlKuaZN5LVxtvaiVQ6hm89iocOa67U8ctzZVHwpTJ00eaJDjESSnf-K7lQxYPD3jHZ1VcibErCbKNM0D_5lAEBkUhaR6IxHtLJ-AAAk7OB86mE4XdBFe6Q4EB_z-Lt6PXzCkGGUh7-VY-hWgyD6dHDpaIEfT6wRXAG4EfE4RijSiWj4HAUepouqHzJ27pWcM3RG-e8jDwVshhwOPoDLx0PAg9PlRxWPMd-fouI5Rjyri5u7ooG3hyF-K6pG4J4dswJL7_pGyHFELV7wK8edwOqTX9EE5VY1DTNO7PkqhocU_Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
بن جیکوبز:
نمایندگان وینیسیوس جونیور، این بازیکن را به لیورپول پیشنهاد دادند، اما باشگاه به این پیشنهاد توجهی نکرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/101895" target="_blank">📅 17:08 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101894">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36c582a64e.mp4?token=gClpTm9CQO7ewkTQw4h7eyEg0s3eAxGjz4TRfpaqY1G0oOWMFTR64OmAeSIi8DH57IBSPr4zbGLTA49WP6bV279I3ltNpgRaSYGE12-sBzHCLkv-aeIhzXAi8W_xWpcwmHiX6XV5AXXnAXZAdBI9kI5pd37v1flyegTVEo7ayjghUj_6vqDoGfMWLWEsZchRcdJiokSRpzRtLqB59-N9n_qmc8vWdnzOew_iZ4pu2GuiSKUiWoWUw34SDDCoM-G9EzktWnZ4oJ1i1zX-z_qeO9hr8g9QRFJXnZwdPqqHZj_cWu8Gjo-SqpyKRY_WMXPLZwqm8w8xMCK2va3jUnNKZTmbKqUAG4UljraPgtQZFb4rxCN9kleohIxQfvXLizajL84Qaf7Dnu1SIVag2QEQL6SFA7r4jBJwJCC5PNF-u1zNETBQOkjrucLUovCROVGz8kEin1SdW32zDLP6bGne6QdvC-JBzDxrRU4y8AxyScNzq0Vun66AQlNpoB_4uWnJjAvglBjlgHOcOQclHtT_WysKfufERcckpInpJvdESbxCPdhQDlpy0TDOFNAYkU23EsrwSfKIcLnkmC7y1NivUZMNYXzn3XMxTbbNJNCi7-WM7HFVVNzayCxuJvXhHO265lhBttD35i9a_trGlDRDSC1bvjpXWy8a1va5cFXOLg0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36c582a64e.mp4?token=gClpTm9CQO7ewkTQw4h7eyEg0s3eAxGjz4TRfpaqY1G0oOWMFTR64OmAeSIi8DH57IBSPr4zbGLTA49WP6bV279I3ltNpgRaSYGE12-sBzHCLkv-aeIhzXAi8W_xWpcwmHiX6XV5AXXnAXZAdBI9kI5pd37v1flyegTVEo7ayjghUj_6vqDoGfMWLWEsZchRcdJiokSRpzRtLqB59-N9n_qmc8vWdnzOew_iZ4pu2GuiSKUiWoWUw34SDDCoM-G9EzktWnZ4oJ1i1zX-z_qeO9hr8g9QRFJXnZwdPqqHZj_cWu8Gjo-SqpyKRY_WMXPLZwqm8w8xMCK2va3jUnNKZTmbKqUAG4UljraPgtQZFb4rxCN9kleohIxQfvXLizajL84Qaf7Dnu1SIVag2QEQL6SFA7r4jBJwJCC5PNF-u1zNETBQOkjrucLUovCROVGz8kEin1SdW32zDLP6bGne6QdvC-JBzDxrRU4y8AxyScNzq0Vun66AQlNpoB_4uWnJjAvglBjlgHOcOQclHtT_WysKfufERcckpInpJvdESbxCPdhQDlpy0TDOFNAYkU23EsrwSfKIcLnkmC7y1NivUZMNYXzn3XMxTbbNJNCi7-WM7HFVVNzayCxuJvXhHO265lhBttD35i9a_trGlDRDSC1bvjpXWy8a1va5cFXOLg0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔙
🔵
۱۲ سال پیش در چنین روزی، دیدیه دروگبا برای دومین بار به چلسی بازگشت؛ اسطوره‌ای که نامش برای همیشه با آبی‌های لندن گره خورد.
👑
📊
آمار دروگبا با چلسی:
🏟️
۳۸۱ بازی
⚽
۱۶۴ گل
🎯
حدود ۸۶ پاس گل
🔥
۱۰۴ گل در لیگ برتر انگلیس
🏆
افتخارات با چلسی:
🇬🇧
۴ قهرمانی لیگ برتر انگلیس
🇪🇺
۱ قهرمانی لیگ قهرمانان اروپا (۲۰۱۲)
🇬🇧
۴ جام حذفی انگلیس (FA Cup)
🇬🇧
۳ جام اتحادیه انگلیس
🇬🇧
۲ سوپرجام انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101894" target="_blank">📅 16:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101893">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWVHPmNgLyuB_OEDOV1kZ3h5CDBGXw7ptv9V6zkGhtmqnN9h1yn-w1yyzsmDhWldPiB9w1bJ1FIiENoy-CjyKoLYr11yZioGjYzKvAk3lptQhtiNiXU6kZroPlBo5NuRA9Jt0ZxZqLM-67KafbnQ-FLZCW8bryBKIgWDrr3bxOyuVxunKZ_bhNs9fjFPDhUlNd9R_mUvAhFw-ucE5kkPFrmajz0YsIlT2l-lPmiaKX-OvybAwsv2mN93ahcqRpGVMXNsmazp44xhW-BtDuc4slFNtCJcWtS-wWsEQnIp7raNQhNFE7t89i4o95GyCumUptJgKiIWX1jUm-KZ9YcEYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزش مالی جام های مختلف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101893" target="_blank">📅 16:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101892">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
دیوید اورنشتاین:
آرسنال در حال بررسی احتمال جذب وینیسیوس جونیور است!‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101892" target="_blank">📅 16:19 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101891">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a105d81352.mp4?token=is3blblIlVyXQC6cTUyCb8NotU4QFUgjmVTYuVj9TpCjnGNgkWb-ECGWLeqrXnFxlF8rQEcWd0i-QsWupezRjqtIcZRsppSRYZ8LqZ-0GgAKCFtzLJM3O_C1Aw-wNyfDHjU1LnQb0V-sEIJPQuRJbITzwCGk7igNcA9jmMOCGNudsN3LRLqSn4hxFhuXj7APTa7n39kcM2bCRwwvF3gKa6vF5dkwt5Ls_H86N1j6VeZixVob9h5S7qcpJiKjn6CwMHVsoIfYJxHxJmAFbXr08mBE7vni2lNnRqF5WnputAU9YAORHTc_T1qRj863LB1Lw-IA8v267A85NNyznB0EFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a105d81352.mp4?token=is3blblIlVyXQC6cTUyCb8NotU4QFUgjmVTYuVj9TpCjnGNgkWb-ECGWLeqrXnFxlF8rQEcWd0i-QsWupezRjqtIcZRsppSRYZ8LqZ-0GgAKCFtzLJM3O_C1Aw-wNyfDHjU1LnQb0V-sEIJPQuRJbITzwCGk7igNcA9jmMOCGNudsN3LRLqSn4hxFhuXj7APTa7n39kcM2bCRwwvF3gKa6vF5dkwt5Ls_H86N1j6VeZixVob9h5S7qcpJiKjn6CwMHVsoIfYJxHxJmAFbXr08mBE7vni2lNnRqF5WnputAU9YAORHTc_T1qRj863LB1Lw-IA8v267A85NNyznB0EFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهترین مدافع جوان، دوست‌دخترش خوشگل
پسری خوش‌چهره و بی‌حاشیه، قهرمان جهان
یه مرد دیگه چی از این دنیا میخواد؟
😍
🏆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/101891" target="_blank">📅 15:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101889">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vO3fzH5-vAgVr_CzrYi5iacrKpFwgTh_DlQDwSE1v8HA9lZNLw3yRaIBZ2k75jbDFUiv6oEZUInAyg7hMN9vizSxBUZaPjTayg15kRIxXXnMLsCpualK-y_5rFARAW4MLrIBpcaOWgjslLBGo-tu84_8tnc2C7EmuRzx5uUUL3tHqx6nrAJYPD_TCZVTEAMG33Mn01TPpAxgd_Wv_2SUO8ld1m0OLT6ND9zw3z2xZEVz4mnP-FQSUGTalbHuSnObppnLlfK3UAyGLvuoP_4jNT91zG2O_Qo9o3jZ4vDZ2mdoiecI_TA2aXpn-H8NUuhYqxO5YogZmRp8Nki0XwlNLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LG9S9_hT8YV7ypVVnUXFEy5N3I-P2cQ8WaQw5nkOyUlEg5igtyxxdOH6Pdvb0-ndX9iz-EHz2B_NF7nsk1qN6_f2SZ9o1ECkAw8pU25b8kTJIyNiCqrIRQWDvx0YqjOf5ajHhZsvrAEZeqTFEx4GV_JxKiDzTvCx4ppVHC58qW2HdaDzmATQ5Ki3_eawvdJjVdy0trQIRM3NXmSwRJsf8Rv3GovzbI0i2qOk1LxqGXTY9cxtoI6cwyhINcq4RUTNZ4oNNV9eJpVQ6HZA3tCleaRwq-8SzR9v325NUZFfhJOFa_yHtdv8NwHFJ5v_7WuZyj637QEPwicYMnAYFK429w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚪️
رئال مادرید و ژوزه مورینیو این بازیکنان را به عنوان بازیکنان "غیرقابل فروش" در نظر می‌گیرند:
🔺
کیلیان امباپه
🔺
جود بلینگام
🔺
فدریکو والورده
🔺
آردا گولر
🔺
برناردو سیلوا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101889" target="_blank">📅 15:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101888">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QvRVQYW_27naMyJkmVesB9fwVEdLS3nnVI2o-L7ho9p_hIlV47FBgDAMvjWi5Z3DDAkvZBp04D1uv6t8sRA0x3fYgdPySiP_GmnHRMu8RwJBlM0hNonV21SImoyjVI0jX-KhJ_10Qdo1C5Lh80Zx_yMFS_2YumyPwZmD7H0-uV22yrGg6lNi7EV-0768KERnN1dPWSWA6TAvRsQWj5xfRW9JioCWO0cQcoW4ytQP8ha6f-b--Lp0rHkXNiqkZ5XAACOV0FXMTLVTqsC2W9q61rk3ppIOMkGxPD0KCjQraF5oM77eU4mPa3xNCRm25U1pgUTgKa7V99O6eDuCigxryg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فوری از فلوریان بلاتنبرگ: منچسترسیتی به صورت شفاهی اعلام آمادگی کرده که پیشنهادی به ارزش 100 میلیون یورو برای جذب یان دیومانده ارائه دهد. اما تا کنون هیچ پیشنهادی به صورت رسمی ارائه نشده است. و مذاکرات با لایپزیگ همچنان ادامه دارد. منچسترسیتی به دقت وضعیت را زیر نظر دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101888" target="_blank">📅 15:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101887">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3rFv9ofbd8DuYhLHtWUKFJX2-JYNGYjkbZL_qz4IMiuwv3L7rmJbWyxBt5RfBvm1HhQ22QXxqs4ev--5KWMW_wBpyBS7lcZ2fZpRPYCSKQodT_cmyj3dCejzBUsTiWXV46r4hZfg_f_03LwM_CZwnhAVmfEqIAtqSB_IBjS-9sSJcVQC7GWR8tg2IizACMaytiydw9hAA1Uj3u_3s9xTkr-ypi3YOz4RTetECStCp6Cg9AO2gSjLIOoYa9kipP_Sn-Jogel4N0OZ6nT8mDk1I5zYy9Qso8ITvM-bYvim1ZU63d8qiYpQYwl5yKXJT93IuVW0NSxA06CsNaWNCEbqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
هزینه تیم‌های پرمیرلیگ تا اینجای نقل‌وانتقالات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101887" target="_blank">📅 15:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101886">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCPl3jGxIBPGlEuzAwolIHVQ_ASroLbOoU6_wPpD6oAesGRrWHwQEyND2En25xL9YurlWYQmU-mhF1V99NYkmCUMGQZ1Wrce2QlECetCCPYQvVEWGxz_4NRluNC3O3r8Py8BgSqhD4Vudq1fp12TKePJiGGyW7fFqEewFbWAmgK0DU95tpJto1UwVEesKNaDFxUMlHobi4GM2Pq3EfiIAchHtUziB1wUi0VPlZtVon-HcjaL8dJEdAzeNOK_3CNrhKRjuPJG6AOBVsz63iTP0M_goTIIih5al-HUSCaRZyHnSjSo1atWYaluxJMgzhV7hZDfRWfYRT1ojQcmMliR7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رودرا: اصلا بعید نیست که اندریک این تابستون رئال رو ترک کنه، این احتمال حالا جدیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101886" target="_blank">📅 15:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101885">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLbSbFF3kraRln7A2CN0FEjqwMrRvvz6e7qfSm5U2fHovi7PUazvh5mANinFOed-pnX8Awlqk2K_8xiuVlW4HTusX5U-8g-ghXQNLqxoROaG2Dri2gfvM_lAijiidjwYLQHK7z-j8L0YnHkXks3hr611v2U_jJjeorc0zi3XMKvTNgaE2Qfvf7EcgNnq9vSrB-fe-_jDlglAIOz3UxW2VPCxsFGrMOYMQFq5ElzE6AnYf-ZmAdXgQ-YR49nWkH1zkmagegVcPbtxBoZFWOVhk7IDryuPXjSWN44QCDU6051xJ-8-w_CBkUhfGqhO-BsUotMV0qsd1BIIB9Ho3af5mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
سانتی اونا: رئال مادرید از شایعات مربوط به انتقال مایکل اولیسه در رسانه‌ها استفاده کرد، در حالی که به طور مخفیانه در حال مذاکره برای جذب یان دیومانده بود. حتی آن‌ها به طور پنهانی به مقر باشگاه لایپزیگ سفر کردند تا این انتقال را نهایی کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101885" target="_blank">📅 15:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101884">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f29886b9b.mp4?token=CGdT7lTFUzONa_atDlCIUVTEmWOKZpgKUPEnb0OCWGfkMso7kjeuh4j5AoPQ4spqRC8-tNprp_0I31YiVNFPjfOVYKQPEk0XrkKeFsBO8YnkAJBAkdH_EKeEEY0dfXXEjNpnHB6GBfayiAqdMDBP1u23xFVUvtWb9167c3_VJpb1cbcdrAwF0BPlniFtnlkEM9ZYAafddBkoPQfZNXxCzlAG9bNI44NPGaTOjpRp-Fi9EBs1zww1G2efrmqAuC1J1nBeTFxdJW-_j2N19y8mZ8dYWBCh8NXk6T9GNfLSJEdFf7s3l1JIQ8g-3ClXseuBCahIt9w-xcvDYU0BT24AY27Qdvny0vZscfNR_-neb2g4uFVZtEuJ8_e6PLfBP5-KQC1dzYVZndFa4j7Pith3qaTF7IikKkL4_jFwdcWtaLBFYBe5kn3tmDdf8p_ZUzyiU2eqUx80-hM2MAEL1CMuAkdmd71Hpdcn2HdVt5eeee45Es618J_UAeCsIGvJkmMTecInLyfOL1FpoBYn4ASf4NFhBgQvTBjlziQJlZS7urSkR6BTkJ2KdVpFmB8jL2HqHAZZ69rU6ayuAvXrEeddBeRin4J0b6jp7C6pDnhzZE0RW-f6VNHA0lg10WqLKq8PLU7h69ELuSLbWubWr8qPDg9gRcuf2FThDbO9WJrnM5o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f29886b9b.mp4?token=CGdT7lTFUzONa_atDlCIUVTEmWOKZpgKUPEnb0OCWGfkMso7kjeuh4j5AoPQ4spqRC8-tNprp_0I31YiVNFPjfOVYKQPEk0XrkKeFsBO8YnkAJBAkdH_EKeEEY0dfXXEjNpnHB6GBfayiAqdMDBP1u23xFVUvtWb9167c3_VJpb1cbcdrAwF0BPlniFtnlkEM9ZYAafddBkoPQfZNXxCzlAG9bNI44NPGaTOjpRp-Fi9EBs1zww1G2efrmqAuC1J1nBeTFxdJW-_j2N19y8mZ8dYWBCh8NXk6T9GNfLSJEdFf7s3l1JIQ8g-3ClXseuBCahIt9w-xcvDYU0BT24AY27Qdvny0vZscfNR_-neb2g4uFVZtEuJ8_e6PLfBP5-KQC1dzYVZndFa4j7Pith3qaTF7IikKkL4_jFwdcWtaLBFYBe5kn3tmDdf8p_ZUzyiU2eqUx80-hM2MAEL1CMuAkdmd71Hpdcn2HdVt5eeee45Es618J_UAeCsIGvJkmMTecInLyfOL1FpoBYn4ASf4NFhBgQvTBjlziQJlZS7urSkR6BTkJ2KdVpFmB8jL2HqHAZZ69rU6ayuAvXrEeddBeRin4J0b6jp7C6pDnhzZE0RW-f6VNHA0lg10WqLKq8PLU7h69ELuSLbWubWr8qPDg9gRcuf2FThDbO9WJrnM5o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
امروز تولد هالکه و به همین مناسبت یادی کنیم از یکی از ضربات سنگین و پشم ریزونش.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101884" target="_blank">📅 14:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101882">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crfvgTZD1e7hvSMwMXlijgkH3-5Q7xt-6-ovuUcQ-yewuTTgZ7RyXiV33Br7vPKbt5CSfrm5N09r81dUckd7tDYy6JFPVVxha3uaSslUG-puSTqD6vBBurBFOZp8KqIVUOEbuBiqbb2WPXk30WBgnTWDAYc48HQ47B_rprlVeEfEJvSdrv3zWqzqa34VWByyZnlZjLbukoSYaQbkRedVWd5Qpw_erk-jMDKo-lrZNXpcimfQuLYE2mCjB8HeibkttnWgLqb5SYFuJFBR7UG68YblWI4ek8waFISo4uRklFVSoORL_H55BHm5upzcaTtgidaEvlb2NJV_udpi40pm-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6342fd750.mp4?token=LviHil9KXnsl-bC1K3zqLUE3Fkv4QBAN8rQUla-pXhK6kZ4sMOc4jQof9dfPgoZqvybJWLLVmv3Pw_XrUsgovUqoLVTpKvYiN_L2WvFrsFafZEpuJ_Z2EnIWlMJPkjH114X0O0llx0r12IIWEUqVMXUHZos_T6EDKo7DW0CeIhQPv8-WynUtAn8PJIYObxhxPH-F9hLRR0KvjYPhpLilsd65Bq7EvnfqiHxAXddCqprGgMOr-PAFPMkcvzd24Z95BWWPGfLLil8YdyiRlaP6Pq3XPVCwOWt3sZ2F94UBAVffxTxzx6_Kv5lU65CBVYBQuz1jTUuZQDGFXF_o6PVdPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6342fd750.mp4?token=LviHil9KXnsl-bC1K3zqLUE3Fkv4QBAN8rQUla-pXhK6kZ4sMOc4jQof9dfPgoZqvybJWLLVmv3Pw_XrUsgovUqoLVTpKvYiN_L2WvFrsFafZEpuJ_Z2EnIWlMJPkjH114X0O0llx0r12IIWEUqVMXUHZos_T6EDKo7DW0CeIhQPv8-WynUtAn8PJIYObxhxPH-F9hLRR0KvjYPhpLilsd65Bq7EvnfqiHxAXddCqprGgMOr-PAFPMkcvzd24Z95BWWPGfLLil8YdyiRlaP6Pq3XPVCwOWt3sZ2F94UBAVffxTxzx6_Kv5lU65CBVYBQuz1jTUuZQDGFXF_o6PVdPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
هِیبا ابوک همسر سابق شرف حکیمی:
وقتی سال ۲۰۲۰ با اشرف ازدواج کردم، عاشقش بودم اما او انگار به من شک داشت و فکر میکرد دارم به او خیانت میکنم. وقتی دیدم نمیشه رابطه رو نجات داد درخواست طلاق دادم اما اشرف اصلا ناراحت به نظر نمی‌رسید! بعدا فهمیدم چرا؛ او تمام دارایی‌هاش رو به نام مادرش کرده بود و چیزی به نام خودش نداشت. این یه حرکت حساب شده بود و واقعا شوکه شدم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/101882" target="_blank">📅 14:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101881">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/356f27159c.mp4?token=fUfhQBTmk-qf-l2U90sKj4MT_a7l1k24QRxjSNLi2a5yuyoDFsiFYTLhiHnQxjrMfUToCu28awAJlf_Q7UJfToWYfPUBnm6K5H1B5KLeYGPb78rm5Dg4E4AZ_y80BV96caVJ3Icm0NZDQBlvkExVP1WYGSddSm2Ian6apo0S_sQX5RDuiUrkK0I9Y8gKarADhzsttvIAaqT_f8JUX9JqtlMxhTy4e-fj7WQoIZ-PKDYmjToS4MiAUxG7SszS5inzgwjCmRQ6Ckz2MPkj1E8RQJ68holzNpsnPri7B3RwUOBNt6SqybW-X7qTE0Pc0jYtM0ysIkpVmg59HonLY9GBaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/356f27159c.mp4?token=fUfhQBTmk-qf-l2U90sKj4MT_a7l1k24QRxjSNLi2a5yuyoDFsiFYTLhiHnQxjrMfUToCu28awAJlf_Q7UJfToWYfPUBnm6K5H1B5KLeYGPb78rm5Dg4E4AZ_y80BV96caVJ3Icm0NZDQBlvkExVP1WYGSddSm2Ian6apo0S_sQX5RDuiUrkK0I9Y8gKarADhzsttvIAaqT_f8JUX9JqtlMxhTy4e-fj7WQoIZ-PKDYmjToS4MiAUxG7SszS5inzgwjCmRQ6Ckz2MPkj1E8RQJ68holzNpsnPri7B3RwUOBNt6SqybW-X7qTE0Pc0jYtM0ysIkpVmg59HonLY9GBaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هالند لاشی تو مراسم عروسی دوناروما هم نتونست جلوی خودشو بگیره و مهمان‌ها رو وادار کرد «حرکت پاروی وایکینگی» رو انجام بدن.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/101881" target="_blank">📅 14:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101880">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ry3ku5GZmHbhCEkaS70rmLUJ75g4ySQ2WAuCrZ6Wn1xTKlWDjQ5wsPLZ8_a8mliHWCoFzmovMdpB3_UW_mZOU8UP8G63_fprA-HzuFvALXhnWGZX7bfpeDySFQjgDgceGgsRL0nnwCAqplpPPJpmk0dh_M3zGOkAukG-LmtCYn95A0cLKTYP5pz5IPfcd-KcRJeFjhpUdkYdzR1RTadKLmHllWisZtcMaPvCv4DzwpWY_vIdl752tT4fHzjfznhyPzIPlKTm7MJqJXE0mWpCxASVjuMN5bdp8a1NQgwXaPrBlSMieCjKcE4gyVh6qxTH6asTgmVPb_DqfOcSzzpe9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خط‌حمله نیست که ماشالا فلیک رفته تیم دوومیدانی برا خط‌حمله ش جمع کرده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/101880" target="_blank">📅 14:00 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
