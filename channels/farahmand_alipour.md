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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 08:52:21</div>
<hr>

<div class="tg-post" id="msg-5588">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.
چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ سخت نیروهای مسلح مقتدر جمهوری اسلامی ایران باشد!</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/5588" target="_blank">📅 22:32 · 26 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5587" target="_blank">📅 21:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5586">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgmlffjzE_qrw0K4fcb3LQ2iexas8EVdu0cykiuoK4Fy6L_MD8sZL-s_CTNJup1hheqtReGr-ZtUQdaH6BSDhOAqzSyHbLrkU-ifQRnNxZcf2M1FULmSmUS3Ai9YT9hEJObZx4gSJP10kRBTTRdSdYNz-cOHNOMaWYgFYuIJ-ma6lrEvxJsDEppERlOQSHXfux3C6cwwdgc1iMlHS_AxH0JhGsvoGGGPBDiOtsZ57LFJ4jHZG3JsrEwAF7S3_9fQfJFLZk2smlIaPORCNezHOhFJrg9Vc8vO14AyAlAnDHV2xLDVwmLEikTH2NsEpRbJU64XtwDF1Mt7fV8lFhsbkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده دقایقی پیش اسرائیل
به جنوب لبنان</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5586" target="_blank">📅 19:49 · 26 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5585" target="_blank">📅 17:03 · 26 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5584" target="_blank">📅 16:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5583">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامپ : تحریم‌ها لغو نخواهد شد!
بستگی به رفتارهای جمهوری اسلامی دارد
(اول صبر می‌کنیم ببینیم ج‌ا چی کار میکنه بعد در صورت نیاز، تحریمی رو برخواهیم داشت.)
ترامپ : صندوق ۳۰۰ میلیاردی سرمایه گذاری در ایران کار رسانه‌های فیک نیوز دمکراته پایه و اساس نداره! (البته این حرف رو خود ونس هم قبلا زده بود که الان ترامپ قاطعانه رد کرد.)</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5583" target="_blank">📅 10:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5582">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNTpIgWIVuzbRHoTGOwA9rElA9FQv7hvWUQVXbK-10dn9SS_0v71VrXTO4f60ZXKatjP2sXegayMEa5NlwI1GauZ_VBGdFQNS30uoKq15rcOKyYooV5tlldtESq0h3neVxCNLmqDq8PPJxQNsfEUqMh4yU2NI8-QRbzGfrrE2zmz6XpgUi2Qq65J0ZhDEj9pgmATvQA67utXwoYin10_W-cekLINiFMbsxYOXJf3b6hxWCOiCbVZjHprm0U7W7tumO5Gp1Cr3ImqtPnwYzjOjwepcmr6D1WXkFRSvZB6Jt52HjzmKUNHFqhLEntdnjKaeyXcgvJdIfB04R3bnQqIww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موساد و ارتش اسرائیل معمولا نتانیاهو را فردی معرفی می‌کنند  که بسیار پر سر و صداست، در حرف زدن جدی و قاطع است، اما در مرحله عمل، و تصمی‌گسری‌های بزرگ بسیار مردد است.  بنت اما متفاوت است او کمتر حرف می‌زند اما جسور و قاطع در امضای عملیات‌های پر ریسک و ضربه‌ها.…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5582" target="_blank">📅 10:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5581">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNmU520OyUOM_rUGL52o5V502SVZxiwXwbVtVswFYx07M6V9JLsPy9PvCLaQlq8p1Vuih4heDgmhog7ZgnjLJeAxR920bn28qdzJZa0XebH1IOYevKa3iNaBVXty7okhdxnoIzCtGr8NF6uJU8PE8_e9aYEOIjCEPXVJ6MGtsPo_VoMrXzKuKOfipkgKCraA9SGhkFGJ5GZowioxf7HLQT_sH1-N4uEn_U1X6AQ_oncogHZxY1IAxInA_8o5PsSoqObOfPK2ZgxXUFzDW6UIgw8JN23jQdVU1dixPYnqKvWZI44r7fXm1iNzjxfY4_IRZcwBnNSJ-aNsybIbbOIKBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">او که از منتقدین سرسخت نتانیاهو در زمان جنگ ۴۰ روزه بود و به او انتقاد می‌کرد  که ضرباتش به اندازه کافی قدرتمند نیست،  و اینکه نتانیاهو زیاد از حد تحت تاثیر ترامپ است، دیشب در یک سخنرانی نیز گفت که راهبرد نتانیاهو موجب شده است که درگیری‌ها طولانی شوند.  او…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5581" target="_blank">📅 10:18 · 26 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5580" target="_blank">📅 10:12 · 26 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5579" target="_blank">📅 10:06 · 26 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5578" target="_blank">📅 10:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5577">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPaPvDSmTle2Cn_G65P6D7joL9eWY8uSmXyTKApGiMx6iKdVabWUynDucceHk9hmkcpBOjAUrJH12OETK415QigsHOtoya0tFg0OvEXz6R9ARyJdzHkOAsBz7-9a5nvJhB1TwaoJ81oKTO34csYloluMiiYMhY-4TUyACRyUH8QyTr6VZmpORy3gPsD92DUQPf2j4tEaOb9BULarmsh2mJlTpeGrAOaABjvfQM4Yz_oupmJ9GvYohyCm068tMaGHUU2YQ-bkYXL73eJd84kmMxKaKfR8BFn0rjxlJ8sI29STuepOQB2ZB2gQtkIfo_CP3rjrdGdvyJlBLTbyio4Muw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اول هسته‌ای، بعد موشکی …
‏به مزدورهاشون که هر شب جمع میشدن، گفتن که چی امضا کردن؟</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5577" target="_blank">📅 09:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5575">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n7qhNLJwMGDM-12nsesYY_c-HiAUzQrGQRvKgp6BGsyrqXOc1bNoMu54tr8abDjZEMlMLljxBep9GtZMH3PH9F5BPSI2eMR61o-64qgC0_ihLybK4SlrpwCGlrMKvS0eDubwNmHGbiqry82M5lYBVl4PGNjA6Eml6MAHt2fbf1_6pQjyOrPVCqJT6woHGoQHURnzKuIF28FCJewzzwNeP0k-iAiB9O3elQcFY9KcQ0eGHtdocHCwswDkNlG8KIwhoGtGYHYuyz5wXi-F4UNAhSVpTWw4lwDScEbGIKtIeRPavWtvPBl3_D9hFjUFzbRDVyIvmSvcYnEYh47FjMBzFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dcXLR2WbeYqRCJYaZ2GzY2xvXLjXXSRf6xwNKCAw4-Bz0fVA9olh8xz9KmEK8ikcoUxG75voMhu3jqkCkCL2deXk-uOXWGBbGfNy1nEAlyucctGcgic7KT6apkoNi2DuiDgCtCTFxFBs80hzgHh4NhFEtyoRCMLK5tUFm1h6RNzwKR6yGq87EHWN60a0CxI0jN1qmQJmzixZ7XbCF7JI2axxIJ2w7eiLMEtDGzotkS8P4jD0FgLrY2i3bHEJhBFNVIGCCq434hDr18daE_P93-Xe2U7pjjAsOYJMpVSjufBVTFnlWeSfOoF8G_M6JDjJU1GE1-iS26z-Wk-SlK9zXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسین شنبه زاده فقط و فقط یک نقطه گذاشت!
نقطه او ۱۷ هزار لایک گرفت، دست خامنه‌ای ۷هزار لایک! رفتن گرفتنش و بیش از هزار روزه زندانیه!  چون فقط با یک نقطه دیکتاتور رو در هم کوبید!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5575" target="_blank">📅 09:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5574">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVG_ztyV0P_3m4VyfBtKxy6gMtx1td5H3osaROc8tPYdmMvyKjCp3O88Mis-yHX5TvvjjlCduuTSHBkXqaH3XCPDtX6g3UTk6Sg9s1IOFZ3uYdf9IkUCNL9Z34uOpoySZv6Ys-JoCocm-i59HO8B8lJ194fRnFPz_bG15fo5JmWeqtGX7KxKJjms26E1o6FxL3ebc_f0E5nAGfy2UxBjmm2pEPFFlXady8a_fUbTv459cwL17ukE4bmfbx_-RQRtmrUSsWdfqGSSJugIBj_rzlbsLiID1h2h9IBZ-cSt_7RrXKiYTwJJbKtnXx_BD1oJ-QmdsArMauCOUECjU-0Teg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنیده شدن صدای سه انفجار در قشم و تنگه هرمز</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5574" target="_blank">📅 01:14 · 26 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5573" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5571" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5569" target="_blank">📅 22:40 · 25 Khordad 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/he8YkKNbsTITWuZmnklEn0W9lteqhc2J61pQIG_2OQhKmYzemrXviUDnNnY1vNiCo_Q8g1fryoAJzRsK_4pSIKcR9yoeGVxzLQfYBAsH-sntyLIECqelvy95kfvz0-_65C8QBKMqDhAalJWluGfGTYzTrE87bXHJqyKA73zcFgqf03aemskeGbZGUL7AOntSbYLDVOW1t6qHaWZVGrKm1uKo_qYsNIUrBjUj_q_fiz490E9o7bH4aHRoOfcxnTYy6sddf4ncYTb1pA8l4mnNDape8GFEGZMLDqrn2lio7Baw3pIz4BPWgDIg5B1i27fbl3X8yhX7br6ExIEYgNErvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pe771ReYIdekS6CAaRmbOsu3NXflO0TABJht_uao_QKzXmH22j4G24dAepXGK3at3_uRgeYwDD1GWQQGfmtxfRv9bVeYn-c6We3yUbT88OYm_HvDM_3tPe2eA5L3iL9ne-YtZILI2tF02-OE-riq_UkT9Tbffv3cXe4dxFozLyU9sDeapqFcRXM8MNNIkpAG6VHBQnBfQGXkQWjUnnBBe3UjYNMkGL-yInWxAdEQLOvLygHfUyPZT4WgtYLy4rIookXR2IZZKNGzLo3cGBB0BjUZYD_uDQHsDyJOjh2ZNWsEyGhrO6pc-iz-FnJG6W7a0ER-4YzGJd_35up5VQ-EIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5566" target="_blank">📅 12:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5565">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bSvIqrU4BeFeZdm7cEzvcluFTzYZ_-hry4N1tcXVjeUIt5iCc1fmTidZaMK7d3e35OQ10MibvHXYh6ZvQOe_OoNco5oyrB8ibM08iBhZZak44wAxbMrS2z4lX0BFPjFiO-6BKLlLqXZp_URz5pHZQID0wg1RiadM2Yh-DeB2JnBMd1Cu5lQQVOdcUBOr78VskfIj_znYt1rjp3Kqoqg1i1O7say4lylh8Zmnw73zk0CFqXX8_9wlWfL082G3KUPhncMIxUI5EV4yNX8Xs6_2TENE7c7x41V8nMbHac3K-YnwrYjp9jJkK08peBEoa-22j2yGHMqAUfcMi98IcoSHRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم وضعیت لبنان</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5565" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5563" target="_blank">📅 10:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5562">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،  ۲ نکته رو به عنوان دستاورد مهم توافق پایان جنگ با آمریکا معرفی میکنه : ۱- پایان جنگ در لبنان ۲- پایان محاصره دریایی.  ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!  چون رسانه‌های غربی چنین موضوعی…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5562" target="_blank">📅 10:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5561">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQVR5AtacmNFXqTnhGJU6rOVVtqAYrIJ4wuCt5ppYB2nbkIqhONd0NPfFvDTmvBnkpAIDDiGdzwWv-6o8rfa_R5hVSjznKyLcbXJBa1hBKFn10XZ3CpBUXHoMYbUcSjqwoeVgfdMo7SdaBcmoWFPaO8WG3VA8ajbRkYdBJJ1WsUpMxm7z7W27QlGDunbgarbUNNafgXsUIln144etEfUuQrp3zTYe7BE86C_5vJRExt4HAwkq3RVlF7EJyuqiEKwH6wcYOg1cX-iwP5EMqvDSJ2P0er6ZRlGMeAUu5wLJs6QOQgl6GfQQ6o4gynA16IbyFPsWGvgTkA6qPJYgDpjgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،
۲ نکته رو به عنوان دستاورد مهم
توافق پایان جنگ با آمریکا معرفی میکنه :
۱- پایان جنگ در لبنان
۲- پایان محاصره دریایی.
ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!
چون رسانه‌های غربی چنین موضوعی رو
به این صراحت ننوشتن!!!</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5561" target="_blank">📅 10:26 · 25 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjaM2xhmeSNrVke722re0xD7Hq--mBlFsbLHV2kSqjVxxSDDi_p9nTezGsMLLDHnW2LTzrm34-_iRIIHUPxe7vjlxGvM83DSixLdLHWbuL1UUrbVvJZh3mQZ8vMwxRH_KAetGXU3EAuDrBlTb0dmqS5gfznNuCFGjesvnsqk5CAQLmAFHJXJK7dB7K3TyB5rx4Ksz8vJ80hngZQblmAzAkNTzBLFBfDeKd_dMmFSJ-Cr79k3Ztuey_hnXIg36aKaHYeY3cTQo9YGK9-kZQS40a_pmubihg3zsZZUbcaHUbIunlXNo-VeBHR-OPVy2ndlLInzbvx-ViR5Tb_z_YeOWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده تهران ؛ ترمز امضای عجولانه توافق کشیده شده. سعید جلیلی جایی نرفته.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/5559" target="_blank">📅 00:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5558">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
همزمان با تشدید تهدیدهای لفظی سران جمهوری اسلامی، اسرائیل بر شدت حملاتش به جنوب لبنان افزود و موجی تازه از حملات را شروع کرد.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5558" target="_blank">📅 23:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5557">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VU0c0jHTIoHhhbIKSO0J_0woKWq1NHo7fOgA_podrBgJIOFfW02Cuoe8UCvxksWf7Gbv3KS0yjmz_YTmgHmg35UEfsroDA5Q7B7U1wS-dR0O6YXg-ZlMYYxFCeuFyppRX-Qyh-RLalc6oAq_MfCFp2KSWklBjNVKmR28nPlJsED7tdV2ggHkxPaE75BtahfotHTOSd6d_aMvxzg3NX-IdWzj9d_thjsDGLdmyOkFp39cwnqE3F5IHa_cxZIPRN12DwESXl343uF7YRkRnRE2E7t6l6iT2Qu-5rbjWJlfQNu9iDk20yNRdWI2xswozAWasW2ZroH3qkHdF2WWPpKWGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ولایتی مشاور بین‌الملل علی خامنه‌ای</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5557" target="_blank">📅 23:45 · 24 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCs5PPHYfuu5Q-qmAbv0EBn3CDxdI6DGlocmCRU5o-yeMcuA75PmRuMG3KfBDBIoI5XeTs-nn2HCKi1inpXiJWD2-tklbT_Ns4nh-MILdhexg481C9sh_p_7jTIRkF1mZCSk68QUeXHlLM1oXNl0XViwAr1VG7g2Ptg8Y_jde44eM6rlEo2KT7JExxYSbD1W4w9zJzpLInVx9iQiJU0cfNaNSnW0TW6G1AQSBd5qE7xV2lW3jPZtDjxWP_2tJB45fytKyOtRh8fAFRq45zTksrdgYYv-uAWvzafHxL_Dj1Ex5Kg8SE8nBusWUFYKdZo-cRIEnOS97ld40gJ8gTTw6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای عالی امنیت ملی
«لبنان جان ماست»
پاسخ رزمندگان اسلام در پیش است.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5552" target="_blank">📅 21:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5550">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qRll8tr4N_bouNtYc2R6eG_y5sM8qTruAyTPrzmCnxlUeuXGsr2UAN6ovNl3qrSrkaqE2PwOHzr1TVq6bpFC_KYS_Zl9abfr08sl0Gt43JLGHsVh450hZBNQ6X1heyz_RYE4RrYsx3GXStn7jyAFJo43kUrbQ9QMILD-lCO26YNbZU6_40WMmd77o6RlD-T6mDSeyZmRoY-VnVHhYHqDIGOphihSk97ZsDMvj_PNvhn8yTuJmej5Eb-Zi25L5eZB377ngv1s_dX7JzkpRCOZibxWGLm0LcWAk6IAgED0D7S0JL5SqIhNzICV2tovD7KD3V0rpPlkRVVxlD_eaLiFSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTn1LqdL-yEmmiEv4Ln6PSxVaeaq6YHDKUba-mrIti48DHZYF6VxNEiALZRvEVx6zS6sMe3F-F_XGVR3_-GBLYfIYXOv-iNw-VMaDMbeoLsqdndsfA_k7tysQWQt8qp0QCDW1nFN0V7uLWsauCcf1WtGK53WbFFB6aQ1R6VOVv2hifI08k72zx2xXFkWWQj_m3xEPpQIlHq3DvUB4HiKVEBSTM2jRiHk4S7U0-4DdUEPH2swNyjmQeGuiyWfc9V-JGxEaK21RljYYWMpZh5ipNRi9klWLkQk9TbFfAJjqgCS6lkeqY0fnWin_5F3z6qUzc4z_YC6KdFvYoewzA79Tg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5546" target="_blank">📅 18:38 · 24 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OWY_HLs1-uQb5_d_JhbYcqSIKO9j7E55RG_guUCFxp7UPQ7kEThNzneiYjn5_CtkNc2W3Zl1L0pZCwro76GTfz7lqYLfRPSBywRWArEOfih8qbiEe7hf8UuIl42Qfzf0aFPW1vBs0_IpOM25z7vcJlydAbN64C5qRVCuUrWcGTV3VPc5jPZNBZb2bY9U1nA0iXLm6VGq4UcKjSn-Uuf20Qxdxa187o1JUQ0cxXvpjcJx_rBBO4fzwECNfFBO-OgxrF7PMfJRetF4KncgtCcR5Y2RNfUo6_WlDW3INquPXKuq0U35eBWrgqP37exqYdqazj3FHl8YPjXgJpdBDeAYhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسرائیل در حالت آماده‌باش کامل،
در پی افزایش تنش میان اسرائیل و حزب‌الله و تهدید جمهوری اسلامی، سخنگوی ارتش اسرائیل از اعلام آماده‌باش ارتش اسرائیل برای پاسخگویی با حملات احتمالی ج‌ا خبر داد.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5543" target="_blank">📅 17:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5542">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=I46VdjhVkDYWu1htf8W27tLbdDw99s8BImj6FUq6-7o93Lt1D1rUuQVb1YUGNMOHQ7cVnEuvejub42RcVCNA6mMBxuIaCUk031VTzY9N9-lDxT3Du9j9EjakOBT-X_YgolT-4EkJBweMmfDM_5Dr1TDgVG-UkNcaj0PYo6Kwlzkmfq9IkUt2mLjaBy48KwOSdegmu6LPf8tXXenxJwTUD-psvTOD19dw1ooYS_x9nCLaAaAPsAW0lAPEWxFessUjqVHpOYWyoEt61Z579z7G45I89eEWQJL5pkJ97-n6slqCePfN-5e4H5U5dLRWhwwww-TvWoIO-74bkb_R0aT_iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=I46VdjhVkDYWu1htf8W27tLbdDw99s8BImj6FUq6-7o93Lt1D1rUuQVb1YUGNMOHQ7cVnEuvejub42RcVCNA6mMBxuIaCUk031VTzY9N9-lDxT3Du9j9EjakOBT-X_YgolT-4EkJBweMmfDM_5Dr1TDgVG-UkNcaj0PYo6Kwlzkmfq9IkUt2mLjaBy48KwOSdegmu6LPf8tXXenxJwTUD-psvTOD19dw1ooYS_x9nCLaAaAPsAW0lAPEWxFessUjqVHpOYWyoEt61Z579z7G45I89eEWQJL5pkJ97-n6slqCePfN-5e4H5U5dLRWhwwww-TvWoIO-74bkb_R0aT_iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=fAP_I9tHmAl-JsP9CWMpfX4QTi7Chzb00kr6-aVKrKBnEGz3eK5AIhpMu8dPRfBEejCEVJP0FbBzVO-m964a4T_aMJwMMrsxXtuabhSUe5ICv6zIP83BZ4K3j1J59k9EenYqaHfiw6tTu8SPh55G4zkexK9oryUYAu7QG3pMaQ17UXyFnA2fUmCpnj9v98j7-mbS-Ir2PblWKjqViGp0HZFOYuMF_B4714xntVeJMDve2RqesAoJXaHCIWu5sCNhfCgID0vHOw0750r9UIOgtZODoE27lMOurMK8lEijrD7f4zZY1hFY1Amk7S4rJOZtM2eF7uNRxM2vx1WVbvGdsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=fAP_I9tHmAl-JsP9CWMpfX4QTi7Chzb00kr6-aVKrKBnEGz3eK5AIhpMu8dPRfBEejCEVJP0FbBzVO-m964a4T_aMJwMMrsxXtuabhSUe5ICv6zIP83BZ4K3j1J59k9EenYqaHfiw6tTu8SPh55G4zkexK9oryUYAu7QG3pMaQ17UXyFnA2fUmCpnj9v98j7-mbS-Ir2PblWKjqViGp0HZFOYuMF_B4714xntVeJMDve2RqesAoJXaHCIWu5sCNhfCgID0vHOw0750r9UIOgtZODoE27lMOurMK8lEijrD7f4zZY1hFY1Amk7S4rJOZtM2eF7uNRxM2vx1WVbvGdsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=m_V7VfN0ArH2sco5MUtUI9lIRzBTtDIUi1EAHSEXE0bTE9NqeZSo_8MXEGVjeWRpI45txLJQSwVVNlYarULt2vGYe0sC_ZDvq3WI_co3pgrcelbAxSzaUOlTRwj9Z_7cXN3OyB9pc21CIuVMLNag0oZcuOCKhsjADQB2Ef5QQanvw8_GMb3A1tDUEhIWlSTZDkBbA0OT6b_JU33YnB6ye-hMn_RPiouWTs7EGmKQgVOQIbdI-dfcYK3Wy1dxxtYCypdR7Ou1XjuUWk7Q7-vuvVWtWy7OlIGl6-3Rj7HUZxK7-962zgL9mb71yqjHnBv6byZd84hrAn6NBArp22sVTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=m_V7VfN0ArH2sco5MUtUI9lIRzBTtDIUi1EAHSEXE0bTE9NqeZSo_8MXEGVjeWRpI45txLJQSwVVNlYarULt2vGYe0sC_ZDvq3WI_co3pgrcelbAxSzaUOlTRwj9Z_7cXN3OyB9pc21CIuVMLNag0oZcuOCKhsjADQB2Ef5QQanvw8_GMb3A1tDUEhIWlSTZDkBbA0OT6b_JU33YnB6ye-hMn_RPiouWTs7EGmKQgVOQIbdI-dfcYK3Wy1dxxtYCypdR7Ou1XjuUWk7Q7-vuvVWtWy7OlIGl6-3Rj7HUZxK7-962zgL9mb71yqjHnBv6byZd84hrAn6NBArp22sVTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=HDzcpP2ocMy2zhH-HtvAZyd862LlIskeuJKLLI38uMzr_rK-kUp5Uipx2hTMSRoCYHn2Me8YREEvX9uA948a8E2v3Gy2Z6buMWVNO5zPiG7Ff6RNgtrn5AZfj1vNPoc91iAgMEKt7iE24AgPC1ds27IoEno7UVPg2HGXJzA-xy5dWM-R0iuLLIOheQEzv7ryImp28d5nNlX52EQbf1zSt0UOW6Xv02u0QI_3SbTTSV2r_-dW6stsMy2rF8_GcT-fDUF0KBBPHuR5ZG0P7EFfhCkI4v5ZMyeEnRf2rVWWBNet6K7E1kE3X9nQGeU2RniHylx781xkeXOBxICWMrUETw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=HDzcpP2ocMy2zhH-HtvAZyd862LlIskeuJKLLI38uMzr_rK-kUp5Uipx2hTMSRoCYHn2Me8YREEvX9uA948a8E2v3Gy2Z6buMWVNO5zPiG7Ff6RNgtrn5AZfj1vNPoc91iAgMEKt7iE24AgPC1ds27IoEno7UVPg2HGXJzA-xy5dWM-R0iuLLIOheQEzv7ryImp28d5nNlX52EQbf1zSt0UOW6Xv02u0QI_3SbTTSV2r_-dW6stsMy2rF8_GcT-fDUF0KBBPHuR5ZG0P7EFfhCkI4v5ZMyeEnRf2rVWWBNet6K7E1kE3X9nQGeU2RniHylx781xkeXOBxICWMrUETw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان : رسول خدا و اصحابش
لت و پار شدن. :)</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/farahmand_alipour/5539" target="_blank">📅 11:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5538">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
حملات موشکی حزب الله به شمال اسرائیل</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/5538" target="_blank">📅 00:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5537">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=YWsAUYmWfOsyrl5xuX4FcFuDXq8-GkYJW9pMOhGt7lgPfojkNcp5QzatgfsEoE5N1p2FBWfkR6yS010dMP48JycnT-pozayCgzCjuJVnBlMzjjYWkhyZIsiW-ZUFPJeK79kc3OUKOf5Zjsen7-6YHaldvkYYhCFsZMnX8Uum0wIXkIyQJxrVtKFDuLjKD3ZPo80rep76u8nPMhPkELJ1Vevj8aju_1QJYSUxQPEmQ54sDj-2UHqpVgGxqEo9Q-3VG82Riptfff0AbCpfg0XyK_4nwIKWKn59TtGAgclKwRIsdJ1zsAJB-QHT75-u-VHzYBdALGq0C3xd44dK3q01Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=YWsAUYmWfOsyrl5xuX4FcFuDXq8-GkYJW9pMOhGt7lgPfojkNcp5QzatgfsEoE5N1p2FBWfkR6yS010dMP48JycnT-pozayCgzCjuJVnBlMzjjYWkhyZIsiW-ZUFPJeK79kc3OUKOf5Zjsen7-6YHaldvkYYhCFsZMnX8Uum0wIXkIyQJxrVtKFDuLjKD3ZPo80rep76u8nPMhPkELJ1Vevj8aju_1QJYSUxQPEmQ54sDj-2UHqpVgGxqEo9Q-3VG82Riptfff0AbCpfg0XyK_4nwIKWKn59TtGAgclKwRIsdJ1zsAJB-QHT75-u-VHzYBdALGq0C3xd44dK3q01Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زنان کفن‌پوش ولایی در برابر وزارت خارجه و سر دادن شعار : مرگ بر عراقچی بی‌شرف نفوذی</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/5537" target="_blank">📅 22:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5536">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8679568b89.mp4?token=EJfrD7hp7BsHeEgJe3J-nlRc62w8bbkcf66XYmsco9h8WI4B18W1z024Q6NkxZsZFtwOEqOHUgc3kdYXhTpzLJSuRcbc_GsfikI2BnAny7GSOUOMlp-3dFWUboee_kcbguVx6C-eKV_Vmo4M44d8Jj46A5l9wGBcHqpDkdISjG7Gju6w383Rs04cwE0otepxVOAd2IY8G1FZHqR2KHuM1Ui_DwQNqNFthy0fmLkrQ4Z_NIMPKPKRgFFoth147EQ8tKRcAMgTeZYfNtzcP25xVktxr9y_cHTyPh0ZXuyzE71G4JnXu8o5USwFS7NfmBFtkKNax602SMpfOroLHJIUlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8679568b89.mp4?token=EJfrD7hp7BsHeEgJe3J-nlRc62w8bbkcf66XYmsco9h8WI4B18W1z024Q6NkxZsZFtwOEqOHUgc3kdYXhTpzLJSuRcbc_GsfikI2BnAny7GSOUOMlp-3dFWUboee_kcbguVx6C-eKV_Vmo4M44d8Jj46A5l9wGBcHqpDkdISjG7Gju6w383Rs04cwE0otepxVOAd2IY8G1FZHqR2KHuM1Ui_DwQNqNFthy0fmLkrQ4Z_NIMPKPKRgFFoth147EQ8tKRcAMgTeZYfNtzcP25xVktxr9y_cHTyPh0ZXuyzE71G4JnXu8o5USwFS7NfmBFtkKNax602SMpfOroLHJIUlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی که گفته بود
به خاطر هسته‌ای
دو بار با ایران وارد جنگ شدند
،
الان با ژست پیروزمندانه! میگه قراره
در داخل خاک ایران، اورانیوم غنی‌سازی شده رو رقیق کنیم!
یک ملت فقیر شد تا اورانیوم اینها غنی بشه، دو تا جنگ راه انداختن،
حالا میگن «در داخل ایران» میخوایم رقیق کنیم! ژست پیروزی هم میگیرن!</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/5536" target="_blank">📅 22:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5535">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=HR9Ra1AMngIxOTv4nFCZwvQbZhGPLGyipP7yMXfYqM_t-FEZE152kRG58XZFuUzViEIW8Pe3PNAEX4pm-hHBdVCMgqeHVLVYA-NdZkar7rjR6mZzG3p14vKd1gVDJAoX191GMgftge47z7W1CjXzf5c86pO9gkdovJAFKmkSBXid0Eyt4cAbGstBBRPzAwlK5P06cMoQgZz-Z4Tgsbl6HhzF0Zx-xgHc3eVJq1CPTUt1KDA-qZLm79-9jk6DI_3ZDLVgV-q4-UkAKz2-qt8P5s85tofd6AUQpT2X8k6ohSMRvo3pC1qemVmXg4JbqA-aL_xaV1LLindKp9CWyTIO91p4HqmLceRy6oEBZEKue_Qg091AwWxaM8goxuLmJGTX_3gMiYsgIucqz4-l0XmBM-8chmYTWU7Pq-vGP3uod2ntpJzxXxSWUKpf1_QrEleLq5JcvMFgTR-qVjZuOFpSOvpN6WkSHTXBF-3cwUU1s253nnkkhg67PD8V38YL7e9QOpUQHiZ9E9yX6aLSXXFrtsINUoRKF0-B6H8HCuJBv6r73CY0WrZbzuDMLSfh_Qnql16XicHerLa4fIC33bZ-wf-ay3got3ETN-Iz_9_sCXjpHxzODP0AGBcw9B-PESbnIQPDzG2dGfRdO5liCCtZ3GdCC3qlC2JhZBf3iLX1FPk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=HR9Ra1AMngIxOTv4nFCZwvQbZhGPLGyipP7yMXfYqM_t-FEZE152kRG58XZFuUzViEIW8Pe3PNAEX4pm-hHBdVCMgqeHVLVYA-NdZkar7rjR6mZzG3p14vKd1gVDJAoX191GMgftge47z7W1CjXzf5c86pO9gkdovJAFKmkSBXid0Eyt4cAbGstBBRPzAwlK5P06cMoQgZz-Z4Tgsbl6HhzF0Zx-xgHc3eVJq1CPTUt1KDA-qZLm79-9jk6DI_3ZDLVgV-q4-UkAKz2-qt8P5s85tofd6AUQpT2X8k6ohSMRvo3pC1qemVmXg4JbqA-aL_xaV1LLindKp9CWyTIO91p4HqmLceRy6oEBZEKue_Qg091AwWxaM8goxuLmJGTX_3gMiYsgIucqz4-l0XmBM-8chmYTWU7Pq-vGP3uod2ntpJzxXxSWUKpf1_QrEleLq5JcvMFgTR-qVjZuOFpSOvpN6WkSHTXBF-3cwUU1s253nnkkhg67PD8V38YL7e9QOpUQHiZ9E9yX6aLSXXFrtsINUoRKF0-B6H8HCuJBv6r73CY0WrZbzuDMLSfh_Qnql16XicHerLa4fIC33bZ-wf-ay3got3ETN-Iz_9_sCXjpHxzODP0AGBcw9B-PESbnIQPDzG2dGfRdO5liCCtZ3GdCC3qlC2JhZBf3iLX1FPk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توضیحات نبویان در خصوص وضعیت تنگه هرمز در تفاهم‌نامه
- به محض امضای تفاهم نامه، تنگه باید فورا باز شود، بدون حاکمیت ج‌ا، گرفتن دوباره تنگه و اعمال حاکمیت بر آن تقریبا غیرممکن می‌شود.
- هر بار که متن تفاهم عوض شد ج‌ا عقب‌نشینی کرد</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5535" target="_blank">📅 21:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5534">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWER3OrIU6OhjG76giHSkDAXNm0seV6ETJpNdYoHMqgoX4g5AZ1Rr0I5TmMQCLsim9GLLkfu8-11bWRUQAJV-MKE9iIPO_TKJ8x_EksKqvaGDzmlTgHg6I46GyP1tfX_rB4XC3VHR6PHVDS3DtUtGhKOdrEgj3KoyKsm8k2hU52fTnYAGrvDhusOZDG9tgGsywRgdFRBqI8-SDx4FBObC-7DpqdFojt1yXixvZCCBy2_J7wzZwAxtfFsmy7TTWDtmc0yhVAxkIahnwfs1y13xI6lsG-kXwS3m0SUn3y4u9rRKC1ufjsAaSY4xMlbVU2uQt40k_vTrTKHlz9EJ5R4Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: اصرار ترامپ
بر امضای تفاهم‌نامه در حالی است که مقامات ج‌ا  صراحتا گفتن  تفاهم نامه هنوز نهایی نشده</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5534" target="_blank">📅 21:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5533">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=Wm0sfbeNByKuK2_EII_SjvUyN8n_ARxNYON5tf8Bq2vf6XUkbBJj9nEckb3vROumt3bDJ4Q-ljQWRpLua4RHq7Ehn6afFYNr2LI8waGg9WKBEtTOZ81tHxXU-K1bO31i1ou2C9BcCNIEvdS8H1nCZEN2o_SybAOxM7hCVP1luAeXNRegIgyzlu5KF6oECw-TShmKJIg6t36o1QdOg3N37BfUibaqmKMe430z099Nma4WJRe-gU93P78kOg5v1jFfxxfQ9GicFWXUuYPpWY7hOKmEuK4r-MrSjrMbCHxewKv6uFGSeUvgTpg-B-rhYaxGgwPnkzvfdsHlsrQilxS9qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=Wm0sfbeNByKuK2_EII_SjvUyN8n_ARxNYON5tf8Bq2vf6XUkbBJj9nEckb3vROumt3bDJ4Q-ljQWRpLua4RHq7Ehn6afFYNr2LI8waGg9WKBEtTOZ81tHxXU-K1bO31i1ou2C9BcCNIEvdS8H1nCZEN2o_SybAOxM7hCVP1luAeXNRegIgyzlu5KF6oECw-TShmKJIg6t36o1QdOg3N37BfUibaqmKMe430z099Nma4WJRe-gU93P78kOg5v1jFfxxfQ9GicFWXUuYPpWY7hOKmEuK4r-MrSjrMbCHxewKv6uFGSeUvgTpg-B-rhYaxGgwPnkzvfdsHlsrQilxS9qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۹ ماه پیش
بعد از جنگ ۱۲ روزه و قبل از جنگ ۴۰ روزه
این تهدید پذیری اگه به وجود آمد پایان نخواهد داشت.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5533" target="_blank">📅 20:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5532">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sd55jvEWWc9igyPdlemy1BCd6FbeA8O15fsVYBwaQrMnrQWB8zqMop1OUnpAiXAmlBIHo51ew9QKQxHZ1BWKQSO5ZfZFWDUEcB8VdgIDdlpae6088SsOMYqmNY0gKpwRaJx8Ylt2Biz8nbDfGiJd90eaPQso4Z9mroh-W_xj1AGXyQBWY2CGYx3gM1Fg_GzlTRBnXHPmhIU21g3kWw5jIB5xGxfAa3Q2G9KnfWLU_3aIoN7nXtkr3wVUzGt9kAKmMT8Gf7_XsReuALs8ytTJX4_uKLJXfiTLfqVjwRzzvQonQ6q8N-oVIxTCk_cdpV3BBh_Bx29PuqFlz0MbGTjs4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwhANuvTAxhhe4BIm1phXhBCUbsDv7UCs5YgKeGw-Vx4XqD9vBKY5zdik2XWUVVDH7mClooZwbtDWkgJP6DYQ3tODMyL94nq2AbvFaZop0hvVNGOB_YwrW1tyimJRPDPcp2r1pbYQVot1HHuTJWb1zhd060zOthP7H5-2sXityGZakH4KBklElbe_xC7emFeKpqXle85iTDoK6JWcjj6xXeBXYULysAaRbfrK-aZS--dk-9xmUWvgMHnxuMOpluNvOw_vuiGx1sA5ZOWMOcrcWwRMzAImklxk_C8nayxSbhzqHkWjRfu2O7pI9VoGtlAPKSN5bccaMi5KhTJ1KUM-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیسی خطاب به قالیباف نوشته.
نگذارید خط تسلیم و سازش با
قاتلان خامنه‌ای به ثمر برسد.
(نه سازش نه تسلیم - نبرد با آمریکا!)</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5531" target="_blank">📅 20:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5530">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvxV-WrcXWcQjUhhxckoizu_wCFfINr7p3xFyiEC99XAVjb8MtRlNv0JJNwY5cwvT4Jsp4XK5dp34oKF1FNq6Y8MptlhcwkxaYmgfXLMA6viI77ZmuGpkAJUD7D6mNJ-eNk0eAi5vJzZJcH2KWSzBxUHgqgsbgC8zmAnGxrN_vXa4e6BmFLnRRfFs-jmLTNl-odB9b6UR89Jq_ldGPhSrXFfM35FJPAyEYm9iT_5fOb77-q9ZimeYj5QOsBDSXBFBaUTNua6ESyYhEh5zinnMIlRhdAhB14Y6Hgmehky-y27oILU9C8U8JXNjEaGf9UDe1GicefF8oirZAqA_7EwtA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=JuWe0Lzmc-b0YoWEqm1e3y_sQHMpd-BOg3bAfvhFd-zZk6s-7mgCauCnXxdPIUbbVLMD-vfZPlekJoOl1xoxtNoilQeeSgc7Czl-Xau40pbIxgEwyOEvJpax9gKEZRTCOLqChMAoipfd9l2s7FvZEbcOn2xqhZmYo0eOhVCqXfggDlUgUl_PKAXq1pN8mfft3O1cNbTj9cNLMpXE0Nx0s-z9qoXPueWngjNaFpOrbppXWPsb7RIks9N3sMsjybMbWuj2X564yBLucchGJOn2_3_4haoHPf52k1TNonWUzgftxLL-Dc1PBUYOPBVLmVHnqbaBKpEDUFK3rxJPQLl0BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=JuWe0Lzmc-b0YoWEqm1e3y_sQHMpd-BOg3bAfvhFd-zZk6s-7mgCauCnXxdPIUbbVLMD-vfZPlekJoOl1xoxtNoilQeeSgc7Czl-Xau40pbIxgEwyOEvJpax9gKEZRTCOLqChMAoipfd9l2s7FvZEbcOn2xqhZmYo0eOhVCqXfggDlUgUl_PKAXq1pN8mfft3O1cNbTj9cNLMpXE0Nx0s-z9qoXPueWngjNaFpOrbppXWPsb7RIks9N3sMsjybMbWuj2X564yBLucchGJOn2_3_4haoHPf52k1TNonWUzgftxLL-Dc1PBUYOPBVLmVHnqbaBKpEDUFK3rxJPQLl0BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان مناطق اطراف نبطیه رو تخلیه کرد تا در مسیر ارتش اسرائیل نباشه.
این جنگ بین لبنان و اسرائیل نیست.
جنگ میان گروه تروریستی حزب الله لبنانه
که با پول و سلاح جمهوری اسلامی و به خاطر خامنه‌ای، جنگی رو راه انداخت.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5528" target="_blank">📅 15:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5527">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fy1AqCDkyxOouT0LYYVNH-slLahrYcVhYNMfK0w91tLuvAkAI-NsQjGCVdjLYdmuk5FosePxPKaqZQ3AKCbhc2nxYLia-lKXDjvgkeuOB3UxgodYYuwfxyk_GNn94AiopTeq_gH_fA7Sr7lYa9ctRPJ45ndsbZItYEP6g9RyCWpKR1PeMrOVlorzu2aDiubakmvV-8uXWz0wOgobwDWr_hqfQb20nnfRuZjG47hp3m520Yfq09cBe2Uq5Fi7Xpq69PioGh8e05nTN2ir1n7w7R2thWH8Qv2snpZjX4o3meTbdJIcDSz7zAh03GNth2ApPn77zLuESBE0VkA9LRAusg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی در باز بشه می‌فهمید
مجتبی خامنه‌ای در واقع همون قالیبافه!
چیزی به اسم مجتبی وجود نداره!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5527" target="_blank">📅 15:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5526">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O2bTv_laczwJ44Sd1nko-BhEbBGINMmXe_pgyHKHunlQ_0M5Sg2QGvIl-9bejBqLVqI8dO3rJL4oDYtavZb_fGcfd5FBKarHWvO9uZceAjRAv-E0k5mIQAQ3wqj2t_WJZXfhgqsU0snO2FyaC74CXym110H3E9FK59L0pXaacWhaOPC9GEui6gZXgC8sGm7fn3TS7Amw_-EgCgtVBIBdPkYU19tYsy82_E9dvkLQX99QbfoJHrecag77u1_3lUV-w2NK13yngzxFXDB-LGbQ74d5OFZGoEHE0MOdgbeXtGjTU1pPGR002rE3yvYJv9Fj-I7fBBQLMaapRZc60MZp2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4stczlo0CmpxwsZ0pMogV0Gb2YpJv81a5zsx89d4ylwumkAWbajsAm-fnIiV5bzuegLhf8d_N_TonXdXeHHrmY0M8yPRXWbmRh3lQE0A2k-qh4-GUTpeb9WlWwaR7I5yJOKWT_mCYyKNuE4aowjDdUSSJSpsiaInc7IMBHN7YmPHFd28UXZSWyS6kfUUhehF_vgxOQEgTFCJo4nZU0MgurITNeDHiqjNLsJzMwhwvsz2ndQTcenzD3XPkAPhgxYaYZ_HryVOIqKlu85PWUucOHGGsuF8Ht9ZG91RqagTvuzraYT2LguBwMiQyea4_MCKS3rmRYKVXpt4O-U4JAX7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات مراسم تدفین خامنه‌ای</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5525" target="_blank">📅 13:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5523">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tc8T0Il0RRWfnaO3-32Y5hCoWQN4v84TZUprloBuyuec8LldvuF_kM8RZqrjBYW6CmBaS84oUeVGvQeW3GpKW1S1yvszbZDMviV9XNsi9JPHYw4KMdo22pLNTss5vXTqDNu8_VfzNtVN2TR8k3fHP24qtEMBu7LFEuZq15dbf30BOJTHsB1yia2RC8KwmmAbTtW1HDsv6WISgl3ecDHnFUWQ_P4YfPs_RCDo1YIlDy720xR9Eer-esbAsjQFvuPWVzy5rGWMQcaQyi0w7hYiHyp4Wji0ThLRMFECbUQbB3sEX-Yub05_8PRA4MCv7x8TqnMbmRWuxy0gWEQBaj4l3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=CCYEi1mEk6d9w5auc_DSZlM6nKHUsNN7v8NdZv2tPmbNqqZ8xqsFY3JdzXca2jDvXRYhzLnpz6-g5rKVmUAXwg9vUpLHGhVYwhHQGwk040YFi7GaWRzd9NNiqAbghDvla8uh6CADgleAlWG9HS4IMG_qaRoN1yD86WKKjWousnfVe_r25xuaglKMIsReCOWDPM8p-2HWx_JcMYEZ6B39OKWX8AHmBSMI2CTEESMs5wvjCygtDZakssqtSOGqCk9N6ItGcJluJT-LxIlCEogACPH4jwo3xTB57iTOvOfRBpX06mLF2g7dGaQ0MUooBKjxOc8Dk6gUDfW4h1pPZT9YTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=CCYEi1mEk6d9w5auc_DSZlM6nKHUsNN7v8NdZv2tPmbNqqZ8xqsFY3JdzXca2jDvXRYhzLnpz6-g5rKVmUAXwg9vUpLHGhVYwhHQGwk040YFi7GaWRzd9NNiqAbghDvla8uh6CADgleAlWG9HS4IMG_qaRoN1yD86WKKjWousnfVe_r25xuaglKMIsReCOWDPM8p-2HWx_JcMYEZ6B39OKWX8AHmBSMI2CTEESMs5wvjCygtDZakssqtSOGqCk9N6ItGcJluJT-LxIlCEogACPH4jwo3xTB57iTOvOfRBpX06mLF2g7dGaQ0MUooBKjxOc8Dk6gUDfW4h1pPZT9YTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVfNUVkATqfz728SkvQH3IiwvdulcjcfUZJ0lChmzuTZwNux5cGW3_pKCjWHljQy7GvgyAd47-kxsGpv7cZpLAGivatXofBMPzCv8SPQ13mdUNFFWkT8TghX9ejCoZiLcXhh7mbU_C6EvRhOAyVxCkAPD9PTVWbr_0k9VXO3czqe10XDH8KPGyetc40Hs569IWZG-8ssBX-lSVinzEHGddZ5rHMdQ4k8P5uAJMNYhfDXd3eskhX6jlCdqDXEyNzUVCupbsup7LrjhY-sE9DX3Vq4NSZZunh7oBIy8oru7Ak0Fgu6ylItkAvyv8MrHlHQgdMFHzMz3MVdrqzqI5bWbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzrhqa227VS75OiuJdcPQm4NlMf0cvNtLJQvwpzxB01atri2XOPEBr5J_8oTuHUuTZcm5INmGa9_d39zOYTLGxeUDFXo6G-DTq1-CRJYO2Hq6G4Gg7c50xa7V7PUJbkyejaqhafXSNg8bgWZPh5WbzsSDf3PHj0PKi6q_bLJNRKuWbKjSAfKriwkbdk4cQM_i1KMsvhuhwh05oaRpxKqPvQZ3go_WI8VQ3ew0NaU4JB3Aa2DK_JIx4i3XkEAAK8vVYAMQtD47wEbXvxcl4WM9ER4rbiqcx6oeuvSzMFG-VeHlLapLu7_7yvR4U7zB8zfL0cF2ZSfIv1enVABS8J82g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5520" target="_blank">📅 01:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5519">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=EafFvx-7ZhGnTkEoz6dqIXjEVwEK2EwS0iC3WyS7mK0g1sS98T3wJz_ugahEMZArLNwJ2iCnKcl7bjRswljEPJCtXbEUIlrrt2L2Kj5F1kSU7Jzj9h11nUjGTbvj1mZemTSAPmn3S-8bOKSNABtZ3qn2xqVco_kXoSpaDydQl1ySLPggbwwj7D3kYUbWnoXvQAJPuQCO4WCRiTyxBYYOL0-RfV6DR1yoYBjdl2rrRwMjejUjRjWWXfetHUHSq5hmcSBjT278ncQRNAE7y_I28EL9XalrGESjV85uCbb3zj7Kr8Fkx1_SsBJOf7cUeY5AHEHDVx-5SaO0hNhuGffyVxaL2lIGPvmbrcUVeJN3yhiG3HqFNARDuXjpwJcweRrv7dbClF9TVWtkM2EIsHBWD8AmQYC8GPRcIw4OvyO9xg5wBRrZzqnUgxsZm-hBMGIsTknHEAJ6NLVWhEZk0PoaAvIdVU178ue8c6FULr22aK9dkAFJmN09_jMwB57h4w0bNI2Oy-HPN_RpwB4E_8ykqIUNz-c4Id5QfBFgnmQVErTN-qCNM2H__LxR8jiY_uRplimPUU2zcmmZeFOabZFcx7RGEdG2oxWbuQFqivLzXwNed4f8EsH47lZWBnnqBbX-dRTnT_KuXGYjLpFpn416yfpE76aMR0vuevOn1ACwDfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=EafFvx-7ZhGnTkEoz6dqIXjEVwEK2EwS0iC3WyS7mK0g1sS98T3wJz_ugahEMZArLNwJ2iCnKcl7bjRswljEPJCtXbEUIlrrt2L2Kj5F1kSU7Jzj9h11nUjGTbvj1mZemTSAPmn3S-8bOKSNABtZ3qn2xqVco_kXoSpaDydQl1ySLPggbwwj7D3kYUbWnoXvQAJPuQCO4WCRiTyxBYYOL0-RfV6DR1yoYBjdl2rrRwMjejUjRjWWXfetHUHSq5hmcSBjT278ncQRNAE7y_I28EL9XalrGESjV85uCbb3zj7Kr8Fkx1_SsBJOf7cUeY5AHEHDVx-5SaO0hNhuGffyVxaL2lIGPvmbrcUVeJN3yhiG3HqFNARDuXjpwJcweRrv7dbClF9TVWtkM2EIsHBWD8AmQYC8GPRcIw4OvyO9xg5wBRrZzqnUgxsZm-hBMGIsTknHEAJ6NLVWhEZk0PoaAvIdVU178ue8c6FULr22aK9dkAFJmN09_jMwB57h4w0bNI2Oy-HPN_RpwB4E_8ykqIUNz-c4Id5QfBFgnmQVErTN-qCNM2H__LxR8jiY_uRplimPUU2zcmmZeFOabZFcx7RGEdG2oxWbuQFqivLzXwNed4f8EsH47lZWBnnqBbX-dRTnT_KuXGYjLpFpn416yfpE76aMR0vuevOn1ACwDfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5519" target="_blank">📅 00:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=eSY6wUrrH_Kxk8qFumgdZPKRztjTcNOiVVEw8VylZ-fNQIIpmRXLn7LZ658hnEcROUYOHDBV3BmlgfxENxGs6_lHjBB3KjIvUPetEqhBHcPP9BiIcyJgm7Kr-hEtABcP4ivaCc0_UDCvGvzyF-hiZ1lRNeTReJWpXbNyt0QmPxr2vMYFQrFyL-FHT0ut500oFahLFoyREvi6N64k6h8nFTM9DMipSwDRrRmjzH_Miy3HxlEvRWxMkAkvaVKvxYcngV_h6sSNDSSuKJpxBpE1cH0Z_3csj_9TONgx-4-Hm6xQkGlcLNG08MppcO32oZsXUOLudiV2J9-oO_eHun8YsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=eSY6wUrrH_Kxk8qFumgdZPKRztjTcNOiVVEw8VylZ-fNQIIpmRXLn7LZ658hnEcROUYOHDBV3BmlgfxENxGs6_lHjBB3KjIvUPetEqhBHcPP9BiIcyJgm7Kr-hEtABcP4ivaCc0_UDCvGvzyF-hiZ1lRNeTReJWpXbNyt0QmPxr2vMYFQrFyL-FHT0ut500oFahLFoyREvi6N64k6h8nFTM9DMipSwDRrRmjzH_Miy3HxlEvRWxMkAkvaVKvxYcngV_h6sSNDSSuKJpxBpE1cH0Z_3csj_9TONgx-4-Hm6xQkGlcLNG08MppcO32oZsXUOLudiV2J9-oO_eHun8YsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FznkkcQYLJRyQkq6JdjalDSw8yvWsYHjZ90PfzmCgTe3j4x6G-7bUfJ5QTDLzFDrEF54dDmXAWBUZNLvoNeHJ3NKnXB95Qa0GN4KvZ3iPIM3oFeovMoBsaVDMWXn_LlIHODJ3Y-zkoF_N-Mo0_tl2qXvPEl1Rnwd1bl8ZuFuVN1Rc8D_uq12_jJBlic4Se8tb8EVQM6iu3ic0FIBuMtQDLc1qdW8gHFN02l-5rJZDSfCHXeur0KwbtOIiZoCUOiYu-J0CmCl04Plb85rrB6p2PmFUzsFDJWyCqd89GyMb3_CiqbKx28Q2DaMrPXC5zbgMzb0hzjJhFMAQUw-gchfCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : این مواردی که جمهوری اسلامی منتشر کرده دروغه! اینها یه مشت آدم بی‌شرف هستند، اصلا نباید با اینها مذاکره‌ای بر پایه حسن نیت صورت بگیره.
حواسمون هست که دیشب هم با پهپاد
به یک کشتی هندی حمله کردند.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/5513" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=rInAooa2HD8E3ZBIwb6fh10h4Kxd70wnvVKQbMol-Q1a8ZfQ2Nj7Ud0XnwImkfgt9t9gVxG3PkEFsray7l-iR1586cboR5LW5ZR-siydTEqVxu_RQzc7o2seYbLrsCT0ofwzf71i6R-QIeYbX6QsvKu2F4Ds4yRVesBPWgsLMAi579C7y9RbCxxMydkd60Jj05EqlntT_SqGi07CET87JpUkfogTCfrWsOJyAwfv5OjVWXLTBLOmOrpar8MssAKDY4qZ7ynqyITHnrGtNLEFvJamcHUbUYAppv58mNzHGsDZ-geIVRgVIvSP7BfUX1KSU3xjKnKfJp-Ixg4cwKGb3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=rInAooa2HD8E3ZBIwb6fh10h4Kxd70wnvVKQbMol-Q1a8ZfQ2Nj7Ud0XnwImkfgt9t9gVxG3PkEFsray7l-iR1586cboR5LW5ZR-siydTEqVxu_RQzc7o2seYbLrsCT0ofwzf71i6R-QIeYbX6QsvKu2F4Ds4yRVesBPWgsLMAi579C7y9RbCxxMydkd60Jj05EqlntT_SqGi07CET87JpUkfogTCfrWsOJyAwfv5OjVWXLTBLOmOrpar8MssAKDY4qZ7ynqyITHnrGtNLEFvJamcHUbUYAppv58mNzHGsDZ-geIVRgVIvSP7BfUX1KSU3xjKnKfJp-Ixg4cwKGb3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOlCwLF1nZdXjbQS8EmRBIkHjgg3Iq6hx9CgNcrMZa74kt3uuIxIC9Lnq4bUPf27-xhD8W7cPeIRrmxB9YlBUO_V5rjMTtk0vJrRmOIPycHy7U2V-MABQDKdLmC0CVMrqvxpyNTyV9wQ_MGKQXkxI4XK3goLxN9VNMt0nP6o4a6xlvAkn3ESRxTQL-bZaFAIuAeCSzZMZsoFwZrk7dcUXuCdl7vk1ovcLSf6HJArkxCiTe7Nt2JvzkKPsC_yfGqFO0-9EbQM78xV4ovhnEGLOx8GVcb4dQvSme2hkwvISU1kOFB4N2XgwU_aFUIFdVPvBC-GcTv4iSl5qmtAUDcuEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
قطر خود به تنهایی حدود ۱۰۰ جنگنده بسیار پیشرفته دارد. شامل ۳۶ فروند رافال، ۳۶ فروند اف ۱۵  و ۲۴ فروند تایفون.
🔺
بریتانیا برای حمایت از قطر ۸ فروند تایفون در این کشور مستقر کرده.  قطر همچنین میزبان بزرگ‌ترین پایگاه نظامی آمریکا در منطقه است ولی اجازه استفاده…</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/farahmand_alipour/5510" target="_blank">📅 12:43 · 22 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=eJIx9teYdzHWYhhdFVUjhJrIgacswNpzpyMHdenpD48wgjoAhlU3738S69zrSs_unnyRmb-sXzMgUZ73pVBkAfs-XTqNtf1MkbK3q98gZ1M97TDXmWQApzxV7qTCPX8JTELNI1SBAR-chsPYsxgs3qS7hAHoWDRsSbBYmucNJptYbxz-1CnbwOz5690mv28NhqgW-VznlKaYrARcfnAn7f0WBJDH5vYhAzRFlvsVqbhubvDC-tC7uEYRiSqRwp5lm9l9VZBhTH9RJRtQFYy64cVNAH9A_DZ-CPQ0NAWFHM2byf8lLm_jW8VsOLYpcMiTyvon5L2M1_cD8JLpfj7Tiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=eJIx9teYdzHWYhhdFVUjhJrIgacswNpzpyMHdenpD48wgjoAhlU3738S69zrSs_unnyRmb-sXzMgUZ73pVBkAfs-XTqNtf1MkbK3q98gZ1M97TDXmWQApzxV7qTCPX8JTELNI1SBAR-chsPYsxgs3qS7hAHoWDRsSbBYmucNJptYbxz-1CnbwOz5690mv28NhqgW-VznlKaYrARcfnAn7f0WBJDH5vYhAzRFlvsVqbhubvDC-tC7uEYRiSqRwp5lm9l9VZBhTH9RJRtQFYy64cVNAH9A_DZ-CPQ0NAWFHM2byf8lLm_jW8VsOLYpcMiTyvon5L2M1_cD8JLpfj7Tiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=E3iD7bA26jhb_HBEGl7yUNzrdQe8PCGRH8oZw91yfqNxBHgUbamI6xknbpIaybto25vbVpo8fkZIJiaVLW_tVqlQ312jbDzQxOkAuSEvUVmXLMY8NhzOFE0gtaGOAd4LlUDsdxv6DlB3fsPaR27FHWxkIr5ffrw4iLmX_V4Wlu_q2fbEYuU5bp0cuZx6rmacHIPRdiw2xD3cVkdf5W13oXWnkUPG9159jlf0hj4TABpPmlUKxTS5fklny_j8_r54VFqqoIiTEQEBLtb8w_-fQkoLSboPJj8BJpLHAg-r1yhdy6dEprN1j9zUNwgIF1lrYXWZL-TtRDPjd4Evi3C0og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=E3iD7bA26jhb_HBEGl7yUNzrdQe8PCGRH8oZw91yfqNxBHgUbamI6xknbpIaybto25vbVpo8fkZIJiaVLW_tVqlQ312jbDzQxOkAuSEvUVmXLMY8NhzOFE0gtaGOAd4LlUDsdxv6DlB3fsPaR27FHWxkIr5ffrw4iLmX_V4Wlu_q2fbEYuU5bp0cuZx6rmacHIPRdiw2xD3cVkdf5W13oXWnkUPG9159jlf0hj4TABpPmlUKxTS5fklny_j8_r54VFqqoIiTEQEBLtb8w_-fQkoLSboPJj8BJpLHAg-r1yhdy6dEprN1j9zUNwgIF1lrYXWZL-TtRDPjd4Evi3C0og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی ظاهرا متقاعد شد که شرط و شروطهای ۱۰ گانه‌اش رو کنار بگذاره.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5507" target="_blank">📅 08:17 · 22 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/5505" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5499" target="_blank">📅 19:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5498">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MT0zoobLRU56LWkR_vxtglyfVF3qSOGE3BXpa4QC1yxYq-D1zimkC7JcumprBnFhitP0Gm5glwGnLpvWnvzy06smGuAmczBAct3r7xQnL4GyURV8_Yvm49xUrMvKOHWXDcb1_1TYzbp59STZYnDcH0yW7yUnNeDOSkdXnv1PX--mi6yrK5I1VVqZQVzkM_CgNgyzQ8-dB2kn3XCj-ANyRDb2Cd3aXEumEl-0ghRt15XrEUSKsw12H1ERGGmi5KVu5BeF9QHghVZqrmTU_03v-IyBWN-k6fy_8mrXnJqe8cuT-HXHpnmnUCBUj9FxFN2QJSHQxRg4sVAsWs2qJ-cixQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=SfXAFZy_UeG0xl8Q-PRWOEBdOWoKoX2PCmd11Eq5hww_QpMS81Ax6iDHj4jIP0ZWV4HYt950ZZ2VcVEMBTggn_yx1kCU3zOKjDsvwrp2HVwwelcHl1MJlePU2qTmEv1wNFf8cPEJ0valjNSax9tWVxbjiVy3FpGvIy8LAZzHjEgJAQIWGInjNNt-koh8QD05IXMHPjBt6BAOWn5QMG30kvCAM78LsKQoVYAerzoSCJuZdnXl2fzKft70yzEfJsvOqhwRvOeUHY8oYAXmiYwt3NK3wV37mD2v3Q1pvKe0nPlzJU6HHWQftSmwqlZHTlKyysBA5-T5Q90lxM1oaobMbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=SfXAFZy_UeG0xl8Q-PRWOEBdOWoKoX2PCmd11Eq5hww_QpMS81Ax6iDHj4jIP0ZWV4HYt950ZZ2VcVEMBTggn_yx1kCU3zOKjDsvwrp2HVwwelcHl1MJlePU2qTmEv1wNFf8cPEJ0valjNSax9tWVxbjiVy3FpGvIy8LAZzHjEgJAQIWGInjNNt-koh8QD05IXMHPjBt6BAOWn5QMG30kvCAM78LsKQoVYAerzoSCJuZdnXl2fzKft70yzEfJsvOqhwRvOeUHY8oYAXmiYwt3NK3wV37mD2v3Q1pvKe0nPlzJU6HHWQftSmwqlZHTlKyysBA5-T5Q90lxM1oaobMbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMYj2RLGEJvWUEZo2t5x9VOZi8Doer4TgWGYAvaYRreQq57r5yCLLMUr3s-QFPmqyWiklYtyc3xOfzEp_fxrEWq3yDwzR3zCt-mFJqIJjfmQ1ozIMhCJw7evqym87uCbj87-IW6FXLyw-8LxIZxf90xIUGy-AJLBcjOCpJXahw8SUO-lhCLAtbCvNTYiYrfihpBBDHqpMUcNrf05E7tfLg0APEZ8-g3iWmemrMQPHTD7quVLG0XNIx9EvH6rwGOSIUI289xSrFmN2XtOSx2SOZvnN6iiE40DN9XpxEm7L-UKjjU01s-Wm7D86lQtmoUIGXvpk4Ul3OvMyV0O_vlGGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGDqVp2QGDDB-QX29ruieqApNTk_xv3g8PNXXjAAYkvFkK2moUITOqSjZHGY0lgnk69d6g6X59IVtOrQf3t-cpOEu6YzeZEv7hxGnxjHpKPM9HO2llnMkm3sO-HiSueXgi9J32_11dOp57KZ7_QmPjOtFAem5c6HyFDyQ01kYQTYZexmRc4tUDdTLzz7MfTvV33wu2H3q9AKCW07A-ZutQ55X8lRrOwdRwUnTsmj-0VM7O2j6dV_18Wv1ItBB0-tywAyz5xTlA6sR1J9sf3MzcUImQzHtHZhvVNYRjMJqe5X-ho1Gxrcw1luoaWvioYbyJnmnhkruleQszM4mnBbpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از انفجار در سیریک
مناطقی که در دو شب گذشته مورد حمله آمریکا بودند در واقع حاشیه تنگه هرمز هستند.
جایی که رادارها و سایت‌های موشکی و پهپادی و…برای کنترل تنگه ، متمرکز شده‌اند.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5493" target="_blank">📅 16:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RS_KNtf-FcMeD3xPtqCChBafsWHJCCgtejJhIgFbnO2X1cKEJ_12rLl0nIBX5dbKFM3EUmjIbYfgjmM8OMmeqoDLmiqAmTKAubyLMedeUErDcrCG-U54h8UzXDnQHD8PsUm22qZDYDHlRLKjkPWf-JSIp_edq8HV0g2RZk_rr11nHEHHNoBavwUR1FreIUtFxJ9kaOugTFU8lOVjTXCogiNx0H2M3XhBmWTK6uTFRWwZrCuWVjbSFgD8KMDywF6DdimuBS_cdmSJem9nJSVtGcXxmV_kwPR4pov0pRx7C7hAaQ0O6RUvQ_FDq1jHJnDDCjCs3BQByv8ZEv39afJLtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اموال ملت ایران! که یا مصادره میشن
یا مفت فروشی میشن به چین
یا غارت و دزدیده میشن !
بقیه‌اش رو هم‌ میدن «مداحان»
و «رجز خوانان»!!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5492" target="_blank">📅 16:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJCWZXhlG4M01GMohVFGJCMcT1EYiQ2eDyQYTBJLvS0mBIhtwQGdld6AoopUC5RAQswlnTkVTh0ShAWCAkLaoHFHX-DkgP6OU4w5Oo5D8NbZVEvIYWzCsyPKTqNu-uTkvM58roOoEiBONCG_LuadQ8Av99WMH49xxVqbjuaJTGnrFaC2_gV_C5DI_xOphlpkE_fMf161BF54Nn-TqILGASoVTyzsnV4ZnK0-KDkFpR1z34eZnCpWhiqhld2F-AguQjOshVEaXubf8fMPz3S1t5dr-soIFaCeltC-5Jjz9z3uj96JGKvxB-FxePRv8AC2EqtqX5ta5rTgrBa14ym7rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5491" target="_blank">📅 16:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGc1MkZgvDYqHqLYrX_okh-odL1zcSMz_hPYj4ggLtJELvgvvFGFGOUZ9-l80OZuTZQNtcc8pBogcVQYg7NgQLIvRDnMLyPUFPSUvKsZ9z9p8Ry3eQDi29j_urMIBoNxwMJzfPrbpSgMl-xkgnxJMAP4Fev9mSCaWL7edmmm0pEKi1aGJdAFzNMAf24UwZv-hcxZ31EqMfUi61rZaBUsSicTkjgWL9CM161ElH-62Y7rrLIrCNmLaRH8UNaoEpb_BC9O-S_CysOx30ZUxZArCwFRtfHsclmNlULepTkJG4IlTSqgpVzYme22iU71RmcdinM56jd9BT7Ox6qUkITTHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCgx6IEoKCaH4ny4vGcwHv03RoCG1GPLOmwtE0gUky2bbhwuh9j-ztKgdz809Zn-z3MoV9Hmi-Hl8GRSe909tJ-XDDibUdxSUpt1HPhfUDHUMgDzPtBVWb1el8Mm-WCdeVzMnvkmtjriy_4j2yK5I_5_rlZS8xIvemzXvU3SBilhRRp-vF4sPQJkCkMsyNWL7V4cqMbTGIQirlnRXnAiWfYYj_1OW44-pef8MN1Lv_--qMnnzt4pVCA8l6e8Dw6IBYtKNfNAI30H_fUCWwG3cpqZAHbZYxv--SgoiYwF72II-V5MLfBb3XtTqilgnYjlGIjOYr4JypNevEIv1LFq7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پاسخ به حمله مستقیم جمهوری اسلامی  ۴ روز بعد اسرائیل حمله‌ای بسیار دقیق و هدفمند به ایران انجام داد.  گران‌بها‌ترین و مهم‌ترین سلاح دفاعی جمهوری اسلامی رو یعنی سامانه پدافند موشکی  اس ۳۰۰ رو که جمهوری اسلامی پس از حدود  ۲۰ سال تلاش و کشمکش از روسیه خریده…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5487" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/163555b294.mp4?token=pNOly9FftiyiMErzRvv-0YS48amGNg9m7Lqk02rD3hKGKyVrBF6c6wgBTVL0BbkIyiHzo3tjmPzXn3zNwsv9rBS3qPYOIlxN59fI0BV20A2HUiGcDsPmVh4EahtlwzQYBvW8u5PjcyEdYcUkuIN7Bmwq6Za9Gqo8Fpg5uqrkbNgzp7u_XEzDuzaAi3VpRhNzVWbuXznXLUUmylXWLmhBaUOdUm9TrgqmE7sHfjxIxQRjLnMsilSf7lo5QFyy2BZ1RtFmS3oL4rWhenAxThUpkS9M3P36YVSqzER12M8899ikiL_jHDSXON-6FeCVXf8yDVEWVPJgiMT1KVUcAbZNGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/163555b294.mp4?token=pNOly9FftiyiMErzRvv-0YS48amGNg9m7Lqk02rD3hKGKyVrBF6c6wgBTVL0BbkIyiHzo3tjmPzXn3zNwsv9rBS3qPYOIlxN59fI0BV20A2HUiGcDsPmVh4EahtlwzQYBvW8u5PjcyEdYcUkuIN7Bmwq6Za9Gqo8Fpg5uqrkbNgzp7u_XEzDuzaAi3VpRhNzVWbuXznXLUUmylXWLmhBaUOdUm9TrgqmE7sHfjxIxQRjLnMsilSf7lo5QFyy2BZ1RtFmS3oL4rWhenAxThUpkS9M3P36YVSqzER12M8899ikiL_jHDSXON-6FeCVXf8yDVEWVPJgiMT1KVUcAbZNGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی از ۲۵ فروردین ۱۴۰۳  رویارویی با اسرائیل را از جنگ نیابتی به یک جنگ مستقیم تبدیل کرد.  در عملیات «وعده صادق ۱» ج‌ا با ۱۷۰ پهپاد، ۱۲۰ موشک بالستیک  و ۳۰ موشک کروز به اسرائیل حمله کرد،  دستور حمله مستقیما از سوی علی خامنه‌ای صادر شد، و جالب اینکه…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5486" target="_blank">📅 10:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIDn1963KwdOGJbsLF2YPFkHhEOYd0Xgi_MLG6YWKUV-LV7JTD_7PPW3CNudANoufaPizpwOEK88pfVrRWJHAEDYY-NdYMuYsUjt9vK5axTH23wjFJmUbq4qw-si5TTAzelgOoKNCEyvJ9YZJQCNoTrnxINHg19Cdk6n4keu9-yrNG6Pb8VyMeMKMtbGTq7WzVeX16jXIvjIQeLCQ4lQSHj8oJXKv8oGWBjpOwMNhCL_e46S3a6q9LVM8-uS3oprXS8BDw4hX1puYHUj-wvBp2E_FpKJDn7Bh4dUIRds5KdncdKj5FWQyb0yOl6XHPxoG-mhgXq-YD8KQbhrFIKviw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ غیر مستقیم با اسرائیل سیاست  جمال عبدالناصر بود.  ناصر فشار سنگینی روی اردن و بعد لبنان آورد تا اجازه دهند، گروه‌های مسلح فلسطینی از مرزهای اردن و لبنان به اسرائیل حمله کنند.  اما مصر خودش چنین اجازه‌ای رو به فلسطینی‌ها نداد! نگذاشت مرزهاش با اسرائیل دچار…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5485" target="_blank">📅 10:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5484">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TaIw1P5RHYCF3ie29w0harGcfFG0bZVVfQxaHn2et-FsShLqcO4DT8BR2JhqU0_njJvXHyl1LqdlpgbGhQniagGq7OuaWnuEiC-G73dGA_gqOUpsJVQOLyf6gnq7aLd3Ak3NH9wYdzOi6dQpUQHIprg9vgSSPsF_jdJQLii1BSzPefysKVWu0KkxsdrNbj8J7eaWdKtRJWIiAEaugLD3Ic092m7M1NWy7DJFsWpzWZV5Ag2SvoI0kD5ZmPwB3lat8gMXOyYZR4UXAr6DXS3rwb9zWxr86U1FSxRmPjJfQsTpyADK2fbrku_A_5B1IxJDCa87ifNp_xnAaFv-MKwXPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی در ۲۵ فروردین ۱۴۰۳  برای اولین بار رویارویی با اسرائیل را از یک جنگ و نبرد ده‌ها ساله «نیابتی»  به یک جنگ مستقیم کشوند.  تا قبل از این تاریخ،  جمهوری اسلامی با مسلح کردن گروه‌های تروریستی مثل حماس، جنبش اسلامی، حزب‌الله، حوثی‌ها و….. با اسرائیل…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5484" target="_blank">📅 10:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZc1RhI-yCxgbi9Axe5Bxe-3ffULS1zn_OEglggwl_P9noDcK3l9eGl0zODdYcrT5ajeSnYv4Tah6Oq1_5Jf8VIjoZhdTOt0oPoHjjbC13sDGJb-DzWZ8KihFjclMEPzWrBEEb63ABrTysodFLTrWkGeuhpdXN5Q0kfEe93JPnbrWfjjZBZbEbqM4iW8ppuFn5K6_rfucBq1tHKGUujBLTtNwzJheP-wFknJ0YsAh0bUIpvdJswqh809-elLPBoIlnEyBDZYiyg4-ISiqFDfyHFavPriS-AZ6nk1jMZ4NwvQHRkf_XDEkeg5tXpAgqSZUzOo9JkPypGddyKwjMfA_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از مهم‌ترین پیش‌شرط‌های جمهوری اسلامی در دوره جنگ ۴۰ روزه این بود  که «جنگ باید کامل تموم بشه»  و آمریکا باید تعهد بده که دیگه به ایران حمله نکنه.  منظورش این بود که یک «آتش‌بس» نمیخوایم! «توقف کامل جنگ رو میخوایم»!  این‌ درخواست از اونجایی میاد  که جمهوری…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5483" target="_blank">📅 10:01 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
