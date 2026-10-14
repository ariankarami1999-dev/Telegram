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
<img src="https://cdn4.telesco.pe/file/S9xYJItOGVSgrARaqBGLz7W6s81Ki0sBw22li7E1yzrInTUSypoPBa-sOzBrSJjdMxVb3YJtIvBjF40kLeBl-ut3oxXt4Qoz7uZVqnvQjRTG7j_IgxcnbxmOZUGVhBvQTXdcje8-Z5IXo8qN-3VCKQNEkJg9WYUaRECBUb7AeZfeN1r_zkmSKoO73xuP1Xy5DtYGal19E6al4f2pwehyw7qocKqNwk-V3qJkqQpkuHe3vyYvs_R8ESrxigpbySp8kfa3gdIfMKuQXmHeVAKLPULRoCkZ7REuiLNW-mx013Uo41ionVX7VbVVr4AoLn34KT8q6IgjKGTBNdeoNDRoRQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-22 05:31:08</div>
<hr>

<div class="tg-post" id="msg-468319">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">گفت‌وگوی ملی فلسطین در قاهره برگزار می‌شود
🔹
الجزیره به نقل از منابع فلسطینی گزارش داد که گفت‌وگوی ملی فلسطین با مشارکت گروه‌های فتح، حماس، جهاد اسلامی و جبههٔ مردمی برای آزادی فلسطین آغاز خواهد شد.
🔹
جلسات قاهره تا پنجشنبه ادامه خواهد داشت و درمورد پایان‌دادن به تفرقه و بازگرداندن وحدت فلسطین بحث خواهد شد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/farsna/468319" target="_blank">📅 04:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468318">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUfTRe6LOaie8KTZGNawXDyDXB5Kx5HUNCIC4FKEE-tVkCeNMQFXNyC668nsD141ujE-6jh1jNwU6hpCngnxN2xKemoYYv08MqanrXniYSTfm_MdNwhsvtHZVamDH8JSoCmnDshuUjU9LPX3-YzjP-M1xX4YV-KCVsKOczCGw4aJMLGcWs0ZBvKiWRg64MQOACyzsacSlAsa7TACH61sHn3DLR4v18HUDOenUoNz_z1264XsozZNQsOAxcg11u7SIHbOa2WAyNZgTvrdNZJbC0twF7Jg7UzucWokjOjDJXDkS_eJ8-uBT9PlvYwXFdgC11E5xf0WlJYb1ALzYcWeVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتراف فرماندهٔ پیشین سنتکام به قدرت پهپادی ایران
🔹
دیوید پترائوس رئیس پیشین سازمان سیا که فرماندهی سنتکام را نیز در کارنامه دارد، گفت: اوکراین روزانه از ۱۰ هزار پهپاد استفاده می‌کند. فکر نمی‌کنم ایرانی‌ها این تعداد پهپاد استفاده کرده باشند؛ با این‌حال همین میزان استفاده از پهپادهای ایرانی نیز به‌اندازهٔ کافی مشکل‌ساز بوده است.
🔹
او پیشتر نیز گفته بود که پایگاه‌های آمریکا در منطقه در پی حملات تلافی‌جویانهٔ موشکی-پهپادی ایران، بی‌استفاده شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/farsna/468318" target="_blank">📅 03:48 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468317">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZ2pwBtx3YGVsj22u_qmTgPJ3GSZqQxL_V602CaPlHtdGpw6T8y9h0C5bfxNpY4XTVCSfmNNLjjRhfVu0uqs3wn1dXAKLEiRk-wSdswfpRSnaBqX6ohtbP1seDiBC7fvHkVAuJNNcEwtDjDrQs35opfUmokpERvVe4JazX-TmXOUuFIaiofRft7aM1jVPteMr-XVwU5_IFQVyWeNSA4Qestrqx5Nw5Wa9uCdwF3U4xWNmJ6v9rlMi0eLfhJ2HZ81fcuwZuAP49nK-Toz22prbwvutJmpfKwzcUtJGecgD3pVOSPhhV52089N3sHDwZx4qBjP9KARNe2sk20rhWTX0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واتیکان: پاپ به سرطان ریه مبتلا است
🔹
واتیکان اعلام کرد که بعد از عمل جراحی برای برداشتن لوب تحتانی ریه راست، مشخص شد که پاپ «لئو چهاردهم» به سرطان ریه مبتلا است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/farsna/468317" target="_blank">📅 03:18 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468316">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a09b75e4b.mp4?token=PJslcqEQLGsSRpLtve7DuFDC5KRqXBGm1euHtBFsIr4k4gidc0k994xQPyUNX1Y0mw_ETa0_xCz6TSvJsFexE3H-DrNxcBekta54zT5yi-2MQD4l0TBrVoya3sGbHAN6l4c2QRT0zfbTwXjI-UWl0vCCKvdTmEiRDJHNIQlLA8_t8hNn-eb9wH5bhir2tUdI0Vf0JrBFlYl1o9FCPvDCnHlx3iwU3uNit-Nc-_yj385D0SSItat1IyAVuYoJAA4AcasoSyTa7dRtcUxOJ5xy3JLoBf9fG6ZRJRk3J5onfXDhdC8y0Owm-0n0ifpnE-ieeJFzwfde3azhmy6RvjmQGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a09b75e4b.mp4?token=PJslcqEQLGsSRpLtve7DuFDC5KRqXBGm1euHtBFsIr4k4gidc0k994xQPyUNX1Y0mw_ETa0_xCz6TSvJsFexE3H-DrNxcBekta54zT5yi-2MQD4l0TBrVoya3sGbHAN6l4c2QRT0zfbTwXjI-UWl0vCCKvdTmEiRDJHNIQlLA8_t8hNn-eb9wH5bhir2tUdI0Vf0JrBFlYl1o9FCPvDCnHlx3iwU3uNit-Nc-_yj385D0SSItat1IyAVuYoJAA4AcasoSyTa7dRtcUxOJ5xy3JLoBf9fG6ZRJRk3J5onfXDhdC8y0Owm-0n0ifpnE-ieeJFzwfde3azhmy6RvjmQGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غیبت‌کردن، آبروبردن و اذیت‌کردن دیگران روحت را کدر می‌کند
🎙
آیت‌الله علوی بروجردی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/farsna/468316" target="_blank">📅 02:59 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468314">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bP4LwaMXK752EYVh4qlum5xymqthPcESboF1Tx84KPJUx7DXnmfunPYJ0HWP9y2mR7txNYpIPfUAj62BVQRr1dNOqSYNF0aYS9TOTOv2zKrroBUduVdtS6zjhnt-5oLxhB1Q8QgxOjRsG5qhk-jhkV2_67adV-KSXMXgX_hH8neQV_foRSJTpy5FEcNBAMHQLL59BSNunvMr7B2VnVWd7uTzeGpMwjSQbl8ZNP-71n4mJUh5q3h6CJcrQmbJpraZbVBc5LudbfCb3u_Kz6n6MQIOlJZ47C28XXxmAPa2rS8BIvGwKbTwB5Awo6r3xerqd8pF5N85sW3rHY_mMSqMMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکسی‌های اینترنتی حق دریافت عوارض شهری از مسافران را ندارند
🔹
با تصویب لایحهٔ دریافت عوارض شهری از شرکت‌های تاکسی اینترنتی، رئیس کمیسیون حمل‌ونقل شورای شهر تهران اعلام کرد شهرداری مجاز است به‌ازای هر سفر انجام‌شده یک درصد مجموع هزینهٔ سفر را دریافت کند.
🔹
براساس مصوبه، پرداخت این عوارض برعهدهٔ شرکت‌ها است و دریافت این هزینه از مسافران مجاز نخواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/farsna/468314" target="_blank">📅 02:36 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468310">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ots7hXgBNIp9hr6mwoayGWWoxmuNrDZ0Ef3Adv84cltAWEsEO8-Bp8SvA3YMfZ-TDhxjQofRu2rZX9mRE9maby3NQthPa4AMabQefR3PRFtL5UDdlf-mFM-RgoBemwi-dZAMbzDssyWxIdZhLW9C_37CpRez3hVgv_vP7UeO4YMWVQz8hHKiuGSis4Jda0I10gMN47LZgcXCYyZruJJP63wXwRsZ56-lN8MOvRxO0r19yoND5WaVJMVgGpBOTHfmGMDu38JkNgf0lY70v24p6Zv3hYBsB-0wEgX3XsuNBGYt5cUqttium480HM-6Uk5zqU1ptyl9oEtsyOcY4bl9gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qW04Fr8_PvnYMRNItPF-2RPhhSdyUMXN79DeDkb73iLt7B8P-4lN0KmbJsRYHb92rZe9FjtRb30oTV3keLoyPUB_jdLZg2uFf5IOcdIvbZaRtVSKUITwtNxS1B2lc2TRg8wLTcLUU0kWmQe4EKLV0hAwKT2LEcBM1qt0JNub7uGvIgjdqhI5ak1nwp_jOmQrJwQxq1zMaEkAnfjD5RIk44y0JM3cvDS5bvqTZwYtCSFOcH1QwJh1M83KGxn-AuzxDL6SB01TsfN1sY80rOpoO_Wfs87fKbU3WZFvVO-XyvymD4S083NS4ip8BtUnb_HtcShvynq9Wm1hzKxJ-DsDZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZsMXiqB8Oaibjgosm7Aw-pZ569tXURsIdYT0dg76R1QFmN-YlaH4pW5kbHuPFfR_b3K8MrrZhYIaUN5ORnUUXAK5v0onnsHd5UxhG1sDwpcuZtq8WfS7lVF3nsDidCf_esYeDW8uTmYAvcDEmSJUkX3nx-v8sVtPxlamqbilfCOZx1SkKjfYmC83hCOP2m8FaFbYOTX05Sx-mYi36pkmW9jUpo-cgV0OEOLAYXCFQHhVJ39m9nuauKz5StNrctqevRKYUHSj4wA62LoeqwV1WqevwFNzpMQVFvzRtgUwid0h3D-9NfZRh1Iampa3asIKPdnn0dHvNrJgYWce-VAi-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VoDohURKNhImowseUweLLy4CMXQHZxWyUkRN5EAw0t8BV60D06CPm3kcMsguD3xS_iO4UY-ID_LM3w22GdHLdJuLQA44-erVL0SlmO-gSJDSuUnyaZHS8yvuWp9Q5rHG8YtArGqXrK20gRdVeXNSifcwbsGTbT4IR1uu2_KdjVMHlvrT7EapQ9Wfd3fhMVq5xqfh-i1WqUYwLLWWo8ZH10cX-hgFxgJ_eeDr5crItcX8DzQq-5dZ7l6GWIL0XV-gdo3cudQ0hIq25_Pr7l63SO0cNRwEESrox1-q4WcgbSfN6-neRIgLbWJLFrn4tP6JVtO9C3Mjz0TRtpKY1KMqaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انهدام باند ۴ نفرهٔ سارقان سابقه‌دار منزل در تهران
🔹
اعضای این باند با استفاده از خودرو‌های پلاک جعلی در مناطق مختلف تهران اقدام به سرقت می‌کردند.
عکس: فاطمه جاوید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/farsna/468310" target="_blank">📅 02:04 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468309">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‌
🎥
وزارت انرژی عربستان: یک ساختمان اداری متعلق به شرکت آرامکو در شهر ظهران هدف حمله قرار گرفت. @Farsna</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/farsna/468309" target="_blank">📅 01:45 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468308">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7bv3EaJS11a6j8_oTMUP3tm-Qyx4NvEeyEoTngh4LDb_nHC4iAorWESZfac7BjJF8i3BkFut7eeYYRE4SjqviP4tx2tJyC_OSQ8hDenhjX864exok2ay5mDjEF_b8VD2t0zBkIijMQPky-4BQpKMxrmyLJIkTWcw_0eSuJxhytFOUEw7hYUuf3fUDuJEX0mQuoB7dHsTxTjR9qBFbzVqwOHT8xhx1vBRRiKjbJf4bzOnnFcQqgve_IFqYm9Rt8YgqJwPHI8KoOhBi8Km3PbdCoqhcggLf4Gl_ROWQEOUT9KosXJHR67W52A4CVlX0PHpimHqhyck4z9V0hVRfbXrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فایننشال تایمز: فقط در یک‌روز ۶ کشتی متخلف در تنگهٔ هرمز مورد حمله قرار گرفتند
🔹
نشریهٔ انگلیسی فایننشال تایمز نوشت: برخورد با کشتی‌های متخلف در تنگهٔ هرمز به بالاترین شدت خود رسیده است.
🔹
به‌حدی که تنها در روز یکشنبه ۶ کشتی مورد حمله قرار گرفته است؛ درحالی‌که در دوهفتهٔ منتهی به ۱۱ اکتبر، ۲۴ کشتی مورد اصابت قرار گرفتند.
🔹
همچنین به گفتهٔ کپلر، محموله‌های نفتی از طریق هرمز در ۱۱ اکتبر به ۲.۹ میلیون بشکه کاهش یافت که کمترین حجم روزانه در این ماه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/farsna/468308" target="_blank">📅 01:29 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468307">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUQoQcqQvUrxxEkyfH0guxh3y00IlT2eHjYeyf1_8vmM3EEc5TFUGT6Z7QdTHlDZIVx9nK62ORNjiiXIZ5aKC6ManwW7iVXmpVlABb2GnChm5E2JPJZ9P9S1vwvyYJu5Yg731PEkFDgHWA2athUUOtI7pagQujU3jjNuIvmXa-oLDSo1tC4Kz24SbQQX8cC5JQHD2PbiBYHFuk3hgDfnOJNdU2-Pt3oGIljW8I0BYrG6Wsj5hH39FuCJAFBDhZS2UtZpIWCoU-XHZ9jlCMGJUSX-zUamYOh41JBOI0h1Xen4h7R5onmqayfPsdRPJ0rVorekv5-F7XScb_6cSbp7wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تداوم حملات رژیم صهیونیستی به جنوب لبنان
🔹
براساس آمار منتشر شده، رژیم صهیونیستی طی ۱۱ روز نخست اکتبر، ۲۶۲ مورد حمله به لبنان انجام داده است.
🔹
این حملات، با تعرضات تازه به شماری از شهرک‌های جنوب این کشور در ۱۲ اکتبر نیز ادامه یافت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/farsna/468307" target="_blank">📅 01:13 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468306">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08fe5dcc83.mp4?token=Zk8LrYxWvkGKD_ErJ_XXAy4oT_RJwN-PkzFVJiqjj0umJr6Bkj_PPf-5gWuXKLYze7E4-wit-Hfg4GFidunV7zPlGsfd0ClpBPJeX5-gHws7f7yBZGR6yaHIxOhLdgPkDLzjPzkk34tLxSEni6NWvwpUzt4bhBGFtWSv1IAztR71lZ9cDcwFyXDTRTAufdR5JA2QlIYnumq_S7SUkGS4BLGpYms-fFqs4M0_Foo7HxHR2dzRG8z3rzvaPSKIq3XOZRzS-1ulPXpBvZVWA4IX9h1qK_2keKpDlRlJO0gJVVjkeqI5G-zg66Vn7FX5MlT9EOkE7Zvmg2FvdR0MwtImtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08fe5dcc83.mp4?token=Zk8LrYxWvkGKD_ErJ_XXAy4oT_RJwN-PkzFVJiqjj0umJr6Bkj_PPf-5gWuXKLYze7E4-wit-Hfg4GFidunV7zPlGsfd0ClpBPJeX5-gHws7f7yBZGR6yaHIxOhLdgPkDLzjPzkk34tLxSEni6NWvwpUzt4bhBGFtWSv1IAztR71lZ9cDcwFyXDTRTAufdR5JA2QlIYnumq_S7SUkGS4BLGpYms-fFqs4M0_Foo7HxHR2dzRG8z3rzvaPSKIq3XOZRzS-1ulPXpBvZVWA4IX9h1qK_2keKpDlRlJO0gJVVjkeqI5G-zg66Vn7FX5MlT9EOkE7Zvmg2FvdR0MwtImtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌  رویترز: ساختمان مرکزی آرامکو در الظهران مورد اصابت قرار گرفته است
🔹
خبرگزاری رویترز به نقل از یک منبع آگاه: ساختمان مرکزی شرکت نفتی سعودی آرامکو در شهر ظهران، امشب مورد اصابت قرار گرفته است.
🔹
هنوز مشخص نیست این ساختمان مستقیماً مورد اصابت قرار گرفته است…</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/farsna/468306" target="_blank">📅 01:08 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468305">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/farsna/468305" target="_blank">📅 01:01 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468303">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEGMFE9ZCtv51fN1897g_1sqJ_NKKr9FQiffSySkUUc4HY--CDmisWgUzgfqvjyUkIzSAVJ4FtBwpCvT0Yfr2zzERmw_j7PNrU-0CJ7Vqcu6LGYwfMeoBcZ71KUjjR11OvxdndgwwpRRffarXXDek1tRd2nuQlyVMeWUj3vRSi9hXd98J9UFVwf3q4v8_-Zru4cCyYSqFz2_EDUPzgZKfl9ZoufCG7QWZP5WnRlGjQNfzpCMAQa5Y0AqIuPLgXZUNpBEriW-IzAIgmCo4Pwayh_CwgE7bsI01ueftYVNvV5Z2N03QplVz6FV9BocSCWHaHKS0LIfnJ3sYB5BlKDhHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سامانۀ درخواست افزایش اعتبار كالابرگ همچنان در دسترس نیست.  @Farsna</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/farsna/468303" target="_blank">📅 00:41 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468302">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3bc0b915.mp4?token=ITL5Q0lY91uCxBiMtW6R3MhAdm-Hq2ZeVXtYPz1JZQFq7f7dTyXlwN5CYItOs_iM_ZJbAddjgRJwpVYKxqEbjccWOwhvidEpKcrF7cGwS3eC_Y-qswX3bIIuAY5Utsyv48_Q_-d3XqRf34TQwju2m4EX5qF6U4ZZjij5mTeuq_GJTjTPJYKAlTotvTNuhWa3LuCqz2pjlLjmz0lIX67885UIvs2hyUZKunGOv2IX_-BfzWmk2TgOh1Y3_vKH8y73fyusak6XEu7z3walnRUt6wb-xI3ZCpIRAw72jjb75R_QDBkCpXNMwvRVYf8CFCnm8-ttTmJ6kvxVkZLdF8vwR7IPoavRgRYMg51enurmbqGJEopg_GxhgNxewFXLa8b8EgaKRbqpMyK1Bz8X28AbDN9Hb7eZKZUH97TVz7Ouq7t_DDLvUsBzyMsPXvw7rO7UoZF9Vi22QZ5vWFEMDC1VVyS4vGebo8XDsqpxOcqTiPL_ZjDz77BtrrsQS4ScbmVFCv-SZveBCuBJkplnRCpLYmokQF2tlyfUUKAMYXi_etkdaMPd7Zj_YX7gn_4OumG6EAb0SCHRp0_37T7r5zs3TCU6UUZxe--n2sEHsnkIWK5IuJc-jvDh9m6s6Kvn0Xb0Vg_WVZuFS44Q87BSWKv_dR21dHhgLgF-aI_24mr-r5Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3bc0b915.mp4?token=ITL5Q0lY91uCxBiMtW6R3MhAdm-Hq2ZeVXtYPz1JZQFq7f7dTyXlwN5CYItOs_iM_ZJbAddjgRJwpVYKxqEbjccWOwhvidEpKcrF7cGwS3eC_Y-qswX3bIIuAY5Utsyv48_Q_-d3XqRf34TQwju2m4EX5qF6U4ZZjij5mTeuq_GJTjTPJYKAlTotvTNuhWa3LuCqz2pjlLjmz0lIX67885UIvs2hyUZKunGOv2IX_-BfzWmk2TgOh1Y3_vKH8y73fyusak6XEu7z3walnRUt6wb-xI3ZCpIRAw72jjb75R_QDBkCpXNMwvRVYf8CFCnm8-ttTmJ6kvxVkZLdF8vwR7IPoavRgRYMg51enurmbqGJEopg_GxhgNxewFXLa8b8EgaKRbqpMyK1Bz8X28AbDN9Hb7eZKZUH97TVz7Ouq7t_DDLvUsBzyMsPXvw7rO7UoZF9Vi22QZ5vWFEMDC1VVyS4vGebo8XDsqpxOcqTiPL_ZjDz77BtrrsQS4ScbmVFCv-SZveBCuBJkplnRCpLYmokQF2tlyfUUKAMYXi_etkdaMPd7Zj_YX7gn_4OumG6EAb0SCHRp0_37T7r5zs3TCU6UUZxe--n2sEHsnkIWK5IuJc-jvDh9m6s6Kvn0Xb0Vg_WVZuFS44Q87BSWKv_dR21dHhgLgF-aI_24mr-r5Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چراغ میدان شهرداری رشت امشب هم با ایستادگی مردم روشن بود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/farsna/468302" target="_blank">📅 00:34 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468301">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">دیوار چین</div>
  <div class="tg-doc-extra">قسمت ۲</div>
