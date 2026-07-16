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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 12:08:39</div>
<hr>

<div class="tg-post" id="msg-6155">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Riol4wSvSsZ_4jpoqTaWzKjCqDe0J-Bo4G3BciOG0tl2HwJP8UlzFohqSIxvOsR4jmyClWMfr3COK--VLWcJR3i_BRrb87uRAytQJhO4MPZmo1GzqFRZ_6aBsEekQb6G5WKNAyLO55uvx7kGmR6SYykyzgMN4NajDSEyQJJjjyDuAt_GWDJjkzwNwnl2jNsOua9zohT03Cd5gMz8x8bw1joVO8MINIGeUNQ0uCqR_qzdeVqS17v8X4viO8_jBOifggeyUnkWjUOuGsht2B8L-YwNihxbhWzT1pfUnKFUoEkagIWMlo6EAqieaeVkWaU-KG0GI4g2PWTbX-NULLsANA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وراجی نکنید  بگذارید بجنگند که صلح بیارن :)  مثل صلحی که ۴۷ ساله در لبنان  ‌ و غزه آوردن!  انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/farahmand_alipour/6155" target="_blank">📅 12:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6154">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">وراجی نکنید
بگذارید بجنگند که صلح بیارن :)
مثل صلحی که ۴۷ ساله در لبنان
‌ و غزه آوردن!
انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/farahmand_alipour/6154" target="_blank">📅 11:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6152">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=B6l6tcnpcRSRD8hFnPU3zmK-6zSqcTSGbXMVzoJDsVEDoiYqb2-DEAj1PT8uHradLneRzGbBn65HVXtDnT2oiTFMrJ8ZerKtHvWGKj6OKspECzgt3AgpBCPTHlTCjINp-ZtU_SbYEkm0DefKAxp0-gPqprzHNcgw8xfjcO5nm-v9WObvs5qzu_Q4yWaoXClQZa3M4ug881VcdgdmHljFUFDIYMIi1zQrEnp9E9NM-IsX7U_N-GvkiZ3dmvkliTGE271GicLpkHOQ6jklsCoSfA8JAs-RKrRX32ZhQLAyDzOUzFyNucQs4WWVTHyfnOlwkxQtDIBbQDPjVTZybcw4lCAEej1yRzAS0zy7zy8CCBQhNWNXIY9bk5R3gqVpzktsUJ7hSlv1ccjv_-oM7E0bH6Pj9vQhQ4aHlOQHFHYWo815qx7DsefdKX3glTCn8jy-2ex8d4vHe0o6l0V8F9H6Bt-6zeQ-LJuvWD-y3rWYJ7U8-8351Gml-Krr6ntPimOXN4dVE7u6dSwiMIEvOEZbFfxMYy3Q-xQ6Q8Ef3ZtnSTh-P6dFZXSW7-EHkp5qJZ0ezxm8Z3LraNPQ5IN-IwKfNu_f4oVKeHPaxn5dhf1mnVxM9O3Yn3lPMfhC_-jaI2ygs3pidr5DPzWWldp3llYtnbA2QPhvNVeytqSPHGYKjcU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=B6l6tcnpcRSRD8hFnPU3zmK-6zSqcTSGbXMVzoJDsVEDoiYqb2-DEAj1PT8uHradLneRzGbBn65HVXtDnT2oiTFMrJ8ZerKtHvWGKj6OKspECzgt3AgpBCPTHlTCjINp-ZtU_SbYEkm0DefKAxp0-gPqprzHNcgw8xfjcO5nm-v9WObvs5qzu_Q4yWaoXClQZa3M4ug881VcdgdmHljFUFDIYMIi1zQrEnp9E9NM-IsX7U_N-GvkiZ3dmvkliTGE271GicLpkHOQ6jklsCoSfA8JAs-RKrRX32ZhQLAyDzOUzFyNucQs4WWVTHyfnOlwkxQtDIBbQDPjVTZybcw4lCAEej1yRzAS0zy7zy8CCBQhNWNXIY9bk5R3gqVpzktsUJ7hSlv1ccjv_-oM7E0bH6Pj9vQhQ4aHlOQHFHYWo815qx7DsefdKX3glTCn8jy-2ex8d4vHe0o6l0V8F9H6Bt-6zeQ-LJuvWD-y3rWYJ7U8-8351Gml-Krr6ntPimOXN4dVE7u6dSwiMIEvOEZbFfxMYy3Q-xQ6Q8Ef3ZtnSTh-P6dFZXSW7-EHkp5qJZ0ezxm8Z3LraNPQ5IN-IwKfNu_f4oVKeHPaxn5dhf1mnVxM9O3Yn3lPMfhC_-jaI2ygs3pidr5DPzWWldp3llYtnbA2QPhvNVeytqSPHGYKjcU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها اگر نوحه میخونن و مداحی و رجز خوانی و.. برای کودکان غزه و لبنان و میناب و….. از تاسف از دست رفتن زندگی نیست! میخوان در این جنگ بی‌‌‌‌پایانی که با جهان دارند،  از جمله و در صدر این‌جنگها،  با خود مردم ایران جنگ دارند، سربازگیری کنند! تا نیروهاشون بزرگ‌تر…</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/farahmand_alipour/6152" target="_blank">📅 11:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6151">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">تمدن اسلامی! تا زمانی که توی مدینه و مگه بود قادر به ساخت «توالت» هم نبود!  مستراح هم نداشتن !! اما دنیا در چه وضعی بود؟  ۶۰۰ سال قبل از تولد اسلام!  توی بیشتر شهرهای جهان  داشتن توالت عمومی! اجباری بود!   اینها میشینن روی منبر  میگن «مدینه فاضله»!!  حالا…</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farahmand_alipour/6151" target="_blank">📅 10:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6150">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">تمدن مصر باستان رو مطالعه کنید ابتدا تا انتهاش بر مدار مرگ بود! فرعون از زمانی که سر کار می‌ا‌ومد به فکر مقدمات مرگش بود و قبرش بود!  هنر و پزشکی و علم و مهندسی مصر همه بر پایه صنعت مرگ بود!  مومیایی و اهرام و جراحی پزشکی و….. همه برای کار و کسب مرگ بود و…</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farahmand_alipour/6150" target="_blank">📅 10:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6149">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bInibF3peiLlxkW8UF3xqJyasj6hZbHKQ5_zaIodU6-wu95PjUz-ARmzyErw6NSUfWQi-L4gSj8U-x4xR3DFD0O-inPbsvgzJNJ-Tk-cWUh6fFHVK6v_K6n0ZyoCLaeaugSindc8RGDAkIOqohSUzQwk1MMXwMC30t2rUAUnjcq5Xado7XHAU0cipNgjXQzEoCJZJ-hhsCWpy57tYR-g8YO1hrYNMQEnsGQFGsIuMpes7DcsSFsYHa1tSctbeagFAmKrPTyqsKLK3bFbkA1VqzUTrBcV4pzLpX3p1UlNuDbBbwQN-QsDwRmJY5vqcop-O6bcZqNb8QgNvnCva65LHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها شنیدید جملاتی با این مفهوم رو که زندگی و این حیات «زندان مومنه»!  آرزوی اینها مرگه! مرگ براشون رهایی است!  اینکه برن و برسن به بهشت و به زندگی!!  مرگ رو آرمان خودشون می‌دونن و زندگی و زیبایی‌هاش  رو پست و حقیر معرفی میکنن!  و اینکه باید دائم به فکر مرگ…</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farahmand_alipour/6149" target="_blank">📅 10:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6148">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اینها اگه می‌بینید برای مدرسه میناب و…..  سر و صدا میکنن، فکر نکنید به این خاطره که «اصل زندگی»  رو دوست دارند. و از مرگ متاثر میشن!  تمام هستی اینها :  مبارزه، جنگ، کشتن،  کشته شدن و….. است!  زندگی براشون چیزی نیست جز  «مبارزه  برای عقیده».  و خوشحال میشن…</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farahmand_alipour/6148" target="_blank">📅 10:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6147">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/farahmand_alipour/6147" target="_blank">📅 10:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6146">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S67FAPbGcSIj2mIMHB3rweXRNd9SeixdnSv8uvrcwW8nnvOtbl0mhQ95jnqSUYbjvGfmho4R6Ei5xQ40o39fj6JfxvGefHFtdDyo6aRh04UmLkVAAsInsKYlzqmuJQs-18faNQ3hC2c7FxONqK1LlxGO-S1wt1buPHFkbTI0qzrEdES4bLTCIb1DLuPjKH07FY6wjWt8Eij3kbViicG7zHZ9WI0tf7C-ipY4FwP2EijBmkd7tORJMqhhusXvszV6kuPkLvoCs7cJuq5qjLeuY_2tMU-eNnXll7N5m2QAlPS0koNASticS7RQENihNJiJvW3sqJXqvNtUahktGgzXuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ایران به یک شهروند زن آمریکایی که در دسامبر ۲۰۲۴ در دوران رئیس‌جمهوری جو بایدنِ خواب‌آلود به‌ناحق بازداشت شده بود، اجازه خروج از کشور داده است. او اکنون در سلامت کامل در خارج از ایران است. ایالات متحده آمریکا از این ژست حسن‌نیت ایران قدردانی می‌کند.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farahmand_alipour/6146" target="_blank">📅 09:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6145">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farahmand_alipour/6145" target="_blank">📅 09:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6144">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">استاندار مرکزی : شب گذشته به دو نظقه در اطراف شهر خنداب حمله شد.
این برای چندمین بار است که اطراف شهر خنداب مورد حمله قرار می‌گیرد.
نه آمریکا دقیقا مشخص میکند چه اهدافی را زده و نه ج‌ا می‌گوید به کجاهاش خورده.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6144" target="_blank">📅 08:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6143">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اطلاعیه  ارتش:  سامانه‌های راداری، سامانه پدافندی پاتریوت و مخازن سوخت آمریکا در پایگاه علی‌السالم کویت را هدف قرار دادیم.
‏ رادار‌های سوپر هاوک، تأسیسات و سامانه‌های پاتریوت واشنگتن در پایگاه شیخ عیسی بحرین نیز طی حملاتی، آسیب‌های جدی دید.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6143" target="_blank">📅 08:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6142">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
استاندار سمنان : به بخش‌هایی از فرودگاه سمنان حمله شده، کسی کشته یا زخمی نشده.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/6142" target="_blank">📅 08:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6141">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAn2Rhw6MG6nUjkdmcJSlFMjL-HZVXD_LhnzWuhO6nAT7foyaLOQhDi7Fpk3aDpNU_YRpLkVFdOM2d2AQUnLueSAd28tre0PkbGARbX6AbalhclNxd9blwOmYQPwBfOE8eHEUtslFt_JkQuKPSxFKih_wrX-reObp9UPdFTCZxQBizFwDmJs1ZccE0-wh-ZItW4uMHGXMFV8VTxh00qbSs6y6G58R2DF51lOtxcxWXH7VNkJ-6BYxkMSbs_VWmyQ4CfdDkbXQlK-Qrch_3Pjc9ox2-uy9k8D7ht7_ySacrDYQvwv6aUddBJx7z8GXAHo7RPrvowI3N-LssBt5r__Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین یارو خودش از دست سپاه و نهادهای زیر نظر خامنه‌ای  فرار کرده و به آمریکا پناه برده!
و آمریکا رو خونه امنی پیدا کرد برای زندگی و نوشتن از اینکه اسلام چقدر زیباست و خوبه و سعادت انسان رو میخواد!
حالا از همونجا به ج‌ا میگه مبارزه کن با آمریکا! مطلقا تسلیم نشید! تا انتهاش برید!</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6141" target="_blank">📅 08:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6140">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">برخی گزارش‌ها از تداوم حملات به اهواز خبر می‌دهند و اینکه تاکنون ‌۹  انفجار  مهیب در شهر شنیده شده.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6140" target="_blank">📅 23:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6139">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
چندین انفجار مهیب در چابهار و بندرعباس
🚨
کویت : امروز ۲۱ پهپاد و ۴ موشک شلیک شده از سوی ج‌ا را منهدم کردیم.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6139" target="_blank">📅 22:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6138">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای ۲ یا ۳ انفجار در اهواز</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6138" target="_blank">📅 22:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6137">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1IRIhMok3xsIlQAiQSYxJYWubrCgyya2gHbNsRAwnnq3-wKqo-DcDjeQHNEzHNtTB89jeCvWltrb61PK1cr95znfSRukDWNlcOmx0HjxL24aqcfS-D5vx1ZEIFj0UO_RIafa9x1z8G6WSiQzsHPyK2MHBWoXNrEhKVzIgigaeCaNTHHoD5xADbRbJP-V6QNhQgLNuxK9aS_vETJ5ckRT6CLLJQP6ZkIM4eAT8ofx3AKPHeaVY5ZwBgJ3MZoXzZU_-nRTpq0rglt1dFNonbmk4kAszGpcrqSTDaEQ2QB1AKOmjH4EPGSPZxVHkVgNJVFIXfsHlJy7faUnONVhsb7Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شما دیگه جرات حمله به اسرائیل
رو ندارید! خودتون هم خوب می‌دونید!
این ۴-۵ روز هم به همه جا حمله کردید
به جز به اون کشوری که بیت‌رهبری
رو زد نابود کرد!
و نشون داد دقیقا کجاست که سست‌تر از لانه عنکبوته!
ولی هر چقدر دوست دارید شعار بدید!
اون حزب‌الله تروریست هم رفت انتقام بگیره  هنوز و همین امروز هم نیم میلیون نفرشون  توی محله‌های مسیحی و سنی لبنان آواره شدن!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6137" target="_blank">📅 20:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6136">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">آنچه شب گذشته در بمپور رخ داد و موجب  کشته شدن تعدادی ای نیروهای ارتشی شد، قابل اجتناب بود.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6136" target="_blank">📅 20:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6135">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e615d142.mp4?token=t5bsUkX-IeEFYc-YKvCCy9f2SEvxB9RMzrzuXUzsgFJo_X3TvvVdU9_i4Kmr0TL7gbXqYJHZFHsKFSjbACt-GTX4vTZ_xQOu-faBmsWhgDXiJXVN_K0CxXG0FZZuDvQ0HlVLduZu_zrQsR-p5baxal3lcxAAwITMkPqWuact3TIUcoUxxou2Iw1H2HxWuBwv2e0dHhLtV7G9zTwCOwq5dyFdK-6whBnTGJ1igqyoSrW3D7QMPoUaRlT_K4Hgqo64oUqNjeMkJ0h6taCVlzEiiEt1VQgRATitKGCDmbktw96wL2nYE_zeo2r6mnZyXva8Ijdt8oKUnU9ixnWxjnO7dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e615d142.mp4?token=t5bsUkX-IeEFYc-YKvCCy9f2SEvxB9RMzrzuXUzsgFJo_X3TvvVdU9_i4Kmr0TL7gbXqYJHZFHsKFSjbACt-GTX4vTZ_xQOu-faBmsWhgDXiJXVN_K0CxXG0FZZuDvQ0HlVLduZu_zrQsR-p5baxal3lcxAAwITMkPqWuact3TIUcoUxxou2Iw1H2HxWuBwv2e0dHhLtV7G9zTwCOwq5dyFdK-6whBnTGJ1igqyoSrW3D7QMPoUaRlT_K4Hgqo64oUqNjeMkJ0h6taCVlzEiiEt1VQgRATitKGCDmbktw96wL2nYE_zeo2r6mnZyXva8Ijdt8oKUnU9ixnWxjnO7dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیش بینی تاریخی بختیار
در دو کلمه، برای مردم ایران</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6135" target="_blank">📅 20:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6134">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=KI23fjmS7QC8Q0wwOq0U6hHbxdtEx9bJKH_PRSWrpoprjeXqQm0vPcC4NwskZyavc-W8oHvAveBx0rbUYjbfX1AOSJ3fofdkqe_TpFgg1LxmFEgIC8QF00rz6SD26f5nlQqiBd8O9pb0FXvSKnmMOVmzX_rsuL-VdieY7LCy2Sthncmu88krStuvdUf_ds0Uq_CQM3TUxf_lKxAEjYJPe_5dBfcRnDwiWbGYTn3UduIoGsxIIqqYc4r07cPTyUjzYc3fwVEALVe24eZJ_oqEga2y9U4iG9C9fAP-wvVZ3WiTNQBQszSSfqF8T-aK_sFnxLucVXeVhFgbLUYphnLRHIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=KI23fjmS7QC8Q0wwOq0U6hHbxdtEx9bJKH_PRSWrpoprjeXqQm0vPcC4NwskZyavc-W8oHvAveBx0rbUYjbfX1AOSJ3fofdkqe_TpFgg1LxmFEgIC8QF00rz6SD26f5nlQqiBd8O9pb0FXvSKnmMOVmzX_rsuL-VdieY7LCy2Sthncmu88krStuvdUf_ds0Uq_CQM3TUxf_lKxAEjYJPe_5dBfcRnDwiWbGYTn3UduIoGsxIIqqYc4r07cPTyUjzYc3fwVEALVe24eZJ_oqEga2y9U4iG9C9fAP-wvVZ3WiTNQBQszSSfqF8T-aK_sFnxLucVXeVhFgbLUYphnLRHIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی که فرمانده سپاه بود و سالها فرماندهی جنگ رو بر عهده داشت
اینجا میگه مطئنم که مسیری که در ذهن مجتبی خامنه‌ای است، بهتر از مسیری بود که شورای عالی امنیت ملی رفت.
مجری ازش می‌پرسه خب اون چه مسیری بود؟
میگه : نمی‌دونم ! نمی‌تونم که ذهن خوانی‌ کنم!
فقط می‌دونه خوب بود :) یه مشت چاپلوس !</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6134" target="_blank">📅 16:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6133">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid Online وحید آنلاین</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMaQb5iODscw4fSyTOQdYljwmSq8rOB0_KAkwAchCMUFELaKeu4sj2KIXvJBFcRO4jNO8nUz3mTxGuIRtlxHW2iNPPHzcvK5NbahsSBhiEj-Vv0PpUhQEmmun5EvhkG76A_N5A-qWRedbWmSkO1N6MDiboi6lwv7pphKVxaReHNnkeVF7yle3iDu4P1Pzt01ET7NdRk1nEBY6F8695jmJPeqtIzVZmRpw1Mvs-BzCpTgFU4S1cTykIkmkdFole4o7Wnwfa4tk0AQ0ve4V-Ov72-_Qhxzhi6J_F1Ww6Idb_8mOPZhI8RUrOBih_R3kbWvs1PVp74zumT2Yfh4MaHGRg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6133" target="_blank">📅 15:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6132">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
سنتکام : به تنب بزرگ حمله کردیم.
در جریان این موج ۹۰ دقیقه‌ای از حملات، با استفاده از مهمات هدایت‌شونده دقیق، سامانه‌های دفاع ساحلی و محل‌های ذخیره‌سازی و پرتاب موشک‌های کروز در جزیره تنب بزرگ را مورد حمله قرار داد.
این حملات توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را بیش از پیش تضعیف کرد.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6132" target="_blank">📅 15:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6131">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">حمله امروز به چابهار</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6131" target="_blank">📅 14:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6130">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
ارتش: «آمریکا بامداد امروز با شلیک ۱۳ فروند موشک، آسایشگاه و محل اسکان یکی از پادگان‌های نیروی زمینی ارتش در بمپور را هدف قرار داد
دشمن به مهمانسرا و اماکن نگهبانی پادگان حمله کرد
‏ ۷ تن از کارکنان پایور و وظیفه تیپ ۳۸۸ ایرانشهر شهید و تعدادی مجروح شدند.»
‏</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6130" target="_blank">📅 14:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6129">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
سنتکام : از نیم ساعت پیش موج تازه‌ای از حملات را آغاز کرده‌ایم.
(از  ساعت ۱۳:۳۰ تهران)</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6129" target="_blank">📅 14:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6128">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnSmheFDJTx0kMzq4DLuHgKUzCcq4Qpz8ReitGtk-V0hV0FGDE0r1QnAa7Rjls8zZFghg-DzBV1Reo2mMScEd7EuaDDKnQhUrM5gdqKuC2rigR3XDBBsl22ok757rU9u2feyJ8q-nVeV04nw48aZv9Ud0_k8T4EtytXDWYeUe8I834ciWvQDUGKHkuTj1mNP_Yx_QvBL86aKceZbCQUUH47rxc7nVAtOOB8PdAf2rwdZo5my3SjZjnFBCGXXM2vKiziMjaTh_LDd7wcCXjZlI8jaohQuEMWso_1OU-SzQSb_A4YzM2B2Wri0TyrzYPntIae2HEHF4F6k42n_ERw2xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابل توجه ساختاری‌های محترم
مدیر حوزه‌های علمیه با بیان اینکه مسئولان باید تفاهم‌نامه‌ها را پایان‌یافته تلقی کنند، از دولت و شورای عالی امنیت ملی خواست به دلیل بدعهدی طرف مقابل، مسیر مذاکرات را متوقف کنند.
مشکلات اقتصادی یا ترس از آسیب به زیرساخت‌ها نباید موجب واهمه مسئولان و رویگردانی از مسیر «جهاد و استقامت» شود.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6128" target="_blank">📅 13:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6127">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=kEt8RmuGtJ0P5FciAi-0I8Lb2TWSaLJsahDDN4fzV4V-qbj0rN0uxkjT-pF-RY7FAMRe8GbAQWvRejb-9VWiwk0pqyjuAJnuv0a7XuAjg3G-PEYgQI8xL1yKifSOx88663cPk6bufH7DDJCA694lrOhAC_gWSyGxPUduVzMQD6mR6CjVomEvUbDjNiqa4L_tzNN6bzfPegyjEUjrkoHVx9apuglFvCs6X-X093uiu1hXT0TupX7JCJ_euu59mobiL4C6fRblTgHA1hxAsd96-1-r4jEmQK5D8C0hmQGdnidLfR4RyGXwpV7zJOUUdsP1Y5v5lWY7HKPSw2TqANF57p-BK5ifWnXABIhj9SmBnmrEE-ee1JmH7gG0c900RoQYfdQtNN2QSrSeo_W94J40CsFLAP3gyltWhRCxGBDLOmrdPSrf92f6eyve8bCVl_tQJZjhkvG2huDM4TVEyIGls3X5yp8xGXGqcOHFMSlyW5RoagGqReeM8927msonwgBx3wvgNv87OUXj4N8PIKov9sxPTifj5n8vvMK6tW1ys21rqvFZHHgJK64tkVPPOXmyXPNjwWV3OJoLzEdFpHFySycaOYZnMUtlppdp6089eDg_SHlD79B38_HBlG-7WoAqURWJcbXRNHP7KZ-XH4CLOiKDeg4GW3wF-4vfYUOIXsU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=kEt8RmuGtJ0P5FciAi-0I8Lb2TWSaLJsahDDN4fzV4V-qbj0rN0uxkjT-pF-RY7FAMRe8GbAQWvRejb-9VWiwk0pqyjuAJnuv0a7XuAjg3G-PEYgQI8xL1yKifSOx88663cPk6bufH7DDJCA694lrOhAC_gWSyGxPUduVzMQD6mR6CjVomEvUbDjNiqa4L_tzNN6bzfPegyjEUjrkoHVx9apuglFvCs6X-X093uiu1hXT0TupX7JCJ_euu59mobiL4C6fRblTgHA1hxAsd96-1-r4jEmQK5D8C0hmQGdnidLfR4RyGXwpV7zJOUUdsP1Y5v5lWY7HKPSw2TqANF57p-BK5ifWnXABIhj9SmBnmrEE-ee1JmH7gG0c900RoQYfdQtNN2QSrSeo_W94J40CsFLAP3gyltWhRCxGBDLOmrdPSrf92f6eyve8bCVl_tQJZjhkvG2huDM4TVEyIGls3X5yp8xGXGqcOHFMSlyW5RoagGqReeM8927msonwgBx3wvgNv87OUXj4N8PIKov9sxPTifj5n8vvMK6tW1ys21rqvFZHHgJK64tkVPPOXmyXPNjwWV3OJoLzEdFpHFySycaOYZnMUtlppdp6089eDg_SHlD79B38_HBlG-7WoAqURWJcbXRNHP7KZ-XH4CLOiKDeg4GW3wF-4vfYUOIXsU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سفیر اسبق جمهوری اسلامی در روسیه: مطمئن باشید اگر ترامپ را بکشیم نه تنها هیچ موشکی به سمت ما شلیک نخواهد شد، بلکه عقلای آمریکا با خوشحالی جنگ را تمام خواهند کرد.
کشتن ترامپ هیچ هزینه‌ای برای ما ندارد و با کشتن او جنگ هم تمام خواهد شد.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6127" target="_blank">📅 11:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6126">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟  به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6126" target="_blank">📅 08:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6125">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIuJph274fFrq4j5e9y7gPp0PZnz45MDdFQdq-RW4wpK_SzA1BgU7OTH2FH_GZ9fpnusocOaRYpHc2HSC4Fzxi1isaRJwQdbCGuR58b-MFHNj5oSE3LQjTZR1Ak8CWauyV5vaALWfFdTM6F_0iI-C_u67Y7waI_gRvrErs8CzbwHPPC0qxXbodEIjf43P-kq9LscqV33AUKW4q9-Ma-sud4PyoghAhEDaodd4rW78192Mswiuv0re3WUKURLYcUZx-UiD5KQj27YPIDI--jdbGRL7FL9bgrPtEkkkDr8BhhSEahsImYe2LUTkJRa4HBmvGVb1SreOg438KqPjGQIhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟
به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت کاخ سفید برگزار کرد.
به گفته سه منبع آگاه، در ابن جلسه که ارشد‌ترین مقامات نظامی و امنیتی آمریکا در آن حضور داشتند در خصوص گسترش حملات صحبت شد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6125" target="_blank">📅 08:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6124">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=aEExiIsY1Ihv4h6-lLp_NksQyzRwuebf0RxZZeY7VF55zRnbG4ljpTAC6qZM91O5-sitamGjC1EdCo9JWgcQzsLuRgeoiE0TtAkQPWsR-htVP4qeIAwPeshtmWXRqjE7wNKt-7HLcTvsKhL0O6snqPFwuEjkWcVJQpDYwwj-LpTQJLAqQHihpDpO43_LiJUNxubcINxKiOhl7jMC4CVru1hxPAXamcXPEXDiBHfD2FbtazKyDXFJuVQWAdlFEDn-i2lH9elNlfGuSt65TPO7I-n582wNseqwtWLjJtktrI3fpkqBYVV-RIjy7mt2gPStM5oyHtJI_rXXLH4xG-EjcELJt2Kw0BZSGBrW-RS_1byIYz3yQsIps-hS1aGKviudPxsk0X0f5ioc6xAtqmW88IkXo_JE56xY7xH_2IlzXcikyEA94KLyhkX3v3M0y7alT18zlb5Kbnvhw2IbKuH0nvEJAkDuxHk176MkP5YSotIrZnYFecmhV6BThImB6wIFfr_leiWMA3ZNaxzaunzafPsQXsb6C7TcCE2j-VniGcWkSRAX8oNQ3iybJVNeBHIp_O5OzVBjIbkXwoiB1HotgBu0sHMIsXwNi1YjVFaDxwtqYHgjCbDVrLMF0DYd1o-tTHX5ltvhezLD927A9fIaQ2r-sb2s2qj6MJwVuXyBNAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=aEExiIsY1Ihv4h6-lLp_NksQyzRwuebf0RxZZeY7VF55zRnbG4ljpTAC6qZM91O5-sitamGjC1EdCo9JWgcQzsLuRgeoiE0TtAkQPWsR-htVP4qeIAwPeshtmWXRqjE7wNKt-7HLcTvsKhL0O6snqPFwuEjkWcVJQpDYwwj-LpTQJLAqQHihpDpO43_LiJUNxubcINxKiOhl7jMC4CVru1hxPAXamcXPEXDiBHfD2FbtazKyDXFJuVQWAdlFEDn-i2lH9elNlfGuSt65TPO7I-n582wNseqwtWLjJtktrI3fpkqBYVV-RIjy7mt2gPStM5oyHtJI_rXXLH4xG-EjcELJt2Kw0BZSGBrW-RS_1byIYz3yQsIps-hS1aGKviudPxsk0X0f5ioc6xAtqmW88IkXo_JE56xY7xH_2IlzXcikyEA94KLyhkX3v3M0y7alT18zlb5Kbnvhw2IbKuH0nvEJAkDuxHk176MkP5YSotIrZnYFecmhV6BThImB6wIFfr_leiWMA3ZNaxzaunzafPsQXsb6C7TcCE2j-VniGcWkSRAX8oNQ3iybJVNeBHIp_O5OzVBjIbkXwoiB1HotgBu0sHMIsXwNi1YjVFaDxwtqYHgjCbDVrLMF0DYd1o-tTHX5ltvhezLD927A9fIaQ2r-sb2s2qj6MJwVuXyBNAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مزدوران حکومتی شعار میدن
«جنوب ایران نکند جنوب لبنان شود»
عجب! شما دیگه چرا؟
خامنه‌ای میگفت «جنوب لبنان الگوی پیشرفته
و موفق مبارزه ایمانی است»! سالی یک میلیارد دلار از اموال ملت ایران رو میدین به گروه‌های تروریستی اونجا  و تبلیغ اینکه ما اونجا پیروزیم و …..!
ولی ظاهرا اسرائیل در جنوب لبنان چنان درسی بهتون داد که الان خودتون هم میگید نکنه بشیم شبیه اون «الگوی موفق»! معرفی شده توسط خامنه‌ای</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6124" target="_blank">📅 07:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6123">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=PANJKvAqXOhcDyBtQuha6Cx623D2-oLTKPU0xhUKWu_szttaPfvCjGfYJ_Gy2aD0q1Wu7XG6l9gIBFf9vTPHsKrLvlW_ncyKpzRBI06e8nAy-ZhDU3s8B4BzC1VP6o1MO0A8g291idAokHDYtAqVdwzXce3xitTwg6uGWsRjZOf9sFbXmb01VE9V605F4liDQekbz5CBFgAIq6x6_CQbG7uSfkh5WIy_eeY2eOuPeaUzf0B7J2MXuaHVqkT3oAvgS9e-Ox56b9shAhmXfdsOzzew12K9nO64PWPuun_eWiOOeX74pjesAitZFOQmYFH6SwiMKrceib_j4s2WZFmXgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=PANJKvAqXOhcDyBtQuha6Cx623D2-oLTKPU0xhUKWu_szttaPfvCjGfYJ_Gy2aD0q1Wu7XG6l9gIBFf9vTPHsKrLvlW_ncyKpzRBI06e8nAy-ZhDU3s8B4BzC1VP6o1MO0A8g291idAokHDYtAqVdwzXce3xitTwg6uGWsRjZOf9sFbXmb01VE9V605F4liDQekbz5CBFgAIq6x6_CQbG7uSfkh5WIy_eeY2eOuPeaUzf0B7J2MXuaHVqkT3oAvgS9e-Ox56b9shAhmXfdsOzzew12K9nO64PWPuun_eWiOOeX74pjesAitZFOQmYFH6SwiMKrceib_j4s2WZFmXgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6123" target="_blank">📅 07:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6122">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=fo0-LVjhRFJovBmTpqnIXlk6tHZbCa85TE5uEJYanwT1vdNqHb9SDmXhOmNy2gWbx4zVtHXNzHrr9Fmvh38oK0No4vTAkvIRQ3csL2nNg0SXVy3Xlcf5REeDbw6eSicLy1B7Pt7oCc2DQZPWybNMGvvxM5bNa-fXTO6PgENIxghz1wG_2GrnR-PxdFrP6B1jeIP9ich2ZJbtHirquRXu-vU3Idxe9udlupvlvXsdMP-zlE6gT1YdtMKTS-ijHQXhBJ9ubNFSqGBwD8fF44d0tcSTj_Fd07drjsPzLI6uWvH7e5JDHUMOpItQCNUgtSP_tvcRcJBPMAQATjadKRXyPCMrYSJA0R3Zohin4AGQtM8rhxtJ-P9eQZa2ZA1-bFVpTPRuVsVd9zwrxuaa02rTlIsKMm-bpuLm72J8sH3zWSFC5blNRFv5OBLczTetgEvb5WRm6SVOFBblfMzof7iESdoN89Fv5lmfyCaIeaWh9RNPImR-PI-9AvttEfEzqdTxxoUFnbC9aNBET5T0lz6LaudIDv90xiG7bCmwa7YOYh7tbDhtx34YNEo1XE1JjlmtqVGLcLWaljTGEFFmZqA1l9M00Nw_-KPDSpfT_3DKJ2F6AGrewTxLdM1gNLOC5Yij9kR--QlOgkl9yv1XJtpMpwH-AXZrh0fH_3R1zd5XK-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=fo0-LVjhRFJovBmTpqnIXlk6tHZbCa85TE5uEJYanwT1vdNqHb9SDmXhOmNy2gWbx4zVtHXNzHrr9Fmvh38oK0No4vTAkvIRQ3csL2nNg0SXVy3Xlcf5REeDbw6eSicLy1B7Pt7oCc2DQZPWybNMGvvxM5bNa-fXTO6PgENIxghz1wG_2GrnR-PxdFrP6B1jeIP9ich2ZJbtHirquRXu-vU3Idxe9udlupvlvXsdMP-zlE6gT1YdtMKTS-ijHQXhBJ9ubNFSqGBwD8fF44d0tcSTj_Fd07drjsPzLI6uWvH7e5JDHUMOpItQCNUgtSP_tvcRcJBPMAQATjadKRXyPCMrYSJA0R3Zohin4AGQtM8rhxtJ-P9eQZa2ZA1-bFVpTPRuVsVd9zwrxuaa02rTlIsKMm-bpuLm72J8sH3zWSFC5blNRFv5OBLczTetgEvb5WRm6SVOFBblfMzof7iESdoN89Fv5lmfyCaIeaWh9RNPImR-PI-9AvttEfEzqdTxxoUFnbC9aNBET5T0lz6LaudIDv90xiG7bCmwa7YOYh7tbDhtx34YNEo1XE1JjlmtqVGLcLWaljTGEFFmZqA1l9M00Nw_-KPDSpfT_3DKJ2F6AGrewTxLdM1gNLOC5Yij9kR--QlOgkl9yv1XJtpMpwH-AXZrh0fH_3R1zd5XK-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا میبینم راست میگه …</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6122" target="_blank">📅 07:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6121">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHJtjCgpgfKYxQODnCZsyZ2mqIBVw5MzRhh2rLSh5ki_q336XL8urRxGJXrGhJoWtUjqFczWcMNsuH5Palf1pGf94FBMd2Dav4lTeBEOfCSIypyLSCgxLKaaCchi2iFRfV_WBJHQ7qNuyeJ3R7rV2A6W5Thu0QM5wrUNZMBhfPQYR4_4YJxshoW7tfP8I-99GeVVYGC6fxv2b4wR9oQyZw8p3HYvTHfoAbP7Tlufft818KDQmIXB70R72wouPGV90jBWcgDxeiclNy980CPu4OC3qOFgMPt8WjZ_CbW89viyZsVeL7qgKHjZHw3aVc0XhnPC_0g0XASi1Md8d-yVCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6121" target="_blank">📅 06:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6120">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BeaQaB5s_EpogbxIo5wV-plQAbnMZHOUJFyiWuPMVZ3H1Ejy5dA0_Ay_aIz8pNO0ZhAuwFxvvuuGr7psuRnAzUDpw93RkzEtdB-IrNwe9-o-t8a2LKR1YyVrR83zu8JOMQE7NxMLNsHRf6fHWcJiqLprjD-QIA39TLpOWBdvutBQUqs0F181LFTscMkpgxfASruadH7DkrGtHLyRBBDHTjxu3cZA8EGpJUgtBLtk3zDOOlfpZGvFU521xIsd_ks9X5r53VrNoxvqLs7gMa74Gl5e0WHIRPe2OGGf3jxLc62a2AYDk1JM6aQPSGyiTrCIjnbFyejk85ClOHkVtUxEUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6120" target="_blank">📅 06:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6119">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=WRLEwoSaNCAMAx2xNdakPNzkIA4Qe5kGfpzwqkSbGxz02YdUiHes8uAUXzY_fKPDgNIU4BM9aTZapQFfvAWl-jehE6Vr4hdpdXhOuLRNz7b152CXRhTRHC-ElfuIeZhbBIOSeA0_XqwY4ZomU5diG341JUMCzbxhM-kRkhxUsXZudTDOFtJYAkvF8e4f7skzC4lzEibipyekSfofnI1uER4zophYusyMkP4gH8mvHMBfxhVtd8A66SFo9BJEo0XlqZhdVoqTC7YZOxJ88n5SOkqkjQY5PmNuGL4WTSlJInOyT4DLncTk-YvDHCf8lMBw95iV4cB1XCJtk9qwbxAsLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=WRLEwoSaNCAMAx2xNdakPNzkIA4Qe5kGfpzwqkSbGxz02YdUiHes8uAUXzY_fKPDgNIU4BM9aTZapQFfvAWl-jehE6Vr4hdpdXhOuLRNz7b152CXRhTRHC-ElfuIeZhbBIOSeA0_XqwY4ZomU5diG341JUMCzbxhM-kRkhxUsXZudTDOFtJYAkvF8e4f7skzC4lzEibipyekSfofnI1uER4zophYusyMkP4gH8mvHMBfxhVtd8A66SFo9BJEo0XlqZhdVoqTC7YZOxJ88n5SOkqkjQY5PmNuGL4WTSlJInOyT4DLncTk-YvDHCf8lMBw95iV4cB1XCJtk9qwbxAsLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام فیلمی از حملات خود به ایران منتشر کرد.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6119" target="_blank">📅 06:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6118">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=kaRapjUpnX9F6gcrP1kSs5TZlFIqcBnYLjEZvSGFNSApxQIM5kGUnbJAHYv4OyNLANr1AedaWQOLYZ1iEA8ixoDJ_Mj1P2NpKZmsJ2qegnzMzW3Qz-a7diM6PgY3BInT8qSIgJRBIk0lenb22c8h5snHsychYb4I8PRQA6jPKgRPvPZDtqVe3duhVjkISF7Ynm8MBU-obdgflUimtO9aP2fWSqwjyxfQ7j6wSc_y5SjntQYgxbMecMofNzf3kaoOiahdF6xNaxii7hBq6gTXCarB9LBsk5c_TrXdCzt2sBV4JzwRqMZbNz_MzSYQ9rYbt9vtgoRdTNzJBpwhvIgKJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=kaRapjUpnX9F6gcrP1kSs5TZlFIqcBnYLjEZvSGFNSApxQIM5kGUnbJAHYv4OyNLANr1AedaWQOLYZ1iEA8ixoDJ_Mj1P2NpKZmsJ2qegnzMzW3Qz-a7diM6PgY3BInT8qSIgJRBIk0lenb22c8h5snHsychYb4I8PRQA6jPKgRPvPZDtqVe3duhVjkISF7Ynm8MBU-obdgflUimtO9aP2fWSqwjyxfQ7j6wSc_y5SjntQYgxbMecMofNzf3kaoOiahdF6xNaxii7hBq6gTXCarB9LBsk5c_TrXdCzt2sBV4JzwRqMZbNz_MzSYQ9rYbt9vtgoRdTNzJBpwhvIgKJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : امشب، فردا و فرداشب به سختی به آنها ضربه خواهیم زد و هفته آینده پل‌ها و نیروگاه‌ها را هدف قرار خواهیم داد، مگر آنکه  مذاکره کنند.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6118" target="_blank">📅 06:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6117">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caeb092620.mp4?token=EpJa-xa532moBT2aE8q6q7-RIbqm9dbKYgpYwO12NkF_B5i0D8OjJ3I-JWbtJM2vjeN43ZBTW_re_LJOybRp5mpPiVHF03hGGMyAQRbnKmGO3L2ftlkojcguOdXp1gKBsVKdNkoSrXaCBTXIPbuFgHGTTdD_nV6y4sVH0sGB1LaNq4DqWGB3mThoNyUEm_aXK0oQcUYh2n4O6APcG5pFlnBCBYMlqSo6CfBXn21t3di_NMy4Ch0JDLKeSeTN58sG58GIYyRWl9IvgbbhGpSPRdCgxCLTvKyXU6nK0eokXk81VzsVfslR_Xb6Vn_hE1xVZvzeXCiVjLRNccNA0NE9Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caeb092620.mp4?token=EpJa-xa532moBT2aE8q6q7-RIbqm9dbKYgpYwO12NkF_B5i0D8OjJ3I-JWbtJM2vjeN43ZBTW_re_LJOybRp5mpPiVHF03hGGMyAQRbnKmGO3L2ftlkojcguOdXp1gKBsVKdNkoSrXaCBTXIPbuFgHGTTdD_nV6y4sVH0sGB1LaNq4DqWGB3mThoNyUEm_aXK0oQcUYh2n4O6APcG5pFlnBCBYMlqSo6CfBXn21t3di_NMy4Ch0JDLKeSeTN58sG58GIYyRWl9IvgbbhGpSPRdCgxCLTvKyXU6nK0eokXk81VzsVfslR_Xb6Vn_hE1xVZvzeXCiVjLRNccNA0NE9Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار ناشی از حمله پهپادی امشب سپاه به کویت
گفته می‌شود مخازن سوخت ارتش آمریکاست.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6117" target="_blank">📅 06:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6116">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/360d24e506.mp4?token=gKlGtDMrozB80goKvLJLwJrnuaFhUmCh50mGPJcqofsiQTu2HLMUtfiTxDD6t9KmJ24DK43CXS3ffh_ZPJoynQdObEMM7QGi9JtG5l81cfuKUtdGoS8fMAWqaC9QBH4W3NH8gyWh_KerooFdUJcoaAxaA7eFjOvAAi5H64jmNiHvEtYs0I3RyqYspH_1kofi-AAmdiF5avcIyHP4QPzMkcWy-0XnHcbY4Y4y001_d7cig7N8vHR3LvohQQvBb9H2jkFHu55gH1Om53-s9Gv-I_OmcB4npQ5ijwoMcDakHuq6iXkd32tIK4G26vo3zSLBt2vV8QkjCZlyzEDwFT1iOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/360d24e506.mp4?token=gKlGtDMrozB80goKvLJLwJrnuaFhUmCh50mGPJcqofsiQTu2HLMUtfiTxDD6t9KmJ24DK43CXS3ffh_ZPJoynQdObEMM7QGi9JtG5l81cfuKUtdGoS8fMAWqaC9QBH4W3NH8gyWh_KerooFdUJcoaAxaA7eFjOvAAi5H64jmNiHvEtYs0I3RyqYspH_1kofi-AAmdiF5avcIyHP4QPzMkcWy-0XnHcbY4Y4y001_d7cig7N8vHR3LvohQQvBb9H2jkFHu55gH1Om53-s9Gv-I_OmcB4npQ5ijwoMcDakHuq6iXkd32tIK4G26vo3zSLBt2vV8QkjCZlyzEDwFT1iOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی با موشک‌های حاوی بمب‌های خوشه‌ای به بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6116" target="_blank">📅 01:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6115">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
ارتش : به پایگاه‌ها اف ۱۸ های آمریکا در اردن حمله پهپادی انجام دادیم.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6115" target="_blank">📅 01:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6114">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‏امشب اتفاق جالبی افتاده، به محض اینکه خبر انفجاری در شهر و استانی منتشر میشه، مسئولان جمهوری اسلامی سریعا مصاحبه میکنن و میگن دروغه و همه چی آرومه!
‏اینطوری مثلا میخوان صورت مسئله رو پاک کنن.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6114" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6113">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LF2XIia-4mmpXQ0pqQ6EIoD3vEkz8VrkLng-_CH61eGRXYG4Xa1LNjnAwqM3Qfhv7hKfq5ykRfsR25yl_qtfwaTIlaVdhgAJKgVLFfepLL3LsYjVKb1xE3TCqMzzgMd50XDdkgax2xWixdYaOBUU40CCDyNAQ-bartF5Xgz7xf_07cIi8UNb5_SIRCrJREhfaMyzJZY4EEqpxtIgHC6DP08X8GX7w5TN30g7dXPAcIaEBbivDWJlWpAHjGlPYDy_rXdOLY1RrfO1t2nWggEge8K8UYmdjka5ueQz0HZFyCqzK8AY4a3ChSy9uGKicj4-QyLsgTKnmahDLAIKfildkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگارهاشون می‌نوشتن که کشتی‌ها دارند  از مسیر عمان رد می‌شوند، تشییع جنازه،  بریم و کاری کنیم که  کشتی‌ها مجبور بشن از آبهای ایران رد بشن  و شروع کردن به حملات به کشتی‌هایی که از مسیر آب‌های عمان میرن.  به زور حمله میگن کشتی‌ها باید از مسیر ما رد بشه.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6113" target="_blank">📅 01:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6112">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfoagWrHgBXwVARf806olMzCg-UvDGMAJPh9LspYh48xpcL17M4tPJw1JNELvhzgTH0zQo1WMN03BMKZglqbUCjnhejmrzYn03Pss0c067q9Wjpz_gULHD8G7lWD2mfYB3dB_aIqxdqfjCE7AaGJ7RMGvgehHPrR_lvN1lbKETRIHxF_jMnmACxHLLto5pb2uqE9vymkc5jPL51_OFZ3br27O31h4gE3lE6iYXEk3LTjxjTitDDtT2i_dUX_ywLGLwhf7Jb3617sNrXuBAOuKERseqtKUupAYaHN0V732UXHpgG9CqZ5V2F-QXWMVIVOxxJ0TBBkw-LnwZsxa8BuLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا در حاشیه خاکسپاری جسد خامنه‌ای و جلوی قالیباف شعار میدادن «مذاکره با دشمن خیانت است»  هنوز به سه کشتی حمله نکرده بودن و نزده بودن زیر تفاهم نامه</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6112" target="_blank">📅 00:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6111">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=Nd141ufUYbnMGhaRS1JJCarGSBS5XUz-AJXtzVq7vr7haCvOI9gmt-uYbS8VBYkL6PSbXBqIaY49yHaWwcgSwgKvFeM-5W9dD8cA7PvzKdD7AoywdgwoMxfVhm1ggyGsvin4ZWCX8T6ZXsQ5Zt04HdUuZMTuiZgwDM1lk8nq5x-Inex0FJ0Md2vkwRag_rKt_DtCduutfbtSg7yvYP063WeRey92YypK0SlNagkmOwfSA-VZfCFDKenWULXuUThzBAJZt4WbJmXBQg561kjdjd_cT93AZV_KW5K-eaLbfwuS2rgIK52iQXW1kAzfUyeb0NdYzGpui3maxQM2xi6XOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=Nd141ufUYbnMGhaRS1JJCarGSBS5XUz-AJXtzVq7vr7haCvOI9gmt-uYbS8VBYkL6PSbXBqIaY49yHaWwcgSwgKvFeM-5W9dD8cA7PvzKdD7AoywdgwoMxfVhm1ggyGsvin4ZWCX8T6ZXsQ5Zt04HdUuZMTuiZgwDM1lk8nq5x-Inex0FJ0Md2vkwRag_rKt_DtCduutfbtSg7yvYP063WeRey92YypK0SlNagkmOwfSA-VZfCFDKenWULXuUThzBAJZt4WbJmXBQg561kjdjd_cT93AZV_KW5K-eaLbfwuS2rgIK52iQXW1kAzfUyeb0NdYzGpui3maxQM2xi6XOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این استوری رو ۶ روز پیش گذاشته بودم  میگفتن آمریکا میخواد آتش بس حفظ بشه ولی جمهوری اسلامی باید «کار دیگر» بکنه!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6111" target="_blank">📅 00:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6110">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550f13e765.mp4?token=f8J8x5NUoX-miI1qMxB4ecJ5QXbJzjhiEmXtCSXYTRoCiXhjZe0HpXAEW7HNQ51timbByE6SPZuepmJo1KMSrwxcxeyNUeZCu835wZLCcxaal-flLtmwGaU7xx-wihHgEL6AZlDc9O0M4bEE3eTZpBdCXZj3IaJE0GisnxJMZRsQ6S8qqHC3es0Hix9FyXvPQCf7w_TWfO-25zsftdHpcL7xC-OGPYHEO_k6vwOJV08KakRcOa0iPGK9cIiId_dsLzPmKb7h8-HHk8ECE-PxuaspBFcDefoBEENanODnCyVau9b01xMt1YA_o4EhDylisP_Erh9JoIeWnruZ6UWepTC_KhfKl8CCkRwwEAqbCU_C4CjyYyuQhH6R040oRBoSvh4tS6BLxCD7payVqiSzgLgW2kARQq8b62csEp-x8Ks-_vDtYNWzM2dj7A37blgyuyyrGT-0ZjU2Dojhde60To4HbekiYChAPHlJvSOdJyxLowsynyuOzrfh56gYOZC3QYN2gIUbf2KRGPGpNmHttPGgVHe0adgNFvBh-qzhaBVMKGtoXhQMrW5RYXubqYXtVnEuKLwQFGBc4FwpPFll1GWz-bcPkIVAKl2XvBxvGRX9W6BvY398eqSdFj2Win3JNstN2TZbyZV3WUANUTGj40hQC6V2T3tMP28NumOh1jc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550f13e765.mp4?token=f8J8x5NUoX-miI1qMxB4ecJ5QXbJzjhiEmXtCSXYTRoCiXhjZe0HpXAEW7HNQ51timbByE6SPZuepmJo1KMSrwxcxeyNUeZCu835wZLCcxaal-flLtmwGaU7xx-wihHgEL6AZlDc9O0M4bEE3eTZpBdCXZj3IaJE0GisnxJMZRsQ6S8qqHC3es0Hix9FyXvPQCf7w_TWfO-25zsftdHpcL7xC-OGPYHEO_k6vwOJV08KakRcOa0iPGK9cIiId_dsLzPmKb7h8-HHk8ECE-PxuaspBFcDefoBEENanODnCyVau9b01xMt1YA_o4EhDylisP_Erh9JoIeWnruZ6UWepTC_KhfKl8CCkRwwEAqbCU_C4CjyYyuQhH6R040oRBoSvh4tS6BLxCD7payVqiSzgLgW2kARQq8b62csEp-x8Ks-_vDtYNWzM2dj7A37blgyuyyrGT-0ZjU2Dojhde60To4HbekiYChAPHlJvSOdJyxLowsynyuOzrfh56gYOZC3QYN2gIUbf2KRGPGpNmHttPGgVHe0adgNFvBh-qzhaBVMKGtoXhQMrW5RYXubqYXtVnEuKLwQFGBc4FwpPFll1GWz-bcPkIVAKl2XvBxvGRX9W6BvY398eqSdFj2Win3JNstN2TZbyZV3WUANUTGj40hQC6V2T3tMP28NumOh1jc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو رو دو هفته پیش گذاشته بودم.  معاون سیاسی نیروی دریایی سپاه اینجا در جمع حامیان حکومت بهشون میگه خیالتون راحت باشه، حملاتی که ‌ آمریکا انجام  میده «واکنش»  به اقدامات ماست!  «کنش» نیست!   تمام این ۴۷ سال همین بوده!  یه کاری میکنن ، تنش راه بیفته،…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6110" target="_blank">📅 00:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6109">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6109" target="_blank">📅 00:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6108">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=Ec_YFQpwRKEGwAisfff1Z18lbRmnOMjVj-02IT-yOCFplS76omI0C2BI_MbThAY5PYKlp1vw5_hPkV56sddmYExogW7eI_9D5GXCd9bzyqF6jQ0dmyOi4JKwzUQekIvC_VJGjzuVM4qkc5FE9FECmH20I3KkU3LZOQ3Cd3sCUE38AiJTIQbEqCBgMcdMsJ77j5FrNe8AC3d9Ch6AdU1GDLTTWz5l-TCEjH9fR0-oCAfXo06X2N50I3GPzM7hb-QVHnN7I2anYSkxZiQiK5XdojzTw6bbG2BQG65rDLFCWrL7-cTLalZYZHcTqNec20iAgMFKOhrCaqRCXzEW81BigA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=Ec_YFQpwRKEGwAisfff1Z18lbRmnOMjVj-02IT-yOCFplS76omI0C2BI_MbThAY5PYKlp1vw5_hPkV56sddmYExogW7eI_9D5GXCd9bzyqF6jQ0dmyOi4JKwzUQekIvC_VJGjzuVM4qkc5FE9FECmH20I3KkU3LZOQ3Cd3sCUE38AiJTIQbEqCBgMcdMsJ77j5FrNe8AC3d9Ch6AdU1GDLTTWz5l-TCEjH9fR0-oCAfXo06X2N50I3GPzM7hb-QVHnN7I2anYSkxZiQiK5XdojzTw6bbG2BQG65rDLFCWrL7-cTLalZYZHcTqNec20iAgMFKOhrCaqRCXzEW81BigA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گشت زنی اف ۱۸ آمریکایی بر فراز چابهار</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6108" target="_blank">📅 00:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6107">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا : محاصره دریایی ایران وارد فاز اجرایی شد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6107" target="_blank">📅 23:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6106">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
چندین انفجار در بندرعباس
🔺
چندین انفجار در اهواز
🔺
پنج انفجار در قشم</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6106" target="_blank">📅 22:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6105">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otS6Wl4NV7Sj8FJobBQ3NK6U-aUjBpRnLRZAEM1cd0R-57u4tj75HqxNzKDkuPo_kt4cOP4OGzh0d1isQWenSJFg3wuB5juuxgwH2vX4Zd-ug6bJf-mU_5knxV_vj5NSPgPoUoqTCiFSbQUdex4us2-We885pD5WXzmpjiKePxLVzJ9axF7wreV3pxEb2_F2aiwEU-4mGKZriOXNe2nskOEbgA17HHwdMgnPo_esE7s7OZpkEHCXl_lQ1gmkBkfhSKVX_v_iW4sBHEaXDqyYSHymAh0mRmhi76lbVUEoMUK4zvp28Xv0aaQ7kmgGRhoEFABKeogEF9Jhe-qzZbKW6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2077085449948938568?s=46</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6105" target="_blank">📅 21:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6104">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
دقایقی پیش : حمله به قشم و شنیده شدن چندین انفجار
🔺
حمله به یک نفتکش اماراتی در سواحل عمان
🔺
فعال شدن پدافند در کویت</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6104" target="_blank">📅 20:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6103">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6103" target="_blank">📅 18:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6102">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWjVHaSRfTPiim3YPbT8QpJ-LJ6anj_7vyYCmKnX7jHI3dSNrgVsUGh5vUnCDpBwD9Zz9G8WMqfDvAszRQ5MZm3P1Y5g8qq-b-zeYZG7gFJx5bZXJHGS-rd9Vka6DjWIk7Jz5nquCZglHOMH7wmEnq0o4ktSltUKHtk8J5UUZGS1u6z-gsCVTUcYVAmZZuhJ3VkKaRkd3wIYxbl2JWVrgLAFLljr3wC7eXFgR0AA9O3Bn0n3R_hE__KVc3vQD16-p_3Bt3S54p9caOyL2l0pi0NB6w15vettKCacBXjcnlOowOqKtspS2dA0Kr7XRLNGOnyA1JM1jbKHD4uFRqnJOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهپاد‌ها (قایق‌های تندرو بدون سرنشین) آمریکایی این مدلی به یکی از مهم‌ترین مراکز نیروی دریایی در بندرعباس نفوذ کردن و حمله کردن.  گفته می‌شود که در این حمله یک زیردریایی ج‌ا را نیز منهدم کردند.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6102" target="_blank">📅 18:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6101">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=XZStI4_7hagBmZyKzrLnFx90LxJE3iZtv7678RmhwazFaKFcloHnthFBbxFRFIWFejqfAZ7bp-ZhGySi5fi1tUlWeF_MUi54_eOsPozg_ImgxVyMZSl8CZaQA-rQMCUP3hyzjmVNJaBn5u0FUXWjp36SeCGrZtp4Jt4are47QvxuX_lFk7bcEaOPllarR2xmtVrOUOQvLXqypXOtHvsHiwmlz9446vuz6cbRAzJjVZ8GxB-P2YvBhNSPKP-MFUYVosPVh9ldwiUTHuO2a0v4K-OPpIwHb-aRRG-HtmzOqPqi734aVZe3YxKHYouqxuO8uDAooVALO8HGKNrraIy5ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=XZStI4_7hagBmZyKzrLnFx90LxJE3iZtv7678RmhwazFaKFcloHnthFBbxFRFIWFejqfAZ7bp-ZhGySi5fi1tUlWeF_MUi54_eOsPozg_ImgxVyMZSl8CZaQA-rQMCUP3hyzjmVNJaBn5u0FUXWjp36SeCGrZtp4Jt4are47QvxuX_lFk7bcEaOPllarR2xmtVrOUOQvLXqypXOtHvsHiwmlz9446vuz6cbRAzJjVZ8GxB-P2YvBhNSPKP-MFUYVosPVh9ldwiUTHuO2a0v4K-OPpIwHb-aRRG-HtmzOqPqi734aVZe3YxKHYouqxuO8uDAooVALO8HGKNrraIy5ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت جنگشون :)</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6101" target="_blank">📅 16:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6100">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YiTbnSDqFfDKFGcv1bwyaY4Nk5Eabos95-tRlSLpA6I7A6iWc8zMWkyzb1gorMl5uxFnIryXTZgUvSGW2iU_ePUNhxbdm_GxxmuPMGdRowVU4wgBat63QDMOiEemm5RQHpRDWfw6ieFC72NGzsv6vyHWlYG4HEg9vIH81zUx3SgfHTbU3ldcgAzvHioTRLcTBx9Z6cXnJKipBeBS3uZf368_dNbJTI0KYLmlbKqbLtca08Bl9XsSp0ZisvSskbrYgnm4Y6yLU0d3KUeiV-Crs9SJXC_-Ou3ZXoeUMAMVm6eCQ-lB0NydUXFu9TMybT8wEP8m5uFPxPmsuU055n4xjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏آمریکا با استفاده از سه قایق بدون سرنشین (شِهپاد)، پایگاه دریایی دیروز بندرعباس را هدف قرار داد و تأسیسات نگهداری زیردریایی و کشتی را منهدم کرد.  این نخستین بار است که نیروهای آمریکایی در نبرد از قایق‌های تهاجمی بدون سرنشین استفاده میکنند.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6100" target="_blank">📅 16:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6099">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">۴۷ سال رژیم اسلامی</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6099" target="_blank">📅 15:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6098">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JVGJcQU276phc2P2z5y0ne-jBJx2c10jONl6S4nVkRjO5WLqEzmjzEDyjqd64iPtrhJP9DlJ8EjhK7UgoKas0Oqfw4gGHkqcPf41a6017fLFQ6-mkPIAEjKF6xSWbgttOpqtg_tllUp22j-WBWUOMsV8s9bR2hw9l0HhyfmxjLRIXcHK6ufIhQIjUCiPaNfDwf3qi-L7o66AVZ1CxAn87zf6rpT1MwrNJmVAUg_CBnJY8EkwqWhwOrcwWqEixFm59Gk8MnTOWFrUaHvCJz0DrDM7hE4AqPpDhSRXukG2_u40GwdauW-mb_oGC0AtFrWVzeepGO8OcFOlHrx6ixdTVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
تخریب ساختمان مرکز آماد و پشتیبانی دریابانی نیروی انتظامی ⁧ بوشهر ⁩ در پی حملات هوایی ⁧ آمریکا ⁩ به مراکز نظامی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6098" target="_blank">📅 15:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6097">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9c510f4f.mp4?token=rmgQjzlyKL7iIWEHfPssPf-HWo2mPBAsHuLzaT_BgsTSBcUlnVsDknSmzl2aaU45UnA6wDsDrQ2qIcrh4zjhaEi_5whSHgVPRxv5u25-nCDmM-ZwKN-NaVA9nh0GXNV4OfGXiAmXS5NfqrjQIBRd-ckx5Dwpe0Fj6liQK3DoL4Pn82g2Hs3GYSfAv7pg_8Dr1kpASclntMdQe5_HHBv3I6Tap_W5fp1SZ4QrkC9ISCcR4esfjjClgmAVmQsOn50z5ZabfmV2f4y8y7djKztwWCn1hO4JTVxh74cBJDjOIPIuz7aXkmbFrZ2ycP0X_KQeTZwBGUFMZ1efcwHlnt87eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9c510f4f.mp4?token=rmgQjzlyKL7iIWEHfPssPf-HWo2mPBAsHuLzaT_BgsTSBcUlnVsDknSmzl2aaU45UnA6wDsDrQ2qIcrh4zjhaEi_5whSHgVPRxv5u25-nCDmM-ZwKN-NaVA9nh0GXNV4OfGXiAmXS5NfqrjQIBRd-ckx5Dwpe0Fj6liQK3DoL4Pn82g2Hs3GYSfAv7pg_8Dr1kpASclntMdQe5_HHBv3I6Tap_W5fp1SZ4QrkC9ISCcR4esfjjClgmAVmQsOn50z5ZabfmV2f4y8y7djKztwWCn1hO4JTVxh74cBJDjOIPIuz7aXkmbFrZ2ycP0X_KQeTZwBGUFMZ1efcwHlnt87eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌پرسه نظرتون درباره اینکه بدون هشدار قبلی برق رو قطع میکنن چیه؟
‏چمران میگه:
‏شما اگر بدونید پریروز چند نقطه برقی رو زدند دیگه این سؤالو نمی‌کردید.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6096" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6095">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WM5py5QS4buS-Q8XxVbiILct0p6jQJohrNReE11NDKLO3PRYh0CzAsxBwy1yxYBegYCTviesA29jF9Ntra1XonEcKWsGkDEb-nalT0_WoKEIAyxLsBVjWt1v1TfllaMlI-vMEEmpwRDaXLkZWg2hMfojm2mHhbnbysdX0csaHlDWkbFBYsUv-7LxC__kgqxKvnEPLngbpRu39cuggwvZ7su7h7YHsaKEuSnx3A4vR7LpXYc6OIAWkTZS896UE_4A7rOU0HneKrKDWclP2U9Qv28dRcRDiGtR4fqoSYBwNOWGqsOFQeC61CRqe-RaFHYgXKL_BTrPIZwZsn7C0a0vyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه ترکیه، دیروز جمهوری اسلامی
رو با اسرائیل مقایسه کرد و گفت
رفتار این دو شبیه هم هستند.
(کاری ندارم که ترکیه خودش چه افتضاحیه، اما نشون از تغییر رویکرد ترکیه نسبت به ج‌ا داره)
یادمون باشه فرمان حمله اخیر از سوی ترامپ در ترکیه صادر شد! یادمون باشه معاملاتی بین ترکیه و آمریکا رخ داد، که آرزوی ۲۰ ساله دولت ترکیه بود.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6095" target="_blank">📅 14:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6094">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
حملات دقایقی پیش به بوشهر ، خورموج و….
🔺
سنتکام چند ساعت پیش گفته بود که این دور از حملاتش متوقف شده.  در اسامی شهرهایی که مورد هدف قرار گرفته بود هم مثلا نامی از کیش نبود!  مشخص نیست آیا همه این حملات را آمریکا انجام می‌دهد، یا کشورهای دیگر (مثلا عربی)…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6094" target="_blank">📅 13:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6093">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dlCInO84AgGuUJdo-giSddCm3Cjyw7TKANRBaMcOpSbmjCfXi8itO4Z-vPGXZDc1xdx3AIbmdb8-B44z62pAUp8nTNuOT0WYvKFSARySGHhV6ppPfB4nNLXD1c78dqVuitBl8Uhqtd2tCnYAidF2opIxVxDGDJe6lNaLLZ3qo87SqP29QzCAUOOVbIs33QmLyawMyxKwHNA0orNFlgZgubY9P5-iap_4xrsK5_K3AtH_uD-JT6il5pd_PMTGm_TdP92XJJBL_eXGuyQSqhagtEGK3PPlYfFEo6Lom9ZhWGoct4d0gIz3C2e0n0efTiFO8La-tIQUnky_Y661n4QfaQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=ekGemtbIoe4rxGarRCym_scpDmmrXwEQTNUvhOtuG6BjFyfdoPCXgE7j53rTdDGTIpcscixhndY_BKwBECCxOzOu-Fe9FJP92PicFvQfzb5SxRYiq1EcFJQ_MVx_GuD4dYHhG8eR4EobtIby337QD8IZiyxcMGe0IxmyjQmeeztvFpKbLGuWGub8oXjaPI3D0sgz6PCZCLp258zw6O4-X2Tzk_oUYo070v3QfSGhQqiiOH6VCNOly79Q86mLqSX_dYIg0ER78JCE1DuiMcg3IaUIRgNF517sfe7COcAR1SqIVtCDgIbqF4e_XbsLaxk2Ouhuk4wMgJafG9LxiaH2KWzC6yVCOd-uqgzFAKlL3pPidegrJEF0ImapjDMYKRr-XaHCxE5yeT1ly1eGocNHza6xYsBLg2Pyd0yYQDV0EnPosibDF4u04_I5ZM92cTjtlauAviR463r0jKfuvRojXt4gxUvxYx88ipNn0xyYQ3ZNST0ApGPth8gWbz9nEoJjhwE31zFcER9pCbQoG1ODgD5EAXe1GKb1qqufMbaLtlc2lgcFLCnAaf5hWIZ7Ukw9BQiT5mGtaEGU_ReQF8zdF2Rfa3JexjYNSLUJ5uxuiJOYXDJInh3g9be9YBfOnDy9vJTeshvtr-h7yYjfHq6KmgMS_pCjvUJ7cHMrmgDBozg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=ekGemtbIoe4rxGarRCym_scpDmmrXwEQTNUvhOtuG6BjFyfdoPCXgE7j53rTdDGTIpcscixhndY_BKwBECCxOzOu-Fe9FJP92PicFvQfzb5SxRYiq1EcFJQ_MVx_GuD4dYHhG8eR4EobtIby337QD8IZiyxcMGe0IxmyjQmeeztvFpKbLGuWGub8oXjaPI3D0sgz6PCZCLp258zw6O4-X2Tzk_oUYo070v3QfSGhQqiiOH6VCNOly79Q86mLqSX_dYIg0ER78JCE1DuiMcg3IaUIRgNF517sfe7COcAR1SqIVtCDgIbqF4e_XbsLaxk2Ouhuk4wMgJafG9LxiaH2KWzC6yVCOd-uqgzFAKlL3pPidegrJEF0ImapjDMYKRr-XaHCxE5yeT1ly1eGocNHza6xYsBLg2Pyd0yYQDV0EnPosibDF4u04_I5ZM92cTjtlauAviR463r0jKfuvRojXt4gxUvxYx88ipNn0xyYQ3ZNST0ApGPth8gWbz9nEoJjhwE31zFcER9pCbQoG1ODgD5EAXe1GKb1qqufMbaLtlc2lgcFLCnAaf5hWIZ7Ukw9BQiT5mGtaEGU_ReQF8zdF2Rfa3JexjYNSLUJ5uxuiJOYXDJInh3g9be9YBfOnDy9vJTeshvtr-h7yYjfHq6KmgMS_pCjvUJ7cHMrmgDBozg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجتبی خامنه‌ای «علی الاصول»
با تفاهم‌ مخالف بود!
و نوه خمینی هم این چند روز گرد و خاک به پا کرد و گفت هویت ما در مبارزه با آمریکاست!
اون‌هایی هم که نگران زیرساخت‌ها بودن
الان سکوت کردن  و صداشون در نمیاد!
آغاز دوران «علی الاصولی» !</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6092" target="_blank">📅 09:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6091">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0CvpJV8YA_Y67qD_w7RvYcMmS6xLLm3YP0y6a5FbiK8jHkw3WMzQQsjngfKOHE87Kk92dGeo1h-j2bWrlqLkjeIPbXQCz_yaXMn75VoYBX9Aj-TfcZZSVH-gBD0W_rEQTxOQW-7MJhYqje4gr2SlEYt0zC7vrnXFiwlqj3rL_nwfTdrxAL263XEKTuQfq3ODT8ciJ9O92ONv-WL9NaXA6_eZBYF6XwkuaP5CRtWC5Ov5h5Znya2Swx9t744HNufCvJ1gAr_gS-mhXXFUEcAkQXhwzD2WkYEto8DOChVAt3AZnPspxpRygGa0kHUUh9xpSBj5yhg3YQa3-a8xFmK4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شب گذشته سپاه به دو سوپرنفتکش (در سواحل عمان) حمله کرد.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6090" target="_blank">📅 09:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6089">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/671b861555.mp4?token=CVIZ63WcdvE-sYBzn69AukNp9rOTN1aCaBxr8TCixnGydLF7EXbIpqnbxGpy0xPO1Sa7jk5kotdvJbErVRwjvYg45Rk4qovDi9DMj1Wi1S4ePV73II36LXl-03gEwP1NVeWVIc59rwaf81IwtCH-PStvwO-1ZNDz3wJEYM1PvtkV8WW_d6Y1ZYKN8PvRB0VQDZxE2j_6dqj79_DzgoMmobQ3OshIgcrScryZVZ1FKDbFEhctuKWQw3dJJiODn_sh3jskpoPLZSMemURCTKloqsY-IvxpsB0kRKbSYxP4zGEzjVwb8Us1rQuEQCanRHXC7_7MyYz1LJt-vYG0ebXcV0CCyqrz86Al-HLPN6v-ZVvc9g9pRjdU_kxURXu-5ZXQM18TnbgjayrkPtrT_t4-HQWwFkoYO6P2E8RsoxY8VGfqCx3VfBNP3LDcsxFKp7e7ZTsu9-ZxCwUiAFxJw9KTjQeTz1bGA1lvw-7mUZft8vabpMzdep4Qs0wmTReA15_dxrQSXut4X9L2jbJ7sJa8SdlMtYCqCc8PDYPw5n49Ltxpq5E6_xWGR_9rtmECrctbG-0Sgqre9MF0KaKZgiRgg4gI9eiQ6vplofW5ppgJo51vo1BkJZo2tPSZStzFHpY6Gtl7Cq7ZHPZbLT2_j1UB4RDHHyoeec3ULCRAEAYSJOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/671b861555.mp4?token=CVIZ63WcdvE-sYBzn69AukNp9rOTN1aCaBxr8TCixnGydLF7EXbIpqnbxGpy0xPO1Sa7jk5kotdvJbErVRwjvYg45Rk4qovDi9DMj1Wi1S4ePV73II36LXl-03gEwP1NVeWVIc59rwaf81IwtCH-PStvwO-1ZNDz3wJEYM1PvtkV8WW_d6Y1ZYKN8PvRB0VQDZxE2j_6dqj79_DzgoMmobQ3OshIgcrScryZVZ1FKDbFEhctuKWQw3dJJiODn_sh3jskpoPLZSMemURCTKloqsY-IvxpsB0kRKbSYxP4zGEzjVwb8Us1rQuEQCanRHXC7_7MyYz1LJt-vYG0ebXcV0CCyqrz86Al-HLPN6v-ZVvc9g9pRjdU_kxURXu-5ZXQM18TnbgjayrkPtrT_t4-HQWwFkoYO6P2E8RsoxY8VGfqCx3VfBNP3LDcsxFKp7e7ZTsu9-ZxCwUiAFxJw9KTjQeTz1bGA1lvw-7mUZft8vabpMzdep4Qs0wmTReA15_dxrQSXut4X9L2jbJ7sJa8SdlMtYCqCc8PDYPw5n49Ltxpq5E6_xWGR_9rtmECrctbG-0Sgqre9MF0KaKZgiRgg4gI9eiQ6vplofW5ppgJo51vo1BkJZo2tPSZStzFHpY6Gtl7Cq7ZHPZbLT2_j1UB4RDHHyoeec3ULCRAEAYSJOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: بیشتر موشک‌هاشون رو از کار انداختیم، بیشتر پهپادهاشون رو.
🔺
توان ساخت پهپادشون رو حدود ۹۲ درصد از بین بردیم. توان ساخت موشکشون رو ۸۹ درصد نابود کردیم.
🔺
یه کم توان براشون مونده، اما برای ما هیچ توانی ندارن. این دیگه تقریباً یه درگیری نظامی کوچیکه</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6089" target="_blank">📅 08:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6088">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3962370842.mp4?token=LMpBJhyAhRnE2uyKgU1N_21CZLyFrCzEkVqWvSSD-GN8wCTuS-rm1C-sS2xK7qyLvelGJZFEcr4GmBg_S4lJ8ksFIiPfkOaLb00rprrWI-ZAzBrVN2R5QD6OdhDS5Wza8ETiKdMRQGp3JD-2v84yJ5voTKK-1cZTN42krfjDQeWFDXB-fk2b08rrqOYCQoWt71bYwE8DNLG8reaEF96Xqs4LcbeFtvZ9aCXTcbQnydMaf9C8JplVnPznLaSh0jN95Z7EQrWBznMKaa-Lld5R2BFaXPgCwharifNTtMPVDbEQsRlXt2yEPC0lG6G1KaIiomn9BC_XZWEIW_JK-3RjYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3962370842.mp4?token=LMpBJhyAhRnE2uyKgU1N_21CZLyFrCzEkVqWvSSD-GN8wCTuS-rm1C-sS2xK7qyLvelGJZFEcr4GmBg_S4lJ8ksFIiPfkOaLb00rprrWI-ZAzBrVN2R5QD6OdhDS5Wza8ETiKdMRQGp3JD-2v84yJ5voTKK-1cZTN42krfjDQeWFDXB-fk2b08rrqOYCQoWt71bYwE8DNLG8reaEF96Xqs4LcbeFtvZ9aCXTcbQnydMaf9C8JplVnPznLaSh0jN95Z7EQrWBznMKaa-Lld5R2BFaXPgCwharifNTtMPVDbEQsRlXt2yEPC0lG6G1KaIiomn9BC_XZWEIW_JK-3RjYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات شدید به کنارک - امشب</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6088" target="_blank">📅 01:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6087">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
ترامپ : حملات جدید می‌تواند برای دو یا سه هفته ادامه یابد.
🔺
سنتکام : موج جدیدی از حملات را برای سومین شب پیاپی آغاز کردیم.
🔺
باشگاه خبرنگاران : ۷ انفجار بزرگ‌ در بندرعباس</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6087" target="_blank">📅 00:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6086">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
شنیده شدن ۳ انفجار شدید در جزیره کیش
🚨
انفجارهای شدید در جم - بوشهر
🚨
چند انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6086" target="_blank">📅 00:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6085">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
ترامپ : امشب و فرداشب با قدرت به ایران حمله خواهیم کرد.
تفاهم‌نامه آزمونی بود که جمهوری اسلامی به آن پایبند نماند.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6085" target="_blank">📅 23:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6084">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">آمریکا سفارت خود در ابوظبی و کنسولگری‌اش در دبی را به دلیل نگرانی‌های امنیتی، تعطیل کرد.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6084" target="_blank">📅 23:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6083">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgmhSdTCNHtiG7GokqVLVXL_eileHCdLxMNgGJdIiYf1voPF4A-aiTLgttP7aeELHWdTxBIupTZB28ouaNbuANueC-_JrV1v8A34Vw4Awg62DaROG_eFQDbKSzjmOAsvYJFz427-8qqIfT2ggv17aJbJ4kN9JUO5Z58-YZK6DYrVryG4H0T70c7XMALThZXxb30pQIT7Ib3Av9pXW5Dml4wVI7KBsVmZejUpdmX8gI4IjvH9KVjf4PdeHShD1WLIpyjKYRas_w6TdZUI7XI68U2LmUZK6q6PUQw8TeSURFZX96X0f5uZuBOCK5g8YAqgGDo9-LwH8_6Xr2H_IeYxyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
انفجار در چابهار و کنارک</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6083" target="_blank">📅 22:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6082">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/645219e055.mp4?token=ptr-lZfbISJ_xEBoFb3DkMvC9wj7a9po_WAsMwtlqsuKsnrV7nHkXsKInZOnzSc2DSABXQgxHrV9pJvFYvRgf6E77rCynUv1mmQaRJk-0rVfsJ9PeHyz5ijUsfeZYDhL91X7Wm_TUn0WuEcYj82snv8kHMBoW4Nun_E2t7lnDzjv1sUIpZaElazOUSVnvqYsEbOEfrRW-Qo12CYu3hNYXg6LMCcH9zT-WZeraQFK7z2RW62RzoV1hmU8opJIJSjGdrhCSIlVLc5H9xTD1b07yCUUfbXXFbhxgyafR7xU7btheXS3RFtbdmN-Ohp977l8zc8W0suZgSzRo1aXV6ZzwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/645219e055.mp4?token=ptr-lZfbISJ_xEBoFb3DkMvC9wj7a9po_WAsMwtlqsuKsnrV7nHkXsKInZOnzSc2DSABXQgxHrV9pJvFYvRgf6E77rCynUv1mmQaRJk-0rVfsJ9PeHyz5ijUsfeZYDhL91X7Wm_TUn0WuEcYj82snv8kHMBoW4Nun_E2t7lnDzjv1sUIpZaElazOUSVnvqYsEbOEfrRW-Qo12CYu3hNYXg6LMCcH9zT-WZeraQFK7z2RW62RzoV1hmU8opJIJSjGdrhCSIlVLc5H9xTD1b07yCUUfbXXFbhxgyafR7xU7btheXS3RFtbdmN-Ohp977l8zc8W0suZgSzRo1aXV6ZzwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏آمریکا با استفاده از سه قایق بدون سرنشین (شِهپاد)، پایگاه دریایی دیروز بندرعباس را هدف قرار داد و تأسیسات نگهداری زیردریایی و کشتی را منهدم کرد.
این نخستین بار است که نیروهای آمریکایی در نبرد از قایق‌های تهاجمی بدون سرنشین استفاده میکنند.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6082" target="_blank">📅 22:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6081">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‏
🚨
🚨
محاصره دریایی ایران از فرداشب ساعت ۲۳:۳۰ دقیقه اعمال خواهد شد.
‏بر طبق قوانین اعمال یک محدودیت تازه دریایی باید ۲۴ ساعت قبل از اجرا، به صاحبان کشتی‌ها اعلام شود.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6081" target="_blank">📅 21:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6080">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be724e9f8e.mp4?token=IjCiLR542HYKw6XD_fFP_aE6l0lXjGRAa_hOEigIKcCDYGRsLhp_5dzWkHJpvYJ38kBHsox75mTagxC03Vkwff23h6Hmn3ACxdvC846n-1duB1Kic55s7O6LIGSxAhgjs5fFfG84mpBImL3EWawP1FQ9Z8Ywl62Sins_06520uJTV7WOn7cYyTCVj_AqCT6Iw0yHmMfHdxp0qHclPKVzpdk-Hfp52SIuJ-_7vzU_S-B2BNV16SwpMuHBU6yvRve-QoansoDJRf7MpDR9JwJ7xK4sg4hm1EShGpTIZvL9F4GvMBYUJW6B-mfDX9RHhI-cBxo9PkC6YgX4_O7W8pnNLKzzLNtNfQ2fmGLnxd84b3vf3cEoL5Q81sTBStP1ww426dLQTciWTblBZoK8jBQ--ZbchtdwNDfUrKO4mK7gPwRD_3DrfMIpkOGa_cFYY3nNWau0x_5fGKW85ucGECUhWpoLVy5qiV_bxFJ5G13ob3ac6GZBLMakpqCTckhsJ4EOx6VrN_iXxJHjqptnl7ZSN519Y2WLb78qnmFKrqTQU5GWGhdPHCjF0y814_-jqFvS2ev6pG8Q74W4NRGH6ulHxkBEB39YxR9GMQj2vpTift4TFymNcei69fSLerFC85_4Bpzd7nK1PoheDY66Y58_yrq1MyOv-I746_EXFSrAjzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be724e9f8e.mp4?token=IjCiLR542HYKw6XD_fFP_aE6l0lXjGRAa_hOEigIKcCDYGRsLhp_5dzWkHJpvYJ38kBHsox75mTagxC03Vkwff23h6Hmn3ACxdvC846n-1duB1Kic55s7O6LIGSxAhgjs5fFfG84mpBImL3EWawP1FQ9Z8Ywl62Sins_06520uJTV7WOn7cYyTCVj_AqCT6Iw0yHmMfHdxp0qHclPKVzpdk-Hfp52SIuJ-_7vzU_S-B2BNV16SwpMuHBU6yvRve-QoansoDJRf7MpDR9JwJ7xK4sg4hm1EShGpTIZvL9F4GvMBYUJW6B-mfDX9RHhI-cBxo9PkC6YgX4_O7W8pnNLKzzLNtNfQ2fmGLnxd84b3vf3cEoL5Q81sTBStP1ww426dLQTciWTblBZoK8jBQ--ZbchtdwNDfUrKO4mK7gPwRD_3DrfMIpkOGa_cFYY3nNWau0x_5fGKW85ucGECUhWpoLVy5qiV_bxFJ5G13ob3ac6GZBLMakpqCTckhsJ4EOx6VrN_iXxJHjqptnl7ZSN519Y2WLb78qnmFKrqTQU5GWGhdPHCjF0y814_-jqFvS2ev6pG8Q74W4NRGH6ulHxkBEB39YxR9GMQj2vpTift4TFymNcei69fSLerFC85_4Bpzd7nK1PoheDY66Y58_yrq1MyOv-I746_EXFSrAjzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی جدید قرارگاه مرکزی خاتم
در خصوص تنگه هرمز
ویدئو رو باز کنید و به چشمهاش نگاه کنید :)
یک دقیقه و پنجاه ثانیه پلک نمیزنه
ابراهیم ذوالفقاری محصول هوش مصنوعی :)
یک انسان عادی، هر ۳-۴  ثانیه یکبار پلک میزند، در یک دقیقه ۱۵ تا ۲۰ بار</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/farahmand_alipour/6080" target="_blank">📅 20:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6079">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DqS1hEL3Jr37p_gW2X-tLcVvB-FXQ9sucMDKdIIn2aprp_yeH44gnHjwb-T2A6TLO5zHMNa1f6bx3FGGvc2qFmTL48T2ECwA03uaP0EBEfejc7z4nPFYOv3nFL6VpeX3zuVTkdU8kr7db-YAWE9rGMU26jgisjtPrfPRpZXLvvGIhCS1Ar9nxeRLBDzo-X-Tc-X2Pe_0nl3pQLpdHzGTjlA5ctq5xWMz75l4hp7TTZ8RjRuF4i1CEbUKBlrWdaN0_hudq0yl_Jvb-dkwpm-kjIKAqXmIr6oQxGEKFvcVgJ-Y_B7Mj-0dcV4-dYjHDYSLdr_XwMY8GG8_uDt97YvU8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qw_Hmy3HWHyWvKroorZ0g71mKOE5bPeEXpl3pMWrcxU2x0I89z2xztzNibGi70shXnb2abot_eoCJAOEbT8qNTWlNI3U5-TKM4NmDtnBA4QAXZOcCgLKEBOHNi49qapvVK4g-PxCnTJaE2sLc0lrAhv-_ngyuBNSQAAOxPANeFIgA5pMcnw42bBFU33Rljvq3qJnU-fHFwWSfoyu9B54T0e05Ozi-riIlcJ6dK7bvKN9vhC6AC68th8e-aArE9e7rfEdtz3nTEhy2gzsbZveNBDndq_BqaRWzDbMh5EDH8_8yuwgEJlHUJO6uUeFTRA4H26C8nMhKYts3Zll_GUCQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6078" target="_blank">📅 17:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6077">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQisjFZObV5lsPsJEQPiL6Gu6aWPyI4w7HY2-a43pDkEclPi4Sm9RmfBpBowqNU6mHm_KZ2znPPh7Iy_iGHejzh7qmYSIFYo-lFCQGFtF0pm3Ijbqs2eYkaZPSGriCaQSnnMSA_YbBDGGZDKhVbLUVzyu2Y2ySLcA9DXW5hCuQxew0yuT3R_SYWEwgo1Kg6ptX_XGeE9SWpFShmcxjpuTE17XK-mwED0aMPiZi634UZiNpyUNGU5rw2eIwdtSeYaFR50GwAHqPx916MYUBCboWbvZba3d4dETv5DVI_Aq04-Isfk7J-7cKVe3jHJJ1vSRqwPS9gRrZs41FQY5fnEAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6077" target="_blank">📅 16:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6076">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترامپ درباره ایران:
‏ما کنترل این تنگه را در دست خواهیم گرفت. احتمالاً مدیریت آن را نیز بر عهده خواهیم داشت.
‏ما به نگهبان تنگه تبدیل خواهیم شد و وقتی این کار را انجام دهیم، هزینه آن به ما پرداخت خواهد شد.
‏ما ۵۰ سال از این تنگه محافظت کردیم و هرگز پولی بابت آن دریافت نکردیم. بدون هیچ دستمزدی از آن محافظت کردیم، اما حالا از این کار درآمد کسب خواهیم کرد.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6076" target="_blank">📅 16:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6075">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
دولت بریتانیا سپاه پاسداران را به عنوان یک
سازمان تروریستی
اعلام کرد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6075" target="_blank">📅 15:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6074">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">عربستان برای مراسم ابراهیم رئیسی «وزیر خارجه»‌اش رو فرستاد! برای مراسم خود خامنه‌ای، ولی امر مسلمین، این بار «معاون وزیر خارجه» فرستاد :)</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6074" target="_blank">📅 13:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6073">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGmLNg8daCcV0-QJb1_qQcUj7qDPECBjh6AYiE2oWo6Eo15qX7cGosJv1qq0pEOHQ03h8m-P4LbG7q0-Y8S8vTEct6Oe942Dg-7bKMUrHTahE-okAurtzZAg0EDx-DdXNzBXyKL285hcz0kM-RCDA3l323JCv_O8k-fluouXikeJIpY6axGkwYxkpoJhPOVxGXYpsg42Kd24UZizWbEaJQLJttrFif1nYAdDX0lNtrrDmWFtf-ESrDfUr7LhKqdk14TIBaG-ddnbPn7N0C6AVzgakWWz5RzUF7AvGw9O23QSvBp-6or4Nyw3gRFR127vHNSOSRLct5RkZ6lUP8CmDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای مراسم «ابراهیم رئیسی»  شخص امیر قطر به تهران رفت،  همراه با نخست وزیر قطر و وزیر خارجه  قطر،  اما برای خامنه‌ای،  سطح هئیت قطری به رئیس مجلس  تنزل پیدا کرد! قطر اهمیت کمتری برای مراسم شخص خامنه‌ای شد! از اثرات حملات جمهوری اسلامی به قطر!
🔺
این مدل احترامی…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6073" target="_blank">📅 13:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6072">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUNS7Crpg1WQuVB7XXqpXk5bfHicLEXWO5AMcZTZiHzZva-mG9EH6rJura6KoiGKK_uaDLyolGq_FYZ4N2LFzrchSXsG8PCe0pQsD7YAXEEgGdWHSMUVwYAOBTZhAET3Cy8co_iyXTlgJYuXJ16oS-9k3OXP9FfdToCxZFZbDCSJKmadGZ5LU1enuH-oUStwdUFH3FguROzETLJjGFaq26SuTri3JPglbV-CaAwmp_C5y8KyDVfEf2S4G4XIn9sdRlv9IgFK5jsit3naLrJDyFz6Z7Wu1Ml7uB0zK3PeBKKCwfZDH1uNgQjEHnEHcUZHp8O_BPZGlR4chijbGsekmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OnNXjpQAeww2Ze4UqRrdnki1MxcqWUr7rPisUuEg_HfC70kEoMpj5pAUkSXOywvG-KnKXDcuM37M7YWZzo7jA7hvwhUYR4Zj_CIx5Ytg_iBV1dL5a5kfRHEXSS5fo7-6zwPI--IBzMId0c-GB-Fb3mSc42cs9kHlQtL5X94rXWcIdgWR08cSmrvBTed0VacIJ8vRIwbEswO1e0E_hypqOn_6IBdUCuEP37kwBsFYALxoxu2bUfKPkbX2hl73uqrsvMO5f8sICKYOxbpagwbZDZ8Yoa9wu9RB0F-60Q7MiyeT9iGUbzq_yW0NQcTIAphJZY5G9jW8wAR0_yLWOam-qw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/868ebce267.mp4?token=u5aU0GtxZcBrMIzyb3xri1dW3ZpO8EiS0xbW591L7EKOMieO_YJOJUAeJPgFnjQy5jojYvmCYElb0apvqUf6UMd36JEP0XD_Q1oF2JHA215a9T4NJ8ftwqVJCjlWJUoKd4XGRXcpdbDqCznski98s8DScFwUZK6uH0zh5X9KKOdqaVDxMfx2mJPpvYo4CFIh-kKCCDCXhnkRFxR6Uxc7TbPhOPOF8g0ZzPU9gD45MuRdSXFKV4X_F6LY9PJ4yg0yew2m3wIIM5B-zIr5WWrfKYN39i0KcETDKo755b5HUAvPR_Ncj7bgVJfR4P70q-LgfsHaL9VSs0l5i9HUCFK5qlRsxWAHmK5L_xm3Y3x4ulU7CBx-ktJmSmpC5Cdxewvt7SmUBcJjhY0NmkwoLrPLq4bnDyvCwByF6Ib1aYmhdTt-MbIOrWXfX0kBkr17TmmGq_VMp5EFLh6qxzqTpmcU4CYuBihorfkKE1I1Se0zXLIppufbO931pIPGWmJBbsg2zYNYzKZNjSfJymFlVQE8vDPRtJcpC_PM051qaE7YDXHyzA69-Qf931HjOcHPMUF3nLfXqc7Vp-kwbtBbAGgrvWReR4fLsfo_gmF0hdwVpaKazfoVKydRJx_1FEzBsAJHvyrN67bZXNjsWzgUAvFp_4-96RT0u6_cBKAjHy1M2ro" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/868ebce267.mp4?token=u5aU0GtxZcBrMIzyb3xri1dW3ZpO8EiS0xbW591L7EKOMieO_YJOJUAeJPgFnjQy5jojYvmCYElb0apvqUf6UMd36JEP0XD_Q1oF2JHA215a9T4NJ8ftwqVJCjlWJUoKd4XGRXcpdbDqCznski98s8DScFwUZK6uH0zh5X9KKOdqaVDxMfx2mJPpvYo4CFIh-kKCCDCXhnkRFxR6Uxc7TbPhOPOF8g0ZzPU9gD45MuRdSXFKV4X_F6LY9PJ4yg0yew2m3wIIM5B-zIr5WWrfKYN39i0KcETDKo755b5HUAvPR_Ncj7bgVJfR4P70q-LgfsHaL9VSs0l5i9HUCFK5qlRsxWAHmK5L_xm3Y3x4ulU7CBx-ktJmSmpC5Cdxewvt7SmUBcJjhY0NmkwoLrPLq4bnDyvCwByF6Ib1aYmhdTt-MbIOrWXfX0kBkr17TmmGq_VMp5EFLh6qxzqTpmcU4CYuBihorfkKE1I1Se0zXLIppufbO931pIPGWmJBbsg2zYNYzKZNjSfJymFlVQE8vDPRtJcpC_PM051qaE7YDXHyzA69-Qf931HjOcHPMUF3nLfXqc7Vp-kwbtBbAGgrvWReR4fLsfo_gmF0hdwVpaKazfoVKydRJx_1FEzBsAJHvyrN67bZXNjsWzgUAvFp_4-96RT0u6_cBKAjHy1M2ro" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانال ۱۴ اسرائیل با انتشار این ویدئو خبر داده که ارتش آمریکا شب گذشته با بمب‌های سنگرشکن به یک ‌انبار موشکی در اطراف پایگاه چهارم شکاری در دزفول حمله کرده است.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6070" target="_blank">📅 08:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6069">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f4228d97a.mp4?token=NQ_pH69QXAP3gy7J4PE-knX6HJ3ge8nwj9qZJZ0aLlPLUF4LQxv6kZeT_9yBwf8dnvoa1XvjQR6qavEwz_dpjlHlcQXmLfBrz5eJcnwNAADAaQpXB02xcuUJ6K4aSIRu0mT17rtb3z7TaHNRw0Sm5zmfmloQ8PT4ZWFek9SSHPllqanRfgyNj6jw_V0F1qKt_SvoUEW-QFFDf3ZzRA2tD_eYxAS6whxOvwfotGdwgzXmqLGXDdV97RxAWFOMQqsQiJPoRgw6nFg_hd_LsCQl-SmDD2o8wkEmvbHy-tuO5NFfhdE-5cZzrfsFruEgxCgZeyJkwPyiuI4I_PljF8GdkJ803skBAOYFE61zlADOXwjWE_qWQS-DLzh-VG8X3bFaRIWkhMvrN180ic6Swu8BspR8cjbwUzRSP4SX7_LK0BiHx-za_D4JT5bqV5dub6tX9Oqr9i2pupPd3r9COX0849TSvL2wKvA5e1yXCFEFM_Aj77l1i2S3kk4fRUzMPJDy4lmoHYYladr8eDDsBumwVbL6dkeA-SBoxnxVVl4nkP9d4z4hKqnuNtz9FyDoyF1WKsNCqo3oAOChSclUoNcAbRsov8rK5HLIXyR2lCZcSCZrep9gNW_Vh3ENuSSda0GJgzhdFu1hgoXuR8oS3lEWF6dDs8zRNYVWy2gJPrA0Upc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f4228d97a.mp4?token=NQ_pH69QXAP3gy7J4PE-knX6HJ3ge8nwj9qZJZ0aLlPLUF4LQxv6kZeT_9yBwf8dnvoa1XvjQR6qavEwz_dpjlHlcQXmLfBrz5eJcnwNAADAaQpXB02xcuUJ6K4aSIRu0mT17rtb3z7TaHNRw0Sm5zmfmloQ8PT4ZWFek9SSHPllqanRfgyNj6jw_V0F1qKt_SvoUEW-QFFDf3ZzRA2tD_eYxAS6whxOvwfotGdwgzXmqLGXDdV97RxAWFOMQqsQiJPoRgw6nFg_hd_LsCQl-SmDD2o8wkEmvbHy-tuO5NFfhdE-5cZzrfsFruEgxCgZeyJkwPyiuI4I_PljF8GdkJ803skBAOYFE61zlADOXwjWE_qWQS-DLzh-VG8X3bFaRIWkhMvrN180ic6Swu8BspR8cjbwUzRSP4SX7_LK0BiHx-za_D4JT5bqV5dub6tX9Oqr9i2pupPd3r9COX0849TSvL2wKvA5e1yXCFEFM_Aj77l1i2S3kk4fRUzMPJDy4lmoHYYladr8eDDsBumwVbL6dkeA-SBoxnxVVl4nkP9d4z4hKqnuNtz9FyDoyF1WKsNCqo3oAOChSclUoNcAbRsov8rK5HLIXyR2lCZcSCZrep9gNW_Vh3ENuSSda0GJgzhdFu1hgoXuR8oS3lEWF6dDs8zRNYVWy2gJPrA0Upc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
صدای انفجار در بندرعباس،
سیریک، جاسک، قشم،
سنتکام : از ساعت ۱۷ به وقت نیویورک
(از ۲۵ دقیقه پیش) حملاتی را شروع کرده‌ایم.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6068" target="_blank">📅 00:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6067">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=H9ALFP3G_TOmn7ZNoOQ4iKNdO5SwaPV4oUK1AfFGwoPUaAt0lL-S7yPaR-vzMkosc42LZq9MWbPHspsGWojiNybL_dh8rFa7Sjjz6Kt6Zlu7w3bH01KVcr4GWCXutOE5baXMe1qgJfE8escTHeLi2q0xyw-wL8H6ReipNtoqOuclMrbfJrpmiyDgGjyjqH8oWX9fRLvFNcOwFWoQTzUWKVlj8Ttq29TgbrjUpZSkZJ24nRtN4Ht1xCikB89lWs2QCvdHFaSslga352uYLBhGQztBuoGtMeZsZh6-tYHxAJAeMM3durn1iQOAAFknDdDPxumXid-_Nll-4IgbxOSPhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=H9ALFP3G_TOmn7ZNoOQ4iKNdO5SwaPV4oUK1AfFGwoPUaAt0lL-S7yPaR-vzMkosc42LZq9MWbPHspsGWojiNybL_dh8rFa7Sjjz6Kt6Zlu7w3bH01KVcr4GWCXutOE5baXMe1qgJfE8escTHeLi2q0xyw-wL8H6ReipNtoqOuclMrbfJrpmiyDgGjyjqH8oWX9fRLvFNcOwFWoQTzUWKVlj8Ttq29TgbrjUpZSkZJ24nRtN4Ht1xCikB89lWs2QCvdHFaSslga352uYLBhGQztBuoGtMeZsZh6-tYHxAJAeMM3durn1iQOAAFknDdDPxumXid-_Nll-4IgbxOSPhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات موشکی سپاه به کویت</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6067" target="_blank">📅 20:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6066">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">فرماندار قشم از اصابت ۱۰ تا ۱۱ پرتابه از عصر امروز یکشنبه دشمن در جزیره قشم خبر داد.
حسین امیر تیموری افزود: تمامی اهداف نظامی بوده است. خوشبختانه این حملات هیچ تلفاتی نداشته است.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6066" target="_blank">📅 19:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6065">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=DEmx4P-bIVldpOEfsg0aCs1Le-frf6Y_bqkSVTHWldOjIHjKYO6FnxdRh_vvwAg3u7rgcirlHHLvZYk21ZyWbv6A_sPzJigcOzmXxASyuMURJmf6NsHqqMqc3phpFz-0VcT-4cC0pWUMGz_PSaIXuxKBi-wMqCSzu6mBvg-3dAJ_M8y9AstViIHDYWQ8fJEpXDF1VPjZtDYWWsUC8RdtxRnIlSk1Z3aLO4ECSXYGHtvk3W13CR1qjZM7fIy9QCWC49Zglw6j9dTRg7qbmZerY25czH3K9xwIhMN-mlScEwbPe3Q2ba4aSpTx_1u5V81Sfx_B3dvootQB-xOaDsNqqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=DEmx4P-bIVldpOEfsg0aCs1Le-frf6Y_bqkSVTHWldOjIHjKYO6FnxdRh_vvwAg3u7rgcirlHHLvZYk21ZyWbv6A_sPzJigcOzmXxASyuMURJmf6NsHqqMqc3phpFz-0VcT-4cC0pWUMGz_PSaIXuxKBi-wMqCSzu6mBvg-3dAJ_M8y9AstViIHDYWQ8fJEpXDF1VPjZtDYWWsUC8RdtxRnIlSk1Z3aLO4ECSXYGHtvk3W13CR1qjZM7fIy9QCWC49Zglw6j9dTRg7qbmZerY25czH3K9xwIhMN-mlScEwbPe3Q2ba4aSpTx_1u5V81Sfx_B3dvootQB-xOaDsNqqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که این ‌تصاویر از نتایج‌ حمله امروز آمریکا به جزیره قشم است.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6065" target="_blank">📅 19:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6064">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
آغاز دور تازه حملات آمریکا
به شهرهای ساحلی جنوب ایران.
بندر عباس و قشم مورد هدف قرار گرفتند.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6064" target="_blank">📅 19:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6063">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">دوستان عزیز
این رسانه کوچک به‌صورت مستقل اداره می‌شه و در ۹ ماه اخیر، به خاطر شرایط خاصی که در اون هستیم، همه زمانم رو گذاشتم روی فعالیت شبکه‌های اجتماعی.
اگر این محتوا برای شما ارزشمنده و اگر مایل به حمایت از ادامه این فعالیت هستید،
این لینک پی‌پال در دسترس شما :
PayPal link :
https://www.paypal.me/Farahmandalipour</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6063" target="_blank">📅 18:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6062">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4bc671310.mp4?token=khWSyLnOS_ZDG1i4rKpIaUDVw3jN7U95cdiyk583_WiF7DF3pDoqvvtatwXKwQTMj2tClXLbsn15TlpEF71a_PwBSdXXre8pLtNrAm3jOsmselMtQ1DBN3FT7cSazfVwQAUbDSkm1Ls-MII9Vje0dQ-xgZSfHkoGRdkst0PTl3fg5X1JRE4vMv-n2Kh2av-nkWFqGxj2FTnCbgGjFkEEv0Zz7SuO4wN6rnUUY_Qe8iDrcyp0tix47TVe7ADxrq0fLeR9y25-xDM9PIXm7yFUa_HH-R8XGfDwijcCfM_RtC7_H0rhlf_uX0nouZGx3mrLb-Aa_xclYHcfocLBxgY7BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4bc671310.mp4?token=khWSyLnOS_ZDG1i4rKpIaUDVw3jN7U95cdiyk583_WiF7DF3pDoqvvtatwXKwQTMj2tClXLbsn15TlpEF71a_PwBSdXXre8pLtNrAm3jOsmselMtQ1DBN3FT7cSazfVwQAUbDSkm1Ls-MII9Vje0dQ-xgZSfHkoGRdkst0PTl3fg5X1JRE4vMv-n2Kh2av-nkWFqGxj2FTnCbgGjFkEEv0Zz7SuO4wN6rnUUY_Qe8iDrcyp0tix47TVe7ADxrq0fLeR9y25-xDM9PIXm7yFUa_HH-R8XGfDwijcCfM_RtC7_H0rhlf_uX0nouZGx3mrLb-Aa_xclYHcfocLBxgY7BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مثل باباش شجاعه :)  باباش هم در جریان جنگ ۱۲ روزه چند هفته رفت «کمین‌گاه»! برنامه‌های شبهای محرم رو هم نبود تا شب عاشورا (دو هفته پس از پایان جنگ!)  که دیگه در جنگ ۴۰ روزه غافلگیرش کردن</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6062" target="_blank">📅 17:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6061">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a80edc91f4.mp4?token=WWgZuv9xAiMxH3MQD3iYQv7nUv8sW05qQvt_pV_TTELQtXLFnwf1wjLQxLXctuE872uE8Oi94V4WE9HaOKfO8WZfhbVgTLwzbcqZIxE97j05zOAyaI8rWqhk1nwcJt-9-a1dpBy-tMhmt8EwkID19-u8yB_A_S-tqJlKScWDpGDeRNBhm3stOI2SXGT9TxrrGyUMBnvZtTv93YL4Y7bj1JbQHCXZ4aRAvspa_WsxAlpkEwXa4n8M_w7F_S7K_aSwxAuG94YhAmbqAtslGLJFOwjjzbsIC19vzqKnGj_-7NICOp1rCxWaTpl4JxAdTGqBazcvMEzoUA-C3iJJkwZEHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a80edc91f4.mp4?token=WWgZuv9xAiMxH3MQD3iYQv7nUv8sW05qQvt_pV_TTELQtXLFnwf1wjLQxLXctuE872uE8Oi94V4WE9HaOKfO8WZfhbVgTLwzbcqZIxE97j05zOAyaI8rWqhk1nwcJt-9-a1dpBy-tMhmt8EwkID19-u8yB_A_S-tqJlKScWDpGDeRNBhm3stOI2SXGT9TxrrGyUMBnvZtTv93YL4Y7bj1JbQHCXZ4aRAvspa_WsxAlpkEwXa4n8M_w7F_S7K_aSwxAuG94YhAmbqAtslGLJFOwjjzbsIC19vzqKnGj_-7NICOp1rCxWaTpl4JxAdTGqBazcvMEzoUA-C3iJJkwZEHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا بگذار مجتبی از «کمین‌گاه»  بیاد بیرون، پوستش نور آفتاب رو ببینه، شما هم به جای هوش مصنوعی، قیافه خودش رو ببینید، ببینید اصلا چه شکلیه، بعد به نتانیاهو بگو بترس.  راستی گفتید مجتبی دقیقا از ترس کی  ۴ ماهه قایم شده؟</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6061" target="_blank">📅 17:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6060">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brrpT2csKggSUxb5EKeSzTlZn3g9QSXXYZmJSKIrLVVF8DgjPowZLbBIfJ2xtdCBU6J7VFf9qMa_Yfe1XXmC8E2zzjl5yriFm_t9FmCqeRfYXV98wriQZ7Ym3zWmy1FLjoaG6SEwWDF68Buu0gkpVHucXEVWx8bifsT06TJyEIL7ZjH3Ku9SJSFo6qThuBu6Ph5HOoR8WftGJ289bYwIgUebV646y16WoZ12YHL1YZYWnk_WRyNRk1Mx2U-_Ao5Al2ZW_Wkz-caULWcz10SB23kZ8PeuZc_RBWpYuo8yHvCWiPGWs-O9PJcQBjL89Ms_fe_OaGn9c7nCHT67wijSKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYa5qLXa0Grx-nCtLXpe5MGmL_AlqLfQHtObhmsmiiyNwhT58flkyW10rU6lkfRbWRVfHAeILuEtLx1_CylSC6meUJ7dSwBG116Gyjwjw18G4oE6E5GHDAinWD88HoU_CBGzdsU8huX7VNxCqLPZStuQalHadAq82WjzxXB5VtJBLQRlD_OPv1kyKpLXJMfsjkrr1Bzbjz150nOMxUvoI7pX7soj79PoOnUoIzMrThnUMlaQfkDfhKDVN0Fo64Ygzu8XSG8Mavegm5H3sBzS8ypwTkRj6-fFNx8TFSRlEzGqRjAcSIOpp0JU2u1t1zGZ0DReiIlRr0AJeMBNyoEzUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشهد  از فردا : روزانه ۲ ساعت خاموشی برای منطقه.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6059" target="_blank">📅 16:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6058">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec46cc2c8f.mp4?token=vZDtjDO0dFoU6c5odS8zBUzaYakmcKVdyK9rkuBiygpeSC_6_1qaY9atzZoUuVz1LLadWO8y3lVizSssXpShtPo-nq6uHFZvKyucFSGXi0808llO--Ke2xFgJwHwKTmDaSorLmKsu1t69x9ojkdYL0Rv0P-wKVu1HDzZJxUzIVLWe_O95Dgbf_eL3vkCRcemFwQa04JiGofCXTGn0Y5CdPI0vgp6hBzOpU4Fm7uiCM6YI7bC25DBfrOTITlSlgYydQZ0HmJCqvyqD6FJBCIFolITt9pHDlnh3J-slDpd-iiRMuTYAGu6JtRdxQoOWkaRghIXlwt2iYECMOLUce4utQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec46cc2c8f.mp4?token=vZDtjDO0dFoU6c5odS8zBUzaYakmcKVdyK9rkuBiygpeSC_6_1qaY9atzZoUuVz1LLadWO8y3lVizSssXpShtPo-nq6uHFZvKyucFSGXi0808llO--Ke2xFgJwHwKTmDaSorLmKsu1t69x9ojkdYL0Rv0P-wKVu1HDzZJxUzIVLWe_O95Dgbf_eL3vkCRcemFwQa04JiGofCXTGn0Y5CdPI0vgp6hBzOpU4Fm7uiCM6YI7bC25DBfrOTITlSlgYydQZ0HmJCqvyqD6FJBCIFolITt9pHDlnh3J-slDpd-iiRMuTYAGu6JtRdxQoOWkaRghIXlwt2iYECMOLUce4utQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوینده شبکه خبر جدی جدی
خبر درگذشت لیندسی‌ گراهام رو دوبار خوند :)
فکر کن تاثیر یک سناتور آمریکایی رو
در برابر کل نهاد مجلس خودشون که ۴ ماهه
کلا تعطیله و کسی هم اهمیت نمیده :)</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6058" target="_blank">📅 16:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6057">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SjA9H47uxr92MdSzARx5mg4Lp5iHGy_Fus45Q-0ODlIM5th2xXDchjd9vt6C20yvlELRFQtJawxTMItNuvTVouPJORxcX5uTSymzHf58liY7VSyvtOnLBlov9hu5buwv-4WlL0GqG8LIf7HJjXNR6WA6yvKsbVp6z0KtTl7avQTj590XsKHZnCmaEC8huSjfzs0nrQm6kzXbbda5Ty-p8ltdHLyOrdHYK8bpy_hPI7jp9YL_UPIDI-E1fvIYVz6PDLd_PYujGy2zzheoFxLxz1_aZhp5iBVh1wHPreKxqo2RDFpPYwoztGKWaP9LRaTrZfX8ZJtcjI5XUQDy_FLCSA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">رقص بر‌ روی ناقوس یک کلیسای قدیمی - توسکانی - ایتالیا</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6056" target="_blank">📅 13:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6055">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6675c3ed5c.mp4?token=dK30zPc4GOZ3q9fcvchMULRL3V14Nv-h761Es3sTjH9bEHSQa9WRYY3Uu4eMSxP3Hw_ixsLXUMog_PedR3vqhJr5PoAOYgfXnxkfueQM4WJu3VzL7JCvR6Z09bCYqusAdHOER_AjX-vodP73oXmYCla0PFFrSgQlS0JkzbpydDDnUIOyTjh8lX0uWmzyHyNMKSNkiLNTLO0SIZe0oDggsAFn4jxycejLAg0eucG5VG50-TeRp7TBMWppUNBYt6UZYqXwI494SlJRLg50DzoLtGPT5Jpi77WJ_wvhHLzjt0y6uSop5ZMz8AiaEeaKMj-hty6QZYYQc0NAVTSvUVN63A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6675c3ed5c.mp4?token=dK30zPc4GOZ3q9fcvchMULRL3V14Nv-h761Es3sTjH9bEHSQa9WRYY3Uu4eMSxP3Hw_ixsLXUMog_PedR3vqhJr5PoAOYgfXnxkfueQM4WJu3VzL7JCvR6Z09bCYqusAdHOER_AjX-vodP73oXmYCla0PFFrSgQlS0JkzbpydDDnUIOyTjh8lX0uWmzyHyNMKSNkiLNTLO0SIZe0oDggsAFn4jxycejLAg0eucG5VG50-TeRp7TBMWppUNBYt6UZYqXwI494SlJRLg50DzoLtGPT5Jpi77WJ_wvhHLzjt0y6uSop5ZMz8AiaEeaKMj-hty6QZYYQc0NAVTSvUVN63A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه اعلام درگذشت «لیندسی گراهام» سناتور آمریکایی در صدا و سیمای خامنه‌ای</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6055" target="_blank">📅 11:58 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
