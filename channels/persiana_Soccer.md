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
<img src="https://cdn4.telesco.pe/file/Wa72znTc0EAiX1Q8iXwNxy3w_zHlndu3ObAUQKA4MG-C1kxsL0LOidTFuojE5rkx4eoK5p-4radGtz0bUugbut2t5ZPdac8MCaaEXdcrcscvfq5g6x12FMhYrMwru0mYBSbTqCH0GRK773fCkTAlOCeeZr8eSkgYa7zPUD0JbN8fJu-PJSEemJW0YuI45VJhEI6g8774upu0m_4n_AjoMxwmF2MzDBbnATW-2h0bFMv8gljjuT_G4ndRzirxT23jrijHlsyGsxfhaBpoKRjzKyV5MYg0bHvt6yz3AECC994SLXAam39sHucohv69tNOHkzqSK0Wo5oL2u5ziTEMm7w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 519K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-23 01:01:02</div>
<hr>

<div class="tg-post" id="msg-29710">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdw-XvfHdxHhABv20xr-V3YdgvhrrHwQkhXyNsArGUVGU6Q23Js3dY7GALlzkk4v-JH76CGdqbcE0WDKwk5w0_4koxCmgB2qJEYwUjnBqPWg2Jgy5kSJH_iMSXFMO1f_YNMc1N_ZuTWUGAb-UUANVe6C1LYs5OjJ27akVm7a2c5jgUY1oHdeEYtQZ7lisGt9bGl76rLqu6lvvk9M9AeRaNT4PXiXfR67W82LW5HRL8sU39zXIvuub9QaIs6AtaTgUnsuuX27vPUGtj2_BhD5a2ep1IXp_EVww8U9zFwtE9wPyf9c18q9xILJP2PMWyWNa3MqQN2Fk6su8Fi8GrWwPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/persiana_Soccer/29710" target="_blank">📅 00:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29709">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_mMWe8Br3VA_eU-BkxhyvSqUBm3gPHpw5o9tXxoPhhrNXXy2FiX2yRPIaRKI6GjIXr4MtgIgoDCmMsJvf4bku0k-xYaK_gqtHYIK-xG19TZ1lI3XHtkC8zInDOMaununHNlqu3NB2WcpCXzVCrxlQ4YGsRUOrtV1GuDu6xyzarVKSY4kQ0fndybSnGxockcLvkMl-JN3SD6zj70EuRC563NUFVL2vjId-fS5PZINaOkzt_Rf2noTSZhuUldUlfVtJ9d4libQ4moi0yIuPrJlv5IkrvbPTukELIaOavMdsXsW5wRQBt-peFoE4HLcLlD_ls5VmFhTbuE8wdibS28uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
تفاوت‌تجربه‌بازی‌درپاریسن‌ژرمن و بارسلونا از زبان فران تورس فوق ستاره اسپانیایی جدید PSG!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/29709" target="_blank">📅 00:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29708">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ko0-x5Oc3XZF2f8CxTPocqrZlA6eQQjBJEvm_s3kxvnGuu2gG-63IHWZ_eTuHMFMjlzcMkBtERvRrB2sDDlsBiYdoCPAiUHylGdSwzVxlkNoJvKywWehWFBgBgpQSRCJ9mo6DZ_Ri0QjzfcRmckMDUhEOeWNFhVZRZPPkg0cLRIUyOokB_k3dMdJDygn_7wAkjF1gykKhIKSJT1jQ7znsb67U7wta-NNQ6Cm43nQwLPRiV05LQVC748WI3neXavvTZxM8qLBx35Qu5l8N8VUcGlvy6ReriorLLabUwcj3Z5vj_uidGNmsELLIuCh2ejUs4WKnQkhTh92ECb0mzEKlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌تراکتور از اول‌مهرحق استفاده از علیرضا بیرانوند رو نداره اگه بنا به هر دلیلی بازی بده اون بازی سه بر صفر میشه و نکته بعدی اینکه باتوجه به‌اینکه پنجره نقل‌ و انتقالات لیگ برتر هم بسته شده بیرانوند نمیتونه با فجر و ملوان قرارداد ببنده و باید…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/persiana_Soccer/29708" target="_blank">📅 00:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29707">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWOrnu-p812CL3XkQUGFly589-2L9k7kEELi1DR29QCPFUqFMKT4V6WcqcSD74kgdo9_Kvso2IXQzeoLvgeP-nzik62exiaLcVsUuB3xQZV4XFB5mBHfxQoFPnbRd0p3mIvuaqHte4gPq_onyAStT8v4fewjl3cDAMJ9mVK4P3VzRgk4isCmVl31tnloniV0ke-EoFinTMHe7ROYfoutxaKPWP97NEoJC8p6dU4Xzh9GVP96XpJlPqcbBjhtfLSRrZ3PqpWkwyVqVQzu85FaO1VHwqIKEQFGP55iljF1A3lK0zySeS30OUetrPhN8JfOgFCouRdoCF4kpdnN-1TlWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هفته‌هفتم‌لیگ‌عراق
؛ امشب هم تیم علیمنصوریان دو بر صفر بازی دو واگذارکرد هم تیم دهوک که تحت هدایت یحیی گلمحمدی سه بر دو شکست خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/persiana_Soccer/29707" target="_blank">📅 23:48 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29705">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X3yfAcU5yrSrL88bwASaWQUHUyjUHueWqzYB5yK3ZGII2CV2mMomzEhPBCeTL8x8ZiY17thKXdov9SdncHzRAHCFINU1qJzys2NE4Lso_IQXUWAnkmg4QlPeEe2SUtm-Yl9DXxxy6zh7G_DU5ukiRkflBIEsnWa-TgiNgGS_oaJoTVa7hqsesAe_d8eao_wEYursQMlqn0NeVVghWqqcfr8U30beW3zH2t7J7NfU5FMpr-cxQF5-p9wBxNE_JbUZX8nLekj2mI1YRAh6bb3bsEzNg3dHKwjzb9QHlqIoTTRo3L302lk7kYOgDPYC5QyV6FwEq74s2BvSuMY1XfmNdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f0jojF_Ta-HZcbeK-fBI31jQAU5TqvZnYvICT0StYf0Cbr7YRH31pm6gyFDyDh-2al6T5BCzXPTYRCb-bE71CN5-4jF4oSyaZbS2birWvHMpmzy1-g3kS2zDeiYkyYBR8ODLK3UKzA42y16mMBqGP0o2Gt6J0ue1TC8r6kgyvXZBxe0zMZZF3Q70X_bYOSskIyW6A4MnAicx-pNcZ_BzmP2gQuV0MBWtZhGTGWhbpbxVQ3jQInTuNaomGY7vi_bcX8vQ1f9JktG2QW2-Wu7dW3vvGL5N4nGFj36FRg0uwNd7KB7gqAshtATk8kIWdCyYMK0thzS43M4GzAKqdXRWsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇦
خبرنگار معروف و محبوب شاختار دونتسک در کنار خانواده اش؛ جالبه شوهرش بازیکن تیم شاختاره اما اندازه خانومش محبوب نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/persiana_Soccer/29705" target="_blank">📅 23:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29704">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jh3i1yDhRuY_pPF_JuHv4pQ4b52DHjbGrJrOd0uPe4kWGY8Z29oJ8YMH1PrpfaHprWY_IgQ5d7_F4HPl_aS5pOEKN5prxEUkdh23AiFGqLrGjS5Dz-4w9GRGICIkWTTCdGrE_JSUiAgQCqgxyX3_vxTJSN4ciJYh6v4uVgmzbtKlm9WpUJyHHBGGAc_kGQkvYU0HzjzHlWVLl_uyA6jd3uDL7e6z3uWFMwcpgtYuW5paN8gYRA1FskYKXmKu00oL4kSI5uw3O9sCIqinAcEBfqiaXq5rNVONvnqj_i34TsiW0OyWwKhFjxyFpRN76fkLrI7U17KGAjFjzH-nVQKFcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
درهفته‌ چهارم لیگ جزیزه؛ آرسنال میکل آرتتا با دوگل دیدنی گیمارش و ساکاساندرلند رو شکست داد و باچهارپیروزی‌پیاپی صدرنشینی‌اش رو تثبیت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/29704" target="_blank">📅 23:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29703">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_jUgMhGMZyAS_RDuwvhlLPFyMjzn6auadaGCafLCXF_EkxJ0yNjNeYgCozcfuWt6ejzLM5dW0OIRMn2Jp6zcIcOKWW3-Oy7dOlSS77d-VwyDVQw31bd6Ou4nLe4_G7FQ77rjGxIE-WhL1Yzak9lDMdbRvxmajdoq7Ze42tC07RJwx9ubsq7WhC_m7qgS09BICpT9VDF53h3JkUV2pn57I99_FLcvtmG7mm8On_UjNYY0yvpvLaYfBprFDiEZeoFoAJjet5HiA3-g8FxvMyyO2j6bSrmc8jO7ehvQaigU_kLQNopcSLi0WGl2_QCDoQl2OgTpjk1Ss4vR3FCjPnj0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌پرشیانا؛ مهدی تارتار سرمربی پرسپولیس‌امروز درحاشیه‌دیدار دوستانه سرخپوشان جلسه‌ای‌کوتاه‌بااوستون اورونوف برگزار کرده و به او گفته که درادامه فصل‌بیشتر از قبل به‌او بازی خواهد داد و مشکلی با ماندن او در تیم پرسپولیس ندارد.
🔴
گفتنی‌ است‌ که علاقه…</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/persiana_Soccer/29703" target="_blank">📅 23:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29702">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/780ec53923.mp4?token=DaIjm1l_KMrBUB_6_EVVDj7gkiELlPslaLfxG8VJGKl1sUvLkRDXh2qFV2hAFEsPdFynEsEt7TKgoQLjagF-7vopu0RSQUIFXpyA49E2Dgn6_8ZVcp4SfMtjCB8HQ5mbK7ZLSgw3Bi06aiu20auuPCVPQpYfk7P2UXz2PiTQxDZaoiR06za1JLg2YUk_RKvKXWFgwhNwvp-k7DXPQ-TBCJep43j3RsrElT4UeEDjBfjRd0hE8uNtM0HxEJHOwlohDmW9lS-PRIzb8EhUzbT7kqffEWLDXrz4HwD1A2qoSFqd_rMa0JwQtmCqgPPcqt74grI4oe4pn_x33IqhrxSgfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/780ec53923.mp4?token=DaIjm1l_KMrBUB_6_EVVDj7gkiELlPslaLfxG8VJGKl1sUvLkRDXh2qFV2hAFEsPdFynEsEt7TKgoQLjagF-7vopu0RSQUIFXpyA49E2Dgn6_8ZVcp4SfMtjCB8HQ5mbK7ZLSgw3Bi06aiu20auuPCVPQpYfk7P2UXz2PiTQxDZaoiR06za1JLg2YUk_RKvKXWFgwhNwvp-k7DXPQ-TBCJep43j3RsrElT4UeEDjBfjRd0hE8uNtM0HxEJHOwlohDmW9lS-PRIzb8EhUzbT7kqffEWLDXrz4HwD1A2qoSFqd_rMa0JwQtmCqgPPcqt74grI4oe4pn_x33IqhrxSgfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیر امریک اوبامیانگ ستاره37ساله‌سابق تیم‌های آرسنال، دورتموند و بارسا با عقد قرار دادی یک ساله به‌ل اکرونیا تیم تازه برگشته به لالیگا پیوست. جالبه بدونید دستمزد یک فصل اوبا تنها 600 هزار دلاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/29702" target="_blank">📅 22:43 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29701">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cqlx8WEzMrxAl3cwk5pzxsDI9J88JaznMhnr5YqcQsfmVc4OvYjehRouqxe5V5tKIPqTW5_Ek1fjKxw36oOVxZw4iVUgffANYNGj60rVH58AlUIYnShyH0KT4J-sZaWl_HumuzU_qa0ZgHK7rZJ-ud_OYSYto5U5tCcy3K4mD-d6hSQrWBBVB0sN1nLTAv_vpVzgWL7V9gMXqHlW_GcavwjiHj_TwGPFF8dK-JKyc099p4G-HboVIkIN8W7PJOuonC4wu8rPw514QQsAAYlzoD-lT7OfP9rEabflAgwuSXBya5wUiZ7raz8jvoUz8HAef_WJFIBjIXO-ODgw6XGTqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
امروز عکاس‌ها دوتا شات جنجالی از لئونور ملکه آینده کشور اسپانیا درکنار شش پسر منتشر کردند که جنجال‌زیادی دررسانه‌های اسپانیایی به‌پا کرده است. عکسا یخورده مثبت 18 بودن تو کانال دو گذاشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/29701" target="_blank">📅 22:18 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29700">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0eb0365ee.mp4?token=E89YPrksJ-aw1UIEmK_lGQ0SUO0Ltpc6mQp2wyhWMn1JDra46-Pl2lXBTZ9Q-tg9IS4qudfBANzEbzZFLPhKjFh7MP4IVLXNJA4Ahv6YH3Os9bvCJ_wGOtF_Ke_80Q8xrphXusiQbsUBm7mX1PRe79GqecRYPJuDzPMhAFx7mIbg0oi9XQiGTpMF7LOiwdJS2vpXYh3ji1DWoao5_oRqbTWuxnUOnRCYAqkFMHohMDLNU5efjNONc3kB1SkFlpN8HWOwya3Rqg8L8qGwgopGUIprdUC-Tjx6gDMgA_S0iqBzcgVxXpqwz5aAT8OYhFR23b-FV-GLkzDS0JApw8B3MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0eb0365ee.mp4?token=E89YPrksJ-aw1UIEmK_lGQ0SUO0Ltpc6mQp2wyhWMn1JDra46-Pl2lXBTZ9Q-tg9IS4qudfBANzEbzZFLPhKjFh7MP4IVLXNJA4Ahv6YH3Os9bvCJ_wGOtF_Ke_80Q8xrphXusiQbsUBm7mX1PRe79GqecRYPJuDzPMhAFx7mIbg0oi9XQiGTpMF7LOiwdJS2vpXYh3ji1DWoao5_oRqbTWuxnUOnRCYAqkFMHohMDLNU5efjNONc3kB1SkFlpN8HWOwya3Rqg8L8qGwgopGUIprdUC-Tjx6gDMgA_S0iqBzcgVxXpqwz5aAT8OYhFR23b-FV-GLkzDS0JApw8B3MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
درهفته‌چهارم‌لیگ‌جزیره؛ منچستریونایتدِ مایکل کرک دراولترافورد مقابل‌منچسترسیتی ده‌نفره یک‌ بر صفر بازی رو واگذارکرد؛ تک‌ گل این دیدار رو ارلینگ هالند برای سیتیزن‌ ها به ثمر رساند. سوپر سیو پشم ریزون دوناروما در دقیقه 90+6 مسابقه رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/29700" target="_blank">📅 21:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29699">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKAFajkbwLw15KmioZJMysYoPIcMgTODvQSWaTdJ1z_2N9s3TwR6lXZhEBo-XnSbV0HcyvUdjjGZQMaeg0UTn2K_gWjwtMH71iv0gaxjlCFh15da0rUIUh1Lyyf7ZzJJi9q-cSj5BpluAAkeNftWRMslWi7nnUACmGPAbzyjGMgOBSYvergVB964wAmUawKhCGUdyARySJHgIFP6PrdyF7FFojkjImlxOGs4K7xj6RdQ8LFUfNwt081l_sn3omJYyXIimWpZQDk8VEXROBCVDHukLWTXl8cMya-0oWq9PJr_W-fGP3n9KmM9WEVc1kJ2GdrUYhcTF2ZaAqjtkPHL5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
به‌مناسبت بازی فردا استقلال مقابل السد؛ نگاهی به تقابل‌های آبی‌های پایتخت مقابل نمایندگان قطر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/29699" target="_blank">📅 21:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29698">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4GkSKrjJp9_V13opeTTJPV5viJDQFcn8KtxbNQ6mvrayt6EEhxy3aTWt59DydbTTbaOCsHGXHW3axoYVuXfapsLM1j-vH7L_rXDN2S0r0IOWcHQbIjDq723lpxBaW2K8_iU5FUSDwWkr88KeQltyiGjOFqPmwqA4OwLofJCsAqu5ohryT1lAawlsQRHcBlRpnhfelEEWowKg8OmVF1QdQ9CQn8MGukzB4K7aNLsNQV6kJPs9xySBOEWno3hg_v97CkDApS_JlTKjT4Q0NEBL9_Q99QSC0m7-ZMciHQoFvwTQI4oi80Hv0vB5EtzkTgzYD0PJ6tcrzmyYwdnOr9F4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بایرن‌مونیخ‌امشب درهفته‌سوم بوندسلیگا با گلزنی هری‌کین فوق‌ستاره انگلیسی‌خود دو بر یک از سد الفرسبرگ گذشت. حالانکته‌جذاب‌این که در 100 پیروزی اخیر باواریایی‌ها در تمام مسابقات هری کین تو 97 مسابقه تاثیر گذاری مستقیم" گل یا پاس گل" داشته. امسال خیلی به توپ طلا نزدیک شده.
📊
عملکرد پشم ریزون هری کین در بایرن مونیخ:
98 مسابقه، 100 گل‌زده، 22 پاس گل، نمره 9.5.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/29698" target="_blank">📅 21:28 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29696">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrvYLYGZicYmBODzD-XRCvPZb_Ek2vO5Nns_nJv8K0l2B_DPL9kCo43h-gumixdPnaH3COgRtsNvgbZP1_CXt4vESeZchidRlYn6yNzhaKhlD_5Z3tTd9SXh284GS0dnF0Myf3ysYx4SpqTPvWg4PPAI1f55bwxRxlsnzSanDg5H23p20MbtwN9q3XSkjbnCf3XxJq3J-SicAc_81Q04AcDY3cIoMJ-GyWJ3eMC7ZhUg_XAPqe_FOzInW8MRAlOIiTs0s2vU37pT-2zg5aDh-dOk0if_S0iWFPgGo3PWTw8kt9GVsya4LCngv5S3CZZV6d5g7BewDive0FKIL76P2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
درهفته‌چهارم‌لیگ‌جزیره؛ منچستریونایتدِ مایکل کرک دراولترافورد مقابل‌منچسترسیتی ده‌نفره یک‌ بر صفر بازی رو واگذارکرد؛ تک‌ گل این دیدار رو ارلینگ هالند برای سیتیزن‌ ها به ثمر رساند. سوپر سیو پشم ریزون دوناروما در دقیقه 90+6 مسابقه رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/29696" target="_blank">📅 21:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29695">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2f40791fb.mp4?token=OipcAdeYpyie4UeH7Lo3oXYrmc_czspluF4GMyFdy_gshGS0bp9YcuYeJOkdp5swdi7XSFu2e_rsjb9leEzYS2bKDHmrw5oMM1wmk6mS8HTF6RdRbJpjlJ-yxah4xTQHifJssNWO0pxLqnJagADW6W3QVn2HnYekxsdf9faJphjRd7U6FA1-VgAEETa6WhIX9FdMwKgWkmmHqr5n8Mof4dABQlA9Xop27hIprkreYVpDgIXtGK-L2_OCTaT_THDzZcFqWmD7rcLfW0dMzHh0p4iTKFS2aTHGFCGqHjC7fTdTY4kRIlmLRLe6CZXdw3XFD1WVDOMj6STZzZCqmK8dox67q473OKQ-hxTfxB63hA7FL85MoYd8b7X67ZbIFQVqu8RQ1hvV5d3fdN-PXZskmSzaRkOWB2EmcFR0eKSoTlkqYhIoB0_L44IdcH2vDTaAwb6VGFHD90vZzQ7HtbuA-InueGyH7ZF5I5mT5wKzfmxtLuWHEU9MfU9xneQnQcmBNe4pZBcWB8noXw1ZP8Jj4tcUAIsttksphk-DB7UAgmWxGfLz7WVCshgCqzucHrVo16yKaScgjby9G-d7w6Rnixt6IdNq5xplHuFlHMarS2plrhxXdVsLdoBpNRhJt8ooH-832JuOo01gKJHPvCjHaC58U0PcL1NrU29n9DBRDdE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2f40791fb.mp4?token=OipcAdeYpyie4UeH7Lo3oXYrmc_czspluF4GMyFdy_gshGS0bp9YcuYeJOkdp5swdi7XSFu2e_rsjb9leEzYS2bKDHmrw5oMM1wmk6mS8HTF6RdRbJpjlJ-yxah4xTQHifJssNWO0pxLqnJagADW6W3QVn2HnYekxsdf9faJphjRd7U6FA1-VgAEETa6WhIX9FdMwKgWkmmHqr5n8Mof4dABQlA9Xop27hIprkreYVpDgIXtGK-L2_OCTaT_THDzZcFqWmD7rcLfW0dMzHh0p4iTKFS2aTHGFCGqHjC7fTdTY4kRIlmLRLe6CZXdw3XFD1WVDOMj6STZzZCqmK8dox67q473OKQ-hxTfxB63hA7FL85MoYd8b7X67ZbIFQVqu8RQ1hvV5d3fdN-PXZskmSzaRkOWB2EmcFR0eKSoTlkqYhIoB0_L44IdcH2vDTaAwb6VGFHD90vZzQ7HtbuA-InueGyH7ZF5I5mT5wKzfmxtLuWHEU9MfU9xneQnQcmBNe4pZBcWB8noXw1ZP8Jj4tcUAIsttksphk-DB7UAgmWxGfLz7WVCshgCqzucHrVo16yKaScgjby9G-d7w6Rnixt6IdNq5xplHuFlHMarS2plrhxXdVsLdoBpNRhJt8ooH-832JuOo01gKJHPvCjHaC58U0PcL1NrU29n9DBRDdE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
هفته چهارم لیگ جزیزه؛ شماتیک ترکیب دو تیم منچستریونایتد
🆚
منچسترسیتی؛ 19:00.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/29695" target="_blank">📅 20:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29694">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UkVJ--5FbPp8gqvG0lYuT9eKk7eawAgehHQJQKfQKQVktlnkBa_rAqZsaQ6fOQ2tdC45aaS_PpGpKGQ1hkEujOjL_YVPLMg0P80dUOPLKQLLc3sZv4i56chK84GLPOs6j1BD4IOeeEgpxaW-Jbfrqg-FGJR0bfzLSbRzN2KRt0dq6k7N7JQFzGulEEV_856M-l7fvTJdbbY4REJ67dcIhZJDhecWcq0pwgvsHpG3Pk-SyNFHkaJ4SKulsGjtOOozwMTSIivguj4VnTmpadN6tRgLOZZOHqTDYcs-RgS5jz39dg-nkWUNJsWau3gfPL40GvEZM3aYXrnVJB0PqqT4Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خب گویا صداوسیما بهش برخورده که مسعود پزشکیان گفته بود تلویزیون دیگه ارزش نگاه کردن نداره و قراره‌که‌از فرداشب‌مجموعه جدید و جذاب امپراطور دریا هرشب‌ساعت 19:00 از شبکه تماشا پخش کنه. بعدش هم قراره جومونگ پخش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/29694" target="_blank">📅 20:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29693">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HugoVNK-GMNk2wFnmSmXinAcQY6MeECPEjK8IgsMjVzxXkr4sCml0HCzD46lLJLGNMtkffmZfsxtGpJD-FjSV9g3r0zlBBAo5EB6mTHJqmHzo5M4zXNkQzYSMnnKu8_oVfO89NSZ_3by-4LdoNZy21ow7yeVSFS6VTG6ieD8gME4J6UjUuvycWfWXrhCkjKN5e4nhyJj7XJVOTNp4vViTp1musQ3gqAMcfSZFfWtEelQpV-iLyiI5iSkst0sIl5WRdYEtG8O2yII6MXwLYggQYzS42Owy0yldbhpnH7SmV55enqlgvH46GtGkzFINRTz7nFe_oJdK3z9HakfcDNRXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه رسمی و عجیب اتحادیه موبایل ایران: مردم به‌هیچ‌عنوان‌برای‌خریدموبایل عجله نکنن چون قراره خیلی قیمت موبایل بیاد پایین. صبوری کنید!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/29693" target="_blank">📅 20:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29692">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59ad168b5f.mp4?token=GxQTBfmUXOmkSzB85mpWDKb9gmFTlt4f2-tdk4VL36L0dBMS-oRjd-YW_xnkU9sF4f3cZC3MKzsnlYw6CkRIGKdXc23x5Wx_c8qXSxk1ewQkaR8PP3D9ytQYKpgIUV0usp4hBhUNQVq7OIoXg6SVXRmuxAJH-zyzZ_lbITjesC8JryWU1B-HkCqbWkv5LDiNwd5Gkx0zVJ9jFU3QX57sU5LNVLKX5x-XSYZ85l2dGADmss1Z_-FbUpyBVHlIHwhdeS3KhsYJsNhdTG6jieeyZxc4t8N4AM0jv6-PFTWbSzy6SEFey9pD-5wXI60uMAZqX7YcgpA6U2rQDJ2h6OvTfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59ad168b5f.mp4?token=GxQTBfmUXOmkSzB85mpWDKb9gmFTlt4f2-tdk4VL36L0dBMS-oRjd-YW_xnkU9sF4f3cZC3MKzsnlYw6CkRIGKdXc23x5Wx_c8qXSxk1ewQkaR8PP3D9ytQYKpgIUV0usp4hBhUNQVq7OIoXg6SVXRmuxAJH-zyzZ_lbITjesC8JryWU1B-HkCqbWkv5LDiNwd5Gkx0zVJ9jFU3QX57sU5LNVLKX5x-XSYZ85l2dGADmss1Z_-FbUpyBVHlIHwhdeS3KhsYJsNhdTG6jieeyZxc4t8N4AM0jv6-PFTWbSzy6SEFey9pD-5wXI60uMAZqX7YcgpA6U2rQDJ2h6OvTfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
دیدار گرم امروز زین الدین زیدان و سرخیو راموس دو اسطوره تاریخی باشگاه رئال مادرید بعد از سال‌ها در حاشیه مسابقات جذاب فرمول یک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/29692" target="_blank">📅 20:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29691">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OA1yYCurRrAcRdaK855BBk3ukgone0HCbrJ54xG9mAU9f93ruYKqfU3PjMnoWWQ3-pz1xHyll5QmZwG7p_pRZ4QLSnvx0qoqc4fQEvc2-dcKkRX7xEGoq5bi8MxY-D4jHaS62O_Wwk8MMTmS7bzvxh0alaWWDGxF3RC4OUmgMkTZN0rdF8KXcB8o1BKZKFTLde4Zj-VjUxZmoC-6ttL3s7h-5_gaQg4JLOCM4T1sXYeFTDi_aAYALjUWDKYytX9VEq6gh9tr7Oagj8c8NpLQM4lOGbcrIt6Hn05q94h0lgtsIGV12ooqXqJc2yFSm6sfWaQmU9MaIG2VM4FC2LMhMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🔔
اگه تو این اوضاع اقتصادی بد دنبال یه راه مطمعن واسه کسب درامد میگردی زود جوین شو
💵
💵
💵
🤩
تحلیل آمار و شرایط بازی
🤩
بررسی آپشن‌های مهم
🤩
چالشهای متنوع همراه با جوایز نقدی
💎
کانال دارکبت محیطی امن برای کسانی که به فوتبال با چشم تماشاگر نگاه نمیکنند بلکه دنبال یه درآمد مطمئن از این راه هستند
🔥
💵
g22
🌐
https://t.me/+KoqkzqAz7CszZjlk
🌐
https://t.me/+KoqkzqAz7CszZjlk
🌐
https://t.me/+KoqkzqAz7CszZjlk</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/29691" target="_blank">📅 20:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29690">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QwmTWrFhk2xqem0xwMasBHQueI7RMsK73fI35AVz2h57AYELVGHNWxT3XmsixNVgaC2-aBf6KWGBYdw1WpkA_pRTpvzOTY_R6EccZ_RqP-2xaS51y1xGYK8Fk9bmswdPGiTkwT32xEKe7HynxZEfKoiBjNk3hnNeCkxdlk1tdX1hccr0zth4dGmHZ049OsVLLecvapUVHEkw9OoEUmX4XmRGcqbp6sEMkKI8oK5JB9DIA1VJfmANhcCb91-V1mrP3qk3j4LA4yFsF7Yics51jT93icAHiCrN_AoCc7mZINhqvz8QfxbX3IBTeBXm6c_GQ68HdM1VAO7Squ_XIfhUAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
🇪🇸
نشریه ال‌ناسیونال:
فابیان رویز ستاره اسپانیایی30ساله پاریسن‌ژرمن درخط هافبک تبدیل به اصلی ترین و مهم ترین هدف سران تیم بارسلونا در پنجره بعدی‌شده. رویز از یونایتد و چلسی‌نیز افر دریافت‌کرده اماباتوجه به‌رفاقت‌نزدیکی‌که با پدری و رودری داره به احتمال زیاد بارسا رو انتخاب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/29690" target="_blank">📅 20:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29689">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQjt6KEobYuw6lQQ17Y3eP9WIhcfXknBjQ-y5VxCJes5cvmv1Wz3CYKDRT_vEHPFLUKEmxArmUvQLbrbOu0tvu7WAv-lwllnBe8EPfziel9D4UmfvHNDb_zdF_YY-EHV8otnu7nEgK9W1l8YOcqc5m0FKMO0r1nZsAng5gbzunE1IGTEbcjC_jZcQFSH2iqClnoNJoVhEoZKaBH4JTYcYSYmiOgE4rqJRZGhGOyQPxjTHaCMx5fVfgTpvK13H1tZWAKyw4bajwMmfQWRdiM8DMdJEOp5nYCvl2cUy9hjVINdpdn63a1iOMxDomKm70_JH5y6TD8MQfjwkQO38WMNnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
در هفته پنجم لالیگا؛ شاگردان فلیک در دیداری خارج از خانه به‌پیروزی‌مهم‌چهار بر دو مقابل لوانته رسید و باپنج‌پیروزی پیاپی در صدر جدول ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/29689" target="_blank">📅 19:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29688">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CB0sMx9Svj14pS459iZOLnTiKk2wbuQAzF0B1vLgVYQtRfdDs1nGLNzQl8rEygP_SnwVJK1mjDklKqtnvlVqcRAA8-Tgrzpi8zkza-dFsEfBHrFDrfmj1G1GReKWKhuNZdIb7qmzK27NmHaskkef64ZyTA-dNrYJFWexhTRWNtGbwYMmm9SyUJLe-pmN6pYmI_dzkroa0XPJdBqtbCa_2P9jOaqCnRF4J8fPqKwp6N8qsCe_STwTIBFz97V0RzQMULpO2hdAFyevUOOW79U4xsdQcPxaB5_AlvWIOpGptYmrwAEGg4K1WSfAnftgogsxZwzmBP6B2O1DzRVeTWD5Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لالیگا|شماتیک ترکیب بارسلونا برای دیدار مقابل لوانته؛ ساعت 17:45 از شبکه پرشیانا.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/29688" target="_blank">📅 19:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29687">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wB2CZ72VmkV4o3KqI1KlNNPxlP4wbbHhwxRtiFhAa1ntbw9hfE-hwuUIZcQeKVChCEBrrMHmZIWV0RfaowrenHUR0ubUBE0D74YHs2NbeZCmx0APdbdVLFkiKaZdCRgx9NPjKi6hYjecyl1fRh0J7AJ9QsnhED5tRKkDFJHGA2l2tx2PNbmOOMMIEJOwFdhRdSPwLDhvA6AZFOugSn3nNcPV74TUnh9dvJ5yi9DdgQsP1wmQJCynA1yaBzSQrvgbm8UZ3cVW6FcrYoRC6QTHMO1UuXt8SlhE3JU7PFLONmi54OCGNcmNe1We_eMYU907iAOku4xksgE50MJPI288Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعدِ لغو بازی‌ با خیبر در هفته‌‌هفتم؛ شاگردان تارتار درپرسپولیس امروز عصر در دیداری دوستانه با نتیجه چهار بر صفر شهید قندی یزد رو شکست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/29687" target="_blank">📅 19:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29686">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4a-hSRkT5236Cfk7MpvK38KESMfMHRn76DyIIVxWgSAltHwkM3JEPg4wZKdJC_6SIXkFF4JrZXZnnOAddWXhIaDS2BPZvu8oAghwdeqVG3nP2jHUIrguNqR9Ggl-umavrxBmve0XVGWeA4aqJMPEbi-PQFkYgCzDJ0iNQXN873eTVsNUGVG-93et1m3cnClKK90wPGlKZ8hJP4-yfsOfPSRx4aKHqh0Mi7dsEEsQM1e6wQqFD_ETBUVtBEHs-AlKSfIDtN43nI3MsYFCSbWSNZOU5x3NAPApDT8JHcWDJnKl1Q9OKjs9qL5kMdx9r4hadisA4DLtOmZbOsFmqrs8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رونمایی از کیت استقلال برای رقابت‌های آسیایی و دیدار فرداشب‌برابر السد در هفته اول لیگ نخبگان؛ این‌مسابقه راس ساعت 21:45 برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/29686" target="_blank">📅 19:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29685">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUSdllg7et3FOMNT1j3bEAjqKX3lsUptkGGoe8yrgQYtm2gt-i7RVsebRyHtAEvg_vgIHZqOuitklO4Jt_urXfA8lkMcYc2fWJAmK4AYuJpWjZH3UKGk6netmx7W6jza8LHzsmQVqav4sFt2ytXZKO2WQvFy_odSgAs0FOWZ8gpU3vV5JavSVm3y1PIzuZz7z-RlGqzZMjNNRYEIDq0GV9tB6iXrUklAD5pgECdsX-Rdax3IhD75NOWEkqc3EUsS__8zCiL2Kq9V9Z7iDiVOreBwAaUJY42d_sAu_esiqXrXYT_fu7kUsW850r_dj-1MvImI3d1Zc9SxFUoee4zKxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ اوستون اورونوف در جدید ترین پیغام خود به مدیریت باشگاه‌پرسپولیس گفته اگه کادرفنی به سبک بازی او اعتقاد داشته‌باشد حاضره به‌زودی با حضور درساختمان‌باشگاه قراردادش‌رو تاسال 2030 با سرخ‌ها تمدید کنه اما اگه تارتار علاقه‌ای به ماندن اورونوف نداشته باشند…</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/29685" target="_blank">📅 19:06 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29684">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f29263824.mp4?token=ZODIJNPF1IZ_Am6rhMIzQ9Za41fJIFX8X_2rHcReO6L6ytuekdPmQOhN_L5M1KFC3vyuzxeyfhHBPu97FyZZ-oapEDrZpe_pL2C787P3q3M_p2gn9gtDK_b6c6vPxVE0pJiBLf2WyUCrUfVrJr41krF_Y1sGkcTuZv70oE8ocg3m-a4KgCzpkBQrwXpbP2VUy_ewkFaA36QJwWwqV8RWgi0KvFmKDapDFF-bu7X0fUdcVNf6mN27C0-u1SaIdGoGZWETBK1e0QcPci1un4G6wUVirKOjv2ywb7GZ_ybxRTuTLEy_z8KFg6RRkxpuzNZZA3TRzlSSMUR5ZoXdUT7m2i89N1KaJzXE7SuR9WDd4_UG9QQGUeYfSWTeLUXiwXwI48vhU_XmCi30PMdhlkexlK6J5hzA7owTLz7wHhacF7I7vlNr0vvT9OKU84OdBpS_QeWz6T2kODlVitueT96LkDuWztQpqZe0qFjFR1Rpa9NsNGaVA8pXOBqMXHC1yNPsyO29bC_6_27eFIghxGgpk4AEhT86tmq86rw1_eqKhgMZBoAzjvYl-FN1nMLvuDXYCZxx1nmlfWVqGY0W9s_awPtFKJwyzDtqHwXNgzyQFBMzVejR3OVksGHFHi5my_ti6oS_7m3H6XzsOh6jdKp60pRUfftN0P51WBhlticvZks" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f29263824.mp4?token=ZODIJNPF1IZ_Am6rhMIzQ9Za41fJIFX8X_2rHcReO6L6ytuekdPmQOhN_L5M1KFC3vyuzxeyfhHBPu97FyZZ-oapEDrZpe_pL2C787P3q3M_p2gn9gtDK_b6c6vPxVE0pJiBLf2WyUCrUfVrJr41krF_Y1sGkcTuZv70oE8ocg3m-a4KgCzpkBQrwXpbP2VUy_ewkFaA36QJwWwqV8RWgi0KvFmKDapDFF-bu7X0fUdcVNf6mN27C0-u1SaIdGoGZWETBK1e0QcPci1un4G6wUVirKOjv2ywb7GZ_ybxRTuTLEy_z8KFg6RRkxpuzNZZA3TRzlSSMUR5ZoXdUT7m2i89N1KaJzXE7SuR9WDd4_UG9QQGUeYfSWTeLUXiwXwI48vhU_XmCi30PMdhlkexlK6J5hzA7owTLz7wHhacF7I7vlNr0vvT9OKU84OdBpS_QeWz6T2kODlVitueT96LkDuWztQpqZe0qFjFR1Rpa9NsNGaVA8pXOBqMXHC1yNPsyO29bC_6_27eFIghxGgpk4AEhT86tmq86rw1_eqKhgMZBoAzjvYl-FN1nMLvuDXYCZxx1nmlfWVqGY0W9s_awPtFKJwyzDtqHwXNgzyQFBMzVejR3OVksGHFHi5my_ti6oS_7m3H6XzsOh6jdKp60pRUfftN0P51WBhlticvZks" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
ویدیو آنالیز دقیق عملکرد شاگردان سهراب بختیاری زاده دربازی هفته اخیر آبی‌ها مقابل پیکان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/29684" target="_blank">📅 18:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29683">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/961ce8dd07.mp4?token=vBo-D4Xj0G9XSqVWo1Karh6U8B-IY_e9EZq_LRNsJ-oX9YB92lheS8WBSUST3CJpFMGjVL9Vhxjy0RyWLcTM_xFGpcx8xWrBfwfl3HlKtDDluEQRFiCnZzSXrSQ6LrCOjhyyDDFCM193zdwBVA2fqLoaJN1FxE_ymPlhmJIcq5Zp_8bKQ-lNLjT3DagueQuaunMXunMk7QR_h97GOOXLMNNuU-K6jy0Y5-ZsoIiBC68wiAeG5katpHvI59JxiKUiF7mGdPeSsoAzk9v02lQpQxSNiBdLI5HsLJ02_9XZrUQ5VXwkk4tCNbor-lsdK3hj06hT4MD3ilVpbGSWroX17Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/961ce8dd07.mp4?token=vBo-D4Xj0G9XSqVWo1Karh6U8B-IY_e9EZq_LRNsJ-oX9YB92lheS8WBSUST3CJpFMGjVL9Vhxjy0RyWLcTM_xFGpcx8xWrBfwfl3HlKtDDluEQRFiCnZzSXrSQ6LrCOjhyyDDFCM193zdwBVA2fqLoaJN1FxE_ymPlhmJIcq5Zp_8bKQ-lNLjT3DagueQuaunMXunMk7QR_h97GOOXLMNNuU-K6jy0Y5-ZsoIiBC68wiAeG5katpHvI59JxiKUiF7mGdPeSsoAzk9v02lQpQxSNiBdLI5HsLJ02_9XZrUQ5VXwkk4tCNbor-lsdK3hj06hT4MD3ilVpbGSWroX17Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
هفته چهارم لیگ جزیزه؛ شماتیک ترکیب دو تیم منچستریونایتد
🆚
منچسترسیتی؛ 19:00.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/29683" target="_blank">📅 18:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29682">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dtnfJlKORJslbYurrVMMT2sZsk0Wy8097D1C1X7lYtSmfvUzyJ-KY8Xth1SbgsxRyQfd1SqCgaQ7il-x5YlqOUrQdblZE1qxGgNkzwNCpJnOMrNNGEI7BUL1pJcXLAqE63xiTHmithknN4Ap1btxknDG2N8lgFPXm6oZLxx2CCxadcPoFtYX5qjnLjk3aLd64BG92YHQX7NcyEz8zjnQ_I0t5VCioTd0BD1Emg7fLhyTzthcxkjFiDAYnT9AIYOGSEKcBURE1f27KWH3kVKVix_cWs1ysEEHYhI6s9sCtWiW9bqGGdcyv8GldD7qb94yBLu5xl4Kth9c6lPttARuXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعدِ لغو بازی‌ با خیبر در هفته‌‌هفتم
؛ شاگردان تارتار درپرسپولیس امروز عصر در دیداری دوستانه با نتیجه چهار بر صفر شهید قندی یزد رو شکست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/29682" target="_blank">📅 18:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29680">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/flAmA2d4bqVOABfKQFLYocyR2m27199gPE5Wx7RxC0AfrXiUfQKcpJTxpiNehvSnD8NM5g2j0O0A51fC8AgsPUugVJKLjt5_cpr4tiFyNVZk7dMaitv7HLuf5SrjIeENooM7chUCPQCm_kt645epWByIr9b6fSZCDLHZOCk1uKkAxdXI38el0nMhy2adkmXYB4LDcId5eoqMWdM3Q8HdShKlwekCbdPdoUO4n9kWR2k1ChE7YEBslDtk9-29Fwgski135f68HvXK_xfJ135qV0eHAYeS4UkLTTEx6y8StBjfKSDKr8sU2IBm25cu0ez-pTRkA_6HtqHtRJPHdD9-Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/frlAAcxteDmU96_DzqQCGFwvTRdi7aS3HJOrWjJOv9fQBHPuPR4B9EF4FMASfGw5XYDl8ykU6MWEnzjzJDjQPyB6oe6H3Zb3m1bo1TZT5r_gRjU8gu6X79eRTWMh85QEMaI6KYsia3IT2eBErHbjOHe6Bl6Zga5QXodaXl21jCZm_JZrKCNk6uzVjooqt5iPJfDs4YyhLa6PZfXpBQ-qpc9mOiXz8YCY0IYTBnL8lyPSGy9SIVH9_USGDLsNT8WgslfhH4pIBKnIol9WVTCkMpqKs8oWrVvD9RZFXkwNPSTG8WwTPjmlin5iL2AUMUPaJe35LYWnum47nRTWacWP9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
به بهانه بازی حساس امشب دربی شهر منچستر؛ نگاهی بیندازیم‌به‌افتخارات من یونایتد و من سیتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/29680" target="_blank">📅 17:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29679">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vE3eoS1_oql3rbYMWyqrqOoehfi23gxbEJgT-2-k6e3KM0XqJ0XQ8pTHUmJdSCczl3HO3r1kA867VWhb8Z1h-Xfikx1QmVk_L8agR7uelRdRL24UOeY1KBS8UXnvpt2s4pdox0LoE1_jOlMUMbQ6BDTrfoajBDNfmRu7qObo_OjOUZnynvxoM41oqNPtQWcLh7r3o7dWmRkHDtZ1nEW_dgPhSDe4NoJ-dkNfWZRgtsOC4tRQE-8JdmDkpAhc4J9OBB3flKZTvRcEkujWWgtAALZDjOqunDHxm2Bq4Aj_clt7jRSaooPS68WSPHd4eVKSeHPjEcYgn-Vg-9bTPbtrkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رادان: بیرانوند شامل‌قانون‌سربازقهرمان نمیشود. دروازه‌بان‌تراکتور ازاول‌مهر سرباز است و باید یکی از تیمای ملوان یا فجرسپاسی را برای بازی انتخاب کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/29679" target="_blank">📅 17:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29678">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af9bbd8729.mp4?token=GQWV5zOr9ODkhh82F6H3OD_Ayowl_rQ1Svu6h6NIohspcfrXL15qfteyo51hg7zNoRcjhy0YyUYfmD8Ty25sjZUC1rtORbcta9du2bkJUFHzsRYm897sN_qqBuoppJKftZadprBvs_8Dsc3zw-x5LKGNQ4weqGP_FKGs7UPR_1jUL8JMi2uc6JRkTUtTW3BHHZV9QliJROo6zR26Y_miru4JpV5RxwhWyNcML_sA4wjUX28pcjqj6uTOUEz3SGMOLApKrHFFMnMXKDJjvGYKfxcme5qoSl5ULSTU1yjjWwA4fbh4r8fwPJ3XE_CA4QqvudPH9ikohmvpn3hhsKJQETzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af9bbd8729.mp4?token=GQWV5zOr9ODkhh82F6H3OD_Ayowl_rQ1Svu6h6NIohspcfrXL15qfteyo51hg7zNoRcjhy0YyUYfmD8Ty25sjZUC1rtORbcta9du2bkJUFHzsRYm897sN_qqBuoppJKftZadprBvs_8Dsc3zw-x5LKGNQ4weqGP_FKGs7UPR_1jUL8JMi2uc6JRkTUtTW3BHHZV9QliJROo6zR26Y_miru4JpV5RxwhWyNcML_sA4wjUX28pcjqj6uTOUEz3SGMOLApKrHFFMnMXKDJjvGYKfxcme5qoSl5ULSTU1yjjWwA4fbh4r8fwPJ3XE_CA4QqvudPH9ikohmvpn3hhsKJQETzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رادان
: بیرانوند شامل‌قانون‌سربازقهرمان نمیشود. دروازه‌بان‌تراکتور ازاول‌مهر سرباز است و باید یکی از تیمای ملوان یا فجرسپاسی را برای بازی انتخاب کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/29678" target="_blank">📅 17:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29677">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7865bde240.mp4?token=Zv4i1SKdjbaewOOqkelgkeyMyco1YouSuTcrkIdb6m6UvtGY3yat8lYb_9YIv1JVHHj-U1Ri1SG-j3z8I6qrLqnYipZYLGejOeA9NQavEiYlhQywvCVaZxKIgu5c31C5Bx-TgafIdZsvgqr2x6ctgph5yGn2mQHxRX9LKZLKvo_31u3ieDwp_JYP5Bcr0pkKFbX_atI_HH9ujMMcQM4cIX1B12CSUm6FeY0duJgnKO0br3RSx7z9X1sESHWz9iBjHnqPsrGWQF6KpswOHu3_oAqG08neCrNVyPFkF6CtfqxS6POGHreMeOfW9LKNpGjwgjGl0WZ1p2VTs8Eo3qko5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7865bde240.mp4?token=Zv4i1SKdjbaewOOqkelgkeyMyco1YouSuTcrkIdb6m6UvtGY3yat8lYb_9YIv1JVHHj-U1Ri1SG-j3z8I6qrLqnYipZYLGejOeA9NQavEiYlhQywvCVaZxKIgu5c31C5Bx-TgafIdZsvgqr2x6ctgph5yGn2mQHxRX9LKZLKvo_31u3ieDwp_JYP5Bcr0pkKFbX_atI_HH9ujMMcQM4cIX1B12CSUm6FeY0duJgnKO0br3RSx7z9X1sESHWz9iBjHnqPsrGWQF6KpswOHu3_oAqG08neCrNVyPFkF6CtfqxS6POGHreMeOfW9LKNpGjwgjGl0WZ1p2VTs8Eo3qko5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‼️
#تکمیلی؛ امیرقلعه‌نویی سرمربی تیم ملی به فدراسیون فوتبال گفته علاوه بردستمزد 100 میلیارد تومانی‌اش برای جام‌ملت‌های‌آسیا؛ درصورت قهرمانی تیم ملی در این رقابت‌ ها 300 میلیارد تومان پاداش خواسته و از مهدی تاج درخواست کرده که تمام این بندها رو در قراردادجدیدش‌بافدراسیون…</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/29677" target="_blank">📅 17:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29676">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6h9itWlcCeR9lIMxuwHVWqo51vbTKTbNevPAa-ws-qNKPBhXhBVTN_XRKs8FMlU5Getuj5pdMh4vGJKiVpemcW2BmMOueR-QJjTFNvrqx5wXzCXLaUSPw69CdURXGosm8_X3lplUltCRNQk8rqHqovLtRIQv-hyiLzM5gTuI1kLh0p8HWyxrhDN0376zxqc9XrJZHzmHF5m4WGn1CC7VHJLREpNZQ3m-mJaSeFQNwYw8kcs4IRZVqUzpNKjHPm1C98Tdj-SwNKs37b9i7Nrp7dqtc0x7PO9hgWCFZ_Xagtb4oR9tL0z3kp35C6wpcoG-FiYeON9sqYADQC5XEk3SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/29676" target="_blank">📅 17:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29675">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‼️
برنده شدن جایزه 15 هزار دلاری یک مسابقه در امریکا توسط این دخترورزشگاه؛ یه مدت صداوسیما هم کپی همین برنامه ساخته بود که بازخورد نگرفت. هیجان مسابقه بالا بود حتما ببینید از دست ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/29675" target="_blank">📅 17:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29674">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhWn8FBMHtztjhnwoW5kSMOrs14i-OC_nh9ohRLWAwrtdAS7xkiSs6g20gRdsF0-TBthxCgh6Xqn4LfXY9pm3NUraoqVltXfTe1mfEj2YYrPFqMJrTmwy3ntUJrnAXQFdrs8GG-phCU7tRfWU9P9jlNu95-0tVAn9fqolwYerI8ZHZCVGnwP_--V6lPc0J8Re4X4M63dL4sUy0hKWELEw9lQaXuhHGeNRfEbsyv7a_9jffpGt89cqotsyVmJq2w_efVS5qfpvAoXO7gR2N3q0TPInvFfewjgQly_K9FThA-wpBdvJMwuA9oD-SomEprw4moYTmYjmfyLIItvkXJ5Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
هفته چهارم سری آ ایتالیا
🇮🇹
ساسولو
🆚
یوونتوس
🇮🇹
⏰
ساعت ۲۲:۱۵
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/29674" target="_blank">📅 17:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29673">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YnIh-tPYn8zeGy1RXYUpwAwEBoQkVHLybsIH6pWWZ5VOZj9EsVlDuUn2_-KfzSVHN6AJ1XjsoVgFm2qfHbSjbm7O2ntAleng6EI6J6zeaSB13MD0R_WF4Zi04nkdGFm3MbK6mVN47Y6GrE3zE-vmw_MRxDKmol3VeGWD0JHlTu8-wgzqI_SAVWYb8fGtZRmKK1P42cxfbcgAYqlQ7QSBg3YCDsu1W9WnIwuZSaAw6kLG667iKrytVn7Bs-O9yM4zXkrXCAkMzk-qVhuO1vQAI2srDf3UVetPtNGhI6LG5qoV_DE9Ot_RVcYhOc47W0xfSFpeK67ZLQMhAr6qR8akYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لالیگا
|شماتیک ترکیب بارسلونا برای دیدار مقابل لوانته؛ ساعت 17:45 از شبکه پرشیانا.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/29673" target="_blank">📅 16:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29672">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0d75NvDJ3clA3UjlyA6gWkhLo1FOXMmPcurtSwtOTERFFXmWMocOsf_PsCXqrgdmZ_NjaFbAHli-d1hXOXOi5_9zbT_jjmGoCE5c6AY7RkMaNHQvug4GyqwZjNi9gWtkrIft3iXHDMKTkGspmfwrAnGKMbUrptftrwiYFHC_0xOYhF0oyclRrtcuv6l3k_dHeMUv8zz-egg6K551srZIEFKjyEJkZ17P6gkfJRltVV1H0CGL85Atxcp5sKG-ZWa95REWE6IFbKFws4tUncR7JR3VDhB_D5uI7JjeB1OANKZxy76pFSfppEcKVoKM_LJ-YdjSBlCCyg4O-dZ5b_MyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
به‌مناسبت بازی فردا استقلال مقابل السد؛ نگاهی به تقابل‌های آبی‌های پایتخت مقابل نمایندگان قطر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/29672" target="_blank">📅 16:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29671">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/570942af95.mp4?token=MoYbjX8At1cX3BV45POOdZRvfb9gQv5dEDAiYI7l0BJbUdRPGNIFvkoy9Iend2p17DqAGLWtQB7SG2E3tC_QQwcPS55MmB21DEj2inIoO4jKvEEJHJ6RcX1rDih9MDOjVPpZ_uzGZBIAVE8qGvvES_KXQpYnochpkaM8Fzlk7IBOG6MUxCS-D0AL8-AtSiuB0qbVgF8x4hzZzvzIK-8bXQoqFlul3gSny-2BZRmLAbAqmAgOkgw3-KTdP3laH3Vpx2qEjP3ud5Hj9plFy7CEZeYMrL7TpLEPFWW8EX9JWzEcaXKn2spgKaP9azFLOEgaA7ApcmoRCPD6cEe3DgaJlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/570942af95.mp4?token=MoYbjX8At1cX3BV45POOdZRvfb9gQv5dEDAiYI7l0BJbUdRPGNIFvkoy9Iend2p17DqAGLWtQB7SG2E3tC_QQwcPS55MmB21DEj2inIoO4jKvEEJHJ6RcX1rDih9MDOjVPpZ_uzGZBIAVE8qGvvES_KXQpYnochpkaM8Fzlk7IBOG6MUxCS-D0AL8-AtSiuB0qbVgF8x4hzZzvzIK-8bXQoqFlul3gSny-2BZRmLAbAqmAgOkgw3-KTdP3laH3Vpx2qEjP3ud5Hj9plFy7CEZeYMrL7TpLEPFWW8EX9JWzEcaXKn2spgKaP9azFLOEgaA7ApcmoRCPD6cEe3DgaJlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ گفته میشود قیمت پلی استیشن شش که درابتدای‌سال2027میلادی رونمایی خواهدشد یه چیزی بین 1400 الی 1600 هزار دلار خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/29671" target="_blank">📅 16:06 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29670">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rj5nrCvw74If24WdgY8P2FqiUH0nzTazRZZedD9R1zH72XP6VLIy7oONH9qwYWyh6rze4f58qpTpFnj1I0trEQP-f3821qN6mve4OmFc0bKh8a3QuCnNwDIbMy71Bbd38IcEkBZeeaNi9gxj28kmL1DlGCoo6CXcZDMoCsbQKKkjG3EA6FaYMEW9sKu72Des67Ha-0lvh2lzWieQ40hI-sWuWS4uhzuewnApsvrU_vbF-BvSoUj_wCXpK0vDXH-NwMFC2NMUaGJppxQygyPIRTZ5gvDtaS9pBhypJPuX6hGzIwSohoXGKFCuOKi4-Dfy1qL8BcfxWyVoEiu6_EC-xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فینال‌قهرمانی‌آسیا؛ شاگردان روبرتو پیاتزا سه بر صفر از ژاپن شکست خوردند و قهرمانی ارزشمند این رقابت‌هارو و کسب سهمیه المپیک رو از دست دادند. یه زمانی همین ژاپن آرزوش بود یه ست از ما ببره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/29670" target="_blank">📅 15:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29669">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7GnrkmbTVmZyRyukfsC1NcO9OePbo9IhUXv8M2UsSFp5NRq46Cr917wLEXiLP9Z9hB7W82JZeBmpTILkcJLXFjcrwuPRUoAsBlnfN-WUZBARrsJno3DqWBftMFlpbVGbs-Ls5qj2F4SIqOoQAOu81hJEaHPNg7myqx8nXwMfBpg6Anb5GzESUQXi350mg5YRBKaxp3Qu6-RB2GHiVdw5lPFfAjKYAsVeo1uiSHVQ4X6GLdGRInS4YCZDc9XbYPaidbKqC2x5yrrEgCZPq_1SyaKEZrhZYzfSCk7eRO_d3ehQhopfB3f2huPu6wYq9rtZuQ4duF_AHdL6jIF72AhcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های منچستر یونایتد
🆚
منچستر سیتی درلیگ‌جزیره؛ شیاطین سرخ با اختلاف برترند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/29669" target="_blank">📅 15:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29668">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXKT2DUY36eebBDQMFrKSdDLtbRTsJJyD2VFeeG_r2ohy8M_A97J_bTfA-P66jdP1hDEoyOE3G6KNYKODd32egFOUKBrMTcTa2CUCdJmGy6NnsbmR0xng9P6lukxBnREOUo8lORqE_SOop8BSkjpOMmP934CsHb4AMQx5mJkTT6PnhwgxrLFrywhOA1mXKuPx_-HTkNhPg55yR1_XWcmiHcCVKj8LnY15X1QWXA2hi7iieCpaz_U7AJOUsT_G3aglVy2yvuxw-27UOxKEgkPacg2P4-lcQNyaw7zpkWJ9Maj076eIXFW5sX_jdfyNXQixT6ipBwuIkDwV9j8HmM-QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کمتراز یساعت‌تاشروع دیدار فوق‌العاده حساس دو تیم ملی والیبال ایران و ژاپن در فینال جام‌ ملت های آسیا 2027؛ نتایج تقابل‌های دو تیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/29668" target="_blank">📅 15:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29667">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f478bf5a4.mp4?token=AqNP0U726F1c6tJ3juMH3yXCMYcvbzNTL0n4nOUYaNDIIi3rU2Eit-1fLxDPBgtYoMrErOLleazT2tU7w30ztzYYceWGfQVL9gLmVoKbQ0Q6OudPVGQuvIEHt26h-m5bbm9h_i89WQcvuzYv0alQ7YCUVuG7mdJ7rz7t0ZoOBFSFWgUoqlo9yt3y65agEiJ5l-D0H_LU3CPZ357doKNcZpeFTPLGRSv-dIIwyXnM7JQRijB7iKX2OLMtmkpjhdlzKPgl5mizjKipXahrJH7oXF-ZojOd9AWZvIpjKLPOiTwYndd8Qa999V8X7gunnPvMPWVk8ZiiWyAyEBIRNT_NiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f478bf5a4.mp4?token=AqNP0U726F1c6tJ3juMH3yXCMYcvbzNTL0n4nOUYaNDIIi3rU2Eit-1fLxDPBgtYoMrErOLleazT2tU7w30ztzYYceWGfQVL9gLmVoKbQ0Q6OudPVGQuvIEHt26h-m5bbm9h_i89WQcvuzYv0alQ7YCUVuG7mdJ7rz7t0ZoOBFSFWgUoqlo9yt3y65agEiJ5l-D0H_LU3CPZ357doKNcZpeFTPLGRSv-dIIwyXnM7JQRijB7iKX2OLMtmkpjhdlzKPgl5mizjKipXahrJH7oXF-ZojOd9AWZvIpjKLPOiTwYndd8Qa999V8X7gunnPvMPWVk8ZiiWyAyEBIRNT_NiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعداز کامنت‌های‌پرشماری‌که زیر پیج السد درباره غیرقانونی‌بودن یاسر آسانی در ترکیب استقلال زدند این باشگاه کامنت‌های اکثر پست‌هاش رو بست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/29667" target="_blank">📅 15:33 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29665">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b2b549c3d.mp4?token=nBDwUtyy9EuNlegMqmLirK-J4GShBNnTN6LC9AFHjF3vyJNFAoEOTagHypWj1OXHCSQQUHfUf1dydKlBXjjY9v4t74NRQH2JfLuVxEi2WDpHJc2jqYnEuHjh0qbKnY-jJKP2EfSSx_GLJDoLEHdnkeRq6X6AKD14g68s4xENmmGXgKeOxNWgMGwSnsXtTNK0fpapWiDiUmWyd_bAwZsQhybA5I10hRcXALxrSr60iKdzngXLsHHCgFcMxvDS8MYwvHVyTFMH0_S0ORqBuMFBxZaDNrvAzx7DOjyTXoATalR5Z-0aBeWzWTdzNYWSuIS9REf7coUmeVlmyyJpMrxA6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b2b549c3d.mp4?token=nBDwUtyy9EuNlegMqmLirK-J4GShBNnTN6LC9AFHjF3vyJNFAoEOTagHypWj1OXHCSQQUHfUf1dydKlBXjjY9v4t74NRQH2JfLuVxEi2WDpHJc2jqYnEuHjh0qbKnY-jJKP2EfSSx_GLJDoLEHdnkeRq6X6AKD14g68s4xENmmGXgKeOxNWgMGwSnsXtTNK0fpapWiDiUmWyd_bAwZsQhybA5I10hRcXALxrSr60iKdzngXLsHHCgFcMxvDS8MYwvHVyTFMH0_S0ORqBuMFBxZaDNrvAzx7DOjyTXoATalR5Z-0aBeWzWTdzNYWSuIS9REf7coUmeVlmyyJpMrxA6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
هواداران‌التعاون پیش از بازی شب گذشته این تیم مقابل النصر با هو کردن نام دیگو ژوتا ستاره فقید لیورپول حسابی روبن نوس ستاره الهلال و دوست صمیمی زوتا رو اذیت کردند.
‼️
در پایان مسابقه هم که مساوی شد این بار رفتن رو اعصاب کریس رونالدو که CR7 دیگه جوابشون رو با این حرکت که میبینید داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/29665" target="_blank">📅 14:46 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29664">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mupLnvTcGPwuDir8228zC9bqfjEQ7HpBp6fDZjFMSRwJ7rU147H9ATvCv2vL1R-KY8zF8gZxEOWLnobaBeM0mixMbqXDwXT2G4k1XjejxpYN9U5DmixMmvkXKDGqe8cNQzfjrXpaQ5ECDgIsMFzpIbVsnV6AKSNM876K09QDd-wBjB_BRSwvrm4wMYkwP1-gSKaqb0-2wV5xji3-vaqwghb8bI3s222Ix1qrnmp5x-sFGwe5l3MGgA7RCjUz0YEz-fCNE6gVYrIDynGnO7NxgDnnLShFWgR3WvW_Ve56vy_p8r9Oc9krbi9i2njRPhmMmPyMma8AUrGdn8XhiENWag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خب گویا صداوسیما بهش برخورده که مسعود پزشکیان گفته بود تلویزیون دیگه ارزش نگاه کردن نداره و قراره‌که‌از فرداشب‌مجموعه جدید و جذاب امپراطور دریا هرشب‌ساعت 19:00 از شبکه تماشا پخش کنه. بعدش هم قراره جومونگ پخش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/29664" target="_blank">📅 14:16 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29663">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltXbbVS0Fp4Q8IEK0Tcubte5uoBdT-BodLu4Ov15dk5wem79YDhpzJUlaLc1psUHdx9Mf-68LDVAgyL7-KGxV3-QqTEIR-ulGt61n-mUMrn02FyZmgiS9fk2JLOeo6UM2ued4GdJoxk95ATrlzl_g1d7S5nIaf82_IR9jz0W-htWw_52lKW5ugCHLwmgYZe8F-vmJShf1uqIX0jOjPiImSSFWgB8BIUSUf7F1os0GVjI3vaIlh34ihH8xzqC4wuHSxcuRV4VzqyZm_VUURmSvd3Md3yMUrXUkFZc3eircfV5duwSl8zt_dFB4fQ4sPpvlkHwyx8f8hZ7bE9K2Xz2EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برای خرید آیفون 18 پرومکس در هر کشور چند ساعت کار لازمه؟! خودتون لیست‌رو میتونید ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/29663" target="_blank">📅 13:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29662">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mm50EgbCqreBxax3o2HlHkVX3T99xrzZKWzeZ4cPVm64Z431lRArKfkGiiASjqOByY4H3ZoERi8RTXD9zfUuAs1anNKABxfqTVQsQKIg8SU6S7y_B1MulxJE3cYBn6Ci8GHqma3EF2fq0xApvI3sD3YFT8T3cfCrVak7F6CbVMX0aSa8GflFNUQssJaDLY2T114Tg-WUG7bkgH5S0sQZo8x7tudPwsYMGZblNc0iPA7laqpnTBRqWNEc5sivHgkHHf-tBjpR5c4z_8wlFrpl99vOyhsgHHjxqx_kR4JDUL9esLSKjxdvIGeacVKKb-ZKHL2flu0EHlRuOo-NsrlC_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از توافق برای تمدید قرارداد آردا گولر؛ باشگاه رئال طی‌روزهای‌آینده‌برای تمدید قرارداد جود بلینگهام تاسال 2032 با او و نماینده‌اش جلسه برگزار میکنه و به‌احتمال‌زیاد توافق نهایی انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/29662" target="_blank">📅 13:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29661">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TizcT9Yen1h6mdaOvErsq2vf91gA4MYVUpxcMXQklVX1bL6SrEm22khapTJ-dDtcJVHiWd_s0AAOFY4sVuKaGZscGHienieu4wPWN78le5hoQllzYnC832GWXhmoyXczZDdJNyRLBv1kYv3Gns_fMH0qhXWnaIwuXwnXk2VGQllnJBgPZtEQQ18gtnIY-u1J9GP-y2Vlc6L1a_0UKM0F3PIIX-lXQLhOGsUPCB98RJkGZXHw_s4KZHzLfxqX7-5wG5tx-IAX_i2nfJD1dgUwCX_o23BUAk714Q2OjlqMO2PeWpJZkGVvg81qbal2RC31droZKbQTiux-WyCzar_GkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برخورد ناخواسته و عجبب و غریب علی حاجی‌ پور بایکی‌از تماشاگران ژاپنی حاضر در سالن در بازی امروز ایران با استرالیا که بعدش‌ فدراسیون والیبال بیانیه داد و از هوادار ژاپنی عذر خواهی کرد.
🇯🇵
ضمن اینکه تیم‌ملی‌والیبال ژاپن دقایقی قبل سه بر صفر کره‌جنوبی رو شکست…</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/29661" target="_blank">📅 13:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29660">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DeWMmqHfHQcHiL2AJndUit_-kPF6bXFPStmoTw_CqG3imNgbtEaVAWduPR9Y07lvwf-jjVcLzrOW8Lpjq9O3ZcrTa4XR0BEImdWP8vU4ovdpJemzk_1VtGk7IgP2UuKTIS3UA_1kQssdO8I-Xgym4CosYiElJGSt2RezoFT_lH8GXn3ym9ipeh0_TWp5NZpPnctF2sJzEuesvy92T99QYi4p-P_55lRQcidJZtFqc-kggPWRnOi1vrJg6kGD5dhn96RP43IM1YDQ-u6VJmuCJ1mmn0CvBq3qBH1lERst2U6WIBJ8Ewu15J9flJRT4J_6WpXZUGD_yKshDLLN6CDJ3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
گلزنی‌دیدنی‌لیونل‌مسی فوق ستاره 39 ساله اینترمیامی دربازی‌بامداد امروز این‌تیم مقابل نشویل صدرنشین لیگ MLS؛ بازی دو بر دو مساوی شد. این 928 امین گل کل دوران حرفه ای لیونل مسی بود.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/29660" target="_blank">📅 13:08 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29659">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1eab57eaae.mp4?token=NK_jffZK3JaTHBHQLQJePF-mOau9pePIxkLi0f5oVWNufQPpgEFO9YX1F-DAfPuWvjKGV4E0f_VnViUEorprHvfX0ilOL8PpWDouvJL051CLceG1daYI2S4BximN60Gb3PE3GjEk3gQ2ACZM_o9rhq4bvZGdYrm9qMGlK7Z-0i1VijLHkgLBm1D42Ov2v92zv2FMGluCpdtRgo5x54vKwSv4cZiZ6EKPbBWhkelZa9qibr7uSOgEx0kkMyOyZr6ZIlD1t-9if2GXbuIh9dmOv6Xe1MDho6z9X9rLBH2xX3lEAb0C_Xb8-SJa9ZSHAOl8n5hvEtC_xr5UhuoLT6wDBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1eab57eaae.mp4?token=NK_jffZK3JaTHBHQLQJePF-mOau9pePIxkLi0f5oVWNufQPpgEFO9YX1F-DAfPuWvjKGV4E0f_VnViUEorprHvfX0ilOL8PpWDouvJL051CLceG1daYI2S4BximN60Gb3PE3GjEk3gQ2ACZM_o9rhq4bvZGdYrm9qMGlK7Z-0i1VijLHkgLBm1D42Ov2v92zv2FMGluCpdtRgo5x54vKwSv4cZiZ6EKPbBWhkelZa9qibr7uSOgEx0kkMyOyZr6ZIlD1t-9if2GXbuIh9dmOv6Xe1MDho6z9X9rLBH2xX3lEAb0C_Xb8-SJa9ZSHAOl8n5hvEtC_xr5UhuoLT6wDBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
هایلایتی‌از عملکرد درخشان عارف آقاسی مدافع 29 ساله استقلال در بازی هفته اخیر آبی‌ها با پیکان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/29659" target="_blank">📅 12:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29658">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHLXi7UKAlQq955pLEKT1107jbIMSX2JCSGpQFU8PmIlHWL4KEM1e0Zgx8hTHssXjwK3VRaSEHcc5A3pxbLusyjNvxF91uoI8615efjaNbqiJpW7IqIsGrM1qluOne_lRNph0mgwhD2o8tUAbwnDKaY8cDnuAP1B5UUNy6E8KfYqlvT25ltzqA9X3snq7OXFU9TyMbAjja5t-tOHzGcAGjcfIloKjflnpGMAQ76Md6q29CTTFMaypZnAmeQBrvkxMQMPqlymA4fjj7aU91yYUsUT7zgV12PnFfcQ-HAkzCDSdyFg8lEOyFaLKVn5WvYhj5hdt-kzD2DwV-aGAA74tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌دیدارها‌ی‌‌‌‌‌امروز؛از دربی‌جذاب‌شهر منچستر تا بازی بارسا بالوانته‌برای‌تثبیت صدرنشینی در لالیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/29658" target="_blank">📅 12:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29657">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9b08e88d1.mp4?token=rvIzBdqmnURk_WCodABMRIQcdZgFRb4belj7iui-IPw-B92J2zSQE9EDZaDscEiTtaJx98duj6um14RtSgQUQXqLFYqyUHqtEA-D1ncpx0j5chnhtQHTLOWyW13CrZEFs21aybTWqBYA49Ji1CEeQKZnh9efcnkXGvbq_-yNj3J0pnvGd3jVwNQBPBKiy7oHoWvQ59Ju5-Dvw14TPbYm5IabOUnuiF36LvFfaE2gS9_a-DOsDadmUIOgdP2N_VcV_DYqJyM_gxWlpz9Y5nS-reK22JdRCfRL8UvvUttqXw55POVE81D65Ny87CekcNXExllwQqN1jts9chIbL2sb1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9b08e88d1.mp4?token=rvIzBdqmnURk_WCodABMRIQcdZgFRb4belj7iui-IPw-B92J2zSQE9EDZaDscEiTtaJx98duj6um14RtSgQUQXqLFYqyUHqtEA-D1ncpx0j5chnhtQHTLOWyW13CrZEFs21aybTWqBYA49Ji1CEeQKZnh9efcnkXGvbq_-yNj3J0pnvGd3jVwNQBPBKiy7oHoWvQ59Ju5-Dvw14TPbYm5IabOUnuiF36LvFfaE2gS9_a-DOsDadmUIOgdP2N_VcV_DYqJyM_gxWlpz9Y5nS-reK22JdRCfRL8UvvUttqXw55POVE81D65Ny87CekcNXExllwQqN1jts9chIbL2sb1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سال 2018 در چنین روزی؛
ممفیس دپای ستاره هلندی لیون این سوپرگل تماشایی رو به PSG زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/29657" target="_blank">📅 12:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29656">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAG8Kf6o5A5Wq1ewDjB6AaXdpnVfdSl-_pJdz8jOs99W8OS8ZVRbQiciaOncmHCo_LJo3r4IcWQ-cFf7w4EEI0T3YsNaWSL9_RAPWPA3cx_FTDo0EhHGysmIjf3-T4QzWiUSNNGfyAW6wHcnNYX57fKmdXQfDuZ7Z6WZtiLfcLUesMQrPovYKJ_olDB5i5fU9bD_hnpjkEkBc0ETeDf5K27nye59brFhB15DBaL5vS2_RCouFLSvLW81P-L47DMMq6KtJTs6t4qK0pvhUnOMM5mLsXCYv4sCTP0zshUd4-lzhz25sZ5GM8Q_4xsoIWdRlr3Kr4mdKeDCnIEUGgytKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴
هفته چهارم لیگ انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچستر یونایتد
🆚
منچستر سیتی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⏰
ساعت ۱۹:۰۰
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/29656" target="_blank">📅 12:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29655">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uw6dCRyN5VP8GgVzQaHO_0CRTbMeWTAqfnwHZy-uaqca35163K3YyvyhSrmZcqFlGfPjlPjiEiyI5XQ2zuSAvCR0izvnH2OtR-sAnJoHi94Qe1HyoF0vUdLpzptbGVMPIxq-jHDUGHO9_aDE5TeVtmVDBcDwylSQAC1JnsB7UJj0Qfei0D-wnOctQ4NYP2SOeiz43kCEv8-eLidv3o487HE7-Qb5--WdGPbjFV99qvXwYr6U2aBS5qgdgv-Jlq5wAIkYm5rPZ5rOrdx7W-Z6JJ2UOSugBUngmXzEr1H6dNRs3b-kjvL-m_BGhjAnmPs2kNR1xqJxrIPYlnJXBSR9rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
گلزنی‌دیدنی‌لیونل‌مسی فوق ستاره 39 ساله اینترمیامی دربازی‌بامداد امروز این‌تیم مقابل نشویل صدرنشین لیگ MLS؛ بازی دو بر دو مساوی شد. این 928 امین گل کل دوران حرفه ای لیونل مسی بود.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/29655" target="_blank">📅 12:05 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29654">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6HYrI1vxSeQkKwfkJaC2Pa3fJRgDT3CMyVUUtn82NgN-gqxlU5uw2tP-K0hBm706cnICX2zlNZK3YcAtpGf_vWQK-bgT2uSzevmg0zogLyftR-WkV8CNF4rjdJK1uB_gEzpRSLnmNW7ibc11POM3sroWBixnZg-9k_s6yWfVyxFJZdVjnP-uwQjHMr5osB7uE8EfbkESMikjggW5h0B-D9U9lTQ5rKAsODTh7i4Zm3pEB_lFmAecV-atj-lPeBfcHl-zRb94OLJ1AzgX8MvOJ0OYRxwRKjhdlxMbBrq3ZpU99LH0WUvl5HJepxV1lbW-ZfVs08nf1nh_M4Kfgl6mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔴
طبق شنیده‌ های رسانه پرشیانا؛ بشار رسن هافبک عراقی پاختاکور که‌اواخر آذر قراردادش با این تیم به پایان میرسه از طریق دوستانی نزدیک خود به باشگاه پرسپولیس اعلام کرده حاضرست نیم فصل به پرسپولیس برگردد. طبق‌پیگیری‌های پرشیانا؛ مدیریت باشگاه پرسپولیس اماده عقد…</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/29654" target="_blank">📅 11:47 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29653">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFxDrCes9JP5OrK7P9ocBUNuuF_8sf9N0fHcbmo0KEXfcbAuDOG9iB9VLWOpDPpqiAL4W3VFZdmkL4AN_y1jD4sSMoI0hOW0kKsO6UiwX59FVyTY-CwGYAoWJNYiNCR5f63x0GXIPGYeWRHKv5jRpbhHpeVuBl2i-98Qlp5Kqbj7XRDUEq-qHPzNCr2GYjoSeDWbUOUNmb1-rRoNkakngSdWFejO8a24yNmVR4TV1XSyXnavZXWXu74BeVfrzWTPUSInyy_M42zLF1ZheGKCXXwVD1CRGEaLtiTkhtosPy_aNvgOvbCPk3gEhsPK0ZW055JrPQuhOvuTsfz-09a0zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
#تقویم
؛ 138 سال پیش همچین روزایی اولین فصل لیگ فوتبال انگلیسی شروع شد که به عنوان اولین لیگ فوتبال در جهان شناخته می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/29653" target="_blank">📅 11:43 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29652">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال در روزهای‌اخیرمذاکرات مثبتی و فشرده ای با مسعود محبی مدافع میانی22ساله خیبر خرم آباد انجام داده و قصد داره با او قراردادی بلند مدت امضا کنه و نیم فصل به جمع آبی پوشان پایتخت اضافه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/29652" target="_blank">📅 10:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29651">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">▶️
صحبت‌های‌احساسی‌لاله‌مرزبان‌درباره مردم ایران پس از اعلام نام او بعنوان بهترین بازیگر فیلم ونیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/29651" target="_blank">📅 10:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29650">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjPHgmB8mJmC4c6swpo8YZM0O0L0euMmYiSxekcgiDu160798EL4xgEDENOex_suv2bpgsD-QwhA8KnKGxU7_pUCwAZ8-jrNu-mexh5YpIaaOZjEZ8a7mrbG6xbbUuAAor9rkmbk-eIMM2hKG3VmpBpHGt13MH9YA6O7OuvzFgcqGIaolPzwQJIFBy7QLDoglJdSM9ADLY5DvhzdD8OYZw_jfmLSrE5bwXsBSKzmWAM4crpHoRyCh1NDRFbp7v8YhUIaqXvzsknL5ic7z6sQMj_cpuy4N_YNWDE3OmWfy3fb9UfCIVlG00CSKzpcelOuKVVg85pF93vFw6lfAtqSsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌اسپورت:
یاسر زبیری مهاجم 21 ساله رن فرانسه‌ که‌این‌فصل‌قرضی سانتاندر بازی‌میکنه که در این 5 مسابقه پنج‌گل برای تیمش به ثمررسانده گفته رویایش پیوستن به بارسلونا درتابستان‌سال بعدست. بارسلونا از علاقه یاسرِ مراکشی به این تیم آگاه‌ست و به احتمال بسیار زیاد برای جذبش اقدام میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/29650" target="_blank">📅 10:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29648">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‼️
#تکمیلی؛ محمد قربانی، محمدجواد حسین نژاد و مهدی قایدی سه ستاره ملی پوش لژیونر هستن که در در حال حاضر در تیم هاشون شرایطی خوبی ندارند و باشگاه‌هاشون هم درنیم‌فصل علاقمند به فروش آن‌ها هستند. به احتمال زیاد هر سه به لیگ برمیگردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/29648" target="_blank">📅 10:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29647">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/379e42f937.mp4?token=GptfafHSfCbwOQgMXvlj5zAI9ZrKJkYkL72rTa7wcpXQ0zkck3iPc4W1ZeOud70mJWET30CuwYrW9XUUk2fw91H1stOEdaFghm0_4SDgNnQjs1UOh7bJ8K77888dJ1TMO7OJ81HG4LG_xr97X14sLIo9VOmZCJGmgUfUXpiEyFcKJRlnfFAwKbuCSOLDoE9vO8SdulocHhS0IRHUv4azRQEyNCp0P6RyQ_Ru9LE4YoH7-W30UQXzqxlISw0YdeWACEeURepro6r4iiJ3tWSbeof21AZ28V4L-K76CIttfBAWluDuPKZkgSwKHjESYkp6MH-g8PhRb6yEhrWw9fPJnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/379e42f937.mp4?token=GptfafHSfCbwOQgMXvlj5zAI9ZrKJkYkL72rTa7wcpXQ0zkck3iPc4W1ZeOud70mJWET30CuwYrW9XUUk2fw91H1stOEdaFghm0_4SDgNnQjs1UOh7bJ8K77888dJ1TMO7OJ81HG4LG_xr97X14sLIo9VOmZCJGmgUfUXpiEyFcKJRlnfFAwKbuCSOLDoE9vO8SdulocHhS0IRHUv4azRQEyNCp0P6RyQ_Ru9LE4YoH7-W30UQXzqxlISw0YdeWACEeURepro6r4iiJ3tWSbeof21AZ28V4L-K76CIttfBAWluDuPKZkgSwKHjESYkp6MH-g8PhRb6yEhrWw9fPJnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
آمار آپدیت‌شده‌از عملکرد کریس رونالدو و لیونل مسی در کل دوران حرفه‌ایشون در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/29647" target="_blank">📅 09:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29646">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5a250924c.mp4?token=KAysH6f00GWyxBk3Md6Nc8F_p5l4RVNLhwhIW-w3VxTKivjBJhnLYMqAtyAbt1eXCRTvftRt_NMooOg7TMSVwvU0ZTt0zgWEF7q-phP45T_MD9-bKNxn1HXvwV8pJ1GXa1Dj1Ig4lrRyg_jCMHndf_rLyz7LyXAZ2lRBiGKIi31ew_0I5R7mNqs2iQRF9hZvXQow3KEaPY0w7zF-4pwwZJ7YP4ct1ZWZ-WrDiI-IUFq-Qs_0QuxMLVml7_ztt19JiDM7I1PirhRPiINPnHkvpv9E28c32upsDWSN0kxKEVAT84s5oRib3lBMPEM82WtCVmbwqVqALzBLBPM7bOUO1IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5a250924c.mp4?token=KAysH6f00GWyxBk3Md6Nc8F_p5l4RVNLhwhIW-w3VxTKivjBJhnLYMqAtyAbt1eXCRTvftRt_NMooOg7TMSVwvU0ZTt0zgWEF7q-phP45T_MD9-bKNxn1HXvwV8pJ1GXa1Dj1Ig4lrRyg_jCMHndf_rLyz7LyXAZ2lRBiGKIi31ew_0I5R7mNqs2iQRF9hZvXQow3KEaPY0w7zF-4pwwZJ7YP4ct1ZWZ-WrDiI-IUFq-Qs_0QuxMLVml7_ztt19JiDM7I1PirhRPiINPnHkvpv9E28c32upsDWSN0kxKEVAT84s5oRib3lBMPEM82WtCVmbwqVqALzBLBPM7bOUO1IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های‌احساسی‌لاله‌مرزبان‌درباره مردم ایران پس از اعلام نام او بعنوان بهترین بازیگر فیلم ونیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/29646" target="_blank">📅 09:44 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29645">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrbaR7b6mC64SWtuO-HxVrdfleSBAOhAwZcOZoIxYaG6AKqbk3-sAOykNa5mauPHRP9IkMI0JXHVibrRwnCx_uh6NyoGuoBtbjseTP7m7gZZQC-JUxVcHrnWT-cVCIbu13EQOJ-n7jlHjw2ayYzDjO0Zc0WJvZo6fjhDPrRTPhtChA2K8FQhTxK9aq4DXQwsifufcpJXMBnMP0liSXmGtu-rHgRkXu88VoFbJHQTNDX7k_z7ALIWQR1c3V5uDb27PJRJ9gGQr5OnfM6RXzkAV21pPN0cwr0ZOOgBmrwOnm2loqIQBWGQyWiQM8oGBgm4lv_UmjzrNDVaeugAr1bkuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
مصاحبه جالب و عجیب و غریب مایکل اولیسه ستاره فرانسوی بایرن مونیخ در پایان بازی دیشب
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/29645" target="_blank">📅 01:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29644">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔵
ستاره جدید الهلال افتضاح هفته‌قبل رو جبران کردند؛ الهلال امشب با درخشش ستاره‌های تازه وارد خود 6بر0 التعاون‌ رو شکست دادند. گابریل مارتینلی ستاره گرانقیمت و تازه‌واردآبی‌های ریاض دراین بازی موفق به کسب هتریک شد و واتکینز دیگر ستاره این تیم دو گل و یک پاس…</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/29644" target="_blank">📅 01:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29642">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWR1ezl5azbA0IUEepBQbb5pc3OnilQYM6c0RS03QaOg73RwPGSUt04PJ4Hd7Rl23qVHWK2CMPR8hnQkzXM55qR_3MJ5Gt2Ac1X4Gqc76_uPIGQ21KRQMPNqJq7I5lMZvrS3j3l--GhycU0jPliMiX_6l4P8c8wtgi-4tJdEzGl5iZdWeLonHdP-MhP4Ifi-XmLpcl7jmislE-LfcNOVHVIzhxweoeCBR81lbRU0MiS5mHmvNArkY-XfiXfeys60k4onq4LrUznWXq2BuSFkVM_BXcn9EdCkga9urAlq2EqGOmub9CFDOCHu1w1CCS-5sVW6CghTrmWMjxkv2oFDHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌دیدارها‌ی‌‌‌‌‌امروز
؛از دربی‌جذاب‌شهر منچستر تا بازی بارسا بالوانته‌برای‌تثبیت صدرنشینی در لالیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/29642" target="_blank">📅 01:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29641">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROyy_grIL_iwd-ylw80wB4_JG9pyqu911iALxzTC7a5OhXrQ_VXCOGUuiofN77zBnwIX0h22Iz5lI0IhmagbBDw5zKJWrNLWdY7dnPmKG-RNAPYr-Q7mdoSSEPJHkwMdbpslrMaHXloA64okVOSLjW_ZWzZUpm-9oz1BDpFvHbztj63zMNCvmLrM9-jBzzJIPf1hRUvdddoRztd-P-bvuTymTwFQkUmGmMxicJhCe5YU7Y5djBNMqj3EG-bNKYcX1XwKYKd_8lNAPeaYgMhrdNdXaM8uXviCxvVzbQOJkWSSnFCgHzsmMj0EBPEod74I-uBKvqZm8a2AqOIPXGhNyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
از توقف همزمان لیورپول، چلسی و تاتنهام در لیگ‌جزیره تا برتری پرگل شاگردان خوزه مورینیو در شب درخشش کیلیان امباپه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/29641" target="_blank">📅 01:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29639">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d04IxtZ3cLe2EPkwvMKaxpRp3m86Rs2m9Y-M72wmpSM0t04m02YRrmreba0zwBsQdoT6clMP2CiESqVm3LcsZ5QgZtL8ZYaHWexLKt11Rg4haE3wDfbDxpDzGFuo47cft6P44HJ3Sl1eZXesaJrwktzR-whCVmhAwDsZK7RrZxG8ZhakAncAZuidMM-Z9qJMvHbrYxKk72TW6x8rxU2XDIJnSfzdyYXDx9eo4RjdmgUL3aclfCLPo650XAZMNZfgpiZ_gtMVm-lWfmtEbYkj4fbE6yO0L5Wl2ZxBFVrVnBLaPp14-59VlMm3higqYYYwzIv_tuklUbggBJUPaK34Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
تصویری‌زیبامریم‌میرزاخانی‌ریاضی‌دان ایرانی و استاد دانشگاه‌استنفورد روی‌جلدکتاب ریاضی دانش آموزان ایتالیایی؛ روحش شاد و یادش گرامی.
🖤
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/29639" target="_blank">📅 00:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29638">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02bd31b46f.mp4?token=ENC-1kD1q4QSWP2rQOTvf6vqH--_qFO6hewSfhw2PruQySrOutDGHuhkyF7mA6nPy6M8lC4tWtmeVE-FGGDLZQ3ClCDbj3UAK2Qq02qgnq90i8Af4NFZUe0PopEyaTDgH5qLMwqQdLvNajulODysSF6WChKsQXxHQYT08BUkUu-FQHqkDGM9pTp95CUsZrelMRNHnS-WmcDTQRJJwCuHjId6rZ67_QeCoKd97rd2iDG20VQMc1Pe-K1W6YPwc_rewB6Vf7pmqzme2KIUggbvJIwmOj8LZdWWnhjEXbLFViC-0OlVqNWSzadPqb2vUIEEm-bacjgnkwld3GQlT3BS93rFWkp0LuIFRYpWEjsjyra4yupXvaXxKeWPLiXtEk-yETRAQ9I8cfsBjoOh-TotRGBq6LakxRhOYEDm4hiMyALKmYWa_DzNBDJ0pUyyi9U92hI00MlCZEEQEDaNeRzBPTAHB8tRJ153rqkEF-XqHmVn_MgVQk_s_L7ZPkIYgm1zhH20GYx4Yu8U_y1yH-kLFpCe7Rtk9KNLdyH9eTZyizcvN8TJO7xOpwzcbK7jv5PUnP1v_D7hJ2usKEeuWrWnhAma9a1ng_IXk6ptCtu8V5dmWg7pxBM8nKKwB44OQZPRbR1jlQk96cgEASkA2k5KWX62qLw5FiXs_YAtrguNguY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02bd31b46f.mp4?token=ENC-1kD1q4QSWP2rQOTvf6vqH--_qFO6hewSfhw2PruQySrOutDGHuhkyF7mA6nPy6M8lC4tWtmeVE-FGGDLZQ3ClCDbj3UAK2Qq02qgnq90i8Af4NFZUe0PopEyaTDgH5qLMwqQdLvNajulODysSF6WChKsQXxHQYT08BUkUu-FQHqkDGM9pTp95CUsZrelMRNHnS-WmcDTQRJJwCuHjId6rZ67_QeCoKd97rd2iDG20VQMc1Pe-K1W6YPwc_rewB6Vf7pmqzme2KIUggbvJIwmOj8LZdWWnhjEXbLFViC-0OlVqNWSzadPqb2vUIEEm-bacjgnkwld3GQlT3BS93rFWkp0LuIFRYpWEjsjyra4yupXvaXxKeWPLiXtEk-yETRAQ9I8cfsBjoOh-TotRGBq6LakxRhOYEDm4hiMyALKmYWa_DzNBDJ0pUyyi9U92hI00MlCZEEQEDaNeRzBPTAHB8tRJ153rqkEF-XqHmVn_MgVQk_s_L7ZPkIYgm1zhH20GYx4Yu8U_y1yH-kLFpCe7Rtk9KNLdyH9eTZyizcvN8TJO7xOpwzcbK7jv5PUnP1v_D7hJ2usKEeuWrWnhAma9a1ng_IXk6ptCtu8V5dmWg7pxBM8nKKwB44OQZPRbR1jlQk96cgEASkA2k5KWX62qLw5FiXs_YAtrguNguY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌دیدارها‌ی‌‌‌‌‌امروز؛ از جدال توپچی‌ها با یاران گرانیت‌ژاکا تانبرد رئال‌مادرید با رایو وایکانو در خانه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29638" target="_blank">📅 00:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29637">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fY4dUlb_KSNAiWvm_4cb0OmgucY0OG7SayuwViM65vNO2-6Le5FcAkoexNFDe6iq2i5IfyWui0cMk9GCEd39QU19kv_tJ2zj9_eXtnkgWQD56kauPqQpJWxauYe1ACRTTQPGTYgxKyNseHZVVYn6YHDPomNtxR-hUPtUsT7jpWV7fmWFdK2UbWFfrOm2oZ6KBjIW3exois2MfBF8YqheH6XClh7-i4lbfAlGNH3yrh42gpFWvtgzcgIr7x4eh9JhsGmiUxLVOlQM6xBrpl7OAGElIAWQ0H26Svyc2NNOyPzU4Segzl8OFQnLJATlF9aP_ecQ5XGoQHubdTcGS4Yj6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لالیگا|شماتیک ترکیب رئال مادرید برای بازی با رایووایکانو؛ ساعت 22:30؛ آقای خاص بالاخره‌خرید140میلیون‌یورویی پرز رو فیکس کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/29637" target="_blank">📅 00:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29636">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n51mOx9_5TUNlF-PncPzirsVNaSdweuuaAWkrdb-HAti26mDAGkwNb-aAYil632HbyZJj7DQ5yOjtnk7XQugWRlXWdMnXOORSwC48wRq9janibXgwxXCOdNuwpKncQiAg30ELn679OjsrcbUTB83pbDo1Z82-JsRkX4OtIlg2LshY0ZwmiMFzTzxFP-jeJCNwpJzOU0uZPCDoZQ-1uwGlr283i0qw-5cPUzIRY3qEV_RWBEWX3EsFyyKlEh04sInjUsMJQyBtbJ8Pr_oQ5L1poDa3M4hW0hKGJrAl7mxw8SjCnBaIxu8ZRlPK2BYr7aM4_5ymfb571NmyDwMA2Ed4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
حضورپارتنر وینیسیوس‌جونیور در ورزشگاه سانتیاگو برنابئو در بازی امشب رئال مادرید مقابل رایووایکانو؛ نیمه اول رئال سه هیچ بازی رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/29636" target="_blank">📅 00:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29635">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iP0gvIOiclpUP4Uh1Qa3-xPSwB7NaoRqjFxjwepdlTB74npwAgL_jtMpJin8MKy4U684S1g8kmAR68ZiV2Lao_rrtDmGMKzSHhV_jOpD_J_f0cV3aex5f1IRUslGnBOdfI-ZiCAJRLRw4mKLfzazsvgK-aGWnM83vUj8wTSPBLeWMzvoV2aEhKSort9bhMswbSGXICIsmzaA_Vndmtpnjiu8v45g1pxazHlfvO7LCv6dY30p5koFlSot_a2L-DNXwnEu1nbLMP2ZYmmbsX2O6Q-u-bwk4PGZA4Fyks3dWr-2YWopgQcU_ugV04lFBaaY4qQzecfPpM0UGjr4FUDhsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
تایید شد؛ بااعلام‌رسمی باشگاه استقلال و با موافقت سهراب بختیتاری زاده صالح حردانی مدافع راست‌آبی‌ها به‌تمرینات‌ این‌تیم برگشت و در بازی روز دوشنبه با السد در لیست آبی‌‌ها قرار خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/29635" target="_blank">📅 00:01 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29633">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-H7LBmrsEI0rV7VepO0o70i56YPsEn6nFvBUhFv3sg5fvc2vpGgZpei4YTTvT_YuAJekpUMqemZTq7t763_Y4bhZgyRn05fI7D_XFM6AyV58a1psRAtv35btQx6tkVrQ-oARyUlAbQ1AJxBCOyKZpIU8ANRee5Gj_OxwmICuJQhELP0X9ckt55Eyz1FTCQYKQ8rHDUiTLt5XZNScS9xuPPwLZ_eL1W-DgMrWnziqGMcvnT8O0Bg6VpyDcbLzTDb3spqe5ipgVLZEn5NrsG4Y1hZkDjVI2FaQPzUmWrTna8ThW2Ri8fMGX8LpUqon2j3FX9d8JCAb7fRE7vCf6pncA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛قیمت‌پلی‌استیشن 5 پرو دربازار به 310 میلیون تومان رسید. بهمن ماه 45 میلیون تومان بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/29633" target="_blank">📅 23:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29632">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5RXlwlgdVev4cB1Fui4yaEo_PAXkK_vKstcvc7BmNMsuY5oBy-gJqL5j57NrS7e16pZB7Y-AW2uWdfhNCFWVQV4u2cwaB3c2AR3iZGzZqdhKHezLqz3e1tLokwaDHjNBbQn6wwX59lxzsGFBVQqAGbgVPx-o2TNKEE-IclGwShxUTlNmfdpyyc8CrBxQHN4CZKoBRp1vaTpn5EzgbVvSt-vTV59AbB04vjHCec5XTwuo2U1WXLuCwxoQtvdoD5dzRyfynQrfPGaUpPYlVtCkbh9bxanaACW8YM8bXPTBOsujWohb3OK4kWdYKLKhGRTJ63z3V-eyYg5l9c4R7Mq0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
بااعلام فابریزیو رومانو؛ مارسلو بروزویچ ستاره کروات سابق النصر با عقدقراردادی دو ساله به ارزش 12 میلیون‌یورو دستمزدخالص به السد قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/29632" target="_blank">📅 23:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29630">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XAfoNrnYtv-THiKe7vA9RHA-s9z4-dfap-yrO6S6DExvY6sy7V0iKETjFD6PcOaRv0osoCEnJvXjusU6tXJJurPmIoqe222fBvtgluKZCafRrK-_fWzgnOVoOGs9n5bTFVrmxiS2xsDkXHiVP_mrILckfiC-TVr2cBK5Z9OHUp_76IKJQdwBRYhUh9i1I3TIRNxhn-QpSGlTLSlcVf1gxCX41zG3cWxFQb-O1YYONs3QolFtY_7gCvzuuWpi42_HQPDKEObzRo3UVXQar1G19hvD0CjX54t-H6Jt_vAPTzLJy4-K-xkyyo8DFEgtzfMf6nmuRfEWlF7MjHUJQqoiiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لالیگا|شماتیک ترکیب رئال مادرید برای بازی با رایووایکانو؛ ساعت 22:30؛ آقای خاص بالاخره‌خرید140میلیون‌یورویی پرز رو فیکس کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/29630" target="_blank">📅 23:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29629">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SSlYr8E7DPndUnSww1fttYjyKLXDAHL2uXEuaWTqedD0GSBALiuJFghjkqkbw_AiE2XsBsr8ARStZLKrKx1YOj8hqz-T_vQqH7EAqLypB_6wp5JBfYd1CUsR-GrRkHTuZdGtAlFOUzI-ElepCvnH4tmp7-xbBi1hdP03vbku-s7aiye_bwSDUuNSBrDYnvL1TR8wHQJ6Yo47lZ0CiGNa4MaS-RyAVl_3Mgn7YnnMJR5CbOJnqU2x58G5RLzntUuIqZUp45kOxzZo0FJUgOwd5LR7NBcHWcQzAmXvsuYvQ2Xrf05um_xY6KZ-9kkEwmx0FQ8EKcfzod0iPPFQM11fmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛طبق‌جدیدترین‌شنیده‌های پرشیانا؛ باشگاه‌پرسپولیس بامدیریت‌باشگاه فولاد برسر انتقال ابوالفضل‌رزاق‌پور به‌جمع شاگردان مهدی‌تارتار در نیم فصل به توافق رسیده‌اند و سرخ‌ها با پرداخت 150 میلیارد تومان رضایت نامه این بازیکن رو میگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/29629" target="_blank">📅 23:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29628">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVxrI9P_6Mk_I6q7u4_g7BS7C0xiHNRSWzA_VsnQuXu96_uLPtCqmfNKuMFMA2si5CP4zrnUy57GcP74GT3BYbKzwr4d0ZzxU3BcNRN4iNAn7DxOeF2gLcDNq-hmD9nJQU1f4mErW5WfDlB0yOamBCT9GCL2IrIr5q7RIF5o3GGK7KRVqLIo4IWSuYR9Ze9qpkosZC1xhQI4XjAWlewP7ESA-fqUJhyW2jE8V2qpfhWcVaXzMg5mPsWHhT3SsyqAgSv6ZHgfZ1mHf3bbERW4jr8YFuRxlzDEZIyURm0SKbL-yehNqD3HE4rcHw9Rqd6FZgzkIQCPoSAub2WguJFLDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست‌جدیدی‌ازبهترین‌برنامه‌های‌هوش مصنوعی برای تولیدمحتوای خفن در اینستاگرام؛ این پست رو یجایی ذخیره کنید به‌کارتون‌میاد و برای دوستانتون هم بفرستید که اونا هم ازش استفاده کنند. عالیه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/29628" target="_blank">📅 22:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29627">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPK83m_ExbW4o6Far2_mXFmfFKtYg_fr7tK4MX7bMi_DM__LE4YgbTkx6bF3VO1_Qqmxkm0ILiLad5qhF5yBj1f6pIah2nS2QLAO1bnDoJbM0nZhPRmAgE8P3-PScDS-JWk8lGNXVAHjNAnX61uEqBXiR3oh6WZ605IXzbcSW0DTETJFZabvg7OS6yTsGdhReN3AUQi4JPQOlvC44sKgicleW1J_Np58-5-nsZPf39vQYWJknmigfj1JXANQNzYoZkiLXNmIO9Sz9BJb0S3UBQf--auJeKtkLlVOBmN1ceE7S2z6j4AdOJSAetCOPWJjO35VD6bI1DKc6qN4r03B0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخبار دریافتی پرشیانا؛ باشگاه پرسپولیس بزودی با پرداخت 250 هزار دلار به دنیل گرا مدافع راست 33 ساله این تیم توافقی قراردادش رو فسخ خواهد کرد و گرا از جمع سرخپوشان جدا میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/29627" target="_blank">📅 22:28 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29626">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKG_5yacfKVv1Hlhl4aFoNMNEXEF80rkOn0-LO1Em5DBRtD1VQNN36x1DcZ_n2scDuKFQmhKmSVg_giAG5bJzUH5reMvSOUkVmfgoLZxCzeNOPVaN5yV4OLTPgK5fDZXT7-gYxFzScAOjZ53FyBcqBmTIr1JdN4GYSJnW_Fy_GkVE6Kl42ylenbIj_QV3fqwKf-SLnO1XOBjFBHK9o4NSnRH3UTqZ2xKKNsKlDdBSU9AnkON2pAPlrchMfsk55GIBg3W8S3HjAbKZKTLqp9rxYWkKFVB8J05D715TyI_pdjTjFP577eJpG6q88BRDMDSTZ1TckTvTnmaeSw1nD34aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔴
طبق شنیده‌ های رسانه پرشیانا؛ بشار رسن هافبک عراقی پاختاکور که‌اواخر آذر قراردادش با این تیم به پایان میرسه از طریق دوستانی نزدیک خود به باشگاه پرسپولیس اعلام کرده حاضرست نیم فصل به پرسپولیس برگردد. طبق‌پیگیری‌های پرشیانا؛ مدیریت باشگاه پرسپولیس اماده عقد…</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/29626" target="_blank">📅 22:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29625">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2989e9b119.mp4?token=QA8Spc7NYjetkskizJ-QKYkzjPAmghQrN5-znITCU1rbjVbLNOkry_Rux2YSCwGQvdMqDNSVcaEjaxMAL3uDTZ0XK_SFhGmc4iotAsSNjOfp_m9B7F7cEr1DYWUa_WntSU3YEXHovjV9hUFYf7FUb42E87wU8wmGaz3oTHkhzHjbPnMmLL3eU0eIXlGYQ3CvsxQzAdIK2SNX1qHlWegfNAf1hQ7dUL1hIHYW0I29Ik43zd4pb4Qa9DDlNFmIbZeGI33lgkcGrgJZKCC-z83lwuTgCECSNbXet3xg5d1b2Yb6JdO52zhEycdFARaeJc4DxwVRVbGcrzEGI4zdrPQSGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2989e9b119.mp4?token=QA8Spc7NYjetkskizJ-QKYkzjPAmghQrN5-znITCU1rbjVbLNOkry_Rux2YSCwGQvdMqDNSVcaEjaxMAL3uDTZ0XK_SFhGmc4iotAsSNjOfp_m9B7F7cEr1DYWUa_WntSU3YEXHovjV9hUFYf7FUb42E87wU8wmGaz3oTHkhzHjbPnMmLL3eU0eIXlGYQ3CvsxQzAdIK2SNX1qHlWegfNAf1hQ7dUL1hIHYW0I29Ik43zd4pb4Qa9DDlNFmIbZeGI33lgkcGrgJZKCC-z83lwuTgCECSNbXet3xg5d1b2Yb6JdO52zhEycdFARaeJc4DxwVRVbGcrzEGI4zdrPQSGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمد نوری استاد جملات قصار! شاهکار جدید ایشون درنشست‌خبری قبل از بازی فردا با سپاهان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/persiana_Soccer/29625" target="_blank">📅 22:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29624">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-3TtXc0pDLi5HMscXL88PgvtFOmqiO2IezLB5bJj7iI9pLqzREBro4IbA30LXth_j73pK1rAq0wkOG-2RGnz_DiMR7NB-2KWVEJusOFjKxc89KKpdaCsAiTlO2CDJChZV2XUJhtouQuYcOZaIujuvcnIciaFzNEjlWIb-pyNXVWby8aEHdxIrYj8x099P8Fykmhju9U9r0OAAtVyR97S5EnSv6Ev1WwXnIit3rH_H0ZlY5Ytu_vE3vSoHWvV-7YMpv2beYrdtE15RQh4Yb8Yi-8OwzHdovDI99Y2wcNkpy4tXvn5GEG_cZXADemyvrcHcu2EmhsSymdDv8QlOWSpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔴
طبق شنیده‌ های رسانه پرشیانا؛
بشار رسن هافبک عراقی پاختاکور که‌اواخر آذر قراردادش با این تیم به پایان میرسه از طریق دوستانی نزدیک خود به باشگاه پرسپولیس اعلام کرده حاضرست نیم فصل به پرسپولیس برگردد. طبق‌پیگیری‌های پرشیانا؛ مدیریت باشگاه پرسپولیس اماده عقد قرارداد با این ستاره 29 ساله تیم‌ملی‌عراقه و درصورت تاییدیه‌مهدی‌تارتار این هافبک تهاجمی خلاق به پرسپولیس باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/persiana_Soccer/29624" target="_blank">📅 21:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29623">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJqdUn8-CDHgPWUvrenM5Vo9T_SNozxqHa1bf-3DlRXCdtHv3tGjEW1r4SpF5fjp4M1_KRLXoM6WeEOXswngJKm3jKxnEDif6viTPrmHj-1MMdD2JUwEEc4FdesinHT1JwOYigZ9C8YHjvGJinO2tzm5ipjmfi6In6T0r8v7XKx6uRLejVFK7FOApDVM4AkOgxv-GkCjE72K4lnv_hAXx3D0qN4kZJxEHvXDUUk9-vnTb9eqM1-38O8Ipkfosr3MepO3aXKAHMz3tJmPfzjbo7wKyPeblCMg8BlvKJW2btHXbDUjbVP6uDvvxgaO7ARu2e_JAMCEVBVaoFKGu5Y2Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
گواردیولاسرمربی‌سابق‌منچسترسیتی:
برای تموم تیم‌ ها در چمپیونزلیگ برنامه داشتم اما هرگز ندونستم چطور رئال رو مدیریت و کنترل کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/persiana_Soccer/29623" target="_blank">📅 21:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29621">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxr2Yjf-sl921UvMNWCPXdT-u3zGhb5avwKl9LEvr3kN9_x34y3dpxG96IDUFhFeWIUUb3fXlKHSA6Zm3OpPsK6odGvdzfbgZ5EjuDkl_pzzVzRQSydHc12Kv30OE06PeTECjl5QiJoOGNsoGE4VdxJQHC1eUvtd1-GBgZpAErbRHuEi2GB5dtVqt3murbjpYNRP461W7kQke4NHQ48q6cW-7BTHXboDUulZAZtD0uC7JGcCpZ-XW9-E8q4Hs4jsSls3w8RbH3U2d-__4cLCMASDUNAfS5S4yWvtABVEblwDunhtAel1EV0QaN3nXUXOUtHRTm4_apO6IhDnrwEH6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قیمت‌امروز انواع پلی‌استیشن 5 با دلار امروز که حدود 223هزارتومان‌بود؛همین کنسول یه هفته پیش 190 200 میلیون تومان بود! قیمت‌ها عالیه واقعا:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/29621" target="_blank">📅 21:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29620">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPxbh42Fh4iYOR2VEQR2PuL9eYFhp8FlTid1SAkUxoesnS-ERh6F5ALc-FkAmhrZMjL7syaCD8gzqRMJUj7Y7nXBNauuVx1oC9TykJdGj7kh2jnAUH7cNdqLJgeWRde8s2ee5ViPT-PMyl56h4-Q9j1EMfpSL49wnhI8aznbjlKfzfXfHYcVUL7Z6GmRYem0Gg4kfQusZY9X9HjRxzr4zGu8XoxhSOZ3Ti3JPo_eln6Ix7P8H88k7QQQ3uTQx6uWg1L1TDo9Ty68bJdaOgsKCt-uXVHm4E1hUtaqO5l55IZOYSAipvuz5ap5huACHV-m2n5vg9ABLhjuZsmFEMu68g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لالیگا
|شماتیک ترکیب رئال مادرید برای بازی با رایووایکانو؛ ساعت 22:30؛ آقای خاص بالاخره‌خرید140میلیون‌یورویی پرز رو فیکس کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/29620" target="_blank">📅 21:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29619">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4VcACAeifbBzqi8lbe5VP5sgL_RCaHTT0cRj--EJuDdY4kyKcxKyh04IeTSObeARZbhMkrcF-KS4WMeyPj06-0MUEcvAmsc69T98CaKsZ0zwj_vVrEMj-nYdD8gLMyjGbooAeFTmpKg5V_SQx9rFBYtW5TVtypnEsNl8akeuhtRVIb7e8-I-89-q2EqicwGfXXD1Jp9eFngtI5I2efh7bY7r4gd6kOpQ9INkrjf0fMpP0dGvM6g53mADYjzoZKqcTUISiCJVbz3ONE8aNmw7bS6gi3tGKEPr7lelO_hwH8dR20HLpoXiYyGVpHBWK8v9toxoCUIj-HYQqo8V7eBSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وقتی‌میگن‌فوتبال‌غیرقابل‌پیش‌بینیه یعنی این؛ الهلال اینزاگی امشب با تموم ستاره های گرانقیمتش همچون مارتینلی و واتکینز اونم در خونه دو بر صفر به‌تیم نئوم باخت. حتی نتونستن به‌این‌تیم گل بزنند. نئوم تا پایان هفته ششم  دومسابقه‌باخته‌بود و چهار گلم خورده بود…</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/29619" target="_blank">📅 21:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29617">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CcGkBK87aBgv7GIkyoeXYmiOsNQ8RegqCpIDVoTXpzH9ithPSbzEnE3xMuAYuTWExV5tfxiBAXtPMl9380mH8vSr9Nd9eB63bIXu9GYb2tsHX_5Oug6_ZQZxDB1gtf8tqWuNViqsCaHu0HrED7Bjpitua18vegvDnBcwp7sGN2onRAweZev28xkkbIkr7jBeSsbNOAFspsY-DfUhZ_RcQgnSPwwnkXLEyXvBR9rUPHcEF0uHLXXPvVli8rKt7h5yYyyPBEfT1ntHIo2ptwGCaD_fQksnxgHEIDYTzM4E5PUmDIMhLG769xOBkVJO486LdHyuCrnvSzwGf2GWIv3fyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عملکرد مثلث هجومى السد حریف پس فرداشب استقلال درچهارهفته‌ابتدایی لیگ ستارگان قطر: اكرم عفيف: پنج گل، چهار پاس گل؛ روبرتو فيرمينو: چهار گل، دو پاس گل؛ کلودینیهو: سه گل یک پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/29617" target="_blank">📅 20:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29616">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6YgfD6OeVbO0nvQLayLXZ-nJGMVd0zk2JifzO6Fw32qP3yx_OFpg3YiXkU1mjlId3m-YmGlTGA4ciOwaBRxRTHtbIchNii6ffFlbyItgicm6kjPOm2MPHnfi0FhhY-oHbs3YoBF7pCBIybTlbRY39R2tHq_KMSg3tURbedX-o3tRkfDu_u1l0V8jfv-AbxLkZbDK2nV5opJONDm9_qKSqPZi5Tu0JdduO-0sVsKTx_4W9lV40AgGVlDXKIjeD7VTszUMm_Bj7ViRxsN-0SevEAUY6OstUPRJ5fL8F-fMfXpB-gjLhbPAnvMMju1fpo7nQN8IdvybLoa7d7AsWMALg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عملکرد مثلث هجومى السد حریف پس فرداشب استقلال درچهارهفته‌ابتدایی لیگ ستارگان قطر: اكرم عفيف: پنج گل، چهار پاس گل؛ روبرتو فيرمينو: چهار گل، دو پاس گل؛ کلودینیهو: سه گل یک پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/29616" target="_blank">📅 20:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29615">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6942e2257c.mp4?token=jUoqyUmLoehumPWbeAVJ1bX56dQjNnabkszQ7Ot6p5MIPaJUTwHWVlOnXqKKQyAvLKYAddSwnlzci4nvjU8P0RPCrhDY7tKRHxF5wfhxrzWrnhbmMwqfu2Z4czSUted66bz7qVVlnE3rb2gZNc7_9mPWKRwmWEEmGSVMcV1x4mQpmSP8k5QEiHi_yHg878swHSxoa1DXW2VyoKZkMmbo2QKIwtEa4eQGvdbyeayCTO0H4Y5YmWfqWxaz86tVX7DY1uSDGPjqYkTN2zpLKFAgZusUW4EfGZhB0KCzS4t4DQpJcim_-edbLI8RjyioWGKmpN3ptSOdsW1fG872uvZsyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6942e2257c.mp4?token=jUoqyUmLoehumPWbeAVJ1bX56dQjNnabkszQ7Ot6p5MIPaJUTwHWVlOnXqKKQyAvLKYAddSwnlzci4nvjU8P0RPCrhDY7tKRHxF5wfhxrzWrnhbmMwqfu2Z4czSUted66bz7qVVlnE3rb2gZNc7_9mPWKRwmWEEmGSVMcV1x4mQpmSP8k5QEiHi_yHg878swHSxoa1DXW2VyoKZkMmbo2QKIwtEa4eQGvdbyeayCTO0H4Y5YmWfqWxaz86tVX7DY1uSDGPjqYkTN2zpLKFAgZusUW4EfGZhB0KCzS4t4DQpJcim_-edbLI8RjyioWGKmpN3ptSOdsW1fG872uvZsyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
گردوخاک اللهیار دراروپا؛ گلزنی دوباره اللهیار صیادمنش ستاره 24 ساله لخ پوزنان در بازی امشب.  عملکرد فوق‌العاده صیادمنش در فصل جدید برای لخ پوزنان لهستان: 6 مسابقه، 5 گل زده، 2 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/29615" target="_blank">📅 20:09 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29613">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h2nZbwHM6slq496ODLnRtC1i6kn2oltBypKGU_ojJZBTVk7zVQ7A0U1gFtBdxMkRGfkZjq-5uHMBuZUAeYgSLNL0_OGEzD3BGwlRvVVd8WnyIU_TEpJpCy8f2wxg06ssBt668v0LaAMr4lde0W2ST5V932I8LKbuU9IgHyHMTJcY90hi4obpkEpeQNTPJVqherq53UHtrETWUMIEsL0i7zBuQg8e9GCk17XJcXlQFoB8V3yehNF_FHqUTruQybOUIT8Wo30FYFZBesRV1Sgex9p7VgmeKd05YR41qY7zHts6J71u8sDUUZnnFmGXz1zJ3aSUdZLmHwqMXDCF5fuhKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xa_juyaVNjrV9M30PpeZZerYMwUYd1dWDPxsXE-XUVLReviGcnr4QFPDaplF2tFGprbCFBIEn6_NglChfrJOXxKC5-M5P14m1oePhC9PbMiQIRF-QC5XYTxQ5O9daaIVmurORjzh85lH5xqCvqs4bKx0E0S2vjHtI4f2-jy-LKjbJ0vwH0f6CbN1BXB-x4GpA86aB--nDXzgc6Y0j7AlHYB-YPnKPNwsicgOAFuhWoTdcmDOqxa4shQUWVY1cTsud1vXAAjHyBp6f7c9zdlOMdZlK55HmkQRc5nsW0ny2KhNyPLSjdyr2hyAvKaj2BuAh0EfYj_UITBIaWzsAt3wDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
عملکرد مثلث هجومى السد حریف پس فرداشب استقلال درچهارهفته‌ابتدایی لیگ ستارگان قطر: اكرم عفيف: پنج گل، چهار پاس گل؛ روبرتو فيرمينو: چهار گل، دو پاس گل؛ کلودینیهو: سه گل یک پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/29613" target="_blank">📅 19:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29612">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‼️
سرگئی‌جاکیروویچ بوسنیایی رویادتونه‌که 3 سال پیش دریکقدمی‌عقدقرارداد بااستقلال قرار گرفته بود این‌فصل سرمربی هال‌سیتی شد و این ماه نیز بعنوان بهترین سرمربی ماه لیگ برتر انگلیس انتخاب شد.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکرد هال سیتی در فصل جدید: سه مسابقه، دو پیروزی، 1 مساوی،…</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/29612" target="_blank">📅 19:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29611">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g13Ga40lXZCLn2OR6Ibl145NYbVqzDwUPHF6bCDxA24ydJrBd4f59VotW92ridgGTcHHOIquPMe0iSxd9ct-FavJFUrcbWr8OsTUfCC-G6YImRlIIiV62vCeCE9ie0t27H7ROyOE-FMVMwg4O_0trfyb-rn98HiUVtErWg41aoFCEv1EM2ryIdQZxvl5MlUk_yzwUkW6YVTrVxWqNeaNmzIh7tSeMluLP8M_kn63XkxMJERguQi9wgpXXTAiV7LT66QTJahBeMWUCNC1sTsBBcxFYwjy4fh0NjyMBMD6aRAaFNh9c07qSSVVICZzNMppfsv21LfZJhz4Y0TCUTEwkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فرصت سوزی برگ ریزون لوئیس واسکز مهاجم بیرمنگام در بازی امروز این تیم در چمپیونشیب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/29611" target="_blank">📅 19:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29609">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCmk8P_KRXsj-FSgyI1kxwnICF5BrmviOm-Lry4HEZHlrCyGUwqF-OfRXbiwX2DlkTZ9-wIbGj_QXZhrMHZURqd8LO1AkSFn5TC2i1Q4WZcKsn26Xp2u2-il8OvVbVFAnCPpMLc_DU-Dv5CL1ZB7QSW4VrkxDTE8Voe3Ei8fxFDZFGrEVIx6R-a-z1KUdvGy5IUbeWCvx_rm5bu1WAuuNazYSO2X6YJ8lUg7pEoKWFM1bs1awwIdtA4e2wQ5iY28RKiIiuJnwO2yK5HIupl0vLHTyM586RqqCjpv4ZTN1DukIoS2_D3EBGXYWGILGuL_KhEz41e0e0ndGNBRm7cFzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
نگاهی به آمار خیره کننده مهدی طارمی ستاره 34 ساله الوصل امارات در دوران حضور در پورتو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/29609" target="_blank">📅 18:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29608">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1z62n9WZTrxbappVrnNt4HN-gVBXfgwRgEAe3yn0SOUbrZoAQjLpji4OnwD-1k7Z4RIrbpIzinQCVsiZVfh6BQuAQFEc_xChNaf85r6t-IUpDjXIlLC6XD4wMKsIiuhB-NltROQ-VHLB9_E7yuTrbhCvsJzRVU-CYUxtGd1rl8ZcwBB8B1DrPy-_MCjhsT539CkY9Q_YJKOj5dJzQ6JfdfirYeef5cz5tVusKtLzlbr0V8foK_fa0Gf_70b900jPaa3O7V521-MQgPhjRYmcSfLM_eiaQ0DQzJ8aIzZZtcv3fX3vmwIEv5xfZUdEVNA1AQWaerirFEeF01xwNuAvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ AS: میکل‌آرتتا اگه تصمیم گرفته باشه در آینده‌راهی بارسابشه فلورنتینو پرز سسک فابرگاس رو راضی خواهد کرد تا به‌‌تیم رئال مادرید بپیوندد اما اولویت اصلی پرز اوردن آرتتا به سانتیاگو برنابئوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/29608" target="_blank">📅 18:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29607">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇦🇷
ویدیویی‌فوق‌العاده‌ازکاشته‌های لیونل مسی فوق ستاره سابق بارسلونا و تیم آرزانتین درمستطیل سبز
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/29607" target="_blank">📅 17:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29606">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ovO3_b-pT1xQmiX_mYs2HN88qkyBQ126bBUHErO9e3ZfUf9NTYJI--7TV76NKxf58TZ-AmKmC8DKt9-1n0FiOmLWiRHAtRUotBAcU3rXkiSmUP7-sAiIAmrpQwHGgwD53_-VPt2ZfyD2ZBU5x5VbXZ_cwCh-DyJ2I0AlMek0-YjMmhKthZjhyclcZoCwseF0M1QZFrPAb3R4V6B7sJKvOOlcJ5p-RLTHUITT3oRAMpIkiUbcyXjBLVU3n5H4Q8gy-UrwaZGSl757nLDWzocLxU1FXI93_2Rs2DQnrlxeeLjg5NNgSzKoF30w-V5z1n1NQSNigEYi0glFRANvlQn1rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
پرواز تماشایی برای گل شماره 979؛ گلزنی دیدنی کریس رونالدو 41 ساله در بازی امشب النصر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/29606" target="_blank">📅 17:42 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29605">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9RcadweXCdrnETrhN22vOpJtICruavHGoR29cpYd-0vwrDDqhYeKvXhfZFclGwGO3iYSQxysJYrqU7rD32dKQ6xeF7Yn3ZqMkH0sOaOIRl_zzDpGGQb4e-q_xBshuaYVqraSBkZKpb8hKG3m2oVonwbvdj8h94KWlDngMj287BL47CnoTUewm3Vf5RbYnKVHh8kxs61Yda04c9CO4fNhkIxi6SGWcXhAluxPy_PVcNgJHynSy6CiFKoJgz-gtn6cbW6k8n_mpOca9VLt9YP9aheIK9UF-Hwo4C7tqbAjlmgbFP4IPOSdA6IMIxm4rYBFmec63zkL6PSoSK_zY29JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔴
برگاتون بریزه؛ طبق آخرین اخبار دریافتی رسانه پرشیانا؛ مدیران باشگاه سپاهان امروز صبح به‌مدیریت تراکتور گفته برای صادرکردن رضایت نامه آرش رضاوند علاوه‌بر تومیسلاو اشترکالی 50 میلیارد تومان هم بایدپرداخت‌کنند تا رضاوند تراکتوری شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/29605" target="_blank">📅 17:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29604">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSbFKFBpis9_I1tEk_IUE6P6YcARosuTCYLkFwx62p0fTYm_nRwB-ILywwx5h1i9rydL2Sy0g-ysrPwrNTPum1g6sbY6RSIZWXMWx_BAC2TkuRQ18B_Cx1atmFXHlN-_7IdPFbeH4twPb1JkgZBBiarQiHbZjKK69E1oOQZlmo5KDV_h1JsRt8uwOVX1K-NOAX6_zqxLHjVwvfkXKcTxQwxektJaXqdfRm2paL9VC-ef4rb11My6vRJaauCFB_0hvrVKLkYPwyRSf7oO2l_ZaN4jchHTo5sb1zRN-3rdnJfpuZil_0v4m2QBEVFmr4JQKFyWEykXvAbQp2b5Xk0Epg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
با برطرف شدن موانع موجود، کاروان تیم فوتبال استقلال تاساعاتی‌دیگربرای دیدار فوق العاده حساس مقابل السد در لیگ نخبگان آسیا، به طور مستقیم از فرودگاه مهرآباد تهران عازم بصره خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/29604" target="_blank">📅 16:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29603">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTnGVNyeLRcec-MyBL9ZPFmaYK5ovEXHCDt5YFua_0vGEQDq-kiw_zhq9olraMJWyMd4YcjCbK-Z0L0H8f7YXEgRDXl32COx4jIifKgMs5GBqx-nRF1WcdUnKEMBK-KHwbr0rSM2YZUg6ixodQAgpqaFNKBfTyiIeqiyRTERKNI3O6SBfDcQ9ev5Zk2E-eBzypgRe9xa_Ae6otWPpMGWTU3JC7oDnaJR651Fjz0Y8dW2n3AIoHBO3BdYlOKa48b68pekqlUSZzGnqEkNGKvYeirOycHZK3BsowUanf99UxKIauSZB0Txrr6fxvrELD8AxumvWGbgk2y3MUEq-C8-wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مقایسه‌کامل‌ودقیق دو سری آیفون 17 پرومکس با آیفون 18 پرومکس که دیشب ازش رونمایی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/29603" target="_blank">📅 16:23 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29602">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abe26c296f.mp4?token=L2yiZ0eX6vUI2bRIOBwjs-GYrvexSFl3FMvprySb0mxeMwr_Gg8RczqG5DMFLPRdZ8b2OWqiLVJZNaGf0HrNG7NQAq8LHEiAQuR0VCYcntHM4QSJTo-QqPIOg4yfJYA2OkeiyZ71GpZJI2vzWMVii5ScZL2YFT2y0d0vuValEMYaw7vEE0KyP9EcNQPeCbjiIl9WTh3bE_A9-ifwx4lZsH8-lyalfA5J_735n5ikI21Tq-bpHMeYU0ptki5DsAE_Z0Zsjc3MfHvt2qKAvS7s8nSLdhg5frGSzfXrZz30jY-VN1eUoIFqXi7phmaxDCIFmJFgU0zpOxsDNblbzjSX2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abe26c296f.mp4?token=L2yiZ0eX6vUI2bRIOBwjs-GYrvexSFl3FMvprySb0mxeMwr_Gg8RczqG5DMFLPRdZ8b2OWqiLVJZNaGf0HrNG7NQAq8LHEiAQuR0VCYcntHM4QSJTo-QqPIOg4yfJYA2OkeiyZ71GpZJI2vzWMVii5ScZL2YFT2y0d0vuValEMYaw7vEE0KyP9EcNQPeCbjiIl9WTh3bE_A9-ifwx4lZsH8-lyalfA5J_735n5ikI21Tq-bpHMeYU0ptki5DsAE_Z0Zsjc3MfHvt2qKAvS7s8nSLdhg5frGSzfXrZz30jY-VN1eUoIFqXi7phmaxDCIFmJFgU0zpOxsDNblbzjSX2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ویدیویی‌از اولین‌پنالتی تاریخ فوتبال که کلا 0.2 ثانیه توپ تو دروازه‌بود. دربازی این هفته لیگ MLS به این شکل که مشاهده میکنید بدون اینکه توپ به تور، تیرک یا دروازه‌بان برخوردی کنه گل میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/29602" target="_blank">📅 16:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29601">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_k8c2tSGIwy3mD0GKPPALJ6s8LHb80k-jswfmxEe8BeGiyXYaGmg2Lj8XiKgjKZxrhMeA6ngrT_aQKoBJjkI9pYkapzm_uTw0a0x0weMxiLD2XrpmlAnqgznkUqdYFV-Hw6pIKyr9VJx_1FuVsJ32X7DfSfbwmrtGAo9662kOr2jgPtCAQfF-g9Et48TIacZeoMyzhR6Huo4Ps8XRgchPxuFYYlzDyFI1i2BBmQX-1cGNEw42ddAGHoED9AUXefIHQZx40Mah32iSVh54H88TLPh41_AQV9zfzDeRshzYQbWOKSZll_MLkOVKyCZivZ_m_5r3-AT2DW1Yu-LXVbCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یاسر آسانی ستاره‌آلبانیایی‌استقلال یک خونه 75 متری در غرب تهران برای تدارکاتچی آبی‌ها خرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/29601" target="_blank">📅 15:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29600">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ffHxC8lBG9zUjLh8q31d6GjeLhxJsATTpGi8Opct_Gz5l9mjVz_UqOXH087nzsOpkWOryZ-Zoin5qI8UqSOhC5q3bKHuVrhCzAvzWSV3vcF8uwgJeVOeHwVuazXvtgR_nvN-8fX21iT06XI60Qg_coPXfnfRxoIvsRMrQRkacfS0pGV7oxlyT-BBVi4rj0xvwtm45b6nVNM7_hO6vaPGuq_sHB_rAAc92Lw3u3gzfZMaKE_SJ0GbZjUAsTFJfdFGM9VonX5RjXicqrxQTH3iNLSl6SSQZdCFOpNknI7BfUpLeyISK6squwd0nUphzXl_wdGpK8OumWFFHeuDRIFI_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌ پرشیانا؛ باتاییدیه کادرفنی؛ سردار آزمون مهاجم 31 ساله شباب الاهلی برای جام ملت‌های آسیا 2027 که قراره در دیماه برگزاربشه بار دیگر به جمع شاگردان امیر قلعه نویی دعوت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/29600" target="_blank">📅 15:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29599">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKXb8m14ya8nFLaCbnBaVHfEgr78LMFnEKRVBdKlFocRytrPYEd2bn-un7u6wup0uA4ZruPg02bXqMzkqNQ5GYdVs7nCFiwg4d5GuuFOtSYh1xAwAf6xELgSwD8i6uB4EeSVcw_kdrbr1Qik2eW4tp5UNIp_hAmSkfuP2j4i7enGgTMyMHwtGwsGmIHhDQVQzQmmn0EPUyN3JB5_jUymXQF9PrFs3ph-mlDsluDdKa8gFHg3aI0glpg7Cc4UmGEpzI_ctKU0xW1AOsdo--kerIn0rRN-rezElWn-mzpaw3TDBwdwyghG9WFFeB9kfbYZKXc5eudMsmQkYo_GIRCVfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ بارسا در لیگ قهرمانان اروپا؛ رافینیا و فرصت تبدیل شدن به بهترین گلزن تاریخ بارسا در چمپیونزلیگ، بعد از لئو مسی افسانه‌ای.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/29599" target="_blank">📅 15:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29597">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be2a23445f.mp4?token=u-61c0t0lsMElKe7CUboyOjdW7ttuee_2R3MPVe0I4xbODZ6nHufZEpa9GpkQO_kfNwYhDUyYKYAvq7fXWIbiGD4S-SWum0ZzLPWSiqshGIXOGI7lqnq1JCDYsyrzQso8uU6mkXPQMLwgbOw46ctnKadSzG9S1D6w5yyoXBqJvG1SBT1NwBe9sgTT1Gf_beWEYzoliJkQ3_yXaqQ0-v6oAvnO1gEB1jKakYOC6McxcGj8XzmdnXKEnB_OmONbeZzzNV_9WpWzvNyhxWvnmGmfKjyHjnkRFI7UHhrO8U1LjH0Z4m97GUudHmn_626g1tr2s1KYqK9P11MVqzUvGp4vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be2a23445f.mp4?token=u-61c0t0lsMElKe7CUboyOjdW7ttuee_2R3MPVe0I4xbODZ6nHufZEpa9GpkQO_kfNwYhDUyYKYAvq7fXWIbiGD4S-SWum0ZzLPWSiqshGIXOGI7lqnq1JCDYsyrzQso8uU6mkXPQMLwgbOw46ctnKadSzG9S1D6w5yyoXBqJvG1SBT1NwBe9sgTT1Gf_beWEYzoliJkQ3_yXaqQ0-v6oAvnO1gEB1jKakYOC6McxcGj8XzmdnXKEnB_OmONbeZzzNV_9WpWzvNyhxWvnmGmfKjyHjnkRFI7UHhrO8U1LjH0Z4m97GUudHmn_626g1tr2s1KYqK9P11MVqzUvGp4vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
شاگردان پیاتزا بابرتری قاطع 3 بر 1 برابر استرالیا درنیمه‌نهایی جام ملت‌های آسیا به فینال این رقابت‌ها راه پیدا کرد و در فینال برای قهرمانی آسیا به مصاف برنده دیدار امروز ژاپن و کره جنوبی خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29597" target="_blank">📅 15:25 · 21 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
