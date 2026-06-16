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
<img src="https://cdn4.telesco.pe/file/pp5kOhkwGsuyhVgcemfTShL-rcp7GnbKyDvU45tqRgOWgg69OTv6fD7vNngZsJGcYhX0k7vp-BE2DYCaMg88G7WDyPVMusxCOoAN9nsibegQ_uY-iUveAYx4NJp8m8uqc-1eAQxat0nTcPK3SCR3IIjDYcCnHonW6GfGgENFcOQLqCrwLsj4Zwjw90kwzUPGvnu8qRs2Z1gbqS7byUe-I42sqmMTG_ZjaeZSw81jW_qSORZG9AfX9zskc3Xe5gFzltdgrkPFCXcdlk3f5UbfFvRLaue35ydEt5LVKwINKXORhu0Q_N2X6FIB7X7hU2DIDcm_Y5yeXhaDWbYFfGKmHw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.3K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 16:53:27</div>
<hr>

<div class="tg-post" id="msg-5584">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwtF72qH8MyPBto30-60mZkW3olD9GnG9fJ2CjrW1NCVLuUeUyN_T-TuCACoLeV4Wk_2cLLWb3K8Ic1YSAqIUvQySYuMN-A1CzpTnF42ikAYkUd37eshgD83x4fup2glXEYY8HtRZ9X1NHCt1CSx4JNeV3rgA09jYj8IUR4KN5nsjZIdwacgjCo9Yt1Ss5gZ5ULE5P36_jInO6JfP3QByGHNCJl85MpMTFCzhtPS9Hz9KX_k6O8VKMxPOXh_Bdrxh7PMkG9BWR6kqskGaokY1ixEB8SAnLSri46Tn4vCxZYMYH6YJ4zQPpgHVDcFRMpQG77N8-F5dPsFg27dUnCiwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای حزب‌الله ۱۵ سال در خاک سوریه و در جنگ داخلی سوریه مشارکت داشتند
تا اینکه یک روز همه شون فرار کردن!
مجبور شدن فرار کنن!
نیروهای جمهوری اسلامی با کمک هواپیماهای باری ارتش روسیه به ایران گریختند، نیروهای حزب‌اله
هم زمینی به لبنان برگشتند، گریختند.
و بعد به سرعت نیروهای احمد شرع
سراسر سوریه رو گرفتند.
بین نیروهای شرع و حزب‌الله ۱۵ سال
جنگ و خاطرات خونین وجود داره.
احمد شرع اما در این ۲-۳ سالی که قدرت گرفته سکوت کرده، اما اگه نیاز بشه، می‌تونه تا ۱۰۰ هزار نیرو روانه لبنان و مناطق تحت کنترل حزب‌الله کنه.
انگیزه بالایی هم دارند!</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/farahmand_alipour/5584" target="_blank">📅 16:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5583">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ : تحریم‌ها لغو نخواهد شد!
بستگی به رفتارهای جمهوری اسلامی دارد
(اول صبر می‌کنیم ببینیم ج‌ا چی کار میکنه بعد در صورت نیاز، تحریمی رو برخواهیم داشت.)
ترامپ : صندوق ۳۰۰ میلیاردی سرمایه گذاری در ایران کار رسانه‌های فیک نیوز دمکراته پایه و اساس نداره! (البته این حرف رو خود ونس هم قبلا زده بود که الان ترامپ قاطعانه رد کرد.)</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/5583" target="_blank">📅 10:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5582">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNTpIgWIVuzbRHoTGOwA9rElA9FQv7hvWUQVXbK-10dn9SS_0v71VrXTO4f60ZXKatjP2sXegayMEa5NlwI1GauZ_VBGdFQNS30uoKq15rcOKyYooV5tlldtESq0h3neVxCNLmqDq8PPJxQNsfEUqMh4yU2NI8-QRbzGfrrE2zmz6XpgUi2Qq65J0ZhDEj9pgmATvQA67utXwoYin10_W-cekLINiFMbsxYOXJf3b6hxWCOiCbVZjHprm0U7W7tumO5Gp1Cr3ImqtPnwYzjOjwepcmr6D1WXkFRSvZB6Jt52HjzmKUNHFqhLEntdnjKaeyXcgvJdIfB04R3bnQqIww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موساد و ارتش اسرائیل معمولا نتانیاهو را فردی معرفی می‌کنند  که بسیار پر سر و صداست، در حرف زدن جدی و قاطع است، اما در مرحله عمل، و تصمی‌گسری‌های بزرگ بسیار مردد است.  بنت اما متفاوت است او کمتر حرف می‌زند اما جسور و قاطع در امضای عملیات‌های پر ریسک و ضربه‌ها.…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/5582" target="_blank">📅 10:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5581">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNmU520OyUOM_rUGL52o5V502SVZxiwXwbVtVswFYx07M6V9JLsPy9PvCLaQlq8p1Vuih4heDgmhog7ZgnjLJeAxR920bn28qdzJZa0XebH1IOYevKa3iNaBVXty7okhdxnoIzCtGr8NF6uJU8PE8_e9aYEOIjCEPXVJ6MGtsPo_VoMrXzKuKOfipkgKCraA9SGhkFGJ5GZowioxf7HLQT_sH1-N4uEn_U1X6AQ_oncogHZxY1IAxInA_8o5PsSoqObOfPK2ZgxXUFzDW6UIgw8JN23jQdVU1dixPYnqKvWZI44r7fXm1iNzjxfY4_IRZcwBnNSJ-aNsybIbbOIKBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">او که از منتقدین سرسخت نتانیاهو در زمان جنگ ۴۰ روزه بود و به او انتقاد می‌کرد  که ضرباتش به اندازه کافی قدرتمند نیست،  و اینکه نتانیاهو زیاد از حد تحت تاثیر ترامپ است، دیشب در یک سخنرانی نیز گفت که راهبرد نتانیاهو موجب شده است که درگیری‌ها طولانی شوند.  او…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/5581" target="_blank">📅 10:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5580">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=TKwr1ad5noJF1gnrLSYu4g-i5Pxkg_pEfuMsr4Gpb5bHj4kUKW9743oreE4hRJio65LfDbvkkaEUexMWDtshdF1VRmXwLTunUlfJc0lRdde6BYxgoYVN0pxBusxr2JhMxGdWYUrOYS1mKKIti8fl7blWT4d6HdXgs_C35Nr5A4nXMi5Yw6ZGdgtvsw-r7LzB5FHFH83FEV7fkfmtuS1mE-B26KqIUKKoJC9FvHgb6DrnJPttDNKQLd3DuNkDIonnV_hYaGowKMQMGaLUR4ZR50gDiW06VAZPhjKArqbK4qH9YBH1sXW-7LA8IlczOzXTY0M2fndov4ap8WXR9p78Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=TKwr1ad5noJF1gnrLSYu4g-i5Pxkg_pEfuMsr4Gpb5bHj4kUKW9743oreE4hRJio65LfDbvkkaEUexMWDtshdF1VRmXwLTunUlfJc0lRdde6BYxgoYVN0pxBusxr2JhMxGdWYUrOYS1mKKIti8fl7blWT4d6HdXgs_C35Nr5A4nXMi5Yw6ZGdgtvsw-r7LzB5FHFH83FEV7fkfmtuS1mE-B26KqIUKKoJC9FvHgb6DrnJPttDNKQLd3DuNkDIonnV_hYaGowKMQMGaLUR4ZR50gDiW06VAZPhjKArqbK4qH9YBH1sXW-7LA8IlczOzXTY0M2fndov4ap8WXR9p78Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">او دیشب در یک مصاحبه گفت که دولت جدیدی در اسرائیل شکل خواهد گرفت و امیدوارم که من رهبر آن دولت باشم و میخواهم به جمهوری اسلامی بگویم که من بدترین کابوس شما خواهم بود،  تا زمانی که مردم ایران آزاد نشوند و  مطمئن نشویم که شما سلاح هسته‌ای ندارید دست از سر شما…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/5580" target="_blank">📅 10:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5579">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=Shq8OtJYjmipoz0XP54m-J9YRzcQE434yOKPrXeLmwZihGcsOpMxVoc5l9cvxw3RVNuDcReLXfhscNlHH869k5a2aYgfoSyufVX0e1G8DenChcoa9bVLduOrwjLS542R2oU59HXISR_5fQmOD24le8DghTzTXaajLwIRVLWmvBIUMs4X8T04FfjviMkxFI4p1SYdRkhOv7eBMu-fdx5SNn3a7vbt5OJ1ciO5XmuPeBAbIDTYU-nEOV26L5NlI6ElpVIxI5en6dyBaqAjPCbS0gLGxY2Mc12tPIO5-I4AE3dyWqhG9opd3ndlfIY_OOnq7zMIYoCG-W0mUzNihqdftR0bYpplsw_nYxrx4JCf3IOHaDWI3xTUrzI3r2xiftoW6OHIKmhSdPej8ojhczKoGk5cyxI9O_qye-VphtyhKEbLC0ax-TVTr84KDGmKzXZ6OI9YonJwvFeGTvYRlLFhTtGHh0xfLb3LFnfn8zqVhBocLPh3nk_Lqq7onTUpzpMl-ObqujCRd5tvjtzT2RiXBSQKjfTq3shM9XU3VPTqpXnVQBdYYctMVQmKLoZ1stAEhMBV-yALUu3CimufYrjX9wKO5qLVi2o2Jh9-oc8UaPii5cNSMORGwW1hEKZm_52CZgSWZVwkzjpdbWPWdDhMHnpe72cJCQ2nAw-L2tcz_3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=Shq8OtJYjmipoz0XP54m-J9YRzcQE434yOKPrXeLmwZihGcsOpMxVoc5l9cvxw3RVNuDcReLXfhscNlHH869k5a2aYgfoSyufVX0e1G8DenChcoa9bVLduOrwjLS542R2oU59HXISR_5fQmOD24le8DghTzTXaajLwIRVLWmvBIUMs4X8T04FfjviMkxFI4p1SYdRkhOv7eBMu-fdx5SNn3a7vbt5OJ1ciO5XmuPeBAbIDTYU-nEOV26L5NlI6ElpVIxI5en6dyBaqAjPCbS0gLGxY2Mc12tPIO5-I4AE3dyWqhG9opd3ndlfIY_OOnq7zMIYoCG-W0mUzNihqdftR0bYpplsw_nYxrx4JCf3IOHaDWI3xTUrzI3r2xiftoW6OHIKmhSdPej8ojhczKoGk5cyxI9O_qye-VphtyhKEbLC0ax-TVTr84KDGmKzXZ6OI9YonJwvFeGTvYRlLFhTtGHh0xfLb3LFnfn8zqVhBocLPh3nk_Lqq7onTUpzpMl-ObqujCRd5tvjtzT2RiXBSQKjfTq3shM9XU3VPTqpXnVQBdYYctMVQmKLoZ1stAEhMBV-yALUu3CimufYrjX9wKO5qLVi2o2Jh9-oc8UaPii5cNSMORGwW1hEKZm_52CZgSWZVwkzjpdbWPWdDhMHnpe72cJCQ2nAw-L2tcz_3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفتالی بنت، مهم‌ترین رقیب نتانیاهو در انتخابات آتی اسرائیل است،  در آخرین نظرسنجی‌ها محبوبیت او از محبوبیت نتانیاهو پیشی گرفته.
🔺
بنت قبلا هم نخست وزیر اسرائیل بوده،  او کسی است که برای اولین بار  جمهوری اسلامی و نیابتی‌هاش رو به  «اختاپوس» تشبیه کرد و اعتقاد…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/5579" target="_blank">📅 10:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5578">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dOhHQbP1NmSoNA7LOu16_mgeEFxN1xmUekzUbmNqFCkaRxPaXuvXK8r2U5jA817xaC8BFjhLHJJQDrfSAx_4G8PGGEtupw2C0uQHkoHiaMqBsIUKIaoMMfcUhOBaPSSpubleLswM6QeLoNNUpHa0T_toBpLOkErCkauP8UX8A3niKHmgNCEvzUPC5b74-zDRuU81gZizvtAkGHFab7JtepV44sXES2WWbZLN8Bh-bm4z9yvf7_vwpraHXwkMJkV6QSjrHoqb0JelpLTHwrTwNcda1avusrnuTootnlYn2NMmqTbxI10ixuqh_Nn1_QQ0zXm2CVJFS9_ERT6s3oyaAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتالی بنت، مهم‌ترین رقیب نتانیاهو در انتخابات آتی اسرائیل است،  در آخرین نظرسنجی‌ها
محبوبیت او از محبوبیت نتانیاهو پیشی گرفته.
🔺
بنت قبلا هم نخست وزیر اسرائیل بوده،  او کسی است که برای اولین بار
جمهوری اسلامی و نیابتی‌هاش رو به
«اختاپوس» تشبیه کرد و اعتقاد داشت
که باید به جای درگیر شدن با دست‌های‌
اختاپوس در لبنان و غزه و سوریه ، عراق و یمن و …..
باید مستقیما به سر اختاپوس کرد.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/5578" target="_blank">📅 10:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5577">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPaPvDSmTle2Cn_G65P6D7joL9eWY8uSmXyTKApGiMx6iKdVabWUynDucceHk9hmkcpBOjAUrJH12OETK415QigsHOtoya0tFg0OvEXz6R9ARyJdzHkOAsBz7-9a5nvJhB1TwaoJ81oKTO34csYloluMiiYMhY-4TUyACRyUH8QyTr6VZmpORy3gPsD92DUQPf2j4tEaOb9BULarmsh2mJlTpeGrAOaABjvfQM4Yz_oupmJ9GvYohyCm068tMaGHUU2YQ-bkYXL73eJd84kmMxKaKfR8BFn0rjxlJ8sI29STuepOQB2ZB2gQtkIfo_CP3rjrdGdvyJlBLTbyio4Muw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اول هسته‌ای، بعد موشکی …
‏به مزدورهاشون که هر شب جمع میشدن، گفتن که چی امضا کردن؟</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/5577" target="_blank">📅 09:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5575">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n7qhNLJwMGDM-12nsesYY_c-HiAUzQrGQRvKgp6BGsyrqXOc1bNoMu54tr8abDjZEMlMLljxBep9GtZMH3PH9F5BPSI2eMR61o-64qgC0_ihLybK4SlrpwCGlrMKvS0eDubwNmHGbiqry82M5lYBVl4PGNjA6Eml6MAHt2fbf1_6pQjyOrPVCqJT6woHGoQHURnzKuIF28FCJewzzwNeP0k-iAiB9O3elQcFY9KcQ0eGHtdocHCwswDkNlG8KIwhoGtGYHYuyz5wXi-F4UNAhSVpTWw4lwDScEbGIKtIeRPavWtvPBl3_D9hFjUFzbRDVyIvmSvcYnEYh47FjMBzFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dcXLR2WbeYqRCJYaZ2GzY2xvXLjXXSRf6xwNKCAw4-Bz0fVA9olh8xz9KmEK8ikcoUxG75voMhu3jqkCkCL2deXk-uOXWGBbGfNy1nEAlyucctGcgic7KT6apkoNi2DuiDgCtCTFxFBs80hzgHh4NhFEtyoRCMLK5tUFm1h6RNzwKR6yGq87EHWN60a0CxI0jN1qmQJmzixZ7XbCF7JI2axxIJ2w7eiLMEtDGzotkS8P4jD0FgLrY2i3bHEJhBFNVIGCCq434hDr18daE_P93-Xe2U7pjjAsOYJMpVSjufBVTFnlWeSfOoF8G_M6JDjJU1GE1-iS26z-Wk-SlK9zXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسین شنبه زاده فقط و فقط یک نقطه گذاشت!
نقطه او ۱۷ هزار لایک گرفت، دست خامنه‌ای ۷هزار لایک! رفتن گرفتنش و بیش از هزار روزه زندانیه!  چون فقط با یک نقطه دیکتاتور رو در هم کوبید!</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5575" target="_blank">📅 09:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5574">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXPNd-sjAK6k0FHjbEUDhvF1E6vdscgOFSJbeTN7yZuVUV-0KxyLKq1qOWkqexFwk-8uukZVbXrW0-m4ElApBznnLTNFTngMxO9ex6FVcg_BKQA9A2zK6H6strq0Zk6o9YPvJCvirBtcT0JN72ga7DTwgPg_h1ISOFoMT4zCdLxKtgAxdXL4UiSMX2cSR203d58Wh7FWlv2HtK7FchT2zQhM-kwO79Tx584swtoTWVuj-SbeDb2nA3DMuYal3WLb02tojAHUNIic672lJ7gG7sFp4b_ij0_WzZc4wkClfJzFdGu-UYfgg3NwGDDnCvu5duseOthqSl2SpURMVVAGqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنیده شدن صدای سه انفجار در قشم و تنگه هرمز</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5574" target="_blank">📅 01:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5573">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=d80hczskAdSXT_RM79irlTeHDBSNlHOFj5HMpZVRcmVQxzICMTMVinXIe6mvt3hVSSRck8MRUMyVc8lXkzPlySQj4uyg3tESVr1k61bf-yMM1qeXBydQpliQrDwreqlsowStr7YwDlTSIi1Gz9XdrvT0yQzKFjEB38OzLOswl6cVOGVPQFqk254OfU3V3LCypujDKptj2aEoFvRGpSeEP_hjyrkldI-QQHukZdhpU68zQudGEGlJQgbUR35F8K8XlbPLxinWDLqNsBN0On0IcbtX4DvGv9gB6FFY9lLS8M-46dypsZMer192FKMbSc7f_MKbSOCjNzYfmcVhLCMgL18NHzQwFT67J3cDuyOJaxOl9d-UC-7S_GGoI9DEY5Q6RXLNleYdxMlKinF8hFOTqxArOBKiWTg4EGS_i2Yh5HtUbKSW0J5MR92oNqHWuv1x3EAE4UpQ2DosVA6D7C3aFiiSU3aZEkjsxnOSCZocXV4O1zsmGCwnpn1o78NRxCEoiCpQkjqs_T1WHOEeXpN0mm9YP-x8k6sZH5IX-K0vEiA89uwMlcEM5NXLQz-zreXHsHMkanYd6ArDb6xK0XIRhHPm0groXobhdUey16YUaM4kjqy7B28M3flHqdXm1DidT0IjU_LI9LfjjBPF7HrtOatovnD7QbYS1Glaou8JYB0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=d80hczskAdSXT_RM79irlTeHDBSNlHOFj5HMpZVRcmVQxzICMTMVinXIe6mvt3hVSSRck8MRUMyVc8lXkzPlySQj4uyg3tESVr1k61bf-yMM1qeXBydQpliQrDwreqlsowStr7YwDlTSIi1Gz9XdrvT0yQzKFjEB38OzLOswl6cVOGVPQFqk254OfU3V3LCypujDKptj2aEoFvRGpSeEP_hjyrkldI-QQHukZdhpU68zQudGEGlJQgbUR35F8K8XlbPLxinWDLqNsBN0On0IcbtX4DvGv9gB6FFY9lLS8M-46dypsZMer192FKMbSc7f_MKbSOCjNzYfmcVhLCMgL18NHzQwFT67J3cDuyOJaxOl9d-UC-7S_GGoI9DEY5Q6RXLNleYdxMlKinF8hFOTqxArOBKiWTg4EGS_i2Yh5HtUbKSW0J5MR92oNqHWuv1x3EAE4UpQ2DosVA6D7C3aFiiSU3aZEkjsxnOSCZocXV4O1zsmGCwnpn1o78NRxCEoiCpQkjqs_T1WHOEeXpN0mm9YP-x8k6sZH5IX-K0vEiA89uwMlcEM5NXLQz-zreXHsHMkanYd6ArDb6xK0XIRhHPm0groXobhdUey16YUaM4kjqy7B28M3flHqdXm1DidT0IjU_LI9LfjjBPF7HrtOatovnD7QbYS1Glaou8JYB0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«روزانه داره ما رو تحقیر میکنه
ما رو به لجن میکشه ،
به رهبر  تهمت جنسی میزنه»</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5573" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5571">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYhOO-R2LUKnhklu74Id45BTDEudSbOxk-7gL-KOCxQkyR8qEy_Ez-QuzOpLMpwC42OCS6v8NNhaCRbUi5pRQKbGOlp9eJWQz3jiGZ7LR5ss_7t4zuGYBjuijWpkjLld5KcDnnmyT9tRbeVSS8KR66zMzfGdkanvuglAjlb5R8eqTxaIslbejMCerhT1bhfOeiq1rn-gVIbwk8JSwwfK3vGamkmqXw0NbHIepgNvAVuToVf4X6QN6qBb7pPDS4t9ER0MNvlCqknelaaTaTwaNAG8H6wfqCcaRMXMgEXu_SR0dZYlasx53n0uRZgq3u470hTExviIqLdWGd5DaN4WDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=IElFrMxJG1OtmGnM8G_XKJYAxgog6m1OnM0dhnk2yXZTbT_JwJaIBRTRbAVODmAEJ4AYnNDI7yXlKFR0eKz2WfFJhQX_LBzrsyJlFPOb75DGLGF67ChufS5j7goZ7B9XP2qOhnae54kWB0Fd7fpdUTvaNgMVrMwMN_4YoZjFsy5pfLk7wCL6W7NVPMDp2sIGeAXCwmtvpJjBOc8OdR1LZj5EYMXXDg69G5Pl3ZYrwpuTajt8MpEtkPcefrNTcA2TDVzNfMXcWTXRJg8Lvb_6DrSd7hwOfYzDgwT3YXf2oIv5G_NkWZnUghYoariRcL9FxDix5VDCGOi04lWSVuhzEIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=IElFrMxJG1OtmGnM8G_XKJYAxgog6m1OnM0dhnk2yXZTbT_JwJaIBRTRbAVODmAEJ4AYnNDI7yXlKFR0eKz2WfFJhQX_LBzrsyJlFPOb75DGLGF67ChufS5j7goZ7B9XP2qOhnae54kWB0Fd7fpdUTvaNgMVrMwMN_4YoZjFsy5pfLk7wCL6W7NVPMDp2sIGeAXCwmtvpJjBOc8OdR1LZj5EYMXXDg69G5Pl3ZYrwpuTajt8MpEtkPcefrNTcA2TDVzNfMXcWTXRJg8Lvb_6DrSd7hwOfYzDgwT3YXf2oIv5G_NkWZnUghYoariRcL9FxDix5VDCGOi04lWSVuhzEIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین فینال رژیم منفور شوروی</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5571" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5569">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=nS6rrCTyqcpZT9Z-lLhSCM87kh5ipNRfSP7WvEBRF054PJ17UTfVaKfScvErgO8EuxxdVUnum9zHl-99-V5QCowpxou0ICjoIZCPLnHxXAgRZ4xgHLOaenesQHPwbtDECDOgCO4uMA-UVhI5uWDinWLSejUn_YjzRlwPNQ2wzAigwA86ePgyhW5yccmVHyVQFxgNK0vL4rbVoNqM6KPaf2hQfqqbQC48h5YGph9GTpXs7YX0mFTmNaMJJLwUzFczrioQBb7HkcfiUzNzou1tGIca_IL5_8FO7EbmXoG2Nter6hVzTfPUyqxqVlc5NyYxc5L-MeXOLWjxEE_qiLfbrHulddS9G_CIpYwRRxMKVi6dFn1jormbE_G0baDUXeHBA-7FcDBWppYbjmYLKNqs6RlQe7ZSIOC3b7dQycppjrMemAaVp4BLTGKkGwpAvxrefxd2jKhZnoNysIu6k8L8vcYhajRrgkMS2Tfs2M9OTX9jlzNOobD_RzOqkOT62gmsstP-x-EUFJ1Ql7P6Z8-du9QOt-BgnMTYi_8MyyulJZyHdBgzSIi5GEBTUoYvWxovaCN7zNGKop4MRt8k8iHj6kgTWGtdKZttMBaZwPeINHRuxz6gOUG-9Eh5BIEBVrARXt9RBfE0uOZZL80ckPsK5k0foYajVvV068TkKaRVFPE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=nS6rrCTyqcpZT9Z-lLhSCM87kh5ipNRfSP7WvEBRF054PJ17UTfVaKfScvErgO8EuxxdVUnum9zHl-99-V5QCowpxou0ICjoIZCPLnHxXAgRZ4xgHLOaenesQHPwbtDECDOgCO4uMA-UVhI5uWDinWLSejUn_YjzRlwPNQ2wzAigwA86ePgyhW5yccmVHyVQFxgNK0vL4rbVoNqM6KPaf2hQfqqbQC48h5YGph9GTpXs7YX0mFTmNaMJJLwUzFczrioQBb7HkcfiUzNzou1tGIca_IL5_8FO7EbmXoG2Nter6hVzTfPUyqxqVlc5NyYxc5L-MeXOLWjxEE_qiLfbrHulddS9G_CIpYwRRxMKVi6dFn1jormbE_G0baDUXeHBA-7FcDBWppYbjmYLKNqs6RlQe7ZSIOC3b7dQycppjrMemAaVp4BLTGKkGwpAvxrefxd2jKhZnoNysIu6k8L8vcYhajRrgkMS2Tfs2M9OTX9jlzNOobD_RzOqkOT62gmsstP-x-EUFJ1Ql7P6Z8-du9QOt-BgnMTYi_8MyyulJZyHdBgzSIi5GEBTUoYvWxovaCN7zNGKop4MRt8k8iHj6kgTWGtdKZttMBaZwPeINHRuxz6gOUG-9Eh5BIEBVrARXt9RBfE0uOZZL80ckPsK5k0foYajVvV068TkKaRVFPE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : تا زمانی که نیاز باشه در لبنان
خواهیم بود. نبرد ما با جمهوری اسلامی
پایان نیافته.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5569" target="_blank">📅 22:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5568">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=vliEBXA0J_ymtqAhKIy8fhSgC8kItyFBuYGvnWJcX83rChkZEw6oc-McONOmKytah9KzSDWRuAEqwkTMm74eCttbH5KcXlS1xozNkiVkqhgm98S-N8u6QPzeMKBlBVnO2aX7rrngjEU-TbisOP0dW0v5iHm7mleI7O0m1QHWjYFycuifQBTSEZ5g5iiiKIYmtg5FCx6-eWx-U2MmjJU_HYJL8w3BRrhLJ3prYcWBERg3oyApWvRLnN2EnpxRtSlPpMRpEqy5QOz1k2Uftxl5YCR8Ka4fF32uSIzjlL2-1pxy_tAnAOMxZ1avcm9ccOzMGLwvK2pH1p8uR76ubacHwIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=vliEBXA0J_ymtqAhKIy8fhSgC8kItyFBuYGvnWJcX83rChkZEw6oc-McONOmKytah9KzSDWRuAEqwkTMm74eCttbH5KcXlS1xozNkiVkqhgm98S-N8u6QPzeMKBlBVnO2aX7rrngjEU-TbisOP0dW0v5iHm7mleI7O0m1QHWjYFycuifQBTSEZ5g5iiiKIYmtg5FCx6-eWx-U2MmjJU_HYJL8w3BRrhLJ3prYcWBERg3oyApWvRLnN2EnpxRtSlPpMRpEqy5QOz1k2Uftxl5YCR8Ka4fF32uSIzjlL2-1pxy_tAnAOMxZ1avcm9ccOzMGLwvK2pH1p8uR76ubacHwIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله دیشب به ضاحیه :)</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5568" target="_blank">📅 13:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5566">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rc1LlD3zqCuGprnmnrbgLpLgnd1mFCu7FK-LL4ySrdE9IHUI6uJ0MkBzb_DSWhuUjvgPQKs_LIEsHEwro6Zy1wom71RiXAhFjZmhYZPs--uXV2A7AwLCrH8xmihGbDHN3RDcmYyDg55mutiL-daY3hWFO1wjfwUOOQ0BslsVzBGckSDS8Vvv0j3pMtI_JJNm3945FOFfbf5qTdh1XVrJb4GXDBmYV5EaulAJ6DczYf6lu3RRfCfN8q10Z6wa2cK-sr0-MDtuB_ejqUSoLyaFwDGhPYPvsNLjeLKy43UufybMif-KgstjzwiO-tWWbdQAx4NiGZTiYOwouruKzJX9-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GBw_GIV4sJgbtRCH48QSCYxpQxAsL6fxtWCMaPz4hl-pvcKsjZTbmk9Q8FhqkJEG0-pEpsRWDeMAECpLCAA25s8HpuMsVLWZEpuAsF8R806XYkgdJOcyaOzIh7KcqGafUu3WchyTlXPhcch9S5gmXu-bRquGo31C85WBYAwn1EZSGxFc8ZbukmzklAeveudC6beCY0luHzs-Koaeawr0ywhCWXJz56C8qsDg6hAvo5tPwK55xTzP-xLPV2eS7GZI68rcrOWM6SoRO35eTvt4AjMlVjvJdC1H3dnxYcAADodsaAIBT3MmomVanAcpEJaAxy_vzP5sT-76b6B8_5hV5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5566" target="_blank">📅 12:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5565">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uo-EVKpONwjyirABFjizyI1SGde-jdHRD27BfKm48QMMal63n5oHUdtEmmhHRtltgeoAogBHaFgVZxsF9iKXbjiSk0KC3a17fws0EQfjaK4BPwghKY3FZn1fJ3LYCnwqCGZRBCgWw0uAybSdQiMQZ0LRjM6WgLj6fchvQJFxgyv5Jk8eQRkEhOS8eppHQht2aXcOkWOjwYiLki_SXoyFqWWXaHBzZH3w6QgJfv-f6wpB4kF3KEgmYiarLicGoKDT_p-YmrL44Ixc1hwsL69n8nGXy3vcZcFo8qX-AC2SJeK-jVtzBzUexMuB2mEj-3tgdrbcdG6aqAMpOQr8OWV73w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم وضعیت لبنان</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5565" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5564">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3y0TZQ7CJDRUoEWhQibPYZ0lIsaALmMn2oL0nm9wzzr1FvgzhkxakrdzL1Yf0tSTzwCw0Oz4ypBxtsB3mdXGiZJ-g_8m5b4e0j4PAUzudQo7b8CZhfXmeXulJfMhOTkD-q4UjeQgRQnvbzKTeJOnF4AN3EkSbt7UmUrhU1P4uwWEGDxSkmFUkl3BgYzcdRs-bWAMA6NJdbCcLgEp5a18cMMa6D5bDqLiCXbj261XLjMAn295jm3bxcNveTZm7QHqhuqrGBtGQ8dE91rIBTAWlCFVTkqaMLKDXmDjSlEA_sz3LoL_e5J0b9tOiDG9hoL8pMZnanGI91b_xB0ovLrfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون  امنیت ملی
و سیاست خارجه  مجلس دقایقی پیش متنی از سخنان وزیر خارجه عمان را منتشر کرد که بر اساس اون، جمهوری اسلامی موافقت کرد که  «هرگز، هرگز مواد قابل استفاده برای ساخت بمب هسته‌ای را انباشت نکند». این تعهد جدید به معنای «انباشت صفر، ذخیره‌سازی صفر و راستی‌آزمایی کامل»
بود که سخت‌گیرانه‌تر
از توافق ۲۰۱۵ (برجام) ارزیابی شد.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5564" target="_blank">📅 10:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5563">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">رسانه‌های جمهوری اسلامی،  حتی بیانیه شورای عالی امنیت ملی،  تفاهم ۶۰ روزه (که هنوز هم امضا نشده  و ۴ روز دیگه احتمالا امضا بشه) رو  «توافق» «پایان جنگ» معرفی و القا می‌کنند.  در حالی که چنین نیست.  یک تفاهم نامه است برای یک دوره ۶۰ روزه که طرفین اقداماتی رو…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5563" target="_blank">📅 10:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5562">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،  ۲ نکته رو به عنوان دستاورد مهم توافق پایان جنگ با آمریکا معرفی میکنه : ۱- پایان جنگ در لبنان ۲- پایان محاصره دریایی.  ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!  چون رسانه‌های غربی چنین موضوعی…</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5562" target="_blank">📅 10:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5561">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIASbCLTccLWvjVaaPS9SOnLV2fmfadjFnASmM3mkdH5j9XtuQnKHwJAKuUIFuUTmbjwoudLRffogDr61CS2r2qZP9l7_YDOvqeykOl4cb3O9qEf4Ltmtp5WFwEMe6efTuivlxruYCCr8nJLQoSwb_r0ngNUhEcPd2s4QxnBsFIJzMB-_f9M0nBuIZ_4xZOgk2GLoGis_9K4nxgnWaX--oUt3AhB2RWGWB6IZ37NTL10-WS6CiwRuTCMrXPrjwFuEseJzLyevrlV3mroTG2lspbDt0ieex-XDt5KawjhdgWouOEgK3nEqtd1kJmIHMVlteQzeOOPEerrKVfAAepSoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،
۲ نکته رو به عنوان دستاورد مهم
توافق پایان جنگ با آمریکا معرفی میکنه :
۱- پایان جنگ در لبنان
۲- پایان محاصره دریایی.
ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!
چون رسانه‌های غربی چنین موضوعی رو
به این صراحت ننوشتن!!!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5561" target="_blank">📅 10:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5560">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=FWlg388FSBuQenrJvhhOIVkIyV6FUclqqUlU6e2Xqab-I70zNltw4u2sK12OV_hOw-LXZAFMZz-XAsaTGGXZmyBI4InFQ7ejY3nz_1ijIILBIbVeiI4uiic787HRsV-V5Xrpfb0hqCUzQrdNmLPSJRzsLe1LGQWsIzqmMHnUAL4N0I0oZUCARGDKbyPdkDVzD5WICHIVGLM_F3qvGtdxjZq_pxOzq62halEoFadbE3OG38Szyg2dsQyhZJvrmaQW8Da-gLo8-bdgL4sS7HX6FjwG_3WMqatdscvup5PqIkS_YOGXe_-QMmcyORhU24slKkRKK0jp0QZtdBz7gBTdGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=FWlg388FSBuQenrJvhhOIVkIyV6FUclqqUlU6e2Xqab-I70zNltw4u2sK12OV_hOw-LXZAFMZz-XAsaTGGXZmyBI4InFQ7ejY3nz_1ijIILBIbVeiI4uiic787HRsV-V5Xrpfb0hqCUzQrdNmLPSJRzsLe1LGQWsIzqmMHnUAL4N0I0oZUCARGDKbyPdkDVzD5WICHIVGLM_F3qvGtdxjZq_pxOzq62halEoFadbE3OG38Szyg2dsQyhZJvrmaQW8Da-gLo8-bdgL4sS7HX6FjwG_3WMqatdscvup5PqIkS_YOGXe_-QMmcyORhU24slKkRKK0jp0QZtdBz7gBTdGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام خبر امضای توافق جمهوری اسلامی  و آمریکا در صدا و سیما.
ظاهرا حمله برنامه ریزریزشده‌شون به اسرائیل هم لغو شد.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5560" target="_blank">📅 01:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5559">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-wkXwb4yMBaQuOk78YFjrSLCuDPwhAHN042ojSiKY4loWKMVF5Wz6RRQee8CBIoYU8L_MMa6752t8_1JnK-9HSeAjBYj11mI7D6JtHmE7Yu9zxjoO-YMdVR3BAs3AUs7XagAGyNFTFzQ1Rz1zlXCqUAEHo92RJHRLkyXZkgwAfeSWnXq768IWN99JPXgoOEtpECC25-deRQ-Ze48q6f4BNebAIwZJ7xdZGCxvSoc6P9TF4Wv1p1NI7b9yR9OOLV7Ak2XsZYZp3xwdR62vZbAFPVxJUE-xyAVs0C4UG1CVcvqYJnO3XDz4zvHX5109UFekxXZlUBKGWGVRDFEN39xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده تهران ؛ ترمز امضای عجولانه توافق کشیده شده. سعید جلیلی جایی نرفته.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5559" target="_blank">📅 00:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5558">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
همزمان با تشدید تهدیدهای لفظی سران جمهوری اسلامی، اسرائیل بر شدت حملاتش به جنوب لبنان افزود و موجی تازه از حملات را شروع کرد.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5558" target="_blank">📅 23:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5557">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okF3troIVHH1V3GBLpqR5SvgtQMLl1RfRfMt8DtDgiGU5H2n4-K7NDICmTk0ZkJAH5128dTM5lPJ8ygEe4IEyAaiX3sqeiVKt5zmH8NbkN__1KJdUJecQeCm3U7IwBOikQYJRYvclgLCS7zmnbDWRVJujt6rnSQjPdSdWxmcokW5pohIMN2WEXe0FRC7_5b4tODUXywzdQ5ZWGycuYl2wDEAr9D1IfmbtOLIRO23q_W-77XUhIbPrct3BWALCvdxPtv7ui1ZXGCx0YrWEA-q_A3jAGghztuQ93O_voFFX8pSvkO0seczzbEL3z3ycKpud5FMrsENFHjNwajzp6J8Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ولایتی مشاور بین‌الملل علی خامنه‌ای</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5557" target="_blank">📅 23:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5556">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5556" target="_blank">📅 23:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5555">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMlEEWr3wgbhYhHlUloum-k8Kh01hkWURi_yrTJL-Nnfz-jr0_onAEbUulhjpoHytVCCJJqR7uFtjlYE1-6HrMRO6efyzI6viItx9QZK9R9IvnOWRF80oRETCnYTezdMQrpqyJRXOJPDucDFZOwCgs-Ay8NWX3U6UYE6gVdcgg46vNhOwoknT0GIvbXTnCJIcXeKf_ziTVBEE_Fqf57JJlMAQAVSgGz8Pb2NDaeDvlQupm-57JZP5DUBtOUo7mKRdh-CeCuOvTC-o6P0Egkl0LdWaR2ni77-IZe_5sj5aM-JDC0Er7nhQGR3zT_qln0xefg0usAzRQoXv-DDrNzZJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف «تمامیت ارضی لبنان عزیز» !
«بساط جنگ افروزی اسرائیل
را برهم خواهیم زد!»
جمهوری اسلامی به خاطر حزب الله لبنان
دوباره میخواد وارد جنگ بشه!
آتش بس به دست آمده میان دولت لبنان
‌ اسرائیل رو رد کردند، به جنگ ادامه دادن
الان هم توافق نامه پایان جنگ با آمریکا رو کنار گذاشتن و میخوان برای حزب‌الله
وارد جنگ با اسرائیل بشن.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5555" target="_blank">📅 22:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5554">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5554" target="_blank">📅 22:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5553">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
لغو تمامی پروازهای غرب کشور!
آمادگی برای پرواز آبگرمکن‌ها
روی بیروت خیلی غیرت دارن</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5553" target="_blank">📅 22:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5552">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKbPVlCnyQdZSpCJUJ24anW8JGFpPcZVlJaPJXWUfAuenpx23LjTQTRoVLSX94NKur0RIQeV0oUb-OafCHVD_0w-9y2tycAqRwXkXtlPJrccz72l3ksMs-toC_KPj3LQ1Hgm8h0aOz6VIF4XIm7gvYkGQEjkZDRzG8T7rtn_m0cXoOoKfXCCQIJbBeXcohhHpe_btFSI5Epxy3yRHrIFPRrA7mce3c7QrhTD5i62b4MX-Ksw71stbnsd1MJP6IuD6Xv-3nFiomUOK_hIbv0WiKXsTmC1MoIov6kZwyiraOA0-BZvDaxLMqqoXA0pl5cGcvUTAomYdl94VeVfRi3E9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای عالی امنیت ملی
«لبنان جان ماست»
پاسخ رزمندگان اسلام در پیش است.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5552" target="_blank">📅 21:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5550">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bAbG5Ti_AF2OjpmSPMJB1KchK-ivnE9S9rXvJ-KYEIxXw9lcCBSlDQkgOnrNc3q6kiXK2QyAOB-tGyS_TjkW_CunnHuiWYIcOoshQhLOaismeHbzRj0391RXzeC0qTZgkepewXdeXg_8tsLE4AjoveLMyMGAPVWDhWaWqbqwxFPbDjKv2xfzWYwafrhpCtsaTQGtSvKhBfnxU56UzAapJ7qpG1n4-unKuxRaK9U-oGltKXwxAtfSYG-hxABp6Uuvk6gwI6h8kkeaXdAfZ-cVIs_xsg-51LccZHpms5NvisJHe51oLAiWxc_e3UW7ADgrd98Ri89d6NLw58MnQ0TFaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DSIs_eL9fbIE_-XQxXO6mO7CbzZly7JzfuWayptkXd1GKK939Z-Tu0khINfrvLpRVsEuiZSpRxl2CA0OpgNCwccYJ-y_tiUsJp83Ur6LOSvw571LZR_dQ16nGxrZK3on1x_G1E6T4ygQ-Dl8HlwX3jvH95-k2YbzdHeiokxb6BqtBeoRHas6PFKactB9cV8h9Cwzdhfns6zMabO3utY8ysja6k0Hi6iVOddzG0PU30NRDDzikKrCg9APd3S1wL8JDdDuq1h44CRf1ZT2ruGiIvkthReHwrRJTB-3NXqT2ycmBNKXulVuy2M2o8R27Y7LWOAUD32p9kh_RxtEYi1o6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عزادار کودکان مینابه
عزادارن حکومتی!
میگه حکومت همونطور که در ۱۸ و ۱۹ دیماه «به حساب» مردم معترض رسید و دست به قتل عام زد،
باید دست به قتل عام معترضین توافق هم بزنه.
اینها هیچ وقت ایران رو دوست نداشتن
هیچ وقت ایران و مردم ایران و‌ کودکانش براشون مهم نبوده
اینها عاشقان جمهوری اسلامی هستن!
اگه برای کودکان میناب هم عزداری میکنن، چون میخوان یک کردیت به جمهوری اسلامی و سیاست‌هاش بدن.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5550" target="_blank">📅 21:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5549">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامپ : نتانیاهو نباید دست به چنین حمله‌ای میزد!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5549" target="_blank">📅 20:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5548">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
ترامپ : به رغم تنش میان حزب الله و اسرائیل، تفاهم‌نامه با ج‌ا امروز امضا می‌شود.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5548" target="_blank">📅 19:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5547">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzBJ-VpRjFd8zc3zW84DzaZz1bxfbUkapF7ke-P9Gn9ZMjIWffBrZ5VMJUaOjazAu_qPKVSzUBrTc7sY9xPzAMsM6jHYWlzfKmdGc9EnYhcQ_gOX1T4UpbTlbb4yGZyQ1hIbS9sqZ85xPzgqiJBHyct0fWSJSQ06ezbnYkBWoHqRV_9S2wTcV3kXWTOieoggDmc-qWT7IfB3rUjCU2wEEkgJfjhSOTQbG2JRKmzEeu7-Uaxd56y47lBOnjsg1q7-QqzJQGigfVCdB5pAvGj-MquFzDyr4QrYWhmWGGGLU3i36m9VAY-03B31IK1_SfSSnJ89AmVcC56eOq6mmovBpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش اسرائیل خبر از حذف
«علی موسی دقوق» از فرماندهان ارشد گروه تروریستی حزب الله لبنان داد.
علی موسی دقوق ، بعد از سقوط صدام حسین، توسط جمهوری اسلامی ماموریت یافت تا به عراق برود و به ایجاد گروه‌های شبه نظامی شیعه عراقی دست بزند.
او از ایجاد کنندگان گروه شبه نظامی شیعی «عصائب اهل حق» در عراق بود و در کشتن ۵ سرباز آمریکایی در کربلا دست داشت.
اسرائیل امروز با حذف او،  پیامی چند جانبه و جداگانه برای حزب الله لبنان،
جمهوری اسلامی و البته آمریکا فرستاد!
فرمانده‌ای را حذف کرد که نقشی کلیدی برای جمهوری اسلامی و حزب الله داشت و آمریکا نیز از حذف او، نمی‌تواند خوشحال نباشد.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5547" target="_blank">📅 19:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5546">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
حمله پهپادی حزب‌الله به اسرائیل</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5546" target="_blank">📅 18:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5545">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ترامپ : اسرائیل نباید به بیروت حمله می‌کرد، آنهم در روزی که ما با ج‌ا در حال امضای یک قرارداد مهم بودیم.
اسرائیل حق دفاع از خود را دارد اما حمله حزب‌الله به اسرائیل چندان جدی نبود، کسی هم کشته یا زخمی نشد، می‌شد بر روی آن چشم بست.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5545" target="_blank">📅 18:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5544">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">قالیباف پس از حمله اسرائیل به بیروت : ادامه مسیر توافق با آمریکا ممکن نیست.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5544" target="_blank">📅 17:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5543">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePnQdAOntboq5Lh1HCcLfB0ECZHvWDg0g9DwWEhshThjSNZ-OHI9bLbV2YcCh7q6uDVztbKV3GhbUHL7pSTFYomqWReDFbH-hDMqiFzN5cTBVxJ2-9uNwiihtByx1C1sGPDuvp154cupJmuI8JNBwpuUuh_rbM8cU2UEGj-lImR35syvWGzbG5PnUu6ZtU0xGOGoMlFFTHTpC5IOMJow2NSy-wKJEVGACMWslwirOGTxnZJy3i1drqtMtKTzL-LFykYZ8QUlPqxllhe5nJtKSFY7WqTQk1ZoaidZ5L2g2av1O0-3M404JHLiHw6X972FJEvwBEvApzxTbIgCo2wkkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسرائیل در حالت آماده‌باش کامل،
در پی افزایش تنش میان اسرائیل و حزب‌الله و تهدید جمهوری اسلامی، سخنگوی ارتش اسرائیل از اعلام آماده‌باش ارتش اسرائیل برای پاسخگویی با حملات احتمالی ج‌ا خبر داد.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5543" target="_blank">📅 17:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5542">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=Bhp4hQSNo5NgCzWdIVRLxhyw7QEqyGRfXx2y9jOQwdr0fW-hhhYBqdpiaJLeftM0uVB0FOGJ9cX5Ox41mUEFopngFPvjTj9NsJojnz3yDkmp7IFNyPoEoU2rg3VoZDJth5qvYjIF2HVAZKk_AgrDAiqyhLbXsJ25KnQ-Yib-9MltHcYkZioWvj7HVGWwkTdS9NBHVcLM0YUhWbE9njtYxCHdBkQ3HXd5cb2Ny4nAo4I8nzCJAN27gzlWslM5XkE9k8HW4-k_GRly5TSyWdYWvDQXXHBAyZgNJYW1h8r7x1k8-GmMtV3OCbns40sp3YdyfAfh5Noa525DozYz9EkFBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=Bhp4hQSNo5NgCzWdIVRLxhyw7QEqyGRfXx2y9jOQwdr0fW-hhhYBqdpiaJLeftM0uVB0FOGJ9cX5Ox41mUEFopngFPvjTj9NsJojnz3yDkmp7IFNyPoEoU2rg3VoZDJth5qvYjIF2HVAZKk_AgrDAiqyhLbXsJ25KnQ-Yib-9MltHcYkZioWvj7HVGWwkTdS9NBHVcLM0YUhWbE9njtYxCHdBkQ3HXd5cb2Ny4nAo4I8nzCJAN27gzlWslM5XkE9k8HW4-k_GRly5TSyWdYWvDQXXHBAyZgNJYW1h8r7x1k8-GmMtV3OCbns40sp3YdyfAfh5Noa525DozYz9EkFBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدونید که هیئت پاکستانی
هر بار که میان تهران، برای مذاکره نمیان،
میان تهدید کنن!  که رهبر و فرماندهان
شما رو بمباران می‌کنیم.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5542" target="_blank">📅 17:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5541">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=KC_Gj4ngpE_UcY1jfqKEPANk6nNP60mcHmysD-KjTyJPfE05hr_CaW88mQ2kiKL-HGQBA3uUwVJCs7ju9icaYcyz2UoZCN6tfY0t8WVDEs3Dd1ocFitSf2Ujx-caXtdB_uxJC6mkgOdIKupXyjlj2ZIVycwQIRb_DIdfbf1Pjzovm1WJ5Gp4M0F2aAYdbAObKh01-7JjP5fNIhCswcCNNeVfGKSyExYC-75gQPxMgczogoF0R0p9uFZVHquEeizVAFalUnS4Mdsd6S62cfUC85IhhS2WKdN1H_xM4H9KadVRgItgTcwY1pbLtPuvQnA3RFLPqSa8jiZj9DFK7a2guA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=KC_Gj4ngpE_UcY1jfqKEPANk6nNP60mcHmysD-KjTyJPfE05hr_CaW88mQ2kiKL-HGQBA3uUwVJCs7ju9icaYcyz2UoZCN6tfY0t8WVDEs3Dd1ocFitSf2Ujx-caXtdB_uxJC6mkgOdIKupXyjlj2ZIVycwQIRb_DIdfbf1Pjzovm1WJ5Gp4M0F2aAYdbAObKh01-7JjP5fNIhCswcCNNeVfGKSyExYC-75gQPxMgczogoF0R0p9uFZVHquEeizVAFalUnS4Mdsd6S62cfUC85IhhS2WKdN1H_xM4H9KadVRgItgTcwY1pbLtPuvQnA3RFLPqSa8jiZj9DFK7a2guA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه‌های وابسته به جمهوری اسلامی :
خبر حذف دبیرکل حزب الله
در حمله امروز اسرائیل به منطقه شیعه نشین ضاحیه بیروت درست نیست.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5541" target="_blank">📅 17:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5540">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=qtifh02wNjV3PedpjqgjLS4xPt62MxUezj_QVfbZG6MZeWnKvRlKhCIizqTbenc5lyZqBYTp7gE3znLxLXuUfvMRFN_GKF1pQTp9raYUyWm3UwjjCV61rpEhqma2t9Hzeb4vQErEe2F3quoVsTeCxHiI9s-dKLORoC0eJ0gMlJO4L0nJbw2EAu8X39cKp6MDegAD99Hf0ao8n-42568vi8C4IRCjjKRTe7ygNQ97FLzoyN78q8t3jb-WBPbSyIuIJsjGPZEZz6nyZdZuzHrjDHfPH_SbzKCmfZkFZFBj4G9MhgmrcOyzBJbQXmXrf_m_dNSbsM4COmCYrhFzv-EIEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=qtifh02wNjV3PedpjqgjLS4xPt62MxUezj_QVfbZG6MZeWnKvRlKhCIizqTbenc5lyZqBYTp7gE3znLxLXuUfvMRFN_GKF1pQTp9raYUyWm3UwjjCV61rpEhqma2t9Hzeb4vQErEe2F3quoVsTeCxHiI9s-dKLORoC0eJ0gMlJO4L0nJbw2EAu8X39cKp6MDegAD99Hf0ao8n-42568vi8C4IRCjjKRTe7ygNQ97FLzoyN78q8t3jb-WBPbSyIuIJsjGPZEZz6nyZdZuzHrjDHfPH_SbzKCmfZkFZFBj4G9MhgmrcOyzBJbQXmXrf_m_dNSbsM4COmCYrhFzv-EIEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله اسرائیل به ضاحیه بیروت
حمله اسرائیل پس از حمله حزب الله
با دو پهپاد به اسرائیل صورت گرفت.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5540" target="_blank">📅 17:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5539">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=Vc_SAX4ryI4FO8Q8NspyuaOgpo3vRLNT9Eow6NrgM7_3Dnm5LNvDZA5OgHxk5JXwVUPRYna2PkSmdr1N5u-aQYUuE2KBK2_5KTLFr93Vl5Ww4fPQoWYN5gGTO6MDW5yI4LBqC5wAfQmmikQWMnllp088gboZUUXSHEbAdqY-FqpPMN4FEMDlKjB3cgpx8-yTFhyi-gg88ngDHpzmClkWXl-vDC01j3RGJE7waZkEB3S-3_VxcWo2hymmkkT8biR3yDDTufiedr5GuLQC4iuv_aHuObZI4YFsEkd6-6wDp46ZUVcaLZnndj1mltgmPx_wtyhsgqT49p-4IPKB3OrRPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=Vc_SAX4ryI4FO8Q8NspyuaOgpo3vRLNT9Eow6NrgM7_3Dnm5LNvDZA5OgHxk5JXwVUPRYna2PkSmdr1N5u-aQYUuE2KBK2_5KTLFr93Vl5Ww4fPQoWYN5gGTO6MDW5yI4LBqC5wAfQmmikQWMnllp088gboZUUXSHEbAdqY-FqpPMN4FEMDlKjB3cgpx8-yTFhyi-gg88ngDHpzmClkWXl-vDC01j3RGJE7waZkEB3S-3_VxcWo2hymmkkT8biR3yDDTufiedr5GuLQC4iuv_aHuObZI4YFsEkd6-6wDp46ZUVcaLZnndj1mltgmPx_wtyhsgqT49p-4IPKB3OrRPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان : رسول خدا و اصحابش
لت و پار شدن. :)</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/5539" target="_blank">📅 11:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5538">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
حملات موشکی حزب الله به شمال اسرائیل</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5538" target="_blank">📅 00:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5537">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=Zn5iPtwvLhtFm4ejbRIia_ABlOiwTiDtNFTfZN9qyAQhBzU0TH7Retf8T7RXUQMatxb6qL5HTMCGH5WBxrR69_qwDbUAQ5b7z6_ApfbS4gnzu4Jy8A_KyMi3tTDr4oVv8FwdkTOOB-gxpdo8jcJ17Ficax5MC3CoYnVwiw9-b9e92aMi1qIkJ7xzgCmjMeuYVggMVLhg4g-KW7VrPXfFjjfSpus-BBw3IpT3Ms2Hs3EnY_QlIdVlBMk6a8M5SLIE-BWTcqaSEdPlXOLGUgE4e7mpyLAS6aqBpQKxwwIUN1qNHzqAggM_ipFdu-8tRlHwjrrbpd4TLPqzGjwSU79lAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=Zn5iPtwvLhtFm4ejbRIia_ABlOiwTiDtNFTfZN9qyAQhBzU0TH7Retf8T7RXUQMatxb6qL5HTMCGH5WBxrR69_qwDbUAQ5b7z6_ApfbS4gnzu4Jy8A_KyMi3tTDr4oVv8FwdkTOOB-gxpdo8jcJ17Ficax5MC3CoYnVwiw9-b9e92aMi1qIkJ7xzgCmjMeuYVggMVLhg4g-KW7VrPXfFjjfSpus-BBw3IpT3Ms2Hs3EnY_QlIdVlBMk6a8M5SLIE-BWTcqaSEdPlXOLGUgE4e7mpyLAS6aqBpQKxwwIUN1qNHzqAggM_ipFdu-8tRlHwjrrbpd4TLPqzGjwSU79lAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زنان کفن‌پوش ولایی در برابر وزارت خارجه و سر دادن شعار : مرگ بر عراقچی بی‌شرف نفوذی</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/5537" target="_blank">📅 22:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5536">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8679568b89.mp4?token=rNQVGkjVMFwmquIK7um24l59J1mJyyu8LLBoxNlFDCo-LD9SjPAYfz2VwV98_PtfCaAtpruQ8B-3R7hyYljjyDTlaTIG-oiD_UEN49w3_fx9S7Szw-oKjLJuTE95Wif9x4tlW3ivSO8SdBAxF6xBkrr4Wq7jRAjHWc9pPwnWd-cCaY2PXFBFBqnmVuaGdceUzWM8LzKQk8WYwi4FSX1aaDlmk6txydaw5ar6WkmQMT21vy9yKwTFg_Lb2uZ1mzbdDRghxLQinmOXGvo8fqUDfOt9bNsCHGMsvRHT9Plx1A0D2zH4SBJoZTMMavrtGBDtz-WRkSgP3p0gv7-kbzT4uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8679568b89.mp4?token=rNQVGkjVMFwmquIK7um24l59J1mJyyu8LLBoxNlFDCo-LD9SjPAYfz2VwV98_PtfCaAtpruQ8B-3R7hyYljjyDTlaTIG-oiD_UEN49w3_fx9S7Szw-oKjLJuTE95Wif9x4tlW3ivSO8SdBAxF6xBkrr4Wq7jRAjHWc9pPwnWd-cCaY2PXFBFBqnmVuaGdceUzWM8LzKQk8WYwi4FSX1aaDlmk6txydaw5ar6WkmQMT21vy9yKwTFg_Lb2uZ1mzbdDRghxLQinmOXGvo8fqUDfOt9bNsCHGMsvRHT9Plx1A0D2zH4SBJoZTMMavrtGBDtz-WRkSgP3p0gv7-kbzT4uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی که گفته بود
به خاطر هسته‌ای
دو بار با ایران وارد جنگ شدند
،
الان با ژست پیروزمندانه! میگه قراره
در داخل خاک ایران، اورانیوم غنی‌سازی شده رو رقیق کنیم!
یک ملت فقیر شد تا اورانیوم اینها غنی بشه، دو تا جنگ راه انداختن،
حالا میگن «در داخل ایران» میخوایم رقیق کنیم! ژست پیروزی هم میگیرن!</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/5536" target="_blank">📅 22:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5535">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=VRBqP1E0gokN_Dz6vcM7FMp1ExWfjm9AFCCh4SsgWbGnNZvAd3mcvRptajQP5ZAI523ErHXwfY6VMDc5iIQIHHKAfmd06AcbQ-8mgWzk7GvQlXeFmDhY5A_uvMD1zeZs1DYOwGVt62JeM9lmlrwQhdMP6Vaye_gNLbKVYc4TUrXduhVeWNGaEQE0NBlvoNMSxPnFESqiK6pfQStifT33wv0o3Y3ecpQ5BT8hPxjjgBBJ_HEkGaDRP7JK7qo0-2IDcjBGzd3KBnmdarC9485uT0UUPdlBEqBv5j5QcLWTQqqL8dpNeL1K3JNOS9s2na1x9YaKoPZW3MeJzDs4js9IVUO61mucsu53dZ-CGIveKVtmRBNFPk8AXTGI2DkQgYdySZyt6MQQ4haMoppE2mslxI3X38lYi5zmB3WqHf7Gv8enwyQa-L0MAFmeLfpBcWotyUjyiEHRP1kMmJaGi8mwgOKZ6f1d439E8HmLbt2ZMoZVO5GLqXjcU86Af2XwY8t9Uo9fptsma6yNr7Czn6fNIcnp2VCTe-EMbfbEf_FBYjndXb-XQxiQ5vFYcoAUhpjHHJx-os_J2I1EYJclvm8souZPnzw0qj1QkXAqDcSzaMlGvy57qRKxrd36U9tEeeN9TqhGd3ptrAvWpP2j-5nX-9S8hb6uWxn3h3qXGKp-U5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=VRBqP1E0gokN_Dz6vcM7FMp1ExWfjm9AFCCh4SsgWbGnNZvAd3mcvRptajQP5ZAI523ErHXwfY6VMDc5iIQIHHKAfmd06AcbQ-8mgWzk7GvQlXeFmDhY5A_uvMD1zeZs1DYOwGVt62JeM9lmlrwQhdMP6Vaye_gNLbKVYc4TUrXduhVeWNGaEQE0NBlvoNMSxPnFESqiK6pfQStifT33wv0o3Y3ecpQ5BT8hPxjjgBBJ_HEkGaDRP7JK7qo0-2IDcjBGzd3KBnmdarC9485uT0UUPdlBEqBv5j5QcLWTQqqL8dpNeL1K3JNOS9s2na1x9YaKoPZW3MeJzDs4js9IVUO61mucsu53dZ-CGIveKVtmRBNFPk8AXTGI2DkQgYdySZyt6MQQ4haMoppE2mslxI3X38lYi5zmB3WqHf7Gv8enwyQa-L0MAFmeLfpBcWotyUjyiEHRP1kMmJaGi8mwgOKZ6f1d439E8HmLbt2ZMoZVO5GLqXjcU86Af2XwY8t9Uo9fptsma6yNr7Czn6fNIcnp2VCTe-EMbfbEf_FBYjndXb-XQxiQ5vFYcoAUhpjHHJx-os_J2I1EYJclvm8souZPnzw0qj1QkXAqDcSzaMlGvy57qRKxrd36U9tEeeN9TqhGd3ptrAvWpP2j-5nX-9S8hb6uWxn3h3qXGKp-U5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توضیحات نبویان در خصوص وضعیت تنگه هرمز در تفاهم‌نامه
- به محض امضای تفاهم نامه، تنگه باید فورا باز شود، بدون حاکمیت ج‌ا، گرفتن دوباره تنگه و اعمال حاکمیت بر آن تقریبا غیرممکن می‌شود.
- هر بار که متن تفاهم عوض شد ج‌ا عقب‌نشینی کرد</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5535" target="_blank">📅 21:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5534">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E6OoQpzWJy2olhOgOuvKyj9Rog9ROqaQXTNN_wJ429qsvgP9Np0ddgO7j8_LIgA5jgbfiZWbwG69vSZNLgHHIGXownM20bf3KIDk2utmakM38JeyjOwkTZzRzKVpRiheV8eNxJv3KYoo5XogYqNPYwMXxHhXGgG4V-0IsrJ6uGJSP4vVktzHxAu7oZmTRqcDvJdS-dXPqrrWAaewm8siqu5DMuSl8Fd6t5G8qqcEdcLmEAXsQErMrZ8ZHwoFFFKHVvlJ9UOYBD5lB7ZfEeEVaGM1Xah3y5mzIRpfP7EBXgP9Xz5zLThjhiRMqg17dREakRRhX6cbBZnagNyx-Jt8RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: اصرار ترامپ
بر امضای تفاهم‌نامه در حالی است که مقامات ج‌ا  صراحتا گفتن  تفاهم نامه هنوز نهایی نشده</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5534" target="_blank">📅 21:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5533">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=qfdDpTDliuaSOSULrpy2577w_MUtqfxpDqs1iimzZQfRtpJPKH0wkVewguZf2Ao6LRvQL03nOa2GanPrD3befSX0JF5drtcpnXqPq4y-Oa1xOBzhmN3K8VlzLwr_kH4X_sSvbCERDJVSYRYN908haWlhh0CCgwvsyUnOs4owJxFIsuzoBTMTKVLT_kS1GmTJCRaVWtvULWRhirizoyN8IYmCGZbEEONaODze7QnLgQkahYISUOurkiGOM046gRfdAO_afTLufueFwHBSD6XNV5UD6QmQTzu2hsMIZWmF982Prx3urhXDRDm_oDh892ICpO_GC9c2omHpGGQjxJ7HBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=qfdDpTDliuaSOSULrpy2577w_MUtqfxpDqs1iimzZQfRtpJPKH0wkVewguZf2Ao6LRvQL03nOa2GanPrD3befSX0JF5drtcpnXqPq4y-Oa1xOBzhmN3K8VlzLwr_kH4X_sSvbCERDJVSYRYN908haWlhh0CCgwvsyUnOs4owJxFIsuzoBTMTKVLT_kS1GmTJCRaVWtvULWRhirizoyN8IYmCGZbEEONaODze7QnLgQkahYISUOurkiGOM046gRfdAO_afTLufueFwHBSD6XNV5UD6QmQTzu2hsMIZWmF982Prx3urhXDRDm_oDh892ICpO_GC9c2omHpGGQjxJ7HBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۹ ماه پیش
بعد از جنگ ۱۲ روزه و قبل از جنگ ۴۰ روزه
این تهدید پذیری اگه به وجود آمد پایان نخواهد داشت.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5533" target="_blank">📅 20:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5532">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJkxYMDRFsqenzs9jCV7Et1WG4RJ0mZpc8kr_OZ8AuD59tarXFYnG836ixQEWN_DTQanNJHsylQaqY-yt8m6uYEC2TAOTBnr2ZgSw6A_4LJ24EO_B7QwC1m9T2UJ3hET4fraObVAquF8J3NJQMqaefSu79GkFG_suX3FFk21SfZBnp5t0h5YaHbCkcpS6rWRzNVwX7zRvwFlMGMQ0JKYQzXNZ1rniOZSRdj83_sLXKTDf82MahOTwoC6Yg6aRCGs9kmHwVKKUIvJvJW-Ado5LRNdOta8W2SdTF7mHwwKSNqTRJywX0t6eMSVktg9AFb-vPMgEm59mhoZfQHXFVdB0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ اکنون:
توافق فردا امضا میشه،
هیچ پولی بهشون نمیدیم.
دیگه به سمت سلاح هسته‌ای نخواهند رفت.
تنگه بلافاصله باز میشه.
بعدا هم اورانیوم غنی‌سازی شده رو از زیر آوار
و خاک بیرون میکشیم و نابودشون میکنیم</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5532" target="_blank">📅 20:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5531">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PGNzy0IWcwIQOENKgkJuptLACWS9VE11OSp0kgF9rUfAfXYq7qgAo6Q6lVma4w7jnVzfW5Xfpwlx84NMsS2lnKdn_XZXeM7-OYedWEOrOFm28hdAj2lb9O3HDbaq5uFEOPEuDr6wn5m-u74YtNzGjrLtqG48jNGxUwVHYpHXMDdmjTR_waEVOlyjGK9UZq8R5MNQjtWUcdxEPvXtDBMU9NruJh6RGJshEXXRZCk4OcvZJhR1hBNHFAOaw3hPXKeQGDQaEOD3D8YzBvzXvJKSSnfdR_y4sm4pp_OECWnIjv7QOxx7ei5LHUOxdl54-2jImFCZLU1xMwyRM9EsRfcQ3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیسی خطاب به قالیباف نوشته.
نگذارید خط تسلیم و سازش با
قاتلان خامنه‌ای به ثمر برسد.
(نه سازش نه تسلیم - نبرد با آمریکا!)</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5531" target="_blank">📅 20:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5530">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMbhWpAtrVu0cLpECYqg8lGSgTZ1kSrPqIjEuOtTV4dzlyN8W2tFfdmdImI72mf556xwOyUKXeP2_hRu8yYyymK5mSjT7jzBzy6D2_U1tYNd2hb25yEPVPFAKlwfWajyF4riAKX8qM6VHQjzBPAw91enFPziJsVh4N7Au4GaXAa6nEOdUWxbHVGW89c3o-1S86S6XPyKFeazSExqeWtFq0pgLZYVKy0o9KuqGwYV7zWlYadj2XS7c-XyAsqoz8AwzZ8Oq1gfZ-JmStaFBDlcSmKzGwOIgV6j4JaBNzRlilT2tHLUfUyLvD8uxryfwD2d6SJskT8Vqbjdsn7MQHiLDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوسف رجی  وزیر امور خارجه لبنان:
«حزب‌الله یک نهاد نظامی غیرقانونی
و بازوی مسلح جمهوری اسلامی
برای بی‌ثباتی منطقه است. اقدامات حزب‌الله، لبنان را وارد جنگ‌هایی کرده
که هیچ ربطی به لبنان ندارد.
ما فقط میخواهیم در یک کشور عادی زندگی کنیم! نه اینکه همیشه در جنگ باشیم.
مردم ایران گروگان نظامی
تمامیت‌خواه هستند.»</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5530" target="_blank">📅 19:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5529">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">نخست وزیر پاکستان: تفاهم‌نامه ظرف ۲۴ ساعت آینده امضا می‌شود.
عراقچی : برای ۲۴ ساعت آینده هیچ برنامه خاصی وجود نداره.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5529" target="_blank">📅 17:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5528">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=isTSGiiYj7ARN_dN_zOYoQdq_3sDbB8JVBn4xH_uj0dRNrR8iib97yrFP7WiD1_3r6EAm5oDwJ01WPP-krvhkka8-Ga1a72s1D6tUBFvfxUXi7Z2c1AUGzOqmKhA3jOjYBh9kzZbEdj3WqZ7ZvE4DVdN98BMqoSKeTK9ywp9GrGzE4RiI4aJGxwFQNKEo91g89CsRkvJi9HGvG3jyY7xOWDG_4lLbkB_86nmMADsL-OiHCXFYFslaOP2gbqfITf2TiFr8LuMDa8CUDnlaO_N5hJOM0ZC9A12DErx4rvKHBRvsLL_E1w6HRtAWFOgTeKemSBjDcF0USDqhjMXA5J70A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=isTSGiiYj7ARN_dN_zOYoQdq_3sDbB8JVBn4xH_uj0dRNrR8iib97yrFP7WiD1_3r6EAm5oDwJ01WPP-krvhkka8-Ga1a72s1D6tUBFvfxUXi7Z2c1AUGzOqmKhA3jOjYBh9kzZbEdj3WqZ7ZvE4DVdN98BMqoSKeTK9ywp9GrGzE4RiI4aJGxwFQNKEo91g89CsRkvJi9HGvG3jyY7xOWDG_4lLbkB_86nmMADsL-OiHCXFYFslaOP2gbqfITf2TiFr8LuMDa8CUDnlaO_N5hJOM0ZC9A12DErx4rvKHBRvsLL_E1w6HRtAWFOgTeKemSBjDcF0USDqhjMXA5J70A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان مناطق اطراف نبطیه رو تخلیه کرد تا در مسیر ارتش اسرائیل نباشه.
این جنگ بین لبنان و اسرائیل نیست.
جنگ میان گروه تروریستی حزب الله لبنانه
که با پول و سلاح جمهوری اسلامی و به خاطر خامنه‌ای، جنگی رو راه انداخت.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5528" target="_blank">📅 15:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5527">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zq9Qc50HUyhmrRWgPMjhMeNzhGNTI5v5H6FDQWPmtumyIxrwNG9zEy1MJPYbJaZen5H9uBpqxqqBn_2aoBlOI2xQkrASNh9f6T1taium-MnPuDwAl9QJ66htZ2ft3SZNwXEONF-d2QDA9iElG3RZP3eOzUe_20ULe2n7Ro251mEJgc3p7jLAYgo5dBrvK_O8LUbGoXnMqLNIbnPBBRV3_YmmhNnur2s0fSY4S-gCqHW0OVcG8EZiSskUFycdzHKJJhoW93zPCUgGfzLsNxgWto9yEP9N6uygp3Es8YsL3GaO2-jXVohSmnv11Ba7laRZzKtP6pBaZOnGw-Gx1kXj4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی در باز بشه می‌فهمید
مجتبی خامنه‌ای در واقع همون قالیبافه!
چیزی به اسم مجتبی وجود نداره!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5527" target="_blank">📅 15:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5526">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hg-BeRkQgT87gj7wDEv-SQSlTT0EUmMdiyS2VjpDCwgBdBBxMNE4HpQ5SlGqP2qKVxQTpMcunH9Vq0tmqXxRGLFI5y0FRyPGgT7TgfH_1tHevG7A4StoA4RTVkomLMoCvM6FgSo1Ggp8Yre6wsiS_IFLB7rIfWsjioz5r79D8sF18HFTXk7SOTRrnIpf2jnKEI2QlFAZ4fVVvoSM9nbxNSFYb2vB_TblOMKBoBbMwoioblagxMNCuFrBtDlXwxJYyRkYzwlpIcN7VujOIXs2wcGJWv6C6vp1Mw-aGIq1qOE5ZgzqmnIt3Y4hLJQA6UkIIgSZfaCBLcEXuD5BO4QO3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : ارتش اسرائیل دقایقی پیش
به حومه شهر نبطیه، یکی از بزرگ‌ترین شهرهای جنوب لبنان رسید.
اکثر جمعیت ۹۰ هزار نفری نبطیه،
از چند هفته پیش شهر را ترک کرده بودند.
بعد از حملات موشکی ج‌ا به اسرائیل،
اسرائیل فشار بیشتری بر روی شهرهای بزرگ جنوب چون صور و نبطیه و….. وارد کرد.
ارتش اسرائیل فردای حمله جمهوری اسلامی
دستور تخلیه شهر صور  - بزرگ‌ترین شهر جنوب  لبنان - را صادر کرد.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5526" target="_blank">📅 15:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5525">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAfan6cda0Y8ccXrBlmWf_buTUXzczX8YQMD3lJaNWq510KVk49ynqDJb_eva-4wSU8P8u-QwKsfNI6rNg5Y0gTf31hGGjAW7yngWzDyDTMEcImLP9rE2UY-B7yRTC_N8A_Pq4s0djIBLwhauVyH33SGiuD4oR7U7VdNkD_km9aVMI0QPJeaDYybxc4eSFW0Hg1jo5m9aihHfEbBaltBcxXwueSVHEuMk-KvtKS_qmnDDLfiadw7zqupVxl0EGIFZy2QrOORqLWj7j5hEgUiWtl4tbB5fuXz_JLiyz1I9qTd8EA-d_Ki94OvX7iQGcsHuXQCG4G8WRbVQjGuYT4Qug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات مراسم تدفین خامنه‌ای</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5525" target="_blank">📅 13:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5523">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thVAp2Y6mpmaOSKTY2pQaTteCuRY6hMZmz7G-cEj6Gw_NvqisSbt6-h3-rGEATV9_sf-BYAsuWIhNDqQoEgyE-vcCTm9vXsZrOQEnzhU4sbPYY6WzC2uFcoh9Fz1efyrOGGKJGXpnMCEw9Ve2ml62tv1HKhUiojvSAPNaXaynRBXDCMtcJ6uyMe6MzXWKLE0_sFSIrIH1z1kKVe0ajr18-GQwuJ1UES60_bzIFdyWVjafxn6Vh2TpebCdofv_ilYNPObDoddEfY2yJlMv0EjlE3XtfFMKoOXtgyTJPJy6iKFrkiqKiFJflREIiFGaVOydIEB3WhZFCfJamx-Ph3Pig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=g2tlk85Pr6fdHbDYtJOP6Rpv7MFGnmXsCaFpbi8BATjjjEvtTlY268Z_P-0Tu7j5nFxEJjuXcxL00Erp-J1LQSydYNLBnGXKyMJy4e8gbgkNltlvsuQcUCpX4CZtIpIH1c-t0VuBBmZEFJDi760Iw-A8ll7De4eU7pit-9lC_8-53KjguXdMfJKHhyPP1cY6ZN6C0x200aKQ7tOLaRQ1rrxYc61YCwWtzaouLr4909pXNSUx0JfYW6gsxA5vgh1AlFiEMpQJ4Q5ywwfg3-do25wl-fmIcgPjv1UK9i_C7U8ah9VZKF3uzqiNSekS99xc2rLfhy3YB0xJzV3__ZUBTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=g2tlk85Pr6fdHbDYtJOP6Rpv7MFGnmXsCaFpbi8BATjjjEvtTlY268Z_P-0Tu7j5nFxEJjuXcxL00Erp-J1LQSydYNLBnGXKyMJy4e8gbgkNltlvsuQcUCpX4CZtIpIH1c-t0VuBBmZEFJDi760Iw-A8ll7De4eU7pit-9lC_8-53KjguXdMfJKHhyPP1cY6ZN6C0x200aKQ7tOLaRQ1rrxYc61YCwWtzaouLr4909pXNSUx0JfYW6gsxA5vgh1AlFiEMpQJ4Q5ywwfg3-do25wl-fmIcgPjv1UK9i_C7U8ah9VZKF3uzqiNSekS99xc2rLfhy3YB0xJzV3__ZUBTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز میگن دشمن جمهورى اسلامى
ايران اينترنشناله!
همين چند سال پيش تلگرام دشمن بود!
حتى «روح اللّٰه زم» رو به خاطر داشتن
«يك كانال تلگرامى» ١عدام كردند!
توی صدا و سیمای نکبت‌شون هم گفتند :«شاهرگ رسانه‌های بیگانه»! یک کانال تلگرامی!
قبل‌ترش وبلاگ! ستار بهشتی رو به خاطر نوشتن در یک وبلاگ کشتن!
قبلترش مشكل «روزنامه‌ها» بود!
چندین روزنامه نگار رو كشتن ، دهها روزنامه و نشريه رو بستن!
قبلترش مشكل راديو بود!! دهه ۶۰! امت حزب اللّٰه بیاد گزارش بده كى توى خونه اش راديوهاى وابسته به دشمن رو گوش ميده!
تاريخ جمهورى اسلامى همين نكبته!</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5523" target="_blank">📅 13:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5522">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5522" target="_blank">📅 11:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5521">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJSDj9IWet5xP5UbXTpvObGNq7CFLaQNweLBveH_Dfkgr9CUZMJdpyCuBWPkuNfxkngEr-K3Gi02xZP-XTEO4VMajuqyUGK7raGquyuukN02xc-HSZWDLdAPNreTstrZPT-SFqJMJRwcLkos3w6BpPToHcspnQEeJLoHchS2C1UxKYQlnS7UHYlP7XgQMEOn4b40Lf5umFK2J1qxWwTux98IEEX74v1-iPXaQhhL1vDQ6UV7TZ0GaMQ23XjsrMm_uWqGyBwPqXqUyPOGWXgWWvplzSw5wEM0hgxN9Ff1-_6O9jq8v4qYOYzeXENPzUI2Xzu94nX0g8tFvN0WO4jNHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگن ترامپ میخواد ۱۰ میلیارد ،
۲۰ میلیارد از سرمایه های بلوکه شده ایران
رو «آزاد» کنه،
و این رو همچون یک پیروزی دارند به حامیانشون القا میکنن،
جمهوری اسلامی بعضا سالانه
۱۰ میلیارد ، ۱۲ میلیارد دلار تخفیف
نفتی به چین میده! از سرمایه‌‌های مردم ایران!
اون بلوکه‌ شده‌ها توسط آمریکا یک روز،
دیروز و زود نقد میشن،
این چوب جراحی که شما به ایران زدید
هرگز برنمیگرده!</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5521" target="_blank">📅 09:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5520">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rREDTeMQB38NG5xL54Can2SZz_-dz0ptspffIoRaIndREhAZnIKoX3nfEvYnxpdIG0CTle1BJJoRPnOU5vF_e1wey38wIkS3QsY7QMI2FHvz1imu5CyK0lLWhuj1_6ao5IWsbYByx7Pa_8Ty4KrkiA5pKO5m9-ksxtU-k6s4QXcosmE3j4AVy72X6X5-gr4G1HqE0k2OltvmDYUNxbfLmlxnFi5mhidKf4nJWA2UVtnE4EuFCkiCOO5557VSMOumb3ROv0tgfJoTxv2NnpEYzMR1hArdPH8Ca7Wf9N1uvK6wgFb4QSh0_Gh3xQeNkOLiXILc_YsT4qQ4XdI3bW7Zgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5520" target="_blank">📅 01:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5519">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=WV_0o0THUk24mEC5OKARku60aNx6x1BLlGxSdK8bLmrRQC6Nu2imXVD7ykba451Ud8tBucl1kZ9Rla2LNEy428lA9vMQyGaCEM74vcHUkNTMl_9TuyCHxPqoGweWyO4SpryLgefSHvOqaSX7DbCxxIuwBpGLf_6jH8utkpXFlQh3SFXgUwxH96CDH3UT2LX62CP-_LUdSkQWIyuHu3M7La0oymQwKsBOAUIXq55QVFwvJe-Mr6fVGGyG1Z7rY1nowiaR_FbCaPHa8SoeDnc_M6Pu7UCEw-iSITWYwHWAFf99fAu5WkLfXcCWYTcTTf8yiLXp22_Qvaj-KWI1yQd29A5KBWPIYK1bQobTZYm9OFSnolfg3jjug-Yt4gPKI2fqz6WBEXl-KldUpSsRGWeSz4JnvRzCEERgunUULFRQ2Qe_V8d9wO38AWs47Qq2NOhkBvaIDnFSpQ0FPJC5ox8Lv2JIg6bgy_NhRJYg4lT7c71l36rFOzPklCJfygsUb9DnWGfxpihUTgxdk62C4_fjc2kqN8p4z_-4QNbyG-PW3yy15BLENuBb3sCSMMF_JRpgCfRNQg-SgXuoY3l7SQjgFoADrqSTSVzKoPH1hq4MIuBebagngn9W2Ibk9nOS1oQHbiQ6vc97eXRItpk8L4x4UU3i_7jlQeyXEJkrIb3Ff7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=WV_0o0THUk24mEC5OKARku60aNx6x1BLlGxSdK8bLmrRQC6Nu2imXVD7ykba451Ud8tBucl1kZ9Rla2LNEy428lA9vMQyGaCEM74vcHUkNTMl_9TuyCHxPqoGweWyO4SpryLgefSHvOqaSX7DbCxxIuwBpGLf_6jH8utkpXFlQh3SFXgUwxH96CDH3UT2LX62CP-_LUdSkQWIyuHu3M7La0oymQwKsBOAUIXq55QVFwvJe-Mr6fVGGyG1Z7rY1nowiaR_FbCaPHa8SoeDnc_M6Pu7UCEw-iSITWYwHWAFf99fAu5WkLfXcCWYTcTTf8yiLXp22_Qvaj-KWI1yQd29A5KBWPIYK1bQobTZYm9OFSnolfg3jjug-Yt4gPKI2fqz6WBEXl-KldUpSsRGWeSz4JnvRzCEERgunUULFRQ2Qe_V8d9wO38AWs47Qq2NOhkBvaIDnFSpQ0FPJC5ox8Lv2JIg6bgy_NhRJYg4lT7c71l36rFOzPklCJfygsUb9DnWGfxpihUTgxdk62C4_fjc2kqN8p4z_-4QNbyG-PW3yy15BLENuBb3sCSMMF_JRpgCfRNQg-SgXuoY3l7SQjgFoADrqSTSVzKoPH1hq4MIuBebagngn9W2Ibk9nOS1oQHbiQ6vc97eXRItpk8L4x4UU3i_7jlQeyXEJkrIb3Ff7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5519" target="_blank">📅 00:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=HZbsxjsyCbXCFw-_YcyxcwqXTEcCTUfKTXetz2R-f8ribX3mcQebbR-WZKI_WV0k1s-X4FSKZq_yxlkuEPJZ7KSIKGxbnhDXKuu7HsA4B-ygCcOLMxG3dq_MyXJAmKl2_Wi6f5h0cbI9oi3B27DlJTE9mr7Gj4DtdFMUYgvP_pB1QV4-6X5XkctccG269LA55fBmM61FNxizciuIA9AXn1NE_dM3eJUIuNEc9JKuY8NUX4hMVAq1oRokVYmJIze8f6TraxhxjSR47__gGxnXYfD7lARMGycBhPCTak3JPm9ebDACLDsdEzUNQXLsG4hiZbk08iGPbS3yTwXk74N3Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=HZbsxjsyCbXCFw-_YcyxcwqXTEcCTUfKTXetz2R-f8ribX3mcQebbR-WZKI_WV0k1s-X4FSKZq_yxlkuEPJZ7KSIKGxbnhDXKuu7HsA4B-ygCcOLMxG3dq_MyXJAmKl2_Wi6f5h0cbI9oi3B27DlJTE9mr7Gj4DtdFMUYgvP_pB1QV4-6X5XkctccG269LA55fBmM61FNxizciuIA9AXn1NE_dM3eJUIuNEc9JKuY8NUX4hMVAq1oRokVYmJIze8f6TraxhxjSR47__gGxnXYfD7lARMGycBhPCTak3JPm9ebDACLDsdEzUNQXLsG4hiZbk08iGPbS3yTwXk74N3Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت نبویان از متن توافق ج‌ا و آمریکا :
یک : طبق متن تنگه هرمز باید باز شود.
‏دو : تحریم‌ها برداشته نمی‌شود.
‏سه :در مسأله هسته‌ای مستعمره آمریکا می‌شویم.
چهار: آزاد سازی پول‌ها اعتبار ندارد.
‏پنج: هیچ ضمانتی آمریکا برای اجرای بندها نداده است.</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/5518" target="_blank">📅 19:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5517">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">وزیر دفاع اسرائیل: از جنوب لبنان خارج نخواهیم شد!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5517" target="_blank">📅 19:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5516">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5516" target="_blank">📅 19:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5515">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5515" target="_blank">📅 19:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5514">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
عراقچی : هرگز تا این اندازه به یک توافق نزدیک نشده بودیم.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5514" target="_blank">📅 18:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5513">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hM7ldggYOSltiz1So1Mk1-vDwicavOQbd7DPqLW8e6J0Qv9CoeB1WeJjk_cH6pUVDbLdozeOW4ScqTIEHQrgPEYs25I6EhCtr-aZdlMj2Z7Dg8shRioIsJ1RQ7cFeK8VMARN1aSm6CKhK-QTOXmErMz1wWkCk9NmVxoFca8sv2nJVJ1EJdj5TZACBnBJU3xxhpBzhS-_hDwS1mQ2NnvI-VAaX-auoZrrWOK-0m6glgkQWAqaRSh8rsq7NrJY9sQr0C7XvSleoBQmKE6E6CHAXTBs30FDQjOchW1f26a4zcbblDQIYqE1CiRlogI3PiclezWSjSl49REzFrYan5Aqrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : این مواردی که جمهوری اسلامی منتشر کرده دروغه! اینها یه مشت آدم بی‌شرف هستند، اصلا نباید با اینها مذاکره‌ای بر پایه حسن نیت صورت بگیره.
حواسمون هست که دیشب هم با پهپاد
به یک کشتی هندی حمله کردند.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/5513" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=ILEfCRHwylG1yPfBXSChuUoF8u3Rl3kpC--uV9aVH_KQ1kLrXRRSnZLt93bON3OngDZpxzGMSs0Tpwdp4wbEBVWSdkoq0CexRfJyjc_Ajdweq64JW6jdLl8PHMKK0T6sz2OwjC2uNshU-xx6MwF8OzGbm3Uyh3-hlxE1vfY72dfcTXx4BJ8PWv64lz4ai1S2bnnx0pzsalVxvwa-sw4vfcwr-awwEBw6x6i4iQS_nj0SMro7tl2YPxOE1gDFvrVzde9N4epd2E10SiFQ3M2Z2qr8Mrj_byBPTi1BnSVYloyCyyw1ZvRFTzWHM-EyMchv4vF0ok6BSN96a5l18pQJIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=ILEfCRHwylG1yPfBXSChuUoF8u3Rl3kpC--uV9aVH_KQ1kLrXRRSnZLt93bON3OngDZpxzGMSs0Tpwdp4wbEBVWSdkoq0CexRfJyjc_Ajdweq64JW6jdLl8PHMKK0T6sz2OwjC2uNshU-xx6MwF8OzGbm3Uyh3-hlxE1vfY72dfcTXx4BJ8PWv64lz4ai1S2bnnx0pzsalVxvwa-sw4vfcwr-awwEBw6x6i4iQS_nj0SMro7tl2YPxOE1gDFvrVzde9N4epd2E10SiFQ3M2Z2qr8Mrj_byBPTi1BnSVYloyCyyw1ZvRFTzWHM-EyMchv4vF0ok6BSN96a5l18pQJIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امروز اسرائیل به صور
دیگه نمیخواید بهشون کمک کنید؟</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5512" target="_blank">📅 15:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5511">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
رسانه‌های حکومتی :
جمهوری اسلامی کنترل تنگه هرمز را رها نخواهد.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5511" target="_blank">📅 14:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5510">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVi9oRDReHniSqHFoEJKUbn77wwE4zUnSJuNq-E3KKViSYOzICtEh1E2HE07UY9Tb3olPPbe2zu_6v1c54Wg3gN5J9oc-okD4QbVUQM7LXfI5LqzvY_01rvuDTkBkRlTLuQ6ArkrYpL7tqEWSPQdnMA3Mj9a59F-IZvv3r-M6klXp_yTyh8pXEX_7bdIQVGgU1A8VO-tySYGnGDQ0zW5gZpd68S84ldQsqRNDZNbyN9PtEGygVKQqkjgz2uEtVe01pvdIPjEWab60ULgoqbaufiLkXKAD_m_TwiJbhlgTLW-tpjepeXIXH57hw_pp61BFh96Enr_B2_eGxOzOYlGRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
قطر خود به تنهایی حدود ۱۰۰ جنگنده بسیار پیشرفته دارد. شامل ۳۶ فروند رافال، ۳۶ فروند اف ۱۵  و ۲۴ فروند تایفون.
🔺
بریتانیا برای حمایت از قطر ۸ فروند تایفون در این کشور مستقر کرده.  قطر همچنین میزبان بزرگ‌ترین پایگاه نظامی آمریکا در منطقه است ولی اجازه استفاده…</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/5510" target="_blank">📅 12:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5509">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">حتی اگر همین امروز جمعه، جمهوری اسلامی و آمریکا به توافقی برسند و آن را در مکه امضا کنند، بازهم این توافق به شدت شکننده و عمر آن بسیار کوتاه خواهد بود.
آمریکا حتی در بدترین حالت، می‌تواند با یک «جمهوری اسلامی مسلح به سلاح هسته‌ای» کنار بیایید! آمریکا بیش از ۷۰ ساله که رقبایی داره مسلح به سلاح هسته‌ای.
روسیه، چین، کره‌شمالی همگی رقبای بعضا متخاصم آمریکا و غرب هستند و همگی سلاح هسته‌ای دارند!
۲۰ سالی که کره‌شمالی مجهز به سلاح هسته‌ای شده، نتونسته کوچکترین آسیبی به کره‌جنوبی و ژاپن و آمریکا وارد کنه، اما گوری  از انزوا و فقر که برای مردمش کنده بود، عمیق‌تر شد!
کوبا همسایه آمریکاست، ۷۰ ساله شعار ضد آمریکایی میده!  آمریکا اهمیتی نمیده!
مشکل اصلی جمهوری اسلامی، آمریکا و توافق با آمریکا نیست! مشکل اصلی جمهوری اسلامی داشتن سلاح هسته‌ای نیست! می‌توانست حتی، مثل همان راهی که پاکستان رفت، ج‌ا هم برود !
مشکل جمهوری اسلامی دشمنی ذاتی‌اش با اسرائیل است و تهدید موجودیت اسرائیل و مسلح کردن و پول‌پاشی به گروه‌های تروریستی است برای تداوم مبارزه و جنگ با اسرائیل!
آمریکا می‌تواند حتی با یک جمهوری اسلامیِ مسلح به سلاح هسته‌ای هم راه بیاید ، آمریکا عادت دارد!
اسرائیل اما قضیه‌اش فرق می‌کند!
پاکستان ‌و هند ۷۰ ساله در یک درگیری پر نفرت به سر می‌برند اما پاکستان هرگز شعار نداده که «هند را نابود می‌کنیم.»
تا ‌وقتی جمهوری اسلامی دشمنی و خصومت علیه اسرائیل را ادامه دهد، نمی‌توان به هیچ پیمان و توافقی خوش‌بین بود. خصوصا حالا بعد از ۷ اکتبر! بعد از ضربات مرگبار به حزب‌الله لبنان و بعد از  اینکه کار به رویارویی مستقیم ج‌ا و اسرائیل کشیده شد
و بعد از تجربه جنگ ۱۲ روزه که به اسرائیل گفت می‌تواند به تنهایی با ج‌ا وارد جنگ شود.</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/5509" target="_blank">📅 09:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5508">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=d4hP7zjlx6dJF2Fak0GyBJbf66MPyZOt3fsJSAUL-njD-fTl63mZV0huRVBsNiOTiNEwF6IyzK_139pEJzqpa0oExJNsk_Eblg-jfLkr4waOOI-jGGVXNLGtUQSDy22YGVdXXLqrRr7inOAJcCFWvpQ_9wC_0mQPPoOhZc8XLSm2RuwYJ-DjMLE4wsTCp8FO9g3QgWrvLS3llURg0FMLTA3S-i9yyMKcDGpTPY-lU7sHwNtaTWY9kV5QZQCdTDndr1b9eXHVOR65gfuqPGaPShchMRt7Mk3NRiEu5cplmf7jDTJJDc208wZwHB6uGVBNktV1QJWKc-bG2Nh_xpJMMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=d4hP7zjlx6dJF2Fak0GyBJbf66MPyZOt3fsJSAUL-njD-fTl63mZV0huRVBsNiOTiNEwF6IyzK_139pEJzqpa0oExJNsk_Eblg-jfLkr4waOOI-jGGVXNLGtUQSDy22YGVdXXLqrRr7inOAJcCFWvpQ_9wC_0mQPPoOhZc8XLSm2RuwYJ-DjMLE4wsTCp8FO9g3QgWrvLS3llURg0FMLTA3S-i9yyMKcDGpTPY-lU7sHwNtaTWY9kV5QZQCdTDndr1b9eXHVOR65gfuqPGaPShchMRt7Mk3NRiEu5cplmf7jDTJJDc208wZwHB6uGVBNktV1QJWKc-bG2Nh_xpJMMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاور قالیباف:
دو نگاه وجود داره، نگاهی که میگه بریم صلح کنیم، بسازیم، یه جوری مشکلمون رو حل کنیم.
یه نگاه دیگه اینه که صلحی در کار نیست!
ما قراره با اینها بجنگیم و قراره اینها رو تسلیم کنیم در برابر اراده خودمون.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/5508" target="_blank">📅 08:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5507">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=dQclX4WBfRzi8JMnWHkRxfgmkDBktN7l6v4K9Bb9cKSDyqvLBiIAMeZv2y_E-kAu1nk7MYrLNhS5XfQzS3BFne_7hWDy3n5xwncxtEVjyYvbOLxW8HB7JXQRXXmPQDMm0U950pDggPi0IG36Kfhwc138HghE_V3NWakQSjklwBi6hKorr9UV-h1z_sFh0LKyXCBy-uedFnctlcMLFf1ObfPXHVR5OEt15DnYB11NwldrJzsg5qUcbPGt4TIt-JKmoqrxiM9OfEsD0L2Y8dOff5dgFO1epeSW3GVOMf7ta0W8dh1yoaf3hUn2hmrIYZ4QRB5HLR2JgnoWvCtoLppsIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=dQclX4WBfRzi8JMnWHkRxfgmkDBktN7l6v4K9Bb9cKSDyqvLBiIAMeZv2y_E-kAu1nk7MYrLNhS5XfQzS3BFne_7hWDy3n5xwncxtEVjyYvbOLxW8HB7JXQRXXmPQDMm0U950pDggPi0IG36Kfhwc138HghE_V3NWakQSjklwBi6hKorr9UV-h1z_sFh0LKyXCBy-uedFnctlcMLFf1ObfPXHVR5OEt15DnYB11NwldrJzsg5qUcbPGt4TIt-JKmoqrxiM9OfEsD0L2Y8dOff5dgFO1epeSW3GVOMf7ta0W8dh1yoaf3hUn2hmrIYZ4QRB5HLR2JgnoWvCtoLppsIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی ظاهرا متقاعد شد که شرط و شروطهای ۱۰ گانه‌اش رو کنار بگذاره.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5507" target="_blank">📅 08:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5506">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">صدا و سیما : شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5506" target="_blank">📅 01:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5505">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
ترامپ : توافق با ایران باید همین چند روز دیگر امضا شود، با حضور ونس و در یک کشور اروپایی.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/5505" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5504">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
نیویورک تایمز:
مدتی کوتاه پیش از آنکه ترامپ حملات به ایران را لغو کند، با پاکستانی‌ها که با ایرانی‌ها میانجیگری می‌کردند، صحبت کرد.
به گفته یک مقام ارشد دولت آمریکا، پاکستانی‌ها به ترامپ گفتند که «ما با ایران به توافق رسیده‌ایم».</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/5504" target="_blank">📅 22:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5503">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک «منبع آگاه» نزدیک به تیم مذاکره‌کننده ایرانی گزارش داد که رژیم در ایران هیچ متنی از توافق را تأیید نکرده است.</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/5503" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5502">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
اکسیوس: ترامپ حمله را لغو کرد، چون قطر گفته بود که به یک توافق رسیده‌ایم و فقط مونده امضای مجتبی خامنه‌ای، اما حملات دو شب گذشته آمریکا،  هم ج‌ا و هم قطر را نسبت به نیت واقعی ترامپ [که جنگ میخواد یا توافق] دچار سوظن کرده بود.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/5502" target="_blank">📅 21:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5501">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
ترامپ : حمله برنامه ریزی شده امشب به جمهوری اسلامی را لغو کردم!
گفتگوهایی با رهبران جمهوری اسلامی داشتم.
محاصره دریایی اما همچنان برقرار است.</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/5501" target="_blank">📅 21:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5500">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
ترامپ : هر شب بهشون حمله می‌کنیم، تا اینکه به توافق برسیم.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5500" target="_blank">📅 20:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5499">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">حمله‌شون هیچ کمکی به لبنان که نکرد هیچ!
هیچ ضربه ای به اسرائیل وارد که نکرد هیچ!
فقط یک پتروشیمی در ماهشهر از بین رفت و اسرائیل فرداش، برای اولین بار دستور تخلیه برای ساکنان یک شهر رو داد!  صور!
دیگه نمیخواید کمک کنید به لبنان؟</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5499" target="_blank">📅 19:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5498">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFVj9AGbczTWHkZfmb1caq_zkTVotU0lZyOQ_hIOIMu8q-EjQLgM9TaT6MvIcOH5Hcj4NRWtvSpnu1PjU3-4Anjgpy68mbAFJYxDBQ_CLc8_mbGeb_LW9_KWmvy1EbF_vDrrNB7dELLUt7Noxcxe__scnVqrKP3fP1VT-bMFitiyZZrXGbZJox3FnFa6K2OH4KOuzIWjdmmFmGkuR4yphPNCjIwdBPVB7qZ7GWXDGVKEzyVUEosP7GcXJJQmiRaouZvHldzhyDqJbgGbrJBSjpFs_1TWLLNkQBZoyv8cjTwzd2_Ajq87QXl9w-mPxCIiwQPZ3FWkJHJscOV8xzR6SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله دقایقی پیش اسرائیل
به شهر صور ۶ تن کشته شدند.
یادآوری : دولت‌های لبنان و اسرائیل  هفته پیش به یک آتش‌بس رسیده بودند
ولی ۳ پ با صدور یک بیانیه،
و حزب‌الله لبنان با صدور یک بیانیه
با این آتش‌بس مخالفت کردند!
جمهوری اسلامی میخواست آتش‌بس
در لبنان رو خودش اعمال کنه!
ولی نتونست!</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5498" target="_blank">📅 18:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5497">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=Ng1J17G_MwORVhkxX1_8coT-H8_NQFZFo8Xm11bn-59hKeeBfqbnbpEntLXXxincVQaN4dp1WIHdihRWSfkpf2wFQnOpukPO2Dq6L0BAMZL3RGx2LRnOuFC6gtp63rvFwMDFJlSZySmqbPmU-yDpgP9Tt3_E18t8h3AN06a9YpquMbkuZYUzct2AF5Ki0CclI_MdEvBg5B-VkkHtz4aw433ArP8OpOMLidXgL4g6XNilzHdVnyiMwYIlNVFHdU4vlu3zGjWL3OrqzfrfrPE96tIvDXnaReXS2jbzspJ1d_GNOZYCXnU_w-mmet8KNuhZHtCO-KRtJEjbF9Rh3EEeOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=Ng1J17G_MwORVhkxX1_8coT-H8_NQFZFo8Xm11bn-59hKeeBfqbnbpEntLXXxincVQaN4dp1WIHdihRWSfkpf2wFQnOpukPO2Dq6L0BAMZL3RGx2LRnOuFC6gtp63rvFwMDFJlSZySmqbPmU-yDpgP9Tt3_E18t8h3AN06a9YpquMbkuZYUzct2AF5Ki0CclI_MdEvBg5B-VkkHtz4aw433ArP8OpOMLidXgL4g6XNilzHdVnyiMwYIlNVFHdU4vlu3zGjWL3OrqzfrfrPE96tIvDXnaReXS2jbzspJ1d_GNOZYCXnU_w-mmet8KNuhZHtCO-KRtJEjbF9Rh3EEeOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی
باید بلند و علنی و روشن بگه
ما «تسلیم شدیم، ما تسلیم شدیم» و «
آمریکا بزرگ‌ترین قدرت جهانه الحمدالله
»
باید روشن بگن که رسانه‌های
فیک نیوز همه بفهمن.
😂</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5497" target="_blank">📅 17:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5496">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‏سی‌ان‌ان:
برنامه‌های نظامی آمریکا برای تلاش جهت تصرف جزیره خارک ماه‌هاست که تدوین شده، اما به دلیل این که این عملیات بسیار پرریسک تلقی می‌شد، پیوسته به تعویق افتاده است. این خبر را یک مقام ارشد پنتاگون و دو مقام دولتی به سی‌ان‌ان گفتند.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5496" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5495">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qANZOzOfxWDYMB0I8enI3zQkLmYX1rOxz25GKm0Q0zZhFjqjsJpBYs7ZShvzJ7lN8nQELEII8gOXs-stNh2K9_rs8TSfJ934ltYyGWXlhSi26sXV4LFzdpbM9kF6XmAOPqEBTIB7pNKFWOBmfZFj2gBZm-XSo0ogH6v7kCFee8Se7hAeqOGHmcRAAjkLQ49Vt_EzkCGLzldanDZyVKPJ3nKGNvaT1j-E3dbO_TUgJAmtfJhVRCtkSq7P1qTHWhcRGWK6WRxXJ7SToqw1yKw9kvC205HPJQawQlsVMe2SMVUeWoWzDJwpBscvGVvPAXS63hAZjCkf8DA_3ZpWKpbGwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه داری آمریکا : خسارات وارده به متحدانمان را از حساب‌های جمهوری اسلامی جبران می‌کنیم.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5495" target="_blank">📅 17:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5494">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامپ دلخور از رسانه‌ها :)
‏ ترامپ در گفتگو با فاکس نیوز:
«‏ آنها دارند با ما مذاکره می‌کنند تا به توافق برسند. این کار برایشان سخت است چون آنها مغرور هستند. آنها بسیار مغرورند.
برجام جاده‌ای به سوی سلاح اتمی بود. راه من جاده‌ای به سوی بدون سلاح اتمی است. می‌گوید شما نمی‌توانید سلاح اتمی داشته باشید. بنابراین آنها یک روز با من بر سر این موضوع جنگیدند، و سپس با آن موافقت کردند: شما نمی‌توانید سلاح اتمی بسازید یا خریداری کنید. بنابراین ما همه چیز را به دست آوردیم، اما رسانه‌ها آنقدر دیوانه‌وار پوشش می‌دهند.
‏مهم نیست من چه کار کنم، رسانه‌ها خواهند گفت این یک پیروزی بزرگ برای ایران بوده است.»</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5494" target="_blank">📅 16:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5493">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJg4G8xXYUZa5EX3mAAhF1ZanmBrFzGkMtd2PSYUKipvbF5XP4vAICOqg5Sn_brB3UR5kjtA0jxyZVDVwgtV0NMgpJ81dLUFWliZxqcT8dnVFc-sQEjzxITESi2WF1MRggQIDj9ZGkJ0_Q1aMJDD70KDm8eTHmzfS9lrYm4mAtULEHcgxNVXrXWyVsG0TIU2ehuNrcjXXG0MSN6SBtNL6a9WBJipYxMhRh9VT9MAYh1oiPG36m1TwWabOXCi7HJtuuiGU00hVfFDySjB2_JYUuHsHhpiP5ndNzmHcnH8YdFgoELYzUPu3a4oM5mYs8bi6sJDQXXZ0auf-6T0GqSwvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از انفجار در سیریک
مناطقی که در دو شب گذشته مورد حمله آمریکا بودند در واقع حاشیه تنگه هرمز هستند.
جایی که رادارها و سایت‌های موشکی و پهپادی و…برای کنترل تنگه ، متمرکز شده‌اند.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5493" target="_blank">📅 16:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JY65bPTBLi6IpQdwOLNELv7ms1g5Ju4lFij71ZE7QbcuFWY4-Wh9SUWn8-T9yiXN-3fHrE2Wf6mZnoW4QhD9w_7D7YCw6vNXQAAsxhwN3aO6ySqN2Bb-pmGjFvFMFqXF29Gzac-aBOHqf1RB9fXB6gnUltS-LjhMIGwwkib-XM48twYioIaADKCuh04YwpX0IGZzieAZxxIbwRKdqj9HUEe0WhT5nbNfbhc3aroi9TASFHOEo1vXksIG1757mfMy0FnU4vDQ8fLuN982xHI6QxWc4mfb4iThW-oBvMQ14xgZI7FpZigy7-4EbhoK9oHUaMYq-BGt6c_o-TIiXeRRfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اموال ملت ایران! که یا مصادره میشن
یا مفت فروشی میشن به چین
یا غارت و دزدیده میشن !
بقیه‌اش رو هم‌ میدن «مداحان»
و «رجز خوانان»!!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5492" target="_blank">📅 16:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UXa952AqzPllwMGOeYC2unQPEBnqyACZevDOe4I1XEQKF08cpkwmn4hQb97UNptbiDau6kNeZCJQ-AS2JxNGooYb8_05fJjt4JhpjoaMZaOZfp3e42etWfX7KPyZ7cepghE7qGogkwJx-o5Cm7XpH3T8c24bpPZy07Knhryi_qHYXsYQgQBZ6EXFKQQGsA9CiqhERNKa7ucSXw95b1CTS8pkrE8gviNTokL4QBnVa224yMnL8uM5xDrjtkj0woDd5uNevJ7iizKECJYHomK-DwYKW0p-nPiG68843-rEbPfxGckRLt4ucENApWCM3U0pjuDCwxY4op4jNvZvNlx9qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5491" target="_blank">📅 16:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gw21_lpAicwd2Qy1wlXXqcnPaYeTWUhsoNbxftkNI6eqPD5O05-aApo1Hl3kfMvon54XRK1AtZ-cEBpD3mj5mhxExSd5KcXgU3hP_CoeernAw5vkDX2AZ3B_CaUkIzvNgQDfwLnu6wlnmrgHwtY_UIYrCVBbxFd1uSZUbPFGBiW4lcSyMhicjw_VFuF2_iakv6MmZY4rhRJPfOHlVUVvXlAOv_bFsCZQWgeYwpq3OLrFBH8eG0xGmD6SJckCdY9CDrbco6EeHoDCMKztKV8U6HJFE-2ZH-dsrMbg-SY_q8E-C9NDuhbkaWuu12ajR7JuYPEb-m2yGGhmBiDdHz4lpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5490" target="_blank">📅 16:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5489">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">بیانیه ارتش اردن : شب گذشته ۲۰ موشک شلیک شده از سوی جمهوری اسلامی را رهگیری و منهدم کردیم.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5489" target="_blank">📅 15:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5488">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بعد کار به جنگ ۱۲ روزه کشیده شد در ۲۳ خرداد ۱۴۰۴ ، که دو روز دیگه میشه سالگرد شروع این جنگ.  اسرائیل، آنگونه که نتانیاهو بعدها گفت،  انتظار داشت که در اولین موج‌های حمله چندین جنگنده‌اش توسط پدافندهای بومی و….. ج‌ا سرنگون بشه اما نشد! اسرائیل حدود ۱۰۰۰ سورتی…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5488" target="_blank">📅 10:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5487">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sR4dAR2Gn772m6PEUq47devO6mtdSUD2d2HLeg45i_LdY6l2hyG7Vi8TARWuCjwR9-yK-ottCLPz4DxakVPp2QH7ro0w7wCyRqiJKqVrzxhFdRBfwBSGmvunbdYgjprkZcDk5IAumnxmf0x1MqQMVrsjOL7qHR-yRt5m3KwdmkrWvIAzZeZSqOv237UlDbsAYEGCKoYMLIlVvTzpda84DJ_E0N3QrF32D2ohskxasVsay7QD6EHHZBFxREotdott8y1V1UTAf9krsogu9eov9vNaxNca7CNj-gRpdvjjFtlbx0eZ9lxvyyXA5lbrQSzF4WIjFJDpkTmGwLDku-q72w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پاسخ به حمله مستقیم جمهوری اسلامی  ۴ روز بعد اسرائیل حمله‌ای بسیار دقیق و هدفمند به ایران انجام داد.  گران‌بها‌ترین و مهم‌ترین سلاح دفاعی جمهوری اسلامی رو یعنی سامانه پدافند موشکی  اس ۳۰۰ رو که جمهوری اسلامی پس از حدود  ۲۰ سال تلاش و کشمکش از روسیه خریده…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5487" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/163555b294.mp4?token=eunGjkJNf9ZI_eZhsZLQyGyFKljYMDJIw2MqRgE9fEC2hZKUOiqN7tmofU9PKHraS8FDKv0C2Wx0fmUWJ7YkF5BoOJ3YcShjE9HRG1RHU657xABxjxdC7CImbSzkoQe6GrE_KEYJhEAL0D1c5pr5p60aptUitSNraspFEZ67Z_9vahBs9u3yFYIXBPS-T3l7BDZ2zsVyFAuwBCelKo9YZ9JTmNHPV0Y_DKM6HTcDeK4IFHQC5rqn6JZVTYkYtAIsVBQVyMWndCP0_cCcnoz4NyRR-YkuUlArPtnx41aL1TB-LcwJy38jcSXKAjwxrhifQkT6ZLU0T8mPTgMqJUqSNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/163555b294.mp4?token=eunGjkJNf9ZI_eZhsZLQyGyFKljYMDJIw2MqRgE9fEC2hZKUOiqN7tmofU9PKHraS8FDKv0C2Wx0fmUWJ7YkF5BoOJ3YcShjE9HRG1RHU657xABxjxdC7CImbSzkoQe6GrE_KEYJhEAL0D1c5pr5p60aptUitSNraspFEZ67Z_9vahBs9u3yFYIXBPS-T3l7BDZ2zsVyFAuwBCelKo9YZ9JTmNHPV0Y_DKM6HTcDeK4IFHQC5rqn6JZVTYkYtAIsVBQVyMWndCP0_cCcnoz4NyRR-YkuUlArPtnx41aL1TB-LcwJy38jcSXKAjwxrhifQkT6ZLU0T8mPTgMqJUqSNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی از ۲۵ فروردین ۱۴۰۳  رویارویی با اسرائیل را از جنگ نیابتی به یک جنگ مستقیم تبدیل کرد.  در عملیات «وعده صادق ۱» ج‌ا با ۱۷۰ پهپاد، ۱۲۰ موشک بالستیک  و ۳۰ موشک کروز به اسرائیل حمله کرد،  دستور حمله مستقیما از سوی علی خامنه‌ای صادر شد، و جالب اینکه…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5486" target="_blank">📅 10:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CU33Ia88w86ZITaUdH2uN6QnMuk6LfjTs0cVErYd2nnNa0Bn-avJfaQH6FuZKlXvttc96TIP1JRZHrz-r9t-jUHvKn-AVmjk1pXdBQt-8aaM7AnHNba3npd7un8YvVF71WUR89L7utfJuUl6311YVrCMEwZ8371h1yFe00mVK0kRmwW1zClvjqKY42tR52ZVOHBBI1imfLFodaS9wW2Qpq1nObiqi7cJQ_ZcZrfefrGzNGqp3qn9q8nHFYs7QBoYi4SIqXQE1pAkZu_gBQOCW4_4gACDNqn-EMvIMwvIcLwgG7CUV5D-QSFF5IaS7BTkly9Hn0QeuRt38v_9ZGNv5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ غیر مستقیم با اسرائیل سیاست  جمال عبدالناصر بود.  ناصر فشار سنگینی روی اردن و بعد لبنان آورد تا اجازه دهند، گروه‌های مسلح فلسطینی از مرزهای اردن و لبنان به اسرائیل حمله کنند.  اما مصر خودش چنین اجازه‌ای رو به فلسطینی‌ها نداد! نگذاشت مرزهاش با اسرائیل دچار…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5485" target="_blank">📅 10:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5484">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArnWt2hD7_OMcO6Fu-zHHlkaUnpqJ-STZLMCIT-17KMFNHRk4BU-b-WadCS__QngC0geJhJHflqQC3beQ4WxJTCtQXd4O2kCczFd8XkQV51-cRTMr9KpoQEiZuafzd4wjHtn5odH5ivG2dwDbwImp7H9uVxHg0QIHvp3iIWn4lM3Xbhl9ZRO72tSXJEgJqN4mnoy2Tg_-iU1BiemFrHKdFMjruVnL7wLtRUJoWvdhE9u-gBrbHbZJcH-EfnXEr0CPo7eEHPTDuQR3Yu1f-VBkekm2UCCey0ZLddGf7KZkkjE8p1_6EcWotlv3LFy1Yav8Ynq3l69qZ6czH_6whjl_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی در ۲۵ فروردین ۱۴۰۳  برای اولین بار رویارویی با اسرائیل را از یک جنگ و نبرد ده‌ها ساله «نیابتی»  به یک جنگ مستقیم کشوند.  تا قبل از این تاریخ،  جمهوری اسلامی با مسلح کردن گروه‌های تروریستی مثل حماس، جنبش اسلامی، حزب‌الله، حوثی‌ها و….. با اسرائیل…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5484" target="_blank">📅 10:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tig1spRKtQYbfTxwfIOdH_rinbNy4I4Ui_3ZJQqO0ICB-D_HGagUYrxTevwltUSSCG7784dUo5MnrKsgShVSoVge83QnusxIkyWuweGDDml0f0QJwfdmmmXwg1E7ejGJpYkYYqhw2dngEGbwPtEr86VH421dHVahdIGDEFofekMBcbk0fflK9unDQgcBwB44FifwFmOpKKdaK0x-XLImgmNHRbXwi7PkJ4y5DSPQcGVkba-CGkFN74uL_dfXzE_6FY15MTTmSfZOpJQrbGnbMdhGvlLMUwBHtPBnesv8ha8ZMDADvY0ZkAIS3ophjr6G3j8OxGJDCe2sD-PP667nLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از مهم‌ترین پیش‌شرط‌های جمهوری اسلامی در دوره جنگ ۴۰ روزه این بود  که «جنگ باید کامل تموم بشه»  و آمریکا باید تعهد بده که دیگه به ایران حمله نکنه.  منظورش این بود که یک «آتش‌بس» نمیخوایم! «توقف کامل جنگ رو میخوایم»!  این‌ درخواست از اونجایی میاد  که جمهوری…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5483" target="_blank">📅 10:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5482">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">یکی از مهم‌ترین پیش‌شرط‌های جمهوری اسلامی در دوره جنگ ۴۰ روزه این بود
که «جنگ باید کامل تموم بشه»
و آمریکا باید تعهد بده که دیگه به ایران
حمله نکنه.  منظورش این بود که یک «آتش‌بس» نمیخوایم! «توقف کامل جنگ رو میخوایم»!
این‌ درخواست از اونجایی میاد
که جمهوری اسلامی کاملا فهمیده
که وارد دوره‌ای از جنگ‌های بی‌پایان
و گاه به گاه شده که به سادگی
دامن جمهوری اسلامی رو رها نخواهد کرد!
بگذریم که هیچ رئیس جمهوری در آمریکا نمی‌تونه وارد تعهدی بشه که رئیس‌جمهور بعدی ملزم به اجرای اون باشه!</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5482" target="_blank">📅 09:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5481">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
حمله به کنگان
ظاهرا کل سواحل جنوب رو دارند میزنن.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5481" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5480">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">گزارش‌هایی از حمله به تاسیسات پتروشیمی  در عسلویه</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/5480" target="_blank">📅 01:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5479">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
گزارشی از حملات شدید به قشم</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/5479" target="_blank">📅 01:11 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
