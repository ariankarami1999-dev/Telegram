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
<img src="https://cdn4.telesco.pe/file/Omc2RfyXRMwm9N40octplrz-Kw2cj_33NRvXDHtSamGlDKKVZABlPrDojgpsQZ1mSiVUqXfGIs9qH3yrpDNbRUwpHk0KrojK_rhAZb_ulF76Ck4F-YLyLpz0Ar1HEzLrFFHQ1gRd03GAmX8djScUnEiGbOSj9H40OIObOD1qefvA70SQZOCPQ_56ng77rC4taXuw_IVNoikEv0fMO7sU5a3LjQRZ4AV7tZiieLmxcruP6L3Uaja3-VX5JvUQkCcXpWV5ZFElCCfL57S8fe1BVZaeYpG3zSMYhMF9BEKtB5HTbJS4253CxY5dmquP4SCoAaKjp0GYXdjGSkJQBH67pg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.41M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-18 09:36:53</div>
<hr>

<div class="tg-post" id="msg-697121">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EzICpl_VOaxB0pm5ZVK3Ectt-7J-MhUjrfj9kfhzFZdSsEK2CtEpeVg7pxTq_BKSw5cpmpnPOoBW4IwgjmuyOMu1YDVOvZBA-5zwlcF4bBH6ezuGgKMYjNvaH7TW8-SLC8r6HvH-2JVLP12MXMNk-WpkEGqnrQ9Lo7CvvHf7eoqACNalStd_IH9lgm7jdqXehFezf-FbOFB1ZItLwcVL3d5ua3L2bd_GKwBkR3WXj_sN9sFve5HOmly9z15nBU7rD7TUFx0j1KT4Q3qjynHHDoGWb8kltI2yk4Tqkq3v6jOIxZJY4z2rSoL6OSw43iOJaK6irvOOUhGFF4zzZBDcow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ، کیتی زکریا را به‌ عنوان جانشین کارولین لیویت در سمت سخنگوی کاخ سفید انتخاب کرد
🔹
نکته جالب درباره این خانم اینکه پدر پدربزرگش ایرانی بوده و به ایتالیا مهاجرت کرده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/akhbarefori/697121" target="_blank">📅 09:30 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697120">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
رئیس سازمان سنجش: سوابق تحصیلی داوطلبان با تاخیر به سازمان سنجش ارسال شد/ نتایج نهایی آبان ماه اعلام می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/akhbarefori/697120" target="_blank">📅 09:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697119">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZeMZ3jlo6B4WlU-07VkUpuzgNkQSKvQOc23AEuNihyItFwTYV95uDQsRlOw9h7w1CrMxh1rYhIMukxLPR50yMgzZKwgaIDe4GMygzDKWvKcPZ3sTWJbG-alzyUpdqUCu1yH4YE0HpjllZAFXxE1Lt6Uxmf85q6fzjtyce2JO4BU3eiKgAuqITQaRu0L7Whd2ZM3NA4hIt3-j2cQdaVdFenNZRHal5boifDaOkTDfMZyKqajci9cOXqOxhh09oHc5hG_hTA4NDxybx1Lkxtp1P9C98YOs4Zf2FLMdVixMV8calTMyUGJgexMDXhUst-6V4ywzzMgWsnYFd57CSvV5WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ دوباره از آرزوی خود برای دریافت جایزه صلح نوبل گفت! #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/akhbarefori/697119" target="_blank">📅 09:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697118">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a448627028.mp4?token=mMH4CtAoUVKWfo8__q2NAMalAoiaJM44DrRDf1gIqIITYYYOdCS6jD5j4cXuZcsBM-0xEHevuAjo-V17wAoo0dSVz8R3YxAefE1BgwgjQJSz8spkO4KHP5mIcRv8w75eTIUjWQan27oZgrKJM3Or14UQzaxAeZGM0nnDJf074h5bET6taIeTj6VjM1pB0WJjavJst-FG6_-mccuyf_sz8bwtg2Gz54Rc7WwZuCOQtdWgiz4DY1NetVjPDy_8RabXFaj5tS3GIYYMVcbnNZK_Jzn1qvh_G7ofUpvb_uhQ5pHZojYcnwhxW1DC7BwYTHes9Qj7r4fSpPVoQo1ZWdBgmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a448627028.mp4?token=mMH4CtAoUVKWfo8__q2NAMalAoiaJM44DrRDf1gIqIITYYYOdCS6jD5j4cXuZcsBM-0xEHevuAjo-V17wAoo0dSVz8R3YxAefE1BgwgjQJSz8spkO4KHP5mIcRv8w75eTIUjWQan27oZgrKJM3Or14UQzaxAeZGM0nnDJf074h5bET6taIeTj6VjM1pB0WJjavJst-FG6_-mccuyf_sz8bwtg2Gz54Rc7WwZuCOQtdWgiz4DY1NetVjPDy_8RabXFaj5tS3GIYYMVcbnNZK_Jzn1qvh_G7ofUpvb_uhQ5pHZojYcnwhxW1DC7BwYTHes9Qj7r4fSpPVoQo1ZWdBgmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیو وایرال از حضور یک روحانی در تجمع که شباهت زیادی به رهبر انقلاب دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/697118" target="_blank">📅 09:07 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697117">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">چله علم النور 4_ جلسه نوزدهم-</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/697117" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
جلسه نوزدهم؛ تنها حمایت‌گر
🔹
سالک باید در نام مبارک المضطر، دعای خود را صریح و شفاف خدمت صاحب‌الزمان ارائه دهد و طلب دستگیری کند تا به آن قوت بخشیده شود.
🔹
اگر انسان‌های ذاکر نام‌های خداوند را در هر کالا و لحظات زندگی بدمند، ذهن‌ کل به سمت نور حرکت می‌کند.
🔹
حکم الهی امروز بر همدلی، دوستی، اتحاد و کمک به دیگران است و افراد باید در نوازش و محبت الهی قرار گیرند تا عذاب الهی برداشته‌ شود.
🔹
امروز زمان تسویه حساب به خاطر خشم و دلخوری‌های قبلی نیست چون در شیوه‌ ابلیسی، نمی‌توانید به آخر‌الزمان باز‌گردید.
🔹
نور نام‌های«الوال و المتعال» در وجود انسان‌ها رشته‌ای از محبت ایجاد می‌کنند آنها را در محافظت فرشتگان قرار می‌دهند و به آنها توفیق می‌دهند رسولان حق باشند.
🔹
نور مبارک «الوال و المتعال» بر سرزمین‌ ایران تابش می‌کند و با ورود مهر و دوستی پروردگار، تقدیر این سرزمین را در جایگاه برتر و متعالی رقم می‌زند.
#مدیتیشن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/697117" target="_blank">📅 09:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697116">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
جنگنده‌های متجاوز عربستان ایستگاه شرکت نفت در استان الحدیده یمن را هدف حمله قرار دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/akhbarefori/697116" target="_blank">📅 08:56 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697113">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ExPQdMdgCk8xXmALs4ahYpLDazknV8mOnwL6RRuSKtJUZWH3AUW8JVZn0RDdV4nQGz0TnmGrxIipMMyt0A_gIEh3-FGiz7O8ZfFf4sZuW2vKiX2WncjgJGqaJYOdFVLktlRRP78SPbqw68w1uQ6lxBuT-ilqjpAAaAkK7JCkB4-BtW6oUuX53Q6tX9Ipgp9h0d2KNwusBqz-pHiaAK9uVWXPDKV3CymC_hLz-9t79cfKn_MamDTzRWMwyIEzg87lxdOkKVXkgnzeGRh1V2kV-6SwIpdusd_pmkY-GawH1ui3sLvnvaKFlPGKq2Gxt_af-aT0XeEtoP_k8vMPVaprQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AojLv6XeuoqPL6zTbgvcYdIo5VVvo3AxiqC7-GqGrn5WoVzOfcAJ5OLkBVoohsMYNvtxmFt5rw5ZCaY6RDA_Uo7_1TbGzsqA_PHzfonrzvTGCHdPhPPguhwdFepTWHg4HmP_1IJamMfdXe4HaEONAtdOKWgUphVip-lqoPgImL1scHFQ8PFbME9ef9C_t5CdYaHY_XlPtU5XInZDMDuFOTJdev6LVTnjEJGfB3n0KI0x65KN4-baOmcWtGmSdw2XQhz4Rv7j4oLeBjUXfdeBG-a0S2YMB-qaNCuRKlk8W1ZdbJaGDLbIq47dCXf86cQUuxbwF1CQSlNo_pCL2faETA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BoVDrg3cpub9O2aLFUno23DDSA7ZhWurheaCMsd7qlJ1b31kHQw3HQjH3eTHPDpFLHgT7v-dB3fi3_2kERLSY0km216ri3d22swMaBvY_BzQBd9Tqq3DX9C7IQw7ARUSIKZG2OF5wB0z7nH-h29CJpFy3msP1Chcfo_e1V5aLype-TJVB7ErzMCewPSMqX_FMA8IgHJ-XeK78TDax9JuZcMj1tTcdzdTxl9IfIsXaYU2DTJLAtAJjc75ZLUn5n2ipOJ6lO3mR0E4ERNyv_J3IgzxCupUD4VToDYed0-_XrFBBQYvJtKmgIyJ5fDapYULiii_fZ5CNmovELKkLBrQRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
گاو دریایی، مهربان‌ترین حیوان دنیاست؛ مغز آن‌ها قابلیت تولید خشم ندارد
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/697113" target="_blank">📅 08:52 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697112">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bdc8ffee1.mp4?token=V65jLKCVO1fxWkbxVXS0Cj5O3jdD9WaL6kBQkz5yR0kau0xwmQ0ryvUF_HIWTNgQviK36vLMF4im4wmiNCw9glNbX8_QXkD4gIpmGe1ZS1bs4pLlNdaUGe6RoQshHvrgXBUNS_rsgkNTlNviPkXTPT1trAPX8_ZJLHyzBQtw98wc2Pk90wRfjfwP_pP7o1Z6q2etIgeR-AXWjExLuCapdADPDJj-YaMuYYDOH8WES1VTxtPxy69Tshd1EmSvLjYXzBiG1xLjm9EmLsvf35ctM5FboOIEHjjA3I1sRaLZSTW3w8w3kUlD6POlmYGP2L6QobfT-xVTk0QEUPqHpss25Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bdc8ffee1.mp4?token=V65jLKCVO1fxWkbxVXS0Cj5O3jdD9WaL6kBQkz5yR0kau0xwmQ0ryvUF_HIWTNgQviK36vLMF4im4wmiNCw9glNbX8_QXkD4gIpmGe1ZS1bs4pLlNdaUGe6RoQshHvrgXBUNS_rsgkNTlNviPkXTPT1trAPX8_ZJLHyzBQtw98wc2Pk90wRfjfwP_pP7o1Z6q2etIgeR-AXWjExLuCapdADPDJj-YaMuYYDOH8WES1VTxtPxy69Tshd1EmSvLjYXzBiG1xLjm9EmLsvf35ctM5FboOIEHjjA3I1sRaLZSTW3w8w3kUlD6POlmYGP2L6QobfT-xVTk0QEUPqHpss25Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظاتی ترسناک از امواج عظیم همراه با رعدوبرق که یک کشتی باری غول‌پیکر را ناچیز نشان می‌دهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/697112" target="_blank">📅 08:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697111">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5d59d8cdb.mp4?token=eM0NOzYYF3Ocs_BukYV35HjmVcsJg-miitea39FxaVEDdGnqqa2r1w24hE496cCfOYRy3adx-I-6FTBdp7vVOTL81AEnpUYfxJXxdtcIfT-mvd_baS3DC5YKmL_DLEHNqjYEFGEoMWeR1y9rJzy6JKvyxbJGmqLWrHTnmlxPxaABeRiOaiASFivYIT_DBYGITwmGrIVCSNDrhRGS8YKF0gxehNjK765-VT15A4RkLNF4H_daqltXvc672yR3NVPWqQP-Y3pJld6N2BC1ecxpiiWJ_qz9X4TA3ScwQHGhuNbAzkp5q7tpYl95SFK5tb2LQjQXZ9xeJxSSgQ4H8CcXnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5d59d8cdb.mp4?token=eM0NOzYYF3Ocs_BukYV35HjmVcsJg-miitea39FxaVEDdGnqqa2r1w24hE496cCfOYRy3adx-I-6FTBdp7vVOTL81AEnpUYfxJXxdtcIfT-mvd_baS3DC5YKmL_DLEHNqjYEFGEoMWeR1y9rJzy6JKvyxbJGmqLWrHTnmlxPxaABeRiOaiASFivYIT_DBYGITwmGrIVCSNDrhRGS8YKF0gxehNjK765-VT15A4RkLNF4H_daqltXvc672yR3NVPWqQP-Y3pJld6N2BC1ecxpiiWJ_qz9X4TA3ScwQHGhuNbAzkp5q7tpYl95SFK5tb2LQjQXZ9xeJxSSgQ4H8CcXnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روزی چهار بار، این حرکات رو انجام بده و با قوز کمرت خداحافظی کن #ورزش_صبحگاهی
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/697111" target="_blank">📅 08:42 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697110">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
انتخاب رشته متقاضیان رشته‌های با آزمون دانشگاه آزاد شرکت‌کننده در آزمون سراسری تا ۲۴ مهرماه تمدید شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/697110" target="_blank">📅 08:42 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697109">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd37e68cad.mp4?token=eB8c5pDqiOdMmUmriXoXQsjQGBWzHMWqolz0cnxf5xhjQRNKMEKv-P7hAzIXqV-xnHCnLOTS0sW0nbHpqJEKZkeJ-tzL0cgiMLP_LKHtjCOGp9lTXa5T19lNSi30FxTbxldennD5aiVMnjeawDFolIv0WnborBGnL6hbTDJXByg4FIAiXx1wWiJ3FOSL0Yja7O5U0QmLBg4ipVQZUoOZKTyPMlkoD66NC_S-SO1NAxW-7H-_eQKec18n2LviqaIUBZRQokECVR3r2BrTsX3AVXEylndKtpnIoFCf4ZzK_0Rn7UYZlqZHK6wlxfF8LO-SQO0qFqT46WRqk2Y6NrEPlampL0OYjVa2KEzeMR_Ot6mfwxCtaIxNEmu5y2xBMRGbSUA7B-s8sYiCrhzaIw6wqgBNe0ftuQrZUYgHU2-jCRNg13n2j3eE9rF1dsA_gGhW5gTqBbvpbGbVa8IeovFDI7-PnSgmPYsukFd-Qcmex9CrzQjLjyhWgKZMqW-kChRjE1azndgKpcs7c2VU7U75L6bMexuKYoID8u0u3KmT9JZbMZlgrcF5ufC-EekVun8vkKVoWK7QbKaM50FMuU-82tibVX8Z8TaEotzcISYw7tlGb-vHdFz-qxsO-xrS7KvYgaiuzOq7NYA6_uRhmVpH5ekZpeDb2c1ylv9sTWOr1Ik" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd37e68cad.mp4?token=eB8c5pDqiOdMmUmriXoXQsjQGBWzHMWqolz0cnxf5xhjQRNKMEKv-P7hAzIXqV-xnHCnLOTS0sW0nbHpqJEKZkeJ-tzL0cgiMLP_LKHtjCOGp9lTXa5T19lNSi30FxTbxldennD5aiVMnjeawDFolIv0WnborBGnL6hbTDJXByg4FIAiXx1wWiJ3FOSL0Yja7O5U0QmLBg4ipVQZUoOZKTyPMlkoD66NC_S-SO1NAxW-7H-_eQKec18n2LviqaIUBZRQokECVR3r2BrTsX3AVXEylndKtpnIoFCf4ZzK_0Rn7UYZlqZHK6wlxfF8LO-SQO0qFqT46WRqk2Y6NrEPlampL0OYjVa2KEzeMR_Ot6mfwxCtaIxNEmu5y2xBMRGbSUA7B-s8sYiCrhzaIw6wqgBNe0ftuQrZUYgHU2-jCRNg13n2j3eE9rF1dsA_gGhW5gTqBbvpbGbVa8IeovFDI7-PnSgmPYsukFd-Qcmex9CrzQjLjyhWgKZMqW-kChRjE1azndgKpcs7c2VU7U75L6bMexuKYoID8u0u3KmT9JZbMZlgrcF5ufC-EekVun8vkKVoWK7QbKaM50FMuU-82tibVX8Z8TaEotzcISYw7tlGb-vHdFz-qxsO-xrS7KvYgaiuzOq7NYA6_uRhmVpH5ekZpeDb2c1ylv9sTWOr1Ik" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت رهبر شهید انقلاب از نشانه‌های تغییر نظم جهان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/697109" target="_blank">📅 08:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697107">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/377d650d8f.mp4?token=AgiljnhXiZQbKTczlyaEkRxlWFKnW5KUFf3_U0G6GzAcmCaruMKUtunXV00VFvhcPXiwPDsBtTmyTYVMvkz0naUSv1PZVCAxlt5sPA75fUHSoYICHY-95uUaZkSZ5r1-esGfUFUMG6Ek5m3J3NaHqd_fcW13WhwG6LiljMksH3FUspigjnZLzUuVczDBn6fwvifqeQzbdcVozKOqm4KYYWRTwEFs2qpg5YBW2U9wuPY2Rts5tQD2kGXlVuCme6-ixwpee7-JBnzg6Qh20s1OUdlp3NBdcKybObtUcnnzzV6mr69dWCDrzKyvZw3ImBFb0o5DRrO9pOnzj23UcgWLvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/377d650d8f.mp4?token=AgiljnhXiZQbKTczlyaEkRxlWFKnW5KUFf3_U0G6GzAcmCaruMKUtunXV00VFvhcPXiwPDsBtTmyTYVMvkz0naUSv1PZVCAxlt5sPA75fUHSoYICHY-95uUaZkSZ5r1-esGfUFUMG6Ek5m3J3NaHqd_fcW13WhwG6LiljMksH3FUspigjnZLzUuVczDBn6fwvifqeQzbdcVozKOqm4KYYWRTwEFs2qpg5YBW2U9wuPY2Rts5tQD2kGXlVuCme6-ixwpee7-JBnzg6Qh20s1OUdlp3NBdcKybObtUcnnzzV6mr69dWCDrzKyvZw3ImBFb0o5DRrO9pOnzj23UcgWLvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحبت‌های تازه منتشر شده ظریف وزیر اسبق امورخارجه که جنجال آفرین شده است: من گفتم با برجامی که یک جای بدی از بدنتان را پاک کردید، فردا بینی تان را پاک می‌کنید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/697107" target="_blank">📅 08:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697106">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
کویت از بریتانیا سامانه پدافند هوایی خریداری می‌کند
🔹
دولت کویت قراردادی ۴۸۹ میلیون دلاری با یک شرکت دفاعی بریتانیایی برای خرید سامانه پدافند هوایی امضا می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/697106" target="_blank">📅 08:31 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697105">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jw6Fgfgb7F1SIpSTchsPK6t8vrregK89bfpNvH6n1rmHdOeU1zCemZYi2NMdpBOm-tfAclZ9G8N_3hnO7wUzViJRrqXRevW5xTq5RWJgQTk4igzEIoNjwmEjl67HStD7nvC_KHSuOIf2Cm8zPPhKO-mi6038j6NV1yhEeNuKV4jpGYnME7CsBIApJBnrkjkxcwB50Vsin0GAAvZgYyUrteyIuO8GAeq308GKeKcTyz6H4SmLH5j-NPRqb61UVoiQqISZIJuiqYqnBpOKZKnfPCMT2vHdBdqmlgXRp9bSa6dBK_7Pzon0zCHG_nMPznMiYEsdJDnTuv5FPRTrk47fHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رابرت پیپ‌ استاد دانشگاه شیکاگو: پیاده‌سازی تفنگداران دریایی آمریکا در یکی از جزایر ایران، بزرگ‌ترین هدیه‌ای است که واشنگتن می‌تواند به تهران بدهد
🔹
آن‌ها عملاً به اهدافی ایده‌آل تبدیل می‌شوند؛ درست مثل ماهی‌هایی که درون یک بشکه گیر افتاده‌اند و پهپادها و موشک‌های ایران می‌توانند به‌ راحتی آن‌ها را هدف قرار دهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/697105" target="_blank">📅 08:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697104">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0925073180.mp4?token=OCnNm8M4xywvdPFDjkFkeQ1GgyUGEhjR2Jv171GS0PUXQg8I-zGb3WZtyF8nxsSKIPN9nmzc9C1btMs3YJLFXPxVAmawkt-Hir4MuaRZIuHO2USvDeUXKJD89HQ8okIAJPQDA8JVMppZiAvf3HRwP36KqTMhEFoocWn0nX8moV-z6Siqnw5_zFY1omNbvK5ZEQTOxYKrn6lAplopq8UvLwfmdpp6qM1WBgPWEHC5kWFzjmlr-fOdwt-9gIN64sefEAA9eqAw2OeR7v_SkSERmH6jZF5s--bTz7qjcxtwBEFkeXdedv72mZLj4CG_08-TLMF773zPNUTcM04WLgIdcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0925073180.mp4?token=OCnNm8M4xywvdPFDjkFkeQ1GgyUGEhjR2Jv171GS0PUXQg8I-zGb3WZtyF8nxsSKIPN9nmzc9C1btMs3YJLFXPxVAmawkt-Hir4MuaRZIuHO2USvDeUXKJD89HQ8okIAJPQDA8JVMppZiAvf3HRwP36KqTMhEFoocWn0nX8moV-z6Siqnw5_zFY1omNbvK5ZEQTOxYKrn6lAplopq8UvLwfmdpp6qM1WBgPWEHC5kWFzjmlr-fOdwt-9gIN64sefEAA9eqAw2OeR7v_SkSERmH6jZF5s--bTz7qjcxtwBEFkeXdedv72mZLj4CG_08-TLMF773zPNUTcM04WLgIdcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: زلنسکی گفت که به دلیل توافق نفتی‌تان با پوتین، شما ضعیف هستید
🔹
ترامپ: چه کسی این را گفت؟
🔹
خبرنگار: زلنسکی
🔹
ترامپ: باشه.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/697104" target="_blank">📅 08:26 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697103">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bpIVa1L4SxwCIXGIb2K4UIkop8PZSPSfpJ5V4SLoZLTdHz79TmVC1lkCs7v_IedES8ls_5JrRfuB2kEWmriuDk8cegJIIIX9UeQfdOCDKHHpLSM05iQx7KB8kYt4YCkbDJ22QnJeLFSUvW6mJXYk-f3RTn24BGmy--Pp0LQqYjdAO19g9O3TfEUMGkOo3DHr29VfZOyHHo7n-XhxILUVAxLXQkXhjK43IxJpfFSGEJM_FndlybNGEvYxJx48H5HkncEVZbTQC18lPHitINUUC6hBO7O5dfyOmyTiN1CCe6PinLUnqcrzFKthRj6727nLLtJPzsYIae65aaDVsZukFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سناتور کریس مورفی: جنگ ترامپ علیه ایران، مایه تحقیر ملی است. این جنگ امنیت ما را کمتر کرده و باعث افزایش قیمت همه‌چیز شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/697103" target="_blank">📅 08:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697102">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
ضرغامی: من دیگر عضو شورای عالی انقلاب فرهنگی نیستم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/697102" target="_blank">📅 08:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697101">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40f201c233.mp4?token=BaU62YxK1S9g6E_FgbO6wG-VxZbw_BLHpAZRBPThwD-j8Tce3OJ-UQBQCJARhLnI95PE9IPr-W3_zFYRVFRikgtAR9P9CkfLRVReXEAhrgV7F7ZfMokeU6sjUk8HFW8f8OFSD2_q1Dme-n-qbR8z8MWo8qahDaCTVLnifsaF_UeUVIjqbdlcG5HzImI7w0SoASK6ZhD8Ca3mh3qoGJKUhMNrf0GAjC0D25gkxmD_wLyfkqaEnZyCgic-ueNcyiZcHS3H8XluMeRmg3OHcoRye286nVbbZtb_cTQguhyEPW9sdzzMum4m-98-l9rCEVzYZ4T7Qkhb0e4xCO3N2inDBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40f201c233.mp4?token=BaU62YxK1S9g6E_FgbO6wG-VxZbw_BLHpAZRBPThwD-j8Tce3OJ-UQBQCJARhLnI95PE9IPr-W3_zFYRVFRikgtAR9P9CkfLRVReXEAhrgV7F7ZfMokeU6sjUk8HFW8f8OFSD2_q1Dme-n-qbR8z8MWo8qahDaCTVLnifsaF_UeUVIjqbdlcG5HzImI7w0SoASK6ZhD8Ca3mh3qoGJKUhMNrf0GAjC0D25gkxmD_wLyfkqaEnZyCgic-ueNcyiZcHS3H8XluMeRmg3OHcoRye286nVbbZtb_cTQguhyEPW9sdzzMum4m-98-l9rCEVzYZ4T7Qkhb0e4xCO3N2inDBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قطع سخنرانی ترامپ توسط یک معترض
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/697101" target="_blank">📅 08:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697100">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56814e1060.mp4?token=iIhstFe2l6vDsanHhizeQ5Kq6yMYRW7VGum4rt54CzlMSFoE4kIqNGYDIA6plWqvM1qRg76m8njTi5VgxWy2dr8Ns5rjwwnZ7biVJEoznUwtIAh4POKOePBdDAr6c45S_iM68QB_sTMhxIGMotgSlHAARt6bKZo54h-uZ-cK-IJlGTdOzkhCCEEHmb6t04OGHanzeumlg0noI-8hLvGzcsPJmM5H1JrsJW8BlPo83fYTKGoTqR6y4T0vXtMPLMGVUeC4DyqTX207eSueQPcDYMvgY5atczxBVAPbFDxvo323e_Y8KcshpkR5dUEylWgojxtpWyFtoCJsBoL1VYwC9i8sG2B7pFI79-ljcm5DeGlcgTAKezfKTgmr32yeWgQ_uaQZyLAn2pG5OQSFJpT8KbFjBaWkkymTPxMlAmf12winP668oWWPmmHyW_stunBMygT9nOzNSS2UsVtoqGf0fcNKz7vuHPQBw5dfggtfTIjBAvBtSB1YigIn3h9uvRALfO-6xfmoSYOzRj9q2MRFlr5kl3tZQ3LmFkYHEK4imlPoZk3C5-GRalf0kd_ZlFTsImiZ4ct2guFt0-cgX3bqLlmnFiN9pLk51P8ROoO6byPXIDKXOJgx9ksFwpIx9RAyQvNdEc-rHQzeZAorOQ9dFjfSVQEBHx5klh3aa14eiLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56814e1060.mp4?token=iIhstFe2l6vDsanHhizeQ5Kq6yMYRW7VGum4rt54CzlMSFoE4kIqNGYDIA6plWqvM1qRg76m8njTi5VgxWy2dr8Ns5rjwwnZ7biVJEoznUwtIAh4POKOePBdDAr6c45S_iM68QB_sTMhxIGMotgSlHAARt6bKZo54h-uZ-cK-IJlGTdOzkhCCEEHmb6t04OGHanzeumlg0noI-8hLvGzcsPJmM5H1JrsJW8BlPo83fYTKGoTqR6y4T0vXtMPLMGVUeC4DyqTX207eSueQPcDYMvgY5atczxBVAPbFDxvo323e_Y8KcshpkR5dUEylWgojxtpWyFtoCJsBoL1VYwC9i8sG2B7pFI79-ljcm5DeGlcgTAKezfKTgmr32yeWgQ_uaQZyLAn2pG5OQSFJpT8KbFjBaWkkymTPxMlAmf12winP668oWWPmmHyW_stunBMygT9nOzNSS2UsVtoqGf0fcNKz7vuHPQBw5dfggtfTIjBAvBtSB1YigIn3h9uvRALfO-6xfmoSYOzRj9q2MRFlr5kl3tZQ3LmFkYHEK4imlPoZk3C5-GRalf0kd_ZlFTsImiZ4ct2guFt0-cgX3bqLlmnFiN9pLk51P8ROoO6byPXIDKXOJgx9ksFwpIx9RAyQvNdEc-rHQzeZAorOQ9dFjfSVQEBHx5klh3aa14eiLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از وقوع زلزله در پاناما
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/697100" target="_blank">📅 08:17 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697099">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
وزارت خزانه‌داری امریکا مجوز موقت انجام معاملاتی را صادر کرده که شامل فروش، تحویل، تخلیه و واردات گازوییل از روسیه تا تاریخ ۷ آوریل ۲۰۲۷ می‌شود
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/697099" target="_blank">📅 08:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697094">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
پوتین به ترامپ: گزینه‌های دیپلماتیک در پرونده ایران هنوز به پایان نرسیده و دستیابی به توافق، امری ممکن و ضروری است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/697094" target="_blank">📅 08:07 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697093">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/420dde080d.mp4?token=u_1VXHJdamSk7WiKg2jLMfraavSQFuhZC94-GDrpy_QMJxb-4dKXz5pCbps-1eOytqBbkyxZHWmAUEBAod4yV7xOjoK1BM_COGJ5xD2BV_JXmUUHkz7mOz71FQk3qpodmSb2jsJBK1_zSJ_5J2RLbEiR5Yw-5TSREAQpANBowWC9bdXQcRFkuaHXTj8vfxZekXY9FFn2Nn5Hr9z-bDu37BEVsnDXOW0tc3uRko69FReo1V6kkVn1BHKjy-2_EutSH9XMncn1GUKQ8MqpqYy4K2LYCaO0ATERmVuy68GZV9oZ-VGT7nFOBvwFH0H9LnsL-hgrbKlO2tipfntl-Cg3wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/420dde080d.mp4?token=u_1VXHJdamSk7WiKg2jLMfraavSQFuhZC94-GDrpy_QMJxb-4dKXz5pCbps-1eOytqBbkyxZHWmAUEBAod4yV7xOjoK1BM_COGJ5xD2BV_JXmUUHkz7mOz71FQk3qpodmSb2jsJBK1_zSJ_5J2RLbEiR5Yw-5TSREAQpANBowWC9bdXQcRFkuaHXTj8vfxZekXY9FFn2Nn5Hr9z-bDu37BEVsnDXOW0tc3uRko69FReo1V6kkVn1BHKjy-2_EutSH9XMncn1GUKQ8MqpqYy4K2LYCaO0ATERmVuy68GZV9oZ-VGT7nFOBvwFH0H9LnsL-hgrbKlO2tipfntl-Cg3wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زلنسکی: اجازه دادن به روسیه برای فروش محصولات نفتی، به مثابه سرمایه‌گذاری در جنگی است که باید پایان یابد، نه اینکه طولانی‌تر شود ‎
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/697093" target="_blank">📅 08:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697092">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7ff41a1b6.mp4?token=IIULpgBRQNSKLIK9pdpokQRBQYc29rRd7lVx9WHmVlI86BOr31zxTe2ZgXuRB6OUV8lCfJVVtNd350LZL4mHrOUNPK43tUGhJvm8-bJEhL2jw3TCpBX_Yp0LTPJSR-35BHY8vYbPe8FkQz4oUJap5ou8lkCbudY80SqWz_1TyaV79GOpkKZM-DnGnn5Y7cAqMpHe-N_UdmiD4F1LQfhKTXZ8p4Dmvk8EuBgAg6HpJjLcMshZWJ2kDKnHLZJGe108RZvf4OumsUNFi7QDI3v0luEnL9XCcGSAdhN8QDjTYoKIq21iDUo5DAtxBiYVveWC4qvWK1P-tfo9AeOadPVsvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7ff41a1b6.mp4?token=IIULpgBRQNSKLIK9pdpokQRBQYc29rRd7lVx9WHmVlI86BOr31zxTe2ZgXuRB6OUV8lCfJVVtNd350LZL4mHrOUNPK43tUGhJvm8-bJEhL2jw3TCpBX_Yp0LTPJSR-35BHY8vYbPe8FkQz4oUJap5ou8lkCbudY80SqWz_1TyaV79GOpkKZM-DnGnn5Y7cAqMpHe-N_UdmiD4F1LQfhKTXZ8p4Dmvk8EuBgAg6HpJjLcMshZWJ2kDKnHLZJGe108RZvf4OumsUNFi7QDI3v0luEnL9XCcGSAdhN8QDjTYoKIq21iDUo5DAtxBiYVveWC4qvWK1P-tfo9AeOadPVsvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ دوباره از آرزوی خود برای دریافت جایزه صلح نوبل گفت!
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/697092" target="_blank">📅 08:05 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697091">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47f6d0c50b.mp4?token=e3Zg85_0MvrtzvOeoiIqznkWCJLAc4gZaL5mluI7Md6PIOOF3dlIiAX999bGUXQK2ELkSr11GpC0vfDIYfHrQC_5qGurjyrRxPiEJPpSeW9F99kmSRDIktDr-Vbly2Iz9m9fUYVCpjiKzfQXBGI_Qe2Ke6Jc_23h7z_GjEoz7npfG6ax6ZczBjsFhExo6DMRnlUXcV0xpsR9VfUxq_A334JtgCrwDkfjQk6XiA3xtnrx6ZEpxjuxTb6aDO8BDnu7pJ_Eh20e5OoGjmIwY-O3tBf07NsZFWh4o1GP39MAfDyuZpBbzbFHuwPSCXRq-Pi8KqrXaC2smZpOF1vuz_HRdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47f6d0c50b.mp4?token=e3Zg85_0MvrtzvOeoiIqznkWCJLAc4gZaL5mluI7Md6PIOOF3dlIiAX999bGUXQK2ELkSr11GpC0vfDIYfHrQC_5qGurjyrRxPiEJPpSeW9F99kmSRDIktDr-Vbly2Iz9m9fUYVCpjiKzfQXBGI_Qe2Ke6Jc_23h7z_GjEoz7npfG6ax6ZczBjsFhExo6DMRnlUXcV0xpsR9VfUxq_A334JtgCrwDkfjQk6XiA3xtnrx6ZEpxjuxTb6aDO8BDnu7pJ_Eh20e5OoGjmIwY-O3tBf07NsZFWh4o1GP39MAfDyuZpBbzbFHuwPSCXRq-Pi8KqrXaC2smZpOF1vuz_HRdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزافه گویی
ترامپ: یا ایران هر آنچه را که می‌خواهیم به ما می‌دهد، یا دیگر وجود نخواهد داشت
!
🔹
مسئله ایران به هر طریقی که شده، خیلی سریع حل‌وفصل خواهد شد.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/697091" target="_blank">📅 08:04 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697090">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
ترکیه دسترسی کودکان به شبکه‌های اجتماعی را ممنوع کرد
🔹
ارائه خدمات شبکه‌های اجتماعی به افراد زیر ۱۵ سال در تر به‌طور کامل ممنوع شد. پلتفرم‌ها موظف شدند نسخه‌های اختصاصی با پروتکل‌های امنیتی و حریم خصوصی تقویت‌شده برای کاربران ۱۵ تا ۱۸ سال ایجاد کنند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/697090" target="_blank">📅 08:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697088">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
پنتاگون آمار تلفات خود در جنگ علیه ایران را افزایش داد
🔹
آمار رسمی تلفات تا تاریخ ۹ اکتبر به ۲۱ کشته و ۸۶۵ زخمی رسید. این ارقام از اضافه شدن ۲ کشته و ۴ زخمی جدید به آمار قبلی حکایت دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/697088" target="_blank">📅 08:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697087">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crgyQN-Gf6N-HMYzdMvyAwOmGgHwl1LYs_PnU9rfdI81m1sroeu6uQBV_2IaNp_nUC8j-lqPcNrbEnhQHuexSMT1QkwXee27AV6V3VgPKb0nQPYoZZFHdwO_9OUU56DPsFQfedttxWDcA3aiXxQR4rSFGRr6VbCrp8m4AbUiF5myQrI8ZRbq005RQUwIO-_MD4evv_JSHJPnA0CHGOWcUYytD-i_ZtPQgDBVNF7bpLN1IUr0JYOQTRYVd7OBr1RsR0WRaiBdRRRsqNVJawezrizbK21S1HX_KX8KRsCVmFGcjRzGi07PyqV1mK7AFU6v9oRATRZmAf37M5Z2PP2o5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز شنبه
۱۸ مهر ماه
۲۸ ربیع‌الثانی ‌۱۴۴۸
۱۰ اکتبر ۲۰۲۶
شنبه‌ها
#دعای_عهد
بخوانیم
⬅️
متن و صوت دعای عهد
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/697087" target="_blank">📅 08:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697086">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBye6L9aKpfyYmVUj26ARoYMT8zf1N2_qWg9_PYmpY8fZjl_cK55DljnXVwKYktEmiyP9yLsitHQUfySn3bNve-SXTFsXBQQnv3-sq5ZR0ojk-NilG00MlBHY5buS-fQ8Q_0J2lEL0g2yEF5zCHUIr0Zm6P6WP_oxaxik8XAJxiOo9UwuvsvP8gbBSSz7IwIdgLdZa2IDP3SrLwbyG1G5vvrrms97ucYaJH4bwION42iIJQm85HPn3KRBMPNNdEuUPb0tlSb4qyzqAIIf5C6fotsiaFST_pKzC3qsRs4Dn2BDbEO-CJ7F0aK9_PPqeFbGnFqCraoEhlsmPyhgY2_MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خبری‌که همه‌منتظرشنیدنش‌بودن
❌
پژوهشگران موفق شده اند ترکیبی را معرفى كنند كه مى تواند سلول هاى بنيادى فوليكول هاى مو را از
خواب چندساله بيدار كند
😳
😳
✅
این تحقیق روی ۱۰۰۰ نفر تست‌بالینی گرفته شده و نتایج فوق العاده در
قطع ریزش و رویش مجدد
داشته است
✅
🔴
حتی روی کسانی که ریزش‌ارثی هم داشتند اثرگذار بوده
رویش مجدد مو به همراه دارد
🧬
در حال حاضر در ایران این روش بالای ۳۰۰۰+ نفر رضایت‌درمانجو داشته
به زبان ساده، موهاى خاموش را دوباره زنده مى كند!
دریافت اطلاعات کامل و نحوه و هزینه درمان روی
لینک واتساپ بزنید
👇
https://wa.me/message/F4D4OKDJSSCFI1</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/akhbarefori/697086" target="_blank">📅 00:30 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697085">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nK9h3cXeElaUsF3s5wqv641CjLD1rHYCAEXx7eqVqMs2kD6xxtZrLou3KKb0GrosxjGygNW4lWFXcvNbXDrIVXQjGTe3noa3jno1u2mE-Qfjdn4_IpLTuREyVR8BdHXGsTmbSjy6bBIzzJ5tQLRusKJWoeH6-a_id4icgT5P5eP98lIBzTB5IX5xuIAfPZrdvCNhQGLYo-B0Guy6HZEpXFgqtWXYCyrNwCnwlbfHwNfvqZYdAxFD_-v9Xzz_AZuEKPqnvY_170g9Guvc7unA5h7_ticRBJ1D58JtXzTUQTTxaQ19SShsOsC0tG0tAuOnNLQkNo2EOcHlz4YHVXrCgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🪥
✨
تمیزی عمیق‌تر، لبخند جذاب‌تر!
با
مسواک برقی اولتراسونیک شیائومی X-3
، مراقبت از دندان‌هات رو یه قدم حرفه‌ای‌تر کن.
😍
⚡️
تکنولوژی اولتراسونیک برای پاکسازی بهتر
🦷
مناسب استفاده روزمره
🔋
شارژی و کاربردی
✨
انتخابی مناسب برای مراقبت از بهداشت دهان و دندان
🔥
قیمت ویژه: فقط ۹۹۸,۰۰۰ تومان
💳
الان بخر، بعداً پرداخت کن!
✅
امکان پرداخت
قسطی با ترب‌پی
🔄
ضمانت تعویض ۳ روزه
🪥
یه انتخاب کوچیک برای شروع یک عادت بهتر!
❤️
https://memarket24.ir/product/fast/63753/180124/</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/akhbarefori/697085" target="_blank">📅 00:30 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697084">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ff362a7ca.mp4?token=vzoTTzSM1vmlCyXSl7zJ96PubuQh1tTtgnFVUwXjHMYbc7-FKkOuier1p-tNG51dB8rRHMBe_bj6ThEOfmmrz5jiMvhRHe-ltMv4ijlszTBFG-SC3iKkGYIoLKsaMvSVClYxjw06N_d7JFENtHKtZNJKvcUwkANVLHG6nE9AWsKnZ6qb8BvhvH2UMIVuNH2vVILmRkPnz-4DjTXxWylo3Vi6aXjZDb4w81epvPnaebEdjxIhbdM8FNzQ9Smxur-8NI5ua_E5u3X8hcxSXjKwh5qXNxhddpi4xz8erKFbBoj-glK3cbJTBZ-dDWD4abENkDoMuySwwzQqX0XUu6Pl3DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ff362a7ca.mp4?token=vzoTTzSM1vmlCyXSl7zJ96PubuQh1tTtgnFVUwXjHMYbc7-FKkOuier1p-tNG51dB8rRHMBe_bj6ThEOfmmrz5jiMvhRHe-ltMv4ijlszTBFG-SC3iKkGYIoLKsaMvSVClYxjw06N_d7JFENtHKtZNJKvcUwkANVLHG6nE9AWsKnZ6qb8BvhvH2UMIVuNH2vVILmRkPnz-4DjTXxWylo3Vi6aXjZDb4w81epvPnaebEdjxIhbdM8FNzQ9Smxur-8NI5ua_E5u3X8hcxSXjKwh5qXNxhddpi4xz8erKFbBoj-glK3cbJTBZ-dDWD4abENkDoMuySwwzQqX0XUu6Pl3DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطور روی فلش رمز بذاریم و از فایل‌هامون محافظت کنیم؟
👨‍💻
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/akhbarefori/697084" target="_blank">📅 00:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697083">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
بیرانوند ممنوع‌الخروج شد
🔹
سازمان نظام‌وظیفه اعلام کرد تا زمان مشخص‌شدن وضعیت کمیسیون پزشکی علیرضا بیرانوند، او حق خروج از کشور را ندارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/akhbarefori/697083" target="_blank">📅 00:16 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697082">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b0c0dc628.mp4?token=ZGxrAc95oU4lqMSR0eAbkpQR0hgnhRxRKCFza_uesLv43KDhUrUpF6JTGG8XXNIQoAisprAYd-hHhFF9H2QCk5_gXi2ani5J-70mkDge5yzYYdXPa21hy4M8v3V0bhbn4gDlZTOzkTyqQEPVquEVc-lepx4XMY_7J1abwvsU94wNPom56P0TmT01g33Xup_C2T9avewSLIR6tSrUXp3CKijSCnVwwHSThMTIYnb9WSY2_LWVcfJOqhTTJNNV4qCPrOoCvOgDZ52EhLN_R1TbqGblaU3M8BbULHEGBp5xdokGWkzaBcJg1hqrhm72JdZuiJ_-_uR7SyUarDSiCi4FoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b0c0dc628.mp4?token=ZGxrAc95oU4lqMSR0eAbkpQR0hgnhRxRKCFza_uesLv43KDhUrUpF6JTGG8XXNIQoAisprAYd-hHhFF9H2QCk5_gXi2ani5J-70mkDge5yzYYdXPa21hy4M8v3V0bhbn4gDlZTOzkTyqQEPVquEVc-lepx4XMY_7J1abwvsU94wNPom56P0TmT01g33Xup_C2T9avewSLIR6tSrUXp3CKijSCnVwwHSThMTIYnb9WSY2_LWVcfJOqhTTJNNV4qCPrOoCvOgDZ52EhLN_R1TbqGblaU3M8BbULHEGBp5xdokGWkzaBcJg1hqrhm72JdZuiJ_-_uR7SyUarDSiCi4FoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زلزله ۷.۵ ریشتری پاناما را لرزاند؛ آمریکا هشدار سونامی صادر کرد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/akhbarefori/697082" target="_blank">📅 00:08 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697081">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d10cb6c5bc.mp4?token=vPrbdogxbMyyFUFhekrvngxlneHQonwz_u9muVNcA3KCy3QMevolXy56zTNf50YgA6SZ-kNDcMgSHPZ7sbDyE8NZmBuakOt1RJLKA9QmAqA9gI1YkgTx1jpbXTP4AshdJVPlhWkUdy7Mp3punSlq4_xZYkkL2W--9koEac3h_8EpHuceMCxXpLx_if8bTUOeq1XjpVjSyExCynRnKPDLlX3XYh3MPinPYl73L7OsRJfvqhRMCIZJnU4tUx2KHeTZxHG0oNzR26GYpMGKNnxVl3mmf2MtCKeHHs904mYcJJnlo8sO_mrkjcfj_6g3pPvifVdND3X-pCwP7UGmDk3TIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d10cb6c5bc.mp4?token=vPrbdogxbMyyFUFhekrvngxlneHQonwz_u9muVNcA3KCy3QMevolXy56zTNf50YgA6SZ-kNDcMgSHPZ7sbDyE8NZmBuakOt1RJLKA9QmAqA9gI1YkgTx1jpbXTP4AshdJVPlhWkUdy7Mp3punSlq4_xZYkkL2W--9koEac3h_8EpHuceMCxXpLx_if8bTUOeq1XjpVjSyExCynRnKPDLlX3XYh3MPinPYl73L7OsRJfvqhRMCIZJnU4tUx2KHeTZxHG0oNzR26GYpMGKNnxVl3mmf2MtCKeHHs904mYcJJnlo8sO_mrkjcfj_6g3pPvifVdND3X-pCwP7UGmDk3TIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عشق یا خودآزاری؟
🔹
با نوشیدنی داغ عشقتو ثابت کن؛ ترند جدید و عجیب این روزهای فضای مجازی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/697081" target="_blank">📅 00:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697080">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXaHrPfQxFDxN19tIJwZP2N7ajtsHclQzOzaBXtnX-9oF1MKTDKSTVwgb3oonOLvTjXxC4sv40heThrrYnr6VWo9vC28RAFFrLyZg9b8_tnNPOCUHzjIDNIQ0fPAPq2Bcjcf1nVLCdJTAFQ4PYeXHM-aUFVIm8ANEtdaQ58IpXUNDSFbWbV55XqagQYD8K3JRoSf9xV5BzJOsmk5AoyHZ2bJ-uRzs5EhJ3MjK1SEfLEz71X1IGWwaLU3bm_serxfNijcN0QFrvsfbcrASUzGKlRqSFHXlloycBc8K86NzV0vwDk9vAUI57137jkHlm9r7qrw30td1vbN-J4hIE_eWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/697080" target="_blank">📅 00:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697079">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30d5944c25.mp4?token=sox8BZaF08LX0X6x2TUdLvoTgSXdKNZLzxJG4G6GnQGkKsYqU2ncuJnvokLrr_0aGxP28iGHZvo8DL7aUkjtz-Z6km9TG578s7J_YdUd25EMoucJff_exFUeNIXgub0Slf0buIOPx_yH9PiJW9dUkVbYcOLADmp7z9245QUZr-5sVRAwd-0E_DHjERvpq815Dam7Ss6pBY0lBnUXXLOxxAfREqKlxuaDSWqZJZKbpWw3mNMIgqfqEVUHn5FPGgRziGCFK6VLicPqRcwYlOeFAIbPvwtwb5wXaQTsNpIZoy4nfVK17eXowwR1TCUX4w1DH3dU2bHSxPbookCGHPPy-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30d5944c25.mp4?token=sox8BZaF08LX0X6x2TUdLvoTgSXdKNZLzxJG4G6GnQGkKsYqU2ncuJnvokLrr_0aGxP28iGHZvo8DL7aUkjtz-Z6km9TG578s7J_YdUd25EMoucJff_exFUeNIXgub0Slf0buIOPx_yH9PiJW9dUkVbYcOLADmp7z9245QUZr-5sVRAwd-0E_DHjERvpq815Dam7Ss6pBY0lBnUXXLOxxAfREqKlxuaDSWqZJZKbpWw3mNMIgqfqEVUHn5FPGgRziGCFK6VLicPqRcwYlOeFAIbPvwtwb5wXaQTsNpIZoy4nfVK17eXowwR1TCUX4w1DH3dU2bHSxPbookCGHPPy-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زارع پور، وزیر پیشین ارتباطات: در کشورهای پیشرفته دنیا برای کپی کردن پهپادهای ایرانی صف کشیدند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/697079" target="_blank">📅 23:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697078">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
از داغ‌ترین خبرهای امروز غافل نمانید
🔹
🔹
جزئیات پیشنهاد پنتاگون برای عملیات نظامی علیه ایران
👇
khabarfoori.com/fa/tiny/news-3250968
🔹
چرا ترامپ می‌گوید پیش از انتخابات به ایران حمله نمی‌کند؟
👇
khabarfoori.com/fa/tiny/news-3251122
🔹
زمین چابهار برای افغانستان! | چه کسی اختیار واگذاری ۱۱۰ هکتار زمین را به نماینده مجلس داده است؟
👇
khabarfoori.com/fa/tiny/news-3250958
🔹
وداع با گوشی | موج عجیب گرانی موبایل‌های میان‌رده‌ تا کجا ادامه دارد؟
👇
khabarfoori.com/fa/tiny/news-3251075
🔹
جنجال عکس یادگاری در تولد پوتین | صدراعظم باید اخراج شود!
👇
khabarfoori.com/fa/tiny/news-3251125
🔹
صفحه ویژه پربازدیدها را اینجا کلیک‌ کنید
🔹
khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/697078" target="_blank">📅 23:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697077">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
خبرنگار ارشد دفاعی کی‌یف‌پست: ما در طول روز فقط سه ساعت برق داریم؛ روسیه زیرساخت‌های حیاتی اوکراین را هدف قرار داده/ وضعیتی که با نزدیک شدن زمستان، نگران‌کننده‌تر خواهد شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/697077" target="_blank">📅 23:39 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697076">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
ادعای
بسنت: دولت آمریکا در حال رایزنی با پاکستان و ترکیه برای بستن تمام مسیرهای زمینی ورود و خروج از ایران است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/697076" target="_blank">📅 23:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697075">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5287688d95.mp4?token=g8LznVVEv4NHZpMFjVP4Bce5BaZSDck_ft4W8HLerdsfCjnYjbEVOxlCDNxBLZqK1xkQkVzdNamj4i80iPuH378OH_OaMo95PTr4a2uSguTLQpRKeRzm98Uja3CtIA_cMmqtMmk2Aun5zxqoz66Vso_q9pyUiN4IZiSic8xwtAaE0CZMUuYyxr9WR5g4WI4-Vq6z9nce5mn5NQmkXwZ8PewcOZ3KgM6CYrg4TXwT3xkFKAsdk9jC--epHf2lMjfWDC-yombGF_1rkdBQdy55RxMRRNjaaqZjjjIHc2sICgdXB0COuqzfRwnEc0XZ0Mb8scNBV1mDqEfExPV59LKQMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5287688d95.mp4?token=g8LznVVEv4NHZpMFjVP4Bce5BaZSDck_ft4W8HLerdsfCjnYjbEVOxlCDNxBLZqK1xkQkVzdNamj4i80iPuH378OH_OaMo95PTr4a2uSguTLQpRKeRzm98Uja3CtIA_cMmqtMmk2Aun5zxqoz66Vso_q9pyUiN4IZiSic8xwtAaE0CZMUuYyxr9WR5g4WI4-Vq6z9nce5mn5NQmkXwZ8PewcOZ3KgM6CYrg4TXwT3xkFKAsdk9jC--epHf2lMjfWDC-yombGF_1rkdBQdy55RxMRRNjaaqZjjjIHc2sICgdXB0COuqzfRwnEc0XZ0Mb8scNBV1mDqEfExPV59LKQMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گرافیتی این توهم را ایجاد می‌کند که خانه محدب و برآمده به نظر می‌رسد
🏢
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/697075" target="_blank">📅 23:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697074">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
پوتین: روسیه آمادگی خود را برای تأمین نفت و فرآورده‌های نفتی مورد نیاز بازارهای آمریکا و سراسر جهان اعلام می‌کند
🔹
این درحالیست‌ که نیمی از پالایشگاه های روسیه از کار افتاده‌اند و در خود روسیه دیزل و بنزین حکم طلا را دارد و کمبود وحشتناک آن در شهرهای مختلف…</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/697074" target="_blank">📅 23:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697073">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
وزارت خزانه‌داری امریکا مجوز موقت انجام معاملاتی را صادر کرده که شامل فروش، تحویل، تخلیه و واردات گازوییل از روسیه تا تاریخ ۷ آوریل ۲۰۲۷ می‌شود
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/697073" target="_blank">📅 23:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697072">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04f0886b31.mp4?token=F5PR5rdHCNkXeh021oprXPDzEsESmicv7yKetWAEV_xeNp3QML_qytmBWcG6-52HDgtRhoh3q5H9ma_jKPlRcU8IWSmRBRrY9FB5lceYSQdez54Y5-OALuUf4zpmaqMHcwukNK6MCNdEwLsh4oboS5vPMObZ3o6Ela6Yg1UKIfl-bZdY0Bh7fPCrzs8doWEXhRVdE6bGF-htVwzDy2SagAlJWxRqXfcfjUP8Q8Mw2AsVtpNoUZfz2HrH-a3duUYfsjZvRGAATLdUEsO0pshJlX0ndtYtk4REtHSp0VwJ1XMmTFOoq5dGhabqM_Xw-H685FRWzl9V6dvKy6qb0c7vbalW_0KWEOLWx30hSRVgHqcozOkJ1uecz6lz3wd1nwx1mPjY-8PsXs03qEjdh0vnwp7zqaBem7rBnsKUaKTCWVbYTBRmYfsz3dwwB0DiqjUbwAwpu81d1mFOhZmUCVSqRS2y4N9fgrSC5PXdOu-X9qRZlNIIPkH6Gynvsm8Ie618KbsBmCYdwUduk90ZMrZq-nzRskxm7Uir6nvpBWRDL3IQjpoGaD-I5yEQJxfdziO2ONov8m4Nu-lNTg0cGLO8R-3xPb7VJQWo38Xz4KvO-kIpq6AJklQPVHtg4jg-GdTy7ExgqaB_euQPkXldOjjOz-PugMbPvDB2daYuHeQowOo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04f0886b31.mp4?token=F5PR5rdHCNkXeh021oprXPDzEsESmicv7yKetWAEV_xeNp3QML_qytmBWcG6-52HDgtRhoh3q5H9ma_jKPlRcU8IWSmRBRrY9FB5lceYSQdez54Y5-OALuUf4zpmaqMHcwukNK6MCNdEwLsh4oboS5vPMObZ3o6Ela6Yg1UKIfl-bZdY0Bh7fPCrzs8doWEXhRVdE6bGF-htVwzDy2SagAlJWxRqXfcfjUP8Q8Mw2AsVtpNoUZfz2HrH-a3duUYfsjZvRGAATLdUEsO0pshJlX0ndtYtk4REtHSp0VwJ1XMmTFOoq5dGhabqM_Xw-H685FRWzl9V6dvKy6qb0c7vbalW_0KWEOLWx30hSRVgHqcozOkJ1uecz6lz3wd1nwx1mPjY-8PsXs03qEjdh0vnwp7zqaBem7rBnsKUaKTCWVbYTBRmYfsz3dwwB0DiqjUbwAwpu81d1mFOhZmUCVSqRS2y4N9fgrSC5PXdOu-X9qRZlNIIPkH6Gynvsm8Ie618KbsBmCYdwUduk90ZMrZq-nzRskxm7Uir6nvpBWRDL3IQjpoGaD-I5yEQJxfdziO2ONov8m4Nu-lNTg0cGLO8R-3xPb7VJQWo38Xz4KvO-kIpq6AJklQPVHtg4jg-GdTy7ExgqaB_euQPkXldOjjOz-PugMbPvDB2daYuHeQowOo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارشناس مسائل غرب آسیا در شبکه سه: ترکیه قصد ورود به جنگ یمن را ندارد و نقش احتمالی پاکستان نیز به دفاع از خاک عربستان محدود می‌شود/ تاکنون هیچ‌یک از این دو کشور برای جنگ با انصارالله اقدام عملیاتی نکرده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/697072" target="_blank">📅 23:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697071">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hV_Tt14JyvG1FpOXrRgdTJpenM5qoc6R4JWYA8qNkf_aIpel9jcmYmcDSc1ZftTV23aDJOcYb0lU8ju0pXNENOR2CjZyUoGzDSwpH37hL7lTIiQi_9DT3u1xbQZXB1Y7jkawDeyz8qKMQ8XxdmcfLrLRHwdhCqT04Mi7fLU7S4RuTmhLkeQKkS6D6plg_3sMY-SR1VBPemxAeI1rnn0ETnVn8rRkWY7hTu5q-cxbYepcBawXIRQaQHa3LbwDUoEBKIROZbS1FI7cx7jBgJYA8hj9EnEu5A_V37iIMWZjM4GBE5Vyud3OXDEdC-oFmgT0n7BFypTleCPcehcUkPfeng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اطلاعیه نهاد آبراه خلیح فارس در مورد وجود دامنه‌های جعلی
نهاد مدیریت آبراه خلیج فارس:
🔹
با توجه به برخی گزارش‌ها مبنی بر سوءاستفاده با دامنه‌های جعلی، تاکید می‌شود کلیه مکاتبات پی‌جی‌اس‌ای از طریق ایمیل و با دامنه
PGSA.ir
صورت می‌گیرد و سایر دامنه‌ها فاقد اعتبار است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/697071" target="_blank">📅 23:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697070">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFN6m5f_jelQw1GyRaVEfe9cSLqiE2lV1OIXT0ZVUTySnou9jvQNr5A7OOJ_2KAlQhrMD8LAeWHs-4EooDHW9V_iTfIzS6RXp96idJxDvksEwZD5OWKjHeETtYMenEzreOsHGW7zj29_E3jNo2IEzKl7mscaOmADrpnunNJ_2CQYPnDdLiZZ77sMPBqOqeP9Fc5Qgs4ZJYQ_5bPhFc6yOKOIrXuGMU4jlyNKbBhci8llcFeEk5f7umjtreEgOm8iF_T3IX8r3NfpbGTiCOFAT5Lj7AAiPm11-pNON1vM2VkdHrUg58mGBW2oa-I_HMta_vVq5HgLmbBdOBw0M23iSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ولی نصر، مشاور سابق اوباما: به‌نظر می‌رسد روبیو در حال طرح نسخهٔ دوم نظریهٔ «برخورد تمدن‌ها» ساموئل هانتینگتون است
🔹
با این تفاوت که به‌جای تقابل اسلام و غرب، این بار از تقابل تمدنی میان ایران و غرب سخن می‌گوید.
🔹
پ.ن: هانتینگتون معتقد بود پس از پایان جنگ سرد، مهم‌ترین خطوط اختلاف و درگیری در جهان به‌تدریج از رقابت میان ایدئولوژی‌ها و نظام‌های اقتصادی به اختلاف میان تمدن‌ها، به‌ویژه تفاوت‌های فرهنگی و مذهبی، منتقل خواهد شد.
﻿
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/697070" target="_blank">📅 23:26 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697068">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
تاج رقم قرارداد قلعه‌نویی را اعلام کرد!
رئیس فدراسیون فوتبال:
🔹
قرارداد قلعه‌نویی تا جام جهانی سالانه ۳۰ میلیارد بود که الان سالانه ۵۰ میلیارد در نظر گرفته‌ایم‌. عدد ۹۰ میلیارد برای جام ملت‌ها را رد می‌کنم‌.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/697068" target="_blank">📅 23:21 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697067">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60b9bc7145.mp4?token=DEbEJ7DIvC7CdAqKCX7Dpg6ix_KqP0UxJG1uCNwU0xihVINjBNG366OM-10NaQYeDECqZjheoxrZqDpc8k8qJZTAGQuSF8YUuKZhRFc5nnl7OwwXBOPW9eg6ENkcegDckBjcNC9E4JySsd0EYMxAtE9dWtYKm1knrQx29bFDRuZJDxi2afsHh5mzxuxpjdSvC1gGUhR8PNuIOp_eUuNuBdLn4if5lQ-UIErUNk6fkNHdTu84cvg7GfdpzTKuRNl-A0AGKXS-MU68fJOOfmRlVr7cD80FJqSlGhLHTJU7o82pNXvR5INHgN-M22Nz6DBKuuQ-G5oiljgFUtNe1K0Eng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60b9bc7145.mp4?token=DEbEJ7DIvC7CdAqKCX7Dpg6ix_KqP0UxJG1uCNwU0xihVINjBNG366OM-10NaQYeDECqZjheoxrZqDpc8k8qJZTAGQuSF8YUuKZhRFc5nnl7OwwXBOPW9eg6ENkcegDckBjcNC9E4JySsd0EYMxAtE9dWtYKm1knrQx29bFDRuZJDxi2afsHh5mzxuxpjdSvC1gGUhR8PNuIOp_eUuNuBdLn4if5lQ-UIErUNk6fkNHdTu84cvg7GfdpzTKuRNl-A0AGKXS-MU68fJOOfmRlVr7cD80FJqSlGhLHTJU7o82pNXvR5INHgN-M22Nz6DBKuuQ-G5oiljgFUtNe1K0Eng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش‌ها از وقوع حادثه در تأسیسات نفتی بقیق عربستان حکایت دارد؛ تصاویری از روشن‌ماندن مشعل‌های نفتی برای بیش از ۲۴ ساعت منتشر شده است.
🔹
بقیق از بزرگ‌ترین مراکز فرآورش نفت خام جهان و تأسیسات راهبردی صادرات نفت عربستان است.
🔹
یک کارگر خارجی مدعی شده این…</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/697067" target="_blank">📅 23:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697066">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_Ma6tUwZVhFksEnqjaRjhdNxkt5rLuc06DTB-9hyZNJg1MIafwDV3h9aw9iUB_-2VGARyj-Jnwum2sT_CBmt5JBUIJxe_vzaARSkGN44KaEW0DWePHcjnxgbRw5TCzI1RfDPCy9q9IGOLOilrmTI7dUn9nhL4OQO2EhZuPeEd7dk9qqrN8z9tzLvRkeGAFBVt1TV58uqA3wA7WbchqWX1d7EuFKD1j0M_bfPTa7Uhf1gE0k3_GEGPxkxyiAaoE8FUL3Ry5LWS8EWInaz6I7mn_BQijXDC1R6bNVOo83mSrLwXk6M2BydjRqZ4uYL6s9ekEo-idgUtpGwYx7Dt8acA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ویدیوی انتقاد آیت‌الله مروی به قوه قضاییه قدیمی است
🔹
واکنش مدیرعامل خبرگزاری میزان به بازنشر فیلم قدیمی از آیت الله مروی و حمله به قوه قضاییه: دروغگویی برکت ندارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/697066" target="_blank">📅 23:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697065">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTprJpcdfDOCIcWL5K2OsyPSFrjuPl32mZFXA-2Nx96UwBKXAfmLoQ6xxmmWe1BBAKW4CpM8Delr_CHYcfIxctR88JWzXSNPocwBGnDEtqV0TDio3_kXxsZuLhnxoME6pn7tK3_S5kx38_5U-pd05SHZNtZAL3qTAQnzE2gNzS4ylyFsV193fsQoIg_BHgjYljojIyRPNA22-XQEx7LwiKAHYV4YsYb85PvkRK_YKvQAJsyIuPBMGzjtR2GZ75TyMbpRRUcljUyxsTm2VlUkoIiQp6obMku5l8f84iSrcNepg8DNCS3MPXHDnsIqbak_AVa6bwjk__zKcXUsbxYvgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سپاه: کشتی غول پیکر حامل گاز ال پی جی مورد اصابت قرار گرفت و دچار آتش سوزی شد؛ مسئولیت تنش افزایی در حمل و نقل دریایی منطقه بر عهده ارتش متجاوز آمریکاست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/697065" target="_blank">📅 23:12 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697064">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZwlgHJ09E3SUuZY0D93SZfVaaAUuXzcGeqf9f3Xwz9_RXfkWqDv__t3Drm-de6Cd3e8OnxxpD2mXreHu-E014rYPuAesZ00pwIJ6MBdiWoKzAbI86uqVYeW8pV_Tt-1m_-EfX4ZZlFS8VgT8AdoWACz1RsWjDkcw6sXGt5MWykLt_nCSFJR5WqoGjrh_MTV0n89B_Y9sR7VJw_1UxJwgq9mG8aQhHvpVCf1UDxFMhVTeEt3WA8ThtD6Yc90_Nt3iDxZk3ksqP-7KqW6ob5Sl0JQSKKGAZh12shyuFdmX7z-0mzITudxsSSphHIiI0AK_rJu9QlzG30pt4r5BaPi6lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزارش‌ها از وقوع حادثه در تأسیسات نفتی بقیق عربستان حکایت دارد؛ تصاویری از روشن‌ماندن مشعل‌های نفتی برای بیش از ۲۴ ساعت منتشر شده است.
🔹
بقیق از بزرگ‌ترین مراکز فرآورش نفت خام جهان و تأسیسات راهبردی صادرات نفت عربستان است.
🔹
یک کارگر خارجی مدعی شده این تأسیسات هدف حملات پهپادی و موشکی انصارالله یمن قرار گرفته و فعالیت‌ها متوقف شده است؛ این ادعاها هنوز تأیید مستقل نشده‌اند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/697064" target="_blank">📅 23:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697063">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">صد میدان10-میدان دهم تهذیب</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/697063" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
شرح کتاب صد میدان خواجه عبدالله انصاری
🔹
میدان دهم، تهذیب
🔹
تهذیب به معنای پاک کردن پلیدی، ناپاکی و شر از هر چیز می‌باشد.
🔹
در حیطه‌ نفس بشر خودبه‌خود مایل به انجام کارهای خیر نیست و گرایش وی به متضاد آنها بیشتر است.
حلیت‌ها بدین شکل هستند:
🔹
نفس را با سنت: از شکایت به مدح گراییدن/ از گزاف به هوشیاری گراییدن/ از غفلت به بیداری گراییدن
🔹
خوی را با صحبت: از زجرت به صبر آیی/ از بخل به بذل آیی/ از مکافات به عفو آیی
🔹
دل را با خلوت: از هلاک امن به حیات ترس آمدن/ از شومی نومیدی به برکت امید آمدن/ از محنت پراکندگی دل به آزادی دل آمدن
#صد_میدان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/697063" target="_blank">📅 23:08 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697061">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
کالا ۲ روزه رسید؛ اما ماه‌هاست که گیر کرده!
🐼
🐻
محموله‌ای که از آن‌سوی دنیا رسیده، چرا هنوز به دست صاحبش نرسیده؟!
📦
وقتی گمرک از مسیر تجارت طولانی‌تر می‌شود!
🎬
این انیمیشن طنز و تماشایی را از دست ندهید؛ داستانی که برای خیلی از تجار ایرانی آشناست!
🔻
ماجراهای راه ابریشم | قسمت سوم
📺
تولید جدید TOOSA Animation
🔗
https://t.me/toosaanimation</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/697061" target="_blank">📅 23:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697060">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4921ce8ad.mp4?token=HYb7pAg9ZeI_npbdyPxAzMaNhgMajwuTiE7k6yPe4gWaSH86yEevJX_AmqyrmSkMlYDOnoii9LYIdmzYC8EtN3b-_EaHftqItT5HKtylu1DbNiYmjHJMnEvn0eNCGT7sVyLlLhZuf1CcWScPNp8-MUvoRnnjXtFamX9TSL2CHvabP00km6bI0ATa10lGAV49Hd8K-4SLx-JKRNmtqOD-kS-PC1ZnIyctJ1pPRpP9l6vP_8IVyaOkrxsrUmH3X-RrPSoRuUiflgN3oWgrtLP46XlnAPRXMe4ccuWssXmhvQhyzfNkQEN7FegECuKFx44bQfvQjGqxm--3bfU5qFop1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4921ce8ad.mp4?token=HYb7pAg9ZeI_npbdyPxAzMaNhgMajwuTiE7k6yPe4gWaSH86yEevJX_AmqyrmSkMlYDOnoii9LYIdmzYC8EtN3b-_EaHftqItT5HKtylu1DbNiYmjHJMnEvn0eNCGT7sVyLlLhZuf1CcWScPNp8-MUvoRnnjXtFamX9TSL2CHvabP00km6bI0ATa10lGAV49Hd8K-4SLx-JKRNmtqOD-kS-PC1ZnIyctJ1pPRpP9l6vP_8IVyaOkrxsrUmH3X-RrPSoRuUiflgN3oWgrtLP46XlnAPRXMe4ccuWssXmhvQhyzfNkQEN7FegECuKFx44bQfvQjGqxm--3bfU5qFop1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔧
دیگه برای هر کار کوچیکی دنبال تعمیرکار نگرد!
🔥
این دریل رو می‌خوای؟ قسطی هم می‌تونی بخری!
دریل و پیچ‌گوشتی شارژی ۴۷ تکه
؛ همه ابزارهای ضروری رو یکجا داشته باش!
💪
✅
موتور قدرتمند و شارژی/ مناسب باز و بسته کردن انواع پیچ
✅
ایده‌آل برای سوراخ‌کاری چوب، پلاستیک و فلزات سبک
✅
همراه با
۴۷ قطعه کاربردی
✅
سبک، خوش‌دست و قابل حمل
🔥
قیمت قبل:
۲,۲۹۸,۰۰۰ تومان
💥
قیمت ویژه: ۱,۹۹۸,۰۰۰ تومان
✅
امکان پرداخت قسطی با ترب پی
👇
برای سفارش و مشاهده جزئیات، روی لینک زیر کلیک کنید.
https://memarket24.ir/product/fast/46482/180124/</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/697060" target="_blank">📅 23:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697059">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUogCDQYTFTsLnVYDX3gT6FeT9-LE7EqIMYaAmevIWmI6AdX2Cub2T55zXOQoCp5MIh46a45ifmTk6cBXrmUiWcAb2qw-Ep1NpadzEXalsA2TRsFaUpH4QwDlvJdu5ChRCGBzdO0FCQk8IexKhuCf1tfoR2oa-OHFgWlJts7Re9x0G-ShIa9Gt4PEHayIss1sAhfEtvelEAhNEb-2rdYts8iynn7AXuXFyk1QwJvanl7aVFyvInbHe_9lzOAQHXKvfTM3xbz0MQvEZCk7SAuQytF9b1YYqfv6Vuyx5wpuVrvzyhKbDL32Q5Y8Hh-2HiTkIXn-VY8BHybjA0YcNUQtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ترامپ: با پوتین توافق کردم/ توافق شد که روسیه فوراً بیش از ۳۰۰ هزار تن گازوئیل به بازار آمریکا و جهان عرضه کند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/697059" target="_blank">📅 23:01 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697058">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
ضرغامی: پخش خطبه‌های نماز جمعه از اشتباهات من بود!
🔹
برخی خطبه‌های نماز جمعه ارزش شنیدن ندارد و باعث گمراهی مردم می‌شود.
🔹
پیغمبر و حضرت خدیجه خودشان هم در شعب ابی‌طالب زندگی کردند اما اینجا مسئول جمهوری اسلامی در شمال تهران زندگی می‌کند و به مردم توصیه زندگی در شعب ابی‌طالب دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/697058" target="_blank">📅 22:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697057">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iB__BA5LXmYdYgKYlGDYO2-tURHIjGwhHdiujw23Yp4mQbE0mAPYiKRlf-bl44W7CzWFNijPNcCS3NBZ1bi67aefA99DX80rohKh0Tyq9ObmIkNlzbBGumBIXnp-3iO5rV6vWrABAiJTLcmiOP_t9rn2a39lf_f1fHBIm21qn39W34BnTnEd7OBrS_QfAd7KYsbrfe7AAGYnCezKQMyEUrW_qc8KJCfqd4OdMHplKtRV2oij4BuP3PT_UvQ49ltA7lmxCfzf2q1zKeXUS9arOQCmzehyC8DrAUeEE92XiqZgkpfjKQYAVE7WTmDMD5No_u2YWk69yaERv906gCLD0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ترامپ: با پوتین توافق کردم/ توافق شد که روسیه فوراً بیش از ۳۰۰ هزار تن گازوئیل به بازار آمریکا و جهان عرضه کند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/697057" target="_blank">📅 22:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697056">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
در هزینه‌های دولت اسراف عظیمی وجود دارد
مصطفی میرسلیم، عضو مجمع تشخیص مصلحت نظام در
#گفتگو
با خبرفوری:
🔹
۳میلیون کارمند دولتی داریم که با کارمندان شرکتی تعداد آنها به ۴ میلیون نفر می‌رسد.
🔹
۸۰ درصد بودجه کشور برای حقوق و مزایا به این افراد تعلق می‌گیرد.
🔹
معادل کشور ما با ۳۰۰ هزار کارمند دولت خود را می‌گرداند و ما با ۳ میلیون کارمند این کار را میکنیم.
🔹
مابقی فقط حقوق می‌گیرند و پشت میزشان روزنامه می‌خوانند. در هزینه‌های دولت اصراف عظیمی وجود دارد.
🔹
همان پولی را که دولت باید خرج رفاه شما کند، از جیبتان برمیدارد و خرج بنزین می‌کند.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/697056" target="_blank">📅 22:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697055">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87787c9aa2.mp4?token=UeAHZ73vrrq6TyTO7YZtjPPUapxHhhVE1zxOr34JBPbOkbNbfPN3PX-DUBiI5raRuFlV6eWyEYJi2rTCE__zsBn7ZBZJ62JlAsUkQ3w0ryA_M4oozF_HCYNu-IJTVqmT5zdYYalk0E_dfPrFa9SPKGAONbcJeufBJSnR5TO_YvOqQOKccLZrzQhahvaOt5CTNcLuV2AkiNgLkLkyVGu_YwpLxOar_JQR_Wr4kI1psH94exB4ngSTWZC_ZN4VrQSR3gYlkTW1dZwVIzWR2sZhARHCwU20xsbox1cISmSi4FUZEKGs8Y6CjN1BO5ehycxCUwimcwfZxww6kRvxu-PN3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87787c9aa2.mp4?token=UeAHZ73vrrq6TyTO7YZtjPPUapxHhhVE1zxOr34JBPbOkbNbfPN3PX-DUBiI5raRuFlV6eWyEYJi2rTCE__zsBn7ZBZJ62JlAsUkQ3w0ryA_M4oozF_HCYNu-IJTVqmT5zdYYalk0E_dfPrFa9SPKGAONbcJeufBJSnR5TO_YvOqQOKccLZrzQhahvaOt5CTNcLuV2AkiNgLkLkyVGu_YwpLxOar_JQR_Wr4kI1psH94exB4ngSTWZC_ZN4VrQSR3gYlkTW1dZwVIzWR2sZhARHCwU20xsbox1cISmSi4FUZEKGs8Y6CjN1BO5ehycxCUwimcwfZxww6kRvxu-PN3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهارت خیره‌کننده دختر ایرانی در باز و بسته کردن سلاح
در حاشیه آموزش‌های نظامی جان‌فدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/697055" target="_blank">📅 22:53 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697054">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
هرکسی ایران را دوست دارد اول صحبت‌های وزیر خارجه آمریکا را بشنود!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/akhbarefori/697054" target="_blank">📅 22:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697053">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85bf58452a.mp4?token=P17mbBno9cRP2nZoUQ-Lw9kWrgs873TjGEk_GY2-86oy50yESgr9BCUFK2OKReP1vrUZv0YqiY-_HEWkjdwmGK5t6eTYn7d2OJ409-nkBiRN8miKiK-gVx8ju6FScfkFRJcLAxM2AMbXjSOtL8DhVvy5o5bwwYfwxRLNekoGXS4FC7PUdZfLqi0rrejmnQXRVIyQ-vEEAr16JTxJ2ybOMpgrQvE2zjGpSl13lnt0OfYXWivjFbMcnUXPq1Vmob0exPhqR7DtQW6ymr22MfVRiLKrWvdhhNBpxItaMek8379Tcywcv2rndaDoJBAZu8-YLDA5co6GqYlZ-DXsKNEiMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85bf58452a.mp4?token=P17mbBno9cRP2nZoUQ-Lw9kWrgs873TjGEk_GY2-86oy50yESgr9BCUFK2OKReP1vrUZv0YqiY-_HEWkjdwmGK5t6eTYn7d2OJ409-nkBiRN8miKiK-gVx8ju6FScfkFRJcLAxM2AMbXjSOtL8DhVvy5o5bwwYfwxRLNekoGXS4FC7PUdZfLqi0rrejmnQXRVIyQ-vEEAr16JTxJ2ybOMpgrQvE2zjGpSl13lnt0OfYXWivjFbMcnUXPq1Vmob0exPhqR7DtQW6ymr22MfVRiLKrWvdhhNBpxItaMek8379Tcywcv2rndaDoJBAZu8-YLDA5co6GqYlZ-DXsKNEiMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تانکرهای نفت عراقی در داخل خاک سوریه هدف حمله قرار گرفتند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/697053" target="_blank">📅 22:50 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697052">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
ضرغامی: من اجازه ندادم میرحسین موسوی در سال ۸۸ در پخش زنده با مردم حرف بزند/ سعید جلیلی به این ماجرا ارتباطی ندارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/697052" target="_blank">📅 22:49 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697051">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e67bbba26.mp4?token=rGlWTOyXEHdtSqPGhyjK6u1OMxVIaBwfaDCvdfPbtzmpFC_mz12sCxjhpzoBLmHVC_-sjA58Nql9I93D563rhkNxF__eN68KcG42moUOs7MHk97Y6rdnZaVrFA1OrhnM_hBkL8q4c0-KVz2gIro0BH1z2QYOLSvtfJ_4id5HeYM9IYg9ETcQCKFTN38O2RGTVVP3mURP4QqcbSH-pFmrwsYt6u-jCw0gWWPmkVcexKFGvjjYLdAYC6GcNE9-FqzOi8SbJRgQ5RtvdFeKBJHO5562nd60ktYwc7-Lg71n33SrGCl0BThhf13f_H8tmvd3zO_woa3QJHtYrCYJSUgYog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e67bbba26.mp4?token=rGlWTOyXEHdtSqPGhyjK6u1OMxVIaBwfaDCvdfPbtzmpFC_mz12sCxjhpzoBLmHVC_-sjA58Nql9I93D563rhkNxF__eN68KcG42moUOs7MHk97Y6rdnZaVrFA1OrhnM_hBkL8q4c0-KVz2gIro0BH1z2QYOLSvtfJ_4id5HeYM9IYg9ETcQCKFTN38O2RGTVVP3mURP4QqcbSH-pFmrwsYt6u-jCw0gWWPmkVcexKFGvjjYLdAYC6GcNE9-FqzOi8SbJRgQ5RtvdFeKBJHO5562nd60ktYwc7-Lg71n33SrGCl0BThhf13f_H8tmvd3zO_woa3QJHtYrCYJSUgYog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حق با شما بود؛ آنها فقط با جمهوری اسلامی مخالف نیستند، آنها با ایران مخالفند...</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/697051" target="_blank">📅 22:47 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697050">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f3c4bb53.mp4?token=PUtBpY98fSlBVlWfHGJR1XbDiNDuSx4ZCKozd2O1yT65r7JwjKZv1bu1I5nTauOvBdbpecLPFQo2To3vg8LlhBVGaaf1T3WAQ39hyHqdLXUPNMI9p3Qr9mOQdzo2Nn-ui1LNER39N9KhOt8n3mWuFpKxPFklGhHBH6fe5isE27N8hDPMyeTDiDfkeo3H3wCGxGEAnyfi6vENL7DZSfUk22gnf64Yl-fDBfw7qUVI8s8R9jSgJabtROXppGzKzqPRd43XSkvcccGbeDspX74PCpi39ffhCsJqlJ6_CAl4K5EsSoREsTVTAOVTqfUhKPbLiGcMScfTJXjv-faTpTse467sHTUmxvD8nemO8aw9643nVRG9qNoubmmQ1yEQ8PnWCJtC8YwcQemC49A6swfUQEvXKCyM8x-Pb7H23XbkqxadO6MoRL5PFtyjoA47J-vaGrkTp1NJl2A0qFd8xNO7SQIaBk7x7isUp6lR0S6vSYbV0nmKlVj9-EGzTquBmQ3wVltpqUG_ZnaAiiwowMdY57Ki1-jdbqv_o85JzefVL3TfdAZuQfia3Wcl8EY29MA17y4MwfVpFTofBaz3yX8raknfofTTZ8hs6ZHllWIAOuzaw24HzSCrWIIcfBSpKbBMesAKWSJ_6c5mpL_HRoo3TJF7XkyJGK2e1VaT0l-BYY8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f3c4bb53.mp4?token=PUtBpY98fSlBVlWfHGJR1XbDiNDuSx4ZCKozd2O1yT65r7JwjKZv1bu1I5nTauOvBdbpecLPFQo2To3vg8LlhBVGaaf1T3WAQ39hyHqdLXUPNMI9p3Qr9mOQdzo2Nn-ui1LNER39N9KhOt8n3mWuFpKxPFklGhHBH6fe5isE27N8hDPMyeTDiDfkeo3H3wCGxGEAnyfi6vENL7DZSfUk22gnf64Yl-fDBfw7qUVI8s8R9jSgJabtROXppGzKzqPRd43XSkvcccGbeDspX74PCpi39ffhCsJqlJ6_CAl4K5EsSoREsTVTAOVTqfUhKPbLiGcMScfTJXjv-faTpTse467sHTUmxvD8nemO8aw9643nVRG9qNoubmmQ1yEQ8PnWCJtC8YwcQemC49A6swfUQEvXKCyM8x-Pb7H23XbkqxadO6MoRL5PFtyjoA47J-vaGrkTp1NJl2A0qFd8xNO7SQIaBk7x7isUp6lR0S6vSYbV0nmKlVj9-EGzTquBmQ3wVltpqUG_ZnaAiiwowMdY57Ki1-jdbqv_o85JzefVL3TfdAZuQfia3Wcl8EY29MA17y4MwfVpFTofBaz3yX8raknfofTTZ8hs6ZHllWIAOuzaw24HzSCrWIIcfBSpKbBMesAKWSJ_6c5mpL_HRoo3TJF7XkyJGK2e1VaT0l-BYY8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کتاب ۳۱۹ ساله نسخه دست‌نویس در دوران صفویه
🪔
📖
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/697050" target="_blank">📅 22:43 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697049">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
انفجار مهمات به‌جامانده از جنگ تحمیلی در دالاهو سه عضو یک خانواده را مجروح کرد
جانشین فرمانده انتظامی سرپل‌ذهاب:
🔹
سه عضو یک خانواده شامل۲ فرد بزرگسال و یک کودک هشت‌ساله بر اثر انفجار مهمات به‌جامانده از جنگ تحمیلی در منطقه شیره‌چقا شهرستان دالاهو مجروح شدند.
#اخبار_کرمانشاه
در فضای مجازی
👇
@akhbare_kermanshah</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/697049" target="_blank">📅 22:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697048">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
شهادت مامور فراجا در حملۀ تروریستی در فاریاب
🔹
سرگرد مهدی جمشیدی، از کارکنان نیروی انتظامی، دقایقی پیش در پی تیراندازی افراد مسلح ناشناس در مرکز شهر فاریاب، به شهادت رسید  #اخبار_کرمان در فضای مجازی
👇
@kerman_news</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/697048" target="_blank">📅 22:32 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697047">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
ادعای ترامپ: با پوتین توافق کردم/ توافق شد که روسیه فوراً بیش از ۳۰۰ هزار تن گازوئیل به بازار آمریکا و جهان عرضه کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/697047" target="_blank">📅 22:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697046">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4019f8179f.mp4?token=ESv8EMZUlO6vp42r62MSVwx0Ey5a8186ZnNFrIUpSCDjXwimpFT0rFj3rXERhzEdn4GIi1FnmzLD9WB-XOgY4zz7zdtOUIugzV_wOJfgJhr9cAqQG7WeUZw5PDsNDGiqT9O0wRn9ppt44PWhFbZajDoLwYzD9sOqANOHNs4TkPlwMwvBS8ui3Mkcl-RjaG6fsYCXC0XEDNbhhM1NhRczHN0ADKQXkKS-SmLkDNl1z_X8xV_p5gUbaad1Uv5yceXsB1DGLxG1vyElYFlunm9nTpP3-6rVoJt6giZlzeJPIAtUCoqQm65AtNTRyTXWQDD0LEnNcSBR7dAxk7pPb7YChw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4019f8179f.mp4?token=ESv8EMZUlO6vp42r62MSVwx0Ey5a8186ZnNFrIUpSCDjXwimpFT0rFj3rXERhzEdn4GIi1FnmzLD9WB-XOgY4zz7zdtOUIugzV_wOJfgJhr9cAqQG7WeUZw5PDsNDGiqT9O0wRn9ppt44PWhFbZajDoLwYzD9sOqANOHNs4TkPlwMwvBS8ui3Mkcl-RjaG6fsYCXC0XEDNbhhM1NhRczHN0ADKQXkKS-SmLkDNl1z_X8xV_p5gUbaad1Uv5yceXsB1DGLxG1vyElYFlunm9nTpP3-6rVoJt6giZlzeJPIAtUCoqQm65AtNTRyTXWQDD0LEnNcSBR7dAxk7pPb7YChw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هوتن شکیبا: من اصلاً آدم ازدواج نیستم، بخاطر بازی نقش حبیب دچار شرم می‌شدم!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/697046" target="_blank">📅 22:26 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697045">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
بلومبرگ به نقل از مقامات غربی: ایران علیرغم ماه‌ها بمباران، موفق شد کارخانه‌های موشک‌سازی و پهپادسازی خود را حفظ کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/697045" target="_blank">📅 22:24 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697044">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
بر اساس گزارش منابع محلی، صداهایی که در یزد و شرق استان تهران شنیده شد، ناشی از رزمایش سامانه‌های پدافند هوایی بوده است./ صابرین‌نیوز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/697044" target="_blank">📅 22:24 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697043">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/It__ciphFEcUJsDvX7_H6TV7Js05KaT7m7AcxO9d3CAxn2jK0zLRBtc7LDvIYf_jsd9yzerI6Q22e6-2ioxoUVI_718keu0pHsl28Mr-DGaDIXowYmAb9kkLX8TbU4zZ_YYCHENN25wA_Lv2CIRMsMs5XFt5U-NL5FKMvmsgQSIyWhCXrBUQMN3VkRX22BqqaKj46Da3KqOylxhIPrUTzqzzfBCwih0tPTKYMmRWKuo25MzPQfQrx_AU7foP2nKPieXgrsB2lt0zUMCZt7w4847sL7WFijKmclHX27vu3sz2iMxbwGCOAHYbrRJwZDtAt1zzAIuzxPpCDMR3aavvUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اظهارات بی‌شرمانه روبیو، وزیر خارجه آمریکا علیه مردم ایران
🔹
هخامنشیان ۴۸۰ سال پیش از میلاد به یونان حمله کردند و آنجا را غارت کردند ریشه ایرانی‌ها به این غارتگران برمی‌گردد!
🔹
او در لفاظی‌اش علیه تاریخ کهن ایران به این واقعیت هیچ اشاره‌ای نکرد که ۴۰۰ سال…</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/697043" target="_blank">📅 22:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697042">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
مصطفی میرسلیم، عضو مجمع تشخیص مصلحت نظام: دولت خودش از عوامل سقوط ارزش پول ملی است/ گرانی قیمت دلار به نفع دولت است
مصطفی میرسلیم، عضو مجمع تشخیص مصلحت نظام در
#گفتگو
با خبرفوری:
🔹
اولین کاری که باید صورت بگیرد تثبیت ارزش پول ملی است.
🔹
هیچ کدام از مردم از تثبیت پول ملی ناراضی نیستند، اما دولت وقتی دلار را گران‌تر می‌فروشد، پول بیشتری به دست می‌آورد و به کسری‌اش میزند.
🔹
دولت خودش یکی از عوامل سقوط ارزش پول ملی است چون در آن نفع وجود دارد. بانک مرکزی باید جلویش را بگیرد که آن هم ملاحظه دولت را میکند‌.
🔹
ریشه‌ی گران شدن بسیاری از کالاها و خدمات این است که ریال دارد ساقط می‌شود.
🔹
دولت باید سختی‌اش را بپذیرد و بگوید به جای اینکه از جیب مردم بردارم ۳۰۰ میلیارد دلار سرمایه خودم بردارم.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/697042" target="_blank">📅 22:19 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697041">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKrlUCanGB2Y4wMPW7O0gSiJETv-19fW-NhoZ1c1tRXxYcxps9ou3sG9NCBK6fBadTKOr8jY4hoEWIRZ2R3A7EJqD1umUkmz3rvycgPZHiAVV8LX1m4TPgQv5TUD-TOC-fJPtSQvy1UpjrBJvhKd3_m1UuYnJJUoFEgHR9STcBRsfLZs58XsLEbrOIppnVZGZXUYKcAuiI8HS_bxtdgRl2YVhhyH7wFytQxYU0UlojFAttQfX_jsQbDA_zbAvT_KCPdt8BRYD71AVZSG1vzADG1E1gxmABFAslMOih2K6ZMLDBULw9NaEsVrp_E466t9CjLvPSWfXNkftwrRRFUnwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نکاتی کلیدی درباره‌ی کم خونی
❣️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/697041" target="_blank">📅 22:14 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697040">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
اسرائیل ترور کرد و آن را به ایران ربط داد
ارتش اسرائیل:
🔹
ما یک شهروند سوری را در مرز سوریه و لبنان ترور کردیم که به دنبال انجام عملیاتی با هدایت ایران بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/697040" target="_blank">📅 22:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697039">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
معاون وزیر خزانه‌داری آمریکا در امور بین‌الملل به الجزیره: ما اقداماتی را برای قطع جریان ارزهای دیجیتال به ایران انجام داده‌ایم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/697039" target="_blank">📅 22:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697038">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
معاون وزیر خزانه‌داری آمریکا در امور بین‌الملل به الجزیره: ما اقداماتی را برای قطع جریان ارزهای دیجیتال به ایران انجام داده‌ایم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/akhbarefori/697038" target="_blank">📅 22:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697035">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VQEizh3BG-6MDteEkInQwGRkMyLQKxMqyGVH21jfMnByfOSTbdRnNu329k2pHcEGB5_FVVnaPm37hRBRLnVa29yNFw0ZXw_-90j2nspNuz9liaCsMCPO87PckezSxg-EGrG_HaNKoMxEcNIk01e1VNEKMuloxOl9p7xpjEffEuLgvgKBZBJrga8e_CcW_0NI010wERH42LjuF9eDyXggW7LMN86SKXQO990DrPazeZWjFx5__QoAVIl1JuK4X5DrTIK_mNqA_-mljSCtGz-93xBm-5C4fIsMFEf3Ns4ckrNYbeYkAPi9tl2Udb3q-XXdcYG8QD-yp1XhZRVsY3-V1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UBNoewqr5ZRsj628JLBT31O0MgSd1IOC8Ar_joDCSh4_8F1UGfIh5VqyJNI5H1Li6-CIidlJw-R9_8WbWMTAc5w3mp9h5ZHhzv1ntTd_S7h9zQqyIaRMhpw6aZ_k6ekTtIw3nNXaxkiGkM86aRuTDTiIYPLJ45UmOjJ3NznySl1HLmyNMlZU63kWD6JX4d9lreZ6f7_O8VpuOAnTGhU9qsRVRaovl-oO8h62vGthTCTwRhF9XXUIr8nPytQqgDTkrFFc_lJjkfhnmn6HAfOd-UQ2PTgyLl5jNpHWBK0FsjI8NoCJIC7AoSd7cTMtUi5YaStyPJMpgVS9a0cT2DwiYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YAuqiOIjWqQwCWBCajI750Oj2qNDk5TxmU-8OichSeyKpGtLiWei_TiWWb-9nRc_2yfjmq3HDhZG_XuikBEd3UsC8nbTYupzFPRjQoupJmXTZxLT1jRA9tfNnB-7sr9ZvZrs_pKuVBiCo8m7NfOP6n8MxdnzQE-YpAVd65_pTClwDDwcm6WqfqnEA9ZrQfZw1sqNwPrEVUJaIGtY1WWgp1vzu10GXTcj9IdoyPIEX21NWGcTEl-tvCxGcxq63KJo8izk76FvRG3MvgsRo5OMKtUgbScDQyvOMsKVvUg3TMEe1sLfIg_oaQHq5yV05oUidJilDsX6_4RvbadF7oNxlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چند روز پیش همزمان با ماه کامل بر فراز آرامگاه کوروش؛ شاهکاری تماشایی!
🌒
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/akhbarefori/697035" target="_blank">📅 21:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697034">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
ساعتی پس از اعطای جایزه نوبل به قاضی دیوان کیفری بین المللی، آمریکا تحریم هایی را علیه این نهاد بین المللی اعمال کرد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/akhbarefori/697034" target="_blank">📅 21:49 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697033">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
زلزله ۷.۵ ریشتری پاناما را لرزاند؛ آمریکا هشدار سونامی صادر کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/697033" target="_blank">📅 21:47 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697031">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42e28f907f.mp4?token=nlaRWd6MqiicmkG6q_8KKP8LluzDQgd3zekozYCge6cDgAbSaBfH16ZTMyueU1U15NiWI1eYLlqztRDSYFxpla0mYDM17-eolIUXXqBLGdfmtSqKkBVTgvqH8n-TiATDuxPp9gzmgvzCP9fLz6kZI975vGQzBPnFfXoZUhngvtRNJEl7WXIwjHkSLynkooyTMbQl99F_6V027yxQ11gdiNvyET1hlRNbW4cnBDMJRJsVo1pHmLsMOoSGAbAaVimW5tTDtwyHIwX3wIdRaJwo9eb0e0rnmnVoalEEUtgiFMBG7IWbRvja-iiA8NFWkuLrSV7zwLrlCMGlML6tIbRw3lohofJEcDrrZzVQA3PG_5RFNi15IJqSnr1CiaGq7PTirdUPwqZdjAAx6H6pYMfglpR701GiVrI2mhXEq7vB__D6LZVjj_Rl3waainEElGx5XxGhN2m3vAK4TtqCgnblvMLT-3mXfSSF7LRqnNOqEB35bR6ao0VN62HWv9p1WkyJRW5K6w7jJ5JKL4sYrQccyvWMW-h6zBY8vRvXpTD1uzrKyhSOocrKxhPb2cKmJH4Z8Mq9NiRMuPlt9eV8ROy3NcmmmYnMToZe6KSwb-Qw8gAZEME9mZpCgaCi_IEkr0CQ1CD0lw7wBIqa7mkLvxYHaLrZ8-Xp9mAj_LXg_NM9tng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42e28f907f.mp4?token=nlaRWd6MqiicmkG6q_8KKP8LluzDQgd3zekozYCge6cDgAbSaBfH16ZTMyueU1U15NiWI1eYLlqztRDSYFxpla0mYDM17-eolIUXXqBLGdfmtSqKkBVTgvqH8n-TiATDuxPp9gzmgvzCP9fLz6kZI975vGQzBPnFfXoZUhngvtRNJEl7WXIwjHkSLynkooyTMbQl99F_6V027yxQ11gdiNvyET1hlRNbW4cnBDMJRJsVo1pHmLsMOoSGAbAaVimW5tTDtwyHIwX3wIdRaJwo9eb0e0rnmnVoalEEUtgiFMBG7IWbRvja-iiA8NFWkuLrSV7zwLrlCMGlML6tIbRw3lohofJEcDrrZzVQA3PG_5RFNi15IJqSnr1CiaGq7PTirdUPwqZdjAAx6H6pYMfglpR701GiVrI2mhXEq7vB__D6LZVjj_Rl3waainEElGx5XxGhN2m3vAK4TtqCgnblvMLT-3mXfSSF7LRqnNOqEB35bR6ao0VN62HWv9p1WkyJRW5K6w7jJ5JKL4sYrQccyvWMW-h6zBY8vRvXpTD1uzrKyhSOocrKxhPb2cKmJH4Z8Mq9NiRMuPlt9eV8ROy3NcmmmYnMToZe6KSwb-Qw8gAZEME9mZpCgaCi_IEkr0CQ1CD0lw7wBIqa7mkLvxYHaLrZ8-Xp9mAj_LXg_NM9tng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتقاد میرسلیم از افشاگری های احمدی‌نژاد؛ افشاگری وحشیانه جایگاهی ندارد
مصطفی میرسلیم، عضو مجمع تشخیص مصلحت نظام در
#گفتگو
با خبرفوری:
🔹
رویه‌ای که از نظر اسلامی قابل‌قبول نبود در دوران احمدی‌نژاد رواج یافت و آن تخریب بود.
🔹
این تخریب‌ها از دوران احمدی‌نژاد شکل گرفت و به ضرر کشور ما تمام شد.
🔹
رویه اتخاذ شده از سوی احمدی‌نژاد که «بگویم، بگویم »، معنی ندارد. برای ما مسلمانان افشاگری وحشیانه اصلا جایگاهی ندارد. افشاگری معنی ندارد و باعث ضایعاتی در جامعه می‌شود‌.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/akhbarefori/697031" target="_blank">📅 21:41 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697030">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e3af0af2f.mp4?token=nKDwmcmlUBAQUxNrMyC60AWwYV1E25QGAmrFFkjYeucp8DYGQfvUEZvdZlwFNJfe0deGW3wplS3uo6_Vas7kaAXDCjajA8fHRHe2hWZn1hNmri5qu0NtixatNHhCX_ovluKMtiiSSw_rUnnIu0gbmJHOKFwy6vNWBpR9qoAdexqarYi7eqrTgQIcKX00x3da4B_tVveK3SEP4hEpcGEp2q69WHMMQWgopm5w19i3kiPcAjECWC9kQ8pmZBqXoEAKGErAjw97wpY8aNjPKKkVKC106dArRx3Om7RKGEY--cSVaEuWN-cBahK7aChVCOnbVAhm47ZyKFKzqEx-7ADttilIthjPyDcLQZcAkmGt0uWU9e5ZmT9WUQEXAbQaAVESyttKn33IbuZ6ntcL6cYv5BL3D1grgj4Aok50ECJgpvjnrpyImYc1LeQHFlY9c-lo9AZ7xY0-ikPejlaPYyUKLPEd37K4dSDXXwsJXcCAFhOWTWNXdCa8iI5Y7-o2h7Ndk3cPN12YMp0xxwAxRsYUVpcmRK4YSPhQ3VVNcYWqup8aleDObMZRRC64xEn5w77dbmC1X5R33cxOzWLLqFFuqEmWHkg4FQXBeUQurx-AQywtBXTXZvmD1W0vCACZrb6nu6e3GuyByu7bUV2X9dDOZ-5kOreLonRETPZEPk4hv2M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e3af0af2f.mp4?token=nKDwmcmlUBAQUxNrMyC60AWwYV1E25QGAmrFFkjYeucp8DYGQfvUEZvdZlwFNJfe0deGW3wplS3uo6_Vas7kaAXDCjajA8fHRHe2hWZn1hNmri5qu0NtixatNHhCX_ovluKMtiiSSw_rUnnIu0gbmJHOKFwy6vNWBpR9qoAdexqarYi7eqrTgQIcKX00x3da4B_tVveK3SEP4hEpcGEp2q69WHMMQWgopm5w19i3kiPcAjECWC9kQ8pmZBqXoEAKGErAjw97wpY8aNjPKKkVKC106dArRx3Om7RKGEY--cSVaEuWN-cBahK7aChVCOnbVAhm47ZyKFKzqEx-7ADttilIthjPyDcLQZcAkmGt0uWU9e5ZmT9WUQEXAbQaAVESyttKn33IbuZ6ntcL6cYv5BL3D1grgj4Aok50ECJgpvjnrpyImYc1LeQHFlY9c-lo9AZ7xY0-ikPejlaPYyUKLPEd37K4dSDXXwsJXcCAFhOWTWNXdCa8iI5Y7-o2h7Ndk3cPN12YMp0xxwAxRsYUVpcmRK4YSPhQ3VVNcYWqup8aleDObMZRRC64xEn5w77dbmC1X5R33cxOzWLLqFFuqEmWHkg4FQXBeUQurx-AQywtBXTXZvmD1W0vCACZrb6nu6e3GuyByu7bUV2X9dDOZ-5kOreLonRETPZEPk4hv2M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قیام دانش‌آموزان باکو علیه ممنوعیت حجاب دولت علیف
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/697030" target="_blank">📅 21:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697029">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
ادعای
سازمان تروریستی سنتکام: از زمان ازسرگیری محاصره علیه ایران، مسیر ۱۳۳ کشتی تجاری را تغییر داده‌ایم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/697029" target="_blank">📅 21:37 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697028">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
رئیس هیات عامل سازمان گسترش و نوسازی صنایع ایران: سهمیه سوخت خودروهای فرسوده بالای ۲۰ سال قطع نشده است/ فرصت ۵ ساله برای جایگزینی داده شده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/697028" target="_blank">📅 21:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697027">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e21e8d23c.mp4?token=SfUuzqvXFNDGvItlPkBEkOhvy56Su-Lb4AWjJ_YOqAjmM7ngJ2DEzVOkSItKRXBRcgfFOsN28Vk5h4Y02WfTh-qAA4uomVV3J0p-yN4jdnfeKY9NuS3F3XFoXwffTB4b4SR8sWsD-Qi9lidzAt5e413wo8PtNJ9aUBZx_oVuSWLZeBT_KuOdvhAwQTg-AUp07oSWS_l4teSWrbEKb-Cvfa2dQ2QmRPKLFR4Dk4PundlqaebzEm9vUtK19OpNg7YMyfOmQUOdJ3zTSjFZlLRjvAAq-oM8gWmfHCs5F5fwd0-UdMmtd2xaZ2jOrO7_sEvSBqknVKyq8AyNFF2YNLsAKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e21e8d23c.mp4?token=SfUuzqvXFNDGvItlPkBEkOhvy56Su-Lb4AWjJ_YOqAjmM7ngJ2DEzVOkSItKRXBRcgfFOsN28Vk5h4Y02WfTh-qAA4uomVV3J0p-yN4jdnfeKY9NuS3F3XFoXwffTB4b4SR8sWsD-Qi9lidzAt5e413wo8PtNJ9aUBZx_oVuSWLZeBT_KuOdvhAwQTg-AUp07oSWS_l4teSWrbEKb-Cvfa2dQ2QmRPKLFR4Dk4PundlqaebzEm9vUtK19OpNg7YMyfOmQUOdJ3zTSjFZlLRjvAAq-oM8gWmfHCs5F5fwd0-UdMmtd2xaZ2jOrO7_sEvSBqknVKyq8AyNFF2YNLsAKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توضیحات عراقچی در خصوص نشست سه جانبه ایران، روسیه و آذربایجان
وزیر امور خارجه:
🔹
به ابتکار روسیه این نشست شکل گرفت و بعضی از پروژه‌های مشترک ۳ کشور مورد بحث و توافق قرار گرفت.
🔹
پروژه‌هایی وجود دارد که همکاری اقتصادی ۳ کشور را دربرمی‌گیرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/akhbarefori/697027" target="_blank">📅 21:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697026">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e5200dd53.mp4?token=hnsxzTT9e-q8rd_gsj01U60BAIVtNXa9dqVzr5vsy8XDuwvZH45BoNc_c6CTA8-dVOE7H1ONUEvbMqSgElufL2279LcAteyDaHebuEgsoeLQCDS54jJRBlhSXTDBIGOibnz0BvyBEZTh4vHKjrxFLSryLzdUxIyWXK2Khk9fjJklYkExuA0r7nnlvVinX7g6YoCXcuexZ6PwdWvhH43SMAFQSQalhOZIiJjudMXbeR6gInFwHXDPqEfUjnBKxy_fbK_5dP6HU8PWpTf9ve4uWeUrM1_1w2Q0pPWTAFxosRC3-MJLW7jf-p8qhap3zs9XErgglKYGn-XRmpx-SHkwiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e5200dd53.mp4?token=hnsxzTT9e-q8rd_gsj01U60BAIVtNXa9dqVzr5vsy8XDuwvZH45BoNc_c6CTA8-dVOE7H1ONUEvbMqSgElufL2279LcAteyDaHebuEgsoeLQCDS54jJRBlhSXTDBIGOibnz0BvyBEZTh4vHKjrxFLSryLzdUxIyWXK2Khk9fjJklYkExuA0r7nnlvVinX7g6YoCXcuexZ6PwdWvhH43SMAFQSQalhOZIiJjudMXbeR6gInFwHXDPqEfUjnBKxy_fbK_5dP6HU8PWpTf9ve4uWeUrM1_1w2Q0pPWTAFxosRC3-MJLW7jf-p8qhap3zs9XErgglKYGn-XRmpx-SHkwiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۵ ترفند ساده برای تشخیص تازگی مواد غذایی که هر کسی باید بدونه
🍯
🐟
🥚
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/697026" target="_blank">📅 21:26 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697024">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8bcc79797.mp4?token=PTgVFQiSRLTDgM7sYbO6cr46xhTAOsMw4MUZeO4WkfEzj2vIYznTX54XH24D8R5mv33XrNNdoAA3snmLt9fdYL8LXgZ8cl_iV1biVjZtgu7hjM1aGQ-3X-Y9wPek-ZBMexsHTAl8xuGjOMpbH4nRFHn30s28eOAD3KCzzgijn1sN1rxjmmEFX8W_lrED1MF9l1P7xdBM1im2OM_igPst6Z_ebUEo5rcWVlvQHQAs7WOhhOXKYC-z-eblaSr2BMI5zIKeGxM3ixmzoGm_Ek2PmBiqmtcUP2ofArQTzuYhW8HtExJLCjl1-_Gecmk8FrFT8v7QfFC66Bp7y0L2AHqPAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8bcc79797.mp4?token=PTgVFQiSRLTDgM7sYbO6cr46xhTAOsMw4MUZeO4WkfEzj2vIYznTX54XH24D8R5mv33XrNNdoAA3snmLt9fdYL8LXgZ8cl_iV1biVjZtgu7hjM1aGQ-3X-Y9wPek-ZBMexsHTAl8xuGjOMpbH4nRFHn30s28eOAD3KCzzgijn1sN1rxjmmEFX8W_lrED1MF9l1P7xdBM1im2OM_igPst6Z_ebUEo5rcWVlvQHQAs7WOhhOXKYC-z-eblaSr2BMI5zIKeGxM3ixmzoGm_Ek2PmBiqmtcUP2ofArQTzuYhW8HtExJLCjl1-_Gecmk8FrFT8v7QfFC66Bp7y0L2AHqPAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر پربازدید از اعتراضات دانش آموزی در فرانسه
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/697024" target="_blank">📅 21:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697023">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
ایلان ماسک رسما به اپراتورهای موبایل اعلان جنگ کرده
🔹
اسپیس‌ایکس با خرید فرکانس‌های ۸۰۰ مگاهرتزی و مجوز پرتاب هزاران ماهواره، به‌دنبال ارائه اینترنت ماهواره‌ای مستقیم به گوشی‌های معمولی است؛ فناوری‌ای که می‌تواند پوشش موبایل را گسترش دهد و وابستگی به دکل‌های زمینی را کاهش دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/697023" target="_blank">📅 21:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697022">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
احسان دهمرده، از پرسنل معاونت فرهنگی اجتماعی فرماندهی انتظامی سیستان و بلوچستان در حمله تروریستی به شهادت رسید  #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/697022" target="_blank">📅 21:14 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697021">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b979e766ff.mp4?token=SohuyuZ7CBrG_ApHhwSSZ6lMQNQuj6SsBBmFCrK4xDBkQuIys4RmEiHjmKeRRxfpEQ_PKUk8es_lx-VLG3iHz4YFGJWbwDUxuH_N4t5pW7_i0KHXCtS8qYEbTD8GI4H2oFD7NyQCjVOW5wPDj40vgqgZkwJQE6m-7aMloT1AjNvJXMKuEku6WUlE5aKN6DuUl-un6wmjD14d34UE2KbB9YkvAmqFMSbXSj3ryK4D501HcEPt8-katyPOWIdhrRMpe6wlX9dYPZAswB4K4BBTxq_y52DABj3xrk2VUn1gR-5WPifH3_DmSGNtydp9yMr_oRIcLO-Nxo1ttGPEsuPphQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b979e766ff.mp4?token=SohuyuZ7CBrG_ApHhwSSZ6lMQNQuj6SsBBmFCrK4xDBkQuIys4RmEiHjmKeRRxfpEQ_PKUk8es_lx-VLG3iHz4YFGJWbwDUxuH_N4t5pW7_i0KHXCtS8qYEbTD8GI4H2oFD7NyQCjVOW5wPDj40vgqgZkwJQE6m-7aMloT1AjNvJXMKuEku6WUlE5aKN6DuUl-un6wmjD14d34UE2KbB9YkvAmqFMSbXSj3ryK4D501HcEPt8-katyPOWIdhrRMpe6wlX9dYPZAswB4K4BBTxq_y52DABj3xrk2VUn1gR-5WPifH3_DmSGNtydp9yMr_oRIcLO-Nxo1ttGPEsuPphQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یائیر گولان، رهبر حزب دموکرات (اپوزیسیون اسرائیل): ترور علی خامنه‌ای بی‌شک اشتباه بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/697021" target="_blank">📅 21:10 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697019">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
مصطفی میرسلیم، عضو مجمع تشخیص مصلحت نظام: انحرافات اقتصادی کشور از دوران هاشمی رفسنجانی آغاز شد/ این انحرافات از همان زمان ادامه پیدا کرد و گریبان کشور را گرفت
مصطفی میرسلیم، عضو مجمع تشخیص مصلحت نظام در
#گفتگو
با خبرفوری:
🔹
رفسنجانی به عنوان رییس‌جمهور تصمیم گرفت سازندگی را اولویت قرار بدهد و مقدار زیادی نقدینگی برای این موضوع صرف شد، اما معادل آن محصول و نیروی انسانی وجود نداشت. لذا در دوران ایشان به تورم ۴۹ درصد رسیدیم که خیلی زیاد بود.
🔹
دلالان زیادی در این میان ثروتمند شدند. اینجا انحرافات اقتصادی درست شد که گریبان ما را گرفت و ادامه یافت‌.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/697019" target="_blank">📅 21:07 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697018">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jamgVLFq90HK8-rKPkE4VO1cW-iug4yYoaT5PNyPHvxwpWivT2qAhecqPA_a5iI0uB1eY4H7Ctslo24T7GyQ7l8tIvi7VUtYdaUhKEC-4O8UQJfnMAuHaJX-Gdhq94REN5Wyx8gBcBk8feGPBkApJJrjOB1iMTgzMJax2NpMylT05PJWf6hZr1wIuOJ6OIPg8mEPre4585-Ter4iDnUzcCe1qairfK5qsoQC5FVY7cV4jnmi83sRIO8xkyaaxfuctevdW7BSemhC2RZyhte0zxt7Lk1jJ1E8x9U2Y_tCU-oQoA_lKDULCxbUEOhiV7jrbs2I7i2tfJYb_XBi8P97BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
باز هم دست ترامپ از جایزه صلح کوتاه ماند؛ ناوی پیلای، قاضی‌ای از جنوب آفریقا برنده جایزه صلح نوبل ۲۰۲۶ شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/697018" target="_blank">📅 21:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697017">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/075e34bb4a.mp4?token=uKQVvz4D89RTVcMIkG2fuFwXR-hVYoCR1CLgXmYhgrYskBTeFnqqqmUFZKN9KcUykPfaFHGA4qBGIq-4g-UN_Kke1GD41dOyJ7TJd2SSyjtdMIQl9eL79Z3Pgo0hDdBTsOq2u3gj93iifrGRS5OMRw4WVbWtgP_Gae1RwqPjrSxNDxXySMJynyAIfLnX47zEM-3iFJX8n0RG_aeQ7DCKP8vL4Jo8oCrKCWdLXZtq-p8EKi5VWNCJB2J9aSw02ZlfDVYWLCPhZtxEeaJfMvAPcVpCVL0iWJ72w-BvYRaTqT-01putYHPEIi6lOUEfHCy_hBMJHaheZjzRBKr8RQ2vtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/075e34bb4a.mp4?token=uKQVvz4D89RTVcMIkG2fuFwXR-hVYoCR1CLgXmYhgrYskBTeFnqqqmUFZKN9KcUykPfaFHGA4qBGIq-4g-UN_Kke1GD41dOyJ7TJd2SSyjtdMIQl9eL79Z3Pgo0hDdBTsOq2u3gj93iifrGRS5OMRw4WVbWtgP_Gae1RwqPjrSxNDxXySMJynyAIfLnX47zEM-3iFJX8n0RG_aeQ7DCKP8vL4Jo8oCrKCWdLXZtq-p8EKi5VWNCJB2J9aSw02ZlfDVYWLCPhZtxEeaJfMvAPcVpCVL0iWJ72w-BvYRaTqT-01putYHPEIi6lOUEfHCy_hBMJHaheZjzRBKr8RQ2vtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فلامینگو جدا افتاده از گله/ دریاچه مهارلوی ایران
🦩
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/697017" target="_blank">📅 21:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697016">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53d6c9260b.mp4?token=lNLeh4PNI9sse8MI3_TzL6DLCHBSAmIUUOJ2JkBRz9YTZbnNUxAp8jbG2L_kLUziFTpsugh-zrpPWlG-P4OOZKBR2M0j0mAjcjHZswfXhzP-Ni4cO4tEno8M5PsuiTMUbE7tg5ZOUbNGnHXpjTlWCUh8RhJV34CjCpiQ0ZL50v9mFf8aCzD02OqxpezPZvUDHHjg2xpj3KHEIYkuJeIHwU0gsZ_8qL2LoKyDyUHowO3CkvWdcEPXPIn3hDTnO3wgtRYAB40plbler8swq5Cv3HnPn8T9oltsP71Ol8RtCTzkdcS15mUpWACDRjjDmFKwr8RjHf5pqP7T0GOiMwounQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53d6c9260b.mp4?token=lNLeh4PNI9sse8MI3_TzL6DLCHBSAmIUUOJ2JkBRz9YTZbnNUxAp8jbG2L_kLUziFTpsugh-zrpPWlG-P4OOZKBR2M0j0mAjcjHZswfXhzP-Ni4cO4tEno8M5PsuiTMUbE7tg5ZOUbNGnHXpjTlWCUh8RhJV34CjCpiQ0ZL50v9mFf8aCzD02OqxpezPZvUDHHjg2xpj3KHEIYkuJeIHwU0gsZ_8qL2LoKyDyUHowO3CkvWdcEPXPIn3hDTnO3wgtRYAB40plbler8swq5Cv3HnPn8T9oltsP71Ol8RtCTzkdcS15mUpWACDRjjDmFKwr8RjHf5pqP7T0GOiMwounQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شب‌های پایانی سیاوش/آخرین تمدید
📣
دعوت بازیگران کنسرت نمایش سیاوش برای شب‌های پایانی
بلیت اجراهای پایانی کنسرت‌نمایش «سیاوش» برای روزهای ۲۲،۲۳،۲۴ مهرماه (چهارشنبه، پنجشنبه، جمعه) از فردا(شنبه) ۱۸ مهرماه ساعت ۱۴ در سایت‌ ایران‌تیک آغاز  می‌شود.
https://www.irantic.com/theater/52434</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/697016" target="_blank">📅 21:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697014">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f22ac382f6.mp4?token=dBLhsFKfG8YSve59CixueVcwisC79oKfLpbZumMfONhySDfRQRUl-kOt4iH_tKmV8L3me6_5gQlwUNJ3MgA2UH117J0WO6mpVR5YyXgeWHLA2LTN33_X9x7XuWdQt9Oyu8lBxEFgWCETf5gD6dH4rJLadrY4PlLqmPmGK9wW2LyX7SbOFe639FM6yrn9kfdyRcqjQ_ihlQLkPVQy3qsFzQp0dx8FVp_Pd3hk2uG75flPxmgYKC3vRrgY4DY8N0j9wir4QADerNHVXltwLh9Be6GZd1XGyTfe57tqPeFqipIMY--zwWtT94T3ZrHL9oE5DUCeizzPWhm9u_m1Urna5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f22ac382f6.mp4?token=dBLhsFKfG8YSve59CixueVcwisC79oKfLpbZumMfONhySDfRQRUl-kOt4iH_tKmV8L3me6_5gQlwUNJ3MgA2UH117J0WO6mpVR5YyXgeWHLA2LTN33_X9x7XuWdQt9Oyu8lBxEFgWCETf5gD6dH4rJLadrY4PlLqmPmGK9wW2LyX7SbOFe639FM6yrn9kfdyRcqjQ_ihlQLkPVQy3qsFzQp0dx8FVp_Pd3hk2uG75flPxmgYKC3vRrgY4DY8N0j9wir4QADerNHVXltwLh9Be6GZd1XGyTfe57tqPeFqipIMY--zwWtT94T3ZrHL9oE5DUCeizzPWhm9u_m1Urna5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پایان بازی| ارونوف برای تارتار گل کاشت/ سرخپوشان به یک‌قدمی صدر رسیدند   پرسپولیس ۳ -- ۱ صنعت نفت
🔹
گل‌ها: تیوی بیفوما(۴)، علی علیپور(۵۳)، اوستون ارونوف(۸۵) برای پرسپولیس / محمدحسین باصری(۶۵) برای صنعت نفت.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/697014" target="_blank">📅 20:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697013">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9f98bbb43.mp4?token=uvfn1ereDfnYDQ4-SQzHEaXaJkD1GjYQymuV21l6Dto4HxZAsYtwuP39FepskNfiNK6cDXwZRAzW2kV6IvscbV3BFjHFVFEFA-zx-grcsjrJ0Noijut2Jo2cPwFYsKbHmj_3l_L452Wn7fBN065UlIDadLrR41YIPHVir4jXlWrUtYT9lB_XVdQzmoLrlWPBKcVhIy7Beg_DnQwbiE69ezn6RF3N-uR4MK-JVQKi118Sf_pLKfnxZzovyW29K-5COUGST16lZ-eVZHdN7lqcJ946O9229X6CfHJsTYY50g5shRawjw55cVtFj2c6UI6mWuQ8Xvo6rjrnCCOW_1-Jjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9f98bbb43.mp4?token=uvfn1ereDfnYDQ4-SQzHEaXaJkD1GjYQymuV21l6Dto4HxZAsYtwuP39FepskNfiNK6cDXwZRAzW2kV6IvscbV3BFjHFVFEFA-zx-grcsjrJ0Noijut2Jo2cPwFYsKbHmj_3l_L452Wn7fBN065UlIDadLrR41YIPHVir4jXlWrUtYT9lB_XVdQzmoLrlWPBKcVhIy7Beg_DnQwbiE69ezn6RF3N-uR4MK-JVQKi118Sf_pLKfnxZzovyW29K-5COUGST16lZ-eVZHdN7lqcJ946O9229X6CfHJsTYY50g5shRawjw55cVtFj2c6UI6mWuQ8Xvo6rjrnCCOW_1-Jjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نماینده جنبش حماس در ایران: ایران به حماس کمک می‌کند؛ ولی خرج حماس را نمی‌دهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/697013" target="_blank">📅 20:49 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697012">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d62dd728d6.mp4?token=o9Jli9jbqtoAC7SJWzOXO5JgPHr3KCMGci_UcxHbp2yFf0brAz_Trfp6yjgRs9MPzkejbZ6XOhOh3D7qkFnqytDvTHwE98nqivaeNinULoDnoKdgPALGujeko8cRw7HnhCz129gviVIKIbTWK_A6uCbSF4EieRNdW0RhcYZrem4pMti6hAS-OH8RgEU86U0XdnskTiIjIKlVkA54DOqDCnp2XJGyVAJxGEMwy3F6fe2ek5U7IGm2NLopUJjcF315YWOSTiHP6ntKbwwkMEUi_g3f7AD3sOifyuL-DFtDYwvgRHmIw42ynMHD3QNb2u00Lm1T3vz0gbpu5DOdOt-y8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d62dd728d6.mp4?token=o9Jli9jbqtoAC7SJWzOXO5JgPHr3KCMGci_UcxHbp2yFf0brAz_Trfp6yjgRs9MPzkejbZ6XOhOh3D7qkFnqytDvTHwE98nqivaeNinULoDnoKdgPALGujeko8cRw7HnhCz129gviVIKIbTWK_A6uCbSF4EieRNdW0RhcYZrem4pMti6hAS-OH8RgEU86U0XdnskTiIjIKlVkA54DOqDCnp2XJGyVAJxGEMwy3F6fe2ek5U7IGm2NLopUJjcF315YWOSTiHP6ntKbwwkMEUi_g3f7AD3sOifyuL-DFtDYwvgRHmIw42ynMHD3QNb2u00Lm1T3vz0gbpu5DOdOt-y8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اتهام‌زنی دوباره نماینده آمریکا علیه ایران در شورای امنیت: انصارالله ابزار تهران هستند؛ ایران باید حمایت از آن‌ها را متوقف کند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/697012" target="_blank">📅 20:44 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697011">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
تصاویر منتشر نشده از شلیک شاهد ۱۳۶ و ۲۳۸ به سمت مواضع دشمن آمریکایی در عملیات نصر ۱ و ۲ و عملیات تنبیه متجاوز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/697011" target="_blank">📅 20:42 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697010">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
مصطفی میرسلیم، عضو مجمع تشخیص مصلحت نظام: دولت ۱۰۰ تا ۱۲۰ میلیارد دلار به صندوق توسعه ملی بدهکار است اما پس نمی‌دهد/ روزی ۲.۵ میلیون بشکه نفت را مفت می‌دهند و مردم هم می‌سوزانند!
مصطفی میرسلیم، عضو مجمع تشخیص مصلحت نظام در
#گفتگو
با خبرفوری:
🔹
در مجمع در زمان آقای رفسنجانی صندوق توسعه ملی درست کردیم که سرمایه نفت (از آنچه به ارزش ذاتی نفت برمیگردد) در آنجا قرار بگیرد تا افراد نیازمند سرمایه از آنجا وام بگیرند و از محل تولید و سودش آن را پس بدهند.
🔹
آقای هاشمی گفت اینها نمی‌توانند صددرصد آن را در صندوق بگذارند، اجازه بدهید ۸۰ درصد را دولت استفاده کند و ۲۰ درصد را در صندوق بگذارند.
🔹
در حال حاضر در صندوق چیزی ندارند. یک رقم فقط این است که دولت ۱۰۰ تا ۱۲۰ میلیارد دلار بدهکار است.
🔹
دولت سرمایه‌اش زیاد است و اگر بخواهد میتواند پس بدهد، اما در تعارض با منافع مدیرانشان است و این کار را نمی‌کند و فقط ۲ و نیم درصد آن محقق شده است.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/697010" target="_blank">📅 20:42 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697009">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9ae359f54.mp4?token=nOTmfzjFOM-nDgDFPdKxBxSd5XwHwgnoM07fJOXGPpCBXjknuTuliQ-ALrmJjqQ9opiA4jBHMDSu-7z7uALOiQ2_yYj2q-druIadfCwn1JBHitQO6bZQzDZrtik1qfXwMM0qKiVMIID3btNnKSbH3tZtp8fMeLlcR0eiW8GH7FqeFju6kEbDZOZR3hJbdZnSaQvKFUjp-HQ4aCIbOh1pDZN6Rf61HUzVyKiC1CcY8vAzSjgQlmN6xDGkjRD3oiV8NiZECuXkKu1hscrEVkqB1wHefJ2hDr5XNOmVCrjYnFUBErjQLe8KNb1_-ZhPFTkfqY-FUd-OixkSThqucMnnTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9ae359f54.mp4?token=nOTmfzjFOM-nDgDFPdKxBxSd5XwHwgnoM07fJOXGPpCBXjknuTuliQ-ALrmJjqQ9opiA4jBHMDSu-7z7uALOiQ2_yYj2q-druIadfCwn1JBHitQO6bZQzDZrtik1qfXwMM0qKiVMIID3btNnKSbH3tZtp8fMeLlcR0eiW8GH7FqeFju6kEbDZOZR3hJbdZnSaQvKFUjp-HQ4aCIbOh1pDZN6Rf61HUzVyKiC1CcY8vAzSjgQlmN6xDGkjRD3oiV8NiZECuXkKu1hscrEVkqB1wHefJ2hDr5XNOmVCrjYnFUBErjQLe8KNb1_-ZhPFTkfqY-FUd-OixkSThqucMnnTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی «نور» تبدیل به ریموت کنترل مغز می‌شود!
🧠
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/697009" target="_blank">📅 20:41 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697008">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
عقده‌گشایی زلنسکی درباره ایران و روسیه
رئیس جمهور اوکراین:
🔹
اقتصاد پوتین را تعطیل کنید. دهان روسیه را ببندید. با فروش‌هایتان به روسیه خوراک ندهید.
🔹
به ما دسترسی به استارلینک بدهید. وقتی به ایران حمله کردید اسرائیل کاملاً حریم هوایی ایران را کنترل کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/697008" target="_blank">📅 20:32 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697007">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYdPeZi9xafw7_VZpmEB0gCZ3I9uB4TxKvOD7d7I60aTRgseQ9Er97l_hVJLQV1IAZWikH0qSF3_wImrDX9_K063YsxkVIECVu86C1FiWDKSdsMba4R8cBVHg9tswXOHhZ2dIjg2gjR210I5Nn6iLKwvJ_8B0EzCRj7l8n4pqHaDmiVb6WRsSJMKXuM7ORve3ISPke8ocZTE6koy83pOscDG3-wWCWA9_EQOYi780CGryQP7G9-8DCCJ_juaWsuVTNqzUwNxAAiKq2TNahLdC916IYXzQMuuEcRGd8v4QTgKtzmneUcM_zwll05z6WX-bSGeTE9e2UrZKqPk3kCsFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دبیر شواری‌عالی امنیت ملی به آمریکا: برای تکرار شکست‌های تاریخی از ایران آماده باشید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/697007" target="_blank">📅 20:24 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697006">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0be0df3c01.mp4?token=BQMpBi6_N72-S6AGIZHwi_dPhM4Dy27GjtY2aM2sfjKbbr2lv1dNWTVLK6svDaEB-ye1kmo5GG-W_OOdU-6vp43gijBkQOWFiyRgAiyYlnReqKImaQHzkosNMSeUsFSr7t5t3fBjC8jnQQ3ON2WuiWcQ_npJHT-qFek1wvcw42x9_DyqwaSYEu_pUsf14rVTvfGqUu9WJv5Pal0bY5QHDLfT3CYBbAEm9Yjxnb9sPGNtdoOAMZ6Cl4aAvua3BvymKxtuzxVa6uB19gh2FxWzXEvmUpVj8nHyQ0xI0ASge1-K8OkWyryK2_MAHZ3uaKh69b5ILJzBIwJg-znnlvYU7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0be0df3c01.mp4?token=BQMpBi6_N72-S6AGIZHwi_dPhM4Dy27GjtY2aM2sfjKbbr2lv1dNWTVLK6svDaEB-ye1kmo5GG-W_OOdU-6vp43gijBkQOWFiyRgAiyYlnReqKImaQHzkosNMSeUsFSr7t5t3fBjC8jnQQ3ON2WuiWcQ_npJHT-qFek1wvcw42x9_DyqwaSYEu_pUsf14rVTvfGqUu9WJv5Pal0bY5QHDLfT3CYBbAEm9Yjxnb9sPGNtdoOAMZ6Cl4aAvua3BvymKxtuzxVa6uB19gh2FxWzXEvmUpVj8nHyQ0xI0ASge1-K8OkWyryK2_MAHZ3uaKh69b5ILJzBIwJg-znnlvYU7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وعده وعید های مبهم و تکراری ترامپ درباره ایران: به‌زودی همه‌چیز تمام می‌شود و قیمت‌ها به‌شدت کاهش می‌یابد!
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/697006" target="_blank">📅 20:22 · 17 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
