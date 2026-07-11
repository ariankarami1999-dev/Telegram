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
<img src="https://cdn4.telesco.pe/file/ZCqcQ8i2RsBMf_LxmISIrqVNjhLjOylK3ACjs2oJ6NwLXREV8uRAVpetpUeUtcsq3xRKBxGaWEmSH0S5hllGBrpc7AwCrjOXwaz5u7lH298YAD1cUhio4RDy-QBJgBzA3EjGxjiv4gfdtPA_5_RzpWVzXoG9rk1CV2oRKdEeR1VAYjCzTqTQok24eJYZjNIT6ihsGGvstlvSjysMTvzZmtKRYBBLuSuBCt5aKfC1m4d3DMnC-PgSaW58J313gvoXligjN2cbO5MjOE4h3iQ3ciavtLVZNhS1rYlzKWVOgtVXBH-mt7hLBCXy1oiTcsiViTjLQSdi8NmrH5tlBJuMDg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 12:34:36</div>
<hr>

<div class="tg-post" id="msg-449131">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6zz4-eEUYYrUDwJfp_wlYivyCO1A3m5ZjwAPaODjHrqd1oFsTEWFj5Jcm88jyykpFT-AkqkEqDE2IFYSdMhHs7ALihh6ib3_cYTTc6nZ5avrJ9gjy-x00fy1BIasPiBJhjoJ4-bpkjAytMQi_6csB0J6-rrdk35rC00El5HnaYWuRQepvj4CRB7xLVFLXu1-LAoosiSCInLGl681bfKakA8UcSOo5fARLT3qyl7QP-BROlWeNVabSOzuVyd7o2OkVnXOrJmHBK7DAmgjCV2MlGNaXleF4YTA207EaariGx8DsmqyEiHYh5-cCOXSoHahUhux7Wo5zsLPQcpUU9JWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریزش ۲ درصدی بورس در آغاز هفته
🔹
شاخص کل بورس در پایان معاملات امروز با ریزش ۱۰۴ هزار واحدی به ۵ میلیون و ۱۸۳ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 361 · <a href="https://t.me/farsna/449131" target="_blank">📅 12:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449130">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqpMqBladttNr9POa5evTlT-qhjP1RwgvHS3NGdOxcbdLDrGuPgIBPlGZtNA2vusGa7VbzxxP2JBkjEbPtjUyNOOJaIETiui1AHXj_TcT-_K5zr0Xhl6c2Vv2LoiPoR0e-5FilEVdc2nwlljk4TWLjvDwMmKSkIVT0nF2Se9xdW0HWHCDteXllyX6RtBky-jmeQxC5DISfhEnof7QjnSciFRXCWhD4CRKQRaXA50vZ3bgkQLukCAvGMGK0nJL8KcuwA2tlFJwFcuvdG4Jx1rf3a7iqKylts58jnneNvcWBy4dNBelyv8iLLLdAwNf_hJU6TH7Ic48SQNjGE3R9871g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
جلیلی: مذاکره در صورتی ارزشمند است که موجب تثبیت و ارتقای قدرت شود
🔹
نمایندهٔ رهبر انقلاب در شورای‌عالی امنیت ملی: مذاکره یک ابزار است؛ نه هدف. ممکن است در مقطعی کارآمد باشد و در مقطعی دیگر، نه.
🔹
نباید به ابزار موضوعیت داد؛ آنچه اهمیت دارد، نوع، چگونگی و زمان استفاده است آن است. اگر موجب تثبیت و ارتقای قدرت شود، ارزشمند است و اگر موجب تضعیف قدرت کشور شود، مضر است.
@Farsna</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/farsna/449130" target="_blank">📅 12:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449129">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
رادیو ارتش صهیونیستی: یک افسر ارتش اسرائیل در پایگاه نظامی شهر الخلیل، بر اثر زیرگرفته‌شدن توسط یک شهروند اسرائیلی که «از اختلال روانی رنج می‌برد» زخمی شد.
@Farsna</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/farsna/449129" target="_blank">📅 12:10 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449128">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dsD1Q9FtTyE1onAXgBg0VTpgI2Z7rlisdW-oPYJrR_KMsHJ9HZ66irmTYgJMESGdHHgXU02RzdtxUlYFy3Eijf_U18PywIeu848x-NyfNOnxO2HIHP0aHqWEXocwEtlhCTBIp901lHR9ljxFImQ-vgRwBhVanJ6y8s4wdEzsLY7gmUie80Ff9ybPfUI4xMFLlJJr7vYng3ajLuddGzF8yyhQCs0LulmBk-U5EoL7IilCr22S8wPW8ez_Ql4RRpfXRBiUvNNvMwMWobPqtTX6SHSf49cJqnMOPcaaq0_5CaX_3I6-wqHHBhbdgljlB29z0vKCoeqTxIQG5oQ8DVYOBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ آمریکا پل کریدوری ایران با چین و روسیه را زد
🔹
بامداد امروز آمریکا با موشک‌های کروز پل راه‌آهن «آق‌تکه‌خان» پل استراتژیک کریدور ریلی چین-ترکمنستان-ایران در شهرستان آققلا، استان گلستان را هدف قرار داد.
🔹
مسیری که روسیه از آبان پارسال کالاهایش را از آن عبور…</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/farsna/449128" target="_blank">📅 11:56 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449127">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">قدردانی وزارت اطلاعات از امت اسلامی دربارهٔ حضور در آیین تشییع قائد شهید
🔹
وزارت اطلاعات: تشییع عظیم و تاریخی بزرگ عالم مجاهد، رهبر حکیم و فرمانده بصیر جبهه مقاومت در ایران سربلند و عراق کریم، جلوه‌ای ماندگار از وفاداری و بصیرت امت اسلامی و تجدید عهد با آرمان‌های الهی مکتب اسلام بود، حماسه‌ای که بار دیگر عمق پیوند ملت‌های مومن و با عزت ایران و عراق را به نمایش گذاشت.
🔹
اینک که آقای شهید امت، خامنه‌ای عزیز، این دردانه تاریخ جهان اسلام و تشیع پس از عمری مجاهدت با بدرقه تاریخی ده‌ها میلیون شیفته و دلداده، در آغوش امام رئوف حضرت علی ابن موسی الرضا(علیه السلام) آرمیده است.
🔹
ما سربازان گمنام امام زمان(عج) در وزارت اطلاعات، بر خود فرض می‌دانیم که از خالقان این عظمت تاریخی، روسا و هیئت‌های دولت‌های دوست و برادر، مراجع معظم تقلید در قم و نجف، مردم بزرگ ایران( اقوام، اصناف، اقشار، اهل سنت، رهبران و اقلیت‌های دینی و...) و ملت کریم و پرشور عراق، مرجعیت دینی، حوزه‌های علمیه، دولت عراق، عشایر، موکب داران، عتبه مقدس علوی، حسینی و عباسی و همه‌ی دلدادگان شهید امت در لبنان، پاکستان، افغانستان، آذربایجان، ترکیه، کشمیر، هندوستان، بحرین و سایر نقاط جهان، صمیمانه و متواضعانه، تشکر و قدردانی نماییم.
🔹
صحنه‌های پرشکوهی که در عراق توسط عشایر و جوانان ذیل مرجعیت دینی رقم خورد و میزبانی کریمانه آنان، جلوه‌ای درخشان از الفت و برادری دو ملت ایران و عراق بود، سرمایه‌ای ماندگار برای امت اسلامی و پشتوانه‌ای استوار برای تداوم راه شهیدان و یاد آور مجاهدت فرماندهان مقاومت شهیدان حاج قاسم و ابو مهدی المهندس در مقابله با گروه تروریستی داعش، که نام خود را در تاریخ مقاومت ماندگار کردند و بار دیگر با مخابره پیام انتقام، رهبران جبهه متخاصم را به واکنش ذلیلانه وادار کردند.
🔹
اینک ایران و عراق تحت ارشادات رهبر معظم انقلاب، حضرت آیت‌ الله سید مجتبی خامنه‌ای حسینی(مدظله) و مراجع معظم تقلید نجف به خصوص حضرت آیت الله العظمی سیستانی(حفظه الله)، در نعمتی کم نظیر که قرن‌ها امت اسلام از آن محروم بود به برکت این خون مبارک و  اتحاد حسینی و علوی متنعم‌اند.
🔹
در پرتو تلألو نورانی این نعمت الهی ما فرزندان خمینی کبیر، خامنه‌ای شهید در وزارت اطلاعات ضمن پاسداشت جلوه‌های این عظمت با رهبر معظم انقلاب(مدظله) عهد «خون و مجاهدت» می‌بندیم ذیل منویات ایشان، تا تحقق آرمان‌های امام راحل و رهبر شهید از پیشتازان نبرد عاشورایی علیه آمریکای جنایتکار و رژیم کودک‌کش صهیونیستی و خون‌خواه رهبر شهیدمان باشیم.
@Farsna</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/farsna/449127" target="_blank">📅 11:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449126">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">🎥
از رهبر شهید عذرخواهی می‌کنم و حلالیت می‌طلبم...
@Farspolitics</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/farsna/449126" target="_blank">📅 11:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449118">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BkmwOLZCzxW_PfDC2c5JSRyjskFS__5fFJuqK_nXIyYhQXtkDXCl9JnbdGDW6fJSLp4oV442tCQJdNv9WBduWZIuBNWCgfMfuzOCY-ansEkuAhT2URIRMxf4Rfc_yGAI2ZWVWjJkBr1cuLx7UchxliA-RPJOWnrUjKx3WQLomjONXlv7orAmu-JeJjZRaFy9dmK2bFEGxUnt5gl9OVgtdkq7xlOtAcJWnu3LJFZsQy7A2D9tCzYOZBArSFTqHlU9-jxnZl_yDeb3Ca2B9rokH1tfBD8z7k_N2lnbowxILdqFxs_d9YueuW0oOcxQduRtisqCgLskKOHqn4FxOiA2Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i7OO69nX0QYCdsVUcb90cIgh4XJHPhSDGoOSG4b9NKS_vRyeKtEnvrospSuBYWIsyJ7SKmeSJR1lBlaiihjYD4rbPIxfryYfnxncfU-e5m0SQnJlwOwscFy3m2qSHfh561GeOxlrataFLs3dV8i_6d2zS5348GqWLd6oSXaIkNjuHSi389qzzcoMuATSxgFTc7lcU5MGR26facEfxedxptXmFhDivBz7w4CqMB8WtLUUKnhiUYHiRe5kL1paSug990z2pQ4eEnkhucLikIfvfGejTtFVjUL3Zq6tchfuAV1od0eqXMXIRcvfwf0sKveqpTHyWuCqOCinYcSMtYchXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MnvnVyRvapc1TB73PB8MA-KhtpFdA580NkwanDN8HbDFRmKIXb_p6snHRjKbyOikWbUtJ9HUys_gKmRVpVzR2emzGxymnTe7gZccKS1iMxVGki8ChHv3esPHUjbGCb5L0uuE1lDUJhqTCSyuIs_Uv_2vmRLzKF_obqNBUuqJH-LzGaSKa_p1AIL_aoY0Aplm7MCUOIOILfw0v-OZGaQ8gT9R4wsvNjlJHp4P421-b5jeAqhRNllOmlLcb-tZ_ITDM9qx4ubkM-p7qgClwG4vQbQ7Flwotn9hZvXNFiuORLVgcLlVwpmmOPHvrFI1FmybLSLOi9jeniGpkBEJZFCdGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AT4JmpN8-hpBhh1GexOzJTwHQ6F2yjb0cAA3HjQXhBuIKsAukeP8Uv-wqvfodrelFGGDuFfSSFktpB7gnz4X6HS8DgHw5QRaYPqHxsYRw77ay8XprluHGn3Um0yShh8wxXFm4Bnsw6YOvgdF7JNYsCjYiEifNG_J1816wWuWgsZqt1JNsF31b7DgPCpua_VysntGpRGtyOHgW3z2HlIeyjqJWjr7WaE1DL3Cj0WjIaxdMzkY1sbxjv6ECOB2zmOH02KluShYqijg0wPG0Yw94RiPO1Ehmc0bKFx1fWotGhmkvKqvABwaemy_XcK4YyNbLvKN2b_aSh9621PrKIIDNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uJTD4TS31NjbYPrgfkcm50A9IJcoIpfKpWk9H4-WZbiKNjzZNjHMSyCbB4ytXtyIviTZIy1XoRianfI3VKe7oqYo9ti4hLXAIkps0gTjw3ndvPBNI83fU-Aubt5YAGylHNTNPCymWfzxGfawfr4tSTG3N3BUhypiUBk0dP9ZU-o2zUfasaUmdKaZXQGhvaYa8EZXY5e8RNEadc8Wjy3z8glZ4DHCaqOcuakR3e2ZWwaLVMixGKR5RTYyiRtBgtqyQyGK9l0J5RBPn8JVA_NU3lnwNU2r-GPaXu0BElPQZVovIYtzxKMFuwrFv8fMh9wE0EWMruRaaWdhXW_PCaJjIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BBFrGdJMBd0zdSojcGd9CF6PWO5JPsadKX7p5iFUM_KcGWSU7vXXcDTINdhpF8QvpmSQ1inYn3D5Y8UuGAqPHBZ9Ydgp1CLT_oYyUnkmAUKdp_CGjLbCbA0H1s1lPjEZ7spHcpja_q5x4fW_RBwpp-tbkbMgYtucZEMqgmqoN6RAG7uWv9DtNYkUKcB9Ulv_PPLeTrk_aTB7MGKren7cv1tFvTR_u5uIoOdlgbend3OZPbrq87ue9V7ZsxwZKzOzZBL9m0Ajtnaz62vlkEj6sjKl1_faOnhkPV-MpCLNuU7bYkidNigjh2ojw5LZnTYmlMMuyeICJhDjszWdtsScwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BD47UgMPR-QUp5m_sQ5TeXTlmG0On-vIRw-F300gVB84-7pp1_EAwGjxec6gnQ5Z0DeVLZhSAmtO67O0LKQvcv9Uqc7Lp6OQ9p_4sy1wAYuE7CfxuEQdvndyTTDPFRI-R6Hb7gb0zL1-MPWmIh5x6Opbm29qIDuY1mYI1jEQ13pd-_WLBpfhzpeUgJPOIQhIHYNG62566ScrTddUoDA2SSfvTXpWHTtKe-MfPoF7v5Qli4DIZy6633FOa97nFbfh5mM8C3xbUrHe4nPoQfNXNbJ3X27mwfwL9Ii0AyyqwS72FdGfuV5PFQ64ukjXUV4JX4y7pJdfsWScpo5Qta7RIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v-VmelPNkXmnynW-uc65XrjB6thqof4RG0xDtvKBC5qWQ8gzQj8ayeq8NdhRIsOblpaWbtCEQaqEcxQ7UFsEDBRh7Ri_se16NRoNkvmyejmKQbt9aXaLw8AwenXJoQMLsy0JaBacWs8xi9aDXfbWhg7K-ac_EpKo8K5x4OP2LrxabqWQfEtK_FP-SvjtY9lKRtA0CSR0DlTHHedadhGstwqCLohQY1qUUwpRROSbsiGE2zTUg85U60QOVZOCf_fvl0u1ykWhoxQ2tt0BVghELFjRTpIaSsH4aunzmIWW90c8lhKKeH_AgfNIRa4agkO71qMMU6_zBVet-J5iUMJSig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آیین بزرگداشت رهبر عظیم‌الشأن شهیدمان از طرف رهبر انقلاب اسلامی در حرم مطهر رضوی
🔹
این مراسم امشب و فرداشب نیز پس از اقامه نماز جماعت مغرب و عشاء در صحن پیامبر اعظم(ص) برگزار می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/farsna/449118" target="_blank">📅 11:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449117">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/205d1d93d5.mp4?token=gS9rk2N2w8h6Wf7WnnYKODiOZFHQcbhyri-V7KJWAU5rJpsCY2yXmfDFp5F304Vaofh0A1f3L2NLD-gvcoMJUbY0z5Mb4XAv_N6YeR2eMsnkgwoDSXRXiAW96YMHGk0tJvqjczoxzJ2aYTAJGDXwirAAJ6O33qZfJrB4Go1WB9zgdMweaya8SlcQ7n0F9UVqWoiTrBqFpo-GgP2v2bKArGeqQo4_9R4aXMU5T27-Mq6YlhNlQ74ByNNXMNj4zPt03bypS3B3HbtyulSHbwAvjOaFcZvB1mz2VJatSisn_vEQcwiXwvuYgWdmv4qswKGpBfITTYoLGnYZqYT1WvqdwTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/205d1d93d5.mp4?token=gS9rk2N2w8h6Wf7WnnYKODiOZFHQcbhyri-V7KJWAU5rJpsCY2yXmfDFp5F304Vaofh0A1f3L2NLD-gvcoMJUbY0z5Mb4XAv_N6YeR2eMsnkgwoDSXRXiAW96YMHGk0tJvqjczoxzJ2aYTAJGDXwirAAJ6O33qZfJrB4Go1WB9zgdMweaya8SlcQ7n0F9UVqWoiTrBqFpo-GgP2v2bKArGeqQo4_9R4aXMU5T27-Mq6YlhNlQ74ByNNXMNj4zPt03bypS3B3HbtyulSHbwAvjOaFcZvB1mz2VJatSisn_vEQcwiXwvuYgWdmv4qswKGpBfITTYoLGnYZqYT1WvqdwTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سربازان فردای ایران با گهواره‌ به میدان آمدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/449117" target="_blank">📅 11:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449116">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‌ فرماندار پاکدشت: صدای انفجار ناشی از امحای مهمات بود
🔹
صدای شنیده‌شده مربوط به عملیات کنترل‌شده امحای مهمات باقی‌مانده از جنگ بوده و هیچ‌گونه حادثه یا تهدیدی متوجه شهروندان نیست.
🔹
این عملیات با رعایت کامل ضوابط ایمنی و توسط نیروهای مسئول و متخصص انجام شده…</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/449116" target="_blank">📅 11:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449114">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyZ1hrTtmbQdL6NfJGAM-zRIj1HfymSOgeueXwTdqw5vR0nRfB1yL1W2b2uic8ZiVOmzQhK4MsNJXuiKnIXdcuLl1viIw8fugjScUY_fGbuXGPvjmeVuZNPHUoougCspGGx_8yPsKrx0elHaXtkyJR9PheofiqL7iNAC7b_xISXwJ6-r84HzDNkIAn9iMb2P4eFsusvTUVx8Qr56VN5M9SFU6YkOm0G-vFOyRIdVbztwjpokTD_HUJxX8LK5Gq4OhCzBPPetCQGj8Rw53P3NZusoeBULWGIaaTjI8-QJENdJwHtU4AxOYBVmCo49xBcfTDHK3WzlAW2HhwDCjSbbkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده کل ارتش: راه امام شهید انقلاب را با قدرت ادامه می‌دهیم
🔹
حضور موج‌آسا و بی‌کران مردمان ایران عزیز، مسلمانان و آزادگان عالم در آیین وداع و تشییع پیکر مطهر رهبر شهید انقلاب و خانواده مکرم ایشان، حماسه‌ای درخشان از پیوند ناگسستنی میان ملت و آرمان‌هایی ترسیم کرد که با خون پاک شهیدان به ویژه امام و قائد شهید انقلاب، رنگ جاودانگی به خود گرفته است.
🔹
راه امام شهید انقلاب، با قدرت ادامه یافته و آینده‌ای روشن را برای ایران اسلامی، رقم خواهد زد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/449114" target="_blank">📅 10:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449113">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47ad7ae545.mp4?token=JNDMnWp9J5-Wbw39U8xkbTXO6H2yDinrHKVw1VArB0dXKjSo3GPNTuZwPyuILuOEyb5oQVX3SmFJqzGcAQpDSQkSm7Sbl4ovy4iEri7FnqLXxmYYnaqKNzevaTDawjJQlx4eVKcEZqWh5HaPowwVhWdWXMZStloi11WXQ9wMhlb9lWBbsJpxxPvJR2DNUxBPHDFI73PNJvu73xfsv18d1dMZchCVOZTpBfBVjoCkzOTPa9lI--ZG1scTmT5C4pUYlKH-1U8MMjAZ6leOGDaFY-SpVkoeBxkXrwhwvmxMy2U2l68eBud9Bd4y6VX_6BYJjvDqiTT3is_1qgkxGSqjGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47ad7ae545.mp4?token=JNDMnWp9J5-Wbw39U8xkbTXO6H2yDinrHKVw1VArB0dXKjSo3GPNTuZwPyuILuOEyb5oQVX3SmFJqzGcAQpDSQkSm7Sbl4ovy4iEri7FnqLXxmYYnaqKNzevaTDawjJQlx4eVKcEZqWh5HaPowwVhWdWXMZStloi11WXQ9wMhlb9lWBbsJpxxPvJR2DNUxBPHDFI73PNJvu73xfsv18d1dMZchCVOZTpBfBVjoCkzOTPa9lI--ZG1scTmT5C4pUYlKH-1U8MMjAZ6leOGDaFY-SpVkoeBxkXrwhwvmxMy2U2l68eBud9Bd4y6VX_6BYJjvDqiTT3is_1qgkxGSqjGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مزار مطهر رهبر شهید انقلاب اسلامی و شهدای خانواده ایشان در رواق دارالذکر حرم امام رضا(ع).  @Farsna</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/farsna/449113" target="_blank">📅 10:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449112">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d989485063.mp4?token=Mr-Zv1yBzqKelavjCL3y1Pq2m6sh1HN5aXJnSz8vBNO_6w-ECev14HELqPgPoGmyNNhQJsk9HLcttrNuKi1noP7CknxatYsTv8NEDWtjkKVCc8NciSHXCIYOz91mV6GvtDB-v_fFBqaeD0ln_PDbB7XkY03-O-IqrmjXfm_n8AI4WlOFDi74je5Q8HPLMrsRZoWzfm4Csokvkmyubt8JKurYgCX-CdlLEdwN-nrPVKZnO6uu9FOjBv6SlstZGcmgZbUf51rxtcHh5moYJyD_zc1D5Kmk-ekYNl4dpmQIW-ZIClLg84ke8dkEK-CeN7zbKi6CyaOVEaQ4tOLYBJO8SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d989485063.mp4?token=Mr-Zv1yBzqKelavjCL3y1Pq2m6sh1HN5aXJnSz8vBNO_6w-ECev14HELqPgPoGmyNNhQJsk9HLcttrNuKi1noP7CknxatYsTv8NEDWtjkKVCc8NciSHXCIYOz91mV6GvtDB-v_fFBqaeD0ln_PDbB7XkY03-O-IqrmjXfm_n8AI4WlOFDi74je5Q8HPLMrsRZoWzfm4Csokvkmyubt8JKurYgCX-CdlLEdwN-nrPVKZnO6uu9FOjBv6SlstZGcmgZbUf51rxtcHh5moYJyD_zc1D5Kmk-ekYNl4dpmQIW-ZIClLg84ke8dkEK-CeN7zbKi6CyaOVEaQ4tOLYBJO8SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاس گل هری کین به ترامپ
🔸
در شرایطی که ترامپ به‌دلیل دخالت در پروندۀ بالوگان با موجی از انتقادها روبه‌رو است، کاپیتان تیم ملی انگلیس در نشست خبری پیش از دیدار مقابل نروژ گفته حدود یک سال‌ونیم پیش با رئیس‌جمهور آمریکا گلف بازی کردم.
🔹
هری کین: راستش بد بازی نکردم. وقتی در پالم‌بیچ بودم، او از من دعوت کرد که با هم گلف بازی کنیم. خب، وقتی رئیس‌جمهور از تو دعوت می‌کند...
🔹
تجربۀ واقعاً عجیب و خاص بود که با او ملاقات کنم. راستش گلفش هم واقعاً خوب است. امیدوارم وقتی به سن او رسیدم، بتوانم به خوبی او بازی کنم. از اینکه دعوتم کرد، خوشحال شدم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/449112" target="_blank">📅 10:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449111">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a51b25b24c.mp4?token=fNfactKujvpeUOccBO102CI58a9Cblu_AraHR832NEVr5IB6I6xdJCbw81n2sSJxMmAwce5PxHWq5YKR2TUzna00PWVMppXQAUAxrxsnv1A3NAkjdFhy9Ks2jElGCF1e4GPI8zWgW-psF7xiDbmdC_z1BspJGwm-h6bn9QmkFG7jIJUV15Ui7ABZbtnQxFODUHIGbp22ntIVt1GyPzOwV8ZAtVsYyd_R2nMe6dWTVgegxLQGnAIBMKt7uwVmF9cPt6hsvrzZNEPyRVhe6UfIewhva7VHhNpEE3Mi4vzwDm8RK0BsOAjfyIrkFsN3zIOldzQBqJ2A3rphSRMI0wXMEg659G8QgzhOT8uTIm8BctnNzUk4SQGEVcDlKnpEinhSGWyGQyamPYr5AlPll0ELJ-GwDrq9Ub8JIF9fermzZsybOJiY8SCxLfEAgGhLkyoxTbDnWGpTOBu8YlGVImgRy6g1i8j6Ba2PB3YKVMBaTclCPn1C6ByMOhgZ9OD3Eg_S5zzQutzrkQxGuNGQGw7BxwfzuaOB2gaY8wgkILAROMzYLsbwVeLZ5AO-tmBQFxKrgBi6zCN5Qyw6bsoKs0HYsrO7TmNyQ2jSDZ3VjaDhyEYwPoL40WB084f2x5xOHSskEk8y4R8OgQG1hPKJO8ZONE9YDc2DB-uqIYTOEJMlBKI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a51b25b24c.mp4?token=fNfactKujvpeUOccBO102CI58a9Cblu_AraHR832NEVr5IB6I6xdJCbw81n2sSJxMmAwce5PxHWq5YKR2TUzna00PWVMppXQAUAxrxsnv1A3NAkjdFhy9Ks2jElGCF1e4GPI8zWgW-psF7xiDbmdC_z1BspJGwm-h6bn9QmkFG7jIJUV15Ui7ABZbtnQxFODUHIGbp22ntIVt1GyPzOwV8ZAtVsYyd_R2nMe6dWTVgegxLQGnAIBMKt7uwVmF9cPt6hsvrzZNEPyRVhe6UfIewhva7VHhNpEE3Mi4vzwDm8RK0BsOAjfyIrkFsN3zIOldzQBqJ2A3rphSRMI0wXMEg659G8QgzhOT8uTIm8BctnNzUk4SQGEVcDlKnpEinhSGWyGQyamPYr5AlPll0ELJ-GwDrq9Ub8JIF9fermzZsybOJiY8SCxLfEAgGhLkyoxTbDnWGpTOBu8YlGVImgRy6g1i8j6Ba2PB3YKVMBaTclCPn1C6ByMOhgZ9OD3Eg_S5zzQutzrkQxGuNGQGw7BxwfzuaOB2gaY8wgkILAROMzYLsbwVeLZ5AO-tmBQFxKrgBi6zCN5Qyw6bsoKs0HYsrO7TmNyQ2jSDZ3VjaDhyEYwPoL40WB084f2x5xOHSskEk8y4R8OgQG1hPKJO8ZONE9YDc2DB-uqIYTOEJMlBKI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آغاز فصل دوم «سرآشپز»/ ادامه رقابت بزرگ آشپزی در شبکه سه
🔹
پس از استقبال مخاطبان از فصل نخست مسابقه تلویزیونی «سرآشپز»، فصل دوم این برنامه به زودی روی آنتن می‌رود.
🔹
این مسابقه با محوریت رقابت آشپزان و نمایش مهارت، خلاقیت و فرهنگ غذایی ایرانی تولید شده است.
🔹
سرآشپز در حالی آماده بازگشت به آنتن می‌شود که موفقیت فصل نخست و استقبال مخاطبان، زمینه‌ساز ادامه این رقابت تلویزیونی شده و انتظار می‌رود فصل جدید نیز با همان رویکرد سرگرم‌کننده و رقابتی، مورد توجه علاقه‌مندان قرار گیرد.
🔹
این برنامه از شنبه پس از اخبار ساعت ۲۲ از شبکه سه پخش می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/449111" target="_blank">📅 10:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449110">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4HFZ_jehUWCzu6IsBqNYHEj751-0OXmz5K80_3zrJUlDm2TCUk3za3Iqewj8WFeTy4KyRJmRTPRaVf_yumOU3PZYkZfYCD8i1YzweXzC-ZCcZnxMoMCPz9NdtED1rAj70d1Fnaa6qlQcsB0-35li-YtKjAF3wOlq8_ArYsLVtp1yWPTzuD-FxwuooxFHFHmKSjBrydeIXSkd6Ym2oSXGXRedzB_nCNtm-h-MjUG1xtO-6YzBbOQN1NGJ_EyUNA1zk54f2Rycs7Whh0iDlEFfpATRkWolye7DZ9hVDyFUARKcT1p62Z8B601k4MubNvJWmS_ze6C8NGKu_ni6_Io6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
به مسابقه جام جهانی دعوت شدید!
جام دی همزمان با جام جهانی
با جوایز جذاب و متنوع
⏰
هر شب از طریق شبکه ورزش و
ویژه برنامه ۲۰۲۶، همراه بیمه دی باشید.
پیش‌بینی هر دیدار،
جایزه داره تو دی‌دار
ورود به بازی
daycup.dayins.com
#کانال
اطلاع رسانی شرکت بیمه دی
@dayins24
#دریافت
نظرات
@prday24</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/farsna/449110" target="_blank">📅 10:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449109">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farsna/449109" target="_blank">📅 10:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449108">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DrMyHyGqA6n7LI3n_YRT0oZaMfk6Aebp69YgScpBXIH7SKi_WXSlYRWjsjBAFw3Cw_Dz7fWCF0WQgZqu3jL6oNdwozBRXd1Pq-Qyms46q6CZFQONZ9j_reI7C3GOPGYqGV1vwPmQuTC1zTC64W6Yb_TFsDsX3O7kBdFLpriXTlnhKLgfJgU-itSkQ_yiKv4zyQUMpkT5P-R0eU9vFUqjO_yomIUp7GEJujIrmCVxwoSPvkCysJJiwtVK4kBr0s801vzIlj-ePkiliC2pUAWpvpXkX-lue7J7ZhQWW2M3XQru6PqnFg5G_rlWax0gYEVD8-_fhoIomFDnDEGX-8Jspw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
پیام رزمندگان پای لانچر به مردم: خدا را شکر که جای خالی ما را در تشییع امام شهید پر کردید  @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/449108" target="_blank">📅 10:07 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449107">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
شنیده شدن صدای انفجار در محدوده شرق استان تهران
🔹
دقایقی پیش مردم در پاکدشت و قیام‌دشت از سمت شرق استان تهران صدای انفجار شنیدند.
🔹
هنوز منشا و محل دقیق این انفجار مشخص نیست‌.
🔹
پیگیری‌های خبرنگار فارس برای مشخص شدن ابعاد این ماجرا ادامه دارد و اخبار تکمیلی…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/449107" target="_blank">📅 09:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449106">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
شنیده شدن صدای انفجار در محدوده شرق استان تهران
🔹
دقایقی پیش مردم در پاکدشت و قیام‌دشت از سمت شرق استان تهران صدای انفجار شنیدند.
🔹
هنوز منشا و محل دقیق این انفجار مشخص نیست‌.
🔹
پیگیری‌های خبرنگار فارس برای مشخص شدن ابعاد این ماجرا ادامه دارد و اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farsna/449106" target="_blank">📅 09:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449105">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0Jkp7wMe3GP1VwkyhA5eTb-0KFU08yqQ5Xzp34qxlwENFCkqNSRwBRi-P8IwfDdMvzBIuOX6mHY_XRZVbiACz4jlDs_MlYmbS-N_WKHA5tUOa5Cvi1hfsOZuKEnKKbB_LCdS3-wCWzndphSXgKXAKpZgyqXJOARUOjABPCCJ8MvuzbO05uxzaknkhV9SR4cBH2f2w5Vj67khHmfEjZ_75TzEOFFufXcWB34bUXoCN6K9-s26yyK7Tl0qxNqVONp6GPtH-L7tZpaufJBFMBFHDkhhSKKA-SuZcb1Bj45W_aPN0dxJndkBw3eP_QtGfdqu1KYaJYztB4jFn3BMp2Ffw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی با استقبال مقامات عمانی وارد مسقط شد.
@Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/449105" target="_blank">📅 09:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449104">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5wi4C_0YyYx3wS1YiXt16HUE97aYqZPMR06YNdgROM5NO3s8y4oau8xOm1DCdOsQ_Zojpdz3gPohjOpB1TJQOoWtqk1Prw0Q2JMeMNlxj0XXwcuN2krMRm155ghbbcQIiK3wHRCVUEGuBwxqa04liC4mVNuwEs51GL_bc3EXBgrlTW2Vhn9m42YkkCADrjq6D2Gti32lHJfx9hEReQ9Jtv_k29y4tPbIZy-DmbRYZkbF4mhh2L8KolzbHZFGZc3OfrWWrPKbYP7fqnoOa4uYQXH_t38MJ4d7JIQmje-eznD8SqkSwlVHvYgr_YT_a3zi69T8AN7LPzJmwDvKKqiFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سخنگوی وزارت خارجه: نیروهای مسلح با چشمانی بیدار تحرکات دشمن را زیر نظر دارند.
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/449104" target="_blank">📅 09:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449103">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a954ff7b09.mp4?token=jNjbBaGYrCC5STz2Z8pIEOGHzJGekuC__zIlWJzHkyDwl0XLtttC8WWkXbNTKc8ScbJbMVOXCTCq3I4Fbw-ryc9aX5qA0nO3cNO_pk39_-I_LHshINYSl0FeQxH0txhbuHfhLKA36fJoky906QQ-Z5SbojAoNnJdHzs358dUoJ5uHYCAsrnVjrIqdcto_S8qZ2ARmAixlIqIRZEmzRhSHGVNw3lhVmiwk6xbIXIR2SCGttAse7uHdJfHAFviLOyD1YXBBlPOvI6ijKktGPaWsrQ6d7enFZirklIonlQVgFSmsZyVVnQh5j-gqKkMzeaOocacHTjopM1bdWsJPieHrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a954ff7b09.mp4?token=jNjbBaGYrCC5STz2Z8pIEOGHzJGekuC__zIlWJzHkyDwl0XLtttC8WWkXbNTKc8ScbJbMVOXCTCq3I4Fbw-ryc9aX5qA0nO3cNO_pk39_-I_LHshINYSl0FeQxH0txhbuHfhLKA36fJoky906QQ-Z5SbojAoNnJdHzs358dUoJ5uHYCAsrnVjrIqdcto_S8qZ2ARmAixlIqIRZEmzRhSHGVNw3lhVmiwk6xbIXIR2SCGttAse7uHdJfHAFviLOyD1YXBBlPOvI6ijKktGPaWsrQ6d7enFZirklIonlQVgFSmsZyVVnQh5j-gqKkMzeaOocacHTjopM1bdWsJPieHrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملۀ ۹۰۰ مار به ساکنان مردم چین
🔹
در پی جاری شدن سیل در یک مزرعۀ پرورش «کبرای قاتل» در چین، حدود ۹۰۰ مار از قفس‌ها گریخته و به ساکنان منطقه حمله کردند. شماری از ساکنان دچار مارگزیدگی شده‌ و با شتاب به بیمارستان منتقل شدند.
🔹
مقامات چین اعلام کردند که ۳۹ نفر از مردم جنوب این کشور در نتیجه سیل ناشی از طوفان گرمسیری «مایساک» جان باختند.
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/449103" target="_blank">📅 08:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449102">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">انهدام محمولۀ انفجاری در مرز کردستان
🔹
فرمانده مرزبانی کردستان: مرزبانان با اشراف اطلاعاتی بر تحرکات گروهک‌های تروریستی، بسته‌ای مشکوک که به‌صورت ماهرانه‌ای جاسازی شده بود را شناسایی و کشف کردند.
🔹
در بررسی بسته ۴ قبضه نارنجک جنگی، ۸ قوطی تله انفجاری به‌همراه ساچمه‌های فلزی و کابل‌های مربوطه کشف و ضبط شد. این تجهیزات برای اقدامات خرابکارانه و ایجاد خسارت قابل استفاده بودند.
🔹
شناسایی و دستگیری عوامل مرتبط با این پرونده در دستور کار اطلاعاتی قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/449102" target="_blank">📅 08:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449101">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Prd8Da9q6O1rTcmtR0uUzEJZKwtBKVvyNF0hJSxRqLu5P7o3aNmE7KOsrMYjXIPSVFro156EQ9duDz5f8f5Wja7J68QQkb0yua_Ac3O5oy94FQZo_NWAWo71tsUb02DtcWICiyT3tw-bPOqN9x_8gvCIGxsK8-Ue_gucp7S39JMy6KUCvy_w8v0fTjL6o669ilmJMSnD2Xhy5cPydy4jk_DTPpuU2-o0jJMLa3fhTvOKhwXwKQUN-Buvaju_5cR3EZmt2Jn9sxX_0aeIreH525uTAeV25H_3j4umVwAKzwpvEVqLJLuytV11Q6z9y6atxDEwd_-5PnLjgouWvBYZFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ آمریکا پل کریدوری ایران با چین و روسیه را زد
🔹
بامداد امروز آمریکا با موشک‌های کروز پل راه‌آهن «آق‌تکه‌خان» پل استراتژیک کریدور ریلی چین-ترکمنستان-ایران در شهرستان آققلا، استان گلستان را هدف قرار داد.
🔹
مسیری که روسیه از آبان پارسال کالاهایش را از آن عبور…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/449101" target="_blank">📅 08:25 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449100">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/860819be3b.mp4?token=PRcIu7t1vwXXYokeTGjaSpCxRFcteNY4w2cIrcd2YlKgodkZwjnrDH1RLKv4cy88UnFKe-Q-vvBObRdatE8ym4iakQFn_Ue-JKgZxCb5Te1bwAjliipAy6mdh3ddJt4VFsuSVSgJNJd4-R7v5aJP3HRnCZvxcYv9Xq5UqyLOyhMESmAVu3Z2_MCbj3KDXwd7fwv1fh-zr4VJnWtGCw7xfWMuylDYLdln-FQKeclMv9CsnPUhDUFc0Nsce-3r8XCPgL0W8m5VUt4_v_qHlSVmSUZau2oe2hE6qcWMfZZnFdjE5vUvW5hqt-Eq-o2qFq1NUn4TNNtn-ywBA5YhoJZLyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/860819be3b.mp4?token=PRcIu7t1vwXXYokeTGjaSpCxRFcteNY4w2cIrcd2YlKgodkZwjnrDH1RLKv4cy88UnFKe-Q-vvBObRdatE8ym4iakQFn_Ue-JKgZxCb5Te1bwAjliipAy6mdh3ddJt4VFsuSVSgJNJd4-R7v5aJP3HRnCZvxcYv9Xq5UqyLOyhMESmAVu3Z2_MCbj3KDXwd7fwv1fh-zr4VJnWtGCw7xfWMuylDYLdln-FQKeclMv9CsnPUhDUFc0Nsce-3r8XCPgL0W8m5VUt4_v_qHlSVmSUZau2oe2hE6qcWMfZZnFdjE5vUvW5hqt-Eq-o2qFq1NUn4TNNtn-ywBA5YhoJZLyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۰ کشته در سقوط مرگبار هواپیمای مسافربری در باهاما
🔹
یک هواپیمای مسافربری کوچک متعلق به شرکت «فلامینگو ایر» در آندروس شمالی، در غرب ناسائو پایتخت باهاما، سقوط کرد و هر ۱۰ سرنشین آن جان باختند.
🔹
سازمان بررسی سوانح هوایی باهاما در بیانیه‌ای اعلام کرد که اطلاعات اولیه نشان می‌دهد این هواپیما از فرودگاه بین‌المللی لیندن پیندلینگ به مقصد فرودگاه سن آندروس پرواز کرده بود که پیش از فرود دچار مشکل شد و به درون بوته‌ها سقوط کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/449100" target="_blank">📅 08:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449099">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSC8yO3K3mZiQm6Z31zpA3zm5n2yfPMQosLdjUMfFVa_RbjNcTZ8JOTfqM58KJm5GjOhJDrLsoBy_ZGFl1GVXyucvhLKF_GxN_m9GhfPi6FB3i2ukNIcs4XasdV3LkNKyqzocsFVxwRlYjp5RO_Ik15gsnyjFvwsdHbc29V3jMbbKiFYoljPo-VvO-L7sr-77ipeTB-fLFxliWmmGkmlKkl9SQYA0gU_0eIR497Rah6Hj20VUC4o-OY_RvFp8TqEQLQUqwutoG9bstg6utTvlVd3LSV2ldj-tRqbD78-4FMSnCgdUyx2MuNGz_MrOw03M4PNle11HFgIfQxEYmlMkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ رایگان بودن مترو و اتوبوس در تهران تا ۱۹ تیر تمدید شد
🔹
با تصویب اعضای شورای شهر تهران مترو و اتوبوس تا پایان مراسم تشییع رهبر شهید انقلاب ۱۹ تیر رایگان باقی ماند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/449099" target="_blank">📅 08:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449098">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDMFKvMDVBl5IDvnQ8fZ3jfWheF2wvkD6QPuxJqUbYck2bSOyr3FHah2p5_MBCiq_rfh5u_fpBNLfP-EN9XxJZoHWyvjfKZIR9if-86UNCC6NKxlZ7XoyZQS04c8i5h3BgPCcGhnGzq1jx4XYhdQ6RLnPxKqQxKFfbib3gjzyMAZ5R9HpFeDBthbDsFFLXpCWCHOQ-Jtn9z1MBMnT-D4CEzDT560hbf-9tICntSR-IJAjwdLPinBhF1nK0nKtdwtx8v8fEQZA0Uo0Azwb8vFF6qpSzlcC2XzUo1X19uW7uyyfamBS9OCPIwXr8rQPA7Y-4q8hN7mL_mqten2L3c0Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلفات زلزلۀ ونزوئلا از ۴۰۰۰ نفر فراتر رفت
🔹
رئیس مجلس ملی ونزوئلا: تعداد جانباختگان زمین‌لرزۀ مرگبار به ۴۱۱۸ تن افزایش یافت و شمار زخمی‌های این فاجعه نیز به ۱۶,۷۴۰ نفر رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/449098" target="_blank">📅 07:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449097">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cV6bxiaYY13BGME6n_dknldxti3rCFUkI8Gu8R8GrsMaLM5duUnhzzG8fp4wGiYvpqJPa4mUQ-iuZG9MVGI9iNLlGQkGFjPyQcSw0hHDNTYIKcuCbrkqV0TRTd0tvaWLek6xltucn6afpfENRn6T2JIvEcaJnyX7qUjjk-fKMEfWH7LAUZMiKgZt41aejKbta6BsDgd80XhPbOOzTEMCKFqevWYsullj4SnBESFqBtU_Tbg-kGJOu5-s1CEvdfg6groJurcA3b10hiETXgmdfcLP1NKFLqdcOTV715LGBhv3ADmt-_axex_L2cxpY9clUArEtdApjwi4PG09zQdRIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جام‌جهانی‌؛ یک جام برای فوتبال و یک گنج برای فیفا
🔹
یک تحلیل اقتصادی تازه نشان می‌دهد بزرگ‌ترین برندۀ جام‌جهانی نه تیم‌های حاضر در میدان، بلکه فیفا است؛ نهادی که بیشترین سهم از درآمدهای میلیارد دلاری جام‌جهانی ۲۰۲۶ را به خود اختصاص داده است!
🔹
فیفا از محل حق پخش تلویزیونی، قراردادهای اسپانسری، تبلیغات و سایر فعالیت‌های تجاری، انتظار دارد حدود ۱۳ میلیارد دلار درآمد کسب کند؛ رقمی که جام‌جهانی ۲۰۲۶ را به سودآورترین دورۀ تاریخ این رقابت‌ها برای نهاد حاکم بر فوتبال جهان تبدیل می‌کند.
🔗
متن کامل این گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/449097" target="_blank">📅 07:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449096">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKmeTgLur7vlrwJP_OhnJLM3jCMupIgm8iepWqKNsriyjGSNxq2jV-xM5QloTYNIilQ4ID-sYWQMkyAWXJx4Ym_mR-bsSJPBo5R65GfwENlrWUUixAqK7Wzt2VLNgpRm_3SeouwfDZDSU1G3bimMkRExHrNBIiDDScFlmoqmKFJMPC95DqJNyTzORRQVqWFR3VGHjrBWVEhEvxGgfzFUOOVT5-3t_gB0JgDUUFed8aWXBLGvonQvtN5dGkMBVw9FIavPQA8eR4wAQ6o-Wr13FGpng_Co_sAoeT0yQ8eFepIbC8HnQwl49xafsL3WSqDTK3kGzwT-AIBsuRTmqtHpQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با ذکر «الله»، آتش‌بازی تهدید علیه ایران راه انداخت
!
🔹
رئیس جمهور آمریکا در پیامی سرشار
از ترس و خشم که در شبکه اجتماعی «تروث سوشال» منتشر کرد، بار دیگر ایران را تهدید به حمله کرد.
🔹
در این پیام نوشته شده است «هزار موشک مسلح و آماده شلیک، جمهوری اسلامی ایران را نشانه گرفته‌اند و هزاران موشک دیگر نیز بلافاصله در پی خواهند آمد، اگر حکومت ایران تهدید خود را عملی کند؛ تهدیدی که در گوشه‌وکنار جهان علنی شده، مبنی بر ترور، یا تلاش برای ترور رئیس‌جمهور کنونی ایالات متحده آمریکا، که در این مورد یعنی من! دستورها هم‌اکنون صادر شده است و ارتش ایالات متحده، برای یک دوره یک‌ساله با قابلیت تمدید، آماده، مایل و تواناست تا کلیه مناطق ایران را کاملاً نابود و ویران سازد — حمد و سپاس خدا را! »
@FarsNewsInt</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/449096" target="_blank">📅 07:07 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449095">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔹
شهردار کی‌یف،‌ پایتخت اوکراین: در پی حملات موشکی روسیه به چندین محله از این شهر، دست‌کم ۶ نفر مجروح شدند.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/449095" target="_blank">📅 06:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449094">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SeFsOlsmWXwoyP0Yn3a8hH0INCTQmB2QFR_QS8SIoeAMrNXemHxboc6NhjIJOu2rM6j6HT_6KNihYH1Gv0_pTq0YS120leGGrazMPpMbCpla9nZwHAnsu9BLLo67_Ot01v-LnvitloKRvWbBEjzjZh52W_pzlLaxqPb_YyeXPO8np0ilYH4WArKZ1jDlkIg9QFVIQDrAn7-KoGQIyyFtKvWJH-ub1L18iMJeHEMJOAH7GUrnoRmzQN8XXDjIpC8YVxe2s7jcd4vamenkGklRemq1R_0sF_n-23vrhxjW68g4uKBh2lk2W2wF7dZjqO0FUJi490Cf7QG8vw_dRPELHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مردی که ۱۰ ساعت زائران رهبر شهید را از زیر قرآن رد کرد
🔹
نه تابلویی کنار خود گذاشته بود و نه از کسی چیزی می‌خواست. قرآن را بالای سر گرفته بود و مردم را از زیر آن عبور می‌داد. کودکان، جوانان، زنان و مردان، یکی‌یکی از زیر قرآن رد می‌شدند و دوباره به صف جمعیت بازمی‌گشتند.
🔹
بعضی‌ها با تعجب می‌پرسیدند ماجرا چیست. وقتی پاسخ را می‌شنیدند، آرام از زیر قرآن رد می‌شدند، دستی به جلد آن می‌کشیدند و بی‌صدا اشک می‌ریختند.
🔗
ماجرای این قرآن در میان جمعیت زائران را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/449094" target="_blank">📅 06:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449093">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OaVep1MdvenBCwqgsI1IFsat5tXCW0Z9D5JqQ91t4Y2C9-4AfFbOce8x3e1kbONWxmPt3AzpomjB27uddXly8j10k4JHpFe8gYk6dPgXhrr3ymxblGvFQsHpl0SGTViMqt9PbB9hQCoS4mCS-8ninBGmn-pxMv8B1sPI6Dgm_h5L0WROE6nbwsLU1kf-Bb5jsnEnleiwvxz13xZzgS7WaOCULdxCH7jINz1M8nyll4Sxakf2Xo79PiBxdGgs0oSpwrESfgaI8zxDfAlKm2yXSf840ze9vLNPfZx68rrYNt_p9y9rONvGpIKASP1BYlUu1e-RlrNNa4rkFZnYhr45lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کالابرگ سرپرستان خانوار دارای رقم انتهایی کدملی ۳، ۴، ۵ و ۶ شارژ شد.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/449093" target="_blank">📅 06:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449091">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JSHUrlwiOWKYv5qlpbAT1ObGyzbjVUQTCX9cbU9OpoyD9FiqTgm-boQ271RdVSokch-310QvCSFE5ncJEV_U679X3rhFczD_HvL62O0VQPQgxvasiqL8hQRxJj5Eoi9KtKhYoN6GGeDX7GM_W22UkUTzi4xEGx7HzLvtM-XTndmQMjWos1fljXW4ccNFoCU6-c5ZYBomrG9-2um_QoszwEdjU7MRSrRHUyg6jGInP5pXMuC6c7WL8hAg-_UWPf2KJ0Z-3epptkgFnm6wWotmSZwETCngTbUmQiytc8FmNhP87_ppDtwjSranuHt-QlozafkXpglcxClJKQbgMddaFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
واکنش عراقچی به عهدشکنی جدید آمریکا با وضع تحریم علیه ایران
🔹
ایران تاکنون به تعهدات خود پایبند بوده است؛ برخلاف آنچه از سوی به‌اصطلاح وزیر خزانه‌داری ایالات متحده شاهدیم که با نقض بند ۹ یادداشت تفاهم، تعهدات آمریکا را زیر پا می‌گذارد.
🔹
این نقض، در ادامۀ سایر موارد نقض تعهدات و اقدامات نادرست ایالات متحده صورت گرفته است.
🔹
واقعیت روشن است: تنها راه پایبندی متقابل هر دو طرف به تعهداتشان است.
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/449091" target="_blank">📅 06:03 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449090">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZWkryh15MGG7cpVx87jFn77oo5dN1B0m1-1u3hFX_dP3NC4HGYDHru7V4KXdTANIYZ3uZnca4S3iXKq3Lc8jMTgt7AvtKBpv_1UFD6BJ-5sMa-PQDz5RqjjSH782FKeNEWeQHmUrIp2S20GfMef_BhrmR_MPe8cerWomOnzR-v6hwk3_aGvAwiAqjKyHSczBhe6huvCBe2Yj3PGP9tH5h9U7k-VyYa-hc_HHYMaJOVRnBFZ7fbg5ngedo0C6mDXkRLk_Jac7bwBGoieaKbIL3ycxdfbhprEZCzYoYCimI4nUdrTTPfa_WTflrup8K2XUe7nTbvDipe-w83QP1WEmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیالت راحت آقاجان، ما مراقب هرمز هستیم
🔹
در اوج گرمای طبرسی ۶۴، جایی که غبارِ راه و جمعیتِ زائران چشم را می‌گیرد، ناگهان بویی متفاوت می‌پیچد؛ بوی دریا، بوی نمک و بوی خلیج فارس. این بو از یک موکبِ خاص است. موکبی که خادمانش از یک جزیرۀ مهم آمده‌اند.
🔹
خادمی که در حال تعارف کردن چای و شربت به زائران مراسم رهبر شهید است، با همان صلابتِ مردانِ جنوب می‌گوید: «ما ۱۳ صیاد، همسر و بچه‌های کوچکمان را به خدا سپردیم و آمدیم تا یک پیام بسیار مهم را به رهبر شهیدمان برسانیم.»
🔗
برای شنیدن پیام موکب‌داران هرمزی به رهبر شهید
اینجا
را بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/449090" target="_blank">📅 05:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449088">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yvs5ju8R8Uc1Ru3XJq0Ns2SpO3fLVE9_ptfuTjDD4XI0IWmvQqyJbmwPwLk4wosTYvbVZoGig1ZCInJrhB1j4XgBGXlvRX2vfHKSToj2DFhGQiKgI7W39oIq7rL8AM8Q6S_06Hb6O-LQ-CBwXwyjGHEbZtWrRn1vlaTd8EFouTBgboC9zn582CtaihP_-AMpUPTPZJevN2wGUK_MQ3DW-zJTgWshQRH8ZuS8SkKSR5iB6tQqEHec5UP7aLCFJng53-yyIYV_J67aGSnnlXUJcRiZC6mc6v8omLMlfj9ic4qanvfWsKgYQt2zXWoTPrk7BrOmXXTVftcIlHtBD5ePwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونمایی چین از سلاح مایکروویوی؛ سلاحی که هدفش را بدون اصابت زمین‌گیر می‌کند
🔹
چین از یک سلاح مایکروویوی ۱۰۰ گیگاواتی رونمایی کرده که برای از کار انداختن پهپادها و سامانه‌های الکترونیکی طراحی شده است.
🔹
این سلاح به‌جای انفجار، پالس‌های مایکروویوی فوق‌قدرتمند را به سمت هدف می‌فرستد تا مدارهای الکترونیکی، سامانه‌های ارتباطی و پهپادها را از کار بیندازد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/449088" target="_blank">📅 05:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449087">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kgl5sRwbLlu_Nc-e9MGQdbN4Ja7gqDOvq57AdFYnXMe5Iy_tABQILXADZ_DOc-FHm_g4ONLAnupl2X7_w8yBJV6myPL1HhyYYB-xNq_Pc4UIKRNojQOI4r-upiG5Xz3TbXr-FLUIM_ZK-2MaEwlGFgdFuLc42UcrpxyZJ426XtlPjQzqtIVW07lef5fhJIEWeUr8MB3eq5WnKliyYSzS7WUh70bufVCA45fO30sT6DRnU4GpTnCgyOa-_-Xb2wR5H31SjFzoAoQzoJCX9Ckeby-EDI6unyzxfyw6XJ-atrCkwBYdHtRCh1TIqxlWCuChusNbws_eQHWMBNdiHWHohw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام دختر ویلچری به رهبر شهید رسید
🔹
جمله‌ای که روی بدنۀ کامیون نوشت، از آنِ او نبود. یادگاری کوتاه از دختر ۲۳ ساله‌ای که بیماری و خانه‌نشینی، راهش را به مراسم بسته بود؛ دختری که تنها یک خواهش داشت: «اگر من نمی‌توانم بیایم، تو به جای من سلامم را برسان و بنویس؛ آقا شفاعت کن ما را.»
🔹
به بدنۀ خودرو که می‌رسم، اولین چیزی که به چشم می‌آید نوشته‌هاست. آن‌قدر زیادند که از رنگ ماشین فقط تکه‌هایی کوچک باقی مانده است. هر کس جمله‌ای گذاشته و رفته؛ یکی نوشته «آقا شفاعت کن ما را»، دیگری «شهادتت مبارک» و آن یکی «حلال کن که دیر شناختمت».
🔗
ماجرای جالب این خودرو و دست نوشته‌های روی آن را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/449087" target="_blank">📅 04:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449086">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdQNpM0G5i2b32kR8IetGQWwFY3JelY5bhtLhrYahhWAj2xlDyRaF0WaIquGfhiZMG6LSLGfQQgLCEWuWNNfebZF2HTsJxpr8QLBNMur2fE62th3jJB9IQzODH_Kuv7KngYSs6lcgQDJGSWGqdzcO5DwuxMkCPuQRD49c7XJAaWPhGFXh5RoDuj6GjukqY9Av-2f09bo6gpotTSPZBMv9LJxQO3i8HTq06nzBnx11q8cYxXDKT4kC5rbhB1ipLzkoiSRqOfn-olPs35qdSPLHZ3dodiBuvazm56wgXQoeGIYVfA4e4zVFGhZujKRtxSybagm6yJSkuiWWqKc685IKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شراکت اپل و خالق چت‌جی‌پی‌تی به دادگاه کشید
🔹
اپل با طرح شکایتی در دادگاه فدرال آمریکا، گفت اپن‌ای‌آی اسرار تجاری و اطلاعات محرمانه مرتبط با توسعه سخت‌افزار را سرقت کرده است؛ پرونده‌ای که دو کارمند سابق اپل و مدیر سخت‌افزار اپن‌ای‌آی نیز در آن نام برده شده‌اند.
🔹
اپل گفته اپن‌ای‌آی و استارتاپ «آی‌او پروداکتز» با همکاری دو کارمند سابق این شرکت، به اطلاعات محرمانه مربوط به طراحی سخت‌افزار و محصولات معرفی‌نشده اپل دست یافته‌اند. این شکایت در دادگاه فدرال کالیفرنیا ثبت شده و اپل خواستار توقف استفاده از این اطلاعات و دریافت غرامت شده است.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/449086" target="_blank">📅 04:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449085">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q78pDxJJoh__6fycF5nw8bNCcRRw5j83ER2e56GyZnwiA3r3WcAj7j9bnUEWqMM70-aYpPL14wK4FZcnDdt_R9LFdfKZ5jN2Vbih5YyQUPpbWmeoSi4KZ3bI3Wt1eRhRoVv_U6C8qbGTYi9sids7XoPJPNuIM8s9_9TZ3mQIm2ViGRFeB6F67RBuNbaefDpagwVSpmU5P8a2dZyoygr6HwDqZRzdE0gmoBVJTCrZm-X-m6t178CvGHamT1V6JNTKL--IH8DApdkII1Z0BVpo_-7d-dNUMybL_7WxCxP9fc2xiYkWDctrjiA_rqas2kDRppBjOfvTvl-V3T8Sg4PNkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من داوطلب قتل ترامپ هستم!
🔹
با پوششی از کفن سفید و پلاکاردی کوبنده به صحنه آمده و برای انتقام رهبر شهیدش عزمی راسخ دارد؛ آن‌قدر راسخ که می‌گوید: «من داوطلب قتل ترامپ هستم!»
🔹
حتی اگر آن پلاکارد کاغذی با آن جمله قرمزرنگ لاتین در دستانش نباشد هم، پیامش روشن و واضح است. لباسش تضادی آشکار با بقیه دارد و همین که پا به خیابان‌های شهر می‌گذارد و یا در روزی مثل بدرقه رهبر شهید به صحنه می‌آید، دشمن همه چیز را از وجناتش می‌خواند. او نماینده‌ای از همه مردم ایران است.
🔗
جزئیات هشدار بانوی کفن‌پوش به ترامپ را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/449085" target="_blank">📅 03:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449084">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط رهبری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69921fea5c.mp4?token=nGcggSI-RiIy8C1tsQNsQzGVs3lTQPKvVdTTOCvlw4OfVi0NDCpg2XrPwb57v9oJyN7HP77pv1nxTqFWLNvHdNavUpPYmexs2fmKJ7sCrysCqFPx1PSdyiAdgl7AIVAXi6xH9zWOGib8SKm-YUFusvissneLTkIQKkSAmKXpWG2D0Hk8J6sEDEbTPHY5f8s1zEYFyNBNnMkd4AQzGlXkCGn2plYFxlpAzoqKqzPYCabk2Fqqec-T71jXYCTx9kBuk3-J0Csf0L7FoPWn6qFtAxsL5tSjIDfHBJH3hCnfHCW6YLbviNYyMFoBdk09kHOsIYGm_KpPePd6NxSXrRruMa-JL0aoTOEaiVBqwLSqqHFHvfv73h48hKZisw9ADNTVm-h6cMknwEt5D4PvJ6Dh_RbhecMEnB5X4jUZjK6kskyiFsRsUzR9vY-DDTXH8k_DUWBybLgBMRv1Cfo8At8pwe-B_Mmk1N68K6kP5iVYhElA_IXuBMsmrEGHzhcldh9VvOC7_omdMclHNr9VhttMA9Dt9psdhFYGPIyBHgMwz1hJ5ZAlQ2sb2DN4R5fZXMkV2Gf4mfL0tYmaxwod9Dt4RXww0kFKowd_P4f8zsTnRPn0KW03HQ5USJ4Zz4kOUSuU1YuQgGYkn5-DtKT2FSthDAdlA0P5YWmxCwr0wBUEY34" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69921fea5c.mp4?token=nGcggSI-RiIy8C1tsQNsQzGVs3lTQPKvVdTTOCvlw4OfVi0NDCpg2XrPwb57v9oJyN7HP77pv1nxTqFWLNvHdNavUpPYmexs2fmKJ7sCrysCqFPx1PSdyiAdgl7AIVAXi6xH9zWOGib8SKm-YUFusvissneLTkIQKkSAmKXpWG2D0Hk8J6sEDEbTPHY5f8s1zEYFyNBNnMkd4AQzGlXkCGn2plYFxlpAzoqKqzPYCabk2Fqqec-T71jXYCTx9kBuk3-J0Csf0L7FoPWn6qFtAxsL5tSjIDfHBJH3hCnfHCW6YLbviNYyMFoBdk09kHOsIYGm_KpPePd6NxSXrRruMa-JL0aoTOEaiVBqwLSqqHFHvfv73h48hKZisw9ADNTVm-h6cMknwEt5D4PvJ6Dh_RbhecMEnB5X4jUZjK6kskyiFsRsUzR9vY-DDTXH8k_DUWBybLgBMRv1Cfo8At8pwe-B_Mmk1N68K6kP5iVYhElA_IXuBMsmrEGHzhcldh9VvOC7_omdMclHNr9VhttMA9Dt9psdhFYGPIyBHgMwz1hJ5ZAlQ2sb2DN4R5fZXMkV2Gf4mfL0tYmaxwod9Dt4RXww0kFKowd_P4f8zsTnRPn0KW03HQ5USJ4Zz4kOUSuU1YuQgGYkn5-DtKT2FSthDAdlA0P5YWmxCwr0wBUEY34" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▪️
آن طرف چه خبر؟
@rahbari_plus</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/449084" target="_blank">📅 03:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449077">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EE7yfEPzCn0Hc0uXG_ZgxmHg0Y2Ev3AJnX0_u_LArKpEwLVrHI5qxbc6sV6Nk1Qyq6cQGOoPcgR4ZXDD5vmePpOK9B1rkhbId-pK0_kb6dcFluZGp1dHpXYVUMxQpah47luIEVL93etso0g0Xq0EpDL9nPcu6kaV-cn3IJpaY_AAV5nOZRn4a4Q_S0OnLOw6b-3Q2ZqEluwM3uvHnvaGr3eawt2mii79ZlOX1G5k6pCKHQUf1-WF4b4parCMk1cjFgVAKSPIsjhjb8hiAjj50Jd4ncA6X7SKTq737cXcLpOBI7GO05Cpmcc0HwgFz1AZVL-IrifznMSrFzosBUhkqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OTdVSYX0pJad_br5OeezMmiDUMQwJ4nxZizjvQhL7afqBWnUlA-0Nh8a_qlluklkjo7RC1ngxvJDDqsVXx-p8ljMZMxuFJsJvxQJFNCIodYGQbRmLSpAwkIyYdBZwJmT5GVhepqhVe-JNJHgbltW0n77D1M18FGkM5v68SEoxmqnIk8rYcZYFFyazVmiCvz7aFwDuEXZhbVE4JVO3h3tDz91jc7C1g5bsdfHxRxeigARV4mQzelxYnMFM41hlLJ4-bv6Tzzx5jX2YBKt7AUaFhuPwjvyOIk9HS3CWa__ZN0hMUZWvqaWrJDoKcPrGahnczw7wr9keOdVKrzGgCJUPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tZXeeR8f4HN48DsyRn1u8etaC6ZGQuy-xaJDHOGfr97LJPA9zgt5XIlupk0po4H7KcwdETmzZaMbNGUQyL4vPhuv-PXrYu_BWNKCkETZHTbTi65Zvsu-Vbb7YupqnlBbkaCduLQzrTSL0k6yLO9dRAIlMa0QneFmdRvzC7rfooes8epizMb2J44awfdIn74IL53VTGbhjsqZPZEVs1hbBybHxFgS5nTjvC2xUsp6-eg3h--wUW48YAQ-WfgNoiQOnUBc7gneZ2_Vwsi0lNphxb569EFUifBgSJSh3GYDwfO70Nv6VvpUnk-W8MofspA9E_EOcBLFcBM6clDBeiFnBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/msmXpEIfwVvcStJla5cFdjfb-8LgIsn7yeO-rgQGnF_AICruNweEzC2s2JA_eaZCfVQJ6mZHfaiKUupctZMHjKWvAL4F0uhp4H8VRByfEPkxgmRw-WmjWLR1I4vkv8zKGd7s8Th55JhgHzwlygQLb4gsYjc39pF5MCxIvwMptcwRxEaDwUUo5LsSANZbYMw_KWXPDMf9h94_z7b7gnMefyafRpNaAzJZjTQL20mVaVo_cKWQiTIgwvIk6DA58F9Vg1rWRRHFC_V2OEwPGZ7Tl8CYCbysN4jhCK00T7Nokl8rCb8_vhDDOY3cLLX5W0J2-TQOHywhs6b1McdsBBgnXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PmPkK5z5Cr6qKyCtH13tLDGhH0EQp64sp_BfoWKk4h9WUqtQPrOIckXGTQg4clrowd_bFNI9LJp3zTuwoxPV0MGHGnjJi1OvJ1UtT74goOghgLZYkmypt5utcPpxSGNpuk-jlELzq9yyfe6NHJ5nW0LzXxMJcbPi3gsAsBarMEP7RVQ4j_QPIFV3QttfhW7PptHZ69kpgOZ9Hi--0-ZNIF85-iF41L67wpyLz6o-CHLf1b4SIyzCeeRgNIl-YYJlGKpB5seSl1972vSCzPzPxUH_gQqxoDI0Ic1vOZVQh-TtmuqEN76Y_WALZWMibLNtsV_hsPqebCUoMPV0YGSQuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M5SZckhCz1RG4uHXVo5EsIIXOpv6qE-kRq9-IdvcTsbichww-sEqLDsCnmzo546v4ZxLKyxe0CRaHT_Kbz0MxCLkhKl8Rsy3Dz6DbGfuyTxREW85Dmj0XleX9YjhW-xmu8wm6vl3Jh4i_vvg0JHqT2SSMXpyjenohu7dZIBg9qHlOeKo5_tD9AIv2v8xTI7Q005HhMH4inJbBl6xiibsz6tXzVNFjjlQQLBiCLFFStRget6FZkSmcFQc_iyjkAc6zB6k45JS2rhhFKpp_GRrLBEbnYefO3n5o0EqXwVwd4_Y91blo-chJFerl0f0a9tydP9TnLnRI7d6QQ-wqKcOJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UQGdSGRyLa5vLzfqzpROFFS3QHmRnsdagk-ZTLiQqZt8i_0npme9TGBqkuzb2nFVw-zIgRU0DCoBnYhY8ujdQuc8wJvu-o4zqLhvE8f3m9kxfRTsr_ohJTp0cgoKlLV0Ze2NWYm_DTWjLrDr_LIN4W3eP2E5OzpxCDSTo_h0yVDDhxH6i1ZKKbsZafXG6Yyj1ChcQAq53Qj3vE_ikat4DRWkU1qljXIzvx0qPFL3cXnrECHDShHAe6TFIcGfkbdPIjNq-SH0tPQBtlk2fCLVdtOmQmfdGfLjhilzfrtKNnSNUYeroTpJtXh8grafkaGnksZZqYo07C-nZ7bo7IdZOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بزرگداشت رهبر شهید در حرم امام رضا(ع)
عکس:
حدیث فقیری
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/449077" target="_blank">📅 03:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449076">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8la7XxIenlB_X68wBdzgf7oUDcB2JJCYbX2N4xnwJONTksCJzxVM87aLlkH1SZ9fZCpcLDtM7CtwPNUv6w71rQDdGO5Bd_UkhU4jNqdsBlX74UlNBoOYOAA0lb6knNhJQOYYm8v_2p-C6ydvhceQiLr-DaEiDK6LOh4Wd_gOrdDwqN_nKz3-bm_8lgsIDjS4D-9WDa9EQxEFg7qnGpba-VfVIB_Aqqrn247njaE5LJXtcYj1Tu9-nb7QOFF88nhUEdhL05sRXpLZozHfGZB6IXosmhTeaNzYckDiOpdoLfNBr-GR1e_9RPFIN2289TQIpm0ZlQW0Xbg2boImFQt8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب‌الله عراق: تشییع حماسی امام خامنه‌ای یک همه‌پرسی در عراق بود
🔹
دبیرکل حزب‌الله عراق: ملت سرافراز عراق در مراسم تاریخی و باشکوه تشییع پیکر امام‌مان هیچ تردیدی باقی نگذاشت و ثابت کرد که ملت مقاومت و جهاد است.
🔹
آن حضور میلیونی، در واقع همه‌پرسی بزرگی بود که در آن مردم اصیل عراق بار دیگر حمایت خود از مقاومت اسلامی و سلاح مقدس آن اعلام و بر آن تأکید کردند.
🔹
از همه رهبران سیاسی و مسئولان دولتی می‌خواهیم که به خواست ملت سرافراز عراق، یعنی ملت مقاومت و جهاد، احترام بگذارند و از همراهی با طرح‌ها و پروژه‌های استکباری یا همسو شدن با برنامه‌ها و اهداف شوم آنها به‌شدت پرهیز کنند.
🔹
همچنین هشدار می‌دهیم که اگر از مسیر درست منحرف شوند، ملت عراق سخن آخر را خواهد گفت و آن زمان، پشیمانی هیچ سودی نخواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/449076" target="_blank">📅 02:56 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449075">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QkJAuPTAFH1YlFlS9uGr4UEPWotcfrSxU8kNwBl3mqXnwkjVasrN9rNkxu70rpXC0G0IIQYVa0NpWxYJdnm19y_dsjaSjeLHCmBtDXQlukiYlZJ-iWvr0O5ZBte3NcB2EKAX-wp1Pjs1WAVESJnoXbCC2EVus47QXaZkjB5DfFgXi8w03nxlLho0fukJwtuGAUJjaYyUjcGziRz9hmEoHIPAVR6zM23GjD1n5I69iE3OQRvpkXZ6fg2tenB0OYYCYZkYWWhmAJIY7tshI8j7bpGgOo80rsI5u8rAufT4SNkg-5yGeFSczglbMw-_oVFqLdyvaT16i_B4BC0JQNAL5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین جملۀ خصوصی رهبر شهید به یک جانباز
🔹
روی ویلچر، مردی نشسته که راه‌رفتن را سال‌هاست از یاد برده؛ «محمدرضا مرادی»، جانباز سال ۱۳۶۱ که در جنگ تحمیلی هر دو پای خود را جا گذاشته و حالا در شصت سالگی، با چشمانی بارانی و تکیه بر دست‌های کوچک نوه‌اش، برای بدرقۀ فرمانده‌اش آمده است.
🔹
مرادی به خاطره‌ای دور در سال ۱۳۹۵ نقب می‌زند؛ خاطره ای از ملاقات خصوصی جانبازها با رهبر شهید. «بعد از یک ملاقات عمومی با رهبر شهید ایشان خودشان گفتند می‌خواهم بچه‌های جانباز را خصوصی ببینم. آمدند؛ صمیمی و بی‌تکلف. تک‌تک ما را در آغوش گرفتند. با اینکه پا نداشتم، آقا خم شدند و مرا محکم بغل کردند.
وقتی نزدیک گوشم رسیدند، گفتند:..»
🔗
آن روز رهبر انقلاب در گوش این جانباز چه گفتند؟
اینجا
را بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/449075" target="_blank">📅 02:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449074">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9zbBYOHDa2AqgvU0QF90EqEp_vv8hlCBpt2RWP0IS7Gj4871EK9D2YUVEZTDxYFpKVqmD1AOeEl5Hynv_emU6Je0_HRxJaysX8B6QbbyaCRuBusoN6P3ZrRhKncU-jwObpR0uW3URSGspv4TKOdmTr-8a7qCXVEDG_hq8Vbbwm_lLZyWPqngklSMMYqI83h7rgRRcoSqSGU_qVV9NGkJhihZnrpgN545KsbAncI36ZhfEinInHxlI7Gao4A2Q2-pcz5IQfysiYXaeejKxbgyrAN6fF2QthM1HHxy7SQf-d9O17gB89mwIqpr7qNEKmOXksF0jtaoz6O7CnKrmdqng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتحادیۀ اروپا: اعتیادآور بودن اینستاگرام برای متا گران تمام می‌شود
🔹
اتحادیۀ اروپا به متا هشدار داد درصورت تغییر ندادن قابلیت‌های اعتیادآور اینستاگرام و فیسبوک، با جریمه‌های سنگین روبه‌رو خواهد شد.
🔹
رگولاتورهای اروپایی معتقدند قابلیت‌هایی مانند پیشنهادهای شخصی‌سازی‌شده، پخش خودکار و اسکرول بی‌نهایت کاربران، به‌ویژه نوجوانان را برای مدت طولانی درگیر محتوا نگه می‌دارد و می‌تواند به استفاده افراطی و اعتیادآور از این پلتفرم‌ها منجر شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/449074" target="_blank">📅 02:10 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449073">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
حملۀ هوایی رژیم صهیونیستی به جنوب لبنان
🔹
منابع خبری از حملۀ جنگنده‌های اسرائیلی به مناطقی از جنوب لبنان گزارش می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/449073" target="_blank">📅 01:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449064">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bDPGzE4NcoC2bDXcABmye2SX3mg8ca3Lqob8cS631N2lRDk8U7EKLc0cFA1jcUudo7c8K0JE_ypvpPbWkg2kP06TR6MFvGV4rhUFghnenwtZcursBDVw6Igs-4yKU7rispiQkahfNxIK5HXmaopdR5P5JIvZpznl8Ktc3vACzjVudwgFacGDSBcvVhA36LybXOPWP91INk_WGsmUbdtZMHK3lh7hg1UlCClASYaCq6uUwTCVJWYj0uVMajU22BZ3CUMiJCFB02wqDKLbH5HZOIYr1WKLfPUjlJ488AD6svR1b9HUMk_vdXvHAzYEpOfSgb1Gr5XCoZXFcUrN_v2raA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NDE-JRw35teD_4auOZMGp9Bslys-pyAMRdgNdqqfrIyRvtX3Ldjde_rhiARe4Ozl2llCyv_A3Kd4P2lqjszpiSK5-Lg_h376YLoKQlDjmBBzvj2VGed2k_T4ZI0L8fzjfH6YNTd6wtz9OrCCZPta5mXSkncwGsmQTObREUjl939s7VKfF7eWzokrgJXULDWFhj9eG_esGRF2wN-8bKvpbFuXTPKHQCIrwmiTDzPPZQKoV4r9fdnL_k3rJqyxflyK5lZewXouQMEZu7DKEg1U5cfpnE5H8wnV0XWZZP24CmocK7wKMP7Svskgvz1sFyFV25pMVEgsHgzrarRd5V04yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/riI2UK-GZgw8dnwNYo5ljPUql9GlWWYf7EQUhUkKLyDwe9BMxZooocLzvK6imJrwdVdqd7UXAVhbW4QkR6RRf5k71-7oYSo52Xf_bc71-pjKdwXhZznk--5rXjepFvVO-BAyJ4XWIjX2UqRjHzxOtM3IiCGqlhUFE8bwUJCVw3cT1YIDua_bQMsVa5_5W1vqhq8ZrgI4XZOGy_OQkzTPW1k5sz3Qde5wsog7pVR7r_PRnPOKWo3rV2ycZYboK3z26mqqdK5d8NNKCUg9izdPFf8lA42p_mxKX-K2mEbuuG8A5ZYuAKxPMSAg4z-7mNyWMJkeT0FNoijap8vBMsasCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YjjHw-UJdgiI9I2kx7zY2lym9Kdzfjk9pH4uQcydkwXXuuBRTHMI7ZQNwM3TdBukvvVG9yhI4dRvcgIVrFKHASZdRBZ4yEz9_XpzPLAiDwYTKEvVyKfMfylgto794JaIW0nNSJazyHLdJwAKl7G6eJpZf46POzI7CtgUlAloULYek2SUEjBG9676umuT3Y1gLiVPnpVDAQe7WQqQVddG5wuD9fEl6EmwD1_8OWV0CDQAWg4oB5hwDJpbeKC_XnkckITT-cs_XJqnifHFhJYs9mrw00jPh55qZsOAnoiR3TFMevViB8ed5Y4kohhtWs6-HFRi4GaH05vFqSFbeU68DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kTiqOKw9VVE_yn09QGFkNgcXwahKRKUafJGkvVie4WD4Qyt4jYY0dLS68doxgFFdFJUk9JqzF_UvrHHvUq6on4WdxPg8dAke-TkTrVzfU_zMw1ifbzXjaY2gF5J2BFjXmB4irt79lhDhYk4LcwWP8UfqZVSRxwCF7WiBHPnPjmC_ju-eUxcNZR0CeQzw33eXkJV7nrZ_1K6-_DXxRiU9yYCJvwHBnKWGTCtxR2vVoUTpaFEYgzSRM1YfFK-QWAqyqK2ysTJm_eW8h7nkFybyTzxch0Gla3SDsJXVci1XgHgJLi9uYy-WisDNqQ-DdeYjNwposmow25hRbB5Tfrx2Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RL5_nukWlnO6Y-_T7OAcztSR8IJCH3Ipbj2K23_dWC6FPdO7mVp6TVq_r8Wc2iA_JBd6SIWFhUJOAl180pLBiyyRI3u5i_HKvwbwX7DtE31XNSmdnuMsfsRh-FWNxC5Xf0sHFnUxh4FaXeOeYuQl00kSvV6tBSrg1KE0ENMX4CYed6bQusI7Sk-42MJgoSfWVifg8_CsJFnC2CEW-VyyrucT5dCKsMYRYnTei2Tpn7HHiz_DtpuJJEB2T81LEngiuipXCq-ptsfSJWyfun1SrkNXd_fYMwJLerMUxoT134_xKWj70ZOfBfqiPmWCoM-p885UBRMOJ5qnwKLk75PNVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/McXhIioZaGQ9q8G0-diqz3LI6cRL_x4tESJnHd3ghXo-KThWlXnNdEvgp4U6Jg80NGiGaY7maXs37Oxs-t2ZA4drcAwoa82CnuLxyON5g7IyjuvQ2HVoHds1tiEeJp_vMlZRNcPXEj2L_r0yyZTUUSnTKMULP_v1YA7_6-J--Nqcuyqsk_tYrTYPpKqN40wDQsXeZXqZF-U_wYa6eJ7iQA-Zmu4WfJC5CEaVEHpH9el3pAwfQOAUyKR89mpVzFjQXi8hAWj0qz8hosVwXPncF11ZARaP6K1CybXJ4bHXc4dCRKY0JpxlnHCGrrDQDkZTc-MsXqIpBnSpBwNEWFwtTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H76NEonCKAO_VXpUXfvyUsbl867HNYNuiaHNfddU6oN2CdwsCjW78U-JC2QPor_CVpquhIyFOGwzRqL7aBJbnuj9wDXSg6N-3yab_wRO_oDVLpy50zfteHkNu3Ivv4zZy9b-6UMwwG-nErwJFdlfKWUbgedn8_B7VUoV5n2Rr_S6KTrS5XKg84ZM5TNGbPEX0E0Bq4BUM9Jshc6LJ78KvhxNnCeThbz_B01uQ8sjzo-BXW-KXyzoa3Tt-SapPdMgVFgCOF6zAERowpbWd8oU009McMT9sj6HbyOLBXt7Gc6qA8cWyJWiOe6XQUtyecBlehTd-51_GTYEcSDCFzXWZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iopwe5y7uziMlwFNpxwHWKDBPFzmaLpfNx0RSYy_VrSZaPzOG-fkIP9lWMX43SCbQ-fNZWUMAgofo37pDVy8w3xi7QCe_Y9yF-jHNDrEKTr9qXWNUYEN8Bdh6o-xtPsXE_au3PpI0c6rY1VmC8AoPeG7kCVbgr7DvLVFssFvkciGolOaIUa_MsArxMQzemuO4pgnmYOv_mtMGUqc1oBAekf9nyFwfHrdl3qHJo4yHAnMLeD3_r6aT63Z-she95MgMOh9F0JUh1_nmLXZyBgzcsinxL3y_k_LbQ3vwDacBrKlaNUEz-kxz7unng7NZCw6g2jG2pP71k90TZwQv5zIwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حال‌وهوای مزار مطهر رهبر شهید انقلاب در رواق دارالذکر حرم رضوی
@Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/449064" target="_blank">📅 01:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449063">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f04c77390.mp4?token=BXJZdtw8P58M_cvlV5eRN9HpU8sNjRhaP0i96_C0ko-5z-h-n6KNNLNwEn0E-WaO2lY6MwvK4ZYQ_ThXvmR-6EYaL_Ias8I2ASRYvJYmHah5Y-rzb4c99OFG2DF-66cA9h6qPUluDGj7HE9fwvFdH-wsTGFepwKC00CZK7bEniAhyWGD1_59ek6Foh_MNox2A_U2rUbdeayAiotfI7jyOOgBHzI8D_5Gu8iaGp3JLsHeQytNpkM58nh5-rQyuEhmd4WLR2FG_ihD4VdGSoM4mKr67rS8pWxHmrx4xAexaA0QCVtHvZp15jewBGeBg56WvtTNTxkZg1scN2XDczfX5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f04c77390.mp4?token=BXJZdtw8P58M_cvlV5eRN9HpU8sNjRhaP0i96_C0ko-5z-h-n6KNNLNwEn0E-WaO2lY6MwvK4ZYQ_ThXvmR-6EYaL_Ias8I2ASRYvJYmHah5Y-rzb4c99OFG2DF-66cA9h6qPUluDGj7HE9fwvFdH-wsTGFepwKC00CZK7bEniAhyWGD1_59ek6Foh_MNox2A_U2rUbdeayAiotfI7jyOOgBHzI8D_5Gu8iaGp3JLsHeQytNpkM58nh5-rQyuEhmd4WLR2FG_ihD4VdGSoM4mKr67rS8pWxHmrx4xAexaA0QCVtHvZp15jewBGeBg56WvtTNTxkZg1scN2XDczfX5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خون‌خواهی قمی‌ها به شب ۱۳۲ رسید
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/449063" target="_blank">📅 01:34 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449062">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">نگرانی هم‌حزبی‌های ترامپ از تنش‌‌آفرینی‌های او با ایران
🔹
اقدامات و اظهارات تنش‌آفرین ترامپ، دربارۀ ایران نگرانی‌های هم‌حزبی‌های او را به‌همراه داشته است.
🔹
رسانه‌های آمریکا گزارش داده‌اند که اعضای حزب جمهوری‌خواه واهمه دارند که ترک میز مذاکره و بازگشت به درگیری‌ها با ایران می‌تواند به افزایش سرسام‌آور قیمت بنزین شده و ضربۀ نهایی را به این حزب در انتخابات میان‌دوره‌ای کنگره وارد کند.
🔹
یک نماینده جمهوری‌خواه در کنگرۀ آمریکا که اشاره‌ای به نام او نشده گفته که تداوم جنگ با ایران نه‌تنها قیمت نفت را بالا می‌برد، بلکه «ضربۀ مهلکی به ادعای مدیریت و کفایت کلی دولت ترامپ» وارد خواهد کرد.
🔹
او در ادامه پرسید: «منظورم این است که ترامپ واقعاً دارد چه کار می‌کند؟ چرا اوضاع این‌قدر بد پیش می‌رود؟ و آیا اصلاً نقشه مشخصی برای بیرون آمدن از این وضعیت وجود دارد؟»
🔹
یک نمایندۀ دیگر جمهوری‌خواه نیز که خواست نامش فاش نشود نیز گفت: «واضح است که آرزوی همۀ ما پایان سریع این جنگ است.»
🔹
او تاکید کرد که از سرگیری درگیری‌ها آسیب سیاسی جدی به حزب وارد خواهد کرد: «اکثریت ما در کنگره، به خصوص جمهوری‌خواهان، نیاز داریم که او هر چه زودتر کار را تمام کند. این وضعیت از نظر سیاسی آسیب‌رسان است.»
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/449062" target="_blank">📅 01:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449061">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">حملۀ پهپادی رژیم صهیونیستی به خانه‌های مسکونی در غزه
🔹
المیادین: پهپادهای اسرائیلی به‌شدت به سمت خانه‌های شهروندان در محله‌های الشجاعیه و الطفاح در شرق شهر غزه شلیک کردند.
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/449061" target="_blank">📅 01:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449059">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1pg1V67FEltxUFkoYYXBkahwPWek3OM_Ruwo9OYNea9LyXMIqChq25KOfKfFOgHJQKBqHA8K_ZKvmthYldVu6b4Zuq6B-FQi1Xk5ad5rRlHc8g4RIBpmwlfGUljMGueaZUf-57bI-qF_h9QRGj66k9mHG3lZhWuSpH4AQsz5juaExkK9yxSUNZZJjXxKtLf2OAyqd2C5SjBINctf1kGIUmH5ioMb_zI173IyO48hsT5rZWGJpQVDnYS-hISjy7bKviDDckIizMoifRMYTpTt0aqenS_p3i5hr9M0JOFalc6tF42JHsn7SJdJnTsF061jBI-bkQkcaA9YXBrrYGbxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
واکنش معاون وزارت خارجه به نقش امارات در تجاوز آمریکا به ایران
🔹
غریب‌آبادی: وزارت بازرگانی آمریکا سند جدیدی را منتشر کرده: تسهیل مقررات کنترل صادرات و ارتقای جایگاه صادراتی به امارات به پاس حمایت آن از تجاوز نظامی علیه ایران.
🔹
این اعتراف رسمی واشنگتن و سند رسوایی ابوظبی، مسئولیت بین‌المللی و آثار حقوقی مستقیمی دارد. امارات عربی متحده باید پاسخگو باشد.
@Farsna</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/449059" target="_blank">📅 00:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449050">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ljAL-GKNmUv7qYNDRY2NgbNVT3lGRk1fX81KJ1c8imPyqxeA0zF4L9752RBgnJiQTRMWkPTryjZ0s7jdQh7vfPsl0ahKOvWGUNKuZp-2_uvD8KJhoksl9Ow4QFNr-ejFoVp7__Eli5PxVs65HKiHs5j4shUKL2JPxy-cYBIeLbpfHs2ug98ORQeHUww1o4ctM1wVboqsPG32JIyOJYMljtwA_vV6jcIdEDbirQlBu7k9CyMOQuQCdJhPzSRjrK1XkNw1gPTRiKwLx5iVfjRvmg3Gdcv_NqRFHzplAprB5wJOkUKF4TB1McT2nvJERKOWd3MyV8prov20JVhYiS7z0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nRaggFBeaFhUYVjNOtu3O6PbnlZiJ4JPa0DHiVa3FrbEQyvdzb0bkEWSrcn0R2Vfh-nsaNyqgOeqZnc_rtcsiUqgPyxeHTeEvaeqb3oVj4Jl0pe7L3CFA2HMY_QaqtaLWhX185cFW-VA7fgDjlrB_Pj4FKWjAsVX2ore3v2OghRIXWOnVe3U_-k1k-8_xANFhctvfrW86KZtzF6xtEkmYqCCZrlWaPX5pjK_fQ4xQIHQ1JjnlOumRYHXYStBWbVOb8chi3cWu_motz2IhI3aDAj8Jylu2ORcmO0QzesO-ydM1FAdXBLVN5DIpFlJondg4F5zZuTZDBAjy5D_euu86A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fOcDlfccc9t1ulVHBInSTt6b-Q0AI3Bh0S7b6_r_xH-YSaTTFVTkl_KDVcbxccEnZdXn5gPAeQ2KThXQp7eK4D6GmuXNwuSOCKo7l8TW1oYdAqftEOdprmYi1LvDNGKb7hLCNzga1EDZTysuDHDFkVyAOQe8Ur-3JI6kpSPLxSTv0N3nZZfc_Cd2uO4N_vdC74t9Ecjw0-Ab8PTo1xlYjdvKriqtGIcVFhOIlz9Q2CRhgdnyDa2eFXKQ7IiikxaaWuC3qi1H3R9QOg1CxccB5w3okb3MtF0t9Wo-Nl59tkk6Mtl8crMMZhLPxQlOp_eFirxwoyeEya5F5dUVKrj6dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EUFB00EhWtS1a2xJ1P8mrmBOhBfMMcmht3w8fBdfqfzXtB7khcfLfKwRQM2o7wTAq65qyAS0fJ8sx9SG50CvhU4_EhlO4o3W2RuiTKADzI7YuGm-IETm3B3vhfVy5jRPh8A3R8NF5qFmQgmW6Ec1xRDJ-vgO8ngSkW_GivL-wjOIbgSxAgQxZozyeVSCEpvcECJLK-D-LFiTC7eBB414z4rtd0a1fjqpipoik57bsOvzKu9YSC9Hj9yT4WlJsksa3zloM2l-p6otb400ytzm5x1ew0pTKO30Eurgq3NWFcwgjJlDA9tNbELZ9v49VRkY-fnw9op4ckTmJu0x_0bf_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rXRpFTmZtsp1Zix2Na-RVzb9idzo4xwBc3ahhFjq8znKkj8ucX2d4dv_1jcE2_25E2DN0QUcq_ZBBNHwPaD8KmQzszz-kRaUAgm-q-gC_NcYS1PXi7YXHyODVmEjHCKzWIyLfAV7UikywUVShVkBUowF0DWfrBx7xb2xa079XVREmhEOiRIxMcZEV_8-H8dF28iI0wV0SV0lSvYI6xCQKn9WwPkPHNPj8ZfMhwtc99KwMAkEIaOTOvqKu1QRnIkutAvS4qOT031ZdpOiobIi1XUCO0cCC53ibqKrDN3OreMTfcW9H5Fmlq34HmpCjHV3qpYF8lNnYm7L8Kj7raAqsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HlCRQHgRC7C77-Myl_v6uZoXz4XoFWdVU7ytqdAhDSuApg8rFDLsQVidRV7nUcsk3SYSJrvKYnJPHab93PCy-KlO9-tAGlZH29b8QbrVtWPPoroYMSos7jRJw3W1KepT10yHPslqd38a3wHjH9UtzOO8myfufA529_XQiuH5_0EDGXZShHHAOdfq4V2y6B26Mg1H2X5UnqB98T2FG6omcbENa1Do6g63D5Qn8AnTS5MetOzFoi06rpPTcqw6T9Gu2ZygkOpzZFbO0VKVIe8zWwxyMC8sro5_aa9tVr_qkbg8h0SACf1-wigcqKwb0HVWkQI-mtZBzoyb5PsAnTOLSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nzzn1EXXe8cuJbgUsDB7of-8jRZNkql7X5TE-yqhNVglb6PFqSRgX0Q7McvEYqMd8eJCj9cPlCMUQ4AjMO-lWjy-KIWcQpl6oHA3R1UHBLbGgibeOY7uMYDetjAOGuPAAe24FlE94-X7VelozmQgw6SGRf10QStInPmgoWFX-sDLQGWFmShrd14VFfScklDhdcTA0IwjgpiO1dxp2bH6iwyq4o2h5IP5Hij_knXMz2xmAYE1NndwLsEZv8frAVMecNDrfHd4iZZUjEKOUU67b8uWK-04CpNeMELMdAcNI87RQ1NFIUJSkM_Ot4Cq7ZssxJ9ADp2NY36rA4_vKvqMWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f3RjtoHNyx8-fpfKWdOhPWRNDZdDgTiVQpyLvnrjj97TS0iOnd-F7BIpBThTnykGiIM9fYYfHkE_EwzSNohikEeQZuCj1DScP6wp_ssxWdVPd6ufr6lHV9jzneaegP21dyR8FC04r1vQVqcWcNGajt-lU29hzYrVqH4r8wjSeXjQ7eTxSN_1ceXzLlIrWShFuQB1Zi5Q_vGT_amQk8vh07drMETUvadRrJfXJCDL8SLGYoFwtaVl7APhfgDtttLComLpNHlqnzOPE_F7fVUAQsALM_1p0k4lYxnZBUcbxRShigD-PE3wmHP05lUdv8CrwBA8WocI6s7y8dStRKwc6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hoSfux0N0KbMWqeSq4H26HPq97lVlztCw16OMKhwt918kLOygys4BL4zLdogJF-sg0qHkOkkOI2zbp4xSPodDqX-DZSSBnGV7QtopM89M84roQuv_VBeql160kJbe7qL92HHV5iFYz2gtPp0yVOHbylzyTViV0ccF7s14x15JB-P1E0l7APsHytHnYiKqXhLQy0ggeddXacqi0HnhZQb0Z48lyATyZfDD0tjrAfvqEdihWZ7F-auHF0vhZeNWN3x6pg60NOkAoSSJmecc7fgfEjBwT_cjh6lIed_RNKD0-X5TdHhZlOiQitHA8L3BOzMg9PEQKSVlThe05nZBdVwcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
شام‌غریبان امام شهید در بوشهر
عکس:
احمدرضا مجیدی
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/449050" target="_blank">📅 00:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449045">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HwNQdsoVnXdl8Hvi3ukUXWF0oXLIYZ50Ny6PzNq3yw_qptfM9iQamKDo63jfJZaX8OvTPVgV0gGP047vHLq44ticiNeue6zpFff-e3dT7b5UQbY2dJ9qoGBJPDDDUlLxsOq53SRmoxVUpoTfTLVoVLe0naFU49x3IR7DwB8pgEN4Hg7jajg5OmUxjt7w6AbAh1FCfUk2Iaima48sLTDR1CC2rlZDF6omtNF0ZDng7f2a9aZ6pMrRo9DCvfBKN-hfCdfNqv8ZtUsv2d0OMDy_uaRyEe93IOKq5Vp7JI9nCyllCxy75HRIPUFklIXeQ7Dnpd-Pf3R23ZWDFe1xLJrv9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LF1HW5ZQyMONu5Q6-9nHCK-_2o8MUXmnz1Fb5DDNrMqSyB1xTXCXIyhXyTyUxbI3q674ym2E-OPGrY0YXvGEHj7JR8zTRV59bT17pd5WqaNBUbfYiqW8NZoWORFnvmCpt-Mhk7wYA19nyjmFy0WoiACOeFCWVCeDfPG7UqMclxpUxCsFcXUilA94EaZYdRGsLthyuqaBDPSxPEqkPKppYriY6IzuBavCJNNYc7yF6cceCpPdoRWQlXP4eMtgksIPyVkJYJObw3kicWMU-R-uFUXHms89P6RbON5XgacPZvPLOnL6OJe4yBbwRonDSdF3A8INkHjD54PhbRQsKUcQ1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YQS468UF7A9ztv7Jl_0WWlaUcrsOtka3lVXFjP7uB6wOnFilUjo0rGAtWdaYtQEZdfFA_t6XAAGAymRyrp-A1Baw_s3eprpqc8DrP56_qcggar5evvQQnLJg6YP-vEDFBeN5poXXUdDdhW83PmFZaraWVvD3KB2z8ZQ5b3JDXiBY-HMacxO3dkPuXIV74JqFiJfc-mqmvipVzkz29aMBCxL5mRjfFsLqNKt72F05QN1eFriOADQ1C8qmxTwwTCgWRUGJCps2ZMPKFc0G-HjL99WQVnC6OzhYix63E_CU_ixjGOXc7WTzHNluFZIbNQwrdO7S2kFnFLxevG7wH868Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aQG4giGrPze9Q2ivSFA8t4fiFyCoVpIRcD3XQJfcNzi5zaiYUgPv6zWek-kCQ_MO59Id2-1n_Bl_1DSpb1fX0X1lG0SLjON9wJkGv7L6Jltho7_ppTwr6aGQvhmqOHcgwtSzxDA3gGHfSuBDPCqsFmYgWOd_S4zXVS61w6_FiXoZimuFWU1nKtNnf-6HSjOP6JKNkzDosKHmfd3yZ30BWbyQVvQFblO1uJcd4uVbQZUP5TyIuaXGBVbigR_wMJOZADvM0_IuU9srN-KAs1vIU0miseFviK9fGBxgdMI6aoRA-I7uFkoTvhATRmHHPCnpJp4c3F-TYokoKyBjuCqTmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lt1ZeCd16wnPP2gedl3cuc4g7LRGEaiq_Yegth1sHJdOGUByP4ap5KkyFOOUw0RJOQyuVOfhNnYPhD0-8hvzUNkAkmkzQoNAuh7NUowxvIwXiUHVNu4fMDCb83EnvLLk2--00eHgzSH7ro7eOMFyRiv_r8WGAwH2g26m4fGM6svXOs8He54hhM1TwzwK6kRazNSnjE9BUBGlxbYePqCyoZH7whoxbl6HTxKuElrEeg7AfvGWOw-YIGi9bKm37UWLdNjRH1y21_WZogNBEQMbVEe7UCV_6aJe9XFaGKT3eTBSYN6PuOhSkfxlhBsGsDPI35c44QwNdNS6q0uye1747g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | شنبه ۲۰ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/449045" target="_blank">📅 00:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449038">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NlLuHnzGzbud3eGUWyjK1ZutDYJ6lu2dWCby78Cl6l-GEh91pE-vCceYRJLULuo3QtGY41KWjTpJnP6hxT68mScwfSnWWaOBLwHbBEmqN8zNgYQ4TUMpEddQ8Gc1opf9O4hnhWW4q_2lDf5xJd0U9du46Ih2aI-jr3QPwcoRfak4s29Mm_jxIEVOixrWRCsw85yqn-tcey_Q404zZW1OdhzVnf-5IClp0SmNUYnw0JA_KT9rl3OFCAc3IVKuFc0sTM1ww07Wj5RBVvCa7YIscfLohrGOxbfABd9FbiBgxbYggV3u3U0xdS3QLHDvMy97ppQbqvW0gXeisOf5TMr3KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oF0TCklrMpLD2RJMCh-FS6S69rtMYD4XMQ5-UrJRwIMAjRlEyb9j7ppReyl723tG_hqGhBT9d-POoCbnbl4vOZPTySpBq6f1NV4yW4BCvL50JIimLI92T2RTSnLqHhkDk7FjtHO2mH2dKttsU-8k8YP2DkfPT7LhHPqmrVuPBCJadi_l3CoztQuXPT2EB172obgDY9jAyyaC8LBgdSbyMc_0cUitXHX3_ymbnH_pS_B9glciKNZWGl9lG7HNSWQiju5EMitOfRPE0-PlJdpHWf-uDHjFXCZ16Yzh4KoEKzPZojE85MrDv7GduJhPFaqk85AMIqklS322_DKoeoE2nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Js4xYb9EnbvFNtQNM0D5XZ9AdXKPWBsyvC8yHjFTsctbrkPeQG9RR65XC1Vd7Lj6rc4mU-mxJkUTRx6WIV49ucwmRoON-ncED5a55JKd77GS5JTsuPtH4usHk0JL7hrAk4UockJwfXTvijsLaI-agwZPXUW-36qnEgcSXdNM5DETFPuXPlItrZWlQzI9-VIAAjxw52RGykMCPg3RythUowVzFhobiOvHzd7_vggInqVcj8JCZ3tQ05gTwN51euHh7PScdk7Z-Eq3XzuUXnx6M-02A36FhHhoPNhpJfcNODRYCTzTLLgo5m_vBbq88zi4E1pLR4xfnvjeQeCZcxlu0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WwRR71ILW6B331Zql-CKGCDkn8AyP-2sSRRWI0fhc7gEP7HByRS7JZAP_kHEiLZ3w2CkDR3lwX8zqRD1DnjlgWmFhCq_cM8cpgfbU17xrOQ3lYsWgwdKJYXvmkawee88tT2S0flgije8y-ZYRKVAgblajZhxzf2rH5QbB05rB7jwToiJLmApkJr8tZo6sO16HVKfHKXRozgyS9xmgUiO6zkxYRMZrKQsD5CC4DspN5Xk8ABiAsf9T9KgZb2wSt9ZL1NbojCO07ZvG3BsjIcMyDJ5KN58C2Zm3DBOeaJVHshvrKIhovyP3kHebvueGQEFgAQB4W-3pLEIeHDFMUIHiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pfoHXJU128k23aAx5CMdUeBKE6KBm9XZVvLInKQ9MeGlGujTSYoJAd7hkOA0hu6_Q-B_4J3nyFYDqz70qDCH0Ei0VoM3mEx8WNhLC_vxaRURk5AsRL1BdKAnCwB97AeXhz1p9kw2OoiFnm1gB9nNWQT6xojR_CO4TvIgOFQ2nBNab2XTkzMZY6Vmg4eLwGVOxhNoTQeJHBpk_v0uK-z-5W_Hu3p4K5ZlFgJ00XE9fMsQRC-JgXiFmn70x1PyutVE8iQLoJAzCKzkAszjMxsUkVSuKsOA53qqVGx5yEfWpvIPE56HIPQlO3QyFL7xZ9R_n0eOJPo9L2OlVScf3pKHYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F-EdKNmNpgcdvzk1ArrUaWCuYzLCthLYki8YkOAYGTzpAvFxghM87u-g1FnCeALlKW8e4PyZHCIqi6U93lkWl5Q5tBVmNkg7jxbVEPRTgRcnuNMM8kye40sAbqqYbbKyse07eK2VpyNhDytEuWLuiX_GJB0oXlZgWw2ROWZVolD2tSwT0sdfblVfywwQ_2cdJri0C0aY8LUMihP4DSS6OmNI5PBqHuR6fdKilByF8aSNv8kKwWT20VWdtQ_dmonz_9eDHfZfcvDeQow8lYFDtSdeJ1vIH_7_O9-OoVuJNOW0b6HjTpnwBO7OU4XAPIRG1PLbOxO7fTKfaKqMayQHMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cnvntUi8R7koTRaDjwDXuibE5m9epqeTauGKQNua-k4q157GDU9jkdUU8RX9Yn0OC9m9fag8Yuz_oGIEBjZC4pdhRMMdx9z0jf8nLYOigMnbHPBgZVRt5tz8_rMFSgPpSWlYoSdQKc_7CzP3hOyBB5LrV0O__e_vhdklC4v_0pMtZgGaPC-044E36MC5obPOIhdlpHOugZz-dQorm6nPXXjd9WnrDyjbM2adh6Mthkw-LCowICy00SrkZhuLQtu2YlwT1hhBkPuMxa4Eex1hjyqWeH_xM8g7cbI6l-vBaoW6AfEFoYjo5qHN6qjnUUl3um8WbzvGtfpOirOTEMoCGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/449038" target="_blank">📅 00:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449037">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKuA2xXhPp81YtfFv_ktnpHUP4GEQ3stBbWS5mVsoSns-2ivWmOUuDSnvkWe56JVS0YpCt8OxrN2xp6hYLA_3ftg2BoWOO1Qi7C0Cmb5tbjhytxhZ55BZViR890Mzq6BhbSop4opOh33ATRKUfcY9On4o4Er4ODMuvbySjdsn2xwYDyGR2FiN97c-1KdTW1NUf7WAY6ZJUsSY46GvFwEUj82AysngkHaNfH7s7J2VsC9PNAeiWCWJD1RYGlnsfh0YYTsQZOSnqbJA0vAeSoVOfCDNuiK1g7sFqVmcmx0WkogrOTb9R2SnTAvvxAbg6_Zsj_x68fwweCJkDFlpcs63g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلجی: تشییع ده‌ها میلیونی، پایگاه مردمی ایران در منطقه را به نمایش گذاشت
🔹
رئیس شورای اطلاع‌رسانی دولت سیزدهم: حضور مردم، چه در شب‌های حضور میدانی و چه در مراسم تشییع گستردۀ تهران، قم، مشهد و به‌ویژه عراق، پیام روشنی از ثبات جمهوری اسلامی و استمرار این مسیر با قدرت بیشتر دارد.
🔹
آمریکایی‌ها، صهیونیست‌ها و تحلیلگران جهان این واقعیت را درک کرده‌اند که ایران نه‌تنها تضعیف نشده، بلکه با اتکا به پشتوانۀ مردمی، قدرتمندتر از گذشته به مسیر خود ادامه می‌دهد.
🔹
این حضور گسترده، علاوه بر نمایش ثبات و استمرار انقلاب، بیانگر پایگاه مردمی جمهوری اسلامی نه‌تنها در داخل ایران، بلکه در سراسر منطقه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/449037" target="_blank">📅 00:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449036">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEAIVrm7Fe3S1hfhOJQJoHMlnkjx3GZV7KxfBDH9QoH6o_uhl28htL3BbDTsk6U7kqM9AXt-uwC3JXT_uZZohmo4-sqheJsw10HVreio_ZKsKykVxIgLYwltQzkOFdX_q6Jqsa5xgWVHGs2xaGA6B0x--1VwvZ_LwrwARRSqvVkdHvl-K0Bbj4_yG6GHCqwhpQ5fNlevd6Ws8fbmCgQ2sDJM763OVaQXRySnBqil9CcoQW2TIGxCjUqiLpPJWXqm2-ztXwnjopeJjTeTpdsJekUuqBKibDDnYTeweg_jKtC8GgNoUsUkeI0Qrngx5yJB8N3uViZNP6BFaylz5GRD6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
گل دوم اسپانیا در دقیقه ۸۸
⚽️
اسپانیا ۲ - ۱ بلژیک @Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/449036" target="_blank">📅 00:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449035">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de99893385.mp4?token=DaRILPOLFnAf2codxLkj8l-khDCnKZSwixIuLZwSE2o7jhyWwnxREKHTGlY9DJmoGwM9g1ic1KRLZHic4fJ9ebhBxWSEZXLrX213R3-VJGLwJz1FPR7RjwR44qxO2HKq9KWQ8bNt2V0y2GVihl932r0St5t2SqBY-jYT2l3qCt6JMRAmzVMI7iWNwd0sJshCZPSfrpc9wFtKdJs5DMYVUXnFChoiM3DJWprJp4ymF_UTg_sUhy2m3n7kCUgFOl0x4LQStKCyTJaPvIX8mava19yQ8EKBCMnB67Uh32mWfmALZ-7hkty3W9SW1koao9G9uXr4kKnVumBvs3ewGerIHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de99893385.mp4?token=DaRILPOLFnAf2codxLkj8l-khDCnKZSwixIuLZwSE2o7jhyWwnxREKHTGlY9DJmoGwM9g1ic1KRLZHic4fJ9ebhBxWSEZXLrX213R3-VJGLwJz1FPR7RjwR44qxO2HKq9KWQ8bNt2V0y2GVihl932r0St5t2SqBY-jYT2l3qCt6JMRAmzVMI7iWNwd0sJshCZPSfrpc9wFtKdJs5DMYVUXnFChoiM3DJWprJp4ymF_UTg_sUhy2m3n7kCUgFOl0x4LQStKCyTJaPvIX8mava19yQ8EKBCMnB67Uh32mWfmALZ-7hkty3W9SW1koao9G9uXr4kKnVumBvs3ewGerIHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرانجام دروازه اسپانیا در دقیقه ۴۱ باز شد
⚽️
اسپانیا ۱ - ۱ بلژیک @Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/449035" target="_blank">📅 00:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449034">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">تصادف ۲ اتوبوس حامل زائران عراقی در محور سبزوار
🔹
اورژانس سبزوار: برخورد دو دستگاه اتوبوس با یکدیگر منجر به مصدومیت ۱۲ نفر شد که ۱۰ مصدوم در محل حادثه سرپایی درمان و ۲ نفر نیز به بیمارستان منتقل شدند.
🔹
اتوبوس حادثه دیده مربوط به زائران عراقی مراسم تشییع رهبر شهید بود که بعد از این حادثه، به موکب نماز جمعه جهت تکریم اعزام شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/449034" target="_blank">📅 00:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449033">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c53005e601.mp4?token=RI8WIRQD4-kkAXElZRZBYXZ8-jhDqKCCE6-w0RqTMl3VLBrI-uKUl4bQQn1W8IHLrYeowx_tyo448bHkp3MIxhrXgpopOtxbwWFqO9SrnSHet7Q6j2u9Jti1EMXU3VMqXw3YutqUMW2esPuUGbLIsdiGQ2i3zq9pQtDDsqpgzf3Gs0DJ-LMeh9Cjwln_3ZA4ttuDXYZJNSu13mqqaGXm7SAwj195SGkOl_LQ3wsKuCWxTUVqyFy_UQkCLi5yp43kjNLR13dVxSL7XaaaqK994Em51ofU7IJhVoZXalDnODeIcBv7tVcBRLN6mK2oTSuqyIla86b3M55XFcsnGV6mKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c53005e601.mp4?token=RI8WIRQD4-kkAXElZRZBYXZ8-jhDqKCCE6-w0RqTMl3VLBrI-uKUl4bQQn1W8IHLrYeowx_tyo448bHkp3MIxhrXgpopOtxbwWFqO9SrnSHet7Q6j2u9Jti1EMXU3VMqXw3YutqUMW2esPuUGbLIsdiGQ2i3zq9pQtDDsqpgzf3Gs0DJ-LMeh9Cjwln_3ZA4ttuDXYZJNSu13mqqaGXm7SAwj195SGkOl_LQ3wsKuCWxTUVqyFy_UQkCLi5yp43kjNLR13dVxSL7XaaaqK994Em51ofU7IJhVoZXalDnODeIcBv7tVcBRLN6mK2oTSuqyIla86b3M55XFcsnGV6mKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جلیلی: معیشت بدون امنیت و دفاع از حاکمیت کشور به‌دست نمی‌آید
🔹
قراردادن خط خون‌خواهی مقابل معیشت، نوعی تحجر است؛ تحجر یعنی شما یک پاسخی برای یک سوالی داشته باشید و اگر ۱۰ بار تجربه نشان داد که پاسخ‌تان غلط است بازهم آن را تکرار کنید.  @Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/449033" target="_blank">📅 00:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449032">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea766c1af2.mp4?token=t_AxHu4RxoIvTQJ2kkSQnYW9FIDYkZ2Q8FPMOmuarx0CbAJSmThrZILXeA7UcWLv22w7w4nJj6scykJlFq98pup_zs7C6JlRtjgFyumYZjUWXa-XBXV9WqI_R3OMYI0Z5Vwa9VNlcPO9FCfl4jH3ZueKnMRrlL0eVsX3fXupSUnPUTaIw_0C4S6sxZLsGUHA-jI6eV2yAwCkQ-9Um-LwuBff_c_cNr6tyDcpZtlJmSwvNIrClwWmwYzeulaBrsC9MpRVwDIHBmxkwj1zYuzIbTze3gkTZufhWNW5OueYDD24l9AchaAA8zp-PYfIrz0y-Y_FL5nY0PFxwA1K94TWOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea766c1af2.mp4?token=t_AxHu4RxoIvTQJ2kkSQnYW9FIDYkZ2Q8FPMOmuarx0CbAJSmThrZILXeA7UcWLv22w7w4nJj6scykJlFq98pup_zs7C6JlRtjgFyumYZjUWXa-XBXV9WqI_R3OMYI0Z5Vwa9VNlcPO9FCfl4jH3ZueKnMRrlL0eVsX3fXupSUnPUTaIw_0C4S6sxZLsGUHA-jI6eV2yAwCkQ-9Um-LwuBff_c_cNr6tyDcpZtlJmSwvNIrClwWmwYzeulaBrsC9MpRVwDIHBmxkwj1zYuzIbTze3gkTZufhWNW5OueYDD24l9AchaAA8zp-PYfIrz0y-Y_FL5nY0PFxwA1K94TWOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: آمریکا تفاهم‌نامه را نقض کرده و ما هیچ تعهدی را بدون مابه‌ازا اجرا نمی‌کنیم
🔹
رویکرد ما تعهد در برابر تعهد است. اگر طرف مقابل تعهداتش را نقض کند متقابلا ایران همان کار را انجام خواهد داد. @Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/449032" target="_blank">📅 00:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449031">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: ایران اجازه بازرسی از تاسیسات آسیب‌دیده ناشی از حملات آمریکا و رژیم صهیونیستی را نمی‌دهد
🔹
قطعنامه ۲۲۳۱ منقضی شده و عملا وجاهت حقوقی ندارد. @Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/449031" target="_blank">📅 23:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449030">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: پیمان‌شکنی آمریکا یک عادت است
🔹
آمریکا با حمله به ایران، لغو معافیت تحریم نفتی و اعمال تحریم‌های جدید تفاهم‌نامه را نقض کرده است. @Farsna</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/449030" target="_blank">📅 23:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449029">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: ما هیچ درخواستی برای مذاکره با آمریکا نداشتیم اما سفر میانجی را به ایران پذیرفتیم. @Farsna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/449029" target="_blank">📅 23:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449028">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🖼
مرندی، کارشناس نزدیک به تیم مذاکره‌کننده: ترامپ و آکسیوس را نادیده بگیرید؛ تا وقتی دولت ترامپ به تعهداتش عمل نکند، هیچ مذاکره‌ای انجام نمی‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/449028" target="_blank">📅 23:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449027">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa65d719cf.mp4?token=BUYwUpWy9K3D9IpAdwDuvlE9QE24S99Lf9wNZpuhP2lRWS3zXItuAfyHqDf9z5_de5MM_kaCVxP05eL2vtvvFs67iJf0F2pTeF404U8wCEJSrmL-cqp2Y2G3VKeVbw-6GqhGgtsPiGEIc9OzYDTj2rAT0GkjJpbNoVy65Db99Ijn4Qsx_0IyQWZmfyReggkiMt9MkHHP5xdP9KioHUcUbfB9nUskz6fJPyHU3XRIXitg7K26Qn0LdHvzyzP25tCnevmxYIvv46Wqx0Mvb9VdtAhbussfV09LmEKLKutegckhrZ3yykotNa_q-gEwmziAhwDhfD2ujOyWkYw6XHGcPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa65d719cf.mp4?token=BUYwUpWy9K3D9IpAdwDuvlE9QE24S99Lf9wNZpuhP2lRWS3zXItuAfyHqDf9z5_de5MM_kaCVxP05eL2vtvvFs67iJf0F2pTeF404U8wCEJSrmL-cqp2Y2G3VKeVbw-6GqhGgtsPiGEIc9OzYDTj2rAT0GkjJpbNoVy65Db99Ijn4Qsx_0IyQWZmfyReggkiMt9MkHHP5xdP9KioHUcUbfB9nUskz6fJPyHU3XRIXitg7K26Qn0LdHvzyzP25tCnevmxYIvv46Wqx0Mvb9VdtAhbussfV09LmEKLKutegckhrZ3yykotNa_q-gEwmziAhwDhfD2ujOyWkYw6XHGcPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جلیلی: انتقام‌ و پاسخ به جسارت دشمن، کمکی به حق حاکمیت همه ملت‌هاست که آمریکا بداند چنین کاری بدون هزینه نیست.  @Farsna</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/449027" target="_blank">📅 23:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449026">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb55b22145.mp4?token=Aqrxu5Y_qRhKldwvsLB2qutZ64Fiy6VFZFgeQtJY_tUCgY0hdy6Fb49y0ypWo-r2kwu22lXqyqotIO95YKmX8h1ongeZVBa5eRms0Z5iM4vksM5HhHJqno3beTEGra8Qtc58BHh1SSh9Va8YFko6Jz96any0bg7dKIZQWbdcvf_BPIRf9xLghvMg_p_Yx36DRgZg5HE_P23dSWzP3qkHpiQKNQvlB_LpdeuXAHHLRDC5yj82WPhBVFECZUh3PrUdAOzUI37_lNOOig_6vj3QValFS6P6YaLsYPHCjLgUvJLXSHrzHWKpqUtmRcrg5utu7LyU728NKppdS3j1oW52YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb55b22145.mp4?token=Aqrxu5Y_qRhKldwvsLB2qutZ64Fiy6VFZFgeQtJY_tUCgY0hdy6Fb49y0ypWo-r2kwu22lXqyqotIO95YKmX8h1ongeZVBa5eRms0Z5iM4vksM5HhHJqno3beTEGra8Qtc58BHh1SSh9Va8YFko6Jz96any0bg7dKIZQWbdcvf_BPIRf9xLghvMg_p_Yx36DRgZg5HE_P23dSWzP3qkHpiQKNQvlB_LpdeuXAHHLRDC5yj82WPhBVFECZUh3PrUdAOzUI37_lNOOig_6vj3QValFS6P6YaLsYPHCjLgUvJLXSHrzHWKpqUtmRcrg5utu7LyU728NKppdS3j1oW52YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پدر زهرای ۱۴ ماهه در مراسم تشییع همسر و فرزندش به‌همراه امام مجاهد و شهید انقلاب  @Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/449026" target="_blank">📅 23:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449025">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be1f11561f.mp4?token=KGYaFzVQw4zfBv82SkZTQ9Cz-ejBQYQUZKnwJt_dPQc6tKKRT6NRmPeYGhx6Zs6LM8awIvRn1O28pCGOzHa-Cn3xrkrd8DINUtbTng65T2ze8mphlDJvXjaHbNk2A-TLzz7Dn88eAk6QBuTfBwPA1yPiMDNO8RVB0j7HdnfXxEUofdFi_h4GLGjcmtyQ32ZzAL567UdMc5MOmvCZIpPOBp5UcN8gHUgxMdkV7pLws6cQDrKSWSXUaxoDSX7_maL-KNHDJ_grlyTbMDMJzrD2s6Lh1euj6Qa3zGiqH-aOGkVzpp_MRLcJZ_nkU-64ZKtcWElByW1a8ucgECOXoPtPUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be1f11561f.mp4?token=KGYaFzVQw4zfBv82SkZTQ9Cz-ejBQYQUZKnwJt_dPQc6tKKRT6NRmPeYGhx6Zs6LM8awIvRn1O28pCGOzHa-Cn3xrkrd8DINUtbTng65T2ze8mphlDJvXjaHbNk2A-TLzz7Dn88eAk6QBuTfBwPA1yPiMDNO8RVB0j7HdnfXxEUofdFi_h4GLGjcmtyQ32ZzAL567UdMc5MOmvCZIpPOBp5UcN8gHUgxMdkV7pLws6cQDrKSWSXUaxoDSX7_maL-KNHDJ_grlyTbMDMJzrD2s6Lh1euj6Qa3zGiqH-aOGkVzpp_MRLcJZ_nkU-64ZKtcWElByW1a8ucgECOXoPtPUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول اسپانیا به بلژیک توسط فابین رویز در دقیقه ۳۰
⚽️
اسپانیا ۱ - ۰ بلژیک @Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/449025" target="_blank">📅 23:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449024">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔸
کسی که کشت امام مرا چرا نکشیم
🔸
که ننگ ماست اگر قاتل تو را نکشیم
🔸
از این به بعد کفن، جای جامه بر تن ماست
🔸
قسم به خون تو، قتل ترامپ گردن ماست
@Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/449024" target="_blank">📅 23:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449023">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35ff73123c.mp4?token=nn_PeWdFQuLNCY0fLxuPxYC_8auFcnStiThxPuHzL02ssPPVo570Wl5qhdLvvuG3-JiNLaQuEHEJSJgr5vWLMdX-V-Q8JLwQMoxy6By8m-usa5hK25mkCwbhMEeBDxdEQSs9sVtSzIvAgL5Ks_nDmEVhEoEjWnWuU1BRIiX4ptbgu-DaIZ3ETwOKqQzDvg1A2ahYCfba9G6mTaanqMKOpyHPBfaTwpw4_ESH7ecFkyxHxB_AbuS-rTyk71BEo2OtIHhHwLwtQNyq1qWGAXG3A5KOYBNolOBUm35jtKTvm-CbYRc9A--lwqIEooPl6tBpxjjrFO7_DmZLV7vths7c7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35ff73123c.mp4?token=nn_PeWdFQuLNCY0fLxuPxYC_8auFcnStiThxPuHzL02ssPPVo570Wl5qhdLvvuG3-JiNLaQuEHEJSJgr5vWLMdX-V-Q8JLwQMoxy6By8m-usa5hK25mkCwbhMEeBDxdEQSs9sVtSzIvAgL5Ks_nDmEVhEoEjWnWuU1BRIiX4ptbgu-DaIZ3ETwOKqQzDvg1A2ahYCfba9G6mTaanqMKOpyHPBfaTwpw4_ESH7ecFkyxHxB_AbuS-rTyk71BEo2OtIHhHwLwtQNyq1qWGAXG3A5KOYBNolOBUm35jtKTvm-CbYRc9A--lwqIEooPl6tBpxjjrFO7_DmZLV7vths7c7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مهار آتش‌سوزی مینی‌پالایشگاه اکسین پلدختر
🔹
مدیر ایمنی شرکت شهرک‌های صنعتی لرستان اعلام کرد آتش‌سوزی مینی‌پالایشگاه اکسین پلدختر مهار شد.
🔹
آتش‌سوزی تنها بشکه‌های حاوی روغن سوخته را درگیر کرده و به تأسیسات و مخازن پالایشگاه سرایت نکرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/449023" target="_blank">📅 23:17 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449022">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مخالفت روسیه و چین با فشار غرب برای استفاده از شورای امنیت علیه ایران
🔹
روسیه و چین روز جمعه با برگزاری نشست شورای امنیت سازمان ملل درباره ایران که از سوی کشورهای غربی حمایت می‌شد، مخالفت کردند.
🔹
این دو کشور تأکید کردند که قطعنامه ۲۲۳۱ در اکتبر ۲۰۲۵ منقضی شده و این شورا دیگر هیچ مأموریتی برای بررسی پرونده هسته‌ای تهران ندارد.
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/449022" target="_blank">📅 23:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449021">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b00339ed1a.mp4?token=hBr_7jBj6E6b2qqpz3aWuXfm8GNoPLesC3_3tPhB9rIF9XPyztKTM7BXZXcG_N1dH4zyWVDv2OHHfKrVDQdZh_Rm6nhwgaTOaKGdsohrSK0OcRY9VoGIm4rRP7XKhCM_qW09CjMKoA8bp2jKwpNBE6A5ktNqHl0yYdLEVjZOlGJAKp_aL_UIihD6p0Qga1NflLUtGq_WhuakHEO9ptmX-rV6GNKPY5bf3sZkEUShNy0Rtd808i_3KFr02_LiNSUHl-O7Nlj9yCxkDf9r-h5-HVoUAzrhli0sVqJ-AxhvbnG0-k3nYNo98VvbKYVd-Ai5xDJ-mZz_gInOFegdVkhTYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b00339ed1a.mp4?token=hBr_7jBj6E6b2qqpz3aWuXfm8GNoPLesC3_3tPhB9rIF9XPyztKTM7BXZXcG_N1dH4zyWVDv2OHHfKrVDQdZh_Rm6nhwgaTOaKGdsohrSK0OcRY9VoGIm4rRP7XKhCM_qW09CjMKoA8bp2jKwpNBE6A5ktNqHl0yYdLEVjZOlGJAKp_aL_UIihD6p0Qga1NflLUtGq_WhuakHEO9ptmX-rV6GNKPY5bf3sZkEUShNy0Rtd808i_3KFr02_LiNSUHl-O7Nlj9yCxkDf9r-h5-HVoUAzrhli0sVqJ-AxhvbnG0-k3nYNo98VvbKYVd-Ai5xDJ-mZz_gInOFegdVkhTYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جلیلی: رهبر شهید کاری کرد که کسی نتواند مثل جنگ جهانی دوم ایران را اشغال کند.  @Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/449021" target="_blank">📅 23:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449020">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94cbd0b246.mp4?token=nMQp17w2Fi6H6WX0xrswPdBDgLjIXsV37stUTRBsKihfuiAOWoareoAGa6HPpyiReIHTO4PE2izelhzUuSmTzNGgJgdh9omWuok1gI6JBP9vT74XPE2fUXe4ZS2wtPndmg0QWUHKGG8m7-2mkiH3OC25LgYtjKnu3ep81mnsHdwsXQ3D8gXApGv-CU3yroXwb1rNLgFXpaythL0Q6yZ4VB-nMFOa1Q4KBxVC86rRhgBIMMC28u648R0SMGZgcyeqfdVXLcPjqSDs9jA3AwMBVILTvyxWvQvahKxlVMLtx5I3BGfV74veqk4q17Gk-ydaap00P1fUqtfNUksjVNtttA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94cbd0b246.mp4?token=nMQp17w2Fi6H6WX0xrswPdBDgLjIXsV37stUTRBsKihfuiAOWoareoAGa6HPpyiReIHTO4PE2izelhzUuSmTzNGgJgdh9omWuok1gI6JBP9vT74XPE2fUXe4ZS2wtPndmg0QWUHKGG8m7-2mkiH3OC25LgYtjKnu3ep81mnsHdwsXQ3D8gXApGv-CU3yroXwb1rNLgFXpaythL0Q6yZ4VB-nMFOa1Q4KBxVC86rRhgBIMMC28u648R0SMGZgcyeqfdVXLcPjqSDs9jA3AwMBVILTvyxWvQvahKxlVMLtx5I3BGfV74veqk4q17Gk-ydaap00P1fUqtfNUksjVNtttA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول اسپانیا به بلژیک توسط فابین رویز در دقیقه ۳۰
⚽️
اسپانیا ۱ - ۰ بلژیک
@Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/449020" target="_blank">📅 23:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449019">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">پزشکیان: احترام متقابل و التزام عملی به تعهدات، پیش‌شرط هرگونه توافق پایدار و موفق خواهد بود
🔹
رئیس‌جمهور در گفت‌وگو با نخست‌وزیر پاکستان: در شرایط کنونی، در کنار تلاش‌های دیپلماتیک برای تثبیت آتش‌بس و جلوگیری از گسترش بحران، روند دوگانه‌ای شکل گرفته که از یک سو رژیم‌صهیونیستی و جریان‌های حامی سیاست‌های تنش‌آفرین و از سوی دیگر دولت آمریکا با عدول از تعهدات خود درصدد برهم‌زدن روندهای موجود و جلوگیری از استقرار آرامش در منطقه هستند.
🔹
انتظار طبیعی آن است که سایر طرف‌ها نیز به تعهدات خود پایبند باشند و از اتخاذ مواضع یا اقداماتی که موجب تضعیف اعتماد و پیچیده‌تر شدن روندهای دیپلماتیک می‌شود، پرهیز کنند. احترام متقابل و التزام عملی به تعهدات، پیش‌شرط هرگونه توافق پایدار و موفق خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/449019" target="_blank">📅 23:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449018">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJRSqqg9ZyzB9R5L2WosoRW-cJkQlhZY9JvmmwUwrML5R0MWFtESyz1dkKZy7C9wIKhb0KFVxWY90CnhTuFiS2wjtQJAddC-KquudS57hckzZllNDmK_v7-3x8lo7ha91XjNYkiCvYXnCd2QcaGdTKvmkNycTWFwwkmuwSusgJMLGFWMYRxTgx_jguopFda2hzWsuNMSWdSrv93AW8Wy_oswtZzX4dxbqwASVO67bkZoq3kAlcEif1ESt_c8m5paoTXXqObOsCXqeR24sAaqR7pgy6hNykELp_JgFNNdKaZb-NNPKPESOaowh6BPy97gQVQLx-esP2c1OmkQZzaOyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
معاون وزیر خارجه: سند جدید آمریکا برای ارتقای رتبه تجاری امارات به پاداش پشتیبانی از تجاوز نظامی علیه ایران، مایهٔ رسوایی ابوظبی است؛ امارات باید پاسخگو باشد.
@Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/449018" target="_blank">📅 22:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449017">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91e36e4e81.mp4?token=nXUXWxL9833H5Ta3JoH243OF6mESqao_gA4F9-a5J4-sCkq45iBuPW0tvy1by8YLGEYHjvtRvA6aTRxoybJuX9rhCki9gZWsgyOQikvFCivdPybRr5RT2hLPzUQIVLC4Ggo9mWpAkaQTIu60Oeta2YGmgQI_9kKuQQgYfJt1n2twSOIBzQ9R_PRanNMCw-ZMagGYiTwr-3cuXKu8FPlzm9p0h2Ae4Gq8VISnNOkn6oEDDy7Dl_PR5E43GdZb3ct7mT3KoV6KTIwG5KghVgclRnyIdGtrmdq-h1-Myq0IvpzhuZANE1koq_MIQ40K_x5A7nWTX2kIHh82ffr8LIHE2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91e36e4e81.mp4?token=nXUXWxL9833H5Ta3JoH243OF6mESqao_gA4F9-a5J4-sCkq45iBuPW0tvy1by8YLGEYHjvtRvA6aTRxoybJuX9rhCki9gZWsgyOQikvFCivdPybRr5RT2hLPzUQIVLC4Ggo9mWpAkaQTIu60Oeta2YGmgQI_9kKuQQgYfJt1n2twSOIBzQ9R_PRanNMCw-ZMagGYiTwr-3cuXKu8FPlzm9p0h2Ae4Gq8VISnNOkn6oEDDy7Dl_PR5E43GdZb3ct7mT3KoV6KTIwG5KghVgclRnyIdGtrmdq-h1-Myq0IvpzhuZANE1koq_MIQ40K_x5A7nWTX2kIHh82ffr8LIHE2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جلیلی: رهبر شهید کاری کرد که کسی نتواند مثل جنگ جهانی دوم ایران را اشغال کند.
@Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/449017" target="_blank">📅 22:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449016">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c63629abe.mp4?token=aFi98Z86oVzs_qZ-aNw9BCT9r0QlQAlHxIeT2XiTk4kGMseSmxf_XoV7IWZSPdcKhKHach-fxGSTA1ITPimCUJ-3rb2E1qnzoWO-5GNxTF-tfMi6-C0497ZWwsJ59rRnfJwcooGh-UNIQWrQ7DcOQNdMtCT_mkQKvGvASPpbuX99B4UfHGZpE9oA4I9RNscnXtMwyCUrIHE2CFfK-dIV7sbbP1ZP_lqBEsi504Nm99Qzx87P0KLHhTRATbI_PqMRqtoJk1q52bUmIJ08pupB4xTdD3P6VPBpec1ijjDSmKnnVVzJZNakKXufsbNWqaIJTjBjodJn_TBwaDkMunTJNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c63629abe.mp4?token=aFi98Z86oVzs_qZ-aNw9BCT9r0QlQAlHxIeT2XiTk4kGMseSmxf_XoV7IWZSPdcKhKHach-fxGSTA1ITPimCUJ-3rb2E1qnzoWO-5GNxTF-tfMi6-C0497ZWwsJ59rRnfJwcooGh-UNIQWrQ7DcOQNdMtCT_mkQKvGvASPpbuX99B4UfHGZpE9oA4I9RNscnXtMwyCUrIHE2CFfK-dIV7sbbP1ZP_lqBEsi504Nm99Qzx87P0KLHhTRATbI_PqMRqtoJk1q52bUmIJ08pupB4xTdD3P6VPBpec1ijjDSmKnnVVzJZNakKXufsbNWqaIJTjBjodJn_TBwaDkMunTJNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
به رهبر شهید ایران سلام، سایه سیدمجتبی مستدام
@Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/449016" target="_blank">📅 22:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449015">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mhs5EunX7oJ12BhR_mOqi7oLIJoZWLcVvfGU447CmhRaZ0EjKhSA9kmn7ENjLQRhTs5G28sz_4N1FIu_fcbnfVsQBk2rLugz8srBacdnKG-u0KnRGs94lIGIVCwczWmohWkfOxMkWpv4nAqLWFS2Poi2oA3Ox0-NDFNTxUybMn_CP4aD-aVCygvApeuxgjz9pvMwkkLOu0FYQ-Zw9RAybKMOy509dDAL5O54wOyMuYfVrJtvOIKNia2ElpLzgjbAVVfnJfcrxSvmn7iEN6bPz_d61gxNqYZ4nJzo4a5BfahnHG-rWBQyD2FkGI490V8nY60nWb5mK6J-FL2FV6Qvzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ بازهم در جهان موازی درخواست ایران برای مذاکره را پذیرفت!
🔹
رئیس‌جمهور آمریکا مدعی شد که ایران از دولت او خواسته مذاکرات ادامه پیدا کند.
🔹
او مدعی شد: «ما با مذاکره با ایران موافقت کردیم اما به صراحت اعلام کردیم که آتش‌بس پایان یافته است». @Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/449015" target="_blank">📅 22:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449014">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1efc24d831.mp4?token=ZVLA2Mm72_MNyYhlZh4f6MeXcwqlo3D3J_4VcIK3qnNSyuoFKEseHRDgfZkY-Ok0DRRmRqpt0KIPHe6EF6sjfK_s9pjq02sU7cfNQkD5KbAX-KY140lz2L2pEK2WHnnWMyetQTPQo-c3SSXaN_drih0Z49xqi9w7UfMVa1BoJbrjWXd-UpBoePUP9dxXIlqim8yR1KnG8XEwNl_WBaOvlxhdza0sc03mGPM0kQF34RJfvOB13wiyq_t5Sj7x15p0iPkZ_jONIb2FnHPxlDdfK369SCbGqK68SSEVPCneafKgGQl1-K1jL5qYGmBNTf3WvfHDQMBPSOkBZIC4lANCOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1efc24d831.mp4?token=ZVLA2Mm72_MNyYhlZh4f6MeXcwqlo3D3J_4VcIK3qnNSyuoFKEseHRDgfZkY-Ok0DRRmRqpt0KIPHe6EF6sjfK_s9pjq02sU7cfNQkD5KbAX-KY140lz2L2pEK2WHnnWMyetQTPQo-c3SSXaN_drih0Z49xqi9w7UfMVa1BoJbrjWXd-UpBoePUP9dxXIlqim8yR1KnG8XEwNl_WBaOvlxhdza0sc03mGPM0kQF34RJfvOB13wiyq_t5Sj7x15p0iPkZ_jONIb2FnHPxlDdfK369SCbGqK68SSEVPCneafKgGQl1-K1jL5qYGmBNTf3WvfHDQMBPSOkBZIC4lANCOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صدای منتظرانت، صدای خونخواهی‌ است...
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/449014" target="_blank">📅 22:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449013">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58dcb9d425.mp4?token=OX7taRwoDSq06vs1zLzpEBKF0kPBCjTKU1_v2nOttK5RLENxyeRAxg5BT2YkLWr73xTG5Xf482383Ol-fu0qU-ZAnWRYouynfElv9UnRSYgXNlMwCEYlz90jo0muaTvLPSDj-Qqgd23lnTFL6xx_u7Ow6g6BM4bcqfylFyeU4o-m1p6bOMoA7W1a2Ug4Z9IGQhsE6H4g_xvt_ihakGcXftnn-8MMCuKSQ8s7XBJtt9OZ_hGnmNTe345yl62dt6rtM2OFqc_S4PjoMrFWfCVz_dgcQDK8j-i9wXHj7i_N-BJlJeCJop64aWU_ZbrR3ip-ocHxTBHFA2GIqkSEAL5XMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58dcb9d425.mp4?token=OX7taRwoDSq06vs1zLzpEBKF0kPBCjTKU1_v2nOttK5RLENxyeRAxg5BT2YkLWr73xTG5Xf482383Ol-fu0qU-ZAnWRYouynfElv9UnRSYgXNlMwCEYlz90jo0muaTvLPSDj-Qqgd23lnTFL6xx_u7Ow6g6BM4bcqfylFyeU4o-m1p6bOMoA7W1a2Ug4Z9IGQhsE6H4g_xvt_ihakGcXftnn-8MMCuKSQ8s7XBJtt9OZ_hGnmNTe345yl62dt6rtM2OFqc_S4PjoMrFWfCVz_dgcQDK8j-i9wXHj7i_N-BJlJeCJop64aWU_ZbrR3ip-ocHxTBHFA2GIqkSEAL5XMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سید علی خمینی: تا وقتی که رهبری معظم انقلاب در مورد پایان تجمعات چیزی نگویند، تجمعات خیابانی ادامه خواهد داشت.  @Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/449013" target="_blank">📅 22:17 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449012">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1eb35161a.mp4?token=aSp1D8XNZHgE1CHbULxPevIxeHaJxINlTFCfvuLVJZ4LknfbiJmEqjSn5tVLdlOBxZeCLDXu9yldsduMtxA5ZlhW8pf4uLEa6D0gHrPpY06zwkayPx7Eh7FWkvPrKmDUKzQfBlrxK46o4kUbd-hr5P7P2lOVqKgddaw2w0wRfLHSHQ0bkgFG8FJjo2Nx-OUYrb9xc3zfv4IUv20WL-pN4obACENyCpk0SjJvDRjs80fjlk_RlK6sO_rs9Ej2-K-NHCCDI_gHo3sha2ZZDLw1vhZo9FTO-eAprhlNRth3wNZxAW-bWbHQXrnJactUUm3BxN-QkKRsDYwcNZEdrxMppA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1eb35161a.mp4?token=aSp1D8XNZHgE1CHbULxPevIxeHaJxINlTFCfvuLVJZ4LknfbiJmEqjSn5tVLdlOBxZeCLDXu9yldsduMtxA5ZlhW8pf4uLEa6D0gHrPpY06zwkayPx7Eh7FWkvPrKmDUKzQfBlrxK46o4kUbd-hr5P7P2lOVqKgddaw2w0wRfLHSHQ0bkgFG8FJjo2Nx-OUYrb9xc3zfv4IUv20WL-pN4obACENyCpk0SjJvDRjs80fjlk_RlK6sO_rs9Ej2-K-NHCCDI_gHo3sha2ZZDLw1vhZo9FTO-eAprhlNRth3wNZxAW-bWbHQXrnJactUUm3BxN-QkKRsDYwcNZEdrxMppA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرائت دست‌نوشته عاشقانه رهبر شهید انقلاب در وصف امام حسین(ع)
@Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/449012" target="_blank">📅 22:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449011">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b20077aff3.mp4?token=Yb-AyW-83jZ3-xTFHka8qG6mfavwgd9b7Ir7R5_JV6o68bpMv4mJ8WZT24V28dH_nY_NX-c6ueBJZKIqZ20wqb-7ZoliK9K6Y4zjx--HR-F_BUnzcecCvib_fFqc-QRhYCfupP4h8YA0Adh6_lwjZp7EmO9WgX28LQ3WQxPvWzCEAqr9_PS3Nfaz2ALTDaSeJdHBsOS6cqSbvRg22NSFXXnz0IMJ34fzC342zb24esms_f-PaBFJCgTAADs7Di-MUDb8z66ZtxFYQtV97BJPjFhnnYemk6-9XcdMrgSwDcgD2rI3IrEztQAeVA5bYkk_dQImAXCeZVANz-8qdldamw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b20077aff3.mp4?token=Yb-AyW-83jZ3-xTFHka8qG6mfavwgd9b7Ir7R5_JV6o68bpMv4mJ8WZT24V28dH_nY_NX-c6ueBJZKIqZ20wqb-7ZoliK9K6Y4zjx--HR-F_BUnzcecCvib_fFqc-QRhYCfupP4h8YA0Adh6_lwjZp7EmO9WgX28LQ3WQxPvWzCEAqr9_PS3Nfaz2ALTDaSeJdHBsOS6cqSbvRg22NSFXXnz0IMJ34fzC342zb24esms_f-PaBFJCgTAADs7Di-MUDb8z66ZtxFYQtV97BJPjFhnnYemk6-9XcdMrgSwDcgD2rI3IrEztQAeVA5bYkk_dQImAXCeZVANz-8qdldamw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سید علی خمینی: مشکل ما با آمریکا از زمان کودتای ۲۸ مرداد آغاز شد و الان ما با آمریکا پدرکشتگی پیدا کرده‌ایم.  @Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/449011" target="_blank">📅 22:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449010">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9b1283110.mp4?token=TXpugDeMq0_3TLRk0fuKW23VUMXCHGgUQoIuyXOZSQMD1_bJ9jkxR56EbnITNc2fhat7GES5K9RKQnTeMSAipEW-IZUlG6xhzzuYeRFe3gU22JGjfFClYowINX9o34f5goEwleLfQq2m8sFAfi_1qfgklzGqFwxDoQAYnPn95aqed0TF1kUnpgzpryrfrrIpxLp8m-_IKCei2vzDYem2Zlevs75XY2J9lwGLMm_TcWacKRn_GRFmF1s53MhOZMoU8s4rrQqXGZFlMTjWtf-oLPmtv7Lexuivpb5yh__rP4sR1eoqYvKLv6btgaU2P6H69uFy8KuDUifNqECUeiwIqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9b1283110.mp4?token=TXpugDeMq0_3TLRk0fuKW23VUMXCHGgUQoIuyXOZSQMD1_bJ9jkxR56EbnITNc2fhat7GES5K9RKQnTeMSAipEW-IZUlG6xhzzuYeRFe3gU22JGjfFClYowINX9o34f5goEwleLfQq2m8sFAfi_1qfgklzGqFwxDoQAYnPn95aqed0TF1kUnpgzpryrfrrIpxLp8m-_IKCei2vzDYem2Zlevs75XY2J9lwGLMm_TcWacKRn_GRFmF1s53MhOZMoU8s4rrQqXGZFlMTjWtf-oLPmtv7Lexuivpb5yh__rP4sR1eoqYvKLv6btgaU2P6H69uFy8KuDUifNqECUeiwIqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سید علی خمینی: هرکس بخواهد مذاکره کند برای اینکه با آمریکا به صلح برسد او خائن است
🔹
هرکس پیام دوستی به آمریکا بفرستد دهانش خبیث و نجس است. @Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/449010" target="_blank">📅 22:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449009">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">آمریکا تحریم‌های جدیدی علیه ایران اعمال کرد
🔹
دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا اعلام کرد اسامی ۸ فرد و ۶ شرکت را در فهرست تحریم‌های مرتبط با ایران قرار داده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/449009" target="_blank">📅 22:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449008">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9575683bac.mp4?token=dxeWTA8RVfRT0AtKW-iW9asomIyTkwE5RPd8hPvz3C3XLIay2MSQapGohKQ0k5YCDBLBwB1gZy04ld_FgvPoZ9bdbPy5zlegKmoQiz8R2ysWZTBDJU-HG0uXTjo-EYFk9625kkJD8GInyWwZy6pOF1gmEbVA4gJZWkhKiagdCjhhbJeH5fZE3_5N7hFw0M5fPb5TCXXU2Bi2mXmetROH_b8L_6kvQz0AoXMZpJ25gIHjdBI8CDlbHtpW3lUMtSqfYobABuevAg9dOsU-SgLqgJSM8PHhYsEqTvM72OO_cJ6Lpa-Er8xOofymtJcMA38flc59p4x7juR2Vv27blunqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9575683bac.mp4?token=dxeWTA8RVfRT0AtKW-iW9asomIyTkwE5RPd8hPvz3C3XLIay2MSQapGohKQ0k5YCDBLBwB1gZy04ld_FgvPoZ9bdbPy5zlegKmoQiz8R2ysWZTBDJU-HG0uXTjo-EYFk9625kkJD8GInyWwZy6pOF1gmEbVA4gJZWkhKiagdCjhhbJeH5fZE3_5N7hFw0M5fPb5TCXXU2Bi2mXmetROH_b8L_6kvQz0AoXMZpJ25gIHjdBI8CDlbHtpW3lUMtSqfYobABuevAg9dOsU-SgLqgJSM8PHhYsEqTvM72OO_cJ6Lpa-Er8xOofymtJcMA38flc59p4x7juR2Vv27blunqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سید علی خمینی: برخی می‌گویند جنگ را ادامه دهید که جمهوری‌خواهان در انتخابات شکست بخورند
🔹
یعنی ما برای اینکه یک سگ زرد برود و شغال بیاید بجنگیم؟ ترامپ برود که چه کسی بیاید جایش؟ ما هم به دموکرات‌ها می‌گوییم مرگ و هم به جمهوری‌خواهان.
🔹
مگر می‌شود که امام…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farsna/449008" target="_blank">📅 22:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449007">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d16ec0d64f.mp4?token=PFw-a2FZNLMFg4cHKxiblUhCy9GvO4FIO8_uqfvm3lEsZge30wK7xBWCAJpZPQZP9-RW1zQ35Psr9NVILbVGDQs7eupoqUsWa9iGJrmrKpftRCEKipw2lpP9Wp61_EGHLwv7ovrhBT3bb7eMLjSGT9iCdtLnEZV0l5uEnbsFNWAMmYDWxfa171BYpRRMYzDAJ3KhV89xyqm3NO4hV7Bds2-PMvRfd4vIK4mVAGPdfDfznaAZxkPXpxifJTg3edwZDW80vgyFakDv_NUhFPcN1F1aYbkRC9mG64ByJXnyWsooiiGtmy3ELa1XDBkBT6nufa_qpd5EgPBG7vJYwK04oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d16ec0d64f.mp4?token=PFw-a2FZNLMFg4cHKxiblUhCy9GvO4FIO8_uqfvm3lEsZge30wK7xBWCAJpZPQZP9-RW1zQ35Psr9NVILbVGDQs7eupoqUsWa9iGJrmrKpftRCEKipw2lpP9Wp61_EGHLwv7ovrhBT3bb7eMLjSGT9iCdtLnEZV0l5uEnbsFNWAMmYDWxfa171BYpRRMYzDAJ3KhV89xyqm3NO4hV7Bds2-PMvRfd4vIK4mVAGPdfDfznaAZxkPXpxifJTg3edwZDW80vgyFakDv_NUhFPcN1F1aYbkRC9mG64ByJXnyWsooiiGtmy3ELa1XDBkBT6nufa_qpd5EgPBG7vJYwK04oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سید علی خمینی: کسانی‌که از جنگ می‌ترسیدند فهمیدند که جنگ هزینه و مشکل دارد اما ترس ندارد؛ ترس از جنگ بدتر از خود جنگ است.  @Farsna</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/449007" target="_blank">📅 21:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449006">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ادعای رویترز: تیم مذاکره‌کننده قطر در تهران حضور دارد
🔹
رویترز به‌نقل از یک منبع آگاه مدعی شد هیئت مذاکره‌کننده قطر در تهران با مقامات ایرانی دیدار کرده است.
🔹
به ادعای این منبع، هدف این سفر کاهش تنش‌ها و فراهم‌کردن زمینه ازسرگیری مذاکرات ایران و آمریکا با…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/449006" target="_blank">📅 21:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449005">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a1cb9a4ea.mp4?token=SbOn3ec4f3V8jYe2shRLJJLAhBketdwAYZ95qsDrH1s3PU--tRqsIFmO5Yn_aBk6GyBQ0OZNzXrM3roamAvUOdNJ0SHPENsXA5tDiQ7JEwz5WFhnLieRummh6U87WUE4LzXxCu4MPd_lFj02ceVc2qESXM9kBAEqcwtJex06Pr4auHdh23czqzkQ5MDED5NBIeHkZGi8UU3ImnoIUJMRZOb9Cf-bOwFejzGNxOEmOAwEdd9k-1_qtjFoyj6EWTjcI71nBk4EffSKzXVWnrjawUC7J9-SVHBOBKpXb36WxyZO7blQQKoC-jxmLvbrxs1tliYPdses4VmnmpQOOFp0Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a1cb9a4ea.mp4?token=SbOn3ec4f3V8jYe2shRLJJLAhBketdwAYZ95qsDrH1s3PU--tRqsIFmO5Yn_aBk6GyBQ0OZNzXrM3roamAvUOdNJ0SHPENsXA5tDiQ7JEwz5WFhnLieRummh6U87WUE4LzXxCu4MPd_lFj02ceVc2qESXM9kBAEqcwtJex06Pr4auHdh23czqzkQ5MDED5NBIeHkZGi8UU3ImnoIUJMRZOb9Cf-bOwFejzGNxOEmOAwEdd9k-1_qtjFoyj6EWTjcI71nBk4EffSKzXVWnrjawUC7J9-SVHBOBKpXb36WxyZO7blQQKoC-jxmLvbrxs1tliYPdses4VmnmpQOOFp0Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سید علی خمینی: گفتنِ احمق به ترامپ، فحش نیست؛ این صفت اوست.  @Farsna</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/449005" target="_blank">📅 21:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449004">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0f81f965a.mp4?token=Xqdzpk0WDszHo7gdpyH60ReGNm0aF-ieU4xbzScpzs8EnZLQVmEKRR84yUQHW4GjfROeZH1lCEzqW7mToXrPPmCkh9ZkNTi55I9KL-X5g7tBwOeO5wcj8clxBCnxXGt12-Q2eZgiFYUwjo7NWZ792e25-bgV57qeR3_plr9VTiDvHscMmRXj0g_W7jGRKc7CWB_6RJxsBJWEFC9H8Dd36P_IrgWLKRQTt9DrtO1TRkB9otuBATdq5KqJHlBHRNLc9ivPIn_cmQByteDJ4C49ip6n4WvUUtmKgaH85hVCcnW1lZe3Z5Bma2YqXgSqfmDZraPnAXAVSEjD3hltzvK9Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0f81f965a.mp4?token=Xqdzpk0WDszHo7gdpyH60ReGNm0aF-ieU4xbzScpzs8EnZLQVmEKRR84yUQHW4GjfROeZH1lCEzqW7mToXrPPmCkh9ZkNTi55I9KL-X5g7tBwOeO5wcj8clxBCnxXGt12-Q2eZgiFYUwjo7NWZ792e25-bgV57qeR3_plr9VTiDvHscMmRXj0g_W7jGRKc7CWB_6RJxsBJWEFC9H8Dd36P_IrgWLKRQTt9DrtO1TRkB9otuBATdq5KqJHlBHRNLc9ivPIn_cmQByteDJ4C49ip6n4WvUUtmKgaH85hVCcnW1lZe3Z5Bma2YqXgSqfmDZraPnAXAVSEjD3hltzvK9Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سید علی خمینی: آن مسئولی که بخوابد و در فکر انتقام رهبر شهید نباشد، باید به وجدان خودش شک کند.  @Farsna</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/449004" target="_blank">📅 21:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449003">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14cfb7b2f7.mp4?token=upXKhJ1PN99BRvSc-wMjv4og9Mk9ZHFW5gO8gUnYtvY2FvutBjuXa96fJF8l7FPNfF1PrlwdcLTtMtGlkfgK8XQh3VKKYQ3MHBa3fId-LA1smlqkBYzV8t20OCCX4WL4xh7hdkhJUG3lvQyWNzMQvxMwuAL658e1nf6i9YdLSvbbFTi8QYVRqTz7drmz4se7z4DwxJaCTGAk-S8I7Sf1Hx9_Ps-EoEUlX1Mv9XKxdEyVTNzOa_9FL-imzwWghpXeGSXG0HdNW83CVJJy8q1dfI-c_nc-oapWgY2Hrni_fefJ2PNgHDsw_NZGwnymBihFnjS-XxhCm_bOI-vW-z5cmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14cfb7b2f7.mp4?token=upXKhJ1PN99BRvSc-wMjv4og9Mk9ZHFW5gO8gUnYtvY2FvutBjuXa96fJF8l7FPNfF1PrlwdcLTtMtGlkfgK8XQh3VKKYQ3MHBa3fId-LA1smlqkBYzV8t20OCCX4WL4xh7hdkhJUG3lvQyWNzMQvxMwuAL658e1nf6i9YdLSvbbFTi8QYVRqTz7drmz4se7z4DwxJaCTGAk-S8I7Sf1Hx9_Ps-EoEUlX1Mv9XKxdEyVTNzOa_9FL-imzwWghpXeGSXG0HdNW83CVJJy8q1dfI-c_nc-oapWgY2Hrni_fefJ2PNgHDsw_NZGwnymBihFnjS-XxhCm_bOI-vW-z5cmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سید علی خمینی: آن مسئولی که بخوابد و در فکر انتقام رهبر شهید نباشد، باید به وجدان خودش شک کند.
@Farsna</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farsna/449003" target="_blank">📅 21:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449002">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B0jPB1z0YPMGu7veKKOLJVqVz-jwMG-Kg9IE8HMbxYJBkSxwELxTJgY_-an_ZWuVkN_LqxSYVXU42Qcq3YEGcNH_-Qw4v-XHzDvCFiXYR5msRoEmjoCalDKXQZfMHjHlBxR025SyfOm_0zjDHA0zJfiZLVRjsnaR6E8r3I0CD9Gi00GQowpPh9vWa4s5IMJ3NBF3HBFWpJSXUrLME_goFYCwu9W_F3_cKujtsOuYHLvlR9cf8wyMwII7B-a-_wNEr86RheM6x6bIfEvH6mcetcYmV_9vkeSZ6ZA1LZ2KFQnZaTk0y1IGtk0lJ2zalHxx2J0vaJpWcea-LVJ2JuCWkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آثار فرزندان سیدحسن نصرالله برای رهبر شهید
🔹
گروهی از هنرمندان لبنانی برای شرکت در مراسم تشییع رهبر شهید و خلق آثاری با محوریت ایشان، مدتی را در ایران سپری کردند و آثار متعددی نیز تولید کردند.
🔹
این گروه با عنوان «پسران حسین» ابتدا راهی تهران و سپس مشهد شدند تا در مراسم تشییع و تدفین پیکر مطهر رهبر شهید نیز حضور داشته باشند.
🔹
اکنون علی نجدی، یکی از اعضای این گروه که در مقطع جنگ رمضان با آثار هنری خود درباره ترامپ در فضای هنری ایران شناخته و مطرح شد، تعدادی از آثار تولیدشده خود و دیگر اعضای گروه را برای خبرگزاری فارس ارسال کرده است؛ آثاری از تمارا فحص، احمد الحاج و علی الرز که در ادامه
اینجا
مشاهده می‌کنید.
@Farsnart</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/449002" target="_blank">📅 21:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449001">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">قالیباف: درگیری با آمریکا هرگز با تسلیم ایران تمام نمی‌شود
🔹
از دید من کسانی می‌توانند با آمریکا مذاکره کنند که آماده جنگ باشند.
🔹
در مذاکرات به معاون رئیس‌جمهور آمریکا تفهیم کردم که ما هیچ اعتمادی به شما نداریم
🔹
ما هرگز دست از آمادگی برای دفاع از کشورمان برنداشتیم و هرلحظه آمریکایی‌ها به تفاهم خیانت کنند ما آماده دفاع تمام عیار هستیم و قاطعانه مقابل آن‌ها می ایستیم و حق ملت ایران را می‌گیریم.
🔹
آن‌ها طعم قدرت و آمادگی نظامی ایران را چشیده‌اند و می‌دانند که ما یقه آمریکا را رها نمی کنیم.
🔹
پایان جنگ برای کشورهای دنیا اولویت است اما همه باید بدانند که این درگیری هرگز با تسلیم ایران پایان نخواهد یافت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/449001" target="_blank">📅 21:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448994">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FdYKAhOvlE1sdLa2_X1oIEcmdOIKKNx9p7Ml-uR0goLSgZSDKKJNiuQ__yBRkX3hitm8DZlR6xRDNv4XbxhtMvZoSEn0pqP-AbC5Xsfbo9QgY9nRaWrYdr7LwNMDEbqZicqKNwUVQv2DpmiMBIVFzH0maK6R9LOsuTV5jyilh2G0Ag7a9eBJCNXqb8T-JryX9sg0WWg5W74obEqxfWy0iDa-IhMbLy0u5ubkxKiPKSljilkp0WhhK9IxjSdBL8drcCHMbv3F4tBw2bbrhEUOEoMfgUwYMh9ulywpJLMGStTsHaGgZWANE4u5iZ23O2LYy7_hPuSNzJWxoUFRj3v9Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MtdqYuB88TrCTLZ1mxaYNcFWdOJ3ePj5Skhd9WkdQwbFTUoqg3EnatCjZZuXWjl7Xht4E_1_tE0RuSQcu1ItmbIR0I_pMU9K2LgWsmrc1JX9-rXBvAK4PAP5ZzAq3gtefp6DTRx5dshNK0RJNAOhZXJm1_zjzdgwA1MCVXyIokN0ZLl0ceqB8V6oZmdHbF4RMoqHyt7rLtU7jQ0XGPo3XK0lCc0HnUx-Hm3TpcqhvMJckIvjMvuLAZZQQAP9QSs0HeZ85i4fdHpIlKZnvFg0psLZAU7K8BU9uYYsuiQZDsm8nAGIDNR-s1lMbM2TLFZ_5TMElOSrJkCfevZV7-4w9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c9MbLr6Dh1nKmENokxOk8Nz2_WyjNz43cDxNFl4NZtsjBoca2_zq2SEwdFCedtAjjlMH3GInATGHf1wSDvb9HjUYYZAY46HbTK-jdQNiO7fHDMyHj8yMZ-wuQohETIAKxDAtU_7wRjCFH1aYULP6WnyMJxtVRQuTQjQS-evMG5Xj3b4gyCc5xdq0u4n7MWhKaNYVfLI04wd5DD__AuTj_cznl6leTGHtxAYDi2562YUBR4IrUQPCvRZmbD2BgeKuF62q24UIgMJkUjkNk8OFqECNmt05WuQwmH5diIFaZ1WLXlvy39ZkLUWVmZsJIIolzkLvs0ZMz6GT9kUECgJWIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JR9z7DK2_uQKEB4q0920h5C-3sxD2z58i_WygopF75fpJt_Tc163RVHWS7-tF-BJV9nz78oLI1x9aT3tTUUWxSPyEAc54KhLUBX_2koVGf0klRx_D6p_9Dg3ryIdiiGrUVsptS0JPVNiKkhUH-igff3jIzPw5LJoUDaM7WUtWPTNc6fq36O1fXJyfUUtAAL2Tlzo6IyyiOU2sMzWbQ4e3yxKKrBWhCeuFr29Dcy8B-gVQh-pBl2rbRH2VY8IJaHqKewUEGi1I-hP859rC9RMwYv3-JfKRcPmxqh2oRaOM5FcIWjvFXgFJ2wnMJ11-7YAkfM1jV_QT4Cg5VwjZF7Jkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HCGNQbHqGn-VK6Fy0m58Skpcr5jc8la3h_mgfx_e_kEj8Rem60gYlQfx-UB6HG30wXGPKdukuAhR_kaAapwR83Q_k1Br6gVF_P2cAwUCwxRK5DQpAmvriqBrR0zpecmJxVnBYePFudNN3xjeXOMThaCHpRcC9Hqe-eadE4-n9Z-AnZcg3HahsYPX1RIjqKzTpudEeDw8ZxAx7wJuMkgyv2BioJQP2jZ_yEBAThGKvCvlLieMAEda5pz3y1_OQqTK8xXvPjkSX0eHVI8_aKJ8tZE0UADiZ3IAosmEXoTgLHNqWmNl2rdY-wewt93W8k6Zy5NmzgYTk18av2FYGGgCoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r5QdCHeIF3oUyaTNNr0Ll024cB0FY5yBmV0Rm7gVZzKAyY1N0WxEDwXHhF17zPISyHV-EqyseZJnZ8I_YRrYli0pLIMambLVol4W3KVcAcuPUSdn1SGBmEG0kB_SpvCoKNRtjrZxbMETvqpsLJ3s89bT2Q-pE3ITIpwsm4ABbM2enaNqr3SjRjby2lcXBafuMCXkMD82AceByZQJZyI2dtI-m_A8U_0YMkuTeJJKqlx0FlRmeQk2RCyadtKAM7LBNsXDcWwDRw5xxtec9wZfgy4j4dFvEeckrtF8N6KHAj4M3VQriHmXnyyof7fqlFNwHT-MluSUZWXldSFf9t-ebg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/diLq9PvSASKy7_98i3G9MtGET4JM8rgdodvnx1fKxo04QCcQUZxzaoQIj2IMjPmmWqenhYfiFhl11L4mvD_33g8S40SpFgxQv4IyFq8iWdaLRfcG75S3q3wHbX2h3eISfH6BvRZnOEdbdypSHERECB3hdUzUzEAPoKCCFHRvqYAez_t6rgPZzYw6XdVfeMQoFYK1c_KvqWhIh_LlVQCoCSjA3wuHDVJhKXIZFdf-HKmlZfhAFJn2vMH4Ror78ATyBelumOXbD47IQEjk5Jvj0TmLNaF8VCfQJGCgfYlnxLxiPs5Vyj0I14u8phahxkzl6qqYdWL2uOdbl0VT0rsVrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مزار رهبر شهید میزبان حضور مردم شد
عکس:
حدیث فقیری
@Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/448994" target="_blank">📅 20:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448993">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d5222c635.mp4?token=GLRLS2xCgs7mccmmAb9isZ1TYbI9dpg3vec7JlLZg0Yy96TlMtNRl6R0vuzhSbpaR85uJcaE5tK4FapcS29o6e7mEp2PTBp7NMXOS1zJ6bvbzqgtKr_FxxGF5FbR2Kff-9xGSB-L5T5xOvUzABvKTBnMvFdk1jGSvOFjpAoQQAulgBPVyMXHR4gNH4iR4ymY3_CmDoeUJsU_3iRWZ-uBCYCtg6pCSPYPCqxNxH-yrrBSaLftjtkPFyymQsyL6bVK4vfxf2p0qxv-T87WHfnh3zr6gZuIOfEHhL4sHDJ1GjoVphRldEMRYVi0ti7kauqiDqDLCoWuQPizrxOA_h9YvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d5222c635.mp4?token=GLRLS2xCgs7mccmmAb9isZ1TYbI9dpg3vec7JlLZg0Yy96TlMtNRl6R0vuzhSbpaR85uJcaE5tK4FapcS29o6e7mEp2PTBp7NMXOS1zJ6bvbzqgtKr_FxxGF5FbR2Kff-9xGSB-L5T5xOvUzABvKTBnMvFdk1jGSvOFjpAoQQAulgBPVyMXHR4gNH4iR4ymY3_CmDoeUJsU_3iRWZ-uBCYCtg6pCSPYPCqxNxH-yrrBSaLftjtkPFyymQsyL6bVK4vfxf2p0qxv-T87WHfnh3zr6gZuIOfEHhL4sHDJ1GjoVphRldEMRYVi0ti7kauqiDqDLCoWuQPizrxOA_h9YvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرائت زیارت امین‌الله در اولین شب پس از تدفین رهبر شهید انقلاب در حرم مطهر امام رضا(ع)
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/448993" target="_blank">📅 20:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448992">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EiA63DaSts2dXYnYJiae8Cu4ciDyT0DF8tYhFlFqJQ1VYlF_GonEtLaWKLxHnC511Jrvfstqu1ubhVTYmKSedp7E4g35M0-hRf7fRFgSwVrjCLqu58LQ3i7YQ4y8YusyrZD49Amyjhm1b-9_pxML677UC5Tjc9QqrBtyfJsGxZkrGZ3oA1zgNXFug__m344k1FZZHD6XRYQ0IBYFYPqlBpJooM4c0LzjUPC2jgS7jNSjMSWz66OgWfo9R-1OmCS7Y6zEXgbC28RsdJp2_uAix6_MwDPcH86NSSPy1X4iZqqNu61DKGJk3fl_WQP9bA4M3jEKPmc5rRHbmbAMoyz_Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
بانک شهر برای جذب نیروی «بانکدار» آزمون استخدامی برگزار می‌کند
🔹
بانک شهر به‌منظور تأمین بخشی از نیروی انسانی مورد نیاز خود، از میان متقاضیان واجد شرایط، در رده شغلی «بانکدار» نیرو جذب می‌کند.
🔹
به گزارش روابط عمومی بانک شهر، بر این اساس، فرآیند جذب از طریق برگزاری آزمون کتبی و با همکاری مرکز سنجش دانشگاه آزاد اسلامی انجام خواهد شد و متقاضیان واجد شرایط، اعم از زن و مرد، می‌توانند در این آزمون شرکت کنند.
🔹
داوطلبانی که در آزمون کتبی حد نصاب لازم را کسب کنند، به مصاحبه‌های تخصصی و عمومی دعوت خواهند شد. در صورت موفقیت در مراحل ارزیابی، فرآیند به‌کارگیری آنان مطابق ضوابط، مقررات و آیین‌نامه‌های داخلی بانک شهر انجام می‌شود.
🔹
بر اساس شرایط اعلام‌شده، دارندگان مدرک کارشناسی با حداکثر ۲۸ سال سن و دارندگان مدرک کارشناسی ارشد با حداکثر ۳۰ سال سن (مدت خدمت سربازی آقایان به سقف سنی اضافه می شود) و همچنین داوطلبان صرفا دارای سابقه بانکی با حداکثر ۴۰ سال سن، مجاز به شرکت در این آزمون هستند.
🔹
متقاضیان برای اطلاع از شرایط ثبت‌نام و جزئیات آزمون می‌توانند از روز سه‌شنبه ۹ تیرماه به پایگاه اینترنتی مرکز سنجش دانشگاه آزاد اسلامی به نشانی:
https://azmoon.org
مراجعه کنند. همچنین این آزمون استخدامی در تاریخ 9 مردادماه برگزار خواهد شد.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/448992" target="_blank">📅 20:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448991">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/448991" target="_blank">📅 20:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448990">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ddc860633.mp4?token=XpMXlEd0mQFOgQXYsCrOG8X06vu1RhyD4SjVY4M8UzR5tUciHTvvhf0t69Blz0BraRvwSQ3ddiDsxXXY2CYPTWKTEZAYGDBz6W2w4cRnItllbyUiBjicKyI6g786wfyvu0bo4Qctpyk9MvQNUVH7Nk2VN2FVlpnpi7_8HilM7rC7bxhI0vnNWEoxnR9Qyd4tkJfH82IDt9X53CmBZyvVY-LFKVKskzNmApxX2UyZVUhBHvnYJciYpI4JbFjkwFiQXog9c9fOg8Y1K04nqPnS6b70ercLnyV4vFkV6s-6j5qwmpQcMcXdZMm94He6af3yjtDaK_SYq0TtwDe9KqapSx15bXXwEYYYThrVsDaaDpiGwROrUve4_9yllfvcVb6BfLu8X-bgKSN6cK9E0YzitSvuMcceWKUtomA2yi7GQM56mKI-hBNFMT_Ya6keI6-Y0p0gEdbhidk07kkDGMrbxK2gNK_Vovdv5NN93vIC0AbSy0O2hRpXffqb4g1yHDOfjLnsczedEFKvXx_wDo4R1Dd0cG527gl_Lie0ZXMxBE7x-oAU47tJY2Fy0kl0LifUIh0HrQwLwW70gbfw1S83QG7x_i1NV85CuHDbk0_9qZNABgS9tnN3jniUUolOUk2d2ywQJeuDj4ftPWaHj505Uv07iDSuMGeul1V0RAbzUEE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ddc860633.mp4?token=XpMXlEd0mQFOgQXYsCrOG8X06vu1RhyD4SjVY4M8UzR5tUciHTvvhf0t69Blz0BraRvwSQ3ddiDsxXXY2CYPTWKTEZAYGDBz6W2w4cRnItllbyUiBjicKyI6g786wfyvu0bo4Qctpyk9MvQNUVH7Nk2VN2FVlpnpi7_8HilM7rC7bxhI0vnNWEoxnR9Qyd4tkJfH82IDt9X53CmBZyvVY-LFKVKskzNmApxX2UyZVUhBHvnYJciYpI4JbFjkwFiQXog9c9fOg8Y1K04nqPnS6b70ercLnyV4vFkV6s-6j5qwmpQcMcXdZMm94He6af3yjtDaK_SYq0TtwDe9KqapSx15bXXwEYYYThrVsDaaDpiGwROrUve4_9yllfvcVb6BfLu8X-bgKSN6cK9E0YzitSvuMcceWKUtomA2yi7GQM56mKI-hBNFMT_Ya6keI6-Y0p0gEdbhidk07kkDGMrbxK2gNK_Vovdv5NN93vIC0AbSy0O2hRpXffqb4g1yHDOfjLnsczedEFKvXx_wDo4R1Dd0cG527gl_Lie0ZXMxBE7x-oAU47tJY2Fy0kl0LifUIh0HrQwLwW70gbfw1S83QG7x_i1NV85CuHDbk0_9qZNABgS9tnN3jniUUolOUk2d2ywQJeuDj4ftPWaHj505Uv07iDSuMGeul1V0RAbzUEE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ما را به سخت‌جانی خود این گمان نبود...
@Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/448990" target="_blank">📅 20:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448989">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/263f294669.mp4?token=LGTGhgNHTIxw-6fXoMv1rMzvIMjipd_wv0JCARbD7t925dNtmPqMiA9S47FaEnegTmQRm1KuRm6DbKBgylcjynJ8J36d7H-kYq3uQoll52QwymJM0y-lMaXB4EVKVwviAniJ4p0oNfvDUI_eHL_E6i0jE-yZtm6mqlPDqGpoBp0W0MyQE_yDp4jrgRK7lvNtR2QRC6XXjPCEKHGqPZDc-3oa8Ktph85zeJmgr7cBbJZ0BC9QtIk7W5sl7J8T7xJLODvfARnWEKp7xVgI_zejKCaibiKsfBLVsy5oAK7qRZgEdUfayl5u42ZPP7ymJ27BZHBN3CYV0o9u2XO9-Yz5-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/263f294669.mp4?token=LGTGhgNHTIxw-6fXoMv1rMzvIMjipd_wv0JCARbD7t925dNtmPqMiA9S47FaEnegTmQRm1KuRm6DbKBgylcjynJ8J36d7H-kYq3uQoll52QwymJM0y-lMaXB4EVKVwviAniJ4p0oNfvDUI_eHL_E6i0jE-yZtm6mqlPDqGpoBp0W0MyQE_yDp4jrgRK7lvNtR2QRC6XXjPCEKHGqPZDc-3oa8Ktph85zeJmgr7cBbJZ0BC9QtIk7W5sl7J8T7xJLODvfARnWEKp7xVgI_zejKCaibiKsfBLVsy5oAK7qRZgEdUfayl5u42ZPP7ymJ27BZHBN3CYV0o9u2XO9-Yz5-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تلاوت آیاتی از کلام‌الله مجید در مراسم بزرگداشت رهبر شهید انقلاب در حرم مطهر امام رضا(ع)
@Farsna</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/448989" target="_blank">📅 20:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448988">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e24b27639.mp4?token=FRXgUqCj6YzyA2ZeO4TIb0BLxmgQGHZ8r_6FzKbpEPnlxhFtoSk_RvLR3-W2j9GmGC5paeDFr6JSjvBWKEmxqwIcFLtSqCeKjpB4voLkrDH2uBlIylBTnhdmHr_o3VcuDF5lkrOCj4u9NL_5EDdPYn7to1GsR-2kfEonvVhnj3ZQdm70mA6Lvg4U9pAlCohmWYFnjgjRDFshoM3ane5_4bdL_-yfjNcT-26O1xl4fGqM0iQHs9s_yscWzbT3cWQKU-Ed__PKwepW-IhpO6Wc2-ESlunMXhiBnuHzdcSfrjOmyTNto09NEYqfvkrkjpTW3vPJuVu4lO63pHkb0vvj_4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e24b27639.mp4?token=FRXgUqCj6YzyA2ZeO4TIb0BLxmgQGHZ8r_6FzKbpEPnlxhFtoSk_RvLR3-W2j9GmGC5paeDFr6JSjvBWKEmxqwIcFLtSqCeKjpB4voLkrDH2uBlIylBTnhdmHr_o3VcuDF5lkrOCj4u9NL_5EDdPYn7to1GsR-2kfEonvVhnj3ZQdm70mA6Lvg4U9pAlCohmWYFnjgjRDFshoM3ane5_4bdL_-yfjNcT-26O1xl4fGqM0iQHs9s_yscWzbT3cWQKU-Ed__PKwepW-IhpO6Wc2-ESlunMXhiBnuHzdcSfrjOmyTNto09NEYqfvkrkjpTW3vPJuVu4lO63pHkb0vvj_4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هم‌اکنون؛ اقامه دسته‌جمعی نماز لیلة‌الدفن برای رهبر شهید انقلاب در حرم مطهر رضوی.
@Farsna</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/448988" target="_blank">📅 20:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448986">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">تکذیب ادعای العربیه و فاکس‌نیوز درباره مذاکرات هفته آینده ایران و آمریکا
🔹
درپی انتشار اخباری از سوی العربیه و فاکس‌نیوز درباره برگزاری دور جدید مذاکرات ایران و آمریکا در هفته آینده، پیگیری‌های خبرنگار فارس از یک منبع آگاه نزدیک به تیم مذاکره‌کننده ایرانی بیانگر این است که این ادعاها صحت ندارد.
🔹
این منبع آگاه در گفت‌وگو با خبرنگار فارس، اخبار منتشرشده درباره نهایی شدن مقدمات مذاکرات در اسلام‌آباد و همچنین ادعای ادامه گفت‌وگوهای فنی در هفته آینده را تکذیب کرد و گفت: این اخبار کذب بوده و هیچ مبنای واقعی ندارد.
🔹
وی تأکید کرد: اخبار مربوط به روند مذاکرات، در صورت وجود هرگونه تحول، صرفاً از مسیرهای رسمی جمهوری اسلامی ایران اطلاع‌رسانی خواهد شد و ادعاهای منتشرشده از سوی برخی رسانه‌های خارجی قابل استناد نیست.
🔹
گفتنی است، شبکه العربیه در ماه‌های اخیر نیز چندین بار اخباری درباره روند مذاکرات ایران و آمریکا منتشر کرده بود که پس از تکذیب از سوی منابع ایرانی، نادرستی آنها آشکار شد.
🔹
این ادعاها در حالی از سوی العربیه و فاکس‌نیوز منتشر شده که ترامپ روز گذشته در واکنش به برگزاری مراسم تشییع رهبر شهید، عصبانی شده و با فحاشی از پایان تفاهم سخن گفته بود.
🔹
با این حال، کمتر از یک روز بعد، برخی رسانه‌های وابسته به آمریکا از ادامه مسیر مذاکرات و گفت‌وگوهای فنی خبر دادند؛ تغییری که از نگاه برخی ناظران، نشان‌دهنده تناقض در مواضع اعلامی دولت آمریکا درباره روند تفاهم با ایران است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farsna/448986" target="_blank">📅 19:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448985">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6f20a3c0d.mp4?token=hEQJmJ6zkeJqosky0WmFhgJkaOEAPaL3tuBFfaDMjoeaua4unNs0gJPb4GzzBwu_MnEFMAIN0G70teq5_NCMGMsRPl9cph02PHvDjWnCjbzenKFiHqCFFOT9Hcct2eHZU2t441XqbZlcbddm_p3cELH6hPY_qNXTm6RbUumAHm95urE6pMfmEw8alKlulJqxLiw6SB4SAXD2_3299qJB7l1yRauo5k8grsuz1_t6i2VB1qa5kWb946TyEfyWwxIah5BJcX6lQtAT40zvH9bf1pgy4d2gwMlyo778quy8xXG2Rl2jwKIbF_gcXQpa82CnSLA2Qq6f_Eg3wiOGqFkqNrSET7N1En4bI-ZUbmwrOsdWHOEdngmndt9T3NfZwdf0gpDZ-lC70JobzCEQYeLX7IlKeKYQKdTyouNETV0Gm1vSc_uYbBdCNlf21YuJX2JafCWXVIdwEPT24PDCRf04FbmYGuNtMncoB6Ro3FSYNaFqwDpq0DgpjolvNyRjIiCoiteQ6eRQ9ZRKVJsdSexfAk1p_B4IRkzJyh_7yL7fi2UwuU0384peuWa1MOkbw428bzV478pcfWwEzf3Ttm0jdpLlZEJe2ambDeAROy_yoTgVrReGTGzGg7OyndfuR1DrmzpzkTKGOgqDiZcDkdGaqfW4kYou2cG_ewLOlnJT6aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6f20a3c0d.mp4?token=hEQJmJ6zkeJqosky0WmFhgJkaOEAPaL3tuBFfaDMjoeaua4unNs0gJPb4GzzBwu_MnEFMAIN0G70teq5_NCMGMsRPl9cph02PHvDjWnCjbzenKFiHqCFFOT9Hcct2eHZU2t441XqbZlcbddm_p3cELH6hPY_qNXTm6RbUumAHm95urE6pMfmEw8alKlulJqxLiw6SB4SAXD2_3299qJB7l1yRauo5k8grsuz1_t6i2VB1qa5kWb946TyEfyWwxIah5BJcX6lQtAT40zvH9bf1pgy4d2gwMlyo778quy8xXG2Rl2jwKIbF_gcXQpa82CnSLA2Qq6f_Eg3wiOGqFkqNrSET7N1En4bI-ZUbmwrOsdWHOEdngmndt9T3NfZwdf0gpDZ-lC70JobzCEQYeLX7IlKeKYQKdTyouNETV0Gm1vSc_uYbBdCNlf21YuJX2JafCWXVIdwEPT24PDCRf04FbmYGuNtMncoB6Ro3FSYNaFqwDpq0DgpjolvNyRjIiCoiteQ6eRQ9ZRKVJsdSexfAk1p_B4IRkzJyh_7yL7fi2UwuU0384peuWa1MOkbw428bzV478pcfWwEzf3Ttm0jdpLlZEJe2ambDeAROy_yoTgVrReGTGzGg7OyndfuR1DrmzpzkTKGOgqDiZcDkdGaqfW4kYou2cG_ewLOlnJT6aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عضو ارشد انصارالله یمن در برنامه پرچمدار: آمریکا و اسرائیل تاوان به‌شهادت‌رساندن آیت‌الله خامنه‌ای را خواهند داد.
@Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/448985" target="_blank">📅 19:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448984">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21ce956558.mp4?token=diyZQyzxIGkaJmmEkkDjRJoCP1hdXUG0-vX73Sp72jhtcRqOHpRgEuU-WOjUWi8_UFcx_Mnoi_f_pnjXuDNfpbHql73GGmR_uf0c0bsbfTtBwCCRTBXHUZ-d7NtRQ-MwNXy-30i1X01kqkcW3Wm_g--afY4eqQyr3fHaSMVnS6wsUZb_TWxCMMCHhlhN_9PqB7qUpKHMm5w_sE0wNfmMnR1HKA1vfzUQz55vZGeXcaXk3elC4vG2cgQGoFQYNJ_bgR5tB39BHr2d8Z1UUNscm7YJglAMILyoRv3-osjr4y1DaCHsm32KsTZVEVU2HgYIJkxEu1aPs6QtRH3NRCHDKFznebM9EHfbxbpORvgXicyoy0NDkW5fnvbESqN6AAkA7BI2kZeS5anLwFNvuCDSr1_kqN7ykeB_1Chyne1E2OB06wiE7WtHuqyyy5-LV2S6PZIQ8WphzyUisk8YGrOGgz9QpJnAvWXeuE-DCmSDXyndsstPANp4CRvnKNIjP_xA8l6ReMR3JXDJpv1il1pDhstlRF6tKNlm1MFCO4lQRb6UdGQtdraV_u59agznJa5SbZvMIqSpEQetxOGxjkhAmAMNyYRSA9s17Btn9Pb3xKcE9gabsfCnvz-LKY7qE0KmHe2IJTiHejxbyXuDP7-RPjTLg6R1aaEwgxLrvoKROEc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21ce956558.mp4?token=diyZQyzxIGkaJmmEkkDjRJoCP1hdXUG0-vX73Sp72jhtcRqOHpRgEuU-WOjUWi8_UFcx_Mnoi_f_pnjXuDNfpbHql73GGmR_uf0c0bsbfTtBwCCRTBXHUZ-d7NtRQ-MwNXy-30i1X01kqkcW3Wm_g--afY4eqQyr3fHaSMVnS6wsUZb_TWxCMMCHhlhN_9PqB7qUpKHMm5w_sE0wNfmMnR1HKA1vfzUQz55vZGeXcaXk3elC4vG2cgQGoFQYNJ_bgR5tB39BHr2d8Z1UUNscm7YJglAMILyoRv3-osjr4y1DaCHsm32KsTZVEVU2HgYIJkxEu1aPs6QtRH3NRCHDKFznebM9EHfbxbpORvgXicyoy0NDkW5fnvbESqN6AAkA7BI2kZeS5anLwFNvuCDSr1_kqN7ykeB_1Chyne1E2OB06wiE7WtHuqyyy5-LV2S6PZIQ8WphzyUisk8YGrOGgz9QpJnAvWXeuE-DCmSDXyndsstPANp4CRvnKNIjP_xA8l6ReMR3JXDJpv1il1pDhstlRF6tKNlm1MFCO4lQRb6UdGQtdraV_u59agznJa5SbZvMIqSpEQetxOGxjkhAmAMNyYRSA9s17Btn9Pb3xKcE9gabsfCnvz-LKY7qE0KmHe2IJTiHejxbyXuDP7-RPjTLg6R1aaEwgxLrvoKROEc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوهٔ خردسال رهبر شهید انقلاب، شهید زهرا محمدی گلپایگانی همراه پدربزرگ خود، حضرت آیت‌الله العظمی شهید سیّدعلی خامنه‌ای در یک مزار به خاک سپرده شده است.
@Farsna</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/448984" target="_blank">📅 19:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448983">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس افغانستان</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be4d3fe5d7.mp4?token=jaSCLZb_jwbodsUHIMPvyMl60rUqYBN9BJtVc4YbsGt2AsXCPDpTxJswfFgs1gEVAvWmxHeae5cQ6bHvupTMxA4Lkrs4hZFUivRamGrHCaZdrQ5Dj3oPlvyO7HrrMBmGhUv2dicNvuHC7rHu0yDwnaZ4k3Pq6Y9PD_6NL8CNP7UMzilOsZVeivTKZSUKrZ-bo1GYzbe8syybWVPF6ix736Kj3nvjC9Hw8kO0T7FRkDCjB5-uJsbRmsgCOgReL7We-2eV_onRBF-dt9C8cpDYBetShG77qVha9IpA-8HMD3NTuYrGWae7SS0G8mqSnjIXs63pOM7cSt7fh48GND1GwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be4d3fe5d7.mp4?token=jaSCLZb_jwbodsUHIMPvyMl60rUqYBN9BJtVc4YbsGt2AsXCPDpTxJswfFgs1gEVAvWmxHeae5cQ6bHvupTMxA4Lkrs4hZFUivRamGrHCaZdrQ5Dj3oPlvyO7HrrMBmGhUv2dicNvuHC7rHu0yDwnaZ4k3Pq6Y9PD_6NL8CNP7UMzilOsZVeivTKZSUKrZ-bo1GYzbe8syybWVPF6ix736Kj3nvjC9Hw8kO0T7FRkDCjB5-uJsbRmsgCOgReL7We-2eV_onRBF-dt9C8cpDYBetShG77qVha9IpA-8HMD3NTuYrGWae7SS0G8mqSnjIXs63pOM7cSt7fh48GND1GwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▪️
گوشه‌ای از محبت افغانستانی‌ها به آقای شهیدان ایران
@Farsnews_af</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/448983" target="_blank">📅 19:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448982">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEg-33N8dYD1-lOfg40xyU7w2wk_67idXZmZSjcA80iOu7A5pJ5sgiQRR54X-aWpORTuZRL2Ig7x2J0a14E1JJItmSgNPRGTf2tkToaQpmeDAxTqDuEhxCOCNnv5mPHpPMDGK-eOqhIaPF3SUjjkqmc1HgjxWfCh_vV5tCnm13uYTCwOpYKgF46i1pM0IwhXJxnR7EsEcQbhC3BL7YwKDVBD3QDMnqeDid1fSqKuJRaoCu5X43AudEWjnwlte6hYHMEdeqfI121qC7Q8V626gI4p5_83k4jG0RoJrmeOBFG7siy89W7EySSR4vivfPVtH5gf6mlEEiP9pEqdwuBmaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدرالحسینی: تشییع ۴۰ میلیونی، منبع جدید قدرت ایران و جبهه مقاومت است
🔹
کارشناس مسائل بین‌الملل: حضور بیش از ۴۰ میلیون نفر در مراسم تشییع رهبر شهید سرمایه‌ای راهبردی برای جمهوری اسلامی و جبهه مقاومت است.
🔹
این حضور، قدرت بازدارندگی و نفوذ نرم ایران را تقویت کرده و در صورت بهره‌برداری صحیح، می‌تواند معادلات سیاسی و امنیتی منطقه را به نفع ایران تغییر دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/448982" target="_blank">📅 19:15 · 19 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
