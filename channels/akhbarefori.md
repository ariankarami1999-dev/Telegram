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
<img src="https://cdn4.telesco.pe/file/qBBaAtJ09tqvVINbISTTwahx4ofkV1RKngVrJ9Eeste1H3iMP4chdLAZpmp60wnbsh_cAzFXkqo1vmsTBLRfqzSV2R0AEDvEiUln6FZDIixY5vqyDUSKjOUD7rFO0yetAuybAkzsPNsBwHp3KjDzzqG7YaOhUVqqX25Q94bFwvvbLt4ydZnFi-h8q403kyHPdENwSH54eQxKyfmaVE06bYz2Znw5ml0z75fIbF5QveBIVvv8pfxsALAMaClIArhJDQhGaP_x5EL0G29SVnd_fol_y03EB2dKd-ConnDkgY6CDthm389Ayv1LZai59yyvDtsR721VZKG_pwKn-DaFJg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.38M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-08 17:38:01</div>
<hr>

<div class="tg-post" id="msg-685575">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sx6BoBNJt3LfYGGizqPR8Ly9Em_ck-vNpA0mTnxFOtysbEzaOk7S7gGWsq5OYmYxEpKAkujoxQCc3aAwFaJZZcp_Uy680d7UAUMICsRStbXRfaaVYmvVdhshCGKB4HRR9NvbxpUCpvdieEL99jm8riuxxLagayLtxrz9WI4wvGx8XhvAhvuiv4pv7bODC9GSNPLZE60VTEJ8siObO6mopwTZb9WjKCXltVd6tBEy-_MtOsUftmxpwAzoGh_Yo2zcsEt3_Zmsdss1QjqSGiBF6JzVVBZV1WCyk8QsxrkAnJzTbOFzYpP6RlEiak0ZtseGZGV-z65H9yxFVfHHYdqgxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#همراه_اول
صدرنشین پوشش روستایی، جاده‌ای و توسعه 5G
🔹
تازه‌ترین گزارش
#رگولاتوری
در بهار ۱۴۰۵ نشان می‌دهد همراه اول در سه شاخص پوشش روستایی، پوشش جاده‌ای و تعداد سایت‌های
#نسل_پنجم
، بالاتر از سایر اپراتورها قرار گرفته است.
🔹
پوشش ۴۴ هزار و ۹۱۸ روستا
🔹
پوشش ۸۲ هزار و ۸۳۰ کیلومتر جاده
🔹
راه‌اندازی یک‌هزار و ۴۳۲ سایت 5G
🔹
براساس این آمار، همراه اول در این سه شاخص جایگاه نخست را در میان اپراتورهای تلفن همراه کشور به خود اختصاص داده است./ سیتنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6 · <a href="https://t.me/akhbarefori/685575" target="_blank">📅 17:37 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685574">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
چرا ترامپ از تهدید نظامی ایران عقب‌نشینی کرد؟
@Tv_Fori</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/akhbarefori/685574" target="_blank">📅 17:32 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685573">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
لحظه شکار مزدوران سعودی توسط ارتش یمن
🔹
نیروهای مسلح یمن ویدئویی از حملات دقیق پهپادی علیه مزدوران سعودی در مناطق مختلف یمن منتشر کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/akhbarefori/685573" target="_blank">📅 17:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685572">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
درگیری مسلحانه در اربیل عراق
🔹
گزارش‌های اولیه حاکی از وقوع درگیری‌های شدید مسلحانه در استان اربیل، واقع در اقلیم کردستان عراق است که منجر به تلفات انسانی شده است.
🔹
هنوز آمار دقیقی از تعداد نهایی قربانیان و مجروحان این حادثه منتشر نشده است./ تسنیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/akhbarefori/685572" target="_blank">📅 17:16 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685571">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80e26c0994.mp4?token=t-D2vN9Tx9Cs0jaAbSAGu0YnkJ7Yk8gnzd72L9FOgRO7bGdh9TxSVNb43TZUIcM8CrIh18GAZSKHSatrT7lZ6LJNSnQdufr73OcgJ2IgbEXkdU-poFFio4bUOP2uni-LFX95fhhaNamrDJo2ZlVqyhUW_5l3YeBXPkYN0R7Q0_c0qs3snIFGX7JhXjsd8XsxVWpAKnLsxQzqAyQ8Ztzpl9w_TAM6zA4iFy9vAHs3GLpKAKgeHl8QS8HQu-rExC9YK9fUf4PXbOCLHZpkP-n9Awc4yhfowfixcd8dOknKJeSoNcnafjRYghOdKRzB9ZdEIGafDT2gaSgAoX82yrL-rIPiUNRB1EcyrHTqGdXhDSxcedMJiDqOoNIWc6caBvzNwsY2Mrf9nkvRF7xf7EemmlqOobGNcExq9E0Pd5l9_duRWV7TJWaAFSpdImcN6B8V7B2Bq2qC8c9qrDN3sISOI-Bfn7b-8Yhw-ZJ033aXkRNDeZvMpaxkcZc6twd4rRQ9zCmSf6UVMhUDiQuP5fsdvVBxcEGCAXhx_P26hs53o8FgHPJkj3FMblf9EEFnEsuGEJ_JrE2UE-Po-3w29GnhXSq7tBoFasSvIKgpPiwnPXYTeE9hbiqcsdHM5PuWZwhmTDUCDEnvXy0baI-Bs7qvS_5LkoUFn_fYPEFAUcAosdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80e26c0994.mp4?token=t-D2vN9Tx9Cs0jaAbSAGu0YnkJ7Yk8gnzd72L9FOgRO7bGdh9TxSVNb43TZUIcM8CrIh18GAZSKHSatrT7lZ6LJNSnQdufr73OcgJ2IgbEXkdU-poFFio4bUOP2uni-LFX95fhhaNamrDJo2ZlVqyhUW_5l3YeBXPkYN0R7Q0_c0qs3snIFGX7JhXjsd8XsxVWpAKnLsxQzqAyQ8Ztzpl9w_TAM6zA4iFy9vAHs3GLpKAKgeHl8QS8HQu-rExC9YK9fUf4PXbOCLHZpkP-n9Awc4yhfowfixcd8dOknKJeSoNcnafjRYghOdKRzB9ZdEIGafDT2gaSgAoX82yrL-rIPiUNRB1EcyrHTqGdXhDSxcedMJiDqOoNIWc6caBvzNwsY2Mrf9nkvRF7xf7EemmlqOobGNcExq9E0Pd5l9_duRWV7TJWaAFSpdImcN6B8V7B2Bq2qC8c9qrDN3sISOI-Bfn7b-8Yhw-ZJ033aXkRNDeZvMpaxkcZc6twd4rRQ9zCmSf6UVMhUDiQuP5fsdvVBxcEGCAXhx_P26hs53o8FgHPJkj3FMblf9EEFnEsuGEJ_JrE2UE-Po-3w29GnhXSq7tBoFasSvIKgpPiwnPXYTeE9hbiqcsdHM5PuWZwhmTDUCDEnvXy0baI-Bs7qvS_5LkoUFn_fYPEFAUcAosdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش‌ها به پیام محسن نامجو به همسرش | آیا او به همسرش نگفته بود به ایران می‌رود؟ | نامجو یک هفته پیش از بازگشت ناپدید شده بود!
🔹
بازگشت ناگهانی محسن نامجو، خواننده و آهنگساز سرشناس به ایران پس از نزدیک به دو دهه مهاجرت، به یکی از داغ‌ترین سرخط‌های خبری…</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/akhbarefori/685571" target="_blank">📅 17:15 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685570">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nR_byhIsZXRpbJZ1bK6sCZ4rLxXMIQWWHWWkmb_AD4jrsA0x3up-rPFIo6A0qRa0hiLVyAlRae3YxlNYNruebSojszmHlZjMHjk1Rgm0Imyl2tWqOpWH6CDo3f5lGmbGRSm-X41QHgnWGzeQ7F748vOvxR8VJOdrscY0yXOooo-20FNmFTCPpyTnqzu3YJfjxieiXkLM6ra_x3JJfQlqsCtObtfiL6lMiEuIENXPJQkfUM6u1zHEzzXALmF7LR_nHAQgtr7X6bN3VvNiEX12egfHu6KaIjyp0-FIhnHjUR7stgbikZbA5r-osdZhlp5gPkbfUbCgLqgYB6e5LFPCEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شبکه CBS: ترامپ با خبر آتش‌بس با ایران، نوسان نفتی می‌گرفته است
🔹
حساب‌های سرمایه‌گذاری ترامپ در سه ماههٔ اول سال، حدود ۳۶۰۰ معاملهٔ سهام یا اوراق بهادار به ارزش کل بین ۲۱۲ تا ۶۹۵ میلیون دلار انجام داده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/685570" target="_blank">📅 17:06 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685569">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUqiJy4FO3JqBop6mnNVeR2of58ZJ9beq3DHVl2SqciK2eSsLcIxUGotvxekqK-DmJtEGWeLI4u81zUG_Q_ojNm3EpeuEvDNfjh4_0BldkXB17QwvPpGKvsKwOgxz74FpNE86lPHcjMejI608HtY-njbvcSQgGeH-dMHpDlC2H71MLYFLIECkDfN3smepMp1RfU0XWaYmZ01HXZ3qboB15UY801DpOlzx_qdCdIAfhNL9ingg2CDaQDfn9RH9ErUZbmBwzNhXdAjh14tVNLoNjNrFRzYkUYO32UhDFRakcbztEO39XXn8KWmqE4cFDTkh4c3SLIOZzaHrZ5cstxPdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاربر اسپانیایی: ترامپ کاملاً دنیا رو بی‌ثبات کرده. دیگه قانونی بین‌المللی وجود نداره؛ می‌تونی کلاهبردار مالیاتی، پدوفیل یا جنایتکار جنگی باشی و انتخابات رو ببری، رئیس یه کشور بشی و مثل هیتلر تو زمان خودش برات هورا بکشن. واقعیت وحشتناک جدید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/685569" target="_blank">📅 17:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685568">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEREh-oEH95dh2ccJvZd0wvjXCDgetBZdzskxciRLi1GXTKW9w2e5AEaihg8XUsS3z-fGOgwMRq4GnFA9HK-yUl31Tr4RF2L4zKz7HYslGIV8dhnTtuOtUDwbbhB7OQbXyDTvB0xtsWETXSvHnnKjkJquzHMQ9gbE436-WcmuNTzjdj564EUQE0VkKRN6EBnWWiuOowErQux05XOHrU7BLe70ldNDNQX0DXsGUWm6TYYYWX1a3rUHShcz6t43Tu0ubrHHI609QID1rmqilBknYbit-fE1-pwTfob8hQk-iyNO4ax7wDannylxwr2N3MvWI0btykl6wVMqBQVA2g7dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روزنامه‌نگار و مفسر سیاسی کانادایی: دونالد ترامپ فکر می‌کند اگر مدام چیزهای احمقانه در رسانه‌های اجتماعی پست کند، ما فراموش خواهیم کرد که او با جفری اپستین به کودکان تجاوز کرده است
.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/akhbarefori/685568" target="_blank">📅 16:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685567">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/227990e230.mp4?token=k9RFrzOTgLaDsY6hKRPJDIj0D79rZ60ivBPhY-yjVqnE8dMceafsGmWmTWWLBEvjzbfEw4cyjaTr-2OUpAOkd4RKU4uH8_L4gaVOOHoe4ZNtqoMaMNIz1kpD-wgTjH-F7JqbGrmRKN3l_G8ixemw2K08fpVYU3o_xpoFrRwK8MH7p72DQkYtDl7F8MP4ycJecqjfDBFDR99gIA7eG2sU4smfTJW_4QLaPvYhb_9i9R1s3WCLe2-7942a03TXCL9K8_lulqBr_Ol8VUdgtGxkCakN_iYD6lPoAWwd2k_PDILaQXZpNZVvbu1YloNuUzcoNnvKaoR7ctYDK405NA5WXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/227990e230.mp4?token=k9RFrzOTgLaDsY6hKRPJDIj0D79rZ60ivBPhY-yjVqnE8dMceafsGmWmTWWLBEvjzbfEw4cyjaTr-2OUpAOkd4RKU4uH8_L4gaVOOHoe4ZNtqoMaMNIz1kpD-wgTjH-F7JqbGrmRKN3l_G8ixemw2K08fpVYU3o_xpoFrRwK8MH7p72DQkYtDl7F8MP4ycJecqjfDBFDR99gIA7eG2sU4smfTJW_4QLaPvYhb_9i9R1s3WCLe2-7942a03TXCL9K8_lulqBr_Ol8VUdgtGxkCakN_iYD6lPoAWwd2k_PDILaQXZpNZVvbu1YloNuUzcoNnvKaoR7ctYDK405NA5WXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تذکر مادر لیلی رشیدی به وضعیت نشستنش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/685567" target="_blank">📅 16:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685566">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
خبرگزاری فرانسه: سران ایران، چین و روسیه با هم دیدار می‌کنند
خبرگزاری فرانسه:
🔹
پوتین، شی جین‌پینگ و پزشکیان، در یک نشست دو روزه در قرقیزستان با یکدیگر دیدار می‌کنند.
🔹
حدود ۱۲ رئیس دولت به بیشکک، سفر خواهند کرد تا بیست‌وپنجمین سالگرد تأسیس سازمان همکاری شانگهای (SCO) را گرامی بدارند.
🔹
این گروه شامل روسیه، چین، هند، پاکستان، ایران، چهار کشور آسیای مرکزی و بلاروس، متحد مسکو، است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/685566" target="_blank">📅 16:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685565">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fd07QA7pTt8rwaU6Xvd73blCEtjEstXDhGHuJH1rZ9EP_LToMMOq-YeNRwiSrA4Xug01gF0i7z8vFoC3o_oR6XVI36L3u1SVqM9VO8Lkj7cg2QjUExS7i6yDmRIGoYBf9lY-YMCL8Hn0PI9fj14H0StDsH_3n7X_MZXPOikLps2Ffz9-f9WZj2FbmCmMddng83tx6ek7nTLnUJq7TS0WX6nDs4hKXos1_LbhFacJHw7ZiasgnUqzK9tuW0XP-nG9a_AjfwcHTiTrKRzHX682jJDjgo1_eHXAj0bHRgsWHD2JxPpXcj6--SJSHHKp_lQSj81yBXiMZ_ISWCYu_12yDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ماجرای اتهام جنسی به محسن نامجو چه بود؟ | یک فایل صوتی جنجالی و میراث یک اتهام | شاکیان او چه کسانی بودند؟
🔹
شهریور ۱۳۹۹ و در جریان داغ شدن جنبش آزارهای جنسی عموما از سوی جامعه ایرانی به یکباره نام محسن نامجو مطرح شد. اما این پرونده به کجا رسید؟
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3241480</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/685565" target="_blank">📅 16:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685564">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
پزشکیان فردا به قرقیزستان می‌رود.
🔹
بانک مرکزی: خداحافظی با چک‌های رمزدار؛ چک تضمین‌شده جایگزین می‌شود.
🔹
سخنگوی دولت عراق: پیشنهاد مطرح‌شده مبنی بر تمدید حضور نیروهای ائتلاف(آمریکایی) در کشور را نپذیرفته‌ایم.
🔹
رویترز: ترامپ به خاطر جنگ علیه ایران هزینه سیاسی سنگینی می‌پردازد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/685564" target="_blank">📅 16:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685563">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61bf3a6e5b.mp4?token=BLsA8VjAq38QKSs0EbsXepyt68Op4VCNn-SfN8Lon1n9gTTIcGxZ2QQUUMcH00nwW0fhuybBIt1uMnk9NT9MJ-QhyjFZK2CUlSiNYk0mSA5Adb2JWHGJeeY1R0UTVucban0G0OZ-14g3g4PFxBuhY1t3WY-5jvSCXsdB2TyEMjXGF3Qrgx1RzVURsPqNcGiLNm509j-ZWWIZajUMLVti5bQh6y2Wipk38ZZcYBPlwEP1AMNEJdeli6aFeaP5Nv_9lAF4KFINzsY6vteBfe5xWyPOZx98XWQpWKEkTPr1-LVqPTIS6zLZmjPVMcW7oRYuRljQFsiy48bFyqeI49Zwrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61bf3a6e5b.mp4?token=BLsA8VjAq38QKSs0EbsXepyt68Op4VCNn-SfN8Lon1n9gTTIcGxZ2QQUUMcH00nwW0fhuybBIt1uMnk9NT9MJ-QhyjFZK2CUlSiNYk0mSA5Adb2JWHGJeeY1R0UTVucban0G0OZ-14g3g4PFxBuhY1t3WY-5jvSCXsdB2TyEMjXGF3Qrgx1RzVURsPqNcGiLNm509j-ZWWIZajUMLVti5bQh6y2Wipk38ZZcYBPlwEP1AMNEJdeli6aFeaP5Nv_9lAF4KFINzsY6vteBfe5xWyPOZx98XWQpWKEkTPr1-LVqPTIS6zLZmjPVMcW7oRYuRljQFsiy48bFyqeI49Zwrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بمباران شدید جنوب لبنان توسط اشغالگران
🔹
چندین شهرک و منطقه مرزی در جنوب لبنان روز یکشنبه شاهد مجموعه‌ای از بمباران‌های توپخانه‌ای و هوایی رژیم صهیونیستی بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/685563" target="_blank">📅 16:28 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685562">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8L2md2br1gJcxiwIGDQKIfqdWWru_JwT-gbGkkUk6vNMEN92du-skFWv-FH8ttay4YwMeOM1A9fipkSGZIqEFtcZchd7H9tEwjVtluuG3z3CEnYfXQRQOO6NZPfJ3mjodGaNt2BaNEyR--EOJRwe3LFCs6byaSDAe-b6qoxYK6QDxwJqdxMMwKZLP4M2vgtrewpRcDvrhTqNPBRlp6mQxmnKlGacKdRujz7dHRs3iXzgVQVQ0BEalXGNH8I0V15NN211VgxZyN_vnKDtYFlk8jyHlsK46OVEyx5svCIjEL_1joGZRZhxsI0aE8eUO8mKSu0MzdVRcesi51gJUg-UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سازمان زمین‌شناسی آمریکا (USGS) امروز رسماً نام «دریاچه انتاریو» را در تمامی اسناد الکترونیکی این سازمان به «دریاچه آمریکا» تغییر داد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/685562" target="_blank">📅 16:17 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685561">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16d7a73ce7.mp4?token=lnATkOao2Sz4piWR61Nlx1fKN34AanZu6TPnzER67ZzIa4aGsHPZcjGy-55vQ5r9cyGI7HBjnIliQzrLT9Jgt7FeWk_a0NGFNXAO20sS2AKrJJ1pIzhEozJdEsiP4KyesaK6LqdxTTqW5ViiqU9US3O0p0jpcQX4er1_WBzhOiHfm2Nw-FDGfaL9hfsKXMyKZIm9cN73mfz34XN18p0kYu9lrFQMd0upqIko6RIc_Rag9fxxpaZQr81Lp0nEOy6OmpnT30Bkdy6cFyRjLfisTGRAxerINt4c8yRp__MvVHYaEsTZk52zRE1H2u0X1oeXmbrJFJIOBgoHDCZ06Teo9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16d7a73ce7.mp4?token=lnATkOao2Sz4piWR61Nlx1fKN34AanZu6TPnzER67ZzIa4aGsHPZcjGy-55vQ5r9cyGI7HBjnIliQzrLT9Jgt7FeWk_a0NGFNXAO20sS2AKrJJ1pIzhEozJdEsiP4KyesaK6LqdxTTqW5ViiqU9US3O0p0jpcQX4er1_WBzhOiHfm2Nw-FDGfaL9hfsKXMyKZIm9cN73mfz34XN18p0kYu9lrFQMd0upqIko6RIc_Rag9fxxpaZQr81Lp0nEOy6OmpnT30Bkdy6cFyRjLfisTGRAxerINt4c8yRp__MvVHYaEsTZk52zRE1H2u0X1oeXmbrJFJIOBgoHDCZ06Teo9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سقوط یک هواپیما در نزدیکی نیروگاه هسته‌ای مجارستان
🔹
یک هواپیمای سبک که توسط خلبانی ناشناس به سرقت رفته بود، در مسیر پرواز به سوی نیروگاه هسته‌ای «پاکس» مجارستان دچار سانحه شد و در مزارع اطراف سقوط کرد.
🔹
تحقیقات گسترده‌ای برای شناسایی هویت سارق و انگیزه اصلی این اقدام خطرناک آغاز کرده‌ شده
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/685561" target="_blank">📅 16:11 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685558">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f2c792a4.mp4?token=cv1BeLK-Rb7sEeGoq_kTms2Yk-g3IPVFaiiY1f9nIajgKtBDvS-BhCq7wAAHkJA7UeEJ77EzUeni25J0pELfG9-sqFClRQcmIokOI2bczRtkFHw_iLIXEmUTvcSvOzg8vj-V2JIfDfDVrRY7Btqtk2Fn1tasieoeJ4ybn6skeHHdUojfQq1x3ozNPxZocjvB_9foqDZMMR3GmZ5vy5gZArpgpWRxLOetVl6pDvg8jhOgg9IZXaZm-Y1LAyFG3ifOzWYkHP62r9pa9uS86KyFSSKyudZIWLfyh3_-fEnIqoN01Ztv_lnbzflOnIYgBaAVsZr50Iy5tSarBRVTcplOpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f2c792a4.mp4?token=cv1BeLK-Rb7sEeGoq_kTms2Yk-g3IPVFaiiY1f9nIajgKtBDvS-BhCq7wAAHkJA7UeEJ77EzUeni25J0pELfG9-sqFClRQcmIokOI2bczRtkFHw_iLIXEmUTvcSvOzg8vj-V2JIfDfDVrRY7Btqtk2Fn1tasieoeJ4ybn6skeHHdUojfQq1x3ozNPxZocjvB_9foqDZMMR3GmZ5vy5gZArpgpWRxLOetVl6pDvg8jhOgg9IZXaZm-Y1LAyFG3ifOzWYkHP62r9pa9uS86KyFSSKyudZIWLfyh3_-fEnIqoN01Ztv_lnbzflOnIYgBaAVsZr50Iy5tSarBRVTcplOpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واژگونی کشتی حامل ۲۶۷ نفر در سواحل قبرس
🔹
یک کشتی مسافربری حامل حدود ۲۶۷ نفر در سواحل گیرنه در بخش ترک‌نشین قبرس واژگون شد و عملیات جست‌وجو و نجات برای یافتن سرنشینان همچنان ادامه دارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/685558" target="_blank">📅 16:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685557">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
سی‌بی‌اس: در آمریکا علیه ترامپ سند رو شد/ او از جنگ با ایران کاسبی کرد!
سی‌بی اس:
🔹
طبق اسناد افشای مالی، تا سه ماهه دوم سال ۲٠۲۶، حساب‌های سرمایه‌گذاری ترامپ در حالی که او بر جنگ آمریکا با ایران نظارت دارد، به خرید و فروش سهام در شرکت‌های نفت و گاز طبیعی ادامه داده‌اند.
🔹
طبق جدیدترین داده‌های موجود از دفتر اخلاق دولتی، ترامپ سهام نفت و گاز به ارزش صدها هزار دلار خرید و فروش کرده است.
🔹
ترامپ سبد سرمایه‌گذاری گسترده‌ای با دارایی‌هایی در هر ۱۱ بخش دارد و تحقیقات سی‌بی‌اس نیوز نشان داد که در سه ماه اول سال، حساب‌های او حدود ۳۶٠٠ معامله سهام یا اوراق بهادار انجام داده‌اند که ارزش کل آن بین ۲۱۲ میلیون دلار تا ۶۹۵ میلیون دلار بوده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/685557" target="_blank">📅 16:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685556">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/751875e9d9.mp4?token=H9FNXICA7T0azqsA_A047Nm-AkRSOiedYBkKMC3ahR0DMKHrT-zjGc2uFzgQcIlXuyVxHnPJmwPET6_lSO7A5VwEqsF2LN7-WlFBWq5ZXDWBfMf7BiVf0ps_RF7MODgJ2t6jBLvK1ahP2m-YR7Lyc5ZWEwqX2yp1rMEiVKDfgai027dXQtTokoa0mjcrVm7KaP-ThzEan43ztsycfEKx8uDYLbBrwGH6sZvRaDKVgjGR7wAl11mW-j6Xp74CXEs805Kf5Z5rHw-vfLMpGjlxJl8obwOfuGnoIe5c9cAxU6ECVtbnu5BXIqwOh2sy1zupcaEChgbg3UoLcT0Vpl1VyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/751875e9d9.mp4?token=H9FNXICA7T0azqsA_A047Nm-AkRSOiedYBkKMC3ahR0DMKHrT-zjGc2uFzgQcIlXuyVxHnPJmwPET6_lSO7A5VwEqsF2LN7-WlFBWq5ZXDWBfMf7BiVf0ps_RF7MODgJ2t6jBLvK1ahP2m-YR7Lyc5ZWEwqX2yp1rMEiVKDfgai027dXQtTokoa0mjcrVm7KaP-ThzEan43ztsycfEKx8uDYLbBrwGH6sZvRaDKVgjGR7wAl11mW-j6Xp74CXEs805Kf5Z5rHw-vfLMpGjlxJl8obwOfuGnoIe5c9cAxU6ECVtbnu5BXIqwOh2sy1zupcaEChgbg3UoLcT0Vpl1VyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایران، سرزمینِ ماست؛ و ما، مردمِ این آب و خاکیم؛ ریشه‌دوانده در خاکش، با قلبی که برای نامش می‌تپد.
🇮🇷
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/685556" target="_blank">📅 15:56 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685555">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ID0ZTkBbys0rZaPhGYXo8BGy9NcCSLfHosjdK3Vq9QzYzfyLLWXk7cUgK2zqWRZbZ-k2mClRZNZpBTaerjdHZBCgL8hf4Tt_yMnYGO2lM5dqRVsXbRWKfAAjfVmx5iu2ond-sujJ6Qzi4GDrLU3ajzl2Q9QopthBuBGApvPnykLKVFVE-GzfEXwELfssWrG77m32ZBFLHFXNEZxIqmkznzjFs_PYioFxEdWuEDi5h1yrJGEJOF48TRkMeZEuapJGPYh_tILds5kwfoGXCKhIDxQPgECW93KkfI5q5RfBvYhEHlAk5cDJDcj1UiX-X8xfvjcRp72sCdJnvhrAR5-1sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دستبرد ترامپ به ثروت ملی ونزوئلا؛ غارت ۶۵ میلیارد بشکه نفت
🔹
دونالد ترامپ، رئیس دولت تروریستی آمریکا، در جدیدترین اقدام خود برای تاراج منابع کشورهای مستقل، مدعی دستیابی به توافقی با ونزوئلا شده است که از آن به عنوان «عظیم‌ترین معامله تاریخ جهان» یاد می‌کند.…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/685555" target="_blank">📅 15:36 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685554">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
ممانعت نیروهای مسلح از عبور غیرمجاز ۳۰ شناور متخلف از تنگه هرمز
🔹
از تاریخ ۳۱ مردادماه تاکنون ۳۰ فروند شناور متخلف قصد عبور غیرمجاز از تنگه هرمز را داشته‌اند که توسط نیروهای مسلح ایران از تردد آنها ممانعت شده است.
🔹
همچنین پیش از آغاز جنگ رمضان در دی‌ماه ۱۴۰۴ بالغ بر یک هزار و ۵۰۰ فروند تانکر نفتکش و یک هزار و ۷۰۰ فروند کشتی تجاری از این مسیر عبور کرده‌اند که این آمار نشان‌دهنده توقف جدی در تردد و تجارت در شرایط فعلی است.
🔹
ادعاهای مطرح‌شده درباره مین‌روبی نیز با هیچ داده‌ای قابل تأیید نیست و طرف آمریکایی تاکنون هیچ مستندی در این زمینه ارائه نکرده است./ مهر
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/685554" target="_blank">📅 15:29 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685553">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
دستان پنهان در جیب مغازه‌داران؛ افزایش عجیب سرقت مواد غذایی
🔹
برای فروشنده‌ها، نگرانی فقط فروش و تأمین کالا نیست؛ امنیت مغازه هم به یکی از دغدغه‌های جدی تبدیل شده است.
🔹
سرقت، خسارتی است که گاهی جبران آن برای یک کسب‌وکار کوچک آسان نیست. نگرانی هر روزه صاحبان مغازه‌ها می‌گویند حالا علاوه بر گرانی و کاهش قدرت خرید، باید نگران امنیت فروشگاه خود هم باشند.
🔹
دغدغه‌ای که آرامش کسبه را تحت تأثیر قرار داده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/685553" target="_blank">📅 15:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685551">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
تلسکوپ فضایی رومن ناسا با موشک فالکون هوی اسپیس‌ایکس به فضا پرتاب شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/685551" target="_blank">📅 15:11 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685550">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDaaIKZbhCxQpimpDQ74FCOD7kDObXAuCpaiHiK-NobNplCuyGBVydKCZ3A9W4zfjnLr1erSHmT_TsdOitwexfb-HmoOjTSeSL_NByqXZ9F9c1EQqIqrr-gBt8pjgAIo-s5KHdqGwEnfdgnov9mH7V0UMhOE-tX8mvrYuEWCy8iwn-4Kt49zMsNCKVoXLSSrPuZF0qwoHx7KwBFm1CAi2_Hy6HiyJZ6I5GytmiJn3y0Pocy-5OChyAAknoEN-VLzsxaVCB2HSiK5fuildUBB9oiwB1IXjiJOlHtW_L4FcM0EruTIvyRXH7vpiVdAL_qj8fP6FNmkPeP8JJvr2zSOxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهادت سرباز عشایری در درگیری مرزی در پاوه
🔹
مهرداد طاهری آرپناهی، سرباز وظیفه اهل شهرستان کوهرنگ چهارمحال‌وبختیاری، در جریان درگیری با اشرار در منطقه مرزی پاوه، بر اثر اصابت گلوله به شهادت رسید.
#اخبار_کرمانشاه
در فضای مجازی
👇
@akhbare_kermanshah</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/685550" target="_blank">📅 15:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685549">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
یونیوز: ایران در صورت گسترش جنگ، شمال اسرائیل را هدف قرار می‌دهد
یونیوز:
🔹
تهران هشدار داده در صورت گسترش عملیات اسرائیل در لبنان، فرودگاه‌ها و پادگان‌های شمال اسرائیل هدف حملات موشکی قرار خواهند گرفت و حمایت ایران از مقاومت ادامه خواهد داشت./ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/685549" target="_blank">📅 15:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685548">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9acccbce2.mp4?token=na5D4k3I-oL-89-5lfevlx0AgyLhQ-2uhEUQkUMKNAFWL_UYIVFIlqcYkhkn9yJ1jFes7puAVyYetaJi7YB3w3o6q0mfDgjLYdt7B8BpXp2ZCLCx_ANN-cMrvXWD3kNF8d-Y2Wmy4si-suXHleAS_JH8-axOAShdWu98cOfwiDV_PSNpE7_CfTC7Wti-TNy71CtSIVBTVaD8tvPkVRFnCzFEWS4Eg5aTIL9mPLicq8Ledv_CI86N-rw2XioiMW93InbHRk0lda7-4NVhBQkEPABrc34-IS9sKabJPvR-oQt-ooxMO40KtTCJHot_l3p1MEoVXXGdr0hVWjQAGmp_pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9acccbce2.mp4?token=na5D4k3I-oL-89-5lfevlx0AgyLhQ-2uhEUQkUMKNAFWL_UYIVFIlqcYkhkn9yJ1jFes7puAVyYetaJi7YB3w3o6q0mfDgjLYdt7B8BpXp2ZCLCx_ANN-cMrvXWD3kNF8d-Y2Wmy4si-suXHleAS_JH8-axOAShdWu98cOfwiDV_PSNpE7_CfTC7Wti-TNy71CtSIVBTVaD8tvPkVRFnCzFEWS4Eg5aTIL9mPLicq8Ledv_CI86N-rw2XioiMW93InbHRk0lda7-4NVhBQkEPABrc34-IS9sKabJPvR-oQt-ooxMO40KtTCJHot_l3p1MEoVXXGdr0hVWjQAGmp_pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کردستان و هورامانات؛ جلوه‌ای بی‌نظیر از طبیعت و تمدن ایران‌زمین
🌱
😍
#اخبار_کردستان
در فضای مجازی
👇
@Akhbarkordestan</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/685548" target="_blank">📅 14:55 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685547">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_-THgpEoWs1cyQ_vcwOOkIrxgdBePgmO32FJ1DiUzYrCFw0z6HMt1nMgr2tA1LpAUFYzuAl9BaD_uuMYPBHApl0lxf7tVBdDe3GICe9yiC6ABgCHybnmkYp4XbYSlTZQA7fa3x18sVbdyENTuSG-U-EtuT1v_fPNdrQ0fCo3PgMe9tHGEhGwoLPpPXsDTiQ8BisCFe3hzZnlGHoeG_ks9DaWdAPtfHBzA0nNxvxNk9VnIhT92Lavpiu3WTkpLs_45LtAz7kLyeRoEcr6SgQWf2ZicRSu3PCmZOmsNsGw6tZRRDsFu-X_F34Lj-XWndnnkED2Od7wXgN6OG-9nTGCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طلای ناب ساغر مرادی در مسابقات قهرمانی آزاد زنان جهان
🔹
ساغر مرادی نماینده وزن ۶۷- کیلوگرم کشورمان با یک عملکرد تاریخی پس از پیروزی مقابل رقبایی از روسیه، چین، آمریکا، کرواسی و یونان بدون از دست دادن حتی یک راند در طول مسابقات صاحب نشان زرین طلا شد‌.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/685547" target="_blank">📅 14:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685546">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
گرانی کالاها دو برابر خدمات؛ شکاف ۷۲ واحدی اقتصاد را تکان داد
🔹
داده‌های بانک مرکزی از تشدید شکاف تورمی میان کالا و خدمات حکایت دارد.
🔹
بر اساس این آمار، تورم نقطه‌به‌نقطه کالا به ۱۲۱.۵ درصد رسیده، در حالی که تورم نقطه‌به‌نقطه خدمات ۴۹.۳ درصد ثبت شده است؛ یعنی فاصله‌ای ۷۲.۲ واحد درصدی میان دو بخش.
🔹
این واگرایی می‌تواند نشانه‌ای از فشار همزمان تورم سمت عرضه و رکود تقاضا باشد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/685546" target="_blank">📅 14:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685545">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjwzQd-Gguj2eMy-916T9Vkri0GI0L0lPUUAO8Z5t--7wcgkKmbxO3aVMWXVBF_LRQt2tJ5id83vN9Daog4j6a90H3PfGgUCi9_OnF6cRYHyKAgMqT9_vK2nPlJwEVT7u5Ag9k0HHzJq6yEuVjOtaELA3yoBbUHbGacWupYRaX5ZFqDeTjNa7v2vLAd2i_zxQKR3V_lcSeCoHBCLiJgV_pjvXeCQQpJLJ2oEt_3PIrd7CvHUajWYn5ZJeFV_ufo8wXadDCTZ7HTwbnn_xD4F5vRsJl-TvRozbsoZmiEBx39nahnpyUJHXdoiSTk3xVf1kUiPgz6w-2IQNboa43hbpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ از کنترل آمریکا بر ۶۵ میلیارد بشکه نفت ونزوئلا خبر داد
🔸
دونالد ترامپ روز جمعه از توافق جدید نفتی ایالات متحده با «دلسی رودریگز»، رئیس‌جمهور موقت ونزوئلا خبر داد.
🔸
او اعلام کرد که بر اساس این توافق، آمریکا کنترل اکثریت ۶۵ میلیارد بشکه از ذخایر نفتی اثبات‌شده این کشور را در اختیار خواهد داشت.
@amarfact</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/685545" target="_blank">📅 14:33 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685544">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad1ca53df6.mp4?token=H1Cvfsc7dGgOdpqYJDf-rDnBDp7RHeny2I0V3_r4e3pL1B-fg3WCvBuLenJ73Rvb63M2256TALw8_3tOC7WFh_e4y-02HQePf7tvtHq9o58q_tCYFw1MX5JYQRCY1e6rANsy7xoEnnTgFoNCnKhTBXQOH0_-KZnf9Q8q1eTVjzOeqvNuFXgKX_OOvNOy3fqa9bLbPoyQjomy8cJ1SzWIX2tjbg1Lm8Bty51s_IxmnNK6T6l2_pNyeLvyPyL6-8rdmvx_yY6v3zYdeIUiwvxmLL984kseNUqy76ioCVB1ByE6ecaaS71Jzu-GmmaD4AL3mWen5CGCqk4NoxW8WBHjyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad1ca53df6.mp4?token=H1Cvfsc7dGgOdpqYJDf-rDnBDp7RHeny2I0V3_r4e3pL1B-fg3WCvBuLenJ73Rvb63M2256TALw8_3tOC7WFh_e4y-02HQePf7tvtHq9o58q_tCYFw1MX5JYQRCY1e6rANsy7xoEnnTgFoNCnKhTBXQOH0_-KZnf9Q8q1eTVjzOeqvNuFXgKX_OOvNOy3fqa9bLbPoyQjomy8cJ1SzWIX2tjbg1Lm8Bty51s_IxmnNK6T6l2_pNyeLvyPyL6-8rdmvx_yY6v3zYdeIUiwvxmLL984kseNUqy76ioCVB1ByE6ecaaS71Jzu-GmmaD4AL3mWen5CGCqk4NoxW8WBHjyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آزمایش جالب یک معلم؛ گاو نر تا زمانی که احساس خطر نکند، به جمعیت حمله نمی‌کند
🐂
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/685544" target="_blank">📅 14:28 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685543">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
نشست «پیمان مکه» فردا در استانبول برگزار می‌شود
🔹
نخستین نشست کمیته سیاسی و دفاعی اعضای «پیمان مکه» با محوریت امنیت بین‌الملل، تقویت توان دفاعی و همکاری عملیاتی نظامی سه کشور برگزار خواهد شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/685543" target="_blank">📅 14:23 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685542">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
هشدار فرماندهان ارشد آمریکا درباره ادامه جنگ با ایران
🔹
طبق گزارش واشنگتن‌پست، فرماندهان ارشد نظامی آمریکا ادامه عملیات گسترده علیه ایران را غیرقابل‌تحمل دانسته و هشدار داده‌اند که جنگ شش‌ماهه در خاورمیانه، توان و آمادگی ارتش آمریکا برای مقابله با تهدیدهای دیگر را کاهش داده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/685542" target="_blank">📅 14:16 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685539">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iMFtFWA6Mz8CApAkfHjyvh1FfJxmiwRxzmq1BjCN62RljseYUFSVHLljm8WQQDmIe0kOVP4-_mKoxipQXj6FVa2PomJtb66_9OEgu4dPu-GrRuQfzOGYBjBl9p0vmBwLyiwyADcxkuCrei2XQr5Sm9WWJjaMmU83FBwjnM8x5ns-86IUKWEqfXIpH_RdGGeNTP-fPvWziQj1XYGH8BV1SZ3OcYqToWyLb8CbaVA7psJFCPn39L1PAF0sB2ymPRt5R-z-dqNEYrSyHBceB70KG_FPn0l4PofPtfJUolWN6tk0aqD9zEYY72707BrbBIXDj84rWHfc1obo8KcQ8ZYrMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZlXdsBQjaA5p0wYIKegGqOc5jyMtRW48c4M-cGoi43Pncf4JiHsn-yfMaGwtiv0JedOdwk0zvru6KNwbn6ko7j8AJJy9IO3F_LqOQrBa_4mtomoRv0xCV8ml-eAFo6Yx6x4J30PA7D9_dL6YvVdv9iLaFxT9LFUirXMR4pG12hGVTPiVIt-fpS0S2cBZ1T8yEBmmfkuU-BqZcOkYOUdoC23qDvG2Bio-nACuHdM1UDwe1FlvQscL_wHWP54Qb0K7AOzEzBSR1KKMwpZO_kPcP-lt-a3Y4UA_DonECea-1bo-doMWFD5fgKYLLQr-ep_IkTWw9Ow1jXOmmir6IooaDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QSvp0XAKPpn516U5Q_BxoiRv0Z_docamnroI0mNQLkYB0aHj4Q5tIIXxlBvkLybxXXDSy4DHlII7thGH6rP0N2-ri8nyrpQjs53DA8XDK1mjAKCNniJ4HnJlmGuP1cLrdy5BQSX_4msXmutJ36lcLyNypzaXXWnrY9wMsJUNYjh7uHh0_VDyGyyeGmNyBh7wLRkiAZbIDSbI8uis3bxeqFHyDAvhNQQUrotJ1xirrAGocJSOGTaLVWaWtOR78hcImTsou3xRvDneI_V8v84bCFMjE7EeT0zap3JRpcBsGYQy2iHR7P53xWnIvxSK8Mv0zLWf5W8jMufSFZPKIMRPjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
انتشار دستخطی از فیش‌برداری شخصی شهید لاریجانی پیرامون مقام شهادت و شهید
🔹
حدیث اول:
رَسُولِ اَللَّهِ (صَلَّى‌اَللَّهُ‌عَلَيْهِ‌وَ آلِهِ): «مَا مِنْ قَطْرَةٍ أَحَبَّ إِلَى اَللَّهِ مِنْ قَطْرَةِ دَمٍ فِي سَبِيلِ اَللَّهِ.»
پیامبر (صلی‌الله‌علیه‌و‌آله‌وسلم): «هیچ قطره‌ای در مقیاس حقیقت و در نزد خداوند، از قطره خونی که در راه خدا و ریخته شود، بهتر نیست.»
🔹
حدیث دوم:
رَسُولِ اَللَّهِ (صَلَّى‌اَللَّهُ‌عَلَيْهِ‌وَ آلِهِ): «فَوْقَ كُلِّ ذِي بِرٍّ بَرٌّ حَتَّى يُقْتَلَ اَلرَّجُلُ فِي سَبِيلِ اَللَّهِ فَإِذَا قُتِلَ فِي سَبِيلِ اَللَّهِ فَلَيْسَ فَوْقَهُ بِرٌّ.»
رسول خدا (صلی‌الله‌علیه‌وآله‌وسلم): «بالا دست بر نیکوکاری، نیکوکاری دیگر است، تا آنگه که در راه خدا شهید شود، همینکه در راه خدا شهید شد، دیگر بالا دست ندارد.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/685539" target="_blank">📅 14:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685538">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
۳۰ تا ۴۰ درصد بازار کسب‌وکارهای مجازی از دسترس خارج شد
پشوتن پورپزشک، عضو هیئت مدیره اتحادیه کسب‌وکارهای مجازی در
#گفتگو
با خبرفوری:
🔹
برآوردها نشان می‌دهد بازار کسب‌وکارهای مجازی در سال ۱۴۰۴ پیش از قطعی‌های اینترنت حدود ۱۲۰ همت بوده است.
🔹
پس از قطعی‌های چندماهه اینترنت حدود ۳۰ تا ۴۰ درصد از این بازار از دسترس خارج شد و بخش قابل توجهی از کسب‌وکارها آسیب دیدند.
🔹
اگر دسترسی پایدار به پلتفرم‌ها ایجاد شود امکان ترمیم تدریجی این بازار وجود دارد اما رشد واقعی نیازمند ثبات در زیرساخت، اقتصاد و شرایط خرید مردم است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/685538" target="_blank">📅 14:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685537">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31d31c32e4.mp4?token=XWlQr4K0KcBTrYQPDpuXUCBCixIz2sDmCmFvQHBdfGJ2bJGugL8Oadpf9BcUQUTRKJLP3tmE1Rajku3hxOdEihsdRtIcr0kQuHjmZs7_UVs1EhkkBZyzLmcV7UxxaN62TtyJOlNT0fPuQFzIyp-6rl3drxOLnTY7tlF5N2CzlNU6SGWoXEH_s4L44beEaNacO73mkngetIsYCrkoxQhDwl0kR3MfaH--C-ng_x5OtvmUgA5gwOMvCXWOVTYeB7Hu1IMoPofVFN4nJK4Zedq6UG48EtNJc5QhC3qQoRWadYRYRGurZxLS9XEvjM8ulwKG3RWjIrboUgcju_qLk3LRTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31d31c32e4.mp4?token=XWlQr4K0KcBTrYQPDpuXUCBCixIz2sDmCmFvQHBdfGJ2bJGugL8Oadpf9BcUQUTRKJLP3tmE1Rajku3hxOdEihsdRtIcr0kQuHjmZs7_UVs1EhkkBZyzLmcV7UxxaN62TtyJOlNT0fPuQFzIyp-6rl3drxOLnTY7tlF5N2CzlNU6SGWoXEH_s4L44beEaNacO73mkngetIsYCrkoxQhDwl0kR3MfaH--C-ng_x5OtvmUgA5gwOMvCXWOVTYeB7Hu1IMoPofVFN4nJK4Zedq6UG48EtNJc5QhC3qQoRWadYRYRGurZxLS9XEvjM8ulwKG3RWjIrboUgcju_qLk3LRTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دارکوب خالدار بزرگ؛ استفاده هوشمندانه از درخت برای شکستن فندق
🐦
🌰
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/685537" target="_blank">📅 13:55 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685536">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c275b5876d.mp4?token=lZOuCXSKiCsJs7vmnQ3ClGcwijJ8DI8w-1ewIlEl0gfHO3-Igj4U5N00_giMlLzn-QzqYprUjU2K1mn5_f0hKPX4Hd-GUtvAfud8rvZlJ3mkgcinsLlyHx2yTLCUWEVljVJclaEVkHS9nhQ4zViy2gxqjFHl4jVkWYMFixUuOs1ZH1x8ZS-0Qi1WzfT3D2ySJClj6JCeeS08He38PLa0pncYE-4CjEnynlndiUyi3UBRIPUiV01UKYpZCh3pd3GZXkGnKBnE58gH_0-1QAffL5qmQe0k9eMijVcJnN-XlDOJla4KCITYNBdfeiDxDi3JtMjwgOA258R6frPlWrwLDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c275b5876d.mp4?token=lZOuCXSKiCsJs7vmnQ3ClGcwijJ8DI8w-1ewIlEl0gfHO3-Igj4U5N00_giMlLzn-QzqYprUjU2K1mn5_f0hKPX4Hd-GUtvAfud8rvZlJ3mkgcinsLlyHx2yTLCUWEVljVJclaEVkHS9nhQ4zViy2gxqjFHl4jVkWYMFixUuOs1ZH1x8ZS-0Qi1WzfT3D2ySJClj6JCeeS08He38PLa0pncYE-4CjEnynlndiUyi3UBRIPUiV01UKYpZCh3pd3GZXkGnKBnE58gH_0-1QAffL5qmQe0k9eMijVcJnN-XlDOJla4KCITYNBdfeiDxDi3JtMjwgOA258R6frPlWrwLDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فراخوان خبرفوری؛ چرخ زندگی
🔹
از خانه تا بازار؛ نگاهی به داستان‌های موفق کسب‌وکارهای کوچک که با تلاش و خلاقیت رشد کردند.
🔸
داستان موفقیت و تلاش شما در کسب‌وکارتان، انگیزه‌بخش مسیر دیگران است، در یک پیام صوتی ۳۰ ثانیه‌ای از چگونگی شروع کارتان بگویید و همراه با عکسی از محصول یا خدماتتان ارسال کنید. روایت‌های  شما در خبرفوری بازتاب داده می‌شود.
👇
#چرخ_زندگی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/685536" target="_blank">📅 13:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685535">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
فایننشال تایمز: دو بانک تحریمی ایران (صادرات-ملی) همچنان در امارات فعال هستند
.
🔹
یمن: سازمان‌های امدادی تحت فشار عربستان از ورود داروهای مورد نیاز مردم جلوگیری می‌کنند.
🔹
رئیس‌جمهور لبنان بر ادامه پیگیری پرونده ناپدیدشدن امام موسی صدر و کشف حقیقت سرنوشت او تأکید کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/685535" target="_blank">📅 13:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685534">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4592fb4ffd.mp4?token=ToIcHztstL__rOSgzEkif0cVANgQ2xaDZB0rz8Jxhs6aojdpg0V1Xp-8EiDRTe0LQzvF5xciaxY_9fZcQAl3FYSOltiR5RWKOFJgKxPNf9Eh49oOHP8TuUE0dXKfO0s34tm_PEWNDcW3mWwQk6Uw-V_5lM3vkk_8MRMFiMJXPK6vU5vY4qAElJ_kYzpo3IqAqBHeOtmVrJ4yg_A_zdld1NZrtNDNSoh1JlATdm22v9n7lxt-w-lEB_gFe2W1_8Bz7eBA-mxgdhqvtkl_t4ygKqyE_U9bUu13LtuStPDOyvAI5hzugl6Y9uRLT5b9rULMXY4xYqjMczrzHRVjSm1seA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4592fb4ffd.mp4?token=ToIcHztstL__rOSgzEkif0cVANgQ2xaDZB0rz8Jxhs6aojdpg0V1Xp-8EiDRTe0LQzvF5xciaxY_9fZcQAl3FYSOltiR5RWKOFJgKxPNf9Eh49oOHP8TuUE0dXKfO0s34tm_PEWNDcW3mWwQk6Uw-V_5lM3vkk_8MRMFiMJXPK6vU5vY4qAElJ_kYzpo3IqAqBHeOtmVrJ4yg_A_zdld1NZrtNDNSoh1JlATdm22v9n7lxt-w-lEB_gFe2W1_8Bz7eBA-mxgdhqvtkl_t4ygKqyE_U9bUu13LtuStPDOyvAI5hzugl6Y9uRLT5b9rULMXY4xYqjMczrzHRVjSm1seA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
السلام عليك يا سيدي يا رسول الله
🕊️
✨
💚
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/685534" target="_blank">📅 13:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685533">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
الجزیره: آمریکا فعلاً از تحریم چین بابت خرید نفت ایران اجتناب می‌کند
🔹
به گفته یک مقام سابق امنیت ملی آمریکا، تحریم چین همچنان به‌عنوان گزینه ذخیره ترامپ باقی مانده و واشنگتن امیدوار است مجبور به استفاده از آن نشود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/685533" target="_blank">📅 13:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685532">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
ایندیپندنت: جنگ ترامپ در ایران به یک شکست تماشایی انجامیده است
ایندیپندنت:
🔹
جنگ ترامپ در ایران به یک شکست تماشایی انجامیده است. تنها برنده مسلم، صنایع دفاعی است. به لاکهید مارتین ده‌ها میلیارد دلار برای تسریع تولید موشک پاتریوت اعطا شده است.
🔹
ترامپ در جنگ ایران پیروز نشده است، او نقاط ضعف آمریکا را به قیمت متحدانش در معرض روسیه و چین قرار داده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/685532" target="_blank">📅 13:36 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685531">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4eb7ff1ee0.mp4?token=Oq5rS34lUE2Z2rQwRIu4C6kkGd0g_DvrVfbYEEr9DZAIPOvZU8RtO_XpKS7bGzDIICmbYRQgMhLgNw4ipkmzTeaoJBHdpxuo-8TmCX2lk5y4wiuPdlbZ4h9b3Qd3Pb9ZVr90Bj99yYvcAhyvUZ57FciJD943nHerENdDyuVQ9-uw0oKRdZcNxZTIc_0kqf_sJBvU4ePDBZvwaAZlurq0TE6ENblhn7dWqwLOmIs5PcjYDxzFOvEtt1hgcah4467-icaUf7DAfX74VbW3G8E7c5TiGOGn8AUlcJJe8QTfdBA59H52GuAu12y0SuOjEoOtFg75ewod22a4JzrlEqXHBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4eb7ff1ee0.mp4?token=Oq5rS34lUE2Z2rQwRIu4C6kkGd0g_DvrVfbYEEr9DZAIPOvZU8RtO_XpKS7bGzDIICmbYRQgMhLgNw4ipkmzTeaoJBHdpxuo-8TmCX2lk5y4wiuPdlbZ4h9b3Qd3Pb9ZVr90Bj99yYvcAhyvUZ57FciJD943nHerENdDyuVQ9-uw0oKRdZcNxZTIc_0kqf_sJBvU4ePDBZvwaAZlurq0TE6ENblhn7dWqwLOmIs5PcjYDxzFOvEtt1hgcah4467-icaUf7DAfX74VbW3G8E7c5TiGOGn8AUlcJJe8QTfdBA59H52GuAu12y0SuOjEoOtFg75ewod22a4JzrlEqXHBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عینک تاشو انگلیسی؛ ساخته‌ شده ۱۰۶ سال پیش
👓
🇬🇧
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/685531" target="_blank">📅 13:33 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685530">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K854ZngugkrU3GRFGQtUFVIV0ic82hSAImRpRcYoWqfca4vVo1Cg9K8YDUDREecYtODNDXUSvyTWQOx50upLHgRuQTUM3KyRPinkV6r59sWl-5RxTYIaKvuCF19I--85dBYBSI43JHNnUrMRf00isaoagjWbHHodT78PUz6ldCA-2D_cI2bS2hJxgzgiligyIBmZB0kuIuovYytv7hhASaioIEbY3dzs9Ud5WonYj4Pu9zQ9Rdu4F6niXmovmSsfWCiPfR-bdt3JTBm641Zy2o5WuO-JQbHmsRSriRLBxkkD990hn8UFB5m0fo_1sjOduqibXIpW--QqRX-ddWyCyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راز جواهرات ایرانی که دیگر در ایران نیستند/ از گوشواره‌‌ای که ستاره هالیوود به گوش انداخت تا گردنبند گمشده همسر محمدرضا شاه
گزارش خبرفوری را اینجا بخوانید و ببینید
👇
khabarfoori.com/fa/tiny/news-3241302</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/685530" target="_blank">📅 13:28 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685529">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
قیمت بنزین در اسراییل به بالاترین قیمت خود در ۱۵ سال اخیر رسید
🔹
هر لیتر بنزین ۸.۵ شیکل ۴۰۰ هزار تومان.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/685529" target="_blank">📅 13:24 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685528">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a4f4f2828.mp4?token=KpiuV4FiKNoRMTiGTGNld56R1wB76-YZHQ1RaqqCJZ32oX0DBbJM0XTQMBhg5X-M-pwO608yg0sT4BHKBHiEmaq8PE3BJKow799XrkRLtFoiy7NHzLphQI0Ei8Qw-Mw_QE6wemPnrqbEaxu0xCpSmMsIDk3KwDK2TCEcdVQ1-m99KuDdEOW559mGqVYI-YZn63waZWu0FYPkvpWwRcZMI2NIaB67MMB61FnJyiv8949OF2lHOAfJHNbtLdBPpwyHPt2G13PgV4ZhYFUW-3_Xw7TVOn71uUbnM8meq7LxwnEKzqkD-j_x1Wv4p79E_Mjg9dLwu26Hr3Vw96TSSeAvzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a4f4f2828.mp4?token=KpiuV4FiKNoRMTiGTGNld56R1wB76-YZHQ1RaqqCJZ32oX0DBbJM0XTQMBhg5X-M-pwO608yg0sT4BHKBHiEmaq8PE3BJKow799XrkRLtFoiy7NHzLphQI0Ei8Qw-Mw_QE6wemPnrqbEaxu0xCpSmMsIDk3KwDK2TCEcdVQ1-m99KuDdEOW559mGqVYI-YZn63waZWu0FYPkvpWwRcZMI2NIaB67MMB61FnJyiv8949OF2lHOAfJHNbtLdBPpwyHPt2G13PgV4ZhYFUW-3_Xw7TVOn71uUbnM8meq7LxwnEKzqkD-j_x1Wv4p79E_Mjg9dLwu26Hr3Vw96TSSeAvzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجسمه‌های رنگ‌آمیزی کودک؛ ایده‌ای ساده برای تبدیل خلاقیت به درآمد
🔹
این بار در #چرخ_زندگی دنبال یک ایده ساده و خلاقانه برای کسب درآمد در خانه رفتیم، ساخت مجسمه‌های خام مخصوص کودکان.
🔹
این مجسمه‌ها را می‌توان در طرح‌های مختلف تولید کرد تا کودکان با رنگ‌آمیزی…</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/685528" target="_blank">📅 13:16 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685527">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
۲ نوجوان اسرائیلی به اتهام جاسوسی برای ایران محاکمه شدند
🔹
دادستانی اسرائیل علیه دو نوجوان ۱۴ و ۱۶ ساله از حیفا به اتهام همکاری با یک عامل مرتبط با ایران کیفرخواست صادر کرد.
🔹
طبق ادعای یدیعوت آحارانوت، آن‌ها در ازای دریافت پول اقدام به تصویربرداری از اماکن، نوشتن شعارهای گرافیتی و جذب نوجوانان دیگر برای انجام مأموریت‌های مشابه کرده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/685527" target="_blank">📅 13:13 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685526">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GuSfL1s8iNLvEqg2zbEW6YwrmMS1WmwE9_lIEAWRiMz5E7s5B3WUjvtgu3836H6c_BMJxJnQbos-nd5NStARdITcp0hsCSVZ393bSqQznnP-JnjTDG-sAKzFaFi3MTORk0E87LVeAe4kjYz_13WUML5PDUPvXwx0X5vcHzidCFQzxkMukgj9qBMaLwKrERZ7D6AjWq0tNNG7kZvQc4ovRk-0UZtQTjy_PzzFmXPtpkYx-_ho3TUJJb3Faa3-bkz5ny9kjPlN0-20YsDpm6gXizsa2DHm3lkyTOdL1KxIpTIzLQ10QcqK8AC0Dnk2DWo9XU6OfdZc9AFY-Od_2v6z_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۹۲ درصد آب شیرین کشور به بخش کشاورزی اختصاص داده می‌شود
🔸
کشورهای افغانستان و پاکستان با اختصاص ۹۸ و ۹۴ درصد از آب شیرین خود به بخش کشاورزی، در صدر این آمار قرار دارند.
🔸
ایران نیز با اختصاص ۹۲ درصد از کل برداشت آب شیرین خود، در میان کشورهای با بیشترین مصرف آب در این بخش جای گرفته است.
🔸
از طرفی دیگر، کشوری مانند هلند توانسته با بارندگی مناسب و بهره‌گیری از کشاورزی مدرن گلخانه‌ای و سامانه‌های بازچرخانی، این سهم را به تنها ۵ درصد برساند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/685526" target="_blank">📅 13:12 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685525">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/416ab68c2f.mp4?token=F066t_yUdGNnNzKD8aWv-c_mWEeKDqi3Y1LjsifZP8d1up-T_zyUEw-Z6AFeoFL-M7rUOzzkhGs2ZwBBO0g3uD9Kni-EkWvEPJGgm8W2_aIePYZGdOblHLDw4R218EF0DAAskcd6EddsUjX0jGr4C_OKTyjX-Rq_Q3oJAn5Y6aDY6u1IsHP0F4qQZSYiMnDC4EgzpZfVVl0bJyue9thr1z8i3SM1gPGBtb_e_gSshUxoOC1kZ44XYaH01byHjOtH1EPWSKcAb38I37FgG7RXV3UNr24NDmzySd421W7Z_gp2uQLD7Zkd95VSmfEt7VtyrbmtvH2LEponccqVEgTIbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/416ab68c2f.mp4?token=F066t_yUdGNnNzKD8aWv-c_mWEeKDqi3Y1LjsifZP8d1up-T_zyUEw-Z6AFeoFL-M7rUOzzkhGs2ZwBBO0g3uD9Kni-EkWvEPJGgm8W2_aIePYZGdOblHLDw4R218EF0DAAskcd6EddsUjX0jGr4C_OKTyjX-Rq_Q3oJAn5Y6aDY6u1IsHP0F4qQZSYiMnDC4EgzpZfVVl0bJyue9thr1z8i3SM1gPGBtb_e_gSshUxoOC1kZ44XYaH01byHjOtH1EPWSKcAb38I37FgG7RXV3UNr24NDmzySd421W7Z_gp2uQLD7Zkd95VSmfEt7VtyrbmtvH2LEponccqVEgTIbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سازمان زمین‌شناسی آمریکا (USGS) امروز رسماً نام «دریاچه انتاریو» را در تمامی اسناد الکترونیکی این سازمان به «دریاچه آمریکا» تغییر داد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/685525" target="_blank">📅 13:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685524">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b86de90f3a.mp4?token=PQHR7eBUU_22AjV38tWMYfS4COfrfVQVWwIMtjrmEUtouuMORxfowcWQShs4p12C644W0ry8FUT2NrWle5UoknxPS9fhdVU05u_lBo9rgVlM20BC00UQBSjO300sXk2xN9cEvJoT0MrboKOcOl9NiIndWpka41e8lByTb1HfLdCa1H-7o7SWnU-_lUvvgUJMIePrqHKsxVPKuz8z-2BZp2JXR7ZOXM3z2m9Z2IzhZJDxekdnNA38K_uey_Of2yyHcp3MJ_E6zobDzS7z1vWKYfSBlgoptnz5hFIOtHt1sC8N58hxvSX8rsg8yIo4eMhh5gZSmBu8HPqUF28EEKoadQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b86de90f3a.mp4?token=PQHR7eBUU_22AjV38tWMYfS4COfrfVQVWwIMtjrmEUtouuMORxfowcWQShs4p12C644W0ry8FUT2NrWle5UoknxPS9fhdVU05u_lBo9rgVlM20BC00UQBSjO300sXk2xN9cEvJoT0MrboKOcOl9NiIndWpka41e8lByTb1HfLdCa1H-7o7SWnU-_lUvvgUJMIePrqHKsxVPKuz8z-2BZp2JXR7ZOXM3z2m9Z2IzhZJDxekdnNA38K_uey_Of2yyHcp3MJ_E6zobDzS7z1vWKYfSBlgoptnz5hFIOtHt1sC8N58hxvSX8rsg8yIo4eMhh5gZSmBu8HPqUF28EEKoadQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین پرواز HÜRJET؛ جت آموزشی مافوق‌صوت ترکیه
🇹🇷
✈️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/685524" target="_blank">📅 13:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685523">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlUtNsRZo-QJHMWIolQU5zg2qcl7F247IJ_SsjWrwpssp07agfIeK1nieKnPHafH5dLItDtp3ngeyIsDuN_hvSXf_IT4nL6WuO6Ruq-9JvAzb7wlFj6girk_M7XRo3-ThgeMaqtqgYBdOVHEydhYb0pBb48hcDeOYChwQeek55dq4DuG9417jvwnTwupXzxX7UQJqz4oZ1tw3KiOdcWbGMNkoWlxwJbGPCAnp2AgSvzFDSDeOlu8N_YsR6ZYNbi2nmqq0xuohK_cj7L1rhJZ7DJv_vtcT2jzD9k4ZNxayDN8QvLcTPKgmwDIS8fFkIppcDo1ZMV3jv6Mq4q9Qm50Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از یک محفل زنانه در ایران دوران قاجار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/685523" target="_blank">📅 12:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685522">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
تانکر ترکرز: میانگین روزانه صادرات نفت خام از طریق تنگه هرمز طی هفت روز گذشته ۳.۸ میلیون بشکه در روز بوده است
🔹
در دوره اجرای تفاهم‌نامه (MoU) که عملاً تنها ۲۵ روز دوام داشت، این رقم ۹.۸ میلیون بشکه در روز بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/685522" target="_blank">📅 12:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685521">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79a8ee04d3.mp4?token=WuJs3AzB9VPN20BBa6qnxR9_2QJdjsrw8PmW636pEIqXRQjd7uvQQQ3OOTAUrP8qO0Jd2PQLPn_vs9Woi5_RKEUEuN3slXXufOdkgL_hhefuwp-XQN_0KGlmg8vK1iQtUiZJN9a_b9AiNfb1CWBLyUlsisIHyMQt8zDqWJBiqnl7GVKD0blh4UAqfVG0vMmcq-aUai3smaQHLjklG320g8C2meQAYTGV2X2aR8qvtIYvkbA5ngfC0j-xzzv8C603sNmaFP4z-TRoEFhZ535r0oQ3cwAprANNGasnceYWEySg8PEKOQx3hcDTPpd5COMDQ48idLHWMlzNlTbhRl6k81jGUGLReyDP3HByirv1qx7LKhOroZTV97c1u0dnLqCvKsbQQl1iPY5kswwLs4puo0zAFi-Wd-GCLbwKHCnxAXbKxEpru-KZSGcDY2DQtDnNmBa7UDOIJaA8H6mzU9BS6TYut3bzfhQWvIENMijBXZlOJum7PQ-1e3xpps9ju0P4gXet7aeEce5Ow35CbrVwr93xUxMAdwCFxSPJ5TTCkUIMXlTJz3zFt0GRa8-hTAaU1jnfzhP7E-THwEH7pCwsRHChaa86vW4SLQkDLDpOdK8a4nfrwpyFCIcrDaPqzTHqCb4vAPtzQmfrpPqR-gn-N0N5RsJeB-Kid0c9MwzQ2ks" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79a8ee04d3.mp4?token=WuJs3AzB9VPN20BBa6qnxR9_2QJdjsrw8PmW636pEIqXRQjd7uvQQQ3OOTAUrP8qO0Jd2PQLPn_vs9Woi5_RKEUEuN3slXXufOdkgL_hhefuwp-XQN_0KGlmg8vK1iQtUiZJN9a_b9AiNfb1CWBLyUlsisIHyMQt8zDqWJBiqnl7GVKD0blh4UAqfVG0vMmcq-aUai3smaQHLjklG320g8C2meQAYTGV2X2aR8qvtIYvkbA5ngfC0j-xzzv8C603sNmaFP4z-TRoEFhZ535r0oQ3cwAprANNGasnceYWEySg8PEKOQx3hcDTPpd5COMDQ48idLHWMlzNlTbhRl6k81jGUGLReyDP3HByirv1qx7LKhOroZTV97c1u0dnLqCvKsbQQl1iPY5kswwLs4puo0zAFi-Wd-GCLbwKHCnxAXbKxEpru-KZSGcDY2DQtDnNmBa7UDOIJaA8H6mzU9BS6TYut3bzfhQWvIENMijBXZlOJum7PQ-1e3xpps9ju0P4gXet7aeEce5Ow35CbrVwr93xUxMAdwCFxSPJ5TTCkUIMXlTJz3zFt0GRa8-hTAaU1jnfzhP7E-THwEH7pCwsRHChaa86vW4SLQkDLDpOdK8a4nfrwpyFCIcrDaPqzTHqCb4vAPtzQmfrpPqR-gn-N0N5RsJeB-Kid0c9MwzQ2ks" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گوشی تاشوی سه‌تکه Huawei Mate XT 2 معرفی شد
🔹
هواوی از نسل جدید گوشی سه‌تکه خود با طراحی U‌شکل رونمایی کرده؛ ساختاری که برخلاف نسل قبل، نمایشگر را به سمت داخل جمع می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/685521" target="_blank">📅 12:33 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685520">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
تیم ملی والیبال بانوان ایران چهارم آسیا شد
🔹
تیم ملی والیبال بانوان ایران در دیدار رده‌بندی رقابت‌های قهرمانی آسیا ۲۰۲۶ با نتیجه ۳ بر صفر مغلوب ژاپن شد و به رتبه چهارم آسیا دست یافت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/685520" target="_blank">📅 12:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685519">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
کاهش جمعیت اتباع خارجی به زیر ۵ میلیون نفر
رئیس مرکز امور اتباع و مهاجرین خارجی وزارت کشور:
🔹
جمعیت اتباع خارجی از ۶.۱ میلیون نفر به زیر ۵ میلیون نفر کاهش یافته و طی سال گذشته نزدیک به ۱.۸ میلیون تبعه غیرمجاز از کشور خارج شده‌اند.
🔹
همچنین جمعیت دانش‌آموزان اتباع خارجی از ۶۰۰ هزار به ۳۲۰ هزار نفر رسیده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/685519" target="_blank">📅 12:24 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685517">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/920d463811.mp4?token=VQ780u9SrtxvaQA1AnTEh2RVUyJn7NvnWlt5Equwbg5KawwFnIeHFkh9eE5mEp1_HDgeRs4Pv1XRbvgEBX7aRhjzoKCbSmkelk-VdJzHIqcxucLcsn6aoZJKVNziqSgKD7Y-69KthG9s6CWX5ZYUexZVpbq36kgMyAh7_zwi_YawgPn4eCczzcFwqY7gCPYxSWnSfJkoqyfOR0aWKTtakP95pJJBBAN8ZqVjIWZ0WecQFkDuNUNsq_ImZrw_IMbsJc28yAM8Jz3VkUL9jIAPuCp8rPtVcHPIvoXxOurP3nrD3ahlVbYJaRtgBcumBoGXVGMySFT7eJVDF6pRcJM4bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/920d463811.mp4?token=VQ780u9SrtxvaQA1AnTEh2RVUyJn7NvnWlt5Equwbg5KawwFnIeHFkh9eE5mEp1_HDgeRs4Pv1XRbvgEBX7aRhjzoKCbSmkelk-VdJzHIqcxucLcsn6aoZJKVNziqSgKD7Y-69KthG9s6CWX5ZYUexZVpbq36kgMyAh7_zwi_YawgPn4eCczzcFwqY7gCPYxSWnSfJkoqyfOR0aWKTtakP95pJJBBAN8ZqVjIWZ0WecQFkDuNUNsq_ImZrw_IMbsJc28yAM8Jz3VkUL9jIAPuCp8rPtVcHPIvoXxOurP3nrD3ahlVbYJaRtgBcumBoGXVGMySFT7eJVDF6pRcJM4bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر پاهایتان حالت پرانتزی دارند یا زانوها به داخل یا خارج متمایل شده‌اند، این تمرین‌های خانگی می‌توانند به بهبود وضعیت پا و کاهش درد زانو کمک کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/685517" target="_blank">📅 12:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685514">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f83e55167.mp4?token=dOw5csm8KQvv4rvNBxscau0Tb26VhdSu8GfJoU45OlHwTUmvpD9WTT0W2ymU0i6d5t814TTuAveOSUhQXzAOwGj_yVePZGrsPQ8_wBd22mo1H8ajBJEpCLq3fF_7NpFgCywuPWFlMHusbRtASBibd8kaxv3Wn2U5UHiHc76PBfI2A-c7Y2hWYOPL-1H2onzifbavHtFAPlNg_EWRBtMCSFaVY4qvJtrqp8odumWjnXAl1oUUewBOBkMQwR0934HcxXaoN6NHvuayIJvYubrZTgA8oWMUKd7VkgW35A9sFz4xlvnxgaR7hXj57FD4m5Yt9SzQSQqRJiShn7tgXFzDtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f83e55167.mp4?token=dOw5csm8KQvv4rvNBxscau0Tb26VhdSu8GfJoU45OlHwTUmvpD9WTT0W2ymU0i6d5t814TTuAveOSUhQXzAOwGj_yVePZGrsPQ8_wBd22mo1H8ajBJEpCLq3fF_7NpFgCywuPWFlMHusbRtASBibd8kaxv3Wn2U5UHiHc76PBfI2A-c7Y2hWYOPL-1H2onzifbavHtFAPlNg_EWRBtMCSFaVY4qvJtrqp8odumWjnXAl1oUUewBOBkMQwR0934HcxXaoN6NHvuayIJvYubrZTgA8oWMUKd7VkgW35A9sFz4xlvnxgaR7hXj57FD4m5Yt9SzQSQqRJiShn7tgXFzDtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سوخت چگونه از مخازن زیرزمینی به داخل خودروی شما منتقل می‌شود؟
#موشکافی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/685514" target="_blank">📅 11:47 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685512">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aIBJOL0elxvvu6PphSHWrdHdfpV9JEEYGmw6TAWJff5VJR-SLqqjqyx9Zaz9mHGkLNnLe4pGXOXAmqew8R1DK56cjXNa8NEkij9W1xTykpYEmK2TCW-uUuKA-DOVoL4xHkIgIkxsqrMIrGAaD0a0g6YCEu8yA_Nqbx56DogvAZRYDH0QC6U-hD_iVn2vjJfIP9xubLZ3B1PDy3TCW59KxEryYyCMBJ9ziC4R0GIC2vUtdFjKaPEBKyysITNo5SE8N37zCwx0RxEPszuZwAoOsOwYFieMCFK04DJDQR10KqpPP4JZyaUCY5oZPZWcGAib1gIIKV0p4oGrTH2bOl9K0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OiUxh1vIK461JGAMMXgQleEoPHO_KLVb0Kj2stp3w8Ql25xloEiGNBQF93SWjD_aaZkLJwzXs38nH5CN5fWcDOmhG7W322TC_CKo-PoF7_E3zRbQSRvCl47JjVwYMvI4DQZ_hV0WEcN_bP8m9pYD_lYvMaYz_i3VOWXhphzuwsgXp1vL67_YkAV9kB7hPtJxou7ZB-AErJru_8FXjwAbBGHZysQzKe3PFLvO7gcLMTssyZtAFcZYnWSA9KUpspm5xPTGkeBl8ug93dQA5otlzj-kDjc0TKG8SrLubPIK93XUlWPl2hmrbg72LAKacKIadaEvx5NGB4EmkDnKDEYj1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
آزمون تافل در ابهام، آزمون دولینگو با محدودیت روبرو شده است
🔹
دولینگو اعلام کرده افرادی که از مدرک هویتی ایرانی استفاده می‌کنند، امکان شرکت در آزمون این مجموعه را نخواهند داشت و همزمان، گزارش‌هایی درباره نبود امکان ثبت‌نام و انتخاب تاریخ آزمون تافل در تهران منتشر شده است.
🔹
این تحولات، ابهام‌ها درباره دسترسی داوطلبان ایرانی به آزمون‌های بین‌المللی زبان را افزایش داده و لغو یا توقف برگزاری تافل برای ایرانیان هنوز به‌صورت رسمی تأیید نشده است./ فرهیختگان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/685512" target="_blank">📅 11:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685511">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
سود سهام عدالت در روزهای آینده واریز می‌شود
؟
🔹
رئیس هیئت مدیره اتحادیه تعاونی سهام عدالت کشور از احتمال واریز مرحله نخست سود سهام عدالت در روزهای آینده خبر داد؛ با این حال، زمان دقیق و مبلغ نهایی سود سهام عدالت ۱۴۰۵ هنوز به‌صورت رسمی و قطعی اعلام نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/685511" target="_blank">📅 11:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685510">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a2c950187.mp4?token=M4x4ppLMqZ6nEICfmK10g4g2mEcWLtchmTBFMVK9cbWvJ6_P_EE9egYqy6bkk_HtkzJ_L9zA_vspkJ2H2XaZAxlTAMvRfaihJmRO4WLiTmlx7sapGQYYC1N4fCWXNRlHA4XQZjDzo-lIdvPAsyC1aAp-JZULb_zaQBRzzLyhC80ibWZCORpXvSLVFiUGbv3-Br_123Qp_qbjgW9GHSzAv2GaiTR5GA26kD7om7A2NH3Y9b-rxWBlKc5wHJCpW6yo9cTr5Zlh-KYrY8NccGf_2HIJyX3qv2l6DwnPJCGpcuBM1gaX2mUU5PsglCdgvXlCxK1oV9VcgKrmWAhC2gQ_RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a2c950187.mp4?token=M4x4ppLMqZ6nEICfmK10g4g2mEcWLtchmTBFMVK9cbWvJ6_P_EE9egYqy6bkk_HtkzJ_L9zA_vspkJ2H2XaZAxlTAMvRfaihJmRO4WLiTmlx7sapGQYYC1N4fCWXNRlHA4XQZjDzo-lIdvPAsyC1aAp-JZULb_zaQBRzzLyhC80ibWZCORpXvSLVFiUGbv3-Br_123Qp_qbjgW9GHSzAv2GaiTR5GA26kD7om7A2NH3Y9b-rxWBlKc5wHJCpW6yo9cTr5Zlh-KYrY8NccGf_2HIJyX3qv2l6DwnPJCGpcuBM1gaX2mUU5PsglCdgvXlCxK1oV9VcgKrmWAhC2gQ_RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فوت ناگهانی هنگام سخنرانی شبانه
🔹
نعمت‌ الهامی از چهره‌های شناخته شده منطقه مغان و کاندیدای دوازدهمین دوره انتخابات مجلس شورای اسلامی از حوزه انتخابیه پارس‌آباد، بیله‌سوار و اصلاندوز، به‌طور ناگهانی دار فانی را وداع گفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/685510" target="_blank">📅 11:33 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685509">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQjSfM2T2q5Ryylb_4slTUGcO4d8SyXyDV3FZ1shzNV4Rr4SeBWRwOo4DfFJNUzgKD4t47GS2MXo83ajX3z97PKm4-V89TWF1wzaATVsiNPuK5fk03COestziCcbK1dr_9ZfCLPKYtd7n2GWUzyVI9eIXMU4_33m2gsX_6c86TXKq8EAgbbcU0F-qHSo1jJFJa-S0qWVJ23hvgiLQAZ2Gg6ZxbNhC3sC5_Zo1p9ZSKWfdvwmvgv9RhnXxSKBN-5UhVsEe7Am4-5v6BQUgNnuPzX9PfQ8E5MBrf_8qvaMg1WBeRUHsqdQpbS1dFt50GfJq6HZCxRA2qu0Cco3L1jPXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آماده‌باش سرویس مخفی آمریکا برای حفاظت از پسر ترامپ  ادعای سی‌ان‌ان:
🔹
پس از پخش ویدئویی از تلویزیون ایران با عنوان «بارون ترامپ را کجا خواهیم کشت؟»، سرویس مخفی در حالت آماده‌باش کامل قرار گرفت.
🔹
این ویدئو حاوی ادعاهایی درباره نظارت بر دانشگاه بارون ترامپ،…</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/685509" target="_blank">📅 11:29 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685508">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81ff99cf26.mp4?token=ODo1rvsNYj5bpx0uw1qhsHVPMRcTEF_aaBgqVY-fHDSkbqIfhHCVz_fGZjPuQwZCjussl3jcqkjIxuj5rxZltVFeMTZ3Wwb_S45oFleAlJ3fDvfbX4KKMx2PyvC0FcdSBmyGVLw3NyL2q1NxZBz4wHGO80psrRn_LAN7Mfj9AvQf7vBTxmuyiQFmJ1d0BuYqMQ0anppCiy9aPJiyxyu3HpVvMy3vCozf-5Ugd2P86N2XK6mFIt2H5h3qUiYCdCVmossfJCaSdEWy0fIGHwfvE9FOoreJW1a0MVHmHwzLf4qNLCxLxv3RoXyRJW0kVbbYVrR1K0hqS5ODXD9xvaKbIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81ff99cf26.mp4?token=ODo1rvsNYj5bpx0uw1qhsHVPMRcTEF_aaBgqVY-fHDSkbqIfhHCVz_fGZjPuQwZCjussl3jcqkjIxuj5rxZltVFeMTZ3Wwb_S45oFleAlJ3fDvfbX4KKMx2PyvC0FcdSBmyGVLw3NyL2q1NxZBz4wHGO80psrRn_LAN7Mfj9AvQf7vBTxmuyiQFmJ1d0BuYqMQ0anppCiy9aPJiyxyu3HpVvMy3vCozf-5Ugd2P86N2XK6mFIt2H5h3qUiYCdCVmossfJCaSdEWy0fIGHwfvE9FOoreJW1a0MVHmHwzLf4qNLCxLxv3RoXyRJW0kVbbYVrR1K0hqS5ODXD9xvaKbIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کف پا مرتبط‌ترین اندام بدن با ارگان‌های داخلی است
🔹
باید با انتخاب کفش مناسب و استاندارد، سلامتی پاها را مدنظر قرار دهیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/685508" target="_blank">📅 11:10 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685500">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sP3i7HgTj8EXQo02O6-ChX2OQBnb8ydKIe_vAlMbIztVWueFj3Sa2nTA8NdwOD-BpDq3D3HEOOO_nC0wcRkDDY3B8n28qjrhNr2SwK-hSlr4tdHGkBI1pem3zqQDvf-ubHcNKunZ8vcraT1Lj8IiBIVIqbGATDSb4kzSg6ECnQJF-RLDTaGYKbpQPJt4AZt1SAMXoWL5bp6V3f-_8z8w2XComUK83chKtuBtijX_NeNLABVzlabNGtMFYMvEuDkpq3lHdvpOA6v87MjKn0kZ3vBeoh3txuf_8W5_O0cLpKUqJqiZYY3NWr87DwQUWd32XQiEK8J2I3-RkH7oCTkEpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VqoxqKBCasOEoXaUpGyrxdKnUXwhyNkn-d54t_M8JOS99a1053LidXA0Exr-UJQecxrTnBx_-_3-4tsgZkn7ELdxZ4vJpc8bBg5BKgHJM1bc9fZXmVhRL7dL6sLAnkNGGQq2dy2gCLTvKrN-KoYjAHsl1cbBeHSnaLXxFkqdlk-lDpCCex9WmmnMzPysAvMAwn8LTZKF7hWDoU7X4yPHlSGij8kghLO-vkGRI7KOn0tcJihZefHPK4AfuBiLJ0Sh-7RCQXyAp7hwbSVuiF05bYkLhWgZIhlcyd40mDvu5QnSCWj--WNArd7IHUT-hR_CdbvKQJIyfdGOY4RqnoaZjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KK7lKLva7n-4YOHV_PWSoH3-YVXURBn-M_aUqt5rkW05cTMC-Q1ntIpGmnBf_Z63Wqv3_UyjQ648-IFEagToOCE_dsOe10Yheom0VPBeGYIUNUDp6Y8jA5QDFI7Ux3g-BL5w9KJSX7Q3OyKDzcRbk2ZqebPqO_3ECitP0mMZj8Dx97x-3tYct91WTudhpLfHBdc-TJp-ZfZrEhIgQYtwMTM64KVoKHkZNipelMMgcIU2FaoqLokNMVGL0yih7p4SsMczQ6RlBNy1GWMsf5QkNDarjPw23Qq-FBiigYN0OaaxFnbZGV1drQsUvThMPCAKqoBK8x0TNYesJGX7htjX9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YRao_-wlH6ni4P2doIFw2Pk_NPy9p0_mUVtDu7XXjeOfxNRkvwJWF6K-_i8Nj3VK0yndFyF7oflsyuw9A0-Gmxx7vwzKcb-VrWlTSfX-Eee9ePyDHErThmCOeBLBxowXKiifEwdDiBepLVZSUcGbnSkiGW5lr1q2d-tHyhXnBImLli8hdiYJHFh3PPkDdZZZCmfL6kSmK6rsE-qqDqFp78nV54Bdhflu2_cGr2rC6DaMn85ZFao0NK42flO_LhqN8cy5GdCDxmLTlnhzAr_CYGCFFYX2pgLD59tERDGf2AsMYnMO9dPjw4Zce40a7UUBpAx1rd9hLwZ-5qMbhn-Dcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rCIx_h0R-w0moo7c1gbzV_Beu26yTcklhnsydUCYZvsv0L0o8-UANccyeGoQ69dUlIIJL2UvWPwInBsLHW9-UvLNH9I0KYaD2MKww7R8SJhCB3omPVo3WDQWKShVhaf4ZDGa34YZCB_hoBlPUu44fcb2GOmsez4MP-0sa01UXxW5XcaAu1GWzWoHEADqKKgc7yf9oqL3_VOYYwmiB8zzjszz5JZSHVFZzwg5sIkVaChbklHlwq4igiPR7g76oryDsjMIhJCRY336LLOzQcVorn-M_bIg-jsBrKaLh-PXEIFyekRNoYmeV4AJ8uFUJAHFxlg-558Y9Lim_S9IN6vHtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GNAfCQLuiYb4DN535LOJQIpl5_kv0GMSmZ8Nh6rtzMieiEx23C6OvDyO_5gHRdQQVu-5_wDcRNJCcg9YNHdppWl5C0yeDx0I8rqVpEMEY7Dtak0mBFejWhdKLB4DYFVyd55ufO-NWaGR7UMWQ4E5kSj3CyOSuHEWY71wfrBS-Z8cUqVPKzSnOqhMxl1A-lLaA2kmpPtDbOKqLfH5mYjaBw5nWUWHAXecfJwfLXGP4e_THJ_KAFEzgFevxcY9nwtFLuY1-B5yGnoc_VXpY-u8rn7k_6kxLQmKlnMBk-CI1uMxAZPtGU-4Zi_EvdN_ZHfjpXNvoqBwPzqOV-7612QBIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YYsx0V_8yjgICpTv9FpijhxH9Nqt2ehHkCLZ_7tyyUeLhjz6yj5WvEY4xTAOM7O_U7HpSUylUDWWTS2i6ia6Kyo2Eg72xWsVJOfSGsm7YfhV4lAM4YKcywP3PkLiEzgNT92a7pDo-V1-3stFQ4EkdcrGcH9XzxWFyfl7oCJHc2jLNdLt5yKUG2UFqVKcuUN4rxEDOXbqeqqWGO5kqLve4KbalHWLZX1Y25xc2_tRNPBaSRRtXvjEa6Xvqns-aoKIlMjvkNREPJhpwVV34LdM6-SL8FDP9fJTWpi5xVTSr_wKhghSFxsY-Yg5mUqJSncqKf0b17hoNXz_lY14u2aLmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ETWWDUBdAQ9pRR3DISkUo_7AHGFqQ5gYpA0Av5B8EnjXIGCjEIT5BxvceCrlJ-yHnXT_s0xNeiuqyXCL7MQNkbymM05LOnbFCXD69Jm9rm3OrKIEjWpKMDPLRSXIiOkHU-bFo9cGdCCoyEPNtY2jze6stohid0Id2ByZVc3EV4YDuNlblTYOm9Yv371Cv-hzoWHOxCeiGkcuc9Bit7mXNesQaRUUxkbd0xVN6sx152mXJzTPLJQciqQ17RZcUWXBV7jpomhiQs-FhKj1R7VdgMTiXYCGxDI2p4tBTQ_tMhmmbrLX8WKSkURtFeOFjklCahJQYjlDSeqCHzMRnDw1FA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری متفاوت و تماشایی از ماه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/685500" target="_blank">📅 11:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685493">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f00434ac85.mp4?token=EtYLpWjW-kfGqcb_ZTyrxOd0DQlv_3ENfGUOX2jKDk2PUNYv9_8u_kZkrYIm8xnUM-kLQV4168CEwLA-8n3sAL4d35oXUSu_auSMFF_cP0pjEE98N5pXWDZ_sqtWc9mGdDfMjkTGC_zLnyWtBCvd4eRU6BXQdVT_QuIlzkCA_GtdPFyyVlYhFD_ZGlbevM8442hTtxu7UU-z5LFjgJ-cHh8O1m18ZMJeXryW_eA2XSW7MusyV7ukfnru-YHTTSUkmZBk-uKlIkOUc5_jMAwfECYQ3ABwuN6zsWvyMgzVOvDPUCtpD0hZT9yIu3lqJxwM5ZMYvJeHWKn3uiflMMzOuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f00434ac85.mp4?token=EtYLpWjW-kfGqcb_ZTyrxOd0DQlv_3ENfGUOX2jKDk2PUNYv9_8u_kZkrYIm8xnUM-kLQV4168CEwLA-8n3sAL4d35oXUSu_auSMFF_cP0pjEE98N5pXWDZ_sqtWc9mGdDfMjkTGC_zLnyWtBCvd4eRU6BXQdVT_QuIlzkCA_GtdPFyyVlYhFD_ZGlbevM8442hTtxu7UU-z5LFjgJ-cHh8O1m18ZMJeXryW_eA2XSW7MusyV7ukfnru-YHTTSUkmZBk-uKlIkOUc5_jMAwfECYQ3ABwuN6zsWvyMgzVOvDPUCtpD0hZT9yIu3lqJxwM5ZMYvJeHWKn3uiflMMzOuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وحشت در ورزشگاه کیپ‌تاون با عبور خطرناک ۲ هواپیما از بالای سر تماشاگران
🔹
پرواز نمایشی دو هواپیمای «ایرلینک» پیش از مسابقه راگبی آفریقای جنوبی و نیوزیلند، تماشاگران ورزشگاه ۵۵ هزار نفری را ترساند.
🔹
یکی از هواپیماها در ارتفاع حدود ۵۰ متری نزدیک سقف ورزشگاه پرواز کرد، اما مسئولان اعلام کردند خطری برای برخورد وجود نداشته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/685493" target="_blank">📅 10:24 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685492">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCuJ5XFD-4wtphN7pwT9RLS0XFV1T2tXLkvcWh8BTXetTQu9t1CMkHJxxheAls4rznM9aEnLJgX9XuV-5AWStyDCYcwLVfo_KiHnj4Ja1btgalpJr9F4D_bnXXYRaQzxOwqq84FNZEz1WyXO_0eBfB-hvbgorvHSi4u40bZqOEdeMkQYy3T1R6VzsOTxq5nyUUCF6KZbYoRJdwfqKjjj4p0HshXXFRscMFiwWNwlLnqzYF2z-iuotpXT6utrpKeksygRfUI121NiD7-Jd1CHSvx_CQYlTpttoLL1q1qUsOuPeCzhCIeWkUV0fqpjmE_mgr9m4Ckn25mPNDutuiCZ5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهنمای دریافت و اهدای خون
🔹
دانستن سازگاری گروه‌های خونی در شرایط اورژانسی حیاتی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/685492" target="_blank">📅 10:18 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685491">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OSXvavIZ_eTYxHXcYt6jsutmDjnICa2s9WFyGKEuo5KYqvTMDlKmBNOCF1GkJdsGjDVTOcoKJmpQW85kz_c5yVTsZE3oBgdOz0wfBLvJHxTBsLvBR7zknwHvyxkoGiaO-MYbm6644GqV_rPdEpAP_DMCk4y6c0KUT77Sv0__iZVoYVP9Ln-eFb5VPnvecXuR0vEY6CRMfSRRaqRIIZH0NvQadTnYjZwiHG9lBAWO0mg25_tet4GHNSblUqdWoYPo_v9-kDWqrOokZAAdm40D5vvjBclcOl634KdoTSE5u0nFosy9A3UXDYCPdO2MVWi9yAuNX8yGZPe_lgQTsoU-YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یوسف پزشکیان: اگر غنی‌سازی نکنیم نمی‌میریم!
🔹
حیات ما به غنی‌سازی وابسته نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/685491" target="_blank">📅 10:10 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685490">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd0ac0aa2a.mp4?token=DhHNx-cZ9TE8P5V8f5VhcUTfytjo89EoyFipHaKUEgTgGYMqMzMpQZq7IiJqosfLjJ_88h8x6GCpNKOX9uMn1hQ7r-uuRaIpWvSn65Dkav68OZKerdmNA6rKhcwY4e9uZLe2t9leAVueuaCnac4t9ojFnO3pu2o0bIpzrB8tUlBWCPjZUTXFMJ5T9dvADVzDvWtprPDQL4nCLDZalcHVDVsA_THuZaImw6LxOqZo8wVxa6Wg2Ct8frDVcm6sneW_1Rg2uHUlxy5kDNgd3G3gC2CTmpyxdWDFgVLVFdqJuKfi6FTVop_xkb1TpFiVupIKYyKyPY2U-nsdIfiwqmyihA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd0ac0aa2a.mp4?token=DhHNx-cZ9TE8P5V8f5VhcUTfytjo89EoyFipHaKUEgTgGYMqMzMpQZq7IiJqosfLjJ_88h8x6GCpNKOX9uMn1hQ7r-uuRaIpWvSn65Dkav68OZKerdmNA6rKhcwY4e9uZLe2t9leAVueuaCnac4t9ojFnO3pu2o0bIpzrB8tUlBWCPjZUTXFMJ5T9dvADVzDvWtprPDQL4nCLDZalcHVDVsA_THuZaImw6LxOqZo8wVxa6Wg2Ct8frDVcm6sneW_1Rg2uHUlxy5kDNgd3G3gC2CTmpyxdWDFgVLVFdqJuKfi6FTVop_xkb1TpFiVupIKYyKyPY2U-nsdIfiwqmyihA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویری هوایی از قله کلیمانجارو؛ بلندمرتبه ترین قله آفریقا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/685490" target="_blank">📅 10:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685487">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9394581bae.mp4?token=RG71K0rXz6c5FN6xVEBu4zNKhsc4A3AfrnvtZ4tepfaIrHe-TD1U08X3id7rkkhW0cNO50ZBWKzHIarJuowjbSJ18qOm5zd4wHEYQJdeWrivlM4K0CmVCirlD6fST0_E_QlvE9kwVdUpGlabBS5dIxGYoOYEN6uhYNfvpQ56cfEnuOjcMK7tMueefHfg08VM1KpAxolwfbvioNOUo1XSPnRUOgZWPFFprC_0nSeGYNqG8eax3gaGdSFeOOuaUC_IreMVvxt4l3DY9JOjVkOjXQNXJUoe40nEJwKYNHOWr0poUEPmoVLSDcWh_GaK-H3pg1VKlReFz0FwHjwc-uR8kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9394581bae.mp4?token=RG71K0rXz6c5FN6xVEBu4zNKhsc4A3AfrnvtZ4tepfaIrHe-TD1U08X3id7rkkhW0cNO50ZBWKzHIarJuowjbSJ18qOm5zd4wHEYQJdeWrivlM4K0CmVCirlD6fST0_E_QlvE9kwVdUpGlabBS5dIxGYoOYEN6uhYNfvpQ56cfEnuOjcMK7tMueefHfg08VM1KpAxolwfbvioNOUo1XSPnRUOgZWPFFprC_0nSeGYNqG8eax3gaGdSFeOOuaUC_IreMVvxt4l3DY9JOjVkOjXQNXJUoe40nEJwKYNHOWr0poUEPmoVLSDcWh_GaK-H3pg1VKlReFz0FwHjwc-uR8kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ورود سامانه بارشی به غرب و شمال غرب کشور و صدور هشدار نارنجی سازمان هواشناسی برای برخی نقاط
🔹
هوا در نیمه دوم هفته خنک می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/685487" target="_blank">📅 09:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685486">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50c84f5d91.mp4?token=XNcOkz_cNdSw3pFvLUYHpLtU7jIHnHjgLd_EBLXlHOwuEUNtmCo8d4nR7yOmMieJ1wVSB7TyW64EuXYktpvwXm0X8zPgR7cqU3Bfvj16WQ_EEI691s9NHbVxI7HY24_WdoZwaPGiMufRJcwf5QVN-w-hjdh8NzqI7kjzaVoilDSJXf141YvcykX989l_xvHgtdtZWT1ciyeRQHHDGTnH_SS95Ll6KqRs7wIh9S1umlWfTp6Mjagnu7c-D0sAg54D5f-G1prw30Ix8DgHLKf6W8td8_Wgp9O79LTGSuJm6jR1l0VZ1seL3Rk1qkzjllZUDuZLCJoes4A8JYni3YtZVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50c84f5d91.mp4?token=XNcOkz_cNdSw3pFvLUYHpLtU7jIHnHjgLd_EBLXlHOwuEUNtmCo8d4nR7yOmMieJ1wVSB7TyW64EuXYktpvwXm0X8zPgR7cqU3Bfvj16WQ_EEI691s9NHbVxI7HY24_WdoZwaPGiMufRJcwf5QVN-w-hjdh8NzqI7kjzaVoilDSJXf141YvcykX989l_xvHgtdtZWT1ciyeRQHHDGTnH_SS95Ll6KqRs7wIh9S1umlWfTp6Mjagnu7c-D0sAg54D5f-G1prw30Ix8DgHLKf6W8td8_Wgp9O79LTGSuJm6jR1l0VZ1seL3Rk1qkzjllZUDuZLCJoes4A8JYni3YtZVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای
کارلسن: گزینه استفاده از سلاح هسته‌ای تاکتیکی علیه ایران در پنتاگون مطرح شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/685486" target="_blank">📅 09:33 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685485">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49cb916dca.mp4?token=YO2E2NVN-ACJe-5162wQ9VLXCgP_pwop5hFYjkMz_c8eBFqOcsLuIGyw50kjP3g80PpI1GRHo6W5wrTI2p5FV7Tz0VzCl4aRHuUXxbNjCluZK7C3Kybd-crAFBSiWHfBdYu8PNoMfT_hZ8NdZvEHzApgEvUKtvZPkbB4B42Mt_-ppxWijpSGxA0BjmNpUXQPjU59soAGIuTM0MHETvP-dq9pidG8yfZ3nibDnr-jvFUdR8MesTcm01Z9cg0YLkqA-uzgfZzTxb7xFAQu51o17i5BJ-4oEMzM0HsNnXC4GOObfI1pQIIqI-Y9-Q_nXe7Wvx1aEp6rX_1OUv5xFOfbxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49cb916dca.mp4?token=YO2E2NVN-ACJe-5162wQ9VLXCgP_pwop5hFYjkMz_c8eBFqOcsLuIGyw50kjP3g80PpI1GRHo6W5wrTI2p5FV7Tz0VzCl4aRHuUXxbNjCluZK7C3Kybd-crAFBSiWHfBdYu8PNoMfT_hZ8NdZvEHzApgEvUKtvZPkbB4B42Mt_-ppxWijpSGxA0BjmNpUXQPjU59soAGIuTM0MHETvP-dq9pidG8yfZ3nibDnr-jvFUdR8MesTcm01Z9cg0YLkqA-uzgfZzTxb7xFAQu51o17i5BJ-4oEMzM0HsNnXC4GOObfI1pQIIqI-Y9-Q_nXe7Wvx1aEp6rX_1OUv5xFOfbxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کدوم امگا ۳ برای تو بهتره؟
🔹
منع مصرف امگا ۳: اگر داروی ضدانعقاد خون مصرف می‌کنید یا مبتلا به هموفیلی هستید، این مکمل مناسب شما نیست و یا حتما با پزشک مشورت کنید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/685485" target="_blank">📅 09:23 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685484">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_p9Eb8d-ebtBVEWflISiePe0WmzkSqltO-l_UibfbF2a3dvxCAB7xRlygGgkw5H5AfSxKoV9CMethMnYgo0_-YTIA7N5YHLAJmsUZmXIRhPadLAS4kj0Wf_QgCNIQDPgZPw_K0tyg5Ygryi4txomFyHNdnU1GEXmHCkbxUNpQbhdP1MjPL_Qv-zyLQgVYK6bq_aHoA9BXRfGVXSZwMz2ep1fQXXUOjiGr_O5DZana1acCs6EvjvCMxg6vq1kI0n-uzdvixGIBdZJAYi2DGFMuh4VBpIb9cVfqqJNnHOrB34AkuUjhcgzIRK6yRqqUAEa2GQZtpbO8cR2AW2qRTXKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رهبر انقلاب: حاکمان آمریکا و رژیم صهیونی، دشمن همۀ امت اسلامی و حتی حکام این کشورها هستند؛ بکار بردن تعابیر زشت آن‌ها نسبت به بعضی سران کشورهای منطقه در حافظه‌ها موجود است
🔹
حاکمان جنایتکار امریکا و نظام جعلی صهیونی دشمنان قسم خورده این اتّحاد و دوستی هستند.…</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/685484" target="_blank">📅 09:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685483">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
اتّحاد، دفاع متقابل در مقابل کفر و همکاری مسلمانان؛ سه گام برای وصول به تمدّن نوین اسلامی
🔹
درس مهمّ اتّحاد و عدم تنازع، درس اوّل مکتب اسلام در مورد نوع مواجهه با دشمن و دوست است. امّا درس دوّم آن، دفاع از یکدیگر در مقابل کفر و درس سوّم، انواع همکاریها و…</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/685483" target="_blank">📅 09:17 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685482">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
رهبر انقلاب: اگر مسلمانان متحد بودند، فلسطین این‌گونه بی‌پناه می‌ماند؟/ حکّام کشورهای منطقه دشمن واقعی را بشناسند و  با آن مقابله کنند/ اکنون وقت آن است که مسلمانان به فکر فرو روند و حوادث را دقیق‌تر بنگرند
🔹
آیا اگر مسلمین یدِ واحده‌ای می‌بودند که مشت خود…</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/685482" target="_blank">📅 09:13 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685481">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
مقصود از وحدت، محور قرار گرفتن نقاط مشترک میان مسلمانان است/ مسلمین باید «اَشِّداءُ عَلی الکُفّار، رُحَماءُ بَینَهُم» را محور فکر و بیان و عمل خود قرار دهند
🔹
مقصود از وحدت آن است که در سطح عمومیِ جوامع اسلامی، نقاط مشترک بین همگان، محور و اصل قرار گیرد.…</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/685481" target="_blank">📅 09:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685480">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
رهبر انقلاب: هر کاری که به تفرقه بین مسلمانان بینجامد مقصود دشمن را سامان داده
🔹
اختلافات عقیدتی و مذهبی گرچه یک وجه مهم از مقصود دشمن اسلام بشمار میرود و او به استفاده از آن بسیار دل بسته است، ولی به آن بسنده نخواهد کرد و تلاش دارد تا انواع تفاوتهای نژادی،…</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/685480" target="_blank">📅 09:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685479">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
رهبر انقلاب: بدخواهان در کمین وحدت مسلمین هستند
🔹
زمان برگزاری اوّلین هفته‌ی وحدت به اسفند ۱۳۵۶ هجری شمسی و دوران مبارزه با دستگاه ستم پهلوی برمی‌گردد؛ آنگاه که رهبر عظیم‌الشّأن شهید اعلی‌‌الله مقامه‌الشّریف در دوران تبعید خود در ایرانشهر این فکر را مطرح…</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/685479" target="_blank">📅 09:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685478">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
با میلاد پیامبر(ص)، چشم‌انداز سعادت بشر درخشش دیگری یافت
🔹
ایّام ولادت وجود مبارک نیّر اعظم، اشرف خلائق، سراج منیر، برگزیده‌ی خداوند، شهر علم، حضرت رحمةٌ‌للعالمین، رسول مکرّم اسلام صلّی‌‌الله علیه وآله وسلّم و فرزند پاک و پاک‌نهادش، حجّت بالغه‌ی الهیّه،…</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/685478" target="_blank">📅 09:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685477">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R7j1PscO3NeyiS9P85YO3duBT80vhMWmKTLkWjrkHiH5sJEPJaP4LeWQ8gItsxyH_euna462M5CE_9AaPH9jik8uj0l18b-wMon53GdLaCWsiJCpe38VVZzwYKFa5FVCxONSOtqOxFSzKm7LoyDcSOJY2N0Nmc2PEWWI6kDmCMxay0B3Z3NI8tC4gbKaQ41Jki30CrA58BMJnb5HbIR7KfJ2tF0Cqk3_DsLGuWm4BBiKtVKtVVR_LfxfS_4S8OFoMnAtKHVzrYCjOvIDE471zqlfm3Cbatu-YLL1dVH3VPDQYakmW38tu0V4GeLAM3WeozGlsKL9tcUYLf4TZXfbPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با میلاد پیامبر(ص)، چشم‌انداز سعادت بشر درخشش دیگری یافت
🔹
ایّام ولادت وجود مبارک نیّر اعظم، اشرف خلائق، سراج منیر، برگزیده‌ی خداوند، شهر علم، حضرت رحمةٌ‌للعالمین، رسول مکرّم اسلام صلّی‌‌الله علیه وآله وسلّم و فرزند پاک و پاک‌نهادش، حجّت بالغه‌ی الهیّه، حضرت امام جعفر صادق صلوات‌الله وسلامه‌علیه را به ملّت شریف ایران و امّت بزرگ اسلام تبریک میگویم.
🔹
از آن وقتی‌که خورشید وجود حضرت ختمی‌مرتبت در مکّه‌ی مکرّمه طلوع نمود، چشم‌انداز سعادت بشر که رَهین کمال بندگی و اطاعت از حضرت حق جلّ و علا است، درخشش دیگری یافت؛ ارواح انبیاء و ملائکه‌ی الهی و قدسیان، غرق در سرور گشته و شیاطین انس و جن، انگشت خشم و حسرت و غم گَزیدند.
🔹
زیرا برترین خلق خداوند در همه‌ی‌ عوالم بی‌شمار خلقت، پا به عرصه‌ی خاکی می‌گذاشت و به‌زودی با خلعت نبوّت و خاتمیّت و با در دست داشتن قرآن عظیم و مأموریت هدایت همه‌جانبه‌ی انسان میرفت تا حرکت کاروان عظیم بشریّت را به‌سوی عبودیّت و تکامل الی‌ الله رقم زند.
🔹
بخشی از پیام رهبر انقلاب اسلامی به مناسبت هفته وحدت | ۸/شهریور/۱۴۰۵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/685477" target="_blank">📅 09:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685474">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c98edaa0b.mp4?token=PH1BrppnkhirKWjcVeSwkfNwwhD4AlWKEovKgMfefXn7OEI9CUL1tTj_v-McHCErCI0Us84bEvyRAIO3lrPqENP_ukrxtrfxbvx1a1zjtuOQjA9lcQ0M3uMGZJhEsV9Ks6oDRAW2c12UnSSGD3ku9s4qoY2t0EiU2Z5mex54c5Ux_tH7oCFQxlcNtMOLFy62Ee3898YH5GYXRzisOStjWjITypgLBU9M_mwSmkZGdjOvMkTp0L-REI4IsB9xUiGunXwXdGvWDUWi4VXCYYgX8JnANxcDRpcmgU_PjQsYyYu5IyGnhRo6nUzgxpd1V2nVTbOij4ExPhvWF38Cr2fBzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c98edaa0b.mp4?token=PH1BrppnkhirKWjcVeSwkfNwwhD4AlWKEovKgMfefXn7OEI9CUL1tTj_v-McHCErCI0Us84bEvyRAIO3lrPqENP_ukrxtrfxbvx1a1zjtuOQjA9lcQ0M3uMGZJhEsV9Ks6oDRAW2c12UnSSGD3ku9s4qoY2t0EiU2Z5mex54c5Ux_tH7oCFQxlcNtMOLFy62Ee3898YH5GYXRzisOStjWjITypgLBU9M_mwSmkZGdjOvMkTp0L-REI4IsB9xUiGunXwXdGvWDUWi4VXCYYgX8JnANxcDRpcmgU_PjQsYyYu5IyGnhRo6nUzgxpd1V2nVTbOij4ExPhvWF38Cr2fBzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدویی از روش جالب روشن کردن مشعل گاز با فلر
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/685474" target="_blank">📅 08:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685472">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwYDtJGo5fwwpkUVwOdZA9k3MJkfqgSpCG8cv-3wWMEsOG4fQ1AA56Jxf9GKLy5Ri3p_RnQlk65wZoLPyVDFZdjBUWBIKtcmiRWlOIwzaAi0d_pF-x8z9SopVmsFECxBUbjwn0hu7TLSqS8pGCzxa4rlVZqaR6wDI_vLcXu_EXpr2j7UhZc05-M1nQRDo0G1NOB4rLuDmmb7hfDYEDTmiCdUP_yjTkT_FnaUHAltBcWcOU4xujksD2aFZcZ9yd6OuCTknj9v2aYPJUVu_xU6tJ55qmB4_tmVCmr-JPgjknC_olaLirDTl0h2KWSY-iW0DPFimHR5Hgi2mEe6YwvDlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
ماه در آسمان آلاباما سرخ شد؛ تصویری تماشایی از ماه‌گرفتگی
🔹
این پدیده که به «ماه خونین» معروف است، زمانی رخ می‌دهد که زمین بین خورشید و ماه قرار می‌گیرد و نور خورشید پس از عبور از جو زمین، با رنگی مایل به قرمز به سطح ماه می‌رسد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/685472" target="_blank">📅 08:16 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685469">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIEG0dTGfxVYglSV_aNix3s2HVRfQVO6iCKCSjuqxbdL8p2aIahU4Q96CQprquB-vQSlyZBlUdS62O7dbP82aqWuqjWWCvsvgbSpliaD7d7qDUpVtlQiWqGqqquC8K3tbjpdKleAYx6t3C78DcTrF9Mkxs-m7jEYV7MHxf0-X4uBIR2g1s9OVaGg5LPcvVfqcNnHmGZE1qqp2c8jkpYToU1f39Y-BSIMERmi7eOJ9jAaiN3fVkdP0L33ymhRsIcvThjHd728x0f1Mmepr5iE2UbVSo-5rqPOqaN6T9GccYEqyIvJfErqnSzZx8C7n9Gt_FmLMLU7u_ZClWquO1yOmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز يکشنبه
۸ شهریور ماه
۱۷ ربیع‌الأول ۱۴۴۸
۳۰ آگوست ۲۰۲۶
یکشنبه‌ها
#حدیث_کسا
بخوانیم
⬅️
متن و صوت حدیث کسا
@AkhbareFori</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/685469" target="_blank">📅 08:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685468">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMGzT5W-q96zFW6mGFKGPXn3QqFKHFiahOkY6Nw0pVZCA-3DfWSWwRrwUSlNDzBRfh7Msv5nL4ylR--DHZK3dEEfs6Lt3sDvFP1jg6Oo3SFqxJE-O8NDTSkkS0t34Oad74v8SkY9RdBadvWjgV3se9yGBo1oh9LCbfeAXSr5pl6DjyWD32NsUxA4a90e4Gv1Qq8eNz5-VPdBYYWkaFavi8m4eWQxOAbXt_28U9CaEMsWY626zW3bZKCzGeBPtua2oMXWxIx7CwUv9r9lI4rQp3tvtRNRg5lDuXyFBol3NVFdvZ7Le2hbcnmcRabMmWeY41FVeoTuya8gX-PXHY3-mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
تخفیف ویژه چمدان خارجی و ایرانی
🔥
چمدون PP نشکن و عمری
😍
خرید مستقیم از واردکننده
✅
بدون واسطه | قیمت عمده حتی تکی
✔️
PP پلی‌پروپیلن (۱۰۰٪ نشکن)
✔️
قفل TSA
🔒
✔️
زیپ و چرخ دوبل 360° سایلنت
✔️
محفظه لباس کثیف
🧳
چمدان پارچه‌ای جنس خارجی هم موجوده
⏰
موجودی محدود | تخفیف کوتاه‌مدت
📞
09153835409
📱
تلگرام:
@Ali_aam06
🔗
https://t.me/maross_mashad
📣
تولیدی چمدان ماروسی</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/akhbarefori/685468" target="_blank">📅 02:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685467">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOmpLRsiBj23N9ilLUo1ffrmEIK7viPHlyKR-J_zP1qDdphAAq2QC5kzLSF5iglkAAFLGt3kXMRwjBexVKN4aWY9_fPiIyNvfS8Kk71SqonRVGoHkCg9cnBIutJ3wOeulkyQ_iipFSzCx7lbirYCwIitSAnOS5mpAUOuc1SgNCxvaLk3iKIQexllqOWESVIZanaWiLGE4y3Pi1SWs5cvaorvk2wz1Zmxtu7dEckhuTTZ4Qtxx2hIlZe8NvnTl9cWxKawC9WA5phm_0-nKMM0aoKj__rlFYpQyr4aulchNlUtFtSc8rau_eslsz8fnm3LMS-4HNioHjA-ZlYu5xIWPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
گوشی نوکیا 105 | دکمه‌ای، ساده و بادوام
اگر دنبال یه گوشی دوم، سبک و جمع‌وجور هستی، نوکیا 105 انتخاب خوبیه
👌
🔹
دو سیم‌کارت
🔹
منوی فارسی
🔹
باتری ۸۰۰ میلی‌آمپری قابل تعویض
🔹
چراغ‌قوه و رادیو FM
🔹
صفحه‌نمایش رنگی ۱.۷۷ اینچی
🔹
ریجستر شده و آماده استفاده
❌
قیمت قبل: ۲,۴۹۸,۰۰۰ تومان
🔴
قیمت ویژه: ۱,۹۹۸,۰۰۰ تومان
🚚
پرداخت درب منزل
✅
ضمانت تعویض ۳ روزه کالا
خرید از سایت
👇
https://memarket24.ir/product/brief/63518/180124/
✨
تخفیف آخر ماه؛ فرصت آخر برای خرید با قیمت بهتر!
https://l.memarket.me/lp/65/180124</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/685467" target="_blank">📅 02:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685462">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b634dd076e.mp4?token=b6bgJoAEyqPlWekne7ZlqsQzHFCjjZLrufS1_eDYpP5DFgsyU8R89W9zbGMFPw3AEMJFbMSoRNVfyDIVwQOdjQ-Q54wIW5s7O5umX-2qlvIy5QDhoGXPSN55BVHWgwynpejpONt7CwU8THlPOItsNxM0tDgk8EA8E9ZkjqAgahuR_JShEsnNFZcUmK2GFcLxFtkbczllgdAUkU8gcREvXxhD7wKqIsubSHbt9lUzPuFwohS1tr-XlOMm-pEn84fY7k_51XPs67YoMhrYjTWkbS7j86Y8gIUsYgLu4AzDpZVeYfiHaTiGXFI9tczQJv1l5aN1yXfPngWdPa57l4g1Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b634dd076e.mp4?token=b6bgJoAEyqPlWekne7ZlqsQzHFCjjZLrufS1_eDYpP5DFgsyU8R89W9zbGMFPw3AEMJFbMSoRNVfyDIVwQOdjQ-Q54wIW5s7O5umX-2qlvIy5QDhoGXPSN55BVHWgwynpejpONt7CwU8THlPOItsNxM0tDgk8EA8E9ZkjqAgahuR_JShEsnNFZcUmK2GFcLxFtkbczllgdAUkU8gcREvXxhD7wKqIsubSHbt9lUzPuFwohS1tr-XlOMm-pEn84fY7k_51XPs67YoMhrYjTWkbS7j86Y8gIUsYgLu4AzDpZVeYfiHaTiGXFI9tczQJv1l5aN1yXfPngWdPa57l4g1Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نماینده سابق کنگره آمریکا: ترامپ باید از والدین دانش آموزان مدرسه میناب عذرخواهی کند
🔹
ترامپ باید از من عذر بخواهد.
🔹
باید از آن خبرنگاری عذر بخواهد که صدایش کرد «خوک».
🔹
باید از آمریکا عذر بخواهد که وعده‌های انتخاباتی‌اش را زیر پا گذاشت.
🔹
باید از پدر و مادرهایی عذر بخواهد که روی مدرسه‌شان در ایران بمب ریخت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/akhbarefori/685462" target="_blank">📅 01:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685461">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
امارات گوش به حرف آمریکا؛ بازرسی از بانک مصری کلید خورد
🔹
بانک مرکزی امارات فقط ۹ ساعت پس از اقدام آمریکا در تحریم یک بانک مصری، از آغاز بازرسی از فعالیت شعبه بانک مصر در این کشور خبر داد.
🔹
وزارت خزانه‌داری آمریکا پیشتر مدعی شده شعبه امارات بانک مصر از ژانویه ۲۰۲۴ تا ژوئن ۲۰۲۶ حدود ۱.۸ میلیارد دلار تراکنش برای ۱۰۳ شرکت پردازش کرده که احتمال ارتباط آن‌ها با شبکه‌های مالی ایران وجود دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/akhbarefori/685461" target="_blank">📅 01:15 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685456">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54cb7f1f24.mp4?token=pIo2M1dRtYtYKG6VLge_l9f1p4030CX6YyWeAdlA3uHHfv9oqYnuO3WMJEJ5BSN-ddlxlG7N2GmD3ufDy4eKHop5MqgS5YnGrjaeMgmzuPdYvD8xzphR48SWTxrq35gS2hmacf6hgKcNwseS2CW2WeeesAHhtccGSyNKP_yONQ7hNcn3Sgwy6bxnddVF2uIPx-E9Ozla0rHOYGS1NtxIo8SZoVyUply2uwD0AMrqsnYq0D_dExjrZNERltA9UAEDXZsaGtRy3hzbZhxvzzNXt6mhiUhK6CrYuk43IomBeZfdVvJ4TQxvf72AdQFQMI6ZabRgrs878KNfPudOwruuIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54cb7f1f24.mp4?token=pIo2M1dRtYtYKG6VLge_l9f1p4030CX6YyWeAdlA3uHHfv9oqYnuO3WMJEJ5BSN-ddlxlG7N2GmD3ufDy4eKHop5MqgS5YnGrjaeMgmzuPdYvD8xzphR48SWTxrq35gS2hmacf6hgKcNwseS2CW2WeeesAHhtccGSyNKP_yONQ7hNcn3Sgwy6bxnddVF2uIPx-E9Ozla0rHOYGS1NtxIo8SZoVyUply2uwD0AMrqsnYq0D_dExjrZNERltA9UAEDXZsaGtRy3hzbZhxvzzNXt6mhiUhK6CrYuk43IomBeZfdVvJ4TQxvf72AdQFQMI6ZabRgrs878KNfPudOwruuIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نحوه عملکرد برف‌پاک‌کن‌های خودرو: توضیحی ساده از مکانیزم آن
#موشکافی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/akhbarefori/685456" target="_blank">📅 00:24 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685453">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقرار مداحی</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ای نخ عبات رشته نجات</div>
  <div class="tg-doc-extra">حاج محمود کریمی</div>
