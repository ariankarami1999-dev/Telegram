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
<img src="https://cdn4.telesco.pe/file/gHuhhFvElCmFI3oXmlrBWIu1kW3QhjIVPMp1163IrJC7PqYJhxWDgC_GIVKGsb3DMWX_3ZfD799Ayy0heRIj1MoU-JU_hHjuOhtqo722i9zat0876Y-t4Xn_b-aD-WGlN_SYkmwk2XmfW8Ih65tARgOO1jl4AXbygJyFPY50AO82hIMMNjyS0I8rH7Z0T6-CT-mby6JEoHYQ73IbtC7MTUL0Nfa-YDLfCTiMzCcBfwiORkP86pKEZ4Y0iimLsBQTnhibrAdYesHqjaYZ8Z8qLQ4ihPVkX7Ynx96HVyvgWJANG7cg2y9Tq2EE2h3KdvpkhCpSi8y6DYthW_LoSi1sBg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.1K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 15:23:01</div>
<hr>

<div class="tg-post" id="msg-17308">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">وزیر امور خارجه ترکیه از ایران و ایالات متحده خواست تا حملات تازه را متوقف کرده و به مذاکرات بازگردند.</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/SBoxxx/17308" target="_blank">📅 14:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17307">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">شرایط جوری شده که اسرائیل عرب های لبنان را می زند و ما هم در پاسخ عرب های کویت را می زنیم که در حین آن هندی ها کشته می شوند</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/SBoxxx/17307" target="_blank">📅 14:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17306">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">شرایط جوری شده که اسرائیل عرب های لبنان را می زند و ما هم در پاسخ عرب های کویت را می زنیم که در حین آن هندی ها کشته می شوند</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/SBoxxx/17306" target="_blank">📅 13:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17305">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">حمله آمریکایی ها به 3 کشتی هندی دیگر!</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/SBoxxx/17305" target="_blank">📅 13:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17304">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">در این نشست گفته بودم که جنگ بعدی در سوریه میان اسراییل و ترکیه خواهدبود.</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/SBoxxx/17304" target="_blank">📅 13:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17303">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پایان جمهوری ترکیه.pdf</div>
  <div class="tg-doc-extra">236.3 KB</div>
