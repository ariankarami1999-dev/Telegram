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
<img src="https://cdn4.telesco.pe/file/Rp27jzV72hWWizsDsMax-MGd50NM72riWgCjv3Hue88xCXPacDhnMCocxbdHieFDN80f6--psAetYdvpm6r4APhJxAvjM030zflx3Vt4sT0ahLVcilkTmjccv7Q4o7rkUKNd46XKK_atiVKdIoq4gVoV3W07sZOhSWlBTG3uv-AUCWN1IJU0mRtLuuCvMw5kMA-euGZycbivY9TxzTulx0xQF0XSzGK5sU7icydYKTguJ75oBNCHV4ex0rFVs6ILiomZiXokepHVC1L8HTLCLRs9kkTjkVrlDD4ogW7q-D3WJUjiZ1ZOIBjg45pobii0Es-FX2PKH1qIq8juSjcEog.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.7K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 14:20:03</div>
<hr>

<div class="tg-post" id="msg-6156">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ca0d3dd94.mp4?token=NKK1Xe3lAdnamy8oGjt7Af4xYh-a2Oj9jDiXQbMSoM_4wMA6jhTxCqJhzeuDqdUq55-rQ4xAbb3-rNIGr6dzxvCIdxNuigjF30xv1d6h1oAp5lyAKefSHb2HHplAkbP7cA6IHpr6TEQdR7NNREw13KpjGWiJkdUDsqMmZ80mso7Y0n4SW6NNSTC0K3beVJWAkFIG_QyPJkhMn1VJiT0Nc_6YSM7cDTfchhFSPXyZYX4UtGtlj5r0_KnsSAOPRAR4rh_PaZU5CN9o-K0Ys1y-L_oR9YzOTKgBnjVZB4X5zlaHHAIHAuxd57L2ntv53JtdaGlCEpyS-HPG-V_FYrKpvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ca0d3dd94.mp4?token=NKK1Xe3lAdnamy8oGjt7Af4xYh-a2Oj9jDiXQbMSoM_4wMA6jhTxCqJhzeuDqdUq55-rQ4xAbb3-rNIGr6dzxvCIdxNuigjF30xv1d6h1oAp5lyAKefSHb2HHplAkbP7cA6IHpr6TEQdR7NNREw13KpjGWiJkdUDsqMmZ80mso7Y0n4SW6NNSTC0K3beVJWAkFIG_QyPJkhMn1VJiT0Nc_6YSM7cDTfchhFSPXyZYX4UtGtlj5r0_KnsSAOPRAR4rh_PaZU5CN9o-K0Ys1y-L_oR9YzOTKgBnjVZB4X5zlaHHAIHAuxd57L2ntv53JtdaGlCEpyS-HPG-V_FYrKpvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله شب گذشته ج‌ا به اربیل در عراق
علی‌الزیدی نخست‌وزیر عراق با صدور بیانیه‌ای،
این حمله را محکوم کرد.
در این بیانیه آمده که «به آژانس‌های امنیتی
مربوطه در هماهنگی با نیروهای امنیتی منطقه دستور داده شده که همۀ تدابیر لازم برای ممانعت از تکرار حملاتی از این دست، و نیز مقابله با هرکسی که به‌دنبال خدشه‌وارد کردن به امنیت جامعۀ سرفراز عراق باشد را اتخاذ کنند».</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/farahmand_alipour/6156" target="_blank">📅 14:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6155">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Riol4wSvSsZ_4jpoqTaWzKjCqDe0J-Bo4G3BciOG0tl2HwJP8UlzFohqSIxvOsR4jmyClWMfr3COK--VLWcJR3i_BRrb87uRAytQJhO4MPZmo1GzqFRZ_6aBsEekQb6G5WKNAyLO55uvx7kGmR6SYykyzgMN4NajDSEyQJJjjyDuAt_GWDJjkzwNwnl2jNsOua9zohT03Cd5gMz8x8bw1joVO8MINIGeUNQ0uCqR_qzdeVqS17v8X4viO8_jBOifggeyUnkWjUOuGsht2B8L-YwNihxbhWzT1pfUnKFUoEkagIWMlo6EAqieaeVkWaU-KG0GI4g2PWTbX-NULLsANA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وراجی نکنید  بگذارید بجنگند که صلح بیارن :)  مثل صلحی که ۴۷ ساله در لبنان  ‌ و غزه آوردن!  انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farahmand_alipour/6155" target="_blank">📅 12:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6154">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">وراجی نکنید
بگذارید بجنگند که صلح بیارن :)
مثل صلحی که ۴۷ ساله در لبنان
‌ و غزه آوردن!
انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farahmand_alipour/6154" target="_blank">📅 11:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6152">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=B6l6tcnpcRSRD8hFnPU3zmK-6zSqcTSGbXMVzoJDsVEDoiYqb2-DEAj1PT8uHradLneRzGbBn65HVXtDnT2oiTFMrJ8ZerKtHvWGKj6OKspECzgt3AgpBCPTHlTCjINp-ZtU_SbYEkm0DefKAxp0-gPqprzHNcgw8xfjcO5nm-v9WObvs5qzu_Q4yWaoXClQZa3M4ug881VcdgdmHljFUFDIYMIi1zQrEnp9E9NM-IsX7U_N-GvkiZ3dmvkliTGE271GicLpkHOQ6jklsCoSfA8JAs-RKrRX32ZhQLAyDzOUzFyNucQs4WWVTHyfnOlwkxQtDIBbQDPjVTZybcw4lCAEej1yRzAS0zy7zy8CCBQhNWNXIY9bk5R3gqVpzktsUJ7hSlv1ccjv_-oM7E0bH6Pj9vQhQ4aHlOQHFHYWo815qx7DsefdKX3glTCn8jy-2ex8d4vHe0o6l0V8F9H6Bt-6zeQ-LJuvWD-y3rWYJ7U8-8351Gml-Krr6ntPimOXN4dVE7u6dSwiMIEvOEZbFfxMYy3Q-xQ6Q8Ef3ZtnSTh-P6dFZXSW7-EHkp5qJZ0ezxm8Z3LraNPQ5IN-IwKfNu_f4oVKeHPaxn5dhf1mnVxM9O3Yn3lPMfhC_-jaI2ygs3pidr5DPzWWldp3llYtnbA2QPhvNVeytqSPHGYKjcU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=B6l6tcnpcRSRD8hFnPU3zmK-6zSqcTSGbXMVzoJDsVEDoiYqb2-DEAj1PT8uHradLneRzGbBn65HVXtDnT2oiTFMrJ8ZerKtHvWGKj6OKspECzgt3AgpBCPTHlTCjINp-ZtU_SbYEkm0DefKAxp0-gPqprzHNcgw8xfjcO5nm-v9WObvs5qzu_Q4yWaoXClQZa3M4ug881VcdgdmHljFUFDIYMIi1zQrEnp9E9NM-IsX7U_N-GvkiZ3dmvkliTGE271GicLpkHOQ6jklsCoSfA8JAs-RKrRX32ZhQLAyDzOUzFyNucQs4WWVTHyfnOlwkxQtDIBbQDPjVTZybcw4lCAEej1yRzAS0zy7zy8CCBQhNWNXIY9bk5R3gqVpzktsUJ7hSlv1ccjv_-oM7E0bH6Pj9vQhQ4aHlOQHFHYWo815qx7DsefdKX3glTCn8jy-2ex8d4vHe0o6l0V8F9H6Bt-6zeQ-LJuvWD-y3rWYJ7U8-8351Gml-Krr6ntPimOXN4dVE7u6dSwiMIEvOEZbFfxMYy3Q-xQ6Q8Ef3ZtnSTh-P6dFZXSW7-EHkp5qJZ0ezxm8Z3LraNPQ5IN-IwKfNu_f4oVKeHPaxn5dhf1mnVxM9O3Yn3lPMfhC_-jaI2ygs3pidr5DPzWWldp3llYtnbA2QPhvNVeytqSPHGYKjcU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها اگر نوحه میخونن و مداحی و رجز خوانی و.. برای کودکان غزه و لبنان و میناب و….. از تاسف از دست رفتن زندگی نیست! میخوان در این جنگ بی‌‌‌‌پایانی که با جهان دارند،  از جمله و در صدر این‌جنگها،  با خود مردم ایران جنگ دارند، سربازگیری کنند! تا نیروهاشون بزرگ‌تر…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farahmand_alipour/6152" target="_blank">📅 11:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6151">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">تمدن اسلامی! تا زمانی که توی مدینه و مگه بود قادر به ساخت «توالت» هم نبود!  مستراح هم نداشتن !! اما دنیا در چه وضعی بود؟  ۶۰۰ سال قبل از تولد اسلام!  توی بیشتر شهرهای جهان  داشتن توالت عمومی! اجباری بود!   اینها میشینن روی منبر  میگن «مدینه فاضله»!!  حالا…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/6151" target="_blank">📅 10:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6150">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">تمدن مصر باستان رو مطالعه کنید ابتدا تا انتهاش بر مدار مرگ بود! فرعون از زمانی که سر کار می‌ا‌ومد به فکر مقدمات مرگش بود و قبرش بود!  هنر و پزشکی و علم و مهندسی مصر همه بر پایه صنعت مرگ بود!  مومیایی و اهرام و جراحی پزشکی و….. همه برای کار و کسب مرگ بود و…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farahmand_alipour/6150" target="_blank">📅 10:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6149">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bInibF3peiLlxkW8UF3xqJyasj6hZbHKQ5_zaIodU6-wu95PjUz-ARmzyErw6NSUfWQi-L4gSj8U-x4xR3DFD0O-inPbsvgzJNJ-Tk-cWUh6fFHVK6v_K6n0ZyoCLaeaugSindc8RGDAkIOqohSUzQwk1MMXwMC30t2rUAUnjcq5Xado7XHAU0cipNgjXQzEoCJZJ-hhsCWpy57tYR-g8YO1hrYNMQEnsGQFGsIuMpes7DcsSFsYHa1tSctbeagFAmKrPTyqsKLK3bFbkA1VqzUTrBcV4pzLpX3p1UlNuDbBbwQN-QsDwRmJY5vqcop-O6bcZqNb8QgNvnCva65LHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها شنیدید جملاتی با این مفهوم رو که زندگی و این حیات «زندان مومنه»!  آرزوی اینها مرگه! مرگ براشون رهایی است!  اینکه برن و برسن به بهشت و به زندگی!!  مرگ رو آرمان خودشون می‌دونن و زندگی و زیبایی‌هاش  رو پست و حقیر معرفی میکنن!  و اینکه باید دائم به فکر مرگ…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farahmand_alipour/6149" target="_blank">📅 10:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6148">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اینها اگه می‌بینید برای مدرسه میناب و…..  سر و صدا میکنن، فکر نکنید به این خاطره که «اصل زندگی»  رو دوست دارند. و از مرگ متاثر میشن!  تمام هستی اینها :  مبارزه، جنگ، کشتن،  کشته شدن و….. است!  زندگی براشون چیزی نیست جز  «مبارزه  برای عقیده».  و خوشحال میشن…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farahmand_alipour/6148" target="_blank">📅 10:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6147">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b6d93f0a9.mp4?token=q98kEx6iNp_WnGzLTkyYFLNUw4eGcMB9OPe_bW_hQEgqIAt4M1mSRhHRvzOOqLzY3wEOssewJDfFlMx3bAnuT0nhOAkBNu-NtfsP_COQK1b0UHINqRLj3ZpGFaRpjGxnsExOOoQBz25m1qZPie2W5V0xSx6zqPRA6SdmWu_cV3nienJ4wJanO-1V1kB1PjfBszENmvBm5p8tUwn3pKR7yAICXvWt2Wv0J7QocNXpS0qwSN5NTt8T-sxH_7GCr253pz66AiJyaV3vVvXfjYw-bjS3frD228oI8m4ArEDDJ4gSuH0QqLL1Ubj1fplS6YDI6VRqtTITOqkwyg_B8J2xkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b6d93f0a9.mp4?token=q98kEx6iNp_WnGzLTkyYFLNUw4eGcMB9OPe_bW_hQEgqIAt4M1mSRhHRvzOOqLzY3wEOssewJDfFlMx3bAnuT0nhOAkBNu-NtfsP_COQK1b0UHINqRLj3ZpGFaRpjGxnsExOOoQBz25m1qZPie2W5V0xSx6zqPRA6SdmWu_cV3nienJ4wJanO-1V1kB1PjfBszENmvBm5p8tUwn3pKR7yAICXvWt2Wv0J7QocNXpS0qwSN5NTt8T-sxH_7GCr253pz66AiJyaV3vVvXfjYw-bjS3frD228oI8m4ArEDDJ4gSuH0QqLL1Ubj1fplS6YDI6VRqtTITOqkwyg_B8J2xkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها اگه می‌بینید برای مدرسه میناب و…..
سر و صدا میکنن، فکر نکنید به این خاطره که «اصل زندگی»  رو دوست دارند.
و از مرگ متاثر میشن!
تمام هستی اینها :
مبارزه، جنگ، کشتن،  کشته شدن و….. است!
زندگی براشون چیزی نیست جز
«مبارزه  برای عقیده».
و خوشحال میشن اگه زندگی رو به خاطر اون عقیده نابود کنن! زندگی نیمی از مردم جهان هم نابود بشه براشون مهم نیست!
چون «برای یک هدف بزرگ‌تر»! مبارزه میکنن!
پس چرا مثلا روی مدرسه میناب مانور میدن؟
چون میخوان شما رو بیارن توی صف مبارزه خودشون
برای اون هدف بزرگ‌تر !
برای جنگ‌های بی پایان تا رسیدن به هدف بزرگ‌تر!
اینها نمیجنگن تا در این دنیا آرامشی باشه
و صلح بلکه میجنگن برای آخرت!
برای اون دنیای دیگه مبارزه میکنن!
از این زندگی و این جهان متنفرن!
این زندگی رو فقط یک پل می‌بینن! یک فرصت برای مبارزه و کشتن و کشته شدن و….. که بعد توی اون جهان به آرامش برسن! این زندگی فقط عرصه و میدان جنگه براشون!</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6147" target="_blank">📅 10:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6146">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S67FAPbGcSIj2mIMHB3rweXRNd9SeixdnSv8uvrcwW8nnvOtbl0mhQ95jnqSUYbjvGfmho4R6Ei5xQ40o39fj6JfxvGefHFtdDyo6aRh04UmLkVAAsInsKYlzqmuJQs-18faNQ3hC2c7FxONqK1LlxGO-S1wt1buPHFkbTI0qzrEdES4bLTCIb1DLuPjKH07FY6wjWt8Eij3kbViicG7zHZ9WI0tf7C-ipY4FwP2EijBmkd7tORJMqhhusXvszV6kuPkLvoCs7cJuq5qjLeuY_2tMU-eNnXll7N5m2QAlPS0koNASticS7RQENihNJiJvW3sqJXqvNtUahktGgzXuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ایران به یک شهروند زن آمریکایی که در دسامبر ۲۰۲۴ در دوران رئیس‌جمهوری جو بایدنِ خواب‌آلود به‌ناحق بازداشت شده بود، اجازه خروج از کشور داده است. او اکنون در سلامت کامل در خارج از ایران است. ایالات متحده آمریکا از این ژست حسن‌نیت ایران قدردانی می‌کند.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6146" target="_blank">📅 09:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6145">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
حملات دیشب به استان‌های خوزستان، سمنان، مرکزی و لرستان
🔺
دیشب تعداد زیادی انفجار در اهواز شنیده شد. برخی‌ها تا ۹ انفجار و برخی تعداد انفجارها را بیشتر تخمین زدند.
🔺
گزارش‌ها حکایت از آن دارد که یکی از موشک‌ها در اهواز و در نزدیکی یک بیمارستان (بقایی) اصابت کرده.
🔺
دیشب همچنین به چند نقطه از استان لرستان حمله شد، برخی گزارش‌های تایید نشده از حمله به پایگاه موشکی امام علی در لرستان خبر می‌دهند.
🔺
استاندار سمنان نیز گفته که به بخش‌هایی از فرودگاه سمنان حمله شده، کسی کشته یا زخمی نشده.
🔺
استاندار مرکزی: شب گذشته به دو نقطه در اطراف شهر خنداب حمله شد. این برای چندمین بار است که اطراف شهر خنداب مورد حمله قرار می‌گیرد.
نه آمریکا دقیقاً مشخص می‌کند چه اهدافی را زده و نه ج.ا می‌گوید به کجاها حمله شده.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/6145" target="_blank">📅 09:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6144">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">استاندار مرکزی : شب گذشته به دو نظقه در اطراف شهر خنداب حمله شد.
این برای چندمین بار است که اطراف شهر خنداب مورد حمله قرار می‌گیرد.
نه آمریکا دقیقا مشخص میکند چه اهدافی را زده و نه ج‌ا می‌گوید به کجاهاش خورده.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6144" target="_blank">📅 08:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6143">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اطلاعیه  ارتش:  سامانه‌های راداری، سامانه پدافندی پاتریوت و مخازن سوخت آمریکا در پایگاه علی‌السالم کویت را هدف قرار دادیم.
‏ رادار‌های سوپر هاوک، تأسیسات و سامانه‌های پاتریوت واشنگتن در پایگاه شیخ عیسی بحرین نیز طی حملاتی، آسیب‌های جدی دید.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6143" target="_blank">📅 08:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6142">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
استاندار سمنان : به بخش‌هایی از فرودگاه سمنان حمله شده، کسی کشته یا زخمی نشده.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6142" target="_blank">📅 08:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6141">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAn2Rhw6MG6nUjkdmcJSlFMjL-HZVXD_LhnzWuhO6nAT7foyaLOQhDi7Fpk3aDpNU_YRpLkVFdOM2d2AQUnLueSAd28tre0PkbGARbX6AbalhclNxd9blwOmYQPwBfOE8eHEUtslFt_JkQuKPSxFKih_wrX-reObp9UPdFTCZxQBizFwDmJs1ZccE0-wh-ZItW4uMHGXMFV8VTxh00qbSs6y6G58R2DF51lOtxcxWXH7VNkJ-6BYxkMSbs_VWmyQ4CfdDkbXQlK-Qrch_3Pjc9ox2-uy9k8D7ht7_ySacrDYQvwv6aUddBJx7z8GXAHo7RPrvowI3N-LssBt5r__Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین یارو خودش از دست سپاه و نهادهای زیر نظر خامنه‌ای  فرار کرده و به آمریکا پناه برده!
و آمریکا رو خونه امنی پیدا کرد برای زندگی و نوشتن از اینکه اسلام چقدر زیباست و خوبه و سعادت انسان رو میخواد!
حالا از همونجا به ج‌ا میگه مبارزه کن با آمریکا! مطلقا تسلیم نشید! تا انتهاش برید!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6141" target="_blank">📅 08:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6140">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">برخی گزارش‌ها از تداوم حملات به اهواز خبر می‌دهند و اینکه تاکنون ‌۹  انفجار  مهیب در شهر شنیده شده.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6140" target="_blank">📅 23:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6139">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
چندین انفجار مهیب در چابهار و بندرعباس
🚨
کویت : امروز ۲۱ پهپاد و ۴ موشک شلیک شده از سوی ج‌ا را منهدم کردیم.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6139" target="_blank">📅 22:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6138">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای ۲ یا ۳ انفجار در اهواز</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6138" target="_blank">📅 22:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6137">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1IRIhMok3xsIlQAiQSYxJYWubrCgyya2gHbNsRAwnnq3-wKqo-DcDjeQHNEzHNtTB89jeCvWltrb61PK1cr95znfSRukDWNlcOmx0HjxL24aqcfS-D5vx1ZEIFj0UO_RIafa9x1z8G6WSiQzsHPyK2MHBWoXNrEhKVzIgigaeCaNTHHoD5xADbRbJP-V6QNhQgLNuxK9aS_vETJ5ckRT6CLLJQP6ZkIM4eAT8ofx3AKPHeaVY5ZwBgJ3MZoXzZU_-nRTpq0rglt1dFNonbmk4kAszGpcrqSTDaEQ2QB1AKOmjH4EPGSPZxVHkVgNJVFIXfsHlJy7faUnONVhsb7Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شما دیگه جرات حمله به اسرائیل
رو ندارید! خودتون هم خوب می‌دونید!
این ۴-۵ روز هم به همه جا حمله کردید
به جز به اون کشوری که بیت‌رهبری
رو زد نابود کرد!
و نشون داد دقیقا کجاست که سست‌تر از لانه عنکبوته!
ولی هر چقدر دوست دارید شعار بدید!
اون حزب‌الله تروریست هم رفت انتقام بگیره  هنوز و همین امروز هم نیم میلیون نفرشون  توی محله‌های مسیحی و سنی لبنان آواره شدن!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6137" target="_blank">📅 20:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6136">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">آنچه شب گذشته در بمپور رخ داد و موجب  کشته شدن تعدادی ای نیروهای ارتشی شد، قابل اجتناب بود.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6136" target="_blank">📅 20:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6135">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e615d142.mp4?token=t5bsUkX-IeEFYc-YKvCCy9f2SEvxB9RMzrzuXUzsgFJo_X3TvvVdU9_i4Kmr0TL7gbXqYJHZFHsKFSjbACt-GTX4vTZ_xQOu-faBmsWhgDXiJXVN_K0CxXG0FZZuDvQ0HlVLduZu_zrQsR-p5baxal3lcxAAwITMkPqWuact3TIUcoUxxou2Iw1H2HxWuBwv2e0dHhLtV7G9zTwCOwq5dyFdK-6whBnTGJ1igqyoSrW3D7QMPoUaRlT_K4Hgqo64oUqNjeMkJ0h6taCVlzEiiEt1VQgRATitKGCDmbktw96wL2nYE_zeo2r6mnZyXva8Ijdt8oKUnU9ixnWxjnO7dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e615d142.mp4?token=t5bsUkX-IeEFYc-YKvCCy9f2SEvxB9RMzrzuXUzsgFJo_X3TvvVdU9_i4Kmr0TL7gbXqYJHZFHsKFSjbACt-GTX4vTZ_xQOu-faBmsWhgDXiJXVN_K0CxXG0FZZuDvQ0HlVLduZu_zrQsR-p5baxal3lcxAAwITMkPqWuact3TIUcoUxxou2Iw1H2HxWuBwv2e0dHhLtV7G9zTwCOwq5dyFdK-6whBnTGJ1igqyoSrW3D7QMPoUaRlT_K4Hgqo64oUqNjeMkJ0h6taCVlzEiiEt1VQgRATitKGCDmbktw96wL2nYE_zeo2r6mnZyXva8Ijdt8oKUnU9ixnWxjnO7dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیش بینی تاریخی بختیار
در دو کلمه، برای مردم ایران</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6135" target="_blank">📅 20:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6134">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=dxunYWxfChNIXlVxiSVeFshsDLCLICo8KsaA1214pc5ymuvIt67vVs8quClylAVmJIjIj2hQeUckvs-hqWDGkF4KA6zsNry5YHXGlIlft1XHcJAQaiu_6hGw7s-2rSfRlyz5QAbo1BUIXGhuN4IRW6D3mtWDNIuNkwcN7iih3gDphASoC7HuNfSDU32XTfC_6QBocklmJKLnBY65ZmaNnQVSp5noF2ZXNw2IRyv2Qj4qeUG9SKl6_xhUZx1aSKUtVSFR92LrfXo77t-XWw2kVGGqhBoIVpgoj7xAfGDl4YA9oP06EBjKZZ2oMZU2VcluPsWSuwSJrap5673QQvapBoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=dxunYWxfChNIXlVxiSVeFshsDLCLICo8KsaA1214pc5ymuvIt67vVs8quClylAVmJIjIj2hQeUckvs-hqWDGkF4KA6zsNry5YHXGlIlft1XHcJAQaiu_6hGw7s-2rSfRlyz5QAbo1BUIXGhuN4IRW6D3mtWDNIuNkwcN7iih3gDphASoC7HuNfSDU32XTfC_6QBocklmJKLnBY65ZmaNnQVSp5noF2ZXNw2IRyv2Qj4qeUG9SKl6_xhUZx1aSKUtVSFR92LrfXo77t-XWw2kVGGqhBoIVpgoj7xAfGDl4YA9oP06EBjKZZ2oMZU2VcluPsWSuwSJrap5673QQvapBoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی که فرمانده سپاه بود و سالها فرماندهی جنگ رو بر عهده داشت
اینجا میگه مطئنم که مسیری که در ذهن مجتبی خامنه‌ای است، بهتر از مسیری بود که شورای عالی امنیت ملی رفت.
مجری ازش می‌پرسه خب اون چه مسیری بود؟
میگه : نمی‌دونم ! نمی‌تونم که ذهن خوانی‌ کنم!
فقط می‌دونه خوب بود :) یه مشت چاپلوس !</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6134" target="_blank">📅 16:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6133">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid Online وحید آنلاین</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pWvX1Nh2zQqkwy3b-h-7B3wtKoi1ecduaVwpRDsbxnpv3JRqjeq9WmQkGONSYVq7MXb6689HXo2EOQj7k6BZKfzE1nXzq0nGCkdc4oK017DR9QbkA5VufzBP7FTwSHLLWbcgUEA-TiprLOxZdPGsfZBS5JF0m8C9UPmtnnkNi_H51j4c9UpNDalZYWavBBZ6-46Szrs1NtMRHUrxuC7gangsqhQ4T6CnW3Ibl44xTpzUT6WyCIseo3hpbYSHlZIKSgTOjnWqvShO1JvypMk5A6sredbIyGQIZCkaUFsLK0JmYSQOkzPWUFWJOregU-jKHEDpDcIo-S4jmrsx9lTZ2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضاییه جمهوری اسلامی از اجرای حکم اعدام محمد امینی دهاقانی، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، خبر داد. مقام‌های قضایی او را به آتش‌زدن فرمانداری و کلانتری مرکزی شهرستان دهاقان در استان اصفهان متهم کرده‌اند؛ از روند بازداشت، بازجویی و جلسات دادگاه و … محمد امینی دهاقانی خبری منتشر نشده.
براساس اطلاعیه منتشر شده در خبرگزاری میزان، ارگان رسانه‌ای قوه قضاییه، حکم اعدام محمد امینی دهاقانی پس از تایید در دیوان عالی کشور، بامداد امروز ۲۴ تیر ۱۴۰۵ اجرا شده است.
در این اطلاعیه آمده است که امینی دهاقانی روز ۱۹ دی ۱۴۰۴ با پرتاب کوکتل مولوتف به ساختمان فرمانداری دهاقان باعث آتش‌سوزی شده و سپس یک کوکتل مولوتف دیگر نیز به سمت کلانتری این شهرستان پرتاب کرده است. مقام‌های قضایی همچنین مدعی شده‌اند او در تحریک معترضان برای حمله به کلانتری نقش داشته است.
دستگاه قضایی جمهوری اسلامی بخش عمده پرونده را بر اعترافات متهم استوار کرده است. در اطلاعیه رسمی ادعا شده که او در بازجویی‌ها پرتاب کوکتل مولوتف به سمت فرمانداری و کلانتری را پذیرفته و همچنین گفته است قصد داشته از یک قبضه سلاح کلاشینکف، که به ادعای مقام‌های امنیتی از ماموران گرفته شده بود، استفاده کند.
محمد امینی دهاقانی همچنین به «بازنشر و ارسال محتوای تبلیغی علیه جمهوری اسلامی، تشویش اذهان عمومی و برهم زدن امنیت روانی جامعه» متهم شده است.
او همچنین به «درخواست ارتباط‌گیری با حساب‌های کاربری» مخالفان جمهوری اسلامی و «درخواست ارتباط‌گیری» با صفحات مجازی مرتبط با خاندان پهلوی هم متهم شده است.
مقام‌های قضایی هیچ اطلاعاتی درباره نحوه دسترسی متهم به وکیل مستقل، شرایط بازجویی یا روند برگزاری دادگاه منتشر نکرده‌اند. همچنین مشخص نیست اعترافات منتشر شده در چه شرایطی اخذ شده و آیا متهم امکان رد یا اعتراض به آن‌ها را داشته است.
اعدام محمد امینی دهاقانی در حالی انجام شده است که نهادهای حقوق بشری بارها نسبت به افزایش صدور و اجرای احکام اعدام برای معترضان و متهمان پرونده‌های امنیتی در جمهوری اسلامی هشدار داده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6133" target="_blank">📅 15:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6132">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
سنتکام : به تنب بزرگ حمله کردیم.
در جریان این موج ۹۰ دقیقه‌ای از حملات، با استفاده از مهمات هدایت‌شونده دقیق، سامانه‌های دفاع ساحلی و محل‌های ذخیره‌سازی و پرتاب موشک‌های کروز در جزیره تنب بزرگ را مورد حمله قرار داد.
این حملات توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را بیش از پیش تضعیف کرد.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6132" target="_blank">📅 15:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6131">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">حمله امروز به چابهار</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6131" target="_blank">📅 14:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6130">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
ارتش: «آمریکا بامداد امروز با شلیک ۱۳ فروند موشک، آسایشگاه و محل اسکان یکی از پادگان‌های نیروی زمینی ارتش در بمپور را هدف قرار داد
دشمن به مهمانسرا و اماکن نگهبانی پادگان حمله کرد
‏ ۷ تن از کارکنان پایور و وظیفه تیپ ۳۸۸ ایرانشهر شهید و تعدادی مجروح شدند.»
‏</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6130" target="_blank">📅 14:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6129">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
سنتکام : از نیم ساعت پیش موج تازه‌ای از حملات را آغاز کرده‌ایم.
(از  ساعت ۱۳:۳۰ تهران)</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6129" target="_blank">📅 14:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6128">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7Q6WBCZNEPYCQbX-plpI9v0G7qkn71b3zY0xNaMBZeBOR5Zi9y2W_dmz0hopXZ3QqW5JISL5KYc7pz8bxE5yh3rD3G4ArhOYVFuvoB8Z6LkO7OK7-putT3YK7UlD9k5LmkBYYJADVFY5138VxAUgElSiYx0qWYzBE8g6lEICbV3fV2AnA_QjVwfsqYcCtAENXVDU5XfTx7Bi0KZjgxZ-Cx3LGploRQYrfLLNw2Je3w8t8NIXilX2yGqlbYC_9GHYup6StBGZ7vISzeL-QIDTmrnUtvIP1ShctNyL2C5tpLxHmDSp_miBw1Vds-o5cbc9jt5ItxFgVaHAXhX-rffMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابل توجه ساختاری‌های محترم
مدیر حوزه‌های علمیه با بیان اینکه مسئولان باید تفاهم‌نامه‌ها را پایان‌یافته تلقی کنند، از دولت و شورای عالی امنیت ملی خواست به دلیل بدعهدی طرف مقابل، مسیر مذاکرات را متوقف کنند.
مشکلات اقتصادی یا ترس از آسیب به زیرساخت‌ها نباید موجب واهمه مسئولان و رویگردانی از مسیر «جهاد و استقامت» شود.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6128" target="_blank">📅 13:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6127">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=OgAO8qPnek9XJ5nRdAV5Xqx7Y3oOIjMjCCjDToAza1lc5pwb-zHozts27oGMd2UxamUC_6ozL_HxoQaGWd9mQPB944fabmQhzdQWCH47rFSPaWLjYlwpO0EikCct9KG9ysbZkxhS7zh5NAdCni2G7Ay5mCciA3cu0xmGcFX4kmSudlQilwOCpEIe2l4vfNrWVSYbt1M6H9sLNRt9DzRTy4TiotAx7HEIusI42r3u8603c4xoBMUnCAC6edhou9iTj5zqp-m1cIW9qJAzk2hymvc-4S86c4tcbvedQw0TrIXL-T78SjkPuht02TzWs0pwnY0KC9p9pOwLfEgs_MV0GEk4zRiVQ00PBZYbrm9CDmH2BRP8y_KnCMvE6fq0AnVB1ggvRmkwujnBKZXAGKNIrlgq2nqAcAx3iYiq3IErypN30u21kQ9r77yzrd6kq-UOjJM_dZFFmHLhG647AJ1csidHSKKA0IGiYl2o1dHprGs128S0WyNKbCGrN-AJXxaejkP4kYTLr3rv1RmVsKMugGPPEZ0PQ-PO7ul3ck21W2sBD6ofShS8NeFBX98Bh4Mg-VJcaQDmmL1eJto_p660UE8Zkj3smn0toqZu2iEMPy3B6HU1nJmRfPZCj2kSS2KZKjBLF_luLQdQqIACi2DtOKRo1N6UJUPxvviLAOVkC_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=OgAO8qPnek9XJ5nRdAV5Xqx7Y3oOIjMjCCjDToAza1lc5pwb-zHozts27oGMd2UxamUC_6ozL_HxoQaGWd9mQPB944fabmQhzdQWCH47rFSPaWLjYlwpO0EikCct9KG9ysbZkxhS7zh5NAdCni2G7Ay5mCciA3cu0xmGcFX4kmSudlQilwOCpEIe2l4vfNrWVSYbt1M6H9sLNRt9DzRTy4TiotAx7HEIusI42r3u8603c4xoBMUnCAC6edhou9iTj5zqp-m1cIW9qJAzk2hymvc-4S86c4tcbvedQw0TrIXL-T78SjkPuht02TzWs0pwnY0KC9p9pOwLfEgs_MV0GEk4zRiVQ00PBZYbrm9CDmH2BRP8y_KnCMvE6fq0AnVB1ggvRmkwujnBKZXAGKNIrlgq2nqAcAx3iYiq3IErypN30u21kQ9r77yzrd6kq-UOjJM_dZFFmHLhG647AJ1csidHSKKA0IGiYl2o1dHprGs128S0WyNKbCGrN-AJXxaejkP4kYTLr3rv1RmVsKMugGPPEZ0PQ-PO7ul3ck21W2sBD6ofShS8NeFBX98Bh4Mg-VJcaQDmmL1eJto_p660UE8Zkj3smn0toqZu2iEMPy3B6HU1nJmRfPZCj2kSS2KZKjBLF_luLQdQqIACi2DtOKRo1N6UJUPxvviLAOVkC_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سفیر اسبق جمهوری اسلامی در روسیه: مطمئن باشید اگر ترامپ را بکشیم نه تنها هیچ موشکی به سمت ما شلیک نخواهد شد، بلکه عقلای آمریکا با خوشحالی جنگ را تمام خواهند کرد.
کشتن ترامپ هیچ هزینه‌ای برای ما ندارد و با کشتن او جنگ هم تمام خواهد شد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6127" target="_blank">📅 11:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6126">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟  به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6126" target="_blank">📅 08:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6125">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mn1jZ-cFqnHoZH2ANs156fu2OoPRB5vxREVL-88JidwYFw0LTyDBAlHCneyJM7f6pyK_Jbm9qBh1XFiKFDZ2jUglPYjhKwhlK6jzaowF-ej5KJlAPgA7FKdpwTb03GjZmuuwE1yyD5vc6xQ6ylBU-UHwByleeL8PQYv2aQv-XAbPSPKqYQOJKXD6guKwVmO7sXTtMdcIXcXhHdLs5nTzqE_PxobNt33ZtFPouASv1KMgjztPnqtJ3wvQfogD0n2uocIx6PbxeeRXBxCYhvU-XP8ENHaH9uc0hoNwEEkGOf0YRZvXb4DyV-YAGV7pviO6F66hKVlEWrQu_iOwN8PJYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟
به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت کاخ سفید برگزار کرد.
به گفته سه منبع آگاه، در ابن جلسه که ارشد‌ترین مقامات نظامی و امنیتی آمریکا در آن حضور داشتند در خصوص گسترش حملات صحبت شد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6125" target="_blank">📅 08:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6124">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=aEExiIsY1Ihv4h6-lLp_NksQyzRwuebf0RxZZeY7VF55zRnbG4ljpTAC6qZM91O5-sitamGjC1EdCo9JWgcQzsLuRgeoiE0TtAkQPWsR-htVP4qeIAwPeshtmWXRqjE7wNKt-7HLcTvsKhL0O6snqPFwuEjkWcVJQpDYwwj-LpTQJLAqQHihpDpO43_LiJUNxubcINxKiOhl7jMC4CVru1hxPAXamcXPEXDiBHfD2FbtazKyDXFJuVQWAdlFEDn-i2lH9elNlfGuSt65TPO7I-n582wNseqwtWLjJtktrI3fpkqBYVV-RIjy7mt2gPStM5oyHtJI_rXXLH4xG-EjcJxQiMOM6q7apqw_PU76X7V7SR7VK-UU2nMBGgPPX4hw7ZrxeguXY_M5JdQtrDYPECQjOnc8UJWlrgX-9DF0wPr2ETJKBIDkQp0fpDLD1Z9nR2o2MvMaeRRPImp6OJLnueE-xIBdHQCbDkufSygVFZcQJrQXmX63rXLDmyUtDelRdwsapi_JbgyQEBTvFKPgkvrF9dh9TD7WRxMC_PSkq31oVuFVbvbilfyw-ywRet8HHC0F8LjzdAoJVyDBPebjlip8wkEChXTAqsjRJMYK_kxqNlimyvQwE2srpuhdFkJtUOjl-f33O9-UXNuclC_BpIV98LKxjLsBAvkpft1k8IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=aEExiIsY1Ihv4h6-lLp_NksQyzRwuebf0RxZZeY7VF55zRnbG4ljpTAC6qZM91O5-sitamGjC1EdCo9JWgcQzsLuRgeoiE0TtAkQPWsR-htVP4qeIAwPeshtmWXRqjE7wNKt-7HLcTvsKhL0O6snqPFwuEjkWcVJQpDYwwj-LpTQJLAqQHihpDpO43_LiJUNxubcINxKiOhl7jMC4CVru1hxPAXamcXPEXDiBHfD2FbtazKyDXFJuVQWAdlFEDn-i2lH9elNlfGuSt65TPO7I-n582wNseqwtWLjJtktrI3fpkqBYVV-RIjy7mt2gPStM5oyHtJI_rXXLH4xG-EjcJxQiMOM6q7apqw_PU76X7V7SR7VK-UU2nMBGgPPX4hw7ZrxeguXY_M5JdQtrDYPECQjOnc8UJWlrgX-9DF0wPr2ETJKBIDkQp0fpDLD1Z9nR2o2MvMaeRRPImp6OJLnueE-xIBdHQCbDkufSygVFZcQJrQXmX63rXLDmyUtDelRdwsapi_JbgyQEBTvFKPgkvrF9dh9TD7WRxMC_PSkq31oVuFVbvbilfyw-ywRet8HHC0F8LjzdAoJVyDBPebjlip8wkEChXTAqsjRJMYK_kxqNlimyvQwE2srpuhdFkJtUOjl-f33O9-UXNuclC_BpIV98LKxjLsBAvkpft1k8IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مزدوران حکومتی شعار میدن
«جنوب ایران نکند جنوب لبنان شود»
عجب! شما دیگه چرا؟
خامنه‌ای میگفت «جنوب لبنان الگوی پیشرفته
و موفق مبارزه ایمانی است»! سالی یک میلیارد دلار از اموال ملت ایران رو میدین به گروه‌های تروریستی اونجا  و تبلیغ اینکه ما اونجا پیروزیم و …..!
ولی ظاهرا اسرائیل در جنوب لبنان چنان درسی بهتون داد که الان خودتون هم میگید نکنه بشیم شبیه اون «الگوی موفق»! معرفی شده توسط خامنه‌ای</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6124" target="_blank">📅 07:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6123">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=XK_TSJ0kR5bzsyoVAH0hctprZFkOGETLE3R0wn0s39O7nQUeXkflH0JmD3k6JUKjWKoCfy1vcm07taH0L_PhkaCf1zpuaGwStMEw9w0rmmOT3kdVBjR6QHXJXDoJoSXHBxCwmqKz1UCjiFP4cmcMsDIiP54kL6k10xDvQZK9pSpgTA8lVezWnO5JqjaJPCnUzZCDnOMoHTPUSw2QJgpF--gc1wl7vYSSzIKY0k7-ljKg6KxWQmKxKOXOe8YjyO0L6pNJW23OqjSZ_zdfYvi-a-xWdgzgd0cSAXZd6GO-WNKxe1EPpCbGeERFox9e_5sHPE0tJgW9ase98zPjpiJPQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=XK_TSJ0kR5bzsyoVAH0hctprZFkOGETLE3R0wn0s39O7nQUeXkflH0JmD3k6JUKjWKoCfy1vcm07taH0L_PhkaCf1zpuaGwStMEw9w0rmmOT3kdVBjR6QHXJXDoJoSXHBxCwmqKz1UCjiFP4cmcMsDIiP54kL6k10xDvQZK9pSpgTA8lVezWnO5JqjaJPCnUzZCDnOMoHTPUSw2QJgpF--gc1wl7vYSSzIKY0k7-ljKg6KxWQmKxKOXOe8YjyO0L6pNJW23OqjSZ_zdfYvi-a-xWdgzgd0cSAXZd6GO-WNKxe1EPpCbGeERFox9e_5sHPE0tJgW9ase98zPjpiJPQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6123" target="_blank">📅 07:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6122">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=vSygAtyBvFN8QEzaftt7KFln2KS5ZvT9V2k_mlZv42hCOxEuiCfxV-am3vCopD_FV4BwmGrfMK2pbC53gVUMhSJsn3EHbhUZoyK0pI-noYpTf7_4rEd_MJNIfA4L-yhexZqwhXdAdRGvh9z8QYB3Mj4w0scBAJb9e5P3zzhAOnirjomfvu9FwpsVqQGZUC-P6NlNcnDk61NjpxmcFI7WYIDCcykdkguSp2vM-xsIQHDaSnYVQ_7Lq3PHqeqmp-5V0jxHpTHe0PIE9mfnPYgFrJNNxC519BPohaJGz4RPrzNg32R0Ox7YpJxEIcMtkpEKyvOI1ZHq9yGuu1OtZnQs0AyzgWJD56uf_ZzeXHgWYsOvqqH1UeBjSybpf_pc5YwkXCpuV6NJOJEleImkY2gXJkL9TjMRVIzy3Pzr0rG3ipeCd0umREBygR08bDBgwJi4T8yEyDZw-nrmYUwINMn3TAqk-31rbyVSUk5zyve9eaXHG965XExFwJX1aCTzl_jqajzHRjHA8JitEdcacq57wM0wXMXEf45R9RCj86zjcyUao8BdUgkpCbebRcvfnl3XDBBDVvFfRxapxvrEdkwqYOcw3qQjmXIxzxUSICPfW23AewnjaFQTmlAf2vOie3af4FxyuqKVMLOJeKatJuHjfjBwQNWBpMi3rQCZhqw5GCE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=vSygAtyBvFN8QEzaftt7KFln2KS5ZvT9V2k_mlZv42hCOxEuiCfxV-am3vCopD_FV4BwmGrfMK2pbC53gVUMhSJsn3EHbhUZoyK0pI-noYpTf7_4rEd_MJNIfA4L-yhexZqwhXdAdRGvh9z8QYB3Mj4w0scBAJb9e5P3zzhAOnirjomfvu9FwpsVqQGZUC-P6NlNcnDk61NjpxmcFI7WYIDCcykdkguSp2vM-xsIQHDaSnYVQ_7Lq3PHqeqmp-5V0jxHpTHe0PIE9mfnPYgFrJNNxC519BPohaJGz4RPrzNg32R0Ox7YpJxEIcMtkpEKyvOI1ZHq9yGuu1OtZnQs0AyzgWJD56uf_ZzeXHgWYsOvqqH1UeBjSybpf_pc5YwkXCpuV6NJOJEleImkY2gXJkL9TjMRVIzy3Pzr0rG3ipeCd0umREBygR08bDBgwJi4T8yEyDZw-nrmYUwINMn3TAqk-31rbyVSUk5zyve9eaXHG965XExFwJX1aCTzl_jqajzHRjHA8JitEdcacq57wM0wXMXEf45R9RCj86zjcyUao8BdUgkpCbebRcvfnl3XDBBDVvFfRxapxvrEdkwqYOcw3qQjmXIxzxUSICPfW23AewnjaFQTmlAf2vOie3af4FxyuqKVMLOJeKatJuHjfjBwQNWBpMi3rQCZhqw5GCE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا میبینم راست میگه …</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6122" target="_blank">📅 07:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6121">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QwnBcPNWp-UpOhsbsyUAf72hyeVvifOLmI4gZvQ99v_IS8lDDzRhWSWKVkGorIFh_h2fIVKlw4L7E_2Akr5KyifhH5ZX0XBgmB5Xbexx2J_-nCYjWzgxL-q18KWnRK1ik3BZLWgsPkuxZXMtU9bdesdE1Yenl0uk6Hd_zJ4ruScuAn08xwCh09UufclVSNaEoX5e9xfoTfSjlrFUAO6D6LRJwE1lnRQwo_KuKpoYVuEYnLTSz-_oOsbkmu-1nQOto1aLFIMjFuECvKnQbUBNiIgDyF1YYZQJkATj-qN3iUI2NcyEuAAG3m0nE12uzS6rpsYDoSN44d1b6-VVr4PSIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6121" target="_blank">📅 06:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6120">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNewOM08hz98z2NVgMaTEel8kSmpxl9Db994jr_SyDxCGG2-7UvnK07Ja9MFw5DlYRvhtfTsZPcUPESUmB_6pWXs5g_IoQB8KYATFURUKdySPXr2Jdz4WGNuT_fROzm8UyhiI1n6mWHDWoGTzw9Q_va-vHhvhT6XsYc-NoNsQ9DXliJbyPvDjEA7M5y0_80nUv4Pvmhd8NuU7EGqm3E26BGiBs5de6jHgb7SizKi4GZU7cNCzIM9ek6ETar5UleZ0xoHbga9RN-yRKVCrrmMsG-0GwOeAHjMsv06NKfAd-cUwt1njPN9NzDhC6VVQpH89LULeB_F_H2rCIWjxuwoqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6120" target="_blank">📅 06:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6119">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=XEzx5YcElxvI6BZ5oC_24M3_KjGP2ZtV9fj9vC75bBdoRCzgnslDtcU4GO0vrVgc20lLT4aOgdGbjK35YdHwD1PloT8J6LnPKzBmmq1pb1M__E1WUbAhz3MozD0KU48IzeDkgc-YZp21ImVDbPhmwqRYSj3LofhWgD9i-JsK4Q3lEV4FdMnD8nIRJ_KcZ0JTsj_rJcQHCvMnToQnAS25PvfgveF02iBx69THeXxYYF53jgpII3vdNj1q-HOcDriOKWf50MzS8VC3MKJ7SalmJYgkqiwguMwc81BzlEAr4Qy9bbnU0S2_NczVFl3Mwm5m5OSU7gHV7d5W--3iBz7KMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=XEzx5YcElxvI6BZ5oC_24M3_KjGP2ZtV9fj9vC75bBdoRCzgnslDtcU4GO0vrVgc20lLT4aOgdGbjK35YdHwD1PloT8J6LnPKzBmmq1pb1M__E1WUbAhz3MozD0KU48IzeDkgc-YZp21ImVDbPhmwqRYSj3LofhWgD9i-JsK4Q3lEV4FdMnD8nIRJ_KcZ0JTsj_rJcQHCvMnToQnAS25PvfgveF02iBx69THeXxYYF53jgpII3vdNj1q-HOcDriOKWf50MzS8VC3MKJ7SalmJYgkqiwguMwc81BzlEAr4Qy9bbnU0S2_NczVFl3Mwm5m5OSU7gHV7d5W--3iBz7KMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام فیلمی از حملات خود به ایران منتشر کرد.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6119" target="_blank">📅 06:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6118">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=VFcZvr5GUOSDqNO_Me9uhcviD8ZobpNjGgVdkRfalRU5anMZ0ACChU424YD5eKyIUrRkmgx3QpGLvVb9Y49Di1g8ZKNg9CQUWfuL-hF7ixWlp8ECUdtXZ02KjrXGA5a5N-mD2fkWvAYJKZxAhTh7syxGVkKXm-m_3uipL4s3Xpr19bvFdF1wOTgA-yGktbimnk_hjEPYpqxwjP9WkRbYcj-_krtCgVpY0kPtgxbXEu4-OckWcZF8Caen0U4wRcTwfNI4ZL-QXCAqOCaWGftd_tY3UVLrEDCZ6CtY2iraDMwaRy7hcX9Ep49HctdZ7Tf3DmSeUqWYNcykmZRtRmEQUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=VFcZvr5GUOSDqNO_Me9uhcviD8ZobpNjGgVdkRfalRU5anMZ0ACChU424YD5eKyIUrRkmgx3QpGLvVb9Y49Di1g8ZKNg9CQUWfuL-hF7ixWlp8ECUdtXZ02KjrXGA5a5N-mD2fkWvAYJKZxAhTh7syxGVkKXm-m_3uipL4s3Xpr19bvFdF1wOTgA-yGktbimnk_hjEPYpqxwjP9WkRbYcj-_krtCgVpY0kPtgxbXEu4-OckWcZF8Caen0U4wRcTwfNI4ZL-QXCAqOCaWGftd_tY3UVLrEDCZ6CtY2iraDMwaRy7hcX9Ep49HctdZ7Tf3DmSeUqWYNcykmZRtRmEQUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : امشب، فردا و فرداشب به سختی به آنها ضربه خواهیم زد و هفته آینده پل‌ها و نیروگاه‌ها را هدف قرار خواهیم داد، مگر آنکه  مذاکره کنند.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6118" target="_blank">📅 06:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6117">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caeb092620.mp4?token=iQE8a8e9IrdWMqWi61v4pRbbU4VoVWEqlmsjAnAWEXE9XSmmTK3otDThVR6h_Y0zFvXSx5raESr4kGa-fsoKvZnQNSKoHyohSh_cvtCDT0soPLgCkT9TG5obAGjq7SoOxXIC6mr5rw2LZp7oKYtJPjZ8BOB2BlpmSLJhkJQTF4jOkwtFbPP6wc45r_F5UTg35E6Y0ntf520SmQF1qFFr61WxxRWJgIAV5JzZqxzcK49hVH_rJm--ZtSvqPGDmXhysUWIEZ0MNxcrTuLFjSCwzSKs-HzvJU9wBfiDHveLgYxaZZFUPUvRaGRXBLaZi4_l-3Ga3-Ai8uAY9oTyL634bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caeb092620.mp4?token=iQE8a8e9IrdWMqWi61v4pRbbU4VoVWEqlmsjAnAWEXE9XSmmTK3otDThVR6h_Y0zFvXSx5raESr4kGa-fsoKvZnQNSKoHyohSh_cvtCDT0soPLgCkT9TG5obAGjq7SoOxXIC6mr5rw2LZp7oKYtJPjZ8BOB2BlpmSLJhkJQTF4jOkwtFbPP6wc45r_F5UTg35E6Y0ntf520SmQF1qFFr61WxxRWJgIAV5JzZqxzcK49hVH_rJm--ZtSvqPGDmXhysUWIEZ0MNxcrTuLFjSCwzSKs-HzvJU9wBfiDHveLgYxaZZFUPUvRaGRXBLaZi4_l-3Ga3-Ai8uAY9oTyL634bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار ناشی از حمله پهپادی امشب سپاه به کویت
گفته می‌شود مخازن سوخت ارتش آمریکاست.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6117" target="_blank">📅 06:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6116">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/360d24e506.mp4?token=uo1riU9JY6si5OKrOqL0kZY-RHXPsjZ9jfAGL9GsLhTs-RYe2k3N1FBzNaXf0Wxys0xRPCp73O0K6z_S-JMLBGWgftyQLsD5zhssQQMilg3CtGoCREHQotqABFSSKLtHFNg37pZ4fqb0n4_HqJXVVe2Eoeq9vzDAYjOBowjP6NWCQ3_1gOyPhoGw17To3YhI2sl-WeCFdHH6GjtmU4D5wZ9tx_NjcBC1YwSGUCkzRcOIVk8GRImFNnk-a_ZO-rkfhDjpPjJ7vDO2cN9jsYEq37PoXLU8VMn6yWsi26xeTEQrxZq0JD21XLGrp3PgA3rZTfgqJ_P__kRiBOX29sPuHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/360d24e506.mp4?token=uo1riU9JY6si5OKrOqL0kZY-RHXPsjZ9jfAGL9GsLhTs-RYe2k3N1FBzNaXf0Wxys0xRPCp73O0K6z_S-JMLBGWgftyQLsD5zhssQQMilg3CtGoCREHQotqABFSSKLtHFNg37pZ4fqb0n4_HqJXVVe2Eoeq9vzDAYjOBowjP6NWCQ3_1gOyPhoGw17To3YhI2sl-WeCFdHH6GjtmU4D5wZ9tx_NjcBC1YwSGUCkzRcOIVk8GRImFNnk-a_ZO-rkfhDjpPjJ7vDO2cN9jsYEq37PoXLU8VMn6yWsi26xeTEQrxZq0JD21XLGrp3PgA3rZTfgqJ_P__kRiBOX29sPuHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی با موشک‌های حاوی بمب‌های خوشه‌ای به بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6116" target="_blank">📅 01:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6115">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
ارتش : به پایگاه‌ها اف ۱۸ های آمریکا در اردن حمله پهپادی انجام دادیم.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6115" target="_blank">📅 01:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6114">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‏امشب اتفاق جالبی افتاده، به محض اینکه خبر انفجاری در شهر و استانی منتشر میشه، مسئولان جمهوری اسلامی سریعا مصاحبه میکنن و میگن دروغه و همه چی آرومه!
‏اینطوری مثلا میخوان صورت مسئله رو پاک کنن.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6114" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6113">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9JZzgtL9YRu9WKK0QCekDOHE99N3uO_2fyG1oFfxkkH0ZBkL5CoNKoCrRPDgJMgvm_oapAQaGigII3t67aeKdZ-Pkx7RSShSkRfl1q7YQmiZ60VJyVBvxqKWmXu7KeJrPEU1ddYFp62cBZ1855HuB_RO3a99vSbsG9T9A33YhAAA6ZNgcjiuUjzAsWuFVXWUfJLd8RkerGQ9P0QIlj6l6AR0YUGSWAb3JmDjZpjR3Xp3Q1R4NVSje9QnhNtZU1SHpu8EybJKg7GscVHDuQqctBNV0lC9t1CBEmSfKJyRUFJVps2CXQXsXwuTtt0I5b30qABYda1ZjZHVXvxc7PUaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگارهاشون می‌نوشتن که کشتی‌ها دارند  از مسیر عمان رد می‌شوند، تشییع جنازه،  بریم و کاری کنیم که  کشتی‌ها مجبور بشن از آبهای ایران رد بشن  و شروع کردن به حملات به کشتی‌هایی که از مسیر آب‌های عمان میرن.  به زور حمله میگن کشتی‌ها باید از مسیر ما رد بشه.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6113" target="_blank">📅 01:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6112">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Go_8LMy8_uVDwbAa6-XZXn6BVa2v8cXGt_jYKPY3estPxS409UUaVC7ypC5WpFhUC5pul-WVlaAUNcye_9OShgjP25HL97C0I2YdrxdkpPb4ej2tH0l4VhuU3bRhJfeRt23RXpu7HO7zHYn5MowKTd8O-sk2SOUcGAHkc7pKu0-QFy8e84Jvx77I3kxvWkq9Mql96b6_V4Ft_WaVoDyajEfsSpudUV3keqO_qsQfCOVkAVa7RKLJBvA-uxhszqBCBciH8UQtS7E3jILAEayJlc9X-P8LMMSBV-MJ-XxvgUeTJ7rUVrlefD84-9osy8fQNJsFahXmYmLQM0O6VcIdQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا در حاشیه خاکسپاری جسد خامنه‌ای و جلوی قالیباف شعار میدادن «مذاکره با دشمن خیانت است»  هنوز به سه کشتی حمله نکرده بودن و نزده بودن زیر تفاهم نامه</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6112" target="_blank">📅 00:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6111">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=Qbr8uhXL6nBPxLH_oo--fgu8tAp6lhPots8Lh7m4VLMUa-BYwbHWUkI_64TjQ3i508iutv2oC2YMyaR5m9UO4Zfma0ucyHYAV0CqzBOkKk1xy2fMDjL7JmMBwBZtzamf7gTvQF3YMrkNTEWppQoKu2atatZD2v5dTKyAtY392xHY4l9kx4NaqSEYq5iM8f3k5jqn7Nb7bVRCFhAxRWPo5wKPMNllLNuTr3Db48tXqyP1n-WfHH_MB4VMJZeeurm-GjEpl4IUWDO2L3AMhlGehVT-Sd2nG9NAywoPL10pmMfomCkxkl6Xt2nGQ4A-yjWC7o2tUSvYF4MVyZUott6R2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=Qbr8uhXL6nBPxLH_oo--fgu8tAp6lhPots8Lh7m4VLMUa-BYwbHWUkI_64TjQ3i508iutv2oC2YMyaR5m9UO4Zfma0ucyHYAV0CqzBOkKk1xy2fMDjL7JmMBwBZtzamf7gTvQF3YMrkNTEWppQoKu2atatZD2v5dTKyAtY392xHY4l9kx4NaqSEYq5iM8f3k5jqn7Nb7bVRCFhAxRWPo5wKPMNllLNuTr3Db48tXqyP1n-WfHH_MB4VMJZeeurm-GjEpl4IUWDO2L3AMhlGehVT-Sd2nG9NAywoPL10pmMfomCkxkl6Xt2nGQ4A-yjWC7o2tUSvYF4MVyZUott6R2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این استوری رو ۶ روز پیش گذاشته بودم  میگفتن آمریکا میخواد آتش بس حفظ بشه ولی جمهوری اسلامی باید «کار دیگر» بکنه!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6111" target="_blank">📅 00:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6110">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550f13e765.mp4?token=ryEUSonkx9fMqija6oaWg0OL5Dog2uDHgbpKQALn-3ZhqYXmnpTK3j55lkbwLcvqWepYyCVD5Xyg8Hw-MxI3B4rkL9cNLLX6fVjh99bc_9kmJWHHdblN6hX0GfyG2-qiMHooVPNh5DMIulaRyBfdzd8MvjZfcmZZSqvtwYGo5_BUI_6scQikj1gsBy43VXRzehjPSKQw3Dei4Hlo7t5AwQjXg2V1s1R5LgTqpcZWfP9c6nGWi3DdxYePvrge9WfAtd6y0lgt2OOe9iv1Rhj_VLUyOqVjaH3gx1jmwFtznh_NmTJ9Ee0rJ2SFL9hST1rUjadYFRtq1jhZg5YrDMqqpJIeugmYrgEo3wCvSNJFwV9lGrZkSrmuKQx1KS7SKBmLDDdU1WIw2kw8-cEnI6BRnlmennDN9jd0jX0-mSETXwqrhigko6uxMXkTi8N9DSC7qNBt36j2rwYjWAwJfVqAj0QVp2sMUN0mNlAXebuhldt4BtbOZIObyVZUkxKctf7fLsDVoN_3d19TVNiUfGtBbnLMQ4xYCaj4iZvCeQw7P4gmS6pBccEWLrRaZpOnraF1-5yR5A3BmdktftejVTPP11pcxEwHrChHW9EU3V_pX-H3dtNF7zGDeDLHSD7pXMe5wwmhxdpqyyJ5RaiE6Fa9LMZQ2P982gsaOA6snJq-vQI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550f13e765.mp4?token=ryEUSonkx9fMqija6oaWg0OL5Dog2uDHgbpKQALn-3ZhqYXmnpTK3j55lkbwLcvqWepYyCVD5Xyg8Hw-MxI3B4rkL9cNLLX6fVjh99bc_9kmJWHHdblN6hX0GfyG2-qiMHooVPNh5DMIulaRyBfdzd8MvjZfcmZZSqvtwYGo5_BUI_6scQikj1gsBy43VXRzehjPSKQw3Dei4Hlo7t5AwQjXg2V1s1R5LgTqpcZWfP9c6nGWi3DdxYePvrge9WfAtd6y0lgt2OOe9iv1Rhj_VLUyOqVjaH3gx1jmwFtznh_NmTJ9Ee0rJ2SFL9hST1rUjadYFRtq1jhZg5YrDMqqpJIeugmYrgEo3wCvSNJFwV9lGrZkSrmuKQx1KS7SKBmLDDdU1WIw2kw8-cEnI6BRnlmennDN9jd0jX0-mSETXwqrhigko6uxMXkTi8N9DSC7qNBt36j2rwYjWAwJfVqAj0QVp2sMUN0mNlAXebuhldt4BtbOZIObyVZUkxKctf7fLsDVoN_3d19TVNiUfGtBbnLMQ4xYCaj4iZvCeQw7P4gmS6pBccEWLrRaZpOnraF1-5yR5A3BmdktftejVTPP11pcxEwHrChHW9EU3V_pX-H3dtNF7zGDeDLHSD7pXMe5wwmhxdpqyyJ5RaiE6Fa9LMZQ2P982gsaOA6snJq-vQI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو رو دو هفته پیش گذاشته بودم.  معاون سیاسی نیروی دریایی سپاه اینجا در جمع حامیان حکومت بهشون میگه خیالتون راحت باشه، حملاتی که ‌ آمریکا انجام  میده «واکنش»  به اقدامات ماست!  «کنش» نیست!   تمام این ۴۷ سال همین بوده!  یه کاری میکنن ، تنش راه بیفته،…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6110" target="_blank">📅 00:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6109">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6109" target="_blank">📅 00:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6108">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=N_Z6bf98m2KmIIXQilModMoMbKNam8pD07rzwxtiT_F1ZCtxYn6k7rtCVo-WSJPkKIIaHiXPqODdmRYX4DA5zjQTkaeR7_FnhZfZZ0W1QIc67VjRCWiynIMtWiWMozjbLqK_2mQvxDzir2UPzdgXznLkyVmiEslh0wFhzOZFemXe90PeC_bhMTRXZER3h40wpH5E19VLRX8b3IO4_X70RIKntYlMaUrlavB4Lp8KB97jZW_l62vadKrqDCpSFhaRTSf-FKCzDs1Wk6vA7y12kpR_1fc702SHqbCItJBLy1WOLeREMSdMeOKZLv1K8tiLW3nww3GSHtqd4kJcP3dj0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=N_Z6bf98m2KmIIXQilModMoMbKNam8pD07rzwxtiT_F1ZCtxYn6k7rtCVo-WSJPkKIIaHiXPqODdmRYX4DA5zjQTkaeR7_FnhZfZZ0W1QIc67VjRCWiynIMtWiWMozjbLqK_2mQvxDzir2UPzdgXznLkyVmiEslh0wFhzOZFemXe90PeC_bhMTRXZER3h40wpH5E19VLRX8b3IO4_X70RIKntYlMaUrlavB4Lp8KB97jZW_l62vadKrqDCpSFhaRTSf-FKCzDs1Wk6vA7y12kpR_1fc702SHqbCItJBLy1WOLeREMSdMeOKZLv1K8tiLW3nww3GSHtqd4kJcP3dj0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گشت زنی اف ۱۸ آمریکایی بر فراز چابهار</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6108" target="_blank">📅 00:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6107">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا : محاصره دریایی ایران وارد فاز اجرایی شد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6107" target="_blank">📅 23:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6106">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
چندین انفجار در بندرعباس
🔺
چندین انفجار در اهواز
🔺
پنج انفجار در قشم</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6106" target="_blank">📅 22:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6105">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPeNbOGwWBIF3ACOmz9C8X7uyuFK6YrbzjbckYusUJnjObsBrrFYOVgp71IF7-S9pe9MAu8N9liMjoJpH8aOM1F72exc05GOqA8T0mnq7MzwnvEWLBJswAb9_8tD8pNqve1TBUzfd-DUXks2IupCaJjDZ2xetjUA5lfilIYLj92S_5NimFsNq2dqg6ysnzGlI4rXToRy8gD-C2MFuWL1qDVrvs1l4qhLK6eRclzA0TkCKkzCNxbbN8BDMybTz9722SLTjPXXzL0xqQNwO0xQB-t_IJZZWHaGge_67UGEiOCMgXLZK4vSKTwGuJwqubfWtqPnSsF2AM8WRE_WsY2OLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2077085449948938568?s=46</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6105" target="_blank">📅 21:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6104">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
دقایقی پیش : حمله به قشم و شنیده شدن چندین انفجار
🔺
حمله به یک نفتکش اماراتی در سواحل عمان
🔺
فعال شدن پدافند در کویت</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6104" target="_blank">📅 20:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6103">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
ترامپ به فاصله ۲۴ ساعت، از ایده گرفتن ۲۰ درصد سود از کشتی‌های عبوری از تنگه هرمز کوتاه آمد.
«به لطف نیروهای نظامی آمریکا و همه اعضای قدرتمندترین نیروی نظامی جهان ــ با فاصله‌ای بسیار زیاد نسبت به دیگران ــ تنگه هرمز برای تردد همه کشتی‌ها باز است، به‌جز کشتی‌های ایران. و این هم به خاطر رهبری دروغگو، خشونت‌طلب و شرور ایران است که این کشور را به سوی نابودی کامل سوق می‌دهد.
بنابراین، ما
یک محاصره کامل
اعمال خواهیم کرد، اما
تنها علیه کشتی‌هایی که به بنادر ایران رفت‌وآمد می‌کنند یا هرگونه محموله مرتبط با ایران حمل می‌کنند.
بر اساس گفت‌وگوهای بسیار سازنده‌ای که با رهبران خاورمیانه داشته‌ام، تصمیم گرفته‌ام
کارمزد ۲۰ درصدی بازپرداخت به ایالات متحده
را با
توافق‌های تجاری و سرمایه‌گذاری
که کشورهای مختلف حوزه خلیج فارس در آمریکا انجام خواهند داد، جایگزین کنم.
این سرمایه‌گذاری‌ها عظیم خواهند بود و در عین حال برای خود آنها و آینده‌شان نیز فوق‌العاده سودمند خواهند بود.»</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6103" target="_blank">📅 18:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6102">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGbg1n2BjZcGEbx9s1zWBMQ_u2rVck3lsZ8of-Yeg1-1oobcAKCSh1nOg71iLh5a0mgxhUGYnStxoC174lotyxjyOMT-fTYCgjYCoxMxDiCWQDXHoSWNhoZa3qk-yY0U_az_SriKXgc662na9hjk28OqGSvLxUjKbgyejc-nY7JGV0WN9TQT6fEKtplIf3uQKG3F3WBdNGcETgYc-coGnEmGmflRmLPOMGm6Z9sv7vFwLPIF-vPkbmGoLlHBx-9QuVEqSqZ9bZZj_UIIjYIYckuubBjTUsGv8u1VlkoLETKo0bo8SVcNULdJqUCDj31cr63dhPSxAm3_c_HhmtdiPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهپاد‌ها (قایق‌های تندرو بدون سرنشین) آمریکایی این مدلی به یکی از مهم‌ترین مراکز نیروی دریایی در بندرعباس نفوذ کردن و حمله کردن.  گفته می‌شود که در این حمله یک زیردریایی ج‌ا را نیز منهدم کردند.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6102" target="_blank">📅 18:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6101">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=WcMw092p-1mcg-wMIwRVMwhRjTL4YTdNUyuVNWswEY4f9INBsRv7U_x5D6fy0ZLSSDMLoZ_bV7Wv8pw-nmTovnuOKIR3lLuXQbAP7mXB3tmg0UG32ToH0uuYnTCQFkrM-KkhtTqsAfjvImYWv4yVm_MJYddUIgrhf_4qMzR9CCYy_H6YQ29S4y9XFqDoQQfFhcyKd8Dfwdd0PKhr3tZi6bpG4LOP3dTZpLWTRo610eGEWU4KpiuaT7644Gcw-IByGoMIbEQ8kdak6haeNhTmrM_nEXSYQ8giVRwGlcxDLNE2VOy8WRltKTSQVE55aJ-wuIYiTGpu-16Vrdb5T0j36g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=WcMw092p-1mcg-wMIwRVMwhRjTL4YTdNUyuVNWswEY4f9INBsRv7U_x5D6fy0ZLSSDMLoZ_bV7Wv8pw-nmTovnuOKIR3lLuXQbAP7mXB3tmg0UG32ToH0uuYnTCQFkrM-KkhtTqsAfjvImYWv4yVm_MJYddUIgrhf_4qMzR9CCYy_H6YQ29S4y9XFqDoQQfFhcyKd8Dfwdd0PKhr3tZi6bpG4LOP3dTZpLWTRo610eGEWU4KpiuaT7644Gcw-IByGoMIbEQ8kdak6haeNhTmrM_nEXSYQ8giVRwGlcxDLNE2VOy8WRltKTSQVE55aJ-wuIYiTGpu-16Vrdb5T0j36g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت جنگشون :)</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6101" target="_blank">📅 16:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6100">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfsUAZNodtj4nAeybllBHf-WZYgHiqQgLoSsLfwxRqnNyz7Cxt9XSxQ83U1KeTBtjdWOIr6j6NL8DlN2NJ8mpQo2tmgautQiDv8sub-YXaVVSY0DPy9ChPmKdbFKRtnSUXFxe38zLrCFe0_iQ-L6kXBZzCVQWCzETFh4981OMgcNWm1WprbLezhuGjwU1cqOhx0qe2rxGUwOt7Tw5FN_XP7eZsKbXsqNGAJu0YAxxKAcJr9zuc-0MpN3E3pVuZX6GCnZCzS4EUQT0y-tOsdFzywMs93GlsuQtpCYNulvYrCNq-e9ZK1r-CQ5eiTYw72GxAsu6gRLrmeRcbei7xQ6pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏آمریکا با استفاده از سه قایق بدون سرنشین (شِهپاد)، پایگاه دریایی دیروز بندرعباس را هدف قرار داد و تأسیسات نگهداری زیردریایی و کشتی را منهدم کرد.  این نخستین بار است که نیروهای آمریکایی در نبرد از قایق‌های تهاجمی بدون سرنشین استفاده میکنند.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6100" target="_blank">📅 16:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6099">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">۴۷ سال رژیم اسلامی</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6099" target="_blank">📅 15:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6098">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLWt4PV5CTD06K-tgXg2oBmAh_o2BrB55Lm-41gGR7RGyTT1Z1Dp-YMWnjyzzofNcOYkGc_moU0qWJnBHWawmlYmLqwkNyFwV9GNARwoiMDexvJZh7xzseYTqIVqsepCeOYwsUmIbvUp1_g7DYHRt7nLCow1zY5fto8JiI3sMg0eHyZa4lknxPFOlXX81giS8oSy-2nmcZJZbfyr3gMWpyzWEjDX2LT7C1HCIHCRUfFbUHPU8pGu4Ep5V4nuwYGH8I_ozM8kbk8I98e4e88Och4yJY1HDJhTtg54V7ergHv1WIWcZiTOWfkVprLrXwMq7Sfywc1rdcqSUZEEryQx9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
تخریب ساختمان مرکز آماد و پشتیبانی دریابانی نیروی انتظامی ⁧ بوشهر ⁩ در پی حملات هوایی ⁧ آمریکا ⁩ به مراکز نظامی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6098" target="_blank">📅 15:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6097">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
حمله به آبادان و ماهشهر
معاون امنیتی و انتظامی استانداری خوزستان:
🔺
امروز سه‌شنبه ۲۳ تیرماه،
در ساعت ۱۳:۲۵ نقطه‌ای در شهرستان آبادان
و در ساعت ۱۳:۳۰ نیز نقطه‌ای در حوالی ماهشهر هدف اصابت پرتابه قرار گرفت.
🔺
حادثه دوم به دو انفجار شدید منجر شده و جزئیات تکمیلی پس از ارزیابی‌های اولیه
اعلام خواهد شد.
🔺
جمهوری اسلامی در این ۴ شب و صدها مورد حملات، هرگز اعلام نکرده که چه تاسیسات
و مراکزی مورد هدف قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6097" target="_blank">📅 14:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6096">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9c510f4f.mp4?token=GkZPWgC7y1FuMj1rWXADTyI19hQCxKx0bFz7MvEtfU-8dPmALYOpTTu_z_L5it2yaaMzH-3ShSopFLGYl3hRtIUG5IPYs6SQ_BJIQXyQTwIu5a3yVDmBLjPAJX11v7HbZ3bPFBmCmvi_XUFR1v6z2YUqAKY8FfFOBuyhk2EAk4X0-d_R4NOfvGbwo67tdtjGDKtvQQ7xr3BnD15vcowZWL1bjT5phQbA6hVmDDAJmDZlt5BuOJF2VKouyiSCvOUq8YvySL2FyLfZw8TTwDBtXWgyNQTOozGvhzpFzBJqTTJR1Lv6HvLbr8AjO6o1hsj6W4YQp2jTAYNc7y6Z8conUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9c510f4f.mp4?token=GkZPWgC7y1FuMj1rWXADTyI19hQCxKx0bFz7MvEtfU-8dPmALYOpTTu_z_L5it2yaaMzH-3ShSopFLGYl3hRtIUG5IPYs6SQ_BJIQXyQTwIu5a3yVDmBLjPAJX11v7HbZ3bPFBmCmvi_XUFR1v6z2YUqAKY8FfFOBuyhk2EAk4X0-d_R4NOfvGbwo67tdtjGDKtvQQ7xr3BnD15vcowZWL1bjT5phQbA6hVmDDAJmDZlt5BuOJF2VKouyiSCvOUq8YvySL2FyLfZw8TTwDBtXWgyNQTOozGvhzpFzBJqTTJR1Lv6HvLbr8AjO6o1hsj6W4YQp2jTAYNc7y6Z8conUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌پرسه نظرتون درباره اینکه بدون هشدار قبلی برق رو قطع میکنن چیه؟
‏چمران میگه:
‏شما اگر بدونید پریروز چند نقطه برقی رو زدند دیگه این سؤالو نمی‌کردید.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6096" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6095">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PGx9eF1pkgF8uOfnJs7LH_rXT7gaH24czjZ19Pu634B9b2DJFHNjgLzPj1_y-ehxXammB4hdAnX9Aydl-YgrKlSNPLCEs0xF1sC5bmj2vx5j6U7xqw1qil1D5rXv7did8YJTe-wGp6DsbMNrsILFXBGqgCtQwBR6qW7HfFQ7OXK1NnIzhiUsSGcdqBz6FC-fw-hpxXnE1gfFWHMRfWv5o2nXyHNK2FY69Fou7oweZ-iybvP3M06bNKTzVcXCnyc5zBkZBdKJrY1WMlDd-AOFUQff0gr-x7FYxOUvFFAbjkpIy632Ful-o4sqjDoASu5NmJqVt6TN0ctecCuKdt5tqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه ترکیه، دیروز جمهوری اسلامی
رو با اسرائیل مقایسه کرد و گفت
رفتار این دو شبیه هم هستند.
(کاری ندارم که ترکیه خودش چه افتضاحیه، اما نشون از تغییر رویکرد ترکیه نسبت به ج‌ا داره)
یادمون باشه فرمان حمله اخیر از سوی ترامپ در ترکیه صادر شد! یادمون باشه معاملاتی بین ترکیه و آمریکا رخ داد، که آرزوی ۲۰ ساله دولت ترکیه بود.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6095" target="_blank">📅 14:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6094">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
حملات دقایقی پیش به بوشهر ، خورموج و….
🔺
سنتکام چند ساعت پیش گفته بود که این دور از حملاتش متوقف شده.  در اسامی شهرهایی که مورد هدف قرار گرفته بود هم مثلا نامی از کیش نبود!  مشخص نیست آیا همه این حملات را آمریکا انجام می‌دهد، یا کشورهای دیگر (مثلا عربی)…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6094" target="_blank">📅 13:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6093">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-eQyjQ9x0zqMB81nlbfnEHqozoNSn-S2--An_pJ1l9n70Hc1u71Z5yoO3AjynMZ_rl13uGb6T2NcsrNuGfMEVpVY7LZ4dQ1gnIjppymA_PdUUFwKeXC4rezoAbOVeZHSttEbfW41Smqd-Ehw5thtSYD2-_6HwhDtjaD95iyqmMwh4M4b-H6E-wWeHlvUgBddDkLoCTNV5S4jjvgmhd9nNDRBg-WPlEK4PDQ7uBRLE-kJ6VarKGQmqqsGdJYnASgMnbM1yiC1GaGafQOpQvhv15hFhmlESCE0o5tWFn3TmvGXEQOQbHFOr9rzla4HCL7p4zVVl_mOyFXlo5RmcmWqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حملات دقایقی پیش به بوشهر ، خورموج و….
🔺
سنتکام چند ساعت پیش گفته بود که این دور از حملاتش متوقف شده.
در اسامی شهرهایی که مورد هدف قرار گرفته بود هم مثلا نامی از کیش نبود!
مشخص نیست آیا همه این حملات را آمریکا انجام می‌دهد، یا کشورهای دیگر (مثلا عربی) نیز در این حملات مشارکت دارند.
🔺
دفعه قبل هم که امارات در پاسخ به هفته‌ها حملات جمهوری اسلامی به جنوب ایران حمله کرد، مقامات ج‌ا تا چندین روز نگفتند که کار امارات بود.
الان هم برخی از این حملات مثلا دیشب، با حملات دقایقی پیش مشخص نیست کار کیه.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6093" target="_blank">📅 13:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6092">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=JAk-Xvg78xIaX7PAZEaCBsdqSgOlP8z5Eo-5UXg5TGgZ0oBYOjrsRKwAbeSGqaTRlrZfrx-rHHbMWra53WpR5c2aMe-sLO9dLwlqYpJzH9WodQnf7zO7MSN1yt4tJJiLZqzKxobfR6Rq44H0qaEvXaETTitiDKUFVSNO4QIbzvjunjOuVWOintJCOa-3saomXkX51QamNeuvnmQbwGFjHp-DF5E2QGCXv-U759KdguKO4tLkfuumK22Zchx2_4u-EMR6gB_DpQVruwzKtSxYphRVkblxXnIpny2amL8YvrjX9F0JObQemwLs_2ZYrprz_vltfBYWznv2y-cuCV69MXadDER40kv7cZKg8sCU4Rx0u70Mggm6hpPE7-5xMQnc_u6IlsbInDQIOz4wfpDHCU0MTeDh1k1NP9574wNc7NG32cvTLMCgskmgdZrain5MYK0EI4GcYXsyon9S7UOXRwZZJ7TdliyEq-x4mitTH1JFymBM3utnstKomeUtV7D-ahEYddO7iZpjr4YvZtiWJ1Ngal16WSQdwRt1PcgFav_zrDvva8OBqkj3SA487VyLixrLKMWPGeF1icEu1yI4TpcFgDYeFlS3kkydUQMDcE6fxy4guEkikBChNX1c-F14H7WVv3h7PgDcHbWNwOldSygRD8b7CMxh2cIV2YwXZTM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=JAk-Xvg78xIaX7PAZEaCBsdqSgOlP8z5Eo-5UXg5TGgZ0oBYOjrsRKwAbeSGqaTRlrZfrx-rHHbMWra53WpR5c2aMe-sLO9dLwlqYpJzH9WodQnf7zO7MSN1yt4tJJiLZqzKxobfR6Rq44H0qaEvXaETTitiDKUFVSNO4QIbzvjunjOuVWOintJCOa-3saomXkX51QamNeuvnmQbwGFjHp-DF5E2QGCXv-U759KdguKO4tLkfuumK22Zchx2_4u-EMR6gB_DpQVruwzKtSxYphRVkblxXnIpny2amL8YvrjX9F0JObQemwLs_2ZYrprz_vltfBYWznv2y-cuCV69MXadDER40kv7cZKg8sCU4Rx0u70Mggm6hpPE7-5xMQnc_u6IlsbInDQIOz4wfpDHCU0MTeDh1k1NP9574wNc7NG32cvTLMCgskmgdZrain5MYK0EI4GcYXsyon9S7UOXRwZZJ7TdliyEq-x4mitTH1JFymBM3utnstKomeUtV7D-ahEYddO7iZpjr4YvZtiWJ1Ngal16WSQdwRt1PcgFav_zrDvva8OBqkj3SA487VyLixrLKMWPGeF1icEu1yI4TpcFgDYeFlS3kkydUQMDcE6fxy4guEkikBChNX1c-F14H7WVv3h7PgDcHbWNwOldSygRD8b7CMxh2cIV2YwXZTM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجتبی خامنه‌ای «علی الاصول»
با تفاهم‌ مخالف بود!
و نوه خمینی هم این چند روز گرد و خاک به پا کرد و گفت هویت ما در مبارزه با آمریکاست!
اون‌هایی هم که نگران زیرساخت‌ها بودن
الان سکوت کردن  و صداشون در نمیاد!
آغاز دوران «علی الاصولی» !</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6092" target="_blank">📅 09:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6091">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سنتکام ساعتی پیش
از پایان این مرحله از حملات خود خبر داد و نوشت :
🔺
جدیدترین موج حملات خود علیه ایران را به پایان رساندیم
🔺
در این عملیات پنج ساعته، به اهداف نظامی در بوشهر، چابهار، جاسک، کنارک، ابوموسی و بندرعباس حمله کردیم
🔺
سیستم‌های دفاع ساحلی و موشکی، سامانه‌های پهپادی و ظرفیت‌های دریایی ایران، هدف قرار گرفت.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6091" target="_blank">📅 09:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6090">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkiJnjI3dfibXRwDk5bSFVDEreHejkziVABGjgc5YGMgy4ZFFogo8T1zRq5G8GSd8oWSElQzoHSswAR9xyYG-lkvj70V5JPCnJAUi4EbTxBwPlSZLWqhD8BPD_jxUiStoWdv-THg0hxVIO5Y0L2OSBn1GBrcfLVLELP5fSSzphMrrUkBZ2tYfdQRJumKn6W6fLyMoq5af-3L7YgRRgpMe1HfBSdt0D9GyjRblC-PqPfI--us5DpFsMyIiPiBPEARbfuR_HzQRW1TS-dg0lleRuztFqGTFfu03Syg5fLE94k-CYY6lDLpOQeit-qarG6UL5hY9e2rKFHwl-c6fndEkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شب گذشته سپاه به دو سوپرنفتکش (در سواحل عمان) حمله کرد.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6090" target="_blank">📅 09:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6089">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/671b861555.mp4?token=CVIZ63WcdvE-sYBzn69AukNp9rOTN1aCaBxr8TCixnGydLF7EXbIpqnbxGpy0xPO1Sa7jk5kotdvJbErVRwjvYg45Rk4qovDi9DMj1Wi1S4ePV73II36LXl-03gEwP1NVeWVIc59rwaf81IwtCH-PStvwO-1ZNDz3wJEYM1PvtkV8WW_d6Y1ZYKN8PvRB0VQDZxE2j_6dqj79_DzgoMmobQ3OshIgcrScryZVZ1FKDbFEhctuKWQw3dJJiODn_sh3jskpoPLZSMemURCTKloqsY-IvxpsB0kRKbSYxP4zGEzjVwb8Us1rQuEQCanRHXC7_7MyYz1LJt-vYG0ebXcV58C9Q7U17PQMM7IF4lrozxRzd3znaPjE1yYZPVaCz1td6Omc_2bc2kMXp9p1oBGPoDIxpr4y7-Ej7FdAJuxa69xOSyHVPrpUmar0922cxI6rvwLiQSI0PGYRoonVI6WKjp-5Jn7VB0eaubSwrBxbx9o9BTNzReWMRU9s1vkBB569mtZpVil8PjNEAkOi2ToRchyi6nhQ2d76hZmQ9KRsf8Pte276m-OREi6DGd-VtiCzcSa0apAPRgbZK1ew8BmHW8YTQ9j6AQvvhMYAZNi5U89Tj13Yzpjq-FovHBpmakHTkda40Wt7E1Enqf6xr_MhHBh1K08rIf3X_pE2gJih7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/671b861555.mp4?token=CVIZ63WcdvE-sYBzn69AukNp9rOTN1aCaBxr8TCixnGydLF7EXbIpqnbxGpy0xPO1Sa7jk5kotdvJbErVRwjvYg45Rk4qovDi9DMj1Wi1S4ePV73II36LXl-03gEwP1NVeWVIc59rwaf81IwtCH-PStvwO-1ZNDz3wJEYM1PvtkV8WW_d6Y1ZYKN8PvRB0VQDZxE2j_6dqj79_DzgoMmobQ3OshIgcrScryZVZ1FKDbFEhctuKWQw3dJJiODn_sh3jskpoPLZSMemURCTKloqsY-IvxpsB0kRKbSYxP4zGEzjVwb8Us1rQuEQCanRHXC7_7MyYz1LJt-vYG0ebXcV58C9Q7U17PQMM7IF4lrozxRzd3znaPjE1yYZPVaCz1td6Omc_2bc2kMXp9p1oBGPoDIxpr4y7-Ej7FdAJuxa69xOSyHVPrpUmar0922cxI6rvwLiQSI0PGYRoonVI6WKjp-5Jn7VB0eaubSwrBxbx9o9BTNzReWMRU9s1vkBB569mtZpVil8PjNEAkOi2ToRchyi6nhQ2d76hZmQ9KRsf8Pte276m-OREi6DGd-VtiCzcSa0apAPRgbZK1ew8BmHW8YTQ9j6AQvvhMYAZNi5U89Tj13Yzpjq-FovHBpmakHTkda40Wt7E1Enqf6xr_MhHBh1K08rIf3X_pE2gJih7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: بیشتر موشک‌هاشون رو از کار انداختیم، بیشتر پهپادهاشون رو.
🔺
توان ساخت پهپادشون رو حدود ۹۲ درصد از بین بردیم. توان ساخت موشکشون رو ۸۹ درصد نابود کردیم.
🔺
یه کم توان براشون مونده، اما برای ما هیچ توانی ندارن. این دیگه تقریباً یه درگیری نظامی کوچیکه</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6089" target="_blank">📅 08:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6088">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3962370842.mp4?token=N330EugaVhbKCsPAvUGGtadwTBUVgJuEW7gNuu2yybE8IwJQB4DwHz-5IbJhbXv9TwHwjuYHxTcSA5EMMyDcF2cgoGsB4P_J7LxetWAwKTdhUmau6vlvcMaZIid1ouTPAUDzrdJgV7EgIO0KDRaDB7jHF93y5nZEmR3ywjdpoZAwF8tQfVXeyKIN7Kmvwy9hlF4PsSmtOPs46udiJGd236LQaj_DJCDirS3C6Se1GYhv-5cHyTso5T-T58wCVccXIPECKxTYHt7BygL1fGneIE-gTAcmZbTCylXTwU0GWIb637__Xm_ljkiusz8D2xKkCcG1xGFhv3PpXGAeMWbMzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3962370842.mp4?token=N330EugaVhbKCsPAvUGGtadwTBUVgJuEW7gNuu2yybE8IwJQB4DwHz-5IbJhbXv9TwHwjuYHxTcSA5EMMyDcF2cgoGsB4P_J7LxetWAwKTdhUmau6vlvcMaZIid1ouTPAUDzrdJgV7EgIO0KDRaDB7jHF93y5nZEmR3ywjdpoZAwF8tQfVXeyKIN7Kmvwy9hlF4PsSmtOPs46udiJGd236LQaj_DJCDirS3C6Se1GYhv-5cHyTso5T-T58wCVccXIPECKxTYHt7BygL1fGneIE-gTAcmZbTCylXTwU0GWIb637__Xm_ljkiusz8D2xKkCcG1xGFhv3PpXGAeMWbMzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات شدید به کنارک - امشب</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6088" target="_blank">📅 01:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6087">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
ترامپ : حملات جدید می‌تواند برای دو یا سه هفته ادامه یابد.
🔺
سنتکام : موج جدیدی از حملات را برای سومین شب پیاپی آغاز کردیم.
🔺
باشگاه خبرنگاران : ۷ انفجار بزرگ‌ در بندرعباس</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6087" target="_blank">📅 00:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6086">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
شنیده شدن ۳ انفجار شدید در جزیره کیش
🚨
انفجارهای شدید در جم - بوشهر
🚨
چند انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6086" target="_blank">📅 00:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6085">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
ترامپ : امشب و فرداشب با قدرت به ایران حمله خواهیم کرد.
تفاهم‌نامه آزمونی بود که جمهوری اسلامی به آن پایبند نماند.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6085" target="_blank">📅 23:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6084">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">آمریکا سفارت خود در ابوظبی و کنسولگری‌اش در دبی را به دلیل نگرانی‌های امنیتی، تعطیل کرد.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6084" target="_blank">📅 23:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6083">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mD0ZgGRXAghL2CIkNMRugyjd5QAmuHu3prNAgvdSnHpA4S6lpfWwtNUKTqjp-_43I1XWgR6AS802fz44XQtu-jdPYvLZQ4g2HkrfaSECaBNsjbuCLuBnPp0VdHaEXacXe3guMvhPdpHWdvemwBNTRmrWmTbBqqVRsJVuTPgqSa0JouJu32_tRQMACBr-c1aeJH3fDLY5VvBH6lMmZOxR3dXqkIz-kNCuMMaKbKYDojZQZhzrD3t8FK3xYmXXINPOrwlgrLgMsjC_6uA_-6qDXGEyLdvGe6_dm71rpbjx6UVOGhZsj_Y-w_y8bwacX83VBLpBz4ypBFmjGkAEvo-WuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
انفجار در چابهار و کنارک</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6083" target="_blank">📅 22:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6082">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/645219e055.mp4?token=ewBe-QRAQe0eTRSDgAIGqK-BcMtX1UvG37U731btkuZdsV-jsb7u_mZNHrWLZTbIsVLf45Xw00emPBIpv2ehpcQWOfKF8uQZqZUmiOyA2fANnfI5ux0pZqmmTfUzPi7wcr8t_1RQadoZrTRwlvOfV1GBT80f7l_ekkWdBwkA3vaD3P0VC6Dts9P5Lou2Y5v7DrfM95Ilvhe1w596dgWV3z3Bb8ZVTuW9E_K0TCN7iTgxRxCAaF65ganRpN0ln_ZrBv6WTJXCU_KMuHWzstpYfwcj1eJ9lUz87bOZVeGc6pGY5mWBuZDRVu5PDu0KQaSYXxZmna44VBupAOCktjlXbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/645219e055.mp4?token=ewBe-QRAQe0eTRSDgAIGqK-BcMtX1UvG37U731btkuZdsV-jsb7u_mZNHrWLZTbIsVLf45Xw00emPBIpv2ehpcQWOfKF8uQZqZUmiOyA2fANnfI5ux0pZqmmTfUzPi7wcr8t_1RQadoZrTRwlvOfV1GBT80f7l_ekkWdBwkA3vaD3P0VC6Dts9P5Lou2Y5v7DrfM95Ilvhe1w596dgWV3z3Bb8ZVTuW9E_K0TCN7iTgxRxCAaF65ganRpN0ln_ZrBv6WTJXCU_KMuHWzstpYfwcj1eJ9lUz87bOZVeGc6pGY5mWBuZDRVu5PDu0KQaSYXxZmna44VBupAOCktjlXbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏آمریکا با استفاده از سه قایق بدون سرنشین (شِهپاد)، پایگاه دریایی دیروز بندرعباس را هدف قرار داد و تأسیسات نگهداری زیردریایی و کشتی را منهدم کرد.
این نخستین بار است که نیروهای آمریکایی در نبرد از قایق‌های تهاجمی بدون سرنشین استفاده میکنند.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6082" target="_blank">📅 22:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6081">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‏
🚨
🚨
محاصره دریایی ایران از فرداشب ساعت ۲۳:۳۰ دقیقه اعمال خواهد شد.
‏بر طبق قوانین اعمال یک محدودیت تازه دریایی باید ۲۴ ساعت قبل از اجرا، به صاحبان کشتی‌ها اعلام شود.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6081" target="_blank">📅 21:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6080">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be724e9f8e.mp4?token=gburE4zl4KslX-tZ4jUrprFKasqwSL4UwO0OI_NeDqBc6tmFmDFZBygqJPGjx654fT3oi9ahVWs2HWL9QjDOcOapfHts1qXmpGOzfMMTliXrkBYcKZnj4yVfc4JTr1RTLSapupdLetsnBUYNbIKFFEgBWOeQlRNwfGsvHDKxca3ebuwz_iHwgsrvjrIpi-23Y6k1aDV2HE1NGeXUaCb1X8n7XuUZ6ggbujtAenm5KKQl3mvUK-7vcE4cNWCa2NARFP2HbLS_E76s6MtHFwlBpfCkZaIC_Xj7eLCTw3a4Re7Dig5WHu4l4NQEYlqIGG_HeM1cLKHubXycmw0KUw18eQkSsI-91Xrn67PdNUXwYmJYhcJd3zTqgXasUGdWOTXiA-YO9kMw-4vEHRa2vi_YNX98iuhmWaXSOrLeOMl-Sz_GltTPyB1GBQPcixRsV2MEnP-bnjo9W9eEAzobqbTeC0wvcuc4K8TjZ3-yhuPxgbAJ8M8YWWArjdoF2cg21vQ8aA_zUlVE2lFxh8asRtQnMi0X0HhUP4GLRV-vi0NDH09J8f1ye0vuSmeHYYzHe5M572RMyEt_vVcGWEMNjuwrfjR7-1RWzTDaTOqPb-zJ3NqInwxlpvu2V3hXqWzGb9jlP831agv8l71-2jvzFCo7tNrcCWOaQ9WlE9ufLrkfJDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be724e9f8e.mp4?token=gburE4zl4KslX-tZ4jUrprFKasqwSL4UwO0OI_NeDqBc6tmFmDFZBygqJPGjx654fT3oi9ahVWs2HWL9QjDOcOapfHts1qXmpGOzfMMTliXrkBYcKZnj4yVfc4JTr1RTLSapupdLetsnBUYNbIKFFEgBWOeQlRNwfGsvHDKxca3ebuwz_iHwgsrvjrIpi-23Y6k1aDV2HE1NGeXUaCb1X8n7XuUZ6ggbujtAenm5KKQl3mvUK-7vcE4cNWCa2NARFP2HbLS_E76s6MtHFwlBpfCkZaIC_Xj7eLCTw3a4Re7Dig5WHu4l4NQEYlqIGG_HeM1cLKHubXycmw0KUw18eQkSsI-91Xrn67PdNUXwYmJYhcJd3zTqgXasUGdWOTXiA-YO9kMw-4vEHRa2vi_YNX98iuhmWaXSOrLeOMl-Sz_GltTPyB1GBQPcixRsV2MEnP-bnjo9W9eEAzobqbTeC0wvcuc4K8TjZ3-yhuPxgbAJ8M8YWWArjdoF2cg21vQ8aA_zUlVE2lFxh8asRtQnMi0X0HhUP4GLRV-vi0NDH09J8f1ye0vuSmeHYYzHe5M572RMyEt_vVcGWEMNjuwrfjR7-1RWzTDaTOqPb-zJ3NqInwxlpvu2V3hXqWzGb9jlP831agv8l71-2jvzFCo7tNrcCWOaQ9WlE9ufLrkfJDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی جدید قرارگاه مرکزی خاتم
در خصوص تنگه هرمز
ویدئو رو باز کنید و به چشمهاش نگاه کنید :)
یک دقیقه و پنجاه ثانیه پلک نمیزنه
ابراهیم ذوالفقاری محصول هوش مصنوعی :)
یک انسان عادی، هر ۳-۴  ثانیه یکبار پلک میزند، در یک دقیقه ۱۵ تا ۲۰ بار</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6080" target="_blank">📅 20:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6079">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcJHIZm49MB44_JL-WZEjAX9VQ0Oe1tjiVYfzQMm8-B57nWSb4oEFaSVfm4nMQ3kVWTzPzngv8tKoDwkZxNwVI4mkWkzcAqLYswL9hrwOlkZr09_XAJZY56XtuQPQ4jBQ3ucDunG7FXWK4ZLHyJ8Fmfbtr-u1uOsPyNBVDuKvRuxjKEDqsXy6ZV6gh2XqGwIdGOGRwaikd0IX7emziEOco5aAzHbr9ei1MJy191WXwj4_Hiupq-bXQSQrizC6qNHDggVf7mzlfYrmP5QGqCQ1hCPqt0cRXvpU-QiT0Be8UJcwDj-t2ef3ABhBX5qPWKcaFVheG3YO9bFK45VruqbjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : از این لحظه به بعد، ایالات متحدهٔ آمریکا با عنوان «
نگهبان تنگه هرمز
»  شناخته خواهد شد.
اما در این جایگاه و به اقتضای انصاف، برای جبران همهٔ هزینه‌های لازم جهت تأمین ایمنی و امنیت این بخش بسیار پرتنش جهان،
۲۰ درصد از ارزش تمام محموله‌ها
ی عبوری را به عنوان هزینه دریافت خواهد کرد.
روند اجرای این طرح و شکل‌گیری سازوکار آن بلافاصله آغاز خواهد شد.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6079" target="_blank">📅 17:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6078">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMAR_JRdUydzfxg-p4q8Cv6A8Xunb-JMzxuVEA4OBN4jmULJ8MnHS2D4BjmtahnPPhdtUCCB4Y4jie-HYaF2ETh368kC2kNV3iS4RoO1jZR2EY8g8KHDO69-xlbIeeUJBHu1sXYawAuFW_QmIhLTL6IXtgRbbhDsfa2IqvkuIwQnb1C-N-ndsybMtcR4Qt29kM23s7SGV4EOrC-4eGHJCpcwiQzE4i_9_JJFV_sNM56_emMuauuwV_f5EDhpYMI9b0d8FwlTfkJLXhey6ruDml180PuoCJBUZExWv4fzjjrS9eX6ZiVM9D0mMQcso15V87zdDdWJ597lpqznG_Yi-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6078" target="_blank">📅 17:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6077">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFHka0rrt_NPLNim7Sq-GSNko7L2a5Vzv2K2Gfy-_M0MdjjOqpvYuKnfeRaVPIgyHy1nd1jCBbgpzEnm4hiCQllwldCE3_bV_ixyjDnhXH91GK9ulVaH_WF4efR_ur2k_iI3U7TdwQEJG5O2iXqS54zbd1WIdCX3nH87jms4kZKl7X7zsHCX3-xCDv4t94OK5DIYzzuftRQxHZzLGdehZieoE08QexdcKa_PYxEz12LSyPthdnB8hscgGLNYobYSzFaPMUJcbeSom8unZCXIfbqTI5fGnERlngEO3Mfy6e0N-k9qRomO59diq9XFD-vx7xr3no1i9lFR2A2uUEXGyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6077" target="_blank">📅 16:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6076">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترامپ درباره ایران:
‏ما کنترل این تنگه را در دست خواهیم گرفت. احتمالاً مدیریت آن را نیز بر عهده خواهیم داشت.
‏ما به نگهبان تنگه تبدیل خواهیم شد و وقتی این کار را انجام دهیم، هزینه آن به ما پرداخت خواهد شد.
‏ما ۵۰ سال از این تنگه محافظت کردیم و هرگز پولی بابت آن دریافت نکردیم. بدون هیچ دستمزدی از آن محافظت کردیم، اما حالا از این کار درآمد کسب خواهیم کرد.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6076" target="_blank">📅 16:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6075">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
دولت بریتانیا سپاه پاسداران را به عنوان یک
سازمان تروریستی
اعلام کرد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6075" target="_blank">📅 15:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6074">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">عربستان برای مراسم ابراهیم رئیسی «وزیر خارجه»‌اش رو فرستاد! برای مراسم خود خامنه‌ای، ولی امر مسلمین، این بار «معاون وزیر خارجه» فرستاد :)</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6074" target="_blank">📅 13:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6073">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYYvKC8kCZMy3QpRQ_5rKolYWCk2zRXdZKwPTt1PFW8QPhvLEQvx2i-559-vVYD9kQT-ibORjFZXICZzoC9t2JM8C6-cv2hfKzTbLIAvCkChgTNA1tK99N-7nmAvNVyrD4aMvv86lEwD9tgVeSAF1SNSfMgDdIBCCNv6hVa-1eCuntMP_1K3l4sKaGxPTlIc4uSAvQe3tigL0QwwDpo0qNnqVUB2lIDrXm5uF8v42GJlEZ3dZYlhT5sZgcpELGUGVJlymVQ4fHfIOjNRqkYeqjfltgzE3OaB533pU4N5rA7YZ2l0rfkVNuV1PcSxvB3jpLS5x478oS0BiY6emf7DQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای مراسم «ابراهیم رئیسی»  شخص امیر قطر به تهران رفت،  همراه با نخست وزیر قطر و وزیر خارجه  قطر،  اما برای خامنه‌ای،  سطح هئیت قطری به رئیس مجلس  تنزل پیدا کرد! قطر اهمیت کمتری برای مراسم شخص خامنه‌ای شد! از اثرات حملات جمهوری اسلامی به قطر!
🔺
این مدل احترامی…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6073" target="_blank">📅 13:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6072">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTQH2l5LoNtbZq2XdtMgOQkN2w5rv9UFY1P_KxXwaPSJTyC9szrF0oSzGM2wbfoqTwxAqA3LFsaiY7Ta6HVQmZQtkVNIDE5G72SFR5vqUPX2quHDevaS8j_OWrdhDew2dcAOvPZ4wMtheT-Dv49jyvl3JnIpv61PoUeOhxFgE8k1EB6Ur4JHNlf950s0VEw-w0kwsxQDr2jLCP2dZPCvIeKpfF0pMMVU9iDTaN_G7X0nKvFjsbCWIF5ij1-jqgwp6ddgM8xw2FPeXov8XXpg7iKb5oR5TBn4AnjWpIlKERWnTm_1aMSN2q8YtaOctPsBr2rUGT7t-QuJAUVgtSnAMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای مراسم «ابراهیم رئیسی»
شخص امیر قطر به تهران رفت،
همراه با نخست وزیر قطر و وزیر خارجه  قطر،
اما برای خامنه‌ای،
سطح هئیت قطری به رئیس مجلس
تنزل پیدا کرد! قطر اهمیت کمتری برای مراسم
شخص خامنه‌ای شد!
از اثرات حملات جمهوری اسلامی به قطر!
🔺
این مدل احترامی که قطر برای
خامنه‌ای و رئیسی قائل شد،
خودش به تنهایی یک توهین به خامنه‌ای بود!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6072" target="_blank">📅 13:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6071">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SkgrbQLJB3W3pmBFHugVmdY4vGQCQ_hKETTu_90BC9oPPhCc97VNdaAWY-j1w99eExz6szu30qBLG6sUz42YLIdHfiLiMKraGdx2u5nN_X947A5sBrguKKlGrNLoIMxjnwZDbva4z36qkcXRM-gbtkOCiGWyh9h8lT-rwNUNSdbRFyhYziyUL9H6g9wvyrvA_Y6LCwYtih5PnhKVwTqQvuc4W63SAGlH1Z8CJO7igTj3rJslM4Aerf2-ALkB7qb8lcyu4vWEkIMbKEuSUu0B9SN2e3gmVDc8ut6M0dLXaexfUp8vmOu8lSVr7N3IWlJM3VDkqCzhJKcP8ZDMY-tXHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مناطقی که در دو روز گذشته
توسط جمهوری اسلامی مورد هدف قرار گرفته.
عمان، قطر، بحرین، کویت و اردن.
عمانی‌ها از حملات جمهوری اسلامی
بسیار خشمگین هستند.
عمان همواره یکی از دوستان ج‌ا در منطقه بوده  اما حملات مداوم ج‌ا
به این کشور باعث شده تا سران این کشور از ج‌ا خشمگین شوند.
🔺
بعد از اینکه در آخرین روزهای جنگ ۴۰ روزه نیروی هوایی امارات دست به عملیاتی در جنوب ایران زد، ج‌ا کمتر به امارات حمله میکند.
🔺
عربستان هم در میانه جنگ ۱۲ روزه به طور رسمی و جدی به ج‌ا هشدار داد که دست به حمله متقابل می‌کند و ج‌ا نیز رویکرد خود را تغییر داد
.
🔺
ج‌ا در هفته‌های اخیر بر بحرین و کویت  و بعضا قطر و عمان تمرکز کرده.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6071" target="_blank">📅 13:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6070">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/868ebce267.mp4?token=u5aU0GtxZcBrMIzyb3xri1dW3ZpO8EiS0xbW591L7EKOMieO_YJOJUAeJPgFnjQy5jojYvmCYElb0apvqUf6UMd36JEP0XD_Q1oF2JHA215a9T4NJ8ftwqVJCjlWJUoKd4XGRXcpdbDqCznski98s8DScFwUZK6uH0zh5X9KKOdqaVDxMfx2mJPpvYo4CFIh-kKCCDCXhnkRFxR6Uxc7TbPhOPOF8g0ZzPU9gD45MuRdSXFKV4X_F6LY9PJ4yg0yew2m3wIIM5B-zIr5WWrfKYN39i0KcETDKo755b5HUAvPR_Ncj7bgVJfR4P70q-LgfsHaL9VSs0l5i9HUCFK5qlQnXVvDq3avoCN4NItimyJueiHB-rutJsjBOuvLDXhoVCmHHrw4eVHgMVT9dLVJw5ZcljS1g-l2_ntzaKtkT346pBFUJNm1OLt3PjuIVKFoNIWYWPU7_rPocgLInj45bXIyRq_0nUj0w0Yr_EwP4hZrFIb-YqpwX9DrRJW_dszzR7T3pRoL7ckkePOjZFfgndRDUOu-07tI_6l0RviWa06VaZMPNzV0YsFcMAIEYAun0FM3m0x3SXPaO9WRfOBT-sif2kmLWUeE3fSi0whoPQlwI8X5XWUNZgpW5Cljs4VQEPgQW2SA1t0Shp4etaWjoihzN2yFTsM5Rp2MhYOnfBE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/868ebce267.mp4?token=u5aU0GtxZcBrMIzyb3xri1dW3ZpO8EiS0xbW591L7EKOMieO_YJOJUAeJPgFnjQy5jojYvmCYElb0apvqUf6UMd36JEP0XD_Q1oF2JHA215a9T4NJ8ftwqVJCjlWJUoKd4XGRXcpdbDqCznski98s8DScFwUZK6uH0zh5X9KKOdqaVDxMfx2mJPpvYo4CFIh-kKCCDCXhnkRFxR6Uxc7TbPhOPOF8g0ZzPU9gD45MuRdSXFKV4X_F6LY9PJ4yg0yew2m3wIIM5B-zIr5WWrfKYN39i0KcETDKo755b5HUAvPR_Ncj7bgVJfR4P70q-LgfsHaL9VSs0l5i9HUCFK5qlQnXVvDq3avoCN4NItimyJueiHB-rutJsjBOuvLDXhoVCmHHrw4eVHgMVT9dLVJw5ZcljS1g-l2_ntzaKtkT346pBFUJNm1OLt3PjuIVKFoNIWYWPU7_rPocgLInj45bXIyRq_0nUj0w0Yr_EwP4hZrFIb-YqpwX9DrRJW_dszzR7T3pRoL7ckkePOjZFfgndRDUOu-07tI_6l0RviWa06VaZMPNzV0YsFcMAIEYAun0FM3m0x3SXPaO9WRfOBT-sif2kmLWUeE3fSi0whoPQlwI8X5XWUNZgpW5Cljs4VQEPgQW2SA1t0Shp4etaWjoihzN2yFTsM5Rp2MhYOnfBE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانال ۱۴ اسرائیل با انتشار این ویدئو خبر داده که ارتش آمریکا شب گذشته با بمب‌های سنگرشکن به یک ‌انبار موشکی در اطراف پایگاه چهارم شکاری در دزفول حمله کرده است.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6070" target="_blank">📅 08:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6069">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f4228d97a.mp4?token=GhMNrqNaaZo5edczPy2ZIMgpjon6c5RbJ5K1JO8A2SgwK0Y134KihC48IcTKY1Na6HnlKbZlMzP4J4Ix30zYK1fHLw7KFwIGAkvTY7CI6A3vTYGwgXklMmT5ViWJFTV-862gP9pNH_sgpC5DnApZ1G2iktHH2xyle9JMp8eZofw0wedUma5ls54yawrdzN1mQSED6PRHdO4xxSZEj-1AMTnlbegKZS3jalTSRYzttW3Z5TNXDW1dN0l46oK-2eN3dkqCssif-HdpXyYlLZ5CQN9F14KD2Fo3iu1OKQ8Kd75cnJb4JbIwbEXTSPsCUVJF8U0U8qxfbpjSXY4bmf56pqmzo9morwH_3FmX6BX22frUt_jMZ0BkVYpxnPRIEXtdRyyrSU6fD9MWHIqssQk5Z7iLBWt1fMFmxomUhofKFwvItsnKIWg1qZJipuyQDKXHFyS7ae2sHSVVIfY6SjK9jyWiP9IyAEQr8ARHTvlFW-RUBR4PqGvDdpOlnVhqqfXOR3mSx_GJ8z_Sz7Fh96i3f1o2ZKZPhPjWuz1nvfbgDrRAgHkfzlgOS5FEB7ydsplrb0eZkbxHd62JgX6s1pPxa2ygt_EryfFX2SV_rsE6NWiodMBiMSCxT0CHxfYzr3gg-cPVeY-L6hACiWHc8SO8NhF6auCuXoeCBGvBqM4bRfE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f4228d97a.mp4?token=GhMNrqNaaZo5edczPy2ZIMgpjon6c5RbJ5K1JO8A2SgwK0Y134KihC48IcTKY1Na6HnlKbZlMzP4J4Ix30zYK1fHLw7KFwIGAkvTY7CI6A3vTYGwgXklMmT5ViWJFTV-862gP9pNH_sgpC5DnApZ1G2iktHH2xyle9JMp8eZofw0wedUma5ls54yawrdzN1mQSED6PRHdO4xxSZEj-1AMTnlbegKZS3jalTSRYzttW3Z5TNXDW1dN0l46oK-2eN3dkqCssif-HdpXyYlLZ5CQN9F14KD2Fo3iu1OKQ8Kd75cnJb4JbIwbEXTSPsCUVJF8U0U8qxfbpjSXY4bmf56pqmzo9morwH_3FmX6BX22frUt_jMZ0BkVYpxnPRIEXtdRyyrSU6fD9MWHIqssQk5Z7iLBWt1fMFmxomUhofKFwvItsnKIWg1qZJipuyQDKXHFyS7ae2sHSVVIfY6SjK9jyWiP9IyAEQr8ARHTvlFW-RUBR4PqGvDdpOlnVhqqfXOR3mSx_GJ8z_Sz7Fh96i3f1o2ZKZPhPjWuz1nvfbgDrRAgHkfzlgOS5FEB7ydsplrb0eZkbxHd62JgX6s1pPxa2ygt_EryfFX2SV_rsE6NWiodMBiMSCxT0CHxfYzr3gg-cPVeY-L6hACiWHc8SO8NhF6auCuXoeCBGvBqM4bRfE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ارتش آمریکا شب گذشته به ۹ شهر
در استان خوزستان حمله کرد : اهواز، آبادان، ماهشهر، بهبهان، شادگان، دزفول (پایگاه چهارم شکاری)، امیدیه (پایگاه پنجم شکاری) اندیمشک و خرمشهر
🚨
بندرعباس، قشم، جاسک و سیرک
در خط ساحلی و «خنداب» در استان مرکزی نیز شب گذشته مورد حمله قرار گرفتند.
🚨
جمهوری اسلامی نیز به اردن،
کویت و بحرین حمله کرد.
🔺
ویدئو : ارتش آمریکا این ویدئو
را از حملات دیشب خود منتشر کرد.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6069" target="_blank">📅 08:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6068">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
صدای انفجار در بندرعباس،
سیریک، جاسک، قشم،
سنتکام : از ساعت ۱۷ به وقت نیویورک
(از ۲۵ دقیقه پیش) حملاتی را شروع کرده‌ایم.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6068" target="_blank">📅 00:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6067">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=QQGl8i-hioAcfOk4JUspYsqdOUfRAyNZi5X_8XFjLlltqLACxDuNzEHZ3pQq5Nd652TE-kzDU9P-lXDZfIlLDvzGz7ASj4ygCldSXQ78WottB9as4px8fzKCckLYrcdRDW-zFmr_jvPCZJ9bwJxPa0ShYs4X7fxBaO2Cx0iP7n5yUwZpcpN30MMyt5DWiPWs8PhQVr3XHZqy6u-GniDO0eLUKluCNhrGQGGoI4_PVJa2TefMlSYZRXFqFoRLGjLv-W8twhMZWxSghSRopXZ1TAIiWEslTgt6sd4v-8sKTwNk4kVjnsvQ1Ifc9AFHyh-LVnp3twWumSuHlUhTFaYu7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=QQGl8i-hioAcfOk4JUspYsqdOUfRAyNZi5X_8XFjLlltqLACxDuNzEHZ3pQq5Nd652TE-kzDU9P-lXDZfIlLDvzGz7ASj4ygCldSXQ78WottB9as4px8fzKCckLYrcdRDW-zFmr_jvPCZJ9bwJxPa0ShYs4X7fxBaO2Cx0iP7n5yUwZpcpN30MMyt5DWiPWs8PhQVr3XHZqy6u-GniDO0eLUKluCNhrGQGGoI4_PVJa2TefMlSYZRXFqFoRLGjLv-W8twhMZWxSghSRopXZ1TAIiWEslTgt6sd4v-8sKTwNk4kVjnsvQ1Ifc9AFHyh-LVnp3twWumSuHlUhTFaYu7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات موشکی سپاه به کویت</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6067" target="_blank">📅 20:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6066">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">فرماندار قشم از اصابت ۱۰ تا ۱۱ پرتابه از عصر امروز یکشنبه دشمن در جزیره قشم خبر داد.
حسین امیر تیموری افزود: تمامی اهداف نظامی بوده است. خوشبختانه این حملات هیچ تلفاتی نداشته است.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6066" target="_blank">📅 19:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6065">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=BzEIibiyL6NokzZzBaVa2RQFJDRQyCC39mAMV7o9Oc3RvX885cpXRtBL0CAKfpYTa7dNuGoN0X-x2odNjCjjJWHDkv_gDymQuWZf3GCWt2y6d5cHFSSkSPingqThjjoJuho7B5n1U_JWjXHHBLVFjLR-R50_OwQNirW6TB0b3tHPGwOs-HimczpePbvMckckPcTAsaeSsAaE-PBnZR3pObKiPm7LfANJIXaIsExF6aKCBsxqYczSf0Apw2uBtbGDmE1JTBPDFlkGUC0XQCjH40Hiftdbpkmw6dF0rH2J8R-rp5ophKlQDmrS3BmqGUN9ABMLtJkXgQYdjw-21hOhgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=BzEIibiyL6NokzZzBaVa2RQFJDRQyCC39mAMV7o9Oc3RvX885cpXRtBL0CAKfpYTa7dNuGoN0X-x2odNjCjjJWHDkv_gDymQuWZf3GCWt2y6d5cHFSSkSPingqThjjoJuho7B5n1U_JWjXHHBLVFjLR-R50_OwQNirW6TB0b3tHPGwOs-HimczpePbvMckckPcTAsaeSsAaE-PBnZR3pObKiPm7LfANJIXaIsExF6aKCBsxqYczSf0Apw2uBtbGDmE1JTBPDFlkGUC0XQCjH40Hiftdbpkmw6dF0rH2J8R-rp5ophKlQDmrS3BmqGUN9ABMLtJkXgQYdjw-21hOhgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که این ‌تصاویر از نتایج‌ حمله امروز آمریکا به جزیره قشم است.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6065" target="_blank">📅 19:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6064">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
آغاز دور تازه حملات آمریکا
به شهرهای ساحلی جنوب ایران.
بندر عباس و قشم مورد هدف قرار گرفتند.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6064" target="_blank">📅 19:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6063">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">دوستان عزیز
این رسانه کوچک به‌صورت مستقل اداره می‌شه و در ۹ ماه اخیر، به خاطر شرایط خاصی که در اون هستیم، همه زمانم رو گذاشتم روی فعالیت شبکه‌های اجتماعی.
اگر این محتوا برای شما ارزشمنده و اگر مایل به حمایت از ادامه این فعالیت هستید،
این لینک پی‌پال در دسترس شما :
PayPal link :
https://www.paypal.me/Farahmandalipour</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6063" target="_blank">📅 18:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6062">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4bc671310.mp4?token=t27fZgrbgpwG62NF333_1q4vCGHCjDXZZfaa2mI4lJZj1PnWRwzDkFE16OyqOpYkCKXw5grqdFGEaNAp43yQoq_w9I_UPF0qQ_wYQJFhd61X_A_yAGVx777cp3zVwrkb_NAYeedx6QKZK99IPYfR2bfrfo8FQ0eh08GJFKyYHcBjMb1qIR-M3sWQGnF0cQnFmFIfALhxJhPPZ1zwfw_faBuJg9EHct6yemXU1lzcJ8pKwZWDc4Cy5HZC4uuZiR9rrM-kV49m10IerJyEAnRFn8zL8Dm4K73aE6ELRh9Q4YUqjgpMALZyjAlxz9ZpsXEKtxn6KtyLdKLNK5Y4tGcjAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4bc671310.mp4?token=t27fZgrbgpwG62NF333_1q4vCGHCjDXZZfaa2mI4lJZj1PnWRwzDkFE16OyqOpYkCKXw5grqdFGEaNAp43yQoq_w9I_UPF0qQ_wYQJFhd61X_A_yAGVx777cp3zVwrkb_NAYeedx6QKZK99IPYfR2bfrfo8FQ0eh08GJFKyYHcBjMb1qIR-M3sWQGnF0cQnFmFIfALhxJhPPZ1zwfw_faBuJg9EHct6yemXU1lzcJ8pKwZWDc4Cy5HZC4uuZiR9rrM-kV49m10IerJyEAnRFn8zL8Dm4K73aE6ELRh9Q4YUqjgpMALZyjAlxz9ZpsXEKtxn6KtyLdKLNK5Y4tGcjAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مثل باباش شجاعه :)  باباش هم در جریان جنگ ۱۲ روزه چند هفته رفت «کمین‌گاه»! برنامه‌های شبهای محرم رو هم نبود تا شب عاشورا (دو هفته پس از پایان جنگ!)  که دیگه در جنگ ۴۰ روزه غافلگیرش کردن</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6062" target="_blank">📅 17:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6061">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a80edc91f4.mp4?token=Xj9HkqzfdtAUJtyAcainZ5rhPZ5AWODVYa63iLq4UVIEYNQspO7yOayxJGkKfGEAZDPxw2RX2ZyfM0J_FkAXp7p8GMnpcCFBTebcB3Wzm6q39Pe94a7ltJAfdVJonDBZcFOSXMlinltE88cqEQ8BvfX4zlkXZQ8sqQJe_p5KBG8z6TKw8VhE7kyYqcJjVmZ7tY0kuvoRGQw2cgjjwulQG-syzyl_ZtWWam-uUfP1ohrBWh-ptEvXQxFLJCZycqSrScuCvR6JxSUFys2E_Mg5cL--fvgXbTTlKtP9ga202kcaAed_XkMDkUFLdwRtbgQyaeVOPYriiqy4TX1on27Rng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a80edc91f4.mp4?token=Xj9HkqzfdtAUJtyAcainZ5rhPZ5AWODVYa63iLq4UVIEYNQspO7yOayxJGkKfGEAZDPxw2RX2ZyfM0J_FkAXp7p8GMnpcCFBTebcB3Wzm6q39Pe94a7ltJAfdVJonDBZcFOSXMlinltE88cqEQ8BvfX4zlkXZQ8sqQJe_p5KBG8z6TKw8VhE7kyYqcJjVmZ7tY0kuvoRGQw2cgjjwulQG-syzyl_ZtWWam-uUfP1ohrBWh-ptEvXQxFLJCZycqSrScuCvR6JxSUFys2E_Mg5cL--fvgXbTTlKtP9ga202kcaAed_XkMDkUFLdwRtbgQyaeVOPYriiqy4TX1on27Rng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا بگذار مجتبی از «کمین‌گاه»  بیاد بیرون، پوستش نور آفتاب رو ببینه، شما هم به جای هوش مصنوعی، قیافه خودش رو ببینید، ببینید اصلا چه شکلیه، بعد به نتانیاهو بگو بترس.  راستی گفتید مجتبی دقیقا از ترس کی  ۴ ماهه قایم شده؟</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6061" target="_blank">📅 17:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6060">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcBkSKQl2Nb5SvDndTHtN95uro8pv14Xrop2zUj56hRwcEIs7C5hGz79x-5fQ_lANftDwt7xRAje0No6m5FUf8bPO5xSym8FxnopVPZBXFOsfiUuPXBAddYh-OOOKKLMWiXMrGUSHKMjNRLc9LMiyoI6YfmF_liF0DXcDcsJsSrQ3IIpJgmaDJH5IU6dC-U4Smt1lOEA1V2YK89y_jK3u_L88D5p0phWZ43huDMx04cgrr2CnYqoSEDEJZUDCQVgSdQGdQAJpJen-hUAR9misyqG46QN5YBXc72Z9_zdEueRkrGTtKqZZM97XV_YDd9JmBXsseelxT7VG-z0QGGOdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا بگذار مجتبی از «کمین‌گاه»
بیاد بیرون، پوستش نور آفتاب رو ببینه،
شما هم به جای هوش مصنوعی،
قیافه خودش رو ببینید،
ببینید اصلا چه شکلیه،
بعد به نتانیاهو بگو بترس.
راستی گفتید مجتبی دقیقا از ترس کی
۴ ماهه قایم شده؟</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6060" target="_blank">📅 17:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6059">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vk9IokQIosan0h28-T3BfFZEYvV5gVtglH6jKDA40ptzsH8DJLMZ_45cmdcGnAhMeCHSUcdnd83N4d30iZ56DCgwnP_KU3I1pUA3Rxz0N8V4YKAF1eA9hEsG7oMuknwF3UsHz1qENk3VspChp8q0V4Cei8ivVc7ymtjDADiqJ5-SmIMfpF1eIbFNc3tCyDWblMRyhM_3WOwJvZABvAwhSjklH7CR6ofdxYbTuIlO_5RKgnF_ejIuCFCHFX-gbNemPx0jrkjylXmHO22PC0yWl1geqUIqiaHsodZWoEEBlZTjym6VwQRZ64eJq6d9jwUS23wOr-gaslKbKDrXBVmwJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشهد  از فردا : روزانه ۲ ساعت خاموشی برای منطقه.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6059" target="_blank">📅 16:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6058">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec46cc2c8f.mp4?token=F-IemB4DNUrLs6QE4ceuyU8VPWlm-6-czvYzAyYnqTX_zR9eFMvIQjaYGvhVhMgHYnRkqV3x1vXtNNfKRdxyJ6GtHRwiYgEQI77_DidLgSdln7NwB1OwVwH_kyqsc32qb4gOBhPhgjGXTyHsV43yr6qp4FOhNGpcbtybli_wVV6uDJ4OqDQipihRwfZSA2QaVZpt5o1ThYga6DLCqnfmYhku1EHJl3Layj-L1fE4rOnOVdnvaUoVcOsE3egvdlsql-Fn2l-0CmMn0yd_n3W3_eLv0Nqn5x9U5vRs6xKIJsVmz-n-L_iFIJy7Fx4CWrw36IbOYoN7Azey6UBRxz7FJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec46cc2c8f.mp4?token=F-IemB4DNUrLs6QE4ceuyU8VPWlm-6-czvYzAyYnqTX_zR9eFMvIQjaYGvhVhMgHYnRkqV3x1vXtNNfKRdxyJ6GtHRwiYgEQI77_DidLgSdln7NwB1OwVwH_kyqsc32qb4gOBhPhgjGXTyHsV43yr6qp4FOhNGpcbtybli_wVV6uDJ4OqDQipihRwfZSA2QaVZpt5o1ThYga6DLCqnfmYhku1EHJl3Layj-L1fE4rOnOVdnvaUoVcOsE3egvdlsql-Fn2l-0CmMn0yd_n3W3_eLv0Nqn5x9U5vRs6xKIJsVmz-n-L_iFIJy7Fx4CWrw36IbOYoN7Azey6UBRxz7FJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوینده شبکه خبر جدی جدی
خبر درگذشت لیندسی‌ گراهام رو دوبار خوند :)
فکر کن تاثیر یک سناتور آمریکایی رو
در برابر کل نهاد مجلس خودشون که ۴ ماهه
کلا تعطیله و کسی هم اهمیت نمیده :)</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6058" target="_blank">📅 16:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6057">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNnTZwsJgYnmHvluxxWDjW6Gw-vL-3DerxyfdVFOfHimGysBcYXAsnHExb9cwEL7yUecQ5JEeKHcNlndmoMk4lzYIsC1CqZI97aaOUWf26ljMrvseZ0TbeTQFr9EEgOXGEx21A7UNeJcv03HxGxfMsltYv0npDzl4Sx5Uosw2wYCklGBBbMeq6H8P5rAuuZ--W1ane9OKcs3MJr-Xb1AW1ZmwF8w6Xz4FBgLvDAstj18bsGeAaCtAPf4AIv4fTdDFIpO11i_ZKyYG5y-8no2Jubt-7OgzB9bl88Z7BC6sVNkmigejdfXqg618s4eriX5ZIqE9NkHFTdeZbU3k_DJVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی این لیست عاقبت و نحوه کشته شدن چهره‌های اصلی که در کربلا نقش داشتن رو نوشته،
خیلی جالبه، چون نحوه کشته شدن اونها تفاوت زیادی با نحوه کشته شدن افراد در کربلا، یا ائمه و… نداشته!
یا با تیر کشته شدن،
یا سرشون از تن جدا شده،
یا تشنه بودن و کشته شدن!
مثلا این رو نوشتن که ببینید عاقبت اونها چی شد!
هیچی! همون عاقبتی شد که مثلا نصیب بزرگان اسلام و شیعه شد!
مثلا یاسر و سمیه چه مدلی کشته شدن؟ به مدل کشته شدن سمیه هم میگید عاقبت بد برای کسانی که مسلمان شدن؟؟
در مورد یزید نوشتن در حال رقص افتاد  مغزش متلاشی شد :)) از روی پشت بام‌ افتاد؟ روی پشت‌بام می‌رقصید؟
بسیاری از تاریخ نویسان مهم و اصلی از جمله «طبری» و «ابن خلدون» نوشتن مرد! نه در حال رقص و نه متلاشی شدن مغز!
عرزشی عقل نداره! با عقل دشمنی داره!</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6057" target="_blank">📅 13:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6056">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">رقص بر‌ روی ناقوس یک کلیسای قدیمی - توسکانی - ایتالیا</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6056" target="_blank">📅 13:16 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
