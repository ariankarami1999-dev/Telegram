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
<img src="https://cdn4.telesco.pe/file/Zeyo_gw63NrJL-D2cnB-jjsLj0E_jYIiqwWYjV1n2lYABGDW4rHIMGYl9qsKaEcqQ_25sGlbMBvx0oVl5lpN70s3vg4bJrW2XNS4vk5wOYYo28qhH9mPx8JqkKchdvmZiF82rL1QzTpnDB-ISjmLBWEklv-DTHowhV-boUEo9VoDV6gq9n_ONI15HgudInbpRALQT3Aa9W8RV0hu3cUx8alCePVOphzIcPCMVK42ppU4Rss0V-MD5MCCFRu-lg2fYiOTbHnbTZS5MZAxHs6yuL2NFk-Ab7mysuOHa7dejp0NFyWjJxC2CzsEgzmljgxNGLN35Q0R1VYiWyORMqNVEw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.32M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 15:32:33</div>
<hr>

<div class="tg-post" id="msg-672139">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
دو برادر معلول در حمله دشمن به پل نیمه‌کارۀ بندر خمیر شهید شدند
🔹
استاندار خوزستان: بیماران سرطانی و تالاسمی هنگام حمله آمریکا در بیمارستان حضور داشتند.
🔹
سقوط پاراگلایدر در دماوند، سلمان عبدلی، خلبان و مسئول ورزش‌های هوایی سمنان درگذشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/672139" target="_blank">📅 15:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672138">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb3be02fd.mp4?token=nt8d0X_wmzC04_VvTRFk3-spInx9JRXkWcmvfzXqNCpNTiKDpwjoyxu6DltI_e_GlHN9_g49DpQZqmhFhs0wbHbyM3xkWL2KWrP_Y3uiHzJxHdfHqTdoya79ltvx-hYANVKuLjERo1Q2N4llgnoCXAmIje1wVJ_w4kfa-HBfapRucgSVwiciyV5k9pGtFmqT8O0pTpmMuPK-GajsqObrln9bFhjSlL69FDpIRMiJv4t0NkdqbowZ7zHHKfoefczIvIvXSF6k2GI8zBTyfJKWJxlKHp5Z2VN3I6WJUIICdZGt27HQ_xjlXwwz9afasPNGK8yu_u3CuTBtbUVrAyui3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb3be02fd.mp4?token=nt8d0X_wmzC04_VvTRFk3-spInx9JRXkWcmvfzXqNCpNTiKDpwjoyxu6DltI_e_GlHN9_g49DpQZqmhFhs0wbHbyM3xkWL2KWrP_Y3uiHzJxHdfHqTdoya79ltvx-hYANVKuLjERo1Q2N4llgnoCXAmIje1wVJ_w4kfa-HBfapRucgSVwiciyV5k9pGtFmqT8O0pTpmMuPK-GajsqObrln9bFhjSlL69FDpIRMiJv4t0NkdqbowZ7zHHKfoefczIvIvXSF6k2GI8zBTyfJKWJxlKHp5Z2VN3I6WJUIICdZGt27HQ_xjlXwwz9afasPNGK8yu_u3CuTBtbUVrAyui3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منفجر کردن مسجدی در جنوب لبنان توسط ارتش رژیم صهیونیستی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/akhbarefori/672138" target="_blank">📅 15:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672137">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a81372c62.mp4?token=hUpZCG8jpdmgQ0OWzm9uY4IJOQvQC-6SNl6fzBFAz5sqw9hbYcd_b4V7-QDOIKTjHU_tCk0ziFuw4Q-8LYEXODPm0H7zCjVLaNOBO3mLlD6bs9QzdRFqnRQ1deNIY1Qdoaau0h-LkqPohYqL9hr9aqVT6rAIrI8o8BSpjKS1N6zOfB0ly3dpHUiXEd3zp1aqFZFM6_YvD_uXohpMmxbKap-gB_ex34llO254vp2RwsoEcWKN3mek_crntYyhgn_d-4W-TaI9mOn5tdirEw7OlHTWy3S9pAq75b7mfjvioX4-P8ivartme85vTnoP3GjpRv1ohn9kBqi73M4j5r0Mew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a81372c62.mp4?token=hUpZCG8jpdmgQ0OWzm9uY4IJOQvQC-6SNl6fzBFAz5sqw9hbYcd_b4V7-QDOIKTjHU_tCk0ziFuw4Q-8LYEXODPm0H7zCjVLaNOBO3mLlD6bs9QzdRFqnRQ1deNIY1Qdoaau0h-LkqPohYqL9hr9aqVT6rAIrI8o8BSpjKS1N6zOfB0ly3dpHUiXEd3zp1aqFZFM6_YvD_uXohpMmxbKap-gB_ex34llO254vp2RwsoEcWKN3mek_crntYyhgn_d-4W-TaI9mOn5tdirEw7OlHTWy3S9pAq75b7mfjvioX4-P8ivartme85vTnoP3GjpRv1ohn9kBqi73M4j5r0Mew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاوی تصاویر دلخراش
♦️
موشک‌های جدید رژیم صهیونیستی پیکر قربانیان را غیرقابل شناسایی می‌کند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/akhbarefori/672137" target="_blank">📅 15:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672136">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ed2a9082f0.mp4?token=lQy7oe0TyeuQhWmywEyOBUqbkLWenwiKsctWUyVlubvvp4-Rci9n69caN_cFcr6v8eNf4lTPYVmomsQVA3wsF-8S2LnrwMob_jEc-0VQGxv4yeEuiVD1pwm6Wu-q5g93SRZqX6g4G8HXRSjrInAEiMGTtEfy9ZoGI4MPPdV4qUWMU_CAUxd6Q0TpgKuJOtHnThkWLNeJauNFEX6N6lpWKQCZdjMoAfamZucXGczXLsHHRhiEzBHzATUSbIRLXLHu0j2MWZkz0efud5FMz04rkqyfiTvGl9Ju32vGRak4qbRmYWjqQqP_44oz_LCOW_sXQYdu5qad7swCTqjGc9lmVA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ed2a9082f0.mp4?token=lQy7oe0TyeuQhWmywEyOBUqbkLWenwiKsctWUyVlubvvp4-Rci9n69caN_cFcr6v8eNf4lTPYVmomsQVA3wsF-8S2LnrwMob_jEc-0VQGxv4yeEuiVD1pwm6Wu-q5g93SRZqX6g4G8HXRSjrInAEiMGTtEfy9ZoGI4MPPdV4qUWMU_CAUxd6Q0TpgKuJOtHnThkWLNeJauNFEX6N6lpWKQCZdjMoAfamZucXGczXLsHHRhiEzBHzATUSbIRLXLHu0j2MWZkz0efud5FMz04rkqyfiTvGl9Ju32vGRak4qbRmYWjqQqP_44oz_LCOW_sXQYdu5qad7swCTqjGc9lmVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حاضری برای وطنت اینو بپوشی؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/akhbarefori/672136" target="_blank">📅 15:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672135">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
آرزو داشتیم به نجف برگردی اما نه اینگونه...
🔹
قاب‌هایی اشک‌آلود از بدرقه‌ی پیکر مطهر  مرجع تقلید شیعیان جهان، حضرت آیت‌الله العظمی شهید خامنه‎‌ای توسط مردم شهر نجف عراق.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/akhbarefori/672135" target="_blank">📅 15:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672134">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZ2Z82n7Fp6hmYlmXX_gbNKyUTV6nzDSIvtbhneawjGPTh9EMAUhXeik8GGopVKGF3mP2wXrN8TJtYubGZ6PLQCklNXuGeZMf3oZlFBj0UyjcNtLNEy47Nsf16xpotWYMvMYO4PDyv__qihF2T1gTUTqxo0Ie-z8X6smifBWWpkKvXlAtHZI9Knq5K1jpzp10ghOTw9PpJibccdjrrT2IxjQoSjBBQIjyKeROQoQtmUN_s1Zglqqtp8a4RTHJzsNY2EDuHz1gNPMv3cTi_kx91BH8jWaVT6JlO9w1DwUpJqFiBAbn0kP-RcX5e0ZhGBXRcjdvdAGDS-t-_XN51PVEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نخست وزیر جدید انگلیس معرفی شد
🔹
اندی برنهام، شهردار پیشین منچستر بزرگ، با کسب حمایت گسترده نمایندگان، اتحادیه‌های کارگری و شاخه‌های حزب کارگر، به رهبری این حزب انتخاب شد و قرار است روز دوشنبه جایگزین کی‌یر استارمر در مقام نخست‌وزیر بریتانیا شود.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/672134" target="_blank">📅 15:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672133">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KtzJ3KietRUyMrJXn9hs3rEZHdPE_fLZLIQRq57-PHjjG-efPAzjzbUsQvz4nEJjd9nRPWIjcmwG5E4vfKMVOABwgSvPhHRdf1bKlvoa_-RdGigOagfQGb8q4g515A-MjNDIm-zYaSIs6qAYh5_AEEkbhLkRE_fuWSZkq9yUwIRRUyNBTu1k9C-5bUbU9xq0LCzTkIin9lq_xANXBiOBDch-yKagFezbplZL0xp4yyjA7ywnudCXwH66BuiUIA22UxXkyoJqrupGZrGV9bO5ur4PRMWk9UFY9peUq5bcabTHV02KsF12k24IMiMm9_e1AicIHKedtQv7ZqC7ngBrRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کمیته وزیران امور شین‌بت تصویب کرد: سارا و بنیامین نتانیاهو تا پایان عمر نخست‌وزیر تحت حفاظت خواهند بود
🔹
وزیران همچنین با تمدید پنج‌ساله حفاظت امنیتی از دو فرزند این زوج، یائیر نتانیاهو و آونر نتانیاهو، موافقت کردند.
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/672133" target="_blank">📅 15:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672132">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
واکنش علی مطهری به گزارش نیویورک تایمز در خصوص احمدی‌نژاد: احمدی‌نژاد دیگر در جامعه ایران طرفدار زیادی ندارد
علی مطهری، نائب رئیس اسبق و نماینده ادوار مجلس در
#گفتگو
با خبرفوری:
🔹
آقای احمدی‌نژاد چندان پایگاه اجتماعی ندارد. عده محدودی طرفدار ایشان هستند.
🔹
اگر هم بحث آلترناتیو بودن احمدی‌نژاد (به ادعای نیویورک تایمز) مطرح بوده باشد، چنین تصمیمی درست نیست.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/672132" target="_blank">📅 15:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672131">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/988241fe78.mp4?token=aXNsaGbg6zA8CsVwnjeKBoeFcOO9k3g4S1hC8Ous29NI1-xyUqVI2ahqWVAYshp43IGjfGzaVKTyjnE_EygzQJkYfmlPVFN4BxilTkeOmtp2ciNvLMeQ5qyUpXBMXXVMYwpQSJdCBVXcm1zTLRDvUYqIe7JobaXMxpkRsw1VJHAOoVIsV6NvHF30AGbeH26G4zsDWWxumCPyv8DPwLbbpzCJoQLuOCq7ZUTbEHxVVlccWFQdC3cR-G3yzjuaucr4JFRpnQsti_A92PBtD2qUt8vWiy4VuQ3f3XEV9R3WeHsBFeGk3w4FwFrJ9cJkb1ncMgpBOOoSuNc2pgjYGB7-EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/988241fe78.mp4?token=aXNsaGbg6zA8CsVwnjeKBoeFcOO9k3g4S1hC8Ous29NI1-xyUqVI2ahqWVAYshp43IGjfGzaVKTyjnE_EygzQJkYfmlPVFN4BxilTkeOmtp2ciNvLMeQ5qyUpXBMXXVMYwpQSJdCBVXcm1zTLRDvUYqIe7JobaXMxpkRsw1VJHAOoVIsV6NvHF30AGbeH26G4zsDWWxumCPyv8DPwLbbpzCJoQLuOCq7ZUTbEHxVVlccWFQdC3cR-G3yzjuaucr4JFRpnQsti_A92PBtD2qUt8vWiy4VuQ3f3XEV9R3WeHsBFeGk3w4FwFrJ9cJkb1ncMgpBOOoSuNc2pgjYGB7-EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنایت‌هایی که‌ آمریکایی‌ها در هرمزگان انجام دادند
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/672131" target="_blank">📅 15:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672130">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95465ecf3a.mp4?token=IjtGll8iVxgrsS-XFd2Jr_8x38gEl6NgXzvHbxj4o8am5E3vxl1sdVFCb3jBYskomkq1JwaXph7jONWYGsYNuKAMHcnBfDLIt6wGyTQw0Mop1xj3GkVQOwpwguekdravTi4Dmd8_BU4AmNIRvIm0ZFCTe9Wnc7c9CzdxD4UIodLlVc7xCl1vMPnVCfDqxtHsGWEmpAsvF082z-7KoahWfmRceg2kkZmroTNBXTH1RgztWun76y-pqgstFj5A0TBGIQfdGTt-yiydSQrjFdvYltFaxHsxHKaXi0I0yNkJLmRgTfcrEMTbn3B7mEJ_KoZ6AbSbJQazJlZ6bwj6qGP4pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95465ecf3a.mp4?token=IjtGll8iVxgrsS-XFd2Jr_8x38gEl6NgXzvHbxj4o8am5E3vxl1sdVFCb3jBYskomkq1JwaXph7jONWYGsYNuKAMHcnBfDLIt6wGyTQw0Mop1xj3GkVQOwpwguekdravTi4Dmd8_BU4AmNIRvIm0ZFCTe9Wnc7c9CzdxD4UIodLlVc7xCl1vMPnVCfDqxtHsGWEmpAsvF082z-7KoahWfmRceg2kkZmroTNBXTH1RgztWun76y-pqgstFj5A0TBGIQfdGTt-yiydSQrjFdvYltFaxHsxHKaXi0I0yNkJLmRgTfcrEMTbn3B7mEJ_KoZ6AbSbJQazJlZ6bwj6qGP4pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پهپاد اسقاطی لوکاس امریکا، نسخه فیک شاهد ۱۳۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/672130" target="_blank">📅 14:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672129">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رهبر انقلاب اسلامی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ViP6-rTQ5dGK-3GfmHRjzALsywu-NFKnf1V2p7V55SewdFNy_G3WJMXl4iDSc6PxwGrhI85aYA2nSBdFTN7f7sjKWSPFyAAItpfOImQG2WVtKC9xcuFhwdZqovsAqA2tilQ6IqdqPNAT-ouUM6v5ziBCxhlPca1ars8L6skUCsvesjBcQM5Xc-Wteeh_QbXiMLWyvkUbv9t8h89GvnmpPJ9J44H-dSOMOc18ABkTsCwYITWOFHJSaNw3ZLnhXkaULjWNTED_kVc3ia7jNtaqp1xj27bgwx8mUAqXOEcj5swiAGCdDt6yLztcUVXl5vbpiA2OWm-6_38ZBw8p947ZWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📍
پایگاه‌های آمریکایی‌ها در منطقه باید تعطیل شوند
🗒
ما با پانزده کشور همسایگی خاکی یا آبی داریم و همیشه مایل به ارتباط گرم و سازنده با همه‌ی آنان بوده‌ایم و هستیم، لکن دشمن پایگاه‌هایی در بعضی از این کشورها احداث کرده تا تسلّط خود بر منطقه را تأمین نماید... من توصیه میکنم هر چه زودتر آن پایگاه‌ها را تعطیل کنند
✍
بخشی از اولین پیام رهبر معظّم انقلاب | ۲۱/اسفند/۱۴۰۴
🖨
نسخه کیفیت اصلی
💻
Rahbar.ir
|
📲
@Rahbar_ir</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/672129" target="_blank">📅 14:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672128">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromوحید یامین پور</strong></div>
<div class="tg-text">"نه به جنگ" گفتن ساکتان جنگ رمضان  در واقع جبهه گشایی برای تجاوزات اخیر دشمن است. اینها پیاده‌نظام رسانه‌ای دشمن‌اند. دندان‌هایشان باید خُرد شود تا به‌یاد بیاورند جنگ را دشمن شروع کرده و ما در حال دفاع و مقاومتیم.
@yaminpour</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/672128" target="_blank">📅 14:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672127">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9g4SAWFnAps8gnb3cDtBblKD1WZwq5985o7-DMmtAtuGn3dy07YjOY93o7ev2NtShoJ-t6rbIyyTZAtb8FHzvROtsWyIaTaX8lgIiUUthlvLYS_OGMJCSZ5lAQLukE9-uUSL24lypRdczbkqhhItWym8EsY8CdzdjLoGTrxZF_pRswSSPTKKjF-VRvCqPnRnVg3yKl_6HzAejTwUiWvEWoag4PAzwsnPE7KHM2S7iGjvWarX0p7C9Kvc5mBJZZ-g0Y-5SJz82W0qa2aTNZ3PX2fYWbcz0d7d6hqbpfCC5y7KkXwqnGlKXMqqwrhejgsaXSU_-nt8_vFbqw-xdKYjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تصویری از کاپ قهرمانی جام جهانی ۲۰۲۶ در نیویورک
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/672127" target="_blank">📅 14:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672126">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
قیمت بنزین همچنان در حال افزایش است
انجمن اتومبیل آمریکا:
🔹
قیمت بنزین همچنان در حال افزایش است و به دلیل وضعیت تنگه هرمز، قیمت هر گالن به ۴ دلار نزدیک شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/672126" target="_blank">📅 14:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672116">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T-yfiMkObJUnNrxUdteAvfIWw-CTI-Ege5SEimRI9jvYicGnL1onFapaRZFAKV1RkwwSY2lUYNeJhe6hfM0chTsedKeFBXAI_RI_hC2RPf3cPm9_xnVLduBocp_cuh8yIA8TIPiqqaJC5w6X2EHAsiNZyeYxYhXPzFkaEPoZzYyArQHZmCZswtCYHAhW2oLgqpUBG_-dng9WUBEMDi7zF7Yq0Y_OIzhpn7U5fWLQwU_TOK_8L5m7LJ6haJ-IeOMFnr8bWjYz6eqbUV27_HjFX77JorAeoFbEvWGcV6NfEupwKLKA0qs7DVVHa_O4G-FTb794Yru8RPB4yXS3E-2STw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lPp83XGcE-6EYGQ3iSwguFxPVnkeBoNPU-sy1-H44qr6fWy_A5VdE--oz-6ZXG2HxZW2_mo3F7ciZP4OjK5B162U5aoUvWysC8ZYYaVVRIPv49I2wehRgzn8exGrI0DLuz8wqwsrpJSLm7rAUhYai---2XI4cwtFX98fpGJhJBUKnJAykf3UzrM85yJgm0PsLon3G3IEFkS2dSldPURE6X4BXEm2a_Sryb93q3sMTG9qfptoUqQWIaqzQveCxq9jOOSMv6RCTUhp-bIinydNxyhXtcO3EW1wPOzJwjJckrRwVMZreMQF7MRKCoeKsAoX2PtyINGP8pv1MzxOKJntUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ESr2OF-5swkRSZcxjyAVlNz0ViBCbP41YP54WZ1KLT32kcaHUiccRpbEUglyzQqjzK2SciDYSShL5MydCaa5b1EliyDieUzFEmtBVfDnMFuhKVoQ0agl0mMei2RmfpNAz72_6g9ccnNZBkEV8Ccle67PRtDjWITd3O5gIXVO_7w4JCDPH1XTji1UwnsBiBn0A-_d1ZJHCmk35yFJda4xK9cczvbnhEbHjD4tbAT52fr2jpLHKnFo0T5ch7MWr6DBrKJ5Ys7KmGYRVvZSjks_JAAug3w26UG0KYROp-VzO7Z5Qq1VHH-qqfrk2aK29vsBrhXqzoSew72C207DyX0KlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A1e_Jf3Xr-HlTSgHyAqs4OyT_c2jFjCfamO2NybM_eecQmubR2Nnh8b-Zse4tcfow_vOOgiaxeOL6qqLgj30_GFTxAM5ai7gXfh-D6EmGtUdb5tMtGAjDC5eMYAyZJHpTC5su9-JmbItNJuK2x47usVmC735IgUyhopfbEgyB4U-ZV_q6omd7Ia2AgkJ1TqzFGzxLOYSS7f5Hglq41BMWfD08XDF1GAhtWxRgfOP5IReF1WlQGcMPNVtZGmxr-yH0W-yhaNZH6CVhZ7fN_FESJeHpKMGRquq1PM1I41kfykq7TLGWJFhssRV8Vv_lXqNWaKUfCSmzz76wbRMvc1Ihg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jPBJfARUyfyTDWw8Wd4mF5qi9aez0HM_SYbhBJCgTmYYpA0BDT1Bgo-pX2jeZFO1mF2VI6Fl_rxEEkJXfAUQCe3RT4qTM3bZPp0Hbdv5n52cJFdOABhG2cp96JwZF0XarmDKnWnGY-2dBgc4yM6ER1vhQb5v2ud5UD2rWp-cC8REu7odXyh1JiMh3tM33Ryzk0m4xlInL6qfn2UsTVj7O51wQjGgSuGunozR2nmpidn302irZdHrTk7xYy4Ll0LekZAQVSaDntgwMyJOVWyCLzFxQC3HdhVXjuTq-xYhrotvdlAW4fKN21Lcexxgjr5AL2PCixPq5fllVfkllpUEgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rVeYAb-EI3gDJ7V9IdwaDrUUuIuAoodTw0OE0mxxz7PEhUwvM19bD82S7iaXieASWiIIfLxqL6B2ZsLEV21-RIdAA4K-T6iri-YD4KTd4ayLLFfyq7DGcOtK4LVH2EcdnZeI0rMMYP2OYfe4GDzmoorCmhYc4QXH1TDasFTnUAnOZpk4-pq3lRGXvN27hm-ykSnYtXstB6wyNCKOKJsc0lwWft2Mww44JamClO3_zvlFuOyu8LBmM99jCqpFWiLFfT2DOZLifnpPk6dftJCtMAtccBAmjixeARlY7xazWwE0Y6bISGcul_uDmNjcZfC7Ucozq-ZN4RAYCJwqP61VjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ERPGWfRAGlcD0xgEKX1jd_5_I0PYE-Cg4tLcKqy6as862w44e2Kl1uVNodO_Bntyd9EGWVw9xCcH-lcJJOpk8Hn-U_s78PgX2i2oXwVTF-pklsk18PZVFPLaPVB3SV2JaiMRAT21QYocyNmEOfNXOjutneloWR5Cqpm4h-iXxIKV7rS-8yu5_LTM_DtdwbVH_DcP1jpqi0yncwN1I99GoYQxu2f1k783auN9bz2YsobxDExKkskNnnlIZ-k0oWh1pBv6J-1HcYGmPVP1EpK1Rb8ixJ8ujKs4_76Nm5wzwhGUZMXqUEYnG95eZy1wWbFrId3sJ4RC-V3pjbHyMFI-Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TPZHz8YkndHEtjGkuzFYTP8s6OMnr4-lYIri_wqLzn69TV8G-SF73LA1cetwH8RksOgR5NGfdxPjcn2cnbAQA0WcBbaYn95bHJHj_KTs_nEGPlDCBmWD1DsGSmA8kANja48mAT_L4aE55P6Xh_ECmEs6DSfF6WI6LzQHHbPuzgWw6PztnlWRhYmijlB8TW29y8ZR8UvJML3Ns0gEV2HGtZrdtIKXnhSHUm6ap5MMegbsqBmLpDeb5BGD-OyTzTolIZmhvAjxXoWxH6EmNB7HGhEx2MH1ynHah9aVBpjeysSmSHQyk3wRWqe5HWyS3QO8sKh_AI1e2h0jPbjKgD3J6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oFIUlhgaedH9KHWV8YZ_qUF5snjE3OdpFEOFRfM9c9nFuwnpsPhti6Ii0XPc61pVt3uPlvvr-_PwOZG7ZommNS1rRXcXOeAlYwm7HU1zBMUwhWzgDhWTQ_f2y7dzlwxqhyuTHdN8UECVfKUeTh9Dx642BMy_CyhZA5eyONEdjHKrRcgWWLoCNOgZnQJjJ_ky6Qb7CNk_8Hs4DgZ2RPTGqy2xtogXpJ_Te8UTCz-gXoEPiGxjQG_kLmpXAAnpCHGFDWtfKoKTr26ygsD4Q_9Djdzg4p7sgzlJ5cmzBD426v-UcME97xtqoO_hpvwZxdnA5nLYxyaKPQIvAmse9wPVeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D_Wrl6VJKQxX-_mqvs7puKYbStAqhSPAiNZpDAng_T3IyjW8X6ddOJ4TdiXWGMOkPrPlCE2TyYSvnBY48pV0-4kds62jAqjvsiCe1vIg46Dc_RvH4XstqMaA6qs0IyZhLFaJaZ76ehJ228ufxqzX90x-aHF3RjEZ8w3BQtrCpK_oOV_5cmeUdexWVdID-fKMDcvlr7HnQ9uh7nP9-PeBCzTfO3KA5C4h6Wxn7H6C_7V9EjzrG6Oi6dzHyMefzVqka4N1MqzpQokgNKdw-jakA5u65XQjGiJioE_jEL8s5gDSoo1MvlS-seBA_nz1r532pCPa2JfgluKO-w4S1wCmHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
روایت‌های ارسالی مخاطبان خبرفوری از قطعی برق خارج از زمان اعلام‌شده
🔸
الوفوری را دنبال کنید
👇
@Alo_fori</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/672116" target="_blank">📅 14:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672105">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46817c70b6.mp4?token=OqEC5lJGrDnpSI47rqb5BUpRnUwXjHBVAE0Ig7rnAv80nRGF22R06Z-0LqlFMGshCUTykDy2h4OqPZW9rtMWcYkrzKRNbA3ISqSdLdQQ3104AqhXeJ1LkpqsEWpLaKJShsOOBlYXtLZ3Bt5N24t4vuTuQmoz9Ig6o5QBZqcEtUfrZRU0kh8Ybh0zH_PkicJV-0IyLoPDsE0tEYyNHVcRe7qaWmaM0DoZOG97PWLCRj9CMjUeF4DhPH3cOa9wHlTm8sBaXoojmsPZXwDEGQ6Rvp4NYrlHeqHbAkdWNP8a3tWLegZqXGDupcvtwE-nND0Uv1yIuVUecG_W8XdfG_bahQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46817c70b6.mp4?token=OqEC5lJGrDnpSI47rqb5BUpRnUwXjHBVAE0Ig7rnAv80nRGF22R06Z-0LqlFMGshCUTykDy2h4OqPZW9rtMWcYkrzKRNbA3ISqSdLdQQ3104AqhXeJ1LkpqsEWpLaKJShsOOBlYXtLZ3Bt5N24t4vuTuQmoz9Ig6o5QBZqcEtUfrZRU0kh8Ybh0zH_PkicJV-0IyLoPDsE0tEYyNHVcRe7qaWmaM0DoZOG97PWLCRj9CMjUeF4DhPH3cOa9wHlTm8sBaXoojmsPZXwDEGQ6Rvp4NYrlHeqHbAkdWNP8a3tWLegZqXGDupcvtwE-nND0Uv1yIuVUecG_W8XdfG_bahQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله مجدد جنگنده‌های آمریکایی به برج مراقبت دریایی چابهار
🔹
صبح امروز ۳ انفجار شدید باعث وحشت مردم منطقه شد، اما منطقه مورد انفجار مشخص نبود. جنگنده‌های ارتش متخاصم آمریکا ‌برای سومین بار طی روزهای اخیر، برج‌ مراقبت دریایی بندر چابهار را با شلیک سه موشک…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/672105" target="_blank">📅 14:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672104">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
سپاه: حمله به مردم و زیرساخت‌های غیرنظامی تاوان بسیار سخت و بیچاره کننده‌ای خواهد داشت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/672104" target="_blank">📅 14:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672103">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/msbNhsPPQwDcx4wTKOaoHVTkyIFaQR_H-XEtQe3kS1-SclAam_qhGr8jicstccLuxq04tNxA4dy3tT6UxmZ1Z2FD63Ec7OfQyyF5LWlA_M5lTEcr-sq93jA0Z5qkryWjumHFdaiGlvhsPkORUL3iWLKqQo9cBgqhJ1WH5cl78OBLcYhAmQJ7Isw8DsRDW6NNOOMX3ouxAJFuKkXSGMjUT3_DGGGq04CYLBSEvNu3xPpj-pMj4AnwdAo14FrzI2xURTZEuSDvIdljmmQc4YlxBEdz9Zvu7k--em6aGoNBHUFC8Cd-xZt1EjU_9gIlhMbUs5qLcD5xNoPXGC_E632nyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افشای دروغ‌گویی اردنی‌ها در رهگیری موشک‌های ایرانی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/672103" target="_blank">📅 14:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672102">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCzUARU6Qkqz7zg10OYGmpUjV0lX2wuJHl0mx4_LPzQFawLi9r80YPF-qQvd-wABWVEaq25bYs0L9Mc36bAI9mYb3BibuM907immUkm050FQu0fyb7ReHWpfJZ_M4g9kWZfd3Pzva9Rx2T-8N5VSwgIgTD8-zMeoRrxhZW4M28vEoOsowQOWQw2foC2ESXKyvYecy_FeEUWqKw1EFS4eVq0QSAv_F1mBjPxalm1Lb_nP3ZfmAoVKZXMqfBkvT6HMrtArRAQgMNUaU3k0zFHhI5-ssHd-HZ--UEQ5qZYFub5oF0776YYhcfdKCw9MkAJIE6YkAOwEPfi71pw_6V6CSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میثم ظهوریان، نماینده مجلس: یکی از عجیب‌ترین و غیرقابل دفاع‌ترین تصمیمات کشور بعد جنگ رمضان پذیرش قطر به عنوان میانجی مذاکرات با آمریکا بوده‌است!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/672102" target="_blank">📅 14:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672101">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/coMgGJFvB0cnD3HDpv-qQ4xhQ-SMFkq2-ZokuVVz9vA_JtNFBfxFKLTub7Y-xNCPxDXwxpamFjQ3QlXq2Wviw6GUixRtghzu-8o5Id2E82pp05_mM182_ZfZ_6ZGLO8rLp-EfVBSIkI9q2gHNg0kaQCgzYpiFLFlExX-v93dUy9ANw9SWdftUfjoXuYT1HBK9HhXtuXv785SV9QIrMiOYtJlidy1HSbihVd3a-O1hdTfKVr4YIQBTDiRw2MO-DzQFIiemIkg5Aunoldn4ZnTXBrG3PIrMdO7_0lq9hUuCzUhuRWopGUR1Iv_lRouQk-aVziJhs7MtxB9_mAuAbmz9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حادثه برای یک کشتی تجاری در شرق بندر الدقم عمان
🔹
سازمان عملیات تجارت دریایی انگلیس (UKMTO) اعلام کرد گزارشی درباره وقوع حادثه‌ای مربوط به یک کشتی تجاری و نیروهای نظامی در فاصله حدود ۱۰۰ مایل دریایی شرق بندر الدقم عمان دریافت کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/672101" target="_blank">📅 14:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672099">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AF14xEPYA_gyrl3KE3Wr5X3u9Ndj-5jGkOzUD__CXTsG1F9YFDH4IO8HthJJF8UX9XjdxipAAt6AxIvvh4y8VSaobTJDMIg1aQxIm_dSZP4R2xDMAevaHCpJrADlDtNu9yiTFhlBkGlt4gce1t_LG947NhkUk5ZChQjKUfUfKvvEAgkqU8DQAvePVrTIicLbUZht0yCbGcrrimdSordrVlLlE6IbwcyCWCjFGB6X8QQVEiScv4MAvrqJxjVTNOG0mYEX45YxIdBWf1Pxps_yJrsf0rk6GqV7hEj5axk_LfACdqIMYM1Wm-h79hlCMXXFCGN7dQ5y06X1tJi6AT9_Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلیمو برای استان‌های همجوار خلیج فارس رایگان شد
پلتفرم فیلیمو با انتشار اطلاعیه‌ای، تماشای محتوا برای هموطنان ساکن چهار استان جنوبی کشور را به مدت ۲هفته رایگان کرد.
در متن منتشرشده آمده است:
یک ایران هم‌داستان شماست
ایستادگی قهرمانانه شما، داستانِ فرزندان امروز و آینده‌ی این سرزمین است.
تماشای فیلیمو برای شما قهرمانان حقیقی ایران، هموطنان نجیب و خونگرم جنوبی، مجاوران و حافظان خلیج همیشه فارس، در استان‌های «هرمزگان، بوشهر، خورستان و سیستان و بلوچستان» به‌مدت «دو هفته» رایگان است تا شاید ساعتی را در قاب تماشا، هم‌داستان شویم!
با هم از این روزهای سخت عبور خواهیم کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/672099" target="_blank">📅 14:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672098">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2492fc3624.mp4?token=bTQSML_4G8pxWV3nE0BKsNUHSc8aBcnWry0e2pDmu-sYj3r2LlnAymda0WaRIV6mJCmtqT0lRfZVWfGQtMf-V7m3sqDYXk84l5O8WpwqAzKQI4aw60j2A_Lo3iiekBNyzsnoU2-1To4SS34YfsxtLe6zdK20Baog9eIxCFtw2Cl77TcQ4uQxff2qGTmZQ70qp5H4gIWAZrwiDK1DLHmRhFLnvc8Z5-DlsvQzFtkCPQ-HYQfpm41EY5EwoeKgz7s9ER8EmXH2Fedkds8vPVwj_YN-bOPDsxvyBwvugBn0eKCpeIvmQdw7w9R7VMBMXPdmYSaD9_rE8gj6GL59eHRoKSANCTH7vCsjqbOIj3f4x5X-tpcvS5yyddK2svImcadn9Mh8bEo0xAWEWH2fnDYfhjP4F3-I_tmM1zzUcyUECERiIaaTdc-HTx9-vfpiaNEkqtCH5k6oDXApZJxh8GU7FHFly1rryilBzWbJAX9UuKWh7Uep6xnbyxxNkshzjMpZOm0BBGfEgG2vmNY2gFV_YKg1e3dSsCya-7GKStpPEglFSPFIZHQp3M6dNbBZ_c6AVJWdhRTgNfQM0q4k-eg5HJsW1RB2MG61mWkhBiSpXpGJgHHVnXGXALBkShNkRFcbudI13fv3LPmX_OgyR-SJjd4oKEm7jLUdoEumx2s6MS4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2492fc3624.mp4?token=bTQSML_4G8pxWV3nE0BKsNUHSc8aBcnWry0e2pDmu-sYj3r2LlnAymda0WaRIV6mJCmtqT0lRfZVWfGQtMf-V7m3sqDYXk84l5O8WpwqAzKQI4aw60j2A_Lo3iiekBNyzsnoU2-1To4SS34YfsxtLe6zdK20Baog9eIxCFtw2Cl77TcQ4uQxff2qGTmZQ70qp5H4gIWAZrwiDK1DLHmRhFLnvc8Z5-DlsvQzFtkCPQ-HYQfpm41EY5EwoeKgz7s9ER8EmXH2Fedkds8vPVwj_YN-bOPDsxvyBwvugBn0eKCpeIvmQdw7w9R7VMBMXPdmYSaD9_rE8gj6GL59eHRoKSANCTH7vCsjqbOIj3f4x5X-tpcvS5yyddK2svImcadn9Mh8bEo0xAWEWH2fnDYfhjP4F3-I_tmM1zzUcyUECERiIaaTdc-HTx9-vfpiaNEkqtCH5k6oDXApZJxh8GU7FHFly1rryilBzWbJAX9UuKWh7Uep6xnbyxxNkshzjMpZOm0BBGfEgG2vmNY2gFV_YKg1e3dSsCya-7GKStpPEglFSPFIZHQp3M6dNbBZ_c6AVJWdhRTgNfQM0q4k-eg5HJsW1RB2MG61mWkhBiSpXpGJgHHVnXGXALBkShNkRFcbudI13fv3LPmX_OgyR-SJjd4oKEm7jLUdoEumx2s6MS4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علی مطهری: یک مقام قضایی سطح پایین دستور فیلترینگ تلگرام را داد/ دولت پزشکیان می‌توانست فیلترینگ تلگرام را رفع کند ولی متاسفانه چون پزشکیان روی وفاق تاکید داشت این اقدام را انجام نداد
علی مطهری، نائب رئیس اسبق و نماینده ادوار مجلس در
#گفتگو
با خبرفوری:
🔹
دیدیم از طرف مقابل خیلی مقاومت شد و هنوز نتوانسته‌اند باز کنند. اگر قرار است بسته شود باید به شکل قانونی انجام شود و اینگونه نباشد که یک نهاد امنیتی یا یک نهاد قضایی اعلام کند که فلان سایت بسته شده است.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/672098" target="_blank">📅 14:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672096">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bc77fdf3c.mp4?token=eEy7Iab7UFGZVwb_t4LmkbPO9X3JcTeuAfYvQDuRsJoTcP1S0CYFVe1MXQpAZh9aRCZXX-L2ZKZjxBpTpwPUS04q7FXiMTsxWmDc5NmrNal5Up75V8iA-Uzcr2QU4uh6kdfUEEcD57jKNALARwrS4zML0sSSWUIGCTCJpR1bIgAOlwiLnN9dyV06v37Jggwu_tuPEpTnIQAuK8yuqLIoRBgu4lbt9fYKz0Q9tz2941h3YSyxyvr2oBNvFWYWC-LTRnFsxkvbeMDNYkc98KyV__e78nE7y8rPL0cvK0KBzq4ixqjTTu1cFOmD-WveP_iFWU1Es-L_0OGwSdCJcff_Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bc77fdf3c.mp4?token=eEy7Iab7UFGZVwb_t4LmkbPO9X3JcTeuAfYvQDuRsJoTcP1S0CYFVe1MXQpAZh9aRCZXX-L2ZKZjxBpTpwPUS04q7FXiMTsxWmDc5NmrNal5Up75V8iA-Uzcr2QU4uh6kdfUEEcD57jKNALARwrS4zML0sSSWUIGCTCJpR1bIgAOlwiLnN9dyV06v37Jggwu_tuPEpTnIQAuK8yuqLIoRBgu4lbt9fYKz0Q9tz2941h3YSyxyvr2oBNvFWYWC-LTRnFsxkvbeMDNYkc98KyV__e78nE7y8rPL0cvK0KBzq4ixqjTTu1cFOmD-WveP_iFWU1Es-L_0OGwSdCJcff_Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رانش زمین در جنوب ‌غربی چین
🔹
بر اثر وقوع رانش زمین در نزدیکی پل «ووجیانگ سانچیائو» در شهرستان پنشویی، واقع در کلانشهر چونگ‌چینگ واقع در جنوب غربی چین، چندین خانه مسکونی تخریب شد و تعدادی از ساکنان زیر آوار گرفتار شدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/672096" target="_blank">📅 14:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672095">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
قالیباف: ایرانی میراث پرافتخار خود را به آسانی واگذار نمی‌‌کند
🔹
مدیرکل روابط عمومی وزارت نیرو: خبر افزایش صادرات برق به پاکستان جعلی و مغرضانه است
🔹
وب‌سایت کپلر: دیروز تنها ۸ کشتی عبور کردند که کمترین میزان در ۳ هفته اخیر است.
🔹
نیروهای امنیتی عراق در استان الانبار یک تروریست داعشی را به دام انداختند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/672095" target="_blank">📅 14:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672094">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
تیزر قسمت چهارم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای حسین حاتمیان که به دلیل سقوط از بالای تریلی و شدت ضربه به سر، روح از جسم جدا شده و قدم به دنیایی بسیار زیبا و دلنشین می گذارد؛ منزل و باغ بزرگی که متعلق به ایشان است را رؤیت می‌کند ولی عذاب دردناکی از دوستان و نزدیکان گناهکار را نیز درک و احساس کرده و در نهایت به دلیل سلام دادن همه روزه به اهل بیت در دنیا، از آنها پاسخ سلام را در برزخ دریافت و توسط نوازش دست مبارک امام جعفر صادق(ع) به دنیا باز می‌گردد را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: حسین حاتمیان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/672094" target="_blank">📅 14:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672093">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f48ceb9ad.mp4?token=JvJSPw9k1WGS2PkLPY4wAohTo7qNzlfHvrvWP8ewst3KuaLZ2v66ocj93nKePMZ-jMvwibFdkYNxlt_FyGYiZJGkiY5Ko9xVCMuRPew64dIwis3D_Qytr9uLj2sh4SuSwyS6tDJslece2blUKS8yYZ4Y16clycs5kHDbTbP_SVYwT0fBZ_TS0iE8BCArBRgpgKhk3DDyYxpDKRznWr8kz3j-me_S5ChB1_BCSRz_KCQe0DPs6HC5hNDrRwQ8mBHUBV7NMKzgzyR7Bt-Iw9VKjpr0Lh2Hbuy2PfpJqkJvmHrWBlvH-9gwqBPw5v685BUG6c7cci7zJFnMcsK7xv0eIDM9WyWON_u_r0_uDSA9z-aMEQmnscxRqED8Z9hruOI0xMOKr2XYrLk0Z0ScRixWIDmGRtMR41ugVJ3wYevTRA2GLFopU_m7fDw_VjNW9K-UqFFMGdXwfxeT7FzS8ixweq-jNy51nIwDIOhg8J2AGxt__5MdgmRVMnmwn6yopTkXPtPOGRCw-K2CeoMtQwaclCJ42c58DerjR1FqmGtkEPwkdBV9mbBILO9qpfBVA58gSjBhhDjdqx35oDxpghJaykfVFweG9aH6HjGlwdq837RLG8fnR_SUnrheiE8UkWgNkbgnpHn5MQHBSwmgaYKx9y9eSW7V9OKqZtIYni8IabM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f48ceb9ad.mp4?token=JvJSPw9k1WGS2PkLPY4wAohTo7qNzlfHvrvWP8ewst3KuaLZ2v66ocj93nKePMZ-jMvwibFdkYNxlt_FyGYiZJGkiY5Ko9xVCMuRPew64dIwis3D_Qytr9uLj2sh4SuSwyS6tDJslece2blUKS8yYZ4Y16clycs5kHDbTbP_SVYwT0fBZ_TS0iE8BCArBRgpgKhk3DDyYxpDKRznWr8kz3j-me_S5ChB1_BCSRz_KCQe0DPs6HC5hNDrRwQ8mBHUBV7NMKzgzyR7Bt-Iw9VKjpr0Lh2Hbuy2PfpJqkJvmHrWBlvH-9gwqBPw5v685BUG6c7cci7zJFnMcsK7xv0eIDM9WyWON_u_r0_uDSA9z-aMEQmnscxRqED8Z9hruOI0xMOKr2XYrLk0Z0ScRixWIDmGRtMR41ugVJ3wYevTRA2GLFopU_m7fDw_VjNW9K-UqFFMGdXwfxeT7FzS8ixweq-jNy51nIwDIOhg8J2AGxt__5MdgmRVMnmwn6yopTkXPtPOGRCw-K2CeoMtQwaclCJ42c58DerjR1FqmGtkEPwkdBV9mbBILO9qpfBVA58gSjBhhDjdqx35oDxpghJaykfVFweG9aH6HjGlwdq837RLG8fnR_SUnrheiE8UkWgNkbgnpHn5MQHBSwmgaYKx9y9eSW7V9OKqZtIYni8IabM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر عملیات ترکیبی موشکی و پهپادی با تاکتیک های ویژه و غافلگیر کننده علیه مواضع آمریکایی در موج‌های ۱۰ تا ۱۶ عملیات نصر۲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/672093" target="_blank">📅 13:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672092">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
اخبار تکمیلی از حملۀ آمریکا به پل‌های جنوب؛ ۵ پل مورد اصابت قرار گرفتند  استانداری هرمزگان:
🔹
در ادامۀ حملات تجاوزکارانۀ آمریکا به استان هرمزگان، متأسفانه علاوه بر پل کهورستان، پل‌های دیگر شهرستان خمیر هم مورد اصابت قرار گرفته است.  کدام پل‌ها مورد حمله…</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/672092" target="_blank">📅 13:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672091">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
حمله به یک کشتی در سواحل یمن
خبرگزاری رویترز به نقل از منابع امنیتی دریایی:
🔹
افراد مسلح به نفتکش حامل محصولات شیمیایی «آسانا» در خلیج عدن در سواحل یمن حمله کردند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/672091" target="_blank">📅 13:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672082">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
علی مطهری: برخی مسئولان امنیتی با پرونده‌سازی برای افراد تلاش می‌کنند انتخابات را مهندسی کنند/ گاهی مسئولان شورای نگهبان فریب می‌خورند و به نوعی رأی می‌دهند که منجر به رد صلاحیت برخی افراد می‌شود
علی مطهری، نایب رئیس اسبق و نماینده ادوار مجلس در
#گفتگو
با خبرفوری:
🔹
گاهی مواردی را که جرم محسوب نمی‌شوند، به عنوان جرم جلوه می‌دهند. دلایل رد صلاحیت آقای لاریجانی خیلی سست و سخیف بود و در دوره دوم که ایشان کاندید شدند دوباره ردصلاحیت شدند که این‌ها ناشی از مهندسی انتخابات است.
🔹
گفتند شما در نطق خود گفته‌اید نهم دی اگر باعث تفرقه شود دیگر یوم‌الله نیست، بلکه یوم‌الشیطان است.
🔹
رهبر انقلاب گفتند که اگر امام بودند (درباره موضوع حصر) خیلی سخت‌تر برخورد می‌کردند. به یکی از  اعضای شورای نگهبان گفتم متاسفم که شما با این افکار عضو شورای نگهبان هستید.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/672082" target="_blank">📅 13:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672081">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
اطلاعیه شماره ۲۴| روابط عمومی سپاه پاسداران انقلاب اسلامی: سامانه راداری برد بلند و چندین فروند هواپیمای راهبردی سوخت‌رسان آمریکا منهدم گردید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/672081" target="_blank">📅 13:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672080">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7D8s4m-BiR5gKF23Iye0rGVzqjk5Mk7ogWUqzd4r7EzgyGsGvC8BWSazM_tcClOHAFq_aSBF45K9DtaJOm0cXgc3e5ioElxP7p9bJ-bBidGT5wmXmywIibAcst8xvnf6tlXhdRdp066JgispIQ8tS06uKnBwdNa2iD2VE0bQftsTWs3SyPC0QcKU8t1LgAfaGURN9BYLRlfnr-nxA-RwWFO6_HtiVgAlDCnqLdSmtE24ZHMnkmzlbCARpVsbxX6ru25VTqrFv4G29PhRDI8hmzQGxz2zLjNEJu1C9XseWZ0THJtPgZiz7v100UC3lbT1qiXgJ7h3drFj0UsG-OSNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۴ خاصیت سیب که سلامتی شما را بیمه می‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/672080" target="_blank">📅 13:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672079">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f11f25b166.mp4?token=J2PUNRXcirImWdNgiPIH5Bqqto51bcSxi5tHO4ejDSpoO6ekUPTHqhdG0aT_huH91enqF6T4RBouJOcWjzKDnSgculPK6GEiLMBann90VOLVy2McbcA_dYQjkdwv9Zly5SxnSr6kzqkfRnOuZim13VsP4D9r7fxeqcQOkuI7s_5-3cbD2bCOWc5VloaJ4zFlB05K3Rn_HlEOhT7tDaY0_R1kMT8Y17ViXDBrweCQ1QKDS67rC8DxeWo4pnASnfpvSXOYcxcZ9_w9fTgyx4KL-4WYscXXyrcQYW_YuYC_7dwLVM8E1vIOsPzaX0MITSX7pFO1ZbsAwKbBaRKgof2kWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f11f25b166.mp4?token=J2PUNRXcirImWdNgiPIH5Bqqto51bcSxi5tHO4ejDSpoO6ekUPTHqhdG0aT_huH91enqF6T4RBouJOcWjzKDnSgculPK6GEiLMBann90VOLVy2McbcA_dYQjkdwv9Zly5SxnSr6kzqkfRnOuZim13VsP4D9r7fxeqcQOkuI7s_5-3cbD2bCOWc5VloaJ4zFlB05K3Rn_HlEOhT7tDaY0_R1kMT8Y17ViXDBrweCQ1QKDS67rC8DxeWo4pnASnfpvSXOYcxcZ9_w9fTgyx4KL-4WYscXXyrcQYW_YuYC_7dwLVM8E1vIOsPzaX0MITSX7pFO1ZbsAwKbBaRKgof2kWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قرائت دعای سلامتی امام زمان(عج) توسط رهبر مسلمانان جهان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/672079" target="_blank">📅 13:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672078">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSS4IkDqKDFdnOw_SE-Vx5jV_3S0ZhZwD7vYATOrMWFPPJ0oPZ6Zzpg0RRY6gE4w4V7vaGXSDsiaEsiGWNt7VTz6f9_TJbqINQU0P7Sz56WCPe6YeoQa_YtowEaDLBWGVzkw7xgIJIdOHhstAIMmgilv1nwg3z4NaiQbtprXRo6HyHjw3QMMcUA3KUbhp1hqlXCBYILL7lmXJxUUe0kxqUHiZMztc_REnAOOmv1JxIz0wKxaZbs__RbQuEnDKboN-2R_tNRIDx7wUlamueWKnNjaYxJjv4x8fT0JE77Nm8UlwdmyKrV249F_uXOd6091zEFljecfeGNqChP0hYX_OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اشاره عراقچی به جریان نفوذ اسرائیلی در امریکا؛ همه این‌ها به‌زودی برملا خواهد شد
🔹
به آمریکایی‌ها مرتبا درباره «نفوذ خارجی» هشدار داده می‌شود؛ پس در مورد کارزار گسترده اسرائیل برای فریب دادن دولت آمریکا و کشاندن آن به یک جنگ انتخابیٍِ بی‌فرجامی که حتما پیروزی در آن نخواهد بود، چه می‌توان گفت؟
🔹
بدتر از آن، اسرائیل از پول مالیات‌دهندگان آمریکایی استفاده می‌کند تا هر صدای منتقدی را در داخل ایالات متحده خاموش کند.
🔹
اما همه این‌ها به‌زودی برملا خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/672078" target="_blank">📅 13:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672077">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
اختلال ارتباطی در ویسیان و معمولان پس از حمله آمریکا
شرکت مخابرات لرستان:
🔹
به‌دلیل اختلال فنی گسترده در زیرساخت‌های ارتباطی، تلفن ثابت و همراه در بخش ویسیان و شهرستان معمولان با قطعی مواجه شده است.
🔹
تیم‌های فنی در حال بازسازی شبکه هستند و طبق برنامه، ارتباطات ویسیان تا عصر امروز و معمولان حداکثر تا بعدازظهر فردا برقرار خواهد شد.
#اخبار_لرستان
در فضای مجازی
👇
@akhbarlorestan</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/672077" target="_blank">📅 13:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672076">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
هشدار سفارت آمریکا به شهروندان خود؛ به عراق سفر نکنید
🔹
سفارت ايالات متحده در عراق با صدور بیانیه‌ای سطح هشدار سفر به این کشور را به بالاترین درجه افزایش داد و از شهروندان آمریکایی خواست به عراق سفر نکنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/672076" target="_blank">📅 13:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672075">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
اخبار تکمیلی از حملۀ آمریکا به پل‌های جنوب؛ ۵ پل مورد اصابت قرار گرفتند  استانداری هرمزگان:
🔹
در ادامۀ حملات تجاوزکارانۀ آمریکا به استان هرمزگان، متأسفانه علاوه بر پل کهورستان، پل‌های دیگر شهرستان خمیر هم مورد اصابت قرار گرفته است.  کدام پل‌ها مورد حمله…</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/672075" target="_blank">📅 13:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672074">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
تعویض گل‌های مزار مطهر رهبر‌ شهید ایران و خانواده ایشان در رواق دارالذکر در جوار حرم امام رضا(ع)
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/672074" target="_blank">📅 13:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672073">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
علی مطهری: شهید لاریجانی ساعاتی قبل از شهادت با پزشکیان جلسه داشت/ پیکر شهید لاریجانی چندان سالم نبود
علی مطهری، نائب رئیس اسبق و نماینده ادوار مجلس در
#گفتگو
با خبرفوری:
🔹
ایشان جای خود را در خانه آشنایان و اقوام به طور دائم عوض می‌کردند. افطار همان شب پیش آقای رئیس جمهور بودند. عوض کردن مکان‌ها به صلاحدید دکتر لاریجانی، فرزندشان و تیم حفاظت بود.
🔹
این اتفاق کار اسرائیل بود چون ترس داشتند به وسیله علی لاریجانی توافق و نزدیکی بین ایران و آمریکا اتفاق بیافتد. هروقت احساس کنند قرار است با آمریکا توافقی شکل بگیرد، کارشکنی می‌کنند. دلیل اصلی شکست خوردن برجام نتانیاهو بود.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/672073" target="_blank">📅 13:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672072">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c8bc8dc64.mp4?token=Ev9Ex4jzSy0LWw_GXfAuhnlHsl7mDb2gmCvMpGsmhJOQdmtc8K_-Qe-tCWnvyWIygRqAiqDfhKimnRQ-oNXNKlcAYZze3HQRjm65BDZJO6JZOo0W3OU1HaRxPQhBYrswLseudGbjS8X0TtuAW50cAtMFLcpkbgYDAX596JajDbwqHZ1pWwH1ddrNV-O8erloF-9Qtx3Gsfkl_zJq1_jVBdl2f-58kGo4TnbavCk4u-3PmWc25CNiXcQ-tL_b8LLhfAkkccmjUx76Axr0Bo0z6QHC2V2edlWJG0Hss6PV1oiJnJHnfJrNRzRvnVvVNcnA5airDPDcHENwyErZ0_tJxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c8bc8dc64.mp4?token=Ev9Ex4jzSy0LWw_GXfAuhnlHsl7mDb2gmCvMpGsmhJOQdmtc8K_-Qe-tCWnvyWIygRqAiqDfhKimnRQ-oNXNKlcAYZze3HQRjm65BDZJO6JZOo0W3OU1HaRxPQhBYrswLseudGbjS8X0TtuAW50cAtMFLcpkbgYDAX596JajDbwqHZ1pWwH1ddrNV-O8erloF-9Qtx3Gsfkl_zJq1_jVBdl2f-58kGo4TnbavCk4u-3PmWc25CNiXcQ-tL_b8LLhfAkkccmjUx76Axr0Bo0z6QHC2V2edlWJG0Hss6PV1oiJnJHnfJrNRzRvnVvVNcnA5airDPDcHENwyErZ0_tJxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیم ملی والیبال نشسته ایران برای نهمین بار قهرمان جهان شد
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/672072" target="_blank">📅 12:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672071">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LaQg__fJmj-1Pv-uLDWThEcx0m3K-N6JYllJhd3pLK_MBrICxwPF50k5LhCmEfkkTSzJu_o5uwie20NrtzOUmgmRG-ym6xTx3AZxRBIucuBUhg9DumGchQNewnkmiS7QRpKdZaRvCBe8pGlo4ZpV9mw2biAIDQTzs4KwlwB1JTrSXCr0BVp-n-Lc0yjL2nPC498p8rIBvgmcEP4FvSAunzqQvAPi1f0scyJDZpQ0f7QjHbp9CddSM5aoh586MtNEs8M5iGyM4EFh6-3tG5XfPs4Q7kLy3YkgMj4y_GiE_YWgMFFByzAwu3yN6NcxcFmgnNINevKQ_VOj670beEe87w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انهدام لانچرهای موشکی مستقر در اردوگاه سازمان ملل توسط ایران
🔹
ایران در یک حمله پیش‌دستانه، لانچرهای هایمارسِ مستقر در اردوگاه سازمان ملل در کویت را منهدم کرد؛ این رویداد بار دیگر نقش پوششی این نهاد در عملیات‌های نظامی (مشابه عملکرد آن در غزه و یمن) و فریب افکار عمومی درباره ماهیت سازمان ملل را آشکار کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/672071" target="_blank">📅 12:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672070">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
افسر ارتش صدام: روزی نبود که خبر ترور کسی را در خانه‎اش نشنویم؛ ایران بعد از جنگ هیچ‌کدام از فرماندهان و خلبانان بعثی زمان جنگ را رها نکرد و همه را حذف کرد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/672070" target="_blank">📅 12:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672069">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
گزارش وقوع حادثه نظامی برای یک نفتکش در خلیج‌فارس
🔹
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از وقوع حادثه میان یک نفتکش و نیروهای نظامی در آب‌های خلیج‌فارس خبر داد.
🔹
تحقیقات برای روشن شدن ابعاد این رویداد آغاز شده و به شناورهای عبوری هشدار امنیتی صادر شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/672069" target="_blank">📅 12:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672068">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jF48efWsOLelUaWj4QWQZUql0q6TNDWtbzaA9r_wqrEj-W3-VhT4aZAOig0Z9BJrOe3VazUIRF4ZkdWcVYGSw1yJtnNahO2xBNIZ2-FxbpIN93SwJ_E1D5YLZ3scb_UJ7HEOIMZlL0Lymq7pAaHtpqaS3jWK2Rj1WMsESgheTekdjpmZ9V0pzJk8yIqy2A-WGpMRU2QRs_IcvChlHvlidUCJevO_78UssHE_7G_c4KknVNm5IfWTT7E8co38F2_syAqCLkDEJcWt2Hn0z8YJD682h9uhtBWIqmhrOZt3F23SbtBpQwXNKm0C46vXk1MIW0SKSJpXAoqa8PXayY5f6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای
کویت: یکی از نیروگاه‌های تولید برق و آب‌شیرین‌کن مورد حمله قرار گرفت که به تأسیسات آن خسارت وارد شد
🔹
در پی حملهٔ به یکی از نیروگاه‌ها، تعداد زیادی از واحدهای تولید برق آسیب دیدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/672068" target="_blank">📅 12:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672067">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
وقوع حادثه دریایی برای یک کشتی در جنوب یمن
🔹
سازمان عملیات تجارت دریایی انگلیس (UKMTO) اعلام کرد گزارشی از وقوع یک حادثه دریایی در فاصله ۶۵ مایل دریایی جنوب شهر المکلا در یمن دریافت کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/672067" target="_blank">📅 12:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672061">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o1DRes35gqWz5Lo81xponQv1iqmDtl_ZIULBHg3PDWlALDDtMxca4Hi1-bGeKpP6AsDKnTAzeJlepOUdkRaSBUxEvsQDlNGpWl7isTycq_SBlp2_cwGqYaaIJiN3jlwaRTuwvbpw0Js1CFM3taxK98La53HgsGdnnbDojc26GTfVmPy3uA6AzOWVCbMTmqIyILzlqOCaptNjSlpILIWwWJqQ-ffnNT85Dpbq0WVx9QYeSHqO9jTecXmUs3mC_qEviPOoAvpr5lTbEnhan--PRl0_2egaSPdHYVDrHif7xDh2FoOLNmR2lqb9-AnuQ9M49k4bUZWi5Rbmbkv_wrUphA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bBxFyh31G-IXcoUa0MgVxkrO6FZmlL-Ejz398Uz6jXnwEc_T4rqmJVNr8QF-aTn16AG0kVjCREuvdsn8LHhJfzsKSZ0oUh1UyEUZl8Bgaqtt25qH_Qsc4ISC7AujY6NDCejDyvY4HEO66S5gsySURKIbe7pztyTy8IhmUCk85QjhbdLV3-ad6XPTpy5bZ1pFOmimoS8rfru5QML4Inpgw4djFmHgUAKmGe9w_YfBFK7ClmGmoJT7Z64hrGVAZdALK2h-kOnwGkJ9eNWskXPhDoizH1h3vxTQcD3U0NXRPPeOHAxeiftriqARGbegvWUqbSr5AWY3SYnu3TfMBqlANA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R4cQjdWi-ZFv9CcgNX_a4N6Utc_0Q_gQqNATFfU3DkZLeZSzLl1bGP28fCH7Iptt3xC5Hgep5BnR4Pc0OCoPat2BoGhl3JKP_gdLLtWrz02rp4noZX1dZBB1PKwyMcUIgQ1nVe4zWLym0F24lAvGFtRdGgsigkrBiZnbTeAFtYHjtg3o8wl0LieOev4iu0VA4X-UsFFtrGe9Qx0APSlAOEMqObJQL6Tu8fjF8RXq8hpfNuuYBJsasMOKyZhxptTgWgEBn1vrcnI_xfWG4DpeKxLuGnn4mVF6xAC-tnD4ZL_OtDIf9O-5KCOdUXEu30xIXAFbQuIEU-_15B59EP2R9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R8cUuZWg3AM9YUOY5FTv_MI1nEyX-zGQzKP-kTv3xRS_MVq1I4ndT6N5rSeRNnV2NqjyLZVsWQqpO2EqgYq1jD2LY-IcvTUoQgra2NZGJet6sKWgacMaiBBRNj6NBD-f6NIjAGhjqmjELMePpcxknFH6ZeoivBpkKErTqpSnc4Vfbl35bwuAwXlK3ctjQs-kfAB3u92fey46l1OPIxQ1d-nJEmjzteKKPILCzRI8bIHMAZXA0MDaqpIa6GsOiocZfpQJVN44qI1sThq8-XjAsA_UbSW3J5t2ClmoQE1j5fMtWXm0yqP1-Y5lgOErp8gbgwTzvCDjwV6UIaWhKJ__ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IlX-KvBf-k9vD3QvcldF5q6zLQkEmffFgk1Mc4J7Kb02R317Q8rkdQYFvjPH7920pPwBouyQG_E5uuURe4bDkxoIzOxoozpxKA2pPg_SJT2NkhX8qI3tFnpNrDSqaz9GbPZ-QCarTM6KGgYMh_SR_89bjpf_KwoTfkPLbb_W32Bmv1_xngJS3KBp-edTlTmrbmouUXrbnimNesT9IB9uRtLx1aqWu2ZOdQC2rsxsYEbakl1jAiE2MAovxt0Vt_zeDJbIVofCMj1Oa0JdUkKww-D8Y3dTvX1gAa4vqpV3Itl7c6IWZT68wlYTZmyGqz5r17ojrzPUjJ9Gc857Xod4pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uV2tFHKkbYQQA-ymqmXwipAlT4n0Nu87-ILWGRjQG9epIjBb0qiSYVh6iRTr6FtnB0OQNaYUh9cTB2TtWhEsf5IsDhIikhl_AXThHWokmW3gyMKBcL2F84hJIUmPJQdBLR017z8FByIlOBaLRW5f56SCBLg1PI945exe9aPzBENln4JvTxCMTpTJ9-rCGtmE4k2rTiXqZNz8kRlDtX1wvjRNok8ZCx-p1k4PLn_s4tX-wNGHxuJKtaTICFSJbIpe55UvQBxASBSm3NPmTo7XT0L3N6Kf82fe3T1vwYlDvO_QQTsZfLQVG9Ki69kcsx3p1Wtyn5IPb-q3RvGwyBN32g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
افشای دروغ‌گویی اردنی‌ها در رهگیری موشک‌های ایرانی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/672061" target="_blank">📅 12:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672060">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51f51880bf.mp4?token=ivIqseVfjjM9eihXX555qP50Os6_cWhg4qkj3444SwfJeFAGB3FnlJ8bLyJ4ifhtRyvdrW5bT8rHVB89TduxDvjbA6vEbhJpRBqart_5Oof0nLGJs_Mtr1CJJP7oOXkyFj27xS-7QYjGOr546gypw6IQvGVEUimZFzDpEdqdyoOdi5MsUjLct4gm0Uvdgs9KV79U5OMqib-wmCPmDC7TLtl3952pf4bik362dbwrBVuQUwFvB3jORYZZVV-9cJJO-iNIhac3vNoHVSaJmVCqzJ6IUWojTcdI-RzFgZ9oYYOus4bGfDTnXttSTIV08eKJ57sRQV6t_3-a-qffPVcm5RKdhfmTz3rZN0irQv4G4uhiWCjIMuE-j8adb8WiBT32mqIPegbbU0ymVgwSuoXdemTSIKILNZLD3lCs-rxQ0XPrhuSsCntIi3llDm5USis7N8R4OCja8DDD7pQ2oKP6qUnkHSwI1twINe2IefkZObfZqKgLHzPTOWqnK0x0KGjdwbN3DTb4u2rcaLvVxSlAKyVdYilY7dGduzwttkvzpdapH2zNrCM3WSsJRRsgfs5cQhmSDMrTL9HeG7FhLWMozOXH6TEk636BZKA9Rm1284wCOc0KqxP9VRxtin1UW23wwrXbxKZvqnxV4XZ4O2-1viKbOSSlCTHptEHtgQEDyEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51f51880bf.mp4?token=ivIqseVfjjM9eihXX555qP50Os6_cWhg4qkj3444SwfJeFAGB3FnlJ8bLyJ4ifhtRyvdrW5bT8rHVB89TduxDvjbA6vEbhJpRBqart_5Oof0nLGJs_Mtr1CJJP7oOXkyFj27xS-7QYjGOr546gypw6IQvGVEUimZFzDpEdqdyoOdi5MsUjLct4gm0Uvdgs9KV79U5OMqib-wmCPmDC7TLtl3952pf4bik362dbwrBVuQUwFvB3jORYZZVV-9cJJO-iNIhac3vNoHVSaJmVCqzJ6IUWojTcdI-RzFgZ9oYYOus4bGfDTnXttSTIV08eKJ57sRQV6t_3-a-qffPVcm5RKdhfmTz3rZN0irQv4G4uhiWCjIMuE-j8adb8WiBT32mqIPegbbU0ymVgwSuoXdemTSIKILNZLD3lCs-rxQ0XPrhuSsCntIi3llDm5USis7N8R4OCja8DDD7pQ2oKP6qUnkHSwI1twINe2IefkZObfZqKgLHzPTOWqnK0x0KGjdwbN3DTb4u2rcaLvVxSlAKyVdYilY7dGduzwttkvzpdapH2zNrCM3WSsJRRsgfs5cQhmSDMrTL9HeG7FhLWMozOXH6TEk636BZKA9Rm1284wCOc0KqxP9VRxtin1UW23wwrXbxKZvqnxV4XZ4O2-1viKbOSSlCTHptEHtgQEDyEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علی مطهری: در ماه‌های اخیر که نظارتی بر موضوع حجاب نیست با موارد ناهنجار مواجه شده‌ایم و دولت باید به این موضوع ورود پیدا کند/ ایران قرار نیست اروپا شود و نمی‌توانیم به برهنگی و بدن‌نمایی بی‌تفاوت باشیم/ قبل از سال ۱۴۰۱ حجاب در کشور وضعیت خوبی داشت
علی مطهری، نائب رئیس اسبق و نماینده ادوار مجلس در
#گفتگو
با خبرفوری:
🔹
حجاب یک اصل اسلامی است و نمی‌توان گفت هیچ نظارتی در این زمینه نباید وجود داشته باشد.
🔹
نمی‌توان اجازه داد خانم‌ها و آقایان، هرطور که دوست دارند، لباس بپوشند.
🔹
اینکه مسئله پوشش در خانم‌ها و آقایان به تدریج به برهنگی و بد‌ن‌نمایی تبدیل شود، چیزی نیست که نسبت به آن بی‌تفاوت باشیم.
🔹
برخی اقدامات ستاد امر به معروف مانند مقایسه تصاویر افراد با کارت ملی، ارسال جریمه به در منزل و محدودیت‌هایی که برای تاکسی‌های اینترنتی ایجاد شد، ضرورتی نداشت و جامعه را تحریک کرد.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/672060" target="_blank">📅 12:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672059">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbIe5H-fG9msX32QafKFeS_hU6XqtPR6WtJqgeA6SeykKwDjdUrqIF_RMhRoEKdDy750fWY3aYDemT67RQWCaIl3yN_9JOUj4qyhnAledj_Mb_QpyaKxrGb-m5bXVq4RJ0eFSMQyxAlNF8mriwp8K3-OZD9h2hWI-j6YlgbGygTDNrYYyhHefvgFjpbGNuQMaO8un9gKuOnxnEohJFQhAfFwrBHQAqqFhM8Xj9KQA3EqCj-vDNAVGx18uuEOR3jzOVUANeENaRpNos8XN77UbnIcDA8ST6-z9odadh6DNUxdMyuJv4lVnsD1YB3MkYcSqMnEo_CDpOcsR1xVvcmhkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این مطالبه‌ی جدی و قطعی مردم است! خونخواهی قائد شهید امت و مجازات عاملین جنایاتی که علیه مردم ایران به وقوع پیوست
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/672059" target="_blank">📅 12:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672057">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wd3kbcTztlDH0i3YCn2D8OiNy_Nlzbowz5qgZunoqKjG12IKEzJA-wx2KlmsTTPXFnlgHRR2xgdzQwA6GxGScXEbX7uTjaPqrAvn3oVfk8pBuat_esJklfJ1hcprs4oe4_c8uSpeZAbTOj9s2x3xdgkHb0U7Lm6yyfutcZhRM3buCB9BDEuOBc39rVUvGkQnNZrbIMbdOUCNB6C5HOGxLDfXgHPwMAdi2CGB4dvQVUtih0nJlihzcmil3Se0yxvG3hmYNL5XjLA5zfsqIkjwbsGB--X8Mi02---425Jwns3-GdwRoaXorS3w9KcXRk6tS48bJlaAgMP-GGdOrrkg_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا مدعی تصرف یک نفتکش ایرانی شد  نهاد تروریستی «ستاد فرماندهی مرکزی آمریکا» (سنتکام):
🔹
این نهاد مدعی شده که نیروهایش در دریای عمان بر عرشه نفتکش ایرانی «ون یائو» فرود آمده و آن را بازرسی کرده‌اند.
🔹
به گفته سنتکام، این اقدام در چارچوب «محاصره دریایی»…</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/672057" target="_blank">📅 12:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672055">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
هلاکت ۸ تروریست کومله در حمله موشکی به سلیمانیه
🔹
حمله به مقر گروهک کومله در روستای «زرگویزله» منجر به کشته‌شدن ۸ نفر و محبوس شدن تعدادی دیگر زیر آوار در مناطق کوهستانی شد./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/672055" target="_blank">📅 12:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672054">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
تشدید عملیات سپاه در اقلیم کردستان؛ هدف‌گیری مواضع تجزیه‌طلبان و تأسیسات گازی
المیادین:
🔹
عملیات پهپادی و موشکی سپاه علیه گروهک‌های تروریستی تجزیه‌طلب در اقلیم کردستان عراق برای سومین روز متوالی ادامه دارد.
🔹
این حملات علاوه بر مواضع تروریستی، تأسیسات گازی مهم منطقه که با پیمانکاران آمریکایی همکاری داشتند را نیز هدف قرار داده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/672054" target="_blank">📅 12:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672053">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VcF6-lYdCN415gJfRJ_Yfxofte75fIFPJOEZ2fr8lHDun4dvHA7leYRB1pkVBJAtKouAWRPczYI44W8EJHEYtOGljOVhpYe1xIBr7detyP4g5wPxOb8VEh9ZMkR-IHtNn4W7IFtRf_DXLsBA6AcQd12UyCts7LZzwONbqhvI7gAzeBeLkUJNe2ZYHX1jvSOWfBOnzvQuiCTrYR5M8kcVk_4YIYddH8C7RsWni-_Q6BnKAURHEH9hVbNDZSzlTagZ_QG4ODg5rehj4dklA9fzpm2wNl2c3VotPwj0tC0QFDXBHG480ZlTD6Z-NxQT2RYIspwQYpoZK2m6dmlxU6p77A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فصل پایانی امپراتوری آمریکا؛ ترامپ و کابوس جنگ زمینی
تحلیلگر آمریکایی:
🔹
ورود به یک جنگ زمینی فرسایشی، تیشه به ریشه هژمونی آمریکا خواهد زد و فروپاشی آن را تسریع می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/672053" target="_blank">📅 12:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672052">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
تجاوز دشمن آمریکایی در تپه الله اکبر بندرعباس/ ۷ نفر مجروح شدند
🔹
دقایقی پیش تپه الله اکبر بندرعباس مجددا مورد حمله دشمن قرار گرفت.
🔹
حجم این اتفاق به حدی بود که برق این منطقه در بندرعباس در حال حاضر قطع شده است، هدف مورد اصابت در این حمله یک دکل مخابراتی…</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/672052" target="_blank">📅 12:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672048">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dr7R3WM4XGK-kq40X6KuJgy4WFISQmMck9zRp9YaOrKW1omY1TUd-ZIJG5AWCeA8gtQBCLZcMp7v2rzU9KxIjcmmWN3am_9Pnb7RbNock2Z1Gy8V3t71XQotE-LQKZiXZAjfXj3OU0TceDN22AQgMXRNi5ZEf--owQ9aU3WBi02y-km-_sHrggZdyF5KC86mBCaoYpSUtjujOypLvuOZCH7nXNxB2CQ_DuAvLB5-e08NbUb9R-bVw3RhrmCYjt6OYv9s3nC6riZmBJcjj7Nlxt_PgIuQF0UEoOyVXntg1Jb_mUcr52ww9geS0ZgpQPJukPLyxI7SgmqJL5L47RWm6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZYM04zD5XPSIUZGr_ZjwfzoH37bXt4ZfIksjvLYd6kTQRJ9K8A93o3N_IUhyEYwtW2kyYd9UL9ZNP5JXRzkmluj7n5npKgrHC50GbA0dNn_lrDA9bG7lp8L94z7G_1NgmoKbDMfAuKTwOHIlJ1iP701suMtRDQcSBzcO2gVChtFx3WEeeB21ESgU7gGcAVY8xvo8XBj6iDv0FsyQHPJQgI5wyg4Kf7wy1hOm7tHkNlX6EZrpUWEWI20Xt8l1bLdxqQSSdnX-B0u_5CTGALDerJ00K7imrjo6YuigxMm7TQWZuMoLFO3jYEII4omwswlMWHjXVCE7pjCvbhApzYRjXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V0vtZrQIkzZa9ahfCOm6_w8srsqw4LhqFdPxcJrBUxSEggAu9VK0l7a9AzzhRMOQpFiyi9oBbnCGxhq0rjSEVGqEMJWScVVS_-lZzKhZzFv1Uv13nQU1ti5QNjh7N491XUliRMHftdoUC5hdWGtpLGEcM3a4PDphKpXDQLcYvQvdfOiEX7DHv_lzx6UHl7HmPvAJFLKjUa90Cv8e0tl4-peL4H2TH8fnJHfJQS1CqJW7-2lVJU2hEKpoV7WVvRkY1qjrmYlu8NLpuxG_YkqfSvF5CUZd62GRprYjuEbd4pPECrr2y4ns4TqSEaMx1-DXSqAmjiNzLGevwOGmF8n2yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EjjS71GHEWN_QtI-UmE2ap_AoFtzPUYp5Aj3_w88WGRCb682T1phRVdReSbQJjfQdDP_fF3k2I55AmdQexOd8cwVqjpANCFQms7UsvzD0qBFKAy5B3gxcmi6aWVvcseX_9PMVPyWTEUNGqUSdEq3LDK6Vu1wz2CGf7v5yqaT995wC0xzf4yiPFmZ22oQ2T9WiuQFeVpeNPqCzWDuZz62pa9m7I4_fyRjsbvZRWyZr3Q-V9CH9aEvHweY07C5occOyEFjGn3u-C6HpLPDtULftjWdayQhW3KDWSWPvl8cLthe9RaCNg1PxJGEL6id723N4fR-i02yWSchfe6eXosUwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
زیبایی کوههای مریخيِ چابهارِ ایران
🇮🇷
#ایران_زیبا
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/672048" target="_blank">📅 12:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672047">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7965901c30.mp4?token=s-nukAFs72NGnK5ob1oLj6aiDG1o6KL4_eSxueDmTRShmMMxT2AHfKo2JHqN9WwMx-MDrK19sXsuV7P_sbd59vQqZ-ELc8CVx240lEIeWvIF51spz631oho86uHqngjtTDnUCHCMKmTnfOsVE4Y8VSZkJPjkbbQ6JS1yXts1Rfe3ksFXLT1D6K8SaTD3wwg7O8Xl-ZF_MU_i86brVNOT-wgD6j2IGdEC8gC6ADm6p_7sUS_9g56Ku_62E1wXAFQbAqtDgiB1nPbqBLDS-5MiFd-rw1RJT476f-XyML18fbcGesnu9YeyambrWCD0eX-pjajHn7NS-395-LWXCZFPgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7965901c30.mp4?token=s-nukAFs72NGnK5ob1oLj6aiDG1o6KL4_eSxueDmTRShmMMxT2AHfKo2JHqN9WwMx-MDrK19sXsuV7P_sbd59vQqZ-ELc8CVx240lEIeWvIF51spz631oho86uHqngjtTDnUCHCMKmTnfOsVE4Y8VSZkJPjkbbQ6JS1yXts1Rfe3ksFXLT1D6K8SaTD3wwg7O8Xl-ZF_MU_i86brVNOT-wgD6j2IGdEC8gC6ADm6p_7sUS_9g56Ku_62E1wXAFQbAqtDgiB1nPbqBLDS-5MiFd-rw1RJT476f-XyML18fbcGesnu9YeyambrWCD0eX-pjajHn7NS-395-LWXCZFPgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امنیت خونه و محل کارت رو همیشه زیر نظر داشته باش!
🎥
💡
دوربین مداربسته لامپی V380؛ یک دوربین هوشمند در ظاهر یک لامپ معمولی!
✅
نصب آسان بدون نیاز به سیم‌کشی پیچیده
✅
اتصال به وای‌فای و مشاهده تصاویر با موبایل
✅
مناسب منزل، مغازه، دفتر کار و پارکینگ
✅
دید بهتر برای کنترل محیط در هر زمان
✅
طراحی لامپی و کم‌جا، بدون اشغال فضای اضافی
🏠
با این دوربین، هر لحظه از محیط اطرافت باخبر باش!
❌
قیمت قبل: ۲,۴۹۸,۰۰۰ تومان
🔥
قیمت ویژه: فقط ۱,۷۹۸,۰۰۰ تومان
🚚
ارسال به سراسر کشور
💳
پرداخت درب منزل
👇
همین حالا سفارش بده و امنیت محیطت رو بیشتر کن.
http://memarket24.ir/briefcart/180124/g-en50734</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/672047" target="_blank">📅 12:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672046">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‌
♦️
سپاه: سکو و موشک‌های هی‌مارس در کویت و محل استقرار نیروهای آمریکایی و ضدانقلاب درهم‌کوبیده شدند
🔹
در تداوم عملیات مقابله به مثل و پاسخ به جنایات جنگی شب گذشته، رزمندگان غیور نیروی زمینی سپاه در موج ۱۵ عملیات نصر ۲ با رمز مبارک "یامهدی ادرکنی" علاوه بر انهدام سکو و موشک‌های هی‌مارس در کویت، طی یک عملیات ضربتی پهپادی و موشکی چندین محل استقرار نیروهای آمریکایی و ضدانقلاب مزدور آمریکا و اسرائیل را درهم کوبیدند و تعداد زیادی از ضد انقلابیون و نیروهای ویژه آمریکایی را به درک واصل کردند. عملیات مقابله به مثل ادامه دارد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/672046" target="_blank">📅 11:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672045">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dw6Ks5DTIG3ibACpHCoertmTSyaJJj7hm_Dx0dXki9KqzBr_dxVhYycAtZXNy9HLjRZzmcFVXKgNYIAZWmZv0isr20q4MJHlXwZZD6DCvMufkOy8sTLJHQOz46P6pXt_7t5M8kwnPZjgtIoTBoyf94SCgj9lZfHcsuIwAAK_-qkBNOmycZk4UObYp956nswmGKOZ7s4_ORvR08jftAe5qv7JvWDFTYEUNsFGmlQWjjFdQKxOoJSS9Sxq8H60Weyd2ecDBSLo7XdMG1EB-0l_g6zcDzl1I_OpIWJOO0eO_FTJaghRb3J399_sprL-0ggELR9QgAvzbWWW0NZiJPfQbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاربر توییتر: آمریکا شب گذشته وقت خود را صرف بمباران پل‌ها، بیمارستان‌ها و نیروگاه‌های برق در ایران کرد
🔹
در تهران باید این پرسش مطرح شود که چرا این پل هنوز پابرجاست؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/672045" target="_blank">📅 11:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672044">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mgfqhw1qyNVnB7_eRwJ6CqKUZ6u64-QOakqUM2FcY4BxWSpOvkzrZAHp1yDALMsBGvTVRpP74IMJywEToVyq_9kNhIxA8JkDgpWRVd0kk1HpFXnAAU58VAhz4jCJ0B5wDhVW-WhAXkPEHkkOeI9KRIM3rn7__EBh0sBuhfhNatcANKt27MhOmJWI59IV8K4WArRW6x3YOpAb_rBhjHpRPB_Trup17gGKJSKM1HjbQViGmbuJC9-SrfwKsF_gw4FETImMQy-RGqHQzwnFwW5fx9JQfpHRM705btdvuQrPt7pYlQym-mzEuNzx2eIcCefH0bWLsadqO5tnVi8k7k8p_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای: تخریب سه ساختمان در شهر نظامی زاید ابوظبی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/672044" target="_blank">📅 11:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672043">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9321113987.mp4?token=T4rnJG_bP6Q-5wjwFxiemjSG3oTvd5pbHy3ckiH1kUGxHYjfiAXGmvaB48ZQNKpD5n1wQaCe8eiLNzDmPugkjj1aqV1yBoVs3Zs77eBvTZTH395f4n-ITwdo00ztG3s8Pb-8bHAtPg8IQHIvIeM7ED71TAZzK0OlU1IDjq3UaBxJLzsSY7HqZV9ulXCfvJZ4sgn2URsdH3ZwyWEgpuMg9Zu8RaeWd3j8BXx-7d6WvCSqpmwc7pmSbiSslr7FniR4_TmzqP0QVPLWriy_EBK4DFwju1XAPAlZWWG368FRDAcHPI2GVSJygeEOBs39ypVrHV4yoW0JvjrC0UbsMbJ82g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9321113987.mp4?token=T4rnJG_bP6Q-5wjwFxiemjSG3oTvd5pbHy3ckiH1kUGxHYjfiAXGmvaB48ZQNKpD5n1wQaCe8eiLNzDmPugkjj1aqV1yBoVs3Zs77eBvTZTH395f4n-ITwdo00ztG3s8Pb-8bHAtPg8IQHIvIeM7ED71TAZzK0OlU1IDjq3UaBxJLzsSY7HqZV9ulXCfvJZ4sgn2URsdH3ZwyWEgpuMg9Zu8RaeWd3j8BXx-7d6WvCSqpmwc7pmSbiSslr7FniR4_TmzqP0QVPLWriy_EBK4DFwju1XAPAlZWWG368FRDAcHPI2GVSJygeEOBs39ypVrHV4yoW0JvjrC0UbsMbJ82g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از اصابت به سامانه پاتریوت آمریکا در نزدیکی اربیل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/672043" target="_blank">📅 11:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672042">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
سپاه پاسداران: جنگنده‌ها و سوخت‌رسان‌های آمریکا در اردن را هدف قرار دادیم  روابط عمومی سپاه پاسداران:
🔹
در واکنش به حمله اخیر آمریکا به زیرساخت‌های بندرعباس، در «عملیات نصر ۲»، پایگاه‌های هوایی آمریکا در اردن را با موشک‌های بالستیک و پهپاد هدف قرار داده…</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/672042" target="_blank">📅 11:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672041">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
سپاه پاسداران: جنگنده‌ها و سوخت‌رسان‌های آمریکا در اردن را هدف قرار دادیم
روابط عمومی سپاه پاسداران:
🔹
در واکنش به حمله اخیر آمریکا به زیرساخت‌های بندرعباس، در «عملیات نصر ۲»، پایگاه‌های هوایی آمریکا در اردن را با موشک‌های بالستیک و پهپاد هدف قرار داده و چندین جنگنده و سوخت‌رسان آمریکایی را منهدم کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/672041" target="_blank">📅 11:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672038">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
قیمت بلیت اتوبوس‌های اربعین اعلام شد
مسیر تهران ـ مهران
🔹
اتوبوس ۴۴ نفره؛ ۱۲۵۰ هزارتومان
🔹
۳۲ نفره؛ ۱۷۰۰هزارتومان
🔹
۲۵ تا ۲۷ نفره؛ ۲۲۰۰ هزارتومان
مسیر تهران ـ شلمچه
🔹
اتوبوس ۴۴ نفره؛ ۱۳۵۰ هزارتومان
🔹
۳۲ نفره؛ ۱۸۵۰ هزارتومان
🔹
۲۵ تا ۲۷ نفره؛  ۲۳۵۰ هزارتومان
مسیر تهران ـ خسروی
🔹
اتوبوس ۴۴ نفره؛ ۱۱۰۰ هزارتومان
🔹
۳۲ نفره؛ ۱۵۵۰ هزارتومان
🔹
۲۵ تا ۲۷ نفره؛  ۱۹۵۰ هزارتومان
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/672038" target="_blank">📅 11:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672037">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af0cedef3b.mp4?token=s6RSaBDZ10LohfPjKSZBOp9FTXwxSD2LOAPxGiVFRRWts17QjXhvOodiC9WF1HpjH0Q2Tl_nRiWM5GpT-GSYG8KyXP9-b_Ve3S6DZ_3y8xp6DPMtfPBPGL7IYxkZYV-_nm0W63SYyHVHfWgkVDZx3mxTOAVHp6lb7N3VQv0gq6TXjFb4KONS7nSr8MOQryDDsJ4J98EfO1I64yYVdaD2f9ZJ92mfVZyC3C73RC5hjVrgTXG0FLgkwyF7yp9SqzFSOfZGtmEseRos7Gg88ceK4GpHtTQLp8w8P8BMSlks9aZIy1kbBPYFpgbdLHzjEuqiV9Sa2ualk7C5nF6gG9Uznig5jxop_148KIbdb68ZI27F89BHeuGKHK_CJF7ZjZuoH21lDdgVFegaLKg4unKxehJ8ofXayrnypndhJ0BJcD5nRaGHyyW7ZQbghLySJQJmhs1Jiroy_OawEBKNgRlNO1BMr8gjlCb3l4Osu_eb8DQXVGwlvqWbIBMEjMMvoOo1HQ7WVO1Tku0T62LER2UYUFo31Jmpjq8wLobBkL2N3hTKB9U77ipzqOdOzT_28vXj68rER966JAAfE92C80_Bf6Mbq5nPg7LbgtdkGb2xSm3JX6g3EBWgsDyovnCGThYIHXBBiK41sb4JlF6EXunBiNi-kVnkJgC69M3sgcByAec" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af0cedef3b.mp4?token=s6RSaBDZ10LohfPjKSZBOp9FTXwxSD2LOAPxGiVFRRWts17QjXhvOodiC9WF1HpjH0Q2Tl_nRiWM5GpT-GSYG8KyXP9-b_Ve3S6DZ_3y8xp6DPMtfPBPGL7IYxkZYV-_nm0W63SYyHVHfWgkVDZx3mxTOAVHp6lb7N3VQv0gq6TXjFb4KONS7nSr8MOQryDDsJ4J98EfO1I64yYVdaD2f9ZJ92mfVZyC3C73RC5hjVrgTXG0FLgkwyF7yp9SqzFSOfZGtmEseRos7Gg88ceK4GpHtTQLp8w8P8BMSlks9aZIy1kbBPYFpgbdLHzjEuqiV9Sa2ualk7C5nF6gG9Uznig5jxop_148KIbdb68ZI27F89BHeuGKHK_CJF7ZjZuoH21lDdgVFegaLKg4unKxehJ8ofXayrnypndhJ0BJcD5nRaGHyyW7ZQbghLySJQJmhs1Jiroy_OawEBKNgRlNO1BMr8gjlCb3l4Osu_eb8DQXVGwlvqWbIBMEjMMvoOo1HQ7WVO1Tku0T62LER2UYUFo31Jmpjq8wLobBkL2N3hTKB9U77ipzqOdOzT_28vXj68rER966JAAfE92C80_Bf6Mbq5nPg7LbgtdkGb2xSm3JX6g3EBWgsDyovnCGThYIHXBBiK41sb4JlF6EXunBiNi-kVnkJgC69M3sgcByAec" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چگونه فیک را از اصل تشخیص دهیم؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/672037" target="_blank">📅 11:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672033">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kU66h9au4Dmq5VGpMjuqfTEzWJjj91Q9FH-s85cHAuPC5JeOFkG7sm9p0ZJksBkEW1xwGKykhU2CcsmNzRFFPs5VnXwX3CETPCG022Xtsy1u8GewmdkeWVqCAbSML13JjKZsvWmPVNGsy_de11Sl8W37wfYnK-DUpi15UWjeRvPzpZoV5ffNk4iP2Nb8IjPkxTuSzwz8Z2p29yAafN6uqhtEzhoCun8oVnK9siviu6NS-wz5WKWQE18gmkU28ax7IpHNz4iVhDA3_YWamsv4Jy_u1IuQ9r4fnV5SdIpxiJr_QUYgi40bTfAS5FpG7mdZGvFZ4_b-Q6uifyh8_I-FtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sYdnfLLa9LtwFVxDMm-c5GWuEPF8oeEwKNcimv6kSXwDYlRse2hwCST0nsTHlYV4k8xVYPUZbO8rEi5fXemf2dZl_dTLgoh3lUDXxG_JyWvXMOnFGv9-f9-KWSR5X_5tt1q1EIu12fjqaMd7drKe6CFbKDfl7rFTjstTkZ-exiwW5m_W9gtkD2fMaGVKxxG8ER17b6MaLAsrD8wvptJAY3sKOP_A9_8hx0BTJIUg4Xp6pY2DsUiK0t5HZbvOe_f6xnNbMBVZ36E630EorWbqeD7vbuSftOx-fC7t_RRcFrWpfkc7vBGCda1X-xr_XcyNdnDilib_vA0-thYCh-YrLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b4Uvtu1E5WL-r7uUyw0G7r3WhwEw7q8Sik_Ls-7B6GstkY6J_FW_65ojy2rXWH1KfjHjlDy6O6o4HbJg67o94ROZu7qQOJKPZu1CwVvCpk5TdBfix97-KIagov2qUSVJs3CgwQbUmauJC81ZSMCY2SrEmYQfhJ6z1ChKhfo3PkYf84w8s8j80sK_tRJcFJVxSPsLPgvMoysevA92g449YSVxzD0WMFy8EYxOHXQ9iMt8t4P8aPVV5aKPlW5zidbLTaXCOjx291licDZFgSsNdwMaCbyzaawbCebX-ISDntj-D7bFoGxtZ8m8R_xMsr0jAa8fo58HvhHxiHsQF2VF1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K4e6qTOoDBmegQGgYZPK9OnCIlonXdG-04xvdWshIYKODla7UIkPbEjq91VA7QnEdI23Ls8NtCfm_S7nxN9OdPWgRVNEUN2ACMmSghUbucTD_H4XCtUtw60N1mAHij03nfef-k3Gl4yn_pWiVVQIm2XCnqe54BAJIdNQzixidQuZw_hqKDKJqJpCNGaJJMbCcBPmSYeb_0RUGnOoe-3ajKCO9eVXmhqDooHHcvH_hZrBcve64ayVnKhZWieNMDMIfAb2CfgUMwjiRoXQ2kh4h-fCxEaxgs_4kmdbcfmiLzTWGH2vPhiltpjqSfIahtmPQLvDI_1ZCxJm7eOUZ1tIGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
افزایش پروازهای نظامی آمریکا به
غرب آسیا
🔹
داده‌های منابع باز (OSINT) از اعزام دست‌کم ۱۰ هواپیمای ترابری C-17A از آلمان به پایگاه‌های آمریکا در خاورمیانه خبر می‌دهند؛ هواپیماهای اطلاعاتی و سوخت‌رسان نیز در حال حرکت به این منطقه‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/akhbarefori/672033" target="_blank">📅 11:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672030">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7GAZInypPYfZXkkC95iZVJG7GQqhjucVOuTeoCIzPA3yFvvs_O9SLwgKzYCcHOnd1cT6KvN7w_Q_MffWnsgcban-SE2I3IuJTl42Dj89oTdmfR0XYLS8qwoophgtIEHThF4FIqKPOlthDRbzIHcGLpnvAcwavObNqk_8M-21sbmgfIm6DVa3fbC4Ae9UvNIEIAhZEJhlVnIf3glcUMofgpdaGrq3cdC2aBY9u2kea-jHVPGYnqvqcL7LslMnZtfmJUIX20GgFU3YkuSGEmKN9Mr_FbiYLElK6PHH0-nTLqa6zQUMs10CbImWcMbtPKyKqco7wWX9MX36PEDCSg1_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس مرکز روابط عمومی وزارت بهداشت: تا ساعت ۶:۳۰صبح ۲۶ تیر، شمار مصدومین حملات آمریکا از ۴۰۰ نفر عبور و ۳۸ نفر هموطن شهید شدند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/akhbarefori/672030" target="_blank">📅 10:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672025">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
حمله به نفتکش در شرق خصب؛ خسارت ساختاری به بدنه و سلامت خدمه
🔹
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از حمله به یک نفتکش در شرق بندر خصب عمان خبر داد که منجر به آسیب ساختاری شد؛ تمامی خدمه در سلامت هستند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/akhbarefori/672025" target="_blank">📅 10:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672022">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QaDm_XFydquA72RPeLIjzH8IlkQ-1DJ6-x_GzMr8A2g9kok-wRej0QPxH-T01oviP7C4Pw59I0tgYnIhW88UYakk1bAqPYsXpbN_-Y8t9JPhmhAv9tSvKuO-vhZSR0nKpXUp4E5iKjxB_oecpzBxxz1gac8qwoV48J5jCvfATEh55hKax-IdY4rUwLfF1f5Ft5bzLjqXZjeKcrIGMWXpGHYUnZiw6gJ2V_swKw6PTIubcCbdpbK13A-xQMEAQuZm0uTnW0GVRUQKaoVwoEH77dpEXEj4JezwZ-1RUaFCEcKP7PbrrkXocZcNvaDOG62acsLE4vWs8s6C9y_NY5nnxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شب‌نشینی ماه و زهره در آسمان امشب ایران
🔹
ماه از غروب امشب در کنار پرنورترین سیارۀ آسمان یعنی زهره، مقارنه‌ای را با یکدیگر خواهند داشت که در آن تقریباً ۲.۶ درجه از هم فاصله دارند.
🔹
این مقارنه از حدود ۱۵ تا ۲۰ دقیقه پس‌ از غروب خورشید تا ساعت ۲۱ در قابل دیدن است و ستاره قلب‌الاسد را نیز می‌توان درست کمی پایین‌تر از ماه و زهره دید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/akhbarefori/672022" target="_blank">📅 10:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672020">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufITZQWwVuQq1uTsW6dLDEB9Qya9Twm0l2VMQVWeQq-JwBV8vM2AXfAe1zvoXY2ygo2ZDD8d8gmXV7hcZNJ5YryV6YSEy-PTZC0FdzH_fREi1jkQo9LTFRlfTWCnqjLtRV_5uns6fx7UXhprm4i3iBl-w_eaIjfkoYsovus7qTKMLMESRUbw9TyW5EzYHwpRYecN3A_bm8oKbS83zhP_s-l2tyTxg0jC4XqG0wltuvWJYKj0MPsUnAFW_RwLEXLj552_RiwXvf8FgkW5uICo6VEIUpvNZnEepLxqpOuOWAZ7m_oZJtk6k7BpBrtYGpVO6BMgW0vPlLGw7X9EbuoRBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شما نفت کش تصرف کنید
ما جزایر قبلی مونُ رو ان شاالله</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/akhbarefori/672020" target="_blank">📅 10:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672019">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hll5YJhHLfeRHaB3G-bW7CYp_TdGhEPKpipy8Y0kpo_vK_say0VkkfEoV0kbG8haOTjvBZRmKhqlIgkn1zkO8hqeTFDAy1JYclJ8aWr6IlObT8d4JR1YsQPm0jxTIQRnNYSkijI_4MwPD0qH8zy8S6rEihLoSIRtB2h-59-XFuHRP6oe4leFY3sxNkcn01nYyQayw8GCPkcQdUih60-ESJ8yo5w72x0p7Egse323Bg_vNObOmyjZy9eWjqBfgOKreGZmQ6GKfwBStMQd6APgtSDWF5bP0_98bixW8qKcdzIiBiQ8ADDsnZb1SdbcnMzeOsf6h_CxLGTcMHRMy66aQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش رئیس کمیسیون امنیت ملی مجلس به حملات به جنوب کشور: روزگارتان را سیاه می‌کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/672019" target="_blank">📅 10:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672018">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaQdHXeZfB8Q6OOI2-QSha_5TfFe0J-vOMjiIBSoilLoL3ugnbdEPYWyL8Mf6MGoSi86TuZr_UR-f28afzMTNeAgQMieudTT-H0ApvcXGfP8OhSAbmO3g4CWHIN80f9AY4zGscS7tIbn6D2gE4qhp63ompZ3J5MHF8MNAhXFoLFVw5gf_KTDxe64P-_4yjf3zAZV8fmaY11Jznx6bSYOs1zSaDWMBfXsGSJJdJ32aA28G4syRcRD8bSiusNKcd6nuNFWh5gj2eNWb2pAaxNlw68iEgnbE8SlSX0KlgHFwNAE_DIlwHkQcOSxodPjHbv61KTlxLHnavbodt0WKcsp4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هدیه ویژه فیفا به قهرمان جام جهانی
🔹
برای نخستین‌بار در تاریخ، قهرمان جام جهانی «انگشتر قهرمانی» دریافت خواهد کرد. این اقدام با الهام از سنت‌های ورزشی آمریکای شمالی انجام می‌شود و انگشترهایی با تعداد محدود هم برای هواداران در سراسر جهان عرضه خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/akhbarefori/672018" target="_blank">📅 09:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672017">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
حمله مجدد جنگنده‌های آمریکایی به برج مراقبت دریایی چابهار
🔹
صبح امروز ۳ انفجار شدید باعث وحشت مردم منطقه شد، اما منطقه مورد انفجار مشخص نبود. جنگنده‌های ارتش متخاصم آمریکا ‌برای سومین بار طی روزهای اخیر، برج‌ مراقبت دریایی بندر چابهار را با شلیک سه موشک هدف قرار دادند.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/akhbarefori/672017" target="_blank">📅 09:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672016">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mfv7sQSJgi24bFbSzaaJahTBOHef1mDBD_Hk0o78Dj7BLFontpUohlBL_iMBCnsHj7Tb4DFoTYYGL552qfPUXnmtrJ0qYGg4yJzHvtcYth88McsUzFAxmY4nXhsdugiXMYJRk8ouqyNRt7FmzH3EycoASpiKIXgd4etRuCRqNhWx-md1z7T88B9xa265pNZwZZbDkbOclbJRTCzTAZM_JVa1wSv5Pj5WUeb2WPoamsuOEa6WVGlKHCpUSvsnWinBV_pFCcbFLcZA8kNu0W-z52v6ItsDFNgfDWrTNfCICpNWgc5yP5SOD8us8ZvWN_WKqXoYu_Mxl9i4zsWLNslgqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سقوط قیمت طلا به زیر ۴۰۰۰ دلار
🔹
قیمت هر اونس طلا در بازار معاملات آتی آمریکا برای تحویل در ماه اوت، با ۰.۲ درصد کاهش، به ۳۹۸۸ دلار رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/akhbarefori/672016" target="_blank">📅 09:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672010">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k6lFLE4ThOL2uolHdoVCVbaCL0E3cwdIWTPhCkOsQ5W_aBRhVIqGvGF3erLDa1YNJJ6UJwQ3_yFRwtqyu-Nip5Tkc-WFoT9A5DyyHx9i75CJlGRcjvinohOnFBM_fd6TML4k7LkoCm68fLZ7_q8oGSDETYNUtSSXWd6wrgIE8yELKlPlZTLPIAXhdcpfhzPypQIjWp5sTbsR5UHrxkDUCC2RaS__bRRGLGLK7fbk3ZidEKDdVsCiZpXladBOy_ApevYcCcnFURyeA_P0VBCbzzBIJh-m4E9gxL68YIzFW_BWN7jto90SWp8PtF6FAvwqBv6O3LWPAFJhf8b4ujmr4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QHYxEShxjQUeumfPSh3TVSi2pMZPnLql2oAliCvLrYPCfas4qs38abf1KZL1-LVhulohfqISVmAQHLNd5EyJrtXV12htdQnOiUUajMVcK0s3_-hWvc3cpn1YTsGoH1TQs-JPhrPljPPzomRb936aTZh5gZa7SsNOuSi8WrU3YOSstOK5-XILuzl2KruoEIebSxzTyCIIwWOlRc_KweR_Z4JaY2O1mRFE4wR3TPbbga3mFpTACD3z4eW9Zh-WAcpzzt70E6Rab9-sDPGgsuT9F8JDs4U4AfCvG_Og-4L6HhK5PMYJF7D-tbn3bIcE_Ve3t2F4lCuXrpa7__4GSvrMSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nPIofuAMUqU2pFYZHHovNZv6kjlrXZ-3Px6jc6FXCWpl1gEuBZo6JqPrBK98z6vF_39tlKXLcEtEjxHiduXT46vUCNxyseqc_HXUwo1l2Zww2O42Y0O7GFjlNrMdDLW9kNB36QAEl03nQWhlJ2ibKPcagIM1HaiSgzMYOYwETTmLs6d2ota3VjXog2O4vClJ2bAXqpN3fAUqSZlk-1150ItIMesmf4iBIDJ2vJSFIQ_7eQNNlb6hLmAVyxB-wevMiO7HsAVbx4ZeFeIce1P94mA771-lO4sebkxeB0iG0i2xH7lbIdF4VfMSuVxGti5vUd3f2F7BI_4jTUYB1-l3Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rOoAGLF2F-tloruCVl_QH37Vpf0bvmmvjdVQp_NuQZn2ZG0jRw5vG1WU99ONL3tgmHNC8ute8DytHeKNDqukhpJyewH3uqC_vK2WrNulLd97FLsmShlAPSyStjWyXOFmXyJfzfdN9NaF4ck5fbpR0KdVUYqRTU0kU-0pQFdgahD9qzrh1uZEJZ9SIhc9s3kXLmirLPzBI2AQICeLelmCgxQqy4BfEQcvc0vFQBXz79X6BNyapUL7UCJ-5eBQqFjpPaC1urvb6zhIlUvbH66foxZ1OQdShHaaRm1Z3WZ_PqmoWEdqRkifQKGsf8kwi8Im6mFj7xvw8prDvgPDje6gHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RcfEwaH_eurUs33M67jt9yMZEKxOc7RLrs0gWk21qWs-f53I5XRjDLGGnKs1NJPpsJHVsuhmReauY4c89TTcA2FzZyDcdQPaXa8GJaUQFjW_xMb7zdxK8qx-kJIo_S4t_3R9D4zzUcVqEJYNm99TL0pfkcmvvS7pAZFneHWhNedsX90G4jn_K-rQxzwloLQHUjAEBpjECfgleZOHY3xSjMLG56nC3nKLyvhKJrHeh94aF2kh63vbIUU5yapYY26jfIa4zPgTMaO0gohoOoQCf8ovJsTxoY1zePN4eKyhRPG-OKNAVGm9etYKHxi1LxJllPQIbTvVWvQ3EXEIkIThhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/husns5CDeT0exdyrpbmFECj7YysYmev2p5jr8pc0onv_lm4pWkCZ9Zdb-A4OJygnMeGbkPRoQgpyh3KyTybmLVQecisJYZfCrHVk8nqPzLRXBIfBgp6rfpFVhwsSKYPwWfkYRM-SdOKRTMadqqAmm8qbk7V5NfQzmJJTPXWJDvQp8DIztXSlNQCtqAuopH_yN05iVxZVocaXU0P_JltiW6URT0js7ctYMuDbBPSiYcmbGRzJRn7ujf3S84-_fDY2hy19LLR5uEtXeDpb6C3fCuRkUqRfMh5JG3erUMMhDJqMIpSGkY_JJ_f93Fqxuu1qBhYlfzVNabzCcnMHS5RK4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۱۰۰ ایده خوشمزه آشپزی که شما را از تکرار غذاهای همیشگی نجات می‌دهد
🍽
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/akhbarefori/672010" target="_blank">📅 09:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672009">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
پایگاه دشمن در کویت در پاسخ به جنایت ارتش آمریکا، در به شهادت رساندن مردم غیرنظامی به آتش کشیده شد  سپاه پاسداران:
🔹
شیطان بزرگ، شب گذشته باز هم به جنایت جنگی روی آورد و با حمله به مراکز غیرنظامی، خدمتگزاران مردم در مخابرات و راه‌آهن و خودروهای عبوری، تعدادی…</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/akhbarefori/672009" target="_blank">📅 09:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672008">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
ادعای مقام آمریکایی به وال استریت ژورنال: حملات آمریکا به پل‌های ایران با هدف قطع مسیرهای تأمین و پشتیبانی به سمت بندرعباس انجام شد؛ جایی که ایران یک پایگاه دریایی دارد و از آن برای حمله به کشتی‌ها در تنگه هرمز استفاده می‌کند
/انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/akhbarefori/672008" target="_blank">📅 09:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672007">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
ارتش اردن حمله سه فروند موشک ایران به خاک این کشور را مورد تایید قرار داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/akhbarefori/672007" target="_blank">📅 09:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672005">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/917fba8769.mp4?token=Gj3KmdByzSiI_Po3Qy_5Y31xREEmiukc64QQwGCoMyKldN0iA2B0qgxycfPrxO772i-FPiELQS8hb6reUPytfCx_P9FSD4v8zB56Fq-X2-67KVoAHesnL2T4vACETc5pZ1JcB5U-x-_zRvr115O9BsMiiQABCv2oGPG5O2N_kCc4bLnmZPYwY1mF-l-nJt01cSRXqVWYjT04uH1n0W3af3uQuJWBed1UnS2kKojpfHJcRrIF2QoIAqIlmtOZZIizTLK2QbqxkZYafVZFcvfZaNuVox2suAEhCwka0QzhvFw_hUmeQRQe1563KxpbycXRMTynkgg_TVCR36EBFpHuVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/917fba8769.mp4?token=Gj3KmdByzSiI_Po3Qy_5Y31xREEmiukc64QQwGCoMyKldN0iA2B0qgxycfPrxO772i-FPiELQS8hb6reUPytfCx_P9FSD4v8zB56Fq-X2-67KVoAHesnL2T4vACETc5pZ1JcB5U-x-_zRvr115O9BsMiiQABCv2oGPG5O2N_kCc4bLnmZPYwY1mF-l-nJt01cSRXqVWYjT04uH1n0W3af3uQuJWBed1UnS2kKojpfHJcRrIF2QoIAqIlmtOZZIizTLK2QbqxkZYafVZFcvfZaNuVox2suAEhCwka0QzhvFw_hUmeQRQe1563KxpbycXRMTynkgg_TVCR36EBFpHuVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از اصابت موفق موشک‌های سپاه به امارات
🔹
در تصاویر ماهواره‌ای منتشر شده از پایگاه الظفره در ابوظبی امارات انهدام چهار سوله نیروهای تروریست آمریکایی به‌ خوبی قابل مشاهده است.
🔹
این خسارات در نتیجه عملیات موفق‌ موشکی روز گذشته سپاه پاسداران انقلاب اسلامی رخ داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/akhbarefori/672005" target="_blank">📅 08:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672004">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/438027df0a.mp4?token=T2nIFf_1BvMh992V9Hrb9lxOR7UxR6LRLTHZwH3Wx9aGj5J-xfK6AdNO_zK91jfgwZ1WxOpTHqAVayuy92PWvRy6m0SVjLXHWntq4qxG8E5vrcbWhbKCSsJU7H_vLCe4RLktSzBHiQK7VZI5RsQeTyUjiwDwYpuU4mz9XBN1vLuTKrDclsUe1VEqqqHYq3JuAKuSbnPq9QT03BkcBqvHpgzp3oLh7wg87nEoydD_gks7JoNCy__PE69N4gc1R8gQggnGQtL1-prMs50YhHVnDHIP3_lRW6jEjuwwEsZQb2ANgYJhzGO7IhsxdfT3EwLjwskTl-HnSw6wFuzJtaFwNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/438027df0a.mp4?token=T2nIFf_1BvMh992V9Hrb9lxOR7UxR6LRLTHZwH3Wx9aGj5J-xfK6AdNO_zK91jfgwZ1WxOpTHqAVayuy92PWvRy6m0SVjLXHWntq4qxG8E5vrcbWhbKCSsJU7H_vLCe4RLktSzBHiQK7VZI5RsQeTyUjiwDwYpuU4mz9XBN1vLuTKrDclsUe1VEqqqHYq3JuAKuSbnPq9QT03BkcBqvHpgzp3oLh7wg87nEoydD_gks7JoNCy__PE69N4gc1R8gQggnGQtL1-prMs50YhHVnDHIP3_lRW6jEjuwwEsZQb2ANgYJhzGO7IhsxdfT3EwLjwskTl-HnSw6wFuzJtaFwNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از ستون دود برخاسته از مقر تروریست‌های تجزیه‌طلب در شمال عراق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/akhbarefori/672004" target="_blank">📅 08:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672001">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
اطلاعیه شماره ۱۹/ حمله غافلگیرانه به مرکز فرماندهی عملیات ویژه دشمن در منطقه التنف سوریه در قصاص خون سربازان شهید ایرانشهر  روابط عمومی سپاه پاسداران: بسم الله قاصم الجبارین و قاتلوهم حتی لاتکون فتنه مردم حماسه آفرین و شجاع و بصیر ایران اسلامی؛
🔹
در پاسخ…</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/akhbarefori/672001" target="_blank">📅 08:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671995">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
اطلاعیه شماره ۱۹/ حمله غافلگیرانه به مرکز فرماندهی عملیات ویژه دشمن در منطقه التنف سوریه در قصاص خون سربازان شهید ایرانشهر
روابط عمومی سپاه پاسداران:
بسم الله قاصم الجبارین
و قاتلوهم حتی لاتکون فتنه
مردم حماسه آفرین و شجاع و بصیر ایران اسلامی؛
🔹
در پاسخ به شرارت‌های ارتش کودک‌کش آمریکا، رزمندگان نیروهای هوافضای سپاه در موج یازدهم عملیات نصر ۲، با رمز مبارک یا اباعبدالحسین (ع) و تقدیم به سربازان مظلوم شهید بمپور ایرانشهر، با حمله غافلگیرانه به مرکز فرماندهی عملیات ویژه دشمن در منطقه تنف سوریه، علاوه بر انهدام یک سامانه راداری، چند فروند بالگرد خاص عملیات ویژه، در قصاص خون سربازان شهید شب قبل در ایرانشهر، تعداد زیادی از نیروهای جنایتکار آمریکایی را به درک واصل کردند.
🔹
کنترل کامل تنگه هرمز کماکان در اختیار رزمندگان شجاع ماست و تا زمانی که شرارت‌های آمریکا ادامه داشته باشد، یک قطره نفت و گاز از این منطقه صادر نخواهد شد.
و ماالنصر الا من عندالله العزیز الحکیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/akhbarefori/671995" target="_blank">📅 07:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671994">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsN1btqSXzNzAZJJ0u0Vpqanqsylyv_FXiYmb_TPnx9-HNnjlldwFDuuJIpXk7zathuSlw_bROzR20gqjT0E_PABDHb4o8YBFQOANUIBzvBGcqa4IKYDhjwtCU4H_3Sm5x3hsq9swBbFld3UjPbDM_uH4GyHuoNgRgXRmN1z1qPTK8DSp9c2OKuQX2-biei6zFyB9t51txIJBN9KHgy6KZEUBpeVoWhaNagZEDGZWrc-k_Rg89XYjfckVtqiEVeJu8UttJsalDcqtBD7TPnc1WuWeX4Ukhh8cwWDt8HrsPaKiiF6gWLrM1SOdozWao75lWLZBQ0FcS7VjLwiqdFVdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز جمعه
۲۶ تیر ماه
۲ صفر ۱۴۴۸
۱۷ جولای ۲۰۲۶
جمعه‌ها
#دعای_ندبه
بخوانیم
⬅️
متن و صوت دعای ندبه
@AkhbareFori</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/akhbarefori/671994" target="_blank">📅 07:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671992">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
اخبار تکمیلی از حملۀ آمریکا به پل‌های جنوب؛ ۵ پل مورد اصابت قرار گرفتند
استانداری هرمزگان:
🔹
در ادامۀ حملات تجاوزکارانۀ آمریکا به استان هرمزگان، متأسفانه علاوه بر پل کهورستان، پل‌های دیگر شهرستان خمیر هم مورد اصابت قرار گرفته است.
کدام پل‌ها مورد حمله قرار گرفتند؟
🔹
پل گریوه؛ مسیر بندرعباس، خمیر، لار
🔹
پل بعد از روستای لاتیدان (کلمتلی)؛ مسیر برگشت بندرعباس، خمیر، لار
🔹
دو پل مسیر کهورستان، لار
🔹
پل نیمه‌کاره؛ محور بندر خمیر، کشار، بندرعباس
🔹
پل روستای مارو شهرستان خمیر
🔹
از مردم تقاضا می‌شود با عدم تردد در محورهای ذکر شده و مناطق مجاور آن، راه را برای تیم‌های امدادی و انتظامی باز نگه دارند.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/akhbarefori/671992" target="_blank">📅 06:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671989">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwjM_UkNgB8bntpHKLcnsYdABqFdGHztTspHVigHSW69-zxyuwhn7DRz7gr1pU54CKLHKwc32IU24UV9ybz_Rh_sAmJOT7_B2jJehwySmQhGDyN2JjCmyuT5z9_2JRZaUnKEPReEGUdCVEuG8_LF_nuP-zQk2geH0kVAOb2tNIjf9UwTWg-d-RiOCwZ2Jt7Dq_cZRulfSN5-nh3_xz-jMyHspyiv48iH9awuWumrvEWWUoKIHMkV7qrRbpTglmkYLOjwN21qwtaBt_3RJaIJHOGrGU9wZXOxLK5rtNLZ6ejJwb8HPM3V8Q01Djd5fIWAgmbU_gu2Xmk4OAQZVRNqsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
منابع عربی: پالایشگاه‌های نفت و پایگاه‌های نظامی آمریکا در بحرین مورد حملۀ مستقیم پهپادی قرار گرفتند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/akhbarefori/671989" target="_blank">📅 06:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671987">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd3bf9fd9.mp4?token=dbDS0wkJLrpHHmM6le6WY3p62H2d9kjswfaiksS0YccaneL2Jxn_zOhWxGK6Ljm_0NZNyTyWyeqcWEDf7tP_BMKzw4kVQTaHxxOnq8XSpQiei_VvxFzci_q9aFwgV0xgU5ISL-xFc9cDGSe6kL1GsVfQncxjGMsQSYSACDREHGHeYXbvUF-knvmxisIleueNIfC4zBRxMLge4nNfOoFUIJG5A_Dy-k4sc9pcr6olS_1IOczEEa9xf-EaR9G8s379qxPm9m2V5j8ds0Mhovlg4Ffrwyt0sANbnJv6hoGWZ4LRdz93vl2wCKfhdJcOSOj2bW-NR388S06ygI8WoZs6ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd3bf9fd9.mp4?token=dbDS0wkJLrpHHmM6le6WY3p62H2d9kjswfaiksS0YccaneL2Jxn_zOhWxGK6Ljm_0NZNyTyWyeqcWEDf7tP_BMKzw4kVQTaHxxOnq8XSpQiei_VvxFzci_q9aFwgV0xgU5ISL-xFc9cDGSe6kL1GsVfQncxjGMsQSYSACDREHGHeYXbvUF-knvmxisIleueNIfC4zBRxMLge4nNfOoFUIJG5A_Dy-k4sc9pcr6olS_1IOczEEa9xf-EaR9G8s379qxPm9m2V5j8ds0Mhovlg4Ffrwyt0sANbnJv6hoGWZ4LRdz93vl2wCKfhdJcOSOj2bW-NR388S06ygI8WoZs6ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرحلۀ دوازدهم عملیات صاعقۀ ارتش؛ حملات پهپادی به مراکز پشتیبانی ارتش جنایتکار آمریکا در کویت
روابط عمومی ارتش:
🔹
در پاسخ به جنایت‌های دشمن مستکبر و انتقام خون پاک شهیدان این مرزوبوم، ساعاتی قبل و در مرحلۀ دوازدهم عملیات صاعقه، پهپادهای انهدامی آرش ارتش جمهوری اسلامی ایران، محل استقرار نیروها و مراکز پشتیبانی لجستیکی ارتش تروریستی و کودک‌کش آمریکا در کویت را هدف قرار دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/akhbarefori/671987" target="_blank">📅 06:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671986">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
دشمن آمریکایی برج مراقبت دریایی چابهار را برای سومین‌بار در یک هفته گذشته مورد حمله موشکی خود قرار داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/akhbarefori/671986" target="_blank">📅 05:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671984">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe012d6dda.mp4?token=bd5Ky20B6EXCayrzC0sRjpS_7WERF0-8064CR5TuuN6CY08KiEN4lWEo4LlMTlJa7NCRKinXalDvfR4j8ujUveFHy2dt1885Mitl5-5W-9FbG6Wjo0g_xQTe_dtaZYVY1djVny1cWsQz2KZvWRSwLD6nIxvzsvAx5uIDYy6BVvQ_wuMPxHCYVkxjW-s9ckF-vI7UK38exuRg6U9NSHM6ml9mUd0VStzoFqn_j0yZ6Z1OkEzkuH2tq4XlzPq4ez5v_hz-lH-yxbzxauE_5KLyg8e1cnSkcyQvu8cCFL_5YSaGGSnquwDJR3bHseOTOZ6aDyvac1XYICJzUDS84XU8MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe012d6dda.mp4?token=bd5Ky20B6EXCayrzC0sRjpS_7WERF0-8064CR5TuuN6CY08KiEN4lWEo4LlMTlJa7NCRKinXalDvfR4j8ujUveFHy2dt1885Mitl5-5W-9FbG6Wjo0g_xQTe_dtaZYVY1djVny1cWsQz2KZvWRSwLD6nIxvzsvAx5uIDYy6BVvQ_wuMPxHCYVkxjW-s9ckF-vI7UK38exuRg6U9NSHM6ml9mUd0VStzoFqn_j0yZ6Z1OkEzkuH2tq4XlzPq4ez5v_hz-lH-yxbzxauE_5KLyg8e1cnSkcyQvu8cCFL_5YSaGGSnquwDJR3bHseOTOZ6aDyvac1XYICJzUDS84XU8MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: "روسیه، چین، ایران، کره شمالی و همچنین گروه‌های غیردولتی، توانایی آسیب رساندن به زیرساخت‌های انتخاباتی ایالات متحده را دارند."
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/akhbarefori/671984" target="_blank">📅 05:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671981">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38775e5358.mp4?token=TrPRlXD54G9_OXPcg-VwXXIQDiMUESgU5vkvx4YHn70crRiLgzNmbh2-UQDE_fd1dcdCMo2CYt5qIwhrYh3Cnf6PfMPw7g1Tgj8CW6Z8LPAoIz_ek84SGPGuPGFUtrim03zE8btFS23cV8PGpr-i6jA2609YSpNTnmelIh314G4B1xs6WvmEdVd5_WJXO0aB9gIr1DI20f_0J01BC5dMlzZWoCcUqow-EMLhsCbgURTQMa83UlRErzjTXYRJhsW2s0t_AfFVwnBZ-QwjJBcL6uED1cH7m-qu9OSxC1Wxc6tXXWF8gDQ_YyzISviEsLPgBQi39Dnz99nbQnqntNTOFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38775e5358.mp4?token=TrPRlXD54G9_OXPcg-VwXXIQDiMUESgU5vkvx4YHn70crRiLgzNmbh2-UQDE_fd1dcdCMo2CYt5qIwhrYh3Cnf6PfMPw7g1Tgj8CW6Z8LPAoIz_ek84SGPGuPGFUtrim03zE8btFS23cV8PGpr-i6jA2609YSpNTnmelIh314G4B1xs6WvmEdVd5_WJXO0aB9gIr1DI20f_0J01BC5dMlzZWoCcUqow-EMLhsCbgURTQMa83UlRErzjTXYRJhsW2s0t_AfFVwnBZ-QwjJBcL6uED1cH7m-qu9OSxC1Wxc6tXXWF8gDQ_YyzISviEsLPgBQi39Dnz99nbQnqntNTOFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای
خوک هار: ما در ایران پیروزی بزرگی به دست می‌آوریم و شما خیلی زود ثمره این تلاش را خواهید دید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/akhbarefori/671981" target="_blank">📅 04:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671978">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f6f7102a.mp4?token=Yd2dxcC88wGXr3M7RrE_XMWkIbZQgLyzXFh4PCmpvn11iUFNOS7Lj8fLFAB38oalyXJE0a2emBF84ddoq7wz3hFIjnqjUEwNBZMHPtFfL7K0jMzu7l_ACM6TwBgOLZglxubCC5r6Ckqm2uVky2E7EItJohpfV1zIQOR7NJpkLFtS_D6jKYfyvsu_zRu-S2S31-8186SaqOu9ZsHCMEbPEAE3aB189-wxay7v97OTsk7lCT0v-8quHCA7tx1hAar6rAta4fRukHVMFcgWX3PMfJ79EAe1zWkZrEKlazab2BB1ykuO4NdkYAUKUoKjwLl7ReaLIUypoK9INngqzJaf6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f6f7102a.mp4?token=Yd2dxcC88wGXr3M7RrE_XMWkIbZQgLyzXFh4PCmpvn11iUFNOS7Lj8fLFAB38oalyXJE0a2emBF84ddoq7wz3hFIjnqjUEwNBZMHPtFfL7K0jMzu7l_ACM6TwBgOLZglxubCC5r6Ckqm2uVky2E7EItJohpfV1zIQOR7NJpkLFtS_D6jKYfyvsu_zRu-S2S31-8186SaqOu9ZsHCMEbPEAE3aB189-wxay7v97OTsk7lCT0v-8quHCA7tx1hAar6rAta4fRukHVMFcgWX3PMfJ79EAe1zWkZrEKlazab2BB1ykuO4NdkYAUKUoKjwLl7ReaLIUypoK9INngqzJaf6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه شیرجه موشک‌ها
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/akhbarefori/671978" target="_blank">📅 04:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671977">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6552de3ed9.mp4?token=Sp9B3m8IDjAdZXK2OOvnanjRbyzH9SzU0oh7F__5s5FjWpeieeQQmjMiE1pAxIm6d-H1Gl_kcI9GUfCCbKX0jeerZqQoNRt2J8B6_QMd3CBhsHXyBFoMcHqGcoxlMTjBU6hEVrIu51DXyQ_1Cn7L4Do_w5qO1rxIAxIHcyzEyM7y4BgabBJC14c5Qa9kj83RbWHvLdGfn44gkAdtZf6QRMsC10Wi85YfO7-Al7M4-Aw9gYv5elF0OTve6yohUH-Y9NC7gmjU5EFlUKW4bwrZD4CoVdYI-6_wHPTYV1Lg2WI6dVrkEMamyQq9_MiO_Xp0xAUhwolkOZUPyLGsDuaN9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6552de3ed9.mp4?token=Sp9B3m8IDjAdZXK2OOvnanjRbyzH9SzU0oh7F__5s5FjWpeieeQQmjMiE1pAxIm6d-H1Gl_kcI9GUfCCbKX0jeerZqQoNRt2J8B6_QMd3CBhsHXyBFoMcHqGcoxlMTjBU6hEVrIu51DXyQ_1Cn7L4Do_w5qO1rxIAxIHcyzEyM7y4BgabBJC14c5Qa9kj83RbWHvLdGfn44gkAdtZf6QRMsC10Wi85YfO7-Al7M4-Aw9gYv5elF0OTve6yohUH-Y9NC7gmjU5EFlUKW4bwrZD4CoVdYI-6_wHPTYV1Lg2WI6dVrkEMamyQq9_MiO_Xp0xAUhwolkOZUPyLGsDuaN9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موشک‌ها در اسمان قطر
🔹
تا الان ۱۱ انفجار در قطر شنیده شده
است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/akhbarefori/671977" target="_blank">📅 04:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671975">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
منابع عربی: یک موشک ایرانی به‌طور مستقیم به یک پایگاه نظامی آمریکایی در بحرین اصابت کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/akhbarefori/671975" target="_blank">📅 04:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671973">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
منابع عربی: یک موشک ایرانی به‌طور مستقیم به یک پایگاه نظامی آمریکایی در بحرین اصابت کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/akhbarefori/671973" target="_blank">📅 04:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671971">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
شمار شهدای حمله به پل‌های بندرخمیر به ۳ نفر رسید؛ ۹ نفر مجروح شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/akhbarefori/671971" target="_blank">📅 04:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671969">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
حادثه در پل بحرین-عربستان
رسانه‌های عربی:
🔹
صدای آژیر آمبولانس‌ها و ماشین‌های آتش‌نشانی که به‌سوی پل متصل‌کنندۀ بحرین و عربستان سعودی در حرکت هستند، به گوش می‌رسد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/akhbarefori/671969" target="_blank">📅 03:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671968">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b757177081.mp4?token=oKiP0JwuqyowpmI3uqg-_WX1o5ysBmtZc3_7IM_cO-437RqnnjsSKElU63OLisKQQr5fNetCDOLS67dXTxHWTZNV5Qy2r4wVnGqx6nxHv0w7FDssmhRO9_NMu8MALLaHdnSQ0-HFp_AGmAC8HvKUINbAiWFS209nuNKAY-OgjSgfoYkOjn0EzjwHKxJ80N_vJ4i7LNAXbFHScWuFSw-zF9rwCLUz5Dr-4u1WHrWSNwUEfCkvA9zr0-FfQGgucojMd-Mg0gbtOnZuidoVPzq5vOGW0m9LljirAm2618Iom8PPC5Ad4DdiY6sqN293q6fQtXXDPxzWBRGgPCefNOEXYJ0MALgQbHBzYGe04XVrD8_i3PUF2J906lZFqM66t0mlRqvr8Uu-sJpmRc3qaTO-DYNgfRbbwuks5MUBTDWAeZ-yFju5MtXifNv8rCAGHA_le9ITGhoFVGSEzVFAQ7kxIDOEgB3X6Eisq4tnvQdjPcAr4GRHSu-OTX53DP_6IWe8Del8TYrIQHF0564bHFi-L0BClgI-xBIeMw1cnBOPhAsZ3qZ7hpxlxE-UDvGjSs9SFMfXFAhAJFssR4Pbgo1rHl5KfcS2efvlv3PgUhDbOEBel_blRQA90h66xtRvyMSzLzlribJCaLrDKKiBl-2lOHNiPaSRYbbToS1twvZVC3U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b757177081.mp4?token=oKiP0JwuqyowpmI3uqg-_WX1o5ysBmtZc3_7IM_cO-437RqnnjsSKElU63OLisKQQr5fNetCDOLS67dXTxHWTZNV5Qy2r4wVnGqx6nxHv0w7FDssmhRO9_NMu8MALLaHdnSQ0-HFp_AGmAC8HvKUINbAiWFS209nuNKAY-OgjSgfoYkOjn0EzjwHKxJ80N_vJ4i7LNAXbFHScWuFSw-zF9rwCLUz5Dr-4u1WHrWSNwUEfCkvA9zr0-FfQGgucojMd-Mg0gbtOnZuidoVPzq5vOGW0m9LljirAm2618Iom8PPC5Ad4DdiY6sqN293q6fQtXXDPxzWBRGgPCefNOEXYJ0MALgQbHBzYGe04XVrD8_i3PUF2J906lZFqM66t0mlRqvr8Uu-sJpmRc3qaTO-DYNgfRbbwuks5MUBTDWAeZ-yFju5MtXifNv8rCAGHA_le9ITGhoFVGSEzVFAQ7kxIDOEgB3X6Eisq4tnvQdjPcAr4GRHSu-OTX53DP_6IWe8Del8TYrIQHF0564bHFi-L0BClgI-xBIeMw1cnBOPhAsZ3qZ7hpxlxE-UDvGjSs9SFMfXFAhAJFssR4Pbgo1rHl5KfcS2efvlv3PgUhDbOEBel_blRQA90h66xtRvyMSzLzlribJCaLrDKKiBl-2lOHNiPaSRYbbToS1twvZVC3U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مروری ساده بر آنچه گذشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/akhbarefori/671968" target="_blank">📅 03:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671967">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5Lh2JsJRCo7uID8a8T7BJHcaJNsVfFx0b2MEQYxZi_yBpShUJwBcuORd785yfBdpRTBbh6UcjrMLdbRDxNKRFm2FvllOZcEqTGTUwoYiMLPCdBe3slryfQHuskg9Flcxy8LoieVRu4WGurRSEPGVDyJKslljia8wB2cMjorCqgyyCDqePOzkMBaoQOrE8cd_FhaUmTxUJA_tnKtPK4SZf1fNs3hZmJgwNKckqZMZw_0DonWSR8q-W5Iqgu4vmU-mhWJYlHn39tw96kF1iVMwOjN9x_Vwmu7AvK1szpsq0UjWdWSEJG7UsvC253rly_bM9lteT7il17T8RVM7yVd9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیت‌الله اعرافی: تفاهم‌نامه تمام شد؛ مذاکرات را ادامه ندهید
🔹
اکنون که رئیس جمهور آمریکا با صراحت و وقاحت تمام، پایان‌ تفاهم‌نامه را اعلام کرده و جنگ را آغاز نموده است، وجهی برای پایبندی به تفاهم‌نامه و ادامه مذاکرات باقی نمی‌ماند.
🔹
رئیس جمهور و سایر اعضای شعام و فرماندهان و مسئولین دیپلماسی کشور باید تفاهم‌نامه با اطاعت تام از رهبر معظم انقلاب به همان مسیری که ایشان تشخیص داده‌اند، بازگردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/akhbarefori/671967" target="_blank">📅 03:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671966">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf85bb926d.mp4?token=WS4CswCzCSBsP_xVEfoh5wtKDtgBViK5SXoqioaN4UMpV3dLCs3sFBBfx1UgyOel7UZGOJuhEiARAnVqZItCB58Jx4bCfLv2gGMU2NVunaLfuB-7mG0ymMA8qKxskqPbFV49ckKUgcxsiBsNoQ-IN6IdRUO6MweToKOu8_AkWAyRblpJSLvW-DRO6udZISPYBaZvuuNLt6FYog6YugeHQSelAsRY2I3Atb3_f9rbSGwCkJPlDLz37_SKtdQM89KOO47inX_DcjBONASDsCTPCpoz_W6z249pssCsBYuS4aRWCyeTEOE31s6n7vUrEvzBZk-Xy8OlRp7F48uoHjZmrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf85bb926d.mp4?token=WS4CswCzCSBsP_xVEfoh5wtKDtgBViK5SXoqioaN4UMpV3dLCs3sFBBfx1UgyOel7UZGOJuhEiARAnVqZItCB58Jx4bCfLv2gGMU2NVunaLfuB-7mG0ymMA8qKxskqPbFV49ckKUgcxsiBsNoQ-IN6IdRUO6MweToKOu8_AkWAyRblpJSLvW-DRO6udZISPYBaZvuuNLt6FYog6YugeHQSelAsRY2I3Atb3_f9rbSGwCkJPlDLz37_SKtdQM89KOO47inX_DcjBONASDsCTPCpoz_W6z249pssCsBYuS4aRWCyeTEOE31s6n7vUrEvzBZk-Xy8OlRp7F48uoHjZmrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک زرد در مصاحبه با فاکس نیوز: اگر ایران به بازدارندگی اتمی برسد، مجبوریم آنها را با احترام آقا (سِر) خطاب کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/akhbarefori/671966" target="_blank">📅 03:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671965">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa9fdadf1c.mp4?token=JZzUWR0wRURkYY16X5rD2iaz5xRZikPC7wwNqBXoqeMoVff8JEo5CClcSgzStyeOVM41nLQOTuLOAZ8UXmPrlNjiDxUReYjN1hfBlLVn-P6dmgMU_FcbbPi_vFQChayQ3LM4zHUkzysLsBZJwbecYMCLX4iSKBz3rLT65WqV-H7Od7JcIsZU35Zcpx1hpa4sB69Hwj939ulZtzBeyHD_tC8TDYr7K-kSL4yqyNvI8gT6_sbUL0gCVKQqnG7XOVGReGyiwoaR5cIXkvsn9_mrZvPLHlvfkKJ9fIIplXV_dy620WfGJjRLNsS33O63PZfLXQzJYSn8_CcqdtscDUGeDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa9fdadf1c.mp4?token=JZzUWR0wRURkYY16X5rD2iaz5xRZikPC7wwNqBXoqeMoVff8JEo5CClcSgzStyeOVM41nLQOTuLOAZ8UXmPrlNjiDxUReYjN1hfBlLVn-P6dmgMU_FcbbPi_vFQChayQ3LM4zHUkzysLsBZJwbecYMCLX4iSKBz3rLT65WqV-H7Od7JcIsZU35Zcpx1hpa4sB69Hwj939ulZtzBeyHD_tC8TDYr7K-kSL4yqyNvI8gT6_sbUL0gCVKQqnG7XOVGReGyiwoaR5cIXkvsn9_mrZvPLHlvfkKJ9fIIplXV_dy620WfGJjRLNsS33O63PZfLXQzJYSn8_CcqdtscDUGeDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارشی از وضعیت پل بندرعباس به لار پس از حمله آمریکا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/akhbarefori/671965" target="_blank">📅 03:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671962">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VmWyhlE68M0dKEGX1B6MukcgmjHXOndN8hhpp7WmfJhmvPf7pt5BhUsUvVmXyTTCpj_8WlmDXawVXeycEyERwO2QKkAFXk9iMRkj_GosLGaaIYmN6xmWZFO5XWxyAARB5pUjX5qr8fCGCVzNTHxoYsZ1A1XILzcTVCYqWei4ToqjlU09RI5X_RHPIgcCOTsZaB0RRVRuR7IefoDiGSNMAFC90nKzgW-7fSFfQuSOzEHbO4QnLyAAeSfnkfixPRJY8rvQot0F9Ftd7HvgE0EIiYIqze-mJ5vilHxqhy7JmVOeNZtRtsKVJ8tGZkGowW_zD5xFMTI2qWo6-Wm6ESD_kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jkj_w7Ux8qTVMruNjrbpDc8Q3HtY9ViiSrj6sFLDjhD7B9XtYCuJ2ZKskQxprD4MS8DKq4LDkpDQV48LDO_lFSRg2Vq2Rk42en_NmI41sXMiWpOXxOCTkyDfj9LDGoPNViHypo6VFqotEDMMLhVCEmBaPLZ6gBPNOwAfyMKE6rRHxcaV3m9e814azrerl-xt6K8KBlzsU7tdsTuIpxFQP2nvhoXF50ndYO0SAeAnMbjjZ-oiUJF-nBDxixAsDOAgSdjX2vpPQXq_VpwEFsHaqAQKusWvNAcH-JWVE_wzQrUpMEezYubbtKPP0miuXswqqWGxgz0vtvCFUVH0Tu2FyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
داور فینال و رده‌بندی جام جهانی ۲۰۲۶
🔹
با اعلام فیفا؛ اسلاوکو وینچیچ از کشور اسلوونی دیدار فینال جام جهانی ۲۰۲۶ که یکشنبه ۲۸ تیر ساعت ۲۲:۳۰ در استادیوم مت‌لایف نیوجرسی بین اسپانیا و آرژانتین برگزار می‌شود را قضاوت خواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/akhbarefori/671962" target="_blank">📅 03:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671961">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0322523c15.mp4?token=EBvzeIZ0K5a1llLbv3tqodLwTAP9d6luVD4K1_MxqkU7wAJf8JD-C7nKddFUnKkxvZ7-ZHwjPi6pjlIU_n7AqpWOt-uhHFqje35BZSduPIr-FebEUiRuDIOlisoyK3yYwpibOpuKmXvLKszTVi5AhaTMgmwxjiSm2fRa7tywDNHTVMLdx4DjDsx54Bzq8sHOAuljKLDKt1w0o2a8-0CVy3Rp35tRCntukfR2P548bZh_TDL_-lHN1C8292me2L0foqaQdfk-zUwgXurWMn6Lc4B6R-rpOVxrCGqdxFYHtA_wVwPbGJKQS41ibTHnZYQCXZ94bE8eEuzcX7BQ2x-tTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0322523c15.mp4?token=EBvzeIZ0K5a1llLbv3tqodLwTAP9d6luVD4K1_MxqkU7wAJf8JD-C7nKddFUnKkxvZ7-ZHwjPi6pjlIU_n7AqpWOt-uhHFqje35BZSduPIr-FebEUiRuDIOlisoyK3yYwpibOpuKmXvLKszTVi5AhaTMgmwxjiSm2fRa7tywDNHTVMLdx4DjDsx54Bzq8sHOAuljKLDKt1w0o2a8-0CVy3Rp35tRCntukfR2P548bZh_TDL_-lHN1C8292me2L0foqaQdfk-zUwgXurWMn6Lc4B6R-rpOVxrCGqdxFYHtA_wVwPbGJKQS41ibTHnZYQCXZ94bE8eEuzcX7BQ2x-tTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موج جدید حمله موشکی از ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/akhbarefori/671961" target="_blank">📅 03:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671960">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4360f9a1c.mp4?token=ZdMY5LilxMqoBprq4jUcR40ewMP74pFk72Om0BKsfDzN2UyNtm_L0a2H_-MxiF5avEpLqNq5hsN_Ffuhzp7JOWnZTwlO-f7gOSJvEue3iwlG19_HeBw6LwBNSC7p6I2My9DA1UGbxQ8tkYX6niywvsHIKRMxZCpYQQMLViHGIzfOOnnWLVZmEBBJPSKF17Ls4S5stRiFGZyPCOGeoialW-wo6Ah7MjAaC7df9uZh3HTSAGdjknD2pb273muKmnIWhoBJ1tR8sy4Eh2EpC_kfF_nG2qnB8zGBPHuWd-Ig9PbLC1za41AQbwDZufOC3XScEF6seRHFCs4Ity-be5JEzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4360f9a1c.mp4?token=ZdMY5LilxMqoBprq4jUcR40ewMP74pFk72Om0BKsfDzN2UyNtm_L0a2H_-MxiF5avEpLqNq5hsN_Ffuhzp7JOWnZTwlO-f7gOSJvEue3iwlG19_HeBw6LwBNSC7p6I2My9DA1UGbxQ8tkYX6niywvsHIKRMxZCpYQQMLViHGIzfOOnnWLVZmEBBJPSKF17Ls4S5stRiFGZyPCOGeoialW-wo6Ah7MjAaC7df9uZh3HTSAGdjknD2pb273muKmnIWhoBJ1tR8sy4Eh2EpC_kfF_nG2qnB8zGBPHuWd-Ig9PbLC1za41AQbwDZufOC3XScEF6seRHFCs4Ity-be5JEzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر ادعایی از فعالیت پدافند در بحرین
🔹
فیلمی که برخی از کاربران منتشر کرده‌اند فعال شدن پدافند هوایی بحرین را نشان می‌دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/akhbarefori/671960" target="_blank">📅 03:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671957">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
ادعای مقام آمریکایی درباره هدف از حمله به پل‌ها در ایران
🔹
یک مقام آمریکایی در گفت‌وگو با روزنامه وال‌استریت‌ژورنال گفته حمله به پل ها با هدف قطع تدارکات به بندرعباس انجام شده است که ایران از آن برای حمله به کشتی‌ها استفاده می کند.
🔹
بسیاری از کاربران در فضای مجازی اقدام آمریکا در حمله به زیرساخت‌های ایران را مصداق جنایت جنگی توصیف کرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/akhbarefori/671957" target="_blank">📅 03:02 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
