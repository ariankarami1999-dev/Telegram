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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 03:51:59</div>
<hr>

<div class="tg-post" id="msg-5588">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.
چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ سخت نیروهای مسلح مقتدر جمهوری اسلامی ایران باشد!</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/5588" target="_blank">📅 22:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5587">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=EKV-mxHILkQ25pkiYWeGMXFoA5nu0GnK601VfxkhIrmDmaDVqTD4AMTJSAmZ5EtkqXBA9H8nsWMGyZibx7FQbeZUK40ge0YafVcSc_TaL2e2YLnCUYlNzYTLb_-YmcFPCrI2OnAu2mZfcf5V3mru_FWPgZw7J09YhElH64umP-ul8TuZWnNgUHftJznDs7n45J6i4fiSEHL3SFUAJJn5vxeAk8ui3JBql4RtztO5KrQHYxV2purCnrwaobae-kFVTTEURo0RyKLIM6G8lMOZknzzm8lw-gQj0RIjUqUsibHVTD7tZCK663-VlslFjxJHV78s2KJfoacygfUNyF-XkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=EKV-mxHILkQ25pkiYWeGMXFoA5nu0GnK601VfxkhIrmDmaDVqTD4AMTJSAmZ5EtkqXBA9H8nsWMGyZibx7FQbeZUK40ge0YafVcSc_TaL2e2YLnCUYlNzYTLb_-YmcFPCrI2OnAu2mZfcf5V3mru_FWPgZw7J09YhElH64umP-ul8TuZWnNgUHftJznDs7n45J6i4fiSEHL3SFUAJJn5vxeAk8ui3JBql4RtztO5KrQHYxV2purCnrwaobae-kFVTTEURo0RyKLIM6G8lMOZknzzm8lw-gQj0RIjUqUsibHVTD7tZCK663-VlslFjxJHV78s2KJfoacygfUNyF-XkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خواستم بنویسم هنوز کفنش هم خشک نشده
که حرفهاش رو رها کردید،
یادم افتاد هنوز تدفین هم نشده!</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/5587" target="_blank">📅 21:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5586">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgmlffjzE_qrw0K4fcb3LQ2iexas8EVdu0cykiuoK4Fy6L_MD8sZL-s_CTNJup1hheqtReGr-ZtUQdaH6BSDhOAqzSyHbLrkU-ifQRnNxZcf2M1FULmSmUS3Ai9YT9hEJObZx4gSJP10kRBTTRdSdYNz-cOHNOMaWYgFYuIJ-ma6lrEvxJsDEppERlOQSHXfux3C6cwwdgc1iMlHS_AxH0JhGsvoGGGPBDiOtsZ57LFJ4jHZG3JsrEwAF7S3_9fQfJFLZk2smlIaPORCNezHOhFJrg9Vc8vO14AyAlAnDHV2xLDVwmLEikTH2NsEpRbJU64XtwDF1Mt7fV8lFhsbkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده دقایقی پیش اسرائیل
به جنوب لبنان</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5586" target="_blank">📅 19:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5585">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">واقعا فکر می‌کنید اگر جمهوری اسلامی
بمب هسته‌ای داشته باشه،
دیگه «هیچ توپی تکونش نمیده؟‌» و
امنیت‌تون تضمین می‌شه؟
یه سؤال: اگه بمب هسته‌ای چنین تضمینی میاره، چرا همین امروز با اسرائیلی که ده‌ها کلاهک هسته‌ای دارد،  وارد رویارویی شده‌اید و هر روز به حامیانتان می‌گویید «پیروزی نزدیک است»؟
اگر سلاح هسته‌ای واقعا مانع شکست میشه پس باید صادقانه به هوادارانتان بگویید : نمی‌تونیم بر اسرائیل پیروز شویم، چون اسرائیل بمب هسته‌ای داره!
اما اگر معتقدید می‌توانید با اسرائیل بجنگید و حتی بر آن پیروز شوید، پس خودتان هم قبول دارید  که بمب هسته‌ای تضمین مطلق امنیت و پیروزی نیست!!
پس چرا بدروغ میگید که اگر جمهوری اسلامی بمب اتم داشته باشد، امنیت کشور تضمین می‌شود؟</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5585" target="_blank">📅 17:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5584">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5584" target="_blank">📅 16:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5583">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامپ : تحریم‌ها لغو نخواهد شد!
بستگی به رفتارهای جمهوری اسلامی دارد
(اول صبر می‌کنیم ببینیم ج‌ا چی کار میکنه بعد در صورت نیاز، تحریمی رو برخواهیم داشت.)
ترامپ : صندوق ۳۰۰ میلیاردی سرمایه گذاری در ایران کار رسانه‌های فیک نیوز دمکراته پایه و اساس نداره! (البته این حرف رو خود ونس هم قبلا زده بود که الان ترامپ قاطعانه رد کرد.)</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5583" target="_blank">📅 10:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5582">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNTpIgWIVuzbRHoTGOwA9rElA9FQv7hvWUQVXbK-10dn9SS_0v71VrXTO4f60ZXKatjP2sXegayMEa5NlwI1GauZ_VBGdFQNS30uoKq15rcOKyYooV5tlldtESq0h3neVxCNLmqDq8PPJxQNsfEUqMh4yU2NI8-QRbzGfrrE2zmz6XpgUi2Qq65J0ZhDEj9pgmATvQA67utXwoYin10_W-cekLINiFMbsxYOXJf3b6hxWCOiCbVZjHprm0U7W7tumO5Gp1Cr3ImqtPnwYzjOjwepcmr6D1WXkFRSvZB6Jt52HjzmKUNHFqhLEntdnjKaeyXcgvJdIfB04R3bnQqIww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موساد و ارتش اسرائیل معمولا نتانیاهو را فردی معرفی می‌کنند  که بسیار پر سر و صداست، در حرف زدن جدی و قاطع است، اما در مرحله عمل، و تصمی‌گسری‌های بزرگ بسیار مردد است.  بنت اما متفاوت است او کمتر حرف می‌زند اما جسور و قاطع در امضای عملیات‌های پر ریسک و ضربه‌ها.…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5582" target="_blank">📅 10:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5581">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNmU520OyUOM_rUGL52o5V502SVZxiwXwbVtVswFYx07M6V9JLsPy9PvCLaQlq8p1Vuih4heDgmhog7ZgnjLJeAxR920bn28qdzJZa0XebH1IOYevKa3iNaBVXty7okhdxnoIzCtGr8NF6uJU8PE8_e9aYEOIjCEPXVJ6MGtsPo_VoMrXzKuKOfipkgKCraA9SGhkFGJ5GZowioxf7HLQT_sH1-N4uEn_U1X6AQ_oncogHZxY1IAxInA_8o5PsSoqObOfPK2ZgxXUFzDW6UIgw8JN23jQdVU1dixPYnqKvWZI44r7fXm1iNzjxfY4_IRZcwBnNSJ-aNsybIbbOIKBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">او که از منتقدین سرسخت نتانیاهو در زمان جنگ ۴۰ روزه بود و به او انتقاد می‌کرد  که ضرباتش به اندازه کافی قدرتمند نیست،  و اینکه نتانیاهو زیاد از حد تحت تاثیر ترامپ است، دیشب در یک سخنرانی نیز گفت که راهبرد نتانیاهو موجب شده است که درگیری‌ها طولانی شوند.  او…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5581" target="_blank">📅 10:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5580">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=TKwr1ad5noJF1gnrLSYu4g-i5Pxkg_pEfuMsr4Gpb5bHj4kUKW9743oreE4hRJio65LfDbvkkaEUexMWDtshdF1VRmXwLTunUlfJc0lRdde6BYxgoYVN0pxBusxr2JhMxGdWYUrOYS1mKKIti8fl7blWT4d6HdXgs_C35Nr5A4nXMi5Yw6ZGdgtvsw-r7LzB5FHFH83FEV7fkfmtuS1mE-B26KqIUKKoJC9FvHgb6DrnJPttDNKQLd3DuNkDIonnV_hYaGowKMQMGaLUR4ZR50gDiW06VAZPhjKArqbK4qH9YBH1sXW-7LA8IlczOzXTY0M2fndov4ap8WXR9p78Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=TKwr1ad5noJF1gnrLSYu4g-i5Pxkg_pEfuMsr4Gpb5bHj4kUKW9743oreE4hRJio65LfDbvkkaEUexMWDtshdF1VRmXwLTunUlfJc0lRdde6BYxgoYVN0pxBusxr2JhMxGdWYUrOYS1mKKIti8fl7blWT4d6HdXgs_C35Nr5A4nXMi5Yw6ZGdgtvsw-r7LzB5FHFH83FEV7fkfmtuS1mE-B26KqIUKKoJC9FvHgb6DrnJPttDNKQLd3DuNkDIonnV_hYaGowKMQMGaLUR4ZR50gDiW06VAZPhjKArqbK4qH9YBH1sXW-7LA8IlczOzXTY0M2fndov4ap8WXR9p78Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">او دیشب در یک مصاحبه گفت که دولت جدیدی در اسرائیل شکل خواهد گرفت و امیدوارم که من رهبر آن دولت باشم و میخواهم به جمهوری اسلامی بگویم که من بدترین کابوس شما خواهم بود،  تا زمانی که مردم ایران آزاد نشوند و  مطمئن نشویم که شما سلاح هسته‌ای ندارید دست از سر شما…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5580" target="_blank">📅 10:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5579">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5579" target="_blank">📅 10:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5578">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5578" target="_blank">📅 10:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5577">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPaPvDSmTle2Cn_G65P6D7joL9eWY8uSmXyTKApGiMx6iKdVabWUynDucceHk9hmkcpBOjAUrJH12OETK415QigsHOtoya0tFg0OvEXz6R9ARyJdzHkOAsBz7-9a5nvJhB1TwaoJ81oKTO34csYloluMiiYMhY-4TUyACRyUH8QyTr6VZmpORy3gPsD92DUQPf2j4tEaOb9BULarmsh2mJlTpeGrAOaABjvfQM4Yz_oupmJ9GvYohyCm068tMaGHUU2YQ-bkYXL73eJd84kmMxKaKfR8BFn0rjxlJ8sI29STuepOQB2ZB2gQtkIfo_CP3rjrdGdvyJlBLTbyio4Muw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اول هسته‌ای، بعد موشکی …
‏به مزدورهاشون که هر شب جمع میشدن، گفتن که چی امضا کردن؟</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5577" target="_blank">📅 09:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5575">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n7qhNLJwMGDM-12nsesYY_c-HiAUzQrGQRvKgp6BGsyrqXOc1bNoMu54tr8abDjZEMlMLljxBep9GtZMH3PH9F5BPSI2eMR61o-64qgC0_ihLybK4SlrpwCGlrMKvS0eDubwNmHGbiqry82M5lYBVl4PGNjA6Eml6MAHt2fbf1_6pQjyOrPVCqJT6woHGoQHURnzKuIF28FCJewzzwNeP0k-iAiB9O3elQcFY9KcQ0eGHtdocHCwswDkNlG8KIwhoGtGYHYuyz5wXi-F4UNAhSVpTWw4lwDScEbGIKtIeRPavWtvPBl3_D9hFjUFzbRDVyIvmSvcYnEYh47FjMBzFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dcXLR2WbeYqRCJYaZ2GzY2xvXLjXXSRf6xwNKCAw4-Bz0fVA9olh8xz9KmEK8ikcoUxG75voMhu3jqkCkCL2deXk-uOXWGBbGfNy1nEAlyucctGcgic7KT6apkoNi2DuiDgCtCTFxFBs80hzgHh4NhFEtyoRCMLK5tUFm1h6RNzwKR6yGq87EHWN60a0CxI0jN1qmQJmzixZ7XbCF7JI2axxIJ2w7eiLMEtDGzotkS8P4jD0FgLrY2i3bHEJhBFNVIGCCq434hDr18daE_P93-Xe2U7pjjAsOYJMpVSjufBVTFnlWeSfOoF8G_M6JDjJU1GE1-iS26z-Wk-SlK9zXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسین شنبه زاده فقط و فقط یک نقطه گذاشت!
نقطه او ۱۷ هزار لایک گرفت، دست خامنه‌ای ۷هزار لایک! رفتن گرفتنش و بیش از هزار روزه زندانیه!  چون فقط با یک نقطه دیکتاتور رو در هم کوبید!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5575" target="_blank">📅 09:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5574">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVG_ztyV0P_3m4VyfBtKxy6gMtx1td5H3osaROc8tPYdmMvyKjCp3O88Mis-yHX5TvvjjlCduuTSHBkXqaH3XCPDtX6g3UTk6Sg9s1IOFZ3uYdf9IkUCNL9Z34uOpoySZv6Ys-JoCocm-i59HO8B8lJ194fRnFPz_bG15fo5JmWeqtGX7KxKJjms26E1o6FxL3ebc_f0E5nAGfy2UxBjmm2pEPFFlXady8a_fUbTv459cwL17ukE4bmfbx_-RQRtmrUSsWdfqGSSJugIBj_rzlbsLiID1h2h9IBZ-cSt_7RrXKiYTwJJbKtnXx_BD1oJ-QmdsArMauCOUECjU-0Teg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنیده شدن صدای سه انفجار در قشم و تنگه هرمز</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5574" target="_blank">📅 01:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5573">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=I6TfowwLjfNPlqAbZIoorsT1h24MAT5dZIqq9EghdjTkTpL0C6t3SaYvoVNMStabHox940Pqth8ZenzweFo8bfh5WWNsnryNHVrqZyV8QD8D8Mmdp_zCQRkmGccYIPMuvMRN5nBOvfPZiUIbAH_cu8A1KAVnCuiFClgEYqonLUYDWsiwxnLECvdaLhsa8cOK5T5dlr_iIxYGC1rpnvX6Wy9aB584afcHYru7FRWdQVrNVgrGcp_7Wq2XCQteN7jfgJooxmGehDZc-vIXwKdlpTSAtJ8L_M6aUgb-5xPGobgCg66ww4ZD8XCME2kpIotQc72X3stQ2JqdhO8IXL1-q6Pb0v-2yOvpis-qROJdqmTStoU_2fy6WVS441Mdymatv_PZm8jC0-NyHHTzoh24kjEtrGR6GfnhJzjIcWjuikdksQtD6g5OLXspalnhMmqPgb48LKtkwim3G9mM6C7RKmqjBO9T9A4mqe1dqn1PC7LzAtBbk3yA7lW6hFlvdpFxniUzvWQhHoxOp6YB4sqQ-2K6ai6B86M3qrcDF-6khFwau--M8FE_KspN3U_n40Zvf6EUd2xQxfQv7nRcIh0oY199hE8BSdEyyRP8y8FSkfMwYVobqYxda8nZoD_Dd6eJaKlVtdN0cnzh0WmkZB3-mjuhKZHsCf-_rPHvcb8ldK8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=I6TfowwLjfNPlqAbZIoorsT1h24MAT5dZIqq9EghdjTkTpL0C6t3SaYvoVNMStabHox940Pqth8ZenzweFo8bfh5WWNsnryNHVrqZyV8QD8D8Mmdp_zCQRkmGccYIPMuvMRN5nBOvfPZiUIbAH_cu8A1KAVnCuiFClgEYqonLUYDWsiwxnLECvdaLhsa8cOK5T5dlr_iIxYGC1rpnvX6Wy9aB584afcHYru7FRWdQVrNVgrGcp_7Wq2XCQteN7jfgJooxmGehDZc-vIXwKdlpTSAtJ8L_M6aUgb-5xPGobgCg66ww4ZD8XCME2kpIotQc72X3stQ2JqdhO8IXL1-q6Pb0v-2yOvpis-qROJdqmTStoU_2fy6WVS441Mdymatv_PZm8jC0-NyHHTzoh24kjEtrGR6GfnhJzjIcWjuikdksQtD6g5OLXspalnhMmqPgb48LKtkwim3G9mM6C7RKmqjBO9T9A4mqe1dqn1PC7LzAtBbk3yA7lW6hFlvdpFxniUzvWQhHoxOp6YB4sqQ-2K6ai6B86M3qrcDF-6khFwau--M8FE_KspN3U_n40Zvf6EUd2xQxfQv7nRcIh0oY199hE8BSdEyyRP8y8FSkfMwYVobqYxda8nZoD_Dd6eJaKlVtdN0cnzh0WmkZB3-mjuhKZHsCf-_rPHvcb8ldK8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«روزانه داره ما رو تحقیر میکنه
ما رو به لجن میکشه ،
به رهبر  تهمت جنسی میزنه»</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5573" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5571">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQ7wqajq0ZM0Djx3nloCOAYEKVNE-_coIWbugO5HcxnqyFeYxNp_07XcztXY6nE3SMVoPA3rZmPRnBbR4QPHpWGt0NnOKVZ0kMSgFlWn26q6VdvRcNDLOsNtPdCPvqSlaIE3ryqCfH_dh2i32KvwB_-0YFkJgT4WvGeaUdAWB7aElHhojN_HN0_L_xiPb0qO3PeN0W5O0itZMIdyNgf_x6p4wX0cmZLRCPKvRNNThdPWkNR9skjJdofxvYuVI7PDuzmBjJojy_KljoM2a8ycryUC78dYgAALtBqU_dhQ2PlUrq4-YNuEu6QJneVW1ZANk94Oa8l_D4fefO0DQShRdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=jAemEnTVgtF-EMz-N911hnA_XKm21LRBOPyAq1iZG6xyVD1kpTtTCO8pQ17Afd1FA_V7m3u7xwIrTce-aXjKUQjSrwZanlymrMVjZ0KpkEq_YBtd5CPm_icaz1w8PIW8rbcK48f9p6bkqyBG9QTI__HXUrY42OEDjkEG0tfZzG7lwrwp30Wc16mpKQ2fVQSZyKodOBesgXqqVu1kx85mLQKKEtbOBloAL2g9ifZu3cR5RvRoEm6IyqLfZ9X1PaYpl4i-oPU9k06e4cA-PfQJC0x4qRaPi9kD9-1PCFjurtLle2S4x9o-_0Ic9WH4r0837mOOmVl26BN5EEewr85_dIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=jAemEnTVgtF-EMz-N911hnA_XKm21LRBOPyAq1iZG6xyVD1kpTtTCO8pQ17Afd1FA_V7m3u7xwIrTce-aXjKUQjSrwZanlymrMVjZ0KpkEq_YBtd5CPm_icaz1w8PIW8rbcK48f9p6bkqyBG9QTI__HXUrY42OEDjkEG0tfZzG7lwrwp30Wc16mpKQ2fVQSZyKodOBesgXqqVu1kx85mLQKKEtbOBloAL2g9ifZu3cR5RvRoEm6IyqLfZ9X1PaYpl4i-oPU9k06e4cA-PfQJC0x4qRaPi9kD9-1PCFjurtLle2S4x9o-_0Ic9WH4r0837mOOmVl26BN5EEewr85_dIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین فینال رژیم منفور شوروی</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5571" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5569">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=B4zLfaAYtmDB3GB3fp1XdYAMfZcgLDsFLddu20zYfZBtm7WgBM2TE_3PlGc7kiWjO5ZGR8XHY_HQRUodlB6nZybFQN35PPlUuYqRCPT_iT5X0LPlq5TwiYzLivL0ONZbvQjWgPGNF_tvJVyShVrqy-fNBa3zlTYN0PLu8o3JTKnHOHZlNC7X8ZPsYaaHnLiUbHCZ4bqQVJ7QDgwIGgpW28v-rlqo_KNu-4zu0RzCqWbGKKTR1m8_FjNk89-qIRr-4lF3Nh0E3VsKWiL_RbLCp6pOAPy7XHBxe0zeAQRfj1Wm1tQdaqDtIr3bnVaycsJ7-eW1qlfuoZ8WnbXG__YTjr8ApQtZEyUDj-9CLkkhv5gJ8qQbgnmbj0PYi9SpEaVd3nvo45ASqza57T8tyB7g55Ebui3190w7KlHZxiHDL4Ez02SlpUIF8qLUt5UvW_YTLsXxp7flRiGDPh0UKATjXHQt_Pfq3HTT-bsfXM_uInlqhwIPeT05S2ytW18NylOgpTzUmslyMdhSIBk67M11hJkmqwKwtIA71kkgM5KF9SVFoqwHirEMcgKWGYRTRxOAXbfgCXEhaL7aoEfg3wlWyMvMjbhEHKOMGRDzeZAnIOVCb6wUks-hPqQtnMTk0uoDoNFq3YCB28MRaa2nuhSbMuO4UnWisgiZwelXbFSX8Oc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=B4zLfaAYtmDB3GB3fp1XdYAMfZcgLDsFLddu20zYfZBtm7WgBM2TE_3PlGc7kiWjO5ZGR8XHY_HQRUodlB6nZybFQN35PPlUuYqRCPT_iT5X0LPlq5TwiYzLivL0ONZbvQjWgPGNF_tvJVyShVrqy-fNBa3zlTYN0PLu8o3JTKnHOHZlNC7X8ZPsYaaHnLiUbHCZ4bqQVJ7QDgwIGgpW28v-rlqo_KNu-4zu0RzCqWbGKKTR1m8_FjNk89-qIRr-4lF3Nh0E3VsKWiL_RbLCp6pOAPy7XHBxe0zeAQRfj1Wm1tQdaqDtIr3bnVaycsJ7-eW1qlfuoZ8WnbXG__YTjr8ApQtZEyUDj-9CLkkhv5gJ8qQbgnmbj0PYi9SpEaVd3nvo45ASqza57T8tyB7g55Ebui3190w7KlHZxiHDL4Ez02SlpUIF8qLUt5UvW_YTLsXxp7flRiGDPh0UKATjXHQt_Pfq3HTT-bsfXM_uInlqhwIPeT05S2ytW18NylOgpTzUmslyMdhSIBk67M11hJkmqwKwtIA71kkgM5KF9SVFoqwHirEMcgKWGYRTRxOAXbfgCXEhaL7aoEfg3wlWyMvMjbhEHKOMGRDzeZAnIOVCb6wUks-hPqQtnMTk0uoDoNFq3YCB28MRaa2nuhSbMuO4UnWisgiZwelXbFSX8Oc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : تا زمانی که نیاز باشه در لبنان
خواهیم بود. نبرد ما با جمهوری اسلامی
پایان نیافته.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5569" target="_blank">📅 22:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5568">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=vliEBXA0J_ymtqAhKIy8fhSgC8kItyFBuYGvnWJcX83rChkZEw6oc-McONOmKytah9KzSDWRuAEqwkTMm74eCttbH5KcXlS1xozNkiVkqhgm98S-N8u6QPzeMKBlBVnO2aX7rrngjEU-TbisOP0dW0v5iHm7mleI7O0m1QHWjYFycuifQBTSEZ5g5iiiKIYmtg5FCx6-eWx-U2MmjJU_HYJL8w3BRrhLJ3prYcWBERg3oyApWvRLnN2EnpxRtSlPpMRpEqy5QOz1k2Uftxl5YCR8Ka4fF32uSIzjlL2-1pxy_tAnAOMxZ1avcm9ccOzMGLwvK2pH1p8uR76ubacHwIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=vliEBXA0J_ymtqAhKIy8fhSgC8kItyFBuYGvnWJcX83rChkZEw6oc-McONOmKytah9KzSDWRuAEqwkTMm74eCttbH5KcXlS1xozNkiVkqhgm98S-N8u6QPzeMKBlBVnO2aX7rrngjEU-TbisOP0dW0v5iHm7mleI7O0m1QHWjYFycuifQBTSEZ5g5iiiKIYmtg5FCx6-eWx-U2MmjJU_HYJL8w3BRrhLJ3prYcWBERg3oyApWvRLnN2EnpxRtSlPpMRpEqy5QOz1k2Uftxl5YCR8Ka4fF32uSIzjlL2-1pxy_tAnAOMxZ1avcm9ccOzMGLwvK2pH1p8uR76ubacHwIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله دیشب به ضاحیه :)</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5568" target="_blank">📅 13:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5566">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AhCkvDn0thqk780x_N75I5lYkZ1qChYdTT3kpFAkL6orzbA2eqzLKrUK_dlY_98q2CeuCPXEourj1i9icBmbITAs9EcqTv3gsulUrSUBN-bpGRhYAkB33FQK01d97IUEQ01QgUPMvcgVOerRAuQ2HO_jUVTc16I6S0O5EzTgD84XRrpuuLS-nEC-zzis7VG1R1uSdQ0xrTbf_2ZyUs3Q5NvZABOPcPHTSclpaxuWB_wIF-En0ytTuQfIZ_y0Sv3qPkYMu-rPtUgGWEjrRx6lBuXn6_dco-DyBibR0akaFvH9dDR5TLtDi9jDk98g83Gcg2s__IndzjsKm07xNJ23Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pe771ReYIdekS6CAaRmbOsu3NXflO0TABJht_uao_QKzXmH22j4G24dAepXGK3at3_uRgeYwDD1GWQQGfmtxfRv9bVeYn-c6We3yUbT88OYm_HvDM_3tPe2eA5L3iL9ne-YtZILI2tF02-OE-riq_UkT9Tbffv3cXe4dxFozLyU9sDeapqFcRXM8MNNIkpAG6VHBQnBfQGXkQWjUnnBBe3UjYNMkGL-yInWxAdEQLOvLygHfUyPZT4WgtYLy4rIookXR2IZZKNGzLo3cGBB0BjUZYD_uDQHsDyJOjh2ZNWsEyGhrO6pc-iz-FnJG6W7a0ER-4YzGJd_35up5VQ-EIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5566" target="_blank">📅 12:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5565">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNjz_OV6yzGG8ZOvlXnXLb_IrlxQXNXQQsxOaO5xT0OxfvaroVoKuVf5BoswpgE9CLTyECDqVaqn0DaQtnjTDxUBEoBq-PoeqD3Y2l4eB_KU-1pJiGHr14_ooaoK4VyMuUyC7aJx9Tkw7_im55y2YNeGoxDw93hiGXxKWnuBxDXgk0XQNXv5CsZn8_N0IZL4nZaEcv-72GFW_ed3alOd4ttzXX1PbVRnYoBN6XDGmS2ErM_jifgyvuic9RGkXWBUItjAseJKwNjUDafk5LUZyzYoYJkOcJ72n8DCQMe3VZqXVRsEYZRbI8lbADO3m1geDseA0rqre0BKoIU7gdYpJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم وضعیت لبنان</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5565" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5564">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a31wtSyRWnKDXHLxwGjVEFTLz9G1hZxFyJoW5QidmB5oYhzwtZqB6ZhzFmHNvyCrNrzlcXwn4pXmHLoXh7Oy6ubEXW2xnGJPXKKRwywOc1McVkCbyHhzskg4RFsdH5Arzo2HAjQmDc3Om08dYOoGSg39qfibGDhODyKTAr1r1d8yGW7MhTYzstiSk7SrbUrC6wtVC2r7nNYMGr9BkLLjv6ulP8RxZKV23SV2iPoGi7gdZFXI9HLgCeSRCBOiSD5gbXfjmaGDjK7iRpg7UT5PuoHgukYpc28OMZAgZnaEhvrtFYD1zwhQA0waFrzl8iJTItRNnJPUTe6rdLbHkRVRYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون  امنیت ملی
و سیاست خارجه  مجلس دقایقی پیش متنی از سخنان وزیر خارجه عمان را منتشر کرد که بر اساس اون، جمهوری اسلامی موافقت کرد که  «هرگز، هرگز مواد قابل استفاده برای ساخت بمب هسته‌ای را انباشت نکند». این تعهد جدید به معنای «انباشت صفر، ذخیره‌سازی صفر و راستی‌آزمایی کامل»
بود که سخت‌گیرانه‌تر
از توافق ۲۰۱۵ (برجام) ارزیابی شد.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5564" target="_blank">📅 10:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5563">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">رسانه‌های جمهوری اسلامی،  حتی بیانیه شورای عالی امنیت ملی،  تفاهم ۶۰ روزه (که هنوز هم امضا نشده  و ۴ روز دیگه احتمالا امضا بشه) رو  «توافق» «پایان جنگ» معرفی و القا می‌کنند.  در حالی که چنین نیست.  یک تفاهم نامه است برای یک دوره ۶۰ روزه که طرفین اقداماتی رو…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5563" target="_blank">📅 10:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5562">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،  ۲ نکته رو به عنوان دستاورد مهم توافق پایان جنگ با آمریکا معرفی میکنه : ۱- پایان جنگ در لبنان ۲- پایان محاصره دریایی.  ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!  چون رسانه‌های غربی چنین موضوعی…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5562" target="_blank">📅 10:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5561">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYGrIlNIntlH1Jst7Q7gvnJ_Yw9BfjQJMmLHYsyplTQAkzeU3TEgnZBjRMq8nTW7jShybU6p9RZgXdkg4x65SHzPXrUkWl3sWMoQdM5HXhW2PCOjQta5fxjbwZNVcvXku0IaxGV2wx969wEoObk3a-oA4wRVzu9nlpvuYebEC5Dl8RdYyw7rYdGi4Uwilr-1o1nDfldgWrwP8Jv7qJO2XIorsepDGFBkJ-kkT60vQEBEdy1ApsS2y3tEPf-keYpZv7X3Yij9BdgxYV_mnLsVBkuKfWoG_2Pln50xe1fbaCKGaCvkcI7VDyKmxaJl9zKsGYjbjXLjUCRvJ1o1a8_KrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،
۲ نکته رو به عنوان دستاورد مهم
توافق پایان جنگ با آمریکا معرفی میکنه :
۱- پایان جنگ در لبنان
۲- پایان محاصره دریایی.
ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!
چون رسانه‌های غربی چنین موضوعی رو
به این صراحت ننوشتن!!!</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5561" target="_blank">📅 10:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5560">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=TFso1GNoAI7Fmxr310xDY2y_8O5w_XULf3fAK3YYjHwtez_O80dwRWEjletZ52PLKgnn3U-1PKu3nqppYhh9jo7ZqDWaM3dI7tihxym54C78ZzDSJsTf6Hy5pQYLpsClqYPIaRpniwxcjDilMf69hku7nQTQs1XbJTJbk8S9ifHAFiQjWWdMIuWy7H27Ugc4FmXn_622BZNC96l5wzczN5x8alvn3qwPdfF7YPYVSCCCkO_99CnXjMBWLdTbwUrLvlfGGxvvRVH-lx7Pjlb61s92jAOkTljp8nNFCtiClkEnt7unljcn-jbwGkZMbPxO-KlOk0IiMc3bSkMY4G2INA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=TFso1GNoAI7Fmxr310xDY2y_8O5w_XULf3fAK3YYjHwtez_O80dwRWEjletZ52PLKgnn3U-1PKu3nqppYhh9jo7ZqDWaM3dI7tihxym54C78ZzDSJsTf6Hy5pQYLpsClqYPIaRpniwxcjDilMf69hku7nQTQs1XbJTJbk8S9ifHAFiQjWWdMIuWy7H27Ugc4FmXn_622BZNC96l5wzczN5x8alvn3qwPdfF7YPYVSCCCkO_99CnXjMBWLdTbwUrLvlfGGxvvRVH-lx7Pjlb61s92jAOkTljp8nNFCtiClkEnt7unljcn-jbwGkZMbPxO-KlOk0IiMc3bSkMY4G2INA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام خبر امضای توافق جمهوری اسلامی  و آمریکا در صدا و سیما.
ظاهرا حمله برنامه ریزریزشده‌شون به اسرائیل هم لغو شد.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5560" target="_blank">📅 01:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5559">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NumZ6OFoSQ05J91rpPY50vcC7cnR_x_mZ47XkBRTZkrEiC4ZZwQ4ASEVBrmBpmhxzDHJLd9SgVVW0-kP_DnKdneTOnuoEaIoPj-Kbam79e9rTht0QF1mriVCuaMpD6Ik4pO46OVRwwQcRefcNu4EEtbxRbDr6TB8dZz_BPfAo1Ig2YeIk9f6RWHQk1y0URSWZcjTVNN8bE3OBhJyGS1fdNxRdWfUJt1uoBkAj7u2MgydsTdmGOZ028p0W-SOZGN-RIyzzdBKsjb3jiBS6MlEJg2MtV3MwSr6IIYeuU08UcYnAD7hETEiotc-huNS_7_WoyR0rpw37rUPscvxgpU6YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده تهران ؛ ترمز امضای عجولانه توافق کشیده شده. سعید جلیلی جایی نرفته.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/5559" target="_blank">📅 00:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5558">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
همزمان با تشدید تهدیدهای لفظی سران جمهوری اسلامی، اسرائیل بر شدت حملاتش به جنوب لبنان افزود و موجی تازه از حملات را شروع کرد.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5558" target="_blank">📅 23:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5557">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnxE_pgOAaHRg4d684v8KDbMeYd9uW9wR68hljygw7icIA5ZYlFdirQ0kHZ0VO3h3JvxgHwxqvzDpYlcRd81zElIWX5v7AcxqySSE6BxjCu95zvXqrkDx0OotWFA5qxCvYZ4Q0xT71TEQnGS731x4NXSDsfif_WvrTWX9KRg8ltiHQHRe8QRfA2JJ13ED03hnYNAU8AFXKakvsmkPh6_dyusTcW_moXwXOeBDC1_VcBER0DxQUL21Ya-dSXMvfoOXiJQBURgP6J1t0IbuC_oP3XmM5OgIiA4CgTOpt8wwR0Ld2-ZtjMJhRYOeMSIAopaEJLuZ3APKdP8MeadvnKXuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ولایتی مشاور بین‌الملل علی خامنه‌ای</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5557" target="_blank">📅 23:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5556">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5556" target="_blank">📅 23:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5555">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ST2lCw3KoyLLWq3qiDfQINae_JjsO-qWFZaaM90YTonajaUbnXY8xxoq5zexa9iXcVUfpZCNrHyQUwbRpArD5NqsTxMr6h0ofUVqTOH9NXfm_-LOe33EhGq3pNEWtEoCdCoprWi3H4CHbad1LBVwchPCgzov1HA9G4Pm98CePza5yFMNfEZiN0vpXY0K_np5iOSoOkUdr6xDo4MaKCNdUB6diwYcykgPHIf1J1S0TFRnFXXd5Wlqiy16-UxgpuHyMek6awclduKqwC_nyWgQO-cfm9yqkgqxJ3OOiqBQs1K4RgynxuObniJ7wg4i8kPB3KOyeSTH_ExO-FHTny6uCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف «تمامیت ارضی لبنان عزیز» !
«بساط جنگ افروزی اسرائیل
را برهم خواهیم زد!»
جمهوری اسلامی به خاطر حزب الله لبنان
دوباره میخواد وارد جنگ بشه!
آتش بس به دست آمده میان دولت لبنان
‌ اسرائیل رو رد کردند، به جنگ ادامه دادن
الان هم توافق نامه پایان جنگ با آمریکا رو کنار گذاشتن و میخوان برای حزب‌الله
وارد جنگ با اسرائیل بشن.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5555" target="_blank">📅 22:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5554">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5554" target="_blank">📅 22:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5553">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
لغو تمامی پروازهای غرب کشور!
آمادگی برای پرواز آبگرمکن‌ها
روی بیروت خیلی غیرت دارن</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5553" target="_blank">📅 22:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5552">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jW31McFqdsdHoOMK_JMwm8j46dsAKbj1W_y1ytI-vyICMK4pamg79Q2Yy9XXpAWPtzbylhv2LkcBeh-zwQVbq5uAe3sQtPYpR5mIhvFGdkyj2yq6dA6E6A0SshR5yYfHq42Y36fID6vUfdWA2EBzjsbM-C9LTPuJGBQLXiZBnw98dR8U0Xjh-2lfe9XF0En7hWom3xdhCyLoNE5Rg3WyUbJCl-nkNPH8ugVcO3ULJrp6BRH_Xn-28g1DSodg6DeSgIQs0oZUlaVxGl5011WaHn1yc7yb1FmU7PvXXq8R8LCy5j4niE6BVgqCqKupW5ESGbefAV4PbUUw83dtol_n6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای عالی امنیت ملی
«لبنان جان ماست»
پاسخ رزمندگان اسلام در پیش است.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5552" target="_blank">📅 21:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5550">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PdXovwTdqbolhRctFHSv2g3GgBJadqXmCKXnYIePcVQ_di3oWVd-T0EZyg6DaDiiTEeeDk5uQoYURLRl8HyVezjsUA-6dd5pQb5vZJD1dlPYwGdwzWuSCXeP6ESjoEvg81AQSWt0qUx3FtakfOA2iLydGQAfrAhaLSBT_se5FcglTHDL_rxEC80dr8Ywxowy4Bn0AcaFYc39gw6qEhyIh7f323EMsk7shCZtTlFgNyR5eZpXIbijOIpk-uZgOBV-bSJyZZ1nEgCnhmv3WqPUEtxBDSztWMV0oHR19iw_c8CLwgjK-JBxg352kXesYkk6GjHmNqu1RwHtX9wIqzCy_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ey_BDRYgw0cYfacctjtVOf0-u7yPboqE1HrU-kHHXphr_cqABShLF2dWiob-SBj3pakmw91N3dJsWIJEQGnyH802qNZRY2q6WK14Kfx3YM3UOedqNpMsHgjd4iyWNDM8vfLSUxfQdFMptkMIb2GFY2Rg4ekoXCWFqybaWL59zka8E2Hbmn2bAkA-doFKsA98PNwvUn0OptURPoF8KOU8A03R0Riza0TlJLRHCNVm7eZeQlegYuTCdTnK1Nzz87G1kBm5bHdO5KXYbpNaJ9AsTBsEXOe2gCsUK7Wp7MzfkgwumBEU33AV3quDM3CqsHC4p8b6xR1OsZUo_g8n0X9ckw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عزادار کودکان مینابه
عزادارن حکومتی!
میگه حکومت همونطور که در ۱۸ و ۱۹ دیماه «به حساب» مردم معترض رسید و دست به قتل عام زد،
باید دست به قتل عام معترضین توافق هم بزنه.
اینها هیچ وقت ایران رو دوست نداشتن
هیچ وقت ایران و مردم ایران و‌ کودکانش براشون مهم نبوده
اینها عاشقان جمهوری اسلامی هستن!
اگه برای کودکان میناب هم عزداری میکنن، چون میخوان یک کردیت به جمهوری اسلامی و سیاست‌هاش بدن.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5550" target="_blank">📅 21:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5549">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ترامپ : نتانیاهو نباید دست به چنین حمله‌ای میزد!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5549" target="_blank">📅 20:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5548">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
ترامپ : به رغم تنش میان حزب الله و اسرائیل، تفاهم‌نامه با ج‌ا امروز امضا می‌شود.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5548" target="_blank">📅 19:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5547">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/teticUpg4wJqQFetTtVtA6DwO4xS2C-FdIRvxkH5h8dYOPICOL7h4RNalbnu9D4erxsWOFby7678PPZIgBhAloVRHEpfa5uHucb9MwwcXILyDgEqBqhSo1EXrQAn24mJ-GHqKwBOLck0eA5jWneFaedVPRqc7BcUNcQ_waX5kRKFoc6JSsIKDJF5Dz8DB8NJMbHrQSsAd3C0xk7VRniUIyxivSAhAxVUj55eRQG-pFjKZ2g-lr6qJQBhZdU9MUCzCH0EIipx6IrEhYq4R-ISUZ3twxqg3yIIsLf9G3jo0vjbYjpFtbmbvTUYFeflTTsUQ4PDCUaOWYHsKRnR7Hv9zw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5547" target="_blank">📅 19:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5546">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
حمله پهپادی حزب‌الله به اسرائیل</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5546" target="_blank">📅 18:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5545">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ : اسرائیل نباید به بیروت حمله می‌کرد، آنهم در روزی که ما با ج‌ا در حال امضای یک قرارداد مهم بودیم.
اسرائیل حق دفاع از خود را دارد اما حمله حزب‌الله به اسرائیل چندان جدی نبود، کسی هم کشته یا زخمی نشد، می‌شد بر روی آن چشم بست.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5545" target="_blank">📅 18:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5544">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">قالیباف پس از حمله اسرائیل به بیروت : ادامه مسیر توافق با آمریکا ممکن نیست.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5544" target="_blank">📅 17:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5543">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uX6LepaTwzFd7kp7MyQ4hmpagyo_vDzqwvbsXSThb4DHOH-TIXba9IYw3KCoC7AOp9rHLe__fV4BL-srZuJMBd93IKtgke5jtompij029RrxrJaf3UrYg2r5ZNn3DiPg9nupajDGvoeccyNtc_mIb-nS2-DTUYWh7x_SRBqnBXJqpiOHqb51rA1Pl4vZ6MiXIArtF8fY6vWOwSJrnd7V2en9tWHKk7HAD9zZN-AiEdWoIJ7sqpvxABVIVmWXjcz44Cvx2y2sN29hijEOWfO9xNAISZgC9xK7qCcOJNA7y7DFlGnhxqTltS0yg6q6Fw_vT48QYQPx2eLBicgBz-I_yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسرائیل در حالت آماده‌باش کامل،
در پی افزایش تنش میان اسرائیل و حزب‌الله و تهدید جمهوری اسلامی، سخنگوی ارتش اسرائیل از اعلام آماده‌باش ارتش اسرائیل برای پاسخگویی با حملات احتمالی ج‌ا خبر داد.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5543" target="_blank">📅 17:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5542">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=Sr3bynEFLt8S3Q1-TCi5D_-cpRxThvGUC2XFceqKWAkt0igCzxXIbTyXvJMwNNawTzAMLiOcZMcmyhss4BOwDyID50LB4DUXi3l-sD4LnzKClcH_hBbJhkKyYWhZlXk7tEbJGoDpel-K4OjvXTHS4dEnkbzL_AaKXXxBmKIUYsELV-HcCnxN-YK3E1ryM7kvtDtMqgUh_bSsCUrajBsXiX-kIJHop1Gz8RDiuaCCSYLa7IX9UFlVzBhZDhYCIY2caBn1FffdPPApSYo_MiPaUi1BxeGgnIF_w-DyUwoYHu26y1PW1TqgDySSxsAB0avFhz2jZeRPeuzfjQWxcoAEUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=Sr3bynEFLt8S3Q1-TCi5D_-cpRxThvGUC2XFceqKWAkt0igCzxXIbTyXvJMwNNawTzAMLiOcZMcmyhss4BOwDyID50LB4DUXi3l-sD4LnzKClcH_hBbJhkKyYWhZlXk7tEbJGoDpel-K4OjvXTHS4dEnkbzL_AaKXXxBmKIUYsELV-HcCnxN-YK3E1ryM7kvtDtMqgUh_bSsCUrajBsXiX-kIJHop1Gz8RDiuaCCSYLa7IX9UFlVzBhZDhYCIY2caBn1FffdPPApSYo_MiPaUi1BxeGgnIF_w-DyUwoYHu26y1PW1TqgDySSxsAB0avFhz2jZeRPeuzfjQWxcoAEUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدونید که هیئت پاکستانی
هر بار که میان تهران، برای مذاکره نمیان،
میان تهدید کنن!  که رهبر و فرماندهان
شما رو بمباران می‌کنیم.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5542" target="_blank">📅 17:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5541">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=fbLlbgYs1TPgf7L_rfd-Kt1otME1RfOousL9wWWHAeFN0uSb_8DfiZszfJEHVBnWUpacyF5VAz8yqxni815Q72vW6Yr4egN9hIkvkwh2-dTqjrHnrsByCgs9k6hbVE0CW22pisupVhG4Es8fSiwDcsI2SmPTlCCVMfGy6_SZqqEnFUL4X1_01ZURNqGibEn8MhuNsnBppK43I2vyqUXeHh8ecDaLOf8PxwYJj9e6aKBGmkZQmOHHAqr8XYKGsU687l8AglLqhXdUGzuDJpp9ZIEIH9UkqDj-U6LmpfSHvc3WTrKSZqDQekBIXi7qFVgUDkWTJxU0k4m72CJeIc9eRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=fbLlbgYs1TPgf7L_rfd-Kt1otME1RfOousL9wWWHAeFN0uSb_8DfiZszfJEHVBnWUpacyF5VAz8yqxni815Q72vW6Yr4egN9hIkvkwh2-dTqjrHnrsByCgs9k6hbVE0CW22pisupVhG4Es8fSiwDcsI2SmPTlCCVMfGy6_SZqqEnFUL4X1_01ZURNqGibEn8MhuNsnBppK43I2vyqUXeHh8ecDaLOf8PxwYJj9e6aKBGmkZQmOHHAqr8XYKGsU687l8AglLqhXdUGzuDJpp9ZIEIH9UkqDj-U6LmpfSHvc3WTrKSZqDQekBIXi7qFVgUDkWTJxU0k4m72CJeIc9eRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه‌های وابسته به جمهوری اسلامی :
خبر حذف دبیرکل حزب الله
در حمله امروز اسرائیل به منطقه شیعه نشین ضاحیه بیروت درست نیست.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5541" target="_blank">📅 17:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5540">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=qIn-5k7XPUaMJ0x7Ixi_fKqW8a5zGVm5U_dEW-788VrGBDxkMhkXnkwhGrg0khp69h9EKvcbHIvFd5ayyw2xbWZF-Oxv8anzjLJ7wY_Iaf5LCvdmXJigLXwWSzFK4U0zTgY_yLWtVFzMkT1indGSEumxezM5cXjJ04-Taej4JT2CEPQXMVE5ximd5G8X8MzG8QeVkSLUIIaJKxi0fd4vbJpijeqb8ogFzvERSwtY7WA1Zm3CA5fL-mRQp-PBXPhnfnmMSQGGMjgmYvd1FP2SiCVkq4vo7yDu6dqbJT4NQTPJQwNpj3S9XnqplvGHsFrE6niM2xGxA2Nqc0diBJSh_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=qIn-5k7XPUaMJ0x7Ixi_fKqW8a5zGVm5U_dEW-788VrGBDxkMhkXnkwhGrg0khp69h9EKvcbHIvFd5ayyw2xbWZF-Oxv8anzjLJ7wY_Iaf5LCvdmXJigLXwWSzFK4U0zTgY_yLWtVFzMkT1indGSEumxezM5cXjJ04-Taej4JT2CEPQXMVE5ximd5G8X8MzG8QeVkSLUIIaJKxi0fd4vbJpijeqb8ogFzvERSwtY7WA1Zm3CA5fL-mRQp-PBXPhnfnmMSQGGMjgmYvd1FP2SiCVkq4vo7yDu6dqbJT4NQTPJQwNpj3S9XnqplvGHsFrE6niM2xGxA2Nqc0diBJSh_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله اسرائیل به ضاحیه بیروت
حمله اسرائیل پس از حمله حزب الله
با دو پهپاد به اسرائیل صورت گرفت.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5540" target="_blank">📅 17:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5539">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=bYEuRFgN_IjOq4dtBXtOPTv6yIJnyX7IYh5I5waxmZpzmKum5VDn2IEsvF0NhqpfaeOJhfCIzvo0orYyTSuIMrmGLjxt5_ui_U461_ZGDg2mo1GX-iv1EEFpykjOOBQPyxVW4PAfbG8U7elvguCP03rpDsNNFprIyCW0GDbsfHMyU_11X6sUUGeQItaN8t9b5whgnCxsygGXgg3cSMHiofdI9yzImVkNvUta1EHifbnI7v5kXmirSkvuEKcCBpKCjxT16yCYDCFXCL8ygKxseNGGUPB7cXnxJh29zwz-J2Y3cDJGzKRNQ8zKPdAMtDDG6dm12DRziXTEAtmYSJ88IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=bYEuRFgN_IjOq4dtBXtOPTv6yIJnyX7IYh5I5waxmZpzmKum5VDn2IEsvF0NhqpfaeOJhfCIzvo0orYyTSuIMrmGLjxt5_ui_U461_ZGDg2mo1GX-iv1EEFpykjOOBQPyxVW4PAfbG8U7elvguCP03rpDsNNFprIyCW0GDbsfHMyU_11X6sUUGeQItaN8t9b5whgnCxsygGXgg3cSMHiofdI9yzImVkNvUta1EHifbnI7v5kXmirSkvuEKcCBpKCjxT16yCYDCFXCL8ygKxseNGGUPB7cXnxJh29zwz-J2Y3cDJGzKRNQ8zKPdAMtDDG6dm12DRziXTEAtmYSJ88IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان : رسول خدا و اصحابش
لت و پار شدن. :)</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/farahmand_alipour/5539" target="_blank">📅 11:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5538">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
حملات موشکی حزب الله به شمال اسرائیل</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/5538" target="_blank">📅 00:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5537">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=kZsgSlx3Yvb5i9N3uoXmLqTEtG00NBAf0zrKcafg0j9miPNLGw-Tsofgb43C3FL77EVWNG0nHlPoR5bc10Uaf2vIEqtzJ2g0m6lN0wxjRzb6C8xLnr2pZn8nGu87dD1sMzVaE2GsxK0oIum0My5LPtUGzUH3kDL1nadFcoY7xh3iwhy5_VDhRCID0tYL1rJkczAKu74rux_pPw88AnoSU6u3N4jrNbLxwaPxth2NtxD8jU5H1QM9qEXWZsblThQ0xmJKiRZYCQpmXwDbGimur0rFtzjImuJXbb2Uqh0t2AgTmhsJ0k3IaCJhHI4Aa-ZwuRqrpVcFxlOJU47R2bd5EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=kZsgSlx3Yvb5i9N3uoXmLqTEtG00NBAf0zrKcafg0j9miPNLGw-Tsofgb43C3FL77EVWNG0nHlPoR5bc10Uaf2vIEqtzJ2g0m6lN0wxjRzb6C8xLnr2pZn8nGu87dD1sMzVaE2GsxK0oIum0My5LPtUGzUH3kDL1nadFcoY7xh3iwhy5_VDhRCID0tYL1rJkczAKu74rux_pPw88AnoSU6u3N4jrNbLxwaPxth2NtxD8jU5H1QM9qEXWZsblThQ0xmJKiRZYCQpmXwDbGimur0rFtzjImuJXbb2Uqh0t2AgTmhsJ0k3IaCJhHI4Aa-ZwuRqrpVcFxlOJU47R2bd5EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زنان کفن‌پوش ولایی در برابر وزارت خارجه و سر دادن شعار : مرگ بر عراقچی بی‌شرف نفوذی</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/5537" target="_blank">📅 22:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5536">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8679568b89.mp4?token=ZwFRjoy1rVVW0FA21QNkB8xSjLbx5fNHoYLSnszpJnwKAy-B_GTyBCaV_NEiaeVomOr-iYYtbGVffM9v2dJxGorwiqP32wQ6JHhEOwXSemHXdl_u_uFsegESaDSmODs5YSNpKUT1EY78GsNzR7xmJlm4vH9yVzhqXjLZhr8pfIlo6AIQvsW3h6kfuCz71Hj1PXequ7_-e7o6oVa-F1E3b9ZO9nuHFTIpuAVBRS-ZgjytkL29cypNG148YpHko6VeA1VpZDTrTxI2w4VlnRLxw6BYXMRgfzo7wGji6528Mv7BX_1YZHbRJYPb93_Yf2f80uqDvpQYuNr1CXLGfBe7Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8679568b89.mp4?token=ZwFRjoy1rVVW0FA21QNkB8xSjLbx5fNHoYLSnszpJnwKAy-B_GTyBCaV_NEiaeVomOr-iYYtbGVffM9v2dJxGorwiqP32wQ6JHhEOwXSemHXdl_u_uFsegESaDSmODs5YSNpKUT1EY78GsNzR7xmJlm4vH9yVzhqXjLZhr8pfIlo6AIQvsW3h6kfuCz71Hj1PXequ7_-e7o6oVa-F1E3b9ZO9nuHFTIpuAVBRS-ZgjytkL29cypNG148YpHko6VeA1VpZDTrTxI2w4VlnRLxw6BYXMRgfzo7wGji6528Mv7BX_1YZHbRJYPb93_Yf2f80uqDvpQYuNr1CXLGfBe7Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی که گفته بود
به خاطر هسته‌ای
دو بار با ایران وارد جنگ شدند
،
الان با ژست پیروزمندانه! میگه قراره
در داخل خاک ایران، اورانیوم غنی‌سازی شده رو رقیق کنیم!
یک ملت فقیر شد تا اورانیوم اینها غنی بشه، دو تا جنگ راه انداختن،
حالا میگن «در داخل ایران» میخوایم رقیق کنیم! ژست پیروزی هم میگیرن!</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/5536" target="_blank">📅 22:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5535">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=nIFixbns_M0IWHXBtwGMZpyqksX3-MpsvzHqBraBYTh3LNoJQb6RdHwhXarmDDKKasWSrWTj4cyTtr0VOFo6JXgSoYEDrUMsCOqPiMNfT1NdaLx5P3g4E4v2jcShfTHvhU1VGUh7xf5y9jIQULXr4r01OZ7LC6NBrPE_nzIO2L3Mcf5LDQrAGqQvtJc0Q9Z_G3NNoy7ucNm2AyurgW2qEuMiZKfMaP0iQJx6ketEYaZRDKJ9jDNgGY1Wej6uCS1o-Jr3Fy14pmH2m069lAN016NlXrKh1Zj0W66H0mBvS1vIAcdTfGBXiL5jKwytWbnYBdZ_BAekFcGBFwgxJWmBxZk0YUURygBMPwwAo8zqfuL3zppk6GMh02vtDqi2J_SQBGLE9vH9bK0MGle6UT9evVd_dkskLu2Z72Fg9kP-QfaeMpRx_U867GWZ4oPp-PBfxrM6_kNBJXC1hWORjwuCZxQtYp252gGdRglJIBg4NDOMkcBlxKUEes7sfxTxXOBj195aghac10_g0O7TFXPGATJKfsAcY3BlWclTvGA-JcvgE9Yfg0Ei5eAxMTpYYanAfKHPROj0YDHEJY6r6mgbd2C47nMiFOl2XJn7H8Jwx8x-ONUbzzXlJ6_2YtYJNPRYFn70ArbV7iGR7Z-AWy5s6sJHVaNufUC8Q6FHIQpbp7E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=nIFixbns_M0IWHXBtwGMZpyqksX3-MpsvzHqBraBYTh3LNoJQb6RdHwhXarmDDKKasWSrWTj4cyTtr0VOFo6JXgSoYEDrUMsCOqPiMNfT1NdaLx5P3g4E4v2jcShfTHvhU1VGUh7xf5y9jIQULXr4r01OZ7LC6NBrPE_nzIO2L3Mcf5LDQrAGqQvtJc0Q9Z_G3NNoy7ucNm2AyurgW2qEuMiZKfMaP0iQJx6ketEYaZRDKJ9jDNgGY1Wej6uCS1o-Jr3Fy14pmH2m069lAN016NlXrKh1Zj0W66H0mBvS1vIAcdTfGBXiL5jKwytWbnYBdZ_BAekFcGBFwgxJWmBxZk0YUURygBMPwwAo8zqfuL3zppk6GMh02vtDqi2J_SQBGLE9vH9bK0MGle6UT9evVd_dkskLu2Z72Fg9kP-QfaeMpRx_U867GWZ4oPp-PBfxrM6_kNBJXC1hWORjwuCZxQtYp252gGdRglJIBg4NDOMkcBlxKUEes7sfxTxXOBj195aghac10_g0O7TFXPGATJKfsAcY3BlWclTvGA-JcvgE9Yfg0Ei5eAxMTpYYanAfKHPROj0YDHEJY6r6mgbd2C47nMiFOl2XJn7H8Jwx8x-ONUbzzXlJ6_2YtYJNPRYFn70ArbV7iGR7Z-AWy5s6sJHVaNufUC8Q6FHIQpbp7E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توضیحات نبویان در خصوص وضعیت تنگه هرمز در تفاهم‌نامه
- به محض امضای تفاهم نامه، تنگه باید فورا باز شود، بدون حاکمیت ج‌ا، گرفتن دوباره تنگه و اعمال حاکمیت بر آن تقریبا غیرممکن می‌شود.
- هر بار که متن تفاهم عوض شد ج‌ا عقب‌نشینی کرد</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5535" target="_blank">📅 21:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5534">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhOdCxPpBnf8Xgt9DW862uoAJZecM56J0o4Th1Hd1H_ywHtU5Q8PKR2EU-d00knLdXOA-BcH1_FkIs64YcFtcuVXxe3iWxw_tclwTQWC0NIAzXvX11z-NfFGo26Si1HvsSp9oZVWMc9EDLjUa1r5M3qKH_ejZMoj85Q5U2C1uRu3IuP3BN7mskbHTL8epHzVddcBwQCN9tk_aQlYgKGRq47bK3NSymHl1SXXRqkiFu-F0t8rN3dvuH0_a9PmvsXeX0aCmrhMsYqS68X08JezIwcoTzNBrNGPeeQIZZpkIp3ldSsPkDoInp6-hy0Q7DN03Tgw86q8UrbJSs2hcZ8Chw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: اصرار ترامپ
بر امضای تفاهم‌نامه در حالی است که مقامات ج‌ا  صراحتا گفتن  تفاهم نامه هنوز نهایی نشده</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5534" target="_blank">📅 21:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5533">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=f2xlDhkLLXCq5ly55uAIS1luSLKb2ItnqnoqFK3spsDfdD2Y0wrDneZjkOkzk63T-BQIR3IdO0RO5Bi29tix60qnT2MWi05Q-o6N-Z2dQ4pMzQl545AmsSPJ1vtaVt0ysvKF7oi0Mff374VG_DJyaMBhygDkNmKEHfZwiWh9YO5xQ9gSkRSvvxBQLehvwyVNZGuv5US8HCUbUBR9G5x9jkxkRbIhcfzwp7ccwlIWidHoO1jEMyv2Yf06mi0YpcqlKJztAk3HWmosJ8CuGKQ_p3J74ld79edEcecg--NvKW8SE-FGazG_VmaO0whWUXZd-2LKfv8MGAGZMc40PGWn_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=f2xlDhkLLXCq5ly55uAIS1luSLKb2ItnqnoqFK3spsDfdD2Y0wrDneZjkOkzk63T-BQIR3IdO0RO5Bi29tix60qnT2MWi05Q-o6N-Z2dQ4pMzQl545AmsSPJ1vtaVt0ysvKF7oi0Mff374VG_DJyaMBhygDkNmKEHfZwiWh9YO5xQ9gSkRSvvxBQLehvwyVNZGuv5US8HCUbUBR9G5x9jkxkRbIhcfzwp7ccwlIWidHoO1jEMyv2Yf06mi0YpcqlKJztAk3HWmosJ8CuGKQ_p3J74ld79edEcecg--NvKW8SE-FGazG_VmaO0whWUXZd-2LKfv8MGAGZMc40PGWn_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۹ ماه پیش
بعد از جنگ ۱۲ روزه و قبل از جنگ ۴۰ روزه
این تهدید پذیری اگه به وجود آمد پایان نخواهد داشت.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5533" target="_blank">📅 20:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5532">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyqEVEnsV9AhCOrl_CGFyFQIc6zUVqLFCpu1VPTXifQeKT7Zt_wc9XXmoOBqiRv555KWZqjcxVZgCBII2X0gzqmXjbuVIRSl0-ITsUbkchnRN8sLWykVUNgC3KgT1gd0g4H20gChF7yRY-UWv7CL_QyWeo9yHNwIknSSrxA5Ku3h-Cfi2Ad53wRMD4uaNx_Ic82TwONB7xTF7tPsagogaT90iNlhmcgQtWVcnGmw7p8UKHXOUT85RfH0qSs-KAYKsf0MaPGtVxhlPZOlcVe2jSg5MQQObI2H2_UB-44faIOhvGF3AvBEgT-ipl7I0H2ReyS0cc1UDRcBYi4be8O4Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ اکنون:
توافق فردا امضا میشه،
هیچ پولی بهشون نمیدیم.
دیگه به سمت سلاح هسته‌ای نخواهند رفت.
تنگه بلافاصله باز میشه.
بعدا هم اورانیوم غنی‌سازی شده رو از زیر آوار
و خاک بیرون میکشیم و نابودشون میکنیم</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5532" target="_blank">📅 20:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5531">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7xVS0f455IWyJ6Nfm_GZZDhb29BqeNIA5WCr7-rMazEvNDpy1Qy7vBORERO2vVxI1wbsF6upc03TrZLRg2qWA175kJ1AtHvvyyj8v0-Ju6mJTwOnHKW9F8MIlM1F8j-UWqnq_-9ux9T6FcWQR410sdBKPX0evIrWJvPBgDM8F_pQ6dd2V7aGemqEqUTq0ZZdRxn-qVS6cKyDsvDMMpbk1ZnWFFCUW2Y4B2Ggtad0KFX42wqF6reggDAUntV7dPPKtJR4YCZR7dUGv5hhA8p4L_Vr4afDNWgKWRmzAikBo4G9GciIX6DNYrWsUbdsTAMwuQNAQbLuCQsqe3Z0Ofz-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیسی خطاب به قالیباف نوشته.
نگذارید خط تسلیم و سازش با
قاتلان خامنه‌ای به ثمر برسد.
(نه سازش نه تسلیم - نبرد با آمریکا!)</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5531" target="_blank">📅 20:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5530">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WOm0D3sN_tcXX30emK5uw40G23KjRpFd7d5XBkhtFwLNy_rPLnpB5B4lu_MXJw24kc0swRT60hY10MyL4O0PHgX2EJnLC1b4PbwSi088CKJa38NpEzODL-Dd55raOKgHvNuwYL4gFp6QRg6XzqJ2bYcD0-ZTyTSWTDDUR8Ix3rmXAxXnG5V9INBNgSlliRJupBIYXvJ1b84JpmI3fCBmIvssE6wp1u13xqNNHCIL3szKBIqxz-gc1-cEwOwPQ_B5r9IDQBm9pYZUYU9C99DkYplDz8ZN1tVIOK7XEw2B2bY8TZ7ZgY68s3_GwTM88Ew--__Da1mrO9fUn2AlKdYfLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوسف رجی  وزیر امور خارجه لبنان:
«حزب‌الله یک نهاد نظامی غیرقانونی
و بازوی مسلح جمهوری اسلامی
برای بی‌ثباتی منطقه است. اقدامات حزب‌الله، لبنان را وارد جنگ‌هایی کرده
که هیچ ربطی به لبنان ندارد.
ما فقط میخواهیم در یک کشور عادی زندگی کنیم! نه اینکه همیشه در جنگ باشیم.
مردم ایران گروگان نظامی
تمامیت‌خواه هستند.»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5530" target="_blank">📅 19:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5529">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نخست وزیر پاکستان: تفاهم‌نامه ظرف ۲۴ ساعت آینده امضا می‌شود.
عراقچی : برای ۲۴ ساعت آینده هیچ برنامه خاصی وجود نداره.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5529" target="_blank">📅 17:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5528">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=PLqy7AiZvDY5gL0iydQ27yg8tRzHi4z5crsFFLl12jv2dOyGhW67sZxW6XC7RQpBHYBnR9ZRwHJ9cKHDaHamtGsG0iR9XcO6LBk4LNLpIoosmKswWp5sqemTgqaqgRND2XjWmohu6UhmYNNp1oIn8EkflUp10D36FapgB89iu379-hAO8W9X5VHaCz8imea-rQeR3-k2N95D7tI2xfJ9ggfSkq-rOqZ4WsCPDni-6W5yZga37MJxt1zucfhU8uKgp5KPFn7VSci19X_7Be-A8UaiRdVU_Xdbb8AFLAWmbFHYSgT0jctRnzBtNU8DZARF59N20BVAksKfi6ArRpDpyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=PLqy7AiZvDY5gL0iydQ27yg8tRzHi4z5crsFFLl12jv2dOyGhW67sZxW6XC7RQpBHYBnR9ZRwHJ9cKHDaHamtGsG0iR9XcO6LBk4LNLpIoosmKswWp5sqemTgqaqgRND2XjWmohu6UhmYNNp1oIn8EkflUp10D36FapgB89iu379-hAO8W9X5VHaCz8imea-rQeR3-k2N95D7tI2xfJ9ggfSkq-rOqZ4WsCPDni-6W5yZga37MJxt1zucfhU8uKgp5KPFn7VSci19X_7Be-A8UaiRdVU_Xdbb8AFLAWmbFHYSgT0jctRnzBtNU8DZARF59N20BVAksKfi6ArRpDpyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان مناطق اطراف نبطیه رو تخلیه کرد تا در مسیر ارتش اسرائیل نباشه.
این جنگ بین لبنان و اسرائیل نیست.
جنگ میان گروه تروریستی حزب الله لبنانه
که با پول و سلاح جمهوری اسلامی و به خاطر خامنه‌ای، جنگی رو راه انداخت.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5528" target="_blank">📅 15:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5527">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LEpuY5icBQXxX8PuJyzKkYNZ4pUVvNv_8J9qY4yAPpD236W1_-9mQLiLFjY4FwIxJ6tocDI58fqK5zlg87F2C3mfMachkJ6Wa8iVuVQphCv41A-17iu13aA__J97d5FENKLHMUAluLItV8zLYpBqt7O2AJuS9WdZcvPyNR7DrmpIQX7dUsgu3ZjvPOfMtwLmszAiqpstwUatjP-6N90EhHnOF4iuq4X-k2hvVo4vLwNA1X-bsRqIdnXUB_mKQm_k9oVm2nmX7IPgWfA4bHKOvVlGru6xUMu8dfu1a_fNOiUQtev1t40GCGillBOFKpIC6l0DUBbVYRYcDOo0jcsmzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی در باز بشه می‌فهمید
مجتبی خامنه‌ای در واقع همون قالیبافه!
چیزی به اسم مجتبی وجود نداره!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5527" target="_blank">📅 15:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5526">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFSnuzB7Y6F0flUnITyO8p-H8m1p-Z4aLQYNfwNEnF7x55DRAk18s0O5lQCOrhFtV1QQBXqYhFpVYAWqYXhz2FnGgXSzqQB8dINHdA659iovBZTuJY4T2CbMcbj40bNd5XsEDjJyOVNP27GffM3g6qNsxYLVqAvrBurIzPk5u9rIuRFw3VGHFodfiurCBr4jIknR01f_J3Xj9eoSOWV1TWwz82DiNIwcjOaasHkQFb39GgbVGAwwVhGlAGGlw-MxpTAuBMzYDfF1BWU_f1UM2R1N3pNvNDg_-SN0V4_75ttGYPiGn3vYlbLwHI1JfChSJq6QIGIFvxlRDBcBF_pu_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : ارتش اسرائیل دقایقی پیش
به حومه شهر نبطیه، یکی از بزرگ‌ترین شهرهای جنوب لبنان رسید.
اکثر جمعیت ۹۰ هزار نفری نبطیه،
از چند هفته پیش شهر را ترک کرده بودند.
بعد از حملات موشکی ج‌ا به اسرائیل،
اسرائیل فشار بیشتری بر روی شهرهای بزرگ جنوب چون صور و نبطیه و….. وارد کرد.
ارتش اسرائیل فردای حمله جمهوری اسلامی
دستور تخلیه شهر صور  - بزرگ‌ترین شهر جنوب  لبنان - را صادر کرد.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5526" target="_blank">📅 15:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5525">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUFJ-uPXSMTOg3iWswS4UZSU7tqplUxF0vxb-nuqp-3WEx6R0GAdz-iWg6Zik3_pMje77NpCxSLr57ha1t1DlL5S_EYpqMboq7Jyp4pr2YsCn49Z05Xc34k6pVXeJJ2bIrBXXqD5UEybF9GBaM_sUNoxYEkgusEzgInC23ZjCEtK-hLHdHimtVv5FSrjr1ibM1pAJEsAFo9EsNu_3XCtoyaCMiLQyykmbPpbbPLaaO10tmMwniKtG2A6nv61HGggMmsvQ-MSKqDZdjZWU4CGjsbm156hIZ0rz1efau6a8CONWijWiOG3ajhbQUTQYBDhqkCcAU14_QuJderJgBi3VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات مراسم تدفین خامنه‌ای</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5525" target="_blank">📅 13:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5523">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KL27zaThmI4O2ewdFsHw0UMwQeB_K6usxNl-fmS7lO4rUVdApy2JdPMJKGPu2H5thnoYlBC_h3_bZXo2dObnw4ZvgK5JRo87Uc63EdR_4hw3uGEX3pD0mOz_H02OwERfP5dQEQ-ufPteubo2e2QGFWWuFCUy1KzLSbeybrl65gXCjMXI2ACch4GMX3Kb5n8ekbNQh0DclkPCEE7D9Lu-0N5TrAK3nNBVZvpH94J5FE3fPleMqoXuIqrDFTnZpnhRihRWO0krVpAlRip8OyGW_eF8_asNt-fGNnF6rHJ1n3c3n_S1feO2vKIMHwh5cLZgQ8F7fBQKDSYYHn0H0pVAeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=QDpLHbJri-w2WLJNTs1PtRSVDMze5xxkb5MJ13X5I0cZqYXxLheg5W_EkluXw2_rdnzZG0MBEWFwn7M-iRVVRVFTG__zXJTAZ1ay-GD_xd4tnsUIdowFSlYGHpJLPu1p7WU-exNkIWlL7UnYlWuPq42kKgVNZZtvKbyXvfGpJWXe_Joe14NgL3MEvklhOpyGGuSNJXDYzPk11EDAnwmcCPWDydA-ULui56xH0EBHEA_gaBHElxiLR4BrsHRagImuhclmIB8hl9WZoM06zVZfKdZvbWdfGvXaOQ-rU-igPE9eccy4v6PCLd7nPivaDWMJDt2QfWz0Q_ttg6MGmpragw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=QDpLHbJri-w2WLJNTs1PtRSVDMze5xxkb5MJ13X5I0cZqYXxLheg5W_EkluXw2_rdnzZG0MBEWFwn7M-iRVVRVFTG__zXJTAZ1ay-GD_xd4tnsUIdowFSlYGHpJLPu1p7WU-exNkIWlL7UnYlWuPq42kKgVNZZtvKbyXvfGpJWXe_Joe14NgL3MEvklhOpyGGuSNJXDYzPk11EDAnwmcCPWDydA-ULui56xH0EBHEA_gaBHElxiLR4BrsHRagImuhclmIB8hl9WZoM06zVZfKdZvbWdfGvXaOQ-rU-igPE9eccy4v6PCLd7nPivaDWMJDt2QfWz0Q_ttg6MGmpragw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5523" target="_blank">📅 13:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5522">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5522" target="_blank">📅 11:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5521">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4jduvqCMR1Hm1rn305-CMitIuGk0oalQHTg4Jn_zfOnKM2m87zXGmkkrJ8slrclomN4xDPd_kjsuI7oD4XNr2gwfMWg02AfPruWdgPYeoR2lhqLEFVFL7GtFKRH6PhKljpGRY8plge57tZWUUhV1uHb8Z65ozgdtWvkt7hJKH7r8dWgGr_9Qb-xkRCtQbPjN1twaDben91HmP6ZUPB1x97Nm-xLUzBz53d4Z1JBE59NoBW-I3x3C8Wnm2_bLSNwWkt6OXoWSpPgoA4GdSQr4rqMeizX5TqDaUfnQdyGaLxcOOcyytWFdcDQSAZqgG2-8zjd6YMqvS2c1MXQSKjEsg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5521" target="_blank">📅 09:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5520">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opTK8JoEzdPDBNJOS6VsIDuARSWMO87kXTgsf1J9TZjocEgIp5JA6SMmpQPPFKDsAGdW3MdhdM4qKLYaNDX9zKt9h1S62EzFw9wtDhFzGg2dk6AwbjR3pGEKmQyn25xlzwgCOP0szfFRtOVHNAeJ3RUxuCZpAG4OftNrOy6omDnS8HGsWEByPkR0paxvLCd8F-eevDz8gbzPVi3IHTjWCSL-6hJpc8h8hTi_9wOAAcT74tlxT5T7Ns8d3DhsTWA-OZoq-Qjun2nLU-cjIrkDqGhvwO4JKCebtE_5I9YSZDDIzaqaY8vR-S47t4Am9rhO41sPiPmSxBF5-WYOzjD8zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5520" target="_blank">📅 01:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5519">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=qp5Kct6FGVrLN3bQvfXIovzYjF1oUJH3h1P8QUlEqOnOYSuJEqZM8o87xGrYqwT95cnpXXsmA7JQMPdvrfBoqgDNiFyRopA68C8xhcBn0Uu2BCf0SkO3QfW2iLHQwtsmpP9EDJcwEkTm5eiM64QG5_crUN45viYjECSHorrHg15WA-tp7osfbZVDvOczEQWOfM9x2jjIN8HSCfrLuGbz-hmMsLFwmm8egQQE0emsVLrHTEC4uZ1ZXu-EK7n--zx41iJFgij4gLLimUVi4zaVEqI1LPcr-oHfTShbzdKkgWNw7mgGBLCY_5LfrLvKYo6gVoki4dtG9LTViJnzPYWRkBO3RjRNSVhUfYr48_qJ8PMLSPJvwfzK7BE7iNtfegqNjLBIyFbl0zxXOzYK5m_PsuW3YDJOIP4KR0a7jH5oUtTy8cLBdimAmpLfyEhc49fD0b4B4yXjnS1a6Ah5l9vETINHZVWEVK-BXLTtZ293tpp6Z1ViEmDdzR5l8iZhs6dSMN92IJ0kV8eWbYlZCRjxyYZwUrpmLr8txomTw9V35HJ5f83AMrXiOifNXlZut9DX3r-IL_q-KQ22RKTK1biKuyr1f1EJVn6CnBArhZLn1k7zmf_xXsbognFeP36q38lvjDAUF2Hb6uqPmLEeoMciAnCqhD2HtyT1fosRQ6hh4So" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=qp5Kct6FGVrLN3bQvfXIovzYjF1oUJH3h1P8QUlEqOnOYSuJEqZM8o87xGrYqwT95cnpXXsmA7JQMPdvrfBoqgDNiFyRopA68C8xhcBn0Uu2BCf0SkO3QfW2iLHQwtsmpP9EDJcwEkTm5eiM64QG5_crUN45viYjECSHorrHg15WA-tp7osfbZVDvOczEQWOfM9x2jjIN8HSCfrLuGbz-hmMsLFwmm8egQQE0emsVLrHTEC4uZ1ZXu-EK7n--zx41iJFgij4gLLimUVi4zaVEqI1LPcr-oHfTShbzdKkgWNw7mgGBLCY_5LfrLvKYo6gVoki4dtG9LTViJnzPYWRkBO3RjRNSVhUfYr48_qJ8PMLSPJvwfzK7BE7iNtfegqNjLBIyFbl0zxXOzYK5m_PsuW3YDJOIP4KR0a7jH5oUtTy8cLBdimAmpLfyEhc49fD0b4B4yXjnS1a6Ah5l9vETINHZVWEVK-BXLTtZ293tpp6Z1ViEmDdzR5l8iZhs6dSMN92IJ0kV8eWbYlZCRjxyYZwUrpmLr8txomTw9V35HJ5f83AMrXiOifNXlZut9DX3r-IL_q-KQ22RKTK1biKuyr1f1EJVn6CnBArhZLn1k7zmf_xXsbognFeP36q38lvjDAUF2Hb6uqPmLEeoMciAnCqhD2HtyT1fosRQ6hh4So" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5519" target="_blank">📅 00:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=W9e6fR0yBB0n944blMco1Xrq8zWBh22Yp4jXROo2jI1mfUNZ3mS66MkV_BAhy-ceez7AgX1043yBtBcZtEo8ZQ9Zq4L0ey33gObmYDfK_I6qnpn61ePwkO9wm4qS6J9kPLzzhd541qd4zAtFLQon3uLs3ZyTMarW2rQFXHI9FA1itAPvOye9IHyFBA44uKv7Pzo9ke5VSrQ1YwF58Se_RXTF1QfX4r7CXt6239tvyt9uuageuMBrt_30ypL5TnbCJGddC73JhRzSdjdIc9JC2qmnyjvD4rpm90yemPQPQuqbWfoF_7nhOh1oE9a2iZCy9mCf2h_fQlpwgMQBZZMMLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=W9e6fR0yBB0n944blMco1Xrq8zWBh22Yp4jXROo2jI1mfUNZ3mS66MkV_BAhy-ceez7AgX1043yBtBcZtEo8ZQ9Zq4L0ey33gObmYDfK_I6qnpn61ePwkO9wm4qS6J9kPLzzhd541qd4zAtFLQon3uLs3ZyTMarW2rQFXHI9FA1itAPvOye9IHyFBA44uKv7Pzo9ke5VSrQ1YwF58Se_RXTF1QfX4r7CXt6239tvyt9uuageuMBrt_30ypL5TnbCJGddC73JhRzSdjdIc9JC2qmnyjvD4rpm90yemPQPQuqbWfoF_7nhOh1oE9a2iZCy9mCf2h_fQlpwgMQBZZMMLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت نبویان از متن توافق ج‌ا و آمریکا :
یک : طبق متن تنگه هرمز باید باز شود.
‏دو : تحریم‌ها برداشته نمی‌شود.
‏سه :در مسأله هسته‌ای مستعمره آمریکا می‌شویم.
چهار: آزاد سازی پول‌ها اعتبار ندارد.
‏پنج: هیچ ضمانتی آمریکا برای اجرای بندها نداده است.</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/5518" target="_blank">📅 19:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5517">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">وزیر دفاع اسرائیل: از جنوب لبنان خارج نخواهیم شد!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5517" target="_blank">📅 19:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5516">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5516" target="_blank">📅 19:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5515">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5515" target="_blank">📅 19:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5514">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
عراقچی : هرگز تا این اندازه به یک توافق نزدیک نشده بودیم.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5514" target="_blank">📅 18:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5513">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IIlPaX2BiAyDvMFrx61s_A6xQfyNzu43VAoFb_ERImT3-HXmby8oHi0LB2MW8vSyaH2pVM348JG0hqPQ6zkIIb3T_cf-EU9R6-n-9jZeJU9EMBYBNdMpTScVKxk8QewXydR3y40R3jnRyTAYoP2y0gcy8Jf6Hr76-ubnmKhVTAK4Fae10FWx0B2150E9Me2EL5UsGvYS6yyFW8HAqfxZIQG6KbwHwTQxncwc-UbVCe_EEfodJb3zlzWeZ0SGTkgr23zAknI38uAqYarBf0y41vv2S7JCKlkdtLblFVyO1EzQrmOJtj8pPb_DLiFfmT8m0j2Q3AFHPR3xkVAQSV0Aug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : این مواردی که جمهوری اسلامی منتشر کرده دروغه! اینها یه مشت آدم بی‌شرف هستند، اصلا نباید با اینها مذاکره‌ای بر پایه حسن نیت صورت بگیره.
حواسمون هست که دیشب هم با پهپاد
به یک کشتی هندی حمله کردند.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/5513" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=MRCOo-_N9s6TiDqEPQ2uRbXf7-m5MmvhRZY5_VkL9lqYKeZcJzE24oIwJ65-qJRCbkOTTB7nCpaC8Z5K0umhX6blpQophgLYIPk9ap1o3QV2dJ3vpfHSzT-19tBwK5AVeIbiLeNM10VTsxN18oBRsQfeV6CwGEkwkbm9y-Hk2kjzL8KcUd4y01gxpkQylcgLvcMN1FkLxxA_o9z-R2GV9bnLLX4s2WZ2aEyd4Me-AoIse4Xc7eV42KrQgPIkTWKKkiYNkL5Ee_fFJBrizklqWDScUxxqQDR-f55YG4Ujk6IiuSCpl8AGzE_wXJPinQv-6aa7S8L62x37Ny1fBweLRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=MRCOo-_N9s6TiDqEPQ2uRbXf7-m5MmvhRZY5_VkL9lqYKeZcJzE24oIwJ65-qJRCbkOTTB7nCpaC8Z5K0umhX6blpQophgLYIPk9ap1o3QV2dJ3vpfHSzT-19tBwK5AVeIbiLeNM10VTsxN18oBRsQfeV6CwGEkwkbm9y-Hk2kjzL8KcUd4y01gxpkQylcgLvcMN1FkLxxA_o9z-R2GV9bnLLX4s2WZ2aEyd4Me-AoIse4Xc7eV42KrQgPIkTWKKkiYNkL5Ee_fFJBrizklqWDScUxxqQDR-f55YG4Ujk6IiuSCpl8AGzE_wXJPinQv-6aa7S8L62x37Ny1fBweLRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امروز اسرائیل به صور
دیگه نمیخواید بهشون کمک کنید؟</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5512" target="_blank">📅 15:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5511">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
رسانه‌های حکومتی :
جمهوری اسلامی کنترل تنگه هرمز را رها نخواهد.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5511" target="_blank">📅 14:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5510">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ax0ysOJme6ZQDJJU-iCsbgNkYVkfS6tzWtrMVibDKexSta0TgOHykMrEEY9GQJbiOUbGNaTJFX19XsJQIBLEu5vJE0rJNF5-eFBkbOBi71p0e0hJb_CWxGpLTweShURLhv-IvWPSPQFKLQhMKksniEsZx7GkkUmpYuB9-a9L8LY063bz_V2wxyWtJNo-0jHkY5aEEtIr5aTAVI1azgOI3xEUfPtjRK2YRCc1GlRmwBp2IKmpl6TIEGJ_XWxzNBsZ6mUMX_O85XXSmMqD2Pn9KVyQk61yPPoQMK8P7kPP5QWd-xVNyMebUi7kup8qieMXtAYZMLIqjHzyCWyJ5mHptg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
قطر خود به تنهایی حدود ۱۰۰ جنگنده بسیار پیشرفته دارد. شامل ۳۶ فروند رافال، ۳۶ فروند اف ۱۵  و ۲۴ فروند تایفون.
🔺
بریتانیا برای حمایت از قطر ۸ فروند تایفون در این کشور مستقر کرده.  قطر همچنین میزبان بزرگ‌ترین پایگاه نظامی آمریکا در منطقه است ولی اجازه استفاده…</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/farahmand_alipour/5510" target="_blank">📅 12:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5509">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/5509" target="_blank">📅 09:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5508">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=B0bGPiVXjev-MDtfbAJqy5xssqPW-f-aPnvwge3ao84PrrUUzzsZvGRob0GXjdEkZZmWDp4cUjIcEjzO0vIslIH2ECIuGLHN5rFKx1-pqk7QTKccnThYvf8d5SZOZ6f4kaMRv7DdhAkXUJpA4s2ufpyUN1leI3adXNxQKAkKe0i86tZwLJ6UkhR6RafpHz9skS_KTM_nSn7c9ifCDeJj3ex9OaLiMAbVLDAQ0Mcs8ESSxd6AgJL3v33vY9g08KdMmd2mjD6QWAehAfACvvHvttU7oXBTamWUyx_zxMumLOpeqF1iigenTx8KCXGSnmA2_1qq38ANhRt30RoWiqBi_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=B0bGPiVXjev-MDtfbAJqy5xssqPW-f-aPnvwge3ao84PrrUUzzsZvGRob0GXjdEkZZmWDp4cUjIcEjzO0vIslIH2ECIuGLHN5rFKx1-pqk7QTKccnThYvf8d5SZOZ6f4kaMRv7DdhAkXUJpA4s2ufpyUN1leI3adXNxQKAkKe0i86tZwLJ6UkhR6RafpHz9skS_KTM_nSn7c9ifCDeJj3ex9OaLiMAbVLDAQ0Mcs8ESSxd6AgJL3v33vY9g08KdMmd2mjD6QWAehAfACvvHvttU7oXBTamWUyx_zxMumLOpeqF1iigenTx8KCXGSnmA2_1qq38ANhRt30RoWiqBi_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاور قالیباف:
دو نگاه وجود داره، نگاهی که میگه بریم صلح کنیم، بسازیم، یه جوری مشکلمون رو حل کنیم.
یه نگاه دیگه اینه که صلحی در کار نیست!
ما قراره با اینها بجنگیم و قراره اینها رو تسلیم کنیم در برابر اراده خودمون.</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/5508" target="_blank">📅 08:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5507">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=J9iMgbmbhGUPjpkYH5_Ugh-Y8wDvcu406W_H1JXGXceTlwEX1rgJd9O4HLUmv9SgQu9Svf47ktLzFt4CgVqkgdEPg-UrEaxMsZ9ShfSWdllhzuAZOJR-rsDdAU4RFK3AOjQEUU0uR-Jn5JQIz8YK3U4ySQStFYqdoiszdTLVjbuuCdcl46pqe1EM_mKVqC7d1cU8UETUKVg4A2Rc5ohDPIjjlEH0n_3jYRtXYNywUmMpBW1UJ4fcXeGiUrcmM32ddRR7iHBlYEBT6d_7IH8Fn-1hy4Kf_h7ftlwgFFUCDxrRUKUuzKyofMBV_fxN_PZX_hYe6wJXEqtFQbKX5k_8pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=J9iMgbmbhGUPjpkYH5_Ugh-Y8wDvcu406W_H1JXGXceTlwEX1rgJd9O4HLUmv9SgQu9Svf47ktLzFt4CgVqkgdEPg-UrEaxMsZ9ShfSWdllhzuAZOJR-rsDdAU4RFK3AOjQEUU0uR-Jn5JQIz8YK3U4ySQStFYqdoiszdTLVjbuuCdcl46pqe1EM_mKVqC7d1cU8UETUKVg4A2Rc5ohDPIjjlEH0n_3jYRtXYNywUmMpBW1UJ4fcXeGiUrcmM32ddRR7iHBlYEBT6d_7IH8Fn-1hy4Kf_h7ftlwgFFUCDxrRUKUuzKyofMBV_fxN_PZX_hYe6wJXEqtFQbKX5k_8pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی ظاهرا متقاعد شد که شرط و شروطهای ۱۰ گانه‌اش رو کنار بگذاره.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5507" target="_blank">📅 08:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5506">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">صدا و سیما : شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5506" target="_blank">📅 01:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5505">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
ترامپ : توافق با ایران باید همین چند روز دیگر امضا شود، با حضور ونس و در یک کشور اروپایی.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/5505" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5504">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
نیویورک تایمز:
مدتی کوتاه پیش از آنکه ترامپ حملات به ایران را لغو کند، با پاکستانی‌ها که با ایرانی‌ها میانجیگری می‌کردند، صحبت کرد.
به گفته یک مقام ارشد دولت آمریکا، پاکستانی‌ها به ترامپ گفتند که «ما با ایران به توافق رسیده‌ایم».</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/5504" target="_blank">📅 22:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5503">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک «منبع آگاه» نزدیک به تیم مذاکره‌کننده ایرانی گزارش داد که رژیم در ایران هیچ متنی از توافق را تأیید نکرده است.</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/5503" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5502">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
اکسیوس: ترامپ حمله را لغو کرد، چون قطر گفته بود که به یک توافق رسیده‌ایم و فقط مونده امضای مجتبی خامنه‌ای، اما حملات دو شب گذشته آمریکا،  هم ج‌ا و هم قطر را نسبت به نیت واقعی ترامپ [که جنگ میخواد یا توافق] دچار سوظن کرده بود.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/5502" target="_blank">📅 21:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5501">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
ترامپ : حمله برنامه ریزی شده امشب به جمهوری اسلامی را لغو کردم!
گفتگوهایی با رهبران جمهوری اسلامی داشتم.
محاصره دریایی اما همچنان برقرار است.</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/5501" target="_blank">📅 21:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5500">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
ترامپ : هر شب بهشون حمله می‌کنیم، تا اینکه به توافق برسیم.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/5500" target="_blank">📅 20:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5499">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">حمله‌شون هیچ کمکی به لبنان که نکرد هیچ!
هیچ ضربه ای به اسرائیل وارد که نکرد هیچ!
فقط یک پتروشیمی در ماهشهر از بین رفت و اسرائیل فرداش، برای اولین بار دستور تخلیه برای ساکنان یک شهر رو داد!  صور!
دیگه نمیخواید کمک کنید به لبنان؟</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5499" target="_blank">📅 19:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5498">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-27fZppBvYXI7opWYx5fu08HOyo8qi0OjXnTvAo84urDJy03uQYpxwr5E3qIwAu-_qvzH7jZdkyC904122WAjg6zJtRrScqlSrTv-aeE1gIyZufi8qpegG4r5Sf8mufAxnTj0hfuF2bJiF0bUa0OxkJmvHZiCKyoRSCq8fNdXbbH1wFj-T9G-E11_5JOfUrqG3LEw1q7rWKJT5fIG0TwmA1Q7aoJLmra82TDuby8e0GnZ-8ZzRUw_WO2g90E4Zl2IXymaaj1oU6WLkbPgFFflEsapry4pYcIMpQUOKIGlB15iodMBa553wb0whe8s6fg_4azdjkPYBGT6vQ8t6R0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=oyqtS4xNEB0OHnxd0DsVi5po2Jf7z8Ymmru0xKBurIo4ekuaIYDePkA25kMmBGmMLtREwjjMJFt5outnq2gxaUdnXQ34VLF1SQE3kiqc9OmZ6xT0yHpmI0YqsNqnsxhS_Bv9ArnPHHmz1EoC7NkU9Mp7aRu77ey_4P8K6OeUufODNJHdJ1_O4oGjz6H2ZWVjAuOSVZLRiqIIh3eqozUYVq8mvMPs2z5alhT1FExJ7-AEr-58amqPeczdPIN5_zXhrUgOsyKC8C7VI657hDJ2-qY7EssFPBSzWmSMDdzz3XwKY6fbnorT4b01madz7obXITYNFnMw7ku7vXOgjASscg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=oyqtS4xNEB0OHnxd0DsVi5po2Jf7z8Ymmru0xKBurIo4ekuaIYDePkA25kMmBGmMLtREwjjMJFt5outnq2gxaUdnXQ34VLF1SQE3kiqc9OmZ6xT0yHpmI0YqsNqnsxhS_Bv9ArnPHHmz1EoC7NkU9Mp7aRu77ey_4P8K6OeUufODNJHdJ1_O4oGjz6H2ZWVjAuOSVZLRiqIIh3eqozUYVq8mvMPs2z5alhT1FExJ7-AEr-58amqPeczdPIN5_zXhrUgOsyKC8C7VI657hDJ2-qY7EssFPBSzWmSMDdzz3XwKY6fbnorT4b01madz7obXITYNFnMw7ku7vXOgjASscg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی
باید بلند و علنی و روشن بگه
ما «تسلیم شدیم، ما تسلیم شدیم» و «
آمریکا بزرگ‌ترین قدرت جهانه الحمدالله
»
باید روشن بگن که رسانه‌های
فیک نیوز همه بفهمن.
😂</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5497" target="_blank">📅 17:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5496">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‏سی‌ان‌ان:
برنامه‌های نظامی آمریکا برای تلاش جهت تصرف جزیره خارک ماه‌هاست که تدوین شده، اما به دلیل این که این عملیات بسیار پرریسک تلقی می‌شد، پیوسته به تعویق افتاده است. این خبر را یک مقام ارشد پنتاگون و دو مقام دولتی به سی‌ان‌ان گفتند.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5496" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5495">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oT4bcTkpL0o7m_S2OvHxIQtTMIDZdByGCJv-OCF3Pql292CTtXENiUKfMYgzKTMLRvS_ZeRAE5aPhGMk56UCBaxOf0Nn5Eg0YURBvgyHPntyARV94UbzHlKptD6d-IEIq3cf7-jMuOQvSPCD-Em137x-JxMOkQe2xv-9G4OT_wA0Olfqj553HZJxoJNts3__xIlrAvW3ASEBcSx0IyQHC7ouPPF3UdMkhSJBRHwk2z3eKK1dkEKew7y13XOayiKSVyCVkkT5dpNj90Ef0F9dOxlamuhRN70ybEIXkeg-wNSorPpTSiS1Zhh3eUWvJipjYejPjDiwtKUXZJN56sykKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه داری آمریکا : خسارات وارده به متحدانمان را از حساب‌های جمهوری اسلامی جبران می‌کنیم.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5495" target="_blank">📅 17:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5494">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ دلخور از رسانه‌ها :)
‏ ترامپ در گفتگو با فاکس نیوز:
«‏ آنها دارند با ما مذاکره می‌کنند تا به توافق برسند. این کار برایشان سخت است چون آنها مغرور هستند. آنها بسیار مغرورند.
برجام جاده‌ای به سوی سلاح اتمی بود. راه من جاده‌ای به سوی بدون سلاح اتمی است. می‌گوید شما نمی‌توانید سلاح اتمی داشته باشید. بنابراین آنها یک روز با من بر سر این موضوع جنگیدند، و سپس با آن موافقت کردند: شما نمی‌توانید سلاح اتمی بسازید یا خریداری کنید. بنابراین ما همه چیز را به دست آوردیم، اما رسانه‌ها آنقدر دیوانه‌وار پوشش می‌دهند.
‏مهم نیست من چه کار کنم، رسانه‌ها خواهند گفت این یک پیروزی بزرگ برای ایران بوده است.»</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5494" target="_blank">📅 16:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5493">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tD3_pBjPbEFQfduxXQ2gOAPej6kpgAl9EZAIfAt42_y-s7Osfd-hTIkrpq_YF0vhp2HNVGGnmGPvLtCh-gK3JSve2o_fFmAltjRDc3tO4y5zVSW-3Epu7DiXHoD9CR4ugWVvlonwwIH3h8U-MSBPOjDXoDAedRsW1_vneAiyeGhdL3BpC2INsbj-YQAbA3p0siu9wQG3wXZ85kZrlR5cY44cQHm0IQeIgeoM4bSlIt8ha4E3NqMHmV1e1pxJCHha1Lca5l2iPXY7mF4UOv6K3Y4F5EdF5zdadXoIoyhWNOhoXyL1OysfD1wJWc9GKnM0-5WBk0EOMltihQeRJayyPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از انفجار در سیریک
مناطقی که در دو شب گذشته مورد حمله آمریکا بودند در واقع حاشیه تنگه هرمز هستند.
جایی که رادارها و سایت‌های موشکی و پهپادی و…برای کنترل تنگه ، متمرکز شده‌اند.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5493" target="_blank">📅 16:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhRffq0FtoepytUlBcEdLbcg18YlndVT7KwThB9kbV4QRHz_6K_ZKB3y_kDTjN5y6TxpMq4_JXb76RvJUCgI8-QdSQrLXBl_nWI05IS90efvMIILOEK2XxCxg9g4ykfnKZtVQXFLtMXca1Ys62wf638-MBfR4LhdknI56LYZOVz-rBiZiPUZ_xDrGeieNhhkF3Lq5aefyelW7JGh7ZUcMyeFrVYIlLFKbfamSzHsCoxmKEFHMObMn2eivdAihcjpHMd2yZJrGwucFWhbkNt7f2C1iTcr4xlmgehdT1tbc9P5iYfLXyGw2WP-SvveCaqJenyb4h3VAxfFmu3TyzPBJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اموال ملت ایران! که یا مصادره میشن
یا مفت فروشی میشن به چین
یا غارت و دزدیده میشن !
بقیه‌اش رو هم‌ میدن «مداحان»
و «رجز خوانان»!!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5492" target="_blank">📅 16:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-e2PswVNXncUSPK0Lfv56ii2yuvJXqxBHLALw8-sqU_hICyJurf8urwKVwWrZRGpLxaCVme3kc6jdHC_90gOjqJbV0YP6gsQ4YsMcfIMhLfwnp2wwOIi2UYIwSPvSsoHmBphTN7q28ArE5bey8agIULmpVRTbtWl-nu1f9R4hJz-7sbabqV08Aog0xD93_aKltlANpSp2kj2kHnIpHiGUeAh0HP3ospH3017U7qKcnpZa0HvrGAX6WQtLKrDsQ9YOO-TQjiWTUv7m1A2_xsu6w4GtQfgzQIoZWA9HKzr7m927K31csUTKjG0nksHLbbQdnmPpNYjgIwAcxSF1xvtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5491" target="_blank">📅 16:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KiSuZJUyRyUKqScKmpoir0Nj9RpKjM-_JSmqPlkg7FcSF5fey8ETHv8k8rOIY6AI95pBm6s0Mip1qcvJhHUEsRpnQ48B4Ug7NU7kdvQjxGNiwxgH5iLBlz5AFDWqBXWccra0bm1Vq7XeW49KsQOjOerybzdJV4Afw64jVC0V2jSHdatV2xXFZ_OR4dM5Y5zWfClecmpr1oW142bmwNX5ijFXC8Ufpd3hgA7EkiBkEH7Wl_aWgAvBb6sy1kkrRCBe3ssRUMdJ_tIWFWyTrMJchmsem6Yi_02DH27ow7WLvTG3wpV5v9tZhKcCSWWkTRTWgbx_rm-2GNo9C3EVP1Li_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5490" target="_blank">📅 16:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5489">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">بیانیه ارتش اردن : شب گذشته ۲۰ موشک شلیک شده از سوی جمهوری اسلامی را رهگیری و منهدم کردیم.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5489" target="_blank">📅 15:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5488">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بعد کار به جنگ ۱۲ روزه کشیده شد در ۲۳ خرداد ۱۴۰۴ ، که دو روز دیگه میشه سالگرد شروع این جنگ.  اسرائیل، آنگونه که نتانیاهو بعدها گفت،  انتظار داشت که در اولین موج‌های حمله چندین جنگنده‌اش توسط پدافندهای بومی و….. ج‌ا سرنگون بشه اما نشد! اسرائیل حدود ۱۰۰۰ سورتی…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5488" target="_blank">📅 10:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5487">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZQuFbBF86vcH72EkhWuwRqtf3EkeSj98rC-x1hx1g_tKCgg57Nixkqg-HlLvZCv411k02hWQ5yHZwM7brP_EbZt7eFL8QXj3bygNKvQ1s9_1BynIuMlJSbGARKcMptdqu11neNDXKMrUqWmUSwqowng2S3o6BEmA__GPtKYngqldyEG7Mxm1LAK1MSAxmq4oEB9Rw51rbwv0hxXPt8t5bFbWqftKE9wxmTHX-eFK9rdGGRPabudX7JoxCQtpG4eUNtp1QlnHGHFYo0Gd9zj705oClPGhF5Rh8fbn4-AU0BkRo2TNDAJBILeKug6EVr-AKEoiJZfuiGtjeW3c0RFJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پاسخ به حمله مستقیم جمهوری اسلامی  ۴ روز بعد اسرائیل حمله‌ای بسیار دقیق و هدفمند به ایران انجام داد.  گران‌بها‌ترین و مهم‌ترین سلاح دفاعی جمهوری اسلامی رو یعنی سامانه پدافند موشکی  اس ۳۰۰ رو که جمهوری اسلامی پس از حدود  ۲۰ سال تلاش و کشمکش از روسیه خریده…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5487" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/163555b294.mp4?token=O4O1EOc5sIBydDeH9G8dz7DrE2A96saFS2V3CZpGXP-SjZGa1vE_iBXhrFl7O8gQPbcAWVR_VF_i1MyyVzrTeVN8aehQAs3TN9mJGtHIefUAGpOTbXp_lP3D8mAQRFS030MjfUdE6xU12_ajlJV1tdNjq80ERoRzslxMGHb43xFwi2SHtdFJYQB1bbx63-sk5jr9SVi1zxPNE_kfhf6o3xn7QmRJK2Ctxd-iLHVa8LCASio2k1tgiNioCUCu3he-nE2ajt5wQm3VdsBjEu7L8jQztENCPt469ZCCk3-Xa3KRbkwj1SsSNzaO0X2O2svFWHiYobU5YBYjsdRnTliWhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/163555b294.mp4?token=O4O1EOc5sIBydDeH9G8dz7DrE2A96saFS2V3CZpGXP-SjZGa1vE_iBXhrFl7O8gQPbcAWVR_VF_i1MyyVzrTeVN8aehQAs3TN9mJGtHIefUAGpOTbXp_lP3D8mAQRFS030MjfUdE6xU12_ajlJV1tdNjq80ERoRzslxMGHb43xFwi2SHtdFJYQB1bbx63-sk5jr9SVi1zxPNE_kfhf6o3xn7QmRJK2Ctxd-iLHVa8LCASio2k1tgiNioCUCu3he-nE2ajt5wQm3VdsBjEu7L8jQztENCPt469ZCCk3-Xa3KRbkwj1SsSNzaO0X2O2svFWHiYobU5YBYjsdRnTliWhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی از ۲۵ فروردین ۱۴۰۳  رویارویی با اسرائیل را از جنگ نیابتی به یک جنگ مستقیم تبدیل کرد.  در عملیات «وعده صادق ۱» ج‌ا با ۱۷۰ پهپاد، ۱۲۰ موشک بالستیک  و ۳۰ موشک کروز به اسرائیل حمله کرد،  دستور حمله مستقیما از سوی علی خامنه‌ای صادر شد، و جالب اینکه…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5486" target="_blank">📅 10:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZb2zhwPRwXdTxc_iX3GU7D59O4Icp13vVDAwaKkR4szKZCmUH_2Nz2ASe5rFGB1wCjnHc3hkSBtbb1uGXyzSX7UQKoiTPE-B3ZePK3qsx9rHb2L-kWuK-m1tuh6lqlH3vxkUYXuH_4cre2c4jWKrYKpuB28BQeEKEh1LTdAN6qLmFsI7lCe3SACXNBt98hIWka6bPiummXFP1zQFfjkCvQhZm98Kg4iW22j5mdODjsER3Bo5znss98iC9NQNWsfzW4JAHkDwW4Q5n4bPWgSJbgCwL3lqNnWEJAWeXyGssKZjYkkeFuvGUGW-HHAz4N6vfqx85ugTfba2KTVOma_9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ غیر مستقیم با اسرائیل سیاست  جمال عبدالناصر بود.  ناصر فشار سنگینی روی اردن و بعد لبنان آورد تا اجازه دهند، گروه‌های مسلح فلسطینی از مرزهای اردن و لبنان به اسرائیل حمله کنند.  اما مصر خودش چنین اجازه‌ای رو به فلسطینی‌ها نداد! نگذاشت مرزهاش با اسرائیل دچار…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5485" target="_blank">📅 10:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5484">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHwRrOPb9ijdeP7RRH5zyFiakL3LjFpyPBji9YW0hJG97S7THgXE3UVfXcvUD-jKo5bN1NyloUVFV7DL-snQ2s6I0Dh6CPNR9EAlDBy6DM_bfuLPYKDNgm-44MytAmjM--Q6Q5D2b3FwWsXTl1LQyJeR1cBtBqGXhDGpI0OZju7nYZRr-7JB6wDi1Ak2SP21VErhMZZGWKogL2brVFsyDNZVP_DPsOSuhu-ee9aRYPGk97J_1-HBvkSVr1PhOCTZlzdcQH1oNF_T7FFrq4Vm7HqWUSayteA16ugiTDs9rtilLbXbIwjWwiufLWHcKMzoNYilnF8mpC3FiAGzZWRtGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی در ۲۵ فروردین ۱۴۰۳  برای اولین بار رویارویی با اسرائیل را از یک جنگ و نبرد ده‌ها ساله «نیابتی»  به یک جنگ مستقیم کشوند.  تا قبل از این تاریخ،  جمهوری اسلامی با مسلح کردن گروه‌های تروریستی مثل حماس، جنبش اسلامی، حزب‌الله، حوثی‌ها و….. با اسرائیل…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5484" target="_blank">📅 10:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVi8e-BK10Eh-9_sT5r8iXiq146kCbny5MENRnVi2bfI4j4mOYbIZQtPwBBxRxJabR_zVD7p48jmfbxj2ZeIIi6xf4HTCkJecWJe_0ITOI-22vpit9JnBWD3AOmbMmkwTC72rZBU6XUAU0W5I-mPSg9XiIvavTGAeGieKH5iTzKc5xAL4zr_d46dfrIQ5l8IPJGDzCPoNZDXxKKorKA7kmActqEI1QaGQgymZehPchLZ9ouWl66JJyEFgtC3CrkByQDgso-swj729RBsGwmHWGJr7KK9MIx60F-SQTKRW-JgRrX-CgMIzKzu95GjNzmoDdI6IDeHHRM8FUPwnzzQUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از مهم‌ترین پیش‌شرط‌های جمهوری اسلامی در دوره جنگ ۴۰ روزه این بود  که «جنگ باید کامل تموم بشه»  و آمریکا باید تعهد بده که دیگه به ایران حمله نکنه.  منظورش این بود که یک «آتش‌بس» نمیخوایم! «توقف کامل جنگ رو میخوایم»!  این‌ درخواست از اونجایی میاد  که جمهوری…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5483" target="_blank">📅 10:01 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
