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
<img src="https://cdn4.telesco.pe/file/tKjgkr8ZBMbrIiHqtyU0w0aT8KExDs-KZueiyBkT5db9_dETSNOJO1lyyTMx0rqG5trob9VxbIfHQHNp_82x-HjZIIOfkLIDOp5VVovkZ0Tdz8Yv_w50K5yexnz9amaDQsBqhxCb7pTsgEzTho_sUQHyl1saUEzUYkMYuBcf-dDBIWPTHl8wsMy-Nedjgemk3ToxSGTgUD3rxTX5fHjE4ygUIzwKVHnnWAWe_N-GAV2GlZ7QT2K05fWAEsO8cYrG_tJVsgDkW-6q32Hsd97xdeZYtlz9_8o-TZl5y3uUirnYa8BoO1bUr-CWQYyX4qppfG_EC1yFjeCWFfkHoCPQxA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.02M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-07 12:18:18</div>
<hr>

<div class="tg-post" id="msg-149997">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3SVBrm86IVkdqcBQcsFwdHlF3RS68ZOMjRs77lp5pdc_MECtHNpxDYHeG8424JYxM3PwuKICIyibOjJX1eo98L27maV8Y6iviWvZMJbZkkbizzphusScvUFO7A_kLWRQlWzLiZIOeXx9Ml2NvhdMq2ziF6qPi--VTR1bQICstg5GOPxsSlatj-ePTjMEUvX0aoNO7x_glSSg-jVXWNb5jdHiNdSd-q3scZP66Hduat95K0AxAoIL5izYtHvsJT3j89kFdMR1wWkcK1GftTd7H7uNDYr0VYbOYaCnBAVDh6SJFgokJyIOPesumVc7etNGXGUm9FINYXwtskp-Ks-qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت دلار هم‌اکنون ۲۵۰هزار تومان!
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/alonews/149997" target="_blank">📅 12:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149996">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jC5n_bfU84d33WVFsmGmIsnA7K0gvxd-8GNtEDTMKTZvVoGGkfOPEPTDqg8CcviXKBXtQ0BZ5k-XADPPhMtAtXcJHYXLukvW0bJCjsu6hLuZ5sO7ikiEA7H4VE_QT8wDOta93kdkr-oPlhFhHqvbDZT4w_oEQR3EYBlBWr5HMldED-p144Yx7uWlquVvuaNPcYvbM6eXRkf7XeP5vPY62Z_OXXKRkQ32wZnLXjODNg_pgkJvXAj-v2st7Apfe4zTNf4pHJQ5ekzFfbWZghjud3AgYYYKaIQVgi3XrEqSTvDXm1f2YuanyOZQrwyx8tXiIDLCuJCxoeYO_vxXtDIFpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلاکارد دیده شده در شب نشینی امت سرخوش در مورد محکومیت رسایی
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/149996" target="_blank">📅 12:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149995">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">به نظرم همتی تو جواب گرونی دلار باید بگه رهبرمون هرچی بگه همونه</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/alonews/149995" target="_blank">📅 12:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149994">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ایران با اختلاف زیاد بی ارزش ترین پول دنیا رو داره
و نکته جالب اینه مردمش همون پول بی ارزش رو هم ندارن
🕺
🕺
🕺
🕺
🕺
🕺</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/149994" target="_blank">📅 12:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149993">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">به نظرتون یه سریا با چه متطقی میگن ما قدرت اول جهانیم؟ خبر ندارن بالا چخبره؟</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/149993" target="_blank">📅 12:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149992">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=o2xTXRkST0jyaKgcvAgaGVq_wuGLrrfJvPZXqZBNZwnHrWLygkVzn9HpryeAIohU2WvaH8RulONh54Ye0F_kVT-rY-9CoOR3icBIwu9M68ybIF7qitubaV4ll51Q3v7W8w_Bny1NxqTvZRx5NVhn0Bi_INZFrVfJMqpwqnJrO1kKKBL8Np2ihIhNH2lUlBJKrVN28ERsOtBwajeEP52IHjvUlYuRK2iCE5CkW4X04fzz2fz105neH7yQ_bSWVisPviPfHnHjiLmFH8pqqJd0ZY4dLlCgUnEUs9FQ8wzccnLft1iihRKN8ssiooagD6z0Zw4GM_Bv_YZG4RauMo26VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=o2xTXRkST0jyaKgcvAgaGVq_wuGLrrfJvPZXqZBNZwnHrWLygkVzn9HpryeAIohU2WvaH8RulONh54Ye0F_kVT-rY-9CoOR3icBIwu9M68ybIF7qitubaV4ll51Q3v7W8w_Bny1NxqTvZRx5NVhn0Bi_INZFrVfJMqpwqnJrO1kKKBL8Np2ihIhNH2lUlBJKrVN28ERsOtBwajeEP52IHjvUlYuRK2iCE5CkW4X04fzz2fz105neH7yQ_bSWVisPviPfHnHjiLmFH8pqqJd0ZY4dLlCgUnEUs9FQ8wzccnLft1iihRKN8ssiooagD6z0Zw4GM_Bv_YZG4RauMo26VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حقوق یک کارگر 65 دلار در ماه
‼️
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/149992" target="_blank">📅 12:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149991">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
سخنگوی دولت: با توجه به شرایطی که در آن قرار داریم، فعلاً تصمیمی برای افزایش حقوق نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/149991" target="_blank">📅 11:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149990">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/933cce337c.mp4?token=NLLjTaxCuXwjsKwDhkBewT1_4M_Qsv4IC2yLo-YuDtQKGybyrT4yGQjmVnp11o2Dgu6ThqUiht1U-XUksMgMwmE8IIOeCfSa8YtWsmHhP_7tJFs9H-ZTaN5_U4ykbaAJTwokESZy68A31rEMAk2VoVDb78ZrxwhfCv2Sl0hX3gdQ0rcmpHmgDmAyMGQU-srs25xzXNvdJS4kYoh9xbP4wXSGN-pUU8q1SP1Mp_2PyJz5TVuHqxx9JOrO1HxVoK3KHgZuCCCmw5f2ByLlGwsZPX3Ey62s4VxYt865Dj88JUzXPt4ugydAkOHLDMeT2wId1BArdGUcA1qR7hsmrEkL6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/933cce337c.mp4?token=NLLjTaxCuXwjsKwDhkBewT1_4M_Qsv4IC2yLo-YuDtQKGybyrT4yGQjmVnp11o2Dgu6ThqUiht1U-XUksMgMwmE8IIOeCfSa8YtWsmHhP_7tJFs9H-ZTaN5_U4ykbaAJTwokESZy68A31rEMAk2VoVDb78ZrxwhfCv2Sl0hX3gdQ0rcmpHmgDmAyMGQU-srs25xzXNvdJS4kYoh9xbP4wXSGN-pUU8q1SP1Mp_2PyJz5TVuHqxx9JOrO1HxVoK3KHgZuCCCmw5f2ByLlGwsZPX3Ey62s4VxYt865Dj88JUzXPt4ugydAkOHLDMeT2wId1BArdGUcA1qR7hsmrEkL6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: افزایش ۳۰۰ هزار تومانی کالابرگ، پول یک پفک هم نمی‌شود!
🔴
سخنگوی دولت: قطعا کالابرگ برای خرید پفک داده نمی‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/149990" target="_blank">📅 11:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149989">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66b62710f4.mp4?token=qtNFOrJvSSZ-snMpZbdwPV8Mde850bP09V0gxZtMKyMpmc7GF7XL413bHqT_mAVEHYzWcSn7IQB0JgGgip3LR4ZOvryxKzDj9SyKkX--tW4Ox_rYRm3jePm4ZYL8QvyStgpdbmIIU3R8CVnaMtmS9hHYlIW_fJkisz36bep4g0Oy2KAv5GBZKbO1KBr_BmERtGqz0JPVWS3EiP0Q_2dlbE-MpP5P9JwwKGAHPAZh7jtc8Ku63b_I-GBH3zqh2svl5Vm0Q1W4N6JRuRWGtA58RH1Llszi85qNqKSt6UFYkGldd6RuKy2YKx70Kyg-9Ucn7Z5eyEZkiGILd6q5_3WTOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66b62710f4.mp4?token=qtNFOrJvSSZ-snMpZbdwPV8Mde850bP09V0gxZtMKyMpmc7GF7XL413bHqT_mAVEHYzWcSn7IQB0JgGgip3LR4ZOvryxKzDj9SyKkX--tW4Ox_rYRm3jePm4ZYL8QvyStgpdbmIIU3R8CVnaMtmS9hHYlIW_fJkisz36bep4g0Oy2KAv5GBZKbO1KBr_BmERtGqz0JPVWS3EiP0Q_2dlbE-MpP5P9JwwKGAHPAZh7jtc8Ku63b_I-GBH3zqh2svl5Vm0Q1W4N6JRuRWGtA58RH1Llszi85qNqKSt6UFYkGldd6RuKy2YKx70Kyg-9Ucn7Z5eyEZkiGILd6q5_3WTOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دود غلیظ مشاهده‌شده در آسمان تهران ناشی از آتش‌سوزی در یک ساختمان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/149989" target="_blank">📅 11:28 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149988">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
سخنگوی دولت: احتمالا در استان‌های شمالی مشکل گاز داشته‌ باشيم
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/149988" target="_blank">📅 11:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149987">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
نتانیاهو: فرمانده تیپ شمال غزه در گردان‌های قسام ترور شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/149987" target="_blank">📅 11:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149986">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
رویترز: روز دوشنبه مقامات آمریکایی و ایرانی با میانجی‌گران دیدار کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/149986" target="_blank">📅 11:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149985">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUyR22xDCt_nRgufkCJViDRRqYQldCvX3xJMtueia57gUhHDeDiTyqnzz6FBWXFDzzX0XNwd8-9rMVeZzMej1zLtLupSfWG9Vb3dIxbnX5NrirdkiWzztG39nMt0D7CRVJ_B1mzpLlYNYCIrcAn5h9EvtePQDdqN7RqSYIOVKTT8HzspUR04zgiVrJnshTdG1wW9sRmgi72jEoftGoWFDqE4SoVll2P2fELsnhJjWWV0Mpi_9OPtSL4dg8CrAGPRGZGLD0sK5amBMxGCceIiKR5I8cP-hu8Pc2xXRCUMeVfEqU6wSY8xyFvlYwuyxOiaOZFY4Ps4IZTerdUG6l-T0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت بعضی مدل‌های لپ‌تاپ اپل در بازار به حدود یک میلیارد و ۲۰۰ میلیون تومان رسیده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/149985" target="_blank">📅 11:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149984">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/27c8682bb3.mp4?token=PdhsY_Fs_gT52VA7Gvna-_NJmpxfiloz284fJ7LpjrLY1J-SafdjAggThLB4l_mE845kVQk0mic-ceM4oB5moHQxoDahPOhUCct1_7J3MT0fr6eLIvQg-qn1IBP8Fu1VzCcDtJmIqtWw0GcNAt9C14WU6hlQYTlCN4c4hz5E0e1j0yorQ78ms6ki7vBuxQF0idvqZltaswKyRM4ner2it1-Y__Lw6qRBWMvL3wWMgXexgdebwJNcG4XgjujvJ6WKXLPNPEf4ylE4eFrc7yx1Fz0nPTMLRg0afG_VfbwwSuOaVxD4a6qiI5Y3KiQykm-6T0FtwKKXK7OqCqDmLVLAww" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/27c8682bb3.mp4?token=PdhsY_Fs_gT52VA7Gvna-_NJmpxfiloz284fJ7LpjrLY1J-SafdjAggThLB4l_mE845kVQk0mic-ceM4oB5moHQxoDahPOhUCct1_7J3MT0fr6eLIvQg-qn1IBP8Fu1VzCcDtJmIqtWw0GcNAt9C14WU6hlQYTlCN4c4hz5E0e1j0yorQ78ms6ki7vBuxQF0idvqZltaswKyRM4ner2it1-Y__Lw6qRBWMvL3wWMgXexgdebwJNcG4XgjujvJ6WKXLPNPEf4ylE4eFrc7yx1Fz0nPTMLRg0afG_VfbwwSuOaVxD4a6qiI5Y3KiQykm-6T0FtwKKXK7OqCqDmLVLAww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سنتکام ویدیویی از پرواز جنگنده‌های F/A-18E/F Super Hornet و F-35C Lightning II نیروی دریایی آمریکا از ناو هواپیمابر کلاس نیمیتز USS George Washington منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/149984" target="_blank">📅 10:52 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149983">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
عراقچی: انعطاف ایران در موضوع هسته‌ای را به شدت تکذیب می‌کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/149983" target="_blank">📅 10:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149982">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">شرکت Tether:  مبلغ 550 میلیون دلار USDT [معادل 134 تریلیون و 200 ملیارد تومن] مرتبط با ایران را فریز کرديم!  ما در سال 2026 به صورت کامل با نهادهای اجرای قانون و مقامات تحریمی آمریکا برای بلاک کردن پول‌های مرتبط با بانک مرکزی ایران و شبکه‌ های تحت تحریم همکاری…</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/149982" target="_blank">📅 10:42 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149981">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
شهردار کرج: من خودم جزء قشر کم درآمد جامعه هستم و حقوقم کلا ۶۰ تومنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/149981" target="_blank">📅 10:41 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149980">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
قالیباف: تلاش‌های امروز آمریکا برای تحمیل محاصره‌ی دریایی، بستن کریدورهای هوایی و اعمال فشار حداکثری بر شریان‌های تجاری کشور با برنامه ریزی و مدیریت جدی در حوزه‌های اقتصادی و پاسخ های نظامی مشابه سال ۶۰ شکست‌ خواهد خورد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/alonews/149980" target="_blank">📅 10:36 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149979">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
قالیباف: ترامپ اخیراً لفاظی‌هایی درباره‌ی تنگه هرمز و عبور کشتی ها از این تنگه مطرح کرد که تکرار ادعاهای پیشین است و حقیقت این مواضع واهی برای همه شناخته شده است.
🔴
هم آمریکایی‌ها و هم سایر کشورها بدانند: همان گونه که قبلا گفته بودیم در منطقه‌ای که ما نفت نفروشیم، کسی نفت نخواهد فروخت و اگر امنیت ما تامین نشود، هیچ زیرساختی ایمن نخواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/alonews/149979" target="_blank">📅 10:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149978">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
قالیباف به ترامپ: بچرخ تا بچرخیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/alonews/149978" target="_blank">📅 10:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149977">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHUBQyccQiePeLo4iQB2n9BlYd_DWM7FWViV-yklkQU9IBHdPvd8qngZc-r3GF1cNUbDlzSSbscsVDNvjUxShNuZwKWwytXw20ZqfHMCeCW0_1KAc7GrDpjLaLVsSkwjmWkQpRKBhPT8WbAf-cqoGDJgRyMPRi2TQjFxAGqeoy1-_4HNzfyFx8yMeBsGtTwnZvwNUr-vnHp1BdG2eMIDLa585wl86HVHGakupGWrX93ivJc2Q0_Kl87AbEHKXFKkd1XvJkuKUjiaUlLxZKxNG2kh6igf71dGnnHn65zsDd9lsZnOZ7Kydk7E7xABUV_pgTPrPHEJEX-dxJgHy1HA5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
غریب آبادی: امارات باید به واقعیت‌های تاریخی و حقوقی منطقه پایبند باشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/149977" target="_blank">📅 10:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149976">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل: دو اسکادران جنگنده آمریکایی در ساعات اخیر به پایگاه هوایی عوفدا در جنوب اسرائیل رسیدند و به نیروهای آمریکایی دیگری که از قبل در این منطقه حضور داشتند، پیوستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/149976" target="_blank">📅 10:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149975">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95ebd1c763.mp4?token=YVU8EiwQmNKRweh7NJJ8S0YwmeLsWHfZgBknJYPE_L7senHWUyP8Y-77XREcUJYEJH1gRYvqyC5BiS4mhktcVX1RYU4EQicgTdJOuPHDc9DUIgWvwXgawjrOcFCRgPn6dvP5u6fZArr7eYClO6uYTHx-z7M3kJ-tZTB9y9p38jK9Zotb9suI0YWQbEZoNvVTzB9Obp9fgnBxhaITL9aFoPXZNuagNGDK1eLJICwcaF7r66FIxv-5ahjOYKaEXh2LuJERlCcRnGtWPlQc_TV5KUM3b2WUO6hoQsLIAeMfV9Tibr2XRu7EAld9zAOuu4cujWRdVAHSUEI-Uv76Z5WuwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95ebd1c763.mp4?token=YVU8EiwQmNKRweh7NJJ8S0YwmeLsWHfZgBknJYPE_L7senHWUyP8Y-77XREcUJYEJH1gRYvqyC5BiS4mhktcVX1RYU4EQicgTdJOuPHDc9DUIgWvwXgawjrOcFCRgPn6dvP5u6fZArr7eYClO6uYTHx-z7M3kJ-tZTB9y9p38jK9Zotb9suI0YWQbEZoNvVTzB9Obp9fgnBxhaITL9aFoPXZNuagNGDK1eLJICwcaF7r66FIxv-5ahjOYKaEXh2LuJERlCcRnGtWPlQc_TV5KUM3b2WUO6hoQsLIAeMfV9Tibr2XRu7EAld9zAOuu4cujWRdVAHSUEI-Uv76Z5WuwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو، وزیر خارجه آمریکا:
«کافی است بگویم آنچه در بریتانیا طی آخر هفته رخ داد — و آنچه ممکن بود رخ دهد — بسیار جدی است.
🔴
این حادثه به دست یک عامل خارجی انجام شده است. فعلاً نمی‌خواهم درباره جزئیات بیشتر صحبت کنم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/149975" target="_blank">📅 10:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149974">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
مارکو روبیو، وزیر خارجه آمریکا:
«رئیس‌جمهور ترامپ به‌وضوح اعلام کرده است که مسئله گرینلند درباره فتح و تصرف نیست؛ بلکه موضوع امنیت ملی است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/149974" target="_blank">📅 10:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149973">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
رویترز:ایالات متحده تا فردا، چهارشنبه، از آخرین پایگاه‌های خود در عراق خارج می‌شود. این کشور جایی است که بیش از ۴۵۰۰ شهروند آمریکایی در طول بیش از دو دهه جنگ، جان خود را از دست دادند. ایران و متحدانش این خروج را به عنوان یک پیروزی جشن می‌گیرند و این امر به آنها آزادی عمل بیشتری می‌دهد، زیرا اکنون نفوذ عمیقی در این کشور دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/149973" target="_blank">📅 10:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149972">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/47df547a14.mp4?token=BdBUjHZIOjpq0XfniJCXeMa7VBF0EHcbR8TB3ccGbQw93o84OzcN20cdlYYC4Agbq6F7bzS6UpfJOBUVztrCagqpT-8_9BjipmxWDcftgLfajFUgzhtJqLYXK_nNX8C3WWDPwVTpYOK2mJPrakNe5fYOxBtPIWIStmaemECmRguyv_YtRIqBl4tw9ptxkmm9qwTclKQrAdvf1t70mtLyuVMV8mDcKGcCKMid0aRKbxwd0-B5Dv4GuIKiLLjDNo5QSufuAQbJT_bo5HhqmgV5vh854or0JmyevJZWns2oguVp7LgJ4F1FESiPTh-WEAT9BnukokZf9aQ5qravVvy75w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/47df547a14.mp4?token=BdBUjHZIOjpq0XfniJCXeMa7VBF0EHcbR8TB3ccGbQw93o84OzcN20cdlYYC4Agbq6F7bzS6UpfJOBUVztrCagqpT-8_9BjipmxWDcftgLfajFUgzhtJqLYXK_nNX8C3WWDPwVTpYOK2mJPrakNe5fYOxBtPIWIStmaemECmRguyv_YtRIqBl4tw9ptxkmm9qwTclKQrAdvf1t70mtLyuVMV8mDcKGcCKMid0aRKbxwd0-B5Dv4GuIKiLLjDNo5QSufuAQbJT_bo5HhqmgV5vh854or0JmyevJZWns2oguVp7LgJ4F1FESiPTh-WEAT9BnukokZf9aQ5qravVvy75w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو، وزیر خارجه آمریکا، درباره زمان برگزاری انتخابات در ونزوئلا: «در ونزوئلا دو اتفاق باید رخ دهد. نخست اینکه اقتصاد این کشور باید به روند بهبود خود ادامه دهد، زیرا مردم ونزوئلا سال‌ها متحمل رنج زیادی شده‌اند.
🔴
ما درباره ۲۵ تا ۳۰ سال فساد و سوءاستفاده مالی صحبت می‌کنیم. اما مسئله دیگری که باید رخ دهد و ما تمرکز زیادی روی آن داریم، گذار دموکراتیک است.
🔴
آنها باید در این کشور انتخابات آزاد و عادلانه برگزار کنند. ما به‌طور جدی با مجلس ملی ونزوئلا در سال ۲۰۱۵ همکاری می‌کنیم تا شرایط لازم برای برگزاری انتخابات آزاد و عادلانه را در سریع‌ترین زمان ممکن فراهم کنیم.
🔴
پس از آن، ونزوئلا می‌تواند وارد مسیر بهبود و رونقی شود که شایسته آن است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/149972" target="_blank">📅 09:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149971">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
فوری / فاکس‌نیوز: اسرائیل برای حمله دوباره به ایران در آماده‌باش است
🔴
فاکس‌نیوز: مقام‌های اسرائیلی علناً از آمادگی برای ازسرگیری حملات به ایران سخن گفته‌اند.
🔴
اسرائیل کاتز، وزیر جنگ اسرائیل، اعلام کرده ارتش در حالت آماده‌باش قرار دارد و برای ازسرگیری عملیات و انجام حمله مستقل به ایران آمادگی دارد.
🔴
با این حال، در همین گزارش آمده است که برخی منابع و تحلیلگران اسرائیلی تمایل کمتری به آغاز دوباره جنگ دارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/149971" target="_blank">📅 09:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149970">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cfb2f478bf.mp4?token=Ybcaq4RbUOuxH_QTPtFHT6Bkri364TjE3aiK8d63KVWnr9iqJ5I7v3Fco7s-hyLAjiO-yaBZkK_6-q3msHro97RI_k-ePJswhRJotDY3u1qP2cZuYeQHNwF9LM-OjqWCQNTre9eZ1NlsrwaKr7aA8Vk98n0eD5NBZe-qj9o_ugHnI2tmR1mhzrZy8F6farTSKxVEPFf4QCIoLTSEimtW1VlDKy_e1UdK_wHTw7HfoNvd7nZB4iCXL4Ett8tbKsetTQXZ6-wDnjIPr4kkY6Fhog-1GWfT8mZx5edUJ8AvIyYDMfTHyhYkNnVrY-k5yUqzij8EleurQuJYDlJUxjL3UZJAd4c5mOOQTqe2TmaKN4SzovtiUljTd8QVkHuaY7McLkFs0W1vIrqQ-ZNEJ9mMLzNPeTYyfGR0vmxQ1J-8d8KOcQL-6Dpt-brJP7Sj8BW82uDF4ISLnK7mlXXCy9GtU4lQuPqvnEtJs-K8_iqbgH48ndX4zGZb6ctH7DzghWlozDno64W1Cg99mldQhZbmnyc4UOwQTZs8tyK_Wd0niu5fdzXG5wDlQmzQH508cNx33KA900mRFjm1s6iwsE5VneNAJZNMnBBav9LFJgXbcJvfkpGjEKqMbqZ_S8bgqqEXLb6hg8mcS2sdRAC7gCgtdOFZ_BileSdSAYNW8hKloTo" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cfb2f478bf.mp4?token=Ybcaq4RbUOuxH_QTPtFHT6Bkri364TjE3aiK8d63KVWnr9iqJ5I7v3Fco7s-hyLAjiO-yaBZkK_6-q3msHro97RI_k-ePJswhRJotDY3u1qP2cZuYeQHNwF9LM-OjqWCQNTre9eZ1NlsrwaKr7aA8Vk98n0eD5NBZe-qj9o_ugHnI2tmR1mhzrZy8F6farTSKxVEPFf4QCIoLTSEimtW1VlDKy_e1UdK_wHTw7HfoNvd7nZB4iCXL4Ett8tbKsetTQXZ6-wDnjIPr4kkY6Fhog-1GWfT8mZx5edUJ8AvIyYDMfTHyhYkNnVrY-k5yUqzij8EleurQuJYDlJUxjL3UZJAd4c5mOOQTqe2TmaKN4SzovtiUljTd8QVkHuaY7McLkFs0W1vIrqQ-ZNEJ9mMLzNPeTYyfGR0vmxQ1J-8d8KOcQL-6Dpt-brJP7Sj8BW82uDF4ISLnK7mlXXCy9GtU4lQuPqvnEtJs-K8_iqbgH48ndX4zGZb6ctH7DzghWlozDno64W1Cg99mldQhZbmnyc4UOwQTZs8tyK_Wd0niu5fdzXG5wDlQmzQH508cNx33KA900mRFjm1s6iwsE5VneNAJZNMnBBav9LFJgXbcJvfkpGjEKqMbqZ_S8bgqqEXLb6hg8mcS2sdRAC7gCgtdOFZ_BileSdSAYNW8hKloTo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو، وزیر خارجه آمریکا، درباره تهدید بمب‌گذاری اخیر در نزدیکی پایگاه RAF Fairford: «آنچه در بریتانیا در آخر هفته رخ داد، آنچه نزدیک بود رخ دهد و آنچه می‌توانست رخ دهد، بسیار جدی است. این حادثه به‌وضوح دست یک عامل خارجی را در میان دارد.
🔴
فعلاً نمی‌خواهم درباره جزئیات بیشتر صحبت کنم. می‌خواهم از مقام‌های بریتانیا تشکر کنم که در این زمینه بسیار همکاری کرده‌اند و اوضاع را به‌خوبی مدیریت کرده‌اند.
🔴
می‌دانم خبر آزادی برخی از این افراد با قرار وثیقه، در حالی که تحقیقات درباره آنها ادامه دارد، باعث نگرانی بسیاری شده است.
🔴
ما در حال رایزنی با مقام‌های بریتانیا درباره تمام این مسائل هستیم. اما باید بگویم که آنها در برخورد با این حادثه بسیار جدی، همکاری و کمک قابل توجهی داشته‌اند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/149970" target="_blank">📅 09:46 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149969">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
رسانه‌های عبری: نشستی با محوریت ایران هم‌زمان با سفر نتانیاهو به امارات برگزار شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/149969" target="_blank">📅 09:42 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149968">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
انفجار کشتی در تنگه هرمز
‏
🔴
شرکت امنیت دریایی «امبری» اعلام کرد یک کشتی تجاری هنگام عبور از مسیر جنوبی تنگهٔ هرمز، در شمال «خصب» عمان هدف اصابت قرار گرفته و دچار آتش‌سوزی شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/149968" target="_blank">📅 09:38 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149967">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
عراقچی نیویورک رو ترک کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/149967" target="_blank">📅 09:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149966">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eFj0NOoyYYxcf3XMksJidEUSgNpEn8aPRkjGbwM-l9EPv5ZhRfbvahqQxqZGbUEkYtVzk6z_Ja5DQI9_hEmnHbSo2hTNZ--kufl0VBF2gYL_ipAHzwU0EinMakz5Io79BeoazQpv7YgW8ij_SGBwb-9fCGLkdP2su9Mfu1iEHhC5oXm_hoH8IDd38FoJONjvO1bnB9htFqrzrkpY02nH7rNIEb7ClZATIyUl47ywKL90kS8xP4Zc8M41jllQIAJI6MT2R7a5bc6jp7CCyRX6PXSgXORpBUy1mwsAISAcQmXAsfmTlPQi4mY3OioMdfjbwZ4ALNSXfXDDVl1p2gYw7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال‌استریت ژورنال: عربستان سعودی انتقال نفت خام از طریق خط لوله آسیب‌دیده شرق-غرب را از سر گرفته، اما با حجم کمتری نسبت به ظرفیت معمول.
🔴
در مقابل، ایران از زمان ازسرگیری محاصره تنگه هرمز توسط آمریکا در ماه ژوئیه، نتوانسته نفت خام خود را از طریق این تنگه منتقل کند.
🔴
ذخایر نفتی ایران که پیش از محاصره انباشته شده بود، ممکن است تا اواسط اکتبر به پایان برسد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/149966" target="_blank">📅 09:31 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149965">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
فوری و رسمی/ دلار 250 هزار تومان
‼️
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/149965" target="_blank">📅 09:26 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149964">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/blxbpUApnhacVw8-DiZ41Ph0Zm7NO4sO5C7_KA2xLHeI9TMsSta4Htu0LbkdBQ9g4L7s9vHY_a4nNNR3m5MXT4EGPNsApL9-_o0Pug60P_HiIJvkuIKpEZ8QHjPubGQo4VKWAM2OzVEIvzauHTujrKqa9iXx3bVvMNGwxAokbGZVzz8LBdqkjyH7T_vaJaiTHNj5WcZ_Fbdshg9njd55eKcbIxZsTMqmg3uqJoqPAuRsHEMABPrlZ-LYO4rZE6omf2KX73bH-St-wq9Ry-ykRbYJ_CUaYh_P1H_Vh0B-_bmIBAGZ_RnOqVzpj_gNJV4fxB32dAbJKzAiKu77ku3Wxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت خام برنت به 107 دلار برای هر بشکه افزایش یافت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/149964" target="_blank">📅 09:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149963">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
عراقچی:
امروز (دوشنبه) یکی از واسطه های قطری دیدار مجددی با ما داشت، بحث هایی را انجام دادیم . روی ایده هایی صحبت کرد و اینکه چگونه می شود برای تحقق شروط ایران راهگشایی کرد و چگونه این شروط را محقق کرد.
🔴
ایده هایی داشتند و بحثی را داشتیم که باز با طرف آمریکایی هم مطرح خواهند کرد و بعد پاسخ نهایی طرف آمریکایی پس از آن به ما منتقل می شود که امیدوارم تا فردا (سه شنبه) این کار انجام شود.
🔴
من چند ساعت دیگر به سمت تهران پرواز می کنم و پاسخ را قطری ها هر موقع که داشته باشند، می دانند که چگونه به دست ما برسانند.
🔴
این ارتباطات و پیام هایی که میانجیگران قطری و پاکستانی رد و بدل می کردند، همیشه بوده، الان با توجه به طرحی که ایران ارائه داد، شکل جدی تری به خودش گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/alonews/149963" target="_blank">📅 02:12 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149962">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03738737a2.mp4?token=k6o9ME9M_cpWPrwUSs84Z7fX1YuqfhWMuojgYC-In9xpgST2ZpY4tFI20blhk4QDmHtzyQFadSUDw0_XvK5sT2pWGwtai31gyNLaBcI6A3rBO-2iRAVaMKHoqEg-xSRT4ijMABg8fEBiJWYrlSAuMr8XB7rzV2FEjgeShS0ETCSpMWRJ1uB61Bo-lIs8gRwy5NpVI2kMwNKakwdfo03dKEEN2DhXwEIInSqaDGdEm73410Ub0GksOs_bRJ0I1KT9MFS9GHg-58u0N1GpwWcKq48PoUecFxXi82vYgHhI_VNLYN0k1VF-ZUi1GMAPWyzPJCnhcZGifSeWRFrchKoLRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03738737a2.mp4?token=k6o9ME9M_cpWPrwUSs84Z7fX1YuqfhWMuojgYC-In9xpgST2ZpY4tFI20blhk4QDmHtzyQFadSUDw0_XvK5sT2pWGwtai31gyNLaBcI6A3rBO-2iRAVaMKHoqEg-xSRT4ijMABg8fEBiJWYrlSAuMr8XB7rzV2FEjgeShS0ETCSpMWRJ1uB61Bo-lIs8gRwy5NpVI2kMwNKakwdfo03dKEEN2DhXwEIInSqaDGdEm73410Ub0GksOs_bRJ0I1KT9MFS9GHg-58u0N1GpwWcKq48PoUecFxXi82vYgHhI_VNLYN0k1VF-ZUi1GMAPWyzPJCnhcZGifSeWRFrchKoLRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بن سبطی از چهره‌های اسرائیلی: مجتبی خامنه‌ای زنده‌ست ولی کسی دستوراتش رو جدی نمیگیره. به گفته او اسرائیل منتظر درگیری بین رهبران ایران یا قیام مردمه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/alonews/149962" target="_blank">📅 01:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149961">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBsJYja_sY7Cnt-Lc962hRWgIydRcpyM93vqs-36BBzuN3MltFxZ4HZfEomlB_Klve7KidDEt2ZEBR5NOlAy_fS2ntXYdK6KvQrEzDdBuZirbXXDVR-R0zXuIQwbs-XhzVjlACAhGUIV7HBLcz83T_Uk5bcmsHID5elQPJFrx4clJ6gPMTb30SjrFPOy7-bFCsMv-Gd4jI7iHsDBP3z2VdkvJ1G6CAkOuPI7hzeRKVVNKI6za4WPzE798M2cSujmm8Fd6tHCYMztiT5d4pzspNkGJBcwtiioUERFU6EVBjwpUIYkAfYuo2CiQUul-dZ2bQLVkPatuCbUuzpADNxhdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:
آکسیوس به‌تازگی گزارشی منتشر کرده که در آن آمده است "ترامپ" به ایران پیشنهاد رفع تحریم‌ها و آزادسازی دارایی‌های مسدودشده را داده است. این خبر نادرست است. من هیچ پیشنهادی به آنها ندادم!
🔴
گزارش آکسیوس، مانند بسیاری از گزارش‌های دیگر، یک داستان ساختگی است که صرفاً با هدف ارضای "سندروم جنون ترامپ" آنها منتشر شده است. آنها باید فوراً این گزارش جعلی را بردارند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/alonews/149961" target="_blank">📅 01:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149960">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
شلیک موشک کروز از هرمزگان
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/alonews/149960" target="_blank">📅 00:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149959">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">در روستایی دورافتاده، کدخدایی بود که سال‌ها با حاکم شهر دشمنی شخصی داشت.
هر بار نام حاکم می‌آمد، کدخدا می‌گفت: «روزی او را سر جایش می‌نشانم.»
اما به مردم روستا می‌گفت: «روستای ما از همه دنیا قوی‌تر است و هیچ‌کس حریف ما نمی‌شود.»
کینه کدخدا روزبه‌روز بیشتر شد و سرانجام تصمیم گرفت با حاکم درگیر شود.
حاکم هم در پاسخ، راه‌های روستا را بست و نیروهایش را به آنجا فرستاد.
کدخدا که نمی‌خواست شکست خود را بپذیرد، مردم را وارد جنگی کرد که توان پیروزی در آن را نداشتند.
خانه‌ها و زمین‌ها یکی‌یکی از بین رفتند و روستایی که زمانی آباد بود، ویران شد.
مردم مات و حیران به خرابه‌های خانه‌هایشان نگاه می‌کردند.
کدخدا اما هنوز می‌گفت: «ما قوی‌ترین روستای دنیا هستیم!»
پیرمردی از میان جمعیت گفت: «اگر قوی بودیم، چرا خانه‌هایمان را از دست دادیم؟»
آن روز مردم فهمیدند گاهی کسی برای پنهان کردن یک کینه شخصی، غرور جمعی را سپر می‌کند.
و روستا بیش از آنکه از قدرت حاکم شکست خورده باشد، قربانی لجاجت کدخدای خود شده بود.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/alonews/149959" target="_blank">📅 00:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149958">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GvzIFGNhOOBhRl2xzrOpod3IURQaYyEZUaZ_R6oANLQYYrII1Wb1W1-P7fblSGhdiKLIlEGPbUoSzUnppFC2fBvuwE4nxxd0AKiGvxHEYtf0ewzAkAJvpsk7R5DlLANsur1wpOHkk3J1cplCE89LLbPCPsC0VUzPP2rggKxE9mIydlUhT_N7XfFA1Dm6kEdJHk4IYLdobd4vdKVDQQeWXiQ0xRbJ9rY-ID1wnLbZzaerCqzEEdE6J2M-ySkJ0k9BE62C2XK7Fn6H1znayoaaohPYBdoqZj7_cuqc2QWVCpB2Vy6GovvV8VI984bxWggptQxaloYCqfieU666e4cABA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاخ سفید:
«ظرف دو هفته چیزی از اقتصاد ایران باقی نخواهد ماند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/alonews/149958" target="_blank">📅 00:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149957">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">نکته اصلی اینجاست که دلار داخل و نفت خیلی این حرفارو تا اینجا جدی نگرفتن  هروقت دیدید اینا شروع به تغییر محسوس کردن بدونید ممکنه جدی باشه  نفت ۱۰۵ دلار  تتر ۲۴۴  @shahab_gold_trading</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/149957" target="_blank">📅 00:23 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149956">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
مهدی محمدی؛ مشاور قالیباف:
روحانی و اصلاح طلبا برای آمریکا پیغام فرستادن که اگه یه لایه دیگه از رهبران و فرماندهان رو ترور کنی؛ احتمالا زمینه تغییرات در ایران به وجود بیاد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/alonews/149956" target="_blank">📅 00:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149955">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d63f3c9c5.mp4?token=QRIQXX5SQRyhU35FrqKQgKFsfEnj5YLNkPg7vopOOL9rTR_0BDOcVXBpfHCnDH_BRtHYJT5sJVNeNwN5FvVQtsxaapHKM04HOcLFA4waHRccTcljRGcF1w_yJQSTRxB884Jlu4531EsIfie8NlWZZsD5obqfzyFi0zf6iS2MBO7bHRhOOhZ7B60q6cbD_fCHAiHWw5ZLwFpuDgzFc8Hc3onJfHHvw55p7lX_ffTlpEIjxv7FW88_37jhCxeVrJTpydVFpLfgXLkuKIK5E61igxqUsHjV6PPV3CdpLKkgyCzkTF56yHhTlrSLN7cNiTsGKEB6Q1iUl1TiuKhj_A_NUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d63f3c9c5.mp4?token=QRIQXX5SQRyhU35FrqKQgKFsfEnj5YLNkPg7vopOOL9rTR_0BDOcVXBpfHCnDH_BRtHYJT5sJVNeNwN5FvVQtsxaapHKM04HOcLFA4waHRccTcljRGcF1w_yJQSTRxB884Jlu4531EsIfie8NlWZZsD5obqfzyFi0zf6iS2MBO7bHRhOOhZ7B60q6cbD_fCHAiHWw5ZLwFpuDgzFc8Hc3onJfHHvw55p7lX_ffTlpEIjxv7FW88_37jhCxeVrJTpydVFpLfgXLkuKIK5E61igxqUsHjV6PPV3CdpLKkgyCzkTF56yHhTlrSLN7cNiTsGKEB6Q1iUl1TiuKhj_A_NUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار خطاب به ترامپ:
آیا تیم شما امروز با ایران صحبت کرده است؟
🔴
ترامپ:
بله.
🔴
خبرنگار:
با میانجی‌ها؟
🔴
ترامپ:
بله.
🔴
خبرنگار:
چیز دیگری هست که بتوانید با ما در میان بگذارید؟
🔴
ترامپ:
ما پیروز خواهیم شد‌.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/alonews/149955" target="_blank">📅 00:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149954">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yl4gyeYCvhyZPylAGebKGMiM3JbgPJ93ZBfclnhv7oFwrIRqgeZGv1KZR2SqkMMS88W0DQZiC1CkweWnYDxJpyNZdPNbNS-O-M-kW0AzrXQ1E3M0XRJD7YCHuYOXa8DKQ9mK4jF2OUaQ0QV9F_a0W7uJBeRHAHW3rfiD6qxCDBtn6zUpKMLzv1WcWrm1q07HgPFqpk2zE2RJwF4uFXxSdQZWFSRI8Ey3hSny4uVVBU9iduSdtaOuhyNa9EMyJ6Z_wwjzfPQ0Pc1bVuCDWU6AZ3-_k9VquRVlcmljsEyg8zoBZhXhXJWq6wAuy4sGfqFE5efl0C5DrWEcWqUkIv9IRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
پاوربانک بخر، ایرپاد هدیه بگیر!
🔋
پاوربانک ۲۳,۰۰۰ میلی‌آمپر Xiaomi M10
🔥
فقط 2.199 م تومان
✅
پرداخت حضوری در درب منزل
✅
ارسال به سراسر کشور (شهر و روستا)
✅
گارانتی تعویض و برگشت
لینک خرید اینجاست
👇
https://yeklinks.ir/powerjzl?utm_source=Telegram&utm_medium=lead&utm_campaign&utm_term=63575912425450218</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/alonews/149954" target="_blank">📅 00:06 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149953">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16b6cf54c5.mp4?token=j9EiBMcjoxfYiprjn07PmN8_4Xjhkh4WP2plY_YqNWV0MPnHZs-Q1Rl4cqI4BGnHwWD--Qo4GTOtIi7djDA9UBP3vU016iwCV5tWUIB5_ek5vXcZYWHGCmeSBYRAfItgzkKfwVGrj6rrb00Lm5xHZ84kzFvPKeabYZEY_BnlBYvngQRk1eatQyso4l53-p47wU_AEKWwToe4IdolcsHgERl4k5JL3suM9CnygIgQjNYPVFt1fyPNTJ1rwloNMKm0F5lD0iV2jaN0_aF08KC7PAuEHkiGZHD2LOe3yQZVDwsskmJnQ66ZrMyBDg-IEsPSzj5KUkG6FFWKSelP3-sxew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16b6cf54c5.mp4?token=j9EiBMcjoxfYiprjn07PmN8_4Xjhkh4WP2plY_YqNWV0MPnHZs-Q1Rl4cqI4BGnHwWD--Qo4GTOtIi7djDA9UBP3vU016iwCV5tWUIB5_ek5vXcZYWHGCmeSBYRAfItgzkKfwVGrj6rrb00Lm5xHZ84kzFvPKeabYZEY_BnlBYvngQRk1eatQyso4l53-p47wU_AEKWwToe4IdolcsHgERl4k5JL3suM9CnygIgQjNYPVFt1fyPNTJ1rwloNMKm0F5lD0iV2jaN0_aF08KC7PAuEHkiGZHD2LOe3yQZVDwsskmJnQ66ZrMyBDg-IEsPSzj5KUkG6FFWKSelP3-sxew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر دولت امارات در مجمع عمومی سازمان ملل: امارات خواستار پیگیری اشغال جزایر سه‌گانه تنب بزرگ، تنب کوچک و ابوموسی توسط ایران است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/alonews/149953" target="_blank">📅 00:01 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149952">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
بیرانوند: همه گیر دادن به سربازی رفتن من، خب اگه با سربازی رفتن من دلار میشه ۱۰ هزار تومن، همین فردا میرم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/alonews/149952" target="_blank">📅 23:59 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149951">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
نایب‌رئیس مجلس ، نیکزاد: مجلس طرح سه فوریتی خروج از NPT را بررسی می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/149951" target="_blank">📅 23:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149950">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCJglbzb_qoB386w9uPjC9Gyt9YVCoIjKCn_N4bRIMgMj-dWTWkQpQ3exQlzzevESLwcEbOR_scGWOuLZ16beHbC8vrUod-q5o8qgU88ocVAW8aa9GD0eq0dHYmI_W5-kzAj8BUGG9kQ6oIQUY9AD6_vfBKEOiWQVVY-GzW6oxSpKa0d8TBNH2E0KtxNvJqiNIrqC_slBdLRCaZq5l7uWkjRUqMj2WV1MD0T5DA1bFqWaqAmZ4nrNyxyVYLHoWMJZR8K8EthHDnjTKJzpT6XZjmvkt9VKKkQD-sQyzqU5-PdSf6PebNtW3Acuo87xY0akk242REtLnX-W233GGTscQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرواز همزمان ۵ سوخت‌رسان آمریکایی در نزدیکی تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/149950" target="_blank">📅 23:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149949">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
نورالدین الدغیر،  خبرنگار الجزیره: اطلاعات حاکی از آن است که پیشنهاد جدید ایران شامل هیچ تعهد هسته‌ای نیست و موضوع هسته‌ای نیز تنها پس از اجرای مرحله نخست مطرح خواهد شد.
🔴
اختلاف کنونی بیش از آنکه بر سر اصل مذاکره باشد، بر سر این موضوع است که کدام طرف باید ابتدا از اهرم‌های فشار خود صرف‌نظر کند
🔴
میانجی‌ها در حال بررسی فرمولی هستند که امکان اجرای تعهدات را بدون آنکه یکی از طرف‌ها به‌صورت یک‌جانبه از اهرم‌های فشار خود دست بکشد، فراهم کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/alonews/149949" target="_blank">📅 23:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149948">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
فوری / گروه «کتائب حزب‌الله» عراق اعلام کرد که اگر محاصره هوایی پروازهای ایران تا اول اکتبر لغو نشود، گذرگاه‌های مرزی هر کشوری را که در این محاصره مشارکت داشته باشد مسدود خواهد کرد و تمامی «هواپیماهای متخاصم» را در حریم هوایی عراق هدف قرار داده و سرنگون خواهد ساخت.
🔴
این بیانیه همچنین «علی الزیدی»، نخست‌وزیر عراق، را تهدید کرده و تصریح می‌کند که اگر دولت در راستای منافع مردم عمل نکند، با توسل به هر ابزاری سرنگون خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/alonews/149948" target="_blank">📅 23:36 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149947">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
فوووری /  دو انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/149947" target="_blank">📅 23:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149946">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
اسرائیل هیوم» گزارش کرده که سفر دیروز نتانیاهو به امارات ۶ ساعت طول کشیده و در این سفر، رئیس موساد و رئیس شورای امنیت داخلی اسرائیل او را همراهی کرده‌اند.
🔴
شبکه ۱۴ اسرائیل نیز گزارش داده نمایندگانی از چند کشور عربی، از جمله عربستان سعودی در دیدار اخیر نخست‌وزیر اسرائیل و رئیس امارات در ابوظبی حضور داشتند.
🔴
المانیتور نیز مدعی شده در سفر محرمانه نتانیاهو به امارات، موضوع ایران «بر دستور کار دیدار» با شیخ محمد غلبه داشته
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/149946" target="_blank">📅 23:13 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149945">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
سیاری معاون ارتش: کل مردم ما به عنوان سرباز آماده دفاع از کشورن
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/alonews/149945" target="_blank">📅 23:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149944">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
ثابتی: حق حمید نیست زندان بره
✅
@AloNews</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/alonews/149944" target="_blank">📅 23:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149943">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNKC24E6NUaBT08EciDewplPmdwarMaiLt-9RY4wzYLI8UWAsO6TIbXKnJSy5P8rY_DULCoeNi0q7qa0fdl3VFy_4SwpGfyGfL9za3KA0fbXxpRjRsyARdIiAvs5mWaZuvBLdVns8TlET063Q1EDn98oUEks1iOaU1vtCCizjCYE9yWQF-wDMYH3j2cK1Z27YtCvlTqxqTT1cK-yrYZQ93OuTzcjMEnLCcw_jqipFD-ScvhmRx8d-HanikdAIFBKdXqEWgCv9OAKMz2G99wCcOKCfu8mT52tsZsV-yk06RSNpGp_Fz4sSJjMWMK3-MGq8NruCRvTnrepHGPkPmG0dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: برخی منابع عبری-عربی مدعی موافقت ایران با توقف غنی‌سازی شدند؛ ایران پیش از جنگ ۴۰ روزه هم با توقف غنی‌سازی موافقت کرده بود
🔴
آمریکا پیش از توقفِ غنی سازی به دنبال ۴۰۰ کیلو اورانیوم ۶۰٪ است، پس از آن تعلیقِ بلندمدت غنی‌سازی حتی در حوزه تحقیقاتیِ موثر را می‌خواهد و بعد از آنهم بعید است که تحریمی بردارد، پولی آزاد کند و جنگ را مجددا پس از انتخابات، از سَر نگیرد!
🔴
آمریکایی‌ها دیگر «تنگه هرمز» را امتیازِ ویژه‌ای که به تنهایی واجدِ شرایطِ مذاکره‌کردن باشد، نمی‌بینند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/alonews/149943" target="_blank">📅 23:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149942">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18688252a5.mp4?token=jXgaEjvXG5jOjmlGVkSxSdq6dbuibSRLMKSi7EaNxfnNZvUC4lmhaUAxE3t5Lizopw7skhNGsFRj2Th3bBt2zx6UhNbC_G8sVdbZ95KDVRZPV2mZhfQELbGTn2O_5ZGyiRKnX7JT1E9Lt670vj0_vRzIWj1gXwuk3vt9h2qpPAbwGv8R9IzFSjL3J-wmbx5kiSl6WOKFGRL34pnVTTy8ZjzY0czPA2le-7Ai7eKm2E2JNuuzZDTpczUFqphxsR5OZQr23rsOC07sMCqiZFkovuSNA40YgBcI8pzxe0eVpE0ZBMhi1iUA9XdZjp_6gGK3rfWNdNXgnhL5hJ_Gb4MSHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18688252a5.mp4?token=jXgaEjvXG5jOjmlGVkSxSdq6dbuibSRLMKSi7EaNxfnNZvUC4lmhaUAxE3t5Lizopw7skhNGsFRj2Th3bBt2zx6UhNbC_G8sVdbZ95KDVRZPV2mZhfQELbGTn2O_5ZGyiRKnX7JT1E9Lt670vj0_vRzIWj1gXwuk3vt9h2qpPAbwGv8R9IzFSjL3J-wmbx5kiSl6WOKFGRL34pnVTTy8ZjzY0czPA2le-7Ai7eKm2E2JNuuzZDTpczUFqphxsR5OZQr23rsOC07sMCqiZFkovuSNA40YgBcI8pzxe0eVpE0ZBMhi1iUA9XdZjp_6gGK3rfWNdNXgnhL5hJ_Gb4MSHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امروز مردم ریخته بودن جلوی در میلی گلد که ودشکست شده و پول ملت رو خورده
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/alonews/149942" target="_blank">📅 22:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149941">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">خب مثل اینکه ترامپ هم تأیید کرده که تیمش از طریق واسطه‌ها با ایران حرف زده   @shahab_gold_trading</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/149941" target="_blank">📅 22:52 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149940">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
ترامپ: ۹۵ درصد تجارت کانادا با آمریکاست
🔴
ترامپ: ۹۵ درصد تجارتی که آنها انجام می‌دهند، با ایالات متحده و با ماست. سهم تجارت ما با آنها در مقایسه با این رقم، بخش بسیار کوچکی است و اصلاً رقم بزرگی نیست.
🔴
ما به آنها تجهیزات نظامی می‌دهیم. به آنها یخ‌شکن هم می‌دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/149940" target="_blank">📅 22:51 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149939">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
ترامپ درباره ایران: اگر می‌خواهید هرج‌ومرج را ببینید، بگذارید شهری را با سلاح هسته‌ای نابود کنند. من فقط درباره اسرائیل و بخش‌های وسیعی از خاورمیانه صحبت نمی‌کنم. بگذارید با سلاح هسته‌ای به ما حمله کنند؛ خطاب به همه آن آدم‌های احمقی که فکر می‌کنند این مسئله اشکالی ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/149939" target="_blank">📅 22:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149938">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
ترامپ درباره ایران: من وارد جنگ شدم تا جلوی چیزی را بگیرم که می‌توانست یکی از بدترین اتفاقاتی باشد که تا به حال برای جهان، و برای ما، رخ داده است.
🔴
در حال حاضر، اسرائیل نابود می‌شد
🔴
اسرائیل وجود نخواهد داشت، منطقه خاورمیانه نیز از بین می‌رفت، و سپس موشک‌ها و بمب‌ها به سمت ما و اروپا شلیک می‌شدند.
🔴
و من این [جنگ] را متوقف کردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/149938" target="_blank">📅 22:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149937">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
ترامپ: تحت ریاست جمهوری بایدن، شما برای بنزین بسیار بیشتر از آنچه که اکنون پرداخت می‌کنید، هزینه می‌کردید
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/149937" target="_blank">📅 22:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149936">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bda947fd66.mp4?token=pUZTd8MpxrPi7k0NHWhdUet_ZZ-4iTvKRI3jFu8tZWm41xLWLL0ERV-1ZHxHMd74elZRZt1EWQkXiq2euReRIwYG-gPpXwKRH6wigE8z3N_7L6s_wx5bO2al8pxVDPv75asnWhdYPbG0aXKtmEvswVFmftX7TGcTwxgcrJzZMdJ_clnN5h-IgTyeprZygYX8ktr8ZCsn8AZ8ULRPVkaKNSxSh0vUZAsY6Wx4Xj_QbxACEcvw5QbfcVUNJCMOfXKi_CNr6AIlPQxefk1rV-9FONInzPjufvGTp4YYHc6BAQ6Vu7tummgm52Rpw1bgkaFTiHZy2DD27a-64j1Q1DwcTSfFa26Zr5-atbof8VrTiGLIdQDEGbpUC74JN8EBxgBidtX5ullLPN4_Omq0EoF_iV2_o65kst6b00gwFIPskYVvh0PjTtaesAuFs-C5fNKwQeY10_zFjwWCDKej6HHmXymcDZPgkadirhbWFLp2eIb0j8AteJhnhjPEkUM4pt_joAcrNC0LLaHMvfUczz4deTUS0i6tvboPv8O9wVsCmlopcH35c7OXzZ0kRFw-iK3PmXNGW5kzOJqVprj2tk_7jfqjLkQmKHEwFEo6q0DuR2DQeKV_9_ia2W6b5PQaKE1pyeYQqsflQAdQExjDZGktwIH9_YbHQk_vSfxX-tzKlNM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bda947fd66.mp4?token=pUZTd8MpxrPi7k0NHWhdUet_ZZ-4iTvKRI3jFu8tZWm41xLWLL0ERV-1ZHxHMd74elZRZt1EWQkXiq2euReRIwYG-gPpXwKRH6wigE8z3N_7L6s_wx5bO2al8pxVDPv75asnWhdYPbG0aXKtmEvswVFmftX7TGcTwxgcrJzZMdJ_clnN5h-IgTyeprZygYX8ktr8ZCsn8AZ8ULRPVkaKNSxSh0vUZAsY6Wx4Xj_QbxACEcvw5QbfcVUNJCMOfXKi_CNr6AIlPQxefk1rV-9FONInzPjufvGTp4YYHc6BAQ6Vu7tummgm52Rpw1bgkaFTiHZy2DD27a-64j1Q1DwcTSfFa26Zr5-atbof8VrTiGLIdQDEGbpUC74JN8EBxgBidtX5ullLPN4_Omq0EoF_iV2_o65kst6b00gwFIPskYVvh0PjTtaesAuFs-C5fNKwQeY10_zFjwWCDKej6HHmXymcDZPgkadirhbWFLp2eIb0j8AteJhnhjPEkUM4pt_joAcrNC0LLaHMvfUczz4deTUS0i6tvboPv8O9wVsCmlopcH35c7OXzZ0kRFw-iK3PmXNGW5kzOJqVprj2tk_7jfqjLkQmKHEwFEo6q0DuR2DQeKV_9_ia2W6b5PQaKE1pyeYQqsflQAdQExjDZGktwIH9_YbHQk_vSfxX-tzKlNM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: درباره فروش تجهیزات نظامی آمریکا به چین با شی صحبت نکردیم
🔴
خبرنگار: سفیر آمریکا در چین، آقای پردو، گفته شما به شی پیشنهاد دادید که آمریکا تجهیزات نظامی به چین بفروشد. این درست است؟
🔴
ترامپ: من اصلاً چنین چیزی نشنیده‌ام. احتمالاً آنها دوست دارند این تجهیزات را بخرند، چون ما تجهیزات بهتری تولید می‌کنیم، اما ما درباره چنین موضوعی صحبت نکردیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/149936" target="_blank">📅 22:45 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149935">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور آمریکا، درباره ایران: به محض اینکه آن جنگ به پایان برسد، تورم به طور کامل از بین خواهد رفت. کاملاً.
🔴
هیچ‌کس درباره این موضوع صحبت نمی‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/149935" target="_blank">📅 22:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149934">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ad829cf81.mp4?token=PZTabsf8CJO45Jxv5IZFn-Knc1IxfM9AdGBrUF1x0XuHl2S1ICgHV97sPTj6cWxDeDoZxpolkW5RLlbqqhGm9-xdgwkvabHnfo2MfWwVfp5zC9BrWwWJX-VvPMPimFT8_H7xSyZZexrulq9J3OUpudiEXiiwjo_MC3xXiUkyjlcg82DcuodZFER9hgVHsZHGKdNO7cz_D0M5oNKVVhVkAupIH-1eGnvYXkDfes-YjIB-_iZrczJNFQXebOd-Jt9pU8JiTwkEKvDaj1gBNDRTnfb2dkwauqzXLXAaSso-RnIhJR2ZfXVG2DzbFuuTkWh25tunT45O0HcySdN_jO6zUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ad829cf81.mp4?token=PZTabsf8CJO45Jxv5IZFn-Knc1IxfM9AdGBrUF1x0XuHl2S1ICgHV97sPTj6cWxDeDoZxpolkW5RLlbqqhGm9-xdgwkvabHnfo2MfWwVfp5zC9BrWwWJX-VvPMPimFT8_H7xSyZZexrulq9J3OUpudiEXiiwjo_MC3xXiUkyjlcg82DcuodZFER9hgVHsZHGKdNO7cz_D0M5oNKVVhVkAupIH-1eGnvYXkDfes-YjIB-_iZrczJNFQXebOd-Jt9pU8JiTwkEKvDaj1gBNDRTnfb2dkwauqzXLXAaSso-RnIhJR2ZfXVG2DzbFuuTkWh25tunT45O0HcySdN_jO6zUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره کانادا:
به نظر من، در طول سه یا چهار هفته آینده، کانادا با ما تماس خواهد گرفت و خواهد گفت: "ما تمام تعرفه‌ها را لغو خواهیم کرد."
🔴
ما در همه چیز پیروز خواهیم شد. حتی دریاچه انتاریو اکنون "دریاچه آمریکا" نامیده می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/149934" target="_blank">📅 22:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149933">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebe3cbb91c.mp4?token=C3aJcaWwiB8TQKi1zWdG9zRjcmOeNYy4kTYYVD47W7AD6nIi8vmxynoempZnMaN8-ZkfoU0bVr87mdBJaY4dHVQx2nxjmzHDmKISM9W6EXjM64Hb7l-Qt3eb8Vk6QoOF0aXZT18nkWqOHJ3aKIcJP2gqmSR2kpNLGPDPHaXFCen4HAfKMTph5AXWHNaQBEWtb5QVe36WIiaTtVy4VEqxREV2HLsFhzSaLSHlsLvt0ynb8i3zOkaLuIWBtdcHVjTZD3BpWoWrRPGt0g9VbZrpwzv5acjzjp6JUHsu5LNGfNLjm7HYDe-PFbsg8IOlz5Z5unCwM-U5CtL99tEBC7K7Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebe3cbb91c.mp4?token=C3aJcaWwiB8TQKi1zWdG9zRjcmOeNYy4kTYYVD47W7AD6nIi8vmxynoempZnMaN8-ZkfoU0bVr87mdBJaY4dHVQx2nxjmzHDmKISM9W6EXjM64Hb7l-Qt3eb8Vk6QoOF0aXZT18nkWqOHJ3aKIcJP2gqmSR2kpNLGPDPHaXFCen4HAfKMTph5AXWHNaQBEWtb5QVe36WIiaTtVy4VEqxREV2HLsFhzSaLSHlsLvt0ynb8i3zOkaLuIWBtdcHVjTZD3BpWoWrRPGt0g9VbZrpwzv5acjzjp6JUHsu5LNGfNLjm7HYDe-PFbsg8IOlz5Z5unCwM-U5CtL99tEBC7K7Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:
اگر می‌خواهید آشوب و فاجعه ببینید، اجازه دهید آن‌ها یک شهر را با سلاح هسته‌ای نابود کنند.
🔴
من فقط درباره اسرائیل و بخش‌های بزرگی از خاورمیانه صحبت نمی‌کنم
🔴
اجازه دهید آن‌ها ما را با سلاح هسته‌ای مورد حمله قرار دهند، برای همه آن افراد احمق که فکر می‌کنند این کار درست است.
🔴
آن‌ها دیوانه هستند. هیچ شکی در این مورد وجود ندارد. آن‌ها آدم‌های بسیار دیوانه‌ای هستند. من همیشه به آن‌ها می‌گویم. من می‌گویم: "شما دیوانه هستید، مرد."
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/149933" target="_blank">📅 22:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149932">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2335881783.mp4?token=BKQQqQC9CK2hprO0FBaaJUGEEa3QS1t_zeg2SGVHTygPc3qoc2ZcliG0q2llg7SgZx9TpidQ-RChaU7-09lcBTxHA7LHNcwd3odfdPZfDNn4JNlDIvTLQH3bXtUrqo1cxcgUV-e-RNLAo2XG-tnZvPAL-RLsABlYj4TV7xWbDvbjGHYZbPd4TRnIcf7dKaTN2P_0jkR6BvapFYk_6Odb4UJHtJG7C9m-avN78_6dhOBvjzAmbBriLRCyWNFD_bsXY6obICK1KjhP5kr56F6q-bJ2Hf-LuLZ6CKCUDujGStjYpKW-Q5E7FIRXdDaSo_nr_sVYx9-Um7Qv7M_JshfxAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2335881783.mp4?token=BKQQqQC9CK2hprO0FBaaJUGEEa3QS1t_zeg2SGVHTygPc3qoc2ZcliG0q2llg7SgZx9TpidQ-RChaU7-09lcBTxHA7LHNcwd3odfdPZfDNn4JNlDIvTLQH3bXtUrqo1cxcgUV-e-RNLAo2XG-tnZvPAL-RLsABlYj4TV7xWbDvbjGHYZbPd4TRnIcf7dKaTN2P_0jkR6BvapFYk_6Odb4UJHtJG7C9m-avN78_6dhOBvjzAmbBriLRCyWNFD_bsXY6obICK1KjhP5kr56F6q-bJ2Hf-LuLZ6CKCUDujGStjYpKW-Q5E7FIRXdDaSo_nr_sVYx9-Um7Qv7M_JshfxAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره دیدار با شی جینپینگ:
به نظر من، اگر بخواهیم این دیدار را از 0 تا 10 امتیازدهی کنیم، من به آن 12 از 10 می‌دهم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/149932" target="_blank">📅 22:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149931">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
خبرنگار: آیا رویداد مربوط به پایگاه نیروی هوایی سلطنتی بریتانیا در فیرفورد  ارتباطی با ایران دارد؟
🔴
ترامپ: «ممکن است داشته باشد، اما باید بگویم که از اینکه آنها این موضوع را علنی کردند، تعجب کردم. من این کار را نمی‌کردم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/149931" target="_blank">📅 22:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149930">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
ترامپ درباره ایران: «ما خیلی زود در آن جنگ پیروز خواهیم شد. آن جنگ تمام خواهد شد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/alonews/149930" target="_blank">📅 22:24 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149929">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171bfa07ec.mp4?token=K5lKBxKzIlVr_FZEPMHQvKEtdWTZNX84R2iWhkLAY9kIBLHlLnwgNK90mqnRUvkNSJ_IU5_jC7aOjIgmX9Z6qh7KJllUxns87IL8ejhXfXhLTqq64Nza5gbdFXVqulUB7XPMM1hIby4bIKY1cvMDFMTvyU3j0_00pBd0Q3iA8qmvRhH4JYk4kVi_ETsPZrYDr5QAQDXe1G78BE-7S_d5JACHJSAZCiqNVvxt3GVGoSF_FzqX_YyKS0KrSwt0ZRb9C7gzdHyrAL3SJp2eM7XCeNJ97t3mRj4eT05I6m-HHzcm0A4UrDfrZvyDDfAgpcxqn4SHSvSuuS1W6b-vLaDlcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171bfa07ec.mp4?token=K5lKBxKzIlVr_FZEPMHQvKEtdWTZNX84R2iWhkLAY9kIBLHlLnwgNK90mqnRUvkNSJ_IU5_jC7aOjIgmX9Z6qh7KJllUxns87IL8ejhXfXhLTqq64Nza5gbdFXVqulUB7XPMM1hIby4bIKY1cvMDFMTvyU3j0_00pBd0Q3iA8qmvRhH4JYk4kVi_ETsPZrYDr5QAQDXe1G78BE-7S_d5JACHJSAZCiqNVvxt3GVGoSF_FzqX_YyKS0KrSwt0ZRb9C7gzdHyrAL3SJp2eM7XCeNJ97t3mRj4eT05I6m-HHzcm0A4UrDfrZvyDDfAgpcxqn4SHSvSuuS1W6b-vLaDlcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: حال شما در ونزوئلا چگونه است؟
🔴
وزیر ورایت: ما هر روز پیشرفت داریم.
🔴
ترامپ: هیچ‌وقت چنین اتفاقی نیفتاده بود. این یک اتفاق فوق‌العاده است که در حال رخ دادن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/149929" target="_blank">📅 22:13 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149928">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
فووووووووووری/نیوزنیشن: یک توافق ابتدایی میان ایران و آمریکا حاصل شده  @shahab_gold_trading</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/149928" target="_blank">📅 22:11 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149927">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c729dfe11a.mp4?token=g7dg9GmAeO0-yfIPenPcrM2M0BySqvEyFXAQNAXf2KUkMdcgul0oL8eC362xgRDk5AgMlhdVW4tGuxlgeDpdf9gSqN3-nG6VUAJvXoE6ZuvO9FOoukHUYE7G3hOVBPgde5IdSn-vEbXV6Y33qH-wDFBsGvwsB42ZtTY30Lqmq1b5lFKdHK58Xxtm-f6Aeww-rWkpnEL5vYnlRurYPceWs6z9ETTdx1tJslMnn93HdX2dh3262G_ZKENFvI55D7BkUJbJko7NwVdlwDHeUZRW4E3rkKVLOdJyHnko4wZ0oMYChBLspN158L5QZcDfMHKv9BqJCj3EyRjTSQTJZK44fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c729dfe11a.mp4?token=g7dg9GmAeO0-yfIPenPcrM2M0BySqvEyFXAQNAXf2KUkMdcgul0oL8eC362xgRDk5AgMlhdVW4tGuxlgeDpdf9gSqN3-nG6VUAJvXoE6ZuvO9FOoukHUYE7G3hOVBPgde5IdSn-vEbXV6Y33qH-wDFBsGvwsB42ZtTY30Lqmq1b5lFKdHK58Xxtm-f6Aeww-rWkpnEL5vYnlRurYPceWs6z9ETTdx1tJslMnn93HdX2dh3262G_ZKENFvI55D7BkUJbJko7NwVdlwDHeUZRW4E3rkKVLOdJyHnko4wZ0oMYChBLspN158L5QZcDfMHKv9BqJCj3EyRjTSQTJZK44fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : اگر جمهوری‌خواهان اکثریت را در مجلس نمایندگان و سنا به دست آورند، به هر فرد بزرگسال پنج هزار دلار کمک خواهیم کرد. و ما می‌توانیم این کار را انجام دهیم.
🔴
دموکرات‌ها نمی‌توانند این کار را انجام دهند، زیرا دموکرات‌ها هیچ درآمدی ندارند و آن‌ها ما را به سمت رکود اقتصادی پیش خواهند برد. آن‌ها هیچ پولی نخواهند داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/alonews/149927" target="_blank">📅 22:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149926">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbaf1d565a.mp4?token=cNdEaNdIYNba_U9OthdoPZsFnAP2kFGa8JZ3ADgTcI12GCKQaXgmmS1kmGVlDouJYi85ViKfGC2tDg1iA_edwraDgYlubvcdllAVOvftkVg7kBPCVXZHblzWMyeIZdnkjLv5ofetHaU2Yrmqj7XBW-ut_C79zoTZnuJNXR8-cggba7kxNS5c3dSgfCvnet6z1bYbXpJZxf0-_nfp-2dp5dUp6_pGnf1w1kqXrAkSB9h1hflS11S68Qn8yrwQyjvS8eeaQCYT1VTM6v_mzoDKWXJRkD8ep6X9HFFpWesMblvUiSjBwInQ92goNI6cXq9tPsVWMGx5lhsU-gyeFdjriw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbaf1d565a.mp4?token=cNdEaNdIYNba_U9OthdoPZsFnAP2kFGa8JZ3ADgTcI12GCKQaXgmmS1kmGVlDouJYi85ViKfGC2tDg1iA_edwraDgYlubvcdllAVOvftkVg7kBPCVXZHblzWMyeIZdnkjLv5ofetHaU2Yrmqj7XBW-ut_C79zoTZnuJNXR8-cggba7kxNS5c3dSgfCvnet6z1bYbXpJZxf0-_nfp-2dp5dUp6_pGnf1w1kqXrAkSB9h1hflS11S68Qn8yrwQyjvS8eeaQCYT1VTM6v_mzoDKWXJRkD8ep6X9HFFpWesMblvUiSjBwInQ92goNI6cXq9tPsVWMGx5lhsU-gyeFdjriw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: امروز، با خوشحالی اعلام می‌کنیم که شرکت "مسابی متالیکس" بزرگترین کارخانه فولادسازی در تاریخ آمریکا را در ایالت بزرگ آیووا خواهد ساخت.
🔴
این کارخانه، بزرگترین کارخانه در جهان است، اما به طور قطع، بزرگترین کارخانه در آمریکا محسوب می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/149926" target="_blank">📅 22:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149925">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d586ff7959.mp4?token=emGrM8MN1nSuU5ie9oj2dB2v4b1dNkfIPxByGJ-ti1MlhrUjCncEfemvoYk5tXY-VJfmLsgO39r7OHShgZGiq4dUhHqYzp20Vj1tCe0vE-TGalCAZGnJ7cOZoS08vR0E0jrTRHJsNZtVoqsAhJ9xLzZVtWHbmbF6nY0uI0vsPOVobodEZmro3l-BIDguggc5sqXGy8p5D2tQryzFpGRB4tq6CpwJuT3IMshDLAJSeRIL9VrT_1USNCYCbekcxnCQAOMa8Zv_hGtqFfj4916CmK9R23FG9hdzctq89U1Pmb8lM2b0qegIN6vGxZcbANyo9xqjl3fS798BMsNAeF2nDpxbfPS_RZ5rMpSFNIw5EpoSL6q1BSmHAcgyq7ae1aA_nsLTZSxgjrnvnXYoIc6EPtaO-7mcSrexTul-VGVMrydu1ThIX8g_342jDosMfwBQSuzV2XrRCeYyVzItpzJguqF5YupLKHw7xgKMbqtHhL0YU9zvutVUMCcVyvN1jNG_KX6b5gDs8162WYThp8B6X-vvzuZWy-3NN0EtpiASCNv4ChPMuZHxVAlNudSrFS4y_kzFfDY5zQya6PMi6vhEq85JAPIdhFuZE6b_ObF6TcPsSt5Ty_8IJo19BmlwgXez6GCZcdro1gIxbaFcP0p25oGHOhfFwXzt9bfSYMRGomE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d586ff7959.mp4?token=emGrM8MN1nSuU5ie9oj2dB2v4b1dNkfIPxByGJ-ti1MlhrUjCncEfemvoYk5tXY-VJfmLsgO39r7OHShgZGiq4dUhHqYzp20Vj1tCe0vE-TGalCAZGnJ7cOZoS08vR0E0jrTRHJsNZtVoqsAhJ9xLzZVtWHbmbF6nY0uI0vsPOVobodEZmro3l-BIDguggc5sqXGy8p5D2tQryzFpGRB4tq6CpwJuT3IMshDLAJSeRIL9VrT_1USNCYCbekcxnCQAOMa8Zv_hGtqFfj4916CmK9R23FG9hdzctq89U1Pmb8lM2b0qegIN6vGxZcbANyo9xqjl3fS798BMsNAeF2nDpxbfPS_RZ5rMpSFNIw5EpoSL6q1BSmHAcgyq7ae1aA_nsLTZSxgjrnvnXYoIc6EPtaO-7mcSrexTul-VGVMrydu1ThIX8g_342jDosMfwBQSuzV2XrRCeYyVzItpzJguqF5YupLKHw7xgKMbqtHhL0YU9zvutVUMCcVyvN1jNG_KX6b5gDs8162WYThp8B6X-vvzuZWy-3NN0EtpiASCNv4ChPMuZHxVAlNudSrFS4y_kzFfDY5zQya6PMi6vhEq85JAPIdhFuZE6b_ObF6TcPsSt5Ty_8IJo19BmlwgXez6GCZcdro1gIxbaFcP0p25oGHOhfFwXzt9bfSYMRGomE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وِس استریتینگ.، وزیر دفاع بریتانیا، درباره جمهوري اسلامي ایران:
🔴
فکر می‌کنم حمایت از اقدامات دفاعی انجام شده توسط ایالات متحده درست بود.
🔴
بی‌شک درست است که بگوییم جنگ در ایران جنگی نبود که ما آن را انتخاب کرده باشیم. اما از سوی دیگر، هیچ شک و تردیدی هم وجود ندارد که ایران یک نیروی شرور است که بریتانیا، منافع ما و متحدان ما را تهدید می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/alonews/149925" target="_blank">📅 22:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149924">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/149924" target="_blank">📅 21:59 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149923">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚀
کانفیگ v2ray نامحدود | چند کاربره
🦋
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
📍
نامحدود _ PLUS
⚡
:
🇩🇪
🇫🇷
🇮🇹
🇸🇪
🇦🇹
🇦🇿
🇵🇱
🇹🇷
🇺🇦
🇦🇱
🇦🇩
🇫🇮
🇳🇱
🇺🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇲
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
برای اولین بار در ایران
👑
کانفیگ ها بدون تبلیغات هستن
🚫
تمامی لوکیشن ها قابل استفاده در جمنای
✅
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
…</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/149923" target="_blank">📅 21:59 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149922">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
خبرگزاری عراق: ازسرگیری پروازهای شرکت هواپیمایی عراق به ایران از طریق فرودگاه نجف، با تلاش‌های مستقیم نخست‌وزیر انجام شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/149922" target="_blank">📅 21:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149921">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
امارات متحده عربی سفر نخست وزیر اسرائیل به این کشور را تکذیب کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/149921" target="_blank">📅 21:53 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149920">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsL5erk3FQh9CRmVKyZHYl6k2Pe8gWflmlNXtwxaQHchu_JFsgjo4bDT7YreOAGyM7TzkISSOeb8gK3ENtzBHUkBG9xTtqS-AxInS1J8TXlpGCR8WQFrMiAcBKxCRHZq8yfG6VDR9N6HzSO9OGQXwif5KTySVPYfL09PIFoxUbBGQQIpakjG9duLapLS5dNzxvVdoiXblxrYwgjMA75I3923JKuwD5ri9F3o3HrONLIsDQ3g8pn8yjAsB3rerpGfyROXvYetxZVioZQu7t9REx4H0h4NXEr1H2nKy4z4D9mIRlFyBx0YnfDZP6nASHQsMeMXi9MAEJRA1pA6lcTHNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار آکسیوس :به گمانم ایالات متحده می‌خواهد شاهد آن باشد که ایران بازرسان آژانس بین‌المللی انرژی اتمی را دوباره دعوت کند؛ کاری که در جریان مذاکرات سوئیس متعهد به انجام آن شده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/149920" target="_blank">📅 21:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149919">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DK8UAHSriz2gksvi1c1xeHglLPV0iS4TUu5ciYM17IP5NfOGtLbkEAR0Y0qKoTaLwxp58MnxaWJUBo4QzH8RL2fCn2e8OFGOUn1pI_eIdMfyXxeASr5-QC3xeS_Ei2Mv0_YuLgDJptFhN_0ltBDhotCXmXDyey8qKy_o3vNIAZzWiLpO8by33Ssv60EceqRUq-6DmyFNFHuhZ_2uNuVyayVAEsU86Q7DrRxTrmYxo6PgGLG1RZuK6P2-KqmrAjYy_yK-KXrr-TwdaRVM6RmubTfCn7iyBsjU86ARM85ps-VjthcLxjXP4AKSvLzfJKpIH7KrUypnvVl5ul7VUjAJCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جایگاه هند و چین در تولید کالاها
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/149919" target="_blank">📅 21:45 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149918">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXZ3QFcgMqwSQBviVCpJBkVGQUd3vMbuDQq6YcJODCRP8TblKm6qu7Af_dugwCMZw0kJw-GUHaOXxhB0cNZwSEnFlPe2IJFMa7SSO7FMFqFX8QZ84jJVdx_OMWTLwVBJl7Miq9LDQAlZ5HfxZHgUf0MAoRGcNNm3ov8A70cI38cgIzEbRS8RL299CoUFP4xjYRtcc1eh9__xIKRlymbCjOn4vRZzU3qSQel3N-q2FLCkSo0cInmyuIRq02RrXhP8gxfrJUdqv550mOTIiW0Jq8kWtidIRegi67F_kDIeXdLp5r9KYyTYeCJN4NHZdc_jf56e8WJYnYiGwU2-Agl4KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سقوط آزاد درآمد دولت قطر از نفت و گاز
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/149918" target="_blank">📅 21:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149917">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSHL0zXjrClIiX_epUBptjAxvOqQneRyby__8ssnMmB2tAC_oEcr63lX9EDJGt6f5mcRIsZVkpTdZXAnXBAL5C37I1huo6gNv_oZz7-nhTEMPpuVdBp9kylVB11wVLbJMYH_ktk-lPx4ftHrVNBe-YyaHkrzUT92Tu-p6bYweDJsF3zsM94g9nSi-rG0uqv4D6IZV6UDA1rgK6llEBWiV8s1YMqY9bWnZd2prSGkqn-Gmcz5lJs9PfVUOHzWNxK6m4Wq9bQUWEpN09lfJ5XVlH1Tm6qR39IlLIv8Jm6tgIbKGBJEAoqyOL0wUImqco4q5v7G3WWm4OsjJakjjr7Mng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسکات بسنت: عملیات "منزوی اقتصادی" باعث شده است که ارزش ریال به پایین‌ترین حد خود در تاریخ برسد.
🔴
ما به تضعیف توانایی حکومت ایران در تأمین مالی تروریسم و توسعه سلاح هسته‌ای ادامه خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/149917" target="_blank">📅 21:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149916">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیلی: نهادهای امنیتی اسرائیل در حال آماده‌سازی برای احتمال از سرگیری درگیری‌ها با ایران هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/alonews/149916" target="_blank">📅 21:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149915">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF): لحظاتی پیش، یک موشک رهگیر به سمت یک هدف هوایی مشکوک که در منطقه‌ای که سربازان IDF در جنوب لبنان در حال عملیات هستند شناسایی شده بود، شلیک شد.
🔴
جزئیات در حال بررسی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/alonews/149915" target="_blank">📅 21:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149914">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
نایا : شرکت هواپیمایی عراق، پروازهای خود به فرودگاه‌های ایران را از طریق فرودگاه بین‌المللی نجف از سر گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/149914" target="_blank">📅 21:18 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149913">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل: نتانیاهو در سفر به امارات نه فقط با مقامات این کشور بلکه با نمایندگانی از سایر کشورهای عربی دیدار کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/alonews/149913" target="_blank">📅 21:13 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149912">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
فوری / فعالیت‌های پدافند هوایی در منطقه کریات شمونا، در شمال اسرائیل و در امتداد مرز اسرائیل و لبنان، مشاهده شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/alonews/149912" target="_blank">📅 21:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149911">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
مطابق گزارش خبرنگار شبکه الحدث در پاکستان، به گفته منابع، ایران با توقف فعالیت‌های غنی‌سازی موافقت کرده است، در ازای آن، تحریم‌های ایالات متحده علیه ایران کاهش خواهد یافت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/alonews/149911" target="_blank">📅 20:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149910">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
یک مقام آمریکایی در گفتگو با سی‌ان‌ان:
مذاکرات مثبت و سازنده‌ای را از طریق میانجی‌ها با ایران دنبال می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/alonews/149910" target="_blank">📅 20:47 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149909">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
عضو هیئت رئیسه مجلس: ما قدرت چهارم جهان نیستیم، قدرت اول جهانیم و تنگه هرمز هم ناموسمونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/alonews/149909" target="_blank">📅 20:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149908">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
حوثی‌ها (انصارالله) اعلام کردند که عربستان سعودی در ۲۴ ساعت گذشته، ۳۸ حمله هوایی و موشکی انجام داده است. این حملات با استفاده از هواپیماهای F-15 و تایفون از پایگاه‌های هوایی خمیس مشیت و طائف، و همچنین موشک‌هایی که از مناطق نجران و جیزان شلیک شده‌اند، صورت گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/149908" target="_blank">📅 20:37 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149907">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byYKWPeyvx2kmniBo55oaABaNHsNHMn99RTiN7CGTnB5JIr5fVSoiaLezVrurXhRBhAM-35BG3MXY2tv_jwgCTgz5NwgAfasTqFTLcDCFQv4RuOiPRTWiv6omV7wEHGdDd-YNVCNXJuUhPfct3pJjIGO2AdOhLnxCAx7GIV-_SOY3JhHNGQaQl7j3bRgF6FmfmhMLoEboa_MQP8THzqsqF_oW-l16_BKW-91gyPnQhz9dVGvu5AegOTEyitAeBQ4VEMzGRN_NZe3T38nrSloublPuhA56VkP5s_b5-mz-Sq2Atv5ALtqTKJl_YlPgcF3tHVAErwPCUgQhefvG5D1DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۴درصد کاهش فوری قیمت نفت در کمتر از  ۳۰ دقیقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/alonews/149907" target="_blank">📅 20:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149906">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOfQmDCp-6jYGPjij5jwSD-sS-WyZ33yjQQxfM1pghQ36uFpmZKy03TussPMzB4mct1wXt40Sp0FQT0mXNkYV8eXZROQLQ8jrHevy5a9-q7e2XnFBOinYrRN6MALj0Z5xs-M_Tt0s-aBZtAEqlC9AVngR6Y1CYcbYeO0g96AyuTxOGs7cUwqmbWNTihormeNOX2h3IJdenXMYQKwtOuUVIxvCuLnM1DL9fikRNwX75fl8OMnWu_owNKFqpmgrq-QYsJiUoVZaDy2VZ_G-YAlNr5uwok-bvfFFSYL2zA6m_7qHGHB4Bi-w-3ixy-wXPq6f6GS8yqEXAd0YE7HlkK1_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ابراهیم رضایی عضو کمیسیون امنیت ملی مجلس: مستعمره‌های آمریکا در منطقه که این روزها برای شعله‌ورتر شدن جنگ فشار می‌آورند، مراقب باشند که در جنگ بعدی کاخ‌هایشان هم هدف مشروع است.
🔴
‌خبر داریم که برای جنگ مجدد فشار می‌آورند و هزینه‌هایش را متقبل شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/alonews/149906" target="_blank">📅 20:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149905">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
یک فروند هواپیما بوئینگ متعلق به شرکت هوایی کاسپین، به دلیل بدهی سه میلیون یورویی در فرودگاه استانبول توقیف شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/149905" target="_blank">📅 20:17 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149904">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
فوری / مقام آمریکایی به باراک راوید: ترامپ آماده کاهش تحریم‌ها و آزادسازی منابع مسدودشده ایران است
🔴
یک مقام آمریکایی به باراک راوید گفت: «دونالد ترامپ آماده است در ازای پیشرفت ملموس در موضوع هسته‌ای، تحریم‌های ایران را کاهش دهد و منابع مالی مسدودشده این کشور را آزاد کند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/alonews/149904" target="_blank">📅 20:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149901">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
مقام آمریکایی به آکسیوس:
بدون پرداختن به مسئله هسته‌ای ایران هیچگونه توافقی در کار نخواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/149901" target="_blank">📅 19:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149900">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
العربیه به نقل از منابع آگاه: امروز مذاکرات غیرمستقیم میان آمریکا و ایران با میانجی‌گری قطر و پاکستان برگزار می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/alonews/149900" target="_blank">📅 19:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149899">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
فوری / برخی منابع عربی مدعی شلیک موشک‌ از خاک ایران شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/149899" target="_blank">📅 19:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149898">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I93Rp2QWkvUHepqIAq04yjjgkAtNwn1lwvfF3QkIlH06ePV0UPOFRS_3Wx0rTvVGbQ5TUYyWXdqj26g3FXWqzNTmcBt0M217phzkHji-yNrq5sQK14Bu233uOx9MDzIKkLSgDWHOS-UaSXwplwQ7STgZZzdzA7CbL8JrnaIlF4P0yZaH0XJYWGZwLa_BfPISiDtCHigN9D6ORK60q0aK5K-vnMttchLCYA2UEbyS1SzzrnEcVu0jRwYkUzMJm02wt85Otqw4cS0ECafh7qzBWZ3mZVoueG4Gp0bbI_VWKJZHoL5yDE8Tm3tQj2wnHV8uAqq9N-vx2xn17obM3QH-vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت جدید خاویر بلاس، ستون نویس مشهور بلومبرگ: صادرات نفت خام از عربستان سعودی، عراق، کویت، امارات متحده عربی، بحرین و قطر (از طریق تمام مسیرها) با هزینه‌های هنگفت و با کمک نیروی دریایی ایالات متحده، به حدود ۸۰ درصد سطح پیش از جنگ رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/149898" target="_blank">📅 19:37 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149897">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">میانجی‌ها امروز یا فردا مذاکرات جداگانه‌ای با آمریکا و ایران تو نیویورک برگزار می‌کنن ولی بعید میدونم اتفاق خاصی بیافته  @shahab_gold_trading</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/149897" target="_blank">📅 19:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149896">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
رویترز: در چارچوب دیدار شی و ترامپ، چین و آمریکا بر سر کاهش تعرفه ۶۰ میلیارد دلاری کالا توافق کردند
🔴
چین و آمریکا توافق کرده‌اند تعرفه‌های اعمال‌شده بر کالاهای وارداتی به ارزش ۶۰ میلیارد دلار از یکدیگر را کاهش دهند؛ اقدامی که طیف گسترده‌ای از محصولات کشاورزی آمریکا و کالاهای مصرفی و خانگی چین را دربرمی‌گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/149896" target="_blank">📅 19:24 · 06 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
