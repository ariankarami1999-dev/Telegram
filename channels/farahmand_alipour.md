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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 18:00:25</div>
<hr>

<div class="tg-post" id="msg-6158">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ایران که ۴۷ ساله که در آتش فتنه اینها می‌سوزه</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/farahmand_alipour/6158" target="_blank">📅 17:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6157">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">سخنگوی قرارگاه خاتم : هر چه در منطقه سالم مانده از نجابت جمهوری اسلامی است!
ذوالفقاری: «همه آنچه که بنا به نجابت ایران هنوز سالم مانده، یعنی تمامی زیرساخت‌ها در منطقه، زیر ضربات پولادین نیروهای مسلح مقتدر جمهوری اسلامی در هم کوبیده خواهد شد؛ آن‌چنان که اثری از آن‌ها بر جای نماند و گویی از ابتدا وجود نداشته‌اند.»
سخنگوی قرارگاه مرکزی خاتم‌الانبیا همچنین دخالت آمریکا در تنگه هرمز را «خط قرمز شکست‌ناپذیر» جمهوری اسلامی خواند.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farahmand_alipour/6157" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6156">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6156" target="_blank">📅 14:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6155">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Riol4wSvSsZ_4jpoqTaWzKjCqDe0J-Bo4G3BciOG0tl2HwJP8UlzFohqSIxvOsR4jmyClWMfr3COK--VLWcJR3i_BRrb87uRAytQJhO4MPZmo1GzqFRZ_6aBsEekQb6G5WKNAyLO55uvx7kGmR6SYykyzgMN4NajDSEyQJJjjyDuAt_GWDJjkzwNwnl2jNsOua9zohT03Cd5gMz8x8bw1joVO8MINIGeUNQ0uCqR_qzdeVqS17v8X4viO8_jBOifggeyUnkWjUOuGsht2B8L-YwNihxbhWzT1pfUnKFUoEkagIWMlo6EAqieaeVkWaU-KG0GI4g2PWTbX-NULLsANA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وراجی نکنید  بگذارید بجنگند که صلح بیارن :)  مثل صلحی که ۴۷ ساله در لبنان  ‌ و غزه آوردن!  انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6155" target="_blank">📅 12:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6154">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">وراجی نکنید
بگذارید بجنگند که صلح بیارن :)
مثل صلحی که ۴۷ ساله در لبنان
‌ و غزه آوردن!
انتقاد از خامنه‌ای عین بی‌شعوری است!</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6154" target="_blank">📅 11:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6152">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=B6l6tcnpcRSRD8hFnPU3zmK-6zSqcTSGbXMVzoJDsVEDoiYqb2-DEAj1PT8uHradLneRzGbBn65HVXtDnT2oiTFMrJ8ZerKtHvWGKj6OKspECzgt3AgpBCPTHlTCjINp-ZtU_SbYEkm0DefKAxp0-gPqprzHNcgw8xfjcO5nm-v9WObvs5qzu_Q4yWaoXClQZa3M4ug881VcdgdmHljFUFDIYMIi1zQrEnp9E9NM-IsX7U_N-GvkiZ3dmvkliTGE271GicLpkHOQ6jklsCoSfA8JAs-RKrRX32ZhQLAyDzOUzFyNucQs4WWVTHyfnOlwkxQtDIBbQDPjVTZybcw4lCAEej1yRzAS0zy7zy8CCBQhNWNXIY9bk5R3gqVpzktsUJ7hSlv1ccjv_-oM7E0bH6Pj9vQhQ4aHlOQHFHYWo815qx7DsefdKX3glTCn8jy-2ex8d4vHe0o6l0V8F9H6Bt-6zeQ-LJuvWD-y3rWYJ7U8-8351Gml-Krr6ntPimOXN4dVE7u6dSwiMIEvOEZbFfxMYy3Q-xQ6Q8Ef3ZtnSTh-P6dFZXSW7-EHkp5qJZ0ezxm8Z3LraNPQ5IN-IwKfNu_f4oVKeHPaxn5dhf1mnVxM9O3Yn3lPMfhC_-jaI2ygs3pidr5DPzWWldp3llYtnbA2QPhvNVeytqSPHGYKjcU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1933ad174.mp4?token=B6l6tcnpcRSRD8hFnPU3zmK-6zSqcTSGbXMVzoJDsVEDoiYqb2-DEAj1PT8uHradLneRzGbBn65HVXtDnT2oiTFMrJ8ZerKtHvWGKj6OKspECzgt3AgpBCPTHlTCjINp-ZtU_SbYEkm0DefKAxp0-gPqprzHNcgw8xfjcO5nm-v9WObvs5qzu_Q4yWaoXClQZa3M4ug881VcdgdmHljFUFDIYMIi1zQrEnp9E9NM-IsX7U_N-GvkiZ3dmvkliTGE271GicLpkHOQ6jklsCoSfA8JAs-RKrRX32ZhQLAyDzOUzFyNucQs4WWVTHyfnOlwkxQtDIBbQDPjVTZybcw4lCAEej1yRzAS0zy7zy8CCBQhNWNXIY9bk5R3gqVpzktsUJ7hSlv1ccjv_-oM7E0bH6Pj9vQhQ4aHlOQHFHYWo815qx7DsefdKX3glTCn8jy-2ex8d4vHe0o6l0V8F9H6Bt-6zeQ-LJuvWD-y3rWYJ7U8-8351Gml-Krr6ntPimOXN4dVE7u6dSwiMIEvOEZbFfxMYy3Q-xQ6Q8Ef3ZtnSTh-P6dFZXSW7-EHkp5qJZ0ezxm8Z3LraNPQ5IN-IwKfNu_f4oVKeHPaxn5dhf1mnVxM9O3Yn3lPMfhC_-jaI2ygs3pidr5DPzWWldp3llYtnbA2QPhvNVeytqSPHGYKjcU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها اگر نوحه میخونن و مداحی و رجز خوانی و.. برای کودکان غزه و لبنان و میناب و….. از تاسف از دست رفتن زندگی نیست! میخوان در این جنگ بی‌‌‌‌پایانی که با جهان دارند،  از جمله و در صدر این‌جنگها،  با خود مردم ایران جنگ دارند، سربازگیری کنند! تا نیروهاشون بزرگ‌تر…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6152" target="_blank">📅 11:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6151">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">تمدن اسلامی! تا زمانی که توی مدینه و مگه بود قادر به ساخت «توالت» هم نبود!  مستراح هم نداشتن !! اما دنیا در چه وضعی بود؟  ۶۰۰ سال قبل از تولد اسلام!  توی بیشتر شهرهای جهان  داشتن توالت عمومی! اجباری بود!   اینها میشینن روی منبر  میگن «مدینه فاضله»!!  حالا…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6151" target="_blank">📅 10:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6150">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">تمدن مصر باستان رو مطالعه کنید ابتدا تا انتهاش بر مدار مرگ بود! فرعون از زمانی که سر کار می‌ا‌ومد به فکر مقدمات مرگش بود و قبرش بود!  هنر و پزشکی و علم و مهندسی مصر همه بر پایه صنعت مرگ بود!  مومیایی و اهرام و جراحی پزشکی و….. همه برای کار و کسب مرگ بود و…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6150" target="_blank">📅 10:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6149">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bInibF3peiLlxkW8UF3xqJyasj6hZbHKQ5_zaIodU6-wu95PjUz-ARmzyErw6NSUfWQi-L4gSj8U-x4xR3DFD0O-inPbsvgzJNJ-Tk-cWUh6fFHVK6v_K6n0ZyoCLaeaugSindc8RGDAkIOqohSUzQwk1MMXwMC30t2rUAUnjcq5Xado7XHAU0cipNgjXQzEoCJZJ-hhsCWpy57tYR-g8YO1hrYNMQEnsGQFGsIuMpes7DcsSFsYHa1tSctbeagFAmKrPTyqsKLK3bFbkA1VqzUTrBcV4pzLpX3p1UlNuDbBbwQN-QsDwRmJY5vqcop-O6bcZqNb8QgNvnCva65LHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها شنیدید جملاتی با این مفهوم رو که زندگی و این حیات «زندان مومنه»!  آرزوی اینها مرگه! مرگ براشون رهایی است!  اینکه برن و برسن به بهشت و به زندگی!!  مرگ رو آرمان خودشون می‌دونن و زندگی و زیبایی‌هاش  رو پست و حقیر معرفی میکنن!  و اینکه باید دائم به فکر مرگ…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6149" target="_blank">📅 10:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6148">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اینها اگه می‌بینید برای مدرسه میناب و…..  سر و صدا میکنن، فکر نکنید به این خاطره که «اصل زندگی»  رو دوست دارند. و از مرگ متاثر میشن!  تمام هستی اینها :  مبارزه، جنگ، کشتن،  کشته شدن و….. است!  زندگی براشون چیزی نیست جز  «مبارزه  برای عقیده».  و خوشحال میشن…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/6148" target="_blank">📅 10:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6147">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6147" target="_blank">📅 10:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6146">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S67FAPbGcSIj2mIMHB3rweXRNd9SeixdnSv8uvrcwW8nnvOtbl0mhQ95jnqSUYbjvGfmho4R6Ei5xQ40o39fj6JfxvGefHFtdDyo6aRh04UmLkVAAsInsKYlzqmuJQs-18faNQ3hC2c7FxONqK1LlxGO-S1wt1buPHFkbTI0qzrEdES4bLTCIb1DLuPjKH07FY6wjWt8Eij3kbViicG7zHZ9WI0tf7C-ipY4FwP2EijBmkd7tORJMqhhusXvszV6kuPkLvoCs7cJuq5qjLeuY_2tMU-eNnXll7N5m2QAlPS0koNASticS7RQENihNJiJvW3sqJXqvNtUahktGgzXuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ایران به یک شهروند زن آمریکایی که در دسامبر ۲۰۲۴ در دوران رئیس‌جمهوری جو بایدنِ خواب‌آلود به‌ناحق بازداشت شده بود، اجازه خروج از کشور داده است. او اکنون در سلامت کامل در خارج از ایران است. ایالات متحده آمریکا از این ژست حسن‌نیت ایران قدردانی می‌کند.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6146" target="_blank">📅 09:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6145">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6145" target="_blank">📅 09:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6144">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">استاندار مرکزی : شب گذشته به دو نظقه در اطراف شهر خنداب حمله شد.
این برای چندمین بار است که اطراف شهر خنداب مورد حمله قرار می‌گیرد.
نه آمریکا دقیقا مشخص میکند چه اهدافی را زده و نه ج‌ا می‌گوید به کجاهاش خورده.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6144" target="_blank">📅 08:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6143">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اطلاعیه  ارتش:  سامانه‌های راداری، سامانه پدافندی پاتریوت و مخازن سوخت آمریکا در پایگاه علی‌السالم کویت را هدف قرار دادیم.
‏ رادار‌های سوپر هاوک، تأسیسات و سامانه‌های پاتریوت واشنگتن در پایگاه شیخ عیسی بحرین نیز طی حملاتی، آسیب‌های جدی دید.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6143" target="_blank">📅 08:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6142">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
استاندار سمنان : به بخش‌هایی از فرودگاه سمنان حمله شده، کسی کشته یا زخمی نشده.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6142" target="_blank">📅 08:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6141">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAn2Rhw6MG6nUjkdmcJSlFMjL-HZVXD_LhnzWuhO6nAT7foyaLOQhDi7Fpk3aDpNU_YRpLkVFdOM2d2AQUnLueSAd28tre0PkbGARbX6AbalhclNxd9blwOmYQPwBfOE8eHEUtslFt_JkQuKPSxFKih_wrX-reObp9UPdFTCZxQBizFwDmJs1ZccE0-wh-ZItW4uMHGXMFV8VTxh00qbSs6y6G58R2DF51lOtxcxWXH7VNkJ-6BYxkMSbs_VWmyQ4CfdDkbXQlK-Qrch_3Pjc9ox2-uy9k8D7ht7_ySacrDYQvwv6aUddBJx7z8GXAHo7RPrvowI3N-LssBt5r__Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین یارو خودش از دست سپاه و نهادهای زیر نظر خامنه‌ای  فرار کرده و به آمریکا پناه برده!
و آمریکا رو خونه امنی پیدا کرد برای زندگی و نوشتن از اینکه اسلام چقدر زیباست و خوبه و سعادت انسان رو میخواد!
حالا از همونجا به ج‌ا میگه مبارزه کن با آمریکا! مطلقا تسلیم نشید! تا انتهاش برید!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6141" target="_blank">📅 08:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6140">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">برخی گزارش‌ها از تداوم حملات به اهواز خبر می‌دهند و اینکه تاکنون ‌۹  انفجار  مهیب در شهر شنیده شده.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6140" target="_blank">📅 23:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6139">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
چندین انفجار مهیب در چابهار و بندرعباس
🚨
کویت : امروز ۲۱ پهپاد و ۴ موشک شلیک شده از سوی ج‌ا را منهدم کردیم.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6139" target="_blank">📅 22:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6138">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای ۲ یا ۳ انفجار در اهواز</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6138" target="_blank">📅 22:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6137">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1IRIhMok3xsIlQAiQSYxJYWubrCgyya2gHbNsRAwnnq3-wKqo-DcDjeQHNEzHNtTB89jeCvWltrb61PK1cr95znfSRukDWNlcOmx0HjxL24aqcfS-D5vx1ZEIFj0UO_RIafa9x1z8G6WSiQzsHPyK2MHBWoXNrEhKVzIgigaeCaNTHHoD5xADbRbJP-V6QNhQgLNuxK9aS_vETJ5ckRT6CLLJQP6ZkIM4eAT8ofx3AKPHeaVY5ZwBgJ3MZoXzZU_-nRTpq0rglt1dFNonbmk4kAszGpcrqSTDaEQ2QB1AKOmjH4EPGSPZxVHkVgNJVFIXfsHlJy7faUnONVhsb7Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شما دیگه جرات حمله به اسرائیل
رو ندارید! خودتون هم خوب می‌دونید!
این ۴-۵ روز هم به همه جا حمله کردید
به جز به اون کشوری که بیت‌رهبری
رو زد نابود کرد!
و نشون داد دقیقا کجاست که سست‌تر از لانه عنکبوته!
ولی هر چقدر دوست دارید شعار بدید!
اون حزب‌الله تروریست هم رفت انتقام بگیره  هنوز و همین امروز هم نیم میلیون نفرشون  توی محله‌های مسیحی و سنی لبنان آواره شدن!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6137" target="_blank">📅 20:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6136">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">آنچه شب گذشته در بمپور رخ داد و موجب  کشته شدن تعدادی ای نیروهای ارتشی شد، قابل اجتناب بود.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6136" target="_blank">📅 20:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6135">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e615d142.mp4?token=PuhN3o-_Z0tf9rFkrulA3O9EWUKixlKn_edSeR81HpeWIGwx6sfetmw9SOmYjQIWTpazwrDVEC64e0J99DqoqGihTmIZ9rXa4bXqHSySaJ7TnDhmGuJOxXgwA1QUfN3cdQBvnT8KRjYVUQqvO9rykNzpZnxVZQHw-nxM3DgFOvpNFHF6hGcAcvFToLy4uazaFh1zEol3kOOTY09AT1aJYkY40mc1qAS2MCigxgU0I3zQGTJo78YIU849dH1mPzGB-wEaN99s4rtS7PE7WZ_0uYuP08wTJML4arx7VdC7rFxX_XcG8f5ZE8L2y2UxmmwtCSaWqSZ4vnxmR5jWAHz3ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e615d142.mp4?token=PuhN3o-_Z0tf9rFkrulA3O9EWUKixlKn_edSeR81HpeWIGwx6sfetmw9SOmYjQIWTpazwrDVEC64e0J99DqoqGihTmIZ9rXa4bXqHSySaJ7TnDhmGuJOxXgwA1QUfN3cdQBvnT8KRjYVUQqvO9rykNzpZnxVZQHw-nxM3DgFOvpNFHF6hGcAcvFToLy4uazaFh1zEol3kOOTY09AT1aJYkY40mc1qAS2MCigxgU0I3zQGTJo78YIU849dH1mPzGB-wEaN99s4rtS7PE7WZ_0uYuP08wTJML4arx7VdC7rFxX_XcG8f5ZE8L2y2UxmmwtCSaWqSZ4vnxmR5jWAHz3ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیش بینی تاریخی بختیار
در دو کلمه، برای مردم ایران</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6135" target="_blank">📅 20:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6134">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=Fp_BNSRlri1TdSh5LxFyh5aKxKV3Xx3ZE_Pf3-guvUHWJ0m51dUzJLoPoowZpLiAvwXnp01GJkEvyYWjgU01HMUYV8mP7KjBXC8LNa-syECuLwWjCm-r6pl-IuSYbZ63uuKXgEHiOfATHpNhXrYEtlZXUd-lQ5Xa35KhM9BqiEfSlgMvNKQFpBVF4kJ_dVJP2qs-A049qS3VVUienMqx8jC3b6lX6_oQQn-Dsv0Zb6cMmyBGF8rTkwdPDVOY-qFgMAWcl7BryFZ9PveAHRgc-4iW9-Vj5gQws5H6IE3_UjUMl-GDqJOIPN-oGleq7xKEEsnBM0d3nh9g5Cne_hsPSYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/296fa239b5.mp4?token=Fp_BNSRlri1TdSh5LxFyh5aKxKV3Xx3ZE_Pf3-guvUHWJ0m51dUzJLoPoowZpLiAvwXnp01GJkEvyYWjgU01HMUYV8mP7KjBXC8LNa-syECuLwWjCm-r6pl-IuSYbZ63uuKXgEHiOfATHpNhXrYEtlZXUd-lQ5Xa35KhM9BqiEfSlgMvNKQFpBVF4kJ_dVJP2qs-A049qS3VVUienMqx8jC3b6lX6_oQQn-Dsv0Zb6cMmyBGF8rTkwdPDVOY-qFgMAWcl7BryFZ9PveAHRgc-4iW9-Vj5gQws5H6IE3_UjUMl-GDqJOIPN-oGleq7xKEEsnBM0d3nh9g5Cne_hsPSYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی که فرمانده سپاه بود و سالها فرماندهی جنگ رو بر عهده داشت
اینجا میگه مطئنم که مسیری که در ذهن مجتبی خامنه‌ای است، بهتر از مسیری بود که شورای عالی امنیت ملی رفت.
مجری ازش می‌پرسه خب اون چه مسیری بود؟
میگه : نمی‌دونم ! نمی‌تونم که ذهن خوانی‌ کنم!
فقط می‌دونه خوب بود :) یه مشت چاپلوس !</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6134" target="_blank">📅 16:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6133">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid Online وحید آنلاین</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVIvNoubsBxkYrzWRWNAJG5v_kMBUAgqdMwKQ38bM0O9YiY4SoO-gopjFANyYPKQYbWhHyEcikVHHfMg8bJ8fk6PpQwPV8a-4O99vLxz41-anX79lnTFGMyICG0bnE5F_ogt_gzqUUKodh0_Lu8VvchGIacXIzIaWbrAMG3VjfMM-Lei9LqoHWPRqCPX6qKbXHjMEwqn8jgoZSAdyjByWUWUk-iIkn_uoJjhwF8nRPgW6mfKxjhNt9Q0r7Dy9UYYPFew3xWBjAtac8AaO1BJqsspgT9jv-QqedIHIbPQSVYxxpPfA0fBkKQoupiYkrfH8oOYP9WUL2AL54C_AkG53g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6133" target="_blank">📅 15:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6132">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
سنتکام : به تنب بزرگ حمله کردیم.
در جریان این موج ۹۰ دقیقه‌ای از حملات، با استفاده از مهمات هدایت‌شونده دقیق، سامانه‌های دفاع ساحلی و محل‌های ذخیره‌سازی و پرتاب موشک‌های کروز در جزیره تنب بزرگ را مورد حمله قرار داد.
این حملات توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را بیش از پیش تضعیف کرد.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6132" target="_blank">📅 15:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6131">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">حمله امروز به چابهار</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6131" target="_blank">📅 14:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6130">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
ارتش: «آمریکا بامداد امروز با شلیک ۱۳ فروند موشک، آسایشگاه و محل اسکان یکی از پادگان‌های نیروی زمینی ارتش در بمپور را هدف قرار داد
دشمن به مهمانسرا و اماکن نگهبانی پادگان حمله کرد
‏ ۷ تن از کارکنان پایور و وظیفه تیپ ۳۸۸ ایرانشهر شهید و تعدادی مجروح شدند.»
‏</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6130" target="_blank">📅 14:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6129">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
سنتکام : از نیم ساعت پیش موج تازه‌ای از حملات را آغاز کرده‌ایم.
(از  ساعت ۱۳:۳۰ تهران)</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6129" target="_blank">📅 14:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6128">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fF8hGdLFdQeyaE2YcSv-vkZ0MARiy0Qm1Hr9amdocbyFcaD2KngYO_m9O_ave7g6GhLTAh2gQwKZLEtatBheNm7pc2SQcu-seGEuyiWTCqhl7U9K4mXP691dTotFB9_ZNTgtyW20toNPMbGdu8N0AUfes6VJeSD_c_xQDrZhNpofa-c0cGmx2BzDhmVOWSvBbr0OJJHE0MUkZIjGL_ET_3CgXOZl8cjO8gRnwpbFaWY_jaOvyc8kQfA9xmWa7nooaDFRVohsv1L0aEsJmgJ2QPvDgvaMnWgl4lE_QbXURkbJUOoK46r39rx2Df40pOHNWf_xoNLdXla2F1E4rAAF_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابل توجه ساختاری‌های محترم
مدیر حوزه‌های علمیه با بیان اینکه مسئولان باید تفاهم‌نامه‌ها را پایان‌یافته تلقی کنند، از دولت و شورای عالی امنیت ملی خواست به دلیل بدعهدی طرف مقابل، مسیر مذاکرات را متوقف کنند.
مشکلات اقتصادی یا ترس از آسیب به زیرساخت‌ها نباید موجب واهمه مسئولان و رویگردانی از مسیر «جهاد و استقامت» شود.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6128" target="_blank">📅 13:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6127">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=kYvYADE63Fsj0PLYU354z_C4cZenA9JMrLzjnV55zB2QinRfDJOFAeAgJBIyUwWzJcOzxBp_rut3_sls_M8sDJivQmtK49Z8MZ9z9Wa6CNurfZ-uNmAbHYNefbSjfqXCHJcLHj9989ZMo0Pd2d3kUGujxSOoYj3YLK6l92BkO1LHm904NDXN3nn_ooAELOyKrP7VRrRwjzGyqnVH_KCU0xib9DHWNMcZG2dQ8oStj8LRA1vvNZJMebI9v-MzQhXvVyQF-86-1uM4jaSl4Aw04ZFtrS7NRgNzLZ9plc3R0MB5uxZg-Ydr3njuf2M5LZo-Nt0Sqne-4_9hxp9gPqgEioiSbPNtN6e7NxDlM4LFXS3evSRmXFji-rjeZoYroAh1ddtLC55Ncozr0PU32e4HURBgFN47A0d-7O_o81P33eXsC2BTwCvAEpa2wGs64uuZ6kudzVWriHCbZlDuElqKWaGISESOan94uoxVuPxMupnA5qZ-LhyjsBeuPRJygoqbwvKSMjUlX-JZmpvQaAk5U_WbhjmfZw120fGetOlxb2nSIngdXvoUQD0gMxcWq43X2OzUB4bGNb2E5VRnc4hm-LzPwCEIRhvIOJ-9etScJDCZwXnEoweOFNsqCpTUYEHOURzVq481iXCYGXkn3ZjlPQg4yu3xiDfAhTMFrhV6agE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=kYvYADE63Fsj0PLYU354z_C4cZenA9JMrLzjnV55zB2QinRfDJOFAeAgJBIyUwWzJcOzxBp_rut3_sls_M8sDJivQmtK49Z8MZ9z9Wa6CNurfZ-uNmAbHYNefbSjfqXCHJcLHj9989ZMo0Pd2d3kUGujxSOoYj3YLK6l92BkO1LHm904NDXN3nn_ooAELOyKrP7VRrRwjzGyqnVH_KCU0xib9DHWNMcZG2dQ8oStj8LRA1vvNZJMebI9v-MzQhXvVyQF-86-1uM4jaSl4Aw04ZFtrS7NRgNzLZ9plc3R0MB5uxZg-Ydr3njuf2M5LZo-Nt0Sqne-4_9hxp9gPqgEioiSbPNtN6e7NxDlM4LFXS3evSRmXFji-rjeZoYroAh1ddtLC55Ncozr0PU32e4HURBgFN47A0d-7O_o81P33eXsC2BTwCvAEpa2wGs64uuZ6kudzVWriHCbZlDuElqKWaGISESOan94uoxVuPxMupnA5qZ-LhyjsBeuPRJygoqbwvKSMjUlX-JZmpvQaAk5U_WbhjmfZw120fGetOlxb2nSIngdXvoUQD0gMxcWq43X2OzUB4bGNb2E5VRnc4hm-LzPwCEIRhvIOJ-9etScJDCZwXnEoweOFNsqCpTUYEHOURzVq481iXCYGXkn3ZjlPQg4yu3xiDfAhTMFrhV6agE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سفیر اسبق جمهوری اسلامی در روسیه: مطمئن باشید اگر ترامپ را بکشیم نه تنها هیچ موشکی به سمت ما شلیک نخواهد شد، بلکه عقلای آمریکا با خوشحالی جنگ را تمام خواهند کرد.
کشتن ترامپ هیچ هزینه‌ای برای ما ندارد و با کشتن او جنگ هم تمام خواهد شد.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6127" target="_blank">📅 11:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6126">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟  به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6126" target="_blank">📅 08:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6125">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USthE0EFGKZE0rOqWKp1Kw1NvCLx-_fzGaxNmjAWpDZAo2L_nlg0i6FyEI8Hyqc5nWFQ52TjHXLKm9yssSHHiLModV1daNof9sUhVf1l-P2vUoSYh3Gax2ivaqm1tM6VvgNZY92Yb6ob5K03IqcI3IdTXFsX76xfnx5O4Hv1kHrRoyIjBWzwVHU_6p3GJ9PAcWi59lSkuvzDlseQWVBvlPx6kV4OuxnQ75SOh_x-vV7NokznaIy2k1kYXEUeYIb06tQO7SQppsTS7vrShNxrTkhtlG7iahtUbpze3w56xoKmHIn1o-GBKeL_87gZIRuYuCRRh84QjgQbq46v5HlSHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟
به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت کاخ سفید برگزار کرد.
به گفته سه منبع آگاه، در ابن جلسه که ارشد‌ترین مقامات نظامی و امنیتی آمریکا در آن حضور داشتند در خصوص گسترش حملات صحبت شد.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6125" target="_blank">📅 08:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6124">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=ftzrVPCGUjms8upJYiWhbV53NCWlmh2E6IG6fZ_NW_OHHTjKLiKddKaFZS99j6g-r_GeKAOdaFpUjuNia7HtL-_vsGMTnC4_4RaFub23HtHQdJP_nbsR6JLDoJPdY8zQOZGfPjBflU3MR87JAZQm_z3Fn3ctAO2E5FGjNGkpnYvTYmApLoFQ1JK8BV9TT8lj_eBpMukV9vciPrvbI-3ukFeDj2_KtzErZaI6mqchhW0qTtEB_-2ykwLKpGpe-w_nobY5GrhEerDGWtt3o-90mStvZXNdBy9ibX2QxfuFa5y4AxTqAK_1uynFRLBquSUUrNtfiQSxM1-rTGOhFV7AlW9a5KftusoIlOXyADehRgd3zQEV32j-J5ZCf5f_tWM5iu27iNGn-n_IsdYXSg1KblzmgkDq8ndOr0wrD1XRKBAHfS_t8SHplovxXPfa2b00zxtgyMx9KZM_RP2bs5fTkgDA3PRzU8Hs_liAeEdevNczJ5iqQpAXEWotwDt6Ma-DzsVqQU3pIOVxz8juYZWh8Xagtncahr6E2pt_2cHpWr11RyDESm0TQQ41WTWmk6t9mkRwY5956OwbG6_CLBYVW9skyYCgxlbD7gyEi4FQCYy4prPNU63wIlUjIFOUGRtTsq4KCmBdSnuemybiOLEeq4nBlp3e3FEz0SF_36j6xF8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=ftzrVPCGUjms8upJYiWhbV53NCWlmh2E6IG6fZ_NW_OHHTjKLiKddKaFZS99j6g-r_GeKAOdaFpUjuNia7HtL-_vsGMTnC4_4RaFub23HtHQdJP_nbsR6JLDoJPdY8zQOZGfPjBflU3MR87JAZQm_z3Fn3ctAO2E5FGjNGkpnYvTYmApLoFQ1JK8BV9TT8lj_eBpMukV9vciPrvbI-3ukFeDj2_KtzErZaI6mqchhW0qTtEB_-2ykwLKpGpe-w_nobY5GrhEerDGWtt3o-90mStvZXNdBy9ibX2QxfuFa5y4AxTqAK_1uynFRLBquSUUrNtfiQSxM1-rTGOhFV7AlW9a5KftusoIlOXyADehRgd3zQEV32j-J5ZCf5f_tWM5iu27iNGn-n_IsdYXSg1KblzmgkDq8ndOr0wrD1XRKBAHfS_t8SHplovxXPfa2b00zxtgyMx9KZM_RP2bs5fTkgDA3PRzU8Hs_liAeEdevNczJ5iqQpAXEWotwDt6Ma-DzsVqQU3pIOVxz8juYZWh8Xagtncahr6E2pt_2cHpWr11RyDESm0TQQ41WTWmk6t9mkRwY5956OwbG6_CLBYVW9skyYCgxlbD7gyEi4FQCYy4prPNU63wIlUjIFOUGRtTsq4KCmBdSnuemybiOLEeq4nBlp3e3FEz0SF_36j6xF8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مزدوران حکومتی شعار میدن
«جنوب ایران نکند جنوب لبنان شود»
عجب! شما دیگه چرا؟
خامنه‌ای میگفت «جنوب لبنان الگوی پیشرفته
و موفق مبارزه ایمانی است»! سالی یک میلیارد دلار از اموال ملت ایران رو میدین به گروه‌های تروریستی اونجا  و تبلیغ اینکه ما اونجا پیروزیم و …..!
ولی ظاهرا اسرائیل در جنوب لبنان چنان درسی بهتون داد که الان خودتون هم میگید نکنه بشیم شبیه اون «الگوی موفق»! معرفی شده توسط خامنه‌ای</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6124" target="_blank">📅 07:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6123">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=emAoAseqrz8XbkKq5c540HoavmViwze6sB3tBHZPqd8_dR86xKlDBl8j8mbue8A33uNHU4Dbv1CU36PST4E0yLBxdwCw_jPoFjMZtQnryqfXTvqvosyRf_A23DUtDn00C5kYgK_J_oTsa5l-jQfKDUQGBBLJ-vtuZwG68HLd3uwpTct4B-N7OWTX0newEQLgBefQgRVqYSqT2VqZZi1itdnPeXL1ZxVsBNCCWKJucq2bB1LKpde-V6ywd0sBtSfHiPSZV8-WWt0xWTB7bUROV9sv0ZGawQ694NQOeXj6GsZ1M8z3HMQeAJ10L-W3IRydEEG-FRmw-JIypvdVUdpVSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=emAoAseqrz8XbkKq5c540HoavmViwze6sB3tBHZPqd8_dR86xKlDBl8j8mbue8A33uNHU4Dbv1CU36PST4E0yLBxdwCw_jPoFjMZtQnryqfXTvqvosyRf_A23DUtDn00C5kYgK_J_oTsa5l-jQfKDUQGBBLJ-vtuZwG68HLd3uwpTct4B-N7OWTX0newEQLgBefQgRVqYSqT2VqZZi1itdnPeXL1ZxVsBNCCWKJucq2bB1LKpde-V6ywd0sBtSfHiPSZV8-WWt0xWTB7bUROV9sv0ZGawQ694NQOeXj6GsZ1M8z3HMQeAJ10L-W3IRydEEG-FRmw-JIypvdVUdpVSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6123" target="_blank">📅 07:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6122">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=U1x53gCWtsZZpbGPskXIIhuMji0nUCRD2ZZvYqFgwQsPfodYNZASHX8-1H7naVFa8ASr2sUqSt-2rX9R5HQ9Qt_uASrGaFlUWQLpjskM5Jv0OD2IOJdNztqLWJSu66vN9qEr30VUgXKfD_CE9Olk7czQJ_Waje0HBSlXhYOjgp-uOgs5TDfLqkXxn2gMpgyZKTMVwNd5wrVsGqHbYvWOAbejgjK9L2sTgjs_iDOAprAI89Bh3x9G56lHmQ77qJ4cJASd9aYsHnJMTWkY-GNhdZH9RqtRL_v8GylewW_X_B4pTv7l0HbEoUA01HAZQsxfFMlkMmqGS1si4uE96TH2nVt7COIKddGfHSjadOw1ziymEjQLDK6aKba39KBHSD7HvaEAlF0ZHL8vbuUlnUNs7pwg8c0MoiURLelz0RP3ZzxCLURt3vZTtViI7RKUSqT_AHK8AhKlsa9zhqYCl5wx0k5zamxKY7vG_eC2z538XNU3dXhKkwI2Y-j3MQFhTE7zbczj6THTEScWqFEReBMIww7IuV2Y7a7820iGk7o5elIN72AMpAX-9YkxNb8xIskLyxO3AnupIPVeTz03TcXIuFem3QDjp8JHIey87QswNIjXEk1770uidtOWVnb5P4fTU4kodTR_IZyg1GBgL42xgP-9j44xf4OkZNMi4znU_28" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=U1x53gCWtsZZpbGPskXIIhuMji0nUCRD2ZZvYqFgwQsPfodYNZASHX8-1H7naVFa8ASr2sUqSt-2rX9R5HQ9Qt_uASrGaFlUWQLpjskM5Jv0OD2IOJdNztqLWJSu66vN9qEr30VUgXKfD_CE9Olk7czQJ_Waje0HBSlXhYOjgp-uOgs5TDfLqkXxn2gMpgyZKTMVwNd5wrVsGqHbYvWOAbejgjK9L2sTgjs_iDOAprAI89Bh3x9G56lHmQ77qJ4cJASd9aYsHnJMTWkY-GNhdZH9RqtRL_v8GylewW_X_B4pTv7l0HbEoUA01HAZQsxfFMlkMmqGS1si4uE96TH2nVt7COIKddGfHSjadOw1ziymEjQLDK6aKba39KBHSD7HvaEAlF0ZHL8vbuUlnUNs7pwg8c0MoiURLelz0RP3ZzxCLURt3vZTtViI7RKUSqT_AHK8AhKlsa9zhqYCl5wx0k5zamxKY7vG_eC2z538XNU3dXhKkwI2Y-j3MQFhTE7zbczj6THTEScWqFEReBMIww7IuV2Y7a7820iGk7o5elIN72AMpAX-9YkxNb8xIskLyxO3AnupIPVeTz03TcXIuFem3QDjp8JHIey87QswNIjXEk1770uidtOWVnb5P4fTU4kodTR_IZyg1GBgL42xgP-9j44xf4OkZNMi4znU_28" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا میبینم راست میگه …</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6122" target="_blank">📅 07:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6121">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJD-JB0CDAE7wJHJN8PprXFuaoxj50sMn7f1M9xeqdQ-cGMZBPF7BgJHFI_IDFNtObjBwjk79VJBahR19otdUWwBVJUP_2o5qvwkyMcpgvORySOKKV34N_D3lKSqqXynUsd-Hrx_hg0Im39peFNyw9s9UryX1KOyIvKEueKhqTUvBdV_Kev5uqO19g9j4k9Oq_fI7y8haxR3zbeZcaKCKYGxBfWRC15sczExcdm3mGeQFHwevCoheSKAgcw9rRv_MHQuwnr7oU9Vf8SF3pWizYDV1RO5bpfyXjAPpPjNXOqW6qsH22JkzarV70xxil9CdrySFEP3Qv_3sGO1hdJ6Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6121" target="_blank">📅 06:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6120">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJKk2KQ-jJMUS0pZ-iLj2FPI2nj4kTObm6L2OuGQyxoe8p9FC-JedZkWy39VLDbPju-xOe4ujW7wntQ-G8FeHbIfGp052MYcmRgaB-EZMfp66pwuBuIhAT4AX8FUXmY8w9z8LQP7Xz91FwsP2-SBWl3m7mtK_JtwdQTDlDjWb8CSIWhf3yKy2pzcMRBJzUrYvG_dKndGpCHC5QUrLWco4SCy33rzKNT0h1Ou2Q87DS45TITRDp_5aainwBCIBdtbgAG_aOUEG1GwW5_Y1TA3OYRDDZ123nFg95z20yFqe-ODU-6l0o3axsHfmhIp5-_eYpbfYBSvRRB9pNiz7RxiMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6120" target="_blank">📅 06:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6119">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=MSuIcgTfkOVTytLXEr8FYxmYyukZrVIug4uBJxOgT3skpexJhq-iJLAdN5KvGaTrhflz1lpvZw5TtIs1DSh1Zr95aDuXDL1d1C0UgPMH7XgQDCIhCJYQYUzzJV6vVodUBjXRrOaB3WGetcn7TAKrTAUx1xC6wd78DEOJJ4cXnXX8JgYEZIy--nnakODO0crvcLFsKJfaf89TKtyIFdxiArj_exX1xW6b6PCTRmSD16kcmV7OUl11fN0x8a0qEtqmss6KEWBMXVVV82FDvCPSlZ2_tUHU0XA91VIzQEp0Ej10FDBXP3K1jQGACsB2zQmFs61DLfGF11j1GWsdxsNuIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=MSuIcgTfkOVTytLXEr8FYxmYyukZrVIug4uBJxOgT3skpexJhq-iJLAdN5KvGaTrhflz1lpvZw5TtIs1DSh1Zr95aDuXDL1d1C0UgPMH7XgQDCIhCJYQYUzzJV6vVodUBjXRrOaB3WGetcn7TAKrTAUx1xC6wd78DEOJJ4cXnXX8JgYEZIy--nnakODO0crvcLFsKJfaf89TKtyIFdxiArj_exX1xW6b6PCTRmSD16kcmV7OUl11fN0x8a0qEtqmss6KEWBMXVVV82FDvCPSlZ2_tUHU0XA91VIzQEp0Ej10FDBXP3K1jQGACsB2zQmFs61DLfGF11j1GWsdxsNuIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام فیلمی از حملات خود به ایران منتشر کرد.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6119" target="_blank">📅 06:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6118">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=pwDUThC7gGhQjVK5fnLdZhDZw2_b9ZAxv1ha7PSFR9UZ_yTnYkfL_WexK_tmut_qg7o-4UggixIUpd4BcDAkus02xBBpJ93DwxlvIxYfGxk4X82ijK7d87CdP954Zuq0r9lSH7gZyQPImnr11LXCaFEm7B30AwJegOqw4RNferia_MV8_eMHe1fphNBvtg_gWdYUZT9eR7wmjabAxsNLPeBWXR4x82yxUYwtPYxWdXEkJlxTxxvZI5Cw3i89juejATmPdgUnGD66Nwu3Ahh57UA5lFm8woYnghk5U7ULDtdfBB3blIC40_Sila_EqPu9IdJCBabZ1eyqlcuth122AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=pwDUThC7gGhQjVK5fnLdZhDZw2_b9ZAxv1ha7PSFR9UZ_yTnYkfL_WexK_tmut_qg7o-4UggixIUpd4BcDAkus02xBBpJ93DwxlvIxYfGxk4X82ijK7d87CdP954Zuq0r9lSH7gZyQPImnr11LXCaFEm7B30AwJegOqw4RNferia_MV8_eMHe1fphNBvtg_gWdYUZT9eR7wmjabAxsNLPeBWXR4x82yxUYwtPYxWdXEkJlxTxxvZI5Cw3i89juejATmPdgUnGD66Nwu3Ahh57UA5lFm8woYnghk5U7ULDtdfBB3blIC40_Sila_EqPu9IdJCBabZ1eyqlcuth122AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : امشب، فردا و فرداشب به سختی به آنها ضربه خواهیم زد و هفته آینده پل‌ها و نیروگاه‌ها را هدف قرار خواهیم داد، مگر آنکه  مذاکره کنند.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6118" target="_blank">📅 06:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6117">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caeb092620.mp4?token=ax17NiSZh6r1UZ1ghwzJRqbrHtGTd1WgDWrP-wbhiO9SS-ZrHFP5b9LoKU18ZOVYmI1p9oeCrBsk7U5ckjByo46OlfjQA8CUmxeO6x69HWaFKc3hytUQnsmnuqpBkuOi4I9h7qwMDQlugqpz3sq6DcRERU-TQiXJnLEgzyHyWDIW0jjNAbL98fCiWPm4TzIdzWpO7UHLl2lv21JJAT-WK5N5a6SGQui0tHHqcXLJU71Sjxj7pMQJqWuDksw9__iBG8CXTllOLs6xZ8vG-PIgSdHT_wuiblxX55y4fc1WmD8xwbzPKUWWkjPw_GgPMPZNLxTra9U3qIAfAC9uUo_upA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caeb092620.mp4?token=ax17NiSZh6r1UZ1ghwzJRqbrHtGTd1WgDWrP-wbhiO9SS-ZrHFP5b9LoKU18ZOVYmI1p9oeCrBsk7U5ckjByo46OlfjQA8CUmxeO6x69HWaFKc3hytUQnsmnuqpBkuOi4I9h7qwMDQlugqpz3sq6DcRERU-TQiXJnLEgzyHyWDIW0jjNAbL98fCiWPm4TzIdzWpO7UHLl2lv21JJAT-WK5N5a6SGQui0tHHqcXLJU71Sjxj7pMQJqWuDksw9__iBG8CXTllOLs6xZ8vG-PIgSdHT_wuiblxX55y4fc1WmD8xwbzPKUWWkjPw_GgPMPZNLxTra9U3qIAfAC9uUo_upA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار ناشی از حمله پهپادی امشب سپاه به کویت
گفته می‌شود مخازن سوخت ارتش آمریکاست.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6117" target="_blank">📅 06:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6116">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/360d24e506.mp4?token=AK_op8jYNq6dMCUOFskiJbcu2ubK5thJSrZLxtAAKNCBLFTvIug1UHoBR2Wti7N469kii97XvMFrDqqlnrByNZmXJhm3ttKHLrlxzTURKVCRv3CFv18bmy5IYz4cMXvD7HvlWixLSFag9EN4y9iP2tc8ENVJmkfWALlH_nOdBVQb5k86MNaH0oJyfm8br14nhtXNgFgacgPjGzMsUURZHL3kkkvIQo1wWmnqKEIBKzccZZFIX3Iudzct8eksQKageVgmFs7pWe9SQyYLk1Nz7FF9sRF_rnBsT4S5vghp59D7qLrw0o_NGNjp8fvy8YIj1hyl37rZYfjVeQ4YJcEPJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/360d24e506.mp4?token=AK_op8jYNq6dMCUOFskiJbcu2ubK5thJSrZLxtAAKNCBLFTvIug1UHoBR2Wti7N469kii97XvMFrDqqlnrByNZmXJhm3ttKHLrlxzTURKVCRv3CFv18bmy5IYz4cMXvD7HvlWixLSFag9EN4y9iP2tc8ENVJmkfWALlH_nOdBVQb5k86MNaH0oJyfm8br14nhtXNgFgacgPjGzMsUURZHL3kkkvIQo1wWmnqKEIBKzccZZFIX3Iudzct8eksQKageVgmFs7pWe9SQyYLk1Nz7FF9sRF_rnBsT4S5vghp59D7qLrw0o_NGNjp8fvy8YIj1hyl37rZYfjVeQ4YJcEPJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی با موشک‌های حاوی بمب‌های خوشه‌ای به بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6116" target="_blank">📅 01:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6115">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
ارتش : به پایگاه‌ها اف ۱۸ های آمریکا در اردن حمله پهپادی انجام دادیم.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6115" target="_blank">📅 01:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6114">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‏امشب اتفاق جالبی افتاده، به محض اینکه خبر انفجاری در شهر و استانی منتشر میشه، مسئولان جمهوری اسلامی سریعا مصاحبه میکنن و میگن دروغه و همه چی آرومه!
‏اینطوری مثلا میخوان صورت مسئله رو پاک کنن.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6114" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6113">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uxiu5kY8T0ldqy3N7r969i1Gso4rVIHJtM_Qj7VCWralYfPnbMsKq6ArxTV_MjkozGWu8IvnEVII9nzPfkjMBF3Z6smxum65sPFx2HxDF68FTrlsKwH8y4d8SMRkLcxDQGlnDXexcVlMq6HO4yJUa5C3sANplZs-Yt8rEMU_rh7Rhdfv15D0tN_cNAf8U8eEKUuq9gVvzUZec6CdJEUdb1koo1dlWX_ZsXW9IykWzyEn9a9R59GKz7rA5M4jzVbnEMUwC6m5PA_yYhPVivSl-SMr9PX4Q-ruZbwCdItlu_RhvR_vvy31VOLpieGIi9mFDwdTbSCO2OTpFe_YFGyvEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگارهاشون می‌نوشتن که کشتی‌ها دارند  از مسیر عمان رد می‌شوند، تشییع جنازه،  بریم و کاری کنیم که  کشتی‌ها مجبور بشن از آبهای ایران رد بشن  و شروع کردن به حملات به کشتی‌هایی که از مسیر آب‌های عمان میرن.  به زور حمله میگن کشتی‌ها باید از مسیر ما رد بشه.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6113" target="_blank">📅 01:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6112">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZTgPcPS_MqGB0peN-WkbU_zDB4gJx794jUoXlA2oHuBLBO-MWGdNqhz2zjTlVVqaLcRzR71ByRCmqXynZXG4-dn1mf1DA3UMC-brkgl7Vxo4bjkcncpLCb2Y-vEklKEVetRD2ijRwUGYo1D706IHe4bmZyVViwAwQHM0b0vxde0O3sNk2NQ-AGKjBojn8jjbxMJy_GvTMOx4pUfiFBdCmol8oi68fo8-JGDEzFrEBcmn_ml6cah-wulCW1ok3lOOnukK7paS54XNqes3f_uQPp0DQ6awXpAtd137qBRF2DUhE4ELw2qXz3g6CJRFOEitHPR4IrCObtGEJbybU8zCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا در حاشیه خاکسپاری جسد خامنه‌ای و جلوی قالیباف شعار میدادن «مذاکره با دشمن خیانت است»  هنوز به سه کشتی حمله نکرده بودن و نزده بودن زیر تفاهم نامه</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6112" target="_blank">📅 00:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6111">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=TwFnqGnRFL9uVQQTwHYy--VeGdNiZtgvRhrpJHZAyT-5-a1xM0Fev-sC-wTM71PAsHOSXkDQirx7ilXnL25Ig9tgFCg9ku_JPRvlLGq-tOaxorf4FL-04VPQ6shkWmeN-iJMftLJksM-5yAMbkTmosLioI6ewjbJz3zlTbdQxwBZ8pThpN5eoG7jwDQZ21-oBWcozcIZRwJPvEiJMr2ybj2lSW5IyOKtZt3u5prEHhdrDrRGhJ0leZkLvGanJPF5Y4a0HguQESaEwgegnDk52pYrweYL7U0Sv9hUhhWNww1J4OnnRW3QTPieDoSElKVu6nX7rz8pUTvWYA9mMRz6iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=TwFnqGnRFL9uVQQTwHYy--VeGdNiZtgvRhrpJHZAyT-5-a1xM0Fev-sC-wTM71PAsHOSXkDQirx7ilXnL25Ig9tgFCg9ku_JPRvlLGq-tOaxorf4FL-04VPQ6shkWmeN-iJMftLJksM-5yAMbkTmosLioI6ewjbJz3zlTbdQxwBZ8pThpN5eoG7jwDQZ21-oBWcozcIZRwJPvEiJMr2ybj2lSW5IyOKtZt3u5prEHhdrDrRGhJ0leZkLvGanJPF5Y4a0HguQESaEwgegnDk52pYrweYL7U0Sv9hUhhWNww1J4OnnRW3QTPieDoSElKVu6nX7rz8pUTvWYA9mMRz6iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این استوری رو ۶ روز پیش گذاشته بودم  میگفتن آمریکا میخواد آتش بس حفظ بشه ولی جمهوری اسلامی باید «کار دیگر» بکنه!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6111" target="_blank">📅 00:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6110">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550f13e765.mp4?token=gSVPJIwg_cLL5yNXaHY9Sb2lDzPFUP-yi3yXet_lUs6O62-dJCW0UO9FCaZvgnnQyr7JYnfVIfCcy3Pw4TTfkfbP_GNZ2k4g0Dj9Kq8KZhu-6QN2aYulyFRob0MLwetZwfKN9zazkI6YW36ipsMX7-goIo3Opf8PTfXnn5KEd7AdyIsmUbbvkcoMzripWaysiJnUhQghoIy5nTNfOiefDUaPv7koTzRqyJRbIyKD6zreL8_PvbL-6xe6ICSLuZOt3duE201sEqMTAe0fZ0_lyrk3O10tYyaBCwboHjZYzNXQJ_vcw-AC3Dor__5VOMUIPmP6Nc_ese_lL2DKL6cRDzf3-irm92YX5CrZEZHx7-9QCQpFfVZ4AGo2aBL-3fPMOUcVsZeG-y-LmlyiT9M7wr4fDF4xhc5nCXA3SbwHhcOscwEl8QuI_xyTRg8ULKG7ZpL4cDtWVmh69j1sjF3fQkIalXCDXWBRtycp6ZtPCZa6uOxNOxE0PVUyddqmBb4_kWNpuuS-7O3mXV40T6mZrQbp8rFlubB5BgGDTtwy1UQRgBDLbTlVRIzDe0HcTaKEzsVXQe-NYVf9oVIbJYNq3TL2DyYQypb_WK8yoYMwxAdysKlCT6jZRY8ARzJJjDaqGu3wSJp9f1eSgUSCrF0UcPCHzl8gb6RClXSYuS3PezE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550f13e765.mp4?token=gSVPJIwg_cLL5yNXaHY9Sb2lDzPFUP-yi3yXet_lUs6O62-dJCW0UO9FCaZvgnnQyr7JYnfVIfCcy3Pw4TTfkfbP_GNZ2k4g0Dj9Kq8KZhu-6QN2aYulyFRob0MLwetZwfKN9zazkI6YW36ipsMX7-goIo3Opf8PTfXnn5KEd7AdyIsmUbbvkcoMzripWaysiJnUhQghoIy5nTNfOiefDUaPv7koTzRqyJRbIyKD6zreL8_PvbL-6xe6ICSLuZOt3duE201sEqMTAe0fZ0_lyrk3O10tYyaBCwboHjZYzNXQJ_vcw-AC3Dor__5VOMUIPmP6Nc_ese_lL2DKL6cRDzf3-irm92YX5CrZEZHx7-9QCQpFfVZ4AGo2aBL-3fPMOUcVsZeG-y-LmlyiT9M7wr4fDF4xhc5nCXA3SbwHhcOscwEl8QuI_xyTRg8ULKG7ZpL4cDtWVmh69j1sjF3fQkIalXCDXWBRtycp6ZtPCZa6uOxNOxE0PVUyddqmBb4_kWNpuuS-7O3mXV40T6mZrQbp8rFlubB5BgGDTtwy1UQRgBDLbTlVRIzDe0HcTaKEzsVXQe-NYVf9oVIbJYNq3TL2DyYQypb_WK8yoYMwxAdysKlCT6jZRY8ARzJJjDaqGu3wSJp9f1eSgUSCrF0UcPCHzl8gb6RClXSYuS3PezE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو رو دو هفته پیش گذاشته بودم.  معاون سیاسی نیروی دریایی سپاه اینجا در جمع حامیان حکومت بهشون میگه خیالتون راحت باشه، حملاتی که ‌ آمریکا انجام  میده «واکنش»  به اقدامات ماست!  «کنش» نیست!   تمام این ۴۷ سال همین بوده!  یه کاری میکنن ، تنش راه بیفته،…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6110" target="_blank">📅 00:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6109">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6109" target="_blank">📅 00:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6108">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=DrdbB_xFABeuWizVxeVT-3w8kdxtJrkLT5Gc8HheXa0gFhJbzDp5jauYpZBX-n9KLErO_yyU4wOC4_Z-hbHkj0XWuZMMHFp8KMQuguj854LQtjP66_URTShFa_lYasxxeh4WTFW6BwGLzP5bXBpVsAZpR9-VqviECXOrUACYB76XE96fEUOdIIZD6qN9T1IzZuNCm-MrIITmP0fwXvPNgTJPehgzxrMqYsNZI3Gvomi9a2GAtoqyhbdUC80GTmdgYRz4CzP1lelQKA7J41kug9oa7wTdnnZD0QNFINxo_pOZyOuQDjmszb0EiaVEfFiyMm5erbuKmohckupN6XOxQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=DrdbB_xFABeuWizVxeVT-3w8kdxtJrkLT5Gc8HheXa0gFhJbzDp5jauYpZBX-n9KLErO_yyU4wOC4_Z-hbHkj0XWuZMMHFp8KMQuguj854LQtjP66_URTShFa_lYasxxeh4WTFW6BwGLzP5bXBpVsAZpR9-VqviECXOrUACYB76XE96fEUOdIIZD6qN9T1IzZuNCm-MrIITmP0fwXvPNgTJPehgzxrMqYsNZI3Gvomi9a2GAtoqyhbdUC80GTmdgYRz4CzP1lelQKA7J41kug9oa7wTdnnZD0QNFINxo_pOZyOuQDjmszb0EiaVEfFiyMm5erbuKmohckupN6XOxQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گشت زنی اف ۱۸ آمریکایی بر فراز چابهار</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6108" target="_blank">📅 00:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6107">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا : محاصره دریایی ایران وارد فاز اجرایی شد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6107" target="_blank">📅 23:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6106">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
چندین انفجار در بندرعباس
🔺
چندین انفجار در اهواز
🔺
پنج انفجار در قشم</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6106" target="_blank">📅 22:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6105">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbXZJ2Kdu76y-dJklZd0SxlFmUzk5K9RkZiqINsTHizm-_RNef9c-zm4hNUfITbuvfWuT-yAPyF3XpwsShXEKwYrPH-EVTlKcy7psAFRKWwlSqsFYQd4Zq_oPfy9ipsNiu9meh2ktIsutQRN1USNrQNQlse8uT6KMsXVIjPGwOCo7b0oPxSc_i-oDmyRE8d7lM90ZpUHZnRgdrOffZLcS2kNJxz9u5XNHHDZ3DHcMHKbIT6id6gRk6y-yV3iuhwZx11BvhWd3Mza_T3sLJKYYnhPLFtK1PV60kAJK0jF1x3u24mGhQNWR_2VoMxEGiwsJil4EOD3cLARmOfAOAgmdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2077085449948938568?s=46</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6105" target="_blank">📅 21:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6104">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
دقایقی پیش : حمله به قشم و شنیده شدن چندین انفجار
🔺
حمله به یک نفتکش اماراتی در سواحل عمان
🔺
فعال شدن پدافند در کویت</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6104" target="_blank">📅 20:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6103">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_kg0UVTP86J2xNcyuBsD0TqgNci-S8GZsqiBJlu-NbIeYe-G3Pg-d5S0vqEElybBSsQGZhAa1Z9Uz7baUT7Kap_yD5i_WthJgXiY6DHaoXSo9z1gXyw35RI9pW5BFbiEUaIGU1FIzI1lpW1dTaG0m3TX2zTpgjvnsDK54-Gy1q5UiKj_tRWMNXNX7RrRUBjfyKp3yRArg1nf7OGvSpANWI3CdRA8KeAAPtOWqEOdjospE-XDzEJeP6btUJxW-UKEyCEoLPljqqNqEADWiPF2msFJSfPIDbIlvZ4zp84QZKXupK0iS_CVmfYtSwhxXck954BPv1l2GuoGqUGpVY9lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهپاد‌ها (قایق‌های تندرو بدون سرنشین) آمریکایی این مدلی به یکی از مهم‌ترین مراکز نیروی دریایی در بندرعباس نفوذ کردن و حمله کردن.  گفته می‌شود که در این حمله یک زیردریایی ج‌ا را نیز منهدم کردند.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6102" target="_blank">📅 18:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6101">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=GekCV1mTTj6V_Do0gWh0rssIbncxj1L6MstQQrXMq4YTwOdKxM2aBSF08vU16a-kcwDDXQ5xz33eBm9-Py_F_3Idc55MOMK47fk3xg1qjeShB2nQSVbjBgn37IA_MoY3DqITLrDg84_a8Pv-N1zFdyz7bMWvZA1JFUpyPF15KK3TrhGYgvTSwYf4XhrIcvPryDEHj_HPc4ATbT-NGDO03ADvEP1QNJULySUmFDwnob7Nti25ME0qmVC0h3p76JLJN5lPx7rVMzf-an2Gs7_195DiQLGztjgHLkqP592blp5Boe2-yyAh0mTYWS6H_PPNMtHeLW4L6aWG2gkLAv86OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=GekCV1mTTj6V_Do0gWh0rssIbncxj1L6MstQQrXMq4YTwOdKxM2aBSF08vU16a-kcwDDXQ5xz33eBm9-Py_F_3Idc55MOMK47fk3xg1qjeShB2nQSVbjBgn37IA_MoY3DqITLrDg84_a8Pv-N1zFdyz7bMWvZA1JFUpyPF15KK3TrhGYgvTSwYf4XhrIcvPryDEHj_HPc4ATbT-NGDO03ADvEP1QNJULySUmFDwnob7Nti25ME0qmVC0h3p76JLJN5lPx7rVMzf-an2Gs7_195DiQLGztjgHLkqP592blp5Boe2-yyAh0mTYWS6H_PPNMtHeLW4L6aWG2gkLAv86OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت جنگشون :)</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6101" target="_blank">📅 16:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6100">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhznjoehiZMEWAuha51wWyV0pbG0ZhrwK4oCRNs2iA008zNlwG9VajeTiOxJU2eP4JaffwDGBxXIVHQxrs9Esr-FqFF6_UuWwwYgUO4WBAiWf6alWm-6QUtzubSQgUsW8WgE1CaaNczvratqTiM-YfRUl7i0ntBzJbNzc7O3qtzlO2cDBDIGindCANXITl5iO1DfWi26fbOmEVX1pBsgLZJF8Na63HfvvCWic_gNkv3czZbRPqdt32TyhDr8Vip8aLAW6yj21mZc7QrPBvqz6cNXQ7tVFa_4arpSpyCBWI3tot2kPXBrQ3EPQRMogd0Do9DtxyBjqVIADYzGCgPRbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏آمریکا با استفاده از سه قایق بدون سرنشین (شِهپاد)، پایگاه دریایی دیروز بندرعباس را هدف قرار داد و تأسیسات نگهداری زیردریایی و کشتی را منهدم کرد.  این نخستین بار است که نیروهای آمریکایی در نبرد از قایق‌های تهاجمی بدون سرنشین استفاده میکنند.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6100" target="_blank">📅 16:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6099">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">۴۷ سال رژیم اسلامی</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6099" target="_blank">📅 15:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6098">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBhqiYMubcu_01bJMWX_qBLu0LDktkCZlNUvpgEadFYhW-NQRkJaRC4CdJ8Q4wsBv7teGrvLFXG0YoxhkpwiinRSGupEYy8LxzZl9RUoYh-pqOkL-Un132kkWrN4WcZs8bUa5AuZkCIRzkIpVu-VzCLgFrgUA1_LVJsoiGpI9nyqTKY3qDkpHww7skb5yhHf4un8rWSj7ybRFHl8OdOlivulS0ULplG14t4B28G6QozDr4-UG8nrQSwNeMXSqSuGQFYz8xM-JTzrNM6RFFsqV_oct3e6aSUSwtvtV3OUBMtCeQSeqp4xrGimBYoxWkfzRhz2M-8S3syW-jbqC-ZRQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
تخریب ساختمان مرکز آماد و پشتیبانی دریابانی نیروی انتظامی ⁧ بوشهر ⁩ در پی حملات هوایی ⁧ آمریکا ⁩ به مراکز نظامی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6098" target="_blank">📅 15:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6097">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6097" target="_blank">📅 14:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6096">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9c510f4f.mp4?token=aHKjaqxdJ14x9Wp4xgbiyVNq8QecS7KeERUh6fUtYLYia9LsCdTncFpTjl2F4meZHkWIKBugsJ_r7cLLh6hM5AUgtV-HnxP6p7ioDyjB8wyvurH_RH3Z-6K8BGo2eyZN5aW4E4XTj8YSOt_kYwNcMMTnYcVQRHnUWqK9eiY9x4pFPL7KWO5PWmA093oF71HEBjMC4qvaqh1Tf7_0-2R4QyRTXy2Tqf2ZuJBnxdPzX6gs92cJ3hhllZ7BqMoh5XU04sWHNm2Mn0G0DvHJq8KZo9bE6uwzXlsNydWKtu1f5uXKRTDe1V7GLyqvTQo-qm8bc4FGCJq3zt6vWoIqdh76JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9c510f4f.mp4?token=aHKjaqxdJ14x9Wp4xgbiyVNq8QecS7KeERUh6fUtYLYia9LsCdTncFpTjl2F4meZHkWIKBugsJ_r7cLLh6hM5AUgtV-HnxP6p7ioDyjB8wyvurH_RH3Z-6K8BGo2eyZN5aW4E4XTj8YSOt_kYwNcMMTnYcVQRHnUWqK9eiY9x4pFPL7KWO5PWmA093oF71HEBjMC4qvaqh1Tf7_0-2R4QyRTXy2Tqf2ZuJBnxdPzX6gs92cJ3hhllZ7BqMoh5XU04sWHNm2Mn0G0DvHJq8KZo9bE6uwzXlsNydWKtu1f5uXKRTDe1V7GLyqvTQo-qm8bc4FGCJq3zt6vWoIqdh76JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌پرسه نظرتون درباره اینکه بدون هشدار قبلی برق رو قطع میکنن چیه؟
‏چمران میگه:
‏شما اگر بدونید پریروز چند نقطه برقی رو زدند دیگه این سؤالو نمی‌کردید.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6096" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6095">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcJOWwA4c3CAhcf1pPdIqGObmlJRycXswP3kHCuy8hQURxhRhVV9VrwNXhkJWermsnTKgczUlvyiF9FI7IjiKPKfP8mykLzJmGuOW_-c1w-x5B8daxYSVUp8i1S7ZWlUA5SaCBHJ7Hu2apVgnRHzr63xTcOTWU4ufSK-FpHJW5uuNq_W8N_fNLxiUwGjWKzr178xdmU0gfNacebyCfonz_qzxkddL_ndEn4fg3WI3_e84oOfNX2LkQo2vMEzkucRkDVp4XPPR0CtGUndidl3xjTdkUYOr7xQ47zyb3t_C5AcZy5AYV10oPht1XEx0XWLjJzrdrRLxHwa5sYsV3hF_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه ترکیه، دیروز جمهوری اسلامی
رو با اسرائیل مقایسه کرد و گفت
رفتار این دو شبیه هم هستند.
(کاری ندارم که ترکیه خودش چه افتضاحیه، اما نشون از تغییر رویکرد ترکیه نسبت به ج‌ا داره)
یادمون باشه فرمان حمله اخیر از سوی ترامپ در ترکیه صادر شد! یادمون باشه معاملاتی بین ترکیه و آمریکا رخ داد، که آرزوی ۲۰ ساله دولت ترکیه بود.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6095" target="_blank">📅 14:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6094">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
حملات دقایقی پیش به بوشهر ، خورموج و….
🔺
سنتکام چند ساعت پیش گفته بود که این دور از حملاتش متوقف شده.  در اسامی شهرهایی که مورد هدف قرار گرفته بود هم مثلا نامی از کیش نبود!  مشخص نیست آیا همه این حملات را آمریکا انجام می‌دهد، یا کشورهای دیگر (مثلا عربی)…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6094" target="_blank">📅 13:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6093">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejdmeedGtWrVrePsqXQTWFBcplDuBdltZn9KVFu2TyyK9Kf4-VZ-yBBQqHnc8gV696NqHJkZkk0J3hrVHI40rFUd9cjgpTyErh0mIvcDjPIgzXlA5o8wFGEhmefm2nEPMqlCJB0Brt2Nr0sp55lzFN9GmPxLXwPIkrVQGKdLwGGadYO5weXnSn1Yyt5p5EEHjYxkXtKNsWQmqmVf9EAw-7-6gohFjTbQOUe5MIvl5i3tvJV82Ol5mKW3iG3k9kmhAGyNGTXHiWPxZrCdTveCRP3hwU4P5iBpehov9T-lpSiWrNwIpDmwzXqPC1BXcpBCLbWfgcTRg1Y7YeBxr8ryhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6093" target="_blank">📅 13:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6092">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=QHGLwbvjZsHB48FvMF2y34SIw6rkudNqlPyzJUzdgNF1ENNixaxOzW2IdHqRqiE1T0tZClxBbd6wSjapb6I43498BJaAi8HvLmN6dSxcfIEe34M8IYIIjoxOByS2YeGkY_eavw734YGQizKby4w9Aglxeh2RYRIJQl6tQZKtcBNCRz49o7GSO8SPfmdsE9oGLcomZ7R3B1TdKd4cYS3_ZXq5nmYJLvzXQpnPf0IVDi07kw83KoxERS8Ujac2i1MRG8fR5gQvSJsgWlCniA_E7NxHQQ6Lv-wl22KNOdWF2I4Zb_icrQMgZLFXTv8IjCLsaMvPc9xAYq-7tW-tgob-VFMCQpLe_fqG22l2CdYXw05RoSO6YolGTviS1QF2aN0f4MxusDeIF_prIF83RJX8onLTJuo_dGEopfcuNuO7nb6oMnyu-A056xArAtcJy-ov-DJrxFs5IcFXUnVYi12NHcbm2n5sm6lTsoiLUKemstAOn3l3g3s-ymSSAqEav9E8jCgOa2Qk46br0sbUquohbxuJL2bczVhu5ik-F-KtGSH02s7G50XYJbOFwG_oGUhQ9-XIxn0r7LwDKPop9EZaKprguaamAyRNXHo8RIkVM5s4NC_V8uurBcJQli_XEzgUQlb7YQnQGXH5rzlJzztuNFmbsRIauG2BW_g5YksbsKE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=QHGLwbvjZsHB48FvMF2y34SIw6rkudNqlPyzJUzdgNF1ENNixaxOzW2IdHqRqiE1T0tZClxBbd6wSjapb6I43498BJaAi8HvLmN6dSxcfIEe34M8IYIIjoxOByS2YeGkY_eavw734YGQizKby4w9Aglxeh2RYRIJQl6tQZKtcBNCRz49o7GSO8SPfmdsE9oGLcomZ7R3B1TdKd4cYS3_ZXq5nmYJLvzXQpnPf0IVDi07kw83KoxERS8Ujac2i1MRG8fR5gQvSJsgWlCniA_E7NxHQQ6Lv-wl22KNOdWF2I4Zb_icrQMgZLFXTv8IjCLsaMvPc9xAYq-7tW-tgob-VFMCQpLe_fqG22l2CdYXw05RoSO6YolGTviS1QF2aN0f4MxusDeIF_prIF83RJX8onLTJuo_dGEopfcuNuO7nb6oMnyu-A056xArAtcJy-ov-DJrxFs5IcFXUnVYi12NHcbm2n5sm6lTsoiLUKemstAOn3l3g3s-ymSSAqEav9E8jCgOa2Qk46br0sbUquohbxuJL2bczVhu5ik-F-KtGSH02s7G50XYJbOFwG_oGUhQ9-XIxn0r7LwDKPop9EZaKprguaamAyRNXHo8RIkVM5s4NC_V8uurBcJQli_XEzgUQlb7YQnQGXH5rzlJzztuNFmbsRIauG2BW_g5YksbsKE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">سنتکام ساعتی پیش
از پایان این مرحله از حملات خود خبر داد و نوشت :
🔺
جدیدترین موج حملات خود علیه ایران را به پایان رساندیم
🔺
در این عملیات پنج ساعته، به اهداف نظامی در بوشهر، چابهار، جاسک، کنارک، ابوموسی و بندرعباس حمله کردیم
🔺
سیستم‌های دفاع ساحلی و موشکی، سامانه‌های پهپادی و ظرفیت‌های دریایی ایران، هدف قرار گرفت.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6091" target="_blank">📅 09:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6090">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEZ6vCttlIv0WHRIu0Xu-uXtOSlCnUfYCQQ421BKLETIsH-l-b70q26xDvP96V9zolcuT6St5bPqqH_6gG6rJF71-aPrVJbTPhwhg4cA1_E3Zyd_une0P5CSfo1sjNDG6sjTDatagVcdcADU_0tPTcRZv7HzlLQmD4j-yqPxn9bzE3wAw7obJPLn180gVcGkBFj9EhJOeyaBC0EjMWOtCYeb-zEcNqTmyPFjBLA-rRTnGVSjqHcP8_BJrpREFPS_60jfX7BYnPOXqiNnbzUKm7IvmoHgCL-RbwhqLStyyuzToyL1TR0OwPtN2FTqMWVjQ11G6zxuX8-mkViykwyM4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شب گذشته سپاه به دو سوپرنفتکش (در سواحل عمان) حمله کرد.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6090" target="_blank">📅 09:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6089">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/671b861555.mp4?token=CVIZ63WcdvE-sYBzn69AukNp9rOTN1aCaBxr8TCixnGydLF7EXbIpqnbxGpy0xPO1Sa7jk5kotdvJbErVRwjvYg45Rk4qovDi9DMj1Wi1S4ePV73II36LXl-03gEwP1NVeWVIc59rwaf81IwtCH-PStvwO-1ZNDz3wJEYM1PvtkV8WW_d6Y1ZYKN8PvRB0VQDZxE2j_6dqj79_DzgoMmobQ3OshIgcrScryZVZ1FKDbFEhctuKWQw3dJJiODn_sh3jskpoPLZSMemURCTKloqsY-IvxpsB0kRKbSYxP4zGEzjVwb8Us1rQuEQCanRHXC7_7MyYz1LJt-vYG0ebXcV6Dnt2kjfEJajaH3_ImBnSuKZi2wNKx6eTzQm0a3vEFTpToctYn9Z3HgPj357ZgAbM_SRBxjPEnr8nnKvAiJd81hUPJkhLkIP28KCTRq96h5o8DEPPCfxmcbnygSBOzAtwJr5dtwrwKNXs5SW41EjVbff1iYLnGw5XtIBvSntPTSJqgFgCB8SL2GLSpzetizEQg0Q7s3nLNIQkDCT1tq0p-LR7t3-umMRYtWW-GmdNfT_eh-0FqrATyjFL-mEAZ7cZSssHrxjaHXvO2Yk2qpu6Is5_1MIYyj8jU5DWQeYejSMe41ncfytr1HUAtbswQucXD2IYyg9zDsH90pwZgEQ0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/671b861555.mp4?token=CVIZ63WcdvE-sYBzn69AukNp9rOTN1aCaBxr8TCixnGydLF7EXbIpqnbxGpy0xPO1Sa7jk5kotdvJbErVRwjvYg45Rk4qovDi9DMj1Wi1S4ePV73II36LXl-03gEwP1NVeWVIc59rwaf81IwtCH-PStvwO-1ZNDz3wJEYM1PvtkV8WW_d6Y1ZYKN8PvRB0VQDZxE2j_6dqj79_DzgoMmobQ3OshIgcrScryZVZ1FKDbFEhctuKWQw3dJJiODn_sh3jskpoPLZSMemURCTKloqsY-IvxpsB0kRKbSYxP4zGEzjVwb8Us1rQuEQCanRHXC7_7MyYz1LJt-vYG0ebXcV6Dnt2kjfEJajaH3_ImBnSuKZi2wNKx6eTzQm0a3vEFTpToctYn9Z3HgPj357ZgAbM_SRBxjPEnr8nnKvAiJd81hUPJkhLkIP28KCTRq96h5o8DEPPCfxmcbnygSBOzAtwJr5dtwrwKNXs5SW41EjVbff1iYLnGw5XtIBvSntPTSJqgFgCB8SL2GLSpzetizEQg0Q7s3nLNIQkDCT1tq0p-LR7t3-umMRYtWW-GmdNfT_eh-0FqrATyjFL-mEAZ7cZSssHrxjaHXvO2Yk2qpu6Is5_1MIYyj8jU5DWQeYejSMe41ncfytr1HUAtbswQucXD2IYyg9zDsH90pwZgEQ0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: بیشتر موشک‌هاشون رو از کار انداختیم، بیشتر پهپادهاشون رو.
🔺
توان ساخت پهپادشون رو حدود ۹۲ درصد از بین بردیم. توان ساخت موشکشون رو ۸۹ درصد نابود کردیم.
🔺
یه کم توان براشون مونده، اما برای ما هیچ توانی ندارن. این دیگه تقریباً یه درگیری نظامی کوچیکه</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6089" target="_blank">📅 08:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6088">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3962370842.mp4?token=EPq7cmxrkzM_deT-NDIszZzEzyCaVNpg0toJSmrSBQ2pJ9CnRDo63Z1enVCaQe9KJl0Bi6YtCAhAVifGdiMAMKhRJED-jmbY_QryvrfgYKHuaa64zM5JQG-vTX3sc8Yji8zkG1HWTZG9AFbuGtoaX_nAW2OcysF6U6S_WOlrn_93cg4yIEPRmtek2PaOJ9M5ljKt59JRY1NBhlHLoCM8n9h_GyRNDqJ8VXNT0bGlwLMIESBkSufIgRKAO3ErjnkNjF7ilOtrvQH7AjU6ckNLAQtkyf4BQY3xdeRWXCBKqlI5gKryX_OA8FGUJPuDlOtgGBvIfQ-qxfdXnQopYKFdWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3962370842.mp4?token=EPq7cmxrkzM_deT-NDIszZzEzyCaVNpg0toJSmrSBQ2pJ9CnRDo63Z1enVCaQe9KJl0Bi6YtCAhAVifGdiMAMKhRJED-jmbY_QryvrfgYKHuaa64zM5JQG-vTX3sc8Yji8zkG1HWTZG9AFbuGtoaX_nAW2OcysF6U6S_WOlrn_93cg4yIEPRmtek2PaOJ9M5ljKt59JRY1NBhlHLoCM8n9h_GyRNDqJ8VXNT0bGlwLMIESBkSufIgRKAO3ErjnkNjF7ilOtrvQH7AjU6ckNLAQtkyf4BQY3xdeRWXCBKqlI5gKryX_OA8FGUJPuDlOtgGBvIfQ-qxfdXnQopYKFdWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات شدید به کنارک - امشب</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6088" target="_blank">📅 01:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6087">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
ترامپ : حملات جدید می‌تواند برای دو یا سه هفته ادامه یابد.
🔺
سنتکام : موج جدیدی از حملات را برای سومین شب پیاپی آغاز کردیم.
🔺
باشگاه خبرنگاران : ۷ انفجار بزرگ‌ در بندرعباس</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6087" target="_blank">📅 00:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6086">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
شنیده شدن ۳ انفجار شدید در جزیره کیش
🚨
انفجارهای شدید در جم - بوشهر
🚨
چند انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6086" target="_blank">📅 00:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6085">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
ترامپ : امشب و فرداشب با قدرت به ایران حمله خواهیم کرد.
تفاهم‌نامه آزمونی بود که جمهوری اسلامی به آن پایبند نماند.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6085" target="_blank">📅 23:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6084">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">آمریکا سفارت خود در ابوظبی و کنسولگری‌اش در دبی را به دلیل نگرانی‌های امنیتی، تعطیل کرد.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6084" target="_blank">📅 23:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6083">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a5OczpN4ZOegefZ7kNYHouEz4gXFe8mICaTucZf_Od7Yl5-ggWLZ1oE3OlYSbILcRHPMzuFR8JTn9JzIQ6-LyYt2J4ATmeYc4XPU1Iuz-A0zhQFptXY8whlXrkrZVD-ipnJiuWS8HW-IpZ9efT0QPqs_k_47A82jdJHuGy6mDek6EwKwMUsvanH4WYMLpvlnjzXrcAoRR8ZGT8kb4WQC5PPSgzT5riq_Ay0Hduc_OJdXBjlsVD5brGAOmhqx4SqMR1cikrXxwTB18ZxUHgXQ1zR6sJORXOAAvzq7kd0ypNFamDOAhR2vKoKDeipfBYRD2aC9vLRTsQbei-X6I9i_Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
انفجار در چابهار و کنارک</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6083" target="_blank">📅 22:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6082">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/645219e055.mp4?token=SCSBPIOIyobSYz6UgvbIgWYbfO0efAA3w4YsjF9JLgryK7xcxZUt3OMaDDeLciIa9QesEnnbCkIRE6kVjV0MZ7pImuiU8a2RSucQfCsst227_uN8p774yCSnJwu8McUlqnm1si_5_GJJ2yVApezPgGOVEwMyfI_cSotr-IF5UU2UCuTfFDWsGk6IQFM3aBr0xxpOyN1eNd_4uArfMN6RyFNCLqJLDDBx8KNqsIKlPIDP9QHwfhSGkaWePqCV6NyqR2Dd3-HlyBBEEkx7UZLJTzPZIJuRdOdXkbBNfycW6uMitpZTRQ8brI9trAT60C4R673XG3yCDLbvEH_sIQ_8sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/645219e055.mp4?token=SCSBPIOIyobSYz6UgvbIgWYbfO0efAA3w4YsjF9JLgryK7xcxZUt3OMaDDeLciIa9QesEnnbCkIRE6kVjV0MZ7pImuiU8a2RSucQfCsst227_uN8p774yCSnJwu8McUlqnm1si_5_GJJ2yVApezPgGOVEwMyfI_cSotr-IF5UU2UCuTfFDWsGk6IQFM3aBr0xxpOyN1eNd_4uArfMN6RyFNCLqJLDDBx8KNqsIKlPIDP9QHwfhSGkaWePqCV6NyqR2Dd3-HlyBBEEkx7UZLJTzPZIJuRdOdXkbBNfycW6uMitpZTRQ8brI9trAT60C4R673XG3yCDLbvEH_sIQ_8sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏آمریکا با استفاده از سه قایق بدون سرنشین (شِهپاد)، پایگاه دریایی دیروز بندرعباس را هدف قرار داد و تأسیسات نگهداری زیردریایی و کشتی را منهدم کرد.
این نخستین بار است که نیروهای آمریکایی در نبرد از قایق‌های تهاجمی بدون سرنشین استفاده میکنند.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6082" target="_blank">📅 22:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6081">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‏
🚨
🚨
محاصره دریایی ایران از فرداشب ساعت ۲۳:۳۰ دقیقه اعمال خواهد شد.
‏بر طبق قوانین اعمال یک محدودیت تازه دریایی باید ۲۴ ساعت قبل از اجرا، به صاحبان کشتی‌ها اعلام شود.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6081" target="_blank">📅 21:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6080">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be724e9f8e.mp4?token=F7r6KTDYBKVOy0aV24t2_4yivtpiCgpMJfOt5l9X6OlsolYlZUB3DB4OWpC3uC2pQlN66TxbH0Co_4NQN72fItEU9SnEXXV8DlNl8R_ohnZyXgVRI9C44YWdSgL5rd8wUjB1eJkrVMts8bRDMXf6AZE2K-ffGUqSoPDXk71PCsT-iWW5nGQfCDIo1w2-ZawYBCZny_FyWpVbrq9pwEc1COuP2nHAaZrQCAwiOCxKK8QvCARni8aL0SQrCvzdXk2dWRBGG04UdXl8kaINnZGKvi8GYMMHlChpJpHrFcD4-OUhOL8yndBNqrpd6fYWJi7O9h9Vxb8k3-RBF6kENGQRahHeHTg1AWvx1DTHHcj7GS2ZfcwW8h4beZPVoE9yrTVl4vn7JGBLr28vhR0BcuWSAkZ6nz3ogEO8RkiWFvRXzNggmWq5vgyoaqzANS9PSgHjqE8M0Po-FAkgCZJcop90b8tRVnLaNSjGYqpITI5o5sBQfjtVu0LSW_RCskxA4ih41aj7cEMlDQt6t3C5tXGu2wJHngPX9GWNsFxgF3gJDlKEQ6oBIXy2yvWxp8hSsA1zbhyF11l0S6gv54w9kmXy7ODq9J7oS4XsVaVbnzfZFkPKxHzmvReQJNmY4RHqaw5BkaVPuTFoMI88ydYbJ73i9re9SXGNXMXgmyspSd7xcUo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be724e9f8e.mp4?token=F7r6KTDYBKVOy0aV24t2_4yivtpiCgpMJfOt5l9X6OlsolYlZUB3DB4OWpC3uC2pQlN66TxbH0Co_4NQN72fItEU9SnEXXV8DlNl8R_ohnZyXgVRI9C44YWdSgL5rd8wUjB1eJkrVMts8bRDMXf6AZE2K-ffGUqSoPDXk71PCsT-iWW5nGQfCDIo1w2-ZawYBCZny_FyWpVbrq9pwEc1COuP2nHAaZrQCAwiOCxKK8QvCARni8aL0SQrCvzdXk2dWRBGG04UdXl8kaINnZGKvi8GYMMHlChpJpHrFcD4-OUhOL8yndBNqrpd6fYWJi7O9h9Vxb8k3-RBF6kENGQRahHeHTg1AWvx1DTHHcj7GS2ZfcwW8h4beZPVoE9yrTVl4vn7JGBLr28vhR0BcuWSAkZ6nz3ogEO8RkiWFvRXzNggmWq5vgyoaqzANS9PSgHjqE8M0Po-FAkgCZJcop90b8tRVnLaNSjGYqpITI5o5sBQfjtVu0LSW_RCskxA4ih41aj7cEMlDQt6t3C5tXGu2wJHngPX9GWNsFxgF3gJDlKEQ6oBIXy2yvWxp8hSsA1zbhyF11l0S6gv54w9kmXy7ODq9J7oS4XsVaVbnzfZFkPKxHzmvReQJNmY4RHqaw5BkaVPuTFoMI88ydYbJ73i9re9SXGNXMXgmyspSd7xcUo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpU1CsCEY7vWaaYKWHfUnGKHUg9qIEhLz60hCzbLkl488cRqGjc9oKbmwC07z-0zlRKKXm29QbhhqOinrx1Et5fvWgBzURLmxVdy6U-fQR2OP3ZdUbP6r2JdMW_IwOaIbphN3ayCmL9V-2DWpEPEGAnQCTS6MBogtUCO0rlHaeJ2KKBJzNVlPH0FzZNhEbGrWq65cRISPz5qROGMYEy3xUn3I0MK2L8diFq5TKyVldUCaGHqWqwmLN4OrvUhNaTNSSqZSkTHXOAXCFi_jF3rMjJRewR-xIoXFEJRdlupvhoNzYW9KYhC3Z0f-FL_Yg50zmYe9w1MSlX2OI3KnneMVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5A7hSiilX8ySRPUfpt7SM6gGd9AWl2pGHsu0KTR2Abq8L9PEWRba-4ZOzkFdZRc2sdj_-sdAdV-3MTLqsznmmnO0w0rZleSE7pYf5Z9Jqd8rZ3tFbGAN7F1AHrf-SkVCGLI1PF0lpcgMSuSwvuXXxmeu2Hwx_MqkLyQJXWbN2PTAHnz7XQ2Fl5avY9o5CAeP3kCHdzAovljV5lkhoXSk4l7ozS8lNXjaEZ8SP_j4arIk9eYRblVELVwtrQWu32j5dBOLrh6uhiK3eK21TlZNcE4qIZltDIj_Srbk1daZrg4FAPEdi5NUWip9BfvgvenxlxdBjxBtZfgjoIS2KV7fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6078" target="_blank">📅 17:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6077">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZhDEl-zMq98m4YGSPR4Phef0bPQ4LQ8rqsyc-2Hv3MyPHysGxYgg_57ScwzCnICzI8C5lOY1qQSz7wvaa1qWI2Yk5xWKvPCjFrOQbRlofIuk7iPqN7AoKDyEwfWUEORipGPF42mthmcxHRPKHMyIXwTK5czLEIHrY0u6IUKdv388f5DJ0SVfoNi2SCT76mOY3sFyR2448N7Af76SwoFAXQbPLr2V8qMg11vnE1SBQIMejuKvM28l8KhHh8lkSgts2lOC2CdrsMck__s8KL_ACOIsoW-owW7mTFGXIGvsKrHPZuLBppNzdKHAfbSzhgDhx3SJEqfpYxYAX7ksn0Zjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6077" target="_blank">📅 16:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6076">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامپ درباره ایران:
‏ما کنترل این تنگه را در دست خواهیم گرفت. احتمالاً مدیریت آن را نیز بر عهده خواهیم داشت.
‏ما به نگهبان تنگه تبدیل خواهیم شد و وقتی این کار را انجام دهیم، هزینه آن به ما پرداخت خواهد شد.
‏ما ۵۰ سال از این تنگه محافظت کردیم و هرگز پولی بابت آن دریافت نکردیم. بدون هیچ دستمزدی از آن محافظت کردیم، اما حالا از این کار درآمد کسب خواهیم کرد.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6076" target="_blank">📅 16:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6075">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
دولت بریتانیا سپاه پاسداران را به عنوان یک
سازمان تروریستی
اعلام کرد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6075" target="_blank">📅 15:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6074">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">عربستان برای مراسم ابراهیم رئیسی «وزیر خارجه»‌اش رو فرستاد! برای مراسم خود خامنه‌ای، ولی امر مسلمین، این بار «معاون وزیر خارجه» فرستاد :)</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6074" target="_blank">📅 13:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6073">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPk-F5Ar2Ql3D6qVEAOjzzfXDu-Uv4qhYtyE-z7NwEssCsUs29scM6XZtA80dSjx1fHmmcd0aJEPUP0bHZ3cnpTHG_tb1tu0CT4c3lB3IC_r77UxEby0E0A-Zf5mdKrfkBnct0pccBSiUvKR2-sF6NA7OwexI9EmBMXsndYknQgK9lUcEReqgS8NSry3N921k8iJI_9a3mM4maQyrT3HoxS9HboaaLNZmJSvVA2fpgwtXDFrDTfnaerEzAL9dy0hNp59K8vlAO7Zj70QK4u49rMx8F6CpoWTwQ7TdX9VAfsX23N6n1EpYGv-8gEfiALJOigVfm25_9ufbKXu-GSOmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای مراسم «ابراهیم رئیسی»  شخص امیر قطر به تهران رفت،  همراه با نخست وزیر قطر و وزیر خارجه  قطر،  اما برای خامنه‌ای،  سطح هئیت قطری به رئیس مجلس  تنزل پیدا کرد! قطر اهمیت کمتری برای مراسم شخص خامنه‌ای شد! از اثرات حملات جمهوری اسلامی به قطر!
🔺
این مدل احترامی…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6073" target="_blank">📅 13:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6072">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bXIADZzGKfQv-8ywmNoznOnLcrjJXxQr2VAci440NeiOP8G-3WoCF8QcNifrOi4GYp8fZkesQEe6NvlWhw7lUtl2FtGr5eYNgK6iW7A4UOExW4v2iJhMKfcuScp4cM_5LwTAJvDns3H_65kopCjdzRbGp7VoMyQZleer4h4X2cAVettTCgSlMr5aargVvPtwf3CE4SJMu2RNb-begFvtaP89siHAeHXNCN-qCD_BKIFtDvd0f58_9Lwwq_FIS-TTl5YVHdTenPjIAfN3nq0pGHoSRlqLN-p0d3khsnWP3nN96yZKUhTY5Xkuvm8Qw-NLln_8l3WaHAy9JKWGGhoLYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6072" target="_blank">📅 13:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6071">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2umuw8Ts3xNSR3q-wJ15MJJ5C0HhZ0GNkoSdiIyOFaewvCRpk7rs1aDSsquZn4IXhbPxZ4R4HM3Qh86TinrojCkBwn-8yuxRJcBNGG_XfNUhb0uP_xUCa7pmE2SnQ72l4WpoNPeChuVG7UOuP-JfXJOgMPwF0Qx_FBoMWPedDHr55g0OrM4usXM4wl3AXoJ69TaQ2ZmpsZIiB8supvFwYjYF0NdDN7KzWLjvEqvcORL_4-1zEbQCFtm2L4zjXJMB0SJAxxdMmJvrx-z6-4tnY2j59MhIxRBCnoIhY_NEn6ZvhkMbxR5yfCOCqkzd7ZJTmmfpLtE_Mr7Xquet3h4bw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/868ebce267.mp4?token=u5aU0GtxZcBrMIzyb3xri1dW3ZpO8EiS0xbW591L7EKOMieO_YJOJUAeJPgFnjQy5jojYvmCYElb0apvqUf6UMd36JEP0XD_Q1oF2JHA215a9T4NJ8ftwqVJCjlWJUoKd4XGRXcpdbDqCznski98s8DScFwUZK6uH0zh5X9KKOdqaVDxMfx2mJPpvYo4CFIh-kKCCDCXhnkRFxR6Uxc7TbPhOPOF8g0ZzPU9gD45MuRdSXFKV4X_F6LY9PJ4yg0yew2m3wIIM5B-zIr5WWrfKYN39i0KcETDKo755b5HUAvPR_Ncj7bgVJfR4P70q-LgfsHaL9VSs0l5i9HUCFK5qiO5yCI4bUeTi-tV1iI-WT935mZr8o5VPHMjZWpjFdI_8fbNXsDKGJtahFkQd4uxJWyryVWkIDESb-mgCo4n207F58X71Jbd_1vp13AOA9gbMQHE4lf4AE0T0zL8zEFRjWjfoLgQrTyOpbqaM_RBBNxCPpq3YgdPIiwdNr6vUeevLfqqBI7LEmhq8ocXwC8qdZ6obAuBfYabrwF7Yszav8-qirYMJeVrIgKbhFfGEvz96xAKo3iYZIIUsp3Ilj-wi6jnwmaizRnzgwF1U6yn2TVFysGjW9KHJeE8ThJLeK0DY1339NjW8WrZYQO3SnZxny61Ddv5d9Z5BnBTn8qzQZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/868ebce267.mp4?token=u5aU0GtxZcBrMIzyb3xri1dW3ZpO8EiS0xbW591L7EKOMieO_YJOJUAeJPgFnjQy5jojYvmCYElb0apvqUf6UMd36JEP0XD_Q1oF2JHA215a9T4NJ8ftwqVJCjlWJUoKd4XGRXcpdbDqCznski98s8DScFwUZK6uH0zh5X9KKOdqaVDxMfx2mJPpvYo4CFIh-kKCCDCXhnkRFxR6Uxc7TbPhOPOF8g0ZzPU9gD45MuRdSXFKV4X_F6LY9PJ4yg0yew2m3wIIM5B-zIr5WWrfKYN39i0KcETDKo755b5HUAvPR_Ncj7bgVJfR4P70q-LgfsHaL9VSs0l5i9HUCFK5qiO5yCI4bUeTi-tV1iI-WT935mZr8o5VPHMjZWpjFdI_8fbNXsDKGJtahFkQd4uxJWyryVWkIDESb-mgCo4n207F58X71Jbd_1vp13AOA9gbMQHE4lf4AE0T0zL8zEFRjWjfoLgQrTyOpbqaM_RBBNxCPpq3YgdPIiwdNr6vUeevLfqqBI7LEmhq8ocXwC8qdZ6obAuBfYabrwF7Yszav8-qirYMJeVrIgKbhFfGEvz96xAKo3iYZIIUsp3Ilj-wi6jnwmaizRnzgwF1U6yn2TVFysGjW9KHJeE8ThJLeK0DY1339NjW8WrZYQO3SnZxny61Ddv5d9Z5BnBTn8qzQZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانال ۱۴ اسرائیل با انتشار این ویدئو خبر داده که ارتش آمریکا شب گذشته با بمب‌های سنگرشکن به یک ‌انبار موشکی در اطراف پایگاه چهارم شکاری در دزفول حمله کرده است.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6070" target="_blank">📅 08:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6069">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f4228d97a.mp4?token=dNiNd2ca2i2NuSgZK-2PiHkIKpKeI8WUpuV63AmNpqN9R2adUEvpY5s403mXDmOedU4bDYk_2qqLHdYDnG2OCNd8dKBE1VA2MDn8VvgTTE5T6kFj2CpMnBnPSydWGr56fb1pzsB28HlX4rSdVUuctlZL-6lJpVc4FQl2yNP76u1ck0C9YUbss4LPn-pGXmQ7I4eOmEYX7TTAO80_wQxwO3rQracQd-BMmDIlX_UxH4qb86gEgd_toWVwUM3cxJuOSpbmhflHcbRc-caaf6Lly1eJnwer7g3Q_fMlRF0Q8IV134Zk-QODtThwFdXw4JL-hkol2sRSoBOrn2XpGOZ5l5yF1HmNGCbPctmMFvinW7GoUYQ8uUTBgUJ0CreWP1ndklNK6lxy086B3HJ_ErLcN9JKdKMXCGybeUSVJiUZ5IJap-bosgF1VfqgYnIHu2Ftjt-hOb1VOHLpg2t8G1BYewJ9Rh9D9byjeEP3pX1icOoukvUl_GC77f7MrA77dsqxb-rmPTqawk_Ja7TxL5pbqvtwZ0zsTiF_XBOjIpli8eC5jpBrlgkMPCLzsAF1YgsOhvWos1frjVhbZ-O56iS7x_Pv-7cRxq1vbKD9KIR-UrfgIyqpl5Q0I5T4NyfvaTCtXd2YwdRON7pLi9O0R0BEE5oYwfFq8KLXObpPUYbCGWM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f4228d97a.mp4?token=dNiNd2ca2i2NuSgZK-2PiHkIKpKeI8WUpuV63AmNpqN9R2adUEvpY5s403mXDmOedU4bDYk_2qqLHdYDnG2OCNd8dKBE1VA2MDn8VvgTTE5T6kFj2CpMnBnPSydWGr56fb1pzsB28HlX4rSdVUuctlZL-6lJpVc4FQl2yNP76u1ck0C9YUbss4LPn-pGXmQ7I4eOmEYX7TTAO80_wQxwO3rQracQd-BMmDIlX_UxH4qb86gEgd_toWVwUM3cxJuOSpbmhflHcbRc-caaf6Lly1eJnwer7g3Q_fMlRF0Q8IV134Zk-QODtThwFdXw4JL-hkol2sRSoBOrn2XpGOZ5l5yF1HmNGCbPctmMFvinW7GoUYQ8uUTBgUJ0CreWP1ndklNK6lxy086B3HJ_ErLcN9JKdKMXCGybeUSVJiUZ5IJap-bosgF1VfqgYnIHu2Ftjt-hOb1VOHLpg2t8G1BYewJ9Rh9D9byjeEP3pX1icOoukvUl_GC77f7MrA77dsqxb-rmPTqawk_Ja7TxL5pbqvtwZ0zsTiF_XBOjIpli8eC5jpBrlgkMPCLzsAF1YgsOhvWos1frjVhbZ-O56iS7x_Pv-7cRxq1vbKD9KIR-UrfgIyqpl5Q0I5T4NyfvaTCtXd2YwdRON7pLi9O0R0BEE5oYwfFq8KLXObpPUYbCGWM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6069" target="_blank">📅 08:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6068">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=nzOQNv7SPi6htRkMrOZtV4w02AbWaSUSgFb45emyUwRTEVFmYDmaFONCIOjy0ZiCFtUE_9ZaE5up2snIwSLsmM_Nb0Lr6RycmKu6z_ABALI-KY6CF-G6iyxXfq0oXg_Cyp1_eO9hvWNOMELI4ghlKcW-ubet9rteeoBrnQawl2a3jvixo4Ah-9LzXcMcGACndMYU_hwRWb9U2rJp2tQo-0CdwCR6f55aADKQ_XOdGpGSoWHoRokcIcqCuQ-CSegVZwGp5OcIlp3ogdeOPrc_h1WoS6fICN0-TuCPHKECBOmQTqif9WFq8FGeZrfpYdW9c5YpvBEE-j8GjEPb_fIVFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=nzOQNv7SPi6htRkMrOZtV4w02AbWaSUSgFb45emyUwRTEVFmYDmaFONCIOjy0ZiCFtUE_9ZaE5up2snIwSLsmM_Nb0Lr6RycmKu6z_ABALI-KY6CF-G6iyxXfq0oXg_Cyp1_eO9hvWNOMELI4ghlKcW-ubet9rteeoBrnQawl2a3jvixo4Ah-9LzXcMcGACndMYU_hwRWb9U2rJp2tQo-0CdwCR6f55aADKQ_XOdGpGSoWHoRokcIcqCuQ-CSegVZwGp5OcIlp3ogdeOPrc_h1WoS6fICN0-TuCPHKECBOmQTqif9WFq8FGeZrfpYdW9c5YpvBEE-j8GjEPb_fIVFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات موشکی سپاه به کویت</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6067" target="_blank">📅 20:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6066">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">فرماندار قشم از اصابت ۱۰ تا ۱۱ پرتابه از عصر امروز یکشنبه دشمن در جزیره قشم خبر داد.
حسین امیر تیموری افزود: تمامی اهداف نظامی بوده است. خوشبختانه این حملات هیچ تلفاتی نداشته است.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6066" target="_blank">📅 19:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6065">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=sr60ewZT4XuePkLG_epPqNfvvs8cxvWxc60gsm3pFAg68z53EtF8BEo7G9I-wQ0On1wDSQmteLewZqVYFqIfOqarysnzJuP47HMnVx-Ec-rPVGvMZlLMhxyjbv-Nfb7zlzS5QCRE1acuYQJGIdJ2uT0PkshiHxf6nDAZxeOk3PTxEhsaXOo7CvvuVUW8F58bJT6Jt78nXcvvzjNJpt0Z4jixGbp9dRM8qnonZKtACs7f5ayvueF4AR9jZrHI0jaPE_G3G4w0NDJNtS9P7CdSKafjNGJTtVr56Bd3f6nlZ-uiKnTSXCAjpinK8KZyeMv4kR5egMKBTBQvkM_0aBjl2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=sr60ewZT4XuePkLG_epPqNfvvs8cxvWxc60gsm3pFAg68z53EtF8BEo7G9I-wQ0On1wDSQmteLewZqVYFqIfOqarysnzJuP47HMnVx-Ec-rPVGvMZlLMhxyjbv-Nfb7zlzS5QCRE1acuYQJGIdJ2uT0PkshiHxf6nDAZxeOk3PTxEhsaXOo7CvvuVUW8F58bJT6Jt78nXcvvzjNJpt0Z4jixGbp9dRM8qnonZKtACs7f5ayvueF4AR9jZrHI0jaPE_G3G4w0NDJNtS9P7CdSKafjNGJTtVr56Bd3f6nlZ-uiKnTSXCAjpinK8KZyeMv4kR5egMKBTBQvkM_0aBjl2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که این ‌تصاویر از نتایج‌ حمله امروز آمریکا به جزیره قشم است.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6065" target="_blank">📅 19:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6064">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
آغاز دور تازه حملات آمریکا
به شهرهای ساحلی جنوب ایران.
بندر عباس و قشم مورد هدف قرار گرفتند.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6064" target="_blank">📅 19:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6063">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">دوستان عزیز
این رسانه کوچک به‌صورت مستقل اداره می‌شه و در ۹ ماه اخیر، به خاطر شرایط خاصی که در اون هستیم، همه زمانم رو گذاشتم روی فعالیت شبکه‌های اجتماعی.
اگر این محتوا برای شما ارزشمنده و اگر مایل به حمایت از ادامه این فعالیت هستید،
این لینک پی‌پال در دسترس شما :
PayPal link :
https://www.paypal.me/Farahmandalipour</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6063" target="_blank">📅 18:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6062">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4bc671310.mp4?token=p-ykQn7Ex0X89D-3-xI7rJM2GYtEfTiWbA6_tkuZqD63Wt-9pi9TLtqVBGl6NAXvT8QgwmZMGauAZda0ml7MPyoQlxyPVux145BjAgCAiar5vGX-5-g4OdVJ2cap0WjqrBfGoRX88aZhecmrNCXM2TPdnAXSN98c4F25TAVPfL2OiXfaJlECjqsOi8YAOeuA2MPlTuWTQD6VsmQi9pxAdRyf99SNEiidi45V2eXhP3z8KyNEXi6_52wGZfb9tjJU5WiPsVslt5xQYczKSBOD61bI37UNsn400r-wk8qVcQ65wWAVoiuy0ERK8kV0ySH5ewDfnqTK1uvwttonIH8L7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4bc671310.mp4?token=p-ykQn7Ex0X89D-3-xI7rJM2GYtEfTiWbA6_tkuZqD63Wt-9pi9TLtqVBGl6NAXvT8QgwmZMGauAZda0ml7MPyoQlxyPVux145BjAgCAiar5vGX-5-g4OdVJ2cap0WjqrBfGoRX88aZhecmrNCXM2TPdnAXSN98c4F25TAVPfL2OiXfaJlECjqsOi8YAOeuA2MPlTuWTQD6VsmQi9pxAdRyf99SNEiidi45V2eXhP3z8KyNEXi6_52wGZfb9tjJU5WiPsVslt5xQYczKSBOD61bI37UNsn400r-wk8qVcQ65wWAVoiuy0ERK8kV0ySH5ewDfnqTK1uvwttonIH8L7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مثل باباش شجاعه :)  باباش هم در جریان جنگ ۱۲ روزه چند هفته رفت «کمین‌گاه»! برنامه‌های شبهای محرم رو هم نبود تا شب عاشورا (دو هفته پس از پایان جنگ!)  که دیگه در جنگ ۴۰ روزه غافلگیرش کردن</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6062" target="_blank">📅 17:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6061">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a80edc91f4.mp4?token=RYg7tFyN48fKC2K-K-NXCPDq8RgzmHB5QluIrmHMm5m74SEhOqyM7H_1NobO5UpmcVddoHV73KoFOqFMGhSJNqV0uiIrG7GP6BlAaCC1ITznGeu9XwqMfwUu3t8no9an2sMkTCb9e71qO8N8k75k4AIuLmCc4t1iuQUZ4mp3NB29QzSaij0dHzIxdSDnDHgdW0MS3I3DRdsbxpZBEVqkGAkVDy2VEf8I1aDQMfn131UppUto26NZDY4crhEWmrGI1Gl44CD5jj4W4QKsLyXU1utB8mQkLyQRyvZE-PgDXrZxgrLnrBcQiCVOGY01JlSy7vObyen9tKPTO1Fwl_9VzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a80edc91f4.mp4?token=RYg7tFyN48fKC2K-K-NXCPDq8RgzmHB5QluIrmHMm5m74SEhOqyM7H_1NobO5UpmcVddoHV73KoFOqFMGhSJNqV0uiIrG7GP6BlAaCC1ITznGeu9XwqMfwUu3t8no9an2sMkTCb9e71qO8N8k75k4AIuLmCc4t1iuQUZ4mp3NB29QzSaij0dHzIxdSDnDHgdW0MS3I3DRdsbxpZBEVqkGAkVDy2VEf8I1aDQMfn131UppUto26NZDY4crhEWmrGI1Gl44CD5jj4W4QKsLyXU1utB8mQkLyQRyvZE-PgDXrZxgrLnrBcQiCVOGY01JlSy7vObyen9tKPTO1Fwl_9VzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا بگذار مجتبی از «کمین‌گاه»  بیاد بیرون، پوستش نور آفتاب رو ببینه، شما هم به جای هوش مصنوعی، قیافه خودش رو ببینید، ببینید اصلا چه شکلیه، بعد به نتانیاهو بگو بترس.  راستی گفتید مجتبی دقیقا از ترس کی  ۴ ماهه قایم شده؟</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6061" target="_blank">📅 17:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6060">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDOpTyFQnMnrxquuh7bgaz5k-o1d0K0wdW_lsxicyguCoiYALCD82tKvS-OOlsOxeI9eInwO8PlmLC0yblYSoEf0EvbgMm_p4U7B0LGFriZX5GtNLKPZ74XaUIwM8lj_SLs3jHahcMsy7Dq9BWJ3DW3Bcq2_p5Mz3CXlTysfnzxYl3ZgU76JI-brFDqGXd6zsIh2zDoIDurSPP9xAzVBPhUNR5ybtK4HC5V6_7ed4IgJUTDThvCggNsMZv8muFTotqY1aZi9o4x2_JCvOIn3bDQL8nW34DT6vwyVdrZADgkdDXqpbR0v7A8gSShK8WXS368QL7cdCDTgdhYJTJANjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا بگذار مجتبی از «کمین‌گاه»
بیاد بیرون، پوستش نور آفتاب رو ببینه،
شما هم به جای هوش مصنوعی،
قیافه خودش رو ببینید،
ببینید اصلا چه شکلیه،
بعد به نتانیاهو بگو بترس.
راستی گفتید مجتبی دقیقا از ترس کی
۴ ماهه قایم شده؟</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6060" target="_blank">📅 17:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6059">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jbdb1qbVo-_uuYPWWkiaIBbJlTlz6NYbeYaoJPQ_d06yHGG_0WdyOzR0MizLjIXtGn9jxoeZq6gDUkJNYwHCVwlGqvlnD8TBigeSsDxIAg1hDo_jPuXHqOyruGpm8cou8KTmSIXtadIntyp2x-JfNRoo5MrhvdL5WYz_BfLVofKP87fr6MCANLQzJ0WDNiZepRLn_vP1-PWOnx7BrMUFq2nDfRsjjPWGcBH76tGjWNHu9SuItwgevcKvJbrYeXxFdrdFjQ4Pgmf7oNzx_vSIpgXnY5Uc_CTDoZsWE45j12xFquiu9_UwDdVWdGfUzl1hNlCYPm1RJPT47MSLRQ4uGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشهد  از فردا : روزانه ۲ ساعت خاموشی برای منطقه.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6059" target="_blank">📅 16:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6058">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec46cc2c8f.mp4?token=iP-FTmeHrrPiCrOQLbeJEhNk1IK9W76-UD0oNI2FLWBDS7siFhBAclfZdIQD5HAKQHGlCIYorZtK-0S-zmcn_vMaQ_BbY-W2WkH0759hK6-UIKeh_DQwEzY1MB_vDB-WZuAZM6FAAqFu3i10qHVJwE-PQsQgwbcimZa6P4NOLI-Saw5HwUM5Uktz4289R6qUS_DRO-hJSy07n7H7_AJUtxQHB-K2kyhzMy-_1ojCAs3pIOPkXc6DrwylAmIdUh4cd8oFcetWkjnvIhrIaxcIoJ8Ji3_XG_Mj1vxmkI7QoDplJunGColi-gUYeAXKHiFD4VOECuF7VO1Yu_P_5Z1Uyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec46cc2c8f.mp4?token=iP-FTmeHrrPiCrOQLbeJEhNk1IK9W76-UD0oNI2FLWBDS7siFhBAclfZdIQD5HAKQHGlCIYorZtK-0S-zmcn_vMaQ_BbY-W2WkH0759hK6-UIKeh_DQwEzY1MB_vDB-WZuAZM6FAAqFu3i10qHVJwE-PQsQgwbcimZa6P4NOLI-Saw5HwUM5Uktz4289R6qUS_DRO-hJSy07n7H7_AJUtxQHB-K2kyhzMy-_1ojCAs3pIOPkXc6DrwylAmIdUh4cd8oFcetWkjnvIhrIaxcIoJ8Ji3_XG_Mj1vxmkI7QoDplJunGColi-gUYeAXKHiFD4VOECuF7VO1Yu_P_5Z1Uyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوینده شبکه خبر جدی جدی
خبر درگذشت لیندسی‌ گراهام رو دوبار خوند :)
فکر کن تاثیر یک سناتور آمریکایی رو
در برابر کل نهاد مجلس خودشون که ۴ ماهه
کلا تعطیله و کسی هم اهمیت نمیده :)</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6058" target="_blank">📅 16:16 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
