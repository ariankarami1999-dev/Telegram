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
<img src="https://cdn4.telesco.pe/file/gfPRKWKhdEZ941-4Bot_YxMc9Ieum1kY164wcePbBaAyfrHStdqGS1rFIZRNP2mnxt7evizAG3OB0V8U8T3bwl4nKWjN_TQrS1DNAKu09R9Ny1EupijNpi4lKRY_qq55dAlhVgwP10FWyF74HxPXsoiX3sKG0qII9R_ZekNZQ6d4taoMhdh79zHFCiItVCHTMiiQ5_WTcjPRSmZFDowWYmgod1pj-VH8SrAZTkI6kTbvDrO27LT0iRQevySYZ3YalZKSiSHiVzuRd61cgAcMsODlGY0v_bMPiCIPonbtVCOI9wmJVyGeQJssGJIh2xcwheerXJlBo3_8XWOwMjxdRg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.2M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-22 11:03:22</div>
<hr>

<div class="tg-post" id="msg-689425">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nYL_us3u2oZooTR3WY2TMfQ2uucDfhrN1i1lNIokH0RK6qjv6xs9_YZv93nN6MQIohKo9M0b2jqsvFaoDuuYs1hpZJbxRHGP1J7r79vGRh8I4fWClclYMGw1PW8OnfGPxfov2TRiOEpp-ofUo5wRCtP66bqtFuSRH5uc6NLTMbowWEZduEtaH0a97NSoUCEPQIzEq9wL80AmY93jEwKeFIFhT3S1b2T54hR4hTqcWJ5JaenBHeyCMg2mD8veOsO23wqb57p268XEI7zaKEOMHC1TrZyuYSg_VPLK9S99Ph83g6YYrjYe0WIQT85DYLIWGPvrjVNz3K_pP8pr-Nw2uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترکیه با ارائه طرحی خواستار دور زدن تنگه هرمز شد
ترکیه‌تودی:
🔹
وزیر انرژی و منابع طبیعی ترکیه، از قطر و کشورهای اروپایی خواست اراده سیاسی لازم برای پیشبرد طرح قدیمی انتقال گاز قطر از مسیر ترکیه به اروپا را نشان دهند.
🔹
این طرح در شرایط اختلال در تنگه هرمز می‌تواند یک مسیر جایگزین برای صادرات گاز قطر ایجاد کند. بایراکتار طول این خط لوله را حدود ۲ هزار تا ۲۲۰۰ کیلومتر اعلام کرد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/akhbarefori/689425" target="_blank">📅 10:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689424">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
یحیی سریع؛ سخنگوی نیروهای مسلح یمن: دشمن سعودی طی ۴۸ ساعت گذشته ۱۲۹ حمله هوایی را علیه مناطق مختلف یمن از جمله تعز، الحدیده، الجوف و مأرب انجام داده است که عمدتا از پایگاه‌های هوایی در خمیس مشیط و طائف و توسط جنگنده‌های F-۱۵E و تایفون آن‌ها صورت می‌گیرد، خواهید دید به این تجاوزات چه واکنشی خواهیم داشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/akhbarefori/689424" target="_blank">📅 10:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689423">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
سپاه حضرت سیدالشهدا استان تهران: عملیات انهدام مهمات عمل نکرده تجاوز آمریکایی صهیونی در شهرستان دماوند امروز تا ساعت ۱۶ انجام می‌شود
/ مهر
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/akhbarefori/689423" target="_blank">📅 10:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689422">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0171c995a0.mp4?token=m_17KwPmrmiik7snotxJBLjsqGGjgxmxrAgSCVpnoDsUsn1DSGCghI7mJlyZf27F0PgV8bt3Nxbu59xddYjV22GthXcG1t79W_OwI36Y73eYpFMh2sbo5ViFhYnn5olS0MQfpBvOBK-nIwNvB-QfPBJfLpAVlZkIaKbrFOmTdY-anaW3QnHA8igJelqDrP-QnRVZ9PfCvLN9ocJpH099Y07pKA9rlwEEk61aS9nXj7PZg-X78tz_LmiGq6lUlZb4z-4dfeHi6LAq-Nrw7edukjRsbLsQw8lo_ONUFkGwh0gUIylyqAhE764LpGQikGnzK-6L58gDFiaDvCE4GNiQnWsxC2Y5CKMj_77PAP3DP-J9VV_QqmR36JaBJqmyQ1UoF5FYylA4Uvf9Z4hJ7a-CdC_risPviddEkxZQ2O54D0PFbXZnZCIydxxRqe7jfJgzabIvut5IztFrm_HTJok0Xgy9bOsF21fhzXV3yRP0qm--nuogzS5pCS-3APjC_GpprkxfVksBw-99QrjbneQcCHDl7LbeCsTigJIeeBUi-Y7YJRNwPnkUCXHSBDV9jtjBDSLXYuzgzcV4KGCsCdTyD1KCM9mXfGPULqNzGpIMHkmAcYvoghZje--YaSsECZ_Uqh7_oB7l5jSaJjnN6W7b5q0-ynDtUFsbscZGprciZsM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0171c995a0.mp4?token=m_17KwPmrmiik7snotxJBLjsqGGjgxmxrAgSCVpnoDsUsn1DSGCghI7mJlyZf27F0PgV8bt3Nxbu59xddYjV22GthXcG1t79W_OwI36Y73eYpFMh2sbo5ViFhYnn5olS0MQfpBvOBK-nIwNvB-QfPBJfLpAVlZkIaKbrFOmTdY-anaW3QnHA8igJelqDrP-QnRVZ9PfCvLN9ocJpH099Y07pKA9rlwEEk61aS9nXj7PZg-X78tz_LmiGq6lUlZb4z-4dfeHi6LAq-Nrw7edukjRsbLsQw8lo_ONUFkGwh0gUIylyqAhE764LpGQikGnzK-6L58gDFiaDvCE4GNiQnWsxC2Y5CKMj_77PAP3DP-J9VV_QqmR36JaBJqmyQ1UoF5FYylA4Uvf9Z4hJ7a-CdC_risPviddEkxZQ2O54D0PFbXZnZCIydxxRqe7jfJgzabIvut5IztFrm_HTJok0Xgy9bOsF21fhzXV3yRP0qm--nuogzS5pCS-3APjC_GpprkxfVksBw-99QrjbneQcCHDl7LbeCsTigJIeeBUi-Y7YJRNwPnkUCXHSBDV9jtjBDSLXYuzgzcV4KGCsCdTyD1KCM9mXfGPULqNzGpIMHkmAcYvoghZje--YaSsECZ_Uqh7_oB7l5jSaJjnN6W7b5q0-ynDtUFsbscZGprciZsM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دلتنگی امیر نوری برای عمو اکبر
🔹
اکبر عبدی از مریضی خسته شده بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/akhbarefori/689422" target="_blank">📅 10:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689421">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/682c96382a.mp4?token=oGiUpHss_0-eLvRGlgmnqmeahKTR1qNhh4PrCpVmLCzRhxp_Z2YDQ-Tw7__mimLQlqktEYfcgp1L-hyR8KQBMGxreewYagTc-PPP4yisbL4lwJ4xfC2O1mvd4MvdRtDQdynNq7XkDGzZFABYbNMAn2ZQSG-QaZM8hipRKU-xqulHpKTUCFqwH7sjxLDfZYxDnnwX63GBF1VCfUg2_RKcyFKGstX5Jx12kRNzC9yb9hmdHoXyUIDx8XimbUk4EhXtm7ZDO0uqRZCNluty7865ZHjy0hhKwlWm48AXSJuIXEMm6m4Q7zuOw5ziTuNctXX58PQNIEeCV4P05L_plKrTX6eITkVWCCw2vlDdrE4Kd6mNL3h1_qnmBIhy_K0_OejSLIJ8CZatO5D7il0HA4fM5tmMm_HOcUZduCdowcLjXu2z4K1yYNk5H8OdjkIrc7TYT9WjbOWOVT1dkv6oUro_biACgJqTKWE0UbYU7uf8qDax8okAJlgVxCXGFsAwfR355_zX1zI3UfQWOO5gikS2QZYI6pa10GSFJCbK5HMey55Fhif9E-kavG7UH0CG9JMGtOKI11KZi986eVhDf9bzeQE1f-wBOJn5uVyDjEdb6gg0nW8OVuybqx2gJMsVR4a5U0teeD2ROEFxDw7gZVtqSIME6MLwkWbTca10ZRBOqvc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/682c96382a.mp4?token=oGiUpHss_0-eLvRGlgmnqmeahKTR1qNhh4PrCpVmLCzRhxp_Z2YDQ-Tw7__mimLQlqktEYfcgp1L-hyR8KQBMGxreewYagTc-PPP4yisbL4lwJ4xfC2O1mvd4MvdRtDQdynNq7XkDGzZFABYbNMAn2ZQSG-QaZM8hipRKU-xqulHpKTUCFqwH7sjxLDfZYxDnnwX63GBF1VCfUg2_RKcyFKGstX5Jx12kRNzC9yb9hmdHoXyUIDx8XimbUk4EhXtm7ZDO0uqRZCNluty7865ZHjy0hhKwlWm48AXSJuIXEMm6m4Q7zuOw5ziTuNctXX58PQNIEeCV4P05L_plKrTX6eITkVWCCw2vlDdrE4Kd6mNL3h1_qnmBIhy_K0_OejSLIJ8CZatO5D7il0HA4fM5tmMm_HOcUZduCdowcLjXu2z4K1yYNk5H8OdjkIrc7TYT9WjbOWOVT1dkv6oUro_biACgJqTKWE0UbYU7uf8qDax8okAJlgVxCXGFsAwfR355_zX1zI3UfQWOO5gikS2QZYI6pa10GSFJCbK5HMey55Fhif9E-kavG7UH0CG9JMGtOKI11KZi986eVhDf9bzeQE1f-wBOJn5uVyDjEdb6gg0nW8OVuybqx2gJMsVR4a5U0teeD2ROEFxDw7gZVtqSIME6MLwkWbTca10ZRBOqvc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معرفی مجموعه کتاب
«کودکی نامداران»
🔹
قصه‌هایی از کودکی قهرمانان و افراد نامدار تاریخ ایران
🔹
برای عضویت در کانون پرورش فکری کودکان و نوجوانان عدد ۰ را به ۴۰۴۰۸۲۳۲۰۰ ارسال کنید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/akhbarefori/689421" target="_blank">📅 10:47 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689420">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffe8d4a20e.mp4?token=Rnv-6C7clZd0swNzXzjWUGSPmGx7aW7QMNr2jTTuDfqUIuBa0r01UaoTsSIT7LUzIOYdHl6KIoY1BW0ziwb04U-RGnOg6DmJf30S8V1DbqbMke3zBkcZfQ9OjmxfEocHG8CyDvNlNadxHjXGczjK41oZS2Qz5J6mY_s_gXLeV_83Li8USKxhykz7ntIHhjuWQ0xLVMzNLbrdWSD7153o1wSA_SupyTDmXxiRjiMtftrTESBsUKF8pHQyOJYalMche1jQu5kWyjDkXMd3xKHLy9jQPZLI6mGdlijL5XiZv1-zCfxaV_vneh8Tcj098e6dyc_FkfcKL81dhm7E7_53EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffe8d4a20e.mp4?token=Rnv-6C7clZd0swNzXzjWUGSPmGx7aW7QMNr2jTTuDfqUIuBa0r01UaoTsSIT7LUzIOYdHl6KIoY1BW0ziwb04U-RGnOg6DmJf30S8V1DbqbMke3zBkcZfQ9OjmxfEocHG8CyDvNlNadxHjXGczjK41oZS2Qz5J6mY_s_gXLeV_83Li8USKxhykz7ntIHhjuWQ0xLVMzNLbrdWSD7153o1wSA_SupyTDmXxiRjiMtftrTESBsUKF8pHQyOJYalMche1jQu5kWyjDkXMd3xKHLy9jQPZLI6mGdlijL5XiZv1-zCfxaV_vneh8Tcj098e6dyc_FkfcKL81dhm7E7_53EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کوییک در نیشابور، توسط زمین بلعیده شد
🔹
در اتفاقی عجیب در خیابان فردوسی شمالی شهر نیشابور، زمین دچار فرونشست و شکاف شد و یک خودروی سواری کوییک را بلعید.
#اخبار_خراسان_رضوی
در فضای مجازی
👇
@SedayeKhorasaniha</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/akhbarefori/689420" target="_blank">📅 10:44 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689419">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78168ec197.mov?token=fb9VQgXDOLDUcAJG2z5UurDG6Rb-VRRuEc7bYZ0HW-3rVOC1ioRMII3Zt9u9JVCgEf_eQbHNoxR97dxKtTuk_tSXcJBPC6uannkO33CniKmOOHn8N-aDLe2ylUhgF_-oR28lH3kOX61CQf28-_i_i7Hrrx7fENNjQwtdP8c5sxc_EYXCYVqGsdCxZQjy2-gsc4UFtsqP4ZR67TfJuB-vdvIIhxTnsFNFNSB70cS41w2KiN0o0xpg9aXhCxEakSCr2sRNTdQdnQHX6mUeoCHpfc1t_UFgUSVLI0th7o6SIUZSDNM-lXdGV0dKsWyEgv2-hGB4TBmkqCi2cuvq_XeW3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78168ec197.mov?token=fb9VQgXDOLDUcAJG2z5UurDG6Rb-VRRuEc7bYZ0HW-3rVOC1ioRMII3Zt9u9JVCgEf_eQbHNoxR97dxKtTuk_tSXcJBPC6uannkO33CniKmOOHn8N-aDLe2ylUhgF_-oR28lH3kOX61CQf28-_i_i7Hrrx7fENNjQwtdP8c5sxc_EYXCYVqGsdCxZQjy2-gsc4UFtsqP4ZR67TfJuB-vdvIIhxTnsFNFNSB70cS41w2KiN0o0xpg9aXhCxEakSCr2sRNTdQdnQHX6mUeoCHpfc1t_UFgUSVLI0th7o6SIUZSDNM-lXdGV0dKsWyEgv2-hGB4TBmkqCi2cuvq_XeW3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توجه وانگ‌یی به نشان نقشه ایران روی کت عراقچی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/akhbarefori/689419" target="_blank">📅 10:41 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689418">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGhhAmO37LOZ8fhMSa-m1eoSr_HdlTprOOkgz3w8cdEMQz6uSDZyaWmQMHQcGC7o6_TsHvTFKl8AtQyGsBmeTDqZ2VyLezQkTTaCAlZPF7Nkt0bp_rB2AHirMiO03LZPIBrqHxW4s1tiHjmgdyid4WLej7nxIGG9r-nXNPug7E8WHA6TzT0yeF18tj3M6IqzXdv65dQh8_cgqchowRrGM_NgntxsunJ1Ts3KdZgvCBcmaY9DE2NxX9qNGRIkKGYZjzDcdJJff4rrP7pVLV7PWfwnaIJGQsF9RMUGj70lIeyyYQWRuemcYdjljkwO9OVoFWCfQA_hHPgINCv3qyNFFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزارش‌ رسانه‌های عربی: مزدوران عربستان سعودی، شامل برخی گردان‌هایی هستن که حدود ۸۰ درصد اعضاشون «سربازان خیالی» هستن؛ یعنی این سربازان فقط در اسناد و مدارک وجود دارن و صرفاً برای دریافت حقوق ثبت‌نام کرده بودن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/akhbarefori/689418" target="_blank">📅 10:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689417">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
پزشکیان: فردا تفاهم ایران و عمان درباره تنگه هرمز نهایی می‌شود
🔹
ما در رابطه با تنگه هرمز با کشور عمان گفتگو کردیم. یک چارچوب مسیر در حقیقت مشخصی را به تفاهم رسیدیم.
🔹
روز دوشنبه قرار است وزرای خارجه همان کشورهای عربی که می‌خواستیم با هم دعوا کنیم، در عمان…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/689417" target="_blank">📅 10:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689416">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe380ebdad.mp4?token=SZ5huQ1cPdv-3V5uID4u4M7nWCqgzaZndQ3GLK0LrUsVcP9CPikgURs3kj6Hd3fCA-QZ1h6yl9tpowGviZRnXQj9asUuyLjWm2J1YzrGtnoX0nEmOpFN71H0MfJkZ_kKqutLjIgtGm8DZb96XZY5TtdmryQ0bzujXjMuD6YairrsvDWGA42frICtrReYvpktnBk8mI4f8QnBkFoQkCY-U9YBE6UnSbyAfcW-NM4a5JPHxW6NQkvGDm7489vDfOYz8KLowjYKOg4-IhJ4SNG6DF8vEQjevKplOBpG-LJJh8I6AsHc2VZe5T25kMg0qWpESN37BchedjX6mbjSJV80CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe380ebdad.mp4?token=SZ5huQ1cPdv-3V5uID4u4M7nWCqgzaZndQ3GLK0LrUsVcP9CPikgURs3kj6Hd3fCA-QZ1h6yl9tpowGviZRnXQj9asUuyLjWm2J1YzrGtnoX0nEmOpFN71H0MfJkZ_kKqutLjIgtGm8DZb96XZY5TtdmryQ0bzujXjMuD6YairrsvDWGA42frICtrReYvpktnBk8mI4f8QnBkFoQkCY-U9YBE6UnSbyAfcW-NM4a5JPHxW6NQkvGDm7489vDfOYz8KLowjYKOg4-IhJ4SNG6DF8vEQjevKplOBpG-LJJh8I6AsHc2VZe5T25kMg0qWpESN37BchedjX6mbjSJV80CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر مردم یمن ۱۰ سال هم نفت می‌فروختند، نمی‌توانستند این‌همه سلاح خریداری کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/689416" target="_blank">📅 10:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689415">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
آغاز دومین مرحله پرداخت وام فوری ۱۵۰ میلیونی بازنشستگان کشور
🔹
دومین مرحله پرداخت وام فوری ۱۵۰ میلیون تومانی ویژه بازنشستگان و مستمری‌بگیران تأمین اجتماعی آغاز شد.
🔹
بر اساس دستورالعمل اعلامی، این تسهیلات بدون نیاز به ارائه چک یا ضامن ،بازپرداخت یک‌ساله و اعتبار آن در کمتر از یک‌روز کاری پرداخت می‌شود.
🔹
فرآیند ثبت درخواست و ارائه مدارک به‌صورت غیرحضوری انجام شده و متقاضیان برای ثبت درخواست نیازی به مراجعه به بانک ندارند.
🔹
جهت اطلاع از شرایط و ثبت درخواست، با کارشناسان از طریق شماره 02191551808 در ارتباط باشید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/689415" target="_blank">📅 10:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689414">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9c0f0ef2a.mp4?token=E9e_3-opi9RszfKqFiFfQPXKkRQibrTzVe7aStM1RujWxrpP6dJZWE9dJFOuv9NTBRaaG89-Prwf63jCCL_gdYSKq7nTRd5Wk3J_Dd_org6rPtZDCt9y2gVyrUoOja_Eiuw7YaWEvoz6R59H7RnF3xHXTefXbapWDti4TjGsBMO1JzTPkNFfqvy_t6nMMh2O29hXSaeUzYDXIi1na45Jy_NxUwyczj3kAnMF6nUwfj0xlvuj6lpDWmq-iQ25Sk2_bcY5A4U1E7nedfZ16M2PgtHPFezEkFnIi82r6GpXXG065duOT3Ty7-pjhx4B0nqZ2b6Jb1j_TabENRncz_YXKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9c0f0ef2a.mp4?token=E9e_3-opi9RszfKqFiFfQPXKkRQibrTzVe7aStM1RujWxrpP6dJZWE9dJFOuv9NTBRaaG89-Prwf63jCCL_gdYSKq7nTRd5Wk3J_Dd_org6rPtZDCt9y2gVyrUoOja_Eiuw7YaWEvoz6R59H7RnF3xHXTefXbapWDti4TjGsBMO1JzTPkNFfqvy_t6nMMh2O29hXSaeUzYDXIi1na45Jy_NxUwyczj3kAnMF6nUwfj0xlvuj6lpDWmq-iQ25Sk2_bcY5A4U1E7nedfZ16M2PgtHPFezEkFnIi82r6GpXXG065duOT3Ty7-pjhx4B0nqZ2b6Jb1j_TabENRncz_YXKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرگزاری روسیه: آیا می‌دانستید این‌ها شهروندان عادی در یمن هستند و اینکه حمل سلاح فرهنگی ریشه‌دار در میان یمنی‌هاست، جایی که کسی بدون سلاح مرد محسوب نمی‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/689414" target="_blank">📅 10:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689413">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjRlAGy4GC8pi5bJwEh6J2mjkWuWsMQ1CYD0XkuNvRr3eVFlIzrzObuzIwprP4oLyVvvMv9kAPOtWu9EVlfKw5cowMtQbBfme63BhA0UgUGz83o7yrX2QFfnhRF_ut0WaOdKl949wy0Mg_gOYRCqQ-OyXmyg3_sJsWfzhhID5M1uj_9bBesTL0wjpZpdOZrlcMwqWEL5CS3Qf2xpkjri6vQl_RL4LkgDUv7O_qmUFKaeXqcP0Zkt8RKRn_nl1XAQgcsQ1W0NI0qgvJJ4OgeQJsztyrUs4c_5sRumkt7vDWBMA48uM20k2PnSMsA08TJ_-6HUoPnjynb39Ep1mGtoDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کنایه فعال سیاسی آمریکایی: انقلابیون یمنی در پی برقراری دموکراسی و آزادی در عربستان هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/689413" target="_blank">📅 10:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689412">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb1dc58a1.mp4?token=RzHenhKzsp15wEmAmaDtED4lW2xoQ4A1AqatukS73xjsOCDSRnuIpTZSqR1m-ojVH0tnCs4OiiNao9iOWOMwpFFWb0F0-tmoRIWVsYqeDx6oeQ00UNdtjWMH9sRdaLfqdGwzthgG7Nqo2_t77QgoEUh_injMC9wlXEzgiX7q5lToFp-B2OaIj-rQVTx-MZd_sZCRdmQcJFR5gIOQAPn-MuL5p1eCE6cRd9adaKZowTPxPOwOczzKPhPPqc2Y1XXQvlYn3viOHjSxLu9oe0TvH3vuAEbNwMA5OvhVO7I_SMqZYUSXUf5lF11hadeYwTND94fQO3I0XJukXdUsAeQpsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb1dc58a1.mp4?token=RzHenhKzsp15wEmAmaDtED4lW2xoQ4A1AqatukS73xjsOCDSRnuIpTZSqR1m-ojVH0tnCs4OiiNao9iOWOMwpFFWb0F0-tmoRIWVsYqeDx6oeQ00UNdtjWMH9sRdaLfqdGwzthgG7Nqo2_t77QgoEUh_injMC9wlXEzgiX7q5lToFp-B2OaIj-rQVTx-MZd_sZCRdmQcJFR5gIOQAPn-MuL5p1eCE6cRd9adaKZowTPxPOwOczzKPhPPqc2Y1XXQvlYn3viOHjSxLu9oe0TvH3vuAEbNwMA5OvhVO7I_SMqZYUSXUf5lF11hadeYwTND94fQO3I0XJukXdUsAeQpsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیل کلینتون: من دیگر پیرتر از آن هستم که بخواهم روی چیزی بیش از حد اغراق و زیاده‌گویی کنم
🔹
دو روز پیش، من ۷۸ ساله شدم. پیرترین مرد خانواده‌ام هستم که هنوز در قید حیات ام. تنها چیزی که می‌خواهم بر آن تأکید کنم این است که هنوز از دونالد ترامپ جوان‌ترم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/689412" target="_blank">📅 10:18 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689411">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
پزشکیان در گفتگو با شبکه خبری «ایندیا تودی» هند: ما اگر دنبال سلاح هسته‌ای بودیم عضو «ان‌پی‌تی» نمی‌شدیم/ ایران هیچ‌گاه متجاوز نبوده است؛ اقدامات آمریکا علیه ایران فقط تبلیغات است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/689411" target="_blank">📅 10:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689410">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
پزشکیان در مصاحبه با ایندیاتودی: آمریکایی‌ها تروریست‌های دولتی هستند  پزشکیان:
🔹
هر کسی را که بخواهند ترور می‌کنند و سپس ادعا می‌کنند که این افراد تروریست هستند. پس دنیای عجیبی است.
🔹
آنها به‌راحتی برای یک نفر آدم می‌کشند. یک خانواده کامل را می‌کشند و یک ساختمان…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/689410" target="_blank">📅 10:11 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689409">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ee8d97a62.mp4?token=fVL4ZlemJnTbPM0UVQ3iAvRJJheumcRKzQoRcHL6_DupfFQGxevKIlKPhRCoBObbr4Sh4DVQj8Qu9DRdSaPy-KvvdbIdvnLTkJVNkx3rXsLOulu1mQqixj6QDAVB-tWbxIp4BRwEEkWPBEkVUwtbBdgQjuKnbanJ78xz0eylYnGZ6Vwt4C-NZOMD3ZURHuNZzzitPdymfS-neIs0wCSOnitms979MiRttzBO_UByKhsLEHEKeh0-ZcUAdBy4JplN1z3KL5Iy9pT14A5tw82Jq8sgO_A6UGP8GZ5D1tx0JIrewOJ2dItgQO7HZmtqFlthoPospHCHPUnfXpse2SdhZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ee8d97a62.mp4?token=fVL4ZlemJnTbPM0UVQ3iAvRJJheumcRKzQoRcHL6_DupfFQGxevKIlKPhRCoBObbr4Sh4DVQj8Qu9DRdSaPy-KvvdbIdvnLTkJVNkx3rXsLOulu1mQqixj6QDAVB-tWbxIp4BRwEEkWPBEkVUwtbBdgQjuKnbanJ78xz0eylYnGZ6Vwt4C-NZOMD3ZURHuNZzzitPdymfS-neIs0wCSOnitms979MiRttzBO_UByKhsLEHEKeh0-ZcUAdBy4JplN1z3KL5Iy9pT14A5tw82Jq8sgO_A6UGP8GZ5D1tx0JIrewOJ2dItgQO7HZmtqFlthoPospHCHPUnfXpse2SdhZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک ترکیب خفن و متفاوت که خیلی آسونه و از پیتزا خوشمزه‌تره
😋
مواد لازم:
🔹
سیب‌زمینی
🔹
قارچ
🔹
فلفل دلمه‌ای
🔹
ذرت
🔹
سوسیس
🔹
پنیر پیتزا #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/689409" target="_blank">📅 10:07 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689408">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_zU-KqEAp9uf_GgPPc5yE2UtmYiQ9lMqTbmeSzAUWyIP2QdBOOxkRwrn15XGtbYjm6-u859Pq3HQfl7cHMM1lwpUChav9DNsof5WrRl2OC8_ACmNEzkzPVCkPtgsRyJctRtTIqgTzGU1ECFT6yyi9TAvcCYfgKH2bPyy-lMT57AiZWmmfUXTw30hoDS99nxWd42BVkEegiH-A8u-nVdq5_f7btq65WMyD5JzNSDPNWNUiXWOOtFJdug57gK_2-kPYzhCKIpg0bjV4OL_84jQt1IERuKMzL_VchmTizfiOGcG-BRFiOsvpUfkgv4WcUFBCLe0eFBXfEmI75ogjSdzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توزیع سهمیه‌ای اقلام مصرفی خودرو
قطعات وارداتی شامل:
کیت‌کلاچ، لنت‌ترمز‌،شمع،وایرشمع،تسمه تایم،تسمه دینام و...
مختص خودروهای داخلی
شروع طرح: یکشنبه ۲۲ شهریورماه
ثبت سفارش با محدودیت کد‌ملی
تحویل رایگان از ۱ تا ۳ روز کاری از طریق پست
🌐
متقاضیان گرامی جهت کسب اطلاعات بیشتر و درخواست اقلام می‌توانند به وب‌سایت ایرانکو مراجعه نمایند:
www.iranko.ir
.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/689408" target="_blank">📅 10:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689407">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
رسانه امنیتی عراق: بخش مسافری گذرگاه‌های شلمچه و الشیب بازگشایی شد؛ فعالیت تجاری در شلمچه از دوشنبه، مندلی از سه‌شنبه و الشیب از پنجشنبه از سر گرفته می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/689407" target="_blank">📅 09:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689406">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
پزشکیان در مصاحبه با ایندیاتودی: آمریکایی‌ها تروریست‌های دولتی هستند
پزشکیان:
🔹
هر کسی را که بخواهند ترور می‌کنند و سپس ادعا می‌کنند که این افراد تروریست هستند. پس دنیای عجیبی است.
🔹
آنها به‌راحتی برای یک نفر آدم می‌کشند. یک خانواده کامل را می‌کشند و یک ساختمان کامل را ویران می‌کنند، بعد می‌گویند یک تروریست را کشتند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/689406" target="_blank">📅 09:57 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689405">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d21a23085.mp4?token=OMy04eDcYfFhSXuF2GcHWaprEcSs8Dpm4Id-iaiFCdbmDjcDeAroEpz8R8WHi8p4bvPsbV_woSghYpaVJveC-6LPod8y5audkAqOnoKAf5kRz793lIlqP-i3Ay8DzDN4ufK3ME2Zi8VPM2kUys_AmlijkUqHJ1qcYubUjahMghLa9GfxFp7rNJS0QKSMiPy0Kkp-ujfpAk7O3-nqwosFEULzcgbnguOSuqyW67QdDV8xng6IpBMGHMbI6w2fMYHlqAIqG9bS7QA_bDmprKfcX6aUzEG2CZgDmKyQ49Aj9TknbKoqto7yZCByDBXKS_RDXsJrC2CPp5Drjc74e34x6xIB1q9y-mDfmOOia_pLD-k_MU64x031DVYGb8TGlMyVHFDTGt6zXtFPTgS-i961xjDPeejV1d-WiqhPaQO_OmmJxQAG4tUTMdBk2zqKGOfk8qwI5-WnTImPAz-AtmhXOpnsgCxKN4kLBFo9a3xO4s2P6BVyfs9Et_wqv1Ks_SchFSap3wlgp8h-LhsxIaFQZg109VUQMvQCRVKzU_TfZWCl5BvphjDBXvDe59UHrcz3S70drG9_F0CwlB_s1PqLTYS5AmClaL3UtAYhUDASxFCK-eMmzTPAFs4ldzDfkG3Zdn64uawRtHSQKKvfhekKNR01D6dA93jGLFoPWVz3En8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d21a23085.mp4?token=OMy04eDcYfFhSXuF2GcHWaprEcSs8Dpm4Id-iaiFCdbmDjcDeAroEpz8R8WHi8p4bvPsbV_woSghYpaVJveC-6LPod8y5audkAqOnoKAf5kRz793lIlqP-i3Ay8DzDN4ufK3ME2Zi8VPM2kUys_AmlijkUqHJ1qcYubUjahMghLa9GfxFp7rNJS0QKSMiPy0Kkp-ujfpAk7O3-nqwosFEULzcgbnguOSuqyW67QdDV8xng6IpBMGHMbI6w2fMYHlqAIqG9bS7QA_bDmprKfcX6aUzEG2CZgDmKyQ49Aj9TknbKoqto7yZCByDBXKS_RDXsJrC2CPp5Drjc74e34x6xIB1q9y-mDfmOOia_pLD-k_MU64x031DVYGb8TGlMyVHFDTGt6zXtFPTgS-i961xjDPeejV1d-WiqhPaQO_OmmJxQAG4tUTMdBk2zqKGOfk8qwI5-WnTImPAz-AtmhXOpnsgCxKN4kLBFo9a3xO4s2P6BVyfs9Et_wqv1Ks_SchFSap3wlgp8h-LhsxIaFQZg109VUQMvQCRVKzU_TfZWCl5BvphjDBXvDe59UHrcz3S70drG9_F0CwlB_s1PqLTYS5AmClaL3UtAYhUDASxFCK-eMmzTPAFs4ldzDfkG3Zdn64uawRtHSQKKvfhekKNR01D6dA93jGLFoPWVz3En8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دویستمین شب تجمعات امت مبعوث شده/ اجرای آهنگ «گفتی میخوام رو ابرا همدم ستاره‌ها شم» توسط رزم‌نوازان سپاه- اصفهان
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/689405" target="_blank">📅 09:55 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689404">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
احتمال شنیدن صدای انفجار در جنوب اصفهان
🔹
عملیات انفجار مهمات عمل‌نکرده امروز یکشنبه از ساعت ۹:۳۰ تا ۱۳ در جنوب اصفهان انجام می‌شود؛ جای نگرانی نیست.
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/689404" target="_blank">📅 09:46 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689403">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77de890b77.mp4?token=pF7mzM8Nt-Al_mA4LJheo69XA7o1Z6FtNXgTxvETZr12RMenSei7rws0PmDw6kq-1v28rFllgQmd-xxJKw2QQWseeWWf-Kbn3XX2OndUeC9ZLf9RHIwWgkGfKuvdsKwk1Lkf1INSvZeJUhMpp4gSoQvfHKxS28sfNj_o6m7JVqrF67vjlhmcD-qQmjPSNKW2q1l8teWJm7tZ6t5w7Fv-GGsboM9fr2D7kbeRIaE_B7doT31uDIjuQLIY6n2AxDp1n_sSu6wb29UoltaPETkDrjS7JNnvk3JZ1aP4kGCNz_RhZAQ_RCMhIevuL5mw2-dP4NBL_1cC_ABtsji4dBsYBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77de890b77.mp4?token=pF7mzM8Nt-Al_mA4LJheo69XA7o1Z6FtNXgTxvETZr12RMenSei7rws0PmDw6kq-1v28rFllgQmd-xxJKw2QQWseeWWf-Kbn3XX2OndUeC9ZLf9RHIwWgkGfKuvdsKwk1Lkf1INSvZeJUhMpp4gSoQvfHKxS28sfNj_o6m7JVqrF67vjlhmcD-qQmjPSNKW2q1l8teWJm7tZ6t5w7Fv-GGsboM9fr2D7kbeRIaE_B7doT31uDIjuQLIY6n2AxDp1n_sSu6wb29UoltaPETkDrjS7JNnvk3JZ1aP4kGCNz_RhZAQ_RCMhIevuL5mw2-dP4NBL_1cC_ABtsji4dBsYBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اسکناس داخل بسته؛ ترفند چینی‌ها برای مقابله با کالای تقلبی
🔹
برخی تولیدکنندگان چینی برای جلوگیری از عرضه کالای تقلبی با نام برندشان، چند اسکناس با شماره‌سریال مشخص داخل بسته قرار می‌دهند و شماره سریال آن را از پیش به مشتری اعلام می‌کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/689403" target="_blank">📅 09:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689402">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
نهاد اطلاع‌رسانی امنیتی عراق: تردد مسافران و مبادلات تجاری با ایران در گذرگاه‌های «زرباطیه» و «المنذریه» به‌صورت ۲۴ ساعته ادامه دارد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/689402" target="_blank">📅 09:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689401">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc68e4cea8.mp4?token=ATRX70hGe6aBgSFr4yYtD-J7-ZHvsYTZvgrtEho0hbpUjVSucZdvzTJgjgSCgo748p961ZIceRwgVSytZQXjDs50e0f7dhZZGAkoqGwwSCPP77GzNaMWTN19rAqc_tk36pf4UmfHGIU0NvDf2GqA2Ej9kZA7X8_DkQfg5yztprMQ1Hw6HYb0-sHmNeuX8Afs7UoOVZRXamw7Vcx3Qsj70WZ9RaL1zahy1QRFAkoaL_55X00qZUK2sIziIqOC2x98xhIZ_L7zXLTpKJMYE-Eyf39zrHzYKW-vaeSkRv72VvM9gaLrPQ5-V8BokI9pMK8G1H-lfyntWj7089Y6WnAyHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc68e4cea8.mp4?token=ATRX70hGe6aBgSFr4yYtD-J7-ZHvsYTZvgrtEho0hbpUjVSucZdvzTJgjgSCgo748p961ZIceRwgVSytZQXjDs50e0f7dhZZGAkoqGwwSCPP77GzNaMWTN19rAqc_tk36pf4UmfHGIU0NvDf2GqA2Ej9kZA7X8_DkQfg5yztprMQ1Hw6HYb0-sHmNeuX8Afs7UoOVZRXamw7Vcx3Qsj70WZ9RaL1zahy1QRFAkoaL_55X00qZUK2sIziIqOC2x98xhIZ_L7zXLTpKJMYE-Eyf39zrHzYKW-vaeSkRv72VvM9gaLrPQ5-V8BokI9pMK8G1H-lfyntWj7089Y6WnAyHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
احمد اروزان کارشناس ترک: خلبانان اسراییل برای حمله به ایران در قونیه ترکیه تمرین میکردند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/689401" target="_blank">📅 09:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689399">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrwelK_y9P0L6zLjM0CXRHpUhqeC7un4yF3h6WnJxASHdLVqiQxyK57eNijPOTVQpDderz_9_3BMMOPx7wp8iFogUOGu4zKdPlXofTuqKef4BYXwIniYKoMYLYCw9mDsw0Y41V9BeIKUJ6MZAv7tyWYBOwtwlENTBrH-c6LJmbFuxLaLhxXvPq5Xaul0_fCj-ACBqMRqKIhdajIlDX2ry4sIjvo-RxSHxxHn0sMvOG6HRWSYXpcesg_CtH9xHuK-rviW1vCy7D3yrMKfpfSkzhFmDJhRMoEj1ZGvrk5dqCIgLUfKh9DyT6UW3y0SONl4Ly3akvM23U6IUd0c8VRF-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کمبود کدام ویتامین‌ها موجب کاهش انگیزه می‌شوند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/689399" target="_blank">📅 09:12 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689398">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEMGYxrs6-ugYHIAkZPqzZXO9Q6x7mhaQj6ws-4QQ5xaJ-ZeqY1jCdMbq2MHBO94sJXQKrxzrjk0hUyjJ2dHVaomYE9OGnbp3UemqvZtAvsUwAHWuPsrz-nJjaglpzQDV-JhggeF6Hn4kFp2GD5pRqEiGwqBWMPCA8hQvc1EuNFFTjDr9QDFYjnft49NPrW3ZgxV1ryxfliR7BQ1P_qI0n8T0jl709gj2I7wwfAdVXC9MNJgnW-4X7HRU6LtnoJOHAGpbYVq47LOaG29MpwPIbp2DGvgzl-tRQFhmmLf3DwqIAc5Z8XKm4NRAycdhJNzC8OP-M8jMD7WVriWsB4Mbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فایننشال تایمز: یمنی ها از هوش مصنوعی Claude برای ساخت موشک‌های بالستیک استفاده کردند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/689398" target="_blank">📅 09:05 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689397">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRasa_factory</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33507dbf46.mp4?token=tkJqc3DUMHV3H-FJE-TyRVzS6KdXMRRSCNwfbW1-gLCGXYlURv_4IUlgrpwtGx1lxCnBevPyBhiBvDF9HtH6CmK67bSbM0ebgXcb2-u99s468Hq3yFYTekuJUBejNhMADHCfXKqz4dgG2W32Z2GGqp0PbbWz3b1AiJz51e0ibwsYGEizmpJR1BGy5BreNYDF1p47lQyupol0rxKyYJJsFdsK-QXQt53p-6_Jpr4D3RWBChXHgyi11bzXRL7kRibTtGbE8QCTcM3nPLtlMqpaLri4R9EMKS9z8VK-L3621moiaqwdnSiUZJONZ0Xiffqossa9o7t0XBlg2Ygf0wiSDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33507dbf46.mp4?token=tkJqc3DUMHV3H-FJE-TyRVzS6KdXMRRSCNwfbW1-gLCGXYlURv_4IUlgrpwtGx1lxCnBevPyBhiBvDF9HtH6CmK67bSbM0ebgXcb2-u99s468Hq3yFYTekuJUBejNhMADHCfXKqz4dgG2W32Z2GGqp0PbbWz3b1AiJz51e0ibwsYGEizmpJR1BGy5BreNYDF1p47lQyupol0rxKyYJJsFdsK-QXQt53p-6_Jpr4D3RWBChXHgyi11bzXRL7kRibTtGbE8QCTcM3nPLtlMqpaLri4R9EMKS9z8VK-L3621moiaqwdnSiUZJONZ0Xiffqossa9o7t0XBlg2Ygf0wiSDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فـروش ویـژه درب‌های داخلی
(ضد آب
💧
ضد بخار
🌫️
خود اطفا
🔥
)
💰
فـقط بـا 4 مــیلیون تـومان پیش پرداخت
💰
راسا‌ دُر با
۲۵ سال
گارانتی تعویض
✅
منازل،هتل‌ها،سازمان‌ها،بیمارستان‌ها و...
🔻
برای اطلاعات بیشتر تماس بگیرید
☎️
05136666789
📞
09153068010
🔻
لینک شبکه‌های اجتماعی راسا دُر:
لینک اینستاگرام
▿ ▾ ▿
لینک تلگرام
راسا‌ دُر تنها تولیدکننده درب‌های پلی‌وود
در شرق کشور و مشهد مقدس
@rasa_factory
|
گروه کارخانجات راسا</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/689397" target="_blank">📅 09:00 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689396">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
مینو محرز: واکسن آنفلوآنزا به دلیل جنگ و تحریم در دسترس نیست  متخصص بیماری‌های عفونی:
🔹
سال‌های گذشته، واکسن آنفلوآنزا طی چنین روزهایی در دسترس بود. شرایط به نحوی بود که نه تنها واکسن در کشور تولید می‌کردیم، بلکه واکسن به کشور وارد می‌شد. در حال حاضر، واکسن…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/689396" target="_blank">📅 08:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689395">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
ثبت سفارش واردات موبایل آغاز شد
🔹
امکان ثبت سفارش و ویرایش ثبت سفارش واردات تلفن همراه هوشمند از امروز ۱۶ شهریور در سامانه جامع تجارت فراهم شد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/689395" target="_blank">📅 08:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689394">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
نهاد اطلاع‌رسانی امنیتی عراق: تردد مسافران و مبادلات تجاری با ایران در گذرگاه‌های «زرباطیه» و «المنذریه» به‌صورت ۲۴ ساعته ادامه دارد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/689394" target="_blank">📅 08:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689393">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fde394b94a.mp4?token=YC8YnqRmYqyVXuu78Tps9YmsIe3Ig7uuMixisKHGLGwNuVe3086_JUuv9zfUSxpedJmN34Ua9Emys2dq8e5F3Sxv91Mco1Ym-pYNZG3u1Ve08RcRYvETtui2mO4xjfbWvYpjlcYTDLlS_MguzSCRsYj9SxVoQInqpNrcVqIsVUtX2HVSOqwj40iHtG8I65zu4jFTMVzCjZuxMzj--oN7I-vZsDmGIvqzPQ7eSplz1VhLMW1RzrgamYAvEoC1B7eERXtI1sU75WKa6pLsyJE892dLZnvajQlXD059oOn2IjXULpIOaoTv6XF7DUxe3JFti7QUP_Y-gVtg6FsrLEcvQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fde394b94a.mp4?token=YC8YnqRmYqyVXuu78Tps9YmsIe3Ig7uuMixisKHGLGwNuVe3086_JUuv9zfUSxpedJmN34Ua9Emys2dq8e5F3Sxv91Mco1Ym-pYNZG3u1Ve08RcRYvETtui2mO4xjfbWvYpjlcYTDLlS_MguzSCRsYj9SxVoQInqpNrcVqIsVUtX2HVSOqwj40iHtG8I65zu4jFTMVzCjZuxMzj--oN7I-vZsDmGIvqzPQ7eSplz1VhLMW1RzrgamYAvEoC1B7eERXtI1sU75WKa6pLsyJE892dLZnvajQlXD059oOn2IjXULpIOaoTv6XF7DUxe3JFti7QUP_Y-gVtg6FsrLEcvQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شلیک موشک ضدکشتی ایران به دشمن آمریکایی با روایت لگو انیمیشن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/689393" target="_blank">📅 08:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689391">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
دقایقی پیش صدای دو انفجار در قشم از سمت دریا شنیده شد
🔹
منابع محلی تاکنون در این باره اظهار نظری نکرده‌اند./ ایرنا  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/689391" target="_blank">📅 08:11 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689390">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
ینبع عربستان متروکه شد
🔹
پس از حمله روز گذشته انصارالله به خط لوله تغذیه پایانه ینبع، بارگیری نفت از این پایانه در دریای سرخ متوقف شد.
🔹
خط لولۀ ینبع یکی از خطوط دورزن تنگۀ هرمز است که مهم‌ترین سهم در عبور نفت حین جنگ ایران و آمریکا را برعهده داشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/689390" target="_blank">📅 08:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689389">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e551fcbb87.mp4?token=bJKWEZMYY06OsHUj9-4dqbaSSSG3ca5TeAkJAct0aMjc0SRUi0N1jJbI2zsp_lnt4-LpYkB0liBQ9SvM0vmOEfOQ2TUlr7YfuIOGUkQ6j_u7nxJW4mT-e07JzsR5P-4xBPwajXjImFldJe1sWK2iaVOS2hJfOMTjGJaNfzP092GCZMOwUqT2de5ATnfCSdMp3x0MjVAOzU2mMDyKnMcraHl73ujTBvaJY9fpl5QZGpquPJ1J8HJrS7xO1z_tMOa4I68g4AHOI3mhexFEIZvUPyoUlHukn2nCHld9W8HuLIB025fssZ49hGUeKY4csrG3Wk3TEkHUWnCycI5qTf_hPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e551fcbb87.mp4?token=bJKWEZMYY06OsHUj9-4dqbaSSSG3ca5TeAkJAct0aMjc0SRUi0N1jJbI2zsp_lnt4-LpYkB0liBQ9SvM0vmOEfOQ2TUlr7YfuIOGUkQ6j_u7nxJW4mT-e07JzsR5P-4xBPwajXjImFldJe1sWK2iaVOS2hJfOMTjGJaNfzP092GCZMOwUqT2de5ATnfCSdMp3x0MjVAOzU2mMDyKnMcraHl73ujTBvaJY9fpl5QZGpquPJ1J8HJrS7xO1z_tMOa4I68g4AHOI3mhexFEIZvUPyoUlHukn2nCHld9W8HuLIB025fssZ49hGUeKY4csrG3Wk3TEkHUWnCycI5qTf_hPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگه زانو درد داری ولی نمی‌خوای ورزش رو کنار بذاری، فول‌بادی لایت دقیقاً برای همین شرایطه
👌
#ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/689389" target="_blank">📅 08:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689388">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8mUJ8xhFFzuPFaNsp89_TN6Exu1dz3Lc0qO6LtSc2kD1VJdoQyu_Sk483vr35n0S0pP9tUX9zUG9qX_YTC8W-zGNDutahMvKDHFw7f6Pu9nfg_JUx1zKrEDNQeAu8YmUwvjl5NCCNtrVjhiE6kj9dOcvNshiWa5qAv5bPWPGZaHDJLCzU4NFq6qEAX0xcj8vQ_EzxAenV6D0PDZ_PODNCIcrUWkG4UOIodZSt5OVgsp3JESrbaAYgTXmsWdSHVQFScxcVbFp2XiOi4jryal9bG3IQCt9POs9h1YhRsi2ZwOY9g3hDhgoIb7VfpWstAcbILUH2b_aGxjQ_ThJo5ihA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سه و نیم برابر شدن هزینه نفتکش‌ها به خاطر جنگ علیه ایران
بلومبرگ:
🔹
از شروع جنگ علیه ایران درآمد روزانه سوپر تانکرها از ۲۱۸ هزار دلار به ۷۸۶ هزار دلار رسیده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/689388" target="_blank">📅 08:01 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689387">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
سخنگوی هیئت‌رئیسه مجلس: خروج از ان‌پی‌تی و تجدیدنظر در دکترین هسته‌ای کاملاً دست‌یافتنی و سهل‌الوصول است؛ در برابر آمریکا صرفاً زبان قدرت جواب می‌دهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/689387" target="_blank">📅 08:01 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689386">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JbsthmN3r-UZtBib8qGDpAknXfLWFI0wbSycwSzRH2jx6oREEuNHlXDRHb2HbSh1t1_nFLEpW0gTiaWLLSQZ3kOCuK7Oh00-EAZcfSHnXDuZUBVhZYEm8_qFxoBvw8Xhf2M9B1hWlqUSFYs2HwhUIFYu7vx6oryt-hcnpRxS2Y21qqzb4dLOCX4iZGYZEKMSMi5qqS6FoKhVFuHPGy6-515kuXPJTd0oBR_LkPtEFQzNi1Sg-fPoI9Fc8Tu7xEmD5473XaSXTuylO_DmesEnGXQ_e8vu30BQ6CA-3VPNyKIgoabKYSNTruNaMw_a5c0cwcWoOLk4jq40-JODX_qIIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: مردم ما را نمی‌توان با زور و تهدید وادار به تسلیم کرد؛ ایران تسلیم نخواهد شد
🔹
اگر آمریکایی‌ها جنگ‌طلب هستند، باید با نیروهای نظامی شجاع ما روبرو شوند؛ چرا علیه زیرساخت‌های غیرنظامی، منابع غذایی و معیشت مردم جنگ به راه انداخته‌اند؟
🔹
اگر آنها انسان هستند، چرا مردم را از دسترسی به آب، غذا و دارو محروم می‌کنند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/689386" target="_blank">📅 08:01 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689385">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
نیرو دریایی سپاه: اگر تنگۀ هرمز در اختیار آمریکاست، بسم‌الله!
معاون سیاسی نیروی دریایی سپاه:
🔹
ترامپ در فضاسازی رسانه‌ای خود مدعی شده که تنگۀ هرمز در اختیار آمریکاست؛ اگر چنین است، بسم‌الله. یکی از ناوهای خود را به فاصلۀ ۱۰۰ کیلومتری نزدیک کنید.
🔹
آمریکایی‌ها می‌دانند که اگر شناورهای آنها نزدیک شوند، با پاسخ رزمندگان ایران مواجه خواهند شد که نمونۀ آن نیز در روزهای گذشته اتفاق افتاده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/689385" target="_blank">📅 08:01 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689384">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
اصابت موشک به یک نفتکش در تنگۀ‌هرمز
🔹
سازمان امنیت دریانوردی انگلیس خبر داد که یک نفتکش با پرچم پاناما به هنگام عبور از تنگۀ هرمز مورد اصابت یک موشک قرار گرفته و از کار افتاده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/689384" target="_blank">📅 08:00 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689383">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AuB_vvZqabUIQStLwp7Wjnx23y1RCuiZYYLPKFaT-DsFce-U8Jjn1QNGmVGdjMYOSToBoXorme3PWlBBt3jM4ceR3vqnUf6erTpPde5TXR_2uYwwUmcTRVLJRgRhq5U91-Q-efHkVGlEZYaP5PBrMD1v_dxfmL9iv2L65ltt9FxlmtpBRIj4oVmKgoUE2eGXvXnuT5KhJtFljOXyMqGKYQ9kTeKd2wDTH_E3R4prXvJsBf0gCUjLd3-iVk_4ZBJAMlkfy2Ge6mxT1c1C_fdQLIcjuw_ay1FBwdEL0VIrPLsILMxuw-O5bmJ_TOvXTWeFWlrkiVg1J8y7laRo5fM71A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز یک‌شنبه
۲۲ شهریور ماه
۱ ربیع‌الثانی ۱۴۴۸
۱۳ سپتامبر ۲۰۲۶
یکشنبه‌ها
#حدیث_کسا
بخوانیم
⬅️
متن و صوت حدیث کسا
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/689383" target="_blank">📅 08:00 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689382">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lt0I6rX0Sj0MMbKQ7DHjLQSSk7L6X8oijnVfoyhOJA--NHB5P96s-CViRrHBWTered6guUc6Q4eJChIt1itB9_ntD7flcQNHtnRktzE_sO15TRiIVzVpAVMUPfwijzJqiuxzPmTEpdMUQmLuWPbmLnDDceh9wtjCakwFVmExM2moM7aBCE4HwAshqnSNKcTgvg5EffACUeNSzz7t6Inx2-NrMGxwL47pCRbitoPFUTXjgYvnxqrZoFcpWJQTDlN6BQ5vOJ8w_o2p3q5YcY8f0lt73Kc6T8IK3CJ99LUZan4OGhhZEKfK38C0apMHo5sofISnzDwfApIYkaW1GWsHpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رویای تحصیل در خارج از کشور رو داری؟
🔻
قبولی دانشگاه، بورسیه و ویزای تحصیلی شاید پیچیده به نظر برسه؛ اما با انتخاب مسیر درست، می‌تونه خیلی ساده‌تر بشه.
🎓
🔘
در انتخاب همراهت هستیم برای:
✅
اخذ پذیرش از بهترین دانشگاه های خارج
✅
بورسیه‌های تحصیلی
✅
ویزای تحصیلی
✅
پذیرش در مقاطع کارشناسی، ارشد، رشته‌های پزشکی و دوره های زبان
✅
دوره جامع آمادگی آزمون پزشکی ایتالیا
🎯
نمی‌دونی از کجا شروع کنی؟
✉️
فرم درخواست مشاوره تخصصی رایگان رو تکمیل کن تا شرایطت رو بررسی کنیم.
🌐
فرم درخواست مشاوره:
https://ezam.entekhabafarin.com/consultant
⁠
یا با شماره های زیر با ما در ارتباط باش:
📞
۰۲۱۷۹۴۱۲
📞
۰۹۹۸۱۲۵۱۲۵۴
✅
@entekhabafarin
موسسه انتخاب | انتخاب درست، شروع یک آینده بهتر
🎓
✈️</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/akhbarefori/689382" target="_blank">📅 00:33 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689381">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">راز بیورزونانس و فرکانس های زیستی که این روزها خبرش همه جاپیچیده وبیماران زیادی رابهبود بخشیده ،چیه؟
میگن تو دانشگاه امیرکبیر مثل کشورهای پیشرفته با یک سیستم تشخیص هوشمند، بیماری ها را تشخیص و بهبود می دهند.
🔹
اگرشما و نزدیکانتان هم بیماری دارید که کلی هزینه
کردید ونتیجه نگرفتید حتما باهاشون تماس بگیرید
👇🏻
☎️
: 02166961000
02166961005
02166404713
جهت دریافت نوبت مشاوره تخصصی با شماره زیر تماس بگیرید
👇🏻
📞
: 09912250295
کانال تلگرام کلینیک بیورزونانس دانشگاه امیرکبیر
👇🏻
https://t.me/bioresonanceclinic
کانال اینستاگرام کلینیک بیورزونانس دانشگاه امیرکبیر
👇🏻
https://www.instagram.com/clinic_bioresonance_amirkabir?igsh=MTVmNHd3eHM2YTFlZg==
کانال بله کلینیک بیورزونانس دانشگاه امیرکبیر
👇🏻
https://ble.ir/bioresonance_amirkabir</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/akhbarefori/689381" target="_blank">📅 00:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689380">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmacqKUeGuG89oGNGw5PSC-tiwYPe57hGvzZ12ruQfjq3gM625m_bQiLHL_RGwruAM8F_QMa5-_HuyA7DdrkOZChoRDk1ff_lesSuL5OFUzck-xkMrRkBDZU3jEBTMSiLFw8u-c2hHeIOqdlctuqhEA_DIWJc2ey1CJdcyPvfuFoQO29Cds12DK3MOnAmQILK1qhD0289bpSmFuXgCRlfcbGuyLk4gGiFDKwNbDWmH4itOXt3MhmqI82aD9gJ43wux0DDwlnh0FGDVXZ5X6IKVgv7qBMI8a5NdY825LN3bz8Hb_a1AaKntMXVlPyDZf5lkwUqV2adouOwv-PrnZizA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👟
جردن شیک با قیمت 1,898,000 تومن!
🔥
اگه دنبال یه کفش اسپرت مردونه‌ای که هم
خوش‌استایل
باشه هم برای استفاده روزمره راحت، این مدل جردن Avin رو ببین
👌
✨
رویه زارا
✅
زیره PU سبک و مقاوم
👌
کفی دوردوزی‌شده برای دوام بیشتر
📏
سایزهای ۴۱ تا ۴۴
🏠
پرداخت درب منزل
🔄
ضمانت تعویض ۳ روزه
🛒
خرید از سایت:
https://memarket24.ir/product/brief/46467/180124/</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/689380" target="_blank">📅 00:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689379">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/luJTslT2wMfgd8xsdLr6UdPSN5RCi4g9cNwjNg7fwmyb484OlwZegaXLaTNNJAenYrtW3oS0IJe9rtLnHZuCsEWvKWamgAOKg0we-J5qDu5gi_DL6RKHTsHVyI0cBV01qCLl8ZtDcwCQHCY0MG5rQpVT5ps9_0CPwXpWSQ3_-BJg8_kLRyIo_f1Wp0xUSqgkNeux6ny9VQom8Q5Ji1Zqr7hfkY4hg8iagbzEPGV4NOnHw5IQl-Sbpl6QTBL_1z1Jyy6ngm5U0wFrjbjCaZlS4zUA99FdIj--mm__lBDpJ8FyJcO3LIun5WT6MESaRl7hE79rz4ybnGmVyjhdTefygA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر می‌کنی چند نفر باید تبلیغتو ببینن تا نتیجه بگیری؟
👀
نه ۱۰ هزار نفر…
نه ۱۰۰ هزار نفر…
بیش از ۵ میلیون مخاطب.
🔥
📣
پکیج تبلیغاتی تلگرام؛
کانال‌های کشوری و استانی خبرفوری
🍂
جشنواره پاییزه شروع شده.
فقط «پاییز» رو بفرست؛ شاید این بار نوبت تبلیغ تو باشه.
📩
@Mahdavi_fahime</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/689379" target="_blank">📅 00:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689378">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e1d5f13fb.mp4?token=VfJxSqy9qhOlpJqlyTJdhceUZR2iGTZbCl0TIK3MoI4WzIfx6y_3KmhTw31Qu3q-_aGeOsXF5LNrVuBRamemvSsAMSNqXEh2jZbtBmwrKOTRbfU5akDa09qZfnlXtAvQHhw4dcUI9o_n57TbGShK4w0cijpb-NphNILkOEyhdY14_L71AgWmwL6DKwG0ytoVxXXcG2buOfeKaobaRdJGeL-TGkF209mhGwYJGd8C50rFnaT24Rj8hXmbILcmdOVuDooFlbuAgKUmc0jQXlUor36W8gV8TSeTsNI45bzBEEVHZaZkgW_UABswuI60ut_lzPUuxIJVtf9y3s29iFSREr70O9TSKAUkN2oouDymRQ52KyVE0U-ftgSgjtpOD2b2L4U9F7w0_5hlBNW9KGvYvVR7SyviXg2ngZAbs_HIh5W8DY1argtVy9oUjQIkkW0blegI7vQjXC8sVkdXWZzXbviNA6JtE8bVyDuQ_qKx13BM6OjXjPUJztx5xC0oFO70OKXqVORBJkRWeFCxKyXU9dOXBQz9nNqsGC1JKlUXaZQ8y_dipwWPazihBXPt489IlXuxJYVejWfVH5MRH7hm0wQhmv9OyyiTg6Kj-A4P9yspaJ3NG42vIPvKjXi--LxbBzk2hTztiNRPfKaTllyGxvZlt517krfX4Sr27yOOaLs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e1d5f13fb.mp4?token=VfJxSqy9qhOlpJqlyTJdhceUZR2iGTZbCl0TIK3MoI4WzIfx6y_3KmhTw31Qu3q-_aGeOsXF5LNrVuBRamemvSsAMSNqXEh2jZbtBmwrKOTRbfU5akDa09qZfnlXtAvQHhw4dcUI9o_n57TbGShK4w0cijpb-NphNILkOEyhdY14_L71AgWmwL6DKwG0ytoVxXXcG2buOfeKaobaRdJGeL-TGkF209mhGwYJGd8C50rFnaT24Rj8hXmbILcmdOVuDooFlbuAgKUmc0jQXlUor36W8gV8TSeTsNI45bzBEEVHZaZkgW_UABswuI60ut_lzPUuxIJVtf9y3s29iFSREr70O9TSKAUkN2oouDymRQ52KyVE0U-ftgSgjtpOD2b2L4U9F7w0_5hlBNW9KGvYvVR7SyviXg2ngZAbs_HIh5W8DY1argtVy9oUjQIkkW0blegI7vQjXC8sVkdXWZzXbviNA6JtE8bVyDuQ_qKx13BM6OjXjPUJztx5xC0oFO70OKXqVORBJkRWeFCxKyXU9dOXBQz9nNqsGC1JKlUXaZQ8y_dipwWPazihBXPt489IlXuxJYVejWfVH5MRH7hm0wQhmv9OyyiTg6Kj-A4P9yspaJ3NG42vIPvKjXi--LxbBzk2hTztiNRPfKaTllyGxvZlt517krfX4Sr27yOOaLs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از کمین نیروهای مسلح یمن در مسیر مزدوران و نظامیان سعودی
🔹
این عملیات گسترده با نام «والله اشد بأسا و اشد تنکیلا» از چندین محور انجام شد.
🔹
هشدار؛ این ویدئو دارای تصاویری است که ممکن است برای همه مناسب نباشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/689378" target="_blank">📅 00:28 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689377">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
بازخوانی پرونده قتل کارگردان مشهور؛ بابک خرمدین چگونه قربانی شد؟
🔹
پنج سال از قتل هولناک بابک خرمدین، کارگردان سینما، به دست پدر و مادرش می‌گذرد.
🔹
جسد مثله‌ شده او در سطل زباله‌ای در اکباتان کشف شد و اعترافات بعدی متهمان، پرونده را به یکی از پیچیده‌ترین جنایات خانوادگی سال‌های اخیر تبدیل کرد. بازخوانی این پرونده از لحظه جنایت تا اعترافات تکان‌دهنده را در این گزارش ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/689377" target="_blank">📅 00:20 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689376">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
برخی منابع خبری از وقوع یک حادثه دریایی نزدیک سواحل یمن خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/689376" target="_blank">📅 00:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689375">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
روسیه: تاکنون ۴۷ متخصص روس‌اتم به نیروگاه بوشهر ایران بازگشته‌اند
🔹
تعدادی از متخصصان در چارچوب تعمیرات برنامه‌ریزی‌شده واحد نخست نیروگاه بوشهر وارد ایران خواهند شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/689375" target="_blank">📅 00:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689374">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FgQsH5gXFYlItXnX52JPcfUvILSi8W4jZsvSFlpML8PX5LkQhiqeCYRsDLLokX7e1ExomzaMM7bi93zgdLUGXB7vfAulJZHd0PSNtQyu4q4iwNP4nyqrc1-b-wf1cJP3797ezuiYrLQ94jw2eitqGJnyNWm8goIaydFLqaN2WkXK25N2mBY3e5Ybx25-XhcMCLcoEiU4ndsCoYWM8bEMMVjZQkOHFZZc8rLA1BXwcuwuAjz1piMEa5-YjB2rJYPhX0fRuX7Q_Q3tEu3SMxx-LjsBw3LWLTG7O9jTQL0EHrcZhis5TiVstKDe5FID-BujVhwcVByUyGuwtbfca_YT6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/689374" target="_blank">📅 00:00 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689372">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/163bee97eb.mp4?token=ViK6F-erfxK5weFGW3sQ-JJq2ON4sUePJZUTDIwZYiUJX9-WbxRV1jjd4VHnhAgQgAyZVq50DX6cUsxAdW1NdlgDdO8NhtUgep0p0W1VNE2abGSX9NeH6q0ipsbwKkln3vS6cFR3gCtZ6Im5_MTEna4T_nzZXhxQilqesDYs6xIj14W-qD19ppC3YcCaCPcTcqnlvQmMNpiquqo4cuPvQX5geuA4IChRbOkse1SQLhUC7E3q04LMtWPwOAqgo73JSdcXuUxGvWiopSTOTF-k9xHzuQiVLDTUio79iZxFOuWK5vLB__L_dRh1FnT8Xwuis-y9sPhG0x3JOHXh1OaRWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/163bee97eb.mp4?token=ViK6F-erfxK5weFGW3sQ-JJq2ON4sUePJZUTDIwZYiUJX9-WbxRV1jjd4VHnhAgQgAyZVq50DX6cUsxAdW1NdlgDdO8NhtUgep0p0W1VNE2abGSX9NeH6q0ipsbwKkln3vS6cFR3gCtZ6Im5_MTEna4T_nzZXhxQilqesDYs6xIj14W-qD19ppC3YcCaCPcTcqnlvQmMNpiquqo4cuPvQX5geuA4IChRbOkse1SQLhUC7E3q04LMtWPwOAqgo73JSdcXuUxGvWiopSTOTF-k9xHzuQiVLDTUio79iZxFOuWK5vLB__L_dRh1FnT8Xwuis-y9sPhG0x3JOHXh1OaRWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری زیبا از بندر خمیر؛ تکه‌ای از بهشتی به نام ایران
😍
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/akhbarefori/689372" target="_blank">📅 23:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689367">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZRIAIEzaNx3OhlbxPDXMxKt8FNnBoyLz7aZJRx0_Q212BXHdh8ZF-kLk5bBvUb2MAAGwVvfckNBsBGRWI8pAHq_iReBE_uKin-K_exsiFuOea8ePeXWngBs5stR2Fe0PipcaQ0A44qtXo_gkhRi43sIAH75D6N1TbaiNHjBOgTb826SfMH_f9Zcu7Gx7sEAB2raRHj1PDN5KiAHC4lYI73k_P1W2osSeOhb2c5bDZvjThJSdAtgyjCBS0SrfictRSPYhbm-hq-taRYDBXFTt7pxdsMz3tlRaAg4-1Bj3M6z0ikp8wALeh-cviyqttp_0QcBvOYSXDjKUdC9-jtVKTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L8zug8mYqqM4Q0SM4Lt1_1db8Yp2mV3VWPO6c-EWbgdLrQ8LHrrgWL2cMK2vbQ5OxJxMiMH9c2cRutlSjIrLJ4NPPOzxnXkFBe6olUz0O-WPJ_eG1H4aEJ2PNJm3biZlnbzvJ1hgrWeCjzbpYa1hOxEJGwImIIjrLEXh3B4-YbvjoDE63oAdOglTEs4qjJt_8XHGi3tfwsWihMb5IvEGT29pOnt0ZlPGZEM_yiR2z4nFC4MEbCojCoru8bGUpBJ2a18VbVy_Q1VnntVrK-64ovsuiI0E0dVy23ZzdP9eCHVS0Ozg40DvlT_m7H18BBtGrYnovc-zGdL-lnHScS2fOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vTK9ZywtioumivVSc4M0WRunn5B_w3x_IzwTnwJ3xzceA-fI0vGqKlXARU9NbHORE5ZmJe3EOZThYxSN_YTtrvPZ2ysOpXYK0DfpEto0XMjFJwbuy1X11C-3GntVbsjvDjcCg89U1pHy5k29CvxZdKkbbyJI23DsObrxQ6r_y6zHPGm3vn6nnG2FBXn8nIHRLo961hQpa5PnUnvpqjyUUd8Eu-uqRBNH-4qOyzClu69x1s40_UIE5kT_jxGlwdctadom8up4m6_gBQLk6nhafZ7fRSzez1FIb6enEuHG-wMx1fSGXMuOaw4za1r7o5EUqUn37v5doseX2slL7HpMPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e1vajhBiat65yZ1yyEUme6otvIB0UNgrc-mFVpW7_-nfIsZgg0oJpvog0A4A929hst-IJEaTVz1zGdNC1d8EM5bRTMxpfanYzSBvSGiT7RfewYSMMK8nJcFYS-00HP_mezcWwrqAABo8j1Dc1bzE9rXagPQFYVKyG9RR5FdRjqeb9gAcSBixjzaFl-4AlCV4aRcVkjDux981cmTS3iTgSpkr2peVoGS24EQ5N3QjeGKzf_jw7Tz8ZqEM_YkJ3hTO57BFMaa3nHZGGd7ZDCcyV75ZvDjd80GUIPTDME_i0LdSuXQRoQyPkfsIb0NDtR_8j5N3u1vr5ZJwBOELtQY0Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CFp7R7AVcOE9dSnw-j3f6Q-y1c0vb8fi-DgYJL0Z12QsNe6HGLkS5k9QSnpZWdARJXZquCWrCJ1aHU2UwGpyVp2Z4pl0U902LiEwTMCRkk-FDsLY_0xZzdCH-VbekqAUgzmQtB9aHgPbNqefasj28HfXDbi_DM_Sab59lYOSDpYn18C6CVH4s5tcc5o2BbEVoTvWQN1QUQYsHxzJ5bP5c6e6-0u2YPBjv06QyBVsEBaDZJI_oS46fTHkRVHXuTyxrfo1HiFvWwZxFZS-mPpiNmAeILmMRbwfEPxAt58CgLnevA7irn2-5A6DonpM_qg5KU-rLajpu0sqC4f4fSIFqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⬇️
همایش هم‌اندیشی مدیران صف و ستاد بانک صادرات ایران برگزار شد
✅
تاکید بر ارتقای کیفی شاخص‌ها در بانک صادرات ایران/ افشین خانی: اعتماد پایدار مشتریان، پشتوانه اصلی توسعه است
💠
همایش هم‌اندیشی مدیران صف و ستاد بانک صادرات ایران با پیروی از شعار محوری «پیشرانی شعب، هوشمندی بانک؛ ارزش‌آفرینی پایدار» برگزار شد و راهکارهای عملیاتی برای توسعه محصولات مشتری‌مدار مورد تاکید قرار گرفت.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331
#اخبار_سایت
#بانک_صادرات
#بانک_صادرات_ایران</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/akhbarefori/689367" target="_blank">📅 23:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689366">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_f_CdzTkCd6ItYSl1nZFx5PPV4iplvuZTj0-Te9eWg2FSrVMf1fbfqXVjsKzND4BYrEvdwTkjTF8rDf-jTuZXJWBch_UtxrnXB_SCosFO_yTz_NWJk4Cs98yT-0t1ras-uQjDIy1RSgTjUrtmWCVw2fbN8jODwhWlfxIdHmahNR5AtHjbx1DcVl8uUNtj_BevSpoQ_MTUkFmjOVm0hsykYFQ6rX7QjBEKe2nMSgL1lLmw5o6Rul8JaN2vn_-0Dd-Dsbl_kl-fc46xCIB6gbRY94PMX4PSPSPlk5wulhB7cuj7xrYPJUNZiiHcuPzWWAT6EfwmM5x3ZLLYrxEi_T-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر دارایی اسرائیل: باید شهروندان ایرانی چیزی برای خوردن، نوشیدن، شغل و برق نداشته باشند... ایجاد مشکلات اقتصادی برای مردم آن‌ها هدف ماست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/akhbarefori/689366" target="_blank">📅 23:42 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689361">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f9PR5FS6WorM6iKmAfEiCGFltTmoZUGzigXMsFRKV6oO50XpysfMCfxvCpeV-cGGtrf_3pbThcYIxgSUpuyLPG1JZFhSEjUR_MryysW4YGykG-00mEc07rK-nSEiR7hDd0NZboIR6laxVOKhpoTHDQb2-Qx1sWvh4El3-YuOw1cca5qWY1AwkVuX3klr47P0VlW6N4wlJa-EMQGPX8HtELtV0p6nklfkE-I2iqlh4OWzhSqmHXZoBCl7qopsdP6B8xTMiR8W-lCcnmiNSdG0YeODFU0ibrUxJEhGZxbG8O0MQ4pugcAbCOTNAREiJRXN4d-gG6o-4HwZHS-qt0vRQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dj7n37SL80aj41xdZG7rp1urFkbM5m33HKxZtqC2G-JM5wFLhBlouOnNf4r2NUJ3ja8rt9zYSKSXjxyTZBehpg_T09-L2qohwEEyBEl-_0adbNVhfRC9Q9fO1bxA8od1OuTdSuJYwmz10RHqsH6VXaimLWyYH1hm1gyDDTT42-PIymg-q0QgessQmteWjR1DQoE8nxA5QlutMRdCjlUi_9uUuDyv9jo657sC_HMD7xEORsE979JcBbBjmZ8WZceMgfEDL0-s89PbNc0O67Sb8JysOiwvlBKzApijFKtjn1k5xomWCYPJVPsPR_CLSfG13ugOOjudkBBfOjELlfTjkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PvxK7lHLnL-cykyDVXQTbwZFNscyIgTsOeeKf2amMcGIZ0A0NFBk8aTshamymAMZvVIeJ3AVkjPg7b4OfkiUccUqOvYwX4im7GwcqkTZUCIpVoZ2-vgks6vsk6GsBlDBZxEXVECCUtEWOb_58TCZEbYBH6I65sD-EyZHIZOELipUhYu0DreCEP0d7cU3U-ywWiSuNZesUtVhcH72BaAUIYCq2YZZZDF_xlzromvFnQpQgJDTenRVGiDw6u1uWFH_GYY7LCWM-ewbi0Arv4N97_e1r3fdlJqwsIdzJX8yG1sYAgAGSK2youWdjVxCBgLI-IPNdr61teXexAORhCoP4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eST-gaR4o3YvTAmFmywCZQUyF4uB6NDW1CHN_fsuwu4-RBMNkS9fP_Ri84QTMsmZsQe0VrRZziEQ2E0bYau2f1WL3C2iPRGk-snGilFHmJFR8u8vcxEEl4uS2-QxEpDSK9z5_n_C-3QvZqbWVh4OP5wlAPLpmm3xVJLNYnc2I-aHCl6EMgmFfpDTykOR2uG_GMyYV6LifXvNdYOxWHcl2lAu2rdGuLo07QLrmhbJPNbBi2CgGJ00lnKkDkSShaTvhilynxNNKWpE6puHruIjARhXZOFb_KA2u9L5cvZHAUU5paPL8LP3gdm2CqmEZYy9gpfeI5VmUM0yzOis381nJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KbxsL-QxT6uiriwN117GZ6fPN1cJqw0sjU6J4XdVAnkM5Vz6_Hm1qBZRrduEYwZL86RroXBVxsrwkA31YUdHm039o_qTC-zYeFDU2v_4rh-fpHM8dgqiVgQhNmmUSFRwPe-oQJrh3_jX5iIlXDdZa6HRXObtFUqrQ4DNKVCJzzyiIHLYRsx5DfVRSkDtHiDFb7LwQzysUi9mE5LyRbC7H6dxNXsgYZVAk3siPJCy53SHxtflrgxcgk33MSnBjpf9OdHShE4oWP8JXFEZqx_gKyXHH7wUJE4tQXGy-YkBQKOhhCql7L9VMuhXAHJT_gO_g1K8Qlz2qorcsluFgJR0XQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
سالادهایی که هم به سبک‌تر شدن بدن کمک می‌کنند، هم به شادابی پوست
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/akhbarefori/689361" target="_blank">📅 23:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689359">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
کارشناس صداوسیما: اگر رهبری اجازه دهند، ظرف ۲۴ ساعت از سلاح هسته‌ای استفاده خواهیم کرد
🔹
خرید فیوز هسته‌ای از کره شمالی کار خیلی ساده‌ای است و ۵۰ تا فیوز می‌توانیم بخریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/akhbarefori/689359" target="_blank">📅 23:11 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689358">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f55a577156.mp4?token=ferfzAeolb-2S-sWcZ3OEZWsYR8MCPzwytdn6oSu_AsT7FBsHL125ErsGY01cFGmjJs5IAMdvK7y2BQ0WdfCaF6QoYZ4_PaiFgl4Gw4JOCI238LR9zTtmoMhRgpcqkq-gm789vBZs5uTrvGT9ilFsEBbrJNUH7slr4HPhTvYKF4vsr-3g1ePZHzXgd5V20vNETTahrrb4bm4silgOIf3PddZ4tJV-pfMCdy81gtNRiLbi6NeaCN-_TxSH9YiqGwLlVCxmR3V3xxiXwSjuCq0Bqs7S7e9TwXJ4qZrq6bkAu7gUXT7UlsWjsaIXSsDhAi9G1XjlLBkypo4d4U4s8BMJ2Rn9KFkoe2ZUzXDU2JhQw159wXHVdj0N16MckfW4Ab9C3WKNSJNGUytJk4YcEMlNnYCSOWg2Y2IdWGrvxBRoP6u_aXUfb6EfbvLzKJAznwGcCCp2POPSidecZ_kCA3RVSb6KAmVIVmeVWXq4zR6zHCR3ikeJ90mK4ReMr9AukGlpsivfyCBYkPg02E4AJUC9qzW6zidYIXonKLbGfb_CgHH0c_RtTIm5-qIwIB00JCk5v5TzQyJmvNIoi3gu5l8QQNEVE8ENHbl5k0VYRJvXdoDaQBl7TCl-hnsut8spoUfiRHNF1FVXMRhWoirVtwqmDjxPqUWOj60F8M8tZ5Tl64" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f55a577156.mp4?token=ferfzAeolb-2S-sWcZ3OEZWsYR8MCPzwytdn6oSu_AsT7FBsHL125ErsGY01cFGmjJs5IAMdvK7y2BQ0WdfCaF6QoYZ4_PaiFgl4Gw4JOCI238LR9zTtmoMhRgpcqkq-gm789vBZs5uTrvGT9ilFsEBbrJNUH7slr4HPhTvYKF4vsr-3g1ePZHzXgd5V20vNETTahrrb4bm4silgOIf3PddZ4tJV-pfMCdy81gtNRiLbi6NeaCN-_TxSH9YiqGwLlVCxmR3V3xxiXwSjuCq0Bqs7S7e9TwXJ4qZrq6bkAu7gUXT7UlsWjsaIXSsDhAi9G1XjlLBkypo4d4U4s8BMJ2Rn9KFkoe2ZUzXDU2JhQw159wXHVdj0N16MckfW4Ab9C3WKNSJNGUytJk4YcEMlNnYCSOWg2Y2IdWGrvxBRoP6u_aXUfb6EfbvLzKJAznwGcCCp2POPSidecZ_kCA3RVSb6KAmVIVmeVWXq4zR6zHCR3ikeJ90mK4ReMr9AukGlpsivfyCBYkPg02E4AJUC9qzW6zidYIXonKLbGfb_CgHH0c_RtTIm5-qIwIB00JCk5v5TzQyJmvNIoi3gu5l8QQNEVE8ENHbl5k0VYRJvXdoDaQBl7TCl-hnsut8spoUfiRHNF1FVXMRhWoirVtwqmDjxPqUWOj60F8M8tZ5Tl64" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این جزیره دنیا را به هم ریخت
🔹
یک جزیره فقط با ۱۳ کیلومتر مربع مساحت، تبدیل به بحران امنیتی_اقتصادی برای کل دنیا شده است.
🔹
جزئیات را در این گزارش ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/akhbarefori/689358" target="_blank">📅 23:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689357">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-0bwrXa4XTpLDpDg1JhlNTIuzhhtpfZpTlNHSadHJkykN85r9m4i-jkEG5_vMg6DqTJwt7xfCVWCql1_-Mbgjm__93vxsBCo12IRx9afOoBifcoCSdpCUynNhAzGzaKdaVkUymqVMzj-8wCdWgZvL1kAv4CEuwFDdzmF4ePMJVBk7uraTdP9pwZFMsh0_MBpYxg48zcK0ySanMg1jplJ2TbxjlmxRwqQHoS-aWXXD0Rem7zdQw0OqK4wgRr_WiwtPrTNvD5BB10BT6IbshdPkdTSXss_RxTazovMSyPZQlWyX77WML4QC7bkCbe24X83pMZC0PvfMIs2FqOXlwNvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برای ساخت شات‌های هوایی سینمایی، همیشه به هلی‌شات و تجهیزات گران‌قیمت نیاز نیست! فقط با یک عکس حرکت دوربین رو طراحی و ویدیوی حرفه‌ای بسازید #هوش_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/689357" target="_blank">📅 23:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689356">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔹
خبرهای داغ امروز را از دست ندهید
🔹
🔹
جزئیات جدید درباره تفاهم نهایی ایران و عمان
👇
khabarfoori.com/fa/tiny/news-3244741
🔹
سرگذشت عجیب «بانوی غبار» | زنی که از ۱۱ سپتامبر جان سالم به در برد اما حادثه برای او تمام نشد
👇
khabarfoori.com/fa/tiny/news-3244720
🔹
گرسنگی به‌عنوان سلاح در محاصره پاریس/ چرا ترامپ نمی تواند تاریخ را تکرار کند؟
👇
khabarfoori.com/fa/tiny/news-3244515
🔹
در اجلاس بریکس چه گذشت؟
👇
khabarfoori.com/fa/tiny/news-3244693
🔹
ریما رامین‌فر چگونه این‌قدر لاغر شد؟ | راز یک تغییر دو ساله
👇
khabarfoori.com/fa/tiny/news-3244433
🔹
صفحه ویژه اخبار پربازدید وبسایت خبرفوری را اینجا کلیک کنید
🔹
khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/689356" target="_blank">📅 22:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689355">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOb3h_drHATll3-7xRGFFvZ0jSPRnoXlBQ6lNeqXKuPtrMs4S1o_GydIN13MFODHKmijqeuIfgaJq05KoOO76XveEz2QxgAUhbr1o3OaZXdcvyX8f7zDb9wtJjK1GW0RMK1BjHO4SsO-srWTOBJqakUc4AcF_3Cfdpqtxg97BI-IP2Le46cRk4FSCdFrywbZWVBU31uh52sq1CoqQ4pMFQurTv29baKuuzxsVSBRBaJW1sMnusAiPQCZLwWNomiJS77DJGCPAf4DDiH1kV1IM5VfQluKpCA6SkLFQKcmEqXIMtYML7CL5iwipY7R-8FyuC2BsUIV8beNjeMahZdEWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقعیت ژئوپلیتیک و اهمیت استراتژیک جزیره میون یمن
🔹
جزیره مایون (پریم) با مساحت ۱۳ کیلومترمربع در ۳ کیلومتری ساحل یمن، قلب تنگه باب‌المندب و مسیر تردد میان دریای سرخ و خلیج عدن را کنترل می‌کند.
🔹
این جزیره با داشتن پایگاه هوایی و فاصله ۲۰ کیلومتری از جیبوتی، یکی از استراتژیک‌ترین گلوگاه‌های نظامی و تجاری جهان است.
🔹
در چند روز اخیر، نیروهای انصارالله یمن کنترل این جزیره استراتژیک را در دست گرفته‌اند؛ اقدامی که اهمیت نظامی و ژئوپلیتیکی باب‌المندب را بیش از پیش برجسته کرده است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/akhbarefori/689355" target="_blank">📅 22:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689354">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4cc63a880.mp4?token=vtbxdeBdq8V0sTzOrc7IKmzN7LzZ2bf-xJZeq9hmWLx8KckpA6SFJJx0DLnyUo3SojRYlseb-bsjjLznZaytlwQ0I0P7yhUa6kw5wNdv4vySHo9gSz13dyZdOEOU0-Mn0uxb63YvsF_JuQmi0SOgUOg1DOZxmk6fMefinDVtXBdEycMZonXg1_TWTYXP5BsDJ03KsfXMbsKuvu-P6ceqBTaZZYxDVMVFE3_IRa_xPtHII-MtqmBLfBwRTQMlWgakhmLmIzMlUzqIFe4HGmTzVVAL5r0ejdEkOZGhncu5zFU3PG0cY2zKQLUC6j_jA-XdPGbEKrCyMz4iw040gF9SRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4cc63a880.mp4?token=vtbxdeBdq8V0sTzOrc7IKmzN7LzZ2bf-xJZeq9hmWLx8KckpA6SFJJx0DLnyUo3SojRYlseb-bsjjLznZaytlwQ0I0P7yhUa6kw5wNdv4vySHo9gSz13dyZdOEOU0-Mn0uxb63YvsF_JuQmi0SOgUOg1DOZxmk6fMefinDVtXBdEycMZonXg1_TWTYXP5BsDJ03KsfXMbsKuvu-P6ceqBTaZZYxDVMVFE3_IRa_xPtHII-MtqmBLfBwRTQMlWgakhmLmIzMlUzqIFe4HGmTzVVAL5r0ejdEkOZGhncu5zFU3PG0cY2zKQLUC6j_jA-XdPGbEKrCyMz4iw040gF9SRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نصب CNG رایگان برای تاکسی‌های اینترنتی
🔹
به گفته معاون وزیر نفت، تاکسی‌های اینترنتی پُرپیمایش در اولویت دوگانه سوزشدنِ رایگان قرار دارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/689354" target="_blank">📅 22:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689352">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_xNj-qDZGVTMATC-HjJ-dTKnXm3ebd47mqoVWnm0fyZ9oCbXEURnadqyPBuXKeijmqRXVXsZ9xQTZu9ujqDN3hXRm3ZUWqIIFH9zZJYmIS2LbTbwyL_aflFV8xF0B8-FFPh2ysUjrM414RPMIVDpdJwV8QT9vNxx-3H5ienodNykZUFd5Yd4stbLYJh9KjhHr3P3lugs_dhitGCeqls1bYcpvA7BwLFOMMoOXIUY6qyDXs8iXCYUqsku9kwukoQgJjaxamhu90kkyDu88ykxMH3thxP0oOYN6AkZauMj-AmrMf1zYcMet3FdxX5K63G_9NcH1JyTsPj47r-B-AZCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لاله مرزبان جایزه بهترین بازیگر بخش «افق‌ها» جشنواره ونیز را دریافت کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/akhbarefori/689352" target="_blank">📅 22:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689351">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
حملۀ عناصر داعش به مقر ارتش عراق در کرکوک
🔹
هنوز ارتش عراق به صورت رسمی این حمله را تأیید نکرده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/689351" target="_blank">📅 22:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689350">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8DY3cuCYHW-R4GSH8wri_PNaKLUdY_StvrUgeKp1x5y_El6asMkDBE_ITZ0YK9oO1Yj9xuVTf61hqe6PmF4VZmGpBfUzovKPdRLt7jtO6EFzIYEAtwfUnATKo79cBz1rqw8e4LsWFovfBAFZVfCFg_onhUwDjO0K9WHE9FMWn39X8MYbwmNzAAXChcrPyOLgplv4KStiCASnZlBqs7RLoOHynv2oBM8aGsq0FWLMwdIM7jAa7vQLVZDvEsknwFt18kNSHlVaqbpn8UWp8wJv9xtXrDsKtKPwC-_zGjCkdlaEdy69634lk3rorLArDcKLSn6OfhSFRW29jsng7RyVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فهرست‌بهای رسمی برای کالای ممنوعه! | اقدام عجیب گمرک؛ انتشار فهرست قیمت مشروبات الکلی خارجی | از آبجوی ۴۲۰ هزار تومانی تا بطری ۳۱ میلیونی
🔹
انتشار یک بخشنامه پنج‌صفحه‌ای از سوی گمرک با سربرگ رسمی وزارت امور اقتصادی و دارایی، تناقض ساختاری و دیرینه مواجهه با پدیده مصرف الکل را دوباره مطرح کرده است.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3244728</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/akhbarefori/689350" target="_blank">📅 22:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689349">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
معاون سیاسی و امنیتی استانداری خوزستان: مرزهای شلمچه و چذابه به‌صورت موقت و محدود تا ساعت ۲۴ امشب برای عبور مسافرانی که پشت مرزها باقی مانده‌اند، بازگشایی می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/akhbarefori/689349" target="_blank">📅 22:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689348">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
ادعای منابع عبری: بن سلمان به ایران پیغام داده که جلوی پیشروی یمنی‌ها را بگیرد و در عوض امتیازاتی به ایران خواهد داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/akhbarefori/689348" target="_blank">📅 22:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689347">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
قیمت لوازم آرایشی و بهداشتی تا ۱۳۰ درصد افزایش داشته است
فرود امینی، رئیس اتحادیه آرایشی و بهداشتی و عطریات در
#گفتگو
با خبرفوری:
🔹
مواد اولیه، کالا و محصولات لوازم آرایشی و بهداشتی مستقیما با قیمت ارز ارتباط دارد و برخی کالاها ۷۰ تا ۱۳۰ درصد افزایش قیمت داشته‌اند.
🔹
در حال حاضر ۸۰ درصد کالاهای قاچاق، تقلبی و حدود ۲۰ درصد آن کالای اورجینال است.
🔹
در بخش لوازم آرایشی، تولیدات داخلی پاسخگوی نیاز بازار نیست و هزینه تمام‌شده تولید داخلی بالا است و ظرفیت برخی خطوط تولید به‌تدریج کاهش پیدا کرده و با توجه به شرایط فعلی و محدودیت تردد، برخی محموله‌های مواداولیه که باید دو ماه پیش می‌رسیدند، هنوز به دست تولیدکنندگان نرسیده‌اند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/akhbarefori/689347" target="_blank">📅 22:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689346">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d5e7b1618.mp4?token=JswAyzIDENqQah3eWtVAA9sZv82Ll2k8t3aVBv4hTz8OFUQwJAiMyjjvxmfswEyfaMW4lI8oqeIw-gByD3DoOVGGlOpJn60y6lOaayFDOK3zrgnOILDJO7KzyIkD1kXknP_dt0FhL-_YbbrS2Z_aKEDTbwXC9XcZwrjt9WPqLqep-XIQFKK2Y8PfQ-9RhuaUrQLsHG5j0zyyGLe7Jdc-cIjMG5FNeX4nb_EQTsDcawIHQgbdfAs-RkOEMnIRP58reglycnml0fyDKwwHI2Zmepn6paBLExMyUazVGNVEiK33qJKqXesOk6ojQMGISIqNDjNTU1HMgnsavqQx2yYZxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d5e7b1618.mp4?token=JswAyzIDENqQah3eWtVAA9sZv82Ll2k8t3aVBv4hTz8OFUQwJAiMyjjvxmfswEyfaMW4lI8oqeIw-gByD3DoOVGGlOpJn60y6lOaayFDOK3zrgnOILDJO7KzyIkD1kXknP_dt0FhL-_YbbrS2Z_aKEDTbwXC9XcZwrjt9WPqLqep-XIQFKK2Y8PfQ-9RhuaUrQLsHG5j0zyyGLe7Jdc-cIjMG5FNeX4nb_EQTsDcawIHQgbdfAs-RkOEMnIRP58reglycnml0fyDKwwHI2Zmepn6paBLExMyUazVGNVEiK33qJKqXesOk6ojQMGISIqNDjNTU1HMgnsavqQx2yYZxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بارش تگرگ در بشاگرد/ جاری شدن روان‌آب و سیلاب در مسیرهای جاده‌‌ای
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/akhbarefori/689346" target="_blank">📅 22:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689345">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4044738bc2.mp4?token=YrTM2ENloq5TTAnHa9NmfkRJemcyWe66xbVZmL5aP37l8RRw8cagRQJ7ruEFLDHrvfqNiynGx19W_GmzLwJPnvnhgqAc1ftzvgUal8BlzbNzbMNOt8Gn9VY5MN3E69A90CB_O5GK3XRsjnhewFRywHunIQPdYee8EO_EHUA_sB8FUswNYlQJjVC6YX7JMER-TovWj82DR0vuQnM3Wz9Rm8AXQO_iuvP01gxKC8p1ANKnuN5gu6127Ronm5klr4I1Q_OY7jKtZIoya7kLLJZFU1d0eKtd0-Sx7sIgSforfyYnCpNiOt0nbqo7KQ7Y_OBNV_avte52Bw1hLtIn7u0feA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4044738bc2.mp4?token=YrTM2ENloq5TTAnHa9NmfkRJemcyWe66xbVZmL5aP37l8RRw8cagRQJ7ruEFLDHrvfqNiynGx19W_GmzLwJPnvnhgqAc1ftzvgUal8BlzbNzbMNOt8Gn9VY5MN3E69A90CB_O5GK3XRsjnhewFRywHunIQPdYee8EO_EHUA_sB8FUswNYlQJjVC6YX7JMER-TovWj82DR0vuQnM3Wz9Rm8AXQO_iuvP01gxKC8p1ANKnuN5gu6127Ronm5klr4I1Q_OY7jKtZIoya7kLLJZFU1d0eKtd0-Sx7sIgSforfyYnCpNiOt0nbqo7KQ7Y_OBNV_avte52Bw1hLtIn7u0feA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمادی جالب از ترامپ در دستان مردم در میدان انقلاب
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/akhbarefori/689345" target="_blank">📅 22:11 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689344">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/akhbarefori/689344" target="_blank">📅 22:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689343">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSedSD5Dr7f3ePqgbgIDqQ5B2GqAXj6x1w6Wdxvoqr6OpPMqSxNw9NvZtqCAkTYK09qzrXN2ZI_esiZbaBSLg3fmULRQDq-s6iqmYVbDdBmWrnlLLhdDXe0wQagrZMyTHlrphH_YE1u9DpBdvFPogUdGI1pGVnGGrv-cDD8PZcM6g-09qVRMXuG1OlKGTUJ5avLOuOqRMGb7trhf3tK3w4t1W1ArHWW9L-M9r_jsOoMJ-UKSsDzBb_nSmpyPjFVSo8MK9tEZEW1FCR5_zhG761gbsGPNRtNyUkH6L2CC7A9QntX34ForlVX4mPp_Dry9wm_AJv9ioVo6V6ZflLOC7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهکارهای فنی خودرو برای کاهش مصرف بنزین
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/akhbarefori/689343" target="_blank">📅 21:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689342">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
حملۀ موشکی یمن به عربستان
/
شنیده شدن صدای انفجارهای مهیب در خمیس مشیط در عربستان
🔹
سازمان دفاع مدنی عربستان خبر داد یک موشک یمن به منطقۀ «جازان» اصابت کرده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/akhbarefori/689342" target="_blank">📅 21:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689341">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6f506dbd1.mp4?token=HdWl7l8Uj7YXLrO0iPjfvmMfa06oS5H-ME-mHXraUZYMRQrt0LKtTp0fAzuQg47u-7Iav8P7OEt0WiBscaT9NPQrsl9todZ8E3cJwOGCcAgDbBe0Hc7hCK0BiOP5zpjho-pqT-z_hafiptx4Ix73Vr_KDm-WGokSXi5Snxr4VnR3mowrNDJDF_qV4Ywz4hWO0A4g7m_HytFyuwwI2MEcheRr3cr_HIOW63BMlyUk86w3cGXwek2jFm50YDVqyFvy6IhQ5zRgH8jSWJ_IfrgHJtUnBgokzun4xnIXjHyBJ_eYgL3QvjYEh-QLb4orT6tpfHZZhHvusG-GHTV725cQ2zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6f506dbd1.mp4?token=HdWl7l8Uj7YXLrO0iPjfvmMfa06oS5H-ME-mHXraUZYMRQrt0LKtTp0fAzuQg47u-7Iav8P7OEt0WiBscaT9NPQrsl9todZ8E3cJwOGCcAgDbBe0Hc7hCK0BiOP5zpjho-pqT-z_hafiptx4Ix73Vr_KDm-WGokSXi5Snxr4VnR3mowrNDJDF_qV4Ywz4hWO0A4g7m_HytFyuwwI2MEcheRr3cr_HIOW63BMlyUk86w3cGXwek2jFm50YDVqyFvy6IhQ5zRgH8jSWJ_IfrgHJtUnBgokzun4xnIXjHyBJ_eYgL3QvjYEh-QLb4orT6tpfHZZhHvusG-GHTV725cQ2zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ریشه فساد در سینما چیست؟
اشکان ضیایی، کارگردان و فیلم‌ساز:
🔹
هر جا که پول و قدرت باشد، فساد هم هست.
🔹
سینما نیز از این قاعده مستثنی نیست و وجود سرمایه و قدرت در آن زمینه‌ساز فساد می‌شود./ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/akhbarefori/689341" target="_blank">📅 21:39 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689330">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EZItYyedyiox7lE-g5TVjMVJSynd58TrHtGw3ZVHAVX6tU9JL3NkqjSum0xbcjX-act3CB3M7goQA_pfFGqCC5w4hKQj9OIyAkwFJHILSG-4R4xU0nzVqYU6Oto7_9RI5zXmUXgUjbiS406IqMKG1OpJI7A4zumR1sPiLO8nHNYnu99laroZ9A1NHsW72pjD8tKr3s-prvk8HcJkq6ypLQda_9kiuecxKuyxZIhSsRsyFU2QEeTCRce8l9f6p3hbSVEF2Erncby4U3jL0Dfd6au33aaOxaOO7MV23iFLz9Vm9O0c2usBtMktbbKRbLc9SwCPqcoASoIi42avgKc-zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jU3tkq3hqr-1n5MJgdBYMr98Ew0ZfTUaSY7EQYQUVgsjXTv7SP6k2GLjbD9-N_En0jD-GE3Upqcye2X-hhxjTHyQsa_OPe-DSpY_DqvGsFuEbr21y1X0Vmij0VGuaMdxgeqY1thA3nauScAbdjvkdK4P3u9soifzZoGjXIb15NN3Ug5AJ9FwB32bjXFLOMnabczIfw1Re8xrehAZ2rQa0Jwu34vgoTMs-TWZGHz-c8Plff5oM9rNFOOytOkyVUqT6PE1jRGOBVt4U3bvUmPcxUxq-IavFFKwIHeaoqF5_vhQ65G3ACmc-gueQSXWHHlqPlSRE8mYM4-yJAl5RXoNSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PHtHVMjjsDKYwHhKZi1T7eyJRedQ3N0nMsCCtpwY1684_W1ZRsM1op_cIbx2CvWOTZPuMHz_a3TR2Pbt9IElvsjLFaaE47zsXjI3g_qzJkuL_fjUQ9GIc4DZX9kQJaNHvoq81gWaV3HPhJut5WvS9LnN0z4595i4QXs_ZEhv4sjvW7FAkf0-DzybEYF6TCC8O-p_5A-FOai1wbvcdpUDXObCKt_z77ZQlng5wJXN7A4SxWH1Td_I-qLbXO1aszFKBkWmcVUz1_wAeFUXpkRSQ-qWNZsnYZcXIzcQF_xcAnJQog3oFViadXDZ7DGcaVn-hYRo630vBmNAuxj9W-Bc9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TmUgwasIs8DiRldxQpaYg1Kw0yIKU7TVkkgr-zB6FxvEEprCpS9Tuc2pSV6yucheATx7TiRog4gnkIZzQbOVRHfCi_xf9NxTwMy-8J2rh1Yk--jeA3AUyk_obQBe8FeDyw4GKfneKGPyg8qWsUJARYipqxAMl1li4IrNeJLN8luriZKlSRTyhjKSRC6ZgUHYPKOsa_Kcr-GVgGuia3Q5-FIOYDAmIjh05DPeTnyAFSmAoH0O-0m3rzXnfBRza8AXmBqQYlc431jQr3Jrflr9HIGA7wijqIlm58vYxdGnlx3OAqP7esXsB7IBvcWjDO-BnNGAGHpo5szi02dNpA3tBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hOCHONpUT42XI1CPTpE8gej4jTcZzF_ZJsnZFaXj2NlBZ2_aQNyFHnSKSnt8aZkW5e7gGARk-YD0633jwf-n_F6dyE_kFoCbTrWM2_ZEoDnJwc9eiZeX8MZATxfBOlUaWXwBzUro0eFCr21BMBkNEU9Zz1B5Lxxu9pSASXaUeBMJTNmKBOSiDCpAXd_Ci-AXDh4ILDYpKHwr_0EE5aP486ezt4ilYhtYzbD8j1974Yz60zozqHWWmj60pMkCm0YLAMXfupX4Ehdm2_Id1ljh6bpSiCw0C_cNPp9xP5XlnsNY_DkpmP1tK_yYbQmF-7VLTPBf6MUDkPtYzQBOvkJbLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N_egxxdyGMYQKlhY1OpzdY-jIUwLj4o9rM7WI1apZ1GSShlh_zpaaNtGZ9aLk6WaYmQGSsK-zm480ee7CGijDCT8uvJzoNPxYCx_AJdZPc4sn2-auK3CL1R0O58Q7ilJ19Jc1PH3_FaEco5OBaopVsOwZar2H_a27X2AUq9Ih4Elk3G30YgccskmiwiJwGdQYtFcPISJWY6ZV3Mjiy6izfQU2fpMGKSrmzjaK0L7in05Wz25LbbkcVv6OYFa_26IWxBdnfWDXFtG_C5gTBPleSnA531iO1IMNCcub9vpLH3KhXcwjyXt4hpI46potDxNa_IjDIQwkqrQF-bAkJFJag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P97ckVvsNjOCjMlvOeWEs3fgTCHipKdk9cVdqD6z7GUN-rrd9pqTke8T2ft5qLX3c254xCVTfMIoDERjJsDK54ssvX_FxaTfYzP4bJbL3ErqeRCDzdjcUPgaqrfaEBD40BjR5gRoi--5N5AgPPCyWKEzWyX_sDBq0uPSoy5pfmx2rxMCV5vlaxEmV6HnPlWUBEjYE5CWxrtg2-M_DXv3TOm1IOFuxqG3jKgf0vB0AqOhuGpEu8LRvqFNyfn8_ShmfWGFvl3FALzwA9g-DlEQMK5O3T97cMkXzQA-keD2SYlnVLBj27oWEHMDfiEksAW9iJGLziaZY-qlr8wP4uYuRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C-XimoWrOT3AlmbsTVsgUowVnHwZpDQrzKF6dI9732fqokSiroLPwdlZP7liyN8pa3_57_Xz6HOiggW1IOhxjNpf_gd15hI0Phz1EIncKYY7MBwOI1tv8h1SXp86LiD_HnnWOoHGrXmpR-cgKShKbs842mps5GyZY58UhIT_aH9aFQblMpTiqEoU9i5gHxQtWVq490mIMGNKSSr7ZgQz5p2B6doHNJlbGZ3luPMFtG4hMcH_ajR27OHC63IhFa4BJzCANLNYlZJr4BR6fhhy-0mrAY3dZcDJyCzQnw_ufaOKCBs95TUJdEm3p0KPz9reJ5LyBw5jZdI_aDmdw-M7XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nfq612vjkXXPvbuxd_gsqKQCTgqIz1pWc9Y9QOgmp5P_KKlPsP5haN2amBvZXDiOeDIduebmRynezeX5HbpK25mse3uAse0B8cj8YKcnS297JeWCWuCkBorjIG4uPW5L8NFBGH_unpnLFeB5ZndcJkGjsNzsZ7OuxRATbX-6N4oCJ0P2GlSxXyPPCJj7lrp_uAfDYkWwP060ygHsWS3lkgwA5lcZez0d0yzPT60L5ek_sCJyOsL2IYWnjblZUbxatElvoBDFQKLiVWJzkx4dDqFaknfARfY4Y_s8GM7WKfJ2pQvWwehAiED_TfblBhkPgpM8tEZlj_0T5ySwiPCq2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LJr2ipIASPSgcXiIozn_mLx04_Ife6borCaD0SUvt_hMnlzZQEnK3qXVUt8MWIlIISPFS7MJnZEvGtnWaLEl1cAblrXgFYbz4iZjGhxss0unkUy1E03BJU4H0bNViyduScbMXf7wDqYrt_kavH2zx9cz4yb8hj_gysZfLDx61GOLQGjhgR24HvNhhsHpkua9MGWm5wcYBgdwUk6K1fzovGL2p_EkIzAakX0Ga-FPMgtBq7xr4Cw6FNn_rX7j_tgx1aaT7_w8Abdw6YXWhqH6x-KSEZTxXbcJAoxtBeoGOXhPH5lKk6I-C7kMa48BLH4yiuYupdnd67RTho7N9LaRtQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
درد دارو
🔹
روایت مخاطبین الوفوری  از موانع پیش‌رو برای دسترسی آسان به اقلام دارویی ضروری.
🔸
در چند خط  روایت خود را همراه با نام، شهر و نام دارو برای ما ارسال کنید
👇
#درد_دارو
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/akhbarefori/689330" target="_blank">📅 21:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689328">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daW9uq8cjS03jh7bSpUuRYyH0hUyTWKlJjVAl0yobY3sOyNbGouA7xBzZXZ-ZgDiQ5PlUlk-OmDinRL0oYnWiBl6t5B2sqjgOCNdcuumYcoQsI6EwH9qOWHezf7JUv-O161Jifl0uPslGYt1RK6NYtLY0RUsb8_brr9IXPnJIhXDqmt39Ix7WpBdMpGFy2jY0tjpnda56q-e3ruiSoYdZ2Tx6aqdlM1Qyg5PK84ihXANTT5fCzPFtZlpkWi1fJI8r_wCSsIoDdt-CNc5maTOzXxWfZH58l2WHqI7QU-8mZSuOciPWk8BIJI0YVMBrJ7p5mspTXm0lQ8yhXK1tBt8Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از جیب فقرا تا باک ثروتمندان؛ بنزین به کدام خانه‌ها می‌رسد؟ | ۷۳.۸ درصد فقرا اصلا به پمپ بنزین نمی‌روند
🔹
بنزین در ایران سال‌هاست بیش از آنکه یک حامل انرژی باشد، یک موضوع اجتماعی و اقتصادی است؛ از سهمیه‌بندی و کارت سوخت تا بحث آزادسازی قیمت. اما پرسش کمترپرداخت‌شده این است که این سوخت واقعا در کدام خانه‌ها مصرف می‌شود؟ داده‌های تازه مرکز آمار ایران از هزینه و مصرف بنزین در دهک‌های درآمدی، تصویری روشن و در عین حال نگران‌کننده از نابرابری در الگوی مصرف بنزین ترسیم می‌کند.
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3244689</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/689328" target="_blank">📅 21:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689327">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
دقایقی پیش صدای دو انفجار در قشم از سمت دریا شنیده شد
🔹
منابع محلی تاکنون در این باره اظهار نظری نکرده‌اند./ ایرنا
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/akhbarefori/689327" target="_blank">📅 21:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689326">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/946a6ff60e.mp4?token=toNIqFLgz5Q6aGFB-NpZjcCYlOGQ4RJPrdksXmqdAFLSe9LrDwkvn4hAZfRI2XGX40JVJ-rtGtNaN_QYJa_y7Z3o0t6w8JvUI8HGCmfTISZ6lJb4VhdmiEdGcOIuOZp13uQ5AVtsDWPde1iAe3ksSTzK19hSdtx53VvFlBNyT89bSZ1kgaZT96hlZakVPWxaVzQjOD6Jjnzl4oMAwp0UDRemCsX2YUHDLiCt4BvcQslTbQ1vTP7gVPuDbKnyby8DaFtmmuNuQC_HqLSO8gW6g7-24Vr-GmihZ6lHqaWHf-rcbjxm02AOMev7f4Z3lht8E-3IhtvBzsDdgDBc_N7IZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/946a6ff60e.mp4?token=toNIqFLgz5Q6aGFB-NpZjcCYlOGQ4RJPrdksXmqdAFLSe9LrDwkvn4hAZfRI2XGX40JVJ-rtGtNaN_QYJa_y7Z3o0t6w8JvUI8HGCmfTISZ6lJb4VhdmiEdGcOIuOZp13uQ5AVtsDWPde1iAe3ksSTzK19hSdtx53VvFlBNyT89bSZ1kgaZT96hlZakVPWxaVzQjOD6Jjnzl4oMAwp0UDRemCsX2YUHDLiCt4BvcQslTbQ1vTP7gVPuDbKnyby8DaFtmmuNuQC_HqLSO8gW6g7-24Vr-GmihZ6lHqaWHf-rcbjxm02AOMev7f4Z3lht8E-3IhtvBzsDdgDBc_N7IZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شادمهر در راه بازگشت به ایران؟
🔹
محسن نامجو با هماهنگی به ایران برگشت؛احتمالا شادمهر عقیلی هم به کشور بازخواهدگشت. فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/akhbarefori/689326" target="_blank">📅 21:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689325">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
افزایش قیمت ۱۰۰ درصدی نهاده‌های دامی/ انجمن صنفی گاوداران: افزایش قیمت گوشت ناشی از افزایش هزینه نهاده‌ها است
احمد مقدسی، رئیس انجمن صنفی گاوداران در
#گفتگو
با خبرفوری:
🔹
حدود ۶۰ درصد نهاده‌های مورد استفاده دامداران شامل علوفه، یونجه، کلش گندم و ذرت علوفه‌ای تولید داخل است که قیمت آنها نسبت به سال گذشته ۱۰۰ درصد افزایش یافته است.
🔹
فعلاً دامداران این افزایش هزینه را از جیب خود پرداخت می‌کنند و این افزایش قیمت هنوز به‌طور کامل در قیمت شیر خام منعکس نشده است.
🔹
در دام‌های پرواری، بالغ بر ۷۵ درصد قیمت تمام‌شده دام زنده مربوط به خوراک است و بنابراین افزایش قیمت گوشت که شاهد هستیم تا حد زیادی ناشی از افزایش هزینه نهاده‌ها می‌باشد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/akhbarefori/689325" target="_blank">📅 21:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689324">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
جزئیات جدید درباره تفاهم نهایی ایران و عمان/ تنگه هرمز با این تفاهم باز نمی‌شود   منبع آگاه:
🔹
تفاهم ایران و عمان اوایل شهریور نهایی شد و به زودی با حضور وزرای خارجه کشورهای حاشیه خلیج فارس اعلام می‌شود.
🔹
مسیر ورود به خلیج فارس کاملاً در آب‌های ایران و بخشی…</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/akhbarefori/689324" target="_blank">📅 21:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689323">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b13bb4a0b5.mp4?token=QvKa27H6jFEGdAthtP7v2AQpkKnGA5osAD27OW2j9fw80E9hUhWiBUCZBHAyX1_0P3_lPnQi5fMo76sQtY7sPAFJely0AGqo2MKybc06KgIMhZJ8jHEtMTHvCZTFj0Di6AF0i6lknk0hrA9aL-_eMNWJlxu-fhheiVid1513c1WcRKXVBc0zka_F3TtRwCZVqcF-JRqmS1qDNSBlZ8lvqxj7BvizkeOUF8WveLqNslxU13Sf0v8o728CM6DAv8RCItHaGNJixS_8i0nr2GcS-2ntt62l6zf3v-AaVd3J7SsRIoVVH0UtP9dxTz3VFOZxj6VrS3UOAdKSDY6Ew0iUlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b13bb4a0b5.mp4?token=QvKa27H6jFEGdAthtP7v2AQpkKnGA5osAD27OW2j9fw80E9hUhWiBUCZBHAyX1_0P3_lPnQi5fMo76sQtY7sPAFJely0AGqo2MKybc06KgIMhZJ8jHEtMTHvCZTFj0Di6AF0i6lknk0hrA9aL-_eMNWJlxu-fhheiVid1513c1WcRKXVBc0zka_F3TtRwCZVqcF-JRqmS1qDNSBlZ8lvqxj7BvizkeOUF8WveLqNslxU13Sf0v8o728CM6DAv8RCItHaGNJixS_8i0nr2GcS-2ntt62l6zf3v-AaVd3J7SsRIoVVH0UtP9dxTz3VFOZxj6VrS3UOAdKSDY6Ew0iUlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بارش تابستانی در ماهنشان استان زنجان سیلاب به‌راه انداخت
#اخبار_زنجان
در فضای مجازی
👇
@akhbarzanjan</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/akhbarefori/689323" target="_blank">📅 21:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689322">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
عدم نظارت بانک مرکزی بر سامانه‌های طلای آنلاین، مثل این است که بگوییم کلانتری گشت ندارد
آلبرت بغزیان، کارشناس مسائل اقتصادی:
🔹
در بحث فروش آنلاین طلا، ممکن است اقدام به فروش بیش از موجودی طلای فیزیکی صورت بگیرد و زمینه سوءاستفاده فراهم شود.
🔹
اگر بانک مرکزی مسئولیت نظارت را نپذیرد، این سؤال مطرح است که چه نهادی ناظر بوده، موجودی این سایت‌ها را تأیید کرده و مردم را به خرید از آن‌ها دعوت کرده است.
🔹
متولی مجوز دادن به چنین معاملاتی بانک مرکزی است، چنین سامانه‌هایی باید دست بانک مرکزی باشد، چک بکند که آیا سایت‌هایی که اعلام کردند این موجودی طلا را دارند یا زیادی فروختند و خالی‌فروشی کردند.
🔹
تصور می‌شد که این نظارت وجود دارد، نه اینکه بعداً متوجه شویم نظارت بانک‌ مرکزی وجود نداشته است انگار که بفهمیم کلانتری محل شب‌ها گشت ندارد؛
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/akhbarefori/689322" target="_blank">📅 21:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689320">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jWbq6JhFbJrcq0vdkYu2bC0RndAzjU4G2ASJwa8SCd9AMjJWjaY6TjO5ktY0nMG38opwd84jMqkUVvQ07ITKbvT11g1FBUNv-7lWZJfp2XKFD6NKk9PtJIpJMYF-e9XFG8odL1oQO453hxiBH0B7KF4QqAlykJwMiHAxQiMjZ7DlblSGHMVxMOsOdtbZ_BFEf3Yv9gJLrHYQOxM68bawN2VGdId-ssE4Y1J-srSXAMUichj-PKgRjpErTFjlarKbOFapqqixlSDSiobJvc5XgCTF4j6qcq0vHlCstz3uAVb5GdiQIXBAtGbfA33IjJf7RPUq95ApxnODo1XsYeG2jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RPGn9CSvqw-dZ38mzPJ8bPiwj1alIJnojHiMNZ5hhnVYhOiA6FkIabjnL-nLcVfTUChVbrbSxEkKY443K5T5DX8YE5K2UY-sxldG15hl8AhxZGrgXbpgWnx8CClbL5JHbl63KJQojIxHpi4KzW9-3USpk1ptDKh1bQn1-57SjWI9fCKtDHerc-dY8_XsEwwdM_R8P3tTgoeQgx0Ac3s_nO4fwpLAOi9y1JKkKNmP4UTkdQCnvuJ77qOXgY66kj0CoxjC27NGmovDloiGsbtct2FjQymcqExPgS4e_vLasyjVVrtggpoy4D5GG-RV6FN81Edt-RB39mZ41oNH8wfNrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
منچ اوسینت: امروز تنها یک نفتکش چینی با سامانه ردیابی روشن از تنگه هرمز عبور کرده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/689320" target="_blank">📅 20:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689318">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fcb869d7a.mp4?token=HzrQ_IO7u5iqDdNlD-uoc_uQKnpggvDNAgIZ-spOg9Cjt2Mwozn4w4tkHCZBrq3GrBulm_alJHjOmrdW-iLmFtggTxI7qAn3WrYCfSoo2zTLZn9vYv__FM-luV_1wJi6kGX_1-1NdyAshBvvoMiJgo3Tgy-MFgLIZ6q8W_LyczW0Sx1oDFqNsnrS8CwpNEO63LYUOqHoRdnJ0wNz9kjd6mtRBWo7a-_hD94WmWVV2vbTVdBSAh4YLJsxStfVyeDJHW2Z6fyhfEKnKsL6VYJCYUqMTyoiCKPnH9CByQfZz8NjDCu6e9YPlpADmJV1TMUA9f9j617wWxhiUoTVDun_QjUVJziLk4nbKMzGqYhaDv5D_r-lsKbh-X8zgDE218DF0im6rGV7C47s5IjoX4KiCGYqZZZixiaqscmRBPScV0O6Qp7EFSZIRJpF6u2QNGa8NuslxcQ2WYFJVS-AFgI0kobMvFbJ0u6Vwkj0tZZDRuGd2rdohULwV4PR05Hek_BeaaasZaDo_phq2Q72Bm4PATaPVeM4ErdLHm5743btAZu-4NwcYjb0BKgkhrL5GISVpizheWD_88MR2gp23ASgkWMNtjdMi2OhEjD3vqKcfyLvaNPV11P8JLQjbTBFpLsAMi9a4_hq-QnjTJIan5VN3ykYkPZ2YMS54AAuVcggnkI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fcb869d7a.mp4?token=HzrQ_IO7u5iqDdNlD-uoc_uQKnpggvDNAgIZ-spOg9Cjt2Mwozn4w4tkHCZBrq3GrBulm_alJHjOmrdW-iLmFtggTxI7qAn3WrYCfSoo2zTLZn9vYv__FM-luV_1wJi6kGX_1-1NdyAshBvvoMiJgo3Tgy-MFgLIZ6q8W_LyczW0Sx1oDFqNsnrS8CwpNEO63LYUOqHoRdnJ0wNz9kjd6mtRBWo7a-_hD94WmWVV2vbTVdBSAh4YLJsxStfVyeDJHW2Z6fyhfEKnKsL6VYJCYUqMTyoiCKPnH9CByQfZz8NjDCu6e9YPlpADmJV1TMUA9f9j617wWxhiUoTVDun_QjUVJziLk4nbKMzGqYhaDv5D_r-lsKbh-X8zgDE218DF0im6rGV7C47s5IjoX4KiCGYqZZZixiaqscmRBPScV0O6Qp7EFSZIRJpF6u2QNGa8NuslxcQ2WYFJVS-AFgI0kobMvFbJ0u6Vwkj0tZZDRuGd2rdohULwV4PR05Hek_BeaaasZaDo_phq2Q72Bm4PATaPVeM4ErdLHm5743btAZu-4NwcYjb0BKgkhrL5GISVpizheWD_88MR2gp23ASgkWMNtjdMi2OhEjD3vqKcfyLvaNPV11P8JLQjbTBFpLsAMi9a4_hq-QnjTJIan5VN3ykYkPZ2YMS54AAuVcggnkI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین وضعیت تعیین‌تکلیف نیروهای شرکتی/ جزئیات تصمیم دولت و مجلس اعلام شد
/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/akhbarefori/689318" target="_blank">📅 20:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689317">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8qz4mR4SBvuYgw-4nYtj5l8z1Bm41dWDZR6HpIUxv5tknT1356r_vvm7yagAsW6o-uDPNO3fv2uizJyfLKTXpCCw_iqh-RpxsPtNiCzmsoTkKO8iXk0wexz7ww9d7eUD4XvS_ZC6-WfsS-aZ8W6MYxJ36u0xAqeKh-XRBlxuf37Kpy_qH2fv0hg4ewjHks6JM_4XXR4XpKQY-r2yvmsFwldFWiJerwomGhvW_0ZtlXeXgHvcmSnBCaR-ovcVq5lr3ieVIer7SO4t-E7cikmT4dmlTIcLPMDMnsTVKxq1hN2urHRZ9pE-kIu0iCiM9SezOGtRGFfv_ICyuO5fBO9iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسامی شهدای عملیات ضدتروریستی سحرگاه امروز سراوان  روابط‌عمومی قرارگاه قدس نیروی زمینی سپاه:
🔹
در عملیات سحرگاه امروز حافظان امنیت که بر علیه تیم‌های تروریستی، در شهرستان سراوان انجام گردید، تعداد ۳ نفر از رزمندگان اسلام، به‌نام‌های «مسلم فاضلی»، «میثاق ثانی»…</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/akhbarefori/689317" target="_blank">📅 20:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689316">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc3852da87.mp4?token=Xos6TAZZ2Ty476ZuSJ3lYjujSlK3eiIa8qxfdYjpM8B9OjsBCFqz2XTCgq3YfuoXwGZDfgBiSfT1f4MUfGV7D5KQxljeIh_eOILWeGg1vjQr_HTkDXq9Q_ahuKYVYJk3KBphQZSDZelshycOurFNsP3iEw0FEswG4XiGF7HT4O5P036sFQY82VEfQpHZHo6Xdooo9NOBjFWzSXEJ2WQELWDs8oq122jPFUc7oISHA8Jj6FSogsMdqBo76x9TCwuuFD149czm_5OwY2EnRT4q1ff4ZlIJcyekWJIIAi1Cwpxq7bXEMSgqIvkljyR6VtDD221dYnPCSym5WP5v6dwsVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc3852da87.mp4?token=Xos6TAZZ2Ty476ZuSJ3lYjujSlK3eiIa8qxfdYjpM8B9OjsBCFqz2XTCgq3YfuoXwGZDfgBiSfT1f4MUfGV7D5KQxljeIh_eOILWeGg1vjQr_HTkDXq9Q_ahuKYVYJk3KBphQZSDZelshycOurFNsP3iEw0FEswG4XiGF7HT4O5P036sFQY82VEfQpHZHo6Xdooo9NOBjFWzSXEJ2WQELWDs8oq122jPFUc7oISHA8Jj6FSogsMdqBo76x9TCwuuFD149czm_5OwY2EnRT4q1ff4ZlIJcyekWJIIAi1Cwpxq7bXEMSgqIvkljyR6VtDD221dYnPCSym5WP5v6dwsVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اتفاقی باور نکردنی! جیرجیرکی که میلیون‌ها سال در دل کهربا زنده نگه داشته شده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/akhbarefori/689316" target="_blank">📅 20:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689315">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپلتفرم شیدا | SHEYDA VOD</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odA7QlXf0OtqPuD90OFBKFL_4aADGPAkHK88tJN4e_yjZVJetRCs0uHDTQZKbSeIrWdF__d2RKx_ZvwSypCJQgvhPWVgLmvv0dUQ0ggVeJ9cJkpj9Cw9cu861kDq9_KUjbkT_Vt_MrgY-Ns4CZXEQ_VU2h1dxmq4opSbHWQ7rbTfr-GNKuGA0-Oy-9PHyHuGoDtvaMjBw9wpHwfS1q2TGdxVmYdvZL0-VVro7ieSLnKEaXWFdpQI6DcZQK-IrGdXur_6AJFhpBduhZBAg0S89aGNaDevLCRcOHVotL4N6H-lgzP-Bp-1BKI9lB_nPCxnLqDWYoXNanAfGEr2er-3Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با روز ملی سینما؛
تصویربرداری «ده پهلوان»، قصه تازه حسن فتحی در عصر صفویه آغاز شد
تصویربرداری سریال «ده پهلوان» به کارگردانی حسن فتحی و تهیه‌کنندگی زینب تقوایی از بیست و یکم شهریور همزمان با روز ملی سینما شروع شد.
به گزارش روابط عمومی شیدا، این عاشقانه تاریخی به نویسندگی نغمه ثمینی و حسن فتحی، داستان خود را در بستر دوران صفویه روایت می‌کند و نخستین سکانس‌های آن در منطقه پارچین مقابل دوربین رفته است.
در نخستین روز فیلمبرداری، محمدعلی مشکیان، مدیر پلتفرم شیدا، و مصطفی شریفی، مدیر محتوا و استراتژی، با حضور در پشت صحنه این پروژه، از روند تولید بازدید کردند.
«ده پهلوان» روایتی عاشقانه و دراماتیک است که در فضای تاریخی عصر صفوی شکل می‌گیرد و یکی از پروژه‌های مهم شیدا در حوزه تولید آثار نمایشی به شمار می‌رود.
جزئیات بیشتر درباره داستان، بازیگران و سایر عوامل این سریال به‌زودی منتشر خواهد شد.
@sheyda_vod
www.sheyda.com</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/akhbarefori/689315" target="_blank">📅 20:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689314">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
معاون برق وزارت نیرو: احتمال قطعی برق در زمستان
معاون برق وزارت نیرو:
🔹
ذخیره گاز تا زمستان به ۳.۵ میلیارد لیتر می‌رسد، اما به دلیل محدودیت‌های گازی ناشی از جنگ و آسیب‌های جنگی، احتمال قطعی برق در زمستان زیاد است./ جریان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/689314" target="_blank">📅 20:39 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689313">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a04a3913a.mp4?token=qNpIN77pORhNbwSIHRGzBq5TjO25ixRTD7IIi3wlLk4j3WnxLvCAyMee3rAI2dWSGk-Y56WHvvQFx7_reb-W45Eqr0v-0Au4S8uQIdXDHH59wSMr_rPIhQInd5KAaPsvn8UfQQGFwsdiLh3-Cip3_BGjn8fjBfh-hMTiH6TUx1Boe2wYeGCHG8BdhHb63gGav9aBO5npdDcuweLf1KLbCO78qkMo9jOiPLn4v1XHuY83pw2QEt0UQqkBbuKe39e_WoabkRBn44mT4Ud1k8TispKyAej81h33V0S5OerI3_QCDh9CgdNg98_qn8MQLKFK_wttJi9l6OLjyZtZoF61jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a04a3913a.mp4?token=qNpIN77pORhNbwSIHRGzBq5TjO25ixRTD7IIi3wlLk4j3WnxLvCAyMee3rAI2dWSGk-Y56WHvvQFx7_reb-W45Eqr0v-0Au4S8uQIdXDHH59wSMr_rPIhQInd5KAaPsvn8UfQQGFwsdiLh3-Cip3_BGjn8fjBfh-hMTiH6TUx1Boe2wYeGCHG8BdhHb63gGav9aBO5npdDcuweLf1KLbCO78qkMo9jOiPLn4v1XHuY83pw2QEt0UQqkBbuKe39e_WoabkRBn44mT4Ud1k8TispKyAej81h33V0S5OerI3_QCDh9CgdNg98_qn8MQLKFK_wttJi9l6OLjyZtZoF61jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۷۰ سال تکامل کامپیوتر، از کامپیوترهای قدیمی تا ماشین‌های آینده
🖥
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/689313" target="_blank">📅 20:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689312">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
تصویری از خسارات وارده به پالایشگاه جیزان متعلق به شرکت آرامکو عربستان در نتیجه حملات یمن
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/akhbarefori/689312" target="_blank">📅 20:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689311">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ff5e01ea0.mp4?token=KXxdfMab94qNoZ5AeC45an4I4iAb62LGGnxVBxcYtvGk_bOnhSNmHh27Kn0J8Ia8SNnipuAM5HQOPoxBZKamir0JwwXeQ3TiKUZGpHIxfs-qA4RzNKu-J2FPC1cCoGwFm-ckmRhC6sb_yYZfXcSKdlWT87_S7HBXlW1pqapBDroN5r4GvlbLdaRNWYpm2Twg_ubkXsw7lTkSnmmq_M4XFMX5vrE1kClKGAaeFXsSFZqW1ne0clzUYaUlYlzJBNxSrRiSMZ8bHkYrmYn0nREWPRJLuRopfPfQRKbYMP8TYTX2GRBZ6lQC9cftFhToSLI4mmPVRqkVVkpiKWSzHUWIcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ff5e01ea0.mp4?token=KXxdfMab94qNoZ5AeC45an4I4iAb62LGGnxVBxcYtvGk_bOnhSNmHh27Kn0J8Ia8SNnipuAM5HQOPoxBZKamir0JwwXeQ3TiKUZGpHIxfs-qA4RzNKu-J2FPC1cCoGwFm-ckmRhC6sb_yYZfXcSKdlWT87_S7HBXlW1pqapBDroN5r4GvlbLdaRNWYpm2Twg_ubkXsw7lTkSnmmq_M4XFMX5vrE1kClKGAaeFXsSFZqW1ne0clzUYaUlYlzJBNxSrRiSMZ8bHkYrmYn0nREWPRJLuRopfPfQRKbYMP8TYTX2GRBZ6lQC9cftFhToSLI4mmPVRqkVVkpiKWSzHUWIcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ در مورد حمله به خط لوله نفت عربستان: به احتمال زیاد ایران مسئول این حمله است    ترامپ:
🔹
جنگ ایران خیلی زود پایان خواهد یافت. جنگ ایران احتمالا پس از انتخابات میان‌دوره‌ای پایان خواهد یافت./ حوثی‌ها نمی‌خواهند با ما بجنگند‌‌. #Devil
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/akhbarefori/689311" target="_blank">📅 20:11 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689310">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1df0873e00.mp4?token=tby1pHCv-LC7lVBKVxizKizBYur-3tB1rKlFaVlEDCaGPgIzrSebiz6k12fVCIDlZI30g_jgnBd7yZ7ZZlijbV2tvloRsUGkjl8FIMtCuoo0-AQXz002Xy8EhB78bgQHjddy3mV0MtINdNGM2PCkSB8DQd18fXreescWNIfQUyHgFzM_40FGai6Oo3p5JL5kJLhgm-Ou_8oQpnUtOonp7HqhLs_Q9M7tM91csEsxQpwha_thyZnX2BY58TdeDZkxQWfIkefmc18PesOm8uIp1XpMqRKBttD2X4lulohIT3VjVjojO_FhIBqU1bYWW_vc-xqzEO7Sddvamvurh6eJ7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1df0873e00.mp4?token=tby1pHCv-LC7lVBKVxizKizBYur-3tB1rKlFaVlEDCaGPgIzrSebiz6k12fVCIDlZI30g_jgnBd7yZ7ZZlijbV2tvloRsUGkjl8FIMtCuoo0-AQXz002Xy8EhB78bgQHjddy3mV0MtINdNGM2PCkSB8DQd18fXreescWNIfQUyHgFzM_40FGai6Oo3p5JL5kJLhgm-Ou_8oQpnUtOonp7HqhLs_Q9M7tM91csEsxQpwha_thyZnX2BY58TdeDZkxQWfIkefmc18PesOm8uIp1XpMqRKBttD2X4lulohIT3VjVjojO_FhIBqU1bYWW_vc-xqzEO7Sddvamvurh6eJ7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بوی سیر روی دستات مونده؟
🧄
😵‍💫
🔹
با این ترفند ساده چند دقیقه‌ای از شرش خلاص شو!
✨
ذخیره‌ش کن که یادت نره
😉
#ترفند_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/akhbarefori/689310" target="_blank">📅 20:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689309">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال رسمی فیلیمو</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6244a14dc9.mp4?token=UnZVn2W421nURZGQy6sFRnPT_4imYgA880G8u4gIKh2df2S-BaVwkiuDA-3Pz4I3x-pGlo7DMTRytcN_wJ8h7FWi-TQstHN0lt6S29sdg_yq_fInwKIKg6lWtMuiNNKd7sOxqlAdvuwLYQojO4QDrY7-qdoFR6wwyC3AFYxCJfHTFi_Ud7NamfzVeykfBc7O4175k-VcsfUdSu2MjoHcVUvHIXd4tzF0IaYMAyoVhas-afpN0EpscSjRjHoWkBjchFqzi-SsXePwR4fUg0llgfHoekrXnxB1e5u95kpV2l1vGA10EHO_mQezGGc_NnRLZxw-Z6jdxnj-v3wQwI0ifKTsEtiWK0nh__3XWnR-CUgn9kCPrGml-rcqBPUpYLqzlaaSOsXih6WVmIJER3p8-d5YbToYaP9gvOt0EYh6TWEIiIykbElPyMTUg4N4w2nCcCu2y-0DDbWtYonUxaXHuQcDaClDwnon8WgfH5Z_j-8-F3pQVqlXt-a9J4UVDBeMTvm-CtwOZcw95PdQjBOAJ7rUe8a6NfNVpKjWPeheXe9WvVOoffKM_X_W1tidcmAKfvHcGGIZGIKSUngaaNvQIHSU8VaMxW_Di3RIC09gX64OLdDLYGlxxrELDqsNnL1PZy6SJOHDQ68CAxlG4Df_asqFUyrP4N3GbhMArYXm0So" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6244a14dc9.mp4?token=UnZVn2W421nURZGQy6sFRnPT_4imYgA880G8u4gIKh2df2S-BaVwkiuDA-3Pz4I3x-pGlo7DMTRytcN_wJ8h7FWi-TQstHN0lt6S29sdg_yq_fInwKIKg6lWtMuiNNKd7sOxqlAdvuwLYQojO4QDrY7-qdoFR6wwyC3AFYxCJfHTFi_Ud7NamfzVeykfBc7O4175k-VcsfUdSu2MjoHcVUvHIXd4tzF0IaYMAyoVhas-afpN0EpscSjRjHoWkBjchFqzi-SsXePwR4fUg0llgfHoekrXnxB1e5u95kpV2l1vGA10EHO_mQezGGc_NnRLZxw-Z6jdxnj-v3wQwI0ifKTsEtiWK0nh__3XWnR-CUgn9kCPrGml-rcqBPUpYLqzlaaSOsXih6WVmIJER3p8-d5YbToYaP9gvOt0EYh6TWEIiIykbElPyMTUg4N4w2nCcCu2y-0DDbWtYonUxaXHuQcDaClDwnon8WgfH5Z_j-8-F3pQVqlXt-a9J4UVDBeMTvm-CtwOZcw95PdQjBOAJ7rUe8a6NfNVpKjWPeheXe9WvVOoffKM_X_W1tidcmAKfvHcGGIZGIKSUngaaNvQIHSU8VaMxW_Di3RIC09gX64OLdDLYGlxxrELDqsNnL1PZy6SJOHDQ68CAxlG4Df_asqFUyrP4N3GbhMArYXm0So" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پارسا پیروزفر و علی شادمان در
#سرخ_و_سیاه
سریال «سرخ و سیاه» به کارگردانی آیدا پناهنده و با نویسندگی ارسلان امیری و آیدا پناهنده، به‌زودی به‌صورت اختصاصی در
#فیلیمو
منتشر خواهد شد.
تهیه‌کنندگان: محمد یمینی و محسن خباز
@filimo</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/akhbarefori/689309" target="_blank">📅 20:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689308">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
موشک‌های رهگیر آمریکایی به‌شدت ناکارآمد از آب درآمده‌اند   ویل شرایور، تحلیلگرآمریکایی:
🔹
مسئله فقط کمبود ذخایر نیست؛ واقعیت این است که موشک‌های رهگیر آمریکایی PAC-3، تاد (THAAD) و SM-3 همگی در عمل به ‌شدت ناکارآمد از آب درآمده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/akhbarefori/689308" target="_blank">📅 20:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689307">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdZc-h80NJtXOUCGNPIvTJByxAkUd8wZZgXxUfLQovR0fp-O1zTD-_kwMD7QH1gHd5o-RWCdG4I0s3wYY0uKHKzYj4td0BtKfR6uyZQY1mSQSlo8ixAUOmjj4pJUfU4Pp3H1r4axIuQIofVVJF1V0-cvapt7OcRTvaWEZ4QB2GnzhiFkY24vap_P0j3nl3Br7FEGQ0PFE-59PpBel3x_Y23bqrvow5WYdY1bCRov89fdGyp4JXQ-3eTH06n3OMX6GO9nyycJUulZ3rpqaZm3fY-ElHFTwG4mFo_acFG3NAvUgbHJ0-9LbAD8WQphSF1JHSAZorbRepAHw9FMePc-rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ابر میانجی
🔹
در حاشیه نشست سران بریکس، شی جین‌پینگ با اعلام آمادگی چین برای میانجیگری میان ایران و آمریکا، پکن را در قامت بازیگری تازه برای گشودن گره جنگ تهران و واشنگتن قرار داد؛ پیشنهادی که می‌تواند معادلات دیپلماتیک منطقه را وارد مرحله‌ای جدید کند.
🔹
هشتصدوپنجاه‌وهشتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/689307" target="_blank">📅 19:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689306">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e69b20bb2b.mp4?token=PTyTqF0hbAXQ3RdJsMuIe7INvKy6UKJPY4JT_gIgM9jgd1EOvtOO0StcS6MF_qtIZYhV9clV23d-fptgRMZ0YLzLlKHRao9GIv2u87b3UqfU6lH-iLnSm09TtpLXnxXYP74TSVCA5PMipxvfYQ6RiCF8tZWgkigWB7t4kt96tnp2VeXcD_biwYt2cjxMFHNWyRuTrJk50TP_i4_GRuELlRDbNhJ0rs9hdxHxfF1EUGigq5zLSALHPiqjmyamSQ5xtHFiU9FxYd0XeYJjpN7rANH_ieuQngv6vpKmx42aMh7okRrzJtjbwBVCXczUqxuVF-4bclE0Lc4FuAXmqJHTnzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e69b20bb2b.mp4?token=PTyTqF0hbAXQ3RdJsMuIe7INvKy6UKJPY4JT_gIgM9jgd1EOvtOO0StcS6MF_qtIZYhV9clV23d-fptgRMZ0YLzLlKHRao9GIv2u87b3UqfU6lH-iLnSm09TtpLXnxXYP74TSVCA5PMipxvfYQ6RiCF8tZWgkigWB7t4kt96tnp2VeXcD_biwYt2cjxMFHNWyRuTrJk50TP_i4_GRuELlRDbNhJ0rs9hdxHxfF1EUGigq5zLSALHPiqjmyamSQ5xtHFiU9FxYd0XeYJjpN7rANH_ieuQngv6vpKmx42aMh7okRrzJtjbwBVCXczUqxuVF-4bclE0Lc4FuAXmqJHTnzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سازهایی که هر روز صداشونو میشنویم، از کجا اومدن؟
🎶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/akhbarefori/689306" target="_blank">📅 19:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689305">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNZXUm_MF2oXc7IR6R3mN8P9htbgQ-bNfZTKxlpnid3xd-u6sgzBbhdwsWMvk3liONmcO0FGnhp6Ve6BfbrV10zWaiK9CUjCyRnWQlooECmdHtjDc_7O8WwwVvPo94u3vgfpinlniHEufjpTSli1FbdazHJX3ploOXuGeYi6j9HVJEgOzv5ak5duupvd4EFoPQ1kx7NAz3UuEV83yGdnD2sOK85_YorPfEhGeeET2oqTJ5yIwMUGgXvZeAfMw7kzt5HvrXczRUMz8wST0JzaVX3joX1jUlkAD93KuH22QVDo07wAPEOB4hWapgjop1LScGoQ2QDsO_BefZoLnG3tpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر فرد در ماه چقدر غذا خورده است؟ | ایرانی‌ها غذا را از سفره حذف کردند؟ | سفره ایرانی زیر فشار یک دهه شوک اقتصادی
🔹
سفره خانوار ایرانی طی بیش از یک دهه گذشته نه فقط کوچک‌تر، بلکه به‌تدریج فقیرتر نیز شده است. بررسی آمار هزینه و درآمد خانوار نشان می‌دهد میزان هزینه واقعی سرانه برای خوراک در سال ۱۴۰۳ نسبت به سال ۱۳۹۰ حدود ۴۳ درصد کاهش یافته است؛ تغییری که تصویری روشن از افت قدرت خرید و کاهش مصرف غذایی خانوارها ارائه می‌کند.
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3244613</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/689305" target="_blank">📅 19:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689304">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AAo3OxkJ3rq34pCzFPz5Sq0hreDaL70cXKGtGZz9nBaLKeqXbuwZBx1wwpw2iD6M-_hdl3KRaYJCnnGXsufYPYhRwI5vn29n5kraeX8R1U3VqPVa633JaLjZyrNrEad4ufOpQt7dQ-01LLIMPoHIoJBpS-ik6QZjgMh4AFZ92yt7ZerK0hrDmjE-ZHLKSk3uLcEiZux19o1D4iPSlXOkL1MofZ7zkeBoaTa0XYAa_vwxn9phFwWej9cZAY9nZh-JE8Wx11q-MwKIePgnhR6A5lQnu6eLMJzhhXNf8BsBYovW3N_TfkNMl_WqUzCkeHfdeTgf-QTa8q7S755sD80_0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جبهۀ مقاومت در کنار ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/akhbarefori/689304" target="_blank">📅 19:33 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689303">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
جزئیات جدید درباره تفاهم نهایی ایران و عمان/ تنگه هرمز با این تفاهم باز نمی‌شود
منبع آگاه:
🔹
تفاهم ایران و عمان اوایل شهریور نهایی شد و به زودی با حضور وزرای خارجه کشورهای حاشیه خلیج فارس اعلام می‌شود.
🔹
مسیر ورود به خلیج فارس کاملاً در آب‌های ایران و بخشی از مسیر خروج نیز در آب‌های ایران است؛ تردد تحت ترتیبات ایرانی و مسیر جنوبی بسته می‌شود.
🔹
این تفاهم به معنی باز شدن تنگه هرمز نیست؛ ایران ۷ شرط به آمریکا اعلام کرده و تا اجرای آن‌ها تنگه مسدود می‌ماند
./ مهر
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/689303" target="_blank">📅 19:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689302">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ow-AXOjl87poSgRaMrIh0HORxRbvaWnLH0l_zItnL0l6EFBesJeSEPW_OxcMBbEItjadKInIy4BNC9_79A_DCucl-gAXg80Yq-wdTbj4uP3YFN3PATww-hjPOx9eHb6NlxYWEtZM6agTMaqBGP0MhctltnwFfyOlSdEoS8tH-Iz2UH_s29MAjLsPohUoSQF1K_0F26Zg5ob_5keQCNMItZEvF-w2dqJKzAtvTdYidxPVSJoZ9LsRZerMIN5PaBY-cWRiwUDEqCPvbhNQc3pJthaIrNpLeYy92s7bVI6vNDfn44wVdzVpfyntx2eZxwpDYG-sEcA4QEsZ7-dLW5b13Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
قاب ضریح امام حسین (ع)
جلوه‌ای از عشق و ارادت به سیدالشهدا که می‌تواند زینت‌بخش دیوارهای خانه و محل کار شما باشد.
این قاب با حال‌وهوایی معنوی و طراحی چشم‌نواز، یاد حرم مطهر را همیشه نزدیک دل‌ها نگه می‌دارد.
✨
مشخصات محصول:
▫️
ابعاد: ۲۵ × ۳۵ سانتی‌متر
▫️
وزن: ۶۹۰ گرم
▫️
متریال: پلی‌استر و پی‌وی‌سی
▫️
طرح: ضریح امام حسین (ع)
▫️
کاربرد: مناسب دکور مذهبی، هدیه و زینت‌بخش منزل یا محل کار
💰
قیمت اصلی: ۱ میلیون و ۷۹۹ هزار تومان
با تخفیف ویژه : ۱ میلیون و ۵۵۷ هزارتومان
⏳
موجودی محدود؛ برای ثبت سفارش، همین حالا اقدام کنید.
📩
سفارش:
@gharar_order
🤍
هر خرید از «قرار»، سهمی در مسیر خیر.
@ghararshop</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/689302" target="_blank">📅 19:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689301">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOagFcrlEeQG2Jg5ElLvG1Gx2lTO82UowAr6ejzlW2wB6sUYn7zpgRmwBAZJ5sK3JRTOkHUE0XcwBdZ-az-YIXSWbipb0QJqLPRni_0n1X1aRWa9BoeNimNFdLdpL6-FfcrCwLM1lEv01xvvJJeMJ7gptjA_pW-5qwIbABMhlnpWE8bk0B5EM7k571H_CHbyMGjDhIcOyTlqJYc0m4HN3vFizQBbyWysN8YoDTIaKs23xVWK7PNmaC0xOcne4rSuJACfrUSNPUdFUqZV1cgNvHEKSdyJAQ4D1KVoictQZ6O9TTmlBAGJcesPwnvS1gBEYasIu79wi-OFFeLl98T9pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از فرح پهلوی در حرم امام علی(ع) - اواسط دهه ۵۰
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/akhbarefori/689301" target="_blank">📅 19:28 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689300">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
هر شهر، بخشی از یک روایت ملی‌‌ست...
۹۸ سال کنار ایران
🇮🇷
📍
شیراز
🔹
شهری که فقط دیده نمی‌شود؛ در آدم می‌ماند.
🔹
در کوچه‌ها، در صداها، در خاطره‌هایی که از نسلی به نسل دیگر ادامه پیدا می‌کنند.
#اعتماد_می‌ماند
#۹۸سال_کنار_ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/689300" target="_blank">📅 19:27 · 21 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
