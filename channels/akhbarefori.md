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
<img src="https://cdn4.telesco.pe/file/rbPGknbRdlXdLSZ2BQX0xP_IHZ1WdynCiMUtgv0oVGdE2m3g2iuQ0oEaqfjWm1NzJErwKEsrX3b3itLmkHU3Eri96G4ZhDU06X4GpAXirPI0G2dHD0-mspK1VXCjvwOAZCpy_goSUyXNNWizai1-f1pdpsFTVPlfNbpDNH7wK9_h7cgxQIE-DTA4v0DVAtoP6lxBOa6kWYZoBRZnMEyCwb3_pY2y1umWpbiW_oGBC-S3M-9awsalzi5dCSFDaHJCOF7M3_XnyiZ2Xvjq7FQXND8WCnLBEo6aeMjLR0GgNlaYD-OcJM1BvpHiCpAsrb9ED-g8mg_8XpEiHHe41JPTsw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.08M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-27 03:18:30</div>
<hr>

<div class="tg-post" id="msg-690770">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfaMM2mOE7mvEvBUpuUNsktmIhQeMjMqAiDtC9BJkSF4MKu9ftVUAfMppI_IUYilchOrSRuS8YV0mh1C8NVtwo1_OH2xRNbKjan1o46yLPIfxfeI-nwx7y49GsffiYyW9RNGDVoZI9naBjUgRSZB3dRNApdyXI5Bd5InFmuJrF-_52-kWHcwMy8EbahuiKrw-M1ty7Xu87SZDLKMnZ7mzpVLy5FkVvWr1oAQAyr2jLhPx-2xSHnjH2HEd26losqT-0HUH4EQmg7ikGN_pvjSdJVM7XHRVgvM8M5l_xXMHkjYfg-GUhi4NfpnDQRpMdA0Nw9MpqeXI2Nu4qIl4i9cCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اگه دنبال انگشتر  معمولی هستی، این کانال به کارت نمیاد!
اما اگه
کار خاص و فاخر
می‌خوای، حتماً یه سر بزن
👀
💍
انگشتر نقره دستساز
✨
حکاکی اساتید برتر ایران | عقیق‌های یمنی و غیر یمنی
📍
تهران | خرید حضوری و آنلاین
🔥
موجودی‌های خاص و کارهای جدید رو اول اینجا ببین!
👇
گالری حنان
https://t.me/+af-LaOPsPHZkMTM0</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/690770" target="_blank">📅 00:31 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690769">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUfRtq_EWRJ_weQk2MbC7FkM2-KrhJwYR0IENENwpKZh4CBU61VrGhwHt45nwZk8T2OSWFHweqzcUKBm6w_0O9Ah7QoSsVhM9k2u83Nmw419Sw9lH7y3Ue-pX8s8Wn8Zb_VBUNQR14aWAq_ZVFyNRpmQWCv4cQ8lNrNJ8HKDKwNZN0Cf1AyJ_CUvkZq3M_wZYeeunCPDAkCaOwbn8ebq3e07RPB4B0qosSsC8rc5huFJFAgEDJtcLkKpApVaFuq3GcsXgIHY2BBoTqGMC8jZqPjMowKMGtXrnWiBteu7K4jKSzJNZTfYxh0QDamM_xZC4D8vP3-bxIWeLDT8F5iH5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
پاوربانک بخر، ایرپاد هدیه بگیر!
🔋
پاوربانک ۲۳,۰۰۰ میلی‌آمپر Xiaomi M10
🔥
فقط
1,899 تومان
💳
پرداخت درب منزل
لینک خرید اینجاست
👇
https://memarket24.ir/product/brief/63565/180124/</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/690769" target="_blank">📅 00:31 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690768">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
حملات شدید اسرائیل به جنوب لبنان
🔹
منابع لبنانی از حملات هوایی و توپخانه‌ای ارتش اسرائیل به چند منطقه در جنوب لبنان از جمله السلوقی، القنطره، بنی‌حیان، طلوسه و النبطیه الفوقا خبر دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/690768" target="_blank">📅 00:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690765">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kGh86Q3XjF5FgiEUiFabQ7eAiYJqJBQpGIO5kpSHCB8HNO5vfe-m5Kp7dkyE4yWBAY79dt0anUvCZn3oKRSF0_9mTtdxZEgiZoCvio8wTi4Nh6OngJwLuB8jj5RRIMXuUU412iIF0BX9pSFvrIL0UkPTZD1gvyv5d0j5MDYLGacs1wbRor_LQgG_NitYW9aeExo-nzCnuV_9VvTdLbg6hI3OOS40WjB48m8SBzKZMdgRqkRMdmYuUBm3orbopZz8oAHIdP01RwyQ0gREohi0R_5zFi9NunDavvilyCx5qBoVT5cwnpC3JIeYlSbvxak407O6_mxRkMNRx_TNsIIwOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ah4PAHEG1-6TegtcbCPorANCNOGnmHY9doh0usfDXXcceJooU8wJKuvjHsywqXvUPSmf-2-BvS7UW3J-RGwjoQJTs-r61ck0nJJPaxZJ6EIh_HOXmDAwlafZadzGstjkNopU9cG0gknn3vUCSQ8NU4injyHjhmy--8n0XkNhZg5q8Sq8TrX1BlnQpJ5bqErd5tvw00fCZ_VW8XnJ43RGlnruczGDkPDOOtmtnFcagC7b1OBnxGGf2dGIK6bAacbZTzuPPo9mLwRmoFDUKV1W974xZc-yR63kS3OTL4E_Rfku64X24Gd7qyoTRpgXBhykVIwQ-T9yOF_5RV4W05SzZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HeChvRjPbOq7H2AfyI-TbB_9obJNfO9wI_jqCwiaNdsWTUq8jg31uWx3jIXnHk56LqY1tfdyhdwWCY1eATfoP_ULlSNzldBOB3k9i6cFGpzaPJPHcJNErtvolLpafyHqzcRkEKFpwS10nORJ_ff4CNSYLljOJk7jdTkfNKrYMhTdB1H2rMOLkOWNKH_Udo2HyFpS5bMATFE8in7UecgZWvegqKou9piKVnjSXJORBApV6-FHvPRrRsJluiNlPeAAaHwUYgJZlnqqN7275iNXBcZorQPiD4cBHB1Ea-BxciukTdSypTqXDDnmsLzoIVdn-eMDkamw0MNBzaj8FXeJxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
کشف گونه جدید گربه در بولیوی
🔹
دانشمندان در جنگل‌های یونگاس بولیوی گونه جدیدی از گربه‌سانان با نام Leopardus tilcayo کشف کردند؛ نخستین گونه گربه‌سان کشف‌شده در بیش از ۱۰۰ سال گذشته.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/690765" target="_blank">📅 00:16 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690763">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e289db30a8.mp4?token=FnAmn8CES1tAZTCwRBTY8BIOvMSBkzHU1hDr6Qrg3BHbApqfoijin9aW2DnGELkFe-9FJRLZC2-3haKRZux0guwBH5-fb9MGgkHY1M4gNAFr15SmHVzsqQdIOPg3mSow5IYgTb84osTsI71tpf5L31cHSTdBW3N5y5bUJo2YueIUo76Cm2ZampQgTkAeQN9vlxfIr6jh3hk-UZfu4ggxP19eU7mnsqbqEybimDv_sKSVS4jSLiJ633DIdlL3Ho1oq2jmhtECet9CRs6bY92_uc0F-v3Ut3gqiuMl9HvqpzmVal-MotIV9EK3OWeRhmrIL0LWgMO_aTHmN2sa5028EWYx8hGpisYpJYSotRPnTQtaiIC49TZfUNOaPne2sslym31NqGHy9YDyt69RC6U26jeqrRIlljcq_nEP-F9pFMC4OVF7giR-heLdYtBWCubef7ogNx9ed8YLyg73Hki0ZFfIAYUU6G7qnmhP1oVp0kbNZ_t_5fDM1n68nJQrXN1T2YXQmm3YDVcbInp4lGZuMIG5NtEmJaYpjY5YMnjHzTgbUEUWlQu1gcBTQsjaYqVrCNiFsaF5lNQxHfNXYykDr9sNjYJAdKTnQnmuS3c7n25KzVQs7icHKVOhX3_IxSY6hCE1kU8xO0nUn_6hxBN6cgNuCj_eerR0jtOsOGzZ4mE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e289db30a8.mp4?token=FnAmn8CES1tAZTCwRBTY8BIOvMSBkzHU1hDr6Qrg3BHbApqfoijin9aW2DnGELkFe-9FJRLZC2-3haKRZux0guwBH5-fb9MGgkHY1M4gNAFr15SmHVzsqQdIOPg3mSow5IYgTb84osTsI71tpf5L31cHSTdBW3N5y5bUJo2YueIUo76Cm2ZampQgTkAeQN9vlxfIr6jh3hk-UZfu4ggxP19eU7mnsqbqEybimDv_sKSVS4jSLiJ633DIdlL3Ho1oq2jmhtECet9CRs6bY92_uc0F-v3Ut3gqiuMl9HvqpzmVal-MotIV9EK3OWeRhmrIL0LWgMO_aTHmN2sa5028EWYx8hGpisYpJYSotRPnTQtaiIC49TZfUNOaPne2sslym31NqGHy9YDyt69RC6U26jeqrRIlljcq_nEP-F9pFMC4OVF7giR-heLdYtBWCubef7ogNx9ed8YLyg73Hki0ZFfIAYUU6G7qnmhP1oVp0kbNZ_t_5fDM1n68nJQrXN1T2YXQmm3YDVcbInp4lGZuMIG5NtEmJaYpjY5YMnjHzTgbUEUWlQu1gcBTQsjaYqVrCNiFsaF5lNQxHfNXYykDr9sNjYJAdKTnQnmuS3c7n25KzVQs7icHKVOhX3_IxSY6hCE1kU8xO0nUn_6hxBN6cgNuCj_eerR0jtOsOGzZ4mE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آنچه امروز با آن روبه‌رو هستیم، جنگ برای بقا است
احمد دستمالچیان، سفیر سابق ایران در لبنان و اردن در
#گفتگو
با خبرفوری:
🔹
ما در دوران ”دموکراسی نابالغ“ به سر می‌بریم و در این مرحله، نقش رسانه‌ها حیاتی است؛ رسانه‌ها باید بر ارتقای سطح آگاهی عمومی تمرکز کنند.
🔹
هرچه آگاهی مردم بیشتر شود، جامعه استوارتر و مطالبه‌گرتر خواهد بود و همین امر، مسئولان را به اصلاح مسیر و تصحیح عملکرد خود وادار می‌کند.
🔹
نباید فراموش کرد که آنچه امروز با آن روبه‌رو هستیم، یک”جنگ بقا“ است؛ نبرد موجودیتی میان جبهه حق و جبهه باطل که فراتر از مسائل گذرا است.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/690763" target="_blank">📅 00:02 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690762">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRLvTNif0ymFgXnxcwMeIi5GZMKs41WkZRgEmRxeel3KaARIAwCMiH-dtxoSlZVEaOpyBeSeqMmpBFXK9xJTMopl3VZ1QYWgbRQnAo_OaAFndpF6zFcjWAqhMl6kGg4t8g7uh9YqVLeqG_39GGO3VO9Y3CgfmQk-XmHXt8GgsNq775R-ASQvxalvwxPE5FBN2IiKIl6XUHR6lhpSyOO1KYOblHVI0hu3IKNj0Q8urJsW5aNZ5Q83gQWQ4HeL6SvXbMYqsAdRyqherzdnUqMjCR1b3QLLmk99sFGEAKFP008IeRnk93NDvYWe7e4dQU8dtCBBKtg1Yt1juMet5AwDAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/akhbarefori/690762" target="_blank">📅 00:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690761">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
ادعای‌ترامپ: اگر‌ کانادا بخواهد به اروپا نزدیک شود و اروپا به او کمک کند، اروپا هم تحریم خواهد شد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/690761" target="_blank">📅 23:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690760">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را ازدست ندهید
🔹
🔹
ترامپ در حال برنامه‌ریزی برای جنگ تازه‌ای علیه ایران است؟
👇
khabarfoori.com/fa/tiny/news-3245846
🔹
در سفر عراقچی به چین چه گذشت؟
👇
khabarfoori.com/fa/tiny/news-3245951
🔹
جزئیات کامل قتل‌عام خانوادگی در تهران + ویدئو
👇
khabarfoori.com/fa/tiny/news-3245893
🔹
ماجرای عکس‌های یواشکی از علی ضیا در فلورانس با زن ناشناس
👇
khabarfoori.com/fa/tiny/news-3245801
🔹
قتل یا خودکشی؟ | مرگ مشکوک زن جوان فیلم‌های منشوری
👇
khabarfoori.com/fa/tiny/news-3245705
🔹
صفحه ویژه خبرهای پربازدید خبرفوری را اینجا بخوانید و ببینید و نظر بدهید
🔹
khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/690760" target="_blank">📅 23:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690759">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqLqLeW3KOCNCYvDP6dyhxMal3BXAXYVdJOsnMRrKcQIz_K87Yj-HwvkcI8XHpuaKW_Gevq8s2OTTxo4UCe2Y0o1jzes02fYpWbohWYSiQ54cMnF-v2UkXbgGwoN-jy83C0ph7oAtCD88yqRa94Bx8PJcAaeXqTElXHbpQ4b1EfWjZ6afmMkcR78FzNLurqfO3DopUwy099r9g7UUGd8xd0tRIWDJYL4-oO4YT6GA0968bJ-nCff284vhy-sLCT2-7CwHNP41KrCPAwMlRO9bEf-uulwdl-k1loraENxLd2CdVlOsc3QR3s1Zp3QEyzSDIr68xe_Wji1PErsRPfBNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انجمن خودروی آمریکا: میانگین قیمت هر گالن گازوئیل در آمریکا به رکورد جدیدی دست یافت و به ۶.۳۹ دلار رسید
🔹
قیمت هر گالن در ایالت کالیفرنیا برای نخستین بار در تاریخ، به ۹ دلار رسید.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/690759" target="_blank">📅 23:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690758">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d8bf2c053.mp4?token=gowpPi0aiXyZys6EqbrAO9bnXREDMXqc0Fn41EOLYO6KEa48Ga7EBf7vcNT4XsHRfmuGCZVh31TlLeAvgAXZjSLfwxn7gihmFDklHC9FIk2JiNxRPi7ufErCLA6vDgnAMxkqSDu3ZTh9gZ-8HrBDec_wRy2txfD6wVB2HXJxUi6lxAXF-5SZZBvtAoTOurGuqgeIfIZn-sABLLqSm5fgJUaXSa0k6fnyz9QKK5jpRcHfVqOXZgvvyoNcngNOULjoa5vGVs2RlIDXDinvHheDxUX0EZnaDfoNuWejMZkZcdBryo-y0zJ0QNRWC2kI__IiPgvQU2jQkCIvVINaZF6KcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d8bf2c053.mp4?token=gowpPi0aiXyZys6EqbrAO9bnXREDMXqc0Fn41EOLYO6KEa48Ga7EBf7vcNT4XsHRfmuGCZVh31TlLeAvgAXZjSLfwxn7gihmFDklHC9FIk2JiNxRPi7ufErCLA6vDgnAMxkqSDu3ZTh9gZ-8HrBDec_wRy2txfD6wVB2HXJxUi6lxAXF-5SZZBvtAoTOurGuqgeIfIZn-sABLLqSm5fgJUaXSa0k6fnyz9QKK5jpRcHfVqOXZgvvyoNcngNOULjoa5vGVs2RlIDXDinvHheDxUX0EZnaDfoNuWejMZkZcdBryo-y0zJ0QNRWC2kI__IiPgvQU2jQkCIvVINaZF6KcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راهنمای اندازه‌گیری مواد غذایی
🔹
این پست برای خانم‌هایی است که در تعیین مقدار مواد غذایی و اندازه مواد اولیه مشکل دارند و نمی‌دانند چه میزان استفاده کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/690758" target="_blank">📅 23:41 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690757">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d15736a757.mp4?token=QZkC7IXu1QZTaONIqfna-j4bCc0W_FUjI5dohsLVMbqSbOdGwnjXlRMSmmRWEtKinf4-o7-MaCGyFFiPEGQcsa5Tr2a71xo0kw-BBkWj1pMdj7ccLracosvfPYW_aZG_mehi2NKpXFzJ5ZxgdZq2xBr-qDncfOit9gHoHtd2dPcZ9pYkeuvG8LIsBln5ZldsDE6c_L4QBG7d-LJZjrtVi96f3xdzy5IRGoLvk13fatkfmh-yGsJ9cc1AfcpJBOQ8UxxXHOjOdVmpjN1LQcXygRHy1YdwetPpG-aJv1j8m_aAyLPnlDQVIRNzEpb5JMu1-BYa_JZvgvnRsjeybkNdgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d15736a757.mp4?token=QZkC7IXu1QZTaONIqfna-j4bCc0W_FUjI5dohsLVMbqSbOdGwnjXlRMSmmRWEtKinf4-o7-MaCGyFFiPEGQcsa5Tr2a71xo0kw-BBkWj1pMdj7ccLracosvfPYW_aZG_mehi2NKpXFzJ5ZxgdZq2xBr-qDncfOit9gHoHtd2dPcZ9pYkeuvG8LIsBln5ZldsDE6c_L4QBG7d-LJZjrtVi96f3xdzy5IRGoLvk13fatkfmh-yGsJ9cc1AfcpJBOQ8UxxXHOjOdVmpjN1LQcXygRHy1YdwetPpG-aJv1j8m_aAyLPnlDQVIRNzEpb5JMu1-BYa_JZvgvnRsjeybkNdgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پایین کشیدن پرچم حکومت جولانی در منطقه الحسکه در شمال شرق سوریه
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/690757" target="_blank">📅 23:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690756">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
سالیوان، مشاور امنیت ملی پیشین کاخ سفید:تقریباً نیمی از نیروی دریایی آمریکا و بخش عمده نیروهای ویژه ما درگیر تلاش برای باز کردن بخشی از تنگه هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/690756" target="_blank">📅 23:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690755">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‼️
تکذیب خبر وقوع انفجار در اطراف جزیره خارگ
🔹
خبر منتشرشده مبنی بر وقوع انفجار در ساعت ۲۲:۴۰ در اطراف جزیره خارگ، تکذیب می‌شود.
🔹
براساس بررسی‌ها، گزارشی از وقوع انفجار در محدوده اطراف جزیره خارگ در زمان مذکور تأیید نشده است./ صداوسیما
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/690755" target="_blank">📅 23:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690754">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-text">نام امیرالمؤمنین روزی ما را میرساند</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/690754" target="_blank">📅 23:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690753">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
پروفسور رابرت پیپ: من سال‌ها جنگ ایران را شبیه‌سازی کرده‌ام؛ ایران پایان این جنگ هژمون منطقه خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/690753" target="_blank">📅 23:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690752">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mohSdyjo-46SbUO4Imllqcm_3AuSAy1Lc6t5CwvRoE2ln--fjnZMWFXecl8XCwixzzjAZbkXkHdWsuZu9vuLc2XxMjueG7ZavNBTDbeWkVqbIBRmya_BlSi8OsD53vxEhDDWB8xJIvCFb_WYaVA52eoDo0JBdCYaNJVTBXPk4nuqKnqg0c3JCAJDnozKbc1NLzepaGK6VtjRlLQBJIAEH8X05eTZ1vCLxf9YFsxr8Aiq8Fw7F4Z2uAGon0d-ZTZy7szzbcIyzYIqWTWg8m03_9hh1EblXYv9VoESUGIPVlbzUcCQIiXAv9RtSNGciLyHuLYjiJhZbWmU4-xnKbvhbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این موشک ها سلاح اصلی ایران در جنگ جدید با آمریکا است
🔹
بسیاری معتقدند در صورت شروع مجدد جنگ، ایران این بار به پایگاه دیه‌گو گارسیا در اقیانوس هند یا پایگاه‌های آمریکا در اروپا حمله خواهد کرد. اما ابزار ایران برای این حمله چیست؟ اگر تهران بخواهد دیه‌گو گارسیا یا پایگاه‌های آمریکا در اروپا و اقیانوس هند را هدف بگیرد، از چه سلاح‌هایی استفاده خواهد کرد؟
گزارش تحلیلی خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3245961</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/690752" target="_blank">📅 23:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690751">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
آسوشیتدپرس: واشنگتن با صدور روادید برای مقامات ارشد ایرانی جهت شرکت در مجمع عمومی سازمان ملل موافقت کرد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/690751" target="_blank">📅 23:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690750">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1f6e8a00c.mp4?token=aj8-e3KKiuKzc2gQswPrpDQnbP9l3_8EP34qcQaDuwXXndL8Jpl87qkKuAb27ASq7I0QW_V0a-y565HEvgroXx7FNzFWT7Z5DD2TnqSz21FLcCnyS7DTyKgYIiVodgoQjETihykJe6Ajv9A7XUcU28v_oF9ZbEvyBMsakPNl74ncDyq5nmfWRCugt7Bb6_teIgK2ITNkne1EMrbA095R2uu6asRu4BBMi69QBOtHgT9yUuXzO-WG6eW8rVVsFIwrFAtkQNF1VTKENyjGYqpm2Ukz--zd31W0VQZxkeyB0_fXl3BmOTHqxGYpV2TcNrBhxdZT_ICDfYxbLYAAaP0DWx2WQODAYXbCv6phZaZ7p9EDoG8RDJi1dixAUcSSPxymo2MOa_r4-mkYqvUm8VKGhf_UGoc7lwEtgIlEKZrwqzE0ytFK1mAdTcAUCbOoXonVGl9MLIU5nT4X4H7O6dx23CCcpxcihm2tdhAY-Y65M3R98vhEj6-IiZjfkKgc1v4992w-ML6ZINhJhazFRb0S30Fk69DrbH9hWH3Ww4aMoIe-h3xKpkpKH7vX6vV1diUofMYuA6aTPj08thgl4MO4mYpNPamGmkgTwROIo7xgGWcZDBUSrgI2F81ZTx91aj524Tnqw781TGQzBoJFsaehAU7AnSjLYmsuA31V18Rhywc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1f6e8a00c.mp4?token=aj8-e3KKiuKzc2gQswPrpDQnbP9l3_8EP34qcQaDuwXXndL8Jpl87qkKuAb27ASq7I0QW_V0a-y565HEvgroXx7FNzFWT7Z5DD2TnqSz21FLcCnyS7DTyKgYIiVodgoQjETihykJe6Ajv9A7XUcU28v_oF9ZbEvyBMsakPNl74ncDyq5nmfWRCugt7Bb6_teIgK2ITNkne1EMrbA095R2uu6asRu4BBMi69QBOtHgT9yUuXzO-WG6eW8rVVsFIwrFAtkQNF1VTKENyjGYqpm2Ukz--zd31W0VQZxkeyB0_fXl3BmOTHqxGYpV2TcNrBhxdZT_ICDfYxbLYAAaP0DWx2WQODAYXbCv6phZaZ7p9EDoG8RDJi1dixAUcSSPxymo2MOa_r4-mkYqvUm8VKGhf_UGoc7lwEtgIlEKZrwqzE0ytFK1mAdTcAUCbOoXonVGl9MLIU5nT4X4H7O6dx23CCcpxcihm2tdhAY-Y65M3R98vhEj6-IiZjfkKgc1v4992w-ML6ZINhJhazFRb0S30Fk69DrbH9hWH3Ww4aMoIe-h3xKpkpKH7vX6vV1diUofMYuA6aTPj08thgl4MO4mYpNPamGmkgTwROIo7xgGWcZDBUSrgI2F81ZTx91aj524Tnqw781TGQzBoJFsaehAU7AnSjLYmsuA31V18Rhywc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افشاگری علی فروتن از سکانسی که باعث توقیف برنامه فیتیله‌ای‌ها شد
علی فروتن:
🔹
چند نماینده مجلس برنامه را تعطیل کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/690750" target="_blank">📅 23:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690749">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FySzsbRMshvujTU3GJSTvG6Fo1ZMtKkOBVj7ZPIp-nIxRvh4Q7anMIli2gvQkWqyN3BV8NCJE63ri9vFaRyabqx48IEviFa_ctq5OMQEoqzeYZPfCoyoIqqktfYUuYDp25Ke7HoBW9C7Mm9KLFQCx25kAHHUifbTDeF1sNqef-GWd3Q8gUD91wLPQeTumBq1-NccTd87hmYjknyK7DRR9DtCZ1Zt_2FkrfKJirbcjNj9RG5NwoyLkXzx-7Rt___jb9cFDs36x9yas0r5djSFGyx0zKiQ77AItnyPyxTaYO9KNk4feHy2-soksnPhDEClbAuzZGKi3bvC6zGbyMfwbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان جذب نیرو
🔹
«فرصت همکاری برای حراست، انتظامات و مهماندار خانم و اقا در گروه ایران نوین در اتوپلازا تهران(واقع در کیلومتر ۱۱ جاده مخصوص تهران) ایجاد شده است.
🔹
اگر به رفتار حرفه‌ای، ارتباط مؤثر و محیط کاری معتبر علاقه‌مندید، رزومه‌تان یا درخواست همکاری را ارسال کنید و جزییات بیشتر متعاقبا اعلام می گردد.
واتساپ: 09309000316
#فرصت_شغلی
#مهماندار
#استخدام
»</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/690749" target="_blank">📅 23:10 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690748">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b40e51255.mp4?token=FJqD6dWZdUpZnTA8Vm9Gi2UHylFb3oOkjdD4tfItql6xG9bmsB8VKxwIdPx1JFJZhn9bRjNK_BjEQ0IYcpP8siytBxKo1A55I5lxZWyTYVtScxA_IzDoRd-CzPh95TBz883-_P8JKrT0rlN78e_HoYvzBpSCXn-opkr6d_s51quDjtf4idEoarsnKaygAc6zqoswtfSl-mKIoRdzhyeCwLnxNV5ZxE2LgyvthVxOnjUhaIyoKUWMtqTHVQz9dbt2IEZBkvXofuFo8VDFH_QRyTK7zRq1ZsNXfJizltta6ewUvUcw7YU-gvlX9Nb4Pai66U9hZPgBb-QC7ZWoxVDA-pprj6lNG5B8--jfQF0dnixOH9NAnKquv80MbABfgPCPWZkadCWyPh_5LLNORVFQlnaHfhf30SnElWChhJ94V3gbXTTIaZhdcWwouUDeC8yf2vo4XxAdKJ-mr_qYmhI11aE9GzdbD-aVUXJfOwemLGodQCi3RSoEDez9Nsp8tbRqSSVgrz1m-HDcPlHTcGeCd8lGZZyGTCb0buuYfWgJrRvcp3PfrPdcgCFoCxoHPMhLvrShUAGPxL9ujd4dPC-PQ744o9rWnuJvllEoELsw7dqpO0eD-OO_SzN2Msndqgz1-YpBQb3FEHqBKxPEEodIRFvwNkbhF_ggoef-dFEMTjE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b40e51255.mp4?token=FJqD6dWZdUpZnTA8Vm9Gi2UHylFb3oOkjdD4tfItql6xG9bmsB8VKxwIdPx1JFJZhn9bRjNK_BjEQ0IYcpP8siytBxKo1A55I5lxZWyTYVtScxA_IzDoRd-CzPh95TBz883-_P8JKrT0rlN78e_HoYvzBpSCXn-opkr6d_s51quDjtf4idEoarsnKaygAc6zqoswtfSl-mKIoRdzhyeCwLnxNV5ZxE2LgyvthVxOnjUhaIyoKUWMtqTHVQz9dbt2IEZBkvXofuFo8VDFH_QRyTK7zRq1ZsNXfJizltta6ewUvUcw7YU-gvlX9Nb4Pai66U9hZPgBb-QC7ZWoxVDA-pprj6lNG5B8--jfQF0dnixOH9NAnKquv80MbABfgPCPWZkadCWyPh_5LLNORVFQlnaHfhf30SnElWChhJ94V3gbXTTIaZhdcWwouUDeC8yf2vo4XxAdKJ-mr_qYmhI11aE9GzdbD-aVUXJfOwemLGodQCi3RSoEDez9Nsp8tbRqSSVgrz1m-HDcPlHTcGeCd8lGZZyGTCb0buuYfWgJrRvcp3PfrPdcgCFoCxoHPMhLvrShUAGPxL9ujd4dPC-PQ744o9rWnuJvllEoELsw7dqpO0eD-OO_SzN2Msndqgz1-YpBQb3FEHqBKxPEEodIRFvwNkbhF_ggoef-dFEMTjE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
این
طاق،
جاودان
است
مرمت
میراث
فرهنگی
، ادامه‌دادن مسیری است برای حفظ بنایی که سال‌ها بخشی از هویت این سرزمین بوده است.
پروژه
مسئولیت
اجتماعی
بیمه‌بازار برای مرمت
مسجد جامع عباسی اصفهان
، حالا وارد مراحل بعدی شده و عملیات بازسازی در بخش‌های مختلف بنا ادامه دارد. کاشی‌های آسیب‌دیده، سنگ‌ها و بخش‌هایی که بیشتر در معرض آسیب بوده‌اند، به‌تدریج در حال مرمت و استحکام‌بخشی هستند.
بیمه‌بازار
؛ در ادامه پروژه مسئولیت اجتماعی
«
طاق
جاودان
»
، همچنان همراه این مسیر است تا سهمی در حفظ و ماندگاری یکی از ارزشمندترین آثار تاریخی ایران داشته باشد
#مسئولیت_اجتماعی
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/akhbarefori/690748" target="_blank">📅 23:10 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690747">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
تحریم‌های جدید آمریکا علیه ایران
🔹
دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری (اوفک) با انتشار بیانیه‌ای اعلام کرد که ۳ فرد و ۲ نهاد ایرانی را به فهرست تحریمی خود افزوده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/690747" target="_blank">📅 23:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690746">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‼️
حادثه امنیتی در تنگه هرمز
🔹
مرکز عملیات تجارت دریایی بریتانیا (UKMTO) از وقوع یک حادثه امنیتی در تنگه هرمز، در ۱۶ مایل دریایی شمال‌شرق خصب عمان، خبر داد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/690746" target="_blank">📅 23:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690745">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkZhJWdluCj6AT3o5jTseJYnDY9IaIlL152W_Jaw2hgrzJH0ZpTikZebyFDyDb6aOkerbpxzoOnqAlAr9Xe0HSNTy9VuCbPUlgvh5tqqIVHDbsuw1gs0CKWapH7q5-ky8_xGJCdQEJAdVTBVgCh-zM0oQH2OTAr5Obz0srKkigwvQKz9gX1i_xNJkSwVhW9CJAhbfh7fk0ZeVT0NgkCmvF8QEGzfBvnvEFOzufR60DMO4vo5uugKsKQNCkBV8ffZIu3_P-1JGyeHAcBd5BiivCG3mVFfhMo0Bar5yqfyfl87cpvaqMD7zkDX45apE-2so8j3VNUN2R2F2p2Ut-sMVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
الجزیره: روسیه و چین پیش‌نویس قطعنامه آمریکا در شورای امنیت سازمان ملل متحد برای تمدید ماموریت کمیته تحریم‌های ایران را وتو کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/690745" target="_blank">📅 22:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690744">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
خبرنگار آمریکایی: آمریکا در دوران حکومت ترامپ
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/690744" target="_blank">📅 22:58 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690743">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmfRIiGoBEN9hWK58uzOwJlh407_qjSJcfwb0tClD6oty5GWcpJF9H5Ab5uhnMDh7hHRrMAKpfW3RXCHjqlOLew3n2oWutjSiGZOgI8Pv0PcploGYc0g0FV2fhbMCzO1f0o3GPs8D2mnrCwoVRA_m8XMYtfYnMnMjUfRwHjlyH82M3lbQfefqQgh3OW02IWwxHeTsOIEsJExuuDLcIxSu8KsMCl2nftZA2UfDEcT1tdmJeKkqW7iUHikVs2kNzqQlJlXCtnANWTBOXC_MdRugAglaSJEgfw-K6kRKywLlCvqtMWR3aD2y5TM8DJFs8foZP2loPozt2TTou5RrQHabg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرنگار آمریکایی: آمریکا در دوران حکومت ترامپ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/690743" target="_blank">📅 22:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690742">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‼️
رسانه‌های عربی از وقوع انفجار در شهر ابها عربستان خبر می‌دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/690742" target="_blank">📅 22:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690740">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
احتمال جابجایی سامانه‌های پدافندی آمریکا از کردستان عراق به اردن   مشاور امنیتی نخست وزیر عراق:
🔹
آمریکا سامانه‌های پدافندی خود را به همراه نیروهای باقی مانده تا پایان سپتامبر از کردستان عراق خارج خواهد کرد.
🔹
آمریکا آمادگی کامل خود را برای اجرای توافق با…</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/690740" target="_blank">📅 22:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690738">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VQ7ojGXFvHELx-jUZw0nAu5PuEC2Aa148plihha0DNVkEJUVRHaXo2LUjN4L8DzY-kO7JOjgP0uv4y4O5Og5p_HpbGsXDCNU2Q2_gpdtGJSDvFNlmfaFlSzMDLXp0hbsWxj4Rt-sHwVSavvcEnllDDl_T5rJIxThjn4v9rUXLr7JRV9SWY5IdiZHLuCWG3cYPA5v8O5kmVNZ_Xv50YeIBnWG5u1vpx3M6IdLvpLZXSn2ehUxhazbMyZb47_-6oORgtWtBdRgmfnf286gPEbRL7Ysrq0dhGbZRdydMsrO4Co6rIMzD4UXM6UsYhid6vCBttTSbNLxAwWeTuZTQPieJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AN8wShLVaNtVkXRi4WQMwl3Z3RUEMs-P_xvNJw4TJOdjzzX4z9LMW8_-RsOimmYKamotseqGXEJsgbCAbRM73W6FWT4KDXS88cZ2tV3igEyCoYv-6pMOZXRGMWtX0BZlgTEFHj7KfWUmHSz_2sMMNTLJztECJcuyRcSTRUxuL0oUtf93crCNr6jPMgKq-KtTHcje7a6qICkwx4YvhTTMJxQvUtiSMC_IypDrBaeg_sT_DSAcJuoyw9AJpNqG8tQMMh1m_oRbAZei3vllmgZR1xu9Ifu7r7JeHdZmY95MXNB1ipDuBFbY78FRQFbh_PhddWj1YYL1y7c2yiSBBUmavg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از رهبر انقلاب، حضرت آیت‌الله سیدمجتبی خامنه‌ای در جریان عیادت سال گذشته فرزندان رهبر شهید انقلاب اسلامی از جانبازان پیجری حزب‌الله لبنان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/690738" target="_blank">📅 22:36 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690736">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کشورهای عربی تصور می‌کردند امنیت خریدنی است و آمریکا امنیت آن‌ها را تضمین می‌کند/ آمریکا نه تنها نمی‌تواند امنیت کشورهای عربی را تضمین کند، بلکه حتی امنیت سربازان خود را هم نمی‌تواند تامین کند
احمد دستمالچیان، سفیر سابق ایران در لبنان و اردن در
#گفتگو
با خبرفوری :
🔹
تقابل‌های اخیر میان آمریکا، اسرائیل و ایران گویای یک واقعیت است که آمریکا نه تنها قادر به تأمین امنیت متحدان خود نیست، بلکه حتی در تأمین امنیت پایگاه‌ها و نیروهای نظامی خود نیز با چالش‌های جدی روبه‌رو است.
🔹
این آزمون تاریخی ثابت کرد که امنیت یک کالای قابل خرید نیست، بلکه مفهومی منطقه‌ای است که نباید با دخالت قدرت‌های خارجی مدیریت شود.
🔹
امنیت پایدار و واقعی، تنها در سایه فرآیند همکاری‌های مشترک میان کشورهای منطقه و با هدف دستیابی به ثبات، رشد و توسعه اقتصادی ایجاد خواهد شد.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/690736" target="_blank">📅 22:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690735">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
تحریم‌های جدید آمریکا علیه ایران
🔹
دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری (اوفک) با انتشار بیانیه‌ای اعلام کرد که ۳ فرد و ۲ نهاد ایرانی را به فهرست تحریمی خود افزوده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/690735" target="_blank">📅 22:26 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690734">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53d7553a19.mp4?token=TKOYw47cVyHdHFG7cArOFuHpRD0Mb2-13S5bkDPQVnN6GuIxCHBzNGyUEI2qamIHJacbM6s9xBM7pblrx81x4sfP4eeP5q-Ze0f2Rmtip_dB-leagIAI-sEls1PclA5aR5hUQned1dgI1bboYd9FRONZi7rGjgOev9ZSxslbNg7GG1liUa97PNT5L2fMs6_ouXUTKZi2Z8JV4jkHBvIZ-9ii_9-n4w6FJUO84geAzEkHvk86iJMEr0-brA3cFrhQ8Jzoag9kONGOWqcfsA6LcUJgGvJ9VNHMP87yCGYDQZ6Dk7NoDYWAGq_2Hfbf52JoTzjLPGorRte9bg7sJHTTsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53d7553a19.mp4?token=TKOYw47cVyHdHFG7cArOFuHpRD0Mb2-13S5bkDPQVnN6GuIxCHBzNGyUEI2qamIHJacbM6s9xBM7pblrx81x4sfP4eeP5q-Ze0f2Rmtip_dB-leagIAI-sEls1PclA5aR5hUQned1dgI1bboYd9FRONZi7rGjgOev9ZSxslbNg7GG1liUa97PNT5L2fMs6_ouXUTKZi2Z8JV4jkHBvIZ-9ii_9-n4w6FJUO84geAzEkHvk86iJMEr0-brA3cFrhQ8Jzoag9kONGOWqcfsA6LcUJgGvJ9VNHMP87yCGYDQZ6Dk7NoDYWAGq_2Hfbf52JoTzjLPGorRte9bg7sJHTTsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش‌های اولیه از سقوط یک فروند جنگنده F-۱۶ در ایالت میشیگان آمریکا
🔹
تا این لحظه اطلاعات دقیقی از وضعیت خلبان، تلفات احتمالی یا دلایل فنی بروز این سانحه منتشر نشده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/690734" target="_blank">📅 22:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690733">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dm41h3mNY58482EI9xDAwa2YuUBiwVIUEPBE5KRTgq9wHqLpSQsCqMgJA23HHViiDA-zA9XAP3EUQpT4RYwrrzfbEaBKDvlE8cWpPiF54CNS77WSmfdElDGwS2h3eUKkfxJEfdUiTXVJ-nrST5jqK_u1j99ocd2wvHIJ1PaxntGwgBgVMo3heT0R8zlx_jBoy3lPJ7ops4YB0B-KYYQYaZAh_0VL6sxFamZ9RruC6UhAOAz7CEGQgMC-As-bkAfr5BVMVpMtuw6VrE1dX-C0Ls4KEJjsLVFDATULq7IamEB8h14EEMYr_iYpMmjPxdQxqKN-7Pc3k_XCZBK8U-pzhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تنبیه انضباطی خاطیان تبریز؛ سوابق کیفری متهم توجیهی برای رفتار نامتعارف مأموران پلیس تبریز نبود!
فرمانده انتظامی آذربایجان‌شرقی:
🔹
ویدیوی منتشرشده از رفتار غیرمتعارف با یک متهم مربوط به ۱۴ خرداد ۱۴۰۵ است که پس از دستگیری فرد مذکور در جریان یک نزاع خیابانی رخ داده است.
🔹
هر چند که متهم سابقهٔ جرائمی از جمله قمه‌کشی، نزاع، مزاحمت خیابانی و توزیع موادمخدر داشت اما این سوابق به هیچ عنوان رفتار نامتعارف و خارج از استانداردهای قانونی مأموران را توجیه نمی‌کند، مأموران دخیل در همان زمان، طبق مقررات انضباطی فراجا تنبیه و «انتظار خدمت» شدند و اقدامات تنبیهی تکمیلی برای برخورد شدیدتر با آنان در کمیسیون قضایی و انضباطی بازرسی کل فراجا درحال پیگیری است.
@AkhbareFori</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/akhbarefori/690733" target="_blank">📅 22:18 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690732">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/569f2c20bd.mp4?token=C5v53R8WKTBpsyOMG-M6kGfgdbHg-0pG6PhqLtcUbuTx-1JaK8ASqBZnzGxFzl3e34o1mbTWHuihSrLtalOZzizFnN1kYr6USFb4cMLVOZQ69DzXaIq1qiL0Sy8hu8e3CiuuCNj2HYwbGjn_88hf2aaXtzlPJCQa_DvjgfKoChozRqDWmg3u-mtvkh5Cxt43QdN3RCiAejTl4QKwmpXhrYxDHCmPRVhPCT9m4nvjam1Nm3-7pM0Ai2N0qEePqv7EY9_r_yyN4T7FlRmPOLPZLfmLI7bndCc640f3tXBs5c4IMAcB8s4QshFpS2nBNhtR2qioZBTTX8RH8C5l7Aql4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/569f2c20bd.mp4?token=C5v53R8WKTBpsyOMG-M6kGfgdbHg-0pG6PhqLtcUbuTx-1JaK8ASqBZnzGxFzl3e34o1mbTWHuihSrLtalOZzizFnN1kYr6USFb4cMLVOZQ69DzXaIq1qiL0Sy8hu8e3CiuuCNj2HYwbGjn_88hf2aaXtzlPJCQa_DvjgfKoChozRqDWmg3u-mtvkh5Cxt43QdN3RCiAejTl4QKwmpXhrYxDHCmPRVhPCT9m4nvjam1Nm3-7pM0Ai2N0qEePqv7EY9_r_yyN4T7FlRmPOLPZLfmLI7bndCc640f3tXBs5c4IMAcB8s4QshFpS2nBNhtR2qioZBTTX8RH8C5l7Aql4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚗
🧹
جارو شارژی خودرو با مکش ۴۵۰۰Pa
سبک، کم‌حجم و شارژی با ۲۰–۲۵ دقیقه کارکرد!
⚡️
اندازه جعبه : 16*16*6 سانتی متر
مکش نیرو:۴۰۰۰ - ۴۵۰۰Pa
ویژگی های خاص:قابلیت استفاده به صورت خشک در خانه و ظرفیت باتری ۲۰۰۰ میلی آمپری
🔥
قیمت ویژه امروز: 1,389,000 تومان
🏠
پرداخت درب منزل
🛒
خرید
👇
memarket24.ir/product/fast/26903/180124/
✨
تخفیف آخر ماه؛ فرصت آخر!
https://l.memarket.me/lp/65/180124</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/690732" target="_blank">📅 22:18 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690731">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
آسوشیتدپرس: واشنگتن با صدور روادید برای مقامات ارشد ایرانی جهت شرکت در مجمع عمومی سازمان ملل موافقت کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/690731" target="_blank">📅 22:14 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690730">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f6b82fae1.mp4?token=V4wA2xc9B4uRwBci-3G-yhygk-yXqf78g7dxxQKo7nOQTQx-f2xAgvhaSzR7AWQ64JXBO_WXSiPcZFYM_yAPGfLnirtbYQVUZ7U4EhnL9HsebhhEqe5m6kCUNHCGqVt-uc4KjKyDS9udVRvl2HlGL88MXDnIp2ybZOMUGpsmbLLOSlBxq4_fJqS94ENfY0guLoVKPqwhEfWnTGW1FcGbA1YdS8pUVnU9lOuXdiDLcjGH6iUT8c0d2ZnJp6IxgpPiJOmuQ5WWXHxPl-UINgeUNKBF5kNlK_uoBhPuSQTRwS3FmWslccUTjXTCrUBGNFq3mEXlad1XfEgGqhj8yp-hhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f6b82fae1.mp4?token=V4wA2xc9B4uRwBci-3G-yhygk-yXqf78g7dxxQKo7nOQTQx-f2xAgvhaSzR7AWQ64JXBO_WXSiPcZFYM_yAPGfLnirtbYQVUZ7U4EhnL9HsebhhEqe5m6kCUNHCGqVt-uc4KjKyDS9udVRvl2HlGL88MXDnIp2ybZOMUGpsmbLLOSlBxq4_fJqS94ENfY0guLoVKPqwhEfWnTGW1FcGbA1YdS8pUVnU9lOuXdiDLcjGH6iUT8c0d2ZnJp6IxgpPiJOmuQ5WWXHxPl-UINgeUNKBF5kNlK_uoBhPuSQTRwS3FmWslccUTjXTCrUBGNFq3mEXlad1XfEgGqhj8yp-hhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از چند قالب ساده تا یک کسب‌وکار خانگی
🔹
در کمپین #چرخ_زندگی تلاش می‌کنیم کسب‌وکارهایی را معرفی کنیم که با سرمایه اولیه نسبتاً کم، امکان شروع در خانه دارند و می‌توانند به تقویت اقتصاد خانواده‌ها، به‌خصوص برای بانوان، کمک کنند.
🔹
این بار سراغ ساخت محصولات…</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/690730" target="_blank">📅 22:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690729">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44c6b995de.mp4?token=Z_4phr5npTceUQtNRip1qoaralt7ADXeadMw0ODuGJkuBFWL_F0xBzNewq4RngIaTNSJJdiAgxrda0srQf0BWflUC3ttHWdz-EnRb9_3kCPZ2TwDQ1_akap2exaHLk_4WGcDuvLTn9yT53kTeC5gCb2-g4RDKneeKqCVA8bvqkoQvTNeQT4judWbLdeuTjlN_OujOcRtsHbg9rS9_vSfG4e_l8cRKNkiEv9R6VPUw36zV9uzUIMX3FCrm-jMbqmwEZmp7UbsS8HIHzhZGMTWHAo-5GPXXoFf-S_uqwj0xY2cQH0fG6F1SKHCVL5ozNLyMOsUEtrVvfY5d-bl0pKBJCcv_hd4wosgUqciCsLfIfFi7TaBTJ1w7VD_g-_Zq8XKLUOMJUJT1VuIRPU4wO7spcXtBzeux0_i2DGo7_55Zs0NlClAkoHExHye02UCy7EMyykQzYXHtnynAnf8eLu54YWPGMAjh-vOEvrDkRXhcdhbJKJrarskB6mlA5kDf8ro5vNReAynPXqIS1mt8zTyiW_m1ztLC-WSwmGfmp5AefgnVJ2-sUWY8FzYpMVnTO6Dd97BfklRwijQBvXzJ-lIHgy3LZ0nzjGKZyJ2HHtXYomuyqG_w8nBdAdkhAJYu94x0QfQE_uWscag0aZXM9Ghu_ebpfDXpqgUblHrLFk2QJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44c6b995de.mp4?token=Z_4phr5npTceUQtNRip1qoaralt7ADXeadMw0ODuGJkuBFWL_F0xBzNewq4RngIaTNSJJdiAgxrda0srQf0BWflUC3ttHWdz-EnRb9_3kCPZ2TwDQ1_akap2exaHLk_4WGcDuvLTn9yT53kTeC5gCb2-g4RDKneeKqCVA8bvqkoQvTNeQT4judWbLdeuTjlN_OujOcRtsHbg9rS9_vSfG4e_l8cRKNkiEv9R6VPUw36zV9uzUIMX3FCrm-jMbqmwEZmp7UbsS8HIHzhZGMTWHAo-5GPXXoFf-S_uqwj0xY2cQH0fG6F1SKHCVL5ozNLyMOsUEtrVvfY5d-bl0pKBJCcv_hd4wosgUqciCsLfIfFi7TaBTJ1w7VD_g-_Zq8XKLUOMJUJT1VuIRPU4wO7spcXtBzeux0_i2DGo7_55Zs0NlClAkoHExHye02UCy7EMyykQzYXHtnynAnf8eLu54YWPGMAjh-vOEvrDkRXhcdhbJKJrarskB6mlA5kDf8ro5vNReAynPXqIS1mt8zTyiW_m1ztLC-WSwmGfmp5AefgnVJ2-sUWY8FzYpMVnTO6Dd97BfklRwijQBvXzJ-lIHgy3LZ0nzjGKZyJ2HHtXYomuyqG_w8nBdAdkhAJYu94x0QfQE_uWscag0aZXM9Ghu_ebpfDXpqgUblHrLFk2QJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعترافات عامل قتل عام خانوادگی تو پونک  متهم:
🔹
اختلاف ارث و فشار روانی، او را به فروپاشی رساند.
🔹
مادرش برای واگذاری سهم ارث تحت فشارش می‌گذاشت؛ از خانه بیرونش کردند و کارتن‌خواب شد، خانواده‌اش می‌گفتند سهم ارثت را واگذار کن یا برو بمیر.
🔹
کسی کمکش نکرد؛ مادر…</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/690729" target="_blank">📅 22:09 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690728">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
خشم شهروند آمریکایی: ۱۴۲ دلار دادم تا فقط باک لعنتی‌ام رو پر کنم!  مرد آمریکایی:
🔹
روزانه یک میلیارد دلار خرج جنگی در ایران کردیم که توش به تمام معنا افتضاح بار آوردیم و مفتضح شدیم؛ قیمت همه داره سر به فلک می‌کشه، اونوقت این عوضی (ترامپ) میگه نگران نباشید!…</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/690728" target="_blank">📅 21:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690727">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91be67c90a.mp4?token=M6gIJTInxPcJ9TNsgb7gdx_MkHUA4PG834pPGWpRjlKyCTuxIL9VSD8bQY9UviD_1jG1jfsFy1DjUAPOCIjlcejVRQY9RXxGP0duEypttUn4Ua0ESgRgH341c6BMkVu_SP2jBs0b7yO1IkfKCnH9YYSEOo5cLJj4LHAT7aB6nUS0rYWLV5d79woibLRNw7EEgZhhcCleghcaCjGeKLKdCcSbv_PQ4xCVDBySTxzwVKED-0O45IBDgp9sYO2GROzKl0mE1VcRK-OHOGZz621rjiK6nXzYQtMQTTsg23LR4JXcIXLvwsqx-zKJvTzXnUYTAofwdIp_Xq8Hps9bXcYBDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91be67c90a.mp4?token=M6gIJTInxPcJ9TNsgb7gdx_MkHUA4PG834pPGWpRjlKyCTuxIL9VSD8bQY9UviD_1jG1jfsFy1DjUAPOCIjlcejVRQY9RXxGP0duEypttUn4Ua0ESgRgH341c6BMkVu_SP2jBs0b7yO1IkfKCnH9YYSEOo5cLJj4LHAT7aB6nUS0rYWLV5d79woibLRNw7EEgZhhcCleghcaCjGeKLKdCcSbv_PQ4xCVDBySTxzwVKED-0O45IBDgp9sYO2GROzKl0mE1VcRK-OHOGZz621rjiK6nXzYQtMQTTsg23LR4JXcIXLvwsqx-zKJvTzXnUYTAofwdIp_Xq8Hps9bXcYBDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس ستاد مشترک ارتش آمریکا: دشمنان ما ممکن است از نظر جغرافیایی پراکنده و دور از هم باشند، اما به شکلی فزاینده با یکدیگر در ارتباط هستند
🔹
از این پس باید فرض را بر این بگذاریم که یگان‌های ما توسط سامانه‌های خودکار شکار، در تمامی طیف‌های فرکانسی مختل و به‌صورت لحظه‌ای ردیابی خواهند شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/690727" target="_blank">📅 21:58 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690726">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
ادعای خصمانه وزارت خزانه‌داری آمریکا: ما به دلیل حمایت از دولت ایران، پلتفرم معاملاتی ارزهای دیجیتال بیت‌بانک را تحریم کرده‌ایم!
بسنت:
🔹
تحریم های امروز علیه ایران یک شرکت تجارت الکترونیک و سه شخص حقیقی را هدف قرار داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/690726" target="_blank">📅 21:54 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690725">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b1c5a1ce3.mp4?token=O033VBtJrskO9F7mBWRJh4GTyciT3yyZQCYHtoxPpgWwSFEhYesO1t1h_xM8ZraGg3WCiTBcGp16qu7cg-Id_CdQ7gE0EEy0SK9J2NmQgwF5tEZ-PTYewEaJxY9JjJ6jf0whZCcZ__-GgXy5PAQuGGtQgjANex7rSQGNNBEEvWAKdJ1HP_q0mCUhCWP-zv4765aJ5EFuiQPkYDnSZzQ4OdvfClFGKXZ-HFbxydWbVU0RSnOO6tajfu6V5m9-VQJpi2QOLIDUn8ZuD2_vZPJbwR8-GAbQYl4tXYOfYqT0LjZTfePlJsjeQmjLID2uNkPYjrxq6-x_bLXvcYwHgB0w6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b1c5a1ce3.mp4?token=O033VBtJrskO9F7mBWRJh4GTyciT3yyZQCYHtoxPpgWwSFEhYesO1t1h_xM8ZraGg3WCiTBcGp16qu7cg-Id_CdQ7gE0EEy0SK9J2NmQgwF5tEZ-PTYewEaJxY9JjJ6jf0whZCcZ__-GgXy5PAQuGGtQgjANex7rSQGNNBEEvWAKdJ1HP_q0mCUhCWP-zv4765aJ5EFuiQPkYDnSZzQ4OdvfClFGKXZ-HFbxydWbVU0RSnOO6tajfu6V5m9-VQJpi2QOLIDUn8ZuD2_vZPJbwR8-GAbQYl4tXYOfYqT0LjZTfePlJsjeQmjLID2uNkPYjrxq6-x_bLXvcYwHgB0w6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صدای آرامش‌بخش درختان کاج در باران
🌲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/690725" target="_blank">📅 21:53 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690724">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
رفاهیات کارمندان در کیف پول واریز می‌شود
/
استفاده از کیف پول اجباری نیست
🔹
طبق تصویب‌نامه هیئت وزیران، دستگاه‌ها باید بخشی از رفاهیات کارکنان را با رضایت خودشان به کیف پول ایران واریز کنند؛ حداقل ماهانه یک میلیون تومان.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/690724" target="_blank">📅 21:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690723">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pu-RWjtzb1CjIfR1_deE_d_WnbO1bVUsixe8W3YEJcbxPGfgsXI2yYYnPCWa7TkBwWnXwJ_QXM0Bz07HTEDsRUG_SIkBGDTzCdDhn3afYM4I9UTodxNL8F-XF_rAeoLQNEEWRGokO8g9M1XOF2ur-DKsPPFdNCNNT76SkbO8heILFCjMJ175_pMZiGfFG1yNxol4ZcV9vUw0hhIgRpgkSxf7oc494DP9p9oXxNLVj_YblK415qfDOL2juar5I5hiZnOMP0Yvw9zOoOvDuXTj9JOvCGHUJ5RGFqD-8oOPcLUcituU2f4OoD556z9JmwjHNlj_F9ANQi1pUP_7YHVcww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فوران یک آتشفشان از فضا
🔹
این تصویر، آتشفشان کلیولند در آلاسکا را نشان می‌دهد که از ارتفاع حدود ۴۰۰ کیلومتری بالای سطح زمین ثبت شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/690723" target="_blank">📅 21:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690722">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
الجزیره: تهدیدهای ترامپ زمینه‌سازی برای مذاکره با ایران است
خبرنگار الجزیره:
🔹
صحبت‌های ترامپ درباره حمله به ایران تلاشی برای زمینه‌سازی مذاکره است؛ چون بلافاصله پس از سفر عراقچی به پکن مطرح شد، تماس وزرای خارجه چین و آمریکا نشان می‌دهد چین در حال سنجش تمایل دو طرف است و ایران به دنبال کسی است که تضمین‌های لازم را بدهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/690722" target="_blank">📅 21:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690721">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
عربستان برای تقویت پدافند هوایی دست به دامن چند کشور شد   آسوشیتدپرس:
🔹
ریاض با نگرانی از کاهش ذخایر موشک‌های رهگیر، از فرانسه، انگلیس، پاکستان و مصر خواسته سامانه‌های دفاع هوایی خود را مستقر کنند.
🔹
این درخواست در حالی مطرح شده که آمریکا نیز با محدودیت ذخایر…</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/690721" target="_blank">📅 21:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690720">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87d07cea0f.mp4?token=TPaE_DfEDWx9vUmGoKZqjXjd-gf2uHSaXeCocCkp5TOCj6_4PmTAKW9zFN8fMw5g92tg_QDqwn5MZLLYwNtYmsfOg6cjpnwCVG4UhOzOmMaiXmt4pVKEKgAHQ5WYOYHaB3I9E3m8snnXy6HIu6KuCYOugaMmknBplXgIg0JBJPlOuAwqqqYpmodblN0ZPHMH5Olv_VUf7YFSbZGqEPCPc7t_IZUHm_vmtvtP6mTQxxluLfCLTje7qCOTVywn1hwhOpPyuEIBQRdgW1CgQw_1U9Smz3du44uzOF5G2p9J4FidUgGqvEAvGezcNs1r139plD3_t4b3eUu-ADPUAsA2Exjp4h2Qb68uBgi7Ctt7sx8QgzH2j5dsV4pBbEA_QGkEbnMVQWtR02e5WgotHDiffU-iQh2bmPFfY7G1BNwKqd2j8exofGUg_a68DxcucJWdB4WhsfIVv6i2oNHMi1xfDaRpKcALzdnVqwLFshJ12om_c0nPzfxaLwodwvx9NphiwUSb-t6OaZDA0MQgyaJxeujoGG_iUgMSBnqxCf_AtafSOJgVEDzXHkLTJFo4bTbRDHddqGuu-U7_FQnIjqIuNkUdu0PWTf6cx0cHJgUz0FDzKyc0Vfa-NjlTkOx-hSc-l0NnnaAfVYkUwpL2TaNsWlbExDARm2BS3xpyRW5EcPY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87d07cea0f.mp4?token=TPaE_DfEDWx9vUmGoKZqjXjd-gf2uHSaXeCocCkp5TOCj6_4PmTAKW9zFN8fMw5g92tg_QDqwn5MZLLYwNtYmsfOg6cjpnwCVG4UhOzOmMaiXmt4pVKEKgAHQ5WYOYHaB3I9E3m8snnXy6HIu6KuCYOugaMmknBplXgIg0JBJPlOuAwqqqYpmodblN0ZPHMH5Olv_VUf7YFSbZGqEPCPc7t_IZUHm_vmtvtP6mTQxxluLfCLTje7qCOTVywn1hwhOpPyuEIBQRdgW1CgQw_1U9Smz3du44uzOF5G2p9J4FidUgGqvEAvGezcNs1r139plD3_t4b3eUu-ADPUAsA2Exjp4h2Qb68uBgi7Ctt7sx8QgzH2j5dsV4pBbEA_QGkEbnMVQWtR02e5WgotHDiffU-iQh2bmPFfY7G1BNwKqd2j8exofGUg_a68DxcucJWdB4WhsfIVv6i2oNHMi1xfDaRpKcALzdnVqwLFshJ12om_c0nPzfxaLwodwvx9NphiwUSb-t6OaZDA0MQgyaJxeujoGG_iUgMSBnqxCf_AtafSOJgVEDzXHkLTJFo4bTbRDHddqGuu-U7_FQnIjqIuNkUdu0PWTf6cx0cHJgUz0FDzKyc0Vfa-NjlTkOx-hSc-l0NnnaAfVYkUwpL2TaNsWlbExDARm2BS3xpyRW5EcPY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مسعود بهنود تا پیش از نوروز به ایران بازمی‌گردد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/690720" target="_blank">📅 21:33 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690719">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
کلاد حالا می‌تواند مثل یک مدیر پروژه، چند کار را هم‌زمان جلو ببرد
🔹
کارها در فضای ابری انجام می‌شوند و حتی اگر لپ‌تاپ را ببندید ادامه پیدا می‌کنند. هر پروژه حافظه مشترک دارد و فایل‌ها یکجا نگه‌داری می‌شوند. این قابلیت فعلاً برای برخی کاربران فعال است و به‌زودی برای همه عرضه می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/690719" target="_blank">📅 21:24 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690718">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mES-bJbTvImbjuxt6LpZ_uy69qTtnc2-ECA96bCEu7lYVwoGeuEgn6QWOziV-75CHhqFCfZvP8tdqHkieUHwt2hsJ28udmJITax6p-djRXKUy8bKMeBBhO2PunwqNXy0y9zcpgGd2s_0rLOTQil-2vdNNASarJhHYq_RNqghbv1IMXC1N9Hz2HBvuXdlGoWWWninKpb2MMFsS5QHdHi29HjOjIYymm_1xBfdbewoiKxnwaOyilBbANs6-U8CxnnlLbg44H6hQs_fOGRXlUELdB8Ga8btEeWt8Cf7GnM6cyzMZCKfmsgDwVCA5Pm5gNHElGdFshSqnPv-Mp5Xsd_nHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افراد مبتلا به آستیگماتیسم در شب چگونه می‌بینند
👀
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/690718" target="_blank">📅 21:19 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690717">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7de3a763e9.mp4?token=Cj27zZew3QAAsaElzkJuSUB7sJLGQF3vlMVJhYwNxZJgiYpPKcN7LoodZdPS8CkLLsw101TWY5ytmFCnbCtVk_glUOkNRltvyigJGOo3xWz_hLqlnLrdPOoSXxgFh2j8wUvMAxQxsfxGBVmf7QX0OP2dZbUIb4tI4Zc7Mznp7aQvNqxdfLJclMkIITf_tfH4cvUSgEMOUEc23hunbMUHgogwYAYQG5bljsd55-MoARUng2gutcefy8b7vZRNL4Hbkn8g9jczMb-kEILFu_X2XvFPtwkvytrbc06VBVJDSS6geKYH56pmRTKYsxzBkLmG8lxKfhqAw3gfD6UgwJoKdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7de3a763e9.mp4?token=Cj27zZew3QAAsaElzkJuSUB7sJLGQF3vlMVJhYwNxZJgiYpPKcN7LoodZdPS8CkLLsw101TWY5ytmFCnbCtVk_glUOkNRltvyigJGOo3xWz_hLqlnLrdPOoSXxgFh2j8wUvMAxQxsfxGBVmf7QX0OP2dZbUIb4tI4Zc7Mznp7aQvNqxdfLJclMkIITf_tfH4cvUSgEMOUEc23hunbMUHgogwYAYQG5bljsd55-MoARUng2gutcefy8b7vZRNL4Hbkn8g9jczMb-kEILFu_X2XvFPtwkvytrbc06VBVJDSS6geKYH56pmRTKYsxzBkLmG8lxKfhqAw3gfD6UgwJoKdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی رسانه‌های انگلیسی از حمله‌ها می‌نویسند؛ روایت جنگ از نگاه دیگران
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/690717" target="_blank">📅 21:17 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690716">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZZQknSNGtagCgtPG9XR4gpOrI0j-pKJxkefxRPl6WfvSd2ttph9osZMaIpokFW-BSvfJc_QsiGM8-hZZlAUymP-W08900D_V_A2pFv3qoMyJ3qHuwbGSUSk5HYyNYm2LNkZXYUY7uYx6Vf98xdRiCNhcSyUfXbmiHL-pAvTG_GmJJh_3xif-O8bUIFbOhS9q6akbmLdceBaslgaW9XnvX3vG0EsbXMcfvjvLG8Jk_BtY-gAimHz9glnjLLVWyCq_t8M1x1fvGz24h-dKkQD3RbqhEGdh2Ds6sZwjbnpXLPnrBh_vUK6G_Q3cvupypgAmHnJMHNAbYf8PVLHVEGiNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیرانوند برای سربازی به فجرسپاسی می‌رود  مدیرعامل فجرسپاسی:
🔹
طبق اعلام ستاد کل نیروهای مسلح، علیرضا بیرانوند باید خدمت سربازی خود را در این باشگاه سپری کند؛ هرچند فجر تا نیم‌فصل امکان استفاده از او را ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/690716" target="_blank">📅 21:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690715">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69e2adbde4.mp4?token=rMm0mOnHsAByFfTMvy72gdsPSS33lL7DL6foGMEhk18qcdaYTg3bg7YLopHkB5Zk3AqUkY0SxCU8DOT0WAicFvcARH_t_wjJ39tIykAm3Su4RDETcYgIv0WZFEjkFtB08oqubW4-KL3oJrMsnFE_kHOP0UtCq40P4RHDWVBFHO4jb05vbIm9jxUqqAZNu8ZRYwp5jy98o_pAcTRfXmjDOotnTvcOTJfdiSY8JrxBr2yAR-tXj1RJZTGpKcVtXi6pdcxzd542avlMntIu5SusjqNdFMHimtZcayvVCRWNMjyLM2m4pw6LOwKFAV1yjHDid8tSR4q-eRAmXQpvdMVilQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69e2adbde4.mp4?token=rMm0mOnHsAByFfTMvy72gdsPSS33lL7DL6foGMEhk18qcdaYTg3bg7YLopHkB5Zk3AqUkY0SxCU8DOT0WAicFvcARH_t_wjJ39tIykAm3Su4RDETcYgIv0WZFEjkFtB08oqubW4-KL3oJrMsnFE_kHOP0UtCq40P4RHDWVBFHO4jb05vbIm9jxUqqAZNu8ZRYwp5jy98o_pAcTRfXmjDOotnTvcOTJfdiSY8JrxBr2yAR-tXj1RJZTGpKcVtXi6pdcxzd542avlMntIu5SusjqNdFMHimtZcayvVCRWNMjyLM2m4pw6LOwKFAV1yjHDid8tSR4q-eRAmXQpvdMVilQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ مدعی شد: تصمیم بزرگی در پیش دارم؛ یا وارد عمل می‌شوم یا نه
🔹
ترامپ روز پنج‌شنبه به «آکسیوس» ادعا کرد در جنگ ایران به یک نقطه عطف حساس نزدیک شده است؛ جایی که باید درباره ازسرگیری حملات گسترده با هدف پایان دادن به درگیری تصمیم بگیرد.
🔹
«تصمیم بزرگی…</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/690715" target="_blank">📅 21:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690714">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
سخنگوی قوه قضاییه: پرونده ترور امام شهید به دادگاه می‌رود
🔹
برای ۱۵۹ تن از مقامات ارشد سیاسی و نظامی دولت آمریکا و رژیم صهیونیستی کیفرخواست صادر شده است، ۶۷ نفر از این مقامات اسرائیلی و ۹۲ نفر آمریکایی هستد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/690714" target="_blank">📅 21:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690713">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqiObyrIVw8P_GUB0wfrDh-PPYNoVD_RRfmlOpdDwphKNA09oXCHOlr_7aw0u7sJRQw2RDnUlFmm8SVGSMJAeeH_t1mGycHBNvrokFU3_6HDjhr2vuZbzbvOdUVhm3xPDZLR4O_iCho8OJbU45yzNFPBmjUpLJw2mBYOuE0xNj36i1at1xuq_JduovCFYn0lRHjS0W-HUMbALpILXBjqkYB1RBqhedtW_nU7LHW57bluk55djEV5CR_O8W7YyZW9aaGnV_yFmx4ikENwecc_zMjs2pSXGJznH48Bk_i5n34r82HhRQu5iU4RyIsTPReoSNOUe8gx6PBR1LEikhrvcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بدن با علائم مختلف بهت پیام میرسونه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/690713" target="_blank">📅 21:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690711">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
ترامپ مدعی شد: تصمیم بزرگی در پیش دارم؛ یا وارد عمل می‌شوم یا نه
🔹
ترامپ روز پنج‌شنبه به «آکسیوس» ادعا کرد در جنگ ایران به یک نقطه عطف حساس نزدیک شده است؛ جایی که باید درباره ازسرگیری حملات گسترده با هدف پایان دادن به درگیری تصمیم بگیرد.
🔹
«تصمیم بزرگی…</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/690711" target="_blank">📅 20:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690710">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
ترامپ مدعی شد: تصمیم بزرگی در پیش دارم؛ یا وارد عمل می‌شوم یا نه
🔹
ترامپ روز پنج‌شنبه به «آکسیوس» ادعا کرد در جنگ ایران به یک نقطه عطف حساس نزدیک شده است؛ جایی که باید درباره ازسرگیری حملات گسترده با هدف پایان دادن به درگیری تصمیم بگیرد.
🔹
«تصمیم بزرگی در پیش دارم. آیا می‌خواهم وارد عمل شوم و آنها را نابود کنم یا نه؟ این تصمیم بزرگی است. هر اتفاقی ممکن است از طرف من بیفتد./ انتخاب
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/690710" target="_blank">📅 20:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690709">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnDfYApZ6Ba4w4Pwfheyjnx1GOvSlgSs1OcdMIoUb9s5ee4GvfB5gYSyxJQcXvUJiVqgaDSxHsTRHf4ekKE1sB4kj5RrVmYnAFNRG-SL0GXFkFsVXpv5YxYz_KE7cdWxOhJ_s1JzUbN1OpHTM0lgF1U1vyU60xde89npitWDuFF6SM70FbeqV1-NI29JkD21YN2vL30BDKqwh3T6tOKO3QOXKoN7M5tPXyxxLSlbOnKg5Yf5_Fx7mL6zb5hxki8cWDJooTbgV84kdHuSwfJ64WvUZjp7jDKANbBVh-tpjS7J_fJwezSjngnc0AAbmoJmUEGLHyEHTL-UquZ2dSiZVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سه آبگیر، سه رنگ، یک بهشت در گیلان
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/690709" target="_blank">📅 20:41 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690707">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
مالیات هر نخ سیگار ایرانی در سال ۱۴۰۵، ۷۲ تومان تعیین شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/690707" target="_blank">📅 20:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690705">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e63e039be7.mp4?token=gNJNe9OMvFef8jSA2Qej3FqAihQMzr9zue9r4V37twueU-igJVbQOx6V7u33efRai9bbuUP8kVvli9WdZXzRdaoCXOddddrd67SdUtWsvLaUajvxR00cWnQL2kvb5mRMaAulGVzbAvk_bnrKF8zauKStMb0yrN2JGkVd_ucKtnWe_SGL97q92lol35-rDy4zKFxAvSJqYMBgoJQ45Yw7FJAY6ii4O7uLGyJ-5dR3966g_C4hJjaOM76xXdC7OEGdx6PqW6Xde7FkkvsxT-vWnjGHvCICcdjmIyh5E57XAwbxkZH3Y8vvy5QfpLT2mb_gHbE9SAHQjLFuXOc0YN0OaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e63e039be7.mp4?token=gNJNe9OMvFef8jSA2Qej3FqAihQMzr9zue9r4V37twueU-igJVbQOx6V7u33efRai9bbuUP8kVvli9WdZXzRdaoCXOddddrd67SdUtWsvLaUajvxR00cWnQL2kvb5mRMaAulGVzbAvk_bnrKF8zauKStMb0yrN2JGkVd_ucKtnWe_SGL97q92lol35-rDy4zKFxAvSJqYMBgoJQ45Yw7FJAY6ii4O7uLGyJ-5dR3966g_C4hJjaOM76xXdC7OEGdx6PqW6Xde7FkkvsxT-vWnjGHvCICcdjmIyh5E57XAwbxkZH3Y8vvy5QfpLT2mb_gHbE9SAHQjLFuXOc0YN0OaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زدن پهپادی سعودی توسط انصارلله
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/690705" target="_blank">📅 20:23 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690704">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/419537b841.mp4?token=nniIo3WxeJpwEK5kymo0XIaDfkGYmKZG5Bmj-QphM4tVXhr-IqpNlBqs2QhLMADO1hjYeo1i6bmrdtkfpDHlcX043vnOaNr4_eWVkfVOmMaacgHmVWeDmGDfMVrj8LANfPtIkLGoqzmNKbVHF9bZRs4gd-fRSUmdWFpZ0V4B9rB9hUx1iErRt_XAc7OULze5lQRdEWa_bkEKSef25Gwbd8eWrukBYVIyDc5DQz1AyaImpNFGigQOPr00zJ9fBtWGa4KTCDRLE1sZd9OdMDpZB7NmrjhUgN9DoSoe1PbYPkhDDNxyffMsRuSulobF4aWiP_iMiZLANk-jlbiocoHgQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/419537b841.mp4?token=nniIo3WxeJpwEK5kymo0XIaDfkGYmKZG5Bmj-QphM4tVXhr-IqpNlBqs2QhLMADO1hjYeo1i6bmrdtkfpDHlcX043vnOaNr4_eWVkfVOmMaacgHmVWeDmGDfMVrj8LANfPtIkLGoqzmNKbVHF9bZRs4gd-fRSUmdWFpZ0V4B9rB9hUx1iErRt_XAc7OULze5lQRdEWa_bkEKSef25Gwbd8eWrukBYVIyDc5DQz1AyaImpNFGigQOPr00zJ9fBtWGa4KTCDRLE1sZd9OdMDpZB7NmrjhUgN9DoSoe1PbYPkhDDNxyffMsRuSulobF4aWiP_iMiZLANk-jlbiocoHgQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قبل از اینکه گوشیتو بدی برای تعمیر، برای حفظ اطلاعات خصوصیت این کارو بکن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/690704" target="_blank">📅 20:23 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690703">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
وزیر دفاع پاکستان: «توافق مکه» در صورتی که عربستان با حملات بیشتری روبه‌رو شود، می‌تواند فعال گردد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/690703" target="_blank">📅 20:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690702">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
احتمال شنیده شدن صدای انفجارهای کنترل‌شده در ساوه
🔹
هم‌زمان با برگزاری نمایش بزرگ محیطی و میدانی، صدای تیراندازی و انفجارهای محدود و کنترل‌شده از شنبه ۲۸ شهریورماه به مدت ۷ شب در این شهر شنیده خواهد شد.
#اخبار_مرکزی
در فضای مجازی
👇
@akhbar_markazi</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/690702" target="_blank">📅 20:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690701">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfiWkKhncuCLLitG9-YRH87By7PJuXhpA8Rn-MVGSlr_EtYOaIATDV8pDeRuFSUKBkxzudiMeYiFJBOMgh7CDeIyWVJKoqkTnmLSTExH57vT4grW0whLWr7bn-UB_GUV7bNvxqYOnzPCIydyLqBv1h7bdr7bw0GUsMMaWs_P5GmA-4jrCyB30emlK8aCbVL3-XLotMCobuZLHphfsL6U-xWd7zm2Kc6qjCzg_JCWSawlOu_9ctuqyUIciiRNTxCTfE95G3WVhvbCM69pbI7VEt-2Yjlumj55B2mgThzcS_aiDgMb1netLeQn0Lm-1XYtnQiCBzn0DmL1lJf-NthIWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دشمن واقعی
🔹
توصیه‌ی مؤکّد و مکرّر این‌جانب به حکّام کشورهای اسلامی خصوصاً کشورهای منطقه غرب آسیا و حاشیه خلیج فارس این است که دشمن واقعی خود را بشناسید و نقشه‌اش را دریافته، با آن مقابله نمایید.
🔹
بخشی از پیام رهبر انقلاب اسلامی به مناسبت هفته وحدت | ۸/شهریور/۱۴۰۵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/690701" target="_blank">📅 20:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690697">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k76WBizo5NdgvGk8fereDpV1s9rlt00a9s8Nd0KUuHeZ2tYWi01ehIarLm3js79oWmCJ0JcmI0E7RdX5N65WyrTMI7UOaYsZ13RxfMY7bBXT-rJn6wRywwmioH0R--dzo941pDCH6Nkd8c-y95YYPysuLwmcG7eZNuoJgsifNbzneIzOtrSpzdsEgeggpysot7JywxchlDClTW9alTFya3sCineSorUMUvg63owOGdNY2jq9eSCDWdDeINCeKtxiKImJgIVaUzVtnxyUowTu9jKEG7IwcxrFB1_GgFpndzc1kj6UB6oZ1x55EtIslt2OTtu1gSkSnCXXaX0D2g_Ywg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارزش باشگاه‌های لیگ برتر ایران
پرسپولیس ارزشمندترین تیم این فصل لیگ برتر ایران شد
./ ترانسفرمارکت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/690697" target="_blank">📅 19:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690696">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QjtRaUh-ooq970L7fp4TVC0MhE9BrhP4R9SzRSR6cHLlHurVGn3RBGiAA6ZLY6LLuIGr-NKaAjNcokJMe2fgr9dbNwroHcrigdZQZH23Fr2CeknoKBWreN3PohcLmfqPuUzCAT2CDif1w9y7DOamwq2DoG6uacr-dYs9omTsdQ1v-XAMMtS8i5X9GRfEw2UoWDmC3AwpGkGptVIbWyq2BeTMhw1wZgBKeFBTgYdhCLaVAoKuyXWr2y9OoF5-OP9Nbsno9gcuCZnoI13RZdcGk1jJA6ODvN0RklMbN3nXPdK43WQ3IyRAzX4kH_NQqrOSOn-2mNWhFXWi-EdIVb6tZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وقوع حادثه امنیتی برای یک نفت‌کش در سواحل یمن
🔹
سازمان تجارت دریایی انگلیس گزارش داد یک نفت‌کش در ۷۵ مایلی شرق بندر عدن توسط یک قایق ناشناس تعقیب شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/690696" target="_blank">📅 19:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690695">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
مقام‌های کشورهای عربی به ایران گفته‌اند که می‌دانند هدف اسرائیل پس از ایران، خودِ آن‌ها هستند
احمد دستمالچیان ، سفیر سابق ایران در لبنان و اردن در
#گفتگو
با خبرفوری:
🔹
این‌گونه نیست که کشورهای منطقه علیه ایران با اسرائیل همراه باشند؛ این موضوع دو دلیل اصلی دارد: نخست خواست ملت‌های خودِ آن کشورها و دوم، هشدارهایی که مسئولان این کشورها دریافت کرده‌اند.
🔹
اسرائیل رژیمی توسعه‌طلب و تجاوزگر است که تمام منطقه را هدف قرار داده است. تنها هدف این رژیم، با همکاری ایالات متحده، تسلط بر منابع نفتی، انسانی و سرزمینی خاورمیانه است.
🔹
از ابتدای پیروزی انقلاب اسلامی تا امروز، اولویت اصلی سیاست خارجی ایران، داشتن روابط حسنه با همسایگان، به‌ویژه کشورهای عربی حاشیه خلیج فارس بوده است و جمهوری اسلامی همواره دست دوستی و برادری به سوی آنان دراز کرده است.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/690695" target="_blank">📅 19:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690694">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
جنگ ایران کشورهای عربی را به فکر سامانه ضدپهپاد انداخت  بلومبرگ:
🔹
جنگ علیه ایران، کشور‌های حوزه خلیج فارس را به سمت هزینه‌های کلان برای سامانه‌های ضد پهپادی سوق داده آنچه اکنون شاهد آن هستیم، احتمالاً بزرگ‌ترین موج هزینه‌کرد در تاریخ دفاعی خلیج فارس است.…</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/690694" target="_blank">📅 19:39 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690693">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c76888993.mp4?token=qSLVY4UwdbGdFcICrURwuMBLLEIkS_5dV7d4sxuNjQHB0YTlDpgdzTBWDoj6gDhNTcxqAznyjnxRWC_qsifNsbVuAyUTIMmdlD1TxTQEy7N8LeV6XXc0vfU1kTAjgAs1vAqkizAKxHH7V0EtgBvlBG-5KKu0R9XPhObeORWgKGlZ_CZdvzpKtMLcsoFpSIw7jyHAlzdFyfOp41_ONJnIvgYjmLoSstLbA8vN25HBhqyMMPUHH250GwB_zVkQkfdpMTeUthaAl6KdiXTJEsAAx-GhQfmHS2_x1e58MGFnw-8YRErTIPx3rXgx8vLF2gt9sFwrGpX9GtyaQvKh-Zt-_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c76888993.mp4?token=qSLVY4UwdbGdFcICrURwuMBLLEIkS_5dV7d4sxuNjQHB0YTlDpgdzTBWDoj6gDhNTcxqAznyjnxRWC_qsifNsbVuAyUTIMmdlD1TxTQEy7N8LeV6XXc0vfU1kTAjgAs1vAqkizAKxHH7V0EtgBvlBG-5KKu0R9XPhObeORWgKGlZ_CZdvzpKtMLcsoFpSIw7jyHAlzdFyfOp41_ONJnIvgYjmLoSstLbA8vN25HBhqyMMPUHH250GwB_zVkQkfdpMTeUthaAl6KdiXTJEsAAx-GhQfmHS2_x1e58MGFnw-8YRErTIPx3rXgx8vLF2gt9sFwrGpX9GtyaQvKh-Zt-_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رونمایی از خودروی ۲۰۰ میلیاردی در تهران
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/690693" target="_blank">📅 19:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690692">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee665b774d.mp4?token=Gacza1iltwvV9ZPhCbdMX_smLQl6aQA6rdnb_FlYYygA6rzB1NmbvTWrgm37DNgR6O3oJIxRi0S43OwbgNbvwR-aiSkiujYRhKTor4Qxzorj-LukWkFViq-cu8etM4lya7D8lHcQvIVVwNagEuJiLwTYTgya0aM4sMNheYPJIo2ZTR16S5wrRS78z45FIuSTnE2L9vlxpIvSDWYrZ00N8z1ZARZB-GEX-K9DXrzt1wKJpVjNIGTJm4cvH1ezTgbbLySNmi_U96jeaxI8QhyBHcLJo5bzSfZsob-2QDGNBT5JHlT7iC_XbYt6EuECE_bhildqemQ5h96-5MLt68R9uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee665b774d.mp4?token=Gacza1iltwvV9ZPhCbdMX_smLQl6aQA6rdnb_FlYYygA6rzB1NmbvTWrgm37DNgR6O3oJIxRi0S43OwbgNbvwR-aiSkiujYRhKTor4Qxzorj-LukWkFViq-cu8etM4lya7D8lHcQvIVVwNagEuJiLwTYTgya0aM4sMNheYPJIo2ZTR16S5wrRS78z45FIuSTnE2L9vlxpIvSDWYrZ00N8z1ZARZB-GEX-K9DXrzt1wKJpVjNIGTJm4cvH1ezTgbbLySNmi_U96jeaxI8QhyBHcLJo5bzSfZsob-2QDGNBT5JHlT7iC_XbYt6EuECE_bhildqemQ5h96-5MLt68R9uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زاکانی در پاسخ به اظهارات روحانی: برای ‌پاسخ به کسی که به خانه ما حمله کرده که همه‌پرسی نمی‌کنند/ یا از سر خوش‌خیالی این پیشنهاد‌ها را مطرح می‌کنند یا از سر ترس/ به خانه ما حمله شده و ما مقاومت می‌کنیم و باید سایه تهدید، تحریم و جنگ را از سر کشور کنار بزنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/690692" target="_blank">📅 19:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690691">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/msNrCNDKJCBS_sT_LnYvuw7Z0ugAL8v06_K2aI_wusRfgSi41aU0rzoKCT-XAhEhKf1qVo68pk6Cp_fI9b9QoaD1DyclMhiTFkjJeGS5gQ5tyFqOxaF9Y49MP1WOh3SUx4_XHCS3SLspB0z7PlYitHS0CAZSnHBpFH9RwEzWZrdFNBVLnR8GNF_PIAxkX17BgrE8wXmwaLR_XsP_UhvM7pT4ZspdZr4S-IbFXAQ-ynvTKIEAAPIg8BBYRHjmcCqYOXb-4NTQcPg1u17KOnsedffwh2YqEuKxLAsgNKJ1V58RSN6A5mKbVZWmFBMqZtzlTMCDji1rgk538FerCaLPCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زنگ خطر انتخاباتی برای ترامپ/ ۴۷ روز تا انتخابات
🔹
در انتخابات میان‌دوره‌ای ۲۰۲۶ آمریکا، رقابت اصلی میان دموکرات‌ها و جمهوری‌خواهان (حزب ترامپ) است؛ برخی برآوردها از افزایش شانس دموکرات‌ها برای کسب کرسی‌های کنگره خبر می‌دهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/690691" target="_blank">📅 19:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690690">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SIdHnAgiNnicwAmkceTduB_aT85h_nTk9vXXAYROsYlx_r6Ob6_g8qIy2XKdMycrENMzZT3x4mWXsFsMY-kLwfoRoGlQqO1VAq005Wi0cNrL0OGVnAMg4PY4PldwaB7MkQWKAe2xUtSFd8ijua5XcUj4VRaRtH9ck2kdSKIV7A-NgPEof4viiBSzAIKTaszc-wRwXYntMP9MS3uCDpsOhT18i93pMnFv8fMPP67UaR8efyCf2c-29LEwEayQkIHjj2gK17p2zL1xsuWM74atteEGgpr6viFdJ9juC3LZt4L9a1HeSM656XoB38IBCZLEZY9J02eD3IDKWfWoop8KrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
پک هدیه «رضا جان»
ترکیبی دلنشین از سه یادگار ارزشمند و معنوی که کنار هم، هدیه‌ای شایسته و خوش‌سلیقه می‌سازند. این بسته، انتخابی مناسب برای هدیه دادن در مناسبت‌های خاص و ثبت لحظه‌ای ماندگار از ارادت است.
✨
مشخصات محصول:
▫️
بسته هدیه شمس: ۵۰۰,۰۰۰ تومان
▫️
فرش سقاخانه: ۴۹۶,۰۰۰ تومان
▫️
عطر و نگین: ۶۰۰,۰۰۰ تومان
💰
قیمت اصلی: ۱,۵۹۶,۰۰۰ تومان
🔥
قیمت با تخفیف ویژه: ۱,۲۹۶,۰۰۰ تومان
⏳
موجودی محدود؛ برای ثبت سفارش، همین حالا اقدام کنید.
📩
ثبت سفارش:
@gharar_order
👁
مشاهده محصولات بیشتر:
@ghararshop
ghararshop.com
قرار؛ تجلی هنر و ارادت</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/690690" target="_blank">📅 19:24 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690689">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
جنگ ایران کشورهای عربی را به فکر سامانه ضدپهپاد انداخت
بلومبرگ:
🔹
جنگ علیه ایران، کشور‌های حوزه خلیج فارس را به سمت هزینه‌های کلان برای سامانه‌های ضد پهپادی سوق داده آنچه اکنون شاهد آن هستیم، احتمالاً بزرگ‌ترین موج هزینه‌کرد در تاریخ دفاعی خلیج فارس است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/690689" target="_blank">📅 19:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690686">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gXy7Ota5_IN6haJXq-3IXsXB62nv1Nb-Q-24gSERikywh2CbPW1VfzdW4YTcxC1VT9NDNcnq0EM9pdJjzobFoP0x-gTyqe0-7sQi2bWMFCxPhIi_cAHhHwh1d7UOuqfle_MeLZxJJafZaxpoG1B6cEpDxUE-HBXffOpidoH2SV6k8I3IdqEsogt-6BkuvWOwmoqEzzG2mLbPzted_QWBzyljYhjojD_aFqIcS_xyhR_1MH6VNZDEjyhW8cv-3SqZwi_5WID-FOa7ijR9EFMFcI3lOeja1SZRFicbmLTseBMYw7Cg52nMHaHyQmzwCYzCNsj1rmq7qAh8efYJBuHxkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tMXxpPxe4LchrBgriiH2k7d5AV4Oj91TQY0HLGmof8-nEd4ix2Vf1iBglI6ue_I2O03SiqVXD2L1L_wcSCf8cpF71rCmx9grjIvJBlNzrkG39D_H9qrxGzE2vk1DWHfOGxYeZ76U0ZrpVHV47WgibkrHT1lTRvoQOyDNUXsAwzSaYpeFn3JrORPGM2d_FocbT-jnYNT_eulbMbm3CZCEkoGUWq0EoANrfI8fh-SSWK5PQcDb2BxePpP_SnLVv6-1GioMMpAeAal_BhtmLHU2yJBHWogxsAHluTO9R51qJLzMZdeGKalvoSVUjXP4VsD2LmjbYHvTORuJaMT92v-xtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دستگاهی که به گوشی می‌چسبد و صدای شما را تغییر می‌دهد
🔹
گجت Key Pocket، با اتصال مغناطیسی به گوشی، صدای زنده را تغییر می‌دهد، با دور زدن محدودیت‌های نرم‌افزاری، صدا را مستقیم به اپلیکیشن‌ها می‌فرستد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/690686" target="_blank">📅 19:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690685">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2705b1db6d.mp4?token=CAHF3N6SbV2p7GlcF3_HJoe7NrRUGD2VOb3MR5BcApHNMxnls8e1dJjdNqwbmcpbkCo6qhuw2UN_e80Kghe1Xsu0-XzkqfxvNrqRkdTgwkPYY2qeAudJ1n38ySh8yOXFoYb1DODeb0BDBjprDicLRD9GuGrC2LHyTzsvyR4q3OGtPwoiKBuinVnyCZvHuUpDhCVOmsDfG2NOiZmLA04mfNdVsqxnqmuBkqPwEF3AvJzb-q2YjyMO9VT99kt5wTme7ZTMFXJpG2pnBHyA__9MsJKgwbFuA_z7iZjajEZMv9qquMPjZ-EZkNCwoOZqEnqf4d0D85ajWlOCIrepATjblg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2705b1db6d.mp4?token=CAHF3N6SbV2p7GlcF3_HJoe7NrRUGD2VOb3MR5BcApHNMxnls8e1dJjdNqwbmcpbkCo6qhuw2UN_e80Kghe1Xsu0-XzkqfxvNrqRkdTgwkPYY2qeAudJ1n38ySh8yOXFoYb1DODeb0BDBjprDicLRD9GuGrC2LHyTzsvyR4q3OGtPwoiKBuinVnyCZvHuUpDhCVOmsDfG2NOiZmLA04mfNdVsqxnqmuBkqPwEF3AvJzb-q2YjyMO9VT99kt5wTme7ZTMFXJpG2pnBHyA__9MsJKgwbFuA_z7iZjajEZMv9qquMPjZ-EZkNCwoOZqEnqf4d0D85ajWlOCIrepATjblg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آسیاب آبی خوانسار تنها آسیاب آبی فعال در کل ایران است که هنوز با سیستم ۲۰۰۰ سال پیش کار می‌کند و همه بازدیدکنندگان را شگفت‌زده کرده‌است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/690685" target="_blank">📅 19:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690684">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bh7mZ9BqhIAPrcjxwXyZYmdQ7_21QR5WlxAlROdQamIcwj__-vguEelc-uI_m3vIahFQw5NHmAM5s5lIAU4pUm9EbZP0a-j4JQzkbi-2orIavZBC7Naf_88c-vXrRyFDRF3CztnDjrG2RaDCgNNeLL9fnSjgAFjJKFbmWBD5hEQKEbSDBkvaEIkgpCamJIC3YvGI2I5o4aQTyV4ixYmlwB6tYhdRIUHL96dPU7zA7c9SHHA62jWrg3mcyPh9waAvc5ZUuLXVzm6UKKNVxg1n0uAi5VjtOXFfKukRyPjGXKQZzEXdAzSrVjL1XCQFV63OYmbXZFmfiySuKH9S7GFz0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اولین عکس از یکی از دو قاتل پرونده قتل عام ۵ عضو خانواده در پونک تهران  #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/690684" target="_blank">📅 18:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690683">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jAQRBzbICrtL9eLT3RKGglQrPjgyNkKJszOwHuRL_bprIXEDB0DJ2yFMGRDS2A63TSvWtpSRMsbwgRH3FA_vpE5qL1cTtjsHZHqYTYh_TtuYcMTMk9nmajUKOtvIh2ZAsT7PH1JmJD5yfdY8UAXmyvLaPVEpYVWcGc6voFkSsdL0LRrmuaOEw-rI3Hp-4GdKDeFMTS3Vmj6l6oLDHGIHad_-uQ1b7hXcb3yolHxED2mw-v47Ewa_S9xkTBNrzTR5TBEfkYtE8wparUmC7qGFYErF8ZZfD0Axw0UX8Ihs0KoymX334NO5vvSqXvDtg-Meubg8GX0UqiYug9s38doM0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با عرض معذرت
🔹
محمدرضا عارف، معاون اول رئیس جمهور در مجمع صنفی کانون استادان دانشگاه: از مردم عذرخواهی می‌کنیم و  شرمنده‌ایم که امروز دخل و خرج مردم با هم نمی‌خواند. نمی‌توان با تورم ۴۰ درصدی و رشد ۲۰ درصدی حقوق در دو سال گذشته، انتظار داشت مردم بتوانند زندگی خود را اداره کنند و اگر تورم امسال به بالای ۶۰ یا ۷۰ درصد برسد و افزایش حقوق ۲۰ درصد باشد، ادامه زندگی برای مردم امکان‌پذیر نخواهد بود.
🔹
هشتصدوشصت‌وسومین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/690683" target="_blank">📅 18:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690682">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
واکنش شهروند آمریکایی به افزایش قیمت بنزین: سه بار بهت رأی دادم ترامپ و این تشکریه که ازت می‌گیرم؟ تو خائنی!
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/690682" target="_blank">📅 18:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690681">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
آناتولی به نقل از منابع پاکستانی: عاصم منیر از ایران خواسته تا انصارالله یمن را متقاعد کند که به تأسیسات انرژی عربستان حمله نکند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/690681" target="_blank">📅 18:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690680">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e82885dd77.mp4?token=u9Uu4mV8RF-YO0waX_abiJG2GrWHf-CAL3_vjOp2HOEYntBOSASeTlPq5CkLftw1PLQ37hkL2VaEFlHAPFBKlWcQpBGI5iLYqsa-zmhHRGCL86VYLTr9UjynvzAXB8naJW32P0WD480C7279C5i4IE2OaG9T6wf3DcSDqWf03Pjo8QJMLb6V9uvPgwpEOpG8jsPyUvxnrgqFTapqzwVryLONfgqnqXXOVvTASPwsQR6qMqz_OdN4LqnkECrY-FnsX8nrB1X37ppt7nXy0MQnsg9-Faeur4qqF9bgN2zvDFS56SLyf3YaaUIOu4Fxggo8koprrYvu4lKVg40uBlfO0T3uCpjT2jqiOMB1zIbjRcGmpf0oSChkWuKS6b0MVeGOo3N9dC14kCG4sWlPoh7tPfW4a7VAnL6TW3zPlJhCuUSK72xirGik8P4_9MM-WQLfLK1lw9lUatngq9UkSI01ELTlaeHYksHK2aNLX9InB3yttz762qPTO0SFlwBG5P3X8e77JbrhZKLK3Wue9ZZL7CpVq9MBWe6RnKwYJqGFMHKdk-jF5fNNjNmIRJBN9ibnIIXpWgiW66EU01WVm686wZDZd1HDZs0LDVPd_ldMx-E_1tjxhBAox35osftAYfia_R1fEL8-f-nHa2Fy40DLEGeesgqungkSXWgqu01AhG8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e82885dd77.mp4?token=u9Uu4mV8RF-YO0waX_abiJG2GrWHf-CAL3_vjOp2HOEYntBOSASeTlPq5CkLftw1PLQ37hkL2VaEFlHAPFBKlWcQpBGI5iLYqsa-zmhHRGCL86VYLTr9UjynvzAXB8naJW32P0WD480C7279C5i4IE2OaG9T6wf3DcSDqWf03Pjo8QJMLb6V9uvPgwpEOpG8jsPyUvxnrgqFTapqzwVryLONfgqnqXXOVvTASPwsQR6qMqz_OdN4LqnkECrY-FnsX8nrB1X37ppt7nXy0MQnsg9-Faeur4qqF9bgN2zvDFS56SLyf3YaaUIOu4Fxggo8koprrYvu4lKVg40uBlfO0T3uCpjT2jqiOMB1zIbjRcGmpf0oSChkWuKS6b0MVeGOo3N9dC14kCG4sWlPoh7tPfW4a7VAnL6TW3zPlJhCuUSK72xirGik8P4_9MM-WQLfLK1lw9lUatngq9UkSI01ELTlaeHYksHK2aNLX9InB3yttz762qPTO0SFlwBG5P3X8e77JbrhZKLK3Wue9ZZL7CpVq9MBWe6RnKwYJqGFMHKdk-jF5fNNjNmIRJBN9ibnIIXpWgiW66EU01WVm686wZDZd1HDZs0LDVPd_ldMx-E_1tjxhBAox35osftAYfia_R1fEL8-f-nHa2Fy40DLEGeesgqungkSXWgqu01AhG8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غول پیکرترین و عجیب‌ترین امواج ثبت شده زمین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/690680" target="_blank">📅 18:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690679">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
برنج، افزایش قیمت افسارگسیخته نخواهد داشت
محمد مختاریانی، رئیس انجمن واردکنندگان و صادرکنندگان برنج ایران در
#گفتگو
با خبرفوری:
🔹
با وجود محاصره دریایی و اقتصادی مشکلی برای تأمین برنج در ماه‌های آینده نداریم و برنج هندی از مسیر دریایی و برنج پاکستانی از مرز زمینی وارد می‌شود.
🔹
با توجه به تولید خوب داخلی و واردات انجام‌ شده، پیش‌بینی افزایش قیمت آنچنانی نداریم و برنج در محدوده تورم نوسان خواهد داشت اما جهش افسارگسیخته قیمت‌ها اتفاق نمی‌افتد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/690679" target="_blank">📅 18:23 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690678">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jh9fqiAMB7gt_QTq-FqlWO_ra-U47PcnoXzHaqtzb4L9WXQgIWRMrlbQ_-dkEl6POGuVAkxJraq2-j6DeS9zIJLcEAmH2TjsxGmyABbakbw7_mEt0BDFeheH7hjUI46uB7uUPipcojGxm7s-DHrHGW96IrzwRZe6v16kS1eqi36J-fA_LIuk6uj0EYQi9_oJZTGUxwvr28klBzKvkDyjJwybeypEfe6v7XhIaWAyYOhp30hNbVUb-3JkqJDwgq7tH_4QswaY6xCVatllvS_sXuMG33gVdt2gkwz9_XNLR_QyxTUUXXblvRXE0oTdZsqZ_mKHMBjWzWZ5iaIQE_HHFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این‌بار به میزبانی استانبول/ برنامه سوپرجام اسپانیا ۲۰۲۷ اعلام شد
🔹
سوپرجام اسپانیا ۲۰۲۷ از ۱۳ تا ۱۷ بهمن ۱۴۰۵ در استانبول برگزار می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/690678" target="_blank">📅 18:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690677">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11691d20c7.mp4?token=U71mC_sK9IuFNiBm_giZyhz_JpoOBT2JZuZsfCk7PkRABGGZs106yc4W-0ykY8ai198flJHFD1cpZx28xqduN9kzVpklY6HtdDacCKh5PX93DnhrruYZWN4byppBa2VrQfV7Tmf4ZIUZt2tRwcFND-v5FxB4xoIEchpAyoz3ttR_W9EqRpAnHRzqIpp-7Ek3d44K5mh2feIlm9l0O-36U_RwjXck1QV2EW60_M3ufuL7GLFCGSVrVDyAnAnOHUhAuVA4W-5q0zhXVqVR7yf6aLfhX0puR09q2QrdNfcHpydMk1yB2oP9K0OGzsb_Jl2kNQ80y35az2FEmu3yZOB3Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11691d20c7.mp4?token=U71mC_sK9IuFNiBm_giZyhz_JpoOBT2JZuZsfCk7PkRABGGZs106yc4W-0ykY8ai198flJHFD1cpZx28xqduN9kzVpklY6HtdDacCKh5PX93DnhrruYZWN4byppBa2VrQfV7Tmf4ZIUZt2tRwcFND-v5FxB4xoIEchpAyoz3ttR_W9EqRpAnHRzqIpp-7Ek3d44K5mh2feIlm9l0O-36U_RwjXck1QV2EW60_M3ufuL7GLFCGSVrVDyAnAnOHUhAuVA4W-5q0zhXVqVR7yf6aLfhX0puR09q2QrdNfcHpydMk1yB2oP9K0OGzsb_Jl2kNQ80y35az2FEmu3yZOB3Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این ویدیو رو ببینید تا در طلافروشی سرتون کلاه نره
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/690677" target="_blank">📅 18:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690676">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه ملت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e913bccf1.mp4?token=K8k3aMFs-WSij3y14-wj1X45kz3vmnqfMA0oI9jNDpHk48Q9jC-SXkM8gMkz4eSGgiP_g7Hf7Tn1A7St2wNcY_do9l6W3LgEAnKtDe9imx1Y48awHfDdGis4-mJh_S86u3iLfQ_oPhmzZZp320DpgaNCiKRTvocM9VD2cNZqjsVCA1ps5Vxa48sBhFuMzehaIcMsSAjtrCzqQgFYKTCJfyEu4jvPJiMP_lh5o-Ie9GOS3Jtn2FYgcFqgcsYjQw0Dt4fl_rVfs2gHu0GTf6L1tOWbLj_pfKghMzSMNze-EiGkzxLCtQqZjGvBPaXssZt1sdyUM23aQsLXsGmu6HkhnzJVbsI565t4fpwpxwLTUrFTuAL_DyIQb2oTNCdojP7Dc4aCtJv_ksbAmOagvG-UJGK7IT9sfqrh3LYIkiHg7YugmLG0Ysq0iK75uMBmkGCGgaLjaobV4YEZrl51rC8FYxG-fbRPrc9TAcO4yKM23zvpUmTdb-3ABUICRc5sp31DHU0FAVPQA14qapXvCsoXYZO4IWQBl7flwfBKJp-oZ8vp11_NWgqbblEjvo81Ifq_T-IFTRNJtgbOM_VMmH2ewlb3ctrtGAnHu6fmtESDWMsrEDYFZb4TS7ppWLz72CvproKLexdWm86D9hEloqf-WfUlkhxESoSq1pSexgZjbPs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e913bccf1.mp4?token=K8k3aMFs-WSij3y14-wj1X45kz3vmnqfMA0oI9jNDpHk48Q9jC-SXkM8gMkz4eSGgiP_g7Hf7Tn1A7St2wNcY_do9l6W3LgEAnKtDe9imx1Y48awHfDdGis4-mJh_S86u3iLfQ_oPhmzZZp320DpgaNCiKRTvocM9VD2cNZqjsVCA1ps5Vxa48sBhFuMzehaIcMsSAjtrCzqQgFYKTCJfyEu4jvPJiMP_lh5o-Ie9GOS3Jtn2FYgcFqgcsYjQw0Dt4fl_rVfs2gHu0GTf6L1tOWbLj_pfKghMzSMNze-EiGkzxLCtQqZjGvBPaXssZt1sdyUM23aQsLXsGmu6HkhnzJVbsI565t4fpwpxwLTUrFTuAL_DyIQb2oTNCdojP7Dc4aCtJv_ksbAmOagvG-UJGK7IT9sfqrh3LYIkiHg7YugmLG0Ysq0iK75uMBmkGCGgaLjaobV4YEZrl51rC8FYxG-fbRPrc9TAcO4yKM23zvpUmTdb-3ABUICRc5sp31DHU0FAVPQA14qapXvCsoXYZO4IWQBl7flwfBKJp-oZ8vp11_NWgqbblEjvo81Ifq_T-IFTRNJtgbOM_VMmH2ewlb3ctrtGAnHu6fmtESDWMsrEDYFZb4TS7ppWLz72CvproKLexdWm86D9hEloqf-WfUlkhxESoSq1pSexgZjbPs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
ارجان؛ جام ارزشمند زندگی
🔶
«بیمه زندگی متصل به دارایی ارجان» بیمه ملت، پیوندی میان پوشش‌های بیمه‌ای و فرصت‌های سرمایه‌گذاری.
برای معرفی این محصول، کلیک کنید
✅
بیمه ملت، همراه خانواده
🆔
@Mellatinsurance_official</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/690676" target="_blank">📅 18:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690673">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/729a6facd2.mp4?token=q9zV9_s_SWkdh10mMg6JCPmHHR3kCZpyTMQ3IV4A7uPzZUNspbuyYbNvnbfYhMeEKLL4pnfE8bYtow31wkMkaVpD2Mb1AuFPnbOoQwYA3V5UJVRxC1yps6lDypHP9TZARkdBQ2qAldP_o52lrAesXqD77W39ZvWOl4Zd_3kriHB3xnuSMYMYR0NgDHrLHfAzqvddHjS1S89CCTlS699JcxEoa_He6pgG_zg3WHJOV4yuX21kYt_NL2KsWHIZoM9y5NDvNgW1dwecTMfaNBNPTV51kjfQBHcMmo57KWIdt8eXO10qx3Jgn0vwRSOd09dZOKQiIG2Y0ML0mOKP0m0H8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/729a6facd2.mp4?token=q9zV9_s_SWkdh10mMg6JCPmHHR3kCZpyTMQ3IV4A7uPzZUNspbuyYbNvnbfYhMeEKLL4pnfE8bYtow31wkMkaVpD2Mb1AuFPnbOoQwYA3V5UJVRxC1yps6lDypHP9TZARkdBQ2qAldP_o52lrAesXqD77W39ZvWOl4Zd_3kriHB3xnuSMYMYR0NgDHrLHfAzqvddHjS1S89CCTlS699JcxEoa_He6pgG_zg3WHJOV4yuX21kYt_NL2KsWHIZoM9y5NDvNgW1dwecTMfaNBNPTV51kjfQBHcMmo57KWIdt8eXO10qx3Jgn0vwRSOd09dZOKQiIG2Y0ML0mOKP0m0H8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزافه گویی نماینده بحرین در شورای امنیت: ایران و نیروهای نیابتی‌اش منطقه ما را به هم ریختند
🔹
نماینده روسیه در شورای امنیت: تحریم‌های «اسنپ‌بک» علیه ایران هیچ وجاهت قانونی ندارد
🔹
نماینده انگلیس در شورای امنیت: برای اعمال فشار بیشتر علیه ایران آماده همکاری هستیم
🔹
نماینده چین: با انقضای قطعنامه ۲۲۳۱، بررسی پرونده هسته‌ای ایران در شورای امنیت پایان یافته است
🔹
نماینده آمریکا در شورای امنیت: وتوی تحریم‌ها توسط چین و روسیه خلاف قواعد بین‌المللی است!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/690673" target="_blank">📅 18:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690672">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G24qNOHDY3pV_nQyqrYzJkZxNXiD9ysX0Nh3ZLFwFU98DtxwIE1hm6MDvT9JaLz6PMGHbR4_CX7Uwja7HqaqU5nWlpTgaUJCGfKQaNVY2PPyJ3giZlUjFV22-xGmaboDzUBYkd3uFfWdIfqS_KCC2aGDAtBBLpjfFZpCUkKXEkd-v80vxj6IIpBSd1PW2O1q-QDD0Mbgs9RjDnyajBWAhfNsdC3RyKn4vXYSeMUWr1eG0e-emshrODGEROfEaP7LrMNX-sI1oEpp-ggyrG3L3osbahJIXX2cPrxzI6Bx7uVdRa_h80-IbmcWvpoYPTRL6KqHANzncwCQHWW16Yy9Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کنایه‌ توییتری استقلال به پرسپولیس پس از رد شکایت از آسانی
🔹
چگونه جلوی فوتبال بازی کردن آسانی را بگیریم؟
🔹
خطا؛ چیزی پیدا نشد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/690672" target="_blank">📅 18:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690671">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ab06e42f5.mp4?token=lHgn1f8lzJp-vyACiuXB_Azyq8aA7FTOhLQhvl9mPDhv8jKUX_r618_PE_l9Pv4ub0WrIBYX_p9cJckriTrtEEIG0er89PDEHgMXQRB8OIDd2YypvNTVcjhAIM122INmE1YQ-TyPdfrqhmKk-FP1P3f2YGxev78fc-qeefUT8w6ece83Eo4wqYMjKdriGdugS27itNkGBq6Jf0VupZpZC0XT20VdAcq4GAOKpH9vs9hdc2OaHVy2TuwbCeYpI4w-ZdtgB0w5LuZugpIQox-pKGxKrxBCO5lH9DOxjigqY05rTYS5whDOLl6dKwmLGyuHrMpZX5YTIf8t3cM9b4XOGjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ab06e42f5.mp4?token=lHgn1f8lzJp-vyACiuXB_Azyq8aA7FTOhLQhvl9mPDhv8jKUX_r618_PE_l9Pv4ub0WrIBYX_p9cJckriTrtEEIG0er89PDEHgMXQRB8OIDd2YypvNTVcjhAIM122INmE1YQ-TyPdfrqhmKk-FP1P3f2YGxev78fc-qeefUT8w6ece83Eo4wqYMjKdriGdugS27itNkGBq6Jf0VupZpZC0XT20VdAcq4GAOKpH9vs9hdc2OaHVy2TuwbCeYpI4w-ZdtgB0w5LuZugpIQox-pKGxKrxBCO5lH9DOxjigqY05rTYS5whDOLl6dKwmLGyuHrMpZX5YTIf8t3cM9b4XOGjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در انگلیسی یک سری کلمه‌های جالب داریم که از تکرار دو کلمه شبیه به هم ساخته میشن و خیلی کاربرد دارن #زبان_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/690671" target="_blank">📅 18:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690670">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24536a38e5.mp4?token=pZ-EQbd7enxT0_VQbPf1kGREGkt0eB4sSZIPs0XMgxFIxvwRDTnSOJiaHnRcWKUboqEkf8S1QM6WtELaO67RONc3RzvvOgOk-UsrtQTbppKqOjfl0JNFDH1KOmdH3Ww9PdV-cQLusvTlWwLPKGh_V1YBxnNAtXmV0tSxu0YROnFDNEh6I4EijdMnby2sT4AWvO15NPg4en6tgBXn29JR-RQsRX6Tpmxk6oVaA14hQi4UCrXotQ5N5aKM5dt9Jx5vSb2L9o5itsVs5d-aNeHYOk5-cA7Z_uV4OfJDy4vpo2e1QanC_qJGsVerX_24bvy57GoC-ns64AUCddgx1fL1KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24536a38e5.mp4?token=pZ-EQbd7enxT0_VQbPf1kGREGkt0eB4sSZIPs0XMgxFIxvwRDTnSOJiaHnRcWKUboqEkf8S1QM6WtELaO67RONc3RzvvOgOk-UsrtQTbppKqOjfl0JNFDH1KOmdH3Ww9PdV-cQLusvTlWwLPKGh_V1YBxnNAtXmV0tSxu0YROnFDNEh6I4EijdMnby2sT4AWvO15NPg4en6tgBXn29JR-RQsRX6Tpmxk6oVaA14hQi4UCrXotQ5N5aKM5dt9Jx5vSb2L9o5itsVs5d-aNeHYOk5-cA7Z_uV4OfJDy4vpo2e1QanC_qJGsVerX_24bvy57GoC-ns64AUCddgx1fL1KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جدیدترین بیلبوردهای شهری تهران که واکنش‌های زیادی در فضای مجازی به دنبال داشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/690670" target="_blank">📅 17:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690669">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
الجزیره: روسیه و چین پیش‌نویس قطعنامه آمریکا در شورای امنیت سازمان ملل متحد برای تمدید ماموریت کمیته تحریم‌های ایران را وتو کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/690669" target="_blank">📅 17:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690668">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/346fb64e2a.mp4?token=RZFZ61nF0nxU4A6N0_KutTpICGaWBhPqB2u-T7Q9uFTfRGhvvbd1484Xf_qNK-WPdo6vWC6NwTDImwMIHtkRIGRpFKTMvldD_KHQpMW7rEU_2OEyxIlZk_2TNCSGSQcYsNQAnzIey9qFvGPb-In0jNLXPTDA_NXlvJzuZUgVmrJvEV8Nb3EO3aiJp9jTpct0I9rDI-AKJu8AhTyjXbT8SxOOaSCB5vdYtg2HwwTxFjE_piuAbcnK3NEw6e6yiTIoVQaiMpTe06nFP5k3CcFX7iNwCijVXhCyTnteYDrnbRTb0WEXyDk3kv5RlKT-tHm-UHuFT4aS2NgnIeqZUMHGJ1VonhaxehI-tH64TgFSwxfP057fvL_ur1JjxW-2HHumfolRK8G76Ll-he2Z91Lc4NqXGrLH9pGC7OyXAJolr7IxkrX6khThUT4f8YyLIQfntRzyJxS6K5uSUvuGU_-uM1KwpEygEyRhgunt7nbOjE-ZDp_rT2dZB9_BvHNca70Lezg93H730C-4pxGoc_oZyvXj3QwedmhngxijLxHcBPrKnBTs1OCbgv9E2nUCaL1Llm6zBkAZxggtxoBLI28z6sdOIkdZWqcCzPo6jmwTCqea_jGHxfkiVkJSl405CyG5P9TNo3FX39q_xihLSJAemhC0Z0KUen3jdBFZ1rr0rnY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/346fb64e2a.mp4?token=RZFZ61nF0nxU4A6N0_KutTpICGaWBhPqB2u-T7Q9uFTfRGhvvbd1484Xf_qNK-WPdo6vWC6NwTDImwMIHtkRIGRpFKTMvldD_KHQpMW7rEU_2OEyxIlZk_2TNCSGSQcYsNQAnzIey9qFvGPb-In0jNLXPTDA_NXlvJzuZUgVmrJvEV8Nb3EO3aiJp9jTpct0I9rDI-AKJu8AhTyjXbT8SxOOaSCB5vdYtg2HwwTxFjE_piuAbcnK3NEw6e6yiTIoVQaiMpTe06nFP5k3CcFX7iNwCijVXhCyTnteYDrnbRTb0WEXyDk3kv5RlKT-tHm-UHuFT4aS2NgnIeqZUMHGJ1VonhaxehI-tH64TgFSwxfP057fvL_ur1JjxW-2HHumfolRK8G76Ll-he2Z91Lc4NqXGrLH9pGC7OyXAJolr7IxkrX6khThUT4f8YyLIQfntRzyJxS6K5uSUvuGU_-uM1KwpEygEyRhgunt7nbOjE-ZDp_rT2dZB9_BvHNca70Lezg93H730C-4pxGoc_oZyvXj3QwedmhngxijLxHcBPrKnBTs1OCbgv9E2nUCaL1Llm6zBkAZxggtxoBLI28z6sdOIkdZWqcCzPo6jmwTCqea_jGHxfkiVkJSl405CyG5P9TNo3FX39q_xihLSJAemhC0Z0KUen3jdBFZ1rr0rnY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی فداکاری، معنای واقعی شغل آتش‌نشانی می‌شود؛ نجات دختر ۸ ساله سبزواری از عمق چاه
🚒
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/690668" target="_blank">📅 17:53 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690667">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
رهبر یمن: دشمن سعودی تجاوزات خود علیه یمن را با پشتیبانی آمریکا و نظارت اسرائیل انجام می‌دهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/690667" target="_blank">📅 17:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690666">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJAhamEJ37QQRiYgWATgcmeBh0uOspKMndORr_zfHDWX_UprnkXp1aN9ugorZZSqYAac3KzLyCuFL7UW90zQMWc-QYtfwgt9IHM8JQE-peO6We37aANeIhhsFlY-pTA9csVlgJROmI-k6dT9ad3uWQHtnN2WyzbBI2Ja9GhTtMQYBVDqqskmt6CQvgGxptcWFZuFRYXI4eJNR2jGy_B6Xp-f5tOwlXz11O6b5lSjNeT3bdmk0cL9lLzrgTNuAJRYZJfEVhYszv5gFDI6uZIu3QQIpTCve7ssI1nQsC6hitYCVNKv6NRcbEO6vxWeB5zCDykBim_jw3COoEV11OBaFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میانبرهای کاربردی word که باعث میشه سرعتت بالا بره
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/690666" target="_blank">📅 17:36 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690665">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17fd05d5a7.mp4?token=QrfGIa71r-i70lsrXuR4FZyQ9eB7uPM750KpalOlogd7JF9k7AYGRtkyhCJpt_p1Tc6oWiehNMahIx-GOBmheusy6jfRgOZ5AaBWMA0-8c8a_sdtnE6Jkfq7Cfq7KcgvxGWaElkB6xJUz-cOk8ld97Wsv_uj7HsFleYx_8fJd18LZR1V7b7wyIzHmkXIO42oc_Fr1UwmNiGiDidyZkFizLE9v5VhiVYu0clTu84r--aju7At0mQa8oo8U1sd8Qs63KF8gna9uI6QdEZAkC3T0qipQuzxJuef28vw0XS7PfYNJuUlChLPihyNz3hhe92wg-11X1hLcMCWPIZnXnLIFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17fd05d5a7.mp4?token=QrfGIa71r-i70lsrXuR4FZyQ9eB7uPM750KpalOlogd7JF9k7AYGRtkyhCJpt_p1Tc6oWiehNMahIx-GOBmheusy6jfRgOZ5AaBWMA0-8c8a_sdtnE6Jkfq7Cfq7KcgvxGWaElkB6xJUz-cOk8ld97Wsv_uj7HsFleYx_8fJd18LZR1V7b7wyIzHmkXIO42oc_Fr1UwmNiGiDidyZkFizLE9v5VhiVYu0clTu84r--aju7At0mQa8oo8U1sd8Qs63KF8gna9uI6QdEZAkC3T0qipQuzxJuef28vw0XS7PfYNJuUlChLPihyNz3hhe92wg-11X1hLcMCWPIZnXnLIFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رهبر نوربخش دوبلور ۴۴ ساله بر اثر سانحه رانندگی از دنیا رفت
🔹
او به جای شخصیت‌های انیمیشنی زیادی صحبت کرده بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/690665" target="_blank">📅 17:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690664">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
آمار مشارکت هر استان به نسبت جمعیت در پویش جان فدا
🔹
زارع؛ سخنگوی ستاد مردمی جان فدا: استان‌های تهران، خراسان رضوی، خوزستان، فارس، آذربایجان بیشترین ثبت‌نام را در جان فدا داشتند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/690664" target="_blank">📅 17:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690662">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a596aec23e.mp4?token=ZyNXLXeAi4fJhvoDmWfoBwKITFb79Yb6j6f_giM2y2vhigWZffaou4vTPn-beqOCsIjM-yRMzh_NjGeGo7ucChi-LbgloYLwAv34SEF8PP93zg1nWS--oonfHQzl8CHMSbKXQAAIlRU5N5cs4IfKf5HTDR778QYTEbwQl8zfnlovqXgJ0Mj0ucFCTVncJmB2Zgam1vZS_vpsCegj2Y9n873L4hu_6KWHaDR6OP19UFQWoIuXL6UdfIhrv9RKDzblfKpyBduHms03Aj-E6myk1CWTFf25Hp9Ui8-4MOqgcR6C5nS69mle-cQeO2pttdrwzXJNdUhPN7OrC1f9JSHSyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a596aec23e.mp4?token=ZyNXLXeAi4fJhvoDmWfoBwKITFb79Yb6j6f_giM2y2vhigWZffaou4vTPn-beqOCsIjM-yRMzh_NjGeGo7ucChi-LbgloYLwAv34SEF8PP93zg1nWS--oonfHQzl8CHMSbKXQAAIlRU5N5cs4IfKf5HTDR778QYTEbwQl8zfnlovqXgJ0Mj0ucFCTVncJmB2Zgam1vZS_vpsCegj2Y9n873L4hu_6KWHaDR6OP19UFQWoIuXL6UdfIhrv9RKDzblfKpyBduHms03Aj-E6myk1CWTFf25Hp9Ui8-4MOqgcR6C5nS69mle-cQeO2pttdrwzXJNdUhPN7OrC1f9JSHSyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای نشان می‌دهد انصارالله یمن در حال حفر خندق (حفره) در اطراف تنگه باب‌المندب است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/690662" target="_blank">📅 17:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690661">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
متکی، نمایندهٔ مجلس: در این مقطع نباید از مذاکره صحبت کنیم و نباید پیامی به آمریکا بدهیم و پیامی هم از آن‌ها دریافت کنیم
🔹
دیپلماسی همیشه به معنای مذاکره نیست و گاهی دیپلماسی یعنی مذاکره نکردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/690661" target="_blank">📅 17:19 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690660">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBPlFBCHAoBxC-fVWXdNuRnmfPWwi-H-hk6_Tzmj8_Lf89BZPCkxTMcN6fXyJVnIFnda7DQa8ngrgCr42FuYHyrvd3oCLhKseLvilZ-hsarxJJYa10jOcGPknI1Bbkeudm1C8oomk3F1ZZkVo1yVhZuVltEL7T7RRMvYYTrtdq80NsxtiUR6bxObHK08tcW7cTyDvK4g5__RC7vvpk_J6fdWL1gLZGqsf_MH2UT07RDK9yyrmOqgnzxSG7ttMPXZVFnGL22EOXrkJV2t0IljlKHxa_G0G4211_f_ziOdxvX0Mqw0BOxZzYaYv_yemPKEaS5dy_qnuF54Xv_Eb-Ufow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وال‌استریت‌ژورنال: آمریکا برای مقابله با ۲۰ موشک ایران، بیش از ۷۰ رهگیر شلیک کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/690660" target="_blank">📅 17:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690658">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
قطعه‌سازان دست به دامن دولت شدند؛خودروسازان بدهی خود را پرداخت نمی‌کنند!
محمدرضا نجفی‌منش، رئیس انجمن قطعه‌سازان خودرو در
#گفتگو
با خبرفوری:
🔹
برای وصول مطالبات خود از خودروسازان دست به دامن دولت و بانک‌ها شده‌ایم، چرا که از دست خودمان کاری برنمی‌آید.
🔹
قیمت‌گذاری دستوری باعث کمبود نقدینگی شده و راه اصولی این است که دولت دست از قیمت‌گذاری دستوری بردارد تا خودروسازان نقدینگی لازم برای پرداخت بدهی به قطعه‌سازان را داشته باشند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/690658" target="_blank">📅 17:10 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690656">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
ادعای نیویورک‌تایمز به نقل از مقامات آمریکایی: چین می‌تواند از طریق جاسوسی در عربستان یا همکاری‌های امنیتی و اطلاعاتی با این کشور، به فناوری جت‌های اف-۳۵ آمریکایی دست پیدا کند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/690656" target="_blank">📅 17:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690655">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
بلومبرگ: محاصره دریایی آمریکا علیه ایران بیش از ۷.۱ میلیار دلار برای واشنگتن هزینه داشته است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/690655" target="_blank">📅 17:05 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690654">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/223070706a.mp4?token=IJYSUkxZLZm6X2awbZGDc8vQvRPKcK1tiVQugJl5ogXsLHDGpxwhSCfkkjP0Mgp4wH6-fEwHuQacfKLUo7x8wos0zhGC0tVpKQrDO8abMOd4IjKMDekMI9knsbkrr9VUthvLGHwsDqM_GBWY0x-hDErJRhGyI7UUBYt0J9geeBx6tfJjPJNABuCHlxC1m1MNFsXPO-vnG-rgLXXoeSfrFyp6oKWIWZV8RyR22PadhZcNRQ5jCBUUFk5ZiI0NiwMEY2998a9vQVDAwuNVSqNb5MdUYerhbklaNvBZEjb_oYp-glcb18GE9xAPNytcvuZgHpT062tpZbaISGztnLSFIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/223070706a.mp4?token=IJYSUkxZLZm6X2awbZGDc8vQvRPKcK1tiVQugJl5ogXsLHDGpxwhSCfkkjP0Mgp4wH6-fEwHuQacfKLUo7x8wos0zhGC0tVpKQrDO8abMOd4IjKMDekMI9knsbkrr9VUthvLGHwsDqM_GBWY0x-hDErJRhGyI7UUBYt0J9geeBx6tfJjPJNABuCHlxC1m1MNFsXPO-vnG-rgLXXoeSfrFyp6oKWIWZV8RyR22PadhZcNRQ5jCBUUFk5ZiI0NiwMEY2998a9vQVDAwuNVSqNb5MdUYerhbklaNvBZEjb_oYp-glcb18GE9xAPNytcvuZgHpT062tpZbaISGztnLSFIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بعد از مصرف امگا ۳ چه اتفاقی در بدن می‌افتد؟
👀
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/690654" target="_blank">📅 17:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690653">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">خبرفوری
pinned «
‼️
خبرفوری/ رهگیری و انهدام پنجاه و سومین پهپاد MQ-۹ ارتش تروریستی امریکا
🔹
پنجاه و سومین پهپاد MQ-۹ ارتش تروریستی امریکا به وسیلهء آتش سامانه نوین پدافند پیشرفته هوافضای سپاه و تحت کنترل شبکه یکپارچه پدافند هوایی کشور ساعت ۱۰.۱۲ صبح امروز در آسمان  جزیره قشم…
»</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/690653" target="_blank">📅 16:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690652">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQyDvw3Y-8lLtGkXdoiWgJMjLKZbYU5JeCdzldssK0Zn71uTk0ppJU9trpm3zHM1v3W38IQYJJs3s8qLITZdQsVH3SBMzEYSXIm4v3GpqG7cyu7ezb4xOXenAC7eAX1lPcrPQpt12qy_ena0J9jkEGu-HlUeBV1wE5t5-D82c1irJnAZbauDh_8Z_6B2VbQEx1TEOvv2yUJnRiX38FwWiFpKEmuK27rAZFlzKsKm5AOmUiGAujpnPJc6LJXIHP_HY6rQYJ6ECjVouX6jBICEIFy_wRfNJ3xTuAr5CNT0YVVMmepYaeRC5feuz89WHATOovzXDgio-q1gNy3ZiOxEtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زلنسکی در آمریکا محبوب‌تر از ترامپ است
شبکه CNN:
🔹
رئیس‌جمهور اوکراین این روزها در نظرسنجی‌ها ۳۱ درصد محبوب‌تر از ترامپ است. برآیند نظرات مثبت و منفی در رابطه با ترامپ ۱۸- است؛ درحالی که این آمار برای زلنسکی ۱۳+ است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/690652" target="_blank">📅 16:50 · 26 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
