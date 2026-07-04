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
<img src="https://cdn1.telesco.pe/file/lFCukSmoru8oVbjNQSAw3dQmNClwDQdQdd_FAysDKaXzu7CITeZ2FoH5lK4XGIN7EvYLOseyNaUZA-Lk-4BukLZBUr9XVBeWtmBadtg_Apw1MmGmN9Xgkcsz7vHQEUAS_Z4qlDJRPVFezpepBscx8biszJtDhtRMUv-TzNWJR1f8Z5luDVViRZa4Gb9NHDjUq75vd4Ppv8_yHP2wlSi31WQmwbYqrkm4723SwpRyDa_hC4MbWVtwxCoPcggw8MQurTWcPb-N3HkiYi8iW3A_2fSPQkIoMDu77vIIV7QqjkogiRLSQYEhjxBwzCc5LmvKH9kjBoMYwpZPQUeZj1-8lg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 159K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPaiایمیل کاری: matinsp.job@gmail.com</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 20:24:41</div>
<hr>

<div class="tg-post" id="msg-4226">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🛡
آموزش کامل نصب و راه‌اندازی سرویس MTProto با ابزار MTProxy
فیلترشکن قوی و پرسرعت برای تلگرام
https://www.youtube.com/watch?v=pyvB6VSPhwg
@WhiteDNS</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/MatinSenPaii/4226" target="_blank">📅 20:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4220">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/orIWqIMWiVmP1_ywP863xKIvbPOQRlCutRQ2XTbGgVYGqoG5Z_wYpYTKf9ZF6BUw-UG_wiL0dGvwIBUR98AkSauFW0pk_Cu7sNx9uTpDtwufdQTMLU0wuiw6CqvgQr9xqV-CD1FuwWw1KMpiXaRzKkzfN-oO-Fx2gsDpwzX3oXNd9IayJb5InBQhZlF6bs76mZFNDr3yBm_9RpNxdBlyD-1UjobY1jvr6C0eZlL5PtHqmRZokG27bcRv2WHahn-tqgjg6tfuvFKrb9IcCQ9VU661KLal8ndmCVVnPm4NwZwqxjKP2r0AAnqFdU7oi-4QDb3p_eRxFOOzfyt4KB16Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TzhguowwV4y4hc9M_ywXbVWeOfRS6rtG4UUKLbYicxOeJmlQCvaVDWvj1Rd79ItGYXzmBjYiCRfLEaaGAdYjXhF0rcRXNeIHSXQU7U782Gji9kYtKPo1CIgjjIMyWj0PrsYX8WintBq2K46U0meYqelKO_Pu2bF3Oi2sakMznw2VMz3LdrqYDKbwlHGMkznqMTjlwJ00Pv9MX6UChVD8kUwh1zM9wxhpqsRT07sZ4HtZ0OScU63zPSRfjufLbmqtC5JPwaYOiB7StHtqThjQiWWkdw09oJN2dS3-hS6sUAx2sxBFk2mepP0I9vPOPxpL9elTWLAazISxKbNwIW4vDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aWbNDsJ9fiyx4Cc_y--ZZG5FXpJMc4zoJqYcyFpFZYcDFQdNcS6_H-YY8SC1QRy5FC1Ybd15ixrB9_1-AleW43LZG-3NNCeloMlqUY5lUkvdrLWnJufM1gGtnaIMRmmhBrXvyOCfgUUBN2ea3lsWqQFjqw1x8_yGGoIZ93tGhSSpgXnf0m3nyRNrjiaC5cA9bjbQ85Xxo8B5KtZwRcBJcisY7GkvVglR-aHQ6lp0BwyBj-5qutxEsVc_-ZBIktQDi86vkIgz5qovR216Dcem4O1xiNL2V074q7CUl42cEKRPFgjjlJC1wMwJdOp_V5_v5P4PdcgG1lY7kFaMTHZK8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Q1o8BjXYEXXbEs-5dhRrGBTIfujSkNJo9gjEwVmKWOA20CgkxaXxNc2Ys2kPh4QvjdYMjyxrjN3PX9kPuJX4rzS_dSS3K_lNkSVDSm5y4CKYgI1HmQUwimWkCqkkSNmcWa8XLSY4k6H_boIWfsZnlpr16-KzBWnfav8kxFBZrA0UwHMho1OzYAMoFUQQfUYzH9J3LhjvSrnEo6fZbn2HFHChHkzx6e0i4NPL4SAKspmwhr8TRH5XfKidwTqR6Y3lWeOXhho6SqyakjVAOjxjK7K7WzKRf6qxCvcGn8qz2CIW2DjIooe0FXHOZi2EjevHiAvwWOY4FuH-4POZx8sJFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fRDWT9gytCbonO_ru8R8pjSmjYMGH560f-la2VCTLfndpREBAdmon35fFYP-BuqopcTo6QJEdaCG-cjHp3DRmsiak8sjdeV1fE7vFsRwe9346hUCh-1Fd-O5gSffYLiIQTGzcR8vJS7Q5wtM0eCnP4x_QYaA0T8ZcD-9cZTJM5qR6002qFtErmrQOfGJ9aeQeTmSEBVWv15l0w9QA1vH-Fc4gKdSI6wGjmifCofRy9_WK0UyqIt1i5hNHHhvcUy7iHRT3gKu7tRzYKkaAbAfqgRnfsQgS0kLgl86bHHhez-1cSFVPMtu-yL-BrzPwRxysS6JAZG4HziCAmE9AmV7qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ihsa68s682InKES1crNTEucDqb60BSNM4eO7vwGdzXU-nSGtvpPyEhY-9cxra9xWs5Tqpikx8TAKdpmShyRQV_d50DplW3hcBSkXgkMAfhc244fg3T1InuO6i_KX3yE1HM9tTwjywBE77tbQNqTiY-sq7RPJlXziDWKvuYGtII71MCPejdwfn89Z3iSW9Djm7O6hkyvZNPwnLBx7LpaJZox7VYTyHC9OOzJYrsaIs37jlq-i_4-QoiVRWcD1TLkpBJu5PmeOLZJHsx9-IV_7PJSuBZX1Odl4ggRT9M1Jw61sEVI4ARpmCHRCa5A5Myx-IfLweY-_Az4Oa1I-HS8HiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">راجب این هایپی که در مورد «ادیت ویدئوی بلند با هوش مصنوعی» راه افتاده چندتا نکته می‌گم و دانشم رو از ۵-۶ تا ویدئویی که تا الان دیدم باهاتون به اشتراک می‌ذارم:  1- نه. اگر دنبال جواب مستقیم و سر راست هستید، هنوز نه. هنوز توانایی این رو نداره که با هزینه‌ی کم،…</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/MatinSenPaii/4220" target="_blank">📅 20:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4219">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DSjlURaa5CLJN4TRI2s3fr31pUvfI9sQV6lPgaD9PKX3mu234wCB_PBErtB10Hv44qocpfXe8Bo6mf_WtY8TdoZWZVlYqHD6djj9OfP6BRDODyCvcegsBqpbgbsvcRxKKtLglmsiFjcoSsCVTiPlskRf2W3MIOm1KIyH_t0yL6MRS-pZXbqJwzn4GK2wssSyiqS9SJ9NexnMyzwPHNFjE6NZpnYARlOSLpri5cV7pU8kt6osghI1qs0x-GFypCoNInPE-bjz8m2jf9MqnnD-P5qKXxmuiAwdG2oHsJFeus9DkEp2MD454Hg8TIrOO9D4-s_osjzjMLLMDlGjCqbuRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راجب این هایپی که در مورد «ادیت ویدئوی بلند با هوش مصنوعی» راه افتاده چندتا نکته می‌گم و دانشم رو از ۵-۶ تا ویدئویی که تا الان دیدم باهاتون به اشتراک می‌ذارم:
1- نه. اگر دنبال جواب مستقیم و سر راست هستید، هنوز نه. هنوز توانایی این رو نداره که با هزینه‌ی کم، بدون اعصاب‌خوردی و بدون زمان زیاد اون کاری که ما می‌خوایم رو انجام بده.
2- چیزی که من از ویدئوهای این دوستان عزیزمون فهمیدم توی یوتوب، اینه که میان با مدل Whisper و یه انجین شروع می‌کنن به کات زدن(که همون هم پر از اشکاله و نیاز به ادیت فراوان داره) و بعدش شروع می‌کنه با یه سری mcp و یا پلاگین کلاد کد که اونها هم اکثرا نیاز به api key پولی یا اشتراک دارن(کما اینکه خود کلاد کد هم نیاز به اشتراک داره) یا یه سری ها هم با Hyperframe، واستون موشن گرافیک می‌ذارن.
3- حتی همین موشن گرافیک‌ها و... هم باید قشنگ و دقیق بهش پرامپت بدید. این نیست که خودش متوجه بشه و این کار رو بکنه. همینطور توی این ویدئویی که تام‌نیلش رو گذاشتم، طرف برمیداره کلاد کد رو اگر درست یادم باشه با Opus 4.8 می‌ذاره روی Extera High effort که خب توکن بسیار زیادی هم می‌بره و فقط ۴۸ ثانیه‌ی اول ویدئو رو باهاش ادیت می‌زنه(بقیه‌اش رو داده ادیتورش
😂
خب مرد حسابی، واقعیت رو بگو دیگه. که مابقی ویدئو رو دادی ادیتور خودت ادیت بزنه)
4- هایپ اطراف برنامه‌نویسی هم زیاد بود، و تا حدودی تبدیل به واقعیت شد و الان ai سرعت برنامه‌نویسی رو بیشتر کرده. پس شاید بتونیم انتظار داشته باشیم توی آینده‌ی نزدیک، با هزینه‌ی کم و یه اشتراک معقول، زحمت ادیت رو از روی دوش ادیتورها برداره. ولی جایگزینی رو بعید می‌دونم</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/MatinSenPaii/4219" target="_blank">📅 19:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4218">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کاربردش می‌تونه اینا باشه:
۱- وقتی دوست دارید هر چیزی رو بگید و در لحظه کامپیوترتون تایپ کنه
۲- یه ایجنت لایو با Hermes بسازید
۳- و کلا کاربرد عمومی. مخصوصا برای کسایی که disability حرکتی دارن و مثل خودم توان تایپ کردن زیاد رو ندارن</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/MatinSenPaii/4218" target="_blank">📅 19:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4217">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">چند روزه می‌بینم همه دارن در مورد whisper حرف میزنن. خواستم بگم یه ساله برای تبدیل گفتار به متن از Handy استفاده می‌کنم و واقعاً بی‌رقیبه. کاملاً آفلاین با پشتیبانی دقیق از فارسی. حرف زدن با کامپیوترو خیلی ساده می‌کنه. github.com/cjpais/handy‎  فقط کافیه شورتکات…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/MatinSenPaii/4217" target="_blank">📅 18:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4216">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XOLegCJTFv46dbT4a_HxeO0Y-Atb-aPeH71QDDRc1FZoQ3Mx9m9XxzW1_XK3R9ozeE9Lv-mIt_OCeXrbAvzfTQUEv32A7RNB-2vl1VyM9rbIBTKGUMTmwHkA9mmX0_g1NHj3BgliCHwnfGp-LostinXfliIRFHKlHsK8kDr2EecCU1iKNEWASIGUHL9xtPic9UUsuGui_-miKl_eyKCKKyB-9h0JV0xHh23fJUTvTPfG-yJcm6S4kfTD52LcAs3-N0KmN0mpqfIGdrBTdMA9CWFpEVc9J-vNhbq9ljPwGa8f1RDBROY9cODbd6sGwsmqUNs9L538k0nSIxiBJ45a3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند روزه می‌بینم همه دارن در مورد whisper حرف میزنن. خواستم بگم یه ساله برای تبدیل گفتار به متن از Handy استفاده می‌کنم و واقعاً بی‌رقیبه.
کاملاً آفلاین با پشتیبانی دقیق از فارسی. حرف زدن با کامپیوترو خیلی ساده می‌کنه.
github.com/cjpais/handy
‎
فقط کافیه شورتکات رو نگه‌ دارید، صحبت کنید و رها کنید تا براتون تایپ کنه.
اگر دنبال یه ابزار STT بی‌دردسر و رایگان برای لینوکس، مک یا ویندوز هستید، حتماً تستش کنید.
✍️
apt_hq</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/MatinSenPaii/4216" target="_blank">📅 18:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4215">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ezWSYemnCURuhyjRfgge5-pzAQ1jVC331EigUI-1UIJiq_u8e1px-WSXvx2AHi3k4nKyz_l3bjF4gsvYMXRYOFsQaYksWoGhPX9mi5wcmNnA1_ipA3HQKPmJ42NS9J18G9BDp4OXpri7F0JveTeuMcblTOYRIp_UduaMILVu3U3_ibE8RXPzrIPrqg2lNd5P3SLIKxYdvXmjUVD-gHyd-YOb18hfwqbkxYQRFDq8AAOiX-KzsaCHkRQpCPSZ3e72BHD17xqcn3E0ULZegO_K5TyIlz51CQl05r-UN8uAMpsYUg7QdPZdJGxCfz7-2dawa5pnPtDadhrQ8cj1xcPTrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا به دادم برسه
3 ساعت و نیم شد ضبطش
😭
😭
از بس دستورات هرمس زیاد بود یا طول میکشید(کل ویدئو رو با api رایگان رفتم بدون سرور و... و واقعا هم خوب بود) و قلق داشت انقد شد
اما ادیتش کنم ۲۰-۳۰ دقیقه بیشتر نمیشه</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/MatinSenPaii/4215" target="_blank">📅 17:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4214">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">برای مثال کیوریتور (Curator) که توی ویدئو توضیحش میدم، یه جورایی کتابدار هرمسه که تو پس‌زمینه سیستم بی‌سروصدا کار می‌کنه.
و Skill هایی که خیلی وقته استفاده نکردید رو پیدا می‌کنه و آرشیو می‌کنه تا سیستم سنگین نشه.
ویدئو پره از اینجور دستورات و همه رو هم تک به تک انجام میدم و تست میکنم و صرفا روخوانی نیست</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/MatinSenPaii/4214" target="_blank">📅 16:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4213">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">هرمس قشنگ یه کارمند تمام وقته. ویدئویی که تا آخر شب می‌ذارم رو حتما ببینید، تا بتونید از تمام پتانسیلش استفاده کنید</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/MatinSenPaii/4213" target="_blank">📅 16:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4212">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">به زودی یه ویدئو داریم برای تمام دستورات ریز و درشت Hermes</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/MatinSenPaii/4212" target="_blank">📅 12:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4211">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">به زودی یه ویدئو داریم برای تمام دستورات ریز و درشت Hermes</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/4211" target="_blank">📅 12:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4210">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iCtW00ZIbkmuCnpKt-sMLyAfxOXp15p49sdgWMj__IznFSWU29cVJmS-OwpP0RpeGLzlgkT2i8KtumC3FZes9lQxzMZEynqf9GcMaco6awCpsj44OffoCZB1vLG_qpXhynGULNLdPVyr7hgv37OZxLIAxT2h1U8fcDD6syOR4SmOw28K8E-X1j2KATjeWg0jsyTbWgGvIAj9rlTn7RvX7xWl6TetqxWLuzp3FyQr7ZDvm1lldo06DQ1cR6_e6P65vgqo6WwgEXYG8Nc7A7juZ_RDG5hOgMIJDJCuY77AbHXCOuehqCjEVHhkx6gPxXlD1VJCpdfQFYkGG39_Dz8vbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این داستان، ایرانی بودن</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/4210" target="_blank">📅 01:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4207">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SytnTUGNOb-SZQ8TiQLvDl7uzdiP4ysm0EluZB6o2iVAby1Tl1DEQxAht2ZSV0RtatQVEDpBtKclVPBrERKO5_EiusqIXgVsGvOAjIF9YQ-N4KN7XiFAdmjptjpb1gceNRXIKhWtaDOsRq1nCOt_4UHoRWqxpkGQPd1BZXQznddlXUwMMrw9lTAHW2g3ia7CJl0NWU5p74Viox8aq-P9AI2wyvgbxkd9Lk2Zh5nLXQIUmZSSFZq1jbRZZsvaCSy_pvWYYDS3CQCvuGDOpfsUEiYAuK7s00RYzYvD4dEmjcRfUUIPRoWVBizg72p6OC1SS1h0ZVB-4W0c3vEjZNNI6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EtPXhBswp_9-kcWXY7swRBaJzro-RU1jbx5OeM0vDRSbraDKcSomR6AZf0ufyRQw52AEMnes87s2l5bzisUJk2J-iVhmVEdzyLnCA-mDME4XpASMSWceOo1WSZxicBiMLNbR0-5mqrbmk10gC0vx5BCsekLy31r66Suhg7D0sqfoSgE2DdnjUhWMGRJ0ULTCoWYfpeBKdx4g6ZNpkd0wd8ueQK9CXO9Cc225ms7HlY6FBjTYAr5L_y9eVRkalRaRdhx93yIai73A0e8cH2Z229FJPaPVkLcDrFoyUeDAmTLpqi9lBpfvR3DJuN_Z2iH3UCBUOG_-4PuECY4yef12zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tUZ4nl8T2-tIHSgQa7LlKk06W5R3wVk2Z2SgvjsrKqHS5jBi1vIN98IdxDWiwq34H16orw3UNrvm3b7akDmNMOJkOLjwIHsN95b1CZaKsHkmEpMt4QSbpvOG6dTt-QMqMjoE2cDc-zLftKBrQ_eLr-T1aGK9-rS-XZK0MHTf9868HH6If8XTikdmnPHe0wSVu42_BEdTtdItZVGSOUJGUd8W2bTA9yJ7u42OLeDc6knfw2Dyk71TzE8pZUwoo860yj3dbyfQ0B2s8kGG6oxKZ4LvTFtnhN4b3PEgvQbn5SWccTmRVNg3mo4stN9vJ00P_Cz_eHV3QytQGfLDAQ8FEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">توی Hermes اگر از دستور Compress استفاده کنید، به صورت دستی زمینه گفتگو رو فشرده می‌کنه و چیزهای به درد نخور رو حذف می‌کنه. هرچند خودش وقتی توی هر Session به 50 درصد ظرفیت برسه این کار رو انجام میده، ولی تأثیرش روی توکن مصرفی خیلی زیاده! همونطور که توی عکس دوم می‌بینید
💪
/compress
—> فشرده‌سازی معمولی کل تاریخچه.
/compress here
[N] —> فقط تا قبل از N پیام اخیر رو فشرده می‌کنه (N پیش‌فرض ۲). پیام‌های اخیر کاملاً دست‌نخورده می‌مونن (وقتی می‌خواید مرز فشرده‌سازی رو خودتون کنترل کنید).
/compress [موضوع خاص]
—> مثلاً /compress database schema — خلاصه‌کننده اولویت رو می‌ده به موضوع خاص (مثل schema دیتابیس) و بقیه چیزها رو یه خورده شدیدتر خلاصه می‌کنه. و محوریت حافظه‌ی Session حول همون موضوعی که گفتید می‌چرخه.
حالا شاید سؤال پیش بیاد، که متین آیا این قضیه، کاری به اون حافظه‌ی بلند مدت و حلقه‌ی یادگیری خود هرمس نداره؟
✉️
باید بگم که اتفاقا چرا. هرمس قبل از فشرده‌سازی، memory flush انجام می‌ده تا اطلاعات مهم از دست نره و توی حافظه‌ی بلند مدتش ذخیره می‌کنه. و این شکلیه که چیزی از قلم نمیفته!</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/4207" target="_blank">📅 01:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4206">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56bbdb4680.mp4?token=CeuEmBciP3Ntr0t4n7I_ozYWf4kXPUEC6QpnclI49-LhcA0UHofX6VPr9NRMFo7OIkuCbBEnBV4bmtzV0k013688ZNhHEvnIuFAldfDoLAI1xzzme3tyA_5Qgun74xj9PsMnEbM_9oJggUv5xxwiJyFUOnj1RjH7A2JIJs6BmJmhxJUzCPKcNJqCkGXN83QRb1WhUAR_Z5vLsKSzE4BKn46Of15I8BDyx1V-8EOAdYc5DAYWJfmK7a9K4Er3UPA9MxNExV6n9ZZuKEP5LaDBTB51Yuu_sacdwDYKnicvr5hz5lI7fXwdk4CgmrGC7NyLf6iQ8KSMKDTKULdCyOcF-4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56bbdb4680.mp4?token=CeuEmBciP3Ntr0t4n7I_ozYWf4kXPUEC6QpnclI49-LhcA0UHofX6VPr9NRMFo7OIkuCbBEnBV4bmtzV0k013688ZNhHEvnIuFAldfDoLAI1xzzme3tyA_5Qgun74xj9PsMnEbM_9oJggUv5xxwiJyFUOnj1RjH7A2JIJs6BmJmhxJUzCPKcNJqCkGXN83QRb1WhUAR_Z5vLsKSzE4BKn46Of15I8BDyx1V-8EOAdYc5DAYWJfmK7a9K4Er3UPA9MxNExV6n9ZZuKEP5LaDBTB51Yuu_sacdwDYKnicvr5hz5lI7fXwdk4CgmrGC7NyLf6iQ8KSMKDTKULdCyOcF-4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بی نهایت آدرس ایمیل با یک دامنه روی کلودفلر:
https://youtu.be/Z069VNFAgAc</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/4206" target="_blank">📅 19:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4205">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">خب دوستان GLM 5.2 اومد روی Nvidia وقت استفاده‌ست
👋</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/4205" target="_blank">📅 19:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4204">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NjSZ_C7I8LY0tNGsUk69ArN-7wXLRBv3qmdajLmGGdAIhvc82Au86JJIeUqF7K4lb_4nOU1Wi2dzgx6b7NBMh8kchX2lhwosXq9fw4C5qAq1QAV7ZsnyN3HPz2od94knB7TqYE9YBALmMyFpic6dMSX-91LCOIelXDDO7hMmOT5g7rRamQOHNJt2rRMUn1UTvRNPqremXs-urf5o40G2gMMlDoDHzXuj0Xibux7lyJf20d20UQWvSuJ6L-E2Cz33EuxUlMPMNE6M3z2e99CgutFDiQuD8AVwzmTaLGg8_L6JCj4UQ-QDiRp4ARg-qw4RGPHzy9-4hB1vb9NsvunpDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب دوستان GLM 5.2 اومد روی Nvidia
وقت استفاده‌ست
👋</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/4204" target="_blank">📅 17:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4202">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Q-v0AtcsiX4nUXSNlFCzuW4Cq4A-9CdNr5vnRCeubXxedP8l2i_UcyAc1yPe0P6RMTeev7gzwQNDnYvucQmlAYgALOWXUqcEvfyha9EgDNm_Uwam0bRj82XrdjueoSiwzL7gN39F2JQzISGcG6xzLmIkGrp3qD5lLC0I-3rkl5FlIDP3I15tGJQ6ThqMjZqXf_jqJWrwi9xa045b4JcowiH9QEUQChCinC5Ke70RK8eVqvaTcsmc0ZVSXQHysoloKCl9L9GHa3lsvckBDZhmd5Kb24BDe2k8zTpMrSeWK2wXmAz__jzccLPypwBmuvKyPG6sxrKIx3bZHcDHK2_GCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NHFy2zkUp_5J-v6N6Eddks8cJEshWihWUof924_vHBJnZttmF3oSnKH-ljMMBgyJdFkLtJlY_bM0Adap4A2ToyGrIEL9W3hlEozOSYWeLoBP8bcfjauMtVMqIbsU3aI-3rwfOrxMiCoGqJk6o5tQ43ltCGhF8PPOgbdnFaE4zmbfqtpX_1G8nqfeZXM6RefC7WyUnuyrkU_Is0U1CWGnJU_iRoAFVS6T_YF4epa_8o1z3m66p4vTA8eZiO-3QRjnenXX015j6HFS0_8VqXCxYzSK77MoR-JInKvQHxZay3awMHFWR_bpiC-e82jjNv6h9vCA0HdXikBNakjcg64RrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">چیز بامزه‌ای نوشت اما پر باگ. دیشب GLM 5.2 برام دومی رو نوشته بود که کار می‌کرد همینو الان با sonnet-5 هم تست میکنم</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/4202" target="_blank">📅 17:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4200">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QPPZU0VeOrMLEA00Ir_5d1nZ-nehTC_aMJv6sH0CPtpF-QQAYeD9JwMH50LklsoWyRAfo_IntInEjboyajhC-Y-FjCnBBVlenUF7Lx_GMCUdd9lYlZgKXsSbna0hBTNcNi2yV5ncKtcfU1Z_-M9YkecAkoXmAGHgy1EFLUMtoor5whjc7I8cH9P-_VXnHDMyCNj8z02_Vy8dim9afBZ5EEgJRfqYNd4K4bbmA02d8s96tUwIZQ8I7ar3UGJ-FBesDcu3vsi4wwNv_L_gsYTq-LB7dD_bH-uEadtjdGeofKUctI5ZpTE686NaWxgHnlGH4DTjfAJLx0DD6tttj3rzBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dKDjZnZCkJRGBlnqQD5Khkyv_h-0TBqu0ht2uoffVxai65ZiKWxzkETqP084sAbjNtldDVAnQF8p_2K9EoAZf6jOy585tXx1GMTiMjMZ_fhX7gF9xLO2nSMoHxilnFyI9PuE81bS0kgum0SYsWkgbLA-eNo3K3bNJCoJRP83Zuipwesnkh548BngEkIO0jHxxioNryIB0s8fncNJjoxm4CYh0bK262XNAT1iYz8hajb_PS0tuJEgWoW44eWDPtEafjmIawFhRSTXfJLJAp8yl931qUZv-dj0RPSpVMGzDS8NN7cR4eehpT6nhsx-XkuQuVL05618GnMq8SZYQ9JVTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بریم ببینم با یه تسک گنگ و غلط غلوط چیکار میکنه</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/4200" target="_blank">📅 16:52 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4199">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nqckhItoj7n9rOPj7HYuSOdqJfZjuOx7ueEaxEvsPrTrTrw80xKrzEhWRJv5ik5qWQNS55EctiB-zCqVnG00jQ-11QN-Vzht3imQx0CZYra4vrE6ZTLNhdNUs6t8ytQN6BdJNuWglbeGBnaqFyoMS9AFnwOGl7-cp5sGUgoIvRCwFDvH5CgN1edWrfWy2l0ikJng14o_NSIrj21Rq4mrlK0PNgd7mMOQbTHcOypaOpSRJMPsMSWTDeLJkwQkxGCi_t7EJ09ucS1fZpKIQn5qUE8OqjCmFUQ3ljcmwA8bLRoRaaOsanX7f3esw4RPhGlXqJkE1F4uaxuqNLQ8iQHPFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثلا هیچ فعالیت روزمره ی معمولی غیر تخصصی و تاحدی تخصصی ای نیست که با chat.qwen.ai نتونی انجامش بدی و نیاز به خرید اشتراک chatgpt یا claude یا gemini داشته باشی. البته دارم تواضع به خرج میدم و میگم که qwen صرفا از پس کارای معمولی برمیاد! برای سرویسی که میتونه…</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/4199" target="_blank">📅 16:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4198">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KlLpdKan4muDLcqfcJbDi4wBSoi_AnsZV6fs2e0rjDyO9DD8Bwx2JCqYwxZE2XeylkltA1_ycJtBlHlzGmCjIWGbf6cBdKvPJG0-6JCYfUFrg187MPl7GKLZFizJq2tLOtLri2VrrQcIxAWo7lMzw8li7OKcWqs94Uq9hIzB-AZTVO-yBxHZlNXo2SNVg7b1dqr306Rybx-tlzYTQey325veRevs1Uoz-WPMxOmvnpDMTBF-_7Y9a_vwfDfHoIuT6JEMymYaJODOaOcT8jsbHgix-nzN0v-3a3SucLs9m4RZrbqDAlhBEq8hiYihDQt2RJsj_9aQ8hINHZq-KNLI_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثلا هیچ فعالیت روزمره ی معمولی غیر تخصصی و تاحدی تخصصی ای نیست که با
chat.qwen.ai
نتونی انجامش بدی و نیاز به خرید اشتراک chatgpt یا claude یا gemini داشته باشی. البته دارم تواضع به خرج میدم و میگم که qwen صرفا از پس کارای معمولی برمیاد! برای سرویسی که میتونه پروژه بسازه، مموری زیاد داره، عکس میسازه، فیلم میسازه، ریزنینگ قوی داره و برای هر سوالت یه لشکر ایجنت بسیج میکنه استفاده از واژه غیرتخصصی تحقیرآمیزه.
✍️
بوکانت</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/4198" target="_blank">📅 16:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4197">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">توی مدلهای چینی طبق تجربه‌ای که روی هرمس داشتم، MiniMax m3 خیلی بهتر از Kimi 2.6 کار کرد واسم روی api انویدیا</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/4197" target="_blank">📅 16:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4196">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">به قول یکی از بچه‌ها هر روز جوری با Claude کار می‌کنم که انگار روز آخرمه</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/4196" target="_blank">📅 14:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4195">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اگر ZCode رو نصب کنید(با Zed Code فرق میکنه) می‌تونید روزانه 3 میلیون توکن رایگان GLM-5.2 و دو میلیون توکن GLM-5 Turbo بگیرید با یه محیط کدنویسی تمیز شبیه به Codex با هر ایمیل هم می‌تونید یه اکانت بسازید و... بله خلاصه
🥰
اینم لینک نصبش: https://zcode.z.ai/en/docs/install</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/4195" target="_blank">📅 13:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4194">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GqZzb0lgV1R4oLIysxE6ouVK4WCYKEbT1FYpw3c63qrtWqE5pg8xwN8eJMAaEmg8Dtr1WV1bP8H4vz6ilyQrJFI8fIUZfptvrItHuLSntFbs4i_LCDVTVhj5CVZwrFdl2et8X8_itfwTGHfyAoRcflz4HC_6FjFJbp7Vgjj5D-w1LRa4PVP3iZjqZhw3b4xGBRjmI5dqn7H_6Hd6Et_0h79uDZUKxQXnLKZqYLdi-pb8wqrTxC0AzzQA92bvwdpbrI_fAUKQctwYPShEdLw5YHWzN8uW3QuMC0HxtpL5nseUIl7p7rsE9zMenIMl2O-Mmp3yarPR28ZM6n-EZ6TMqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر ZCode رو نصب کنید(با Zed Code فرق میکنه) می‌تونید روزانه 3 میلیون توکن رایگان GLM-5.2 و دو میلیون توکن GLM-5 Turbo بگیرید با یه محیط کدنویسی تمیز شبیه به Codex با هر ایمیل هم می‌تونید یه اکانت بسازید و... بله خلاصه
🥰
اینم لینک نصبش: https://zcode.z.ai/en/docs/install</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/4194" target="_blank">📅 00:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4193">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hJXwzwZ2tppCO8-rV9lULH33DvAAzy60e2ZIIR8BP_R-m7en7LCwF6vFDJwhPDIgXUqVhZzej1RIwxDiNUQJywkqOInzpf_N2z9B7qJFERKT8MJ-s_I3H8CbgzFk_WGZC5GJSt7NTqmiINZ2ukS5zNWZ16oPfB6ys9UcEu1gd5p0bKMbk93yCYMyWWyTZEbykbDKthDBBZJhiLvFLzKXNLBviKcY9SGLVFmySfOluUSDwyNEmUmbymDYK7e8l4FwGZ0o0lm8Uor65dQ6jVDV9PogmgnU5mYGXupdlU-DDPqflhyDLAmgViAbRTwmjt0K_Kty0IQFFWL8LY9V7d1RMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر ZCode رو نصب کنید(با Zed Code فرق میکنه) می‌تونید روزانه 3 میلیون توکن رایگان GLM-5.2 و دو میلیون توکن GLM-5 Turbo بگیرید با یه محیط کدنویسی تمیز شبیه به Codex
با هر ایمیل هم می‌تونید یه اکانت بسازید و...
بله خلاصه
🥰
اینم لینک نصبش:
https://zcode.z.ai/en/docs/install</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/4193" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4192">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسمپا- آزاد سازی اینترنت</strong></div>
<div class="tg-text">‏DoH HTTP Proxy یک ابزار سبک و کاربردی برای ویندوز است که با ایجاد یک پروکسی محلی، درخواست‌های اینترنتی را از طریق DNS over HTTPS مدیریت می‌کند. این برنامه زمانی مفید است که DNS شبکه دچار اختلال، جعل، مسدودسازی یا ناپایداری شده باشد و تلاش می‌کند با استفاده…</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/4192" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4191">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسمپا- آزاد سازی اینترنت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBgG1KYca-j_WzhXX-uUJCtVR3LinuF0OTHfmXZtSgNYQQ9_6j7N2MSoLDz1SYNIZ__nfdOtcFmkpndTuJebgGSwF5W2cn0ssXObAG6IgJKe_UCrnHY6s08BegN0VrwVfsJJS4gcqZJB1_XPBgVhopc44S6oIZIuEoa0dYK5G4WomGTwHwm4ymgZ79dcCH1DapCMv3DgTBIvVgIfFuCKVWcG2CuLvn0aEaYxuuG7koyFdW4o6Q3Ppy43sYa17YWORR__zHiz20XC3wVN6fa9RV2C7kWiiBwRj3u8hVbUe2CPUbQH-srcweie7CthDyeacaW9--bI9j9A1jR9UwBIIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
DoH
HTTP Proxy یک ابزار سبک و کاربردی برای ویندوز است که با ایجاد یک پروکسی محلی، درخواست‌های اینترنتی را از طریق DNS over HTTPS مدیریت می‌کند. این برنامه زمانی مفید است که DNS شبکه دچار اختلال، جعل، مسدودسازی یا ناپایداری شده باشد و تلاش می‌کند با استفاده از endpointهای DoH، کش نتایج قبلی، fallback و حالت اضطراری، اتصال کاربر را پایدارتر و قابل‌اعتمادتر نگه دارد.
لینک دانلود برنامه:
https://github.com/SAMPA-ASA/DoH-HTTP-Proxy/releases/latest
لینک پروژه
👇
https://github.com/SAMPA-ASA/DoH-HTTP-Proxy</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/4191" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4190">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nhrknGTxNZwkDD5tK0ORdQd_b9BhkWrtjXvZEWmr4UFDEjjDi-6c88ih0_F3Vu44uravagmRAMRrajbvTyTBtJAgaU8363QWPZ8mGMYVdB5618jnOCTlG6-lZSjNpGjJXhkWkBAb0pgJtAfbPgwvAkz9xzcw4aX8q-GrVxZ6BBjF5XrCzIFD06O6wZJazTTIAwf_VzyDoAhXVtf4NNAwVg9wRr1DYfehmW6pBIY9ikQT6DsLCHAAjDyNPlpwLfE-wnGNRd5w1kDEJDdTRqNlh_dJjaho1hrvgAf8RsV4i9YB1ci6QBDBWz-wthfv-qu8livE8dMlQ0-NfjTb5xYZ3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از تلگرام برای ارتباط با ایجنت هرمس Hermes استفاده می‌کنید بهش بگید که تاپیک فعال کنه یا فرمان /topic بزنید. بعدش بهتون میگه که برو توی تنظیمات BotFather و گزینهThreaded Mode روشن کن بعد از اون برای هر موضوع میتونی یه تاپیک جدا باز کنی و ایجنت موضوعهای مختلف باهم قاطی نمیکنه
✍️
Hessamsh</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/4190" target="_blank">📅 23:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4189">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">برای هرمس، 1 هسته سی پی یو و 1 گیگ رم به عنوان Minimum کافیه. اما پیشنهاد میکنم 2 هسته - 2 گیگ رم باشه</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/4189" target="_blank">📅 22:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4188">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B9ZAobDAKiBbAqpQyE5-QziPoCaiziYHbK2efwaJaSHs3pal-72zGHNfOywGhJzmG6WMAZqxLolORPzLrC6WNr_DyBIWVAliIWJuwziE7YnwXUt0mfDC4GbX6WSqozSxlwDv-DFDKwjpxQt9sWoqu8EJFt5fSQIkiTlsWjiOmmg-I3e7hxCgC7R1dGPlNeBibEhfn4RUwbdofZavpJKk8mssrd8OzXhUyZ9QpNZ0AZG_zhKi6rHepinAxTlDs2GXZM7zhk8G6QALztoKS5nm5625C5SONw-96xTrCud50bbYgmfXzm2S_PGXbaq6B2xtRDstz7fsJ_p3J90BQQ-kBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفقا اگر صحبت کاری‌ای داشتید با من، از اینجا می‌تونید ایمیل بدید و مطرح کنید:  matinsp.job@gmail.com  سؤالاتتون راجب متدها و... رو توی کامنت‌های یوتوب بپرسید. این ایمیل برای این منظور ساخته نشده
❤️
ممنونم از درکتون</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/4188" target="_blank">📅 21:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4187">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">رفقا اگر صحبت کاری‌ای داشتید با من، از اینجا می‌تونید ایمیل بدید و مطرح کنید:  matinsp.job@gmail.com  سؤالاتتون راجب متدها و... رو توی کامنت‌های یوتوب بپرسید. این ایمیل برای این منظور ساخته نشده
❤️
ممنونم از درکتون</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/4187" target="_blank">📅 21:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4186">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">رفقا اگر صحبت کاری‌ای داشتید با من، از اینجا می‌تونید ایمیل بدید و مطرح کنید:
matinsp.job@gmail.com
سؤالاتتون راجب متدها و... رو توی کامنت‌های یوتوب بپرسید. این ایمیل برای این منظور ساخته نشده
❤️
ممنونم از درکتون</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/4186" target="_blank">📅 21:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4185">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X_D7RAV42vE97jFivTEnW7Li4q-boPLFt6KGRua7F9eYhUV0UJCS0bU5kJ7ikKbn_PnuUUrPyXbBHASJ-CIaB5SQ1tn3ejNYcXwioEdJAlzMdbfJTJqxy7FnoDejpMZvOxylISChWcb_vdMeftDuZp2jYAShtzTHxEHLAIhKMEhEIhY4sm1y7jxj9F-wrGGQ40AJngkpuOfV2Eor9KYui2mbqIi96yuhLIcSUCembh44yV77GCIIt7pPBCree1dZcd-La8hbN1DSaF0EsAMBbLjRnfKVmyCcH8xzSXf4nJAlZeHnjKG9yJZsv1bdgadZqG3mcs_JaSxzP_IEsXBn0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی هم تر و تمیز و عالی</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/4185" target="_blank">📅 21:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4184">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">فیلم آموزشی Clash Party
https://youtu.be/gMFH88yRghg</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/4184" target="_blank">📅 21:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4183">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سلام خدمت همه دوستان
✍️
سرویس ساب WhiteDNS در گیتهاب راه‌اندازی شد.
✍️
اسکنر های ما هر ۳۰دقیقه بیشتر از ۲۵۰هزار کانفیگ را اسکن میکنند، از خروجی این اسکن تست سرعت، دسترسی و DNS Leak گرفته میشه تا بهترین کانفیگ ها جدا بشن.  نتیجه این تست، هر ۳۰دقیقه داخل…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/4183" target="_blank">📅 21:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4182">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">سلام خدمت همه دوستان
✍️
سرویس ساب WhiteDNS در گیتهاب راه‌اندازی شد.
✍️
اسکنر های ما هر ۳۰دقیقه بیشتر از ۲۵۰هزار کانفیگ را اسکن میکنند، از خروجی این اسکن تست سرعت، دسترسی و DNS Leak گرفته میشه تا بهترین کانفیگ ها جدا بشن.
نتیجه این تست، هر ۳۰دقیقه داخل این مخزن گیتهاب برای سرویس های متفاوت قابل دسترسی خواهد بود.
🌎
ساب مناسب اپ های V2Ray, V2rayNG & ...
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/base64.txt
🌎
ساب مناسب Clash Mi, Clash Party
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
🍏
IOS App
: Clash Mi, Karing
👾
Android App
: Clash Party, Karing
👍
Mac App
: Clash Party
📱
Windows App
: Clash Party
📱
Linux App
: Clash Party
@WhiteDNS</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/MatinSenPaii/4182" target="_blank">📅 21:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4181">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بن شدن حساب‌های کلاد واقعا نگران کننده شده. هرکسی هم بن شده از ایرانیکارت خرید کرده یا سابقه خرید داشته</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/4181" target="_blank">📅 20:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4180">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">بن شدن حساب‌های کلاد واقعا نگران کننده شده.
هرکسی هم بن شده از ایرانیکارت خرید کرده یا سابقه خرید داشته</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/4180" target="_blank">📅 19:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4179">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">☠️
نصب و استفاده از Hermes، آینده‌ی هوش مصنوعی
⚡️
فایل لینک‌های مورد نیاز: https://t.me/MatinSenPaii/4178
⭐️
توی این ویدئو: 00:00 چرا هرمس؟ چه استفاده‌هایی میتونیم ازش بکنیم؟ 04:17 نصب و راه اندازی روی دسکتاپ(ویندوز، مک، لینوکس) 13:47 نصب و راه‌ اندازی روی…</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/4179" target="_blank">📅 17:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4178">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hermes-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">886 B</div>
</div>
<a href="https://t.me/MatinSenPaii/4178" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دستورات نصب Hermes روی سیستم‌عامل‌های مختلف و سرور
سایت YottaSrc:
https://yottasrc.com/
سایت Netlen:
https://www.netlen.com.tr/
سایت Senko:
https://senko.digital/</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/4178" target="_blank">📅 14:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4177">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qHTBkrU-WksOkkTOkvR2wSU2SGfRCbt86GfuP8JMgDbKDwLh0sV97bOy0rGdrFMvHJMrHfQ7tNTZpCM1goY3-87BYZYrG9LlzBwPp1ZKxeExMdFklVVTwCG6yC3Ba8WVYK5rLyPidAtKIZNhaymgDFBW8PDnzotL5wUNQ5ntdYcf50m08Zxr4xjef2vFdpThLN66czcQEdUZd7rLhJYLjyCz71EWQfwCAXfHWDtLozv10In2vC8AYBpp9GC99DxHgtOjmgExKfuIDe2ydcc_no7ImgUUverdlSCalC2wIxDv43AsfxRMBn9uoRAJgyPvAtE2WuiX11r4Qsb3RQUb2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
نصب و استفاده از Hermes، آینده‌ی هوش مصنوعی
⚡️
فایل لینک‌های مورد نیاز:
https://t.me/MatinSenPaii/4178
⭐️
توی این ویدئو:
00:00 چرا هرمس؟ چه استفاده‌هایی میتونیم ازش بکنیم؟
04:17 نصب و راه اندازی روی دسکتاپ(ویندوز، مک، لینوکس)
13:47 نصب و راه‌ اندازی روی سرور لینوکسی
16:46 نصب 9Router روی سرور لینوکسی
18:10 استفاده از API و مدلهای رایگان قدرتمند Nvidia
21:20 دور زدن محدودیت دسترسی به API ها با Worker کلودفلر
22:40 استفاده از Endpoint 9Router بر روی لینوکس و ساخت Combo
24:31 اتصال Hermes به اکانت تلگرام( و واتس اپ و دیسکورد و...)
26:35 نوشتن یه کرون جاب کوچولو که هر 5 دقیقه قیمت بیت کوین رو بفرسته و تحلیل کنه
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به پیش‌نیاز خاصی نداره. دو تا ویدئوی قبل رو دیده باشید، عالیه
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/4177" target="_blank">📅 14:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4176">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ویدئو 2 ساعت و نیم ضبطش زمان برد، بعد از ادیت شد نیم ساعت
😭
دستم شکست انقد با موس اسکرول کردم</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/4176" target="_blank">📅 04:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4175">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MSTU5hwE1MYlkKhp8F4yrACG4Jsv7xmnzASMjy1Bm9o2X1ASIxfkO6wgzv4MQdn-scxkFkdOPiwYwapU528hM2Wn2aBmJsooPTV2nMivctotodT-OvzaUxjogBfyYToE99JWt_zXSG-UMbs16-mBI5l3X5uiRBK__grrPPjAAI5w4PQbboWrmu5fKrghrI187kc5qYdbFy9GdPmmfFS37_7mIqKPK8qm9QcfnaiUF89a0wYQNe0oy1QY2Ri1rQvWqiMoj_eSjovcu5IrDywryMWOlpjZZlI1VV1ygkvu08odDpq7nTtd3qiGT4yT3M-9VgQz_GgcmC5WNyyNtd5sWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این وسط دسترسی به Fable هم برگشت</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/4175" target="_blank">📅 01:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4174">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">وسط ضبط ویدئو به طرز ضایعی یه ۱۲-۱۳ بار به ارور خوردم
😂
(اون پشت حلشون کردم و شما قرار نیست ببینید. هاها)</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/4174" target="_blank">📅 01:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4168">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-Desktop-1.0.0-beta6-linux-amd64.deb</div>
  <div class="tg-doc-extra">19.1 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4168" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/4168" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4167">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUoVEaKLri2IEKB9svC9uxKFhD4y84n38mPSSo0gFKSCHAQxYih0FUE9ij5aVqUC7GOS6kvgw87IJBCM6smNdzaExN-7fSaYCKMs34ah9Cc-JaEuYEULOk_BF2-HrdxuX9bjl285p-ajrVNO7IoMNSslYTSK630NwoDcl_bf8qbCeZRVslLY9pTfP-iemDckgn5a8-75EsmeW0HkbHfZtq4uG9XONcGApfeyd2aqAxdLcGucVAGfmTVZ6FpWdjhL8DLy__d0NMktfx5n-pUV7bbgRyjg6dSBzeo9phYQ4r1fHs3XWVBfPTE7YzinDHwITArQ9NpzmfjCykNDsF_GMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
