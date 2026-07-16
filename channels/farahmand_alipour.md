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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 09:44:46</div>
<hr>

<div class="tg-post" id="msg-6146">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S67FAPbGcSIj2mIMHB3rweXRNd9SeixdnSv8uvrcwW8nnvOtbl0mhQ95jnqSUYbjvGfmho4R6Ei5xQ40o39fj6JfxvGefHFtdDyo6aRh04UmLkVAAsInsKYlzqmuJQs-18faNQ3hC2c7FxONqK1LlxGO-S1wt1buPHFkbTI0qzrEdES4bLTCIb1DLuPjKH07FY6wjWt8Eij3kbViicG7zHZ9WI0tf7C-ipY4FwP2EijBmkd7tORJMqhhusXvszV6kuPkLvoCs7cJuq5qjLeuY_2tMU-eNnXll7N5m2QAlPS0koNASticS7RQENihNJiJvW3sqJXqvNtUahktGgzXuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ایران به یک شهروند زن آمریکایی که در دسامبر ۲۰۲۴ در دوران رئیس‌جمهوری جو بایدنِ خواب‌آلود به‌ناحق بازداشت شده بود، اجازه خروج از کشور داده است. او اکنون در سلامت کامل در خارج از ایران است. ایالات متحده آمریکا از این ژست حسن‌نیت ایران قدردانی می‌کند.</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/farahmand_alipour/6146" target="_blank">📅 09:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6145">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/farahmand_alipour/6145" target="_blank">📅 09:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6144">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">استاندار مرکزی : شب گذشته به دو نظقه در اطراف شهر خنداب حمله شد.
این برای چندمین بار است که اطراف شهر خنداب مورد حمله قرار می‌گیرد.
نه آمریکا دقیقا مشخص میکند چه اهدافی را زده و نه ج‌ا می‌گوید به کجاهاش خورده.</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farahmand_alipour/6144" target="_blank">📅 08:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6143">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اطلاعیه  ارتش:  سامانه‌های راداری، سامانه پدافندی پاتریوت و مخازن سوخت آمریکا در پایگاه علی‌السالم کویت را هدف قرار دادیم.
‏ رادار‌های سوپر هاوک، تأسیسات و سامانه‌های پاتریوت واشنگتن در پایگاه شیخ عیسی بحرین نیز طی حملاتی، آسیب‌های جدی دید.</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farahmand_alipour/6143" target="_blank">📅 08:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6142">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
استاندار سمنان : به بخش‌هایی از فرودگاه سمنان حمله شده، کسی کشته یا زخمی نشده.</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farahmand_alipour/6142" target="_blank">📅 08:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6141">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAn2Rhw6MG6nUjkdmcJSlFMjL-HZVXD_LhnzWuhO6nAT7foyaLOQhDi7Fpk3aDpNU_YRpLkVFdOM2d2AQUnLueSAd28tre0PkbGARbX6AbalhclNxd9blwOmYQPwBfOE8eHEUtslFt_JkQuKPSxFKih_wrX-reObp9UPdFTCZxQBizFwDmJs1ZccE0-wh-ZItW4uMHGXMFV8VTxh00qbSs6y6G58R2DF51lOtxcxWXH7VNkJ-6BYxkMSbs_VWmyQ4CfdDkbXQlK-Qrch_3Pjc9ox2-uy9k8D7ht7_ySacrDYQvwv6aUddBJx7z8GXAHo7RPrvowI3N-LssBt5r__Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین یارو خودش از دست سپاه و نهادهای زیر نظر خامنه‌ای  فرار کرده و به آمریکا پناه برده!
و آمریکا رو خونه امنی پیدا کرد برای زندگی و نوشتن از اینکه اسلام چقدر زیباست و خوبه و سعادت انسان رو میخواد!
حالا از همونجا به ج‌ا میگه مبارزه کن با آمریکا! مطلقا تسلیم نشید! تا انتهاش برید!</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/farahmand_alipour/6141" target="_blank">📅 08:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6140">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">برخی گزارش‌ها از تداوم حملات به اهواز خبر می‌دهند و اینکه تاکنون ‌۹  انفجار  مهیب در شهر شنیده شده.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6140" target="_blank">📅 23:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6139">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
چندین انفجار مهیب در چابهار و بندرعباس
🚨
کویت : امروز ۲۱ پهپاد و ۴ موشک شلیک شده از سوی ج‌ا را منهدم کردیم.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6139" target="_blank">📅 22:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6138">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای ۲ یا ۳ انفجار در اهواز</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6138" target="_blank">📅 22:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6137">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1IRIhMok3xsIlQAiQSYxJYWubrCgyya2gHbNsRAwnnq3-wKqo-DcDjeQHNEzHNtTB89jeCvWltrb61PK1cr95znfSRukDWNlcOmx0HjxL24aqcfS-D5vx1ZEIFj0UO_RIafa9x1z8G6WSiQzsHPyK2MHBWoXNrEhKVzIgigaeCaNTHHoD5xADbRbJP-V6QNhQgLNuxK9aS_vETJ5ckRT6CLLJQP6ZkIM4eAT8ofx3AKPHeaVY5ZwBgJ3MZoXzZU_-nRTpq0rglt1dFNonbmk4kAszGpcrqSTDaEQ2QB1AKOmjH4EPGSPZxVHkVgNJVFIXfsHlJy7faUnONVhsb7Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شما دیگه جرات حمله به اسرائیل
رو ندارید! خودتون هم خوب می‌دونید!
این ۴-۵ روز هم به همه جا حمله کردید
به جز به اون کشوری که بیت‌رهبری
رو زد نابود کرد!
و نشون داد دقیقا کجاست که سست‌تر از لانه عنکبوته!
ولی هر چقدر دوست دارید شعار بدید!
اون حزب‌الله تروریست هم رفت انتقام بگیره  هنوز و همین امروز هم نیم میلیون نفرشون  توی محله‌های مسیحی و سنی لبنان آواره شدن!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6137" target="_blank">📅 20:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6136">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">آنچه شب گذشته در بمپور رخ داد و موجب  کشته شدن تعدادی ای نیروهای ارتشی شد، قابل اجتناب بود.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6136" target="_blank">📅 20:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6135">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e615d142.mp4?token=t5bsUkX-IeEFYc-YKvCCy9f2SEvxB9RMzrzuXUzsgFJo_X3TvvVdU9_i4Kmr0TL7gbXqYJHZFHsKFSjbACt-GTX4vTZ_xQOu-faBmsWhgDXiJXVN_K0CxXG0FZZuDvQ0HlVLduZu_zrQsR-p5baxal3lcxAAwITMkPqWuact3TIUcoUxxou2Iw1H2HxWuBwv2e0dHhLtV7G9zTwCOwq5dyFdK-6whBnTGJ1igqyoSrW3D7QMPoUaRlT_K4Hgqo64oUqNjeMkJ0h6taCVlzEiiEt1VQgRATitKGCDmbktw96wL2nYE_zeo2r6mnZyXva8Ijdt8oKUnU9ixnWxjnO7dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e615d142.mp4?token=t5bsUkX-IeEFYc-YKvCCy9f2SEvxB9RMzrzuXUzsgFJo_X3TvvVdU9_i4Kmr0TL7gbXqYJHZFHsKFSjbACt-GTX4vTZ_xQOu-faBmsWhgDXiJXVN_K0CxXG0FZZuDvQ0HlVLduZu_zrQsR-p5baxal3lcxAAwITMkPqWuact3TIUcoUxxou2Iw1H2HxWuBwv2e0dHhLtV7G9zTwCOwq5dyFdK-6whBnTGJ1igqyoSrW3D7QMPoUaRlT_K4Hgqo64oUqNjeMkJ0h6taCVlzEiiEt1VQgRATitKGCDmbktw96wL2nYE_zeo2r6mnZyXva8Ijdt8oKUnU9ixnWxjnO7dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیش بینی تاریخی بختیار
در دو کلمه، برای مردم ایران</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6135" target="_blank">📅 20:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6134">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6134" target="_blank">📅 16:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6133">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6133" target="_blank">📅 15:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6132">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
سنتکام : به تنب بزرگ حمله کردیم.
در جریان این موج ۹۰ دقیقه‌ای از حملات، با استفاده از مهمات هدایت‌شونده دقیق، سامانه‌های دفاع ساحلی و محل‌های ذخیره‌سازی و پرتاب موشک‌های کروز در جزیره تنب بزرگ را مورد حمله قرار داد.
این حملات توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را بیش از پیش تضعیف کرد.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6132" target="_blank">📅 15:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6131">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">حمله امروز به چابهار</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6131" target="_blank">📅 14:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6130">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
ارتش: «آمریکا بامداد امروز با شلیک ۱۳ فروند موشک، آسایشگاه و محل اسکان یکی از پادگان‌های نیروی زمینی ارتش در بمپور را هدف قرار داد
دشمن به مهمانسرا و اماکن نگهبانی پادگان حمله کرد
‏ ۷ تن از کارکنان پایور و وظیفه تیپ ۳۸۸ ایرانشهر شهید و تعدادی مجروح شدند.»
‏</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6130" target="_blank">📅 14:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6129">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
سنتکام : از نیم ساعت پیش موج تازه‌ای از حملات را آغاز کرده‌ایم.
(از  ساعت ۱۳:۳۰ تهران)</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6129" target="_blank">📅 14:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6128">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9Iv9tJny44ivgS_gX_qjDCSLi19XS9wCTNDSvuFe6H2k2A_347P1efYGNCE8-4wbLd3IjaZ8ceOxhvqUQGus5t5WmlZiwFWeqRBFKi1AjRJOxu_SeZ7pegvA8JaOqUaECK6nBmQeu_0v8KBl_oRzg2xOxO3OHOVv17cTNpkGdYwc0LQVqn5TCZtuRKoGcsw3wTOAwgFHVUcvCleQyrsoh00ynq3YnTnod1wkcLVk3IdJdI537Tgp5wrIaSizOkLaJFFnvg6yLlq3SfG-JPhI0SYrF-n308KOSOLZj_Px0J-MjFqZrhmCi0hwpjUZvSPRyjrPhrKBnpHoVxaVwPtPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابل توجه ساختاری‌های محترم
مدیر حوزه‌های علمیه با بیان اینکه مسئولان باید تفاهم‌نامه‌ها را پایان‌یافته تلقی کنند، از دولت و شورای عالی امنیت ملی خواست به دلیل بدعهدی طرف مقابل، مسیر مذاکرات را متوقف کنند.
مشکلات اقتصادی یا ترس از آسیب به زیرساخت‌ها نباید موجب واهمه مسئولان و رویگردانی از مسیر «جهاد و استقامت» شود.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6128" target="_blank">📅 13:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6127">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=bZSRQN0_-i1IBfNceXCS3m1cslXegyECZ2VqCPfX5HY4t8EeTiKbDG5i_DHiThRcEUiPYYh5mUj9CtT4XiXAzEdkC4LOap6MvoCzpFU7lYMeURcoV43bVXdvvHTOWoswQlgx5n_lnYUpwgLMKet_qFdp8bc_pUuuuqfXLqCtAW6sU5lsIPlmtm0Veg0s21w0qQESmU3pYCIbiFCpCnIJREFT1k3J8SeIwEIhkk_M-qgsmuOt4Ol1NAjA5JM44gE2xcMNcy4LWNIz2LkCYzj9Gg3hGuW5GujQjQRTD8dWuoXJLDznwj8t0_Kan0IQc7b61u2Z70x0zV37-5pWrnsxOQetezIhK-WZaojfmaSGX1PXJRQrhn9f10lSzthamRfYE6c0BxLmcS36b-CJc6f7u7dApHvaWBMxs-NsYRW_PezkWyYFuoTgIaC_AvomAZJWs3FGsMzlDoNAVMKp1TQuiYkYodaVPRUxV6ONhENiIZoKdMtSZgKMKOGvvYL1ndV_0BM6A47fVS5YiPLwtxXwT6hiiNdY6uTB9X012Zt8-CoYXxBUzJFrDRf3geH4mrkTAOTuwjC1ZVER4UnJmjSzIoFu2TDhiohWLcUhqO-2Sl33nSOG0m-oeOJuWWU72nO7fWs87nGvP6DW2Sn7Rbag-FhNhN3kYj06W_p6Irv8igg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd0a98053a.mp4?token=bZSRQN0_-i1IBfNceXCS3m1cslXegyECZ2VqCPfX5HY4t8EeTiKbDG5i_DHiThRcEUiPYYh5mUj9CtT4XiXAzEdkC4LOap6MvoCzpFU7lYMeURcoV43bVXdvvHTOWoswQlgx5n_lnYUpwgLMKet_qFdp8bc_pUuuuqfXLqCtAW6sU5lsIPlmtm0Veg0s21w0qQESmU3pYCIbiFCpCnIJREFT1k3J8SeIwEIhkk_M-qgsmuOt4Ol1NAjA5JM44gE2xcMNcy4LWNIz2LkCYzj9Gg3hGuW5GujQjQRTD8dWuoXJLDznwj8t0_Kan0IQc7b61u2Z70x0zV37-5pWrnsxOQetezIhK-WZaojfmaSGX1PXJRQrhn9f10lSzthamRfYE6c0BxLmcS36b-CJc6f7u7dApHvaWBMxs-NsYRW_PezkWyYFuoTgIaC_AvomAZJWs3FGsMzlDoNAVMKp1TQuiYkYodaVPRUxV6ONhENiIZoKdMtSZgKMKOGvvYL1ndV_0BM6A47fVS5YiPLwtxXwT6hiiNdY6uTB9X012Zt8-CoYXxBUzJFrDRf3geH4mrkTAOTuwjC1ZVER4UnJmjSzIoFu2TDhiohWLcUhqO-2Sl33nSOG0m-oeOJuWWU72nO7fWs87nGvP6DW2Sn7Rbag-FhNhN3kYj06W_p6Irv8igg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سفیر اسبق جمهوری اسلامی در روسیه: مطمئن باشید اگر ترامپ را بکشیم نه تنها هیچ موشکی به سمت ما شلیک نخواهد شد، بلکه عقلای آمریکا با خوشحالی جنگ را تمام خواهند کرد.
کشتن ترامپ هیچ هزینه‌ای برای ما ندارد و با کشتن او جنگ هم تمام خواهد شد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6127" target="_blank">📅 11:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6126">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟  به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6126" target="_blank">📅 08:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6125">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/irtg0fM4-BlexxRqLd1sMb-zdL7m2wJeFfTajVEXJFT7XrpFyA4vMD_UcKHsNIFMAxVmlCqOsapNhdEvkMdpTAEEANDPhfGNR1el-YjE2nUlD8O28siry1CDCxNVf04245z10QYomuYu8a0nh6KIGRGedvl_2xaTGGFVU1pTXAADdrFBliuEd2L33NiWPyhjo1xfT3VduCT6sBJ_y-5wbgzPod0ZxJRBerjg-sfW8M7O9TEXVMci2iOt2gW0_IYlvdButklUj8Swy5779hnuwJko5TOC4yzbb90TmK0mhz_IpeZ39ae4ZHU7ECPxzEnnWTE8zUIi9ApseC6r9BlHRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلسه اتاق وضعیت برای بررسی حملات گسترده‌تر آمریکا علیه ایران؛ آیا ترامپ آماده تشدید جنگ است؟
به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا روز سه‌شنبه برای گفتگو درباره عملیات تهاجمی گسترده علیه ایران جلسه‌ای را با حضور مشاوران ارشد خود در اتاق وضعیت کاخ سفید برگزار کرد.
به گفته سه منبع آگاه، در ابن جلسه که ارشد‌ترین مقامات نظامی و امنیتی آمریکا در آن حضور داشتند در خصوص گسترش حملات صحبت شد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6125" target="_blank">📅 08:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6124">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=aEExiIsY1Ihv4h6-lLp_NksQyzRwuebf0RxZZeY7VF55zRnbG4ljpTAC6qZM91O5-sitamGjC1EdCo9JWgcQzsLuRgeoiE0TtAkQPWsR-htVP4qeIAwPeshtmWXRqjE7wNKt-7HLcTvsKhL0O6snqPFwuEjkWcVJQpDYwwj-LpTQJLAqQHihpDpO43_LiJUNxubcINxKiOhl7jMC4CVru1hxPAXamcXPEXDiBHfD2FbtazKyDXFJuVQWAdlFEDn-i2lH9elNlfGuSt65TPO7I-n582wNseqwtWLjJtktrI3fpkqBYVV-RIjy7mt2gPStM5oyHtJI_rXXLH4xG-EjcDDDp9XY-saULu9JQAiWb0x-EASOFrEtiniGgNM8uJp-jlJRUtXmZCqg3mnMpajckWyDHu2TRb9JkDmLGx9w77hkhC5fq2L1zWSW2w_Mbg66s38n1rJbWxKNJXrRF8oz-DzXygNGGWlsfjZ6As9KdVLUkIyqaHIGRD-zTl-yl5kHrA1Dn900zlDsgw17IibQy3_r9Nq2MC7gMPaJxfT-G5Tas0sEsEsbgG8aCV9UEp-dwCk5nc8RGukcmsAayOJrHjEdXIfNuS2hq4GsnbRy-Fi_DGFSv6KbdGuVTwH2ZvXkSfwvEXlFw7UC27pptw-SsRa1Olcvy97i6wxHC5gfGLY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bd4825a45.mp4?token=aEExiIsY1Ihv4h6-lLp_NksQyzRwuebf0RxZZeY7VF55zRnbG4ljpTAC6qZM91O5-sitamGjC1EdCo9JWgcQzsLuRgeoiE0TtAkQPWsR-htVP4qeIAwPeshtmWXRqjE7wNKt-7HLcTvsKhL0O6snqPFwuEjkWcVJQpDYwwj-LpTQJLAqQHihpDpO43_LiJUNxubcINxKiOhl7jMC4CVru1hxPAXamcXPEXDiBHfD2FbtazKyDXFJuVQWAdlFEDn-i2lH9elNlfGuSt65TPO7I-n582wNseqwtWLjJtktrI3fpkqBYVV-RIjy7mt2gPStM5oyHtJI_rXXLH4xG-EjcDDDp9XY-saULu9JQAiWb0x-EASOFrEtiniGgNM8uJp-jlJRUtXmZCqg3mnMpajckWyDHu2TRb9JkDmLGx9w77hkhC5fq2L1zWSW2w_Mbg66s38n1rJbWxKNJXrRF8oz-DzXygNGGWlsfjZ6As9KdVLUkIyqaHIGRD-zTl-yl5kHrA1Dn900zlDsgw17IibQy3_r9Nq2MC7gMPaJxfT-G5Tas0sEsEsbgG8aCV9UEp-dwCk5nc8RGukcmsAayOJrHjEdXIfNuS2hq4GsnbRy-Fi_DGFSv6KbdGuVTwH2ZvXkSfwvEXlFw7UC27pptw-SsRa1Olcvy97i6wxHC5gfGLY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مزدوران حکومتی شعار میدن
«جنوب ایران نکند جنوب لبنان شود»
عجب! شما دیگه چرا؟
خامنه‌ای میگفت «جنوب لبنان الگوی پیشرفته
و موفق مبارزه ایمانی است»! سالی یک میلیارد دلار از اموال ملت ایران رو میدین به گروه‌های تروریستی اونجا  و تبلیغ اینکه ما اونجا پیروزیم و …..!
ولی ظاهرا اسرائیل در جنوب لبنان چنان درسی بهتون داد که الان خودتون هم میگید نکنه بشیم شبیه اون «الگوی موفق»! معرفی شده توسط خامنه‌ای</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6124" target="_blank">📅 07:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6123">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=EykgZLzJyXWEZdoHR0VrlbUSt654FzIH5Ilj6C_-tAyeBm6IixGOC7f7gqCF9aygGq5pG8sDGZWXJxJUbTlZ2Mjfsr_63Mcc5FOS4hnX2sjsVR1xUP2r0Y2pYcf2tODqjWnutJIgQ67Mc7GD2OfDHSJZjEtgtVVqQk9Q-kbUlTWpgC5d8JyvFoEZGeHligAq7rlz8n2RiF_tp8iJ1imhOBG2fYxKFqA0bkRDRvu_idqz_8tqSKeuSB6KtvD-2630Li5cIJvS4_PKVpBBjdo9kbofh_Hp5GAcLxgpoLkJu2tzSaKob4APvrpbG4V9DYSwgSGjtPi3x4cXY9k2SoOtjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0378588a4a.mp4?token=EykgZLzJyXWEZdoHR0VrlbUSt654FzIH5Ilj6C_-tAyeBm6IixGOC7f7gqCF9aygGq5pG8sDGZWXJxJUbTlZ2Mjfsr_63Mcc5FOS4hnX2sjsVR1xUP2r0Y2pYcf2tODqjWnutJIgQ67Mc7GD2OfDHSJZjEtgtVVqQk9Q-kbUlTWpgC5d8JyvFoEZGeHligAq7rlz8n2RiF_tp8iJ1imhOBG2fYxKFqA0bkRDRvu_idqz_8tqSKeuSB6KtvD-2630Li5cIJvS4_PKVpBBjdo9kbofh_Hp5GAcLxgpoLkJu2tzSaKob4APvrpbG4V9DYSwgSGjtPi3x4cXY9k2SoOtjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6123" target="_blank">📅 07:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6122">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=MYSo8VvGU7w57GPF_Rv1BKklxxrnKvYjZ5YjoP4GZQ_UuftOST-n9nJKBBNJiq-uMS83om15_h9oeMXST7brcrY92ctNp0qboZfitkuOE5WFuzYzsXiafv2E8TRVd6Ex0LYOP2jqkWV27oNCmnb-Ym59ruIBHKQ1JCejXx9FTU12140jYvLLUFBH4_eK2mjbZSzmj222sUapP-6G70_WBCSAYYgLyLEuBiSW5dNUUxrM0uXtOIgSKnyBdn73u3MtS0A6pt5n0MMsqzUg9sbw4BWiOePFduSkXAvGtK1Hdbnv_sk6DrICo1zSZ2iXp_Sz9XSOr7WgblsqTJi33-7_YjcV2hBs9RE12GsfrcqrNpcy7jDGLg1lZGvn6hq1WYo3w8P69OkK9A27KzkxPfNdSCyMg-GHlc8lSGBMEVwi0AVik8d74gFxzhxR0WQ46c7quuOiYDCBGrmKtRHWP-CHWqMG2XBS_5aR0ZxtpWRb8O3CO_SA7Xc2dAGr0egLQ5FV6j0Dc3oy7Kqb7no03kkEUNPp-QDlisuNOGCANDhsdsFLSPB8sXv6aJsUY-LtD7tSsOo78UdqircGdEdbpl64nutRPbvuqYwawpsQZXnhjr9aBeBkwTNK00ZNcvhuaU_ZL3ullYFe5JaRXnRf0wb0fpjyaYNkfgMe6DiahigGE5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5b6a441ee.mp4?token=MYSo8VvGU7w57GPF_Rv1BKklxxrnKvYjZ5YjoP4GZQ_UuftOST-n9nJKBBNJiq-uMS83om15_h9oeMXST7brcrY92ctNp0qboZfitkuOE5WFuzYzsXiafv2E8TRVd6Ex0LYOP2jqkWV27oNCmnb-Ym59ruIBHKQ1JCejXx9FTU12140jYvLLUFBH4_eK2mjbZSzmj222sUapP-6G70_WBCSAYYgLyLEuBiSW5dNUUxrM0uXtOIgSKnyBdn73u3MtS0A6pt5n0MMsqzUg9sbw4BWiOePFduSkXAvGtK1Hdbnv_sk6DrICo1zSZ2iXp_Sz9XSOr7WgblsqTJi33-7_YjcV2hBs9RE12GsfrcqrNpcy7jDGLg1lZGvn6hq1WYo3w8P69OkK9A27KzkxPfNdSCyMg-GHlc8lSGBMEVwi0AVik8d74gFxzhxR0WQ46c7quuOiYDCBGrmKtRHWP-CHWqMG2XBS_5aR0ZxtpWRb8O3CO_SA7Xc2dAGr0egLQ5FV6j0Dc3oy7Kqb7no03kkEUNPp-QDlisuNOGCANDhsdsFLSPB8sXv6aJsUY-LtD7tSsOo78UdqircGdEdbpl64nutRPbvuqYwawpsQZXnhjr9aBeBkwTNK00ZNcvhuaU_ZL3ullYFe5JaRXnRf0wb0fpjyaYNkfgMe6DiahigGE5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا میبینم راست میگه …</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6122" target="_blank">📅 07:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6121">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKuOAqsHD7TgowGsFpr3nvkEvM3ymPiB_45EAbnlvsRqGyzG3gu2PasgN3CddWO9tVUfKJifT0iyIdHvBz-2brQiwxMpdGdeSQDMKr2O8WxJaJxLV9SkMiSBhKdPmXqXhlVuSrAlOvhkXtJQjTefOUObnsQEGkhh9Or2VSVQHHD776eZLVR3CAh06MK2DFOCsuq9eFGDfH7hW6o23FqReaTpb13HNZIkTxbRbbfHeGSYgf9Oj8IDHR1XgiFdLBw683niIgTNpqASY9wquYPcscCSMAfhWWwbAsIHQ5Ttg4YHDpeWoEn0_OYXbFCSeNXlIZwgy8MevP6H6Z-fPX8_bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6121" target="_blank">📅 06:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6120">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqbOdrHw9C2NtxilZNjWisC31l8r6Pnkk7BN2rJVv4hOIDbyYSzYtKUo-C7sQPexY4_gvyRhiTdN4Zd6df-9HIpfzVPIhe_pThZlaXWlgsn-O5u9DzxBLZRN0931wH89Kvn-vUEfMf9OVZrOBn6qrjOLNmnRX-LUy-WU7RbJwzr2orrDgLn7tepeSGb1y6atz7xJagshYL-d9Z9MPi3GOiEz2F5knvmhOugHtAnSYt1Pt_XAE_b41DHwm488eGBonR_YhAtoKzUVXXphXc8e1iJYkzvDRUi0Uqj2TK3nJm6KMHh5XMWz_9ub4jGLa-iLX1Ds7R-z_H-pEzc2NuF5cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه محلی «حال وش» از حمله به آسایشگاه سربازان در شهر «بمپور » در استان سیستان و بلوچستان خبر می‌دهد و کشته شدن ۱۰ سرباز و زخمی شدن ۱۵ سرباز</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6120" target="_blank">📅 06:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6119">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=kK0TPPJJlRzXUMG4mdQlG84R8D8US0MnxkbdABoooMFAcDGpYeWAk3IwtNaIuxDdbjbJyO9zXdQVjXuGHiSl0fnBtQ4-FqXyezlo5gWzUaF8aHkm9YUhYPagVHshGVe3OrPLRjsHHiS8uVP17rYHfD_fntFQR50UG5ilc0K83TgE5Oj0VlDy1e_XObBDPwysqoAFl1M6_-J5Kr88fDk-nZOyYfhwrnREy0YGenFTvJgHRPgjQ4O2GqpMd_XBoBpxBhQt7BqfLIV0_KuLRmqY_P2V5R3ykSIMFmnY5-04P_lxcleVvFzfyrMMRHq8eTuvOjVmLuB1euQajOQBz3Zbnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba02e5e863.mp4?token=kK0TPPJJlRzXUMG4mdQlG84R8D8US0MnxkbdABoooMFAcDGpYeWAk3IwtNaIuxDdbjbJyO9zXdQVjXuGHiSl0fnBtQ4-FqXyezlo5gWzUaF8aHkm9YUhYPagVHshGVe3OrPLRjsHHiS8uVP17rYHfD_fntFQR50UG5ilc0K83TgE5Oj0VlDy1e_XObBDPwysqoAFl1M6_-J5Kr88fDk-nZOyYfhwrnREy0YGenFTvJgHRPgjQ4O2GqpMd_XBoBpxBhQt7BqfLIV0_KuLRmqY_P2V5R3ykSIMFmnY5-04P_lxcleVvFzfyrMMRHq8eTuvOjVmLuB1euQajOQBz3Zbnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام فیلمی از حملات خود به ایران منتشر کرد.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6119" target="_blank">📅 06:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6118">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=fI3y84eyqsPSV4Ax35-6-Y6lGlwmebz6kxpAsnr7KAOOuKQYHJ3r8eES0aiV7fHH2_uSsTYsMM8eCKMmgP9JmYzVUDRd1wuizJN0aWyx9u6WFVyeBhkWjmxIpufMLml0fmCdoSRtLUmyRm8aOj1XvO-zmeBeuzBa6mdQT6oIjyblKvFpw6-aaEERtZ-2q9tZwtLiBrhYkwsEyaO5hls1_17JsMFThxsEJy2O3q-9lH30FmZpgH0rnS7OtTp9SzySwRwsQ9HoJwrQltzFidIVo6-vWp_WHIKz4EWsjeh__f9ZU7vO82MMA5357Hx-KXlzZsAr6NdvCno4-1wmm_uxIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b9746249d.mp4?token=fI3y84eyqsPSV4Ax35-6-Y6lGlwmebz6kxpAsnr7KAOOuKQYHJ3r8eES0aiV7fHH2_uSsTYsMM8eCKMmgP9JmYzVUDRd1wuizJN0aWyx9u6WFVyeBhkWjmxIpufMLml0fmCdoSRtLUmyRm8aOj1XvO-zmeBeuzBa6mdQT6oIjyblKvFpw6-aaEERtZ-2q9tZwtLiBrhYkwsEyaO5hls1_17JsMFThxsEJy2O3q-9lH30FmZpgH0rnS7OtTp9SzySwRwsQ9HoJwrQltzFidIVo6-vWp_WHIKz4EWsjeh__f9ZU7vO82MMA5357Hx-KXlzZsAr6NdvCno4-1wmm_uxIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : امشب، فردا و فرداشب به سختی به آنها ضربه خواهیم زد و هفته آینده پل‌ها و نیروگاه‌ها را هدف قرار خواهیم داد، مگر آنکه  مذاکره کنند.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6118" target="_blank">📅 06:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6117">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caeb092620.mp4?token=fu35AScmuGREc1LlHMH6QIi7mTL5tRggtgK_l_gA_oNfNyYhAv-oyOg-L2us73waNxIqiaioBFzs-waHatjrFkp2LXLm61kVdwOhMCEU7Zg7jZYRgfoWw3AMwi0fc0IZVEJxfMzUW5xOyunLYbkNjyoOGV1Akf6I4aj8lhdSp6XQleTB6Mo0FTnbMpe9ZKxjjpMBHCevcSGsAAGSkMdZ3i6S_DVxNYf7_wsxJB6nWWcbCthqan5fHLFP4cU454rBCMJXHOhgqnQhJrBYQS3j3dnIuT61u9p7DM_E_kvtHe4kU8CJsCDFmvrLvu3vcE2g0wYCstA8zGSKUJhJZF6atw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caeb092620.mp4?token=fu35AScmuGREc1LlHMH6QIi7mTL5tRggtgK_l_gA_oNfNyYhAv-oyOg-L2us73waNxIqiaioBFzs-waHatjrFkp2LXLm61kVdwOhMCEU7Zg7jZYRgfoWw3AMwi0fc0IZVEJxfMzUW5xOyunLYbkNjyoOGV1Akf6I4aj8lhdSp6XQleTB6Mo0FTnbMpe9ZKxjjpMBHCevcSGsAAGSkMdZ3i6S_DVxNYf7_wsxJB6nWWcbCthqan5fHLFP4cU454rBCMJXHOhgqnQhJrBYQS3j3dnIuT61u9p7DM_E_kvtHe4kU8CJsCDFmvrLvu3vcE2g0wYCstA8zGSKUJhJZF6atw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار ناشی از حمله پهپادی امشب سپاه به کویت
گفته می‌شود مخازن سوخت ارتش آمریکاست.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6117" target="_blank">📅 06:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6116">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/360d24e506.mp4?token=YrEnZ-sQWLkroZ9190rSlHb6G2JVUhP7sjYpDIV1qAdE14PgI2Db-wQ9S5JpJDUYEIEXFVUSYN5biebTn2GnQt_2C-JGgvnzyxyfN31mryKI9SVMRea0wCgVyhiKDjSL-H5mIUqXs3kJcmk0y3TxhpZyi7JLALnX0WSx64rMi8Y773XRoTwnemFO_l-nAV_2B3Q3B2_bbsh32mXo8rAogKSnzMfrqm_OzS1g8gytCjgVeg3NiIAIOYCVAEGeBNHN9IrI51xuhZBmZUIlemYPArPhf7PqH--vBbWkejG605su2zlHoV-3CUSxHV-SRx4wjgltFp1VvgsQ9VCldJHeeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/360d24e506.mp4?token=YrEnZ-sQWLkroZ9190rSlHb6G2JVUhP7sjYpDIV1qAdE14PgI2Db-wQ9S5JpJDUYEIEXFVUSYN5biebTn2GnQt_2C-JGgvnzyxyfN31mryKI9SVMRea0wCgVyhiKDjSL-H5mIUqXs3kJcmk0y3TxhpZyi7JLALnX0WSx64rMi8Y773XRoTwnemFO_l-nAV_2B3Q3B2_bbsh32mXo8rAogKSnzMfrqm_OzS1g8gytCjgVeg3NiIAIOYCVAEGeBNHN9IrI51xuhZBmZUIlemYPArPhf7PqH--vBbWkejG605su2zlHoV-3CUSxHV-SRx4wjgltFp1VvgsQ9VCldJHeeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی با موشک‌های حاوی بمب‌های خوشه‌ای به بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6116" target="_blank">📅 01:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6115">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
ارتش : به پایگاه‌ها اف ۱۸ های آمریکا در اردن حمله پهپادی انجام دادیم.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6115" target="_blank">📅 01:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6114">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‏امشب اتفاق جالبی افتاده، به محض اینکه خبر انفجاری در شهر و استانی منتشر میشه، مسئولان جمهوری اسلامی سریعا مصاحبه میکنن و میگن دروغه و همه چی آرومه!
‏اینطوری مثلا میخوان صورت مسئله رو پاک کنن.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6114" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6113">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qIFC1vge61qTunxQBAfb_F96gPm3Bj9p8e11IJKBEmR7bH74FqL5CyRGxeEvXSuYmAz10kw_4CgvKNuskxMjkOw8fBIix0A0clFkeRStugLJWnzSSm7qcljlIp2nhUR3eBu1890ocKkSwXARNudyOMoWLL565FktodVkdmZ5FM4NgsmQ2drg9TNq_Mipp4YbbrRd24mUdq7aYPceR75JmpSeoQlnHMy6JVhdmNNRyoNjsshHc1WOWmqDidZRMv5ykCjUI3d2PCtErXz5NneqPQfVPGthHYu41-a0gk4xSO7VNfjW-RU25atMRnpiVXM_5diYWs0hy2oDQWLGzz54gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگارهاشون می‌نوشتن که کشتی‌ها دارند  از مسیر عمان رد می‌شوند، تشییع جنازه،  بریم و کاری کنیم که  کشتی‌ها مجبور بشن از آبهای ایران رد بشن  و شروع کردن به حملات به کشتی‌هایی که از مسیر آب‌های عمان میرن.  به زور حمله میگن کشتی‌ها باید از مسیر ما رد بشه.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6113" target="_blank">📅 01:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6112">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5gbzsqtwC7jvznw-W2Rmbyb4ob2IOZ-cXqA1amkWVJWsy3Y61kxVnuLx4uYIxqNG48MWpf44A091aL-UwcBWXbjCbo2FgdsOiMT2VNNeF49u1gWOJ-ocuzHXaV8Xjd7Wt0zVrQHgJnHCMLLAF9_xN8o4mBqNQy_UW_fRmyGGuGIFzRUhRItMGr1_PIAv7cJZvr7b4eHHfDb-WgcwCRNe71CkIRzcp6nQAf4SqaOq8zY7z6PFSmjGJmT1tPThwn8UBYgOyE7iWxua6qR0rYHHsyamywaZ8fYrD2Finn1GW514sP3R3F1TiPBY_4rh1ZNBc3Q5Dct_N6LSbHgSwBn1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا در حاشیه خاکسپاری جسد خامنه‌ای و جلوی قالیباف شعار میدادن «مذاکره با دشمن خیانت است»  هنوز به سه کشتی حمله نکرده بودن و نزده بودن زیر تفاهم نامه</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6112" target="_blank">📅 00:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6111">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=CnyTRluCDKo2NIdDrKSxrRx6aZajUh9C7m7mmsOk0sLc9Vu3HoFVRDBiUhgMEUY1OgQGv23Snn0cdgiE_-Twg71ZQfuodACstw92Gf04IZxzCaEqd9vK4FsJrTiNrUkSQJU9jDl_yJJy9KRT97YujK2inm92wQNbTCMgsK1o2RI6WdmUG4IOWxrV9zatJYO8i1Rp_crM1NdNCaGk-RsLWA5OUJOwhOOQ7wvVfz0IczpnMksO_1YoH0_u9wv5_0-W7djuJmPUvXmVL32QdNxpxQpnwE0x0ukoscrJ4PdT7rSk6b4G_hl9mJF0dUy-aN4XwDG9ojxD7XXPFAs0yDsKZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d90d3d98f9.mp4?token=CnyTRluCDKo2NIdDrKSxrRx6aZajUh9C7m7mmsOk0sLc9Vu3HoFVRDBiUhgMEUY1OgQGv23Snn0cdgiE_-Twg71ZQfuodACstw92Gf04IZxzCaEqd9vK4FsJrTiNrUkSQJU9jDl_yJJy9KRT97YujK2inm92wQNbTCMgsK1o2RI6WdmUG4IOWxrV9zatJYO8i1Rp_crM1NdNCaGk-RsLWA5OUJOwhOOQ7wvVfz0IczpnMksO_1YoH0_u9wv5_0-W7djuJmPUvXmVL32QdNxpxQpnwE0x0ukoscrJ4PdT7rSk6b4G_hl9mJF0dUy-aN4XwDG9ojxD7XXPFAs0yDsKZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این استوری رو ۶ روز پیش گذاشته بودم  میگفتن آمریکا میخواد آتش بس حفظ بشه ولی جمهوری اسلامی باید «کار دیگر» بکنه!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6111" target="_blank">📅 00:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6110">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550f13e765.mp4?token=FVZR_ZsODoUGMA5A_Ep7d-AO6OdA1cR5GD4csXSzcr1bh_MykjEojkDoJcPT6DdDrmUTPbB5FudwTKqyel0_nScCHasPP89OVVu3kOk8kHNrcCspb-yrussF3kn0St0tIhMkXfLoGQo-w9hzyeFOZf-n8fx38-lFohdPVxkstaCjiMhvW_UZ5zdpgTieAk5qDVk6DI7O2x14rih6aTG3Dvm4yYUZZUNZUPWcXZHa5Kl7ph8iQUPMtAhLNpUNTgcKFmn8YrHaIq7bAynnlPO0bJG3unVHDfLro_vPXv7-_EyOlL07IVCNqVt_4e6nEhCTiDgJP1EfmwW19zqGdB75qIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550f13e765.mp4?token=FVZR_ZsODoUGMA5A_Ep7d-AO6OdA1cR5GD4csXSzcr1bh_MykjEojkDoJcPT6DdDrmUTPbB5FudwTKqyel0_nScCHasPP89OVVu3kOk8kHNrcCspb-yrussF3kn0St0tIhMkXfLoGQo-w9hzyeFOZf-n8fx38-lFohdPVxkstaCjiMhvW_UZ5zdpgTieAk5qDVk6DI7O2x14rih6aTG3Dvm4yYUZZUNZUPWcXZHa5Kl7ph8iQUPMtAhLNpUNTgcKFmn8YrHaIq7bAynnlPO0bJG3unVHDfLro_vPXv7-_EyOlL07IVCNqVt_4e6nEhCTiDgJP1EfmwW19zqGdB75qIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو رو دو هفته پیش گذاشته بودم.  معاون سیاسی نیروی دریایی سپاه اینجا در جمع حامیان حکومت بهشون میگه خیالتون راحت باشه، حملاتی که ‌ آمریکا انجام  میده «واکنش»  به اقدامات ماست!  «کنش» نیست!   تمام این ۴۷ سال همین بوده!  یه کاری میکنن ، تنش راه بیفته،…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6110" target="_blank">📅 00:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6109">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6109" target="_blank">📅 00:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6108">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=aDKL7YK8rGCDPyZC776KdLuRGn6Tcs1MJPN6IrtAYbXZgsc_y0qdAk91I136Td2R6cswvvW64fKPOWvw1RVwNYll474CtcN3rViiUjaEt3VLVfjES3D5hwN3ZNjkdGojp2BxaNTHvtePnFsJ7BJt1WqhvP1g4kCUNs-h_P1KOEjEIEqU5NOco0krYsFFCH9oBrc950i7C_PZLQZCg48PTpxlCMvojcuVoJDWkydp1ybEEZHo7XBuK1O85c0-Xu8HqrVES6AtWTPYNQwGrlvFpDYkty4CstM8qqE1W4OENbOVDsWi7bRkaFxfE6xXzDpAwibn53qLI-KkD_virWy1VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0b9d2dcec.mp4?token=aDKL7YK8rGCDPyZC776KdLuRGn6Tcs1MJPN6IrtAYbXZgsc_y0qdAk91I136Td2R6cswvvW64fKPOWvw1RVwNYll474CtcN3rViiUjaEt3VLVfjES3D5hwN3ZNjkdGojp2BxaNTHvtePnFsJ7BJt1WqhvP1g4kCUNs-h_P1KOEjEIEqU5NOco0krYsFFCH9oBrc950i7C_PZLQZCg48PTpxlCMvojcuVoJDWkydp1ybEEZHo7XBuK1O85c0-Xu8HqrVES6AtWTPYNQwGrlvFpDYkty4CstM8qqE1W4OENbOVDsWi7bRkaFxfE6xXzDpAwibn53qLI-KkD_virWy1VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گشت زنی اف ۱۸ آمریکایی بر فراز چابهار</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6108" target="_blank">📅 00:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6107">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا : محاصره دریایی ایران وارد فاز اجرایی شد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6107" target="_blank">📅 23:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6106">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
چندین انفجار در بندرعباس
🔺
چندین انفجار در اهواز
🔺
پنج انفجار در قشم</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6106" target="_blank">📅 22:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6105">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0DZvVdn7YXUd0gcNJHIequ4n1Q6mrnde3SW_OhN4eewbDpfzl--N2NH27sl0kP_YoE9hjU1B1B4tnDbkTqLkbNNLHinap392-kLu5P3brlujChPJJ7mTM70ZvrXzLB287UlZlkgwomH27T5ubvXYFLzwk6zcLVvFU3jxyRAaEnhxAwdCQ7vqJs4Dt6xH9k_qmB_kPZIbNLQ5RDoRWwSg50OqQgFGlSdnEQe6hN-INc9qKgJk_IsFZEuI2r9o3x6_xjvIBtwjbu5XeXizFxOv-DI1a9yLlT0uXDGC1dz06gkxhDfNsxTuuqNZwV80iIB73viJpfsFw32-pz-_eN77Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2077085449948938568?s=46</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6105" target="_blank">📅 21:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6104">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
دقایقی پیش : حمله به قشم و شنیده شدن چندین انفجار
🔺
حمله به یک نفتکش اماراتی در سواحل عمان
🔺
فعال شدن پدافند در کویت</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6104" target="_blank">📅 20:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6103">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3J65Id6iGzpSN6Q8haJ78Vp-lFsaOd15N-F1RsOyN6SDD8V4fanQ2H8QrfHUoxw9xQiM4-fofmpLRDFRQhwniDbOfBEIGdpveUnCcEyja_ibs56p2nDiZt5yvBZCQRGM2fMKqOVOyEMnYRQC8U_ychQbdblbj83ncZpAIue5qADUrQCdciZbvKXUvAv07_NGJ0EG0UQRo6rPTV2SBn1c0a7hVuwmm72KSaScvQvyevwHm26wPqjk1ffFQOqPpzs5xwBwPBTMe_B2dau5ETnnUAjQnwAddxKDJQaZSgpP1SkL16L-0qbVQJnFnHdu2lifRsKZFpg7Yr3r-gv60p3RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهپاد‌ها (قایق‌های تندرو بدون سرنشین) آمریکایی این مدلی به یکی از مهم‌ترین مراکز نیروی دریایی در بندرعباس نفوذ کردن و حمله کردن.  گفته می‌شود که در این حمله یک زیردریایی ج‌ا را نیز منهدم کردند.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6102" target="_blank">📅 18:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6101">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=NH88shuUUlgjvXrAoF4JnfHo0HRdnzukTX8leqtbwSR98m2_3HlDOduoEqKizoG3zSE-GHmHgwd1yMI4gy0X-9Qjd9IWe4gCXA2roFF1VZ9nqYyOobsSTvwKpbhjTzjVY0WBvBBG-fCD0nSRsfJWH_c0GPImo6mah3dmIvrCCmpZ7NbgcWw2MYz9bM-Y0mgnnW1dmexwzQMvRRZOeNz-Xt32_NGUZkmmIRmRc_KAtpBOQMrz-TKntaAqn96tLOQM8DXREhgJxUqgaOvNvL0el4boK6kxL1lFdHs8tdg9r8BPn45zqoSNNFzyBlkm3tp9eG0KtfIMSr4LuzmpAq0WvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee96f6523b.mp4?token=NH88shuUUlgjvXrAoF4JnfHo0HRdnzukTX8leqtbwSR98m2_3HlDOduoEqKizoG3zSE-GHmHgwd1yMI4gy0X-9Qjd9IWe4gCXA2roFF1VZ9nqYyOobsSTvwKpbhjTzjVY0WBvBBG-fCD0nSRsfJWH_c0GPImo6mah3dmIvrCCmpZ7NbgcWw2MYz9bM-Y0mgnnW1dmexwzQMvRRZOeNz-Xt32_NGUZkmmIRmRc_KAtpBOQMrz-TKntaAqn96tLOQM8DXREhgJxUqgaOvNvL0el4boK6kxL1lFdHs8tdg9r8BPn45zqoSNNFzyBlkm3tp9eG0KtfIMSr4LuzmpAq0WvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت جنگشون :)</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6101" target="_blank">📅 16:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6100">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/de0MdUd-wvefLP0UEMGxZFkHc594wRq5rZDLm3enMY6_Vtzabb5pSmzcMwDLmWIeQdEu2WSzoJmYVFX8cTxQDVDfHsZMdtkHn595LpsUJbbiAH3t7H9Zo9rpGLQDkYWWKyyf-zMwYg1yW0xMH6RRWw8P4PCBa_tL_1MIwI3EaapHhSWgnHDsEGFGBemcVduI4NG4Gh3kPo4Fe9uCWuWroTIKVqyZyvesYh6_o2kHSktx89rnl4uCAWtuO0hy-Jw4DZ-TwtuehM-vf41_R9rLviErqycsQPMvIiCKr0XyK1zEcXuvH16vjRLso6WuMX90ZRL24lzGdx9ZnNaS9um0jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏آمریکا با استفاده از سه قایق بدون سرنشین (شِهپاد)، پایگاه دریایی دیروز بندرعباس را هدف قرار داد و تأسیسات نگهداری زیردریایی و کشتی را منهدم کرد.  این نخستین بار است که نیروهای آمریکایی در نبرد از قایق‌های تهاجمی بدون سرنشین استفاده میکنند.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6100" target="_blank">📅 16:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6099">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">۴۷ سال رژیم اسلامی</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6099" target="_blank">📅 15:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6098">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGpujkeUvArIwvm5yijk4A7NPpR2B7E7GKDuH874yEipSHouKaOebYsA3qDiUhwc-G-cQTEi6oW89dSEzc93P-rVpEMg_GZlZGsquf7WvJjE4rmT555wTnF1YA9jC1TAy6sj8gGAoupj0KKxA9D9zoRGmEOw3J296oCKchT8k1yhKWreyD6EEaO7dss_Wl0us2dZhQcJcZ1oyMtZTYK6IFg_j7JerT9RE04NuwXA-pLzwQER7iL8UhhsYPvFIZAKu38VNtBTivKeIx0CFm4DFhhL978lLxaQwQiCTbTJyKf-oRwpZLDqmnD1wrVYGhbWYcZlU1YtokPJ80yszkqb3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
تخریب ساختمان مرکز آماد و پشتیبانی دریابانی نیروی انتظامی ⁧ بوشهر ⁩ در پی حملات هوایی ⁧ آمریکا ⁩ به مراکز نظامی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6098" target="_blank">📅 15:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6097">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9c510f4f.mp4?token=tpBpMgpHay9ta9s9J-J9oJXF8aWjBCPRxwoaqAEEoPP5f7-u-fAEa8Eo5B8z7ofbHXX6liGDQ3zc_0GaJ6NRP9tnbWy3IiHrI_agq4R6McG8nnhfvFsrc2CSX0S2ARwx4NngVHopoRV8e2VEdMaGZfQblUfNR3NDEm7P9J9GiKrIFuPnXyjVgNDEYDz3hEIU4Ph46ME4td4_JqG-8m5tkJdQZwhYqBHma8yXGJGLPADkvnluVQ9x5rogiL1buNjw9oAZvhHOperrvxyLeASzze0-DkskBnkvl8K3wMBW_BEbLg2LK9-4pgPPcFTyRCg1IkDUwemqT4cAMzJwZqpKEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9c510f4f.mp4?token=tpBpMgpHay9ta9s9J-J9oJXF8aWjBCPRxwoaqAEEoPP5f7-u-fAEa8Eo5B8z7ofbHXX6liGDQ3zc_0GaJ6NRP9tnbWy3IiHrI_agq4R6McG8nnhfvFsrc2CSX0S2ARwx4NngVHopoRV8e2VEdMaGZfQblUfNR3NDEm7P9J9GiKrIFuPnXyjVgNDEYDz3hEIU4Ph46ME4td4_JqG-8m5tkJdQZwhYqBHma8yXGJGLPADkvnluVQ9x5rogiL1buNjw9oAZvhHOperrvxyLeASzze0-DkskBnkvl8K3wMBW_BEbLg2LK9-4pgPPcFTyRCg1IkDUwemqT4cAMzJwZqpKEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">می‌پرسه نظرتون درباره اینکه بدون هشدار قبلی برق رو قطع میکنن چیه؟
‏چمران میگه:
‏شما اگر بدونید پریروز چند نقطه برقی رو زدند دیگه این سؤالو نمی‌کردید.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6096" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6095">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pyizwmy9SyAq7cvEqVFpn6HSxs3eS0SJAZTe9X0RsW56w-eYiUuSM7NP6sA2UmvqsEEv8FwgnDmSpSTsFgPjtNG5r3LxMK7EuviBhGRszbYrM6WgithWloHpcPw3Y6SG76sm5XDlU4Zlfe3rcILu2R0VqFTucx3I0ZC7qhkZlKtJFimfkfzWU8qOih_9upvm0DWImma2v6y9MK2y3dYQFLo7lFDDzEGBkivOHie7oEKMa2rnFHionlf_g5pDSA4TG1o2rPQXXGs363XhACGerk-oH1SNSb7-0uUHXC_wn5B4grTgrUSAw9pjRmiWyox0_ZZHmyjbtiFjeerUXHE4dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه ترکیه، دیروز جمهوری اسلامی
رو با اسرائیل مقایسه کرد و گفت
رفتار این دو شبیه هم هستند.
(کاری ندارم که ترکیه خودش چه افتضاحیه، اما نشون از تغییر رویکرد ترکیه نسبت به ج‌ا داره)
یادمون باشه فرمان حمله اخیر از سوی ترامپ در ترکیه صادر شد! یادمون باشه معاملاتی بین ترکیه و آمریکا رخ داد، که آرزوی ۲۰ ساله دولت ترکیه بود.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6095" target="_blank">📅 14:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6094">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
حملات دقایقی پیش به بوشهر ، خورموج و….
🔺
سنتکام چند ساعت پیش گفته بود که این دور از حملاتش متوقف شده.  در اسامی شهرهایی که مورد هدف قرار گرفته بود هم مثلا نامی از کیش نبود!  مشخص نیست آیا همه این حملات را آمریکا انجام می‌دهد، یا کشورهای دیگر (مثلا عربی)…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6094" target="_blank">📅 13:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6093">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHw35T_ng5gvltZE9RHBh7TQPluPNnh3fdaFeX_SszLm1XKnLeK1KWYFwDfLScadu9gCazIFw3TbMjElT22GP0P4vtIVfOXoC5bQZ83cakQy27uPHRX4gCwwwVkeD_a45A5O_wt6ZfhAbG3EYMcXn1M3TzIJ9kcDJ2QS067FCC_NbfVHctTkgQ4axcjXBzCAFwQQvgiZzVGPzYHiORNfDl4H_BRYgisOp3Jhg74ZFTI12GlfyJygRBtuKT7xSP929K50tGnTjL09nymk1CwiyeEpa2oa56AvsCjhTw5658BBuE7HYK6ePwvKs3myyHR6jGBClmmWnYEprq2b_jwwLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6093" target="_blank">📅 13:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6092">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=r7Av8IfTdu4vylJnObwgawnH0boLG8xEZobWQ6A4U5iuxQWvaI1iO8q1MmwzQsBvTTepJjQZww5aNO1f7szUBMrn2TGaRM8CDnXwjXeugHBkov5qptgUqFZfW1mY06DtRVc-u9GXVHGZBqhG2NRkeJgOyIygJei9q4rzwbYLEuzkQ74wilSfkd8mCCJpx3P69vZati5NExcaHN5xI2QLP_ZmAvsuEUayJHRL318nWXkFwK0zVhxoDjoETdpFjvaVCwd9s-s0_QS21qYjRozeNrX1l0ORKMeKY3R5iosPK78kCx2-BRLco9MbHvoTNTBvorxyAyWQzBSjqN21dySD2o5Y7sUOPvbjpKNpx6K8MMsQlCODyQyHPfjlf2EKuWtDzbxpVitZL9em4R66sWa3VIIsCdB7v9koE31e03LHP_9Uja5QBjJMLmajxN4BqrrnfAaO1c-PqszbPpx1kYNW8-MQ3HkfWYftEs5PSgsiePrq8rtJsQYNfMg7Nn_OeHfaVLuGDSCueV3Vv5erxT1eBr-P_LdJKP6TkzTktsKLolwMnFTspwebPJUn_tBb-wrIZPZMbLCwWINykl37v-7hakscL4t_yQLMbmgJ4HbBGc-RW86PmBMVuvMlP1E4QZQGm6a4x_FE7qTmPgUSdMenZebgMe5QeNBYFJSF7cNcCeU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b04e0dceb0.mp4?token=r7Av8IfTdu4vylJnObwgawnH0boLG8xEZobWQ6A4U5iuxQWvaI1iO8q1MmwzQsBvTTepJjQZww5aNO1f7szUBMrn2TGaRM8CDnXwjXeugHBkov5qptgUqFZfW1mY06DtRVc-u9GXVHGZBqhG2NRkeJgOyIygJei9q4rzwbYLEuzkQ74wilSfkd8mCCJpx3P69vZati5NExcaHN5xI2QLP_ZmAvsuEUayJHRL318nWXkFwK0zVhxoDjoETdpFjvaVCwd9s-s0_QS21qYjRozeNrX1l0ORKMeKY3R5iosPK78kCx2-BRLco9MbHvoTNTBvorxyAyWQzBSjqN21dySD2o5Y7sUOPvbjpKNpx6K8MMsQlCODyQyHPfjlf2EKuWtDzbxpVitZL9em4R66sWa3VIIsCdB7v9koE31e03LHP_9Uja5QBjJMLmajxN4BqrrnfAaO1c-PqszbPpx1kYNW8-MQ3HkfWYftEs5PSgsiePrq8rtJsQYNfMg7Nn_OeHfaVLuGDSCueV3Vv5erxT1eBr-P_LdJKP6TkzTktsKLolwMnFTspwebPJUn_tBb-wrIZPZMbLCwWINykl37v-7hakscL4t_yQLMbmgJ4HbBGc-RW86PmBMVuvMlP1E4QZQGm6a4x_FE7qTmPgUSdMenZebgMe5QeNBYFJSF7cNcCeU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">سنتکام ساعتی پیش
از پایان این مرحله از حملات خود خبر داد و نوشت :
🔺
جدیدترین موج حملات خود علیه ایران را به پایان رساندیم
🔺
در این عملیات پنج ساعته، به اهداف نظامی در بوشهر، چابهار، جاسک، کنارک، ابوموسی و بندرعباس حمله کردیم
🔺
سیستم‌های دفاع ساحلی و موشکی، سامانه‌های پهپادی و ظرفیت‌های دریایی ایران، هدف قرار گرفت.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6091" target="_blank">📅 09:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6090">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/naXlskZj5-PcFgPrtia0jGWb7HUCzK_tFeDRGHN4rGokde3hZ_3cowvudgHwxXA7Lc8CVaYMgReGwRT8SKOX97x3RVwOMS8rAe4agmviQmH1627H1VE83oxi7JP-mUtYaPGGqkRbiNNDdtzulcsPsKFAZx_CRONJDujTt9Rgth-j-NWhRKjY4E9xWD_ndTtDh5l8DoChyAcYhm6COCF_bJT-uxfUwg6GQq5l-sL6VQ__UenJuHEcjctsxW_26ak6OJ6cDUBjqsWJLEkSzAxZGpHmweOsfbHZue65wP7slfwATR0VZSzv8o7GWklkBrMnanZNQ1NdjahID3xCQXYTrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شب گذشته سپاه به دو سوپرنفتکش (در سواحل عمان) حمله کرد.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6090" target="_blank">📅 09:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6089">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/671b861555.mp4?token=gW11UoyPtege7kJvaY69D8UShSDXu6O8B-WsEpgT55kJvA2onf1WDWb9MGfcVJPPvYHBumqGMbnlJlUQaIlF0wgqjuAgB1BKPS9hvoALRNIMY2_IYSMUHB85IEa-Jh-s477_tSzRoQZTrpLzn22SvfEbUWESZ9pN-oBnd8Z7I2-7icQnooPrgqB3sE21OoRgEMvXl3gvs-dyHd2kSFGF32MbIEjD-9omHrRxGkF1Nllh2_ZTI8vXdXQ2_LpMS1WjD_OhxYZMm9qF79XVZrGiSAl56l1sc9WQ1WdD5yUosxdvjPgiKxmQ5Yw0qxfDAMGUZcHYhCpoIOiFiaigdGz5EVvaxe0RaJ5m3mLt7rCieVXlRKrrFDsTAaTiTltWDRaTxSyVYzjuFpF4S5Sn6qWpdXpN_0SFvq4xDNUsJt1q7nIrhiunB4eRMI6hprzl4fOE89yJN0fJA44cA05UeIISdYjnYSSJ30QjeVP9TmW4G2azGnOKheI1TbI5v18ndiZ3GSZXmJOT0VrQt1T64t0u3ORk6IIVMsW5hrcqZ16VUNwkzH3Uz7MxLQc35KImbL_c4sg-OD0ToP1jYRN08xM7Y3aFsetLeuoiq6oPCFzer-MDgjfMIvwDo8sWxEAbkrdcl-cwQhPA0K6t_95pZDGZYFVUddwxMy_jrFHmEQnisds" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/671b861555.mp4?token=gW11UoyPtege7kJvaY69D8UShSDXu6O8B-WsEpgT55kJvA2onf1WDWb9MGfcVJPPvYHBumqGMbnlJlUQaIlF0wgqjuAgB1BKPS9hvoALRNIMY2_IYSMUHB85IEa-Jh-s477_tSzRoQZTrpLzn22SvfEbUWESZ9pN-oBnd8Z7I2-7icQnooPrgqB3sE21OoRgEMvXl3gvs-dyHd2kSFGF32MbIEjD-9omHrRxGkF1Nllh2_ZTI8vXdXQ2_LpMS1WjD_OhxYZMm9qF79XVZrGiSAl56l1sc9WQ1WdD5yUosxdvjPgiKxmQ5Yw0qxfDAMGUZcHYhCpoIOiFiaigdGz5EVvaxe0RaJ5m3mLt7rCieVXlRKrrFDsTAaTiTltWDRaTxSyVYzjuFpF4S5Sn6qWpdXpN_0SFvq4xDNUsJt1q7nIrhiunB4eRMI6hprzl4fOE89yJN0fJA44cA05UeIISdYjnYSSJ30QjeVP9TmW4G2azGnOKheI1TbI5v18ndiZ3GSZXmJOT0VrQt1T64t0u3ORk6IIVMsW5hrcqZ16VUNwkzH3Uz7MxLQc35KImbL_c4sg-OD0ToP1jYRN08xM7Y3aFsetLeuoiq6oPCFzer-MDgjfMIvwDo8sWxEAbkrdcl-cwQhPA0K6t_95pZDGZYFVUddwxMy_jrFHmEQnisds" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: بیشتر موشک‌هاشون رو از کار انداختیم، بیشتر پهپادهاشون رو.
🔺
توان ساخت پهپادشون رو حدود ۹۲ درصد از بین بردیم. توان ساخت موشکشون رو ۸۹ درصد نابود کردیم.
🔺
یه کم توان براشون مونده، اما برای ما هیچ توانی ندارن. این دیگه تقریباً یه درگیری نظامی کوچیکه</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6089" target="_blank">📅 08:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6088">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3962370842.mp4?token=Wi7vFuhkerHn7O399bnVaHOKbvJ-cW9LaEOZRT4bRg7GtCbNzsZUxFysSRlMDhtTb8iV_C_RlwbO-IzApEQ9ITa_S0d_4HiBRhmNd-1-mX-jnMzWU5w-ll1GA75OdZgRAiI0LW-oUcZCQb04qyYhRlGuZ_6kpsF_ANHwAhpR7UuXbbJv4auaAvUK_PID4-1WERtNzy0V8vWNOABCJsiuqt1qcIkE7Thm45_kPtpt9RCr9XbhVXRJx9n2fn_BjRVSVrcDc_ePULcHPxMB5gVm3ZZI0TTsOyOHFJ1Kz-l_NB4wC0Dx-bukoC8cdVSEYoEtDa0AdPKEKc5L8rnUEHn57A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3962370842.mp4?token=Wi7vFuhkerHn7O399bnVaHOKbvJ-cW9LaEOZRT4bRg7GtCbNzsZUxFysSRlMDhtTb8iV_C_RlwbO-IzApEQ9ITa_S0d_4HiBRhmNd-1-mX-jnMzWU5w-ll1GA75OdZgRAiI0LW-oUcZCQb04qyYhRlGuZ_6kpsF_ANHwAhpR7UuXbbJv4auaAvUK_PID4-1WERtNzy0V8vWNOABCJsiuqt1qcIkE7Thm45_kPtpt9RCr9XbhVXRJx9n2fn_BjRVSVrcDc_ePULcHPxMB5gVm3ZZI0TTsOyOHFJ1Kz-l_NB4wC0Dx-bukoC8cdVSEYoEtDa0AdPKEKc5L8rnUEHn57A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات شدید به کنارک - امشب</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6088" target="_blank">📅 01:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6087">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
ترامپ : حملات جدید می‌تواند برای دو یا سه هفته ادامه یابد.
🔺
سنتکام : موج جدیدی از حملات را برای سومین شب پیاپی آغاز کردیم.
🔺
باشگاه خبرنگاران : ۷ انفجار بزرگ‌ در بندرعباس</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6087" target="_blank">📅 00:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6086">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
شنیده شدن ۳ انفجار شدید در جزیره کیش
🚨
انفجارهای شدید در جم - بوشهر
🚨
چند انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6086" target="_blank">📅 00:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6085">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
ترامپ : امشب و فرداشب با قدرت به ایران حمله خواهیم کرد.
تفاهم‌نامه آزمونی بود که جمهوری اسلامی به آن پایبند نماند.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6085" target="_blank">📅 23:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6084">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">آمریکا سفارت خود در ابوظبی و کنسولگری‌اش در دبی را به دلیل نگرانی‌های امنیتی، تعطیل کرد.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6084" target="_blank">📅 23:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6083">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AH7ISOPxxzZxY95IRScno2zM08SQwzmwYkc0xBrUQtxsSJJ5rkv0soB3mQnAvV2RnVieWbcRTlhkYmP0BClTZYa9UjP8E_-3N2ADn3GrJL-lDYxERUVS7OKA6waJeXfIURTK7ukjOTRKE93GrhhB8-lxNjJbhoyKEjGTWzz5xuz6R3vBh12Ur2M7zVSQtDCewwhh-CYXxTJu23jLCNlMQ5ZnKPJ6kfnxFt6cMj7sZlNMroJ0bBmUIeO1Dx7wDNFMoiyjklYRWplYiRfseBk0ButJiwaED1AK0rJ4Dney3HQmXehdFh7sxOCrHzUWbmR12kaGYD8RurDtW369kG_f_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
انفجار در چابهار و کنارک</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6083" target="_blank">📅 22:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6082">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/645219e055.mp4?token=GcwdNCs2eY4ZTsjihnYsCd8ifAAM6G2dNsf0j92Nx7ZAZAsIDmmev8uP7DPWsfm-UMpdbbtoPueTXmdFFSGMYKXO6_YXK9efPuCvDk41U08g9PQvM6DL-TLWblJZs7NxOP-Qz6hBvpjT4cPNv4-_tUf1TedyUezQasbzNHltbE3sHFt7S-1Gibjv_TX9zvZTDEEpMO9ZsyS_KMLSp7PKbTDxB6pQ_LtJt2D3-Z9yco1aeTcBEket0hr0OV_slYFSkOCAVUhqg86a1EddsTfyVqLkjYZ44eUu8c3oSa_M7KLbyUrfzT0um6tpAJHXwHEEOf-AxsgvT_E_bZR2ALhEjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/645219e055.mp4?token=GcwdNCs2eY4ZTsjihnYsCd8ifAAM6G2dNsf0j92Nx7ZAZAsIDmmev8uP7DPWsfm-UMpdbbtoPueTXmdFFSGMYKXO6_YXK9efPuCvDk41U08g9PQvM6DL-TLWblJZs7NxOP-Qz6hBvpjT4cPNv4-_tUf1TedyUezQasbzNHltbE3sHFt7S-1Gibjv_TX9zvZTDEEpMO9ZsyS_KMLSp7PKbTDxB6pQ_LtJt2D3-Z9yco1aeTcBEket0hr0OV_slYFSkOCAVUhqg86a1EddsTfyVqLkjYZ44eUu8c3oSa_M7KLbyUrfzT0um6tpAJHXwHEEOf-AxsgvT_E_bZR2ALhEjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏آمریکا با استفاده از سه قایق بدون سرنشین (شِهپاد)، پایگاه دریایی دیروز بندرعباس را هدف قرار داد و تأسیسات نگهداری زیردریایی و کشتی را منهدم کرد.
این نخستین بار است که نیروهای آمریکایی در نبرد از قایق‌های تهاجمی بدون سرنشین استفاده میکنند.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6082" target="_blank">📅 22:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6081">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‏
🚨
🚨
محاصره دریایی ایران از فرداشب ساعت ۲۳:۳۰ دقیقه اعمال خواهد شد.
‏بر طبق قوانین اعمال یک محدودیت تازه دریایی باید ۲۴ ساعت قبل از اجرا، به صاحبان کشتی‌ها اعلام شود.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6081" target="_blank">📅 21:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6080">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be724e9f8e.mp4?token=p3U4-bA2xDx2nFxNUXWpODsbmLLplTMebUPoC90CPeTH2gR9nmxySjIp-c8I1nEg_KEJZp7OMqTQksFofU1Ol1BOunHNSTyF_ADuMpMrGQ6T6l2VsFMHCV1pvO20_bOP1CVkfaPnIJq-O89jb53Hbr5fgSl76_aasJOvsNIpmJG9JGC0wS8cf8vIT7EcGjfnaFvFGUQl_5HN12cxxrAEUcUt3YCg2fmiAbsyltq0kXCZseL77SoAX_DzQZARNmjUs40XQtafqYtVUz1VqL6e5pjf3hAbdXTUV3xIEMaG9j6-FOXmccZ9Pw07fXJTMXswVBRxShMPbO8HnwmfwwlNRpYldymhE-npXriS45cEpbpKfaf7uT7HtmUU4MJ5VJ9FENVXaW-JYV1AhfNjlPBVMK3qrQ4V-1TyRcpz4miHRD65aB5AipsOsnGbPsSdFwc-T5MHJtva1FqzAzMuCrMHADbVYTMPTaGlQM5mG71MR2ojH64YK57gWueJuwjffYkrigr5LJUC8DVErbxW6ljv6qCVcC7nzneagQRzrwvlc70J1tl2wl8lOkR2iiCvbgOJ8Gkmo2C7d_d91dL0HmEceoxahO3UHho2VxSF9uUujgKpkljODKcHVhv7A5QTHaA0K1-Tl1XWpk5rKRQmXMMzLuxIeR7g2lnVPFL02JU6wNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be724e9f8e.mp4?token=p3U4-bA2xDx2nFxNUXWpODsbmLLplTMebUPoC90CPeTH2gR9nmxySjIp-c8I1nEg_KEJZp7OMqTQksFofU1Ol1BOunHNSTyF_ADuMpMrGQ6T6l2VsFMHCV1pvO20_bOP1CVkfaPnIJq-O89jb53Hbr5fgSl76_aasJOvsNIpmJG9JGC0wS8cf8vIT7EcGjfnaFvFGUQl_5HN12cxxrAEUcUt3YCg2fmiAbsyltq0kXCZseL77SoAX_DzQZARNmjUs40XQtafqYtVUz1VqL6e5pjf3hAbdXTUV3xIEMaG9j6-FOXmccZ9Pw07fXJTMXswVBRxShMPbO8HnwmfwwlNRpYldymhE-npXriS45cEpbpKfaf7uT7HtmUU4MJ5VJ9FENVXaW-JYV1AhfNjlPBVMK3qrQ4V-1TyRcpz4miHRD65aB5AipsOsnGbPsSdFwc-T5MHJtva1FqzAzMuCrMHADbVYTMPTaGlQM5mG71MR2ojH64YK57gWueJuwjffYkrigr5LJUC8DVErbxW6ljv6qCVcC7nzneagQRzrwvlc70J1tl2wl8lOkR2iiCvbgOJ8Gkmo2C7d_d91dL0HmEceoxahO3UHho2VxSF9uUujgKpkljODKcHVhv7A5QTHaA0K1-Tl1XWpk5rKRQmXMMzLuxIeR7g2lnVPFL02JU6wNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqqRM2Plx2pRQPDILF-TgiXrGJ4CDhuIKp8_butv1RSVe4Tr_Np7sK07_TYSMr5Ypkcz1qGSHIXvuAvkqi3daSC-fkTxeKEfLA3FGygDyYF852VAduouQVLSEblICq4VQAfrJowgaUDaHsHZY4spCO-x3YkIO0yGo5T4zwjtBiTdBAH4ELWAsbyyLtBWnLTwqqa_nJG16Mnv1Jcrg2rhmwIszPV2aYx97gOYh57aksjGC8YUz6kGQVSmmPP3X3hvEyapSDnXGoN5PnUNCZXJZYGaVJNh6HfJn2NOIXnHUKpn1WFhVxGGa6AATozNb_kHvMqHSq-89wjhtVy7jTwIwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : از این لحظه به بعد، ایالات متحدهٔ آمریکا با عنوان «
نگهبان تنگه هرمز
»  شناخته خواهد شد.
اما در این جایگاه و به اقتضای انصاف، برای جبران همهٔ هزینه‌های لازم جهت تأمین ایمنی و امنیت این بخش بسیار پرتنش جهان،
۲۰ درصد از ارزش تمام محموله‌ها
ی عبوری را به عنوان هزینه دریافت خواهد کرد.
روند اجرای این طرح و شکل‌گیری سازوکار آن بلافاصله آغاز خواهد شد.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6079" target="_blank">📅 17:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6078">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yr_GycIpzWajFAyttbhEO3c6qfMYRUeQjaxu8MPLkIMHpo4f5m1OoiIUqEmS0I-KE82l2zbKQEG7nqPbpFjo8M3_Z0KSxaQJLcfPy66n_kBlLhA6KYWzRCaLbeREeaOtL7M_Vd3kIqTxJS7ilMlJFug7_EYGGbVS9AWcz75HUT5NVojE3NW8_fmv-5XecMB_bvImai1DfP5DE596-fKC1zdY5WRe-nWSf9B6_6f7D9cPjipeU37EKosTeFYQO5zMyva6HcEiOoW8LxXFuV3wVXTKsPGB7CAPjoExewzAuceikB6nA7ODZHOsxYWAjzlfTwtEDRvWWKVFDMkCV-OIGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6078" target="_blank">📅 17:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6077">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9nFNK3QM4QVYnu5_VX8mNmDs3uV1iaq9IiWnZEHZWJPTIWl0tatsh07Y5E9HDTpOnl3SL1J2bowW-Ac-Gs5pBjbL4ff-t-fLfL_PXFYAbKPplEjiGuOOJvSK-ylxLcTVICX5WX-Qx3Cusvi8eKgfnWGKyCn3hffPiopr4QYpTjnzYeLAy6jjd3Z8D1Z3A2gSpBy1RjbaMNUCjBq4gwqyO5X2E4Sb-nNFsDIpktpyFTqAPIYm7g23DxwVQPjGzCU8ljVSfEmFAFu8RU6p_U94DU2ww-Wk-cvxeActBdX5xmHLTx_fmK9OZcPdNWbfr8p_K6V7ijAEjUVEauCDzHhew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6077" target="_blank">📅 16:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6076">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترامپ درباره ایران:
‏ما کنترل این تنگه را در دست خواهیم گرفت. احتمالاً مدیریت آن را نیز بر عهده خواهیم داشت.
‏ما به نگهبان تنگه تبدیل خواهیم شد و وقتی این کار را انجام دهیم، هزینه آن به ما پرداخت خواهد شد.
‏ما ۵۰ سال از این تنگه محافظت کردیم و هرگز پولی بابت آن دریافت نکردیم. بدون هیچ دستمزدی از آن محافظت کردیم، اما حالا از این کار درآمد کسب خواهیم کرد.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6076" target="_blank">📅 16:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6075">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
دولت بریتانیا سپاه پاسداران را به عنوان یک
سازمان تروریستی
اعلام کرد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6075" target="_blank">📅 15:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6074">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">عربستان برای مراسم ابراهیم رئیسی «وزیر خارجه»‌اش رو فرستاد! برای مراسم خود خامنه‌ای، ولی امر مسلمین، این بار «معاون وزیر خارجه» فرستاد :)</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6074" target="_blank">📅 13:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6073">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/It2hEFYXbzYbVkioVDg0p9tgmtQ3YxPgBFm-fknEQ_8sNlvBvsPDE0aJ7LwbdV8PNp9IU4yaexcQV3szyZo581-Kp0ddZeg4gaXg6edPKpRPKIouEs-hiCqVfVw30YUScznyueL03yfOaFFTLf-4hKLpsd0i1y6hgj6HRyF7EzKNFzMj7arXFtz3YXG7-VzaODQ6KWR7jFgjmTCAX0tTk_4aHtbHJtvFYvZna2sWq7D5MeExj_vhjZ0VLym0HjH5cI6MqobLE1HEMEnxm_Nnb2QRGNPYvkrHhmvLz93r-f2PrPLDLb9Kuh2H4yC5q774EaJ8Qyhz8ktePDplishq7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای مراسم «ابراهیم رئیسی»  شخص امیر قطر به تهران رفت،  همراه با نخست وزیر قطر و وزیر خارجه  قطر،  اما برای خامنه‌ای،  سطح هئیت قطری به رئیس مجلس  تنزل پیدا کرد! قطر اهمیت کمتری برای مراسم شخص خامنه‌ای شد! از اثرات حملات جمهوری اسلامی به قطر!
🔺
این مدل احترامی…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6073" target="_blank">📅 13:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6072">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ed19EddXQDZWXEjHK8Beu7E55llGPm1dO16rrbrXww9eTbgNWy1iJapRyvulP1wINmNqo4VipgJwHZZ44SM0ldKDxSj4mLgHm4EImp2JUVz4dsZBn9mfdq4YtqBx2QBPQ7QiAn3feYCexXkGlV3-l6IWfC0y8mc8FBksmfKkt0wpXu-FaDoY6Nq2zInA5VGnBOQp2qLi-BZsCO103EJaqXw0og3YJ-MTunohV5GvAoZErnVtmYYo0Qbpqx9A5ZiPbUCAcYmxsBZyBb8jsll7KGmrXeSYbHw25oDdFL1JffnttNStIcc5IT7PEzwtR4pp4XlQtBycFM-IAsh-R28Szw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCRpfvdsBVjpJ-u18X440eu2pZZPOlMzaI7Wa0cfevQvHof0x0cu2R6aSgVr4c0Ys8iTl56V8poKXyusy7idH2KjWSXCEwfp3KpwwgZwxrqGW1oMWGPDOQess-bYJOLB3HoPpt4M8PWVw03PcN1PH9pOoFRmzuSU4cJ2vMhnuc5foxhCvkHd9KFoQAb1mJhljF4j6xmuLECAeQ0W8wsBUoXbvcB0yMtTMQg0lzXjdwygSGjvbsxgEu9ORHL0pUudpby48Qsm7spkC2r5D7Sqx6VNLKK8-fAqbo0eqBf5dqH0nvwSBdXWmAIumzyssYjxiXA0syjhRbOWj08g86a5cw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/868ebce267.mp4?token=k0tG9gjvKKSbsqCHNdNNXpTImRar00zEdThu51-ChsQNNn0TcWdJpRTVMDFNOv-Mm6Yw4c8PpVxyrxnP4u1Xu0okj_TbYN4Pamf1UZJ4tYNyURt3y51lviP3MSEc3fVf1OUUQ3uush1-fGLwcjcD0EqU3SdWhqwqaHQdengvAtgOJsjz7ATwoNQZI_03EjQLvcsbrKuFIDHBZtiQhSBkwnC3SBmK6e8e8NlDbTYk7YGhmlCbLMhCyBSVeKL8sluIRyZ3Eg9_d2IrBxfWJ-B-W7-BwdFRRnSLLhdz4rQAOIQsbjj4CNVXCeiS8yTSwnSeM6NW_sKjnMO81VE5179A3iJof1B661GNnQzFItKnHxs8cNUkBsprsyBoQ29ufqbbKyYU90dDUgm_aRpUOj6j_49nAByu2oYBpZTzwzjGedYWgcLMAiVIZ9tKWLlxNoHtc9KGCo9iuP8047pInECLbP5GwWOMCZugNtf_pTOtPiTq5JUH21oPnD_fzZcJnLIknjm4DQVl3gIQZY5Rw075a0TnixgUkXaFfVWPXjsF8eDM0SYs7JSCmZOVEd3ru8FVWOSZmCVwIdy159c57LhiGpFrTE3Mzs0FetVeoiehNa15VmQVQAIWtGtazFn8scSoZ7--5dWgLOyw1qiCGGAW6IWF3IV2C2DsPMw6S9H3UAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/868ebce267.mp4?token=k0tG9gjvKKSbsqCHNdNNXpTImRar00zEdThu51-ChsQNNn0TcWdJpRTVMDFNOv-Mm6Yw4c8PpVxyrxnP4u1Xu0okj_TbYN4Pamf1UZJ4tYNyURt3y51lviP3MSEc3fVf1OUUQ3uush1-fGLwcjcD0EqU3SdWhqwqaHQdengvAtgOJsjz7ATwoNQZI_03EjQLvcsbrKuFIDHBZtiQhSBkwnC3SBmK6e8e8NlDbTYk7YGhmlCbLMhCyBSVeKL8sluIRyZ3Eg9_d2IrBxfWJ-B-W7-BwdFRRnSLLhdz4rQAOIQsbjj4CNVXCeiS8yTSwnSeM6NW_sKjnMO81VE5179A3iJof1B661GNnQzFItKnHxs8cNUkBsprsyBoQ29ufqbbKyYU90dDUgm_aRpUOj6j_49nAByu2oYBpZTzwzjGedYWgcLMAiVIZ9tKWLlxNoHtc9KGCo9iuP8047pInECLbP5GwWOMCZugNtf_pTOtPiTq5JUH21oPnD_fzZcJnLIknjm4DQVl3gIQZY5Rw075a0TnixgUkXaFfVWPXjsF8eDM0SYs7JSCmZOVEd3ru8FVWOSZmCVwIdy159c57LhiGpFrTE3Mzs0FetVeoiehNa15VmQVQAIWtGtazFn8scSoZ7--5dWgLOyw1qiCGGAW6IWF3IV2C2DsPMw6S9H3UAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانال ۱۴ اسرائیل با انتشار این ویدئو خبر داده که ارتش آمریکا شب گذشته با بمب‌های سنگرشکن به یک ‌انبار موشکی در اطراف پایگاه چهارم شکاری در دزفول حمله کرده است.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6070" target="_blank">📅 08:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6069">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f4228d97a.mp4?token=NQ_pH69QXAP3gy7J4PE-knX6HJ3ge8nwj9qZJZ0aLlPLUF4LQxv6kZeT_9yBwf8dnvoa1XvjQR6qavEwz_dpjlHlcQXmLfBrz5eJcnwNAADAaQpXB02xcuUJ6K4aSIRu0mT17rtb3z7TaHNRw0Sm5zmfmloQ8PT4ZWFek9SSHPllqanRfgyNj6jw_V0F1qKt_SvoUEW-QFFDf3ZzRA2tD_eYxAS6whxOvwfotGdwgzXmqLGXDdV97RxAWFOMQqsQiJPoRgw6nFg_hd_LsCQl-SmDD2o8wkEmvbHy-tuO5NFfhdE-5cZzrfsFruEgxCgZeyJkwPyiuI4I_PljF8GdkEeaQ_e_VYimJHXSakLzdrUixrWYkAEuEUhWaVEvGLSdi68A8oxDZk7rZ_X7Uns-a8qUp9nNJQquh3HlNjHdBTuF_18r10MwnSGHnmvlX-2tMxRz-HwoCmXvI4IXg-QNJhv16JqMLx0E_z1Il4nySmBerxgk7PPVFJ13y0-HFr5chELdaVhQEFA7FdRMBiL6uWFS-MLsv1dZD9QM1w-1Q_v9VMv6TjQREzwOscXCGnp7ddZ40W7Fhhcpht6RIpTyQMn7fhiS0L9y2HeC5Fxe7eBKUs02_kzdfpmRKoPW0gl-mAwM0Cu0Rll5u6y9j3vfyujzs41eQlfRVW9drIJhXxc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f4228d97a.mp4?token=NQ_pH69QXAP3gy7J4PE-knX6HJ3ge8nwj9qZJZ0aLlPLUF4LQxv6kZeT_9yBwf8dnvoa1XvjQR6qavEwz_dpjlHlcQXmLfBrz5eJcnwNAADAaQpXB02xcuUJ6K4aSIRu0mT17rtb3z7TaHNRw0Sm5zmfmloQ8PT4ZWFek9SSHPllqanRfgyNj6jw_V0F1qKt_SvoUEW-QFFDf3ZzRA2tD_eYxAS6whxOvwfotGdwgzXmqLGXDdV97RxAWFOMQqsQiJPoRgw6nFg_hd_LsCQl-SmDD2o8wkEmvbHy-tuO5NFfhdE-5cZzrfsFruEgxCgZeyJkwPyiuI4I_PljF8GdkEeaQ_e_VYimJHXSakLzdrUixrWYkAEuEUhWaVEvGLSdi68A8oxDZk7rZ_X7Uns-a8qUp9nNJQquh3HlNjHdBTuF_18r10MwnSGHnmvlX-2tMxRz-HwoCmXvI4IXg-QNJhv16JqMLx0E_z1Il4nySmBerxgk7PPVFJ13y0-HFr5chELdaVhQEFA7FdRMBiL6uWFS-MLsv1dZD9QM1w-1Q_v9VMv6TjQREzwOscXCGnp7ddZ40W7Fhhcpht6RIpTyQMn7fhiS0L9y2HeC5Fxe7eBKUs02_kzdfpmRKoPW0gl-mAwM0Cu0Rll5u6y9j3vfyujzs41eQlfRVW9drIJhXxc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6069" target="_blank">📅 08:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6068">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=KBWkMqcCBDr_78_CKIGKWMAqZzQw8Pp9-RzSmxFdD1rP3VhVmSaurG0XX3BCKkK8M61u_5Wz7SqrHrfR3rjtKAWVBuTkuDrZUw4Y3dgxnJ8IWGXconjCm-wkrf6iJuaQpB97Jxu6t8ueRNpdXFwvFrgytg9sPGcmT6Q237-5g7uLximme69TXcXeHOiZrEF0mX6Rk-r1zlbwyuBbw6DKr3F9fwO-BIzESu7TJf2CsCzS4aUj2aUe3m7GxcFd8Muf3tFar65vI0vaXEiUTM1GRxP5GeLTst_uOfgANxXJb_FE9NV4b-BfUQiQbdCykWzHFtkEJw44oqg8fj_DJCc2_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f281af3eac.mp4?token=KBWkMqcCBDr_78_CKIGKWMAqZzQw8Pp9-RzSmxFdD1rP3VhVmSaurG0XX3BCKkK8M61u_5Wz7SqrHrfR3rjtKAWVBuTkuDrZUw4Y3dgxnJ8IWGXconjCm-wkrf6iJuaQpB97Jxu6t8ueRNpdXFwvFrgytg9sPGcmT6Q237-5g7uLximme69TXcXeHOiZrEF0mX6Rk-r1zlbwyuBbw6DKr3F9fwO-BIzESu7TJf2CsCzS4aUj2aUe3m7GxcFd8Muf3tFar65vI0vaXEiUTM1GRxP5GeLTst_uOfgANxXJb_FE9NV4b-BfUQiQbdCykWzHFtkEJw44oqg8fj_DJCc2_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات موشکی سپاه به کویت</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6067" target="_blank">📅 20:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6066">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">فرماندار قشم از اصابت ۱۰ تا ۱۱ پرتابه از عصر امروز یکشنبه دشمن در جزیره قشم خبر داد.
حسین امیر تیموری افزود: تمامی اهداف نظامی بوده است. خوشبختانه این حملات هیچ تلفاتی نداشته است.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6066" target="_blank">📅 19:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6065">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=LvqIgI2jbGtqa-6Bnyk2Y15Y5cJ5eI7UpFg2EXc7vKMLLjvhihEF9doFOAVXF6QaGpvWWHgVkBpcNtC8D3jV5OtziZyKgsBplzcgK4vzEPEHCqqKJkjS6dE51tECr1nZFfwW5BCuXJq10GPwXB2ZVrruh-htJ6X1hRJPPL_Ull-smuGH6Tlhc2n-FJVHhn7Gm91SmzKlfeukAms1TsJLBeZ7MLGyBoj8l4WHwTmV71a9CJTfD1XFjZADpv3G6uoBx8mV65eJzCFV1BDjBnZNSVMSgw2TTRPXnaQjGADU770ufb8pNLeifE6YmB333jDz7v48OrJXb6C3XNBi00m5Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d7e0d02cd.mp4?token=LvqIgI2jbGtqa-6Bnyk2Y15Y5cJ5eI7UpFg2EXc7vKMLLjvhihEF9doFOAVXF6QaGpvWWHgVkBpcNtC8D3jV5OtziZyKgsBplzcgK4vzEPEHCqqKJkjS6dE51tECr1nZFfwW5BCuXJq10GPwXB2ZVrruh-htJ6X1hRJPPL_Ull-smuGH6Tlhc2n-FJVHhn7Gm91SmzKlfeukAms1TsJLBeZ7MLGyBoj8l4WHwTmV71a9CJTfD1XFjZADpv3G6uoBx8mV65eJzCFV1BDjBnZNSVMSgw2TTRPXnaQjGADU770ufb8pNLeifE6YmB333jDz7v48OrJXb6C3XNBi00m5Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می‌شود که این ‌تصاویر از نتایج‌ حمله امروز آمریکا به جزیره قشم است.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6065" target="_blank">📅 19:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6064">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
آغاز دور تازه حملات آمریکا
به شهرهای ساحلی جنوب ایران.
بندر عباس و قشم مورد هدف قرار گرفتند.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6064" target="_blank">📅 19:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6063">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دوستان عزیز
این رسانه کوچک به‌صورت مستقل اداره می‌شه و در ۹ ماه اخیر، به خاطر شرایط خاصی که در اون هستیم، همه زمانم رو گذاشتم روی فعالیت شبکه‌های اجتماعی.
اگر این محتوا برای شما ارزشمنده و اگر مایل به حمایت از ادامه این فعالیت هستید،
این لینک پی‌پال در دسترس شما :
PayPal link :
https://www.paypal.me/Farahmandalipour</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6063" target="_blank">📅 18:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6062">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4bc671310.mp4?token=bfDZJm-HQ86KEO2ok3uoM_b8LKA8nDTqxUDsQycSc1xs1eaNd3m0FqD9wmEMHOo2qjm7s74aUJIlv3rVMCCAQ78MMr25Cwn4vLMsGhEmpPt-bmpB3fsDJOTqwzBWcU5pId31whf8M6xalpPDLx0GrXyBTS-4hlgaQ3UFusn70A9b1bknfAZSI55i6G41lB_OHZK0XOIV8eoCme5BTFQbomZ5AHNRb8-l1j2m0yNTRniQR_BkPjtgMu65TpuFVSEtX_TG4ZUbVD6XD_XzWFif4TZwQaZztwn3Vpzv5WfHJkJlTCrryODw1w7vcDJRE9WXtNOSxhIUGPdQJmRa_O3YGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4bc671310.mp4?token=bfDZJm-HQ86KEO2ok3uoM_b8LKA8nDTqxUDsQycSc1xs1eaNd3m0FqD9wmEMHOo2qjm7s74aUJIlv3rVMCCAQ78MMr25Cwn4vLMsGhEmpPt-bmpB3fsDJOTqwzBWcU5pId31whf8M6xalpPDLx0GrXyBTS-4hlgaQ3UFusn70A9b1bknfAZSI55i6G41lB_OHZK0XOIV8eoCme5BTFQbomZ5AHNRb8-l1j2m0yNTRniQR_BkPjtgMu65TpuFVSEtX_TG4ZUbVD6XD_XzWFif4TZwQaZztwn3Vpzv5WfHJkJlTCrryODw1w7vcDJRE9WXtNOSxhIUGPdQJmRa_O3YGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مثل باباش شجاعه :)  باباش هم در جریان جنگ ۱۲ روزه چند هفته رفت «کمین‌گاه»! برنامه‌های شبهای محرم رو هم نبود تا شب عاشورا (دو هفته پس از پایان جنگ!)  که دیگه در جنگ ۴۰ روزه غافلگیرش کردن</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6062" target="_blank">📅 17:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6061">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a80edc91f4.mp4?token=YuIVGmuYz1JPrcXoBzHLTBOOAghL2_oYo6OcrR3TUrfUO3UgMZw7hQ0X0KiiyUy-c80qXrGT8ftImsEzXctwAXwR63Us_Asar0VUT27YdDpt5P8UfI5Ky1ci1pDzDa7PWnRQvpF3DmUio5H-64dpoCbqjPX0XqcxnIh99D28inmzu-KxoVG3U22RHvCe8abvazU3eopWuRR5BAPzYJyWrJh03LxAsqMtypHP3GiNph53qgZgpgBeLpXmnrkPXHmjxqgrgeUnj6GBHEFrexvsseY3mUbRt6Bk-YAve0p0qtmAsyV6EuZMipPKZY1PDBaqGH0H4x7uFVikZBPBRBPxxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a80edc91f4.mp4?token=YuIVGmuYz1JPrcXoBzHLTBOOAghL2_oYo6OcrR3TUrfUO3UgMZw7hQ0X0KiiyUy-c80qXrGT8ftImsEzXctwAXwR63Us_Asar0VUT27YdDpt5P8UfI5Ky1ci1pDzDa7PWnRQvpF3DmUio5H-64dpoCbqjPX0XqcxnIh99D28inmzu-KxoVG3U22RHvCe8abvazU3eopWuRR5BAPzYJyWrJh03LxAsqMtypHP3GiNph53qgZgpgBeLpXmnrkPXHmjxqgrgeUnj6GBHEFrexvsseY3mUbRt6Bk-YAve0p0qtmAsyV6EuZMipPKZY1PDBaqGH0H4x7uFVikZBPBRBPxxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا بگذار مجتبی از «کمین‌گاه»  بیاد بیرون، پوستش نور آفتاب رو ببینه، شما هم به جای هوش مصنوعی، قیافه خودش رو ببینید، ببینید اصلا چه شکلیه، بعد به نتانیاهو بگو بترس.  راستی گفتید مجتبی دقیقا از ترس کی  ۴ ماهه قایم شده؟</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6061" target="_blank">📅 17:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6060">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QkvE_kaNG3iS5sV3ezo04KqgFxfaHH5wPAgmXxKwHGSt1STLbYh0VOHLWdQUkfisXbxwpcNX3fS0mMMFnbIDBS2szp5pgBiUM_Ql91-nWHS3BplkY1aSJJECUxo3F-uHFp8fXyZ8QNN4SCPyKYHp0ZqjmbJFdoIaONF0zYoDt6YapEYfW-_OCqKx_4o6p8aX8_eq6kBnl15e18dg2VH015ux9Pd1_OUpI2ZNqUFGWy1fLiYC24rth_a2ExT2GOkXFd1Xkp3klAQRmNt63XIAmHSCy_65dWVMGYeGQMVJuq9st7ASaKUxsqZacLWnqino7PlRzpK2EDLuEkPtVCHobQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fbb8lhvg8RwlvU5Ut3s0OlFaYjX5iDL0N175vWjPWhuKDIlmgzA1lE7yypBBAkTJG3dwLI1rxtSU9OXOFa3k_P7uqBmOZF0pUo5-PgSlClL7b7kpemB-9aaCDL0YtOikwFW7n4v_aHPi_htVUFWkFR5fIiqyHD-gne2azhdj1Ti4iuy0WavJM4JWJDFotwQg-uyW1DiwESWJg0ItGtpT8ZRIi-X0fsza3gblIDmtLhjWdft9rFFAcVWvnBk8M5GxvByWgqc0BtlcKitLMpsEq2HPnnx2ymwyH6rvoN-aDgVUmYnfm5ZfuBT41bTSvf1a5ePv-dzabS4WExAeI8vRxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشهد  از فردا : روزانه ۲ ساعت خاموشی برای منطقه.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6059" target="_blank">📅 16:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6058">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec46cc2c8f.mp4?token=rcrbKU-lE91K10MC4X9IwP8zgOEBlFN1qkdv4ZlM79jJCArRgFoLXEuWTyEd1oQciPpUlYoMQSgYt1ws4Tgx485hNnnnrnGI-Rh_h670l2GOOGUrjg7l2Yk3l8LSQx7Y1HpkmNDkw-0fDn5GCrs3dLYBbg01TCF1cKAolfNCfrg4lfSvOVCRdpBA8jwk3ZHOH7Jh2PK4RiRt0TQZ6Pti-Ovowiy56KffuNC-cm2yZWSWhMCwPp3nJxNUz21QVFYVaINnPK1milJYZEE6_-J_lDbWbFuU5Ie0LugGqDis4HNr5A3O3MwdeuMdSsg5lN_Wx1jYkEYBVD8bOr3nruYGsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec46cc2c8f.mp4?token=rcrbKU-lE91K10MC4X9IwP8zgOEBlFN1qkdv4ZlM79jJCArRgFoLXEuWTyEd1oQciPpUlYoMQSgYt1ws4Tgx485hNnnnrnGI-Rh_h670l2GOOGUrjg7l2Yk3l8LSQx7Y1HpkmNDkw-0fDn5GCrs3dLYBbg01TCF1cKAolfNCfrg4lfSvOVCRdpBA8jwk3ZHOH7Jh2PK4RiRt0TQZ6Pti-Ovowiy56KffuNC-cm2yZWSWhMCwPp3nJxNUz21QVFYVaINnPK1milJYZEE6_-J_lDbWbFuU5Ie0LugGqDis4HNr5A3O3MwdeuMdSsg5lN_Wx1jYkEYBVD8bOr3nruYGsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوینده شبکه خبر جدی جدی
خبر درگذشت لیندسی‌ گراهام رو دوبار خوند :)
فکر کن تاثیر یک سناتور آمریکایی رو
در برابر کل نهاد مجلس خودشون که ۴ ماهه
کلا تعطیله و کسی هم اهمیت نمیده :)</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6058" target="_blank">📅 16:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6057">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouQmA9d_2cM0fXHa72hII6efg3fghpqS8v5KNOl7tfwyBZkFPketGwcFwOOgzis4LsSuuocMglXbvR7RtUC7u_ed-t9JgWdLbAYTEZEhZXXOf-zM9gZp-45zitN3D4LRGi8EJIH2rx2dDa3CaZMtsD1YBhzFQY-WWdnPal3iojl9SHHaWpxQyhyoK7PfAXnWeXMNtdheK3WVuMAPRCAYRaNK5sYEhBdLQWFN_kv7LJN34aY5TKG3Q75xgce6RkY_4CyKOG7ZfEONRbrP302s_fsHKpvx-crKWo9ueKtBs25PZ8RTw-WGjXfjnY20AuyB0VTsq7nBo1HFpBjJQORwRg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6057" target="_blank">📅 13:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6056">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">رقص بر‌ روی ناقوس یک کلیسای قدیمی - توسکانی - ایتالیا</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6056" target="_blank">📅 13:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6055">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6675c3ed5c.mp4?token=rJyIzpy9Ctr-hgbE8ZzVB90pMZ5zzVQ9eTReHc9bKz54S5xV0dGA663m2zvxaJhrAF4lHlrnITf7FloW9uMTJSHR22jEIp0Mc4A9dlvhd12FtXwpN7E4ZQkp_EleqSfegScG1JQONbkoCESpCQregTadDY_JA4ZRacw5MEe-h7F4chAekEYO8z7tNvD2RULlG3X4sbDD7GW1AHwv_evWf6ncIFSgwXq0Wjd6POISiLoObPBEV8W_TmJqdu4RBPjGXB02wHmP-2DmON_yAIVSBSxORNYm3BuiaOxTQXL-XbMhbIFZuX43qaEBUxwm_OLvm2lmmDjq-YCnenT8YF9mng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6675c3ed5c.mp4?token=rJyIzpy9Ctr-hgbE8ZzVB90pMZ5zzVQ9eTReHc9bKz54S5xV0dGA663m2zvxaJhrAF4lHlrnITf7FloW9uMTJSHR22jEIp0Mc4A9dlvhd12FtXwpN7E4ZQkp_EleqSfegScG1JQONbkoCESpCQregTadDY_JA4ZRacw5MEe-h7F4chAekEYO8z7tNvD2RULlG3X4sbDD7GW1AHwv_evWf6ncIFSgwXq0Wjd6POISiLoObPBEV8W_TmJqdu4RBPjGXB02wHmP-2DmON_yAIVSBSxORNYm3BuiaOxTQXL-XbMhbIFZuX43qaEBUxwm_OLvm2lmmDjq-YCnenT8YF9mng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه اعلام درگذشت «لیندسی گراهام» سناتور آمریکایی در صدا و سیمای خامنه‌ای</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6055" target="_blank">📅 11:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6054">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkRr_y-qVLod_sMAtFTveypOGZDLkwe1rRUklwvkjqABUJ3cvQsl_D3IsvzCyP53qepzLS8IL_P5cl5IGwWligwLx5L2CkQLQ-84MG2lmG0wZ1A7kRkS2THqQXvEG-AMYDbWUw_NMJEVfJaP2_W8csuhWtSGYotUzLkwK7AkW5vg2LFWfVZok2EUj9bmYcaB2y3Pc3wjSKe8DHU9aMl2LO6er0X-qrJWzWYXbNykMQT5FgrLsHGkfxoGkVWQPFdUjBGEVzHAawOmhZ-5_exzlMz1si41H9_OhumjGME2GIsJPgsmu7pQ2r0u3AK8BiGeMb4dNU5-D3o2wIaNw55Lrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمی‌دونم این خبر تا چه حد صحت داره
ولی ظاهرا دولت اسرائیل
مهر ابطال به پاسپورت خامنه‌ای زد
و خامنه‌ای از سفر به بیت المقدس جامونده!
او هم به یاسر عرفات و عبدالناصر
و خمینی و صدام پیوست.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6054" target="_blank">📅 11:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6053">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پوتین براشون مدودف رو به تهران فرستاد، مدودف هم جمله‌ای گفت که رافضی‌‌ها  به ملکوت اعلی رسوند!  به صراحت گفت اگه تنگه هرمز رو بگیرید دیگه اصلا نیازی به «سلاح هسته‌ای» ندارید!  کنترل این تنگه اثرش از سلاح هسته‌ای هم بیشتره.   مدودف اضافه کرد که ج‌ا علاوه بر…</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6053" target="_blank">📅 10:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6052">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJatmvdddCXin9W5I7d146NtmkjgSKHF3qpl9Z4PyMEfDpQkWmmZeUzAwmmNQ_CxSlKjXPq6PO7fvxOrD7cHlCWaFfVdPmEnLa_VxBcXf1lfNqHXCi3eIr7gc3vNpmZrIiIrfCelyt6WtFW6WgyEfCtwx-Zfbi743vUpCBckLWvUdqL-pVOiyziGXypRXNyBWYtfi72GpnDKdve7KLLUUS_T2l6A_z4t5fQnyDHVdG3LBDPDFM5TjxVw8NSvfJwbMzNJpUR0OzQUJNpCgg8uYAzXgRwjrs9HsURSI5LJeknEtvg2mcXqD3eWyMWmGYFyyB_oG98gQqCnskD0rZ2tgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا اینکه اینها (قالیباف - عراقچی)  به یک تفاهم رسیدن برای مذاکره و یکسری دستاورد اقتصادی و…….  اینجا بود که تندروها وارد شدند.  اما سفر «مدودف» ، دست راست پوتین به تهران برای شرکت در مراسم خامنه‌ای  و حرف‌هایی که در خصوص تنگه زد، باعث شد تا وضعیت تندتر بشه.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6052" target="_blank">📅 10:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6051">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDRPiCs-KiF3fDmaxhf0txoUkh8C3EnxuOzvlxb2uvTdMuZ2wbBTmI_-SJHNpa3Rv6wu3AIfaWtjrkqmPVu533NB0sRaOhWoJmfp5UVSmQ2VsF1XR6jQQkT1I7yLzHgiuiYH9DsZqdMYVgnkV4V8-YXaDyEhYxqF83yjsWYRrxoknkV98zaovGECaVgWK6v-4karTvlBpRqFI2v4lFpLMjuwQhYhMPzBBedg6vdpeH8G4F3FR82t9-QMNcyBDYtlssCjtmdQEOQkZLKr08u4zDbxQFg1b2MqVuKw1cQKwD5fcIig4bTUyACr275iG2vXjazQjtz4i1y93echrqCg6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و به یاد بیاریم که پیام تبریک پوتین برای  مجتبی خامنه‌ای،  حتی از پیام‌ تبریک شهردار تهران،  حتی از پیام تبریک جوادی آملی، حتی از پیام تبریک تروریست‌های  حزب‌الله لبنان زودتر صادر شد!  پوتین به مجتبی خامنه‌ای نوشت :«اطمینان دارم مسیر پدرت رو ادامه میدی»  و…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6051" target="_blank">📅 10:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6050">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0KjVoOX5jU62-nSicez9z0HQppkkBn2PQZxeRVu7tzeaffQaV9EvxcCj_gx2MS8fSpe2g5jG_Sc6CLTrikEmcVL_qTQdQXwRwuONpkwyjpg3RQTA8kw3emus1aHGxGumensT12H_Fz2gleKp9RmlQsW13MH6g9Yyc4kjg1G9LkLD0_izAvi3G6Wu3cbIyFSX4AcQOxlLgw832LH9rOLLdehgXa6dAVPzYa1iMMQcLhQO4cZIJ5aaWrrO7nVmxidRFsiJiO914LeO8WnqhERzgJsrL_vnhHMn7kJNt52zT2wpsIew2Vu-SAlLQbkbLR9LTGHYBVn5q012_Gvrf1gag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به طور کلی در جریان باشید  که در چند ماه اخیر، یک سطح تازه و جدید  از درگیری در جنگ روسیه  و اوکراین رو شاهد هستیم.  کشورهای غربی به اوکراین موشک دوربرد نمیدن! و اوکراین مجبور بود روی مرزهای خودش با ارتش روسیه مقابله کنه، اما دست به تولید انبوه پهپاد و…..…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6050" target="_blank">📅 10:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6048">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wv9NlVse_SVBL7wz85IB4dnEdmVC3CR1kqj5uq9jwME8u0WluOZj-L0xGzyTpOkrHYDSQHDhA7bteIIld-32mrmXwNRel9mBY7b9hgMHVN0KqzpyRsXXWPatVf3PQR0o1VAS69hwfTmVg6G-R7Bg60ld6mAmVMHvPUgqWojIXeYDwln9xRBgz-O7rEPqvakqCibWJ0hvc5cEY46z2C6bC5sOtcqt4YAXznymDmjXuFbyaYIDFiugRfvbw5eKFHSbZjNe7xSMM9dwzWjmyZ605TnvLWqImiuSwmC_aCaJ7omw8dBCz8o5tcEXrs9s1ZFpCsDfrPOfjgNplP0ZFLho_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g1456bHihdWVykMskqAPuh2Y75e2lxlB8SBCkhIQm9sb-f9ku7m23gaIejXT7H6pHdYXP60ct2mT-SIGt8W1yEnxZJr7OdVcIlhRCv4heLcGH59WbofhIF5UNo5GONyhVdvEzYQklYwAmvvTIy6nuHvRuEqZKpFhm0WnPoUSSbJ-ilmGo6sGEniUuxKxiI5AWbVKEfPgHOZO1whFXfk9bE9ZNgG6s966R3JvzZyDE2er2Tn6QOBtwi8wZq_xOz3t3T08fd1u-Cfxgu514Z2r4-bo9rkooEGiA7Q8amLvpikGXkroHpaksbNZ1Z-lGr-0A6oavcwxwVnbdYCMtYjH3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب  و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز. این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6048" target="_blank">📅 10:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6047">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سفر مدودف، دست راست پوتین، به تهران  و مواضعی که گرفت در واقع تندروهای جمهوری اسلامی رو به شدت ترغیب
و تهییج کرد نا بزن زیر تفاهم‌نامه‌ و گرفتن کنترل تنگه هرمز.
این شد که موجی از شعار دادن ارزشی‌ها، برنامه‌های صدا و سیما، حرفهای مداحان و حمله به سه کشتی در یک روز،  راه افتاد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6047" target="_blank">📅 10:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6046">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLmnwDq_2Ce_qCdLRRpDhwQC2xvcrTkdU0RYT4loWmM5OJSgzHI79gc5vOkqnqnvF9KVifv_rr20jcXGcbTVGxeV3h1fsTcuC_lBdVySZwf-NO2KVYrn5_CGauPEwjNDcdlHJ5T0sIHLGdMGNe4vP6_Gzt7fi5c2b8B2VZsfFx63EK6mF7UL8gofE1kLDrjp6Adcxj1RdtbiztABYeDK3HJDFh6y95yrzInd0pt3OfthnCeOPYKcayotYpfkmrkmtbf_Bt71iBxECU6dx3ErkzVxOUGhc6pEv1OK07lMiLmDsSl6DBORFsOdMiQDpbTNv096mPsw3fmL8ujz-XltwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیندسی گراهام درگذشت.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6046" target="_blank">📅 09:54 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