</div>
<a href="https://t.me/farsna/468301" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قسمت ۱ – دیوار چین</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/farsna/468301" target="_blank">📅 00:31 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468300">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H7cVymnkUnDbj0sD1Z_g_N8KviBGOBWZJyA_i8Q-JZA_DvMrosVvix5agFuwpPf8cWw172-ljRQIa9iy7HXFx5bSdTC4yupQt9Y5pvwLFXT95imZ3NaheL6dfGSoi7NtQVEIpw9fTV7fD7Puiy2nh1kJ1DiVkqdYfUYCixpiEEhanKs7ddtz1Zl--e-9tKA8KEqAC3vphyHl6EYl-Q3h-QqQq1vc_WFKIsCBA2dCRL7a5UI7YwgdPMa7f6qsXirz4gn9S0fMLoM8NfyGnjUGWSYV-FkADGBeERimVVeT51sU2sYrUElObk_PmtLq0MmBwIPQ5VxSAXeiW6b3gjeYvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زخم مال و نمک طعنه
🔹
بازرگانی در دادوستد هزار دینار زیان دید و سرمایه‌اش از دست رفت. رو به پسرش کرد و با تأکید گفت: «مبادا این راز را پیش کسی بازگو کنی یا بگذاری آشنا و غریبه از این باخت باخبر شوند.»
🔹
پسر گفت: «پدر جان، فرمانت را بر چشم می‌گذارم و لب فرو می‌بندم؛ اما می‌خواهم بدانم پنهان‌کردنِ این ماجرا چه فایده‌ای دارد و مصلحت در چیست؟»
🔹
بازرگان گفت: «برای اینکه اندوهمان ۲ برابر نشود؛ یکی ازدست‌رفتن سرمایه و مال، و دیگری طعنه و سرکوفت همسایگان و بدخواهان.»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farsna/468300" target="_blank">📅 00:11 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468299">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‌ منابع عربی از حملۀ موشکی یمن به ریاض پایتخت عربستان سعودی خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/farsna/468299" target="_blank">📅 00:09 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468298">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/renvYPPKWdz-S6vxMLNNaepEvgEVXjVO4kENvHOTXtMXMGP99sJy7hCREFMgHVI_5Ki1yhqLUhC5vXBCnPfz8n81dpZ5YXTEgu-JA5xdVCbwSusFVV_niIkZ8auvflugfcsFtAquFfq_1O-oNP3lljvnhbg8EsKF-yeVFpYU1LueWCH-ItFVcQKpV5d4lKJmzqJCKa3fHVWr2SX2GK9mOLA0tPp37vy7yszzfVZiZ4l8F2HaKWgawg1BWSd8m8Zi8tznjEtliayNl7EsN3oyBnR1fLwUhjUBuNQ1Mrwow3PNmJKplhJ_ODYmJ0BJTNyAKGx_pbr_Ocs-W3nJT03D8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس را بدون اختلال دنبال کنید
🔸
به‌دلیل محدودیت‌های ناشی از تحریم‌های آمریکا و عدم ارائهٔ برخی خدمات زیرساختی به خبرگزاری فارس، دسترسی به وب‌سایت فارس برای برخی کاربران با اختلال مواجه شده است.
🔸
برای دسترسی پایدار به اخبار فارس، آخرین نسخهٔ اپلیکیشن فارس را
به‌صورت مستقیم
یا از
کافه‌بازار
و
مایکت
دانلود کنید.
@Farsna</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/farsna/468298" target="_blank">📅 00:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468297">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmwi8eLhM7uIEahCh9IB8b3Phg6m-vl8wRCaRfreaK_e5aIrCSwMnS9fuegFlX6oxMKEGnAdHPFD5YvkV16Imns9C-BJp6NOYQ8Ea76SvPqS3ZDmLOYED1HdA2hXSG8DrValFgZPSm2CA0Q3OFtClhV4nZ3BjcKhy3z6JJLcOAUbfjJbByYkP_vFf1I9ZS-VGNEnLCkmNCdOLmijvRm1WQRvNfX6JOIFTBsyCCGqSeVHwLy_GaL3kR-dyDDxczPLv7vXHZQHZ64nSD7bbvULfcOrhbNIm4qI7U7c0sUoHYn-_AuIKTUBIwyYwUxyWXI4xS741pMEhRTmCGdeKDWZow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کره شمالی موشک دوربردش را به رخ ترامپ کشید
🔹
بعد از آنکه دونالد ترامپ اعلام کرد ممکن است با رئیس کره شمالی دیدار کند او موشکی را به نمایش گذاشت که قابلیت رسیدن به خاک آمریکا را دارد.
🔸
رسانه دولتی کره شمالی روز سه‌شنبه گزارش داد که کیم جونگ اون رئیس این کشور، از موزه‌ای در حوزه صنایع دفاعی بازدید کرده است که در آن یک موشک بالستیک قاره‌پیما با قابلیت رسیدن به خاک آمریکا به نمایش گذاشته شده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farsna/468297" target="_blank">📅 23:46 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468296">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23c991654e.mp4?token=LLybbiKal4s-G5u_JL4WjibB7i6EhXH44XVje6t0-FTeoDXvF91QHYfWTK09p1J8umA8VBEXg0ojdqJFNNtmsBFG-PVsARUeTBVFDi0PT90ofgWxRaRRPhq0ZG-SPmuSK-Ry-aXJBOSHABYcddvTr52-f2v9HMc1KHlhU3N9-VZRRbElkq7JkX6cFaxm99EdMNsHKnWFD-xlcQ5HsN3bMw2IVWyqLLlBJK2gD3dHXKinYwrnBzTGql9ryKxdqu9RxJrnCt79bSAdBWqlLuTdSagvc-QN2Zhj-D-PuxZMMjp_gjFMCWsu1XK_eRrzzd9_tedVIuFhx3jm7dBXIlAhfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23c991654e.mp4?token=LLybbiKal4s-G5u_JL4WjibB7i6EhXH44XVje6t0-FTeoDXvF91QHYfWTK09p1J8umA8VBEXg0ojdqJFNNtmsBFG-PVsARUeTBVFDi0PT90ofgWxRaRRPhq0ZG-SPmuSK-Ry-aXJBOSHABYcddvTr52-f2v9HMc1KHlhU3N9-VZRRbElkq7JkX6cFaxm99EdMNsHKnWFD-xlcQ5HsN3bMw2IVWyqLLlBJK2gD3dHXKinYwrnBzTGql9ryKxdqu9RxJrnCt79bSAdBWqlLuTdSagvc-QN2Zhj-D-PuxZMMjp_gjFMCWsu1XK_eRrzzd9_tedVIuFhx3jm7dBXIlAhfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اولین باران پاییزی شیراز را آب‌وجارو کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/468296" target="_blank">📅 23:36 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468295">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd7781b10e.mp4?token=FFauvFWO8Z9DGLUz-OqfL9OFbRzh-GoKoo-tbJGnjSp-KFBwItXHEv_QXdsGQ34zRYFT7pHKcAUUbTBOJqmjL0fGAW3tq1-gQEr3DDHb2_CcBnukeU49BPuVdh-LaFwxpaF5x0K19BqcY33RKy1cifKt7Q92AFAfrh5VjYl9QBbWtinSAd2FbOYCGAQAWGQnUscSfb9vw1aAPQoZcJ7OcaA0LI660AVbVQVXLA2LaI9RX_RSBGMGa7kKEWSor3gHoosAV-0LrIIaULaW9JraNb_G4SAyu-Xf4IWCZ-LdX5TKMDsuuN_MMKrSptVD4-uECL9swHr3xtCmJjTYVvenyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd7781b10e.mp4?token=FFauvFWO8Z9DGLUz-OqfL9OFbRzh-GoKoo-tbJGnjSp-KFBwItXHEv_QXdsGQ34zRYFT7pHKcAUUbTBOJqmjL0fGAW3tq1-gQEr3DDHb2_CcBnukeU49BPuVdh-LaFwxpaF5x0K19BqcY33RKy1cifKt7Q92AFAfrh5VjYl9QBbWtinSAd2FbOYCGAQAWGQnUscSfb9vw1aAPQoZcJ7OcaA0LI660AVbVQVXLA2LaI9RX_RSBGMGa7kKEWSor3gHoosAV-0LrIIaULaW9JraNb_G4SAyu-Xf4IWCZ-LdX5TKMDsuuN_MMKrSptVD4-uECL9swHr3xtCmJjTYVvenyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
حضور نیروهای ویژۀ نیروی زمینی سپاه در رزمایش  ضدتروریستی اوراسیا ۲۰۲۶ بلاروس  @Farsna</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/468295" target="_blank">📅 23:22 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468294">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‌  انفجار در نزدیکی مقر آرامکو در شرق عربستان
🔹
خبرگزاری رویترز: صدای انفجار در نزدیکی مقر شرکت آرامکو در منطقۀ الظهران شنیده شده است.
🔸
سازمان دفاع مدنی عربستان ساعتی پیش با اشاره به حملات به الظهران در شرق عربستان، مدعی شد که موشک یمن را رهگیری کرده است.…</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/468294" target="_blank">📅 23:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468292">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UKXyWyO1izBonusN0UpdylBAB6ETEMHEAKsQ7KBjz-oy8dNRhdJ5BJMKMUnmzQetT2YWnAJ4LbRO3ygvKYNU6yGEAvRz6E2_mskAj6GAAIFS2E0BuREB1yqHmVnvF79Bb5JFJ_y48ufiUh6QBN5wLmWBhhkOGIMLVlCp0lRH0U3otUJwcPnrSPMgTTVM0QZ9_HMhggvY9zEE031gYGZSBR6SxlL0GRTyg7mkA3Y_rrZf0xOVRpXrzrJWRXIaASwXYdMafxMY2Ggio6epiTWh_aQ39DUIu1lHZ4vXTuxCMGeIANQw0xkKCIoutvKOHvZ0AfjOyOYYtKpNYno_3UNdrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gcgnGdoOnOeq66tp0ZYtivte8sn8a-ffrLlS27K9bLDwSSxeBcGUYw8fOJKwEMxJHb7W3EKU4Va19ESW48kyJDnFovDLnaB240IupvC2DIh4gA8Qm75wEQHt0CywcVXeKMdr35Zg0Qk6kmffs8m2qY_xAeAqw4ub05KGjGQFDtLGAawUyVGpALYl6NMUbI_xWp0i4s1xeuMi0p3aEU_s3Fbaf-jyl8d_uBlLycDX1VexreNDTNh469ilf6VlSq3ZQsHFOCuLy-qm-_-8GGUY3QI44vjq_caXI_RzHbBwQ8VhMFPxajBkeOF0df-IHFQyGZ-1Y1HjjUL0OxEPidE7mQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور نیروهای ویژۀ نیروی زمینی سپاه در رزمایش  ضدتروریستی اوراسیا ۲۰۲۶ بلاروس
@Farsna</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/468292" target="_blank">📅 23:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468291">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QyZlPPtWFdMgG8UeD1yD0eaJAFt2s6x4Oe1OdsryN2oNXgl4AEgUZ5dUlkfDTeTJz23-tJbUOazocTNICzUCkxSLCbq_vPCkFPc5CpeaDkO0WyfjJ6HuzKVAM76HQ55QO1UKY0J9gwXT2N21ZFy8SRaQ_HHala4qbJBFI1Xmvjf57ke1dOPFsBwmFCnL6oMa66LEFOhnY6o614dYmwHgQfp9V-LOe59DYCMhwCeNWES41I7ePOP7lPgk1ELbdmxHtn7on_hkpiT-Lut_Otz3T_21QTPL5S5C0OxiU2ErRD-hfnyyEq96eCy3PBFt6xUJrCoBJ5nJ1TJcHxMH5HLsxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملهٔ سایبری به فروشگاه زنجیره ۱۳۰ سالهٔ هلندی
🔹
فعالیت چندین مرکز توزیع شرکت سوپرمارکت زنجیره‌ای «آلبرت هاین» (Albert Heijn) در هلند، به‌دنبال یک حادثه امنیت سایبری، به‌طور کامل متوقف شده است.
🔹
به‌طوری‌که وب‌سایت، اپلیکیشن‌ها و خدمات مشتریان این شرکت همچنان از دسترس خارج هستند و قفسه‌های فروشگاه‌های آن روزبه‌روز خالی‌تر می‌شوند.
🔹
همچنین، گزارش‌های وجود دارد که کارکنان فروشگاه‌ها مجبور شده‌اند برچسب‌های قیمت را به‌صورت دستی روی محصولات نصب کنند چراکه رچسب‌های الکترونیکی قفسه‌ها قیمت‌های نادرستی را نمایش می‌دهند.
🔹
این اختلال به خارج از هلند نیز گسترش یافته و سایر برندهای متعلق به گروه «آهولد دِلهایزه» (Ahold Delhaize) را هم تحت تاثیر قرار داده است؛ از جمله فروشگاه‌های زنجیره‌ای «هانافورد»، «جاینت فود»، «استاپ اند شاپ» و «فود لاین» در آمریکا.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/468291" target="_blank">📅 23:14 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468290">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">کشته شدن ۴ نیروی امنیتی الجولانی در حماه سوریه
🔹
مرکز موسوم به دیدبان حقوق بشر سوریه: یک گشت امنیتی در حومۀ شرقی حماه، هدف حمله افراد ناشناس قرار گرفت و طی آن ۳ نفر از نیروهای امنیتی دولت الجولانی به ضرب گلوله چند فردناشناس سوار بر موتور سیکلت کشته شدند.
🔹
در یک حمله دیگر، افراد ناشناس به ایست بازرسی الحمرا در ریف حماة حمله کردند که در این حادثه هم یک نفر کشته و چندین نفر دیگر زخمی شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/farsna/468290" target="_blank">📅 23:14 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468289">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkxe_mLWhYZoX0OXTcwMQy-iTbZEtx3cgpGz80detkt4QIsjAwdy8aFrgV4dIewnOR6HiK9IaFnnGO2s4spWz6tK9r6rPblljxQYcoaBEk1aYlVq81gB-_Z-9twy60Ou9C5XbOIwAL43x7EZ0Jy-iDSGTpHFs-XhiONyWlxl-Ysb_w0ExEVKd15EFhp736rJUBwz6no2gLTOx0EvHikVuQ7krWIpcbYZKMOh1uO08pb-IoyssZz-1pxi7_SU-CPdhRclF5HsH8nA13wSQCNPlDGexyOzYEM_n0Q36RcEHPH6qOI2v115TgQr-F3aXCZUaalFPucrNT2-93wQfhHyYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دستخط رهبر شهید انقلاب در تجلیل از شهدای مقاومت
◾️
سلام بر شهدای مقاومت و خیل عظیم مجاهدانی که در این راه جان خود را تقدیم کردند؛سیّدعلی خامنه‌ای
@Farsna</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/farsna/468289" target="_blank">📅 23:07 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468282">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eN-tSoPw0L5aHOLeh4ls9m7k2MseL1bn2naVZAfCiqD1KxbX0HVJdGxksFyMRXTqnAQQbie8xc_cVZ6c13pX4-MGLdtKWbl8znvCh2QcdqnebCoTix3Bmhx5alM1_ojMVXDp6YOH6k7LhcvLuVWVK8E-0J7gjrVY7XHSYI8Yxvi5WYQjjAZogsBCOPlvUb2W-CgN7YMnJSiDDXUqyMTQvp0BFh0To7A79z2xBZ1NWtVcT-V4Zl6x5e8uQ_7DHRQamRqhlhz5yBqonzQV0C93gCZZmvgq8aJNF7luUEJWCDu_m45VANGvKIP5ps75ieHBR2XEP55278ZVbGJcX7BgrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c8cwAxkp8PI7urSclvhYfdUP4IFkipuOVotTl0akRpLOG8L7_DNccIFg7uaLeZp6B9wAr62j-hSS0GepPWVsayKUspK1Bft2q5CehTErDlpliYK_OfLIw82Oj9CPoJ-2MXVNQm7EX_az9XGPhZ_1nUiXzMV8CiQkh2N4I3Un2eEwou0VVgLJxIK9B2Tm7n_Q3sinBTR8bLsvy3GjeTujhoAfYJkaU8cc_oC5JNSzbWsP3UnlJIXN1YlJo_1_OWRb9FQKP3EG-2xCvuntbVFWJRofYLCC0t7kryDzlE8PxAEF_vPLyNxNvmBVJUREB0GtN4UbQXscJI-Khex29IQb8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qa9me7qGKpldyFqTF7VQ6J2_ik1Yic01wYaSTSRSQXDCWNwR53HrwZEJFdtuQRdgJJI54Z_HAcZqJtxIdKboJOdSTXRErqR_THVfQgcIR1goLAQcOL2ewBy6VLjwlYqTpJ-C6aTKVaiY98KV7dRelnDA1cOwPlH_D7TWe85ab9Q93QAawOo7ZeCe0YQkuw-Fh2LWZpE2kaCtJ-giQyt73vY4_ghhKZigrevyGnbW2RUYheL_LqK_BvHlYMHQakMR8CJ8o7fp_xaMYgrnvA1YeKeaoYm_HNugdaUcUypAYV9XQlDr1PCtMnq_ZiJsZT_dvbtWvakSiiinrNbS-Sg9tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MEJpJYGS0L6K2UX9O7mqfzcTt8szMihYlN9H1gtWTWvX-X84HTxzYcn_HZfYKzn45Wseg-3j-N7_3W7o2CiI_crPoR6PTJ8phod4faVtwfOoQVMB7ZjSAcvco6NVlNHSBrKQrehVmlqK_4T_wHxwNqrUhGTN3XEiXCiJ_3v2o5gYowaUjWKNWU7fu1gTfwqDx3zzo5i44XhRGT9sfJ8w64lnnovp-n2BjBa-8R3iNjg160uM4l0sDDEo7AMlKvJHQWR3Vg3VFREmeug_6d5Xej5Ox3u8mtwCXbnYEt6ksQAmXy-ebVkxrwCLhHuD8sbI6r3kbEXNOmvejZnCQWJBTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ERqyAN45NbiIxg6EeV60ftQvVB5-ICLOzNF7-ZiqX6yp8kMhFvQ6O9IRCMaBLM8DUmqBFe125xoMPAE75qwwVzFHbXCpzmRTx8wvjvXKcNCCGl8TrnV5E4DMPeKL3kW3Bpo3jsfA5xRyuQV9iwBFMyDGhqZ6bLox4cEUBL_oq16DrEd6nfXP3W_wlpBgh6e48UhY3yTF1UBZYjHKzA66sayIa_86hyEB_Bft5o0SRUWgHn3HMVZUt1gq_bSy82rozfF5WOOLlvc9BwzHnKTBbH7P-dL1ae0d2mj0lczqSxM2lPSmx4QmgfNf-HLQmgxRu2tgpZdqVhur1apVFnfvyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XT9uuHiovclevfmGzRe97ccqtzveSmN8TxdqjBtf2LEv0y8rYDgn__6-8QXQVOlfCQAqx8ZW7Zk_js6zfUEdUO7j2uUoRp87PYrPQhVnHqQg2AcGIEp30M7-PjI-CGxo0dVZEEtRoS4whB7iA2oF4ac_5BXdEMw3HCI52ovS8MZCFn9gXpebIPfI0YG9ojwCi3uKGdJ-KK6spzn9pzKd_xc_kmhIJQKbobeXA3wkw6_RztTVLUXJSikOkx1E_qvaG3R7sK0Ik3k7G4gNDjTpv_2qEyTtcekKmtqIDb0uTL_PC8-Uu49hXRsY_WFyZRb6-v8FnboQbA3Xz1-idEtDyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mXGm6nMHHzUjmzKwcY10yZ4TjauzrtygH0wWkZ1afmDAz6Ugz6R5bXJLFRnQdNWwjaGtDYZYpVt7HXT5atrWbFDhO3NZB4i0WpXbyL-S9lbuCTG2xG1DVk37OGng7O2LkMqs0HOcx2AScrJUsZRDONhd020W5F6GeQ-LdPhZ9CB2ojqqEcKvrvZjiPGdQ_gbxbXuL7aI16XiG8gTywYb9X6njsirKfzH7QWC1ieUv07OQ2Px0uyOM8gVmdm6e2nG_5rrq582Rv6Ci7g8rUgYINQpP4t5LQH5SqhFiSLe86BAII8icvJT2fLZ5Z3NtWhrSONc8ptKnDnAIZ1AQlrIVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
سرخ‌وسفید پوشانی که شایستۀ تجلیل هستند
عکس:
زینب حمزه‌لویی
@Farsna</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/468282" target="_blank">📅 23:04 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468281">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63ec1cd3c7.mp4?token=Do38GIrskSyMgUXn8FgJZYLV0_AFIofCM75Ij8VUhPFwsxnxjlvoiE8NeNuRhYl03lED4CgTy_xlFeOBZfQS097r_YyA20Diw_6XyUbOYV_vZNghwIh-m6bbVNtJdv5ZxMmuPuFpvxjjXFy3qydDi_VREGdZSO8JJfFM4dg2pgiELt-K_RlZTE10f8KRqiTKkj8pg1-kHPh_W3Z9ThA5XXv5fMOFBZzimkNnBANkmdGWNcTNyj7NmuEUOlXnRm9_xaSpKnCTJyeDCynEa2el_MMl4thJZKnjpMu3vjm2AHQxdJq1DlTNdAEJ8c7v7marbcZdXux3bgzUrke4CYKrvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63ec1cd3c7.mp4?token=Do38GIrskSyMgUXn8FgJZYLV0_AFIofCM75Ij8VUhPFwsxnxjlvoiE8NeNuRhYl03lED4CgTy_xlFeOBZfQS097r_YyA20Diw_6XyUbOYV_vZNghwIh-m6bbVNtJdv5ZxMmuPuFpvxjjXFy3qydDi_VREGdZSO8JJfFM4dg2pgiELt-K_RlZTE10f8KRqiTKkj8pg1-kHPh_W3Z9ThA5XXv5fMOFBZzimkNnBANkmdGWNcTNyj7NmuEUOlXnRm9_xaSpKnCTJyeDCynEa2el_MMl4thJZKnjpMu3vjm2AHQxdJq1DlTNdAEJ8c7v7marbcZdXux3bgzUrke4CYKrvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حماسه‌ای که هرشب در اصفهان پرشورتر می‌شود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/farsna/468281" target="_blank">📅 22:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468280">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/783f7423ad.mp4?token=jdLVfNMAACLq3WSCLmGPcQTYwvh2hBIbzWeMJ1JSCyy4rCo5eWYIbAqNE-lUnhw0ZCN57HHbm5iC-nXDZIYaSvnpOQNseM6iY_Ib9YBiKHvTd5JBxuZOtJTnv3-4OhOcnXV9nnDO20EffjUEGcFrwyQZDLcqZKllQuUFm6BFZ1FqOciNkjXb0Vae_UHOIt4h0ZfT2shXlcuKnZ7ZiDyFgrrY5S6S9HE4N-CJE9JHZAsgRH3_x4XL9pNQjZmcjfWaG89JIjh-oK4EyKhKwff6M2fwP57lNimRwOVib4xfo7oncUTAVY4Vds97T9pXnFo7sjnNr0LmOp0Nu-32Uz6qKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/783f7423ad.mp4?token=jdLVfNMAACLq3WSCLmGPcQTYwvh2hBIbzWeMJ1JSCyy4rCo5eWYIbAqNE-lUnhw0ZCN57HHbm5iC-nXDZIYaSvnpOQNseM6iY_Ib9YBiKHvTd5JBxuZOtJTnv3-4OhOcnXV9nnDO20EffjUEGcFrwyQZDLcqZKllQuUFm6BFZ1FqOciNkjXb0Vae_UHOIt4h0ZfT2shXlcuKnZ7ZiDyFgrrY5S6S9HE4N-CJE9JHZAsgRH3_x4XL9pNQjZmcjfWaG89JIjh-oK4EyKhKwff6M2fwP57lNimRwOVib4xfo7oncUTAVY4Vds97T9pXnFo7sjnNr0LmOp0Nu-32Uz6qKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تگرگ در بشاگرد هرمزگان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/468280" target="_blank">📅 22:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468279">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1ecf4b508.mp4?token=AwK_MmavvbvvftRMtKuLXnOK0NTxlzbpwl-3gkuLrBPmA9CJ1XLsCRXiods5QSpOc4p7SgcVhVnNMfNhfheA_dRWpF6CgJxejCiEo5DiiD0wkgtjCrSGx415FL-mk9IrktFK5k4uJzjY4llbkOPixz_wveG-28jaJoiogw3D0UPISu62PuXNW6HUl0f9xwM_MPI6Vq3uuOYnVS1KQc7xEo9Ax-HoV5ymjubjTvNHjPtKPf4tX5V7eYKYX3NTAOgHHdqPow0sSOffi_HQdJy8D-dmhtfuUc2HouJcA1oF0X7O6zPlrRDR79OcclImA9T45dNw_AMmMpHGnxBRY7_krg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1ecf4b508.mp4?token=AwK_MmavvbvvftRMtKuLXnOK0NTxlzbpwl-3gkuLrBPmA9CJ1XLsCRXiods5QSpOc4p7SgcVhVnNMfNhfheA_dRWpF6CgJxejCiEo5DiiD0wkgtjCrSGx415FL-mk9IrktFK5k4uJzjY4llbkOPixz_wveG-28jaJoiogw3D0UPISu62PuXNW6HUl0f9xwM_MPI6Vq3uuOYnVS1KQc7xEo9Ax-HoV5ymjubjTvNHjPtKPf4tX5V7eYKYX3NTAOgHHdqPow0sSOffi_HQdJy8D-dmhtfuUc2HouJcA1oF0X7O6zPlrRDR79OcclImA9T45dNw_AMmMpHGnxBRY7_krg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش اختصاصی شبکه سه از وضعیت نابسامان کمبود آب و غذا در غزه
@Farsna</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/farsna/468279" target="_blank">📅 22:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468278">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‌ ‌
🔴
سخنگوی ائتلاف سعودی وقوع حمله به نقاطی در الظهران و حرض در شرق عربستان را تایید کرد. @Farsna</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/468278" target="_blank">📅 22:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468270">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a00I6F83Dk5s7dRcBu5EOVJu-4w6CYAVSDpsCMIf4lu4JupYMOirum32fCuyR_ctgWbrtMc2-_02ePjIyLVLdRK0ORTYFPoPjnB6EZ0YeoWXEwerdLhf2KAlu_JtW3yyR33w1xa2tIhk_tw4XAwMVFgoeltix9MnH4wboLhDuf_dWlhKAPe4KtpxxzFHpZ2lPiSMmhE3Lz-hMradBTVj-zhgAaYE0NLK_QXAntiQJ2tQTgUjCxyex4Dnv6kBRT3XlFhECyLOdlal73pZnRER8SA56ATA4nAS-HUbWTjldkJ8BP3-s_EfMcnd8bQSfwkReMoLcPEXqZ0aQwWkERyVbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک نفتکش دیگر در تنگۀ هرمز هدف قرار گرفت
🔹
سازمان تجارت دریایی انگلیس: یک نفتکش در تنگۀ هرمز هدف اصابت پرتابه‌ای ناشناس قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/468270" target="_blank">📅 22:39 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468269">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">احضار مسئولان میراث فرهنگی همدان پس از انتشار فیلم یک بلاگر در غار علیصدر
🔹
معاون دادستان استان همدان: درپی انتشار فیلم شنای یک بلاگر در غار علیصدر و انتقادها دربارۀ نحوۀ حفاظت از این اثر ملی، مسئولان میراث فرهنگی برای ارائه توضیحات فراخوانده شدند.
🔹
هیچ‌کس حق ندارد به بهانه تولید محتوا یا جذب مخاطب، ضوابط حفاظتی این اثر ارزشمند را نادیده بگیرد و آن را در معرض آسیب قرار دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/farsna/468269" target="_blank">📅 22:36 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468268">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aba203693.mp4?token=KDG_9dLq075mpCdudnQKrsAWLMKIZJdUSacAz-ZLfm1PmRdTyKcjcGKLRFARo4TbiCXGY_zTAJ49cVoCSuUhGaKKOAwZC2Rxg1R8JvfCmqLQrFgNBp7wYOmYf6ANhM7aq361PrvU4i4b4QnTjz_dXhgPj1Ci67o_m_UbBH_e7lzd230onxaOGsd6SF1b9cQkj8qwD0pry2E_3IGEW5tLKh1NIgqZf1YLiWCiEDRx7JX1GpmAFw2cliVhf2fy8E0PxZ_9vmDGbQUO3iqY7_p5TuN1R7e9YQJNfW-CJTue8vN5dHpvuemoZ063c9f8jHpYyh5NYUUVsI9t5vLR2CV4MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aba203693.mp4?token=KDG_9dLq075mpCdudnQKrsAWLMKIZJdUSacAz-ZLfm1PmRdTyKcjcGKLRFARo4TbiCXGY_zTAJ49cVoCSuUhGaKKOAwZC2Rxg1R8JvfCmqLQrFgNBp7wYOmYf6ANhM7aq361PrvU4i4b4QnTjz_dXhgPj1Ci67o_m_UbBH_e7lzd230onxaOGsd6SF1b9cQkj8qwD0pry2E_3IGEW5tLKh1NIgqZf1YLiWCiEDRx7JX1GpmAFw2cliVhf2fy8E0PxZ_9vmDGbQUO3iqY7_p5TuN1R7e9YQJNfW-CJTue8vN5dHpvuemoZ063c9f8jHpYyh5NYUUVsI9t5vLR2CV4MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
باران شدید پاییزی، دشتستان در استان بوشهر را غافلگیر کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/468268" target="_blank">📅 22:32 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468267">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c18c34af21.mp4?token=mG6GyHmSGYUVhcYqUXfKZFOSeOHj3854ETDKSobL2dULpbrfpFx0ApcOHz5zqZ9PBIb0nirpo0PaMTmL98fhQ6lJGAkVGE8AkXuJgTI1FULcMPIe4abs4_Ng94arFVAKV1wW0dwC74bAiS5_BVXETOE-6OD2KG6mrZsL9T_fO9AscqEXPVWmNAFYL43YMJjkDLTaA1Y37mNiXEpdNrhxFiFJrPlJrHQG83yOESn29oSsz8TQVPv1rgCY3mWJJBxoVuEypX9PKaz9gwTVvnjQh_P4C-RvjMchABA5Wu8I3syCj4_ItfYtutlfHxkxyE_NHxWTyJwh2fUrJ2SqpG42dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c18c34af21.mp4?token=mG6GyHmSGYUVhcYqUXfKZFOSeOHj3854ETDKSobL2dULpbrfpFx0ApcOHz5zqZ9PBIb0nirpo0PaMTmL98fhQ6lJGAkVGE8AkXuJgTI1FULcMPIe4abs4_Ng94arFVAKV1wW0dwC74bAiS5_BVXETOE-6OD2KG6mrZsL9T_fO9AscqEXPVWmNAFYL43YMJjkDLTaA1Y37mNiXEpdNrhxFiFJrPlJrHQG83yOESn29oSsz8TQVPv1rgCY3mWJJBxoVuEypX9PKaz9gwTVvnjQh_P4C-RvjMchABA5Wu8I3syCj4_ItfYtutlfHxkxyE_NHxWTyJwh2fUrJ2SqpG42dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ ‌
🔴
سخنگوی ائتلاف سعودی وقوع حمله به نقاطی در الظهران و حرض در شرق عربستان را تایید کرد. @Farsna</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/farsna/468267" target="_blank">📅 22:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468266">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b88f2193bf.mp4?token=Nu8mLCJPI5c6PBTj0hUFi4f4JiE9m6w-wk2GGrIGk6LqD_nwYfRlJJQoXCWz8CcyAi1hk8fXk-FjfCtuHJ4CbD2oVvRqAAvE9rEMThO3ilsJL6PhZwbrzsFtxEb8KUpntB0fHHK0dGc25MMevzRlYwmyy_eg7dk7jMydUFqmkAULtDPJjQr7tnfQKYEWqEeuYWMX6SDEmPhvyfP68Xv9670X7Bk_gDlq9q-Q15sqVERPyf-KwjSoeddGbZ9E1JYxS6mBriFmMpix-V3GPGKgVhf3V5vlnNhQtzDBQCDIIC5_kt_fvbyXXA1aB5XGk01I0fY8h12NUQCIL9iYqTZfuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b88f2193bf.mp4?token=Nu8mLCJPI5c6PBTj0hUFi4f4JiE9m6w-wk2GGrIGk6LqD_nwYfRlJJQoXCWz8CcyAi1hk8fXk-FjfCtuHJ4CbD2oVvRqAAvE9rEMThO3ilsJL6PhZwbrzsFtxEb8KUpntB0fHHK0dGc25MMevzRlYwmyy_eg7dk7jMydUFqmkAULtDPJjQr7tnfQKYEWqEeuYWMX6SDEmPhvyfP68Xv9670X7Bk_gDlq9q-Q15sqVERPyf-KwjSoeddGbZ9E1JYxS6mBriFmMpix-V3GPGKgVhf3V5vlnNhQtzDBQCDIIC5_kt_fvbyXXA1aB5XGk01I0fY8h12NUQCIL9iYqTZfuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام خلج: گاهی یک امتحان کوتاه الهی می‌تواند درهای بزرگی از رحمت و روزی را به روی انسان باز کند
@Farsna</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/farsna/468266" target="_blank">📅 22:28 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468265">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‌ هشدار فوری یمن برای تخلیۀ فرودگاه ریاض و ۲ تاسیسات نفتی
🔹
سخنگوی نیروهای مسلح یمن: در صورت انجام حملۀ اعلام شده دشمن سعودی به صنعاء، مقر شرکت آرامکو در الدمام و نیز فرودگاه ملک خالد و پالایشگاه شرکت آرامکو در ریاض باید فورا تخلیه شوند. @Farsna</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/468265" target="_blank">📅 22:19 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468264">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‌
🔴
منابع عربی از حملۀ موشکی یمن به آرامکو در شرق عربستان خبر می‌دهند.
🔹
به گفتۀ این منابع، ریاض پایتخت سعودی نیز هدف حمله قرارگرفته است. @Farsna</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/468264" target="_blank">📅 22:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468263">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‌  حملات موشکی یمن به شرق عربستان
🔹
سازمان دفاع مدنی عربستان با تأیید ضمنی حملات یمن، از فعال شدن آژیرهای خطر در شرق این کشور خبر داد. @Farsna</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/468263" target="_blank">📅 22:10 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468262">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50387948a4.mp4?token=L5voXJ-yTscoGwarfLZP9HLIv4arZANAntoRVJ4KeCRxlzsKmfsXOe__RXqe0E1-g3SsHRTHJTSvPUe_ZKblUxmGcfvcsRb7-bU1oVdagmJvMRdP-TeivjWcyP1fnUKz8nADXhv3yTY7_G01aF2RHUv2uOn5zeh5R5Z_nK7cNMfAu6mcfST7wN0slpsToprqU7jzlB-zZjISRVZ8jfh7O9nEFdvzD3ai4LKWP213YmKA2_qa3CxE6OQT9gh_Fc619azeqv_X-dqkM_arYqnqtxaz8NpvFDwUBMsh6GHwlTt5WWP0gjcsf_e-WnRqw9nXmGgFYenlYVPQNGH3ZBvDhTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50387948a4.mp4?token=L5voXJ-yTscoGwarfLZP9HLIv4arZANAntoRVJ4KeCRxlzsKmfsXOe__RXqe0E1-g3SsHRTHJTSvPUe_ZKblUxmGcfvcsRb7-bU1oVdagmJvMRdP-TeivjWcyP1fnUKz8nADXhv3yTY7_G01aF2RHUv2uOn5zeh5R5Z_nK7cNMfAu6mcfST7wN0slpsToprqU7jzlB-zZjISRVZ8jfh7O9nEFdvzD3ai4LKWP213YmKA2_qa3CxE6OQT9gh_Fc619azeqv_X-dqkM_arYqnqtxaz8NpvFDwUBMsh6GHwlTt5WWP0gjcsf_e-WnRqw9nXmGgFYenlYVPQNGH3ZBvDhTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم ایستادگی در دستان مردم مراغه ؛ دفاع از میهن در شب ۲۲۷
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/468262" target="_blank">📅 21:54 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468261">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42a345b3c5.mp4?token=XZM7GRi5GCggxov8v5gX-lcxRmgunWB5qj_qeWHME4CZVLsCK-2cAYAis4GVhaRp9aAGVJJL1kDIhcmphSQ_YzWoc1uziRsH0MfuqyG1D4Km2_PRL3uf0Hl5F4viQ6TvsTrT1cC3tdbwPl4vBNhS5Y5pciVnXYKmAZHgGv2bcCXCFWVLfROF8T5ifupDBod8gVRdXJ2P0AI7ATABkx611cnCm_EDN5hgSuu8rtAt4S5H8WU1WR1m9qq4rThjUehUYQAq_d3zifIyKIG3Xo6n8kA1YaA8p5D9XwdVyHEDOKIA59Z3sH8YPSxhSfD2ppmVInHl6JQ5MeWMXCyFo_J4UZphozS8hx7pwXgB173LMVFCAv_tYuG9PqZ4xC_a2gAm9_DOwIKPQPSKldjdNtZ6e6yoAqP76C5mfFRztmNRLN1xnCNBGN9FxiAacFPg_UHN4BdX64GZfecOGuMcNHhdZMb0Oum4jsT2KYbQA0NZtMrA2HF2HkTKmZfQCHyUkMEoboA4w8mkx6qrM150tMRGHmIqL4pTIi1IbVqSObA3V0HTRBnv3EIAbnzAuCpWozaYe4Xf4NV1J-wcWJ_wm7i7U6UpfqXi-3UOWF3v3tG9EHvwab1_Wuwc0s-5sxuiSdztzTYgzKCcqsI0m6Q1IiyvCmgzAYxPkkkCRGQguVdeVq4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42a345b3c5.mp4?token=XZM7GRi5GCggxov8v5gX-lcxRmgunWB5qj_qeWHME4CZVLsCK-2cAYAis4GVhaRp9aAGVJJL1kDIhcmphSQ_YzWoc1uziRsH0MfuqyG1D4Km2_PRL3uf0Hl5F4viQ6TvsTrT1cC3tdbwPl4vBNhS5Y5pciVnXYKmAZHgGv2bcCXCFWVLfROF8T5ifupDBod8gVRdXJ2P0AI7ATABkx611cnCm_EDN5hgSuu8rtAt4S5H8WU1WR1m9qq4rThjUehUYQAq_d3zifIyKIG3Xo6n8kA1YaA8p5D9XwdVyHEDOKIA59Z3sH8YPSxhSfD2ppmVInHl6JQ5MeWMXCyFo_J4UZphozS8hx7pwXgB173LMVFCAv_tYuG9PqZ4xC_a2gAm9_DOwIKPQPSKldjdNtZ6e6yoAqP76C5mfFRztmNRLN1xnCNBGN9FxiAacFPg_UHN4BdX64GZfecOGuMcNHhdZMb0Oum4jsT2KYbQA0NZtMrA2HF2HkTKmZfQCHyUkMEoboA4w8mkx6qrM150tMRGHmIqL4pTIi1IbVqSObA3V0HTRBnv3EIAbnzAuCpWozaYe4Xf4NV1J-wcWJ_wm7i7U6UpfqXi-3UOWF3v3tG9EHvwab1_Wuwc0s-5sxuiSdztzTYgzKCcqsI0m6Q1IiyvCmgzAYxPkkkCRGQguVdeVq4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دبیر شورای‌عالی فضای مجازی: شناسایی پایانه‌های استارلینک از اولویت‌های ماست
🔹
فناوری‌های مورد استفاده برای شناسایی و مقابله با استارلینک، به اختلال در جی‌پی‌اس محدود نمی‌شود و فناوری‌های دیگری نیز در این زمینه به کار گرفته شده است.
🔹
هدف از مقابله با استارلینک،…</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/468261" target="_blank">📅 21:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468260">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iaYqWjIveRSun1OWrawgvwKk5ozYBSedSh2DeJfm0zI0UFXN51FtdhfD5gQ7shM1p2f2KZFa8WtGPwadx6AFtnKI7p7rpT1NlH9FPyowLDcf8OAGYfj93T6OUwTKro8UP5WYczASajrBnGo-0t_6urhSeHbKRpjhO13Gzb2Cz5NUfsP0wnLOZyNQTRxBL_F47IetFG0Wq8e4rv3B9fDmvCdjGB7ChqoAhq7H6C-VkJ5vlDgUFAz5yg2qtFflRLupns8FDAyeazxytcQ1bI8121HfbLS_Hwl0lWBuJATg9XlDVgw8PZaKkm-1YVv5_2ZPyw2eWgf582xKhjSCRJ-e5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مراسم اولین سالگرد سردار علیرضا افشار
🗓
شنبه ۲۵ مهر از ساعت ۱۵ تا ۱۶:۳۰
🔹
میدان جهاد مسجد نور
@Farsna</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/468260" target="_blank">📅 21:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468259">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhvwazojONZTzVzn_m-UcoFSg_mz9ezSHXwoQtSefkNMO3dZzdz_NjR26Y2KegGuV7dnKKJ6d9M89MtXWcKSRVuJchc4FA8FrL1CroYCUWfzLhvG0pM6WbnmsAmZQtFaD99-77oEYHaSfQfy8IZmZA-I_rq--C2BMOhAUqN2Kwmpp9PQwWaGK__cVcvBhJN7HZdlDuP2VwisgtM1XRLZuJY3HSFvl9U6LFDCjx_Cfjxh97XYkMYb1bQoTHqUD6GsxY7NiXOh9fOHJ9hRhQ6hCH0T6b0n7sCEhIF9rzz5QENfrbJCYvVuRfCQ_7EzGpRe0RvF2z0dZcmt9bYvr7aV9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماجرای نامۀ تکراری منشی ویژه‌ی رهبر شهید
🔹
شهید سعید صاحبدل، منشی ویژه‌ی رهبر شهید انقلاب، در نهم اسفندماه ۱۴۰۴ در محلّ کارش در دفتر رهبری، همراه رهبر شهید انقلاب به شهادت رسید.
🔹
او از دوره‌ی ریاست جمهوری جزو همکاران رهبر شهید انقلاب شده بود و پس از آن به دفتر رهبری آمد. مردی که سال‌ها در سایه‌ی سکوت، امانت و اخلاص خدمت کرد و بی‌آنکه بخواهد نامی از خود به جای بگذارد، الگویی از پایبندی به تکلیف، رازداری و ساده‌زیستی بود.
🔹
خانواده شهید: حاج سعید در جلسه‌ای در دفتر رهبر شهید انقلاب حضور داشت که ایشان وارد اتاق شدند و خطاب به شهید صاحبدل فرمودند: «آمده‌ای همکار ما بشوی؟» حاج سعید، با همان سادگی همیشگی، پاسخ داد که در دفتر ریاست جمهوری مشغول گردآوری اسناد است.
🔹
رهبر انقلاب فرمودند: «اسناد را سایرین هم می‌توانند گردآوری کنند؛ شما به دفتر ما بیا.» این دعوت، تنها جابه‌جاییِ محلّ خدمت نبود؛ بلکه نشانه‌ی اعتمادی بود که به شخصیّت و منش او وجود داشت.
🔹
روزی نامه‌ای را خدمت رهبر شهید انقلاب برد و ایشان فرمودند نامه تکراری است؛ حاج سعید از تکراری بودن نامه خبر نداشت، زیرا نامه‌های محرمانه را نمی‌دید و خود را مجاز نمی‌دانست از محدوده‌ی مسئولیّتش فراتر برود.
🔹
در جریان جنگ ۱۲ ‌روزه نیز از آرامش و اعتماد او روایت‌هایی نقل شده است. در آن روزهای دشوار، هنگامی که برای همۀ مردم امکان فراهم کردن پناهگاه وجود نداشت و رهبر شهید انقلاب نیز به همین دلیل در پناهگاه حضور نیافتند، جمله‌ای بر زبان ایشان جاری شد: «این مملکت، مملکت امام زمان عج است و آسیبی به آن وارد نمی‌شود.» حاج سعید، در چنین فضایی، همچنان همان خادم آرام و وظیفه‌شناس بود.
@Farsna</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/468259" target="_blank">📅 21:49 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468258">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acb5ecb019.mp4?token=N25ofN9jAEI4gezla6zVY3vCNEN8DJno5cOSPviHcviy40ITBE7kosv8i0_ZVf5x89iBlvZUllP2idUMPIvrokQrqhrHKxeHgK8X-mU60Srid6eMuyf5gMCPyyzKVzpkdEWZhMJF5xT3K35ebHpAkZoECpTCyxudg5qbnaTRlArffDfyMCk20G9U68RD1ZjMbtnES-owX8MNuXldDnoWtygkP-9rTbW8-OYUDtqas8CdD4h8KyUlUhdMXDcCU7PpewY48Ol_MUBhjAS4vphTw6yluqpxtZMxk7LSGjTz0v-K1xGQF6z9aJ8Efn2M2WR0th9ZepW7f99Egtq-tXK4DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acb5ecb019.mp4?token=N25ofN9jAEI4gezla6zVY3vCNEN8DJno5cOSPviHcviy40ITBE7kosv8i0_ZVf5x89iBlvZUllP2idUMPIvrokQrqhrHKxeHgK8X-mU60Srid6eMuyf5gMCPyyzKVzpkdEWZhMJF5xT3K35ebHpAkZoECpTCyxudg5qbnaTRlArffDfyMCk20G9U68RD1ZjMbtnES-owX8MNuXldDnoWtygkP-9rTbW8-OYUDtqas8CdD4h8KyUlUhdMXDcCU7PpewY48Ol_MUBhjAS4vphTw6yluqpxtZMxk7LSGjTz0v-K1xGQF6z9aJ8Efn2M2WR0th9ZepW7f99Egtq-tXK4DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وکلای جدید تهران سوگند یاد کردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/468258" target="_blank">📅 21:41 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468257">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e6e15db74.mp4?token=F-WHFddaLkveWJk0aEjdPfFRkwGf59pHZZ5YH412BOPcedwGmt7YYCt6pEwbHfz9Sropxccb4g1WxNENrOwnXZijZAYl-yzN8euXrutntjKzQrC9WTf1SKW2sD4kofTadfEVdn9T5mUeehXqmFayXtfPlp8a66FnJJSsN9cWKOPvUNif_AASOZYSPyPoFI9DnAZ9N3gXcQPL68_ABWlr3blP-ZGEc2629jAjIilDTSitXx-2EJEpg1YTfQWxMlLaUMVJVa1k58EnyaBbsld8E2rDVLTGCTt5CnReGbmoGR-tHqAWF4pHNYX3-APRV43IRh5gvSH1gUKP57HUkkvhGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e6e15db74.mp4?token=F-WHFddaLkveWJk0aEjdPfFRkwGf59pHZZ5YH412BOPcedwGmt7YYCt6pEwbHfz9Sropxccb4g1WxNENrOwnXZijZAYl-yzN8euXrutntjKzQrC9WTf1SKW2sD4kofTadfEVdn9T5mUeehXqmFayXtfPlp8a66FnJJSsN9cWKOPvUNif_AASOZYSPyPoFI9DnAZ9N3gXcQPL68_ABWlr3blP-ZGEc2629jAjIilDTSitXx-2EJEpg1YTfQWxMlLaUMVJVa1k58EnyaBbsld8E2rDVLTGCTt5CnReGbmoGR-tHqAWF4pHNYX3-APRV43IRh5gvSH1gUKP57HUkkvhGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مادر همسر رهبر انقلاب: آیت‌الله سیدمجتبی خامنه‌ای در خاکسپاری رهبر شهید در حرم امام رضا(ع) حضور داشتند و ایشان در صحت و سلامتی کامل هستند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/468257" target="_blank">📅 21:39 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468256">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">خداداد عزیزی ۴ ماه و عالیشاه ۴ جلسه محروم شد
⚽️
کمیتۀ انضباطی فدراسیون آرای مربوط به حواشی دیدار تراکتور-گل‌کهر را به شرح زیر اعلام کرد:
🔹
خداداد عزیزی ۴ ماه محرومیت از ورود به ورزشگاه‌ها و ۲ میلیارد تومان جریمه
🔹
امید عالیشاه ۴ جلسه محرومیت از مسابقات و ۵۰۰…</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/farsna/468256" target="_blank">📅 21:37 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468255">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lNL7ghhymSGAR6Tlz94Vl1IrFUgrw50kFPQZ2vsEhetwX1N47Cc0j_jcwb38xuhuW8Vib5L8CTk0BSX1RVHhPOBTTOUcv_XugMsSQXZubvjSnIayeAG1uJWo-D5zHT9rC6CDKm2RrkthACy4WF58o3d-KxqPXAPWwg0pceqDf2FJ419xxao1F4pAVQNN9jzd_phEMyplpYWFYzS487PvfAe8Kqnbb8nAIwbCmEM9unBepjI8AtrRb3w-pQKQGZYreu-SpztuO58OsYZ59_SGN24KyGxSYcfeRCgWbW3b3l_6YFgVp0UJou8Nw9mMPqbceqm19CUMc9z7Fz4Ea-mtSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی ارتش: حضور مردم در میدان در محاسبات دشمن لحاظ می‌شود
🔹
اجتماعات شبانه و حضور مردم در میادین و خیابان‌ها از مصادیق قدرت نرم است و به‌شدت در محاسبات دشمن نیز لحاظ می‌شود.
🔹
این حضور باعث دلگرمی و احساس مسئولیت بیشتر رزمندگان برای انجام درست وظایف خود می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/468255" target="_blank">📅 21:36 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468254">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c4e437586.mp4?token=AXhnaDT5EJyyV2RXtaoFCMrlCDXv2vDH9gHv-osoSD-mc4GWrFwx1wDqfxKuL9Oj3T5ap11yz6Q9gmynDW-GXzk9HkVcPyQglkU7LXNXx2D-dKwec6HN1M72i5ByoRiRW0ezJQG7FAw-Rr7CoufpLGJ0zYUhuuSiLYSgyuOMWTnXSfQGLMsueCp2K3zgTUa0mwRfcPUqP1RzDDwcs9jXt6t_Yjx5w8azthg7scDSS0NjedjZbIrW_LSltfzZ2UjkNw2uKeL0POhZDixSXG_0KM1pdFBxia0TGORSLhFLtjri6blK1oNCgUpXr4RrP3fuEtEiCOLe2ULVPy8iitjS2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c4e437586.mp4?token=AXhnaDT5EJyyV2RXtaoFCMrlCDXv2vDH9gHv-osoSD-mc4GWrFwx1wDqfxKuL9Oj3T5ap11yz6Q9gmynDW-GXzk9HkVcPyQglkU7LXNXx2D-dKwec6HN1M72i5ByoRiRW0ezJQG7FAw-Rr7CoufpLGJ0zYUhuuSiLYSgyuOMWTnXSfQGLMsueCp2K3zgTUa0mwRfcPUqP1RzDDwcs9jXt6t_Yjx5w8azthg7scDSS0NjedjZbIrW_LSltfzZ2UjkNw2uKeL0POhZDixSXG_0KM1pdFBxia0TGORSLhFLtjri6blK1oNCgUpXr4RrP3fuEtEiCOLe2ULVPy8iitjS2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اعتراض کاربران به ملوانان آمریکایی؛ چرا کودکان را می‌کشید؟
@Farsna</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/farsna/468254" target="_blank">📅 21:32 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468253">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">📷
هشدار تخلیۀ یمن برای ۳ نقطۀ عربستان  @Farsna</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/farsna/468253" target="_blank">📅 21:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468252">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYZVAI6KR0nocAJwVWg1CAXx5c3KQVfTExquyp_EMU4Fs3csVRlFu03McytoHp1cwSzJRrNbVF4FklFMV-ViABlhKspgoIEju5eRvBxHxp0UZA1m5-H6iZ05YicuQsMBQzYC9jeC6bAwLftjFjhLz-s6ljhNEoPFVUe1ZBQSoSDnXE9yWZ3gpy7-Y1-euy5oRtK_qG5zX8D9_xTyX6msuPGIoS7AcpfsGiUOPjazP5eR0dMUHHcg_NY-nGbtcY5oI9B99nRKH_-dlyC5lIzZx69ffUsqNIaMSLrehnhMgOfZK9k9cwC_pTQAad9H3zFemQha1QcYfqvVrYpCLg2DSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلنسکی: روسیه پس‌از اعلام آتش‌بس انرژی توسط ترامپ، به تأسیسات انرژی اوکراین در کی‌یف و خارکیف حمله کرد.  @Farsna</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/468252" target="_blank">📅 21:26 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468251">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
توپخانۀ ارتش اشغالگر اسرائیل شهرهای المنصوری، بیت یاحون در صور و شهر بنت‌جبیل را بمباران کرد.
🔹
ساعتی قبل نیز زوطر شرقی و میفدون هدف حملات صهیونیستی قرار گرفته بود.
@Farsna</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/farsna/468251" target="_blank">📅 21:22 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468250">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">بقائی: عملیات‌های پرچم دروغین جنایت‌های آمریکا و اسرائیل را نمی‌پوشاند
🔹
سخنگوی وزارت خارجه با انتشار ویدئویی درباره تاریخچه عملیات‌های پرچم دروغین آمریکا و رژیم صهیونیستی در ۷ دهۀ گذشته نوشت: پرچم‌ دروغین، شگردی دیرینه‌ است: اول صحنه‌سازی کن، سپس انگشت اتهام…</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/468250" target="_blank">📅 21:10 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468248">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14358db62.mp4?token=suwtdIVoG8gje59FKJZ8aBDteGXXngnVkfp2ZZk5u2XS14ucaYtz1du6dNlev7LtjwGgxGou4YMPOziVzAsqle4JayaI4jtuiK6r0kiDwWoci7s83_V4_7KCNZ-ZBs8HNG2rz4hMKuT0oxDiAZIa4sCRouZlRNVLBtOBeb1v5afVg-Xh3NnN98s6h6wtPCd2e1EssdRNLGU3YmkS_cauqgLdAOD0c3S8gLk3GOkSDGZLqm1Ovhaa4_bVpAjgF0GYSQqBeML-DXV8jhPyK-dbjyYW8p03Ob8pBcsr90hNKBKnffZRfd1EwyxxUQcLQe1Ow9rupj-JChMIOyhbfWhYLwqnh4pyDXio5JIfuJtMc-WzDAIRKpe64KrO1JZbZmfDM4Iqax3b2iyRvyWAhVdOEvDFJJoK0UohIC0h_2Pk1vtnFRUzpPQxuX9tYkDc5pFbU2v4-C0ObNI0ThDujUVfLuM8tOZyYPqgcnqV-iLB2js5Glv9kbMfYEWeJC9Kjl5DEVnVUvZzANje8zC7h1KWXoqwbtH19RA9hBj7ZFPwU4G8VM8pjFU5qbuve3GESGeQ3vIFGhlw1MrANMXyRlvmPmWo_kGRgoJ2qfaYxkAT6RkvR0KxVC-7YOMjcHvdj6M0_eBfH_1QxXQj4aHbyXH--K28lQRmDlff2vBTA_PvKw8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14358db62.mp4?token=suwtdIVoG8gje59FKJZ8aBDteGXXngnVkfp2ZZk5u2XS14ucaYtz1du6dNlev7LtjwGgxGou4YMPOziVzAsqle4JayaI4jtuiK6r0kiDwWoci7s83_V4_7KCNZ-ZBs8HNG2rz4hMKuT0oxDiAZIa4sCRouZlRNVLBtOBeb1v5afVg-Xh3NnN98s6h6wtPCd2e1EssdRNLGU3YmkS_cauqgLdAOD0c3S8gLk3GOkSDGZLqm1Ovhaa4_bVpAjgF0GYSQqBeML-DXV8jhPyK-dbjyYW8p03Ob8pBcsr90hNKBKnffZRfd1EwyxxUQcLQe1Ow9rupj-JChMIOyhbfWhYLwqnh4pyDXio5JIfuJtMc-WzDAIRKpe64KrO1JZbZmfDM4Iqax3b2iyRvyWAhVdOEvDFJJoK0UohIC0h_2Pk1vtnFRUzpPQxuX9tYkDc5pFbU2v4-C0ObNI0ThDujUVfLuM8tOZyYPqgcnqV-iLB2js5Glv9kbMfYEWeJC9Kjl5DEVnVUvZzANje8zC7h1KWXoqwbtH19RA9hBj7ZFPwU4G8VM8pjFU5qbuve3GESGeQ3vIFGhlw1MrANMXyRlvmPmWo_kGRgoJ2qfaYxkAT6RkvR0KxVC-7YOMjcHvdj6M0_eBfH_1QxXQj4aHbyXH--K28lQRmDlff2vBTA_PvKw8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرمانده نیروی دریایی سپاه: امروز آمریکا  با ۷ ناوگان خود به قاچاقچی سوخت تبدیل شده
🔹
ناو ۱۳ میلیارد دلاری آمریکا بی‌خاصیت شده و ۷۰۰ کیلومتر از تنگۀ هرمز فاصله گرفته زیرا جرئت ندارد به تنگۀ هرمز نزدیک شود. @Farsna</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/468248" target="_blank">📅 21:01 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468247">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5895cf7046.mp4?token=KQkiiRPboP4gtL9eoKxyeixpE0_5JRry66tr1MawF4Ozo0xzBpaH1BVruMJmHWFndZBkbjDmBVQQRzXahu64w8bbmoh_DXJ18YW2cnhJxuB48ghHpDSGy9zdFd4qJIZ_FCV14_oSITDoaltRt2GNh7EBOW9LFjtI9ZfMdrHUxCL6Fuml_B1NKKsZS8Ar0IM7qwtqOcJj9cuGf-uoSB85vkqlHNhcSJoYeG6A36HHY1ZhMSfEbOZlLbFi3vn0pkl7WZ2BHD8jYuFax8_BYDY4gne94zWvBj2tgcnxfMzJ7DwelQkCoeYXKSBCVrEscz4e6NSQNhhNEAwNDxbvZe5n9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5895cf7046.mp4?token=KQkiiRPboP4gtL9eoKxyeixpE0_5JRry66tr1MawF4Ozo0xzBpaH1BVruMJmHWFndZBkbjDmBVQQRzXahu64w8bbmoh_DXJ18YW2cnhJxuB48ghHpDSGy9zdFd4qJIZ_FCV14_oSITDoaltRt2GNh7EBOW9LFjtI9ZfMdrHUxCL6Fuml_B1NKKsZS8Ar0IM7qwtqOcJj9cuGf-uoSB85vkqlHNhcSJoYeG6A36HHY1ZhMSfEbOZlLbFi3vn0pkl7WZ2BHD8jYuFax8_BYDY4gne94zWvBj2tgcnxfMzJ7DwelQkCoeYXKSBCVrEscz4e6NSQNhhNEAwNDxbvZe5n9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اخلاقی، وزیر پیشنهادی دفاع: برنامهٔ دفاعی شهید نصیرزاده را با قدرت ادامه خواهیم داد
@Farsna</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/farsna/468247" target="_blank">📅 21:01 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468246">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d12ce974bc.mp4?token=Vf8NSgy82fYKKD2WQ8RLdo8UMjTztHz0KSJT0z43RSaBUlLssAcHrxnrstWzXnFQsW5dJOF04Zi1ST176Inb-dPsVumzS-KjoiNiGEkFcML6BFQ5N3I30wMZd7kwin-jWy33IoB51nik7W237bKukhl-Jb6K85MjHk5W3DFmMZtZKmHS-VJzXcEXTGQ1FeoEL5lJHC7MQ91ququAvegABF4Rsyy0XjJa36Y9hnj3AuSdgW8LbZUAV7uwBGYHtLgbum97NI-XU9xXwcBnFPUUFJQLt4KtBXbi3KKmtWee9_Lp8lUyFaL3MxoTEliTU2ZQmVK_w6j1DoimEtViAdf0Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d12ce974bc.mp4?token=Vf8NSgy82fYKKD2WQ8RLdo8UMjTztHz0KSJT0z43RSaBUlLssAcHrxnrstWzXnFQsW5dJOF04Zi1ST176Inb-dPsVumzS-KjoiNiGEkFcML6BFQ5N3I30wMZd7kwin-jWy33IoB51nik7W237bKukhl-Jb6K85MjHk5W3DFmMZtZKmHS-VJzXcEXTGQ1FeoEL5lJHC7MQ91ququAvegABF4Rsyy0XjJa36Y9hnj3AuSdgW8LbZUAV7uwBGYHtLgbum97NI-XU9xXwcBnFPUUFJQLt4KtBXbi3KKmtWee9_Lp8lUyFaL3MxoTEliTU2ZQmVK_w6j1DoimEtViAdf0Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرمانده نیروی دریایی سپاه: امروز آمریکا  با ۷ ناوگان خود به قاچاقچی سوخت تبدیل شده
🔹
ناو ۱۳ میلیارد دلاری آمریکا بی‌خاصیت شده و ۷۰۰ کیلومتر از تنگۀ هرمز فاصله گرفته زیرا جرئت ندارد به تنگۀ هرمز نزدیک شود. @Farsna</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/468246" target="_blank">📅 20:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468245">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/826bbca047.mp4?token=K516ynEN4ndcgAAYaLt34Sm7AFppz6vNzD-Mbwzc9L7XlQsMBSXsTzP2Xdg0yCXW8ROas4zw3eo5qioaROIFrcBqeUz9Azd7fVrQiInmdoBiFUNJnNNtpCohSwoO7QsMpDrohs04Mg54d54P6xY0fuypZ4rJuzComl1Y49mh94gSnN-qKj5dQxAvvi3VctLjAU5Ix0nApV5WOGcW9mgrC1lGrOKcF797FNi9KDuzEoo8eD_r103LsD5FlBn45j3xxJImDGxPXoPBrU0K16QZWNe_oA886Azh72tMm9EcP23uXTpR6cr0tVevxV6AfPC_FeOa3Oq_W5wO2-5kWqYjiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/826bbca047.mp4?token=K516ynEN4ndcgAAYaLt34Sm7AFppz6vNzD-Mbwzc9L7XlQsMBSXsTzP2Xdg0yCXW8ROas4zw3eo5qioaROIFrcBqeUz9Azd7fVrQiInmdoBiFUNJnNNtpCohSwoO7QsMpDrohs04Mg54d54P6xY0fuypZ4rJuzComl1Y49mh94gSnN-qKj5dQxAvvi3VctLjAU5Ix0nApV5WOGcW9mgrC1lGrOKcF797FNi9KDuzEoo8eD_r103LsD5FlBn45j3xxJImDGxPXoPBrU0K16QZWNe_oA886Azh72tMm9EcP23uXTpR6cr0tVevxV6AfPC_FeOa3Oq_W5wO2-5kWqYjiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرمانده نیروی دریایی سپاه: نقاط ضعف تاکتیکی‌مان را تبدیل به نقاط قوت کرده‌ایم
🔹
اگر آمریکایی‌ها می‌خواهند ببینند تنگۀ هرمز باز است یا بسته وارد میدان شوند تا ببینند چه کسی آن را کنترل می‌کند. @Farsna</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/468245" target="_blank">📅 20:54 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468244">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">رئیس شورای‌عالی سیاسی یمن: پایان محاصرۀ ۱۲ ساله هدف ما از جنگ با عربستان است
🔹
المشاط: هدف نبرد امروز، پایان‌دادن به تجاوز و محاصرۀ سعودی است که از ۱۲ سال پیش آغاز شده تا به نقطۀ بازگرداندن ثروت‌های ملی و بیرون‌راندن تمام متجاوزان از سرزمین‌مان برسیم.
🔹
خطاب…</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farsna/468244" target="_blank">📅 20:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468243">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06655cbfbf.mp4?token=EDKs-W4jWkqO9bVqiDkFgMM2pUFxxglGXlAkWBZ-CIPci8kWFGcSQEwsh4i3SRksEOD9jt2z2x67RzoTg8jDW95zmPtLJItpycHlzErVFbEx_-67lTNIuF9UbJ8WtBjOxSIy5ww7x4PXLwoyPJBwkx0ld1o2nHZjBt0uzx-IjisTYYA1gjLGDRJRwxZlJ1F7v5N6tIBUOGwgozHGdnXqsTOIt6B3N5wrZz4BTN2Br2vD6XXGOEfgYd96j2kol3FRZKFKQkUu60QWd27hwNdcK5VURATpO5Udt-Dj5PR8EKYcASlZ45VK-HNcPY3SCmGUVkfplJEQeFw08siax3lfXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06655cbfbf.mp4?token=EDKs-W4jWkqO9bVqiDkFgMM2pUFxxglGXlAkWBZ-CIPci8kWFGcSQEwsh4i3SRksEOD9jt2z2x67RzoTg8jDW95zmPtLJItpycHlzErVFbEx_-67lTNIuF9UbJ8WtBjOxSIy5ww7x4PXLwoyPJBwkx0ld1o2nHZjBt0uzx-IjisTYYA1gjLGDRJRwxZlJ1F7v5N6tIBUOGwgozHGdnXqsTOIt6B3N5wrZz4BTN2Br2vD6XXGOEfgYd96j2kol3FRZKFKQkUu60QWd27hwNdcK5VURATpO5Udt-Dj5PR8EKYcASlZ45VK-HNcPY3SCmGUVkfplJEQeFw08siax3lfXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرمانده نیروی دریایی سپاه: نقاط ضعف تاکتیکی‌مان را تبدیل به نقاط قوت کرده‌ایم
🔹
اگر آمریکایی‌ها می‌خواهند ببینند تنگۀ هرمز باز است یا بسته وارد میدان شوند تا ببینند چه کسی آن را کنترل می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/farsna/468243" target="_blank">📅 20:49 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468242">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3928d27be5.mp4?token=TO6umVw0x9eZF8LUTiiVEYMFB1aGOwxXK7RIrXLqYw0KPgJA7oTmAwuQQsOvXeOrxsj624D-0d0Cp_a9TRQ8aIye4KPp02YG4gK1-24YXSFbUqKCs8pW1rbT1i0l6_GKDFndQc6IIacAxd54ujJIVbnWz62qNF0_Cy7MdzE3UyN9qywF6TEfxX8BxG45LmSqUrmiObLwki8zBiAnOPJr12hryBURk10-FwvcKuk_QiJuOgZFRtNBVZQ6ASkRI5Mwlp3hEfkieQHzf8I-oOZ4r9XXwda1un--V_MeZLOIgXmnOB3UqrZ-gxOoqMZ3IBe6QvnqXS1bvAn1_7e8fWA3HzOGfZw5V3VcMVs77i9C__Cj-pzwX0HuVXDyUPXhJMe788CF74VuDBtcCYMGwIqZTvnBRO3i58KN784FNAKXuI5DM4Dti_vLf0Ao85kKEmc6VGGvXvsbGTwTRc0Ervv6nh4xiOwDYhOfQ1THdvEvfZk2B7jPT7LP0lg3WGZtdalJC6cJSMkbc0asvZfo3QOkDXy3O0CwAXg37NborpQC8apH78fBETzblznqREgKN02IpxFPl633MXSQtG0A-I4s_5oDACjS6Cm5MmaQBOTTk8ddfVQHU9kcLiTsBepptnWQLpeyPY3F6fpj2dgNvrEqKr6IcRsxxBLfNMmwDZGc_uE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3928d27be5.mp4?token=TO6umVw0x9eZF8LUTiiVEYMFB1aGOwxXK7RIrXLqYw0KPgJA7oTmAwuQQsOvXeOrxsj624D-0d0Cp_a9TRQ8aIye4KPp02YG4gK1-24YXSFbUqKCs8pW1rbT1i0l6_GKDFndQc6IIacAxd54ujJIVbnWz62qNF0_Cy7MdzE3UyN9qywF6TEfxX8BxG45LmSqUrmiObLwki8zBiAnOPJr12hryBURk10-FwvcKuk_QiJuOgZFRtNBVZQ6ASkRI5Mwlp3hEfkieQHzf8I-oOZ4r9XXwda1un--V_MeZLOIgXmnOB3UqrZ-gxOoqMZ3IBe6QvnqXS1bvAn1_7e8fWA3HzOGfZw5V3VcMVs77i9C__Cj-pzwX0HuVXDyUPXhJMe788CF74VuDBtcCYMGwIqZTvnBRO3i58KN784FNAKXuI5DM4Dti_vLf0Ao85kKEmc6VGGvXvsbGTwTRc0Ervv6nh4xiOwDYhOfQ1THdvEvfZk2B7jPT7LP0lg3WGZtdalJC6cJSMkbc0asvZfo3QOkDXy3O0CwAXg37NborpQC8apH78fBETzblznqREgKN02IpxFPl633MXSQtG0A-I4s_5oDACjS6Cm5MmaQBOTTk8ddfVQHU9kcLiTsBepptnWQLpeyPY3F6fpj2dgNvrEqKr6IcRsxxBLfNMmwDZGc_uE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عروسیِ متفاوتی که قصه‌اش از پشت دیوار دانشگاه کلید خورد
@Farsna</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/farsna/468242" target="_blank">📅 20:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468240">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">دولت روش جدید شناخت پردرآمدها را تصویب کرد
🔹
هیئت وزیران در مصوبه‌ای با عنوان «شیوه‌نامه شناسایی و گروه‌بندی اقتصادی خانوارها»، سازوکار شناسایی وضعیت اقتصادی خانوارهای ایرانی را تعیین کرد.
🔹
براساس این مصوبه اطلاعاتی مانند درآمد، املاک، خودرو، دارایی‌های بورسی، تسهیلات بانکی، مصرف انرژی و وضعیت اقامت افراد در خارج از کشور، برای گروه‌بندی اقتصادی خانوارها مورد استفاده قرار می‌گیرد.
🔹
طبق این مصوبه خانوارهای کشور براساس مجموع درآمدها و مشخصات اقتصادی و اجتماعی، در ۳ گروه اقتصادی بالا، متوسط و پایین قرار بگیرند.
🖼
اما افراد چگونه می‌توانند به اطلاعات اقتصادی خود اعتراض کنند؟
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/468240" target="_blank">📅 20:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468239">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YSn8xa4EC57f76OqjykQE4L-W64nmPmBzJVo144IqLQdMVu1OO5zpAN6UshqyZEqfw9eFxIDyl3808plB_KQJ81zOCnsk7Auqe1F4AOnQhDzf0GKFDGUvxu101pIeyDGX_HvImIKqRKz7jdVYityVC9noZAzyNaxehCGuug2chviXtfK5V-ewNIo6kGcKpitror9LOHny7Y6WMhqn0xguJjlNS3pKriHt21Aerem4yZ3M43C9DJVjh0DkC91017JWnpW3icmJxgqAoQTvrGXX2Fp7Ru5V9Zcx3TAnyM8V8Y0S_e4d6Y6nWRTHOGRH8wkgTqxTEz8NmlROr7uV3PqDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس شورای‌عالی سیاسی یمن: پایان محاصرۀ ۱۲ ساله هدف ما از جنگ با عربستان است
🔹
المشاط: هدف نبرد امروز، پایان‌دادن به تجاوز و محاصرۀ سعودی است که از ۱۲ سال پیش آغاز شده تا به نقطۀ بازگرداندن ثروت‌های ملی و بیرون‌راندن تمام متجاوزان از سرزمین‌مان برسیم.
🔹
خطاب به عربستان می‌گویم: عاقل کشوری است که در تجاوز به یمن دخیل بوده، اما قبل از اینکه خیلی دیر شود، از جنگ خارج شده است.
@Farsna</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/farsna/468239" target="_blank">📅 20:44 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468238">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca2114dbac.mp4?token=klLEo3lcQxkIzyzksVxh0VgXMMo8wr_eRkbAECwXr5HJaceaU-yCJ-FNx90OlX54Rf9RmvNNqo9j30rivhUBw7VtL_h4gLVo1QTLMSIqVJeLL1hKgop7YoZAP_LZCy-bf75I6N3VFJ4qKC4sLo32Osnd5Y7AENaMAwMeZ3hgofjaS881g11PDdi9fVzhJ0FD1k-oXkgMM6sJ0wztfHwgHvWCfvdrvtv9aC1O11JZ--4pLt-Y1qZadwErr_d3vuU5arzexBhgPbmzl59aC9SVHPfRzltW4OY9pUk6grrP2wiR52CunceEu5PhxtMPH9vnsd_4oPDh82U0RIQJuADV3J1BkIQzvjz_4-bEhaSiLSJMhO2qD_YEGM3d0hgRLQff9QM4PlXxF4pPz9vGzjgWsNdY-8oYNaf4oH2xTcFnvbiQ79kwMAC7d91NveHxF3LN0DlNYkKw0XBP2Icn4aCWxYsyo7mgcGv3cPmDpNZ4V3dykCr7pumoFYohMt4jCZVDXv3h3n2Fnb1m7YTCDDypm4FkKvJBilYO5cb8P4YUm2wDlgG_0zN45qa1L_BVvVL-uXW35MvW3wBr7jZw8GvikWG5SE8gcA6FidmWhFUN17L6c8jIpv7BGifpqh0KlKF48KYtMf-dnuI0ObeiPzllIiVLW91ZpHn3mSogjQUOSTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca2114dbac.mp4?token=klLEo3lcQxkIzyzksVxh0VgXMMo8wr_eRkbAECwXr5HJaceaU-yCJ-FNx90OlX54Rf9RmvNNqo9j30rivhUBw7VtL_h4gLVo1QTLMSIqVJeLL1hKgop7YoZAP_LZCy-bf75I6N3VFJ4qKC4sLo32Osnd5Y7AENaMAwMeZ3hgofjaS881g11PDdi9fVzhJ0FD1k-oXkgMM6sJ0wztfHwgHvWCfvdrvtv9aC1O11JZ--4pLt-Y1qZadwErr_d3vuU5arzexBhgPbmzl59aC9SVHPfRzltW4OY9pUk6grrP2wiR52CunceEu5PhxtMPH9vnsd_4oPDh82U0RIQJuADV3J1BkIQzvjz_4-bEhaSiLSJMhO2qD_YEGM3d0hgRLQff9QM4PlXxF4pPz9vGzjgWsNdY-8oYNaf4oH2xTcFnvbiQ79kwMAC7d91NveHxF3LN0DlNYkKw0XBP2Icn4aCWxYsyo7mgcGv3cPmDpNZ4V3dykCr7pumoFYohMt4jCZVDXv3h3n2Fnb1m7YTCDDypm4FkKvJBilYO5cb8P4YUm2wDlgG_0zN45qa1L_BVvVL-uXW35MvW3wBr7jZw8GvikWG5SE8gcA6FidmWhFUN17L6c8jIpv7BGifpqh0KlKF48KYtMf-dnuI0ObeiPzllIiVLW91ZpHn3mSogjQUOSTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم ایران با حضور و ایستادگی، روح مقاومت را زنده نگه داشتند
@Farsna</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/farsna/468238" target="_blank">📅 20:40 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468237">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a5CvDGzXGwcWwYb3VIlnzyAllkwDSaWXj-jPVg_Knb5fuSZkFswAKUGloi6_MJETWGNdLVHAHKqJWotpGlWbdz3zEky8uWMF6s2FQeG_xUPVSQIsMIZH9hwxTZBpxjSCXAYGGvLDMLT5BRhnY8JMWYrTr1rhhTQFD14iNJ86dQN4cus9KNe8jk4oB93bbWsrUsr8kIacybf5xI-rmr_P75ArcCbSc5YfubB0f_0W32eHgn2dGP347kdfWP-Ei3sGXp1GO337fkR-TwFN7MgBqfdGG_ANiQXh2G9oKqAyXFLdwrz3ApvKNa0yWPZ1Zik2v91Q0buM2B-Yg9e_EFcGjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشک دختران دانش‌آموز باکویی دیده شد
🔹
کاربران شبکه‌های اجتماعی در واکنش به گزارش‌ها دربارهٔ جلوگیری از حضور دختران محجبه در کلاس‌های درس در جمهوری آذربایجان، سیاست‌های آموزشی این کشور را به باد انتقاد گرفتند و گفتند: آزادی و حقوق زنان مسلمان با این قانون زیر…</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/468237" target="_blank">📅 20:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468236">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fn4u6Be2OSLApoIrIquuaB-so1eD98tSYA89FMPBBXyENWUgRzMimwVB7gdQutIWFpUs48Eo2Rjfr2MZgT_HLvl_mwQ992y_9aWnEac0ZRTYoJsVuITZBQD6YdUOZ7gJA1XUq-gyCXHBTp6QZpKKMoI3NP7WQWqjE5RTHZCgNcF1iHck3zEIKJ8sjX4Wrdfvk12KR77ifmVqZuDeFcwL-xBKJQg2SrZHnMENLB_qagOZxrtnvy17JwdntfVs_u2grvL03DgDXGy7FFNJDCaDVXgoEIjKi_rbhxtmxRsvEqEWhraU5KCZtyK1H_9t9RZZ9g1AUDIQ-tUMIFhSyLx9uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
توییت فرمانده نیروی زمینی سپاه خطاب به دشمن: ما منتظریم!
@Farsna</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/468236" target="_blank">📅 20:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468235">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a524a3bf0.mp4?token=PjKiC6i83p9IOWHrorMiidRMMz3NgpBAQOSGvXHAPuMPLUg6eYcEDW9DAHLEyGdIYInzvhN558gp_qH5qytkpfTyFN9v7oS8YEPCHj7rYFW9RJx1HaC7dXmgWNJr8Ew4QiQMi1XejuOtXHQIS_S8iTkYpALTEgeDyyjhKk6RZCkkmiqhu_LOo5Hs8sza25K4E2wxZ9CSduFs1KVbhGvQyzolR5b4H8FMOIaHXFFiujxeuvmpEm1NZVdeUBB52hG2o_TzQXALpg9AXGtq0CFN-Uy9qC-f1OxKxIdJfhRSbsKkLPOPJecVuZZ7Hu4IaRlii2Jatxi8WEvSBQLBeFC9mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a524a3bf0.mp4?token=PjKiC6i83p9IOWHrorMiidRMMz3NgpBAQOSGvXHAPuMPLUg6eYcEDW9DAHLEyGdIYInzvhN558gp_qH5qytkpfTyFN9v7oS8YEPCHj7rYFW9RJx1HaC7dXmgWNJr8Ew4QiQMi1XejuOtXHQIS_S8iTkYpALTEgeDyyjhKk6RZCkkmiqhu_LOo5Hs8sza25K4E2wxZ9CSduFs1KVbhGvQyzolR5b4H8FMOIaHXFFiujxeuvmpEm1NZVdeUBB52hG2o_TzQXALpg9AXGtq0CFN-Uy9qC-f1OxKxIdJfhRSbsKkLPOPJecVuZZ7Hu4IaRlii2Jatxi8WEvSBQLBeFC9mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار نقدی: سفرای برخی کشورهای خلیج‌فارس از ما برای حمله به پایگاه‌های آمریکا در منطقه تشکر می‌کنند.  @Farsna</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/farsna/468235" target="_blank">📅 20:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468234">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNgObpl57mVSyhcahJWuNjz4lUq3B7aPJrbBxxsXDwr22fi7aWDewLY4mBcxSrH1Lx49dxTHTk5AzvBJPOenmZUxkRyxZx5fSbsW6dZIyo_gcyC1LzFxZQmStAqQPFFtGdbdIKyTO_e85_ZIcl8JLFsRpdxHP6aIRfBstFVFXLJmPiLcxmNTDICNtqtRcfkMrBxnfGv0GA1OartUfmBaEnLBiX5yr4s1W8JpCXBER-gjOzzuUTWNX0oFllCmYQExN4FlleeKvYX4RIUDJJWlLTGHCBLOVcrXwO3ti8gB3huLJPuYwG2L5URlRK985ypsIGsmPehZXJe54a5wPY9CVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقاومت ترامپ در برابر پذیرش واقعیت
🔹
ترامپ که در تلاش است تاثیر بسته‌بودن تنگۀ هرمز بر گرانی بنزین در آمریکا را انکار کند، این‌بار مدعی شد حملات اوکراین به پالایشگاه‌های روسیه عامل اصلی گرانی بنزین آمریکایی‌هاست.
🔹
این فرافکنی درحالی است که کارشناسان اقتصادی…</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/468234" target="_blank">📅 20:10 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468233">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">آیت‌الله قربانی امام‌جمعهٔ پیشین رشت درگذشت
🔹
آیت‌الله زین‌العابدین قربانی، امام‌جمعهٔ سابق رشت و نمایندهٔ سابق استان گیلان در مجلس خبرگان رهبری بامداد امروز پس‌از سال‌ها فعالیت در عرصه‌های دینی، فرهنگی، علمی و سیاسی در ۹۳ سالگی دار فانی را وداع گفت.  عکس:…</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/468233" target="_blank">📅 20:08 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468232">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9422bdb92.mp4?token=SaurHBTLrePSmllsrljKnnw2Ub10X6QKTQaB8g2B5yrvPmVoWAdvmGRC8cj6XP9yVmH3C0NGj2bAa3cYdyLf5LKk3SU9EGokwE_eHDKoc5jOz_u9F9PscZDxH0ewLYHttAHqw8w990vY0nuhqRK-HakzmzM0uzvVB5S1UTxazrXLqakAQXQJI8Q0xSFe79A9FMGXjTn2WH-UGFK2_hIZIrCsGGw7Ku__8wCDAP00jtmRc4a2i8Ceh-BdLuqlalpaIm4I_px7kFN7HHDvXZXH7WAuqsInFYlWdTCXSG59cLmpJH8MiO3dCOMqdvGAKOcr85QKBGko-1hhCAdgbU8hFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9422bdb92.mp4?token=SaurHBTLrePSmllsrljKnnw2Ub10X6QKTQaB8g2B5yrvPmVoWAdvmGRC8cj6XP9yVmH3C0NGj2bAa3cYdyLf5LKk3SU9EGokwE_eHDKoc5jOz_u9F9PscZDxH0ewLYHttAHqw8w990vY0nuhqRK-HakzmzM0uzvVB5S1UTxazrXLqakAQXQJI8Q0xSFe79A9FMGXjTn2WH-UGFK2_hIZIrCsGGw7Ku__8wCDAP00jtmRc4a2i8Ceh-BdLuqlalpaIm4I_px7kFN7HHDvXZXH7WAuqsInFYlWdTCXSG59cLmpJH8MiO3dCOMqdvGAKOcr85QKBGko-1hhCAdgbU8hFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار نقدی: هلال‌احمر اردن به ما خبر داد که ۲۰۰ آمریکایی در حملۀ ما به اردن کشته شده‌‌اند
🔹
هتل‌های محل اقامت سربازان آمریکایی در کویت و بحرین را که هدف قرار دادیم از سر شب تا صبح آمبولانس به آنجا تردد می‌کرد. @Farsna</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/468232" target="_blank">📅 20:06 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468231">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6afd1c67fb.mp4?token=o6RHB-i_s1cT_ZM2h8KLKnaziPcGpZLT7vaAvZC4OAHALDMZnIWB50jBLKxZe8nzsYi-dJtgIhQA1-jXqKiKf9rED_W6wN_1oppmVk5OjLbzIplD3tjeGE5QqG7LuhkT3uy5fY506wri4bqAUgG22JDgim3c73Iet8FP7zs0kklNUHAvRm3jPLQlCmsrNYFUqFqlgaG4gNnInE2aVj9Q6aZxTjFnz0X6GoUFrbD96kwsQ_iYX1EthxzH2w2Z7oxPf99MTIfsb2vUN4r6c24OPrWW3M_xjTigqioUkFp3ox__H7r58XDkGId1ffgCKVsIMLA3XuvB9TwhMJ9GhnGcgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6afd1c67fb.mp4?token=o6RHB-i_s1cT_ZM2h8KLKnaziPcGpZLT7vaAvZC4OAHALDMZnIWB50jBLKxZe8nzsYi-dJtgIhQA1-jXqKiKf9rED_W6wN_1oppmVk5OjLbzIplD3tjeGE5QqG7LuhkT3uy5fY506wri4bqAUgG22JDgim3c73Iet8FP7zs0kklNUHAvRm3jPLQlCmsrNYFUqFqlgaG4gNnInE2aVj9Q6aZxTjFnz0X6GoUFrbD96kwsQ_iYX1EthxzH2w2Z7oxPf99MTIfsb2vUN4r6c24OPrWW3M_xjTigqioUkFp3ox__H7r58XDkGId1ffgCKVsIMLA3XuvB9TwhMJ9GhnGcgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار نقدی: هلال‌احمر اردن به ما خبر داد که ۲۰۰ آمریکایی در حملۀ ما به اردن کشته شده‌‌اند
🔹
هتل‌های محل اقامت سربازان آمریکایی در کویت و بحرین را که هدف قرار دادیم از سر شب تا صبح آمبولانس به آنجا تردد می‌کرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/farsna/468231" target="_blank">📅 20:01 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468230">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3b87dba00.mp4?token=YkrkHMKp-Qe-EMAXX4AAJ3Y-mxOqpErUPxwGO73uS6-5Hx0gXcYirTcdUPVNWurXGyS3RGcqrW_uzsWxIe-20_ObI05xFZjctUkO7w80tSpkvAsmGihcRzTofURHYwFJB4DFryibu_siU2YAGBF0_xtxABtZsqrmKyeDSMaRPi-H7LVBaFQ4NAaIxP_rt7_NlJwQxxuayO-znzAcOLthYX00T5OZ5xBNkbdGttduH5XFAANT8-2FQOYMyCxiNUnJWeyb0jwd4R9c_SGRGTaWG3alPnm9pUiutxNfMZ3EISts3MsnhJ_knqfiHm-th9fu5lL2pRKq0oNp5l5ls_tzHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3b87dba00.mp4?token=YkrkHMKp-Qe-EMAXX4AAJ3Y-mxOqpErUPxwGO73uS6-5Hx0gXcYirTcdUPVNWurXGyS3RGcqrW_uzsWxIe-20_ObI05xFZjctUkO7w80tSpkvAsmGihcRzTofURHYwFJB4DFryibu_siU2YAGBF0_xtxABtZsqrmKyeDSMaRPi-H7LVBaFQ4NAaIxP_rt7_NlJwQxxuayO-znzAcOLthYX00T5OZ5xBNkbdGttduH5XFAANT8-2FQOYMyCxiNUnJWeyb0jwd4R9c_SGRGTaWG3alPnm9pUiutxNfMZ3EISts3MsnhJ_knqfiHm-th9fu5lL2pRKq0oNp5l5ls_tzHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روسیه هم مانند ایران گرفتار تحریم و جنگ است اما ...
🔹
روسیه باوجود تحریم و درگیری در جنگ زیرساختی، ارزش پول خود را حفظ کرده و تورمی تک‌رقمی و به مراتب کم‌تر از ایران دارد.
@Farsna</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/468230" target="_blank">📅 19:57 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468229">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6504906783.mp4?token=D7K-dOZjjdY9LV5-uS6P9ou458fJ5I9V6bzIUdz0TZb_83UwHntAOysw-0dfS9cmNFYrjLcezaK3pYOJA2vYyUf8x_hXDWK9FOkn5vlR7FKW_blhiIIl6pnNCK-OBqBNjHNENUdm75w45PBT6T8jMFEjsWj_gZQMKSg8Y07XN8QXvwuZogobsTw0kHv3g0uptlnJUBn-tPnTW0gg-fnt6ndYRM_opxrlNjM_Ymyo8-_kbo9qz_yYJKe1ZMRJd-M6_DpqHOkJj-j6ydSheZwLqsK32kMIMZU7QUwC6y_KskATUiXJh8JoWkjLzOkXdsi94WgY6KMKSsuyKb2Exu0g5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6504906783.mp4?token=D7K-dOZjjdY9LV5-uS6P9ou458fJ5I9V6bzIUdz0TZb_83UwHntAOysw-0dfS9cmNFYrjLcezaK3pYOJA2vYyUf8x_hXDWK9FOkn5vlR7FKW_blhiIIl6pnNCK-OBqBNjHNENUdm75w45PBT6T8jMFEjsWj_gZQMKSg8Y07XN8QXvwuZogobsTw0kHv3g0uptlnJUBn-tPnTW0gg-fnt6ndYRM_opxrlNjM_Ymyo8-_kbo9qz_yYJKe1ZMRJd-M6_DpqHOkJj-j6ydSheZwLqsK32kMIMZU7QUwC6y_KskATUiXJh8JoWkjLzOkXdsi94WgY6KMKSsuyKb2Exu0g5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: ممکن است از ترکیه بخواهم در پاسخ به اقدامات یمن مشارکت داشته باشد.  @Farsna</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/468229" target="_blank">📅 19:51 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468228">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TCsh1GJeiMAAxywQCYGRSm_8I42RhaU8QxWLlQx9jVbhu2XbPaGyKqs14MXVf4Y1T_iTz-ZQPpe20Ei_ThI4Sgup7GAt9zrEJoYzwUhGjR8CtiwHG094mXBt0KKP4pW2Jmz7J0I7M88k10YdjQhPRjypkwWKK3lGdiEDARq_4x1e2ws3B_4WcRP5FQpWroGQODy_8lpwvXSZzTmep5sbyFRIYiHhYtnzSKG3DGK67dCnV_iiYzxUrV4QbLFcv9Vwyh1DkACSxCA1f7ILBnqGkyCQ__Rw1KlKRHbkfB03U4P5QuYff8TV2f2m0Y6QWcNZ7LT5RVkjeUrv63pnUo9FQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشک دختران دانش‌آموز باکویی دیده شد
🔹
کاربران شبکه‌های اجتماعی در واکنش به گزارش‌ها دربارهٔ جلوگیری از حضور دختران محجبه در کلاس‌های درس در جمهوری آذربایجان، سیاست‌های آموزشی این کشور را به باد انتقاد گرفتند و گفتند: آزادی و حقوق زنان مسلمان با این قانون زیر…</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/468228" target="_blank">📅 19:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468225">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NOefgmlPTgaDK9LG4BUFaLGL2LvduYBpf8Jy8sE3dYC1ggtMrNbIwFEACAsiHMZJVzIRww6GW7kKoZ1B6f5-UP9Xasj2oCk9wg9x4l-UCcUHgro_09FHGojqMLojFpIWRCloIZRSf5ZWXaNCK2Y4zvApufFnDgrLOCyrDZPfIEe72yYIbzthHrLUb8t6i1JmZQHs92G54pHD5pdibM1GwZSPP_YzXcnM7z7kSAYpEeRDcHEEHI3fbdMZIqIZ1_6MLh9XStwpQB_WoOnNRgGs2uKhVOkz5LU8ji2L9SRm96D4TqmYcOYVNrcuKjhuwnMgs1EzkHI3xn_zNH0ToXE4UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XpqDTc3PK8nxrCjyPBRMlidA76F9WsvA-QMC36FvU_3OJiPaNMKMmSWHhVg5Q1BKBoC3E2G2U-EGLlc8AjWbW_8q2NAo6pVpGsjG2Ybn3Xj7H3qlyjWS6Y-gocxi5lW_EiQslRfeYDbALRYS59sRakLohCZT_BIGB-vC0gqmVHlwoveTn95YIi9oNNUWslCDwyunolmUMMcm5Gv4K1UtvBBZ4fSHPlsBlDVKOEj-G3QdEH3GZWV6jK7STX3Xnro191WgSbg0za-hzgxNj3OHw3jV49fmIW_T8GOsiAWoL8y4r_OCW8JXKumozgoZVHUgKPaxboRJrozQq9VfC9Ugkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ADXFuinxbi_MuLwu9eFHaFSw14FIjAOZ5cuB9_GVny0jyGVundydSpZ9-1-0IEd2872TIMe46Aep1ZnJnZ178aLinItwnjJR7M6PEYZSu_PTrkbsBY9B7U_26gSc7dNiybyp1lB7ftwQvc7KRY8i5kNVaR0tmaF38nP-x2LW5SIrwlNgI_pq4zWL3us4SisXxxEEWUDkvXfMueqACX6veM7NiwsH4pZRncCT5-3BLAAb7nhoEIp7grl9zuKYeiQ23nj_nOQNi35R6VaOcnsjS4zPOcXfX3Wvcmwu2j0l0DYTsfAO0braC1H6-pILsRlxsWUHU3-ye7QdNG-rXxEfAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دیدار اعضای دفتر حفظ‌ونشر آثار رهبر شهید با خانواده شهید سعادت
🔹
در ادامۀ پویش «اول خانواده شهدا»،  رئیس سازمان تبلیغات اسلامی، به همراه اعضای دفتر حفظ‌ونشر آثار رهبر شهید انقلاب و جمعی از اصحاب و اهالی رسانه، با حضور در منزل شهید محمدعلی سعادت، ضمن ادای احترام به مقام والای این شهید، با خانواده معزز ایشان دیدار و گفت‌وگو کردند.
🔹
شهید سعادت از اهالی رسانه بود که دهم اسفندماه ۱۴۰۴، در مسیر بازگشت از تجمعات مردمی در تهران، بر اثر حمله آمریکایی-صهیونیستی به فیض شهادت نائل آمد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/468225" target="_blank">📅 19:37 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468223">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b335b37f5.mp4?token=v5pWVPmOBjEB_WpOvSpycr46_mBqFzIA4qT3rzJNPp2xE91UYCzQWVHKm4NmWHqqOPX_amikPHi0vOANFx6w9W7Pjuli8LeUfKVxuxpzH7BFnMLrT70wv9o4ZI52zunwTFRF71IAKAdEPUp9BCB0TWOhvMWDH-13WKdMe0--6H6rVV2eFeGWTH71SWcc46-_3Kz96-0IdNp71m8PaQFfcy7LrKFRJIf46kTnQxrAXgUE8S_DhRhXxVaE0EZdcEIblWCiC3znPpYs1HoUZRgn2NI-1yauEy0_hIiLOIC2FiCKIa6dG5oA70bDb0ML39XtlMPfaax6bykfBOerhL4W0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b335b37f5.mp4?token=v5pWVPmOBjEB_WpOvSpycr46_mBqFzIA4qT3rzJNPp2xE91UYCzQWVHKm4NmWHqqOPX_amikPHi0vOANFx6w9W7Pjuli8LeUfKVxuxpzH7BFnMLrT70wv9o4ZI52zunwTFRF71IAKAdEPUp9BCB0TWOhvMWDH-13WKdMe0--6H6rVV2eFeGWTH71SWcc46-_3Kz96-0IdNp71m8PaQFfcy7LrKFRJIf46kTnQxrAXgUE8S_DhRhXxVaE0EZdcEIblWCiC3znPpYs1HoUZRgn2NI-1yauEy0_hIiLOIC2FiCKIa6dG5oA70bDb0ML39XtlMPfaax6bykfBOerhL4W0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون سازمان توسعهٔ تجارت: ۴۰ درصد از افت صادرات دریایی را جبران کردیم
🔹
در سال ۱۴۰۴ واردات ۴۲ و صادرات ۱۵۵ میلیون تن بود که ۷۵ درصد صادرات از خلیج فارس و دریای عمان انجام شد.
🔹
پس از محاصرهٔ دریایی، انتظار کاهش ۷۵ درصدی می‌رفت، اما آمار ۶ ماهه کاهش ۳۵ درصدی را نشان می‌دهد و ۴۰ درصد از حجم دریایی جبران شد.
🔹
پیش‌بینی می‌شود در نیمهٔ دوم سال با اصلاح رویه‌ها، صادرات افزایش یابد.
@Farsna</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/farsna/468223" target="_blank">📅 19:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468222">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79c7998c96.mp4?token=bbXH_Mon-ALWEZJnic8OTmOYe0ijyMJMUrppfz19wL-QQU3BA4JqYoo9uj9RuKzuUWOjbBR9CzIn0a_ymmdwjQiTqfUfrrQ7zlCeFlSMKpSgnouDjn3SIBJtrJhlzgP8sQVM7PJRshlHx3fcDLg4qfT1gYM-Nzx2Vviaq1PeaM8l3HZ_zg5DBNGOOX9jv-Xu10lmyhVhfEiQlJ95QJt3k0HpyZ2PUe-lecYLwQzLys4vPAPbUFmC5QKBd1EmA4TAsIlwvti_TEemy1vHGynIyzEMssqGllVqj6B0V7gmkgbRvBT8WZOfqmMB7Y565YrLajGRp8pKITUv6hMaS18YjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79c7998c96.mp4?token=bbXH_Mon-ALWEZJnic8OTmOYe0ijyMJMUrppfz19wL-QQU3BA4JqYoo9uj9RuKzuUWOjbBR9CzIn0a_ymmdwjQiTqfUfrrQ7zlCeFlSMKpSgnouDjn3SIBJtrJhlzgP8sQVM7PJRshlHx3fcDLg4qfT1gYM-Nzx2Vviaq1PeaM8l3HZ_zg5DBNGOOX9jv-Xu10lmyhVhfEiQlJ95QJt3k0HpyZ2PUe-lecYLwQzLys4vPAPbUFmC5QKBd1EmA4TAsIlwvti_TEemy1vHGynIyzEMssqGllVqj6B0V7gmkgbRvBT8WZOfqmMB7Y565YrLajGRp8pKITUv6hMaS18YjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هشدار سناتور آمریکایی به ترامپ دربارهٔ ورود به جنگ علیه یمن
🔹
کریس مورفی سناتور دموکرات آمریکا پس از سفر به قطر و عربستان، با انتقاد از نحوهٔ مدیریت ترامپ در جنگ علیه ایران تاکید کرد ورود واشنگتن به جنگ با یمن، شرایط منطقه را خطرناک‌تر خواهد کرد.
🔹
او گفت…</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/468222" target="_blank">📅 19:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468221">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jU1WvMbOz-REdFOyVE1ZLW_yC8xJRFIMIQEyjxDkqapHOQvwMdszFWeFY3Xuz6sDnXVM5GpSmv7LNxed7Ode3CKCLi3FQKM_zI_NKpvVHUM4Q5egiDxGjBB0hAfMlRcl6wxgnQoWjcdgVgGY44509hzj3DrwbwThlpXLL_brSYmb-YSfz60rdPKV-z9TusrXkHrk_4_nFX9OAFKzQfwzvXCzTTNn1KdhVpehxGkOeYkn2douvkhCDhPvBZt8ZNRdbtvpMxB5WvcU3mBoC69GqPPL2HbSFjYIettepLhQMcMcwjORy3EkhyHnUZTXwprGI5b0VBi1qPTjiX9QwoCmog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتراف شقایق نوروزی: کمی دیگر مانده تا رضا پهلوی گوی سبقت را از منفورترین مزدوران تاریخ برباید
🔹
«باید اعتراف کنم که ما تو را دست‌کم گرفتیم، قیافه احمقت را نگاه کردیم و با خود گفتیم این مگر چقدر می‌تواند در مزدوری از بالانس زدن در یوگا بهتر باشد؟» این بخشی از اظهارات تازه شقایق نوروزی، فعال ‌رسانه‌ای و بازیگر خارج‌نشین دربارۀ رضا پهلوی است.
🔹
او که این اظهارات را در واکنش به ناراحتی رضا پهلوی در قبال آسیب دیدن یک فرودگاه در عربستان بر زبان می‌راند، تصریح کرده که پهلوی‌چی‌ها تبلیغات‌چیِ هدف قرار گرفتن بیش از ۹۰ زیرساخت حیاتی کشور در جنگ اخیر بودند و فقط کمی دیگر مانده است که رضا پهلوی گوی سبقت را از منفورترین مزدوران تاریخ برباید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/farsna/468221" target="_blank">📅 19:09 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468220">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a947198ba.mp4?token=kvw3Dc_YwB_UpzsN5en74Ye6RqZYXyhp-5_ezd4atWYh-S9Ibz5aZzDqcS4FTOyjsJhi6BdcBgdKLzbBOPAs-PMlIPiT75AKrxZccFMW91IYUXjCq32fvLWhjQAMBfGWeondVotS0Jzd0iZKQyNCHvBQE5RJZmpp0OS7BrYA5DNaEeUtFkmiK5kkwKAvqD3t2AY0FlE2TNHDTkr0cB1t-TcibHRswpVoqP3AHDPl7o2XnH_GCKIkLmqFi-QqjKgPqDPmLbcMcGOo4Y3NfIDT0GQopeiA2BdhJEp-GUdz6FjLAG8F3dHFa-jAJDtbakwft1wvnUMwAb7KT37jCQ8N6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a947198ba.mp4?token=kvw3Dc_YwB_UpzsN5en74Ye6RqZYXyhp-5_ezd4atWYh-S9Ibz5aZzDqcS4FTOyjsJhi6BdcBgdKLzbBOPAs-PMlIPiT75AKrxZccFMW91IYUXjCq32fvLWhjQAMBfGWeondVotS0Jzd0iZKQyNCHvBQE5RJZmpp0OS7BrYA5DNaEeUtFkmiK5kkwKAvqD3t2AY0FlE2TNHDTkr0cB1t-TcibHRswpVoqP3AHDPl7o2XnH_GCKIkLmqFi-QqjKgPqDPmLbcMcGOo4Y3NfIDT0GQopeiA2BdhJEp-GUdz6FjLAG8F3dHFa-jAJDtbakwft1wvnUMwAb7KT37jCQ8N6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترفند صهیونیست‌ها برای ایجاد بدبینی نسبت به مسئولان
@Farsna</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/468220" target="_blank">📅 19:05 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468219">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MS81_RFuu8jBMLWeXKiI-dTRxrucHZfe4_Szr4fh05ZjyDOWAf5Pbe_ySG3ktD_UcPnKvoR-RVELpR09NM8AsPJxY0o8l19s-s8R4MsC147zMeLFjtlISkdh2YSE5HoGgoN27NKkyFmkR74X8QIZltz9RmYKWmpzDRJKqq1BrUGMCR_06gid81oCGRAHTbdm5q63h1BJE6H1odijKivkLgGgWQw4MKx_CE84JAq6PNMsAGpxCtDZcgsCnwpBfJVxT5-26__vsO0u42_eqwMjgew8RRC5E6D5pBsN_2P6f4l79_lqDwgMc-n9EHzNXTqrV1ZPEUfcaWiaaywQTuh6Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمال برکناری هگزث توسط ترامپ
🔹
«دومینیک میشائیل تریپی» نویسنده و تحلیلگر سیاسی غربی طی پیامی در شبکه اجتماعی ایکس مدعی شد که ترامپ در پی برکناری «پیت هگزث» وزیر جنگ آمریکاست.
🔹
وی در این پیام نوشت: گفته می‌شود که ترامپ در نظر دارد پس از انتخابات میان دوره کنگره، پیت هگزث، وزیر جنگ را بر کنار کند تا با انداختن تقصیر جنگ نامحبوب ایران به گردن او، میراث و شهرت خود به عنوان «رئیس‌جمهوری ضد جنگ» را حفظ کند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/468219" target="_blank">📅 18:52 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468212">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gjh913RTC8_O8a7mCclpKzfyfHtCQ1QFdqhcsZlX6o2_hoOLkDbNU35YRKC-eQBm28Yjf6oglM6b8brFY70KmGNXMUj0W_WFc8Bh4yJ1K5MDe5j-gez0TWfg0HVsNqtfNE49_HsbdLxBz0bgbZB44Hn8FDYZGzWglMb_hsU4pWg--9bIuWksBe7FN1xd1L6jkvYuQ3nyVDupAyc8HAVewYU3WO4km0C6hZX0CL_STAPrR_J5jeAZ_VASks2OpzGTbV9KYSbM9H72ff8I3uiqwav-jf5CuVCA8q7HcsSX5LGAwFsH9dadjm9DMThsjZbJlgDCySpy0ALMSKY_P2e2XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/wBCgsFOq5BP51K6inLMg-68Xqt-DaxPLmrXt9oGraKfmtu3emSoHq_YB82g9CQfh4zBOOuZYhmUx73QpjzGAmV-Qf8GLhmmarJyU8hfoLQBiI4ewwo64Gi51Db20bwnvt9CrOV2Q6TducSoOC6qc_48fjtnpT3FefkozCUy4oMrLVIVztwwn-PvDZ5swkXj2WUI09GbzJ6UlsKU0FM873nbGsEQbnZG9M5B4pROnZINCo3tczmuGxjLZQxA09D6sg0OlYGSkh8D1TRDEkWVoAf7HqCoR5TVaN4YwH7cQnI8h8bE8UpR-hppcUt0XfkWoKkDil-loh3ElwNG4h7Ebnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qrCnV24zVmpSIXGjU6bMt1E3sE3DJUJyVIYBwLAwDBZa4ExuKJGvQaJTFlImC9YqMgbL-TOJKhZNxzilXpR5roaNj1Txsb8mqDojp2jt2fFpv57qv49yU7tbp0yWtWwlmpzQ3nRuBmDplfyhBu3pDDpJtYSJg2XZv0tFdiMiItVm5A3x33U0Ei-0zDecvFoVk27u-oObjKlU6pir8QVNrnuJxBGJd6B2hkmcj6DLF8f4HWOjwD-ItHAYfjsTq6GZ_4FbgUNUc_jTW4f2HcLS6dM6n4XRiUMrMjbQYkezcFhhrQBaaWzBffdbd8AzY99P5IopNn5q8OIRPDi2nuy_8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XmQhbk3tPR_xmSwho-PIjbcti9uyF9NFEPTn0AUeUnEfiB5fnjW74HxStXYiMXIYxhcKtopfIyAWpb0JJ-Ke2fNwlLU1kgJm6Z2yvnozlCh-viKVAzu3tLcBw5AtJudrs4IWAIBZOzpkbpK_UNPuxF5VjI9NGrqaBrNCq503B7PRPsldZD14yoS3iXNyjcT7wgAIPR_3zHpRCklO8644EESTKUdJtcIXAPEDX9DPdOFwp0k5lZTvAUhg0gtmKHGf-6aYMT2FyQcEy9LE8ITWKorsnDCsdQ_7dc5ngPiEA_Mo81Zu5bM8gKPzP7_Kz7884MmVo3ixm6NZtDP7gRE0MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m3b0iDrVLcpV4KTD7XErBiV1OzjWR0b1m6LQL41ldhc1rc4Im6IqHxZCgew75isIFCkr4Jj2ui93Fl0Mdz7bWyNdn-P2P7jJG-BK_sTrBan3f1ptZ32a4ffNR6uEDuY78khLVvsciccnCQsubbLJneH4VaczGMyRQMDwgFpF8uHDgicqXx_o_3psc39uFgY6-q7rcZeEF7_Be3g2ot-8CPZK4d7vOEvuCccpfp2SHgO3Tc8Xx7P70xacRNDaZ_TV9V4ufHeWBgSgKbuZSqSx_17FXBcf4S30UK3SNKX3sfVBr5pURZep9Hn_jcD-I1lldnjJ8R46amYsweu9t2jNpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/agN-joE6QFT6TTe0mxrKbk3BxdPrgihda0o7I34RKLufPkbLtgD-h8qFUJag7zFNfkExXV7ZUSxfxFFtezP_TMs-CwXkKF6v3wBbHMUATihz2kIS3WOVKY8E3GVx4cl_EKNmKK95ORK4t8kdbl_yJ4xyU2uQVSsWuPqMXRgiamIiEpBoLrtQJyXq1KA9PpyGbJ6nxT56XSgMOQzSKB4XXmqgyORfd12uOmw-jpiIRq7D7PyZlXoFBbaQvVdHmcRrj7hTbo9OyyDifFOZptMKO_96TD6Eah-EaXE38ia3JW8oWv24i4QZPkBISGxDUGKAC-F9FywzMwkIttIRs52QsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q-4JkbtP9q8xz7XjddPtuE479J3mEfl4YrorMCc6ZeYfO9eG9HDTGnhW7iKY2Z5KyJwfuHc8CdwXhS9DeZYzD92zus6fzwVtO2p63cbc8z67rsBcggkvpi4p6Nn-YOUn6HRO5y1jJXIoqsIPoSuFCGkKH0C_SdyfaX3rnWZ3yRbqRbw1xR4ZkK8ZJLSVr1BDyrA0Lu6IXAQkWojbTI9boXIOocZ6tjk3F8S0-GzZtCTBtNxucFBNFO70_qo7BJd-dzY2HIUiebEF39Y8C2n3r6-JN_YEUiK98RTWRi5ifsSRGL_UhH8Fp5LjlWAA8ArJpwL4L2z_ofw-e4hX817XLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
لوبیای لرستان در یک قدمی بازار
🔹
لوبیای قرمز، چیتی، سفید و چشم‌بلبلی از انواع لوبیای لرستان است که برداشت آن از اواخر شهریور آغاز و تا نیمه اول مهر ادامه دارد.
عکس:
نگار ده‌دهی
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/468212" target="_blank">📅 18:41 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468211">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‌
🔴
سخنگوی نیروهای مسلح یمن: شرکت نفتِ منطقه صباحۀ صنعا از فرآورده‌های نفتی خالی است و هدف‌قرار‌دادن آن هیچ ارزش نظامی ندارد. @Farsna</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/468211" target="_blank">📅 18:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468210">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEUht0VVdqCU-ftAV-6xGFvIkJrCW9SIx8hGwk517IPlSJnYNTNd0Gd6gD-jvSEogZs-QNusNoMExCP_LRDKuwI4uy5IAqYg36pjtAs-WHYil3upMgoA7EwfWiY-KdXt-nz5wKYziylu1SkTXVklIXh1QUzOrXbMuXlDKxuuVy-vBkJPqZmpNNDgP3ZpDcz22JIHbDNK0g_o05K0eHY5qd4eZ_FKr5tOULseE9M-kEuKGCG6_4vRJRPGbKF-nVteEtPgCo3qiEeDGTQkSD-4OUJI3aPyp85iW5q-aSFptT-yhEecBgwkEs7_XNdSXHe3YA0xHEcAxo-wNBHYtNDczQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک‌تایمز: آمارهای صادرات نشان می‌دهد دلیل افزایش قیمت گازوئیل و انرژی تا حد زیادی جنگ ترامپ با ایران است
🔹
البته حملات اوکراین به روسیه نیز در این موضوع نقش داشته است. @Farsna</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farsna/468210" target="_blank">📅 18:32 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468209">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5ey28pIntceRPHz6MhdUSdDL58Xf_kvftz0X0tQ6_PCtX6QcYJFQOymRL_jT7zJxEulPa5v5zbOns6yOEh6HecPu_BplPWfG6tcugK5-l6TasysqOSPEJ96JYFq9J7rwV4XXa0LFWIY6geJOg5Dgv6qCSfrjHtPMqRxBPa9pMgi9xDmXg-D0O0e5-kLyFrljFGiyPIn2ZU6j4tAbtKW21w50Y8YkQ3pIu94LzUm3bRqSZs2qqcLLPg0xpFW5OqmtH4rHxkA5jD9QfT5f9WZtxZcU75vENOs-xQxjDsUCZ6YEbbW_Z2w4MfPv1h_jg6SH4ZgYogivAs4Y5EiFhcyiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
صندوق‌های سکه، طلا و نقرۀ بورس امروز یکپارچه قرمزپوش شد
@Farsna</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/farsna/468209" target="_blank">📅 18:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468208">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D969c6KQNy6w4JHAkeTpUcoKsHHANAcJ6FS7nDNYOpNbBJHUdm2ngRg3boH2f8rMrvi_jCLWnEAuQRmm-iSZIARk2ssWvCWDUziq5wqr_wuwgcsa-825-nlmwddH9x5ZPjSYaWEUm03o9k8FTKRAqvoPxc8Y13qXzAy64BmeqTRsFiAfQcC92TTZ1p0PjMeE2dBBItmKoxGY-7SIVegkAMnbiTIChZqQ2pDUBmjcgFg629eWglkZX2oA0A67bRDTyxdB2xZv_imJfsOHdzGgwptUkjTNJwppdw0-1gMM9qD9sQe9U24HkD_677VxsBVuVv-4J1YCGwYYhtjoqTjOXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشک دختران دانش‌آموز باکویی دیده شد
🔹
کاربران شبکه‌های اجتماعی در واکنش به گزارش‌ها دربارهٔ جلوگیری از حضور دختران محجبه در کلاس‌های درس در جمهوری آذربایجان، سیاست‌های آموزشی این کشور را به باد انتقاد گرفتند و گفتند: آزادی و حقوق زنان مسلمان با این قانون زیر…</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/468208" target="_blank">📅 18:20 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468207">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cf4dadc0c.mp4?token=RPeQ23xU11QdCf4vir_lc3L5VTzFpSn57Q6ymKeEzoDDU1q6QMoJlNmVNuu1A4tr2IIWh9Jvp4bh9EJ7rVZkZVWRfEsU3eXeZSg329ko4RyVOexBrOHb2h8FGijU8lTMmRUcZe5AunSGlwZA7PhJbe8luXOaeR6vKeMmyn2JQ6ZZtHFv9HOtJ6ZQxHDH26nNXoLzhaGf9LUUxQsmECbeVEBJCt0YjmpdMkBRMuhwHfHOzhqPFoxKL3r5N4XwJaqirXbQmB6EpUDt4ibAD-59QNVkr74CyraiA1g9Kvi_8MSXbx5g-zIAcB_338vCDVM0GtcOBmkcISB-mfwdhURvZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cf4dadc0c.mp4?token=RPeQ23xU11QdCf4vir_lc3L5VTzFpSn57Q6ymKeEzoDDU1q6QMoJlNmVNuu1A4tr2IIWh9Jvp4bh9EJ7rVZkZVWRfEsU3eXeZSg329ko4RyVOexBrOHb2h8FGijU8lTMmRUcZe5AunSGlwZA7PhJbe8luXOaeR6vKeMmyn2JQ6ZZtHFv9HOtJ6ZQxHDH26nNXoLzhaGf9LUUxQsmECbeVEBJCt0YjmpdMkBRMuhwHfHOzhqPFoxKL3r5N4XwJaqirXbQmB6EpUDt4ibAD-59QNVkr74CyraiA1g9Kvi_8MSXbx5g-zIAcB_338vCDVM0GtcOBmkcISB-mfwdhURvZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تریلی حامل ۱۰۹ قبضه سلاح جنگی در مرز پرویزخان توقیف شد
🔹
دادستان کرمانشاه: در بازرسی از یک تریلی در مرز پرویزخان، ۹۹ سلاح کمری، ۱۰ کلاشینکف، ۱۷۰۰ فشنگ و ۱۹۸ خشاب کمری کشف شد که در بخش‌های مختلف خودرو جاسازی شده بودند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/468207" target="_blank">📅 18:19 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468206">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgP5Ho4Z9t34G11LDhM4uhpdtlCci1f1dFUweMCZTu1zTRquKPVSMCp8pAcKsaLklSMBOJe7yIBb7yh_TBvePXF-5MDpPtSegGpuDuMk2x1MKPT18FUA6Rugobv0jICfMzQwhEem1z0bBqUzwKzxg8fx_tHfjdQslDqoLTpKuvzE_7cqPK9GWmFAyj9paGnDmhsQMSAb1xP_nzH1DW1uJRozC1O9RV2mTddSwrc7SVnzsi5qI7nS_2VPvcoM5qN3Rwk__MiswESnewwAcwqrFYA-SxOEGs6wa4uQcVjpWXgiycqg66c1D-tWyTAGik_Kgw1Qy05HGqkhMLGSIqiUpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی ۵ پلتفرم رمزارزی به خدمات بانکی قطع شد
🔹
از ساعت ۱۶ امروز دسترسی ۵ پلتفرم صرافی رمزارزی به خدمات بانکی و برداشت غیرحضوری محدود می‌شود و کاربران این پلتفرم‌ها امکان واریز و برداشت وجه را نخواهند داشت.
🔹
طبق اطلاعات رسیده به خبرنگار فارس، تصمیم برای این…</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/farsna/468206" target="_blank">📅 18:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468205">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f0c3bea69.mp4?token=WY_NrzfNr_-MvF9C-1huRSBKND0RKT3abB8U4PZ1U9jeeSUp5G-TY7RrHy5H39JQsz_YlnUCQYZSaaxGWBI8cJHigcvcIDKZ4HCzpMNqIa3JDsI2DFag_Lng-oZQBp_HliY0ISnV7mEUZTprhiK5k0YqJBWdHvkwVO2MmlWYp6ltRMYdEyYkt6JdBMdoRY_0RcTe-q6D4zmoZoLK8cBI4CW6qbb-QzZlchKsxXyx0ahYFEttyS13wJxJe9mAIzCScO8pSge2Sw7nbYdhcC_z3XcLRXJ5FVaIlciUtG2WvkaoqQfEKtxUeUk2oJ-rc9_UEmztvuBWw6-R3IUPHEe3pBWPSHEMjcjPHz8iXhT_MG2xS_dXqTYY_Wg2o6rucXq0TpUHRLYPv1-QsLiB0Pq3nBfpXVBA6N5OVs1V4q1DqBwfs9EZj9Pe7_XgBDJtAOVSPIaUAVNU6CGLdHg16Cr-mJdjP7x5wZ3GYwsJBjrGu6m-6nSxNWipKy9_eFxymfjlAKk330t4KK-AdknDTuE47DXkmp14xJYLS6Bq5ITKmwZgcLUq6wTPK555vnUL9GzV1XlAEipNn6KiJ5kr0NhvxDbh-xQZv46xTPHe2pw52YAxhX6nG8wx9uzC2jpQpZmmUKdMN7UbQjgVKHxGrr0HPrSC5MltBfbjr-XtazcPpbs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f0c3bea69.mp4?token=WY_NrzfNr_-MvF9C-1huRSBKND0RKT3abB8U4PZ1U9jeeSUp5G-TY7RrHy5H39JQsz_YlnUCQYZSaaxGWBI8cJHigcvcIDKZ4HCzpMNqIa3JDsI2DFag_Lng-oZQBp_HliY0ISnV7mEUZTprhiK5k0YqJBWdHvkwVO2MmlWYp6ltRMYdEyYkt6JdBMdoRY_0RcTe-q6D4zmoZoLK8cBI4CW6qbb-QzZlchKsxXyx0ahYFEttyS13wJxJe9mAIzCScO8pSge2Sw7nbYdhcC_z3XcLRXJ5FVaIlciUtG2WvkaoqQfEKtxUeUk2oJ-rc9_UEmztvuBWw6-R3IUPHEe3pBWPSHEMjcjPHz8iXhT_MG2xS_dXqTYY_Wg2o6rucXq0TpUHRLYPv1-QsLiB0Pq3nBfpXVBA6N5OVs1V4q1DqBwfs9EZj9Pe7_XgBDJtAOVSPIaUAVNU6CGLdHg16Cr-mJdjP7x5wZ3GYwsJBjrGu6m-6nSxNWipKy9_eFxymfjlAKk330t4KK-AdknDTuE47DXkmp14xJYLS6Bq5ITKmwZgcLUq6wTPK555vnUL9GzV1XlAEipNn6KiJ5kr0NhvxDbh-xQZv46xTPHe2pw52YAxhX6nG8wx9uzC2jpQpZmmUKdMN7UbQjgVKHxGrr0HPrSC5MltBfbjr-XtazcPpbs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اولین روایت‌ خانوادگی از علامه طباطبائی
#کتاب_باز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/farsna/468205" target="_blank">📅 18:10 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468204">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">گروهک‌های تروریستی شرق کشور زیر ضرب دستگاه‌های امنیتی
🔹
گروهک‌های تروریستی در جنوب شرق کشور که با دستور رژیم صهیونیستی مأمور به ایجاد ناامنی در این منطقه هستند، در هفته‌های اخیر با اجرای چند عملیات محدود و غافلگیرانه و بازتاب رسانه‌ای گسترده، تلاش کرده‌اند تصویری از ناامنی فراگیر و ناتوانی نیروهای امنیتی در مقابله با خود را ارائه دهند.
🔹
بازداشت تعدادی از عناصر کلیدی، هلاکت تعدادی از اعضا، کشف و ضبط تجهیزات و انهدام چندین خانه تیمی، نشان‌دهنده اشراف اطلاعاتی و توان رزمی بالای نیروهای حافظ امنیت در این منطقه است.
🔹
یک کارشناس مسائل امنیتی در این باره می‌گوید که این گروهک‌ها که در میدان واقعی نبرد تحت فشار هستند، برای پنهان کردن ضعف خود در برابر حامیان منطقه‌ای و اسرائیل، روحیه‌بخشی به نیروهای وابسته، تأثیرگذاری بر افکار عمومی و القای ناتوانی دستگاه‌های امنیتی، به جنگ ادراکی متوسل شده‌اند.
🔹
وی ادامه می‌دهد که نکته مهم دیگر این است که وقتی گروهک‌ها در میدان نبرد توان ایستادگی مستقل و تحمل ضربات را ندارند، تنها گزینه باقی‌مانده تجمیع لاشه‌های متلاشی‌شده برای ساختن یک ویترین بزرگ‌تر است. راه‌اندازی گروه جدیدی با نام «جبهه مبارزه مردمی» در واقع بر همین اساس بوده است.
🔹
این کارشناس مسائل امنیتی تاکید می‌کند که میان وضعیت میدانی این گروهک‌ها و تصویری که در فضای رسانه‌ای از خود می‌سازند، فاصله بسیاری وجود دارد. حجم بازتاب رسانه‌ای یک عملیات، معادل گستردگی توان عملیاتی یا نفوذ میدانی نیست و عملیات غافلگیرانه، حتی در صورت موفقیت تاکتیکی، به معنای برتری راهبردی نخواهد بود.
@Farspolitics
-
link</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/farsna/468204" target="_blank">📅 18:05 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468203">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رسمی هلدینگ تاپیکو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIr6eImLOPW8t6t2_Wk9vqoJM7d_EKUre67jxXwZubsMHA9XcyMt0J5jHSB5_DTq-XNSK9WppUo12u8Iq2YAVMIsO9NKp35ZzPqU2pVvkX18hz-crdCDdvjUoJNYuFK-bJUGKVbT-XhAoJwZQs9EJ879IbhnaIUM3qlbL73fzYIQuW2uoEPFC81n3OI6W9n5yuJlikkJNsnqBAh7DGPK9ZUG6Ke0bcEIwgTdk9wmvIeZe2rvI3Z1C3uRg2625RdCInMK_ZMyOsg3lizkGfYBK1B0Iop17FW0Fo1PV8wGNWp6KXZYl6LUr0FIOjFLV-yQAKYCRz9HwOfYj2ELTOOjPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
برای اولین بار در ایرانول انجام شد:
✅
دریافت اعتبار ویژه مالیاتی برای دو پروژه فناورانه
🔶
سرپرست شرکت نفت ایرانول، از شرکت‌های تابعه هلدینگ تاپیکو اعلام کرد: این شرکت در راستای توسعه فناوری، ارتقای کیفیت محصولات و تقویت فعالیت‌های تحقیق و توسعه، برای نخستین‌بار موفق به دریافت تأییدیه حدود ۵۷ میلیارد ریال اعتبار مالیاتی برای دو پروژه فناورانه در حوزه روانکارهای پیشرفته شد.
@tappico1381</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/farsna/468203" target="_blank">📅 18:04 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468202">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQD5GFlvOf5bkOX1xJb-3mxrJHdBFYUoz-Vuf5e4M_CG7lJ1GdJx6C5SA4ZHyp40u-QuBTHkQ7nWm8Gy5fh0igcdC9UZSZkRl8QYAq-ONKEDrUJZwHPr0pd3bMG8nhm_fs_hoDsr9yfB7oTWcedblzh_H0bfBMZDEMwG1620Ie4aAfuAojM-zS3YQeEQ0iCTIR9I27mWTF3tcyHQ-xEO6YT2S3e67GRchVdDSvMyMbk2hKYvWjwqWmEa3ahp-mGvjzLoSjZgF_0nV9BTL-GTx24Vg4gZ2z8tdXRWTJEDxl82v1Si6cmWF33rPup4hBdkv1vn5eLmQOxmDyhJbS8tAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
فرصت سرمایه‌گذاری فولاد مبارکه
در حوزه ساخت افزایشی (3d Printing)
🔸
برای اطلاعات بیشتر کانال صندوق سرمایه‌گذاری خطرپذیر فولاد مبارکه را دنبال کنید.
◀️
برای عضویت اینجا کلیک کنید.
|صندوق سرمایه‌گذاری خطرپذیر فولاد مبارکه|
🪩
MSTID.com
🆔
@Mstidfund</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/farsna/468202" target="_blank">📅 18:03 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468201">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/farsna/468201" target="_blank">📅 18:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468200">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbXFkhG0vxEJT5ooMgeyVGYSxybs8lBfQicc8_2y_gPGvIuyKZ3kDlTRiqoDSXIJiOT9DZr1DzYZHqkJdjHiCmjFrGmR4-9wUt43AUbCYHY5zuz29_-vSpyyGQ2A8Y_Bz8z9LqOH6KiFJoMP72a5MvZs9qsjSJcMbL6qUQ18TBPb_yNmeJuYBbbhxoGJTadE1DbH5ApChYkoLX_5nWyaP2PZKg9keEoAHMDGCUOvU6Th_DkxlWsyAtp6sjY9tceCqPLY4IJdVd32AEyZCNsDnOqq5Z40yg-PYpuXvJbLLVP7pXX-EfuxvF_Zwx8VidrNDK33XF4RebFZW1JUQ-92gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاهان فاتح دربی اصفهان شد
⚽️
ذوب‌آهن ۱ - ۲ سپاهان
@Farsna</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/farsna/468200" target="_blank">📅 17:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468199">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c704e3ecd8.mp4?token=UgyR6nF3NBGVz9Eclw2QyiDr4zWt06zvhXtx-lOTxLJxi0sFwouPS6J0sv2g_JD2h3QyK4WG4eLhshKvUYuH-Rlg2ALaV3hvNUgcS9xIu0FuMWpyThWut_PLcy_1ocAjGHEyCIahAD3mj2cODC8_FgyuI9AmES6cAKp3YgA3TN4TL-bdR8ygC4XGwoYahnzKi5JiStVjkp25j1G4Ehe2fkxxq85eOm7MnLIrY1_rlmDAiyQWhvfAorDI1vY_ws34yjB67hNb_8t9tlnrXDfHmd4sRaXOV7I_hL6VoXTaU0vaBAAYb50z8fPm6NcZL2bmQ2qG5_mjmUWEucRTS7Q7fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c704e3ecd8.mp4?token=UgyR6nF3NBGVz9Eclw2QyiDr4zWt06zvhXtx-lOTxLJxi0sFwouPS6J0sv2g_JD2h3QyK4WG4eLhshKvUYuH-Rlg2ALaV3hvNUgcS9xIu0FuMWpyThWut_PLcy_1ocAjGHEyCIahAD3mj2cODC8_FgyuI9AmES6cAKp3YgA3TN4TL-bdR8ygC4XGwoYahnzKi5JiStVjkp25j1G4Ehe2fkxxq85eOm7MnLIrY1_rlmDAiyQWhvfAorDI1vY_ws34yjB67hNb_8t9tlnrXDfHmd4sRaXOV7I_hL6VoXTaU0vaBAAYb50z8fPm6NcZL2bmQ2qG5_mjmUWEucRTS7Q7fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سخنگوی نیروهای مسلح یمن: شرکت نفتِ منطقه صباحۀ صنعا از فرآورده‌های نفتی خالی است و هدف‌قرار‌دادن آن هیچ ارزش نظامی ندارد. @Farsna</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/farsna/468199" target="_blank">📅 17:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468198">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8c4818c08.mp4?token=nK8w_dmPyM7YGnDUIsanOF969DOgODSyeh0EpAW4qnzXNQkSNZvGk_IHDfuH1_9IFD6T7D5lmvTRgQc_RC5DvlkyzEg3hSy1jqBEOLTv4ksufbAO8cVmUboDnsLwxY8jOwUVjUG1T1ywrgialv2gpdE0cnKOx0E9Dlz1fhb3J0CpdLcXaskbnyjKKtWY6vDtyEG1QGpnw2JCxq_UqtX9Mx3zLZCMxjsReNZEtSjdD_gTBoPjjk_83UxoBmtIEthRb6XJWY8uW4LozctRbtk1x0bap45BrgHiGGorkYnYMIczXe1Qyq3m4zIiPYv1Qv9jJGAm18R3F-09EXoERqFJIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8c4818c08.mp4?token=nK8w_dmPyM7YGnDUIsanOF969DOgODSyeh0EpAW4qnzXNQkSNZvGk_IHDfuH1_9IFD6T7D5lmvTRgQc_RC5DvlkyzEg3hSy1jqBEOLTv4ksufbAO8cVmUboDnsLwxY8jOwUVjUG1T1ywrgialv2gpdE0cnKOx0E9Dlz1fhb3J0CpdLcXaskbnyjKKtWY6vDtyEG1QGpnw2JCxq_UqtX9Mx3zLZCMxjsReNZEtSjdD_gTBoPjjk_83UxoBmtIEthRb6XJWY8uW4LozctRbtk1x0bap45BrgHiGGorkYnYMIczXe1Qyq3m4zIiPYv1Qv9jJGAm18R3F-09EXoERqFJIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اخطار قانونی قاضی دادگاه منافقین به نهادهای ناظر بین‎المللی
🔹
قاضی دهقانی در پنجاه‌وششمین جلسه رسیدگی به جنایات منافقین، به مراجع اروپایی و نهادهای ناظر بین‌المللی درباره ممانعت از استرداد متهمان و اجرای اعلان‌های قرمز اینترپل هشدار داد.
🔹
او تأکید کرد هرگونه…</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/farsna/468198" target="_blank">📅 17:57 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468195">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GOmdJQcro71XUWMDBpIN4ZQ0C_vha0UoAWnyKV7m00xvVJflkWwmBKRDCoVTKyDPS-yjue5zk7DkpKc-gkxTM6Qu-U4ZtPQhJ9YVlIPnrfp60EtMaaP14dB3GhJU8R29w6p7KOATRi7LQbfm6AaeAIT5t9VUhNy_x1s3FOz38ncUE7dhA8sfmMYOJ7NhUc6wHh85CNTGWuDF4xNIDiwVlr7oaygVfIMqt0yMQldbe7XlFRDTMtkTZN01FTfEohK8QSRAgBEebCG6F9JaG3Kamfms0eZ1BTLWXN_IGhuRWsTXk4jDQnhRduU65z956bBCRIKahtSDpM7cS3btdDp9IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nv7TeqRRg35H6-dUP4x7gUPs8YK_-0RnY076oqHL80nHtvScIS-f8SQT5DOMWycrkgHQhpJqXWAnBONIyVbaZs2p_yg4u8Mxxpx8bR_815lj0Sj3emgt9qz5xDzukoDvGFPFpzGSokgTMLQMoGDPLBEQMXgXf8M1f-97MEoKceKcd7mLeV5kDx37WqPsBY96PjpIhaYkyY9uHSw0iVWeEzYAleqmulNzBQfmWMSfCc_T_kYlDw6Srq_AAuEa7r2G-bs62Z0wFJOuGB8rVl7ez9g70GAlV9gtzwhsbYKVBajY64F2gNJ-hRjg1A1J8Q-IRRdIGiulcee18PGM5utRjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pD2br8_P5hbd1wiDhqQhn40duII5f82sg7I2oGcK99lCJg0xbWqps5pPaEjfAIuBjqZMhizic1YPdIaE9p9r_Q0bjToX69tblSI4j4KOJwvi2K0sod77O49al9f4YC4pAWskMSQe9dxAYtwV04TXXarfoFn1-DYGLwFxjFPTBzPdzRugK7wKJ8KgJv4mbOJGeI1UT0C3AIxCNKKO8-f42lO6Ug4yfAbNq9Fn-DvCP0Qymnf2eVoO6o0CZSYeJfLKwobK8Ca-BIojiuCJGsslR-OFedN2QG4aUPioXshU4JyUkqDtqoJqKd8dCy1-iFGkXY6lpmdfz_ghqFyVqwyACg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‌ هشدار فوری یمن برای تخلیۀ فرودگاه ریاض و ۲ تاسیسات نفتی
🔹
سخنگوی نیروهای مسلح یمن: در صورت انجام حملۀ اعلام شده دشمن سعودی به صنعاء، مقر شرکت آرامکو در الدمام و نیز فرودگاه ملک خالد و پالایشگاه شرکت آرامکو در ریاض باید فورا تخلیه شوند. @Farsna</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/farsna/468195" target="_blank">📅 17:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468194">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oeT2OJv8EY3RhVWnMpi7V496ywsk1LctAwTIK9G74Qt1sMQq7UZq_kL0QB6Ndu2BMIUolDPjsDrGhgVkqd5CtZYm3F9FOjHMYVZWZ42r8SR8aD-wKOXb6bjuk2nRPmZ0GI2vxzggcfzQnDuwAoM9FL4IyKH4kSYr5XegZqwAkssCwMZr2UHY0nypE8GdJ_7wk4ZMTwr8KYMBG4vJC8kZaweJQAw-MAoafC-OMiNxxmMJvpQdyobT_J9PsGAc7haPrWyxFnfa7mAbQWrvySdYWN50BOdl3F7G3PgVozNrQQPSMI2uONbFK3JIp1pV0ZuJiVxXgKVWKKvszY7sWgAKKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت ایران بیش از ۲۴ دلار گران شد
🔹
جدیدترین آمار دبیرخانه سازمان کشورهای صادرکننده نفت خام نشان می‌دهد که نفت سنگین ایران در سپتامبر (شهریور ماه) ۱۰۵.۸۴ دلار به ازای هر بشکه فروخته شده است.
🔹
این رقم نسبت به ماه پیش از آن یعنی آگوست ۲۴.۵۹ دلار گران‌تر شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/farsna/468194" target="_blank">📅 17:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468193">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e97599bfb.mp4?token=gbR-G6sY3Dm0Yjy3aowT6gA7IjxLgJiPzalz7OCSn4brfrDmZ2Ncb9an4hL_rIe8Fxlb3KSfAdI1KRp_glbUALcqrQs9sCwJsYywwFATrXjlqilCnyZki4hXWJ2ZrgntE2RDRoQfkWYhF0rEJNztxBbN-xEHBu1kOJIMhfidHEqVjSmx4HkM5dpD_VO6yXKPxaKvwcmstUr0a-kPcLMj3P1Z_gNDVl_VZKlEvJGGfFo9nlqVf-Ghkg5SFTjpaJqgVkoFsTrwwX_dqhd181da_ApU5X9HmvVy0tE_LJxLe3LigiPfMZfA3_Vl5cUxWaWn86fBi7cEnnTR97lu8Optxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e97599bfb.mp4?token=gbR-G6sY3Dm0Yjy3aowT6gA7IjxLgJiPzalz7OCSn4brfrDmZ2Ncb9an4hL_rIe8Fxlb3KSfAdI1KRp_glbUALcqrQs9sCwJsYywwFATrXjlqilCnyZki4hXWJ2ZrgntE2RDRoQfkWYhF0rEJNztxBbN-xEHBu1kOJIMhfidHEqVjSmx4HkM5dpD_VO6yXKPxaKvwcmstUr0a-kPcLMj3P1Z_gNDVl_VZKlEvJGGfFo9nlqVf-Ghkg5SFTjpaJqgVkoFsTrwwX_dqhd181da_ApU5X9HmvVy0tE_LJxLe3LigiPfMZfA3_Vl5cUxWaWn86fBi7cEnnTR97lu8Optxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌گرفتن نفتکش متخلف در شرق تنگۀ هرمز
🔹
نیروی دریایی ارتش: ظهر امروز یک نفتکش متخلف که با خاموش‌کردن سامانه‌های ردیابی قصد عبور از منطقۀ ممنوعه در شرق تنگۀ هرمز را داشت، دچار آسیب و آتش‌سوزی شد.
🔹
یگان‌های عملیاتی نیروی دریایی در شرق تنگۀ هرمز، دریای عمان و دریای عرب با اشراف کامل، رفت‌وآمد شناورها و فعالیت‌های دشمن را به‌صورت لحظه‌ای رصد می‌کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/farsna/468193" target="_blank">📅 17:38 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468192">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGgzF12VSmIdYmzf7RK6xpH2MllmEIxlmhXIP1oF2bhlforJZrhNLLFdWrGYxbkfyDegd8kK5aawrrZ-1TKJwagIUgMntAG3GKk9HL2W-bFBa78oBnWJaV9MHbXDNShx_wmFxuSBQfa50_yPtXI9qXNLVfkmT-55jrlRCplgg--8O6UiV5oagtf3Hn8ZojXwDbQn-39CtPn8pFNPcUBm4TUe3-1xvkCEmiqhJbYB5RS5RZ_0hO0PlmBfXfkgpC55hEa557PV2doeI-nrkSLnfGFDRIIyoJCTNqMKS4iiIloIEONJviBRrWFWy8dq52zfEu6A_pf9bEZIqLCqfHAvnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
سازمان هدفمندسازی یارانه‌ها: مهلت ثبت درخواست افزایش اعتبار كالابرگ تا ساعت ۲۴ روز جمعه ۲۴ مهر تمدید شد. @Farsna</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/468192" target="_blank">📅 17:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468191">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‌
🔴
المسيره: عربستان تأسیسات شرکت نفتِ غرب صنعا را بمباران کرد. @Farsna</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/farsna/468191" target="_blank">📅 17:28 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468190">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">📷
ائتلاف سعودی برای مرکز نفت «الصباحه» یمن در صنعا هشدار تخلیه صادر کرد
🔸
سخنگوی نیروهای مسلح یمن در پاسخ گفته هرگونه حمله به صنعا با پاسخ کوبنده در ریاض همراه خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/farsna/468190" target="_blank">📅 17:26 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468189">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سازمان برنامه‌وبودجه متولی جدید کالابرگ شد
🔹
معاون اقتصادی وزارت تعاون: براساس تصمیم دولت، سازمان برنامه‌وبودجه به‌عنوان متولی اصلی طرح کالابرگ الکترونیک تعیین شده است.
🔹
تمامی نهادها و دستگاه‌ها باید برای اجرای بهینه این طرح با سازمان برنامه همکاری کنند.…</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/468189" target="_blank">📅 17:24 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468188">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromانتشارات فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Slg2miskmuCs2YiILX-GvpAl61NmZJ4Cmjv0ANmXKZLLdG_8S5_GYTqNX0o8SwMliJqsm8R3M7WsRkSpeOKPtQ9Q9JDO6brYdSE0PZFKWgRfznt_nfhH50rnUPsy6-TPXIvNc8EolSNSISUUyzHHpuxWEdExo8b_MLTPKyanUt6AeqN6jy833RMrv-ODyT1T_8PSQ3WAgmV6hDFGajbUwshESxsVjRJJpbSsE8ALFdQwgZtz844dLkLCt8k-y_ViRz8etnwX4l_fkyKSwl0Tlpef9ueaNfu5PVU55YgXdvu9tpeVOLccVZQt1Ot6Vzo9iU6O3FVSAKZE44Y4pv0nKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📚
انتشارات فارس؛ مرکز جامع کتب رسانه
، جایی برای کشف تازه‌ترین منابع دنیای رسانه و فناوری!
نزدیک به ۲ هزار عنوان از حدود ۷۰ ناشر؛ از رسانه و علوم شناختی تا هوش مصنوعی، همه در یک مقصد.
🚀
🔍
برای یادگیری، پژوهش یا پیدا کردن کتابی متفاوت، اینجا را از دست ندهید!
راه‌های تهیه کتاب:
‌
🛒
برای خرید آنلاین روی لینک کلیک کن
📱
ارسال پیامک عنوان کتاب به ۵۰۰۰۱۶۷۶
📞
تماس با ۶۶۹۷۳۹۹۶ یا ۶۶۹۷۳۷۹۴
🏢
فروشگاه حضوری: خیابان انقلاب، روبه‌روی دانشگاه تهران، مجتمع پارسا، انتشارات فارس
‌
✅
انتشارات فارس مرکز جامع کتب رسانه</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/farsna/468188" target="_blank">📅 17:20 · 21 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
