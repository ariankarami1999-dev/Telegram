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
<img src="https://cdn4.telesco.pe/file/kQTnWz9_dPFhiQrfnjHw1dBVLYTjOAZkO1Fo8TtMqbHd5O-dkMHJL9qSQTxl09qB2jKIByRpwSeekQDXo93iTg6CszYrgOUMNyC7ZC5e0Ja-VZxTL35_RRg1uYjOcTd6ZuXPU8elYLqkUQgbeTboSW8-GbOpD-cFwkXMZrDKfcQUTWIM7zS2MvUBhhKlSAKs8YsTeMGLZFrQOJzmxOs3lQ-ojPRB8Ye2ZgQyQ000nvfuNaOUXxmbcIUwuQbBtQXmbaj6QCSxnshHM2Tu3CuNK1Urk7L5hfPKC1DuwnACUWLy9MMaFGjkKmgk-p-sIjfrZ0B9cWtdHYsNCBBkKrlo7w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-22 14:24:14</div>
<hr>

<div class="tg-post" id="msg-455857">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NxVjt2GYknQCTfLNT6W8ATpSOuIzw48AtFjWRM5xpyQqlh02KNPNOunMkgmVpwK8qm0W_H0kdNoxhZ0nm0j96qpyE9M9FLrJCMqRCOjgcw8WGR-w4WtQIKyf2FGWB7OJRK0wDrkAUp74-YUgDg-fDRPqpOIFbRzCDARE84JAL9eB7OplnZAsJ_o3Ln1jHvNPvSRbRRFr4iceTYU76HPFs4ir_79uGYwZpJHh8hD0SAJYZE7tuFXHlz5loUVGxIZzocNL8oI_EqFnoSFyRT611t1bsJiCloCzQ_ySpByin6d5JRHEvM9kpZ-yIpojU_lKqEY7wRCqyJ1Mo57MBcVEbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایکس حساب سخنگوی نیروهای مسلح یمن را بست
🔹
پلتفرم آمریکایی ایکس، حساب سرتیپ یحیی سریع را مسدود کرد تا شاید بتواند صدای عملیات‌های پیشدستانه انصارالله در معادله «محاصره در برابر محاصره» را خاموش کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/farsna/455857" target="_blank">📅 14:20 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455856">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37df6d9d9b.mp4?token=l-h8e_3VMKeGjdV6Bi-Axwdy06MYAtfP_0LHhx4W7raktSogAbyh7yKL0u-0N_hMyi66Kheh9RGKs8lpBsb5FBQ0wQcWEs9oSqOYckSFOJaM7sXqJMR-EJhMRUqMexRDVP-NfKTpPdutgTVNzCcKXU8fPfu86vFUOKuXCqZRfHpTuI4wq9PaNIGEtMqDTgn5uoelAMXgB-7J_P_C8ZdvElOZdarr9T2571vlGGwZS59pNiR1CyyJZ9vnCHXL255iOoLIe2iwlVhHygTpXPhM_N_l5j471rB76f0ZoaRTDdcW9qmljUp7GZ15kv1LSVuW4-_72lwCaLD-RMD46emyAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37df6d9d9b.mp4?token=l-h8e_3VMKeGjdV6Bi-Axwdy06MYAtfP_0LHhx4W7raktSogAbyh7yKL0u-0N_hMyi66Kheh9RGKs8lpBsb5FBQ0wQcWEs9oSqOYckSFOJaM7sXqJMR-EJhMRUqMexRDVP-NfKTpPdutgTVNzCcKXU8fPfu86vFUOKuXCqZRfHpTuI4wq9PaNIGEtMqDTgn5uoelAMXgB-7J_P_C8ZdvElOZdarr9T2571vlGGwZS59pNiR1CyyJZ9vnCHXL255iOoLIe2iwlVhHygTpXPhM_N_l5j471rB76f0ZoaRTDdcW9qmljUp7GZ15kv1LSVuW4-_72lwCaLD-RMD46emyAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک باند ۴ نفرهٔ سازمان یافته</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/farsna/455856" target="_blank">📅 14:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455855">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94ec95bfe2.mp4?token=cAt3KdtjFDQ6EQM1viGqd0InClDwB_bEzrcwKC3vyFoNUKVutdYExaxPCBc4LguaqK8-skSvCwr8GEdazGbNAv4jyBVwTzCXHHpp68-SIB1zS4oux1T977r7V8AyaW3GINh2eOuGt8cCG4BUflR4GISTbvHRN-0TLuYKoeCxZiqL0cHm04GUMLzMAa3SCB55ZiioUI_wUYakdIfxHxHPK1IJcso96iDvnUrKpEds_lV0eACu2fCKY046AZMhrV9fbw3HZm3F4Truu3hHxJMRsYPSt-ZKfzsuMhmq1sJJHrANj7NchT0w66yUsR7noH08dlk-_902mjwpKLcOEQHSig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94ec95bfe2.mp4?token=cAt3KdtjFDQ6EQM1viGqd0InClDwB_bEzrcwKC3vyFoNUKVutdYExaxPCBc4LguaqK8-skSvCwr8GEdazGbNAv4jyBVwTzCXHHpp68-SIB1zS4oux1T977r7V8AyaW3GINh2eOuGt8cCG4BUflR4GISTbvHRN-0TLuYKoeCxZiqL0cHm04GUMLzMAa3SCB55ZiioUI_wUYakdIfxHxHPK1IJcso96iDvnUrKpEds_lV0eACu2fCKY046AZMhrV9fbw3HZm3F4Truu3hHxJMRsYPSt-ZKfzsuMhmq1sJJHrANj7NchT0w66yUsR7noH08dlk-_902mjwpKLcOEQHSig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری خیابانی آستارایی‌ها در سالروز شهادت امام رضا(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/farsna/455855" target="_blank">📅 14:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455854">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ceefa4e9f.mp4?token=MzjfkLMiMZWxxwQ4RsC8hiE0nXNM0lvtZy0URXAYYUZM6JWWrsL2b6JjBr_xV-w_QBoKQMO5NR14wDsyukUr8zsGhfLb-Hb1DA4jdinLo50ZaRq8BQsvow6esa32Wlc7Typn7dUE5gjXpOEYJXRkf88CSyJYkQ0lJQ23zmK1Bf-oeSICCzi8Sr_vApFHBBxS5Z5JRSBl8oo-TWRTEhbKOXCZ_Vq0sD0GPEr5yL63UEHvsgclARQp-Dnp80nUycvSYAZOLKZZp605Bs6KcP_drXr1K8kjTqG1oBpfefZagz0gLqdJ1zZ6jDhoHdBLbaSrp6hBX5btTLwc46-7sjFyvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ceefa4e9f.mp4?token=MzjfkLMiMZWxxwQ4RsC8hiE0nXNM0lvtZy0URXAYYUZM6JWWrsL2b6JjBr_xV-w_QBoKQMO5NR14wDsyukUr8zsGhfLb-Hb1DA4jdinLo50ZaRq8BQsvow6esa32Wlc7Typn7dUE5gjXpOEYJXRkf88CSyJYkQ0lJQ23zmK1Bf-oeSICCzi8Sr_vApFHBBxS5Z5JRSBl8oo-TWRTEhbKOXCZ_Vq0sD0GPEr5yL63UEHvsgclARQp-Dnp80nUycvSYAZOLKZZp605Bs6KcP_drXr1K8kjTqG1oBpfefZagz0gLqdJ1zZ6jDhoHdBLbaSrp6hBX5btTLwc46-7sjFyvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انهدام ۲ هسته‌ٔ عملیاتی گروهک تروریستی-تکفیری با دستگیری ۴ تروریست و کشته شدن ۲ تن از آنان در جنوب‌شرق کشور
🔹
ادارۀ کل اطلاعات سیستان و بلوچستان: ۲ هسته‌ٔ سازمان یافته وارداتی دیگر از گروهک‌های تروریستی-تکفیری وابسته به سرویس‌های جاسوسی دشمن آمریکایی-صهیونی…</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/farsna/455854" target="_blank">📅 13:46 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455853">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHoAkR2-v3Nq4hCyXoPJyMXs-Q4DxCkcy0c7Fw5c6bv-EeHkLwHM9345SEfYsZyC-MgJliRkaeHCqIMeIGY87DW9ZgON22BRwLDbkKxbd2Gg_KMIpCoFlLs0gH_IFH4A-MxF8JV3QAuQCI8IxhF_fWvPk0kiZVCFLkVTY7fJOu7vG5Vojg75zjZMJby3TOIoQief2NzUib3ZOkeg5g4kzknYG67NGtd3HZwkxW4nN2plKhLtS8WoX75lcjT4XWFQL10dN6B62Sfe_djnluaON0e-tAPO7mgbGgjqAHjK69_7_IU7gRHhW-kiiVGKO0rGFKA31nLWDdKN7AYesgLVLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژنرال بازنشسته آمریکایی: پهپادها و جنگنده‌های ایرانی دمار از روزگارمان درآوردند
🔹
ژنرال بازنشسته نیروی هوایی آمریکا، گلن ون‌هرک، در نشست سالانه سمپوزیوم دفاع موشکی و فضایی در هانتسویل، آلاباما، با ادعان به شکست سامانه‌های پدافندی این کشور در برابر حملات هوایی ایران، گفت: «صادقانه بگویم، پهپادها و سایر وسایل هوافضایی از جمله سه فروند اف-۵ که از ایران بلند شدند و در ارتفاع پایین به پایگاه هوایی ما حمله کرده و بمب ریختند، دمار از روزگار ما درآوردند.»
🔹
این ژنرال ارشد بازنشسته که در پنل تخصصی مقابله با پهپادها سخن می‌گفت، بیان داشت: «این برای من به عنوان یک خلبان بسیار شرم‌آور است که بگویم چنین اتفاقی افتاده است. این اولین بار در چند دهه اخیر است که نیروهای آمریکایی هدف چنین حمله‌ای قرار می‌گیرند.»
🔹
به گزارش پایگاه خبری «وار زون»، این حملات در حالی رخ داده‌اند که در کنار حسگرهای مرتبط با سامانه‌های پدافند هوایی مختلف از جمله پاتریوت و هواپیماهای آواکس E-3 سنتری (سیستم هشدار و کنترل هوابرد) در آسمان، ارتش آمریکا سال‌ها زمان گذاشته است تا یک شبکه یکپارچه‌تر پدافند هوایی و موشکی را با همکاری متحدان و شرکای خود در سراسر خاورمیانه توسعه بدهد.
🔹
این پایگاه خبری در ادامه می‌نویسد: «ایران در روزهای ابتدایی این درگیری به‌طور فعال رادارهای پدافند هوایی و موشکی منطقه را هدف قرار داده بود؛ موضوعی که به گفته کارشناسان نظامی، خود به‌تنهایی زنگ خطر جداگانه‌ای برای نیروهای آمریکایی محسوب می‌شود.»
🔹
در ادامه این گزارش آمده است: «این مسئله این پرسش را مطرح می‌کند که ایران برای پشتیبانی از این عملیات چه توانمندی‌های دیگری را به میدان آورده است؟ نیروهای ایرانی ممکن است برای هموار کردن مسیر حمله، حملات موشکی و پهپادی گسترده‌تری را علیه حسگرها، مراکز فرماندهی و کنترل و دیگر مواضع انجام داده باشند. همچنین احتمال استفاده از جنگ الکترونیک، حملات سایبری و انواع مختلف عملیات فریب نیز وجود دارد.»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/farsna/455853" target="_blank">📅 13:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455852">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">انهدام ۲ هسته‌ٔ عملیاتی گروهک تروریستی-تکفیری با دستگیری ۴ تروریست و کشته شدن ۲ تن از آنان در جنوب‌شرق کشور
🔹
ادارۀ کل اطلاعات سیستان و بلوچستان: ۲ هسته‌ٔ سازمان یافته وارداتی دیگر از گروهک‌های تروریستی-تکفیری وابسته به سرویس‌های جاسوسی دشمن آمریکایی-صهیونی به هنگام ورود به کشور شناسایی و پیش از هرگونه اقدام ایذایی، در سلسله عملیات‌های نیروهای اطلاعاتی استان در شهرستان خاش، تعداد ۴ نفر از تروریست‌ها دستگیر و ۲ نفر دیگر در درگیری با نیروهای حافظ امنیت به هلاکت رسیدند.
🔹
این ۲ هسته‌ٔ عملیاتی آموزش دیده وارداتی مزدور دشمن آمریکایی-صهیونیستی قصد اجرای پروژه دشمن در ناامن سازی استان و ضربه به زیرساخت‌های اقتصادی جنوب استان را داشتند که قبل از هرگونه اقدام، شناسایی و متلاشی شدند.
🔹
همچنین یک باند ۴ نفرهٔ سازمان یافته شرارت و مخل نظم و امنیت عمومی در شهرستان زاهدان که درصدد ربایش شهروندان این شهر و باجگیری از خانواده آنان بود، در تور اطلاعاتی سربازان گمنام امام زمان(عج) قرار گرفته و به همراه مقادیری سلاح و تجهیزات دستگیر شدند.
@Farsna</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/farsna/455852" target="_blank">📅 13:27 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455851">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/988b13041b.mp4?token=LxyCCBAOA8J4mt9LTK1v5DnMvsvmLPShgdbPZbgOW2jv-bDtbSjvA7ZTB1uStIwOqwnZzkvSmuzBqNX4rRWvnWs6q01Y3oi4FQOKPpnsVA0r3ZUR9fTAbZO5p9tYryWQ6Hd_m1fqaTlUhR9KaXNWMQBhEfZcgR9exzhBcTFAR4zcGAewm1iOV2ONwD2L-qtJVauqqdxEgzLGCn493BiiIVABx8tVyd-NttRbwgebSdLuzexPBkVg6PcW6hz3grr4Ct9VaWnskN_ndbpk8-bvkazYbHzvjMIS952fxL2DxganCOv0RCjkulsdcTatLSHIK4aPJiAq4qyhx4BxSS28og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/988b13041b.mp4?token=LxyCCBAOA8J4mt9LTK1v5DnMvsvmLPShgdbPZbgOW2jv-bDtbSjvA7ZTB1uStIwOqwnZzkvSmuzBqNX4rRWvnWs6q01Y3oi4FQOKPpnsVA0r3ZUR9fTAbZO5p9tYryWQ6Hd_m1fqaTlUhR9KaXNWMQBhEfZcgR9exzhBcTFAR4zcGAewm1iOV2ONwD2L-qtJVauqqdxEgzLGCn493BiiIVABx8tVyd-NttRbwgebSdLuzexPBkVg6PcW6hz3grr4Ct9VaWnskN_ndbpk8-bvkazYbHzvjMIS952fxL2DxganCOv0RCjkulsdcTatLSHIK4aPJiAq4qyhx4BxSS28og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری مردم نهبندان خراسان‌جنوبی در سوگ شهادت امام رضا(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/farsna/455851" target="_blank">📅 13:25 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455844">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ljiRCg72t6ikgZjrB36I-1dQm9OBmT5BGY1FDQ85RsMQUvx4mLars6c0IATIwiJHV7MrsEcSefbQJYwEPAbsENRiJ8D2EbqQBDUiM3FgKAZyI7sEtO8AVW3-27zn-SxH7u1ya3EzY0UDuxTO6EOnQEX-i8PLeBTNWeLM3eaZH0BS-CHWSfgojlWDeyZ4pf8GMWWKgFoIChiWi5dfyoE7K7tnU7Q-_wEiT0ffBHXVmcj6wsgDnwPdHW-l3BQNNP-eaurt67bdWRHEF4WAxO2pRNBl07oQ30A089NxrRagxLlx1KaK_rh90hbC2fTnzX4g7KLvH24aQbWgfqNdnYb0Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JG03kG2CFpsSw9O0U9gFvQhiiEQtv6AeWhkvMl66QfFOcQnqVdxcAUSw12uAydlj6lpRd95XlhYX0WRBcr85sDWsUVS7S_TQDpOuh5PZHHxnR-P3e1JNbOPPWM7nkhRrlmJS9BZqbkvSdey_qS-wqzEPniFqNmP8fBsq228mpIHul44RJjEjr3zah4Qk9u_1Baz5ARpDCzBmhjrCczq_WP24Sa4L_bhG29oVnGpIfak47DlyscBdcwIHq6jEwBFteM_wfPdKuUzKrYXdyQbh2hKXMesjutlveB3se3htBZKvf64-AX8nQPClfgAzeo7iz0jcCCwtU_Zu2vlBh5f4gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DmMxMRMxFjB8pG4NRGDPIP4v6VuV0mp0FqoEyOub1At_3usEa8NluyzzRCMrMObhL4E7jkA-DSIr8ZOzS4kXTMmZSKiiasf57UGX9A8d33gI93tYl6BZJ-XtD_u-GZaLjZIThMj-E9PqMdFGSwKm6vPk1VPCpwqLRHm51jGtAV9D4kBorcJq85p_zGC0Sc0g7-Ih11klvlrniPcs9WKTf1_3UoNN8crD5JawYNEzVV7t6fQHeUv9HmoSVGfzWYdTPQBtYVmenvNx41ZEO68VWRtf03s66Fk_nWHz5nAX9y6luQmprLvuzkdb52It8V92xgtcm_VOUy5fg6bLKvOZ9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i2sIXXQZMeT4RUmS6JAL5ddgaS6UUebQDqFXMt28MAtiXLc_gEuv1YY-mYaAnx5v9PIgdZv9vFTHpK0RX5WrdrpKInAXkX4IryQwQOSCIpXQTLf98BLeSEBfC1SHyG-nRlVNLkAkHMalDn8Y4rJuUlKgyTP2JjZE6SN_M_rJ3q-hbNkulFKFYjtQwhb_ybwX2pCfVtTYwNG8cI6M1drVOlXtP4dzphP3U3hC-pAxMK7_Z6Sx81eKIVcL2VBUtr8lA6WF9SyjF6i5jx9cOHKG08MQ_IhC3iRHcXWYiDaSZ1xGMiiSoRANXDGaZcsA6xAZoJRymLmu7Ee4NC_sorPdtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uvoyBngm1pwJuXfHIwcRsGQXStT3mriXnJqTQmkv4s7SUbklecsaK_FQt5OfEmlKUJFHTe7fERXK-xnwLd9RL9FeciwVN8bZ-tdHeFM8EnjreLOROrCWqFyMaMNtwkdUbEtLZihPOTkv9FqCGMPQtTWNG7da7vtxUNYTjeMkP6wAJgv3yUu1sOc_bscGlDeijqTuKy9aBc6HzB9rrRuoIsrr_vh8dobqkeqq_uumpE0o7x8H4BDuFChMZLHG83eHqvPIIzn8HhqhVDHdUijDPZleTRFoAMFlZYu9EvuAg-ho8_JB3WGuk5cjAtYy6Hfjh9iWbl48MvE7pAAoCF3fdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XQpGb27tV2L5dA5qYuzAbVmots9Unq6p8FWZ3IAVAu11h1x5tQgw5kEJNp8UcmBCndh07Clz5UNSZjM0qddBaPIiNtSrQao7MUZucm5uBibyYLuhpFeVK7QqxZnTyUVwp2GrLIyURi0PQ0EcDglMt9BbfSM9jJ-bK8_-xIOsxjaWbbfwbWufOtlYZ92iQxq6eOiN8g2aYF_0LSOKXAeaBbnGPzLTF-Hoc-srLdVyEJJb0d0DjaiPeCBxhw4RrIAwx0jFqOzZkjRMeqOvY0V6fKH-rInF6-rLD9GJTah5Naz2IxOrwjIIEg6UYYgwTkYR5YEB9MnE8oYYXpdGDCqtgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uVAC8qm4bv_yitBG5cJrXyCq3ySlrIBaAWz-XWkxHdIVbqeZWJC4EDk55Wf3WsL_mHt2H0yGPHq_MK_weavGuMCFT0Qi-F_IhEBgoZiuyg4TErO_ycWXpEAbERe3BgfbKzIrB4n9yfeNwN940ESL4FCZSeqfueto_G1H711ysJvOrxbzfAoKJCLzgdc-ouXl2kgANGMB1QQTZirpL84wbsfS1JJ0ggXJmjIuANypI2zzHkapCDsX0TZ9l5ep0NonNt25FVd-Lb8aYoFcIZhl3XP9X4iXf5Vs-oBCxpKc-IKWtION-Av_Zzwfd0F1g4mfARQc1ptf-DQ1iCr3b7JwqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تبریز غرق در ماتم شهادت امام رضا(ع)
عکس:
عطا داداشی
@Farsna</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/farsna/455844" target="_blank">📅 13:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455843">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/712bc5e595.mp4?token=QrDJ_exdTRihlsCud69mhYmpCbOD4ye5uUwM-u2zRM_wvJxioCQ1wPHjbHzJ9RoVcQdn5cH-1Hja33OfwAX6n_d5J7VcTMXOpWEGrXK4qJoT_H8n1jnWkbndX-wKr-ju0u5JaSujXLEau4MEBVXaR6js_Il8IrJUWiNmedqjLOQDrTjCvhxYLuqv_XwZ2UTyzRCkxhDIVeDpMWnTYHm6KawE9-MhjT4qdNVLEMguAYYO9lk8MwTbgR1mN6jZxc9JQ3a_0NuT7OKVBBtdvfYNxjUBogjohOg_RzhHM9ofz7fO74U5_sk36I1bLT8V9vqEyV0JUXd8q4R5xsvb8ilhojzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/712bc5e595.mp4?token=QrDJ_exdTRihlsCud69mhYmpCbOD4ye5uUwM-u2zRM_wvJxioCQ1wPHjbHzJ9RoVcQdn5cH-1Hja33OfwAX6n_d5J7VcTMXOpWEGrXK4qJoT_H8n1jnWkbndX-wKr-ju0u5JaSujXLEau4MEBVXaR6js_Il8IrJUWiNmedqjLOQDrTjCvhxYLuqv_XwZ2UTyzRCkxhDIVeDpMWnTYHm6KawE9-MhjT4qdNVLEMguAYYO9lk8MwTbgR1mN6jZxc9JQ3a_0NuT7OKVBBtdvfYNxjUBogjohOg_RzhHM9ofz7fO74U5_sk36I1bLT8V9vqEyV0JUXd8q4R5xsvb8ilhojzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قطعهٔ موسیقی «به رَسم کِرام» با غزلی از رهبر شهید در نجوای با امام رضا‌(ع)
@Farsna</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/farsna/455843" target="_blank">📅 13:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455842">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0c5432f7b.mp4?token=F9TA-_exaZ4DQ43MQCHTXMMVNiCbx_Xl6i3biANqttG6zsdH-FmNMtAkwBrSabskjg9Uy5fOvz_8ZqoQKcWnItQ1kFVcJGu7zTMamubAzVtCwYhlsNGXmNpPAY26WGodze8Wkauhe187bXMpEL72s8X27u6j2X2eFBK9cmFH2hY7gdCzgzn4pbhfliQCleEbHlpMRxrPcWgbGPv-vW42K0NrF-0hN5--Z7VJ3vNfEaTl46lpojb79lTzl-i4TsLawRGVkQ1hE4gCEUJcZqhbqjhuXe-QiZ798YTyytJdjFkF7QBa2Sw55skaT94c-t_71SFaqgKpGQzYZf0ySE2Mkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0c5432f7b.mp4?token=F9TA-_exaZ4DQ43MQCHTXMMVNiCbx_Xl6i3biANqttG6zsdH-FmNMtAkwBrSabskjg9Uy5fOvz_8ZqoQKcWnItQ1kFVcJGu7zTMamubAzVtCwYhlsNGXmNpPAY26WGodze8Wkauhe187bXMpEL72s8X27u6j2X2eFBK9cmFH2hY7gdCzgzn4pbhfliQCleEbHlpMRxrPcWgbGPv-vW42K0NrF-0hN5--Z7VJ3vNfEaTl46lpojb79lTzl-i4TsLawRGVkQ1hE4gCEUJcZqhbqjhuXe-QiZ798YTyytJdjFkF7QBa2Sw55skaT94c-t_71SFaqgKpGQzYZf0ySE2Mkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زمزمهٔ صلوات خاصه حضرت علی‌‌بن‌موسی‌الرضا(ع) توسط رهبر شهید انقلاب در حرم‌رضوی
@Farsna</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/farsna/455842" target="_blank">📅 12:58 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455835">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dR4WzrWyPMj2USvc5aOIe_vB6R82m0BGdfLrDsPDp8zGrZjhIl9RY4wMTUvY0CRGla69G7WY0wt1DjT0D0SoRQhnoMz8msUklIN8aLh7B8SkMbsoWjcs-oUV2a0mydMw3Fz44MMvY3jGsc5O02g4J7vYEnVvh8eSIqOHopMr0O5YSId9u2ZAfsgHC1pjAddl4uT8N_-kgeRcYZhXncdSiFsrUuY7xy9gcqqwkrbtREnrbPMQNl0-FGzhCRQAL66LprzrIZnXZuVRJ4fXJcLlz1JDw_ETdl0VW3TzwoJJadUnkaV8bCkHPCZZN7YFhbrcIFy85rUHaZtZE3Ia_hYwbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CVXwB1FHcJFcLAWMBfu0KN_KEoxojtJy5pEnHn0Y0mbff0b_xpVeQDAH4QFKmV2HaYogwOsM2O9mKwC8gafnDbyx2OLGQegfNTw68n-2eTB948b5EIi39CEGBeGzoqzAU_3V8bKKz9g5imDeEqT6zHR5P_EOpaciiC_-J0fu-i3k5MDpv3thU2MqQKKbfdUC7PzXM1YrnDKDjJ4Hk4lGX6ZV_9-_Ig43qOIeKG7yfuYJMZIvkdWVsa_PhbbGrk_W2FocaKT74WxtwyZkcX1uO2tp1C0uprMFUyOIDzy16X3NvYxuXRjzuBMyqgOOLgL_vIckc9cuWLfhPY1b6krvLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OR1I9cG0S_fDtOAhrMzafoxG_zNi8vMWoAFq9CIy8K80XXG3B0QjHSJ0gRmUQO720r0T2SqpK7jmiBwj_JJXJQiTWraw83N56ywcTBOBg6G13SPibLO1gyVA2B8aU2HZvYdV7AMohvtkxrw81lKYCdPIhiY5haXDj0JS-bUW1AIShsoO-V5AWPoe4E5LmWqA4RGwVonz513eNt3AlQaggd6j75i8T13LVJygGHUP48pE-GPXHNtli2K3W5FeNcuBOtZaSwKO2JHfpbCNAai1zoFLgTpXKJ9zWnUnwYYbUHyRBOOtfBzSbYmsXgfVKzjOcc_s1JlUNQFA46MQ1A6iMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SNnCuSWtSNwBRZsyotoU9wBOlYysHvpMr9rbpQK21j0cw0yOFDJpwNepG0lj2EVp9dcVm0ZHpmdcQhuUvd32KBjKIp8D9Jov9Ax3ojyOsnrXkFo58MnkuFGXbkYh7KUFK-2ivKK5saN7GTgrc-34dpgQLNXSjA_-Nt67UDfYr-M9JLHPSoEZpSv7h_47oAgxQ_-RLLz9aBT453h9GVZsuIkHUpufds1t3XIJSQ2RGWMfzDkXQPCB-h8wxBcOerm05DkllvrIMQMAFA3qx0jxaJm03yQ-gUXln6q3LAJv5U6Su9tPiKJXEWvcRmKgks2jZCAkc8cn7MxmFSA-SCAXTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h0RceKuJ3JIBcnYG-iyEk3XJ9C-yZMeWeac7klKPmfOK5VaOicz8CVQD8oDpTwx_EIO1G29Vfkg42TKDg-DVmR8pQ_EVLepdl4Y8NcXHPbqhLDyPGpAQURVv1OQ71bi-USo-jJpNDptfRsjO-5Q3cX-ac0iyjNBoz2G4cz-t01gs7-uY56WnIeJoANEDMGmtasSW83iGPpLKpjrho7IN225xyo6FNLql1f-rFc1dxGlFhKxTDtLIHKBcDYS8RAQHGmE8E7ZMFUvyRLaHGlTRDQMDN-M61DwpJ2FnENyesZs0uKzLVLlnlT3jVQTdxvQU0pR7u_2l5xcCU7qYIfXJtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nXN_2YJs6DjzWxRjRD2YI_gWmPhy9itRgsIhOyI844kR6JsQTPPhkz2ZgRd_QJb1cFdoIoshrkslhtXILZSlCvOBJoH6bXm-PN9iX7hGyxwW0Y7BZGfsaxPt8xYP3XrFMtKrgwSdjH3aUI03JPwHY1hdwNsbUxUBfvxtkodWf4MaloAsVUe71ehL_R6tGUZ1K4oHAHnCRIJnKnaDQWWh5daYGXmlbzRjAuvHPjggjfWC0TfW8Ic0wgi6gk9XdQowB_joC6xwv2kWBcdANQsUT-2q7DRad_LhAPfWpqmxvZUb-tK9fkqwZ77lis67QTguR6ZQlIjJPxjZ72exySr-Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K1SDSao7KGwiEBteMKSWvZQRZPlerblvpqckWj1hbsb1Tdu6jYq5qoGECq_g33CAMKAQVk0lHDEZ8kK03z4nKdR9r15KFUUiRKsIqqPn1rPcBLR4ToAbXINDWKS44U6fJxUtZ_jwj5-Uf-8Zx9veiCgl18F_Br6Bd7gS8hXZn_YAXPnLQUyOvdcA0EMSxQnGOBHlTndkhtJN-dzJGlafiZnYIxjqz-Lln0asg1o8Sl-JX54dJAioLmiP-X9Y8Vibv9e_9x7w_5UcDGMEDHylymtnZLBOGbJFVqy89ndQYAZcIJQjftGKzHrxArrl_Pj6o5YAA_rMlDyhWLcxvQg46g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آئین نخل‌برداری یزدی‌ها در مشهدالرضا
عکس:
علیرضا رجب‌زادگان
@Farsna</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/farsna/455835" target="_blank">📅 12:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455834">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/636abc426c.mp4?token=DuSOW35qF4E4Xu9g2-eW91SN2-AuWwSaRCCcqjOJRQOM_E3fFqJR5Lf27Hlt7uutrf5L3vEYlEYKa2PyIUNQrtNbFEWptH0mVCisGBioScOSiHcWqNZCJ55t8LYQRGUjVnRiiLnwn3WLLwWHYwF5sDpUhFTLaF8H5LNfOn-MoQI8mKRwPUKtWQiGSQg6OcddcErkGYj02sSp3KGS7ugt4mU70SCfnFLE8h6HwoqTBS0rvXz3q9epz5VdAvp9fYzI8X9QjSzuwHKapJ9hLGwvHT_HLw4KxtvVCE16s1_C1rHDZQk-1u1qE1LHjcdqXHb3mrMJZJneIND1hHsB8Vp-LDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/636abc426c.mp4?token=DuSOW35qF4E4Xu9g2-eW91SN2-AuWwSaRCCcqjOJRQOM_E3fFqJR5Lf27Hlt7uutrf5L3vEYlEYKa2PyIUNQrtNbFEWptH0mVCisGBioScOSiHcWqNZCJ55t8LYQRGUjVnRiiLnwn3WLLwWHYwF5sDpUhFTLaF8H5LNfOn-MoQI8mKRwPUKtWQiGSQg6OcddcErkGYj02sSp3KGS7ugt4mU70SCfnFLE8h6HwoqTBS0rvXz3q9epz5VdAvp9fYzI8X9QjSzuwHKapJ9hLGwvHT_HLw4KxtvVCE16s1_C1rHDZQk-1u1qE1LHjcdqXHb3mrMJZJneIND1hHsB8Vp-LDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرازهایی از زیارت امین‌الله که سال گذشته در روز شهادت امام رضا(ع) در حسینیهٔ امام خمینی باحضور رهبر شهید قرائت شد
@Farsna</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/farsna/455834" target="_blank">📅 12:51 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455833">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GM2e-8RWnQl_6T7u38Woh5HDDuVVUVwj9mOC4Ip4DBLw1nWXuVSH5a-9pwvwtAhsg5OOlTHvlBIpox2fkOtSMjLkilR070qSJcpQfrUvQtJEYbbYcNXQlK6Mli16VR-ny3g41aviOtfHKEqJtKchDcrBpCQ8xMpEe-1U16XrSJ_aAvT9IKnVCi9aNELNTiTEsWVzys87H05CU5ftqHxHnluwRFj51aZ-CI8H-1c1QkYvlKnaDjNm-_fgtRwrmguwPNllF9T4Lh5ki2PZwmji_PvjMXZnit2ywgaHwKeiXjLKJ8X5sLV7sl-pt1MQ7RJJzlCOVy3HUCZZQ5pDznA_0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گروسی:سازمان ملل در حال مرگ تدریجی است
🔹
مدیرکل آژانس بین‌المللی انرژی اتمی: من خطر فروپاشی یا نابودی فوری و ناگهانی سازمان ملل را نمی‌بینم. فکر می‌کنم موضوع بیشتر به نوعی مرگ تدریجی شبیه است.
🔹
سازمان ملل در حال از دست دادن اهمیت و اعتبار خود است و سهم قابل‌توجهی در حل بحران‌های جدید یا جنگ‌های بین‌دولتی ندارد.
@Farsna</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/farsna/455833" target="_blank">📅 12:46 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455832">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h66gv1R1a6u41K6Nx3yAzfbCaHu_RbU09bjy1F-Xj-UATVMhERKGHq0PkRSrS7JwP2Jlz3MT6Zownsk8TZJKT7dRv57YS3TUuzcuBIhd2VORuMGe4tLTSLI3qccKsT4owvhx7MK73zu7fTLO9iR2kp0pumAr3911utp9ygkNG6F6CLsDA9T-TkUg60msHaKox9-9k_hSa8yUQ8YFuMdKXi_IwtVwBc-nnWIoJ0RBIjl38ZICAoQccTLwtzg55szjxYi_lyrDoHdxEsjM87JDnXO-8XQ36xUe227zOURiNVyQibG_Iz_HuRWs_QNF8Op5tnKg_HenOD-QYgKqEbW34w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار سنایی‌راد: در جنگ احتمالی آینده تهاجمی‌تر از قبل عمل خواهیم کرد
🔹
معاون سیاسی دفتر عقیدتی ـ سیاسی فرماندهٔ کل قوا: دشمن تصور می‌کند با ایجاد اختلاف داخلی و فشار اقتصادی می‌تواند حوادثی مشابه دی‌ماه را تکرار کند و در همین راستا اقداماتی انجام می‌دهد، اما تاکنون محاسبات آن‌ها محقق نشده است.
🔹
امروز نیز اتحاد مقدس مردم ایران زیر پرچم «الله اکبر» و «لا اله الا الله» شکل گرفته و باید این اتحاد را حفظ کنیم.
🔹
در داخل کشور باید به این موضوع توجه داشته باشیم که اتحاد مقدس، هم سفارش رهبر شهید و هم انتظار و مطالبهٔ رهبر معظم انقلاب اسلامی است و به امید خدا، با وجود اختلاف سلیقه‌ها و تفاوت دیدگاه‌های سیاسی، هرجا پای دشمن در میان باشد، وحدت و اتحاد مردم تقویت خواهد شد.
🔹
به عنوان یک سرباز کوچک عرض می‌کنم که مردم هیچ نگرانی نسبت به توان دفاعی کشور در برابر دشمن نداشته باشند. ما در جنگ اخیر ایستادیم و به اذن خداوند، در جنگ احتمالی آینده محکم‌تر و تهاجمی‌تر خواهیم ایستاد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/farsna/455832" target="_blank">📅 12:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455831">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9394ce654c.mp4?token=EfC658pIr7bw50Uir24oMEtgY_-3jIdxjtMJzzbioee-E-1htkdmjru2RCMmfsYUvhLq_yO2GhATmBVdm3XjkFno-u35775510LHeVrooEgHlH72eRTsq0uQ5xtE-HwdimmCUPrrxOjci6QOfdEc0SAknAMO2IOwfyxL0D-2Lrx2QGXVJCZvQuz0qsEB1_y-mRdUWzp6htw4xegHuUusUtXCP43Vmu_NhCxLt--6IaF7en6IWC_LZi8AC3jRI3ibpmxGcz8s3YabSuj21peXpvQJcp1kaG2463rrIJ7713BIa-_pkrn1kkD1Bv1B6_yTzoohZCyS11fDafmdq_F7qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9394ce654c.mp4?token=EfC658pIr7bw50Uir24oMEtgY_-3jIdxjtMJzzbioee-E-1htkdmjru2RCMmfsYUvhLq_yO2GhATmBVdm3XjkFno-u35775510LHeVrooEgHlH72eRTsq0uQ5xtE-HwdimmCUPrrxOjci6QOfdEc0SAknAMO2IOwfyxL0D-2Lrx2QGXVJCZvQuz0qsEB1_y-mRdUWzp6htw4xegHuUusUtXCP43Vmu_NhCxLt--6IaF7en6IWC_LZi8AC3jRI3ibpmxGcz8s3YabSuj21peXpvQJcp1kaG2463rrIJ7713BIa-_pkrn1kkD1Bv1B6_yTzoohZCyS11fDafmdq_F7qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پایان قلدری شرور اجیرشده با شلیک پلیس
🔹
در پی انتشار ویدئویی از صحنه شرارت و قدرت‌نمایی فردی با سلاح سرد در فضای مجازی که در آن متهم با استفاده از قمه به یکی از شهروندان حمله کرده بود، تیم‌های عملیاتی پلیس اطلاعات تهران بزرگ بلافاصله وارد عمل شده و متهم را دستگیرکردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/farsna/455831" target="_blank">📅 12:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455830">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5fa4cf399.mp4?token=qTH2Zqa7fxSue37ZpKfffWN1aIuCyYPHtvhtw6L0BYGP76QW4gVoCyDsNGJtlhfsWeL3mMq_xxh8yoc40dlHt9abET2RwUvpYYK0rJEa0dmaRC3UwhdV0YOSvob9-P9aTWJNVMAaG1rfhdL-4JPGYMMC3Fki-0BBsaDV4RPYmKYhBwX7eCxDNpIJ7IFDogODCWzqUZdfWLU3ien4fXEgiLiKUpUR7-bcVAsS2--6rm0vJfq8yyKXjYdcG4Co9IFHw21OjTzjJmQJxx4N4YzKV8YZVbF8aMXOl0d3_kiLUM-xTbzOkIcJTRhfbsiTWQhhXyXfymhPFk_Ie8GUmUAx50HQ2eDHv9Mxtvp3zqGXidvzf31mkp-6jmVD2PzF3Sr8mOQeywYry14U4zvH3TW1af39FX_lwUsz1O_TsmhsJmGDSJSyWk35buvE_OxnmheEYJ3qsV9YAshPirefbd8vH23IRlUObgNPBja0Xt367NXouBtarRuy_lVgq9lgIQu2zWmZX0bjhBg7P9wj48KH9B7k81JNNP_onSTZ2ufzkwzcF5-nB7zIB8W1HE0iYxirG5qjpnGux6mx44uD9GkgXHL7FMzANFeAs1Nf9w-SOlrjEUY19hNqTwrMKRK1LrnccxidQMYEHOZtu9T5rbOYfFPtpfWd7lh7fNrmCn_3fW8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5fa4cf399.mp4?token=qTH2Zqa7fxSue37ZpKfffWN1aIuCyYPHtvhtw6L0BYGP76QW4gVoCyDsNGJtlhfsWeL3mMq_xxh8yoc40dlHt9abET2RwUvpYYK0rJEa0dmaRC3UwhdV0YOSvob9-P9aTWJNVMAaG1rfhdL-4JPGYMMC3Fki-0BBsaDV4RPYmKYhBwX7eCxDNpIJ7IFDogODCWzqUZdfWLU3ien4fXEgiLiKUpUR7-bcVAsS2--6rm0vJfq8yyKXjYdcG4Co9IFHw21OjTzjJmQJxx4N4YzKV8YZVbF8aMXOl0d3_kiLUM-xTbzOkIcJTRhfbsiTWQhhXyXfymhPFk_Ie8GUmUAx50HQ2eDHv9Mxtvp3zqGXidvzf31mkp-6jmVD2PzF3Sr8mOQeywYry14U4zvH3TW1af39FX_lwUsz1O_TsmhsJmGDSJSyWk35buvE_OxnmheEYJ3qsV9YAshPirefbd8vH23IRlUObgNPBja0Xt367NXouBtarRuy_lVgq9lgIQu2zWmZX0bjhBg7P9wj48KH9B7k81JNNP_onSTZ2ufzkwzcF5-nB7zIB8W1HE0iYxirG5qjpnGux6mx44uD9GkgXHL7FMzANFeAs1Nf9w-SOlrjEUY19hNqTwrMKRK1LrnccxidQMYEHOZtu9T5rbOYfFPtpfWd7lh7fNrmCn_3fW8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای حرم‌رضوی در سالروز شهادت امام هشتم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/farsna/455830" target="_blank">📅 12:24 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455829">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkBYC-eeCkwUtnRuvKu9xd93V8DQYrsiHGrzpdD0qhjBGdlvsuAWAVpnckX6bRCOiN-j-BZS9W_g9O34SXPvJm4PoJ0AU0iEmPspZqV2_5LDcwwm0L30Sg99S9__UJ1xXoPZNTJ0J1lI7CH-kqV7S2RSAomzlX7UlK5rIZHCa4KAoKl5lxENEFOB7FVfKQlbMS03Z_mEOpTOywibttnRL2OaCKP_OSnTBpoMna4y5Wg6iftW8RzFyR-j92O2m92UzDWT7xubpeFJMz-n6njIL2OHthatcnfyKhsfxpQ8LEc7xb0HME9FQzWGNsI96FP48UpnfEkURXNsZfcbdVhvWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران: بلندی‌های جولان بخشی جدایی‌ناپذیر سرزمین سوریه است
🔹
وزارت امور‌خارجه: ایران لفاظی‌های نخست‌وزیر جنایت پیشه رژیم صهیونیستی مبنی بر تعلق همیشگی بلندی‌های جولان سوریه به این رژیم و نیز نفی کشور مستقل فلسطین را به شدت محکوم می‌کند.
🔹
اساساً سرکرده باند جنایتکار و مافیایی حاکم بر سرزمین اشغال شده فلسطین در جایگاهی نیست که راجع به تشکیل دولت مستقل فلسطینی اظهارنظر کند، چرا که سرزمین فلسطین متعلق به مردم فلسطین است و توهمات نژادپرستانه رژیم نسل‌کش صهیونیستی نمی‌تواند این واقعیت را تغییر دهد.
🔹
علاوه بر این بلندی‌های جولان بخشی جدایی ناپذیر از سرزمین سوریه است و جاه‌طلبی‌های استعماری یک موجودیت غاصب و اشغالگر نمی‌تواند واقعیت‌های حقوقی و تاریخی آن را تغییر دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/farsna/455829" target="_blank">📅 12:13 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455822">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/riaxsymK0rLrtD0Qclf3AThWrRVzfB0Zb6fTWPSfCi-dKZitdKC8PcI50vuby1t63F1nO6A6KixSygOlZCJ8Y0YPaEStHD6cOnLdnXhWEZ2qwunqW9lvyC1AI0HmJ-XzFi9zh4TrtH2mPboScQSpzaL4UfW9CLDQ7euwheTdYwW7bD-v5iMmLaZcVXxvbvOTZNT0HmwDPByZi0eCNfM_8eqxxS5Pj2ZH-Hwmdi-rhwpRaY9x1oUPwRdNfulsHJmsS7TkpL4Mvm-ISwcYw3bVmtlzFGAlzbd3P8Roh54E1fQzkeLZdByl1XPbvYXfbEB_GQnY6-CkgXLeu_1LZTUaZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GQF0ykdx_7yRNCToQDNIudJUK4HL2ADS89k34BMhYY9v6Q5_jegmEdpg1R9RkcKZjniAWVBIj0WL12CbB-9kguWPUZIYu5os3HrvO7cIjoeF8Of3wckKxYkHNQz5Hf72oAKGAt8LWmpZrxWALRDHTsygScOxzKZq8L4LfICMgJX-eXYEUpbbYnst_0MEYeADMqxgqbGfz6hAdB6iuBZ1UvjNYS3lZNPceRKhzmo7LMxq5NJ6Eu_Qj13APw7XLUET3_5YbMeXdmd76AUiHP_uBDkceSYgZQkIQuv22P_h6KTcKF7k7M3mYqKM4Lvt05YJywaff3xhOyzWDtMuu9X__Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GnBWiOYDelEugyHq1ySFatA-Nzymkihcy1Mg5gRxJePoBezTvE3YX5pocss7M3OLOv0eyuWi1I7DSkpWPzzILnXDFBmoYezvI7Au-Q2ertDPxjwz_NIMAcCEcgXYCi65_Abil9aB0m8I0wpzffcv0LPkz-D9CrLDtKdnuLUvM-tlLyCCAoijgPTOtFp1RHG6OPlgtKWiEI347SJSsV7Yq2k0X7qHGWHbq6OIsXgmtPNuF7rHLymShi_dTOE71lzlcdqd2ASMm0qMsG-OoTYZCz3MX7y-KnVNSDQQKjLV_E1kasCfXF88IbwF2jKmZj4tFpeOrlt6G6rb2fvQtKQ85w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gvolG8wI64P8XtfNkgeyoYosYh1g1_j1CcokIYUwXdmRtcxbkU6cBrqNITikxM-SBV2BkTAgJ9xubdE_VzkhnLmhouerq9PEUXQjn5O9QeNse0KsJbSdpKByh1en_AWh5MUGH9Un6g7nVIDFmyz072yejDSEz3LfCxWA1sl25i_HDhLBu1W2Y096iUAmaChbKas8r_2JezD4pRkWx0oWoX3W-jQg22pG6iBxc0NTn8WrX7u8VkY0BfEQ7S13tbLm5Neh3MnEVQB1Bo753RN8K3vaZaDcbxtxnP72Vl8fqXXkDMCFBPw6gsQXWf-_gmLIEg-WzcuBlcnfdBvO2M2INw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fFu93nnxAaBtKKn-UxARgEkWbLOPhUcpSujPpl1qwUY6ykVwkvhJy4L9hbNrhgjGRX6BeMfMxeGuHC8lILm_RPJAxlkyj_DfrbxToqznFaJbsh09PY9QfCjgAovV6oL3-ewRcXSSO8YqbZRSFg_qc_YXUp2i2dMprc9O8vx3PQHJ_mQACgJj-SAgrrSUQHoRQu1b9pQb59o61F3DTiCRs7MjwssNvqMT1NQzCa1jTK6UIKzA24bdpKM_ApU2kh7wQ62arVzRmFWFDCmlN6UTMravxFBjENRygmeOTYLYl6O-y3lPpJ08jUwSdZYopQdGVnRN8z_w-hqyDRO1KfhplQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Edb0RRjx1ttYblbF03DW6LPuE74uyvTrHtr2oE4nLWhvFMCPSaVYVAI_nvVR1OCgjZQSoRDoAyzvlt9-KieskLI6Ww5XrdEzvmz4t3FONBGYGoPAScVu-CQDs-4RaQEBlvs4ABKUQZz7n5NSvVsA03rpxhLaL6IOghXyWmn8E-NXb67YjtjX9Aly7-clkjD7P8XQr1I4N9SejuQaV90ZuiIfjWnflikIklehJZxZdAtEqBworfVlk3CPTYgECe-yjN-k66o7myQbx81GGMPmDihPqbG7Wqp8knFwgdZAjX-WG8TyWNRl16XJeXZ-7oDbxAh_oaBWQZXUbRuUKThXQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ul0tqzTlhKGkxtPOCFnC5OS-J0FUP0PwnqCjcSIfiiv-LCU1WkNcci7QlBh9kI0FyanjHN_gNy80XXoQLwWlk804UYZIxEIWzq_LACSZBqU847uUBFTp42ZnQw_oeUYWyE3K1OukSWbM7zvRKQWZzzeoM7XqFSGAeAwZ5HJ6TcisQ9otMlHlDOnGV5iQx1HH2CAh-2wKZuQfRZDmnEAPLmoH98IsuSkhJ7M7DlBV9PqqQo-KPAnv46JgCe9KoeFkYfdT6XocouLva3-pCizK9GRLV-TL3PDCnqiivmklSOOJqkYJpZgSnpbatxCyrPjFTZ9gm-nSkgSwjXZid3AXKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عزاداری سالروز شهادت امام رضا(ع) در حرم‌رضوی
عکس:
حدیث فقیری
@Farsna</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/farsna/455822" target="_blank">📅 12:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455821">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3961b8b3a3.mp4?token=CXMzzwDrqTP4BBxQFORhsPCFgjMZTqlI7uA0zYybNmLVDK1QJKso03Sz4mamYBwVGubjA9WnM4W5BpQdG5XReeWSzOR5Dda65cH69n17X4cIeJ3fsJDYWnWphK8K_ErsD7CLTEgbDP6ApZ7b8kbEvNPuKvSdK026vhJWbQNgVEX82lenNYeH9UdchHyasbA0ykx4oq6zNjRiWV8GpUoyFPWJCApwp7hBu-SgupxraZ0tFPmfREGSt0C7019GOF-y0psqDGPOWImdFoS1Kd5_1W1V0tmzquF7dwBjNTg5AfcGgaBYEOhojaKNlBexZFk5n_jNH_xBfw8FCi6tKMWs5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3961b8b3a3.mp4?token=CXMzzwDrqTP4BBxQFORhsPCFgjMZTqlI7uA0zYybNmLVDK1QJKso03Sz4mamYBwVGubjA9WnM4W5BpQdG5XReeWSzOR5Dda65cH69n17X4cIeJ3fsJDYWnWphK8K_ErsD7CLTEgbDP6ApZ7b8kbEvNPuKvSdK026vhJWbQNgVEX82lenNYeH9UdchHyasbA0ykx4oq6zNjRiWV8GpUoyFPWJCApwp7hBu-SgupxraZ0tFPmfREGSt0C7019GOF-y0psqDGPOWImdFoS1Kd5_1W1V0tmzquF7dwBjNTg5AfcGgaBYEOhojaKNlBexZFk5n_jNH_xBfw8FCi6tKMWs5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تیغ مجمع تشخیص بر گردن بانک مرکزی
🔹
رئیس کمیسیون اقتصادی دبیرخانه مجمع تشخیص:  بررسی سیاست‌های پولی و بانکی در مجمع تشخیص در حالی بررسی است؛ هدف این سیاست‌ها، اصلاح ساختار نظام بانکی و به حداقل رساندن آثار منفی ناترازی بانک‌ها و عملکرد بازار پول است.
🔹
گزارش کمیسیون اقتصادی پس از طی فرآیندی طولانی به صحن مجمع رسید و چند بند آن نیز به تصویب رسید، اما به دلیل شرایط خاص و ضرورت‌های موجود، امکان ادامه بررسی جلسات فراهم نشد.
🔹
استقلال بانک مرکزی و اصلاح ساختار نظام بانکی از محورهای مهم این سیاست‌ها است، همچنین با توجه به تحولات نظام‌های پرداخت در جهان و شرایط تحریمی ایران، باید مشخص شود کشور چگونه می‌تواند از ظرفیت رمزارزها در نظام پرداخت استفاده کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/farsna/455821" target="_blank">📅 11:58 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455820">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4fVby-hm42jvdW8Olb5bv7RqnSphlpXzqMwstuoixUQdMKWGZhoQbJQAaZZIIlYc6emj6WVlqPaTyeVnNVukjELQ-qcEK51DZiWWqwMmznYIVu-KJoCAX9Cv0mKO3N5p7w9LQQ69xPhmayeQkFfW_waPIJuMHT_R7OF1pq7NG_OPH4JgfaFR5Z2XI3G9Ckfl6cu80E88A5GY3Pzll_5M9lnQwkb-AS2STW0J5DyRs7GTnPvAEXy3DU4-UtzPFHHMCXKalhvYDJEj7ZKSfd6gJ4Rma-TfRwmHv7CCM58RIUAhL8zwlGuhzYe9zGfNkv_YeWnEVyIAdGkg8Uio03Tzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طمع ترامپ برای درآمدزایی از تروث
سوشال برایش دردسرساز شد
🔹
دونالد ترامپ به دلیل راه‌اندازی سرویس اشتراکی که تا ۱۰۰ هزار دلار در ماه برای دسترسی زودهنگام به پست‌های او و مقامات ارشد دولت در تروث سوشال هزینه می‌گیرد، با شکایت جدیدی مواجه شده است.
🔹
شاکیان این پرونده، نشریه اینترسپت و بنیاد آزادی مطبوعات هستند که در دادگاه فدرال ناحیه جنوبی نیویورک علیه ترامپ، دو دستیار او و دفتر اجرایی رئیس‌جمهور شکایت کرده‌اند.
🔹
این شکایت، سرویس «تروث ای‌پی‌آی» را هدف قرار داده است؛ سرویسی پولی که اول آگوست توسط شرکت مالک تروث سوشال راه‌اندازی شد. شاکیان این سازوکار را «بی‌سابقه، فسادآمیز و خلاف قانون اساسی» خوانده‌اند.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/farsna/455820" target="_blank">📅 11:52 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455819">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8cb1de271.mp4?token=SkJCkKZrgTJyiHLVUb_Kd9Apq8uORgVhG2iJ6IbPHIx3m4zPsYHMcrfnYCW0TPEwL6lntYheM9vc2EagymzW3E5t-31TuILINrL8vbD7txpRbcaf4AJhlZNFi1exfH4BdzVUOFvv8xr6Aqn5T5vk3fKafxVOvvZm51j5euIXeQvvTYaUD06O-2nIglV54GXIy1x7ltHSEYhWjYizvPHDnwFWYzfjiZF9eX4D3Dswac4Uii2s04XpN1RG5udWTayRU6f5XuEBxgRqPaVF59XNFMtYOBIKpHVcHc3RFWVms8vaCRjdSk0gYXzAT8v6ggj6bJi43zHflHBZ8JZDiv6d6Fakq7QtK0pEQxuItyj-YACS3Cy68CFrexJX-051rtP6A4_JVX1oSXUVjxZx9tPCjlKk0QXCy4rq3opWByrqEMKWd9JEG5d83kMw2uYimuY-17ckDNf09puBvZwyIvLScXNZptlOAQtLld3jvyYM_TYWwmM0IetjPT5vcviwTDkCJsxtcWMx-iMvfdUu_JQM0LS9vcU1YCVTaDC3g0GXidSPOSTb869vPgyCfsi9qSA-6H7oTief7TDMnQRfk38O437buMPaPD3sle-eYgJM2bxujGg74pyY2X5O9etzWNcL1sUKF_G1Z6gHy6oZ9Ywh6PiMsZnBFb3ohm2YZHuwHII" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8cb1de271.mp4?token=SkJCkKZrgTJyiHLVUb_Kd9Apq8uORgVhG2iJ6IbPHIx3m4zPsYHMcrfnYCW0TPEwL6lntYheM9vc2EagymzW3E5t-31TuILINrL8vbD7txpRbcaf4AJhlZNFi1exfH4BdzVUOFvv8xr6Aqn5T5vk3fKafxVOvvZm51j5euIXeQvvTYaUD06O-2nIglV54GXIy1x7ltHSEYhWjYizvPHDnwFWYzfjiZF9eX4D3Dswac4Uii2s04XpN1RG5udWTayRU6f5XuEBxgRqPaVF59XNFMtYOBIKpHVcHc3RFWVms8vaCRjdSk0gYXzAT8v6ggj6bJi43zHflHBZ8JZDiv6d6Fakq7QtK0pEQxuItyj-YACS3Cy68CFrexJX-051rtP6A4_JVX1oSXUVjxZx9tPCjlKk0QXCy4rq3opWByrqEMKWd9JEG5d83kMw2uYimuY-17ckDNf09puBvZwyIvLScXNZptlOAQtLld3jvyYM_TYWwmM0IetjPT5vcviwTDkCJsxtcWMx-iMvfdUu_JQM0LS9vcU1YCVTaDC3g0GXidSPOSTb869vPgyCfsi9qSA-6H7oTief7TDMnQRfk38O437buMPaPD3sle-eYgJM2bxujGg74pyY2X5O9etzWNcL1sUKF_G1Z6gHy6oZ9Ywh6PiMsZnBFb3ohm2YZHuwHII" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تازه‌ترین تصاویر از آلودگی نفتی در سواحل جنوبی قشم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/farsna/455819" target="_blank">📅 11:39 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455818">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5dTax459NLjdsc44tq0BVzS35nOHV8fxSz4bdnUUY_dNKpHhRI8VvXRU8u5wyVVRi9ExWEp_6GetxAxok8mtfi89xkuNas8GwiRvKaS8FO9uMtZYw8jlcBbLXZPR8u07i1wBlm_CwMPeyxz_rOPdYnyzATQRKAlnTqQ7H5FFYweBqTksuiQK_fi1HBHcjzGK2HSS4eUyDkNWRRWC28_nEwNqavr2oQQ-WsfAyGq78InmqTPxgHYqzFlanEn4JfNYqx91GCtBabDydLi9qqlTThB6scOS7mjF3iMk5QGDt3-XmXJhDXGWw4sVbuJ56R-e38QL_8r-UQSjsGRhUzt-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: آمریکا در قبال تنگهٔ هرمز، مرتکب اشتباه محاسباتی بزرگی شده است
🔹
آمریکا مدت‌هاست که به دلیل ضعف اطلاعاتی، دچار اشتباهات محاسباتی مکرر می‌شود. جنگ علیه ایران نمونه‌ای روشن از آن است. اکنون نیز در قبال تنگهٔ هرمز، مرتکب اشتباه محاسباتی حتی بزرگ‌تری شده است.
🔹
بدتر از اخبار جعلی، اطلاعات جعلی است. مراقب باشید.
🔹
الله بزرگ است، بزرگ‌تر از هر قدرتی بر روی زمین. ما بر الله توکل داریم.
@Farsna</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/farsna/455818" target="_blank">📅 11:32 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455817">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🎥
آمدم ای شاه پناهم بده
🔹
نوحه‌خوانی در حرم‌رضوی به‌مناسبت شهادت امام رضا(ع)
@Farsna</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/farsna/455817" target="_blank">📅 11:27 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455816">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">دستگیری ۱۵ حفار غیرمجاز و کشف ۲ تُن سنگ طلادار
🔹
فرمانده انتظامی کلیبر آذربایجان‌شرقی از اجرای چند عملیات هدفمند علیه حفاران غیرمجاز و قاچاقچیان سنگ معدنی طلا خبر داد.
در این عملیات‌ها:
🔸
۱۵ حفار غیرمجاز دستگیر شدند.
🔸
بیش از ۲ تُن سنگ معدنی طلا کشف شد.
🔸
یک وانت نیسان و ۸ موتورسیکلت توقیف شد.
🔸
۳ موتور برق، ۲ دژبر و یک بالابر نیز توقیف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/farsna/455816" target="_blank">📅 11:12 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455815">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OrgHHIiX0YXm6padaQc5gdkPaMBdi3DrOqZLAXo8ctILJUvD2suQn-f1Y7fQsRFEQn6fu3X0V1NMKQqjuq5SZLOs3dUUb2jyk9xrCkMn02zChSWWgsJcxx96hFHWOAKyKQWmYAqSN4uM7CuI6QT-AMoFnf7VkiHJEpspAPlmiGpSP4iiEWkNXNzYv78wCBh5vC_g9o6wYFmhZFGOuTL5FHW40bZbEVMNeSzjW7r3WCSDWcoSD-cgHSBw3cfA3sSproAvvSeyj9hpSmQ-D_PMHyAPYE9ePbMo3lSVY2VL6U9jBxGCR-narMF0gQH0ln84c9x6qIx7ylqdnNzCQMJMyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚙️
گام موثر بانک صادرات ایران در حمایت از اشتغال/ اعطای تسهیلات به بخش صنعت ۷۲ درصد رشد کرد
🔹
بانک صادرات ایران با اعطای بیش از ۷۲۰ هزار میلیارد ریال تسهیلات به بخش صنعت در پایان بهار ۱۴۰۵، به نقش‌آفرینی موثر در حمایت از واحدهای تولیدی و افزایش اشتغال پرداخت.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/farsna/455815" target="_blank">📅 11:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455814">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ioLQsq9fQf7fMLShzVy2ZO7_FFrSyoUkGhVsdN6sumyHUve0P1x7Lxz7M5Ik3saZC4CJQUhmTuYFfs2zLI6RYGmwbZfkRRdeDS8PTRzaIkWuVFBepLb_3GD5hx9yhzJ9QpcL1D4VzjufrUisgdIptOqoRfkrYUsZpMY690N7zpZD46d_1SkYvregAgbyFg0YIyJ7Sr6eiurThszVMOchC6FO5R9-4G9Yo6LoAhqYVwT6BGHfigs1VsqKJ2ZCcjHF62oWxaD1H8JkcIXpuuLCdvuFkdDS7bhRLtTD5Dn-eAIwcVEk8MHJFXFgYW1cErsyQJrooQeZGOfB7MU_xO5k2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵ فروشگاه آنلاین مذهبی که ارزش یک‌بار دیدن را دارند
۱.
فروشگاه موکب‌آرت
۲.
فروشگاه پوشاک معراج
۳.
فروشگاه ربیع
۴.
فروشگاه ماهد
۵.
فروشگاه مغیث
اگر به دنبال تجربه‌ای متفاوت در خرید محصولات فرهنگی، مذهبی و ایرانی هستید،
این ۵ مجموعه
می‌توانند نقطه شروع خوبی برای شما باشند.</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/farsna/455814" target="_blank">📅 11:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455813">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/farsna/455813" target="_blank">📅 11:09 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455812">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64cf91335c.mp4?token=ltAVCHAXbkBGf6QeVH0aCTZqU2OwkxqWNynuJf85sfhvMDoBZiQ6DAWmdqcZYhwkhhML04kiYsjRJ65uj4P4QJc1C7cxAU56srYWrqX32C9FU-SfUSdN7x5PY9Hnkn9alNt3V_0m2SQUtI01P9gDIYIwRiWl2NUVtqsgtUspdc-yJ-f3lHcLgDQgLUb4foqVDJ6TZGqjTNdILvuQ-tFtuRyyFmEi--iezJVSrsGORpbcABSh4aH86jASnn-MgMWIy_GWh_uRoBXI87dWJ5F9d_O6PDWQA5U6fLoXCJdVoq14mKVruvoyMcija5qb5bgpLmgIMiLmL9JE7WCjirEcpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64cf91335c.mp4?token=ltAVCHAXbkBGf6QeVH0aCTZqU2OwkxqWNynuJf85sfhvMDoBZiQ6DAWmdqcZYhwkhhML04kiYsjRJ65uj4P4QJc1C7cxAU56srYWrqX32C9FU-SfUSdN7x5PY9Hnkn9alNt3V_0m2SQUtI01P9gDIYIwRiWl2NUVtqsgtUspdc-yJ-f3lHcLgDQgLUb4foqVDJ6TZGqjTNdILvuQ-tFtuRyyFmEi--iezJVSrsGORpbcABSh4aH86jASnn-MgMWIy_GWh_uRoBXI87dWJ5F9d_O6PDWQA5U6fLoXCJdVoq14mKVruvoyMcija5qb5bgpLmgIMiLmL9JE7WCjirEcpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تاریکی تاراگونای اسپانیا در لحظهٔ خورشیدگرفتگی کامل
@Farsna</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/farsna/455812" target="_blank">📅 10:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455811">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CF-4M0ieQYqjfm-_DW2CBNcwFNz0e65NuEsg8wX34Mi7L-5OWA7sFWvN_m8VKX5mJOYRAfx8U_XTi7qHuRLco6TZ78RCm6epffQld3abQkKZ7062nJ7emUzEnfelIMCCWlmct5s1u9dsnjFqVGa9s96PV143iGPVKEAgONQymsQ5XpI-xipzVt7EbsJOmkCtfRJY53Ae1847v6FJmP2B8cErNc6krpyDYxKHjPWq4QHV4veEKQGFswHEBPBy3CCkKFdgCPXsXfYgXoscrcpGNECY4lvh8Lv4PCQshzxX3wwBJq_mOV4J22-5FcWhMdcntScF17bjvemkXOBIpqOHVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الزیدی: عراق پایگاه تجاوز به همسایگان نمی‌شود
🔹
نخست‌وزیر و فرمانده کل نیروهای مسلح عراق در بازدید شبانه از مرکز عملیات پدافند هوایی، با تاکید بر نقش محوری عراق در امنیت منطقه، اعلام کرد که خاک و حریم هوایی این کشور هرگز پایگاه تجاوز به همسایگان نخواهد بود.
🔹
علی فالح الزیدی همچنین بر تأمین تمامی نیازمندی‌های پدافند هوایی، ارتقای سطح رزمی و فناوری، و فراهم‌سازی مقدمات ایجاد سامانه‌ای پیشرفته برای حفاظت از حریم هوایی عراق تاکید کرد و گفت: «آسمان و حاکمیت عراق، نمادی است که اجازه نخواهیم داد حریم آن نقض شود یا امنیت آن از سوی هر قدرتی مورد تعرض قرار گیرد».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/farsna/455811" target="_blank">📅 10:44 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455810">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b31a9e4389.mp4?token=s50FX8gimS6_u-c5nNJ03ircAFV4fUMFSDhwga1MDnvZlIZiFTKezhtvo0s9wR_SNonb-eBQILwSpgRiAWGPOMziBkruae6ESnP5vsccFkpgp3o5x7IINgifbbfHXgVL8BMP6V6vOxpvi3BUXPw9woSAGVbDYXnjlTujcUYU5HfNw4_-jJUv2yPUNNi5FmBi6vVu4DjFF9MdzKUJqTWj7QDj9dt5bwlPX1BnQE3j2myLtVTWhrTdrrLfNdHwCBUCzOZVuNVZwGDXH7azXFjZxT3GcpqEanTwyMgMTyjKs7CykVJvzIzbjpHySi10e7pg6L8FYSN_tsh8bxVvv3tc6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b31a9e4389.mp4?token=s50FX8gimS6_u-c5nNJ03ircAFV4fUMFSDhwga1MDnvZlIZiFTKezhtvo0s9wR_SNonb-eBQILwSpgRiAWGPOMziBkruae6ESnP5vsccFkpgp3o5x7IINgifbbfHXgVL8BMP6V6vOxpvi3BUXPw9woSAGVbDYXnjlTujcUYU5HfNw4_-jJUv2yPUNNi5FmBi6vVu4DjFF9MdzKUJqTWj7QDj9dt5bwlPX1BnQE3j2myLtVTWhrTdrrLfNdHwCBUCzOZVuNVZwGDXH7azXFjZxT3GcpqEanTwyMgMTyjKs7CykVJvzIzbjpHySi10e7pg6L8FYSN_tsh8bxVvv3tc6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دستهٔ عزاداری خادمان و زائران در حرم بانوی کرامت برگزار شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/farsna/455810" target="_blank">📅 10:32 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455809">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMEMMueWHCsniNVlac-Qc87Clzzyv43_MQAyWoSf8Nki4bFZW0_vOMygPb6Bf55ygZKCZwo4CaLxEeKKSii-Deb6PFPhhhvtg7FNfbuBxASlLDRQHO63Rco9OPgAh5_gIagPuhbvwR8gp3IyccvfkGcgK01w4wQe3A3x02yEhhuXbDirwR8xIU_DUrLy0R757mlammIXX44msu12DJfVGBtbDmoa5Ifbj1EW1fVe-fkCmsS0KXFQcU-kSbaYs39L_04EhuRmkO3XcEmfR4BXGpbP5fymyc5-YnmNNhQL-ykVwrH4E79HxSsx3zZ-XSAF4ARwUnpDu57cTw5RcoJa4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان بسیج: آمریکایی‌ها قدرت انقلاب اسلامی را در مراسم تشییع رهبر شهید مشاهده کردند
🔹
حجت‌الاسلام طائب: بعد از مراسم تشییع رهبر شهید، دشمنان متوجه شدند که محبوب‌بودن یک فرد در بین ملتش و ملت‌های منطقه را نمی‌توانند با هیچ قاعده‌ای محاسبه کنند. این محبوبیت برای جهان به خوبی به نمایش گذاشته شد.
🔹
آن‌ها برای این‌که این قاعده‌ها را به‌هم بزنند دوباره یک جنگ دیگری در تنگهٔ هرمز راه انداختند و دنبال تعرض جدیدی بودند اما به لطف خدا آمریکایی‌هایی که اعلام می‌کنند ایرانی‌ها نه نیروی هوایی دارد نه نیروی دریایی، بازهم با شکست مواجه شدند.
🔹
امروز می‌بینید که تنگهٔ هرمز تحت مدیریت و کنترل جمهوری اسلامی ایران قرار دارد و کشور ما در کمال امنیت به مسیر خودش ادامه می‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/455809" target="_blank">📅 10:24 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455808">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00c994b8a7.mp4?token=MxZaeFIflQSjMLaUauVu5PxT4Sg3xv0jTrffIhaetvl9h3uo3tN9rh-D0Hvbgssum5PnDZKHSQ3BET1dcvsPE94lAo4bR-bB7HlEL7_VyJA59cdhdYPnVXP69agLlYpeEP4J1uqPDo1oW8J-W5QAUoEgVN_SqtRCyofxM-2SGP7F6Hd0hG1-fEzK2j1dDSYxLyQ4fs-Mp0YS0PKeOkCnAQwRYD7KQKTRR7rJB4tmE3JyWfL35FrE0yIT1wiVmZlRXYvi4vJtt9hfx_c5yC1dv5joPt4u19qfo8XUDXqEMC_N3j-_LK2OSH4cy7l7rMlbXabCvQON74gZb_huCGCMgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00c994b8a7.mp4?token=MxZaeFIflQSjMLaUauVu5PxT4Sg3xv0jTrffIhaetvl9h3uo3tN9rh-D0Hvbgssum5PnDZKHSQ3BET1dcvsPE94lAo4bR-bB7HlEL7_VyJA59cdhdYPnVXP69agLlYpeEP4J1uqPDo1oW8J-W5QAUoEgVN_SqtRCyofxM-2SGP7F6Hd0hG1-fEzK2j1dDSYxLyQ4fs-Mp0YS0PKeOkCnAQwRYD7KQKTRR7rJB4tmE3JyWfL35FrE0yIT1wiVmZlRXYvi4vJtt9hfx_c5yC1dv5joPt4u19qfo8XUDXqEMC_N3j-_LK2OSH4cy7l7rMlbXabCvQON74gZb_huCGCMgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سقوط بالگرد نظامی در تگزاس؛ هر ۲ خلبان کشته شدند
🔹
یک بالگرد تهاجمی ارتش آمریکا در مزرعه‌ای در مرکز تگزاس سقوط کرد و آتش گرفت که در این حادثه هر ۲ خلبان کشته شدند و ساکنان اطراف منطقه تخلیه شدند.
@Farsna</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/farsna/455808" target="_blank">📅 10:16 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455807">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/145f4dc47b.mp4?token=J8qLlVobOIFcS255WWX3Ofob1TeIZOgrO1ukCPPjikJaz0zy7e2_bdacOY_xFkiI7oKLeaJQk5duRzjt3H8wKuVp3_DmV5egfIRLV1AqZPV-yGFEE6N-FU0pRM_XVM4w3dykYThyHZ12V6yMjmLpRSaPr8PJukkBJBvEJUB4SjbdZZ3KpZOmCaYKxpYOPNQ6hBNP-_8_OqvL6K2CrpCaKxAgEKhESikYbClB1HvpQ_FLksOzZEFLvFnIgggzv_um8BVDKZLHsdLjjXUITsvYJEbPnSGUohr1Qs17UEXLFR6ZhF7zVhEj-eLzouvPPsYUXHhV-6JE3V_fMt2LZXlN1YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/145f4dc47b.mp4?token=J8qLlVobOIFcS255WWX3Ofob1TeIZOgrO1ukCPPjikJaz0zy7e2_bdacOY_xFkiI7oKLeaJQk5duRzjt3H8wKuVp3_DmV5egfIRLV1AqZPV-yGFEE6N-FU0pRM_XVM4w3dykYThyHZ12V6yMjmLpRSaPr8PJukkBJBvEJUB4SjbdZZ3KpZOmCaYKxpYOPNQ6hBNP-_8_OqvL6K2CrpCaKxAgEKhESikYbClB1HvpQ_FLksOzZEFLvFnIgggzv_um8BVDKZLHsdLjjXUITsvYJEbPnSGUohr1Qs17UEXLFR6ZhF7zVhEj-eLzouvPPsYUXHhV-6JE3V_fMt2LZXlN1YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اشک و مقتل‌خوانی آیت‌الله علم‌الهدی در روز شهادت امام رضا(ع)
@Farsna</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/farsna/455807" target="_blank">📅 10:09 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455806">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
منابع عربی از یورش نیروهای اشغالگر اسرائیلی به روستای قصره در منطقهٔ نابلس خبر می‌دهند
@Farsna</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/455806" target="_blank">📅 09:52 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455805">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pUYxvEcW4A-3k8zlWzYxCepwBI_KiuiFhbDnzNPlbOWNTYToCuxl1y5f2tOkaC_2ao9GljO1zRBN73ay43p98aF6xkugYgIRPqdhQagzEOCfwiSSCkKZ7t3ZRBvE8v3nxWDCYtGArIDEyGjIdDXxdNRwo44xQa3610p8NG8qVxZntAc7eNP2yIXmHoFBIjG-rnIhssMeZKBNLVaeWEWzUhsvfXMF3Gq6YyFRoZbLy-NHVzK4fWXzSYRcDILQBva0AiCJcNfpn86HeMiIODkT1wLSVhLrGuiZlHtcjYYM0YEHAdqA90YSxC-wa0VzEBklgH5AgKFRlW5tTYQUEDCb8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار رئیس سازمان بسیج با آیت‌الله سبحانی
🔹
صبح امروز هم‌زمان با سالروز شهادت امام رضا(ع) حجت‌الاسلام حسین طائب رئیس سازمان بسیج مستضعفین با آیت‌الله سبحانی دیدار و گفتگو کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/455805" target="_blank">📅 09:46 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455804">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/661f970a60.mp4?token=HXv1A8ihibIRXUDliiOG-sEC7-2IudI9JvwwWP5SBrYsRzXnqRVofLSyBT7r5EKsB0XO-RwTrmTY9HxCLreVlASw16U0eQ8kv3zBbUwxdsUl6mQJ_J5f6ARcFh98tmIS_Y853Z9pJMH84Ufe0gEka4jJ-tPnh1zfuJn4wSLmfp1T9L9k8Y2WpCo1mfOZ1WdYDdq3m6240Uc5M6rWl_IHT3MeO1egmFDv64g9w118ErdfiAaBdtT4sF_Tk2D61CkK8dReZ4c28E4OdSJMNBfpR4oQCbkMPCGfsr630PhJDeytnISCeM7pWipVJZ4eoqwiCFIiK5UiWB5xQqD4vqOagQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/661f970a60.mp4?token=HXv1A8ihibIRXUDliiOG-sEC7-2IudI9JvwwWP5SBrYsRzXnqRVofLSyBT7r5EKsB0XO-RwTrmTY9HxCLreVlASw16U0eQ8kv3zBbUwxdsUl6mQJ_J5f6ARcFh98tmIS_Y853Z9pJMH84Ufe0gEka4jJ-tPnh1zfuJn4wSLmfp1T9L9k8Y2WpCo1mfOZ1WdYDdq3m6240Uc5M6rWl_IHT3MeO1egmFDv64g9w118ErdfiAaBdtT4sF_Tk2D61CkK8dReZ4c28E4OdSJMNBfpR4oQCbkMPCGfsr630PhJDeytnISCeM7pWipVJZ4eoqwiCFIiK5UiWB5xQqD4vqOagQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زنجیرزنی هیئت‌های یزدی در جوار حرم‌رضوی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/455804" target="_blank">📅 09:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455803">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83b215ea36.mp4?token=M_TelJ5S3mIg8ZMz_2m2yGYG5Sz5QOTltKgQoNNOIulDGUWeCXcizXW7Aqy5IsegbQaUB-bf6SmDBWony28zP66LKa5HWGGaGMjmiFghzgwV_0bMvGYsWdRiCSFVFuFBvNlioVGH3bOS2bWTkyEoiF3bBnOvI-c2G2s7Z6C5ifwdDxbPFOXllYKOlv7UoY1l-p16_WbHrKDSxh9G_2zQ7Pbu4qWavn2dNZBKj98FjZE-D6eP52VERFGBtZfHzIo8S-z-52jqSOpqBfAXDD8BbwuS5fdP3HPU97kTX9vYCXE4evqKH8zM3X3W_cCYfKQQ7iCYKsBZUschuzYZP43Vyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83b215ea36.mp4?token=M_TelJ5S3mIg8ZMz_2m2yGYG5Sz5QOTltKgQoNNOIulDGUWeCXcizXW7Aqy5IsegbQaUB-bf6SmDBWony28zP66LKa5HWGGaGMjmiFghzgwV_0bMvGYsWdRiCSFVFuFBvNlioVGH3bOS2bWTkyEoiF3bBnOvI-c2G2s7Z6C5ifwdDxbPFOXllYKOlv7UoY1l-p16_WbHrKDSxh9G_2zQ7Pbu4qWavn2dNZBKj98FjZE-D6eP52VERFGBtZfHzIo8S-z-52jqSOpqBfAXDD8BbwuS5fdP3HPU97kTX9vYCXE4evqKH8zM3X3W_cCYfKQQ7iCYKsBZUschuzYZP43Vyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: گرما تا یکشنبه در بیشتر مناطق کشور ماندگار است
@Farsna</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/farsna/455803" target="_blank">📅 09:37 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455802">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/444b4437d9.mp4?token=RdBn7YoDp6bC6F1eCI16piQ5JMPVGsqDLa2OJzdKY8dpY5UuhJJ3mLKI4ktxC6SeUyITNDKodl6enQSl5CnaZ9dthUGrzIy90OhNP02W42thS_nde8c8z5V3nReKGk_N4qHpiALsXWIxEWyINvRU0xYWUAD7bVqWXBAVlK9tZ2CymiMS5jUr0yXqx1y0LfT4qxPboKs-RbkVg9o9ynZI7JF1tTvJFUGXiqRlNUgSpUUTz5LKG1k19HNbAYaapDkHHpdGQItcE49eZqdG4mhq8j0tfhn9MHDFZF299fhnI-mHCsp8vfhPPxW9a-ONvb29wd4OiDgc51kagz99fkRVKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/444b4437d9.mp4?token=RdBn7YoDp6bC6F1eCI16piQ5JMPVGsqDLa2OJzdKY8dpY5UuhJJ3mLKI4ktxC6SeUyITNDKodl6enQSl5CnaZ9dthUGrzIy90OhNP02W42thS_nde8c8z5V3nReKGk_N4qHpiALsXWIxEWyINvRU0xYWUAD7bVqWXBAVlK9tZ2CymiMS5jUr0yXqx1y0LfT4qxPboKs-RbkVg9o9ynZI7JF1tTvJFUGXiqRlNUgSpUUTz5LKG1k19HNbAYaapDkHHpdGQItcE49eZqdG4mhq8j0tfhn9MHDFZF299fhnI-mHCsp8vfhPPxW9a-ONvb29wd4OiDgc51kagz99fkRVKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ویژه‌برنامهٔ سالروز شهادت امام رضا(ع) در حرم رضوی
@Farsna</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/455802" target="_blank">📅 09:31 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455801">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
زلزلهٔ ۵.۴ ریشتری کشمیر پاکستان را لرزاند
🔹
مرکز لرزه‌نگاری اروپا-مدیترانه (EMSC) اعلام کرد که زمین‌لرزه‌ای به بزرگی ۵.۴ ریشتر، کشمیر تحت کنترل پاکستان را به لرزه درآورده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/455801" target="_blank">📅 09:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455800">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnM0IFbx4N5SgHMHhIZUvomZS-zOdYBgNscU1WL_QbvoB4oEInqJYtTt7gtumWglN5oEh3xORj4P8L5_TJQvlgyvMh46a_oPoNF4_dTruMQHvjsWXpcwAbWECy0iEI-a5WUFZLVQq6C1tZkRBSfOF_kx_5vrftZSbT4SObeB6W2oR3WLCXefW_caZ8xMUM8nKQAqVa7JH7UlCKnt6yzuK_sscrjMqy1mt3DrXAJkN6X5bx09KQE_wuiNocUE1oScpRTfcmcYOd-kgGxcqJ4DATWNOSX5tyWsa7l71sDpG723Ej9KGvf0FYdw9Tmq3FKYYFfd2JBm5oXbZbj8-10Yxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیرانوند با ۹ طلا رکورد آسیا و جهان را شکست
🔹
محمدجواد بیرانوند در یک مسابقه فراموش نشدنی که رکورد آسیا و جهان را شکست، مدال های طلای یکضرب، دوضرب و مجموع نوجوانان و جوانان آسیا و آسیای میانه در دسته ۷۵ کیلوگرم را تصاحب کرد.
🔹
بیرانوند با مهار وزنه ۱۶۶ کیلوگرمی…</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/455800" target="_blank">📅 09:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455799">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3i3-XAFio9bMxxFYY4h_5xdMVE3UtS4trVVOz15unl_BhJ9eIr7_iyZpiWT7ml5p7Z5Un6OInkYjJScTUw3y3h-dXVIJ1X8jJwBFU0nEO-FlNsGFMx-PS9pH1zEeFLKGu9jL52PI73eAFbA7aK5iWkeozceOY4ll7MtReXdzuakg-f1czqiqllq9k0d55-7IdcevGg8ppBkyi_zlUfdtgz5yU7sQRYmwCi_30V-mSyVSm-KCzgJJgYU6Rf2jE70O7DIk75TL_iCj8ANeWkpX3st9PPFLZthX7x3S3Af9xSCbAhpwA7O5S0zX_701xnm6By3L6jywLJv--YpuIrKdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز هم صدای گلوله در مدرسه آمریکا؛ این بار دستشویی دبیرستان
🔹
مقام‌های امنیتی ایالت جورجیا آمریکا اعلام کردند که یک دانش‌آموز ۱۴ ساله در سرویس بهداشتی مدرسه به یک دانش‌آموز دیگر تیراندازی کرد و سپس توسط پلیس دستگیر شد.
🔹
بر اساس گزارش اداره کلانتری شهرستان هیوستون، یک دانش‌آموز بر اثر شلیک گلوله مجروح و برای مداوا به بیمارستانی محلی منتقل شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/455799" target="_blank">📅 09:05 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455798">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🎥
اجتماع خون‌خواهی گلستانی‌ها در حرم مطهر رضوی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/455798" target="_blank">📅 08:52 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455797">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf5c9795e3.mp4?token=EkpD4CVj74ScGeu2mCR3dXKJ_PbFVwoS0st6ChRm-gu7TMgg9id6axB7W7fBaBRM8cunrJYVaGgQ_UCvEfpTWFauH5n3UWmv-CPmeLo0oz_YLiVXGKbm911nKGk4JyyLrmJTzdJC5bAfFgjLzvPzsaAzpsJSQb5OhfVQtOKnl3Hp6N0fWNDPUJUzQnb1GlxPWa07x7Ky97CRYlQ4zPmYP7EaqspXBHeU0ihfulpj0xxf7JD0Md9SZCEj5JJ4zUzwtQDvSTS9lAWXA9srczU0eF9ClLN0kglNMt8TxX8o9BaZRbEpTWEAxT3jgJFSbe02snm6jKWumxlQ0zAtsdWlX1QZUO4is8aAUQV13Q04w1pliBHqhx4C5Vq5WAGeNx-DP6k6O3mTp12n6kXhBVpl4M3yZr8juJqkSeED9YqMgX8yVC9reXD2ZGR6lAAgmAEoLfMeqjIP9ni3wUAi8ZkCXt-9NArDO9seXqUw_arW4wiI2e_I7TYLctCVwI6eG0gfWxu2hoAIUyE4cU6uNYujo0ZXB1JbxqCkmjG4-qEcOz9MSsGMwg_vXdT8lbHDhsgQFS2-4wUAVvbA4K-5jguHYYj46LlsSGyfx5AxpqzJ839xkTuEVvG6touC0AA3ZRT-UwQ3W_ded-SRPWchAXnvtl4_p8J0KUG3jfoFzxihQ4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf5c9795e3.mp4?token=EkpD4CVj74ScGeu2mCR3dXKJ_PbFVwoS0st6ChRm-gu7TMgg9id6axB7W7fBaBRM8cunrJYVaGgQ_UCvEfpTWFauH5n3UWmv-CPmeLo0oz_YLiVXGKbm911nKGk4JyyLrmJTzdJC5bAfFgjLzvPzsaAzpsJSQb5OhfVQtOKnl3Hp6N0fWNDPUJUzQnb1GlxPWa07x7Ky97CRYlQ4zPmYP7EaqspXBHeU0ihfulpj0xxf7JD0Md9SZCEj5JJ4zUzwtQDvSTS9lAWXA9srczU0eF9ClLN0kglNMt8TxX8o9BaZRbEpTWEAxT3jgJFSbe02snm6jKWumxlQ0zAtsdWlX1QZUO4is8aAUQV13Q04w1pliBHqhx4C5Vq5WAGeNx-DP6k6O3mTp12n6kXhBVpl4M3yZr8juJqkSeED9YqMgX8yVC9reXD2ZGR6lAAgmAEoLfMeqjIP9ni3wUAi8ZkCXt-9NArDO9seXqUw_arW4wiI2e_I7TYLctCVwI6eG0gfWxu2hoAIUyE4cU6uNYujo0ZXB1JbxqCkmjG4-qEcOz9MSsGMwg_vXdT8lbHDhsgQFS2-4wUAVvbA4K-5jguHYYj46LlsSGyfx5AxpqzJ839xkTuEVvG6touC0AA3ZRT-UwQ3W_ded-SRPWchAXnvtl4_p8J0KUG3jfoFzxihQ4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این رزمنده هنوز در جبهه نگهبانی می‌دهد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/455797" target="_blank">📅 08:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455796">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd14256e04.mp4?token=rQV76zpFU6zuaoaF7Zwf01JcycHfFitD1b0r_FDwBPtZCbp6nQ-l0iK_B125Bhtwi6pU_D-WDmgklNrBLd3qJ8jtVm8LSKDmAZelj8o0iXk4si_YQQciaCpb1J3Uc7kwUiAcOn0ZAsHo_zINhYCZL5eUteqH1IwAaiwVPGvAOen_vzjhupo5JtbF5F9qCn9LvL56GK4n6wRlA9i37bUCEzAyVmlgx28Q7d3J9twZn10lGIzdcMy4zHLlf4Kpb10yVofuoQGTTfMEc0hUgSYQZYpTrO26gGWp0usWobP1a1db9Z_B9cTeTO7qhn9q_cuAFYE0DbKzb9MzwhT1qqyusrTFv9TVcuo-sLvmUAwORwRgENAdaSbkfEcfsf5LasY7Yd21AjLxvL55yqgkev9sgIaewiS8MC9E58JRGuXzVVMlCWnsjAbXho3saNOvqmnbqc9iRKPQzR7okuXaW9Gq5uvatM-xRBdXpkVz9yq-l5VptAm_R9lHMfULAnm9d5m-jBR0N0eVn54jZWDwTZp1HVmw6OioR6klm5Ax5wOv0mkHWr3UtbHlB3rLNQ5V2M_Vu2AEgxOY3JKYh5KVc_ZLkJ-ZXSoAO6CUk3duKF3eG4fq0GmrlDCeeojoSKoXe2OOH9SsP_hWF1elmhDh3HZlbwUaiwgF4N18_-N4RmAzSw4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd14256e04.mp4?token=rQV76zpFU6zuaoaF7Zwf01JcycHfFitD1b0r_FDwBPtZCbp6nQ-l0iK_B125Bhtwi6pU_D-WDmgklNrBLd3qJ8jtVm8LSKDmAZelj8o0iXk4si_YQQciaCpb1J3Uc7kwUiAcOn0ZAsHo_zINhYCZL5eUteqH1IwAaiwVPGvAOen_vzjhupo5JtbF5F9qCn9LvL56GK4n6wRlA9i37bUCEzAyVmlgx28Q7d3J9twZn10lGIzdcMy4zHLlf4Kpb10yVofuoQGTTfMEc0hUgSYQZYpTrO26gGWp0usWobP1a1db9Z_B9cTeTO7qhn9q_cuAFYE0DbKzb9MzwhT1qqyusrTFv9TVcuo-sLvmUAwORwRgENAdaSbkfEcfsf5LasY7Yd21AjLxvL55yqgkev9sgIaewiS8MC9E58JRGuXzVVMlCWnsjAbXho3saNOvqmnbqc9iRKPQzR7okuXaW9Gq5uvatM-xRBdXpkVz9yq-l5VptAm_R9lHMfULAnm9d5m-jBR0N0eVn54jZWDwTZp1HVmw6OioR6klm5Ax5wOv0mkHWr3UtbHlB3rLNQ5V2M_Vu2AEgxOY3JKYh5KVc_ZLkJ-ZXSoAO6CUk3duKF3eG4fq0GmrlDCeeojoSKoXe2OOH9SsP_hWF1elmhDh3HZlbwUaiwgF4N18_-N4RmAzSw4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چهارپایه‌خوانی حسین ستوده در جمع زائران عزادار حرم رضوی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/455796" target="_blank">📅 08:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455795">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">پشت صحنهٔ خودکفایی دفاعی محققان ایرانی از زبان رئیس جهاددانشگاهی
🔹
رئیس جهاددانشگاهی: بخشی از این دستاوردها حاصل تلاش جوانانی بود که حتی برخی از آنها هنوز تحصیلات دانشگاهی خود را به پایان نرسانده بودند.
🔹
در جهاددانشگاهی صنعتی شریف، دوستان ما کارهای بسیار مهمی انجام دادند. یکی از این اقدامات مربوط به هواپیماهای F5 بود.
🔹
پس از خروج آمریکایی‌ها، برخی تجهیزات و قطعات حساس این هواپیماها از کشور خارج شده بود و هواپیماها با مشکلات جدی مواجه شدند.
🔹
جوانان جهاددانشگاهی صنعتی شریف که بعضاً هنوز تحصیلاتشان را به پایان نرسانده بودند، با استفاده از توان مهندسی معکوس برای بازسازی و فعال‌سازی این تجهیزات اقدام کردند.
🔹
این اقدامات با همکاری جهاد خودکفایی نیروی هوایی انجام شد و توانست بخشی از تجهیزات مورد نیاز را برای استفاده در دوران جنگ تحمیلی و دفاع مقدس آماده کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/455795" target="_blank">📅 08:20 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455794">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201d701596.mp4?token=f4vSObYot64_EPGYVgD-ML_ttCmJxMfmqRUxOoNyX6QqnlfcUKKIACCtqvUQQId6j69U88s1xoBG3KtemBEb-g1N3VG4NsDFRZq-q07dgGxJWn1SZucs4f3s0QPr1HxCyLZH7_PR41U90ONLJCejHlbGxnIPUYWaDGswPBQFAJU8rZn_HWWuwPR4ePIiJTuaQp4DCUpVTN8XLQfYlff83buO06NccCZJwzDTNUrp-nffgos_ruwUSks24BKQZdajgalj7p7N73ZG95ujP1gMQEQZQ9IbeMU_lCXk80QE7b7nz1OsPkkNGkGST1jGJ8ZbtzfitL9ZOKE5oTaMwp05sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201d701596.mp4?token=f4vSObYot64_EPGYVgD-ML_ttCmJxMfmqRUxOoNyX6QqnlfcUKKIACCtqvUQQId6j69U88s1xoBG3KtemBEb-g1N3VG4NsDFRZq-q07dgGxJWn1SZucs4f3s0QPr1HxCyLZH7_PR41U90ONLJCejHlbGxnIPUYWaDGswPBQFAJU8rZn_HWWuwPR4ePIiJTuaQp4DCUpVTN8XLQfYlff83buO06NccCZJwzDTNUrp-nffgos_ruwUSks24BKQZdajgalj7p7N73ZG95ujP1gMQEQZQ9IbeMU_lCXk80QE7b7nz1OsPkkNGkGST1jGJ8ZbtzfitL9ZOKE5oTaMwp05sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشییع نمادین تابوت امام رضا(ع) توسط خادمیاران رضوی در کوهبنان
کرمان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/455794" target="_blank">📅 08:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455793">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/105c882a85.mp4?token=el6_0lG3ZHf4M1hUs2GS2r1F6FI1ghzZ2dnmF1NCF9ii9RXOkodBFeXSC-1RgCVT6iDycFDyYU2wE2tIq_Rh1exrU04Jh0CtzLoOsgT0KDtB4-5HCOQ8o6MtNTO9AliRby5dufYKX71zE3itcie6l2T_ijQJ6PaAruc4DyWptzze21yYCHiAHQHBT5FEtCp2RyZMdBw5wuUF4EYbbXFcgpYAbaUwTSoSn2oEGmhTtsIYducSC7APP0Z3pSEDBpYQl9IdFyjcgvYO2DToDYDDky0yas7Xghxcasm67udpRQ4kaSW3OZxmlkMRZmNXmRPJWjTFVg2A9DgB4IhQvBrD9AWm4nqnMYIKpf_pk5m6qdRhHi3_fAkkAHP3erUcC9bka57kPTW2smGgT9QLLhjzC85u1gI1YpEmPOuz8JtqydA7pPOev3-WQgK7ZmdlC4F5kFAfGWuQp-zdx5Ra_j2zHWNq_Ac3w7qm9GhlMj5poMWtzRnzFO-5Rvk_NL1uoNPRCJE57ZPZWvWTzo2_MB-90ehR3gjRqew_p9OP8Iufu0e8YHcoSRK7OI2tOd-m_OSTvNKTtV0MYYGuEOGeWOAFUbq4O0cMFIH1Jzfsc3C-uLiwVPydOmE9zhx_Y_qr-MCfG_ZxvfG5mubCtDo-nFbAZUNZ4V-ezLuNdjGS88GhUYI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/105c882a85.mp4?token=el6_0lG3ZHf4M1hUs2GS2r1F6FI1ghzZ2dnmF1NCF9ii9RXOkodBFeXSC-1RgCVT6iDycFDyYU2wE2tIq_Rh1exrU04Jh0CtzLoOsgT0KDtB4-5HCOQ8o6MtNTO9AliRby5dufYKX71zE3itcie6l2T_ijQJ6PaAruc4DyWptzze21yYCHiAHQHBT5FEtCp2RyZMdBw5wuUF4EYbbXFcgpYAbaUwTSoSn2oEGmhTtsIYducSC7APP0Z3pSEDBpYQl9IdFyjcgvYO2DToDYDDky0yas7Xghxcasm67udpRQ4kaSW3OZxmlkMRZmNXmRPJWjTFVg2A9DgB4IhQvBrD9AWm4nqnMYIKpf_pk5m6qdRhHi3_fAkkAHP3erUcC9bka57kPTW2smGgT9QLLhjzC85u1gI1YpEmPOuz8JtqydA7pPOev3-WQgK7ZmdlC4F5kFAfGWuQp-zdx5Ra_j2zHWNq_Ac3w7qm9GhlMj5poMWtzRnzFO-5Rvk_NL1uoNPRCJE57ZPZWvWTzo2_MB-90ehR3gjRqew_p9OP8Iufu0e8YHcoSRK7OI2tOd-m_OSTvNKTtV0MYYGuEOGeWOAFUbq4O0cMFIH1Jzfsc3C-uLiwVPydOmE9zhx_Y_qr-MCfG_ZxvfG5mubCtDo-nFbAZUNZ4V-ezLuNdjGS88GhUYI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مداحی باسم کربلایی در نیمه‌شب حرم امام رضا(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/455793" target="_blank">📅 07:44 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455792">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RavycDvN0IFC2uH645wAb74CGP5bi-cIQblnI-2RNDePwXDZLZ9LsaQIWCT4N7xXmg7IdzTLepy_rRh9nDhQkxTZCTggYd-LSuBIvvwX5DXJOUI5NrygDWvnyAKdLegB8IYmQ88e_ULumDGvgvDc55AoGmYcECYzHSmTSUiMcv9CoVT_S0foSDAtKIYrbrHQMHTRVZ76EfuVhVXKK5nnIje44Zn1krIZhe3LlRmZ7nan5n3tXLRZawOo1qGBAerCadDV9Sg9J_qIujOoHmMWKUP8YdBRrl1AJEKnMI7weCEPeXQeSbF-WirFBYBxyKGQsrQtGIs6W0hFMEiqA3crIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: کشورهایی مانند فرانسه باید از موعظه‌کردن جهانیان دربارهٔ «حقوق بشر» و قوانین بین‌المللی دست بردارند
🔹
این کار یک ریاکاری آشکار و شرم‌آور است. حمایت شما از نسل‌کشی اسرائیل در غزه و حملات تجاوزکارانه به ایران، هرگونه برتری اخلاقی را که تصور می‌کردید دارید، از بین برده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/455792" target="_blank">📅 07:38 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455791">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rb2SlndEfn4k9Bz9wvibgWWecZP2yeCKMK7Bm3aP6AgGn3uPNpS4AKeRwB7kcev4mDtp0NmGB0SJiCWBMRQQyXZr5yrw7vDEGNbY-jfL9DPgAbZycVwfAp0Eggw7lXKLIDz1J5_VIXlyfpClAIpfxdpzk3MtUhAjIRiyx8FWQj2qIq6uNsrD1NMNT3DZOgK3RTgz1UJEZDwms47WhqImGxdrJ-59T-BKuwjFOZW9cssgHPctgKE8QGAr4r8rTosEczLTTHmh-Q1HcI-qJT2yiGYLzZvnkCFwXccehgQSnfkvhNTb-WQKD4mjlsf5bu4TK9plcup6jpNAJk9rgIWQmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر رفاه:
کالابرگ مسافران عتبات عالیات و کشور عراق حذف نمی‌شود
⚠️
زائرانی که پیامک اقامت در خارج و لزوم احراز سکونت در داخل کشور دریافت کرده‌اند، چه کنند؟
🔸
کد دستوری: #۱۴۶۳*۵۰۰*
🔸
مراجعه به دفتر پیشخوان دولت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/455791" target="_blank">📅 07:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455790">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDQd8FeYdkIN4zzKjz6FHMRrJjCgh2A_HZaCCH1bRZO598ZKciYqch9QKU6HqWERlZc6mkUmvEhDuVn8sFM4ti8pz3wwqk9dLlzI5T1FzFWLxVUi20RFeHb9FExtSVBBLdIgvcIXvsdPqQx1G8iLxQP6PU4UquOe4QJoTq2xNjPh5Qxx95mO5HJOLTAQ66jpjB7UgoOgML5iKdFjpGY9lAZE49YE4upxS9xHix4RvNy-NeN0V7CONrci7nUQdNyi2Kq4tx-DO8iB0WeOA-A_DFHyaeRmJWRlMpujj7su0yvGOwOAYOJPdm0qX56RK0eg66TEcEfTwCD9YvsaiMeSVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«آقای قاضی» علیه یک عادی‌سازی خطرناک
🔹
با ورود «آقای قاضی» به آنتن تلویزیون، به نوعی فرمول آثار ژانر حقوقی دگرگون و با فرمت متفاوت تجربه‌ای دیگر از سریال‌های حقوقی برای مخاطب عیان شد.
🔹
قسمت اخیر این مجموعه به مسئله تبلیغ مواد مخدر و قبح زدایی از آن در برنامه‌های اینترنتی اشاره کرده است.
🔹
طرح این موضوع در قالب یک درام حقوقی مسئله را از سطح یک هشدار رسانه‌ای فراتر می‌برد. در این روایت موضوع نه صرفا به رفتار یک فرد، بلکه به مجموعه‌ای از عوامل از جمله نوع محتوای منتشرشده، مخاطبان و مسئولیت حقوقی در قبال آن مرتبط می‌شود.
🔹
انتشار بخش‌هایی از آن در شبکه‌های اجتماعی و توجه کاربران به موضوع مطرح‌ شده، نشان داد مسئله تبلیغ مواد مخدر در محتوای اینترنتی، برای بخشی از مخاطبان موضوعی قابل بحث است.
🔹
«آقای قاضی» با قرار دادن این موضوع در چارچوب یک پرونده حقوقی، امکان بررسی همین پرسش‌ها را فراهم کرده است؛ اینکه در مواجهه با محتوایی که ممکن است به عادی ‌شدن یک رفتار پرخطر منجر شود، مسئولیت هر یک از بازیگران این عرصه تا کجا ادامه دارد و قانون در چه نقطه‌ای وارد عمل می‌شود.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/455790" target="_blank">📅 06:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455786">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IBvi8-VzAejB3WWHpBKHDTwI6WTErOL_q6EJluOZORddm7uHsxtV8NQjfHSbJtIIvxAi0BV3eVq7RLrUZ97LW11pHz_M5b6uUBZ0SfA_gQsCu2qsp0gOOauZU13tFzAlLBy3sFPqRWfRivo0SeOMX0XdOve1g8WAZlQyLdrplHnvREuVqhDZu5n91E68Z1vTr4Lqr7doxy1rknsQ1j91V3YeD0Jm9AkphSgqG-4Anf3lULOtEX9YlwgzSSBUH7TIA-9eRC3VHPPvR7oDOxPZvQBDd3w3kY8ciGPsBfjeS2tBSb57nbaRSdvlp4dQEZT6SiRB1pKTeqpx3N2NBhUDyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X6XQetQ9wvP8I1P6EbTf4WnHmOT0Y-6k6ij9hqkytwIQciDv3WSFK7SDgGYnFRbXPtxBO9EdEFRcx5NNuIVbMf407gbSzokPZnjxNLOaLfdSi-tQ5mrQaH2qY-q1vWgIDTKrcYrHwYCBHErw91E-SWK8NLfVSnaJTo8ZCZxUs7XLOYCLl5CXLCsPT138UAFkG2w50sXwI0U3jomHpUr8UH3R44lQaE0HH3TNJG81tC2DgI_ny4qDWSb2yGx34VM4qyObnmHa3-G2B51bMlzoJPp7NLa73Ju61EClEAE4iRrj2xBVofsMp6-PDIW4IQj2HPTKHuN0kpGhxE7YgW3sPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QzqDfsweXbhbqXG6G7GdZ37L5jkJ9gTtplhCTrrtp3ovusL38CIWSsIAx60YF7Rz2R5DoLaZzBC1EnclrU9jKvkBD7Ad6RH6YyfQ5KcrsMX8KAwzUdv0M6e8M34ojM9YhCxfNmmT9aJ3gc_dFVSO4MmjT08vNMCnPD7RmVlFSDr6t08lLgIyGjzHQ7t5xZ0e64aUps-Dyj1B9vEQjMHbIWYhf9T_6utAsv75aeA4j6I0bIeSHcAVMtP0A-NUW6ZUj4fk9ZHnS3NdLQQtAHbIDaxVtSjw2mxaWV9Bc3QAoVA6-TOxHt3jm37RAHaHhx3k8IwTmCBKysFTa8O7yqM8Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SEUj3N5jYVLu0gVOXSbMpNct_Lq54HTt78Svae6w7PtyCR8cSkBBEI4cfma04aIvISivpPk34dyijPd8iRP-042rFXft2SVU1yb6w11BxSN_4LRCt1a0f4kCRd_CQNtQ9V-ADIsPhESZ9E01JfFWltfBB0Jy1JSU19eMOAkRs4483Bt9BCaZRZ419M3RyR5HVGwFWB0hsk7Vf7w4fjL-SJut6dv3k7armhepf-eplyukdqrlBcNyhlF7SXom6UYLT5Y-7pBU1S4qbqr7gdXpLkyauYTMvyRv-2TjAiExfrm-BDtE5rsuzp7T9jFkaxZHUpNcJL9mdL377T249tFgVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
زائران پیادهٔ امام رضا(ع) در راه مشهد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/455786" target="_blank">📅 05:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455785">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">تماس‌های تبلیغاتی مزاحم و نسخه‌ای که ایران کم دارد
🔹
تماس‌های تبلیغاتی ناخواسته همچنان برای کاربران دردسرساز است؛ فرانسه رضایت قبلی مردم را شرط تماس تبلیغاتی کرده اما در ایران هنوز بار مقابله با این مزاحمت بر دوش مشترک است.
🔹
در فرانسه شرکت‌ها برای تماس تبلیغاتی باید قبل از تماس، رضایت فرد را گرفته باشند. فرد هم هر زمان که بخواهد می‌تواند رضایت خود را پس بگیرد. اگر شرکتی بدون اجازه تماس تبلیغاتی برقرار کند، با جریمۀ سنگینی روبه‌رو می‌شود.
🔹
در ایران هم برای مقابله با تماس‌های تبلیغاتی راه‌هایی وجود دارد. شکایت در سامانۀ ۱۹۵ و در برخی موارد کدهای دستوری اپراتور؛ اما مشکل اینجاست که شکایت همیشه به‌معنای پایان تماس‌ها نیست. ممکن است یک شماره مسدود شود یا دربارۀ آن شکایت ثبت شود، اما مدتی بعد همان تماس از شمارۀ دیگری برقرار شود.
🔹
تجربۀ فرانسه یک تفاوت مهم دارد. در این مدل، شرکت تبلیغاتی باید قبل از تماس، اجازۀ فرد را داشته باشد.
🔹
حالا اگر قرار باشد این رویکرد در ایران هم جدی‌تر دنبال شود، چند موضوع می‌تواند مورد توجه قرار بگیرد؛ شرکت باید بتواند رضایت فرد را اثبات کند، لغو رضایت باید ساده و فوری باشد و برای کسانی که به‌صورت گسترده و تکراری بدون اجازه تماس می‌گیرند، جریمۀ بازدارنده در نظر گرفته شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/455785" target="_blank">📅 05:20 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455784">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">کشف ۱۸۱ قبضه سلاح غیرمجاز در خوزستان
🔹
در اجرای چند عملیات همزمان و مشترک پلیسی، ۱۸۱ قبضه سلاح غیرمجاز شامل ۵۷ قبضه سلاح جنگی و ۱۲۴ قبضه سلاح شکاری غیرمجاز به همراه ۲۶۵۰ فشنگ مربوطه کشف و ضبط شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/455784" target="_blank">📅 04:48 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455780">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/wCW1FJ1lVFnvuKA1NXMLo6LiCfD7Qz1IqWTz3Bp9rtHaeF_G2UOngKo6c_bvL48eZp223r5GRLOp-6D7nSoI623-DYA0JLJgvdEPLjhjousbuJ27Vw9Pl2IF6op1D7ACAPBQJBXBF_kyTGH9Nd7ZWKX9CZD3aZuaSZ5O8-HUaeUIipu75SACa3w9clAKNAi9zBTzl0GsUSh5uKXrhzqfKdidxtQTyQREJzEBpsDMExo74NdmC8_wUC68WU3mF69fRMK_Qora49Rl-1YMP5OSv6nCA359w43rvo2PIa2ra0g-IMj0ftQ06zZmcfbG2iG5SEphndZbCdVDXo3Ilag4cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fbm57Fm0VbFqlYtGawJ7NmXiu4qQ3BoVJcGg7ZNu65dbiKgcX-YtLwq3xBhNOkZU3kRIVL6KYgRg1iJ58tYDjdpyv7dK4D_JSc-SYVXNT7tEYsMiPGaUTjlu-2QwlX02Je8eLZzJ-I7QH55Kd5e1TnD0pGOh-0b3HSR8xe8aoWiDXZIl9X8heQuq-hRtFH1g8fOx8BATim_3jOp-NXfUNnRMhLs0ezq-X0eUN6ogIqKcLGyhF0fPPFVj7k2AHxELMs9kebvrWNX50e6RTxwiNwkLqDs_-0e-6YECsHFX7q49s081NtQ6nHonwA2OAltZLiG-1K6QIuzt02iclHwc0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h_N9OrHR85jwmulJbXEWz32kIx87dqlFvHuoh4NuU6h8DNc-wvE-q38bT8N6uawmbsvlwfTWLRk8EccIDtjhCo3tqxsiYT_p4Q_JcFyFCMZLdlpLSTdLszYL2DinctG3ICuHw3u9mwOip9P_dOvjFok2ujzElzMQdlad4J5LErLivBMgvqibu3TJarKh12ki2bIUIUNR8jdhCuMfLDrMsI2oNsZL7_bdOzG3kDKsdWQlCJOarI5Rhws4tfn1YbGJVEleM2pvMlFc2Ejhup9D8jHibgQYDZivUyKJVML6kisd_8tTxGeBbvXSl-QNUiguPYM3U9xil0zzdziGX3XYig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TzjqNjZlvYMzL786jZIgY929t3CQPOR9l99Le7zxuh5zomceHIqGCVySfQP2PxSvKaFKs_P-S2m56jSu39cvbyLmcid1wfILPUOLGchhnHo-R5hWRPQa02Ny0kf57LEwT6-JN7r7ur0tpAmCmL6VFht8UXNHR7Mf_ValtJT9IFwPjTcmcBiiRc72sj0O-lJIUv9feO8dRvYRH64I7P0HEeNJPQaAOFfa9EqDBt5U6dicyZGRQkKn79y2lXFGHWGmfZY1uGB-OVb74oOKJvQFpLLYWOtqm11LWWCE1P7TtV2Qlxw9KCDQS6q7laEu86eaC0Yb0mFMdRDV5zElvqtz8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اجتماع انتقام‌خواهی کرمانشاهی‌ها مراسم عزاداری شهادت امام رضا(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/455780" target="_blank">📅 04:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455779">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/930bda4916.mp4?token=DdegjDtEUd6D68i7udGnUkEaP9g9sAj6MPiJTEFqKu0yw6ivwxjXM1xZoIHD4QkspLLKMdD4xG7_-0biH1BizVYmnEHOwX7MKj2X4ybHKdqP_dyCfyqvgAYxeJkomaQXRw62QrCeH0vlddrYZsJFvyX3BB_DL0WdFBVqb6olI-zqvgGofbhSmJUBUnSMm7ouf01EY5W40kvCYFcr4J-mh8h7VoTCGzBpVyZDg3c57-DnoDo0FFX4l-D5i6wX01rKYeFLSnCAgvk4wDNRopgnsS0BpQXxiAptTkYOfYqa2VODtM2lL3BaJvbGQiGLtNAyyWWAjfiAh3rm_W0M8JP50XeamqPHaeGRSQn8vvuaKQrSqMK51xkvjee0OguTZdRHtPP-MEFI5eVfBCRRQYm6LWmuFvybaFpL0Ilkjcz7jWJCkn8_3-r4_5xZv_wEHkZ8gq1h9y1ChxGLKhFSPpL7vwmfybUHVGDumnxFJBG9rwCqHhJvKH1rquR_fYJgu8tygYbXAyYJxLFoVyqBjiQqNJoTEmCy9Z0o10KVrT5zUbu-GRPvqQrL_4SNfBnJRhFT-k3AUOAUNi4kChNg_e_Lt9aRsRp4WiyMHda3vG_Jve21jQ8_PysySn6lD9gW8gJyAnwjfXET7TtqEXk8eJPpHc_6VSzHlqd5ODNos3qrdtM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/930bda4916.mp4?token=DdegjDtEUd6D68i7udGnUkEaP9g9sAj6MPiJTEFqKu0yw6ivwxjXM1xZoIHD4QkspLLKMdD4xG7_-0biH1BizVYmnEHOwX7MKj2X4ybHKdqP_dyCfyqvgAYxeJkomaQXRw62QrCeH0vlddrYZsJFvyX3BB_DL0WdFBVqb6olI-zqvgGofbhSmJUBUnSMm7ouf01EY5W40kvCYFcr4J-mh8h7VoTCGzBpVyZDg3c57-DnoDo0FFX4l-D5i6wX01rKYeFLSnCAgvk4wDNRopgnsS0BpQXxiAptTkYOfYqa2VODtM2lL3BaJvbGQiGLtNAyyWWAjfiAh3rm_W0M8JP50XeamqPHaeGRSQn8vvuaKQrSqMK51xkvjee0OguTZdRHtPP-MEFI5eVfBCRRQYm6LWmuFvybaFpL0Ilkjcz7jWJCkn8_3-r4_5xZv_wEHkZ8gq1h9y1ChxGLKhFSPpL7vwmfybUHVGDumnxFJBG9rwCqHhJvKH1rquR_fYJgu8tygYbXAyYJxLFoVyqBjiQqNJoTEmCy9Z0o10KVrT5zUbu-GRPvqQrL_4SNfBnJRhFT-k3AUOAUNi4kChNg_e_Lt9aRsRp4WiyMHda3vG_Jve21jQ8_PysySn6lD9gW8gJyAnwjfXET7TtqEXk8eJPpHc_6VSzHlqd5ODNos3qrdtM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیامبر اکرم(ص): از هم‌نشینی با مردگان بپرهیز!
🎙
آیت‌الله فروغی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/455779" target="_blank">📅 04:05 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455778">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D31QDD9pLu0NxtmolP2cVmkG0Sge7RNU3u3o3ZOxKT28kmazQ_1UPQ3nneAQXWHVD1UA5aiyG-Zd4G2V_mmjQXVOJUxbu9y2csVSWVq0xX22YZu0vSC7_MJxYQCRVlNdnzqL2X4IUtsdwre-vX54tB3e-zRTejRdXn5DdvhLev9TS1GwhvwQ_ecyowd0mVyxi_NxgVSmarXHEwtXelZUrd35DoSdLScxAeCbCc3g1OvGgBZgIc8Yz7-nn4yelgssvFkSPbuyG2093hPjaKENQs4cCBogjvLSn0DXePegNoUJlKgyY5fR1G-6YTwE7oC8AoDO0HOhxjT8KvUUplrLfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای آمریکا درباره تهدیدی که ترامپ را در کامیون غذا مخفی کرد
🔹
یک مقام ارشد آمریکایی بامداد پنجشنبه در مصاحبه با شبکه «اِی‌بی‌سی نیوز» مدعی شد که نفوذ مخفیانه یک گروه ایرانی به ترکیه به همراه موشک‌های دوش‌پرتاب، رئیس جمهور آمریکا را مجبور به تغییر هواپیما کرد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/455778" target="_blank">📅 03:50 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455777">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSfkBBivHq0TOAZTEqO4sQ3DE2lBClGffZ_Z66vbGW6LUlV2eJhzcdl0fC8XY7MgAu4XgmkSViZDjNkyt-iA_cpnLueJIBnGCN8zgQWUNX2jJxFFz2T6G0WnNYHcO7pXXSEEHwWWlFpJ6Eg7xmqTujH0eTsZusEx-OdNbxGhtIwb3l24L_PQq5x-MR8wWCL48OJLP48pz-YCoERkeMeK9LwZ2Nh2LzjnYzB_ytTl9NbxdALRpvwZClaAgAktn3bMEEEdKtcfwI-ygpuCIWdFm1VfpLF87n55EbyAEG43oUSXcS9XhHfmiLZI2va_E-7YgKIeriWrW261k_1btJNykg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا: خروج از عراق تا ۳۰ سپتامبر تکمیل می‌شود
🔹
خبرگزاری آسوشیتدپرس به نقل از یک مقام آمریکایی گزارش داد که آمریکا در مسیر خروج تمام نیروها از عراق تا ۳۰ سپتامبر است، که به حضور نظامی در آنجا از زمان حمله سال ۲۰۰۳ پایان می‌دهد.
🔹
این منبع که نامش فاش نشد، گفت نیروهای امنیتی عراق، پیشمرگه‌ها و نیروهای امنیتی منطقۀ کردستان مبارزه با تروریست‌ها را رهبری خواهند کرد.
🔹
همچنین در این گزارش ادعا شده که همزمان دولت عراق نیز با فشار برای خلع سلاح شبه‌نظامیان حامی ایران روبه‌رو است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/455777" target="_blank">📅 03:25 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455776">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1c2852062.mp4?token=fPxbsuJe84suONwbx2vGV9vOduI02CXJ0ye3AKywdD2ChWrZAWbnHIHgfc0OM_Gx-cIJYobMDlg-9ThzxxIrzc5iWJ-lw6vLrdxixc0Lb_ttg2980zN_mGWis42BqfrZFrnYK86eznAB79iL5z2ooK1PAyvf_3c_3jeMejVDZ9na0j0s2JfVsSk8xHIM6NUyxBshj6D6e8gSEQvPFiBUrA6-m9WEPLTh-zyM3jfEjLQyGJt_9BbcJAwqLShWBN5694xPiozWPDOevY8XLQyS8Hxm5p21_UskBCtoz1-kA_tMf90qeuR-A1ypiDDHSlQf1FqWp-n1pUN_iRyMvFKeVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1c2852062.mp4?token=fPxbsuJe84suONwbx2vGV9vOduI02CXJ0ye3AKywdD2ChWrZAWbnHIHgfc0OM_Gx-cIJYobMDlg-9ThzxxIrzc5iWJ-lw6vLrdxixc0Lb_ttg2980zN_mGWis42BqfrZFrnYK86eznAB79iL5z2ooK1PAyvf_3c_3jeMejVDZ9na0j0s2JfVsSk8xHIM6NUyxBshj6D6e8gSEQvPFiBUrA6-m9WEPLTh-zyM3jfEjLQyGJt_9BbcJAwqLShWBN5694xPiozWPDOevY8XLQyS8Hxm5p21_UskBCtoz1-kA_tMf90qeuR-A1ypiDDHSlQf1FqWp-n1pUN_iRyMvFKeVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجمع شبانۀ دانشجویان مشهدی در جمع زائران امام‌رضا(ع)
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/455776" target="_blank">📅 03:16 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455769">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AfHsBABjOZUAutWZOCZ2ai2KzvsraaNwNUY99mYEysovL-jSG5gQeoON64cvfneoB1Axc6ebbNi2s3KTVrsZNCgcXXwgkNLv1amz4Uzllj6GY_TU51VyU6V1QyxtQR-t-zaunKeHcugPBsl7T5zSMNdDbQflfe8OkqpFkQLxKn6aj6dgZzBAv6bM6nGK37JGnqd7_M02QtfiA-iaaUqaNnOWHXnO6i_A2pYK7EQ37S7lhkg16SQWj25F8meMjyYinTBuV1nJvNaYzACAwb7m2s5f78CvXQ0XfTz_XfwSV-eZMTTm7e8eUuab3lzE1SbwQVMS8xfuYYdhi0TjcSjTMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qhEFWBRf_baBNPUeRNUtcAy_r6KFTHDHrMH_TO1DZggnsfcLwWo1yzKwGkvi5Nq3CDCcr-KI0UIG31-KsR2drrm42M1cNbjSEE8-Y92B3LoHnJaUsqj0Rj313sK91_bihZfvIyX0ebdUFn6lkHZr8WuyKn3KfTj3Bg3bo1_rGxpczILkS7MwMbEb7NLiznfKmBPd-63ZSzUynreeaAzA6gqCJGs8Uega__2BwXZw6glxD-QxSLJLS5Jsd6HS31CEhZ7wSCMe_BZpmKzlvWwiF5w5bxKqkL-swPLpXTdotvFYZo904seaJmZiQXpSK3QI_T72qvanyFV01vgDMJpWDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jkvfl0Um8f5fideDsUKHnb8EvsnA51nHOWRSRB1_SNeC3exOyQdHsM9n_j55aMYa4R8kfCqbXqn9wFFl9kvIWV3rD132V4dz2NXcLIaPpEJOxODO9F05uWgkWD0zebKPeh7bOgizEGc3wcgXN67N5uibzbnvHnHNkeqbG739cryqGyTsgAydh6jsTwMtxi8Duo83LpGGLIooX2yFPSDGIb9joPvDuTSuqIZFp1tVWAQIOC-s7oykP7XjYiv3ncY__GzM_1wbTIHoUWtzWDCfoY4ewBSyZ1rqcezTkYObbIPai1CZGyCuBXp6AF-MSE1PGuKkR1BlCcrQi0477YxOwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tlxd5sbwukOBDB44nSz9a2OiaELr633haWpsguy15_2kqOka04Iu9bnypb8Rg_Plw6EZHMi2ipGOLe7PPl5wJr9C81DFmMBzyBB7ImoCcTv8L01ayMsIlDc1ePAesHV4tH-P_e67KYPWXcPV5dQnv1LOhlvDwj15lleGHT2V4eti-QfpnHpBH2Z5H7ORXTfzchoO2aiLnUstuurGqbcfXN7xs36fVgsA-t6CClDEmej1GzccWrgbnoGDRAlciCQeTNItAhSJs0rTf_dJ8y3rflui_TIFPsC9FRDRRehArJCaJ0BMcri-9pVWkDjgVwma2OTz9EMtDW6StJ7SQLfVew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ncu4Q6zdTquIEJA9Egt9AgEgFtPzUVBDXfsAvDFWwz3TJ4AF6v33D4Art5NVOwu7I8_iMWhKKBIrgH7HRHv0HhbUu7yrZ5l6y5iZL2Q7VjXmJlDBjHjA12Vai9EpRGIMNvcBBk-o-IjnHKcC2Ddmt-1CjtNW5n0R89rXYh5z_gywLPYaTTpzwSFgZkWMlWZmSn29YhpR8Cr165wt4B5baOLK85KfVGT7gF8pdZsLCXkGP-yA7LDJ7zILF2qQ48QyizeBzxX2HCSQpvam8MB9f9QVPuNshaBZ_0-qAyILVxE2ze8ZU2mOVVqjWWXK6QwZthSh2Rtj_yLVCIJE7eRIWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MpgQBTxnmpuvQii7N19guRx3-GCuI_EMVnyOG-G2AMtf78_GX6lg05BxE3IKdqgjh_7x5pr5m61VML06NV3qEKuJXCR4BaCPIv12-QMPizi5J28LSFhsy4v6l6SipxUgEKeKALR9cmV4KnDjlwyPr7krBqSeacMiutob0RyRiMQEtSD3YJy04mEn3k6ggH7wgPbXKKn9_U_s72uVL0KmDeGgpQuIyvKaCi4Ls5Ah8PM_rLQdzVdsfk7s_u4kYPyHXa-tHLqI1MEycI4Ldu8aPgaymLeRz4oj929yq1M54gTchTuaPv6xrMWRKLPF9ZL7ivNBBJxKlRgZtv_NcJ4CWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/doDwM3mE2lskPV15ubWJ3NpFWZSrVgfvWjnkfwDUXfIoUvHu5lumjCpjUb2BMOmv5FObxhlxpf1mvuCJjlr3Gjv7bG1YwWmFD8xqMJZZROxwjZkTU1T2nQqXf9pX6J82iNgoMHPrRceV7ehWlf8oq2_sFZlKNN-7LLklbihu5r2maNykwuLtdlk-A7pVYGtwBZGCQU0-M3mAB05GX9hyMxZFVA-pmdKcnioCyJHnKclzx_P5Vn-Z_Lt4HymwVJ9V7zFKj_qOz0goPQbWFJroyK34mVObLkxcGtLoHABLJjiF7UR_2TmEmzcshuFDIBAiEKg7RZmwImSyp4IfVLabLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
قاب‌هایی از خیل عظیم عزاداران امام رئوف در حرم مطهر رضوی
عکس:
امیرمهدی آقاجانى
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/455769" target="_blank">📅 02:51 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455768">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hb3JnHl4WvvAIVCsZD-vrdNMpatWQE2KUcf64l6M8lB3EH07mQMcEmh99sB2REo6P8_EBn09eiApnhoQsNVdWqTdkw3dE4Si9UYM-TpxgiluzsgiFEuJHsHYeg3ZYtf8Ih4a97iABL30-CkpwivOUZaCTncMY0W06YUrw50R_lWCoh6006UfcQJIsf84GGaq2kEG4ICbPf0XTcn6NaRZVl-m0apOoKlmAefYjCd382F2ZVfy4dHye5NnKEuKqSMXaKTusBmYIhIIz9WURMjIt6dv0g50kPBnS0IAbYuLS9tlGSvZFCo4Rkl62qWxND2Lf98ZA5oNlEilfrh-sNjEtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قدردانی حماس از بیانیۀ محسن رضایی
🔹
رئیس دفتر روابط عربی و اسلامی حماس از بیانیۀ دبیر شورای عالی امنیت ملی کشورمان دربارۀ لزوم تن‌دادن آمریکا به پایان جنگ در تمام جبهه‌ها قدردانی کرد.
🔹
در بیانیۀ حماس آمده است: پایان دادن به این جنگ‌ها به نفع منطقه، مردم و آیندۀ آن است. ادامۀ آن‌ها اما فقط در خدمت برنامه‌های دشمن صهیونیستی است که مبتنی بر تجزیۀ منطقه، بی‌ثبات کردن و از بین‌بردن منابع آن است.
🔸
پیش از این سردار رضایی در توییتی نوشته بود: پیام ایران واضح است؛ تنگۀ هرمز تا زمانی که آمریکا به جنگ و محاصره پایان ندهد، دارایی‌های مسدود شده ایران را آزاد نکند و با آتش‌بس در سراسر منطقه، از جمله در لبنان و غزه، موافقت نکند، بازگشایی نخواهد شد. تا زمانی که همۀ شرایط برآورده نشود، تنگه بسته خواهد ماند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/455768" target="_blank">📅 02:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455767">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmBYDVmlcllKiyFdi4VSkMKAWbJlym_U6Ss5XKCPd5itOJs6AmIgX_95pP0KVowAY3FIG8N_MljoP2Wz7UXZk-3SHMui30hS5fXvkWNThyD0jb5zna2drx75MQfMkTAJKpyoIPtfuQz5stoi_xoIu1DVXemamb_n5ZMOj6aJUcY50Q2qshZEp1pMb98H7ZYiNa0fcKAB1aiuTzP398Ou_yJIGAYPY2W0v2qwQlOmtF_xgP6huZ69Ku0en08NlgCbmKXPkrh4067gpxvKMPGeh6VbkGDZixLfMSVgaet147_BzWX8ysdpPBNgyYBxicSLwNBtp3IfAlTROwW1GksWRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش منفعلانۀ دولت لبنان به باقی‌ماندن اسرائیل در مناطق جنوبی
🔹
نخست‌وزیر منفعل لبنان ضمن اشاره به تخریب سیستماتیک زیرساخت‌های شهری در جنوب این کشور توسط رژیم صهیونیستی، به محکوم کردن تصمیم اسرائیل برای باقی‌ماندن در مناطق اشغالی بسنده کرد.
🔹
نواف سلام در بیانیه‌ای گفت که حملات، تهاجم‌ها، تخریب‌ها و ویرانی سیستماتیک خانه‌ها، زیرساخت‌ها، ساختمان‌های دولتی و اماکن مذهبی توسط اسرائیل، نقض جدی اصول و قواعد حقوق بین‌الملل و قوانین بشردوستانه است.
🔸
وزیر جنگ کودک‌کش رژیم اشغالگر عصر چهارشنبه با حضور در مناطق اشغالی جنوب لبنان، مدعی شد که اسرائیل از این منطقه خارج نخواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/455767" target="_blank">📅 01:58 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455762">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HGJYHpBxBCSWD4jT9TD0yuQVUnl6DGmfmOGEPGsQoicEASUZLiTpg5WIEUm0GNPO5FlrqassL4yv7krm0BcWb0kDuvjne79MYOiJXNoPr0_WxwaSvUS7JIRFHpuU3AhQWYRW9jYpBD7HCzsX6n8MCkRvBl6LxOfxM5NWYzqPkqPEV-BPrFWF59ZvuY0--wFqATW19qM8bwwFrAgn4toopMSMKV0F9jFE3BcUHkDG4OSH81Bwd5gXsaUIcQ2I8tuF7_NkZ0jtBMyqJh-lFjmvA667DIBjrKv89nN5HiAAuvtuz6Vu5doX9uWbg6BVXFHa4ADuSb6VdMCDMQ0xbk6rpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ML5CePI1lGew-P2sJq0kIPJZd4bmhntPFPOqbZdgvTGt3dqqBPhS1QAE4FIZddVeMjhJM_SRsTCgGmGbBrlM9V0IMDKd6SYBlNYIEDn1RS5kr6vwxqjMl-yneYd_ofVPV6TGnzHDuvu7TXd6yhdR34ZQiiQjSIm-bNvrGhJedYF-ekWuOkuRKZVURIVs51QEPliMrdxonzQAFth7pLMr-oKby10z5Qizh1bTDB4QvPTqOu_Tg2b02uvja1sb44T0uKdT0mQy0jI4QY-t20MVQ9J_Mc0Bh4bA9aKWtn4nfj19VJq53jeTjgV17HBQeZZGw8JBzIJ4_NJ5_kdc-FaazA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NyB_8AuPWKB1fAA-uqqp6OhnRqyfjQwXeiVY4ubEyalG73uoaBGxOFAmf6sNK4ZFHiDAmAVYkEs18ZoE-WOrQkAiXqDECKZmc95CFwAKn_wKB2y6Rtx65sJTn0GDL4U4V2icJr4aHiZCt2tUnzmiQ4n0H0uTgAyP45CjWxGOTR16g7w1Jx6EGF7omdW1lIdNi_-xNdKAzvTPeA5LpESOrFD58Dtf8S_94O30nUt-bX6DR71vYCB_9Q61z8JbHsfJjbI5by4BQJ0_pidZp637DZVbSEHQtGaJ8mTyfPC1lQ_9JzXnplAOrBNhCkoT9bzxMwpGguLA4BZ4Xg3NWw0a_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q_Ndx5N8sc8IXL0EhbjnQHmDBurtRQMZ1IY77dpcjENu-9-bSbCnOggC4eHtEnHH39dY5LoqpsS5cYjZxABTrTRM3IMki9cx7hdtHZoJlhbDs1pd2txQg0tn6ZiW4W9sYY9QfPKkDL3kR_6yTQth6HAOR5UFFiOW7n7-tGdX-FVASxBdXDWE1XdAUEhqIhp-8cmW8Cwrzmgudgn_5cjVpMqa2YIt5Phglxp5FuL-Gy5Pp5tXDAHGKnUP8DAC7H9n61JWcaYjm9sADL7VKZYN9mZwbyFXlhiHL4xnOKHtf7HSe2GY36CqV6pbBvjZkmZak_cp6zqleBuzvU3YNl_2gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mmCsIsIcezs75Kt8mi0KSphPw-bRtEQKGINVTvDeaT_6CszG0OPd80BgbAatOzE4rIKM7DVxbNEjQTr3J2h-kJJHf--DYakaubb4r4fRSoU9YFJIWnDBiy33XfVuMApBqRm2bgpbTWpWYIdk_qNrBd5V5HmoyFTVyx2nhfLFk6JUnOrZRRZX9G66pvfYGg-OvYSLLpz90JYDU0AF9vjbNOxjFXDKOSLMAPmB1Cr---P1GxTzuyO_nEmoHpCDfVAPWgj1Hr-5Ih21N3URJNscXsVNVbNhJTTnB51D-jl8NCTJgUfUq_m4Q21Bc_OlUCFE_mtEeAJfr4FweqAfif1jDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم چهارپایه‌خوانی در حرم مطهر امام‌رضا(ع)
عکس:
علیرضا رجب‌زادگان
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/455762" target="_blank">📅 01:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455761">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXCP2QLB8j7gjiJuS0ELLn6xgIHueQSOskevXTqEhRHiVniytAJOukYV7Ag9voA6YoiJNNx_f1ybLjGTrkDkJ-x04HjQ1xH5MLfjaHHwoeFhwuZZPxUVp8Che6esJ7b87oo1_l-pdkD9PPTSKSzfezH5j7-r-GL1REGUvnnC0n2ACrvtz3ESbnRhHBi-GUXykFOcUfnLVqK9wK87W1sZQU0NyfP3h-5iRrMvR4EAPe9Ut3bCGR_UBSk5oztHiXxElulx2zhZRomkemaiJC9gspJEefRemLh8aut6tMIpionOlje2rQspwdNPa_RkPvmzfJtqZh9gt0wOnJBzZRX77w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات متعدد صهیونیست‌ها به جنوب لبنان
🔹
المیادین: توپخانۀ ارتش رژیم صهیونیستی اطراف ارتفاعات علی الطاهر را گلوله‌باران کرد.
🔹
همچنین اشغالگران، ساختمان‌هایی را در شهر الخیام، شهرک حداثا و منطقه بین شهرک‌های مجدل‌زون و منصوری منفجر کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/455761" target="_blank">📅 01:13 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455760">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c30da54c2e.mp4?token=RuMkfrq4VRIF8L17HJs15KGWyF1icZk207ncqtCSe_MBJ-mHx9Ll-2nMunAWA32xTIs2HZLY2aLxFbs2lNjyhE_A38ryX90Jrc7Yjzy6NQBQY2e8ueF1RA7n6-vSNV8cGgOPWRTSWuGuFS2R340n21_YNGLyql29h7uP_VQ8dZzYOsW1UkAdeZ-7FrACLWOsxKL5RlqpXy5_7Oah2Tdo2M5lZGkZ_Og4GB3CbGALUBqRy_FhxnmKRnIz3gDMgqDJuNEXex9BTiayp0IOxco7EtsU8b4LAVwJhLtMnQQ3ELqtgRi8DNVshUnzuX_GjmlBEpirLSTo3ABcSxNrPGUToQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c30da54c2e.mp4?token=RuMkfrq4VRIF8L17HJs15KGWyF1icZk207ncqtCSe_MBJ-mHx9Ll-2nMunAWA32xTIs2HZLY2aLxFbs2lNjyhE_A38ryX90Jrc7Yjzy6NQBQY2e8ueF1RA7n6-vSNV8cGgOPWRTSWuGuFS2R340n21_YNGLyql29h7uP_VQ8dZzYOsW1UkAdeZ-7FrACLWOsxKL5RlqpXy5_7Oah2Tdo2M5lZGkZ_Og4GB3CbGALUBqRy_FhxnmKRnIz3gDMgqDJuNEXex9BTiayp0IOxco7EtsU8b4LAVwJhLtMnQQ3ELqtgRi8DNVshUnzuX_GjmlBEpirLSTo3ABcSxNrPGUToQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🏆
لحظۀ بالا بردن جام قهرمانی توسط کاپیتان مارکینیوش
⚽️
پاری‌سن‌ژرمن‌ برای دومین‌بار متوالی قهرمان سوپرجام اروپا شد.
@Sportfars</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/455760" target="_blank">📅 01:09 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455759">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74e503c661.mp4?token=AvmAdqAT7qleUJQSwCuZ7MEbrYa3JT3_3o6j0dhCvZjxuuVOlPKG7vDTaAXOWcT7MaVjdiocu63lhieadtNi3QUCWuY6tgITHjzkGPzBaHXxsi2T_TwQg6LsSR9KBJc5V5HbOTpIv9pWzVw6XBqvo2iDf82VKFhTorQEs5cuPw1-eXzQqoNotCPe42VbdfHtXFjrNCY3dMOksYU7rRSCtM4iGX0QRC7rDomlTe0WOcb5TvwxrWa3wUCS3vmRGyymY67eAQmovfGf7I54hu7lv3kfeS_ymM01bjTsDJvbtgrrJn3GzFdcUvJBV4cyrpfyqcW14mWeYEBLsElh5FC7Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74e503c661.mp4?token=AvmAdqAT7qleUJQSwCuZ7MEbrYa3JT3_3o6j0dhCvZjxuuVOlPKG7vDTaAXOWcT7MaVjdiocu63lhieadtNi3QUCWuY6tgITHjzkGPzBaHXxsi2T_TwQg6LsSR9KBJc5V5HbOTpIv9pWzVw6XBqvo2iDf82VKFhTorQEs5cuPw1-eXzQqoNotCPe42VbdfHtXFjrNCY3dMOksYU7rRSCtM4iGX0QRC7rDomlTe0WOcb5TvwxrWa3wUCS3vmRGyymY67eAQmovfGf7I54hu7lv3kfeS_ymM01bjTsDJvbtgrrJn3GzFdcUvJBV4cyrpfyqcW14mWeYEBLsElh5FC7Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قاب‌هایی خاص از خطبه‌خوانی شهادت امام رضا(ع) در حرم مطهر رضوی
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/455759" target="_blank">📅 01:07 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455758">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gf11CtJLHnEedNgyEWVvTAQirjU5l3Rdz32rZyTq8nENU1aAASJm-WR6kgP8QwQm5cnEMjU2_0oDQ9aLeyx2EngWh-YixErLFwReL69gfl-8I9qlbD2ERWmMkIA-GTuGBsMYPtlsAMTto3sInWorzSJDTnSNNm04C-3hv0KKsy9B4a3cGj6MRLGyMQUTb5LaMwvVCzLnm2D6XS4UxnP5IY56otp_08mlTcHjfSLKA7547RCOt0aXlA59agwGcGfveZHJtOP_YQNRpdaCyMftSNKJCwi_RV_tkQriGGM6rKqRNH4ueVWgDSb_W9vXhqyTqMm0LcLHaHf6-K2LHwtTHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۴ ساحل قشم آلوده به نفت شدند
🔹
سواحل سوزا، شیب‌دراز، نقاشه و بخش‌هایی از جزیره هنگام دچار آلودگی نفتی شدند و مدیرکل آلودگی دریایی سازمان محیط‌زیست می‌گوید که علت این آلودگی هنوز مشخص نشده است.
🔹
هماهنگی‌های لازم برای پاکسازی کامل این محدوده انجام شده و پیش‌بینی…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/455758" target="_blank">📅 01:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455757">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">تاکسی‌ها و مسافران در کرمان سهمیه ویژۀ بنزین ۵ هزار تومانی می‌گیرند
🔸
مدیر شرکت پخش فرآورده‌های نفتی کرمان: سهمیۀ بنزین ۵ هزارتومانی به تاکسی‌های اینترنتی، ناوگان درون‌شهری و برون‌شهری و مسافران در استان کرمان اختصاص داده می‌شود.
🔹
سهمیۀ سوخت خودروهای شخصی…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farsna/455757" target="_blank">📅 00:38 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455756">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CAKmP6fqCAEpx4JTLi7Oh06W9LzZlQxmrcMxL2PodoXxlT9GH-27wZa-gNod-W6El6bGnm6biHXZePH2bBnzzPSmorH5CVWQK1HHatSSwgwkeYx56Cs1nPWd3GWZFtMWs_KgCoKxdGPKza_d3R0MM_Etrft8BTxh0J0l2u1bCXkLIhgXjDRlB2o3Nqh60-wqKCzFshKnLu14b3b1vdbSqpdBj9anQkuAOXqDQgWJKao8fNi0svUbMrlnIPhS7qlJGm5D0GNuaJup2HiHRhfolsXAz8GgmstGRiBFbiFXA-KVHCAY8Lg3ZgDn8R0i_JOFmLNf7iLr99-FbdXO03Tplg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکسی‌ها و مسافران در کرمان سهمیه ویژۀ بنزین ۵ هزار تومانی می‌گیرند
🔸
مدیر شرکت پخش فرآورده‌های نفتی کرمان: سهمیۀ بنزین ۵ هزارتومانی به تاکسی‌های اینترنتی، ناوگان درون‌شهری و برون‌شهری و مسافران در استان کرمان اختصاص داده می‌شود.
🔹
سهمیۀ سوخت خودروهای شخصی در مناطق مختلف کشور برابر با ۱۱۰ لیتر در دو لایۀ ۱۵۰۰ و ۳۰۰۰ تومانی است؛ در استان کرمان هم با توجه به اجرای طرح جامع مدیریت سوخت، علاوه بر سهمیۀ ۱۱۰ لیتری، ۴۰ لیتر بنزین ۵ هزار تومانی نیز اختصاص داده شده است.
🔹
وضعیت تخصیص سوخت به تاکسی‌های اینترنتی نهایی شده و هیچ محدودیتی برای تامین سوخت مورد نیاز پلتفرم‌های اینترنتی نیست.
🔹
در خصوص وضعیت تخصیص سهمیۀ گازوئیل، هیچ‌گونه تغییر قیمت و تغییر سهمیه‌ای اتفاق نخواهد افتاد.
🔗
جزئیات و شرح کامل خبر را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/455756" target="_blank">📅 00:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455755">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d352a6c411.mp4?token=p3aYojDhLLD_GKzwCahir7qtqv7DXhKGDprNH87-mCSaA18Bopq5Ah8BXIDQmgv9qZA_HWO7bLbJuNolaRbpg9xk1EfLL5HUjcK1h1n3X3vKOgmm8lJToTkE2Y2jlUesXlMyh8VpcmJxkkSPZvZTuqqqsxBIkHX13gLbVqA1K6aI911IaMxApdbY1gIudL4hBkpB6hw4FsnDYyTh7kGFwNu9NYUbFeRl3QJubc839jZEsZIg2gOyunzAH481OEVrqLMr7-9cQF-jo2NV9J_UGyIJe5v6dLw0a2Wzp02S8vSvZp6XjIeGuLmLPr3653WaDdexzJ_lPKq_sTtIjqV-Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d352a6c411.mp4?token=p3aYojDhLLD_GKzwCahir7qtqv7DXhKGDprNH87-mCSaA18Bopq5Ah8BXIDQmgv9qZA_HWO7bLbJuNolaRbpg9xk1EfLL5HUjcK1h1n3X3vKOgmm8lJToTkE2Y2jlUesXlMyh8VpcmJxkkSPZvZTuqqqsxBIkHX13gLbVqA1K6aI911IaMxApdbY1gIudL4hBkpB6hw4FsnDYyTh7kGFwNu9NYUbFeRl3QJubc839jZEsZIg2gOyunzAH481OEVrqLMr7-9cQF-jo2NV9J_UGyIJe5v6dLw0a2Wzp02S8vSvZp6XjIeGuLmLPr3653WaDdexzJ_lPKq_sTtIjqV-Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل تساوی استون‌ویلا به پاریسن‌ژرمن توسط ماچو در دقیقۀ ۴۵  @Farsna</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/455755" target="_blank">📅 00:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455754">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bjXR7JfoLMBwmA66g3Lz-WZo-cYy7aglmMd-QCxsApgEZEizIc6QbtPB9DsHlIjLLKQBdWAdkMuLKpp3RpXqtN2bGvdk3mo1BfNrPcieYCVfAbkbrGDa6fsjNv7WOzbsGiAjyPUH9yFdykuegcySFsntCM2EELIAQ5NEHyoxBEgY5imECbaMRDp8CrShG0R5eamDcRbwcWcGiLb1xHbQ2Ur1p5L80n_N9RDacKxTW2EiJ_wt-YUY053a7pta5Ch9-N7uZn4rgvum-nuHs7jfhNDGw_jmiN4VzzBLVRg8Q5MOxqsb4uBhd4V6eBavoHSLGXtCrmB0P_Hf-7c32ue70A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای سلطنتی امارات در تهران
🔹
طبق داده‌های ناوبری هوایی، هواپیمای جت سلطنتی امارات(A6-RJA) امروز به تهران سفر کرده؛‌ این هواپیما دیروز هم به تهران سفر کرده بود و پس از یک ساعت به امارات بازگشت.
🔹
هواپیمای یاد شده توسط مقامات دولتی امارات  استفاده می‌شود و تاکنون مقام‌‌های رسمی از هدف این سفر خبری منتشر نکرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farsna/455754" target="_blank">📅 23:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455753">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYSsSMX6l31N4rxeNFUVOCicOTt2m0hOoJonS8qVdASYFYnHQT_rzkIAj_kkGgEhcBLDo41yV4NZN5ZcT-HlDbYanPl25KsfkizoplHejrDIKcGgW-i1aMMvJ7wXjN3WUtoAsRqcc2rNI8RjT4a73yjL3CGj4wudHp9JKWulESm4C0pmSvd5aOZZ6nONe4AyNHo7o34rFjRMDaC8j-dX9qKI7zy0lm9bFB55HaRWh606k7MZKXay3WLVzE2DmJH9epnD3JjfZar_956g4t3T1vsU_TgE-xN_Fo3DNG1-wymT1pQqM3aYS5IEc0JGTtsgOQEoPuKvq85YnBwp_k_6cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداحافظی کارولین لویت با کاخ سفید
🔹
رئیس‌جمهور آمریکا دونالد ترامپ با انتشار پیامی در تروث سوشال از کناره‌گیری سخنگوی کاخ سفید خبر داد.
🔹
وی در این باره گفت: کارولین لویت، دبیر مطبوعاتی فوق‌العاده کاخ سفید و یکی از مورد اعتمادترین دستیاران من، در پایان ماه از سمت خود کناره‌گیری خواهد کرد تا بتواند زمان بیشتری را با فرزندان خردسال و خانواده زیبایش بگذراند.
🔸
ترامپ افزود: کارولین اکنون یکی از مشاوران ارشد من و صدایی تأثیرگذار در حزب جمهوری‌خواه خواهد بود، در حالی که ما برای به چالش کشیدن تاریخ و پیروزی قطعی در انتخابات میان‌دوره‌ای تلاش می‌کنیم.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/455753" target="_blank">📅 23:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455752">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/807de0eb7d.mp4?token=gAHjs1BCU1aX-vjfOg3iqZBAF41OeTQsqUB-PQ69olzlFQFZ1-SMoFyb6LeH20WKuW-xncNGnm2vQdejbnuEb1hFgPKUzZA9jb3j-5mkgTgLfNljeGeTjROcR7m1-xXRGvUN--EVLbKN-_BvLzdnf4-9JYelV8BpU4zq8QSjd1AQZEBh2G451GY_UfDWVTpqxb_IaS1pj_0jHSY5kOkvw8Dld9q7BCEnCWBeEfMmEmEyhQyZqPhmQXvTWLFfnxlavlrzG0-vIzNSVJQZGHgxgzJbswb3QeUKxHsxVKldAGlD4crwjUa6CPFp8uefmNMrwbi3M3w4CDYZp7fA_6VOUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/807de0eb7d.mp4?token=gAHjs1BCU1aX-vjfOg3iqZBAF41OeTQsqUB-PQ69olzlFQFZ1-SMoFyb6LeH20WKuW-xncNGnm2vQdejbnuEb1hFgPKUzZA9jb3j-5mkgTgLfNljeGeTjROcR7m1-xXRGvUN--EVLbKN-_BvLzdnf4-9JYelV8BpU4zq8QSjd1AQZEBh2G451GY_UfDWVTpqxb_IaS1pj_0jHSY5kOkvw8Dld9q7BCEnCWBeEfMmEmEyhQyZqPhmQXvTWLFfnxlavlrzG0-vIzNSVJQZGHgxgzJbswb3QeUKxHsxVKldAGlD4crwjUa6CPFp8uefmNMrwbi3M3w4CDYZp7fA_6VOUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول پاریسن‌ژرمن به استون‌ویلا در سوپرجام اروپا توسط کوارتسخلیا  @Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/455752" target="_blank">📅 23:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455751">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62f104184f.mp4?token=lUc9nt871uT8UtgAy_X-OdhdKFrCGzR3Rh_9NQIJtuopeP3TEU7kGlAYWa8KzMBIfKZdQzN_BlzmiXxhST25fyzQlZ5n4GroucoaXXR_PFc_oN9q6nrP-OCH3JDhCyfC37R-L4XD4qExxEH_q3lyXKPLrfPBAlV88HHRrg7Zl13fRaNJPuw55U7su8xJ-0hNGvzwDNWD6eVIQzeY-J2iin8GTyi3kKuhM_aeqwOXeX94xfU4I8RIbKsxsUfTXdiA4MFl0Z4v7uGcOl7AyEiTJ0MKbb5aIhUEynwKtovG-SU6hpsUTuNdi0OkZpEvaqur9rZA0-7zL2lHB_SBBi_dDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62f104184f.mp4?token=lUc9nt871uT8UtgAy_X-OdhdKFrCGzR3Rh_9NQIJtuopeP3TEU7kGlAYWa8KzMBIfKZdQzN_BlzmiXxhST25fyzQlZ5n4GroucoaXXR_PFc_oN9q6nrP-OCH3JDhCyfC37R-L4XD4qExxEH_q3lyXKPLrfPBAlV88HHRrg7Zl13fRaNJPuw55U7su8xJ-0hNGvzwDNWD6eVIQzeY-J2iin8GTyi3kKuhM_aeqwOXeX94xfU4I8RIbKsxsUfTXdiA4MFl0Z4v7uGcOl7AyEiTJ0MKbb5aIhUEynwKtovG-SU6hpsUTuNdi0OkZpEvaqur9rZA0-7zL2lHB_SBBi_dDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول پاریسن‌ژرمن به استون‌ویلا در سوپرجام اروپا توسط کوارتسخلیا
@Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/455751" target="_blank">📅 22:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455750">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a26d806e9.mp4?token=ei9-KTh2euhbKgvtgRFklZpGbD_bMCRJ_3iwVc97JwqFUfrLNWbwIKC1xfyV7Ew-_Y-exBSBUNH3eMgTwA_HxDF4U8SxpjAVdfoAyD9auJjgPibVsbSooW5OqQ2OozW2KaK-TaZ_vQPF88FOrjuodLraR9epBBAomRMtO1c2kKWLXZPCHxBKzgMFhpV4cEebOuyfijrhuw_Cq7Sjmh06vxC4sTvGiIz7haOgX7r2u2RmzCNegtYQyr8kfEv6pprWkdlEyisKS4rcIGYKsqXc_SM63hTNArlvuMYct6gD8OLutmFnaTKYnm2Ufhyw32nkMxegw5uRjC_bT6b5biz0Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a26d806e9.mp4?token=ei9-KTh2euhbKgvtgRFklZpGbD_bMCRJ_3iwVc97JwqFUfrLNWbwIKC1xfyV7Ew-_Y-exBSBUNH3eMgTwA_HxDF4U8SxpjAVdfoAyD9auJjgPibVsbSooW5OqQ2OozW2KaK-TaZ_vQPF88FOrjuodLraR9epBBAomRMtO1c2kKWLXZPCHxBKzgMFhpV4cEebOuyfijrhuw_Cq7Sjmh06vxC4sTvGiIz7haOgX7r2u2RmzCNegtYQyr8kfEv6pprWkdlEyisKS4rcIGYKsqXc_SM63hTNArlvuMYct6gD8OLutmFnaTKYnm2Ufhyw32nkMxegw5uRjC_bT6b5biz0Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بروجردی‌ها دل‌هایشان را از خیابان راهی حرم امام رضا(ع) کردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/455750" target="_blank">📅 22:56 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455749">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nugXHex_SGoNLYsFTfldRFUMBMLH499T-Tc5er4uYCefAQ9870MMwnjpUQFYSE1MmYhAOtBYwdqTWWkHjSTVkC3TsiOTgS9UndoML2WnxwMbva7wZwX5IQCq6l-wrxMlMVDm0YXrdKNArewy5AmjNz4pmleeX0EqX345DYwEvEOKZSbxOPo9ia3FlTIKF92IA75cAtsRLmtE960GivDmzEFuHf6X8sMMsg-4j0-bSCYcjjMtn6oO1GCfyw6S_8ugH0ikDAnYGZZYo3m_OVmfYGImLjKS8aAAv1leLY4HChu-nj4pIrHMS0p9hJFnbGinOFmPAzlTS2rQD5gHbd8kWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتصابی غیر منتظره
🇳🇱
ژاوی هدایت تیم ملی هلند را تا سال ۲۰۳۰ برعهده گرفت.
@Sportfars</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/455749" target="_blank">📅 22:53 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455748">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
منابع عربی از حملات پهپادی نیروهای مسلح یمن به مزدوران سعودی در بندر المخاء خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/455748" target="_blank">📅 22:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455747">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IkE1ZRzoHva_P2Y9VRHT9Xf3WJ6kS3tFm3JSqEu3eG86dBr_gfstkqAhFIrwu_YTWYk2GLs4cBESm-QkNTBjRQTvgs5XHUbpPlj_mzOCG4WgGNkwD_eyUOnZFXlnp1oQbDsSe3ngp_UblevNR2BhnOTcLwxItid1VrG2cA8otUTLqP8TU_eZAPnLO9quoQmFPuPBdMLCbjSx_rCyd2tUcQjsf2Uf3PgccmSAODACAyaw1xEjK32_t89nIQzF1119kVxGJr8XfRnVLaz-rDHkx7-frt6VWE0I-w5jaZsobyU7Xc9H4wgB3enGw59sMkMVKnjqr6mv-_jxfJozjqEvuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشت آمریکا به تنظیمات کارخانه پس‌ از شکست سایر راهبردها علیه ایران
🔹
به گزارش روز سه‌شنبه آسوشیتدپرس، دولت ترامپ امیدوار است که جنگ چندماهه و فشار اقتصادی ناشی از درگیری‌ها، ایران را مجبور کند که در برابر خواسته‌های آمریکا برای پایان دادن به برنامه هسته‌ای و بازگشایی کامل تنگه هرمز تسلیم شود.
🔹
این بخشی از تغییر رویکرد ترامپ در این هفته است و او مدعی شده که ایران اکنون در آستانه فروپاشی مالی قرار دارد، در حالی که ایران دهه‌ها تحریم‌های مالی را تحمل کرده است.
🔹
اما به نوشته رسانه آمریکایی، اعمال تحریم‌ها اغلب راهبردی بلندمدت محسوب می‌شوند، نه ابزاری فوری برای پایان دادن به درگیری‌ها.
🔸
این تغییر رویکرد در حالی رخ داده که ذخایر تسلیحات اصلی آمریکا رو به کاهش است و به نظر می‌رسد که مذاکرات متوقف شده است، اما ترامپ اصرار دارد که فشار اقتصادی مجدد می‌تواند به پیشرفت گفت‌وگوها منجر شود.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/455747" target="_blank">📅 22:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455746">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-kuUxE_poRyGjeM-tARI4CPorRgB1fgbk8T_J8F1yUbdELWO3VD7dP6Zleu2q_GRPC48NwqYeRKioUx-ayilNW5fT4IJ5KkvXjtKDHwTBr7vBnjFS13CfcBRPOS8Xs31yGmP0mYwrNB9CsoiXgZtL8sH--J1pkw2Pd62gbRUzC04HR3oQfEtFC4DSrtthqJliwAx8dmTJ7UwD37W4Mxz-7IfiJOuVqa92wmwXriwpzs0vCWDitweyB_jjakwAjvvsn_vhHA7mVFgznjOcvPCRyeRcrzQpMRLdkECEoi3aXarCff1EDLWQ4IaLMbxQWwWHxqbrkZcPN_2nJonEEP_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
نهاد مدیریت آبراهۀ خلیج‌فارس: تنگۀ هرمز تا پذیرش شروط ایران همچنان بسته است
🔹
ادعاها و توییت‌های پیاپی مسئولان آمریکایی درباره رفع انسداد تنگه هرمز، واقعیت را تغییر نمی‌دهد؛ تنگه هرمز همچنان مسدود است و تا پذیرش شروط ایران بازگشایی نخواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/455746" target="_blank">📅 22:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455745">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/317abc18ad.mp4?token=bo75ajilZELSOPCe3OF3NyvACyDzClel66YyOdR7W-SzQ-HcmYv06vgKTkOiXDCPofelEa5KKPz3RaoJ3SpS3K6MPxUU-cnmpTxKuo7uBkH2eLpBUxAS7Ixv0xurRJBw_OgNdQAPlNkP81ju_I7dWUy7f-2B26IuMN6yjADiLvLQ9lh9Xg02jgin2LjywokbPXl2yUomIfYNbghnjS7iBsAH_T3rDhMWTID_tHW-1swL_TLN5XBY_YgiI6iUNofcIIB_aAQ8-Po-ZmPClHsHH5z2gh5C2gVuWVfQOOqX4E_wHjPc_yaACV9uqH_KJMhbyFOG2fa0RMEQNuAkoqF60Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/317abc18ad.mp4?token=bo75ajilZELSOPCe3OF3NyvACyDzClel66YyOdR7W-SzQ-HcmYv06vgKTkOiXDCPofelEa5KKPz3RaoJ3SpS3K6MPxUU-cnmpTxKuo7uBkH2eLpBUxAS7Ixv0xurRJBw_OgNdQAPlNkP81ju_I7dWUy7f-2B26IuMN6yjADiLvLQ9lh9Xg02jgin2LjywokbPXl2yUomIfYNbghnjS7iBsAH_T3rDhMWTID_tHW-1swL_TLN5XBY_YgiI6iUNofcIIB_aAQ8-Po-ZmPClHsHH5z2gh5C2gVuWVfQOOqX4E_wHjPc_yaACV9uqH_KJMhbyFOG2fa0RMEQNuAkoqF60Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری برای پیامبر اسلام در بندر ریگ بوشهر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/455745" target="_blank">📅 22:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455744">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa5d40d145.mp4?token=CUVN_fjvMHWf6ruo2vwrUrpkrW-BXtMLnaXdE9M0bP01YQYsWt7YBFqcsDZB1w9rHwACQ_CkplPpkBNxiIwp-gAaBmKnQlKRht_qjsRN_3mKFJemKJg1ghHWnnFddM14SPMV0tTh11lWUiXxtw44AMJiXySSlEI4SjqSf8pLZ75DAFTOqL7pl9OsEPMd9auD5K3xnBV7eeKeuvy7vnKQVNsVQmMzhaWW_WPVJ3QYLIsoto2QX5lNjIufQzeBfa-V8mX3u73Ipsl5McbD7WooRXGZIOQwawSmepGm8stZNgSo6hHa8Kp1W3q47Hz63d1hYuRbhmoiuCoPFzrw7VJnYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa5d40d145.mp4?token=CUVN_fjvMHWf6ruo2vwrUrpkrW-BXtMLnaXdE9M0bP01YQYsWt7YBFqcsDZB1w9rHwACQ_CkplPpkBNxiIwp-gAaBmKnQlKRht_qjsRN_3mKFJemKJg1ghHWnnFddM14SPMV0tTh11lWUiXxtw44AMJiXySSlEI4SjqSf8pLZ75DAFTOqL7pl9OsEPMd9auD5K3xnBV7eeKeuvy7vnKQVNsVQmMzhaWW_WPVJ3QYLIsoto2QX5lNjIufQzeBfa-V8mX3u73Ipsl5McbD7WooRXGZIOQwawSmepGm8stZNgSo6hHa8Kp1W3q47Hz63d1hYuRbhmoiuCoPFzrw7VJnYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رواق دارالذکر و جای خالی رهبر شهید در میان زائران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/455744" target="_blank">📅 22:12 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455742">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKosrzjMTS3XxCZM-s3dfv8rbm3TWYVTgkkYOt3E0Od-CT4A3YyFOH2Fv-hxmtOeEv0kYtXGl0rjN8CuynhMEflN-hOPkjc98uvhkvsPShkgwTxCljAHn8-ZL4yqGAa_1O4Zn2SiWqUauxleeERwiaoerTk6pWM1We6jLVEguN5G74h-zfw-IgXKweWrVkf_W5jygxF9J8SQ0MRh5pq1ZckwM9U41ClKmesLgjuqGKBHHSrxR8JmP9QU1UkS7VaWgm_VUxBvvZlYqEwmhpDbQWFnUEpZX2ygsko2e86kWVsU38_eFwhbogZpQB14jqplk50SwV0QQW0n7yeLgjbj2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیکر شهید ۱۸ ساله پس‌از ۳۸ سال شناسایی شد
🔹
فرمانده بسیج اصلاندوز استان اردبیل:  شهید جاوید‌الاثر اکبر بابازاده، متولد ۱۳۴۹ بود و در تاریخ ۱۳۶۷ در عملیات کربلای ۱۰ در منطقه ماووت عراق به شهادت رسید.
🔹
پس‌از ۳۸ سال، پیکر مطهر این شهید والامقام شناسایی شده و در روزهای آینده تشییع خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/455742" target="_blank">📅 21:42 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455741">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmDTEd1QyzqPnXdzd9_qL3H8uEeN4VVfz_Qod27_uaAraIyOPgR0cyqdFtum7FBb_Epwe2nFOU5NArtbQpFjZo6zC8W6dM5-DjcdKJAa2-QpKWDy44ArD2kxHplqYIyry_Bav91w4YOlF_qUEi2QdK6EXAfVFAanae_xXmeB-K3Co4FkkS-NTUrFeCOt6LqxMkNvArAToj6ODK-4pB3Jzk4GAG4QxbklEkI9ZwBCz2Y6qOLx9vq1Ip8KbetVcHQQ7AxiwpXSGN0TMT9-ojBOeXP6LEPpkhScU-6NNimD7_jYCuB1k7Zk0mZNUlRSk3lymGDL8Ag24CS8MwhQtR-0rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویب کنوانسیون خزر ایران را از کریدور انرژی جنوبی حذف می‌کند
🔹
الموتی، استادیار روابط بین‌الملل: در این‌که رژیم حقوقی دریای خزر باید مشخص و روشن شود تردیدی نیست اما باید کنوانسیونی به تصویب در ایران برسد که دست‌کم درحد قابل‌قبولی منافع و امنیت ما را تامین کند.
🔹
در کنوانسون دریای خزر حدود بستر و زیربستر مشخص نشده و تصویب کنوانسیون دریای مازندران، بدون تضمین و ترسیم خط مبدأ به‌معنای واگذاری برگ‌برنده در حسّاس‌ترین مذاکرات پیشِ رو است.
🔹
شهید رئیسی نیز در اجلاس قبلی سران کشورهای ساحلی، تصویب این کنوانسیون در مجلس ایران را منوط به ترسیم خط مبدا مورد تاکید جمهوی اسلامی ایران دانسته بود.
🔹
همچنین یکی از حساس‌ترین مباحث، موضوع عبور خط‌لوله نفت و گاز در عرض دریای خزر است.
🔹
این طرح، نفت و گاز ترکمنستان و قزاقستان  را به باکو رسانده و در صورت اتصال آن به مسیر ترامپ و یا دالان زنگزور و از انجا به ترکیه و اروپا، ایران را از کریدور جنوبی انرژی حذف می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/455741" target="_blank">📅 21:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455740">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kAWSWb8H-elEkV3mJo_Fh5dTQUZkI_zZuiGNeS1LSKEez0X7OQEcM5v1GrVi_7LBCJxvZn8vE1yqtaMueUZPKBL5I49xCsZTRCGb2j-gRJpA2Xd8tB94Ilfa-ioHhYfqo3RiQWOChXyhQOxE5iO7fJg6sQwnroZKDq9qP9w3bgjfdbJvyx1qsGJgsjWeSz0BGbYxp3a1Yu1Lq8xYtCGXTw8q7L8gXadVQMZZO9drjkqyv4kWwJ-Byc72FZsuYn-8nZ_6BcRKZZTW_I-Urw9deblUzOD6neW8e33ybEo3knlIvIDXs56sHooYBQcfYYbaDo5CKZDXy3xJFPutlJU8TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«غلامحسین محمدی» سرپرست سازمان تأمین اجتماعی شد
با حکم وزیر تعاون، کار و رفاه اجتماعی، غلامحسین محمدی به عنوان سرپرست سازمان تأمین اجتماعی منصوب شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/455740" target="_blank">📅 21:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455739">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2MYAytrWO5gN702BS8ekLHmCKyRQh0BZMR2p6KokumRZYBHw-_6O04qCkuI8HvE6xeZKZqgBE8sDsq631OqX_ICKVtdR1xTafIv6kLLuAY0H0kDsyvX8IryjiNT4QKDvGOosPbZ21l3p3dJ9A8wScSmkYWflJMyVB8YOFjplWVDzFuLL8nCGZzDJYaawBIeMnl-vA6MP7w5w0CLDseHlFLEywwf_Sccs_bE3twm0FREuKMiHz2MQdVbI6WHQUty6Txw4edw00guXoqcmUmo2hrlRxaQxC2x69R27Kh21m9zlAdCXR6qOFqLvJJKrJQ16VvvE9GFcJypc3hCOpnAfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ثبت‌نام دوره تخصصی «هوش مصنوعی در روابط عمومی و رسانه» آغاز شد.
🔹
این دوره یک برنامه آموزشی جامع، کاربردی و پروژه‌محور است که به شما می‌آموزد چگونه هوش مصنوعی را وارد فرآیندهای واقعی روابط عمومی، رسانه و ارتباطات سازمانی کنید.
🔹
در این دوره ۲۴ ساعته، از تولید محتوای حرفه‌ای و مهندسی پرامپت تا تحلیل افکار عمومی، رصد رسانه‌ها و مدیریت هوشمند بحران را به‌صورت گام‌به‌گام فرا می‌گیرید.
🎉
ویژه مدیران و کارشناسان روابط عمومی، رسانه و ارتباطات
⚠️
مهلت ثبت‌نام: تا ۲۷ مردادماه
📝
ثبت‌نام دوره حضوری
📝
ثبت‌نام دوره آنلاین
مرکز آموزش‌های آزاد خبرگزاری فارس</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/455739" target="_blank">📅 21:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455738">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/455738" target="_blank">📅 21:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455737">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">وال‌استریت‌ژورنال هم بلوف‌زنی ترامپ دربارۀ تنگه هرمز را زیر سوال برد
🔹
درحالی‌که ترامپ در روزهای گذشته بارها به قصد فرار از شکست، ادعا کرده کنترل تنگه هرمز را را دراختبار دارد، نشریۀ آمریکایی وال‌استریت‌ژورنال امروز با انتشار آمارهایی دربارۀ تنگه هرمز ادعاهای او را به چالش کشیده است.
🔹
این نشریه گزارش داده که روز گذشته ۱۴ شناور از این آبراه بین‌المللی عبور کرده‌اند درحالی‌که که پیش‌از جنگ روزانه ۱۳۰ شناور از این مسیر عبور می‌کردند.
🔹
وال‌استریت‌زورنال نوشته از میان این ۱۴  شناور هم ۱۱ فروند مسیری را انتخاب کردند که تحت مدیریت ایران قرار دارد.
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/455737" target="_blank">📅 21:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455736">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c06ad40e89.mp4?token=tYkq8Iw95pnPwGAO_BJO3c4yHSvs5_hGZKrzHpuFsKpZDZnQxgYsE1pZx9MQXU2jxNtoyAxMCDnb1F-gjfGorJTkpbXbu3w2l4riP7z0KiI_YhpoV6ZfTSB4thFefTesM-TPkQXS1SJcs89a5zI4R6mIRDTBtQ_-WXqN8dMaqhfY-rdRdU_wqo7ehFLayprd2roF6LZdcwy6NbVFon3n1G-LjrJvu-Ucw0_zCpbDQT5WUK0mu1ZHBSnHBAWVQOAuTbKIMS3A0Vx31c3AxrDcTBMkO-KG1UgNI7Mwf72SZqe-tL-cKfWULiJ3yfv9yiMOmRHcXw7XdpWrDNVXg0Wrbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c06ad40e89.mp4?token=tYkq8Iw95pnPwGAO_BJO3c4yHSvs5_hGZKrzHpuFsKpZDZnQxgYsE1pZx9MQXU2jxNtoyAxMCDnb1F-gjfGorJTkpbXbu3w2l4riP7z0KiI_YhpoV6ZfTSB4thFefTesM-TPkQXS1SJcs89a5zI4R6mIRDTBtQ_-WXqN8dMaqhfY-rdRdU_wqo7ehFLayprd2roF6LZdcwy6NbVFon3n1G-LjrJvu-Ucw0_zCpbDQT5WUK0mu1ZHBSnHBAWVQOAuTbKIMS3A0Vx31c3AxrDcTBMkO-KG1UgNI7Mwf72SZqe-tL-cKfWULiJ3yfv9yiMOmRHcXw7XdpWrDNVXg0Wrbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاروان سوارکاران در راه حرم سلطان خراسان
🔹
کاروانی متشکل از ۲۸ سوارکار خراسان شمالی، از روز گذشته حرکت خود را آغاز کرد تا پس‌از پیمودن مسیر ۲۲۰ کیلومتری، فردا در سالروز شهادت امام ‌رضا(ع) به مشهد مقدس برسد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/455736" target="_blank">📅 20:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455735">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15d9f23eb0.mp4?token=UVH996Q5HzQSri46RFqKq6WfRKH005HDmf6bTrm4sUW1-lHE-6MEbi78QOlGS59_kaYSIf6_2krE72ZJGuPrdOAkV5QmygfdsJVL0a7hvtODcGKF3EVu6X20tUrvlnXi4bPJ35aoY-Mhkyq8KRpYUyGRSOGRHOJGshOPWMP3crmGXCpGnf3R3pIHTnCgV7oR-WrMchhQ1bEmR0BN9uuYZn75uLSKEVdag6N3JF7lM0AaKhuSwRiPIjn7azUL_S58AJURvyjfRQABi3cHl2OQCARR6EvnG3IKdMeC7FZVrMgmJvd1TWOznhd6D88add_pqMi6xRZpTHTbSInzZwLTZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15d9f23eb0.mp4?token=UVH996Q5HzQSri46RFqKq6WfRKH005HDmf6bTrm4sUW1-lHE-6MEbi78QOlGS59_kaYSIf6_2krE72ZJGuPrdOAkV5QmygfdsJVL0a7hvtODcGKF3EVu6X20tUrvlnXi4bPJ35aoY-Mhkyq8KRpYUyGRSOGRHOJGshOPWMP3crmGXCpGnf3R3pIHTnCgV7oR-WrMchhQ1bEmR0BN9uuYZn75uLSKEVdag6N3JF7lM0AaKhuSwRiPIjn7azUL_S58AJURvyjfRQABi3cHl2OQCARR6EvnG3IKdMeC7FZVrMgmJvd1TWOznhd6D88add_pqMi6xRZpTHTbSInzZwLTZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۴ ساحل قشم آلوده به نفت شدند
🔹
سواحل سوزا، شیب‌دراز، نقاشه و بخش‌هایی از جزیره هنگام دچار آلودگی نفتی شدند و مدیرکل آلودگی دریایی سازمان محیط‌زیست می‌گوید که علت این آلودگی هنوز مشخص نشده است.
🔹
هماهنگی‌های لازم برای پاکسازی کامل این محدوده انجام شده و پیش‌بینی…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/455735" target="_blank">📅 20:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455734">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hi17i6bhgQkxSujQQfjrM1S8Xx8TUJvkXMfLS6vQw7CGZLW6fC0GDUw6H732QuOt1Mqg3VpJUb_iDvu9jrbgWidKcQBpJTTsEoxbLbMr2t4W0098ZJrprMNcKzyspGrEb9U1ngk9P9pTkdQVXjdZemVosBKm5hdplaZCclROupEHd_lTLiUL6yETwyFByR9HUFRljxU9-XFLGX1rgy_Pa_WuG64mk_OsTrS_iQWFQiApvLHcyKdRywGQC6F6BBUC2dL90VZvO9g6ZhtLZyThgudZGA07jGmV3ORcoGMOQW6skUFSDX1sFAfjIzpX4fear-CrWVoqHC2zkRyDBZKmIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار نقدی: حتی اگر این جنگ سال‌ها طول بکشد تا روز آخر موشک شلیک می‌کنیم
🔹
آمریکا هزاران منافع اقتصادی در سراسر جهان دارد و همۀ آن‌ها را می‌توان به راحتی نابود کرد.
🔹
باید به سطحی از بازدارندگی برسیم که دشمن دیگر جرئت حمله به ما را نداشته باشد.
🔹
ما هرگز جنگ واقعی و تمام‌عیار با آمریکا را تجربه نکرده بودیم تا بدانیم که دقیقا چگونه باید با آمریکا بجنگیم؛ در این ۵ ماه، ما یاد گرفتیم چگونه این کار را انجام دهیم.
🔹
در این جنگ ما متوجه شدیم ارتش آمریکا از آن‌چه ما تصور می‌کردیم ضعیف‌تر است.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/455734" target="_blank">📅 20:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455733">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6484ef1de9.mp4?token=YVPKBtADSssHWvMCA-A4UylnFJcLEBmrF4YrvITpm6RNE3kFIgICR-s71A5aJltMMy-nT0EkOeWDUED-Ricc5RUTh2ZUZJhox94-yaYqW6fuMcTkH0nPFRT4CI0xQIq0UJzNsuwbJCTumfe4-ulfk2l0iPRXKKULZyLRxnmeltFBAibMK4Mgfc6USAJTgNzyr58RfZgt3zNzrMFTW_U3fv-0MbToTbgurmKr9AnBu3eP0bK7a2YitGlV-5meWAHVssokjSex5PE9qnvpdg30oOpQFt66dV0nnwA4xq9d4OoYfV5GFQZoDMswk0hPlzR2FrTTpTky6cVg-kVGDlEiNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6484ef1de9.mp4?token=YVPKBtADSssHWvMCA-A4UylnFJcLEBmrF4YrvITpm6RNE3kFIgICR-s71A5aJltMMy-nT0EkOeWDUED-Ricc5RUTh2ZUZJhox94-yaYqW6fuMcTkH0nPFRT4CI0xQIq0UJzNsuwbJCTumfe4-ulfk2l0iPRXKKULZyLRxnmeltFBAibMK4Mgfc6USAJTgNzyr58RfZgt3zNzrMFTW_U3fv-0MbToTbgurmKr9AnBu3eP0bK7a2YitGlV-5meWAHVssokjSex5PE9qnvpdg30oOpQFt66dV0nnwA4xq9d4OoYfV5GFQZoDMswk0hPlzR2FrTTpTky6cVg-kVGDlEiNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای حرم امام رضا(ع) در شب شهادت ایشان
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/455733" target="_blank">📅 20:12 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455732">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCMeuKKCCLzAVeDz0WjBe2zSf-wdPhl0UAbbmvRdiS9jG-DYewRL6ch8Mi2WY0taayE2797iL3uWk69DhoCXm2bLCR2O3Y-9_yt4IAwiq5d8Dwm5VF7uqSq7xjlF2HvOmf5gdCi0xLVeYG3cI5DPtKoTXHre7ZSZaLEuMyZp-dAH-ppDjOl0vTqQcvrPHJir5bLTwMALy_pHFByFiMMVU0IX7PBR5yNq9JU29XTVJtzTiQF-QYEXxoymPnZwDHxmpv9LR-1fRu8Z6V9FpwSSwP448bs1ybqf69d5zBEaEpDgL3L7WakFhDE_CB_lR2zPeqt7UkVlYshMRqqIvfQbJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دیدار نخست‌وزیر عراق با فرمانده سازمان تروریستی سنتکام
🔹
الزیدی، نخست‌وزیر عراق گفته در جریان این دیدار به پایبندی بر خروج تمامی نیروهای نظامی آمریکا از خاک عراق تاکید شده است.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/455732" target="_blank">📅 19:46 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455725">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kv_UTcXppO4gH03c6ODjMdOi_3W_bZX2Fd_SOjjQWkw-ZTmKd7IR3DMwmN6SAlq6pcVCElmOgQohhVzGAc9T9mq8cqnULHrdS4jjM75AWQdYh2kSrDBYQEkpcZQaZHYBveBhBkEc9fvF-htgI2NXcoLdS3spTJUpwi_e5bNmyhXhx-rTu6K43evYdxq6Rmufe2dSuN7pjAcFWDsr6ro7S2eE2Zm6NQv3t6LQCRBJzxjwo82X-6xfEeMdACsb0nToI15xDNIkaneS74qBCugo4AD8CGM6_E4iGhsJ3uXD05oXrjJHsTgnEabK7kJn-vIQMJvzDrchkvPxwO3NhigVow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y7ILFgiVulhV6QsKmFIgDkt__KRPJKUuWykQaLU5yRMXlERFbwWhioemx2SlNh1q7MuPXcb7-n8bd3rADo82VvuuHmiQ4fIYVNwEAABjEwqIlZlqQMzbbiivKKmlT1otaVp50Vig7o2U8UVC45SNKYGvhWk6XzqPHIiu6pBB98rRWPbO7S9H6pEqzvy6159IJPkTFlFJ0JgP4VLp7vGE3TaIq3QDtLCEt689dIegwUp0jyUFbKmOxE91MF23ggrFxN-J1ib06DhNLMBX6tMFvmPzmtm0YosrszbGMPm1sXDXDjZ845X7J5ue2xnlrzFCfsmmg7B1t7ePOmD0DYd6pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oE3tgE4EdlYQH9mmkXXDkCzP-KkwrUrLzjgUPwjGOd_Q-SheykR64FIGgwGSNEWqUrckXAgqzlTdmVkX_2ctpD14qRi0_7nI5xqU1PYgI9Lrm2XKUGVVhHRuxpZFNvahqvubs-xuLXBBVw5kpQNN23gM7lFLokX2MfnvchxGq7PU7ko86RrNWKNgjPpdi--bdn87QTxscFoSBc4tAnI0nIYARXIQ6yYFfbrZ4jBESSGJjJGtTcAUQGXovCcUPRZWSC08f8FN69_n0kOZmZvnvezb6HXddq4G8LOs1g8nkFcgMOrLm21tfyFcAy2uBChNaGBI5TNzVm1ThDX8mL7f7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/URnDqnJalV2pwoncFZkbH1P_qJrjmIfNI1caXfGfgCGcAdcUdXUGPt3xMP3Dm9eU2JG-ojXQRP1BF8To_u2Llr4nPPvkddkiG_du0892anKuQlu1_uUNv53lbuo_6EN380TUIYRa6ARd08Y_4GU0ciI7aD5QR3uDOT9NuvOfuJjIFy6pvnrQvGgS8BH6e3wXplzb80Lew1sf7Np6W9PdC0LMNhV9Q_jF80K2b606LCn873C3RKx1MZTmmYMiEEPwEZGmQOWoi_2Ga8D8OLgLmGlpM0Krv-5pl-MglKkicHAaeLHjhGbYFvPrFv5YRz-tLrzpGb-TeoDSBAk1-8kx0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O0PRECLI-PJeDYlxnVrK0riixRWF38z0m-5FKp_cP7YIBu8s4rIHoIQzkZyAqlMtMnxp9m_hq2FvI_KYuOvnX4nJACrk406J-yhYOND9n6RKohZqITDyjDdkivmBRzCdAses1JBodT_B1PsSB_tjRSGXHg9yv90ZqfO1Ni8p_OhKT8HFr9gnz_fBaGuVvPy8v0iiMMWV6cUUPcaeKU3urr_eTyvlYKg0BpwtAVVrQ0R2rIRlXjb68QJlzDbqd6AHI-5C4cMoGHAtTPsvhG8zrCOAC5_FevwRErlfrn3wGXR49oKUirbVkK3ZoTFvwPzAH23qSaO0r7xIcXg79yz_AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eO4DBveWaHv9MZ1uqnyJ9EQNuQhcXPy2XgbJUt0nOdMaPCOXVoB_TvgB5dFiBuRbWldKS3zpinvS1cvzcA5pbN7fzxEt2E-9p01eSS9JodpuvhXbF3tUgEwxcYaVYboSzGoKvcARRHi_mdgygdieaM41pUmkdsiO-J4ShGssmVtPdec7EV01WvfkXhY20unISREF2Ki8pnp4r0XG1-XBJlpHRJ6Y2v_QXnbvTHSu1gK-H4Oa1bwUVi9MSL1qTMwHHPh5BUQQ3RTZHlXLvDItUpDGji0yPkA_T6dSFE4l14wn-laduU97dYTCWQQlVcpK8kpHsAJBiqdp7q4zjtmVaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RfOC5YjEcH7ayxV5cTvTweAoWy5rfFZy15CDk3d-yWCIgLV1rvVD0Bd4Ce_BNjv9KUGZBECoFGJOusG0Jj4cXK7zQSeAX_gTzlONTTDChRRDFUEIR8rpK3SBRvZEigZ-1db-OfKtXsKbHi1D_8k8qpSXAv6yy1-CY7OHbJTze773sMbYdp6-mCU0jSNu17Hcn16BQ7muSXT6debXPca3kP6eRa-Ti0M_IQgQAFqI4jDL7sHQSlcaE3EzvsqA-MV1u44gocp1m5EN193EaOE9ce4OuDi0rAWfJYO0s1qZZ7iUf5m9KznLY__xOmG8tz9GMYWOfOTZhD_rdr5uEy3r4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مردم تبریز با پرچم‌های سرخ خونخواهی عزای شهادت پیامبر(ص) را برپا داشتند
عکس:
حسن محمودی
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/455725" target="_blank">📅 19:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455724">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🎥
جاده‌هایی که به پناهگاه مردم ایران ختم می‌شوند
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/455724" target="_blank">📅 19:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455723">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59c3dff57b.mp4?token=hZYBiB2-PxkwZtAN5i0fZxWzi09lz72w3NWvxOH6kzpIUW7rP0ggGWMf-gjs6PagZzuEJGz4YmzNMBvNZutV95U6RTEBLZtxYv1vZ-JXS5x7vQvqfecqiLSkBSuV1sTUB30iMeQ5ivEicocd9FebIN2e76yqiLFlWl8wERoEz0wr6gS7-9fn3jwAMeubUekdC6Yfw_5BousqoW3LGCESYkkab70FF9jgbQLABQx4sOFFqf8tyVoMsq9vP2EZ91yR6X-11t5DuPeeVlTxon_9kwIdTRYCWdw4YAbbpAqOTF1_Or5N-ifonMjgmlCIGpbRazNpdQD0bmqM60RCRkmD6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59c3dff57b.mp4?token=hZYBiB2-PxkwZtAN5i0fZxWzi09lz72w3NWvxOH6kzpIUW7rP0ggGWMf-gjs6PagZzuEJGz4YmzNMBvNZutV95U6RTEBLZtxYv1vZ-JXS5x7vQvqfecqiLSkBSuV1sTUB30iMeQ5ivEicocd9FebIN2e76yqiLFlWl8wERoEz0wr6gS7-9fn3jwAMeubUekdC6Yfw_5BousqoW3LGCESYkkab70FF9jgbQLABQx4sOFFqf8tyVoMsq9vP2EZ91yR6X-11t5DuPeeVlTxon_9kwIdTRYCWdw4YAbbpAqOTF1_Or5N-ifonMjgmlCIGpbRazNpdQD0bmqM60RCRkmD6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فوران آب پس از شکستگی خط‌ انتقال آب به بجنورد  @Farsna - Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/455723" target="_blank">📅 19:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455722">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/141b8c11ad.mp4?token=uuWIyE7RZg4giYhp05a44iEsNdayou2trvjei-lGS8Bewa7d9F94EHQklO4NRs8D_cL_pqZ9uhT5XlJQj5gapLVPPf2fJ7Bem2wncKgMnqzAu5jvMoDZeDG5zNzuKhaio5i8Uzi-ELodtSlBVI-HAdgGrTpRvSVOZ_r99H532fAzt5EzC9uidJXGMU0r9cRBVKH-mR1h2AQsxk8XOz0NxidM-qtemR7dg8tJ-uoRnaN-h2RJw-6IH9StBD2muJqJVNxmC-IDSb9mYIhD1sSpmgj_p5XZ0zqqf7dNVve85HG-yDp39ij7VpEc8pb_l0WICbXwubRkIGo5SPWLuJqEQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/141b8c11ad.mp4?token=uuWIyE7RZg4giYhp05a44iEsNdayou2trvjei-lGS8Bewa7d9F94EHQklO4NRs8D_cL_pqZ9uhT5XlJQj5gapLVPPf2fJ7Bem2wncKgMnqzAu5jvMoDZeDG5zNzuKhaio5i8Uzi-ELodtSlBVI-HAdgGrTpRvSVOZ_r99H532fAzt5EzC9uidJXGMU0r9cRBVKH-mR1h2AQsxk8XOz0NxidM-qtemR7dg8tJ-uoRnaN-h2RJw-6IH9StBD2muJqJVNxmC-IDSb9mYIhD1sSpmgj_p5XZ0zqqf7dNVve85HG-yDp39ij7VpEc8pb_l0WICbXwubRkIGo5SPWLuJqEQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرار کامیونی ترامپ سوژۀ طنز مجری آمریکایی شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/455722" target="_blank">📅 19:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455721">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">رویترز: هیچ گفت‌وگویی میان ایران و آمریکا در جریان نیست
🔹
خبرگزاری رویترز به نقل از «یک منبع ارشد ایرانی» نوشته: هیچ گفت‌وگویی برای تمدید آتش‌بس میان آمریکا و ایران انجام نشده، زیرا هیچ توافقی وجود ندارد و در نتیجه چیزی هم برای تمدید وجود ندارد.
🔸
خبرگزاری آناتولی ترکیه دیروز مدعی شده‌ بود ۲ طرف با تمدید ۶۰ روزۀ آتش‌بس موافقت کرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/455721" target="_blank">📅 18:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455720">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plBX3gU_8J8ooIuiC_XUcSn50o_bWrJGqCdc8nEErnSS5m5leN5B9mziD1svp6qJW_CK7wwNlWct075wf8aXif3o2yzTErZTqmVVaya8GnfRmaLC4YHszTvHO-lpAJHoDbKF9q6Gw2iAbzu5E9WSZd2xTcmtrl_hLTeHJw4I3N3OJy5TXnJ1M0lMIRynLnkD0Us8WIxup_1btT8X4GqlUcCZ3wt_AQ7sMKYVS6uT5Y-vhfH2-TZdn9QXhHiT5pBd4uqO8_gZ1melscZCsG35UM3vPI4lSlxIe5pTT6nI3YC5nZPiWeKCJEXDKUlcemNwPm1ZSmGCRzRNX1mVNvEkZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راز بیدار شدن پیش از زنگ ساعت
🔹
مغز انسان یک ساعت داخلی ۲۴ ساعته دارد که زمان خواب و بیداری را تنظیم می‌کند و بر فرایندهایی مانند دمای بدن، فشارخون و ترشح هورمون‌ها نیز اثر می‌گذارد. نور محیط، به‌ویژه نور صبح، نقش مهمی در تنظیم این ساعت زیستی دارد.
🔹
وقتی هر روز در ساعت مشخصی می‌خوابیم و بیدار می‌شویم، بدن به این الگو عادت می‌کند و مغز می‌تواند پیش از زمان معمول بیداری، بدن را برای بیدار شدن آماده کند؛ به همین دلیل گاهی بدون زنگ ساعت، تقریباً در همان ساعت همیشگی از خواب بیدار می‌شویم.
🔹
این ساعت داخلی با تغییر برنامه خواب یا سفر به مناطق زمانی مختلف می‌تواند دچار اختلال شود و نتیجه آن خستگی، بی‌خوابی یا خواب‌آلودگی در زمان نامناسب باشد. شناخت سازوکار ساعت زیستی می‌تواند به درک بهتر و درمان اختلالات خواب کمک کند.
متن کامل گزارش را
اینجا
بخوانید.
@FarsnaTech</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/455720" target="_blank">📅 18:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455719">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eboSpMHJMW9xz-tEZRItFoflVF1lpN7hgpmjpauRKG9i4V_aHo-2jp9HPCWXE5vx2hcqY6FnYjdeUbk5dcLq3nQFJkMGW7PcYho1gBpaAhFfoFhwnJ_RTWShdzGkjWSPCLxAh9VC87eeAK9sFN1XUP3IMedWqcTywGG37a8lc6KtheRgBs-awS90glwjdPs2dQ4bXdq-B2R5t-4YbEKWF81tx4d3phEqZrgKjATIgB7RELinHxEFrIxCzN-d7MVAREfDoOTqzPH9OsdI6XXQAWNPgfsQy1YMBNC8IBxXx4EmtnOugxfRHXwLb_7O5yU4sb-XaePV1pLfGkRTcfesJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دالیچ سرمربی جدید امارات
⚽️
زلاتکو دالیچ سرمربی کرواسی در جام‌جهانی ۲۰۲۶ که سابقۀ نایب‌قهرمانی جهان با این تیم را هم دارد، به‌عنوان سرمربی جدید تیم ملی امارات انتخاب شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/455719" target="_blank">📅 18:23 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455718">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a7eedd60c.mp4?token=Q_J62PpW2Z7K9f1MxLMlG51B5PhMdkKov_54L5XfPR9_zCPTsDkwC9Ax7Lb1tVMXP_u1ulzXnvx3e9csFT9RtJit2wQnIRdCUulykALLCO76EWr7jJm1-bCs-Iy1W53sahx4l_abN_YY1mdCcIk6ejbAwdhN8IllTfTeXKyYTOrHNYCSzGiSb20L2qbOiy0Z59wBSrnYQ5yM_3srImawSUe2ySr1Twf70j3XnRafA_s0TnyLkhT0wfUUZdPMxPmCMZbuWcNxps6iD3TqnwCN_acM3swAIGUzT-1ktcvh45h9CpJpnbcRK3WXoOJHj1MGEJTeaYwGBDdlbYiTnE0PDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a7eedd60c.mp4?token=Q_J62PpW2Z7K9f1MxLMlG51B5PhMdkKov_54L5XfPR9_zCPTsDkwC9Ax7Lb1tVMXP_u1ulzXnvx3e9csFT9RtJit2wQnIRdCUulykALLCO76EWr7jJm1-bCs-Iy1W53sahx4l_abN_YY1mdCcIk6ejbAwdhN8IllTfTeXKyYTOrHNYCSzGiSb20L2qbOiy0Z59wBSrnYQ5yM_3srImawSUe2ySr1Twf70j3XnRafA_s0TnyLkhT0wfUUZdPMxPmCMZbuWcNxps6iD3TqnwCN_acM3swAIGUzT-1ktcvh45h9CpJpnbcRK3WXoOJHj1MGEJTeaYwGBDdlbYiTnE0PDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بارش شدید تابستانی مردم کهورستان هزمزگان را غافلگیر کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/455718" target="_blank">📅 18:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455717">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">احتمال کاهش کارکنان سفارت آمریکا در منطقه
🔹
سی‌ان‌ان گزارش داده که با تداوم درگیری‌ها در کشورهای منطقه، واشنگتن قصد دارد تعداد کارکنان سفارتخانه‌های خود را در منطقه کاهش دهد.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/455717" target="_blank">📅 18:07 · 21 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
