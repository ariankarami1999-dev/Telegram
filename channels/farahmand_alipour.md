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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 21:43:22</div>
<hr>

<div class="tg-post" id="msg-5587">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farahmand_alipour/5587" target="_blank">📅 21:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5586">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgmlffjzE_qrw0K4fcb3LQ2iexas8EVdu0cykiuoK4Fy6L_MD8sZL-s_CTNJup1hheqtReGr-ZtUQdaH6BSDhOAqzSyHbLrkU-ifQRnNxZcf2M1FULmSmUS3Ai9YT9hEJObZx4gSJP10kRBTTRdSdYNz-cOHNOMaWYgFYuIJ-ma6lrEvxJsDEppERlOQSHXfux3C6cwwdgc1iMlHS_AxH0JhGsvoGGGPBDiOtsZ57LFJ4jHZG3JsrEwAF7S3_9fQfJFLZk2smlIaPORCNezHOhFJrg9Vc8vO14AyAlAnDHV2xLDVwmLEikTH2NsEpRbJU64XtwDF1Mt7fV8lFhsbkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده دقایقی پیش اسرائیل
به جنوب لبنان</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farahmand_alipour/5586" target="_blank">📅 19:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5585">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">واقعا فکر می‌کنید اگر جمهوری اسلامی
بمب هسته‌ای داشته باشه،
دیگه «هیچ توپی تکونش نمیده؟‌» و
امنیت‌تون تضمین می‌شه؟
یه سؤال: اگه بمب هسته‌ای چنین تضمینی میاره، چرا همین امروز با اسرائیلی که ده‌ها کلاهک هسته‌ای دارد،  وارد رویارویی شده‌اید و هر روز به حامیانتان می‌گویید «پیروزی نزدیک است»؟
اگر سلاح هسته‌ای واقعا مانع شکست میشه پس باید صادقانه به هوادارانتان بگویید : نمی‌تونیم بر اسرائیل پیروز شویم، چون اسرائیل بمب هسته‌ای داره!
اما اگر معتقدید می‌توانید با اسرائیل بجنگید و حتی بر آن پیروز شوید، پس خودتان هم قبول دارید  که بمب هسته‌ای تضمین مطلق امنیت و پیروزی نیست!!
پس چرا بدروغ میگید که اگر جمهوری اسلامی بمب اتم داشته باشد، امنیت کشور تضمین می‌شود؟</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/5585" target="_blank">📅 17:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5584">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/5584" target="_blank">📅 16:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5583">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ : تحریم‌ها لغو نخواهد شد!
بستگی به رفتارهای جمهوری اسلامی دارد
(اول صبر می‌کنیم ببینیم ج‌ا چی کار میکنه بعد در صورت نیاز، تحریمی رو برخواهیم داشت.)
ترامپ : صندوق ۳۰۰ میلیاردی سرمایه گذاری در ایران کار رسانه‌های فیک نیوز دمکراته پایه و اساس نداره! (البته این حرف رو خود ونس هم قبلا زده بود که الان ترامپ قاطعانه رد کرد.)</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5583" target="_blank">📅 10:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5582">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNTpIgWIVuzbRHoTGOwA9rElA9FQv7hvWUQVXbK-10dn9SS_0v71VrXTO4f60ZXKatjP2sXegayMEa5NlwI1GauZ_VBGdFQNS30uoKq15rcOKyYooV5tlldtESq0h3neVxCNLmqDq8PPJxQNsfEUqMh4yU2NI8-QRbzGfrrE2zmz6XpgUi2Qq65J0ZhDEj9pgmATvQA67utXwoYin10_W-cekLINiFMbsxYOXJf3b6hxWCOiCbVZjHprm0U7W7tumO5Gp1Cr3ImqtPnwYzjOjwepcmr6D1WXkFRSvZB6Jt52HjzmKUNHFqhLEntdnjKaeyXcgvJdIfB04R3bnQqIww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موساد و ارتش اسرائیل معمولا نتانیاهو را فردی معرفی می‌کنند  که بسیار پر سر و صداست، در حرف زدن جدی و قاطع است، اما در مرحله عمل، و تصمی‌گسری‌های بزرگ بسیار مردد است.  بنت اما متفاوت است او کمتر حرف می‌زند اما جسور و قاطع در امضای عملیات‌های پر ریسک و ضربه‌ها.…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5582" target="_blank">📅 10:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5581">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNmU520OyUOM_rUGL52o5V502SVZxiwXwbVtVswFYx07M6V9JLsPy9PvCLaQlq8p1Vuih4heDgmhog7ZgnjLJeAxR920bn28qdzJZa0XebH1IOYevKa3iNaBVXty7okhdxnoIzCtGr8NF6uJU8PE8_e9aYEOIjCEPXVJ6MGtsPo_VoMrXzKuKOfipkgKCraA9SGhkFGJ5GZowioxf7HLQT_sH1-N4uEn_U1X6AQ_oncogHZxY1IAxInA_8o5PsSoqObOfPK2ZgxXUFzDW6UIgw8JN23jQdVU1dixPYnqKvWZI44r7fXm1iNzjxfY4_IRZcwBnNSJ-aNsybIbbOIKBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">او که از منتقدین سرسخت نتانیاهو در زمان جنگ ۴۰ روزه بود و به او انتقاد می‌کرد  که ضرباتش به اندازه کافی قدرتمند نیست،  و اینکه نتانیاهو زیاد از حد تحت تاثیر ترامپ است، دیشب در یک سخنرانی نیز گفت که راهبرد نتانیاهو موجب شده است که درگیری‌ها طولانی شوند.  او…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5581" target="_blank">📅 10:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5580">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=TKwr1ad5noJF1gnrLSYu4g-i5Pxkg_pEfuMsr4Gpb5bHj4kUKW9743oreE4hRJio65LfDbvkkaEUexMWDtshdF1VRmXwLTunUlfJc0lRdde6BYxgoYVN0pxBusxr2JhMxGdWYUrOYS1mKKIti8fl7blWT4d6HdXgs_C35Nr5A4nXMi5Yw6ZGdgtvsw-r7LzB5FHFH83FEV7fkfmtuS1mE-B26KqIUKKoJC9FvHgb6DrnJPttDNKQLd3DuNkDIonnV_hYaGowKMQMGaLUR4ZR50gDiW06VAZPhjKArqbK4qH9YBH1sXW-7LA8IlczOzXTY0M2fndov4ap8WXR9p78Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=TKwr1ad5noJF1gnrLSYu4g-i5Pxkg_pEfuMsr4Gpb5bHj4kUKW9743oreE4hRJio65LfDbvkkaEUexMWDtshdF1VRmXwLTunUlfJc0lRdde6BYxgoYVN0pxBusxr2JhMxGdWYUrOYS1mKKIti8fl7blWT4d6HdXgs_C35Nr5A4nXMi5Yw6ZGdgtvsw-r7LzB5FHFH83FEV7fkfmtuS1mE-B26KqIUKKoJC9FvHgb6DrnJPttDNKQLd3DuNkDIonnV_hYaGowKMQMGaLUR4ZR50gDiW06VAZPhjKArqbK4qH9YBH1sXW-7LA8IlczOzXTY0M2fndov4ap8WXR9p78Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">او دیشب در یک مصاحبه گفت که دولت جدیدی در اسرائیل شکل خواهد گرفت و امیدوارم که من رهبر آن دولت باشم و میخواهم به جمهوری اسلامی بگویم که من بدترین کابوس شما خواهم بود،  تا زمانی که مردم ایران آزاد نشوند و  مطمئن نشویم که شما سلاح هسته‌ای ندارید دست از سر شما…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5580" target="_blank">📅 10:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5579">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5579" target="_blank">📅 10:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5578">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5578" target="_blank">📅 10:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5577">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPaPvDSmTle2Cn_G65P6D7joL9eWY8uSmXyTKApGiMx6iKdVabWUynDucceHk9hmkcpBOjAUrJH12OETK415QigsHOtoya0tFg0OvEXz6R9ARyJdzHkOAsBz7-9a5nvJhB1TwaoJ81oKTO34csYloluMiiYMhY-4TUyACRyUH8QyTr6VZmpORy3gPsD92DUQPf2j4tEaOb9BULarmsh2mJlTpeGrAOaABjvfQM4Yz_oupmJ9GvYohyCm068tMaGHUU2YQ-bkYXL73eJd84kmMxKaKfR8BFn0rjxlJ8sI29STuepOQB2ZB2gQtkIfo_CP3rjrdGdvyJlBLTbyio4Muw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اول هسته‌ای، بعد موشکی …
‏به مزدورهاشون که هر شب جمع میشدن، گفتن که چی امضا کردن؟</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5577" target="_blank">📅 09:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5575">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n7qhNLJwMGDM-12nsesYY_c-HiAUzQrGQRvKgp6BGsyrqXOc1bNoMu54tr8abDjZEMlMLljxBep9GtZMH3PH9F5BPSI2eMR61o-64qgC0_ihLybK4SlrpwCGlrMKvS0eDubwNmHGbiqry82M5lYBVl4PGNjA6Eml6MAHt2fbf1_6pQjyOrPVCqJT6woHGoQHURnzKuIF28FCJewzzwNeP0k-iAiB9O3elQcFY9KcQ0eGHtdocHCwswDkNlG8KIwhoGtGYHYuyz5wXi-F4UNAhSVpTWw4lwDScEbGIKtIeRPavWtvPBl3_D9hFjUFzbRDVyIvmSvcYnEYh47FjMBzFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dcXLR2WbeYqRCJYaZ2GzY2xvXLjXXSRf6xwNKCAw4-Bz0fVA9olh8xz9KmEK8ikcoUxG75voMhu3jqkCkCL2deXk-uOXWGBbGfNy1nEAlyucctGcgic7KT6apkoNi2DuiDgCtCTFxFBs80hzgHh4NhFEtyoRCMLK5tUFm1h6RNzwKR6yGq87EHWN60a0CxI0jN1qmQJmzixZ7XbCF7JI2axxIJ2w7eiLMEtDGzotkS8P4jD0FgLrY2i3bHEJhBFNVIGCCq434hDr18daE_P93-Xe2U7pjjAsOYJMpVSjufBVTFnlWeSfOoF8G_M6JDjJU1GE1-iS26z-Wk-SlK9zXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسین شنبه زاده فقط و فقط یک نقطه گذاشت!
نقطه او ۱۷ هزار لایک گرفت، دست خامنه‌ای ۷هزار لایک! رفتن گرفتنش و بیش از هزار روزه زندانیه!  چون فقط با یک نقطه دیکتاتور رو در هم کوبید!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5575" target="_blank">📅 09:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5574">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXPNd-sjAK6k0FHjbEUDhvF1E6vdscgOFSJbeTN7yZuVUV-0KxyLKq1qOWkqexFwk-8uukZVbXrW0-m4ElApBznnLTNFTngMxO9ex6FVcg_BKQA9A2zK6H6strq0Zk6o9YPvJCvirBtcT0JN72ga7DTwgPg_h1ISOFoMT4zCdLxKtgAxdXL4UiSMX2cSR203d58Wh7FWlv2HtK7FchT2zQhM-kwO79Tx584swtoTWVuj-SbeDb2nA3DMuYal3WLb02tojAHUNIic672lJ7gG7sFp4b_ij0_WzZc4wkClfJzFdGu-UYfgg3NwGDDnCvu5duseOthqSl2SpURMVVAGqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنیده شدن صدای سه انفجار در قشم و تنگه هرمز</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5574" target="_blank">📅 01:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5573">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5573" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5571">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYhOO-R2LUKnhklu74Id45BTDEudSbOxk-7gL-KOCxQkyR8qEy_Ez-QuzOpLMpwC42OCS6v8NNhaCRbUi5pRQKbGOlp9eJWQz3jiGZ7LR5ss_7t4zuGYBjuijWpkjLld5KcDnnmyT9tRbeVSS8KR66zMzfGdkanvuglAjlb5R8eqTxaIslbejMCerhT1bhfOeiq1rn-gVIbwk8JSwwfK3vGamkmqXw0NbHIepgNvAVuToVf4X6QN6qBb7pPDS4t9ER0MNvlCqknelaaTaTwaNAG8H6wfqCcaRMXMgEXu_SR0dZYlasx53n0uRZgq3u470hTExviIqLdWGd5DaN4WDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=IElFrMxJG1OtmGnM8G_XKJYAxgog6m1OnM0dhnk2yXZTbT_JwJaIBRTRbAVODmAEJ4AYnNDI7yXlKFR0eKz2WfFJhQX_LBzrsyJlFPOb75DGLGF67ChufS5j7goZ7B9XP2qOhnae54kWB0Fd7fpdUTvaNgMVrMwMN_4YoZjFsy5pfLk7wCL6W7NVPMDp2sIGeAXCwmtvpJjBOc8OdR1LZj5EYMXXDg69G5Pl3ZYrwpuTajt8MpEtkPcefrNTcA2TDVzNfMXcWTXRJg8Lvb_6DrSd7hwOfYzDgwT3YXf2oIv5G_NkWZnUghYoariRcL9FxDix5VDCGOi04lWSVuhzEIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=IElFrMxJG1OtmGnM8G_XKJYAxgog6m1OnM0dhnk2yXZTbT_JwJaIBRTRbAVODmAEJ4AYnNDI7yXlKFR0eKz2WfFJhQX_LBzrsyJlFPOb75DGLGF67ChufS5j7goZ7B9XP2qOhnae54kWB0Fd7fpdUTvaNgMVrMwMN_4YoZjFsy5pfLk7wCL6W7NVPMDp2sIGeAXCwmtvpJjBOc8OdR1LZj5EYMXXDg69G5Pl3ZYrwpuTajt8MpEtkPcefrNTcA2TDVzNfMXcWTXRJg8Lvb_6DrSd7hwOfYzDgwT3YXf2oIv5G_NkWZnUghYoariRcL9FxDix5VDCGOi04lWSVuhzEIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین فینال رژیم منفور شوروی</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5571" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5569">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5569" target="_blank">📅 22:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5568">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=vliEBXA0J_ymtqAhKIy8fhSgC8kItyFBuYGvnWJcX83rChkZEw6oc-McONOmKytah9KzSDWRuAEqwkTMm74eCttbH5KcXlS1xozNkiVkqhgm98S-N8u6QPzeMKBlBVnO2aX7rrngjEU-TbisOP0dW0v5iHm7mleI7O0m1QHWjYFycuifQBTSEZ5g5iiiKIYmtg5FCx6-eWx-U2MmjJU_HYJL8w3BRrhLJ3prYcWBERg3oyApWvRLnN2EnpxRtSlPpMRpEqy5QOz1k2Uftxl5YCR8Ka4fF32uSIzjlL2-1pxy_tAnAOMxZ1avcm9ccOzMGLwvK2pH1p8uR76ubacHwIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=vliEBXA0J_ymtqAhKIy8fhSgC8kItyFBuYGvnWJcX83rChkZEw6oc-McONOmKytah9KzSDWRuAEqwkTMm74eCttbH5KcXlS1xozNkiVkqhgm98S-N8u6QPzeMKBlBVnO2aX7rrngjEU-TbisOP0dW0v5iHm7mleI7O0m1QHWjYFycuifQBTSEZ5g5iiiKIYmtg5FCx6-eWx-U2MmjJU_HYJL8w3BRrhLJ3prYcWBERg3oyApWvRLnN2EnpxRtSlPpMRpEqy5QOz1k2Uftxl5YCR8Ka4fF32uSIzjlL2-1pxy_tAnAOMxZ1avcm9ccOzMGLwvK2pH1p8uR76ubacHwIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله دیشب به ضاحیه :)</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5568" target="_blank">📅 13:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5566">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rc1LlD3zqCuGprnmnrbgLpLgnd1mFCu7FK-LL4ySrdE9IHUI6uJ0MkBzb_DSWhuUjvgPQKs_LIEsHEwro6Zy1wom71RiXAhFjZmhYZPs--uXV2A7AwLCrH8xmihGbDHN3RDcmYyDg55mutiL-daY3hWFO1wjfwUOOQ0BslsVzBGckSDS8Vvv0j3pMtI_JJNm3945FOFfbf5qTdh1XVrJb4GXDBmYV5EaulAJ6DczYf6lu3RRfCfN8q10Z6wa2cK-sr0-MDtuB_ejqUSoLyaFwDGhPYPvsNLjeLKy43UufybMif-KgstjzwiO-tWWbdQAx4NiGZTiYOwouruKzJX9-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GBw_GIV4sJgbtRCH48QSCYxpQxAsL6fxtWCMaPz4hl-pvcKsjZTbmk9Q8FhqkJEG0-pEpsRWDeMAECpLCAA25s8HpuMsVLWZEpuAsF8R806XYkgdJOcyaOzIh7KcqGafUu3WchyTlXPhcch9S5gmXu-bRquGo31C85WBYAwn1EZSGxFc8ZbukmzklAeveudC6beCY0luHzs-Koaeawr0ywhCWXJz56C8qsDg6hAvo5tPwK55xTzP-xLPV2eS7GZI68rcrOWM6SoRO35eTvt4AjMlVjvJdC1H3dnxYcAADodsaAIBT3MmomVanAcpEJaAxy_vzP5sT-76b6B8_5hV5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5566" target="_blank">📅 12:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5565">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uo-EVKpONwjyirABFjizyI1SGde-jdHRD27BfKm48QMMal63n5oHUdtEmmhHRtltgeoAogBHaFgVZxsF9iKXbjiSk0KC3a17fws0EQfjaK4BPwghKY3FZn1fJ3LYCnwqCGZRBCgWw0uAybSdQiMQZ0LRjM6WgLj6fchvQJFxgyv5Jk8eQRkEhOS8eppHQht2aXcOkWOjwYiLki_SXoyFqWWXaHBzZH3w6QgJfv-f6wpB4kF3KEgmYiarLicGoKDT_p-YmrL44Ixc1hwsL69n8nGXy3vcZcFo8qX-AC2SJeK-jVtzBzUexMuB2mEj-3tgdrbcdG6aqAMpOQr8OWV73w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم وضعیت لبنان</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5565" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5564">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHYk7T7BlKohVaqwQxDU7Q1fjWsr4cSsUyhEoccM_LyYF4jDguudnZn4ZOlvrTB9yEyoJZToDVGMjGpAdr609MLcc7KSMpqQZ7HUFR4WlBmirdTJO9hZhx01gwZ1MBPjOz1t9OmDKjKz6jc0-8O3l2K_fi4zTYMUFfj8JrT4zzj-HgGVy6F_LYQ6rfyFfl-e_ZGyEY0dZtpHIuDBHLxifNe18GRdEd9z6IU3je7-FRr-EMqqTbLfCBbFhenIRgweLFgtZBUPCkNqsrDIse9ahwqJKeLo4A1w54hkchYdtJZlg792EmlyQT0UXsbVLls_OdcTfcvsx1K4HPZ4qBnmTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون  امنیت ملی
و سیاست خارجه  مجلس دقایقی پیش متنی از سخنان وزیر خارجه عمان را منتشر کرد که بر اساس اون، جمهوری اسلامی موافقت کرد که  «هرگز، هرگز مواد قابل استفاده برای ساخت بمب هسته‌ای را انباشت نکند». این تعهد جدید به معنای «انباشت صفر، ذخیره‌سازی صفر و راستی‌آزمایی کامل»
بود که سخت‌گیرانه‌تر
از توافق ۲۰۱۵ (برجام) ارزیابی شد.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5564" target="_blank">📅 10:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5563">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">رسانه‌های جمهوری اسلامی،  حتی بیانیه شورای عالی امنیت ملی،  تفاهم ۶۰ روزه (که هنوز هم امضا نشده  و ۴ روز دیگه احتمالا امضا بشه) رو  «توافق» «پایان جنگ» معرفی و القا می‌کنند.  در حالی که چنین نیست.  یک تفاهم نامه است برای یک دوره ۶۰ روزه که طرفین اقداماتی رو…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5563" target="_blank">📅 10:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5562">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،  ۲ نکته رو به عنوان دستاورد مهم توافق پایان جنگ با آمریکا معرفی میکنه : ۱- پایان جنگ در لبنان ۲- پایان محاصره دریایی.  ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!  چون رسانه‌های غربی چنین موضوعی…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5562" target="_blank">📅 10:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5561">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SN29ff7fB7J17Simuw28t4DpT6Zvvmo7mRjmXXH1shuDwnhaokH62qO70uW0iFpJXjrExLZuy05lTEDu4-Y76e7XjgMfiVeFbevLJbbEa3bNOf0L5ky7_PC8qkVCAFhrjTMdV6AFZ9IAR0Ax2KumYqJb54FRjVo_XPOg-iKHnCo4b0xwwCGTMye7AF_B7Kj2fkGKrtY3G1JdA0GxPy2qQUp0K9AI2yQvnp2us8DCPd9O7jMgCsgW3F8QUXF4O6iIUCUYWxF8q5O88kDMWYA4S1YD_O5yg15Ffvzl3WKZt6ybinjipgKi0Q--Ynh_v76oOHVnAG6JWMv6WQ7vAJrAYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،
۲ نکته رو به عنوان دستاورد مهم
توافق پایان جنگ با آمریکا معرفی میکنه :
۱- پایان جنگ در لبنان
۲- پایان محاصره دریایی.
ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!
چون رسانه‌های غربی چنین موضوعی رو
به این صراحت ننوشتن!!!</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5561" target="_blank">📅 10:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5560">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=KcWo7ScMpajv4h37qVqEKYO_6FlD7KyuoN9HTMHDCNI58dQ58Bqt0eKYFhL1qVcCK3210dpap-UYqFg0hSC6rVrhNqZtZxko20Z1VsuN5Bt0pFVSQy7HVlZzMlE9urAFSq9tw-GaaeoTiP0Nn8VCfMPatLXJwELXcZh3HfMWGUJGH001Ubswx9Nqq12Lv48HxYbDak2TUsep5nYCFu3GD5gcMIh5pNdmvIoSBvZ3KgCO7PQql-WbUjlg8M-3dcPsBboEEK3ySNhgAPqYXF8rN72M3kKgt6nzuzGjjWeTWpvXfADJuUX64dPiJMQ2Be0eirAa9Y0GWlUHKxVpREsCTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=KcWo7ScMpajv4h37qVqEKYO_6FlD7KyuoN9HTMHDCNI58dQ58Bqt0eKYFhL1qVcCK3210dpap-UYqFg0hSC6rVrhNqZtZxko20Z1VsuN5Bt0pFVSQy7HVlZzMlE9urAFSq9tw-GaaeoTiP0Nn8VCfMPatLXJwELXcZh3HfMWGUJGH001Ubswx9Nqq12Lv48HxYbDak2TUsep5nYCFu3GD5gcMIh5pNdmvIoSBvZ3KgCO7PQql-WbUjlg8M-3dcPsBboEEK3ySNhgAPqYXF8rN72M3kKgt6nzuzGjjWeTWpvXfADJuUX64dPiJMQ2Be0eirAa9Y0GWlUHKxVpREsCTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام خبر امضای توافق جمهوری اسلامی  و آمریکا در صدا و سیما.
ظاهرا حمله برنامه ریزریزشده‌شون به اسرائیل هم لغو شد.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5560" target="_blank">📅 01:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5559">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTpvzzzvg1TOfJlG4Be_5zo8_MseCDeXt4RLbNh8Uq3rEo7OdKCZYNnmcj6yIiWA6dT0kl3N568AO-QxD-ASUXu1DT8wE3fjptFvB-n0Qd2_oah4vkKn0ew5PnwQep92hKahxrdAnOiXNYRE1nGofjr3GrIk6YvZRDZoUClV9iiyOUlRxXzgKyniiVF54TSDzqgmMeql02xE8DPS6LpXez1jHih2TdmgTjHD2MKm5PNe9SsU5Qsaa1KEnUvjeungM8fji3sOLLYLCqciKrhNg9IOcvvcMGOR-Wjdcs0opfyIEQQehsNQGLuPUHX3jJvxEWifopEBb-n0KBiSx_zhpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده تهران ؛ ترمز امضای عجولانه توافق کشیده شده. سعید جلیلی جایی نرفته.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5559" target="_blank">📅 00:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5558">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
همزمان با تشدید تهدیدهای لفظی سران جمهوری اسلامی، اسرائیل بر شدت حملاتش به جنوب لبنان افزود و موجی تازه از حملات را شروع کرد.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5558" target="_blank">📅 23:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5557">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THT4AcGyas-GwHUtrph7qqw3q_3vs64juV-pI5_hHVIynm4jPtSRY7LlbjSmlDPPNJ_wpCnsdsw2p1G8QHoUmrFOYQgMfo-Xw_jjrP9PSnq_3cIzKOFqSzp_B7Twub0HpKnZwcQKPxpOZeLnX2u2z0kuqZ7orICmLf8cAaLjH2JXrMmLGsCNboUoQMYPYdY8WwXJYcOyOf_xIzDgJlfR6Zgqw3B4vcXdg7BRJxKd6NYc-cI_-UddtnztnNLhU1YGsAQwa1G5sQngCdUJIh7Ikjlvy2zOD5h-1b6G-KUuHDP_bKB0Tt_Ivz7xzF11MPkUXjy33W1v3NlHElO-NFNc6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ولایتی مشاور بین‌الملل علی خامنه‌ای</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5557" target="_blank">📅 23:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5556">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5556" target="_blank">📅 23:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5555">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dojG55UyRaNJYHPNaMooGfIxvl7-Q_8GqO6rHRT68nXdpyhV6WHePqeLkxkz87fYRVe0rOJfSd_7MawgmOobBSuyECBD67QaOgu0vPQbhcnnL6mCoQugECeUZuAvQlDP7_RC12NPzFht1up_RRGxcmxcqNjaGtx9F5vz9g62ZDntkUSBkp9YDVncyvSzKNH9Fi7vCuGkYcGBwj7PNqL7hUr_GvC6TG1liTSXDQiKgffMRhUIa3yWvKwNIUsvYqN1Z9PQqzrLTizzChIYRSk2yg3aSITuHzbpDVlvylMf0JtScm8Qy82b36V1tzt8q1pQtLkRQ-NlIG46hoFj5Ss8HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف «تمامیت ارضی لبنان عزیز» !
«بساط جنگ افروزی اسرائیل
را برهم خواهیم زد!»
جمهوری اسلامی به خاطر حزب الله لبنان
دوباره میخواد وارد جنگ بشه!
آتش بس به دست آمده میان دولت لبنان
‌ اسرائیل رو رد کردند، به جنگ ادامه دادن
الان هم توافق نامه پایان جنگ با آمریکا رو کنار گذاشتن و میخوان برای حزب‌الله
وارد جنگ با اسرائیل بشن.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5555" target="_blank">📅 22:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5554">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5554" target="_blank">📅 22:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5553">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
لغو تمامی پروازهای غرب کشور!
آمادگی برای پرواز آبگرمکن‌ها
روی بیروت خیلی غیرت دارن</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5553" target="_blank">📅 22:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5552">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NxgRB3U7I1Qxr-qPQFYIWKNkCKbFbOuOr-zmN4e__wstGco2yb1ybDZ5JF9olGZ1tQA1jJHCTTK8ojjFshBYEEBuf4yqV-v-P-G341hHnkY5PNi7Al_IgukH3DoqWV3LxCUxfduj10zw1A7cQx5H1cEZdM594_4TtxbtiDuKfsWQJjBbdUUwpzbt0Rqh_qc7laK3boNppPsfebgd8jctOKKGXB3grg7aph0JtqPXbbQvbWmouwlHeJewvrFWNTS0OwhZ5siQHEYpIL5a4zBnOvZBW9vkCqPGIx5ncKfGct2owjT05gFbUuF-LZ4Oz8AYQJxE9sBLHJKg19tWNWRJTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای عالی امنیت ملی
«لبنان جان ماست»
پاسخ رزمندگان اسلام در پیش است.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5552" target="_blank">📅 21:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5550">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ld1oe2jWjbm58nLf5E36LQu-zVuErd8QsAcfEVtx9ygCQc8JD5xRznlqAVkxcIDQv2IK33gvPJqE5Hk8eCY8x3QLo0B6MBcGz-UFbPOnS9mgH6PiEnEgCnod2HHhtx9mND3dQR0K8LXSBeYmq8a-AbvnrBNKk-BLl5zQo3FE1XEf3KbfP4Et9tcet4CkUdpAlnhmHbw3bR-zT5D8I5VHdUwLu8PbvZQxpcZcPuzILNZr67b2ADkuij6X_IVgFMWY6dlzKR_bVzv0MlCwTZVEmDjNF570597KvSANv0xsNy2Ahrrd9slgSOdQDgPaPSyrvYQY80FBV-v1qdnND1b23g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mBDzOmACKiq3fhRpebigt_MkhU9-evIk5czGTN67Frkz99rGm-LCkbz1IqITViedU0G3Le5t78mP28OMaFJxYIsoNGpshUAW9K-5m8MvgkrBubAPf5nuHzkluo8X2DM3mhECf4IyBqby-bF369MAu5fD8JuQdoGrWsphrFuZc4Ni93dPKXS_Xr8ehhboK869tOMPGnUku7j_oCRkBYKaLL1npK9Cg-QWecCUu-AhsCpOpLKLhbQDRDTeXGJ2ecHfGMPbwQErAkygRAa3Opo0dew-DYczOsAGSs88wzQq_yjcrlgx01p6x3T8auEqYB8gtav27Mjz7VHqjeATKg-OeQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عزادار کودکان مینابه
عزادارن حکومتی!
میگه حکومت همونطور که در ۱۸ و ۱۹ دیماه «به حساب» مردم معترض رسید و دست به قتل عام زد،
باید دست به قتل عام معترضین توافق هم بزنه.
اینها هیچ وقت ایران رو دوست نداشتن
هیچ وقت ایران و مردم ایران و‌ کودکانش براشون مهم نبوده
اینها عاشقان جمهوری اسلامی هستن!
اگه برای کودکان میناب هم عزداری میکنن، چون میخوان یک کردیت به جمهوری اسلامی و سیاست‌هاش بدن.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5550" target="_blank">📅 21:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5549">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ترامپ : نتانیاهو نباید دست به چنین حمله‌ای میزد!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5549" target="_blank">📅 20:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5548">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
ترامپ : به رغم تنش میان حزب الله و اسرائیل، تفاهم‌نامه با ج‌ا امروز امضا می‌شود.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5548" target="_blank">📅 19:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5547">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/goV6Y0KsgFGdlhGQiAxr308VueWV8h0Njzuoy72DnLyDTbcWKN4o5-IrH8w0sxwxFRMn4h3wL_r_wNdq27RSLCZGr7YlDeDzE6P3TDaOzN9RBO0i9cITa2TJDh-vYjq-ZJFrLrAYe6XDSdOa1_DQJeDDtiWjxx3Z2pVjzKr8mQHcq7NqL39u9uZMLzftWrulzU72eDBu9UtLjfdiW3EdtrdWefkjTFTjRyrfQ5KeRm_RspJvGwfjie4U5joV1EkLOzzmq43K80_xgjscrCATjqSzyMy61tb2pOvKiW60dLyv6wURxarWRhdwHkNALoHs-uzO1E0Nvi-27eRacrLqWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5547" target="_blank">📅 19:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5546">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
حمله پهپادی حزب‌الله به اسرائیل</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5546" target="_blank">📅 18:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5545">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامپ : اسرائیل نباید به بیروت حمله می‌کرد، آنهم در روزی که ما با ج‌ا در حال امضای یک قرارداد مهم بودیم.
اسرائیل حق دفاع از خود را دارد اما حمله حزب‌الله به اسرائیل چندان جدی نبود، کسی هم کشته یا زخمی نشد، می‌شد بر روی آن چشم بست.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5545" target="_blank">📅 18:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5544">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">قالیباف پس از حمله اسرائیل به بیروت : ادامه مسیر توافق با آمریکا ممکن نیست.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5544" target="_blank">📅 17:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5543">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mkbiNuKW6aqHkucSmnxHcH7tREVfLfLpEKKxs_qaPd1elFH6BkW6nqHzImtHlifMfgY5awibcvRt916wNkYyQusd-yspjcmL9PxY8pQIhZIxM2iDhCa98f5X8Jo1LfIpwRi8cIwEkU-aqLkfXxeuBBX_cYWF_-psf_hKhDgPcrf6OqV4SzULRncpaZE-cRqvbznioJGqkU8nlNZLz0lsSBwCfZws_Pwny2H-4xKJnIadI3tYUFwizVK_k16A5uP0cXpVF4P1bmFSUNmWlQw2Ga7Cm8XhjppNZkpbCwBftSw3kElL4UV8HtIeOrvyL_AQF_i4K2q3QECm5-w7822ZQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسرائیل در حالت آماده‌باش کامل،
در پی افزایش تنش میان اسرائیل و حزب‌الله و تهدید جمهوری اسلامی، سخنگوی ارتش اسرائیل از اعلام آماده‌باش ارتش اسرائیل برای پاسخگویی با حملات احتمالی ج‌ا خبر داد.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5543" target="_blank">📅 17:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5542">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=vccqzp9YG_PBxAo6QYki3NDLC3EpKnm9eSqnqxWj54YSdfyig_T21aGwDRUCQ1GQv9Myatk0CfxS-92_r-HyXlIIvi8TVBjGx2wW1lPXFMX2XWknBwnkmFPUw9WmzinS5SGpAeRoQvndbt3aOB6TuQd05DT2vECnkpXan8A9MR9NAXvzOpe3wuhuyWiiNUs3V7YNGgOoYZw7gtALDjJNiGC8G2ISDnQ8NkqGMHtjsqIwKiOx7ywa_JKOuohYz6iVRUAEC1Pkii4znzXNIsCFZuGIXBf8TxW5QlZ7-iYq_NeAhIPjn-ebWnSEVenCihG0YUoI0vqYGwYA5AuF8lzv2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=vccqzp9YG_PBxAo6QYki3NDLC3EpKnm9eSqnqxWj54YSdfyig_T21aGwDRUCQ1GQv9Myatk0CfxS-92_r-HyXlIIvi8TVBjGx2wW1lPXFMX2XWknBwnkmFPUw9WmzinS5SGpAeRoQvndbt3aOB6TuQd05DT2vECnkpXan8A9MR9NAXvzOpe3wuhuyWiiNUs3V7YNGgOoYZw7gtALDjJNiGC8G2ISDnQ8NkqGMHtjsqIwKiOx7ywa_JKOuohYz6iVRUAEC1Pkii4znzXNIsCFZuGIXBf8TxW5QlZ7-iYq_NeAhIPjn-ebWnSEVenCihG0YUoI0vqYGwYA5AuF8lzv2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدونید که هیئت پاکستانی
هر بار که میان تهران، برای مذاکره نمیان،
میان تهدید کنن!  که رهبر و فرماندهان
شما رو بمباران می‌کنیم.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5542" target="_blank">📅 17:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5541">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=DVTf8Ze7RIeHN-HD2Z6JFQW6tD0i6F4Wg6WkWBV4QcOOZMdTjdBd2UFFWgFmJqPvcW4qGP2JOUUkkLevpU27arqR6qU6qmZcIYc3JPkcbmqtg61BZ7Yq6bKgmZ3kW4LKS--EnEN89cRaa53gWmYgv6NEcAM17C928azuITqbCqjUqPWLTV9uYTJR_RO3evSZlpRhIdmARyeLnsruoj5BWLL78Lpkt6kwDbeGGDuE0awXURrtjPbE6p-FSdHLOQvdjUI8LU8QZRE8MvSd6a83TCmDTeOE3-FMtfVUGU_LNSlWuJGhg_BjY_vtxMqPXyXdfBDFHJQVemPwoJaxwFGBGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=DVTf8Ze7RIeHN-HD2Z6JFQW6tD0i6F4Wg6WkWBV4QcOOZMdTjdBd2UFFWgFmJqPvcW4qGP2JOUUkkLevpU27arqR6qU6qmZcIYc3JPkcbmqtg61BZ7Yq6bKgmZ3kW4LKS--EnEN89cRaa53gWmYgv6NEcAM17C928azuITqbCqjUqPWLTV9uYTJR_RO3evSZlpRhIdmARyeLnsruoj5BWLL78Lpkt6kwDbeGGDuE0awXURrtjPbE6p-FSdHLOQvdjUI8LU8QZRE8MvSd6a83TCmDTeOE3-FMtfVUGU_LNSlWuJGhg_BjY_vtxMqPXyXdfBDFHJQVemPwoJaxwFGBGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه‌های وابسته به جمهوری اسلامی :
خبر حذف دبیرکل حزب الله
در حمله امروز اسرائیل به منطقه شیعه نشین ضاحیه بیروت درست نیست.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5541" target="_blank">📅 17:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5540">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=evidlRF0evqUeWgy5aZ4Y1AnmvJHdHycG4qlQtvGuirUBo545JarhhNUhtQN2zRwXiaJ81gRiyh2jHShJuetQu76JvJlgFX4ypKWqXVMGqRK2g8vOgIAdUT2xHCvpN2jK7fWTaWAWLyFK6dMpjkXTierqhA3j1nwXlJzm4eWBCNmF2MhVxv08rWjuYfvvI4jlaF-X75kQlirLWR8GMsfklLgjIiehG1TM7D1I2rqz5JR6CU_hkhQsnCtBuPp7OkNGTmzM7b2issIHqCLldqGwyPLUPV7Fl6hewdymH2czBV5rwwOSsvkIaw8ZEHNDpWJ4EHqIftcQtIX4Ku2P7Ta3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=evidlRF0evqUeWgy5aZ4Y1AnmvJHdHycG4qlQtvGuirUBo545JarhhNUhtQN2zRwXiaJ81gRiyh2jHShJuetQu76JvJlgFX4ypKWqXVMGqRK2g8vOgIAdUT2xHCvpN2jK7fWTaWAWLyFK6dMpjkXTierqhA3j1nwXlJzm4eWBCNmF2MhVxv08rWjuYfvvI4jlaF-X75kQlirLWR8GMsfklLgjIiehG1TM7D1I2rqz5JR6CU_hkhQsnCtBuPp7OkNGTmzM7b2issIHqCLldqGwyPLUPV7Fl6hewdymH2czBV5rwwOSsvkIaw8ZEHNDpWJ4EHqIftcQtIX4Ku2P7Ta3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله اسرائیل به ضاحیه بیروت
حمله اسرائیل پس از حمله حزب الله
با دو پهپاد به اسرائیل صورت گرفت.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5540" target="_blank">📅 17:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5539">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=dHiaMEhMXiQjJJfcxwCenxhiRbNPawrtS2jBcLxkCkpe03OTppYM734txBLjrmMC_g623xMydm1IP1gdSO9pgcjjdunvuH5y7VK5LHEhWhc9EhFTFtTdjP4Ya1W_4NnVmguIiLasGYSofwrlxdmXcqr3hCrsC8B11dgENinwbv9RvIM2dDQ75zqRvSq867Xy6VhTu7vmbF8hLFTIZXHLv4kQjRJlbL3FmOgAQSoh6WIq6ESDDsSaVNR2ceDJ9Msft09tfX21pFOZif9FpS30vPplM7hk2OxEmpzQH2sFLOxHVFHgO1JZJpBOHPSYt8coOzY1ybIG5U5xMqsp5ukS0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=dHiaMEhMXiQjJJfcxwCenxhiRbNPawrtS2jBcLxkCkpe03OTppYM734txBLjrmMC_g623xMydm1IP1gdSO9pgcjjdunvuH5y7VK5LHEhWhc9EhFTFtTdjP4Ya1W_4NnVmguIiLasGYSofwrlxdmXcqr3hCrsC8B11dgENinwbv9RvIM2dDQ75zqRvSq867Xy6VhTu7vmbF8hLFTIZXHLv4kQjRJlbL3FmOgAQSoh6WIq6ESDDsSaVNR2ceDJ9Msft09tfX21pFOZif9FpS30vPplM7hk2OxEmpzQH2sFLOxHVFHgO1JZJpBOHPSYt8coOzY1ybIG5U5xMqsp5ukS0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان : رسول خدا و اصحابش
لت و پار شدن. :)</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/5539" target="_blank">📅 11:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5538">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
حملات موشکی حزب الله به شمال اسرائیل</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/5538" target="_blank">📅 00:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5537">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=rXeOOlIQ0JwfamufJ-69L2EyUSmZisd3TYgS_swcn_LafZZ5X2-3L36eIHUVnsMmMFWCCGQtT76CtPL_4sJKB9s18HQyMfp6AVRU8GRiDlXTEoC2lbAP7RyF7GtBsEaJy8OBDlpdTyE1DYCD7cS4y_tmBw2jY007bEHAeZ-D9PEMLy79L2hlFnzA-q4lHT9WdVEuNUh8hmk_Dgh141_EgReVrvF0bIfLcrTO3nBFfpCn8Auu5uBcxD_70z4XYYz55Xl24DNwKMsB-lKPIg2JSfiiKuUMsbmvUIO2sYFcNyVmjJFGxeHxOtOgv7R_mfK4zHXgSEQE-PgdKth3arXm7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=rXeOOlIQ0JwfamufJ-69L2EyUSmZisd3TYgS_swcn_LafZZ5X2-3L36eIHUVnsMmMFWCCGQtT76CtPL_4sJKB9s18HQyMfp6AVRU8GRiDlXTEoC2lbAP7RyF7GtBsEaJy8OBDlpdTyE1DYCD7cS4y_tmBw2jY007bEHAeZ-D9PEMLy79L2hlFnzA-q4lHT9WdVEuNUh8hmk_Dgh141_EgReVrvF0bIfLcrTO3nBFfpCn8Auu5uBcxD_70z4XYYz55Xl24DNwKMsB-lKPIg2JSfiiKuUMsbmvUIO2sYFcNyVmjJFGxeHxOtOgv7R_mfK4zHXgSEQE-PgdKth3arXm7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زنان کفن‌پوش ولایی در برابر وزارت خارجه و سر دادن شعار : مرگ بر عراقچی بی‌شرف نفوذی</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/5537" target="_blank">📅 22:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5536">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8679568b89.mp4?token=dX9Lg8YaBEoE2q8Y5dn73aerY_Chixae0fm93B21VNOZrOQwXcmEkF2qC4V6XFlNDnUFOVfHfTI5HiKgOllkWuBjzl5Uve-gQh4eD9YlJBIvYJeW0Jx7puRsofyvmEKApC9pwGZoGt6n-C3bNF6z_s-5SgDgB1NVNsUTZWnTqDXcEnytazCx2tOnAcUmAHavCfz7CyvMC4aocILUAbHaRRMQ07UMQOwLzlYbrevcMql6HWKcE0RLpkg3tPeAX5OUdswuxLJgGTHYCcxPWmii7g9WNAFz8bPMB61XywD8h2TrpqUjtHF9BlrYSBWgL02OkPysx_JyLR7pACA8WK1nGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8679568b89.mp4?token=dX9Lg8YaBEoE2q8Y5dn73aerY_Chixae0fm93B21VNOZrOQwXcmEkF2qC4V6XFlNDnUFOVfHfTI5HiKgOllkWuBjzl5Uve-gQh4eD9YlJBIvYJeW0Jx7puRsofyvmEKApC9pwGZoGt6n-C3bNF6z_s-5SgDgB1NVNsUTZWnTqDXcEnytazCx2tOnAcUmAHavCfz7CyvMC4aocILUAbHaRRMQ07UMQOwLzlYbrevcMql6HWKcE0RLpkg3tPeAX5OUdswuxLJgGTHYCcxPWmii7g9WNAFz8bPMB61XywD8h2TrpqUjtHF9BlrYSBWgL02OkPysx_JyLR7pACA8WK1nGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=HR9Ra1AMngIxOTv4nFCZwvQbZhGPLGyipP7yMXfYqM_t-FEZE152kRG58XZFuUzViEIW8Pe3PNAEX4pm-hHBdVCMgqeHVLVYA-NdZkar7rjR6mZzG3p14vKd1gVDJAoX191GMgftge47z7W1CjXzf5c86pO9gkdovJAFKmkSBXid0Eyt4cAbGstBBRPzAwlK5P06cMoQgZz-Z4Tgsbl6HhzF0Zx-xgHc3eVJq1CPTUt1KDA-qZLm79-9jk6DI_3ZDLVgV-q4-UkAKz2-qt8P5s85tofd6AUQpT2X8k6ohSMRvo3pC1qemVmXg4JbqA-aL_xaV1LLindKp9CWyTIO9xDue4DOb8hP9GkUloiP-l-aqPnWGOpXTLSmO4jNsaUBIKmzuFzP17BxpNF99mlMZnMdJelPM45OXzlTUQxbaw9WtRsDUdVeaeXEmE6nDEef2tM7DEP5ygRG4qULRFKT71P6Iq1QijyIenyof6byzCIfkmhhLoqjG8-RDPNK1c3DlNi2diZiBNEuj9z90zw--CpNx4qlO1rfc6evoLkT3B6tb-A40qeuXjjr2Ak9L_iBQxLMCjAxHnkuBGAVqIVp_pLK7U0oIfzmzqB9oDNG6RVQNNGO-z34NArir2eYFjAgnPOXPqtBxxDYoNGXgnmsCHgyAGIMnuyXn2NB8cYGJ5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=HR9Ra1AMngIxOTv4nFCZwvQbZhGPLGyipP7yMXfYqM_t-FEZE152kRG58XZFuUzViEIW8Pe3PNAEX4pm-hHBdVCMgqeHVLVYA-NdZkar7rjR6mZzG3p14vKd1gVDJAoX191GMgftge47z7W1CjXzf5c86pO9gkdovJAFKmkSBXid0Eyt4cAbGstBBRPzAwlK5P06cMoQgZz-Z4Tgsbl6HhzF0Zx-xgHc3eVJq1CPTUt1KDA-qZLm79-9jk6DI_3ZDLVgV-q4-UkAKz2-qt8P5s85tofd6AUQpT2X8k6ohSMRvo3pC1qemVmXg4JbqA-aL_xaV1LLindKp9CWyTIO9xDue4DOb8hP9GkUloiP-l-aqPnWGOpXTLSmO4jNsaUBIKmzuFzP17BxpNF99mlMZnMdJelPM45OXzlTUQxbaw9WtRsDUdVeaeXEmE6nDEef2tM7DEP5ygRG4qULRFKT71P6Iq1QijyIenyof6byzCIfkmhhLoqjG8-RDPNK1c3DlNi2diZiBNEuj9z90zw--CpNx4qlO1rfc6evoLkT3B6tb-A40qeuXjjr2Ak9L_iBQxLMCjAxHnkuBGAVqIVp_pLK7U0oIfzmzqB9oDNG6RVQNNGO-z34NArir2eYFjAgnPOXPqtBxxDYoNGXgnmsCHgyAGIMnuyXn2NB8cYGJ5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توضیحات نبویان در خصوص وضعیت تنگه هرمز در تفاهم‌نامه
- به محض امضای تفاهم نامه، تنگه باید فورا باز شود، بدون حاکمیت ج‌ا، گرفتن دوباره تنگه و اعمال حاکمیت بر آن تقریبا غیرممکن می‌شود.
- هر بار که متن تفاهم عوض شد ج‌ا عقب‌نشینی کرد</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5535" target="_blank">📅 21:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5534">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tnsc2bt-uavFL13dqiZjGI9WcmYrH9q5_Gbql5rL3MKSnOEDLhKtwFpiRk6cpj5Q96Z6wKF1exL0qtdkImerNlB5XfeXjXFj1e8t9YcjRndy2QiJnh62YykbHkMR7OgGdLpCgsEsuPKbV9UdpBAnCM10e9u_Ge_8aI1Zg4jZKeBLH4KflqnJeHO1EGt0bbHO_ADUXjJHbo6qmVhajxO32vrW2wZbX7UJHTu8NeIQltwPxRK1ik_4xDJxmaqJ8eE2-ovOuBB5AFRoQaUlvJ3JBGm5TUfiQvIMFLjGGKlzHjoEOSkh51tLmIARoibh_V5t-D10gpacHOU1AXhCoqOa0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: اصرار ترامپ
بر امضای تفاهم‌نامه در حالی است که مقامات ج‌ا  صراحتا گفتن  تفاهم نامه هنوز نهایی نشده</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5534" target="_blank">📅 21:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5533">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=rEsZi6DOFNaaZDhEtLE-9S4ObanOm_mXs-E4ljtZJIiOfPvyxof02-bsuFewBzjNT8ewTmijkCPF5s9nqHIevRJ6xMowFSqFJJV3CHcG6aRb1MdTnTaSqzNSxariuF80LbFcbXOpdDLblzMBFLBPoQSOvwpnqVmN7xLkvGw-raCUO78MjCBi1SYsFG92xz2ZhpEeaw57EEzm9T2jvGQdXdPmX-De5aQ0kqS2MUYbX2EhxXTjz-_RvXkwLo_9SMTCQEcpzPGDfqyTHDtQFGJn7AOql7Z_ZMPvqKXcgkv6dFX7epTrAzx89qvumiM4Xxy7WRJ6E7RMm495CoYSD1vzYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=rEsZi6DOFNaaZDhEtLE-9S4ObanOm_mXs-E4ljtZJIiOfPvyxof02-bsuFewBzjNT8ewTmijkCPF5s9nqHIevRJ6xMowFSqFJJV3CHcG6aRb1MdTnTaSqzNSxariuF80LbFcbXOpdDLblzMBFLBPoQSOvwpnqVmN7xLkvGw-raCUO78MjCBi1SYsFG92xz2ZhpEeaw57EEzm9T2jvGQdXdPmX-De5aQ0kqS2MUYbX2EhxXTjz-_RvXkwLo_9SMTCQEcpzPGDfqyTHDtQFGJn7AOql7Z_ZMPvqKXcgkv6dFX7epTrAzx89qvumiM4Xxy7WRJ6E7RMm495CoYSD1vzYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۹ ماه پیش
بعد از جنگ ۱۲ روزه و قبل از جنگ ۴۰ روزه
این تهدید پذیری اگه به وجود آمد پایان نخواهد داشت.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5533" target="_blank">📅 20:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5532">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGjdxT4ZPXgOHi6Dp_g2QZzX3VKBeC1DlX_EI4Up7boDISZyK1L_Eo8DgHwi9EtdAflXWJOfkpTfemITB6xtF7H5f6I25AHA_UF7pcJAoRoZx797RfXhS-tlxt95wIoaJ5MU7vFUmZz4v8gBRHGtU2c0531MKdlk9JnypK0v8kmrI2d2m07OlJmmriwljgXVwzKDiWq8Igr72kRoz8UcYJDV_papl_n3bZZb83OLHTCoKdoBY3iouB9tNexc15z7Dof1inTXzpWXjWZHSJFNAwg8H3E-MvE2cAC93WXfQCK5UR0KYTtn0vdu5FKUezxclU1iCNLQ-xXhXb1Ny6m5uA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HrGzHVP9XDOlvp_uku8fubPwZe7sGxoJjaT7NOjNZxClet7niSlL6hK005xBRoVwKCdrVhCTZndUloIzo844goBGf8sOqbGjXhQNGp3e41ft7O1x04ntjCqHQWg1f5sR0dioPXZxfs3ybYA1dOnR2UCoz_TgObVmTt3cC-T6utE_jebYTQvdeHXP5TfVsfB8l56kIPyv1Oj1i8YnA0OQT-VxKP1KaUzDw6dB_uOK2kgw8VoQMrtu2UJ-MdojFlELk2NAIc7jH4zj67TcTowWC4ZDd9IfAj0O2p1UyH2oGBjwXo90I-xwQ9zJXtzE9cH1K7dclGm1v3R94YIMiKxe4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیسی خطاب به قالیباف نوشته.
نگذارید خط تسلیم و سازش با
قاتلان خامنه‌ای به ثمر برسد.
(نه سازش نه تسلیم - نبرد با آمریکا!)</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5531" target="_blank">📅 20:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5530">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJv8Nq24steluKWjnHSBxwTIkmOx9LIP1WLXUJU4avw2DUpSKrqh2iVlLQBnciPFC-mcaw3D_6P9RVCj4LKuxSzh98Rt60OymWwpXHV0lxcBf-4uUhNwVJXfxUAsBSMeS1K2lUT4o0xKU6OvOt8InWcg5RNh1rpatPagvTpuf2PDMKEkubGN_Csz9bYtdop7MFUYSdM6lJ91OtORddYsE43ezeinX6weaMv-vwW3iELhM5TBkypgAlHFRn9qzyslT_3sw7ArVKG4MbH1uGWuNuQpilukeEQe5EDuAZZ7tlLIIhN7ltE6tqRGdRmU5NrAmcHVTgdvv5iwajRTFzYvLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">نخست وزیر پاکستان: تفاهم‌نامه ظرف ۲۴ ساعت آینده امضا می‌شود.
عراقچی : برای ۲۴ ساعت آینده هیچ برنامه خاصی وجود نداره.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5529" target="_blank">📅 17:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5528">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=WTSpJJDEelb7h7Tx3fttqzAi_dJJNv9KWMnpkNtHfP2N9TuYT4goCklbsXdHmTjR78ruRXHau9NBNYHPbGO_3H_5GusgIjmxQ4uQ1-V2U8bE9Yzs6SR0Be26UlqjBeVCqFdIW2-xqzoDZ6L7C5nu8nPebTWHjEI8gZQcEeG8GLzLX-pN5P-tOP7w-TlE0my-yTK0meIVqF716W_mRe2PbcISOklgqjQ5k79l9g7m_Z7eLbSOrRyTtPas5En2JEOfvcqn7U9Cr04Eb6_298jPH0ENzK05Shqm4t8hVU9FAYAV6pLtIa-fqT_KqSDgwkibdSVPfloyvHQ0v-tNnxCr3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=WTSpJJDEelb7h7Tx3fttqzAi_dJJNv9KWMnpkNtHfP2N9TuYT4goCklbsXdHmTjR78ruRXHau9NBNYHPbGO_3H_5GusgIjmxQ4uQ1-V2U8bE9Yzs6SR0Be26UlqjBeVCqFdIW2-xqzoDZ6L7C5nu8nPebTWHjEI8gZQcEeG8GLzLX-pN5P-tOP7w-TlE0my-yTK0meIVqF716W_mRe2PbcISOklgqjQ5k79l9g7m_Z7eLbSOrRyTtPas5En2JEOfvcqn7U9Cr04Eb6_298jPH0ENzK05Shqm4t8hVU9FAYAV6pLtIa-fqT_KqSDgwkibdSVPfloyvHQ0v-tNnxCr3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان مناطق اطراف نبطیه رو تخلیه کرد تا در مسیر ارتش اسرائیل نباشه.
این جنگ بین لبنان و اسرائیل نیست.
جنگ میان گروه تروریستی حزب الله لبنانه
که با پول و سلاح جمهوری اسلامی و به خاطر خامنه‌ای، جنگی رو راه انداخت.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5528" target="_blank">📅 15:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5527">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZgTPNA2zMGn4vTvkteoOoTNRVzJPXB6RC4KmfoRP-qF4GMzlR6pGVxF7K80qFC7BmUPcZfqNVPmpHisnDPbSdHfOXzYAhTc5VcStYnu_Siht8nylr5EPoZP97qpd5xtj_agv-KNW72gRK6A-y8j-vA0-HoZjC8NYcnQwvyo5sBdiz1n4w2Xtvva5ghnmClSAiJda8qN4_VoOCkHGBSyjOQLiRIgfrguqt_KdNxCslOjLwwkCBbFhFpo7T7cVVw7ghYn1-9aU47umQfqYm1yCihM64FnoICiO7pOF7nZfxnmiKk0vU32z9lc2YGLFKJHsHFl4g_aq07sw0NQB8juYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی در باز بشه می‌فهمید
مجتبی خامنه‌ای در واقع همون قالیبافه!
چیزی به اسم مجتبی وجود نداره!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5527" target="_blank">📅 15:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5526">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKuGfg0eL52UC04ka03Q8AvCr-qS-GXR_NZcZGsTED2hUyQuuJQZ4UWku10wKwVaJIh9HVBUTxynUeVYOW87zBW0421k_XF5tVzs9ipvgszqKSg0EtT4yFiw9T-HXzQhHPEryg3nYRXllJ75zyuCNHMzCGc-Qvjx_lS_BUBCoLxJgiOes0L8ZS9ewV5S454A-XPx6nIX4luLt_PqfBvi8r98ioIiZYal4xS3AkzxrMHyGZIQ71KPPMMBlG1sKjZCkZ3WXteODCjsJbZJca-_r0W4cURIgzPKok2q-8DPK013mHkqoQ_SXQXaR-J8Pgy3PIHbu5MNKUsnJLXSvjMN2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : ارتش اسرائیل دقایقی پیش
به حومه شهر نبطیه، یکی از بزرگ‌ترین شهرهای جنوب لبنان رسید.
اکثر جمعیت ۹۰ هزار نفری نبطیه،
از چند هفته پیش شهر را ترک کرده بودند.
بعد از حملات موشکی ج‌ا به اسرائیل،
اسرائیل فشار بیشتری بر روی شهرهای بزرگ جنوب چون صور و نبطیه و….. وارد کرد.
ارتش اسرائیل فردای حمله جمهوری اسلامی
دستور تخلیه شهر صور  - بزرگ‌ترین شهر جنوب  لبنان - را صادر کرد.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5526" target="_blank">📅 15:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5525">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oao-keGOyEo27vyddul3qFRvFpLbMhI1QnHy-qpf9BMC6YGNLXl0ojH18Z9K7lz_Ju02RO2KxOZy7NcGmR8N2Ks1eM1dEt0NziAYfk8-0YTYi4zJ5JObUeh15S99I0Mg0k1h3MHmhVg7Mc8SeopsIGPBh0cCWX0fHtC4O51Kz5c2NvZHXvQoaT5OfEqQ2Mk6VIKKjRm42UP0M-rJvLmE4e_zhMYoHge1RVFVPBOTN1ltZuOfA0H4m3GMmum9BMCuSxRlhIE271g-bRxjkBjLjm_XJV1y02vFTTr-6JV11Vn9paBPUHK31tWNrH-1tWRTdwBpzbmDwNLsIozvQjUplw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات مراسم تدفین خامنه‌ای</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5525" target="_blank">📅 13:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5523">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFDKGwA6nBdBIsH1nMuwiP3BOMOTkvxGKWSWAV6IpENwGmqFpTjUGQRvd991oSarwOQ1-MJFmTeA3SfTj2QR5KfhGUrvcUq9426C7-SGqNpAp6QfoAjYnIJgbFralYf7JNJTOwuiaOXPW3UopY9YVd_cUKi8t1q6MrYsMA8uOAn5utyjFqHAF0d3X1VpUSeMSAk95V9mrfo2gidbknV_lRLgPCShMw_-jwbxHyi_98Tv3jonUAkntethmFT3GKi2JK3YZVVmp7mYMhQhl_yOkkt7gqnVScp2am_ZpygFbbG0HooqyjLyZX_gkAlejMHr0hlnYhtHvCY0_HFCabTgYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=I6C2NETpwAwqOuLvr7oaMClkmUptTa1WhKukyI_FgpkZ-HRlumcpZgOozHa8hHW3m2oQe4McQHg-5Fde9bK_NlMqfCSQ0cuvsZIreG2KhAcafa1svEsR-9vPtfaAi4uM9eyVLcOZYPAClJEuzMEQzCS3YMf0DT0vFkzIHlgkjdkyMicD6npz60BbW7hOnxajP2UBR9c_voEmJTQZa-b7aTYRvNP-HRXB2PKBcrkIG1KyN_RpKuzos2pklHFMGXcv32OS1fOUg44sYKBU2WT0kek5UuDhp-ILUvUrmPlPBc0yq7YcQhv3lmBSyPbuz9zXs1txUxKJ-BOZ9pIzjZ26hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=I6C2NETpwAwqOuLvr7oaMClkmUptTa1WhKukyI_FgpkZ-HRlumcpZgOozHa8hHW3m2oQe4McQHg-5Fde9bK_NlMqfCSQ0cuvsZIreG2KhAcafa1svEsR-9vPtfaAi4uM9eyVLcOZYPAClJEuzMEQzCS3YMf0DT0vFkzIHlgkjdkyMicD6npz60BbW7hOnxajP2UBR9c_voEmJTQZa-b7aTYRvNP-HRXB2PKBcrkIG1KyN_RpKuzos2pklHFMGXcv32OS1fOUg44sYKBU2WT0kek5UuDhp-ILUvUrmPlPBc0yq7YcQhv3lmBSyPbuz9zXs1txUxKJ-BOZ9pIzjZ26hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5522" target="_blank">📅 11:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5521">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YnTzohet3iKpmoEUXnpIZChdDUhZuzxH_FfE600aFUlfazaBTUDTRNpyRbDS-dSb5SdYLmB3XfcPcyPAwCpSHksxMGjsK3WqU5M1p4pB1qibXKyQNiQ6i4Fk1_s7JFGw_eay3Awijrr2eTLpM9oJneVktRvs0zIDvSMLOk_wUZIU6hLIxWzinvMkI_8VOfjolGjMFByZjMX9mc2XClV5RLgSHN_qqp4Os7ms_1sGlS7SxXnpC5bohQWDkBH0iGv7PQanqihn2uDe9AnrBX5YPoZ9VjoHMx7s_HW9jhxSEf1t0aQt5rG32KC4G_YZWXbrbyfls85bTfvCLQuTtJLjNg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDXBGnQq9S3R4D8SkKRREN7xJ80DEoOyf5lcbHtAenmR10oOkTvQQL9UglTgHX7BYj-RLBxnGYnOMoUaUks6Gync7L9FJ8tL_q-3zcfUXsD3g-F1d_ZISR5eXAFN3Qci53Vjxbx99HIMEZw42e-g1DW6DcKiBZLWyaKZAt3ec6oHDVPQE3NGyiCzvRNLepNUjDK3mqBuVz-VLB5rb_D3rHcW6jJD8mYD91mfCApPrFG6cAY3qPYL-Uj8BhTQebFUrkn891YMGml5H5lW5AiAi6nwWZwwc3E_sFZ_4nmDHuucyj_NdtUSA9_jpUjAFobuMw8TQuH_W-OrWuRHkXT9aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5520" target="_blank">📅 01:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5519">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=GtGJVLHG-jy5Seij99FKNZOLVAP14tbtwtqS3XUK1V0VS_15u3MWutmjlRBwR8Sn14GTBVtVtLljTqdAcBylUCKfkqH5Y571kpusyCHr3BCq4331uUOAmtLiBQK6oRue9eUHCmejo6DvWHqqVLWKjOYGkZqE7pOq5_1Yf1HhUp_OUcbe3IIlfVG0YBfCmqDX8BXzNyw1hT1MdUwVugwh_TrswrFJy6X9q_AqaQiMcKc_1lZ2TxcRNB_2CxXKTRm_IHRUyIvLorBLX6q-uVVep0M7o1RqkqbYDLqqz-w3MQpHj6ASRPARnyarYeh93BYbuM6c4TDZqltiqi46F_UAsJlazhLTRlGMcnM-pEQ9EqRlLZ0BmkGxeQNWYV4us4czc8ZcYTbLp3SYIQGL87L3EdNjayzC2psjiDL_U3wLiQ0Fq2aOyNHWy3Nwr5PqCX-laaPaZr1i3xIvFthb5M7CH411YTyU6gCoOZYAbbRP_OXWxuv52DmlpWuhtsbbK3v2oxx1q23WvMs3LjsWhJBhnrrW0xhkzRpYmJHbd6-Hm1z2Yt-w2QwSOWKVJQBugu0Vllo6T0Ke3foHAbkkanpHvgwthGIMKZaqwcmJaq0w0dif09aR98ZIXijqxMdaIFPR5dSjXf2tAaG9e9-D3_bxAKqGCRcj4PFL-_095ERLEJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=GtGJVLHG-jy5Seij99FKNZOLVAP14tbtwtqS3XUK1V0VS_15u3MWutmjlRBwR8Sn14GTBVtVtLljTqdAcBylUCKfkqH5Y571kpusyCHr3BCq4331uUOAmtLiBQK6oRue9eUHCmejo6DvWHqqVLWKjOYGkZqE7pOq5_1Yf1HhUp_OUcbe3IIlfVG0YBfCmqDX8BXzNyw1hT1MdUwVugwh_TrswrFJy6X9q_AqaQiMcKc_1lZ2TxcRNB_2CxXKTRm_IHRUyIvLorBLX6q-uVVep0M7o1RqkqbYDLqqz-w3MQpHj6ASRPARnyarYeh93BYbuM6c4TDZqltiqi46F_UAsJlazhLTRlGMcnM-pEQ9EqRlLZ0BmkGxeQNWYV4us4czc8ZcYTbLp3SYIQGL87L3EdNjayzC2psjiDL_U3wLiQ0Fq2aOyNHWy3Nwr5PqCX-laaPaZr1i3xIvFthb5M7CH411YTyU6gCoOZYAbbRP_OXWxuv52DmlpWuhtsbbK3v2oxx1q23WvMs3LjsWhJBhnrrW0xhkzRpYmJHbd6-Hm1z2Yt-w2QwSOWKVJQBugu0Vllo6T0Ke3foHAbkkanpHvgwthGIMKZaqwcmJaq0w0dif09aR98ZIXijqxMdaIFPR5dSjXf2tAaG9e9-D3_bxAKqGCRcj4PFL-_095ERLEJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5519" target="_blank">📅 00:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=cwENYb23msLWIM9AFHV1I-r2ZbRPHg9HxKe5GWHyw4u5z2Pe4KEM1iNjT8iiWkhVf7XdzvNosHhY2G4JHITjLcljI84KRaBMAQIb9aUhklkyZeJTGu18v16vaEm6--xmObwNpoZi1ZnDZu-1xfzd49BAW_pWutvpJmsArycIb455ftn0gjlttDUnGVP2R8mMQFO1LToYaPa7E308h214G_n1QHlBV-tmQeY7oDCtbAs9IqOCBYLhdBkXRxApVnbiZuHENfoTEuOv5qDKKDr53qQr8Oka45XRc_SVdqFstusoybRt-0agfI7_hXhKPTc0oMOeQ9pLfZC5farMLRjuTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=cwENYb23msLWIM9AFHV1I-r2ZbRPHg9HxKe5GWHyw4u5z2Pe4KEM1iNjT8iiWkhVf7XdzvNosHhY2G4JHITjLcljI84KRaBMAQIb9aUhklkyZeJTGu18v16vaEm6--xmObwNpoZi1ZnDZu-1xfzd49BAW_pWutvpJmsArycIb455ftn0gjlttDUnGVP2R8mMQFO1LToYaPa7E308h214G_n1QHlBV-tmQeY7oDCtbAs9IqOCBYLhdBkXRxApVnbiZuHENfoTEuOv5qDKKDr53qQr8Oka45XRc_SVdqFstusoybRt-0agfI7_hXhKPTc0oMOeQ9pLfZC5farMLRjuTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">وزیر دفاع اسرائیل: از جنوب لبنان خارج نخواهیم شد!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5517" target="_blank">📅 19:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5516">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5516" target="_blank">📅 19:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5515">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5515" target="_blank">📅 19:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5514">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
عراقچی : هرگز تا این اندازه به یک توافق نزدیک نشده بودیم.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5514" target="_blank">📅 18:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5513">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3Roc0z1oSZ5YHIMX67EmgPE3v-kOriLCQLlkJa2epIcOM9cX3pd_1knnvEdOfZE2YtOlqkDUP9PdAdSngK_WHVseMvEmNABPL-KyP7oj36nQ8hUlT6EzQAyPMT8GjKEBHipNtR9rc0dg_K930A5N845xWAdxuL2y1kugIFh8_K9wgMkD1pSPiVlWcqEFJdtzukILGbn6y4CSbyFPuReOYmWhaJvwc-8FtitUBbM9OSDPdyMbxe7UxoD22Qi4M7HU0eJFPYZ8QFAyipogWrv42wFV5_ujgH60TT1LiDl3r1N2oKuDItqhMfcRPIwu_nHaRZ1ucnTqp9XavUdmg-gtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : این مواردی که جمهوری اسلامی منتشر کرده دروغه! اینها یه مشت آدم بی‌شرف هستند، اصلا نباید با اینها مذاکره‌ای بر پایه حسن نیت صورت بگیره.
حواسمون هست که دیشب هم با پهپاد
به یک کشتی هندی حمله کردند.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/5513" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=hTC7j0IAdTsM2x-Cl-VK32d6qqJT0dia7OnUqLkNQEtw4Q33nPirdIgdv9rnS_xEIbbcJKwEnW-DMw6QUd05HrCPsQuzoYU0qJRYiMkUGtp9oSkHzzmPKY2WYU-mONhFW-lK8RV641CpjtE2bM3X0cN1J6UN_62zPPwZAMcNIp3PsRbVqrDd0ur_Fn1yoGqI6g-bbOZu48-6Cd59j-Iy83gK6bJEhubSIEYceA9jDxDB8TkU1GFKQI01g0r60FAdHyNPZaygEaN1E8Qvjtdopq2a-91suZmjhV2dvWVIHlLst8QIwXAs3Mog8BJ9QMNSXcpY-uXkfPo6YR2EGwzUJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=hTC7j0IAdTsM2x-Cl-VK32d6qqJT0dia7OnUqLkNQEtw4Q33nPirdIgdv9rnS_xEIbbcJKwEnW-DMw6QUd05HrCPsQuzoYU0qJRYiMkUGtp9oSkHzzmPKY2WYU-mONhFW-lK8RV641CpjtE2bM3X0cN1J6UN_62zPPwZAMcNIp3PsRbVqrDd0ur_Fn1yoGqI6g-bbOZu48-6Cd59j-Iy83gK6bJEhubSIEYceA9jDxDB8TkU1GFKQI01g0r60FAdHyNPZaygEaN1E8Qvjtdopq2a-91suZmjhV2dvWVIHlLst8QIwXAs3Mog8BJ9QMNSXcpY-uXkfPo6YR2EGwzUJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امروز اسرائیل به صور
دیگه نمیخواید بهشون کمک کنید؟</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5512" target="_blank">📅 15:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5511">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
رسانه‌های حکومتی :
جمهوری اسلامی کنترل تنگه هرمز را رها نخواهد.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5511" target="_blank">📅 14:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5510">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4QqSMDCzxaQSxBPMvz7DnIecqgN-rZlM1DbdAEePNTB_o-wpMiCKE20cOOJJaAjkwQRW69ABq_NXPbLsMSwh-XnQNQzYlQRpo8qmrYUjIcn6MrZypEWfQRxjJvmOxOygtc9J8VPZeNyoEv2mHDdykyCBM0HnosJjIvaF-IzLnruRSALDQxVDEbgirm5dWwoe5wR17KEvJtonf3Yuvxfye4aQ7JE8i3GQpxki8rKsYAppnaPWOXIkDftPYRLLrmr6C90wj2Nay-9yC4OAPhykPUUpbU4y2nQFPMsWGJgITUgAVAbwVgecEgZWndhJzOAt5PpeICJbEyCB7fsmRTdnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
قطر خود به تنهایی حدود ۱۰۰ جنگنده بسیار پیشرفته دارد. شامل ۳۶ فروند رافال، ۳۶ فروند اف ۱۵  و ۲۴ فروند تایفون.
🔺
بریتانیا برای حمایت از قطر ۸ فروند تایفون در این کشور مستقر کرده.  قطر همچنین میزبان بزرگ‌ترین پایگاه نظامی آمریکا در منطقه است ولی اجازه استفاده…</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/farahmand_alipour/5510" target="_blank">📅 12:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5509">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/5509" target="_blank">📅 09:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5508">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=k3SwNStEG5LVXmQU1hsIZNQ5_7IWmlDsiryu-Rxbqhsm61mlFBdiGdsMDPVesP3lynK11FEP7QQGDUBxE3mLwGFtfbgZweDcLuSyedMF-WY447Ps9iuT0-juNFrUuXZsgzHW1a82iE8NQrjtIvW3pX8aJ9KiqsCWiMDIRkPk55_Xs5geDW3ZgiZWfDERym_RNY8A2jdwMFvjnHNzbrr0OiS52soiDDCWDjT-96dxvG3wbmNtuxgt1P4zG1lwZxd24NfqlvnbkaPmOAXQgpPODarCYvZU12sMMzdtXqaDmOwznIGQ-6EGA5iqTxDXn_ALCd8kmZRXlEgSwxSscJBpWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=k3SwNStEG5LVXmQU1hsIZNQ5_7IWmlDsiryu-Rxbqhsm61mlFBdiGdsMDPVesP3lynK11FEP7QQGDUBxE3mLwGFtfbgZweDcLuSyedMF-WY447Ps9iuT0-juNFrUuXZsgzHW1a82iE8NQrjtIvW3pX8aJ9KiqsCWiMDIRkPk55_Xs5geDW3ZgiZWfDERym_RNY8A2jdwMFvjnHNzbrr0OiS52soiDDCWDjT-96dxvG3wbmNtuxgt1P4zG1lwZxd24NfqlvnbkaPmOAXQgpPODarCYvZU12sMMzdtXqaDmOwznIGQ-6EGA5iqTxDXn_ALCd8kmZRXlEgSwxSscJBpWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاور قالیباف:
دو نگاه وجود داره، نگاهی که میگه بریم صلح کنیم، بسازیم، یه جوری مشکلمون رو حل کنیم.
یه نگاه دیگه اینه که صلحی در کار نیست!
ما قراره با اینها بجنگیم و قراره اینها رو تسلیم کنیم در برابر اراده خودمون.</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/5508" target="_blank">📅 08:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5507">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=sPjDek_rXSbymPB9F-6TCE_ZMDklbIxgMDFs8QcF7I_Jg1Z-MTB6OPuB-f5exY_MOigwVRvh42kcuUzInyjSiX5upRC5gXcjZfcCECXSeKV0d4qhW8wKPuHhEyOgq0RhcFV_NFg8Opalexu70dMR2eI41Sx-1IWJh4F-Jt1F5SHN3KBi5n7HPiyxJGANq1-FjQMlQOd5P95mbeOB3q1krHhd7lkMQca_0Glk9gjBGUGBTC1k1r2-5e8ngPYRTjygXiV7MAMBYzGkMoNcoQ2sORvyuml3hkL5CJo7PNyoXzvB-sPndZxnYhhNUIYKAQjAsBbDNJHe7SuFOofnLtXa5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=sPjDek_rXSbymPB9F-6TCE_ZMDklbIxgMDFs8QcF7I_Jg1Z-MTB6OPuB-f5exY_MOigwVRvh42kcuUzInyjSiX5upRC5gXcjZfcCECXSeKV0d4qhW8wKPuHhEyOgq0RhcFV_NFg8Opalexu70dMR2eI41Sx-1IWJh4F-Jt1F5SHN3KBi5n7HPiyxJGANq1-FjQMlQOd5P95mbeOB3q1krHhd7lkMQca_0Glk9gjBGUGBTC1k1r2-5e8ngPYRTjygXiV7MAMBYzGkMoNcoQ2sORvyuml3hkL5CJo7PNyoXzvB-sPndZxnYhhNUIYKAQjAsBbDNJHe7SuFOofnLtXa5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی ظاهرا متقاعد شد که شرط و شروطهای ۱۰ گانه‌اش رو کنار بگذاره.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5507" target="_blank">📅 08:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5506">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">صدا و سیما : شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5506" target="_blank">📅 01:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5505">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
ترامپ : توافق با ایران باید همین چند روز دیگر امضا شود، با حضور ونس و در یک کشور اروپایی.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/5505" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5504">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
نیویورک تایمز:
مدتی کوتاه پیش از آنکه ترامپ حملات به ایران را لغو کند، با پاکستانی‌ها که با ایرانی‌ها میانجیگری می‌کردند، صحبت کرد.
به گفته یک مقام ارشد دولت آمریکا، پاکستانی‌ها به ترامپ گفتند که «ما با ایران به توافق رسیده‌ایم».</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/5504" target="_blank">📅 22:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5503">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک «منبع آگاه» نزدیک به تیم مذاکره‌کننده ایرانی گزارش داد که رژیم در ایران هیچ متنی از توافق را تأیید نکرده است.</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/5503" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5502">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
اکسیوس: ترامپ حمله را لغو کرد، چون قطر گفته بود که به یک توافق رسیده‌ایم و فقط مونده امضای مجتبی خامنه‌ای، اما حملات دو شب گذشته آمریکا،  هم ج‌ا و هم قطر را نسبت به نیت واقعی ترامپ [که جنگ میخواد یا توافق] دچار سوظن کرده بود.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/5502" target="_blank">📅 21:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5501">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
ترامپ : حمله برنامه ریزی شده امشب به جمهوری اسلامی را لغو کردم!
گفتگوهایی با رهبران جمهوری اسلامی داشتم.
محاصره دریایی اما همچنان برقرار است.</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/5501" target="_blank">📅 21:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5500">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
ترامپ : هر شب بهشون حمله می‌کنیم، تا اینکه به توافق برسیم.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/5500" target="_blank">📅 20:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5499">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">حمله‌شون هیچ کمکی به لبنان که نکرد هیچ!
هیچ ضربه ای به اسرائیل وارد که نکرد هیچ!
فقط یک پتروشیمی در ماهشهر از بین رفت و اسرائیل فرداش، برای اولین بار دستور تخلیه برای ساکنان یک شهر رو داد!  صور!
دیگه نمیخواید کمک کنید به لبنان؟</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5499" target="_blank">📅 19:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5498">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UIAuG5Mmz3uyQ1FGc9kE2s6hRhcKs5U5xYBuWVOCJG7ZosHT2HrzbzYj7YSCrZuSXfx7VOnfi-gelpyD2PfCrSiyxcpusZAiesXCF_A49IE2cX4OF5-q5D6kqH8J-x7hshM4G5ODbPsNhpbYGJfPlcVxg1gBoyjvwyOqAzbYCsFWKhsDQfxPpkwfd_Vim11sHr3MsUH_uNz7YLFY9nMI1PywM32fZbHOuzxQgyPKXl0jalAn-kg8pdOYQ6A47vxKg9YIpeVeldYAqcITPcd_o69c-6QzIxo5U-CHCSxXEVZColZbprdUj-JdBhuBR5JNG823VcJEft3Lh3beP6300A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=pDrb1k_3PLyid5pgKWbyvr-wstvsHgspaS7rmBmz7i7BotuqtqizaoW96_UoNBD45aLeugZyIAKtgF8lk2wE5mJcfacG5aLCI1rEfxGIdKllNS1BipvI6MD00uS3uFtr-_BFG-R0BsWXjtl9HPx43vGoO1qfxlDup0dNYUE689C7WcIOKqVmGJ456yqbb7YnAgvWX8kZ2mkyNQmP21U54eDT71QkbSK0BasKGmPLszkdCqOyAXhAs01h67cGXWCuxyguHJetgE_6_gCVq81Gh7a2qvJvPcMQx8_pXQvSZIB5pDvSUmEnyYYsx6hIhNnBN8bP86u-_yL-65bronz94w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=pDrb1k_3PLyid5pgKWbyvr-wstvsHgspaS7rmBmz7i7BotuqtqizaoW96_UoNBD45aLeugZyIAKtgF8lk2wE5mJcfacG5aLCI1rEfxGIdKllNS1BipvI6MD00uS3uFtr-_BFG-R0BsWXjtl9HPx43vGoO1qfxlDup0dNYUE689C7WcIOKqVmGJ456yqbb7YnAgvWX8kZ2mkyNQmP21U54eDT71QkbSK0BasKGmPLszkdCqOyAXhAs01h67cGXWCuxyguHJetgE_6_gCVq81Gh7a2qvJvPcMQx8_pXQvSZIB5pDvSUmEnyYYsx6hIhNnBN8bP86u-_yL-65bronz94w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‏سی‌ان‌ان:
برنامه‌های نظامی آمریکا برای تلاش جهت تصرف جزیره خارک ماه‌هاست که تدوین شده، اما به دلیل این که این عملیات بسیار پرریسک تلقی می‌شد، پیوسته به تعویق افتاده است. این خبر را یک مقام ارشد پنتاگون و دو مقام دولتی به سی‌ان‌ان گفتند.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5496" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5495">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OO6bFvMofvv1aJaDYbhpSS49rafLoYcpMOSTJcP48jVXYZ3xxYJYoPYbWZypZZSuqWpW3K3k_QCOLK3RHzY5XDwXj3gglb6ubJfynoICOzbDQA_sh-Mwcqh1JRmdnZyexz3jTyBJ-1LHgw8dLvJ2HYr2nbDQrKSh1o50V4jFED7W45mtFJ19SMRaMopMWl-UUdOjoHKyvnAw0onMaKmtblcZQf-JbyZBzi6hF-IOh5j-ZsCAOyw1cHqaViEGh__nrX4iWgd3WtUDq4BhXEm-nPBWxolk6BQTAi2zE2RbijQh-ATpgagzNfEv6CWJEUgwoGEWcLi1OrjDWo98jgJZ6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه داری آمریکا : خسارات وارده به متحدانمان را از حساب‌های جمهوری اسلامی جبران می‌کنیم.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5495" target="_blank">📅 17:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5494">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ دلخور از رسانه‌ها :)
‏ ترامپ در گفتگو با فاکس نیوز:
«‏ آنها دارند با ما مذاکره می‌کنند تا به توافق برسند. این کار برایشان سخت است چون آنها مغرور هستند. آنها بسیار مغرورند.
برجام جاده‌ای به سوی سلاح اتمی بود. راه من جاده‌ای به سوی بدون سلاح اتمی است. می‌گوید شما نمی‌توانید سلاح اتمی داشته باشید. بنابراین آنها یک روز با من بر سر این موضوع جنگیدند، و سپس با آن موافقت کردند: شما نمی‌توانید سلاح اتمی بسازید یا خریداری کنید. بنابراین ما همه چیز را به دست آوردیم، اما رسانه‌ها آنقدر دیوانه‌وار پوشش می‌دهند.
‏مهم نیست من چه کار کنم، رسانه‌ها خواهند گفت این یک پیروزی بزرگ برای ایران بوده است.»</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5494" target="_blank">📅 16:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5493">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TToYB7p-k5qfizKiZ0I6Q7sCo0ghebnPkNmbOndnyPBgDQNnKClWpomlmapH4i55dvJVsU7y8yU-RxzPecrqAflvvN6SrKVon5vUPcZ27BjC-8Xd5mWNdSyf1dkaivdLYV8Fk5O5NtBSGtJiEwSQHCvEWdM9h5a9OVSsKVWoxWZIbs1238rjeIL50ckqe5BZa6zibJ7bwTPpAIhjBYEMOZ2A7-SAOimtiSXf-cCvWRKdwpG5qNxebB3esPbcv9D52NLjo67dpOYmoBhwPXHPq81jwPZNdY-J60R1vog9BZ01ZMo2GQVHCyZcpdqPDIhZZ_sWjCG9gNOlEi8s96Uvzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از انفجار در سیریک
مناطقی که در دو شب گذشته مورد حمله آمریکا بودند در واقع حاشیه تنگه هرمز هستند.
جایی که رادارها و سایت‌های موشکی و پهپادی و…برای کنترل تنگه ، متمرکز شده‌اند.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5493" target="_blank">📅 16:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWAgR8il0DaU_Ov5ixMAY3ZmcEtTCvJQSD5WnaGLkwX7Kvd8579xnBWaGp9GGyC9wkfjN9HVf_8jHLPf6w0zKXRYRsx6OqTcLhviVGTR7Vsw4t1q6ux1tZm4C2EM0B2VJZHNXylhaHf7HmHd_cRB6KTnK4KcWUObNRI9yzIUwyMu-LgotFDBAuIKqhvcaZsVa6Uu_PIVJng67ST325QmFZH_eOi0a2jESh9IIgdSw8jbj5qXYw8HufSClhi_XM0RJG0AN2Pvvic9wuddoO_ZIjfehQ4YgYtB7ro4qPhr--cTAfeuvaoYWKSWc2bYSzMLg4GDJ54eGHvu8xqf6e9Sug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اموال ملت ایران! که یا مصادره میشن
یا مفت فروشی میشن به چین
یا غارت و دزدیده میشن !
بقیه‌اش رو هم‌ میدن «مداحان»
و «رجز خوانان»!!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5492" target="_blank">📅 16:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDATcSiOZgspXOv4tCdeQxdECIbCnF4EXjL3kps75hVm2-cSJs74dYBYFUVl6Bvizaq3bRT59PlyxupvOoCcf8up1UIm-OCS0tjhFuVHw1fP83BGtlp7QFl3Jihd70wZdVRqS26jenWIoLggnw2eJvrW1EuTDZgeX9RUdIWpGpwu9HDd-3KkGkTkEuvDBLrdAvL9WUbfKEi0BdbSase_FeDLCDGVzLfJymthzjD-S7S4dmyVeXNCLnZjmwFbz8OkYL57NqHeWMAiIFF6I7moix8aGsXm6QWZZNdD_xXE53cjAiDoUv0Qv5qscpEH_yJiy3CQKpEeZCc3C_WYzPj1Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5491" target="_blank">📅 16:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dx8YvzLReniEkr9uAVTxW63sKdeaZ1acesjONv2JlddFs7sTON7DmkOkRNwMYLaDCvBPva0ElvNBSBhzd4EjTsPeyyyAx-V7e9_OGBpcMgySbJTK917qzZO0y2wJi2pyhfl01Z702C1XIgYV-0ow7iOJ4HmczCTygkLFIdxjfnKLgTWDVsdas3R2CW4zp9ytLX6TLXFjySefu4UIX2KJRU1JEycxIuLXHtdcMTJe4zVsAhu5LY0-HlOzbtmqS8D97gt7CmKQxoFAHVJsLQDb8yOD2uk1yqfHKtwiricvVRsMypmfQfLdJrDygSP834UY0_Ly3VU5IjJDPBwBJkSpmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5490" target="_blank">📅 16:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5489">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بیانیه ارتش اردن : شب گذشته ۲۰ موشک شلیک شده از سوی جمهوری اسلامی را رهگیری و منهدم کردیم.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5489" target="_blank">📅 15:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5488">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">بعد کار به جنگ ۱۲ روزه کشیده شد در ۲۳ خرداد ۱۴۰۴ ، که دو روز دیگه میشه سالگرد شروع این جنگ.  اسرائیل، آنگونه که نتانیاهو بعدها گفت،  انتظار داشت که در اولین موج‌های حمله چندین جنگنده‌اش توسط پدافندهای بومی و….. ج‌ا سرنگون بشه اما نشد! اسرائیل حدود ۱۰۰۰ سورتی…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5488" target="_blank">📅 10:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5487">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/itTw5fdEWZdjD1LumiGMLlxel7Q2WH0suIX8bGoVvY_TYIQDJHAkb7jd6kPtCgB-wbWc8cpc3GXkY5K6X9z9-qHIYn2LSwrI7ESAJC99WrVcadY4s6F1JLSm6Z7mPmvuFgnTTuPfXI49-Uq4Z4uwgZ4TmcAmTlf-YbxqTyXy7BdN8x7XPCErkt3QRWpHdKp3nAInrJESBChSAgKvFSsKTWpMuRLSiDW1Lkccyfx3fwgOQPnYTNGpxW9I6lXiS7d3_BNrXo4BmNumh4VS0nd7g94yoe3--l0YFmURwuJZdZ5hRC5B2sobPhiK5m6eF5HyDjS96TW5en2u4I1MHYqcbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پاسخ به حمله مستقیم جمهوری اسلامی  ۴ روز بعد اسرائیل حمله‌ای بسیار دقیق و هدفمند به ایران انجام داد.  گران‌بها‌ترین و مهم‌ترین سلاح دفاعی جمهوری اسلامی رو یعنی سامانه پدافند موشکی  اس ۳۰۰ رو که جمهوری اسلامی پس از حدود  ۲۰ سال تلاش و کشمکش از روسیه خریده…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5487" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/163555b294.mp4?token=XeqH2zZN_B3ikDhh1_s7qd-yM5fZz8-LnewRNUNxiEQ5DpS9ftAyMP7GTvgLtrdKWOIpFcTRjunMwCcjuVpkoyHU72Qr3nhB-FlUKDi_XN8bw9gtvIcn5M_uMVLqinbGFb04QGY_pjuBHwNeOLhVWgeoCqe27OQorYB2qzjr7DY3dhGwQ2t8jkno-pf4l36-rTUS5krWrAiV64hPICeQdkPkTt24ND6guLkh6yt-hM98MUe9ITR2jcr0M9A8nIT0leKSF2BfCZS79bSdggMo1MFhscxdNm6UgRUN7WvgFDz-zFUhcC5Fk08-eXlFkKBQPDoiyPQfWtLqd_vftUb51w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/163555b294.mp4?token=XeqH2zZN_B3ikDhh1_s7qd-yM5fZz8-LnewRNUNxiEQ5DpS9ftAyMP7GTvgLtrdKWOIpFcTRjunMwCcjuVpkoyHU72Qr3nhB-FlUKDi_XN8bw9gtvIcn5M_uMVLqinbGFb04QGY_pjuBHwNeOLhVWgeoCqe27OQorYB2qzjr7DY3dhGwQ2t8jkno-pf4l36-rTUS5krWrAiV64hPICeQdkPkTt24ND6guLkh6yt-hM98MUe9ITR2jcr0M9A8nIT0leKSF2BfCZS79bSdggMo1MFhscxdNm6UgRUN7WvgFDz-zFUhcC5Fk08-eXlFkKBQPDoiyPQfWtLqd_vftUb51w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی از ۲۵ فروردین ۱۴۰۳  رویارویی با اسرائیل را از جنگ نیابتی به یک جنگ مستقیم تبدیل کرد.  در عملیات «وعده صادق ۱» ج‌ا با ۱۷۰ پهپاد، ۱۲۰ موشک بالستیک  و ۳۰ موشک کروز به اسرائیل حمله کرد،  دستور حمله مستقیما از سوی علی خامنه‌ای صادر شد، و جالب اینکه…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5486" target="_blank">📅 10:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bglD49FnP4t20YODp--23ciFgWfoLJ9xgmDMxGIUIi37VRD1WIBVUKwMuEmqkS6n8j-jSHyTl85PSBvyeJUjueyB7-gd0MWZyMW4XgO3Y2eiNDVboLEDcFXW8toOIG6Z4ygZaBfyw854Gzcwi-Dos8GBVeXRQonxZixeNiMpUmyUSBrg1-oAHNKcXWzi_QuqOL8bD2pRqQtjTTU8p3GoOTMqDPYQLeAq248bgPIR2tVO7gdhxDrYhQKg2Q3cE3TNeaUXh-99nagm5mimeq4fBjWc5dxLpnabuClDRzobFJpWey1tENxj87rQpp3b-tr5YEizQJkBQzFQZngQoaYk2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ غیر مستقیم با اسرائیل سیاست  جمال عبدالناصر بود.  ناصر فشار سنگینی روی اردن و بعد لبنان آورد تا اجازه دهند، گروه‌های مسلح فلسطینی از مرزهای اردن و لبنان به اسرائیل حمله کنند.  اما مصر خودش چنین اجازه‌ای رو به فلسطینی‌ها نداد! نگذاشت مرزهاش با اسرائیل دچار…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5485" target="_blank">📅 10:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5484">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfm_VO30zU-FrCJAgE-uNr1Hyfow7Vs3C9cio1UObG-BP_UOLJeQDuNHwB-dTFeRPU7EVfBtc_Nobaur-LfXKPzf50sLUAPj3a2EqTYrnbSOzdJt_dNBt0frGwv2p0GlNfbz-U7tvdNdyKuo1tXbPN2k927mJoHJFBmz1pmBxNRgkOSq7zxfOCbkbq_OBLPFvg1yqqsgxipwqT76cDl3up4izH9naLgbFefw6C97qIsxSGBbOaxzfB5qPlFiQ_9KAn3CS5CyUa82XmkXXp4b_DILero3v7_WaCRpetQKzsyrfAlt48mdsBdxm7OIfeQVksLzuZxpqJ0gPAROszAFXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی در ۲۵ فروردین ۱۴۰۳  برای اولین بار رویارویی با اسرائیل را از یک جنگ و نبرد ده‌ها ساله «نیابتی»  به یک جنگ مستقیم کشوند.  تا قبل از این تاریخ،  جمهوری اسلامی با مسلح کردن گروه‌های تروریستی مثل حماس، جنبش اسلامی، حزب‌الله، حوثی‌ها و….. با اسرائیل…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5484" target="_blank">📅 10:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNBzFo1Os9qlDzzlWQm0SHc_eNYqmjW5adEHFNFVtOLPmWiwIdCJJK4IuKCcxKZ7qxydatV2JezrJN6c-G6h6Z-fQ6RUpH-EKp5StLUhAsaqgVZVTKOXdHOHiVqyiRgsSPiQIYAs4YvHmH5yqoZDc4BM4hvSdpJwjryyqN0sS5WuFmqTINnfm2f9gjXXL6MDYcwLqxzkapoSyNi8hQ6fosMXUAWjnLSrDLt1FIE8iutmLRMc7IZ7ZNLn58wsAEEjaEJAddD4d45jCA8xKelCowo-SBKTZbdbbNS8dBr4FSzLZmufOD9yvU2J00nuoUdr0W-W7wH0KeHjksOw_yVeDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از مهم‌ترین پیش‌شرط‌های جمهوری اسلامی در دوره جنگ ۴۰ روزه این بود  که «جنگ باید کامل تموم بشه»  و آمریکا باید تعهد بده که دیگه به ایران حمله نکنه.  منظورش این بود که یک «آتش‌بس» نمیخوایم! «توقف کامل جنگ رو میخوایم»!  این‌ درخواست از اونجایی میاد  که جمهوری…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5483" target="_blank">📅 10:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5482">
<div class="tg-post-header">📌 پیام #1</div>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
