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
<img src="https://cdn4.telesco.pe/file/A8WPC7gAut6xy59ZLtArD25Qw4AEDatkq3rpQtdtqlCa3_eDfajnOzWrdodnwMK_VJnIfUJq2zoxoNT2Fvb_Gh9LuvqjOw8sNhDnf4GWCxmqCX6UErs6SY-FZRr0NKrVLtSqf53Bi-FSOGtCk3JAqowTNqMXRZ2R_sVoamYjhJjRvW8-VECx4nZGHMP3ouM81jteSdRR2wWmzcWNKf0cx0Ia8c_uiNEGpbRevdJW9L9MKJP3FMA3BsCQRnIrEK9lenEt3Jx0vqb7QJqTPG9bb4rBchlca9jNYnkGPMy1INqX1lIBDP_4uqRzsKqVyEaAmWBIOaV7eLBuenFjERWdcQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 07:03:24</div>
<hr>

<div class="tg-post" id="msg-455611">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGtzEv14OgJMyAMtc82c00J1CSQzemxwyZsDHAOnEtrxuyfK3ZFJQA5C4k4YCNx8O4ISBanb38MsEuxt-Ug0IKRpYFE971c4l6pMl2KRBAgUvY8yRu4wtYdSWgzg_u93wx68DB3UkwOg2XzoHjawFvp1NCZ955ruxBVOG9l9OPbTdDe3PDYRVtiyHD32bRWfXaw3xXJEGxU5zO058muzDy7ioLAT1BbOYQsAoxvMzeJx3PPCuYl9D9u8QS8dVyVrg1BwqUfLPQ4oC5nOZM6v7nULXCj1fBM-jYG8zqNPRDVxQmuMzD4YEhKwk-_KFH_ZWb1OtQZiJrjFPgn5S1s8Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار سیلاب در حاشیه و بستر رودخانه‌های مازندران
🔹
مدیریت بحران مازندران با اشاره به هشدار سطح زرد هواشناسی اعلام کرد که خانواده‌ها از اسکان و توقف در حاشیه و بستر رودخانه‌ها و مسیرها خودداری کنند.
🔹
همچنین هواشناسی مازندران نیز از احتمال آب‌گرفتگی محلی، جاری شدن روان‌آب و پرآب شدن رودخانه‌ها در پی رگبار باران، وزش باد و رعدوبرق طی ساعات بعدازظهر و شب خبر داد.
🔹
طبق هشدار هواشناسی، کاهش دید، ریزش سنگ، اختلال در تردد و احتمال وقوع صاعقه از پیامدهای این سامانۀ ناپایدار است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 374 · <a href="https://t.me/farsna/455611" target="_blank">📅 07:01 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455610">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0rVTdfvMaam09q-4BwIbASB13rGawqqH9vqzgUdapsnwm8GnwJq1mrSlrqc3e-9rZs1OmzCibnjZ-yT40f18FljXrxDwVmyRYhq77SmjsPbRZ2gYJp_evjhHHMSyh5q17isIsPwoB-8lDmmkFz2BRIH-BfNvNNRSmdqaUG56IVXS9XMoSnpyBHLU_yUa6WNEzjrNNu73tL6pcJV7Scv1g-PGMYx1sdGSukc17psgK2h9qeChQVfcGBKU4WgNFQVQ2xN0zjWiEZgo-mfmyDS8UIDbocuSBirGg_gC0-jZhV96rZWg3w_dWMsxv-kTR12sD2i0i7xyjubG3-aCYlInA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مخفی‌شدن ترامپ در کامیون حمل غذا سوژه شد
🔹
گزارش‌ها دربارۀ خروج مخفیانۀ ترامپ از ترکیه و جابه‌جایی او با یک کامیون حمل غذا، موجی از شوخی‌های کاربران را در فضای مجازی به‌راه انداخته است.
🔹
روز هشتم ژوئیه (۱۸ خرداد)، پس از برگزاری اجلاس ناتو در ترکیه، رئیس‌جمهور…</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/farsna/455610" target="_blank">📅 05:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455609">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان
🔹
المیادین گزارش داد که مناطق مختلفی از جنوب لبنان هدف حملات هوایی و توپخانه‌ای ارتش رژیم صهیونیستی قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/farsna/455609" target="_blank">📅 05:44 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455608">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6hTXLOPZ4-fRTsB4lhxYnvQap-xOe1JAPezvYNFnHZZLL2_lsnc4fj1Wz943DoVy4qEvy1AU1b-kiV8tqWM0u8JjSOcgKKOMg0ifn8NYN6Ey-YDTVD7lzElH88TR0sTRU09_5FzajOHepKIANshNHSyJyzpr4smidN7fM7FCKF5583MJclntRuNOeHworFoTlwMMiZWLSTpf0_ob_qmmY6mN3jav9euNjDzCkQsA5kIEKiVx-or-SJ2NvJS3mehV1TXHK7K223dhvZu9KvUDwW3wJbwxbWnC1cIXdZfYB40_hVx3gOrQYMNmOFGN2UxbMlanBxq_SCBl0N4ZImDjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واشنگتن‌پست به نقل از پنتاگون:
بر اثر حملات آمریکا به یمن در سال ۲۰۲۵، حداقل ۱۵۰ غیرنظامی کشته و ۲۵۰ نفر زخمی شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/farsna/455608" target="_blank">📅 05:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455604">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C5ig_xLfdqazfqScuMnYuFNWVbrWdcPn1OLqawisDDPR0WnkAV4K-gdLouSuV1FHiLtae8D7OXNrUnqPsq5LgnqMCkpPVZPaXv2924RpzBrcOgOg3nZugDWC1FoTbHic-nqKp6Y1T197pRhSMEJtmBQnt408d829skpL79QCiNdwsqbfWg3pE-4sX0_tkcI-p6Qb3TwPfV4naMEfViNnJRfV3F5-jG34LpktyLxvnZQGqNPN8NwR2oKt4kyysQ87MrxlJAWVirEnz2NbLOAreIyvCOPwUfJ2mNb7H9Fm_dz8JEwuxlLfoNkUEwULuNbaG6SpCfJ3CvwZJcUcIXaznw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GUFhNEtofi_evHO94QkTnNwNqBL3V0leA2EYfNcIbhs2hxdM31W8l51WJnAT0uzb6u2-fUzjasev1sa8uXJp47DlHzwEN3ljqx-x_1xlOdv8nsvdFZCu5k9epsFW2AFq7VHhwnn9NBDlOU3JrtK2r_LoJYYvzZMNLta6I-T5zL80vfx02N3zeFt3mFGK9GT8Sk8DabkhTe9jEbIaa--hIM8-cX2nvQ7bVPPnWqxOnQKlm4Ac8ww8MspH81jbkItpKhjYxYppqUpmGpAFI5LGUWGK-hbcy43qt12HqijyEKJsiRg8VZL6lfu5wecvYrH9fWWffv2hnksAsGVNvtExLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pfROCUHWzd2cZfTh2EPP8rf0dli4gxKZhUWGBSdxXYPKAkS-dXFXBWRefr6n00_Y-7nvgKRzIz9YOLtOMaaPleoDPuyELTGfhyu221dYE_UcdR6670JzXd3LeBmCQRLwGZJEjWtZXzxus-izo8UK6H4wfAerG2D915YR4aluXvQiRoUiBEqci4V55KmLl0QvbLS_TDBeHv9U4RWkH3zQypFyoFIZzR9aH6PVy3BzaljR1jW9Wp_iTXx4phrfYiQeolzPASmaCta2x9vE8JmazBT-zqGPYKtwMt7GFRDxvwYvxgEtdBZE5g2ZpdYsXh4F745HvyiqSTlRGyYB96wcPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/srB10CMVk05lBlNY59_32Mp_ubaNekTlhMcq_3nv-sV0zHCRzKwwXSd_osj1lHcw8_VD2MM61n1gxC49Tvq3b5hwKAMXXBhSzdiKRcPK_eVT8cFM32lyNxTaE4rJLM-gWT0zDN7Iv0jywnb0OYy4_uCo9QZcaVpVtfVbmVf6mzbpCoqdStRI3TtZ5XjOXgVxU0O7r74AFBONZ33dUcEKHI1yqZVzjZU0m--RJ_6OnPFESgBSA5iUUInEM5Z0ZXh9wdGMWcd2oz-v9oD42SF-f9p2OO3NXjq9NUQL0fAfiUulkUtQJSI40ldaol2WBmxf2__sVyawzIQc_31W3VDs7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مخفی‌شدن ترامپ در کامیون حمل غذا سوژه شد
🔹
گزارش‌ها دربارۀ خروج مخفیانۀ ترامپ از ترکیه و جابه‌جایی او با یک کامیون حمل غذا، موجی از شوخی‌های کاربران را در فضای مجازی به‌راه انداخته است.
🔹
روز هشتم ژوئیه (۱۸ خرداد)، پس از برگزاری اجلاس ناتو در ترکیه، رئیس‌جمهور آمریکا در حالی که کاخ سفید همچنان مدعی بود او با هواپیمای «ایر فورس وان» در حال سفر است، ظاهراً از ترس تهدیدهای ایران بی‌سروصدا و با یک هواپیمای نظامی دیگر این کشور را ترک کرد.
🔹
ترامپ ابتدا در مقابل دوربین‌های خبرنگاران سوار هواپیمای ریاست‌جمهوری «ایر فورس وان» قدیمی‌تر در آنکارا شد، اما بعدتر به‌طور مخفیانه و از طریق یک کامیون خدمات پذیرایی فرودگاه که معمولاً برای بارگیری غذا و سایر تجهیزات مورد استفاده قرار می‌گیرد، به هواپیمایی کوچک‌تر منتقل شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/farsna/455604" target="_blank">📅 05:21 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455603">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a49537d50f.mp4?token=cuP5u7Gd00j1REos1fceIozKk-YAPrcusHJOxc77yBOoSOqShWWXQDuXckZicx7ujFZMMXZN5QCiOVAe6kuiZWE3z7NWI-lSqnGVxMhAxBrZaMAuU8FWvNwanwKC7VBoBBxIJkt3RjhW-YKjFwFpCfkBa3ZlAg8BWeUW9Bb07UIUK1G3QdUiBS74QPC45Q7R1-e3aQHSAaFtIRXBVCDLtfdWcI6d9zpuDAe9ffXBcGaPbMfAS01oSo-nrTzf9mJMGFc6E0x793gQkn1dUSE_85vvk5HvjgUMkr3A8CbZm6wS8YpiE1OaU48FBelP7qatJUxrev_Avi--ljx3kvj8pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a49537d50f.mp4?token=cuP5u7Gd00j1REos1fceIozKk-YAPrcusHJOxc77yBOoSOqShWWXQDuXckZicx7ujFZMMXZN5QCiOVAe6kuiZWE3z7NWI-lSqnGVxMhAxBrZaMAuU8FWvNwanwKC7VBoBBxIJkt3RjhW-YKjFwFpCfkBa3ZlAg8BWeUW9Bb07UIUK1G3QdUiBS74QPC45Q7R1-e3aQHSAaFtIRXBVCDLtfdWcI6d9zpuDAe9ffXBcGaPbMfAS01oSo-nrTzf9mJMGFc6E0x793gQkn1dUSE_85vvk5HvjgUMkr3A8CbZm6wS8YpiE1OaU48FBelP7qatJUxrev_Avi--ljx3kvj8pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملۀ پهپادی به یک نیروگاه برق در لیبی
🔹
الجزیره گزارش داد که نیروگاه برق الزاویه هدف حملات هواپیماهای بدون سرنشین قرار گرفته است.
🔹
شب گذشته نیز کارخانۀ ترکیب و بسته‌بندی نفت در پالایشگاه «الزاویه» هدف حملۀ پهپادی مجدد قرار گرفته بود.
🔹
هنوز هیچ گروهی مسئولیت حملات پهپادی اخیر به زیرساخت‌های انرژی در الزاویه را برعهده نگرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/farsna/455603" target="_blank">📅 05:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455602">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">کرۀ شمالی موشک بالستیک آزمایش کرد
🔹
وزارت دفاع ژاپن و ستاد مشترک ارتش کرۀ جنوبی اعلام کردند که حداقل یک فروند موشک بالستیک از منطقۀ «وونسان» در کرۀ شمالی به سمت دریای شرقی شلیک شده است.
🔸
این پرتاب‌های موشکی کرۀ شمالی در حالی انجام شد که قرار است کرۀ جنوبی و آمریکا رزمایش مشترک سالانۀ مهم خود را هفتۀ آینده آغاز کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/farsna/455602" target="_blank">📅 03:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455601">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09f0c890df.mp4?token=jXlDhOMMJJPILde7LgDpC8rT9bX3uKpyPFZDZzl-3gsN1hMiyOq90zgSFlmPCkCZDj4gX9hH-_ftuuLb_Gy7x0MKGWLv-0qLue4_XMQ_MDS5AOFi5BNi5rXqfaKvR9JtOGiFFnzFpurKwCPn7zyMtX1ydv0dPKOtPhw7TYW0PgB02OLerlv866nvVwyBdoNeYhsyFpMGtK3ndM2iIXIMSdvhGUP8GHOhM3B8NKIv1d2mp3jbIsDVoG_ht3HmraJUjBYh9OAxAqcklypC6UgOo8-hVTK4EOZCAbydvC_052DUY2_U4IiIYZS5eEeA-m-pSDN4SSvTGENG1saKDJPvOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09f0c890df.mp4?token=jXlDhOMMJJPILde7LgDpC8rT9bX3uKpyPFZDZzl-3gsN1hMiyOq90zgSFlmPCkCZDj4gX9hH-_ftuuLb_Gy7x0MKGWLv-0qLue4_XMQ_MDS5AOFi5BNi5rXqfaKvR9JtOGiFFnzFpurKwCPn7zyMtX1ydv0dPKOtPhw7TYW0PgB02OLerlv866nvVwyBdoNeYhsyFpMGtK3ndM2iIXIMSdvhGUP8GHOhM3B8NKIv1d2mp3jbIsDVoG_ht3HmraJUjBYh9OAxAqcklypC6UgOo8-hVTK4EOZCAbydvC_052DUY2_U4IiIYZS5eEeA-m-pSDN4SSvTGENG1saKDJPvOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دمام‌زنی زائران مشهدالرضا(ع) در خیابان‌های منتهی به حرم مطهر رضوی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/455601" target="_blank">📅 01:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455600">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">حملات توپخانه‌ای اسرائیل به مناطقی در غزه
🔹
منابع خبری از حملات ارتش رژیم صهیونیستی به مناطقی از شهر خان‌یونس در جنوب نوار غزه گزارش دادند.
@Farsna</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farsna/455600" target="_blank">📅 01:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455599">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">معاون وزیر کار: نقص اطلاعات فراجا، کالابرگ برخی افراد را قطع کرد
🔹
پیگیری خبرنگار فارس از وزارت رفاه نشان می‌دهد کالابرگ برخی افراد حاضر در کشور به‌‌دلیل ثبت‌نشدن اطلاعات ورود در سامانه فراجا متوقف شده و وزارت رفاه پیگیر اصلاح این اطلاعات است.
🔹
معاون وزیر…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/455599" target="_blank">📅 00:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455598">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e4f1ffff9.mp4?token=dEVrZmp6rwcDOxkW5OuHoUk23swhia6RWKq4NA83DGTpMAVeGfZhhVlk01cl3XJMxHvgKEPYSRR4wh2F2n5NIcTMdpU4krMuhAEKaWxgkXfq2Mp25W1fagyBdUxnVwBADcvsNmq6s12HqQBUCN3MTqioVbqpfSPH2j_c0Ce4MCG2NXciUpBi7HTOVaE7RxluroLrWpywT777R9T_p3B6T41WOme1iZPnEtMAuSrMztEd3l-ttizlzPBkhLU2b4LTQDdLKsCqnLGYQxnjXYEMNU6Pg1pO44yn6ecQSqvRzDbJB9sMK3d5Yl88xiWN2J4836SoSuOVf8J47ljt0dFFnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e4f1ffff9.mp4?token=dEVrZmp6rwcDOxkW5OuHoUk23swhia6RWKq4NA83DGTpMAVeGfZhhVlk01cl3XJMxHvgKEPYSRR4wh2F2n5NIcTMdpU4krMuhAEKaWxgkXfq2Mp25W1fagyBdUxnVwBADcvsNmq6s12HqQBUCN3MTqioVbqpfSPH2j_c0Ce4MCG2NXciUpBi7HTOVaE7RxluroLrWpywT777R9T_p3B6T41WOme1iZPnEtMAuSrMztEd3l-ttizlzPBkhLU2b4LTQDdLKsCqnLGYQxnjXYEMNU6Pg1pO44yn6ecQSqvRzDbJB9sMK3d5Yl88xiWN2J4836SoSuOVf8J47ljt0dFFnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر صهیونیست: نمی‌گذاریم غزه بازسازی شود
🔹
«گیدئون سعر» وزیر خارجه رژیم صهیونیستی با بیان اینکه یک سال است که غزه بازسازی نشده، گفت که نابودی تمام سلاح‌ها در این باریکه یکی از پیش‌شرط‌ها است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/455598" target="_blank">📅 00:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455597">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1d0f154e7.mp4?token=B6YxqyIwYlVMAfjnNjyatd_6UuoYbXo0KoEivshGu9IIh2ZLVRQnDpiB4VwCGVD1PbnZkeHyMWcEpOmoPibZugwSeIZmQuxG14Lw1jnpMSIRRw9jn1iqXWMRxv1TZZMVg7dSSMn5v2GFgHZ2JrIC7TmmU13DdKHEl2uRFELTtqtqKQmFNa109sarwCB_nOl-WLbsNE4OKfjm7kr2-2nRXis_OXlB2izP-c8cMMm4Dp4d-oUm_UjmH4H73NaV2iYGgItb1O8hzIRgYYxYasE0qhrHlzswEneCHRGhPgT1cWBIDN28AY3wf19Qal6xJeKn4PDWvJH0sUrj-XBnJx29ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1d0f154e7.mp4?token=B6YxqyIwYlVMAfjnNjyatd_6UuoYbXo0KoEivshGu9IIh2ZLVRQnDpiB4VwCGVD1PbnZkeHyMWcEpOmoPibZugwSeIZmQuxG14Lw1jnpMSIRRw9jn1iqXWMRxv1TZZMVg7dSSMn5v2GFgHZ2JrIC7TmmU13DdKHEl2uRFELTtqtqKQmFNa109sarwCB_nOl-WLbsNE4OKfjm7kr2-2nRXis_OXlB2izP-c8cMMm4Dp4d-oUm_UjmH4H73NaV2iYGgItb1O8hzIRgYYxYasE0qhrHlzswEneCHRGhPgT1cWBIDN28AY3wf19Qal6xJeKn4PDWvJH0sUrj-XBnJx29ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجمع خون‌خواهی دانشجویان مشهدی در جمع زائران امام رضا(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/455597" target="_blank">📅 00:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455592">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MgFICeFf3Y7PjkECF35iMXqQYfPvPZgMB4vmZt1VguNW0sM8JymYQP6ivIwfmdWy5FcB575FvJp6F-BQfQxjrtKx29DaNlY_seft97sMpdqK3RDpGPjgxe7y57TREkp1-OVP12gxo53vJyJtZCT970nCZaEwwKKxDp12-5HngDwJTm4uJ8-4lYZwemGFauONWRL-Emnuygs334khH6yRJXoy5eZzaE_6lmXZUNhfPRK7V-gSn5RWqXbmnTSrThpKngBy0YUEt_PJg1IKP_d522LpdftYUpf0VK0mnsBl8oV0DJ0jBzGsiX1keLZPeO9rRUhc1yR-Rn_8hFilllevHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hqq5T5foOG1SeIlAiHhwlM2hr12oj-0r4ihLqAhzV9rU2LUpKhmTrKtqckuZaemMZcBJBk6axXaudK5eR5_hR_NDd8v5vNaRYJP4d0yJpNjvS01KGWjDJe9PhwsLQKaYEu5IVfwNSVZ9gnSwekYwY_ld0aBtDEUfckKUX4ylVcubZKeGMYgJoYtzLg6V06WlOzxpH3-sk6HmgrDNcPJigzFG33ui-lz9OjgO2NKMVcTrX_FLSbVJ607iK0nW4kVk9xx9ccB3VynOesYw34IOAMJoupMpLDzZjmquIVy_B1eB7hTR4k_el10C_aMkbSgsJCffjO7eVBFHgqaR6lmHuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sa6NATKFNuWEKfLiOvnoaBXUsAGIAS1H5LrY2EeAfy-E65laSbQeCPYuRloG79WDJqcVAHugwSJYL-dW1PdfbNlmVrCXidvnSjQYMrvz5iTN-BSEPrKcOyIUQA8XbSbIdqr3l5HWDIMqvtP5BvcnF2NXrJd7L9QQUDGxo9Gb0UAb4ZrTJZBDGauOiCmHs7UJH7gpB_FX77yDse-qNyDn3jj-j7GgzPGUNHQGfiVUDPeNYOy_c2sN5ywFfRDeRL0w74sQJFKaB5HQVmo-rLwEeK8n4YlEQnhu34Zd1F-dbW-5bqmMHEvrKIRZW8b_QGNJyXhibvvC2Tewi954S8bHxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kszIISgDrRfgSWbSiP3wl5Wnxcs-W3-DRsERlXrl7dr63dha0xQ4ElxbE-KgMQadxK3wUE_F9pdqlcb-e8d3Xv-iuOrVkrEbYRr053-beTLmnYLR16jWnGWdY4IgAFIeAbGcWisur9vCqyFFm3kprhJO_PdpimJZNAaNN7Q6OHGVk80cLHfxH6wwgJT9gURU-kEcIOw330TR6jIkj_V4YKOIhK7QmOLmms6v4GRgQ06O1XB_IKnplBXbB1-xNstvlVdaIFnlVhqxtcsYuU7-_TuqT4Vj1W__gJhdj1Z3OHnAy7AvHIHVrPcfo4un5LO_Kg6t726OY0M5QQLmltK9cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HbmldwLnbvU4I7JsqqwRPouplqXC6b0Ua49SiVx-km5uRYELRrtsHOtJRAfxy8_BN2Qe5GKGouOgGE3TYCOzEgwkd-PngwqWsmDLWLPiwuPRZRF4pE-lRI5LhIyuMkxoxky4xRK4_Cvh-X0aZjH813bxIpp2KPwzwTTrjUreLDs1spgyIl8ySC3UgnomVqlKqSOTe8g8SH9ovpcNmDL2hG-2xwuGh87ctBucKaTrUUcmbPHkTzi_6wGXa3ahQwCvFsJ3rTeXQSE4qzQ_peSH7OmMUecXvv4_Xkw0uhnsqThbF4wPsrky8lBeLLoV0ozp9GwLgkJzn5O1vnGWcH9l7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حرم مطهر رضوی در شب رحلت پیامبر اکرم(ص) و شهادت امام حسن مجتبی(ع)
عکس:
حدیث فقیری
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/455592" target="_blank">📅 00:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455591">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/971416d83b.mp4?token=uw8SkJg4d_M6D45aGMKE9kxwRw6vkoK5_GdzQ0ugf7zHlMJwGpNR4sf_jwYChqlBrZIxM9bTJ5qXs_DuwkY1Ho7gR9P9XLPBl8BgHawDYRjgBmqTruk9uzW9873swTSQTmvI-NMYy2DFOccYWb6sj8oevqM9wzSLmFO-udkk_aOZyfEap03Uu6H5EC1lbjRwnSdKAiODHwyrYGE20vHrmbAm5uMGhhtQvJg0CFxpXMBEE7Xg0c4vud8kzJyMupCmKtevqekDmMvBdenOqn6y587UUt3f9FT3QMgY33kDuX_BRrFEbA4QnAjWfAWa0gTppnFmxGeypMZ3Bf1BLn-UCmcv91NaMkESvSY0yooCi4BuljSoL1qD9_4I1zUnXgKJ9CA9PnCyQumxNjzHB77soGazMYi-Kw5Un-96_4MLz55-AgmG4oGGpG3nrkICUmCBHHKM8AIOcgMakU5mCTocsrfKcYb1bsa-48_Se23Q1I7CMkIIc2qJm91SQpxOPz8yvxo8IwXusC9zryM-dVAb6ed3ISwEOCVDmdTWuIHUKNs0MX3NOr_LTbfOLS9g4QHiYddi6IgD1y5ayzGV64eiRfHWvGSmX7LCNk1_oZEPGQhBAxuza3qK6harEr_qp4ofMrX15by8UQnzldHo8xNLjCqmEt5sei5YoAfK7GQ1kfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/971416d83b.mp4?token=uw8SkJg4d_M6D45aGMKE9kxwRw6vkoK5_GdzQ0ugf7zHlMJwGpNR4sf_jwYChqlBrZIxM9bTJ5qXs_DuwkY1Ho7gR9P9XLPBl8BgHawDYRjgBmqTruk9uzW9873swTSQTmvI-NMYy2DFOccYWb6sj8oevqM9wzSLmFO-udkk_aOZyfEap03Uu6H5EC1lbjRwnSdKAiODHwyrYGE20vHrmbAm5uMGhhtQvJg0CFxpXMBEE7Xg0c4vud8kzJyMupCmKtevqekDmMvBdenOqn6y587UUt3f9FT3QMgY33kDuX_BRrFEbA4QnAjWfAWa0gTppnFmxGeypMZ3Bf1BLn-UCmcv91NaMkESvSY0yooCi4BuljSoL1qD9_4I1zUnXgKJ9CA9PnCyQumxNjzHB77soGazMYi-Kw5Un-96_4MLz55-AgmG4oGGpG3nrkICUmCBHHKM8AIOcgMakU5mCTocsrfKcYb1bsa-48_Se23Q1I7CMkIIc2qJm91SQpxOPz8yvxo8IwXusC9zryM-dVAb6ed3ISwEOCVDmdTWuIHUKNs0MX3NOr_LTbfOLS9g4QHiYddi6IgD1y5ayzGV64eiRfHWvGSmX7LCNk1_oZEPGQhBAxuza3qK6harEr_qp4ofMrX15by8UQnzldHo8xNLjCqmEt5sei5YoAfK7GQ1kfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاشمری‌ها در خون‌خواهی قائد شهید، شب ۱۶۴ نیز میدان را خالی نکردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/455591" target="_blank">📅 23:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455590">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-text">🎥
چه شوری در دلم افتاده از توصیف شیرینت
🔹
شعرخوانی حمیدرضا برقعه‌ای در مدح امام حسن(ع)
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/455590" target="_blank">📅 23:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455589">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f933dd533.mp4?token=g5Wo4LfhHXqkgGZYjo8tf25kdkDQG1j1Ed34BK_BipeA7w7qJxV2oWXFWyz4wif18-7SLamTqm-TWPmg0FeI-Kn2Je9m1dkHuNP7ToCoY6g-irMSyOcN5q-iS418qAAOHK7A8FkrTmQzNUIz3MmT8gRmR5gdXTm2tSke_NUr45mGLyPkLTsl8xPiPDfw38JhIEPop1hUjZt_06RRWsXAHWGBCdt8lI7uvNO7WPcGyTpm3jfcPwDX3gpTSMelwxNCONzKZmHb3jEqGQFRGfydYKWhbugz2AwxSkp2uWYIIXeCGqqaffvdRI_3DnRzFz06rNPjv28bPr-i9Fdj5mrOCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f933dd533.mp4?token=g5Wo4LfhHXqkgGZYjo8tf25kdkDQG1j1Ed34BK_BipeA7w7qJxV2oWXFWyz4wif18-7SLamTqm-TWPmg0FeI-Kn2Je9m1dkHuNP7ToCoY6g-irMSyOcN5q-iS418qAAOHK7A8FkrTmQzNUIz3MmT8gRmR5gdXTm2tSke_NUr45mGLyPkLTsl8xPiPDfw38JhIEPop1hUjZt_06RRWsXAHWGBCdt8lI7uvNO7WPcGyTpm3jfcPwDX3gpTSMelwxNCONzKZmHb3jEqGQFRGfydYKWhbugz2AwxSkp2uWYIIXeCGqqaffvdRI_3DnRzFz06rNPjv28bPr-i9Fdj5mrOCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پارسال همین شب‌ها؛ خادمی سردار شهید تنگسیری در حرم رضوی
@Farsna</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/455589" target="_blank">📅 23:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455588">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5ANYPRxY3_5gSGqnFCBsAZ8WTIY1XMyMbbRX9OV7ZcTb7wq-ClXU3QnhxL5D0ptVfalcJh46VcXTSTG3KYJJvN8vB41yiAJdhA2JOSki4p86de7NF6FFUtdb1HUEZD52O_W4XvZPjbcnPUJmkPl8EpNTwHmiFQmflp0xrT05ar6w2f0O2nG_p8ApQ1jKvCyVGrac5H6MzpfWozCUv_SyZ7kAXeXBienWRsdnesg7hApMmxvehhVx5C87hE9iGCWKrHY9Tx2JDIfExeR1TpySyJRDNv7TAHHpadDVyAjDUpy_0sOyZ47RvpDHQwyUhk-SdxzOhVi2qAdyLQIfhdwfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلنسکی: طرح‌هایی برای مجبور کردن روسیه به پایان جنگ به آمریکا داده‌ایم
🔹
ولودیمیر زلنسکی، رئیس‌جمهور اوکراین: اوکراین پیشنهاداتی را به ایالات متحده ارائه کرده است تا روسیه را مجبور به پایان دادن به جنگ کند.
🔸
آمریکا می‌تواند به دفاع ما کمک کند، به ویژه در زمینه پدافند هوایی، و بر روسیه فشار وارد کند تا برنامه‌های متفاوتی داشته باشد، برای پایان جنگ آماده شود و آن را به تعویق نگذارد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/455588" target="_blank">📅 23:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455587">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOgJB45GhXA834DvGhMZ1Wkx9i1F9vR-hS-Ytjbg2d34Q2hQ1vrkknmnOjopK3cCUhwEsZcuP8ZH1Fw5v726Xxub1tryjblDiR3wZxP6dsRZkjPHm9R7h4B9qIMk2rmDjaHMLzc5mCiS8OB5PI2KiEya4QweeIPbRJb-QUbySz_oHnd5YFFDs2_Ug-Q3wyDbCzqOwL2OHFSITmnKqegfNALlogmI6W3tuXwKqgYJbWaS2xo8Qsh0aw4jWQLAosu8w97Gj8LIrzMSjUZEwesq4jVnrCW2lPrCw8PbWn_fgIlrpkb9fBB1tFC2E97CtBIo6s5AvbZkobXGn6u5M7CPrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش‌سوزی مشکوک در نزدیکی فرودگاهی در واشنگتن
🔹
رسانه‌های آمریکایی از آتش‌سوزی در نزدیکی فرودگاه اسپوکین در ایالت واشنگتن آمریکا و توقف فعالیت در این فرودگاه خبر می‌دهند.
🔹
آمریکایی‌ها تاکنون علتی برای این آتش‌سوزی مخابره نکرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/455587" target="_blank">📅 23:42 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455586">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
حملهٔ هوایی رژیم صهیونیستی به جنوب لبنان
🔹
شبکهٔ المنار: جنگنده‌های رژیم صهیونیستی دره الحجیر در اطراف شهرک دیر سریان را بمباران کردند.
@Farsna</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/455586" target="_blank">📅 23:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455585">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e8c92bb74.mp4?token=R6yYV2LdwzvRHbuY6vGyFIhZja15t0aw9pMuN2OEd5pmN6wrPovxdioG4UFG0nxaEwuGCfk1I2LXWELPOYGoMHQ59yuOvqIWk8CHehWSagkUmYj3kMK9UIQuoymRDDS2cupSfVRiBNz_BcmKWFsnSkAnOql2AbX136f9exCuhhvzQM263KcK1-bbzy_ZkCmxEF7mmjKSs2UBQm2OGlHOmIKfoosZ9FbUxXEygI15V8r3NdG2tnuFyQ9SyP17rkUDi5RJC4VBInAnEFeNC97uLauzQBhQeYnH7kOqkWV4AWEmk_slbb96hK5AoNn15dw7TLVJgd_yBfQE0_hvBhTPzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e8c92bb74.mp4?token=R6yYV2LdwzvRHbuY6vGyFIhZja15t0aw9pMuN2OEd5pmN6wrPovxdioG4UFG0nxaEwuGCfk1I2LXWELPOYGoMHQ59yuOvqIWk8CHehWSagkUmYj3kMK9UIQuoymRDDS2cupSfVRiBNz_BcmKWFsnSkAnOql2AbX136f9exCuhhvzQM263KcK1-bbzy_ZkCmxEF7mmjKSs2UBQm2OGlHOmIKfoosZ9FbUxXEygI15V8r3NdG2tnuFyQ9SyP17rkUDi5RJC4VBInAnEFeNC97uLauzQBhQeYnH7kOqkWV4AWEmk_slbb96hK5AoNn15dw7TLVJgd_yBfQE0_hvBhTPzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای آلودگی نفتی در سواحل قشم
🔹
تصاویر منتشرشده در فضای مجازی، این روزها بخش‌هایی از سواحل قشم را با لکه‌های نفتی نشان می‌دهد.
🔹
بررسی‌های خبرنگار فارس نشان می‌دهد منشأ این موضوع هنوز مشخص نیست اما احتمال دریایی بودن منشأ آلودگی نیز مطرح شده است.
🔹
دادستان قشم دستگاه‌های مسئول را مکلف کرده منشأ آلودگی را شناسایی کنند و عملیات جمع‌آوری و پاک‌سازی نوار ساحلی نیز بدون وقفه انجام می‌شود.
🔸
این نخستین‌بار نیست که سواحل هرمزگان با آلودگی نفتی روبه‌رو می‌شوند؛ اردیبهشت امسال نیز بخش‌هایی از سواحل این استان تحت‌تأثیر آلودگی نفتی قرار گرفته بود.
🔹
سواحل جنوبی ایران محل زیست گونه‌های مختلف دریایی است و به گفتۀ مدیرکل حفاظت محیط‌زیست هرمزگان، آلودگی نفتی می‌تواند برای چنین زیستگاه‌هایی پیامدهای جدی داشته باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/455585" target="_blank">📅 23:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455584">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3da26e9533.mp4?token=iblRUJODytyQRrQIm5J7fhv8mm6ZbHCoXnidy-cuxFoN62j2Xk0Qlg_Nm4ODSTACOSFunKoq_Suj498hXYSLpx-Aj8YUSMkhcKSyOSqllAK4QdRt-glx17I_cnXBd4TigzmaaboOJfTCG44CzyWoljre1YO8fx9B2m6p93zdjV1F4UkRqw8zs6COzyb0bOu8qSShmcQr6JJ-5HDyZ34YOHWWXKIn8p_1ZsJqMm-WMlmu7eo8CdkLvNAGCxg4W7e9McTk3nhBIzXIMO_aACcOC0I_Rb-odPfdtPk5qLcvUVifcIKDSP7EGXXZ8TnaybDy9i1O6BMlVkXK5J4lSg4HuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3da26e9533.mp4?token=iblRUJODytyQRrQIm5J7fhv8mm6ZbHCoXnidy-cuxFoN62j2Xk0Qlg_Nm4ODSTACOSFunKoq_Suj498hXYSLpx-Aj8YUSMkhcKSyOSqllAK4QdRt-glx17I_cnXBd4TigzmaaboOJfTCG44CzyWoljre1YO8fx9B2m6p93zdjV1F4UkRqw8zs6COzyb0bOu8qSShmcQr6JJ-5HDyZ34YOHWWXKIn8p_1ZsJqMm-WMlmu7eo8CdkLvNAGCxg4W7e9McTk3nhBIzXIMO_aACcOC0I_Rb-odPfdtPk5qLcvUVifcIKDSP7EGXXZ8TnaybDy9i1O6BMlVkXK5J4lSg4HuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار نقدی: پیروزی ما حاصل حضور مردم در میدان و نفوذ در جهان بود  @Farsna</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/455584" target="_blank">📅 23:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455583">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7262ea5013.mp4?token=DZBIxr9wUuScSmuKfiklf1G4Rt-Q9yh7xwRL4gRPT-IWp9IZEimov88KUT_bsKnL6wCvovIPP4Psd4lxYRkm6UvS-1IasFcb4SOx-C8smWkiy13OyVOwtf2XKs7rshWCmElVlDYQjlhfrVAp3vozSgDihbmxeyjSLKULrZuguGlp3ckbVOaT0gm2m-pfRhXzbIeFsgtQy7wjivXrF2CTUEbDX7mwp1fvjmAyN_ImgNapjOc_b1m5F6c5Es5tsJQqOVcI4MP31HypDY5sqG828INS1zxNN3YIPgD-l1jT5ci4QYTZxo3nVUnD55KOIcy1om1O-N26bsv3Kad2AMWAmzR2RsaPPHquSx-XOBGMF_BdaTb7uexa6mNXP2MurSTR9ZOA_eJ778K9Lm9dSkzBtNBezA6PUl5RmTI9FLkrpB5gn9fctXgy9yiVAw02h41lPQF9Ontdx1tLPy5VbPza0ChZqX0a5lLd0ma0YBgF2RbXxolROjqY_FyqFR6enDyKBgEpqo-A8yrHhZchI3b-wd6VTrNg8nyUK2KsyNEbMj2HX0zZQa0zHQU6Aad1Z6tTQ49MNztFvfEdTKNbkqtkb6Lp3a5nRlNx9WPFKgAQMIk_TLyqgyWDSLYEPKRvGvYDgBJAPe7ahuR1XaikmLeYg6GvKuHBc6hqDIJHLS5yKdU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7262ea5013.mp4?token=DZBIxr9wUuScSmuKfiklf1G4Rt-Q9yh7xwRL4gRPT-IWp9IZEimov88KUT_bsKnL6wCvovIPP4Psd4lxYRkm6UvS-1IasFcb4SOx-C8smWkiy13OyVOwtf2XKs7rshWCmElVlDYQjlhfrVAp3vozSgDihbmxeyjSLKULrZuguGlp3ckbVOaT0gm2m-pfRhXzbIeFsgtQy7wjivXrF2CTUEbDX7mwp1fvjmAyN_ImgNapjOc_b1m5F6c5Es5tsJQqOVcI4MP31HypDY5sqG828INS1zxNN3YIPgD-l1jT5ci4QYTZxo3nVUnD55KOIcy1om1O-N26bsv3Kad2AMWAmzR2RsaPPHquSx-XOBGMF_BdaTb7uexa6mNXP2MurSTR9ZOA_eJ778K9Lm9dSkzBtNBezA6PUl5RmTI9FLkrpB5gn9fctXgy9yiVAw02h41lPQF9Ontdx1tLPy5VbPza0ChZqX0a5lLd0ma0YBgF2RbXxolROjqY_FyqFR6enDyKBgEpqo-A8yrHhZchI3b-wd6VTrNg8nyUK2KsyNEbMj2HX0zZQa0zHQU6Aad1Z6tTQ49MNztFvfEdTKNbkqtkb6Lp3a5nRlNx9WPFKgAQMIk_TLyqgyWDSLYEPKRvGvYDgBJAPe7ahuR1XaikmLeYg6GvKuHBc6hqDIJHLS5yKdU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمایندۀ جنوب در لیگ‌برتر به‌یاد کودکان میناب
🔹
استقلال خوزستان از پیراهن فصل جدید خود با نمادی از خلیج فارس و کودکان میناب رونمایی کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/455583" target="_blank">📅 23:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455582">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e650ac866.mp4?token=q_iBheBTqJfhDf74fvey8bchrHyrb5NYXe_KupvT4P5UnodPYhncg6cBIC5w-YMOUHQnIkY-s0CxoBb_7P4sGXnmQ4-rJ-yT5uQxP02q0QKIBY4nI3qNC77iAOWQ0xZokqHjc223KL4g48JU1IXrhu_JzhX9nShSyqwcEOGJqZ_CL1X_I_0O4kaWfvfehxSeYdCjnuac5HgSbqJ0gLhPf76UcfvTYOooRGo8E6SOWSjBS5VQqbS9taiVs8SW1yc_WPXhweIWZjJy-AoG9CfbatuPRbw6UviAxw9IziOvQqy6uY5kFBR1qsqgkQVNV2BcT0o5k90wUKcz_GL76ogsEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e650ac866.mp4?token=q_iBheBTqJfhDf74fvey8bchrHyrb5NYXe_KupvT4P5UnodPYhncg6cBIC5w-YMOUHQnIkY-s0CxoBb_7P4sGXnmQ4-rJ-yT5uQxP02q0QKIBY4nI3qNC77iAOWQ0xZokqHjc223KL4g48JU1IXrhu_JzhX9nShSyqwcEOGJqZ_CL1X_I_0O4kaWfvfehxSeYdCjnuac5HgSbqJ0gLhPf76UcfvTYOooRGo8E6SOWSjBS5VQqbS9taiVs8SW1yc_WPXhweIWZjJy-AoG9CfbatuPRbw6UviAxw9IziOvQqy6uY5kFBR1qsqgkQVNV2BcT0o5k90wUKcz_GL76ogsEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار نقدی: وقتی دشمن به اهدافش نرسید؛ برنامه‌ای برای ادامه نداشت  @Farsna</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/455582" target="_blank">📅 23:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455581">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89468323b2.mp4?token=v7NhWhzzNhMyvsGfflCWOVVhx3CtHXxJ94nQeQrpaQ1JXS7vlmKvWMiZdRFRja-19DDTLXDiXpehLAfraUkAQWec6kTR2xguvRHjWw8vIAXFUY5LMkgX8OSjRW2bkCmhF_z1MPRbAEdxwsO-8bAjArUYHLr_TB7E9e_59jTOL0iv7CRkUKuiqzcZI3GxHZvypfd5eWqndiZN88TfaACBUgGnO86BV2C1yl3fv2Esc2amkt0gl-dBweRfPN6GyvesxgAz59IlLR3zukdSpHAR1XdYWspK94hjyNttKNIq0b7lZzXbs6bVbwlPG9aj3GcwahZRE2dzvyNU-Xu-yUjD-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89468323b2.mp4?token=v7NhWhzzNhMyvsGfflCWOVVhx3CtHXxJ94nQeQrpaQ1JXS7vlmKvWMiZdRFRja-19DDTLXDiXpehLAfraUkAQWec6kTR2xguvRHjWw8vIAXFUY5LMkgX8OSjRW2bkCmhF_z1MPRbAEdxwsO-8bAjArUYHLr_TB7E9e_59jTOL0iv7CRkUKuiqzcZI3GxHZvypfd5eWqndiZN88TfaACBUgGnO86BV2C1yl3fv2Esc2amkt0gl-dBweRfPN6GyvesxgAz59IlLR3zukdSpHAR1XdYWspK94hjyNttKNIq0b7lZzXbs6bVbwlPG9aj3GcwahZRE2dzvyNU-Xu-yUjD-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردارنقدی: بعد از جنگ، جمهوری اسلامی طرفداران زیادی در دنیا پیدا کرده است  @Farsna</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/farsna/455581" target="_blank">📅 22:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455580">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
برخی منابع از وقوع ۲ انفجار مجدد در مواضع مزدوران سعودی در مأرب یمن خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/455580" target="_blank">📅 22:48 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455579">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QeDqlqDF077eVnK3Z44RMSQQRs2G9wL7chikZH1QMtATtIJwnEcB0BWMgY4ysaSKWiAChY61NRs5DhqSm6BO2x1S7UAp9PTqRgagaiB4ffs0idlfxMfgGEx7XLMdLmVQmSY3xJED2z23MuRsHUfR01bIASAOsxvrkBRwjR8El1WoCCRhG0N4YFmauRUAdB2FMkEPvSYIh4A2BB24idL1szrOQKFcV3WaganSxFmiV6TApybODvAZgKhBqOafudTvAk7IZeJGAkkSEbk7WikFFYkIPJ3mZbFRxdhi8f6zYg6DCGebt5-qLc-cI6uUguDWOT5s8QkLsQuuWe8--pCepQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲ مقام آمریکایی: ایران تنها در یک روز آمریکا را به شلیک ۵۰ پاتریوت مجبور کرد
🔹
۲ مقام آمریکایی امروز در گفت‌وگو با نیویورک‌تایمز خبر داده‌اند که تنها در یک روز از ۵ روزهای نبرد میان ایران و ایالات‌متحده، آمریکا مجبور به شلیک حدود ۵۰ تیر موشک پاتریوت شد که هر کدام حدود ۴ میلیون دلار قیمت دارند.
🔸
اشاره نیویورک‌تایمز به حملات ایران پس‌از نقض تفاهم‌نامه توسط آمریکاست که در یکی از آن‌ها در تاریخ ۲۶ تیر حمله به پایگاه موفق‌السلطی اردن به کشته‌‌شدن دست‌کم ۳ نظامی آمریکا و زخمی‌شدن ده‌ها نظامی دیگر منجر شد.
🔹
نیویورک‌تایمز در این گزارش مفصل به تشریح این پرداخته که ایران چگونه تاکتیک‌های جنگی خودش را منطبق کرده تا بتواند از سامانه‌های پدافندی آمریکا عبور کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/455579" target="_blank">📅 22:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455578">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d7021b6ac.mp4?token=pIX05VSIwdi4g11kLhUM9jE8rvV30vjMMVMrUKNBXqxtapoVhm4tQprjNpovsCoY8bd3IqswGd-UW6sArW7hgn6PVBpITB6SAq4BaLJM5jMiAkNUWnrG23oNFXky7d9MNLgPlKS3AtS7ZjGjwl1bt26cMTwtHCZXFOKo_QDA-hZFEn9xPu8qdOoZJVx9Qp371VZLAlt1lddPabqWYQeHpYGouayabvLzroDq9LvC6AsC_qx974WnCTPyCZrosqBgbidOqb8YqAVFML80X6Ti_ZBHW3HJpJxfYl00ypQOomJiWQ0Zt9iCoVguOyqkBvlOAGv8stihURtrAg43oNZYRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d7021b6ac.mp4?token=pIX05VSIwdi4g11kLhUM9jE8rvV30vjMMVMrUKNBXqxtapoVhm4tQprjNpovsCoY8bd3IqswGd-UW6sArW7hgn6PVBpITB6SAq4BaLJM5jMiAkNUWnrG23oNFXky7d9MNLgPlKS3AtS7ZjGjwl1bt26cMTwtHCZXFOKo_QDA-hZFEn9xPu8qdOoZJVx9Qp371VZLAlt1lddPabqWYQeHpYGouayabvLzroDq9LvC6AsC_qx974WnCTPyCZrosqBgbidOqb8YqAVFML80X6Ti_ZBHW3HJpJxfYl00ypQOomJiWQ0Zt9iCoVguOyqkBvlOAGv8stihURtrAg43oNZYRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار نقدی: آن‌چه ما را برای جنگیدن متمایز می‌کند و دشمن آن را ندارد، ایمان است.  @Farsna</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/farsna/455578" target="_blank">📅 22:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455577">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18b80717a4.mp4?token=PzXiHNZsqU3ApBqPf03PVySIL1gsgD_bPU3LPvKXhhh2nI_97fZ-OtJivw4UYQlqjQgeN6yCEGGdVZA8zHOPu1QCLI1tI-K8LWRZebeYW4djzmmOlJ2EWHYrqtO7-Vjn6TeKy09ax4yllVR9f5MDxeNsQXJ9c2Otcev0diRsfHsdjGVvioKBIDvn_EuiFROaRhjyl7z-ZNER2eNhUFKJRRC_jexeHUQew0jGVIVuJ2kJrs6C5lVuK4H7I1Gn53DfDhO60-iNsthYqliaLrG1Xs9p5hGDdJeOx9e-NY_lIhUI82w5tYkzcDFtcRV8SQGknzEhCgfl0qHFS8AgvhaXBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18b80717a4.mp4?token=PzXiHNZsqU3ApBqPf03PVySIL1gsgD_bPU3LPvKXhhh2nI_97fZ-OtJivw4UYQlqjQgeN6yCEGGdVZA8zHOPu1QCLI1tI-K8LWRZebeYW4djzmmOlJ2EWHYrqtO7-Vjn6TeKy09ax4yllVR9f5MDxeNsQXJ9c2Otcev0diRsfHsdjGVvioKBIDvn_EuiFROaRhjyl7z-ZNER2eNhUFKJRRC_jexeHUQew0jGVIVuJ2kJrs6C5lVuK4H7I1Gn53DfDhO60-iNsthYqliaLrG1Xs9p5hGDdJeOx9e-NY_lIhUI82w5tYkzcDFtcRV8SQGknzEhCgfl0qHFS8AgvhaXBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرمانده نیروی دریایی سپاه: آمریکایی‌ها در خلیج فارس بهترین ابزارها را دارند، ناو و جنگنده دارند ولی یک چیزی ندارند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/455577" target="_blank">📅 22:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455576">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa04e53aad.mp4?token=g9rRfeEvEE8NoTu3r6udMQ4JI9WXe3JGj3VcPaXEUX7LR-uMjs7Y_ODDzVLPi8VUjV5XTyxQ0MiAWaRa1nV_sE5jQvDW3t3eMabn6ppK-e2MzmV9VTJIatdGkJHkJjeHgI9_ME62CR6g0ClNLXEOW7XkUdHgPqpkCE9I3BV2jhfp-1tAI0jjXrwOuIiCAO9K6RmsXtYzV5RPCqJOC86Yh0WIV2buEjDXAeFZv55WpgcTnIEgARxtI-hP8JXKwjYnKG8wloEl195IM7RU-1_1PvEfXe7OH_HGxxttkvA4J5o4nLJmBXsZSuJLRZx_CTSKMTiMBJpcJUzIv79h7pQ0aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa04e53aad.mp4?token=g9rRfeEvEE8NoTu3r6udMQ4JI9WXe3JGj3VcPaXEUX7LR-uMjs7Y_ODDzVLPi8VUjV5XTyxQ0MiAWaRa1nV_sE5jQvDW3t3eMabn6ppK-e2MzmV9VTJIatdGkJHkJjeHgI9_ME62CR6g0ClNLXEOW7XkUdHgPqpkCE9I3BV2jhfp-1tAI0jjXrwOuIiCAO9K6RmsXtYzV5RPCqJOC86Yh0WIV2buEjDXAeFZv55WpgcTnIEgARxtI-hP8JXKwjYnKG8wloEl195IM7RU-1_1PvEfXe7OH_HGxxttkvA4J5o4nLJmBXsZSuJLRZx_CTSKMTiMBJpcJUzIv79h7pQ0aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اضافه‌خدمت سربازان فراجا با انجام این کارها بخشیده می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/farsna/455576" target="_blank">📅 22:30 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455575">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23e49d43e4.mp4?token=HCZj7WO8C8g9U27GO_jHkIEaqgOlHxeJzSyyJbnP2PVig13AS1Re_7CjpxOFjU1cCbvjq36M6vgmmp6GjkTenCe1Xbl-Xy4wJSSHu9d-VPjUVX4LLwKwUtqbCrmol81ZlonfpQBH224yhKfuRsstKVrYoRirkoUbWPDjqY3Cy9IXlZQqu22thye0o7lXjKJdgH0tErj1GfzJu3EaY4WqSo6pd_xqKW9NbqUanfpIJtnDWM2LYDoH1OUaGOMa-K0OmPO8B3e9ikoZ2-N9MIqwBisP2p_qj-wICym2AlE5rlv8wSygkJF2t_EseuDBLsWHuMTY7frQuwY25dFq-rtzHKjwEiwne181OKlArHX6rLR1vsK6It9D2pUjKvZLiECY7e7czhjaDP7m_uWbLjGh08fMrWYFcHZ2CHcbCot0xCQexw5iTHrJYBQLcZdWPMTCBNEFcKSkd_j7ogeq1EA3wfQZhlwrVXuIzdxl3XAwfqh6tzto1U8hw3JQXavd13PreWYnxdkLNVsFzeUoloTeoMZXV__XvgnrxyX8dGLCnzDMjtOcYk_Mk7tXzrFgkDyjlBHKz8-JCP9oz6Kb9fYNCEW7styv2FmuN74GT0H-aX471nk21JbkT5mocdPVSIMedTicv67z34RJyZiBEXgRsBNeentIoxeqZtiFsDWpUio" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23e49d43e4.mp4?token=HCZj7WO8C8g9U27GO_jHkIEaqgOlHxeJzSyyJbnP2PVig13AS1Re_7CjpxOFjU1cCbvjq36M6vgmmp6GjkTenCe1Xbl-Xy4wJSSHu9d-VPjUVX4LLwKwUtqbCrmol81ZlonfpQBH224yhKfuRsstKVrYoRirkoUbWPDjqY3Cy9IXlZQqu22thye0o7lXjKJdgH0tErj1GfzJu3EaY4WqSo6pd_xqKW9NbqUanfpIJtnDWM2LYDoH1OUaGOMa-K0OmPO8B3e9ikoZ2-N9MIqwBisP2p_qj-wICym2AlE5rlv8wSygkJF2t_EseuDBLsWHuMTY7frQuwY25dFq-rtzHKjwEiwne181OKlArHX6rLR1vsK6It9D2pUjKvZLiECY7e7czhjaDP7m_uWbLjGh08fMrWYFcHZ2CHcbCot0xCQexw5iTHrJYBQLcZdWPMTCBNEFcKSkd_j7ogeq1EA3wfQZhlwrVXuIzdxl3XAwfqh6tzto1U8hw3JQXavd13PreWYnxdkLNVsFzeUoloTeoMZXV__XvgnrxyX8dGLCnzDMjtOcYk_Mk7tXzrFgkDyjlBHKz8-JCP9oz6Kb9fYNCEW7styv2FmuN74GT0H-aX471nk21JbkT5mocdPVSIMedTicv67z34RJyZiBEXgRsBNeentIoxeqZtiFsDWpUio" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خسارت رگبارهای سیلابی به چهاردانگۀ مازندران رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/455575" target="_blank">📅 22:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455574">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🎥
اولین تصاویر از ۶ متهم پروندۀ قتل حمیدرضا رجب‌زاده
🔸
حمیدرضا رجب‌زاده حدود ۱۷ روز پیش ناپدید شده بود اما ۶ روز پیش ویدیویی از پیکر آسیب‌دیده‌اش در یک کانال ضدانقلاب منتشر و در فضای مجازی دست‌به‌دست شد. در نهایت روز گذشته پیکر سوخته حمیدرضا رجب‌زاده در اطراف…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/455574" target="_blank">📅 22:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455573">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9382974591.mp4?token=BRZU6iJ1iqQFg0mIyy3C6VTLqCbHgqWupZngcTHHAM8-XUSMrog7DpovKACCpj2s6sQKVgXB3RoKSMgUXJ83rCFcpSEWxTFq9-cYDdjpsNlxULxsfoYMRyIEn-yLs0XX7KccrJsDF-nKWyFtgjz0KLfk8E7ARWwTaNgzwmqfx9GbvgB4KhTKDEFz0eNmJT8c6mmGYMN-LkvHDzvtrhaNomDbV6KOEdiuASHHdonyJ-qL5MSUH0SfhEyMzUI3v-L_K01yFWmNO1hVtErVR89gBJYcfVjQ5LWu5k_yWwz4MCJjYQR5W00NFlXN7CmcizytRxzItu3EGG1HS5BPIZQnYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9382974591.mp4?token=BRZU6iJ1iqQFg0mIyy3C6VTLqCbHgqWupZngcTHHAM8-XUSMrog7DpovKACCpj2s6sQKVgXB3RoKSMgUXJ83rCFcpSEWxTFq9-cYDdjpsNlxULxsfoYMRyIEn-yLs0XX7KccrJsDF-nKWyFtgjz0KLfk8E7ARWwTaNgzwmqfx9GbvgB4KhTKDEFz0eNmJT8c6mmGYMN-LkvHDzvtrhaNomDbV6KOEdiuASHHdonyJ-qL5MSUH0SfhEyMzUI3v-L_K01yFWmNO1hVtErVR89gBJYcfVjQ5LWu5k_yWwz4MCJjYQR5W00NFlXN7CmcizytRxzItu3EGG1HS5BPIZQnYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پورابراهیمی: قرارگاه خاتم‌الانبیا باید در حوزۀ اقتصاد تشکیل شود
🔹
رئیس کمیسیون اقتصادی دبیرخانه مجمع تشخیص: رهبر شهید فرموده بودند «جنگ ما با وزارت خزانه‌داری آمریکا است» و امروز نیز محاصرۀ دریایی را می‌توان مصداق این جنگ اقتصادی دانست.
🔹
در شرایط فعلی،…</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/455573" target="_blank">📅 22:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455572">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86175ae2d8.mp4?token=IF5JKKXw9L561_QQStCSyE7OgjSIDR3N2J_fYSTC6GMhoG8aGPI0Z8f6Okd0UrGOy2zP3XYcat4qul1STrS7oteOtfmVOZkRo_37QaO7jqg3Ln3Qio0B3tIbr8NfdUIBH2-Cpy66q_hHtrhdh2PyEOMF2KpJTOL5Zs_JhcQryMGVESCw-Btb2Z9t7ICYLH58lDuvaL8vTqH7wAaEe5zsBB5cQCc5JV6TgPtoZy4V7KHlHFCcWlQLrf8Se4gKB12L7KjrjYo6fQ8WxGdXGC3BQTHe3UQAg1-b-9UlLCm8EYFfolFNIRMSvqF-1uuyf1cSmqhEEunw_r2bqiyah2k2XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86175ae2d8.mp4?token=IF5JKKXw9L561_QQStCSyE7OgjSIDR3N2J_fYSTC6GMhoG8aGPI0Z8f6Okd0UrGOy2zP3XYcat4qul1STrS7oteOtfmVOZkRo_37QaO7jqg3Ln3Qio0B3tIbr8NfdUIBH2-Cpy66q_hHtrhdh2PyEOMF2KpJTOL5Zs_JhcQryMGVESCw-Btb2Z9t7ICYLH58lDuvaL8vTqH7wAaEe5zsBB5cQCc5JV6TgPtoZy4V7KHlHFCcWlQLrf8Se4gKB12L7KjrjYo6fQ8WxGdXGC3BQTHe3UQAg1-b-9UlLCm8EYFfolFNIRMSvqF-1uuyf1cSmqhEEunw_r2bqiyah2k2XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بروجردی‌ها: نه خسته‌ایم نه رنجور، ایستاده‌ایم تا ظهور
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/455572" target="_blank">📅 22:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455571">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d26ccae06.mp4?token=Fa9_5dr3JkmKQbJybThaqhoB7DuomFDPECz_Pe4hyCB02-65IpRcBGU3TxmM9uGV3Uf0CVFgTPl_f7v6lxv0znUwj0K_w8963dXZhLYeQRyDGcL4er55I0t6MBNTy2UX4EASCna8yY2uAKhq5hZwNWwOAc3SxsP6Iih-W8wcAudFJuvBDxmcfaWXB8xQ9w0IE0P9WrZjMS-H6wSTMZ8BvmWBhFURQoEvwMer46xmiiB-WesD7mVtM78rZgZYQQlMAEpRz1pzOBsnA60BWmjXYtqOXWfKngmFp9unuMq-GQnVNGFjgBjGuxPjtlYbwlW6Hahj0Ne_a1rq0lMY1bRysA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d26ccae06.mp4?token=Fa9_5dr3JkmKQbJybThaqhoB7DuomFDPECz_Pe4hyCB02-65IpRcBGU3TxmM9uGV3Uf0CVFgTPl_f7v6lxv0znUwj0K_w8963dXZhLYeQRyDGcL4er55I0t6MBNTy2UX4EASCna8yY2uAKhq5hZwNWwOAc3SxsP6Iih-W8wcAudFJuvBDxmcfaWXB8xQ9w0IE0P9WrZjMS-H6wSTMZ8BvmWBhFURQoEvwMer46xmiiB-WesD7mVtM78rZgZYQQlMAEpRz1pzOBsnA60BWmjXYtqOXWfKngmFp9unuMq-GQnVNGFjgBjGuxPjtlYbwlW6Hahj0Ne_a1rq0lMY1bRysA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در سالروز شهادت پیامبر(ص) مدینه سیاه‌پوش نمی‌شود
🔹
هم‌زمان با سالروز شهادت پیامبر اکرم(ص)، مسجدالنبی مملو از زائرانی از سراسر جهان است؛ اما در مدینه خبری از مراسم عمومی سوگواری، نوحه‌خوانی و سیاه‌پوش‌شدن اماکن نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/455571" target="_blank">📅 22:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455568">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AseK89wMSEQjomd4Z2YhLPvYUPUPy4uTWhBTW9SkmevNFG7c7PY91_e6dn8i4SDw3TTsjZOfbBci3DWLoBNJEXe4a0Ie71sUrCbAJDVG2uiQO7hFG5lJ6b12d-JT0PAxaD8D7MfM-ukTk8b_M0hmWbWAjvtwopTORsLGQDSNhHvFn838wKhHO60QF4-ckGRtnuTpxvyGkrKvV-oH_CoqLpdjp2v5Elg9XJoHQCelkPArbM8hkW-Qd6V_Sl-OtWTTliCf_rQGYaSB36h9BvUsFCSwwKYIJ9sG9IzCsm1uxBuC8Gc9o_rlOIVfhQZ3kSm_1Il_VXb8N4rK7k2rULL6tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e3hwFOwB5rDEfOw-9PPHTMKO0H9vMMSrAKy1V69zvrTkX6OoQwh-lCY022_apAR0aFBZ19uzJkJjy57vgyOKni1xVpvnOpoqW50IrtlYvYTNqLkEOu75e8QqjNWG88behh-y8XstAxUZ3IkNhyWVLtQErCbq0QujNZJKi3E_-6fS1mR_pct4nrRD_qmJHqDsS2OfhXaph9XchwC3j322XJn4sXd4CDmV8akZFgWJ2l6C2JDgAZcoHP5IvBzJIdm9Y46RFJDBhIqBOXafOoOzSJ8wL0wWroD-xIPClQM7gNIIJLpjSO9pJ6yN8GEPxI2dMQKizy9j1_mM5xtFvQEbXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vtbaz1HA-oWaYf7P2EcjSXsJ_pG_DN_8S9oZGxHuPIgoiG98ElZr2RNFFqDbncwlzZtLQESSbaeNAm_-mVghs3tChEMXYh1i3q72xKm85W4aKVWkzgVi4MM9DHggHTThpRx370ZaMuGYvytPZT_8ox_JQnGi17JZM9sXPN8K4cQdk-oip7GrvZaqX6ki1I5e7TE6xe4R9APg6CbIbOVhV7Ahhl5ZRHqUWGOykYqKRSYe0QshJ_dSpWtTVeLReTq3vb1676daWaB4lL1AAbp2CDob5Bo6AoTVOKRLu9olbmskuT999LRaHm2iey8Sev0nGQE5lK4UhBGy5VfxjKrQCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نماز جماعت حرم امیرالمومنین(ع) در شب شهادت رسول‌الله(ع)
@Farsna</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/455568" target="_blank">📅 22:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455567">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17fc4e62c7.mp4?token=faJ4rBuBxJkHN7rxRql2WyCjHim0WMFze2urN4Daf57v_AGhyBFUXhPbOCa4UndDAZWf_yqcfKyX6F7KK326IHGB-eyDJ4XzJKhcBJqegZuQJ9MreGcgr3tRR2p7X0n18jyKZUB_QmpIKCkibMJsIlfCTGQvJ6dKjtkMWWbBJhvPGRiygOorMN686BgW61KwB4QU1ciEJNvenwMlTx3BskJ2diZ6p_yJxv7lVjnlmhIdLuPersb7qUx1DSOgdw7Z94fIBqzl8h5OlYYr0bfP0fHxVnHE7fm-4zmXhTQXcapih7774NXaQFrbBzuQGWoRmNiHSxOt-wzb4KuYtwPKoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17fc4e62c7.mp4?token=faJ4rBuBxJkHN7rxRql2WyCjHim0WMFze2urN4Daf57v_AGhyBFUXhPbOCa4UndDAZWf_yqcfKyX6F7KK326IHGB-eyDJ4XzJKhcBJqegZuQJ9MreGcgr3tRR2p7X0n18jyKZUB_QmpIKCkibMJsIlfCTGQvJ6dKjtkMWWbBJhvPGRiygOorMN686BgW61KwB4QU1ciEJNvenwMlTx3BskJ2diZ6p_yJxv7lVjnlmhIdLuPersb7qUx1DSOgdw7Z94fIBqzl8h5OlYYr0bfP0fHxVnHE7fm-4zmXhTQXcapih7774NXaQFrbBzuQGWoRmNiHSxOt-wzb4KuYtwPKoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج ۱۶۴حضور زرندی های ولایتمدار در میدان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/455567" target="_blank">📅 22:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455566">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2G_4FEunSpDwlixxMaJFM9Gb4qgcWDnF3eabqWyo0DWAq2KnwYn3GREQ51TLmiA4lIwgk4noxYz39wEwHq5X16cRsCYRB5VYl427M9AEGesHvr2DHL-tzg-LNufSM2u4g6pccda8ArPzNLGgJJanuFbhQkVYOItgYWXTJKHEsXlOGyb4l4_GikRTwhMOAtrgR5f-wPyfngWyzhuO1NV2LmEoPYmUNq1VRyDdbkmd8iUS893YASWVthmKSEoDuYUDZ8beH31IYQTBBDLnhp7mVYOm39_8qh2NoBi01ES6lUc5C4gbtfVUOjkPUuLS5NSy_rpyCa0p7J263xv8d5Oog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرط سنگین رامین برای پیوستن به فولاد
🔹
طی ساعات اخیر شایعاتی درباره پیوستن رامین رضاییان به فولاد خوزستان مطرح شده اما پیگیری‌ها نشان می‌دهد که این بازیکن هنوز قراردادی با باشگاه خوزستانی به امضا نرسانده است.
🔹
رضاییان در مذاکراتی که با مسئولان باشگاه فولاد خوزستان داشته، خواستار قراردادی به ارزش ۲۰۰ میلیارد تومان شده. رقمی که مورد موافقت باشگاه فولاد قرار نگرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/farsna/455566" target="_blank">📅 21:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455565">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">جزئیات نیویورک‌تایمز از تخصص ۲ نظامی آمریکایی کشته‌شده در حملات ایران
🔹
روزنامه نیویورک‌تایمز گزارش داده نیروهای مسلح ایران با بررسی جنگ اوکراین موافق شده‌اند به پایگاه‌های آمریکا در منطقه ضربه وارد کنند.
🔹
به نوشته این روزنامه در اوکراین، روسیه از ترکیبی از موشک‌های بالستیک و کروز برای منحرف کردن حواس پدافند هوایی اوکراین استفاده کرده و سپس پهپادها را گسیل داشته است.
🔹
به نوشته این روزنامه در جریان جنگ ۱۲ روزه در ژوئن ۲۰۲۵ مقام‌های ایران دیده بودند که نیروهای اسرائیلی و آمریکایی چقدر سریع موشک‌های رهگیر بالستیک خود را برای سرنگونی رگبار پهپادها و موشک‌های ایرانی مصرف کردند.
🔹
مرگبارترین حملات ایران علیه نیروهای آمریکایی در اردن، پایگاه هوایی موفق السلطی در ازرق را هدف قرار داد؛ یک پایگاه نظامی اردنی که نیروی هوایی آمریکا به طور فزاینده‌ای از آن به عنوان کانون اصلی ده‌ها فروند هواپیما و چند هزار نظامی استفاده کرده است.
🔹
بسیاری از نیروهای آمریکایی که پیش‌تر در کویت، بحرین، قطر و امارات متحده عربی مستقر بودند، قبل و در طول جنگ به پایگاه‌هایی مانند موفق السلطی در اردن منتقل شدند که از ایران دورتر بود و در برابر حملات پهپادی و بالستیک ایمن‌تر تلقی می‌شد.
🔹
به نوشته نیویورک‌تایمز متخصصان نظامی آمریکا که نحوه حملات پهپادی و موشکی در جنگ اوکراین را بررسی کرده‌اند، ماه‌هاست که با فرماندهی مرکزی آمریکا در خاورمیانه (سنتکام) همکاری می‌کنند تا تجربیات به دست آمده از جنگ اوکراین را به آن‌ها منتقل کنند.
🔸
دو نفر از سه سرباز آمریکایی که بر اثر حملات ایران به پایگاه آمریکا در اردن کشته شدند، از اعضای همین یگان‌های پدافند هوایی مستقر در آلمان بودند که در راستای همین همکاری و انتقال تجربه به منطقه اعزام شده بودند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/farsna/455565" target="_blank">📅 21:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455564">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XvErdH7k1nnDc2E-yvUpETYr45cOMQm4wjpef9YUQFXLxmfT80A_0WcKfeVhsqJCo2chtCp5I8AteCL-wsWNo02b0I4mxDSPcTbMUZc4pJ2tggp_nr3Thl3guJgRqcEGFvQbd9F1HzF2tvVdGQ2zN5PVxNQVO6-TLIRgzqO34FZG-bDew641Xq5rdEaiuC_YiI9wykvhOlxYDegVohDBbLOg3zLEmMITMGuhnKBaoOxDjOCrpa0Oyt2flfbAYUKc3hsf2KFbRCVR67H7v9djw0KS5lLIJWsaE6-gJZPVCUC30fdXZ7jhX5lAEobnjNtm37H0IOUELCGKH2HI0G52tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ونزوئلا و اسرائیل روابط کنسولی خود را از سرگرفتند
🔹
رژیم صهیونیستی و ونزوئلا امروز در بیانیه‌ای مشترک، ازسرگیری روابط کنسولی میان ۲ طرف را اعلام کردند.
🔹
طبق این بیانیه، «گفت‌وگوها شامل توافق بر سر ایجاد سازوکاری هماهنگ بود که ارائه خدمات کنسولی به شهروندان ۲ طرف را امکان‌پذیر می‌سازد.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/455564" target="_blank">📅 21:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455562">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/410eba0dda.mp4?token=q8p2kuuR0l82UCNDao32pKAH0UZwtCRpGNRDoaHww2M9mwgLapfh8oWQ_IdpP283kC6GHgSj8XfDl3KJ_yLdTAIeP_4qhGP0RjcqUSLbThrh2aS5hHFVzJEXcn3k5-1UD4DR1T7vi3bmGcIn5HLxgC3qTH-cljKiThdTjgs1C5LQho8QP-xZsPBk1su72QLWA92elcmbyrvzJ_a2DhkuC3RqOoP15cPLKmC1-LBMppyHmQO-G8pOjZFiS-pGqhzVuyHwk9vlNcGYSEtN14SmarpiftQemz5RBJ2UWCphaDnjgloCPiModQZvdFF_05BgBXB-aNRkzqjmrgTlQt4b8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/410eba0dda.mp4?token=q8p2kuuR0l82UCNDao32pKAH0UZwtCRpGNRDoaHww2M9mwgLapfh8oWQ_IdpP283kC6GHgSj8XfDl3KJ_yLdTAIeP_4qhGP0RjcqUSLbThrh2aS5hHFVzJEXcn3k5-1UD4DR1T7vi3bmGcIn5HLxgC3qTH-cljKiThdTjgs1C5LQho8QP-xZsPBk1su72QLWA92elcmbyrvzJ_a2DhkuC3RqOoP15cPLKmC1-LBMppyHmQO-G8pOjZFiS-pGqhzVuyHwk9vlNcGYSEtN14SmarpiftQemz5RBJ2UWCphaDnjgloCPiModQZvdFF_05BgBXB-aNRkzqjmrgTlQt4b8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نقل‌قول جعلی منتسب به سردار وحیدی چگونه از هند به سخنرانی نتانیاهو رسید؟
🔹
هفتۀ گذشته نتانیاهو، نخست‌وزیر رژیم صهیونیستی گفت «امروز شنیدیم احمد وحیدی، فرمانده سپاه پاسداران به صراحت قصد ایران برای توسعۀ سلاح هسته‌ای را اعلام کرده است.
🔹
این درحالی است که…</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/455562" target="_blank">📅 21:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455561">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZAKtFAIi89jpaxL2MnET1XBVsHy4j4LKIdyblzE5TnCh_QmSKRQNsXKcK_2MXODgnhlC2Brra4SF_1kvM-vdw9ubZ0_il34h26sMDngBcuWZ5sp_Kkia9Yhe9ttBSE95lO3mZqz7Gb1fWF7uGZLrwSYZHXcj7Wf27iA_oj7z9WXJ0LAuk3gFJNmBLk4rMtWSRErbrHH6vWK7g-4vU0R9AYIVnDSJyQerUJRqC4CGdvbQ24SL9X7BuLS_LRCZL4vlTSMDK7gAPJiuKYb-jOwm9LHB5JqsOm7cB2Pa2SiPz_33Fhhu3nlDm9Zltlgms03VzBZs5alYGSYilFj1X73Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یمن: عربستان به جای ناله‌کردن محاصره را متوقف کند
🔹
معاون وزیر اطلاع‌رسانی یمن: ما از ممنوعیت کشتیرانی دریایی علیه دشمن سعودی کوتاه نخواهیم آمد.
🔹
به دشمن سعودی می‌گوییم به‌ جای ناله و شکایت به دلیل کشتی‌های هدف‌قرارگرفته، محاصره و تجاوز ظالمانۀ خود علیه یمن را متوقف کند.
🔹
عربستان از عملیات نیروهای مسلح یمن به دلیل دقت آن‌ها در هدف قرار دادن عناصر تحت حمایتش، غافلگیر شده است.
🔹
عربستان هیچ گزینه‌ای جز تسلیم شدن در برابر خواست ملت یمن ندارد و یمنی‌ها امروز برای لغو محاصره کشور، متحدتر از هر زمان دیگری هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/455561" target="_blank">📅 21:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455560">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‌
🔴
حملهٔ موشکی به یک کشتی سعودی دیگر در باب‌المندب
🔹
منابع خبری گزارش دادند، یک کشتی تجاری دیگر متعلق به عربستان امروز در تنگهٔ باب‌المندب هدف حملهٔ موشکی قرار گرفتند.
🔸
این برای نخستین‌بار است که ۲ کشتی در فاصلهٔ زمانی تنها ۲ ساعت از یکدیگر در دریای سرخ…</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/455560" target="_blank">📅 21:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455559">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fcc9d5cb8.mp4?token=ljVK0FLIpM2S9r1b-De5WyI6C_uF18roes02D_j24RfnvLghwADQdz-q9KZeoaqIFjjt6qn0Oq4Tz8pVBgbk4tyt8spcvvvDBtBxpT2MaLn6nl6WbLQgsZIulfYbxrjX1tJ4eThqqRSG3am7w6XLv1Yz72uBMvciErrpVCyKXI1VqKsm3c6jfn4pbufbGy9tBPZg7nvlNk7YzvDvEqxhsl1UujZgZCnW18XXIWr6m9zzncCldleYR9OTO5UcDqhUiUCgBvI6Noc9yuCJvecP5pn_ZtUYW1pOGKCN0kusTCGt9HwwV9KCG7vYGvXZkVQXDiw-vv5wPgp7sHFX-IfQrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fcc9d5cb8.mp4?token=ljVK0FLIpM2S9r1b-De5WyI6C_uF18roes02D_j24RfnvLghwADQdz-q9KZeoaqIFjjt6qn0Oq4Tz8pVBgbk4tyt8spcvvvDBtBxpT2MaLn6nl6WbLQgsZIulfYbxrjX1tJ4eThqqRSG3am7w6XLv1Yz72uBMvciErrpVCyKXI1VqKsm3c6jfn4pbufbGy9tBPZg7nvlNk7YzvDvEqxhsl1UujZgZCnW18XXIWr6m9zzncCldleYR9OTO5UcDqhUiUCgBvI6Noc9yuCJvecP5pn_ZtUYW1pOGKCN0kusTCGt9HwwV9KCG7vYGvXZkVQXDiw-vv5wPgp7sHFX-IfQrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پشت پردهٔ طولانی‌شدن واگذاری سهام سایپا
@Farsna</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/455559" target="_blank">📅 21:17 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455558">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0aMNMAUZYV0O1Ob4QN3veW6OESNw_zITMELG3-at4W7dpfUMERDiDM3ZNCZ8U4bWY3j2VYjB7dgY6KvfHbNdF0_IX-SCPsAcs2287j8hCzzFAWNRQBYrse78pvXRkjmAW8K4uHZ6Q5kopvrLOvbZMovhSs_ldtef8-9GB-LPlGTm3jM1fL17w4Kn8Xsq4n8yJwEUAXtmTfcvd2KvzfpoaJOO-Tk6GMf5BUquq_NIaqcgS1TL2G-QeZnYRVq-SFcmtP-qzgpKPRUzSBTWC23c_E9Czuui3MaItIdXOHhb9u9phwtIo60UYwrCgFX5KysmZpAPIbFy93PR_DPrY0PxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: بر تعمیق روابط با پاکستان در همۀ زمینه‌ها تأکید داریم
🔹
رئیس‌جمهور در دیدار با وزیر کشور پاکستان: پیوندهای عمیق تاریخی، فرهنگی و مردمی میان ایران و پاکستان، پشتوانه‌ای ارزشمند برای مناسبات ۲ کشور است.
🔹
ظرفیت‌های گسترده‌ای برای گسترش همکاری‌های سیاسی، اقتصادی، تجاری، فرهنگی و امنیتی دو کشور وجود دارد.
🔹
نقوی، وزیر کشور پاکستان هم گفت: روابط ایران و پاکستان مستحکم و ناگسستنی است و ما با عزمی جدی، توسعه همه‌جانبه مناسبات با جمهوری اسلامی ایران را دنبال می‌کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/455558" target="_blank">📅 21:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455557">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05f19957e6.mp4?token=HqWOCs2yJq9L4-Mbx6VtvsjUHeu0U8klsBxfOEB5ana9PEAJIt9WT_iSLVxMI2N62LIy6XjwN7z9JYUeY4fIYoKFqOfidck5jhW5vgsUU0YVLKGAkZ8Ngz2gs0AsUtbRHD2D6oom1fT9vDlnx86OiLivyop5vjPa8vAO3CZGwcb_YoJLfJmdeuTHA-hFp1KUJUlw3nDX_t6d7g_A61Er3zYO2FnSoaks7tRs_5iif9hIu6uHapwpPzV4oihxmdVUQ7dIDdMq3G1Tb0uuNZA_lbV0UqBg5rWxxGKiOzIveIpylEHkvfpCwjjmNej8OcumCGI8fYSwjSd9s_zD1L6U0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05f19957e6.mp4?token=HqWOCs2yJq9L4-Mbx6VtvsjUHeu0U8klsBxfOEB5ana9PEAJIt9WT_iSLVxMI2N62LIy6XjwN7z9JYUeY4fIYoKFqOfidck5jhW5vgsUU0YVLKGAkZ8Ngz2gs0AsUtbRHD2D6oom1fT9vDlnx86OiLivyop5vjPa8vAO3CZGwcb_YoJLfJmdeuTHA-hFp1KUJUlw3nDX_t6d7g_A61Er3zYO2FnSoaks7tRs_5iif9hIu6uHapwpPzV4oihxmdVUQ7dIDdMq3G1Tb0uuNZA_lbV0UqBg5rWxxGKiOzIveIpylEHkvfpCwjjmNej8OcumCGI8fYSwjSd9s_zD1L6U0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای ارسال پیامک قطع کالابرگ به مردم چیست؟
@Farsna</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/455557" target="_blank">📅 21:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455556">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
برخی منابع از وقوع ۲ انفجار مجدد در مواضع مزدوران سعودی در مأرب یمن خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/455556" target="_blank">📅 20:56 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455555">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1m4d_HbQSvWSo5rBj2QPhw0ae8yxnCxElFsm-5r9h02Il18Dd1FSAfR1Gi8CWB8KqPlc9RAY89svOXmycMrGXSBv_Snn4I4LJKQzNPNdTnisBngFQ6UySGZwi2ltrPLUGojHnOZmF83WCwBy995l_OtiQMFqW3X33Xck2Nl9t_x0UhBGTuOyHtgQcJeFMQl8RgdyxzokKHVQ28R4D_e1LQ2bUV89vCBtQEKuuV7v-EFocUzYRuWJzNeFNjXSc17RjTmidf7GAKyQKXuT84FvyQmQ5hAL5evso2uW3q-46jv9QmXE913lFchslx7QC7g2vi_tfXZp5kAlifperCiwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای عالی امنیت ملی
: تا زمانی که همه شرایط برآورده نشود، تنگه هرمز بسته خواهد ماند
🔹
سرلشکر محسن رضایی در شبکه اجتماعی ایکس نوشت: پیام ایران واضح است: تنگه هرمز تا زمانی که ایالات متحده به جنگ و محاصره پایان ندهد، دارایی‌های مسدود شده ایران را آزاد نکند و جنگ در سراسر منطقه از جمله در لبنان و غزه پایان نیابد، بازگشایی نخواهد شد. تا زمانی که همه شرایط برآورده نشود، تنگه هرمز بسته خواهد ماند.
@Farspolitics</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/farsna/455555" target="_blank">📅 20:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455554">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34778a2dae.mp4?token=dV6uL9Xsx5O9eKI257KJCJOfuIc2RqS_PeU51BHmyZc3ncNtmzj6GMGuUpNq-RPdBVtyAaS7VALowhtWOpPz_quJgyIHCyvYBYL-433o2dCWSk-SYs5ygJI8-Scjfld456z-lv3a0AQGZWfzAjVnJNdN5WM-gsLUVsYQYt-6pXX0ZDViiiFipSk23z8R4tW-SQeLGzueXl4tYVEDr1_xTEQsTglKpt_5GENpcMZylB4tL1OXVNSpPHrSAGKt6OtG14mEm8JCazDViiVHg5JcNbkGozb7DjbAl5KyNyuISqi4o77NmuW79BThy5YQsCY5IjyRzLD6WoQnKtWM6atY34WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34778a2dae.mp4?token=dV6uL9Xsx5O9eKI257KJCJOfuIc2RqS_PeU51BHmyZc3ncNtmzj6GMGuUpNq-RPdBVtyAaS7VALowhtWOpPz_quJgyIHCyvYBYL-433o2dCWSk-SYs5ygJI8-Scjfld456z-lv3a0AQGZWfzAjVnJNdN5WM-gsLUVsYQYt-6pXX0ZDViiiFipSk23z8R4tW-SQeLGzueXl4tYVEDr1_xTEQsTglKpt_5GENpcMZylB4tL1OXVNSpPHrSAGKt6OtG14mEm8JCazDViiVHg5JcNbkGozb7DjbAl5KyNyuISqi4o77NmuW79BThy5YQsCY5IjyRzLD6WoQnKtWM6atY34WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۶۴ شب ایستادگی؛ مردم از اقتدار ایران می‌گویند
@Farsna</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/455554" target="_blank">📅 20:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455553">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfom1_CePRR2_21nkdG1COhBnZlrZR9Mkkv9rviIfmkmTKvWVZ4chGXUY4lhQB5nrGR6upO_NVXMgF8nDjoazlrRTrPlS7MbP_LBFCCa8QoNatCYmQUeFfhklmFAJbRFDGgQdFdyBQzWvkbWpGRPKHPwkXbJ1UIWhvgH3WjRHrHQX34vpwY-oeQqepQKQf-SVoyqMj2qjm57TvkEGPbXHhg8hOBe-wHjRyDZ2_qJtEyuS0dfZW5Ce3KnwOBNtAhwBRTGXbPBfIvqJyz0jimyMSmfpa0_Lpf3zayGMe-zmBInIZkL16CLOt9bkarL8VpVzMAC0NEuMQjSpqh5D66bYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گفت‌وگوی تلفنی عراقچی و رئیس اتحادیه میهنی کردستان عراق
🔹
عراقچی وزیر امورخارجه در گفت‌وگو با بافل طالبانی، رئیس اتحادیۀ میهنی کردستان دربارۀ تقویت هماهنگی‌ها و همکاری‌های امنیتی با هدف حفظ امنیت مرزهای مشترک تبادل‌نظر کردند.
@Farsna</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/455553" target="_blank">📅 20:53 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455547">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۱۱.pdf</div>
  <div class="tg-doc-extra">2.8 MB</div>
</div>
<a href="https://t.me/farsna/455547" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۱۰.pdf</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farsna/455547" target="_blank">📅 20:42 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455546">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKGG1ap0A6Pbt562YKifsn2MBuDseVGfMrOOHWk24iA8Qs1QS8YYFzmR65aLt1eXkl9fMmhX5MIjHAcFl8jbDAdhYIZFE_8qAkRj2qNcltShEUebPqHChJyXk3m0hIiY4G7LT8kEorpUr-bT955DavmDlY8C5TkVbbMQ72Co2UgKynLOhHX34d88TCFGMhRJ86m6qoSPiO-1KkoNk8FrCbruwuTo8o47oxj9VFVdBaeALP2AXK9zmjHxEXKlptUN2--dZCbQZrg9fXz6DHEBOxgwYQQ1wofPUKBFhsoYDjNUNBqesTCmu8Z6H_W2z4hNnKFA8BZTGjSnejSi7si0nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روایت آیت‌الله طاهری از فرآیند انتخاب رهبری توسط مجلس خبرگان
🔹
نماینده مردم گلستان در مجلس خبرگان: دشمن با تمام وجود تهدیدهایی را علیه مجلس خبرگان و اعضای آن مطرح کرد و چندین بار نیز اقداماتی را برای ممانعت از برگزاری جلسه و انجام فرآیند انتخاب اجرایی کرد.
🔹
بارها تلاش‌هایی برای برگزاری جلسه حضوری صورت گرفت که هربار به دلایل امنیتی و برخی اتفاقات امکان برگزاری مهیا نشد.
🔹
در یک هفته‌ای که اعضا در محل‌های متفاوتی حضور داشتند جلسات کوچک ۵، ۱۰ و ۱۲ نفره در بین اعضا تشکیل شد.
🔹
در این جلسات به جزئیات دربارهٔ ویژگی‌های اخلاقی، فقهی و علمی  آیت‌الله سیدمجتبی خامنه‌ای پرداخته شد و آنچه به‌عنوان رای نهایی خبرگان مطرح شد حاصل یک یقین کامل و جامع نسبت به مصداق بود.
🔹
علاوه بر رای مکتوب، اعضای خبرگان رهبری به‌صورت ویدیویی نیز رای خود را ضبط کردند و در اختیار افراد مطمئن قرار دادند.
🔹
ما در آن یک هفته به وضوح عنایت حق تعالی و امام‌ زمان(عج) را برای کمک به سرنوشت جامعه و انقلاب اسلامی دیدیم و باید تصریح کرد که حضرت آیت‌الله سید مجتبی خامنه‌ای با اکثریت مطلق آرا از میان گزینه‌ها انتخاب و معرفی شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/455546" target="_blank">📅 20:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455545">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1GmdSlzRYsFAtSXQghjMuU0cl4oxE5gqL4ZbLm4Lr42LAewRFnISgIDVZNWztkEnwLBtCDSLuoB4EtpFW20VWKHbinJx5ZY6dO4eRU3TdNsTkIM38JpfV8vZotjGlstkqxKj87Lu9l0rbptV-IOouNfKuqIzoJAnYlZ0Fk12R1V3_WH2h1yCXvgZMYFvyNUo5e9rgrnHQlYaxoVchLtPHhbkL08ph_42bIPI_cZyoWqk4M904tmLU-QiiIERXMdMZLH1JmQUBC-bMecTXlEGS_dnnhySHEQ0ht8Y7Jf_fqD-NVF8hhwY3jkDAfa3maE4s2sMYHWvkwX38VwbWBAOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: سلاح و جنگنده به اروپا می‌فروشیم و آن‌ها در ارسال به اوکراین آزادند
🔹
رئیس‌جمهور آمریکا از فروش مهمات و جنگنده‌ها به اتحادیهٔ اروپا خبر داد و گفت کشورهای اروپایی می‌توانند تسلیحات خریداری‌شده را به اوکراین منتقل کنند.
🔹
این موضع‌گیری در شرایطی صورت می‌گیرد که روسیه بارها ارسال هرگونه سلاح به اوکراین را «مختل‌کننده روند صلح» و «درگیرکننده مستقیم کشورهای ناتو» خوانده است.
🔸
وزیرخارجهٔ روسیه، پیشتر تأکید کرده بود که هر محمولهٔ تسلیحاتی به اوکراین، هدفی مشروع برای نیروهای روسیه محسوب می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/farsna/455545" target="_blank">📅 20:24 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455544">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5bfada637.mp4?token=cN4ja1acvCUYtCH_ZRLqT1UFtJ-PEGzRRkWvp47vxWzcZP88fpDArOp7zpHw6sg-ASVqIRAp4oFzDcZvreiSEyImyXh379I6mtuxZDaVqrKeEP_pZcwmHNCXW27fMLtSeAGNnnwm0HgJkif-vChp3NNULaeSHYz4t9VVE_tkqfXuNBfzTBx-d-fFQyScAeAt9V7nmiRwkS7YcP17Ql48_DeizWUrX0-GK4muNoekhcV-0JnDJYg4yFTvnG5QEaWl9s8RcX2GjUXfvbZUMA2_Lzugt2D1voWQ4z6XgwnOTrjyqhIgK4yInhMhC32Q1DeyYAkOkir5y5gArwqKUAKCKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5bfada637.mp4?token=cN4ja1acvCUYtCH_ZRLqT1UFtJ-PEGzRRkWvp47vxWzcZP88fpDArOp7zpHw6sg-ASVqIRAp4oFzDcZvreiSEyImyXh379I6mtuxZDaVqrKeEP_pZcwmHNCXW27fMLtSeAGNnnwm0HgJkif-vChp3NNULaeSHYz4t9VVE_tkqfXuNBfzTBx-d-fFQyScAeAt9V7nmiRwkS7YcP17Ql48_DeizWUrX0-GK4muNoekhcV-0JnDJYg4yFTvnG5QEaWl9s8RcX2GjUXfvbZUMA2_Lzugt2D1voWQ4z6XgwnOTrjyqhIgK4yInhMhC32Q1DeyYAkOkir5y5gArwqKUAKCKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایتی از حملهٔ سنگین دشمن صهیونیست به ارتفاعات علی الطاهر برای اشغال این منطقه با سو‌ءاستفاده از فرصت آتش‌بس  @Farsna</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/455544" target="_blank">📅 20:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455543">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f57ad4d8b9.mp4?token=WVfc8l1NnAlpXu_ufr2AnOoOeDmBxanMGgK3QmOaXTldJ7FXXUdKyc3l7tIOzFYp9cNzQcGOxpe6GFXfcxjPjaIAeVq76KPyRPcLunFihFeK9ogOXxU11j1ErQ9wO2SquyEFBjG7IcI5dewMV8efJV9LwrqwRrsjMrXClMOtgxHjeZA-l1z5x9tUrvKJlI-9ZLQ1ODa2s3BiF1U3IcECZ7KbFO4lnzWakT9CYPtYPq4HLWWv7s4uwNGIVY8OdF62lx1uGJcFtpT4oU9kR4NZXELz8Uc4lDnfF2JwAuSVTvZ_vG0Ob8ARoqYpDOG5Ad1ceDj92wUhfdPb-VSAcYCscg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f57ad4d8b9.mp4?token=WVfc8l1NnAlpXu_ufr2AnOoOeDmBxanMGgK3QmOaXTldJ7FXXUdKyc3l7tIOzFYp9cNzQcGOxpe6GFXfcxjPjaIAeVq76KPyRPcLunFihFeK9ogOXxU11j1ErQ9wO2SquyEFBjG7IcI5dewMV8efJV9LwrqwRrsjMrXClMOtgxHjeZA-l1z5x9tUrvKJlI-9ZLQ1ODa2s3BiF1U3IcECZ7KbFO4lnzWakT9CYPtYPq4HLWWv7s4uwNGIVY8OdF62lx1uGJcFtpT4oU9kR4NZXELz8Uc4lDnfF2JwAuSVTvZ_vG0Ob8ARoqYpDOG5Ad1ceDj92wUhfdPb-VSAcYCscg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام رفیعی در سمت خدا: هر غم‌دیده‌ای به زیارت امام رضا(ع) برود، غم دلش برطرف می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/455543" target="_blank">📅 19:57 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455542">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05571479e8.mp4?token=e-xugPGWHIFPPsvt07EtJg_885VptryR1vuujrveCC5oXpo6pJwEVhhLirMrxacpis2cU0RWEDfi0yCFjXH7uYqTik8W-gTFrLuXxpvWoEqYOvQQAGYmJzbPKmsrYJ8dwjk8461B2w6wUq4yLTSSdtc50jCkHP4zUKDlxNWRJH1_i7zsJQXY2gkEOCE3nbLlg1S-jO61o56FTih-8NiWmNWOqT_3vEjLlq28ydyWUqu8KHiet1UEsvt5BLbXW_Q-sDEfCCWIZ0bojGvoSpC1rfrRarsGBlD5C-hbWbHP49UBQVB5r3YI-xVJy2BSXKatMNwxX2tWXezJ2bNZT9bldQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05571479e8.mp4?token=e-xugPGWHIFPPsvt07EtJg_885VptryR1vuujrveCC5oXpo6pJwEVhhLirMrxacpis2cU0RWEDfi0yCFjXH7uYqTik8W-gTFrLuXxpvWoEqYOvQQAGYmJzbPKmsrYJ8dwjk8461B2w6wUq4yLTSSdtc50jCkHP4zUKDlxNWRJH1_i7zsJQXY2gkEOCE3nbLlg1S-jO61o56FTih-8NiWmNWOqT_3vEjLlq28ydyWUqu8KHiet1UEsvt5BLbXW_Q-sDEfCCWIZ0bojGvoSpC1rfrRarsGBlD5C-hbWbHP49UBQVB5r3YI-xVJy2BSXKatMNwxX2tWXezJ2bNZT9bldQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی سپاه: امروز حتی یک شناور جنگی آمریکا در خلیج فارس حضور ندارد
🔹
سردار محبی: آمریکا پیش‌از جنگ رمضان ۳۰ تا ۴۰ شناور جنگی در منطقه داشت اما امروز حتی یک شناور جنگی آمریکا در خلیج فارس حضور ندارد.
🔹
درصورت وقوع مجدد تهدید علیه ایران، صدها هزار مایل خطوط…</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/455542" target="_blank">📅 19:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455540">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCiGR5VjUm4PBGtHPRyw5jI1-PfsQMJqOqLp65vgzkGiONv56uI6Ae1WcrpXF5vmhdmJDFL27SSs4lnjxmj7uZxbLmBjNltcW6kumRhcoD9hplZG7bz3E8_znxYZY4uODbkNqJ1LB8o0hhmrtNt8VUnTT-zVogs1O08B1-TCLgHIiyOmktDnFe8kcUvgs9Ncy3bXZBkm-J-YNH8x1Ac6k4pH2FhYr_GNe3wD5wAAPPY3GvWzIZxBmnEdQ7iIw8ObnJB0DHn5RbNV0Ci-fZReNxdnJ2uajpG8fhSRQxKHp9VMceowCY9ibdRaTuBjoaw-epuqSePebyzftDZ3gSmELQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر رضایی: آمریکا باید جنگ را پایان دهد و پول‌های مسدودشده ایران را بپردازد
🔹
دبیر شورای‌عالی امنیت ملی در دیدار با سفیر چین:  اقدام چین در حمایت‌نکردن از قطعنامۀ ضدایرانی و غیرقانونی ارائه‌شده در شورای امنیت سازمان ملل، در جنگ رمضان را مثبت ارزیابی می‌کنیم.
🔹
تا زمانی‌ که آمریکا رفتار خود را تغییر ندهد و شروط ایران را نپذیرد تنگه هرمز باز نخواهد شد.
🔹
آمریکا باید جنگ را پایان دهد، پول‌های مسدود شده ایران را بپردازد و در کل منطقه از جمله لبنان و غزه جنگ باید پایان یابد و شروطی دیگر که از طریق واسطه‌ها به آن‌ها منتقل شده است را عمل کند.
🔹
اگر بین ایران و عمان توافقی بر سر مسیر عبور و مرور در تنگه هرمز شود، این توافق موضوعی جدا از انسداد تنگه هرمز خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/455540" target="_blank">📅 19:30 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455539">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VcfFUpSxzgCBlOYiNUYMkjTgg_Yko2-9m8B7Y5eMmI5FPPb7tuoVr2HCuR_MbGOlbq36BcvSvG83XSMK5UuUcXAhbW89GylilbhhH31w1JK1bi-1vF1yhLuWZ-4p8iCTnxYcMU4ahniwu4zICSSz3bbOXQctMGasKuBT5MfjgZ0BZ374SzDbDyi1Eg2B4lw98HPrrIhEn1xZa2khyg0kiWmiyvaZVY5py8S2UHenmoKzIGGZ9d-9lIPkFgSqiLd35-VcTz9hdNH6msZbN7PSSdqGllzbf6W12W6eDbNKAdk7qIMy0JN9eKUUrYl8WWjlafJK4NXsTO5ZY_3gsCKlXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه: امروز حتی یک شناور جنگی آمریکا در خلیج فارس حضور ندارد
🔹
سردار محبی: آمریکا پیش‌از جنگ رمضان ۳۰ تا ۴۰ شناور جنگی در منطقه داشت اما امروز حتی یک شناور جنگی آمریکا در خلیج فارس حضور ندارد.
🔹
درصورت وقوع مجدد تهدید علیه ایران، صدها هزار مایل خطوط انتقال انرژی، هزاران نیروگاه و همۀ سامانه‌های آمریکایی و غیرآمریکایی و حتی زیرساخت‌های جهانی متصل به اینترنت در معرض تهدید قرار دارند.
🔹
دکترین آمریکا بر جنگیدن همزمان در چند جبهه استوار است و کاهش تسلیحات برای این کشور در قلب اقیانوس آرام، در مقابل روسیه و چین و همچنین در جبهه‌هایی که آمریکا آنها را تهدید تلقی می‌کند، تهدید بزرگی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/farsna/455539" target="_blank">📅 19:27 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455538">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eH0vPXnkPMRiNElpeBspJ2JXc8jSlH1Rn4loueZuyrL0zRok06Y4A4jEa2lntg1upJz2FkuHYlQLMzqDzBPJVDtARmmIIpQvnLOtNqlZJ1h2XYftinCK2RFGTr2jKOCX3hDyJo51EDYTAvEvv56KHtLwv0KUgCzNMrLMYjyTFpydvqaZBdu5_F9GZrtGyELQDoOpUFIjg_3fAevoLai4LYlExksQNSmfL53-qRITV3X7ZIsDJLk_tc9P4Pi-tQkIIHM1nZVIKidjZ7R152JKx9niK6Kw35jpBfrSJsm4lnKQE-br4aDrD9IqS1NhESx9dh0wZWVJJTzaje7qfumlWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۱۰۰ دلاری‌های تقلبی در شیراز
🔹
پلیس شیراز: ماموران انتظامی حین گشت‌زنی به یک سواری پژو مشکوک و دستور ایست دادند که راننده بدون توجه اقدام به فرار می‌کند.
🔹
پس از تعقیب، ماموران موفق شدند خودرو را توقیف و در بازرسی از آن یک هزار و ۷۰۰ برگ تقلبی ۱۰۰ دلاری کشف کنند.
🔹
در این خصوص ۵ نفر دستگیر که در بررسی تخصصی مشخص شد یکی از متهمان غیربومی و اهل یکی از کشورهای عربی می‌باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/455538" target="_blank">📅 19:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455537">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/739a7eec6f.mp4?token=J5VAJxTR3tF1K4Rj0LWbGrR65hFDAvP0GgY5srHLnokR_4wx-u6WAg5z43e8eCnhW83pYOhkTSo79--R26thE5s7YuShaKhIn1PZjBWObAGlp54TXWnph0xcIPFhLqtLsq_hHR3AWi5CTnwxViv8l9USfQZI2fAFaHahniuUlEpQ2dl0rQGJSoVw5fKiGk4sjBQVeiVZoaCaM99Tr3Lr2YtMKbyQgWLfC9sCg3PN5mJpeOWqm3DSxGzUKbj9IqnnRpSTIabR3lpeie6T9D_FpT9HwvD-XesnCtxwTibaqYRJqMnNxRFqwgifpNvf-i8B9UuZbO6TGb47mhZCSLgqhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/739a7eec6f.mp4?token=J5VAJxTR3tF1K4Rj0LWbGrR65hFDAvP0GgY5srHLnokR_4wx-u6WAg5z43e8eCnhW83pYOhkTSo79--R26thE5s7YuShaKhIn1PZjBWObAGlp54TXWnph0xcIPFhLqtLsq_hHR3AWi5CTnwxViv8l9USfQZI2fAFaHahniuUlEpQ2dl0rQGJSoVw5fKiGk4sjBQVeiVZoaCaM99Tr3Lr2YtMKbyQgWLfC9sCg3PN5mJpeOWqm3DSxGzUKbj9IqnnRpSTIabR3lpeie6T9D_FpT9HwvD-XesnCtxwTibaqYRJqMnNxRFqwgifpNvf-i8B9UuZbO6TGb47mhZCSLgqhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیرانوند با ۹ طلا رکورد آسیا و جهان را شکست
🔹
محمدجواد بیرانوند در یک مسابقه فراموش نشدنی که رکورد آسیا و جهان را شکست، مدال های طلای یکضرب، دوضرب و مجموع نوجوانان و جوانان آسیا و آسیای میانه در دسته ۷۵ کیلوگرم را تصاحب کرد.
🔹
بیرانوند با مهار وزنه ۱۶۶ کیلوگرمی رکورد نوجوانان آسیا را شکست و در تلاش بعدی دست به کار بزرگ‌تری زد و با مهار وزنه ۱۷۴ کیلوگرمی رکورد نوجوانان جهان را نیز جا به‌ جا کرد تا یک روز تاریخی را برای وزنه‌برداری ایران رقم بزند.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/farsna/455537" target="_blank">📅 19:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455536">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d86cc18a19.mp4?token=P5tkpGmo6fSH7CguLWLMAxp2jOFfYlfEtJvmEwE5O3ZwUTTJLFf_QyRUN5pAczWkuXkClvZWkD1freWOlUqmr93O9NAYfv8XU-dLWSGJ7PE8lIFN_E44BmoK3cQGqWJ4VUo3e3SZdaikW43pFEnfW-45dq6lRVfjSNOeRtRXDkeokXMfP9vBoNJ-LUJ5jN-oH_c9jmXAKh8ldNm8QNrweQY6Zka97bTkPX8Sr_Ojxvz_w97Hw4_QXFqw5att2ErnRaUu-jGq8-J38RwFaZSQ25-_pFYAnOQKBtXu2saMz5DJhaJNhOjn3hkmnXpSfgTBP2_HakozUhpSHz9kWyQ4NpgqVTQCFOSK1qs-yWazLKBYT67o_dHGz5GTeVMOS0-IOnom32kyhYK-n9p14edYQx-lX40Q-QwcJbA6UCCDZodoQ-bDD4l0Db0ivz_NY-4cidxPwfvuc1lOMqNV8GA9vQsjcU78kl9gorZ1fnlYJeRwjoRzgd0N7UQVw-H5A2yRdwBJJx0cVz5WPFp0MDCKj5L0Z_bOS3dSfRrAWKCrvWIYl7zb3rUhhmkFTbfVpmbHphtZlluM14JEXbNi2LeD3esODmW28CC4zTnpEZAytTaJuMIeQ48zrLmkRoz9dmax7ZRcr7YvsEpS3TxQ2CLRcH3P5xHgVMioaTPq3U2dA-0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d86cc18a19.mp4?token=P5tkpGmo6fSH7CguLWLMAxp2jOFfYlfEtJvmEwE5O3ZwUTTJLFf_QyRUN5pAczWkuXkClvZWkD1freWOlUqmr93O9NAYfv8XU-dLWSGJ7PE8lIFN_E44BmoK3cQGqWJ4VUo3e3SZdaikW43pFEnfW-45dq6lRVfjSNOeRtRXDkeokXMfP9vBoNJ-LUJ5jN-oH_c9jmXAKh8ldNm8QNrweQY6Zka97bTkPX8Sr_Ojxvz_w97Hw4_QXFqw5att2ErnRaUu-jGq8-J38RwFaZSQ25-_pFYAnOQKBtXu2saMz5DJhaJNhOjn3hkmnXpSfgTBP2_HakozUhpSHz9kWyQ4NpgqVTQCFOSK1qs-yWazLKBYT67o_dHGz5GTeVMOS0-IOnom32kyhYK-n9p14edYQx-lX40Q-QwcJbA6UCCDZodoQ-bDD4l0Db0ivz_NY-4cidxPwfvuc1lOMqNV8GA9vQsjcU78kl9gorZ1fnlYJeRwjoRzgd0N7UQVw-H5A2yRdwBJJx0cVz5WPFp0MDCKj5L0Z_bOS3dSfRrAWKCrvWIYl7zb3rUhhmkFTbfVpmbHphtZlluM14JEXbNi2LeD3esODmW28CC4zTnpEZAytTaJuMIeQ48zrLmkRoz9dmax7ZRcr7YvsEpS3TxQ2CLRcH3P5xHgVMioaTPq3U2dA-0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقوع سیل در شهر کلاته‌رودبار استان سمنان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farsna/455536" target="_blank">📅 19:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455535">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ff7ce3cb5.mp4?token=jQgB0IBlJd3QR4E3Ez_8tn7jXdPvwRUfgs41qCVMBvrhMFDToktrsFh0KotVsw_sig82yqXZA8ry9CsCi18PHvsi7ywk9NH7ebxX_iM6d7uNcmQzoPw9eTeE1HvIErBDm8vgS16J0xo2ZyHp8JUTLaMXwvi1sfjlEZEoUhvTMo1ThFdpwz4CT_5v3RGx5qiEXVElC2L9icSXkdfd9U5YTDFNZLDL536txpBfxKEIAg-BWP5m7IggyChnA9BWspyCJN9XqRpSXfAvz0oB6zHL7LGkBrIf7pGlSCXuKYxP6KIZ7_JNBygOznd8ayhWmr5lp9cfdVLqQQ6aNO1kZiDA0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ff7ce3cb5.mp4?token=jQgB0IBlJd3QR4E3Ez_8tn7jXdPvwRUfgs41qCVMBvrhMFDToktrsFh0KotVsw_sig82yqXZA8ry9CsCi18PHvsi7ywk9NH7ebxX_iM6d7uNcmQzoPw9eTeE1HvIErBDm8vgS16J0xo2ZyHp8JUTLaMXwvi1sfjlEZEoUhvTMo1ThFdpwz4CT_5v3RGx5qiEXVElC2L9icSXkdfd9U5YTDFNZLDL536txpBfxKEIAg-BWP5m7IggyChnA9BWspyCJN9XqRpSXfAvz0oB6zHL7LGkBrIf7pGlSCXuKYxP6KIZ7_JNBygOznd8ayhWmr5lp9cfdVLqQQ6aNO1kZiDA0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مه و باران، مهمان فیروزکوه شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/farsna/455535" target="_blank">📅 19:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455534">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef65b9ea68.mp4?token=JtrxUgEKBSmHsTJFy4L4N3pfJnYhDOevTM7TIRgnpMyvgMlo3J_ZMCx_mLNuQjVtpNXMX2d28lw6Nv6QI1GzUKo2j_bne_FeMN2usCe0BE0YizOkhNbpYv9f2FaaSMNV9AHKV1Q3_vOFL0ogJyXM0QFcGzxt_lZ73OUhcNO-hoMeMW6_3zp551e-XBto6iTt7tcpS4O5IWPXEIgQT51NXeo3m-DbiJTrzmFZHk_jXGqskdf6N70WL7pQOfcjIKvMmw9RkUCcrhwiBJ6ouS6Krd5m4ypnM6ne2pYsIZzmqmnt9A5mGENVJfMaw1GNBglBeB7jVcQ1rE9WawAJ620Wvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef65b9ea68.mp4?token=JtrxUgEKBSmHsTJFy4L4N3pfJnYhDOevTM7TIRgnpMyvgMlo3J_ZMCx_mLNuQjVtpNXMX2d28lw6Nv6QI1GzUKo2j_bne_FeMN2usCe0BE0YizOkhNbpYv9f2FaaSMNV9AHKV1Q3_vOFL0ogJyXM0QFcGzxt_lZ73OUhcNO-hoMeMW6_3zp551e-XBto6iTt7tcpS4O5IWPXEIgQT51NXeo3m-DbiJTrzmFZHk_jXGqskdf6N70WL7pQOfcjIKvMmw9RkUCcrhwiBJ6ouS6Krd5m4ypnM6ne2pYsIZzmqmnt9A5mGENVJfMaw1GNBglBeB7jVcQ1rE9WawAJ620Wvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت نیویورک‌تایمز از شرط‌های ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/455534" target="_blank">📅 18:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455533">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8CbbWL8Yh_esk64i0mGvlFOpXgdCwJpdnVcMKZbHy8cF5LYlhX5xyvvle9hwOGkn-bjrk5MMwBik9P4G6c8n_NCpRal8H8luDDWshv8pZlZZfH2Sqqmkdag0GtoGrxDQkirA3GAPuJclTKlyKVFmw3uMe7V5fMPFmyPwHXrDBFpt0_92QBL3q7XO_w0c9wyQFzl0qYxhjA1w8shgsNGfywYq45T4x-Ti5kR2ZJJy82lHiZFrrqczw5M-EIxpDAvItM7eG6omoClC8kuI6PVex3RcuAew-5D7LV3PC3llsNTsotgxcfUGzu6AVqr3ZIYWkzXV0cGw7KGXPrQEIdC3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
رومینگ ایرانسل، انتخاب بیش از نیمی از زائران اربعین
🔸
تا پایان مراسم اربعین ۱۴۰۵،
بیش از ۱.۷ میلیون زائر از رومینگ ایرانسل استفاده کردند. رقمی که با توجه به آمارهای رسمی از حضور بیش از ۳.۳ میلیون زائر ایرانی در عراق، به معنای استفاده بیش از نیمی از زائران از خدمات رومینگ ایرانسل است.
🔸
تعرفه‌های مقرون‌به‌صرفه، کیفیت مطلوب و دسترسی مناسب به خدمات ارتباطی از عوامل استقبال زائران بود.
🔸
ایرانسل با ارائه بسته‌های رومینگ، امکان استفاده از خدمات ارتباطی را بدون نیاز به تهیه سیم‌کارت عراقی فراهم کرد. بسته هدیه ۱۰ برابری و ۲۰ درصد تخفیف بیشتر برای ثبت‌نام‌شدگان سامانه «سماح» نیز تا پایان ماه صفر در دسترس است.
🔸
استفاده رایگان از ترافیک «ایرانسل‌من» و وب‌سایت ایرانسل برای خرید بسته، شارژ و پرداخت قبض، بسته هدیه روبیکا و تماس رایگان با سامانه ۴۰۳۰، از دیگر خدمات ایرانسل بود.
🔸
کارشناسان ایرانسل در نقاط مرزی و مسیر راهپیمایی، به‌صورت شبانه‌روزی در کنار زائران حضور داشتند. همچنین توسعه زیرساخت شبکه از ماهها قبل از این مراسم و پایش مستمر رومینگ برای حفظ کیفیت و پایداری ارتباطات انجام شد.
👈
جزئیات بیشتر
@irancellnews1</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/farsna/455533" target="_blank">📅 18:56 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455532">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MnEnb7ZHxFUViHWTDHkrltaGtrXQsz7S5YX12JPZAPOCk6lXtmU4gNpKiKBlRBkoGW1QvvGmam5guxudFno0RCAqz6ndInDvjhfVhbgPSJ_IZmxhu92vvUyvW7ZVlcUe2o5Omw2EFgM_Hq4igFLTwnhTVD-3UiwQZIeJqxRoiyhrG2_vP7UufZBJ9PRaMcvpoXIsIYuk03kWdboS-WsJnzTm_Mit4owcj9FQA77lqTVGTsPr5hNvNCSE4tK37zssNIVl09EpYQ8khA0yjTLE3dASFSum8_frOil4UKDU1wcbNhV3SsVZym2xEgAWkcMzJgUcXUQSRlEOefCGRcuSfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔶
پارسیان پیشران حمایت از جوانی جمعیت و تسهیل ازدواج جوانان؛
🔸
پرداخت قریب ۲۵ هزار میلیارد ریال تسهیلات ازدواج و فرزندآوری توسط بانک پارسیان در ۴ ماهه نخست سال
📎
جزئیات خبر</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/455532" target="_blank">📅 18:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455531">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/455531" target="_blank">📅 18:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455530">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cE0RwbPFzIELEyWU6WHgK8H3tBPRsYmBU3r1lRkQiQDk7rhOCJthh10bwOMNN8FhE5O-mLNlBOB9qfD427ccvTb1crt02aPcynTR3pzATClRrPsHsEOUZcXOHhjgD8GG5K3V0FuMvCigKDwqk_H0nPu3AZjOCzDtIGGWL2tmQiUTzNmGTXK2Ni273d7qnEwg9IJoi-kJt2w4xFGgjz5oQ29L4NcJ4PTnzxj7mLoqxBcqHiiw2nESAUk8_pd2kRj2jjxGQJOFegxrhHZdeSEP7WpoHUlI_zjYa7U_lDF9ED3_UIPmX0tBkXo9MQ01GGpcSXJQSgzrIVNpyQGukGytJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مخبر، مشاور رهبر انقلاب:  تنگه هرمز باز نخواهد شد تا شرایط ایران محقق شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/455530" target="_blank">📅 18:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455528">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b5cca6996.mp4?token=bcOBTl_tjFes7JvdagKwTSsAsM3quja2MOrygTHym8gj7y-76LpXuNly1gci4GAwibFbfJJfoNDxajTJoYdTmiG1sQc_uDDw6cX-4Pkp7qwIb20AJqejxZfQ18FdniX9IIrNOh3_XlHTkSZr_hpPPEBX-JWFnHQaGhBxuvg8w58hso8AgNYW5zXJy1xrv4dr9PxSiTcVbIXe0vZjGOzfS9Crk1v5rTqOlS6bNNYoqhy2uSnC9IvB6Taq6q_YX1SjaDDqEAyqL_NbqWzaxQNnD8l-3A-tiSETSxHR1eljNgC2uDv5rZMU_qXf2bZkX9RTgrWnPwziDweWowMUcP_FaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b5cca6996.mp4?token=bcOBTl_tjFes7JvdagKwTSsAsM3quja2MOrygTHym8gj7y-76LpXuNly1gci4GAwibFbfJJfoNDxajTJoYdTmiG1sQc_uDDw6cX-4Pkp7qwIb20AJqejxZfQ18FdniX9IIrNOh3_XlHTkSZr_hpPPEBX-JWFnHQaGhBxuvg8w58hso8AgNYW5zXJy1xrv4dr9PxSiTcVbIXe0vZjGOzfS9Crk1v5rTqOlS6bNNYoqhy2uSnC9IvB6Taq6q_YX1SjaDDqEAyqL_NbqWzaxQNnD8l-3A-tiSETSxHR1eljNgC2uDv5rZMU_qXf2bZkX9RTgrWnPwziDweWowMUcP_FaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملهٔ موشکی به گروهک تروریستی کومله در اربیل
🔹
امجد حسین‌پناهی، از سران گروهک تروریستی کومله اعلام کرد که مقرهای این گروهک در درهٔ «آلانه» در اطراف استان اربیل عراق هدف حملهٔ ۳ موشک قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/455528" target="_blank">📅 18:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455527">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bifGI32aiw8bVnE8jIAHSiwnNRITGRFXHmBGewSVlU6UhjU3vwftNn2Cd6vIjJnhEQXBQoyipXYJ7jKZf7ELHhbBfz8oXERgS880apLmYAQVPTkCyEXJslq49LH0P_6r6kNlTXndYilSuCQWLr-8ghqLYRtxuJhuUuNpIQh28PkcP1RELUTyZ6wgsxhg_zb6MgcX9ymXv6SLHJf0R594f6bk8zIGiMttStnZVTPZt4UaYkLb7hdQijWfIWokS3mi9jTDiQ4SOo144vv3gec7LjmiTbeXlZC4khN6yBVQcsRFa3m1uHxk3KEgt_IcbV5Za0xhH4iX3-cH1PS1nP3Z8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ولایتی: عربستان از سیاست‌های پرهزینۀ آمریکا عبرت بگیرد
🔹
در شب شهادت پیامبر رحمت(ص) خواستار رفع محاصره ۱۱ ساله رکن جنوبی جبهه مقاومت، یمن عزیز و برادران مومن و غیور انصارالله هستیم که با ایمان و اعتقاد راستین از امت اسلامی و غزه مظلوم دفاع کردند. آسیب به آنان، آسیب بر امت اسلامی است.
🔹
غرب آسیا، نه حیاط خلوت غرب است و نه میدان نفوذ هیچ قدرت دیگر.
🔹
عربستان نیز شایسته است به جای ادامه فشار بر یمن، از فلسطین و آرمان قدس دفاع کند و از سیاست‌های پرهزینه و غیرعاقلانۀ آمریکا عبرت بگیرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/455527" target="_blank">📅 18:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455520">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VjsTeauU4LOp2artPma5txyKQuQ4Pici7jTKVO6LfOfdIETMo81mga9KNEhbSZAl-Sx2_Mbw8VkO3Vdk05WGoP6JdS6G-1Db714sAFPL880Nq7nV5bEJ12AmonKstnfWWdp7kv3LG_IHlAs6cBmCawDeTSXZd5AyvS4dMxeqYanFZUqAoCJDU1S-ATeXUEdq8Q6Ko8bgfp0EUj7JPMzeo_wAfoCQuFxgc0CMN5d-OjXEMDN8xw-iWYBQl156t6xfaE6A1nBHux1D2e6D6OUd7IDSmMMPFmXGc9ce45jp1o-E8bMurXzfqFBIRwOUPmNkR2VxnN68alEWoXUkHGl6ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NAdzvkWI0Kh8Dy8K6vnTqwmCPc2pihbVaVBIsSojxEkFEC79o41eUjxv2WNr6wNG9_tjkrFN-nD2Y6CDjvOh-iatTK-flxte7cyNZT8MDHW0qkVMKeZegh3xQqU0p_SIkpBD9VH9he0rc8IfxnxrvqNGMWgMMjPpMHUGefBx_1wuhAh1tuAuMwuUF0PugFt9z802KOjQjBbpTFOVrX97U2-V6gGKQlvq1vKwXJn3vbGm7AZh7ZJ-qhHBa3XjS-6P1gpwc75iD1AOhbft6ogY-gvCyyohXHK86bpLFmyPh5O_W26dXeAVOJCPtRkJ44LPfv7S0U5LealYujp8hhdDyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YTKA_XnDwQ43wk3MOcvQW1AwauJqdihaZ5VCKgFyifse4hrkznKHsyn5Lp5g6eZ9T_lYsi90jbJQU5GqCTktxq1t0nU4QUQ9Gfywyd7hmENGIIVCZFcydeF3dR-aihoWtNQG6SVQgxX0qPTFs9ZJPyljt9zDrMwou3UUsY2ByYK2QzikO49ZNb5ygAxt5xzGMVQYgPkN3MOxiSBBnajq3dJCTvSYhnGI152iuUSZY2-K_p5YMZKYL6EMdE3rZUvm1jdtEyRAIS46uaFDuZ6bBMpvtRQJTPmIHzhY9xgyQ-e8mhl0UysJbkvsJoJGpA3xl7Pl7khFOGhpU3nc7PC3nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fk-2yPG3LgSWChg49peMuQ_F5OKCLiAjiR1Az3ezM0bbqfiXfvP1BVoL7EDpg0zkaL6gDM6AmucbezuiXm6wsCk0sexy9eL2hnDKjnSNzW7pIjtOY4g9sHweo_Owg0sSdVJgPQeiuq4oOh4eBR_5lHTuQeo3nQ_z4gnu5X5sDtyiLor1nmACJVEBWUfQUly73j-04A9jumAQuH_OW4fo4J2ZQo35PGNgszAsG2js3nE81kWK6TnpGiza9LG6shdVX-vwPWfhajyiLy2nk2n87y4yTre5H2_uRv12ehxfq4acXyvdMoc5zmJ-X9SbcTdvmemlCnBOyd5wVgG2m9OBAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oJGlK2OZpMONkXrA9z0GIb7QI0GZmOVz1BUyKRrg85F2Z6C6bzRB_JZ93kZ1az3dSYUTD8p1lNy-4KiyBZSl427IZDycsvlnq0Kcu9DOR1XD3PyU7cIjAs2YuoljKqryqTDLWBZP9TQ2mKgT2AMdY8yOkNbL6fZG-Y3-3jnvZyPAysxxTw1o8E2RAXbU_F26JGq_TKEps---EjtHyWkx4btHqRm_DyEjLee5A-UQB8rr76XpH06XGAI7alu5HTEZVnT9VjEXpf9aEVV4IM3xUO-ymaZbyESGe6Cvlk1ntE08kblx3YSc3Oyxmoqz69cG73ap1dh3Mh0oZqho06tydA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cg-OduErap5xCKTNqHr0BHtflNCj-BmJZcJmqvH9gH9A5AalWFTfq0NNpQv3TcboyOOJL2OIG9zBefIipScRk0alrwMMdedTQLTrT8PBY0rlNaqn5JK-Rmp5xc-fu_zqmA2S7KjXZ7dP-V8WjQM8gsw2keHs8IovPM-zMpEr78hLuoYu3gn0Z2RZVAzmle_dI9FqtXfLxc637yvFx1_kYUzurTWEB24ayKXCmKzXQmtegA9B1wFWMH_IChslv2piyFJebhbK2tgjFcPeBPDQZ6ko4rGdzRWj878DpUGrvulYYGt8a4aQGHZDR3fMIRATZX0MFrm1EZ9yw7oTkfZrQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UeW9MjsvE9iuGtviiRv3Sf-iCzN7FlFx0WuyU18zieuCvki8Grr2LV0zaEtQcmGjR5dDog9D7xZo58z7XLGmzZnRXaILlhCLUMvCFpvQZ2P_cpO5JWeGO1tnFitu-XguBcijhm190bboQjZiMUVU82g12dBxg7H7Y7v2gpH6rC8IzfmExadkvJJUTAGDbp9dFRnBaYL6ScrCtQ65vR3H_3sMeYv_Jg7uG5hycecXq7l0lzdclRQyJTbO3lCCmmXliJ3STsoPLq6RnKCjfkVYaT_iSU2ENCDMMuTQAQ1W3RQ7wJXnChS1vsNbTQr1chmkY6LFiLFf2AI5vTWVpFACTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تفاهم‌نامهٔ همکاری بین وزارت بهداشت و وزارت خارجه برای بازسازی زیرساخت‌های آسیب‌دیده در جنگ، امروز به‌امضا رسید.  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/455520" target="_blank">📅 18:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455519">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDBzSX09JllCtfCeWtmIKpkomZjX_N-HEPzEnLfpNurWTAVN1pw9P0Etrd9rCvUORk9UPvmeIvjRyfJdE9osbxhk08VbXIUHZiR7qOm7XSZ6V-LRinRV0Lv_WZE9FA-d5dCBVOTSAw8TzwR-ujYrEbku3X_aaJZvWhfu4EEfRbzeM8dmSBhudWNhJ9Kbqxl1j_HEHTRnnbUGERqP4d5SIejZzyTHj65a0xF4RBf4WEo-u9G7MYgEvA0aVa8QNeAv8uqkfj-vSeOSpX-829jbCVabUp9riEQKs86pt70UOe_l7KXGUPZRAaiwkQd8cWcsp4M1vY3GC1i5RLhEVSlFfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر انقلاب از سرلشکر عبداللهی، رئیس جدید ستادکل نیروهای مسلح چه مطالباتی دارند؟
🔸
ارتقای توانمندی و آمادگی‌های همه‌جانبه و روزآمد دفاعی-امنیتی نیروهای مسلح و بسیج مردمی
🔸
فراهم‌سازی امکان پاسخگویی به‌موقع، انقلابی و مؤثر به هر سطح و نوع از تهدیدات متعارف و…</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farsna/455519" target="_blank">📅 18:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455517">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SBiUEmgOq6tXDHVXJBLeOY2Y7Sdf3XsKFAAl8LQHjMfb_y7bIcmHghGWR6-k6BZdHc-xWCHTPYPlYzpGa2CjSY96PS-tLeQP_FsGbp1jRGhz3As0nd8xJm8GnFtDhTADVfWKqEaEYo4Oo8Kx_C7rdRqmeYt2gRYRLU58iTvwXm0Nb7RI1Ywl2yx_PfZW02bS2GJKJSVJeb47gbTO-DKfr7YVTjciaWLGO_pG_xg9Tzsu0BVRlVEOkScHnmAd8MCwZySciGaG7su7c1bqFVvbtmqe13yq9BKHW5cKfIcD3W5ftVbVTd0RflMO8u6BeWNjsUYde_iU_n6EJcyW9Z0IjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JrWi_IWTlwedBz6UbIcAp5YqXAXL-jm6cCCYWDH14eJOzoq1YaJGFr71cJJURSTuqJFlFZhep173vMjPOe0Jdz9kjFDn1usRaXRT3i4fPayo0A_9OKgoiQzaj9fwyMMZDtzekOSKivPgZpi8q8b28DOK8_fBxUcAHfmOfRIcnYbLeHW9xGG-L2SU9GLfAJYmIdrSH3gSEQQEf5WfdHCCqItb2_TMYs4XcVl5HDpRhPvFPtf1jZhOCk0Zns6l89tRpmzBgmfbcYNxBQR_ZLLVB7DoQtvTteGbSislzzMG0AKzhgMCOnaQKOd60M3nNsxS_37j5g0IdnhV_kUddTFoYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
وزیر کشور پاکستان با عراقچی دیدار کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/455517" target="_blank">📅 17:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455516">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdf3c21c13.mp4?token=lI_9EkdMK6XJt7lXobMDPFr89sOXWc6HawNIMb8I6hu1HH_TD79ZDJg7EFgnhWI2eMK0uFXA7uOaCXlXDm-bMGGoSqWbQgkFcWSbya0Z1dWA4xNvYqk0uqoFU-PHSZPEPgz9DOgl9d2RWZspvfTOTuAYnQTPHQyAUhGPAFVktQWpvY3If40JYIqVKW88PLPjGYKIzxcBydAzGvphjiVxkUe3KASkSacvkh7J6SxmQME27RLk_4zxSbBPA0ZbHXuwgTUq5lnXjnZqAkSL5jFOo2YV_x1ux5zrc_zJOXrqSXbvF37SKNfT3uGsOBhbx6vUGW6p_BW5SEfhlIxxK-eaxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdf3c21c13.mp4?token=lI_9EkdMK6XJt7lXobMDPFr89sOXWc6HawNIMb8I6hu1HH_TD79ZDJg7EFgnhWI2eMK0uFXA7uOaCXlXDm-bMGGoSqWbQgkFcWSbya0Z1dWA4xNvYqk0uqoFU-PHSZPEPgz9DOgl9d2RWZspvfTOTuAYnQTPHQyAUhGPAFVktQWpvY3If40JYIqVKW88PLPjGYKIzxcBydAzGvphjiVxkUe3KASkSacvkh7J6SxmQME27RLk_4zxSbBPA0ZbHXuwgTUq5lnXjnZqAkSL5jFOo2YV_x1ux5zrc_zJOXrqSXbvF37SKNfT3uGsOBhbx6vUGW6p_BW5SEfhlIxxK-eaxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بر اثر زلزلۀ ۷.۴ ریشتری غرب کلمبیا، تاکنون دست‌کم ۱۳۲ نفر جان باخته و ۵۷۰ نفر مجروح شده‌اند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/455516" target="_blank">📅 17:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455515">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdxz60hAXMNBybkbkMaQMWIEOoeydVc4r5ICO6CZVFTjmU1TeRJXXQW90FSeWFALoYwuVteV1MfXM97M0Pp28US4lTsQV4TcvuGyuNQdh46QgPfLgBL5NbBKIMp8VrZVnfvKHSsVm9seFCwyvfWgthtnhHQW4s-0938ucS5yWEeMSZKt94lCg_KeU8jgXv6Sx6N3PqQuM3DljMbjWbS8qnU75UDUz9yVm-dxiopLaXsU-OYUqvl7Ft6-OPCmHi3cmZ_vGtEeEn3TDNFAX2IIuUZGNqhOuLjd9o9hmgpRg4lVRXb58DWg7o278f7JLTEpVwDYqzu5OCdBz8oU2gODxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر کشور پاکستان برای دیدار با همتای ایرانی خود امروز وارد تهران خواهد شد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/455515" target="_blank">📅 16:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455514">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQ3IJT-_zXy6ee847MiVHTR6tc2cjRTgMv2_hDgRi2a6zlzvfQvWzoALrsbDn86ZRUeLw0IC2SPtUmtx-FwCFfDJ8PTtAp8M6n8u_VSciMrK_lkYcTh6ooRYewdL0ojlJMrdd3pRFQ3gJ36uzgKVV24ufP3Tw2vsUBk2TiALqwgQE_P6iNXPmjBZx1GZKdZoTcTLjCxjByyXurQO4Ap0wVjdp87HxMLQctd3xNYWuAUjh3DElRtExiqPdi2hjlLKe3xpLqndczzaaEH71E_R5bZopFfk1a2Ms7t1_TBV4m2bsnTXOo56BOLuZ5Zw58Rc6XcCJDPrFmEb2sgIMUySsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌ بانک مرکزی برای شرکت در اجلاس بریکس عازم هند شد
@Farsna</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/455514" target="_blank">📅 16:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455513">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mY3ahZghFS463bmCNbhu8EzR7z9HzTsykxg2WxzPizcuHqCTZvsu-1thHCBePuYOZi2NbeDAY8yslcG5xPYx2LXv9LCx0fXhge0uNI9ngkhEVqr5XKA0B7zpkfdzdDZ4Qz5IrhDsYVp63Gd6PaxZZwN4AZIw6WziuOWjFhWxgpxVzc0BGEsf8PqfdLzp-ARz-cDZr3ipNVpOEjrDviyMtB0DcnoE2GC-f3h7x2H-LvE0yEPaCqNdpHQzi4jJLlUzUPN1d6Qc09dGIzh6crTfJSWKkEmikiou_JfBxTnvgw2K_rErhK1pmapMXtuid76fjAXEsxiGcPMsU3zY_34ERw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار ابن‌الرضا: زیر بار حرف زور نمی‌رویم
🔹
سرپرست وزارت دفاع در گفت‌وگوی تلفنی با وزیر دفاع مالزی: ایران همواره خواهان برقراری صلح و ثبات در منطقه بوده، اما این صلح نباید به معنای پذیرش خواسته‌های نامشروع و تحمیل ارادهٔ طرف مقابل باشد.
🔹
ملت ایران اجازه نخواهد داد دستاوردهای این مقاومت افتخارآمیز با فشار و حرف زور نادیده گرفته شود.
🔹
فتنهٔ اصلی در منطقه و جهان اسلام، رژیم صهیونیستی است و تداوم جنایات و تجاوزات این رژیم یکی از عوامل اصلی بی‌ثباتی و ناامنی در منطقه به شمار می‌رود.
🔹
وزیر دفاع مالزی هم در این گفت‌وگو گفت: مالزی در کنار ایران برای کمک به برقراری صلح و امنیت جهانی قرار دارد و بر توسعهٔ همکاری میان ۲ کشور تأکید می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/455513" target="_blank">📅 16:42 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455512">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTuG8wkMYCMfBnff9gAczd6fA_l9Cch4ZA47g5Eq17hiyPEwdXRQz8iGXJPVnZjsYSwK_PsyrHw19SDt7oPI47UaKygOQhRFEX6835ZH5DWgqiFD8WLllqNyy0JU7ok5ehjfxHpd8ABoXrLEA-Py9XQIe2yU_Ri921EIImNUEM2rrl3zLq_gMLOZzQuW5eKfKt6rg92HiLTKcHyNmhd38hLFOq2hXpzMFBa4iFIk0I-_gQvH2Vv_3kDeztIyZBCyIcw7BZsGsxtQ3KwUZfeCnbS7kdUGcYflqinRkXNlRjDfQFxJ_XICzvnDJa4DZSdM97cdRn6TsWnMpM8OKB7H1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر کشور پاکستان برای دیدار با همتای ایرانی خود امروز وارد تهران خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/455512" target="_blank">📅 16:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455511">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-n6tXyaPC8IxiKmYhfZgPlYuNfuGWBGFE22p-0YGLWaLXMDBIwfm5pXRJwiG-6pzjBFj71ZcEUz7rxruCONzw3Aec-k3f_LhT-G70SE8QAs1hrijV9BtxrAjqzSjl3AjigeWu2PLwPXebzeyM_gNCnAZXKIsy3osnDBLi6jn_Tc6Z_yYWg6M4DiUv_rjRt7ZDR36dOELt9VqxLVQ9FEc_0H-vSoqCmghS-7D2yewRrbyNcQ-4ke5KJN9hRg9bcjvmcWkGHIH4iA6Jrj_O8T72Bt3n7hnbjsLRRsqIuCLBHCoJXaP_TiJTPgK7zcJ73iWkLy7FNX0xth60qYajPZaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر کار: نقص اطلاعات فراجا، کالابرگ برخی افراد را قطع کرد
🔹
پیگیری خبرنگار فارس از وزارت رفاه نشان می‌دهد کالابرگ برخی افراد حاضر در کشور به‌‌دلیل ثبت‌نشدن اطلاعات ورود در سامانه فراجا متوقف شده و وزارت رفاه پیگیر اصلاح این اطلاعات است.
🔹
معاون وزیر رفاه گفت:‌ افرادی که صرفاً به عراق سفر کرده‌اند و پس‌از آن به کشور بازگشته‌اند و به کشور دیگری سفر نکرده‌اند، اطلاعات لازم از سوی فراجا ارائه می‌شود تا از فهرست افراد مشکوک به اقامت خارج از کشور خارج شوند و کالابرگ آنها مجدداً برقرار شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/455511" target="_blank">📅 16:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455510">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‌
🔴
محسن رضایی دبیر شورای‌عالی امنیت ملی شد
🔹
معاون ارتباطات دفتر رئیس جمهور: با حکم رئیس‌جمهور، محسن رضایی به‌عنوان دبیر شورای عالی امنیت ملی منصوب شد. @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/455510" target="_blank">📅 16:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455509">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pw6HjbiNHK6xFw_4lfZqOSxhtNvy46FKiTkbLzL1w4OBPJFO2neqgl5DJs-eymsRsfYEAF4aOkyPTAo6Dwe0jRsOkVK4DELXlsggk9q36m6tAypJcivephOCC37hhhYlTZ4aN3lIw5xx08e507O_Xv1MZhPAuPfS39ZWaGu-qHBF7GeODiCxU4klq2L837eohLuGF_xpWu5BGa38TvgDrXyoucDWP29FsqGHjJ9L92Cij8IMKNp0dvX7qf60N4pzza8CWCLB2-EFVw_9ch6ewO7RPOJanCdZ5o6gB6ANCcU57XE2hHc63vmPp3rK75FMPOoz_StG2yquakH3gkfY-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهردار بوشهر برکنار شد
🔹
اعضای شورای شهر بوشهر با رأی به استیضاح شهردار، به فعالیت حسین حیدری در شهرداری پایان دادند. @Farsna - Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/455509" target="_blank">📅 15:52 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455508">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🖼
پزشکیان در پیام‌های جداگانه انتصاب رئیس و جانشین ستادکل نیروهای مسلح، فرمانده و جانشین فرمانده کل سپاه، فرمانده نیروی دریایی سپاه و رئیس سازمان بسیج را  تبریک گفت.  @Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/455508" target="_blank">📅 15:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455507">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMKgqUy7SRwy5Fs2j0EnMSxbyaCUIxFMqhqwpi-LAGH4MiGwLaqQcgtR2pjNIk_IjiSI0awWNQ6WDZFEFINUKVW3SHnsL0JbaAVHppcuNcyCEwvtHjgE6pku9lnZS5f2kY_B-ncpFLwTx2BggUwPaB3pMNcE39xpUMBxJ9cF55tHUrW6bkQ1pHVaXcPluJFyAoYZMPxOfWEOqUPbjlnNO1C8d57D_rEArsRF1efNBHmOZyACumjUnWuqnFrrZw4GVK109Flyz3jYq0x8YifPTMvY1LWV6CKDXA9wKbPXBAKkswHE6dasoTgdx1B9dFL3vflZF42vO9d7uEwhRTNhyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاود روی متن‌هایش ردپای نامرئی می‌گذارد
🔹
آنتروپیک با افزودن یک واترمارک نامرئی به متن‌های تولیدشده با کلاود، راه تازه‌ای برای شناسایی محتوای هوش مصنوعی ایجاد کرده است؛ نشانه‌ای که در ظاهر متن دیده نمی‌شود و هنگام خواندن یا ویرایش آن، تفاوتی با یک نوشته عادی ندارد.
🔹
نکته مهم این است که این واترمارک هنگام کپی‌کردن متن نیز همراه آن باقی می‌ماند و به این ترتیب همواره قابل تشخیص خواهد بود که آن متن توسط هوش‌مصنوعی نوشته شده است.
🔹
مدل‌های کلاود که از ۲ اوت(۱۱مرداد) عرضه شده‌اند، از ابتدا به واترمارک نامرئی مجهزند و آنتروپیک در حال اضافه‌کردن این قابلیت به مدل‌های قدیمی‌تر است.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/455507" target="_blank">📅 15:48 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455505">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9bUE2P4jdVh-sSPQ4G0P1z_KvXzVn0-KdykhHFyCOEFqUlHfNJDpp3WNoTSpBTSblqnS7GldGVfYuBR2N43SQuPGkqtWHUId66YktgpVLl5yMX1D2eyJu4EP8_Wj-whNrwZOfIoRlMMkmq39K5pxKPMH-mWHDEKApvEBJfIUQHIV0X6hDpKPmT6afdc1N9I8UpYXk_1JyjcSvi97okz0qJTG0htLYAnusaP1vit_aAPSibV8eAbAwN9E1UmZ3cjd6xbaOb1tGMZADYGjX6DWaiHQWUcbHA-5KM3B0bX8lrLchFRWkKhbfrUz-U1VN1wAW_EpeUR38uJflEQsOwJLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
حملهٔ موشکی به یک کشتی سعودی دیگر در باب‌المندب
🔹
منابع خبری گزارش دادند، یک کشتی تجاری دیگر متعلق به عربستان امروز در تنگهٔ باب‌المندب هدف حملهٔ موشکی قرار گرفتند.
🔸
این برای نخستین‌بار است که ۲ کشتی در فاصلهٔ زمانی تنها ۲ ساعت از یکدیگر در دریای سرخ…</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farsna/455505" target="_blank">📅 15:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455504">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cd10ae97a.mp4?token=tVXmgWm5OHkYHcY_SUvyeWr5oeN7u5Pod34Cqe9ic0i0WNmu3n5RB_jkgDyjBq01Wu3uXiDsFgFKTI1TBuVLodHuedag0Atdxux42XvjfdhfFofgqOik-GCKdOfksk0U2aQ2pbh3UiHCG63U6Yp__3MZEDxal4_5hgZrEdbaktUDa0Qn3zrZCbx_f-JUcXwehNBvrrIPkDXA1_QLi3VjtR05nPtVNsUnyQUB1apWmPkWi-MMRI7KYNnMBnF8ejDT0gRf5RtUMnNJdHs08C7Cjd-LBiRF14j5RAlqCx6vUHJ7LYZoRSwHNg6xRcySiZMbKcF9n-0-5kyZ4Hz849i1wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cd10ae97a.mp4?token=tVXmgWm5OHkYHcY_SUvyeWr5oeN7u5Pod34Cqe9ic0i0WNmu3n5RB_jkgDyjBq01Wu3uXiDsFgFKTI1TBuVLodHuedag0Atdxux42XvjfdhfFofgqOik-GCKdOfksk0U2aQ2pbh3UiHCG63U6Yp__3MZEDxal4_5hgZrEdbaktUDa0Qn3zrZCbx_f-JUcXwehNBvrrIPkDXA1_QLi3VjtR05nPtVNsUnyQUB1apWmPkWi-MMRI7KYNnMBnF8ejDT0gRf5RtUMnNJdHs08C7Cjd-LBiRF14j5RAlqCx6vUHJ7LYZoRSwHNg6xRcySiZMbKcF9n-0-5kyZ4Hz849i1wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرا محسن رضایی مسئول امنیت ملی شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/455504" target="_blank">📅 15:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455503">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJHP3b2OpqOHDQdGxA5FihThXR6kiWacUFkluwRohHV2JpXbQbvLhhhBVYipPbtJeOPoXVazefqWbDMX9k7Zc4p9LKOM5Uw6gZyTcBzDAENEquJRTWWgcpbcdy3VBQp0HBTHH0t93gpTwZyRURC4FaV3EUyiCbZicB7EMJ12PlIezSmJr7dpnU8FQKWeweTx8uKW23oweOHKVrxysoUHheGQ1w8dVQeaM0LbLet1NnvWPFzhxDMpDTS5DbTCYp_ssEjF5Hcdidwu3maTrmFxTprho9pmji9nBr6iQMWNjOTLz6peX3MVfkKHeuopPIiqs9hz-LzZ63Fg9UIqJ-H7jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم: کنکور سراسری در زمان مقرر برگزار می‌شود
🔹
برای برگزاری آزمون، هماهنگی‌های لازم از تأمین برق حوزه‌های امتحانی تا هماهنگی‌های امنیتی، با دستگاه‌های مختلف انجام شده است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/farsna/455503" target="_blank">📅 15:30 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455502">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53ba1afedb.mp4?token=voMW-UTlmHuY2htXSkkHYligYcg7Y1e-7VLPhHnyrbXhMCm2S94XkKIFpQpbwftdrP2Z1paYi_ulJ-c02ezmLLQPJppILes7KlBfjeeWhNi8T5EbX280gNdG21nS7cHCCnaFgVb99w8mmzkJtY_Pl4T5DF54_DQaullI60MNtoeejOKcX4rlpWlI15lFyny157_NvgjZKDeaXYpIZZfVwAMpJQok-dlaEn-FwSZFzBfsoh1o6sO3uy9xdnu15ZWR7a2O2Bu-nfaJVOyvrAQ0kRHFVZGmXuLgG8jBvuaE_EbeWMP-NOXOpdk_F17LvK5bsrVe5mOZpFa9_wMdiQ6SNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53ba1afedb.mp4?token=voMW-UTlmHuY2htXSkkHYligYcg7Y1e-7VLPhHnyrbXhMCm2S94XkKIFpQpbwftdrP2Z1paYi_ulJ-c02ezmLLQPJppILes7KlBfjeeWhNi8T5EbX280gNdG21nS7cHCCnaFgVb99w8mmzkJtY_Pl4T5DF54_DQaullI60MNtoeejOKcX4rlpWlI15lFyny157_NvgjZKDeaXYpIZZfVwAMpJQok-dlaEn-FwSZFzBfsoh1o6sO3uy9xdnu15ZWR7a2O2Bu-nfaJVOyvrAQ0kRHFVZGmXuLgG8jBvuaE_EbeWMP-NOXOpdk_F17LvK5bsrVe5mOZpFa9_wMdiQ6SNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فروشگاه‌هایی که قیمت‌های قدیمی را از روی اجناس پاک می‌کنند و با قیمت جدید به مردم می‌فروشند
🔹
رئیس تعزیرات تهران: با فروشگاه‌های زنجیره‌ای که اجناس را با قیمتی بالاتر از قیمت درج‌شده بفروشند به‌شدت برخورد می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/455502" target="_blank">📅 15:18 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455501">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a33540e9c.mp4?token=BOxz7BVSxtCImBG0zcG3bsP8JhxQ_LFnsjACt8_FOI906mVuwgxCZ5-Mu9AnwgNb92OnYqjHT0V06PA3C97gvsGibOdNpC6pMl6-fSzZj15gnB9voj2UsIw2U6Etai0f6aTq7YIDA1n64jBfitDOlJuZlFIhuHANoyeW4pPe1qaWDkujn_YdRLFdB7U9xCiG8c6eQ8lgh4prXU3AWpNd7xI62ePHuAKYPUebxp1voM-gNz_-UyECb1CK-gyd0hSZpcRHTRMfrpBZP6UqcBmLcf0AwdsFEoIqo5UM362axoR6NcosybjGxCaR5odzFI2Jt-IrUC4dqNZdcj68Fobj0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a33540e9c.mp4?token=BOxz7BVSxtCImBG0zcG3bsP8JhxQ_LFnsjACt8_FOI906mVuwgxCZ5-Mu9AnwgNb92OnYqjHT0V06PA3C97gvsGibOdNpC6pMl6-fSzZj15gnB9voj2UsIw2U6Etai0f6aTq7YIDA1n64jBfitDOlJuZlFIhuHANoyeW4pPe1qaWDkujn_YdRLFdB7U9xCiG8c6eQ8lgh4prXU3AWpNd7xI62ePHuAKYPUebxp1voM-gNz_-UyECb1CK-gyd0hSZpcRHTRMfrpBZP6UqcBmLcf0AwdsFEoIqo5UM362axoR6NcosybjGxCaR5odzFI2Jt-IrUC4dqNZdcj68Fobj0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کارنامۀ ترامپ بعد از بسته‌شدن تنگۀ هرمز
🔹
بنابر اعلام وزارت انرژی آمریکا ذخایر نفت استراتژیک آمریکا در این هفته ۶.۱ ملیون بشکه کاهش یافته و به کمترین مقدار در ۴۰ سال گذشته رسیده است.
🔹
همزمان قیمت نفت برنت نیز با افزایش مجدد، در آستانۀ ۹۰ دلاری شدن قرار دارد.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/455501" target="_blank">📅 15:17 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455500">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxGzqx22pesDlhZv1-xXv5YT3203Pn16c3LFj7ojqoVrPTXY_KT5N6YFg9QXOmOUz7SKhTQ4Sk_G8YDDQ-maWor8RynZVonYpBF1GTSNrIV-MVV0IJyfAXJoRjCXVA3K4-ZsXswp8ALgbyeC1DVhVwJ7aXDat3VLHZAgBmuN4gAENqtJMNdsTKDKYJufVz4icBSxJ8CXbm2uM9UCldRXD1LTY6rZ7a1sYdMRwgXyQWi9itxG5JZJHliLTWhKbUoKuFli2uxUhw-AC1XmCw7VxO1dQpeBI6NeOxySent7gZWcD3Ef-INpSx4QwZ48fNlfUrJzB7BOPWwHKBgD0zdPhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
واکنش رسانه‌های مختلف جهان به انتصابات جدید رهبر معظم انقلاب  @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/455500" target="_blank">📅 15:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455499">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5be9d724b0.mp4?token=Bajl0hQUcZovTlsy5T0fX_9OKBkUVHKdFW1STrhuzTGhuWpClXKipHgLL2Pa2Pr97n6jjQ_J3I7745YuNd7awkh2Et3sRpU5GkoS5oinDqo5X1cinhooEFJFZp8SD1HXiPSgewAC3opaBiTclrMPTLQYEGW8l12dkTKK8ssft_k12vUtG1piIVKZPt7p1sTAlpfVWRSK72Tij4MzaWbjlsGh3n14rSa5q8KA4eEMFCR5nZND-oS-xJRpVECH3UOQfsVsNk3ywd0EE0XUthfpK1vzTI4mcfeFnBXJ0cp3Dm9odm-oU1OWR8owqQ-gdrXEL9A5JtUN5MhdtKz_oNsFTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5be9d724b0.mp4?token=Bajl0hQUcZovTlsy5T0fX_9OKBkUVHKdFW1STrhuzTGhuWpClXKipHgLL2Pa2Pr97n6jjQ_J3I7745YuNd7awkh2Et3sRpU5GkoS5oinDqo5X1cinhooEFJFZp8SD1HXiPSgewAC3opaBiTclrMPTLQYEGW8l12dkTKK8ssft_k12vUtG1piIVKZPt7p1sTAlpfVWRSK72Tij4MzaWbjlsGh3n14rSa5q8KA4eEMFCR5nZND-oS-xJRpVECH3UOQfsVsNk3ywd0EE0XUthfpK1vzTI4mcfeFnBXJ0cp3Dm9odm-oU1OWR8owqQ-gdrXEL9A5JtUN5MhdtKz_oNsFTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایران میدان‌دار جنگ
🔹
نیویورک‌تایمز: جنگ ۶ ماهۀ دولت ترامپ علیه ایران، بیش از آنکه به پیروزیِ راهبردی منجر شود، در مسیر یک شکست راهبردی قرار گرفته و این وضع، جایگاه نظامی و سیاسیِ واشنگتن را با تردیدهای جدی روبه‌رو کرده.
@Farsna</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/farsna/455499" target="_blank">📅 14:53 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455498">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dd3c187fd.mp4?token=HKFR8pxUXm-fk14evtwmnrzx_U-MsY3RXI_cJ3OM_tHPh0hGI-pVyVGhwVt8Lh7JKHWlpiDkio8DBPLmiHS83ogJ5jfq566jab6xWQYNEDfv4OoPmWyBi5ddVBfzPSBW6AFE4353nUvYH6esocXERfsDkipy8hq_UjjqbrCbcPMrillQwlT3zQERGlyuUCIaUtM5WIxQ__aZtxRveac7n3aXUAn5uy0vkTSm1XguPusKsHgYXEwBI7JQaVqCrl0FwlnqmPnrd8A00W3l6AiGjYrihmFAkelqqflQBYL9BMddLAWd2COzbCOBruxn8paFG0kr4IqPmEd-68I2I__rhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dd3c187fd.mp4?token=HKFR8pxUXm-fk14evtwmnrzx_U-MsY3RXI_cJ3OM_tHPh0hGI-pVyVGhwVt8Lh7JKHWlpiDkio8DBPLmiHS83ogJ5jfq566jab6xWQYNEDfv4OoPmWyBi5ddVBfzPSBW6AFE4353nUvYH6esocXERfsDkipy8hq_UjjqbrCbcPMrillQwlT3zQERGlyuUCIaUtM5WIxQ__aZtxRveac7n3aXUAn5uy0vkTSm1XguPusKsHgYXEwBI7JQaVqCrl0FwlnqmPnrd8A00W3l6AiGjYrihmFAkelqqflQBYL9BMddLAWd2COzbCOBruxn8paFG0kr4IqPmEd-68I2I__rhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ رهبر انقلاب ۶ فرمانده عالی‌رتبه را منصوب کردند
🔹
حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای، فرمانده معظم کل قوا، با صدور احکام جداگانه‌ای مسئولیت‌ها و مأموریت‌های ۶ تن از فرماندهان و مدیران عالی‌رتبه نیروهای مسلح را ابلاغ کردند.
🔹
براساس این احکام، سردار سرلشکر…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/455498" target="_blank">📅 14:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455497">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a20cc9106.mp4?token=joR7joULzP4UmTKFMeHtoY9tpGFmnZH7yOKDemdvlN9zCvvCLRpMUUPOS6US6S7zbII5HAesMrphTadM6-wcLPnwRprMvb1nzNgVNq77JadKuspUQAQZo5RBEQ4FH-hdgdZ0c0mWowiLXGBT_EvoayDRj__g2pnnKXa9Qd5KD44wughvrV05zq_quQqhQ60UeSxCmlvsy334Oi9AG2F7sIefxUKbTEPaYRQFil7eS6vG_xeQkVWc7p0xh6ngk32TsUYF9u35-p5sTV8JiGh3F7QrkdhXfxuFVBnMjS9ouU_t241iA5IsGuf77dnPzS_GlECElzfYS1vChc3xUfbL5L6pqkBNikfTo2LfO3zxm4PljWiPPBz0rPoxj3wV9PmP82b41CH8Yq2-ZOTBztrtnFaTlUMsid07gMAxZJVPKW7RXL56aP7MVNBYHpw5S9SDP8J7xINrx_9QQ7-7-s2AqbeZ5MD_Bvijx9I34jp44Q4NmKYepzGNoBXWuXBZxOPxylnXBGTdHTxDeWJCmS9jo4NUK_etQJct2ufXjYNGEGpPXOF7DwuEVR4R77A8iQoATv51fJD418B8cWrAVJOMpvGY80ohULy8ggDbJxIjBWHVWbbbJ7WxiI5EFPTCF_BpCybhjc2FG0s6bzhp0MvtO2wEcQ_il_X69oLftjzjObI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a20cc9106.mp4?token=joR7joULzP4UmTKFMeHtoY9tpGFmnZH7yOKDemdvlN9zCvvCLRpMUUPOS6US6S7zbII5HAesMrphTadM6-wcLPnwRprMvb1nzNgVNq77JadKuspUQAQZo5RBEQ4FH-hdgdZ0c0mWowiLXGBT_EvoayDRj__g2pnnKXa9Qd5KD44wughvrV05zq_quQqhQ60UeSxCmlvsy334Oi9AG2F7sIefxUKbTEPaYRQFil7eS6vG_xeQkVWc7p0xh6ngk32TsUYF9u35-p5sTV8JiGh3F7QrkdhXfxuFVBnMjS9ouU_t241iA5IsGuf77dnPzS_GlECElzfYS1vChc3xUfbL5L6pqkBNikfTo2LfO3zxm4PljWiPPBz0rPoxj3wV9PmP82b41CH8Yq2-ZOTBztrtnFaTlUMsid07gMAxZJVPKW7RXL56aP7MVNBYHpw5S9SDP8J7xINrx_9QQ7-7-s2AqbeZ5MD_Bvijx9I34jp44Q4NmKYepzGNoBXWuXBZxOPxylnXBGTdHTxDeWJCmS9jo4NUK_etQJct2ufXjYNGEGpPXOF7DwuEVR4R77A8iQoATv51fJD418B8cWrAVJOMpvGY80ohULy8ggDbJxIjBWHVWbbbJ7WxiI5EFPTCF_BpCybhjc2FG0s6bzhp0MvtO2wEcQ_il_X69oLftjzjObI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
باران تابستانی به کلاته‌رودبار دامغان طراوت بخشید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/455497" target="_blank">📅 14:37 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455496">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_dA22amHhMiEfSl8yDLiXJFg03vCiZY95xVTYc1p66c_6YZs1ifBtnwHu9U6T0R2Vt5Ihun6MvcrHx6cC_pVz2O_pWj2ra4uGNlajQo9Z8_l_AhEnFVywXCTsdYnBhuTCTbNpw2GbrLyHk1tr7tZ3fvNqN_tugyl-z59AipCw3mfNozrLliJ6XbEB0Mxz87VQJLixs3KuRqDlk1O0OzOcAai-yeE36OEFGKWoxhL1PWhTCVYFN4xFgNJT9G1129azqveCH9kWiuFe2MKxNYkoHmfYTo5movlcuUDL0dBJwGBD0OCo8ty3WRfC9I5rk3wd_dj2oTB7-O9P53vuBS-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فولاد مبارکه پیشتاز در تولید فولادهای پیشرفته
شرکت فولاد مبارکه با توسعه سبد محصولات خود، گام بلندی در مسیر تولید فولادهای پیشرفته و با ارزش افزوده بالا برداشته است.
بر اساس اینفوگرافیک منتشرشده، تولید فولادهای خاص در این مجموعه با هدف تأمین نیاز صنایع راهبردی از جمله خودروسازی، زیرساخت‌ها و صنعت نفت و گاز دنبال می‌شود؛ رویکردی که ضمن کاهش وابستگی به تأمین خارجی، به توسعه زنجیره تأمین و افزایش تاب‌آوری صنایع کشور کمک می‌کند.
این مسیر، بخشی از تحول فولاد مبارکه از تولید محصولات عمومی به سمت فولادهای پیشرفته و تخصصی است.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/455496" target="_blank">📅 14:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455494">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس‌ پرس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mUIswNHD4N9vREJ793pw0YLUfU8ERaQlzOJS0J272-pkOWP2R2pJgA5djzjvt-NLsUX1lRxBwN6bRI2jjSAcwFi93lw7biPdcHvpqJxvumUEl3wASjUKIE4NQ9L31sCW6XBqNHkTrYxXWvRSWG6OYifGkXwwWddHaiE_14zPjnPf8_if42cQCoZD8jMz1Bs5WwPynJSqEiKKVFJzpX4fu5y1YL-y3cmtKDfN3m2ivca4svKkQ0aRevCM1wqEOqtaFRA1iIw3PGXcYZm-WJBZMnv9Tn27GxAtBVw6jXuBvq0PCezxE-uhDFjejM5PNnZLYtPyIXSKjpOf1TvCPJBJLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p-ouzFdYqn9Y4LyZ1-mN7Zf5VOgTZbOU5hlAOzW42pHULk9dNb6tWk94UAJqrmM1cEAJvA0ejZItg1PJ_FSHRPgh3Sf6fbbHDPuwZx9HFdBcIXMt4k57fyNrJ44ep6bWN1kkGv8cLBghKBmXCuVvgLWL-decloY9vQ6JihUh51o_7_7DIVDdv0cF2jCM4hlQp9ZcmkN3LYjq05pNuiwjaNWVRo3grAupENVdz5aHkFe3dp_jySlWqkfzYOcKSkqWU8-8_wKgRxaSmvYxUDy0FP-qMYM_-Xh4zKjZdOT8S9Na1nlSjTffXeSvixdeyCwz4ejEWNeSfM0ybB8tmcyAJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔸
مدیرعامل مس ایران:
🔰
هماهنگی راهبردی شرکت ملی مس و صندوق بازنشستگی ضروری است
🔻
نشست مشترک مدیرعامل و رئیس هیئت‌مدیره مؤسسه صندوق بازنشستگی مس با مدیران عامل شرکت‌های تابعه، با هدف ابلاغ سیاست‌های کلان، تبیین الزامات حکمرانی شرکتی و تقویت هم‌افزایی راهبردی برگزار شد.
🔹
در این نشست که با حضور برخط دکتر سیدمصطفی فیض، مدیرعامل شرکت ملی صنایع مس ایران، همراه بود، بر لزوم هم‌راستایی میان مؤسسه صندوق بازنشستگی مس، شرکت ملی صنایع مس ایران و شرکت‌های تابعه و همچنین ارتقای نظام‌های پایش عملکرد، شفافیت و انضباط مالی تأکید شد.
🔹
دکتر فیض با تشریح سیاست‌های شرکت ملی مس در حوزه‌های نظارتی و عملیاتی، هماهنگی استراتژیک میان مؤسسه صندوق بازنشستگی و شرکت ملی مس را ضروری و اجتناب‌ناپذیر دانست و شرکت‌های تابعه صندوق را بازوان اجرایی شرکت ملی مس و مجتمع‌های تولیدی عنوان کرد.
ادامه خبر در مس‌پرس:
https://mespress.ir/x6Sw
@mespress_ir</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/455494" target="_blank">📅 14:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455493">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/455493" target="_blank">📅 14:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455492">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5brPlq3w9k9fVuNjbEqqPsjbK1AdO4gmqUS2SDArUtDkkdno5rECHYIlQWqmlxbqHMPK8GkyRIGf8m75VG-fxajuiZeqhjkLylloLEraawiC-c0e3CYyi0lvoU-u1ZZH8bXeE9ts0bL_N0EoNcDJ1lYm2Us-E6kdBVJfdvpB5m8mibFW3J5rV5ft7ORAfu2taRmO4_gpddLN3S2RCLsMWRko5xKnhE3-FzBuUf1k84SuY5kleZOlyI5AmVMVCJnM9P3S9h1Tx0U1WRqkC0ZN1OcPufhWqbFbWqbLmeCD2tIaM5nwKVx3Ku6nRu2__Ni-YRsD0KZvFKLKggI7uE-DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه‌ای به‌بزرگی ۳.۳ ریشتر در عمق ۸ کیلومتری زمین، تازه‌آباد کرمانشاه را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/farsna/455492" target="_blank">📅 14:17 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455491">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c314f67236.mp4?token=Kf60hw7Zb8qnQshp0iy6VDw7bksUM0xFQAnh0zmY0-u1Kp6WYbrCneDAOo6qTO4OjUCi3hBGWkK-8XwvT3w_4_ngUUrjwpHAj90flgIgEAumlz__8mUtZZUYOQCSAZh5_0SXAbzVa1p_ECGfVxZUxVL-ZJqr3_EEFswHUr6862ARX44GZMvmHpr-bH15bjJLXJnt_W8b3i9rxUW8lwv124KuT4cPWTt0xvE41ch1w8RXSJpWzmVDTAQ4Gn_Edd8n7fuU0KhhQSUovGRTpSzcR42rBzAx28liYQmo7WEohoBdd_zsCRjouPFOQR4wsqiYRgyDuwVflixXLWA-7a5QoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c314f67236.mp4?token=Kf60hw7Zb8qnQshp0iy6VDw7bksUM0xFQAnh0zmY0-u1Kp6WYbrCneDAOo6qTO4OjUCi3hBGWkK-8XwvT3w_4_ngUUrjwpHAj90flgIgEAumlz__8mUtZZUYOQCSAZh5_0SXAbzVa1p_ECGfVxZUxVL-ZJqr3_EEFswHUr6862ARX44GZMvmHpr-bH15bjJLXJnt_W8b3i9rxUW8lwv124KuT4cPWTt0xvE41ch1w8RXSJpWzmVDTAQ4Gn_Edd8n7fuU0KhhQSUovGRTpSzcR42rBzAx28liYQmo7WEohoBdd_zsCRjouPFOQR4wsqiYRgyDuwVflixXLWA-7a5QoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بزرگ‌ترین پالایشگاه روسیه که در ۶۵۰۰ کیلومتری مرز اوکراین قرار دارد، در آتش سوخت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/455491" target="_blank">📅 14:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455490">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/612dd85d5a.mp4?token=I2F_xOWwMOnBLOIR4CiJZdmqxrSaqZmdVLMd8sJq2BldPwSJ506dCLECFAw17d15xv_jZndsdM2cgRRamrI8uelFWey-GQJ6Rrb-AZ0EMy4fr7oQphNdYG3nHtP8SoSFpwh_Gn_p9Oo8QjSAEXSAA1ppXqa5xEGS8xd5lJc6YFNwxOQH_yyWi7XgCRn43oxGZFDOndZlbmYHCHjzGn3DcPdxaB9rvxK9-dQz79Wq9e_-_EosWkVGmUTLYkX363kT2NnGTcXpRysTL8CBcnY8356xa9nIRlcHgiXOkYVdCGotzBFCtsbiW7G5s1Mwf7AJUJ5gN6dLuajvIStREy1H1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/612dd85d5a.mp4?token=I2F_xOWwMOnBLOIR4CiJZdmqxrSaqZmdVLMd8sJq2BldPwSJ506dCLECFAw17d15xv_jZndsdM2cgRRamrI8uelFWey-GQJ6Rrb-AZ0EMy4fr7oQphNdYG3nHtP8SoSFpwh_Gn_p9Oo8QjSAEXSAA1ppXqa5xEGS8xd5lJc6YFNwxOQH_yyWi7XgCRn43oxGZFDOndZlbmYHCHjzGn3DcPdxaB9rvxK9-dQz79Wq9e_-_EosWkVGmUTLYkX363kT2NnGTcXpRysTL8CBcnY8356xa9nIRlcHgiXOkYVdCGotzBFCtsbiW7G5s1Mwf7AJUJ5gN6dLuajvIStREy1H1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمایندهٔ ولی‌فقیه در بنیاد شهید و امور ایثارگران: در جنگ ۴۰ روزه ۴ جنین به‌شهادت رسیدند
.
@Farsna</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/455490" target="_blank">📅 14:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455485">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">منابع غیررسمی از حمله به یک کشتی عربستان در باب‌‌المندب خبر دادند
🔹
شبکه «الجمهوریه» یمن و برخی منابع عربی از هدف‌قرارگرفتن یک کشتی عربستان در نزدیکی باب‌المندب خبر دادند. @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/455485" target="_blank">📅 13:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455484">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjhvbJVjmz9KBo2ZQ53RrzpG00qdcm35isj6IPq8rm9LhoN3zeYSBefUb5M2IVdqEdLkyAxyjmmOPUDbzq1f4CU8cMIw3nnFvXfrjG7wKo69ZtPNc1eCwLfwoqUcmtsHYBte33U9Qe8k4KM40gPiD0CdXzvqiEcbUDUfPvbEyCjzx4eybRla9LtxYIYUGian8j8nLB2GiBSOEFVIr04EefSAm08vGgz91wdTCvj5_FXlQ7qK6OQybh0KW7HDcl5dCZbQei1fANNONPSBhB87aaF_1gIyk4BUzoV68gjYg2uo270gPwbpmBHYWIhF8PhJSFjY9OHkOdA3xiA5Tj3Vjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: معیشت مردم باید دغدغۀ اصلی نظام باشد
🔹
با مدیرانی که برای افراد فاقد صلاحیت کارت بازرگانی صادر می‌کنند، طبق قوانین برخورد شود.
🔹
بهره‌مندی از ظرفیت محله‌محوری و مسجدمحوری الزامی برای راستی‌آزمایی و ارزیابی وضعیت درآمدی و اقتصادی خانوارهاست.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/455484" target="_blank">📅 13:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455483">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">پیام تبریک رئیس ستادکل نیروهای مسلح درپی انتصاب فرمانده کل سپاه  برادر ارجمند سردار سرلشکر پاسدار احمد وحیدی؛ سلام علیکم
🔹
حسن اعتماد فرماندهی معظم کل قوا در اعطای درجۀ سرلشکری و انتصاب جناب‌عالی به‌سمت فرمانده کل سپاه پاسداران انقلاب اسلامی که بیانگر لیاقت،…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/455483" target="_blank">📅 13:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455481">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQhXcltNsSkzg24RO1SpkrZfpYX81Q1M9aKmpyJtdzd1494gSwe-NfwqTI_BjhlbACj0mixTmMn4t_tDaRWs8Hnu46dtD9nFdiq8BXqL5ZWGYbEZzF_ShAlFuyGtcFEZRk6sx3DONLLY8lzkkS9T1kUDO19QfP9Cn3fdu6nMCwUAHg_nIWRbuCVw5_m7w9MVqxArRX3SHU8Dyzls4trKqDVVVi-S65bW9SmE-hEI5pgIBdgJ_tiCSoTmCkX9Ye3K0951_9SPD9qVvYPb2QoOCJZbyTsq57qQIqKyAIFEJy7VxNyYkbd3GeyHKF1B3VUMGXb9NnTutBabB9iUrUywNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ پیام فرمانده کل سپاه در پی انتصاب محسن رضایی به دبیری و نمایندگی رهبر انقلاب در شورای‌عالی امنیت ملی
🔹
برادر ارجمند آقای محسن رضایی انتصاب شایسته و حکیمانه جناب‌عالی به‌سمت نماینده رهبر معظم انقلاب در شورای‌عالی امنیت ملی و دبیری این شورا را صمیمانه تبریک…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/455481" target="_blank">📅 13:20 · 20 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