نسخه جدید WhiteDNS Desktop 1.0.0-beta6 منتشر شد
در این نسخه، ماژول جدید WhiteDNS VPN به WhiteDNS Desktop اضافه
شده.
امکانات این نسخه:
• اضافه شدن WhiteDNS VPN به اپ دستکتاپ
•  انتخاب هوشمند بهترین سرور
•  نمایش کشور و وضعیت سرورها
•  اتصال بدون نیاز به تنظیمات پیچیده
•  تجربه کاربری ساده و روان</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/4167" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4166">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ecMbclJsHLnp86fCxK0Boui1m3JkuRKKDBI1EqzIf9LSE7pUSwwKnMBOqk2MxED3OS_1L3jU4lVh2whI0SazyrtGHf97NIy7JDLLb8cqfH5HX7xzMAB6KTnB-31L6ecGTU-1_Q2--1ufJkqifzt2ibsGKhqQj7aC2EhoW4X6OhO3Tbd50vCWo1EvSjZotXV8m4S0cIeCIqi8IpPphGWaAeKtNR1lcihBVhct_QPq9E4LYnGNw714c48YWjseSaIOSl_BP-84vuKdqKb4cm6l6IzvxOKqpQWOrHehcSOPSWEg3liLAMXpnW2vUzbWT-37wTb8PkJ7YXrJ52mITeexzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این api هایی که Nvidia میده واقعا سخاوتمندانه‌ست. 40 ریکوئست در دقیقه
با 9router انداختم پشت هرمس، چه میکنه این Qwen و MiniMax3
توی ویدئو آموزشش رو میدم که چطوری بتونید وریفای بکنید و ProxyPool هم بزنید که روی سرور مشکلی نداشته باشه(مثلا با آیپی سرور من مشکل داشت انویدیا که با یه رله کلودفلر حلش کردم)</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/4166" target="_blank">📅 22:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4165">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">کلودفلر یه درگاه جدید معرفی کرده که اجازه می‌ده روی هر وب‌پیج، API، دیتاست یا ابزار MCP که پشت شبکه کلودفلر دارید، سیستم درآمدزایی پیاده کنید. تسویه‌حساب‌ها از طریق پروتکل باز x402 و با استیبل‌کوین انجام می‌شه؛ یعنی عملاً دیگه نیازی نیست درگیر ساخت و پیاده‌سازی…</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4165" target="_blank">📅 22:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4164">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ugRY2ihvYs2Vam8C_lGoKvBeTHSsi1HRtV3UVI-kjByzmKoXcXGF8ysW9rc--MQLpG6pnkXZtZ3X7kaXUwBLk3lHhk41pzSJR73KmTQvg55h4K5tT--iyY1YwJn4bG5_seWbTtTHFgfRtBp2HZHcejvem96eX3QO9L1xShuOMNvJEN9RXxUvQb6ViQLrhgqkiIQkJGPyKJuAvDbXIMCYVFCVu3o2-Ydv45a3Cydy2JD187CfZlYk3yJgl7EOcv65CHwQfoWYikad0jmi9LNTyRhHw_eJJe2j_PHab7Cy27AB-7GjTeG4bjpWh3MC6FbrMZIIdnEfKg5rBKg5DrIg-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر یه درگاه جدید معرفی کرده که اجازه می‌ده روی هر وب‌پیج، API، دیتاست یا ابزار MCP که پشت شبکه کلودفلر دارید، سیستم درآمدزایی پیاده کنید. تسویه‌حساب‌ها از طریق پروتکل باز x402 و با استیبل‌کوین انجام می‌شه؛ یعنی عملاً دیگه نیازی نیست درگیر ساخت و پیاده‌سازی زیرساخت‌های پیچیده‌ی پرداخت هم بشید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/4164" target="_blank">📅 22:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4163">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">از بین سایت‌هایی که تست کردم برای SMS، کاوه نگار که باید میرفتی از دفتر اسناد رسمی احراز هویتشو انجام میدادی، فراز اس ام اس هم که شیش ساعت گشتم اصلا بخش API پیدا نکردم. بیست دقیقه وقتمو تلف کردن این دوتا تا وقتی که رفتم
sms.ir
و همه چیش اوکی بود و 10 تا هم پیامک رایگان داد. خیلی هم سرراست api تنظیم شد از خارج به داخل هم دسترسی داد</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/4163" target="_blank">📅 21:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4162">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">تمام رادار جنگ الان فعاله و AI هر نیم ساعت یه بار، خبرگزاری‌ها و پنج-شیش تا کانال تلگرامی رو چک می‌کنه و اگر جنگ شده باشه و اسرائیل و آمریکا به ایران، یا برعکس حمله کرده باشن، پیامک میده</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/4162" target="_blank">📅 16:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4161">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PmB-Myd6xPKe-86TUe-37vzMw0Sy_2V7GBm5JduMy32HDoVc-QC0Git1_ks9KR1ZEvWj5EiGnRciuXbfDo3bQBTz5mI8j8seWG0hUWK2VguEUDm1SiCMdd-pEzDcP-_aREGJ8w25wsKdXbFMbulUxcaX8fUIesurHG-Z5D9Z3cbLM-IEbKJ6nTEQDjezZxhOFVl8UCMSKWKKaeWd88DjXNQ6oD-doix7Gtyb5B5z1kSUMlbxUE4W62r-p9GxpY_3PX3kNjRYKa27bZB17cdAvO6X4_802ibwi84aqnA5OKZP0EiT6I7ipxVP1Z49e6D-xiLo-yO7NYSMhkb_6LqKfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌خوام باهاش یه رادار جنگ بنویسم</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/4161" target="_blank">📅 16:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4159">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">می‌خوام باهاش یه رادار جنگ بنویسم</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4159" target="_blank">📅 15:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4158">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qt0H_ZAtdM_jmDCzcTVOm4LWhuYfZS_ZAqsw3xVeySh5jzERMQWeg2SONXVhv3kwGMiT5zG0Vka-0135myegDDjGMawiKNpiM99iW8r1ODMlD5Z2-SLvW_ft9-X4eukLYb4tDJ8R0fFNWbAWn4i98u6_JCCMO4uYdRkdH4I2e3cbcpGOA2Ue2Msarec1OvwXeW_ltBymZOHZmUDQovw-Z7arB7h8TBpuxxSwdSdMvaEkU9eWG5J3SmTcql17aVQnmDk9OrDy9KRZ8KZSaw1ZgVXryo3s7hJcpAgCUJhb-yuTsV3nvCG9VJ3UzzLWcR8K7mXlUkSXNa82WztfNyYuJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمی برای خود یادگیری را شیرین کنیم
(دادم همه رو هرمس با gemini 3.5 نوشت چون هم یادم میره چی رو تا کجا دیدم و هم همه‌اش هی چک میکنم که چقدر ازش مونده و الان درصد دارم و اعصابم آرومه)</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/4158" target="_blank">📅 15:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4157">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">می‌خواستم ویدئوی هرمس رو ضبط کنم اما انقدر برق نوسان داره و هی سه راه قطع میشه کلا برقش، اعصابم داغون شد. می‌ذارم یه کم برق بهتر شد میگیرمش آموزش رو</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/4157" target="_blank">📅 14:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4156">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">همین الان ویدئوی یاشار عزیز رو دیدم، و باید بگم دیدگاه فوق‌العاده‌ای میده به شما از ai
اینکه دیدم یه سینیور چطوری بدون گارد و با آگاهی و مطالعه‌ی کامل از ai استفاده می‌کنه توی حوزه‌ی خودش، واقعا لذت‌بخش بود.
نکته همینجاست
با این ai عزیز دل، حتی باید بیشتر از قبل مطالعه کنید و دانشتون رو بیشتر کنید تا برتری داشته باشید نسبت به رقبا. و قوه‌ی حل مسئله‌تون رو تقویت کنید و کارهای تکراری یا سنگین رو، به راحتی بسپرید بهش. اگر به مبحث باگ بانتی هم علاقه ندارید، ۱۵ دقیقه‌ی اولش رو ببینید حتما
https://youtu.be/-Rt_Z0allhM</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/4156" target="_blank">📅 13:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4155">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">متا قراره برای استفاده از عینک‌های هوشمندش ریت‌لیمیت بذاره
😐
و یه مدل پرداخت (soft paywall) داشته باشه که باید ماهیانه اشتراک تهیه کنید  لینک خبر
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4155" target="_blank">📅 13:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4154">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WOn5TrUopjfz3WrgWzQWJ5bfIoeW-JHpp2FtpNYBo3STBqgTVIA3ZZ6rTWHzaeMPfLW_WM3s-si4BIjzTFPe-29RVbDs7QhNLJno2Jrmcr-xle8XJTTAGA5oM1Ex0-A5r9w1pp2xzSHOzDQexWoLC9vmPvO_z5Eg4vJQ9cNdw_fudtJNqDdRBq4bFYVyR4yEUkkasTBBH0cTeak9WPLdqOkWKY2re0J6e6ebiAZpeCE4AergU89aqX6P3r-jJPQLyFlgwWD5C3xWU8-a-0ZjaPMEmOxe5X8pVdbtB-fYjTAWquvIJfPcwX5dZwQzGSclFNnqkPe2aRfoyBuLr7Cytw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متا قراره برای استفاده از عینک‌های هوشمندش ریت‌لیمیت بذاره
😐
و یه مدل پرداخت (soft paywall) داشته باشه که باید ماهیانه اشتراک تهیه کنید
لینک خبر
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/4154" target="_blank">📅 13:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4153">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/guGFjFcmCNqnhaZBhIgdF_jtH6sFXPXOlw2QS9GKyAF4aFcJ6wbzoAvVeXN_qT5KKos1QjImIo5exD_2ZFFWt03tYrPlNhg2y7olUlOCko4Gt1RyBIGctf4Q_eznjquYbnINaOfai6mYFl8dpAFZIsZbNkms-1uQG5BCkqbdEKJt1NJoPHacrr3Nr4v0Lh4C21AKxJ5G7CpTTM4gdbukkzPTBVcIpdcJC9Bjm4JyNN1sCfoo5jsyD2sAtpDZf9GSG8eASe8-klmINUXvwpflnD7AMtOWN4Bv68stCSGxZ4Cc0X7DgY1kdR4y1IizU79wo6maalnrzrfjZEZjuqSXvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غول چینی، GLM 5.2
همچنان ارزونتر از حتی Sonnet 5</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/4153" target="_blank">📅 10:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4152">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">خب گویا کلاد Fable 5 امروز برمیگرده
😁
آنتروپیک گفتش که با دولت آمریکا مذاکره کردیم و امروز مجددا مدل رو آنلاین می‌کنیم</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/4152" target="_blank">📅 10:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4151">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NE4ZqtyGeI1wSs3Jbtc4PjzYLXIr9cat016OwKxR2z4e-Ca2WxFGkv6UkKvHCnJseJod3aPsk54JtPglN1PmIBSTLf4cU_M_Nh5MqQmiZJoj2pHbgmT8WaGSXYsuF5LVJsdnCfJUhPrfFWQ5agpbt-L19P7hhFy5_CNTUJqHat_9tUpIzloQT65XumqxZFWsS9F9NfxVafwAG-2YjvHvvWR7OqNdhijNhR1rTCmTUy4cavUEbSebOPAhsqTISNDC6vuS9SlBQvPY3AIxOf29SYzswiKq4Ebv2fS75zUkskmtjDJwYDULAVv1ZQ3YPCPZqGZ2ZJTwq-rNy4SMnuNNZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انقدر هوش مصنوعی‌ها چند ساعت اخیر آپدیت دادن که نمیدونم کدوم رو برم تست کنم
😂
وضعیت عجیبی شده</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/4151" target="_blank">📅 01:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4150">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">انقدر هوش مصنوعی‌ها چند ساعت اخیر آپدیت دادن که نمیدونم کدوم رو برم تست کنم
😂
وضعیت عجیبی شده</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/4150" target="_blank">📅 01:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4149">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f2ffa3ab51.mp4?token=aS0XtgjksWQ9xkBurAvP-rm6eYc2DcUhCoJT-uk5qvrdkCRxGgARK68yUHAhfon3CZibSVpAIeTZzfrW-pyGUCRUM2rf-RZEWWipdHewDkloJLnCisqaRe1-VBBiagsEoxvzp66hrX3DyvOVM97HgrnYpbr7BD0gPbjlTs2v7xWBCOlolXwff2HHkR9Me4dDainGD2vbbmUOx9K0Lo5Oz70GnBkgLTCewwbr8kXR_aSwJvEanMq13LJNgHAoCSd9GZmticN5ZsZPN_KGDeBzWgvlmAV5dUwXCwvEUHLvdIUCX3Fd2TuwCkFslLqFtn04oD1F4yc98qyYNtYX50uKVA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f2ffa3ab51.mp4?token=aS0XtgjksWQ9xkBurAvP-rm6eYc2DcUhCoJT-uk5qvrdkCRxGgARK68yUHAhfon3CZibSVpAIeTZzfrW-pyGUCRUM2rf-RZEWWipdHewDkloJLnCisqaRe1-VBBiagsEoxvzp66hrX3DyvOVM97HgrnYpbr7BD0gPbjlTs2v7xWBCOlolXwff2HHkR9Me4dDainGD2vbbmUOx9K0Lo5Oz70GnBkgLTCewwbr8kXR_aSwJvEanMq13LJNgHAoCSd9GZmticN5ZsZPN_KGDeBzWgvlmAV5dUwXCwvEUHLvdIUCX3Fd2TuwCkFslLqFtn04oD1F4yc98qyYNtYX50uKVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شرکت Anthropic از Claude Science رونمایی کرده که به صورت اختصاصی برای مراحل مختلف کارهای پژوهشی و علمی طراحی شده.
توی این نسخه محقق‌ها می‌تونن کدهایی که مدل می‌نویسه (Artifacts) رو به طور دقیق ردیابی کنن، محیط‌های اجرای کد رو بر اساس نیازشون همون‌جا بسازن، و جالب‌تر از همه، بیشتر از ۶۰ تا دیتابیس معتبر علمی رو مستقیم به کلود متصل کنن تا تحلیل‌ها روی داده‌های واقعیِ علمی انجام بشه. این نسخه فعلا تو حالت بتا در دسترسه.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/4149" target="_blank">📅 01:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4148">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9603918fce.mp4?token=BHpWL2XWKEw4aocJe5LsRpFPNU9DJBimfq4vYQ-Iygn5uXgLZIEDD3_Il-Lf3v_l25lx996qAwl3p1Q4FSXKoR2ZzodLONdDKDnekwjT-GPXGWen36V4LK1HPRoIWCHm60EMgCyoph9FP17t95X2l8YDBzzAfjLqQmlhQt0VOrQXVbp9eVkrsQCAb6KT7mLVVgzZ4WprEsDqAd5Gq5nhgNxpMsDYHgMp7eegvbAn0gTImgw1olTftWC065AdLjNBGdZnHZPMf90HmkX23CGuxDx4d5hILJA6O1I2KYcRT5uAk_Z-MTLfpAlLRxhPMBCzuduITrNaJaPfxaWwhj8dpg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9603918fce.mp4?token=BHpWL2XWKEw4aocJe5LsRpFPNU9DJBimfq4vYQ-Iygn5uXgLZIEDD3_Il-Lf3v_l25lx996qAwl3p1Q4FSXKoR2ZzodLONdDKDnekwjT-GPXGWen36V4LK1HPRoIWCHm60EMgCyoph9FP17t95X2l8YDBzzAfjLqQmlhQt0VOrQXVbp9eVkrsQCAb6KT7mLVVgzZ4WprEsDqAd5Gq5nhgNxpMsDYHgMp7eegvbAn0gTImgw1olTftWC065AdLjNBGdZnHZPMf90HmkX23CGuxDx4d5hILJA6O1I2KYcRT5uAk_Z-MTLfpAlLRxhPMBCzuduITrNaJaPfxaWwhj8dpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نسخه جدید Hermes Agent سرعت خوندن صفحات وب رو ۶۰ برابر بیشتر و هزینه مصرف توکن رو ۴۹ برابر کمتر کرده.
تیم توسعه‌دهنده‌اش، Nous Research،  با حذف پردازش‌های میانی کاری کردن که دیتای تمیز مستقیماً از بک‌اند به ایجنت برسه. همچنین برای صفحات طولانی و سنگین، داکیومنت‌ها اول روی سیستم کاربر ذخیره میشن و ایجنت به صورت صفحه‌بندی‌شده و فقط در صورت نیاز اطلاعات رو می‌خونه.
این تغییر یعنی کیفیت تحلیل و پردازش هیچ افتی نمی‌کنه، اما زمان و هزینه‌ای که بابتش صرف میشه به شکل چشم‌گیری کاهش پیدا کرده. و یکی از نقاط ضعفش یعنی مصرف زیاد توکن رو پوشش میده!
کم کم تیم Hermes داره یکی یکی مشکلات محصولش رو برطرف می‌کنه و امیدوارم همین شکلی جلو بره
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/4148" target="_blank">📅 01:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4147">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l9REUXuN6Kcu3B8Df8vTPU9hNGbRt9ggUyWsIOkdW_2rFrnzIkVj1GlTDNNQQEyyKJMQTgHabjIA1fTOZ8e0jL_DD9_hQ-VHQ8DFXylVXknRFKGsR9FI7kr00ojk0Ld_8OvekOe3IFBPsgxiwq9enBBBJm6PK-jEHJFyw7bHoxfv1D2Oqkb2VZ7_ev0dUs0kBpTKRoGb-OKLinhWdLRWKPkhtkOH1JX5DF2Cyx63xL8qNJ9JNNqqkUKDJeACEvHV2QnX8Nrub8wSCVe6bxoZmn-VP1pvjdgToaOapitmMCmCvTqdntT369Y27gd5R-7o7fKIogF8Xv5gqKjZwBZjOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم بنچمارک منتشر شده توسط خود کلاد</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/4147" target="_blank">📅 23:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4146">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nYGBUcLCtjZ0hQS0QeGDU2BYu37zwd0TYK-Csx50fCNu_PMG9nNCdS_qoTggbX0OGWinJk2DlhTY1U5arWMdguSwVb_AzCEGG37gKTemsQogkRl8pfYTBsCep35LkiF_Zc51pvEcsDs_nROfvcHTBcbINa1bye80QGhYhX_6DMigph-fOVF06YnPKn1BHkTAZAgQTxLUq3Oldm8IaZl5wbEUySRYvURxxhZ4sSH5Fx-Z3ZxQ7AQ0rvFXMBAOfBoSk74Vk-9Ey95zck0BohMrSqVlqbvRgJnQLiHsfvSv9p8-PdwXb6cT_38hyTmwiaTRETMoFUa0T_nzG_OhM9EaZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم‌الله‌ آنتروپیک Claude Sonnet 5 رو معرفی کرد همین یک ساعت پیش</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4146" target="_blank">📅 23:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4145">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IWpghatrwI-60q8EiTgn0gqBiXMgRBCUTJQ0Ex6kdDJ7jdQLrXgK-UMDI9A3cN6oRdo0h4Lk89V_7lwJSmJA_DH1UF0hQSBDvJ2F9WrEgt74O6_FQtYZYSxW3hmF5TdDpFX04bMJoLkgPW9iMoZm6Hf09CXQr3hoWyb9BiX528ELOXle3C0v62T5BoIiN5EvUaUXBiEbjku5eB4s7NOkKZMDte2Ci4CFKvGcX12wIVYBKe4-e5FuhyBN_kB1XSKR93mx0Osl4w7Py8FWs2P-bGtUXr5xaOw-cbNycvL425AVB5Y8S1qRskAoAzduWwic1VF9BzMq7NSgBYXoIkfC5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم‌الله‌
آنتروپیک Claude Sonnet 5 رو معرفی کرد همین یک ساعت پیش</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4145" target="_blank">📅 23:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4144">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">پولسازی از طریق کانال‌های انیمیشن کودک با کمک هوش مصنوعی!
🚀
تا همین چند وقت پیش، ساخت انیمیشن برای کودکان نیاز به یک تیم بزرگ (نویسنده، صداپیشه، انیماتور و موزیسین) داشت، اما الان با ابزارهای AI، یک نفر به تنهایی می‌تونه یک امپراتوری محتوایی بسازه!  این ویدیو…</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/4144" target="_blank">📅 23:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4143">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAiSegaro👾</strong></div>
<div class="tg-text">پولسازی از طریق کانال‌های انیمیشن کودک با کمک هوش مصنوعی!
🚀
تا همین چند وقت پیش، ساخت انیمیشن برای کودکان نیاز به یک تیم بزرگ (نویسنده، صداپیشه، انیماتور و موزیسین) داشت، اما الان با ابزارهای AI، یک نفر به تنهایی می‌تونه یک امپراتوری محتوایی بسازه!
این ویدیو دقیقاً به شما یاد میده که:
✅
چطور کاراکترهای ثابت و باکیفیت طراحی کنید.
✅
چطور با استفاده از AI سناریو و موزیک مخصوص کودک بسازید.
✅
چطور انیمیشن‌ها رو با صدای کاراکترها لیپ‌سینک (همگام‌سازی لب) کنید.
اگر به دنبال یک بیزینس مدل جدید و پولساز در حوزه هوش مصنوعی هستید، این آموزش گام‌به‌گام رو از دست ندید.
ویدیو با حجم 300 مگابایت اپلود شده , از طریق نسخه دسکتاپ تلگرام میتونید با حجم کمتر دانلود کنید.
〰️
〰️
〰️
〰️
〰️
〰️
در صورتی که مایل بودید میتونید از لینک زیر دونیت کنیدتا قسمت های بعدی و موضوعات بیشتری پوشش داده شود.
🌎
donate.isega.ro
〰️
〰️
〰️
〰️
〰️
〰️
📽
زیرنویس فارسی
🌐
ترجمه این ویدیو با وب‌سایت
isega.ro
انجام شده — حتماً سر بزن!
📌
برای دیدن قسمت‌های بعدی کانال رو دنبال کن:
📺
🌐
@AiSegaro
🚀
هر روز یک قدم نزدیک‌تر به آینده‌ای هوشمند!
📤
بازنشر آزاد با</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4143" target="_blank">📅 21:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4142">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J2kKHGUxztORaeX8yLL4s8qLQLshznxN-sxA8YOy_sVO_FwD6qlg0PLl5E3GNhht83miWoUr62o8HBKsJN-5z4Bi-96wqgR4eL5pqHDHL83H1wMe50hv1bTvLWm6db1A-ab83FRLte4JBYxAcrQ2LkTPu_wpYTTIXjQ1PSHeUY_289x9qi7COAQGZOYsVVRZE0OAUwYdvXxPr_gQodhNb0Vdt0gq2mRCKH7hKSFWWNv3sE4FXwfUAG7YRLWDMsMu6xCw3D8tcJE8M_jGFMe3LAu6mQefGkWwwWK8zVkKIzVon5K1S3gZMNIcIBDSgTqhBpnQzbf_IdYrn7OWspc_lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوتوب یه قابلیتی آورده به اسم Ask پایین ویدئوها، که می‌تونید وسط ویدئو اگر جاییش رو متوجه نشدید از جمنای بپرسید
🎨
فعلا برای وب فعاله گویا</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/4142" target="_blank">📅 21:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4140">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">برای نصب کردن 9Router روی سرور اوبونتو اول sudo apt update && sudo apt upgrade -y curl -fsSL https://get.docker.com | sh sudo systemctl enable --now docker و بعدش این دستور رو بزنید docker run -d \\   --name 9router \\   -p 20128:20128 \\   -v "$HOME/.9router:/app/data"…</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/4140" target="_blank">📅 18:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4139">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">☠️
این شکلی از هر API ای استفاده کن برای هوش مصنوعی🫪
⚡️
لینک سایت 9router: https://9router.com/
⭐️
توی این ویدئو: 1- یاد میگیریم که چطوری از اینهمه API Key رایگان استفاده کنیم 2- ابزار 9Router رو نصب کنیم و این API ها رو اونجا جمع کنیم 3- کلی API رایگان…</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/4139" target="_blank">📅 17:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4138">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">انقدر برق رفت و اومد و نوسان داره روی محافظ میترسم لپ تاپ و همه چی بسوزه آخرش. آقا بیا قطع کن همون دو ساعتو، نخواستیم</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/4138" target="_blank">📅 15:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4137">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">بیشترین درخواست توی یوتوب و توییتر ازم این بود که آروم تر صحبت کنم
😁
من فقط نمی‌خوام حوصله‌تون سر بره یا وقتتونو الکی بگیرم
اما از ویدئو بعدی سعی می‌کنم شمرده شمرده تر صحبت کنم</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/4137" target="_blank">📅 14:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4136">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/We0B3DvFMDLPAPUssqQVj5GxY28wJXRHuOJh1DH26xx6EJtwUMNaUHvySdpGUEXh5YsOrq_R_xR9TMn_6rLn59tbMSqi3g84oPJXgtp9q726mVOUsd4ZTWNYJXRQlteXDmVfyL1ojv__uaG9c9zRN8f--n-vg8v8Yd7hHv6xZpm0A0QGnUhr8jOxCvMb9YiIWUMvuqgqZMMLgQhRLNwAz4H2E8_2aLZ_37SlQDH4fhWvQNiCLlHYhGQeYA4MjoSR-W_VflIYEJ3lUIm0oJY6ATWyq-mOSrEFYjSVD2w6htbKI6-xIeZwt8_D83yeVApiVNGigfuiSFURgu6szzAPQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مورد نسخه‌ی موبایل Hermes، من توی ساب‌ردیتش دیدم که یکی واسش نسخه اندروید ساخته و Pull Request زده روی گیتهاب(که کدش ادغام بشه) منتها هنوز، رسمی منتشر نشده</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/4136" target="_blank">📅 14:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4135">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4135" target="_blank">📅 14:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4132">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SDx_RTAOFoPg2y8NUj3-_JTp8y9gXAxvBN5XCSSAJasqXFXgGnDqw6adKstwIkx_RtMVAvlu7Q9SCtSDOHsuqBCIrvZ3Jg_9vX5WSsGt60dFkWb7o08fyv1mgDlUYq7ifsCNoseDsLxot8GJNFvvaL1l5Sgv0-1LPjsIc3Li7gmOgyD_abN8ymklYgCEpsWqpBC3d_1bbN8SoHaS0sAOvLhpw4I-ZlWdGJtMOlI_pxI7rzLcU03X9X4OdxN2SfKAqjXoB_AAGEcFqgEv9hmCAYiiyHUuVmaKawq_rHBwGOf_xyOp_09KB_Wtoz9o0N10ii-mnozhrldDfIffpLgz7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SrKvEtaL_A56fGHSMFYHTkfSeHwFGfC3TNdwd97fmVjNAdStbXVTsxrhKscDhdJG7DqT5wF_yJmWA8ivudnfVRjUNcOQePjoxh0tesIhvtZ50d1Phvrs9w4aSNUaAT4eKgOWX7bKZBUTM63PfF-KqcEHxeRDjN-niBwVOzgHrtXpEIaXgq06Sd692WufQfe1cPcUOM1mPKCDuoSxCQCt3EnesbT74EItj8ChkhUP5S8onRCcBo7cT9UiIEdxzprcACGa2qPAVP7dNKfZknBSAAOzQ0Bli-vWOiNuFbbV2tCRGDsWH-UFz0tQssskR1zQ7LGyLm9FkmZEzGUsb6qj3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LrXsh8J4HR0Pd6jjG71xCxeHcT9CQmnODT4P8lsbtJGK4iZyfCQgvB_fcTJxAAxk8YhEaCrzuVYu24coua4GrBzufN-BiGSNKQcvYB1HEBqTPGuw1ILQFVMy8__RmdE8ItxdVkBuHgfQDpLaMqQHs85mt8cNaApz1Ff0DCe1KBWQ-sy0MBppd5buxEr3-WjU4nGa0jr8YlikldlC2_RgKdboRNJGwoTVtnGwI7-t5wWGOZrHol2A0SuPvR-wwnjvR7hwpTttXQNMB5HoXmQ2e5Il73wymOYB9QUxAvHWQuzoAVtFV2ekby4Veumo2LbGfiMqtOJ8Ja4bJiwaHz1omg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">واقعا Hermes و وصل کردنش روی تلگرام، یه چیز دیگه‌ست!
فقط کافیه ازش بخوای، و بوم
انجام شده. ویدئوی بعدی، هرمس هست
👀</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/4132" target="_blank">📅 13:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4131">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🚀
اسکنر WhiteDNS  اسکنر WhiteDNS ابزاری برای اسکن، تست و مدیریت آی‌پی‌هاست که در دو نسخه در دسترسه:
💻
نسخه دسکتاپ مناسب برای اسکن‌های سنگین، سریع و حرفه‌ای؛ مخصوص کسایی که می‌خوان تعداد زیادی آی‌پی رو بررسی و تست کنن. https://github.com/WhiteDNS/WhiteDNS…</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/4131" target="_blank">📅 08:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4130">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WL0o9OnRvGYgZdZQVD1larNH1jBNMMq5BOtSSm1k3VKNt-_QszNHQlCwjGN4jdnoFw2qnbNSJ1i3uGjj1DjoUwXkJQRWroY7gVA9ATNgfCWM4qRgPavtrMpFIXlRctJH1Sv_PTZXr0XYxQgvFXX9KMHaIYZz2mjMD-JhR6p8PKCst2xhQ-8u3rvqME61hEo-rbYd791N1Br1NGS739vVh0LMlCyr1f5Hir7xNmYoZM9kPExiRlq2WlLRLg_3MnFQLXPT7OTCZpyqkPX-Lv7Z6q2PPBMWM0dSkTBlT9_s9oKW_0ZmUMWhwbUUwX6_BUYTPwJjPGAv9gjR7nDHIBgbuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
اسکنر WhiteDNS
اسکنر WhiteDNS ابزاری برای اسکن، تست و مدیریت آی‌پی‌هاست که در دو نسخه در دسترسه:
💻
نسخه دسکتاپ
مناسب برای اسکن‌های سنگین، سریع و حرفه‌ای؛ مخصوص کسایی که می‌خوان تعداد زیادی آی‌پی رو بررسی و تست کنن.
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/v1.3desktop
📱
نسخه اندروید
سبک، بهینه‌شده برای موبایل و قابل استفاده روی گوشی، با امکانات کاربردی نسخه دسکتاپ.
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/v1.3
⛏
قابلیت‌ها:
• لیست آماده از ASNهای ایران و ASNهای معروف داخل اپ
• امکان وارد کردن لیست آی‌پی دلخواه
• Health Check برای توقف خودکار اسکن در زمان ناپایداری اینترنت و ادامه بعد از پایدار شدن اتصال
• ادیت یک کانفیگ و ساخت تعداد زیادی کانفیگ روی آی‌پی‌های تمیز با چند کلیک
• استخراج آی‌پی از داخل کانفیگ‌ها
• تست سرعت دانلود و آپلود آی‌پی‌های اسکن‌شده
• انتخاب پورت از لیست آماده یا وارد کردن پورت دلخواه
• لاگ پیشرفته برای بررسی لحظه‌ای روند اسکن
• خروجی کامل و دقیق از نتایج اسکن
متدهای اسکن:
⭐️
IP Scan
برای پیدا کردن آی‌پی‌های تمیز از دیتاسنترهای داخلی و خارجی و استفاده در کانفیگ‌ها.
⭐️
HTTP Scan
برای پیدا کردن آی‌پی‌هایی که امکان استفاده به عنوان پروکسی HTTP رو دارن.
⭐️
SOCKS5 Scan
برای شناسایی آی‌پی‌هایی که می‌تونن به عنوان پروکسی SOCKS5 استفاده بشن.
⭐️
SNI Scanner
برای اسکن دامنه‌های موردنظر روی لیست آی‌پی‌ها و پیدا کردن آی‌پی‌های مناسب برای SNI Spoofing.
⭐️
Speed Test
برای تست سرعت دانلود، آپلود و Packet Loss آی‌پی‌های اسکن‌شده، همراه با رتبه‌بندی خودکار.
این ابزار برای کاربرهایی ساخته شده که می‌خوان با دقت بیشتری آی‌پی‌ها رو بررسی کنن، خروجی تمیزتر بگیرن و زمان کمتری برای تست دستی تلف کنن.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/4130" target="_blank">📅 08:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4129">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5950435463.webm?token=p7zfdYMvcix2dfnLdGgFcsD5O_9T0T1dG-9wNkVhm8G4s9_lQ8ZW7ZIpJyYb44hN6ogNrQaXa5UoYpXIWJsqWTKM5SZgytL9WCAeD6w80QzszvoBeNgftekBkQN3Jtn0Y0cNa_NnIcVCpGnJjnFvcW333OanT52Uxrng4O8whThVwhUf3qjOFtJFjeMazGbVy9xoUfw2AkaYqWSHaikMku1Q1lSPaubluaunI9RWHyITFPV82Wzw0r5AHvqfpJs2Zqqrf7eT21o8Qq4MsNyP_VysPPj7XcKGHHIBP2UfTQxcCpDl2JNZQSNegzFPNnah1ptt_BsjFl9fv00OblhtqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5950435463.webm?token=p7zfdYMvcix2dfnLdGgFcsD5O_9T0T1dG-9wNkVhm8G4s9_lQ8ZW7ZIpJyYb44hN6ogNrQaXa5UoYpXIWJsqWTKM5SZgytL9WCAeD6w80QzszvoBeNgftekBkQN3Jtn0Y0cNa_NnIcVCpGnJjnFvcW333OanT52Uxrng4O8whThVwhUf3qjOFtJFjeMazGbVy9xoUfw2AkaYqWSHaikMku1Q1lSPaubluaunI9RWHyITFPV82Wzw0r5AHvqfpJs2Zqqrf7eT21o8Qq4MsNyP_VysPPj7XcKGHHIBP2UfTQxcCpDl2JNZQSNegzFPNnah1ptt_BsjFl9fv00OblhtqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/4129" target="_blank">📅 04:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4128">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">☠️
این شکلی از هر API ای استفاده کن برای هوش مصنوعی🫪
⚡️
لینک سایت 9router: https://9router.com/
⭐️
توی این ویدئو: 1- یاد میگیریم که چطوری از اینهمه API Key رایگان استفاده کنیم 2- ابزار 9Router رو نصب کنیم و این API ها رو اونجا جمع کنیم 3- کلی API رایگان…</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4128" target="_blank">📅 03:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4127">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N3nUbfrYcAJRSbtKKtNm8yx0-JRwMy75pLd53QRz3wFWgWkZl4Ls2SqtKDvnRktzWrR7LJU4qUfseIeb5S1iOgENQKjI6fwqiiTqVQ48r9p3xu2BUDYWNj2dF1Ai_KaH4t6rKhtyY2jWb8QR7-dJihLQNyfhPDsEMjMOKMp0zmMANABn_ARR9Cjp7UPrmlcEUbeRGkyQhEjV0e_je_apcKs8ENwqxi0pWG0NXJT1hNn1ISD2ACMhBqatbi-MoBKyJBYltz4YvqRpk4ZP5ecGvy2ajrwJidtK0n2KxCY3tTNfHZ9E0ohoFAsAN0IhlRRIHkyrInRJyN_mZ4k-daQ1WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
این شکلی از هر API ای استفاده کن برای هوش مصنوعی🫪
⚡️
لینک سایت 9router:
https://9router.com/
⭐️
توی این ویدئو:
1- یاد میگیریم که چطوری از اینهمه API Key رایگان استفاده کنیم
2- ابزار 9Router رو نصب کنیم و این API ها رو اونجا جمع کنیم
3- کلی API رایگان وصل می‌کنیم بهش
3.5- اگر تیک آبی توییتر داریم، به راحتی از گروک 4 و اگر جمنای پرو داریم، از AntiGravity استفاده می‌کنیم
4- از امکانات 9Router مثل Combo استفاده می‌کنیم و چندین هوش مصنوعی رو توی یه مدل فرضی کنار هم میاریم
5- به ChatBox و افزونه Cline وصلش می‌کنیم که هم بتونیم عادی چت کنیم، هم بتونیم کد بزنیم باهاش
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل رایگان و ساده‌ست و نیاز به پیش‌نیاز یا هزینه نداره
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/4127" target="_blank">📅 03:33 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4126">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">وسط ویدئو متوجه شدم اگر کانکشنتون با api ها خصوصا جمنای قطع میشه هی، می‌تونه مشکل از proxy-ip یا آیپی تمیزتون باشه
گفتم این نکته رو بهتون بگم</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/4126" target="_blank">📅 01:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4125">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">کمی ویدئو API بیشتر طول میکشه تا آماده بشه
صفر تا صد تمام API های هوش مصنوعی رو میگم بهتون
محتوا رو فدای سرعت نمی‌کنیـم
🥰</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/4125" target="_blank">📅 21:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4120">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.8-arm64-v8a.apk</div>
  <div class="tg-doc-extra">18.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4120" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⭐
