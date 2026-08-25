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
<img src="https://cdn4.telesco.pe/file/VGcelHTCAH-w6-U6Bw2hYLqLXHFVLkz3Vco6srfOBIdtTO1Cx7ov6s1fQRkeU7Y5jUmatvNbYuAjH-TsYciA_x7vOdO7hrySQHIH83sMQnJPHRAn3B7qgxcB0bNcJIK27kge-KhijgbqJAoSKECN2Az9lz-wsw1FDnsoTH8-BZa4cwf8Ik-km7SlQI2-0xKbv31YQgPuEDtwb3gITu8S5j5bape44FEQzsx9RjpRQKNLjgreyxl6_cC-gGc1ESfZrMY5-ifdNHEG5qxraGKTk30OLoLNjT-vQ2MDn4ISOpXvcDf15pwArKvePTuEtVD9FONJCsoMhP-GtNGjinNZdg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.6K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-03 15:59:41</div>
<hr>

<div class="tg-post" id="msg-20196">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHGalfjYFCGDaacrLCNGRz9Heg4erIed0-4ahOBA66NKwlyZm8axMI3NdivP-DarsL-OpAZ634-t4uiKSItwDpXdUYwfUjmM9rm_zc0e3Mufq-ySANoOJEOPhNrXX5PXq5DzVxvwCHi9nL7FYH7jADjCfZ6OxYzZbZEmWIs7Vc9J4z42AD-3Lmen_d2ve4FzMuwdGouf3SbeO25Dccc0h1jkTDlglgx1dbDbbrMgrKL8K1JHzLM__dekHJPrEvV6_X9LQbUZ7e2X2oArUvY2A7Hy8BN2Wdh77b8kvG32Y6krJPoEPONpnKWX32ICBrgkWrmXV29aUAXYB5sMp6NPKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ
«جمهوری اسلامی ایران که در حال فروپاشی است، بخش‌های بزرگی از نیروهای نظامی خود را حقوق نمی‌دهد و هم‌زمان، در سطحی بی‌سابقه اقدام به کشتن معترضان می‌کند؛ حتی افرادی که در حال اعتراض نیستند.
این یک بحران انسانی با ابعادی بی‌سابقه است و باید همین حالا متوقف شود.</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/SBoxxx/20196" target="_blank">📅 15:19 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20195">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">لحظه ای که روسیه ضد اوکراین سلاح هسته ای استفاده کند، آمریکا هم ایران را با هسته ای خواهدزد.  شاید هم اول آمریکا بزند.</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/SBoxxx/20195" target="_blank">📅 14:47 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20194">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">حالا اگر تصویر میکنید که یک فروند ناصر همتی میتواند جلوی این روند ژئوپولیتیکی را بگیرد که ولی خب.</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/SBoxxx/20194" target="_blank">📅 13:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20193">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبلومبرگ فارسی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwvALGhZzTkJ92jevSSrV__ubptniQY15ZqwtF6CGlOnNIUS4grACjKMcjdN3JtOWM5ql9zUvgaWof2mDodmJ4tvJHX6YK3vqBH3xel-SZl29igLqmfvxn-EKrJtq_v43I2z-kHpgTlBEmzYH59OMscPNcMVSIIFnbc-1GcdJQmcY96KzEik-WwOUMAkKM8Dlenwv8PKizSz7epWfCSIZxZNyrJ0uCb-vBlSYpaf5A9ks-PLH_kvAyTn4IlCUK7TUm8VLUKVxxXlp-qe0nKUq55au-vyIRAn2nt__7kV1t67Z4Sbse8IpdEyL2-yA0qDgTmfGsWavfHY3dEyITZhcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای همتی از زمان دلار ۳٠ تومانی تا امروز که دلار ۲٠٠ تومان را پشت سر گذاشت به آینده اقتصاد خوش‌بین است
☑️
@persiannbloomberg
بلومبرگ فارسی
✔️</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/SBoxxx/20193" target="_blank">📅 13:55 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20192">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKpAhQF_i0wvHn9iGGhcKgbVvnW0zB_InYRUMyfG8jCPojYWWPLXrWLmXEecQZnpxiWoo9uAP7wDKpRqWdG8sxOweaxvH00JaGKnsIz8UadQrnM1YAmtWBELkwm2qkkoCTc5Yf8MK1AqU71PndtLbwzG_OdXiqmdm61DFTbVuLkKJCZ2TE5SbGKY-POBDWfSTiezFOTsrp0G5702gp9bzSkHIbYBbRUpbO8z6xOAx3INy8cvaGqbdHFjJpeHGcRRmcvSJeS08C1ZXfpmCKk67hvICSeJ4cpRBPo2Zf8g75UaaQXlItdXpbDvF1flBCGUBFq_fJGt_W8FCt4kndhS5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادغام شبکه خبر و اینترنشنال</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SBoxxx/20192" target="_blank">📅 12:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20191">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">چرند.</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SBoxxx/20191" target="_blank">📅 12:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20190">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">یک منبع مطلع در خبرگزاری العربیه:   آمریکا پیشنهاد کرده است که در ازای باز شدن تنگه هرمز و توقف حملات توسط عوامل، محاصره را متوقف کرده و تحریم‌ها را رفع کند.</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SBoxxx/20190" target="_blank">📅 12:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20189">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">یک منبع مطلع در خبرگزاری العربیه:
آمریکا پیشنهاد کرده است که در ازای باز شدن تنگه هرمز و توقف حملات توسط عوامل، محاصره را متوقف کرده و تحریم‌ها را رفع کند.</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SBoxxx/20189" target="_blank">📅 12:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20188">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qw2Cx3JWDq2z2dEHD26oGfFBK15hRJNf-E5f3-e8SCt1wiPsBLYik1niRt27AdtBsZqCqEC92IQvpNS6C8LQOYE7b-Vewk5uPDOllXFhwIUF5OoEZHcX4GwVwK_EwKhoziY4vrycGLpAKoegsrEpd0xX6aoHBR33eP08Ctj1pM0HbSGuFRNpmeQcOxtihmNszzCO8dYWCdOYH346Jzl-RgXXwwzpSenqrHSBW3BL3i22tBMoCy-8gRBlMHa4A0pO-lHDC_Z1XVh3ItChqDtDkSuJtxjZ50wanea92XSRFQKOzXIq8dRaZ10-NIZqukJXjFpZzeV6wyFyk2k1xg8zTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز هم بسیار بالاست و پیش بینی می شود شاخص نزدک افت داشته باشد.
طلا هم با این وضعیت قاعدتاً امروز باید به افت خود ادامه بدهد.
دقت کنید که سقف دیشب عملاً جعلی بود و بعد از ثبت آن حدود 800 پیپ افت داشت.</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SBoxxx/20188" target="_blank">📅 11:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20187">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cc0E6HyjCoBCQ9DbWTd2ybW7-b0NzNhapS_peJZVX7U4JVsNCBR3dUU4QHOtaS4BuIIPS5G2jY4tSWfRJUGoUSbRiXVswC1ertNtbNMHvd2UAv1tc1RekIiamCttaLRvxgy7jzvqbO4HFcDGC7QeyjxF2hvXJNQibohjcSHzasjsD8z_GxXKRLGXyQOGVqPXdaeF_5RI0-v9LG840Kfp3BWJ1wz5-svUIe62SM8yW5wPZ8lE372UTG7RYz6yY80W9_YO3dVcKsdNahLDIrvoJjlVsNKKqZ_dyaXwH6Nf_7pfO6lZyN_RvVfFB20i4UXasmlpp394y6DJ_Eqz2WWy_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج 2 نفت دارد تمام می شود.  موج اصلاحی دلار به ریال هم قاعدتاً باید آغاز بشود با تارگت 240 به بالا.</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SBoxxx/20187" target="_blank">📅 10:38 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20186">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YSCK6XezcI0IFW0AqinkiN7Bts2N9IsH0x7fk2hqIaTbx6t4-17pwBgMxhxW_yPzHTy4Hg0aEqbsAjx5uwhlwBZWOg4fkwO_3VHa3hwddyDSyMpnEsR1nV6gNydJNad825xulhMhMFcT1iFjChDoH5wn8BQiRMC26ppOLeMqCIvcv9NxpKdEUNdgR1k-ERN7rxy7mzGVkzn5kkG9gESFOpR11XWpkdDYAQB3wWB9HedwgdlbRbShWZIqWgUNcJVNg1YqU9B3rFlzouMjDDB2PpOK4tAAfSRmenFJ6zMwabcPw7TZlSuApn-eMy4vpZ9VfbUnMcDA1gsFy82g_arGSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بسته جدید بسنت سروصدایش بیشتر از تاثیرش خواهدبود.  چین اگر بخواهد — که به نظرم می خواهد — به هر قمیتی از سقوط کامل اقتصاد ایران جلو میگیرد و همه ابزارهایش را هم دارد که اینجا اشاره کردم.  کالاهای موردنیاز ایران را کماکان تا جای امکان صادر می کند و پولی…</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/20186" target="_blank">📅 03:24 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20185">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hrw41KIQysxEoo1WF0krhJLfkRhqQTQWLlcTfNEFW4XpQvaouye_GMgd7o-ZJ40f1TloKPIUMq3ZJmK-q2G0a8GgOzkAHDbCEA1VNeEqf7sUxw6xY1zE1gSl1WdwU17wZ2hlb-MmweVlem0Hw9Zg7DOfuqXID5U__0tlkpMxGgsxrnuTRDZwUg1NyKy7w7_gxfwA3XjdMqeE72nsGbCWWda0y0-mDI9BtNXOyuCHcJEHhx-ueKCy-eY2_Wmjas5ihu-P6It3ta60R1oNytmi4e1fCuN4KED5CwgV6MgdEYc5uiD6XJTOMuC1aoI5Ejs4dGNsIgcXsDDAWeUfBPV38A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح بسیار بالایی قرار دارد.  دقت کنید که با آغاز برنامه بازخرید اوراق قرضه بلندمدت خزانه داری آمریکا، یک عامل جدید وارد محاسبات شده که در این شاخص هنوز آن را دخیل نکرده ایم که روی طلا موثر است.   ولی با این حال، پیش…</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SBoxxx/20185" target="_blank">📅 03:11 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20184">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">فرمانده انتظامی کل کشور در ساری:  جنگ سوم هنوز تمام نشده لذا باید با آمادگی کامل در برابر دشمن، غافگیر نشویم، چرا که خیلی از غافلگیری‌ها نتیجه غفلت بوده و دشمن از ما دست برنداشته و جایی از ما دست بر می دارد که ما دست برتر داشته باشیم.   دشمن به‌دنبال ایجاد…</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SBoxxx/20184" target="_blank">📅 01:24 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20183">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تحلیل عوامل سیاسی چرایی شتاب شدید رالی اخیر دلار</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SBoxxx/20183" target="_blank">📅 01:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20182">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/313a4a00f6.mp4?token=DiF7WVyi_q3fTNzQhhy9MwOT0AOLqMsRZ6DNkTUhfs28iFZLcLZpaSFUriHmLfopyrOWryzqEFD5LLPtnkWDbkxtVeNtKlwVBAUNz_0sFXQEs_uwJdXN250z2q95_6sdArpWsj-LWdV22vtsRDGqvEvyGnCIcsuYKbiZpxlsy5PFV2YxVNTqRSruCEvy560PgP1Ws2f8NpYrcpKkMoq-uLRPp86bxMTyK0qlgw8b1peTtTI1ozCTazQtRtUc5sgfXr_E4Zl6YLHM_ijFp93alg7c9P7MCu6klE5NbISFlJsAcPQSCazM0Bdq3hMiVOXdqqFQaXwYOwxiiLUBUZJ_hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/313a4a00f6.mp4?token=DiF7WVyi_q3fTNzQhhy9MwOT0AOLqMsRZ6DNkTUhfs28iFZLcLZpaSFUriHmLfopyrOWryzqEFD5LLPtnkWDbkxtVeNtKlwVBAUNz_0sFXQEs_uwJdXN250z2q95_6sdArpWsj-LWdV22vtsRDGqvEvyGnCIcsuYKbiZpxlsy5PFV2YxVNTqRSruCEvy560PgP1Ws2f8NpYrcpKkMoq-uLRPp86bxMTyK0qlgw8b1peTtTI1ozCTazQtRtUc5sgfXr_E4Zl6YLHM_ijFp93alg7c9P7MCu6klE5NbISFlJsAcPQSCazM0Bdq3hMiVOXdqqFQaXwYOwxiiLUBUZJ_hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های امشب محسن رضایی دیگر قطعی کرد که جمهوری اسلامی به دنبال زدن چاه ها و تاسیسات نفتی منطقه و نیز خط لوله های جایگزینی است که از سوی عرب ها و ترک ها دارد ساخته می شود.  منتظر نفت 130 دلاری باشید.</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/20182" target="_blank">📅 01:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20181">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">کری خوانی وزیر خزانه داری آمریکا برای عبدالناصر همتی:   به زودی دلار 300 هزار تومانی تحویلت می دهم</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SBoxxx/20181" target="_blank">📅 01:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20180">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCOmSggIPS0SAVWCPLi9NaSKw7S8EwYOL5HQmZmI2jY6miiJGrTuWFTGFL7g7QWogy1plSEhD1O0h7qfSfHw2U-IR9emWOs8wZe0cttlc1AmZ61z8JDOZRGgRsbcYKDL_FYUJB5wWiQinqRSPIyG8IAm7KGp3_N1jEvuoAGiCPKYKMIPrOJjAlThlOCm3svUrwnKTeY8LDLOOv-NX85ykNtgFFbdVMgJYrOTK2l8b-5hcjKI-_NQ8RJ7nSXaie8MklIrSEbVUr8AIo1-kQIjXLO9hp5PifgkORB-MhLQCJQQB4h5JMKHPFbx7ch2aYnXnyNqbRo2jNDn6Q5ZKVOE5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذخایر نفت خام آمریکا به سطحی پایین رسیده است که از دهه ۱۹۷۰ شاهد آن نبوده‌ایم.</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/20180" target="_blank">📅 23:53 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20179">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:  «امروز، وزارت خزانه‌داری ایالات متحده عملیات طرد اقتصادی، یک کمپین بی‌سابقه علیه جمهوری اسلامی ایران را آغاز کرده است.  ما در حال آغاز یک حمله اقتصادی علیه ارتباطات مالی ایران در سراسر جهان هستیم. هدف ما قطع هرگونه…</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SBoxxx/20179" target="_blank">📅 23:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20178">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3mxSpnYmXK4HwDE3Mo0YLg1nK2IYbtZXU3thkXZNziMnHBIYoKy6x1YViGwc-iwi8XRqaYr1tUiZDcqUqoMBuKD3YaXt65pSEIgLNfbBL-OkyHJ2Nbo_N-9dY9aDEXLW7EJs23B6agwqUeZrO7_oVyhtnmozl_478XikwAmdEjtKCkYsLXhCGGsz4tnsZh-uPv4PyV7U-bE9-pQzzUXddhryYn_V40gc0_-0-vrMlCaHTWHSkT8RSz84A38tyPOIfMEkQ9wtg21RYJSzWlAvr0ExcHy9RPns3YVR8AOH7PJ4fHwuEqIVG6WBl3br2No3QokQ278rMQS3WxngTahGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:  «امروز، وزارت خزانه‌داری ایالات متحده عملیات طرد اقتصادی، یک کمپین بی‌سابقه علیه جمهوری اسلامی ایران را آغاز کرده است.  ما در حال آغاز یک حمله اقتصادی علیه ارتباطات مالی ایران در سراسر جهان هستیم. هدف ما قطع هرگونه…</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/20178" target="_blank">📅 23:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20177">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده، درباره‌ی چین:  «ما می‌خواهیم امروز اینجا روشن کنیم که هیچ‌کس فراتر از دسترس تحریم‌های ایالات متحده نیست.  اگر آن‌ها تسهیل‌گر معاملات باشند و بخشی از اکوسیستمی باشند که نفت ایران را به پول و سرکوب تبدیل می‌کند، هدف…</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/20177" target="_blank">📅 21:57 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20176">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">نتانیاهو: ایران تلاش کرد یکی از پسرهایم را به قتل برساند
کانال ۱۲ اسرائیل: سانسور نظامی ماه‌ها انتشار جزئیات تلاش ایران برای ترور یکی از پسرهای نتانیاهو را ممنوع کرده بود.</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/20176" target="_blank">📅 21:39 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20175">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:  «خطاب به سربازان عادی حامی این رژیم: همچنان که حقوق‌هایتان بیشتر و بیشتر قطع می‌شود یا ظاهراً فقط به تعویق می‌افتد، از خود بپرسید که آیا فرماندهانتان کشورتان را برای پیروزی ترک می‌کنند یا برای ویرانی، و به یاد بیاورید…</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/20175" target="_blank">📅 21:26 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20174">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:  «ترامپ در حال برقراری تماس‌های تلفنی با رهبران جهان است و درخواست‌های مشخصی برای توقف تعاملات آنها با رژیم ایران دارد.  اکنون زمان آن رسیده است که رهبران جهان بین آمریکا و ایران تصمیم بگیرند.  هر نهادی که از طرف…</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/20174" target="_blank">📅 21:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20173">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:  «امروز، وزارت خزانه‌داری ایالات متحده عملیات طرد اقتصادی، یک کمپین بی‌سابقه علیه جمهوری اسلامی ایران را آغاز کرده است.  ما در حال آغاز یک حمله اقتصادی علیه ارتباطات مالی ایران در سراسر جهان هستیم. هدف ما قطع هرگونه…</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/20173" target="_blank">📅 21:24 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20172">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:
«امروز، وزارت خزانه‌داری ایالات متحده عملیات طرد اقتصادی، یک کمپین بی‌سابقه علیه جمهوری اسلامی ایران را آغاز کرده است.
ما در حال آغاز یک حمله اقتصادی علیه ارتباطات مالی ایران در سراسر جهان هستیم. هدف ما قطع هرگونه شریان اقتصادی است که این رژیم استبدادی را حفظ می‌کند تا زمانی که تهران به تنهایی بایستد.
از امروز، ما حلقه محاصره را تنگ‌تر کرده و هر منبع درآمد بالقوه‌ای را که سپاه پاسداران و رژیم ایران را تأمین مالی می‌کند، مسدود خواهیم کرد. ما در حال اجرای رویکرد «بدون نشت» هستیم.»</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/20172" target="_blank">📅 21:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20171">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">صحبت های امشب محسن رضایی دیگر قطعی کرد که جمهوری اسلامی به دنبال زدن چاه ها و تاسیسات نفتی منطقه و نیز خط لوله های جایگزینی است که از سوی عرب ها و ترک ها دارد ساخته می شود.  منتظر نفت 130 دلاری باشید.</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/20171" target="_blank">📅 18:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20170">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lB-F8t_gnmds70MwfYFqR2oGFAtx33yJmpHcGJsU5RfveIu35vnoUq1_gJhgTplyNHBYVuGMS9Juufy8BMwsR6lDveB2bA0G8kEJP4AyTkaPKOTxMMYo44wsKHGKhiQlGCx3ryfjoIU99JR62SGV-ltiBFdsx1EITPbTiK6kiyt7WVsz3v0s9DLoLbakwPA-QS7VAwIy5fuDbJeh6x-j3Ga1vi47c_QL3Px55FtGwt3_TQqsapwgvc33BpWfcpsBGikq6P3BfsTgXxHyOOVaGEfFd-yx9KGv8o5rbatGc8mvsZtckdQthjmS-1cEtmXxsm0LxPQeUnqMv2Yxc6-6YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواننده Secret Box از 2.5 ماه پیش میداند که هدف درگیر کردن ترکیه چیست. بزودی یونان هم به اسرائیل خواهدپیوست.</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/20170" target="_blank">📅 18:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20169">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">جلسه گذاشته اند برای بررسی وضعیت صنعت برق کشور بعد در همین جلسه برق رفته !</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/20169" target="_blank">📅 18:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20168">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">جلسه گذاشته اند برای بررسی وضعیت صنعت برق کشور بعد در همین جلسه برق رفته !</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/20168" target="_blank">📅 18:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20167">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c94f2d5d3.mp4?token=h-c2ylFpJNVxzvYv8nsPcOG5JrjvIUti0cpxEOP1DACZp_Myrj5GDC0AzU8xYB-ePotd5RFPe_G3fGX19_74SD-wLnaq38-DNjDGcGM0tOrOnDjWnAafEAECGBfLsYI-nLPgm_HLz7HEjaveLEUrvyYbo9tfIg9o6IRG8SqPnC6XaD6IwHDU2vaYB5mjoPvqvkAJMd1e1ZAAPV5XfXkUbtpOe4MaLNbtKz_UlJ-yCro-RPT4k4t9YhdIYcZaBZdh42ArQlJ9yJjKp-pveMI-YNI_Cm3NTqvwERR4v6Wdi3mKX_KbMU6lKMZ6epi3oL1EfyWgXDpBlj4TOTEqNCO9CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c94f2d5d3.mp4?token=h-c2ylFpJNVxzvYv8nsPcOG5JrjvIUti0cpxEOP1DACZp_Myrj5GDC0AzU8xYB-ePotd5RFPe_G3fGX19_74SD-wLnaq38-DNjDGcGM0tOrOnDjWnAafEAECGBfLsYI-nLPgm_HLz7HEjaveLEUrvyYbo9tfIg9o6IRG8SqPnC6XaD6IwHDU2vaYB5mjoPvqvkAJMd1e1ZAAPV5XfXkUbtpOe4MaLNbtKz_UlJ-yCro-RPT4k4t9YhdIYcZaBZdh42ArQlJ9yJjKp-pveMI-YNI_Cm3NTqvwERR4v6Wdi3mKX_KbMU6lKMZ6epi3oL1EfyWgXDpBlj4TOTEqNCO9CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:  ایران به صورت کامل در‌ حال فروپاشی است.</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/20167" target="_blank">📅 16:21 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20166">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxAg5PqcZ2imTzc-pIheUJ6dn8-GcoK5w0Xc1shL_dhkVRYGz-51hKe1Y8dDKQK33sd-c9b1Xkqao2tXnMRbIdKF9iOJAXUDDJ2MKC3uytTVnApT4GjNbN5xD7C3Uf3dtMJiV6819lcCpnvbfDiOpLhZ3wLuZ6ZurTBG7MvbHrsnInF-CTN_FIIdMexRBZfVaoU9cBVBsnxJg4XwOqNRc60Phbo5AJOdt0MkJQF4kkwCRk2XnCWSPIJy1qnvGmTJ86xKbCzh9JVBINXh_Los6wIxCOnwrd-cUFarF0DzWsFhJanhzbp1hjl7nuhEyZ7zKiXcVtBTfnPHyM3bk7NcIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
ایران به صورت کامل در‌ حال فروپاشی است.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/20166" target="_blank">📅 16:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20165">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">وزیر سابق دفاع اسرائیل، یوآو گالانت، درباره ترکیه:
باید درک کنید که وقتی ایران تضعیف می‌شود، آن خلأ توسط کسی پر خواهد شد.
نامزد طبیعی، با آرزوهای امپراتوری در خاورمیانه، ترکیه است.
ترکیه یک کشور قوی با میراث امپراتوری است. آن در پل میان آسیا و اروپا قرار دارد.
آن بزرگ‌ترین ارتش ناتو را به جز آمریکایی‌ها دارد، یک صنعت دفاعی بسیار قوی، مردمی سخت‌کوش و در عمل یکی از مناطق اصلی صنعتی اروپا است.</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/20165" target="_blank">📅 16:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20164">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9HAM8uNYiEYBUxq1V3bFh_kKA88EgZ5DQn8ywWbzcR2xOno7WemDyftxNRV-ZQVPW2hUA5AV1K3lp0Py0yuWlt6l1cjzODcHQDo-9vygW_mJCgy24NhFcKqDvLUdgvfs5w8FTAkpfmOdTdarWQsAW1WjZM5aDsKt0Weh5Uz5tDeKDsxpK8jG1_fRBFOhu4IjJMvqCjQ7sVEGBLVx1voEr1D8O4R8CbNsHnIkYjpzPVDfXfX0X3xDjzGf_Bt017xzZmGD_PmaEG-vT_zlPFprNfIi3fg9uuxOBgMjpqD3EGQv1BMWiPs-CR17P7KZttQPBAiqLKStfkURXtO-jD97A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موشک PL-15 و تحول در نیروی هوایی مصر  همانطور که در یادداشت پیشین گفتم، محدودیتهای شدید اعمال شده روی تامین موشک های دوربرد هوا به هوا برای مصر از سوی غربی ها، مصر را به خرید جنگنده J-10 CE چینی واداشته که مجهز به موشک دوربرد PL-15 است.  اما این موشک چه ویژگی…</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/20164" target="_blank">📅 14:00 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20163">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">Secret Box
pinned «
این بسته جدید بسنت سروصدایش بیشتر از تاثیرش خواهدبود.  چین اگر بخواهد — که به نظرم می خواهد — به هر قمیتی از سقوط کامل اقتصاد ایران جلو میگیرد و همه ابزارهایش را هم دارد که اینجا اشاره کردم.  کالاهای موردنیاز ایران را کماکان تا جای امکان صادر می کند و پولی…
»</div>
<div class="tg-footer"><a href="https://t.me/SBoxxx/20163" target="_blank">📅 13:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20162">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">هر وقت پاکستان میانجیگری میکند یک جایی ازشان منفجر می شود</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/20162" target="_blank">📅 12:59 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20161">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bded5954b1.mp4?token=AHhtxqhv0Y01zYYjs1JQZEqrpValHPB-LJWQdVP5nGCWrxLpOHVlyt9kV1r2J78ZmHltrWbm4jBCMH7Uhf1HJCZ9-pBv_iM6XUpaY1N0B3Ri4Ylh-bNPI33p5_0fLesqtR5XK_CgUEmgx3v0BoYMzMLA1IfkW0Z_RE6S16dFtrXotQUex1OiKVEVw7lWW7Aerj8SMazwlwthvofq9FaTuJmodnlrHFcDDB4o32-cZq7EgeA1ZJuDcEZ-uTy43ryUmtOJZNwEyol26nA5UnVQfWWraNne9cmVTZLRLDZgeZJy0tQQy4bVWc9tiCf-5xJ4x13jgUZPKfwjABrGHmW0dojdpAWeGgsOMtTc49wdlkbYMHUy_Hx8FeoDSYN1WT9ELOYknc-7ZkcRP5hD3CPbSUvlj7zxpt_Ax1liZsn04qlwWn0b50WirAo0nOY0rhPr6_Wge3SHlvAGdlZjYGLOhsXvzzWx8AJ6L4rNLPJ_lf1VUbWoPg8Fz2rZeQziAe1IUG5RypRF-a89ruA7-dFmrjQXxK2RwJ0ROgu9p5IdxCwywIxOSrZbeNw5ZBCa9M2uwUipoAcEgElsk1TQV0lMU7txlJcNAntcf4Rolx1yOQQS2i0wUwfFcSsm3enfsqbZ3lW0Uscr1t9dvZ1-KVr1ya2yu8G9pPhs1YVRgUb9QxM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bded5954b1.mp4?token=AHhtxqhv0Y01zYYjs1JQZEqrpValHPB-LJWQdVP5nGCWrxLpOHVlyt9kV1r2J78ZmHltrWbm4jBCMH7Uhf1HJCZ9-pBv_iM6XUpaY1N0B3Ri4Ylh-bNPI33p5_0fLesqtR5XK_CgUEmgx3v0BoYMzMLA1IfkW0Z_RE6S16dFtrXotQUex1OiKVEVw7lWW7Aerj8SMazwlwthvofq9FaTuJmodnlrHFcDDB4o32-cZq7EgeA1ZJuDcEZ-uTy43ryUmtOJZNwEyol26nA5UnVQfWWraNne9cmVTZLRLDZgeZJy0tQQy4bVWc9tiCf-5xJ4x13jgUZPKfwjABrGHmW0dojdpAWeGgsOMtTc49wdlkbYMHUy_Hx8FeoDSYN1WT9ELOYknc-7ZkcRP5hD3CPbSUvlj7zxpt_Ax1liZsn04qlwWn0b50WirAo0nOY0rhPr6_Wge3SHlvAGdlZjYGLOhsXvzzWx8AJ6L4rNLPJ_lf1VUbWoPg8Fz2rZeQziAe1IUG5RypRF-a89ruA7-dFmrjQXxK2RwJ0ROgu9p5IdxCwywIxOSrZbeNw5ZBCa9M2uwUipoAcEgElsk1TQV0lMU7txlJcNAntcf4Rolx1yOQQS2i0wUwfFcSsm3enfsqbZ3lW0Uscr1t9dvZ1-KVr1ya2yu8G9pPhs1YVRgUb9QxM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در حالی که ‌وزیر کشور پاکستان در ایران است تا معامله تمدید آتش بس میان ایران و آمریکا را جوش بدهد، شهر دالبندین در این کشور بدست جدایی خواهان بلوچ سقوط کرد!</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/20161" target="_blank">📅 12:58 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20160">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترور یک مامور فراجا در ایرانشهر  به گزارش مرکز اطلاع‌ر‌سانی پلیس سیستان و بلوچستان، ساعتی قبل افرادی مسلح به سمت مأمور انتظامی در ایرانشهر با سلاح گرم تیراندازی کردند که در پی این اقدام، استوار یکم «مهران سالارزاده» به درجه رفیع شهادت نائل شد.</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/20160" target="_blank">📅 12:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20159">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ic7QItOoW92afJz5Bq4AWE_UTT1ccFr88AvZNSa-fzXUMBOwDCiNsHTMiMs641OvEn0X2QiHdwjxZ_IB2hPSnnW-j5E8BOGqRRFkldlFu0nqq_NSKUwROPM_lsHDqkhNW96lW6tscI9j5KMepVzMpyCbOfsLTJcuuYWzUaEvp4VQnc9EKIbnWdEyrnpI_JSOMtprYPRuKfBySsd9XCBmYbCfbaEdysWoPdyc5_lPwpFvA2oR13iQ1UCQvLmr3O5Ay4gMtFVVe6t0cA0HULbs5G1IuXSrOO1M8-9karvG-_aE5k7pzZaEXIy3wgDp_Q1hKQkTbLm5vNbT-t5eYI4n5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس بانک مرکزی:
مشکلی برای تأمین ارز نداریم و هر کارآفرین هرچقدر اسکناس بخواهد تأمین می‌کنیم</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/20159" target="_blank">📅 12:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20158">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3e31f970d.mp4?token=fIop_gzlHOo2yFukFJRsErRD2u7Z853RnRp_InpQDQKyfadS50N7n6ayn3Omjovg-ODmS_Flyyc6ZjzT0gr1-D6djYIfDHULyGRTsfr0o1HVMNKx6SZwA0SrBDuF0s5DhJ-I08v6ie2t4IGBmzOyhQCOlvtGIHnfcUiJlgfm-O46_MR8SJVfgR_sKf2aIFEg9kiOT9RzORofBq9UyC8H4y13QDHfvQQ68YMa46RDFM8Bv3AO0dvKIu4HKvxiETERyNuPXMARHQ4XLU5SqMg_7PdUJXfaGGiRseuW-1aFZkCBTrfZwcHVJevoGAPCDY0WRvnwODvBTlzhb0bRjChotg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3e31f970d.mp4?token=fIop_gzlHOo2yFukFJRsErRD2u7Z853RnRp_InpQDQKyfadS50N7n6ayn3Omjovg-ODmS_Flyyc6ZjzT0gr1-D6djYIfDHULyGRTsfr0o1HVMNKx6SZwA0SrBDuF0s5DhJ-I08v6ie2t4IGBmzOyhQCOlvtGIHnfcUiJlgfm-O46_MR8SJVfgR_sKf2aIFEg9kiOT9RzORofBq9UyC8H4y13QDHfvQQ68YMa46RDFM8Bv3AO0dvKIu4HKvxiETERyNuPXMARHQ4XLU5SqMg_7PdUJXfaGGiRseuW-1aFZkCBTrfZwcHVJevoGAPCDY0WRvnwODvBTlzhb0bRjChotg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این بسته جدید بسنت سروصدایش بیشتر از تاثیرش خواهدبود.  چین اگر بخواهد — که به نظرم می خواهد — به هر قمیتی از سقوط کامل اقتصاد ایران جلو میگیرد و همه ابزارهایش را هم دارد که اینجا اشاره کردم.  کالاهای موردنیاز ایران را کماکان تا جای امکان صادر می کند و پولی…</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/20158" target="_blank">📅 12:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20157">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">درباره اینکه پول خرید واردات چطور پرداخت بشود نیز با توجه به اینکه ایران کشوری با بدهی پایین است، شاید چینی ها به دلیل نقشی که ایران دارد روی فشار بر مالیه و توان نظامی آمریکا وارد می کند، خطوط اعتباری درنظر بگیرند که بعداً (مثلاً بعد از رفتن ترامپ) تسویه بشود.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/20157" target="_blank">📅 12:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20156">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">عاصم منیر به تهران آمد.</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/20156" target="_blank">📅 12:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20155">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا مدعی شد:  امروز صبح بزرگترین حمله مالی تاریخ علیه ایران را آغاز خواهیم کرد  روز تسویه حساب اقتصادی ایران نزدیک است  هدف ما قطع تمام شریان‌های اقتصادی است که ایران را سرپا نگه می‌دارد.  جایگزین برای کشورهایی که سرنوشت خود را به تهران…</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/20155" target="_blank">📅 12:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20154">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HS8K_ytVGllDMi8AHg0hchd1hrBynQQvQOzEtt_V8jSD9SwkL1s2lkm3X-VCcJgUV1K4n-GZlwO4gHLkJGbCFggOg0MKnC7lY2GMufaZoQ6iErVgGKIKb9HmHbW4C2xHgIJfzO1V1OLW2SRt7RLZfpw0Wc-nhwAEiyfrG7xdPJBSBb2lCI3OQtY8loXa1369xuAlW0BPRBs16aA2LL_H1qzdq-lmoD1t56OEtym-Uv_EhOxB4hFnot89mx2tpNUez5eycDtLx9lkVzoL5LOq94oco5nU_QwsRgF_qrq184v8Psre7_TFJWGSG36srUzfz7XiQdasnK9Oms0_WFHUqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز گزارش داده که صادرات نفت ایران در اوت به حدود
۵۳۴ هزار بشکه در روز
کاهش یافته، در حالی که میانگین سال ۲۰۲۵ حدود
۱.۴ میلیون بشکه در روز
بوده است</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/20154" target="_blank">📅 11:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20153">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ما بیشتر تیله بازان خوبی هستیم به نظرم.</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/20153" target="_blank">📅 11:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20152">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">فعلاً این یادداشت را بخوانید؛ توضیحاتی درباره برنامه بازخرید اوراق قرضه که هفته پیش اعلام شد و سناریوهای پیش روی طلا ارائه داده ام.</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/20152" target="_blank">📅 11:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20151">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AAeNl3U84nkxSskODNFATwE21KBFuyxxQuuI14sa7WJyQQPbmRPumvpBwWHx7r-1zAxhSEuUb86jYXto19VDwIc6MDfiD2pc13IK-rGSXGrkMtZIXxQl9neTDyjbiV17-ORm52TzT6dw3EHQsvQBzwQyh1uqWjVaxRo3XS0KryLCkdqVSod4jut-CHQK1bVK8pHv_DwztjWHfSRVkpHZjoptqxrsfY_nM7TNFFunWAv0cK3doiCoaCnminZYdB9_4WOy4Jp8PNl9nN6SdsyufJL5miM7OjyM4kr2kxpDNVryy9z6sKxmQJnkzg1AahRhsh6NgLWjWHL-Mc96EAyEjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح بسیار بالایی قرار دارد.
دقت کنید که با آغاز برنامه بازخرید اوراق قرضه بلندمدت خزانه داری آمریکا، یک عامل جدید وارد محاسبات شده که در این شاخص هنوز آن را دخیل نکرده ایم که روی طلا موثر است.
ولی با این حال، پیش بینی می شود که شاخص های سهام امروز زیر فشار فروش بالایی بروند و نفت هم احتمال زیاد صعودی باشد.
برای طلا، احتمالاً از مومنتوم صعودی کاسته بشود و اصلاح داشته باشیم اما به یاد داشته باشید که اقدام اخیر خزانه داری زمینه بنیادی طلا را تغییر داده است و از این پس، معیار موفقیت شاخص GRI را روی دارایی های کاملاً ریسکی مانند شاخص های سهام تعریف میکنیم.</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/20151" target="_blank">📅 11:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20150">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qiq4Tc4PGI9lStBaJ22DhhHFDVMNyWD-Zl-i37W9SXaUlJeXXV4h6M58TP4qo5STmWszg6LXLRXqUJnYO535887jgLOc7dtnePMrc2mt_Id_YHcC4hk4zQVvxenaOrE0vfcjdCvcgdUIBcsvXuRzvgAfY4dQHNpiqWZDSZW3T53xfXTNelxeLmve2k5gTPLBB3eIooFOJJQS4BTVEKXTzQfklyZ0ZD22ZJ4bGsFblrbUzGdAK7POdfBPzzJ4f4o3yDjbYfW3h5ziV5eJpT1rMxcLk7hkHgGYf4wNwV8UDDtKfTYcEEsXdv2yXgg6XXP5S9r2EqqniqzG-XHfkwIjaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هدف قرار گرفتن یک کشتی نفت کش در نزدیکی بندر ینبع عربستان</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/20150" target="_blank">📅 11:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20149">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا مدعی شد:
امروز صبح بزرگترین حمله مالی تاریخ علیه ایران را آغاز خواهیم کرد
روز تسویه حساب اقتصادی ایران نزدیک است
هدف ما قطع تمام شریان‌های اقتصادی است که ایران را سرپا نگه می‌دارد.
جایگزین برای کشورهایی که سرنوشت خود را به تهران گره می‌زنند، بسته شدن هرگونه مسیری به سوی رفاه پایدار است.
هر کشوری که به عنوان شریان مالی برای یک نظام رو به زوال عمل کند، باید انتظار داشته باشد که انزوا را با آن تقسیم کند.</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/20149" target="_blank">📅 10:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20148">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">یک مقاله در روزنامه اورشلیم پست اسرائیل خواستار آن شده است که اسرائیل، ترکیه را به عنوان یک تهدید نظامی در سطح ایران در نظر بگیرد، و این جمله تحریک‌آمیز را مطرح کرده است:  از ادلب تا استانبول، اسرائیل در صورت لزوم، حمله خواهد کرد، نه اینکه دفاع کند.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/20148" target="_blank">📅 01:34 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20147">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-aKjcTbyrG958h9XqnKegjgDqVBT8uATxafdAeYdqGOcM-E4WTQ6XWDV99X3o_7uYQd57yd2EjoaE2tC3lp7gUlK_QIRrBoQxlzQYTYK-HgYwy3aWT6GTt59G5JzToSrlszZs7egYAX0HbMXSOSfZf948FT0QvP0BbnQMgF-lzozu_lCv7NtvXwW4JYzI0LpmwFtYW7glk698CTO3t9GPnCH2rxjuEuEkclV6ntwHi7IyhwGuyKe4SlDciM4jHHQGKHK4xXCcN3Q8rJWJ76DHT8kuCn3bFiuKNsWCFHFgr-BqbJf2YCjv4cH9CXNNvPEBZeCiphD7UqP-3CGbHWXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مرندی:
در روزهای آینده، درگیری نظامی به احتمال زیاد دوباره شعله‌ور خواهد شد.
با هر رژیمی که با ترامپ برای گرسنگی دادن به شهروندان ایرانی همکاری کرده باشد، به شدت برخورد خواهد شد. اقتصاد جهانی در آستانه سقوط است.</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SBoxxx/20147" target="_blank">📅 22:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20146">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c36a2627a.mp4?token=SdSgoUtmoDGHanoPGXEjILhcTenbhqfUZU84e_vlzakxUbTwooKoHTd2-GjAwpsE6VdPaBKdKtmDmwFF06YodhflEH_Du7RBpN1y6K05tkYrQwB8otf3Y00UpCIhsNUfpQ_U7avljTyL0a8GMNV5bQmmnw0duwRDyVBWKWIrJKNZU5uElebWdRagdjPABVs_dMLkIXbhN7HUjzZl8m88XBnXHM46sTz_osGO2re89RQlDaIsg95dh9zgjYnJNBYNzfi3AXK5Bu_d4QNgCoSbbYmpn7kA6PybG9N4rbE7JQH0eydTbKL33MvCZ8f5GPDFCraZCAGrFn7X61rQtFp7dYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c36a2627a.mp4?token=SdSgoUtmoDGHanoPGXEjILhcTenbhqfUZU84e_vlzakxUbTwooKoHTd2-GjAwpsE6VdPaBKdKtmDmwFF06YodhflEH_Du7RBpN1y6K05tkYrQwB8otf3Y00UpCIhsNUfpQ_U7avljTyL0a8GMNV5bQmmnw0duwRDyVBWKWIrJKNZU5uElebWdRagdjPABVs_dMLkIXbhN7HUjzZl8m88XBnXHM46sTz_osGO2re89RQlDaIsg95dh9zgjYnJNBYNzfi3AXK5Bu_d4QNgCoSbbYmpn7kA6PybG9N4rbE7JQH0eydTbKL33MvCZ8f5GPDFCraZCAGrFn7X61rQtFp7dYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر نیرو:   این هفته خاموشی‌ها تمام می‌شود</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SBoxxx/20146" target="_blank">📅 21:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20145">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">وزیر نیرو:
این هفته خاموشی‌ها تمام می‌شود</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/20145" target="_blank">📅 21:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20144">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/20144" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">یک صوتی مفصل در این خصوص خواهم داد.</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/20144" target="_blank">📅 19:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20143">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">آیا صادرات نفت ایران از مسیر ریلی می‌تواند جایگزین صادرات دریایی شود؟   در هفته‌های اخیر گزارش‌هایی منتشر شده مبنی بر اینکه ایران در حال بررسی استفاده از مسیرهای ریلی برای انتقال نفت خود به چین، به‌ویژه از طریق خاک افغانستان و آسیای مرکزی، است. این ایده در…</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/20143" target="_blank">📅 17:48 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20142">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/un1OQiVtuxdC0VDRhfUh7dTSEF3H_SjON1ii4JokdQO92NtTxIwqYdYGIhCFN7sbKiBbAHJ9ZsI7VoupWAi-Gp5PZwNQ0hrZCzn1uJWKer3uMhSC4_Q9xVBF2ZS9qXqJJLqdZiOyKAPweZYEDwhE72XImULKxW7QX8Q8G3Q6vO0BfVZ4omDHS6INy5uga-Hj7auMqolE-TUzXNOVUSuLicKevGGJcN5fEBM2blgexKS4rwRhS-xkjlyo4X2kL9FAu2P9JXIJxRX5bDG7kWRpr9dc0v9JywDG4Bnt0hXJjHlzKddtOi0LiMcM1X15b4uzYsal3vTLUrQAgzfXkLHeKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتصال ریلی ایران و چین
پس از آغاز نخستین محاصره بنادر ایران در
۱۳ آوریل
، حمل‌ونقل ریلی کالا از
شی‌آن چین به تهران
افزایش یافته و تعداد قطارهای باری این مسیر از حدود یک قطار در هفته به یک قطار در هر
سه تا چهار روز
رسیده است.
این مسیر ریلی پیش از آغاز بحران نیز فعال بود.
نخستین قطار باری مستقیم از شی‌آن در
۲۵ مه ۲۰۲۵
در بندر خشک
آپِرین (Aprin)
در نزدیکی تهران تخلیه بار کرد. بنابراین، مسیر مذکور پیش از اعمال فشارهای دریایی ایجاد شده بود.
مسیر قطار از
قزاقستان و ترکمنستان
عبور می‌کند و سپس وارد ایران می‌شود و به آپرین می‌رسد. در این مرکز، محموله‌ها ترخیص شده و برای توزیع در سراسر کشور ارسال می‌شوند. حمل بار از این مسیر ریلی حدود
۱۳ تا ۱۶ روز
زمان می‌برد، در حالی که حمل دریایی در شرایط عادی حدود
۳۰ تا ۴۵ روز
طول می‌کشد.
افزایش تقاضا برای این مسیر هزینه حمل را نیز بالا برده است. قیمت حمل یک کانتینر ۴۰ فوتی در ماه مه به حدود
۷ هزار دلار
رسید که تقریباً ۴۰ درصد بیشتر از سطح معمول بود.
هر قطار حدود
۵۰ کانتینر
حمل می‌کند. محموله‌ها عمدتاً شامل قطعات خودرو، ژنراتورها، تجهیزات الکترونیکی و سایر کالاهای صنعتی و مصرفی هستند. قطارهای برگشتی که با ظرفیت پایین حرکت می‌کنند نیز هزینه حمل در مسیر غرب را افزایش می‌دهند.
بااین‌حال، ظرفیت ریلی قابل مقایسه با تجارت دریایی نیست. یک کشتی کانتینری بزرگ می‌تواند هزاران کانتینر حمل کند و انتقال نفت خام یا سایر محموله‌های فله‌ای در مسافت حدود
۱۰٬۴۰۰ کیلومتر
از طریق راه‌آهن از نظر اقتصادی مقرون‌به‌صرفه نیست.
در نتیجه، این کریدور ریلی نمی‌تواند تجارت نفت ایران پیش از محاصره را احیا کند یا جایگزین دسترسی آزاد به بنادر شود.
پس از آنکه آمریکا نخستین محاصره را در
۱۸ ژوئن
لغو کرد، این محاصره در
۱۴ ژوئیه
دوباره برقرار شد و اهمیت مسیر ریلی به‌عنوان یک کانال جایگزین افزایش یافت.
ایران همچنین از مسیرهای زمینی و ریلی دیگری استفاده می‌کند. خطوط ریلی در شمال به سمت
روسیه
امتداد دارند و گذرگاه‌های زمینی در شرق نیز امکان ارتباط با
پاکستان
را فراهم می‌کنند.
هیچ‌یک از این مسیرها از نظر حجم قابل مقایسه با حمل‌ونقل دریایی از طریق خلیج فارس نیستند، اما امکان انتقال بخشی از کالاهای مورد نیاز ایران از طریق مسیرهای زمینی و ریلی را فراهم می‌کنند
.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/20142" target="_blank">📅 17:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20141">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">برخی اخبار تاییدنشده خبر از سفر عاصم منیر به تهران می دهند.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/20141" target="_blank">📅 16:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20137">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">انسان‌ها_بحث_درباره_خودآگاهی_هوش_مصنوعی_را_برعکس_در_نظر_می‌گیرند.pdf</div>
  <div class="tg-doc-extra">328.9 KB</div>