</div>
<a href="https://t.me/SBoxxx/17303" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">وزیر دفاع اسراییل:  به وزیر کشور ترکیه که تهدید می‌کند و رویای حکومت بر اورشلیم را در سر می‌پروراند - این را می‌گویم: اورشلیم قسطنطنیه نیست، و کشور اسرائیل امپراتوری صلیبی در حال فروپاشی نیست، بلکه کشوری قوی و مصمم است که توانایی خود را در دفاع از خود در برابر…</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/SBoxxx/17303" target="_blank">📅 13:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17302">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">دلار خرید دارد همینجا با تارگت ۲۴۰ الی ۲۶۰ هزار تومان</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SBoxxx/17302" target="_blank">📅 13:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17301">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🇺🇸امریکانا🇺🇸</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4d7ae260d.mp4?token=GCqEyrQl_RlL1MxTak2IeDPlERn6y4bZc8iBYyUeOHaTGfeSeam-mB1YBrS1EXWFKftGBBfWtylD6K6RAKFg15pP37o4DXiNkeYbbhxeU0AoJ63Fd6Fuw67qFIsKpn5P3wF_rdSSjmvzQ0RMjjxTbs1lgeSb9Qnw3Bz6nr010zrYnjYCVFGyh3qBRPaaTAACiwHh6CWhs-p8aalqYxWkwI-9uCjy0JWfOgCHURpyX-sp4ipWhJi4vY5P9TsBbN7koUYTMCyYuWIft1xzZnWY1n5IY2KZH--4Rxq__FlfCXeUscNn9Kv1QFi0mUo08P2dxI59DgeSRFI4P_hN7LSnQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4d7ae260d.mp4?token=GCqEyrQl_RlL1MxTak2IeDPlERn6y4bZc8iBYyUeOHaTGfeSeam-mB1YBrS1EXWFKftGBBfWtylD6K6RAKFg15pP37o4DXiNkeYbbhxeU0AoJ63Fd6Fuw67qFIsKpn5P3wF_rdSSjmvzQ0RMjjxTbs1lgeSb9Qnw3Bz6nr010zrYnjYCVFGyh3qBRPaaTAACiwHh6CWhs-p8aalqYxWkwI-9uCjy0JWfOgCHURpyX-sp4ipWhJi4vY5P9TsBbN7koUYTMCyYuWIft1xzZnWY1n5IY2KZH--4Rxq__FlfCXeUscNn9Kv1QFi0mUo08P2dxI59DgeSRFI4P_hN7LSnQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تهدید تلویحی ایران به حمله اتمی / کیث کلوگ، مشاور سابق ترامپ:
«داشتن یک جنگ طولانی مدت، روش جنگی آمریکایی نیست. ما باید به روشی که در جنگ جهانی دوم و جنگ جهانی اول انجام دادیم برگردیم و کار را تمام کنیم، آنها را نابود کنیم.»
🆔
@Americana_ir</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SBoxxx/17301" target="_blank">📅 13:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17300">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سقوط بالگرد پاکستان با 22 کشته!</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/SBoxxx/17300" target="_blank">📅 12:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17299">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سردار فدوی، مشاور فرمانده سپاه: در آستانه پیروزی عظیمی قرار داریم!</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/SBoxxx/17299" target="_blank">📅 12:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17298">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجنگاوران</strong></div>
<div class="tg-text">مقامات ایرانی می‌گویند یک کشتی باری از شهرستان سیریک در هرمزگان، ایران، صبح امروز در دریای عمان توسط «پرتابۀ دشمن آمریکایی» هدف قرار گرفته است.
آنها گفتند این کشتی ۱۵۰ تنی که از خاصب به سمت سیریک در حرکت بود، حدود ۵ مایل از بندر خاصب مورد اصابت قرار گرفت. ۵ خدمه آن توسط کشتی‌های عبوری نجات یافته و به عمان منتقل شدند.</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/SBoxxx/17298" target="_blank">📅 11:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17297">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">چیزی که امروز گفتم این بود که دقت پرتابه های ایران در جنگ اخیر نسبت به جنگ پارسال یا عملیات های وعده صادق-1 و 2  به صورت جهشی افزایش یافته و این یعنی جنگ سختی خواهدبود.  و اتفاقاً همین کار را ترسناک تر می کند چون آمریکایی ها معمولاً وقتی کارشان در جنگ گره…</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/17297" target="_blank">📅 10:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17296">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">این ترحمه مقاله سیمور هارش — روزنامه نگار معروف — است درباره نشت اطلاعاتی مبتنی بر گرایش ترامپ به استفاده از سلاح هسته ای!  دقیقاً در راستای مطالبی که گفته شد.</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SBoxxx/17296" target="_blank">📅 10:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17295">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">چقدر ترامپ جنگ در ایران را تشدید خواهد کرد؟ یک منبع مطلع از کاخ سفید می‌گوید رئیس‌جمهور گزینه هسته‌ای را مطرح کرده است  چهار ماه پس از آغاز یک جنگ هوایی دشوار با ایران، محبوبیت دونالد ترامپ رئیس‌جمهور آمریکا در میان رأی‌دهندگان آمریکایی در حال کاهش است. به…</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SBoxxx/17295" target="_blank">📅 09:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17293">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fRnHR3cgX0lse2cv1WAdPhHf0VGGAW0OAs6JL9hLOoOQnwxSUdRE-tU3KP4gARhoNlmT9qsIk98doADOPfcw8glZ3otWTYIgYq65DqGXo3ccjIIvXYf7_sLeDFpLuI2AaYSJJKAzYE0LNWpwT4tzVXXxuXkTIIXbGlbXcw3aZpx2Q7CGfO0hIWc12mB-wAwNJdoBej8qnpWy2lRO_v5VLdbWQ66YftEAeDc1w3u4-9I2U85co7-MTKNOSZLFmEDChu26KrsRhhpETVPZsag8ozFXtUdHKvOQINfOKvoK7Lp4AxZcLDgVZmKTgW6aLzdDlr0jMQo7dor2a8tc24Jv2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چیزی که امروز گفتم این بود که دقت پرتابه های ایران در جنگ اخیر نسبت به جنگ پارسال یا عملیات های وعده صادق-1 و 2  به صورت جهشی افزایش یافته و این یعنی جنگ سختی خواهدبود.  و اتفاقاً همین کار را ترسناک تر می کند چون آمریکایی ها معمولاً وقتی کارشان در جنگ گره…</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/17293" target="_blank">📅 09:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17292">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دقایقی پیش انفجاری در نزدیکی سفارت آمریکا در بغداد روی داده است.</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/17292" target="_blank">📅 08:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17291">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oD0dGUf39TEaBLDbr-OzacmOxOmBECIUYEX9LqZp8IWUl5zEis4cHEifoOgepn53A_Rr-U0xVnN3cree9jwjvScxktuDZ60jXP7VTrZ9k7LNHfbmKxTZmkx9jmzLSPrGrjLvY5_jj1HJ5C48YiMRKa7VjEXlreaWrEHgpMnIeL3LxeZNCtXctptOCprRwfqsjENgeZWMGWgGFduWcVH7y72NjNAL7XXKXWQZ85F-po-lk4kyMUm1lXuaSdafiOjGn4TAIpnFGbibL4YQAkeRvVx0XAgRcZAYJ40xeii7KngzrLgc3HKjb3qq-BGJj_qSq91f8fOogbNp7dsYCYmAVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هندی ها بدون نام بردن از آمریکا حمله به نفتکش را محکوم کرده اند و گفته اند از ۲۴ سرنشین آن، دقیقا ۰۳ نفرشان گم شده اند!  سبحان الله!</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/17291" target="_blank">📅 08:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17290">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">محل استقرار جنگنده های F35، F15، F16 آمریکایی منهدم شد
سپاه پاسداران انقلاب اسلامی:
مردم مومن و قهرمان ایران که با بیش از صد روز ایستادگی در میدان حماسه آفرینی و نصاب جدیدی از بصیرت و مقاومت را به نمایش گذاشتید؛
به دنبال افتخار آفرینی های سحرگاه رزمندگان اسلام در سرکوب دشمن متجاوز آمریکایی با توکل به خدای متعال، فرزندان دلیر شما در نیروی هوافضای سپاه در پاسخ به حملات موشکی ارتش کودک‌کش امریکا به یک مکان تفریحی، یک مجتمع تولیدی و محوطه یک پادگان از اطراف کرج و نظر آباد و یک پایگاه محلی سپاه در شهرستان پیشوا برای تنبیه متجاوز، صبح امروز با ۱۲ فروند موشک بالستیک محل استقرار جنگنده های F35، F15، F16 آمریکایی و همچنین تاسیسات مهم ارتش تروریستی آمریکا واقع در پایگاه هوایی و مرکز کنترل الازرق را هدف قرار داده و آن تاسیسات و مقدار زیادی از جنگنده‌ها را منهدم کردند. عملیات رزمندگان اسلام تا زمان ادامه شرارت‌های دشمن ادامه دارد.
و ماالنصر الا من عند الله العزیز الحکیم</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/17290" target="_blank">📅 08:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17289">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">— مرکز فرماندهی مرکزی ایالات متحده پایان حملات آمریکا علیه ایران را اعلام کرد.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/17289" target="_blank">📅 04:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17288">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">انفجارهای شدید در بحرین</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/17288" target="_blank">📅 04:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17287">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">فرماندار اشتهارد:
صداهای انفجار احتمالا مربوط به انفجارها در خارج از استان از جمله ملارد تهران است.</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/17287" target="_blank">📅 04:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17286">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سردار موسوی:
تنگه مقدس هرمز را ناامن می‌کنید؟! منطقه را برایتان جهنم می‌کنیم</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/17286" target="_blank">📅 04:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17285">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">آیا ایران در صورت حمله آمریکا، کارت برنده هسته‌ای دارد؟
پپه اسکوبار گزارش می‌دهد که اگر ایالات متحده جنگ علیه ایران را از سر بگیرد، جمهوری اسلامی می‌تواند به سرعت برای انفجار یک وسیله هسته‌ای در خاک خود اقدام کند؛ نه به عنوان یک اقدام جنگی، بلکه به عنوان یک نمایش غیرقابل برگشت و مستقل از توانایی کنترل تسلط تشدید تنش.
یک سوال واضح: آیا ایران می‌تواند در صورت لزوم به سرعت یک بمب هسته‌ای بسازد؟
به گفته استاد MIT، تد پاستول، ایران در حال حاضر مواد کافی (۴۵۰ کیلوگرم اورانیوم ۶۵٪) برای تبدیل آن به سوخت درجه تسلیحاتی برای یک بمب هسته‌ای کوچک دارد. و با همین مواد، آنها می‌توانند حداقل ۱۰ بمب از این نوع بسازند - به اندازه‌ای کوچک که روی موشک‌هایی که می‌توانند به اسرائیل برسند، نصب شوند.
چگونه؟ با استفاده از یک ترفند ساده: پیچیدن هسته هسته‌ای در یک "بازتابنده نوترونی" (ساخته شده از اورانیوم ضعیف شده یا سایر فلزات). این کار نوترون‌ها را به هسته بازمی‌گرداند و واکنش را کارآمدتر می‌کند.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/17285" target="_blank">📅 02:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17284">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ایران در حال آماده‌سازی برای انجام یک حمله بزرگ علیه اسرائیل با استفاده از سلاح‌های جدید است.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/17284" target="_blank">📅 02:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17283">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">خب موج اول گویا تمام شده.
به نظرم از جمعه موج اصلی حملات شروع بشود.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/17283" target="_blank">📅 02:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17282">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">بیانیه روابط عمومی سپاه پاسداران انقلاب اسلامی:
پس از نفوذ یک فروند جنگنده اف 16 به حریم هوایی خلیج فارس و شلیک موشک از سوی سامانه پدافند هوایی سپاه پاسداران، هواپیمای مهاجم متواری شد.</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/17282" target="_blank">📅 02:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17281">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">یک کارخانه پتروشیمی متعلق به مجتمع گازی پارس جنوبی احتمالاً در عسلویه هدف قرار گرفته است  هنوز مشخص نیست که آیا دود دیده شده ناشی از سقوط ترکش است یا یک برخورد واقعی.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/17281" target="_blank">📅 02:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17280">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">یمن به آمریکا هشدار داد - درصورت ادامه حملات به ایران سکوت نمی‌کنیم</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/17280" target="_blank">📅 02:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17279">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/17279" target="_blank">📅 02:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17278">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">فاکس نیوز گزارش می‌دهد که اهداف بعدی نیروگاه‌های برق در ایران خواهند بود.</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/17278" target="_blank">📅 01:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17277">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">📡
حسین اژدهایی ؛ خبرنگار ویژه صداوسیما در بندرعباس:  در قشم و چند شهر دیگر صداهایی شبیه انفجار شنیده شده است که هنوز محل آن نامشخص است</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/17277" target="_blank">📅 01:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17276">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34cf9de796.mp4?token=s9Yd12wiCVqOibJqYAs-ZHb4sfTj9iZaLFrREZ1dVJpOdUf25flNgsffwieQmHrWFUHqBrTzj3XPdjTBXnRlWsNlhuZkEBU6EQI_2gdDljpSQnnSOjT88PMJpHP8iSe_3_t2Bx08ypuKQQ229uuP0a8hsj6wiF8rBtcUgeBAbIVfkaHhOxhBtCieczv20UNdxUu_huvi1vfXy79GbbU-C_Xp_-nHfUZ_85ZJKbeV57H7T5ORNY7Ab7EA0EQZS1IFQ5VdEwkibHDknZ-tZj4IvE_frjDIoOCkGi1ySgMyIXWKqWoypC5acrytl7g7mu4YbuqkxO_QOtDrm8Zk6t8b9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34cf9de796.mp4?token=s9Yd12wiCVqOibJqYAs-ZHb4sfTj9iZaLFrREZ1dVJpOdUf25flNgsffwieQmHrWFUHqBrTzj3XPdjTBXnRlWsNlhuZkEBU6EQI_2gdDljpSQnnSOjT88PMJpHP8iSe_3_t2Bx08ypuKQQ229uuP0a8hsj6wiF8rBtcUgeBAbIVfkaHhOxhBtCieczv20UNdxUu_huvi1vfXy79GbbU-C_Xp_-nHfUZ_85ZJKbeV57H7T5ORNY7Ab7EA0EQZS1IFQ5VdEwkibHDknZ-tZj4IvE_frjDIoOCkGi1ySgMyIXWKqWoypC5acrytl7g7mu4YbuqkxO_QOtDrm8Zk6t8b9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این را بفرستید خب</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/17276" target="_blank">📅 01:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17275">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">درگیری‌ها در تنگه هرمز بین سپاه پاسداران و ایالات متحده در حال وقوع است  بر اساس منابع محلی، سپاه پاسداران و نیروی دریایی ایالات متحده به طور فعال در تنگه هرمز درگیر هستند.</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/17275" target="_blank">📅 01:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17274">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">درگیری‌ها در تنگه هرمز بین سپاه پاسداران و ایالات متحده در حال وقوع است
بر اساس منابع محلی، سپاه پاسداران و نیروی دریایی ایالات متحده به طور فعال در تنگه هرمز درگیر هستند.</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/17274" target="_blank">📅 01:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17273">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">مناطق مورد حمله آمریکا</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/17273" target="_blank">📅 01:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17272">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mSjJ5Lw5XmyO3m11ziSntFlNfhQJHUpNfhk5_S9KN9zjB5nD-98qZ3N2hPQUOLVT5B5_ifOw9LIUprC4OcfDWmUICXdP3Zz_Q0j4ttJ2jfn8Qg0ammT0Tbohpghw9xovYAsEqFYwxAjmrd5mgZGCTgMtW-bADL0eBPmWFvMfA_aNyEHAD-NpDKWHH1wXpav6CqhRuajyLvS08T9w021MzPJumY6SiQbbIXWrhxczJrcOpv9yNAbEhka-cmX4e72NqNQIgVX_o6mjMUVsu_DxzgkloVu-l0-Ov6LkryX3zb0a1vgZsx2Luy4d8dKqUruPp2wiwmuQ7b6iANJD4FHwdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مناطق مورد حمله آمریکا</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/17272" target="_blank">📅 01:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17271">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7111d88fe1.mp4?token=aqcgZg6KNQ7w9QZlNVkrNYkZXimyxYG0bzDb2dTH4BQdsj-Gg-Uo6crKk--m_2wl8uXPMywNozvNQbwk3OC2MYlTXkVEh0S2ZTHamVZzVPgBpjiMRKoGRQaU0e8zChOkXjgLsoQsCB-8LfalrW-7lxvjH7jCUyqyD5YNxqcQglmeh7VRJNHGGOCfITQm1ttx7Jkd8Coo0mrmdwDwG6eK3IAP_AwLIedRET9VYDfj4k1a3zF0OCiiOfK79g4aFtEJt7hjcm8IhOHuAeTdneNXZBHkLQ7arMsZm_l2vvcer9DCz14ilt4J3bg222ZdzD_2uxgXDCY88tdJdrKaIRW79Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7111d88fe1.mp4?token=aqcgZg6KNQ7w9QZlNVkrNYkZXimyxYG0bzDb2dTH4BQdsj-Gg-Uo6crKk--m_2wl8uXPMywNozvNQbwk3OC2MYlTXkVEh0S2ZTHamVZzVPgBpjiMRKoGRQaU0e8zChOkXjgLsoQsCB-8LfalrW-7lxvjH7jCUyqyD5YNxqcQglmeh7VRJNHGGOCfITQm1ttx7Jkd8Coo0mrmdwDwG6eK3IAP_AwLIedRET9VYDfj4k1a3zF0OCiiOfK79g4aFtEJt7hjcm8IhOHuAeTdneNXZBHkLQ7arMsZm_l2vvcer9DCz14ilt4J3bg222ZdzD_2uxgXDCY88tdJdrKaIRW79Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💪
صداوسیما جمهوری اسلامی ایران به نقل از ارتش آمریکا ، خبر از تهاجم این ارتش به مواضعی درخاک کشور ایران داد</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/17271" target="_blank">📅 01:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17270">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogPk4uPErGFCgc1i4gXHT7YICZeZB5RKHN_dduip6sXdVNkUblOcLSZ2itOP4Mt3fPzeEL4nT5Hq_pXBC-tSnlSaYTrxwC8cceC6kN3Bfo6y-xgbTiCxBIZ4-OdDU-3PQ2xQRFIXYPIZHS6NAgzku_OdkW16JfLyD5VhBm4IGAU4p8h8RDQXVrI2ctY9g7fpjhzzs_RsmuRRopnT7XdR0ac9vuAaHLaAOxV_ZTlPq4v5YOfiNtpZx86kflrOs_4E9sZBFS93GTSDFP3nZZGtPR7OFRMN41n6G-52GZ85D_MlqFk6xcBCRtaqukrwCLZ0yr9JmXI0ez7u1X50ms-srw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💪
صداوسیما جمهوری اسلامی ایران به نقل از ارتش آمریکا ، خبر از تهاجم این ارتش به مواضعی درخاک کشور ایران داد</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/17270" target="_blank">📅 01:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17269">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">یک مقام آمریکایی می‌گوید حملات به جنوب ایران شامل «صدها هدف» خواهد بود و به مدت ساعت‌ها ادامه خواهد داشت</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/17269" target="_blank">📅 01:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17268">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">به نظرم میخواهند بگویند راه مذاکره (تسلیم) باز است و در ضمن به کنگره هم بگویند که اینها حمله نیست بلکه دفاع از خود است.</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/17268" target="_blank">📅 01:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17267">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">یک اصطکاک ریزی بین آمریکایی ها و اسرائیلی ها قابل مشاهده است که به نظر بعد از لو رفتن قضیه جاسوسی اسرائیل از سیستم اطلاعات نظامی آمریکا ایجاد شده.  اما به نظرم موقت است و راهبردی نیست.</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/17267" target="_blank">📅 01:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17266">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">یک کارخانه پتروشیمی متعلق به مجتمع گازی پارس جنوبی احتمالاً در عسلویه هدف قرار گرفته است
هنوز مشخص نیست که آیا دود دیده شده ناشی از سقوط ترکش است یا یک برخورد واقعی.</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/17266" target="_blank">📅 01:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17265">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">صدای انفجار از بندرعباس</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/17265" target="_blank">📅 01:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17264">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">حمله دفاعی دیگر چه صیغه ای است؟!</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/17264" target="_blank">📅 01:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17263">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">نیروهای فرماندهی مرکزی ایالات متحده امروز ساعت ۵:۱۵ بعد از ظهر به وقت شرقی، با دستور فرمانده کل قوا، حمله‌های دفاعی اضافی را علیه چندین هدف در ایران آغاز کردند. این حملات در پاسخ به تهاجم بی‌دلیل و ادامه‌دار ایران است.</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/17263" target="_blank">📅 01:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17262">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">U.S. Central Command forces began launching additional self-defense strikes today at 5:15 p.m. ET against multiple targets in Iran at the Commander in Chief’s direction. The strikes are in response to Iran’s unwarranted and continued aggression.  @U_S_CENTCOM</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/17262" target="_blank">📅 01:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17261">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromU.S. Central Command</strong></div>
<div class="tg-text">U.S. Central Command forces began launching additional self-defense strikes today at 5:15 p.m. ET against multiple targets in Iran at the Commander in Chief’s direction. The strikes are in response to Iran’s unwarranted and continued aggression.
@U_S_CENTCOM</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/17261" target="_blank">📅 01:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17260">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">صدای انفجار از بندرعباس</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/17260" target="_blank">📅 01:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17259">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">شلیک موشک از غرب کشور</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/17259" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17258">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">تسنیم:
انفجار در سیریک</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/17258" target="_blank">📅 01:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17257">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">انفجارهایی در سیریک و جزیره قشم (منطقه تنگه هرمز) گزارش شده است.
سامانه‌های پدافند هوایی اکنون در غرب تهران فعال شده‌اند.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/17257" target="_blank">📅 00:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17256">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">خداوکیلی ببینید گیر چه اسکل هایی افتاده ایم!  اینها برای فرزندان ما تصمیم میگیرند!</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/17256" target="_blank">📅 00:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17255">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">به نظر می رسد جنگ قطعی شده.</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/17255" target="_blank">📅 00:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17254">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گزارش موسسه مطالعات جنگ از کمک های نظامی و اطلاعاتی روسیه و چین به ایران  روسیه از تلاش‌های ایران برای بازسازی توانمندی‌های نظامی خود در دوره آتش‌بس حمایت می‌کند. نیویورک تایمز به نقل از مقامات آمریکایی گزارش داد که روسیه قطعات پهپاد را از طریق دریای خزر به…</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/17254" target="_blank">📅 00:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17253">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سخنگوی کمیسیون امنیت ملی مجلس:
در جنگ ۴۰ روزه وسعت آب‌های سرزمینی ایران افزایش یافت، در جنگ بعدی شاید وسعت خاک ایران افزایش یابد.</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/17253" target="_blank">📅 00:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17251">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ادعای منبع پاکستانی به الحدث:
ما امروز از امضای توافقنامه صلح، دور شده‌ایم.</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/17251" target="_blank">📅 23:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17250">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">مسئول ایرانی به المیادین:  آماده اجرای نسخه جدیدی از جنگ هستیم  شبکه المیادین به نقل از یک منبع امنیتی سیاسی بلندپایه ایرانی اعلام کرد که  اگر ترامپ این‌بار در محاسبات خود مرتکب اشتباه شود، قیمت نفت با صدایی بلندتر با جهان سخن خواهد گفت.  این مسئول ایرانی…</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/17250" target="_blank">📅 23:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17249">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">مسئول ایرانی به المیادین:  آماده اجرای نسخه جدیدی از جنگ هستیم
شبکه المیادین به نقل از یک منبع امنیتی سیاسی بلندپایه ایرانی اعلام کرد که  اگر ترامپ این‌بار در محاسبات خود مرتکب اشتباه شود، قیمت نفت با صدایی بلندتر با جهان سخن خواهد گفت.
این مسئول ایرانی تصریح کرد تهران برای اجرای نسخه جدیدی از جنگ آماده است و غافلگیری‌هایی در انتظار دشمنان است.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/17249" target="_blank">📅 23:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17247">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">لینک ویدیوی نشست امروز با نیما</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/17247" target="_blank">📅 23:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17246">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ادعای خبرنگار الجزیره: واسطه قطری تهران را ترک کرد   واسطه قطری تهران را ترک کرد. به گفته وی سند توافق برای حل برخی اختلافات که هنوز به دلیل تغییرات آمریکا پابرجا هستند، نیاز به کار دارد.   منابعی در تهران می‌گویند هرگونه حمله به ایران به معنای پایان اجرای…</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/17246" target="_blank">📅 23:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17245">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ادعای خبرنگار الجزیره: واسطه قطری تهران را ترک کرد
واسطه قطری تهران را ترک کرد. به گفته وی سند توافق برای حل برخی اختلافات که هنوز به دلیل تغییرات آمریکا پابرجا هستند، نیاز به کار دارد.
منابعی در تهران می‌گویند هرگونه حمله به ایران به معنای پایان اجرای آتش‌بس است و واسطه‌ها در حال حرکت برای جلوگیری از هر درگیری جدیدی هستند.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/17245" target="_blank">📅 23:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17244">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">شبکه CNN: فرماندهان جدید ایران ریسک‌هایی را می‌پذیرند که اسلاف آنها از آن اجتناب می‌کردند
حملات موشکی این هفته ایران یکی از جسورانه‌ترین اقدامات تهران برای بازتعریف خطوط قرمزش است و نشان می‌دهد که رهبرانش آماده پذیرش ریسک‌های بزرگ‌تر هستند. تغییر گسترده در استراتژی ایران با حملات اخیر گامی رو به جلو بود. این تحولات نشان‌دهنده یک چرخش بزرگ‌تر در تهران است؛ جایی که نسل جدیدی از رهبران در حال کنار گذاشتن رویکرد محتاطانه و تدافعی سنتی جمهوری اسلامی هستند.
آنها اکنون به جای اتکای صرف به بازدارندگی و صبر استراتژیک، تمایل بیشتری برای پذیرش ریسک و به‌کارگیری اهرم‌های نظامی، اقتصادی و منطقه‌ای خود جهت شکل‌دادن به تحولات خاورمیانه دارند.این نخستین بار در دهه‌های گذشته است که یک قدرت منطقه‌ای ابزار، ظرفیت و تمایل به کارگیری قدرت سخت در برابر مانورهای نظامی اسرائیل و آمریکا را دارد.
تهران به دنبال ایجاد یک معادله جدید است. رویدادهای اخیر بار دیگر ثابت کرد که رهبری فعلی ایران بر این باور است که هر آنچه از طریق دیپلماسی به دست نیاید، در نهایت از طریق قدرت قابل دستیابی است.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/17244" target="_blank">📅 23:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17243">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AyxMu2P1j8cIj86n9k_axn0N6eST8uGHtDomqCPwzMuIdgl50K_PBwpg5ApK7PDRW-l2PWoK78I76nJyGkSg4dOXxJnfz7Sz4Th6QYUvM32-Ohagy2cY1L8CwZElbU00rBKUxhrmTxy3Zai1p62isrSgXekvEVSda3_DsBUZzD2tYafvIkhBCSZbtrkdZIrps0IZZhFfI5GZRyvawa83RiMlgJ-4wCUB770wFXTOqrKmOPtK8ePYXO3Q97f2QohWTql82iOBwpSoeWUAohESB3eJaVjrQPZeB2P9NHDtth82mmffLJcDh0fOE2Sj-4QQjpUjYtoQJ4wMdeYZdCal3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش سوزی در میدان قیام تهران</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/17243" target="_blank">📅 20:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17242">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BatmfVQuPHcY6Jdrz1OTcLPhCkDpsTqyyryxjNT_z-eL7IusyhRvyyo18_3rhdjPWE4Q-VRdyCwWiFJPK6oIis5nWijooVGmmO2_pBpSNw2bY1x43w2APBQ53466e6iv8g2CeGWscmBp6eEQARO30TVlf8sgk4knOo4xjmP_hDfvv_ZqKMjRXNj4VYeizgTE7efd7t3tjmsbFLSeyNQq1w77RAn0fP7t3G39HM9fZUTvN53Oxsf_PNpilW5UMcWks-pNYKWj5Rh3c9yiIul6Em3gmcRWi6himFXa4JVXY-Qyi-Q4wIvggGiL58usjYFFO-RO0UUr3cxaN1hFJlnvWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا نفتکش «سیتی بلو» را در خلیج عمان هدف قرار داد  سنتکام: نیروهای آمریکایی نفتکش «سیتی بلو» را در خلیج عمان مختل کردند. یک هواپیمای آمریکایی پس از سرباز زدن خدمه از دستورات، موتورخانه کشتی را هدف قرار داد. از آغاز محاصره در ۱۳ آوریل، سنتکام ۸ کشتی متخلف…</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/17242" target="_blank">📅 20:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17241">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">آمریکا نفتکش «سیتی بلو» را در خلیج عمان هدف قرار داد
سنتکام: نیروهای آمریکایی نفتکش «سیتی بلو» را در خلیج عمان مختل کردند. یک هواپیمای آمریکایی پس از سرباز زدن خدمه از دستورات، موتورخانه کشتی را هدف قرار داد. از آغاز محاصره در ۱۳ آوریل، سنتکام ۸ کشتی متخلف را هدف قرار داده است.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/17241" target="_blank">📅 20:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17240">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ا ترامپ:  «ما بسیار به رسیدن به توافق با ایران نزدیک بودیم، اما آنها مدام ما را به تأخیر می‌اندازند و به ما بی‌توجهی می‌کنند».</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/17240" target="_blank">📅 19:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17239">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">تصویب قطعنامه ضد ایرانی در شورای حکام ( ۲۱ رأی موافق ، ۳ رأی مخالف و ۱۰ رأی ممتنع
)</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/17239" target="_blank">📅 19:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17238">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ا ترامپ:  «ما بسیار به رسیدن به توافق با ایران نزدیک بودیم، اما آنها مدام ما را به تأخیر می‌اندازند و به ما بی‌توجهی می‌کنند».</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/17238" target="_blank">📅 19:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17237">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ا ترامپ:
«ما بسیار به رسیدن به توافق با ایران نزدیک بودیم، اما آنها مدام ما را به تأخیر می‌اندازند و به ما بی‌توجهی می‌کنند».</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/17237" target="_blank">📅 19:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17236">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">لینک ویدیوی
نشست امروز با نیما</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/17236" target="_blank">📅 19:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17235">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❗
ترامپ: من نزدیک به صدور دستور حملات جدید به نیروگاه‌ها و پل‌های ایرانی هستم - فاکس نیوز</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/17235" target="_blank">📅 19:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17234">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59886795a.mp4?token=ewTNGJ8VN8G_KYCZziot8ZMx8A6B1kGGLWKBO7IOhazLDSuRqLi-SxiH9U69kS-X9eOIpscFwQfgjdN_jjQRAySDufmYFlrk8yvUApFqe5LB7RQsRDF0Vn9CF69ifQO76KYafxtYBBpSHMX2xGyejo5ZXd2rEANuAqMKjDTKSo4wkU7o5YBg_NfN4YBRNwwj2L93B0XJUQKCIuYTuewsBM7BKswJX6Z42YxlR6APyLw5PI5jJG87np-7LlIm7_M-88v6vRZs-582i0BAs0ftCHdQQhApiQgDhFk8oSdsQGCZIkDyoP1-vCuNB35mh6h5Pv3XrlmZL0SRIkDkvDOZrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59886795a.mp4?token=ewTNGJ8VN8G_KYCZziot8ZMx8A6B1kGGLWKBO7IOhazLDSuRqLi-SxiH9U69kS-X9eOIpscFwQfgjdN_jjQRAySDufmYFlrk8yvUApFqe5LB7RQsRDF0Vn9CF69ifQO76KYafxtYBBpSHMX2xGyejo5ZXd2rEANuAqMKjDTKSo4wkU7o5YBg_NfN4YBRNwwj2L93B0XJUQKCIuYTuewsBM7BKswJX6Z42YxlR6APyLw5PI5jJG87np-7LlIm7_M-88v6vRZs-582i0BAs0ftCHdQQhApiQgDhFk8oSdsQGCZIkDyoP1-vCuNB35mh6h5Pv3XrlmZL0SRIkDkvDOZrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/17234" target="_blank">📅 19:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17233">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترامپ درباره ایران: امروز دوباره به شدت به آنها ضربه خواهیم زد.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/17233" target="_blank">📅 19:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17232">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">عجب گیری کردیم به حضرت عباس</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/17232" target="_blank">📅 19:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17231">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❗
ترامپ: ما به شدت به ایران حمله خواهیم کرد</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/17231" target="_blank">📅 19:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17230">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">باورتان میشود این دو جمله را ظرف چند دقیقه گفته؟</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/17230" target="_blank">📅 19:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17229">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❗
ترامپ: ما به شدت به ایران حمله خواهیم کرد</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/17229" target="_blank">📅 19:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17228">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❗
ترامپ: ما به شدت به ایران حمله خواهیم کرد</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/17228" target="_blank">📅 19:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17227">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">این یعنی نه ایران و نه روسیه از این جهش بهای نفت حداکثر استفاده را نبرده اند؛ ما به دلیل محاصره دریایی آمریکا صادراتمان افت کرده (پست ریپلای شده را ببینید) و روسها هم به دلیل حملات سنگین پهپادی اوکراین.  عربها هم که عمدتاً ضربه دیده اند و لذا بزرگترین منفعت…</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/17227" target="_blank">📅 19:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17226">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">جالب است بدانید در جنگ جهانی اول، عثمانی متحد آلمان بود و در جنگ جهانی دوم هم نازیهای آلمانی با گردان های پان ترک مورد حمایت آنکارا در میان تاتارهای کریمه بشدت همکاری داشتند.  اساسا یکی از دلایلی که استالین تاتارهای کریمه را بعد از بازپسگیری اوکراین از نازی…</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/17226" target="_blank">📅 18:37 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17225">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اردوغان:  «هشتاد و پنج سال پیش، سکوت و بی‌عملی در برابر هیتلر منجر به از دست رفتن هشتاد میلیون جان در سراسر جهان شد. تمام بشریت بهای جنون هیولای خون‌آشام را پرداخت کرد.  امروز، همان اشتباه تکرار می‌شود. نسل‌کشی‌هایی که توسط قصاب غزه، نتانیاهو، و کابینه او…</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SBoxxx/17225" target="_blank">📅 18:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17224">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اردوغان:  «اجازه دهید این را بسیار شفاف بیان کنم: هیچ‌کس نباید به دنبال ماجراجویی برود و هیچ‌کس نباید خود را به واگن شبکه نسل‌کشی‌های صهیونیستی ببندد.  اگر هر کس سعی کند بر حقوق و منافع ترکیه و ترک‌های قبرس در شرق مدیترانه تجاوز کند، می‌خواهم بدانند که پاسخ…</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SBoxxx/17224" target="_blank">📅 18:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17223">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترکها در ظاهر می گویند اردوغان موفق شده ترامپ را متقاعد کند تا از این طرح جلوگیری کند اما به نظرم این پلن A شان بوده و پلن B شان شامل ورود مستقیم نظامی به ایران همراه باکو برای اشغال شمال غربی ایران بوده که پیشتر اشاره کرده بودم.  در هر صورت، در راند بعدی…</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SBoxxx/17223" target="_blank">📅 18:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17222">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">نتانیاهو از تشکیل اتحاد جدیدی علیه «محور شیعه بنیادگرا و محور سنی بنیادگرا» خبر داد.  این اتحاد شامل هند، یونان، قبرس، کشورهای آفریقایی، کشورهای عربی و کشورهای آسیایی خواهد بود.</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SBoxxx/17222" target="_blank">📅 18:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17221">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ارتش اسرائیل تأیید کردن که در جریان حمله موشکی ایران به اسرائیل در اوایل این هفته، خساراتی به پایگاه هوایی رامات داوید نیروی هوایی اسرائیل وارد شده است.</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SBoxxx/17221" target="_blank">📅 18:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17220">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ارتش اسرائیل تأیید کردن که در جریان حمله موشکی ایران به اسرائیل در اوایل این هفته، خساراتی به پایگاه هوایی رامات داوید نیروی هوایی اسرائیل وارد شده است.</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SBoxxx/17220" target="_blank">📅 18:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17219">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ig5lAvx-7gO7tFOEFFzIy91f3xop7me4u6VEIDr9IfaQEKIZ6ktMhUK87_39ouBSI712P9214D6o3E83-igYPBlwclQlgwQ2V_2JnO5UrA-mRMh2AncljkdOwboB5uM7k0Ln61zi8JrDu16Q_1cfQAHgKJYswU4sZiko8czpLMa9Md_wD5qKP0O4fOV50SrwS-CJMrTTE6W2f3nYs-EIdOoAIwevvJu47Sj7vNvH37xW5mZuluzVECJuCL6K6tftrrpbnFG7aguCtTB1r9QulkjNP16C3wfefLdtvCQzr5KRXTNa18-yyMM7N8okTq45ouBkTgecXxxfjMRNyrY3DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تولید موشک‌های بالستیک تاکتیکی کره شمالی به شدت افزایش یافته است.
کارخانه‌های این کشور تولید موشک KN-23 را افزایش داده و کیم جونگ اون دستور داده ظرفیت موشک‌های بالستیک و کروز طی پنج سال ۲.۵ برابر شود تا نیاز روسیه تأمین و کشور در برابر هر سناریوی آمریکایی مقاوم شود.
کارشناسان کنگره آمریکا مانورهای صعودی این موشک‌ها را پیشرفته‌ترین دستاورد تسلیحات تاکتیکی کره شمالی توصیف می‌کنند. نوع بزرگ‌تر آن حامل کلاهک ۲۵۰۰ کیلوگرمی است، از سامانه‌های AEGIS آمریکا فرار می‌کند و سال گذشته ۱۰۰۰ فروند از نوع کوتاه‌برد آن در خط مقدم منطقه غیرنظامی مستقر شد.
کیم جونگ اون شخصاً از کارخانه‌هایی بازدید کرد که از اهداف فراتر رفته بودند و این توسعه را وظیفه اصلی ارتش بازسازیشده کره شمالی خواند.
این کشور همچنین تولید مواد هسته‌ای درجه تسلیحاتی را دو برابر کرده و موشکهای هایپرسونیک خود را آزمایش می‌کند،</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/17219" target="_blank">📅 17:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17218">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">از امشب ساعت 21 در ورزش سه؛
💡
جواد خیابانی و خداداد عزیزی در بر جام 2026
🏆
متفاوت‌ترین برنامه #جام_جهانی2026(بر جام) با اجرای جواد خیابانی و خداداد عزیزی
🆔
@varzesh3</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SBoxxx/17218" target="_blank">📅 17:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17217">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromورزش سه</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f8d3318cf.mp4?token=HsduGcJjhZhn_h7yARq9xyFd9khn8MvSeTYZmBhOQx9JGmAXgo2JBEnJpMGGfy1djJbmUzCLncEtiilB07qEqvuKBbkATCM09GEFSPMc1nC8zzJlCYC0nCaWBLeWI16j9AuCH5OjzNeIdBhtLaDCci4T2g-Q9zzxdZtWyHUr7zLL6N6Qwrv3y85KoDaWFAwacMu52fy5FhJEKz4uoXAA-7MFlfmefzzRmfQcM6odHzFUXh7Qp93-rfLwQISFSDw-cOxlBdtNWj4EnOynGPHaTVHueu_8dMAw9rwgU3bn9FRy_FhQ-qT0ujUkoKwEH2rLwLACoOEShSQBFvxDwynNoqg_GwQGyofFREjrBmccwN-fhKzJtsOJYVTt8pucM_gvpzKTvwr3YrQS_KxJuebC6Dj00_OSz4QOsV-FmjsddYkg0QX8_1hNgIjadudNLuQXppwQHdCbwQXrGIUU4qP6JPoysMDJtTROFkVQsM99gGwsEz-Ma53I1AONXiMXcT59blTn9lN1VNgTCoUZ7V6wxJaGHM6UOdqKHnkq7OG8S9fp-HIaxThJYnzo-9eCM3kqQzFoXX6B8iQLkMSOQNJtm52tpq6ntn0HjFPGHEMna9dEO4XtvolIR1RN80rtyJlNjyAKY_-D39D6nTbh5LdQ2zfJ_N2gEVBaMMKoCPV0Nfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f8d3318cf.mp4?token=HsduGcJjhZhn_h7yARq9xyFd9khn8MvSeTYZmBhOQx9JGmAXgo2JBEnJpMGGfy1djJbmUzCLncEtiilB07qEqvuKBbkATCM09GEFSPMc1nC8zzJlCYC0nCaWBLeWI16j9AuCH5OjzNeIdBhtLaDCci4T2g-Q9zzxdZtWyHUr7zLL6N6Qwrv3y85KoDaWFAwacMu52fy5FhJEKz4uoXAA-7MFlfmefzzRmfQcM6odHzFUXh7Qp93-rfLwQISFSDw-cOxlBdtNWj4EnOynGPHaTVHueu_8dMAw9rwgU3bn9FRy_FhQ-qT0ujUkoKwEH2rLwLACoOEShSQBFvxDwynNoqg_GwQGyofFREjrBmccwN-fhKzJtsOJYVTt8pucM_gvpzKTvwr3YrQS_KxJuebC6Dj00_OSz4QOsV-FmjsddYkg0QX8_1hNgIjadudNLuQXppwQHdCbwQXrGIUU4qP6JPoysMDJtTROFkVQsM99gGwsEz-Ma53I1AONXiMXcT59blTn9lN1VNgTCoUZ7V6wxJaGHM6UOdqKHnkq7OG8S9fp-HIaxThJYnzo-9eCM3kqQzFoXX6B8iQLkMSOQNJtm52tpq6ntn0HjFPGHEMna9dEO4XtvolIR1RN80rtyJlNjyAKY_-D39D6nTbh5LdQ2zfJ_N2gEVBaMMKoCPV0Nfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از امشب ساعت 21 در ورزش سه؛
💡
جواد خیابانی و خداداد عزیزی در بر جام 2026
🏆
متفاوت‌ترین برنامه
#جام_جهانی2026
(بر جام) با اجرای جواد خیابانی و خداداد عزیزی
🆔
@varzesh3</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/17217" target="_blank">📅 17:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17216">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">وزیر اسرائیلی میکی زوهار در پاسخ به اظهارات اردوغان:  دیکتاتور اردوغان اگر جرات کند ما را آزمایش کند، سرنوشتش بدتر از ایران خواهد بود.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/17216" target="_blank">📅 15:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17215">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❗
ترامپ: من نزدیک به صدور دستور حملات جدید به نیروگاه‌ها و پل‌های ایرانی هستم - فاکس نیوز</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/17215" target="_blank">📅 14:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17214">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBmde-Sh3DRdRHot_P8wBVj89EXNNMhPGnQdtdFMS3yDvtd94RWVkZlDUvk8ymfQySCayyK-L8vao4TDtrNIVH2aIrNhAYbOnm45kwcbZvWYhNYcFrWOeiEiNISsQRnzZaxA4lpDxjKP53880ef3DHoEK_F1vTdv-IBrukiu5MVTIP4S59wBuQX-8XH008hImE7BMElkjH2C8X03mIyqFyHX3enWf80KEDPG4-1KOufRxfJ7S5msot-xUWjRCXWpbjNQPB4ucYVDBtH-hiAriM16SFhhxpPejWuFj6ob3TH2WN0kMT8lAsTjSXF0ZUAjP7dESiaHBkT45912KaYc-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/17214" target="_blank">📅 14:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17213">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترامپ:
نیروی نظامی ایران کاملاً به هم ریخته است. بخش زیادی از آن، مانند نیروی دریایی و نیروی هوایی‌شان، دیگر وجود ندارد - آنها کاملاً شکست خورده‌اند.
ایران فقط حرف می‌زند و هیچ اقدامی نمی‌کند. قلدر خاورمیانه مُرده است!
آنها برای مذاکره بر سر توافقی که می‌توانست برایشان عالی باشد، خیلی دیر کرده‌اند
،  حالا باید بهای آن را بپردازند!</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/17213" target="_blank">📅 14:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17212">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">رجب طیب اردوغان رئیس جمهور ترکیه : «حملات نتانیاهو و شبکه جنایتکارش علیه سوریه و لبنان به نقطه‌ای رسیده است که نه تنها این دو کشور برادر را تهدید میکند بلکه اکنون ترکیه را نیز تهدید میکند.»  امنیت ترکیه تنها در هاتای شروع نمی‌شود ؛ بلکه در حلب ، دمشق و بیروت…</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/17212" target="_blank">📅 14:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17211">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jd2-oVferIbDYpYxpY-P36Jz3lGXdB9-HV2ulRTOgXf5XszxLfT4kXrqJ2c7jfEQHT5g7bToE6ppRc2qwUD9z7YYIWTGziiRMcHUytG11RtcS2VRY4_QPW4zdEzQ-kvp5pPvieB_RsMKs_eFJGg4bhFBTS1lpFcW8g3WvR5CBhstm5vBTwwd6HetUusfZxSF1jsfqbtrWAE_uwG9nGB3SALCztEjIzmrwx1zbnBxpsr0dqeWwoAblLerjF7r0-ELz5uSF_AcqUAv8bEn7FaDJMKmoQJUuS9BsNs4pjDDwNoz4-w3y6I7gvPrqfQ9JHYpx6f4m4T06uZcXcsY0AEGdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متن کامل گزارش کنگره آمریکا درباره هواگردهای سرنگون شده ارتش این کشور در جنگ با ایران:  بررسی کلی  در ۲۸ فوریه ۲۰۲۶، ایالات متحده آمریکا با هماهنگی اسرائیل، عملیات‌های نظامی علیه ایران را تحت عنوان عملیات خشم حماسی (OEF) آغاز کرد. این درگیری شامل نبردهای هوایی،…</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/17211" target="_blank">📅 14:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17210">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5RunpJTyuXV3e7KEiKJ1DDmodjezPXAZ0BgOa2qyU2hVcM93C-Bc4tTvf-YkegvxFlCzlI6ADJoICso74-c7zY4bt1xLlgHr9ywpIE27tRIQ-iIyottffTZE1i5K-PjO9J93hdB-qPwXRX_N9Hd_VwdLyt4PdwUDTQJ7MXCRkyxhSiSN1a5T2tba0as-vRTQxep2qwYpmulm-wIB7vRTq6xrg25r4jv8Pi_zvYYNbxGUp4nHh9t2fjoeaAtJw3Fwl4BhddTTw3gR8_k-8KR3RswvyT0ViAPJCNtX4aTsRQXVrcxD11hlnHMDAAyWvTyPJsDXFkang7kYKlPzODrMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رجب طیب اردوغان رئیس جمهور ترکیه : «حملات نتانیاهو و شبکه جنایتکارش علیه سوریه و لبنان به نقطه‌ای رسیده است که نه تنها این دو کشور برادر را تهدید میکند بلکه اکنون ترکیه را نیز تهدید میکند.»  امنیت ترکیه تنها در هاتای شروع نمی‌شود ؛ بلکه در حلب ، دمشق و بیروت…</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/17210" target="_blank">📅 13:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17209">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اردوغان:   حملات اسرائیل به سوریه و لبنان اکنون به تهدیدی برای ترکیه تبدیل شده است</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/17209" target="_blank">📅 13:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17208">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اردوغان:
حملات اسرائیل به سوریه و لبنان اکنون به تهدیدی برای ترکیه تبدیل شده است</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/17208" target="_blank">📅 13:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17207">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ارتش  آمریکا از شامگاه شب گذشته تاکنون در سه موج حمله مراکز راداری و کنترل فرماندهی سپاه (زیرساخت های کنترلی تنگه هرمز ) و دو مخزن آب در قشم، سیریک و جاسک را مورد تهاجم قرار دادند.</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/17207" target="_blank">📅 10:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17206">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ارتش  آمریکا از شامگاه شب گذشته تاکنون در سه موج حمله مراکز راداری و کنترل فرماندهی سپاه (زیرساخت های کنترلی تنگه هرمز ) و دو مخزن آب در قشم، سیریک و جاسک را مورد تهاجم قرار دادند.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/17206" target="_blank">📅 10:41 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
