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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 00:53:57</div>
<hr>

<div class="tg-post" id="msg-5588">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.
چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ سخت نیروهای مسلح مقتدر جمهوری اسلامی ایران باشد!</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farahmand_alipour/5588" target="_blank">📅 22:32 · 26 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/5587" target="_blank">📅 21:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5586">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgmlffjzE_qrw0K4fcb3LQ2iexas8EVdu0cykiuoK4Fy6L_MD8sZL-s_CTNJup1hheqtReGr-ZtUQdaH6BSDhOAqzSyHbLrkU-ifQRnNxZcf2M1FULmSmUS3Ai9YT9hEJObZx4gSJP10kRBTTRdSdYNz-cOHNOMaWYgFYuIJ-ma6lrEvxJsDEppERlOQSHXfux3C6cwwdgc1iMlHS_AxH0JhGsvoGGGPBDiOtsZ57LFJ4jHZG3JsrEwAF7S3_9fQfJFLZk2smlIaPORCNezHOhFJrg9Vc8vO14AyAlAnDHV2xLDVwmLEikTH2NsEpRbJU64XtwDF1Mt7fV8lFhsbkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده دقایقی پیش اسرائیل
به جنوب لبنان</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5586" target="_blank">📅 19:49 · 26 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5585" target="_blank">📅 17:03 · 26 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5584" target="_blank">📅 16:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5583">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامپ : تحریم‌ها لغو نخواهد شد!
بستگی به رفتارهای جمهوری اسلامی دارد
(اول صبر می‌کنیم ببینیم ج‌ا چی کار میکنه بعد در صورت نیاز، تحریمی رو برخواهیم داشت.)
ترامپ : صندوق ۳۰۰ میلیاردی سرمایه گذاری در ایران کار رسانه‌های فیک نیوز دمکراته پایه و اساس نداره! (البته این حرف رو خود ونس هم قبلا زده بود که الان ترامپ قاطعانه رد کرد.)</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5583" target="_blank">📅 10:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5582">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNTpIgWIVuzbRHoTGOwA9rElA9FQv7hvWUQVXbK-10dn9SS_0v71VrXTO4f60ZXKatjP2sXegayMEa5NlwI1GauZ_VBGdFQNS30uoKq15rcOKyYooV5tlldtESq0h3neVxCNLmqDq8PPJxQNsfEUqMh4yU2NI8-QRbzGfrrE2zmz6XpgUi2Qq65J0ZhDEj9pgmATvQA67utXwoYin10_W-cekLINiFMbsxYOXJf3b6hxWCOiCbVZjHprm0U7W7tumO5Gp1Cr3ImqtPnwYzjOjwepcmr6D1WXkFRSvZB6Jt52HjzmKUNHFqhLEntdnjKaeyXcgvJdIfB04R3bnQqIww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موساد و ارتش اسرائیل معمولا نتانیاهو را فردی معرفی می‌کنند  که بسیار پر سر و صداست، در حرف زدن جدی و قاطع است، اما در مرحله عمل، و تصمی‌گسری‌های بزرگ بسیار مردد است.  بنت اما متفاوت است او کمتر حرف می‌زند اما جسور و قاطع در امضای عملیات‌های پر ریسک و ضربه‌ها.…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5582" target="_blank">📅 10:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5581">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNmU520OyUOM_rUGL52o5V502SVZxiwXwbVtVswFYx07M6V9JLsPy9PvCLaQlq8p1Vuih4heDgmhog7ZgnjLJeAxR920bn28qdzJZa0XebH1IOYevKa3iNaBVXty7okhdxnoIzCtGr8NF6uJU8PE8_e9aYEOIjCEPXVJ6MGtsPo_VoMrXzKuKOfipkgKCraA9SGhkFGJ5GZowioxf7HLQT_sH1-N4uEn_U1X6AQ_oncogHZxY1IAxInA_8o5PsSoqObOfPK2ZgxXUFzDW6UIgw8JN23jQdVU1dixPYnqKvWZI44r7fXm1iNzjxfY4_IRZcwBnNSJ-aNsybIbbOIKBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">او که از منتقدین سرسخت نتانیاهو در زمان جنگ ۴۰ روزه بود و به او انتقاد می‌کرد  که ضرباتش به اندازه کافی قدرتمند نیست،  و اینکه نتانیاهو زیاد از حد تحت تاثیر ترامپ است، دیشب در یک سخنرانی نیز گفت که راهبرد نتانیاهو موجب شده است که درگیری‌ها طولانی شوند.  او…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5581" target="_blank">📅 10:18 · 26 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5580" target="_blank">📅 10:12 · 26 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5579" target="_blank">📅 10:06 · 26 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5578" target="_blank">📅 10:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5577">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPaPvDSmTle2Cn_G65P6D7joL9eWY8uSmXyTKApGiMx6iKdVabWUynDucceHk9hmkcpBOjAUrJH12OETK415QigsHOtoya0tFg0OvEXz6R9ARyJdzHkOAsBz7-9a5nvJhB1TwaoJ81oKTO34csYloluMiiYMhY-4TUyACRyUH8QyTr6VZmpORy3gPsD92DUQPf2j4tEaOb9BULarmsh2mJlTpeGrAOaABjvfQM4Yz_oupmJ9GvYohyCm068tMaGHUU2YQ-bkYXL73eJd84kmMxKaKfR8BFn0rjxlJ8sI29STuepOQB2ZB2gQtkIfo_CP3rjrdGdvyJlBLTbyio4Muw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اول هسته‌ای، بعد موشکی …
‏به مزدورهاشون که هر شب جمع میشدن، گفتن که چی امضا کردن؟</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5577" target="_blank">📅 09:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5575">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n7qhNLJwMGDM-12nsesYY_c-HiAUzQrGQRvKgp6BGsyrqXOc1bNoMu54tr8abDjZEMlMLljxBep9GtZMH3PH9F5BPSI2eMR61o-64qgC0_ihLybK4SlrpwCGlrMKvS0eDubwNmHGbiqry82M5lYBVl4PGNjA6Eml6MAHt2fbf1_6pQjyOrPVCqJT6woHGoQHURnzKuIF28FCJewzzwNeP0k-iAiB9O3elQcFY9KcQ0eGHtdocHCwswDkNlG8KIwhoGtGYHYuyz5wXi-F4UNAhSVpTWw4lwDScEbGIKtIeRPavWtvPBl3_D9hFjUFzbRDVyIvmSvcYnEYh47FjMBzFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dcXLR2WbeYqRCJYaZ2GzY2xvXLjXXSRf6xwNKCAw4-Bz0fVA9olh8xz9KmEK8ikcoUxG75voMhu3jqkCkCL2deXk-uOXWGBbGfNy1nEAlyucctGcgic7KT6apkoNi2DuiDgCtCTFxFBs80hzgHh4NhFEtyoRCMLK5tUFm1h6RNzwKR6yGq87EHWN60a0CxI0jN1qmQJmzixZ7XbCF7JI2axxIJ2w7eiLMEtDGzotkS8P4jD0FgLrY2i3bHEJhBFNVIGCCq434hDr18daE_P93-Xe2U7pjjAsOYJMpVSjufBVTFnlWeSfOoF8G_M6JDjJU1GE1-iS26z-Wk-SlK9zXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسین شنبه زاده فقط و فقط یک نقطه گذاشت!
نقطه او ۱۷ هزار لایک گرفت، دست خامنه‌ای ۷هزار لایک! رفتن گرفتنش و بیش از هزار روزه زندانیه!  چون فقط با یک نقطه دیکتاتور رو در هم کوبید!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5575" target="_blank">📅 09:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5574">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXPNd-sjAK6k0FHjbEUDhvF1E6vdscgOFSJbeTN7yZuVUV-0KxyLKq1qOWkqexFwk-8uukZVbXrW0-m4ElApBznnLTNFTngMxO9ex6FVcg_BKQA9A2zK6H6strq0Zk6o9YPvJCvirBtcT0JN72ga7DTwgPg_h1ISOFoMT4zCdLxKtgAxdXL4UiSMX2cSR203d58Wh7FWlv2HtK7FchT2zQhM-kwO79Tx584swtoTWVuj-SbeDb2nA3DMuYal3WLb02tojAHUNIic672lJ7gG7sFp4b_ij0_WzZc4wkClfJzFdGu-UYfgg3NwGDDnCvu5duseOthqSl2SpURMVVAGqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنیده شدن صدای سه انفجار در قشم و تنگه هرمز</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5574" target="_blank">📅 01:14 · 26 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5573" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5571" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5569" target="_blank">📅 22:40 · 25 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5568" target="_blank">📅 13:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5566">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AhCkvDn0thqk780x_N75I5lYkZ1qChYdTT3kpFAkL6orzbA2eqzLKrUK_dlY_98q2CeuCPXEourj1i9icBmbITAs9EcqTv3gsulUrSUBN-bpGRhYAkB33FQK01d97IUEQ01QgUPMvcgVOerRAuQ2HO_jUVTc16I6S0O5EzTgD84XRrpuuLS-nEC-zzis7VG1R1uSdQ0xrTbf_2ZyUs3Q5NvZABOPcPHTSclpaxuWB_wIF-En0ytTuQfIZ_y0Sv3qPkYMu-rPtUgGWEjrRx6lBuXn6_dco-DyBibR0akaFvH9dDR5TLtDi9jDk98g83Gcg2s__IndzjsKm07xNJ23Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pe771ReYIdekS6CAaRmbOsu3NXflO0TABJht_uao_QKzXmH22j4G24dAepXGK3at3_uRgeYwDD1GWQQGfmtxfRv9bVeYn-c6We3yUbT88OYm_HvDM_3tPe2eA5L3iL9ne-YtZILI2tF02-OE-riq_UkT9Tbffv3cXe4dxFozLyU9sDeapqFcRXM8MNNIkpAG6VHBQnBfQGXkQWjUnnBBe3UjYNMkGL-yInWxAdEQLOvLygHfUyPZT4WgtYLy4rIookXR2IZZKNGzLo3cGBB0BjUZYD_uDQHsDyJOjh2ZNWsEyGhrO6pc-iz-FnJG6W7a0ER-4YzGJd_35up5VQ-EIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5566" target="_blank">📅 12:00 · 25 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5564" target="_blank">📅 10:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5563">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">رسانه‌های جمهوری اسلامی،  حتی بیانیه شورای عالی امنیت ملی،  تفاهم ۶۰ روزه (که هنوز هم امضا نشده  و ۴ روز دیگه احتمالا امضا بشه) رو  «توافق» «پایان جنگ» معرفی و القا می‌کنند.  در حالی که چنین نیست.  یک تفاهم نامه است برای یک دوره ۶۰ روزه که طرفین اقداماتی رو…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5563" target="_blank">📅 10:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5562">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،  ۲ نکته رو به عنوان دستاورد مهم توافق پایان جنگ با آمریکا معرفی میکنه : ۱- پایان جنگ در لبنان ۲- پایان محاصره دریایی.  ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!  چون رسانه‌های غربی چنین موضوعی…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5562" target="_blank">📅 10:32 · 25 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5557" target="_blank">📅 23:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5556">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5556" target="_blank">📅 23:02 · 24 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5548" target="_blank">📅 19:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5547">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UWhJqWQX-Ww8USbSTO3-GpzEn6sssVZIEgkJo71aSSPhmw9om_8t0AI9-zU-Pl2RNW8Aoxo-98-Td50GQZ6cS5irOGcqC15LBN9PNgg0kvAKRcfAN63Kn31gwcDaczW95OmCi437P2I1eOF_N-fJPa_DNGGf45Rsnv4WurkBc6gdxksvrdvJa-MjbL9fT9EqvbN_2bEUjGfl2xOSj2gqvltMA6cwZLiovZsvPoFNNWOuzrY0zwNTn0wcDewSMOn5DTfec0mL6LWRUCsfiQJqlkck6vi1Vm7QB69GZWkHGtOc7sGGIK3crDLzCT6Zy0e4DK0a9ZyjVeyB8EN3IPeyEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hthkip3nlzPew-wKUG4F0nrF6p6n_DHC4OTuWHx4TdXv5uvF1N5i71zZVzvix-tjA7GGZ2wXZSKHMtCg4JPP2EKsS5_H4NkMSRN5mM7HMYq-qBYdoRmZkKVLfPhUvsgKhHf-4GgQrEu5LTDQgbkaLAbnZQQz-TKoTjT2tQSX87chcJtGPKMhLoQXJo6V-vbVOC8_jvJzaC097SdwcjVT0ghG0mq0PF-8Co3ZE4zZFBLZLHIoJeQFXn6yAN39hIFdvAB7iuiUXA40fETvkKE3R3kmF0fcA2saqJtJUsynPcdabCF1_i3rLOBJCkHfaV_8NfDvCQXLOhIzFJp05J2UJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسرائیل در حالت آماده‌باش کامل،
در پی افزایش تنش میان اسرائیل و حزب‌الله و تهدید جمهوری اسلامی، سخنگوی ارتش اسرائیل از اعلام آماده‌باش ارتش اسرائیل برای پاسخگویی با حملات احتمالی ج‌ا خبر داد.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5543" target="_blank">📅 17:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5542">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=m_rSI5bhne5DSuRZmLoyLUS8aeaKnjnJn_UR7-jeqfQ5JQP_3tDP7-5OGWqmvBzePWHT8T-vgexzYc9whGFYkk-ateMa4BKOpKRN6heP5utjLXv1sexqweeWcTREX26LzdMcy0PzQ1TXa6SwfJyIdRhfxqwZbilMdZIQaqSOPjnWoRl87uYcpUOJDrSxFjAPGQlUBFmoUtCDGbIYb7wSqv1dXxEzQ2iSA1tAe1ogsxSRBG7Dmeyfwee948aAN56h5pv9CdMR8l-D0QBryvUmYZnABars6ShOErnzTsgOfGy6XX1eROoKxQ88U4K9EQDpOlLx_2OtoPaKRQG4DmLtWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=m_rSI5bhne5DSuRZmLoyLUS8aeaKnjnJn_UR7-jeqfQ5JQP_3tDP7-5OGWqmvBzePWHT8T-vgexzYc9whGFYkk-ateMa4BKOpKRN6heP5utjLXv1sexqweeWcTREX26LzdMcy0PzQ1TXa6SwfJyIdRhfxqwZbilMdZIQaqSOPjnWoRl87uYcpUOJDrSxFjAPGQlUBFmoUtCDGbIYb7wSqv1dXxEzQ2iSA1tAe1ogsxSRBG7Dmeyfwee948aAN56h5pv9CdMR8l-D0QBryvUmYZnABars6ShOErnzTsgOfGy6XX1eROoKxQ88U4K9EQDpOlLx_2OtoPaKRQG4DmLtWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=BxaRK9lj82WdDTACuBXOC1jj741Pu9Gs-2bawgIdos1DqAgnLT86qa9AwtyCCiAZmctQqsgMG3NcpEDCW7Vorq0O3H6MJkYcV9ZJ4LGDvo3oS20yWPsGHJ1SfkxF2GLrhT_FnBG2vf1g6Xk6oQnChmyofBB6OuYJHcAvj1w-xV8eFlNWVA6esXJGdtr1b1C4CR1WXp4L9YKYTohaEcNc9ABtW49xMxzzhyWnqVb9QtA7mHIpCybhn5MExag-DjYI-6BX2JRh5_wlfd6TSxWKBFENr6YAbuLWPgwxRzlVf9ZsvaIpg3MhFh0ob083UbPwcbKtAZT0XKrZFVEbNikTQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=BxaRK9lj82WdDTACuBXOC1jj741Pu9Gs-2bawgIdos1DqAgnLT86qa9AwtyCCiAZmctQqsgMG3NcpEDCW7Vorq0O3H6MJkYcV9ZJ4LGDvo3oS20yWPsGHJ1SfkxF2GLrhT_FnBG2vf1g6Xk6oQnChmyofBB6OuYJHcAvj1w-xV8eFlNWVA6esXJGdtr1b1C4CR1WXp4L9YKYTohaEcNc9ABtW49xMxzzhyWnqVb9QtA7mHIpCybhn5MExag-DjYI-6BX2JRh5_wlfd6TSxWKBFENr6YAbuLWPgwxRzlVf9ZsvaIpg3MhFh0ob083UbPwcbKtAZT0XKrZFVEbNikTQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=bLHemckaKpWbi5BVC1J-GO7aevGUwwGeLWVu6-Dh_5f-1mV6TfawhJ4FjMVFuGBvTEi_yFvYaZzfi7bXADUMY3DVhdZ5Ut8X9L0rAbSw-Lpehuh_HXlvJEvt1aNPfBpuglfNPDV00R7Q-SuHyFpCxny3ruqwVK3gqjO8RMUT07pEySZU_CU-W9puXjYwkBadHvQk0pzW5uJ4jNc2hEMaPbLwpISXDokOz0UDuFIzTQzVckaE7JDlGOKQlSeZ_fF7qP0EuwauOdgAuYu1vykMx8oF8D3gzC4YYiAnfe3UJZOm9O8KcuJD_4Grm9238zGzZANio7Ga6fX5x5m7T3Yzyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=bLHemckaKpWbi5BVC1J-GO7aevGUwwGeLWVu6-Dh_5f-1mV6TfawhJ4FjMVFuGBvTEi_yFvYaZzfi7bXADUMY3DVhdZ5Ut8X9L0rAbSw-Lpehuh_HXlvJEvt1aNPfBpuglfNPDV00R7Q-SuHyFpCxny3ruqwVK3gqjO8RMUT07pEySZU_CU-W9puXjYwkBadHvQk0pzW5uJ4jNc2hEMaPbLwpISXDokOz0UDuFIzTQzVckaE7JDlGOKQlSeZ_fF7qP0EuwauOdgAuYu1vykMx8oF8D3gzC4YYiAnfe3UJZOm9O8KcuJD_4Grm9238zGzZANio7Ga6fX5x5m7T3Yzyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله اسرائیل به ضاحیه بیروت
حمله اسرائیل پس از حمله حزب الله
با دو پهپاد به اسرائیل صورت گرفت.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5540" target="_blank">📅 17:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5539">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=MWLsCqoCRGuM6fYmfWEhjIMjYNkJ0l2PgrDOvVPeKe_um25Yt-P5XJJ1HyaupMJK37sZfSOWFmzUQ5Rvnu8rsbyFdbNYi0Sjt3uqmDUk6qUGUm0T4o5f9Loe8KpVzPb590zYT-BQmSdZzViUtQhH_2BXabQ_9eahXqe0LI6JNHsb8SnsuvjVYZwZ83wpZedGUMKJqH-4gsAoc95lUNRz9Hf1suLZmdTlB4_BFio9qrNDdc-lG8vkYt4DtAggj3IUcwMrMSa1gwNzpXxwgDoPtIVjQ9_RSvzT7c8cNZ0UVEa9BVJo3_zDnu5DNeMLnX4ACtd4GJaJNWFtKE853z6oNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=MWLsCqoCRGuM6fYmfWEhjIMjYNkJ0l2PgrDOvVPeKe_um25Yt-P5XJJ1HyaupMJK37sZfSOWFmzUQ5Rvnu8rsbyFdbNYi0Sjt3uqmDUk6qUGUm0T4o5f9Loe8KpVzPb590zYT-BQmSdZzViUtQhH_2BXabQ_9eahXqe0LI6JNHsb8SnsuvjVYZwZ83wpZedGUMKJqH-4gsAoc95lUNRz9Hf1suLZmdTlB4_BFio9qrNDdc-lG8vkYt4DtAggj3IUcwMrMSa1gwNzpXxwgDoPtIVjQ9_RSvzT7c8cNZ0UVEa9BVJo3_zDnu5DNeMLnX4ACtd4GJaJNWFtKE853z6oNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=ItqfZIZ_VJil7L-itsKWaefujCVRAuFWqfR0A7SAlUO4GgTZaguMwsnKy7YP8RIPFxoan5L2olxkS5b0VeD_O2o9bdv787aeZzbJnup-mZYKXMLTcFpIyCzWjDSKanHNWHYlNz-8Nmj8kO4xaphBi4PNzCbcZ2e-7k9T1589itHDRzqUrX7lcvm8vn2nOK_gUSCvlNZy0AYEpW27wn0n55vaqOcza3d-1AgH0uxEywhJuh3M0qcPEDE8DXtp0YTQBrZIs1S6-k9nYrisBnPz7M4EM1E34zCVaHy5oqs9_gBUq5poyBR6JcxoYzbTsi3e80bpqzDuFqL7jbsHGVgX9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=ItqfZIZ_VJil7L-itsKWaefujCVRAuFWqfR0A7SAlUO4GgTZaguMwsnKy7YP8RIPFxoan5L2olxkS5b0VeD_O2o9bdv787aeZzbJnup-mZYKXMLTcFpIyCzWjDSKanHNWHYlNz-8Nmj8kO4xaphBi4PNzCbcZ2e-7k9T1589itHDRzqUrX7lcvm8vn2nOK_gUSCvlNZy0AYEpW27wn0n55vaqOcza3d-1AgH0uxEywhJuh3M0qcPEDE8DXtp0YTQBrZIs1S6-k9nYrisBnPz7M4EM1E34zCVaHy5oqs9_gBUq5poyBR6JcxoYzbTsi3e80bpqzDuFqL7jbsHGVgX9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زنان کفن‌پوش ولایی در برابر وزارت خارجه و سر دادن شعار : مرگ بر عراقچی بی‌شرف نفوذی</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/5537" target="_blank">📅 22:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5536">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8679568b89.mp4?token=R3ae_syo6PLn44sLlj8kNOTjVulCh11QktaVRU8-o9X554ZdIg9Sp3Mr9P9yHBJpxVT8dPg9_Si9AxBxHagPtenziMtJyQaVx3nxCWxDbj3mmmCtk18rj6YkCKi18UrC-pxgKDlRWZPBXwsSSJ6JxotSxY9hfXxjgxnM8xRbCJo3DObMrt-oyPm-GHqBzMzCFPKz6E8Q8BXcXkFAjbCf4gupBcNMaweC7iRESbIKEa8PPxfD783tJm6t2o1mjEJP0MTvCH6exLYsrFLcLSCtz22fct0y34VZW67PAuawGOHODTJye2z2xRjtkfHh9ak_ikOF2X3nfLVXqpHhjV2RVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8679568b89.mp4?token=R3ae_syo6PLn44sLlj8kNOTjVulCh11QktaVRU8-o9X554ZdIg9Sp3Mr9P9yHBJpxVT8dPg9_Si9AxBxHagPtenziMtJyQaVx3nxCWxDbj3mmmCtk18rj6YkCKi18UrC-pxgKDlRWZPBXwsSSJ6JxotSxY9hfXxjgxnM8xRbCJo3DObMrt-oyPm-GHqBzMzCFPKz6E8Q8BXcXkFAjbCf4gupBcNMaweC7iRESbIKEa8PPxfD783tJm6t2o1mjEJP0MTvCH6exLYsrFLcLSCtz22fct0y34VZW67PAuawGOHODTJye2z2xRjtkfHh9ak_ikOF2X3nfLVXqpHhjV2RVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=HR9Ra1AMngIxOTv4nFCZwvQbZhGPLGyipP7yMXfYqM_t-FEZE152kRG58XZFuUzViEIW8Pe3PNAEX4pm-hHBdVCMgqeHVLVYA-NdZkar7rjR6mZzG3p14vKd1gVDJAoX191GMgftge47z7W1CjXzf5c86pO9gkdovJAFKmkSBXid0Eyt4cAbGstBBRPzAwlK5P06cMoQgZz-Z4Tgsbl6HhzF0Zx-xgHc3eVJq1CPTUt1KDA-qZLm79-9jk6DI_3ZDLVgV-q4-UkAKz2-qt8P5s85tofd6AUQpT2X8k6ohSMRvo3pC1qemVmXg4JbqA-aL_xaV1LLindKp9CWyTIO9wXpjfymMuVNcoyhp0yB5gEiwI4YQWG50Gmq8SAOHC1RfJFmd5U5Uu_dSSWArBTL-yXoe4Sj1yZr5wF0oyTYzWUtWl8Qic44cLtfGyqpAhLrCr_Zdgn0H-lNJ8bfdkPXAsxGRQ3JzPR-nGKjX-CQw0wuGc0cnX8iICnWxOoj90gaBFRvpIhUguPG_CSVPvM6k--5Os8g5yiLhrxTKR-EgBP_mVE-VJoueNmQUgGpjTubqwVbjT0OpCTo2UH0YQGNWAVxLlkGk1Kt7h_2rRfAJWgLDBEZArdWwbslxUc51jibzdbejGR0eNVbZ4X1xjlluokKSK2tPveoD_WoCgjRwGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=HR9Ra1AMngIxOTv4nFCZwvQbZhGPLGyipP7yMXfYqM_t-FEZE152kRG58XZFuUzViEIW8Pe3PNAEX4pm-hHBdVCMgqeHVLVYA-NdZkar7rjR6mZzG3p14vKd1gVDJAoX191GMgftge47z7W1CjXzf5c86pO9gkdovJAFKmkSBXid0Eyt4cAbGstBBRPzAwlK5P06cMoQgZz-Z4Tgsbl6HhzF0Zx-xgHc3eVJq1CPTUt1KDA-qZLm79-9jk6DI_3ZDLVgV-q4-UkAKz2-qt8P5s85tofd6AUQpT2X8k6ohSMRvo3pC1qemVmXg4JbqA-aL_xaV1LLindKp9CWyTIO9wXpjfymMuVNcoyhp0yB5gEiwI4YQWG50Gmq8SAOHC1RfJFmd5U5Uu_dSSWArBTL-yXoe4Sj1yZr5wF0oyTYzWUtWl8Qic44cLtfGyqpAhLrCr_Zdgn0H-lNJ8bfdkPXAsxGRQ3JzPR-nGKjX-CQw0wuGc0cnX8iICnWxOoj90gaBFRvpIhUguPG_CSVPvM6k--5Os8g5yiLhrxTKR-EgBP_mVE-VJoueNmQUgGpjTubqwVbjT0OpCTo2UH0YQGNWAVxLlkGk1Kt7h_2rRfAJWgLDBEZArdWwbslxUc51jibzdbejGR0eNVbZ4X1xjlluokKSK2tPveoD_WoCgjRwGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توضیحات نبویان در خصوص وضعیت تنگه هرمز در تفاهم‌نامه
- به محض امضای تفاهم نامه، تنگه باید فورا باز شود، بدون حاکمیت ج‌ا، گرفتن دوباره تنگه و اعمال حاکمیت بر آن تقریبا غیرممکن می‌شود.
- هر بار که متن تفاهم عوض شد ج‌ا عقب‌نشینی کرد</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5535" target="_blank">📅 21:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5534">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WUKRu4GO2I94LaATl0C10LXa1SYdv-hlB3IYBkOuSeCq-bSHZGj7Qm4AOVPMGHxkZjjofpCWiZWMoaghlg2kaBkB7JhA_f7KGDwXzpYTFdhx8ga7eyakJrMJJfhvAXO6rkBfle4hks0uLDFoZltInaCdpmgdDvj2dl9vk-hFcjWkHAXGiXKQMMU7deS6QF2JwjKHcHTSfyyJyKXTQtI6KxAtGmH2dXgOK4vFuqbK04ZzGYu_Gy7eqGc7bXxQPiqkTwBPmiSV9U7xbwmgBg1J6iej68fhMCNn40KTAoCBPvSxO6RYKa4XMOAsu_wja3GojH5kX4rpW8xWBUGueb7_RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: اصرار ترامپ
بر امضای تفاهم‌نامه در حالی است که مقامات ج‌ا  صراحتا گفتن  تفاهم نامه هنوز نهایی نشده</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5534" target="_blank">📅 21:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5533">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=IQBI_yFeF8M8AFGfSuYmMnWNrwyN0v2mnBVQ9dLZNzvhqYV9UfufJRleOYbe4cIUJBfTyYxfh-9-88tAffUtaoqboKQiizAwA2yAmWqvIkXw5Zm2BBTEJpWaAXe-zhVSWeMz-P_dU90mP2oAuXp7y94h8du-ahpKUjP5J7PY_lnGbWHvAhzxuhFYCsW8Xv3WIGHaT792UXF8-3k_ni5YXRHflm9G5iFxPE7Sm-4dVBudJo1kYUZhAMBd8Xm9WQ8N0vkfVCK5CINVeAgrvaAqLyT_JFJ2b5nXZe8lJGS-cvLEfvkMA983ryoejLCMhNpKIMrlnVmwTAY6-4_wx5fHyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=IQBI_yFeF8M8AFGfSuYmMnWNrwyN0v2mnBVQ9dLZNzvhqYV9UfufJRleOYbe4cIUJBfTyYxfh-9-88tAffUtaoqboKQiizAwA2yAmWqvIkXw5Zm2BBTEJpWaAXe-zhVSWeMz-P_dU90mP2oAuXp7y94h8du-ahpKUjP5J7PY_lnGbWHvAhzxuhFYCsW8Xv3WIGHaT792UXF8-3k_ni5YXRHflm9G5iFxPE7Sm-4dVBudJo1kYUZhAMBd8Xm9WQ8N0vkfVCK5CINVeAgrvaAqLyT_JFJ2b5nXZe8lJGS-cvLEfvkMA983ryoejLCMhNpKIMrlnVmwTAY6-4_wx5fHyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۹ ماه پیش
بعد از جنگ ۱۲ روزه و قبل از جنگ ۴۰ روزه
این تهدید پذیری اگه به وجود آمد پایان نخواهد داشت.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5533" target="_blank">📅 20:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5532">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZmB2aZ7MZKcP63pO9hPxNyB5AF7IuUlfLTIh6ZeVyqIDRarPb3irStnBkBu6dCWPoiRtVvFibXM2vcEhmX4NaOxRjYZUO63sogl8ctt866HCjQz3B0iVao-Vmq7HYUAQcu7YO9246lsmCga0OqLDJy4B1-B8519OZL80sHBBKTyIVL-1inKOQ_AHiRCKhnoLV6rOwNFDm657UeKz6ngMgk-QQyIE7xUSBt0zD4vxxSIxwTY3FEODD2LdBWUhKOkbD-K2Rkebki0yocR0-CFaTbZObcGwOHW6phhPsfKqwVDBlMZdihnSaQPYHX9bzc5n0FicqRMiybAGpaHRD_Skyg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzX9wf5t_RG4TbK1flWMyRFqaOdY_E_owensz0ncVgcjAGYv13NnepK8tBQnkvbc3-6lUfgdbFDvebEYfiEn9VtDXYKVs8d3PnfpSw9BxfFfs2AZC8x8AbgxISwxl0iilp3F4mQIbjx9TjQECpo1ulm3rQjg4oxgCIRRvw0tBvgXRbJdVDsY1kDalV7CShuGR1uvPC8gL7lxx9fh7ydvGoEji0c6QJdvO5NMOcOoeesHq61Ya3ViN5Z8RHDxovOUDo_osXzWuCzL1WMINLKtoyZ0vSzyguUnXBV644bii-ZoOrp7wRlB95nMpqVC8D6llR9AY0UdWHg1ZVKkpOmFWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیسی خطاب به قالیباف نوشته.
نگذارید خط تسلیم و سازش با
قاتلان خامنه‌ای به ثمر برسد.
(نه سازش نه تسلیم - نبرد با آمریکا!)</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5531" target="_blank">📅 20:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5530">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-xUdg9PMyBKCKQlqNyeB6ue4GVw_fl1_pf5avKQrdDzFGukFB41GTftUXwv80V0n-vOp66ZeHYuMCZi6LExYbJfvUStvIX1Z7BR2oaCzojn5jKvGJ0-Cjc5zL_w0ZnxRXQDJYG7Jt5pPrEIaaQ4lZ6f3PpIrSVxqJhbsQB5aItFqrD8FcLq82jZOD46PHM3SNxO4qwIKwIFtGje7VH357OL5CW8WmVvuAJ-sRV12N9ntTGg7TSRtn41ZI3m9IX73irrgSEXgzwcFaLPMzvtLmE5ggZ-BNnCCEsYC5bkP4x1EH8RwDuQERT4Jjm35WwGbjX6ENMD6w5vEZnVTMFnxg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5529" target="_blank">📅 17:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5528">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=tChKCjwR5K1lVMe8vk9LbsQ2ujx1envwHpE73mURI1fnOYf_Ncx4cbEWXCgqNj-7bgVRRbBlPweU2VRWy-qME6DPcK8HpinQ7H_ozltQVVNWY0X1breaKiMvm8MwhzfGOh-DT8RmR6A_tsFBXjHKjZxRod8POclEAVf2NAYvqrs58NMmnzodMnMhn5e_M2YvWBHGQynQHWGlbPAJ7p3xkEH7q_3e4njVh_Xhkm-rgOv0i-z3vJOTvupwP0h-tPOmRuIiwKpvNXKFtMg5BW95vE7ozWVLO03nZtQMIRnyiYObGp2jszWgMK4tRfS5tuwayt3blFtB02q14YBveUuZ5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=tChKCjwR5K1lVMe8vk9LbsQ2ujx1envwHpE73mURI1fnOYf_Ncx4cbEWXCgqNj-7bgVRRbBlPweU2VRWy-qME6DPcK8HpinQ7H_ozltQVVNWY0X1breaKiMvm8MwhzfGOh-DT8RmR6A_tsFBXjHKjZxRod8POclEAVf2NAYvqrs58NMmnzodMnMhn5e_M2YvWBHGQynQHWGlbPAJ7p3xkEH7q_3e4njVh_Xhkm-rgOv0i-z3vJOTvupwP0h-tPOmRuIiwKpvNXKFtMg5BW95vE7ozWVLO03nZtQMIRnyiYObGp2jszWgMK4tRfS5tuwayt3blFtB02q14YBveUuZ5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان مناطق اطراف نبطیه رو تخلیه کرد تا در مسیر ارتش اسرائیل نباشه.
این جنگ بین لبنان و اسرائیل نیست.
جنگ میان گروه تروریستی حزب الله لبنانه
که با پول و سلاح جمهوری اسلامی و به خاطر خامنه‌ای، جنگی رو راه انداخت.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5528" target="_blank">📅 15:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5527">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EDdqMLcBowZ8Lwt_5TE5un2RawKpLBK_hf2wW9sz5u4_03459nvEJ7u1vNYW_X6GVHVfDJ2Co6ow6MNNEvTYAn1QrXj5jWaaAabU2lblb8o72bNCow2cMxxzGInAkJXiLma393n1AoTrBOef9krXFsAFexytrPeW1S89VG43VXNwIX7Y7egsoztW3DmwFwur7Bj0pNVcNtJ_Q0RbPHtlZQ1OnJXJg6q0ZXvaKSpSPiIBat048VO-2dSIQHgSS97PguOcZ0qVOT9z1LiDV-rnUzslKJ9eyO-DRjSTsTrnCUJEYXs0sNDCx2iD93IawplHjH2dFH5GcAOt2FmremDOOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی در باز بشه می‌فهمید
مجتبی خامنه‌ای در واقع همون قالیبافه!
چیزی به اسم مجتبی وجود نداره!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5527" target="_blank">📅 15:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5526">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XlnziVA9YNPyyHP9XI2fkKDE-_Y9easTXFyYQWOX4bjH9JEG3fSFW-ZuDJwIfx6FoCdWfjbKY5xLi3mp8YX51_ahE6lWP6dhrdU9DsFtBRPkWqg-RNJwxWjELB1gkyBd2YIONYrUdkWJzkzblnSR6UUJp9eWnZnlGVOa2Y9AuCkKspMMeGbmYgBrovpXZOK1UNDNRvwZAJONkEREoI0bB23J5hXXCfK9CklWt6ZHtfI_xox2vYbljiwB05LpNFGZDwC-eg1RoLFrTlHnw0KtjkbW-EjR2rSnDur56Ukm47gAUogpKk8x0eiCh-d4_pSrA5uxmnlUFtxfQt4K9WMVlg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ka6j9LTFstHXuJRzyKqFdQmEnQ4o0QDvVeGkIsFGgmW1t2K-imKZQ3Xdgf2_1-2g2MDIB_AtfklEaR_ipJ9uWZlNcOvV60_hUzVxL3nhaGthxiyNcUoWUkO-rxCoaC-MClOzUIWloAv48ksyd22lvbCoQ84uipxeYAM9i1Mg0d0cy1Sww3e6JawDSZy_uDSh-1IG68yR5gmg_krbnG9kr6E7YtRtCB50eTIbC4LGDiefy-LVEGIjT6dymB64kBmrdarwXj0zD9ti2Syy5kUvcWGJJk2H-xihwLoAuF5inktipmEA0-MBT6c5Ms1FYoZHzHwo7yPHeWOZWyNcNmysXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات مراسم تدفین خامنه‌ای</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5525" target="_blank">📅 13:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5523">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owkGwbX152gPwN21Uv0I4f5-tju-MBwVSf23Zjv-2iXen5x2flwGKZi05Qi8XcXB6Xsss7mreKfyA09OFXALWvdK6SgyzsTUysfeIqOy3_azMC9A-1SMP6AaCbl9b87OCyGhMmfzhz-ylxwEAKKLTLKhpj_EXtUgfJAAl3txk6RyZnPuTM6H-cZ85q0LZyAMpXd8ed0DoOJDlgS0kn_nwV338o2Mr8vEclGrQeSS_SW-lMLP9SPyUjTEOJmnOo9HH-JLKJ9q49J8J_R4rupsnneltyN4XwGVKKTQ10zygrzKJ5ZmGesa0dq9BRzf0_JcjALd0Baf5LoZldGmtACKRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=VsvBQlTk1SIFUwRoV9n8H8ZP_7BMmPpdvg0vSEdKLFC_pS5GJ4Xh1LswZlAzHToLgNl_VQxfjMnCRSdkMsuk1L20O4KT2RESMPVyFbleoQMewzMlSqVBcQqH1o1FNudTET6AKEH0-DuVzbAjKUouPkPEHNmYfd14Yb5vEe5hBS4mKfBi7Zhrm2ydPlqrCeQ-8TmGtpnOvxdkXlXPBNYLYdThzLBLYh4G1S7ROzIjlCryVi8BKv2FLIjMMSWftuw1BDeaXa6vSTQ32A_pdwwwYqiaFMpSdyntYTNcLUWk8D6gHt73iyQiaSHDAyzmQmhgf3IRA9Dt7b8nQkrBe-M1Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=VsvBQlTk1SIFUwRoV9n8H8ZP_7BMmPpdvg0vSEdKLFC_pS5GJ4Xh1LswZlAzHToLgNl_VQxfjMnCRSdkMsuk1L20O4KT2RESMPVyFbleoQMewzMlSqVBcQqH1o1FNudTET6AKEH0-DuVzbAjKUouPkPEHNmYfd14Yb5vEe5hBS4mKfBi7Zhrm2ydPlqrCeQ-8TmGtpnOvxdkXlXPBNYLYdThzLBLYh4G1S7ROzIjlCryVi8BKv2FLIjMMSWftuw1BDeaXa6vSTQ32A_pdwwwYqiaFMpSdyntYTNcLUWk8D6gHt73iyQiaSHDAyzmQmhgf3IRA9Dt7b8nQkrBe-M1Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5522" target="_blank">📅 11:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5521">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VABzEtQBdWJWtWnY75iEefr2ET4EFjZPjvm8IGMG0yBarur1iZ8IqWFVVU8VGUZabyn7XQAx6FfR_v-FqXCyd6yAjBra9c6IPURf19KDykVzmr-iBdHFUsBBgVAme_uUPZTeFYut8P5gUGhnCauIopgtMU5Mikqw1Ka_ws_a9RkSHBrUYVZbaAmx2YDWjn8VZLGYlfu_HbW9Gm4_Qf-Z0lSkgq4plwyNTd4aZ-23D_l_NUExrQlMLZ12NJNcTFGu_bg5729e88zUnmkJ6n2-GKp0FiAIKG5ezqQEYYOa_nWMLUuh4FlLkcUMHZ27yehb4EFCEGeTHipfbYtcXLoCLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5521" target="_blank">📅 09:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5520">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PX0vCRGmcbTLWo5twvMxbRJ0d9B172NtVRdurIOMsLtw-K7cUIVz_5er0VxBXTp3Z8yVluFfZb_9rMsCCayJnnYXOkEVveWxYm_pkV4Eqwyl3h9sEPLOHrKNjfRkfSXXyMlMY2y7Uwg-zJXEJ9td_wAjjOazmDXcyeP24OOOHQHPjRlkTOYT3kOAYOnA6jSOhNuCQaY3VrBmIgHI03LEFaecjrKZhY6qRyV_V7mP6h37IAyqhAHMpFz8M4FO-tRGyXi5G7LVItncVxRbJBG8MDOwjxQWEp_N3iqrK98vvGCPcrmz-7QZ_P0mCoYOTR8kZi_O2zvnZsbw2l1RsqdZQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5520" target="_blank">📅 01:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5519">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=hJsa1LQhIE29yEgL4SziNkx8n_n0w1hHWXDpRNkvXarPcmrBcCeGr0m85zt_-gnENY0ny5nl-OfOUPiRjSd6gW1SACnliI9OTiL3mFIYhq_jrZ8W6sJT9DSl-fOJuibUM6EtTTh91s3RDogY7oyIjMnGg1NN3EkFwRyK1oVlIo-Pli7fkipst3DrfsBwr-BQ9QVbpEnI9rhDn2CcgjZDcFfIBUxx48sJr308eT4M8ShGSy_ozXN0l-I9bJHgVbfLN5ShMN9rzUPjFcA9eiflptUGu6WRl4hu-wDH3_LtHRxxMdWO4HmY5rT5v7xs_tfv_9-Nn3d7rd9Jze7U4kjT_SonfeB6EbSshMjrU45T_FBPrrQ-rfCj62J_qfHEMeM9ptCc0QXhBO08kfa8SEMoWrYAgK-yI6HKyGd3yNTsF8Rb0stKDOFrfUD4lOPpK1O7vexXXdUyEPRUpfH1YpOYGLLRl0v44Ic7O8x92d8RWMUXqaE1HiNrtqyajrFNVa9pec04hIVid16zwjntjOgMCsG2Hr-bfXAEqEoKH_pVGn2aBgUA5_tL4SF42oAVW3cUF6LlfF8A1lQnHBlyM8563dTL_-elaEw_9MM1eyDPmKl_yQugmuvWgRNhr7zB1OoP6bnpc36-PlLYgrwmzWA6oxpD2lU8a2Xap4Bk3mbj3Ic" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=hJsa1LQhIE29yEgL4SziNkx8n_n0w1hHWXDpRNkvXarPcmrBcCeGr0m85zt_-gnENY0ny5nl-OfOUPiRjSd6gW1SACnliI9OTiL3mFIYhq_jrZ8W6sJT9DSl-fOJuibUM6EtTTh91s3RDogY7oyIjMnGg1NN3EkFwRyK1oVlIo-Pli7fkipst3DrfsBwr-BQ9QVbpEnI9rhDn2CcgjZDcFfIBUxx48sJr308eT4M8ShGSy_ozXN0l-I9bJHgVbfLN5ShMN9rzUPjFcA9eiflptUGu6WRl4hu-wDH3_LtHRxxMdWO4HmY5rT5v7xs_tfv_9-Nn3d7rd9Jze7U4kjT_SonfeB6EbSshMjrU45T_FBPrrQ-rfCj62J_qfHEMeM9ptCc0QXhBO08kfa8SEMoWrYAgK-yI6HKyGd3yNTsF8Rb0stKDOFrfUD4lOPpK1O7vexXXdUyEPRUpfH1YpOYGLLRl0v44Ic7O8x92d8RWMUXqaE1HiNrtqyajrFNVa9pec04hIVid16zwjntjOgMCsG2Hr-bfXAEqEoKH_pVGn2aBgUA5_tL4SF42oAVW3cUF6LlfF8A1lQnHBlyM8563dTL_-elaEw_9MM1eyDPmKl_yQugmuvWgRNhr7zB1OoP6bnpc36-PlLYgrwmzWA6oxpD2lU8a2Xap4Bk3mbj3Ic" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5519" target="_blank">📅 00:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=GpRb2ROWpAooOp6WEqHzmJQ_7y4AtIIKyL3KIyV8TTlX7Vwt_DUpWymnn6jd_S7obThG8xhd-xG6qkHg0NdVP4ZswIFNpiU7WQ6iFJzHN4xImefjVnMuw-Kiq0UCdtra2fJlGR186BHKKIaZEhXM5dRajUbX-e6gaSJQG2Yi_1n9XwIBenbO_TURW2DEHNebiGHCi4c-C3Pb8GFlIstlgj4wK7TthuSnQ1DzMtPnww7OSw26qJWOFoE3LUR6cJes0lgfRm51c2cl9sHcwdWT81e66YD9nUEFpmjxO4G_VCVqlAlDqtW4xTqvZUS8LTlcvgP1PvJY2s1ypFwruSu-Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=GpRb2ROWpAooOp6WEqHzmJQ_7y4AtIIKyL3KIyV8TTlX7Vwt_DUpWymnn6jd_S7obThG8xhd-xG6qkHg0NdVP4ZswIFNpiU7WQ6iFJzHN4xImefjVnMuw-Kiq0UCdtra2fJlGR186BHKKIaZEhXM5dRajUbX-e6gaSJQG2Yi_1n9XwIBenbO_TURW2DEHNebiGHCi4c-C3Pb8GFlIstlgj4wK7TthuSnQ1DzMtPnww7OSw26qJWOFoE3LUR6cJes0lgfRm51c2cl9sHcwdWT81e66YD9nUEFpmjxO4G_VCVqlAlDqtW4xTqvZUS8LTlcvgP1PvJY2s1ypFwruSu-Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DrsjzdgQAwQcSkDqhvAru05FVBkLXTHZhZiPq4Jzi7Zw37qEGEXRlrqbuVpq8NPVRwSv-uZ9eJRkVWt7QWR4MhttGxbCcqbDlDIHumvY-QZUx4tBeiyE90_KpHd16DJC_YsoT4IosEPHuZxGZytTBneWDr6FxuxzJcfTLH4eCgy6rWTXx5RPUE5iUwTGm6juaBlF3s7Hfih0vIils9vvhvQku1kcPmspBNf-qSiWhxMs1uCEK5iwKhAOKuy9MdzdZ8_3SoAz2x-w340VZ1U8Czu0IP16U2E6NrXxpuWqXRgDQ1y3-TRwLeHf10uuYC6qUITkJhR5d7QlHfluKIoUxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : این مواردی که جمهوری اسلامی منتشر کرده دروغه! اینها یه مشت آدم بی‌شرف هستند، اصلا نباید با اینها مذاکره‌ای بر پایه حسن نیت صورت بگیره.
حواسمون هست که دیشب هم با پهپاد
به یک کشتی هندی حمله کردند.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/5513" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=IO0lv1q0iNyCAowEJNB89seo-X_S0klNtBB7n37_MTsI2KZrCRnURFQ9qGjy73ZUS-VoSBhHC-mWBl4c4p5Car4KYdKqRu7rvzkHW9v6Z9RRD1tkwyultpL63NZMYUX6-SqbURhfXfrIn7oZmsnE5sc_0djnYRkYzGvpNOZiSferX1g903xPTNr-93sSI9Vfa_WveoR2X2UfHpgxbZrwYG5iMd6sUeKHk18NQB6gO6XIvIoKyM8eAzE8R6tlJvRzGf6n7dHVIsq1-6ZDY06cuCZkyvwSGbeRW0Q6NA54bvzmWKVt1pxK1qc7nUstiHGsWx-956JHkxBI_bnuobfDqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=IO0lv1q0iNyCAowEJNB89seo-X_S0klNtBB7n37_MTsI2KZrCRnURFQ9qGjy73ZUS-VoSBhHC-mWBl4c4p5Car4KYdKqRu7rvzkHW9v6Z9RRD1tkwyultpL63NZMYUX6-SqbURhfXfrIn7oZmsnE5sc_0djnYRkYzGvpNOZiSferX1g903xPTNr-93sSI9Vfa_WveoR2X2UfHpgxbZrwYG5iMd6sUeKHk18NQB6gO6XIvIoKyM8eAzE8R6tlJvRzGf6n7dHVIsq1-6ZDY06cuCZkyvwSGbeRW0Q6NA54bvzmWKVt1pxK1qc7nUstiHGsWx-956JHkxBI_bnuobfDqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K74AkspzNqMlqX82Zzqlh_HhvGYU9em_UrshvXhRn4CbzHkT2weoxBQEAHiJk9jGeDOwbpNTQAHDkHJagQEvegQzo6TIE0e2enapvg4MhUxglKcfpzIjCqeeI6b3BSHsw9yqwJEOg0yRQ-PfiY8XFa_ciLhmMMqVRxBd2qu51KtiG1myTXccZrekzoHwwYFRuVCz5DsG3pOjKOZXaK1tRpcgPdMAztMU7tRecwpVO6maiWmMWRf9CreuRAdqIXV1OMw5ptXk1sMSt502--KWp-xJYH_gE2leWCSfbESJt1rIrCSWcLzeIyHZrib6RuKRwhyg9kfyMf4ZCPTxO2k5dA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=F-jEaSrNYNvVtvbSktVoBTpMF6m5gPHvjCxi-9ADWAK0df_TVJy8BGXCSkHVY1fbkZsdVDgy3-8C_iC-5cpK3IdmG3_kxrgJKhh5RHxpOQQDOeRi_ZJMqMC_fmDb4W1izikd4AV40y2cKu2kvcvZ04PbhUhUIrYcRDm8HxkyoNSSuClEMI2PnMsxZenuB5TwWX4L--YtNRRfbxWDzkD06xmkAYIH2uAi38a_gfw408lqPnc6odh7NwxicCy6jC6m9t4PJXW5XH7htac4uGZlJmnKwCcBc8b2aoXG1Yv5iiEDXxkVtWlDe0NBox55Gs9hXxLOlWeXlGn7bB1Y0xDxDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=F-jEaSrNYNvVtvbSktVoBTpMF6m5gPHvjCxi-9ADWAK0df_TVJy8BGXCSkHVY1fbkZsdVDgy3-8C_iC-5cpK3IdmG3_kxrgJKhh5RHxpOQQDOeRi_ZJMqMC_fmDb4W1izikd4AV40y2cKu2kvcvZ04PbhUhUIrYcRDm8HxkyoNSSuClEMI2PnMsxZenuB5TwWX4L--YtNRRfbxWDzkD06xmkAYIH2uAi38a_gfw408lqPnc6odh7NwxicCy6jC6m9t4PJXW5XH7htac4uGZlJmnKwCcBc8b2aoXG1Yv5iiEDXxkVtWlDe0NBox55Gs9hXxLOlWeXlGn7bB1Y0xDxDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=UskznrclQq6W8OwQcCR3s3fh-ULGyNmWWESe1jWS-cb5TsEV_t3KWbuf4atJHgMIvXVfLMIN0cQOt4J8N8K-gDg3-peRE9_33c4n_iHcTsVO4byG1S4uzy0kZqzn0WWx0GAt_wL-enPbQvdspqcBiRnNNF5zPk3SFSLdAg5vzV1YUTUvS-G80logitAI9XnPvqsFeVDvvzGfFIFG3dFpWCOZgfNDkf5sFAUABlKbQrs1t01y0ONTyWBdujkS1TU49NnUSHiVVVAvySKtsELc3JzVJxuYB80UrdwEEkv_YwulOLfjGjHjTesUDO3CQiovqrV71CZP1AElbE8rpPV-Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=UskznrclQq6W8OwQcCR3s3fh-ULGyNmWWESe1jWS-cb5TsEV_t3KWbuf4atJHgMIvXVfLMIN0cQOt4J8N8K-gDg3-peRE9_33c4n_iHcTsVO4byG1S4uzy0kZqzn0WWx0GAt_wL-enPbQvdspqcBiRnNNF5zPk3SFSLdAg5vzV1YUTUvS-G80logitAI9XnPvqsFeVDvvzGfFIFG3dFpWCOZgfNDkf5sFAUABlKbQrs1t01y0ONTyWBdujkS1TU49NnUSHiVVVAvySKtsELc3JzVJxuYB80UrdwEEkv_YwulOLfjGjHjTesUDO3CQiovqrV71CZP1AElbE8rpPV-Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/5501" target="_blank">📅 21:08 · 21 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gf1pI7lQKW4iKYFLVeyjIxGesH5xvsJEVohFMpDG9VXOKgT0vNQipPNmAKatSQ6bL2i5BNRjTxmsN6r7VvkPmPjKwzcqlUC_zZSKNOY-uuEPpb7yiv1Y8xTRWtmdWamu-oOsKG6p2V7oMTF9fscCS7ut2cHIi_x5GfPRKsAAG4QM8JhV72xVzCDOPsl0a-OfS8TnZjxM92XCuw0X2LEU3QPftA_JGR7Hm-3B2FuMWKgoDi3CTaEGROaKFXMp5HmzTyyr54P4KawdsC3infXmG7olePIc-K1x-3gyYHwqp_hYKhiqFTSUb1K69ew-rwZ8VuA4DC7tGvq2INj4Z3Cfgw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=Dd83QCUVJ45OukY69qctHKlWXsJK7U0K0zXSM-E6tnFsZt5xgTMJW2vEHDVc0i8oyB4Kb2O3ZIdTi1aJRgqBF4Eavo7n8zCtE-lCVNYGpbt8cl9ywJhkmp_pW3RJwRnAg9pX-RXYPId4RRqFbUf5K3fWJpNNgphEIrSXoLxvORlNVTJtSZP2grBPe7afUiU7CazALMtwSOL-bCNeF3ti5gdFEdFzoNI1dzVOIJ9Y6bSnM8tfGVKSspk13YRmS0OrAnxyQvS16dKwFL9kQcOrS0N-nouT8icKxBQIb1tqVuzrTIAdV90KVKnTUt7B4OdEwWikjlfQX2HAp6Ts2U-6KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=Dd83QCUVJ45OukY69qctHKlWXsJK7U0K0zXSM-E6tnFsZt5xgTMJW2vEHDVc0i8oyB4Kb2O3ZIdTi1aJRgqBF4Eavo7n8zCtE-lCVNYGpbt8cl9ywJhkmp_pW3RJwRnAg9pX-RXYPId4RRqFbUf5K3fWJpNNgphEIrSXoLxvORlNVTJtSZP2grBPe7afUiU7CazALMtwSOL-bCNeF3ti5gdFEdFzoNI1dzVOIJ9Y6bSnM8tfGVKSspk13YRmS0OrAnxyQvS16dKwFL9kQcOrS0N-nouT8icKxBQIb1tqVuzrTIAdV90KVKnTUt7B4OdEwWikjlfQX2HAp6Ts2U-6KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVuFOvifCYrt-6Tfnv1tX29j4ODu7zC9Nxj5WnKCsFEXHqmHPQJj9VY8Qgh9TmVSQnFbZbA4J0mg9_Kuk_SJRxOel8bXcVHoJjEhhOeIKmdDrJDJYjIbeqTVNzVyPOCC-Jv-cDcHjOYh8VTcZtVvyWwVTqfq17XE8cf8d8lQm2-3D35GRQdswFRjUMwwBAt6z1Se8n3aini3ptSLQgqBi2cn_fX-PIv1yV2Ww1PejM06H8O3sZGdTwskGDfkf0mJqc6tmia10fQtPYXjnGh3KUIovsjdyaba9BzihsRPZCj0Ps15X7mLlHPbhJI5ka_XegxuPfbZqY8YuGO_yH87yw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnnJ-GGYTyZsWaRunLbGsi2ExWJSnxWjf9cSEihAkcPYKDODLTkn55hINcrjeBfOF9bpfXOV-jd2CDRzek926cYeNuWnSlhJwW4r6_95FPuaZFFAAczyqlU_IrnTbGBvEKRzY02Mf6VP0M4wtAWmuhniuB0y3jF2niOsMR4aLAwrG-SPaiBe5LgRKbfaiyTjLApYnEXzZGjW2rsIEjKnfUAAfW1VSrYp_6chN12YJuZ6NwngyLOGh9MUjndYb7QBV6XI1HQQJj_GJvs-_797f4lPzaZfBh9vwbGmJeMnWf0zIxExQjA97yS-cykdhLTzjthz83LkyWWZ1fhTmqUZqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از انفجار در سیریک
مناطقی که در دو شب گذشته مورد حمله آمریکا بودند در واقع حاشیه تنگه هرمز هستند.
جایی که رادارها و سایت‌های موشکی و پهپادی و…برای کنترل تنگه ، متمرکز شده‌اند.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5493" target="_blank">📅 16:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTNaQ5BnW5ank0fIc4jyDARuHkjn9sGx4E8est1CtUb3n70hAz60bmMl-_TXOvCDPyZZKWeipQ-uN0f4K8V_CXqUQ9TM80B3IY4hDVfxAmU8YBVjZjmyMK_Gx8wQKK1V3w_bBk9ABIUDyWZxDd_7E7-t_tg6PQ-un1LkgSBOXbwrQLXHY6zqsYYLVdEVlvSKFreV0Wu-NQgNScpKwfozeFCCVAwTPfLjkWJQ5EUvKQGLZuOfzDFBo79fSptH0nEPRAHUAwgUrs_-KUdeT_GnfK0avfG5rWY7OPl9e6iW2Iu7hx43cVc7o_XOGrGE-x_JBppi9qw2tdVoT4p5m9ryug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اموال ملت ایران! که یا مصادره میشن
یا مفت فروشی میشن به چین
یا غارت و دزدیده میشن !
بقیه‌اش رو هم‌ میدن «مداحان»
و «رجز خوانان»!!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5492" target="_blank">📅 16:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UtJfwi_y9N8XhRSrQqAACOjlq0wy8HgC3sr1Eslb5Wu4Cf-RPbeoW2fCzBaZSC4Sq-H9lVq1BtdTLZGX0TFBHpKergxDzzEoM_5-cwIDnP0cCcjmg4J8_t6nMR_lmSYFxyfWKDD0tmwaYtZCTu6EJCO-QKs_hzOmOIwYFYYxlW5B6CWO5jf7XZ6r6D7TQpKNZZQz_H9BvjVfTrRSyBOsN2P9qgbqarwHFR_2ljZigaJEwx5GscSXsKWe77JJWaIrDyPksumf3zbUZs8pw7Q9QrlZnOpJU_H29_Msk4AQZjdrXrfKPurw20wV4YQFXl-Vubcu1fzR8B3oDOpWT3qtsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5491" target="_blank">📅 16:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l932m9Jr-aVBVp1r9WWGU0P4G1xXdNWsiPAePV7IFEl6bXDgXIOZaHu5ySpqcBIOnGDplxckm58nRf0IU54rMT0MwqRLAJm-5GcYrWQKADAE2tGeseK1i4L5_1caa3RPoFeQVXmdozDhBW2PtJEpHmG0VUWFBucyCAJpodxj8Rhmn89eHTG16goySqdOnqYREiUpaoI09UiREl_ljhROs7YKFD92MPxnzmZrFOzhPvebctE9ZinpaKT5JWRgJECLwsF3l6KJjEaJ3cxPljGO71Ub__Cv4OcDeJ1EC3b9pR5wql4J3gt6f9H76HSDjKHnwTAmBkJMX3HvIOn-w3795Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5490" target="_blank">📅 16:01 · 21 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQoG_x7R3m0pk-sVx4aF1xu1QhUJhJfDHhOJioa7Bohn0FDKHRGYNGVuSdMnRbRq9lxM8LUiVP8dvw7YWvaxyFmh1mhjKwR99oNVOWdctYlyKCvHJ2AHnXlZ-Qdk8CSBnsl4Itl69NjlFntjmImBLGMdV76Nj7UJbC4IN1eQp3CuF-7MCiuVD2zC9n1zkWc7AXMN32sDa9Z7QxSoxDn2OVSMys5o100W5a6sfcUz0leZJ8J76tFzDGc57qFv_4J_O6ePN2h3awZAgYOZO_ORrn3NQiO_AXF-l8U93f_aTA7BeRSytBeY3V8YVNnSFXLF-XmKkrWqvsLO-clsgTcQbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پاسخ به حمله مستقیم جمهوری اسلامی  ۴ روز بعد اسرائیل حمله‌ای بسیار دقیق و هدفمند به ایران انجام داد.  گران‌بها‌ترین و مهم‌ترین سلاح دفاعی جمهوری اسلامی رو یعنی سامانه پدافند موشکی  اس ۳۰۰ رو که جمهوری اسلامی پس از حدود  ۲۰ سال تلاش و کشمکش از روسیه خریده…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5487" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/163555b294.mp4?token=nFg71e2MYxLXYpB_FINlM1z1Zq6O1H8UArlH2IRClrnj1RBQQL1vf65BP0qOQ2DSHfjTgaxTZnK_PsXjCVj3XwW6qLsF8EWFu1AHJvlpFQ6QRv-MhNo3FDenPXxfMuA8r5QIwkuVTMhboc3bEPWnuAMmy7o0-nbLS1aELvheb9jPRQcoJvTLT2PmO29s_goFtUZNlx5Dc0fzHgOkpwYSsclUCZsscaU73GBGw2gnK4f3eL8w6DP1q_QcGH-fT2zOncKX8-LX3hZbY4ugHVCktm_g8naPV7VdDnzIqOIM3aRGQ9mwuVtdaWBfUAUz6xs2Osw3W-f_5XkovEUqd2mmXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/163555b294.mp4?token=nFg71e2MYxLXYpB_FINlM1z1Zq6O1H8UArlH2IRClrnj1RBQQL1vf65BP0qOQ2DSHfjTgaxTZnK_PsXjCVj3XwW6qLsF8EWFu1AHJvlpFQ6QRv-MhNo3FDenPXxfMuA8r5QIwkuVTMhboc3bEPWnuAMmy7o0-nbLS1aELvheb9jPRQcoJvTLT2PmO29s_goFtUZNlx5Dc0fzHgOkpwYSsclUCZsscaU73GBGw2gnK4f3eL8w6DP1q_QcGH-fT2zOncKX8-LX3hZbY4ugHVCktm_g8naPV7VdDnzIqOIM3aRGQ9mwuVtdaWBfUAUz6xs2Osw3W-f_5XkovEUqd2mmXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی از ۲۵ فروردین ۱۴۰۳  رویارویی با اسرائیل را از جنگ نیابتی به یک جنگ مستقیم تبدیل کرد.  در عملیات «وعده صادق ۱» ج‌ا با ۱۷۰ پهپاد، ۱۲۰ موشک بالستیک  و ۳۰ موشک کروز به اسرائیل حمله کرد،  دستور حمله مستقیما از سوی علی خامنه‌ای صادر شد، و جالب اینکه…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5486" target="_blank">📅 10:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hi6vGFFP2npvpaJ0lKnytG-wNZAtsgwReLMyh_kS1MvZZ3KmFQYPbhj610ZTveJHQ3x_SadrYNdPLZFegtyQUYrUQWT2QA_IHbpKTCWh9GBTU_1HzOOTxVjUHmYBqTjnNMb_fywFBc_OmG9f1wN6RqRonj-EHVGOXjb7JBXgIZQqsRnZtZDmuuIfqhFCL_CR_FCxuUhzuT8PdC4OvdZFjRLMm6EUBw-3c2oRfpqnzAsh3JA633z-5MEstmggnuPGJ5TGPIeD9m_ZVDNEdFOxqDG-7YaGe920wXbtnumQe4ViMPkCc5BDFxX1IKSmFcLuRqwotiwKlRZbfkmRTPDSuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ غیر مستقیم با اسرائیل سیاست  جمال عبدالناصر بود.  ناصر فشار سنگینی روی اردن و بعد لبنان آورد تا اجازه دهند، گروه‌های مسلح فلسطینی از مرزهای اردن و لبنان به اسرائیل حمله کنند.  اما مصر خودش چنین اجازه‌ای رو به فلسطینی‌ها نداد! نگذاشت مرزهاش با اسرائیل دچار…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5485" target="_blank">📅 10:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5484">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hn3npn-jnUzaP55UzjiYfPVKvaw08sj8wFFCaTtgxXMmSmQeM1Y-HJI0Z8ASsqy5OIcSTbj9HuxHOy06Zqu-DWEB8PgL-0Qo5dM-26lUeniASp60CSXqx1IVg35xJ3uQsFyYI-jklAqPeptfnQcJEEJCOA2t07s9r1wbnwzAb68JUdtGZ_8xlQDPS4Vx4t5ms70K0yOWek2BUq-gdOvz4P7Ji6weMlgsNSIJyvKB2NxwnGd3J7ktOvzxZp4TfRkDNOxPErJE0ohUqdkzaW8hwsBAlIwAGGkWFFPCAPrDyymOMeBDJts5J3FFRICxe73LBF8LR1PJpy-NJQJyUtEnhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی در ۲۵ فروردین ۱۴۰۳  برای اولین بار رویارویی با اسرائیل را از یک جنگ و نبرد ده‌ها ساله «نیابتی»  به یک جنگ مستقیم کشوند.  تا قبل از این تاریخ،  جمهوری اسلامی با مسلح کردن گروه‌های تروریستی مثل حماس، جنبش اسلامی، حزب‌الله، حوثی‌ها و….. با اسرائیل…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5484" target="_blank">📅 10:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqOGSmICRBVgKlZivLK5Mobw3lEeEDcnG_K1ZkEeO0cGgXUcmCxn1-xBf3v7-lrMe5a2dM0ow4i4Tk2_isC92wC09xqdwnd1MYMnWWAu1CTWRbI0a9DEBAbNj6MOnFTByYXuSGm-v_x2wQfJJOhvqDHdyf5vDe0ok8uZfRi_CYzk2WiwyqK9FxZX48jTcZrwitCs4iazN-E7r0uxySu3VEMJahGZ_RQiBIV2q8wvTXktw39kHDxSznXPvmEEq3MFaZLJ8_nxbROq2mV6znNDbbo1CrD4zhXjwSadIgHRzOpbShCiRwxa5E1zWJjTw9pSK_WFdSZKe_KvxY60z6QEfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از مهم‌ترین پیش‌شرط‌های جمهوری اسلامی در دوره جنگ ۴۰ روزه این بود  که «جنگ باید کامل تموم بشه»  و آمریکا باید تعهد بده که دیگه به ایران حمله نکنه.  منظورش این بود که یک «آتش‌بس» نمیخوایم! «توقف کامل جنگ رو میخوایم»!  این‌ درخواست از اونجایی میاد  که جمهوری…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5483" target="_blank">📅 10:01 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