</div>
<a href="https://t.me/SBoxxx/20137" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">یک بحثی که وجود دارد اینکه یک مدل «رایانش قهری زیستی» هم مدنظر ممکن است قرار بگیرد. (Forceful Biological Computing) که در آن مغز یک انسان بدون رضایت خودش از طریق کاشت ابزارهای خاصی (نانورباتها یا ....) در اختیار یک شرکت پردازشگر هوش مصنوعی قرار بگیرد.  در…</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/20137" target="_blank">📅 15:57 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20136">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ترکیه، فاکستان، عربستان، ایران، بنگلادش!  به نظرم اسمش را پیمان «جده» بگذارند بهتر است.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/20136" target="_blank">📅 15:47 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20135">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">المیادین به نقل از یه مقام ایرانی:   از ایران برای پیوستن به "توافق مکه" دعوت شده و تهران الان دارد این موضوع را بررسی می‌کند!</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20135" target="_blank">📅 14:29 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20134">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">المیادین به نقل از یه مقام ایرانی:
از ایران برای پیوستن به "توافق مکه" دعوت شده و تهران الان دارد این موضوع را بررسی می‌کند!</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/20134" target="_blank">📅 14:02 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20132">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RuyQyAKkt_E5GTqtVvUT7OTsK_XH9lIsKVUKCpcPaslUXuOvp_2Z7HcWTVQMILHT6LoExKGRO9pMHLdkBwg1nPfrj4zgZEHH-wgukltWHxFCS8TtBv7lUX62y_Fb6wFz8l1KqP_Mc6YUea-Wa02glrhqWNYyi7SW3IOrzHHaCmnCJWay4ljt7zJsAZgxGgzkT_UDfGW_WW3NZKRtVS1nByBqn23f2ej-n9juqEr5T93oIOkTu1xe61e11j7mBzWQb8HZDl1RgsLj1m74oG25eYvdobtKfUEkmtndOinDSS5CRAL0yb4tOZCpRpcYBCTIpMRQxwUWY67fE_3Z-mO86w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04647b5b32.mp4?token=JoDiwzjR6sb9fIJYc-d9TkLQnS89OI1hhyGCocIdZiAICTRfsuHUdY7sGvxQyLfgOXdH9csBjxUHi5b6ZkrrHaJFlJk5DnCA0mtYtFsL-8Y9USjaXgD38cBaTUAfdrhD6vKIgxh1VjmGA5tNb3x3UQ6tf7UtPhrcO1QLNiyopthlIrPkOZ7bIzvZZS32acRQmdtDUo6uibiS_W6DPZ6Cqi-t-OHBmOT8QdI3Nmy5mU9aNGYa7jPaV9jw1XsQ801pfDaVNFa1IA_0pPO_K2kH8_0F9qcameZj9E-s1BILFz0vaewACmy5dSbUFxC95XO3QTtwZXkV7oRBa0uV_w07_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04647b5b32.mp4?token=JoDiwzjR6sb9fIJYc-d9TkLQnS89OI1hhyGCocIdZiAICTRfsuHUdY7sGvxQyLfgOXdH9csBjxUHi5b6ZkrrHaJFlJk5DnCA0mtYtFsL-8Y9USjaXgD38cBaTUAfdrhD6vKIgxh1VjmGA5tNb3x3UQ6tf7UtPhrcO1QLNiyopthlIrPkOZ7bIzvZZS32acRQmdtDUo6uibiS_W6DPZ6Cqi-t-OHBmOT8QdI3Nmy5mU9aNGYa7jPaV9jw1XsQ801pfDaVNFa1IA_0pPO_K2kH8_0F9qcameZj9E-s1BILFz0vaewACmy5dSbUFxC95XO3QTtwZXkV7oRBa0uV_w07_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاریکاتور اکونومیست با عنوان «کمبود رهگیرها» تصویری طنزآمیز اما هشداردهنده از یکی از مهم‌ترین آسیب‌پذیری‌های جنگ‌های مدرن ارائه می‌کند یعنی محدود بودن ذخایر موشک‌های پدافندی در برابر حجم بالای حملات موشکی و پهپادی.
در تصویر، سربازانی که ظاهراً نماینده آمریکاییها و متحدانشان هستند، در حالی که تعداد زیادی تیر دشمن ایرانی در سپرهایشان فرو رفته، زیر بارانی از تیرهای دیگر گرفتار شده‌اند.
دیالوگ بالای تصویر نیز به‌صراحت می‌گوید که جهان به رهگیرهای بیشتری نیاز دارد، اما بخش بزرگی از ذخایر موجود برای دفاع از آسمان خاورمیانه مصرف شده است.
نکته جالب‌تر، شباهت بسیار آشکار ترکیب‌بندی تصویر به صحنه معروف فیلم
300
است؛ جایی که سربازان اسپارتی در برابر سپاه عظیم ایران هخامنشی، زیر باران تیرهای پرشمار، سپرهای خود را بالا می‌برند. این ارجاع تاریخی، پیام کاریکاتور را تقویت می‌کند: مدافعان امروزی نیز با وجود فناوری پیشرفته، در برابر «اشباع» شدن سامانه‌های دفاعی با همان مسئله‌ای روبه‌رو هستند که سربازان اسپارتی به‌صورت نمادین با آن مواجه بودند.
طنز پایانی تصویر نیز تلخ است: سرباز سمت راست می‌گوید «امیدوارم دیگر چنین اشتباهی نکنیم»؛ اشاره‌ای به این واقعیت که مصرف سریع رهگیرها می‌تواند در جنگی طولانی، خود به یک بحران راهبردی تبدیل شود.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/20132" target="_blank">📅 08:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20131">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">خب دیگر بس است بخوابیم.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/20131" target="_blank">📅 01:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20130">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">هر ایرانی در سال یک بار معتاد بشود و 2 بار ترک کند تا اینطوری تعداد معتادان کشور کاهش یابد و وابستگی کشور به تریاک وارداتی کاهش یافته و صرفه جویی ارزی کنیم.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/20130" target="_blank">📅 01:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20129">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">هر خانواده ایرانی در خانه اش یک نفر را به عنوان سرباز آمریکایی اعلام کند تا ما دستگیرش کنیم و به آن خانواده 30 هزار دلار بدهیم.</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/20129" target="_blank">📅 01:27 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20128">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">مردم در خانه شان تنگه های هرمز پرورش بدهند تا ببندیم و از کشتی های عبوری عوارض بگیریم!</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/20128" target="_blank">📅 01:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20127">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewec8XzAP9cvmBQ2KanbX3HJ7UJVDGYBErsP54Vteul0FyJyJbmmoBYkUoCUsMd9LOOYU6yP5DeHXEqakG_EAb7TT2hu4saqy6bIiVohoQLJWaFW0YWJ9CQucCd3xCl4gye31nwK_-HNKxLi5UKakkWv3ORIHX5Ae6x6hVWHHURle-0G9t2KEgnH6UhV5WuiT4nAFQPDPnOId4dvsukNLBuT6c8xY-j5gsJzQxcpM1keRo9edIaQbOgcFsNeq3L1cLl0Vwn7FuYI7akRoWHQG-4AUf_x9ZOxgSr5taUVM5kMm1ScBz8UuOTphxq_H3EtDihg2256D6UYIaslGCLBjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب گیری کردیم به حضرت عباس!</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/20127" target="_blank">📅 01:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20126">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owiWOeFtCcbJhDpeTf21B_jK9WT2Jjrkme-ty23E6eb2as2Kh4G1Ed-EpOBhjJFWnJ5TBOfWfIQjN9T2Vhs7z4aTbS5nfwi0ReN2STmTisu-tXYyKLdgL3z3SvJ3oD-zFVo9lvdhc6NA9UZL9tvNnjCaRia9JElSxn0e_t1HIJri1IX6HU7alknsJDE7LlCoOZOEUBHFUFkwFXeGvjeWTCGzEg40zshU-sdGNwzGNKcgWx5so4oa2e707xPzE8EJtaTiqGgWAtqvBuQyA-TVdmrqarzg5oQApvG3_BKpIOYnN9c8eLa3fROhWViFRN7s37uTPZibMhgsrzmNG5K-WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاربران اسرائیلی با انتشار این تصویر، به تهدید اردوغان پرداختند.  جالب است که این تصویر شباهت بسیاری به صحنه دستگیر کردن عبدالله اوجالان رهبر PKK دارد که اتفاقاً با کمک مستقیم موساد صورت گرفت.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/20126" target="_blank">📅 00:54 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20125">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPWDZ2iwiqpvUsWeuSFFaqov3SXmPceJ-d9xGMp8l3ciwq0XfXKRFR-26AQZbgPrhq_85_2xNp5HbFo14k-pNWIWiIw1tVY5f-6dqIf89J6AP19SSyHreyAb3gsGaC5lk5dhZgwGc1V_GSM2peCRfd9_h8oSCcUF9b-fWvHD7b2e-Blx3NiNiRQ7OpJqw5yRytyQh4p1rU_HeQqHXHMoDOJa1wGZC7i58tJDee31JfOOrdmGLErXkQn48KZgTptH7dxzCxCYH5MUkLu3q0gPyn4fCuNI-h6gA5H2hMITs2ko39Vt6Tk-UX_jaz6qFj6zTqsPqx_IGCiGmlg46ktC8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاربران اسرائیلی با انتشار این تصویر، به تهدید اردوغان پرداختند.
جالب است که این تصویر شباهت بسیاری به صحنه دستگیر کردن عبدالله اوجالان رهبر PKK دارد که اتفاقاً با کمک مستقیم موساد صورت گرفت.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/20125" target="_blank">📅 00:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20124">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">به‌نظر می‌رسد در درون ساختار قدرت جمهوری اسلامی، شکاف میان جناح میانه رو و جریان تندرو و ضد امتیاز، در حال برجسته‌تر شدن است.   اگرچه این شکاف هنوز به تغییر رسمی سیاست حکومت منجر نشده، اما اظهارات اخیر دکتر پزشکیان، محمدباقر قالیباف و عبدالناصر همتی نشان می‌دهد…</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/20124" target="_blank">📅 00:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20123">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">به نظر من جمهوری اسلامی بزودی گزینه آخرالزمانی حمله به چاههای نفت و تاسیسات انرژی منطقه را فعال خواهدکرد که در پی آن نفت به بالای ۱۳۰ دلار و طلا به زیر ۴۰۰۰ دلار خواهندرفت.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20123" target="_blank">📅 00:48 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20122">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">مردم فلافل بخورند و در خانه شان نیروگاه بادی راه بیاندازند</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/20122" target="_blank">📅 00:47 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20121">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGOSHs_7lRF5yKlqT0-o45G4J6NJfDxwkTg-3db4SDmOIsK2_RqetwjLv__qvT-fteYDcWaMzoaN-zS-IFmXQiOYvXGtXNRVRDSfNGOkydGPkm30SmJ6C3pYRN-9GT5SG6QsWwrfqHteVG6s_8_JpRUnzdb_Ttb2BqX1ebhBugIuZugbsiI6Vk2rWdDkALIXGQ3j038yhKwxFanqi0MZikN7gInpBJs1CisGIe1udswfdOT0Vg2nFe8rbNKHZhiCSerwJMHEwC2O6gMSBgiGSEli7ayoQkFRnJ85uLXOfnz4xkydihi7Rzp5dOKFN9APt3qjYX0XpiEjScrofNZ2EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عن این مفنگی را درآوردید!
ولش کنید دیگر بگذارید بمیرد.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/20121" target="_blank">📅 00:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20120">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m2r1o9jm31Uajlfa6oKj-a3MFNRaHdI0wadktizVaUq4mLeR51HS5UJx2-_1vkILpfiCERudiyTU0ot0m9gGuCzcz-pt5YQF8mBo7ZsCBwxcsNNS3ilFY6KoaGRgX-Gpr9lEzVHzm0rSjUBZwwJJRj0GUfS5sN5ahoLB18zgfg5eUjMeTOqgWfRVVcgh_eyXVzfFeLW-0jvSPNSzf_bEsAfpXJfrMEveKucINqiSwXBgN774lrLhzXHG_1Ynrbxzj6OQKiCMSznx0Rkw-rfa0VeMR0BJYDjxPnMlYEDf4yG7umi4FI_CZ5Cb35aOonFP7IguX8udX1Nj_t-iTgN4Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید یادتان نباشد ولی این نخبه نابغه کشورمان — دکتر حجت عبدالملکی — که حتی رییسی او را از کابینه اش اخراج کرد یک بار گفته بود با 1 میلیون تومان میشود کار ایجاد کرد!
یک نفر خوش ذوق هم زیر پستش کامنت کرده بود بله 700 هزار تومان دستگاه تقطیر با 300 هزار تومان کشمش!
البته الان با 1 میلیون تومان نهایتاً یک پیتزا با یک دوغ به شما می دهند و آبش را هم میدهند Meساکی بخورد.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/20120" target="_blank">📅 00:38 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20119">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">باید در هر کوچه یک شیره کش خانه باشد و بعد کنارش یک کمپ ترک اعتیاد بزنیم تا مردم هر کوچه از هم پول بگیرند و گردش مالی ایجاد بشود و مالیاتش را هم بدهند به ما.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/20119" target="_blank">📅 00:28 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20118">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">محسن رضایی:   مردم در خانه‌ها و محلات شروع به تولید محصولات مورد نیاز جامعه کنند</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/20118" target="_blank">📅 23:21 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20117">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">محسن رضایی:
مردم در خانه‌ها و محلات شروع به تولید محصولات مورد نیاز جامعه کنند</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SBoxxx/20117" target="_blank">📅 23:18 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20116">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f676cce991.mp4?token=BqzdajyJZk8-CL61653Lkkkok4FUH6tnGx5XTzBLv1XzjNl3q3NPPAq7qk7fIQXTnmU8t0S02_RS8DMMjYoID8aQmLx7cB5G8iNGzrEepdRKxDKalcA1M24OLQLNL9SUFIK7ky6XOPA6O9_hNG1ZjitR5Rtteq22BlkQbKMFjj60KY91akAgiIojhKr3EKr_n3kCf-9Lcvjmfi_UzK91YIdv1aWdzePayh9LD22b2w4OUuI_V2huVUQJhG5ym9V7DUxLM1rfEHVB7vlUBkXpDWDkMncG82TnZQ-VZOT4KgQoQrdI0ixgjCL6_8DhJ2qIQm_aXCZCZ3PNNYht4XTNlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f676cce991.mp4?token=BqzdajyJZk8-CL61653Lkkkok4FUH6tnGx5XTzBLv1XzjNl3q3NPPAq7qk7fIQXTnmU8t0S02_RS8DMMjYoID8aQmLx7cB5G8iNGzrEepdRKxDKalcA1M24OLQLNL9SUFIK7ky6XOPA6O9_hNG1ZjitR5Rtteq22BlkQbKMFjj60KY91akAgiIojhKr3EKr_n3kCf-9Lcvjmfi_UzK91YIdv1aWdzePayh9LD22b2w4OUuI_V2huVUQJhG5ym9V7DUxLM1rfEHVB7vlUBkXpDWDkMncG82TnZQ-VZOT4KgQoQrdI0ixgjCL6_8DhJ2qIQm_aXCZCZ3PNNYht4XTNlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخستین تمرین رزمی جنگنده سبک یاک روسی در نیروی هوایی ایران    ‌
👍
جنگنده یاک در کنار دو فروند جنگنده میگ ۲۹، در عملیات رهگیری و منهدم کردن پهپاد هدف مشارکت داشت و خلبانان جنگنده‌های میگ ۲۹ با مهارت بالا موفق به شناسایی و رهگیری پهپاد هدف شدند.
👍
در ادامه، جنگنده…</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/20116" target="_blank">📅 22:59 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20115">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اسراییل در حال بمباران جنوب لبنان است.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/20115" target="_blank">📅 21:54 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20114">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmhbOvFmv6HuLCqHZ-AMT4Cnz7HQMTgrlIMTY7T9tVDAx7EPaa_rw3K5PYeBmJRjIRQYjcJGK4-pwYw0zy7HevmRh_y1PWnwRmFpIlH4bIyQU8OB443u_ZSlZf2Wsfy--Nnaquz5UmUJ6mpc6BvzuzqwO9ocQaAUlM6yhKT3LoeRFvWMdhJPaBf3wNly2YavHyiszr-PA9w5zyfwkJCSb2bGaKtwJ_DTAzcNef0v-u62ZzaV5bgfn6EJE7MOqk69PclTRK8TpJGA7NpgXd7qrGHpMsX8nKTkzFCDIGDH6wboYuAYXTwgHe_3ugm-6iY0QMfHeVmtlqJuMwaIa97f3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقاله در روزنامه اورشلیم پست اسرائیل خواستار آن شده است که اسرائیل، ترکیه را به عنوان یک تهدید نظامی در سطح ایران در نظر بگیرد، و این جمله تحریک‌آمیز را مطرح کرده است:
از ادلب تا استانبول، اسرائیل در صورت لزوم، حمله خواهد کرد، نه اینکه دفاع کند.</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/20114" target="_blank">📅 20:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20113">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">یک صوتی مفصل در این خصوص خواهم داد.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/20113" target="_blank">📅 18:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20112">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اوه اوه!    بنگلادش در حال بررسی امکان پیوستن به پیمان مکه است!</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/20112" target="_blank">📅 18:38 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20111">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">باز سعودی ها دستکم کتک خوردن ترک‌ها در سوریه از اسراییل برای بار پنجم را محکوم کردند!  شهناز جوراب که کلا خودش را زده به کوچه علی چپ!   نه حملات یمنی ها به سعودی را محکوم کرد نه حملات اسراییلی ها به ترک‌ها را !  سبحان الله عجب پیمانی شد این پیمان ناتوی اسلامی…</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/20111" target="_blank">📅 18:37 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20110">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">دلار فردایی تهران
⏳
192,300 تومان!  کاملاً مشخص است به صورت دستوری دلار را دارند بالا می برند تا جناح تندرو را به تسلیم وادارند یا دستکم گرانی ها را به گردن آنها بیاندازند.</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/20110" target="_blank">📅 18:36 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20109">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">به‌نظر می‌رسد در درون ساختار قدرت جمهوری اسلامی، شکاف میان جناح میانه رو و جریان تندرو و ضد امتیاز، در حال برجسته‌تر شدن است.   اگرچه این شکاف هنوز به تغییر رسمی سیاست حکومت منجر نشده، اما اظهارات اخیر دکتر پزشکیان، محمدباقر قالیباف و عبدالناصر همتی نشان می‌دهد…</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/20109" target="_blank">📅 18:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20108">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">خیلی عجیب است.   خود ترامپ در مارس ۲۰۱۹ منطقه جولان را به عنوان بخشی از خاک اسراییل به رسمیت شناخته آن وقت سفیرش در ترکیه صحبت از «اشغال» جولان می‌کند!  حدس میزنم عمر سیاسی  — و شاید زیستی — تام باراک (که عرب تبار است) بزودی به پایان برسد.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/20108" target="_blank">📅 18:26 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20107">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-poll">
<h4>📊 تاریخ شروع جنگ ایران و‌ عراق از دید عراقیها چه تاریخی است و چرا؟</h4>
<ul>
<li>✓ ۳۱ شهریور ۵۹ — حمله همه جانبه ارتش عراق</li>
<li>✓ ۳۰ شهریور ۵۹ — حمله هوایی ایران</li>
<li>✓ ۱۰ مرداد ۵۹ — سخنان تحریک آمیز رهبران ایران</li>
<li>✓ ۱۳ شهریور ۵۹ — گلوله باران مندلی و خانقین توسط ایران</li>
</ul>
</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/20107" target="_blank">📅 14:45 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20106">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">این هم جواب آمریکا:  ایالات متحده در حال پیشبرد قانونی است که هلند را مجبور می‌کند تمام فروش و خدمات باقی‌مانده دستگاه‌های لیتوگرافی ASML به چین را ممنوع کند.  قانون MATCH به دستگاه‌های DUV قدیمی‌تر که هنوز تحت قوانین هلند مجاز هستند، هدف می‌گیرد.  چین ۳۳…</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/20106" target="_blank">📅 14:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20105">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">چین می‌گوید تهدید رئیس‌جمهور ترامپ برای آغاز «جنگ اقتصادی» علیه ایران و شرکای تجاری آن کارساز نخواهد بود.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/20105" target="_blank">📅 14:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20104">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">دنیس اشتایلرمن، رئیس شرکت فایر پوینت، تولیدکننده موشک‌های «فلامینگو»، پیامی با تهدید علیه ایران منتشر کرد.  این تصویر، فلامینگوهای صورتی را نشان می‌دهد که در امتداد مسیری که اوکراین و ایران را به هم متصل می‌کند، پرواز می‌کنند و لوگوی شرکت و عنوان زیر آن آمده…</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/20104" target="_blank">📅 13:48 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20103">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/20103" target="_blank">📅 13:22 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20102">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ایران اجازه عبور چندین تانکر نفتی عراقی از تنگه هرمز را پس از درخواست عراق صادر کرد: ایرنا  چنین اقدامی در اوج فشارهایی که روی اوراق قرضه خزانه داری آمریکا آمده به صورتی که باعث شده اسکات بسنت دست به طرح عجیب و غریب بازخرید اوراق قرضه بلندمدت بدون تقاضا بزند،…</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/20102" target="_blank">📅 12:15 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20101">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">به‌نظر می‌رسد در درون ساختار قدرت جمهوری اسلامی، شکاف میان جناح میانه رو و جریان تندرو و ضد امتیاز، در حال برجسته‌تر شدن است.   اگرچه این شکاف هنوز به تغییر رسمی سیاست حکومت منجر نشده، اما اظهارات اخیر دکتر پزشکیان، محمدباقر قالیباف و عبدالناصر همتی نشان می‌دهد…</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/20101" target="_blank">📅 12:13 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20100">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">به‌نظر می‌رسد در درون ساختار قدرت جمهوری اسلامی، شکاف میان جناح میانه رو و جریان تندرو و ضد امتیاز، در حال برجسته‌تر شدن است.   اگرچه این شکاف هنوز به تغییر رسمی سیاست حکومت منجر نشده، اما اظهارات اخیر دکتر پزشکیان، محمدباقر قالیباف و عبدالناصر همتی نشان می‌دهد…</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/20100" target="_blank">📅 12:05 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20099">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddIBYUcHxIVEX32b0JqBBKeEf_vncW6KPtSuwRgZ5XfqwYc9xx199QzBXyM03ThvUaFJUm8GlsuuIjuofZ_2r--XEWfyN7D-LlSujzHPLpczjBXMBsfhHnX56YwpD_KeiOMmaS_pICwHiECsBoNR1d1NbtJ4lWW_9ZEDwlSiz_A6bXnNmufw1rh8KRjXeByktk5t_dvY00Gz62SsiwunOTMXcn4dHzsUugi93IouPxMFel7ymiYK3mZkg-sGPJdz_VHs2ge_Egxj3YgUm50smMlqC_0Dm76f9woK_WjTOfOIPgVx5EltZ3uHx_7AJJn34TUjrjEFRDBvqVnp7DEN5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به‌نظر می‌رسد در درون ساختار قدرت جمهوری اسلامی، شکاف میان جناح میانه رو و جریان تندرو و ضد امتیاز، در حال برجسته‌تر شدن است.
اگرچه این شکاف هنوز به تغییر رسمی سیاست حکومت منجر نشده، اما اظهارات اخیر دکتر پزشکیان، محمدباقر قالیباف و عبدالناصر همتی نشان می‌دهد بخشی از حاکمیت بیش از گذشته به این جمع‌بندی رسیده که ادامه جنگ و فشار اقتصادی می‌تواند هزینه‌ای سنگین تر از جنگ برای نظام ایجاد کند.
پزشکیان دیروز صراحتاً گفت بهتر است جنگ در مقطعی پایان یابد و «اکنون» پایان دادن به آن ترجیح دارد. قالیباف نیز هشدار داد که حتی قدرت نظامی بالا، بدون گردش مالی، رشد اقتصادی و تولید داخلی، نمی‌تواند کشوری را که مردمش تحت فشار معیشتی قرار دارند، پایدار نگه دارد. مهم‌تر از همه، همتی اذعان کرد که صادرات نفت ایران تقریباً متوقف شده و کشور با کمبود ارز، هزینه‌های بازسازی و افزایش بیکاری جوانان مواجه است.
این اظهارات را می‌توان نشانه‌ای از شکل‌گیری یک کارزار هماهنگ در بخش میانه رو جمهوری اسلامی برای مهندسی افکار عمومی جامعه ایرانی در جهت باز کردن دوباره باب دیپلماسی و فاصله گرفتن از فضای پرتنش کنونی ارزیابی کرد.</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/20099" target="_blank">📅 12:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20098">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح بالایی قرار دارد و پیش بینی می شود طلا یک اصلاح نزولی دستکم در حد 300 الی 500 پیپ داشته باشد.</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/20098" target="_blank">📅 11:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20097">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4df224890.mp4?token=WUZ4BI_wKLF-TIje7vrtxvVJZ1lwb22CmS8doEdubHE9Gm53mjN7RTpbQYSQwxYttL0CCwmTRf02_7KgtYTvkq8xocJ8vfxaayXeP-S4hViC5a4dD1TbuuvO3N2EIqbd10p0pedSPxjhBexwrXLuDld6M9fhwqEUH0qvmGaLnC8nu2_uIJBbFu3kLseJY5yv9TQcK9yCVZtrI-3c3VN9T5DLh_qiIK1OuMnYgPs3WvN24D20d_9Lbs6FNxgjV1i4b5lw4R7l17Xt-y4HmwsSM1GbrjHHLU_o9KjvTFkdIHMVxEYo4BGYTwwkYGUNnBTXqj7ozFsRPxiGeYrscDL1gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4df224890.mp4?token=WUZ4BI_wKLF-TIje7vrtxvVJZ1lwb22CmS8doEdubHE9Gm53mjN7RTpbQYSQwxYttL0CCwmTRf02_7KgtYTvkq8xocJ8vfxaayXeP-S4hViC5a4dD1TbuuvO3N2EIqbd10p0pedSPxjhBexwrXLuDld6M9fhwqEUH0qvmGaLnC8nu2_uIJBbFu3kLseJY5yv9TQcK9yCVZtrI-3c3VN9T5DLh_qiIK1OuMnYgPs3WvN24D20d_9Lbs6FNxgjV1i4b5lw4R7l17Xt-y4HmwsSM1GbrjHHLU_o9KjvTFkdIHMVxEYo4BGYTwwkYGUNnBTXqj7ozFsRPxiGeYrscDL1gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام وضعیت</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/20097" target="_blank">📅 11:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20096">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">مدیرعامل شرکت نفت ستاره خلیج فارس از عملیاتی‌شدن استفاده از متانول به‌عنوان جزء اکسیژنه در ترکیب بنزین تولیدی این پالایشگاه خبر داد.   این تغییر می‌تواند برای بخشی از خودروهای موجود در بازار، به‌ویژه قطعات لاستیکی و پلاستیکی مسیر سوخت، ریسک فرسودگی زودرس ایجاد…</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/20096" target="_blank">📅 11:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20095">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">مدیرعامل شرکت نفت ستاره خلیج فارس از عملیاتی‌شدن استفاده از متانول به‌عنوان جزء اکسیژنه در ترکیب بنزین تولیدی این پالایشگاه خبر داد.
این تغییر می‌تواند برای بخشی از خودروهای موجود در بازار، به‌ویژه قطعات لاستیکی و پلاستیکی مسیر سوخت، ریسک فرسودگی زودرس ایجاد کند.
به گزارش شبکه اطلاع‌رسانی طلا و ارز، مدیرعامل شرکت نفت ستاره خلیج فارس روز جمعه ۳۰ مرداد ۱۴۰۵ (۲۱ آگوست ۲۰۲۶ (۳۰ مرداد ۱۴۰۵)) از
افزودن متانول به بنزین
تولیدی این پالایشگاه خبر داد. به گفته او متانول در حال حاضر به‌عنوان یکی از اجزای اکسیژنه در ترکیب سوخت مصرفی خودروها به‌کار گرفته می‌شود.
اکسیژنه‌ها ترکیباتی هستند که به
بنزین
اضافه می‌شوند تا احتراق کامل‌تر شود و عدد اکتان سوخت افزایش پیدا کند. عدد اکتان بالاتر یعنی سوخت در برابر خودسوزی زودهنگام در موتور مقاوم‌تر است؛ همین ویژگی باعث می‌شود پالایشگاه‌ها از این نوع افزودنی‌ها به‌جای ترکیبات گران‌تر مانند MTBE استفاده کنند.
چرا متانول نگران‌کننده است؟
متانول
برخلاف بسیاری از افزودنی‌های رایج، خاصیت خورندگی بیشتری روی قطعات لاستیکی و پلاستیکی سامانه سوخت‌رسانی دارد. اورینگ‌ها، شیلنگ‌های سوخت، دیافراگم پمپ بنزین و برخی مخازن پلاستیکی از جمله قطعاتی هستند که در تماس طولانی‌مدت با متانول، سریع‌تر از حد معمول فرسوده می‌شوند. نتیجه عملی برای مالک خودرو، احتمال نشتی سوخت یا کاهش عمر همین قطعات و افزایش هزینه تعمیر است.
کدام خودروها بیشتر در معرض‌اند؟
خودروهایی که سامانه سوخت‌رسانی آن‌ها برای درصد بالای الکل یا متانول طراحی نشده، بیشترین آسیب‌پذیری را دارند. این گروه شامل بخشی از خودروهای مدل پایین‌تر و برخی خودروهای وارداتی قدیمی‌تر می‌شود که استانداردهای سوخت انعطاف‌پذیر (فلکس‌فیوئل) در آن‌ها رعایت نشده است. خودروهای جدیدتر با قطعات مقاوم به الکل معمولاً ریسک کمتری دارند.
مدیرعامل
ستاره خلیج فارس
تأکید کرده است که درصد متانول در ترکیب بنزین در چارچوب استانداردهای مصوب کنترل می‌شود. با این حال، جزئیات دقیق درباره سهم متانول در هر لیتر بنزین و نظارت مستمر بر کیفیت آن، اطلاعاتی است که مصرف‌کننده هنوز به‌طور شفاف در اختیار ندارد.
استفاده از افزودنی‌های داخلی به‌جای واردات ترکیبات اکسیژنه، برای پالایشگاه‌ها از نظر اقتصادی مقرون‌به‌صرفه‌تر تمام می‌شود. این رویکرد در سال‌های اخیر در چند کشور دیگر نیز با هدف کاهش وابستگی به واردات آزمایش شده، اما همواره با هشدارهای فنی درباره سازگاری آن با ناوگان خودرویی موجود همراه بوده است.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/20095" target="_blank">📅 11:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20094">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">این موشک های دوش پرتاب حرارتی صرفا برای زدن بالگردها، پهپادها و هواپیماهایی که در ارتفاع پایین پرواز می‌کنند مناسب هستند.  به نظر می‌رسد هدف از تسلیح ایران به این سلاح ها، ایجاد فرسایش در نیروهای آمریکایی است که محتملا در حمله زمینی به جنوب ایران درگیر خواهندشد.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/20094" target="_blank">📅 10:54 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20093">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترامپ:  آیا تا به حال کمونیست شاد دیده‌اید؟  آیا تا به حال دیده‌اید که یک کمونیست بخندد؟ من هرگز چنین چیزی ندیده‌ام. من با کمونیست‌ها آشنا بوده‌ام. آن‌ها افراد بسیار ناراحتی هستند.  ما می‌خواهیم شاد باشیم!</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/20093" target="_blank">📅 03:34 · 31 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