</div>
<a href="https://t.me/akhbarefori/685453" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✨️
ای نخ عبات رشته نجات
ای یم نگاهت معنی حیات
ای دم و صدات صدای قلب کائنات
🎙
حاج
#محمود_کریمی
میلاد
#حضرت_محمد
(ع)
💚
مرجع رسمی مولودی و مداحی
👇🏻
👇🏻
@gharar_madahi</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/akhbarefori/685453" target="_blank">📅 00:16 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685449">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da12c27796.mp4?token=hU1lPfudrwQc78WZ32ymBGDkWFMlMSFiHJIL40_2ec9m7G6o2P7N6csV3LHDth7H8551CdgWJKlB6fkpkxc5dybtyqsl-kOJPgo5I4wwO4edfRp7DKhmx5s5JDdrRrSUxqYitT1MDC5O1DYZ2v3KMyk3KMQbO8E19DI7tMSRvpLOQLNf6r8wov-C4UaUt7YB9pOU4uoxZOz8ui0EHlWEWYiwZntv-QNCv8ip1WOFtY1wpE7EwS2dxyltx_kRH_a6OtwEjcb3VnC2gpaRE74yEFpVkdgTe3P79rfATzpFpZ8HzjkWqJ0jC-8-UH6t3_EdrZnYdaGw9PcVxiFaygizGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da12c27796.mp4?token=hU1lPfudrwQc78WZ32ymBGDkWFMlMSFiHJIL40_2ec9m7G6o2P7N6csV3LHDth7H8551CdgWJKlB6fkpkxc5dybtyqsl-kOJPgo5I4wwO4edfRp7DKhmx5s5JDdrRrSUxqYitT1MDC5O1DYZ2v3KMyk3KMQbO8E19DI7tMSRvpLOQLNf6r8wov-C4UaUt7YB9pOU4uoxZOz8ui0EHlWEWYiwZntv-QNCv8ip1WOFtY1wpE7EwS2dxyltx_kRH_a6OtwEjcb3VnC2gpaRE74yEFpVkdgTe3P79rfATzpFpZ8HzjkWqJ0jC-8-UH6t3_EdrZnYdaGw9PcVxiFaygizGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیو‌هایی که در روزهای اخیر از مسابقات تنیس در باشگاه انقلاب در فضای مجازی پر بازدید شده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/akhbarefori/685449" target="_blank">📅 00:13 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685448">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTtd5fpmscmqh8Qt2whaHjfi2DHRekrK2CmFFStEUvTw8Xvc6lUdNVR_BGGpauRa0n6SAhgDgIakN5fu5IGMruNVpZXsPDb8VczfU5KJ2nA73qn1NBgSy16zsjOmCrr6lZmp-YO8YAbZWmFtvatJ9W2II8IlFwYBM1J2OD31i6wcN6QAPVhwr5v0DWN_oulrvgCK6mkK7mIHK6EfFP5nNdFoTqW0qXwyBxmADkypBMQ3q2iE_OgDgIWk59hoBM3_dk-R8UNrzpFxWStclOJaERmmo2o_e-xySeG0AeudAE8jJQEviJi2MoMaXmOcHPG-nsTsDk8cXnTohbVP8Tnf6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش‌ها به پیام محسن نامجو به همسرش | آیا او به همسرش نگفته بود به ایران می‌رود؟ | نامجو یک هفته پیش از بازگشت ناپدید شده بود!
🔹
بازگشت ناگهانی محسن نامجو، خواننده و آهنگساز سرشناس به ایران پس از نزدیک به دو دهه مهاجرت، به یکی از داغ‌ترین سرخط‌های خبری و رسانه‌ای تبدیل شده است.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3241385</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/akhbarefori/685448" target="_blank">📅 00:10 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685447">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
هشدار احتمال وقوع سیل در شش استان کشور
🔹
سخنگوی سازمان مدیریت بحران کشور نسبت به احتمال وقوع سیل و آبگرفتگی معابر در شش استان کشور هشدار داد.
🔹
احتمال وقوع سیلاب و آبگرفتگی در استان های آذربایجان شرقی، آذربایجان غربی، اردبیل، گیلان و ارتفاعات شمالی استان های کردستان و زنجان طی روزهای یکشنبه و دوشنبه وجود دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/akhbarefori/685447" target="_blank">📅 00:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685445">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9rM-aMf53MqavxpSFsZhvbh7JEBqVccOlUmsfw_QzmfQ9_bafVEwO4fEGbO7N0Reuqe-mk2upyLXUMhy8BWib6Fjjycn40Wegmu930Pxz_JO1rO_xsoZenc8x_89J7XOEABjx2W9VC6wnPrPMJ6S3uuQmJtepZlPpz3wD3QRpSUGkky-QUv-bncxn_O2WI0yAwmGeMj1UaSgrBhwgU13s0hYEZUIrq64b2eVsUi5LHlmsn-GWREKWWCysr9ois6kFM4fNRGqsUaRasHJdme1eaQPRDJC1_C6aqzw5HXMjB3rkhbmZjvFYUl1Fw-yu-OK30oMEfMEPxdRQrq87fwWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/685445" target="_blank">📅 00:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685444">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقرار مداحی</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نماهنگ هله یا ایها النبی</div>
  <div class="tg-doc-extra">حنیف طاهری</div>