نسخه جدید WhiteDNS VPN 0.0.8 منتشر شد
میدونم آپدیت کردن این سرعت یکم برای هم شما هم من سخته. اما تونستم دقیق مورد رو پیدا کنم و فیکسش کن
ی
م.
ممنون از تمام دوستانی که نسخه‌های قبلی رو تست کردند و مشکلات رو گزارش دادند.
⛏
در این نسخه، مشکل لود شدن بعضی سرویس‌ها مثل یوتیوب و اینستاگرام برطرف شده و اتصال‌ها پایدارتر شده‌اند.
✍️
از همه شما بابت اختلال‌ها و مشکلاتی که در اتصال داشتیم صمیمانه عذرخواهی می‌کنیم. ممنون که همراه ما هستید و با گزارش‌هاتون کمک می‌کنید WhiteDNS بهتر بشه.
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/4120" target="_blank">📅 18:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4119">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اگر نمی‌خواید این بلا سرتون بیاد و کس دیگه‌ای بفهمه ای ایران هستید از وی‌پی‌ان‌تون، از نسخه‌ی جدید WhiteDNS استفاده کنید</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/4119" target="_blank">📅 18:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4118">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ولی GLM 5.2 واقعا عجیبه. قیمتش روی api تقریبا ۴-۵ برابر از Opus 4.8 کمتره
این چینیا چیکار کردن با آنتروپیک، خدا میدونه</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/4118" target="_blank">📅 18:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4117">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">☠️
آموزش استفاده از هوش مصنوعی MiMo Code + پروژه‌ی ساخت ربات تلگرام با AI
⚡️
لینک‌های استفاده شده توی ویدئو:  1-فقط گروک استفاده شد. ویدئو رو ببینید متوجه می‌شید: https://grok.com
⭐️
توی این ویدئو: 1- یاد میگیریم که چطوری از هوش مصنوعی استفاده کنیم تا ابزارهای…</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/4117" target="_blank">📅 11:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4116">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">تمام سعیم رو می‌کنم که سری ویدئوهای AI، برای همه‌ی مردم مناسب باشه. تنها خواهشی که ازتون دارم اینه که نترسید، وقت بذارید، و ویدئوها رو ببینید و کار با این ابزارهای جدید رو یاد بگیرید
🥳
خیلیا که کمی از این فضا دور بودن، فکر  ما داریم راجب چه چیز خفنی حرف می‌زنیم و ...
در صورتی که شاید تفاوت درک و دانش ما از این زمینه با شما، صرفا دو سه روز کلنجار رفتن با ابزارهای مختلف باشه! همین.
به محض اینکه کم‌خوابی ۳۰-۴۰ ساعته‌م جبران شد ویدئو رو واستون ضبط می‌کنم
🤲</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/4116" target="_blank">📅 11:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4115">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RMn29DgvUlRuQiHBPebfzF2QL1QIzdLpX7er4IFFyqvwjkJuZa71l-Z0zT8ORAm65f62M52fftaZ8CKvGX0wKA0VKuV9hX-maDE4ltpFlI1c-I6C3jVRft_KxfTj_urD57oYlIdo-RkYMMzdX0zFqZDSZicTIk01C1ddWukTf_27WBhDrI7Fwr9BK79P_TZfofRn6dAsdWDfr_V-h_HJ5Cxz7aIWsokQZQ1WfHaenSQ5_0_XbAeHooSc478tNMa9wIt9Odie8P09kjHldeHT-_Wx33LtGQ8BnWGQflv6eAhCeq4d_M822deHy5Y38xvIIuNjJ8AwKYoYQ4yc9CsaAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت هم دقیقا شبیه همینه حتی قالب‌هاشون یکیه
😂
https://api.bluesminds.com/register?aff=drPB  ۱۰۰ دلار میده باز هم میگم مراقب باشید و توی پروژه‌ی حساس استفاده نکنید</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/4115" target="_blank">📅 11:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4112">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vTH8B_kBTZLXgPNRo2z21HCGS9rPAEjV7CXCeMyvE-svRk1B2jmsUPfG-jUB6hqujSJs3xDosweoGgv70s87v2repF01yYxf9Xqi6ZYIp2s8pnKSMyOGnuQj71zAeXt5_DlbBpdDueAC3WKB-xgJbDFsaIo-MvGWU0_7K37cCxERWMZotQ6mlDt24KKCk3l-SlD3gMmr3vt2rYZPfN1koN1S9qC5bT6FegvRcPl9U-h7gJelaBX_MPzdgYXSCDapfY1hiaBYeACRggoIwxdlFGjNHdu7CuhPQnkQjSBpONkdn-EtcvfdfSmEv-PAoqUDNkILVRTLnQYdqoN9iqcAUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FgAuBSdtq2pVXeyFcQxHsyF1-TwGX4PcrSOchbHqR7qj40D4WJ4BSNfQHrjLAhFxsDzrRfBeDP0X_dA6INycjUInSh4PpAmF6dEj4wffxSyjFCC94IQmAh-Jric26JJ7w7cdmCw8Mr23jUaxVcgPNzu8YQTxc-O1Z9JLX4z2hLCt4wAKqAU80NrEPvA-BCOch9IJAtUlB4p4gn-D7Ogt_IcEfcwe-AVLEMeHAiuNGLxkPAUHLdcdGHffVVGMW5Z05iTKF3eNpp-Yonsal29AWEbvKScZkQuj_J32o9kS618y_7je9VWCBnIA2n--_4WwHJfUbEOJZBF5IvdIV0bHXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/asYR-UxqAkwhGOXJ5WI-HmP5tdfzKPdKLrE86munZwd5-nd-qEn6z_kgLNo6S_5BW8Oe-tngWiRU-CCrvicHEp0D8jX7dIld8HoJSi18mC4lbyujKyESDzcmmNiT2o5db36fYmNkhdj5qwqBLr3_Tp5PZ5EHi-CsemKqa93hnu8laQwBH5FumKszUTFLm-Ls_zgI8PBHDPRkGotFxYBTmkfIP6mZf7uDCnoo5QsjkJCtWHYoAIJV1_FvwMq0lp28q4HbU_bzci-j1verV-GyqQLHkXnP6lFunfkBeCdFk6H5ZnJ-wWnBtXQC66jfcVut-rBqKX_UgfHuqSbvIzDvIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکی واقعا داره پول میده به یوتوب که ایرانیا رو به دین مسیحیت دعوت کنه
این تیکه هم از یه فیلم بود. دوبله فارسی
😂
😂
وبسایتشون هم بامزه بود
https://daneh.online/four-spiritual-laws/</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/4112" target="_blank">📅 08:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4110">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vu-1H3AOBnDpNWV_nK8BpYVHEhrO8reLmS4gQhRP0Qo_Qvb8cnNu5k_qSL3LSNKkuG5616iPFIOk7X4rLf7g_1k3hPrlRrSDJz13JIOugoCztvO-c8CqMs0QN7KJjO5DWsutw56zP7Hy1lBj6KI7QmWPTGfJfPCuUOHxEE7tmH0QXYpn2Ti353lLjxFlMvqsj1BlP1kZMoIGAk8AKVl7NUhhbfOOnC6RhnphVgLOzXXddOgs0eAbb9oUQwZYEkBSEqw-P6HMcD1zV9LdSVo4InobWFeNcHWMvaFZKCz-shWkF_5bksc2Qrffo_0N5j8xEcJ66z0-UQgPB5Y69Ggdbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EhItCBQSzPkAYMz3P-6EDO3Q0IMCJGkgJaP6J90b65fEptRvHY7fkwtZW7EAerQEUqcGPAWR6j_i4FLm7-0DZYYJBpa6QdcEY8UoQyjtNi37rkN8IexHtwBWJMfdFcgoXP3OR7DpkkgZRuBZyBcNXvk0z2QDSfnzIQk5bVVO3VpLjQmzycaoDTgX97GCDsz9qs9woXZBR-tzWNK-X6NwED0-hAn5govi3ezudUxjahRHkkDSkV2dwgMyY9rEF5dKxfmdURy5fkmcwipDRF5ZTwSkgbEBtOFYl1T8UuIG1ySZDeQuwitTtX7oAJApizaaAEFr4dusVS-iFstSutkUJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگر حواستون به توکن‌های Hermes و ستاپ درستش نباشه، اتفاقای خوبی نمیفته:)) همه‌ی اینا برای یه تسک ساده. بهش گفتم برو نقدهای منفی راجب Berserk رو بخون و بهم بگو 10 دقیقه طول کشید و کلی توکن سوزوند با gemini-flash . اما در نهایت، نتیجه خلاصه و عالی و دقیق بود(حاوی…</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/4110" target="_blank">📅 04:07 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4108">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EE7u-uwpV7x2sNE0HzgSCmIJ8QMFfJNL3B-VCc5gnwVaFDor57kF01D5Oabu7iuLvP83Xo_B8xmheNtfTeZhdQVmkHpY-zwfyWE6-kD49Gld5liA0e4MRIE2YcH63QpGjBNzkuNbGbJdVlVzsOWqvhBqzfLN1EJ-TkpuEXp_KsySR3drV0L9n6YdCSzeN8wbsWTWoarTDJktGweGBm0vP4EfWia2JC728OEWfCgIGiCQc5ltEv9-4GRFCrKdiQEJd8moaMGdrpTiYQQrP7uX0770o0P-k0hXOfbyoXtmxdkS2XbjFSnUEyxtxw5FhnuiXzEENVf1e1m9jW3rRgud5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iWPmijNkyh7_JduCcBDHTy2eMD5t5YuOenOmss5nj6-Av1zgCEhwP7tRJa4CXjNsGNR7ysWh449W4eX06T6M4UWRorxPkeA9IFoEFH6PefR8za4B8kapz_kjeoMLUPbMPKiZ6yCFyYZ39WnZXur3H-4SPlESURYlXXpi7G2Z5O9UuiFF99jQdqtYbnt139NYzipVuqiAJRM3Q-vupWNeMUzr1S8UTtrDzlpFNkgt-wfYyD3I_TsOZsvBYvLD77DzTwssQSMmYtv3SMph70z8Rh_aIGiIKLL6Uj8dFbKLoiar54_VOOlAAMn2uFhq5xzRvwz1NJu7CoLPGPL-TPYURg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگر حواستون به توکن‌های Hermes و ستاپ درستش نباشه، اتفاقای خوبی نمیفته:))
همه‌ی اینا برای یه تسک ساده.
بهش گفتم برو نقدهای منفی راجب Berserk رو بخون و بهم بگو
10 دقیقه طول کشید و کلی توکن سوزوند با gemini-flash . اما در نهایت، نتیجه خلاصه و عالی و دقیق بود(حاوی اسپویل طبیعتا)</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/4108" target="_blank">📅 04:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4107">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">یکی از خفن‌ترین و کم‌هزینه‌ترین مدل‌هایی که می‌تونید ازش استفاده کنید برای ترجمه‌ی بسیار روون از انگلیسی به فارسی، مدل جمنای gemini-3.1-flash-lite هستش. روزانه 500 تا ریکوئست می‌تونید بزنید و 250K توکن هم داره. از aistudio.google.com هم می‌تونید بگیرید که…</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/4107" target="_blank">📅 03:12 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4106">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">یکی از خفن‌ترین و کم‌هزینه‌ترین مدل‌هایی که می‌تونید ازش استفاده کنید برای ترجمه‌ی بسیار روون از انگلیسی به فارسی، مدل جمنای gemini-3.1-flash-lite هستش. روزانه 500 تا ریکوئست می‌تونید بزنید و 250K توکن هم داره. از
aistudio.google.com
هم می‌تونید بگیرید که بسیار راحته و توی ویدئو بهتون یاد میدم. در کنار یه سری api و چیز میز دیگه</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4106" target="_blank">📅 03:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4105">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">رفقا اگر می‌خواید از نسخه‌ی دسکتاپ Hermes استفاده کنید، به نظرم یه دور Hermes رو با Keep Data حذف کنید و بعد، از اینستالر Desktop استفاده کنید. چون من دو بار روی دوتا سیستم مختلف تست کردم و اگر اول CLI نصب می‌شد، بعدا با Hermes Desktop میخواستم نسخه‌ی دسکتاپ رو بگیرم، به باگ‌های به شدت عجیب غریبی می‌خوردم و یه سری از بخش ها کلا به درستی نصب نشده بود. الان که دانلود کردم از
https://hermes-agent.nousresearch.com/
اینجا، اوکی شد</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/4105" target="_blank">📅 01:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4104">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">کار خفنی که پدرام امروز کرد این بودش که جلوی دی‌ان‌اس لیک رو گرفت کلا توی اپ WhiteDNS
اگر وصل نمیشید به اپ، حتما از Fronting IP استفاده کنید.
من که با سرعت بالا وصلم</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/4104" target="_blank">📅 22:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4103">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🌎
سلام به همراه عزیز WhiteDNS
تغییرات جدیدی روی سرویس WhiteDNS VPN اعمال شده که از همین حالا در دسترس هستند:
✅
تمام کانکشن‌ها با دقت بالا از نظر DNS Leak بررسی و اعتبارسنجی می‌شوند.
✅
قوانین جدید پراکسی اضافه شده تا سایت‌های داخلی ایران به صورت مستقیم باز شوند و دیگر نیازی نباشد برای دسترسی به آن‌ها VPN را قطع کنید.
✅
تبلیغات از بسیاری از وب‌سایت‌ها حذف می‌شوند تا تجربه بهتری داشته باشید.
برای استفاده از این قابلیت‌ها نیازی به آپدیت اپلیکیشن نیست. کافی است یکی از کارهای زیر را انجام دهید:
• یک‌بار دیتای اپ WhiteDNS VPN را پاک کنید.
• یا اپلیکیشن را مجدداً نصب کنید.
• یا حداکثر تا ۳ ساعت صبر کنید تا تنظیمات جدید به صورت خودکار از سرور دریافت شوند.
ممنون از همگی.
🙏
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/4103" target="_blank">📅 22:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4102">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">این 9router واقعا ۱۰۰-هیچ freellmapi رو میزنه. شاید کلا با همین بهتون آموزش دادم</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/4102" target="_blank">📅 19:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4101">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">یه گزینه هم داره به اسم disable ai
هرچی فیچر ai هست رو غیرفعال می‌کنه توی کل برنامه
اینم برای عزیزان دل مخالف ai
😂</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/4101" target="_blank">📅 16:20 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