</div>
<a href="https://t.me/akhbarefori/685444" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✨️
تو معجزه ات قرآنه ولی
معجزه کردی با برادرت علی
اومدی که به همه بگی
ناد علی ناد علی سینجلی
🎙
#حنیف_طاهری
میلاد
#حضرت_محمد
(ع)
مرجع رسمی مولودی و مداحی
👇🏻
👇🏻
@gharar_madahi</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/akhbarefori/685444" target="_blank">📅 23:49 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685440">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
اصلاح سهمیه‌های کنکور به امسال نمی‌رسد
وزیر علوم:
🔹
اصلاح سهمیه‌های پذیرش دانشجو که از مهر ۱۴۰۳ در دستور کار دولت قرار گرفته، در کنکور ۱۴۰۵ اجرا نخواهد شد.
🔹
در نظام پذیرش دانشجو بیش از ۳۰ نوع سهمیه وجود دارد و طبق اعلام مشاور عالی وزیر بهداشت، در برخی سال‌ها سهمیه‌ای‌ها بیش از ۶۰ درصد پذیرفته‌شدگان را تشکیل داده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/akhbarefori/685440" target="_blank">📅 23:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685439">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1340f65a8.mp4?token=Rj52YmYdJPiA9bPMJF_Toe9h3RQr9i5HXi2xjoBmK0jyK68pHjFZiZHaz_1QTjVx5sIy7oUT15gXYJP20mWyJYvr35h-xLp5lDoDN24_UrFRn15NKT8B7E5F81V-WmILtTXjulGgmASkbRlVbqmwqKTRr5bZjLJQD0M8ecsUOsfADxMDHEz6KP1WI9jPJ2c6I5g3kuyRq2BDDULaJg4TywMnN37K1f6jqF1qjN3R5SJNubWfeytlFXe49bl4IzJU1D4bNcRLbSdVlkVkeLzsFfXpwlsNiGXxxFdXlVJnNDdc3vqCPR2W3pJJqg353lLK5fTQHA0Ex7tEzrEdK-kYzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1340f65a8.mp4?token=Rj52YmYdJPiA9bPMJF_Toe9h3RQr9i5HXi2xjoBmK0jyK68pHjFZiZHaz_1QTjVx5sIy7oUT15gXYJP20mWyJYvr35h-xLp5lDoDN24_UrFRn15NKT8B7E5F81V-WmILtTXjulGgmASkbRlVbqmwqKTRr5bZjLJQD0M8ecsUOsfADxMDHEz6KP1WI9jPJ2c6I5g3kuyRq2BDDULaJg4TywMnN37K1f6jqF1qjN3R5SJNubWfeytlFXe49bl4IzJU1D4bNcRLbSdVlkVkeLzsFfXpwlsNiGXxxFdXlVJnNDdc3vqCPR2W3pJJqg353lLK5fTQHA0Ex7tEzrEdK-kYzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تفسیر حدادعادل از پیام رهبر انقلاب درباره مذاکرات و خطاب به افرادی که قصد دارند مذاکرات را غلط جلوه دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/akhbarefori/685439" target="_blank">📅 23:34 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685438">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f8a45ff7e.mp4?token=sFfORJGC7ga02deNBs1SRiUB7T1qYWHuVzoKZnSUaPSClCP-wg6gOWTP2pqBIcrMeyipRHJ2J5c-N1vOXKbPS9XtxShjBPRrN1Zi3_KTRxzqqgDx-08Fo7GkG-HfhfMnDquklpH22623bMyAFQtzEPzxIL-z-NYBEkaBEWWn6Uwpnyq04Hr4446qgE5627pYEYhtx6VhZHpA5VJwUFQ9meObY-N06CQ7q7nwuj31BhYqKZB-uLIZMD6puG91ti12i3sLtxUFnqPL1LzrteQ85ftFWMzQPpAa-dR_onAdnksCi7oZmxApTmpKFWSN50IA5gWk7ORweGxisMPiaq_ETQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f8a45ff7e.mp4?token=sFfORJGC7ga02deNBs1SRiUB7T1qYWHuVzoKZnSUaPSClCP-wg6gOWTP2pqBIcrMeyipRHJ2J5c-N1vOXKbPS9XtxShjBPRrN1Zi3_KTRxzqqgDx-08Fo7GkG-HfhfMnDquklpH22623bMyAFQtzEPzxIL-z-NYBEkaBEWWn6Uwpnyq04Hr4446qgE5627pYEYhtx6VhZHpA5VJwUFQ9meObY-N06CQ7q7nwuj31BhYqKZB-uLIZMD6puG91ti12i3sLtxUFnqPL1LzrteQ85ftFWMzQPpAa-dR_onAdnksCi7oZmxApTmpKFWSN50IA5gWk7ORweGxisMPiaq_ETQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نجاتگران چینی در مناطق سیل‌زده نپال، هنگام جست‌وجوی بازماندگان گرفتار زیر گل‌ولای ناشی از سیلاب ناگهانی، با فریاد زدن «کسی آنجا هست؟» تلاش می‌کنند نشانه‌ای از افراد مفقود پیدا کنند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/akhbarefori/685438" target="_blank">📅 23:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685437">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b18c117eae.mp4?token=KcKGSbTj_xIrEY_x5tjZd5sYuainFaj6vt5CjEwuBmNLrtfwDbcTPnJYivTTs2fVRIYAtQRT0js-Z8nIln7aLPxoiIqvbBNdoNpkdTUThaPELNtOwRNZ4aFiog5w-XdswyH0Z0nNmJofNz6AKH98-C036XfMeZkanWV_eRwxd0fghOUrd30oGA3z04iIsxW9_mWaEtSrdNJcfO2DzNoYLtzovtfS-OEbpDPkOzAl2lezSgdWXu3qdmBRjWI66Bq0D75JXB2gqL6IHBinDz2Yobt8odTvwx57LF5GZVj_prUDllWlh17XJe8Zyfb-rTbfKQyAuwdAxLZBC_RKhYgDEIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b18c117eae.mp4?token=KcKGSbTj_xIrEY_x5tjZd5sYuainFaj6vt5CjEwuBmNLrtfwDbcTPnJYivTTs2fVRIYAtQRT0js-Z8nIln7aLPxoiIqvbBNdoNpkdTUThaPELNtOwRNZ4aFiog5w-XdswyH0Z0nNmJofNz6AKH98-C036XfMeZkanWV_eRwxd0fghOUrd30oGA3z04iIsxW9_mWaEtSrdNJcfO2DzNoYLtzovtfS-OEbpDPkOzAl2lezSgdWXu3qdmBRjWI66Bq0D75JXB2gqL6IHBinDz2Yobt8odTvwx57LF5GZVj_prUDllWlh17XJe8Zyfb-rTbfKQyAuwdAxLZBC_RKhYgDEIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازیگران فیلم جواهری در قصر در گذر زمان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/685437" target="_blank">📅 23:25 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685428">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TiEHooVdzaBSQd0fSCso0-I6nXwypKiVWDYrVAj8IzDmmvqZBXQv5FXimtsiP5AJxUAxJs1DQt26WupkavlzAx4lrYS4lUfzfuWh55a01r94zeIYuaetxO1M02bT7FM9qN-r5xJ6zcxcNQx358_9dF7HTLObfePCphBVe2CEZIH4hPvfTG1Bs_nIi6MC7jyyp2kngUEUGTaGr-OpLWE7ZutQFu7lT4DD8Sqx1AvqlZ26DY4gMl3ozxPsMGIXDB6GxNKY8UsY_2mX1BGxcevHPSfSEV4TzAGWrSbR-CRlkNQo6f5eY9bJU5dlnJ5UI43mjPsS6dVxbEOwS5o3dILfyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gb_ElnHAYrcs-2B-dSUl9is2tC_CbdUhbtP9U9nt9YCuPveM2nxisV4VrF0OFGxqEBlUNNV05wgKpSMURertFJ3nHyjDnK6qu3dz7SMfPEjAqYAbKXWqQKZ1LrXbVkpeAyDKwQ7u0R1IljZH2-QCZdoq7mU3De9Qv-f4gUaQT6p0XmxckwmnvcrOcFHchllzWwd8N3xBTsoDTGPZptmhv6CZo7WKnPSblkQZQtvL_lg-v5Lf6BYhrPFlMMgqOkA45MuqmiISAzWUmPt2l6ttt1FSwA3N3uE3t4nUNB0uBD3yOYTCnM2bNgbVpdm8362DJypOfwqA_w2-3qexHpPfVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/neWtAqlUxFFshHYgr2dJIJlbERccRdjQLUZrG_C3H56cY6DvkCLFo-sVr_B4bkWN2HShSpL0OXK9K23jRjgzWRl6zlr4BKz7z0XXBO5AhPx-36-cbWWwaLZF1JK8nTspHoIed4jhhvYLuffYtMupBTipc9OPVs1eqg5dwYwLq1exyqAFbKjvlrH8Xkp3bhDzXRHfQoZn8d5OIIVUkIVYyUB6S4ab9ucYyhgSZeQlcjWl2VFeCRL3DdUc2da-OHz-E-fiJJfcRUkNRVg1ykxz5fufriq2VCemCrgDBIP_w94wNMJcmdUc2r13rR5kbDF5vEZmYteYNqGBdqd8ry2CPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HvatyUvAty7bk_1l1GqnhiuYqnobcpA1smsBgeQzvwiO05pOy75qUl3oWQm9jBWDCIILJ03h161G9ja_YAMfuSs3GYVimiZAnLMCQkPRjn7FCZi1NuPnSW1YGILOxPQf5diczC_g4pNDVrUn08TH5jE9vcIalXxTbJIm6lUDiRZLgTe5RQpUVh8k13uLZHDCgwbrM6JpWWKOraBj7TD8QcA6AaU3uYds-PaggU-dZmS7ZE7CqieGPQO_IytECgQzifJjCNJdjb9HdMzC7V3G0uvoBdGHukB61Pjg3kxOtZQus4OkURbYhAPSirEp5Inz8HC2cZNmuJFj2HS552WPuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KNElhP2g2V_w9YYq9eImPG48Xo7fth_S28J_K2vbspxnlhIBbtRIBQRiy8tH-E_NPb4mUnRa_-qUZJJARWox7hwZDPg0bWHsDaq7tBagQr4LWzMSTnh4FKs2YwxdECYRs_VifTJjccLqwsrshggnCIucgq0EobrQYHLkFhoQa4UaB_VtyECd3XvLY83ZIHHC80TEwGVQqPijkXAjKzEAmBSHgfY8lyGU8O8J2gAWzIGkVB6BOiPDPTrjIynewYJWkp39RurUlZAfhfeMzfAzQEa5dwmQmAYVzghZttT3ZhCWTL_HmRY2ptpfY8avSabKk3dVNfdJVnbzL-0HtV4pTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LRBL1ivHtYHw6-pLCzpHJ-925nBG4lex3aQgcRf4gekIErUldRe3bvrdI-Y23ZKqGR1I2JMqBwh2ZAKxgG9TyaByHDLyJyeA5eXIxG1ucWQIv_4wYmiedKDHPS0qb-iZg60GMrnENRGO-QF4HZHnuqKqUvWa0FPR0HgQN2ScfvPp4jdtGIlNxcAz0kKvbeM26uRIXL4HW7qrGGsx7U85jlJbW8qZSLP1tiBxnzrE7nRtkw4D8mnnRYyklcm_lgoR2jk5TGJrza7v7jjlECzo2Ew0aacslboHTs3hY4d9d2WT-PApw-89TabFbnROoT_kys-7JpyvvbTH74roe3iYlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nwP36kFLX0HxYDqgEdGKYQVrwF_KoTJUf-EbfFh3IoTUDKNZjGl-eSD5APMzS-osp4nkhJs4jFfsHKiSa2fCxT7UZM4AgSbb-gKtZBBs0EMrkQGOtNvMHg2urQSaejtGPWmfQu8-LaH3wiUmYOcZsSwWVSFxKoQOD9_Mm6tHUW1fXVFadg2YebZ7NyZU2yiQqgPxWI3TI8B7h2Ri6sWnwAAFwjM0DIilA93dCX2w37GsMTaJc8vurxTGaaQ1Awu7XAzGNX1huyTonDelW4MltoH97PYjWZu-3okopreMHtB0GoJ1ywrKMEk1D338y7tolo-hM3wQtCG71PRBViCaGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cad3UB_TO-4C4ZOzhyEgLcJqT9mKOkPlbBIfDLh8Dc_JGk5w9LHQ1D0SpEVOiwybpIIEA72d_o1oo22sRA0QBAfI-7DGnHfn66P9kAAYqbNeDSJj6CW24sPWPRiQ0wt-xP-sq7gU2mtejEZ-h7eeBHma3Q4VQci_43KBg_viYHfimBZQVa-0gyk6jayz9tGg80Q0o7T5_EGzwc2Rzozyw9c4dTWIu0sDG6-AMkJ-YGinkJqd3w-gAom0JHihwe9YW6pDrdql3X9s7Ot2ymIbewnDHeFmr7CUP5n4aMgYChztuftypEzYht34RffRgH5168DQGPORLk59ndfkiXluNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FDVJ81Y3C1LUHCE2cMtX-X_e9uJ9ldsiVvuJCy2vkhmWRXzDqMO26SIcMNLmag7GZikpcfZBR1t8NHSR-nJpvKcL8EU7SGFEcRRihL6tVh25WjL5OQB8noGcZrS4zS3uCD9-oCuilgrJu90ZxFnnKeJ_Fsys14w_CpMofahxcgG8oXjacT0YGnrmymHwHWkjVKBTobwMyOvDCziIFgRKuGATx_4y7YifEMjI1ixnStUFVRNiZ3r7h0zbDq4nXV6Ikh71FYwnk5pjScWPjGBL0Ahllco5k3zpII2cw_F-aDicnz8rggEwpONcTNoy0qdHTEhV7Tsy9fy1KKa9OPuLzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
درد دارو
🔹
روایت بیماران از بحران تهیه دارو؛ سرگردانی در شهر برای یافتن نسخه‌هایی که بی‌پاسخ مانده‌اند.
🔸
الوفوری را دنبال کنید
👇
#درد_دارو
@Alo_fori</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/akhbarefori/685428" target="_blank">📅 23:25 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685426">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🌹
دسترسی آسان به فایل‌های تصویری برنامه "زندگی پس از زندگی"
داستان افرادی که از مرگ برگشتند
#فصل_پنجم
🔹
اول
🔹
دوم
🔹
سوم
🔹
چهارم
🔹
پنجم
🔹
ششم
🔹
هفتم
🔹
هشتم
🔹
نهم
🔹
دهم
🔹
یازدهم
🔹
دوازدهم
🔹
سیزدهم
🔹
چهاردهم
🔹
پانزدهم
🔹
شانزدهم
🔹
هفدهم
🔹
هجدهم
🔹
نوزدهم
🔹
بیستم
🔹
بیست‌و‌یکم
🔹
بیست‌و‌دوم
🔹
بیست‌وچهارم
🔹
بیست‌و‌پنجم
🔹
بیست‌وششم
🔹
بیست‌وهفتم
🔹
بیست‌وهشتم
🔹
بیست‌ونهم
🔹
سی‌ام
🔹
سی‌ویکم
🔹
سی‌ودوم
#زندگی_پس_از_زندگی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/685426" target="_blank">📅 23:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685424">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01cc087fc5.mp4?token=nlFPlEprMQB0MPBJCAPzzc95fklFAKco4o_skLhrq-t9U3Ra-eNEnWkSJ4eA8sQ_jSHNT9yg8itx3c0ziYBO5fGvSy9PtSmWpdrt_u2UrTr06qDAUhG1HIfPt-aTA6JivdhYH_4fzVbwm5m0TA-3DaCA3iLez2fxo1ucgH9pVvL_MMMAJApCqhKz3I8_aHOnJplCBTf1O3Gg0IBszBpTJe3AhAkgScwBjlHkkQ68snhIsnWzRG7MNzJBWSz2GO3i7z4REZ4BHiXr_M_w-mxnfFQbIvd0Mz2zfAEAk0vhG1CuBDVYVg-lqL3bk9MD8T8gdNg5-O3zsksoaXEbwbRgRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01cc087fc5.mp4?token=nlFPlEprMQB0MPBJCAPzzc95fklFAKco4o_skLhrq-t9U3Ra-eNEnWkSJ4eA8sQ_jSHNT9yg8itx3c0ziYBO5fGvSy9PtSmWpdrt_u2UrTr06qDAUhG1HIfPt-aTA6JivdhYH_4fzVbwm5m0TA-3DaCA3iLez2fxo1ucgH9pVvL_MMMAJApCqhKz3I8_aHOnJplCBTf1O3Gg0IBszBpTJe3AhAkgScwBjlHkkQ68snhIsnWzRG7MNzJBWSz2GO3i7z4REZ4BHiXr_M_w-mxnfFQbIvd0Mz2zfAEAk0vhG1CuBDVYVg-lqL3bk9MD8T8gdNg5-O3zsksoaXEbwbRgRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گوشی‌ای که براى خيلی‌ها، اولين تجربه استفاده از گوشی هوشمند بود
🔹
گوشى Samsung Galaxy Gio از مدل‌های اقتصادی سامسونگ در اوايل دهه ۲۰۱۰ بود.
🔹
اين مدل براى خيلی‌ها يكى از اولين تجربه‌هاى استفاده از گوشی هوشمند محسوب می‌شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/685424" target="_blank">📅 23:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685419">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135e761d0d.mp4?token=u0Vn04oD_pkzj_NTi1n0ayQlVyGNtiHUnClTqdxrMBaaP80NVHjC18mYJm9nUODCRDv6bglixbaZ3mWYnxVfLaDn8aTH0z-JC_t6qTXUpcolYpFRppva97PfaZSDrVXqiuHopbrXvM-U0OWHWApddshQivsg3DUqIREmCbd7l_VGL_Db6N5fqsz0WNz7vVx4TSeTcXG_hiZGOC_PTMOkIOwRKKV9m6HGIJRlcWjeOKGEa8jxW-9wgRMBesskrl4QyCp8_a3nGkWS57cDg2FfuDzi9KB6IdKMBkv4ywK_9cHBHtQxw3W_p-OIgsDIHiJ4rbCYUbCsomowYx6U7gUWmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135e761d0d.mp4?token=u0Vn04oD_pkzj_NTi1n0ayQlVyGNtiHUnClTqdxrMBaaP80NVHjC18mYJm9nUODCRDv6bglixbaZ3mWYnxVfLaDn8aTH0z-JC_t6qTXUpcolYpFRppva97PfaZSDrVXqiuHopbrXvM-U0OWHWApddshQivsg3DUqIREmCbd7l_VGL_Db6N5fqsz0WNz7vVx4TSeTcXG_hiZGOC_PTMOkIOwRKKV9m6HGIJRlcWjeOKGEa8jxW-9wgRMBesskrl4QyCp8_a3nGkWS57cDg2FfuDzi9KB6IdKMBkv4ywK_9cHBHtQxw3W_p-OIgsDIHiJ4rbCYUbCsomowYx6U7gUWmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨️
هزار طایفه آمد و هزار مکتب رفت
و ماند شیعه که قال الامام صادق(ع) داشت
#پک_استوری
ویژه ولادت امام صادق (ع)
💚
@Heyate_gharar</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/685419" target="_blank">📅 23:12 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685410">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pyftUbFW6ZoCU3RFfXR6cV510Iy6gldotvdcvvipmmIjNgnMC0f78gI6wacyV06rihtBrsQPPqvfqQajB5waJqfotZvCHUdTPpDUkR2sEd3QNxyYFZIFz5nIOySu51YqwWNP54fAFd3Qks92rW9VF6k63v1ycsZ85xbUxD6KBooi3OCSBygIzws-QGFYbvAZ-arUF7J7BX3bkQs22QTXoNpGB5IMTVfxH_uj64GeP-fVDZKvW8Ti4jchnWYiYJzSAhDyzpIfg4jYAAUN94-bD_HOU0dSoM-3IZy6T-1NvexAaLQOnQP07jJeTLKlQ1fhqhcAebygJQvFrw5yjLiDEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jp7eIDQ7VY41GRTwkpMkhXwiyhctiIW79C_ZAEUvZHtQnjZckTQZL6QjSFyeErDJZdD4yr5sAq0B1SPKqZZ7QlJD5J-iSMU5eWmLVQ2nJScp4m9Nr18AUI76nWYF1sO2Xs0E-RDyPPWfZmDPAXOvBfE9slGlpSdy8y_obigBC7l0gLu6QSYTXX_MqU2eTAaQbCnPDAEkdZi6ZhacE6H62Zfe0W3W1EGwP0h-sYQGpca0TaqXjwqzE-y7-6HS7qD_yf4v-9kOG3tu-zNXawmuPF6fHgZNuxGFJBadtANOn7XvbGrMjAXklkaws6wWl1UlUYGgRMaRIAgo_BDAEW7a4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U5dTMTenLhSmVEbHuwxTLi4SVzKV4o8mhBx15lFlqWD_5UI09wpcRci_1QtjHsYvTPWTSYp3hbrxn79fuZG2HhEMBRog6ANo-YCqkEarWw3VvN8vIC6-adsVZaP4LZSQmKVFOcLxpX7ySOBOSL9tNnfK892PbbnROLmjLfqJuaLhwJjt1hppNWGXMSCJczi9OyKSPzfMEaeOsDhreQlbAoLPtv_6IQeE1sl07Nnx4XMVkDnqsYYKkpWG0Gof0GNOkGArOOoEA7X61RSAOEPFsLIU5Pw50CriMcEhfpGieYTg4kzLXfsxdEWdQMiwkpd6DTz_CVcA1b0kD6BHt-xVNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ep4T7v8qIbsOtc-yQCEo-LWF8-LpE9vdMufB9Ol_IpHc3oEu6qU9IRyeZuODty5S6QyLjvRII4fJiYIz1U870l23Bg3Cf4KYzdzjaOjg31Nouaif1Ti6SMfF-mRIKejPzh2zZVkustox5D7Xz-eHfj9klwpGH2IH7oLWsVhfWydT_ucn4nA_D9Qo7Qxu0QjIrfc52yn4g1gzQ4HjYVfgBbEA1thwpIKMhUetuK6GEHz6XNsZAKtonD-oFI9e5sUlFppUlUoCo4HNsLejSecnqbJ27wgAHk3nXsC4NnusbQiyLGXvHcSGyjb9MXTSO1bgzlcJKbsT4lTmqKZtW937Iw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨️
دوای درد دین و درد دنیا ، درد بی دردی
حضورت دردهای مرگ را حتی طبابت کرد
▫️
#والپیپر
به مناسبت میلاد حضرت محمد (ص)
💚
دریافت فایل تصاویر
👇🏻
👇🏻
@Heyate_gharar</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/685410" target="_blank">📅 22:46 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685408">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55c81e867b.mp4?token=tLB6gWNIb6L8w5YjUVJlk_AHHfo56MxMl7MgDUFp7IWF4cyzcdChr5N7ccG_hQ1Yv8oyjcK1rBMdwVpJ8eKObFFyhTXutMY5lv6TP0pbLUioGkfKeoJ0a4s52PJWIcbSq171Vw7lxFIi2M5lQyciKXZhOGjaf1peDB3CmaAGe0_FR9QxEJkNro2lcodAmRwWJDamVIJOsFum_BDfifKlI8XTx4LaeEsiWD6Z8V1MSU7PzDWis_Pxj2X-5e21FeoJAj-ahGKIz4ICsFdstlMFxiUf_10AiVHEDHpHDKKDLQUnoafOQsgSE-FoJfuAQkA8o39bvAP0EBX7agX8t07R3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55c81e867b.mp4?token=tLB6gWNIb6L8w5YjUVJlk_AHHfo56MxMl7MgDUFp7IWF4cyzcdChr5N7ccG_hQ1Yv8oyjcK1rBMdwVpJ8eKObFFyhTXutMY5lv6TP0pbLUioGkfKeoJ0a4s52PJWIcbSq171Vw7lxFIi2M5lQyciKXZhOGjaf1peDB3CmaAGe0_FR9QxEJkNro2lcodAmRwWJDamVIJOsFum_BDfifKlI8XTx4LaeEsiWD6Z8V1MSU7PzDWis_Pxj2X-5e21FeoJAj-ahGKIz4ICsFdstlMFxiUf_10AiVHEDHpHDKKDLQUnoafOQsgSE-FoJfuAQkA8o39bvAP0EBX7agX8t07R3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی عجیب از درگیری چند دختر باهم؛ گفته شده این درگیری مربوط به دعوا برای یک پسر بوده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/685408" target="_blank">📅 22:42 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685407">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
پشت پرده گرانی‌ کالاها با وجود افزایش تولیدات در کشور، چیست؟
وزیر جهاد کشاورزی:
🔹
هیچ مرغ آلوده‌ای در کشور توزیع  نشده است
🔹
اقدامات ترامپ و جنگ با ایران سبب افزایش قیمت جهانی برخی کالاها شده است و در این میان برای ایران آنچه که بیشتر از سایر کشورها افزایش یافته است، قیمت حمل و نقل است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/685407" target="_blank">📅 22:40 · 07 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
